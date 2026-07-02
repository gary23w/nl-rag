---
title: "Chemical shift"
source: https://en.wikipedia.org/wiki/Chemical_shift
domain: spectroscopy-nmr
license: CC-BY-SA-4.0
tags: nuclear magnetic resonance, chemical shift, spin coupling, nmr spectroscopy
fetched: 2026-07-02
---

# Chemical shift

In nuclear magnetic resonance (NMR) spectroscopy, the **chemical shift** is the resonant frequency of an atomic nucleus relative to a standard in a magnetic field. Often the position and number of chemical shifts are diagnostic of the structure of a molecule. Chemical shifts are also used to describe signals in other forms of spectroscopy such as photoemission spectroscopy.

Some atomic nuclei possess a magnetic moment (nuclear spin), which gives rise to different energy levels and resonance frequencies in a magnetic field. The total magnetic field experienced by a nucleus includes local magnetic fields induced by currents of electrons in the molecular orbitals (electrons have a magnetic moment themselves). The electron distribution of the same type of nucleus (e.g. 1H, 13C, 15N) usually varies according to the local geometry (binding partners, bond lengths, angles between bonds, and so on), and with it the local magnetic field at each nucleus. This is reflected in the spin energy levels (and resonance frequencies). The variations of nuclear magnetic resonance frequencies of the same kind of nucleus, due to variations in the electron distribution, is called the chemical shift. The size of the chemical shift is given with respect to a reference frequency or reference sample (see also chemical shift referencing), usually a molecule with a barely distorted electron distribution.

## Operating frequency

The operating (or Larmor) frequency $\omega _{0}$ of a magnet (usually quoted as absolute value in MHz) is calculated from the Larmor equation

$\omega _{0}=-\gamma B_{0},$

where *B*0 is the induction of the magnet (SI units of tesla), and $\gamma$ is the magnetogyric ratio of the nucleus — an empirically measured fundamental constant determined by the details of the structure of each nucleus. For example, the proton operating frequency for a 1-tesla magnet is calculated as

$\omega _{0}=-4.258\cdot 10^{7}~{\frac {\text{Hz}}{\text{T}}}\times 1.000~{\text{T}}=-42.58~{\text{MHz}}.$

MRI scanners are often referred to by their field strengths *B*0 (e.g. "a 7 T scanner"), whereas NMR spectrometers are commonly referred to by the corresponding proton Larmor frequency (e.g. "a 300 MHz spectrometer", which has a *B*0 of 7 T). While chemical shift is referenced in order that the units are equivalent across different field strengths, the actual frequency separation in hertz scales with field strength (*B*0). As a result, the difference of chemical shift between two signals (ppm) represents a larger number of hertz on machines that have larger *B*0, and therefore the signals are less likely to be overlapping in the resulting spectrum. This increased resolution is a significant advantage for analysis. Higher-field machines are also favoured on account of having intrinsically higher signal arising from the Boltzmann distribution of magnetic spin states.

## Chemical shift referencing

Chemical shift δ is usually expressed in parts per million (ppm) by frequency, because it is calculated from

$\delta ={\frac {\nu _{\text{sample}}-\nu _{\text{ref}}}{\nu _{\text{ref}}}},$

where *ν*sample is the absolute resonance frequency of the sample, and *ν*ref is the absolute resonance frequency of a standard reference compound, measured in the same applied magnetic field *B*0. Since the numerator is usually expressed in hertz, and the denominator in megahertz, δ is expressed in ppm.

The detected frequencies (in Hz) for 1H, 13C, and 29Si nuclei are usually referenced against TMS (tetramethylsilane), TSP (trimethylsilylpropanoic acid), or DSS, which by the definition above have a chemical shift of zero if chosen as the reference. Other standard materials are used for setting the chemical shift for other nuclei.

Thus an NMR signal observed at a frequency 300 Hz higher than the signal from TMS, where the TMS resonance frequency is 300 MHz, has a chemical shift of

${\frac {300~{\text{Hz}}}{300\times 10^{6}~{\text{Hz}}}}=1\times 10^{-6}=1~{\text{ppm}}.$

Although the absolute resonance frequency depends on the applied magnetic field, the chemical shift is independent of external magnetic field strength. On the other hand, the resolution of NMR will increase with applied magnetic field.

### Tau scale

In early proton NMR publications, the τ scale was also used, defined as τ = 10 ppm - δTMS. It fell out of use around 1970.

### Referencing methods

Practically speaking, diverse methods may be used to reference chemical shifts in an NMR experiment, which can be subdivided into *indirect* and *direct* referencing methods. Indirect referencing uses a channel other than the one of interest to adjust chemical shift scale correctly, i.e. the solvent signal in the deuterium (lock) channel can be used to reference the a 1H NMR spectrum. Both indirect and direct referencing can be done as three different procedures:

