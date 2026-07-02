---
title: "WebGL"
source: https://en.wikipedia.org/wiki/WebGL
domain: phaser-framework
license: CC-BY-SA-4.0
tags: phaser framework, phaser game framework, html5 game framework, phaser scene
fetched: 2026-07-02
---

# WebGL

**WebGL** (short for **Web Graphics Library**) is a JavaScript API for rendering interactive 2D and 3D graphics within any compatible web browser without the use of plug-ins. WebGL is fully integrated with other web standards, allowing GPU-accelerated usage of physics, image processing, and effects in the HTML canvas. WebGL elements can be mixed with other HTML elements and composited with other parts of the page or page background.

WebGL programs consist of control code written in JavaScript, and shader code written in OpenGL ES Shading Language (GLSL ES, sometimes referred to as ESSL), a language similar to C or C++. WebGL code is executed on a computer's GPU.

WebGL is designed and maintained by the non-profit Khronos Group. On February 9, 2022, Khronos Group announced WebGL 2.0 support from all major browsers.

From 2024, a new graphics API, WebGPU, is being developed to supersede WebGL. WebGPU provides extended capabilities, a more modern interface, and direct GPU access, which is useful for demanding graphics as well as AI applications.

## Design

WebGL 1.0 is based on OpenGL ES 2.0 and provides an API for 3D graphics. It uses the HTML5 canvas element and is accessed using Document Object Model (DOM) interfaces.

WebGL 2.0 is based on OpenGL ES 3.0. It guarantees the availability of many optional extensions of WebGL 1.0, and exposes new APIs. Automatic memory management is provided implicitly by JavaScript.

Like OpenGL ES 2.0, WebGL lacks the fixed-function APIs introduced in OpenGL 1.0 and deprecated in OpenGL 3.0. This functionality, if required, has to be implemented by the developer using shader code and JavaScript.

Shaders in WebGL are written in GLSL and passed to the WebGL API as text strings. The WebGL implementation compiles these strings to GPU code. This code is executed for each vertex sent through the API and for each pixel rasterized to the screen.

## History

WebGL evolved out of the Canvas 3D experiments started by Vladimir Vukićević at Mozilla. Vukićević first demonstrated a Canvas 3D prototype in 2006. By the end of 2007, both Mozilla and Opera had made their own separate implementations.

In early 2009, the non-profit technology consortium Khronos Group started the WebGL Working Group, with initial participation from Apple, Google, Mozilla, Opera, and others. Version 1.0 of the WebGL specification was released March 2011.

An early application of WebGL was Zygote Body. In November 2012 Autodesk announced that they ported most of their applications to the cloud running on local WebGL clients. These applications included Autodesk Fusion and AutoCAD.

Development of the WebGL 2 specification started in 2013 and finished in January 2017. The specification is based on OpenGL ES 3.0. First implementations are in Firefox 51, Chrome 56 and Opera 43.

## Implementations

### Almost Native Graphics Layer Engine

Almost Native Graphics Layer Engine (ANGLE) is an open source graphic engine which implements WebGL 1.0 (2.0 which closely conforms to ES 3.0) and OpenGL ES 2.0 and 3.0 standards. It is a default backend for both Google Chrome and Mozilla Firefox on Windows platforms and works by translating WebGL and OpenGL calls to available platform-specific APIs. ANGLE currently provides access to OpenGL ES 2.0 and 3.0 to desktop OpenGL, OpenGL ES, Direct3D 9, and Direct3D 11 APIs. ″[Google] *Chrome uses ANGLE for all graphics rendering on Windows, including the accelerated Canvas2D implementation and the Native Client sandbox environment.″*

## Software

WebGL is widely supported by modern browsers. However, its availability depends on other factors, too, like whether the GPU supports it. The official WebGL website offers a simple test page. More detailed information (like what renderer the browser uses, and what extensions are available) can be found at third-party websites.

### Desktop browsers

Source:

