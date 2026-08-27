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

### Tier evidence disclosure classification

Tier evidence and tier communication are separate. A verifier establishes a tier from authenticated evidence, including private inputs and locally configured trust material; an envelope communicates only the minimum public facts needed to bind and report that tier. The classifications below are normative:

- **private witness**: supplied to the proving/evidence-evaluation boundary, committed and constrained where the statement requires it, but never serialized in the envelope or verifier result;
- **verifier trust-store artifact**: independently configured policy, key, certificate, authorization, attestation root/profile, revocation, or registry material; a prover MAY transport a byte-identical candidate, but it is not a public claim fact and is never trusted from the envelope;
- **committed public fact**: interpretation-critical fact bound by `commitment` or the canonical public-input digest and evaluated by the verifier, while its value is not disclosed in the envelope;
- **selectively disclosed value**: a policy-approved value intentionally exposed in the statement-specific `public_inputs`; absence of approval makes it private/committed, not optional metadata; and
- **public envelope field**: a canonical field defined by the claim-envelope schema. Public fields are not automatically safe for logs, indexes, or ledgers, whose allowlists may be narrower.

A field listed with alternatives uses the least-disclosing classification that still permits independent verification; moving it to a more public class requires a versioned statement/registry change and privacy review.

| Tier | Private witness | Verifier trust-store artifact | Committed public fact | Selectively disclosed value | Public envelope field |
| --- | --- | --- | --- | --- | --- |
| `A0_SYNTHETIC` | Fixture contents; test-run opening; generator/test-key signature evidence when proved rather than externally checked. | Approved fixture-generator/CI test keys and test namespace authorization. | Fixture and generator version/digest; synthetic marker; test-run integrity; test-key identifier if it is not approved for disclosure. | Fixture/generator version or digest and synthetic marker only when the statement profile requires a relying party to see them. | Numeric `assurance_tier` (`0`); statement, policy, suite/key, validity, domain, commitment, nullifier, and proof fields; proof/result communication uses the canonical tier mapping. |
| `A1_UNSIGNED_SOFTWARE` | Raw telemetry; gateway processing record; receipt-time/transport evidence; explicit absence-of-source-auth evidence. | Authorized gateway/verifier software identities, versions, and keys; accepted ingestion and clock profiles. | `UNSIGNED`/`UNKNOWN` trust state; gateway/software identity and version; ingestion transport; receipt-time basis; missing-authentication reason. | Coarsened receipt window, transport class, software profile, or missing-authentication reason only when required by policy. | Numeric `assurance_tier` (`1`) and the common canonical envelope fields; no source key or source identifier. |
| `A2_PROTOCOL_SIGNED` | Signed frame/fields; signature; source pseudonym opening; sequence/link value; observation-time evidence. | Authorized protocol keys, owner/device authorization mapping, protocol/profile and signed-field rules, activation/expiry/revocation records. | `SIGNED_VALID`; signed-field coverage; source-key authorization result/digest; key status and revocation-check time; sequence/link and observation-time basis. | Protocol/profile, coverage, coarse observation window, and a domain-scoped rotating key identifier only when the statement/policy requires disclosure. | Numeric `assurance_tier` (`2`) and the common canonical envelope fields; a stable key or source pseudonym is forbidden. |
| `A3_APPROVED_GATEWAY_ATTESTED` | Attestation statement/evidence; gateway pseudonym opening; measurements; telemetry binding and transformation record; source-protocol evidence. | Gateway enrollment key, approval/profile, attestation roots, authorized measurements/configurations, and revocation/freshness policy. | Gateway approval/profile result; evidence digest and freshness; measurements; source trust; transformation version; coverage/time basis; trust-anchor/key validation result. | Approval/profile ID, measurement/configuration digest, transformation version, coarse coverage, or rotating domain-scoped gateway/key identifier when necessary. | Numeric `assurance_tier` (`3`) and the common canonical envelope fields; no stable gateway pseudonym. |
| `A4_HARDWARE_BACKED_DEVICE` | Device attestation/certificate path candidate; device/key pseudonym opening; boot/firmware measurements; nonce; covered sensor/data-path evidence; calibration evidence. | Manufacturer/owner enrollment, certificate and attestation roots, hardware profiles, firmware authorization, calibration authority, and revocation state. | Chain/profile validation; measurement and freshness result; covered path/sensor class; enrollment/calibration/revocation status and time; coverage/time basis. | Hardware-profile ID, approved measurement digest, covered sensor class, calibration reference, coarse coverage, or rotating domain-scoped device/key identifier only when policy requires it. | Numeric `assurance_tier` (`4`) and the common canonical envelope fields; no stable device identity or pseudonym. |
| `A5_INDEPENDENTLY_CORROBORATED` | All primary/per-source evidence; source pseudonym openings; correlation inputs, clocks, match details, and independence evidence. | Each source's tier trust artifacts; independence/ownership/failure-domain profile; correlation-rule authorization and per-source revocation material. | Primary tier; qualifying source count and per-source tiers; independence/profile result; evidence digests; correlation algorithm/version, tolerances, coverage, clock treatment, match, freshness, and revocation results. | Primary tier, source count/per-source tiers, independence/profile ID, correlation version/tolerances, coarse coverage, or rotating per-source key/trust-anchor identifiers only when necessary. | Numeric `assurance_tier` (`5`) and the common canonical envelope fields; the primary tier is disclosed only through an approved `public_inputs` entry, not a second tier label. |

