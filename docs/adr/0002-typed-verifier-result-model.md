# ADR-0002: Typed verifier result model

| Metadata | Value |
| --- | --- |
| Status | Current |
| Accountable owner | Cryptography lead |
| Required reviewers | Architecture, security, product, and relying-party leads |
| Decision date | 2026-08-27 |
| Review trigger | Result dimension/value or precedence change; envelope/API major-version freeze; publication or assurance semantics change |
| Supersedes | The single primary-outcome contract in the pre-freeze claim-envelope draft |

## Context

The draft public contract collapsed proof verification, policy eligibility, time, revocation, replay, assurance, and policy-required receipts into one primary outcome. That made a valid proof appear cryptographically invalid when a contextual check failed, allowed publication availability to obscure proof validity, and left a relying party's business decision dangerously close to verifier output. Consumers could not reliably distinguish permanent evidence defects, contextual rejection, retryable dependencies, and external discretion.

## Decision

The normative result uses independent closed, typed dimensions for envelope/cryptographic evaluation; policy, freshness, revocation, and replay acceptance; declared/effective assurance and tier sufficiency; and optional publication receipt verification/finality. Each dimension has explicit precedence. Optional publication unavailability never changes cryptographic validity and is ignored for aggregate acceptance unless authenticated policy requires publication.

An aggregate `service_disposition`, when exposed, is derived convenience data rather than a proof result. The verifier never produces or serializes a relying-party business decision; applications record such a decision separately with its own authority and audit data. The complete normative schema, values, precedence, and derivation are defined in `docs/claim-envelope.md`.

## Considered options

1. **Typed independent dimensions (selected).** Preserves evidence facts, makes retry and rejection causes machine-readable, and prevents category errors.
2. **Keep one primary outcome plus reason codes.** Rejected because reason-code combinations cannot prevent consumers from treating the primary value as cryptographic truth and provide no stable typing for simultaneous facts.
3. **Return only raw evaluation facts.** Rejected because interoperable clients still need bounded enums, precedence, and deterministic acceptance inputs.
4. **Let the verifier return the business decision.** Rejected because verifier inputs cannot capture the relying party's contractual authority, risk, or wider evidence and because this conflates mathematical evaluation with authorization.

## Consequences

- This is a breaking change to the planned public result contract. Any implementation or fixture using the former primary outcomes must migrate before the contract is declared stable; a released predecessor would require a new API/result major version.
- A valid proof can be policy-rejected, replayed, assurance-insufficient, accompanied by an invalid receipt, or rejected by the relying party without contradiction.
- Clients must consume named dimensions and must not infer cryptographic validity from lifecycle state or aggregate disposition.
- Publication adapters can fail independently; optional outages cannot downgrade cryptographic evaluation.
- Audit and telemetry may carry safe dimension values but not restricted proof inputs or the external decision as if it came from the verifier.

## Evidence, validation, and rollback

Golden vectors and two independent implementations must cover every enum and precedence collision, including valid-proof/policy-rejected, valid-proof/replayed, valid-proof/receipt-invalid, valid-proof/assurance-insufficient, and verifier-valid/business-rejected cases. Contract tests must recompute aggregate disposition, reject inconsistent serialized aggregates, and prove optional publication outages leave cryptographic evaluation unchanged.

Rollback before contract freeze requires superseding this ADR and updating all affected normative documents and vectors atomically. After freeze, changing or recombining dimensions requires a new public result/API major version and migration guidance; silently restoring a single outcome is forbidden.

## Affected documents

- `docs/claim-envelope.md`
- `docs/architecture.md`
- `docs/commercial-model.md`
- `docs/product-scope.md`
- `docs/testing-and-operations.md`
- `docs/decisions.md`
