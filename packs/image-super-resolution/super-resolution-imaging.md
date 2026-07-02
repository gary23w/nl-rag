---
title: "Super-resolution imaging"
source: https://en.wikipedia.org/wiki/Super-resolution_imaging
domain: image-super-resolution
license: CC-BY-SA-4.0
tags: image super resolution, single image upscaling, detail reconstruction, high resolution synthesis, learned upsampling
fetched: 2026-07-02
---

# Super-resolution imaging

**Super-resolution imaging** (**SRI**) is a class of techniques to improve the resolution of an imaging system, thus achieving "**super resolution**" (**SR**). In **optical SR** the diffraction limit of systems is transcended by means of a super lens, while in **geometrical SR** the resolution of digital imaging sensors is enhanced.

In some radar and sonar imaging applications (e.g. magnetic resonance imaging (MRI), high-resolution computed tomography), subspace decomposition-based methods (e.g. MUSIC) and compressed sensing-based algorithms (e.g., SAMV) are employed to achieve SR over standard periodogram algorithm.

Super-resolution imaging techniques are used in general image processing and in super-resolution microscopy.

## Principles

Several concepts are fundamental to super-resolution imaging:

- Diffraction limit: the capacity of an optical instrument to reproduce the details of an object in an image has limits that are imposed by laws of physics: the diffraction equations in the wave theory of light, or the uncertainty principle for photons in quantum mechanics. Information transfer can never be increased beyond this boundary, but packets outside the limits can be cleverly swapped for (or multiplexed with) some inside it. Super-resolution microscopy does not so much “break” as “circumvent” the diffraction limit. New procedures probing electro-magnetic disturbances at the molecular level (in the so-called near field) remain fully consistent with Maxwell's equations.
- Spatial frequency domain: A succinct expression of the diffraction limit is given in the spatial frequency domain. In Fourier optics light distributions are expressed as superpositions of a series of grating light patterns in a range of fringe widths - these widths represent the spatial frequencies. It is generally taught that diffraction theory stipulates an upper limit, the cut-off spatial-frequency, beyond which pattern elements fail to be transferred into the optical image, i.e., are not resolved. But in fact what is set by diffraction theory is the width of the passband, not a fixed upper limit. No laws of physics are broken when a spatial frequency band beyond the cut-off spatial frequency is swapped for one inside it: this has long been implemented in dark-field microscopy. Nor are information-theoretical rules broken when superimposing several bands, disentangling them in the received image needs assumptions of object invariance during multiple exposures, i.e., the substitution of one kind of uncertainty for another.
- Information: When the term super-resolution is used in techniques based on the inference of object details using a statistical treatment of the image within standard resolution limits (for example, averaging multiple exposures), it involves an exchange of one kind of information (extracting signal from noise) for another (the assumption that the target has remained invariant). Recent breakthroughs incorporate **quantum-transformer hybrids** into super-resolution, such as *QUIET‑SR*, a 2025 model that employs shifted quantum window attention within a transformer to enhance image detail while respecting diffraction and information-theory limits Similarly, **frequency-integrated transformers** (e.g., FIT) enrich super-resolution by explicitly combining spatial and frequency-domain information via FFT-based attention, improving reconstruction across scales
- Resolution and localization: True resolution involves the distinction of whether a target, e.g. a star or a spectral line, is single or double, ordinarily requiring separable peaks in the image. When a target is known to be single, its location can be determined with higher precision than the image width by finding the centroid (center of gravity) of its image light distribution. The word *ultra-resolution* had been proposed for this process but it did not catch on, and the high-precision localization procedure is typically referred to as super-resolution.

## Techniques

### Optical or diffractive super-resolution

Substituting spatial-frequency bands: Though the bandwidth allowable by diffraction is fixed, it can be positioned anywhere in the spatial-frequency spectrum. Dark-field illumination in microscopy is an example. See also aperture synthesis.

#### Multiplexing spatial-frequency bands

An image is formed using the normal passband of the optical device. Then, some known light structure (for example, a set of light fringes) is superimposed on the target. The image now contains components resulting from the combination of the target and the superimposed light structure, e.g. moiré fringes, and carries information about target detail which simple unstructured illumination does not. The “superresolved” components, however, need disentangling to be revealed. For an example, see structured illumination (figure to left).

#### Multiple parameter use within traditional diffraction limit

