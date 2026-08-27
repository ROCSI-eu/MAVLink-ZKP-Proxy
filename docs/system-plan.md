# System Architecture and Delivery Plan

**Document status:** proposed baseline

**Repository maturity:** documentation only

**Audience:** engineering, security, product, operations, and technical reviewers

## 1. Purpose and success criteria

The system will accept selected MAVLink telemetry and produce independently verifiable, privacy-preserving policy claims. It should disclose no more information than the policy requires and retain enough metadata to investigate failures without treating a blockchain transaction as proof that source telemetry was truthful.

The first implementation is successful when a deterministic simulation demonstrates this sequence:

1. a bridge receives MAVLink 2 telemetry from one SITL vehicle;
2. the bridge validates framing, records trust status, and normalizes supported messages;
3. a worker generates a speed-policy proof from a versioned record;
4. a separate verifier accepts valid proofs and rejects altered inputs, stale records, and replays;
5. a mock chain adapter records the proof digest and lifecycle state; and
6. an operator can observe status without receiving exact coordinates.

Target service-level objectives are hypotheses until Phase 1 benchmarks establish baselines. For the vertical slice, measure p50/p95/p99 ingress-to-verification latency, proofs per second, memory per proving worker, dropped-frame rate, and proof failure rate; do not claim “real-time” behavior without an explicit deadline and evidence.

## 2. Scope

### 2.1 In scope for the minimum viable system

- MAVLink 2 ingestion from ArduPilot or PX4 SITL over UDP.
- An allowlist of message types required by the selected claim.
- Explicit distinction between authenticated and untrusted MAVLink sources.
- Canonical, versioned telemetry records with provenance and replay fields.
- One bounded speed proof, local verification, and deterministic fixtures.
- A chain-adapter interface and an offline mock implementation.
- Redacted operator status and an append-only audit event model.
- A single vehicle and a single operator role in a local environment.

### 2.2 Deferred

- Geofence polygon proofs, aggregation, recursion, and proof batching.
- Multiple vehicles, policy orchestration, and fleet-level coordination.
- Live Midnight deployment and production token/economic design.
- High availability, Kubernetes, and multi-region disaster recovery.
- Raw log/object storage and historical analytics beyond test evidence.
- Hardware-backed attestation and production key ceremonies.

### 2.3 Explicit non-goals

- Flight control, navigation, collision avoidance, or autonomous command authorization.
- Byzantine consensus between aircraft or a guarantee of continued operation after disconnection.
- Proving physical sensor truth, vehicle airworthiness, or operator identity solely with a ZK proof.
- Storing raw, high-rate telemetry on a public ledger.
- Supporting every MAVLink dialect or transport in the first release.
- Certification for safety-critical, defense, or regulated deployment.

## 3. Operating assumptions and constraints

- SITL is the only supported source until a hardware test plan is approved.
- UDP is acceptable for local simulation but supplies neither confidentiality nor delivery guarantees.
- MAVLink 2 signing can authenticate frames when provisioned correctly; unsigned frames must remain visibly untrusted and must not silently become eligible for compliance claims.
- Wall-clock time is not inherently trustworthy. Recency claims require a defined clock authority, maximum skew, monotonic sequence data, and verifier policy.
- A chain can timestamp submission and make records durable; it does not make off-chain telemetry accurate.
- Precise telemetry, identifiers, salts, signing keys, witnesses, and proving material are sensitive assets.
- Midnight SDK and contract compatibility, disclosure semantics, fees, finality, and supported proof verification must be proven by a time-boxed spike before production architecture is committed.

## 4. Architecture and responsibilities

| Component | Owns | Must not own |
| --- | --- | --- |
| MAVLink bridge | Transport adapters, frame parsing, allowlist, signature/trust result, normalization, sequence-gap metrics | Policy decisions, proof keys, chain submission |
| Policy/proof worker | Policy lookup, witness construction, proof generation, sensitive-input lifecycle | MAVLink parsing, operator authorization, direct chain access |
| Verifier | Public-input reconstruction, proof verification, replay/expiry checks, verification result | Private witness access |
| Chain adapter | Idempotent submission, network translation, transaction/finality state, mock/live implementations | Raw telemetry or private witness storage |
| Operator API/UI | Authentication, authorization, redaction, live status, audit queries | Direct access to bridge sockets or proving keys |
| Metadata store | Policies, proof lifecycle, audit events, idempotency records | Raw telemetry by default |

