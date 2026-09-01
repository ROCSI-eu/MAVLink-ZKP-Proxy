# Current work authorization

| Metadata | Value |
| --- | --- |
| Status | Current risk-proportionate work rule |
| Audience | Maintainer, contributors, reviewers, and prospective participants |
| Accountable role | Repository maintainer at solo concept level |
| Review trigger | Data, participants, proof promotion, hardware/operational use, workflow-validation claim, pilot, or production promotion |
| Authority | [`docs/delivery-plan.md`](delivery-plan.md) controls milestone sequencing and gates |

## Three accountability levels

1. **Solo concept level.** The maintainer may reconcile documentation, run demonstrably synthetic experiments, and make explicitly provisional decisions. Outputs must not claim independence, external validation, specialist approval, or readiness.
2. **External validation level.** Real provider and relying-party participants are required, plus only the reviewers triggered by the research or technical risk in the [role-by-risk matrix](pre-m1-participant-readiness.md#role-by-risk-matrix).
3. **Pilot or production level.** Named accountable discipline owners, independent reviews, and recorded separation of duties are mandatory. Conflicts, approval authority, operational ownership, and residual-risk acceptance must be explicit.

A missing external role is a blocker to promotion into the work or claim that triggers that role. It is not a blocker to solo documentation reconciliation, synthetic planning, or the isolated [solo experimental sandbox](delivery-plan.md#solo-experimental-sandbox-track).

## Authorized solo concept work

The maintainer may:

- review, reconcile, correct, cross-link, and provisionally dispose of repository documentation;
- maintain contradiction, authority, evidence, decision, and status records;
- create synthetic, minimized, test-only examples and experiments that do not use or resemble restricted source data;
- create disposable schema/encoding spikes, fixture-driven parsers, local mock adapters, non-cryptographic prototypes, proof feasibility benchmarks, toy circuits/local verification, no-hardware/no-command-path SITL experiments, and local UI/CLI demonstrations under the delivery plan's solo experimental sandbox rules;
- draft role definitions, research protocols, technical designs, fixtures, and review templates as Proposed material; and
- complete M1 through maintainer review and record its result only as **“solo-maintainer provisional baseline.”**

AI may assist drafting but cannot be a participant, independent reviewer, accountable owner, approver, or relying-party decision owner.

## Experimental sandbox authorization

Sandbox creation and iteration are authorized now and do not require external participants or independent reviewers. Every artifact and output MUST show **`EXPERIMENTAL`**, **`SYNTHETIC_ONLY`**, and **`NOT VALIDATION OR PRODUCTION AUTHORIZATION`**, use only demonstrably synthetic inputs with recorded provenance, and remain isolated from real telemetry, live ledgers/networks, hardware, command paths, credentials/non-test keys, participant data, and production infrastructure. Local loopback mocks and disposable test keys are permitted; external network access is denied by default.

Sandbox outputs cannot satisfy M1–M11, discovery, independent-review, security, interoperability, MVP, pilot, or production evidence. They cannot support external claims. Promotion into a supported prototype, external-discovery evidence, an MVP component, or a pilot/production component requires the distinct destination gate in the [delivery plan](delivery-plan.md#solo-experimental-sandbox-track); promotion is a reviewed copy or reimplementation, never removal of labels in place.

## Risk-triggered limits

The solo concept level does not permit participant research, personal or restricted data handling, external workflow-validation claims, promotion of an experimental proof design, hardware or operational use, pilots, deployment, or production activity. Each becomes eligible only when its row in the role-by-risk matrix and the applicable promotion destination are satisfied. These limits block promotion and claims, not creation of a compliant sandbox experiment.

Paper and non-cryptographic examples must be labelled respectively **“paper mockup — no proof generated”** and **“non-cryptographic UX prototype — no proof generated or verified”** on every surface and associated record. `A0_SYNTHETIC` remains the only demonstrator assurance tier.

Recruitment administration may use public professional channels after an appropriate privacy arrangement exists for contact data. It must remain separate from research and may not be cited as discovery, validation, demand, pilot intent, or willingness-to-pay evidence.

## M1 and promotion

The recorded [M1 boundary](reviews/validated-claim-contract/m1-boundary-record.md) is sufficient to start M1. The maintainer may set M1 to `in_progress`, reconcile its documents, perform the M1 review, and finish it as a **solo-maintainer provisional baseline** without external participants or discipline reviewers. The review must identify unresolved contradictions and future promotion blockers and must state that it is not an independently approved baseline.

M2 or another external-validation activity may begin only when real provider and relying-party participants are available and every reviewer triggered by that activity's actual risks is recorded. Untriggered disciplines are not prerequisites. Pilot or production promotion additionally requires named discipline owners, independent review, and separation-of-duty evidence.

A status-changing pull request must cite its evidence, update the operational register, preserve applicable exclusions, and pass `python3 scripts/check_docs.py`.