1. **Internal referencing**, where the reference compound is added directly to the system under study." In this common practice, users adjust residual solvent signals of 1H or 13C NMR spectra with calibrated spectral tables. If substances other than the solvent itself are used for internal referencing, the sample has to be combined with the reference compound, which may affect the chemical shifts.
2. **External referencing**, involving sample and reference contained separately in coaxial cylindrical tubes. With this procedure, the reference signal is still visible in the spectrum of interest, although the reference and the sample are physically separated by a glass wall. Magnetic susceptibility differences between the sample and the reference phase need to be corrected theoretically, which lowers the practicality of this procedure.
3. **Substitution method**: The use of separate cylindrical tubes for the sample and the reference compound, with (in principle) spectra recorded individually for each. Similar to external referencing, this method allows referencing without sample contamination. If field/frequency locking via the 2H signal of the deuterated solvent is used and the solvents of reference and analyte are the same, the use of this methods is straightforward. Problems may arise if different solvents are used for the reference compound and the sample as (just like for external referencing) magnetic susceptibility differences need to be corrected theoretically. If this method is used without field/frequency locking, shimming procedures between the sample and the reference need to be avoided as they change the applied magnetic field (and thereby influence the chemical shift).

Modern NMR spectrometers commonly make use of the absolute scale, which defines the 1H signal of TMS as 0 ppm in proton NMR and the center frequencies of all other nuclei as percentage of the TMS resonance frequency:

$\Xi [\%]=100\times {\frac {\upsilon _{X}^{\text{obs}}}{\upsilon _{\text{TMS}}^{\text{obs}}}}.$

The use of the deuterium (lock) channel, so the 2H signal of the deuterated solvent, and the Ξ value of the absolute scale is a form of internal referencing and is particularly useful in heteronuclear NMR spectroscopy as local reference compounds may not always be available or easily used (i.e. liquid NH3 for 15N NMR spectroscopy). This system, however, relies on accurately determined 2H NMR chemical shifts enlisted in the spectrometer software and correctly determined Ξ values by IUPAC. A recent study for 19F NMR spectroscopy revealed that the use of the absolute scale and lock-based internal referencing led to errors in chemical shifts. These may be negated by inclusion of calibrated reference compounds.

## The induced magnetic field

The electrons around a nucleus will circulate in a magnetic field and create a secondary induced magnetic field. This field opposes the applied field as stipulated by Lenz's law and atoms with higher induced fields (i.e., higher electron density) are therefore called *shielded*, relative to those with lower electron density. Electron-donating alkyl groups, for example, lead to increased shielding whereas electron-withdrawing substituents such as nitro groups lead to *deshielding* of the nucleus. Not only substituents cause local induced fields. Bonding electrons can also lead to shielding and deshielding effects. A striking example of this is the pi bonds in benzene. Circular current through the hyperconjugated system causes a shielding effect at the molecule's center and a deshielding effect at its edges. Trends in chemical shift are explained based on the degree of shielding or deshielding.

Nuclei are found to resonate in a wide range to the left (or more rare to the right) of the internal standard. When a signal is found with a higher chemical shift:

- The applied effective magnetic field is lower, if the resonance frequency is fixed (as in old traditional CW spectrometers)
- The frequency is higher, when the applied magnetic field is static (normal case in FT spectrometers)
- The nucleus is more deshielded
- The signal or shift is **downfield** or at **low field** or paramagnetic.

Conversely a lower chemical shift is called a **diamagnetic shift**, and is **upfield** and more shielded.

## Diamagnetic shielding

In real molecules protons are surrounded by a cloud of charge due to adjacent bonds and atoms. In an applied magnetic field (**B**0) electrons circulate and produce an induced field (**B**i) which opposes the applied field. The effective field at the nucleus will be **B** = **B**0 − **B**i. The nucleus is said to be experiencing a diamagnetic shielding.

## Factors causing chemical shifts

Important factors influencing chemical shift are electron density, electronegativity of neighboring groups and anisotropic induced magnetic field effects.

Electron density shields a nucleus from the external field. For example, in proton NMR the electron-poor tropylium ion has its protons downfield at 9.17 ppm, those of the electron-rich cyclooctatetraenyl anion move upfield to 6.75 ppm and its dianion even more upfield to 5.56 ppm.

A nucleus in the vicinity of an electronegative atom experiences reduced electron density and the nucleus is therefore deshielded. In proton NMR of methyl halides (CH3X) the chemical shift of the methyl protons increase in the order I < Br < Cl < F from 2.16 ppm to 4.26 ppm reflecting this trend. In carbon NMR the chemical shift of the carbon nuclei increase in the same order from around −10 ppm to 70 ppm. Also when the electronegative atom is removed further away the effect diminishes until it can be observed no longer.