### 4.1 Data flow

1. The bridge receives a frame and captures `received_at`, peer, MAVLink system/component IDs, sequence number, signature result, and parser result.
2. Supported messages update a short-lived per-source snapshot. The bridge emits a record only when required values satisfy freshness and source-consistency rules.
3. The proof worker fetches an immutable policy by digest, constructs the witness, and deletes witness material after proof generation.
4. The verifier reconstructs public inputs, checks proof validity, age, policy status, and nullifier uniqueness.
5. The adapter submits an idempotency key and approved public metadata to a mock or live backend.
6. Lifecycle events (`received`, `proved`, `verified`, `submitted`, `finalized`, `failed`) are append-only and safe for the intended audience.

Backpressure must be bounded at each queue. The initial policy is **drop oldest unproved telemetry while emitting a metric and audit event**; flight traffic must never wait on proof or chain latency.

### 4.2 Trust boundaries

```text
[untrusted network / SITL]
          | MAVLink frame
          v
[bridge boundary] -- canonical record --> [sensitive proving boundary]
          |                                      |
          | redacted event                       | proof + public inputs
          v                                      v
[operator boundary] <--- status -------- [verification boundary]
                                                |
                                                | approved metadata only
                                                v
                                      [external chain boundary]
```

Production deployment should isolate the proving worker, disable outbound access except to required dependencies, mount keys read-only from a secrets provider, and ensure logs cannot serialize witnesses.

## 5. Canonical data contract

JSON is an edge/debug representation, not the canonical proof encoding. The implementation must define a Protobuf schema and a deterministic byte-to-field mapping before circuit work begins. Floating-point values are prohibited in proof inputs.

Example normalized record (valid JSON):

```json
{
  "schema_version": 1,
  "record_id": "0191d7c8-632f-7f3d-a5ad-2dcbe4223d24",
  "source": {
    "system_id": 23,
    "component_id": 1,
    "trust": "signed_valid",
    "message_ids": [33, 74]
  },
  "observed_at_unix_ms": 1712345678000,
  "received_at_unix_ms": 1712345678120,
  "position": {
    "latitude_deg_e7": 513456789,
    "longitude_deg_e7": -113456789,
    "relative_altitude_mm": 54500
  },
  "ground_speed_cm_s": 125,
  "policy_digest": "sha256:0123456789abcdef...",
  "nonce": "base64url-128-bit-random-value"
}
```

Message ID 33 (`GLOBAL_POSITION_INT`) supplies scaled position fields; message ID 74 (`VFR_HUD`) can supply groundspeed. The bridge must document autopilot/dialect differences and reject unit overflows rather than coerce them.

### 5.1 Speed-policy statement (first circuit)

**Private witness**

- normalized horizontal speed;
- source pseudonym/commitment opening;
- record nonce and commitment opening;
- any private policy parameters explicitly approved by the threat model.

**Public inputs**

- schema and circuit version;
- policy digest and public maximum speed;
- approved time-window identifier (not necessarily an exact timestamp);
- record commitment;
- domain-separated nullifier;
- pass claim encoded by successful verification.

**Constraints**

- speed is represented as a non-negative, range-constrained integer in cm/s;
- `speed <= maximum_speed` is enforced in-circuit;
- the record commitment binds every field required by the statement;
- the nullifier binds the deployment domain, policy, source pseudonym, and nonce;
- encodings, endianness, field reductions, hash parameters, and domain-separation tags are fixed in a versioned specification.

Recency cannot be proven from an untrusted timestamp alone. The verifier checks the approved window and clock policy outside the circuit unless a trusted time attestation is introduced.

### 5.2 Data classification and retention

