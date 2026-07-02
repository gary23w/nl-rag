---
title: "Nixpkgs Reference Manual (part 2/6)"
source: https://nixos.org/manual/nixpkgs/stable/
domain: nix-language
license: CC-BY-SA-4.0
tags: nix language, nix lang, nixos, nixpkgs, nix expression
fetched: 2026-07-02
part: 2/6
---

## Using overlays to configure alternatives

Certain software packages have different implementations of the same interface. Other distributions have functionality to switch between these. For example, Debian provides DebianAlternatives. Nixpkgs has what we call `alternatives`, which are configured through overlays.

### BLAS/LAPACK

In Nixpkgs, we have multiple implementations of the BLAS/LAPACK numerical linear algebra interfaces. They are:

- OpenBLASThe Nixpkgs attribute is `openblas` for ILP64 (integer width = 64 bits) and `openblasCompat` for LP64 (integer width = 32 bits). `openblasCompat` is the default.
- LAPACK reference (also provides BLAS and CBLAS)The Nixpkgs attribute is `lapack-reference`.
- Intel MKL (only works on the x86_64 architecture, unfree)The Nixpkgs attribute is `mkl`.
- BLISBLIS, available through the attribute `blis`, is a framework for linear algebra kernels. In addition, it implements the BLAS interface.
- AMD BLIS/LIBFLAME (optimized for modern AMD x86_64 CPUs)The AMD fork of the BLIS library, with attribute `amd-blis`, extends BLIS with optimizations for modern AMD CPUs. The changes are usually submitted to the upstream BLIS project after some time. However, AMD BLIS typically provides some performance improvements on AMD Zen CPUs. The complementary AMD LIBFLAME library, with attribute `amd-libflame`, provides a LAPACK implementation.

Introduced in PR #83888, we are able to override the `blas` and `lapack` packages to use different implementations, through the `blasProvider` and `lapackProvider` argument. This can be used to select a different provider. BLAS providers will have symlinks in `$out/lib/libblas.so.3` and `$out/lib/libcblas.so.3` to their respective BLAS libraries. Likewise, LAPACK providers will have symlinks in `$out/lib/liblapack.so.3` and `$out/lib/liblapacke.so.3` to their respective LAPACK libraries. For example, Intel MKL is both a BLAS and LAPACK provider. An overlay can be created to use Intel MKL that looks like:

```
final: prev:

{
  blas = prev.blas.override { blasProvider = final.mkl; };

  lapack = prev.lapack.override { lapackProvider = final.mkl; };
}
```

This overlay uses Intel’s MKL library for both BLAS and LAPACK interfaces. Note that the same can be accomplished at runtime using `LD_LIBRARY_PATH` of `libblas.so.3` and `liblapack.so.3`. For instance:

```
$ LD_LIBRARY_PATH=$(nix-build -A mkl)/lib${LD_LIBRARY_PATH:+:}$LD_LIBRARY_PATH nix-shell -p octave --run octave
```

Intel MKL requires an `openmp` implementation when running with multiple processors. By default, `mkl` will use Intel’s `iomp` implementation if no other is specified, but this is a runtime-only dependency and binary compatible with the LLVM implementation. To use that one instead, Intel recommends users set it with `LD_PRELOAD`. Note that `mkl` is only available on `x86_64-linux` and `x86_64-darwin`. Moreover, Hydra is not building and distributing pre-compiled binaries using it.

To override `blas` and `lapack` with its reference implementations (i.e. for development purposes), one can use the following overlay:

```
final: prev:

{
  blas = prev.blas.override { blasProvider = final.lapack-reference; };

  lapack = prev.lapack.override { lapackProvider = final.lapack-reference; };
}
```

For BLAS/LAPACK switching to work correctly, all packages must depend on `blas` or `lapack`. This ensures that only one BLAS/LAPACK library is used at one time. There are two versions of BLAS/LAPACK currently in the wild, `LP64` (integer size = 32 bits) and `ILP64` (integer size = 64 bits). The attributes `blas` and `lapack` are `LP64` by default. Their `ILP64` version are provided through the attributes `blas-ilp64` and `lapack-ilp64`. Some software needs special flags or patches to work with `ILP64`. You can check if `ILP64` is used in Nixpkgs with `blas.isILP64` and `lapack.isILP64`. Some software does NOT work with `ILP64`, and derivations need to specify an assertion to prevent this. You can prevent `ILP64` from being used with the following:

```
{
  stdenv,
  blas,
  lapack,
  ...
}:

assert (!blas.isILP64) && (!lapack.isILP64);

stdenv.mkDerivation {
  # ...
}
```

### Switching the MPI implementation

All programs that are built with MPI support use the generic attribute `mpi` as an input. At the moment Nixpkgs natively provides the following MPI implementations:

- Open MPI (default), attribute name `openmpi`
- MPICH, attribute name `mpich`
- MVAPICH, attribute name `mvapich`

To provide MPI enabled applications that use `MPICH`, instead of the default `Open MPI`, use the following overlay:

```
final: prev:

{
  mpi = final.mpich;
}
```


## Overriding

Sometimes one wants to override parts of `nixpkgs`, e.g. derivation attributes, the results of derivations.

These functions are used to make changes to packages, returning only single packages. Overlays, on the other hand, can be used to combine the overridden packages across the entire package set of Nixpkgs.


## <pkg>.override

The function `override` is usually available for all the derivations in the nixpkgs expression (`pkgs`).

It is used to override the arguments passed to a function.

Example usages:

```
pkgs.foo.override {
  arg1 = val1;
  arg2 = val2; # ...
}
```

