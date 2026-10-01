# ADR 0002: Ontology first

**Status:** accepted

**Context:** modules built on ad-hoc tables drift apart.

**Decision:** every module reads and writes objects defined in `aerolisa.core`.

**Consequences:** more design upfront (Dec. 2026), much less rework later; the planner and copilot can combine modules without special cases.
