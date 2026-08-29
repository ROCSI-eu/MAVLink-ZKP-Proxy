# Delivery plan

| Metadata | Value |
| --- | --- |
| Status | Proposed sequence and gates |
| Audience | Delivery, engineering, cryptography, security, product, platform, and operations |
| Accountable role | Delivery lead; named discipline roles approve their evidence |
| Review trigger | Scope, dependency, phase, gate, evidence, or ownership change |
| Authority | Normative phase order and gates; Phases 0–3 define the proposed MVP, and Phases 4–5 are post-MVP |

## Delivery rules

Phases are evidence gates, not calendar promises. A phase cannot exit solely because code exists. Its milestone record identifies evidence, approvers, unresolved risks, and accepted residual risk. Unknown dates, SLOs, and capacity targets remain TBD until the responsible role has evidence.

Technical completion and product discovery are parallel evidence tracks. Passing a discovery gate establishes only that the selected workflow deserves the next round of evaluation; it does not establish security, safety, operational, regulatory, commercial, or production readiness. Conversely, passing technical tests does not establish user value, adoption, pilot intent, or willingness to pay. A phase exits only when both its technical evidence and its stated product-discovery evidence are accepted.

The three product-discovery gates occur at the first point their required artifacts exist: the problem/workflow gate before Phase 1, the real-proof technical-workflow gate after the Phase 2 artifacts exist, and the paired-design-partner commercial gate after the Phase 3 offline package exists and before a pilot. Evidence from a later gate cannot be presumed at an earlier gate, and passing technical evidence cannot substitute for commercial evidence.

### Product-discovery evidence rubric

Discovery records MUST identify the participant and role, workflow and decision tested, representative inputs, method, pre-agreed acceptance threshold, observed result, objections, and product-owner disposition. Before Phase 1, comprehension research MAY use paper mockups or a non-cryptographic offline UX prototype only when every surface and research record is conspicuously labelled **“paper mockup — no proof generated”** or **“non-cryptographic UX prototype — no proof generated or verified.”** Such research cannot count as proof production, authenticated-artifact handling, or independent verification. Post-Phase-2 technical evaluations use real proofs, canonical public inputs, authenticated verification/policy/revocation artifacts, and an independent verifier. Post-Phase-3 commercial evaluations use the self-contained **offline evidence package**, including positive and negative claim fixtures, those proof and verification materials, claim wording and limitations, and instructions for import and verification without a vendor service or network dependency.

| Question | Evidence required |
| --- | --- |
| **Privacy improvement** | A field-by-field comparison of the current disclosure with the offline package, reviewed by the provider and relying party, shows which sensitive fields are eliminated and confirms that no restricted field is exposed. Participant preference alone is insufficient without the disclosure comparison. |
| **Verifier comprehension** | A representative relying-party reviewer, without coaching during the task, correctly explains what an accepted and rejected result mean, the public claim, assurance tier, freshness and replay limits, and what is *not* proven; observed errors and wording revisions are recorded. |
| **Acceptable integration effort** | A reference integrator records elapsed engineering time, code/configuration changes, dependencies, deployment and support steps, and unresolved blockers, then compares them with a threshold agreed with the workflow owner before the evaluation. |
| **Assurance sufficiency** | The relying party documents the minimum source trust, provenance, policy, freshness, replay, and verification controls needed for its decision and accepts or rejects the package's explicit assurance tier against those needs. Acceptance is limited to that decision and does not imply sensor truth, safety, or regulatory compliance. |
| **Performance fit** | Measurements on representative hardware and package sizes cover proof generation where relevant, package transfer/import, verification latency, reviewer handling time, memory, and throughput, and are compared with workflow-specific thresholds agreed before the test. These are discovery thresholds, not SLOs or capacity claims. |
| **Pilot intent** | A written evaluation or pilot commitment names the provider and relying-party owners, decision and scope, fixtures or governed data, timing, resources, success/stop criteria, and the procurement or budget-validation next step. Informal interest, meeting attendance, positive feedback, an unsigned expression of interest, or agreement to keep talking does not qualify. Pilot intent is not validated willingness to pay; that requires separate purchasing evidence such as an executed paid-pilot agreement or completed purchase. |

Failed or inconclusive criteria remain recorded learning and keep the applicable discovery gate closed; they are not converted into production-readiness claims.

## Next milestone — Validated claim and verifier contract

This is the named next milestone. This plan owns the milestone's entry conditions, workstream, required evidence, and exit rules. The repository remains documentation only, and this milestone describes proposed validation work; it does not state or imply that a prototype, verifier, proof circuit, or production component has been implemented.

### Milestone entry criteria

Entry requires all of the following; an unassigned discipline or an implicit approval keeps the milestone closed.

