---
title: "CUDA"
source: https://en.wikipedia.org/wiki/CUDA
domain: high-performance-computing
license: CC-BY-SA-4.0
tags: high-performance computing, parallel computing, amdahl law, gpu general-purpose computing
fetched: 2026-07-02
---

# CUDA

**CUDA** (**Compute Unified Device Architecture**) is a proprietary parallel computing platform and application programming interface (API) developed by the American technology corporation Nvidia that allows software to use certain types of graphics processing units (GPUs) for accelerated general-purpose processing, significantly broadening their utility in scientific and high-performance computing. CUDA was created by Nvidia starting in 2004 and was officially released in 2007. When it was first introduced, the name was an acronym for *Compute Unified Device Architecture*, but Nvidia later dropped the common use of the acronym and now rarely expands it.

CUDA is both a software layer that manages data, giving direct access to the GPU and CPU as necessary, and a library of APIs that enable parallel computation for various needs. In addition to drivers and runtime kernels, the CUDA platform includes compilers, libraries and developer tools to help programmers accelerate their applications.

CUDA is written in the C programming language but is designed to work with a wide array of other programming languages including C++, Fortran, Python and Julia. This accessibility makes it easier for specialists in parallel programming to use GPU resources, in contrast to prior APIs like Direct3D and OpenGL, which require advanced skills in graphics programming. CUDA-powered GPUs also support programming frameworks such as OpenMP, OpenACC and OpenCL.

## Background

The graphics processing unit (GPU), as a specialized computer processor, addresses the demands of real-time high-resolution 3D graphics compute-intensive tasks. By 2012, GPUs had evolved into highly parallel multi-core systems allowing efficient manipulation of large blocks of data. This design is more effective than general-purpose central processing unit (CPUs) for algorithms in situations where processing large blocks of data is done in parallel, such as:

- cryptographic hash functions
- machine learning
- molecular dynamics simulations
- physics engines

The origins of CUDA trace to the early 2000s, when Ian Buck, a computer science Ph.D. student at Stanford University, began experimenting with using GPUs for purposes beyond rendering graphics. Buck had first become interested in GPUs during his undergraduate studies at Princeton University, initially through video gaming. After graduation, he interned at Nvidia, gaining deeper exposure to GPU architecture. At Stanford, he built an 8K gaming rig using 32 GeForce graphics cards, originally to push the limits of graphics performance in games like Quake and Doom. However, his interests shifted toward exploring the potential of GPUs for general-purpose parallel computing.

To that end, Buck developed Brook, a programming language designed to enable general-purpose computing on GPUs. His work attracted support from both Nvidia and the Defense Advanced Research Projects Agency (DARPA). In 2004, Nvidia hired Buck and paired him with John Nickolls, the company's director of architecture for GPU computing. Together, they began transforming Brook into what would become CUDA. CUDA was officially released by Nvidia in 2007.

Under the leadership of Nvidia CEO Jensen Huang, CUDA became central to the company's strategy of positioning GPUs as versatile hardware for scientific applications. By 2015, CUDA's development increasingly focused on accelerating machine learning and artificial neural network workloads.

## Ontology

The following table offers a non-exact description for the ontology of the CUDA framework.

| memory (hardware) | memory (code, or variable scoping) | computation (hardware) | computation (code syntax) | computation (code semantics) |
|---|---|---|---|---|
| RAM | non-CUDA variables | host | program | one routine call |
| VRAM, GPU L2 cache | global, const, texture | device | grid | simultaneous call of the same subroutine on many processors |
| GPU L1 cache | local, shared | SM ("streaming multiprocessor") | block | individual subroutine call |
|   |   | warp = 32 threads |   | SIMD instructions |
| GPU L0 cache, register |   | thread (aka. "SP", "streaming processor", "cuda core", but these names are now deprecated) |   | analogous to individual scalar ops within a vector op |

## Programming abilities

