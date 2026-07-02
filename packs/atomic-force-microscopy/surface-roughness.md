---
title: "Surface roughness"
source: https://en.wikipedia.org/wiki/Surface_roughness
domain: atomic-force-microscopy
license: CC-BY-SA-4.0
tags: scanning probe, cantilever tip, surface topography, tapping mode
fetched: 2026-07-02
---

# Surface roughness

**Surface roughness** or simply **roughness** is the quality of a surface of not being smooth and it is hence linked to human (haptic) perception of the surface texture. From a mathematical perspective it is related to the spatial variability structure of surfaces, and inherently it is a multiscale property. It has different interpretations and definitions depending on the disciplines considered.

In surface metrology, surface roughness is a component of surface finish (surface texture). It is quantified by the deviations in the direction of the normal vector of a real surface from its ideal form. If these deviations are large, the surface is rough; if they are small, the surface is smooth. Roughness is typically assumed to be the high-frequency, short-wavelength component of a measured surface. However, in practice it is often necessary to know both the amplitude and frequency to ensure that a surface is fit for a purpose.

## Role and effect

Roughness plays an important role in determining how a real object will interact with its environment. In tribology, rough surfaces usually wear more quickly and have higher friction coefficients than smooth surfaces. Roughness is often a good predictor of the performance of a mechanical component, since irregularities on the surface may form nucleation sites for cracks or corrosion. On the other hand, roughness may promote adhesion. Generally speaking, rather than scale specific descriptors, cross-scale descriptors such as surface fractality provide more meaningful predictions of mechanical interactions at surfaces including contact stiffness and static friction.

Although a high roughness value is often undesirable, it can be difficult and expensive to control in manufacturing. For example, it is difficult and expensive to control surface roughness of fused deposition modelling (FDM) manufactured parts. Decreasing the roughness of a surface usually increases its manufacturing cost. This often results in a trade-off between the manufacturing cost of a component and its performance in application.

Roughness can be measured by manual comparison against a "surface roughness comparator" (a sample of known surface roughness), but more generally a surface profile measurement is made with a profilometer. These can be of the contact variety (typically a diamond stylus) or optical (e.g.: a white light interferometer or laser scanning confocal microscope).

However, controlled roughness can often be desirable. For example, a gloss surface can be too shiny to the eye and too slippery to the finger (a touchpad is a good example) so a controlled roughness is required. This is a case where both amplitude and frequency are very important.

Surface structure plays a key role in governing contact mechanics, that is to say the mechanical behavior exhibited at an interface between two solid objects as they approach each other and transition from conditions of non-contact to full contact. In particular, normal contact stiffness is governed predominantly by asperity structures (roughness, surface slope and fractality) and material properties.

In terms of engineering surfaces, roughness is considered to be detrimental to part performance. As a consequence, most manufacturing prints establish an upper limit on roughness, but not a lower limit. An exception is in cylinder bores where oil is retained in the surface profile and a minimum roughness is required.

Surface structure is often closely related to the friction and wear properties of a surface. A surface with a higher fractal dimension, large $Ra$ value, or a positive $Rsk$ , will usually have somewhat higher friction and wear quickly. The peaks in the roughness profile are not always the points of contact. The form and waviness (i.e. both amplitude and frequency) must also be considered.

## Parameters

A roughness value can either be calculated on a profile (line) or on a surface (area). The profile roughness parameter ( $Ra$ , $Rq$ , ...) are more common. The area roughness parameters ( $Sa$ , $Sq$ , ...) give more significant values.

### Profile roughness parameters

The profile roughness parameters are included in BS EN ISO 4287:2000 British standard, identical with the ISO 4287:1997 standard. The standard is based on the ″M″ (mean line) system. There are many different roughness parameters in use, but $Ra$ is by far the most common, though this is often for historical reasons and not for particular merit, as the early roughness meters could only measure $Ra$ . Other common parameters include $Rz$ , $Rq$ , and $Rsk$ . Some parameters are used only in certain industries or within certain countries. For example, the $Rk$ family of parameters is used mainly for cylinder bore linings, and the *Motif parameters* are used primarily in the French automotive industry. The MOTIF method provides a graphical evaluation of a surface profile without filtering waviness from roughness. A *motif* consists of the portion of a profile between two peaks and the final combinations of these motifs eliminate ″insignificant″ peaks and retains ″significant″ ones. Please note that $Ra$ is a dimensional unit that can be micrometer or microinch.

