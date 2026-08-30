# M2 paired-discovery entry readiness record

| Record field | Value |
| --- | --- |
| Work item | `M2` — Run paired provider/relying-party discovery |
| Record date | 2026-08-30 |
| Status | **Open** — entry conditions are not satisfied |
| Current disposition | `M1` and `M2` remain `blocked`; `gate_closed=false` |
| Required accountable role | Discovery lead with product owner; accepted assignees absent |
| Primary tracker | [Issue #49](https://github.com/ROCSI-eu/Telemetry-Attestation-Gateway/issues/49) |
| Downstream tracker | [Issue #50](https://github.com/ROCSI-eu/Telemetry-Attestation-Gateway/issues/50), blocked by issue #49 |
| Authority | [`docs/delivery-plan.md`](../../delivery-plan.md), [`docs/discovery-research-plan.md`](../../discovery-research-plan.md), and the [`M1` authority map](authority-map.md) |
| Actual operating context | [`solo-planning-readiness-record.md`](solo-planning-readiness-record.md) |

## Purpose and non-authorization

This record coordinates the evidence required to move `M2` from `blocked` to `in_progress`. It is not an approval record and does not itself satisfy an entry condition.

The repository is in a solo, documentation-planning state. The prior M1 participant and approval claims are Superseded, so M1 is not accepted. This record does not authorize participant-data collection, interviews, completed research records, a prototype, proof generation or verification, telemetry or SITL integration, hardware, a vehicle command path, live publication, a pilot, pricing, or production activity.

The industrial-site inspection workflow and its buyer, relying-party decision, coverage unit, disclosure need, assurance requirement, volume, purchasing path, pilot intent, and willingness to pay remain hypotheses or **Open** questions. Bounded horizontal speed remains a Proposed synthetic technical primitive, not an approved compliance product.

## Current entry-state assessment

| Entry condition | Required owner or reviewers | Current status | Evidence or blocker |
| --- | --- | --- | --- |
| Accepted documentation-only `M1` baseline | Delivery lead and required `M1` reviewers | **Open / blocking** | Prior M1 participation and approval claims are Superseded; the required real participants and reviews are absent |
| Named individuals for product, delivery, architecture, cryptography, security, privacy, safety, telemetry, discovery, and relying-party decision ownership | Delivery lead; each named role holder acknowledges accountability | **Open / blocking** | One maintainer holds provisional planning responsibilities only; no accepted role assignments or independent relying-party decision owner exist |
| Provider-side and relying-party-side participants | Discovery lead, product owner, paired participants | **Deferred / blocking** | External recruitment is Deferred until funding or suitable organic relationships exist |
| Approved bounded paired-discovery protocol and evidence-sufficiency method | Product owner; discovery-method and delivery review | **Deferred / blocking** | `docs/discovery-research-plan.md` remains a Proposed protocol; no independent discovery-method approval exists |
| Approved research and input-handling arrangement | Product owner and privacy owner; security and delivery review where applicable | **Deferred / blocking** | Google Drive is only Proposed and unconfigured; no approved handling record, system, access model, retention, deletion, or disclosure control exists |
| Synthetic-or-governed inputs | Product owner and privacy owner | **Current planning boundary only** | All present planning inputs are limited to demonstrably synthetic, minimized, test-only data; this does not authorize research execution |
| Hypothesis and non-claim boundary acknowledged | Product, discovery, relying-party, privacy, safety, security, and delivery reviewers | **Current maintainer acknowledgement only** | The workflow, claim materiality, coverage, need, decision, assurance, procurement, pilot intent, and willingness to pay remain Open; required independent acknowledgements are absent |
| Demonstrator assurance restricted to `A0_SYNTHETIC` | Security lead with product/privacy and relying-party review | **Current maintainer acknowledgement only** | `A0_SYNTHETIC` is the only permitted demonstrator tier; required role reviews remain absent |
| Mandatory output labels | Product, discovery, privacy, security, safety, and delivery reviewers | **Current maintainer acknowledgement only** | Every paper output states **“paper mockup — no proof generated”**; every non-cryptographic output states **“non-cryptographic UX prototype — no proof generated or verified”** on every surface and associated record |
| Complete entry disposition | Delivery lead after all required evidence and reviews | **Open / blocking** | The maintainer explicitly acknowledges that no positive M2 entry disposition can currently be issued |

The Current planning safeguards are necessary but do not compensate for missing M1 acceptance, real accountable participants, independence, paired discovery participants, method approval, privacy/input approval, or an approved evidence system.

## Required acceptance evidence

Before `M2` may become `in_progress`, the repository must contain only the minimum non-sensitive references needed to establish all of the following:

1. **Accepted M1:** real preliminary participation, approved M1 boundary, required discipline reviews, and a valid delivery-lead acceptance disposition.
2. **Accountability:** approved stable references resolve to the named individuals for every required role, and each individual has acknowledged the relevant accountability and review duties. Names, contact details, or private directory material need not and should not be copied into Git.
3. **Independent relying-party ownership and paired participation:** a genuine relying-party decision owner is not the producer, maintainer, project team, or an AI proxy; the required provider-side and relying-party-side participants are available for the same bounded decision workflow.
4. **Protocol approval:** the product owner has approved the bounded paired-discovery scope, and a qualified discovery-method reviewer has approved the method, sampling rationale, evidence-sufficiency rule, contradiction handling, and review trigger.
5. **Privacy and input approval:** the product and privacy owners have approved the purpose and lawful basis where applicable, notice and consent, minimization and prohibited data, approved systems, access and export controls, retention and deletion, disclosure review, incident handling, and the exact repository path and formats permitted for any minimized synthesis.
6. **Input eligibility:** the approved plan limits work to synthetic inputs or inputs covered by the recorded governance arrangement. Raw or restricted participant, customer, mission, or telemetry data is not copied into Git, fixtures, logs, screenshots, exports, or mockups.
7. **Claim boundary:** the entry reviewers acknowledge that proof validity is not telemetry truth; one observation is not interval, whole-flight, safety, contractual, payment, or regulatory compliance; verification is not the relying party's business decision; and publication is optional corroboration rather than verification authority.
8. **Assurance boundary:** `A0_SYNTHETIC` is the only demonstrator assurance tier. A relying party may identify a higher future requirement, but that neither upgrades evidence nor authorizes hardware or other work needed to attain it.
9. **Output labelling:** every permitted paper or non-cryptographic concept surface, export, screenshot, recording, result, and research record carries the applicable required label.
10. **Delivery disposition:** the delivery lead records that the complete entry set is satisfied, cites the accepted evidence references, and confirms that no excluded activity is thereby authorized.

## Privacy and repository boundary

Governed source evidence belongs only in an approved external research system. Google Drive is presently Proposed but unconfigured and unapproved. Do not place participant names, contact details, employer or site details where identifying, recruitment records, recordings, transcripts, raw notes, consent records, procurement documents, contract material, exact locations, flight paths, telemetry, customer or mission identifiers, credentials, restricted fields, or re-identifying combinations in Git or an unapproved Drive location.

Until a privacy-handling approval explicitly permits a repository evidence path, do not create `docs/discovery/` or commit completed research material. Blank templates may remain planning aids only.

## Deferred conditions and revisit trigger

External recruitment, discovery-method approval, and research/input-handling approval are **Deferred**. They may be reconsidered when funding or suitable organic relationships make genuine paired participation realistic and when qualified reviewers and a controlled external evidence system can be established.

Deferred does not mean satisfied. Each deferred item remains blocking until accepted evidence changes its status.

## Transition procedure

Only when accepted M1 evidence and every M2 entry condition are complete:

1. update this record with the non-sensitive evidence references, reviewer acknowledgements, expiry or review triggers, and delivery-lead disposition;
2. update the `M2` row in `docs/management/validated-claim-contract-register.csv` from `blocked` to `in_progress`;
3. populate the approved `accountable_person_ref` and accepted `evidence_refs`;
4. clear only the satisfied entry blockers, retain `gate_closed=false`, and add a dated `last_status_change_ref`;
5. close issue #49 and leave issue #50 open for the governed discovery evidence and final `M2` disposition; and
6. run `python3 scripts/check_docs.py` and the applicable repository review checks.

Moving `M2` to `in_progress` would authorize only the bounded, approved discovery work. It would not accept `M2`, close product-scope Gate 1, authorize `M3`, or establish implementation, demand, pilot readiness, willingness to pay, safety, compliance, or production readiness.
