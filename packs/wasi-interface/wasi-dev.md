---
title: "Introduction · WASI.dev"
source: https://wasi.dev/
domain: wasi-interface
license: CC-BY-SA-4.0
tags: wasi interface, webassembly system interface, wasm sandbox capabilities, wasm host abi
fetched: 2026-07-02
---

# Introduction

The **WebAssembly System Interface (WASI)** is a group of standards-track API specifications for software compiled to the **W3C WebAssembly (Wasm) standard**. WASI is designed to provide a secure standard interface for applications that can be compiled to Wasm from any language, and that may run anywhere, from browsers to clouds to embedded devices.

By standardizing APIs for WebAssembly, WASI provides a way to compose software written in different languages without costly and clunky interface systems like HTTP-based microservices. We believe that every project with a plugin model should be using WASI, and that WASI is ideally suited for projects with SDKs for multiple languages, e.g. client libraries.

To date, WASI has seen three milestone releases: **0.1**, **0.2**, and **0.3**. (Sometimes you will see these referred to as Preview 1/2/3 or P1/P2/P3.) WASI 0.3 adds native async support to the Component Model and refactors WASI interfaces to take advantage of async primitives like `stream<T>` and `future<T>`. For more details, see WASI 0.3.

## Who are we?

WASI is an open standard under active development by the **WASI Subgroup** in the **W3C WebAssembly Community Group**. Discussions happen in GitHub issues, pull requests, and bi-weekly Zoom meetings.

## Who are you?

WASI and Wasm are tools for any type of software developer: whether you're writing web apps, plugins, serverless functions, User-Defined Functions (UDFs) in a database, embedded controller components, sidecar networking filters, or something completely different. This site is intended to introduce the concepts and vocabulary of WASI regardless of your background, use-case, or familiarity with the WebAssembly ecosystem.

## How to get started

There are many different runtimes that support WASI including Wasmtime, WAMR, WasmEdge, wazero, Wasmer, wasmi, wasm3, jco and pywasm. Many of these runtimes have different areas of focus (i.e., IoT, embedded devices, and edge for WAMR, server-side and non-web embeddings with components for Wasmtime, and running in JS environments and browsers for Jco). The introductory documentation for each is a great place to start.

WASI can be implemented by both core Wasm modules and applications built according to the **Component Model**, a specification for Wasm applications that are interoperable and composable. You can learn more about components in the Bytecode Alliance's **WebAssembly Component Model** documentation.

WASI applications run in a **capability-based** sandbox: a Wasm module or component starts with no ambient authority and can only do what the host explicitly grants. See the Security page for more.

When you're ready to start building, the Component Model documentation walks through compiling a first component and running it on Wasmtime or jco, with tutorials for Rust, JavaScript, Python, Go, C, C#, and MoonBit.

Continue reading to learn more about WASI releases, including available APIs and how they are defined.
