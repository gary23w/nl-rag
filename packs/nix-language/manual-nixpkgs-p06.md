---
title: "Nixpkgs Reference Manual (part 6/6)"
source: https://nixos.org/manual/nixpkgs/stable/
domain: nix-language
license: CC-BY-SA-4.0
tags: nix language, nix lang, nixos, nixpkgs, nix expression
fetched: 2026-07-02
part: 6/6
---

# Nixpkgs Reference Manual

Converts an attrset containing one of `hash`, `sha256` or `sha512`, into one containing `outputHash{,Algo}` as accepted by `mkDerivation`.

An appropriate “fake hash” is substituted when the hash value is `""`, as is the convention for fetchers.

All other attributes in the set remain as-is.

##### Type

```
normalizeHash :: { hashTypes :: [String]; required :: Bool; } -> AttrSet -> AttrSet
```

##### Arguments

**hashTypes**

the set of attribute names accepted as hash inputs, in addition to `hash`

**required**

whether to throw if no hash was present in the input; otherwise returns the original input, unmodified

##### Example

Example 240.

lib.fetchers.normalizeHash

usage example

Located at lib/fetchers.nix:113 in `<nixpkgs>`.

#### `lib.fetchers.withNormalizedHash`

Wraps a function which accepts `outputHash{,Algo}` into one which accepts `hash` or `sha{256,512}`

##### Example

```
withNormalizedHash { hashTypes = [ "sha256" "sha512" ]; } (
  { outputHash, outputHashAlgo, ... }:
  ...
)
```

is a function which accepts one of `hash`, `sha256`, or `sha512` (or the original’s `outputHash` and `outputHashAlgo`).

Its `functionArgs` metadata only lists `hash` as a parameter, optional iff. `outputHash` was an optional parameter of the original function. `sha256`, `sha512`, `outputHash`, or `outputHashAlgo` are not mentioned in the `functionArgs` metadata.

##### Type

```
withNormalizedHash :: { hashTypes :: [String]; } -> (AttrSet -> a) -> (AttrSet -> a)
```

##### Arguments

**hashTypes**

the set of attribute names accepted as hash inputs, in addition to `hash`

they must correspond to a valid value for `outputHashAlgo`, currently one of: `md5`, `sha1`, `sha256`, or `sha512`.

**f**

the function to be wrapped

### Note

In nixpkgs, `mkDerivation` rejects MD5 `outputHash`es, and SHA-1 is being deprecated.

As such, there is no reason to add `md5` to `hashTypes`, and `sha1` should only ever be included for backwards compatibility.

##### Output

`withNormalizedHash { inherit hashTypes; } f` is functionally equivalent to

```
args: f (normalizeHash {
  inherit hashTypes;
  required = !(lib.functionArgs f).outputHash;
} args)
```

However, `withNormalizedHash` preserves `functionArgs` metadata insofar as possible, and is implemented somewhat more efficiently.

Located at lib/fetchers.nix:201 in `<nixpkgs>`.

### lib.filesystem: filesystem functions

Functions for querying information about the filesystem without copying any files to the Nix store.

#### `lib.filesystem.pathType`

The type of a path. The path needs to exist and be accessible. The result is either `"directory"` for a directory, `"regular"` for a regular file, `"symlink"` for a symlink, or `"unknown"` for anything else.

##### Inputs

**path**

The path to query

##### Type

```
pathType :: Path -> String
```

##### Examples

Example 241.

lib.filesystem.pathType

usage example

Located at lib/filesystem.nix:69 in `<nixpkgs>`.

#### `lib.filesystem.pathIsDirectory`

Whether a path exists and is a directory.

##### Inputs

**`path`**

1. Function argument

##### Type

```
pathIsDirectory :: Path -> Bool
```

##### Examples

Example 242.

lib.filesystem.pathIsDirectory

usage example

Located at lib/filesystem.nix:103 in `<nixpkgs>`.

#### `lib.filesystem.pathIsRegularFile`

Whether a path exists and is a regular file, meaning not a symlink or any other special file type.

##### Inputs

**`path`**

1. Function argument

##### Type

```
pathIsRegularFile :: Path -> Bool
```

##### Examples

Example 243.

lib.filesystem.pathIsRegularFile

