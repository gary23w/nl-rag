---
title: "Rendering (computer graphics) (part 1/2)"
source: https://en.wikipedia.org/wiki/Rendering_(computer_graphics)
domain: paint-timing
license: CC-BY-SA-4.0
tags: paint timing api, first contentful paint, first paint metric, render performance milestone
fetched: 2026-07-02
part: 1/2
---

# Rendering (computer graphics)

**Rendering** is the process of generating an image from input data such as 3D models. The word "rendering" (in one of its senses) originally meant the task performed by an artist when depicting a real or imaginary thing (the finished artwork is also called a "rendering"). Today, to "render" commonly means to use a computer to generate an image from a precise specification, often created by an artist (or multiple artists) via interactive 3D modeling software. Types of images rendered include both still images and frames for films and video games.

In a computer graphics context, in standard usage, the word "rendering" by itself means rendering 3D scenes, but it is sometimes used with a broader meaning. A modifier such as "2D" or "3D" is used when there is potential ambiguity (e.g. **3D rendering**).

A software application or component that performs rendering is called a **rendering engine**, **render engine**, **rendering system**, **graphics engine**, or simply a **renderer**.

A distinction is made between real-time rendering, in which images are generated and displayed immediately (ideally fast enough to give the impression of motion or animation), and offline rendering (sometimes called pre-rendering) in which images or film frames, are generated for later viewing. Offline rendering can use a slower and higher-quality renderer. Interactive applications such as games must primarily use real-time rendering, although they may incorporate pre-rendered content.

Rendering produces images of scenes or objects defined using coordinates in 3D space, seen from a particular viewpoint. It uses knowledge and ideas from optics, the study of visual perception, mathematics, and software engineering, and it has applications such as video games, simulators, visual effects for films and television, design visualization, and medical diagnosis. Realistic rendering requires modeling the propagation of light in an environment, e.g. by applying the rendering equation.

Real-time rendering uses high-performance *rasterization* algorithms that process a list of shapes and determine which pixels are covered by each shape. When more realism is required (e.g. for architectural visualization or visual effects) slower pixel-by-pixel algorithms such as *ray tracing* are used instead. (Ray tracing can also be used selectively during rasterized rendering to improve the realism of lighting and reflections.) A type of ray tracing called *path tracing* is currently the most common technique for photorealistic rendering. Path tracing is also popular for generating high-quality non-photorealistic images, such as frames for 3D animated films. Both rasterization and ray tracing can be sped up ("accelerated") by specially designed microprocessors called GPUs.

Rasterization algorithms are also used to produce images containing only 2D shapes such as polygons and text. This type of rendering is sometimes called *2D rendering*, and its applications include digital illustration, graphic design, 2D animation, desktop publishing and the display of user interfaces.

Historically, rendering was called **image synthesis** but today this term is likely to mean AI image generation. The term "neural rendering" is sometimes used when a neural network is the primary means of generating an image but some degree of control over the output image is provided. Neural networks can also assist rendering without replacing traditional algorithms, e.g. by removing noise from path traced images.

**Notes**

1. "Rendering is the process of producing an image from the description of a 3D scene." Pharr et al., Physically Based Rendering, The MIT Press, 2023, Introduction


## Features

### Photorealistic rendering

A large proportion of computer graphics research has worked towards producing images that resemble photographs. Fundamental techniques that make this possible were invented in the 1980s, but at the end of the decade, photorealism for complex scenes was still considered a distant goal. Today, photorealism is routinely achievable for offline rendering, but remains difficult for real-time rendering.

In order to produce realistic images, rendering must simulate how light travels from light sources, is reflected, refracted, and scattered (often many times) by objects in the scene, passes through a camera lens, and finally reaches the film or sensor of the camera. The physics used in these simulations is primarily geometrical optics, in which particles of light follow (usually straight) lines called *rays*, but in some situations (such as when rendering thin films, like the surface of soap bubbles) the wave nature of light must be taken into account.

Effects that may need to be simulated include:

- Shadows, including both shadows with sharp edges and *soft shadows* with umbra and penumbra
- Reflections in mirrors and smooth surfaces, as well as rough or rippled reflective surfaces
- Refraction – the bending of light when it crosses a boundary between two transparent materials such as air and glass. The amount of bending varies with the wavelength of the light, which may cause colored fringes or "rainbows" to appear.
- Volumetric effects – absorption and scattering when light travels through partially transparent or translucent substances (called *participating media* because they modify the light rather than simply allow rays to pass through)
- Caustics – bright patches, sometimes with distinct filaments and a folded or twisted appearance, resulting when light is reflected or refracted before illuminating an object.

In realistic scenes, objects are illuminated both by light that arrives directly from a light source (after passing mostly unimpeded through air), and light that has bounced off other objects in the scene. The simulation of this complex lighting is called global illumination. In the past, indirect lighting was often faked (especially when rendering animated films) by placing additional hidden lights in the scene, but today path tracing is used to render it accurately.

