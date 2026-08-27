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

## Product positioning

The system is a **privacy-preserving telemetry attestation gateway**. It accepts eligible telemetry at an explicit trust boundary and produces narrowly scoped, independently verifiable evidence that private telemetry satisfies a public policy while withholding unrelated or sensitive source data. MAVLink is the first telemetry adapter rather than the outer boundary of the product, and bounded speed is the first claim type rather than the limit of the claim model.

A ledger is optional. If configured, it provides a publication or timestamp boundary for approved proof metadata; it is not the source of truth for telemetry, vehicle state, or proof validity. The source record, its explicitly represented trust state, the claim definition, and independent verification retain their respective authority whether or not metadata is published to a ledger.

This positioning explicitly excludes the following product categories:

- **MAVLink router:** the system does not provide general message routing or protocol forwarding.
- **Telemetry archive:** it does not serve as a flight-log repository, system of record for raw telemetry, or historical analytics platform.
- **Flight controller:** it does not navigate, stabilize, or otherwise control a vehicle.
- **Command-authority system:** it does not approve, originate, authorize, or relay vehicle commands.
- **Anonymous tracking service:** privacy-preserving claims must not become a means to track vehicles, operators, or missions anonymously or pseudonymously.
- **General-purpose blockchain bridge:** the optional ledger adapter does not transport arbitrary messages or assets and does not provide cross-chain infrastructure.

The repository name and any eventual product name are branding concerns, not implicit scope changes. A rename requires a separate, explicit branding decision and coordinated terminology migration; product documentation must not silently rename the system.

## Stakeholders and actors

| Actor | Need or responsibility |
| --- | --- |
| Vehicle/SITL source | Emits telemetry; is not implicitly trusted |
| Operator | Observes redacted lifecycle and failures |
| Auditor/relying party | Evaluates the typed verifier result and independently owns any business accept/reject decision |
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

### Commercial validation gates

Commercial validation is staged so that a criterion is not demanded before the artifact needed to test it exists. Passing one gate authorizes only the next evaluation stage; it is not production, regulatory, safety, or whole-flight-compliance evidence. If any criterion is missed, that gate remains closed: narrow or change the workflow, record the learning in the decision register, and repeat the applicable discovery rather than expanding implementation.

#### Gate 1 — problem and workflow validation (before Phase 1)

Before broad implementation begins or Phase 1 is entered, the product owner must record evidence that all of the following criteria are met:

- Complete at least **15 documented problem interviews across at least 10 organizations**, including at least **8 buyer-role interviews** with budget or procurement visibility and **5 relying-party interviews**; at least 10 interviewees must confirm that current speed-evidence disclosure or review creates a material problem.
- Confirm the actual buyer, proof-producing actor, relying party, workflow owner, evidence-acceptance decision, handoffs, current alternative, observed decision volume, acceptable review time, and consequences and handling of false acceptance, false rejection, and unverifiable outcomes. The working **5–50 decisions per buyer per month** hypothesis must be replaced with observed buyer data.
- Complete a field-by-field disclosure map of the current workflow and proposed claim, including the minimum public disclosure and restricted fields, reviewed by buyer and relying-party representatives.
- Obtain explicit buyer and relying-party acceptance that the proposed evidence is for an eligible telemetry **snapshot**, not continuous or whole-flight coverage; record whether snapshot evidence is sufficient for the decision or what sampling/coverage claim would instead be required.
- Identify the purchasing route and budget holder. This is route validation only; willingness to pay is reserved for Gate 3.
- Test the exact accepted, rejected, and unverifiable claim wording and adjacent limitations with representative relying-party reviewers, and record uncoached comprehension, objections, failure reasons, and revisions.

Gate 1 discovery MAY use paper mockups or a non-cryptographic offline UX prototype. Every screen, package, result, and research record used that way MUST be conspicuously labelled **“paper mockup — no proof generated”** or **“non-cryptographic UX prototype — no proof generated or verified,”** as applicable, and MUST NOT be represented as technical validation or independent verification.

#### Gate 2 — technical workflow validation (after Phase 2 artifacts exist)

After Phase 2 has produced the circuit, real proofs, canonical public inputs, authenticated verification/policy/revocation artifacts, and an independent verifier, the product owner, cryptography lead, and security lead must record:

