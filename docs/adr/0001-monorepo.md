# ADR 0001: Monorepo

**Status:** accepted

**Context:** one developer, one ontology shared by every component.

**Decision:** a single repository, `aerolisa`, with one Python package and independent subpackages.

**Consequences:** one version, one CI, atomic changes across components. Independence is enforced by the import rule in `architecture.md` rather than by separate repositories.
