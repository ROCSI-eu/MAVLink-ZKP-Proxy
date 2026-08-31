# M1 documentation-reconciliation boundary record

| Record field | Value |
| --- | --- |
| Milestone/work item | Validated claim and verifier contract / `M1` |
| Originally recorded on | 2026-08-30 |
| Entry-condition authority | [`docs/delivery-plan.md`](../../delivery-plan.md#accountability-levels-and-m1-start) |
| Scope | Documentation reconciliation only |
| Status | Current restriction; sufficient for solo concept M1 entry |
| Evidence classification | Maintainer planning boundary; not accepted participant, review, approval, or milestone evidence |
| Current correction | [`solo-planning-readiness-record.md`](solo-planning-readiness-record.md#current-disposition) |
| Review trigger | Any proposed activity, data use, environment, publication, or service boundary outside the restriction below |

## M1 activity boundary

Any future M1 activity is limited to **documentation reconciliation only**. It may compare, resolve, and record contradictions among repository documents and produce the documentation artifacts identified for M1 in the delivery plan. It uses no participant or customer telemetry or research data.

This boundary permits **no**:

- prototype, proof, or verifier;
- telemetry, SITL, or hardware integration or testing;
- command path, including a vehicle command path;
- live ledger or network publication;
- production use or production authorization; or
- multi-tenant service or identity boundary.

These restrictions remain Current safeguards and authorize M1 documentation reconciliation at solo concept level. They do not authorize external validation or technical, pilot, or production work.

## Operational controls

1. Planning inputs and outputs are limited to repository documentation and documentation-governance records.
2. No participant-level or customer data, telemetry, research notes, recordings, transcripts, credentials, production identifiers, or extracts from live systems may be collected, copied, linked, or processed.
3. Planning work must not create or exercise executable, integration, testing, command, publication, production, tenancy, or identity paths.
4. A contributor who encounters data or a requested activity outside this boundary must stop that activity and avoid committing the material.
5. Maintainer review may close M1 only as a **solo-maintainer provisional baseline**; this restriction does not independently approve it or authorize M2 or later work.

## Approval references

The historical approval references below are **Superseded**. The role identifiers did not resolve to assigned people, and no valid multi-role approvals occurred.

| Approver role | Historical placeholder | Historical approval reference | Current disposition |
| --- | --- | --- | --- |
| Delivery | `team-directory:TAG-DELIVERY-01` | `TAG-M1-BOUNDARY-DELIVERY-2026-08-30` | **Superseded** — not approval evidence |
| Security | `team-directory:TAG-SECURITY-01` | `TAG-M1-BOUNDARY-SECURITY-2026-08-30` | **Superseded** — not approval evidence |
| Privacy | `team-directory:TAG-PRIVACY-01` | `TAG-M1-BOUNDARY-PRIVACY-2026-08-30` | **Superseded** — not approval evidence |
| Safety | `team-directory:TAG-SAFETY-01` | `TAG-M1-BOUNDARY-SAFETY-2026-08-30` | **Superseded** — not approval evidence |

The maintainer may enforce the restriction as a planning rule, but that is not independent delivery, security, privacy, or safety approval.

## Entry-condition disposition

The boundary is recorded and M1 may be `in_progress` at solo concept level. Historical external approvals remain Superseded, but their absence is not an M1 blocker. Maintainer review may finish M1 as a **solo-maintainer provisional baseline**; future external roles are promotion blockers only for the risk-triggered external-validation, pilot, or production work.
