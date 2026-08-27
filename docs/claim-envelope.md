# Claim envelope specification

| Metadata | Value |
| --- | --- |
| Status | Normative baseline; registered algorithms and concrete proof suites remain Open |
| Audience | Prover, verifier, relying-party, policy, ledger, and interoperability implementers |
| Accountable role | Cryptography lead, with security and protocol-owner approval |
| Review trigger | Envelope, encoding, proof suite, policy, key, revocation, disclosure, replay, or receipt change |
| Authority | Normative wire contract and verifier result model |

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHOULD**, **SHOULD NOT**, and **MAY** are to be interpreted as normative requirements. An envelope conveys a privacy-preserving claim and the material needed to evaluate it; it is not evidence that the underlying sensor was truthful.

## Version and canonical serialization

An envelope version is the two-element unsigned-integer array `[major, minor]`. This specification defines `[1, 0]`. A major version changes field meaning or canonical encoding. A minor version may only add optional fields whose absence preserves meaning. A verifier MUST reject an unknown major version as `unsupported`. It MAY process a newer minor version only when it recognizes every present field and the applicable policy explicitly permits that minor version; otherwise it returns `unsupported`. The version is independent of telemetry-schema, statement, proof-suite, policy, and key versions.

The normative wire representation is deterministic CBOR as specified by RFC 8949 section 4.2, with the following profile:

- the top-level value and every structured child are maps with the exact text-string keys defined below;
- map keys are compared and ordered by their deterministic CBOR encodings; duplicate or unknown keys are forbidden;
- integers use the shortest encoding; indefinite-length items, floating-point values, tags, and CBOR `null` are forbidden;
- text is valid UTF-8 and in Unicode NFC; identifiers use the restricted ASCII syntax stated below;
- byte strings have the exact lengths required by their registered algorithm; and
- an optional field is omitted, never encoded with a sentinel value.

The media type is `application/vnd.mavlink-zkp.claim-envelope+cbor;v=1`. A transport using base64url MUST use the unpadded RFC 4648 URL-safe alphabet and is only a transport wrapper; implementations MUST decode it to bytes before canonicality checks. JSON MAY be emitted as a diagnostic view with media type `application/vnd.mavlink-zkp.claim-envelope+json;v=1`, but it is non-canonical and MUST NOT be hashed, signed, committed, or accepted as the verification wire form.

Canonicality is verified by strict decode, schema validation, deterministic re-encoding, and byte-for-byte comparison with the received CBOR. Failure at any step is `malformed`.

## Envelope fields

All identifier strings (`statement_id`, `proof_suite`, `domain`, and URI-like identifiers) are case-sensitive ASCII, 1–255 bytes, and MUST NOT contain whitespace or control characters. Digest and identifier byte strings are raw bytes rather than hexadecimal or base64 text. Bounds below are inclusive.

| Field | Type | Required | Normative meaning |
| --- | --- | --- | --- |
| `envelope_version` | `[uint, uint]` | Yes | Envelope major and minor version; exactly `[1, 0]` here. |
| `statement_id` | text | Yes | Registered statement and statement-version identifier defining the proved predicate and ordered public-input mapping. For the first statement this identifies the speed-at-or-below-policy-bound predicate. |
| `proof_suite` | text | Yes | Registered proof system, transcript, curve/field, hash, commitment, nullifier, and public-input encoding profile. No algorithm defaults are permitted. |
| `assurance_tier` | uint `0..255` | Yes | Policy-defined assurance tier. It is a claim input, not a verifier-computed score; a verifier MUST confirm that policy permits it. |
| `policy_ref` | map | Yes | Exactly `{"id": text, "version": uint, "digest": bstr}`. `digest` is over the canonical policy artifact using the suite's registered digest algorithm. |
| `validity` | map | Yes | Exactly `{"not_before": uint, "not_after": uint}` in Unix epoch seconds. `not_before <= not_after`; both endpoints are inclusive. |
| `domain` | text | Yes | Relying-party/deployment context. It MUST be an input to the statement or a suite-defined domain-bound public-input digest. Exact string comparison is required; redirects, aliases, and case folding are forbidden. |
| `commitment` | bstr | Yes | Suite-sized commitment to the private record and all interpretation-critical fields required by the statement specification. |
| `nullifier` | bstr | Yes | Suite-sized, domain-separated replay identifier binding at least the domain, policy, source pseudonym, and record nonce. |
| `verification_key_id` | map | Yes | Exactly `{"id": text, "version": uint, "digest": bstr}`; identifies and integrity-binds one authenticated verification-key artifact. |
| `public_inputs` | map | Yes | The exact allowlisted, typed public values required by `statement_id`, excluding values already represented by canonical envelope fields. Unknown inputs are forbidden. |
| `proof` | map | Yes | Exactly one proof form defined below. |
| `ledger_receipt` | map | No | Optional receipt defined below; it does not change cryptographic proof validity. |

The canonical public-input sequence is the registered `statement_id` sequence. It MUST include, directly or through a registered suite-defined digest, the statement/schema and circuit identifiers, policy digest, validity window, domain, commitment, nullifier, verification-key identifier, assurance tier, and statement-specific public values. A verifier MUST reconstruct that sequence from the envelope and MUST NOT trust a separately supplied public-input byte array.

### Proof attachment and reference

`proof` is exactly one of:

- attached: `{"kind": "attached", "content_type": text, "bytes": bstr}`; or
- referenced: `{"kind": "referenced", "content_type": text, "uri": text, "digest": bstr, "size": uint}`.

