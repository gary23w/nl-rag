---
title: "Inelastic mean free path"
source: https://en.wikipedia.org/wiki/Inelastic_mean_free_path
domain: x-ray-photoelectron-spectroscopy
license: CC-BY-SA-4.0
tags: photoemission, surface analysis, binding energy, chemical state
fetched: 2026-07-02
---

# Inelastic mean free path

The **inelastic mean free path** (**IMFP**) is an index of how far an electron on average travels through a solid before losing energy.

If a monochromatic, primary beam of electrons is incident on a solid surface, the majority of incident electrons lose their energy because they interact strongly with matter, leading to plasmon excitation, electron-hole pair formation, and vibrational excitation. The intensity of the primary electrons, *I*0, is damped as a function of the distance, d, into the solid. The intensity decay can be expressed as follows:

$I(d)=I_{0}\ e^{-d\ /\lambda (E)}$

where *I*(*d*) is the intensity after the primary electron beam has traveled through the solid to a distance d. The parameter λ(*E*), termed the inelastic mean free path (IMFP), is defined as the distance an electron beam can travel before its intensity decays to 1/e of its initial value. (Note that this is equation is closely related to the Beer–Lambert law.)

The inelastic mean free path of electrons can roughly be described by a universal curve that is the same for all materials.

The knowledge of the IMFP is indispensable for several electron spectroscopy and microscopy measurements.

## Applications of the IMFP in XPS

Following, the IMFP is employed to calculate the effective attenuation length (EAL), the mean escape depth (MED) and the information depth (ID). Besides, one can utilize the IMFP to make matrix corrections for the relative sensitivity factor in quantitative surface analysis. Moreover, the IMFP is an important parameter in Monte Carlo simulations of photoelectron transport in matter.

## Calculations of the IMFP

Calculations of the IMFP are mostly based on the algorithm (full Penn algorithm, FPA) developed by Penn, experimental optical constants or calculated optical data (for compounds). The FPA considers an inelastic scattering event and the dependence of the energy-loss function (EFL) on momentum transfer which describes the probability for inelastic scattering as a function of momentum transfer.

## Experimental measurements of the IMFP

To measure the IMFP, one well known method is elastic-peak electron spectroscopy (EPES). This method measures the intensity of elastically backscattered electrons with a certain energy from a sample material in a certain direction. Applying a similar technique to materials whose IMFP is known, the measurements are compared with the results from the Monte Carlo simulations under the same conditions. Thus, one obtains the IMFP of a certain material in a certain energy spectrum. EPES measurements show a root-mean-square (RMS) difference between 12% and 17% from the theoretical expected values. Calculated and experimental results show higher agreement for higher energies.

For electron energies in the range 30 keV – 1 MeV, IMFP can be directly measured by electron energy loss spectroscopy inside a transmission electron microscope, provided the sample thickness is known. Such measurements reveal that IMFP in elemental solids is not a smooth, but an oscillatory function of the atomic number.

For energies below 100 eV, IMFP can be evaluated in high-energy secondary electron yield (SEY) experiments. Therefore, the SEY for an arbitrary incident energy between 0.1 keV-10 keV is analyzed. According to these experiments, a Monte Carlo model can be used to simulate the SEYs and determine the IMFP below 100 eV.

## Predictive formulas

Using the dielectric formalism, the IMFP $\lambda ^{-1}$ can be calculated by solving the following integral:

| $\lambda ^{-1}={\frac {1}{\pi E}}\int _{\omega _{\mathrm {min} }}^{\omega _{\mathrm {max} }}\,d\omega \int _{k_{-}}^{k_{+}}\mathrm {Im} \left({\frac {-1}{\epsilon (k,\omega )}}\right)\,{\frac {dk}{k}}$ |   | 1 |
|---|---|---|

with the minimum (maximum) energy loss $\omega _{\mathrm {min} }$ ( $\omega _{\mathrm {max} }$ ), the dielectric function $\epsilon$ , the energy loss function (ELF) $\mathrm {Im} ({\frac {-1}{\epsilon (k,\omega )}})$ and the smallest and largest momentum transfer $k_{\pm }={\sqrt {2E}}\pm {\sqrt {2(E-\omega )}}$ . In general, solving this integral is quite challenging and only applies for energies above 100 eV. Thus, (semi)empirical formulas were introduced to determine the IMFP.

A first approach is to calculate the IMFP by an approximate form of the relativistic Bethe equation for inelastic scattering of electrons in matter. Equation **2** holds for energies between 50 eV and 200 keV:

| $\lambda ^{-1}={\frac {\alpha (E)E}{E_{p}^{2}(\beta \ln {(\gamma \alpha (E)E)-(C/E)+(D/E)^{2}})}}$ |   | 2 |
|---|---|---|

with

$\alpha (E)={\frac {1+{\frac {E}{2m_{e}c^{2}}}}{(1+{\frac {E}{m_{e}c^{2}}})^{2}}}={\frac {1+{\frac {E}{1021}}999.8}{(1+{\frac {E}{510}}998.9)^{2}}}$

and

