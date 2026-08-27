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

## Telemetry assurance model

Assurance describes the provenance of the telemetry used by a claim, not the strength of the proof system. A valid zero-knowledge proof preserves the assurance of its inputs; it cannot upgrade them. The following ordered tiers are the only assurance labels. Higher tiers add evidence but do not make sensors infallible, establish continuous coverage, or by themselves establish physical, safety, contractual, or regulatory compliance.

| Tier | What is authenticated | What remains untrusted | Permitted claim wording | Eligible use cases | Prohibited reliance | Key-provisioning expectations | Required verification metadata |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `A0_SYNTHETIC` — synthetic | Fixture identity, schema/version, and test-run integrity when produced by the controlled test harness. | Any relationship to a real device, flight, place, time, sensor, or operator. | “The synthetic fixture satisfies/fails policy P under version V.” | Development, CI, demonstrations clearly labelled synthetic, proof interoperability, and negative testing. | Real-world events; contractual, physical, safety, operational, or regulatory conclusions. | No device key. Fixture-generator and CI signing keys, if used, are test-only, namespace-separated, documented, and barred from higher tiers. | Tier ID; fixture and generator version/digest; synthetic marker; policy/claim/circuit and verifier versions; proof result; verification time; domain; validity/replay result; test-key identifier if used. |
| `A1_UNSIGNED_SOFTWARE` — unsigned software telemetry | The verifier authenticates only the proof and the gateway/software processing named in the evidence; no telemetry origin is cryptographically authenticated. | Sender identity, transport source, software host, sensor origin and truth, capture time, and resistance to injection, replay, or modification before commitment. | “Unsigned telemetry received by gateway G satisfies/fails policy P”; never “device reported” or “vehicle complied.” | Local experimentation, migration diagnostics, and explicitly low-assurance analytics where spoofing has no material consequence. | Identity, physical occurrence, safety, payment, access, enforcement, contractual acceptance, or regulatory compliance. | No source key is accepted. Gateway/verifier keys follow environment separation and normal lifecycle controls; absence of a source key is explicit, not a provisioning exception. | Tier ID; `UNSIGNED`/`UNKNOWN` source trust state; gateway/software identity and version; ingestion transport; observation/receipt-time basis; policy/claim/circuit and verifier versions; proof result; domain; expiry/replay result; explicit missing-source-authentication reason. |
| `A2_PROTOCOL_SIGNED` — protocol-signed telemetry | Message integrity and possession of an authorized protocol signing key at the signed-message boundary, plus the signed fields covered by the pinned protocol profile. | Whether the key is held by the intended physical device, sensor truth/calibration, pre-signing data path, device integrity, operator authority, location/time truth, and coverage between messages. | “Telemetry signed by protocol key K satisfies/fails policy P for the stated observation scope.” | Authenticated-source demonstrations and low-risk audit evidence where the relying party explicitly accepts protocol-key provenance. | Claims of hardware origin, tamper resistance, airworthiness, continuous-flight, safety, or regulatory compliance. | Unique authorized keys are provisioned through an authenticated process; owner/device mapping, scope, algorithm/profile, activation, rotation, expiry, compromise response, and revocation are recorded. Shared/default/test keys are ineligible. | Tier ID; `SIGNED_VALID` state; protocol/profile and signed-field coverage; pseudonymous key ID and authorization-chain digest; key status and revocation check time; sequence/link ID; observation and verification time basis; policy/claim/circuit/verifier versions; proof result; domain; expiry/replay result. |
| `A3_APPROVED_GATEWAY_ATTESTED` — approved gateway-attested telemetry | An approved gateway's identity, measured/approved software configuration, ingestion path, transformation, and binding of received telemetry to the claim; protocol origin only when separately validated and recorded. | Sensor truth/calibration, physical mounting/device identity unless in the gateway approval, inputs before the gateway boundary, operator intent, and completeness outside the declared coverage. | “Approved gateway G attests that telemetry processed under profile C satisfies/fails policy P for scope S.” | Contractual evidence and controlled pilots whose relying-party policy names the gateway approval, configuration, and residual risks. | Unqualified physical-device origin, safety certification, regulatory compliance, or conclusions beyond the attested path and coverage interval. | Gateway keys are generated/stored in an approved protected boundary; enrollment binds key to gateway, owner, approval profile, and environment. Authorized configurations, renewal, rotation, revocation, remote-attestation trust anchors, and incident handling are auditable. | Tier ID; gateway pseudonymous ID and approval/profile ID; attestation statement/evidence digest and freshness; software/configuration measurements; trust-anchor and key IDs; source protocol trust state; transformation/normalization version; coverage/time basis; policy/claim/circuit/verifier versions; proof result; domain; expiry/replay and revocation results. |
| `A4_HARDWARE_BACKED_DEVICE` — hardware-backed device telemetry | Possession of a non-exportable device key rooted in approved hardware, its enrollment to the device identity/class, approved boot/firmware measurements, and the device-to-claim data-path elements expressly covered by attestation. | Sensor accuracy/calibration and environment unless separately attested, supply-chain claims outside approval, operator authority, physical mounting/tampering beyond hardware capabilities, time/location truth, and observations outside declared coverage. | “Hardware-backed device D attests that covered telemetry satisfies/fails policy P under device profile H for scope S.” | Higher-assurance asset provenance and governed operational/contractual evidence after device-profile and relying-party approval. | Automatic safety action; claims of sensor truth, uninterrupted mission compliance, certification, or regulatory compliance without the additional authority and evidence required for that decision. | Per-device non-exportable keys are generated or injected under an approved ceremony; manufacturer/owner enrollment and certificate chain bind hardware profile and environment. Secure storage, anti-cloning, firmware authorization, rotation, renewal, revocation, decommissioning, and compromise recovery are tested and audited. | Tier ID; pseudonymous device/key ID; certificate/attestation chain and hardware-profile ID; boot/firmware measurements; attestation nonce and freshness; covered data-path/sensor IDs; enrollment and revocation status/time; calibration reference if policy requires it; coverage/time basis; policy/claim/circuit/verifier versions; proof result; domain; expiry/replay result. |
| `A5_INDEPENDENTLY_CORROBORATED` — independently corroborated telemetry | The qualifying `A2`–`A4` primary evidence and independently controlled evidence sources are each authenticated, then bound to the same event/scope using an approved correlation rule. | Truth shared by correlated failure modes, collusion, independence assumptions, gaps between samples, and any physical fact not measured by the corroborating sources. | “Primary tier Ax evidence and N independent sources corroborate that the covered observations satisfy/fail policy P within tolerances T.” The primary tier must also be named. | High-consequence contractual or oversight review where a documented threat model, independence assessment, and human decision process accept the residual risk. | A standalone guarantee of physical truth, safety, legality, certification, or regulatory compliance; automatic action; or “independent” wording when ownership, keys, clocks, networks, or failure modes are not sufficiently separated. | Every source meets its own tier's provisioning rules. Independent administrative control, trust roots, key ceremonies, revocation paths, and separation of ownership/failure domains are documented; a common gateway key cannot manufacture independence. | Tier ID plus primary tier; source count, per-source tier and pseudonymous key/trust-anchor IDs; independence/profile ID; evidence digests; correlation algorithm/version, tolerances, coverage, clocks, and match result; per-source freshness/revocation results; policy/claim/circuit/verifier versions; proof result; domain; expiry/replay result. |

### Mandatory tier binding and presentation

Every policy, proof request, public verification input, verification result, audit event, API response, operator display, export, and ledger record **MUST** carry the exact tier ID. A policy **MUST** declare both the tier it requires and the tiers it accepts; omission, an unknown tier, or a tier below the requirement fails closed. Verification **MUST** check that the evidence supplies all metadata required by its declared tier, bind the tier into the policy digest and proof/public-input domain, and return at least `declared_tier`, `required_tier`, `tier_check` (`pass` or `fail`), and a machine-readable failure reason. A cryptographically valid proof with a failed tier check is not an accepted verification result.

Tier assignment is based on verified evidence, never on a caller-selected label. Missing, expired, revoked, malformed, or unverifiable tier evidence causes rejection or an explicit downgrade only when policy permits that lower tier; the result records the effective lower tier and downgrade reason. Composite claims use the lowest tier among evidence necessary to the claim unless an approved composition profile specifies and reports a stricter rule. User-facing wording **MUST** use the permitted wording for the effective tier and display the tier adjacent to the result; applications **MUST NOT** hide, rename, or visually imply that low-assurance evidence demonstrates physical or regulatory compliance.

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