- Named individuals are recorded for the product, delivery, architecture, cryptography, security, privacy, safety, telemetry, discovery, and relying-party roles. The relying-party role represents the owner of the decision being researched, not the producer or project team acting as a proxy. Each person acknowledges their accountability and the reviews assigned below.
- The documentation baseline is approved as a **documentation-only maturity state**. No prototype, proof, verifier, telemetry integration, operational control, or product capability is claimed to exist merely because its contract is described.
- The candidate bounded-speed claim and relying-party decision are identified only as hypotheses to validate. Entry authorizes no hardware integration or testing, vehicle command path, live ledger/network publication, production authorization, or multi-tenant service or identity boundary.
- Discovery uses synthetic inputs or inputs covered by documented, approved governance for consent or other lawful basis, minimization, access, retention, and deletion. Raw or restricted participant/customer telemetry is not copied into fixtures, research reports, logs, or prototype outputs.
- `A0_SYNTHETIC` is the milestone's only demonstrator assurance tier. A relying party may state a higher required future tier, but that request neither upgrades demonstration evidence nor authorizes work needed to attain it.
- Every paper output is conspicuously labelled **“paper mockup — no proof generated”** and every non-cryptographic prototype output is conspicuously labelled **“non-cryptographic UX prototype — no proof generated or verified.”** The label appears on every screen, export, result, screenshot, recording, and research record, not only in accompanying instructions.

### Dependency graph and work items

The identifiers below are gates, not dates. An arrow means that accepted evidence from the item on the left is a prerequisite for the item on the right. Parallel branches may proceed only where the individual prerequisites permit.

```text
M1 -> M2 -> M3 -> M4 -> M5 -> M6 -> M7 --\
                    \          \-> M8 -> M9 -> M10 -> M11
                     \--------------^       /             ^
                      \--------------------/--------------/
```

More precisely: `M1 → M2 → M3`; `M3 → M4`; `M4 → M5`; `M4 + M5 → M6`; `M2 + M4 + M5 + M6 → M7`; `M3 + M4 + M5 + M6 → M8`; `M3 + M5 + M8 → M9`; `M4 + M8 + M9 → M10`; and `M1…M10 → M11`.

#### M1 — Reconcile the documentation baseline

- **Objective and rationale:** produce one contradiction register and an agreed authority map for claim, wire, result, assurance, discovery, testing, and decision language, so later executable evidence tests one contract rather than silently choosing among documents. This file remains the sole milestone-plan authority.
- **Existing documentation files affected:** `docs/delivery-plan.md`, `docs/README.md`, `docs/system-plan.md`, `docs/product-scope.md`, `docs/architecture.md`, `docs/data-and-proof-model.md`, `docs/claim-envelope.md`, `docs/security-and-privacy.md`, `docs/testing-and-operations.md`, `docs/discovery-research-plan.md`, and `docs/decisions.md`.
- **Proposed future artifacts/modules:** **Proposed:** `docs/reviews/validated-claim-contract/reconciliation-register.md` and `docs/reviews/validated-claim-contract/authority-map.md`.
- **Accountable role and required reviewers:** delivery lead accountable; product, architecture, cryptography, security, privacy, safety, telemetry, discovery, and relying-party role holders review.
- **Prerequisites:** milestone entry criteria satisfied.
- **Deliverables and acceptance evidence:** line-addressable conflict/duplication inventory, disposition and owner for every conflict, explicit normative-document precedence, and reviewer sign-off showing no unresolved contradiction can change a downstream test interpretation.
- **Principal risks:** paper agreement hides semantic conflict; a proposed artifact becomes a competing plan; broad editorial cleanup obscures substantive changes.
- **Relative size:** `S`.
- **Category:** documentation governance.
- **Decision or gate closed:** documentation-baseline approval and authority-map gate.
- **ADR requirement:** no new ADR unless reconciliation changes a previously accepted architectural decision; any such change amends or supersedes that ADR before acceptance.
- **Implementation exclusions:** no code, schema freeze, dependency selection, prototype, discovery claim, or production-readiness assertion.

#### M2 — Run paired provider/relying-party discovery

- **Objective and rationale:** observe both sides of the same evidence handoff and the actual relying-party decision, alternatives, harms, purchasing route, minimum disclosure, and assurance need; unpaired interest cannot validate a workflow.
- **Existing documentation files affected:** `docs/delivery-plan.md`, `docs/product-scope.md`, `docs/discovery-research-plan.md`, `docs/commercial-model.md`, `docs/security-and-privacy.md`, and `docs/decisions.md`.
- **Proposed future artifacts/modules:** **Proposed:** `docs/research/validated-claim-contract/paired-round/`, containing a sampling rationale, governed-input register, paired session records, disclosure comparisons, contradiction log, and evidence-to-decision summary.
- **Accountable role and required reviewers:** discovery lead accountable with product owner; relying-party, privacy, security, safety, and delivery role holders review, and the paired provider and relying-party participants validate factual notes.
- **Prerequisites:** accepted `M1`; approved research protocol and synthetic-or-governed input handling.
- **Deliverables and acceptance evidence:** rubric-complete paired records, contradictory and inconclusive cases, buyer/procurement visibility, workflow volumes and failure handling, unaided comprehension observations, and the product owner's explicit evidence-sufficiency disposition. Paper and non-cryptographic outputs carry the entry labels everywhere.
- **Principal risks:** recruiting convenience participants; producer answers substituted for relying-party authority; sensitive data capture; coached comprehension; overclaiming a small sample.
- **Relative size:** `L`.
- **Category:** product discovery.
- **Decision or gate closed:** whether evidence is sufficient to select, narrow, or reject the candidate workflow for claim contracting; this does not by itself pass product-scope Gate 1.
- **ADR requirement:** none; material product decisions are recorded in `docs/decisions.md`, not an architecture ADR.
- **Implementation exclusions:** no real proof, authenticated-artifact claim, hardware, command, live-ledger, production, multi-tenant, pricing, pilot, or willingness-to-pay claim.

