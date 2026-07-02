---
title: "GraalVM"
source: https://en.wikipedia.org/wiki/GraalVM
domain: quarkus
license: CC-BY-SA-4.0
tags: quarkus framework, quarkus native, graalvm native, jakarta ee
fetched: 2026-07-02
---

# GraalVM

**GraalVM** is a Java Development Kit (JDK) written in Java. The open-source distribution of GraalVM is based on OpenJDK, and the enterprise distribution is based on Oracle JDK. Along with just-in-time (JIT) compilation, GraalVM can also compile a Java application ahead of time. This allows for faster initialization, greater runtime performance, and decreased resource consumption, but the resulting executable can only run on the platform it was compiled for.

It provides additional programming languages and execution modes. The first production-ready release, GraalVM 19.0, was distributed in May 2019. The most recent release is GraalVM for JDK 24.0.2, made available in July 2025.

**Major differentiators of GraalVM compared to the base JDK include:**

- *Graal Compiler*, a just-in-time (JIT) compiler.
- *GraalVM Native Image is* a technology to compile Java applications ahead of time.
- *Truffle Language Implementation Framework* and *GraalVM SDK,* a Java-based framework and a collection of APIs for developing high-performance language runtimes.
- *GraalVM Polyglot API*, an API to embed guest language code in a Java-based host application.
- *JavaScript Runtime,* an ECMAScript 2023-compliant JavaScript runtime, as well as Node.js.
- *LLVM Runtime is* a runtime to execute languages that can be transformed into LLVM bitcode.

## Goals

- To improve the performance of Java virtual machine (JVM)-based languages to match native languages.
- To reduce the startup time of JVM-based applications by compiling them ahead of time.
- To enable GraalVM integration into the Oracle Database, OpenJDK, Android/iOS, and similar custom embeddings.
- To enable embedding guest language code in a JVM-based host application.
- To enable mixing of code from any programming language in a single application, billed as a "polyglot application."

## History

GraalVM has its roots in the Maxine Virtual Machine project at Sun Microsystems Laboratories (now Oracle Labs). The project's goal was to write a Java virtual machine in Java itself to avoid the problems of developing in C++, particularly manual memory management, and benefit from meta-circular optimizations. The project changed its focus to the compiler and to hook it into the HotSpot runtime as much as possible. The GraalVM compiler, Graal, was started by manually converting the code of the HotSpot client compiler (named "C1") into Java, replacing the previous Maxine compiler.

Graal was included in HotSpot-based JDK releases such as OpenJDK from Java SE 9 through 15, to provide experimental ahead-of-time compilation. The UseJVMCICompiler option also enabled the use of Graal as a replacement for the server compiler (named "C2"). The option was removed in Java SE 16 to eliminate the duplicate effort of maintaining a version in the JDK and a standalone GraalVM release. A similar function to create a native executable from a Java application is provided by the `native-image` tool of standalone GraalVM releases. The tool processes a Java application's classes and other metadata to create a binary for a specific operating system and architecture. It can be used to build a native executable or a native shared library.

## Releases

GraalVM is available as Oracle GraalVM under the GraalVM Free Terms and Conditions (GFTC) license, as Oracle GraalVM Enterprise Edition accessible by accepting the "OTN License Agreement Oracle GraalVM Enterprise Edition Including License for Early Adopter Versions", or as a Community Edition with an open-source license. Oracle Corporation announced the release of *Oracle GraalVM Enterprise Edition* on May 8, 2019, and *Oracle GraalVM* on June 13, 2023, introducing a new GraalVM Free Terms and Conditions (GFTC) license. GraalVM can substitute for a default JDK on Linux and macOS platforms on x64 and AArch64 CPUs, and on a Windows x64 platform. The release schedule is at the Oracle Help Center and the GraalVM website.

