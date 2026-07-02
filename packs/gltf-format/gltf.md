---
title: "glTF"
source: https://en.wikipedia.org/wiki/GlTF
domain: gltf-format
license: CC-BY-SA-4.0
tags: gltf format, khronos gltf, 3d asset transmission, pbr gltf
fetched: 2026-07-02
---

# glTF

**glTF** (Graphics Library Transmission Format or GL Transmission Format and formerly known as WebGL Transmissions Format or WebGL TF) is a standard file format for three-dimensional scenes and models. A glTF file uses one of two possible file extensions: **.gltf** (JSON/ASCII) or **.glb** (binary). Both .gltf and .glb files may reference external binary and texture resources. Alternatively, both formats may be self-contained by directly embedding binary data buffers (as base64-encoded strings in .gltf files or as raw byte arrays in .glb files). An open standard developed and maintained by the Khronos Group, it supports 3D model geometry, appearance, scene graph hierarchy, and animation. It is intended to be a streamlined, interoperable format for the delivery of 3D assets, while minimizing file size and runtime processing by apps. As such, its creators have described it as the "JPEG of 3D".

## Overview

The glTF format stores data primarily in JSON. The JSON may also contain blobs of binary data known as buffers, and refer to external files, for storing mesh data, images, etc. The binary .glb format also contains JSON text, but serialized with binary chunk headers to allow blobs to be directly appended to the file.

The fundamental building blocks of a glTF *scene* are *nodes*. Nodes are organized into a hierarchy, such that a node may have other nodes defined as children. Nodes may have *transforms* relative to their parent. Nodes may refer to *resources*, such as *meshes*, *skins*, and *cameras*. Meshes may refer to *materials*, which refer to *textures*, which refer to *images*. Scenes are defined using an array of root nodes.

Most of the top-level glTF properties use a flat hierarchy for storage. Nodes are saved in an array and are referred to by index, including by other nodes. A glTF scene refers to its root nodes by index. Furthermore, nodes refer to meshes by index, which refer to materials by index, which refer to textures by index, which refer to images by index.

All glTF data structures support being extended using a JSON property, allowing arbitrary JSON data to be added.

## Releases

### glTF 1.0

Members of the COLLADA working group conceived the file format in 2012. At SIGGRAPH 2012, Khronos presented a demo of glTF, which was then called WebGL Transmissions Format (WebGL TF). On October 19, 2015, Khronos released the glTF 1.0 specification.

#### Adoption of glTF 1.0

At SIGGRAPH 2016, Oculus announced their adoption of glTF citing the similarities to their ovrscene format. In October 2016, Microsoft joined the 3D Formats working group at Khronos to collaborate on glTF.

### glTF 2.0

The second version, glTF 2.0, was released in June 2017, and is a complete overhaul of the file format from version 1.0, with most tools adopting the 2.0 version. Based on a proposal by Fraunhofer originally presented at SIGGRAPH 2016, physically based rendering (PBR) was added, replacing WebGL shaders used in glTF 1.0. glTF 2.0 added the GLB binary format into the base specification. Other upgrades include sparse accessors and morph targets for techniques such as facial animation, and schema tweaks and breaking changes for corner cases or performance such as replacing top-level glTF object properties with arrays for faster index-based access. There is ongoing work towards import and export in Unity and an integrated multi-engine viewer and validator.

#### Adoption of glTF 2.0

On March 3, 2017, Microsoft announced that they would be using glTF 2.0 as the 3D asset format across their product line, including Paint 3D, 3D Viewer, Remix 3D, Babylon.js, and Microsoft Office. Sketchfab also announced support for glTF 2.0. The glTF and GLB formats are used on and supported by companies including DGG, UX3D, Sketchfab, Facebook, Microsoft, Meta, Google, Adobe, Box, TurboSquid, Unreal Engine, Unity, and Qt Quick 3D. The format has been noted as an important standard for augmented reality, integrating with modeling software such as Autodesk Maya, Autodesk 3ds Max, and Poly.