| Class | Examples | Default handling |
| --- | --- | --- |
| Secret | signing/proving keys, witness, salts | Secrets manager or memory only; never logs; zeroize where practical |
| Restricted | exact location, stable vehicle identity, raw MAVLink logs | Do not persist in MVP; role-restricted if later approved |
| Internal | policy configuration, failure diagnostics | Authenticated access; retention set by owner |
| Shareable | circuit version, proof digest, transaction state | May enter audit/chain record after review |

Before production, product and privacy owners must define jurisdiction, lawful purpose, data subject handling, deletion requirements, and concrete retention periods. “Hashing” a stable identifier is pseudonymization, not anonymization.

## 6. Technology strategy

Selections below are directions to validate, not statements about implemented software.

| Concern | Default candidate | Decision gate |
| --- | --- | --- |
| Bridge and services | Rust workspace with Tokio and a maintained MAVLink library | Parse/signature compatibility against both target SITLs; fuzz and throughput results |
| Contracts | Protobuf with Buf; tonic gRPC internally | Schema compatibility test and generated-client ergonomics |
| UI boundary | HTTP for queries, WebSocket or SSE for lifecycle events | Auth/redaction design review |
| Operator UI | TypeScript + React + Vite | Only after API vertical slice; accessibility baseline required |
| Proof system | Rust-native candidates and Midnight-compatible approach | ADR comparing verification target, setup, proof size, latency, memory, auditability, licensing |
| Chain integration | Port/interface with deterministic mock, then supported Midnight SDK/contract stack | Compatibility spike on a pinned network/SDK release |
| Metadata | PostgreSQL when lifecycle persistence becomes necessary | Migration/backup/retention design |
| Telemetry/event transport | In-process bounded channels first | Introduce NATS only when measured scaling or isolation requires it |
| Observability | Structured logs, Prometheus metrics, OpenTelemetry traces | Privacy review of attributes and cardinality test |

Avoid premature dependencies: Redis, object storage, NATS, Kubernetes, and separate deployable services are not MVP requirements. Begin as a modular monolith or small workspace with ports that preserve later extraction boundaries.

### 6.1 Proposed source layout

```text
crates/
  domain/             # dependency-light records, policies, state machine
  mavlink-bridge/     # transport and normalization adapters
  prover/             # witness construction and proof backend port
  verifier/           # verification and replay policy
  chain-adapter/      # trait, mock, and later Midnight implementation
  api/                # authenticated/redacted external boundary
proto/                # versioned service contracts
fixtures/             # synthetic, non-sensitive replay data
docs/adr/              # architecture decision records
deploy/compose/        # local integration only when services exist
```

Dependencies should point inward to `domain`; external SDK types must not cross adapter boundaries.

## 7. Security and privacy model

### 7.1 Assets and actors

Assets include exact telemetry, mission association, identity mappings, policy definitions, signing keys, proving/verifying material, audit integrity, and service availability. Actors include the vehicle/SITL, operator, verifier/relying party, administrator, external network, and a potentially malicious telemetry sender or compromised service.

### 7.2 Priority threats and required controls

| Threat | Initial controls | Validation |
| --- | --- | --- |
| Forged or unsigned telemetry | MAVLink 2 signing where supported; explicit trust enum; policy rejects ineligible trust states | Negative integration fixtures |
| Replay or duplicate submission | Sequence tracking, nonce/nullifier, bounded time window, durable uniqueness constraint, idempotency key | Replay tests and restart test |
| Malformed-frame parser exploit | Allowlist, length/range checks, dependency review, fuzzing, resource limits | Continuous fuzz target/corpus |
| Witness leakage | Process isolation, log denylist, memory lifecycle, crash-dump policy, least privilege | Log snapshot and failure-injection tests |
| Correlation through public inputs | Rotating/domain-specific pseudonyms, coarse windows, minimal metadata | Privacy review against example observer attacks |
| Compromised policy or verifier key | Signed/versioned policy, digest pinning, separation of duties, rotation procedure | Rotation and rollback exercise |
| Chain outage or reorganization | Local verification independent of chain; retry state machine; finality states; bounded queue | Fault-injection test |
| Denial of service/prover exhaustion | Admission control, per-source quotas, bounded queues, cancellation, metrics | Load test with an explicit overload criterion |

