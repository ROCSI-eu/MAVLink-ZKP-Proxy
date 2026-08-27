# ADR-0001: Half-open validity windows for envelope version 1

| Metadata | Value |
| --- | --- |
| Status | Current |
| Accountable owner | Cryptography lead |
| Required reviewer | Security lead |
| Decision date | 2026-08-27 |
| Review trigger | A documented relying-party requirement for different endpoint semantics; envelope-major-version change; clock or skew model change |
| Supersedes | None |

## Context

The draft envelope specification described both validity endpoints as inclusive, while the policy lifecycle already used an inclusive lower bound and exclusive upper bound. That contradiction would make canonical vectors, verifier outcomes, adjacent policy windows, and decisions at `not_after` implementation-dependent. Before envelope version 1 and its canonical vectors are frozen, the cryptography lead, with security-lead review, selected the semantic contract below. No relying-party requirement for inclusive upper bounds or another rule is recorded.

## Decision

Envelope version 1 validity windows are non-empty half-open intervals `[not_before, not_after)`. A verifier evaluates currency as:

```text
not_before <= decision_time < not_after
```

Consequently, equality at `not_before` is current, equality at `not_after` is expired, and `not_before` MUST be less than `not_after`. Clock/skew policy may define a tolerance calculation, but it does not change endpoint inclusivity. A relying-party requirement for another boundary rule must be documented and reviewed by the cryptography and security leads, use an explicitly versioned contract, and must not reinterpret a version 1 envelope.

Canonical golden vectors are not frozen until they include equality at, just before, and just after each endpoint, plus empty and inverted windows and applicable skew cases.

## Considered options

1. **Half-open `[not_before, not_after)` (selected).** This follows the conventional interval model, composes adjacent windows without overlap, and agrees with the existing policy lifecycle.
2. **Closed `[not_before, not_after]`.** This makes the upper-bound second belong to adjacent windows and conflicted with existing expiry language. No relying-party requirement supports it.
3. **Policy-selectable endpoint semantics within version 1.** This adds a consensus-critical semantic switch and risks two verifiers interpreting identical bytes differently unless more data is bound into the envelope.

## Consequences

- Adjacent windows can meet at one timestamp without both being current.
- A claim evaluated at `decision_time == not_after` returns `expired` when no higher-precedence failure applies.
- Empty and inverted windows are structurally invalid, so a one-second interval is represented by `not_after == not_before + 1`.
- Existing draft examples and planned vectors must use the half-open rule; implementations based on the former inclusive prose must change before claiming version 1 conformance.
- Different relying-party semantics require new reviewed versioning and new vectors rather than a policy-time reinterpretation.

## Evidence and validation

The claim-envelope field semantics, currency check, outcome table, and precedence order use the same inequality. The data/proof lifecycle and authorized-window policy example use the same model. The interoperability plan requires deterministic boundary, malformed-window, and skew vectors in two independent implementations.

Rollback before the version 1 freeze consists of superseding this ADR and updating all affected normative documents and unreleased vectors together. After the freeze, changing endpoint semantics requires a new envelope major version and migration plan.

## Affected documents

- `docs/claim-envelope.md`
- `docs/data-and-proof-model.md`
- `docs/testing-and-operations.md`
- `docs/product-scope.md`
- `docs/decisions.md`
