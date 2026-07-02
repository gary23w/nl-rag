---
title: "DirectCompute"
source: https://en.wikipedia.org/wiki/DirectCompute
domain: directx-graphics
license: CC-BY-SA-4.0
tags: directx api, direct3d, hlsl shader, directx raytracing
fetched: 2026-07-02
---

# DirectCompute

**Microsoft DirectCompute** is an application programming interface (API) that supports running compute kernels on general-purpose computing on graphics processing units on Microsoft's Windows Vista, Windows 7 and later versions. DirectCompute is part of the Microsoft DirectX collection of APIs, and was initially released with the DirectX 11 API but runs on graphics processing units that use either DirectX 10 or DirectX 11. The DirectCompute architecture shares a range of computational interfaces with its competitors: OpenCL from Khronos Group, compute shaders in OpenGL, and CUDA from NVIDIA.

The DirectCompute API brings enhanced multi-threading capabilities to leverage the emerging advanced compute resources. The API is designed for non-graphical applications to access and use GPU resources.

## Compute Pipeline

The Compute pipeline is a type of graphics pipeline used for dispatching and executing compute shaders. Compute pipelines are run through compute command lists, which are restricted to recording only copy and compute commands. Compute shaders are used for general-purpose algorithms and computations, and are run through parallel processors on the GPU. This parallel execution model done by the compute pipeline is organized into a dispatch, thread groups, and threads. The dispatch is a 3-dimensional container of thread groups, and a thread group is a 3-dimensional container of threads. Thread groups are ran on the GPU in *waves.*

This pipeline allows for workloads to be easily sent to the GPU without the need for restructuring all of a program's code.

A typical compute pipeline contains a read-only shader resource view as an input, constant buffer views for additional resource constants, and an unordered access view for an output. It is important to set the resource states of these resources in order to improve performance.

## Example code

The initialization of the compute pipeline involves creating the root signature, reading the compute shader, and creating the pipeline state object.

```mw
// Set the root signature
CD3DX12_VERSIONED_ROOT_SIGNATURE_DESC root_signature_desc{
    1, root_parameters, 
    0, nullptr
};

// Serialize the root signature
Microsoft::WRL::ComPtr<ID3DBlob> root_signature_blob{nullptr};
Microsoft::WRL::ComPtr<ID3DBlob> error_blob{nullptr};
D3DX12SerializeVersionedRootSignature(
    &root_signature_desc, D3D_ROOT_SIGNATURE_VERSION_1_1,
    root_signature_blob.GetAddressOf(), error_blob.GetAddressOf()
);

// Create the root signature
Microsoft::WRL::ComPtr<ID3D12RootSignature> root_signature{nullptr};
device->CreateRootSignature(
    0, root_signature_blob->GetBufferPointer(),
    root_signature_blob->GetBufferSize(),
    IID_PPV_ARGS(root_signature.GetAddressOf())
);

// Read the compute shader
Windows::WRL::ComPtr<ID3DBlob> compute_shader{nullptr};
D3DReadFileToBlob(L"C:/path/to/compute/shader", compute_shader.GetAddressOf());

// Create the compute pipeline state object (PSO)
struct PipelineStateStream {
    CD3DX12_PIPELINE_STATE_STREAM_ROOT_SIGNATURE root_signature;
    CD3DX12_PIPELINE_STATE_STREAM_CS compute_shader;
} pipeline_state_stream;

// Setting the root signature and the compute shader to the PSO
pipeline_state_stream.root_signature = root_signature.Get();
pipeline_state_stream.compute_shader = CD3DX12_SHADER_BYTECODE{compute_shader.Get()};

D3D12_PIPELINE_STATE_STREAM_DESC pipeline_state_stream_desc{
    sizeof(PipelineStateStream), &pipeline_state_stream
};
 
// Create pipeline state
device->CreatePipelineState(
    &pipeline_state_stream_desc,
    IID_PPV_ARGS(pipeline_state_stream.GetAddressOf())
);
```

After the initialization of the compute pipeline, every frame, the pipeline state must be set, the compute root signature must be set, and the dispatch is run.

```mw
command_list->SetPipelineState(pipeline_state);
command_list->SetComputeRootSignature(root_signature);
command_list->Dispatch(groups_x, groups_y, groups_z);
```
