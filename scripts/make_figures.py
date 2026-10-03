"""Generate benchmark figures (matplotlib, no seaborn)."""
import os, csv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

RES = os.path.join(os.path.dirname(__file__), "../benchmarks/results")
FIG = os.path.join(os.path.dirname(__file__), "../benchmarks/figures")
os.makedirs(FIG, exist_ok=True)

def load(name):
    with open(os.path.join(RES, name)) as f:
        r = list(csv.DictReader(f))
    return r

# F1 friction factor vs Re (log-log)
rows = load("e3_friction.csv")
Re = np.array([float(r["Re"]) for r in rows]); f = np.array([float(r["f_Fanning"]) for r in rows])
plt.figure(); plt.loglog(Re, f, "o-", ms=3); plt.loglog(Re[Re<2100], 16/Re[Re<2100], "k--", label="16/Re")
plt.xlabel("Re"); plt.ylabel("Fanning f"); plt.legend(); plt.grid(True, which="both", alpha=0.3)
plt.title("Friction: laminar 16/Re vs Blasius 0.079 Re^-1/4"); plt.savefig(f"{FIG}/f1_friction.png", dpi=150); plt.close()

# F2 Chilton-Colburn collapse
rows = load("e5_chilton_colburn.csv")
Re = np.array([float(r["Re"]) for r in rows])
plt.figure(); plt.loglog(Re, [float(r["f_over_2"]) for r in rows], "s-", label="f/2")
plt.loglog(Re, [float(r["jH"]) for r in rows], "o-", label="jH")
plt.loglog(Re, [float(r["jD"]) for r in rows], "^-", label="jD")
plt.xlabel("Re"); plt.ylabel("j / f/2"); plt.legend(); plt.grid(True, which="both", alpha=0.3)
plt.title("Hidden pattern: Chilton-Colburn collapse jH=jD=f/2"); plt.savefig(f"{FIG}/f2_chilton_colburn.png", dpi=150); plt.close()

# F3 Graetz entrance
rows = load("e4_graetz.csv")
L = np.array([float(r["L_m"]) for r in rows]); Nu = np.array([float(r["Nu_Hausen"]) for r in rows])
plt.figure(); plt.semilogx(L, Nu, "o-"); plt.axhline(3.66, color="k", ls="--", label="3.66 fully developed")
plt.xlabel("L [m]"); plt.ylabel("Nu Hausen"); plt.legend(); plt.grid(True, alpha=0.3)
plt.title("Graetz entrance: Nu(L) -> 3.66"); plt.savefig(f"{FIG}/f3_graetz.png", dpi=150); plt.close()

print("figures:", sorted(os.listdir(FIG)))
