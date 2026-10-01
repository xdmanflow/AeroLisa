# Fleet Maintenance Planner

> Ranks engines to inspect first by combining predicted remaining useful life, anomaly scores and real aircraft utilization.

**Path:** `src/aerolisa/planner` · **Target:** v0.3 · Apr 2027

## How it works
1. C-MAPSS engines are assigned to real A320-family airframes from OpenSky (**simulated fleet, labelled as such**).
2. Each engine's degradation advances with its aircraft's real flight cycles (`aerolisa.modules.fleet`).
3. `aerolisa.modules.engine_health` produces RUL predictions and anomaly scores.
4. The planner ranks engines by risk and explains each ranking (which signals drove it).

## Definition of done
- [ ] Ranked list with an explanation per engine
- [ ] Visible in the dashboard and through the API
- [ ] 3-minute demo explains one decision end to end
