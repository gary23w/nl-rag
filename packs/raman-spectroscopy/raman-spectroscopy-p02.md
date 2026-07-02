---
title: "Raman spectroscopy (part 2/2)"
source: https://en.wikipedia.org/wiki/Raman_spectroscopy
domain: raman-spectroscopy
license: CC-BY-SA-4.0
tags: inelastic scattering, vibrational mode, stokes shift, surface enhanced
fetched: 2026-07-02
part: 2/2
---

## Simulation of molecular Raman spectroscopy

### Static (harmonic) model

In the conventional *Placzek* framework, the Raman activity of a vibrational normal mode *p* , which is determined by the derivatives of the isotropic and anisotropic parts of the polarizability tensor respect to normal coordinate $Q_{p}$ :

$S_{p}=45\!\left({\frac {\partial \alpha _{\mathrm {iso} }}{\partial Q_{p}}}\right)^{2}+7\!\left({\frac {\partial \alpha _{\mathrm {aniso} }}{\partial Q_{p}}}\right)^{2}$

Where, $\alpha$ is the 3x3 polarizability tensor.

$\alpha _{\mathrm {iso} }={\frac {1}{3}}(\alpha _{xx}+\alpha _{yy}+\alpha _{zz})$ $\alpha _{\mathrm {aniso} }={\sqrt {{\frac {1}{2}}\!\left[(\alpha _{xx}-\alpha _{yy})^{2}+(\alpha _{yy}-\alpha _{zz})^{2}+(\alpha _{zz}-\alpha _{xx})^{2}+6(\alpha _{xy}^{2}+\alpha _{yz}^{2}+\alpha _{zx}^{2})\right]}}$

In the **double-harmonic approximations**, the potential energy is expanded to the **second order** near equilibrium (harmonic force fields), while polarizability, is truncated at **first order** in the normal coordinates.

### Polarizability, normal coordinate and frequency

The static polarizability tensor is calculated as the second derivative of the electronic energy $E(\mathbf {F} )$ respect to the external electric field $\mathbf {F}$ :

$\alpha _{ij}\;=\;-\,\left.{\frac {\partial ^{2}E(\mathbf {F} )}{\partial F_{i}\,\partial F_{j}}}\right|_{\mathbf {F} =0},\qquad i,j\in \{x,y,z\}$

In practice, $\alpha$ can be calculated through analytical methods or by employing the finite difference method for energy under small perturbations in $\mathbf {F}$ . The polarizability derivatives used to calculate Raman activities, which could be obtained by the chain rule that relates Cartesian coordinates $\mathbf {R}$ and normal coordinates $Q_{p}$ :

${\frac {\partial {\boldsymbol {\alpha }}}{\partial Q_{p}}}=\sum _{i}{\frac {\partial {\boldsymbol {\alpha }}}{\partial R_{i}}}{\frac {\partial R_{i}}{\partial Q_{p}}}.$

The $\partial R_{i}/\partial Q_{p}$ is given by the normalized linear transformation between cartesian coordinate and mass-weighted normal coordinates:

${\frac {\partial R_{i}}{\partial Q_{p}}}=(\mathbf {M} ^{-1/2}\mathbf {L} )_{ip},$

Where M is the diagonal matrix of atomic masses and L is the matrix of orthonormal eigenvectors (normal modes). It is given by diagonalizing the mass-weighted Hessian matrix:

$\mathbf {H} ^{(\mathrm {mw} )}=\mathbf {M} ^{-1/2}\,\mathbf {H} \,\mathbf {M} ^{-1/2}.$

The Cartesian Hessian elements are second derivatives of the potential energy respect to atomic Cartesian coordinates:

$H_{ab}\;=\;\left.{\frac {\partial ^{2}E}{\partial R_{a}\,\partial R_{b}}}\right|_{\mathbf {R} =\mathbf {R} _{0}},\qquad a,b=1,\dots ,3N.$

Diagonalization of the mass-weighted Hessian, we can obtain the eigenvalues $\omega _{p}^{2}$ and eigenvectors $\mathbf {L}$ ; the vibrational wavenumbers ${\tilde {\nu }}_{p}={\frac {\omega _{p}}{2\pi c}}$ are Five (or six for nonlinear molecules) near-zero eigenvalues correspond to overall translations and rotations, which need to remove from the modes when we do vibrational analysis. Since the $\partial {\boldsymbol {\alpha }}/\partial \mathbf {R}$ is known from finite differences or gradient calculation, it will used to calculate $Q_{p}$ , and further to get the Raman activities.

### Raman intensity (Placzek–Neugebauer expression)

Finally, after get the raman activity, The Raman intensity for the mode p is provided by

$I_{p}({\tilde {\nu }})=K\,({\tilde {\nu }}_{\mathrm {in} }-{\tilde {\nu }}_{p})^{4}{\tilde {\nu }}_{p}^{-1}\!\left[45\!\left({\frac {\partial \alpha _{\mathrm {iso} }}{\partial Q_{p}}}\right)^{2}+7\!\left({\frac {\partial \alpha _{\mathrm {aniso} }}{\partial Q_{p}}}\right)^{2}\right]\!{\frac {1}{1-\exp(-hc{\tilde {\nu }}_{p}/k_{\mathrm {B} }T)}}$

