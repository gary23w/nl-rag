---
title: "Nixpkgs Reference Manual (part 5/6)"
source: https://nixos.org/manual/nixpkgs/stable/
domain: nix-language
license: CC-BY-SA-4.0
tags: nix language, nix lang, nixos, nixpkgs, nix expression
fetched: 2026-07-02
part: 5/6
---

# Nixpkgs Reference Manual

Message that should be traced

**`x`**

Value to return

##### Type

```
traceIf :: Bool -> String -> a -> a
```

##### Examples

Example 207.

lib.debug.traceIf

usage example

Located at lib/debug.nix:78 in `<nixpkgs>`.

#### `lib.debug.traceValFn`

Trace the supplied value after applying a function to it, and return the original value.

##### Inputs

**`f`**

Function to apply

**`x`**

Value to trace and return

##### Type

```
traceValFn :: (a -> b) -> a -> a
```

##### Examples

Example 208.

lib.debug.traceValFn

usage example

Located at lib/debug.nix:114 in `<nixpkgs>`.

#### `lib.debug.traceVal`

Trace the supplied value and return it.

##### Inputs

**`x`**

Value to trace and return

##### Type

```
traceVal :: a -> a
```

##### Examples

Example 209.

lib.debug.traceVal

usage example

Located at lib/debug.nix:143 in `<nixpkgs>`.

#### `lib.debug.traceSeq`

`builtins.trace`, but the value is `builtins.deepSeq`ed first.

##### Inputs

**`x`**

The value to trace

**`y`**

The value to return

##### Type

```
traceSeq :: a -> b -> b
```

##### Examples

Example 210.

lib.debug.traceSeq

usage example

Located at lib/debug.nix:179 in `<nixpkgs>`.

#### `lib.debug.traceSeqN`

Like `traceSeq`, but only evaluate down to depth n. This is very useful because lots of `traceSeq` usages lead to an infinite recursion.

##### Inputs

**`depth`**

1. Function argument

**`x`**

2. Function argument

**`y`**

3. Function argument

##### Type

```
traceSeqN :: Int -> a -> b -> b
```

##### Examples

Example 211.

lib.debug.traceSeqN

usage example

Located at lib/debug.nix:218 in `<nixpkgs>`.

#### `lib.debug.traceValSeqFn`

A combination of `traceVal` and `traceSeq` that applies a provided function to the value to be traced after `deepSeq`ing it.

##### Inputs

**`f`**

Function to apply

**`v`**

Value to trace

##### Type

```
traceValSeqFn :: (a -> b) -> a -> a
```

##### Examples

Example 212.

lib.debug.traceValSeqFn

usage example

Located at lib/debug.nix:278 in `<nixpkgs>`.

#### `lib.debug.traceValSeq`

A combination of `traceVal` and `traceSeq`.

##### Inputs

**`v`**

Value to trace

##### Type

```
traceValSeq :: a -> a
```

##### Examples

Example 213.

lib.debug.traceValSeq

usage example

Located at lib/debug.nix:307 in `<nixpkgs>`.

#### `lib.debug.traceValSeqNFn`

A combination of `traceVal` and `traceSeqN` that applies a provided function to the value to be traced.

##### Inputs

**`f`**

Function to apply

**`depth`**

2. Function argument

**`v`**

Value to trace

##### Type

```
traceValSeqNFn :: (a -> b) -> Int -> a -> a
```

##### Examples

Example 214.

lib.debug.traceValSeqNFn

usage example

Located at lib/debug.nix:345 in `<nixpkgs>`.

#### `lib.debug.traceValSeqN`

A combination of `traceVal` and `traceSeqN`.

##### Inputs

**`depth`**

1. Function argument

**`v`**

Value to trace

##### Type

```
traceValSeqN :: Int -> a -> a
```

##### Examples

Example 215.

lib.debug.traceValSeqN

usage example

Located at lib/debug.nix:380 in `<nixpkgs>`.

