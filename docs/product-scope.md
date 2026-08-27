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

## Product discovery: selected beachhead workflow

The initial commercial hypothesis is **privacy-preserving speed-policy evidence for an industrial-site drone inspection**. This is a discovery selection, not evidence that a market has been validated and not authorization to connect hardware or make a flight-safety decision.

| Role | Initial selection | Responsibility in the workflow |
| --- | --- | --- |
| Buyer | Drone inspection provider's compliance director | Buys a reusable way to satisfy customer evidence requests without surrendering commercially sensitive flight data |
| Proof-producing actor | The provider's flight-operations gateway, acting for the drone operator | Normalizes eligible telemetry and produces the bounded-speed proof after an inspection flight |
| Relying party | Industrial site owner's inspection-contract compliance officer | Verifies the claim and decides whether the speed-policy evidence attached to that flight is acceptable |

### Existing workflow and unmet need

Today, the provider exports a flight log or a manually prepared, signed compliance report after each inspection. The site owner's compliance officer receives it through the contract document channel, checks the reported speed against the site's limit, asks for clarification when fields or provenance are unclear, and records an accept/reject exception against the inspection deliverable. The selected product would replace only the disclosure-heavy speed-evidence step: it would produce and independently verify a claim that an eligible telemetry snapshot's normalized horizontal speed was at or below the public policy maximum. It would not prove the sensor was truthful, summarize an entire flight, or authorize flight or payment automatically.

The provider cannot disclose exact coordinates, complete trajectories, timestamps beyond the bounded freshness information required by policy, vehicle or customer identifiers, mission objectives, imagery, or unrelated telemetry. Those fields can expose critical-site layout, customer identity, operating methods, and the provider's commercially sensitive route planning. Discovery must establish the minimum public policy, proof-version, freshness, and replay metadata the relying party actually needs.

The relying party makes one evidence-acceptance decision for each inspection-flight deliverable, normally after the flight and before closing the contractual compliance review. The working frequency hypothesis is **5–50 decisions per buyer per month**; interviews must replace this range with observed buyer data. A false acceptance could allow a non-compliant deliverable to pass contractual review, hide a site-policy exception, and require investigation or reinspection; because telemetry truth is outside the proof, the relying party must not treat acceptance as a safety guarantee. A false rejection can delay deliverable acceptance and payment, cause avoidable analyst work or a repeat inspection, and damage provider/customer trust.

Ordinary signed reports are inadequate because a signature authenticates the reporter and protects report integrity but does not demonstrate that the private values satisfy the speed bound; the relying party must either trust the provider's assertion or request the underlying log. Contractual access controls are also inadequate because they reduce authorized access but still require sensitive data to be copied into another organization's systems, where retention, breach, subpoena, insider access, and onward-use risks remain. Neither mechanism provides the same minimal, independently verifiable claim, although signatures, contracts, authentication, and audit controls remain necessary around the proof workflow.

### Commercial validation gate

Before broad implementation begins or Phase 1 is entered, the product owner must record evidence that all of the following criteria are met:

- Complete at least **15 documented problem interviews across at least 10 organizations**, including at least **8 buyer-role interviews** with budget or procurement visibility and **5 relying-party interviews**; at least 10 interviewees must confirm that current speed-evidence disclosure or review creates a material problem.
- Secure at least **2 written design-partner commitments**, each covering a drone inspection provider and a participating industrial-site relying party, a named workflow owner, access to representative synthetic or appropriately governed data, and agreement to evaluate the workflow. A non-binding expression of interest alone does not count.
- For each design partner, complete at least **3 end-to-end workflow demonstrations** (at least **6 total**) from an eligible fixture through proof production, independent verification, and a recorded human accept/reject decision, with **100% correct outcomes** for the agreed positive and negative cases and no restricted field exposed in the verifier input, operator view, audit output, or mock-chain record.
- Obtain documented confirmation from both design-partner buyer owners that the workflow is preferable to raw-log disclosure for the tested case, identify the purchasing route and budget holder, and record a credible paid-pilot price or a signed paid-pilot commitment.
- Record observed decision volume, acceptable review time, false-acceptance and false-rejection handling, minimum public disclosure, and the objections or failure reasons from every demonstration.

If any criterion is missed, the gate remains closed: narrow or change the workflow, document the learning in the decision register, and repeat discovery rather than expanding the implementation. Product discovery may use mockups and the existing synthetic vertical-slice plan; it does not relax the SITL-only or no-command constraints.

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
- What minimum public disclosure does the selected industrial-site relying party require?
- What lawful purpose, jurisdiction, and retention obligations apply to any future pilot?

See the [decision register](decisions.md) for owners, evidence, and due gates.

## Related documents and validation

The [architecture](architecture.md) implements these boundaries; [security and privacy](security-and-privacy.md) owns threats; and the [delivery plan](delivery-plan.md) owns acceptance evidence. Validate this document through product, security, privacy, and safety review before changing an MVP gate.
