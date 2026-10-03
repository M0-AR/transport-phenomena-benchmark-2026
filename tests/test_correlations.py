import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))
from tpbench.correlations import fanning_friction, nusselt_graetz_hausen, sherwood_ranz_marshall

def test_laminar():
    assert abs(float(fanning_friction(1000)) - 0.016) < 1e-9

def test_blasius():
    import numpy as np
    assert abs(float(fanning_friction(1e4)) - 0.079*1e4**-0.25) < 1e-12

def test_graetz_limit():
    assert abs(float(nusselt_graetz_hausen(1000, 7.0, 0.02, 50.0)) - 3.66) < 0.2

def test_ranz_marshall_stagnant():
    assert abs(float(sherwood_ranz_marshall(0, 600)) - 2.0) < 1e-9
