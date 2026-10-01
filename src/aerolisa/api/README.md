# Ontology API

> FastAPI layer exposing AeroLisa's ontology objects, module outputs and planner results.

**Path:** `src/aerolisa/api` · **Target:** v0.3 · Apr 2027

## Planned endpoints
- `GET /aircraft`, `GET /aircraft/{icao24}`
- `GET /engines/{engine_id}/snapshots`
- `GET /planner/ranking`
- `GET /operations/delays?airport=`
- `GET /market/deliveries`

Used by the dashboard and by the copilot's tools. Interactive docs at `/docs`.