- Google Chrome – WebGL 1.0 has been enabled on all platforms that have a capable graphics card with updated drivers since version 9, released in February 2011. By default on Windows, Chrome uses the ANGLE (Almost Native Graphics Layer Engine) renderer to translate OpenGL ES to Direct X 9.0c or 11.0, which have better driver support. However, on Linux and Mac OS X, the default renderer is OpenGL. It is also possible to force OpenGL as the renderer on Windows. Since September 2013, Chrome also has a newer Direct3D 11 renderer, which requires a newer graphics card. Chrome 56+ supports WebGL 2.0.
- Firefox – WebGL 1.0 has been enabled on all platforms that have a capable graphics card with updated drivers since version 4.0. Since 2013 Firefox also uses DirectX on the Windows platform via ANGLE. Firefox 51+ supports WebGL 2.0.
- Safari – Safari 6.0 and newer versions installed on OS X Mountain Lion, Mac OS X Lion and Safari 5.1 on Mac OS X Snow Leopard implemented support for WebGL 1.0, which was disabled by default before Safari 8.0. Safari version 12 (available in MacOS Mojave) has available support for WebGL 2.0 as an "Experimental" feature. Safari 15 enables WebGL 2.0 for all users.
- Opera – WebGL 1.0 has been implemented in Opera 11 and 12, but was disabled by default in 2014. Opera 43+ supports WebGL 2.0.
- Internet Explorer – WebGL 1.0 is partially supported in Internet Explorer 11. Internet Explorer initially failed most of the official WebGL conformance tests, but Microsoft later released several updates. The latest 0.94 WebGL engine currently passes ≈97% of Khronos tests. WebGL support can also be manually added to earlier versions of Internet Explorer using third-party plugins such as IEWebGL.
- Microsoft Edge – For Microsoft Edge Legacy, the initial stable release supports WebGL version 0.95 (context name: "experimental-webgl") with an open source GLSL to HLSL transpiler. Version 10240+ supports WebGL 1.0 as prefixed. Latest Chromium-based Edge supports WebGL 2.0.

### Mobile browsers

- Google Chrome – WebGL 1.0 is supported on Android as of Chrome 25. WebGL 2.0 is supported on Android as of Chrome 58. Chrome is used for the Android system webview as of Android 5.
- Firefox for mobile – WebGL 1.0 is available for Android devices since Firefox 4.
- Safari on iOS – WebGL 1.0 is available for mobile Safari in iOS 8. WebGL 2.0 is available for mobile Safari in iOS 15.
- Microsoft Edge – Prefixed WebGL 1.0 was available on Windows 10 Mobile.. Latest Chromium-based Edge supports WebGL 2.0.
- Opera Mobile – Opera Mobile 12 supports WebGL 1.0 (on Android only).
- Sailfish OS – WebGL 1.0 is supported in the default Sailfish browser.
- Tizen – WebGL 1.0 is supported

## Tools and ecosystem

### Utilities

The low-level nature of the WebGL API, which provides little on its own to quickly create desirable 3D graphics, motivated the creation of higher-level libraries that abstract common operations (e.g. loading scene graphs and 3D objects in certain formats; applying linear transformations to shaders or view frustums). Some such libraries were ported to JavaScript from other languages. Examples of libraries that provide high-level features include A-Frame (VR), BabylonJS, PlayCanvas, three.js, OSG.JS, Google’s model-viewer and CopperLicht. Web3D also made a project called X3DOM to make X3D and VRML content run on WebGL.

### Games

There has been an emergence of 2D and 3D game engines for WebGL, such as Unreal Engine 4 and Unity. The Stage3D/Flash-based Away3D high-level library also has a port to WebGL via TypeScript. A more light-weight utility library that provides just the vector and matrix math utilities for shaders is sylvester.js. It is sometimes used in conjunction with a WebGL specific extension called glUtils.js.

There are also some 2D libraries built atop WebGL, like Cocos2d-x or Pixi.js, which were implemented this way for performance reasons in a move that parallels what happened with the Starling Framework over Stage3D in the Flash world. The WebGL-based 2D libraries fall back to HTML5 canvas when WebGL is not available. Removing the rendering bottleneck by giving almost direct access to the GPU has exposed performance limitations in the JavaScript implementations. Some were addressed by asm.js and WebAssembly (similarly, the introduction of Stage3D exposed performance problems within ActionScript, which were addressed by projects like CrossBridge).

### Content creation

As with any other graphics API, creating content for WebGL scenes requires using a 3D content creation tool and exporting the scene to a format that is readable by the viewer or helper library. Desktop 3D authoring software such as Blender, Autodesk Maya or SimLab Composer can be used for this purpose. In particular, Blend4Web allows a WebGL scene to be authored entirely in Blender and exported to a browser with a single click, even as a standalone web page. There are also some WebGL-specific software such as CopperCube and the online WebGL-based editor Clara.io. Online platforms such as Sketchfab and Clara.io allow users to directly upload their 3D models and display them using a hosted WebGL viewer.

### Environment-based tools

Starting from Firefox Version 27, Mozilla has given Firefox built-in WebGL tools that allow the editing of vertices and fragment shaders. A number of other debugging and profiling tools have also emerged.
