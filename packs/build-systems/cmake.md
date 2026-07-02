---
title: "CMake"
source: https://en.wikipedia.org/wiki/CMake
domain: build-systems
license: GFDL-1.3 / CC-BY-SA-4.0
tags: makefile, cmake, build system, compiler toolchain
fetched: 2026-07-02
---

# CMake

**CMake** is a free, cross-platform, software development tool for building applications via compiler-independent instructions. It also can automate testing, packaging and installation. It runs on a variety of platforms and supports many programming languages.

As a meta-build tool, CMake configures native build tools which in turn build the codebase. CMake generates configuration files for other build tools based on CMake-specific configuration files. The other tools are responsible for more directly building, using the generated files. A single set of CMake-specific configuration files can be used to build a codebase using the native build tools of multiple platforms.

Notable native build tools supported by CMake include: Make, Qt Creator, Ninja, Android Studio, Xcode, and Visual Studio.

CMake is distributed as free and open-source software under a permissive BSD-3-Clause license.

## History

Initial development began in 1999 at Kitware with funding from the United States National Library of Medicine as part of the Visible Human Project. CMake was first released in 2000.

CMake was developed to support building the Insight Segmentation and Registration Toolkit (ITK) for multiple platforms. Stated goals included addressing weaknesses while maintaining strengths of contemporary tools such as autoconf and libtool, and to align with state of the art build technology of the time: configure scripts and Make files for Unix platforms, and Visual Studio project files for Windows.

CMake was inspired by multiple contemporary tools. pcmaker – developed by Ken Martin and others to support building the Visualization Toolkit (VTK) – converted Unix Make files into NMake files for building on Windows. gmake supported Unix and Windows compilers, but its design led to issues that were hard to resolve. Both tools were working examples of a build tool that supported both Unix and Windows, but they suffered from a serious flaw: they required Windows developers to use the command line even though many prefer to use an integrated development environment (IDE) such as Visual Studio.

CMake was to provide similar cross-platform support but to better satisfy the preferences of the developers on each platform.

The design goals of the first version included:

- Depend only on host C++ compiler; no other third-party tools or libraries required
- Generate Visual Studio project files (as well as Unix files)
- Support building targets: program, static library, shared library
- Run build-time code generators
- Support separate directory trees for source vs. build files
- Support host computer capability introspection
- Support automatic dependency scanning of C/C++ header files
- All features must work consistently and equally well on all supported platforms

For various reasons, CMake developers chose to develop a scripting language for CMake instead of using Tcl – a popular language for building at the time. Use of Tcl would have then added a dependency to the host machine which is counter to the goal of no dependencies other than a compiler. Also, Tcl was not well supported on Windows and some Unix systems at the time of initial development.

Subsequent development and improvements were fueled by the incorporation of CMake into developers’ own systems, including the VXL Project, the CABLE features added by Brad King, and GE Corporate R&D for support of DART (which is depracated since 3.7.). Additional features were created when VTK transitioned to CMake for its build environment and for supporting ParaView.

Version 3.0 was released in June 2014. It has been described as the beginning of "Modern CMake". Experts now advise to avoid variables in favor of *targets* and *properties*. The commands `add_compile_options`, `include_directories`, `link_directories`, `link_libraries` that were at the core of CMake 2 should now be replaced by target-specific commands.

## Name

CMake developer Brad King stated that "the 'C' in CMake stands for 'cross-platform'".

## Features

### Generators and IDE support

CMake can generate project files for IDEs like Microsoft Visual Studio, Xcode, Eclipse CDT and build scripts for MSBuild or NMake on Windows; Unix Make on Unix-like platforms such as Linux, macOS, and Cygwin; and Ninja on both Windows and Unix-like platforms by specifying generator for a platform-specific build tool. By default, CMake automatically determines default generator for the host environment it runs on. Command line option `-G` can be used to specify alternative generator. E.g. `-G Unix Makefiles` forces CMake to create build scripts for make.

CMake does not support custom generators without modifying the CMake implementation. None-the-less, the CMake source code could be modified to include a custom generator.

### Build targets

CMake supports building executables, libraries (e.g. `libxyz`, `xyz.dll` etc.), object file libraries and pseudo-targets (including aliases). CMake can produce object files that can be linked against by executable binaries/libraries, avoiding dynamic (run-time) linking and using static (compile-time) linking instead. This enables flexibility in configuration of various optimizations.

Target generation can be configured via target properties. With older versions, this was done via `CMAKE_`-prefixed global variables, but this approach is deprecated.

### Hierarchical configuration

CMake configuration files can be structured according the hierarchical structure of the source code; the source tree. A `CMakeLists.txt` in a root source directory serves as the root of the configuration. It may include sub-directories which each contain a `CMakeLists.txt`. Repeating this, results in a hierarchical structure of configuration that follows the structure of the source code.

### Separate build tree

CMake can store generated files (both by CMake and the native build tools) in a directory tree that is separate from the source tree.

This enables multiple builds from the same source tree since each has non-overlapping file system space. This may be leveraged to build different or even incompatible configurations such as for different platforms.

This also simplifies file management by allowing removing generated files by deleting a single directory tree instead of removing multiple files and directories throughout the source tree. This tends to prevent accidentally deleting source files or accidentally adding generated files to source control.

### Dependency management

