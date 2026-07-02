---
title: "Extreme ultraviolet lithography (part 2/2)"
source: https://en.wikipedia.org/wiki/Extreme_ultraviolet_lithography
domain: photolithography
license: CC-BY-SA-4.0
tags: semiconductor photolithography, extreme ultraviolet lithography, photomask fabrication, photoresist patterning
fetched: 2026-07-02
part: 2/2
---

## Mask defects

Reducing defects on extreme ultraviolet (EUV) masks is currently one of the most critical issues to be addressed for commercialization of EUV lithography. Defects can be buried underneath or within the multilayer stack or be on top of the multilayer stack. Mesas or protrusions form on the sputtering targets used for multilayer deposition, which may fall off as particles during the multilayer deposition. In fact, defects of atomic scale height (0.3–0.5 nm) with 100 nm FWHM can still be printable by exhibiting 10% CD impact. IBM and Toppan reported at Photomask Japan 2015 that smaller defects, e.g., 50 nm size, can have 10% CD impact even with 0.6 nm height, yet remain undetectable.

Furthermore, the edge of a phase defect will further reduce reflectivity by more than 10% if its deviation from flatness exceeds 3 degrees, due to the deviation from the target angle of incidence of 84 degrees with respect to the surface. Even if the defect height is shallow, the edge still deforms the overlying multilayer, producing an extended region where the multilayer is sloped. The more abrupt the deformation, the narrower the defect edge extension, the greater the loss in reflectivity.

EUV mask defect repair is also more complicated due to the across-slit illumination variation mentioned above. Due to the varying shadowing sensitivity across the slit, the repair deposition height must be controlled very carefully, being different at different positions across the EUV mask illumination slit.

### Multilayer reflectivity random variations

GlobalFoundries and Lawrence Berkeley Labs carried out a Monte Carlo study to simulate the effects of intermixing between the molybdenum (Mo) and silicon (Si) layers in the multilayer that is used to reflect EUV light from the EUV mask. The results indicated high sensitivity to the atomic-scale variations of layer thickness. Such variations could not be detected by wide-area reflectivity measurements but would be significant on the scale of the critical dimension (CD). The local variation of reflectivity could be on the order of 10% for a few nm standard deviation.

### Multilayer damage

Multiple EUV pulses at less than 10 mJ/cm2 could accumulate damage to a Ru-capped Mo/Si multilayer mirror optic element. The angle of incidence was 16° or 0.28 rads, which is within the range of angles for a 0.33 NA optical system.

### Pellicles

Production EUV tools need a pellicle to protect the mask from contamination. Pellicles are normally expected to protect the mask from particles during transport, entry into or exit from the exposure chamber, as well as the exposure itself. Without pellicles, particle adders would reduce yield, which has not been an issue for conventional optical lithography with 193 nm light and pellicles. However, for EUV, the feasibility of pellicle use is severely challenged, due to the required thinness of the shielding films to prevent excessive EUV absorption. Particle contamination would be prohibitive if pellicles were not stable above 200 W, i.e., the targeted power for manufacturing.

Heating of the EUV mask pellicle (film temperature up to 750 K for 80 W incident power) is a significant concern, due to the resulting deformation and transmission decrease. ASML developed a 70 nm thick polysilicon pellicle membrane, which allows EUV transmission of 82%; however, less than half of the membranes survived expected EUV power levels. SiNx pellicle membranes also failed at 82 W equivalent EUV source power levels. At target 250 W levels, the pellicle is expected to reach 686 degrees Celsius, well over the melting point of aluminum. Alternative materials need to allow sufficient transmission as well as maintain mechanical and thermal stability. However, graphite, graphene or other carbon nanomaterials (nanosheets, nanotubes) are damaged by EUV due to the release of electrons and also too easily etched in the hydrogen cleaning plasma expected to be deployed in EUV scanners. Hydrogen plasmas can also etch silicon as well. A coating helps improve hydrogen resistance, but this reduces transmission and/or emissivity, and may also affect mechanical stability (e.g., bulging).