- At least **3 end-to-end technical workflow demonstrations for each of 2 paired provider/relying-party evaluation teams** (at least **6 total**), including agreed positive and negative cases, from an eligible SITL fixture through real proof production, authenticated artifact handling, independent verification, and a recorded human accept/reject decision, with **100% correct outcomes**. The teams need not yet have made the Gate 3 design-partner or purchasing commitments.
- Evidence that the verifier receives no witness and that no restricted field appears in the proof package, authenticated artifacts, or verifier input; the provider and relying party must confirm from the tested artifacts that disclosure is preferable to raw-log disclosure for this case.
- Relying-party confirmation that the demonstrated source trust, provenance, policy, freshness, replay, snapshot limitation, and independent-verification controls are sufficient for the stated decision, plus observed reviewer comprehension, review time, objections, and every failure reason.

Paper mockups and non-cryptographic prototypes cannot satisfy Gate 2. A vendor assertion, self-verification by the proof producer, or a demonstration without authenticated portable artifacts also cannot satisfy it.

#### Gate 3 — commercial pilot validation (after Phase 3 offline package exists)

After Phase 3 has produced the versioned offline evidence package, and before a pilot begins, the product owner must record:

- At least **2 written paired design-partner commitments**, each naming a drone inspection provider and a participating industrial-site relying party, their workflow owners, the decision and scope, access to representative synthetic or appropriately governed data, timing, resources, success/stop criteria, and agreement to evaluate the offline workflow. A non-binding expression of interest alone does not count.
- Integration evidence for both pairs using the self-contained offline package without a vendor service or network dependency, including positive and negative cases, a human accept/reject interpretation, elapsed engineering time, code/configuration changes, dependencies, deployment/support steps, blockers, and comparison with pre-agreed integration and performance thresholds.
- Evidence that no restricted field appears in the Phase 3 offline package, verifier output, logs, mock publication record, or any justified operator view/API during either paired integration.
- Documented confirmation from both design-partner buyer owners that the packaged workflow is preferable to raw-log disclosure for the tested case, plus purchasing evidence: the validated route and budget holder, a credible paid-pilot price, and either an executed paid-pilot agreement or another completed purchase. Pilot intent alone is not purchasing evidence.

All three gates preserve the SITL-only, no-command, privacy, snapshot-limitation, authenticated-artifact, and independent-verification constraints. No gate authorizes hardware, command handling, disclosure of restricted fields, or reliance on a vendor service as the verifier.

## MVP scope

