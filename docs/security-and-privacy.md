# Security and privacy

| Metadata | Value |
| --- | --- |
| Status | Proposed threat baseline; listed decisions remain Open |
| Audience | Security, privacy, cryptography, engineering, operations, product, and safety |
| Accountable role | Security lead; product/privacy owner for data purpose; safety owner for hardware boundaries |
| Review trigger | Asset, actor, data flow, trust, cryptography, disclosure, command boundary, or deployment change |
| Authority | Normative minimum controls for the proposed MVP |

## Assets, actors, and trust assumptions

Assets are precise telemetry, mission association, identity mappings, policies, signing/proving/verifying material, witnesses, salts, audit integrity, and availability. Actors include the SITL/vehicle source, operator, auditor/relying party, administrators, external networks, and malicious senders or compromised components.

Assumptions are deliberately limited:

- The source, UDP network, wall clock, prover, operator client, and future chain are separate trust domains.
- Valid protocol signing can support source authentication only after key provisioning and compatibility are validated; it does not prove sensor truth.
- Unsigned, unknown, and invalid signatures remain distinguishable.
- Verification is independent of the prover. Chain consensus is not vehicle or swarm consensus.
- Stable pseudonyms and hashes can be correlated and are not anonymous merely because they obscure plaintext.

## Safety boundary

The MVP is observational. No verifier result, chain event, UI action, timeout, or error path may produce a MAVLink command. Simulation is the only permitted source until the hardware gate passes. Any command path requires a new product decision, hazard analysis, authorization protocol, fail-safe design, and safety review; it is not an extension of the MVP.

## Threat and risk register

Every risk has a response, accountable role, and validation mechanism.

| Threat/risk | Required response | Accountable role | Validation/evidence |
| --- | --- | --- | --- |
| Forged, unsigned, or compromised telemetry | Preserve trust enum; validate signing profile; policy rejects ineligible state | Telemetry lead + security lead | Signed/unsigned/invalid fixtures and key-provisioning review |
| Replay, duplicate, or cross-domain proof | Versioned nonce/nullifier, domain binding, expiry policy, durable uniqueness, idempotency | Security lead | Replay, restart, wrong-domain, and duplicate tests |
| Malformed parser input | Allowlist, strict ranges/lengths, resource limits, dependency review | Telemetry lead | Continuous fuzz corpus and malformed fixtures |
| Witness, key, location, or identity leakage | Data minimization, log denylist, least privilege, memory/crash-dump policy, redaction | Security lead | Log snapshots, failure injection, access review |
| Public-input correlation | Coarse windows, minimal metadata, domain-specific rotating pseudonyms | Product/privacy owner | Observer-focused privacy review |
| Policy/key compromise | Immutable signed/versioned policy, digest pinning, separation, rotation/revocation | Security lead | Rotation and rollback exercise |
| Proving overload or denial of service | Admission control, quotas, bounded queues, cancellation, observable drops | Service owner | Load/fault tests against an approved overload criterion |
| Chain outage, retry, or reorganization | Local verification independence, bounded idempotent retries, explicit finality/reconciliation | Chain lead | Outage/restart/reorganization contract tests |
| Proof incompatibility or excessive cost | Benchmark and target-chain compatibility spikes before commitment | Cryptography + chain leads | Reviewed ADR with executable evidence |
| SDK/network change | Adapter isolation, pinned validated versions, shared mock/live contract suite | Chain lead | Upgrade rehearsal and contract tests |
| Scope expands into vehicle control | Enforce one-way data boundary and separate governance | Product + safety owners | Architecture review and no-command integration assertion |
| Unapproved hardware use | Require hazard analysis and controlled test plan before connection | Safety owner | Signed milestone gate evidence |

Residual severity and acceptance criteria are **Open** until the team adopts a risk-rating method. High-severity residual risk may not be silently accepted; the accountable owner records acceptance in milestone evidence.

## Required control areas

### Signing, keys, and cryptographic material

Key generation, storage, rotation, revocation, backup, access, and incident procedures MUST be specified before any non-local key is used. Secrets never enter logs, fixtures, chain metadata, or browser clients. Proof-system setup assumptions and verification-key distribution remain Open until selection.

### Replay, time, and state

Sequence tracking is evidence, not a complete replay defense. Policy MUST combine canonical domain-separated nullifiers, idempotency, accepted versions, explicit time authority/skew/window rules, and persistent uniqueness where restarts matter. A source timestamp alone is insufficient.

### Authorization, logging, and redaction

The proposed initial roles are `operator` (redacted lifecycle) and `auditor` (approved proof metadata). Administrative policy/key privileges need a separate design. Authentication technology is Open; selecting a token format is not authorization design. Logs and traces use opaque correlation IDs, avoid stable vehicle IDs, and are tested for restricted fields.

### Data classification and retention

| Class | Examples | MVP handling |
| --- | --- | --- |
| Secret | Signing/proving keys, witness, salts/openings | Memory or approved secret boundary; never log |
| Restricted | Exact location, stable identity, raw MAVLink | Do not persist; no operator/chain disclosure |
| Internal | Policy, redacted diagnostics | Authenticated access; duration Open |
| Shareable | Approved versions, proof digest, lifecycle/finality | Publish only after privacy review |

Jurisdiction, lawful purpose, data-subject handling, deletion, and concrete retention remain Open to the product/privacy owner. Raw telemetry retention and object storage are Deferred.

## Unresolved security decisions

- Signing profile, trust-state eligibility, and key provisioning.
- Clock authority, skew/window limits, sequence reset behavior, and nullifier store durability.
- Proof system/setup, hash/commitment/nullifier primitives, and key lifecycle.
- Authentication mechanism, administrative roles, and separation of duties.
- Public metadata allowlist, pseudonym rotation, retention, and incident contact/process.

These are tracked with evidence and due gates in [decisions](decisions.md); none should be inferred from candidate technology names.

## Acceptance and related documents

Security acceptance requires threat review; negative, fuzz, replay, redaction, authorization, restart, rotation, and outage evidence; and explicit disposition of blocking risks at each [delivery gate](delivery-plan.md). The [data and proof model](data-and-proof-model.md) owns cryptographic semantics and [testing and operations](testing-and-operations.md) owns test execution/readiness.
