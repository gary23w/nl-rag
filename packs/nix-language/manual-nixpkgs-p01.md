---
title: "Nixpkgs Reference Manual (part 1/6)"
source: https://nixos.org/manual/nixpkgs/stable/
domain: nix-language
license: CC-BY-SA-4.0
tags: nix language, nix lang, nixos, nixpkgs, nix expression
fetched: 2026-07-02
part: 1/6
---

# Nixpkgs Reference Manual


## Version 26.05pre-git

**List of Examples**

**1. Map over leaf attributes**

**2. Map over an leaf attributes defined by a condition**

**3. Create an interdependent package set on top of `pkgs`**

**4. Using `callPackage` from a scope**

**5. Enable debug symbols for use with GDB**

**6. Setting and accessing `passthru` attributes**

**7. Example definition of `mkLocalDerivation` extended from `stdenv.mkDerivation` with `lib.extendMkDerivation`**

**8. Update source hash with the fake hash method**

**9. Using `fetchurl` to download a file**

**10. Using `fetchurl` to download a file with multiple possible URLs**

**11. Manipulating the content downloaded by `fetchurl`**

**12. Using `fetchzip` to output contents directly**

**13. Using `fetchzip` to decompress a `.rar` file**

**14. Use `sparseCheckout` to only include some directories:**

**15. Invocation of `runCommandWith`**

**16. Invocation of `runCommand`**

**17. Usage 1 of `makeDesktopItem`**

**18. Usage 2 of `makeDesktopItem`**

**19. Usage 1 of `writeTextFile`**

**20. Usage 2 of `writeTextFile`**

**21. Usage 3 of `writeTextFile`**

**22. Usage of `writeText`**

**23. Usage of `writeTextDir`**

**24. Usage of `writeScript`**

**25. Usage of `writeScriptBin`**

**26. Usage of `writeShellScript`**

**27. Usage of `writeShellScriptBin`**

**28. Usage of `writeShellApplication`**

**29. Check that `pkg-config` modules are exposed using default values**

**30. Check that `pkg-config` modules are exposed using explicit module names**

**31. Check that `*config.cmake` modules are exposed using explicit module names**

**32. Check hyperlinks in the `nix` documentation**

**33. Run `testers.shellcheck`**

**34. Run `testers.shfmt`**

**35. Check a program version using all the default values**

**36. Check the program version using a specified command and expected version string**

**37. Check that a build fails, and verify the changes made during build**

**38. Check that a build fails, and verify the changes made during build**

**39. Check that two paths have the same contents**

**40. Test a function which appends a value to an array**

**41. Check that two packages produce the same derivation**

**42. Prevent nix from reusing the output of a fetcher**

**43. Run a command with network access**

**44. Run a NixOS test using `runNixOSTest`**

**45. Using `fakeNss` with `dockerTools.buildImage`**

**46. Using `fakeNss` with an override to add extra lines**

**47. Wrapping an AppImage from GitHub**

**48. Wrapping an AppImage with extra packages**

**49. Extracting an AppImage to install extra files**

**50. Extracting an AppImage to install extra files, using `postExtract`**

**51. Building a Docker image**

**52. Building a Docker image with `runAsRoot`**

**53. Building a Docker image with `extraCommands`**

**54. Building a Docker image with a creation date set to the current time**

**55. Building a layered Docker image**

**56. Streaming a layered Docker image**

**57. Exploring the layers in an image built with `streamLayeredImage`**

**58. Building a layered Docker image with packages directly in `config`**

**59. Pulling the nixos/nix Docker image from the default registry**

**60. Pulling the nixos/nix Docker image from a specific registry**

**61. Finding the digest and hash values to use for `dockerTools.pullImage`**

**62. Exporting a Docker image with `dockerTools.exportImage`**

**63. Importing an archive built with `dockerTools.exportImage` in Docker**

**64. Exploring output naming with `dockerTools.exportImage`**

**65. Using `dockerTools.exportImage` with a path as `fromImage`**

**66. Using `dockerTools`’s environment helpers with `buildImage`**

**67. Using `dockerTools`’s environment helpers with `buildLayeredImage`**

**68. Using `dockerTools.shadowSetup` with `dockerTools.buildImage`**

**69. Using `dockerTools.shadowSetup` with `dockerTools.buildLayeredImage`**

**70. Building a Docker image with `buildNixShellImage` with the build environment for the `hello` package**

**71. Building a Docker image with `streamNixShellImage` with the build environment for the `hello` package**

**72. Adding extra packages to a Docker image built with `streamNixShellImage`**

**73. Adding a `shellHook` to a Docker image built with `streamNixShellImage`**

**74. Creating an OCI runtime container that runs `bash`**

**75. Building a Portable Service image**

**76. Specifying symlinks when building a Portable Service image**

**77. Copying a package and its closure to another machine with `mkBinaryCache`**

**78. Using `npmHooks`**

**79. Navigate Java compiler variants in `javaPackages` with `nix repl`**

**80. List all Python packages in Nixpkgs**

**81. Ephemeral shell**

**82. Declarative shell**

**83. Using `pkgs.zlib.override {}`**

**84. Using `pkgs.buildEmscriptenPackage {}`**

**85. Overriding the kernel derivation**

**86. Using `pkgs.linuxPackages_custom` with a specific source, version, and config file**

**87. Edit-compile-run loop when developing `mellanox` drivers**

**88. Usage of `pkgs.substitute`**

**89. Usage of `pkgs.replaceVars`**

