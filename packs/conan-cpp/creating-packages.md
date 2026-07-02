---
title: "Creating packages"
source: https://docs.conan.io/2/tutorial/creating_packages.html
domain: conan-cpp
license: CC-BY-SA-4.0
tags: conan cpp, c++ packages, package manager, dependency management
fetched: 2026-07-02
---

# Creating packages

This section shows how to create Conan packages using a Conan recipe. We begin by creating a basic Conan recipe to package a simple C++ library that you can scaffold using the **conan new** command. Then, we will explain the different methods that you can define inside a Conan recipe and the things you can do inside them:

- Using the `source()` method to retrieve sources from external repositories and apply patches to those sources.
- Add requirements to your Conan packages inside the `requirements()` method.
- Use the `generate()` method to prepare the package build, and customize the toolchain.
- Configure settings and options in the `configure()` and `config_options()` methods and how they affect the packages’ binary compatibility.
- Use the `build()` method to customize the build process and launch the tests for the library you are packaging.
- Select which files will be included in the Conan package using the `package()` method.
- Define the package information in the `package_info()` method so that consumers of this package can use it.
- Use a *test_package* to test that the Conan package can be consumed correctly.

After this walkthrough around some Conan recipe methods, we will explain some peculiarities of different types of Conan packages like, for example, header-only libraries, packages for pre-built binaries, packaging tools for building other packages or packaging your own applications.

Table of contents

- Create your first Conan package
  - A note about the Conan cache
- Handle sources in packages
  - Sources from a *zip* file stored in a remote repository
  - Sources from a branch in a *git* repository
  - Using the conandata.yml file
- Add dependencies to packages
  - Headers transitivity
- Preparing the build
- Configure settings and options in recipes
  - Conan packages binary compatibility: the **package ID**
- Build packages: the build() method
  - Build and run tests for your project
  - Conditionally patching the source code
  - Conditionally select your build system
- Package files: the package() method
  - Using CMake install step in the package() method
  - Use conan.tools.files.copy() in the package() method and packaging licenses
  - Managing symlinks in the package() method
- Define information for consumers: the package_info() method
  - Setting information in the package_info() method
  - Define information for consumers depending on settings or options
  - Properties model: setting information for specific generators
  - Propagating environment or configuration information to consumers
  - Define components for Conan packages that provide multiple libraries
- Testing Conan packages
- Other types of packages
  - Header-only packages
  - Package prebuilt binaries
  - Tool requires packages

Note

The Conan 2 Essentials training course is available for free at the JFrog Academy, which covers the same topics as this documentation but in a more interactive way. You can access it here.
