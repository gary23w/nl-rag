---
title: "Rendering (computer graphics) (part 2/2)"
source: https://en.wikipedia.org/wiki/Rendering_(computer_graphics)
domain: volumetric-rendering
license: CC-BY-SA-4.0
tags: volumetric rendering, volume ray marching, participating media rendering, radiative transfer volume
fetched: 2026-07-02
part: 2/2
---

## Techniques

Choosing how to render a 3D scene usually involves trade-offs between speed, memory usage, and realism (although realism is not always desired). The **algorithms** developed over the years follow a loose progression, with more advanced methods becoming practical as computing power and memory capacity increased. Multiple techniques may be used for a single final image.

An important distinction is between image order algorithms, which iterate over pixels in the image, and object order algorithms, which iterate over objects in the scene. For simple scenes, object order is usually more efficient, as there are fewer objects than pixels.

**2D vector graphics**

The

vector displays

of the 1960s-1970s used deflection of an

electron beam

to draw

line segments

directly on the screen. Nowadays,

vector graphics

are rendered by

rasterization

algorithms that also support filled shapes. In principle, any 2D vector graphics renderer can be used to render 3D objects by first projecting them onto a 2D image plane.

**3D rasterization**

Adapts 2D rasterization algorithms so they can be used more efficiently for 3D rendering, handling

hidden surface removal

via

scanline

or

z-buffer

techniques. Different realistic or stylized effects can be obtained by coloring the pixels covered by the objects in different ways.

Surfaces

are typically divided into

meshes

of triangles before being rasterized. Rasterization is usually synonymous with "object order" rendering (as described above).

**Ray casting**

Uses geometric formulas to compute the first object that a

ray

intersects.

It can be used to implement "image order" rendering by casting a ray for each pixel, and finding a corresponding point in the scene. Ray casting is a fundamental operation used for both graphical and non-graphical purposes,

e.g. determining whether a point is in shadow, or checking what an enemy can see in a

game

.

**Ray tracing**

Simulates the bouncing paths of light caused by

specular reflection

and

refraction

, requiring a varying number of ray casting operations for each path. Advanced forms use

Monte Carlo techniques

to render effects such as area lights,

depth of field

, blurry reflections, and

soft shadows

, but computing

global illumination

is usually in the domain of path tracing.

**Radiosity**

A

finite element analysis

approach that breaks surfaces in the scene into pieces, and estimates the amount of light that each piece receives from light sources, or indirectly from other surfaces. Once the

irradiance

of each surface is known, the scene can be rendered using rasterization or ray tracing.

**Path tracing**

Uses

Monte Carlo integration

with a simplified form of ray tracing, computing the average brightness of a

sample

of the possible paths that a photon could take when traveling from a light source to the camera (for some images, thousands of paths need to be sampled per pixel

). It was introduced as a

statistically unbiased

way to solve the

rendering equation

, giving ray tracing a rigorous mathematical foundation.

Each of the above approaches has many variations, and there is some overlap. Path tracing may be considered either a distinct technique or a particular type of ray tracing. Note that the usage of terminology related to ray tracing and path tracing has changed significantly over time.

Ray marching is a family of algorithms, used by ray casting, for finding intersections between a ray and a complex object, such as a volumetric dataset or a surface defined by a signed distance function. It is not, by itself, a rendering method, but it can be incorporated into ray tracing and path tracing, and is used by rasterization to implement screen-space reflection and other effects.

A technique called photon mapping traces paths of photons from a light source to an object, accumulating data about irradiance which is then used during conventional ray tracing or path tracing. Rendering a scene using only rays traced from the light source to the camera is impractical, even though it corresponds more closely to reality, because a huge number of photons would need to be simulated, only a tiny fraction of which actually hit the camera.

Some authors call conventional ray tracing "backward" ray tracing because it traces the paths of photons backwards from the camera to the light source, and call following paths from the light source (as in photon mapping) "forward" ray tracing. However, sometimes the meaning of these terms is reversed. Tracing rays starting at the light source can also be called *particle tracing* or *light tracing*, which avoids this ambiguity.

