# Management coordination

The [artifact status register](validated-claim-contract-register.csv) is the lightweight, tool-neutral operational index for the delivery plan's `WF`, `CC`, `FV`, `TF`, `PB`, `RP`, `ST`, `CE`, and `MP` artifacts. It supersedes the former `M1`–`M11` milestone register; milestone status and prerequisite fields no longer authorize or block work.

## Authority and handling rules

1. [`docs/delivery-plan.md`](../delivery-plan.md) remains normative for artifact dependencies, promotion evidence, risks, and exclusions.
2. The register records the four independent status dimensions and coordination metadata; it must not restate substantive requirements.
3. [`docs/decisions.md`](../decisions.md) remains authoritative for decision state and ADR requirements.
4. Discovery participant identities and confidential customer data must not enter the register.
5. Empty evidence or decision references mean no approved reference has been recorded; they do not mean a requirement is satisfied.
6. A status change must identify the artifact version or digest, intended use, evidence, owner, decision date, limitations, and approving authority when applicable.
7. A `no`, `pending`, or `not sought` value in one status field does not block unrelated safe exploration.
8. External-tool changes do not silently supersede repository requirements. A material artifact or gate change must update the owning document and applicable decision record.

## Register conventions

- `exploration_allowed` uses `yes`, `restricted`, or `no`.
- `artifact_provisional` uses `yes`, `no`, or `superseded`.
- `externally_validated` and `approved_for_deployment` use `not sought`, `pending`, `yes`, or `no`.
- Multi-value reference fields use semicolon-separated repository references.
- Limitations are scoped assertions, not a substitute for the promotion language in the delivery plan.
