# AeroLisa Market Analytics

> Airbus orders, deliveries and backlog analytics from public monthly data: trends by family, customer region and year, with a simple delivery-rate forecast.

**Path:** `src/aerolisa/modules/market` · **Target:** v0.1 — Jan 2027

## Why

Production rate and backlog drive everything downstream: fleet growth, maintenance demand, spare parts. A good first module to prove the platform works end to end.

## Role in AeroLisa

Light analytics module. Reads `Delivery` objects from the ontology and publishes the Market page of the dashboard.

## Features

- Deliveries per month and per aircraft family
- Backlog evolution
- Simple, documented forecast of monthly delivery rate with its limits stated
- Charts exported for the dashboard

## Stack

Python · pandas · matplotlib / Plotly · statsmodels

## Data

- Public Airbus orders & deliveries figures (airbus.com). Not redistributed; fetched by `aerolisa.pipelines`.

## Roadmap

- [ ] v0.1: descriptive analytics + charts (Jan 2027)
- [ ] v0.2: forecast with backtest (spring 2027)

## Definition of done

- [ ] Runs standalone on sample data
- [ ] Every chart has a one-line takeaway

## Results

_Added at release._
