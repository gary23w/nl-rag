---
title: "MLIR (software)"
source: https://en.wikipedia.org/wiki/MLIR_(software)
domain: mlir-compiler
license: CC-BY-SA-4.0
tags: mlir compiler, intermediate representation, compiler optimization, domain specific dialect
fetched: 2026-07-02
---

# MLIR (software)

**MLIR** (**Multi-Level Intermediate Representation**) is an open-source compiler infrastructure project developed as a sub-project of the LLVM project. It provides a modular and extensible intermediate representation (IR) framework intended to facilitate the construction of domain-specific compilers and improve compilation for heterogeneous computing platforms. MLIR supports multiple abstraction levels in a single IR and introduces dialects, a mechanism for defining custom operations, types, and attributes tailored to specific domains. The name "Multi-Level Intermediate Representation" reflects the system’s ability to model computations at various abstraction levels and progressively lower them toward machine code.

MLIR was originally developed in 2018 by Chris Lattner at Google, and publicly released as part of LLVM in 2019. It was designed to address challenges in building compilers for modern workloads such as machine learning, hardware acceleration, and high-level synthesis by providing reusable components and standardizing the representation of intermediate computations across different programming languages and hardware targets.

MLIR is used in a range of systems including TensorFlow, Mojo, TPU-MLIR, and others. It is released under the Apache License 2.0 with LLVM exceptions and is maintained as part of the LLVM project.

## History

Work on MLIR began in 2018, led by Chris Lattner at Google in collaboration with Mehdi Amini, River Riddle, and others, as a response to the growing complexity of modern compiler toolchains. The project aimed to improve the modularity, composability, and maintainability of compiler infrastructures, particularly in domains such as machine learning, high-level synthesis, and hardware acceleration. It was formally introduced at the 2019 LLVM Developer Meeting and was open-sourced later that year as part of the LLVM monorepository.

MLIR’s architecture was shaped by prior experiences building compilers such as XLA and LLVM, where limitations in existing intermediate representations hindered optimization and reuse across abstraction levels. To address this, MLIR introduced a novel concept of multi-level IRs that could coexist in the same system and be gradually lowered through well-defined transformations. A foundational design feature was the use of dialects, allowing different domains and hardware targets to define custom operations and type systems while maintaining interoperability.

Since its release, MLIR has been adopted by multiple compiler ecosystems and research efforts. In TensorFlow, MLIR serves as the foundation for rewriting and lowering transformations in components such as XLA and TensorFlow Runtime. The language Mojo, developed by Modular Inc., relies on MLIR to achieve ahead-of-time compilation for artificial intelligence workloads. Additional projects that have built on MLIR include TPU-MLIR for compiling models to Tensor Processing Unit hardware, ONNX-MLIR for interoperable machine learning models, MLIR-AIE for targeting Xilinx AI Engines, IREE for compiling and executing machine learning models across CPUs, GPUs, and accelerators, DSP-MLIR, a compiler infrastructure tailored for digital signal processing (DSP) applications, and torch-mlir, which brings MLIR-based compilation capabilities to the PyTorch ecosystem.

MLIR continues to evolve as part of the LLVM Project and follows the project's release schedule and development policies. It is developed collaboratively by contributors from industry, academia, and the broader open-source community.

## Dialects

In MLIR, a **dialect** defines a self-contained namespace of operations, types, attributes, and other constructs. Dialects are the primary mechanism for extensibility, allowing developers to introduce domain-specific abstractions while maintaining compatibility within the broader MLIR framework. Each operation within a dialect is identified by a unique name and may include optional operands, results, attributes, and regions. Operands and results follow the static single-assignment form (SSA), and each result is associated with a type. Attributes represent compile-time metadata, such as constant values. Regions consist of ordered blocks, each of which may take input arguments and contain a sequence of nested operations. While MLIR is designed around SSA, it avoids traditional PHI nodes by using block arguments in conjunction with the operands of control-flow operations to model value merging.

The general syntax for an operation is the following:

```mw
%res:2 = "mydialect.morph"(%input#3) ({
            ^bb0(%arg0: !mydialect<"custom_type"> loc("mysource.cc":10:8)):
                // nested operations
         }) { some.attribute = true, other_attribute = 1.5 }
         : (!mydialect<"custom_type">) -> (!mydialect<"other_type">, !mydialect<"other_type">)
         loc(callsite("foo" at "mysource.cc":10:8))
```