**90. Usage of `pkgs.replaceVarsWith`**

# Preface

The Nix Packages collection (Nixpkgs) is a set of thousands of packages for the Nix package manager, released under a permissive MIT license. Packages are available for several platforms, and can be used with the Nix package manager on most GNU/Linux distributions as well as NixOS.

This document is the user *reference* manual for Nixpkgs. It describes the entire public interface of Nixpkgs in a concise and orderly manner, and all relevant behaviors, with examples and cross-references.

To discover other kinds of documentation:

- nix.dev: Tutorials and guides for getting things done with Nix
- NixOS **Option Search** and reference documentation
- Nixpkgs **Package Search**
- **NixOS** manual: Reference documentation for the NixOS Linux distribution
- `CONTRIBUTING.md`: Contributing to Nixpkgs, including this manual

# Overview of Nixpkgs

Nix expressions describe how to build packages from source and are collected in the Nixpkgs repository. Also included in the collection are Nix expressions for NixOS modules. With these expressions the Nix package manager can build binary packages.

Packages, including the Nix packages collection, are distributed through channels. The collection is distributed for users of Nix on non-NixOS distributions through the channel `nixpkgs-unstable`. Users of NixOS generally use one of the `nixos-*` channels, e.g., `nixos-22.11`, which includes all packages and modules for the stable NixOS 22.11. Stable NixOS releases are generally only given security updates. More up-to-date packages and modules are available via the `nixos-unstable` channel.

Both `nixos-unstable` and `nixpkgs-unstable` follow the `master` branch of the Nixpkgs repository, although both do lag the `master` branch by generally a couple of days. Updates to a channel are distributed as soon as all tests for that channel pass, e.g., this table shows the status of tests for the `nixpkgs-unstable` channel.

The tests are conducted by a cluster called Hydra, which also builds binary packages from the Nix expressions in Nixpkgs for `x86_64-linux`, `aarch64-linux`, `x86_64-darwin` and `aarch64-darwin`. The binaries are made available via a binary cache.

The current Nix expressions of the channels are available in the Nixpkgs repository in branches that correspond to the channel names (e.g., `nixos-22.11-small`).

# Using Nixpkgs


## Platform Support

Packages receive varying degrees of support, both in terms of maintainer attention and available computation resources for continuous integration (CI). We have 7 defined tiers denoting how well supported each platform is.


## Tiers

### Tier 1

Tier 1 platforms receive the highest level of support where problems can block updates, platform-specific patches are freely applied, and most packages are expected to work.

### Tier 2

Tier 2 platforms are expected to remain functional with updates, receive platform-specific patches as needed, and have many packages built by Hydra with full ofBorg support.

### Tier 3

Tier 3 platforms may receive non-intrusive platform-specific fixes, have native bootstrap tools available with cross-build toolchains in binary cache, but updates might break builds on these platforms.

### Tier 4-7

Platform Tiers 4 through 7 indicate varying levels of minimal support going from receiving only limited fixes to platforms with no support, but a path to support.


## Breakdown

| Triple | Support Tier | Channel Blockers | Hydra Support | Ofborg Support | Bootstrap Tarballs | Cross Compiling Support |
|---|---|---|---|---|---|---|
| `x86_64-unknown-linux-gnu` | Tier 1 | Many | ✔️ | ✔️ | ✔️ | ✔️ |
| `aarch64-unknown-linux-gnu` | Tier 2 | Some | ✔️ | ✔️ | ✔️ | ✔️ |
| `x86_64-unknown-linux-musl` | Tier 3 | None | Limited | ❌ | ✔️ | ✔️ |
| `aarch64-unknown-linux-musl` | Tier 3 | None | Limited | ❌ | ✔️ | ✔️ |
| `x86_64-unknown-unknown-freebsd` | Tier 3 | None | ❌ | ❌ | ✔️ | ✔️ |
| `arm64-apple-darwin` | Tier 2 | Some | ✔️ | ✔️ | ✔️ | ❌* |
| `x86_64-apple-darwin` | Tier 2 | Some | ✔️ | ✔️ | ✔️ | ❌* |
| `i686-unknown-linux-gnu` | Tier 3 | None | Limited | ❌ | ✔️ | ✔️ |
| `riscv32-unknown-linux-gnu` | Tier 4 | None | ❌ | ❌ | ❌ | ✔️ |
| `riscv64-unknown-linux-gnu` | Tier 3 | None | ❌ | ❌ | ✔️ | ✔️ |
| `loongarch64-unknown-linux-gnu` | Tier 3 | None | ❌ | ❌ | ✔️ | ✔️ |
| `armv6l-unknown-linux-gnueabihf` | Tier 3 | None | ❌ | ❌ | ✔️ | ✔️ |
| `armv6l-unknown-linux-musleabihf` | Tier 3 | None | ❌ | ❌ | ✔️ | ✔️ |
| `armv7l-unknown-linux-gnueabihf` | Tier 3 | None | ❌ | ❌ | ✔️ | ✔️ |
| `armv5tel-unknown-linux-gnueabi` | Tier 3 | None | ❌ | ❌ | ✔️ | ✔️ |
| `mips64el-unknown-linux-gnuabi64` | Tier 3 | None | ❌ | ❌ | ✔️ | ✔️ |
| `mips64el-unknown-linux-gnuabin32` | Tier 3 | None | ❌ | ❌ | ✔️ | ✔️ |
| `mipsel-unknown-linux-gnu` | Tier 3 | None | ❌ | ❌ | ✔️ | ✔️ |
| `powerpc64-unknown-linux-gnuabielfv2` | Tier 3 | None | ❌ | ❌ | ✔️ | ✔️ |
| `powerpc64le-unknown-linux-gnu` | Tier 3 | None | ❌ | ❌ | ✔️ | ✔️ |
| `s390x-unknown-linux-gnu` | Tier 3 | None | ❌ | ❌ | ✔️ | ✔️ |

