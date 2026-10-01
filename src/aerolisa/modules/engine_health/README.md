# Predictive Maintenance & Anomaly Detection

> Remaining-useful-life prediction and anomaly detection for turbofan engines on NASA C-MAPSS: baseline vs Random Forest vs XGBoost vs LSTM, evaluated and packaged. Project #2 of AeroLisa.

**Path:** `src/aerolisa/modules/engine_health` · **Target:** v0.2 — Mar 2027 (Project #2)

## Why

Mirrors the Defence & Space posting on time-series anomaly detection. Predicting failures before they happen avoids unscheduled removals and aircraft on ground, the core promise of predictive maintenance.

## Role in AeroLisa

**Project #2.** Produces an `EngineSnapshot` (predicted RUL, anomaly score, explanation) for each engine; the planner ranks inspections from it.

## Features

- Naive baseline, then Random Forest, XGBoost and an LSTM
- RUL target clipping (piecewise-linear label), sliding windows, rolling features
- Anomaly detection: z-scores, Isolation Forest, autoencoder
- Time-based split (no shuffling), RMSE / MAE / NASA scoring function, precision / recall / F1 for alerts
- Packaged model + MLflow experiment tracking

## Stack

Python · scikit-learn · XGBoost · PyTorch · MLflow · pandas · matplotlib

## Data

- NASA C-MAPSS (FD001–FD004), optionally PHM08. Downloaded at runtime.

## Roadmap

- [ ] Baseline + features (Feb 20–21, 2027)
- [ ] RF / XGBoost + anomaly detection (Feb 27–28)
- [ ] Evaluation report, release v0.2 (Mar 6–7)
- [ ] LSTM variant (Mar 13–14)

## Definition of done

- [ ] Beats the naive baseline with documented precision / recall / F1
- [ ] Fully reproducible from a clean clone
- [ ] Comparison table of ≥ 3 models

## Results

_Added at release._
