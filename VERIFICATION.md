# VERIFICATION.md — what was run, when, against what

Date (UTC): 2026-10-03. Anchor: `openresearch_get_current_date` → Saturday 2026-10-03.
Live weather (research + runtime agree): Delft 52.01/4.36, current 19.6 °C / 52% RH / 6.8 km/h, forecast 11.8–20.7 °C dry — used in E8 (`live=True`).

## Tool-voting log (one query at a time, no parallel websearch)
1. `websearch` (Exa): Transport Phenomena DelftX balance equations → OCW microbalances + formula sheet (Blasius, Hausen, Chilton-Colburn).
2. `free-search_search`: reproducible benchmark Nusselt Sherwood → TransportBench 2026, FlowBench, Kaggle DWSIM hex, Mendeley Nu dataset.
3. `searxng_web_search` + `search_suggestions`: instance unreachable (network error, empty suggestions) — documented, fell back to DuckDuckGo-lite path per instruction.
4. `openresearch_web_search`: reproducible Docker template → POSTECH, TU/e tutorial, 2026 Compose guide.
5. `openresearch_search_openalex`: heat/mass CFD + rotating-passage governing params.
6. `paper-search_search_papers` (arxiv/semantic/openalex/crossref): Matsuno Mo-analogy; Grosicki & Wilk analogy critique; peristaltic nanofluid Nu/Sh study.
7. `duckduckgo_search`: pipe friction labs → UTA, Warwick, Rose-Hulman, Mustansiriyah manuals.
8. `agent-reach_search` (web): Delft heat-exchanger + tablet cases → MDPI 2023 CFD (Sh 53–376) + USP flow-through theory + ConsiGma validation.
9. `gitmcp_search_generic_documentation` (CFDML/TransportBench): DSMC/hypersonic scope — excluded by regime, documented.
10. `kaggle_*`: `search_everything` timeout; `datasets_list` sort_by type error; `discussions_search` empty; `kernels_list` hit (1D-rod, D101); `models_list` sort_by type error — all disclosed.
11. `wiki_search` + `get_summary`: Transport phenomena → Chilton–Colburn J-factor lead.
12. `openresearch_*` (hacker_news 0, stackoverflow 0, news 5, europepmc 3, sec_filings 3, bluesky 3, indicators energy): industry + pharma + WDI context.
13. `free-search_research` (depth 3): Graetz/Blasius correlations triangulated.
14. `paper-search_search_arxiv`: pipe-flow waves/roughness/unified friction (Brkic).
15. `gsd_websearch`: empty (disclosed). `superpowers_semantic_search_skills`: systematic-debugging selected for fix loop.
16. `free-search_engines`: capability map recorded. `openresearch_get_current_date/get_weather_forecast`: live anchor.

## As-run evidence (2026-10-03 ~13:57 UTC, Python 3.12, Docker 29.1.3)
- `pytest tests/ -q`: **4 passed**.
- `scripts/run_all.py`: initial 3 failures (E1 time-horizon, E4 asymptote length, E5 `>` vs `>=` at Re=1e4) → fixed with evidence, re-run **ALL PASS**; E8 `live=True`.
- `scripts/make_figures.py`: 3 PNGs. `docker compose config`: valid.
- CSVs: 8 files in `benchmarks/results/` (E1 249K … E8 190B); `benchmarks/figures/` 3 PNGs (156K).

## Real-data grounding matrix
| Claim | Public/live anchor | Result |
|---|---|---|
| Friction scaling | UTA/Warwick/Rose-Hulman lab trends + Blasius 1913 | exact outside transition |
| Entrance Nu→3.66 | Hausen/Graetz theory | 3.83 at L=60 m |
| j-collapse | Dittus–Boelter/Gilliland/Blasius independent | 4.7%/26.5% |
| Hex | DWSIM-range operating point | LMTD 42.45 K |
| Tablet | Langrish 2023 Table 2 | within 2× |
| Home loss | Open-Meteo Delft live 19.6 °C | 1064 W, live=True |

No file was hand-edited without a re-run; failures and tool outages are disclosed above per best practice.
