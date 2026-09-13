# Aircraft-TO Trajectory Optimization Project

**Optimizing flight trajectories for fuel efficiency and reduced climate impact, using classical optimal control and reinforcement learning — benchmarked against real-world flight data.**

---

## Repository Description

A research-grade project that models aircraft flight dynamics and computes optimized 4D trajectories (latitude, longitude, altitude, time) that minimize fuel burn and contrail formation. Two optimization approaches — direct collocation (classical optimal control) and reinforcement learning (PPO/SAC) — are implemented, compared against each other, and validated against real ADS-B flight trajectories from the OpenSky Network. Real ERA5 wind field data is integrated so optimized trajectories react to actual atmospheric conditions rather than idealized still air.

The project sits at the intersection of **aerospace engineering, optimal control, reinforcement learning, and data science**, and produces an interactive map comparing real flown routes to optimizer-suggested alternatives with estimated fuel and emissions savings.

---

## Keywords

`aircraft-trajectory-optimization` `optimal-control` `reinforcement-learning` `aerospace-engineering` `flight-dynamics` `fuel-efficiency` `contrail-avoidance` `climate-impact-aviation` `ADS-B` `OpenSky-Network` `ERA5-wind-data` `point-mass-model` `direct-collocation` `pseudospectral-optimal-control` `CasADi` `GEKKO` `PPO` `SAC` `stable-baselines3` `gym-environment` `4D-trajectory-planning` `air-traffic-management` `data-science` `machine-learning` `python`

---

## Project Overview

Commercial flight trajectories are rarely fuel-optimal — pilots and airlines follow standardized procedures and ATC-constrained routes that leave real fuel and emissions savings on the table. This project asks:

> **Given an aircraft's performance envelope, real wind conditions, and a real flown route, how much better could the trajectory be — and can a learned (RL) policy match a mathematically optimal (control theory) solution?**

The project is split into four stages:

1. **Flight dynamics modeling** — a physics-based point-mass model of aircraft performance (thrust, drag, fuel flow vs. altitude/speed/weight).
2. **Classical optimal control** — direct collocation to compute a provably near-optimal fuel-minimizing trajectory.
3. **Reinforcement learning** — a custom Gym environment where an RL agent learns to fly a fuel-efficient trajectory step by step.
4. **Validation & comparison** — benchmarking both methods against each other and against real historical flights.

---

## Why This Project Is Different

Most student ML projects stop at "train a model, report accuracy." This project instead:

- Grounds machine learning in **real physical constraints** (thrust limits, climb rates, fuel flow — not a toy environment).
- Uses **real-world data** (actual ADS-B flight tracks + real reanalysis wind fields), not synthetic or Kaggle-clean data.
- Compares a **rigorous mathematical baseline (optimal control)** against a **learned baseline (RL)** — a comparison rarely done at student level, since it requires competence in both fields.
- Targets a genuinely active 2023–2025 research problem: **contrail avoidance**, since contrails are estimated to account for roughly two-thirds of aviation's climate impact — more than CO2 emissions from burned fuel.
- Produces a **visual, demo-able result**: real flight vs. optimized flight, overlaid on an interactive map with quantified savings.

---

## Tech Stack

| Component | Tools |
|---|---|
| Flight dynamics model | Python, NumPy, custom point-mass BADA-like performance model |
| Classical optimization | CasADi or GEKKO (direct collocation / pseudospectral methods) |
| Reinforcement learning | Gymnasium (custom env), Stable-Baselines3 (PPO / SAC) |
| Real flight data | [OpenSky Network](https://opensky-network.org/) API |
| Wind/weather data | [ERA5 reanalysis](https://cds.climate.copernicus.eu/) (ECMWF) |
| Visualization | Plotly / deck.gl / Kepler.gl, Matplotlib |
| Analysis | Pandas, GeoPandas |

---

## Project Structure

```
aircraft-trajectory-optimization/
│
├── data/
│   ├── raw/                  # Downloaded ADS-B tracks, ERA5 wind grids
│   └── processed/            # Cleaned, resampled trajectory + wind data
│
├── dynamics/
│   ├── performance_model.py  # Point-mass aircraft dynamics (thrust, drag, fuel flow)
│   └── constraints.py        # Speed/altitude/climb-rate envelope limits
│
├── optimal_control/
│   ├── collocation.py        # Direct collocation formulation (CasADi/GEKKO)
│   └── solve_baseline.py     # Runs the classical solver on a chosen route
│
├── rl/
│   ├── trajectory_env.py     # Custom Gymnasium environment
│   ├── train.py               # PPO/SAC training script
│   └── evaluate.py           # Rollout + reward analysis
│
├── validation/
│   ├── compare_trajectories.py  # Real vs. classical vs. RL comparison
│   └── fuel_savings_report.py   # Computes estimated fuel/CO2 savings
│
├── visualization/
│   └── map_dashboard.py       # Interactive map of trajectories
│
├── notebooks/                 # Exploratory analysis, plots for the report
├── requirements.txt
└── README.md
```

---

## Getting Started

### 1. Clone and set up environment
```bash
git clone https://github.com/<your-username>/aircraft-trajectory-optimization.git
cd aircraft-trajectory-optimization
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Get data access
- Create a free account on [OpenSky Network](https://opensky-network.org/) for ADS-B trajectory data.
- Register with [Copernicus Climate Data Store](https://cds.climate.copernicus.eu/) for ERA5 wind data.
- Add credentials to a `.env` file (see `.env.example`).

### 3. Pick a route and pull real flight data
```bash
python data/fetch_opensky.py --route "LFPG-KJFK" --date 2025-03-01
```

### 4. Run the classical optimal control baseline
```bash
python optimal_control/solve_baseline.py --route LFPG-KJFK --objective fuel
```

### 5. Train the RL agent
```bash
python rl/train.py --route LFPG-KJFK --timesteps 500000
```

### 6. Compare and visualize
```bash
python validation/compare_trajectories.py --route LFPG-KJFK
python visualization/map_dashboard.py --route LFPG-KJFK
```

---

## Example Output (target deliverable)

- An interactive map showing: **actual flown trajectory** (blue), **optimal-control trajectory** (green), **RL-agent trajectory** (orange), overlaid on real wind vectors.
- A summary table: estimated fuel burn (kg), estimated CO2 (kg), estimated contrail-risk exposure (time spent in ice-supersaturated regions), for all three trajectories.
- A short report analyzing where RL matches/diverges from the optimal control baseline, and why.

---

## Roadmap / Stretch Goals

- [ ] Add multi-flight batch evaluation (not just one route)
- [ ] Incorporate contrail formation model (ISSR — ice-supersaturated region avoidance)
- [ ] Add ATC/airspace constraint zones to the optimization
- [ ] Wrap as a lightweight web demo (route picker → optimized trajectory)
- [ ] Extend to multi-aircraft conflict-free trajectory optimization

---

## Background & References

- Eurocontrol BADA (Base of Aircraft Data) — standard aircraft performance modeling
- OpenSky Network — [Schäfer et al., "Bringing Up OpenSky"](https://opensky-network.org/publications)
- Contrail climate impact research (e.g. Google Research / American Airlines contrail avoidance trials, 2023–2024)
- CasADi: [Andersson et al., "CasADi: a software framework for nonlinear optimization and optimal control"](https://web.casadi.org/publications/)
- Stable-Baselines3 documentation

---

## Author

Project — Aircraft Trajectory Optimization, developed as part of an AI & Data Science engineering specialization.

---

## 📄 License

MIT License (or specify your preferred license).
