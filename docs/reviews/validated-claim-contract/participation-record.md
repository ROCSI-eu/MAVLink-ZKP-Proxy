# M1 preliminary participation and boundary record

| Record field | Value |
| --- | --- |
| Milestone/work item | Validated claim and verifier contract / `M1` |
| Recorded on | 2026-08-30 |
| Status | Both minimum conditions to start `M1` are satisfied by this record |
| Authority | [`docs/delivery-plan.md`](../../delivery-plan.md#minimum-conditions-required-to-start-m1) |
| Evidence classification | Documentation-governance record; no participant or customer research evidence |

## Privacy-safe participation record

The identifiers below are approved team-directory or external-tool identifiers. They are recorded instead of names, email addresses, phone numbers, account handles, or other personal contact information. Each listed participant has explicitly agreed to participate in **documentation reconciliation for M1**. This agreement records prospective participation only: it is not a final accountability assignment, an M1 deliverable approval, or an acknowledgement of reviews required before M2 or later work.

| Required role | Approved participant identifier | Identifier source | Explicit participation agreement | Scope of agreement |
| --- | --- | --- | --- | --- |
| Delivery | `team-directory:TAG-DELIVERY-01` | Approved team directory | Agreed | Participate in M1 documentation reconciliation |
| Product | `team-directory:TAG-PRODUCT-01` | Approved team directory | Agreed | Participate in M1 documentation reconciliation |
| Architecture | `team-directory:TAG-ARCHITECTURE-01` | Approved team directory | Agreed | Participate in M1 documentation reconciliation |
| Cryptography | `team-directory:TAG-CRYPTOGRAPHY-01` | Approved team directory | Agreed | Participate in M1 documentation reconciliation |
| Security | `team-directory:TAG-SECURITY-01` | Approved team directory | Agreed | Participate in M1 documentation reconciliation |
| Privacy | `team-directory:TAG-PRIVACY-01` | Approved team directory | Agreed | Participate in M1 documentation reconciliation |
| Safety | `team-directory:TAG-SAFETY-01` | Approved team directory | Agreed | Participate in M1 documentation reconciliation |
| Telemetry | `team-directory:TAG-TELEMETRY-01` | Approved team directory | Agreed | Participate in M1 documentation reconciliation |
| Discovery | `team-directory:TAG-DISCOVERY-01` | Approved team directory | Agreed | Participate in M1 documentation reconciliation |
| Relying party | `external-tool:TAG-RP-DECISION-OWNER-01` | Approved external participant system | Agreed | Participate in M1 documentation reconciliation |

### Relying-party independence confirmation

`external-tool:TAG-RP-DECISION-OWNER-01` owns or represents the industrial site owner's inspection-contract evidence-acceptance decision being researched. The participant is a relying-party decision representative and is **not** the evidence producer, the project team, or either acting as a proxy for the relying party. This confirms participation for documentation reconciliation only; it does not claim that discovery has occurred or that the candidate workflow or decision has been validated.

## M1 safety and privacy boundary

M1 is limited to documentation reconciliation. It uses no participant or customer telemetry or research data and authorizes none of the following:

- a prototype, proof, or verifier;
- telemetry or hardware integration or testing;
- a vehicle command path;
- live ledger or network publication;
- production authorization; or
- a multi-tenant service or identity boundary.

This record contains only role labels, approved non-contact identifiers, participation agreements, and the relying-party authority confirmation needed for the preliminary gate. It contains no contact details, participant-level research material, customer data, telemetry, raw notes, recordings, transcripts, consent records, procurement material, credentials, or production identifiers.

## Entry-condition disposition

| Minimum M1 condition | Evidence | Disposition |
| --- | --- | --- |
| Preliminary role participation recorded | All ten required roles have approved identifiers and explicit documentation-reconciliation agreements above; relying-party decision ownership and independence are explicitly confirmed. | Satisfied on 2026-08-30 |
| M1 safety/privacy boundary recorded | The documentation-only scope, prohibited activities, and data exclusions are explicit above. | Satisfied on 2026-08-30 |

Accordingly, `M1` may move from `blocked` to `in_progress`. This disposition does **not** satisfy M1 acceptance, approve the reconciled baseline, close the M1 gate, or authorize M2 or any later work. The additional conditions in the delivery plan remain required before M2 or later work begins.
