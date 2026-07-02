---
title: "Plasma oscillation"
source: https://en.wikipedia.org/wiki/Plasma_oscillation
domain: plasma-physics
license: CC-BY-SA-4.0
tags: plasma physics, magnetohydrodynamics simulation, debye length, plasma oscillation
fetched: 2026-07-02
---

# Plasma oscillation

**Plasma oscillations**, also known as **Langmuir waves** (eponymously after Irving Langmuir), are rapid oscillations of the electron density in conductive media, most notably plasmas as well as metals, at frequencies typically corresponding to the ultraviolet band of the electromagnetic spectrum. The oscillations can be described as an instability in the dielectric function of a free electron gas. The frequency depends only weakly on the wavelength of the oscillation. The quasiparticle resulting from the quantization of these oscillations is the *plasmon*.

Langmuir waves were discovered by American physicists Irving Langmuir and Lewi Tonks in the 1920s. They are parallel in form to Jeans instability waves, which are caused by gravitational instabilities in a static medium.

## Mechanism

Consider an electrically neutral plasma in equilibrium, consisting of a gas of positively charged ions and negatively charged electrons. If one displaces an electron or a group of electrons slightly with respect to the ions, the Coulomb force pulls the electrons back, acting as a restoring force.

### Cold electrons

If the thermal motion of the electrons is ignored, the charge density oscillates at the *plasma frequency*:

$\omega _{\mathrm {pe} }={\sqrt {\frac {n_{\mathrm {e} }e^{2}}{m^{*}\varepsilon _{0}}}},\quad {\text{[rad/s]}}\quad {\text{(SI units)}}$

$\omega _{\mathrm {pe} }={\sqrt {\frac {4\pi n_{\mathrm {e} }e^{2}}{m^{*}}}},\quad {\text{[rad/s]}}\quad {\text{(cgs units)}}$

where $n_{\mathrm {e} }$ is the electron number density, e is the elementary charge, $m^{*}$ is the electron effective mass, and $\varepsilon _{0}$ is the vacuum permittivity. This assumes infinite ion mass, a good approximation since electrons are much lighter.

A derivation using Maxwell’s equations gives the same result via the dielectric condition $\epsilon (\omega )=0$ . This is the condition for plasma transparency and wave propagation.

In electron–positron plasmas, relevant in astrophysics, the expression must be modified. As the plasma frequency is independent of wavelength, Langmuir waves have infinite phase velocity and zero group velocity.

For $m^{*}=m_{\mathrm {e} }$ , the frequency depends only on electron density and physical constants. The linear plasma frequency is:

$f_{\text{pe}}={\frac {\omega _{\text{pe}}}{2\pi }}\quad {\text{[Hz]}}$

Metals are reflective to light below their plasma frequency, which is in the UV range (~10²³ electrons/cm³). Hence they appear shiny in visible light.

### Warm electrons

Including the effects of electron thermal velocity $v_{\mathrm {e,th} }={\sqrt {k_{\mathrm {B} }T_{\mathrm {e} }/m_{\mathrm {e} }}}$ , the dispersion relation becomes:

$\omega ^{2}=\omega _{\mathrm {pe} }^{2}+3k^{2}v_{\mathrm {e,th} }^{2}$

This is known as the Bohm–Gross dispersion relation. For long wavelengths, pressure effects are minimal; for short wavelengths, dispersion dominates. At these small scales, wave phase velocity $v_{\mathrm {ph} }=\omega /k$ becomes comparable to $v_{\mathrm {e,th} }$ , leading to Landau damping.

In bounded plasmas, plasma oscillations can still propagate due to fringing fields, even for cold electrons.

In metals or semiconductors, the ions' periodic potential is accounted for using the effective mass $m^{*}$ .

### Plasma oscillations and negative effective mass

Plasma oscillations can result in an effective negative mass. Consider the mass–spring model in Figure 1. Solving the equations of motion and replacing the system with a single effective mass gives:

$m_{\rm {eff}}=m_{1}+{\frac {m_{2}\omega _{0}^{2}}{\omega _{0}^{2}-\omega ^{2}}}$

where $\omega _{0}={\sqrt {k_{2}/m_{2}}}$ . As $\omega$ approaches $\omega _{0}$ from above, $m_{\rm {eff}}$ becomes negative.

This analogy applies to plasmonic systems too (Figure 2). Plasma oscillations of electron gas in a lattice behave like a spring system, giving an effective mass:

$m_{\rm {eff}}=m_{1}+{\frac {m_{2}\omega _{\rm {p}}^{2}}{\omega _{\rm {p}}^{2}-\omega ^{2}}}$

Near $\omega _{\rm {p}}$ , this effective mass becomes negative. Metamaterials exploiting this behavior have been studied.
