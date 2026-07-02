---
title: "V8 (JavaScript engine)"
source: https://en.wikipedia.org/wiki/V8_(JavaScript_engine)
domain: deno-deploy
license: CC-BY-SA-4.0
tags: deno deploy, deno edge runtime, typescript edge functions, v8 isolate deploy
fetched: 2026-07-02
---

# V8 (JavaScript engine)

**V8** is a JavaScript and WebAssembly engine developed by Google for its Chrome browser. V8 is free and open-source software (FOSS) and part of the Chromium project. It is also used in non-browser contexts, notably including the Node.js runtime system. Other server-side JavaScript runtimes use alternative engines, such as Bun (which uses JavaScriptCore) and Hermes (used by React Native).

## History

Google created V8 for its Chrome browser, so V8's first release coincided with Chrome's first release in 2008. It was named after the V8 engine, and its lead developer was Lars Bak. For several years, Chrome was faster than other browsers at executing JavaScript.

The V8 assembler is based on the Strongtalk assembler. On 7 December 2010, a new compiling infrastructure named Crankshaft was released, with speed improvements. In version 41 of Chrome in 2015, project TurboFan was added to provide more performance improvements with previously challenging workloads such as asm.js. Much of V8's development is strongly inspired by the Java HotSpot Virtual Machine developed by Sun Microsystems, with the newer execution pipelines being very similar to those of HotSpot's.

Support for the WebAssembly language began in 2015.

In 2016, the Ignition interpreter was added to V8 with the design goal of reducing the memory usage on small memory Android phones in comparison with TurboFan and Crankshaft. Ignition is a register based machine and shares a similar (albeit not the exact same) design to the templating interpreter utilized by HotSpot.

In 2017, V8 shipped a brand-new compiler pipeline, consisting of Ignition (the interpreter) and TurboFan (the optimizing compiler). Starting with V8 version 5.9, Full-codegen (the early baseline compiler) and Crankshaft are no longer used in V8 for JavaScript execution, since the team believed they were no longer able to keep pace with new JavaScript language features and the optimizations those features required.

In 2021, a new tiered compilation pipeline was introduced with the release of the SparkPlug compiler, which supplements the existing TurboFan compiler within V8, in a direct parallel to the profiling C1 Compiler used by HotSpot.

In 2023, the Maglev SSA-based compiler was added, which is 10 times slower than Sparkplug but 10 times faster than TurboFan, bridging the gap between Sparkplug and TurboFan for less frequently run loops that do not get "hot" enough to be optimised by TurboFan, as is the case for most web applications that spend more time interacting with the browser than in JavaScript execution.

## Design

V8 first generates an abstract syntax tree with its own parser. Then, Ignition generates bytecode from this syntax tree using the internal V8 bytecode format. TurboFan compiles this bytecode into machine code. In other words, V8 compiles ECMAScript directly to native machine code using just-in-time compilation before executing it. The compiled code is additionally optimized (and re-optimized) dynamically at runtime, based on heuristics of the code's execution profile. Optimization techniques used include inlining, elision of expensive runtime properties, and inline caching. The garbage collector is a generational incremental collector.

## Usage

V8 can compile to x86, ARM or MIPS instruction set architectures in both their 32-bit and 64-bit editions; it has additionally been ported to PowerPC, and to IBM ESA/390 and z/Architecture, for use in servers.

V8 can be used in a browser or integrated into independent projects. V8 is used in the following software:

- Chromium-based web browsers - Google Chrome, Brave, Opera, Vivaldi and Microsoft Edge.
- Cloud-based environments, like Google Apps Script
- Couchbase database server
- Deno runtime environment
- Electron desktop application framework, used by apps such as the Visual Studio Code text editor and Discord
- MarkLogic database server
- NativeScript mobile application framework
- Node.js runtime environment
