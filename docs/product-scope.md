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
- An explicit assurance tier on every policy and verification result, governed by the [telemetry assurance model](security-and-privacy.md#telemetry-assurance-model); the product must fail closed on missing or insufficient tiers and must not present low-assurance evidence as physical or regulatory compliance.
- Versioned normalized telemetry, deterministic fixtures, and deterministic encoding requirements.
- One proof that horizontal speed in centimetres per second is at or below a public policy maximum.
- Independent local verification including version, policy, expiry, and replay checks.
- A replaceable chain adapter and offline deterministic mock; no live-chain dependency in default CI.
- Redacted lifecycle status and an append-only audit event model.

## Integration product: initial relying-party workflow

The initial integration product is a **machine-to-machine evidence path**, not a dashboard product. A provider gateway submits one self-contained bounded-speed claim package; the relying party's service obtains or receives its independently reproducible verification result and records its own accept/reject decision. A minimal operator view MAY expose the same redacted status and recovery actions, but rich search, analytics, workflow builders, policy authoring, and fleet administration are deferred. The proof package and verifier remain usable without the hosted service as required by the independent-verifier architecture.

### Minimum integration surfaces

| Surface | Phase 1 minimum | Explicitly not required for API stability |
| --- | --- | --- |
| SDK | One supported library that constructs canonical submission envelopes, supplies idempotency and correlation headers, submits a claim, polls a result, verifies webhook signatures, and invokes the offline verifier. It MUST expose the wire response and stable error code rather than replace them with SDK-only meanings. | Multiple languages, UI components, policy builders, telemetry ingestion, and automatic business acceptance. |
| CLI | Non-interactive `claim submit`, `claim status`, `claim verify`, and `audit export` commands with JSON input/output, file/stdin support, deterministic exit codes, and no secret or proof content in default logs. | An interactive console, dashboard parity, or fleet operations. |
| API | Authenticated operations to submit one claim package, retrieve its redacted lifecycle/verification result, and export authorized audit events. Submission accepts a proof, canonical reviewed public inputs, explicit schema/circuit/policy/domain versions, opaque caller reference, and idempotency key; it MUST NOT accept raw telemetry as a convenience field. | General proof orchestration, batch/fleet endpoints, policy administration, raw-log upload, and chain-specific operations. |
| Webhook | An optional signed notification for terminal verification and submission/finality changes. Its payload contains an event ID, claim ID, event type, occurred-at time, result/status, version, and status URL; consumers retrieve details from the API. Delivery is at least once. | Proof or witness delivery, a complete event bus, or a webhook-only source of truth. |
| Audit export | A paginated, machine-readable JSON Lines export over an authorized time/cursor range containing redacted lifecycle events, actor/action, stable outcome/error code, version identifiers, and integrity/ordering metadata. | Raw telemetry, witnesses, exact position or speed, secrets, stable source identity, unrestricted bulk history, or a compliance certification report. |

### Actors and permissions

Permissions are tenant- and purpose-scoped, deny by default, and enforced by the API rather than by an SDK or dashboard. Service identities are preferred for the integration path; human identities are used only for review, recovery, and audit. No role can retrieve a witness or restricted source data through these surfaces.

| Actor | Minimum allowed actions | Prohibited or separately authorized actions |
| --- | --- | --- |
| Provider submitter service | Submit claims for its authorized tenant and policy set; read the redacted status of claims it submitted. | Read another submitter's claims, declare verification success, accept on behalf of a relying party, export audit history, or administer policies/credentials. |
| Relying-party verifier service | Retrieve authorized proof packages or results, independently verify them against its allowlist, read relevant status, and register an opaque evidence-decision reference if that operation is enabled. | Access private inputs, mutate cryptographic results, submit as the provider, or infer that verification is a safety/payment authorization. |
| Webhook receiver | Receive only subscribed events for an authorized tenant and verify delivery signatures; fetch details using its separately scoped API credential. | Treat delivery as exactly once, use a webhook signature as proof validity, or receive witness/restricted fields. |
| Human reviewer/operator | Read redacted status and errors for assigned cases and perform explicitly authorized retry/cancel/recovery actions where lifecycle rules permit. | View raw telemetry or witnesses, rewrite terminal results, or gain administrative permission implicitly. |
| Auditor | Read/export the minimum redacted, purpose-bound audit range needed for review. | Submit or mutate claims, recover secrets, or perform an unbounded cross-tenant export. |
| Tenant administrator | Manage tenant service identities, role bindings, webhook endpoints, and permitted policy/version allowlists with auditable changes and separation-of-duty controls. | Read private proof inputs merely by being an administrator or alter historical audit events. |

### Contract behavior

- **Idempotency:** every mutating request requires a caller-generated opaque idempotency key scoped to tenant, operation, and authenticated principal. The service stores a canonical request digest and returns the original resource and outcome for an identical retry. Reuse with different canonical content fails with a stable `IDEMPOTENCY_CONFLICT`; concurrent duplicates converge on one claim. Retention is at least the claim's validity and retry window and is advertised by the service. Webhooks use immutable event IDs and may be delivered more than once; consumers deduplicate by event ID. A transport timeout is an unknown outcome and clients query/retry with the same key.
- **Version negotiation:** the wire API uses a major version in its protocol route or media type and reports its exact contract version. Every claim also carries independent schema, claim, circuit, policy, encoding/domain-separation, and proof-system versions; omission or unsupported combinations fail closed. Additive compatible fields may appear within a major version and clients ignore unknown optional fields but never unknown enum values that affect security or verification. The service publishes a machine-readable compatibility document and deprecation/sunset metadata; it never silently upgrades a proof or policy.
- **Error semantics:** synchronous responses use an appropriate transport status plus a structured body containing stable code, safe message, retryability, opaque correlation ID, and optional field pointers; they contain no witness value or secret. Authentication/authorization failure, malformed input, unsupported version, policy rejection, cryptographic rejection, conflict, throttling, dependency unavailability, and internal failure remain distinguishable. An accepted submission means only that processing began. Terminal `VERIFIED`, `REJECTED`, and `FAILED` outcomes are explicit, and local cryptographic verification remains distinct from optional publication/finality.
- **Rate limits:** quotas are enforced per tenant and credential, with stricter limits for submission and export than status reads. Responses advertise the applicable limit, remaining budget or standard retry metadata where safe, and `Retry-After` on throttling. Clients use bounded exponential backoff with jitter and the same idempotency key. Limits, payload bounds, concurrency, and export windows are published contract parameters rather than implied availability targets; throttling never turns a rejected or unknown result into acceptance.
- **Redaction:** request/response logs, errors, traces, metrics, webhooks, status resources, audit exports, and support tooling use an allowlist. They exclude raw telemetry, witnesses, exact speed and position, fine-grained source time beyond approved policy bounds, salts/openings, keys/tokens/signatures used as credentials, stable vehicle/source identity, customer or mission details, and unreviewed proof-system internals. Proof bytes and approved public inputs are returned only to a role and endpoint that require them, are never placed in URLs, and are represented in logs only by an approved digest if necessary. Opaque IDs MUST be non-semantic and tenant-scoped; export access, generation, and download are themselves audited.

### Stability gate

The API MUST remain explicitly experimental until executable consumer/provider contract tests cover canonical serialization, authentication and actor denial cases, idempotent retry and conflict, every stable error family, supported and unsupported version combinations, lifecycle transitions, pagination/cursors, rate-limit behavior, webhook signature/replay/deduplication, and restricted-field absence across responses, logs, webhooks, and audit exports. The same suite MUST run against the service and the supported SDK/CLI where applicable.

Before the API is declared stable, one reference relying-party integration owned as versioned code MUST submit the deterministic positive and negative fixtures through the public machine interface, independently verify the returned packages, consume duplicate/out-of-order webhook deliveries, reconcile status after a simulated timeout, export its authorized audit trail, and demonstrate that no restricted field crosses the boundary. Its CI must pass against the release candidate. Documentation or a dashboard demonstration alone does not satisfy this gate; breaking changes after stability require a new major API version and a published migration path.

## Ranked claim roadmap

The roadmap ranks claims by the order in which the product should investigate and, if promoted, implement them. Rank is not a commitment or an assertion that a claim is feasible. **Bounded horizontal speed remains the Phase 1 proof primitive**; later claims must not broaden Phase 1 or bypass the commercial validation gate. Every claim proves only that authenticated, eligible inputs satisfy its versioned policy and time semantics. It does not by itself prove that a sensor reported physical truth or authorize an operational, safety, payment, or command decision.

| Rank and candidate claim | Relying-party decision enabled | Required private witness | Minimum public disclosure | Source-authenticity requirement | Time semantics | Expected proof frequency | Principal correlation risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **1 — Bounded horizontal speed (Phase 1 primitive)** | Accept or reject speed-policy evidence attached to one inspection-flight deliverable. | Normalized horizontal speed; eligible source message and integrity/provenance material needed to bind that value to the proof instance. | Claim and circuit versions, public maximum speed and unit, pass result, source-trust class, policy identifier, freshness/validity bounds, and replay-resistant proof identifier; no exact speed, position, vehicle identifier, or fine-grained timestamp. | A pinned MAVLink 2 signed-message profile or an explicitly disclosed untrusted/synthetic trust state; signature validation, key authorization, message eligibility, and normalization version must be bound to the evidence. | A named observation instant or bounded sampling interval, with maximum source age, proof creation time, expiry, and replay scope defined by policy; a snapshot must not be presented as whole-flight compliance. | Phase 1: per selected eligible telemetry snapshot during demonstrations; product workflow: normally one evidence package per inspection-flight decision, with any repeated samples explicitly disclosed as partial coverage. | Stable proof, policy, source-key, or precise-time metadata could link inspections and reconstruct operational tempo even when speed and location remain private. |
| **2 — Altitude bound** | Decide whether evidence supports compliance with a contractual or site-specific minimum and/or maximum altitude policy for the covered observation. | Normalized altitude value, altitude datum/reference, source message, and provenance/integrity material. | Claim/circuit and policy identifiers, public lower and/or upper bound with unit and datum, pass result, trust class, coarse validity interval, and replay-resistant identifier; no exact altitude or coordinates. | An authenticated, authorized source plus a documented trust chain for the altitude field and datum conversion; transformations and calibration assumptions must be versioned. | Policy must state whether the claim covers one instant, a defined interval, or a flight segment, including sample cadence, allowed gaps, freshness, clock source, and boundary inclusivity. | At policy checkpoints or as an interval/segment proof; potentially several proofs per flight until safe aggregation is feasible. | Altitude bands combined with time, terrain, or known infrastructure can reveal location, task phase, or vehicle identity. |
| **3 — Geofence inclusion or exclusion** | Decide whether the covered observations remained inside an authorized area or outside a prohibited area, without receiving the trajectory. | Normalized position observations, private timestamps or ordering data, polygon/volume membership inputs when policy geometry is private, and source provenance. | Claim/circuit and policy identifiers, result, whether the rule is inclusion or exclusion, public or committed geometry/version, altitude/datum convention, coverage interval and gap policy, trust class, and replay-resistant identifier; no coordinates or path. | Authenticated and authorized position/time sources; the geometry issuer and policy version must also be authenticated, and coordinate-system conversions must be deterministic and bound to the proof. | Explicit start/end and timezone/clock basis, sample cadence, maximum gap, boundary rule, and treatment of stale, reordered, or missing observations; sampled membership must not be described as continuous containment. | Per protected area and covered flight segment, normally one aggregate proof per relying-party decision rather than one proof per position report. | Area identifiers, geometry versions, time intervals, and repeated membership results can reveal customer sites, destinations, or recurring missions. |
| **4 — Route-corridor adherence** | Decide whether a covered flight segment followed an approved corridor within stated lateral/vertical tolerances. | Ordered normalized positions and times, route/corridor definition if private, tolerances, and source provenance. | Claim/circuit and policy identifiers, result, committed or public corridor/version, public tolerances where required, coverage interval, sampling/gap rule, trust class, and replay-resistant identifier; no trajectory or exact waypoint times. | Authenticated, authorized position and time observations plus an authenticated corridor issuer; ordering, coordinate conversion, and route-version binding must be verifiable. | A defined segment with monotonic ordering, clock tolerance, minimum sampling cadence, maximum gap, endpoint rules, and an explicit statement that discrete samples do not prove the path between samples. | Normally one proof per corridor segment or flight; retries and overlapping segments must share a disclosed replay/coverage model. | Corridor and policy identifiers are strong location and customer signals; repeated segment timing can fingerprint routes and operating patterns. |
| **5 — Authorized time window** | Decide whether the covered activity occurred within an approved operating window without learning exact event times. | Authenticated event or observation times, window authorization when private, relevant ordering data, and source provenance. | Claim/circuit and authorization-policy identifiers, pass result, coarse window or commitment, timezone and clock basis, validity/expiry, trust class, and replay-resistant identifier; no exact timestamp unless indispensable. | An authenticated authorized clock or timestamp source bound to eligible telemetry, plus authenticated issuance and revocation state for the window authorization; host receipt time alone is insufficient unless policy explicitly accepts it. | Inclusive/exclusive boundaries, timezone, clock authority, skew tolerance, daylight-saving handling, revocation cutoff, freshness, and whether the claim concerns start, end, every sample, or the entire interval must be explicit. | Per authorization window, flight, or relevant event; avoid periodic proofs that expose a high-resolution activity schedule. | Even coarse recurring windows can expose staffing, maintenance, customer activity, and mission cadence, especially when linked to other claims. |
| **6 — Composite mission compliance** | Decide whether one mission evidence package satisfies an explicitly enumerated conjunction of promoted claims for contractual review. | Witnesses for every component claim, mission-scoped binding data, policy composition data, and provenance sufficient to prevent mixing observations from different missions or sources. | Composite/circuit and policy-bundle identifiers, pass result, component claim types and versions, coverage and gap semantics, trust-class summary, expiry, and mission-scoped replay-resistant identifier; disclose no component values or stable mission/vehicle identity unless required. | Every component must meet its own source-authenticity requirement, while authenticated mission binding, policy issuance, component-version compatibility, and anti-splicing controls establish that components concern the same authorized scope. | A single declared coverage model must reconcile component instants and intervals, clock sources, skew, gaps, expiry, revocation, and partial failures; “mission compliant” is prohibited unless the policy defines complete mission coverage. | Normally one proof per mission decision, regenerated only for an authorized policy change or corrected evidence with explicit supersession semantics. | Combining otherwise minimal claims creates a distinctive mission fingerprint and amplifies linkage through shared policy, timing, source, and replay metadata. |

### Candidate promotion criteria

Ranks 2–6 remain discovery candidates and enter implementation only when the product owner records all of the following evidence for that specific claim. Passing these criteria prioritizes implementation planning; it does not move hardware, live-chain, command, or safety boundaries.

- **Customer evidence:** documented buyer and relying-party evidence identifies the real decision, decision frequency, consequence of false acceptance and rejection, current alternative, required disclosure, and willingness to evaluate the claim. At least one design partner must provide representative synthetic or appropriately governed fixtures and written acceptance cases.
- **Privacy review:** the privacy owner approves the data-flow and disclosure inventory, correlation and composition analysis, retention and deletion treatment, replay metadata, and mitigations. The review must show why every public input is necessary and assess linkage with existing claims.
- **Proof feasibility:** engineering and cryptography document the precise predicate, witness and public-input schema, deterministic encoding and normalization, constraint/performance estimate, coverage and failure semantics, and positive and negative test vectors. A prototype must demonstrate independent verification without exposing restricted witness fields.
- **Source trust:** security documents the authoritative source for every witness and policy input, authentication and authorization chain, key and revocation handling, trust-state representation, clock/datum/coordinate assumptions where relevant, and behavior for missing, stale, reordered, unsigned, or invalid inputs.

If any category is absent, unresolved, or relies on an implicit assumption, the candidate stays deferred. Promotion requires a dated decision-register entry naming the accountable product, privacy, engineering/cryptography, and security approvers, linking the evidence above, fixing the claim's rank or recording why order changed, and defining an implementation acceptance gate. Composite mission compliance cannot be promoted until each included component claim has independently met these criteria and the composition-specific correlation and anti-splicing risks have been reviewed.

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