Anisotropic induced magnetic field effects are the result of a local induced magnetic field experienced by a nucleus resulting from circulating electrons that can either be paramagnetic when it is parallel to the applied field or diamagnetic when it is opposed to it. It is observed in alkenes where the double bond is oriented perpendicular to the external field with pi electrons likewise circulating at right angles. The induced magnetic field lines are parallel to the external field at the location of the alkene protons which therefore shift downfield to a 4.5 ppm to 7.5 ppm range. The three-dimensional space where a diamagnetic shift is called the shielding zone with a cone-like shape aligned with the external field.

The protons in aromatic compounds are shifted downfield even further with a signal for benzene at 7.73 ppm as a consequence of a diamagnetic ring current.

Alkyne protons by contrast resonate at high field in a 2–3 ppm range. For alkynes the most effective orientation is the external field in parallel with electrons circulation around the triple bond. In this way the acetylenic protons are located in the cone-shaped shielding zone hence the upfield shift.

## Magnetic properties of most common nuclei

1H and 13C are not the only nuclei susceptible to NMR experiments. A number of different nuclei can also be detected, although the use of such techniques is generally rare due to small relative sensitivities in NMR experiments (compared to 1H) of the nuclei in question, the other factor for rare use being their slender representation in nature and organic compounds.

| Isotope | Occurrence in nature (%) | Spin number I | Magnetic moment μ (*μ*N) | Electric quadrupole moment (e × 10−24 cm2) | Operating frequency at 7 T (MHz) | Relative sensitivity |
|---|---|---|---|---|---|---|
| 1H | 099.984 | ⁠1/2⁠ | −2.79628 | −0 | 300.13 | 1 |
| 2H | 000.016 | 1 | −0.85739 | −0.0028 | 046.07 | 0.0964 |
| 10B | 018.8 | 3 | −1.8005 | −0.074 | 032.25 | 0.0199 |
| 11B | 081.2 | ⁠3/2⁠ | −2.6880 | −0.026 | 096.29 | 0.165 |
| 12C | 098.9 | 0 | −0 | −0 | 000 | 0 |
| 13C | 001.1 | ⁠1/2⁠ | −0.70220 | −0 | 075.47 | 0.0159 |
| 14N | 099.64 | 1 | −0.40358 | −0.071 | 021.68 | 0.00101 |
| 15N | 000.37 | ⁠1/2⁠ | −0.28304 | −0 | 030.41 | 0.00104 |
| 16O | 099.76 | 0 | −0 | −0 | 000 | 0 |
| 17O | 000.0317 | ⁠5/2⁠ | −1.8930 | −0.0040 | 040.69 | 0.0291 |
| 19F | 100 | ⁠1/2⁠ | −2.6273 | −0 | 282.40 | 0.834 |
| 28Si | 092.28 | 0 | −0 | −0 | 000 | 0 |
| 29Si | 004.70 | ⁠1/2⁠ | −0.5548 | −0 | 059.63 | 0.0785 |
| 31P | 100 | ⁠1/2⁠ | −1.1205 | −0 | 121.49 | 0.0664 |
| 35Cl | 075.4 | ⁠3/2⁠ | −0.92091 | −0.079 | 029.41 | 0.0047 |
| 37Cl | 024.6 | ⁠3/2⁠ | −0.68330 | −0.062 | 024.48 | 0.0027 |

1H, 13C, 15N, 19F and 31P are the five nuclei that have the greatest importance in NMR experiments:

- 1H because of high sensitivity and vast occurrence in organic compounds
- 13C because of being the key component of all organic compounds despite occurring at a low abundance (1.1%) compared to the major isotope of carbon 12C, which has a spin of 0 and therefore is NMR-inactive.
- 15N because of being a key component of important biomolecules such as proteins and DNA
- 19F because of high relative sensitivity
- 31P because of frequent occurrence in organic compounds and moderate relative sensitivity

## Chemical shift manipulation

In general, the associated increased signal-to-noise and resolution has driven a move towards increasingly high field strengths. In limited cases, however, lower fields are preferred; examples are for systems in chemical exchange, where the speed of the exchange relative to the NMR experiment can cause additional and confounding linewidth broadening. Similarly, while avoidance of second order coupling is generally preferred, this information can be useful for elucidation of chemical structures. Using refocussing pulses placed between recording of successive points of the free induction decay, in an analogous fashion to the spin echo technique in MRI, the chemical shift evolution can be scaled to provide apparent low-field spectra on a high-field spectrometer. In a similar fashion, it is possible to upscale the effect of J-coupling relative to the chemical shift using pulse sequences that include additional J-coupling evolution periods interspersed with conventional spin evolutions.

## Other chemical shifts

The Knight shift (first reported in 1949) and Shoolery's rule are observed with pure metals and methylene groups, respectively. The NMR chemical shift in its present-day meaning first appeared in journals in 1950. Chemical shifts with a different meaning appear in X-ray photoelectron spectroscopy as the shift in atomic core-level energy due to a specific chemical environment. The term is also used in Mössbauer spectroscopy, where similarly to NMR it refers to a shift in peak position due to the local chemical bonding environment. As is the case for NMR the chemical shift reflects the electron density at the atomic nucleus.