* - Cross compiling is only supported on Darwin hosts.


## Global configuration

Nix comes with certain defaults about which packages can and cannot be installed, based on a package’s metadata. By default, Nix will prevent installation if any of the following criteria are true:

- The package is thought to be broken, and has had its `meta.broken` set to `true`.
- The package isn’t intended to run on the given system, as none of its `meta.platforms` match the given system.
- The package’s `meta.license` is set to a license which is considered to be unfree.
- The package has known security vulnerabilities but has not or can not be updated for some reason, and a list of issues has been entered into the package’s `meta.knownVulnerabilities`.
- There are problems for packages which must be acknowledged, e.g. deprecation notices.

Each of these criteria can be altered in the Nixpkgs configuration.

### Note

All this is checked during evaluation already, and the check includes any package that is evaluated. In particular, all build-time dependencies are checked.

A user’s Nixpkgs configuration is stored in a user-specific configuration file located at `~/.config/nixpkgs/config.nix`. For example:

```
{ allowUnfree = true; }
```

### Caution

Unfree software is not tested or built in Nixpkgs continuous integration, and therefore not cached. Most unfree licenses prohibit either executing or distributing the software.

The `NIXPKGS_CONFIG` environment variable can override the configuration file location. Nixpkgs resolves the config in this order:

1. `$NIXPKGS_CONFIG`, if set and the file exists.
2. `~/.config/nixpkgs/config.nix`, if it exists.
3. `~/.nixpkgs/config.nix` (legacy), if it exists.
4. Empty configuration.

On NixOS, `NIXPKGS_CONFIG` points to `/etc/nix/nixpkgs-config.nix` system-wide. Drop a file there to apply configuration to `nix-env`, `nix-shell`, and other user-level commands. NixOS does not create this file. The `nixpkgs.config` option does not affect `nix-env`, `nix-shell`, or other user-level commands.

This lookup applies to non-flake usage like channels and `<nixpkgs>`. Flakes ignore it; pass `config` directly when importing `nixpkgs`.


## Installing broken packages

There are several ways to try compiling a package which has been marked as broken.

- For allowing the build of a broken package once, you can use an environment variable for a single invocation of the nix tools:
  ```
$ export NIXPKGS_ALLOW_BROKEN=1
  ```
- For permanently allowing broken packages with a specific name to be built, you may add a corresponding `problems.handlers` to your user’s configuration file, for example:
  ```
{
  problems.handlers.hello.broken = "warn"; # or "ignore"
}
  ```
- For permanently allowing all broken packages to be built, you may add `allowBroken = true;` to your user’s configuration file, like this:
  ```
{ allowBroken = true; }
  ```


## Installing packages on unsupported systems

There are also two ways to try compiling a package which has been marked as unsupported for the given system.

- For allowing the build of an unsupported package once, you can use an environment variable for a single invocation of the nix tools:
  ```
$ export NIXPKGS_ALLOW_UNSUPPORTED_SYSTEM=1
  ```
- For permanently allowing unsupported packages to be built, you may add `allowUnsupportedSystem = true;` to your user’s configuration file, like this:
  ```
{ allowUnsupportedSystem = true; }
  ```

The difference between a package being unsupported on some system and being broken is admittedly a bit fuzzy. If a program *ought* to work on a certain platform, but doesn’t, the platform should be included in `meta.platforms`, but marked as broken with e.g. `meta.broken = !hostPlatform.isWindows`. Of course, this begs the question of what “ought” means exactly. That is left to the package maintainer.


## Installing unfree packages

All users of Nixpkgs are free software users, and many users (and developers) of Nixpkgs want to limit and tightly control their exposure to unfree software. At the same time, many users need (or want) to run some specific pieces of proprietary software. Nixpkgs includes some expressions for unfree software packages. By default unfree software cannot be installed and doesn’t show up in searches.

There are several ways to tweak how Nix handles a package which has been marked as unfree.

- To temporarily allow all unfree packages, you can use an environment variable for a single invocation of the nix tools:
  ```
$ export NIXPKGS_ALLOW_UNFREE=1
  ```
- It is possible to permanently allow individual unfree packages, while still blocking unfree packages by default using the `allowUnfreePredicate` configuration option in the user configuration file.This option is a function which accepts a package as a parameter, and returns a boolean. The following example configuration accepts a package and always returns false:For a more useful example, try the following. This configuration only allows unfree packages named roon-server and Visual Studio Code:
  ```
{ allowUnfreePredicate = (pkg: false); }
  ```
  ```
{
  allowUnfreePredicate =
    pkg:
    builtins.elem (lib.getName pkg) [
      "roon-server"
      "vscode"
    ];
}
  ```
