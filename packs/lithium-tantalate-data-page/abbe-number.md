---
title: "Abbe number"
source: https://en.wikipedia.org/wiki/Abbe_number
domain: lithium-tantalate-data-page
license: CC-BY-SA-4.0
tags: lithium tantalate data page
fetched: 2026-07-04
---

# Abbe number

In optics and lens design, the **Abbe number**, also known as the **Vd-number** or **constringence** of a transparent material, is an approximate measure of a material's dispersion (change in refractive index as a function of wavelength), with high Vd values indicating low dispersion. It is named after Ernst Abbe (1840–1905), the German physicist who defined it. The term Vd-number should not be confused with the normalized frequency in fibers.

The Abbe number $V_{\text{d}}$ of a material is defined as: $V_{\text{d}}\equiv {\frac {n_{\text{d}}-1}{n_{\text{F}}-n_{\text{C}}}},$ where $n_{\text{C}}$ , $n_{\text{d}}$ , and $n_{\text{F}}$ are the refractive indices of the material at the wavelengths of the Fraunhofer's C, d, and F spectral lines (656.3 nm, 587.56 nm, and 486.1 nm, respectively). This formulation only applies to human vision; outside this range, alternative spectral lines are required. For non-visible spectral lines, the term "V-number" is more commonly used. The more general formulation is $V\equiv {\frac {n_{\text{center}}-1}{n_{\text{short}}-n_{\text{long}}}},$ where $n_{\text{short}}$ , $n_{\text{center}}$ , and $n_{\text{long}}$ are the refractive indices of the material at three different wavelengths.

Abbe numbers are used to classify glass and other optical materials in terms of their chromaticity. For example, the higher dispersion flint glasses have relatively small Abbe numbers V less than 55, whereas the lower dispersion crown glasses have larger Abbe numbers. Values of $V_{\text{d}}$ range from below 25 for very dense flint glasses, around 34 for polycarbonate plastics, up to 65 for common crown glasses, and 75 to 85 for some fluorite and phosphate crown glasses.

Abbe numbers are useful in the design of achromatic lenses, as their reciprocal is proportional to dispersion (slope of refractive index versus wavelength) in the domain where the human eye is most sensitive (see above figure). For other wavelength regions, or for higher precision in characterizing a system's chromaticity (such as in the design of apochromats), the full dispersion relation is used (i.e., refractive index as a function of wavelength).

## Abbe diagram

An **Abbe diagram** (sometimes referred to as "the glass veil") is produced by plotting the refractive index of a material $n_{\text{d}}$ as a function of Abbe number V . Glasses can then be categorized and selected according to their positions on the diagram. This categorization could be in the form of a letter-number code, as used for example in the Schott Glass catalogue, or a 6-digit glass code.

Glasses' Abbe numbers, along with their mean refractive indices, are used in the calculation of the required refractive powers of the elements of achromatic lenses in order to cancel chromatic aberration to first order. These two parameters, which enter into the equations for the design of achromatic doublets, are exactly what is plotted on an Abbe diagram.

Due to the difficulty and inconvenience in producing sodium and hydrogen lines, alternate definitions of the Abbe number are often substituted (ISO 7944). For example, rather than the standard definition given above, which uses the refractive index variation between the F and C hydrogen lines, one alternative measure is to use mercury's e-line compared to cadmium's F′- and C′-lines: $V_{\text{e}}={\frac {n_{\text{e}}-1}{n_{{\text{F}}'}-n_{{\text{C}}'}}}.$ This formulation takes the difference between cadmium's blue (F′) and red (C′) refractive indices at wavelengths 480.0 nm and 643.8 nm, respectively, relative to $n_{\text{e}}$ for mercury's e-line at 546.073 nm, all of which are in close proximity to—and somewhat easier to produce—than the C, F, and d-lines. Other definitions can be similarly employed; the following table lists standard wavelengths at which n is commonly determined, including the standard subscripts used.

| λ (nm) | Fraunhofer's symbol | Light source | Color |
|---|---|---|---|
| 365.01 | i | Hg | UV-A |
| 404.66 | h | Hg | violet |
| 435.84 | g | Hg | blue |
| 479.99 | F′ | Cd | blue |
| 486.13 | F | H | blue |
| 546.07 | e | Hg | green |
| 587.56 | d | He | yellow |
| 589.30 | D | Na | yellow |
| 643.85 | C′ | Cd | red |
| 656.27 | C | H | red |
| 706.52 | r | He | red |
| 768.20 | A′ | K | IR-A |
| 852.11 | s | Cs | IR-A |
| 1013.98 | t | Hg | IR-A |

## Derivation of relative change

Starting with the Lensmaker's equation, we obtain the thin lens equation by neglecting the small term that accounts for lens thickness d : $P_{0}={\frac {1}{f}}=(n-1){\Biggl [}{\frac {1}{R_{1}}}-{\frac {1}{R_{2}}}+{\frac {(n-1)d}{nR_{1}R_{2}}}{\Biggr ]}\approx (n-1)\left({\frac {1}{R_{1}}}-{\frac {1}{R_{2}}}\right),$ when $d\ll {\sqrt {R_{1}R_{2}}}$ .

The change in refractive power $P_{0}$ between two wavelengths $\lambda _{\text{short}}$ and $\lambda _{\text{long}}$ is given by $\Delta P_{0}=P_{\text{short}}-P_{\text{long}}=(n_{\text{s}}-n_{\ell })\left({\frac {1}{R_{1}}}-{\frac {1}{R_{2}}}\right),$ where $n_{\text{s}}$ and $n_{\ell }$ are the short and long wavelengths' refractive indexes, respectively.

The difference in power can be expressed relative to the power at a center wavelength $\lambda _{\text{c}}$ : $P_{\text{c}}=(n_{\text{c}}-1)\left({\frac {1}{R_{1}}}-{\frac {1}{R_{2}}}\right),$ with $n_{\text{c}}$ having an analogous meaning as above. Now rewrite $\Delta P_{0}$ to make $P_{\text{c}}$ and the Abbe number at the center wavelength $V_{\text{c}}$ accessible: $\Delta P_{0}=\left(n_{\text{s}}-n_{\ell }\right)\left({\frac {n_{\text{c}}-1}{n_{\text{c}}-1}}\right)\left({\frac {1}{R_{1}}}-{\frac {1}{R_{2}}}\right)=\left({\frac {n_{\text{s}}-n_{\ell }}{n_{\text{c}}-1}}\right)P_{\text{c}}={\frac {P_{\text{c}}}{V_{\text{c}}}}.$ The relative change is therefore inversely proportional to $V_{\text{c}}$ : ${\frac {\Delta P_{0}}{P_{\text{c}}}}={\frac {1}{V_{\text{c}}}}.$
