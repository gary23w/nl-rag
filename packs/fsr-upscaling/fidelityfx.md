---
title: "GPUOpen"
source: https://en.wikipedia.org/wiki/FidelityFX
domain: fsr-upscaling
license: CC-BY-SA-4.0
tags: fidelityfx super resolution, fsr upscaling, spatial image upscaling, lanczos resampling upscale
fetched: 2026-07-02
---

# GPUOpen

(Redirected from

FidelityFX

)

**GPUOpen** is a middleware software suite originally developed by AMD's Radeon Technologies Group that offers advanced visual effects for computer games. It was released in 2016. GPUOpen serves as an alternative to, and a direct competitor of Nvidia GameWorks. GPUOpen is similar to GameWorks in that it encompasses several different graphics technologies as its main components that were previously independent and separate from one another. However, GPUOpen is partially open source software, unlike GameWorks which is proprietary and closed.

## History

GPUOpen was announced on December 15, 2015, and released on January 26, 2016.

## Rationale

Nicolas Thibieroz, AMD's Senior Manager of Worldwide Gaming Engineering, argues that "it can be difficult for developers to leverage their R&D investment on both consoles and PC because of the disparity between the two platforms" and that "proprietary libraries or tools chains with 'black box' APIs prevent developers from accessing the code for maintenance, porting or optimizations purposes". He says that upcoming architectures, such as AMD's RX 400 series "include many features not exposed today in PC graphics APIs".

AMD designed GPUOpen to be a competing open-source middleware stack released under the MIT License. The libraries are intended to increase software portability between video game consoles, PCs and also high-performance computing.

## Components

GPUOpen unifies many of AMD's previously separate tools and solutions into one package, also fully open-sourcing them under the MIT License. GPUOpen also makes it easy for developers to get low-level GPU access.

Additionally AMD wants to grant interested developers the kind of low-level "direct access" to their GCN-based GPUs, that surpasses the possibilities of Direct3D 12 or Vulkan. AMD mentioned e.g. a low-level access to the Asynchronous Compute Engines (ACEs). The ACE implement "Asynchronous Compute", but they cannot be freely configured under either Vulkan or Direct3D 12.

GPUOpen is made up of several main components, tools, and SDKs.

### Games and CGI

Software for computer-generated imagery (CGI) used in development of computer games and movies alike.

#### Visual effects libraries

| Name | API | Source | Description |
|---|---|---|---|
| TressFX | DirectX 12, Vulkan | GitHub | This visual effects library allows the creation of realistic hair, fur, and grass. |
| GeometryFX | DirectX 11 | GitHub | This library allows easy access to compute-based triangle filtering. |
| DepthOfFieldFX | DirectX 11 | GitHub | This library grants access to a depth of field implementation optimized for the GCN GPU architecture via a compute shader. |
| ShadowFX | DirectX 11, DirectX 12 | GitHub | This library grants access to an implementation for deferred shadow filtering that is optimized for the GCN GPU architecture. |
| FidelityFX | DirectX 11, DirectX 12, Vulkan | GitHub | FidelityFX is a suite of visual effects and effects-helper libraries. |

#### FidelityFX