usage example

Located at lib/filesystem.nix:137 in `<nixpkgs>`.

#### `lib.filesystem.haskellPathsInDir`

A map of all haskell packages defined in the given path, identified by having a cabal file with the same name as the directory itself.

##### Inputs

**`root`**

The directory within to search

##### Type

```
haskellPathsInDir :: Path -> { [String] :: Path }
```

Located at lib/filesystem.nix:156 in `<nixpkgs>`.

#### `lib.filesystem.locateDominatingFile`

Find the first directory containing a file matching `pattern` upward from a given `file`. Returns `null` if no directories contain a file matching `pattern`.

##### Inputs

**`pattern`**

The pattern to search for

**`file`**

The file to start searching upward from

##### Type

```
locateDominatingFile :: RegExp -> Path -> ({ path :: Path; matches :: [MatchResults]; } | Null)
```

Located at lib/filesystem.nix:193 in `<nixpkgs>`.

#### `lib.filesystem.listFilesRecursive`

Given a directory, return a flattened list of all files within it recursively.

##### Inputs

**`dir`**

The path to recursively list

##### Type

```
listFilesRecursive :: Path -> [Path]
```

Located at lib/filesystem.nix:233 in `<nixpkgs>`.

#### `lib.filesystem.packagesFromDirectoryRecursive`

Transform a directory tree containing package files suitable for `callPackage` into a matching nested attribute set of derivations.

For a directory tree like this:

```
my-packages
├── a.nix
├── b.nix
├── c
│  ├── my-extra-feature.patch
│  ├── package.nix
│  └── support-definitions.nix
└── my-namespace
   ├── d.nix
   ├── e.nix
   └── f
      └── package.nix
```

`packagesFromDirectoryRecursive` will produce an attribute set like this:

```
# packagesFromDirectoryRecursive {
#   callPackage = pkgs.callPackage;
#   directory = ./my-packages;
# }
{
  a = pkgs.callPackage ./my-packages/a.nix { };
  b = pkgs.callPackage ./my-packages/b.nix { };
  c = pkgs.callPackage ./my-packages/c/package.nix { };
  my-namespace = {
    d = pkgs.callPackage ./my-packages/my-namespace/d.nix { };
    e = pkgs.callPackage ./my-packages/my-namespace/e.nix { };
    f = pkgs.callPackage ./my-packages/my-namespace/f/package.nix { };
  };
}
```

In particular:

- If the input directory contains a `package.nix` file, then `callPackage <directory>/package.nix { }` is returned.
- Otherwise, the input directory’s contents are listed and transformed into an attribute set.If a regular file’s name has the `.nix` extension, it is turned into attribute where:The attribute name is the file name without the `.nix` extensionThe attribute value is `callPackage <file path> { }`Directories are turned into an attribute where:The attribute name is the name of the directoryThe attribute value is the result of calling `packagesFromDirectoryRecursive { ... }` on the directory.As a result, directories with no `.nix` files (including empty directories) will be transformed into empty attribute sets.Other files are ignored, including symbolic links to directories and to regular `.nix` files; this is because nixlang code cannot distinguish the type of a link’s target.

##### Inputs

**`callPackage`**

The function used to convert a Nix file’s path into a leaf of the attribute set. It is typically the `callPackage` function, taken from either `pkgs` or a new scope corresponding to the `directory`.

**`newScope`**

If present, this function is used when recursing into a directory, to generate a new scope. The arguments are updated with the scope’s `callPackage` and `newScope` functions, so packages can require anything in their scope, or in an ancestor of their scope.

**`directory`**

The directory to read package files from.

##### Type

```
packagesFromDirectoryRecursive :: {
  callPackage :: Path -> AttrSet -> Any;
  newScope? :: AttrSet -> Scope;
  directory :: Path;
} -> AttrSet
```

##### Examples

Example 244. Basic use of

lib.packagesFromDirectoryRecursive

Example 245. Create a scope for the nix files found in a directory

Located at lib/filesystem.nix:370 in `<nixpkgs>`.

#### `lib.filesystem.resolveDefaultNix`

Append `/default.nix` if the passed path is a directory.

##### Inputs

A single argument which can be a path value or a string containing an absolute path.

##### Output

