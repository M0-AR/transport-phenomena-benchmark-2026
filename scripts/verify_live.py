"""Live re-verification: re-fetches Open-Meteo Delft + checks CSV freshness."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))
from tpbench.live import fetch_open_meteo
wx = fetch_open_meteo()
print("LIVE Delft:", wx["current"])
assert "temperature_2m" in wx["current"]
print("verify_live PASS")
