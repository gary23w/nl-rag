---
title: "Worklet - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Worklet
domain: css-layout-api
license: CC-BY-SA-4.0
tags: css layout api, layout worklet definition, custom layout algorithm, fragment layout children
fetched: 2026-07-02
---

# Worklet

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2021.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The **`Worklet`** interface is a lightweight version of Web Workers and gives developers access to low-level parts of the rendering pipeline.

With Worklets, you can run JavaScript and WebAssembly code to do graphics rendering or audio processing where high performance is required.

Worklets allow static import of ECMAScript modules, if supported, using `import`. Dynamic import is disallowed by the specification — calling `import()` will throw.

## Worklet types

Worklets are restricted to specific use cases; they cannot be used for arbitrary computations like Web Workers. The `Worklet` interface abstracts properties and methods common to all kind of worklets, and cannot be created directly. Instead, you can use one of the following classes:

| Name | Description | Location | Specification |
|---|---|---|---|
| `AudioWorklet` | For audio processing with custom AudioNodes. | Web Audio render thread | Web Audio API |
| `AnimationWorklet` | For creating scroll-linked and other high performance procedural animations. | Compositor thread | CSS Animation Worklet API |
| `LayoutWorklet` | For defining the positioning and dimensions of custom elements. |   | CSS Layout API |
| `SharedStorageWorklet` | For running private operations on cross-site data, without risk of data leakage. | Main thread | Shared Storage API |

**Note:** Paint worklets, defined by the CSS Painting API, don't subclass `Worklet`. They are accessed through a regular `Worklet` object obtained using `CSS.paintWorklet`.

For 3D rendering with WebGL, you don't use worklets. Instead, you write vertex shaders and fragment shaders using GLSL code, and those shaders will then run on the graphics card.

## Instance properties

*The Worklet interface does not define any properties.*

## Instance methods

**`Worklet.addModule()`**

Adds the script module at the given URL to the current worklet.

## Specifications

| Specification |
|---|
| HTML # worklets-worklet |

## Browser compatibility
