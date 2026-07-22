Supplementary Software Documentation
Companion Code Repository for Technical and Numerical Validation
Manuscript: "Graphene-Assisted Electrostatic Interface Engineering for Radiation-Tolerant MR-DWELL
Dosimeters"
Authors: Bigul Dosymova, Mikhail Dolgopolov
This directory contains the Python computational scripts and analytical models required to reproduce
the figures, parametric sweeps, and machine-learning classification workflow presented in the
Supplementary Material of the manuscript.
1. Repository Files
File Name Description & Functional Role
analytic_model.py Core analytical engine. Computes electrostatic screening factors,
quantum capacitance effects, radiation-induced resonance energy
shifts, line broadening, and parameter sweeps (barrier thickness, trap
density).
plot_fig1.py Generates Figure S1: Quantum transmission spectra T(E) across the
MR-DWELL heterostructure for various h-BN spacer thicknesses at preirradiation
(D = 0) and post-irradiation (D = 1 MGy) states.
plot_fig2.py Generates Figure S2: Resonance linewidth evolution Γ(D) for the
graphene-assisted device in comparison with an unscreened metalcontact
benchmark.
classification_model.py Generates Figure S3: Synthetic dataset generation and dimensionality
reduction workflow (PCA/LDA) for multi-parameter radiation type and
dose-level classification.
requirements.txt Complete list of Python package dependencies with exact version
requirements for environmental reproducibility.
2. Installation & Requirements
The code requires Python 3.8 or higher. All necessary library dependencies (including numpy , scipy ,
matplotlib , and scikit-learn ) can be installed using pip :
# Install required Python packages
pip install -r requirements.txt
3. Usage & Execution
Each figure script is fully self-contained and can be executed independently from the command line:
Supplementary Software | MR-DWELL Dosimeters Page 1 of 2
# Generate Figure S1 (Transmission Spectra)
python plot_fig1.py
# Generate Figure S2 (Linewidth Evolution)
python plot_fig2.py
# Generate Figure S3 (PCA/LDA Classification)
python classification_model.py
Upon execution, high-resolution vector and raster graphic files (PNG/PDF) are automatically exported
and saved to the current working directory.
4. Important Technical Notes
Unified Physics Engine: analytic_model.py acts as the single source of truth for physical
constants, geometry, and phenomenological saturation parameters across all plotting routines.
Synthetic Classification Workflow: The classification pipeline in classification_model.py
generates synthetic feature vectors based on analytical descriptor distributions; it does not
require external raw experimental data files.
Reproducibility: All stochastic processes (such as synthetic feature sampling and crossvalidation
splitting) utilize a fixed random seed ( random_state = 42 ) to guarantee exact numerical
reproducibility.
Software Versioning & Calibration
All analytical routines correspond to version 2.0 of the calibrated model, incorporating independent
phenomenological fitting parameters for low-dose sensitivity (αeff) and asymptotic saturation shift
(ΔEmax).
5. Citation
If you utilize this code, analytical model, or generated synthetic datasets in your research, please cite the
original article:
B. Dosymova and M. Dolgopolov, "Graphene-Assisted Electrostatic Interface Engineering for Radiation-
Tolerant MR-DWELL Dosimeters" (2026).
•
•
•
Supplementary Software | MR-DWELL Dosimeters Page 2 of 2
