---
title: "Consuming packages"
source: https://docs.conan.io/2/tutorial/consuming_packages.html
domain: conan-cpp
license: CC-BY-SA-4.0
tags: conan cpp, c++ packages, package manager, dependency management
fetched: 2026-07-02
---

# Consuming packages

This section shows how to build your projects using Conan to manage your dependencies. We will begin with a basic example of a C project that uses CMake and depends on the **zlib** library. This project will use a *conanfile.txt* file to declare its dependencies.

We will also cover how you can not only use ‘regular’ libraries with Conan but also manage tools you may need to use while building: like CMake, msys2, MinGW, etc.

Then, we will explain different Conan concepts like settings and options and how you can use them to build your projects for different configurations like Debug, Release, with static or shared libraries, etc.

Also, we will explain how to transition from the *conanfile.txt* file we used in the first example to a more powerful *conanfile.py*.

After that, we will introduce the concept of Conan build and host profiles and explain how you can use them to cross-compile your application to different platforms.

Then, in the “Introduction to versioning” we will learn about using different versions, defining requirements with version ranges, the concept of revisions and a brief introduction to lockfiles to achieve reproducibility of the dependency graph.

Table of contents

- Build a simple CMake project using Conan
- Using build tools as Conan packages
- Building for multiple configurations: Release, Debug, Static and Shared
  - Modifying settings: use Debug configuration for the application and its dependencies
  - Modifying options: linking the application dependencies as shared libraries
  - Difference between settings and options
  - Introducing the concept of Package ID
- Understanding the flexibility of using conanfile.py vs conanfile.txt
  - Use the layout() method
  - Use the validate() method to raise an error for non-supported configurations
  - Conditional requirements using a conanfile.py
  - Use the generate() method to copy resources from packages
  - Use the build() method and `conan build` command
- How to cross-compile your applications using Conan: host and build contexts
  - Conan two profiles model: build and host profiles
- Introduction to versioning
  - Version ranges
  - Revisions
  - Lockfiles

Note

The Conan 2 Essentials training course is available for free at the JFrog Academy, which covers the same topics as this documentation but in a more interactive way. You can access it here.
