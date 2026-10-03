"""Validated empirical correlations used across DelftX TP101x/TP102x.

Sources verified online (2026-10-03):
- Blasius 1913: f_F = 0.079 Re^-1/4, 4000<Re<1e5 (ScienceDirect Topics; Delft formula sheet)
- Laminar Fanning: f_F = 16/Re, Re<2100 (UTA/Warwick/Rose-Hulman lab manuals)
- Dittus-Boelter: Nu = 0.023 Re^0.8 Pr^n, n=0.4 heating / 0.3 cooling, Re>1e4
- Sieder-Tate: Nu = 0.027 Re^0.8 Pr^1/3 (mu/mu_s)^0.14 (viscosity correction)
- Seider-Tate / Hausen mean: Nu_m = 3.66 + (0.065 (D/L) Re Pr)/(1+0.04[(D/L)RePr]^{2/3}) (Graetz)
- Leveque (short L / high Sc): Sh = 1.615 (Gz)^{1/3}, Gz=(D/L)ReSc
- Ranz-Marshall (sphere/tablet): Sh = 2 + 0.6 Re^{1/2} Sc^{1/3}
- Chilton-Colburn: j_H = St_H Pr^{2/3} = f_F/2 ; j_D = St_D Sc^{2/3} = f_F/2
- Churchill-Bernstein (cylinder cross-flow) for live weather validation
- Stefan-Boltzmann grey: q = eps sigma (Ts^4 - Tsur^4)
"""
import numpy as np

SIGMA = 5.67e-8

def reynolds(rho, v, D, mu):
    return rho * v * D / mu

def prandtl(mu, cp, k):
    return mu * cp / k

def fanning_friction(Re):
    Re = np.asarray(Re, dtype=float)
    f = np.empty_like(Re, dtype=float)
    lam = Re < 2100
    turb = (Re >= 4000) & (Re <= 1e5)
    trans = ~(lam | turb)
    f[lam] = 16.0 / Re[lam]
    f[turb] = 0.079 * Re[turb] ** (-0.25)
    # linear blend in transition 2100-4000 (engineering interpolation, flagged)
    f[trans] = np.interp(Re[trans], [2100, 4000],
                          [16.0/2100, 0.079*4000**-0.25])
    return f

def darcy_friction(Re):
    return 4.0 * fanning_friction(Re)

def pressure_drop_fanning(f_F, L, D, rho, v):
    return 2.0 * f_F * (L / D) * rho * v**2  # = f_F * ... Delft sheet: dp = 4 f (L/D)(rho v^2/2)*... consistent

def nusselt_dittus_boelter(Re, Pr, heating=True):
    n = 0.4 if heating else 0.3
    Re = np.asarray(Re, dtype=float)
    return np.where(Re >= 1e4, 0.023 * Re**0.8 * np.asarray(Pr)**n, np.nan)

def nusselt_sieder_tate(Re, Pr, mu_bulk, mu_wall):
    return 0.027 * np.asarray(Re)**0.8 * np.asarray(Pr)**(1/3) * (np.asarray(mu_bulk)/np.asarray(mu_wall))**0.14

def nusselt_graetz_hausen(Re, Pr, D, L):
    """Hausen mean-Nu for laminar entrance (constant wall T). Limit -> 3.66."""
    Gz = (D / L) * np.asarray(Re) * np.asarray(Pr)
    return 3.66 + (0.065 * Gz) / (1.0 + 0.04 * Gz**(2/3))

def sherwood_leveque(Re, Sc, D, L):
    Gz = (D / L) * np.asarray(Re) * np.asarray(Sc)
    return 1.615 * Gz**(1/3)

def sherwood_gilliland(Re, Sc):
    """Turbulent analogue of Dittus-Boelter: Sh = 0.023 Re^0.83 Sc^0.44 (common form)."""
    return 0.023 * np.asarray(Re)**0.83 * np.asarray(Sc)**0.44

def sherwood_ranz_marshall(Re, Sc):
    return 2.0 + 0.6 * np.asarray(Re)**0.5 * np.asarray(Sc)**(1/3)

def chilton_colburn_jH(Re, Pr, f_F):
    St_H = nusselt_dittus_boelter(Re, Pr) / (np.asarray(Re)*np.asarray(Pr))
    return St_H * np.asarray(Pr)**(2/3), np.asarray(f_F)/2.0

def chilton_colburn_jD(Re, Sc, f_F, which="gilliland"):
    Sh = sherwood_gilliland(Re, Sc) if which == "gilliland" else sherwood_ranz_marshall(Re, Sc)
    St_D = Sh / (np.asarray(Re)*np.asarray(Sc))
    return St_D * np.asarray(Sc)**(2/3), np.asarray(f_F)/2.0

def churchill_bernstein(Re, Pr):
    Re = np.asarray(Re, dtype=float)
    return 0.3 + (0.62*np.sqrt(Re)*np.asarray(Pr)**(1/3)) / \
        ((1+(0.4/np.asarray(Pr))**(2/3))**0.25) * (1+(Re/282000)**(5/8))**(4/5)

def radiative_loss(eps, Ts_K, Tsur_K):
    return eps * SIGMA * (Ts_K**4 - Tsur_K**4)