Wrinkles on pellicles can cause CD nonuniformity due to uneven absorption; this is worse for smaller wrinkles and more coherent illumination, i.e., lower pupil fill.

In the absence of pellicles, EUV mask cleanliness would have to be checked before actual product wafers are exposed, using wafers specially prepared for defect inspection. These wafers are inspected after printing for repeating defects indicating a dirty mask; if any are found, the mask must be cleaned and another set of inspection wafers are exposed, repeating the flow until the mask is clean. Any affected product wafers must be reworked.

TSMC reported starting limited use of its own pellicle in 2019 and continuing to expand afterwards, and Samsung is planning pellicle introduction in 2022. However, follow-up reporting indicating no users of EUV pellicles due to accelerated damage under higher power.

Without pellicles, yield can be significantly reduced by particles added onto the die exposure area of the mask. The particle size also determines if it can be fatal to yield.

### Hydrogen bulging defects

As discussed above, with regard to contamination removal, hydrogen used in recent EUV systems can penetrate into the EUV mask layers. TSMC indicated in its patent that hydrogen would enter from the mask edge. Once trapped, bulge defects or blisters were produced, which could lead to film peeling. These are essentially the blister defects which arise after a sufficient number of EUV mask exposures in the hydrogen environment. TSMC proposed some means for mitigating hydrogen blistering defects on EUV masks, which may impact productivity.


## EUV stochastic issues

EUV lithography is particularly sensitive to stochastic effects. In a large population of features printed by EUV, although the overwhelming majority are resolved, some suffer complete failure to print, e.g. missing holes or bridging lines. A known significant contribution to this effect is the dose used to print. This is related to shot noise, to be discussed further below. Due to the stochastic variations in arriving photon numbers, some areas designated to print actually fail to reach the threshold to print, leaving unexposed defect regions. Some areas may be overexposed, leading to excessive resist loss or crosslinking. The probability of stochastic failure increases exponentially as feature size decreases, and for the same feature size, increasing distance between features also significantly increases the probability. Line cuts which are misshapen are a significant issue due to potential arcing and shorting. Yield requires detection of stochastic failures down to below 1e-12.

The tendency to stochastic defects is worse from defocus over a large pupil fill.

Multiple failure modes may exist for the same population. For example, besides bridging of trenches, the lines separating the trenches may be broken. This can be attributed to stochastic resist loss, from secondary electrons. The randomness of the number of secondary electrons is itself a source of stochastic behavior in EUV resist images.

The coexistence of stochastically underexposed and overexposed defect regions leads to a loss of dose window at a certain post-etch defect level between the low-dose and high-dose patterning cliffs. Hence, the resolution benefit from shorter wavelength is lost.

The resist underlayer also plays an important role. This could be due to the secondary electrons generated by the underlayer. Secondary electrons may remove over 10 nm of resist from the exposed edge.

Photon shot noise also leads to stochastic edge placement error. The photon shot noise can be compensated to some degree by blurring factors such as secondary electrons or acids in chemically amplified resists; when significant the blur also reduces the image contrast at the edge. An edge placement error (EPE) as large as 8.8 nm was measured for a 48 nm pitch EUV-printed metal pattern.

With the natural Poisson distribution due to the random arrival and absorption times of the photons, there is an expected natural dose (photon number) variation of at least several percent 3 sigma, making the exposure process susceptible to stochastic variations. The dose variation leads to a variation of the feature edge position, effectively becoming a blur component. Unlike the hard resolution limit imposed by diffraction, shot noise imposes a softer limit, with the main guideline being the ITRS line width roughness (LWR) spec of 8% (3s) of linewidth. Increasing the dose will reduce the shot noise, but this also requires higher source power.

