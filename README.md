# Supplementary Software Documentation
## Companion Code Repository for Technical and Numerical Validation

**Manuscript:** "Graphene-Assisted Electrostatic Interface Engineering for Radiation-Tolerant MR-DWELL Dosimeters"  
**Authors:** Bigul Dosymova, Mikhail Dolgopolov

This directory contains the Python computational scripts and analytical models required to reproduce the figures, parametric sweeps, and machine-learning classification workflow presented in the Supplementary Material of the manuscript.

---

## 1. Repository Files

| File Name | Description & Functional Role |
| :--- | :--- |
| `analytic_model.py` | Core analytical engine. Computes electrostatic screening factors, quantum capacitance effects, radiation-induced resonance energy shifts, line broadening, and parameter sweeps (barrier thickness, trap density). |
| `plot_fig1.py` | Generates **Figure S1**: Quantum transmission spectra $T(E)$ across the MR-DWELL heterostructure for various h-BN spacer thicknesses at pre-irradiation ($D = 0$) and post-irradiation ($D = 1\text{ MGy}$) states. |
| `plot_fig2.py` | Generates **Figure S2**: Resonance linewidth evolution $\Gamma(D)$ for the graphene-assisted device in comparison with an unscreened metal-contact benchmark. |
| `classification_model.py` | Generates **Figure S3**: Synthetic dataset generation and dimensionality reduction workflow (PCA/LDA) for multi-parameter radiation type and dose-level classification. |
| `requirements.txt` | Complete list of Python package dependencies with exact version requirements for environmental reproducibility. |

---

## 2. Installation & Requirements

The code requires Python 3.8 or higher. All necessary library dependencies (`numpy`, `scipy`, `matplotlib`, and `scikit-learn`) can be installed using `pip`[cite: 4]:

```bash
# Install required Python packages
pip install -r requirements.txt
