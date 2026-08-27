# Proposed architecture

| Metadata | Value |
| --- | --- |
| Status | Proposed; no components are implemented |
| Audience | Engineering, platform, security, cryptography, and operations |
| Accountable role | Architecture lead |
| Review trigger | Component, dependency, data-flow, trust-boundary, lifecycle, or failure-policy change |
| Authority | Normative boundaries/invariants; diagrams, APIs, technology and source layout are illustrative |

## Context and principles

The system accepts selected telemetry from one SITL source, constructs a versioned private witness, verifies a bounded-speed proof independently, and records only approved metadata through a mock chain boundary. Dependencies point inward to a dependency-light domain model. External telemetry, proving, persistence, UI, and Midnight SDK types MUST remain behind adapters.

Begin as a modular process or small workspace. Separate deployment units, brokers, caches, object storage, and orchestration require measured isolation or scaling needs.

```text
[untrusted SITL/UDP]
        |
        v
[MAVLink bridge] -> [proof worker] -> [verifier] -> [chain adapter/mock]
        |                                  |
        +------ [redacted operator API/UI]-+
                         |
                  [metadata/audit port]
```

## Component responsibilities

| Component | Owns | Must not own |
| --- | --- | --- |
| MAVLink bridge | Transport, frame parsing, allowlist, signature result, trust classification, normalization, sequence-gap metrics | Policy decisions, proof keys, chain submission |
| Proof worker | Immutable policy lookup, witness construction, proof generation, sensitive-input lifecycle | MAVLink parsing, operator authorization, direct chain access |
| Verifier | Public-input reconstruction, proof verification, expiry and replay policy, verification result | Private witness access |
| Chain adapter | Idempotent submission, external translation, mock/live implementations, transaction/finality state | Raw telemetry or witness storage |
| Operator API/UI | Authentication/authorization boundary, redaction, lifecycle views, audit queries | Bridge sockets, private inputs, proving keys |
| Metadata/audit port | Policies, lifecycle events, idempotency and uniqueness records | Raw telemetry by default |

These are logical components, not a requirement for multiple services.

## Trust boundaries and data flow

1. The bridge captures peer metadata, system/component IDs, sequence, parser result, signature result, and receive time.
2. Allowlisted messages update one short-lived source snapshot. A record is emitted only when freshness and source-consistency rules pass.
3. The proof worker obtains an immutable policy by digest, constructs the witness, and releases sensitive material after proving.
4. The verifier reconstructs public inputs and checks proof validity, accepted versions, policy status, expiry policy, and nullifier uniqueness.
5. Only after verification, the adapter submits an idempotency key and approved public metadata.
6. The operator boundary receives redacted state; it never receives exact coordinates or witness material.

SITL/UDP, proving, verification, operator, persistence, and external-chain boundaries have distinct trust. Chain durability says nothing about source truth. Verification MUST NOT trust a prover-supplied interpretation of public inputs.

## Architectural invariants

- The MVP is observational: no component emits vehicle commands.
- Untrusted input remains labeled; trust cannot be upgraded without validated authentication evidence.
- The verifier has no witness access and independently reconstructs public inputs.
- Raw telemetry, exact position, stable identity, salts, and witnesses do not cross the chain or operator boundary.
- Default CI and local verification do not require an external network.
- Queues are bounded; telemetry ingestion never waits on proving or chain latency.
- Schema, circuit, policy, commitment, and domain-separation versions are explicit.
- State mutations are idempotent and lifecycle transitions are auditable.

## Deployment modes

Deployment placement does not change the data-minimization invariant. The **approved proving boundary** is the host, enclave, or customer-controlled network segment authorized to ingest raw telemetry and construct a witness. Raw telemetry, exact position, stable source identity, salts/openings, and witnesses MUST remain inside that boundary in every mode. Only the proof, explicitly reviewed public inputs, opaque correlation/idempotency identifiers, redacted lifecycle events, and approved aggregate operational signals may leave it. A verifier is always outside the proving trust boundary and MUST be able to reconstruct public inputs and validate a proof without telemetry, witness access, or a call to a vendor service.

### Local developer