CMake ensures that downstream components are re-built when its sources are changed or built.

### Flexible project structure

CMake can locate system-wide and user-specified executables, files, and libraries. These locations are stored in a cache, which can then be tailored before generating the target build files. The cache can be edited with a graphical editor, which is shipped with CMake.

Complicated directory hierarchies and applications that rely on several libraries are well supported by CMake. For instance, CMake is able to accommodate a project that has multiple toolkits, or libraries that each have multiple directories. In addition, CMake can work with projects that require executables to be created before generating code to be compiled for the final application. Its open-source, extensible design allows CMake to be adapted as necessary for specific projects.

### Compiler feature detection

CMake allows specification of features that the compiler is required to support in order to get the target program or library compiled.

### Compiler support

CMake supports many compilers, including: Apple Clang, Clang, GNU GCC, MSVC, Oracle Developer Studio, and Intel C++ Compiler.

### Packaging

CMake can produce packages that can be consumed both by end-user and third-party cmake-based project. Via CPack, built files may be packed into an archive file for a target system's package manager (e.g. dpkg) or installer supported by the target platform. CMake provides functions for pulling packages from a remote server that can be used as part of the build process or link previously installed cmake packages.

### GUI

Cmake may be run by using a ncurses program like `ccmake` that can be used to configure projects via command-line interface.

### Precompiled headers and modules

It is possible to generate precompiled headers via CMake since version 3.6. As of version 3.28, CMake can also compile modules. Experimental support for header units also exists.

### JSON strings

CMake supports extracting values into variables from JSON-data strings (since version 3.19).

## Language

CMake includes an interpreter for a relatively simple, custom, imperative scripting language that supports variables, string manipulation, arrays, function and macro declaration, and module inclusion (importing).

The interpreter reads CMake language commands from files named `CMakeLists.txt` which specify source files and build preferences. CMake uses this information to generate native tool configuration files. Additionally, files with suffix `.cmake` can be used for storing additional script.

### Command syntax

CMake language commands are formatted as:

```
name(argument ...)
```

Arguments are whitespace-separated and can include keywords to separate groups of arguments. For instance, in the following command, the keyword `COMPILE_FLAGS` delimits a list of source files from compiler flags.

```
set_source_file_properties(filename ... COMPILE_FLAGS compile_flag ...)
```

## Implementation

The CMake scripting language is implemented via Yacc and Lex generators.

The executable programs CMake, CPack, and CTest are written in C++.

Much of CMake's functionality is implemented in modules written in the CMake language.

CMake documentation (since release 3.0) uses reStructuredText markup. HTML pages and man pages are generated by the Sphinx documentation generator.

## Additional tools

CMake ships with numerous `.cmake` script files and development tools that facilitate tasks such as finding dependencies (both built-in and external, e.g. `FindXYZ` modules), testing the toolchain environment and executables, packaging releases (CPack), and managing dependencies on external projects (`ExternalProject` module). Additional development tools include:

- **ccmake** and **cmake-gui** — for updating configuration variables intended for a native build tool
- **CPack** — for packaging software as Linux RPM, deb, and gzip packages, NSIS files (for Windows), and macOS packages
- **CTest** and **CDash** — for software testing and reporting

## Adoption

CMake has been very widely adopted among commercial, open source, and academic software projects. A few notable users include Android NDK, Netflix, Inria, MySQL, Boost (C++ libraries), KeePassXC, KDE, KiCAD, FreeCAD, Webkit, Blender, Biicode, ReactOS, Apache Qpid, the ATLAS experiment, and Second Life.

## Build process

Building via CMake has two major stages. First, native build tool configuration files are generated from CMake configuration files – written in the CMake scripting language. The command line syntax is `cmake <dir>` where <dir> is a directory that contains a `CMakeLists.txt` file. Then, the native build tools are invoked either via CMake (`cmake --build <dir>`) or directly via the native tool's interface. The native build tools use the generated files.

## Examples

### Hello world

The following demonstrates configuring CMake to build a hello world program written in C++, and using CMake to build the program.

hello.cpp:

```mw
#include <print>

int main() {
    std::println("Hello, world!");
    return 0;
}
```

CMakeLists.txt:

```mw
cmake_minimum_required(VERSION 3.22)
project(HelloWorld CXX)
add_executable(hello hello.cpp)
```

To build via CMake, first cd to the directory containing the two files above. Then, generate the native build config files via the cross-platform CMake command:

```mw
cmake -B out .
```

All generated files will be under the directory *out* as specified via `-B out`.

Then, build via the native build tool as supported thru CMake:

```mw
cmake --build out
```

The program is then available for running. Via Bash, the command is like `./out/hello`. On Windows, the output file ends with `.exe`.

### Include

This example demonstrates configuring the preprocessor include path.

hello.cpp:

```mw
#include <print>

#include "hello.hpp"

int main() {
    for (int i = 0; i < TIMES; ++i) {
        std::println("Hello, world!");
    }
    return 0;
}
```

hello.hpp:

```mw
#pragma once

constexpr int TIMES = 10;
```

CMakeLists.txt:

```mw
cmake_minimum_required(VERSION 3.22)
project(HelloWorld CXX)
add_executable(hello hello.cpp)
target_include_directories(hello PRIVATE ${PROJECT_SOURCE_DIR})
```
