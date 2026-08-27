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