If the input refers to a directory that exists, the output is that same path with `/default.nix` appended. Furthermore, if the input is a string that ends with `/`, `default.nix` is appended to it. Otherwise, the input is returned unchanged.

##### Type

```
resolveDefaultNix :: (Path | String) -> (Path | String)
```

##### Examples

Example 246.

lib.filesystem.resolveDefaultNix

usage example

### lib.fileset: file set functions

The `lib.fileset` library allows you to work with *file sets*. A file set is a (mathematical) set of local files that can be added to the Nix store for use in Nix derivations. File sets are easy and safe to use, providing obvious and composable semantics with good error messages to prevent mistakes.

#### Overview

Basics:

- Implicit coercion from paths to file sets
- `lib.fileset.maybeMissing`:Create a file set from a path that may be missing.
- `lib.fileset.trace`/`lib.fileset.traceVal`:Pretty-print file sets for debugging.
- `lib.fileset.toSource`:Add files in file sets to the store to use as derivation sources.
- `lib.fileset.toList`:The list of files contained in a file set.

Combinators:

- `lib.fileset.union`/`lib.fileset.unions`:Create a larger file set from all the files in multiple file sets.
- `lib.fileset.intersection`:Create a smaller file set from only the files in both file sets.
- `lib.fileset.difference`:Create a smaller file set containing all files that are in one file set, but not another one.

Filtering:

- `lib.fileset.fileFilter`:Create a file set from all files that satisisfy a predicate in a directory.

Utilities:

- `lib.fileset.fromSource`:Create a file set from a `lib.sources`-based value.
- `lib.fileset.gitTracked`/`lib.fileset.gitTrackedWith`:Create a file set from all tracked files in a local Git repository.

If you need more file set functions, see this issue to request it.

#### Implicit coercion from paths to file sets

All functions accepting file sets as arguments can also accept paths as arguments. Such path arguments are implicitly coerced to file sets containing all files under that path:

- A path to a file turns into a file set containing that single file.
- A path to a directory turns into a file set containing all files *recursively* in that directory.

If the path points to a non-existent location, an error is thrown.

### Note

Just like in Git, file sets cannot represent empty directories. Because of this, a path to a directory that contains no files (recursively) will turn into a file set containing no files.

### Note

File set coercion does *not* add any of the files under the coerced paths to the store. Only the `toSource` function adds files to the Nix store, and only those files contained in the `fileset` argument. This is in contrast to using paths in string interpolation, which does add the entire referenced path to the store.

##### Example

Assume we are in a local directory with a file hierarchy like this:

```
├─ a/
│  ├─ x (file)
│  └─ b/
│     └─ y (file)
└─ c/
   └─ d/
```

Here’s a listing of which files get included when different path expressions get coerced to file sets:

- `./.` as a file set contains both `a/x` and `a/b/y` (`c/` does not contain any files and is therefore omitted).
- `./a` as a file set contains both `a/x` and `a/b/y`.
- `./a/x` as a file set contains only `a/x`.
- `./a/b` as a file set contains only `a/b/y`.
- `./c` as a file set is empty, since neither `c` nor `c/d` contain any files.

#### `lib.fileset.maybeMissing`

Create a file set from a path that may or may not exist:

- If the path does exist, the path is coerced to a file set.
- If the path does not exist, a file set containing no files is returned.

##### Inputs

**`path`**

1. Function argument

##### Type

```
maybeMissing :: Path -> FileSet
```

##### Examples

Example 247.

lib.fileset.maybeMissing

usage example

Located at lib/fileset/default.nix:186 in `<nixpkgs>`.

#### `lib.fileset.trace`

Incrementally evaluate and trace a file set in a pretty way. This function is only intended for debugging purposes. The exact tracing format is unspecified and may change.

This function takes a final argument to return. In comparison, `traceVal` returns the given file set argument.

This variant is useful for tracing file sets in the Nix repl.

##### Inputs

**`fileset`**

The file set to trace.

This argument can also be a path, which gets implicitly coerced to a file set.

**`val`**

The value to return.

##### Type

```
trace :: FileSet -> Any -> Any
```

##### Examples

Example 248.

lib.fileset.trace

usage example

Located at lib/fileset/default.nix:245 in `<nixpkgs>`.

