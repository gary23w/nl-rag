---
title: "Meson (software)"
source: https://en.wikipedia.org/wiki/Meson_(software)
domain: meson-build
license: CC-BY-SA-4.0
tags: meson build, build system, build automation, ninja backend
fetched: 2026-07-02
---

# Meson (software)

**Meson** (/ˈmɛ.sɒn/) is a software build automation tool for building a codebase. Meson adopts a convention over configuration approach to minimize the data required to configure the most common operations. Meson is free and open-source software under the Apache License 2.0.

Meson is written in Python and runs on Unix-like (including Linux and macOS), Windows and other operating systems. It supports building C, C++, C#, CUDA, Objective-C, D, Fortran, Java, Rust, and Vala. It handles dependencies via a mechanism named *Wrap*. It supports GNU Compiler Collection (gcc), Clang, Visual C++ and other compilers, including non-traditional compilers such as Emscripten and Cython. The project uses ninja as the primary backend buildsystem, but can also use Visual Studio or Xcode backends.

Meson's support for Fortran and Cython was improved to help various scientific projects in their switch from setuptools to Meson, for example SciPy. Meson can be used as a PEP517 backend to build Python *wheels*, via the meson-python package.

## Language

The syntax of Meson's build description files, the Meson language, borrows from Python, but is not Python. It is designed such that it can be reimplemented in any other language; for example, muon is a C implementation, and Meson++ is a C++ implementation. The dependency on Python is an implementation detail.

The Meson language is intentionally not Turing-complete, and therefore can not express an arbitrary program. Instead, arbitrary build steps beyond compiling supported languages can be represented as custom targets.

The Meson language is strongly typed, such that builtin types like library, executable, string, and lists thereof, are non-interchangeable. In particular, unlike Make, the list type does not split strings on whitespace. Thus, whitespace and other characters in filenames and program arguments are handled cleanly.

## Speed and correctness

As with any typical buildsystem, correct incremental builds are the most significant speed feature (because all incremental progress is discarded whenever the user is forced to do a clean build).

Unlike bare Make, the separate configure step ensures that changes to arguments, environment variables and command output are not partially applied in subsequent builds, which would lead to a stale build.

Like Ninja, Meson does not support globbing of source files. By requiring all source files to be listed in the build definition files, the build definition file timestamps are sufficient to determine whether the set of source files has changed, thereby ensuring that removed source files are detected. CMake supports globbing, but recommends against it for the same reason.

Meson uses ccache automatically if installed. It also detects changes to symbol tables of shared libraries to skip relinking executables against the library when there are no ABI changes. Precompiled headers are supported, but require configuration. Debug builds are without optimization by default.

## Features

A stated goal of Meson is to facilitate modern development practices. As such, Meson knows how to do unity builds, build with test coverage etc. without the programmer having to write support for this.

### Subprojects

Meson can automatically find and use external dependencies installed on the user's system via pkg-config, CMake, and project-specific lookups. Alternatively, or as a fallback, a dependency can be provided as a *subproject* – a Meson project within another, either contained or as a download link, possibly with patches. This lets Meson resolve dependency hell for the convenience of casual users who want to compile the project, but may contribute to software bloat if a common installed dependency could have been used instead. The mode favored by Linux packagers is therefore fallback.

Meson supports Meson and CMake subprojects. A Meson build file may also refer to the WrapDB service.

### Cross compilation

Cross compilation requires extra configuration, which Meson supports in the form of a separate *cross file*, which can be external to the Meson project.

### Installation directory setup

Setting the library installation directory on x86_64 Unix is handled automatically by Meson, but not by other tools such as Autotools.

## Adopters

GNOME has made it a goal to port its projects to Meson. As of late 2017, GNOME Shell itself exclusively requires Meson after abandoning Autotools, and central components like GTK+, Clutter-GTK, GLib and GStreamer can be built with Meson.

Many freedesktop.org projects have switched to Meson. Systemd relies on Meson since dropping Autotools in version 234, and also X.Org and Mesa were ported to Meson.

## Feature comparison

Feature comparison with CMake and Make.

| Feature | Meson | CMake | Make |
|---|---|---|---|
| Datatypes | Yes | No | No |
| List datatype | Yes | semicolon-delimited string | whitespace-delimited string |
| Dictionary datatype | since 0.47.0 | No | No |
| File globbing | No | Yes | non-standard extension on some variants |
| Extensible via custom functions | No | Yes | No |
| Can read output of arbitrary commands (at configure time) | run_command | Yes | Yes |
| Can run arbitrary commands at build time as recipes of custom targets | Yes | Yes | Yes |
| Prohibits stale builds (partial rebuild against input change) | Yes (unless there are bugs) | If not globbing source files | *Recursive Make* (an idiomatic pattern) is broken in this respect |
| The target that runs tests depends on the tests being built (e.g. `test` depends on `all`) | Yes | No, and `add_dependencies(test all)` is forbidden, because the `test` target is reserved. | Trivial to add |
| Ccache | Automatic | Trivial to add | Trivial to add |
| Distcc | Trivial to add | Trivial to add | Trivial to add |
| Symbol-table-aware relinking | Yes | Do it yourself | Do it yourself |
| Precompiled headers | Optional | CMake ≥ 3.16 | Do it yourself |
| Finding installed dependencies | pkg-config, CMake packages | CMake module, pkg-config | — |
| Downloading dependencies automatically | subproject | FetchContent | — |
| Finding installed dependencies, with download fallback | pkg-config + subproject | CMake module/pkg-config + `FetchContent` | — |
| pkg-config file generator | Yes | No | — |
| Facilitate use as an auto-downloadable dependency | Can be used as a Meson subproject | No | — |
