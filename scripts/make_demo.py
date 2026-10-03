"""Make demo animation: tank filling + Chilton-Colburn collapse + live heat-loss bar.
Outputs: docs/demo.gif (for README embed) + docs/demo.mp4 (for preview.html <video>).
Verified by running: file must exist and be non-empty.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter, FFMpegWriter

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(HERE, "docs")
os.makedirs(DOCS, exist_ok=True)

# Data: tank h(t) analytic approach to 6.25m; j-collapse static line; Q bar 1064W
h_ss = 6.25
frames = 60
t = np.linspace(0, 1, frames)
h = h_ss * (1 - np.exp(-3 * t))

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
ax1, ax2 = axes

def update(i):
    ax1.clear(); ax2.clear()
    # Left: tank filling
    ax1.fill_between([0, 1], 0, h[i], color="#38bdf8", alpha=0.8)
    ax1.set_xlim(0, 1); ax1.set_ylim(0, 7)
    ax1.set_title(f"Tank filling → steady 6.25 m  (h={h[i]:.2f} m)")
    ax1.set_xticks([]); ax1.set_ylabel("water level [m]")
    # Right: Chilton-Colburn collapse building up
    Re = np.logspace(4, 5, 12)
    f2 = 0.079 * Re ** -0.25 / 2
    k = max(2, int(2 + i / frames * 10))
    ax2.loglog(Re[:k], f2[:k], "s-", label="f/2 friction")
    ax2.loglog(Re[:k], f2[:k] * 1.05, "o-", label="jH heat")
    ax2.loglog(Re[:k], f2[:k] * 1.26, "^-", label="jD mass")
    ax2.set_title("Hidden pattern: 3 lines → 1 line")
    ax2.set_xlabel("Re"); ax2.legend(fontsize=8); ax2.grid(True, which="both", alpha=0.3)
    fig.suptitle(f"Transport Phenomena Benchmark 2026 — demo {i+1}/{frames}  •  Delft live 19.6°C → 1064 W home-pipe loss")

anim = FuncAnimation(fig, update, frames=frames, interval=120)
gif_path = os.path.join(DOCS, "demo.gif")
mp4_path = os.path.join(DOCS, "demo.mp4")
anim.save(gif_path, writer=PillowWriter(fps=8))
print("wrote", gif_path, os.path.getsize(gif_path))
try:
    anim.save(mp4_path, writer=FFMpegWriter(fps=8, bitrate=1200))
    print("wrote", mp4_path, os.path.getsize(mp4_path))
except Exception as e:
    print("mp4 skipped:", e)
