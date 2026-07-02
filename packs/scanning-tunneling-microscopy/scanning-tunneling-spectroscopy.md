---
title: "Scanning tunneling spectroscopy"
source: https://en.wikipedia.org/wiki/Scanning_tunneling_spectroscopy
domain: scanning-tunneling-microscopy
license: CC-BY-SA-4.0
tags: quantum tunneling imaging, atomic resolution, tunneling current, surface states
fetched: 2026-07-02
---

# Scanning tunneling spectroscopy

**Scanning tunneling spectroscopy (STS)**, an extension of scanning tunneling microscopy (STM), provides information about the density of electrons in a sample as a function of their energy.

In scanning tunneling microscopy, a metal tip is moved over a conducting sample without making physical contact. A bias voltage applied between the sample and the tip allows current to flow between them. This is a result of quantum tunneling across a barrier; in this instance, the physical distance between the tip and the sample.

The scanning tunneling microscope is used to obtain "topographs" - topographic maps - of surfaces. The tip is rastered across a surface and, in constant current mode, a constant current is maintained between the tip and the sample by adjusting the height of the tip. A plot of the tip height at all measurement positions provides the topograph. These topographic images can obtain atomically resolved information on metallic and semiconducting surfaces.

However, the scanning tunneling microscope does not measure the physical height of surface features. One such example of this limitation is an atom adsorbed onto a surface. The image will result in some perturbation of the height at this point. A detailed analysis of the way in which an image is formed shows that the transmission of the electric current between the tip and the sample depends on two factors: (1) the geometry of the sample and (2) the arrangement of the electrons in the sample. The latter is described quantum mechanically by an "electron density". The electron density is a function of both position and energy, and is formally described as the local density of electron states, abbreviated as local density of states (LDOS), which is a function of energy.

Spectroscopy, in its most general sense, refers to a measurement of the number of something as a function of energy. For scanning tunneling spectroscopy the scanning tunneling microscope is used to measure the number of electrons (the LDOS) as a function of the electron energy. The electron energy is set by the electrical potential difference (voltage) between the sample and the tip. The location is set by the position of the tip.

At its simplest, a "scanning tunneling spectrum" is obtained by placing a scanning tunneling microscope tip above a particular place on the sample. With the height of the tip fixed, the electron tunneling current is then measured as a function of electron energy by varying the voltage between the tip and the sample (the tip to sample voltage sets the electron energy). The change of the current with the energy of the electrons is the simplest spectrum that can be obtained, it is often referred to as an I-V curve. As is shown below, it is the slope of the I-V curve at each voltage (often called the dI/dV-curve) which is more fundamental because dI/dV corresponds to the electron density of states at the local position of the tip, the LDOS.

## Introduction

Scanning tunneling spectroscopy is an experimental technique which uses a scanning tunneling microscope (STM) to probe the local density of electronic states (LDOS) and the band gap of surfaces and materials on surfaces at the atomic scale. Generally, STS involves observation of changes in constant-current topographs with tip-sample bias, local measurement of the tunneling current versus tip-sample bias (I-V) curve, measurement of the tunneling conductance, $dI/dV$ , or more than one of these. Since the tunneling current in a scanning tunneling microscope only flows in a region with diameter ~5 Å, STS is unusual in comparison with other surface spectroscopy techniques, which average over a larger surface region. The origins of STS are found in some of the earliest STM work of Gerd Binnig and Heinrich Rohrer, in which they observed changes in the appearance of some atoms in the (7 x 7) unit cell of the Si(111) – (7 x 7) surface with tip-sample bias. STS provides the possibility for probing the local electronic structure of metals, semiconductors, and thin insulators on a scale unobtainable with other spectroscopic methods. Additionally, topographic and spectroscopic data can be recorded simultaneously.

## Tunneling current

Since STS relies on tunneling phenomena and measurement of the tunneling current or its derivative, understanding the expressions for the tunneling current is very important. Using the modified Bardeen transfer Hamiltonian method, which treats tunneling as a perturbation, the tunneling current ( I ) is found to be

| $I={\frac {4\pi e}{\hbar }}\int _{-\infty }^{\infty }\left[f\left(E_{F}-eV+\varepsilon \right)-f\left(E_{F}+\varepsilon \right)\right]\rho _{S}\left(E_{F}-eV+\varepsilon \right)\rho _{T}\left(E_{F}+\varepsilon \right)\left\|M_{\mu \nu }\right\|^{2}\,d\varepsilon \ ,$ |   | 1 |
|---|---|---|