| Release | Date | Java Version | Features |
|---|---|---|---|
| GraalVM 19.0.0 | 2019-05-09 | OpenJDK 1.8.0_212 | The first production release for Linux and macOS x64 platforms. Windows availability was under development and released as early adopter functionality. |
| GraalVM 19.1.0 | 2019-07-02 | OpenJDK 1.8.0_212 | Introduced `libgraal`, a shared library produced by GraalVM Native Image, which contained a pre-compiled binary of the Graal compiler that dramatically improved compilation speed. The release also improved profile-guided optimization (PGO) implementation for Native Image. |
| GraalVM 19.2.0 | 2019-08-20 | OpenJDK 1.8.0_222 | This release added preliminary functionality to compile native applications using the LLVM toolchain, shipped with GraalVM. GraalVM Native Image improved throughput performance and simplified the process of collecting data for profile-guided optimizations (PGO). Custom polyglot access was implemented in the polyglot runtime to control access for polyglot bindings and data sharing between languages. A preview of Java Flight Recorder (JFR) functionality was released as a plugin for VisualVM. |
| GraalVM 19.3.0 | 2019-11-19 | Oracle JDK 1.8.0_231, 11.0.5 OpenJDK 1.8.0_232,11.0.5 | This release announced the first GraalVM Java SE 11-based builds; added new platforms — Linux AArch64 and experimental Windows x64. This release also added module encapsulation to isolate Graal compiler and Truffle API code from the application code. GraalVM Native Image switched to using the JDK native code instead of manual substitutions. The Native Image Maven Plugin was first introduced. GraalVM Enterprise 19.3.0 was the first planned long-term support (LTS) release. |
| GraalVM 20.0.0 | 2020-02-18 | Oracle JDK 1.8.0_241, 11.0.6 OpenJDK 1.8.0_242, 11.0.6 | Improved Windows compatibility; included enhanced Native Image technology, and improved tooling, as well as many changes in the compiler and hosted languages. |
| GraalVM 20.1.0 | 2020-05-19 | Oracle JDK 1.8.0_251, 11.0.7 OpenJDK 1.8.0_252, 11.0.7 | Included several improvements for many of the components. In addition to performance improvements, usability fixes for Native Image were published. The JavaScript engine implemented all ECMAScript 2020 mode features by default. The regular expression engine (*TRegex*) used by JavaScript and Python implemented all expressions. Ruby (*TruffleRuby*) was improved in compatibility with native gems. |
| GraalVM 20.2.0 | 2020-08-18 | Oracle JDK 8u261, 11.0.8 OpenJDK 1.8.0_262, 11.0.8 | This release introduced a new Partial Loop Unrolling optimization for JIT compilation. Improved the G1GC-like garbage collection for workloads where Native Image requires smaller GC pauses. Native Image was extended to generate “mostly static” executables which statically link everything except `libc.` |
| GraalVM 20.3.0 | 2020-11-17 | Oracle JDK 1.8.0_271, 11.0.9 OpenJDK 1.8.0_272, 11.0.9 | The first LTS Enterprise version of Oracle GraalVM Enterprise Edition and the final release for 2020. This release provided code sharing in the GraalVM LLVM runtime, enabling sharing of abstract syntax tree (AST) and compiled code of common bitcode libraries between multiple contexts within a single engine. An experimental "sandbox resource limits" feature was added to Oracle GraalVM Enterprise Edition. |
| GraalVM 21.0.0 | 2021-01-19 | Oracle JDK 1.8.0_281,11.0.10 OpenJDK 1.8.0_282,11.0.10 | This release introduced Java on Truffle — a Java virtual machine implementation based on a Truffle interpreter. GraalVM Native Image added serialization functionality, AWT and Swing implementations for the Linux platform. The GraalVM Updater was improved to enable updating/upgrading a local GraalVM installation. |
| GraalVM 21.1.0 | 2021-04-20 | Oracle JDK 1.8.0_291, 11.0.11, 16.0.1 OpenJDK 1.8.0_292, 11.0.11, 16.0.1 | This release added Java 16 (experimental) functionality and improved Linux AArch64 compatibility. GraalVM Native Image enabled reporting on the build to produce multiple artifacts, and improved compatibility with Windows. Multi-tier compilation was enabled by default for the polyglot runtime (first introduced in GraalVM 20.3); a new sandbox option `--sandbox.MaxHeapMemory=<size>` to specify the maximum heap memory was introduced. |
| GraalVM 21.2.0 | 2021-07-20 | Oracle JDK 1.8.0_301, 11.0.12, 16.0.2 OpenJDK 1.8.0_302, 11.0.12, 16.0.2 | In this release, the GraalVM team added a novel SIMD (Single Instruction Multiple Data) vectorization optimization for sequential code, and a Strip Mining optimization for non-counted loops for the Graal compiler. It also included new official Gradle and Maven plugins for GraalVM Native Image with initial JUnit 5 testing functionality and added basic Java Flight Recorder (JFR) functionality on Java SE 11 in GraalVM Native Image, and the “epsilon” GC to build an executable without a garbage collector. Java on Truffle introduced a HotSwap Plugin API to reload code without restarting a running application. |
| GraalVM 21.3.0 | 2021-10-19 | Oracle JDK 1.8.0_311, 11.0.13, 17.0.1 OpenJDK 1.8.0_312, 11.0.13, 17.0.1 | The GraalVM distributions for Java SE 17 became available for download. The release added a new Infeasible Path Correlation optimization to eliminate infeasible paths, provided an implementation for Constant Blinding to defend against JIT spraying attacks. GraalVM Native Image improved gathering the reflection metadata distinguishing between queried and invoked reflection methods, added the initial compatibility for the Java Platform Module System, and several new optimizations to reduce the size of the executable and its build time. |
| GraalVM 22.0.0 | 2022-01-18 | Oracle JDK 11.0.14, 17.0.2 OpenJDK 11.0.14, 17.0.2 | As of this release, GraalVM dropped support for Java SE 8, and removed support for Java SE 12, 13, 14, 15, and 16. This release brought new user-friendly build output for GraalVM Native Image with progress bars and more summary information; improved compatibility with the Java Platform Module System (the options `--add-reads` and `--add-modules`appeared); and a new loop rotation optimization for the Graal compiler that converts more non-counted loops to counted loops. |
| GraalVM 22.1.0 | 2022-04-19 | Oracle JDK 11.0.15, 17.0.3 OpenJDK 11.0.15, 17.0.3 | This release introduced a preview build for Apple Silicon, `darwin-aarch64`. GraalVM Native Image added a new mode to create conditional configuration using the Tracing agent, and a new “quick build” mode, `-Ob`, to reduce the time to produce development builds. The Truffle framework introduced `TruffleStrings`— an implementation of a String type shared between Truffle languages. |
| GraalVM 22.2.0 | 2022-07-19 | Oracle JDK 11.0.16, 17.0.4 OpenJDK 11.0.16, 17.0.4 | This release featured a smaller JDK size, improved memory usage, and better library compatibility. The Oracle GraalVM team together with the Spring, Micronaut, and Quarkus teams introduced the GraalVM Reachability Metadata Repository, a centralized place providing configuration for libraries which did not support GraalVM Native Image. GraalVM Native Image also implemented a Software Bill of Materials (SBOM), and started to run on the module path by default. JavaScript, LLVM runtimes, and VisualVM were decoupled from the main package and provided as installable components. |
| GraalVM 22.3.0 | 2022-10-18 | Oracle JDK 11.0.17, 17.0.5, 19.0.1 OpenJDK 11.0.17, 17.0.5, 19.0.1 | This was the last release to support Java SE 11, and the last Feature release of the year. GraalVM Enterprise 22.3.0 would be supported for the next 18 months, and GraalVM Community for 12 months. This version provided Java SE 19 builds, enabling users to take advantage of the latest Java SE 18 and Java SE 19 features. GraalVM Native Image implemented OpenJDK Project Loom Virtual Threads (JEP 425); a `jlink` implementation; and provided multiple new monitoring features. The GraalPython project was renamed to GraalPy, and its launcher from `graalpython` to `graalpy`. |
| GraalVM for JDK 17 | 2023-06-13 | Oracle JDK 17.0.7 OpenJDK 17.0.7 | This release introduced a new distribution: **Oracle GraalVM**, under the new GraalVM Free Terms and Conditions license. Along with performance improvements, an implementation for the ZGC garbage collector. GraalVM Native Image introduced the Native Image Bundles feature and added Machine Learning (ML) based profile inference — a pre-trained machine learning model to predict the control flow of graph branches. Also, as of this release, GraalVM Native Image set build environments on Windows automatically (it was no longer a requirement to run the x64 Native Tools Command Prompt). |
| GraalVM for JDK 20 | 2023-06-13 | Oracle JDK 20.0.1 OpenJDK 20.0.1 |   |
| GraalVM for JDK 21 | 2023-09-19 | Oracle JDK 21 OpenJDK 21 | This release brought all Java SE 21 features to GraalVM such as virtual threads from Project Loom. Performance improvements in this release made ahead-of-time compiled Java applications run at peak performance as on HotSpot. This release enabled the Garbage First Garbage Collector (G1 GC) on Linux AArch64 (in addition to Linux x64) in GraalVM Native Image. The GraalVM SDK was refactored and split into four modules. Languages runtimes were "unchained" from the GraalVM JDK and became available as Java libraries at Maven Central. Oracle GraalVM for JDK 21 became the current long-term support (LTS) release. |
| GraalVM for JDK 22 | 2023-03-19 | Oracle JDK 22 OpenJDK 22 |   |
| GraalVM for JDK 23 | 2024-09-17 | Oracle JDK 23 OpenJDK 23 |   |
| GraalVM for JDK 24 | 2025-03-18 | Oracle JDK 24 OpenJDK 24 |   |
| GraalVM 25 | 2025-09-16 | Oracle JDK 25 OpenJDK 25 |   |