Real-time rendering, including video game graphics, typically uses rasterization, but increasingly combines it with ray tracing and path tracing. To enable realistic global illumination, real-time rendering often relies on pre-rendered ("baked") lighting for stationary objects. For moving objects, it may use a technique called *light probes*, in which lighting is recorded by rendering omnidirectional views of the scene at chosen points in space (often points on a grid to allow easier interpolation). These are similar to environment maps, but typically use a very low resolution or an approximation such as spherical harmonics. (Note: Blender uses the term 'light probes' for a more general class of pre-recorded lighting data, including reflection maps.)

Examples comparing different rendering techniques

- (3D rendered image showing three copies of a cartoon cow. The one on the left has a mirror surface, and the one on the right uses a transparent glass material. The shadows of the cows are blocky (like blurry pixels) due to low quality settings in the renderer.) A low quality rasterized image, rendered by Blender's EEVEE renderer with low shadow map resolution and a low-resolution mesh
- (3D rendered image showing three copies of a cartoon cow. The one on the left has a mirror surface, and the one on the right uses a transparent glass material. The image is speckled with many white dots, especially in the shadowed areas, due to low quality settings in the renderer. The reflection, transparency, and lighting are realistic, but the speckles distract from this.) A low quality path traced image, rendered by Blender's Cycles renderer with only 16 sampled paths per pixel and a low-resolution mesh
- (3D rendered image showing three copies of a cartoon cow. The one on the left has a mirror surface, and the one on the right uses a transparent glass material. The outlines are angular and there are some defects (due to the low-resolution mesh of the models), and the transparent cow has no shadow.) A ray traced image, using the POV-Ray program (using only its ray tracing features) with a low-resolution mesh
- (3D rendered image showing three copies of a cartoon cow. The one on the left has a mirror surface, and the one on the right uses a transparent glass material. The outlines of the cows and the shadows are smooth with no blockiness or angular defects, and the reflection looks quite realistic, but the transparency does not look convincing, and the lighting in the shadowed areas of the cows is not quite realistic.) A higher quality rasterized image, using Blender's EEVEE renderer with light probes
- (3D rendered image showing three copies of a cartoon cow. The one on the left has a mirror surface, and the one on the right uses a transparent glass material. The outlines of the cows and the shadows are smooth with no blockiness or angular defects. There are a few speckles of white pixels, but far fewer than in the low-quality image. The reflection, transparency, and lighting look realistic.) A higher quality path traced image, using Blender's Cycles renderer with 2000 sampled paths per pixel
- (3D rendered image showing three copies of a cartoon cow. The one on the left has a mirror surface, and the one on the right uses a transparent glass material. The outlines of the cows and the shadows are smooth with no blockiness or angular defects. The lighting is realistic, including in the shadowed areas. The base surface is illuminated by bright spots and lines ("caustics") caused by light being focused by the reflective and transparent cows.) An image rendered using POV-Ray's ray tracing, radiosity and photon mapping features
- (3D rendered image showing three copies of a cartoon cow. The one on the left has a metalic surface, and the one on the right uses a transparent glass material. The cow in the center appears made of glazed porcelain. The cows are standing on a wooden table. Lights and other background details from a cafe environment are reflected in the slightly glossy table and the cows.) A more realistic path traced image, using Blender's Cycles renderer with image-based lighting
- (3D rendered image showing three copies of a cartoon cow. The one on the left has a mirror surface, and the one on the right uses a transparent glass material. The base surface is illuminated by finely detailed bright spots and lines ("caustics") caused by light being focused by the reflective and transparent cows. The caustics are colorful in some places, due to chromatic dispersion.) A spectral rendered image, using POV-Ray's ray tracing, radiosity and photon mapping features

### Rasterization

The term *rasterization* (in a broad sense) encompasses many techniques used for 2D rendering and real-time 3D rendering. 3D animated films were rendered by rasterization before ray tracing and path tracing became practical.

A renderer combines rasterization with *geometry processing* (which is not specific to rasterization) and *pixel processing* which computes the RGB color values to be placed in the *framebuffer* for display.

The main tasks of rasterization (including pixel processing) are:

