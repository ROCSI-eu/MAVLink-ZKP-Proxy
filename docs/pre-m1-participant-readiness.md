# Pre-M1 participant readiness pack

| Metadata | Value |
| --- | --- |
| Status | Proposed / unapproved preparation material |
| Audience | Maintainer, future recruitment coordinators, prospective participants, and reviewers |
| Accountable role | Repository maintainer for factual maintenance; milestone roles remain unassigned |
| Review trigger | Role requirement, independence rule, privacy boundary, evidence format, recruitment authorization, or M1 entry-condition change |
| Authority | Supporting preparation material only; [current work authorization](current-work-authorization.md) controls permitted pre-M1 activity and the [delivery plan](delivery-plan.md) controls M1 prerequisites, evidence, review, acceptance, and exit |
| Related tracker | [Issue #57](https://github.com/ROCSI-eu/Telemetry-Attestation-Gateway/issues/57) |

## Status and non-authorization

This pack prepares the project to assess possible future participants. It does not establish that any participant, reviewer, accountable person, or relying-party decision owner exists. Every template and criterion below is **Proposed / unapproved** until the applicable governance and real participants accept it.

The repository currently has no eligible preliminary participant set. `M1` remains `blocked`, `gate_closed=false`, and all later work remains blocked.

The Current work authorization now permits only lightweight pre-M1 outreach through public professional contact channels, use of the message below, minimum contact/role/interest/conflict handling outside Git, and an initial non-research suitability conversation. This pack does not authorize research or discovery interviews, workflow-evidence collection, telemetry exchange, procurement claims or discussions, restricted-data handling, prototypes, telemetry or SITL work, proof work, hardware, publication, pilots, deployment, or production activity. Recruitment contact and suitability discussion MUST NOT be treated as discovery, customer validation, independent review, product evidence, or evidence of demand, workflow fit, pilot intent, or willingness to pay.

## Preliminary role profiles

M1 entry requires prospective real participants for all ten preliminary roles. A role reference must resolve to a real person who understands the documentation-only scope and agrees to participate in reconciliation. A role title, placeholder, organization name, AI system, or maintainer assertion alone is insufficient.

| Role | Preliminary M1 contribution | Minimum fit | Specific exclusion or independence condition |
| --- | --- | --- | --- |
| Delivery | Coordinate the reconciliation sequence, evidence references, blockers, and status updates | Can maintain evidence-gated work and distinguish entry, progress, and acceptance | Must not convert schedule pressure or repository activity into gate evidence |
| Product | Test claim, workflow, actor, decision, and non-claim language for product consistency | Can identify unsupported demand, workflow, pilot, and commercial assertions | Must preserve every Open hypothesis and avoid treating technical plausibility as buyer evidence |
| Architecture | Review authority, component, trust-boundary, lifecycle, and offline-verification consistency | Can reason about modular boundaries, failure behavior, versioning, and dependency isolation | Must not present Proposed components or technologies as implemented or selected |
| Cryptography | Review statement, canonical-input, commitment, proof, key, and typed-result semantics | Can assess proof-contract language, deterministic encoding, domain separation, and failure-closed behavior | Must preserve proof validity versus telemetry truth and must not claim cryptographic implementation evidence |
| Security | Review authentication, revocation, replay, key, policy, failure, and restricted-data boundaries | Can assess threat assumptions and security-material lifecycle requirements | Must not elevate MAVLink signing or proof validity into sensor truth, hardware integrity, or compliance |
| Privacy | Review minimization, disclosure, linkage, retention, access, evidence handling, and publication boundaries | Can identify personal-data and correlation risks and distinguish pseudonymity from anonymity | Must not approve participant or restricted-data handling merely because the repository uses synthetic examples |
| Safety | Review observational-only scope, command exclusions, hardware gates, and overclaim risks | Can assess whether language implies control, automatic action, flight safety, or unsupported compliance | Must preserve the absolute prohibition on MAVLink command generation, approval, forwarding, or relay |
| Telemetry | Review MAVLink adapter language, units, field provenance, trust state, observation semantics, and adapter boundaries | Can assess MAVLink telemetry semantics without assuming sensor or mission truth | Must keep MAVLink as a Proposed first adapter rather than the product boundary |
| Discovery | Review research questions, participant-role coverage, method limits, contradictory evidence, and evidence-to-decision rules | Can distinguish preparation from research execution and hypotheses from findings | Preliminary participation is not independent method approval and does not authorize research |
| Relying-party decision owner | Review whether proposed evidence language maps to a genuine external acceptance decision | Actually owns, or formally represents the owner of, the external decision being researched | Must be independent of the producer, maintainer, project team, and any AI proxy; a consultant without delegated decision authority is insufficient |

One person may be considered for more than one non-relying-party preliminary role only when each assignment is explicit and no required independence or separation is implied. Role combination does not create independent review. The relying-party decision-owner role cannot be combined with the producer, maintainer, or project-team role for gate purposes.

## Common eligibility criteria

A prospective preliminary participant must:

- be a real person and use a stable reference that can be checked without publishing contact details;
- understand that the repository is documentation-only and that M1 authorizes reconciliation only;
- agree to the role-specific contribution and the M1 safety/privacy boundary;
- disclose material conflicts, role combinations, organizational interests, and limits of authority through the approved governance process;
- agree that participation is not proof of product demand, technical feasibility, pilot intent, compliance, safety, or production readiness;
- agree that no participant, customer, telemetry, mission, site, procurement, or restricted data will be placed in Git; and
- understand that later accountability, review, research, and M2 requirements are separate gates.

Disqualifying conditions include an invented or non-resolving identity; refusal to acknowledge the documentation-only boundary; reliance on AI as the accountable participant; inability to state actual decision authority; undisclosed material conflict; expectation of immediate implementation, hardware, flight control, participant research, or production claims; or a request to place restricted information in Git.

## Minimum non-sensitive repository reference

The repository record for a prospective participant should contain only the approved minimum:

| Field | Required content |
| --- | --- |
| `role_id` | One of `delivery`, `product`, `architecture`, `cryptography`, `security`, `privacy`, `safety`, `telemetry`, `discovery`, or `relying-party` |
| `stable_person_ref` | An approved non-contact reference resolving to the real person, such as a consenting public GitHub account reference or an opaque record in an approved governance system |
| `participation_ack_ref` | Opaque reference to the person's acknowledgement of the preliminary role |
| `m1_boundary_ack_ref` | Opaque reference to the person's acknowledgement of the M1 safety/privacy boundary |
| `conflict_disposition_ref` | Opaque reference to the recorded conflict and independence disposition |
| `authority_scope` | For the relying-party role only, a minimized statement that the person owns or formally represents the external decision |
| `record_status` | `Proposed`, `Open`, `Current`, `Deferred`, or `Superseded`, used according to repository definitions |

Do not place legal names, email addresses, phone numbers, CVs, signatures, credentials, private profile links, employer-sensitive details, participant notes, or identity documents in Git. Do not recreate the former placeholder pattern with identifiers that do not resolve to an actual person and acknowledgement.

A public GitHub account reference is optional, not mandatory. It may be used only with the person's agreement and does not by itself prove expertise, authority, independence, or acknowledgement. An opaque external reference may be used only after the external governance system and access model are approved for that purpose.

## Proposed acknowledgement templates

These templates are unapproved drafting material. They must be adapted only after bounded recruitment contact is separately authorized.

### Preliminary participation acknowledgement

> I acknowledge that I am being considered as the prospective preliminary `<role_id>` participant for M1 documentation reconciliation. I am a real person, understand the role profile and stated limits, and agree to participate in reconciliation if the project validly opens M1. This acknowledgement does not constitute final accountability, independent approval, research participation, product validation, technical validation, pilot intent, or authorization for implementation or restricted-data handling. I have disclosed material conflicts and role combinations through the approved governance process.

### M1 safety/privacy-boundary acknowledgement

> I acknowledge that M1 is limited to documentation reconciliation. It uses no participant/customer telemetry or research data and authorizes no prototype, proof, verifier, telemetry or hardware integration or testing, vehicle command path, live ledger or network publication, production authorization, or multi-tenant service or identity boundary. I will not treat M1 participation or reconciliation output as proof, verification, discovery, safety, compliance, demand, pilot, or production evidence.

### Relying-party authority confirmation

> I confirm that I own, or formally represent the owner of, the external evidence-acceptance decision described only as an Open hypothesis in the repository. I am not acting as the producer, repository maintainer, project team, or an AI proxy. My preliminary participation does not validate the workflow, claim, assurance requirement, purchasing path, pilot intent, or willingness to pay.

## Proposed non-contact outreach-message template

**Approved only for the bounded contact permitted by the Current work authorization.** Adaptation may identify the relevant role and public repository link, but must not expand the description, request research information, or imply a product, customer, procurement, or review claim.

> We are preparing a documentation-only reconciliation milestone for an open-source concept called Telemetry Attestation Gateway. The public repository is `<public-repository-link>`. The project currently has no implementation, validated workflow, customer, pilot, or production claim. We are seeking a prospective participant for the narrowly defined `<role_id>` documentation role before M1 could begin. An initial conversation would cover only role fit, authority, availability, conflicts, and willingness to accept the M1 boundaries. It would not be a research or discovery interview and would not involve workflow evidence, telemetry, prototypes, hardware, proofs, procurement, confidential data, or independent review. We would keep only minimum contact, role, interest, and conflict information outside Git, publish no contact details or private evidence in Git, and provide a clear option to decline without further contact.

The message may be adapted to the specific role without implying funding, employment, a customer relationship, approved research, selected workflow, product demand, pilot readiness, independent review, procurement intent, or regulatory use.

## Recruitment trigger and stop conditions

Bounded recruitment outreach is triggered by maintainer approval of the lightweight policy in the Current work authorization. It does not depend on prior funding or an existing organic relationship. The maintainer may contact a candidate for a named preliminary role through a public professional channel, use the approved message, retain only minimum contact, role, interest, and conflict information outside Git, and hold the initial non-research suitability conversation described there.

Before contact, the maintainer must identify the target role, use a public professional channel, confirm that the storage route is outside Git and limited to the minimum fields, and preserve the relying-party independence rule and all role disqualifiers. The candidate must receive the repository, concise description, boundaries, and option to decline. Any acknowledgement or later non-public information remains subject to an approved privacy notice, handling route, access, retention, deletion, withdrawal, and disclosure-review controls.

Stop contact and keep M1 blocked if the candidate declines, cannot establish role or decision authority, requests restricted information in Git, expects implementation or research outside the authorization, cannot accept the safety/privacy boundary, has an unresolved material conflict, or would cause the project team to proxy the relying-party decision. Also stop before any research or discovery interview, workflow-evidence collection, telemetry exchange, procurement claim or discussion, restricted-data handling, recording or transcript, or independent-review request. Do not preserve or reuse recruitment statements as discovery, customer validation, independent review, or product evidence.

## Future M1 entry checklist

A future M1-entry PR may be opened only after accepted evidence shows all of the following:

- real prospective participants are recorded for every required preliminary role;
- every stable reference resolves to a real person and the applicable acknowledgements;
- the relying-party participant genuinely owns or represents the external decision and is independent of the producer and project team;
- all conflicts and role combinations have explicit dispositions;
- the M1 safety/privacy boundary is recorded in a form satisfying the delivery plan and acknowledged as applicable by the required real participants;
- the repository contains only minimized non-sensitive references, while governed source records remain outside Git;
- no participant recruitment record is misrepresented as M2 discovery or product evidence;
- the operational register changes only `M1` from `blocked` to `in_progress`, retains `gate_closed=false`, clears only satisfied entry blockers, and retains the unresolved reviewer-approval blocker until M1 acceptance evidence exists;
- the Current pre-M1 authorization and any bounded recruitment authorization are marked Superseded or narrowed for traceability as appropriate; and
- `python3 scripts/check_docs.py` passes.

Beginning M1 would authorize documentation reconciliation only. It would not accept M1, begin M2, close issue #49, begin issue #50, authorize research, or authorize technical work.

## Completion of the preparation tracker

Issue #57 may close when this pack and its routing references are accepted and internally consistent. That closure means only that preparation material exists. It does not establish participants, satisfy M1 entry, change the register status, or close any milestone gate.
