---
title: "Local-density approximation"
source: https://en.wikipedia.org/wiki/Local-density_approximation
domain: density-functional-theory
license: CC-BY-SA-4.0
tags: density functional theory, kohn-sham equations, hohenberg-kohn theorems, pseudopotential
fetched: 2026-07-02
---

# Local-density approximation

**Local-density approximations** (**LDA**) are a class of approximations to the exchange–correlation (XC) energy functional in density functional theory (DFT) that depend solely upon the value of the electronic density at each point in space (and not, for example, derivatives of the density or the Kohn–Sham orbitals). Many approaches can yield local approximations to the XC energy. However, overwhelmingly successful local approximations are those that have been derived from the homogeneous electron gas (HEG) model. In this regard, LDA is generally synonymous with functionals based on the HEG approximation, which are then applied to realistic systems (molecules and solids).

In general, for a spin-unpolarized system, a local-density approximation for the exchange-correlation energy is written as

$E_{\rm {xc}}^{\mathrm {LDA} }[\rho ]=\int \rho (\mathbf {r} )\epsilon _{\rm {xc}}(\rho (\mathbf {r} ))\ \mathrm {d} \mathbf {r} \ ,$

where *ρ* is the electronic density and *єxc* is the exchange-correlation energy per particle of a homogeneous electron gas of charge density *ρ*. The exchange-correlation energy is decomposed into exchange and correlation terms linearly,

$E_{\rm {xc}}=E_{\rm {x}}+E_{\rm {c}}\ ,$

so that separate expressions for *E*x and *E*c are sought. The exchange term takes on a simple analytic form for the HEG. Only limiting expressions for the correlation density are known exactly, leading to numerous different approximations for *є*c.

Local-density approximations are important in the construction of more sophisticated approximations to the exchange-correlation energy, such as generalized gradient approximations (GGA) or hybrid functionals, as a desirable property of any approximate exchange-correlation functional is that it reproduce the exact results of the HEG for non-varying densities. As such, LDA's are often an explicit component of such functionals.

The local-density approximation was first introduced by Walter Kohn and Lu Jeu Sham in 1965.

## Applications

Local density approximations, as with GGAs are employed extensively by solid state physicists in ab-initio DFT studies to interpret electronic and magnetic interactions in semiconductor materials including semiconducting oxides and spintronics. The importance of these computational studies stems from the system complexities which bring about high sensitivity to synthesis parameters necessitating first-principles based analysis. The prediction of Fermi level and band structure in doped semiconducting oxides is often carried out using LDA incorporated into simulation packages such as CASTEP and DMol3. However an underestimation in Band gap values often associated with LDA and GGA approximations may lead to false predictions of impurity mediated conductivity and/or carrier mediated magnetism in such systems. Starting in 1998, the application of the Rayleigh theorem for eigenvalues has led to mostly accurate, calculated band gaps of materials, using LDA potentials. A misunderstanding of the second theorem of DFT appears to explain most of the underestimation of band gap by LDA and GGA calculations, as explained in the description of density functional theory, in connection with the statements of the two theorems of DFT.

## Homogeneous electron gas

Approximation for *є*xc depending only upon the density can be developed in numerous ways. The most successful approach is based on the homogeneous electron gas. This is constructed by placing *N* interacting electrons in to a volume, *V*, with a positive background charge keeping the system neutral. *N* and *V* are then taken to infinity in the manner that keeps the density (*ρ* = *N* / *V*) finite. This is a useful approximation, as the total energy consists of contributions only from the kinetic energy, electrostatic interaction energy and exchange-correlation energy, and that the wavefunction is expressible in terms of plane waves. In particular, for a constant density *ρ*, the exchange energy density is proportional to *ρ*⅓.

## Exchange functional

The exchange-energy density of a HEG is known analytically. The LDA for exchange employs this expression under the approximation that the exchange-energy in a system where the density is not homogeneous, is obtained by applying the HEG results pointwise, yielding the expression

$E_{\rm {x}}^{\mathrm {LDA} }[\rho ]=-{\frac {3e^{2}}{16\pi \varepsilon _{0}}}\left({\frac {3}{\pi }}\right)^{1/3}\int \rho (\mathbf {r} )^{4/3}\ \mathrm {d} \mathbf {r} =-{\frac {3}{4}}\left({\frac {3}{\pi }}\right)^{1/3}\int \rho (\mathbf {r} )^{4/3}\ \mathrm {d} \mathbf {r} \,,$

where the second formulation applies in atomic units.

## Correlation functional

Analytic expressions for the correlation energy of the HEG are available in the high- and low-density limits corresponding to infinitely-weak and infinitely-strong correlation. For a HEG with density *ρ*, the high-density limit of the correlation energy density is

$\epsilon _{\rm {c}}=A\ln(r_{\rm {s}})+B+r_{\rm {s}}(C\ln(r_{\rm {s}})+D)\ ,$

