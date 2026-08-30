# Discovery research plan

| Metadata | Value |
| --- | --- |
| Status | Proposed protocol; no interviews or findings recorded |
| Audience | Product owner, privacy owner, researchers, and discovery reviewers |
| Accountable role | Product owner |
| Review trigger | Privacy-handling approval, research-method change, or completion of an interview round |
| Authority | Governs discovery collection and the promotion of findings into product decisions |

## Current state and evidence boundary

This document is a research protocol, not discovery evidence. No participant has been interviewed for this repository, no market fact is established here, and no conclusion may be inferred from the questions or hypotheses below.

There is intentionally no `docs/discovery/` evidence area yet. The product owner MUST approve the privacy-handling record described below before anyone creates that directory or commits interview material, notes, transcripts, contact details, recordings, quotations, or synthesized findings. Approval to run interviews is not approval to store their outputs in Git.

Until that approval exists:

- researchers MAY use this guide to plan recruitment and interviews;
- researchers MAY use the blank files in [`templates/discovery/`](templates/discovery/) as optional structural guidance, but MUST keep completed copies in the approved external research system;
- interview data MUST NOT be committed anywhere in this repository;
- `docs/product-scope.md` and `docs/decisions.md` MUST NOT be changed based on recollection, assumptions, recruiting conversations, or unreviewed notes; and
- the current speed workflow, roles, volumes, costs, and market descriptions remain hypotheses rather than findings.

## Privacy-handling approval gate

Before creating an evidence area, the product owner and privacy owner MUST approve a dated handling record outside this repository or in an already approved governance system. The record must identify:

1. the research purpose, lawful basis where applicable, participant population, jurisdictions, and accountable owner;
2. notice and consent language, including whether recording and attributed quotations are separately optional;
3. the minimum data collected, prohibited data, anonymization or pseudonymization method, and re-identification/linkage risks;
4. the approved systems for recruitment data, recordings, transcripts, raw notes, consent records, and repository-ready synthesis;
5. role-based access, sharing and export rules, subprocessors, residency constraints, and incident contact;
6. a retention and deletion schedule for each artifact class, including backups, withdrawals, legal holds, and proof of deletion;
7. the minimum aggregation or redaction threshold for repository material and the reviewer responsible for disclosure control; and
8. the exact repository path and allowed file formats, plus a statement that Git history is difficult to retract and therefore contains only approved, minimized synthesis.

The approval record MUST expose only a non-sensitive approval reference, approver roles, approval date, scope, and expiry/review trigger to the repository. It MUST NOT expose participant identities or otherwise defeat anonymization. If approval is refused, expires, or does not permit Git storage, no discovery evidence area is created; governed evidence stays in the approved system and repository documents may cite only an approved, non-identifying synthesis or reference.

## Sampling and interview structure

Recruit both sides of the same real decision wherever possible:

- **Provider-side buyers:** people who own or materially influence budget or procurement for the provider, plus workflow practitioners who prepare or release evidence. Do not treat an interested engineer as a buyer without budget evidence.
- **Site-owner relying parties:** people who review the evidence, own the policy or contractual decision, or bear the consequence of accepting, rejecting, or escalating it. Do not substitute a provider's description of the relying party for a relying-party interview.

Track role coverage and organization coverage without publishing identities. Separate interviews are preferred so commercial relationships and hierarchy do not suppress disagreement. Ask first about the most recent concrete decision, then test alternatives; do not introduce zero-knowledge proofs, speed, local verification, or a preferred pilot structure before documenting the unaided workflow.

Recruitment targets are planning controls used to manage coverage and surface gaps; they are not validation evidence, do not establish that a problem is confirmed, and MUST NOT be converted into prevalence claims. Evidence sufficiency depends on the documented sampling rationale, paired decision coverage, provenance, buyer or procurement visibility, contradictions, missing coverage, and limitations rather than attainment of a target count.

The interviewer MUST distinguish direct experience from opinion, future preference, and hearsay. Quantitative answers require a period, unit, range or count, and the participant's basis for knowing. One statement is a reported observation, not a market prevalence claim.

## Core interview guide

Use neutral follow-ups and preserve meaningful disagreement. The prompts below are required topics, not a script that implies an expected answer.

### Recent decision and materiality

1. “Walk me through the most recent occasion when you requested, produced, reviewed, or declined operational evidence for an inspection flight.” Record the trigger, decision owner, parties, sequence, systems, and outcome.
2. “What evidence was actually requested?” Ask for the request or template if the participant may lawfully share a redacted copy. Only after the unaided answer, ask whether speed appeared and whether it affected the decision.
3. “Which interval did the decision cover: one observation, a segment, selected samples, or the whole flight?” Record the participant's terminology, required sampling/coverage rule, and whether snapshot evidence could satisfy it.
4. “What happens if the evidence is accepted incorrectly, rejected incorrectly, or cannot be verified?” Record operational, contractual, safety, financial, and review consequences without assigning severity on the participant's behalf.

### Current disclosure, retention, and cost

5. “What is disclosed today, to whom, through which system, and why is each field needed?” Record raw logs, reports, signatures, provenance, identifiers, locations, timestamps, imagery, and other fields only when mentioned or confirmed.
6. “Who stores each copy, for how long, under what deletion or legal-hold rule, and who can review or export it?” Distinguish policy from observed practice.
7. “For the most recent case, how much preparation, transfer, review, clarification, escalation, and rework occurred?” Capture elapsed time, staff time, role, external spend, and frequency separately; do not manufacture a total cost from missing inputs.