#### M3 — Bound the claim and relying-party decision

- **Objective and rationale:** select an exact observation unit and predicate and state what the result can and cannot support, preventing a speed snapshot from being promoted into interval, segment, whole-flight, safety, contractual, or regulatory compliance.
- **Existing documentation files affected:** `docs/delivery-plan.md`, `docs/product-scope.md`, `docs/data-and-proof-model.md`, `docs/claim-envelope.md`, `docs/security-and-privacy.md`, `docs/discovery-research-plan.md`, and `docs/decisions.md`.
- **Proposed future artifacts/modules:** **Proposed:** `docs/contracts/bounded-speed/claim-scope-draft.md`, `schemas/claims/bounded-speed-draft.cddl`, and `testdata/synthetic/bounded-speed/README.md`.
- **Accountable role and required reviewers:** product owner accountable; relying-party, telemetry, architecture, cryptography, privacy, safety, and security role holders review.
- **Prerequisites:** accepted `M2` evidence-sufficiency disposition.
- **Deliverables and acceptance evidence:** selected-or-rejected workflow decision; named producer, relying party, decision and false-accept/false-reject consequences; predicate, units, bounds, observation/coverage semantics, public/private field map, non-claims, and synthetic examples reviewed against discovery evidence.
- **Principal risks:** ambiguous coverage; unit or integer-bound errors; policy language implies physical truth; restricted disclosure; a research hypothesis is mistaken for a supported product claim.
- **Relative size:** `M`.
- **Category:** product and claim contract.
- **Decision or gate closed:** claim-scope portion of product-scope Gate 1 and the bounded-speed statement candidate decision.
- **ADR requirement:** an ADR is required only if the selected scope changes an architectural boundary; statement identifier/version freeze remains a later ADR-backed release decision.
- **Implementation exclusions:** no circuit, prover, verifier, parser, SITL integration, continuous/aggregate claim, hardware provenance, or external authorization.

#### M4 — Freeze draft result and time semantics for testing

- **Objective and rationale:** reconcile typed independent verifier dimensions, precedence, explicit decision time, observation/validity windows, freshness, replay, revocation, and the external business-decision boundary so every later fixture has one deterministic expected result.
- **Existing documentation files affected:** `docs/delivery-plan.md`, `docs/claim-envelope.md`, `docs/data-and-proof-model.md`, `docs/architecture.md`, `docs/testing-and-operations.md`, `docs/decisions.md`, `docs/adr/0001-half-open-validity-windows.md`, and `docs/adr/0002-typed-verifier-result-model.md`.
- **Proposed future artifacts/modules:** **Proposed:** `schemas/verifier/result-draft.cddl`, `testdata/contracts/result-time/`, and `docs/contracts/verifier/result-time-crosswalk.md`.
- **Accountable role and required reviewers:** cryptography lead accountable; architecture, security, product, relying-party, privacy, telemetry, and delivery role holders review.
- **Prerequisites:** accepted `M3` claim boundary and `M1` authority map.
- **Deliverables and acceptance evidence:** cross-document semantic matrix; boundary and cross-dimensional expected-result vectors; explicit clock authority and integer decision times; deterministic precedence; proof result kept separate from service disposition and business decision; reviewers reproduce expected outcomes without oral interpretation.
- **Principal risks:** collapsing independent dimensions; wall-clock nondeterminism; consuming replay state too early; treating cryptographic validity as policy or business acceptance.
- **Relative size:** `M`.
- **Category:** verifier contract.
- **Decision or gate closed:** testable draft result/time contract and typed-outcome precedence gate.
- **ADR requirement:** required; accept or amend ADR-0001 and ADR-0002 before this item closes, with a new ADR for any incompatible semantic choice.
- **Implementation exclusions:** no public API stability, production clock/replay store, UI approval action, real proof verification, or relying-party business automation.

#### M5 — Define assurance and disclosure presentation

- **Objective and rationale:** keep declared, effective, required, and demonstrator assurance distinct and make exclusions and public disclosure understandable; proof strength must not be presented as telemetry provenance or truth.
- **Existing documentation files affected:** `docs/delivery-plan.md`, `docs/security-and-privacy.md`, `docs/claim-envelope.md`, `docs/data-and-proof-model.md`, `docs/product-scope.md`, `docs/discovery-research-plan.md`, and `docs/decisions.md`.
- **Proposed future artifacts/modules:** **Proposed:** `docs/contracts/assurance/a0-disclosure-profile.md`, `schemas/registries/assurance-tier-draft.json`, and `testdata/contracts/assurance-disclosure/`.
- **Accountable role and required reviewers:** security lead accountable with privacy lead; product, cryptography, safety, telemetry, discovery, and relying-party role holders review.
- **Prerequisites:** accepted `M2`, `M3`, and `M4`.
- **Deliverables and acceptance evidence:** field-by-field disclosure map; canonical `A0_SYNTHETIC` presentation and non-claims; separate record of any relying-party requested future tier and evidence gap; linkage/re-identification review; positive/negative presentation examples; unaided reviewer correctly distinguishes proof validity, assurance sufficiency, and business decision.
- **Principal risks:** ordinal tiers imply guaranteed truth; hidden linkability; requested future tier is presented as attained; prototype labels are lost in exports.
- **Relative size:** `M`.
- **Category:** security and privacy contract.
- **Decision or gate closed:** milestone assurance/disclosure vocabulary and `A0_SYNTHETIC` demonstrator-profile gate.
- **ADR requirement:** required before the assurance registry is frozen; the ADR records alternatives, linkage and migration consequences, with explicit product/privacy and security approval. The milestone may test a visibly draft registry before that freeze.
- **Implementation exclusions:** no `A1`–`A5` attainment, device/gateway keys, attestation, sensor-truth claim, hardware work, stable assurance registry, or production authorization.