#### `lib.debug.traceFnSeqN`

Trace the input and output of a function `f` named `name`, both down to `depth`.

This is useful for adding around a function call, to see the before/after of values as they are transformed.

##### Inputs

**`depth`**

1. Function argument

**`name`**

2. Function argument

**`f`**

3. Function argument

**`v`**

4. Function argument

##### Type

```
traceFnSeqN :: Int -> String -> (a -> b) -> a -> b
```

##### Examples

Example 216.

lib.debug.traceFnSeqN

usage example

Located at lib/debug.nix:425 in `<nixpkgs>`.

#### `lib.debug.runTests`

Evaluates a set of tests.

A test is an attribute set `{expr, expected}`, denoting an expression and its expected result.

The result is a `list` of **failed tests**, each represented as `{name, expected, result}`,

- expectedWhat was passed as `expected`
- resultThe actual `result` of the test

Used for regression testing of the functions in lib; see tests.nix for more examples.

Important: Only attributes that start with `test` are executed.

- If you want to run only a subset of the tests add the attribute `tests = ["testName"];`

##### Inputs

**`tests`**

Tests to run

##### Type

```
runTests :: {
  tests :: [String];
  ${testName} :: {
    expr :: a;
    expected :: a;
  };
}
->
[
  {
    name :: String;
    expected :: a;
    result :: a;
  }
]
```

##### Examples

Example 217.

lib.debug.runTests

usage example

Located at lib/debug.nix:512 in `<nixpkgs>`.

#### `lib.debug.throwTestFailures`

Pretty-print a list of test failures.

This takes an attribute set containing `failures` (a list of test failures produced by `runTests`) and pretty-prints each failing test, before throwing an error containing the raw test data as JSON.

If the input list is empty, `null` is returned.

##### Inputs

**`failures`**

A list of test failures (produced `runTests`), each containing `name`, `expected`, and `result` attributes.

##### Type

```
throwTestFailures :: {
  failures = [
    {
      name :: String;
      expected :: a;
      result :: a;
    }
  ];
}
->
Null
```

##### Examples

Example 218.

lib.debug.throwTestFailures

usage example

Located at lib/debug.nix:619 in `<nixpkgs>`.

#### `lib.debug.testAllTrue`

Create a test assuming that list elements are `true`.

##### Inputs

**`expr`**

1. Function argument

##### Examples

Example 219.

lib.debug.testAllTrue

usage example

Located at lib/debug.nix:682 in `<nixpkgs>`.

### lib.options: NixOS / nixpkgs option handling

Module System option handling.

#### `lib.options.isOption`

Returns true when the given argument `a` is an option

##### Inputs

**`a`**

Any value to check whether it is an option

##### Examples

Example 220.

lib.options.isOption

usage example

##### Type

```
isOption :: Any -> Bool
```

Located at lib/options.nix:77 in `<nixpkgs>`.

#### `lib.options.mkOption`

Creates an Option declaration for use with the module system.

##### Inputs

**Attribute set**

containing none or some of the following attributes.

**`default`**

Optional default value used when no definition is given in the configuration.

**`defaultText`**

Substitute for documenting the `default`, if evaluating the default value during documentation rendering is not possible.

Can be any nix value that evaluates.

Usage with `lib.literalMD` or `lib.literalExpression` is supported

**`example`**

Optional example value used in the manual.

Can be any nix value that evaluates.

Usage with `lib.literalMD` or `lib.literalExpression` is supported

**`description`**

Optional string describing the option. This is required if option documentation is generated.

**`relatedPackages`**

Optional related packages used in the manual (see `genRelatedPackages` in `../nixos/lib/make-options-doc/default.nix`).

**`type`**

Optional option type, providing type-checking and value merging.

**`apply`**

Optional function that converts the option value to something else.

**`internal`**

Optional boolean indicating whether the option is for NixOS developers only.

**`visible`**