```text
[untrusted SITL/UDP] -> | developer workstation: bridge + prover | -> | local verifier + mock adapter |
                              approved proving boundary                    separate logical trust
```

| Concern | Definition |
| --- | --- |
| Trust boundaries and crossing data | Untrusted UDP crosses into the workstation with MAVLink frames and peer metadata. The logical prover-to-verifier boundary carries only the proof, reviewed public inputs, version/policy identifiers, and opaque request identifiers; the mock receives only approved public metadata. Process separation SHOULD be used to exercise the boundary even when all components share one host. |
| Key ownership | The developer owns disposable source-signing and proving keys. Test verification keys/parameters are pinned repository artifacts or locally generated fixtures; production keys MUST NOT be used. |
| Connectivity | Loopback or a controlled local network is sufficient. Fixture proving, verification, lifecycle inspection, and mock submission MUST work with external networking disabled. |
| Updates | The developer updates the pinned workspace, fixtures, circuit artifacts, and local configuration; incompatible versions fail before processing. |
| Failure behavior | Loss of SITL stops new records; prover or mock failure produces an explicit local state without blocking ingestion. Restart may discard non-durable development state, but MUST NOT leak restricted values or turn a failed verification into success. |

### Edge agent plus managed control plane

```text
[vehicle/SITL] -> | customer edge: bridge + prover | -> | managed control plane: verifier + API + adapter |
                        approved proving boundary              vendor-operated trust boundary
```

| Concern | Definition |
| --- | --- |
| Trust boundaries and crossing data | Raw MAVLink enters only the customer-approved edge boundary. Across the customer/vendor boundary, the agent sends mutually authenticated envelopes containing proofs, reviewed public inputs, version/policy identifiers, opaque correlation/idempotency identifiers, and redacted health/lifecycle signals. Policy bundles, verification artifacts, revocation state, and update metadata cross toward the edge; raw telemetry and witnesses never do. |
| Key ownership | The customer owns source-authentication keys and authorizes the edge identity. Proving keys remain on the edge and are customer-owned or customer-authorized; the managed operator owns service transport/API keys. Verification material is public, version-pinned, and independently exportable. |
| Connectivity | Telemetry ingestion and proving tolerate loss of the vendor link using a bounded encrypted outbox containing only permitted boundary outputs. Submission and managed status are eventually connected; inbound vehicle-network access from the control plane is neither required nor allowed. |
| Updates | The vendor publishes signed agent, policy, circuit, and verifier compatibility metadata and operates control-plane rollout/rollback. The customer approves and schedules edge installation and key rotation; the agent rejects unsigned, revoked, or incompatible updates. |
| Failure behavior | A control-plane outage does not stop bounded local ingestion/proving or erase locally determined results. Outbox overflow follows configured drop/fail-closed policy with redacted audit evidence. Expired policy/revocation material, invalid proofs, and version mismatch fail closed; reconnect drains permitted artifacts idempotently. |

### Fully customer-managed

```text
[vehicle/SITL] -> | customer proving segment: bridge + prover | -> | customer service segment: verifier + API + adapter |
                       approved proving boundary                         separate customer trust boundary
```

| Concern | Definition |
| --- | --- |
| Trust boundaries and crossing data | The customer defines network and administrative separation between the proving segment and verifier/service segment. Only proofs, reviewed public inputs, version/policy identifiers, opaque identifiers, and redacted signals cross it; any chain boundary receives only approved public metadata. No operational data path to the vendor is required. |
| Key ownership | The customer generates, stores, rotates, backs up, and revokes source, proving, transport, operator, and submission keys. Verification keys/parameters may be obtained as signed public artifacts and are pinned and auditable by the customer. |
| Connectivity | Private networking is sufficient. All runtime components, verification, policy resolution, audit, and optional mock submission operate without vendor network or credentials; external-chain connectivity is required only when the customer enables live submission. |
| Updates | The customer owns artifact validation, compatibility testing, maintenance windows, rollout, rollback, migrations, and incident response. The vendor may publish signed releases and advisories but has no deployment access or automatic-update dependency. |
| Failure behavior | Private-network partitions isolate stages: the prover retains only a bounded queue of permitted outputs, while verification and local audit continue for available artifacts. Vendor unavailability has no runtime effect. Customer persistence or chain failures are explicit and reconcile idempotently; unsupported or stale security material fails closed. |