#### `lib.fileset.traceVal`

Incrementally evaluate and trace a file set in a pretty way. This function is only intended for debugging purposes. The exact tracing format is unspecified and may change.

This function returns the given file set. In comparison, `trace` takes another argument to return.

This variant is useful for tracing file sets passed as arguments to other functions.

##### Inputs

**`fileset`**

The file set to trace and return.

This argument can also be a path, which gets implicitly coerced to a file set.

##### Type

```
traceVal :: FileSet -> FileSet
```

##### Examples

Example 249.

lib.fileset.traceVal

usage example

Located at lib/fileset/default.nix:303 in `<nixpkgs>`.

#### `lib.fileset.toSource`

Add the local files contained in `fileset` to the store as a single store path rooted at `root`.

The result is the store path as a string-like value, making it usable e.g. as the `src` of a derivation, or in string interpolation:

```
stdenv.mkDerivation {
  src = lib.fileset.toSource { ... };
  # ...
}
```

The name of the store path is always `source`.

##### Inputs

Takes an attribute set with the following attributes

**`root` (Path; *required*)**

The local directory path that will correspond to the root of the resulting store path. Paths in strings, including Nix store paths, cannot be passed as `root`. `root` has to be a directory.

### Note

Changing `root` only affects the directory structure of the resulting store path, it does not change which files are added to the store. The only way to change which files get added to the store is by changing the `fileset` attribute.

**`fileset` (FileSet; *required*)**

The file set whose files to import into the store. File sets can be created using other functions in this library. This argument can also be a path, which gets implicitly coerced to a file set.

### Note

If a directory does not recursively contain any file, it is omitted from the store path contents.

##### Type

```
toSource :: {
  root :: Path,
  fileset :: FileSet,
} -> SourceLike
```

##### Examples

Example 250.

lib.fileset.toSource

usage example

Located at lib/fileset/default.nix:418 in `<nixpkgs>`.

#### `lib.fileset.toList`

The list of file paths contained in the given file set.

### Note

This function is strict in the entire file set. This is in contrast with combinators `lib.fileset.union`, `lib.fileset.intersection` and `lib.fileset.difference`.

Thus it is recommended to call `toList` on file sets created using the combinators, instead of doing list processing on the result of `toList`.

The resulting list of files can be turned back into a file set using `lib.fileset.unions`.

##### Inputs

**`fileset`**

The file set whose file paths to return. This argument can also be a path, which gets implicitly coerced to a file set.

##### Type

```
toList :: FileSet -> [ Path ]
```

##### Examples

Example 251.

lib.fileset.toList

usage example

Located at lib/fileset/default.nix:512 in `<nixpkgs>`.

#### `lib.fileset.union`

The file set containing all files that are in either of two given file sets. This is the same as `unions`, but takes just two file sets instead of a list. See also Union (set theory).

The given file sets are evaluated as lazily as possible, with the first argument being evaluated first if needed.

##### Inputs

**`fileset1`**

The first file set. This argument can also be a path, which gets implicitly coerced to a file set.

**`fileset2`**

The second file set. This argument can also be a path, which gets implicitly coerced to a file set.

##### Type

```
union :: FileSet -> FileSet -> FileSet
```

##### Examples

Example 252.

lib.fileset.union

usage example

Located at lib/fileset/default.nix:555 in `<nixpkgs>`.

#### `lib.fileset.unions`

The file set containing all files that are in any of the given file sets. This is the same as `union`, but takes a list of file sets instead of just two. See also Union (set theory).

The given file sets are evaluated as lazily as possible, with earlier elements being evaluated first if needed.

##### Inputs

**`filesets`**

A list of file sets. The elements can also be paths, which get implicitly coerced to file sets.

##### Type

```
unions :: [ FileSet ] -> FileSet
```

##### Examples

Example 253.

lib.fileset.unions

usage example

Located at lib/fileset/default.nix:617 in `<nixpkgs>`.

#### `lib.fileset.intersection`

The file set containing all files that are in both of two given file sets. See also Intersection (set theory).

The given file sets are evaluated as lazily as possible, with the first argument being evaluated first if needed.

##### Inputs

**`fileset1`**

The first file set. This argument can also be a path, which gets implicitly coerced to a file set.