Optional, whether the option and/or sub-options show up in the manual. Use false to hide the option and any sub-options from submodules. Use “shallow” to hide only sub-options. Use “transparent” to hide this option, but not its sub-options. Default: true.

**`readOnly`**

Optional boolean indicating whether the option can be set only once.

##### Examples

Example 221.

lib.options.mkOption

usage example

Located at lib/options.nix:139 in `<nixpkgs>`.

#### `lib.options.mkEnableOption`

Creates an option declaration with a default value of `false`, and can be defined to `true`.

##### Inputs

**`name`**

Name for the created option

##### Examples

Example 222.

lib.options.mkEnableOption

usage example

Located at lib/options.nix:186 in `<nixpkgs>`.

#### `lib.options.mkPackageOption`

Creates an Option attribute set for an option that specifies the package a module should use for some purpose.

The package is specified in the third argument under `default` as a list of strings representing its attribute path in nixpkgs (or another package set). Because of this, you need to pass nixpkgs itself (usually `pkgs` in a module; alternatively to nixpkgs itself, another package set) as the first argument.

If you pass another package set you should set the `pkgsText` option. This option is used to display the expression for the package set. It is `"pkgs"` by default. If your expression is complex you should parenthesize it, as the `pkgsText` argument is usually immediately followed by an attribute lookup (`.`).

The second argument may be either a string or a list of strings. It provides the display name of the package in the description of the generated option (using only the last element if the passed value is a list) and serves as the fallback value for the `default` argument.

To include extra information in the description, pass `extraDescription` to append arbitrary text to the generated description.

You can also pass an `example` value, either a literal string or an attribute path.

The `default` argument can be omitted if the provided name is an attribute of pkgs (if `name` is a string) or a valid attribute path in pkgs (if `name` is a list). You can also set `default` to just a string in which case it is interpreted as an attribute name (a singleton attribute path, if you will).

If you wish to explicitly provide no default, pass `null` as `default`.

If you want users to be able to set no package, pass `nullable = true`. In this mode a `default = null` will not be interpreted as no default and is interpreted literally.

##### Inputs

**`pkgs`**

Package set (an instantiation of nixpkgs such as pkgs in modules or another package set)

**`name`**

Name for the package, shown in option description

**Structured function argument**

Attribute set containing the following attributes.

**`nullable`**

Optional whether the package can be null, for example to disable installing a package altogether. Default: `false`

**`default`**

Optional attribute path where the default package is located. Default: `name` If omitted will be copied from `name`

**`example`**

Optional string or an attribute path to use as an example. Default: `null`

**`extraDescription`**

Optional additional text to include in the option description. Default: `""`

**`pkgsText`**

Optional representation of the package set passed as pkgs. Default: `"pkgs"`

##### Type

```
mkPackageOption :: Pkgs -> (String | [String]) -> { nullable? :: Bool; default? :: String | [String]; example? :: Null | String | [String]; extraDescription? :: String; pkgsText? :: String; } -> Option
```

##### Examples

Example 223.

lib.options.mkPackageOption

usage example

Located at lib/options.nix:308 in `<nixpkgs>`.

#### `lib.options.mkSinkUndeclaredOptions`

This option accepts arbitrary definitions, but it does not produce an option value.

This is useful for sharing a module across different module sets without having to implement similar features as long as the values of the options are not accessed.

##### Inputs

**`attrs`**

Attribute set whose attributes override the argument to `mkOption`.

Located at lib/options.nix:360 in `<nixpkgs>`.

#### `lib.options.mergeDefaultOption`

A merge function that merges multiple definitions of an option into a single value

### Caution

This function is used as the default merge operation in `lib.types.mkOptionType`. In most cases, explicit usage of this function is unnecessary.

##### Inputs

**`loc`**

location of the option in the configuration as a list of strings.

e.g. `["boot" "loader "grub" "enable"]`

**`defs`**

list of definition values and locations.

