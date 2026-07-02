---
title: "3D computer graphics"
source: https://en.wikipedia.org/wiki/3D_computer_graphics
domain: babylonjs
license: CC-BY-SA-4.0
tags: babylon.js, babylonjs engine, webgl 3d engine, babylon scene
fetched: 2026-07-02
---

# 3D computer graphics

**3D computer graphics**, sometimes called **3D computer-generated imagery** (**3D-CGI**), refers to computer graphics that use a three-dimensional (3D) representation of geometric data (often Cartesian) stored in the computer for the purposes of performing calculations and rendering digital images, usually 2D images but sometimes 3D images. The resulting images may be stored for viewing later (possibly as an animation) or displayed in real time.

3D computer graphics, contrary to what the name suggests, are most often displayed on two-dimensional displays. Unlike 3D film and similar techniques, the result is two-dimensional, without visual depth. More often, 3D graphics are being displayed on 3D displays, like in virtual reality systems.

3D graphics stand in contrast to 2D computer graphics which typically use completely different methods and formats for creation and rendering.

3D computer graphics rely on many of the same algorithms as 2D computer vector graphics in the wire-frame model and 2D computer raster graphics in the final rendered display. In computer graphics software, 2D applications may use 3D techniques to achieve effects such as lighting, and similarly, 3D may use some 2D rendering techniques.

The objects in 3D computer graphics are often referred to as 3D models. Unlike the rendered image, a model's data is contained within a graphical data file. A 3D model is a mathematical representation of *any* three-dimensional object; a model is not technically a *graphic* until it is displayed. A model can be displayed visually as a two-dimensional image through a process called 3D rendering, or it can be used in non-graphical computer simulations and calculations. With 3D printing, models are rendered into an actual 3D physical representation of themselves, with some limitations as to how accurately the physical model can match the virtual model.

## History

William Fetter was credited with coining the term *computer graphics* in 1961 to describe his work at Boeing. An early example of interactive 3-D computer graphics was explored in 1963 by the Sketchpad program at Massachusetts Institute of Technology's Lincoln Laboratory. One of the first displays of computer animation was *Futureworld* (1976), which included an animation of a human face and a hand that had originally appeared in the 1972 experimental short *A Computer Animated Hand*, created by University of Utah students Edwin Catmull and Fred Parke.

3-D computer graphics software began appearing for home computers in the late 1970s. The earliest known example is *3D Art Graphics*, a set of 3-D computer graphics effects, written by Kazumasa Mitazawa and released in June 1978 for the Apple II.

Virtual Reality 3D is a version of 3D computer graphics. Although the first VR headsets appeared in the late 1950s, VR did not become widely popular until the 2000s. In 2012 the Oculus was released and since then, the 3D VR headset world has expanded.

## Overview

3D computer graphics production workflow falls into three basic phases:

1. 3D modeling – the process of forming a computer model of an object's shape
2. Layout and CGI animation – the placement and movement of objects (models, lights, etc.) within a scene
3. 3D rendering – the computer calculations that, based on light placement, surface types, and other qualities, generate (rasterize the scene into) an image

### Modeling

The modeling describes the process of forming the shape of an object. The two most common sources of 3D models are those that an artist or engineer originates on a computer with a 3D modeling tool, or models scanned into a computer from real-world objects (polygonal modeling, patch modeling, and NURBS modeling are some popular tools used in 3D modeling). Models can also be produced procedurally or via physical simulation.

Basically, a 3D model is formed from points called vertices that define the shape and form polygons. A polygon is an area formed from at least three vertices (a triangle). A polygon of n points is an n-gon. The overall integrity of the model and its suitability to use in animation depend on the structure of the polygons.

### Layout and animation

Before rendering into an image, objects must be laid out in a 3D scene. This defines spatial relationships between objects, including location and size. Animation refers to the temporal description of an object (i.e., how it moves and deforms over time). Popular methods include keyframing, inverse kinematics, and motion-capture). These techniques are often used in combination. As with animation, physical simulation also specifies motion.

Stop Motion has multiple categories within such as Claymation, Cutout, Silhouette, Lego, Puppets, and Pixelation.

Claymation is the use of models made of clay used for an animation. Some examples are Clay Fighter and Clay Jam.

Lego animation is one of the more common types of stop motion. Lego stop motion is the use of the figures themselves moving around. Some examples of this are Lego Island and Lego Harry Potter.

### Rendering

Rendering converts a model into an image either by simulating light transport to get photo-realistic images, or by applying an art style as in non-photorealistic rendering. The two basic operations in realistic rendering are transport (how much light gets from one place to another) and scattering (how surfaces interact with light). This step is usually performed using 3-D computer graphics software or a 3-D graphics API.

