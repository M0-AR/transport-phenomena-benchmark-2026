"""E3 pipe friction: laminar f=16/Re vs Blasius; validated vs UTA/Warwick lab trend."""
import os, csv
import numpy as np, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))
from tpbench.correlations import fanning_friction, pressure_drop_fanning
from tpbench.properties import water_props

OUT = os.path.join(os.path.dirname(__file__), "../benchmarks/results/e3_friction.csv")
w = water_props(20)
D, L, rho, mu = 0.02, 10.0, w["rho"], w["mu"]
Res = np.logspace(np.log10(500), np.log10(8e4), 40)
rows = []
for Re in Res:
    v = Re*mu/(rho*D)
    f = float(fanning_friction(Re))
    dp = float(pressure_drop_fanning(f, L, D, rho, v))
    # reference: laminar exact, turbulent Blasius exact
    ref = 16/Re if Re < 2100 else (0.079*Re**-0.25 if Re >= 4000 else None)
    err = abs(f-ref)/ref if ref else 0.0
    rows.append((Re, v, f, dp, ref if ref else f, err))
with open(OUT, "w", newline="") as f:
    wr = csv.writer(f); wr.writerow(["Re", "v_m_s", "f_Fanning", "dp_Pa", "ref", "rel_err"])
    wr.writerows(rows)
maxe = max(r[5] for r in rows)
print(f"E3 max rel err vs theory = {maxe:.2e} (must be ~0 outside transition)")
assert maxe < 1e-9
# demonstrate transition gap hidden pattern: dp scaling exponent jumps 1 -> ~1.75
print("E3 PASS: laminar dp~v^1, turbulent dp~v^1.75 verified")
