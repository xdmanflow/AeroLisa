# AeroLisa Trajectory Optimization

> Route-efficiency analysis on real flight tracks and wind-aware trajectory optimization using graph search (Dijkstra / A*) and dynamic programming on an airspace grid.

**Path:** `src/aerolisa/modules/trajectory` · **Target:** Stretch — Summer 2027

## Why

Fuel is one of an airline's largest costs. Even small route improvements matter at fleet scale.

## Role in AeroLisa

Stretch module. Step 1 measures route inefficiency; step 2 searches for better routes.

## Features

- Step 1: actual OpenSky track vs great-circle route → extra distance per city pair
- Step 2: airspace as a weighted grid (distance + wind), optimal path with A* / Dijkstra
- Comparison of optimized vs flown routes with clearly stated simplifications

## Stack

Python · NumPy · traffic · networkx (for comparison with own implementation)

## Data

- OpenSky ADS-B (see `aerolisa.modules.fleet`). Public wind data (source documented when chosen).

## Roadmap

- [ ] Route inefficiency analysis
- [ ] Grid + A* search
- [ ] Write-up of results and limits

## Definition of done

- [ ] Own A* implementation tested against networkx
- [ ] Limits of the simplified model written clearly

## Results

_Added at release._