- It is also possible to allow and block licenses that are specifically acceptable or not acceptable, using `allowlistedLicenses` and `blocklistedLicenses`, respectively.The following example configuration allowlists the licenses `amd` and `wtfpl`:The following example configuration blocklists the `gpl3Only` and `agpl3Only` licenses:Note that `allowlistedLicenses` only applies to unfree licenses unless `allowUnfree` is enabled. It is not a generic allowlist for all types of licenses. `blocklistedLicenses` applies to all licenses.
  ```
{
  allowlistedLicenses = with lib.licenses; [
    amd
    wtfpl
  ];
}
  ```
  ```
{
  blocklistedLicenses = with lib.licenses; [
    agpl3Only
    gpl3Only
  ];
}
  ```

A complete list of licenses can be found in the file `lib/licenses.nix` of the nixpkgs tree.


## Installing insecure packages

There are several ways to tweak how Nix handles a package which has been marked as insecure.

- To temporarily allow all insecure packages, you can use an environment variable for a single invocation of the nix tools:
  ```
$ export NIXPKGS_ALLOW_INSECURE=1
  ```
- It is possible to permanently allow individual insecure packages, while still blocking other insecure packages by default using the `permittedInsecurePackages` configuration option in the user configuration file.The following example configuration permits the installation of the hypothetically insecure package `hello`, version `1.2.3`:
  ```
{ permittedInsecurePackages = [ "hello-1.2.3" ]; }
  ```
- It is also possible to create a custom policy around which insecure packages to allow and deny, by overriding the `allowInsecurePredicate` configuration option.The `allowInsecurePredicate` option is a function which accepts a package and returns a boolean, much like `allowUnfreePredicate`.The following configuration example allows any version of the `ovftool` package:Note that `permittedInsecurePackages` is only checked if `allowInsecurePredicate` is not specified.
  ```
{ allowInsecurePredicate = pkg: builtins.elem (lib.getName pkg) [ "ovftool" ]; }
  ```


## Packages with problems

A package may have several problems associated with it. These can be either manually declared in `meta.problems`, or automatically generated from its other `meta` attributes. Each problem has a name, a “kind”, a message, and optionally a list of URLs. Not all kinds can be manually specified in `meta.problems`, and some kinds can exist only up to once per package. Currently, the following problem kinds are known (with more reserved to be added in the future):

- “removal”: The package is planned to be removed some time in the future. Unique.
- “deprecated”: The package relies on software which has reached its end of life.
- “maintainerless”: Automatically generated for packages with `meta.maintainers == []`. Unique, not manually specifiable.
- “broken”: Automatically generated for packages with `meta.broken = true`.

Each problem has a handler that deals with it, which can be one of “error”, “warn” or “ignore”. “error” will disallow evaluating a package, while “warn” will simply print a message to the log.

The handler for problems can be specified using `config.problems.handlers.${packageName}.${problemName} = "${handler}";`.

There is also the possibility to specify some generic matchers, which can set a handler for more than a specific problem of a specific package. This works through the `config.problems.matchers` option:

```
{
  problems.matchers = [
    # Fail to build any packages which are about to be removed anyway
    {
      kind = "removal";
      handler = "error";
    }

    # Get warnings when using packages with no declared maintainers
    {
      kind = "maintainerless";
      handler = "warn";
    }

    # You deeply care about this package and want to absolutely know when it has any problems
    {
      package = "hello";
      handler = "error";
    }
  ];
}
```

Matchers can match one or more of package name, problem name or problem kind. If multiple conditions are present, all must be met to match. If multiple matchers match a problem, then the highest severity handler will be chosen. The current default value contains `{ kind = "removal"; handler = "warn"; }`, meaning that people will be notified about package removals in advance.

Package names for both `problems.handlers` and `problems.matchers` are taken from `lib.getName`, which looks at the `pname` first and falls back to extracting the “pname” part from the `name` attribute.


## Modify packages via `packageOverrides`

You can define a function called `packageOverrides` in your local `~/.config/nixpkgs/config.nix` to override Nix packages. It must be a function that takes pkgs as an argument and returns a modified set of packages.

```
{
  packageOverrides = pkgs: rec {
    foo = pkgs.foo.override {
      # ...
    };
  };
}
```


## `config` Options Reference

The following attributes can be passed in `config`.

**`enableParallelBuildingByDefault`**

Whether to set `enableParallelBuilding` to true by default while building nixpkgs packages. Changing the default may cause a mass rebuild.

*Type:* boolean

*Default:*

```
false
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`allowAliases`**

Whether to expose old attribute names for compatibility.

The recommended setting is to enable this, as it improves backward compatibility, easing updates.

The only reason to disable aliases is for continuous integration purposes. For instance, Nixpkgs should not depend on aliases in its internal code. Projects that aren’t Nixpkgs should be cautious of instantly removing all usages of aliases, as migrating too soon can break compatibility with the stable Nixpkgs releases.

*Type:* boolean

*Default:*

```
true
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`allowBroken`**

Whether to allow broken packages.

See Installing broken packages in the NixOS manual.

*Type:* boolean

*Default:*

```
false || builtins.getEnv "NIXPKGS_ALLOW_BROKEN" == "1"
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`allowDeprecatedx86_64Darwin`**

Silence the warning for the upcoming deprecation of the `x86_64-darwin` platform in Nixpkgs 26.11.

See the release notes for more information.

*Type:* boolean

*Default:*

```
false
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`allowUnfree`**

Whether to allow unfree packages.

See Installing unfree packages in the NixOS manual.

*Type:* boolean

*Default:*

