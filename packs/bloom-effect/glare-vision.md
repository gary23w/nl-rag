---
title: "Glare (vision)"
source: https://en.wikipedia.org/wiki/Glare_(vision)
domain: bloom-effect
license: CC-BY-SA-4.0
tags: bloom shader effect, light bloom rendering, gaussian blur bloom, glare post-processing
fetched: 2026-07-02
---

# Glare (vision)

**Glare** is difficulty of seeing in the presence of bright light such as direct or reflected sunlight or artificial light such as car headlamps at night. Because of this, some cars include mirrors with automatic anti-glare functions and in buildings, blinds or louvers are often used to protect occupants. Glare is caused by a significant ratio of luminance between the task (that which is being looked at) and the glare source. Factors such as the angle between the task and the glare source and eye adaptation have significant impacts on the experience of glare.

## Discomfort and disability

Glare can be generally divided into two types, discomfort glare and disability glare. Discomfort glare is a psychological sensation caused by high brightness (or brightness contrast) within the field of view, which does not necessarily impair vision. In buildings, discomfort glare can originate from small artificial lights (e.g. ceiling fixtures) that have brightnesses that are significantly greater than their surrounding. When the luminous source occupies a much greater portion of the visual field (e.g. daylit windows), discomfort caused by glare can be linked to a saturating effect. Since observers will not always look directly at a bright illuminated source, discomfort glare usually arises when an observer is focusing on a visual task (e.g. a computer-screen) and the bright source is within their peripheral visual field.

Disability glare impairs the vision of objects without necessarily causing discomfort. This could arise for instance when driving westward at sunset. Disability glare is often caused by the inter-reflection of light within the eyeball, reducing the contrast between task and glare source to the point where the task cannot be distinguished. When glare is so intense that vision is completely impaired, it is sometimes called **dazzle**.

## Reducing factors

Glare can reduce visibility by:

- Reduction of brightness of the rest of the scene by constriction of the pupils
- Reduction in contrast of the rest of the scene by scattering of the bright light within the eye.
- Reduction in contrast by scattering light in particles in the air, as when the headlights of a car illuminate the fog close to the vehicle, impeding vision at larger distance.
- Reduction in contrast between print and paper by reflection of the light source in the printed matter (veiling glare).
- Reduction in contrast by reflection of bright areas on the surface of a transparent medium as glass, plastic or water; for example when the sky is reflected in a lake, so that the bottom below or objects in the water cannot be seen (veiling glare).
- bloom surrounding objects in front of glare

Sunglasses are often worn to reduce glare; polarized sunglasses are designed to reduce glare caused by light reflected from non-metallic surfaces such as water, glossy printed matter or painted surfaces. An anti-reflective treatment on eyeglasses reduces the glare at night and glare from inside lights and computer screens that is caused by light bouncing off the lens. Some types of eyeglasses can reduce glare that occurs because of the imperfections on the surface of the eye.

Light field measurements can be taken to reduce glare with digital post-processing.

## Measurement

### Methods

Discomfort glare has often been studied using psychophysics experiments, where the common methods have been the luminance adjustment and category rating procedures. Studies conducted by Petherbridge and Hopkinson and Luckiesh and Guth. were amongst the first to compared subjective assessments given by observers against physical measurements produced by a glare source.

### Biases

A comprehensive review of the methods used to measure glare showed that there are biases associated with its measurement. Luminance adjustments are sensitive to anchoring effects caused when the initial starting luminance viewed influences the final assessment of visual discomfort. Glare is also subject to stimulus range bias effects. This occurs when the luminance range influences the final evaluation of glare given by the observer. A larger range, often results in higher glare evaluations given.

### Prediction models

Glare from artificial lights is typically measured with luminance meters. From daylit windows, cameras are used to convert the pixels into luminance. Both of which are able to determine the luminance of objects within small solid angles. The glare of a scene i.e. visual field of view, is then calculated from the luminance data of that scene.

The International Commission on Illumination (CIE) defines glare as:

> *"Visual conditions in which there is excessive contrast or an inappropriate distribution of light sources that disturbs the observer or limits the ability to distinguish details and objects".*

The CIE recommends the *Unified glare rating* (UGR) as a quantitative measure of glare. Other glare calculation methods include *CIBSE Glare Index*, *IES Glare Index* and the *Daylight Glare Index* (DGI).

### Unified glare rating

The Unified Glare Rating (UGR) is a measure of the glare in a given environment, accounting only interior artificial lights, proposed by Sorensen in 1987 and adopted by the International Commission on Illumination (CIE). It is basically the logarithm of the glare of all visible lamps, divided by the background lumination $L_{b}$ :

$\mathrm {UGR} =8\log {\frac {0.25}{L_{b}}}\sum _{n}\left(L_{n}^{2}{\frac {\omega _{n}}{p_{n}^{2}}}\right),$

Where $\log$ is the common logarithm (base 10), $L_{n}$ is the luminance of each light source numbered n , $\omega _{n}$ is the solid angle of the light source seen from the observer and $p_{n}$ is the Guth Position Index, which depends on the distance from the line of sight of the viewer.

### Daylight Glare Probability

The Daylight Glare Probability (DGP) is a measure glare from real daylight condition in side-lit room within the field of view from curtain position, not considering for artificial light. It considers illuminance and luminance from glare sources to estimate the level of dissatisfaction. DGP was proposed by Wienold and Christoffersen in 2006 and adopted as first ever day-lighting standard by the European Standard's EN 17037 (2018) Daylight in Buildings. The EN 17037 glare assessment helps designer to determine shading need, transmission of glazing if the DGP is higher than 0.4. However, data from tropical climate countries suggests the DGP threshold is expected to be 0.24, significant lower than Wienold and Christoffersen's Copenhagen and Freiburg data.

$\mathrm {DGP} =5.87\times 10^{-5}\times E_{V}+9.18\times 10^{-2}\times log\left(1+\sum _{i}{\frac {L_{s,i}^{2}\times \omega _{s,i}}{E_{V}^{1.87}\times P_{i}^{2}}}\right)+0.16,$

Where $\log$ is the common logarithm (base 10), $E_{V}$ is the illuminance at eye level (lx), $L_{s}$ is the luminance of glare source (cd/ $m^{2}$ ), i is the number of glare sources, $\omega _{s}$ is the solid angle of the glare sources seen from the observer and $p_{i}$ is the Guth Position Index, which depends on the distance from the line of sight of the viewer.