Since these parameters reduce all of the information in a profile to a single number, great care must be taken in applying and interpreting them. Small changes in how the raw profile data is filtered, how the mean line is calculated, and the physics of the measurement can greatly affect the calculated parameter. With modern digital equipment, the scan can be evaluated to make sure there are no obvious glitches that skew the values.

Because it may not be obvious to many users what each of the measurements really mean, a simulation tool allows a user to adjust key parameters, visualizing how surfaces which are obviously different to the human eye are differentiated by the measurements. For example, $Ra$ fails to distinguish between two surfaces where one is composed of peaks on an otherwise smooth surface and the other is composed of troughs of the same amplitude. Such tools can be found in app format.

By convention every 2D roughness parameter is a capital R followed by additional characters in the subscript. The subscript identifies the formula that was used, and the R means that the formula was applied to a 2D roughness profile. Different capital letters imply that the formula was applied to a different profile. For example, $Ra$ is the arithmetic average of the roughness profile, $Pa$ is the arithmetic average of the unfiltered raw profile, and $Sa$ is the arithmetic average of the 3D roughness.

Each of the formulas listed in the tables assumes that the roughness profile has been filtered from the raw profile data and the mean line has been calculated. The roughness profile contains n ordered, equally spaced points along the trace, and $y_{i}$ is the vertical distance from the mean line to the $i^{\text{th}}$ data point. Height is assumed to be positive in the up direction, away from the bulk material.

#### Amplitude parameters

Amplitude parameters characterize the surface based on the vertical deviations of the roughness profile from the mean line. Many of them are closely related to the parameters found in statistics for characterizing population samples. For example, $Ra$ is the arithmetic average value of filtered roughness profile determined from deviations about the center line within the evaluation length and $Rt$ is the range of the collected roughness data points.

The arithmetic average roughness, $Ra$ , is the most widely used one-dimensional roughness parameter.

| Parameter | Description | Formula |
|---|---|---|
| $Ra$ , $Raa$ , Ryni | Average, or arithmetic average of profile height deviations from the mean line. | $Ra={\frac {1}{l_{r}}}\int _{0}^{l_{r}}\left\|z(x)\right\|dx$ |
| $Rq$ , $Rms$ | Quadratic mean, or root mean square average of profile height deviations from the mean line. | $Rq={\sqrt {{\frac {1}{l_{r}}}\int _{0}^{l_{r}}z(x)^{2}dx}}$ |
| $Rv_{i}$ , $Rv$ | Maximum valley depth below the mean line, within a single sampling length; Average Rv value over assessment length | $Rv_{i}=\|\min z(x)\|$ ; $Rv={\frac {\sum _{i=1}^{n}Rv_{i}}{n}}$ |
| $Rp_{i}$ , $Rp$ | Maximum peak height above the mean line, within a single sampling length; Average Rp value over assessment length | $Rp_{i}=\max z(x)$ ; $Rp={\frac {\sum _{i=1}^{n}Rp_{i}}{n}}$ |
| $Rz_{i}$ , $Rz$ | Maximum peak to valley height of the profile, within a single sampling length; Average Rz value over assessment length | $Rz_{i}=Rp_{i}+Rv_{i}$ ; $Rz={\frac {\sum _{i=1}^{n}Rz_{i}}{n}}$ |
| $Rsk$ | Skewness, or measure of asymmetry of the profile about the mean line. | $Rsk={\frac {1}{Rq^{3}}}\left[{\frac {1}{l_{r}}}\int _{0}^{l_{r}}z^{3}(x)dx\right]$ |
| $Rku$ | Kurtosis, or measure of peakedness (or tailedness) of the profile about the mean line. | $Rku={\frac {1}{{Rq}^{4}}}\left[{\frac {1}{l_{r}}}\int _{0}^{l_{r}}z^{4}(x)dx\right]$ |
| $RzDIN$ , $Rtm$ | Average distance between the highest peak and lowest valley in each sampling length, ASME Y14.36M - 1996 Surface Texture Symbols | $RzDIN={\frac {1}{s}}\sum _{i=1}^{s}Rt_{i}$ , where s is the number of sampling lengths, and $Rt_{i}$ is $R{\text{t}}$ for the $i^{\text{th}}$ sampling length. |
| $RzJIS$ | Japanese Industrial Standard for $Rz$ , based on the five highest peaks and lowest valleys over the entire sampling length. | $R{\text{zJIS}}={\frac {1}{5}}\sum _{i=1}^{5}Rp_{i}-Rv_{i}$ , where $Rp_{i}$ and $Rv_{i}$ are the $i^{\text{th}}$ highest peak, and lowest valley respectively. |