#### M6 — Specify executable offline policy fixtures

- **Objective and rationale:** turn policy lifecycle and explicit-time rules into deterministic, authenticated test evidence without a registry, network dependency, ambient trust store, or production authority.
- **Existing documentation files affected:** `docs/delivery-plan.md`, `docs/data-and-proof-model.md`, `docs/claim-envelope.md`, `docs/security-and-privacy.md`, `docs/testing-and-operations.md`, and `docs/decisions.md`.
- **Proposed future artifacts/modules:** **Proposed:** `schemas/fixtures/offline-policy-v0.json`, `testdata/policy/offline-v0/`, and `tools/fixture-checker/` (disposable Phase 0 checker).
- **Accountable role and required reviewers:** security lead accountable; cryptography, architecture, privacy, testing/operations, delivery, and relying-party role holders review.
- **Prerequisites:** accepted `M4` and `M5` semantics.
- **Deliverables and acceptance evidence:** fixture schema; immutable policy bytes and recomputed digests; conspicuously test-only trust anchors and deterministic signatures; explicit decision-time vectors for approval, activation, both half-open boundaries, deprecation, revocation/recheck, expiry, rollback, ordering, tampering, missing and incompatible evidence; checker output proving fail-closed behavior and `TEST_ONLY_NOT_PRODUCTION_AUTHORIZATION` on every result.
- **Principal risks:** fixture keys mistaken for secrets or production roots; expected labels trusted instead of signatures/digests; nondeterminism; offline fixture semantics diverge from the contract.
- **Relative size:** `L`.
- **Category:** security test infrastructure.
- **Decision or gate closed:** deterministic test-only offline policy-profile readiness gate.
- **ADR requirement:** no ADR for disposable fixture mechanics; an ADR is required before any policy schema, trust topology, or lifecycle contract is frozen for release.
- **Implementation exclusions:** no network registry, mutable `latest`, production keys, production authorization, online freshness claim, operational key ceremony, or reusable production policy service.

#### M7 — Validate verifier UX and relying-party interpretation

- **Objective and rationale:** test whether a relying-party reviewer can independently explain accepted, rejected, and temporarily unverifiable outcomes, scope, assurance, time/replay limits, and non-claims before an implementation interface is selected.
- **Existing documentation files affected:** `docs/delivery-plan.md`, `docs/product-scope.md`, `docs/discovery-research-plan.md`, `docs/claim-envelope.md`, `docs/security-and-privacy.md`, `docs/testing-and-operations.md`, and `docs/architecture.md`.
- **Proposed future artifacts/modules:** **Proposed:** `prototypes/verifier-ux-noncrypto/`, `docs/research/validated-claim-contract/verifier-ux/`, and `testdata/ux/verifier-results/`.
- **Accountable role and required reviewers:** product owner accountable with discovery lead; relying-party, accessibility, privacy, security, safety, cryptography, and delivery role holders review.
- **Prerequisites:** accepted `M2`, `M4`, `M5`, and `M6`; only synthetic fixture outputs used.
- **Deliverables and acceptance evidence:** labelled paper/non-cryptographic prototype; task script and pre-agreed comprehension threshold; uncoached positive and negative sessions; observed errors, accessibility notes and wording revisions; exports preserve full typed result, decision time, `A0_SYNTHETIC`, test-only classification, and the external-decision boundary.
- **Principal risks:** polished mockup implies working verification; binary color/status hides dimensions; coaching; inaccessible presentation; research record loses mandatory label.
- **Relative size:** `M`.
- **Category:** verifier experience and discovery.
- **Decision or gate closed:** verifier-comprehension evidence and presentation-language gate, not proof verification or commercial validation.
- **ADR requirement:** none for paper or disposable non-cryptographic research; an ADR is required later only if a stable public interface or architectural UI boundary is selected.
- **Implementation exclusions:** no cryptography, proof generation/verification, network call, vendor verdict, authorization control, production UI, account, multi-tenancy, payment, command, or pilot.

#### M8 — Execute the envelope and vector spike