This operation, named `morph`, belongs to the `mydialect` dialect. It takes one input operand (`%input#3`) of type `custom_type` and produces two output values of type `other_type`. The operation includes two attributes-`some.attribute` and `other_attribute`-and contains a region with a single block (`^bb0`) that accepts one argument. The `loc` keyword specifies source-level location information, which can be used for debugging or diagnostic reporting.

The syntax of operations, types and attributes can also be customized according to the user preferences by implementing proper parsing and printing functions within the operation definition.

### Core dialects

The MLIR dialects ecosystem is open and extensible, allowing end-users to define new dialects that capture the semantics of specific computational domains. At the same time, the MLIR codebase provides a variety of built-in dialects that address common patterns found in intermediate representations. These core dialects are designed to be self-contained and interoperable, making them suitable for reuse across different compiler stacks.

For example, the `arith` dialect includes basic mathematical operations over integers and floating-point types, while the `memref` dialect provides operations for memory allocation and access. Control-flow abstractions are handled by dialects such as `affine`, which supports affine loop nests suitable for polyhedral optimization, and `scf`, which provides structured control flow using constructs like `for`, `if`, and `while`. The `func` dialect supports function definitions and calls, while the `gpu` dialect introduces primitives for GPU programming models. Additionally, the `tosa` dialect defines a portable and quantization-friendly operator set for machine learning inference. Finally, the `llvm` dialect provides a one-to-one mapping to LLVM IR, enabling seamless lowering to LLVM’s backend and reuse of its optimization and code generation infrastructure.

The following code defines a function that takes two floating point matrices and performs the sum between the values at the same positions:

```mw
func.func @matrix_add(%arg0: memref<10x20xf32>, %arg1: memref<10x20xf32>) -> memref<10x20xf32> {
    %result = memref.alloc() : memref<10x20xf32>

	affine.for %i = 0 to 10 {
		affine.for %j = 0 to 20 {
			%lhs = memref.load %arg0[%i, %j] : memref<10x20xf32>
			%rhs = memref.load %arg1[%i, %j] : memref<10x20xf32>
			%sum = arith.addf %lhs, %rhs : f32
			memref.store %sum, %result[%i, %j] : memref<10x20xf32>
		}
	}
    
    func.return %result : memref<10x20xf32>
}
```

Although different dialects may be used to express similar computations, the level of abstraction and the intended compilation flow may vary. In the example above, the `affine` dialect enables polyhedral analysis and optimizations, while the `memref` and `arith` dialects express memory and arithmetic operations, respectively.

## Operation definition specification

The operations of a dialect can be defined using the C++ language, but also in a more convenient and robust way by using the Operation definition specification (ODS). By using TableGen, the C++ code for declarations and definitions can be then automatically generated.

The autogenerated code can include parsing and printing methods – which are based on a simple string mapping the structure of desired textual representation – together with all the boilerplate code for accessing fields and perform common actions such verification of the semantics of each operation, canonicalization or folding.

The same declaration mechanism can be used also for types and attributes, which are the other two categories of elements constituting a dialect.

The following example illustrates how to specify the *assembly format* of an operation expecting a variadic number of operands and producing zero results. The textual representation consists in the optional list of attributes, followed by the optional list of operands, a colon, and types of the operands.

```mw
let assemblyFormat = "attr-dict ($operands^ `:` type($operands))?";
```

## Transformations

Transformations can always be performed directly on the IR, without having to rely on built-in coordination mechanisms. However, in order to ease both implementation and maintenance, MLIR provides an infrastructure for IR rewriting that is composed by different rewrite drivers. Each driver receives a set of objects named *patterns*, each of which has its own internal logic to match operations with certain properties. When an operation is matched, the rewrite process is performed and the IR is modified according to the logic within the pattern.

### Dialect conversion driver

This driver operates according to the *legality* of existing operations, meaning that the driver receives a set of rules determining which operations have to be considered *illegal* and expects the patterns to match and convert them into *legal* ones. The logic behind those rules can be arbitrarily complex: it may be based just on the dialect to which the operations belong, but can also inspect more specific properties such as attributes or nested operations.