$E_{p}=28.816\left({\frac {N_{\nu }\rho }{M}}\right)^{0.5}(\mathrm {eV} )$

and the electron energy E in eV above the Fermi level (conductors) or above the bottom of the conduction band (non-conductors). $m_{e}$ is the electron mass, c the vacuum velocity of light, $N_{\nu }$ is the number of valence electrons per atom or molecule, $\rho$ describes the density (in $\mathrm {\frac {g}{cm^{3}}}$ ), M is the atomic or molecular weight and $\beta$ , $\gamma$ , C and D are parameters determined in the following. Equation **2** calculates the IMFP and its dependence on the electron energy in condensed matter.

Equation **2** was further developed to find the relations for the parameters $\beta$ , $\gamma$ , C and D for energies between 50 eV and 2 keV:

| $\beta =-1.0+9.44/(E_{p}^{2}+E_{g}^{2})^{0.5}+0.69\rho ^{0.1}(\mathrm {eV^{-1}} \mathrm {nm^{-1}} )$ |   | 3 |
|---|---|---|

- $\gamma =0.191\rho ^{-0.5}(\mathrm {eV^{-1}} )$
- $C=19.7-9.1U(\mathrm {nm^{-1}} )$
- $D=534-208U(\mathrm {eV} \mathrm {nm^{-1}} )$
- $U={\frac {N_{\nu }\rho }{M}}=(E_{p}/28.816)^{2}$

Here, the bandgap energy $E_{g}$ is given in eV. Equation **2** an **3** are also known as the TTP-2M equations and are in general applicable for energies between 50 eV and 200 keV. Neglecting a few materials (diamond, graphite, Cs, cubic-BN and hexagonal BN) that are not following these equations (due to deviations in $\beta$ ), the TTP-2M equations show precise agreement with the measurements.

Another approach based on Equation **2** to determine the IMFP is the S1 formula. This formula can be applied for energies between 100 eV and 10 keV:

$\lambda ^{-1}={\frac {(4+0.44Z^{0.5}+0.104E^{0.872})a^{1.7}}{Z^{0.3}(1-W)}}$

with the atomic number Z (average atomic number for a compound), $W=0.06H$ or $W=0.02E_{g}$ ( H is the heat of formation of a compound in eV per atom) and the average atomic spacing a :

$a^{3}={\frac {10^{21}M}{\rho N_{A}(g+h)}}(\mathrm {nm^{3}} )$

with the Avogadro constant $N_{A}$ and the stoichiometric coefficients g and h describing binary compounds $G_{g}H_{h}$ . In this case, the atomic number becomes

$Z={\frac {gZ_{g}+hZ_{h}}{g+h}}$

with the atomic numbers $Z_{g}$ and $Z_{h}$ of the two constituents. This S1 formula shows higher agreement with measurements compared to Equation **2**.

Calculating the IMFP with either the TTP-2M formula or the S1 formula requires different knowledge of some parameters. Applying the TTP-2M formula one needs to know M , $\rho$ and $N_{\nu }$ for conducting materials (and also $E_{g}$ for non-conductors). Employing S1 formula, knowledge of the atomic number Z (average atomic number for compounds), M and $\rho$ is required for conductors. If non-conducting materials are considered, one also needs to know either $E_{g}$ or H .

An analytical formula for calculating the IMFP down to 50 eV was proposed in 2021. Therefore, an exponential term was added to an analytical formula already derived from **1** that was applicible for energies down to 500 eV:

| $\lambda ^{-1}={\frac {1}{2\pi a_{0}E}}\left(A\ln {\frac {4E}{I}}-{\frac {7C}{4E}}(1-\exp {(-AE/2C)})\right)$ |   | 4 |
|---|---|---|

For relativistic electrons it holds:

| $\lambda ^{-1}={\frac {1}{\pi a_{0}v^{2}}}\left(A\ln {\frac {2v^{2}}{I}}-{\frac {7C}{2v^{2}}}(1-\exp {(-Av^{2}/4C)})\right)$ |   | 5 |
|---|---|---|

with the electron velocity v , $v^{2}=c^{2}\tau (\tau +2)/(\tau +1)^{2}$ and $\tau =E/c^{2}$ . c denotes the velocity of light. $\lambda$ and $a_{0}$ are given in nanometers. The constants in **4** and **5** are defined as following:

- $A=\int _{0}^{\infty }\mathrm {Im} \left({\frac {-1}{\epsilon (\omega )}}\right)\,d\omega$
- $A\ln {(I)}=\int _{0}^{\infty }\mathrm {Im} \left({\frac {-1}{\epsilon (\omega )}}\right)\ln {(\omega )}\,d\omega$
- $C=\int _{0}^{\infty }\mathrm {Im} \left({\frac {-1}{\epsilon (\omega )}}\right)\omega \,d\omega$

## IMFP data

IMFP data can be collected from the National Institute of Standards and Technology (NIST) Electron Inelastic-Mean-Free-Path Database or the NIST Database for the Simulation of Electron Spectra for Surface Analysis (SESSA). The data contains IMFPs determined by EPES for energies below 2 keV. Otherwise, IMFPs can be determined from the TPP-2M or the S1 formula.
