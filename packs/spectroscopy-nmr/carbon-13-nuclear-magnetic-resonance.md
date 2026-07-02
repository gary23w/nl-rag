---
title: "Carbon-13 nuclear magnetic resonance"
source: https://en.wikipedia.org/wiki/Carbon-13_nuclear_magnetic_resonance
domain: spectroscopy-nmr
license: CC-BY-SA-4.0
tags: nuclear magnetic resonance, chemical shift, spin coupling, nmr spectroscopy
fetched: 2026-07-02
---

# Carbon-13 nuclear magnetic resonance

**Carbon-13 (C13) nuclear magnetic resonance** (most commonly known as **carbon-13 NMR spectroscopy** or **13C NMR spectroscopy** or sometimes simply referred to as **carbon NMR**) is the application of nuclear magnetic resonance (NMR) spectroscopy to carbon. It is analogous to proton NMR (1 H NMR) and allows the identification of carbon atoms in an organic molecule just as proton NMR identifies hydrogen atoms. 13C NMR detects only the 13 C isotope. The main carbon isotope, 12 C does not produce an NMR signal. Although about 1 million times less sensitive than 1H NMR spectroscopy, 13C NMR spectroscopy is widely used for characterizing organic and organometallic compounds, primarily because 1H-decoupled 13C-NMR spectra are simpler, have a greater sensitivity to differences in the chemical structure, and thus are better suited for identifying molecules in complex mixtures. At the same time, such spectra lack quantitative information about the atomic ratios of different types of carbon nuclei, because the nuclear Overhauser effect used in 1H-decoupled 13C-NMR spectroscopy enhances the signals from carbon atoms with a larger number of hydrogen atoms attached to them more than from carbon atoms with a smaller number of H's, and because full relaxation of 13C nuclei is usually not attained (for the sake of reducing the experiment time), and the nuclei with shorter relaxation times produce more intense signals.

The major isotope of carbon, the 12C isotope, has a spin quantum number of zero, so is not magnetically active and therefore not detectable by NMR. 13C, with a spin quantum number of 1/2, is less abundant (1.1%), whereas other popular nuclei are 100% abundant, e.g. 1H, 19F, 31P.

## Receptivity

13C NMR spectroscopy is much less sensitive (ca. by 4 orders of magnitude) to carbon than 1H NMR spectroscopy is to hydrogen, because of the lower abundance (1.1%) of 13C compared to 1H (>99%), and because of a lower (0.702 vs. 2.8) nuclear magnetic moment. Stated equivalently, the gyromagnetic ratio (6.728284 107 rad T−1 s−1) is only 1/4th that of 1H.

On the other hand, the sensitivity of 13C NMR spectroscopy benefits to some extent from nuclear Overhauser effect, which enhances signal intensity for non-quaternary 13C atoms.

## Chemical shifts

The disadvantages in "receptivity" are compensated by the high sensitivity of 13C NMR signals to the chemical environment of the nucleus, i.e. the chemical shift "dispersion" is great, covering nearly 250 ppm. This dispersion reflects the fact that non-1H nuclei are strongly influenced by excited states ("paramagnetic" contribution to shielding tensor. This paramagnetic contribution is unrelated to paramagnetism). For example, most 1H NMR signals for most organic compounds are within 15 ppm.

The chemical shift reference standard for 13C is the carbons in tetramethylsilane (TMS), whose chemical shift is set as 0.0 ppm at every temperature.

Typical chemical shifts in 13C-NMR

### Coupling constants

Homonuclear 13C-13C coupling is normally only observed in samples that are enriched with 13C. The range for one-bond 1J(13C,13C) is 50–130 Hz. Two-bond 2J(13C,13C) are near 10 Hz.