### Independent relying-party verifier

```text
| any approved proving deployment | -> proof package -> | relying-party verifier |
        approved proving boundary                         independent trust boundary
```

| Concern | Definition |
| --- | --- |
| Trust boundaries and crossing data | A prover or distribution channel supplies a self-contained package with the proof, canonical reviewed public inputs, policy/circuit/schema and domain identifiers, required public verification artifacts or immutable references, and optional approved submission receipt. It supplies no raw telemetry, stable identity, salt/opening, or witness. The relying party trusts neither the prover's interpretation nor a vendor verdict. |
| Key ownership | The original operator retains source and proving keys. The relying party owns its trust store and policy/version allowlist and pins authenticated public verification keys/parameters; no vendor-held secret or credential is necessary. |
| Connectivity | Verification MUST run offline after approved artifacts and revocation/status snapshots have been imported. Vendor DNS, API, telemetry, license, and control-plane access are not verification dependencies; fetching chain state is optional and separately reported. |
| Updates | Artifact publishers sign and version circuit, schema, policy, verification, and revocation material. The relying party decides when to import it, validates provenance and compatibility, retains evidence for the decision epoch, and can roll back its local verifier according to policy. |
| Failure behavior | Missing, unauthenticated, revoked, expired, or incompatible artifacts yield an explicit indeterminate/rejected result, never an online fallback or acceptance. Network loss has no effect on a complete package. Receipt or chain lookup failure is reported separately and does not rewrite the cryptographic verification result. |

## Lifecycle and API direction

Normative lifecycle states are:

```text
RECEIVED -> PROVING -> PROVED -> VERIFIED -> SUBMITTED -> FINALIZED
                  \-> FAILED     \-> REJECTED     \-> SUBMISSION_FAILED
```

Transitions are monotonic; retries add attempt metadata rather than moving finalized state backward. Error output MUST use stable codes and exclude restricted data. Mutations require idempotency keys and requests use opaque correlation IDs.

Illustrative API operations are a proof request by record reference and policy version, a redacted proof-status query, and an authorized lifecycle-event stream. Contract format (including Protobuf/gRPC, HTTP, SSE, or WebSocket) is **Open**, not an implemented commitment.

## Failure and backpressure behavior

- When a bounded ingress-to-proof queue is full, drop the oldest unproved record, increment a metric, and append a redacted audit event.
- Parser, proof, verification, persistence, and adapter failures are explicit terminal or retryable states; they never suppress ingestion silently.
- Chain failure does not invalidate local verification. Retries are bounded and idempotent; finality is represented, not assumed.
- Restart recovery MUST preserve uniqueness and prevent duplicate submission once persistence is introduced.
- Clock skew, stale mixed snapshots, malformed data, and unsupported versions fail closed for claim eligibility.

Queue sizes, retry budgets, expiry windows, and overload thresholds are **Open** pending benchmarks and threat review.

## Proposed technology and layout

Rust/Tokio, a maintained MAVLink library, Protobuf/gRPC, React/Vite, PostgreSQL, OpenTelemetry, and proof-system candidates are evaluation directions only. A Midnight adapter and deterministic mock are proposed; exact SDK, contract language, proof-verification route, fees, and finality semantics require a compatibility spike. NATS, Redis, object storage, Kubernetes, and multiple deployables are not MVP requirements.

A possible implementation layout is `domain`, `mavlink-bridge`, `prover`, `verifier`, `chain-adapter`, and `api` modules plus `fixtures` and versioned contracts. Phase 0 may change this via an ADR.

## Acceptance, open decisions, and related documents

Validate boundaries with dependency checks, contract tests, data-flow review, restart/overload tests, and confirmation that no command path or restricted-field serialization exists. Open architecture decisions are tracked in [decisions](decisions.md). Proof semantics are in [data and proof model](data-and-proof-model.md), controls in [security and privacy](security-and-privacy.md), and phase evidence in the [delivery plan](delivery-plan.md).
