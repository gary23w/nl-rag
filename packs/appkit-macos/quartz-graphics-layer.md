---
title: "Quartz (graphics layer)"
source: https://en.wikipedia.org/wiki/Quartz_(graphics_layer)
domain: appkit-macos
license: CC-BY-SA-4.0
tags: appkit framework, macos gui, aqua interface, quartz compositor
fetched: 2026-07-02
---

# Quartz (graphics layer)

In Apple's macOS operating system, **Quartz** is the Quartz 2D and Quartz Compositor part of the Core Graphics framework. Quartz includes both a 2D renderer in Core Graphics and the composition engine that sends instructions to the graphics card. Because of this vertical nature, *Quartz* is often synonymous with *Core Graphics*.

In a general sense, *Quartz* or *Quartz technologies* can refer to almost every part of the macOS graphics model from the rendering layer down to the compositor including Core Image and Core Video. Other Apple graphics technologies that use the "Quartz" prefix include these:

- Quartz Extreme
- QuartzGL (originally Quartz 2D Extreme)
- QuartzCore
- Quartz Display Services
- Quartz Event Services

## Quartz 2D and Quartz Compositor

Quartz 2D is the primary two-dimensional (2D) text and graphics rendering library: It directly supports Aqua by displaying two-dimensional graphics to create the user interface, including on-the-fly rendering and anti-aliasing. Quartz can render text with sub-pixel precision; graphics are limited to more traditional anti-aliasing, which is the default mode of operation but can be turned off. In Mac OS X 10.4 Tiger, Apple introduced Quartz 2D Extreme, enabling Quartz 2D to offload rendering to compatible GPUs. However, GPU rendering was not enabled by default due to potential video redraw issues or kernel panics. In Mac OS X v10.5 Quartz 2D Extreme was renamed to QuartzGL.

The Quartz Compositor is the compositing engine used by macOS. In Mac OS X Jaguar and later, the Quartz Compositor can use the graphics accelerator (GPU) to vastly improve composition performance. This technology is known as Quartz Extreme and is enabled automatically on systems with supported graphics cards.
