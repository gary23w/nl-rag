---
title: "Immersion lithography"
source: https://en.wikipedia.org/wiki/Immersion_lithography
domain: photolithography
license: CC-BY-SA-4.0
tags: semiconductor photolithography, extreme ultraviolet lithography, photomask fabrication, photoresist patterning
fetched: 2026-07-02
---

# Immersion lithography

**Immersion lithography** is a technique used in semiconductor manufacturing to enhance the resolution and accuracy of the photolithographic process. It involves using a liquid medium, typically water, between the lens and the wafer during exposure. By using a liquid with a higher refractive index than air, immersion lithography allows for smaller features to be created on the wafer.

Immersion lithography replaces the usual air gap between the final lens and the wafer surface with a liquid medium that has a refractive index greater than one. The angular resolution is increased by a factor equal to the refractive index of the liquid. Current immersion lithography tools use highly purified water for this liquid, achieving feature sizes below 45 nanometers.

## Background

The ability to resolve features in optical lithography is directly related to the numerical aperture of the imaging equipment, the numerical aperture being the sine of the maximum refraction angle multiplied by the refractive index of the medium through which the light travels. The lenses in the highest resolution "dry" photolithography scanners focus light in a cone whose boundary is nearly parallel to the wafer surface. As it is impossible to increase resolution by further refraction, additional resolution is obtained by inserting an immersion medium with a higher index of refraction between the lens and the wafer. The blurriness is reduced by a factor equal to the refractive index of the medium. For example, for water immersion using ultraviolet light at 193 nm wavelength, the index of refraction is 1.44.

The resolution enhancement from immersion lithography is about 30–40% depending on materials used. However, the depth of focus, or tolerance in wafer topography flatness, is improved compared to the corresponding "dry" tool at the same resolution.

The idea for immersion lithography was patented in 1984 by Takanashi et al. It was also proposed by Taiwanese engineer Burn J. Lin and realized in the 1980s. In 2004, IBM's director of silicon technology, Ghavam Shahidi, announced that IBM planned to commercialize lithography based on light filtered through water.

## Defects

Defect concerns, e.g., water left behind (watermarks) and loss of resist-water adhesion (air gap or bubbles), have led to considerations of using a topcoat layer directly on top of the photoresist. This topcoat would serve as a barrier for chemical diffusion between the liquid medium and the photoresist. In addition, the interface between the liquid and the topcoat would be optimized for watermark reduction. At the same time, defects from topcoat use should be avoided.

As of 2005, Topcoats had been tuned for use as antireflection coatings, especially for hyper-NA (NA>1) cases.

By 2008, defect counts on wafers printed by immersion lithography had reached zero level capability.

## Polarization impacts

As of 2000, Polarization effects due to high angles of interference in the photoresist were considered as features approach 40 nm. Hence, illumination sources generally need to be azimuthally polarized to match the pole illumination for ideal line-space imaging.

## Throughput

As of 1996, this was achieved through higher stage speeds, which in turn, as of 2013 were allowed by higher power ArF laser pulse sources. Specifically, the throughput is directly proportional to stage speed V, which is related to dose D and rectangular slit width S and slit intensity Iss (which is directly related to pulse power) by V=Iss*S/D. The slit height is the same as the field height. The slit width S, in turn, is limited by the number of pulses to make the dose (n), divided by the frequency of the laser pulses (f), at the maximum scan speed Vmax by S=Vmax*n/f. At a fixed frequency f and pulse number n, the slit width will be proportional to the maximum stage speed. Hence, throughput at a given dose is improved by increasing maximum stage speed as well as increasing pulse power.

In 2015 ASML reported that their TWINSCAN NXT:1980Di immersion lithography platform archieved throughputs of up to 275 WPH, targeted for high volume manufacturing.

## Multiple patterning

The resolution limit for a 1.35 NA immersion tool operating at 193 nm wavelength is 36 nm. Going beyond this limit to sub-20nm nodes requires multiple patterning.

In 2016 Samsung announced successful tests of a 10nm SoC using triple patterning, slated for mass production in 2017.
