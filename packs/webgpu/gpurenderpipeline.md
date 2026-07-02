---
title: "GPURenderPipeline - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/GPURenderPipeline
domain: webgpu
license: CC-BY-SA-2.5
tags: webgpu, gpu compute web, gpudevice, webgpu render pipeline
fetched: 2026-07-02
---

# GPURenderPipeline

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

**Note:** This feature is available in Web Workers.

The **`GPURenderPipeline`** interface of the WebGPU API represents a pipeline that controls the vertex and fragment shader stages and can be used in a `GPURenderPassEncoder` or `GPURenderBundleEncoder`.

A `GPURenderPipeline` object instance can be created using the `GPUDevice.createRenderPipeline()` or `GPUDevice.createRenderPipelineAsync()` methods.

## Instance properties

**`label`**

A string providing a label that can be used to identify the object, for example in `GPUError` messages or console warnings.

## Instance methods

**`getBindGroupLayout()`**

Returns the pipeline's `GPUBindGroupLayout` object with the given index (i.e., included in the originating `GPUDevice.createRenderPipeline()` or `GPUDevice.createRenderPipelineAsync()` call's pipeline layout).

## Examples

**Note:** The WebGPU samples feature many more examples.

### Basic example

Our basic render demo provides an example of the construction of a valid render pipeline descriptor object, which is then used to create a `GPURenderPipeline` via a `createRenderPipeline()` call.

```js
// …

const vertexBuffers = [
  {
    attributes: [
      {
        shaderLocation: 0, // position
        offset: 0,
        format: "float32x4",
      },
      {
        shaderLocation: 1, // color
        offset: 16,
        format: "float32x4",
      },
    ],
    arrayStride: 32,
    stepMode: "vertex",
  },
];

const pipelineDescriptor = {
  vertex: {
    module: shaderModule,
    entryPoint: "vertex_main",
    buffers: vertexBuffers,
  },
  fragment: {
    module: shaderModule,
    entryPoint: "fragment_main",
    targets: [
      {
        format: navigator.gpu.getPreferredCanvasFormat(),
      },
    ],
  },
  primitive: {
    topology: "triangle-list",
  },
  layout: "auto",
};

const renderPipeline = device.createRenderPipeline(pipelineDescriptor);

// …
```

## Specifications

| Specification |
|---|
| WebGPU # gpurenderpipeline |

## Browser compatibility
