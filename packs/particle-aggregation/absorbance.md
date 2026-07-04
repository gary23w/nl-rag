---
title: "Absorbance"
source: https://en.wikipedia.org/wiki/Absorbance
domain: particle-aggregation
license: CC-BY-SA-4.0
tags: particle aggregation
fetched: 2026-07-04
---

# Absorbance

In spectroscopy, **absorbance** (abbreviated as **A**) is a logarithmic value which describes the portion of a beam of light which does not pass through a sample. Whilst the name refers to the absorption of light, other interactions of light with a sample (reflection, scattering) may also contribute to attenuation of the beam passing through the sample. The term "internal absorbance" is sometimes used to describe beam attenuation caused by absorption, while "attenuance" or "experimental absorbance" can be used to emphasize that beam attenuation can be caused by other phenomena.

## History and uses of the term absorbance

### Beer-Lambert law

The roots of the term absorbance are in the Beer–Lambert law (or Beer's law). As light moves through a medium, it will become dimmer as it is being "extinguished". Pierre Bouguer recognized that this extinction (now often called attenuation) was not linear with distance traveled through the medium, but related to what is now referred to as an exponential function.

If $I_{0}$ is the intensity of the light at the beginning of the travel and $I_{d}$ is the intensity of the light detected after travel of a distance d , the fraction transmitted, T , is given by

$T={\frac {I_{d}}{I_{0}}}=\exp(-\mu d)\,,$

where $\mu$ is called an attenuation constant (a term used in various fields where a signal is transmitted though a medium) or coefficient. The amount of light transmitted decreases exponentially with distance. Taking the natural logarithm in the above equation, we get

$-\ln(T)=\ln {\frac {I_{0}}{I_{d}}}=\mu d\,.$

For scattering media, the constant is often divided into two parts, $\mu =\mu _{s}+\mu _{a}$ , separating it into a scattering coefficient $\mu _{s}$ and an absorption coefficient $\mu _{a}$ , obtaining

$-\ln(T)=\ln {\frac {I_{0}}{I_{s}}}=(\mu _{s}+\mu _{a})d\,.$

If the size of a detector is very small compared to the distance traveled by the light, any light that is scattered by a particle, either in the forward or backward direction, will not strike the detector. (Bouguer was studying astronomical phenomena, so this condition was met.) In such cases, a plot of $-\ln(T)$ as a function of wavelength will yield a superposition of the effects of absorption and scattering. Because the absorption portion is more distinct and tends to ride on a background of the scatter portion, it is often used to identify and quantify the absorbing species. Consequently, this is often referred to as absorption spectroscopy, and the plotted quantity is called "absorbance", symbolized as $\mathrm {A}$ . Some disciplines by convention use decadic (base 10) absorbance rather than Napierian (natural) absorbance, resulting in $\mathrm {A} _{10}=\mu _{10}d$ (with the subscript 10 usually not shown).

### Absorbance for non-scattering samples

Within a homogeneous medium such as a solution, there is no scattering. In this case, researched extensively by August Beer, the concentration of the absorbing species follows the same linear contribution to absorbance as the path-length. Additionally, the contributions of individual absorbing species are additive. This is a very favorable situation, and made absorbance an absorption metric far preferable to absorption fraction (absorptance). This is the case for which the term "absorbance" was first used.

A common expression of the Beer's law relates the attenuation of light in a material as $\mathrm {A} =\varepsilon \ell c$ , where $\mathrm {A}$ is the **absorbance;** $\varepsilon$ is the molar attenuation coefficient or absorptivity of the attenuating species; $\ell$ is the optical path length; and c is the concentration of the attenuating species.

### Absorbance for scattering samples

For samples which scatter light, absorbance is defined as "the negative logarithm of one minus absorptance (absorption fraction: $\alpha$ ) as measured on a uniform sample". For decadic absorbance, this may be symbolized as $\mathrm {A} _{10}=-\log _{10}(1-\alpha )$ . If a sample both transmits and remits light, and is not luminescent, the fraction of light absorbed ( $\alpha$ ), remitted ( R ), and transmitted ( T ) add to 1: $\alpha +R+T=1$ . Note that $1-\alpha =R+T$ , and the formula may be written as $\mathrm {A} _{10}=-\log _{10}(R+T)$ . For a sample which does not scatter, $R=0$ , and $1-\alpha =T$ , yielding the formula for absorbance of a material discussed below.

Even though this absorbance function is very useful with scattering samples, the function does not have the same desirable characteristics as it does for non-scattering samples. There is, however, a property called absorbing power which may be estimated for these samples. The absorbing power of a single unit thickness of material making up a scattering sample is the same as the absorbance of the same thickness of the material in the absence of scatter.

### Optics

In optics, **absorbance** or **decadic absorbance** is the *common logarithm* of the ratio of incident to *transmitted* radiant power through a material, and **spectral absorbance** or **spectral decadic absorbance** is the common logarithm of the ratio of incident to *transmitted* spectral radiant power through a material. Absorbance is dimensionless, and in particular is not a length, though it is a monotonically increasing function of path length, and approaches zero as the path length approaches zero.

## Mathematical definitions

### Absorbance of a material

The **absorbance** of a material, denoted A, is given by

$A=\log _{10}{\frac {\Phi _{\text{e}}^{\text{i}}}{\Phi _{\text{e}}^{\text{t}}}}=-\log _{10}T,$

where

- ${\textstyle \Phi _{\text{e}}^{\text{t}}}$ is the radiant flux *transmitted* by that material,
- ${\textstyle \Phi _{\text{e}}^{\text{i}}}$ is the radiant flux *received* by that material, and
- ${\textstyle T=\Phi _{\text{e}}^{\text{t}}/\Phi _{\text{e}}^{\text{i}}}$ is the transmittance of that material.

Absorbance is a dimensionless quantity. Nevertheless, the **absorbance unit** or **AU** is commonly used in ultraviolet–visible spectroscopy and its high-performance liquid chromatography applications, often in derived units such as the milli-absorbance unit (mAU) or milli-absorbance unit-minutes (mAU×min), a unit of absorbance integrated over time.

Absorbance is related to optical depth by

$A={\frac {\tau }{\ln 10}}=\tau \log _{10}e\,,$

where τ is the optical depth.

### Spectral absorbance

**Spectral absorbance in frequency** and **spectral absorbance in wavelength** of a material, denoted *Aν* and *Aλ* respectively, are given by

${\begin{aligned}A_{\nu }&=\log _{10}{\frac {\Phi _{{\text{e}},\nu }^{\text{i}}}{\Phi _{{\text{e}},\nu }^{\text{t}}}}=-\log _{10}T_{\nu }\,,\\A_{\lambda }&=\log _{10}{\frac {\Phi _{{\text{e}},\lambda }^{\text{i}}}{\Phi _{{\text{e}},\lambda }^{\text{t}}}}=-\log _{10}T_{\lambda }\,,\end{aligned}}$

where

- ${\textstyle \Phi _{\mathrm {e} ,\nu }^{t}}$ is the spectral radiant flux in frequency *transmitted* by that material;
- ${\textstyle \Phi _{\mathrm {e} ,\nu }^{i}}$ is the spectral radiant flux in frequency *received* by that material;
- ${\textstyle T_{\nu }}$ is the spectral transmittance in frequency of that material;
- ${\textstyle \Phi _{\mathrm {e} ,\lambda }^{t}}$ is the spectral radiant flux in wavelength *transmitted* by that material;
- ${\textstyle \Phi _{\mathrm {e} ,\lambda }^{i}}$ is the spectral radiant flux in wavelength *received* by that material; and
- ${\textstyle T_{\lambda }}$ is the spectral transmittance in wavelength of that material.

Spectral absorbance is related to spectral optical depth by

${\begin{aligned}A_{\nu }&={\frac {\tau _{\nu }}{\ln 10}}=\tau _{\nu }\log _{10}e\,,\\A_{\lambda }&={\frac {\tau _{\lambda }}{\ln 10}}=\tau _{\lambda }\log _{10}e\,,\end{aligned}}$

where

- τν is the spectral optical depth in frequency, and
- τλ is the spectral optical depth in wavelength.

Although absorbance is properly unitless, it is sometimes reported in "absorbance units", or AU. Many people, including scientific researchers, wrongly state the results from absorbance measurement experiments in terms of these made-up units.

## Relationship with attenuation

### Attenuance

Absorbance is a number that measures the *attenuation* of the transmitted radiant power in a material. Attenuation can be caused by the physical process of "absorption", but also reflection, scattering, and other physical processes. Absorbance of a material is approximately equal to its attenuance when both the absorbance is much less than 1 and the emittance of that material (not to be confused with radiant exitance or emissivity) is much less than the absorbance. Indeed,

$\Phi _{\mathrm {e} }^{\mathrm {t} }+\Phi _{\mathrm {e} }^{\mathrm {att} }=\Phi _{\mathrm {e} }^{\mathrm {i} }+\Phi _{\mathrm {e} }^{\mathrm {e} }\,,$

where

- ${\textstyle \Phi _{\mathrm {e} }^{\mathrm {t} }}$ is the radiant power transmitted by that material,
- ${\textstyle \Phi _{\mathrm {e} }^{\mathrm {att} }}$ is the radiant power attenuated by that material,
- ${\textstyle \Phi _{\mathrm {e} }^{\mathrm {i} }}$ is the radiant power received by that material, and
- ${\textstyle \Phi _{\mathrm {e} }^{\mathrm {e} }}$ is the radiant power emitted by that material.

This is equivalent to

$T+\mathrm {ATT} =1+E\,,$

where

- ${\textstyle T=\Phi _{\mathrm {e} }^{\mathrm {t} }/\Phi _{\mathrm {e} }^{\mathrm {i} }}$ is the transmittance of that material,
- ${\textstyle \mathrm {ATT} =\Phi _{\mathrm {e} }^{\mathrm {att} }/\Phi _{\mathrm {e} }^{\mathrm {i} }}$ is the *attenuance* of that material,
- ${\textstyle E=\Phi _{\mathrm {e} }^{\mathrm {e} }/\Phi _{\mathrm {e} }^{\mathrm {i} }}$ is the emittance of that material.

According to the Beer's law, *T* = 10−*A*, so

- $\mathrm {ATT} =1-10^{-A}+E\approx A\ln 10+E,\quad {\text{if}}\ A\ll 1,$

and finally

- $\mathrm {ATT} \approx A\ln 10,\quad {\text{if}}\ E\ll A.$

### Attenuation coefficient

Absorbance of a material is also related to its *decadic attenuation coefficient* by

$A=\int _{0}^{l}a(z)\,\mathrm {d} z\,,$

where

- l is the thickness of that material through which the light travels, and
- *a*(*z*) is the *decadic attenuation coefficient* of that material at z.

If *a*(*z*) is uniform along the path, the attenuation is said to be a *linear attenuation*, and the relation becomes $A=al.$

Sometimes the relation is given using the *molar attenuation coefficient* of the material, that is its attenuation coefficient divided by its molar concentration:

$A=\int _{0}^{l}\varepsilon c(z)\,\mathrm {d} z\,,$

where

- ε is the *molar attenuation coefficient* of that material, and
- *c*(*z*) is the molar concentration of that material at z.

If *c*(*z*) is uniform along the path, the relation becomes

$A=\varepsilon cl\,.$

The use of the term "molar absorptivity" for molar attenuation coefficient is discouraged.

## Use in Analytical Chemistry

Absorbance is a widely used measurement in quantitative absorption spectroscopy. While the attenuation of a light beam can be also be described by *transmittance* (the ratio of transmitted incident light), the logarithmic formulation of absorbance is convenient for sample quantification: under conditions where the Beer's law is valid, absorbance will be linearly proportional to sample thickness and the concentration of the absorptive species.

For quantitative purposes, absorbance is often measured on a sample solution held in a cuvette, where the solution is sufficiently dilute that the linear relationship of the Beer's law holds. The cuvette provides a known and consistent path length for the light beam passing through the sample. Measuring first the absorbance of the cuvette and a "blank" solution containing no analyte, differences in absorbance between samples can be used to quantity the analyte. Spectrometers generally measure absorbance separately for a range of wavelengths: this data is then plotted as absorbance vs. wavelength.

## Shade number

Some filters, notably welding glass, are rated by shade number (SN), which is 7/3 times the absorbance plus one:

${\begin{aligned}\mathrm {SN} &={\frac {7}{3}}A+1\\&={\frac {7}{3}}(-\log _{10}T)+1\,.\end{aligned}}$

For example, if the filter has 0.1% transmittance (0.001 transmittance, which is 3 absorbance units), its shade number would be 8.
