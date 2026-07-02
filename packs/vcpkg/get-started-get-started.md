---
title: "Install and use packages with CMake"
source: https://learn.microsoft.com/en-us/vcpkg/get_started/get-started
domain: vcpkg
license: CC-BY-SA-4.0
tags: vcpkg cpp, c++ packages, package manager, manifest mode
fetched: 2026-07-02
---

# Install and use packages with CMake

Read in English

Edit

Note

Access to this page requires authorization. You can try signing in or changing directories.

Access to this page requires authorization. You can try changing directories.

# Tutorial: Install and use packages with CMake

This tutorial shows you how to create a C++ "Hello World" program that uses the `fmt` library with CMake and vcpkg. You'll install dependencies, configure, build, and run a simple application.

## Prerequisites

- A terminal
- A C++ compiler
- CMake
- Git

Note

For Windows users, Visual Studio's MSVC (Microsoft Visual C++ Compiler) is the required compiler for C++ development.

## 1 - Set up vcpkg

1. Clone the repository The first step is to clone the vcpkg repository from GitHub. The repository contains scripts to acquire the vcpkg executable and a registry of curated open-source libraries maintained by the vcpkg community. To do this, run: The vcpkg curated registry is a set of over 2,000 open-source libraries. These libraries have been validated by vcpkg's continuous integration pipelines to work together. While the vcpkg repository does not contain the source code for these libraries, it holds recipes and metadata to build and install them in your system.
  ```
git clone https://github.com/microsoft/vcpkg.git
  ```
2. Run the bootstrap script Now that you have cloned the vcpkg repository, navigate to the `vcpkg` directory and execute the bootstrap script: `cd vcpkg && bootstrap-vcpkg.bat` `cd vcpkg; .\bootstrap-vcpkg.bat` `cd vcpkg && ./bootstrap-vcpkg.sh` The bootstrap script performs prerequisite checks and downloads the vcpkg executable. That's it! vcpkg is set up and ready to use.

## 2 - Set up the project

1. Configure the `VCPKG_ROOT` environment variable. `export VCPKG_ROOT=/path/to/vcpkg export PATH=$VCPKG_ROOT:$PATH` Note Setting environment variables using the `export` command only affects the current shell session. To make this change permanent across sessions, add the `export` command to your shell's profile script (e.g., `~/.bashrc` or `~/.zshrc`). `set "VCPKG_ROOT=C:\path\to\vcpkg" set PATH=%VCPKG_ROOT%;%PATH%` Note Setting environment variables in this manner only affects the current terminal session. To make these changes permanent across all sessions, set them through the Windows System Environment Variables panel. `$env:VCPKG_ROOT = "C:\path\to\vcpkg" $env:PATH = "$env:VCPKG_ROOT;$env:PATH"` Note Setting environment variables in this manner only affects the current terminal session. To make these changes permanent across all sessions, set them through the Windows System Environment Variables panel. Setting `VCPKG_ROOT` tells vcpkg where your vcpkg instance is located. Adding it to `PATH` ensures you can run vcpkg commands directly from the shell.
2. Create the project directory.
  ```
mkdir helloworld && cd helloworld
  ```

## 3 - Add dependencies and project files

1. Create the manifest file and add the `fmt` dependency. First, create a manifest file (`vcpkg.json`) in your project's directory by running the `vcpkg new` command from within the `helloworld` directory: Next, add the `fmt` dependency: Your `vcpkg.json` should look like this: This is your manifest file. vcpkg reads the manifest file to learn what dependencies to install and integrates with CMake to provide the dependencies required by your project. The default `vcpkg-configuration.json` file introduces baseline constraints, specifying the minimum versions of dependencies that your project should use. While modifying this file is beyond the scope of this tutorial, it plays a crucial role in defining version constraints for your project's dependencies. Therefore, even though it's not strictly necessary for this tutorial, it's a good practice to add `vcpkg-configuration.json` to your source control to ensure version consistency across different development environments.
  ```
vcpkg new --application
  ```
  ```
vcpkg add port fmt
  ```
  ```
{
    "dependencies": [
        "fmt"
    ]
}
  ```
2. Create the project files. Create the `CMakeLists.txt` file with the following content: Now, let's break down what each line in the `CMakeLists.txt` file does: Create the `helloworld.cpp` file with the following content: In this `helloworld.cpp` file, the `<fmt/core.h>` header is included for using the `fmt` library. The `main()` function then calls `fmt::print()` to output the "Hello World!" message to the console.
  ```
cmake_minimum_required(VERSION 3.10)

project(HelloWorld)

find_package(fmt CONFIG REQUIRED)

add_executable(HelloWorld helloworld.cpp)

target_link_libraries(HelloWorld PRIVATE fmt::fmt)
  ```
  - `cmake_minimum_required(VERSION 3.10)`: Specifies that the minimum version of CMake required to build the project is 3.10. If the version of CMake installed on your system is lower than this, an error will be generated.
  - `project(HelloWorld)`: Sets the name of the project to "HelloWorld."
  - `find_package(fmt CONFIG REQUIRED)`: Looks for the `fmt` library using its CMake configuration file. The `REQUIRED` keyword ensures that an error is generated if the package is not found.
  - `add_executable(HelloWorld helloworld.cpp)`: Adds an executable target named "HelloWorld," built from the source file `helloworld.cpp`.
  - `target_link_libraries(HelloWorld PRIVATE fmt::fmt)`: Specifies that the `HelloWorld` executable should link against the `fmt` library. The `PRIVATE` keyword indicates that `fmt` is only needed for building `HelloWorld` and should not propagate to other dependent projects.
  ```
#include <fmt/core.h>

int main()
{
    fmt::print("Hello World!\n");
    return 0;
}
  ```

## 4 - Build and run the project

1. Run CMake configuration CMake can automatically link libraries installed by vcpkg when `CMAKE_TOOLCHAIN_FILE` is set to use vcpkg's custom toolchain. This can be acomplished using CMake presets files. Create the following files inside the `helloworld` directory: `CMakePresets.json` `CMakeUserPresets.json` The `CMakePresets.json` file contains a single preset named "vcpkg", which sets the `CMAKE_TOOLCHAIN_FILE` variable. The `CMakeUserPresets.json` file sets the `VCPKG_ROOT` environment variable to point to the absolute path containing your local installation of vcpkg. It is recommended to not check `CMakeUserPresets.json` into version control systems. Finally, configure the build using CMake:
  ```
{
  "version": 2,
  "configurePresets": [
    {
      "name": "vcpkg",
      "generator": "Ninja",
      "binaryDir": "${sourceDir}/build",
      "cacheVariables": {
        "CMAKE_TOOLCHAIN_FILE": "$env{VCPKG_ROOT}/scripts/buildsystems/vcpkg.cmake"
      }
    }
  ]
}
  ```
  ```
{
  "version": 2,
  "configurePresets": [
    {
      "name": "default",
      "inherits": "vcpkg",
      "environment": {
        "VCPKG_ROOT": "<path to vcpkg>"
      }
    }
  ]
}
  ```
  ```
cmake --preset=default
  ```
2. Build the project Run:
  ```
cmake --build build
  ```
3. Run the application Finally, run the executable to see your application in action: `./build/HelloWorld Hello World!` `.\build\HelloWorld.exe Hello World!`

## Next steps

- Tutorial: Package a library with vcpkg
- vcpkg.json Reference
- What is manifest mode?

## Additional resources
