---
title: "Light field"
source: https://en.wikipedia.org/wiki/Light_field
domain: irradiance-volumes
license: CC-BY-SA-4.0
tags: irradiance volume, volumetric light grid, diffuse global illumination cache, light field probe
fetched: 2026-07-02
---

# Light field

A **light field**, or **lightfield**, is a physical field that describes the amount of light flowing in every direction through every point in a three-dimensional space. The mathematical space of all possible light rays is given by the five-dimensional **plenoptic function** (with three position coordinates and two direction angles as arguments), and the magnitude of each ray is given by its radiance.

Michael Faraday was the first to propose that light should be interpreted as a field, much like the magnetic fields on which he had been working. The term *light field* was coined by Andrey Gershun in a classic 1936 paper on the radiometric properties of light in three-dimensional space.

The term "radiance field" may also be used to refer to similar, or identical concepts. The term is used in modern research such as neural radiance fields.

## Formulation

For geometric optics—i.e., in the regime of incoherent light and objects larger than the wavelength of light—the fundamental carrier of light is a ray. The measure for the amount of light traveling along a ray is radiance, denoted by *L* and expressed in units of W·sr−1·m−2; i.e., watts (W) per steradian (sr) per square meter (m2). The steradian is a measure of solid angle, and meters squared are used as a measure of cross-sectional area, as shown at right.

The radiance along all such rays in a region of three-dimensional space illuminated by an unchanging arrangement of lights is called the plenoptic function. The plenoptic illumination function is an idealized function used in computer vision and computer graphics to express the image of a scene from any possible viewing position at any viewing angle at any point in time. It is not used in practice computationally, but is conceptually useful in understanding other concepts in vision and graphics. Since rays in space can be parameterized by three coordinates, *x*, *y*, and *z* and two angles *θ* and *ϕ*, as shown at left, it is a five-dimensional function, that is, a function over a five-dimensional manifold equivalent to the product of 3D Euclidean space and the 2-sphere.

### Irradiance field

The light field at each point in space can be treated as an infinite collection of vectors, one per direction impinging on the point, with lengths proportional to their radiances.

Integrating these vectors over any collection of lights, or over the entire sphere of directions, produces a vector-valued function of 3D space called the **vector irradiance field**. The vector direction at each point in the field can be interpreted as the orientation of a flat surface placed at that point to most brightly illuminate it. The vector magnitude is a scalar-valued function of 3D space, called the **irradiance**.

### Higher dimensionality

Time, wavelength, and polarization angle can be treated as additional dimensions, yielding higher-dimensional functions, accordingly.

## The 4D light field

In a plenoptic function, if the region of interest contains a concave object (e.g., a cupped hand), then light leaving one point on the object may travel only a short distance before another point on the object blocks it. No practical device could measure the function in such a region.

However, for locations outside the object's convex hull (e.g., shrink-wrap), the plenoptic function can be measured by capturing multiple images. In this case the function contains redundant information, because the radiance along a ray remains constant throughout its length. The redundant information is exactly one dimension, leaving a four-dimensional function variously termed the photic field, the 4D light field or lumigraph. Formally, the field is defined as radiance along rays in empty space.

The set of rays in a light field can be parameterized in a variety of ways. The most common is the two-plane parameterization. While this parameterization cannot represent all rays, for example rays parallel to the two planes if the planes are parallel to each other, it relates closely to the analytic geometry of perspective imaging. A simple way to think about a two-plane light field is as a collection of perspective images of the *st* plane (and any objects that may lie astride or beyond it), each taken from an observer position on the *uv* plane. A light field parameterized this way is sometimes called a light slab.

### Sound analog

The analog of the 4D light field for sound is the sound field or wave field*,* as in wave field synthesis, and the corresponding parametrization is the Kirchhoff–Helmholtz integral, which states that, in the absence of obstacles, a sound field over time is given by the pressure on a plane. Thus this is two dimensions of information at any point in time, and over time, a 3D field.

This two-dimensionality, compared with the apparent four-dimensionality of light, is because light travels in rays (0D at a point in time, 1D over time), while by the Huygens–Fresnel principle, a sound wave front can be modeled as spherical waves (2D at a point in time, 3D over time): light moves in a single direction (2D of information), while sound expands in every direction. However, light travelling in non-vacuous media may scatter in a similar fashion, and the irreversibility or information lost in the scattering is discernible in the apparent loss of a system dimension.

## Image refocusing

Because light field provides spatial and angular information, we can alter the position of focal planes after exposure, which is often termed *refocusing*. The principle of refocusing is to obtain conventional 2-D photographs from a light field through the integral transform. The transform takes a lightfield as its input and generates a photograph focused on a specific plane.

