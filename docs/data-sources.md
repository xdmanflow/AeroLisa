# Data sources

| Source | Content | Access | Terms | Committed? |
|---|---|---|---|---|
| NASA C-MAPSS | Simulated turbofan run-to-failure data (FD001–FD004) | NASA Prognostics Center of Excellence data repository | Public dataset | No, downloaded at runtime |
| OpenSky Network | ADS-B state vectors and flights | REST API; historical database with an approved account | Non-commercial research use; check current terms | No, never redistributed |
| Airbus orders & deliveries | Monthly public figures | airbus.com | Airbus site terms | No, downloaded at runtime |
| Eurocontrol | Delays and operational performance | ansperformance.eu | Site terms | No, downloaded at runtime |
| Maintenance documents | Public manuals, FAQs, regulatory texts | Listed in `src/aerolisa/copilot/corpus_sources.md` | Per document | Only if the licence allows |

`sample_data/` contains tiny extracts or synthetic data so that tests and demos run offline.