e.g. `[ { file = "/foo.nix"; value = 1; } { file = "/bar.nix"; value = 2 } ]`

##### Example

Example 224.

lib.options.mergeDefaultOption

usage example

##### Merge behavior

Merging requires all definition values to have the same type.

- If all definitions are booleans, the result of a `foldl'` with the `or` operation is returned.
- If all definitions are strings, they are concatenated. (`lib.concatStrings`)
- If all definitions are integers and all are equal, the first one is returned.
- If all definitions are lists, they are concatenated. (`++`)
- If all definitions are attribute sets, they are merged. (`lib.mergeAttrs`)
- If all definitions are functions, the first function is applied to the result of the second function. (`f -> x: f x`)
- Otherwise, an error is thrown.

Located at lib/options.nix:422 in `<nixpkgs>`.

#### `lib.options.mergeOneOption`

Require a single definition.

### Warning

Does not perform nested checks, as this does not run the merge function!

Located at lib/options.nix:451 in `<nixpkgs>`.

#### `lib.options.mergeUniqueOption`

Require a single definition.

### Note

When the type is not checked completely by check, pass a merge function for further checking (of sub-attributes, etc).

##### Inputs

**`loc`**

2. Function argument

**`defs`**

3. Function argument

Located at lib/options.nix:470 in `<nixpkgs>`.

#### `lib.options.mergeEqualOption`

“Merge” option definitions by checking that they all have the same value.

##### Inputs

**`loc`**

1. Function argument

**`defs`**

2. Function argument

Located at lib/options.nix:499 in `<nixpkgs>`.

#### `lib.options.getValues`

Extracts values of all `value` keys of the given list.

##### Type

```
getValues :: [{ value :: a; ... }] -> [a]
```

##### Examples

Example 225.

getValues

usage example

Located at lib/options.nix:542 in `<nixpkgs>`.

#### `lib.options.getFiles`

Extracts values of all `file` keys of the given list

##### Type

```
getFiles :: [{ file :: a; ... }] -> [a]
```

##### Examples

Example 226.

getFiles

usage example

Located at lib/options.nix:564 in `<nixpkgs>`.

#### `lib.options.scrubOptionValue`

This function recursively removes all derivation attributes from `x` except for the `name` attribute.

This is to make the generation of `options.xml` much more efficient: the XML representation of derivations is very large (on the order of megabytes) and is not actually used by the manual generator.

This function was made obsolete by `renderOptionValue` and is kept for compatibility with out-of-tree code.

##### Inputs

**`x`**

1. Function argument

Located at lib/options.nix:645 in `<nixpkgs>`.

#### `lib.options.renderOptionValue`

Ensures that the given option value (default or example) is a `_type`d string by rendering Nix values to `literalExpression`s.

##### Inputs

**`v`**

1. Function argument

Located at lib/options.nix:671 in `<nixpkgs>`.

#### `lib.options.literalExpression`

For use in the `defaultText` and `example` option attributes. Causes the given string to be rendered verbatim in the documentation as Nix code. This is necessary for complex values, e.g. functions, or values that depend on other values or packages.

##### Examples

Example 227.

literalExpression

usage example

##### Inputs

**`text`**

The text to render as a Nix expression

Located at lib/options.nix:714 in `<nixpkgs>`.

#### `lib.options.literalCode`

For use in the `defaultText` and `example` option attributes. Causes the given string to be rendered verbatim in the documentation as a code block with the language bassed on the provided input tag.

If you wish to render Nix code, please see `literalExpression`.

##### Examples

Example 228.

literalCode

usage example

##### Inputs

**`languageTag`**

The language tag to use when producing the code block (i.e. `js`, `rs`, etc).

**`text`**

The text to render as a Nix expression

Located at lib/options.nix:759 in `<nixpkgs>`.

#### `lib.options.literalMD`

For use in the `defaultText` and `example` option attributes. Causes the given MD text to be inserted verbatim in the documentation, for when a `literalExpression` would be too hard to read.

