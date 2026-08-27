# Commercial model

| Metadata | Value |
| --- | --- |
| Status | Proposed product and packaging policy |
| Audience | Product, community, engineering, security, partners, and customers |
| Accountable role | Product owner |
| Review trigger | Change to licensing, packaging, interoperability, hosted services, or edition compatibility |
| Authority | Normative for the boundary between independently usable community capabilities and optional commercial services |

## Purpose and commercial principle

The project uses an open-core model in which the complete standard proof path remains open, inspectable, and independently usable. Commercial value may be created by operating, integrating, governing, and supporting that path at organizational scale; it must not come from making a proprietary service necessary to understand, produce, or verify a standard proof.

“Open” in this document means available under the repository's open-source license, with sufficient source, schemas, documentation, and test material to use the capability without an account, network call, commercial credential, or managed control plane. Final license selection and any third-party-license constraints require an explicit decision before distribution.

## Capabilities that must remain open

The following form the portable interoperability floor and **MUST** remain open, versioned, documented, and independently usable:

- **Claim specifications:** the predicate, units, boundary behavior, public inputs, private witness, assurance semantics, time and replay fields, failure conditions, and version-identification rules for every standard claim.
- **Circuits and build inputs:** circuit source, constraints, reproducible build instructions, and the information required to associate circuit and proving-system versions with verification material. A standard claim must not depend on an undisclosed constraint or proprietary circuit variant.
- **Proof verification:** a local verifier and the verification keys or deterministic retrieval rules needed to validate supported standard proofs offline. Verification must expose explicit outcomes for malformed, unsupported, expired, policy-mismatched, and cryptographically invalid evidence.
- **Canonical encodings:** normative schemas, field ordering, integer widths, endianness, domain separators, hashing rules, normalization rules, and versioning behavior for claims, policies, public inputs, proofs, and verification results.
- **Synthetic fixtures and vectors:** non-sensitive positive, boundary, malformed, and negative examples sufficient to reproduce proof generation and verification and to detect incompatible encodings or circuit behavior.
- **Local CLI or SDK:** at least one maintained, scriptable implementation that can normalize supported synthetic inputs, create a standard proof, and verify it locally without a hosted account. Its interfaces must be adequate for CI and third-party integration, not merely a demonstration UI.
- **Adapter contract tests:** a reusable conformance suite for telemetry, policy, verifier, and publication adapters, including deterministic mock implementations. Third parties must be able to implement an adapter and establish compatibility without access to proprietary infrastructure.

These artifacts must be usable together as a complete local path. Publishing isolated source files while withholding required schemas, keys, build steps, fixtures, or test harnesses does not satisfy this boundary.

## Optional commercial capabilities

Commercial community support, self-hosted enterprise packages, and managed services may add capabilities that reduce operational burden or meet organizational requirements, including:

- hosted policy authoring, approval workflows, distribution, version history, and revocation management;
- tenant isolation, organization and project boundaries, quotas, delegated administration, and billing controls;
- managed verifier APIs, autoscaling, caching, rate limiting, health reporting, and authenticated batch processing;
- durable replay protection and coordinated nonce or nullifier state across processes, regions, and recovery events;
- identity-provider integration, including SSO, federation, directory synchronization, role mapping, and lifecycle automation;
- configurable audit exports and connectors for customer-controlled object stores, SIEM systems, compliance workflows, or evidence archives;
- regional deployment, data-residency controls, private networking, customer-managed keys, and managed disaster recovery;
- operational support, implementation assistance, upgrade planning, incident coordination, and validated deployment guidance; and
- measured service objectives for availability, latency, support response, recovery, retention, and capacity, backed by commercial terms where offered.

These features may be proprietary because they operate or administer the open proof path rather than redefine it. Their security, privacy, retention, and assurance claims must remain explicit. Service objectives are commitments of a particular offering, not properties of the proof protocol or defaults for the proposed MVP.

## Independence and anti-lock-in rules

Commercial packaging **MUST** preserve all of the following principles:

1. A relying party can verify any standard proof locally using open artifacts and public verification material; a managed API is a convenience, not an authority.
2. Standard proof validity cannot depend on a vendor account, license server, undisclosed allowlist, proprietary identity assertion, billing state, or successful connection to a hosted service.
3. Managed services may add authenticated envelopes, policy approvals, timestamps, replay decisions, audit records, or service attestations, but these must be separable from the underlying cryptographic verification result. The verifier must distinguish “proof valid” from “accepted by this service policy.”
4. Vendor-specific metadata must use namespaced, optional extensions. It must not change the meaning or canonical encoding of a standard field, and an implementation that does not understand it must still be able to verify the standard proof when safe to do so.
5. Verification keys, circuit identifiers, schemas, and compatibility data required for previously issued standard proofs must remain available under a documented lifecycle policy. Ending a hosted product must not make retained standard proofs unverifiable.
6. Customers can export standard proofs, public inputs, policies needed to interpret them, replay/audit state they are entitled to retain, and configuration in documented formats. Export must not require the destination verifier to use the managed edition.
7. No proprietary policy language may be the only way to express a standard claim. A managed policy may impose additional organizational acceptance rules, but the standard predicate and public inputs remain portable.
8. Security fixes that affect standard proof soundness, canonical interpretation, or conformance belong in the open artifacts. A paid tier must not be the only edition capable of correctly verifying a supported standard proof.

## Community and managed edition compatibility

The community implementation defines the interoperability floor; the claim specification and canonical test vectors, rather than either edition's incidental behavior, define the wire contract.

| Expectation | Required behavior |
| --- | --- |
| Standard proof portability | A standard proof produced by either edition verifies in every conformant verifier that supports its declared claim, circuit, encoding, and proving-system versions. |
| Managed production | Managed services produce the same standard proof envelope and canonical public inputs, except for explicitly namespaced optional metadata. |
| Community production | Managed verification accepts conformant community-produced proofs without requiring that they were created through a vendor account or hosted policy service. Organizational policy may reject them only with a distinct, explainable policy result. |
| Version negotiation | Both editions publish supported versions and return explicit unsupported-version errors. Silent reinterpretation, coercion, or downgrade is prohibited. |
| Conformance | Both editions run the same open fixtures and adapter contract tests for shared behavior. Managed-only tests may cover operations, isolation, or integrations but cannot replace shared conformance tests. |
| Release compatibility | Additive optional fields require documented handling; breaking canonical, claim, circuit, or adapter changes require a new version and migration guidance. |
| Deprecation | Deprecation announces affected versions, timelines, replacement paths, and verification-material retention. Managed services must not withdraw support earlier than their published commitments. |
| Result semantics | Cryptographic validity, claim/policy evaluation, freshness, replay, source-assurance, and service authorization remain separately identifiable so editions do not collapse different decisions into a generic success result. |

Feature parity is not required: managed editions may provide better scale, availability, administration, integrations, and support. Interoperability parity is required for every capability described as a standard claim or standard proof. Proprietary claim types must be labeled as extensions and must not be represented as community-standard compatible until their specifications, verification path, encodings, and conformance material meet the open boundary above.

## Governance and validation

A change that moves an existing open capability behind a commercial boundary, alters standard proof portability, or creates a managed-only dependency requires product, architecture, cryptography, and community review plus an accepted ADR. The review must include an offline verification demonstration, cross-edition conformance results, export/exit analysis, and an inventory of proprietary extensions.

Release acceptance requires testing both directions: community-produced proof to managed verifier, and managed-produced proof to community verifier. It also requires proving that the documented local CLI or SDK completes the standard fixture path with hosted endpoints disabled.

This model inherits the product boundaries in [product scope](product-scope.md), the proof semantics in [data and proof model](data-and-proof-model.md), component boundaries in [architecture](architecture.md), security controls in [security and privacy](security-and-privacy.md), and evidence requirements in [testing and operations](testing-and-operations.md). Where a commercial feature changes a normative protocol decision, the [decision register](decisions.md) records the accountable decision and migration consequences.
