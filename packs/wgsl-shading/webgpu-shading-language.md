---
title: "WebGPU Shading Language"
source: https://en.wikipedia.org/wiki/WebGPU_Shading_Language
domain: wgsl-shading
license: CC-BY-SA-4.0
tags: wgsl shader, webgpu shading language, wgsl compute, gpu shading web
fetched: 2026-07-02
---

# WebGPU Shading Language

**WebGPU Shading Language** (**WGSL**, internet media type: `text/wgsl`) is a high-level shading language and the normative shader language for the WebGPU API on the web. WGSL's syntax is influenced by Rust and is designed with strong static validation, explicit resource binding, and portability in mind for secure execution in browsers. In web contexts, WebGPU implementations accept WGSL source and perform compilation to platform-specific intermediate forms (for example, to SPIR‑V, DXIL, or MSL via the user agent), but such backends are not exposed to web content.

## History and background

Graphics on the web historically used WebGL, with shaders written in GLSL ES. As applications demanded more modern GPU features and finer control over compute and graphics pipelines, the W3C's GPU for the Web Community Group and Working Group created WebGPU and its companion shading language, WGSL, to provide a secure, portable model suitable for the web platform. WGSL was developed to be human-readable, avoid undefined behavior common in legacy shading languages, and align closely with WebGPU's resource and validation model.

## Design goals

WGSL's design emphasizes:

- Safety and determinism suitable for web security constraints (extensive static validation and well-defined semantics).
- Portability across diverse GPU backends via an abstract resource model shared with WebGPU.
- Readability and explicitness (no preprocessor, minimal implicit conversions, explicit address spaces and bindings).
- Alignment with modern GPU features (compute, storage buffers, textures, atomics) while retaining a familiar C/Rust-like syntax.

## Language overview

### Types and values

Core scalar types include `bool`, `i32`, `u32`, and `f32`. Vectors (e.g., `vec2`, `vec3`, `vec4`) and matrices (up to 4×4) are available for floating-point element types. Optional `f16` (half precision) may be enabled via a WebGPU feature; availability is implementation-dependent. Atomic types (`atomic<i32>`, `atomic<u32>`) support limited atomic operations in qualified address spaces.

### Variables and address spaces

Variables are declared with `let` (immutable), `var` (mutable), or `const` (compile-time constant). Storage classes (address spaces) include `function`, `private`, `workgroup`, `uniform`, and `storage` with `read` or `read_write` access as applicable. WGSL defines explicit layout and alignment rules; attributes such as `@align`, `@size`, and `@stride` control data layout for buffer interoperability.

### Functions and control flow

Functions use explicit parameter and return types. Control flow includes `if`, `switch`, `for`, `while`, and `loop` constructs, with `break`/`continue`. Recursion is disallowed; entry-point call graphs must be acyclic.

### Entry points and attributes

Shaders define stage entry points with `@vertex`, `@fragment`, or `@compute`. Attributes annotate bindings and interfaces, including `@group`, `@binding` (resource binding), `@location` (user-defined I/O), `@builtin` (stage built-ins such as `position` or `global_invocation_id`), `@interpolate`, and `@workgroup_size`.

### Resources

WGSL exposes buffers (`uniform`, `storage`), textures (sampled, storage, and multisampled variants), and samplers (filtering/non-filtering/comparison). The binding model is explicit via descriptor sets called groups and bindings, matching WebGPU's pipeline layout model.

## Compilation and validation

Browsers compile WGSL to platform-appropriate representations and native driver formats; the specific compilation pipeline is not observable by web content. WGSL source undergoes strict parsing and static validation, and WebGPU enforces robust resource access rules to avoid out-of-bounds memory hazards, contributing to predictable behavior across implementations.

## Shader stages

WGSL supports three pipeline stages: vertex, fragment, and compute.

### Vertex shaders

Vertex shaders transform per-vertex inputs and produce values for rasterization, including a clip-space position written to the `position` builtin.

#### Example

```mw
/* Transforms positions by an MVP matrix and passes through color. */

struct VertexInput {
  @location(0) position : vec3f,  // vec3f is an alias for vec3<f32>
  @location(1) color : vec3f,
};

struct VertexOutput {
  @builtin(position) clip_position : vec4f,
  @location(0) color : vec3f,
};

@group(0) @binding(0)
var<uniform> mvp : mat4x4f;

@vertex
fn main(v_in : VertexInput) -> VertexOutput {
  var v_out : VertexOutput;
  v_out.clip_position = mvp * vec4f(v_in.position, 1.0);
  v_out.color = v_in.color;
  return v_out;
}
```

### Fragment shaders

Fragment shaders run per-fragment and compute color (and optionally depth) outputs written to color attachments.

#### Example

```mw
/* Writes an interpolated color with opaque alpha. */

@fragment
fn main(@location(0) color : vec3f) -> @location(0) vec4f {
  return vec4f(color, 1.0);
}
```

If half-precision (`vec4h`, shorthand for `vec4<f16>`) is desired, the code must be prefaced with a `enable f16;` statement.

### Compute shaders

Compute shaders run in workgroups and are used for general-purpose GPU computations.

#### Example

```mw
/* Doubles elements from an input buffer into an output buffer. */

struct Params {
  element_count : u32,
};

@group(0) @binding(0)
var<storage, read> in_data : array<f32>;
@group(0) @binding(1)
var<storage, read_write> out_data : array<f32>;
@group(0) @binding(2)
var<uniform> params : Params;

@compute @workgroup_size(64)
fn main(@builtin(global_invocation_id) gid : vec3<u32>) {
  let idx : u32 = gid.x;
  if (idx >= params.element_count) { return; }
  out_data[idx] = in_data[idx] * 2.0;
}
```

## Differences from GLSL and HLSL

Compared with legacy shading languages, WGSL:

- Omits a preprocessor and requires explicit types and conversions.
- Uses explicit address spaces and binding annotations aligned with WebGPU's model.
- Enforces strict validation to avoid undefined behavior common in other shading languages.
- Defines a portable, web-focused feature set; 16-bit types and other features are opt-in and may depend on device capabilities.