##### Inputs

**`text`**

1. Function argument

Located at lib/options.nix:778 in `<nixpkgs>`.

#### `lib.options.showOption`

Convert an option, described as a list of the option parts to a human-readable version.

##### Inputs

**`parts`**

1. Function argument

##### Examples

Example 229.

showOption

usage example

Located at lib/options.nix:817 in `<nixpkgs>`.

#### `lib.options.showOptionWithDefLocs`

Pretty prints all option definition locations

##### Inputs

**`option`**

The option to pretty print

##### Examples

Example 230.

lib.options.showOptionWithDefLocs

usage example

##### Type

```
showOptionWithDefLocs :: { files :: [String]; loc :: [String]; ... } -> String
```

Located at lib/options.nix:905 in `<nixpkgs>`.

### lib.path: path functions

#### `lib.path.append`

Append a subpath string to a path.

Like `path + ("/" + string)` but safer, because it errors instead of returning potentially surprising results. More specifically, it checks that the first argument is a path value type, and that the second argument is a valid subpath string.

Laws:

- Not influenced by subpath normalisation:
  ```
append p s == append p (subpath.normalise s)
  ```

##### Inputs

**`path`**

The absolute path to append to

**`subpath`**

The subpath string to append

##### Type

```
append :: Path -> String -> Path
```

##### Examples

Example 231.

append

usage example

Located at lib/path/default.nix:236 in `<nixpkgs>`.

#### `lib.path.hasPrefix`

Whether the first path is a component-wise prefix of the second path.

Laws:

- `hasPrefix p q` is only true if `q == append p s` for some subpath `s`.
- `hasPrefix` is a non-strict partial order over the set of all path values.

##### Inputs

**`path1`**

1. Function argument

##### Type

```
hasPrefix :: Path -> Path -> Bool
```

##### Examples

Example 232.

hasPrefix

usage example

Located at lib/path/default.nix:286 in `<nixpkgs>`.

#### `lib.path.removePrefix`

Remove the first path as a component-wise prefix from the second path. The result is a normalised subpath string.

Laws:

- Inverts `append` for normalised subpath string:
  ```
removePrefix p (append p s) == subpath.normalise s
  ```

##### Inputs

**`path1`**

1. Function argument

##### Type

```
removePrefix :: Path -> Path -> String
```

##### Examples

Example 233.

removePrefix

usage example

Located at lib/path/default.nix:345 in `<nixpkgs>`.

#### `lib.path.splitRoot`

Split the filesystem root from a path. The result is an attribute set with these attributes:

- `root`: The filesystem root of the path, meaning that this directory has no parent directory.
- `subpath`: The normalised subpath string that when appended to `root` returns the original path.

Laws:

- Appending the `root` and `subpath` gives the original path:
  ```
p ==
  append
    (splitRoot p).root
    (splitRoot p).subpath
  ```
- Trying to get the parent directory of `root` using `dirOf` returns `root` itself:
  ```
dirOf (splitRoot p).root == (splitRoot p).root
  ```

##### Inputs

**`path`**

The path to split the root off of

##### Type

```
splitRoot :: Path -> { root :: Path; subpath :: String; }
```

##### Examples

Example 234.

splitRoot

usage example

Located at lib/path/default.nix:422 in `<nixpkgs>`.

#### `lib.path.hasStorePathPrefix`

Whether a path has a store path as a prefix.

### Note

As with all functions of this `lib.path` library, it does not work on paths in strings, which is how you’d typically get store paths.

Instead, this function only handles path values themselves, which occur when Nix files in the store use relative path expressions.

##### Inputs

**`path`**

1. Function argument

##### Type

```
hasStorePathPrefix :: Path -> Bool
```

##### Examples

Example 235.

hasStorePathPrefix

usage example

Located at lib/path/default.nix:492 in `<nixpkgs>`.

