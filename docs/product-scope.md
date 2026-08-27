# Product scope

| Metadata | Value |
| --- | --- |
| Status | Proposed MVP baseline |
| Audience | Product, engineering, security, safety, and reviewers |
| Accountable role | Product owner |
| Review trigger | Change to actors, outcomes, scope, non-goals, or release gates |
| Authority | Normative for MVP scope; examples are illustrative |

## Purpose and intended outcome

Selected telemetry can reveal location, identity, and mission details even when a relying party needs only a compliance claim. The proposed system separates private source data from a minimal public claim and auditable lifecycle metadata.

The intended outcome is a deterministic demonstration that one SITL vehicle's normalized horizontal speed satisfies a configured upper bound, while exact position is not exposed to the operator view or mock chain record. A proof establishes only that its witness satisfies its circuit and public inputs. It does not establish sensor truth, airworthiness, operator identity, or physical compliance.

## Stakeholders and actors

| Actor | Need or responsibility |
| --- | --- |
| Vehicle/SITL source | Emits telemetry; is not implicitly trusted |
| Operator | Observes redacted lifecycle and failures |
| Auditor/relying party | Evaluates approved proof metadata and verification outcome |
| Product owner | Owns purpose, disclosures, and acceptance |
| Engineering/cryptography/security | Implement and validate boundaries within their disciplines |
| Service owner/SRE | Owns measured operating limits after a runnable system exists |
| Safety owner | Approves any progression beyond simulation; no command path is authorized |

## MVP scope

- One vehicle in a local SITL environment and one operator workflow.
- MAVLink 2 ingestion over development-only UDP, with an allowlist for `GLOBAL_POSITION_INT` and `VFR_HUD`.
- Explicit source trust state; unsigned or invalidly signed input never silently becomes trusted.
- Versioned normalized telemetry, deterministic fixtures, and deterministic encoding requirements.
- One proof that horizontal speed in centimetres per second is at or below a public policy maximum.
- Independent local verification including version, policy, expiry, and replay checks.
- A replaceable chain adapter and offline deterministic mock; no live-chain dependency in default CI.
- Redacted lifecycle status and an append-only audit event model.

## Deferred

- Polygon/geofence proofs, aggregation, recursion, batching, and private policy parameters.
- Multiple vehicles, fleet coordination, and policy orchestration.
- Live Midnight integration, token/economic design, and production chain operations.
- Hardware telemetry, hardware-backed attestation, and production key ceremonies.
- High availability, multi-region recovery, Kubernetes, raw-log storage, and historical analytics.
- Final production SLOs and retention periods, which require measured and legal evidence.

## Non-goals and safety constraint

- No flight control, navigation, collision avoidance, autonomous decision execution, or command authorization.
- No MAVLink command output from the proxy under any success or failure condition.
- No claim of Byzantine or swarm consensus, continued operation after disconnection, or reliable/confidential delivery from UDP.
- No claim that a proof or blockchain inclusion authenticates physical telemetry.
- No public-ledger storage of raw high-rate telemetry.
- No support for every dialect/transport and no safety-critical, defense, or regulated certification claim.

Any proposed command path is a separate product requiring hazard analysis, safety governance, authorization design, and a new scope decision.

## Success measures and constraints

The MVP succeeds when one synthetic fixture reproducibly traverses ingestion, normalization, proving, verification, mock submission, and redacted observation; required negative cases reject; and the evidence is produced by a documented CI command. Exact criteria are owned by the [delivery plan](delivery-plan.md).

Latency, throughput, availability, recovery, retention, and capacity values remain **Open** until measured and approved by the accountable roles. The vertical slice records distributions and resource use; it does not label them “real-time.” SITL is the only source until hardware entry gates pass.

## Open decisions

- Which SITL implementation and signed-message profile is the single pinned Phase 1 baseline?
- Who is the relying party, and what minimum public disclosure do they require?
- What lawful purpose, jurisdiction, and retention obligations apply to any future pilot?

See the [decision register](decisions.md) for owners, evidence, and due gates.

## Related documents and validation

The [architecture](architecture.md) implements these boundaries; [security and privacy](security-and-privacy.md) owns threats; and the [delivery plan](delivery-plan.md) owns acceptance evidence. Validate this document through product, security, privacy, and safety review before changing an MVP gate.