- **Objective and rationale:** demonstrate strict canonical decoding, deterministic re-encoding, reconstructed ordered public inputs, mutation rejection, and independent format agreement before treating the draft envelope as executable. Opaque placeholder proof bytes isolate format questions from proof-system selection.
- **Existing documentation files affected:** `docs/delivery-plan.md`, `docs/claim-envelope.md`, `docs/data-and-proof-model.md`, `docs/testing-and-operations.md`, `docs/architecture.md`, and `docs/decisions.md`.
- **Proposed future artifacts/modules:** **Proposed:** `schemas/envelope/v0-spike.cddl`, `crates/envelope-spike/` (disposable reference codec), `tools/envelope-vector-checker/` (independently authored disposable checker), and `testdata/envelope/v0-spike/`.
- **Accountable role and required reviewers:** architecture lead accountable; cryptography, security, privacy, telemetry, testing/operations, and delivery role holders review.
- **Prerequisites:** accepted `M3`, `M4`, `M5`, and `M6` contracts.
- **Deliverables and acceptance evidence:** shared golden and negative corpus; rejection of non-canonical, duplicate, unknown, invalid, out-of-bound and unsupported data; byte-identical re-encoding; field-by-field mutations including proof attachment/reference shape; public-input reconstruction; reference/checker agreement; documented clean-checkout command.
- **Principal risks:** shared logic defeats independence; placeholder acceptance is described as proof verification; premature version/API stability; corpus omits interpretation-critical mutations.
- **Relative size:** `L`.
- **Category:** disposable interoperability spike.
- **Decision or gate closed:** executable format-spike gate only; release still requires two genuinely independent implementations in different languages and its release ADR.
- **ADR requirement:** no proof-system ADR and no released-envelope ADR are required for this disposable spike; an accepted release ADR is mandatory before the envelope is called released, interoperable, or stable.
- **Implementation exclusions:** no circuit, proof generation, cryptographic verification, proof-system benchmark dependency, stable library/API, production hardening, or claim that placeholder bytes are a proof. In particular, `M10` does **not** block this item.

#### M9 — Establish pinned SITL compatibility evidence

- **Objective and rationale:** prove that a selected simulator/autopilot, MAVLink dialect, message set, units, ranges, timing and signing/trust states can supply the bounded synthetic record without widening the claim or silently coercing unavailable data.
- **Existing documentation files affected:** `docs/delivery-plan.md`, `docs/data-and-proof-model.md`, `docs/architecture.md`, `docs/testing-and-operations.md`, `docs/security-and-privacy.md`, `docs/product-scope.md`, and `docs/decisions.md`.
- **Proposed future artifacts/modules:** **Proposed:** `testdata/sitl/compatibility/`, `tools/sitl-compat-probe/` (disposable probe), and `docs/evidence/sitl/compatibility-matrix.md`.
- **Accountable role and required reviewers:** telemetry lead accountable; architecture, security, safety, cryptography, product, privacy, and delivery role holders review.
- **Prerequisites:** accepted `M3` claim fields, `M5` trust/disclosure profile, and `M8` envelope/public-input draft.
- **Deliverables and acceptance evidence:** pinned simulator/autopilot, dialect and message/profile versions; executable compatibility matrix for `GLOBAL_POSITION_INT` and `VFR_HUD` candidate fields; synthetic capture/replay digests; unit/range/availability/signing-state results; deterministic normalization samples; documented rejection of malformed, mixed-source, stale, invalid-signature and unsupported inputs.
- **Principal risks:** simulator behavior mistaken for flight hardware; dialect drift; mismatched clocks/units; unsigned data overstated; compatibility probe grows into an ingestion service.
- **Relative size:** `L`.
- **Category:** telemetry compatibility evidence.
- **Decision or gate closed:** initial SITL/autopilot, dialect, message and signing-profile decision needed for Phase 1 entry and proof-system comparison inputs.
- **ADR requirement:** an ADR is required only if the selected profile establishes a durable architectural or dependency commitment; the evidence-backed selection is always recorded in `docs/decisions.md`.
- **Implementation exclusions:** no hardware/vehicle connection, command transmission, real flight, generalized MAVLink support, production parser/gateway, live network, or assurance above `A0_SYNTHETIC`.

#### M10 — Benchmark candidate proof systems

- **Objective and rationale:** compare candidate proof systems against the accepted claim/result/time contract and pinned SITL-derived synthetic records so the proof-system decision is evidence-based rather than chosen before statement shape and workload are known.
- **Existing documentation files affected:** `docs/delivery-plan.md`, `docs/data-and-proof-model.md`, `docs/claim-envelope.md`, `docs/testing-and-operations.md`, `docs/architecture.md`, `docs/security-and-privacy.md`, and `docs/decisions.md`.
- **Proposed future artifacts/modules:** **Proposed:** `benchmarks/proof-systems/`, `testdata/proof-benchmarks/bounded-speed/`, `docs/evidence/cryptography/proof-system-comparison.md`, and `docs/adr/0003-proof-system-selection.md`.
- **Accountable role and required reviewers:** cryptography lead accountable; architecture, security, telemetry, privacy, safety, engineering, delivery, and relying-party role holders review.
- **Prerequisites:** accepted `M4` contract semantics, completed `M8` envelope/vector evidence, and accepted `M9` pinned SITL compatibility corpus. Contract or SITL changes invalidate affected benchmark results.
- **Deliverables and acceptance evidence:** reproducible disposable harness; at least the viable candidates and a documented rejection rationale for excluded candidates; valid/boundary/altered-input measurements on representative declared hardware; parameters, versions, setup and sample counts; proof size, generation and verification p50/p95/p99, peak memory and throughput; security/assumption, licensing, portability, key/setup and lifecycle comparison; draft proof-system ADR with raw results.
- **Principal risks:** toy benchmark does not constrain the real statement; incomparable tuning; unsafe candidate assumptions; benchmark prototype is promoted into product code; performance is represented as an SLO.
- **Relative size:** `XL`.
- **Category:** cryptographic technology decision.
- **Decision or gate closed:** candidate proof-system selection and permission to begin real Phase 2 proof implementation. The benchmark is mandatory **after contract and SITL evidence and before real Phase 2 circuit/prover/verifier implementation**; it is deliberately **not** a prerequisite for the placeholder-proof envelope/vector spike in `M8`.
- **ADR requirement:** required; the proof-system ADR is accepted by cryptography and security, with architecture review, before real Phase 2 proof implementation begins.
- **Implementation exclusions:** only disposable benchmark implementations are allowed; no production circuit/prover/verifier, production parameters or ceremony, stable proof format/API, performance SLO, hardware telemetry, or production-readiness claim.

