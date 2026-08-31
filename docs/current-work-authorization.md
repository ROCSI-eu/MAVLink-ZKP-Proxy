# Current work authorization

| Metadata | Value |
| --- | --- |
| Status | Current documentation-governance rule |
| Audience | Maintainer, contributors, reviewers, and prospective participants |
| Accountable role | Repository maintainer for factual maintenance; milestone accountability remains unassigned until the delivery-plan requirements are satisfied |
| Review trigger | Any proposed expansion of work, data use, participant contact, role combination, independence model, milestone status, or evidence system |
| Authority | Owns only the work permitted while `M1` entry remains unsatisfied; [`docs/delivery-plan.md`](delivery-plan.md) remains the sole authority for milestone prerequisites, sequencing, evidence, review, acceptance, and exit |

## Purpose and precedence

This document removes ambiguity about what may be done while the project has one maintainer and `M1` remains `blocked`. It is a conservative Current boundary for pre-M1 activity, not a milestone, phase, approval, or substitute for the delivery plan.

The [solo planning readiness record](reviews/validated-claim-contract/solo-planning-readiness-record.md) records the factual operating context. The [operational register](management/validated-claim-contract-register.csv) records Current milestone status. If this document conflicts with a milestone prerequisite or exclusion in the delivery plan, the delivery plan controls and the narrower interpretation applies.

## Authorized work

While `M1` entry remains unsatisfied, work is limited to:

- reviewing, reconciling, correcting, and cross-linking repository documentation;
- recording contradictions, status corrections, traceability, and non-sensitive governance findings;
- drafting role definitions, evidence requirements, review checklists, approval templates, and privacy-safe record schemas that remain Proposed until accepted by the required people, including the Proposed [pre-M1 participant readiness pack](pre-m1-participant-readiness.md);
- conducting low-risk recruitment outreach under the lightweight pre-M1 outreach policy below;
- creating demonstrably synthetic, minimized, test-only planning examples that do not exercise or imply a prototype, proof, verifier, telemetry path, or production capability;
- maintaining repository metadata, documentation navigation, issue and pull-request hygiene, and documentation validation; and
- correcting unsupported claims in ways that reduce apparent authorization, maturity, assurance, or readiness.

The pre-M1 participant readiness pack is supporting preparation material only. This authorization permits use of its bounded outreach message, but the pack does not establish a participant, satisfy an M1 entry condition, or amend the delivery plan.

### Lightweight pre-M1 outreach policy

Maintainer approval of this Current policy is the trigger for bounded outreach; prior funding and an existing organic relationship are not required. The maintainer may:

1. contact prospective participants only through public professional contact channels;
2. share only the public repository and a concise, accurate project description, including its documentation-only status and the limits of the proposed role;
3. collect outside Git only the minimum contact detail, prospective role, interest, and conflict information needed to assess possible participation;
4. conduct one initial, non-research conversation limited to role fit, decision authority, availability, conflicts, and willingness to accept the M1 boundaries; and
5. record in Git only the minimized, non-sensitive references allowed by the readiness pack after the person agrees.

Contact must be proportionate, allow an immediate decline, and stop on decline or any stop condition in the readiness pack. Outreach and the suitability conversation are recruitment administration only. They MUST NOT be designed, recorded, analyzed, cited, or represented as discovery, customer validation, independent review, product evidence, or evidence of demand, workflow fit, pilot intent, or willingness to pay.

A paper mockup or non-cryptographic UX illustration created solely as a documentation example must still carry the applicable mandatory label on every surface and associated record. Its creation does not authorize research use and does not count as discovery, proof, verification, or product evidence.

## Prohibited work

This Current authorization does not permit:

- participant contact outside the lightweight policy; interviews, observation sessions, surveys, recordings, transcripts, research consent collection, procurement discussions or claims, or participant-level research records;
- collection or use of real customer, participant, site, mission, vehicle, telemetry, identity, contact, or other restricted data, except for the minimum contact, role, interest, and conflict information held outside Git under the lightweight policy;
- treating Google Drive or any other system as an approved research or restricted-evidence system before its governance and approvals are accepted;
- paper-mockup or non-cryptographic-prototype research, completed discovery records, claim-selection findings, demand findings, pilot intent, or willingness-to-pay evidence;
- executable prototypes, format or vector spikes, parser work, MAVLink or SITL execution, telemetry integration, circuits, proving, verification, policy execution, replay state, persistence, APIs, user interfaces, publication, or external SDK integration;
- hardware work, vehicle command paths, live-network or ledger activity, pilots, deployment, production preparation, or production claims; or
- any activity assigned to `M2` or a later work item.

## Provisional role combination and independence

The sole maintainer may apply product, delivery, architecture, cryptography, security, privacy, safety, telemetry, and discovery perspectives while drafting and reconciling documentation. That role combination is a planning convenience only.

It does not provide an assigned accountable person for milestone purposes, independent review, specialist approval, product-versus-privacy separation, discovery-method approval, relying-party authority, or delivery-gate approval. ChatGPT or another AI system may assist with drafting and analysis but cannot be an accountable person, reviewer, participant, approver, or relying-party decision owner.

No maintainer acknowledgement or AI-assisted review may be converted into evidence that a required independent role, review, or participant exists.

## Transition to M1

This authorization remains Current while `M1` is `blocked`. `M1` may move to `in_progress` only when the minimum start conditions in the delivery plan are satisfied by accepted, non-placeholder evidence:

1. prospective real participants are recorded for every preliminary role required by the delivery plan, including a genuine relying-party representative who owns the external decision and is not the producer, maintainer, project team, or AI proxy; and
2. the M1 safety/privacy boundary is recorded in a form that satisfies the delivery plan and is acknowledged as applicable by the real preliminary participants whose roles are required for M1 entry.

Bounded outreach may be used to identify and assess those prospective participants before M1. It does not itself establish a participant or satisfy either entry condition. Before the valid M1 transition, contact must stop short of research or discovery interviews, workflow-evidence collection, telemetry exchange, procurement claims or discussions, restricted-data handling, and any request for independent review. Nothing learned during recruitment may be carried into M1 or a later milestone as discovery, customer-validation, independent-review, or product evidence.

The transition must be made through a scoped pull request that:

- cites the accepted non-sensitive evidence references;
- updates the operational register from `M1=blocked` to `M1=in_progress` while retaining `gate_closed=false`;
- removes only blockers actually satisfied;
- preserves every M1 implementation and data exclusion;
- marks this pre-M1 authorization Superseded or narrows it to traceability as appropriate; and
- passes `python3 scripts/check_docs.py`.

Beginning M1 would authorize documentation reconciliation only. It would not accept M1, begin M2, authorize participant research, or authorize technical work.

## Decision and ADR disposition

This rule formalizes and narrows the already recorded Current solo-planning boundary. It does not select an architecture, implementation technology, product claim, workflow, assurance level, or commercial model and does not relax any milestone prerequisite. No ADR is required for this documentation-governance clarification.
