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

## Phase 0 — decision framing and scaffold

**Entry:** documentation baseline approved.

**Deliverables:** minimal workspace/toolchain; one documented format/lint/test/schema command; dependency policy; ADR template/process; canonical schema draft; synthetic fixtures; refreshed threat review.

**Exit evidence:** clean checkout passes the documented command; product, telemetry, cryptography, and security approve public/private fields and trust vocabulary; owners and due gates exist for all Open MVP-blocking decisions; no unhandled critical threat blocks Phase 1. The product-scope Gate 1 problem/workflow record is accepted: interview counts and problem confirmations pass; buyer, producer, relying-party, workflow, disclosure map, snapshot-versus-coverage acceptance, purchasing route/budget holder, observed volume/review time, failure handling, and prototype comprehension are documented. Any paper or non-cryptographic prototype bears the required no-proof label.

**Accountable:** architecture and delivery leads. This is the **next implementation step**.

## Phase 1 — telemetry vertical slice

**Depends on:** Phase 0 schema/trust review and selected SITL profile.

**Deliverables:** pinned SITL scenario; allowlisted parser; trust classification; normalizer; bounded channel; deterministic record/replay fixture; ingress metrics; fuzz target.

**Exit evidence:** repeated fixture runs produce identical canonical records; supported units/ranges are verified; malformed, unsupported, mixed-source, stale, and invalid-signature inputs reject; sequence gaps and overload drops are observable; fuzzing runs in CI or scheduled automation. Gate 1 remains valid or is reopened if Phase 1 findings change the actors, workflow, disclosure map, snapshot limitation, or claim wording; Phase 1 telemetry output is not presented as a proof or independently verified result.

**Accountable:** telemetry lead.

## Phase 2 — proof spike and local verification

**Depends on:** Phase 1 golden canonical records and approved encoding draft.

**Deliverables:** candidate benchmark harness; bounded-speed circuit; golden vectors and real proofs; authenticated, portable verification/policy/revocation artifacts; independent verifier; proof-system ADR; version/key lifecycle draft.

**Exit evidence:** valid, equality-boundary, altered-input, overflow, stale, replay, wrong-version/policy/domain cases behave as specified; verifier receives no witness; report states hardware, parameters, p50/p95/p99, memory, proof size, and throughput; cryptography/security review accepts the ADR. Product-scope Gate 2 then passes at least three real-proof workflows for each of two paired provider/relying-party evaluation teams (at least six total), with 100% correct agreed positive/negative outcomes, authenticated artifacts, independent verification, human interpretation, restricted-field absence from the proof and verification materials, tested disclosure preference, assurance sufficiency, snapshot limitations, comprehension, review time, objections, and failure reasons. Mockups, non-cryptographic prototypes, producer self-verification, or vendor-only verification do not qualify.

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
