# ADR-0003: Layered licensing model for the open proof path

| Metadata | Value |
| --- | --- |
| Status | Proposed; adoption blocked by Open governance prerequisites |
| Accountable owner | Product owner |
| Required reviewers | Legal, community, architecture, dependency/security, and repository-maintainer representatives |
| Decision date | Open |
| Review trigger | Evidence for any licensing gate; path or contribution-policy change |
| Supersedes | Nothing; MIT remains effective |

## Context and business objective

The commercial model promises an independently usable open proof path, but MIT permits closed redistribution of modified core files. It therefore does not legally enforce the documented openness expectations for circuits, verifiers, schemas, local tooling, fixtures, and adapter-conformance material.

**Proposed business objective:**

> Align the repository’s enforceable licensing terms with its documented open-core and anti-lock-in model by keeping distributed modifications to the standard proof-path implementation open, while allowing proprietary operational services, enterprise integrations, control-plane features, and larger works that do not replace or redefine the open interoperability floor.

This statement supplies a proposal for review; repository evidence does not show that the accountable business owner has approved it.

## Proposed decision and scope

After, and only after, every gate below is evidenced, use MPL-2.0 for project-authored machine-oriented artifacts (software, workflows, scripts, build tooling, circuits, schemas, adapters, and reference prover/verifier tools), CC-BY-4.0 for narrative documentation, specifications, diagrams, governance, and explanatory material, and CC0-1.0 only for explicitly designated synthetic fixtures, golden vectors, conformance inputs, and expected outputs. Preserve third-party terms.

Require DCO 1.1 sign-off. Require no copyright assignment or CLA, commercial dual licensing, source-available restriction, non-commercial restriction, or field-of-use restriction. MPL file-level obligations would apply when covered files are distributed; hosted operation alone would not create AGPL-style source-disclosure obligations. Proprietary larger works, enterprise control planes, integrations, operational tooling, and managed services remain possible provided they do not replace or redefine the open interoperability floor.

Detailed existing-path and mixed/generated-content rules are in [`LICENSING.md`](../../LICENSING.md). The existing governance CSV classification and ownership/relicensing of all prior material remain Open.

## Alternatives considered

- **Retain MIT:** simplest and permissive, but does not require distributed core modifications to remain open and lacks an express contributor patent grant.
- **Apache-2.0:** adds express patent terms while remaining permissive, but does not provide file-level reciprocity.
- **MPL-2.0 (preferred proposal):** stronger reciprocity than MIT or Apache, with an express contributor patent grant and file-level copyleft suitable for verifier, circuit, schema, and interoperability files while permitting proprietary larger works.
- **EUPL-1.2:** European framing and reciprocity, but broader compatibility/communication implications require legal analysis and may make the intended boundary less predictable.
- **AGPL-3.0:** network copyleft is broader than the desired distributed-file boundary and would make hosted operation a disclosure trigger.
- **AGPL plus commercial dual licensing:** adds that broad trigger, copyright-control/assignment pressure, and a commercial exception model inconsistent with this proposal.
- **Source-available or non-commercial licensing:** restricts use, is not the intended open-source model, and conflicts with unrestricted commercial use around the open interoperability floor.

MPL is proposed because it combines stronger reciprocity than permissive alternatives with a less expansive boundary than AGPL (and the potentially broader EUPL analysis), keeps distributed modifications to core interoperability files open, and supports differentiation through operations, support, integration, proprietary larger works, and managed services.

## Benefits, costs, and implications

Expected benefits are file-level reciprocity for distributed modifications; MPL's express contributor patent grant; proprietary larger-work and managed-service compatibility; clearer documentation and data licensing; less friction copying synthetic vectors; and closer alignment of governance promises with downstream obligations.

Costs and risks are greater complexity; contributor and dependency review; possible resistance from permissive-only consumers; path/SPDX maintenance; relicensing limits for prior contributions; Romanian/EU legal confirmation; and ambiguity for generated or mixed-content files. DCO records provenance assertions but neither transfers copyright nor cures missing permissions. CC licenses' patent treatment differs from MPL's and needs legal review.

The open proof path and its proof-soundness/canonical-interpretation fixes remain a project governance commitment independently of whether a downstream legal duty applies. Publication remains separate from verification, and verifier output remains separate from relying-party business decisions.

## Governance evidence

| Required prerequisite | Evidence found | Status |
| --- | --- | --- |
| Separately stated business objective | The proposed objective above; no accountable approval record found | Proposed, not approved |
| Legal review | No review, reviewer, opinion, or Romanian/EU analysis found | Open, blocking |
| Community-impact analysis | Benefits/risks above are a review brief; no consultation, feedback, or accountable disposition found | Open, blocking |
| Dependency review | Initial inventory in the dependency policy; action pinning, provenance, compatibility, and future dependency review unresolved | Open, blocking |
| Accepted ADR | This ADR is Proposed and has no decision date or approvals | Open, blocking |

Repository history inspected through the baseline commit shows one contributor name using two email addresses. That observation cannot establish legal identity, ownership, employment assignment, imported-material provenance, or relicensing authority. Open GitHub pull-request and issue state could not be verified from the execution environment because remote access returned HTTP 403; reviewers must repeat that check before disposition. No evidence authorizes an effective transition.

## Dependency compatibility and historical MIT treatment

The repository contains no implementation manifests or vendored source. The Python checker is standard-library-only; two GitHub Actions are external dependencies requiring exact-version/license review. Future proof-system, cryptographic, MAVLink, CBOR, SDK, generated, and vendored choices remain unapproved under the [dependency policy](../dependency-licensing-policy.md).

Existing and earlier published content remains available under its applicable MIT grant. Adoption would not revoke those permissions or justify rewriting history. Before transition, the rights holder must establish ownership or permission file by file and resolve whether the existing copyright name is the exact legal holder. Anything not demonstrably relicensable remains MIT with an explicit mapping.

## Transition, validation, and supersession

After all gates close, one reviewed transition change must: record approvers/evidence and exact transition commit; change this status consistently with the register; add unmodified SPDX license texts; update the root entrypoint; apply reviewed SPDX/REUSE mappings without conflicts; enumerate MIT exceptions; verify contributor permissions and dependencies; and update release attribution/SBOM procedures. It must check links, recognized identifiers, status/README coherence, non-conflicting mappings, unchanged protocol identifiers, and absence of restricted data. CI supports consistency, not legal compliance.

If the proposal is rejected, supersede this ADR with the reason and retain MIT. If an adopted model must change, use a new ADR and prospective transition; preserve historical grants, notices, and third-party terms. Rollback never silently removes rights already granted.

## Affected documents

- `LICENSE` (unchanged and authoritative)
- `LICENSING.md`
- `CONTRIBUTING.md`
- `.github/pull_request_template.md`
- `README.md`
- `docs/README.md`
- `docs/commercial-model.md`
- `docs/dependency-licensing-policy.md`
- `docs/decisions.md`
- `scripts/check_docs.py`