If a target has no special polarization or wavelength properties, two polarization states or non-overlapping wavelength regions can be used to encode target details, one in a spatial-frequency band inside the cut-off limit the other beyond it. Both would use normal passband transmission but are then separately decoded to reconstitute target structure with extended resolution.

#### Probing near-field electromagnetic disturbance

Super-resolution microscopy is generally discussed within the realm of conventional optical imagery. However, modern technology allows the probing of electromagnetic disturbance within molecular distances of the source, which has superior resolution properties. See also evanescent waves and the development of the new super lens.

### Geometrical or image-processing super-resolution

#### Multi-exposure image noise reduction

When an image is degraded by noise, the resolution may be improved by averaging multiple exposures. See example on the right.

#### Single-frame deblurring

Known defects in a given imaging situation, such as defocus or aberrations, can sometimes be mitigated in whole or in part by suitable spatial-frequency filtering of even a single image. Such procedures all stay within the diffraction-mandated passband, and do not extend it.

#### Sub-pixel image localization

The location of a single source can be determined by computing the "center of gravity" (centroid) of the light distribution extending over several adjacent pixels (see figure on the left). Provided that there is enough light, this can be achieved with arbitrary precision, very much better than pixel width of the detecting apparatus and the resolution limit for the decision of whether the source is single or double. This technique, which requires the presupposition that all the light comes from a single source, is at the basis of what has become known as super-resolution microscopy, e.g. stochastic optical reconstruction microscopy (STORM), where fluorescent probes attached to molecules give nanoscale distance information. It is also the mechanism underlying visual hyperacuity.

#### Bayesian induction beyond traditional diffraction limit

Some object features, though beyond the diffraction limit, may be known to be associated with other object features that are within the limits and hence contained in the image. Then conclusions can be drawn, using statistical methods, from the available image data about the presence of the full object. The classical example is Toraldo di Francia's proposition of judging whether an image is that of a single or double star by determining whether its width exceeds the spread from a single star. This can be achieved at separations well below the classical resolution bounds, and requires the prior limitation to the choice "single or double?"

The approach can take the form of extrapolating the image in the frequency domain, by assuming that the object is an analytic function, and that we can exactly know the function values in some interval. This method is severely limited by the ever-present noise in digital imaging systems, but it can work for radar, astronomy, microscopy or magnetic resonance imaging. More recently, a fast single image super-resolution algorithm based on a closed-form solution to *$\ell _{2}-\ell _{2}$* problems has been proposed and demonstrated to accelerate most of the existing Bayesian super-resolution methods significantly.

## Aliasing

Geometrical SR reconstruction algorithms are possible if and only if the input low resolution images have been under-sampled and therefore contain aliasing. Because of this aliasing, the high-frequency content of the desired reconstruction image is embedded in the low-frequency content of each of the observed images. Given a sufficient number of observation images, and if the set of observations vary in their phase (i.e. if the images of the scene are shifted by a sub-pixel amount), then the phase information can be used to separate the aliased high-frequency content from the true low-frequency content, and the full-resolution image can be accurately reconstructed.

In practice, this frequency-based approach is not used for reconstruction, but even in the case of spatial approaches (e.g. shift-add fusion), the presence of aliasing is still a necessary condition for SR reconstruction.

## Technical implementations

There are many both single-frame and multiple-frame variants of SR. Multiple-frame SR uses the sub-pixel shifts between multiple low resolution images of the same scene. It creates an improved resolution image fusing information from all low resolution images, and the created higher resolution images are better descriptions of the scene. Single-frame SR methods attempt to magnify the image without producing blur. These methods use other parts of the low resolution images, or other unrelated images, to guess what the high-resolution image should look like. Algorithms can also be divided by their domain: frequency or space domain. Originally, super-resolution methods worked well only on grayscale images, but researchers have found methods to adapt them to color camera images. Recently, the use of super-resolution for 3D data has also been shown.

## Research

Research into using neural network computing to perform super-resolution image construction. For example, deep convolutional networks were used to generate a 1500x scanning electron microscope image from a 20x microscopic image of pollen grains. However, while this technique can increase the information content of an image, there is no guarantee that the upscaled features actually exist in the original image. For this reason deep convolutional upscalers are not appropriate for applications involving ambiguous inputs where the presence or absence of a single feature is critical. Hallucinated details in images taken for medical diagnosis, as an example, could be problematic.