The two issues of shot noise and EUV-released electrons point out two constraining factors: 1) keeping dose high enough to reduce shot noise to tolerable levels, but also 2) avoiding too high a dose due to the increased contribution of EUV-released photoelectrons and secondary electrons to the resist exposure process, increasing the edge blur and thereby limiting the resolution. Aside from the resolution impact, higher dose also increases outgassing and limits throughput, and crosslinking occurs at very high dose levels. For chemically amplified resists, higher dose exposure also increases line edge roughness due to acid generator decomposition. Also, an upper limit to how much dose can be increased is imposed by resist loss.

Due to resist thinning with increased dose, EUV stochastic defectivity limits will define a narrow CD or dose window. The thinner resist at higher incident dose reduces absorption, and hence, absorbed dose. The thinner resist is also more susceptible to nanovoids leading to resist breaks.

Even with higher absorption at the same dose, EUV has a larger shot noise concern than the ArF (193 nm) wavelength, mainly because it is applied to thinner resists. There is also an extra component noise from the secondary electron emission.

Due to stochastic considerations, the IRDS 2022 lithography roadmap now acknowledges increasing doses for smaller feature sizes.

EUV resolution will likely be compromised by stochastic effects. Stochastic defect densities have exceeded 1/cm2, at 36 nm pitch; this is aggravated by electron blur. In 2024, an EUV resist exposure by ASML revealed a missing+bridging 32 nm pitch contact hole defect density floor >0.25/cm2 (177 defects per wafer), made worse with thinner resist. ASML indicated 30 nm pitch would not use direct exposure but double patterning. Intel did not use EUV for 30 nm pitch. Besides lower absorbed photon density, the impact of stochastic effects on EUV resolution is also tied to the smaller molecular size of EUV resists.

DRAM scaling will also become difficult at 10-11 nm design rules, due to EUV stochastics. The storage node patterns, which are arranged in a hexagonal array, are particularly sensitive due to their reliance on hexapole EUV illumination, which splits the image into three different sub-images, each with a third of the dose.

Larger features may unexpectedly suffer from stochastic fluctuations as well, due to local peaks and valleys in their aerial image.

IMEC's yield model updated in 2024 indicated that increased EUV use for 5nm node and beyond resulted in reduced yield, due to higher stochastic defectivity at tighter pitches.

As of 2025, stochastic defect probabilities were on the order of ppm, and could also vary over an order of magnitude, leading to erratic yields.

### Pupil fill ratio

For pitches less than half-wavelength divided by numerical aperture, dipole illumination is necessary. This illumination fills at most a leaf-shaped area at the edge of the pupil. However, due to 3D effects in the EUV mask, smaller pitches require even smaller portions of this leaf shape. Below 20% of the pupil, the throughput and dose stability begin to suffer. Higher numerical aperture allows a higher pupil fill to be used for the same pitch, but depth of focus is significantly reduced.

A larger pupil fill is more susceptible to stochastic fluctuations from point to point in the pupil.


## Use with multiple-patterning

EUV is anticipated to use double-patterning at around 34 nm pitch with 0.33 NA. This resolution is equivalent to '1Y' for DRAM. In 2020, ASML reported that 5 nm M0 layer (30 nm minimum pitch) required double-patterning. In H2 2018, TSMC confirmed that its 5 nm EUV scheme still used multi-patterning, also indicating that mask count did not decrease from its 7 nm node, which used extensive DUV multi-patterning, to its 5 nm node, which used extensive EUV. EDA vendors also indicated the continued use of multi-patterning flows. While Samsung introduced its own 7 nm process with EUV single-patterning, it encountered severe photon shot noise causing excessive line roughness, which required higher dose, resulting in lower throughput. TSMC's 5 nm node uses even tighter design rules. Samsung indicated smaller dimensions would have more severe shot noise.

In Intel's complementary lithography scheme at 20 nm half-pitch, EUV would be used only in a second line-cutting exposure after a first 193 nm line-printing exposure.

Multiple exposures would also be expected where two or more patterns in the same layer, e.g., different pitches or widths, must use different optimized source pupil shapes. For example, when considering a staggered bar array of 64 nm vertical pitch, changing the horizontal pitch from 64 nm to 90 nm changes the optimized illumination significantly. Source-mask optimization that is based on line-space gratings and tip-to-tip gratings only does not entail improvements for all parts of a logic pattern, e.g., a dense trench with a gap on one side.

