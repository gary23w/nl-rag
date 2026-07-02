---
title: "Software build"
source: https://en.wikipedia.org/wiki/Software_build
domain: slsa-framework
license: CC-BY-SA-4.0
tags: slsa provenance framework, build integrity levels, supply chain provenance, hermetic build attestation
fetched: 2026-07-02
---

# Software build

A **software build** is the process of converting source code files into standalone software artifact(s) that can be run on a computer, or the result of doing so. In include functions such as version control, code quality analysis, compilation, and linking.

In software production, builds optimize software for performance and distribution, packaging into formats such as '.*exe'; '.deb'; '.apk'*.

The build process often employs specialized tools such as CMake, Make, or Gradle, and integrates with automation systems including Jenkins or GitHub Actions. Despite advancements, challenges such as dependency conflicts, platform compatibility, and long compile times, remain problems.

## Functions

In software development, building software is an end-to-end process that involves many distinct functions. Some of these functions are described below.

### Version control

The version control function carries out activities such as workspace creation and updating, baselining and reporting. It creates an environment for the build process to run in and captures metadata about the inputs and output of the build process to ensure repeatability and reliability.

Tools such as Git, AccuRev or StarTeam help with these tasks by offering tools to tag specific points in history as being important, and more.

### Code quality

Also known as static program analysis/static code analysis this function is responsible for checking that developers have adhered to the seven axes of code quality: comments, unit tests, duplication, complexity, coding rules, potential bugs and architecture & design.

Ensuring a project has high-quality code results in fewer bugs and influences nonfunctional requirements such as maintainability, extensibility and readability; which have a direct impact on the ROI for a business.

### Compilation

This is only a small feature of managing the build process. The compilation function turns source files into directly executable or intermediate objects. Not every project will require this function.

While for simple programs the process consists of a single file being compiled, for complex software the source code may consist of many files and may be combined in different ways to produce many different versions.

### Linking

A linker or link editor is a computer program that combines intermediate software build files such as object and library files into a single executable file such as a program or library. A linker is often part of a toolchain that includes a compiler and/or assembler that generates intermediate files that the linker processes. The linker may be integrated with other toolchain tools such that the user does not interact with the linker directly.

A simpler version that writes its output directly to memory is called the *loader*, though loading is typically considered a separate process.

## Build tools

The process of building a computer program is usually managed by a build tool, a program that coordinates and controls other programs. Examples of such a program are make, Gradle, Ant, Maven, Rake, SCons and Phing. The build utility typically needs to compile the various files, in the correct order. If the source code in a particular file has not changed then it may not need to be recompiled ("may not" rather than "need not" because it may itself depend on other files that have changed). Sophisticated build utilities and linkers attempt to refrain from recompiling code that does not need it, to shorten the time required to complete the build. A more complex process may involve other programs producing code or data as part of the build process and software.