Assuming $L_{F}(s,t,u,v)$ represents a 4-D light field that records light rays traveling from position $(u,v)$ on the first plane to position $(s,t)$ on the second plane, where F is the distance between two planes, a 2-D photograph at any depth $\alpha F$ can be obtained from the following integral transform:

${\mathcal {P}}_{\alpha }\left[L_{F}\right](s,t)={1 \over \alpha ^{2}F^{2}}\iint L_{F}\left(u\left(1-{\frac {1}{\alpha }}\right)+{\frac {s}{\alpha }},v\left(1-{\frac {1}{\alpha }}\right)+{\frac {t}{\alpha }},u,v\right)~dudv$

,

or more concisely,

${\mathcal {P}}_{\alpha }\left[L_{F}\right]({\boldsymbol {s}})={\frac {1}{\alpha ^{2}F^{2}}}\int L_{F}\left({\boldsymbol {u}}\left(1-{\frac {1}{\alpha }}\right)+{\frac {\boldsymbol {s}}{\alpha }},{\boldsymbol {u}}\right)d{\boldsymbol {u}}$

,

where ${\boldsymbol {s}}=(s,t)$ , ${\boldsymbol {u}}=(u,v)$ , and ${\mathcal {P}}_{\alpha }\left[\cdot \right]$ is the photography operator.

In practice, this formula cannot be directly used because a plenoptic camera usually captures discrete samples of the lightfield $L_{F}(s,t,u,v)$ , and hence resampling (or interpolation) is needed to compute ${\textstyle L_{F}\left({\boldsymbol {u}}\left(1-{\frac {1}{\alpha }}\right)+{\frac {\boldsymbol {s}}{\alpha }},{\boldsymbol {u}}\right)}$ . Another problem is high computational complexity. To compute an $N\times N$ 2-D photograph from an $N\times N\times N\times N$ 4-D light field, the complexity of the formula is $O(N^{4})$ .

### Fourier slice photography

One way to reduce the complexity of computation is to adopt the concept of Fourier slice theorem: The photography operator ${\mathcal {P}}_{\alpha }\left[\cdot \right]$ can be viewed as a shear followed by projection. The result should be proportional to a dilated 2-D slice of the 4-D Fourier transform of a light field. More precisely, a refocused image can be generated from the 4-D Fourier spectrum of a light field by extracting a 2-D slice, applying an inverse 2-D transform, and scaling. The asymptotic complexity of the algorithm is $O(N^{2}\operatorname {log} N)$ .

### Discrete focal stack transform

Another way to efficiently compute 2-D photographs is to adopt discrete focal stack transform (DFST). DFST is designed to generate a collection of refocused 2-D photographs, or so-called Focal Stack. This method can be implemented by fast fractional fourier transform (FrFT).

The discrete photography operator ${\mathcal {P}}_{\alpha }\left[\cdot \right]$ is defined as follows for a lightfield $L_{F}({\boldsymbol {s}},{\boldsymbol {u}})$ sampled in a 4-D grid ${\boldsymbol {s}}=\Delta s{\tilde {\boldsymbol {s}}},$ ${\tilde {\boldsymbol {s}}}=-{\boldsymbol {n}}_{\boldsymbol {s}},...,{\boldsymbol {n}}_{\boldsymbol {s}}$ , ${\boldsymbol {u}}=\Delta u{\tilde {\boldsymbol {u}}},{\tilde {\boldsymbol {u}}}=-{\boldsymbol {n}}_{\boldsymbol {u}},...,{\boldsymbol {n}}_{\boldsymbol {u}}$ :

${\mathcal {P}}_{q}[L]({\boldsymbol {s}})=\sum _{{\tilde {\boldsymbol {u}}}=-{\boldsymbol {n}}_{\boldsymbol {u}}}^{{\boldsymbol {n}}_{\boldsymbol {u}}}L({\boldsymbol {u}}q+{\boldsymbol {s}},{\boldsymbol {u}})\Delta {\boldsymbol {u}},\quad \Delta {\boldsymbol {u}}=\Delta u\Delta v,\quad q=\left(1-{\frac {1}{\alpha }}\right)$

Because $({\boldsymbol {u}}q+{\boldsymbol {s}},{\boldsymbol {u}})$ is usually not on the 4-D grid, DFST adopts trigonometric interpolation to compute the non-grid values.

The algorithm consists of these steps:

- Sample the light field $L_{F}({\boldsymbol {s}},{\boldsymbol {u}})$ with the sampling period $\Delta s$ and $\Delta u$ and get the discretized light field $L_{F}^{d}({\boldsymbol {s}},{\boldsymbol {u}})$ .
- Pad $L_{F}^{d}({\boldsymbol {s}},{\boldsymbol {u}})$ with zeros such that the signal length is enough for FrFT without aliasing.
- For every ${\boldsymbol {u}}$ , compute the Discrete Fourier transform of $L_{F}^{d}({\boldsymbol {s}},{\boldsymbol {u}})$ , and get the result $R1$ .
- For every focal length $\alpha F$ , compute the fractional fourier transform of $R1$ , where the order of the transform depends on $\alpha$ , and get the result $R2$ .
- Compute the inverse Discrete Fourier transform of $R2$ .
- Remove the marginal pixels of $R2$ so that each 2-D photograph has the size $(2{n}_{\boldsymbol {s}}+1)$ by $(2{n}_{\boldsymbol {s}}+1)$

