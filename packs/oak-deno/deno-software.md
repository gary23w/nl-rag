---
title: "Deno (software)"
source: https://en.wikipedia.org/wiki/Deno_(software)
domain: oak-deno
license: CC-BY-SA-4.0
tags: oak deno framework, deno middleware framework, deno web server, oak context router
fetched: 2026-07-02
---

# Deno (software)

**Deno** (/diːnoʊ/) is a runtime for JavaScript, TypeScript, and WebAssembly that is based on the V8 JavaScript engine and the Rust programming language. Deno was co-created by Ryan Dahl, the creator of Node.js, and Bert Belder.

Deno explicitly takes on the role of both runtime and package manager within a single executable, rather than requiring a separate package-management program.

## History

Deno was announced at JSConf EU 2018 by Ryan Dahl in his talk "10 Things I Regret About Node.js". In his talk, Dahl mentioned his regrets about the initial design decisions with Node.js, focusing on his choices of not using promises in API design, usage of the legacy build system GYP, node_modules and package.json, leaving out file extensions, magical module resolution with index.js and breaking the sandboxed environment of V8. He eventually presented the prototype of Deno, aiming to achieve system call bindings through message passing with serialization tools such as Protocol Buffers, and to provide command line flags for access control.

Deno was initially written in Go and used Protocol Buffers for serialization between privileged (Go, with system call access) and unprivileged (V8) sides. However, Go was soon replaced with Rust due to concerns of double runtime and garbage collection pressure. Tokio was introduced in place of libuv as the asynchronous event-driven platform, and FlatBuffers was adopted for faster, "zero-copy" serialization and deserialization but later in August 2019, FlatBuffers was removed after publishing benchmarks that measured a significant overhead of serialization in April 2019.

A standard library, modeled after Go's standard library, was created in November 2018 to provide extensive tools and utilities, partially solving Node.js' dependency tree explosion problem.

The official Deno 1.0 was released on May 13, 2020.

Deno Deploy, inspired by Cloudflare Workers, was released on June 23, 2021. Announced May 4, 2022 Beta 4 improved the dashboard and added billing functionality.

Deno Fresh 1.0 was announced June 28, 2022. It features a new full stack web framework for Deno that by default sends zero JavaScript to the client. The framework has no build step which allows for an order of magnitude improvements in deployment times. Version 1.1 was released September 8, 2022.

Deno SaaSKit beta was announced April 4, 2023. It is an open-source, modern SaaS template built with Fresh and Deno.

Deno 2 was released October 9, 2024. It primarily brings Node.js compatibility improvements and removes deprecated features.

## Overview

Deno aims to be a productive and secure scripting environment for the modern programmer. Similar to Node.js, Deno emphasizes event-driven architecture, providing a set of non-blocking core I/O utilities, along with their blocking versions. Deno could be used to create web servers, perform scientific computations, etc. Deno is open source software under the MIT License.

### Comparison with Node.js

Deno and Node.js are both runtimes built on the V8 JavaScript engine developed by the Chromium Project, the engine used for Chromium and Google Chrome web browsers. They both have internal event loops and provide command-line interfaces for running scripts and a wide range of system utilities.

Deno mainly deviates from Node.js in the following aspects:

1. Supports only ES Modules like browsers where Node.js supports both ES Modules and CommonJS. CommonJS support in Deno is possible by using a compatibility layer.
2. Supports URLs for loading local or remote dependencies, similar to browsers, and uses module specifiers like `npm:` and `node:` to import NPM or polyfill Node.JS modules. Node.js supports both URLs and modules.
3. Does not require a package manager for resource fetching, thus no need for a registry like npm.
4. Supports TypeScript out of the box, using a snapshotted TypeScript compiler or the swc compiler with caching mechanisms.
5. Aims for better compatibility with browsers with a wide range of Web APIs.
6. Restricts file system and network access by default in order to run sandboxed code.
7. Supports a single API to utilize promises, ES6 and TypeScript features whereas Node.js supports both promise and callback APIs.
8. Minimizes core API size, while providing a large standard library with no external dependencies.
9. Uses message passing channels for invoking privileged system APIs and using bindings.

## Funding

On March 29, 2021, Deno Land Inc was announced, with backing in millions of dollars from Shasta Ventures, Mozilla Corporation and a few others. It was established to further the development of Deno and provide a commercial offering to users.

A year on, Deno announced a further $21 million in Series A funding led by Sequoia Capital.
