"""Thermophysical properties (water, air, benzoic-acid/water). SI units."""
import numpy as np

WATER_20C = {"rho": 998.2, "mu": 1.002e-3, "k": 0.598, "cp": 4182.0, "Pr": 7.01}
AIR_20C = {"rho": 1.204, "mu": 1.81e-5, "k": 0.0259, "cp": 1007.0, "Pr": 0.713}
# Benzoic acid in water (Langrish et al. / Irandoust & Andersson, MDPI Processes 2023, 11:505)
BENZOIC_WATER_25C = {"D_AB": 1.21e-9, "Cs": 3.4e-3 * 1000.0 / 1000.0,  # ~3.4 g/L saturation
                     "Cs_kg_m3": 3.4, "Sc": 830.0}

def water_props(T_C: float = 20.0):
    """Linearised water properties around 20 C (sufficient for benchmark)."""
    dT = T_C - 20.0
    return {
        "rho": 998.2 - 0.2 * dT,
        "mu": 1.002e-3 * np.exp(-0.024 * dT),
        "k": 0.598 + 0.0012 * dT,
        "cp": 4182.0,
        "Pr": max(1.0, 7.01 - 0.15 * dT),
    }

def air_props(T_C: float = 20.0):
    dT = T_C - 20.0
    return {
        "rho": 1.204 * 293.15 / (273.15 + T_C),
        "mu": 1.81e-5 + 5e-8 * dT,
        "k": 0.0259 + 7e-5 * dT,
        "cp": 1007.0,
        "Pr": 0.713,
    }