**`fileset2`**

The second file set. This argument can also be a path, which gets implicitly coerced to a file set.

##### Type

```
intersection :: FileSet -> FileSet -> FileSet
```

##### Examples

Example 254.

lib.fileset.intersection

usage example

Located at lib/fileset/default.nix:668 in `<nixpkgs>`.

#### `lib.fileset.difference`

The file set containing all files from the first file set that are not in the second file set. See also Difference (set theory).

The given file sets are evaluated as lazily as possible, with the first argument being evaluated first if needed.

##### Inputs

**`positive`**

The positive file set. The result can only contain files that are also in this file set. This argument can also be a path, which gets implicitly coerced to a file set.

**`negative`**

The negative file set. The result will never contain files that are also in this file set. This argument can also be a path, which gets implicitly coerced to a file set.

##### Type

```
difference :: FileSet -> FileSet -> FileSet
```

##### Examples

Example 255.

lib.fileset.difference

usage example

Located at lib/fileset/default.nix:727 in `<nixpkgs>`.

#### `lib.fileset.fileFilter`

Filter a file set to only contain files matching some predicate.

##### Inputs

**`predicate`**

The predicate function to call on all files contained in given file set. A file is included in the resulting file set if this function returns true for it.

This function is called with an attribute set containing these attributes:

- `name` (String): The name of the file
- `type` (String, one of `"regular"`, `"symlink"` or `"unknown"`): The type of the file. This matches result of calling `builtins.readFileType` on the file’s path.
- `hasExt` (String -> Bool): Whether the file has a certain file extension. `hasExt ext` is true only if `hasSuffix ".${ext}" name`.This also means that e.g. for a file with name `.gitignore`, `hasExt "gitignore"` is true.

Other attributes may be added in the future.

**`path`**

The path whose files to filter

##### Type

```
fileFilter ::
  ({
    name :: String,
    type :: String,
    hasExt :: String -> Bool,
    ...
  } -> Bool)
  -> Path
  -> FileSet
```

##### Examples

Example 256.

lib.fileset.fileFilter

usage example

Located at lib/fileset/default.nix:806 in `<nixpkgs>`.

#### `lib.fileset.fromSource`

Create a file set with the same files as a `lib.sources`-based value. This does not import any of the files into the store.

This can be used to gradually migrate from `lib.sources`-based filtering to `lib.fileset`.

A file set can be turned back into a source using `toSource`.

### Note

File sets cannot represent empty directories. Turning the result of this function back into a source using `toSource` will therefore not preserve empty directories.

##### Inputs

**`source`**

1. Function argument

##### Type

```
fromSource :: SourceLike -> FileSet
```

##### Examples

Example 257.

lib.fileset.fromSource

usage example

Located at lib/fileset/default.nix:880 in `<nixpkgs>`.

#### `lib.fileset.gitTracked`

Create a file set containing all Git-tracked files in a repository.

This function behaves like `gitTrackedWith { }` - using the defaults.

##### Inputs

**`path`**

The path to the working directory of a local Git repository. This directory must contain a `.git` file or subdirectory.

##### Type

```
gitTracked :: Path -> FileSet
```

##### Examples

Example 258.

lib.fileset.gitTracked

usage example

Located at lib/fileset/default.nix:939 in `<nixpkgs>`.

#### `lib.fileset.gitTrackedWith`

Create a file set containing all Git-tracked files in a repository. The first argument allows configuration with an attribute set, while the second argument is the path to the Git working tree.

`gitTrackedWith` does not perform any filtering when the path is a Nix store path and not a repository. In this way, it accommodates the use case where the expression that makes the `gitTracked` call does not reside in an actual git repository anymore, and has presumably already been fetched in a way that excludes untracked files. Fetchers with such equivalent behavior include `builtins.fetchGit`, `builtins.fetchTree` (experimental), and `pkgs.fetchgit` when used without `leaveDotGit`.

If you don’t need the configuration, you can use `gitTracked` instead.

This is equivalent to the result of `unions` on all files returned by `git ls-files` (which uses `--cached` by default).

### Warning

Currently this function is based on `builtins.fetchGit` As such, this function causes all Git-tracked files to be unnecessarily added to the Nix store, without being re-usable by `toSource`.

