# Management coordination

The [validated-claim contract register](validated-claim-contract-register.csv) is a lightweight, tool-neutral operational index for work items `M1`–`M11`.

## Authority and handling rules

1. [`docs/delivery-plan.md`](../delivery-plan.md) remains normative for scope, prerequisites, deliverables, acceptance, risks, and exclusions.
2. The register is the operational index for status and external-tool mapping; it must not restate substantive requirements.
3. [`docs/decisions.md`](../decisions.md) remains authoritative for decision state and ADR requirements.
4. Discovery participant identities and confidential customer data must not enter the register.
5. `accountable_person_ref` must use an approved team-directory or external-tool identifier rather than personal contact details.
6. `external_tool_ref` may remain empty until import. Every imported ticket must preserve the repository work-item ID.
7. A transition to `accepted` requires both evidence references and approval from all required reviewer roles.
8. External-tool changes do not silently supersede repository requirements. A material scope or gate change must update the owning document and the applicable decision record.

## Register conventions

- `status` uses only `not_started`, `blocked`, `in_progress`, `in_review`, `accepted`, `rejected`, or `deferred`.
- Multi-value fields use semicolon-separated repository IDs, role names, or references.
- Empty cells mean that no approved reference has been recorded; they do not mean that a requirement has been satisfied.
- `gate_closed` is `true` only when the gate named by the delivery plan is closed through its required review.
- `adr_required` records `true`, `false`, or `conditional`; consult the decision register and delivery plan for the authoritative requirement and its conditions.
- `blocking_reason` is a short coordination label, not a substitute for prerequisite or acceptance language in the delivery plan.
