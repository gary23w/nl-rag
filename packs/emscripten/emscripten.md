---
title: "Emscripten"
source: https://en.wikipedia.org/wiki/Emscripten
domain: emscripten
license: CC-BY-SA-4.0
tags: emscripten toolchain, llvm to wasm, c++ to webassembly, asm.js compilation
fetched: 2026-07-02
---

# Emscripten

**Emscripten** is an LLVM/Clang-based compiler that compiles LLVM IR to WebAssembly, primarily for execution in web browsers.

Emscripten allows applications and libraries written in C or C++ to be compiled ahead of time and run efficiently in web browsers, typically at speeds comparable to or faster than interpreted or dynamically compiled JavaScript. It even emulates an entire POSIX operating system, enabling programmers to use functions from the C standard library (libc).

With the more recent development of the WebAssembly System Interface (WASI) and WebAssembly runtimes such as Node.js, Wasmtime, and Wasmer, Emscripten can also be used to compile to WebAssembly for execution in non-web embeddings as well.

## Usage

Emscripten has been used to port a number of C/C++ code bases to WebAssembly, including Unreal Engine 3, SQLite, MeshLab, Bullet physics, AutoCAD, and a subset of the Qt application framework. Other examples of software ported to WebAssembly via Emscripten include the following:

### Game engines

The Unity, Defold, and Godot game engines provide an export option to HTML5, utilizing Emscripten. Unreal Engine had this export option but it has been migrated out of the engine to a community member plug in. The Source Engine, has a community developed port for Emscripten dubbed "HalfLife2JS".

### Frameworks & toolkits

openFrameworks exports native C++ applications to HTML5 via Emscripten. emscripten-qt permits compiling applications written using the Qt application framework to WebAssembly.

### Software archiving

In December 2014, the Internet Archive launched a DOSBox emulator compiled in Emscripten to provide browser-based access to thousands of archived MS-DOS and PC programs.

### Creation

Emscripten was created by Alon Zakai in 2010, motivated by his desire to port his fork of the open-source first-person shooter game *Sauerbraten*, known as *Syntensity*, to the web. *Sauerbraten* (also known as *Cube 2*) is an open-source FPS game, and *Syntensity* was Zakai's project that extended the Cube 2 Engine for greater flexibility. Observing the increasing shift of applications to web browsers, Zakai began developing Emscripten as an LLVM-to-JavaScript compiler, aiming to make it possible to run existing C and C++ code, such as game engines, directly in the browser. In early blog posts, Zakai explained that his long-term goal was "to run Syntensity, or a smaller version of it, on the web", and Emscripten was released as open source shortly after its initial development, making it available for the broader community to experiment with and contribute to.