This may change in the future.

##### Inputs

**`options` (attribute set)**

**`recurseSubmodules` (optional, default: `false`)**

Whether to recurse into Git submodules to also include their tracked files. If `true`, this is equivalent to passing the –recurse-submodules flag to `git ls-files`.

**`path`**

The path to the working directory of a local Git repository. This directory must contain a `.git` file or subdirectory.

##### Type

```
gitTrackedWith :: { recurseSubmodules :: Bool ? false } -> Path -> FileSet
```

##### Examples

Example 259.

lib.fileset.gitTrackedWith

usage example

Located at lib/fileset/default.nix:994 in `<nixpkgs>`.

#### `lib.fileset.empty`

The empty fileset. It can be useful as a default value or as starting accumulator for a folding operation.

##### Type

```
empty :: FileSet
```

Located at lib/fileset/default.nix:1017 in `<nixpkgs>`.

#### `lib.fileset.isFileset`

Tests whether a given value is a fileset, or can be used in place of a fileset.

##### Inputs

**`value`**

The value to test

##### Type

```
isFileset :: Any -> Bool
```

##### Examples

Example 260.

lib.fileset.isFileset

usage example

Located at lib/fileset/default.nix:1051 in `<nixpkgs>`.

### lib.sources: source filtering functions

#### `lib.sources.commitIdFromGitRepo`

Get the commit id of a git repo.

##### Inputs

**`path`**

1. Function argument

##### Examples

Example 261.

commitIdFromGitRepo

usage example

Located at lib/sources.nix:520 in `<nixpkgs>`.

#### `lib.sources.cleanSource`

Filters a source tree removing version control files and directories using `cleanSourceFilter`.

##### Inputs

**`src`**

1. Function argument

##### Examples

Example 262.

cleanSource

usage example

Located at lib/sources.nix:522 in `<nixpkgs>`.

#### `lib.sources.cleanSourceWith`

Like `builtins.filterSource`, except it will compose with itself, allowing you to chain multiple calls together without any intermediate copies being put in the nix store.

##### Examples

Example 263.

cleanSourceWith

usage example

Located at lib/sources.nix:523 in `<nixpkgs>`.

#### `lib.sources.cleanSourceFilter`

A basic filter for `cleanSourceWith` that removes directories of version control system, backup files (`*~`) and some generated files.

##### Inputs

**`name`**

1. Function argument

**`type`**

2. Function argument

Located at lib/sources.nix:524 in `<nixpkgs>`.

#### `lib.sources.sourceByRegex`

Filter sources by a list of regular expressions.

##### Inputs

**`src`**

1. Function argument

**`regexes`**

2. Function argument

##### Examples

Example 264.

sourceByRegex

usage example

Located at lib/sources.nix:533 in `<nixpkgs>`.

#### `lib.sources.sourceFilesBySuffices`

Get all files ending with the specified suffices from the given source directory or its descendants, omitting files that do not match any suffix. The result of the example below will include files like `./dir/module.c` and `./dir/subdir/doc.xml` if present.

##### Inputs

**`src`**

Path or source containing the files to be returned

**`exts`**

A list of file suffix strings

##### Type

```
sourceFilesBySuffices :: SourceLike -> [String] -> Source
```

##### Examples

Example 265.

sourceFilesBySuffices

usage example

Located at lib/sources.nix:534 in `<nixpkgs>`.

#### `lib.sources.trace`

Add logging to a source, for troubleshooting the filtering behavior.

##### Inputs

**`src`**

Source to debug. The returned source will behave like this source, but also log its filter invocations.

##### Type

```
sources.trace :: SourceLike -> Source
```

Located at lib/sources.nix:536 in `<nixpkgs>`.

### lib.cli: command-line serialization functions

#### `lib.cli.toGNUCommandLineShell`

Automatically convert an attribute set to command-line options.

This helps protect against malformed command lines and also to reduce boilerplate related to command-line construction for simple use cases.

`toGNUCommandLineShell` returns an escaped shell string.

##### Inputs

**`options`**

How to format the arguments, see `toGNUCommandLine`

**`attrs`**

The attributes to transform into arguments.

##### Examples

Example 266.

