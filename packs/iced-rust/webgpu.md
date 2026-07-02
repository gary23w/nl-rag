---
title: "WebGPU"
source: https://en.wikipedia.org/wiki/WebGPU
domain: iced-rust
license: CC-BY-SA-4.0
tags: iced toolkit, elm architecture, rust reactive gui, cross-platform rendering
fetched: 2026-07-02
---

# WebGPU

**WebGPU API** is a JavaScript, Rust, C++, and C API for cross-platform efficient graphics processing unit (GPU) access. Using a system's underlying Vulkan, Metal, or Direct3D 12 technologies, WebGPU allows for graphics processing, games, and more, as well as AI and machine learning applications. WebGPU is intended to supersede the older WebGL as the main graphics standard for the Web.

In JavaScript, WebGPU can be provided by a web browser or other JavaScript environment like Node.js and Deno. Rust and C++ can use their respective implementations of the WebGPU specification. Other languages like Python, Java, and Go can use WebGPU by extending the C language specification.

Google Chrome and Microsoft Edge first released WebGPU support in April 2023. Safari debuted WebGPU support in June 2025 with Safari 26. Firefox first released WebGPU in July 2025 with Firefox 141. The W3C standard is a candidate recommendation.

## Technology

WebGPU enables 3D graphics within an HTML canvas. It also has robust support for general-purpose GPU computations.

WebGPU uses its own shading language called WebGPU Shading Language (WGSL) that was designed to be trivially translatable to SPIR-V, until complaints caused redirection into a more traditional design, similar to other shading languages. The syntax is similar to Rust. Tint is a Google-made compiler for WGSL. Naga is a similar project developed for the needs of wgpu-rs.

## Implementations

Both Google Chrome and Firefox support WebGPU and WGSL. Firefox and Deno use the Rust wgpu library. Safari follows upstream specifications of both WebGPU and WGSL.

Chrome version 113 enabled initial WebGPU support on Windows devices with Direct3D 12, ChromeOS devices with Vulkan, and macOS with Metal. This support for Android was enabled in version 121.

## History

On June 8, 2016, Google showed "Explicit web graphics API" presentation to the WebGL working group (during the bi-annual face to face meeting). The presentation explored the basic ideas and principles of building a new API to eventually replace WebGL, aka "WebGL Next".

On January 24, 2017, Khronos hosted an IP-free meeting dedicated to discussion of "WebGL Next" ideas, collided with WebGL working group meeting in Vancouver. Google team presented the NXT prototype implementing a new API that could run in Chromium with OpenGL, or standalone with OpenGL and Metal. NXT borrowed concepts from all of Vulkan, Direct3D 12, and Metal native APIs. Apple and Mozilla representatives also showed their prototypes built on Safari and Servo correspondingly, both of which closely replicated the Metal API.

On February 7, 2017, Apple's WebKit team proposed the creation of the W3C community group to design the API. At the same time they announced a technical proof of concept and proposal under the name "WebGPU", based on concepts in Apple's Metal. The WebGPU name was later adopted by the community group as a working name for the future standard rather than just Apple's initial proposal. The initial proposal has been renamed to "WebMetal" to avoid further confusion.

The W3C "GPU for the Web" Community Group was launched on February 16, 2017. At this time, all of Apple, Google, and Mozilla had experiments in the area, but only Apple's proposal was officially submitted to the "gpuweb-proposals" repository. Shortly after, on March 21, 2017, Mozilla submitted a proposal for WebGL Next within Khronos repository, based on the Vulkan design.

On June 1, 2018, citing "resolution on most-high level issues" in the cross-browser standardization effort, Google's Chrome team announced intent to implement the future WebGPU standard.

On 13 February, 2020, Google unveiled Tint as an alternative to WHLSL textual language proposal to WebGPU API, and the language eventually became the standardized WebGPU Shading Language (WGSL), and Tint became the name of compiler within Dawn, the WebGPU implementation of Chromium.