```
false || builtins.getEnv "NIXPKGS_ALLOW_UNFREE" == "1"
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`allowUnfreePackages`**

Allows specific unfree packages to be used.

This option composes with `nixpkgs.config.allowUnfreePredicate` by also allowing the listed package names.

Unlike `nixpkgs.config.allowUnfreePredicate`, this option merges additively, similar to `environment.systemPackages`. This enables defining allowed unfree packages in multiple modules, close to where they are used.

This avoids the need to centralize all unfree package declarations or globally enable unfree packages via `nixpkgs.config.allowUnfree = true`.

*Type:* list of string

*Default:*

```
[ ]
```

*Example:*

```
[
  "ut1999"
]
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`allowUnsupportedSystem`**

Whether to allow unsupported packages.

See Installing packages on unsupported systems in the NixOS manual.

*Type:* boolean

*Default:*

```
false || builtins.getEnv "NIXPKGS_ALLOW_UNSUPPORTED_SYSTEM" == "1"
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`allowVariants`**

Whether to expose the nixpkgs variants.

Variants are instances of the current nixpkgs instance with different stdenvs or other applied options. This allows for using different toolchains, libcs, or global build changes across nixpkgs. Disabling can ensure nixpkgs is only building for the platform which you specified.

*Type:* boolean

*Default:*

```
true
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`checkMeta`**

Whether to check that the `meta` attribute of derivations are correct during evaluation time.

*Type:* boolean

*Default:*

```
false
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`configurePlatformsByDefault`**

Whether to set `configurePlatforms` to `["build" "host"]` by default while building nixpkgs packages. Changing the default may cause a mass rebuild.

*Type:* boolean

*Default:*

```
false
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`contentAddressedByDefault`**

Whether to set `__contentAddressed` to true by default while building nixpkgs packages. Changing the default may cause a mass rebuild.

*Type:* boolean

*Default:*

```
false
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`cudaCapabilities`**

A list of CUDA capabilities to build for.

Packages may use this option to control device code generation to take advantage of architecture-specific functionality, speed up compile times by producing less device code, or slim package closures.

For example, you can build for Ada Lovelace GPUs with `cudaCapabilities = [ "8.9" ];`.

If not provided, the default value is calculated per-package set, derived from a list of GPUs supported by that CUDA version.

See the CUDA section in the Nixpkgs manual for more information.

*Type:* list of string

*Default:*

```
[ ]
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`cudaForwardCompat`**

Whether to enable PTX support for future hardware.

When enabled, packages will include PTX code that can be JIT-compiled for GPUs newer than those explicitly targeted by `cudaCapabilities`.

*Type:* boolean

*Default:*

```
true
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`cudaSupport`**

Whether to build packages with CUDA support by default while building nixpkgs packages. Changing the default may cause a mass rebuild.

*Type:* boolean

*Default:*

```
false
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`doCheckByDefault`**

Whether to run `checkPhase` by default while building nixpkgs packages. Changing the default may cause a mass rebuild.

*Type:* boolean

*Default:*

```
false
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`fetchedSourceNameDefault`**

This controls the default derivation `name` attribute set by the `fetch*` (`fetchzip`, `fetchFromGitHub`, etc) functions.

Possible values and the resulting `.name`:

- `"source"` -> `"source"`
- `"versioned"` -> `"${repo}-${rev}-source"`
- `"full"` -> `"${repo}-${rev}-${fetcherName}-source"`

The default `"source"` is the best choice for minimal rebuilds, it will ignore any non-hash changes (like branches being renamed, source URLs changing, etc) at the cost of `/nix/store` being easily cache-poisoned (see NixOS/nix#969).

Setting this to `"versioned"` greatly helps with discoverability of sources in `/nix/store` and makes cache-poisoning of `/nix/store` much harder, at the cost of a single mass-rebuild for all `src` derivations, and an occasional rebuild when a source changes some of its non-hash attributes.

Setting this to `"full"` is similar to setting it to `"versioned"`, but the use of `fetcherName` in the derivation name will force a rebuild when `src` switches between `fetch*` functions, thus forcing `nix` to check new derivation’s `outputHash`, which is useful for debugging.

Also, `"full"` is useful for easy collection and tracking of statistics of where the packages you use are hosted.

If you are a developer, you should probably set this to at least`"versioned"`.

Changing the default will cause a mass rebuild.

*Type:* one of “source”, “versioned”, “full”

*Default:*

```
"source"
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`gitConfig`**

The default git configuration for all `pkgs.fetchgit` calls.

Among many other potential uses, this can be used to override URLs to point to local mirrors.

Changing this will not cause any rebuilds because `pkgs.fetchgit` produces a fixed-output derivation.

To set the configuration file directly, use the `gitConfigFile` option instead.

To set the configuration file for individual calls, use `fetchgit { gitConfigFile = "..."; }`.

*Type:* attribute set of attribute set of anything

*Default:*

```
{ }
```

*Example:*

```
{
  url = {
    "https://my-github-mirror.local" = {
      insteadOf = [
        "https://github.com"
      ];
    };
  };
}
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`gitConfigFile`**

A path to a git configuration file, to be used for all `pkgs.fetchgit` calls.

This overrides the `gitConfig` option, see its documentation for more details.

*Type:* null or absolute path

*Default:*

```
null
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`hashedMirrors`**

The set of content-addressed/hashed mirror URLs used by `pkgs.fetchurl`. In case `pkgs.fetchurl` can’t download from the given URLs, it will try the hashed mirrors based on the expected output hash.

See `copy-tarballs.pl` for more details on how hashed mirrors are constructed.

*Type:* list of string

*Default:*