Authorization starts with two roles: `operator` can view redacted status; `auditor` can view approved proof metadata. Administrative policy/key actions require a separately designed role and audit path. Authentication technology is an ADR; “use JWT” alone is not an authorization design.

### 7.3 Safety rule

The proxy is observational in the MVP. No verifier, chain event, dashboard action, or failure mode may write MAVLink commands back to a vehicle. Any future command path requires a separate hazard analysis, authorization protocol, fail-safe behavior, and review by relevant safety experts.

## 8. API and lifecycle semantics

The Protobuf contract is authoritative. An HTTP gateway may expose equivalent operations:

- `POST /v1/proofs:speed` accepts a record reference, policy version, and idempotency key; it does not accept arbitrary raw witness fields from browser clients.
- `GET /v1/proofs/{proof_id}` returns redacted lifecycle state.
- `GET /v1/events` streams authorized state transitions.
- health endpoints distinguish liveness from dependency readiness.

Proof lifecycle is monotonic except for retry metadata:

```text
RECEIVED -> PROVING -> PROVED -> VERIFIED -> SUBMITTED -> FINALIZED
                  \-> FAILED     \-> REJECTED     \-> SUBMISSION_FAILED
```

Every request carries a correlation ID; mutations require an idempotency key. Error responses use stable machine-readable codes and never include private input. Contract versions follow additive compatibility rules; breaking changes require a new major namespace and migration plan.

## 9. Delivery phases and gates

### Phase 0 — decision closure and scaffold

**Deliverables:** workspace, formatter/linter/test CI, dependency policy, ADR template, canonical Protobuf draft, synthetic fixtures, initial threat model.

**Exit gate:** clean checkout runs one documented command for formatting, linting, tests, and schema checks; owners approve public/private fields; no unresolved critical threat blocks the vertical slice.

### Phase 1 — telemetry vertical slice

**Deliverables:** SITL setup, allowlisted parser, trust status, normalizer, bounded channel, record/replay tool, metrics.

**Exit gate:** a pinned SITL scenario produces deterministic canonical records; malformed and unsupported frames are rejected; sequence gaps and overload drops are observable; parser fuzz target runs in CI or scheduled automation.

### Phase 2 — proof spike and local verification

**Deliverables:** benchmark harness, speed circuit, deterministic vectors, verifier, proof-system ADR, key/version lifecycle draft.

**Exit gate:** valid, boundary, altered-input, stale, and replay cases pass; constraint tests cover min/max/overflow; benchmark report records hardware and p50/p95/p99; independent verifier code does not receive witness data.

### Phase 3 — adapter and operator API

**Deliverables:** chain port, deterministic mock, lifecycle persistence, authenticated/redacted endpoints, minimal status UI.

**Exit gate:** the complete fixture reaches `FINALIZED` against the mock; duplicate requests do not duplicate records; outage/retry/restart tests pass; UI and logs expose no restricted fields.

### Phase 4 — Midnight compatibility test environment

**Entry gate:** supported SDK, network, contract language, proof verification route, expected costs, and finality semantics are documented in an ADR.

**Deliverables:** pinned adapter, test-environment contract, transaction watcher, reconciliation job, key runbook.

**Exit gate:** submit/retry/finality/reorganization scenarios are evidenced; public metadata matches privacy review; secrets rotation and rollback are exercised; live and mock implementations pass the same contract suite.

### Phase 5 — hardening and controlled pilot

**Deliverables:** performance envelope, dependency/SBOM and image scanning, backup/restore evidence, incident runbooks, external security review, privacy assessment, controlled hardware test plan.

**Exit gate:** service objectives and capacity limits are approved; high-severity findings are resolved or explicitly accepted by an accountable owner; rollback, restore, key rotation, overload, and dependency-outage exercises pass.

No phase exit is based solely on code completion. Evidence links, accountable approvers, and residual risks belong in the milestone record.

## 10. Testing and quality strategy

