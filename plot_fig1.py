#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
plot_figs1_resonance_profiles.py

Fully automated script to generate Fig. S1 (Supplementary Material):
Analytical Lorentzian resonance-line profiles illustrating the calculated 
resonance shifts and linewidth broadening predicted by the model at D = 1 MGy 
for different h-BN spacer thicknesses: (a) 0.5 nm, (b) 1.0 nm, (c) 2.0 nm, (d) 3.0 nm.

Derived from the analytical model equations using manuscript parameters 
together with the model calibration constant Q_MAX.
"""

import numpy as np
import matplotlib.pyplot as plt

# Set publication style
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 0.8

# Visualization parameters (strictly decoupled from the analytical model)
VIS_A1 = 0.6
VIS_A2 = 0.4
VIS_BACKGROUND = 0.01

def two_lorentzian_profile(E, E1, gamma1, E2, gamma2, A1=VIS_A1, A2=VIS_A2, background=VIS_BACKGROUND):
    """
    Returns an analytical two-Lorentzian profile constructed from 
    the resonance energies and linewidths predicted by the analytical model.
    
    Note: Peak amplitudes (A1, A2) and background are visualization parameters only.
    Individual resonances are represented as independent Lorentzian contributions 
    without coherent interference. Peak amplitudes are intentionally kept constant 
    to isolate the effects of resonance shifts and linewidth broadening predicted by the model.
    """
    L1 = (gamma1 / 2)**2 / ((E - E1)**2 + (gamma1 / 2)**2)
    L2 = (gamma2 / 2)**2 / ((E - E2)**2 + (gamma2 / 2)**2)
    profile = background + A1 * L1 + A2 * L2
    return profile

def generate_figs1():
    # ==========================================
    # 1. Core Model Parameters (Strictly from Manuscript)
    # ==========================================
    D = 1e6                 # Accumulated absorbed dose (Gy) = 1 MGy
    D0 = 500.0              # Characteristic saturation dose (Gy)
    
    # Q_MAX was calibrated once using the reference device and then kept
    # fixed for all calculations reported in Figs. 4, 5, and S1.
    # Q_MAX is an analytical calibration constant defining the normalization
    # of the effective trapped-charge variable rather than a directly 
    # measurable physical quantity.
    Q_MAX = 550.0           
    
    # Manuscript-defined energy-shift coefficients (alpha_i)
    alpha1 = 0.14           # meV per unit effective charge
    alpha2 = 0.06           # proportional second resonance coefficient
    
    # Manuscript-defined linewidth coefficients linked strictly via beta_i = 0.1 * alpha_i
    beta1 = 0.1 * alpha1    # = 0.014
    beta2 = 0.1 * alpha2    # = 0.006
    
    # Initial DWELL resonance parameters (D = 0)
    E1_0 = 82.0             # meV
    E2_0 = 126.0            # meV
    gamma1_0 = 4.0          # meV
    gamma2_0 = 7.0          # meV
    
    # Quantum capacitance and reference device mapping:
    # td = 1 nm, eta = 2.09
    C_Q = 0.72              # fF
    td_ref = 1.0            # nm (reference spacer thickness)
    eta_ref = 2.09          # reference eta value at td_ref
    C_geo_ref = C_Q / eta_ref  # reference geometric capacitance
    
    thicknesses = [0.5, 1.0, 2.0, 3.0]  # nm
    
    # Setup figure grid (2x2)
    fig, axes = plt.subplots(2, 2, figsize=(12, 9.5), dpi=300)
    axes = axes.flatten()
    
    E_grid = np.linspace(40, 165, 1000)
    
    for idx, td in enumerate(thicknesses):
        ax = axes[idx]
        
        # ==========================================
        # 2. Analytical Calculations
        # ==========================================
        # Geometric capacitance scales inversely with spacer thickness: C_geo proportional to 1/td
        C_geo = C_geo_ref * (td_ref / td)
        eta = C_Q / C_geo
        
        # Electrostatic screening in the analytical capacitance-divider approximation: S = eta / (1 + eta)
        S = eta / (1.0 + eta)
        
        # Explicit charge kinetics reflecting manuscript definitions:
        # Within the capacitance-divider approximation:
        # Q_tr = Q_MAX * [D / (D + D0)]
        # Q_screen = S * Q_tr
        # Q_eff = Q_tr - Q_screen = Q_tr * (1 - S)
        Q_tr = Q_MAX * (D / (D + D0))
        Q_screen = S * Q_tr
        Q_eff = Q_tr - Q_screen  # equivalently Q_tr * (1.0 - S)
        
        # Resonance shifts calculated from the analytical model equations: Delta E_i = alpha_i * Q_eff
        delta_E1 = alpha1 * Q_eff
        delta_E2 = alpha2 * Q_eff
        
        # Shifted resonance energies
        E1_1 = E1_0 - delta_E1
        E2_1 = E2_0 - delta_E2
        
        # Linewidth broadening calculated from the analytical model: Gamma_i = Gamma_0i + beta_i * Q_eff
        gamma1_1MV = gamma1_0 + beta1 * Q_eff
        gamma2_1MV = gamma2_0 + beta2 * Q_eff
        
        # Analytical profile before irradiation (D = 0 MGy)
        profile_0 = two_lorentzian_profile(E_grid, E1_0, gamma1_0, E2_0, gamma2_0)
        
        # Analytical profile after irradiation (D = 1 MGy)
        profile_1 = two_lorentzian_profile(E_grid, E1_1, gamma1_1MV, E2_1, gamma2_1MV)
        
        # Plot curves
        ax.semilogy(E_grid, profile_0, '--', color='#1b4f72', label='Before irradiation', lw=1.8)
        ax.semilogy(E_grid, profile_1, '-', color='#c0392b', label='After 1 MGy', lw=1.8)
        
        # Axis settings
        ax.set_xlim(40, 170)
        ax.set_ylim(1e-3, 1.2)
        ax.grid(True, which='both', linestyle='--', alpha=0.4, color='#cccccc')
        
        # Panel title using strict mathematical LaTeX formatting matching the article style
        panel_letter = chr(97 + idx) # a, b, c, d
        ax.set_title(
            rf'({panel_letter})  $t_d = {td:.1f}\,\mathrm{{nm}}$  ($\eta = {eta:.2f}$)',
            fontsize=10.5, fontweight='bold', pad=8, loc='left'
        )
        
        ax.set_xlabel(r'Energy $E$ (meV)', fontsize=9.5, fontweight='bold')
        ax.set_ylabel(r'Relative profile (a.u.)', fontsize=9.5, fontweight='bold')
        
        # Unified vertical height for Delta E arrow across all panels
        arrow_y = 0.45
        ax.annotate('', xy=(E1_1, arrow_y), xytext=(E1_0, arrow_y),
                    arrowprops=dict(facecolor='#c0392b', edgecolor='#c0392b', arrowstyle='<->', lw=1.5))
        
        # Exact calculated shift annotation placed safely inside the panel via relative axes coordinates
        delta_E1_measured = E1_0 - E1_1
        ax.text(
            0.05, 0.82,
            rf'$\Delta E_1 = {delta_E1_measured:.1f}\,\mathrm{{meV}}$',
            transform=ax.transAxes,
            fontsize=9,
            fontweight='bold',
            color='#c0392b',
            bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=2)
        )
        
        ax.legend(loc='lower right', framealpha=0.9, fontsize=9)

    plt.tight_layout()
    
    # Save outputs in multiple formats
    plt.savefig('Fig_S1_Resonance_Profiles.png', dpi=300, bbox_inches='tight')
    plt.savefig('Fig_S1_Resonance_Profiles.pdf', bbox_inches='tight')
    plt.savefig('Fig_S1_Resonance_Profiles.svg', bbox_inches='tight')
    
    print("Fig. S1 generated from the analytical model using manuscript parameters and the calibration constant Q_MAX.")

if __name__ == '__main__':
    generate_figs1()