```
[
  "https://tarballs.nixos.org"
]
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`microsoftVisualStudioLicenseAccepted`**

If the Microsoft Visual Studio license has been accepted.

Please read https://www.visualstudio.com/license-terms/mt644918/ and enable this config if you accept.

*Type:* boolean

*Default:*

```
false || builtins.getEnv "NIXPKGS_ALLOW_UNFREE" == "1"
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`npmRegistryOverrides`**

The default npm registry overrides for all `fetchNpmDeps` calls, as an attribute set.

For each attribute, all files fetched from the host corresponding to the name will instead be fetched from the host (and sub-path) specified in the value.

For example, an override like `"registry.npmjs.org" = "my-mirror.local/registry.npmjs.org"` will replace a URL like `https://registry.npmjs.org/foo.tar.gz` with `https://my-mirror.local/registry.npmjs.org/foo.tar.gz`.

To set the string directly, see `npmRegistryOverridesString`.

*Type:* attribute set of string

*Default:*

```
{ }
```

*Example:*

```
{
  "registry.npmjs.org" = "my-mirror.local/registry.npmjs.org";
}
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`npmRegistryOverridesString`**

A string containing a string with a JSON representation of npm registry overrides for `fetchNpmDeps`.

This overrides the `npmRegistryOverrides` option, see its documentation for more details.

*Type:* string

*Default:*

```
"{}"
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`problems.handlers`**

Specify how to handle packages with problems. Each key has the format `packageName.problemName`, each value is one of “error”, “warn” or “ignore”.

This option takes precedence over anything in `problems.matchers`.

Package names are taken from `lib.getName`, which looks at the `pname` first and falls back to extracting the “pname” part from the `name` attribute.

See <link xlink:href=“https://nixos.org/manual/nixpkgs/stable/#sec-ignore-problems”>Installing packages with problems</link> in the NixOS manual.

*Type:* attribute set of attribute set of (one of “ignore”, “warn”, “error”)

*Default:*

```
{ }
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`problems.matchers`**

A more powerful and less ergonomic version of `problems.handlers`. Each value is a matcher, that may match onto certain properties of a problem and specify a handler for them.

If multiple matchers match a problem, the handler with the highest severity (error > warn > ignore) will be used. Values in `problems.handlers` always take precedence over matchers.

Any matchers must not contain both a `package` and `name` field, for this should be handled by using `problems.handlers` instead.

*Type:* list of (submodule)

*Default:*

```
[ ]
```

*Example:*

```
[
  {
    handler = "warn";
    kind = "maintainerless";
  }
  {
    handler = "error";
    package = "myPackageICareAbout";
  }
]
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`problems.matchers.*.package`**

Match problems of packages with this name

*Type:* null or string

*Default:*

```
null
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`problems.matchers.*.handler`**

Specify the handler for matched problems

*Type:* one of “ignore”, “warn”, “error”

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`problems.matchers.*.kind`**

Match problems of this problem kind

*Type:* null or one of “maintainerless”, “broken”, “removal”, “deprecated”, “broken”

*Default:*

```
null
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`problems.matchers.*.name`**

Match problems with this problem name

*Type:* null or string

*Default:*

```
null
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`recursionMode`**

In which way to recurse through Nixpkgs. In most cases you want keep this as the default. You can use this to emulate how `hydra` and `search` are going through Nixpkgs.

*Type:* one of “hydra”, “eval”, “search”

*Default:*

```
"eval"
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`replaceBootstrapFiles`**

Use the bootstrap files returned instead of the default bootstrap files. The default bootstrap files are passed as an argument. Changing the default may cause a mass rebuild.

*Type:* function that evaluates to a(n) attribute set of package

*Default:*

```
lib.id
```

*Example:*

```
prevFiles:
let
  replacements = {
    "sha256-YQlr088HPoVWBU2jpPhpIMyOyoEDZYDw1y60SGGbUM0=" = import <nix/fetchurl.nix> {
      url = "(custom glibc linux x86_64 bootstrap-tools.tar.xz)";
      hash = "(...)";
    };
    "sha256-QrTEnQTBM1Y/qV9odq8irZkQSD9uOMbs2Q5NgCvKCNQ=" = import <nix/fetchurl.nix> {
      url = "(custom glibc linux x86_64 busybox)";
      hash = "(...)";
      executable = true;
    };
  };
in
builtins.mapAttrs (name: prev: replacements.${prev.outputHash} or prev) prevFiles
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`replaceStdenv`**

A function to replace the standard environment (stdenv).

The function receives an attribute set with `pkgs` and should return a stdenv derivation.

This can be used to globally replace the stdenv with a custom one, for example to use ccache or distcc. Changing the default may cause a mass rebuild.

*Type:* null or (function that evaluates to a(n) package)

*Default:*

```
null
```

*Example:*

```
{ pkgs }: pkgs.ccacheStdenv
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`rewriteURL`**

A hook to rewrite/filter URLs before they are fetched.

The function is passed the URL as a string, and is expected to return a new URL, or null if the given URL should not be attempted.

This function is applied *prior* to resolving mirror:// URLs.

The intended use is to allow URL rewriting to insert company-internal mirrors, or work around company firewalls and similar network restrictions.

*Type:* function that evaluates to a(n) (null or string)

*Default:*

```
(url: url)
```

*Example:*

```
{
  # Use Nix like it's 2024! ;-)
  rewriteURL = url: "https://web.archive.org/web/2024/${url}";
}
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`rocmSupport`**

Whether to build packages with ROCm support by default while building nixpkgs packages. Changing the default may cause a mass rebuild.

*Type:* boolean

*Default:*

```
false
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`showDerivationWarnings`**

