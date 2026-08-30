# M2 paired-discovery entry readiness record

| Record field | Value |
| --- | --- |
| Work item | `M2` — Run paired provider/relying-party discovery |
| Record date | 2026-08-30 |
| Status | **Open** — entry conditions are not satisfied |
| Current disposition | `M2` remains `blocked`; `gate_closed=false` |
| Accountable role | Discovery lead with product owner |
| Primary tracker | [Issue #49](https://github.com/ROCSI-eu/Telemetry-Attestation-Gateway/issues/49) |
| Downstream tracker | [Issue #50](https://github.com/ROCSI-eu/Telemetry-Attestation-Gateway/issues/50), blocked by issue #49 |
| Authority | [`docs/delivery-plan.md`](../../delivery-plan.md), [`docs/discovery-research-plan.md`](../../discovery-research-plan.md), and the [`M1` authority map](authority-map.md) |

## Purpose and non-authorization

This record coordinates the evidence required to move `M2` from `blocked` to `in_progress`. It is not an approval record and does not itself satisfy an entry condition.

The accepted `M1` baseline is a documentation-only maturity state. This record does not authorize participant-data collection, interviews, completed research records, a prototype, proof generation or verification, telemetry or SITL integration, hardware, a vehicle command path, live publication, a pilot, pricing, or production activity.

The industrial-site inspection workflow and its buyer, relying-party decision, coverage unit, disclosure need, assurance requirement, volume, purchasing path, pilot intent, and willingness to pay remain hypotheses or **Open** questions. Bounded horizontal speed remains the first technical primitive, not an approved compliance product.

## Current entry-state assessment

| Entry condition | Required owner or reviewers | Current status | Evidence or blocker |
| --- | --- | --- | --- |
| Accepted documentation-only `M1` baseline | Delivery lead and required `M1` reviewers | **Current / satisfied** | `authority-map.md` and `reconciliation-register.md` |
| Named individuals for product, delivery, architecture, cryptography, security, privacy, safety, telemetry, discovery, and relying-party decision ownership | Delivery lead; each named role holder acknowledges accountability | **Open** | Existing role identifiers do not establish the named-individual and acknowledgement requirement |
| Approved bounded paired-discovery protocol and evidence-sufficiency method | Product owner; discovery-method and delivery review | **Open** | `docs/discovery-research-plan.md` remains a Proposed protocol and records no approval or findings |
| Approved research and input-handling arrangement | Product owner and privacy owner; security and delivery review where applicable | **Open** | No dated handling approval reference, scope, expiry/review trigger, or permitted repository disclosure has been recorded |
| Synthetic-or-governed inputs | Product owner and privacy owner | **Open** | No approved input class or governed-data reference has been recorded for `M2` execution |
| Hypothesis and non-claim boundary acknowledged | Product, discovery, relying-party, privacy, safety, security, and delivery reviewers | **Open** | Repository rules are documented, but the complete `M2` entry acknowledgement set is absent |
| Demonstrator assurance restricted to `A0_SYNTHETIC` | Security lead with product/privacy and relying-party review | **Open** | `A0_SYNTHETIC` is the only Current demonstrator tier, but the required entry acknowledgement is not recorded |
| Mandatory output labels | Product, discovery, privacy, security, safety, and delivery reviewers | **Open** | Every paper output must state **“paper mockup — no proof generated”**; every non-cryptographic output must state **“non-cryptographic UX prototype — no proof generated or verified”** on every surface and research record |
| Complete entry disposition | Delivery lead after all required evidence and reviews | **Open** | `milestone_entry_criteria_not_satisfied` remains the valid register blocker |

## Required acceptance evidence

Before `M2` may become `in_progress`, the repository must contain only the minimum non-sensitive references needed to establish all of the following:

1. **Accountability:** approved stable references resolve to the named individuals for every required role, and each individual has acknowledged the relevant accountability and review duties. Names, contact details, or private directory material need not and should not be copied into Git.
2. **Protocol approval:** the product owner has approved the bounded paired-discovery scope, and the discovery-method reviewer has approved the method, sampling rationale, evidence-sufficiency rule, contradiction handling, and review trigger.
3. **Privacy and input approval:** the product and privacy owners have approved the purpose and lawful basis where applicable, notice and consent, minimization and prohibited data, approved systems, access and export controls, retention and deletion, disclosure review, incident handling, and the exact repository path and formats permitted for any minimized synthesis.
4. **Input eligibility:** the approved plan limits work to synthetic inputs or inputs covered by the recorded governance arrangement. Raw or restricted participant, customer, mission, or telemetry data is not copied into Git, fixtures, logs, screenshots, exports, or mockups.
5. **Claim boundary:** the entry reviewers acknowledge that proof validity is not telemetry truth; one observation is not interval, whole-flight, safety, contractual, payment, or regulatory compliance; verification is not the relying party's business decision; and publication is optional corroboration rather than verification authority.
6. **Assurance boundary:** `A0_SYNTHETIC` is the only demonstrator assurance tier. A relying party may identify a higher future requirement, but that neither upgrades evidence nor authorizes hardware or other work needed to attain it.
7. **Output labelling:** every permitted paper or non-cryptographic concept surface, export, screenshot, recording, result, and research record carries the applicable required label.
8. **Delivery disposition:** the delivery lead records that the complete entry set is satisfied, cites the accepted evidence references, and confirms that no excluded activity is thereby authorized.

## Privacy and repository boundary

Governed source evidence belongs only in the approved external research system. Do not commit participant names, contact details, employer or site details where identifying, recruitment records, recordings, transcripts, raw notes, consent records, procurement documents, contract material, exact locations, flight paths, telemetry, customer or mission identifiers, credentials, restricted fields, or re-identifying combinations.

Until a privacy-handling approval explicitly permits a repository evidence path, do not create `docs/discovery/` or commit completed research material. Blank templates may remain planning aids only.

## Transition procedure

When every entry condition has accepted evidence:

1. update this record with the non-sensitive evidence references, reviewer acknowledgements, expiry or review triggers, and delivery-lead disposition;
2. update the `M2` row in `docs/management/validated-claim-contract-register.csv` from `blocked` to `in_progress`;
3. populate the approved `accountable_person_ref` and accepted `evidence_refs`;
4. clear only `milestone_entry_criteria_not_satisfied`, retain `gate_closed=false`, and add a dated `last_status_change_ref`;
5. close issue #49 and leave issue #50 open for the governed discovery evidence and final `M2` disposition; and
6. run `python3 scripts/check_docs.py` and the applicable repository review checks.

Moving `M2` to `in_progress` authorizes only the bounded, approved discovery work. It does not accept `M2`, close product-scope Gate 1, authorize `M3`, or establish implementation, demand, pilot readiness, willingness to pay, safety, compliance, or production readiness.
