---
title: "Bidirectional reflectance distribution function"
source: https://en.wikipedia.org/wiki/Bidirectional_reflectance_distribution_function
domain: path-tracing
license: CC-BY-SA-4.0
tags: path tracing, monte carlo rendering, rendering equation, importance sampling
fetched: 2026-07-02
---

# Bidirectional reflectance distribution function

The **bidirectional reflectance distribution function** (**BRDF**), symbol $f_{\text{r}}(\omega _{\text{i}},\,\omega _{\text{r}})$ , is a function of four real variables that defines how light from a source is reflected off an opaque surface. It is employed in the optics of real-world light, in computer graphics algorithms, and in computer vision algorithms. The function takes an incoming light direction, $\omega _{\text{i}}$ , and outgoing direction, $\omega _{\text{r}}$ (taken in a coordinate system where the surface normal $\mathbf {n}$ lies along the *z*-axis), and returns the ratio of reflected radiance exiting along $\omega _{\text{r}}$ to the irradiance incident on the surface from direction $\omega _{\text{i}}$ . Each direction $\omega$ is itself parameterized by azimuth angle $\phi$ and zenith angle $\theta$ , therefore the BRDF as a whole is a function of 4 variables. The BRDF has units sr−1, with steradians (sr) being a unit of solid angle.

## Definition

The BRDF was first defined by Fred Nicodemus around 1965. The definition is:

$f_{\text{r}}(\omega _{\text{i}},\,\omega _{\text{r}})\,=\,{\frac {\mathrm {d} L_{\text{r}}(\omega _{\text{r}})}{\mathrm {d} E_{\text{i}}(\omega _{\text{i}})}}\,=\,{\frac {\mathrm {d} L_{\text{r}}(\omega _{\text{r}})}{L_{\text{i}}(\omega _{\text{i}})\cos \theta _{\text{i}}\mathrm {d} \omega _{\text{i}}}}$

where L is radiance, or power per unit solid-angle-in-the-direction-of-a-ray per unit projected-area-perpendicular-to-the-ray, E is irradiance, or power per unit *surface area*, and $\theta _{\text{i}}$ is the angle between $\omega _{\text{i}}$ and the surface normal, $\mathbf {n}$ . The index ${\text{i}}$ indicates incident light, whereas the index ${\text{r}}$ indicates reflected light.

The reason the function is defined as a quotient of two differentials and not directly as a quotient between the undifferentiated quantities, is because irradiating light other than $\mathrm {d} E_{\text{i}}(\omega _{\text{i}})$ , which are of no interest for $f_{\text{r}}(\omega _{\text{i}},\,\omega _{\text{r}})$ , might illuminate the surface which would unintentionally affect $L_{\text{r}}(\omega _{\text{r}})$ , whereas $\mathrm {d} L_{\text{r}}(\omega _{\text{r}})$ is only affected by $\mathrm {d} E_{\text{i}}(\omega _{\text{i}})$ .

The **Spatially Varying Bidirectional Reflectance Distribution Function** (SVBRDF) is a 6-dimensional function, $f_{\text{r}}(\omega _{\text{i}},\,\omega _{\text{r}},\,\mathbf {x} )$ , where $\mathbf {x}$ describes a 2D location over an object's surface.

The **Bidirectional Texture Function** (BTF) is appropriate for modeling non-flat surfaces, and has the same parameterization as the SVBRDF; however in contrast, the BTF includes non-local scattering effects like shadowing, masking, interreflections or subsurface scattering. The functions defined by the BTF at each point on the surface are thus called **Apparent BRDFs**.

The **Bidirectional Surface Scattering Reflectance Distribution Function** (BSSRDF), is a further generalized 8-dimensional function $S(\mathbf {x} _{\text{i}},\,\omega _{\text{i}},\,\mathbf {x} _{\text{r}},\,\omega _{\text{r}})$ in which light entering the surface may scatter internally and exit at another location.