## Components

The GraalVM compiler, Graal, is shipped with the components of a normal Java virtual machine (OpenJDK). Additional components are included in GraalVM to enable new execution modes (*GraalVM Native Image*) or programming languages (*LLVM runtime*, *GraalVM JavaScript* as a potential replacement to the deprecated Nashorn engine, *TRegex* as a regular expression engine).

### Compiler

The GraalVM compiler, Graal, is a modern Java (JIT) compiler. It complements or replaces the existing compilers (C1/C2 in HotSpot). In contrast to those existing compilers, Graal is written in a modular, maintainable and extendable fashion in Java itself. It is released under GPL version 2 with the classpath exception.

### Native Image

GraalVM Native Image is an ahead-of-time compilation technology that produces executable binaries of class files. It is released as an early adopter technology, which means it is production-ready but may include backport incompatible updates in future releases.

This functionality supports JVM-,based languages, but can optionally run dynamic languages, developed on top of GraalVM with the Truffle framework. The executable file does not run on a JVM and uses necessary runtime components such as thread scheduling or GC from a minimal bespoke virtual machine called Substrate VM. Since the resulting native binary includes application classes, JDK dependencies and libraries already, the startup and execution time are reduced significantly.

GraalVM Native Image is officially supported by the Fn, Gluon, Helidon, Micronaut, Picocli, Quarkus, Vert.x and Spring Boot Java frameworks.

