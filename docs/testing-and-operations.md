# Testing and operations

| Metadata | Value |
| --- | --- |
| Status | Proposed quality and readiness baseline; SLOs are Open |
| Audience | Engineering, cryptography, security, platform, QA, and operations |
| Accountable role | Service owner/SRE, with discipline leads for specialized evidence |
| Review trigger | Interface, threat, circuit, deployment, SLO, retention, or failure-mode change |
| Authority | Normative evidence categories and readiness gates; tooling/topology examples are illustrative |

## Test layers

- **Unit/property:** conversions, ranges, freshness, trust eligibility, lifecycle invariants, canonical encoding, circuit boundaries.
- **Negative:** invalid/unsigned signatures as policy dictates, stale/mixed snapshots, malformed lengths, overflow, duplicate nullifiers, wrong policy/version/domain, altered public inputs.
- **Golden/cryptographic:** deterministic cross-implementation schema, commitment, nullifier, proof, and verification vectors, including equality at the speed bound.
- **Contract:** clients and mock/live adapters against identical version and state-transition suites.
- **Integration:** pinned SITL or synthetic replay with no external-network requirement in default CI.
- **Fuzz:** MAVLink parser, canonical decoder, public API decoder, and proof/public-input decoder; corpus and regressions retained.
- **Security/privacy:** dependencies, secrets, authorization matrix, log/trace/UI redaction, public-metadata review, key rotation and rollback.
- **Resilience:** restart, persistence unavailable, chain timeout/reorganization, corrupt artifact, clock skew, queue overload, and cancellation.

Fixtures MUST be synthetic or approved for redistribution. Randomized failures print reproducible seeds. Test output must not contain restricted or secret data.

## Benchmark methodology

Measure ingestion, queue wait, proving, verification, submission, and end-to-end stages separately. Reports state commit, schema/circuit/policy version, proof parameters, machine CPU/memory, operating system, concurrency, queue settings, fixture, warm-up, sample count, and p50/p95/p99 where meaningful. Record proofs/second, peak memory per worker, dropped-frame rate, proof size, and failure rate.

No “real-time,” scalable, fault-tolerant, or capacity claim is permitted without an explicit workload, deadline/criterion, repeatable method, and result. Thresholds and regression budgets are **TBD by the service owner** after Phase 1/2 baselines.

## Observability and privacy

Required signals are counters for received/rejected/dropped frames and proof outcomes; histograms for queue/proving/verification/submission/end-to-end duration; bounded-queue/backlog gauges; and lifecycle/finality health. Opaque correlation IDs join signals. Stable vehicle IDs, exact telemetry, witnesses, keys, salts, and unreviewed public inputs MUST NOT appear in logs, traces, metrics labels, crash artifacts, or alerts.

Alerts must correspond to user-visible symptoms or safety/security controls and link to an owned runbook once operations begin. Alert thresholds remain Open until baselines exist; high-cardinality attributes require review.

## Deployment progression and resilience

1. Offline deterministic fixture and in-process/mock dependencies.
2. Local SITL integration in a controlled network.
3. Midnight test environment only after the Phase 4 entry ADR.
4. Controlled hardware pilot only after privacy, security, operational, and safety evidence.
5. Production is a separate approval, not an automatic phase outcome.

A minimal local Compose profile may be added when dependencies exist. PostgreSQL, separate services, containers, OpenTelemetry tooling, and UI infrastructure remain proposed. Kubernetes, Redis, NATS, object storage, high availability, and multi-region recovery require demonstrated needs.

Backups/restores apply only when durable state is introduced. Retry, reconciliation, restart, overload, dependency outage, and corrupt-state behavior must be exercised before their corresponding environment gate.

## Deployment-mode acceptance checks

Every supported mode MUST have reproducible evidence for its applicable checks. Packet captures, logs, traces, crash artifacts, queues, and persisted records used as evidence MUST be inspected to confirm that raw telemetry, exact position, stable identity, salts/openings, and witnesses remain inside the approved proving boundary.

| Mode | Required acceptance evidence |
| --- | --- |
| Local developer | Run the pinned synthetic fixture, proof generation, independent verification, lifecycle query, and mock submission with external network access denied. Confirm only reviewed public inputs and redacted metadata cross the logical prover/verifier and mock boundaries; confirm disposable keys are used and restart/failure states do not expose restricted values. |
| Edge agent plus managed control plane | Capture both directions at the customer/vendor boundary and confirm the permitted proof envelope, redacted signals, signed policy/update material, and no restricted fields. Disconnect vendor networking while continuing bounded ingestion and proving, exercise outbox overflow, then reconnect and prove idempotent drain. Reject invalid server identity, unsigned/revoked updates, expired policy state, altered proofs, and incompatible versions. |
| Fully customer-managed | Install and operate from an exportable, integrity-checked artifact bundle with vendor DNS, APIs, credentials, and networks blocked. Exercise proof, verification, policy lookup, audit, backup/restore where applicable, and mock submission; confirm vendor outage has no runtime effect. Test customer-controlled key rotation/revocation, segmented-network partition, bounded queues, rollback, and optional chain outage independently. |
| Independent relying-party verifier | On a machine with no vendor or general network route, import a self-contained proof package and authenticated verification/policy/revocation artifacts, reconstruct canonical public inputs, and obtain the expected result without witness or prover access. Repeat for altered inputs, missing/revoked/expired/incompatible artifacts, and confirm each fails closed. Demonstrate that optional chain/receipt lookup failure is reported separately from proof validity. |

The offline tests MUST block traffic rather than merely omit configuration, assert that no DNS or connection attempt targets a vendor endpoint, and retain the verifier command, artifact digests, trust-store/policy snapshot, decision time, and result. A cached vendor verdict is not independent verification. Acceptance also requires update and rollback ownership to match the selected topology, documented key custody, stated connectivity assumptions, and observed failure behavior consistent with [architecture](architecture.md#deployment-modes).

## SLOs, retention, and readiness

Availability, latency, recovery objectives, data-loss tolerance, capacity, retention durations, and alert thresholds are **Open/TBD**, not zero or unlimited. The service owner proposes values from workload and benchmark evidence; product/privacy approves retention and security reviews exposure.

Production readiness requires:

- accepted workload, SLOs, capacity limits, and overload behavior;
- supported version matrix and upgrade/rollback procedure;
- data inventory, purpose, retention/deletion, access, and backup treatment;
- key rotation/revocation and incident runbooks;
- restore/reconciliation evidence and dependency-failure exercises;
- resolved or explicitly owned residual security/privacy findings;
- external review appropriate to the risk; and
- an approved hardware safety case while preserving no-command architecture.

## Acceptance and related documents

Each [delivery phase](delivery-plan.md) links reproducible commands and artifacts satisfying the relevant categories above. [Architecture](architecture.md) defines failures and signals, [data and proof model](data-and-proof-model.md) defines vectors, and [security and privacy](security-and-privacy.md) defines restricted data and controls.