In all these cases, the dependence on the wavelength of light has been ignored. In reality, the BRDF is wavelength dependent, and to account for effects such as iridescence or luminescence the dependence on wavelength must be made explicit: $f_{\text{r}}(\lambda _{\text{i}},\,\omega _{\text{i}},\,\lambda _{\text{r}},\,\omega _{\text{r}})$ . Note that in the typical case where all optical elements are linear, the function will obey $f_{\text{r}}(\lambda _{\text{i}},\,\omega _{\text{i}},\,\lambda _{\text{r}},\,\omega _{\text{r}})=0$ except when $\lambda _{\text{i}}=\lambda _{\text{r}}$ : that is, it will only emit light at wavelength equal to the incoming light. In this case it can be parameterized as $f_{\text{r}}(\lambda ,\,\omega _{\text{i}},\,\omega _{\text{r}})$ , with only one wavelength parameter.

## Physically based BRDFs

Physically realistic BRDFs for reciprocal linear optics have additional properties, including,

- positivity: $f_{\text{r}}(\omega _{\text{i}},\,\omega _{\text{r}})\geq 0$
- obeying Helmholtz reciprocity: $f_{\text{r}}(\omega _{\text{i}},\,\omega _{\text{r}})=f_{\text{r}}(\omega _{\text{r}},\,\omega _{\text{i}})$
- conserving energy: $\forall \omega _{\text{i}},\,\int _{\Omega }f_{\text{r}}(\omega _{\text{i}},\,\omega _{\text{r}})\,\cos {\theta _{\text{r}}}d\omega _{\text{r}}\leq 1$

## Applications

The BRDF is a fundamental radiometric concept, and accordingly is used in computer graphics for photorealistic rendering of synthetic scenes (see the rendering equation), as well as in computer vision for many inverse problems such as object recognition. BRDF has also been used for modeling light trapping in solar cells (e.g. using the OPTOS formalism) or low concentration solar photovoltaic systems.

In the context of satellite remote sensing, NASA uses a BRDF model to characterise surface reflectance anisotropy. For a given land area, the BRDF is established based on selected multiangular observations of surface reflectance. While single observations depend on view geometry and solar angle, the MODIS BRDF/Albedo product describes intrinsic surface properties in several spectral bands, at a resolution of 500 meters. The BRDF/Albedo product can be used to model surface albedo depending on atmospheric scattering.

## Models

BRDFs can be measured directly from real objects using calibrated cameras and lightsources; however, many phenomenological and analytic models have been proposed including the Lambertian reflectance model frequently assumed in computer graphics. Some useful features of recent models include:

- accommodating anisotropic reflection
- editable using a small number of intuitive parameters
- accounting for Fresnel effects at grazing angles
- being well-suited to Monte Carlo methods.

W. Matusik et al. found that interpolating between measured samples produced realistic results and was easy to understand.

Diffuse

Glossy

Mirror

Three elemental components that can be used to model a variety of light-surface interactions.

The incoming light ray is shown in black, the reflected ray(s) modeled by the BRDF in gray.

### Some examples

