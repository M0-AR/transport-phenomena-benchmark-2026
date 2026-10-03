"""E1 macro balances: tank filling + heat-exchanger-precursor energy balance + momentum (pipe)."""
import os, csv
import numpy as np
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))
from tpbench.balances import macro_balance_step

OUT = os.path.join(os.path.dirname(__file__), "../benchmarks/results/e1_macro.csv")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

# Case A: water tank dM/dt = Fin - Fout ; Fin=2 kg/s, Fout=k*sqrt(h)
# Time constant ~ rho*A*sqrt(h)/k ~ 3000 s -> integrate to 20000 s to reach steady state
dt, t_end = 5.0, 20000.0
M, A_tank, rho = 500.0, 1.0, 998.0
rows = []
t = 0.0
while t <= t_end:
    h = M / (rho * A_tank)
    Fout = 0.8 * np.sqrt(max(h, 0))
    M = macro_balance_step(M, dt, 2.0, Fout)
    rows.append((t, M, h, Fout))
    t += dt
# steady-state check: Fin=Fout -> h_ss=(Fin/0.8)^2
h_ss = (2.0/0.8)**2
with open(OUT, "w", newline="") as f:
    w = csv.writer(f); w.writerow(["t_s", "M_kg", "h_m", "Fout_kg_s"])
    w.writerows(rows)
print(f"E1 tank steady h_ss analytic={h_ss:.3f} m, simulated h_end={rows[-1][2]:.3f} m")
print(f"E1 wrote {OUT} n={len(rows)}")
# pass criterion
assert abs(rows[-1][2]-h_ss)/h_ss < 0.05, "macro balance did not reach steady state"
print("E1 PASS")
