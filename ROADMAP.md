# 🗺️ Roadmap

Rule: **cut scope, not dates.** A smaller release on time beats a bigger one late.

## v0.1: Foundation · target Jan. 17, 2027

- [ ] CLI published (Nov. 22, 2026)
- [ ] Ontology v0 designed on paper (Dec. 2026)
- [ ] `aerolisa.core`: objects, links, migrations
- [ ] C-MAPSS and Airbus O&D DAGs with quality checks
- [ ] Market analytics
- [ ] First Streamlit dashboard
- [ ] Everything runs with `sample_data/`

## v0.2: Engine health · target Mar. 7, 2027

- [ ] Features: RUL clipping, sliding windows, rolling statistics
- [ ] Naive baseline, Random Forest, XGBoost, time-based split
- [ ] Anomaly detection: z-scores, Isolation Forest
- [ ] Evaluation report comparing ≥ 3 models
- [ ] LSTM variant (Mar. 14)

## v0.3: Fleet & operations · target Apr. 18, 2027

- [ ] OpenSky flight segmentation and utilization metrics
- [ ] Eurocontrol delay analytics
- [ ] Planner v0: RUL × real cycles → ranked inspection list
- [ ] FastAPI ontology API
- [ ] Docker Compose stack, CI/CD, deployment on Google Cloud

## v1.0: Copilot · target May 16, 2027

- [ ] RAG over public maintenance documents, cited answers
- [ ] Agent with tools on the ontology API
- [ ] Evaluation question set
- [ ] Demo video + portfolio page

## Stretch: Trajectory · target Summer 2027

- [ ] Route inefficiency vs great-circle
- [ ] Wind-weighted grid + A* search