## Methods to create light fields

In computer graphics, light fields are typically produced either by rendering a 3D model or by photographing a real scene. In either case, to produce a light field, views must be obtained for a large collection of viewpoints. Depending on the parameterization, this collection typically spans some portion of a line, circle, plane, sphere, or other shape, although unstructured collections are possible.

Devices for capturing light fields photographically may include a moving handheld camera or a robotically controlled camera, an arc of cameras (as in the bullet time effect used in *The Matrix*), a dense array of cameras, handheld cameras, microscopes, or other optical system.

The number of images in a light field depends on the application. A light field capture of Michelangelo's statue of *Night* contains 24,000 1.3-megapixel images, which is considered large as of 2022. For light field rendering to completely capture an opaque object, images must be taken of at least the front and back. Less obviously, for an object that lies astride the *st* plane, finely spaced images must be taken on the *uv* plane (in the two-plane parameterization shown above).

The number and arrangement of images in a light field, and the resolution of each image, are together called the "sampling" of the 4D light field. Also of interest are the effects of occlusion, lighting and reflection.

## Applications

### Illumination engineering

Gershun's reason for studying the light field was to derive (in closed form) illumination patterns that would be observed on surfaces due to light sources of various shapes positioned above these surface. The branch of optics devoted to illumination engineering is nonimaging optics. It extensively uses the concept of flow lines (Gershun's flux lines) and vector flux (Gershun's light vector). However, the light field (in this case the positions and directions defining the light rays) is commonly described in terms of phase space and Hamiltonian optics.

### Light field rendering

Extracting appropriate 2D slices from the 4D light field of a scene, enables novel views of the scene. Depending on the parameterization of the light field and slices, these views might be perspective, orthographic, crossed-slit, general linear cameras, multi-perspective, or another type of projection. Light field rendering is one form of image-based rendering.

### Synthetic aperture photography

Integrating an appropriate 4D subset of the samples in a light field can approximate the view that would be captured by a camera having a finite (i.e., non-pinhole) aperture. Such a view has a finite depth of field. Shearing or warping the light field before performing this integration can focus on different fronto-parallel or oblique planes. Images captured by digital cameras that capture the light field can be refocused.

### 3D display

Presenting a light field using technology that maps each sample to the appropriate ray in physical space produces an autostereoscopic visual effect akin to viewing the original scene. Non-digital technologies for doing this include integral photography, parallax panoramagrams, and holography; digital technologies include placing an array of lenslets over a high-resolution display screen, or projecting the imagery onto an array of lenslets using an array of video projectors. An array of video cameras can capture and display a time-varying light field. This essentially constitutes a 3D television system. Modern approaches to light-field display explore co-designs of optical elements and compressive computation to achieve higher resolutions, increased contrast, wider fields of view, and other benefits.

### Brain imaging

Neural activity can be recorded optically by genetically encoding neurons with reversible fluorescent markers such as GCaMP that indicate the presence of calcium ions in real time. Since light field microscopy captures full volume information in a single frame, it is possible to monitor neural activity in individual neurons randomly distributed in a large volume at video framerate. Quantitative measurement of neural activity can be done despite optical aberrations in brain tissue and without reconstructing a volume image, and be used to monitor activity in thousands of neurons.

### Generalized scene reconstruction (GSR)

This is a method of creating and/or refining a scene model representing a generalized light field and a relightable matter field. Data used in reconstruction includes images, video, object models, and/or scene models. The generalized light field represents light flowing in the scene. The relightable matter field represents the light interaction properties and emissivity of matter occupying the scene. Scene data structures can be implemented using Neural Networks, and Physics-based structures, among others. The light and matter fields are at least partially disentangled.

### Holographic stereograms

Image generation and predistortion of synthetic imagery for holographic stereograms is one of the earliest examples of computed light fields.

### Glare reduction

Glare arises due to multiple scattering of light inside the camera body and lens optics that reduces image contrast. While glare has been analyzed in 2D image space, it is useful to identify it as a 4D ray-space phenomenon. Statistically analyzing the ray-space inside a camera allows the classification and removal of glare artifacts. In ray-space, glare behaves as high frequency noise and can be reduced by outlier rejection. Such analysis can be performed by capturing the light field inside the camera, but it results in the loss of spatial resolution. Uniform and non-uniform ray sampling can be used to reduce glare without significantly compromising image resolution.
