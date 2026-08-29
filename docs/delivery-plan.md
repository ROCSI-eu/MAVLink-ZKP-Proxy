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

**Entry:** the documentation baseline is approved, the bounded-speed claim and relying-party decision to be tested are identified, and accountable product, architecture, cryptography, security, and delivery roles agree on the questions that the Phase 0 evidence must resolve.

**Workstream:** refine the claim envelope, canonical public-input reconstruction, typed verifier outcomes, trust vocabulary, test-only offline policy profile, and product-discovery record. Bounded, disposable Phase 0 spikes are permitted solely to answer those questions and produce reviewable evidence. They may include throwaway codecs, vector checkers, schema experiments, synthetic fixtures, paper mockups, or conspicuously labelled non-cryptographic offline UX prototypes. They are not production foundations and MUST NOT be represented as implemented product capabilities.

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

**Exit evidence:** clean checkout passes the documented command; the executable format spike passes every strict-decode, deterministic re-encoding, public-input reconstruction, mutation-rejection, and reference-codec/independent-checker comparison case with placeholder proof bytes; the offline policy fixture schema validates every checked-in policy, anchor, event, checkpoint, and decision-time vector, recomputed digests and fixture signatures match, and all artifacts are visibly isolated as test-only and incapable of production authorization; the two-independent-implementation, two-language evidence and release ADR are accepted before any envelope is described as released or interoperable or any public API as stable; product, telemetry, cryptography, and security approve public/private fields and trust vocabulary; owners and due gates exist for all Open MVP-blocking decisions; no unhandled critical threat blocks Phase 1. The product-scope Gate 1 problem/workflow record is accepted: interview counts and problem confirmations pass; buyer, producer, relying-party, workflow, disclosure map, snapshot-versus-coverage acceptance, purchasing route/budget holder, observed volume/review time, failure handling, and prototype comprehension are documented. Any paper or non-cryptographic prototype bears the required no-proof label.

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