Which warnings to display for potentially dangerous or deprecated values passed into `stdenv.mkDerivation`.

A list of warnings can be found in /pkgs/stdenv/generic/check-meta.nix.

This is not a stable interface; warnings may be added, changed or removed without prior notice.

*Type:* list of value “maintainerless” (singular enum)

*Default:*

```
[ ]
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`strictDepsByDefault`**

Whether to set `strictDeps` to true by default while building nixpkgs packages. Changing the default may cause a mass rebuild.

*Type:* boolean

*Default:*

```
false
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`structuredAttrsByDefault`**

Whether to set `__structuredAttrs` to true by default while building nixpkgs packages. Changing the default may cause a mass rebuild.

*Type:* boolean

*Default:*

```
false
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|

**`warnUndeclaredOptions`**

Whether to warn when `config` contains an unrecognized attribute.

*Type:* boolean

*Default:*

```
false
```

*Declared by:*

| `pkgs/top-level/config.nix` |
|---|


## Declarative Package Management

### Build an environment

Using `packageOverrides`, it is possible to manage packages declaratively. This means that we can list all of our desired packages within a declarative Nix expression. For example, to have `aspell`, `bc`, `ffmpeg`, `coreutils`, `gdb`, `nix`, `emscripten`, `jq`, `nox`, and `silver-searcher`, we could use the following in `~/.config/nixpkgs/config.nix`:

```
{
  packageOverrides =
    pkgs: with pkgs; {
      myPackages = pkgs.buildEnv {
        name = "my-packages";
        paths = [
          aspell
          bc
          coreutils
          gdb
          ffmpeg
          nix
          emscripten
          jq
          nox
          silver-searcher
        ];
      };
    };
}
```

To install it into our environment, you can just run `nix-env -iA nixpkgs.myPackages`. If you want to load the packages to be built from a working copy of `nixpkgs` you just run `nix-env -f. -iA myPackages`. To explore what’s been installed, just look through `~/.nix-profile/`. You can see that a lot of stuff has been installed. Some of this stuff is useful some of it isn’t. Let’s tell Nixpkgs to only link the stuff that we want:

```
{
  packageOverrides =
    pkgs: with pkgs; {
      myPackages = pkgs.buildEnv {
        name = "my-packages";
        paths = [
          aspell
          bc
          coreutils
          gdb
          ffmpeg
          nix
          emscripten
          jq
          nox
          silver-searcher
        ];
        pathsToLink = [
          "/share"
          "/bin"
        ];
      };
    };
}
```

`pathsToLink` tells Nixpkgs to only link the paths listed which gets rid of the extra stuff in the profile. `/bin` and `/share` are good defaults for a user environment, getting rid of the clutter. If you are running on Nix on macOS, you may want to add another path as well, `/Applications`, that makes GUI apps available.

### Getting documentation

After building that new environment, look through `~/.nix-profile` to make sure everything is there that we wanted. Discerning readers will note that some files are missing. Look inside `~/.nix-profile/share/man/man1/` to verify this. There are no man pages for any of the Nix tools! This is because some packages like Nix have multiple outputs for things like documentation (see section 4). Let’s make Nix install those as well.

```
{
  packageOverrides =
    pkgs: with pkgs; {
      myPackages = pkgs.buildEnv {
        name = "my-packages";
        paths = [
          aspell
          bc
          coreutils
          ffmpeg
          nix
          emscripten
          jq
          nox
          silver-searcher
        ];
        pathsToLink = [
          "/share/man"
          "/share/doc"
          "/bin"
        ];
        extraOutputsToInstall = [
          "man"
          "doc"
        ];
      };
    };
}
```

This provides us with some useful documentation for using our packages. However, if we actually want those manpages to be detected by man, we need to set up our environment. This can also be managed within Nix expressions.

```
{
  packageOverrides = pkgs: {
    myProfile = pkgs.writeText "my-profile" ''
      export PATH=$HOME/.nix-profile/bin:/nix/var/nix/profiles/default/bin:/sbin:/bin:/usr/sbin:/usr/bin
      export MANPATH=$HOME/.nix-profile/share/man:/nix/var/nix/profiles/default/share/man:/usr/share/man
    '';
    myPackages = pkgs.buildEnv {
      name = "my-packages";
      paths = with pkgs; [
        (runCommand "profile" { } ''
          mkdir -p $out/etc/profile.d
          cp ${myProfile} $out/etc/profile.d/my-profile.sh
        '')
        aspell
        bc
        coreutils
        ffmpeg
        man
        nix
        emscripten
        jq
        nox
        silver-searcher
      ];
      pathsToLink = [
        "/share/man"
        "/share/doc"
        "/bin"
        "/etc"
      ];
      extraOutputsToInstall = [
        "man"
        "doc"
      ];
    };
  };
}
```

For this to work fully, you must also have this script sourced when you are logged in. Try adding something like this to your `~/.profile` file:

```
#!/bin/sh
if [ -d "${HOME}/.nix-profile/etc/profile.d" ]; then
  for i in "${HOME}/.nix-profile/etc/profile.d/"*.sh; do
    if [ -r "$i" ]; then
      . "$i"
    fi
  done
