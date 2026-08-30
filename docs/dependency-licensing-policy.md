# Dependency licensing policy

| Metadata | Value |
| --- | --- |
| Status | Current review policy; all implementation dependency choices remain Open |
| Audience | Contributors, architecture, security, release, and legal reviewers |
| Accountable role | Architecture lead |
| Review trigger | New, upgraded, generated, linked, vendored, or distributed third-party material |
| Authority | Normative dependency review gate; not an approval of any dependency |

## Policy

Before an implementation choice becomes Current, record the package, version, source, use/linkage and distribution mode, transitive tree, license and notices, known incompatibilities, and architecture, security, and legal disposition. Repository licensing never replaces third-party obligations.

- Common permissive licenses (for example MIT, BSD-2-Clause, BSD-3-Clause, ISC, Apache-2.0, and Zlib) are normally acceptable candidates after notice, patent, provenance, and compatibility checks.
- Weak-copyleft dependencies (including MPL, LGPL, and EPL families) require compatibility review of linking, modification, file/module boundaries, distribution, and source/notice duties.
- Strong or network-copyleft dependencies (including GPL and AGPL families, and EUPL where relevant obligations may extend through compatibility rules) require explicit architecture and legal review before selection.
- Source-available, non-commercial, field-of-use, ethical-use, and custom terms are review-required and prohibited by default unless a recorded decision explicitly approves the exact use. They must never be called open source merely because source is visible.
- Unknown, missing, or contradictory terms block use and distribution.

Proof-system and cryptographic libraries additionally require review of patent grants, parameter/setup provenance, export/security constraints, and generated verifier or key terms. MAVLink and CBOR libraries require dialect/schema/code-generator provenance and compatibility review. SDKs require review of bundled binaries, telemetry/network behavior, platform terms, and transitive packages. Generated code inherits no assumed license: preserve generator, template, input, output notices, and reproducible commands. Vendored artifacts require a recorded reason, exact source/version, checksums, license texts/notices, modification markers, update owner, and vulnerability process.

Releases containing dependencies must produce a machine-readable SBOM appropriate to the ecosystem and an attribution/notice bundle, with source-offer or relinking materials where required. CI should verify inventories against manifests and lockfiles when those exist; it cannot establish legal compliance.

## Current inventory and Open findings

The default-branch snapshot at `2b7133672c73f865787550faa993e77eb166b0cf` is documentation-only and has no package manifest, lockfile, vendored source, proof library, cryptographic library, MAVLink library, CBOR library, SDK, fixture corpus, or generated implementation. `scripts/check_docs.py` uses only the Python standard library. The documentation workflow invokes the externally maintained `actions/checkout@v4` and `actions/setup-python@v5`; their exact resolved revisions, transitive/action contents, licenses, and release-distribution relevance have not been recorded and remain **Open** for the transition dependency review.

No dependency is approved by this inventory. A complete dependency and imported-material review, including Git history/provenance, is an unmet prerequisite for ADR-0003.