For true photorealism, the camera used to take the photograph must be simulated. The *thin lens approximation* allows combining perspective projection with depth of field (and bokeh) emulation. Camera lens simulations can be made more realistic by modeling the way light is refracted by the components of the lens. Motion blur is often simulated if film or video frames are being rendered. Simulated lens flare and bloom are sometimes added to make the image appear subjectively brighter (although the design of real cameras tries to reduce these effects).

Realistic rendering uses mathematical descriptions of how different surface materials reflect light, called *reflectance models* or (when physically plausible) *bidirectional reflectance distribution functions (BRDFs)*. Rendering materials such as marble, plant leaves, and human skin requires simulating an effect called subsurface scattering, in which a portion of the light travels into the material, is scattered, and then travels back out again. The way color, and properties such as roughness, vary over a surface can be represented efficiently using texture mapping.

### Other styles of 3D rendering

For some applications (including early stages of 3D modeling), simplified rendering styles such as wireframe rendering may be appropriate, particularly when the material and surface details have not been defined and only the shape of an object is known. Games and other real-time applications may use simpler and less realistic rendering techniques as an artistic or design choice, or to allow higher frame rates on lower-end hardware.

Orthographic and isometric projections can be used for a stylized effect or to ensure that parallel lines are depicted as parallel in CAD rendering.

Non-photorealistic rendering (NPR) uses techniques like edge detection and posterization to produce 3D images that resemble technical illustrations, cartoons, or other styles of drawing or painting.

### 2D rendering

In 2D computer graphics the positions and sizes of shapes are specified using 2D coordinates (x and y) instead of 3D coordinates (x, y, and z). 2D rendering APIs often use a resolution-independent coordinate system, with a viewport determining how to convert coordinates to pixel indexes called *device coordinates*. Transformations such as scaling, translation, and rotation may be applied before rendering the shapes. These affine transformations are often represented by 3 × 3 matrices, allowing easier composition of transformations.

Higher-quality 2D rendering engines such as SVG renderers usually implement anti-aliasing to reduce the jagged appearance of rasterized lines and shape edges. When rendering overlapping shapes, renderers commonly use a "painter's model" in which the shapes are drawn in some determined order, or their contributions to each pixel are composited using blending operations that may depend on the order of the inputs. Renderers may allow giving shapes a "z index" or "stacking order" to specify the rendering or blending order (unlike the z coordinate used in 3D rendering, this third coordinate only indicates an order, not a distance, and cannot be meaningfully rotated together with the x and y coordinates).

2D rendering typically does not simulate light propagation (which would likely require specifying 3D positions or thickness for the shapes). Effects such as drop shadows and transparency are defined by mathematical functions with no physical basis.

2D rendering for print output may need to support very high resolutions, e.g. 600 or 1200 DPI for a typical laser printer, or 2400 DPI or higher for an imagesetter or platesetter. Grayscale and color images require halftones (or some form of dithering or stochastic screening) and color separations. A rendering engine called a *raster image processor* (RIP) converts input data such as PDF files into the high-resolution bitmap images used by the printer.


## Inputs

Before a 3D scene or 2D image can be rendered, it must be described in a way that the rendering software can understand. Historically, inputs for both 2D and 3D rendering were usually text files, which are easier than binary files for humans to edit and debug. For 3D graphics, text formats have largely been supplanted by more efficient binary formats, and by APIs which allow interactive applications to communicate directly with a rendering component without generating a file on disk (although a scene description is usually still created in memory prior to rendering).

Traditional rendering algorithms use geometric descriptions of 3D scenes or 2D images. Applications and algorithms that render visualizations of data scanned from the real world, or scientific simulations, may require different types of input data.

The PostScript format (which is often credited with the rise of desktop publishing) provides a standardized, interoperable way to describe 2D graphics and page layout. The Scalable Vector Graphics (SVG) format is also text-based, and the PDF format uses the PostScript language internally. In contrast, although many 3D graphics file formats have been standardized (including text-based formats such as VRML and X3D), different rendering applications typically use formats tailored to their needs, and this has led to a proliferation of proprietary and open formats, with binary files being more common.

### 2D vector graphics

A vector graphics image description may include:

- Coordinates and curvature information for line segments, arcs, and Bézier curves (which may be used as boundaries of filled shapes)
- Center coordinates, width, and height (or bounding rectangle coordinates) of basic shapes such as rectangles, circles and ellipses
- Color, width and pattern (such as dashed or dotted) for rendering lines
- Colors, patterns, and gradients for filling shapes
- Bitmap image data (either embedded or in an external file) along with scale and position information
- Text to be rendered (along with size, position, orientation, color, and font)
- Clipping information, if only part of a shape or bitmap image should be rendered
- Transparency and compositing information for rendering overlapping shapes
- Color space information, allowing the image to be rendered consistently on different displays and printers

