#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
plot_figs2_linewidth_comparison.py

Fully automated script to generate Fig. S2 (Supplementary Material):
Linewidth Γ(D) for the graphene-assisted device (η = 2.09) 
vs. illustrative metal-contact comparison.
"""

import numpy as np
import matplotlib.pyplot as plt

# Set publication style
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 0.8

def generate_figs2():
    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)

    # Dose array (kGy)
    D = np.linspace(-0.5, 10.0, 1000)
    D_model = np.clip(D, 0, None)
    D0 = 0.5  # Characteristic dose D0 = 500 Gy = 0.5 kGy
    
    # Saturation kinetics model: D / (D + D0)
    sat = D_model / (D_model + D0)

    # Linewidth curves matching Figure S2 values
    Gamma1_metal = 4.0 + 1.67 * sat
    Gamma2_metal = 7.0 + 2.16 * sat
    Gamma1_graph = 4.0 + 0.37 * sat
    Gamma2_graph = 7.0 + 0.22 * sat

    # Plot curves
    ax.plot(D, Gamma1_graph, '-', color='#1b4f72', lw=2, label=r'$\Gamma_1$, graphene ($\eta=2.09$)')
    ax.plot(D, Gamma2_graph, '--', color='#1b4f72', lw=2, label=r'$\Gamma_2$, graphene ($\eta=2.09$)')
    ax.plot(D, Gamma1_metal, '-', color='#e74c3c', lw=2, label=r'$\Gamma_1$, metal contact (illustrative)')
    ax.plot(D, Gamma2_metal, '--', color='#e74c3c', lw=2, label=r'$\Gamma_2$, metal contact (illustrative)')

    # Extended axis limits to give breathing room for text labels and legend
    ax.set_xlim(-0.8, 12.0)
    ax.set_ylim(3.0, 11.5)
    ax.grid(True, which='both', linestyle='--', alpha=0.4, color='#cccccc')

    # Labels and Title matching the manuscript style
    ax.set_xlabel(r'Accumulated dose $D$ (kGy)', fontsize=12, fontweight='bold')
    ax.set_ylabel(r'Linewidth $\Gamma$ (meV)', fontsize=12, fontweight='bold')
    ax.set_title(
        r'Figure S2. Linewidth $\Gamma(D)$: graphene-assisted device ($\eta=2.09$)' + '\n' + 
        r'vs. illustrative metal-contact comparison', 
        fontsize=12, fontweight='bold', pad=12
    )

    # Vertical reference line at D = 2 kGy
    ax.axvline(x=2.0, color='green', linestyle=':', lw=1.5)

    # Intersection markers at D = 2 kGy
    idx_2kgy = np.argmin(np.abs(D - 2.0))
    ax.plot(2.0, Gamma1_graph[idx_2kgy], marker='o', color='green', markersize=5)
    ax.plot(2.0, Gamma2_graph[idx_2kgy], marker='o', color='green', markersize=5)
    ax.plot(2.0, Gamma1_metal[idx_2kgy], marker='o', color='green', markersize=5)
    ax.plot(2.0, Gamma2_metal[idx_2kgy], marker='o', color='green', markersize=5)

    # Annotation for 80% saturation at D = 2 kGy
    ax.annotate(
        r'$D \approx 2$ kGy' + '\n' + r'$\approx 80\%$ of' + '\n' + r'asymptotic value',
        xy=(2.0, Gamma1_metal[idx_2kgy]), xytext=(3.2, 5.0),
        arrowprops=dict(facecolor='green', edgecolor='green', arrowstyle='->', lw=1.2),
        fontsize=10, fontweight='bold', color='green'
    )

    # Indicator for D0 = 500 Gy
    ax.axvline(x=0.0, color='grey', linestyle='-.', lw=1.2)
    ax.annotate(
        r'$D_0 = 500$ Gy', xy=(0.0, 3.5), xytext=(0.4, 3.3),
        arrowprops=dict(facecolor='grey', edgecolor='grey', arrowstyle='->', lw=1),
        fontsize=9, color='grey', fontweight='bold'
    )

    # Initial baseline value markers at D = 0
    ax.plot(0, 4.0, marker='o', markerfacecolor='none', markeredgecolor='#e74c3c', markersize=6, markeredgewidth=1.5)
    ax.text(-0.6, 3.8, '4.0', fontsize=10, fontweight='bold', color='#e74c3c')

    ax.plot(0, 7.0, marker='o', markerfacecolor='none', markeredgecolor='#e74c3c', markersize=6, markeredgewidth=1.5)
    ax.text(-0.6, 6.8, '7.0', fontsize=10, fontweight='bold', color='#e74c3c')

    # Asymptotic values at D = 10.8 with horizontal reference guides
    ax.text(10.8, 4.37, '4.37 meV', fontsize=9.5, fontweight='bold', color='#1b4f72', va='center')
    ax.text(10.8, 7.22, '7.22 meV', fontsize=9.5, fontweight='bold', color='#1b4f72', va='center')
    ax.text(10.8, 5.67, '5.67 meV', fontsize=9.5, fontweight='bold', color='#e74c3c', va='center')
    ax.text(10.8, 9.16, '9.16 meV', fontsize=9.5, fontweight='bold', color='#e74c3c', va='center')

    ax.axhline(y=4.37, color='#1b4f72', linestyle=':', lw=0.8, alpha=0.6)
    ax.axhline(y=7.22, color='#1b4f72', linestyle=':', lw=0.8, alpha=0.6)
    ax.axhline(y=5.67, color='#e74c3c', linestyle=':', lw=0.8, alpha=0.6)
    ax.axhline(y=9.16, color='#e74c3c', linestyle=':', lw=0.8, alpha=0.6)

    # Legend placed safely in the upper-right whitespace above curves
    ax.legend(loc='upper right', bbox_to_anchor=(0.99, 0.99), framealpha=0.9, fontsize=9.5)

    plt.tight_layout()
    
    # Save outputs in multiple publication-ready formats
    plt.savefig('Fig_S2_Linewidth_Comparison.png', dpi=300, bbox_inches='tight')
    plt.savefig('Fig_S2_Linewidth_Comparison.pdf', dpi=300, bbox_inches='tight')
    plt.savefig('Fig_S2_Linewidth_Comparison.svg', dpi=300, bbox_inches='tight')
    
    print("Fig. S2 updated successfully.")

if __name__ == '__main__':
    generate_figs2()