- One vehicle in a local SITL environment and one operator workflow.
- MAVLink 2 ingestion over development-only UDP, with an allowlist for `GLOBAL_POSITION_INT` and `VFR_HUD`.
- Explicit source trust state; unsigned or invalidly signed input never silently becomes trusted.
- An explicit assurance tier on every policy and verification result, governed by the [telemetry assurance model](security-and-privacy.md#telemetry-assurance-model); the product must fail closed on missing or insufficient tiers and must not present low-assurance evidence as physical or regulatory compliance.
- Versioned normalized telemetry, deterministic fixtures, and deterministic encoding requirements.
- One proof that horizontal speed in centimetres per second is at or below a public policy maximum.
- Independent local verification that reports separate cryptographic, policy, freshness, revocation, replay, assurance, and optional publication dimensions; any aggregate disposition is derived and no business decision is verifier-produced.
- A replaceable chain adapter and offline deterministic mock; no live-chain dependency in default CI.
- Redacted lifecycle status and an append-only audit event model.

## Integration product: initial relying-party workflow

The initial integration product is a **machine-to-machine evidence path**, not a dashboard product. The verifier output follows the normative typed result model: proof validity remains visible when policy, replay, assurance, or receipt checks do not pass. A relying party’s accept/reject of the inspection deliverable is a separate business record made under its own authority; neither the verifier nor a convenience service disposition produces it. A provider gateway submits one self-contained bounded-speed claim package; the relying party's service obtains or receives its independently reproducible verification result and records its own accept/reject decision. A minimal operator view MAY expose the same redacted status and recovery actions, but rich search, analytics, workflow builders, policy authoring, and fleet administration are deferred. The proof package and verifier remain usable without the hosted service as required by the independent-verifier architecture.

### Milestone-aligned integration surfaces

The integration surface grows only when the delivery-plan artifact and validated workflow evidence justify it. Phases 0–2 require no hosted service, tenant model, webhook, or network dependency: the product is a file/stdin-based offline package plus an explicitly experimental verifier CLI or minimal library sufficient to run fixtures and discovery evaluations.

| Delivery milestone | Required surface | Deferred at this milestone |
| --- | --- | --- |
| **Phase 0 — decision framing and scaffold** | Versioned fixture and schema files, a documented non-interactive file/stdin invocation, and machine-readable validation errors with deterministic exit behavior. A verifier CLI or minimal library MAY be a scaffold and MUST be labelled experimental. | Hosted API, SDK submission client, persistence, lifecycle service, webhooks, tenant administration, and audit export service. |
| **Phase 1 — telemetry vertical slice** | Offline fixture record/replay and canonical-record output through files/stdin. The experimental CLI or minimal library is sufficient for parser, trust, normalization, negative-fixture, and discovery work. | Network submission/status operations and every managed-service or control-plane surface. |
| **Phase 2 — proof spike and local verification** | A self-contained offline proof package and experimental non-interactive verifier CLI or minimal library that consumes files/stdin, emits typed machine-readable results and stable error codes, excludes restricted fields, and verifies independently without a vendor service or network dependency. | A stable public API, hosted lifecycle, managed notifications, administration, and service-level export. |
| **Phase 3 — mock adapter and operator boundary (MVP cutoff)** | Continue to ship the versioned offline package and independent verifier. Only when validated workflow evidence justifies it, add the smallest authenticated **single-organization or explicitly non-multi-tenant** API needed to submit one package and read its redacted result/lifecycle; a minimal status view is optional. Mutations MUST be idempotent, including deterministic conflict behavior. | Multi-tenant isolation or administration, cross-tenant access/export, managed webhooks, billing identifiers, organization/environment hierarchy, policy administration, fleet/batch operations, and API-stability commitments beyond the evidence-backed surface. |

### Phase 3 contract behavior

Any Phase 3 API is experimental and evidence-bounded. It uses non-interactive service credentials, explicit contract and artifact versions, allowlisted request/response schemas, stable machine-readable errors, opaque non-billing correlation identifiers, and deterministic behavior. It MUST NOT accept raw telemetry or witnesses as convenience fields. An accepted submission means only that processing began, and typed cryptographic, policy, freshness, revocation, replay, assurance, and optional publication dimensions remain distinct from the relying party's business decision.

Every mutation requires an opaque idempotency key scoped to the non-multi-tenant deployment, authenticated principal, and operation. Identical retries return the original resource and outcome; reuse with different canonical content fails with stable `IDEMPOTENCY_CONFLICT`; concurrent duplicates converge; and a timeout is reconciled with the same key or a status read. If no mutation is justified, the file/stdin verifier remains the complete integration surface.

Errors contain a stable code, safe message, retryability, opaque correlation ID, and optional field pointers. All files, stdin/stdout schemas, API payloads, URLs, logs, traces, metrics, lifecycle records, operator views, and mock publication records use reviewed allowlists and exclude raw telemetry, witnesses, exact protected values, stable source identity, secrets, and customer or mission details. Proofs and approved public inputs remain portable for offline independent verification.

The Phase 3 surface cannot be called stable until executable tests cover every implemented operation's canonical serialization, authentication and authorization denials, idempotency where mutations exist, stable error families, supported and unsupported version combinations, lifecycle transitions, and restricted-field absence. Features deferred to the post-MVP control plane are not prerequisites for Phase 3 stability.

## Ranked claim roadmap

The roadmap ranks claims by the order in which the product should investigate and, if promoted, implement them. Rank is not a commitment or an assertion that a claim is feasible. **Bounded horizontal speed remains the Phase 1 proof primitive**; later claims must not broaden Phase 1 or bypass the staged commercial validation gates. Every claim proves only that authenticated, eligible inputs satisfy its versioned policy and time semantics. It does not by itself prove that a sensor reported physical truth or authorize an operational, safety, payment, or command decision.

| Rank and candidate claim | Relying-party decision enabled | Required private witness | Minimum public disclosure | Source-authenticity requirement | Time semantics | Expected proof frequency | Principal correlation risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **1 — Bounded horizontal speed (Phase 1 primitive)** | Accept or reject speed-policy evidence attached to one inspection-flight deliverable. | Normalized horizontal speed; eligible source message and integrity/provenance material needed to bind that value to the proof instance. | Claim and circuit versions, public maximum speed and unit, pass result, source-trust class, policy identifier, freshness/validity bounds, and replay-resistant proof identifier; no exact speed, position, vehicle identifier, or fine-grained timestamp. | A pinned MAVLink 2 signed-message profile or an explicitly disclosed untrusted/synthetic trust state; signature validation, key authorization, message eligibility, and normalization version must be bound to the evidence. | A named observation instant or bounded sampling interval, with maximum source age, proof creation time, expiry, and replay scope defined by policy; a snapshot must not be presented as whole-flight compliance. | Phase 1: per selected eligible telemetry snapshot during demonstrations; product workflow: normally one evidence package per inspection-flight decision, with any repeated samples explicitly disclosed as partial coverage. | Stable proof, policy, source-key, or precise-time metadata could link inspections and reconstruct operational tempo even when speed and location remain private. |
| **2 — Altitude bound** | Decide whether evidence supports compliance with a contractual or site-specific minimum and/or maximum altitude policy for the covered observation. | Normalized altitude value, altitude datum/reference, source message, and provenance/integrity material. | Claim/circuit and policy identifiers, public lower and/or upper bound with unit and datum, pass result, trust class, coarse validity interval, and replay-resistant identifier; no exact altitude or coordinates. | An authenticated, authorized source plus a documented trust chain for the altitude field and datum conversion; transformations and calibration assumptions must be versioned. | Policy must state whether the claim covers one instant, a defined interval, or a flight segment, including sample cadence, allowed gaps, freshness, clock source, and boundary inclusivity. | At policy checkpoints or as an interval/segment proof; potentially several proofs per flight until safe aggregation is feasible. | Altitude bands combined with time, terrain, or known infrastructure can reveal location, task phase, or vehicle identity. |
| **3 — Geofence inclusion or exclusion** | Decide whether the covered observations remained inside an authorized area or outside a prohibited area, without receiving the trajectory. | Normalized position observations, private timestamps or ordering data, polygon/volume membership inputs when policy geometry is private, and source provenance. | Claim/circuit and policy identifiers, result, whether the rule is inclusion or exclusion, public or committed geometry/version, altitude/datum convention, coverage interval and gap policy, trust class, and replay-resistant identifier; no coordinates or path. | Authenticated and authorized position/time sources; the geometry issuer and policy version must also be authenticated, and coordinate-system conversions must be deterministic and bound to the proof. | Explicit start/end and timezone/clock basis, sample cadence, maximum gap, boundary rule, and treatment of stale, reordered, or missing observations; sampled membership must not be described as continuous containment. | Per protected area and covered flight segment, normally one aggregate proof per relying-party decision rather than one proof per position report. | Area identifiers, geometry versions, time intervals, and repeated membership results can reveal customer sites, destinations, or recurring missions. |
| **4 — Route-corridor adherence** | Decide whether a covered flight segment followed an approved corridor within stated lateral/vertical tolerances. | Ordered normalized positions and times, route/corridor definition if private, tolerances, and source provenance. | Claim/circuit and policy identifiers, result, committed or public corridor/version, public tolerances where required, coverage interval, sampling/gap rule, trust class, and replay-resistant identifier; no trajectory or exact waypoint times. | Authenticated, authorized position and time observations plus an authenticated corridor issuer; ordering, coordinate conversion, and route-version binding must be verifiable. | A defined segment with monotonic ordering, clock tolerance, minimum sampling cadence, maximum gap, endpoint rules, and an explicit statement that discrete samples do not prove the path between samples. | Normally one proof per corridor segment or flight; retries and overlapping segments must share a disclosed replay/coverage model. | Corridor and policy identifiers are strong location and customer signals; repeated segment timing can fingerprint routes and operating patterns. |
| **5 — Authorized time window** | Decide whether the covered activity occurred within an approved operating window without learning exact event times. | Authenticated event or observation times, window authorization when private, relevant ordering data, and source provenance. | Claim/circuit and authorization-policy identifiers, pass result, coarse window or commitment, timezone and clock basis, validity/expiry, trust class, and replay-resistant identifier; no exact timestamp unless indispensable. | An authenticated authorized clock or timestamp source bound to eligible telemetry, plus authenticated issuance and revocation state for the window authorization; host receipt time alone is insufficient unless policy explicitly accepts it. | Version 1 uses `[not_before, not_after)`; timezone, clock authority, skew tolerance, daylight-saving handling, revocation cutoff, freshness, and whether the claim concerns start, end, every sample, or the entire interval must be explicit. A relying-party need for other boundary semantics requires a separately reviewed versioned contract, not reinterpretation of version 1. | Per authorization window, flight, or relevant event; avoid periodic proofs that expose a high-resolution activity schedule. | Even coarse recurring windows can expose staffing, maintenance, customer activity, and mission cadence, especially when linked to other claims. |
| **6 — Composite mission compliance** | Decide whether one mission evidence package satisfies an explicitly enumerated conjunction of promoted claims for contractual review. | Witnesses for every component claim, mission-scoped binding data, policy composition data, and provenance sufficient to prevent mixing observations from different missions or sources. | Composite/circuit and policy-bundle identifiers, pass result, component claim types and versions, coverage and gap semantics, trust-class summary, expiry, and mission-scoped replay-resistant identifier; disclose no component values or stable mission/vehicle identity unless required. | Every component must meet its own source-authenticity requirement, while authenticated mission binding, policy issuance, component-version compatibility, and anti-splicing controls establish that components concern the same authorized scope. | A single declared coverage model must reconcile component instants and intervals, clock sources, skew, gaps, expiry, revocation, and partial failures; “mission compliant” is prohibited unless the policy defines complete mission coverage. | Normally one proof per mission decision, regenerated only for an authorized policy change or corrected evidence with explicit supersession semantics. | Combining otherwise minimal claims creates a distinctive mission fingerprint and amplifies linkage through shared policy, timing, source, and replay metadata. |

### Candidate promotion criteria

Ranks 2–6 remain discovery candidates and enter implementation only when the product owner records all of the following evidence for that specific claim. Passing these criteria prioritizes implementation planning; it does not move hardware, live-chain, command, or safety boundaries.

- **Customer evidence:** documented buyer and relying-party evidence identifies the real decision, decision frequency, consequence of false acceptance and rejection, current alternative, required disclosure, and willingness to evaluate the claim. At least one design partner must provide representative synthetic or appropriately governed fixtures and written acceptance cases.
- **Privacy review:** the privacy owner approves the data-flow and disclosure inventory, correlation and composition analysis, retention and deletion treatment, replay metadata, and mitigations. The review must show why every public input is necessary and assess linkage with existing claims.
- **Proof feasibility:** engineering and cryptography document the precise predicate, witness and public-input schema, deterministic encoding and normalization, constraint/performance estimate, coverage and failure semantics, and positive and negative test vectors. A prototype must demonstrate independent verification without exposing restricted witness fields.
- **Source trust:** security documents the authoritative source for every witness and policy input, authentication and authorization chain, key and revocation handling, trust-state representation, clock/datum/coordinate assumptions where relevant, and behavior for missing, stale, reordered, unsigned, or invalid inputs.

If any category is absent, unresolved, or relies on an implicit assumption, the candidate stays deferred. Promotion requires a dated decision-register entry naming the accountable product, privacy, engineering/cryptography, and security approvers, linking the evidence above, fixing the claim's rank or recording why order changed, and defining an implementation acceptance gate. Composite mission compliance cannot be promoted until each included component claim has independently met these criteria and the composition-specific correlation and anti-splicing risks have been reviewed.

## Post-MVP control plane

A managed multi-tenant control plane is a future product surface, not part of the MVP. Its purpose would be to manage authorization, policy assignment, service limits, and privacy-preserving operational accounting around the proof workflow; it would not become a telemetry inventory or a source of proof truth. Implementation stays outside Phases 0–3 unless the selected design partner documents that it is necessary for the agreed workflow and the product, security, and privacy owners approve the resulting scope change. Tenant administration, per-tenant quota semantics, cross-tenant exports, managed webhooks, billing-related identifiers, and the organization/environment hierarchy belong exclusively to this post-MVP control-plane scope. A design-partner need during Phase 3 may trigger a new scope decision, but does not silently make Phase 3 multi-tenant.

### Future concepts

| Concept | Post-MVP meaning |
| --- | --- |
| Tenant | The top-level security, authorization, audit, quota, and billing boundary for one managed customer relationship. A tenant identifier is opaque and must not encode a customer, mission, or vehicle identity. |
| Organization | A tenant-scoped grouping for business ownership and delegated administration, potentially representing a provider, relying party, or business unit; its cross-organization sharing rules remain an explicit decision. |
| Environment | An isolated tenant-scoped deployment context, such as development, test, or production, with separate credentials, policy assignments, quotas, and audit scope. Moving data or configuration between environments is not implicit. |
| Policy owner | A tenant- or organization-scoped principal accountable for proposing, approving, versioning, assigning, and retiring policy definitions and verifier allowlists; ownership does not grant access to witnesses or source telemetry. |
| Verifier | A human or service principal authorized for specified tenants, organizations, environments, policies, and purposes to verify proof packages or consume results; verification authority does not imply policy ownership or administration. |
| Administrator | A human or service principal with explicitly delegated control-plane permissions. Administration is separated by function and scope, does not imply verifier or policy-owner authority, and never grants access to private proof inputs. |
| Quota | A versioned, scoped limit on allowed control-plane or proof-service operations, such as submissions, verifications, concurrency, storage, or audit export. A quota is an enforcement and service-protection rule, not evidence about vehicle activity or compliance. |
| Usage record | A minimal, append-only accounting event for an authorized service operation, containing only an opaque tenant/environment scope, operation class, coarse time bucket where possible, quantity, outcome class, and applicable quota or pricing version. It is not a claim, proof, audit substitute, or telemetry record. |

Raw telemetry, witnesses, and stable vehicle or source identifiers **MUST NOT** be billing dimensions or control-plane metadata. They must not be copied into tenant profiles, organization or environment records, role bindings, policy ownership, quota keys, usage records, invoices, dashboards, support views, or control-plane logs. Accounting must use allowlisted operation-level measures and opaque, scoped identifiers; commercial requirements that cannot be met within that boundary require a new privacy and product decision rather than expanding collection silently.

### Managed-pilot decision gates

Before any managed multi-tenant pilot, accountable owners must resolve and record the following questions in ADRs and executable acceptance evidence:

- **Isolation:** What are the tenant and environment isolation boundaries for identity, authorization, compute, queues, caches, persistence, cryptographic keys, logs, metrics, exports, backups, and support access? How are cross-tenant object references denied, tested, monitored, and handled during incident response and restore?
- **Audit:** Which control-plane and data-access actions are recorded, who may read or export each scope, how are ordering and integrity demonstrated, and how are redaction, retention, legal hold, clock authority, and administrator actions handled without turning the audit trail into sensitive telemetry?
- **Delegated administration:** Which roles may create organizations and environments, bind principals, assign policies, manage verifiers and credentials, set quotas, or delegate narrower authority? Which operations require separation of duties, step-up authentication, expiry, approval, or emergency-access review, and how are privilege escalation and confused-deputy paths tested?
- **Data residency:** In which jurisdictions may each metadata class, key, audit event, usage record, support artifact, replica, and backup be processed or stored? How are routing, subprocessors, failover, export, migration, and verifiable residency enforcement represented in the contract?
- **Deletion:** What is the deletion authority and schedule for every control-plane record and derived copy; how do tenant closure, user erasure, policy retirement, backup expiry, caches, exports, legal holds, and externally held proof packages interact; and what evidence demonstrates deletion without claiming recall of already distributed artifacts?

The pilot gate must also fix the resource hierarchy and identifier model, role and delegation matrix, isolation architecture, audit schema, residency map, deletion/retention schedule, and quota/usage schema. Negative cross-tenant authorization tests, restore and deletion exercises, audit-integrity checks, residency/failover tests, and verification that prohibited billing fields are absent are required before onboarding more than one managed tenant.

## Deferred

- Polygon/geofence proofs, aggregation, recursion, batching, and private policy parameters.
- Multiple vehicles, fleet coordination, and policy orchestration.
- Live Midnight integration, token/economic design, and production chain operations.
- Hardware telemetry, hardware-backed attestation, and production key ceremonies.
- High availability, multi-region recovery, Kubernetes, raw-log storage, and historical analytics.
- Final production SLOs and retention periods, which require measured and legal evidence.
- Managed multi-tenant control-plane implementation, including its identity hierarchy, delegated administration, quota enforcement, and usage accounting, subject to the managed-pilot decision gates above.

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