#### `lib.path.subpath.isValid`

Whether a value is a valid subpath string.

A subpath string points to a specific file or directory within an absolute base directory. It is a stricter form of a relative path that excludes `..` components, since those could escape the base directory.

- The value is a string.
- The string is not empty.
- The string doesn’t start with a `/`.
- The string doesn’t contain any `..` path components.

##### Inputs

**`value`**

The value to check

##### Type

```
subpath.isValid :: String -> Bool
```

##### Examples

Example 236.

subpath.isValid

usage example

Located at lib/path/default.nix:565 in `<nixpkgs>`.

#### `lib.path.subpath.join`

Join subpath strings together using `/`, returning a normalised subpath string.

Like `concatStringsSep "/"` but safer, specifically:

- All elements must be valid subpath strings.
- The result gets normalised.
- The edge case of an empty list gets properly handled by returning the neutral subpath `"./."`.

Laws:

- Associativity:
  ```
subpath.join [ x (subpath.join [ y z ]) ] == subpath.join [ (subpath.join [ x y ]) z ]
  ```
- Identity - `"./."` is the neutral element for normalised paths:
  ```
subpath.join [ ] == "./."
subpath.join [ (subpath.normalise p) "./." ] == subpath.normalise p
subpath.join [ "./." (subpath.normalise p) ] == subpath.normalise p
  ```
- Normalisation - the result is normalised:
  ```
subpath.join ps == subpath.normalise (subpath.join ps)
  ```
- For non-empty lists, the implementation is equivalent to normalising the result of `concatStringsSep "/"`. Note that the above laws can be derived from this one:
  ```
ps != [] -> subpath.join ps == subpath.normalise (concatStringsSep "/" ps)
  ```

##### Inputs

**`subpaths`**

The list of subpaths to join together

##### Type

```
subpath.join :: [String] -> String
```

##### Examples

Example 237.

subpath.join

usage example

Located at lib/path/default.nix:642 in `<nixpkgs>`.

#### `lib.path.subpath.components`

Split a subpath into its path component strings. Throw an error if the subpath isn’t valid. Note that the returned path components are also valid subpath strings, though they are intentionally not normalised.

Laws:

- Splitting a subpath into components and joining the components gives the same subpath but normalised:
  ```
subpath.join (subpath.components s) == subpath.normalise s
  ```

##### Inputs

**`subpath`**

The subpath string to split into components

##### Type

```
subpath.components :: String -> [String]
```

##### Examples

Example 238.

subpath.components

usage example

Located at lib/path/default.nix:702 in `<nixpkgs>`.

#### `lib.path.subpath.normalise`

Normalise a subpath. Throw an error if the subpath isn’t valid.

- Limit repeating `/` to a single one.
- Remove redundant `.` components.
- Remove trailing `/` and `/.`.
- Add leading `./`.

Laws:

- Idempotency - normalising multiple times gives the same result:
  ```
subpath.normalise (subpath.normalise p) == subpath.normalise p
  ```
- Uniqueness - there’s only a single normalisation for the paths that lead to the same file system node:
  ```
subpath.normalise p != subpath.normalise q -> $(realpath ${p}) != $(realpath ${q})
  ```
- Don’t change the result when appended to a Nix path value:
  ```
append base p == append base (subpath.normalise p)
  ```
- Don’t change the path according to `realpath`:
  ```
$(realpath ${p}) == $(realpath ${subpath.normalise p})
  ```
- Only error on invalid subpaths:
  ```
builtins.tryEval (subpath.normalise p)).success == subpath.isValid p
  ```

##### Inputs

**`subpath`**

The subpath string to normalise

##### Type

```
subpath.normalise :: String -> String
```

##### Examples

Example 239.

subpath.normalise

usage example

Located at lib/path/default.nix:799 in `<nixpkgs>`.

### lib.fetchers: functions which can be reused across fetchers

#### `lib.fetchers.normalizeHash`