Here is a common conversion table with roughness grade numbers:

| Roughness, N | Roughness values, Ra | RMS (μin.) | Center line avg., CLA | Roughness, Rt |   |
|---|---|---|---|---|---|
| ISO grade numbers | micrometers (μm) | microinches (μin.) | (μin.) | (μm) |   |
| N12 | 50 | 2000 | 2200 | 2000 | 200 |
| N11 | 25 | 1000 | 1100 | 1000 | 100 |
| N10 | 12.5 | 500 | 550 | 500 | 50 |
| N9 | 6.3 | 250 | 275 | 250 | 25 |
| N8 | 3.2 | 125 | 137.5 | 125 | 13 |
| N7 | 1.6 | 63 | 69.3 | 63 | 8 |
| N6 | 0.8 | 32 | 35.2 | 32 | 4 |
| N5 | 0.4 | 16 | 17.6 | 16 | 2 |
| N4 | 0.2 | 8 | 8.8 | 8 | 1.2 |
| N3 | 0.1 | 4 | 4.4 | 4 | 0.8 |
| N2 | 0.05 | 2 | 2.2 | 2 | 0.5 |
| N1 | 0.025 | 1 | 1.1 | 1 | 0.3 |

#### Slope, spacing and counting parameters

Slope parameters describe characteristics of the slope of the roughness profile. Spacing and counting parameters describe how often the profile crosses certain thresholds. These parameters are often used to describe repetitive roughness profiles, such as those produced by turning on a lathe.

| Parameter | Description | Formula |
|---|---|---|
| $Rdq,R\Delta q$ | the RMS of the slope of the profile within the sampling length | $Rdq={\sqrt {{\frac {1}{N}}\sum _{i=1}^{N}\Delta _{i}^{2}}}$ |
| $Rda,R\Delta a$ | the average absolute slope of the profile within the sampling length | $Rda={\frac {1}{N}}\sum _{i=1}^{N}\|\Delta _{i}\|$ |
| $\Delta _{i}\!$ | where $\Delta _{i}\!$ is calculated according to ASME B46.1 and is a 5th order Savitzky–Golay smoothing filter | $\Delta _{i}={\frac {1}{60dx}}(y_{i+3}-9y_{i+2}+45y_{i+1}-45y_{i-1}+9y_{i-2}-y_{i-3})$ |

Other "frequency" parameters are Sm, $\lambda$ a and $\lambda$ q. Sm is the mean spacing between peaks. Just as with real mountains it is important to define a "peak". For Sm the surface must have dipped below the mean surface before rising again to a new peak. The average wavelength $\lambda$ a and the root mean square wavelength $\lambda$ q are derived from $\Delta$ a. When trying to understand a surface that depends on both amplitude and frequency it is not obvious which pair of metrics optimally describes the balance, so a statistical analysis of pairs of measurements can be performed (e.g.: Rz and $\lambda$ a or Ra and Sm) to find the strongest correlation.

#### Bearing ratio curve parameters

These parameters are based on the bearing ratio curve (also known as the Abbott-Firestone curve.) This includes the Rk family of parameters.

#### Fractal theory

The mathematician Benoît Mandelbrot has pointed out the connection between surface roughness and fractal dimension. The description provided by a fractal at the microroughness level may allow the control of the material properties and the type of the occurring chip formation. But fractals cannot provide a full-scale representation of a typical machined surface affected by tool feed marks; it ignores the geometry of the cutting edge. (J. Paulo Davim, 2010, *op.cit*.). Fractal descriptors of surfaces have an important role to play in correlating physical surface properties with surface structure. Across multiple fields, connecting physical, electrical and mechanical behavior with conventional surface descriptors of roughness or slope has been challenging. By employing measures of surface fractality together with measures of roughness or surface shape, certain interfacial phenomena including contact mechanics, friction and electrical contact resistance, can be better interpreted with respect to surface structure.

### Areal roughness parameters

Areal roughness parameters are defined in the ISO 25178 series. The resulting values are Sa, Sq, Sz,... Many optical measurement instruments are able to measure the surface roughness over an area. Area measurements are also possible with contact measurement systems. Multiple, closely spaced 2D scans are taken of the target area. These are then digitally stitched together using relevant software, resulting in a 3D image and accompanying areal roughness parameters.