#### M11 — Conduct the final stop/go review

- **Objective and rationale:** decide from the complete evidence whether the validated claim/verifier contract is coherent and valuable enough to authorize only the bounded next phase, while making unresolved and residual risks explicit.
- **Existing documentation files affected:** `docs/delivery-plan.md`, `docs/product-scope.md`, `docs/architecture.md`, `docs/data-and-proof-model.md`, `docs/claim-envelope.md`, `docs/security-and-privacy.md`, `docs/testing-and-operations.md`, `docs/discovery-research-plan.md`, and `docs/decisions.md`.
- **Proposed future artifacts/modules:** **Proposed:** `docs/reviews/validated-claim-contract/stop-go-record.md` and `docs/reviews/validated-claim-contract/evidence-index.md`.
- **Accountable role and required reviewers:** delivery lead accountable; named product, architecture, cryptography, security, privacy, safety, telemetry, discovery, and relying-party role holders are required approvers, with engineering consulted on feasibility.
- **Prerequisites:** `M1` through `M10` accepted; required ADRs accepted; evidence index immutable or content-addressed for review; open blockers have owners and closure gates.
- **Deliverables and acceptance evidence:** item-by-item evidence index; approval/rejection and dissent; threat and privacy review; discovery sufficiency decision; selected claim, SITL and proof-system dispositions; recorded approvers, unresolved risks and accepted residual risk; explicit scope authorized by a go and explicit stop conditions.
- **Principal risks:** schedule pressure waives evidence; conditional approvals hide blockers; technical evidence substitutes for discovery; go language is read as production, safety, or commercial approval.
- **Relative size:** `M`.
- **Category:** milestone governance.
- **Decision or gate closed:** final **stop/go** for the Validated claim and verifier contract milestone and, only on go, authorization for the bounded Phase 1 scope plus subsequent real Phase 2 proof work in dependency order.
- **ADR requirement:** all ADRs required by `M4`, `M5`, `M8` release claims (if any), and `M10` must be accepted; the review record is not itself an ADR.
- **Implementation exclusions:** no waiver of prerequisites; no declaration of production/security/safety/regulatory/commercial readiness; no hardware, command, live ledger, multi-tenant service, pilot, or deployment authorization.

Bounded, disposable Phase 0 spikes are permitted solely where an item above allows them and solely to answer its named questions. They are not production foundations and MUST NOT be represented as implemented product capabilities. `docs/delivery-plan.md` remains the milestone authority: proposed evidence indexes, research records, contracts, ADRs, fixtures, and review records support this plan and MUST link back here rather than restating or superseding its sequence or gates.

**Required evidence:** the applicable Phase 0 deliverables and exit evidence below, including strict-decoding and mutation vectors, independent format checking, deterministic test-only policy artifacts, reviewed public/private fields and trust terms, closure plans for MVP-blocking decisions, threat review, and accepted product-scope Gate 1 evidence. Each artifact records its disposable or test-only status where applicable.

**Exit and stop/go rules:** the accountable reviewers conduct an explicit milestone review against the entry, workstream, and required evidence. A **go** requires acceptance of all Phase 0 exit evidence and records approvers, unresolved risks, and any accepted residual risk. A failed, incomplete, or inconclusive review is a **stop**: bounded Phase 0 investigation may continue, but broad Phase 1 production engineering MUST NOT begin. Passing this review authorizes only the proposed Phase 1 scope; it does not establish implementation, production, security, safety, commercial, or deployment readiness.

## Phase 0 — decision framing and scaffold

**Entry:** documentation baseline approved.

### Executable format spike gate

Before the claim-envelope format can be treated as a released version, the Phase 0 spike MUST provide executable evidence for all of the following using placeholder proof bytes:

- strict decoding that rejects non-canonical encodings, duplicate or unknown fields, invalid types and bounds, and unsupported versions;
- deterministic re-encoding with byte-for-byte comparison against the input and shared golden vectors;
- reconstruction of the ordered public inputs from envelope fields rather than acceptance of a caller-supplied public-input byte sequence;
- rejection of mutations to each interpretation-critical field, proof attachment/reference shape, and expected verifier outcome; and
- comparison between one reference codec and an independently authored lightweight decoder or vector checker that agrees on accepted bytes, reconstructed public inputs, rejection cases, and typed outcomes.

