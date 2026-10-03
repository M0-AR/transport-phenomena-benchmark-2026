"""E2 microbalances: slab/cylinder/sphere conduction + Fick diffusion analogue."""
import os, csv
import numpy as np
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))
from tpbench.balances import conduction_slab, conduction_cylinder, conduction_sphere

OUT = os.path.join(os.path.dirname(__file__), "../benchmarks/results/e2_micro.csv")
x, T, q = conduction_slab(100, 20, 0.1, k=0.598)
r, Tc, qL = conduction_cylinder(100, 20, 0.05, 0.15)
rs, Ts, Q = conduction_sphere(100, 20, 0.05, 0.15)
# Fick analogue: same math, D_AB instead of alpha; flux N = -D dc/dx
D_AB, c0, c1, L = 1.21e-9, 3.4, 0.0, 0.0025
N_A = -D_AB*(c1-c0)/L
with open(OUT, "w", newline="") as f:
    w = csv.writer(f); w.writerow(["case", "flux_SI", "check"])
    w.writerow(["slab_q_Wm2", q, "Fourier linear"])
    w.writerow(["cyl_q_per_L_Wm", qL, "log profile"])
    w.writerow(["sph_Q_W", Q, "1/r profile"])
    w.writerow(["fick_N_kg_m2s", N_A, "benzoic acid"])
print(f"E2 slab q={q:.1f} W/m2 cyl q/L={qL:.1f} W/m sph Q={Q:.2f} W Fick N={N_A:.3e}")
# analytic checks
assert abs(q - 0.598*80/0.1) < 1e-6
assert Q > 0 and qL > 0
print("E2 PASS")
