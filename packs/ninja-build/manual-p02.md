---
title: "The Ninja build system (part 2/2)"
source: https://ninja-build.org/manual.html
domain: ninja-build
license: CC-BY-SA-4.0
tags: ninja build, build system, build automation, incremental builds
fetched: 2026-07-02
part: 2/2
---

## Dyndep Examples

### Fortran Modules

Consider a Fortran source file `foo.f90` that provides a module `foo.mod` (an implicit output of compilation) and another source file `bar.f90` that uses the module (an implicit input of compilation). This implicit dependency must be discovered before we compile either source in order to ensure that `bar.f90` never compiles before `foo.f90`, and that `bar.f90` recompiles when `foo.mod` changes. We can achieve this as follows:

```
rule f95
  command = f95 -o $out -c $in
rule fscan
  command = fscan -o $out $in

build foobar.dd: fscan foo.f90 bar.f90

build foo.o: f95 foo.f90 || foobar.dd
  dyndep = foobar.dd
build bar.o: f95 bar.f90 || foobar.dd
  dyndep = foobar.dd
```

In this example the order-only dependencies ensure that `foobar.dd` is generated before either source compiles. The hypothetical `fscan` tool scans the source files, assumes each will be compiled to a `.o` of the same name, and writes `foobar.dd` with content such as:

```
ninja_dyndep_version = 1
build foo.o | foo.mod: dyndep
build bar.o: dyndep |  foo.mod
```

Ninja will load this file to add `foo.mod` as an implicit output of `foo.o` and implicit input of `bar.o`. This ensures that the Fortran sources are always compiled in the proper order and recompiled when needed.

### Tarball Extraction

Consider a tarball `foo.tar` that we want to extract. The extraction time can be recorded with a `foo.tar.stamp` file so that extraction repeats if the tarball changes, but we also would like to re-extract if any of the outputs is missing. However, the list of outputs depends on the content of the tarball and cannot be spelled out explicitly in the ninja build file. We can achieve this as follows:

```
rule untar
  command = tar xf $in && touch $out
rule scantar
  command = scantar --stamp=$stamp --dd=$out $in
build foo.tar.dd: scantar foo.tar
  stamp = foo.tar.stamp
build foo.tar.stamp: untar foo.tar || foo.tar.dd
  dyndep = foo.tar.dd
```

In this example the order-only dependency ensures that `foo.tar.dd` is built before the tarball extracts. The hypothetical `scantar` tool will read the tarball (e.g. via `tar tf`) and write `foo.tar.dd` with content such as:

```
ninja_dyndep_version = 1
build foo.tar.stamp | file1.txt file2.txt : dyndep
  restat = 1
```

Ninja will load this file to add `file1.txt` and `file2.txt` as implicit outputs of `foo.tar.stamp`, and to mark the build statement for `restat`. On future builds, if any implicit output is missing the tarball will be extracted again. The `restat` binding tells Ninja to tolerate the fact that the implicit outputs may not have modification times newer than the tarball itself (avoiding re-extraction on every build).
