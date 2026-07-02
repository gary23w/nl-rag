---
title: "Quantum efficiency"
source: https://en.wikipedia.org/wiki/Quantum_efficiency
domain: image-sensors-cmos
license: CC-BY-SA-4.0
tags: image sensor, active-pixel sensor, bayer filter, rolling shutter
fetched: 2026-07-02
---

# Quantum efficiency

The **quantum efficiency** (**QE**) of a photodetector is a measure of its electrical response to light. Another name for it is **incident photon to converted electron** (**IPCE**) **ratio**.

In a charge-coupled device (CCD) or other photodetector, quantum efficiency is the ratio between the number of charge carriers collected at either terminal and the number of photons hitting the device's photoreactive surface. As a ratio, QE is dimensionless, but it is closely related to the responsivity, which is expressed in amps per watt. Since the energy of a photon is inversely proportional to its wavelength, QE is often measured over a range of different wavelengths to characterize a device's efficiency at each photon energy level. For typical semiconductor photodetectors, QE drops to zero for photons whose energy is below the band gap. A photographic film typically has a QE of much less than 10%, while CCDs can have a QE of well over 90% at some wavelengths.

## Solar cells

A solar cell's quantum efficiency value indicates the amount of current that the cell will produce when irradiated by photons of a particular wavelength. If the cell's quantum efficiency is integrated over the whole solar electromagnetic spectrum, one can evaluate the amount of current that the cell will produce when exposed to sunlight. The ratio between this energy-production value and the highest possible energy-production value for the cell (i.e., if the QE were 100% over the whole spectrum) gives the cell's overall energy conversion efficiency value. Note that in the event of multiple exciton generation (MEG), quantum efficiencies of greater than 100% may be achieved since the incident photons have more than twice the band gap energy and can create two or more electron-hole pairs per incident photon.

### Types

Two types of quantum efficiency of a solar cell are often considered:

- **External quantum efficiency (EQE)** is the ratio of the number of charge carriers collected by the solar cell to the number of photons of a given energy *shining on the solar cell from outside* (incident photons).
- **Internal quantum efficiency (IQE)** is the ratio of the number of charge carriers collected by the solar cell to the number of photons of a given energy that shine on the solar cell from outside *and* are absorbed by the cell.

The IQE is always larger than the EQE in the visible spectrum. A low IQE indicates that the active layer of the solar cell is unable to make good use of the photons, most likely due to poor carrier collection efficiency. To measure the IQE, one first measures the EQE of the solar device, then measures its transmission and reflection, and combines these data to infer the IQE. ${\text{EQE}}={\frac {\text{electrons/sec}}{\text{photons/sec}}}={\frac {{\text{(current)}}/{\text{(charge of one electron)}}}{({\text{total power of photons}})/({\text{energy of one photon}})}}$ ${\text{IQE}}={\frac {\text{electrons/sec}}{\text{absorbed photons/sec}}}={\frac {\text{EQE}}{\text{1-Reflection-Transmission}}}$

The external quantum efficiency therefore depends on both the absorption of light and the collection of charges. Once a photon has been absorbed and has generated an electron-hole pair, these charges must be separated and collected at the junction. A "good" material avoids charge recombination. Charge recombination causes a drop in the external quantum efficiency.

The ideal quantum efficiency graph has a square shape, where the QE value is fairly constant across the entire spectrum of wavelengths measured. However, the QE for most solar cells is reduced because of the effects of recombination, where charge carriers are not able to move into an external circuit. The same mechanisms that affect the collection probability also affect the QE. For example, modifying the front surface can affect carriers generated near the surface. Highly doped front surface layers can also cause 'free carrier absorption' which reduces QE in the longer wavelengths. And because high-energy (blue) light is absorbed very close to the surface, considerable recombination at the front surface will affect the "blue" portion of the QE. Similarly, lower energy (green) light is absorbed in the bulk of a solar cell, and a low diffusion length will affect the collection probability from the solar cell bulk, reducing the QE in the green portion of the spectrum. Generally, solar cells on the market today do not produce much electricity from ultraviolet and infrared light (<400 nm and >1100 nm wavelengths, respectively); these wavelengths of light are either filtered out or are absorbed by the cell, thus heating the cell. That heat is wasted energy, and could damage the cell.

## Image sensors

Quantum efficiency (QE) is the fraction of photon flux that contributes to the photocurrent in a photodetector or a pixel. Quantum efficiency is one of the most important parameters used to evaluate the quality of a detector and is often called the spectral response to reflect its wavelength dependence. It is defined as the number of signal electrons created per incident photon. In some cases it can exceed 100% (i.e. when more than one electron is created per incident photon).

### EQE mapping

Conventional measurement of the EQE will give the efficiency of the overall device. However it is often useful to have a map of the EQE over large area of the device. This mapping provides an efficient way to visualize the homogeneity and/or the defects in the sample. It was realized by researchers from the Institute of Researcher and Development on Photovoltaic Energy (IRDEP) who calculated the EQE mapping from electroluminescence measurements taken with a hyperspectral imager.

## Spectral responsivity

Spectral responsivity is a similar measurement, but it has different units: amperes per watt (A/W); (i.e. how much current comes out of the device per unit of incident light power). Responsivity is ordinarily specified for monochromatic light (i.e. light of a single wavelength). Both the quantum efficiency and the responsivity are functions of the photons' wavelength (indicated by the subscript λ).

To convert from responsivity (*Rλ*, in A/W) to QEλ (on a scale 0 to 1): $QE_{\lambda }={\frac {R_{\lambda }}{\lambda }}\times {\frac {hc}{e}}\approx {\frac {R_{\lambda }}{\lambda }}{\times }(1240\;\mathrm {W\cdot {nm}/A} )$ where λ is the wavelength in nm, *h* is the Planck constant, *c* is the speed of light in vacuum, and *e* is the elementary charge. Note that the unit W/A (watts per ampere) is equivalent to V (volts).

### Determination

$QE_{\lambda }=\eta ={\frac {N_{e}}{N_{\nu }}}$ where $N_{e}$ = number of electrons produced, $N_{\nu }$ = number of photons absorbed. ${\frac {N_{\nu }}{t}}=\Phi _{o}{\frac {\lambda }{hc}}$

Assuming each photon absorbed in the depletion layer produces a viable electron-hole pair, and all other photons do not, ${\frac {N_{e}}{t}}=\Phi _{\xi }{\frac {\lambda }{hc}}$ where *t* is the measurement time (in seconds), $\Phi _{o}$ = incident optical power in watts, $\Phi _{\xi }$ = optical power absorbed in depletion layer, also in watts.