where $f\left(E\right)$ is the Fermi distribution function, $\rho _{s}$ and $\rho _{T}$ are the density of states (DOS) in the sample and tip, respectively, and $M_{\mu \nu }$ is the tunneling matrix element between the modified wavefunctions of the tip and the sample surface. The tunneling matrix element,

| $M_{\mu \nu }=-{\frac {\hbar ^{2}}{2m}}\int _{\Sigma }\left(\chi _{\nu }^{*}\nabla \psi _{\mu }-\psi _{\mu }\nabla \chi _{\nu }^{*}\right)\cdot \,d{\mathbf {S} }\ ,$ |   | 2 |
|---|---|---|

describes the energy lowering due to the interaction between the two states. Here $\psi$ and $\chi$ are the sample wavefunction modified by the tip potential, and the tip wavefunction modified by sample potential, respectively.

For low temperatures and a constant tunneling matrix element, the tunneling current reduces to

| $I\propto \int _{0}^{eV}\rho _{S}\left(E_{F}-eV+\varepsilon \right)\rho _{T}\left(E_{F}+\varepsilon \right)\,d\varepsilon \ ,$ |   | 3 |
|---|---|---|

which is a convolution of the DOS of the tip and the sample. Generally, STS experiments attempt to probe the sample DOS, but equation (3) shows that the tip DOS must be known for the measurement to have meaning. Equation (3) implies that

| ${\frac {dI}{dV}}\propto \rho _{S}\left(E_{F}-eV\right)\ ,$ |   | 4 |
|---|---|---|

under the gross assumption that the tip DOS is constant. For these ideal assumptions, the tunneling conductance is directly proportional to the sample DOS.

For higher bias voltages, the predictions of simple planar tunneling models using the Wentzel-Kramers Brillouin (WKB) approximation are useful. In the WKB theory, the tunneling current is predicted to be

| $I\propto \int _{0}^{eV}\rho _{S}\left(r,E\right)\rho _{T}\left(r,E-eV\right)T\left(E,eV,r\right)\,dE\ ,$ |   | 5 |
|---|---|---|

where $\rho _{s}$ and $\rho _{t}$ are the density of states (DOS) in the sample and tip, respectively. The energy- and bias-dependent electron tunneling transition probability, T, is given by

| $T=\exp \left(-{\frac {2Z{\sqrt {2m}}}{\hbar }}{\sqrt {{\frac {\phi _{s}+\phi _{t}}{2}}+{\frac {eV}{2}}-E}}\right)\ ,$ |   | 6 |
|---|---|---|

where $\phi _{s}$ and $\phi _{t}$ are the respective work functions of the sample and tip and Z is the distance from the sample to the tip.

The tip is often regarded to be a single molecule, essentially neglecting further shapes induced effects. This approximation is the Tersoff-Hamann approximation, which suggests the tip to be a single ball-shaped molecule of certain radius. The tunneling current therefore becomes proportional to the local density of states (LDOS).

## Experimental methods

Acquiring standard STM topographs at many different tip-sample biases and comparing to experimental topographic information is perhaps the most straightforward spectroscopic method. The tip-sample bias can also be changed on a line-by-line basis during a single scan. This method creates two interleaved images at different biases. Since only the states between the Fermi levels of the sample and the tip contribute to I , this method is a quick way to determine whether there are any interesting bias-dependent features on the surface. However, only limited information about the electronic structure can be extracted by this method, since the constant I topographs depend on the tip and sample DOS's and the tunneling transmission probability, which depends on the tip-sample spacing, as described in equation (5).

By using modulation techniques, a constant current topograph and the spatially resolved $dI/dV$ can be acquired simultaneously. A small, high frequency sinusoidal modulation voltage is superimposed on the D.C. tip-sample bias. The A.C. component of the tunneling current is recorded using a lock-in amplifier, and the component in-phase with the tip-sample bias modulation gives $dI/dV$ directly. The amplitude of the modulation Vm has to be kept smaller than the spacing of the characteristic spectral features. The broadening caused by the modulation amplitude is 2 eVm and it has to be added to the thermal broadening of 3.2 kBT. In practice, the modulation frequency is chosen slightly higher than the bandwidth of the STM feedback system. This choice prevents the feedback control from compensating for the modulation by changing the tip-sample spacing and minimizes the displacement current 90° out-of-phase with the applied bias modulation. Such effects arise from the capacitance between the tip and the sample, which grows as the modulation frequency increases.