As the names suggests, this driver is typically used for converting the operations of a dialect into operations belonging to a different one. In this scenario, the whole source dialect would be marked as illegal, the destination one as legal, and patterns for the source dialect operations would be provided. The dialect conversion framework also provides support for type conversion, which has to be performed on operands and results to convert them to the type system of the destination dialect.

MLIR allows for multiple conversion paths to be taken. Considering the example about the sum of matrices, a possible lowering strategy may be to generate for-loops belonging to the *scf* dialect, obtaining code to be executed on CPUs:

```mw
#map = affine_map<(d0, d1) -> (d0, d1)>

module {
    func.func @avg(%arg0: memref<10x20xf32>, %arg1: memref<10x20xf32>) -> memref<10x20xf32> {
        %alloc = memref.alloc() : memref<10x20xf32>
        %c0 = arith.constant 0 : index
        %c10 = arith.constant 10 : index
        %c1 = arith.constant 1 : index
        
        scf.for %arg2 = %c0 to %c10 step %c1 {
            %c0_0 = arith.constant 0 : index
            %c20 = arith.constant 20 : index
            %c1_1 = arith.constant 1 : index
            
            scf.for %arg3 = %c0_0 to %c20 step %c1_1 {
                %0 = memref.load %arg0[%arg2, %arg3] : memref<10x20xf32>
                %1 = memref.load %arg1[%arg2, %arg3] : memref<10x20xf32>
                %2 = arith.addf %0, %1 : f32
                memref.store %2, %alloc[%arg2, %arg3] : memref<10x20xf32>
            }
        }
        
        return %alloc : memref<10x20xf32>
    }
}
```

Another possible strategy, however, could have been to use the *gpu* dialect to generate code for GPUs:

```mw
#map = affine_map<(d0, d1) -> (d0, d1)>

module {
    func.func @avg(%arg0: memref<10x20xf32>, %arg1: memref<10x20xf32>) -> memref<10x20xf32> {
        %alloc = memref.alloc() : memref<10x20xf32>
        %c0 = arith.constant 0 : index
        %c10 = arith.constant 10 : index
        %0 = arith.subi %c10, %c0 : index
        %c1 = arith.constant 1 : index
        %c0_0 = arith.constant 0 : index
        %c20 = arith.constant 20 : index
        %1 = arith.subi %c20, %c0_0 : index
        %c1_1 = arith.constant 1 : index
        %c1_2 = arith.constant 1 : index
        
        gpu.launch blocks(%arg2, %arg3, %arg4) in (%arg8 = %0, %arg9 = %c1_2, %arg10 = %c1_2) threads(%arg5, %arg6, %arg7) in (%arg11 = %1, %arg12 = %c1_2, %arg13 = %c1_2) {
            %2 = arith.addi %c0, %arg2 : index
            %3 = arith.addi %c0_0, %arg5 : index
            %4 = memref.load %arg0[%2, %3] : memref<10x20xf32>
            %5 = memref.load %arg1[%2, %3] : memref<10x20xf32>
            %6 = arith.addf %4, %5 : f32
            memref.store %4, %alloc[%2, %3] : memref<10x20xf32>
            gpu.terminator
        }
        
        return %alloc : memref<10x20xf32>
    }
}
```

### Greedy pattern rewrite driver

The driver greedily applies the provided patterns according to their benefit, until a fixed point is reached or the maximum number of iterations is reached. The benefit of a pattern is self-attributed. In case of equalities, the relative order within the patterns list is used.

## Traits and interfaces

MLIR allows to apply existing optimizations (e.g., common subexpression elimination, loop-invariant code motion) on custom dialects by means of traits and interfaces. These two mechanisms enable transformation passes to operate on operations without knowing their actual implementation, relying only on some properties that traits or interfaces provide.

Traits are meant to be attached to operations without requiring any additional implementation. Their purpose is to indicate that the operation satisfies certain properties (e.g. having exactly two operands). Interfaces, instead, represent a more powerful tool through which the operation can be queried about some specific aspect, whose value may change between instances of the same kind of operation. An example of interface is the representation of memory effects: each operation that operates on memory may have such interface attached, but the actual effects may depend on the actual operands (e.g., a function call with arguments possibly being constants or references to memory).