In September 2016, Oracle detailed plans to add ahead-of-time compilation to the OpenJDK using the GraalVM compiler for Java SE 9. This proposal, tracked by JEP 295: Ahead-of-Time Compilation, was included in Java SE 9. The experimental use of GraalVM as a just-in-time compiler was added for the Linux x64 platform for Java SE 10.

In Java SE versions 9 to 15, the `jaotc` command creates an executable. The experimental `-XX:+EnableJVMCIProduct` flag enables the use of Graal JIT compiler. The functionality is since available in the Native Image component of standalone GraalVM releases.

### Truffle Language Implementation Framework

In association with GraalVM, Oracle Labs developed an abstract syntax tree (AST) interpreter called "Truffle" that enables it to implement languages on top of GraalVM. Many languages have been implemented in Truffle, including an experimental C interpreter claiming to be about as fast as GCC and Clang.

The Truffle framework and its dependent part, GraalVM SDK, are released under the Universal Permissive License, version 1.0, to encourage the use of the framework for projects that do not want to be bound by the copyright or other parent rights.

### Instrumentation-Based Tool Support

A major advantage of the GraalVM ecosystem is language-agnostic, fully dynamic instrumentation support directly built into the VM runtime. Execution events can be captured by API clients with overhead that is extremely low in fully optimized code.

The core GraalVM installation provides a language-agnostic debugger, profiler, heap viewer, and others based on instrumentation and other VM support. GraalVM also includes a backend implementation of the Chrome Inspector remote debugging protocol. Although designed originally for JavaScript debugging, it can be used to debug all GraalVM languages from a browser.

## Embedding languages

Another advantage of GraalVM is the possibility to embed code from a guest language in Java and write "polyglot" applications. A developer can integrate JavaScript, Python, or other supported languages inside Java source code, granting them the characteristic advantages of those languages. A host Java application and a guest language pass data back and forth in the same memory space. It is possible thanks to the Truffle Language Implementation Framework and the GraalVM Polyglot API. Below is the example how to call a function defined in Python from Java:

```mw
try (Context context = Context.create()) {
    Value function = context.eval("python", "lambda x: x + 1");
    assert function.canExecute();
    int x = function.execute(41).asInt();
    assert x == 42;
}
```

The Python function increments its input value by one and returns the result to the host language. From Java, for security purposes, we ask first if the variable function can be executed via the `canExecute()` call, and then we invoke the function with the `execute()` call. Find more examples in the Embedding Languages reference documentation.

## Language and runtime support

GraalVM is written in and for the Java ecosystem. It can run applications written in all languages that compile to the Java bytecode format, for example, Java, Scala, Kotlin, and more.

Based on the Truffle Language Implementation Framework, the following additional languages are designed for use with GraalVM:

- GraalJS: An ECMAScript 2023 compliant JavaScript runtime, with support for Node.js
- GraalPy: A Python 3 language implementation
- GraalVM LLVM Runtime (*Sulong*): An LLVM bitcode interpreter implementation
- GraalWasm: A WebAssembly implementation
- TruffleRuby: A Ruby language implementation with preliminary support for Ruby on Rails
- FastR: An R language implementation

Support for additional languages can be implemented by users of GraalVM. Some notable third-party language implementations are grCuda, SOMns, TruffleSqueak, and Yona.
