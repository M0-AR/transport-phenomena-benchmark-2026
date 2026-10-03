"""Run full benchmark suite E1-E8. Exit non-zero on any failure."""
import subprocess, sys, os
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
exps = [f"e{i}_{n}.py" for i, n in [
    (1, "macro_balances"), (2, "microbalances"), (3, "pipe_friction"),
    (4, "graetz_leveque"), (5, "chilton_colburn"), (6, "heat_exchanger"),
    (7, "tablet_dissolution"), (8, "live_weather")]]
fail = 0
for e in exps:
    p = os.path.join(HERE, "experiments", e)
    print("="*70); print("RUN", e)
    r = subprocess.run([sys.executable, p])
    if r.returncode != 0:
        print("FAIL", e); fail += 1
print("="*70)
print("ALL PASS" if fail == 0 else f"{fail} FAILURES")
sys.exit(fail)