- Lambertian model, representing perfectly diffuse (matte) surfaces by a constant BRDF.
- Lommel–Seeliger, lunar and Martian reflection.
- Hapke scattering model, physically motivated approximation of the radiative transfer solution for a porous, irregular, and particulate surface. Often used in astronomy for planet/small body surface reflection simulations. Multiple versions and modifications exist.
- Phong reflectance model, a phenomenological model akin to plastic-like specularity.
- Blinn–Phong model, resembling Phong, but allowing for certain quantities to be interpolated, reducing computational overhead.
- Torrance–Sparrow model, a general model representing surfaces as distributions of perfectly specular microfacets.
- Cook–Torrance model, a specular-microfacet model (Torrance–Sparrow) accounting for wavelength and thus color shifting.
- Ward model, a specular-microfacet model with an elliptical-Gaussian distribution function dependent on surface tangent orientation (in addition to surface normal).
- Oren–Nayar model, a "directed-diffuse" microfacet model, with perfectly diffuse (rather than specular) microfacets.
- Ashikhmin–Shirley model, allowing for anisotropic reflectance, along with a diffuse substrate under a specular surface.
- Trowbridge–Reitz model, a specular-microfacet model that models surfaces as consisting of microfacets of not only random orientation but also random curvature.
- HTSG (He, Torrance, Sillion, Greenberg), a comprehensive physically based model.
- Fitted Lafortune model, a generalization of Phong with multiple specular lobes, and intended for parametric fits of measured data.
- Lebedev model for analytical-grid BRDF approximation.
- ABC-like model for accurate and efficient rendering of glossy surfaces.
- ABg model
- K-correlation (ABC) model

## Acquisition

Traditionally, BRDF measurement devices called gonioreflectometers employ one or more goniometric arms to position a light source and a detector at various directions from a flat sample of the material to be measured. To measure a full BRDF, this process must be repeated many times, moving the light source each time to measure a different incidence angle. Unfortunately, using such a device to densely measure the BRDF is very time-consuming. One of the first improvements on these techniques used a half-silvered mirror and a digital camera to take many BRDF samples of a planar target at once. Since this work, many researchers have developed other devices for efficiently acquiring BRDFs from real world samples, and it remains an active area of research.

There is an alternative way to measure BRDF based on HDR images. The standard algorithm is to measure the BRDF point cloud from images and optimize it by one of the BRDF models.

A fast way to measure BRDF or BTDF is a conoscopic scatterometer The advantage of this measurement instrument is that a near-hemispheric measurement can be captured in a fraction of a second with resolution of roughly 0.1°. This instrument has two disadvantages. The first is that the dynamic range is limited by the camera being used; this can be as low as 8 bits for older image sensors or as high as 32 bits for the newer automotive image sensors. The other disadvantage is that for BRDF measurements the beam must pass from an external light source, bounce off a pellicle and pass in reverse through the first few elements of the conoscope before being scattered by the sample. Each of these elements is antireflection-coated, but roughly 0.3% of the light is reflected at each air-glass interface. These reflections will show up in the image as a spurious signal. For scattering surfaces with a large signal, this is not a problem, but for Lambertian surfaces it is.

## BRDF fabrication

BRDF fabrication refers to the process of implementing a surface based on the measured or synthesized information of a target BRDF. There exist three ways to perform such a task, but in general, it can be summarized as the following steps:

- Measuring or synthesizing the target BRDF distribution.
- Sample this distribution to discretize it and make the fabrication feasible.
- Design a geometry that produces this distribution (with microfacet, halftoning).
- Optimize the continuity and smoothness of the surface with respect to the manufacturing procedure.

Many approaches have been proposed for manufacturing the BRDF of the target :

- **Milling the BRDF:** This procedure starts with sampling the BRDF distribution and generating it with microfacet geometry then the surfaced is optimized in terms of smoothness and continuity to meet the limitations of the milling machine. The final BRDF distribution is the convolution of the substrate and the geometry of the milled surface.
- **Printing the BRDF:** In order to generate spatially varying BRDF (svBRDF) it has been proposed to use gamut mapping and halftoning to achieve the targeted BRDF. Given a set of metallic inks with known BRDF an algorithm proposed to linearly combine them to produce the targeted distribution.  So far printing only means gray-scale or color printing but real-world surfaces can exhibit different amounts of specularity that affects their final appearance, as a result this novel method can help us print images even more realistically.
- **Combination of Ink and Geometry:** In addition to color and specularity, real-world objects also contain texture. A 3D printer can be used to manufacture the geometry and cover the surface with a suitable ink; by optimally creating the facets and choosing the ink combination, this method can give us a higher degree of freedom in design and more accurate BRDF fabrication.