- **Unit/property tests:** unit conversions, ranges, snapshot freshness, lifecycle invariants, canonical encoding, circuit boundaries.
- **Negative tests:** invalid signatures, stale/mixed-source snapshots, malformed lengths, duplicate nullifiers, wrong policy/version, altered public inputs.
- **Contract tests:** generated clients and both chain adapters against the same Protobuf and state-transition suite.
- **Integration tests:** pinned SITL or recorded synthetic fixtures; no external network required for the default CI path.
- **Fuzzing:** MAVLink ingress, canonical decoder, API boundary, and proof/public-input decoder.
- **Performance tests:** benchmark proving separately from ingestion and end-to-end latency; publish machine configuration and queue settings.
- **Security tests:** dependency audit, secret scanning, SBOM, container scan, authorization matrix, and log-redaction assertions.
- **Resilience tests:** process restart, database unavailable, chain timeout/reorganization, corrupt artifact, clock skew, and overload.

Fixtures must be synthetic or reviewed for redistribution. Randomized tests must print reproducible seeds. Cryptographic vectors and schema golden files are version controlled.

## 11. Operations baseline

Local development should be reproducible with pinned toolchains and, once dependencies exist, a minimal Compose profile. Production topology follows measured needs; Kubernetes is not a default requirement.

Required signals include:

- counters for frames received/rejected/dropped and proofs by outcome;
- histograms for queue wait, proving, verification, submission, and end-to-end latency;
- gauges for bounded queue depth and adapter backlog;
- traces joined by opaque correlation IDs, never stable vehicle IDs; and
- alerts tied to user-visible symptoms and runbooks.

Initial recovery objectives, availability targets, retention durations, and alert thresholds remain **TBD by the service owner** after Phase 1/2 measurements. Production readiness requires explicit values rather than generic claims of scalability or fault tolerance.

## 12. Decision and ownership register

| Decision | Needed by | Accountable role | Required evidence |
| --- | --- | --- | --- |
| Autopilot, dialect, and signed-message profile | Phase 1 start | Telemetry lead | SITL compatibility matrix |
| Canonical encoding and snapshot freshness | Phase 1 start | Architecture + security | Schema review and golden vectors |
| Proof system and circuit toolchain | Phase 2 exit | Cryptography lead | Benchmark/compatibility ADR and review |
| Trusted time and replay policy | Phase 2 exit | Security lead | Threat analysis and negative tests |
| Midnight SDK/contract integration | Phase 4 entry | Chain lead | Executable spike and cost/finality notes |
| Data purpose and retention | Phase 3 exit | Product/privacy owner | Data inventory and retention schedule |
| SLOs and production topology | Phase 5 entry | Service owner/SRE | Load results and capacity model |
| Hardware pilot safety case | Before hardware connection | Safety owner | Hazard analysis and approved test plan |

Names replace roles when a team is staffed. A decision is not closed until its ADR records context, options, outcome, consequences, owner, date, and evidence.

## 13. Principal risks

| Risk | Consequence | Near-term response |
| --- | --- | --- |
| Proof verification cannot be implemented economically or natively on the target chain | Architecture rework | Phase 2/4 compatibility spikes before production build-out |
| Source telemetry is unauthenticated or compromised | Valid proof of false input | Preserve trust state; require eligible signing/attestation policy |
| Proving latency exceeds telemetry rate | Unbounded backlog or stale claims | Benchmark, bounded queues, sampling/batching only after semantics review |
| Public metadata permits vehicle correlation | Privacy objective fails | Minimize inputs, rotate pseudonyms/nullifiers, observer-focused privacy review |
| SDK/network interfaces change | Integration instability | Pin versions behind adapter, contract tests, documented upgrade policy |
| Scope expands into flight control | Safety and liability exposure | Enforce observational boundary and separate governance for commands |

## 14. Documentation maintenance

This plan is the architectural baseline, not a promise that each candidate will ship. Update it when scope or boundaries change. Record irreversible or contested decisions in `docs/adr/`. Each release should publish supported versions, schema/circuit identifiers, migrations, known limitations, security contact, and operational runbooks.