- Determining which pixels are covered by each geometric shape in the 3D scene or 2D image (this is the actual rasterization step, in the strictest sense)
- Blending between colors and depths defined at the vertices of shapes, e.g. using barycentric coordinates (*interpolation*)
- Determining if parts of shapes are hidden by other shapes, due to 2D layering or 3D depth (*hidden surface removal*)
- Evaluating a function for each pixel covered by a shape (*shading*)
- Smoothing edges of shapes so pixels are less visible (*anti-aliasing*)
- Blending overlapping transparent shapes (*compositing*)

3D rasterization is typically part of a *graphics pipeline* in which an application provides lists of triangles to be rendered, and the rendering system transforms and projects their coordinates, determines which triangles are potentially visible in the *viewport*, and performs the above rasterization and pixel processing tasks before displaying the final result on the screen.

Historically, 3D rasterization used algorithms like the *Warnock algorithm* and *scanline rendering* (also called "scan-conversion"), which can handle arbitrary polygons and can rasterize many shapes simultaneously. Although such algorithms are still important for 2D rendering, 3D rendering now usually divides shapes into triangles and rasterizes them individually using simpler methods.

High-performance algorithms exist for rasterizing 2D lines, including anti-aliased lines, as well as ellipses and filled triangles. An important special case of 2D rasterization is text rendering, which requires careful anti-aliasing and rounding of coordinates to avoid distorting the letterforms and preserve spacing, density, and sharpness.

After 3D coordinates have been projected onto the image plane, rasterization is primarily a 2D problem, but the 3rd dimension necessitates *hidden surface removal*. Early computer graphics used geometric algorithms or ray casting to remove the hidden portions of shapes, or used the *painter's algorithm*, which sorts shapes by depth (distance from camera) and renders them from back to front. Depth sorting was later avoided by incorporating depth comparison into the scanline rendering algorithm. The *z-buffer* algorithm performs the comparisons indirectly by including a depth or "z" value in the framebuffer. A pixel is only covered by a shape if that shape's z value is lower (indicating closer to the camera) than the z value currently in the buffer. The z-buffer requires additional memory (an expensive resource at the time it was invented) but simplifies the rasterization code and permits multiple passes. Memory is now faster and more plentiful, and a z-buffer is almost always used for real-time rendering.

A drawback of the basic z-buffer algorithm is that each pixel ends up either entirely covered by a single object or filled with the background color, causing jagged edges in the final image. Early *anti-aliasing* approaches addressed this by detecting when a pixel is partially covered by a shape, and calculating the covered area. The A-buffer (and other supersampling and multi-sampling techniques) solve the problem less precisely but with higher performance. For real-time 3D graphics, it has become common to use complicated heuristics (and even neural-networks) to perform anti-aliasing.

In 3D rasterization, color is usually determined by a *pixel shader* or *fragment shader*, a small program that is run for each pixel. The shader does not (or cannot) directly access 3D data for the entire scene (this would be very slow, and would result in an algorithm similar to ray tracing) and a variety of techniques have been developed to render effects like shadows and reflections using only texture mapping and multiple passes.

Older and more basic 3D rasterization implementations did not support shaders, and used simple shading techniques such as *flat shading* (lighting is computed once for each triangle, which is then rendered entirely in one color), *Gouraud shading* (lighting is computed using normal vectors defined at vertices and then colors are interpolated across each triangle), or *Phong shading* (normal vectors are interpolated across each triangle and lighting is computed for each pixel).

Until relatively recently, Pixar used rasterization for rendering its animated films. Unlike the renderers commonly used for real-time graphics, the Reyes rendering system in Pixar's RenderMan software was optimized for rendering very small (pixel-sized) polygons, and incorporated stochastic sampling techniques more typically associated with ray tracing.

### Ray casting

One of the simplest ways to render a 3D scene is to test if a ray starting at the viewpoint (the "eye" or "camera") intersects any of the geometric shapes in the scene, repeating this test using a different ray direction for each pixel. This method, called *ray casting*, was important in early computer graphics, and is a fundamental building block for more advanced algorithms. Ray casting can be used to render shapes defined by *constructive solid geometry* (CSG) operations.

Early ray casting experiments include the work of Arthur Appel in the 1960s. Appel rendered shadows by casting an additional ray from each visible surface point towards a light source. He also tried rendering the density of illumination by casting random rays from the light source towards the object and plotting the intersection points (similar to the later technique called *photon mapping*).

