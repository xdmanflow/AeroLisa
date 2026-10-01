# Aircraft Maintenance ETL Pipeline

> End-to-end ETL for aviation data (NASA C-MAPSS, Airbus orders & deliveries, OpenSky ADS-B, Eurocontrol): Airflow DAGs, PostgreSQL, data-quality checks, Docker. Project #1 of AeroLisa.

**Path:** `src/aerolisa/pipelines` · **Target:** v0.1 — Jan 2027 (Project #1)

## Why

Mirrors Airbus postings on ETL, data carve-out, transformation and loading for automation. Reliable, validated pipelines are the foundation of any fleet-data platform.

## Role in AeroLisa

**Project #1.** Owns all ingestion: one Airflow DAG per source, loading clean data into the ontology defined in `aerolisa.core`.

## Features

- DAG `cmapss`: download → validate → compute remaining-useful-life label → load
- DAG `airbus_orders_deliveries`: monthly refresh of public O&D figures
- DAG `opensky` (v0.3): A320/A350-family flight tracks → flights and cycles
- DAG `eurocontrol` (v0.3): delay and punctuality data
- Layers: raw → clean → curated; idempotent tasks; data-quality report per run

## Stack

Python · pandas · PostgreSQL · Apache Airflow · PySpark (for ADS-B volumes) · Docker · pytest

## Data

- **NASA C-MAPSS** turbofan degradation simulation (NASA Prognostics Center of Excellence). Downloaded at runtime, not committed.
- **Airbus orders & deliveries**: public monthly figures from airbus.com. Downloaded at runtime; raw files not redistributed.
- **OpenSky Network**: ADS-B data, used under OpenSky's terms (non-commercial research). Raw data not redistributed.
- **Eurocontrol** performance data (ansperformance.eu), used under its terms.

## Roadmap

- [ ] C-MAPSS DAG + quality checks (Jan 16–17, 2027)
- [ ] O&D DAG (Jan 2027)
- [ ] OpenSky DAG with PySpark (Apr 2027)
- [ ] Eurocontrol DAG (Apr 2027)

## Definition of done

- [ ] Runs end to end unattended
- [ ] Quality checks pass and produce a report
- [ ] Explainable in under 5 minutes with the architecture diagram

## Results

_Added at release._