The *trends* in J(1H,13C) and J(13C,13C) are similar, except that J(1H,13C are smaller owing to the modest value of the 13C nuclear magnetic moment. Values for 1J(1H,13C) range from 125 to 250 Hz. Values for 2J(1H,13C) are near 5 Hz and often are negative.

## Implementation

### Sensitivity

As a consequence of low receptivity, 13C NMR spectroscopy suffers from complications not encountered in proton NMR spectroscopy. Many measures can be implemented to compensate for the low receptivity of this nucleus. For example, high field magnets with wider internal bores are capable of accepting larger sample tubes (typically 10 mm in diameter for 13C NMR versus 5 mm for 1H NMR). Relaxation reagents allow more rapid pulsing. A typical relaxation agent is chromium(III) acetylacetonate. For a typical sample, recording a 13C NMR spectrum may require several hours, compared to 15–30 minutes for 1H NMR. The nuclear dipole is weaker, the difference in energy between alpha and beta states is one-quarter that of proton NMR, and the Boltzmann population difference is correspondingly less. One final measure to compensate for low receptivity is isotopic enrichment.

Some NMR probes, called cryoprobes, offer 20x signal enhancement relative to ordinary NMR probes. In cryoprobes, the RF generating and receiving electronics are maintained at ~ 25K using helium gas, which greatly enhances their sensitivity. The trade-off is that cryoprobes are costly.

### Coupling modes

Another potential complication results from the presence of large one bond J-coupling constants between carbon and hydrogen (typically from 100 to 250 Hz). While potentially informative, these couplings can complicate the spectra and reduce sensitivity. For these reasons, 13C-NMR spectra are usually recorded with proton NMR decoupling. Couplings between carbons can be ignored due to the low natural abundance of 13C. Hence in contrast to typical proton NMR spectra, which show multiplets for each proton position, carbon NMR spectra show a single peak for each chemically non-equivalent carbon atom.

In further contrast to 1H NMR, the intensities of the signals are often not proportional to the number of equivalent 13C atoms. Instead, signal intensity is strongly influenced by (and proportional to) the number of surrounding spins (typically 1H). Integrations are more quantitative if the delay times are long, i.e. if the delay times greatly exceed relaxation times.

The most common modes of recording 13C spectra are proton-noise decoupling (also known as noise-, proton-, or broadband- decoupling), off-resonance decoupling, and gated decoupling. These modes are meant to address the large J values for 13C - H (110–320 Hz), 13C - C - H (5–60 Hz), and 13C - C - C - H (5–25 Hz) which otherwise make completely proton coupled 13C spectra difficult to interpret.

With proton-noise decoupling, in which most spectra are run, a noise decoupler strongly irradiates the sample with a broad (approximately 1000 Hz) range of radio frequencies covering the range (such as 100 MHz for a 23,486 gauss field) at which protons change their nuclear spin. The rapid changes in proton spin create an effective heteronuclear decoupling, increasing carbon signal strength on account of the nuclear Overhauser effect (NOE) and simplifying the spectrum so that each non-equivalent carbon produces a singlet peak.

Both the atoms, carbon and hydrogen exhibit spins and are NMR active. The nuclear Overhauser Effect is in general, showing up when one of two different types of atoms is irradiated while the NMR spectrum of the other type is determined. If the absorption intensities of the observed (i.e., non-irradiated) atom change, enhancement occurs. The effect can be either positive or negative, depending on which atom types are involved.

The relative intensities are unreliable because some carbons have a larger spin-lattice relaxation time and others have weaker NOE enhancement.

In gated decoupling, the noise decoupler is gated on early in the free induction delay but gated off for the pulse delay. This largely prevents NOE enhancement, allowing the strength of individual 13C peaks to be meaningfully compared by integration, at a cost of half to two-thirds of the overall sensitivity.

With off-resonance decoupling, the noise decoupler irradiates the sample at 1000–2000 Hz upfield or 2000–3000 Hz downfield of the proton resonance frequency. This retains couplings between protons immediately adjacent to 13C atoms but most often removes the others, allowing narrow multiplets to be visualized with one extra peak per bound proton (unless bound methylene protons are non-equivalent, in which case a pair of doublets may be observed).

## Distortionless enhancement by polarization transfer spectra

**Distortionless enhancement by polarization transfer** (DEPT) is an NMR method used for determining the presence of primary, secondary and tertiary carbon atoms. The DEPT experiment differentiates between CH, CH2 and CH3 groups by variation of the selection angle parameter (the tip angle of the final 1H pulse): 135° angle gives all CH and CH3 in a phase opposite to CH2; 90° angle gives only CH groups, the others being suppressed; 45° angle gives all carbons with attached protons (regardless of number) in phase.

Signals from quaternary carbons and other carbons with no attached protons are always absent (due to the lack of attached protons).

The polarization transfer from 1H to 13C has the secondary advantage of increasing the sensitivity over the normal 13C spectrum (which has a modest enhancement from the nuclear Overhauser effect (NOE) due to the 1H decoupling).

## Attached proton test spectra

Another useful way of determining how many protons a carbon in a molecule is bonded to is to use an **attached proton test** (APT), which distinguishes between carbon atoms with even or odd number of attached hydrogens. A proper spin-echo sequence is able to distinguish between S, I2S and I1S, I3S spin systems: the first will appear as positive peaks in the spectrum, while the latter as negative peaks (pointing downwards), while retaining relative simplicity in the spectrum since it is still broadband proton decoupled.

Even though this technique does not distinguish fully between CHn groups, it is so easy and reliable that it is frequently employed as a first attempt to assign peaks in the spectrum and elucidate the structure. Additionally, signals from quaternary carbons and other carbons with no attached protons are still detectable, so in many cases an additional conventional 13C spectrum is not required, which is an advantage over DEPT. It is, however, sometimes possible that a CH and CH2 signal have coincidentally equivalent chemical shifts resulting in annulment in the APT spectrum due to the opposite phases. For this reason the conventional 13C{1H} spectrum or HSQC are occasionally also acquired.
