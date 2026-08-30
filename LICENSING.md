# Repository licensing policy

| Metadata | Value |
| --- | --- |
| Status | Current license record; layered transition Proposed and blocked by Open reviews |
| Audience | Users, contributors, release managers, and legal and dependency reviewers |
| Accountable role | Repository maintainer |
| Review trigger | License, path class, dependency, contribution, or distribution change |
| Authority | Human-readable path-classification authority; while the proposal is pending, the root `LICENSE` controls |

## Effective state and proposed target

**Current:** the root [`LICENSE`](LICENSE) is the authoritative grant and `MIT` remains the effective license for every project-authored file in this repository. Nothing in this policy, ADR-0003, or the commercial model changes that grant.

**Proposed, not legally approved or implemented:** after every governance gate in [ADR-0003](docs/adr/0003-layered-licensing-model-for-the-open-proof-path.md) is evidenced and the ADR is changed through review, project-authored artifacts would use:

| Existing or future artifact class | Proposed SPDX identifier |
| --- | --- |
| Machine-oriented artifacts, including `.github/workflows/**`, `scripts/**`, software, circuits, schemas, adapters, libraries, build tooling, and reference prover/verifier implementations | `MPL-2.0` |
| Narrative and governance material, including `README.md`, `CONTRIBUTING.md`, `LICENSING.md`, and `docs/**/*.md` | `CC-BY-4.0` |
| Only fixtures, golden vectors, conformance inputs, and expected outputs explicitly designated synthetic and non-sensitive | `CC0-1.0` |
| Vendored or third-party material | Its original license, notice, and attribution |

The existing CSV coordination register is governance data rather than an explicitly designated synthetic fixture; its transition classification is **Open** because tabular/mixed-content treatment needs legal review. `LICENSE` itself remains the applicable license text/notice rather than being reclassified. The repository currently contains no implementation, circuit, schema, proof vector, fixture corpus, or vendored source. Future classes above are assignment rules, not claims that those paths exist.

No MPL, CC BY, or CC0 license text or SPDX assignment is added while the gate is incomplete. On approval, canonical, unmodified texts would be added under `LICENSES/`, and maintainers would apply SPDX headers to practical machine-oriented files plus `.reuse/dep5` declarations where headers are disruptive. Those changes must be reviewed as one transition commit.

## Classification rules

To identify a file's license, check in order: (1) an explicit SPDX header or adjacent notice, (2) a future `.reuse/dep5` mapping, (3) a preserved third-party notice, and (4) this policy and the root `LICENSE`. Today step (4) resolves all project-authored files to MIT.

- **Mixed-content files:** classify by the file's primary function only after review. Separately licensed embedded material must be clearly delimited and attributed; split files where practical. A Markdown specification containing machine-readable examples does not make those examples CC0 automatically.
- **Generated files:** carry the generator's stated output terms and provenance where those terms apply; otherwise assign deliberately based on output purpose. Record the generator and inputs. Generated does not mean copyright-free.
- **Synthetic data:** CC0 would apply only to a path or file expressly marked synthetic after privacy and provenance review. Never infer CC0 from a `test`, `fixture`, or `example` name.
- **Third-party and vendored content:** preserve upstream terms, notices, source offers, and modification notices. Project licensing never overrides them. Do not vendor material until provenance and compatibility are recorded.
- **Dependencies:** remain governed by their own terms and the [dependency licensing policy](docs/dependency-licensing-policy.md). Linking or installation does not relicense a dependency.
- **New path classes and exceptions:** the maintainer proposes a mapping in this file and the mechanical SPDX mapping together. Exceptions must name the affected paths, original and intended terms, provenance, compatibility analysis, and reviewers; silent exceptions are prohibited.

## Contributions, patents, and history

Contributions require DCO 1.1 sign-off under [`CONTRIBUTING.md`](CONTRIBUTING.md). Sign-off is not a copyright assignment. Contributions are submitted under the effective license applicable to the destination at the time of contribution; while this proposal is pending, that is MIT unless an explicit third-party notice controls. No CLA, commercial dual-license grant, source-available restriction, non-commercial restriction, or field-of-use restriction is adopted here.

MIT has no express patent-license clause. The proposed MPL-2.0 classification would provide its express contributor patent grant for MPL-covered contributions; the scope and consequences require legal review. CC BY 4.0 and CC0 1.0 have different patent treatment and must not be described as equivalent.

Earlier published commits and copies retain the MIT permissions granted for those versions; a later transition cannot revoke them. History will not be rewritten merely to alter notices. The commit history currently shows one contributor name with two email addresses, but that does not establish copyright ownership, authority to relicense, or whether any material was imported. Permission/provenance for every affected file and whether `Romanian Cyber Space Initiative` is the exact legal rights holder rather than a project or trade name are **Open**. Until resolved, all affected material stays MIT.

## Trademark, naming, and conformance

Copyright licensing does not grant a right to imply endorsement or official status. Forks may state factual origin, but may not claim official conformance unless they pass the maintained conformance suite under its then-current rules. This is not a claim that a certification suite currently exists.

Protocol identifiers and canonical formats remain controlled by their versioning and compatibility rules. The repository rename does not authorize changing existing media types or other compatibility identifiers. Any certification mark or commercial product brand requires a separate decision. This policy claims no registered trademark right.