## Applications

The freedom in modeling intermediate representations enables MLIR to be used in a wide range of scenarios. This includes traditional programming languages, but also high-level synthesis, quantum computing and homomorphic encryption. Machine learning applications also take advantage of built-in polyhedral compilation techniques, together with dialects targeting accelerators and other heterogeneous systems.

For specific compiler projects and toolchains built using MLIR, see the Ecosystem section below.

## Ecosystem

MLIR has fostered a growing ecosystem of open-source projects, production compilers, and experimental toolchains across multiple domains. These projects demonstrate MLIR’s flexibility in modeling, optimizing, and lowering computations for a diverse set of hardware targets.

**TensorFlow/XLA** integrates MLIR as a foundational component of its modern compiler infrastructure. MLIR is used to represent TensorFlow computation graphs in an extensible intermediate form, facilitating transformations such as fusion, quantization, and backend-specific lowering. Both the TensorFlow Runtime(TFRT) and the Accelerated Linear Algebra (XLA) compiler rely on MLIR to improve portability and performance across hardware platforms.

**IREE** (Intermediate Representation Execution Environment) is an end-to-end compiler and runtime system built entirely on MLIR. It compiles high-level machine learning models-such as those from TensorFlow and TensorFlow Lite into optimized, portable executables that can target a variety of hardware backends, including CPUs, GPUs, and dedicated accelerators. IREE supports both ahead-of-time (AOT) and just-in-time (JIT) compilation workflows, and serves as a demonstration of how MLIR can function as the intermediate representation for a complete compiler stack, encompassing frontend lowering, optimization, backend code generation, and runtime execution.

**torch-mlir** is a compiler project that integrates MLIR-based infrastructure into the PyTorch ecosystem. It introduces Torch and TorchCoversion dialects which model PyTorch-level abstractions, such as TorchScript and eager-mode semantics, and provides transformation passes to progressively lower these representations toward hardware-optimized targets. torch-mlir is designed to be a modular backend framework, enabling high-performance execution across diverse platforms, including CPUs, GPUs, and specialized accelerators.

**ONNX-MLIR** is a compiler framework built on MLIR that targets the ONNX ecosystem. It provides a conversion and optimization pipeline for ONNX models by translating them into MLIR using a series of dedicated dialects that represent ONNX operations and intermediate forms. ONNX-MLIR enables execution across a wide range of hardware platforms by leveraging MLIR’s extensible lowering infrastructure and backend integration. The project supports model import, shape inference, and code generation for multiple targets, and serves as a reference implementation of ONNX-to-MLIR compilation.

**MLIR-AIE** is a compiler framework developed by Xilinx for programming AI Engine (AIE) arrays found on Versal ACAP platforms. It extends MLIR with custom dialects and transformation passes tailored to the dataflow architecture and compilation constraints of AIE hardware. MLIR-AIE enables software developers to write high-level programs and compile them into optimized instruction sets suitable for deeply embedded, parallel, and statically scheduled workloads. The framework supports hardware-specific pipelines such as IRON and AIR for targeting AMD’s Ryzen AI and Versal-AIE platforms.

**Triton-MLIR** is a compiler infrastructure that brings MLIR based tooling to the Triton programming model, which is used to write highly efficient custom GPU kernels. It introduces MLIR dialects that represent Triton's core abstractions, including blocks, warps, and memory spaces, and integrates them with existing MLIR transformation pipelines. Triton-MLIR enables new paths for optimization, interoperability, and backend extensibility within the Triton ecosystem. It also forms part of Microsoft’s broader effort to unify Triton’s kernel representation under the MLIR compiler architecture.

**Mojo** is a systems programming language developed by Modular Inc. that integrates Python syntax with low-level performance characteristics. Mojo is built on MLIR and uses it as its core intermediate representation framework. The language defines custom dialects to support advanced compilation features such as static typing, memory layout control, metaprogramming, and hardware specialization. MLIR enables Mojo to seamlessly interoperate with other MLIR-based systems and to generate highly optimized code for a wide range of accelerators and heterogeneous platforms.