In order to obtain I-V curves simultaneously with a topograph, a sample-and-hold circuit is used in the feedback loop for the z piezo signal. The sample-and-hold circuit freezes the voltage applied to the z piezo, which freezes the tip-sample distance, at the desired location allowing I-V measurements without the feedback system responding. The tip-sample bias is swept between the specified values, and the tunneling current is recorded. After the spectra acquisition, the tip-sample bias is returned to the scanning value, and the scan resumes. Using this method, the local electronic structure of semiconductors in the band gap can be probed.

There are two ways to record I-V curves in the manner described above. In constant-spacing scanning tunneling spectroscopy (CS-STS), the tip stops scanning at the desired location to obtain an I-V curve. The tip-sample spacing is adjusted to reach the desired initial current, which may be different from the initial current setpoint, at a specified tip-sample bias. A sample-and-hold amplifier freezes the z piezo feedback signal, which holds the tip-sample spacing constant by preventing the feedback system from changing the bias applied to the z piezo. The tip-sample bias is swept through the specified values, and the tunneling current is recorded. Either numerical differentiation of I(V) or lock-in detection as described above for modulation techniques can be used to find $dI/dV$ . If lock-in detection is used, then an A.C. modulation voltage is applied to the D.C. tip-sample bias during the bias sweep and the A.C. component of the current in-phase with the modulation voltage is recorded.

In variable-spacing scanning tunneling spectroscopy (VS-STS), the same steps occur as in CS-STS through turning off the feedback. As the tip-sample bias is swept through the specified values, the tip-sample spacing is decreased continuously as the magnitude of the bias is reduced. Generally, a minimum tip-sample spacing is specified to prevent the tip from crashing into the sample surface at the 0 V tip-sample bias. Lock-in detection and modulation techniques are used to find the conductivity, because the tunneling current is a function also of the varying tip-sample spacing. Numerical differentiation of I(V) with respect to V would include the contributions from the varying tip-sample spacing. Introduced by Mårtensson and Feenstra to allow conductivity measurements over several orders of magnitude, VS-STS is useful for conductivity measurements on systems with large band gaps. Such measurements are necessary to properly define the band edges and examine the gap for states.

Current-imaging-tunneling spectroscopy (CITS) is an STS technique where an I-V curve is recorded at each pixel in the STM topograph. Either variable-spacing or constant-spacing spectroscopy may be used to record the I-V curves. The conductance, $dI/dV$ , can be obtained by numerical differentiation of I with respect to V or acquired using lock-in detection as described above. Because the topographic image and the tunneling spectroscopy data are obtained nearly simultaneously, there is nearly perfect registry of topographic and spectroscopic data. As a practical concern, the number of pixels in the scan or the scan area may be reduced to prevent piezo creep or thermal drift from moving the feature of study or the scan area during the duration of the scan. While most CITS data obtained on the times scale of several minutes, some experiments may require stability over longer periods of time. One approach to improving the experimental design is by applying feature-oriented scanning (FOS) methodology.

## Data interpretation

From the obtained I-V curves, the band gap of the sample at the location of the I-V measurement can be determined. By plotting the magnitude of I on a log scale versus the tip-sample bias, the band gap can clearly be determined. Although determination of the band gap is possible from a linear plot of the I-V curve, the log scale increases the sensitivity. Alternatively, a plot of the conductance, $dI/dV$ , versus the tip-sample bias, V, allows one to locate the band edges that determine the band gap.

The structure in the $dI/dV$ , as a function of the tip-sample bias, is associated with the density of states of the surface when the tip-sample bias is less than the work functions of the tip and the sample. Usually, the WKB approximation for the tunneling current is used to interpret these measurements at low tip-sample bias relative to the tip and sample work functions. The derivative of equation (5), I in the WKB approximation, is

| ${\frac {dI}{dV}}=\rho _{s}\left(r,eV\right)\rho _{t}\left(r,0\right)T\left(eV,eV,r\right)+\int _{0}^{eV}\rho _{s}\left(r,E\right)\rho _{t}\left(r,E-eV\right){\frac {dT\left(E,eV,r\right)}{dV}}\,dE\ ,$ |   | 7 |
|---|---|---|

where $\rho _{s}$ is the sample density of states, $\rho _{t}$ is the tip density of states, and T is the tunneling transmission probability. Although the tunneling transmission probability T is generally unknown, at a fixed location T increases smoothly and monotonically with the tip-sample bias in the WKB approximation. Hence, structure in the $dI/dV$ is usually assigned to features in the density of states in the first term of equation (7).

