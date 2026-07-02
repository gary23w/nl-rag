---
title: "Path tracing (part 1/2)"
source: https://en.wikipedia.org/wiki/Path_tracing
domain: path-tracing
license: CC-BY-SA-4.0
tags: path tracing, monte carlo rendering, rendering equation, importance sampling
fetched: 2026-07-02
part: 1/2
---

# Path tracing

**Path tracing** is a rendering algorithm in computer graphics that simulates how light interacts with objects and participating media to generate realistic (*physically plausible*) images. It is based on earlier, more limited, ray tracing algorithms.

Path tracing is used to create photorealistic images for artistic purposes, and for applications such as architectural rendering and product design. It is also used to render frames for animated films, and visual effects for film and television. Because it can be very accurate and unbiased, it is commonly used to generate reference images when testing the quality of other rendering algorithms.

The technique uses the Monte Carlo method to compute estimates of global illumination and simulate the ways different materials reflect (or scatter), transmit, absorb, and emit light. It can incorporate simple modeling of the effects of aperture and lens (depth of field, and bokeh) and shutter speed (motion blur), or more realistic simulation of the optical components in a camera.

The algorithm works by describing illumination in a scene using the *rendering equation*, or *light transport equation*, and finding an approximate solution using Monte Carlo integration. An inefficient (but accurate) version of the algorithm can be very simple, and involves tracing a ray from the camera, allowing this ray to bounce in random directions as it hits different objects in the scene, and computing the amount of light transmitted along the path to the camera whenever the path encounters a light source. This process is repeated many times for each pixel (each repetition, with generated path and transmitted light, is called a *sample*), and the results are averaged. One main difference between this algorithm and standard ray tracing is that a single unbranching path is traced each time, while "Whitted-style" or "Cook-style" ray tracing recursively samples branching paths (e.g. when light is both reflected and refracted by a glass object).

More practical versions incorporate improvements such as quasi-Monte Carlo methods (techniques that distribute samples more evenly), importance sampling (take more samples of paths that are likely to transport more light), and *next event estimation* (allow a very limited form of branching, and sample additional paths that connect to the lights more directly).

Because path tracing uses random samples there is noise in the final image, which decreases as more samples are taken. Images commonly require many thousands of samples per pixel (spp) to reduce noise to an acceptable level, and denoising techniques (e.g. based on neural networks) are often used. Denoising is usually necessary when path tracing is used for real-time rendering in video games, because relatively few samples can be taken.

Many alternative algorithms for path tracing have been developed, although they do not always outperform more straightforward implementations. These include bidirectional path tracing (which traces paths forwards from the light source as well as backwards from the camera), Metropolis light transport, and ways of combining path tracing with photon mapping. Video games often use biased versions of path tracing to improve performance (e.g. limiting the number of bounces in each path). A family of techniques called ReSTIR has been developed that can help real-time path tracing by sharing data between nearby pixels and consecutive frames.


## History

Like all ray tracing methods, path tracing is based on ray casting, which Arthur Appel used for computer graphics rendering in the late 1960s. In 1980, John Turner Whitted published a recursive ray tracing algorithm that allows rendering images of scenes containing mirrored surfaces and refractive transparent objects. In 1984, Cook et al. described a form of ray tracing called *distributed ray tracing*, which uses Monte Carlo integration to render effects such as depth of field, motion blur, reflection from rough surfaces, and area lights. The same year, the radiosity method (not a ray tracing method) was published, which was the first physically based method for rendering diffuse global illumination. In 1986, Jim Kajiya published a paper exploring how to use distributed ray tracing to render physically-based global illumination, and this paper also introduced and named the method called "path tracing". Path tracing and other distributed ray tracing techniques were further refined in the late 1980s and early 1990s by researchers such as James Arvo and Peter Shirley, and by Greg Ward in the open source Radiance software.

Despite being theoretically able to render any lighting, the original form of path tracing can sometimes be very inefficient (or noisy) for rendering light that is reflected or refracted before illuminating a visible surface, including diffuse global illumination where light enters an area through narrow gaps, because it traces paths only from the camera. To address this, variations of path tracing that trace paths from both the camera and from light sources, called *bidirectional path tracing*, were published in 1993 by Eric Lafortune and Yves Willems, and in 1997 by Eric Veach and Leonidas Guibas. In 1997 Veach and Guibas also published an alternative method called *Metropolis light transport*, which combines bidirectional path tracing with the Metropolis method. Veach's lengthy Ph.D. dissertation described both techniques, along with the theoretical background of path tracing; later, the book Physically Based Rendering (which won an Academy Award for Technical Achievement in 2014) helped to make information about path tracing more widely available.