and the low limit

$\epsilon _{\rm {c}}={\frac {1}{2}}\left({\frac {g_{0}}{r_{\rm {s}}}}+{\frac {g_{1}}{r_{\rm {s}}^{3/2}}}+\dots \right)\ ,$

where the Wigner-Seitz parameter $r_{\rm {s}}$ is dimensionless. It is defined as the radius of a sphere which encompasses exactly one electron, divided by the Bohr radius *a*0. In terms of the density *ρ*, this means

${\frac {4}{3}}\pi r_{\rm {s}}^{3}={\frac {1}{\rho \,a_{0}^{3}}}\ .$

An analytical expression for the full range of densities has been proposed based on the many-body perturbation theory. The calculated correlation energies are in agreement with the results from quantum Monte Carlo simulation to within 2 milli-Hartree.

Accurate quantum Monte Carlo simulations for the energy of the HEG have been performed for several intermediate values of the density, in turn providing accurate values of the correlation energy density.

## Spin polarization

The extension of density functionals to spin-polarized systems is straightforward for exchange, where the exact spin-scaling is known, but for correlation further approximations must be employed. A spin polarized system in DFT employs two spin-densities, *ρ*α and *ρ*β with *ρ* = *ρ*α + *ρ*β, and the form of the local-spin-density approximation (LSDA) is

$E_{\rm {xc}}^{\mathrm {LSDA} }[\rho _{\alpha },\rho _{\beta }]=\int \mathrm {d} \mathbf {r} \ \rho (\mathbf {r} )\epsilon _{\rm {xc}}(\rho _{\alpha },\rho _{\beta })\ .$

For the exchange energy, the exact result (not just for local density approximations) is known in terms of the spin-unpolarized functional:

$E_{\rm {x}}[\rho _{\alpha },\rho _{\beta }]={\frac {1}{2}}{\bigg (}E_{\rm {x}}[2\rho _{\alpha }]+E_{\rm {x}}[2\rho _{\beta }]{\bigg )}\ .$

The spin-dependence of the correlation energy density is approached by introducing the relative spin-polarization:

$\zeta (\mathbf {r} )={\frac {\rho _{\alpha }(\mathbf {r} )-\rho _{\beta }(\mathbf {r} )}{\rho _{\alpha }(\mathbf {r} )+\rho _{\beta }(\mathbf {r} )}}\ .$

$\zeta =0\,$ corresponds to the diamagnetic spin-unpolarized situation with equal $\alpha \,$ and $\beta \,$ spin densities whereas $\zeta =\pm 1$ corresponds to the ferromagnetic situation where one spin density vanishes. The spin correlation energy density for a given values of the total density and relative polarization, *є*c(*ρ*,*ζ*), is constructed so to interpolate the extreme values. Several forms have been developed in conjunction with LDA correlation functionals.

## Exchange-correlation potential

The exchange-correlation potential corresponding to the exchange-correlation energy for a local density approximation is given by

$v_{\rm {xc}}^{\mathrm {LDA} }(\mathbf {r} )={\frac {\delta E^{\mathrm {LDA} }}{\delta \rho (\mathbf {r} )}}=\epsilon _{\rm {xc}}(\rho (\mathbf {r} ))+\rho (\mathbf {r} ){\frac {\partial \epsilon _{\rm {xc}}(\rho (\mathbf {r} ))}{\partial \rho (\mathbf {r} )}}\ .$

In finite systems, the LDA potential decays asymptotically with an exponential form. This result is in error; the true exchange-correlation potential decays much slower in a Coulombic manner. The artificially rapid decay manifests itself in the number of Kohn–Sham orbitals the potential can bind (that is, how many orbitals have energy less than zero). The LDA potential can not support a Rydberg series and those states it does bind are too high in energy. This results in the highest occupied molecular orbital (HOMO) energy being too high in energy, so that any predictions for the ionization potential based on Koopmans' theorem are poor. Further, the LDA provides a poor description of electron-rich species such as anions where it is often unable to bind an additional electron, erroneously predicating species to be unstable. In the case of spin polarization, the exchange-correlation potential acquires spin indices. However, if one only considers the exchange part of the exchange-correlation, one obtains a potential that is diagonal in spin indices (in atomic units):

$v_{\rm {xc,\alpha \beta }}^{\mathrm {LDA} }(\mathbf {r} )={\frac {\delta E^{\mathrm {LDA} }}{\delta \rho _{\alpha \beta }(\mathbf {r} )}}={\frac {1}{2}}\delta _{\alpha \beta }{\frac {\delta E^{\mathrm {LDA} }[2\rho _{\alpha }]}{\delta \rho _{\alpha }}}=-\delta _{\alpha \beta }{\Big (}{\frac {3}{\pi }}{\Big )}^{1/3}2^{1/3}\rho _{\alpha }^{1/3}$
