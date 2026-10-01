# AeroLisa Core

> Shared ontology and data-access library for AeroLisa: Aircraft, Engine, Flight, Airport and Delivery objects, database models, validation and configuration.

**Path:** `src/aerolisa/core` · **Target:** v0.1 — Jan 2027

## Why

In platforms like Palantir Foundry, the ontology maps raw tables to real-world objects (an aircraft, an engine, a flight) and their links. Getting this model right is what lets independent applications share the same truth.

## Role in AeroLisa

The contract between all modules. Every repo depends on it; modules never import each other and communicate only through the ontology.

## Features

- Object types: `Aircraft`, `Engine`, `Flight`, `Airport`, `Operator`, `Delivery`, `EngineSnapshot`
- Links: aircraft ↔ engines, aircraft ↔ flights, flight ↔ airports, delivery ↔ aircraft
- Pydantic schemas for validation + SQLAlchemy models for storage
- Shared config and database session helpers
- Versioned with semantic versioning; each module pins a release

## Stack

Python · Pydantic · SQLAlchemy · Alembic (migrations) · PostgreSQL · pytest

## Data

- No data. Schemas only.

## Roadmap

- [ ] Design ontology on paper (Dec 2026)
- [ ] v0.1: objects + links + migrations (Jan 2027)
- [ ] v0.2: EngineSnapshot for RUL outputs (Mar 2027)
- [ ] v0.3: Flight and Operator enrichment for fleet module (Apr 2027)

## Definition of done

- [ ] Every object has a definition, a schema and a test
- [ ] Migrations run from zero on an empty database
- [ ] Documented diagram in docs/ontology.md

## Results

_Added at release._
