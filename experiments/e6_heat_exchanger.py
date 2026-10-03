"""E6 shell-and-tube heat exchanger (Delft chemical-industry case): LMTD + NTU."""
import os, csv, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))
from tpbench.balances import lmtd, ntu_effectiveness
OUT = os.path.join(os.path.dirname(__file__), "../benchmarks/results/e6_hex.csv")
# Hot oil 90->60 C, cold water 20->45 C, counter-flow; U=500 W/m2K, A=10 m2
Thi, Tho, Tci, Tco = 90, 60, 20, 45
L = lmtd(Thi, Tho, Tci, Tco)
Q_lmtd = 500*10*L
# NTU check: C_hot=2000 W/K, C_cold=4180 W/K
Cmin, Cmax = 2000, 4180
eps = ntu_effectiveness(Cmin, Cmax, 500*10)
Qmax = Cmin*(Thi-Tci)
Q_ntu = eps*Qmax
with open(OUT, "w", newline="") as f:
    import csv as c
    w = c.writer(f); w.writerow(["LMTD_K", "Q_LMTD_W", "eps_NTU", "Q_NTU_W"])
    w.writerow([L, Q_lmtd, eps, Q_ntu])
print(f"E6 LMTD={L:.2f} K Q={Q_lmtd/1000:.1f} kW eps={eps:.3f} Q_NTU={Q_ntu/1000:.1f} kW")
assert 30 < L < 45 and 0.5 < eps < 0.95
print("E6 PASS")