The CUDA platform is accessible to software developers through CUDA-accelerated libraries, compiler directives such as OpenACC, and extensions to industry-standard programming languages including C, C++, Fortran and Python. C/C++ programmers can use 'CUDA C/C++', compiled to PTX with nvcc (Nvidia's LLVM-based C/C++ compiler) or by clang itself. Fortran programmers can use 'CUDA Fortran', compiled with the PGI CUDA Fortran compiler from The Portland Group. Python programmers can use the cuPyNumeric library to accelerate applications on Nvidia GPUs.

In addition to libraries, compiler directives, CUDA C/C++ and CUDA Fortran, the CUDA platform supports other computational interfaces, including the Khronos Group's OpenCL, Microsoft's DirectCompute, OpenGL Compute Shader and C++ AMP. Third party wrappers are also available for Python, Perl, Fortran, Java, Ruby, Lua, Common Lisp, Haskell, R, MATLAB, IDL, Julia, and native support in Mathematica.

In the computer game industry, GPUs are used for graphics rendering, and for game physics calculations (physical effects such as debris, smoke, fire, fluids); examples include PhysX and Bullet. CUDA has also been used to accelerate non-graphical applications in computational biology, cryptography and other fields by an order of magnitude or more.

CUDA provides both a low level API (CUDA **Driver** API, non single-source) and a higher level API (CUDA **Runtime** API, single-source). The initial CUDA SDK was made public on 15 February 2007, for Microsoft Windows and Linux. Mac OS X support was later added in version 2.0, which supersedes the beta released February 14, 2008. CUDA works with all Nvidia GPUs from the G8x series onwards, including GeForce, Quadro and the Tesla line. CUDA is compatible with most standard operating systems.

CUDA 8.0 comes with the following libraries (for compilation & runtime, in alphabetical order):

- cuBLAS – CUDA Basic Linear Algebra Subroutines library
- CUDART – CUDA Runtime library
- cuFFT – CUDA Fast Fourier Transform library
- cuRAND – CUDA Random Number Generation library
- cuSOLVER – CUDA based collection of dense and sparse direct solvers
- cuSPARSE – CUDA Sparse Matrix library
- NPP – NVIDIA Performance Primitives library
- nvGRAPH – NVIDIA Graph Analytics library
- NVML – NVIDIA Management Library
- NVRTC – NVIDIA Runtime Compilation library for CUDA C++

CUDA 8.0 comes with these other software components:

- nView – NVIDIA nView Desktop Management Software
- NVWMI – NVIDIA Enterprise Management Toolkit
- GameWorks PhysX – is a multi-platform game physics engine

CUDA 9.0–9.2 comes with these other components:

- CUTLASS 1.0 – custom linear algebra algorithms,
- NVIDIA Video Decoder was deprecated in CUDA 9.2; it is now available in NVIDIA Video Codec SDK

CUDA 10 comes with these other components:

- nvJPEG – Hybrid (CPU and GPU) JPEG processing

CUDA 11.0–11.8 comes with these other components:

- CUB is new one of more supported C++ libraries
- MIG multi instance GPU support
- nvJPEG2000 – JPEG 2000 encoder and decoder

## Advantages

CUDA has several advantages over traditional general-purpose computation on GPUs (GPGPU) using graphics APIs:

- Scattered reads – code can read from arbitrary addresses in memory
- Unified virtual memory (CUDA 4.0 and above)
- Unified memory (CUDA 6.0 and above)
- Shared memory – CUDA exposes a fast shared memory region that can be shared among threads. This can be used as a user-managed cache, enabling higher bandwidth than is possible using texture lookups.
- Faster downloads and readbacks to and from the GPU
- Full support for integer and bitwise operations, including integer texture lookups

## Limitations

- Whether for the host computer or the GPU device, all CUDA source code is now processed according to C++ syntax rules. This was not always the case. Earlier versions of CUDA were based on C syntax rules. As with the more general case of compiling C code with a C++ compiler, it is therefore possible that old C-style CUDA source code will either fail to compile or will not behave as originally intended.
- Interoperability with rendering languages such as OpenGL is one-way, with OpenGL having access to registered CUDA memory but CUDA not having access to OpenGL memory.
- Copying between host and device memory may incur a performance hit due to system bus bandwidth and latency (this can be partly alleviated with asynchronous memory transfers, handled by the GPU's DMA engine).
- Threads should be running in groups of at least 32 for best performance, with total number of threads numbering in the thousands. Branches in the program code do not affect performance significantly, provided that each of 32 threads takes the same execution path; the SIMD execution model becomes a significant limitation for any inherently divergent task (e.g. traversing a space partitioning data structure during ray tracing).
- No emulation or fallback functionality is available for modern revisions.
- Valid C++ may sometimes be flagged and prevent compilation due to the way the compiler approaches optimization for target GPU device limitations.
- C++ run-time type information (RTTI) and C++-style exception handling are only supported in host code, not in device code.
- In single-precision on first generation CUDA compute capability 1.x devices, denormal numbers are unsupported and are instead flushed to zero, and the precision of both the division and square root operations are slightly lower than IEEE 754-compliant single precision math. Devices that support compute capability 2.0 and above support denormal numbers, and the division and square root operations are IEEE 754 compliant by default. However, users can obtain the prior faster gaming-grade math of compute capability 1.x devices if desired by setting compiler flags to disable accurate divisions and accurate square roots, and enable flushing denormal numbers to zero.
- Unlike OpenCL, CUDA-enabled GPUs are only available from Nvidia as it is proprietary. Attempts to implement CUDA on other GPUs include:
  - Project Coriander: Converts CUDA C++11 source to OpenCL 1.2 C. A fork of CUDA-on-CL intended to run TensorFlow.
  - CU2CL: Convert CUDA 3.2 C++ to OpenCL C.
  - GPUOpen HIP: A thin abstraction layer on top of CUDA and ROCm intended for AMD and Nvidia GPUs. Has a conversion tool for importing CUDA C++ source. Supports CUDA 4.0 plus C++11 and float16.
  - ZLUDA is a drop-in replacement for CUDA on AMD GPUs and formerly Intel GPUs with near-native performance. The developer, Andrzej Janik, was separately contracted by both Intel and AMD to develop the software in 2021 and 2022, respectively. However, neither company decided to release it officially due to the lack of a business use case. AMD's contract included a clause that allowed Janik to release his code for AMD independently, allowing him to release the new version that only supports AMD GPUs.
  - ChipStar can compile and run CUDA/HIP programs on advanced OpenCL 3.0 or Level Zero platforms.
  - SCALE is a CUDA-compatible programming toolkit for ahead of time compilation of CUDA source code on AMD GPUs, aiming to expand support for other GPUs in the future.

## Example

This example code in C++ loads a texture from an image into an array on the GPU:

```mw
texture<float, 2, cudaReadModeElementType> tex;

void foo() {
    cudaArray* cu_array;

    // Allocate array
    cudaChannelFormatDesc description = cudaCreateChannelDesc<float>();
    cudaMallocArray(&cu_array, &description, width, height);

    // Copy image data to array
    cudaMemcpyToArray(cu_array, image, width*height*sizeof(float), cudaMemcpyHostToDevice);

    // Set texture parameters (default)
    tex.addressMode[0] = cudaAddressModeClamp;
    tex.addressMode[1] = cudaAddressModeClamp;
    tex.filterMode = cudaFilterModePoint;
    tex.normalized = false; // do not normalize coordinates

    // Bind the array to the texture
    cudaBindTextureToArray(tex, cu_array);

    // Run kernel
    dim3 blockDim(16, 16, 1);
    dim3 gridDim((width + blockDim.x - 1)/ blockDim.x, (height + blockDim.y - 1) / blockDim.y, 1);
    kernel<<< gridDim, blockDim, 0 >>>(d_data, height, width);

    // Unbind the array from the texture
    cudaUnbindTexture(tex);
}

__global__ void kernel(float* odata, int height, int width) {
    unsigned int x = blockIdx.x*blockDim.x + threadIdx.x;
    unsigned int y = blockIdx.y*blockDim.y + threadIdx.y;
    if (x < width && y < height) {
        float c = tex2D(tex, x, y);
        odata[y*width+x] = c;
    }
}
```

Below is an example given in Python that computes the product of two arrays on the GPU. The unofficial Python language bindings can be obtained from *PyCUDA*.

```mw
import numpy
import pycuda.autoinit

from numpy.typing import NDArray, float32
from pycuda.compiler import SourceModule
from pycuda.driver import Function, In, Out

mod: SourceModule = SourceModule(
    """
__global__ void multiply_them(float* dest, float* a, float* b) {
    const int i = threadIdx.x;
    dest[i] = a[i] * b[i];
}
"""
)

multiply_them: Function = mod.get_function("multiply_them")

a: NDArray[float32] = numpy.random.randn(400).astype(numpy.float32)
b: NDArray[float32] = numpy.random.randn(400).astype(numpy.float32)

dest: NDArray[float32] = numpy.zeros_like(a)
multiply_them(Out(dest), In(a), In(b), block=(400, 1, 1))

print(dest - a * b)
```

Additional Python bindings to simplify matrix multiplication operations can be found in the program *pycublas*.

```mw
 
import numpy

from pycublas import CUBLASMatrix

A: CUBLASMatrix = CUBLASMatrix(numpy.mat([[1, 2, 3], [4, 5, 6]], numpy.float32))
B: CUBLASMatrix = CUBLASMatrix(numpy.mat([[2, 3], [4, 5], [6, 7]], numpy.float32))
C: CUBLASMatrix = A * B
print(C.np_mat())
```

while CuPy directly replaces NumPy:

```mw
import cupy

from cupy.typing import NDArray, float64

a: NDArray[float64] = cupy.random.randn(400)
b: NDArray[float64] = cupy.random.randn(400)

dest: NDArray[float64] = cupy.zeros_like(a)

print(dest - a * b)
```

## GPUs supported

Note on notation: compute capability X.Y is also written as SMXY or sm_XY (e.g. 10.3 as SM103 or sm_103) in professional Nvidia software and the code Nvidia has contributed to LLVM.

Below is a table of supported CUDA compute capabilities based on the CUDA SDK version and microarchitecture, listed by code name:

CUDA SDK support vs. microarchitecture (cell: compute capability)

CUDA SDK

version(s)

Tesla

Fermi

Kepler

(early)

Kepler

(late)

Maxwell

Pascal

Volta

Turing

Ampere

Ada

Lovelace

Hopper

Blackwell

1.0

1.0 – 1.1

1.1

1.0 – 1.1+x

2.0

1.0 – 1.1+x

2.1 – 2.3.1

1.0 – 1.3

3.0 – 3.1

1.0

2.0

3.2

1.0

2.1

4.0 – 4.2

1.0

2.1

5.0 – 5.5

1.0

3.0

3.5

6.0

1.0

3.2

3.5

6.5

1.1

3.7

5.x

7.0 – 7.5

2.0

5.x

8.0

2.0

6.x

9.0 – 9.2

3.0

7.0 – 7.2

10.0 – 10.2

3.0

7.5

11.0

3.5

8.0

11.1 – 11.4

3.5

8.6

11.5 – 11.7.1

3.5

8.7

11.8

3.5

8.9

9.0

12.0 – 12.6

5.0

9.0

12.8

5.0

12.0

12.9

5.0

12.1

13.0 – 13.3

7.5

12.1

Note: CUDA SDK 10.2 is the last official release for macOS, as support will not be available for macOS in newer releases.

CUDA compute capability by version with associated GPU semiconductors and GPU card models (separated by their various application areas):

| Compute capability (version) | Micro- architecture | GPUs | GeForce | Quadro, NVS | Tesla/Datacenter | Tegra, Jetson, DRIVE |
|---|---|---|---|---|---|---|
| 1.0 | Tesla | G80 | GeForce 8800 Ultra, GeForce 8800 GTX, GeForce 8800 GTS(G80) | Quadro FX 5600, Quadro FX 4600, Quadro Plex 2100 S4 | Tesla C870, Tesla D870, Tesla S870 |   |
| 1.1 | G92, G94, G96, G98, G84, G86 | GeForce GTS 250, GeForce 9800 GX2, GeForce 9800 GTX, GeForce 9800 GT, GeForce 8800 GTS(G92), GeForce 8800 GT, GeForce 9600 GT, GeForce 9500 GT, GeForce 9400 GT, GeForce 8600 GTS, GeForce 8600 GT, GeForce 8500 GT, GeForce G110M, GeForce 9300M GS, GeForce 9200M GS, GeForce 9100M G, GeForce 8400M GT, GeForce G105M | Quadro FX 4700 X2, Quadro FX 3700, Quadro FX 1800, Quadro FX 1700, Quadro FX 580, Quadro FX 570, Quadro FX 470, Quadro FX 380, Quadro FX 370, Quadro FX 370 Low Profile, Quadro NVS 450, Quadro NVS 420, Quadro NVS 290, Quadro NVS 295, Quadro Plex 2100 D4, Quadro FX 3800M, Quadro FX 3700M, Quadro FX 3600M, Quadro FX 2800M, Quadro FX 2700M, Quadro FX 1700M, Quadro FX 1600M, Quadro FX 770M, Quadro FX 570M, Quadro FX 370M, Quadro FX 360M, Quadro NVS 320M, Quadro NVS 160M, Quadro NVS 150M, Quadro NVS 140M, Quadro NVS 135M, Quadro NVS 130M, Quadro NVS 450, Quadro NVS 420, Quadro NVS 295 |   |   |   |
| 1.2 | GT218, GT216, GT215 | GeForce GT 340*, GeForce GT 330*, GeForce GT 320*, GeForce 315*, GeForce 310*, GeForce GT 240, GeForce GT 220, GeForce 210, GeForce GTS 360M, GeForce GTS 350M, GeForce GT 335M, GeForce GT 330M, GeForce GT 325M, GeForce GT 240M, GeForce G210M, GeForce 310M, GeForce 305M | Quadro FX 380 Low Profile, Quadro FX 1800M, Quadro FX 880M, Quadro FX 380M, Nvidia NVS 300, NVS 5100M, NVS 3100M, NVS 2100M, ION |   |   |   |
| 1.3 | GT200, GT200b | GeForce GTX 295, GTX 285, GTX 280, GeForce GTX 275, GeForce GTX 260 | Quadro FX 5800, Quadro FX 4800, Quadro FX 4800 for Mac, Quadro FX 3800, Quadro CX, Quadro Plex 2200 D2 | Tesla C1060, Tesla S1070, Tesla M1060 |   |   |
| 2.0 | Fermi | GF100, GF110 | GeForce GTX 590, GeForce GTX 580, GeForce GTX 570, GeForce GTX 480, GeForce GTX 470, GeForce GTX 465, GeForce GTX 480M | Quadro 6000, Quadro 5000, Quadro 4000, Quadro 4000 for Mac, Quadro Plex 7000, Quadro 5010M, Quadro 5000M | Tesla C2075, Tesla C2050/C2070, Tesla M2050/M2070/M2075/M2090 |   |
| 2.1 | GF104, GF106 GF108, GF114, GF116, GF117, GF119 | GeForce GTX 560 Ti, GeForce GTX 550 Ti, GeForce GTX 460, GeForce GTS 450, GeForce GTS 450*, GeForce GT 640 (GDDR3), GeForce GT 630, GeForce GT 620, GeForce GT 610, GeForce GT 520, GeForce GT 440, GeForce GT 440*, GeForce GT 430, GeForce GT 430*, GeForce GT 420*, GeForce GTX 675M, GeForce GTX 670M, GeForce GT 635M, GeForce GT 630M, GeForce GT 625M, GeForce GT 720M, GeForce GT 620M, GeForce 710M, GeForce 610M, GeForce 820M, GeForce GTX 580M, GeForce GTX 570M, GeForce GTX 560M, GeForce GT 555M, GeForce GT 550M, GeForce GT 540M, GeForce GT 525M, GeForce GT 520MX, GeForce GT 520M, GeForce GTX 485M, GeForce GTX 470M, GeForce GTX 460M, GeForce GT 445M, GeForce GT 435M, GeForce GT 420M, GeForce GT 415M, GeForce 710M, GeForce 410M | Quadro 2000, Quadro 2000D, Quadro 600, Quadro 4000M, Quadro 3000M, Quadro 2000M, Quadro 1000M, NVS 310, NVS 315, NVS 5400M, NVS 5200M, NVS 4200M |   |   |   |
| 3.0 | Kepler | GK104, GK106, GK107 | GeForce GTX 770, GeForce GTX 760, GeForce GT 740, GeForce GTX 690, GeForce GTX 680, GeForce GTX 670, GeForce GTX 660 Ti, GeForce GTX 660, GeForce GTX 650 Ti BOOST, GeForce GTX 650 Ti, GeForce GTX 650, GeForce GTX 880M, GeForce GTX 870M, GeForce GTX 780M, GeForce GTX 770M, GeForce GTX 765M, GeForce GTX 760M, GeForce GTX 680MX, GeForce GTX 680M, GeForce GTX 675MX, GeForce GTX 670MX, GeForce GTX 660M, GeForce GT 750M, GeForce GT 650M, GeForce GT 745M, GeForce GT 645M, GeForce GT 740M, GeForce GT 730M, GeForce GT 640M, GeForce GT 640M LE, GeForce GT 735M, GeForce GT 730M | Quadro K5000, Quadro K4200, Quadro K4000, Quadro K2000, Quadro K2000D, Quadro K600, Quadro K420, Quadro K500M, Quadro K510M, Quadro K610M, Quadro K1000M, Quadro K2000M, Quadro K1100M, Quadro K2100M, Quadro K3000M, Quadro K3100M, Quadro K4000M, Quadro K5000M, Quadro K4100M, Quadro K5100M, NVS 510, Quadro 410 | Tesla K10, GRID K340, GRID K520, GRID K2 |   |
| 3.2 | GK20A |   |   |   | Tegra K1, Jetson TK1 |   |
| 3.5 | GK110, GK208 | GeForce GTX Titan Z, GeForce GTX Titan Black, GeForce GTX Titan, GeForce GTX 780 Ti, GeForce GTX 780, GeForce GT 640 (GDDR5), GeForce GT 630 v2, GeForce GT 730, GeForce GT 720, GeForce GT 710, GeForce GT 740M (64-bit, DDR3), GeForce GT 920M | Quadro K6000, Quadro K5200 | Tesla K40, Tesla K20x, Tesla K20 |   |   |
| 3.7 | GK210 |   |   | Tesla K80 |   |   |
| 5.0 | Maxwell | GM107, GM108 | GeForce GTX 750 Ti, GeForce GTX 750, GeForce GTX 960M, GeForce GTX 950M, GeForce 940M, GeForce 930M, GeForce GTX 860M, GeForce GTX 850M, GeForce 845M, GeForce 840M, GeForce 830M | Quadro K1200, Quadro K2200, Quadro K620, Quadro M2000M, Quadro M1000M, Quadro M600M, Quadro K620M, NVS 810 | Tesla M10 |   |
| 5.2 | GM200, GM204, GM206 | GeForce GTX Titan X, GeForce GTX 980 Ti, GeForce GTX 980, GeForce GTX 970, GeForce GTX 960, GeForce GTX 950, GeForce GTX 750 SE, GeForce GTX 980M, GeForce GTX 970M, GeForce GTX 965M | Quadro M6000 24GB, Quadro M6000, Quadro M5000, Quadro M4000, Quadro M2000, Quadro M5500, Quadro M5000M, Quadro M4000M, Quadro M3000M | Tesla M4, Tesla M40, Tesla M6, Tesla M60 |   |   |
| 5.3 | GM20B |   |   |   | Tegra X1, Jetson TX1, Jetson Nano, DRIVE CX, DRIVE PX |   |
| 6.0 | Pascal | GP100 |   | Quadro GP100 | Tesla P100 |   |
| 6.1 | GP102, GP104, GP106, GP107, GP108 | Nvidia TITAN Xp, Titan X, GeForce GTX 1080 Ti, GTX 1080, GTX 1070 Ti, GTX 1070, GTX 1060, GTX 1050 Ti, GTX 1050, GT 1030, GT 1010, MX350, MX330, MX250, MX230, MX150, MX130, MX110 | Quadro P6000, Quadro P5000, Quadro P4000, Quadro P2200, Quadro P2000, Quadro P1000, Quadro P400, Quadro P500, Quadro P520, Quadro P600, Quadro P5000 (mobile), Quadro P4000 (mobile), Quadro P3000 (mobile) | Tesla P40, Tesla P6, Tesla P4 |   |   |
| 6.2 | GP10B |   |   |   | Tegra X2, Jetson TX2, DRIVE PX 2 |   |
| 7.0 | Volta | GV100 | NVIDIA TITAN V | Quadro GV100 | Tesla V100, Tesla V100S |   |
| 7.2 | GV10B GV11B |   |   |   | Tegra Xavier, Jetson Xavier NX, Jetson AGX Xavier, DRIVE AGX Xavier, DRIVE AGX Pegasus, Clara AGX |   |
| 7.5 | Turing | TU102, TU104, TU106, TU116, TU117 | NVIDIA TITAN RTX, GeForce RTX 2080 Ti, RTX 2080 Super, RTX 2080, RTX 2070 Super, RTX 2070, RTX 2060 Super, RTX 2060 12GB, RTX 2060, GeForce GTX 1660 Ti, GTX 1660 Super, GTX 1660, GTX 1650 Super, GTX 1650, MX550, MX450 | Quadro RTX 8000, Quadro RTX 6000, Quadro RTX 5000, Quadro RTX 4000, T1000, T600, T400 T1200 (mobile), T600 (mobile), T500 (mobile), Quadro T2000 (mobile), Quadro T1000 (mobile) | Tesla T4 |   |
| 8.0 | Ampere | GA100 |   |   | A100 80GB, A100 40GB, A30 |   |
| 8.6 | GA102, GA103, GA104, GA106, GA107 | GeForce RTX 3090 Ti, RTX 3090, RTX 3080 Ti, RTX 3080 12GB, RTX 3080, RTX 3070 Ti, RTX 3070, RTX 3060 Ti, RTX 3060, RTX 3050, RTX 3050 Ti (mobile), RTX 3050 (mobile), RTX 2050 (mobile), MX570 | RTX A6000, RTX A5500, RTX A5000, RTX A4500, RTX A4000, RTX A2000 RTX A5000 (mobile), RTX A4000 (mobile), RTX A3000 (mobile), RTX A2000 (mobile) | A40, A16, A10, A2 |   |   |
| 8.7 | GA10B |   |   |   | Jetson Orin Nano, Jetson Orin NX, Jetson AGX Orin, DRIVE AGX Orin, IGX Orin |   |
| 8.9 | Ada Lovelace | AD102, AD103, AD104, AD106, AD107 | GeForce RTX 4090, RTX 4080 Super, RTX 4080, RTX 4070 Ti Super, RTX 4070 Ti, RTX 4070 Super, RTX 4070, RTX 4060 Ti, RTX 4060, RTX 4050 (mobile) | RTX 6000 Ada, RTX 5880 Ada, RTX 5000 Ada, RTX 4500 Ada, RTX 4000 Ada, RTX 4000 SFF Ada, RTX 2000 Ada, RTX 5000 Ada (mobile), RTX 4000 Ada (mobile), RTX 3500 Ada (mobile), RTX 2000 Ada (mobile) | L40S, L40, L20, L4, L2 |   |
| 9.0 | Hopper | GH100 |   |   | H200, H100, GH200 |   |
| 10.0 | Blackwell | GB100 |   |   | B200, B100, GB200 |   |
| 10.3 | GB110 |   |   | B300, GB300 |   |   |
| 11.0 | GB10B |   |   |   | Jetson AGX Thor, DRIVE AGX Thor |   |
| 12.0 | GB202, GB203, GB205, GB206, GB207 | GeForce RTX 5090, RTX 5080, RTX 5070 Ti, RTX 5070, RTX 5060 Ti, RTX 5060, RTX 5050 | RTX PRO 6000 Blackwell Workstation, RTX PRO 5000 Blackwell, RTX PRO 4500 Blackwell, RTX PRO 4000 Blackwell | RTX PRO 6000 Blackwell Server |   |   |
| 12.1 | GB20B |   | DGX Spark |   |   |   |
| Compute capability (version) | Micro- architecture | GPUs | GeForce | Quadro, NVS | Tesla/Datacenter | Tegra, Jetson, DRIVE |

* – OEM-only products

1. CUDA Toolkit 13.0 renamed the SM101 for Thor GPUs to SM110.

## Version features and specifications

Note: A GPU with a higher compute capacity is able to execute PTX code meant for a GPU of a lower range of compute capacities. However, it is possible to compile CUDA code into a form that only works on one family (same "X") of GPUs; if existing code is compiled this way, recompilation will be needed for it to work on a newer GPU.

Feature support (unlisted features are supported for all compute capabilities)

Compute capability (version)

1.0, 1.1

1.2, 1.3

2.x

3.0

3.2

3.5, 3.7, 5.x, 6.x, 7.0, 7.2

7.5

8.x

9.0, 10.x, 12.x

Warp vote functions (__all(), __any())

No

Yes

Warp vote functions (__ballot())

No

Yes

Memory fence functions (__threadfence_system())

Synchronization functions (__syncthreads_count(), __syncthreads_and(), __syncthreads_or())

Surface functions

3D grid of thread blocks

Warp shuffle functions

No

Yes

Unified memory programming

Funnel shift

No

Yes

Dynamic parallelism

No

Yes

Uniform Datapath

No

Yes

Hardware-accelerated async-copy

No

Yes

Hardware-accelerated

split arrive/wait barrier

Warp-level support for reduction ops

L2 cache residency management

DPX instructions for accelerated dynamic programming

No

Yes

Distributed shared memory

Thread block cluster

Tensor memory accelerator (TMA) unit

Feature support (unlisted features are supported for all compute capabilities)

1.0, 1.1

1.2, 1.3

2.x

3.0

3.2

3.5, 3.7, 5.x, 6.x, 7.0, 7.2

7.5

8.x

9.0, 10.x, 12.x

Compute capability (version)

### Data types

#### Floating-point types

| Data type | Supported vector types | Bits | Comments |   |   |   |   |
|---|---|---|---|---|---|---|---|
| Storage Length (complete vector) | Used Length (single value) | Sign | Exponent | Mantissa |   |   |   |
| E2M1 = FP4 | e2m1x2 / e2m1x4 | 8 / 16 | 4 | 1 | 2 | 1 |   |
| E2M3 = FP6 variant | e2m3x2 / e2m3x4 | 16 / 32 | 6 | 1 | 2 | 3 |   |
| E3M2 = FP6 variant | e3m2x2 / e3m2x4 | 16 / 32 | 6 | 1 | 3 | 2 |   |
| UE4M3 | ue4m3 | 8 | 7 | 0 | 4 | 3 | Used for scaling (E2M1 only) |
| E4M3 = FP8 variant | e4m3 / e4m3x2 / e4m3x4 | 8 / 16 / 32 | 8 | 1 | 4 | 3 |   |
| E5M2 = FP8 variant | e5m2 / e5m2x2 / e5m2x4 | 8 / 16 / 32 | 8 | 1 | 5 | 2 | Exponent/range of FP16, fits into 8 bits |
| UE8M0 | ue8m0x2 | 16 | 8 | 0 | 8 | 0 | Used for scaling (any FP4 or FP6 or FP8 format) |
| FP16 | f16 / f16x2 | 16 / 32 | 16 | 1 | 5 | 10 |   |
| BF16 | bf16 / bf16x2 | 16 / 32 | 16 | 1 | 8 | 7 | Exponent/range of FP32, fits into 16 bits |
| TF32 | tf32 | 32 | 19 | 1 | 8 | 10 | Exponent/range of FP32, mantissa/precision of FP16 |
| FP32 | f32 / f32x2 | 32 / 64 | 32 | 1 | 8 | 23 |   |
| FP64 | f64 | 64 | 64 | 1 | 11 | 52 |   |

#### Version support

| Data type | Basic Operations | Supported since | Atomic Operations | Supported since for global memory | Supported since for shared memory |
|---|---|---|---|---|---|
| 8-bit integer signed/unsigned | loading, storing, conversion | 1.0 | —N/a | —N/a |   |
| 16-bit integer signed/unsigned | general operations | 1.0 | atomicCAS() | 3.5 |   |
| 32-bit integer signed/unsigned | general operations | 1.0 | atomic functions | 1.1 | 1.2 |
| 64-bit integer signed/unsigned | general operations | 1.0 | atomic functions | 1.2 | 2.0 |
| any 128-bit trivially copyable type | general operations | No | atomicExch, atomicCAS | 9.0 |   |
| 16-bit floating point FP16 | addition, subtraction, multiplication, comparison, warp shuffle functions, conversion | 5.3 | half2 atomic addition | 6.0 |   |
| atomic addition | 7.0 |   |   |   |   |
| 16-bit floating point BF16 | addition, subtraction, multiplication, comparison, warp shuffle functions, conversion | 8.0 | atomic addition | 8.0 |   |
| 32-bit floating point | general operations | 1.0 | atomicExch() | 1.1 | 1.2 |
| atomic addition | 2.0 |   |   |   |   |
| 32-bit floating point float2 and float4 | general operations | No | atomic addition | 9.0 |   |
| 64-bit floating point | general operations | 1.3 | atomic addition | 6.0 |   |

Note: Any missing lines or empty entries do reflect some lack of information on that exact item.

### Tensor cores

FMA per cycle per tensor core

Supported since

7.0

7.2

7.5 Workstation

7.5 Desktop

8.0

8.6 Workstation

8.7

8.6 Desktop

8.9 Desktop

8.9 Workstation

9.0

10.0

10.1

12.0

Data Type

For dense matrices

For sparse matrices

1st Gen (8x/SM)

1st Gen? (8x/SM)

2nd Gen (8x/SM)

3rd Gen (4x/SM)

4th Gen (4x/SM)

5th Gen (4x/SM)

1-bit values (AND)

8.0 as

experimental

No

No

4096

2048

8192

No

1-bit values (XOR)

7.5–8.9 as

experimental

No

1024

No

4-bit integers

8.0–8.9 as

experimental

256

1024

512

legacy mma.sync

No

4-bit floating point FP4 (E2M1)

10.0

No

4096

tbd

512

6-bit floating point FP6 (E3M2 and E2M3)

10.0

No

2048

tbd

8-bit integers

7.2

8.0

No

128

128

512

256

1024

2048

256

8-bit floating point FP8 (E4M3 and E5M2) with FP16 accumulate

8.9

No

256

8-bit floating point FP8 (E4M3 and E5M2) with FP32 accumulate

128

128

16-bit floating point FP16 with FP16 accumulate

7.0

8.0

64

64

64

256

128

512

1024

128

16-bit floating point FP16 with FP32 accumulate

32

64

128

64

16-bit floating point BF16 with FP32 accumulate

7.5

8.0

No

64

32-bit (19 bits used) floating point TF32

speed tbd (32?)

128

32

64

256

512

32

64-bit floating point

8.0

No

No

16

speed tbd

32

16

tbd

Note: Any missing lines or empty entries do reflect some lack of information on that exact item.

| Tensor Core Composition | 7.0 | 7.2, 7.5 | 8.0, 8.6 | 8.7 | 8.9 | 9.0 |
|---|---|---|---|---|---|---|
| Dot Product Unit Width in FP16 units (in bytes) | 4 (8) | 8 (16) | 4 (8) | 16 (32) |   |   |
| Dot Product Units per Tensor Core | 16 | 32 |   |   |   |   |
| Tensor Cores per SM partition | 2 | 1 |   |   |   |   |
| Full throughput (Bytes/cycle) per SM partition | 256 | 512 | 256 |   | 1024 |   |
| FP Tensor Cores: Minimum cycles for warp-wide matrix calculation | 8 | 4 | 8 |   |   |   |
| FP Tensor Cores: Minimum Matrix Shape for full throughput (Bytes) | 2048 |   |   |   |   |   |
| INT Tensor Cores: Minimum cycles for warp-wide matrix calculation | No | 4 |   |   |   |   |
| INT Tensor Cores: Minimum Matrix Shape for full throughput (Bytes) | No | 1024 | 2048 | 1024 |   |   |

| FP64 Tensor Core Composition | 8.0 | 8.6 | 8.7 | 8.9 | 9.0 |
|---|---|---|---|---|---|
| Dot Product Unit Width in FP64 units (in bytes) | 4 (32) | tbd |   | 4 (32) |   |
| Dot Product Units per Tensor Core | 4 | tbd |   | 8 |   |
| Tensor Cores per SM partition | 1 |   |   |   |   |
| Full throughput (Bytes/cycle) per SM partition | 128 | tbd |   | 256 |   |
| Minimum cycles for warp-wide matrix calculation | 16 | tbd |   |   |   |
| Minimum Matrix Shape for full throughput (Bytes) | 2048 |   |   |   |   |

### Technical specifications

Technical specifications

Compute capability (version)

1.0

1.1

1.2

1.3

2.x

3.0

3.2

3.5

3.7

5.0

5.2

5.3

6.0

6.1

6.2

7.0

7.2

7.5

8.0

8.6

8.7

8.9

9.0

10.x

12.x

Maximum number of resident grids per device

(concurrent kernel execution, can be lower for specific devices)

1

16

4

32

16

128

32

16

128

16

128

Maximum dimensionality of grid of thread blocks

2

3

Maximum x-dimension of a grid of thread blocks

65535

2

31

− 1

Maximum y-, or z-dimension of a grid of thread blocks

65535

Maximum dimensionality of thread block

3

Maximum x- or y-dimension of a block

512

1024

Maximum z-dimension of a block

64

Maximum number of threads per block

512

1024

Warp size

32

Maximum number of resident blocks per multiprocessor

8

16

32

16

32

16

24

32

Maximum number of resident warps per multiprocessor

24

32

48

64

32

64

48

64

48

Maximum number of resident threads per multiprocessor

768

1024

1536

2048

1024

2048

1536

2048

1536

Number of 32-bit regular registers per multiprocessor

8 K

16 K

32 K

64 K

128 K

64 K

Number of 32-bit uniform registers per multiprocessor

No

2 K

Maximum number of 32-bit registers per thread block

8 K

16 K

32 K

64 K

32 K

64 K

32 K

64 K

32 K

64 K

Maximum number of 32-bit regular registers per thread

124

63

255

Maximum number of 32-bit uniform registers per warp

No

63

Amount of shared memory per multiprocessor

(out of overall shared memory + L1 cache, where applicable)

16 KiB

16 / 48 KiB (of 64 KiB)

16 / 32 / 48 KiB (of 64 KiB)

80 / 96 / 112 KiB (of 128 KiB)

64 KiB

96 KiB

64 KiB

96 KiB

64 KiB

0 / 8 / 16 / 32 / 64 / 96 KiB (of 128 KiB)

32 / 64 KiB (of 96 KiB)

0 / 8 / 16 / 32 / 64 / 100 / 132 / 164 KiB (of 192 KiB)

0 / 8 / 16 / 32 / 64 / 100 KiB (of 128 KiB)

0 / 8 / 16 / 32 / 64 / 100 / 132 / 164 KiB (of 192 KiB)

0 / 8 / 16 / 32 / 64 / 100 KiB (of 128 KiB)

0 / 8 / 16 / 32 / 64 / 100 / 132 / 164 / 196 / 228 KiB (of 256 KiB)

0 / 8 / 16 / 32 / 64 / 100 KiB (of 128 KiB)

Maximum amount of shared memory per thread block

16 KiB

48 KiB

96 KiB

48 KiB

64 KiB

163 KiB

99 KiB

163 KiB

99 KiB

227 KiB

99 KiB

Number of shared memory banks

16

32

Amount of local memory per thread

16 KiB

512 KiB

Constant memory size accessible by CUDA C/C++

(1 bank, PTX can access 11 banks, SASS can access 18 banks)

64 KiB

Cache working set per multiprocessor for constant memory

8 KiB

4 KiB

8 KiB

Cache working set per multiprocessor for texture memory

16 KiB per TPC

24 KiB per TPC

12 KiB

12 – 48 KiB

24 KiB

48 KiB

32 KiB

24 KiB

48 KiB

24 KiB

32 – 128 KiB

32 – 64 KiB

28 – 192 KiB

28 – 128 KiB

28 – 192 KiB

28 – 128 KiB

28 – 256 KiB

Maximum width for 1D texture reference bound to a CUDA

array

8192

65536

131072

Maximum width for 1D texture reference bound to linear

memory

2

27

2

28

2

27

2

28

2

27

2

28

Maximum width and number of layers for a 1D layered

texture reference

8192 × 512

16384 × 2048

32768 x 2048

Maximum width and height for 2D texture reference bound

to a CUDA array

65536 × 32768

65536 × 65535

131072 x 65536

Maximum width and height for 2D texture reference bound

to a linear memory

65000 x 65000

65536 x 65536

131072 x 65000

Maximum width and height for 2D texture reference bound

to a CUDA array supporting texture gather

—

N/a

16384 x 16384

32768 x 32768

Maximum width, height, and number of layers for a 2D

layered texture reference

8192 × 8192 × 512

16384 × 16384 × 2048

32768 x 32768 x 2048

Maximum width, height and depth for a 3D texture

reference bound to linear memory or a CUDA array

2048

3

4096

3

16384

3

Maximum width (and height) for a cubemap texture reference

—

N/a

16384

32768

Maximum width (and height) and number of layers

for a cubemap layered texture reference

—

N/a

16384 × 2046

32768 × 2046

Maximum number of textures that can be bound to a

kernel

128

256

Maximum width for a 1D surface reference bound to a

CUDA array

Not

supported

65536

16384

32768

Maximum width and number of layers for a 1D layered

surface reference

65536 × 2048

16384 × 2048

32768 × 2048

Maximum width and height for a 2D surface reference

bound to a CUDA array

65536 × 32768

16384 × 65536

131072 × 65536

Maximum width, height, and number of layers for a 2D

layered surface reference

65536 × 32768 × 2048

16384 × 16384 × 2048

32768 × 32768 × 2048

Maximum width, height, and depth for a 3D surface

reference bound to a CUDA array

65536 × 32768 × 2048

4096 × 4096 × 4096

16384 × 16384 × 16384

Maximum width (and height) for a cubemap surface reference bound to a CUDA array

32768

16384

32768

Maximum width and number of layers for a cubemap

layered surface reference

32768 × 2046

16384 × 2046

32768 × 2046

Maximum number of surfaces that can be bound to a

kernel

8

16

32

Maximum number of instructions per kernel

2 million

512 million

Maximum number of Thread Blocks per Thread Block Cluster

No

16

8

Technical specifications

1.0

1.1

1.2

1.3

2.x

3.0

3.2

3.5

3.7

5.0

5.2

5.3

6.0

6.1

6.2

7.0

7.2

7.5

8.0

8.6

8.7

8.9

9.0

10.x

12.x

Compute capability (version)

### Multiprocessor architecture

Architecture specifications

Compute capability (version)

1.0

1.1

1.2

1.3

2.0

2.1

3.0

3.2

3.5

3.7

5.0

5.2

5.3

6.0

6.1

6.2

7.0

7.2

7.5

8.0

8.6

8.7

8.9

9.0

10.x

12.x

Number of ALU lanes for INT32 arithmetic operations

8

32

48

192

128

128

64

128

128

64

64

64

128

Number of ALU lanes for any INT32 or FP32 arithmetic operation

—

N/a

—

N/a

Number of ALU lanes for FP32 arithmetic operations

64

64

128

128

Number of ALU lanes for FP16x2 arithmetic operations

No

1

128

128

64

Number of ALU lanes for FP64 arithmetic operations

No

1

16 by FP32

4 by FP32

8

8 / 64

64

4

32

4

32

2

32

2

64

2

Number of Load/Store Units

4 per 2 SM

8 per 2 SM

8 per 2 SM / 3 SM

8 per 3 SM

16

32

16

32

16

32

Number of special function units for single-precision floating-point transcendental functions

2

4

8

32

16

32

16

Number of texture mapping units (TMU)

4 per 2 SM

8 per 2 SM

8 per 2 / 3SM

8 per 3 SM

4

4 / 8

16

8

16

8

4

Number of ALU lanes for uniform INT32 arithmetic operations

No

2

Number of tensor cores

No

8 (1st gen.)

0 / 8

(2nd gen.)

4 (3rd gen.)

4 (4th gen.)

Number of raytracing cores

No

0 / 1

(1st gen.)

No

1 (2nd gen.)

No

1 (3rd gen.)

No

Number of SM Partitions = Processing Blocks

1

4

2

4

Number of warp schedulers per SM partition

1

2

4

1

Max number of new instructions issued each cycle by a single scheduler

2

1

2

2

1

Size of unified memory for data cache and shared memory

16 KiB

16 KiB

64 KiB

128 KiB

64 KiB SM + 24 KiB L1 (separate)

96 KiB SM + 24 KiB L1 (separate)

64 KiB SM + 24 KiB L1 (separate)

64 KiB SM + 24 KiB L1 (separate)

96 KiB SM + 24 KiB L1 (separate)

64 KiB SM + 24 KiB L1 (separate)

128 KiB

96 KiB

192 KiB

128 KiB

192 KiB

128 KiB

256 KiB

Size of L3 instruction cache per GPU

32 KiB

use L2 Data Cache

Size of L2 instruction cache per Texture Processor Cluster (TPC)

8 KiB

Size of L1.5 instruction cache per SM

4 KiB

32 KiB

32 KiB

48 KiB

128 KiB

32 KiB

128 KiB

~46 KiB

128 KiB

Size of L1 instruction cache per SM

8 KiB

8 KiB

Size of L0 instruction cache per SM partition

only 1 partition per SM

No

12 KiB

16 KiB?

32 KiB

Instruction Width

32 bits instructions and 64 bits instructions

64 bits instructions + 64 bits control logic every 7 instructions

64 bits instructions + 64 bits control logic every 3 instructions

128 bits combined instruction and control logic

Memory Bus Width per Memory Controller in bits

64 ((G)DDR)

32 ((G)DDR)

512 (HBM)

32 ((G)DDR)

512 (HBM)

32 ((G)DDR)

512 (HBM)

32 ((G)DDR)

512 (HBM)

32 ((G)DDR)

L2 Cache per Memory Controller

16 KiB

32 KiB

128 KiB

256 KiB

1 MiB

512 KiB

128 KiB

512 KiB

256 KiB

128 KiB

768 KiB

64 KiB

512 KiB

4 MiB

512 KiB

8 MiB

5 MiB

6.25 MiB

8 MiB

Number of Render Output Units (ROP) per memory controller (or per GPC in later models)

4

8

4

8

16

8

12

8

4

16

2

8

16

16 per GPC

3 per GPC

16 per GPC

Architecture specifications

1.0

1.1

1.2

1.3

2.0

2.1

3.0

3.2

3.5

3.7

5.0

5.2

5.3

6.0

6.1

6.2

7.0

7.2

7.5

8.0

8.6

8.7

8.9

9.0

10.x

12.x

Compute capability (version)

For more information read the Nvidia CUDA C++ Programming Guide.

## Usages of CUDA architecture

- Accelerated rendering of 3D graphics
- Accelerated interconversion of video file formats
- Accelerated encryption, decryption and compression
- Bioinformatics, e.g. NGS DNA sequencing BarraCUDA
- Distributed calculations, such as predicting the native conformation of proteins
- Medical analysis simulations, for example virtual reality based on CT and MRI scan images
- Physical simulations, particularly in fluid dynamics
- Neural network training in machine learning problems
- Large Language Model inference
- Face recognition
- Volunteer computing projects, such as SETI@home and other projects using BOINC software
- Molecular dynamics
- Mining cryptocurrencies
- Structure from motion (SfM) software

## Comparison with competitors

CUDA competes with other GPU computing stacks: Intel OneAPI and AMD ROCm.

Whereas Nvidia's CUDA is closed-source, Intel's OneAPI and AMD's ROCm are open source.

### Intel OneAPI

**oneAPI** is an initiative based in open standards, created to support software development for multiple hardware architectures. The oneAPI libraries must implement open specifications that are discussed publicly by the Special Interest Groups, offering the possibility for any developer or organization to implement their own versions of oneAPI libraries.

Originally made by Intel, other hardware adopters include Fujitsu and Huawei.

#### Unified Acceleration Foundation (UXL)

Unified Acceleration Foundation (UXL) is a new technology consortium working on the continuation of the OneAPI initiative, with the goal to create a new open standard accelerator software ecosystem, related open standards and specification projects through Working Groups and Special Interest Groups (SIGs). The goal is to offer open alternatives to Nvidia's CUDA. The main companies behind it are Intel, Google, ARM, Qualcomm, Samsung, Imagination, and VMware.

### AMD ROCm

**ROCm** is an open source software stack for graphics processing unit (GPU) programming from Advanced Micro Devices (AMD).