This is a format and interoperability spike. It MUST NOT require a circuit implementation, proof generation, or cryptographic proof verification; opaque placeholder proof bytes are sufficient. The independent checker MAY be throwaway and MAY use the same language as the reference codec. The two-language release gate therefore does not block early synthetic discovery fixtures or an intentionally disposable schema spike. Field numbers and names, the canonical profile, proof attachment rules, and the outcome schema remain pre-standard and MAY change incompatibly until the gate passes.

Promotion to a released interoperable envelope or stable public API requires two genuinely independent implementations in different languages, with no shared envelope codec or verification business-logic library, to pass the released vector corpus and exchange the required fresh evidence. The accepted release ADR MUST identify the frozen contract and link those results as well as the executable vectors and mutation results; documentation edits or use of a version number alone cannot promote it. Cross-proof-system or cross-edition verification MUST be demonstrated in every claimed direction, using the corresponding proof/public-input and negative vectors, before making that compatibility claim; single-system or single-edition evidence cannot satisfy that gate.

**Deliverables:** minimal workspace/toolchain; one documented format/lint/test/schema command; dependency policy; ADR template/process; canonical schema draft; synthetic fixtures; executable format-spike vectors, a reference codec, and an independent lightweight decoder or vector checker; the versioned schema and checked-in material for the [test-only offline policy profile](data-and-proof-model.md#test-only-offline-policy-profile), including immutable policy bytes, pinned test trust anchors, deterministic signed status fixtures, and explicit decision times; refreshed threat review.

**Exit evidence:** clean checkout passes the documented command; the executable format spike passes every strict-decode, deterministic re-encoding, public-input reconstruction, mutation-rejection, and reference-codec/independent-checker comparison case with placeholder proof bytes; the offline policy fixture schema validates every checked-in policy, anchor, event, checkpoint, and decision-time vector, recomputed digests and fixture signatures match, and all artifacts are visibly isolated as test-only and incapable of production authorization; the two-independent-implementation, two-language evidence and release ADR are accepted before any envelope is described as released or interoperable or any public API as stable; product, telemetry, cryptography, and security approve public/private fields and trust vocabulary; owners and due gates exist for all Open MVP-blocking decisions; no unhandled critical threat blocks Phase 1. The product-scope Gate 1 problem/workflow record is accepted under the approved sampling rationale and evidence-sufficiency rule: paired provider/relying-party coverage, actual buyer or procurement visibility, contradictory and inconclusive cases, sampling limitations, and the product owner's explicit sufficiency determination are documented alongside the producer, workflow, disclosure map, snapshot-versus-coverage acceptance, purchasing route/budget holder, observed volume/review time, failure handling, and prototype comprehension. Any paper or non-cryptographic prototype bears the required no-proof label.

**Accountable:** architecture and delivery leads. This phase supplies the bounded evidence for the [**Validated claim and verifier contract**](#next-milestone--validated-claim-and-verifier-contract) stop/go review.

## Phase 1 — telemetry vertical slice

**Depends on:** a **go** decision at the [**Validated claim and verifier contract**](#next-milestone--validated-claim-and-verifier-contract) review, including accepted Phase 0 schema/trust evidence and a selected SITL profile. Broad Phase 1 production engineering is blocked until that decision is recorded.

**Deliverables:** pinned SITL scenario; allowlisted parser; trust classification; normalizer; bounded channel; deterministic record/replay fixture; ingress metrics; fuzz target.

**Exit evidence:** repeated fixture runs produce identical canonical records; supported units/ranges are verified; malformed, unsupported, mixed-source, stale, and invalid-signature inputs reject; sequence gaps and overload drops are observable; fuzzing runs in CI or scheduled automation. Gate 1 remains valid or is reopened if Phase 1 findings change the actors, workflow, disclosure map, snapshot limitation, or claim wording; Phase 1 telemetry output is not presented as a proof or independently verified result.

**Accountable:** telemetry lead.

## Phase 2 — proof spike and local verification

**Depends on:** Phase 1 golden canonical records and approved encoding draft.

**Deliverables:** candidate benchmark harness; bounded-speed circuit; golden vectors and real proofs; authenticated, portable verification/policy/revocation artifacts; independent verifier; executable lifecycle vectors using the Phase 0 test-only offline policy profile; proof-system ADR; version/key lifecycle draft.

**Exit evidence:** valid, equality-boundary, altered-input, overflow, stale, replay, wrong-version/policy/domain cases behave as specified; against the Phase 0 offline fixture, the independent verifier exercises approval/activation ordering, both effective-window boundaries at explicit decision times, deprecation, revocation and pre-revocation-claim recheck, expiry, compatible rollback, compatibility rejection, ordered checkpoints, signature/digest tampering, and missing or unauthorized evidence, with the specified audit fields and fail-closed reason codes; the verifier rejects the fixture profile outside explicit test configuration and labels every result `TEST_ONLY_NOT_PRODUCTION_AUTHORIZATION`; verifier receives no witness; report states hardware, parameters, p50/p95/p99, memory, proof size, and throughput; cryptography/security review accepts the ADR. Product-scope Gate 2 then passes at least three real-proof workflows for each of two paired provider/relying-party evaluation teams (at least six total), with 100% correct agreed positive/negative outcomes, authenticated artifacts, independent verification, human interpretation, restricted-field absence from the proof and verification materials, tested disclosure preference, assurance sufficiency, snapshot limitations, comprehension, review time, objections, and failure reasons. Mockups, non-cryptographic prototypes, producer self-verification, or vendor-only verification do not qualify.

**Accountable:** cryptography lead.

## Phase 3 — mock adapter and operator boundary (MVP cutoff)

**Depends on:** Phase 2 accepted local proof semantics.

**Deliverables:** chain port and deterministic mock; versioned offline evidence package and experimental non-interactive verifier CLI or minimal library; only the persistence needed for lifecycle/idempotency; the smallest authenticated single-organization or explicitly non-multi-tenant submit/status API, and a minimal status UI, only if validated workflow evidence justifies them.

**Exit evidence:** the synthetic fixture reaches `FINALIZED` offline; offline independent verification remains possible without a vendor service or network dependency; duplicates do not duplicate state wherever mutations exist; applicable retry/restart/outage tests pass; files, verifier output, logs, mock records, and any justified UI/API contain no restricted data; stable machine-readable errors and non-interactive verification are tested; accessibility baseline is reviewed if a UI exists. The milestone record reports all six rubric results: Gate 2 supplies privacy improvement, verifier comprehension, and assurance sufficiency; Gate 3 supplies acceptable integration effort, performance fit, and pilot intent. After the offline package exists and before a pilot, product-scope Gate 3 requires two written paired provider/relying-party design-partner commitments, both pairs' package integrations without a vendor service or network dependency, positive and negative cases with human interpretation, pre-agreed integration/performance results, restricted-field absence across the Phase 3 surfaces, buyer preference, and purchasing evidence consisting of the validated route and budget holder, a credible paid-pilot price, and an executed paid-pilot agreement or another completed purchase. Every criterion must pass; a demonstration, informal interest, or pilot intent alone is insufficient.

**Accountable:** engineering lead, with security and product approval.

Completion of the Phase 3 exit evidence and the MVP definition of done marks the
MVP cutoff. The remaining phases are optional post-MVP progression and are not
required to complete or accept the MVP.

## Phase 4 — post-MVP Midnight compatibility test environment

**Entry gate:** an ADR identifies a supported SDK/network/contract language, proof-verification route, disclosure behavior, expected cost model, and finality semantics using executable spike evidence.

**Deliverables:** pinned adapter; test-environment contract; transaction watcher/reconciliation; key runbook.

**Exit evidence:** submit, retry, timeout, finality, and reorganization scenarios pass; live and mock adapters pass one contract suite; public metadata passes privacy review; rotation and rollback are exercised.

**Accountable:** chain lead. Live production deployment remains Deferred.

## Phase 5 — post-MVP hardening and controlled hardware pilot

**Entry gate:** Phases 0–4 evidence complete; service objectives/capacity proposal based on measurements; product/privacy obligations defined; safety owner approves hazard analysis and controlled hardware test plan.

**Deliverables:** performance envelope; dependency/SBOM/image evidence as applicable; backup/restore and incident runbooks; external security/privacy review; isolated hardware-pilot procedure.

**Exit evidence:** approved SLOs and limits; high-severity findings resolved or explicitly accepted; rollback, restore, key rotation, overload, and dependency-outage exercises pass; hardware test preserves the no-command boundary.

**Accountable:** service owner/SRE and safety owner. This gate does not authorize production.

### Deferred production deployment gate

Neither the offline fixture profile nor completion of Phases 0–5 authorizes production. A future production deployment gate MUST separately approve and exercise the authoritative registry services, online cache-freshness and freeze/outage controls, operational approval quorum, break-glass custody and handling, and production trust-root and key ceremonies (including provisioning, protection, rotation, revocation, recovery, and audit). Until that gate has named accountable operators, accepted governance and architecture, and linked runbook/drill evidence, each of these capabilities and every production authorization that depends on them remains Deferred. Test trust anchors, deterministic fixture signatures, and offline lifecycle results MUST NOT be cited as substitute evidence.

## Definition of done for the MVP

- One pinned synthetic scenario is reproducible in default offline CI.
- Normative data/proof semantics have reviewed vectors and an accepted proof-system ADR.
- Required positive, negative, fuzz, security, privacy, resilience, and benchmark evidence is linked.
- The mock adapter is the only required chain dependency; no restricted field crosses operator or chain boundaries.
- No vehicle command path exists.
- All lifecycle transitions, drops, failures, duplicates, and retries are observable and bounded.
- Accepted ADRs, supported versions, known limitations, and residual risks are recorded.

Phases 4–5 are outside the MVP. Hardware, live-chain, or production work requires the explicit post-MVP entry evidence above; completion of the preceding code alone is insufficient.

## Related documents and validation

[Product scope](product-scope.md) owns outcomes, [architecture](architecture.md) owns boundaries, [testing and operations](testing-and-operations.md) owns evidence methods, and [decisions](decisions.md) owns closure. Validate this plan by milestone review against every listed artifact, gate, owner, and dependency.