Interpretation of $dI/dV$ as a function of position is more complicated, but can reveal information about the momentum-space electronic structure from Quasiparticle interference imaging. Spatial variations in T show up in measurements of $dI/dV$ as an inverted topographic background. When obtained in constant current mode, images of the spatial variation of $dI/dV$ contain a convolution of topographic and electronic structure. An additional complication arises since $dI/dV=I/V$ in the low-bias limit. Thus, $dI/dV$ diverges as V approaches 0, preventing investigation of the local electronic structure near the Fermi level.

Since both the tunneling current, equation (5), and the conductance, equation (7), depend on the tip DOS and the tunneling transition probability, T, quantitative information about the sample DOS is very difficult to obtain. Additionally, the voltage dependence of T, which is usually unknown, can vary with position due to local fluctuations in the electronic structure of the surface. For some cases, normalizing $dI/dV$ by dividing by $I/V$ can minimize the effect of the voltage dependence of T and the influence of the tip-sample spacing. Using the WKB approximation, equations (5) and (7), we obtain:

| ${\frac {dI/dV}{I/V}}={\frac {\displaystyle \rho _{s}\left(r,eV\right)\rho _{t}\left(r,0\right)+\int _{0}^{eV}{\frac {\rho _{s}\left(r,E\right)\rho _{t}\left(r,E-eV\right)}{T\left(eV,eV,r\right)}}{\frac {dT\left(E,eV,r\right)}{dV}}\,dE}{\displaystyle {\frac {1}{eV}}\int _{0}^{eV}\rho _{s}\left(r,E\right)\rho _{t}\left(r,E-eV\right){\frac {T\left(E,eV,r\right)}{T\left(eV,eV,r\right)}}\,dE}}\ .$ |   | 8 |
|---|---|---|

Feenstra et al. argued that the dependencies of $T\left(E,eV,r\right)$ and $T\left(eV,eV,r\right)$ on tip-sample spacing and tip-sample bias tend to cancel, since they appear as ratios. This cancellation reduces the normalized conductance to the following form:

| ${\frac {dI/dV}{I/V}}={\frac {d\left(\ln I\right)}{d\left(\ln V\right)}}={\frac {\rho _{s}\left(r,eV\right)\rho _{t}\left(r,0\right)+A\left(V\right)}{B\left(V\right)}}\ ,$ |   | 9 |
|---|---|---|

where $B\left(V\right)$ normalizes T to the DOS and $A\left(V\right)$ describes the influence of the electric field in the tunneling gap on the decay length. Under the assumption that $A\left(V\right)$ and $B\left(V\right)$ vary slowly with tip-sample bias, the features in $\left(dI/dV\right)/\left(I/V\right)$ reflect the sample DOS, $\rho _{s}$ .

## Limitations

While STS can provide spectroscopic information with amazing spatial resolution, there are some limitations. The STM and STS lack chemical sensitivity. Since the tip-sample bias range in tunneling experiments is limited to $\pm \phi /e$ , where $\phi$ is the apparent barrier height, STM and STS only sample valence electron states. Element-specific information is generally impossible to extract from STM and STS experiments, since the chemical bond formation greatly perturbs the valence states.

At finite temperatures, the thermal broadening of the electron energy distribution due to the Fermi-distribution limits spectroscopic resolution. At $T=300\,\mathrm {K}$ , $k_{\text{B}}T\approx 0.026\,\mathrm {eV}$ , and the sample and tip energy distribution spread are both $2k_{\text{B}}T\approx 0.052\,\mathrm {eV}$ . Hence, the total energy deviation is $\Delta E\approx 0.1\,\mathrm {eV}$ . Assuming the dispersion relation for simple metals, it follows from the uncertainty relation $\Delta x\Delta k\geq 1/2$ that

| $\Delta E\geq {\frac {\hbar ^{2}k_{F}}{2M^{*}\Delta x}}=0.47{\frac {E_{F}-E_{0}}{rk_{F}}}\ ,$ |   | 10 |
|---|---|---|

where $E_{F}$ is the Fermi energy, $E_{0}$ is the bottom of the valence band, $k_{F}$ is the Fermi wave vector, and r is the lateral resolution. Since spatial resolution depends on the tip-sample spacing, smaller tip-sample spacings and higher topographic resolution blur the features in tunneling spectra.

Despite these limitations, STS and STM provide the possibility for probing the local electronic structure of metals, semiconductors, and thin insulators on a scale unobtainable with other spectroscopic methods. Additionally, topographic and spectroscopic data can be recorded simultaneously.