lib.cli.toGNUCommandLineShell

usage example

Located at lib/cli.nix:42 in `<nixpkgs>`.

#### `lib.cli.toGNUCommandLine`

Automatically convert an attribute set to a list of command-line options.

`toGNUCommandLine` returns a list of string arguments.

##### Inputs

**`options`**

How to format the arguments, see below.

**`attrs`**

The attributes to transform into arguments.

###### Options

**`mkOptionName`**

How to string-format the option name; By default one character is a short option (`-`), more than one characters a long option (`--`).

**`mkBool`**

How to format a boolean value to a command list; By default it’s a flag option (only the option name if true, left out completely if false).

**`mkList`**

How to format a list value to a command list; By default the option name is repeated for each value and `mkOption` is applied to the values themselves.

**`mkOption`**

How to format any remaining value to a command list; On the toplevel, booleans and lists are handled by `mkBool` and `mkList`, though they can still appear as values of a list. By default, everything is printed verbatim and complex types are forbidden (lists, attrsets, functions). `null` values are omitted.

**`optionValueSeparator`**

How to separate an option from its flag; By default, there is no separator, so option `-c` and value `5` would become `["-c" "5"]`. This is useful if the command requires equals, for example, `-c=5`.

##### Examples

Example 267.

lib.cli.toGNUCommandLine

usage example

Located at lib/cli.nix:118 in `<nixpkgs>`.

#### `lib.cli.toCommandLineShellGNU`

Converts the given attributes into a single shell-escaped command-line string. Similar to `toCommandLineGNU`, but returns a single escaped string instead of a list of arguments. For further reference see: `lib.cli.toCommandLineGNU`

Located at lib/cli.nix:166 in `<nixpkgs>`.

#### `lib.cli.toCommandLineGNU`

Converts an attribute set into a list of GNU-style command-line arguments.

`toCommandLineGNU` returns a list of string arguments.

##### Inputs

**`options`**

Options, see below.

**`attrs`**

The attributes to transform into arguments.

###### Options

**`isLong`**

A function that determines whether an option is long or short.

**`explicitBool`**

Whether or not boolean option arguments should be formatted explicitly.

**`formatArg`**

A function that turns the option argument into a string.

##### Examples

Example 268.

lib.cli.toCommandLineGNU

usage example

Located at lib/cli.nix:228 in `<nixpkgs>`.

#### `lib.cli.toCommandLineShell`

Converts the given attributes into a single shell-escaped command-line string. Similar to `toCommandLine`, but returns a single escaped string instead of a list of arguments. For further reference see: `lib.cli.toCommandLine`

Located at lib/cli.nix:251 in `<nixpkgs>`.

#### `lib.cli.toCommandLine`

Converts an attribute set into a list of command-line arguments.

This is the most general command-line construction helper in `lib.cli`. It is parameterized by an `optionFormat` function, which defines how each option name and its value are rendered.

All other helpers in this file are thin wrappers around this function.

`toCommandLine` returns a *flat list of strings*, suitable for use as `argv` arguments or for further processing (e.g. shell escaping).

##### Inputs

**`optionFormat`**

A function that takes the option name and returns an option spec, where the option spec is an attribute set describing how the option should be rendered.

The returned attribute set must contain:

- `option` (string): The option flag itself, e.g. `"-v"` or `"--verbose"`.
- `sep` (string or null): How to separate the option from its argument. If `null`, the option and its argument are returned as two separate list elements. If a string (e.g. `"="`), the option and argument are concatenated.
- `explicitBool` (bool): Controls how boolean values are handled:`false`: `true` emits only the option flag, `false` emits nothing.`true`: both `true` and `false` are rendered as explicit arguments via `formatArg`.

Optional fields:

- `formatArg`: Converts the option value to a string. Defaults to `lib.generators.mkValueStringDefault { }`.

**`attrs`**

An attribute set mapping option names to values.

Supported value types:

- null: omitted entirely
- bool: handled according to `explicitBool`
- list: each element is rendered as a separate occurrence of the option
- any other value: rendered as a single option argument

Empty attribute names are rejected.

##### Examples

Example 269.

lib.cli.toCommandLine

basic usage example

Example 270.

lib.cli.toCommandLine

usage with a more complex option format