### Buying and assurance

8. “Who owns the problem, budget, approval, security/privacy review, procurement, contracting, integration, and renewal?” Ask what purchasing route was used for the closest comparable purchase and what evidence shows budget authority.
9. “What is the minimum provenance and assurance needed for this decision?” Probe source authentication, authorization, time, coverage, transformation, signing keys, revocation, custody, auditability, and independent corroboration only after the unaided answer.
10. Present a clearly labelled concept in randomized order where practical: (a) the current artifact, (b) a signed minimized report, and (c) a minimized report with an exportable proof. Ask which is sufficient and why; do not claim that a signature or proof establishes sensor truth or whole-flight behavior.
11. For the exportable-proof concept, compare vendor verification with independent local verification. Ask whether local verification changes acceptance, review burden, procurement, security review, outage handling, or willingness to pilot. Record “no difference” and rejection as valid outcomes.

### Volume, integration, and pilot

12. “How many such decisions occurred in a defined recent period, and what drives peaks?” Record decisions, flights, evidence packages, and exceptions as different measures.
13. “What consequence or value attaches to one decision and to aggregate volume?” Keep participant estimates, observed records, and researcher calculations distinguishable.
14. “What is the least integration you would accept?” Test offline file exchange, command-line or library verification, API/service integration, identity and policy integration, audit export, support, deployment location, and allowable dependencies without assuming any is required.
15. “What would a credible pilot require?” Record paired participants, governed or synthetic data, duration, decision count, success and stop criteria, resources, security/privacy/legal review, support, price or budget path, and who can authorize it.

Close by asking what was missing or wrongly assumed and whether the participant permits follow-up. Do not request sensitive flight data merely to make an interview appear evidential.

## Recording and synthesis rules after approval

If the privacy gate authorizes a discovery evidence area, its first commit MUST include the non-sensitive approval reference and a README defining the approved schema and controls. Each governed interview synthesis should use an opaque participant code and record:

- interview date or approved coarse period, side (`provider_buyer`, `provider_practitioner`, or `relying_party`), role category, organization segment, and evidence-strength classification;
- consent scope and redaction review status without including the consent record itself;
- structured observations for every tested topic, including “not asked,” “unknown,” “not requested,” and contradictory answers;
- provenance for each observation, such as participant report, redacted artifact review, measured workflow, or researcher inference;
- quantities with unit, time window, sample basis, and uncertainty;
- quotations only when separately approved and safe from contextual re-identification; and
- researcher interpretation in a visibly separate section from reported facts.

Do not commit names, contact details, employer names where identifying, exact sites, flight paths, customer or mission identifiers, raw telemetry, recordings, transcripts, consent forms, procurement documents, credentials, or sensitive contract terms. Hashing an identity does not anonymize it. Small-cell combinations and distinctive quotations require suppression or coarsening.

Round-level findings MUST report the denominator and role mix, supporting and contradicting observations, missing coverage, source type, and limitations. They MUST NOT convert recruitment criteria into findings, extrapolate prevalence from a convenience sample, combine unlike units, or describe stated intent as purchasing behavior.

Any change to this protocol, its sampling rationale, or its evidence-sufficiency rule requires product-owner review and discovery-method review before use. Any change affecting what evidence is collected, transformed, retained, disclosed, or stored also requires privacy-owner review before the change is applied to stored evidence.

## Evidence-to-decision rule

Only privacy-reviewed, recorded evidence may support a change to `docs/product-scope.md` or `docs/decisions.md`. Every such change MUST cite the approved evidence identifiers and state:

- which provider-side and relying-party observations support it;
- contradictory or inconclusive evidence;
- whether the conclusion concerns a snapshot, segment, samples, or whole flight;
- the evidence strength and sample limitations; and
- the product owner who accepted the interpretation.

Absence of an interview response is not evidence of absence. Research findings may close, narrow, or reopen a hypothesis; they do not silently expand implementation scope.

### Speed-materiality stop rule

Speed is material only if recorded relying-party evidence shows that speed evidence is actually requested and changes or is necessary to the selected decision, and provider-side evidence confirms a material disclosure, retention, review, or commercial burden in supplying it. Technical interest, feasibility, a generic site limit, or an interviewer-prompted preference is insufficient.

If the recorded evidence does not establish that materiality, bounded speed remains a technical primitive for the deterministic demonstrator. The product owner MUST keep implementation from broadening, mark the commercial claim/vertical selection for reopening in the decision register using the evidence references, and run a new bounded discovery round before selecting another claim or vertical. A failed speed hypothesis does not authorize additional telemetry, hardware, claims, integrations, or markets.

## Completion checklist

A discovery round is ready for product-owner review only when:

- privacy approval was valid for every recorded artifact and repository disclosure;
- both provider-side buyers and site-owner relying parties were interviewed, with role and organization coverage stated;
- every required topic above has an answer or an explicit missing-data marker;
- current artifacts and costs are distinguished from opinions and proposed concepts;
- snapshot, segment, sampled, and whole-flight decisions are not conflated;
- findings include counterevidence and limitations and contain no invented market facts; and
- proposed scope or decision edits cite only the approved evidence set.
