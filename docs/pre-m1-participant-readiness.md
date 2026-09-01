# Risk-proportionate participant and reviewer readiness

| Metadata | Value |
| --- | --- |
| Status | Current readiness and promotion criteria |
| Audience | Maintainer, future participants, reviewers, and accountable owners |
| Accountable role | Repository maintainer for solo concept records; named owners at pilot or production level |
| Review trigger | Change in activity, data, risk, claim, environment, or maturity level |
| Authority | Supporting matrix for the accountability levels in the [delivery plan](delivery-plan.md#status-dimensions) |

## Readiness principle

There is no fixed ten-person preliminary prerequisite. Readiness is assessed by activity and risk. The maintainer can begin and finish M1 documentation reconciliation alone. External roles unavailable today are recorded as future promotion blockers only where a matrix trigger applies.

## Role-by-risk matrix

| Proposed activity or claim | Accountability level | Required participation or review before starting or making the claim | What absence blocks |
| --- | --- | --- | --- |
| Documentation reconciliation, synthetic examples, provisional contract or architecture decisions | Solo concept | Maintainer review; synthetic-only boundary | Nothing beyond solo work; output remains provisional |
| Participant research or any personal, contact, customer, or restricted-data handling | External validation | Privacy reviewer; discovery/method reviewer when research is conducted; real participants under approved governance | Data collection/handling and research, not documentation drafting |
| Claiming a provider-to-relying-party workflow has been validated | External validation | Real provider participant and real relying-party representative who owns or formally represents the decision; discovery reviewer for research validity | Workflow-validation, demand, comprehension, assurance-sufficiency, or pilot-intent claims |
| Promoting a proof design, cryptographic statement, setup, key lifecycle, or proof-system choice beyond a synthetic candidate | External validation | Cryptography reviewer; security reviewer where threat, key, verification, or failure semantics are implicated | Promotion or implementation claim for that proof design |
| Security, identity, replay, revocation, trust-boundary, or restricted-artifact design promoted beyond a provisional draft | External validation | Security reviewer; privacy reviewer when disclosure, linkage, identity, or personal data is implicated | Security/privacy approval claims and affected technical promotion |
| Telemetry compatibility or provenance claim based on a real source or integration | External validation | Telemetry reviewer; provider participant for source facts; cryptography/security only if their risks are implicated | Real-source compatibility or provenance claim |
| Hardware connection, vehicle testing, command-adjacent work, or operational use | External validation | Safety reviewer and accountable operational/telemetry owner; security reviewer where control or connectivity creates a security risk | Hardware or operational activity and safety claim |
| Relying-party UX, accessibility, or unaided interpretation claim | External validation | Real relying-party representative; discovery reviewer; accessibility reviewer when accessibility is in scope | Workflow comprehension or accessibility-validation claim |
| Pilot or production | Pilot or production | Named accountable owners for every implicated discipline; independent security, privacy, safety, cryptography, operational, and other reviews as risk requires; provider/relying-party ownership; documented separation of build, review, approval, operation, and residual-risk acceptance | Pilot, deployment, production, readiness, or compliance promotion |

A person may cover multiple roles during external validation only when conflicts are disclosed and no required independence is defeated. At pilot or production level, combinations must satisfy the recorded separation-of-duty design; the builder cannot self-supply a required independent review. AI never fills a required role.

## Evidence record

For each triggered row, record: activity and intended claim; accountability level; risk trigger; real participant or reviewer reference; authority and independence scope; conflicts and combinations; evidence reviewed; disposition; limitations; and the exact promotion blocked while incomplete. Keep contact details, participant-level records, raw notes, recordings, consent records, credentials, telemetry, and restricted evidence outside Git in an approved system.

## M1 readiness

The existing documentation-only safety/privacy boundary is sufficient for M1 entry. M1 requires no preliminary participant roster. Maintainer acceptance may close M1 only as **“solo-maintainer provisional baseline”** and must list external-validation blockers for future work rather than treating them as M1 blockers.

## Recruitment boundary

Public-channel outreach may identify potential future participants after contact-data privacy controls are approved. The initial exchange is limited to role fit, authority, availability, conflicts, boundaries, and willingness to participate. It is recruitment administration—not research, independent review, validation, demand evidence, pilot intent, or willingness-to-pay evidence.
