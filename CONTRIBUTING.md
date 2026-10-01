# Contributing

AeroLisa is a personal learning project, but it follows team conventions on purpose.

## Workflow
1. Open an issue (feature, bug or weekend task).
2. Branch from `main`: `feat/engine-health-baseline`, `fix/opensky-timezone`, `docs/ontology`.
3. Commit with [Conventional Commits](https://www.conventionalcommits.org): `feat(fleet): detect takeoffs from altitude`.
4. Open a pull request using the template; CI must be green before merging.
5. Tag releases `v0.1.0`, `v0.2.0`… and update `CHANGELOG.md`.

## Rules
- Modules in `src/aerolisa/modules/` import **only** `aerolisa.core`, never each other.
- Every feature ships with tests and runs on `sample_data/`.
- Notebooks are for exploration; reusable code moves to `src/`.
- No raw data, secrets or files over 1 MB in Git (pre-commit enforces it).
- First version of the code written without AI; AI is used for review.

## Setup
```bash
make install
pre-commit install
make test
```