where

- ${\tilde {\nu }}_{\mathrm {in} }$ : the wavenumber of incident light (cm $^{-1}$ );
- ${\tilde {\nu }}_{p}$ : the vibrational wavenumber of mode p ;
- $K={\frac {2\pi ^{4}}{45\epsilon _{0}^{2}c^{4}}}$ is a physical prefactor;
- h : Planck constant; c : speed of light; $k_{\mathrm {B} }$ : Boltzmann constant; T : absolute temperature;
- Term $({\tilde {\nu }}_{\mathrm {in} }-{\tilde {\nu }}_{p})^{4}$ provides the characteristic frequency dependence from frequency difference;
- Last factor is the **thermal population correction** distinguishing Stokes and anti-Stokes lines

Since some thermodynamic calculations ignored in the harmonic approximation, DFT-calculated harmonic frequencies are systematically **too high**.

Hence, an scaling factor $f_{\mathrm {scale} }$ is applied to vibrational frequencies before comparing simulated spectrum with the experiment:

${\tilde {\nu }}_{\mathrm {corr} }=f_{\mathrm {scale} }\,{\tilde {\nu }}_{\mathrm {calc} }$

For example, the B3LYP/TZVP scaling factor is 0.965.

Before to calculating the static spectrum, the structure must be optimized to its lowest energy point using the same or an approximate DFT basis set/functional. The mentioned static (harmonic) method also has been integrated into the Gaussian software as default, using the keyword Opt Freq=Raman to calculate.

### Dynamic (time correlation) approach

The harmonic approximation methods ignore some non-harmonic calculations. As an alternative, *ab initio* or machine-learned molecular-dynamics trajectories provide dynamic Raman spectrum.

At each time step, the real-time polarizability tensor ${\boldsymbol {\alpha }}(t)$ is calculated, from the isotropic and anisotropic components we mentioned as $\alpha _{\mathrm {iso} }(t)$ and $\alpha _{\mathrm {aniso} }(t)$ , there will obtained from dynamical trajectory.

The time autocorrelation functions as follow:

$C_{\mathrm {iso} }(t)=\langle \alpha _{\mathrm {iso} }(0)\,\alpha _{\mathrm {iso} }(t)\rangle ,\qquad C_{\mathrm {aniso} }(t)=\langle \alpha _{\mathrm {aniso} }(0)\,\alpha _{\mathrm {aniso} }(t)\rangle$

and during the Fourier transforms, the isotropic and anisotropic Raman spectra generated as:

$I_{\mathrm {iso} }(\omega )\propto \int e^{i\omega t}\,C_{\mathrm {iso} }(t)\,dt,$ $I_{\mathrm {aniso} }(\omega )\propto \int e^{i\omega t}\,C_{\mathrm {aniso} }(t)\,dt.$

An isotropic media (liquids, gases), the **observable Raman** **spectra** under unpolarized detection is a rotational average of the two components:

$I_{\mathrm {Raman} }(\omega )=I_{\mathrm {iso} }(\omega )+{\frac {4}{3}}\,I_{\mathrm {aniso} }(\omega ).$

This expression is derived from the angular momentum averaging of scattered lights from the random molecular orientations.

The factor 4/3 the iso/aniso probably contribution.

And the **depolarization ratio**, often used experimentally to featurize the polarization effects, is defied by:

$\rho (\omega )={\frac {I_{\perp }(\omega )}{I_{\parallel }(\omega )}}={\frac {3\,I_{\mathrm {aniso} }(\omega )}{45\,I_{\mathrm {iso} }(\omega )+4\,I_{\mathrm {aniso} }(\omega )}}.$

The ratio show the information on the symmetry of the vibrational modes.

So, from the time dependent polarizability tensor ${\boldsymbol {\alpha }}(t)$ , the isotropic and anisotropic time series can be obtained. Their autocorrelation functions are calculated, Fourier transformed, and finally combined using the rotational averaging method to generate the total Raman spectrum.

This polarizability-autocorrelation Fourier transform method naturally integrates anharmonic coupling, temperature broadening, and the polarization effects. It is providing a realistic description of Raman spectroscopy beyond the harmonic approximation.

### Machine learning approach

In recent years, machine learning has become a powerful tool in Raman spectroscopy, enabling data-driven prediction and interpretation of spectral line characteristics. Such as machine learned interatomic potential and generative model.

**Zihan Zou et al.****.** Using equivariant graph neural networks to predict molecular polarizabilities and Hessian matrices, and using harmonic vibration models to reproduce Raman spectra with quantum-level precision.

**Tianqing Hu et al.****.** Using a *generative Transformer architecture* with a *graph neural network* to achieve bi-directional prediction between molecular structures formula and their corresponding IR/Raman spectra.

**Grace M. Sommers et al.****.** Provide a neural network force field to reconstruct the Raman spectrum of liquid water directly from the *time-dependent polarizability trajectory*, bridging molecular dynamics and spectroscopy.

**Michael Gastegger et al.****.** Using differentiable graph neural network framework to model IR/Raman spectrum under some external perturbations such as electric fields. This work highlights the versatility of machine learning in capturing some environmental effects and non-harmonic effects.
