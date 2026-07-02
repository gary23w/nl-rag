---
title: "Post–Hartree–Fock"
source: https://en.wikipedia.org/wiki/Post-Hartree%E2%80%93Fock
domain: quantum-chemistry-dft
license: CC-BY-SA-4.0
tags: quantum chemistry, electronic structure, coupled cluster, configuration interaction
fetched: 2026-07-02
---

# Post–Hartree–Fock

(Redirected from

Post-Hartree–Fock

)

In computational chemistry, **post–Hartree–Fock** (**post-HF**) methods are the set of methods developed to improve on the Hartree–Fock (HF), or self-consistent field (SCF), method. They add electron correlation which is a more accurate way of including the repulsions between electrons than in the Hartree–Fock method where repulsions are only averaged.

## Details

In general, the SCF procedure makes several assumptions about the nature of the multi-body Schrödinger equation and its set of solutions:

- For molecules, the Born–Oppenheimer approximation is inherently assumed. The true wavefunction should also be a function of the coordinates of each of the nuclei.
- Typically, relativistic effects are completely neglected. The momentum operator is assumed to be completely nonrelativistic.
- The basis set is composed of a finite number of orthogonal functions. The general wavefunction is a linear combination of functions from a complete (infinite) basis set.
- The energy eigenfunctions are assumed to be products of one-electron wavefunctions. The effects of electron correlation, beyond that of exchange energy resulting from the anti-symmetrization of the wavefunction, are completely neglected.

For the great majority of systems under study, in particular for excited states and processes such as molecular dissociation reactions, the fourth item is by far the most important. As a result, the term *post–Hartree–Fock method* is typically used for methods of approximating the electron correlation of a system.

Usually, post–Hartree–Fock methods give more accurate results than Hartree–Fock calculations, though at greater computational cost.

## Post–Hartree–Fock methods

- Configuration interaction (CI)
- Coupled cluster (CC)
- Møller–Plesset perturbation theory (MP2, MP3, MP4, etc.)
- Quadratic configuration interaction (QCI)
- Algebraic Diagrammatic Construction (ADC)
- Quantum chemistry composite methods (G2, G3, CBS, T1. etc.)

Methods that use more than one determinant are not strictly post–Hartree–Fock methods, as they use a single determinant as reference, but they often use similar perturbation, or configuration interaction methods to improve the description of electron correlation. These methods include:

- Multi-configurational self-consistent field (MCSCF)
- Multireference single and double configuration interaction (MRCISD)
- N-electron valence state perturbation theory (NEVPT).