fi
```

Now just run `. "${HOME}/.profile"` and you can start loading man pages from your environment.

### GNU info setup

Configuring GNU info is a little bit trickier than man pages. To work correctly, info needs a database to be generated. This can be done with some small modifications to our environment scripts.

```
{
  packageOverrides = pkgs: {
    myProfile = pkgs.writeText "my-profile" ''
      export PATH=$HOME/.nix-profile/bin:/nix/var/nix/profiles/default/bin:/sbin:/bin:/usr/sbin:/usr/bin
      export MANPATH=$HOME/.nix-profile/share/man:/nix/var/nix/profiles/default/share/man:/usr/share/man
      export INFOPATH=$HOME/.nix-profile/share/info:/nix/var/nix/profiles/default/share/info:/usr/share/info
    '';
    myPackages = pkgs.buildEnv {
      name = "my-packages";
      paths = with pkgs; [
        (runCommand "profile" { } ''
          mkdir -p $out/etc/profile.d
          cp ${myProfile} $out/etc/profile.d/my-profile.sh
        '')
        aspell
        bc
        coreutils
        ffmpeg
        man
        nix
        emscripten
        jq
        nox
        silver-searcher
        texinfoInteractive
      ];
      pathsToLink = [
        "/share/man"
        "/share/doc"
        "/share/info"
        "/bin"
        "/etc"
      ];
      extraOutputsToInstall = [
        "man"
        "doc"
        "info"
      ];
      postBuild = ''
        if [ -x $out/bin/install-info -a -w $out/share/info ]; then
          shopt -s nullglob
          for i in $out/share/info/*.info $out/share/info/*.info.gz; do
              $out/bin/install-info $i $out/share/info/dir
          done
        fi
      '';
    };
  };
}
```

`postBuild` tells Nixpkgs to run a command after building the environment. In this case, `install-info` adds the installed info pages to `dir` which is GNU info’s default root node. Note that `texinfoInteractive` is added to the environment to give the `install-info` command.


## Overlays

This chapter describes how to extend and change Nixpkgs using overlays. Overlays are used to add layers in the fixed-point used by Nixpkgs to compose the set of all packages.

Nixpkgs can be configured with a list of overlays, which are applied in order. This means that the order of the overlays can be significant if multiple layers override the same package.


## Installing overlays

The list of overlays can be set either explicitly in a Nix expression, or through `<nixpkgs-overlays>` or user configuration files.

### Set overlays in NixOS or Nix expressions

On a NixOS system the value of the `nixpkgs.overlays` option, if present, is passed to the system Nixpkgs directly as an argument. Note that this does not affect the overlays for non-NixOS operations (e.g. `nix-env`), which are looked up independently.

The list of overlays can be passed explicitly when importing nixpkgs, for example `import <nixpkgs> { overlays = [ overlay1 overlay2 ]; }`.

NOTE: DO NOT USE THIS in nixpkgs. Further overlays can be added by calling the `pkgs.extend` or `pkgs.appendOverlays`, although it is often preferable to avoid these functions, because they recompute the Nixpkgs fixpoint, which is somewhat expensive to do.

### Install overlays via configuration lookup

The list of overlays is determined as follows.

1. First, if an `overlays` argument to the Nixpkgs function itself is given, then that is used and no path lookup will be performed.
2. Otherwise, if the Nix path entry `<nixpkgs-overlays>` exists, we look for overlays at that path, as described below.See the section on `NIX_PATH` in the Nix manual for more details on how to set a value for `<nixpkgs-overlays>.`
3. If one of `~/.config/nixpkgs/overlays.nix` and `~/.config/nixpkgs/overlays/` exists, then we look for overlays at that path, as described below. It is an error if both exist.

If we are looking for overlays at a path, then there are two cases:

- If the path is a file, then the file is imported as a Nix expression and used as the list of overlays.
- If the path is a directory, then we take the content of the directory, order it lexicographically, and attempt to interpret each as an overlay by:Importing the file, if it is a `.nix` file.Importing a top-level `default.nix` file, if it is a directory.

Because overlays that are set in NixOS configuration do not affect non-NixOS operations such as `nix-env`, the `overlays.nix` option provides a convenient way to use the same overlays for a NixOS system configuration and user configuration: the same file can be used as `overlays.nix` and imported as the value of `nixpkgs.overlays`.


## Defining overlays

Overlays are Nix functions which accept two arguments, conventionally called either `final` and `prev` in newer code or `self` and `super` in older code, and return a set of packages. For example, the following is a valid overlay.

```
final: prev:

{
  boost = prev.boost.override { python = final.python3; };
  rr = prev.callPackage ./pkgs/rr { stdenv = final.stdenv_32bit; };
}
```

The first argument (`final`, `self`) corresponds to the final package set. You should use this set for the dependencies of all packages specified in your overlay. For example, all the dependencies of `rr` in the example above come from `final`, as well as the overridden dependencies used in the `boost` override.

The second argument (`prev`, `super`) corresponds to the result of the evaluation of the previous stages of Nixpkgs. It does not contain any of the packages added by the current overlay, nor any of the following overlays. This set should be used either to refer to packages you wish to override, or to access functions defined in Nixpkgs. For example, the original recipe of `boost` in the above example, comes from `prev`, as well as the `callPackage` function.

The value returned by this function should be a set similar to `pkgs/top-level/all-packages.nix`, containing overridden and/or new packages.

Overlays are similar to other methods for customizing Nixpkgs, in particular the `packageOverrides` attribute described in the section called “Modify packages via `packageOverrides`”. Indeed, `packageOverrides` acts as an overlay with only the `prev` argument. It is therefore appropriate for basic use, but overlays are more powerful and easier to distribute.
