---
title: "Conformational ensembles"
source: https://en.wikipedia.org/wiki/Conformational_ensemble
domain: molecular-modeling
license: CC-BY-SA-4.0
tags: molecular modeling, force field, molecular mechanics, potential energy surface
fetched: 2026-07-02
---

# Conformational ensembles

(Redirected from

Conformational ensemble

)

In protein chemistry, **conformational ensembles**, also known as **structural ensembles**, are models describing the structure of intrinsically unstructured proteins. Such proteins are flexible in nature and cannot be described by a single structural representation. The techniques of ensemble calculation are relatively new on the field of structural biology, and are still facing certain limitations that need to be addressed before it will become comparable to classical structural description methods such as biological macromolecular crystallography.

## Purpose

Ensembles are models consisting of a set of conformations that describe the structure of a flexible protein. Even though the degree of conformational freedom is extremely high, flexible/disordered protein generally differ from fully random coil structures. The main purpose of these models is to gain insights regarding the function of the flexible protein, extending the structure-function paradigm from folded proteins to intrinsically disordered proteins.

## Calculation techniques

The calculation of ensembles rely on experimental measurements, mostly by Neutron spin echo spectroscopy, Nuclear Magnetic Resonance spectroscopy and Small-angle X-ray scattering. These measurements yield structural information.

### Short-range

- Chemical Shifts (CS)
- Residual Dipolar Couplings (RDCs)
- J-couplings
- Hydrogen-exchange
- Solvent-accessibility.

### Long-range

- Paramagnetic Relaxation Enhancements (PREs)
- Nuclear Overhauser effects (NOEs)
- SAXS topological restraints.

### Constrained molecular dynamics simulations

The structure of disordered proteins may be approximated by running constrained molecular dynamics (MD) simulations where the conformational sampling is being influenced by experimentally derived constraints.

### Fitting experimental data

Another approach uses selection algorithms such as ENSEMBLE and ASTEROIDS. Calculation procedures first generate a pool of random conformers (initial pool) so that they sufficiently sample the conformation space. The selection algorithms start by choosing a smaller set of conformers (an ensemble) from the initial pool. Experimental parameters (NMR/SAXS) are calculated (usually by some theoretical prediction methods) for each conformer of chosen ensemble and averaged over ensemble. The difference between these calculated parameters and true experimental parameters is used to make an error function and the algorithm selects the final ensemble so that the error function is minimised.

## Limitations

The determination of a structural ensemble for an IDP from NMR/SAXS experimental parameters involves generation of structures that agree with the parameters and their respective weights in the ensemble. Usually, the available experimental data is less compared to the number of variables required to determine making it an under-determined system. Due to this reason, several structurally very different ensembles may describe the experimental data equally well, and currently there are no exact methods to discriminate between ensembles of equally good fit. This problem has to be solved either by bringing in more experimental data or by improving the prediction methods by introducing rigorous computational methods.