| Name | Algorithm | Source | Description | Official support |
|---|---|---|---|---|
| FidelityFX CAS | Contrast Adaptive Sharpening | GitHub | This algorithm adaptively sharpens an image or scene while minimizing artifacts. | DirectX 11+, DirectX 12, Vulkan |
| FidelityFX CACAO | Combined Adaptive Compute Ambient Occlusion | GitHub | This algorithm is an optimized implementation of adaptive sampling ambient occlusion. | DirectX 11+, DirectX 12, Vulkan |
| FidelityFX LPM | Luminance Preserving Mapper | GitHub | This algorithm is used to tone map the luma of an RGB pixel rather than tone mapping the color of the pixel. | DirectX 11+, DirectX 12, Vulkan |
| FidelityFX SPD | Single Pass Downsampler | GitHub | This algorithm, optimized for the RDNA GPU architecture, is used to generate 12 MIP levels for a given texture. | DirectX 11+, DirectX 12, Vulkan |
| FidelityFX SSSR | Stochastic Screen Space Reflections | GitHub | This algorithm is used to add screen space reflections to a frame or scene. | DirectX 11+, DirectX 12, Vulkan |
| FidelityFX VS | Variable Shading | GitHub | This algorithm is used to generate image-based variable rate shading using the luminance of samples in the prior frame. | DirectX 11+, DirectX 12, Vulkan |
| FidelityFX Parallel Sort | Radix Sort | GitHub | This algorithm provides a compute-based radix sort. | DirectX 11+, DirectX 12, Vulkan |
| FidelityFX Denoiser | Shadow & Reflection Denoiser | GitHub | This algorithm provides denoising functionality for ray-traced shadows and ray-traced or screen-space reflections. | DirectX 11+, DirectX 12, Vulkan |
| FidelityFX Super Resolution 1 | Spatial Upsampler | GitHub | This algorithm is used to upsample an image or frame into a higher resolution using only the spatial information provided in the input frame. | DirectX 11+, DirectX 12, Vulkan |
| FidelityFX Super Resolution 2 | Temporal Upscaler | GitHub | This algorithm is used to upscale frame(s) into a higher resolution using the temporal information provided by input frames. | DirectX 12, Vulkan |
| FSR 3 Frame Generation | Analytical temporal frame interpolator | GitHub | This algorithm increases the perceived frame rate of a game by calculating an intermediate frame based of two already rendered frames. | AMD RDNA 2+, NVIDIA RTX 20+, Intel Arc |
| FSR™ “Redstone” |   |   |   |   |
| FSR™ Upscaling | Neural network-based image upscaler | GitHub | This algorithm uses machine learning–based models to upscale rendered frames to a higher resolution. | AMD RDNA 4 |
| FSR™ Frame Generation | Neural network-based frame interpolator | This algorithm uses machine learning-based models to generate an intermediate frame based off two already rendered frames. | AMD RDNA 4 |   |
| FSR™ Ray Regeneration | Neural network-based real-time denoiser | This algorithm uses machine learning-based models to denoise ray traced surfaces. | AMD RDNA 4 |   |
| FSR™ Radiance Caching (Technical Preview) | Neural network-based radiance caching | This algorithm uses machine learning-based models to approximate indirect radiance in path-traced scenes, reducing the number of required ray calculations. | AMD RDNA 4 |   |

#### FidelityFX Super Resolution

***FidelityFX Super Resolution*** (***FSR***) is a real time rendering technology suite. There are multiple versions of FSR with distinctive techniques:

- FSR 1 is a spatial upscaler based on or similar to the Lanczos algorithm, requiring an anti-aliased lower resolution image. It also performs edge reconstruction and gradient reversal. This is then followed by a contrast adaptive sharpening pass (RCAS) to reintroduce detail into the final image. AMD states:FSR is composed of two main passes:An upscaling pass called **EASU** (Edge-Adaptive Spatial Upsampling) that also performs edge reconstruction. In this pass the input frame is analyzed and the main part of the algorithm detects gradient reversals – essentially looking at how neighboring gradients differ – from a set of input pixels. The intensity of the gradient reversals defines the weights to apply to the reconstructed pixels at display resolution.A sharpening pass called **RCAS** (Robust Contrast-Adaptive Sharpening) that extracts pixel detail in the upscaled image.
- FSR 2 is a temporal upscaler based on a modified Lanczos requiring an aliased lower resolution image and utilising the temporal data (such as motion vectors and frame history) and then applies its own antialiasing pass which replaces the game's built in antialiasing solution.
- FSR 3 adds frame generation and "native antialiasing". Frame generation increases the perceived frame rate of a game. "Native antialiasing", similar to Nvidia's DLAA, can be used without upscaling for improved antialiasing; it can also be combined with frame generation and Anti-Lag+.
- FSR™ “Redstone” (formerly marketed as FSR 4) is a rendering suite that uses machine learning–based models for upscaling, frame generation, ray regeneration, and radiance caching.