Altering the scene into a suitable form for rendering also involves 3D projection, which displays a three-dimensional image in two dimensions. Although 3-D modeling and CAD software may perform 3-D rendering as well (e.g., Autodesk 3ds Max or Blender), exclusive 3-D rendering software also exists (e.g., OTOY's Octane Rendering Engine, Maxon's Redshift)

- Examples of 3-D rendering
- (A 3-D rendering with ray tracing and ambient occlusion using Blender and YafaRay) A 3-D rendering with ray tracing and ambient occlusion using Blender and YafaRay
- (A 3-D model of a Dunkerque-class battleship rendered with flat shading) A 3-D model of a *Dunkerque*-class battleship rendered with flat shading
- (During the 3-D rendering step, the number of reflections "light rays" can take, as well as various other attributes, can be tailored to achieve a desired visual effect. Rendered with Cobalt.) During the 3-D rendering step, the number of reflections "light rays" can take, as well as various other attributes, can be tailored to achieve a desired visual effect. Rendered with Cobalt.
- (A 3-D rendering of a penthouse) A 3-D rendering of a penthouse

### Materials and textures

Materials and textures are properties that the render engine uses to render the model. One can give the model materials to tell the render engine how to treat light when it hits the surface. Textures are used to give the material color using a color or albedo map, or give the surface features using a bump map or normal map. It can also be used to deform the model itself using a displacement map.

## Software

3-D computer graphics software produces computer-generated imagery (CGI) through 3D modeling and 3D rendering or produces 3-D models for analytical, scientific, entertainment, and industrial purposes.

### File formats

There are many varieties of files supporting 3-D graphics, for example, Blender (.blend), Wavefront (.obj), .fbx and .x DirectX files. Each file type generally tends to have its own unique data structure.

Each file format can be accessed through its respective applications, such as DirectX files, and Quake. Alternatively, files can be accessed through third-party standalone programs, or via manual decompilation.

### Modeling

3-D modeling software is a class of 3-D computer graphics software used to produce 3-D models. Individual programs of this class are called modeling applications or modelers.

3-D modeling starts by describing 3 display models: drawing points, drawing lines and drawing triangles and other polygonal patches.

3-D modelers allow users to create and alter models via their 3-D mesh. Users can add, subtract, stretch and otherwise change the mesh to their desire. Models can be viewed from a variety of angles, usually simultaneously. Models can be rotated and the view can be zoomed in and out.

3-D modelers can export their models to files, which can then be imported into other applications as long as the metadata are compatible. Many modelers allow importers and exporters to be plugged-in, so they can read and write data in the native formats of other applications.

Most 3-D modelers contain a number of related features, such as ray tracers and other rendering alternatives and texture mapping facilities. Some also contain features that support or allow animation of models. Some may be able to generate full-motion video of a series of rendered scenes (i.e. animation).

### Computer-aided design (CAD)

Computer-aided design software may employ the same fundamental 3-D modeling techniques that 3-D modeling software uses but their goal differs. They are used in computer-aided engineering, computer-aided manufacturing, Finite element analysis, product lifecycle management, 3D printing and computer-aided architectural design.

### Complementary tools

After producing a video, studios then edit or composite the video using programs such as Adobe Premiere Pro or Final Cut Pro at the mid-level, or Autodesk Combustion, Digital Fusion, Shake at the high-end. Match moving software is commonly used to match live video with computer-generated video, keeping the two in sync as the camera moves.

Use of real-time computer graphics engines to create a cinematic production is called machinima.

## Other types of 3D appearance

### Photorealistic 2D graphics

Not all computer graphics that appear 3D are based on a wireframe model. 2D computer graphics with 3D photorealistic effects are often achieved without wire-frame modeling and are sometimes indistinguishable in the final form. Some graphic art software includes filters that can be applied to 2D vector graphics or 2D raster graphics on transparent layers. Visual artists may also copy or visualize 3D effects and manually render photo-realistic effects without the use of filters.

### 2.5D

Some video games use 2.5D graphics, involving restricted projections of three-dimensional environments, such as isometric graphics or virtual cameras with fixed angles, either as a way to improve performance of the game engine or for stylistic and gameplay concerns. By contrast, games using 3D computer graphics without such restrictions are said to use true 3D.

### Other forms of animation

Cutout is the use of flat materials such as paper. Everything is cut out of paper including the environment, characters, and even some props. An example of this is Paper Mario. Silhouette is similar to cutouts except they are one solid color, black. Limbo is an example of this. Puppets are dolls and different puppets used in the game. An example of this would be Yoshi's Wooly World. Pixelation is when the entire game appears pixelated, this includes the characters and the environment around them. One example of this is seen in Shovel Knight.