“Common canonical envelope fields” means the fields required by the [claim envelope](claim-envelope.md#envelope-fields), not all tier-establishment evidence. Policy/claim/circuit/verifier versions and proof result remain public through those canonical fields or the typed verifier result as applicable; verification time, replay, freshness, revocation, and tier-check outcomes are public result fields, not proof-envelope evidence. No tier requires public disclosure of a source pseudonym. Rotating key identifiers are permitted only under the claim-envelope rules below and are never evidence of identity by themselves.

### Mandatory tier binding and presentation

Every policy, proof request, public verification input, verification result, audit event, API response, operator display, export, and ledger record **MUST** carry the tier using the canonical mapping: the envelope/public-input encoding carries its numeric value, while human-readable and paired typed surfaces carry the exact string tier ID and reject inconsistency. A policy **MUST** declare both the tier it requires and the tiers it accepts; omission, an unknown tier, or a tier below the requirement fails closed. Verification **MUST** check that the evidence supplies all metadata required by its declared tier, bind the tier into the policy digest and proof/public-input domain, and return at least `declared_tier`, `required_tier`, `tier_check` (`pass` or `fail`), and a machine-readable failure reason. A cryptographically valid proof with a failed tier check is not an accepted verification result.

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

The proposed initial operational roles are `operator` (redacted claim lifecycle) and `auditor` (read-only approved proof, policy-decision, and integrity metadata). Policy lifecycle adds the following roles:

| Role | Permitted responsibility | Prohibited combination or action |
| --- | --- | --- |
| `policy_author` | Draft immutable policy content and propose compatibility/effective windows. | Cannot approve, activate, publish as authoritative, revoke, or approve its own rollback. |
| `policy_issuer` | Attest organizational ownership and sign an exact policy digest for submission to approval. | Cannot self-approve unless an explicitly approved emergency governance profile requires and records it. |
| `policy_approver` | As the approval authority, approve, activate, deprecate, revoke, and authorize rollback for exact digests within delegated scope. | Cannot alter policy bytes, status history, or publication records; routine approval MUST be separate from author and publisher. |
| `policy_publisher` | Publish approved bytes, signed status events, checkpoints, and availability endpoints exactly as authorized. | Cannot create approval/status authority, rewrite history, or choose rollback targets. |
| `policy_verifier` | Resolve policy/status from configured trust anchors, validate signatures, freshness, compatibility, and windows, and issue a decision. | Cannot accept prover-selected trust anchors or override a failed/unknown state. |
| `policy_auditor` | Read and reconcile policy, approval, publication, cache, rollback, revocation, and decision evidence. | Has no authoring, status-changing, publication, or verification-override privilege. |

Production authorization MUST use least privilege, scoped issuer/approval delegations, multi-party approval for revocation and rollback where time permits, and recorded break-glass credentials for emergencies. Break-glass use MUST be time bounded, independently reviewed, and cannot bypass signed exact-digest decisions or append-only audit. Publisher, approver, and verifier credentials use separate keys and service identities; compromise of a transport or publication key does not grant policy approval. Authentication technology remains Open; selecting a token format is not authorization design. Logs and traces use opaque correlation IDs, avoid stable vehicle IDs, and are tested for restricted fields. The lifecycle semantics, trusted publication, outage behavior, and required decision evidence are normative in [data and proof model](data-and-proof-model.md#policy-lifecycle-and-verifier-trust).

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
- Authentication mechanism, role-assignment workflow, quorum/delegation rules, and break-glass custody.
- Public metadata allowlist, pseudonym rotation, retention, and incident contact/process.

These are tracked with evidence and due gates in [decisions](decisions.md); none should be inferred from candidate technology names. The assurance-tier registry and nullifier registry remain Proposed: freezing either requires an ADR and explicit product/privacy and security approval.

## Acceptance and related documents

Security acceptance requires threat review; negative, fuzz, replay, redaction, authorization, restart, rotation, and outage evidence; and explicit disposition of blocking risks at each [delivery gate](delivery-plan.md). The [data and proof model](data-and-proof-model.md) owns cryptographic semantics and [testing and operations](testing-and-operations.md) owns test execution/readiness.
