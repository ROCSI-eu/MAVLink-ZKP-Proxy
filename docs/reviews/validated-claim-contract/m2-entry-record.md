# M2 paired-discovery entry readiness record

| Record field | Value |
| --- | --- |
| Work item | `M2` — Run paired provider/relying-party discovery |
| Record date | 2026-08-30 |
| Status | **Open** — entry conditions are not satisfied |
| Current disposition | `M1` is `in_progress`; `M2` remains `blocked`; `gate_closed=false` |
| Required accountable role | Discovery lead with product owner; accepted assignees absent |
| Primary tracker | [Issue #49](https://github.com/ROCSI-eu/Telemetry-Attestation-Gateway/issues/49) |
| Downstream tracker | [Issue #50](https://github.com/ROCSI-eu/Telemetry-Attestation-Gateway/issues/50), blocked by issue #49 |
| Authority | [`docs/delivery-plan.md`](../../delivery-plan.md), [`docs/discovery-research-plan.md`](../../discovery-research-plan.md), and the [`M1` authority map](authority-map.md) |
| Actual operating context | [`solo-planning-readiness-record.md`](solo-planning-readiness-record.md) |

## Purpose and non-authorization

This record coordinates the evidence required to move `M2` from `blocked` to `in_progress`. It is not an approval record and does not itself satisfy an entry condition.

The repository is in a solo, documentation-planning state. The prior independent M1 approval claim is Superseded; M1 is proceeding at solo concept level and may finish only as a solo-maintainer provisional baseline. This record does not authorize participant-data collection, interviews, completed research records, a prototype, proof generation or verification, telemetry or SITL integration, hardware, a vehicle command path, live publication, a pilot, pricing, or production activity.

The industrial-site inspection workflow and its buyer, relying-party decision, coverage unit, disclosure need, assurance requirement, volume, purchasing path, pilot intent, and willingness to pay remain hypotheses or **Open** questions. Bounded horizontal speed remains a Proposed synthetic technical primitive, not an approved compliance product.

## Current entry-state assessment

| Entry condition | Required owner or reviewers | Current status | Evidence or blocker |
| --- | --- | --- | --- |
| Solo-maintainer provisional `M1` baseline | Repository maintainer | **Open / blocking M2 until M1 review** | M1 is in progress; no independent approval is required or claimed |
| Risk-triggered accountability recorded | Discovery lead with product owner; reviewers identified by the role-by-risk matrix | **Open / blocking only for triggered work** | The planned participant research triggers privacy and discovery-method review; additional roles are required only if the actual activity triggers their risk row |
| Provider-side and relying-party-side participants | Discovery lead, product owner, paired participants | **Deferred / blocking** | Bounded pre-M1 recruitment outreach is permitted, but M2 paired participation and research recruitment remain Deferred until funding or suitable organic relationships exist |
| Approved bounded paired-discovery protocol and evidence-sufficiency method | Product owner; discovery-method review | **Deferred / blocking** | `docs/discovery-research-plan.md` remains a Proposed protocol; no independent discovery-method approval exists |
| Approved research and input-handling arrangement | Product owner and privacy reviewer; additional review only where the matrix is triggered | **Deferred / blocking** | Google Drive is only Proposed and unconfigured; no approved handling record, system, access model, retention, deletion, or disclosure control exists |
| Synthetic-or-governed inputs | Product owner and privacy owner | **Current planning boundary only** | All present planning inputs are limited to demonstrably synthetic, minimized, test-only data; this does not authorize research execution |
| Hypothesis and non-claim boundary acknowledged | Product owner, discovery lead, paired participants, and risk-triggered reviewers | **Current maintainer acknowledgement only** | The workflow, claim materiality, coverage, need, decision, assurance, procurement, pilot intent, and willingness to pay remain Open; the required external acknowledgements are absent |
| Demonstrator assurance restricted to `A0_SYNTHETIC` | Product owner, relying-party participant, and any reviewer triggered by the proposed assurance claim | **Current maintainer acknowledgement only** | `A0_SYNTHETIC` is the only permitted demonstrator tier; required external review remains absent |
| Mandatory output labels | Product owner and discovery lead | **Current maintainer acknowledgement only** | Every paper output states **“paper mockup — no proof generated”**; every non-cryptographic output states **“non-cryptographic UX prototype — no proof generated or verified”** on every surface and associated record |
| Complete entry disposition | Discovery lead with product owner after all applicable evidence and risk-triggered reviews | **Open / blocking** | The maintainer explicitly acknowledges that no positive M2 entry disposition can currently be issued |

The Current planning safeguards permit M1 but do not compensate for the paired participants, discovery-method review, privacy/input review, or approved evidence system triggered by M2.

## Required acceptance evidence

Before `M2` may become `in_progress`, the repository must contain only the minimum non-sensitive references needed to establish all of the following:

1. **Provisional M1 baseline:** maintainer review records a solo-maintainer provisional baseline with no claim of independent approval.
2. **Accountability:** the activity and intended claims are mapped to the role-by-risk matrix; approved stable references resolve to the accountable discovery and product owners, paired participants, privacy and discovery-method reviewers, and any additional role actually triggered. Each referenced person has acknowledged the applicable duties. Names, contact details, or private directory material need not and should not be copied into Git.
3. **Independent relying-party ownership and paired participation:** a genuine relying-party decision owner is not the producer, maintainer, project team, or an AI proxy; the required provider-side and relying-party-side participants are available for the same bounded decision workflow.
4. **Protocol approval:** the product owner has approved the bounded paired-discovery scope, and a qualified discovery-method reviewer has approved the method, sampling rationale, evidence-sufficiency rule, contradiction handling, and review trigger.
5. **Privacy and input approval:** the product and privacy owners have approved the purpose and lawful basis where applicable, notice and consent, minimization and prohibited data, approved systems, access and export controls, retention and deletion, disclosure review, incident handling, and the exact repository path and formats permitted for any minimized synthesis.
6. **Input eligibility:** the approved plan limits work to synthetic inputs or inputs covered by the recorded governance arrangement. Raw or restricted participant, customer, mission, or telemetry data is not copied into Git, fixtures, logs, screenshots, exports, or mockups.
7. **Claim boundary:** the product owner, discovery lead, paired participants, and reviewers triggered by the actual claim acknowledge that proof validity is not telemetry truth; one observation is not interval, whole-flight, safety, contractual, payment, or regulatory compliance; verification is not the relying party's business decision; and publication is optional corroboration rather than verification authority.
8. **Assurance boundary:** `A0_SYNTHETIC` is the only demonstrator assurance tier. The relying-party participant and any reviewer triggered by a proposed assurance claim acknowledge that a higher future requirement neither upgrades evidence nor authorizes hardware or other work needed to attain it.
9. **Output labelling:** every permitted paper or non-cryptographic concept surface, export, screenshot, recording, result, and research record carries the applicable required label.
10. **Entry disposition:** the discovery lead and product owner record that the complete applicable entry set is satisfied, cite the accepted evidence references, and confirm that no excluded activity is thereby authorized.

## Privacy and repository boundary

Governed source evidence belongs only in an approved external research system. Google Drive is presently Proposed but unconfigured and unapproved. Do not place participant names, contact details, employer or site details where identifying, recruitment records, recordings, transcripts, raw notes, consent records, procurement documents, contract material, exact locations, flight paths, telemetry, customer or mission identifiers, credentials, restricted fields, or re-identifying combinations in Git or an unapproved Drive location.

Until a privacy-handling approval explicitly permits a repository evidence path, do not create `docs/discovery/` or commit completed research material. Blank templates may remain planning aids only.

## Deferred conditions and revisit trigger

M2 paired-participant research recruitment, discovery-method approval, and research/input-handling approval are **Deferred**. The separately authorized bounded pre-M1 outreach may identify prospective preliminary participants but does not authorize M2 recruitment or supply M2 evidence. The deferred M2 activities may be reconsidered when funding or suitable organic relationships make genuine paired participation realistic and when qualified reviewers and a controlled external evidence system can be established.

Deferred does not mean satisfied. Each deferred item remains blocking until accepted evidence changes its status.

## Transition procedure

Only when accepted M1 evidence and every M2 entry condition are complete:

1. update this record with the non-sensitive evidence references, reviewer acknowledgements, expiry or review triggers, and discovery-lead/product-owner disposition;
2. update the `M2` row in `docs/management/validated-claim-contract-register.csv` from `blocked` to `in_progress`;
3. populate the approved `accountable_person_ref` and accepted `evidence_refs`;
4. clear only the satisfied entry blockers, retain `gate_closed=false`, and add a dated `last_status_change_ref`;
5. close issue #49 and leave issue #50 open for the governed discovery evidence and final `M2` disposition; and
6. run `python3 scripts/check_docs.py` and the applicable repository review checks.

Moving `M2` to `in_progress` would authorize only the bounded, approved discovery work. It would not accept `M2`, close product-scope Gate 1, authorize `M3`, or establish implementation, demand, pilot readiness, willingness to pay, safety, compliance, or production readiness.
