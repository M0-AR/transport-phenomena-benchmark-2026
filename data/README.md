# Data sources (all public; no keys)

- `live_cache.json` — Open-Meteo Delft snapshot (auto-written by E8). Refresh: `python3 scripts/verify_live.py`.
- Public anchors (fetched during research, not vendored for licence hygiene):
  - Kaggle `kuriangeorge/heat-exchanger-dataset-parametric-study` (DWSIM shell-and-tube parametric).
  - Mendeley `xss4btn4v7` (Nu vs velocity analogue).
  - UTA / Warwick / Rose-Hulman pipe-friction lab manuals (trend validation for E3).
  - Langrish et al. MDPI Processes 2023 11:505 Table 2 (E7 anchors hard-coded with citation).
  - World Bank WDI `EG.EGY.PRIM.PP.KD` etc.; SEC EDGAR THT Heat Transfer 8-K / SmartHeat 424B3 (industry context).
- Regenerating everything needs only internet for E8; all else is closed-form.
