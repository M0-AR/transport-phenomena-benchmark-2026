# PAPER.md — Publishable draft scaffold (target: education + fluids journal)

## Title
A Minimal Reproducible Benchmark for Transport Phenomena: Macro/Micro Balances, Entrance Effects and the Chilton–Colburn Collapse, Grounded in Live Data

## Authors
[TBD — repo owner] + DelftX instructors cited as curriculum source (Mudde, Hamersma, Bera)

## Abstract
[Use README Abstract verbatim; 180 words.]

## 1. Introduction
Process industries (mech/chem/metallurgical, semiconductors, wind, pharma) all reduce to mass/momentum/energy transport (Delft programme rationale; World Bank energy-intensity + SEC heat-exchanger industry context).

## 2. Curriculum-to-code mapping
Table Delft module → experiment → analytic asymptote (README §1). Prerequisites stated.

## 3. Theory
General + micro balance; Fourier/Fick/Newton; Re/Pr/Sc/Nu/Sh/Gz/St/j/f_F; list correlations with validity windows (README §2).

## 4. Methods
Docker Compose harness; sequential multi-engine research protocol (engines listed, SearXNG outage + Kaggle endpoint errors disclosed); live-data policy (Open-Meteo runtime fetch, `live` flag); tolerances pre-registered (5% E1, exact E3, 0.3 E4, 30% E5, 2× E7).

## 5. Results
E1–E8 table with as-run numbers (README §5) + 3 figures. Emphasise hidden pattern §3 + three documented breakdowns.

## 6. Discussion
Why analogy holds for gases and fails for high-Sc/short-duct/special geometries (cite Grosicki & Wilk, Matsuno, Sohn). Pedagogical value: each experiment fails loudly outside its regime — ideal for teaching assumption-checking (Delft goal: "make the right assumptions").

## 7. Threats to validity
Constant properties; smooth walls; beaker-specific dissolution fit; steady live case; single live timestamp (repeat `verify_live.py` across seasons proposed).

## 8. Future work
Bayesian tablet-dissolution meta-analysis over EuropePMC 39 papers; non-Newtonian extension; transient home-loss with hourly Open-Meteo; TransportBench/FlowBench SciML comparison (out-of-regime noted).

## References
[Copy README §6; add DOIs on submission. Key: Blasius 1913; Hausen; Lévêque; Ranz & Marshall 1952; Chilton & Colburn 1934; Dittus & Boelter 1930; Churchill & Bernstein 1977; Langrish et al. 2023; TransportBench arXiv:2606.02997.]

## Checklists
- [ ] Register analysis plan before adding datasets
- [ ] Archive `benchmarks/results/*.csv` + `data/live_cache.json` to Zenodo
- [ ] Ethics: no human data; energy filings are public EDGAR