`content_type` MUST be the registered, versioned media type for `proof_suite`. An attached proof's size is bounded by the suite registry and policy. For a referenced proof, `digest` covers the exact retrieved bytes, `size` is their exact byte length, and both MUST be checked before parsing. Fetching MUST follow verifier policy for scheme, host, redirects, size, timeout, and authentication. A reference MUST NOT embed credentials. Fetch failure, timeout, or an unavailable but otherwise permitted dependency produces `temporarily_unverifiable`; a forbidden reference, digest/size mismatch, or proof parse failure produces `invalid`. Verifiers MUST NOT silently change between attached and referenced material or treat the URI as proof identity.

### Optional ledger receipt

When present, `ledger_receipt` is exactly `{"ledger_id": text, "transaction_id": text, "recorded_at": uint, "payload_digest": bstr, "finality": text, "proof": bstr}`. The registered ledger profile defines canonical transaction identifiers, the digest algorithm, `finality` values, and receipt-proof verification. `payload_digest` MUST bind the canonical envelope with `ledger_receipt` omitted, preventing recursion. A receipt is corroborating submission/order evidence only: it neither repairs an invalid claim nor establishes sensor truth, freshness before submission, or proof validity. Receipt failure is reported as receipt metadata alongside the primary outcome unless policy requires a valid receipt; under such a policy, cryptographically bad or inconsistent receipts are `invalid`, revoked ledger trust is `revoked`, and an unavailable ledger dependency is `temporarily_unverifiable`.

## Public disclosure and binding rules

The canonical envelope is public-disclosure material. Producers MUST use an explicit, reviewed allowlist per `(envelope major, statement_id, proof_suite, assurance_tier)` and MUST disclose only fields in this specification and the selected statement's `public_inputs`. Private witnesses, commitment openings, source identifiers or stable pseudonyms, record nonces, salts, raw telemetry, exact position, signing keys, and linkable operational metadata MUST NOT appear anywhere in an envelope, URI, receipt, or extension. Hashing or encrypting a disallowed stable identifier does not make it permitted.

Policy artifacts MUST state the permitted statement and suite versions, assurance tiers, public-input names and bounds, validity duration and clock/skew rules, accepted domains, key status, revocation source/freshness, nullifier retention scope, proof-reference rules, and any ledger requirement. Envelope `policy_ref.digest` and `verification_key_id.digest` MUST be compared in constant time after length validation. A policy or key selected only by a mutable name is insufficient.

Before proof verification, the verifier MUST authenticate and integrity-check the referenced policy, verification key, suite parameters, and revocation state. It MUST evaluate at an explicit integer `decision_time` from its configured clock authority. An envelope is current when `not_before <= decision_time <= not_after`, subject only to the policy's explicit skew rule. Nullifier uniqueness MUST be checked and recorded atomically in a durable store scoped by domain, policy, and statement. A nullifier is recorded only after all required checks succeed; concurrent attempts MUST yield at most one `valid` result.

## Verifier outcomes

A verifier returns exactly one primary outcome code plus a non-sensitive reason code, evaluated facts (including `decision_time` and policy/key digests), and receipt status when applicable. It MUST NOT expose witnesses or secrets in diagnostics. Outcomes are deterministic for the same envelope and the same authenticated policy, keys, revocation snapshot, replay state, decision time, and dependency results.

| Outcome | Required use |
| --- | --- |
| `valid` | Canonical/schema checks, version support, disclosure policy, domain, time, artifact authentication, revocation, replay, proof, and required receipt checks all pass, and the nullifier is atomically accepted. |
| `invalid` | A supported, well-formed claim fails a cryptographic or binding check, uses a wrong domain/policy/key, violates disclosure or policy constraints, has altered public inputs, or has a bad proof/reference/required receipt. |
| `expired` | The authenticated claim is outside its permitted time: `decision_time > not_after` (or violates the policy's explicit maximum-age/skew rule). A not-yet-valid claim (`decision_time < not_before`) also uses `expired` with reason `NOT_YET_VALID`. |
| `replayed` | The nullifier is already accepted in the applicable durable replay scope, including a losing concurrent submission. |
| `revoked` | An otherwise addressable policy, verification key, proof suite/parameters, issuer authorization, or policy-required ledger trust anchor is revoked at the decision time. |
| `unsupported` | The canonical envelope uses an unsupported envelope/statement/suite version, assurance tier, registered algorithm, content type, or optional feature. It does not mean a supported proof failed. |
| `malformed` | Bytes are not canonical CBOR or violate structural schema, types, lengths, ranges, required/exclusive fields, UTF-8/NFC, or unknown-field rules. No network lookup or proof verification SHOULD occur. |
| `temporarily_unverifiable` | Required authenticated material, replay storage, clock/revocation freshness, referenced proof, or policy-required ledger service is transiently unavailable and no definitive negative result is known. This outcome MUST NOT be cached or represented as valid. |

Outcome precedence is: `malformed`, `unsupported`, `invalid` for locally decidable policy/binding violations, `expired`, `revoked`, `replayed`, cryptographic `invalid`, `temporarily_unverifiable`, then `valid`. Implementations SHOULD continue safe local checks when useful but MUST return the highest-precedence applicable result and MUST NOT fetch attacker-selected resources before structural, version, domain, and policy-reference checks. No outcome other than `valid` authorizes the claimed action; retry is appropriate only for `temporarily_unverifiable`, or after the relevant inputs/state have deliberately changed.

## Registries and conformance

The project MUST maintain reviewed registries for statement identifiers, proof suites and media types, digest lengths, canonical public-input order and encoding, verification-key identifiers, assurance tiers, policy schemas, and ledger profiles. Registry entries are immutable; changes receive new identifiers or versions. Removing support requires an announced migration and revocation/retention plan.

An implementation is conformant only if it passes the golden-vector and independent cross-implementation requirements in [testing and operations](testing-and-operations.md#claim-envelope-interoperability).