In February 2020, the Smithsonian Institution launched their Open Access Initiative, releasing approximately 2.8 million 2D images and 3D models into the public domain, using glTF for the 3D models.

In July 2022, glTF 2.0 was released as the ISO/IEC 12113:2022 International Standard. Khronos stated they would make regular submissions to bring updates and new widely adopted glTF functionality into refreshed versions of ISO/IEC 12113 to ensure that there is no long-term divergence between the ISO/IEC and Khronos specifications.

The open-source game engine Godot supports importing glTF 2.0 files since version 3.0 and export since version 4.0.

### Extensions

The glTF format can be extended with arbitrary JSON to add new data and functionality. Extensions can be placed on any part of a glTF, including nodes, animations, materials, textures, and on the entire document. Khronos keeps a non-comprehensive registry of glTF extensions on GitHub, including all official Khronos extensions and a few third-party extensions.

- PBR extensions model the physical appearance of real-world objects, allowing developers to create realistic 3D assets that have the correct appearance. As new PBR extensions are released, they continue to expand PBR capabilities within the glTF framework, allowing a wider range of scenes and objects to be realistically rendered as 3D assets.

- The KTX 2.0 extension for universal texture compression enables 3D models in the glTF format to be highly compressed and to use natively supported texture formats, reducing file size and boosting rendering speed.

- Draco is a glTF extension for mesh compression, to compress and decompress 3D meshes, to help reduce the size of 3D files. It compresses vertex attributes, normals, colors, and texture coordinates.

- Various glTF extensions for game engine interoperability have been developed by OMI group. This includes extensions for physics shapes, physics bodies, physics joints, audio playback, seats, spawn points, and more.

- The VRM consortium has developed glTF extensions for advanced humanoid 3D avatars including dynamic spring bones and toon materials.

## Derivative formats

3D Tiles, an OGC Community Standard, builds on glTF to add a spatial data structure, metadata, and declarative styling for streaming massive heterogeneous 3D geospatial datasets.

VRM, a model format for VR, is built on the .glb format. It is a 3D humanoid avatar specification and file format.

## Software ecosystem

Khronos maintains the glTF Sample Viewer for viewing glTF assets. Khronos also maintains the glTF Validator for validating if 3D models conform to the glTF specification.

Khronos maintains a glTF Compressor tool to interactively optimize and fine-tune compression settings for glTF assets using KTX 2.0 textures.

glTF loaders are in open-source WebGL engines including PlayCanvas, Three.js, Babylon.js, Cesium, PEX, xeogl, and A-Frame. The Godot game engine supports and recommends the glTF format, with both import and export support.

Open-source glTF converters are available from COLLADA, FBX, and OBJ. Assimp can import and export glTF.

glTF files can also be directly exported from a variety of 3D editors, such as Blender, Unity (using the glTFast importer/exporter), Freecad, Vectary, Autodesk 3ds Max (natively or using Verge3D exporter), Autodesk Maya (using babylon.js exporter), Autodesk Inventor, Modo, Houdini, Paint 3D, Godot, and Substance Painter.

Open-source glTF utility libraries are available for programming languages including JavaScript, Node.js, C++, C#, Python, Haskell, Java, Go, Rust, Haxe, Ada, and TypeScript. Khronos keeps a list of these libraries and other related applications on their ecosystem site.

The Khronos 3D Commerce Working Group released Asset Creation Guidelines in 2020 outlining best practices for use of the glTF file format in 3D Commerce. In 2025, the Working Group launched Asset Creation Guidelines 2.0, a continuously updated resource with additional guidance for geometry, mesh optimization, UV maps, textures, materials/PBR performance, and web optimization.

The Khronos PBR Neutral Tone Mappers specification is a tone mapper designed to faithfully reproduce an object's base color, hue, and saturation when using PBR rendering under grayscale lighting, supporting brand- and product-accurate color representation.

Khronos maintains the glTF Asset Auditor to allow retailers and advertising technology platforms to validate 3D assets against either a default Audit Profile modelled on the 2020 3D Commerce Asset Creation Guidelines or a custom profile defined by the target application.
