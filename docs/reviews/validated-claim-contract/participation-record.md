# M1 preliminary participation and boundary record

| Record field | Value |
| --- | --- |
| Milestone/work item | Validated claim and verifier contract / `M1` |
| Originally recorded on | 2026-08-30 |
| Status | **Superseded** — traceability only; the recorded participation claims were not satisfied |
| Authority | [`docs/delivery-plan.md`](../../delivery-plan.md#minimum-conditions-required-to-start-m1) |
| Current correction | [`solo-planning-readiness-record.md`](solo-planning-readiness-record.md#actual-operating-context) |
| Evidence classification | Historical planning record; not participant, approval, review, or milestone evidence |

## Privacy-safe participation record

The identifiers below were recorded as though they resolved to approved participants. The current factual operating-context review established that they do not resolve to assigned people or an independent external participant. They were planning placeholders and cannot establish participation, accountability, acknowledgement, review, approval, or relying-party independence.

| Required role | Historical placeholder | Current disposition |
| --- | --- | --- |
| Delivery | `team-directory:TAG-DELIVERY-01` | **Superseded** — no assigned participant evidenced |
| Product | `team-directory:TAG-PRODUCT-01` | **Superseded** — no assigned participant evidenced |
| Architecture | `team-directory:TAG-ARCHITECTURE-01` | **Superseded** — no assigned participant evidenced |
| Cryptography | `team-directory:TAG-CRYPTOGRAPHY-01` | **Superseded** — no assigned participant evidenced |
| Security | `team-directory:TAG-SECURITY-01` | **Superseded** — no assigned participant evidenced |
| Privacy | `team-directory:TAG-PRIVACY-01` | **Superseded** — no assigned participant evidenced |
| Safety | `team-directory:TAG-SAFETY-01` | **Superseded** — no assigned participant evidenced |
| Telemetry | `team-directory:TAG-TELEMETRY-01` | **Superseded** — no assigned participant evidenced |
| Discovery | `team-directory:TAG-DISCOVERY-01` | **Superseded** — no assigned participant evidenced |
| Relying party | `external-tool:TAG-RP-DECISION-OWNER-01` | **Superseded** — no independent relying-party participant evidenced |

### Relying-party independence correction

The historical statement that `external-tool:TAG-RP-DECISION-OWNER-01` represented an industrial-site decision owner is **Superseded**. No genuine relying-party decision owner has been identified. The maintainer, producer, project team, or an AI system cannot act as a proxy for that external decision owner.

The relying-party role remains **Open** and blocking. Bounded external recruitment outreach is **Current / permitted** under the [Current work authorization](../../current-work-authorization.md#lightweight-pre-m1-outreach-policy), without prior funding or a suitable organic relationship, but only after its minimum privacy arrangement is approved. Outreach does not establish participation, independence, acknowledgement, approval, review, or milestone evidence.

## M1 safety and privacy boundary

The intended documentation-only restriction remains a valid planning safeguard:

- no participant or customer telemetry or research data;
- no prototype, proof, or verifier;
- no telemetry, SITL, or hardware integration or testing;
- no vehicle command path;
- no live ledger or network publication;
- no production authorization; and
- no multi-tenant service or identity boundary.

This restriction does not by itself satisfy the M1 entry conditions because the required real participation and approvals were not obtained.

## Entry-condition disposition

| Minimum M1 condition | Current evidence | Disposition |
| --- | --- | --- |
| Preliminary role participation recorded | No real participants or resolving approved references exist for the required roles; the relying-party role is unassigned. | **Open / not satisfied** |
| M1 safety/privacy boundary recorded and approved | The restriction is documented, but the historical delivery, security, privacy, and safety approvals were not real approvals. | **Open / not satisfied** |

M1 must therefore remain `blocked`; `gate_closed=false`. This record is retained only to explain and supersede the earlier unsupported claims. It authorizes no M1 execution, M2 work, participant research, implementation, or later milestone.