### 3D geometry

A geometric scene description may include:

- Size, position, and orientation of geometric primitives such as spheres and cones (which may be combined in various ways to create more complex objects)
- Vertex coordinates and surface normal vectors for meshes of triangles or polygons (often rendered as smooth surfaces by subdividing the mesh)
- Transformations for positioning, rotating, and scaling objects within a scene (allowing parts of the scene to use different local coordinate systems).
- "Camera" information describing how the scene is being viewed (position, direction, focal length, and field of view)
- Light information (location, type, brightness, and color)
- Optical properties of surfaces, such as albedo, roughness, and refractive index,
- Optical properties of media through which light passes (transparent solids, liquids, clouds, smoke), e.g. absorption and scattering cross sections
- Bitmap image data used as texture maps for surfaces
- Small scripts or programs for generating complex 3D shapes or scenes procedurally
- Description of how object and camera locations and other information change over time, for rendering an animation

Many file formats exist for storing individual 3D objects or "models". These can be imported into a larger scene, or loaded on-demand by rendering software or games. A realistic scene may require hundreds of items like household objects, vehicles, and trees, and 3D artists often utilize large libraries of models. In game production, these models (along with other data such as textures, audio files, and animations) are referred to as "assets".

### Volumetric data

Scientific and engineering visualization often requires rendering volumetric data generated by 3D scans or simulations. Perhaps the most common source of such data is medical CT and MRI scans, which need to be rendered for diagnosis. Volumetric data can be extremely large, and requires specialized data formats to store it efficiently, particularly if the volume is *sparse* (with empty regions that do not contain data).

Before rendering, level sets for volumetric data can be extracted and converted into a mesh of triangles, e.g. by using the marching cubes algorithm. Algorithms have also been developed that work directly with volumetric data, for example to render realistic depictions of the way light is scattered and absorbed by clouds and smoke, and this type of volumetric rendering is used extensively in visual effects for movies. When rendering lower-resolution volumetric data without interpolation, the individual cubes or "voxels" may be visible, an effect sometimes used deliberately for game graphics.

### Photogrammetry and scanning

Photographs of real world objects can be incorporated into a rendered scene by using them as textures for 3D objects. Photos of a scene can also be stitched together to create panoramic images or environment maps, which allow the scene to be rendered very efficiently but only from a single viewpoint. Scanning of real objects and scenes using structured light or lidar produces point clouds consisting of the coordinates of millions of individual points in space, sometimes along with color information. These point clouds may either be rendered directly or converted into meshes before rendering. (Note: "point cloud" sometimes also refers to a minimalist rendering style that can be used for any 3D geometry, similar to wireframe rendering.)

### Neural approximations and light fields

A more recent, experimental approach is description of scenes using radiance fields which define the color, intensity, and direction of incoming light at each point in space. (This is conceptually similar to, but not identical to, the light field recorded by a hologram.) For any useful resolution, the amount of data in a radiance field is so large that it is impractical to represent it directly as volumetric data, and an approximation function must be found. Neural networks are typically used to generate and evaluate these approximations, sometimes using video frames, or a collection of photographs of a scene taken at different angles, as "training data".

Algorithms related to neural networks have recently been used to find approximations of a scene as 3D Gaussians. The resulting representation is similar to a point cloud, except that it uses fuzzy, partially-transparent blobs of varying dimensions and orientations instead of points. As with neural radiance fields, these approximations are often generated from photographs or video frames.


## Outputs

The output of rendering may be displayed immediately on the screen (many times a second, in the case of real-time rendering such as games) or saved in a raster graphics file format such as JPEG or PNG. High-end rendering applications commonly use the OpenEXR file format, which can represent finer gradations of colors and high dynamic range lighting, allowing tone mapping or other adjustments to be applied afterwards without loss of quality.

Quickly rendered animations can be saved directly as video files, but for high-quality rendering, individual frames (which may be rendered by different computers in a cluster or *render farm* and may take hours or even days to render) are output as separate files and combined later into a video clip.

The output of a renderer sometimes includes more than just RGB color values. For example, the spectrum can be sampled using multiple wavelengths of light, or additional information such as depth (distance from camera) or the material of each point in the image can be included (this data can be used during compositing or when generating texture maps for real-time rendering, or used to assist in removing noise from a path-traced image). Transparency information can be included, allowing rendered foreground objects to be composited with photographs or video. It is also sometimes useful to store the contributions of different lights, or of specular and diffuse lighting, as separate channels, so lighting can be adjusted after rendering. The OpenEXR format allows storing many channels of data in a single file. Renderers such as Blender and Pixar RenderMan support a large variety of configurable values called Arbitrary Output Variables (AOVs).
