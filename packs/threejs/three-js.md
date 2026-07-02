---
title: "Three.js"
source: https://en.wikipedia.org/wiki/Three.js
domain: threejs
license: CC-BY-SA-4.0
tags: three.js, threejs, webgl 3d library, 3d scene rendering
fetched: 2026-07-02
---

# Three.js

**Three.js** is a cross-browser JavaScript library and application programming interface (API) used to create and display animated 3D computer graphics in a web browser using WebGL. The source code is hosted in a repository on GitHub.

## Overview

Three.js allows the creation of graphical processing unit (GPU)-accelerated 3D animations using the JavaScript language as part of a website without relying on proprietary browser plugins. This is possible due to the advent of WebGL, a low-level graphics API created specifically for the web.

High-level libraries such as Three.js, Babylon.js, Verge3D and many more make it possible to author complex 3D computer animations for display in the browser without the effort required for a traditional standalone application or a plugin.

## History

Three.js was first released by Ricardo Cabello on GitHub in April 2010. The origins of the library can be traced back to his involvement with the demoscene in the early 2000s. The code was originally developed in the ActionScript language used by Adobe Flash, later being ported to JavaScript in 2009. In Cabello's mind, there were two strong points that justified the shift away from ActionScript: Firstly, JavaScript provided greater platform independence. Secondly, applications written in JavaScript would not need to be compiled by the developer beforehand, unlike Flash applications.

Additional contributions by Cabello include API design, CanvasRenderer, SVGRenderer, and being responsible for merging the commits by the various contributors into the project.

With the advent of WebGL, Paul Brunt was able to implement the new rendering technology quite easily as Three.js was designed with the rendering code as a module rather than in the core itself. Branislav Uličný, an early contributor, started with Three.js in 2010 after having posted a number of WebGL demos on his own site. He wanted WebGL renderer capabilities in Three.js to exceed those of CanvasRenderer or SVGRenderer. His major contributions generally involve materials, shaders, and post-processing.

Soon after the introduction of WebGL 1.0 on Firefox 4 in March 2011, Joshua Koo came on board. He built his first Three.js demo for 3D text in September 2011. His contributions frequently relate to geometry generation.

Starting from version 118, Three.js uses WebGL 2.0 by default.

Three.js has over 2000 contributors on GitHub.

## Features

Three.js includes the following features:

- Effects: Anaglyph, cross-eyed, and parallax barrier.
- Scenes: add and remove objects at run-time; fog
- Cameras: perspective and orthographic; controllers: trackball, FPS, path and more
- Animation: armatures, forward kinematics, inverse kinematics, morph, and keyframe
- Lights: ambient, direction, point, and spot lights; shadows: cast and receive
- Materials: Lambert, Phong, smooth shading, textures, and more
- Shaders: access to full OpenGL Shading Language (GLSL) capabilities: lens flare, depth pass, and extensive post-processing library
- Objects: meshes, particles, sprites, lines, ribbons, bones, and more - all with Level of detail
- Geometry: plane, cube, sphere, torus, 3D text, and more; modifiers: lathe, extrude, and tube
- Import/export: native serialization/deserialization via JSON, glTF, OBJ, USDZ, and more.
- Utilities: full set of time and 3D math functions including Viewing frustum, matrix, quaternion, UVs, and more
- Support: API documentation is under construction. A public forum and wiki is in full operation.
- Examples: Over 150 files of coding examples plus fonts, models, textures, sounds, and other support files
- Debugging: Stats.js, WebGL Inspector, Three.js Inspector
- Virtual and Augmented Reality via WebXR
- Physically based rendering (PBR): support for physically accurate materials like MeshStandardMaterial and MeshPhysicalMaterial

- Instancing: use of InstancedMesh for efficient rendering of thousands of repeated objects

- Post-processing: built-in post-processing pipeline with effects such as bloom, depth of field, outline, motion blur, SSAO, and FXAA

- Built-in editor: graphical scene editor available online for building and exporting 3D scenes

- Interactive controls: built-in controls such as OrbitControls, DragControls, TransformControls, and PointerLockControls for user interaction and navigation

- Alternative renderers: in addition to WebGLRenderer, Three.js also provides SVGRenderer and CSS3DRenderer, as well as experimental support for WebGPURenderer.

Three.js runs in all browsers with support for WebGL 2.0.

Three.js is made available under the MIT License.