| Release | Release date | Highlights |
|---|---|---|
| 1.0 / *1.0.1* | Jun 2021 | FidelityFX Super Resolution (FSR) launch, source code available July 2021. |
| *1.0.2* | Nov 2021 | Robust Contrast-Adaptive Sharpening (RCAS) oversharpening hotfix. |
| 1.1 | Jul 2023 | Available as part of FidelityFX SDK. |
| 2.0.1 / *2.0.1a* | Mar 2022 | FidelityFX Super Resolution 2.0 (FSR 2) launch, source code available June 2022. |
| 2.1.0 | Sep 2022 | Reduced ghosting and improved upscaling quality. Farming Simulator 2022 was one of early adopters with patch 1.7.1. |
| *2.1.1* | Sep 2022 |   |
| *2.1.2* | Oct 2022 |   |
| 2.2.0 / *2.2.0a* | Nov 2022 | HDR range improvements, ghosting and flickering artefacts reduction. Source code available February 2023. |
| *2.2.1* | Jun 2023 |   |
| 2.2.2 | Jul 2023 | Available as part of FidelityFX SDK. |
| 3.0 / *3.0.3* | Sep 2023 | FSR 3 adds frame generation combined with FSR 2 and Anti-Lag+ and supports GPUs from AMD, Nvidia, and Intel. FSR 3 is also compatible with the ninth generation of video game consoles. Source code available December 2023 as part of FidelityFX SDK. |
| *3.0.4* | Mar 2024 |   |
| *3.1.0* | Jun 2024 | Reduced ghosting, flickering and shimmering and improved temporal stability. Decoupled frame generation from upscaling. Made source file easily upgradable for developers. Vulkan and Xbox Game Development Kit (GDK) support. Source code available July 2024 as part of FidelityFX SDK 1.1. |
| FSR™ “Redstone” |   |   |
| FSR™ Upscaling (4.0.2) | Aug 2025 | Introduced a machine learning-based algorithm to increase the resolution of an image based off an input image. |
| *FSR™ Upscaling (4.0.3)* | Dec 2025 | Fixing a rendering error when surface dimensions are not multiples of 8. |
| FSR™ Frame Generation (4.0.0) | Dec 2025 | Introduced a machine learning-based frame interpolation algorithm. |
| FSR™ Ray Regeneration (1.0.0) | Dec 2025 | Introduced a machine learning-based real-time denoiser for ray-traced workloads. |
| FSR™ Radiance Caching (0.9.0) (Preview) | Dec 2025 | Machine learning–based radiance caching technique that approximates indirect lighting in path-traced scenes to reduce ray sampling requirements (preview). |

The standard presets for FSR by AMD can be found in the table below. Note that these presets are not the only way in which the algorithm can be used, they are simply presets for input/output resolutions. Certain titles, such as *Dota 2*, offer resolution sliders to fine tune the scaling percentage or dynamically scaling the internal render resolution depending on the FPS cap. AMD has also created a command-line interface tool which allows the user to upscale any image using FSR1/EASU as in addition to other upsampling methods such as bilinear interpolation. It also allows the user to run various stages of the FSR pipeline, such as RCAS, independently.

| Quality preset | Scale factor | Render scale |
|---|---|---|
| Native AA (since v3.0) | 1.00× | 100% |
| Ultra Quality (v1.0 only) | 1.30× | 77.0% |
| Quality | 1.50× | 66.6% |
| Balanced | 1.70× | 58.8% |
| Performance | 2.00× | 50.0% |
| Ultra Performance (since v2.0) | 3.00× | 33.3% |

FSR 2 can also be modded into nearly any game supporting DLSS by swapping the DLSS DLL with a translation layer DLL that maps the DLSS API calls to FSR 2 API calls.

1. FSR versions stated in *italic* present hotfixes or minor updates.
2. The algorithm does not necessarily need to be implemented using these presets; it is possible for the implementer to define custom input and output resolutions.
3. The linear scale factor used for upsampling the input resolution to the output resolution. For example, a scene rendered at 540p with a 2.00x scale factor would have an output resolution of 1080p.
4. The linear render scale, compared to the output resolution, that the technology uses to render scenes internally before upsampling. For example, a 1080p scene with a 50% render scale would have an internal resolution of 540p.

#### Frame Generation

