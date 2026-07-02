---
title: "GitHub"
source: https://github.com/google/jsonnet
domain: jsonnet
license: Apache-2.0
tags: jsonnet language, data templating language, json config generation, google jsonnet
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

google

/

jsonnet

Public

- Notifications You must be signed in to change notification settings
- Fork 474
- Star

Branches

Tags

Open more actions menu

## Folders and files

| Name | Name | Last commit message | Last commit date |
|---|---|---|---|
| Latest commit History1,406 Commits1,406 Commits |   |   |   |
| .github/workflows | .github/workflows |   |   |
| benchmarks | benchmarks |   |   |
| case_studies | case_studies |   |   |
| cmd | cmd |   |   |
| core | core |   |   |
| cpp | cpp |   |   |
| doc | doc |   |   |
| editors | editors |   |   |
| examples | examples |   |   |
| gc_stress | gc_stress |   |   |
| include | include |   |   |
| java_comparison | java_comparison |   |   |
| perf_tests | perf_tests |   |   |
| platform_defs | platform_defs |   |   |
| python | python |   |   |
| stdlib | stdlib |   |   |
| test_cmd | test_cmd |   |   |
| test_suite | test_suite |   |   |
| third_party | third_party |   |   |
| tools | tools |   |   |
| .bazelignore | .bazelignore |   |   |
| .bazelversion | .bazelversion |   |   |
| .clang-format | .clang-format |   |   |
| .gitattributes | .gitattributes |   |   |
| .gitignore | .gitignore |   |   |
| CMakeLists.txt | CMakeLists.txt |   |   |
| CONTRIBUTING | CONTRIBUTING |   |   |
| Dockerfile | Dockerfile |   |   |
| LICENSE | LICENSE |   |   |
| MANIFEST.in | MANIFEST.in |   |   |
| MODULE.bazel | MODULE.bazel |   |   |
| MODULE.bazel.lock | MODULE.bazel.lock |   |   |
| Makefile | Makefile |   |   |
| PYTHON_README.md | PYTHON_README.md |   |   |
| README.md | README.md |   |   |
| pyproject.toml | pyproject.toml |   |   |
| release_checklist.md | release_checklist.md |   |   |
| setup.py | setup.py |   |   |
| tests.sh | tests.sh |   |   |
|   |   |   |   |

## Repository files navigation

# Jsonnet - The data templating language

(master branch build status badge)

For an introduction to Jsonnet and documentation, visit our website.

This repository contains the original implementation. You can also try go-jsonnet, a newer implementation which in some cases is orders of magnitude faster, and is recommended in preference to the C++ version.

Visit our discussion forum.

**Security notes:** If you need to process *untrusted inputs* (untrusted Jsonnet code), it is best not to use the C++ implementation, as it is not hardened for that use-case. The expected use-case is for evaluating Jsonnet code that you / your organisation has written and trusts not to be malicious. Even ignoring the risk of exploitable bugs in the implementation, the `import`, `importstr`, and `importbin` language constructs can potentially be used to exfiltrate sensitive data unless you take extra steps to restrict these or sandbox the jsonnet interpreter. By default, these constructs can import from any path accessible to the interpreter process.

## Packages

Jsonnet is available on Homebrew:

```
brew install jsonnet
```

Jsonnet is available on MSYS2:

```
pacman -S mingw-w64-clang-i686-jsonnet
```

```
pacman -S mingw-w64-clang-x86_64-jsonnet
```

```
pacman -S mingw-w64-i686-jsonnet
```

```
pacman -S mingw-w64-x86_64-jsonnet
```

```
pacman -S mingw-w64-ucrt-x86_64-jsonnet
```

The Python binding is on pypi:

```
pip install jsonnet
```

You can also download and install Jsonnet using the vcpkg dependency manager:

```
git clone https://github.com/Microsoft/vcpkg.git
cd vcpkg
./bootstrap-vcpkg.sh
./vcpkg integrate install
vcpkg install jsonnet
```

The Jsonnet port in vcpkg is kept up to date by Microsoft team members and community contributors. If the version is out of date, please create an issue or pull request on the vcpkg repository.

## Building Jsonnet

You can use either GCC or Clang to build Jsonnet. Note that on recent versions of macOS, `/usr/bin/gcc` and `/usr/bin/g++` are actually Clang, so there is no difference.

### Makefile

To build Jsonnet with GCC, run:

```
make
```

To build Jsonnet with Clang, run:

```
make CC=clang CXX=clang++
```

To run the output binary, run:

```
./jsonnet
```

To run the reformatter, run:

```
./jsonnetfmt
```

### Bazel

Bazel builds are also supported. Install Bazel if it is not installed already. Then, run the following command to build with GCC:

```
bazel build -c opt //cmd:all
```

To build with Clang, use one of these two options:

```
env CC=clang CXX=clang++ bazel build -c opt //cmd:all

# OR

bazel build -c opt --action_env=CC=clang --action_env=CXX=clang++ //cmd:all
```

This builds the `jsonnet` and `jsonnetfmt` targets defined in `cmd/BUILD`. To launch the output binaries, run:

```
bazel-bin/cmd/jsonnet
bazel-bin/cmd/jsonnetfmt
```

### CMake

```
cmake . -Bbuild
```

```
cmake --build build --target run_tests
```

## Contributing

See the contributing page on our website.

## Developing Jsonnet

### Running tests

To run the comprehensive suite:

```
make test
```

### Locally serving the website

You need a `doc/js/libjsonnet.wasm` which can either be downloaded from the production website:

```
wget https://jsonnet.org/js/libjsonnet.wasm -O doc/js/libjsonnet.wasm
```

Or you can build it yourself, which requires checking out go-jsonnet. See the README.md in that repo for instructions.

The standard library is documented in a structured format in `doc/_stdlib_gen/stdlib-content.jsonnet`. The HTML (input for Jekyll) is regenerated using the following command:

```
tools/scripts/update_web_content.sh
```

Then, from the root of the repository you can generate and serve the website using Jekyll (you need version 4.3.0 or later):

```
jekyll serve -s doc/
```

This should build and serve the website locally, and automatically rebuild when you change any underlying files.
