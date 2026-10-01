# Architecture

```mermaid
flowchart TB
    subgraph SRC[Public data sources]
        S1[NASA C-MAPSS]
        S2[OpenSky ADS-B]
        S3[Airbus orders and deliveries]
        S4[Eurocontrol]
    end
    SRC --> P[pipelines + Airflow DAGs<br/>raw to clean to curated, quality checks]
    P --> C[(core<br/>ontology on PostgreSQL)]
    C --> M1[engine_health]
    C --> M2[fleet]
    C --> M3[operations]
    C --> M4[market]
    C -.-> M5[trajectory - stretch]
    M1 --> PL[planner<br/>Fleet Maintenance Planner]
    M2 --> PL
    PL --> API[api - FastAPI]
    M3 --> API
    M4 --> API
    API --> D[dashboard - Streamlit]
    API --> CO[copilot<br/>RAG + agent]
```

## Layers
1. **Sources**: public datasets, downloaded at runtime.
2. **Pipelines** (`aerolisa.pipelines`, `dags/`): raw → clean → curated, idempotent tasks, a data-quality report per run.
3. **Ontology** (`aerolisa.core`): real-world objects and their links, stored in PostgreSQL. See [ontology.md](ontology.md).
4. **Modules** (`aerolisa.modules.*`): independent analytics, each reading and writing ontology objects.
5. **Applications**: planner, API, dashboard, copilot.
6. **Platform**: Docker Compose, CI/CD, MLflow, Google Cloud.

## Dependency rule
```text
core  ←  pipelines, modules  ←  planner, api  ←  dashboard, copilot
```
Arrows point to what a component may import. Anything else is a design error.

## Decisions
See [adr/](adr).