FSR 3 adds frame generation, a technique that creates new frames in between existing ones by using motion interpolation. Launching in September 2023, FSR 3 uses a combination of FSR 2 and optical flow analysis, which runs using asynchronous compute (as opposed to Nvidia's DLSS 3 which uses dedicated hardware). Because FSR 3 uses a software-based solution, it is compatible with GPUs from AMD, Nvidia, and Intel as well as the ninth generation of video game consoles. To combat additional latency inherent to the frame generation process, AMD has a driver-level feature called Anti-Lag, which only runs on AMD GPUs.

FSR “Redstone” adds a machine learning-based approach to generate frames.

AMD Fluid Motion Frames (AFMF) is a driver-level frame generation technology launching in Q1 2024 which is compatible with all DirectX 11 and DirectX 12 games, however it runs on RDNA 2 and RDNA 3 GPUs. AFMF uses optical flow analysis but not motion vectors, so it can only interpolate a new frame between two traditionally rendered frames. AFMF currently is not compatible with VSYNC.

#### Tools

The official AMD directory lists:

| Name | Source code | API | OS | Task |
|---|---|---|---|---|
| CodeXL | CodeXL | Direct3D, OpenGL, OpenCL, Vulkan | Linux Windows | software development tool suite that includes a GPU debugger, a GPU profiler, a CPU profiler, a static OpenCL kernel analyzer and various plugins. |
| static analyzer for AMD CodeXL | amd-codexl-analyzer | Direct3D, OpenGL, OpenCL | Linux Windows 64bit | Off-line compiler and performance analysis CLI-tool for processing: OpenCL kernels, HLSL shaders and GLSL shaders part of the AMD CodeXL tools suite Requires either Radeon Software Crimson Edition or AMD Catalyst to be installed to run this tool. |
| D3D 12 plug-in for GPU PerfStudio | amd-gpuperfstudio-dx12 | Direct3D 12 | Windows | a plug-in to GPU PerfStudio GPU perfstudio |
| Tootle | amd-tootle | agnostic | Linux Windows | **Triangle Order Optimization Tool**; originally developed in 2006; can be easily integrated as part of a rendering or mesh pre-processing tool chain Cf. http://mgarland.org/files/papers/quadrics.pdf |

Having been released by ATI Technologies under the BSD license in 2006 HLSL2GLSL is not part of GPUOpen. Whether similar tools for SPIR-V will be available remains to be seen, as is the official release of the Vulkan (API) itself. Source-code that has been defined as being part of GPUOpen is also part of the Linux kernel (e.g. amdgpu and amdkfd), Mesa 3D and LLVM.

#### Software development kits

| Name | Source | API | OS | Task |
|---|---|---|---|---|
| Advanced Media Framework (AMF) SDK | GitHub | DirectX 12 | Linux, Windows 64-bit | Light-weight, portable multimedia framework that abstracts away most of the platform and API-specific details. |
| AMD GPU Services (AGS) SDK | GitHub | DirectX | Windows 64-bit |   |
| LiquidVR SDK | GitHub | Direct3D 11 | Windows | improves the smoothness of virtual reality. The aim is to reduce latency between hardware so that the hardware can keep up with the user's head movement, eliminating the motion sickness. A particular focus is on dual GPU setups where each GPU will now render for one eye individually of the display |
| Radeon Machine Learning (RML) SDK | GitHub | DirectX 12, Metal, OpenCL | Linux, OS X, Windows |   |
| Radeon ProRender SDK (formerly FireRender) | GitHub | OpenCL | Linux, macOS, Windows | physically-based rendering engine |
| RadeonRays SDK (formerly FireRays) | GitHub | DirectX 12, Vulkan | Linux 64-bit, OS X, Windows 64-bit | A high efficiency, high performance heterogeneous ray tracing intersection library for GPU and CPU or APU on any platform. |
| RapidFire SDK | GitHub | DirectX, OpenGL | Windows | facilitates the use of AMD's video compression acceleration SIP blocks VCE (H.264 encoder) and UVD (H.264 decoder) for "Cloud gaming"/off-site rendering |
| True Audio Next (TAN) SDK | GitHub | OpenCL | Windows 64-bit | SDK for Radeon GPU accelerated and multi-core high-performance audio signal processing. |

### Professional Compute

As of 2022, AMD compute software ecosystem is regrouped under the ROCm metaproject.

Software around Heterogeneous System Architecture (HSA), General-Purpose computing on Graphics Processing Units (GPGPU) and High-Performance Computing (HPC)

#### Radeon Open Compute (ROCm)

AMD's "Boltzmann Initiative" (named after Ludwig Boltzmann) was announced in November 2015 at the SuperComputing15 and productized as the Radeon Open Compute platform (ROCm). It aims to provide an alternative to Nvidia's CUDA which includes a tool to port CUDA source-code to portable (HIP) source-code which can be compiled on both HCC and NVCC.

- Radeon Open Compute Kernel (ROCK) driver
- Radeon Open Compute Runtime (ROCR) runtime
- HCC: Heterogeneous Compute Compiler
- HIP: C++ Heterogeneous-Compute Interface for Portability

#### Heterogeneous System Architecture

- HSAIL-GDB: provides an GNU Debugger-based debugging environment for HSA Intermediate Layer (HSAIL)
- HSA Runtime APIs
- Linux amdkfd v1.6.1 release for Kaveri & Carrizo

#### Various (deprecated)

- clFFT library for Fast Fourier transform written in OpenCL
- hcFFT library for Fast Fourier transform written in HCC-optimized C++

## Availability

GPUOpen are available under the MIT license to the general public through GitHub starting on January 26, 2016.

There is interlocking between GPUOpen and well established and widespread free software projects, e.g. Linux kernel, Mesa 3D and LLVM.
