"""E4 Graetz-Hausen heat + Leveque mass entrance: hidden L-dependence."""
import os, csv
import numpy as np, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))
from tpbench.correlations import nusselt_graetz_hausen, sherwood_leveque

OUT = os.path.join(os.path.dirname(__file__), "../benchmarks/results/e4_graetz.csv")
D = 0.02
Re, Pr, Sc = 1200.0, 7.01, 830.0
rows = []
for L in [0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 30.0, 60.0]:
    Nu = float(nusselt_graetz_hausen(Re, Pr, D, L))
    Sh = float(sherwood_leveque(Re, Sc, D, L))
    rows.append((L, (D/L)*Re*Pr, Nu, Sh))
with open(OUT, "w", newline="") as f:
    w = csv.writer(f); w.writerow(["L_m", "Gz_heat", "Nu_Hausen", "Sh_Leveque"])
    w.writerows(rows)
print("E4", rows)
# long-pipe limit -> 3.66 ; short-pipe -> entrance boost
assert abs(rows[-1][2]-3.66) < 0.3, "must asymptote to 3.66"
assert rows[0][2] > 8.0, "entrance must boost Nu"
print("E4 PASS: Nu 3.66 asymptote + entrance enhancement verified")
