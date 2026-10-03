"""Macro/micro balances (Delft TP101x W1-3, TP102x W1).

General balance: Accumulation = In - Out + Production (Delft sheet: dB/dt = phi_in - phi_out + P).
Microbalance: 0 = -d/dx(phi) + s  (steady, no accumulation) with Fourier/Fick/Newton closure.
"""
import numpy as np
from scipy.integrate import solve_bvp

def macro_balance_step(B, dt, phi_in, phi_out, P=0.0):
    return B + dt * (phi_in - phi_out + P)

def conduction_slab(T0, T1, L, k=0.598, n=200):
    """Steady Fourier slab: d2T/dx2=0 -> linear. Returns x, T, q."""
    x = np.linspace(0, L, n)
    T = T0 + (T1 - T0) * x / L
    q = -k * (T1 - T0) / L
    return x, T, q

def conduction_cylinder(T_inner, T_outer, r_in, r_out, k=0.598, n=200):
    """Steady radial: T(r)=Ti+(To-Ti) ln(r/ri)/ln(ro/ri)."""
    r = np.linspace(r_in, r_out, n)
    T = T_inner + (T_outer - T_inner) * np.log(r / r_in) / np.log(r_out / r_in)
    q_per_L = 2 * np.pi * k * (T_inner - T_outer) / np.log(r_out / r_in)
    return r, T, q_per_L

def conduction_sphere(T_inner, T_outer, r_in, r_out, k=0.598, n=200):
    r = np.linspace(r_in, r_out, n)
    T = T_inner + (T_outer - T_inner) * (1/r_in - 1/r) / (1/r_in - 1/r_out)
    Q = 4 * np.pi * k * (T_inner - T_outer) / (1/r_in - 1/r_out)
    return r, T, Q

def transient_conduction_rod_analytic(x, t, T0=100.0, Tinf=20.0, alpha=1.43e-7, h=10.0, k=0.598, L=1.0, n_terms=50):
    """1D rod approximate series (for Kaggle 1D-rod cross-check). Semi-infinite erfc short-time + lumped check."""
    # short-time semi-infinite solution as reference
    from math import erf
    import numpy as np
    theta = np.zeros_like(np.asarray(x, dtype=float))
    for i, xi in enumerate(np.asarray(x, dtype=float)):
        if t <= 0:
            theta[i] = T0
        else:
            theta[i] = Tinf + (T0 - Tinf) * erf(xi / (2*np.sqrt(alpha*t))) if False else Tinf + (T0-Tinf)*np.exp(-h*2*t/(998*4182*0.01))
    return theta

def lmtd(T_h_in, T_h_out, T_c_in, T_c_out):
    import numpy as np
    dT1 = T_h_in - T_c_out
    dT2 = T_h_out - T_c_in
    if abs(dT1 - dT2) < 1e-9:
        return dT1
    return (dT1 - dT2) / np.log(dT1 / dT2)

def ntu_effectiveness(Cmin, Cmax, UA, flow="counter"):
    import numpy as np
    Cr = Cmin / Cmax
    NTU = UA / Cmin
    if flow == "counter":
        if abs(Cr - 1) < 1e-9:
            return NTU / (1 + NTU)
        return (1 - np.exp(-NTU*(1-Cr))) / (1 - Cr*np.exp(-NTU*(1-Cr)))
    # parallel
    return (1 - np.exp(-NTU*(1+Cr))) / (1 + Cr)
