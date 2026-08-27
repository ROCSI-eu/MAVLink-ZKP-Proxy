# Data and proof model

| Metadata | Value |
| --- | --- |
| Status | Proposed; encoding and proof system are Open |
| Audience | Cryptography, telemetry, security, and implementing engineers |
| Accountable role | Cryptography lead, with telemetry and security approval |
| Review trigger | Supported message, unit, schema, encoding, circuit, commitment, nullifier, or disclosure change |
| Authority | Normative requirements; JSON record is illustrative and non-canonical |

The public wire contract, disclosure boundary, artifact references, and verifier result semantics are defined by the normative [claim envelope specification](claim-envelope.md). If an illustrative representation in this document conflicts with that specification, the claim envelope specification governs.

## Canonical telemetry model

The MVP snapshot draws only from the selected MAVLink dialect's `GLOBAL_POSITION_INT` and `VFR_HUD`. Compatibility with a pinned SITL and exact field selection MUST be demonstrated before schema approval. The internal record uses integers and rejects overflow or unavailable values rather than coercing them.

| Concept | Unit/encoding | Source direction |
| --- | --- | --- |
| Latitude/longitude | signed degrees × 10^7 | `GLOBAL_POSITION_INT` candidate fields |
| Relative altitude | signed millimetres | `GLOBAL_POSITION_INT` candidate field |
| Horizontal ground speed | non-negative centimetres/second | Normalize a validated groundspeed source |
| Observed/received time | integer milliseconds plus named clock provenance | Source and bridge clocks; not inherently trusted |
| Source trust | closed enum, not Boolean | Parser/signature evaluation |

Required initial trust values are `SIGNED_VALID`, `UNSIGNED`, `SIGNATURE_INVALID`, and `UNKNOWN`. `SIGNATURE_INVALID` records MUST NOT be claim-eligible. Eligibility for `UNSIGNED` or `UNKNOWN` is **Open** and must be explicit in policy; no state silently becomes `SIGNED_VALID`.

Illustrative edge/debug JSON:

```json
{
  "schema_version": 1,
  "record_id": "0191d7c8-632f-7f3d-a5ad-2dcbe4223d24",
  "source": {
    "system_id": 23,
    "component_id": 1,
    "trust": "SIGNED_VALID",
    "message_ids": [33, 74]
  },
  "observed_at_unix_ms": 1712345678000,
  "received_at_unix_ms": 1712345678120,
  "position": {
    "latitude_deg_e7": 513456789,
    "longitude_deg_e7": -113456789,
    "relative_altitude_mm": 54500
  },
  "ground_speed_cm_s": 125,
  "policy_digest": "sha256:illustrative-not-a-complete-digest",
  "nonce": "illustrative-base64url-value"
}
```

This JSON is not the proof encoding and its values do not define production identifiers or algorithms.

## Deterministic encoding requirements

Before circuit implementation, a versioned specification MUST define field order, widths, signedness, bounds, absence semantics, byte order, byte-to-field conversion, field-reduction rejection, hash/commitment parameters, and domain-separation tags. Floating-point proof inputs are prohibited. Golden vectors MUST cover minimum, maximum, negative where allowed, overflow, absent, malformed, and cross-language cases.

A record commitment binds every field needed to interpret the claim, including schema/circuit version, policy digest, trust state where eligibility depends on it, speed, source commitment, nonce, and approved time-window representation. The final bound-field list remains **Open** pending privacy and circuit review.

## First proof statement

Given a versioned committed record and policy, the prover knows a valid opening whose normalized horizontal speed `speed_cm_s` is within the supported integer range and satisfies `speed_cm_s <= maximum_speed_cm_s`. Successful verification represents the pass claim; it does not prove source truth or recency by itself.

### Private witness

- normalized horizontal speed;
- source pseudonym/commitment opening;
- record nonce and commitment opening; and
- only those additional fields approved by the threat model.

### Public inputs

- schema and circuit identifiers;
- policy digest and public `maximum_speed_cm_s`;
- approved coarse time-window identifier;
- record commitment;
- domain-separated nullifier; and
- deployment/domain identifier required to prevent cross-context replay.

### Circuit constraints

- `speed_cm_s` and `maximum_speed_cm_s` have explicit bit widths and range constraints.
- The circuit enforces the non-strict upper bound, including equality.
- Commitment and nullifier calculations use the versioned, domain-separated encoding.
- The nullifier binds at least deployment domain, policy, source pseudonym, and nonce.
- Unsupported versions or non-canonical encodings cannot verify.

## Recency, replay, and limitations

A timestamp alone does not prove recency. Until trustworthy time attestation exists, the verifier applies an external policy using a named clock authority, maximum skew, accepted window, sequence evidence, and durable nullifier uniqueness. Those values and the handling of resets/reordering are **Open** and owned by security.

MAVLink signing, if validated and provisioned, authenticates protocol frames; it does not validate sensors. UDP provides neither confidentiality nor reliable delivery. A chain may timestamp and durably order submission metadata; it does not authenticate the original reading.

## Data classification and lifecycle

Classification and retention controls are authoritative in [security and privacy](security-and-privacy.md). Witness and opening material MUST be released after proving and never logged. Exact position is not required by the first speed statement and MUST NOT become a public input. Hashing stable identity is pseudonymization, not anonymization.

Schema, circuit, policy, proving/verifying key, commitment, nullifier, and domain versions require compatibility rules and migration/revocation procedures before persistence or live-chain work. Key-generation/setup assumptions depend on the selected proof system and remain **Open**.

## Acceptance and related documents

Acceptance requires reviewed golden vectors; circuit boundary/overflow/altered-input tests; an independent verifier without witness access; replay, wrong-policy, wrong-domain, and unsupported-version rejection; and benchmark evidence identifying hardware and parameters. The [claim envelope specification](claim-envelope.md) owns the canonical public exchange format and verifier outcomes. [Architecture](architecture.md) owns component flow, [security and privacy](security-and-privacy.md) owns eligibility and handling controls, and [decisions](decisions.md) owns closure evidence.
