# AeroLisa CLI

> Command-line tool to register data sources, manage configurations and track runs of AeroLisa. Mini-project #0: Python OOP, JSON persistence, tests, packaging.

**Path:** `src/aerolisa/cli` · **Target:** v0.1 — Nov 2026 (Mini-project #0)

## Why

Before building pipelines, a platform needs a clean way to declare what data exists, where it comes from and when it was last refreshed.

## Role in AeroLisa

First brick of AeroLisa and mini-project #0 of the learning plan. Later becomes the command-line entry point of the platform.

## Features

- `renaissance source add|list|remove` — manage a catalog of data sources
- `renaissance status` — show last refresh and health of each source
- JSON persistence of the catalog, validated on load
- Classes with clear responsibilities (SOLID), full pytest suite
- Installable with `pip install .` (pyproject.toml)

## Stack

Python (standard library: argparse, json, pathlib, dataclasses) · pytest · GitHub Actions

## Data

- No data. Stores only a local catalog file.

## Roadmap

- [ ] v0.1: catalog CRUD + JSON + tests (Nov 22, 2026)
- [ ] v0.2: `status` reads run history from the platform database (Jan 2027)

## Definition of done

- [ ] All commands tested
- [ ] CI green on every push
- [ ] README shows a 30-second usage example

## Results

_Added at release._