It’s also possible to access the previous arguments.

```
pkgs.foo.override (previous: {
  arg1 = previous.arg1; # ...
})
```

```
import pkgs.path {
  overlays = [ (self: super: { foo = super.foo.override { barSupport = true; }; }) ];
}
```

```
{
  mypkg = pkgs.callPackage ./mypkg.nix {
    mydep = pkgs.mydep.override {
      # ...
    };
  };
}
```

In the first example, `pkgs.foo` is the result of a function call with some default arguments, usually a derivation. Using `pkgs.foo.override` will call the same function with the given new arguments.

Many packages, like the `foo` example above, provide package options with default values in their arguments, to facilitate overriding. Because it’s not usually feasible to test that packages build with all combinations of options, you might find that a package doesn’t build if you override options to non-default values.

Package maintainers are not expected to fix arbitrary combinations of options. If you find that something doesn’t work, please submit a fix, ideally with a regression test. If you want to ensure that things keep working, consider becoming a maintainer for the package.


## <pkg>.overrideAttrs

The function `overrideAttrs` allows overriding the attribute set passed to a `stdenv.mkDerivation` call, producing a new derivation based on the original one. This function is available on all derivations produced by the `stdenv.mkDerivation` function, which is most packages in the Nixpkgs expression `pkgs`.

Example usages:

```
{
  helloBar = pkgs.hello.overrideAttrs (
    finalAttrs: previousAttrs: { pname = previousAttrs.pname + "-bar"; }
  );
}
```

In the above example, “-bar” is appended to the pname attribute, while all other attributes will be retained from the original `hello` package.

The argument `previousAttrs` is conventionally used to refer to the attr set originally passed to `stdenv.mkDerivation`.

The argument `finalAttrs` refers to the final attributes passed to `mkDerivation`, plus the `finalPackage` attribute which is equal to the result of `mkDerivation` or subsequent `overrideAttrs` calls.

If only a one-argument function is written, the argument has the meaning of `previousAttrs`.

Function arguments can be omitted entirely if there is no need to access `previousAttrs` or `finalAttrs`.

```
{ helloWithDebug = pkgs.hello.overrideAttrs { separateDebugInfo = true; }; }
```

In the above example, the `separateDebugInfo` attribute is overridden to be true, thus building debug info for `helloWithDebug`.

### Note

Note that `separateDebugInfo` is processed only by the `stdenv.mkDerivation` function, not the generated, raw Nix derivation. Thus, using `overrideDerivation` will not work in this case, as it overrides only the attributes of the final derivation. It is for this reason that `overrideAttrs` should be preferred in (almost) all cases to `overrideDerivation`, i.e. to allow using `stdenv.mkDerivation` to process input arguments, as well as the fact that it is easier to use (you can use the same attribute names you see in your Nix code, instead of the ones generated (e.g. `buildInputs` vs `nativeBuildInputs`), and it involves less typing).


## <pkg>.overrideDerivation

### Warning

You should prefer `overrideAttrs` in almost all cases, see its documentation for the reasons why. `overrideDerivation` is not deprecated and will continue to work, but is less nice to use and does not have as many abilities as `overrideAttrs`.

### Warning

Do not use this function in Nixpkgs as it evaluates a derivation before modifying it, which breaks package abstraction. In addition, this evaluation-per-function application incurs a performance penalty, which can become a problem if many overrides are used. It is only intended for ad-hoc customisation, such as in `~/.config/nixpkgs/config.nix`.

The function `overrideDerivation` creates a new derivation based on an existing one by overriding the original’s attributes with the attribute set produced by the specified function. This function is available on all derivations defined using the `makeOverridable` function. Most standard derivation-producing functions, such as `stdenv.mkDerivation`, are defined using this function, which means most packages in the Nixpkgs expression, `pkgs`, have this function.

Example usage:

```
{
  mySed = pkgs.gnused.overrideDerivation (oldAttrs: {
    name = "sed-4.2.2-pre";
    src = fetchurl {
      url = "ftp://alpha.gnu.org/gnu/sed/sed-4.2.2-pre.tar.bz2";
      hash = "sha256-MxBJRcM2rYzQYwJ5XKxhXTQByvSg5jZc5cSHEZoB2IY=";
    };
    patches = [ ];
  });
}
```

In the above example, the `name`, `src`, and `patches` of the derivation will be overridden, while all other attributes will be retained from the original derivation.

The argument `oldAttrs` is used to refer to the attribute set of the original derivation.

### Note

A package’s attributes are evaluated *before* being modified by the `overrideDerivation` function. For example, the `name` attribute reference in `url = "mirror://gnu/hello/${name}.tar.gz";` is filled-in *before* the `overrideDerivation` function modifies the attribute set. This means that overriding the `name` attribute, in this example, *will not* change the value of the `url` attribute. Instead, we need to override both the `name` *and* `url` attributes.


## lib.makeOverridable

The function `lib.makeOverridable` is used to make the result of a function easily customizable. This utility only makes sense for functions that accept an argument set and return an attribute set.

Example usage:

```
{
  f =
    { a, b }:
    {
      result = a + b;
    };
  c = lib.makeOverridable f {
    a = 1;
    b = 2;
  };
}
```

The variable `c` is the value of the `f` function applied with some default arguments. Hence the value of `c.result` is `3`, in this example.

The variable `c` however also has some additional functions, like c.override which can be used to override the default arguments. In this example the value of `(c.override { a = 4; }).result` is 6.

# Nixpkgs `lib`


## Functions reference

The Nixpkgs repository has several utility functions to manipulate Nix expressions.
