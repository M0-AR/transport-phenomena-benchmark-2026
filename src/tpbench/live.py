"""Live-data helpers. No API keys. Cached with graceful offline fallback."""
import json, os, urllib.request

CACHE = os.path.join(os.path.dirname(__file__), "../../data/live_cache.json")

def fetch_open_meteo(lat=52.01, lon=4.36, timeout=20):
    url = (f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"
           "&current=temperature_2m,relative_humidity_2m,wind_speed_10m&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=UTC&forecast_days=3")
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return json.loads(r.read().decode())
    except Exception as e:
        if os.path.exists(CACHE):
            with open(CACHE) as f:
                return json.load(f)
        raise RuntimeError(f"live fetch failed and no cache: {e}")

def save_cache(payload):
    os.makedirs(os.path.dirname(CACHE), exist_ok=True)
    with open(CACHE, "w") as f:
        json.dump(payload, f, indent=2)
    return CACHE
