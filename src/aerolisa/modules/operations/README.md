# AeroLisa Operations Performance

> European air-traffic operational performance from Eurocontrol data: delays by cause, airport and season, with SQL analytics and visual reports.

**Path:** `src/aerolisa/modules/operations` · **Target:** v0.3 — Apr 2027

## Why

Delays cost airlines money and ripple through the network. Understanding where and why they happen is the operational side of fleet performance.

## Role in AeroLisa

Operations page of the dashboard. Also the practice dataset used for the SQL weekends of the learning plan.

## Features

- Delay minutes by cause, airport, month and season
- Window functions: rolling averages, rankings, year-over-year
- Top recurring bottlenecks
- Report pages for the dashboard

## Stack

SQL (PostgreSQL) · Python · pandas · Plotly

## Data

- Eurocontrol performance data (ansperformance.eu), used under its terms.

## Roadmap

- [ ] SQL practice queries (Nov–Dec 2026)
- [ ] Packaged module + dashboard page (Apr 2027)

## Definition of done

- [ ] Every query documented with the question it answers
- [ ] Runs standalone on sample data

## Results

_Added at release._
