---
title: "Rust-based platform for the Web"
source: https://swc.rs/
domain: swc-compiler
license: CC-BY-SA-4.0
tags: swc compiler, rust javascript compiler, fast typescript transpiler, swc bundler
fetched: 2026-07-02
---

# SWC

Rust-based platform for the Web

SWC is an extensible Rust-based platform for the next generation of fast developer tools. It’s used by tools like Next.js, Parcel, and Deno, as well as companies like Vercel, ByteDance, Tencent, Shopify, Trip.com, and more.

SWC can be used for both compilation and bundling. For compilation, it takes JavaScript / TypeScript files using modern JavaScript features and outputs valid code that is supported by all major browsers.

🏎

SWC is **20x faster than Babel** on a single thread and **70x faster** on four cores.

Get Started · Playground · Blog · Rustdocs  · GitHub Repository  · Donate

## Overview

SWC can be downloaded and used as a pre-built binary, or built from source. Currently, the following binaries are provided:

- Mac (Apple Silicon)
- Mac (x64)
- Linux (x86_64)
- Linux (aarch64)
- Linux (armv7)
- Alpine Linux (also install `@swc/core-linux-musl`)
- Android (aarch64)
- Windows (win32-x64)
- Windows (ia32)

#### Download prebuilt binaries

### pnpm

```
pnpm add -D @swc/cli @swc/core
```

### npm

```
npm i -D @swc/cli @swc/core
```

### yarn

```
yarn add -D @swc/cli @swc/core
```

#### Transpile JavaScript file and emit to stdout

```
npx swc ./file.js
```

## Features

SWC is designed to be extensible. Currently, there is support for:

- Compilation
- Minification
- Transforming with WebAssembly
- Usage inside webpack and Rspack (`swc-loader`)
- Improving Jest performance (`@swc/jest`)
- Custom Plugins

Learn more.

## Community

SWC is created by kdy1 . Follow @kdy1dev  on Twitter for future project updates.

Feel free to join the discussions on GitHub !