When rendering scenes containing many objects, testing the intersection of a ray with every object becomes very expensive. Special data structures are used to speed up this process by allowing large numbers of objects to be excluded quickly (such as objects behind the camera). These structures are analogous to database indexes for finding the relevant objects. The most common are the *bounding volume hierarchy* (BVH), which stores a pre-computed bounding box or sphere for each branch of a tree of objects, and the *k-d tree* which recursively divides space into two parts. Recent GPUs include hardware acceleration for BVH intersection tests. K-d trees are a special case of *binary space partitioning*, which was frequently used in early computer graphics (it can also generate a rasterization order for the painter's algorithm). *Octrees*, another historically popular technique, are still often used for volumetric data.

Geometric formulas are sufficient for finding the intersection of a ray with shapes like spheres, polygons, and polyhedra, but for most curved surfaces there is no analytic solution, or the intersection is difficult to compute accurately using limited precision floating point numbers. Root-finding algorithms such as Newton's method can sometimes be used. To avoid these complications, curved surfaces are often approximated as meshes of triangles. Volume rendering (e.g. rendering clouds and smoke), and some surfaces such as fractals, may require ray marching instead of basic ray casting.

### Ray tracing

Ray casting can be used to render an image by tracing light rays backwards from a simulated camera. After finding a point on a surface where a ray originated, another ray is traced towards the light source to determine if anything is casting a shadow on that point. If not, a *reflectance model* (such as Lambertian reflectance for matte surfaces, or the Phong reflection model for glossy surfaces) is used to compute the probability that a photon arriving from the light would be reflected towards the camera, and this is multiplied by the brightness of the light to determine the pixel brightness. If there are multiple light sources, brightness contributions of the lights are added together. For color images, calculations are repeated for multiple wavelengths of light (e.g. red, green, and blue).

*Classical ray tracing* (also called *Whitted-style* or *recursive* ray tracing) extends this method so it can render mirrors and transparent objects. If a ray traced backwards from the camera originates at a point on a mirror, the reflection formula from geometric optics is used to calculate the direction the reflected ray came from, and another ray is cast backwards in that direction. If a ray originates at a transparent surface, rays are cast backwards for both reflected and refracted rays (using Snell's law to compute the refracted direction), and so ray tracing needs to support a branching "tree" of rays. In simple implementations, a recursive function is called to trace each ray.

Ray tracing usually performs anti-aliasing by taking the average of multiple samples for each pixel. It may also use multiple samples for effects like depth of field and motion blur. If evenly spaced ray directions or times are used for each of these features, many rays are required, and some aliasing will remain. *Cook-style*, *stochastic*, or *Monte Carlo ray tracing* avoids this problem by using random sampling instead of evenly spaced samples. This type of ray tracing is commonly called *distributed ray tracing*, or *distribution ray tracing* because it samples rays from probability distributions. Distribution ray tracing can also render realistic "soft" shadows from large lights by using a random sample of points on the light when testing for shadowing, and it can simulate chromatic aberration by sampling multiple wavelengths from the spectrum of light.

Real surface materials reflect small amounts of light in almost every direction because they have small (or microscopic) bumps and grooves. A distribution ray tracer can simulate this by sampling possible ray directions, which allows rendering blurry reflections from glossy and metallic surfaces. However, if this procedure is repeated recursively to simulate realistic indirect lighting, and if more than one sample is taken at each surface point, the tree of rays quickly becomes huge. Another kind of ray tracing, called *path tracing*, handles indirect light more efficiently, avoiding branching, and ensures that the distribution of all possible paths from a light source to the camera is sampled in an unbiased way.

Ray tracing was often used for rendering reflections in animated films, until path tracing became standard for film rendering. Films such as Shrek 2 and Monsters University also used distribution ray tracing or path tracing to precompute indirect illumination for a scene or frame prior to rendering it using rasterization.

Advances in GPU technology have made real-time ray tracing possible in games, although it is currently almost always used in combination with rasterization. This enables visual effects that are difficult with only rasterization, including reflection from curved surfaces and interreflective objects, and shadows that are accurate over a wide range of distances and surface orientations. Ray tracing support is included in recent versions of the graphics APIs used by games, such as DirectX, Metal, and Vulkan.

Ray tracing has been used to render simulated black holes, and the appearance of objects moving at close to the speed of light, by taking spacetime curvature and relativistic effects into account during light ray simulation.

### Radiosity

Radiosity (named after the radiometric quantity of the same name) is a method for rendering objects illuminated by light bouncing off rough or matte surfaces. This type of illumination is called *indirect light*, *environment lighting*, *diffuse lighting*, or *diffuse interreflection*, and the problem of rendering it realistically is called *global illumination*. Rasterization and basic forms of ray tracing (other than distribution ray tracing and path tracing) can only roughly approximate indirect light, e.g. by adding a uniform "ambient" lighting amount chosen by the artist. Radiosity techniques are also suited to rendering scenes with *area lights* such as rectangular fluorescent lighting panels, which are difficult for rasterization and traditional ray tracing. Radiosity is considered a physically-based method, meaning that it aims to simulate the flow of light in an environment using equations and experimental data from physics, however it often assumes that all surfaces are opaque and perfectly Lambertian, which reduces realism and limits its applicability.

In the original radiosity method (first proposed in 1984) now called *classical radiosity*, surfaces and lights in the scene are split into pieces called *patches*, a process called *meshing* (this step makes it a finite element method). The rendering code must then determine what fraction of the light being emitted or diffusely reflected (scattered) by each patch is received by each other patch. These fractions are called *form factors* or *view factors* (first used in engineering to model radiative heat transfer). The form factors are multiplied by the albedo of the receiving surface and put in a matrix. The lighting in the scene can then be expressed as a matrix equation (or equivalently a system of linear equations) that can be solved by methods from linear algebra.

Solving the radiosity equation gives the total amount of light emitted and reflected by each patch, which is divided by area to get a value called *radiosity* that can be used when rasterizing or ray tracing to determine the color of pixels corresponding to visible parts of the patch. For real-time rendering, this value (or more commonly the irradiance, which does not depend on local surface albedo) can be pre-computed and stored in a texture (called an *irradiance map*) or stored as vertex data for 3D models. This feature was used in architectural visualization software to allow real-time walk-throughs of a building interior after computing the lighting.

The large size of the matrices used in classical radiosity (the square of the number of patches) causes problems for realistic scenes. Practical implementations may use Jacobi or Gauss-Seidel iterations, which is equivalent (at least in the Jacobi case) to simulating the propagation of light one bounce at a time until the amount of light remaining (not yet absorbed by surfaces) is insignificant. The number of iterations (bounces) required is dependent on the scene, not the number of patches, so the total work is proportional to the square of the number of patches (in contrast, solving the matrix equation using Gaussian elimination requires work proportional to the cube of the number of patches). Form factors may be recomputed when they are needed, to avoid storing a complete matrix in memory.

The quality of rendering is often determined by the size of the patches, e.g. very fine meshes are needed to depict the edges of shadows accurately. An important improvement is *hierarchical radiosity*, which uses a coarser mesh (larger patches) for simulating the transfer of light between surfaces that are far away from one another, and adaptively sub-divides the patches as needed. This allows radiosity to be used for much larger and more complex scenes.

Alternative and extended versions of the radiosity method support non-Lambertian surfaces, such as glossy surfaces and mirrors, and sometimes use volumes or "clusters" of objects as well as surface patches. Stochastic or Monte Carlo radiosity uses random sampling in various ways, e.g. taking samples of incident light instead of integrating over all patches, which can improve performance but adds noise (this noise can be reduced by using deterministic iterations as a final step, unlike path tracing noise). Simplified and partially precomputed versions of radiosity are widely used for real-time rendering, combined with techniques such as *octree radiosity* that store approximations of the light field.

### Path tracing

As part of the approach known as *physically based rendering*, **path tracing** has become the dominant technique for rendering realistic scenes, including effects for movies. For example, the popular open source 3D software Blender uses path tracing in its Cycles renderer. Images produced using path tracing for global illumination are generally noisier than when using radiosity (the main competing algorithm for realistic lighting), but radiosity can be difficult to apply to complex scenes and is prone to artifacts that arise from using a tessellated representation of irradiance.

Like *distributed ray tracing*, path tracing is a kind of *stochastic* or *randomized* ray tracing that uses Monte Carlo or Quasi-Monte Carlo integration. It was proposed and named in 1986 by Jim Kajiya in the same paper as the rendering equation. Kajiya observed that much of the complexity of distributed ray tracing could be avoided by only tracing a single path from the camera at a time (in Kajiya's implementation, this "no branching" rule was broken by tracing additional rays from each surface intersection point to randomly chosen points on each light source). Kajiya suggested reducing the noise present in the output images by using *stratified sampling* and *importance sampling* for making random decisions such as choosing which ray to follow at each step of a path. Even with these techniques, path tracing would not have been practical for film rendering, using computers available at the time, because the computational cost of generating enough samples to reduce variance to an acceptable level was too high. Monster House, the first feature film rendered entirely using path tracing, was not released until 20 years later.

In its basic form, path tracing is inefficient (requiring too many samples) for rendering caustics and scenes where light enters indirectly through narrow spaces. Attempts were made to address these weaknesses in the 1990s. *Bidirectional path tracing* has similarities to photon mapping, tracing rays from the light source and the camera separately, and then finding ways to connect these paths (but unlike photon mapping it usually samples new light paths for each pixel rather than using the same cached data for all pixels). *Metropolis light transport* samples paths by modifying paths that were previously traced, spending more time exploring paths that are similar to other "bright" paths, which increases the chance of discovering even brighter paths. *Multiple importance sampling* provides a way to reduce variance when combining samples from more than one sampling method, particularly when some samples are much noisier than the others.

This later work was summarized and expanded upon in Eric Veach's 1997 PhD thesis, which helped raise interest in path tracing in the computer graphics community. The Arnold renderer, first released in 1998, proved that path tracing was practical for rendering frames for films, and that there was a demand for unbiased and physically based rendering in the film industry; other commercial and open source path tracing renderers began appearing. Computational cost was addressed by rapid advances in CPU and cluster performance.

Path tracing's relative simplicity and its nature as a Monte Carlo method (sampling hundreds or thousands of paths per pixel) have made it attractive to implement on a GPU, especially on recent GPUs that support ray tracing acceleration technology such as Nvidia's RTX and OptiX. However bidirectional path tracing and Metropolis light transport are more difficult to implement efficiently on a GPU.

Techniques have been developed to denoise the output of path tracing, reducing the number of paths required to achieve acceptable quality, at the risk of losing some detail or introducing small-scale artifacts that are more objectionable than noise. Neural networks are now widely used for this purpose.

Research into improving path tracing continues. Many variations of bidirectional path tracing and Metropolis light transport have been explored, and ways of combining path tracing with photon mapping. Recent *path guiding* approaches construct approximations of the light field probability distribution in each volume of space, so paths can be sampled more effectively.

By combining denoising and hardware ray tracing acceleration, it is now practical to use path tracing for real-time rendering. Due to performance constraints, biased techniques such as a radiance cache may be incorporated. Spatiotemporal reservoir resampling (ReSTIR) aims to improve the quality of real-time path tracing and allow more complex lighting by reusing samples (paths) from previous frames and adjacent pixels.

### Machine learning

As of 2003, machine learning (ML) techniques were being used in other areas of computer graphics, such as texture synthesis, fitting surfaces to point clouds, and fitting curves to motion capture data. The use of ML for rendering expanded with the availability of GPUs that can evaluate neural networks (especially convolutional neural networks) quickly.

Neural networks and Gaussian mixture models have been used in conjunction with rendering techniques such as path tracing to encode bidirectional reflectance distribution functions (BRDFs), or to encode cached radiance at points in space (for biased acceleration of rendering or for path guiding). Neural radiance fields (NeRFs) take the latter approach to an extreme, encoding radiance at all points in a volume, and using evaluation of this approximation as the primary rendering method.

One of the most widely used applications of machine learning in rendering is denoising of path traced images (in practice, most path tracing now likely uses such a denoiser). Neural networks trained on pairs of noisy and low-noise images (or sometimes pairs of images with uncorrelated noise) can use data such as surface normal and albedo in addition to the rendered image, to reduce blurring or artifacts and preserve textures, and are effective at removing the scattered bright pixels called "fireflies" that frequently occur in path tracing. Denoisers specialized for real-time rendering can work with very low sample counts and improve temporal coherence to reduce flickering.


## Hardware acceleration

Rendering is usually limited by available computing power and memory bandwidth, and so specialized hardware has been developed to speed it up ("accelerate" it), particularly for real-time rendering. Hardware features such as a framebuffer for raster graphics are required to display the output of rendering smoothly in real time.

Hardware acceleration does not replace the use of software for rendering, rather it speeds up selected operations or calculations using dedicated circuits, or runs portions of the software's code on a different type of processor.

### History

In the era of vector monitors (also called *calligraphic displays*), a display processing unit (DPU) was a dedicated CPU or coprocessor that maintained a list of visual elements and redrew them continuously on the screen by controlling an electron beam. Advanced DPUs such as Evans & Sutherland's Line Drawing System-1 (and later models produced into the 1980s) incorporated 3D coordinate transformation features to accelerate rendering of wire-frame images. Evans & Sutherland also made the Digistar planetarium projection system, which was a vector display that could render both stars and wire-frame graphics (the vector-based Digistar and Digistar II were used in many planetariums, and a few may still be in operation). A Digistar prototype was used for rendering 3D star fields for the film Star Trek II: The Wrath of Khan – some of the first 3D computer graphics sequences ever seen in a feature film.

Shaded 3D graphics rendering in the 1970s and early 1980s was usually implemented on general-purpose computers, such as the PDP-10 used by researchers at the University of Utah. It was difficult to speed up using specialized hardware because it involves a pipeline of complex steps, requiring data addressing, decision-making, and computation capabilities typically only provided by CPUs (although dedicated circuits for speeding up particular operations were proposed ). Supercomputers or specially designed multi-CPU computers or clusters were sometimes used for ray tracing. In 1981, James H. Clark and Marc Hannah designed the Geometry Engine, a VLSI chip for performing some of the steps of the 3D rasterization pipeline, and started the company Silicon Graphics (SGI) to commercialize this technology.

Home computers and game consoles in the 1980s contained graphics coprocessors that were capable of scrolling and filling areas of the display, and drawing sprites and lines, though they were not useful for rendering realistic images. Towards the end of the 1980s PC graphics cards and arcade games with 3D rendering acceleration began to appear, and in the 1990s such technology became commonplace. Today, even low-power mobile processors typically incorporate 3D graphics acceleration features.

### GPUs

The 3D graphics accelerators of the 1990s evolved into modern GPUs. GPUs are general-purpose processors, like CPUs, but they are designed for tasks that can be broken into many small, similar, mostly independent sub-tasks (such as rendering individual pixels) and performed in parallel. This means that a GPU can speed up any rendering algorithm that can be split into subtasks in this way, in contrast to 1990s 3D accelerators which were only designed to speed up specific rasterization algorithms and simple shading and lighting effects (although tricks could be used to perform more general computations).

Due to their origins, GPUs typically still provide specialized hardware acceleration for some steps of a traditional 3D rasterization pipeline, including hidden surface removal using a z-buffer, and texture mapping with mipmaps, but these features are no longer always used. Recent GPUs have features to accelerate finding the intersections of rays with a bounding volume hierarchy, to help speed up all variants of ray tracing and path tracing, as well as neural network acceleration features sometimes useful for rendering.

GPUs are usually integrated with high-bandwidth memory systems to support the read and write bandwidth requirements of high-resolution, real-time rendering, particularly when multiple passes are required to render a frame, however memory latency may be higher than on a CPU, which can be a problem if the critical path in an algorithm involves many memory accesses. GPU design accepts high latency as inevitable (in part because a large number of threads are sharing the memory bus) and attempts to "hide" it by efficiently switching between threads, so a different thread can be performing computations while the first thread is waiting for a read or write to complete.

Rendering algorithms will run efficiently on a GPU only if they can be implemented using small groups of threads that perform mostly the same operations. As an example of code that meets this requirement: when rendering a small square of pixels in a simple ray-traced image, all threads will likely be intersecting rays with the same object and performing the same lighting computations. For performance and architectural reasons, GPUs run groups of around 16-64 threads called *warps* or *wavefronts* in lock-step (all threads in the group are executing the same instructions at the same time). If not all threads in the group need to run particular blocks of code (due to conditions) then some threads will be idle, or the results of their computations will be discarded, causing degraded performance.

### Hardware and software rendering

Historically, the term *hardware rendering* (possibly an abbreviation of "hardware accelerated rendering" or "hardware-assisted rendering") was sometimes used to mean rendering using a hardware-accelerated rasterization pipeline (typically for real-time rendering). In contrast, *software rendering* meant offline rendering using software that was not limited by the capabilities of graphics hardware, and could use more realistic and higher quality techniques. Both hardware and software have evolved, and although these terms are still used, their meaning may now be context-dependent.

When OpenGL and Direct3D were introduced in the 1990s, there was a need to use these APIs on computers that did not have hardware acceleration for 3D graphics. "Fallback" rendering implementations were provided that did not require special hardware, and these are sometimes called "software renderers" (today hardware acceleration is almost always available, and these CPU-only implementations are used primarily for testing). More recently, "software rendering" may also mean rendering that does not use graphics APIs such as OpenGL, Metal, Direct3D, or Vulkan.

Types of renderers that in the past might have been called "software renderers" (e.g. path tracing renderers used for offline rendering for movies) now commonly use GPU acceleration, often via APIs such as CUDA or OpenCL, which are not graphics-specific. Since these latter APIs allow running C++ code on a GPU, it is now possible to run the same rendering code on either a CPU or GPU.


## Chronology of algorithms and techniques

The following is a rough timeline of frequently mentioned rendering techniques, including areas of current research. Note that even in cases where an idea was named in a specific paper, there were almost always multiple researchers or teams working in the same area (including earlier related work). When a method is first proposed it is often very inefficient, and it takes additional research and practical efforts to turn it into a useful technique.

The list focuses on academic research and does not include hardware. (For more history see #External links, as well as Computer graphics#History and Golden age of arcade video games#Technology.)

- 1760 – Lambertian reflectance model
- 1931 – Standardized RGB representation of color
- 1967 – Torrance-Sparrow reflectance model
- 1968 – Ray casting
- 1968 – Warnock hidden surface removal
- 1970 – Scanline rendering
- 1971 – Gouraud shading
- 1973 – Phong shading
- 1973 – Phong reflectance model
- 1974 – Texture mapping
- 1974 – Z-buffering
- 1976 – Environment mapping
- 1977 – Blinn–Phong reflectance model
- 1977 – Shadow volumes
- 1978 – Shadow mapping
- 1978 – Bump mapping
- 1980 – BSP trees
- 1980 – Ray tracing
- 1981 – Cook-Torrance reflectance model
- 1983 – MIP maps
- 1984 – Octree ray tracing
- 1984 – Alpha compositing
- 1984 – Distributed ray tracing
- 1984 – Radiosity (method for non-trivial scenes in 1985)
- 1984 – A-buffer
- 1985 – Hemicube radiosity
- 1986 – Light source tracing
- 1986 – Rendering equation
- 1986 – Path tracing
- 1987 – Reyes rendering
- 1988 – Irradiance caching
- 1991 – Xiaolin Wu line anti-aliasing
- 1991 – Hierarchical radiosity
- 1993 – Oren–Nayar reflectance model
- 1993 – Tone mapping
- 1993 – Subsurface scattering
- 1993 – Bidirectional path tracing (Lafortune & Willems formulation)
- 1994 – Ambient occlusion
- 1995 – Photon mapping
- 1995 – Multiple importance sampling
- 1997 – Bidirectional path tracing (Veach & Guibas formulation)
- 1997 – Metropolis light transport
- 1997 – Instant Radiosity
- 2002 – Precomputed Radiance Transfer
- 2002 – Primary sample space Metropolis light transport
- 2003 – MERL BRDF database
- 2005 – Lightcuts
- 2005 – Radiance caching
- 2009 – Stochastic progressive photon mapping (SPPM)
- 2012 – Vertex connection and merging (VCM) (also called unified path sampling)
- 2012 – Manifold exploration
- 2013 – Gradient-domain rendering
- 2014 – Multiplexed Metropolis light transport
- 2014 – Differentiable rendering
- 2015 – Manifold next event estimation (MNEE)
- 2017 – Path guiding (using adaptive SD-tree)
- 2020 – Spatiotemporal reservoir resampling (ReSTIR)
- 2020 – Neural radiance fields
- 2023 – 3D Gaussian splatting