Path tracing requires tracing a large number of *paths* of light in order to produce an image with a visually acceptable amount of noise. This made path tracing very slow on computers available in the 1980s and 1990s, and noise remained a problem when trying to reproduce the style of earlier computer graphics animated films. Most animated films produced until around 2010, by studios such as Pixar, used rasterization-based rendering, with ray tracing used selectively for reflections (and later for precomputed or cached global illumination). However the speed of computers rapidly increased during the 1990s. Blue Sky Studios pioneered using Monte Carlo ray tracing for global illumination in animation, including in the 1998 short film "Bunny", but they did not disclose the precise techniques used.

Path tracing gradually become more practical for film production in the early 2000s. The Arnold renderer, developed by Marcos Fajardo, was used by Sony Pictures Imageworks to produce the feature-length film *Monster House*, released in 2006. Pixar rewrote their RenderMan software to use path tracing, and released their first feature-length path-traced film *Finding Dory* in 2016. Although path tracing still had a large computational cost, animation studios discovered that less human labor was required when using it, for example because global illumination no longer needed to be faked by manually placing lights. The amount of noise present in path traced images still caused difficulties, particularly when rendering motion blur (which was used extensively by earlier animated films) but denoising techniques were developed to address this. New techniques were also needed for rendering hair and fur, and to handle the extremely large scenes sometimes required by films.

Renderers such as Arnold, and Disney's Hyperion, originally only used CPUs for rendering, but as GPUs became more capable (and APIs such as CUDA, OpenCL, and OptiX were released) researchers and developers began adapting algorithms and implementations to use GPUs. GPUs can dramatically reduce rendering time: for example using a high-end GPU to accelerate portions of the rendering code can make it over 30 times faster than using only a high-end CPU.


## Description

Kajiya's 1986 paper defined a recursive integral equation called the rendering equation, which describes a simplified form of *light transport*. Using Monte Carlo integration for the integral on the right side of the equation leads fairly directly to the path tracing algorithm:

$I(x,x')=g(x,x')\left[\epsilon (x,x')+\int _{S}\rho (x,x',x'')I(x',x'')dx''\right]$

This expresses *I(x,x')*, the light arriving at point *x* from point *x'*, as the product of a *geometry term*, *g(x,x')*, which is 0 if there is something blocking the light between the two points and 1 otherwise, and the amount of light leaving point *x'* and traveling towards *x*. The light leaving point *x'* is the sum of the light emitted by the surface at *x'*, and the integral of the light arriving at *x'* from all other points in the scene (the integration domain *S*) and being reflected towards *x*. The factor *ρ(x,x',x'')*, which calculates how much light is reflected, must take into account the angles at which the light is arriving and leaving, and characteristics of the surface material, typically expressed as a *bidirectional reflectance distribution function* (BRDF) or *bidirectional transmission distribution function* (BTDF).

The equation is often called the *light transport equation* (LTE), and it is frequently written using integration over directions instead of surfaces. (In Kajiya's version of the equation, the geometry term ensures that only one surface point can contribute light from any given direction.) Actual rendering also involves a related equation called the *measurement equation* that expresses the amount of light received by the camera along particular rays.

The version of the equation used by Kajiya assumes the light is a single wavelength (wavelength does not appear as a parameter for any of the functions). It is a simplification for geometrical optics, and does not take into account phenomena such as diffraction, polarization, and fluorescence. It integrates only over surfaces, and does not handle *participating media* (regions of space that scatter, absorb, and emit light). However extensions to handle such cases, and multiple wavelengths, were mentioned in the paper, and were well understood (and there is no fundamental limitation of the path tracing algorithm that prevents rendering these effects).

Kajiya described how older ray tracing methods find approximate solutions to the rendering equation. He also showed that the rendering equation is equivalent to the *radiosity equation* solved by the radiosity rendering method; however the radiosity method assumes surfaces are Lambertian, and using it for non-Lambertian materials gives inaccurate (biased) values. Additional bias is caused by the fact that the radiosity method uses finite element approximations of surfaces. Kajiya adapted existing distributed ray tracing methods to solve the rendering equation (i.e. to find radiance values at chosen points on surfaces for a steady state or equilibrium solution to light transport in the scene) in an unbiased way, using Monte Carlo integration.

In Whitted-style recursive ray tracing, the integral on the right side of the equation is replaced by a sum of the contributions of specific reflected and refracted rays, and the direct light arriving at the point from all light sources in the scene (lights may be point source or directional, so lighting can be evaluated easily, or some approximation may be used for other types of lights). A constant "ambient term" may be added to approximate global illumination. Distributed ray tracing introduced the use of Monte Carlo integration for rendering rough reflection, sampling multiple directions at each bounce instead of using the contribution of a single direction, but diffuse global illumination was still usually approximated using an ambient term.

The problem with using Monte Carlo integration for diffuse global illumination is the high variance of the result (requiring many samples to reduce noise to an acceptable level). To address this, the paper first explored stratified sampling approaches. Distributed ray tracing allows multiple branching rays to be traced at each step, and a method called "hierarchical integration", using independent stratification of the integration domain at each step, had previously been explored. However global illumination requires sampling larger domains of directions or surface points. Adaptively stratifying these domains in order to reduce variance was found to be too difficult. Importance sampling, where samples are chosen from a non-uniform distribution according to how much they are likely to contribute to the final result, was identified as a more viable approach.

When using importance sampling, hierarchical integration (via recursive ray tracing) is no longer necessary, and this led to the formulation of *path tracing*:

> This diagram also points out an alternative algorithm for conventional distributed ray tracing. Rather than shooting a branching tree, just shoot a path with the rays chosen probabilistically. For scenes with much reflection and refraction, this cuts down vastly on the number of ray object intersections to be computed for a given pixel and performs a remarkable speed up of ray tracing for very little programming work. However, for this new fast form of ray tracing—called path tracing—we have found that it is very important to maintain the correct proportion of reflection, refraction, and shadow ray types contributing to each pixel.

— James T. Kajiya, "The Rendering Equation"


## Algorithm

Ray tracers are often implemented using recursive functions, however a path tracer by nature does not need to be recursive, and can use a loop instead.

Here is pseudocode for a non-recursive function that traces a single path. It can either use *next event estimation* (NEE) or wait until the path hits a light by chance before accumulating light. It uses *cosine-weighted* sampling of ray directions, which is effective for diffuse surfaces (it is optimal for Lambertian surfaces) and simplifies the code:

```
function TracePath(cameraRay):
    ray ← cameraRay
    throughput ← 1
    value ← 0

    loop:
        intersection ← FirstRayIntersection(ray)
        
        if [using NEE]:
            lightSample ← SampleLights()
            value ← value + throughput × ComputeLightAmount(ray, intersection, lightSample)
        else if [intersection object is a light]:
            value ← value + throughput × intersection.emittedLight
        
        newDirection ← CosineWeightedSample(intersection.surfaceNormal)

        throughput ← throughput × π × intersection.BRDF(−ray.direction, intersection.surfaceNormal, newDirection)
        
        ray.start ← intersection.location
        ray.direction ← newDirection
        
        q ← ComputeTerminationProbability(throughput)
        
        if random() < q:
            return value
        
        throughput ← throughput / (1 - q)
```

The code uses "ray" values that consist of a start point in 3D space and a normalized direction vector. When simulating a pinhole camera, the input camera ray should use the camera location as the start point, and a direction chosen based on the pixel location. The function should be called multiple times for each pixel, using the average of the returned results as the final pixel value. The `random()` function should return a value between 0 and 1.

For simplicity, the code only works for opaque surface materials, and it assumes the scene is enclosed (rays can never exit the scene). It only traces a single wavelength of light, but could be modified to work with RGB values or spectral rendering (see below). Light sources handled in the non-NEE case are assumed to be perfectly diffuse (otherwise, instead of a constant emittedLight value, another function would need to be evaluated to compute the amount of light emitted in the opposite direction to the ray).

The code uses a trick known as *Russian roulette* to make the function unbiased by terminating the loop probabilistically. Provided `ComputeTerminationProbability` returns a value greater than 0 (or eventually does, e.g. when `throughput` drops below a threshold) then the loop will eventually terminate (by returning the accumulated value). Whenever "q" is greater than 0 and the loop keeps going, `throughput` is increased to compensate for the fact that other sampled paths may have been terminated at that point. This ensures that the result has the correct expected value.

The "q" value can be computed using any heuristic (even a constant probability could be used), but to make it effective, if `throughput` drops to a very low value (close to zero) then q should be close to 1. If larger termination probabilities are used, paths will tend to be shorter, but variance will be higher (there will be fewer long paths, but the throughput in those paths will be increased by a larger factor, which will tend to produce scattered bright pixels).

`CosineWeightedSample` samples directions in the hemisphere at a point on a surface, with probability proportional to the cosine of the angle between the direction and the surface normal (equivalent to integrating using the *projected solid angle* measure). This is commonly done for diffuse surfaces, and it simplifies the code because the cosine factor in the throughput formula and the inverse probability factor (required for importance sampling) cancel. Otherwise, direction sampling usually tries to use probabilities proportional to the product of the BRDF and the cosine factor. For perfectly specular surfaces, only a single direction is possible and slightly different code must be used.

The BRDF value is multiplied by *π* to cancel out the factor 1/*π* included in the BRDF by convention. (This convention comes from the fact that the integral of the cosine of the angle between the direction and the surface normal over the entire hemisphere is *π*, and so the BRDF for a perfect, non-absorbing, Lambertian surface must include a normalization factor of 1/*π* to make it evaluate to 1.) The 1/*π* factor can also be seen as part of the PDF for cosine-weighted sampling (which also includes the cosine factor that has been canceled), and since we need to divide by the PDF we multiply by *π*. Example path tracing code often explicitly computes the full PDF for cosine-weighted sampling and then divides by it (and multiplies the BRDF by the cosine factor, since it is no longer canceled) – this is also what the code needs to do if it uses a distribution other than the cosine-weighted distribution for sampling directions.


## Components of a modern path tracer

To improve performance and turn path tracing into a useful algorithm for rendering complex, realistic images, various techniques and enhancements are incorporated into the rendering engine.

### Sampling

#### Importance sampling

Importance sampling is a standard technique to reduce the variance (in this context, average squared magnitude of the error) of the result of Monte Carlo integration. It can significantly reduce the number of samples required to render a path traced image with an acceptable amount of noise. It involves choosing a probability density function (PDF) that is roughly proportional to the value being integrated, and drawing samples from that probability density instead of from a uniform distribution.

Surface materials do not reflect the same amount of light in all directions, and so a common type of importance sampling used in path tracing is to draw samples (in this case, directions from a hemisphere around a surface point) from a PDF that has the same shape as the bidirectional reflectance distribution function (BRDF) used for the material (see #Scattering distribution functions below) when choosing a direction for the next ray in a path. This is especially effective for glossy or shiny materials.

#### Multiple importance sampling

Importance sampling requires selecting a single probability density function (PDF) from which to draw the samples used for Monte Carlo integration, but often in path tracing, there are multiple alternative PDFs that can be used. For example, this can occur when integrating a function that is the product of two other functions, if there are good PDFs known for sampling the two functions individually, but not for sampling the product. Either one of the PDFs must be chosen, or some method must be found for combining them.

A common case is sampling the amount of direct light from an area light that is reflected by a point on the surface of an object towards the camera. When choosing the ray direction to sample at the object's surface point, either a random point on the surface of the light can be chosen (without using information about the object's surface material) and then the direction of the ray towards that light point can be computed, or a ray direction can be sampled proportional to the bidirectional reflectance distribution function (BRDF) of the object's surface (without taking the light location and shape into consideration). The first strategy ensures that the sampled ray does not miss the light, but for a glossy surface it may choose a direction at which very little light is reflected towards the camera, so it is more effective for rough (diffuse) surfaces. The second strategy is often effective for glossy surfaces because it will likely choose a direction at which the value of the BRDF is high, but the ray in the chosen direction may miss the light.

In simpler forms of path tracing, usually the first strategy is used for direct light, and is known as *next event estimation* (NEE), and the algorithm then continues tracing the path to sample indirect light, using the second strategy to select the sampled direction. If the next ray hits the surface of the light by chance (the light is usually also an object in the scene), the emitted light from the surface is ignored because otherwise that light would be counted twice. This works well for diffuse surfaces, but is not optimal for glossy surfaces.

A method called *multiple importance sampling* (MIS) allows using both types of sampling together, avoiding situations where a suboptimal strategy is chosen or values are counted twice (causing bias). MIS computes weights for blending the two samples so that the result is unbiased, and a larger weight is given to the strategy that is more likely to be effective. Weights are chosen using a heuristic, and an unbiased result will be produced if the weights satisfy certain conditions. Although various heuristics have been devised, some of which may be more effective in different situations, the *balance heuristic* is broadly applicable. A variation called the *one-sample model* selects one sampling strategy to use instead of blending multiple samples, and in this variation the balance heuristic always minimizes variance.

MIS can be used whenever multiple alternative probability density functions (PDFs) are available to use for importance sampling, and none of the alternatives is clearly better in all situations (some of the PDFs might only partially cover the domain being sampled). It is an essential component of bidirectional path tracing (see below).

#### Quasi-Monte Carlo sampling

The basic path tracing algorithm uses a random number generator to choose ray directions to sample at each point in the path (and points on lights, if next event estimation is used). This ensures that the result is unbiased, and avoids creating visible artifacts in the image. However when path tracing is repeated and the samples are averaged, because the sampled directions are completely random, they will not sample the integration domain evenly (there will be clumps and gaps in the directions that are sampled). This is normal and unavoidable for standard Monte Carlo integration, but there are techniques called *quasi-Monte Carlo* techniques that can reduce the variance by making the samples more evenly distributed. This means that the samples no longer have the randomness properties required by standard Monte Carlo integration, and so it must be done carefully to avoid bias and artifacts.

The simplest way of doing this is to break the domain being sampled (e.g. the hemisphere of ray directions leaving a surface) into segments and choosing a random point in each segment. This is called *stratified sampling*, and its drawbacks are that the number of samples being taken must be known in advance, and clumping may still occur (samples from adjacent segments may be very close together if they are both at the edge of a segment).

If the number of samples is not known in advance, methods called *low-discrepancy sequences* can be used to generate samples that tend to be spread out and cover the domain evenly. Popular sequences with this property include Halton and Sobol' sequences. These are predefined (non-random) sequences, but in modern path tracers the sequences are permuted (*scrambled*) to make them more random.

Stratified sampling and low-discrepancy sequences can become less effective as the dimension of the domain being sampled increases. Path tracing involves generating very high-dimensional samples. E.g. simple path tracing of opaque surfaces (with no light sampling) uses samples that have dimension equal to twice the number of bounces in the path, because each ray direction is a 2D sample on a hemisphere. If stratified sampling or a low-discrepancy sequence is used independently for each bounce, there will likely be correlations between the bounce directions, which will cause bias in the image, and also the complete samples (including all bounce directions) will not cover the domain evenly. Path tracers typically use very high dimensional low discrepancy sequences, but this means that sampling of individual bounces (considered independently as 2D samples) may not be optimal. A simple technique called *padding* improves this, and a more expensive technique called *sliced optimal transport* generates sequences where all lower-dimensional projections of the multidimensional samples tend to be evenly distributed, by repeatedly optimizing 1D slices.

The above techniques ensure that the set of paths sampled for each individual pixel is well-distributed. Techniques based on blue noise can help ensure that samples for adjacent pixels tend to be widely separated. This is usually more important when only a small number of paths is traced per pixel.

#### Spectral rendering

Computer graphics commonly represents light values as vectors of red, green, and blue components. Color or albedo for surfaces is similarly represented as separate multipliers for red, green, and blue. Although this approach can be adequate in some situations (e.g. it is accurate when light values are added together), when applied to path tracing it is equivalent to simulating a scene lit by exactly three wavelengths of light, which is not realistic. Modern path tracers provide the option to instead use random samples of wavelengths in the visible spectrum of light, which is called *spectral rendering*. This is now a standard approach when realistic, physically-based rendering is the goal.

For performance reasons, multiple (e.g. four) wavelengths are usually sampled at a time (a single path is traced, but the lighting calculations are performed for multiple wavelengths). This can also reduce the *color noise* that occurs with spectral sampling. Wavelengths are typically converted into RGB values when the path contributions are accumulated.

This approach allows simulating chromatic dispersion (e.g. "rainbows" visible when light hits a cut glass object). It also allows rendering scenes with more realistic light sources and materials, and correctly modeling diffuse global illumination and participating media, when light is bounced multiple times between colored surfaces or scattered by colored volumetric media (without exaggerated color or unnatural color shifts).

#### Path guiding

When indirect illumination varies strongly with direction, sampling directions using only the surface material's bidirectional scattering distribution function (BSDF) can be inefficient. In such cases, *path guiding* builds a representation of the indirect illumination in the scene and uses it to draw samples. Practical methods can do this iteratively during rendering by learning an approximate spatio-directional radiance field in an unbiased manner.

### Spatial data structures

#### Ray-object intersection acceleration

One of the most common and expensive operations performed by a path tracer is finding the first object, and corresponding surface point, intersected by a light ray starting at a particular point and traveling in a particular direction (a similar but simpler operation is testing if there is anything blocking the light between two points in space). To speed this up, path tracers use a 3D spatial data structure. The structure most commonly used today is the bounding volume hierarchy (BVH), and recent GPUs provide a hardware-accelerated version of this. However other structures such as *k*-d trees and octrees have also been used. Some path tracers require that all objects be represented using triangle meshes, which simplifies code and data structures (hardware acceleration is also usually optimized for triangles).

#### Light sampling acceleration

Generating samples of direct light (for *next event estimation*) is most effective if importance sampling is used, which requires sampling lights proportionally to their brightness, and (ideally) inversely proportionally to the square of the distance to the light. When the scene has a large number of lights, it becomes prohibitively expensive to examine all lights and compute weights before choosing a small number of lights to sample.

*BVH light sampling*, using a spatial tree data structure, can speed up sampling while taking locations of lights into account. (An approach that only considers brightness, called *power* sampling, uses a simpler non-spatial data structure.) Lights that are close together are grouped together in the tree, and the total brightness of the lights in each branch of the tree is stored. Spatial bounds for the branches of the tree allow quickly skipping lights that are behind the surface for which direct light is being estimated, and also allow weighting groups of lights based on direction and distance. Use of a tree for sampling is unbiased because the aggregate data is only used to compute sampling probabilities, not for the light amount used for rendering. A biased algorithm called *lightcuts* uses a similar tree, but approximates groups of distant lights (branches of the tree) by treating them as a single light, instead of importance sampling individual lights.

### Turning samples into images

#### Filtering

If path tracing only uses camera rays corresponding to the exact centers of pixels in the image, severe aliasing can result. Path tracers usually remove or reduce aliasing by filtering out frequencies higher than can be represented by the image's resolution. To do this, they use a filter kernel, such as a Gaussian filter, or filters such as Mitchell–Netravali filters or the Lanczos filter that improve sharpness but can introduce ringing artifacts. Either locations around the pixel center are sampled, weighted by the filter kernel (called *filter importance sampling*), or locations on the camera plane are sampled uniformly (usually with stratified sampling, so the same number of samples is taken in the square around each pixel) and then samples are added to any pixels whose kernels intersect the sample (called *weighted importance sampling*). The latter approach can reduce variance slightly, but may not be compatible with denoisers (for example, the occasional very bright samples called "fireflies" are spread across a neighborhood of pixels, and cannot be easily removed).

#### Denoising

Even when thousands of paths are averaged, the output of path tracing usually contains visible noise. Although the most reliable (and unbiased) way to reduce noise is to trace more paths (or make improvements such as better importance sampling), many biased approaches have been used to eliminate or reduce noise.

Path traced images often contain bright pixels colloquially called "fireflies", which can result when a path that was considered low priority by importance sampling (unlikely to produce a bright value) intersects a light source or a bright area of the scene, or when indirect light enters through a narrow gap and very few paths travel through that gap. Although technically these bright samples are necessary in order to produce an unbiased image, they are subjectively unhelpful, and they can greatly increase variance. Many heuristics have been used to identify fireflies and remove them, e.g. replacing them with the average of surrounding pixels or spreading their brightness out to nearby pixels. This is similar to outlier detection in statistics. Sometimes individual samples are filtered, rather than accumulated pixel values. Techniques related to density estimation, using variable-width kernels, have been tried.

Many techniques use edge detection to allow denoising filters that blur the image while still preserving sharp edges of objects. Edge detection for denoising a rendered image typically uses data other than the final brightness, such as the depth and normal vector of the first point intersected by the camera ray. Edge-preserving filters that do not rely on this type of data (using only pixel color and brightness values) include *bilateral filters*, *guided filters*, and *non-local means* filters. Techniques based on wavelets and other multiscale filters have been tried, which can handle the varying frequency characteristics of an image (e.g. blurriness caused by depth of field).

Sometimes the direct light and indirect light contributions to a pixel are rendered and denoised separately, which allows preserving detail in the direct lighting, while smoothing the indirect light (which is usually noisier). More complex algorithms denoise specular reflection separately (since it varies differently with pixel location), and some work with individual samples and construct a statistical model for the local light field around each visible point on a surface.

More recently, convolutional neural networks have been used to implement denoising filters, training the neural network on a large dataset of noisy and noiseless copies of the same images. These neural networks can use data such as depth and normal, surface albedo, and surface roughness/shininess as part of their inputs.

An alternative or complementary approach is *adaptive sampling*, which takes additional samples in regions of the image where variance is higher (this is tricky to do without introducing bias).

#### Tone mapping

The output of path tracing is linear brightness values for pixels, which then need to be converted into a viewable image or a video or film frame. The range of brightness values may be larger than displayable by a standard computer monitor, or representable by a file format that uses 8-bit color values, such as JPEG or PNG. Images often contain very bright highlights, or pixels where a light source such as the sun is seen directly. If the brightness of the entire image is reduced so that the brightest pixels are not clipped, the rest of the scene will often be too dark.

Methods called *tone mapping* or *tone reproduction* are often used to transform (or *map*) the pixel values in such *high dynamic range* (HDR) images into the range of values allowed by common file formats and computer monitors or other displays, while attempting to make details in both shadows and brighter areas visible, often incorporating models of how human vision responds to varying brightness. The aim is usually to produce a subjective impression of the true brightness of the scene, despite the reduced range of pixel values. Many different methods and tone mapping curves are available, often with parameters to tune them. Some methods aim to reproduce the look of images captured on photographic film, and may alter the colors and saturation of the image.

Tone mapping does not need to be implemented as part of the path tracer. If the rendered image is output to a linear HDR format (e.g. OpenEXR), tone mapping can be applied later (which may be preferable, since the tone mapping method or parameters can be changed without re-rendering the image).


## Scattering distribution functions

Real objects are never perfectly smooth mirrors (although perfect mirrors are often simulated in computer graphics for convenience and simplicity). When light hits an opaque object, it is always reflected (or *scattered*) in multiple directions. The amount of light that is reflected in each direction mainly depends on the angle at which it arrives relative to the *surface normal*. Shiny materials, often called *specular* materials, reflect more light at angles close to the angle at which a perfect mirror would reflect light, producing a distinct highlight (called a *specular highlight*) when a bright light source is reflected. In contrast, materials that scatter light more (reflecting it in a broader range of directions without a sharp peak) are called *rough* or *diffuse*. In general there is no clear distinction between specular and diffuse materials, for example a diffuse surface may have a coat of varnish over it that gives it specular highlights.

Materials for which the amount of light reflected in a particular direction depends only on the angles between the incoming ray of light (called the *incident* ray), the outgoing or reflected ray (called *exitant*), and the surface normal are called *isotropic*. In this case the surface material has no particular orientation (rotating the surface around the surface normal will not change the way light is reflected). Materials for which the orientation does matter are called *anisotropic*, and include materials such as brushed steel or aluminum. Although many real-world materials are subtly anisotropic, anisotropy is often ignored by computer graphics, since it is simpler and more efficient to treat materials as isotropic.

One extreme case is a "perfectly rough" material where the amount of reflected light does not depend on the angle of the incident light, and there are no highlights at all. An example of this type of material is the Lambertian material commonly used in computer graphics (it does not exist in the real world, but a material called Spectralon, which is a polymer powder, is very close). For a Lambertian material, the amount of reflected light is proportional to the cosine of the angle between the exitant ray and the surface normal.

The above effects can all be described by a type of function called a *bidirectional reflectance distribution function* (BRDF). The parameters to these functions are the directions of the incoming ray and the outgoing ray with respect to some frame of reference on the surface (there are multiple ways of representing the directions as numbers). The output of the function is a factor that the amount of incoming light should be multiplied by to get the amount of outgoing light. The BRDF, as typically defined, does not include the factor for Lambertian refectance mentioned above (the cosine of the angle between the exitant ray and the surface normal) and so the BRDF for a Lambertian surface is a constant function. Omitting this factor gives the BRDF the property of *reciprocity*: swapping the incident and exitant rays in the parameters to the function does not change the output (by convention, both directions point away from the surface). The BRDF is scaled appropriately for use in the light transport equations (where it is multiplied by incoming light values and integrated), and it returns a value of 1/*π* for a Lambertian material that does not absorb any light.

Along with reciprocity, an important property of valid BRDFs is that they are energy conserving: when the BRDF is used in light transport equations, the total amount of light reflected should never be greater than the amount of light arriving at the surface. (These properties will not hold for individual wavelengths when effects such as fluorescence are observed.) The BRDF must also always return a non-negative value.

BRDFs can be different for each wavelength of light. For example non-metallic materials usually have white highlights, reflecting all wavelengths nearly equally at certain angles, while also diffusely reflecting light in a wavelength-dependent way (which gives the material its color). Wavelength-varying BRDFs can also model iridescent materials.

BRDFs are a core part of path tracing: they are evaluated at every path vertex where a ray intersects a surface (in order to compute the throughput of the remaining part of the path), and also when computing direct lighting at surface points. BRDFs do not describe properties of transparent or partially transparent materials (for which other types of scattering distribution functions are needed). However BRDFs are useful because many materials are effectively opaque to visible light, or have a very small amount of translucency near the surface that can be ignored or approximated by the BRDF.

Although data for BRDFs can be obtained by measuring reflectance of real surfaces, the BRDFs used for rendering in practice are usually mathematical functions (often designed to simulate simplified physical properties of real surfaces) that are reasonably efficient to evaluate, and produce effects similar to real materials. They often have parameters such as "roughness" that can be easily changed. Multiple simple BRDFs (often called *lobes* due to the shape of the functions) are sometimes layered.

BRDFs do not, by themselves, include information about the texture of a surface. In realistic rendering, often color and "roughness" parameters (and sometimes orientation and amount of anisotropy) are encoded using texture mapping and used to modify the BRDF for individual points on the surface.

A similar type of function used when light passes through the surface of a transparent material is a *bidirectional transmittance distribution function* (BTDF). A term that includes both BRDFs and BTDFs is *bidirectional scattering distribution function* (BSDF). To handle general scattering in transparent materials, volume rendering uses a similar function (but with an incompatible definition) called a *phase function*.


## Volume rendering

Volumetric path tracing is used for rendering scenes containing *participating media*, which are 3D regions of space (rather than the surfaces of objects) that emit light, or in which light can be absorbed or scattered. Participating media are often thought of as containing particles, so that a ray of light passing through the medium has a chance of interacting with a particle (and being absorbed or scattered) that is higher the farther the ray travels. Path tracers that perform volume rendering usually allow it to be combined with rendering of surfaces. Kayija's rendering equation can be generalized for volumetric path tracing, however there are other volumetric light transport equations that may lead to more practical algorithms (just as the original form of the rendering equation is usually converted to use integrals over ray directions for standard path tracing).

Volumetric path tracing is commonly performed backwards from the camera, like standard path tracing, taking advantage of the reciprocity property of most light interactions. Camera rays are sampled (or ray directions for reflections or global illumination that arrives at a point on a surface) as usual, and then scattering events are generated when a ray passes through a participating medium that can scatter light. The probability of these scattering events (and how far the ray usually travels before the next event) is related to the density of the material. When a ray is scattered, a new ray is cast in the new direction, similar to scattering from a surface, with the probability of each new direction determined by a probability density function called a *phase function*.

Volumetric path tracing also uses integration to compute how much light is absorbed and scattered away when a ray passes through space (called *attenuation*), and how much light is emitted back along the ray (taking absorption and scattering along the ray into account) if the participating medium is emissive.

All of these operations are much simpler and faster if the participating medium is homogeneous (has the same density everywhere with respect to scattering, absorption, and emission). In that case integration can be performed analytically to compute attenuation and emission, and there is also a simpler way to generate scattering events with the correct probability distribution. Materials typically rendered as homogeneous media (which may still have complex shapes) include water and colored glass. The formula used for homogeneous absorption is known as the Beer–Lambert law or Beer's law.

When the participating medium is inhomogenous (has density or other properties that vary spatially) more complex and slower algorithms must be used. These types of media include clouds, mist, smoke, and fire. The input data for rendering these materials is usually volumetric data (structured similarly to voxels). To perform operations such as integration, the code often needs to ray march through the media, querying data for points along the ray. This can be done sparsely (examining the material at only a few, usually randomly chosen, points) or densely (examining closely spaced points), depending on the algorithm. The commonly used *null scattering* algorithm treats the medium as homogeneous when choosing which points to sample, allowing it to sample the medium sparsely, and it can be very efficient if the medium is nearly homogeneous.
