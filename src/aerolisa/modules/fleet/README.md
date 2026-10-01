# AeroLisa Fleet Utilization

> Fleet utilization analytics from real ADS-B data (OpenSky Network): flight hours, cycles, rotations and airport patterns for A320- and A350-family aircraft.

**Path:** `src/aerolisa/modules/fleet` · **Target:** v0.3 — Apr 2027

## Why

Utilization (hours and cycles) is what wears aircraft and engines out. Knowing how hard each airframe is flown is the link between operations and maintenance.

## Role in AeroLisa

Turns raw ADS-B tracks into `Flight` objects and per-aircraft cycles. Those real cycles drive the simulated engine degradation in the planner.

## Features

- Flight segmentation: takeoff and landing detection from altitude and ground speed
- Great-circle and haversine distances; block-time estimates
- Cycles and hours per airframe, per operator, per week
- Rotation patterns and busiest city pairs
- Scales with PySpark / BigQuery

## Stack

Python · traffic (ADS-B library) · PySpark · BigQuery · pandas · Plotly

## Data

- OpenSky Network ADS-B data under OpenSky's terms of use (non-commercial research). Historical access requires an account. Raw data is never committed or redistributed.

## Roadmap

- [ ] PySpark practice on an OpenSky sample (Jan 2027)
- [ ] Segmentation + utilization metrics (Apr 2027)
- [ ] Release v0.3 with planner integration (Apr 2027)

## Definition of done

- [ ] Segmentation validated on hand-checked flights
- [ ] Cycles per airframe feed the planner

## Results

_Added at release._