In 2020, ASML reported that for the 3 nm node, center-to-center contact/via spacings of 40 nm or less would require double- or triple-patterning for some contact/via arrangements.

For the 24–36 nm metal pitch, it was found that using EUV as a (second) cutting exposure had a significantly wider process window than as a complete single exposure for the metal layer. However, using a second exposure in the LELE approach for double patterning does not get around the vulnerability to stochastic defects.

Multiple exposures of the same mask are also expected for defect management without pellicles, limiting productivity similarly to multiple-patterning.

Self-aligned litho-etch-litho-etch (SALELE) is a hybrid SADP/LELE technique whose implementation has started in 7 nm. Self-aligned litho-etch-litho-etch (SALELE) has become an accepted form of double-patterning to be used with EUV.

In order to avoid higher doses for alleviating stochastic effects (even for 36 nm vias) splitting the pattern, leading to double patterning or multipatterning, would lead to a better image quality. In fact, this occurs at large enough design rules (i.e., 36 nm) that it overlaps with DUV double patterning.


## Single-patterning extension: anamorphic high-NA

A return to extended generations of single-patterning would be possible with higher numerical aperture (NA) tools. An NA of 0.45 could require retuning of a few percent. Increasing demagnification could avoid this retuning, but the reduced field size severely affects large patterns (one die per 26 mm × 33 mm field) such as the many-core multi-billion transistor 14 nm Xeon chips. by requiring field stitching of two mask exposures.

In 2015, ASML disclosed details of its anamorphic next-generation EUV scanner, with an NA of 0.55. These machines cost around US$360 million. The demagnification is increased from 4× to 8× only in one direction (in the plane of incidence). However, the 0.55 NA has a much smaller depth of focus than immersion lithography. Also, an anamorphic 0.52 NA tool has been found to exhibit too much CD and placement variability for 5 nm node single exposure and multi-patterning cutting.

Depth of focus being reduced by increasing NA is also a concern, especially in comparison with multi-patterning exposures using 193 nm immersion lithography:

| Wavelength | Refractive index | NA | DOF (normalized) |
|---|---|---|---|
| 193 nm | 1.44 | 1.35 | 1 |
| 13.3–13.7 nm | 1 | 0.33 | 1.17 |
| 13.3–13.7 nm | 1 | 0.55 | 0.40 |

High-NA EUV tools focus horizontal and vertical lines differently from low-NA systems, due to the different demagnification for horizontal lines.

High-NA EUV tools also suffer from obscuration, which can cause errors in the imaging of certain patterns.

Intel completed assembly of its first commercial high-NA tool, TWINSCAN EXE:5000, in its D1X R&D fab in Oregon in April 2024, with a second machine installed in October 2024. In late 2025, Intel installed the new TWINSCAN EXE:5200B for its upcoming 14A node, with volume production expected in 2027.

For sub-2nm nodes, high-NA EUV systems will be affected by a host of issues: throughput, new masks, polarization, thinner resists, and secondary electron blur and randomness. Reduced depth of focus requires resist thickness less than 30 nm, which in turn increases stochastic effects, due to reduced photon absorption.

Electron blur is estimated to be at least ~2 nm, which is enough to thwart the benefit of High-NA EUV lithography.

Beyond high-NA, ASML in 2024 announced plans for the development of a hyper-NA EUV tool with an NA beyond 0.55, such as an NA of 0.75 or 0.85. These machines could cost US$720 million each and are expected to be available in 2030. A problem with Hyper-NA is polarization of the EUV light causing a reduction in image contrast.


## Beyond EUV wavelength

A much shorter wavelength (~6.7 nm) would be beyond EUV, and is often referred to as BEUV (beyond extreme ultraviolet). With current technology, BEUV wavelengths would have worse shot noise effects without ensuring sufficient dose. (The generally accepted 'border' of UV is 10nm below which the (soft) X-ray region begins.)
