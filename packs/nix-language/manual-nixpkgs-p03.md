---
title: "Nixpkgs Reference Manual (part 3/6)"
source: https://nixos.org/manual/nixpkgs/stable/
domain: nix-language
license: CC-BY-SA-4.0
tags: nix language, nix lang, nixos, nixpkgs, nix expression
fetched: 2026-07-02
part: 3/6
---

## Nixpkgs Library Functions

Nixpkgs provides a standard library at `pkgs.lib`, or through `import <nixpkgs/lib>`.

### lib.asserts: assertion functions

#### `lib.asserts.assertMsg`

Throw if `pred` is false, else return `pred`. Intended to be used to augment asserts with helpful error messages.

##### Inputs

**`pred`**

Predicate that needs to succeed, otherwise `msg` is thrown

**`msg`**

Message to throw in case `pred` fails

##### Type

```
assertMsg :: Bool -> String -> Bool
```

##### Examples

Example 1.

lib.asserts.assertMsg

usage example

Located at lib/asserts.nix:50 in `<nixpkgs>`.

#### `lib.asserts.assertOneOf`

Specialized `assertMsg` for checking if `val` is one of the elements of the list `xs`. Useful for checking enums.

##### Inputs

**`name`**

The name of the variable the user entered `val` into, for inclusion in the error message

**`val`**

The value of what the user provided, to be compared against the values in `xs`

**`xs`**

The list of valid values

##### Type

```
assertOneOf :: String -> ComparableVal -> [ComparableVal] -> Bool
```

##### Examples

Example 2.

lib.asserts.assertOneOf

usage example

Located at lib/asserts.nix:91 in `<nixpkgs>`.

#### `lib.asserts.assertEachOneOf`

Specialized `assertMsg` for checking if every one of `vals` is one of the elements of the list `xs`. Useful for checking lists of supported attributes.

##### Inputs

**`name`**

The name of the variable the user entered `val` into, for inclusion in the error message

**`vals`**

The list of values of what the user provided, to be compared against the values in `xs`

**`xs`**

The list of valid values

##### Type

```
assertEachOneOf :: String -> [ComparableVal] -> [ComparableVal] -> Bool
```

##### Examples

Example 3.

lib.asserts.assertEachOneOf

usage example

Located at lib/asserts.nix:139 in `<nixpkgs>`.

#### `lib.asserts.checkAssertWarn`

Wrap a value with logic that throws an error when assertions fail and emits any warnings.

##### Inputs

**`assertions`**

A list of assertions. If any of their `assertion` attrs is `false`, their `message` attrs will be emitted in a `throw`.

**`warnings`**

A list of strings to emit as warnings. This function does no filtering on this list.

**`val`**

A value to return, wrapped in `warn`, if a `throw` is not necessary.

##### Type

```
checkAssertWarn :: [{ assertion :: Bool; message :: String; }] -> [String] -> a -> a
```

##### Examples

Example 4.

lib.asserts.checkAssertWarn

usage example

Located at lib/asserts.nix:192 in `<nixpkgs>`.

### lib.attrsets: attribute set functions

Operations on attribute sets.

#### `lib.attrsets.attrByPath`

Returns an attribute from nested attribute sets.

Nix has an attribute selection operator `.` which is sufficient for such queries, as long as the number of attributes is static. For example:

```
(x.a.b or 6) == attrByPath ["a" "b"] 6 x
# and
(x.${f p}."example.com" or 6) == attrByPath [ (f p) "example.com" ] 6 x
```

##### Inputs

**`attrPath`**

A list of strings representing the attribute path to return from `set`

**`default`**

Default value if `attrPath` does not resolve to an existing value

**`set`**

The nested attribute set to select values from

##### Type

```
attrByPath :: [String] -> Any -> AttrSet -> Any
```

##### Examples

Example 5.

lib.attrsets.attrByPath

usage example

Located at lib/attrsets.nix:88 in `<nixpkgs>`.

#### `lib.attrsets.hasAttrByPath`

Returns if an attribute from nested attribute set exists.

Nix has a has attribute operator `?`, which is sufficient for such queries, as long as the number of attributes is static. For example:

```
(x?a.b) == hasAttrByPath ["a" "b"] x
# and
(x?${f p}."example.com") == hasAttrByPath [ (f p) "example.com" ] x
```

**Laws**:

  ```
hasAttrByPath [] x == true
  ```

##### Inputs

**`attrPath`**

A list of strings representing the attribute path to check from `set`

**`set`**

The nested attribute set to check

##### Type

```
hasAttrByPath :: [String] -> AttrSet -> Bool
```

##### Examples

Example 6.

lib.attrsets.hasAttrByPath

usage example

Located at lib/attrsets.nix:156 in `<nixpkgs>`.

#### `lib.attrsets.longestValidPathPrefix`

Returns the longest prefix of an attribute path that refers to an existing attribute in a nesting of attribute sets.

Can be used after `mapAttrsRecursiveCond` to apply a condition, although this will evaluate the predicate function on sibling attributes as well.

Note that the empty attribute path is valid for all values, so this function only throws an exception if any of its inputs does.

**Laws**:

  ```
attrsets.longestValidPathPrefix [] x == []
  ```
  ```
hasAttrByPath (attrsets.longestValidPathPrefix p x) x == true
  ```

##### Inputs

**`attrPath`**

A list of strings representing the longest possible path that may be returned.

**`v`**

The nested attribute set to check.

##### Type

```
longestValidPathPrefix :: [String] -> AttrSet -> [String]
```

##### Examples

Example 7.

lib.attrsets.longestValidPathPrefix

usage example

Located at lib/attrsets.nix:225 in `<nixpkgs>`.

#### `lib.attrsets.setAttrByPath`

Create a new attribute set with `value` set at the nested attribute location specified in `attrPath`.

##### Inputs

**`attrPath`**

A list of strings representing the attribute path to set

**`value`**

The value to set at the location described by `attrPath`

##### Type

```
setAttrByPath :: [String] -> Any -> AttrSet
```

##### Examples

Example 8.

lib.attrsets.setAttrByPath

usage example

Located at lib/attrsets.nix:285 in `<nixpkgs>`.

#### `lib.attrsets.getAttrFromPath`

Like `attrByPath`, but without a default value. If it doesn’t find the path it will throw an error.

Nix has an attribute selection operator which is sufficient for such queries, as long as the number of attributes is static. For example:

```
x.a.b == getAttrFromPath ["a" "b"] x
# and
x.${f p}."example.com" == getAttrFromPath [ (f p) "example.com" ] x
```

##### Inputs

**`attrPath`**

A list of strings representing the attribute path to get from `set`

**`set`**

The nested attribute set to find the value in.

##### Type

```
getAttrFromPath :: [String] -> AttrSet -> Any
```

##### Examples

Example 9.

lib.attrsets.getAttrFromPath

usage example

Located at lib/attrsets.nix:335 in `<nixpkgs>`.

#### `lib.attrsets.concatMapAttrs`

Map each attribute in the given set and merge them into a new attribute set.

##### Inputs

**`f`**

1. Function argument

**`v`**

2. Function argument

##### Type

```
concatMapAttrs :: (String -> Any -> AttrSet) -> AttrSet -> AttrSet
```

##### Examples

Example 10.

lib.attrsets.concatMapAttrs

usage example

Located at lib/attrsets.nix:374 in `<nixpkgs>`.

#### `lib.attrsets.updateManyAttrsByPath`

Update or set specific paths of an attribute set.

Takes a list of updates to apply and an attribute set to apply them to, and returns the attribute set with the updates applied. Updates are represented as `{ path = ...; update = ...; }` values, where `path` is a list of strings representing the attribute path that should be updated, and `update` is a function that takes the old value at that attribute path as an argument and returns the new value it should be.

Properties:

- Updates to deeper attribute paths are applied before updates to more shallow attribute paths
- Multiple updates to the same attribute path are applied in the order they appear in the update list
- If any but the last `path` element leads into a value that is not an attribute set, an error is thrown
- If there is an update for an attribute path that doesn’t exist, accessing the argument in the update function causes an error, but intermediate attribute sets are implicitly created as needed

##### Type

```
updateManyAttrsByPath :: [{ path :: [String]; update :: (Any -> Any); }] -> AttrSet -> AttrSet
```

##### Examples

Example 11.

lib.attrsets.updateManyAttrsByPath

usage example

Located at lib/attrsets.nix:436 in `<nixpkgs>`.

#### `lib.attrsets.attrVals`

Returns the specified attributes from a set.

##### Inputs

**`nameList`**

The list of attributes to fetch from `set`. Each attribute name must exist on the attribute set

**`set`**

The set to get attribute values from

##### Type

```
attrVals :: [String] -> { [String] :: a } -> [a]
```

##### Examples

Example 12.

lib.attrsets.attrVals

usage example

Located at lib/attrsets.nix:535 in `<nixpkgs>`.

#### `lib.attrsets.attrValues`

Returns the values of all attributes in the given set, sorted by attribute name.

##### Type

```
attrValues :: { [String] :: a } -> [a]
```

##### Examples

Example 13.

lib.attrsets.attrValues

usage example

Located at lib/attrsets.nix:558 in `<nixpkgs>`.

#### `lib.attrsets.getAttrs`

Given a set of attribute names, return the set of the corresponding attributes from the given set.

##### Inputs

**`names`**

A list of attribute names to get out of `set`

**`set`**

The set to get the named attributes from

##### Type

```
getAttrs :: [String] -> { [String] :: a } -> { [String] :: a }
```

##### Examples

Example 14.

lib.attrsets.getAttrs

usage example

Located at lib/attrsets.nix:591 in `<nixpkgs>`.

#### `lib.attrsets.catAttrs`

Collect each attribute named `attr` from a list of attribute sets. Sets that don’t contain the named attribute are ignored.

##### Inputs

**`attr`**

The attribute name to get out of the sets.

**`list`**

The list of attribute sets to go through

##### Type

```
catAttrs :: String -> [{ [String] :: a }] -> [a]
```

##### Examples

Example 15.

lib.attrsets.catAttrs

usage example

Located at lib/attrsets.nix:624 in `<nixpkgs>`.

#### `lib.attrsets.filterAttrs`

Filter an attribute set by removing all attributes for which the given predicate return false.

##### Inputs

**`pred`**

Predicate taking an attribute name and an attribute value, which returns `true` to include the attribute, or `false` to exclude the attribute.

If possible, decide on `name` first and on `value` only if necessary. This avoids evaluating the value if the name is already enough, making it possible, potentially, to have the argument reference the return value. (Depending on context, that could still be considered a self reference by users; a common pattern in Nix.)

`filterAttrs` is occasionally the cause of infinite recursion in configuration systems that allow self-references. To support the widest range of user-provided logic, perform the `filterAttrs` call as late as possible. Typically that’s right before using it in a derivation, as opposed to an implicit conversion whose result is accessible to the user’s expressions.

**`set`**

The attribute set to filter

##### Type

```
filterAttrs :: (String -> a -> Bool) -> { [String] :: a } -> { [String] :: a }
```

##### Examples

Example 16.

lib.attrsets.filterAttrs

usage example

Located at lib/attrsets.nix:667 in `<nixpkgs>`.

#### `lib.attrsets.filterAttrsRecursive`

Filter an attribute set recursively by removing all attributes for which the given predicate return false.

##### Inputs

**`pred`**

Predicate taking an attribute name and an attribute value, which returns `true` to include the attribute, or `false` to exclude the attribute.

**`set`**

The attribute set to filter

##### Type

```
filterAttrsRecursive :: (String -> Any -> Bool) -> AttrSet -> AttrSet
```

##### Examples

Example 17.

lib.attrsets.filterAttrsRecursive

usage example

Located at lib/attrsets.nix:700 in `<nixpkgs>`.

#### `lib.attrsets.foldlAttrs`

Like `lib.lists.foldl'` but for attribute sets. Iterates over every name-value pair in the given attribute set. The result of the callback function is often called `acc` for accumulator. It is passed between callbacks from left to right and the final `acc` is the return value of `foldlAttrs`.

### Note

There is a completely different function `lib.foldAttrs` which has nothing to do with this function, despite the similar name.

##### Inputs

**`f`**

1. Function argument

**`init`**

2. Function argument

**`set`**

3. Function argument

##### Type

```
foldlAttrs :: ( a -> String -> b -> a ) -> a -> { [String] :: b } -> a
```

##### Examples

Example 18.

lib.attrsets.foldlAttrs

usage example

Located at lib/attrsets.nix:795 in `<nixpkgs>`.

#### `lib.attrsets.foldAttrs`

Apply fold functions to values grouped by key.

##### Inputs

**`op`**

A function, given a value and a collector combines the two.

**`nul`**

The starting value.

**`list_of_attrs`**

A list of attribute sets to fold together by key.

##### Type

```
foldAttrs :: (a -> b -> b) -> b -> [{ [String] :: a }] -> { [String] :: b }
```

##### Examples

Example 19.

lib.attrsets.foldAttrs

usage example

Located at lib/attrsets.nix:833 in `<nixpkgs>`.

#### `lib.attrsets.collect`

Recursively collect sets that verify a given predicate named `pred` from the set `attrs`. The recursion is stopped when the predicate is verified.

##### Inputs

**`pred`**

Given an attribute’s value, determine if recursion should stop.

**`attrs`**

The attribute set to recursively collect.

##### Type

```
collect :: (AttrSet -> Bool) -> AttrSet -> [Any]
```

##### Examples

Example 20.

lib.attrsets.collect

usage example

Located at lib/attrsets.nix:875 in `<nixpkgs>`.

#### `lib.attrsets.cartesianProduct`

Return the cartesian product of attribute set value combinations.

##### Inputs

**`attrsOfLists`**

Attribute set with attributes that are lists of values

##### Type

```
cartesianProduct :: { [String] :: [a] } -> [{ [String] :: a }]
```

##### Examples

Example 21.

lib.attrsets.cartesianProduct

usage example

Located at lib/attrsets.nix:915 in `<nixpkgs>`.

#### `lib.attrsets.mapCartesianProduct`

Return the result of function `f` applied to the cartesian product of attribute set value combinations. Equivalent to using `cartesianProduct` followed by `map`.

##### Inputs

**`f`**

A function, given an attribute set, it returns a new value.

**`attrsOfLists`**

Attribute set with attributes that are lists of values

##### Type

```
mapCartesianProduct :: ({ [String] :: a } -> b) -> { [String] :: a } -> [b]
```

##### Examples

Example 22.

lib.attrsets.mapCartesianProduct

usage example

Located at lib/attrsets.nix:955 in `<nixpkgs>`.

#### `lib.attrsets.nameValuePair`

Utility function that creates a `{name, value}` pair as expected by `builtins.listToAttrs`.

##### Inputs

**`name`**

Attribute name

**`value`**

Attribute value

##### Type

```
nameValuePair :: String -> a -> { name :: String; value :: a; }
```

##### Examples

Example 23.

lib.attrsets.nameValuePair

usage example

Located at lib/attrsets.nix:987 in `<nixpkgs>`.

#### `lib.attrsets.mapAttrs`

Apply a function to each element in an attribute set, creating a new attribute set.

##### Inputs

**`f`**

A function that takes an attribute name and its value, and returns the new value for the attribute.

**`attrset`**

The attribute set to iterate through.

##### Type

```
mapAttrs :: (String -> a -> b) -> { [String] :: a } -> { [String] :: b }
```

##### Examples

Example 24.

lib.attrsets.mapAttrs

usage example

Located at lib/attrsets.nix:1020 in `<nixpkgs>`.

#### `lib.attrsets.mapAttrs'`

Like `mapAttrs`, but allows the name of each attribute to be changed in addition to the value. The applied function should return both the new name and value as a `nameValuePair`.

##### Inputs

**`f`**

A function, given an attribute’s name and value, returns a new `nameValuePair`.

**`set`**

Attribute set to map over.

##### Type

```
mapAttrs' :: (String -> a -> { name :: String; value :: b; }) -> { [String] :: a } -> { [String] :: b }
```

##### Examples

Example 25.

lib.attrsets.mapAttrs'

usage example

Located at lib/attrsets.nix:1055 in `<nixpkgs>`.

#### `lib.attrsets.mapAttrsToList`

Call a function for each attribute in the given set and return the result in a list.

##### Inputs

**`f`**

A function, given an attribute’s name and value, returns a new value.

**`attrs`**

Attribute set to map over.

##### Type

```
mapAttrsToList :: (String -> a -> b) -> { [String] :: a } -> [b]
```

##### Examples

Example 26.

lib.attrsets.mapAttrsToList

usage example

Located at lib/attrsets.nix:1089 in `<nixpkgs>`.

#### `lib.attrsets.attrsToList`

Deconstruct an attrset to a list of name-value pairs as expected by `builtins.listToAttrs`. Each element of the resulting list is an attribute set with these attributes:

- `name` (string): The name of the attribute
- `value` (any): The value of the attribute

The following is always true:

```
builtins.listToAttrs (attrsToList attrs) == attrs
```

### Warning

The opposite is not always true. In general expect that

```
attrsToList (builtins.listToAttrs list) != list
```

This is because the `listToAttrs` removes duplicate names and doesn’t preserve the order of the list.

##### Inputs

**`set`**

The attribute set to deconstruct.

##### Type

```
attrsToList :: { [String] :: a } -> [{ name :: String; value :: a; }]
```

##### Examples

Example 27.

lib.attrsets.attrsToList

usage example

Located at lib/attrsets.nix:1134 in `<nixpkgs>`.

#### `lib.attrsets.mapAttrsRecursive`

Like `mapAttrs`, except that it recursively applies itself to the *leaf* attributes of a potentially-nested attribute set: the second argument of the function will never be an attrset. Also, the first argument of the mapping function is a *list* of the attribute names that form the path to the leaf attribute.

For a function that gives you control over what counts as a leaf, see `mapAttrsRecursiveCond`.

Example 28. Map over leaf attributes

##### Type

```
mapAttrsRecursive :: ([String] -> a -> b) -> AttrSet -> AttrSet
```

Located at lib/attrsets.nix:1161 in `<nixpkgs>`.

#### `lib.attrsets.mapAttrsRecursiveCond`

Like `mapAttrsRecursive`, but it takes an additional predicate that tells it whether to recurse into an attribute set. If the predicate returns false, `mapAttrsRecursiveCond` does not recurse, but instead applies the mapping function. If the predicate returns true, it does recurse, and does not apply the mapping function.

Example 29. Map over an leaf attributes defined by a condition

##### Type

```
mapAttrsRecursiveCond :: (AttrSet -> Bool) -> ([String] -> a -> b) -> AttrSet -> AttrSet
```

Located at lib/attrsets.nix:1186 in `<nixpkgs>`.

#### `lib.attrsets.mapAttrsToListRecursive`

Apply a function to each leaf (non‐attribute‐set attribute) of a tree of nested attribute sets, returning the results of the function as a list, ordered lexicographically by their attribute paths.

Like `mapAttrsRecursive`, but concatenates the mapping function results into a list.

##### Inputs

**`f`**

Mapping function which, given an attribute’s path and value, returns a new value.

This value will be an element of the list returned by `mapAttrsToListRecursive`.

The first argument to the mapping function is a list of attribute names forming the path to the leaf attribute. The second argument is the leaf attribute value, which will never be an attribute set.

**`set`**

Attribute set to map over.

##### Type

```
mapAttrsToListRecursive :: ([String] -> a -> b) -> AttrSet -> [b]
```

##### Examples

Example 30.

lib.attrsets.mapAttrsToListRecursive

usage example

Located at lib/attrsets.nix:1241 in `<nixpkgs>`.

#### `lib.attrsets.mapAttrsToListRecursiveCond`

Determine the nodes of a tree of nested attribute sets by applying a predicate, then apply a function to the leaves, returning the results as a list, ordered lexicographically by their attribute paths.

Like `mapAttrsToListRecursive`, but takes an additional predicate to decide whether to recurse into an attribute set.

Unlike `mapAttrsRecursiveCond` this predicate receives the attribute path as its first argument, in addition to the attribute set.

##### Inputs

**`pred`**

Predicate to decide whether to recurse into an attribute set.

If the predicate returns true, `mapAttrsToListRecursiveCond` recurses into the attribute set. If the predicate returns false, it does not recurse but instead applies the mapping function, treating the attribute set as a leaf.

The first argument to the predicate is a list of attribute names forming the path to the attribute set. The second argument is the attribute set.

**`f`**

Mapping function which, given an attribute’s path and value, returns a new value.

This value will be an element of the list returned by `mapAttrsToListRecursiveCond`.

The first argument to the mapping function is a list of attribute names forming the path to the leaf attribute. The second argument is the leaf attribute value, which may be an attribute set if the predicate returned false.

**`set`**

Attribute set to map over.

##### Type

```
mapAttrsToListRecursiveCond :: ([String] -> AttrSet -> Bool) -> ([String] -> a -> b) -> AttrSet -> [b]
```

##### Examples

Example 31.

lib.attrsets.mapAttrsToListRecursiveCond

usage example

Located at lib/attrsets.nix:1308 in `<nixpkgs>`.

#### `lib.attrsets.genAttrs`

Generate an attribute set by mapping a function over a list of attribute names.

##### Inputs

**`names`**

Names of values in the resulting attribute set.

**`f`**

A function, given the name of the attribute, returns the attribute’s value.

##### Type

```
genAttrs :: [String] -> (String -> a) -> { [String] :: a }
```

##### Examples

Example 32.

lib.attrsets.genAttrs

usage example

Located at lib/attrsets.nix:1348 in `<nixpkgs>`.

#### `lib.attrsets.genAttrs'`

Like `genAttrs`, but allows the name of each attribute to be specified in addition to the value. The applied function should return both the new name and value as a `nameValuePair`.

### Warning

In case of attribute name collision the first entry determines the value, all subsequent conflicting entries for the same name are silently ignored.

##### Inputs

**`xs`**

A list of strings `s` used as generator.

**`f`**

A function, given a string `s` from the list `xs`, returns a new `nameValuePair`.

##### Type

```
genAttrs' :: [a] -> (a -> { name :: String; value :: b; }) -> { [String] :: b }
```

##### Examples

Example 33.

lib.attrsets.genAttrs'

usage example

Located at lib/attrsets.nix:1385 in `<nixpkgs>`.

#### `lib.attrsets.isDerivation`

Check whether the argument is a derivation. Any set with `{ type = "derivation"; }` counts as a derivation.

##### Inputs

**`value`**

Value to check.

##### Type

```
isDerivation :: Any -> Bool
```

##### Examples

Example 34.

lib.attrsets.isDerivation

usage example

Located at lib/attrsets.nix:1417 in `<nixpkgs>`.

#### `lib.attrsets.toDerivation`

Converts a store path to a fake derivation.

##### Inputs

**`path`**

A store path to convert to a derivation.

##### Type

```
toDerivation :: Path -> Derivation
```

Located at lib/attrsets.nix:1434 in `<nixpkgs>`.

#### `lib.attrsets.optionalAttrs`

If `cond` is true, return the attribute set `as`, otherwise an empty attribute set.

##### Inputs

**`cond`**

Condition under which the `as` attribute set is returned.

**`as`**

The attribute set to return if `cond` is `true`.

##### Type

```
optionalAttrs :: Bool -> AttrSet -> AttrSet
```

##### Examples

Example 35.

lib.attrsets.optionalAttrs

usage example

Located at lib/attrsets.nix:1482 in `<nixpkgs>`.

#### `lib.attrsets.zipAttrsWithNames`

Merge sets of attributes and use the function `f` to merge attributes values.

##### Inputs

**`names`**

List of attribute names to zip.

**`f`**

A function, accepts an attribute name, all the values, and returns a combined value.

**`sets`**

List of values from the list of attribute sets.

##### Type

```
zipAttrsWithNames :: [String] -> (String -> [a] -> b) -> [{ [String] :: a }] -> { [String] :: b }
```

##### Examples

Example 36.

lib.attrsets.zipAttrsWithNames

usage example

Located at lib/attrsets.nix:1519 in `<nixpkgs>`.

#### `lib.attrsets.zipAttrsWith`

Merge sets of attributes and use the function `f` to merge attribute values. Like `lib.attrsets.zipAttrsWithNames` with all key names are passed for `names`.

Implementation note: Common names appear multiple times in the list of names, hopefully this does not affect the system because the maximal laziness avoid computing twice the same expression and `listToAttrs` does not care about duplicated attribute names.

##### Type

```
zipAttrsWith :: (String -> [a] -> b) -> [{ [String] :: a }] -> { [String] :: b }
```

##### Examples

Example 37.

lib.attrsets.zipAttrsWith

usage example

Located at lib/attrsets.nix:1554 in `<nixpkgs>`.

#### `lib.attrsets.zipAttrs`

Merge sets of attributes and combine each attribute value in to a list.

Like `lib.attrsets.zipAttrsWith` with `(name: values: values)` as the function.

##### Type

```
zipAttrs :: [{ [String] :: a }] -> { [String] :: [a] }
```

##### Examples

Example 38.

lib.attrsets.zipAttrs

usage example

Located at lib/attrsets.nix:1579 in `<nixpkgs>`.

#### `lib.attrsets.mergeAttrsList`

Merge a list of attribute sets together using the `//` operator. In case of duplicate attributes, values from later list elements take precedence over earlier ones. The result is the same as `foldl mergeAttrs { }`, but the performance is better for large inputs. For n list elements, each with an attribute set containing m unique attributes, the complexity of this operation is O(nm log n).

##### Inputs

**`list`**

1. Function argument

##### Type

```
mergeAttrsList :: [AttrSet] -> AttrSet
```

##### Examples

Example 39.

lib.attrsets.mergeAttrsList

usage example

Located at lib/attrsets.nix:1612 in `<nixpkgs>`.

#### `lib.attrsets.recursiveUpdateUntil`

Update `lhs` so that `rhs` wins for any given attribute path that occurs in both.

Unlike the `//` (update) operator, which operates on a single attribute set, This function views its operands `lhs` and `rhs` as a mapping from attribute *paths* to values.

The caller-provided function `pred` decides whether any given path is one of the following:

- `true`: a value in the mapping
- `false`: an attribute set whose purpose is to create the nesting structure.

##### Inputs

**`pred`**

Predicate function (of type `List String -> Any -> Any -> Bool`)

Inputs:

- `path : List String`: the path to the current attribute as a list of strings for attribute names
- `lhsAtPath : Any`: the value at that path in `lhs`; same as `getAttrFromPath path lhs`
- `rhsAtPath : Any`: the value at that path in `rhs`; same as `getAttrFromPath path rhs`

Output:

- `true`: `path` points to a value in the mapping, and `rhsAtPath` will appear in the return value of `recursiveUpdateUntil`
- `false`: `path` is part of the nesting structure and will be an attrset in the return value of `recursiveUpdateUntil`

`pred` is only called for `path`s that extend prefixes for which `pred` returned `false`.

**`lhs`**

Left attribute set of the update.

**`rhs`**

Right attribute set of the update.

##### Type

```
recursiveUpdateUntil :: ([String] -> AttrSet -> AttrSet -> Bool) -> AttrSet -> AttrSet -> AttrSet
```

##### Examples

Example 40.

lib.attrsets.recursiveUpdateUntil

usage example

Located at lib/attrsets.nix:1706 in `<nixpkgs>`.

#### `lib.attrsets.recursiveUpdate`

A recursive variant of the update operator `//`. The recursion stops when one of the attribute values is not an attribute set, in which case the right hand side value takes precedence over the left hand side value.

##### Inputs

**`lhs`**

Left attribute set of the merge.

**`rhs`**

Right attribute set of the merge.

##### Type

```
recursiveUpdate :: AttrSet -> AttrSet -> AttrSet
```

##### Examples

Example 41.

lib.attrsets.recursiveUpdate

usage example

Located at lib/attrsets.nix:1766 in `<nixpkgs>`.

#### `lib.attrsets.matchAttrs`

Recurse into every attribute set of the first argument and check that:

- Each attribute path also exists in the second argument.
- If the attribute’s value is not a nested attribute set, it must have the same value in the right argument.

##### Inputs

**`pattern`**

Attribute set structure to match

**`attrs`**

Attribute set to check

##### Type

```
matchAttrs :: AttrSet -> AttrSet -> Bool
```

##### Examples

Example 42.

lib.attrsets.matchAttrs

usage example

Located at lib/attrsets.nix:1805 in `<nixpkgs>`.

#### `lib.attrsets.overrideExisting`

Override only the attributes that are already present in the old set useful for deep-overriding.

##### Inputs

**`old`**

Original attribute set

**`new`**

Attribute set with attributes to override in `old`.

##### Type

```
overrideExisting :: AttrSet -> AttrSet -> AttrSet
```

##### Examples

Example 43.

lib.attrsets.overrideExisting

usage example

Located at lib/attrsets.nix:1858 in `<nixpkgs>`.

#### `lib.attrsets.showAttrPath`

Turns a list of strings into a human-readable description of those strings represented as an attribute path. The result of this function is not intended to be machine-readable. Create a new attribute set with `value` set at the nested attribute location specified in `attrPath`.

##### Inputs

**`path`**

Attribute path to render to a string

##### Type

```
showAttrPath :: [String] -> String
```

##### Examples

Example 44.

lib.attrsets.showAttrPath

usage example

Located at lib/attrsets.nix:1891 in `<nixpkgs>`.

#### `lib.attrsets.getOutput`

Get a package output. If no output is found, fallback to `.out` and then to the default. The function is idempotent: `getOutput "b" (getOutput "a" p) == getOutput "a" p`.

##### Inputs

**`output`**

1. Function argument

**`pkg`**

2. Function argument

##### Type

```
getOutput :: String -> :: Derivation -> Derivation
```

##### Examples

Example 45.

lib.attrsets.getOutput

usage example

Located at lib/attrsets.nix:1927 in `<nixpkgs>`.

#### `lib.attrsets.getFirstOutput`

Get the first of the `outputs` provided by the package, or the default. This function is aligned with `_overrideFirst()` from the `multiple-outputs.sh` setup hook. Like `getOutput`, the function is idempotent.

##### Inputs

**`outputs`**

1. Function argument

**`pkg`**

2. Function argument

##### Type

```
getFirstOutput :: [String] -> Derivation -> Derivation
```

##### Examples

Example 46.

lib.attrsets.getFirstOutput

usage example

Located at lib/attrsets.nix:1963 in `<nixpkgs>`.

#### `lib.attrsets.getBin`

Get a package’s `bin` output. If the output does not exist, fallback to `.out` and then to the default.

##### Inputs

**`pkg`**

The package whose `bin` output will be retrieved.

##### Type

```
getBin :: Derivation -> Derivation
```

##### Examples

Example 47.

lib.attrsets.getBin

usage example

Located at lib/attrsets.nix:1998 in `<nixpkgs>`.

#### `lib.attrsets.getLib`

Get a package’s `lib` output. If the output does not exist, fallback to `.out` and then to the default.

##### Inputs

**`pkg`**

The package whose `lib` output will be retrieved.

##### Type

```
getLib :: Derivation -> Derivation
```

##### Examples

Example 48.

lib.attrsets.getLib

usage example

Located at lib/attrsets.nix:2027 in `<nixpkgs>`.

#### `lib.attrsets.getStatic`

Get a package’s `static` output. If the output does not exist, fallback to `.lib`, then to `.out`, and then to the default.

##### Inputs

**`pkg`**

The package whose `static` output will be retrieved.

##### Type

```
getStatic :: Derivation -> Derivation
```

##### Examples

Example 49.

lib.attrsets.getStatic

usage example

Located at lib/attrsets.nix:2056 in `<nixpkgs>`.

#### `lib.attrsets.getDev`

Get a package’s `dev` output. If the output does not exist, fallback to `.out` and then to the default.

##### Inputs

**`pkg`**

The package whose `dev` output will be retrieved.

##### Type

```
getDev :: Derivation -> Derivation
```

##### Examples

Example 50.

lib.attrsets.getDev

usage example

Located at lib/attrsets.nix:2089 in `<nixpkgs>`.

#### `lib.attrsets.getInclude`

Get a package’s `include` output. If the output does not exist, fallback to `.dev`, then to `.out`, and then to the default.

##### Inputs

**`pkg`**

The package whose `include` output will be retrieved.

##### Type

```
getInclude :: Derivation -> Derivation
```

##### Examples

Example 51.

lib.attrsets.getInclude

usage example

Located at lib/attrsets.nix:2118 in `<nixpkgs>`.

#### `lib.attrsets.getMan`

Get a package’s `man` output. If the output does not exist, fallback to `.out` and then to the default.

##### Inputs

**`pkg`**

The package whose `man` output will be retrieved.

##### Type

```
getMan :: Derivation -> Derivation
```

##### Examples

Example 52.

lib.attrsets.getMan

usage example

Located at lib/attrsets.nix:2151 in `<nixpkgs>`.

#### `lib.attrsets.chooseDevOutputs`

Pick the outputs of packages to place in `buildInputs`

##### Inputs

**`pkgs`**

List of packages.

##### Type

```
chooseDevOutputs :: [Derivation] -> [Derivation]
```

Located at lib/attrsets.nix:2168 in `<nixpkgs>`.

#### `lib.attrsets.recurseIntoAttrs`

Make various Nix tools consider the contents of the resulting attribute set when looking for what to build, find, etc.

This function only affects a single attribute set; it does not apply itself recursively for nested attribute sets.

##### Inputs

**`attrs`**

An attribute set to scan for derivations.

##### Type

```
recurseIntoAttrs :: AttrSet -> AttrSet
```

##### Examples

Example 53.

lib.attrsets.recurseIntoAttrs

usage example

Located at lib/attrsets.nix:2204 in `<nixpkgs>`.

#### `lib.attrsets.dontRecurseIntoAttrs`

Undo the effect of `recurseIntoAttrs`.

##### Inputs

**`attrs`**

An attribute set to not scan for derivations.

##### Type

```
dontRecurseIntoAttrs :: AttrSet -> AttrSet
```

Located at lib/attrsets.nix:2221 in `<nixpkgs>`.

#### `lib.attrsets.unionOfDisjoint`

`unionOfDisjoint x y` is equal to `x // y`, but accessing attributes present in both `x` and `y` will throw an error. This operator is commutative, unlike `//`.

##### Inputs

**`x`**

1. Function argument

**`y`**

2. Function argument

##### Type

```
unionOfDisjoint :: AttrSet -> AttrSet -> AttrSet
```

Located at lib/attrsets.nix:2243 in `<nixpkgs>`.

### lib.strings: string manipulation functions

String manipulation functions.

#### `lib.strings.join`

Concatenates a list of strings with a separator between each element.

##### Inputs

**`sep`**

Separator to add between elements

**`list`**

List of strings that will be joined

##### Type

```
join :: String -> [String] -> String
```

##### Examples

Example 54.

lib.strings.join

usage example

Located at lib/strings.nix:73 in `<nixpkgs>`.

#### `lib.strings.concatStrings`

Concatenate a list of strings.

##### Type

```
concatStrings :: [String] -> String
```

##### Examples

Example 55.

lib.strings.concatStrings

usage example

Located at lib/strings.nix:95 in `<nixpkgs>`.

#### `lib.strings.concatMapStrings`

Map a function over a list and concatenate the resulting strings.

##### Inputs

**`f`**

1. Function argument

**`list`**

2. Function argument

##### Type

```
concatMapStrings :: (a -> String) -> [a] -> String
```

##### Examples

Example 56.

lib.strings.concatMapStrings

usage example

Located at lib/strings.nix:125 in `<nixpkgs>`.

#### `lib.strings.concatImapStrings`

Like `concatMapStrings` except that the function `f` also gets the position as a parameter.

##### Inputs

**`f`**

1. Function argument

**`list`**

2. Function argument

##### Type

```
concatImapStrings :: (Int -> a -> String) -> [a] -> String
```

##### Examples

Example 57.

lib.strings.concatImapStrings

usage example

Located at lib/strings.nix:156 in `<nixpkgs>`.

#### `lib.strings.intersperse`

Place an element between each element of a list

##### Inputs

**`separator`**

Separator to add between elements

**`list`**

Input list

##### Type

```
intersperse :: a -> [a] -> [a]
```

##### Examples

Example 58.

lib.strings.intersperse

usage example

Located at lib/strings.nix:186 in `<nixpkgs>`.

#### `lib.strings.concatStringsSep`

Concatenate a list of strings with a separator between each element

##### Inputs

**`sep`**

Separator to add between elements

**`list`**

List of input strings

##### Type

```
concatStringsSep :: String -> [String] -> String
```

##### Examples

Example 59.

lib.strings.concatStringsSep

usage example

Located at lib/strings.nix:226 in `<nixpkgs>`.

#### `lib.strings.concatMapStringsSep`

Maps a function over a list of strings and then concatenates the result with the specified separator interspersed between elements.

##### Inputs

**`sep`**

Separator to add between elements

**`f`**

Function to map over the list

**`list`**

List of input strings

##### Type

```
concatMapStringsSep :: String -> (a -> String) -> [a] -> String
```

##### Examples

Example 60.

lib.strings.concatMapStringsSep

usage example

Located at lib/strings.nix:261 in `<nixpkgs>`.

#### `lib.strings.concatImapStringsSep`

Same as `concatMapStringsSep`, but the mapping function additionally receives the position of its argument.

##### Inputs

**`sep`**

Separator to add between elements

**`f`**

Function that receives elements and their positions

**`list`**

List of input strings

##### Type

```
concatIMapStringsSep :: String -> (Int -> a -> String) -> [a] -> String
```

##### Examples

Example 61.

lib.strings.concatImapStringsSep

usage example

Located at lib/strings.nix:297 in `<nixpkgs>`.

#### `lib.strings.concatMapAttrsStringSep`

Like `concatMapStringsSep` but takes an attribute set instead of a list.

##### Inputs

**`sep`**

Separator to add between item strings

**`f`**

Function that takes each key and value and return a string

**`attrs`**

Attribute set to map from

##### Type

```
concatMapAttrsStringSep :: String -> (String -> a -> String) -> { [String] :: a } -> String
```

##### Examples

Example 62.

lib.strings.concatMapAttrsStringSep

usage example

Located at lib/strings.nix:334 in `<nixpkgs>`.

#### `lib.strings.concatLines`

Concatenate a list of strings, adding a newline at the end of each one.

##### Inputs

**`list`**

List of strings. Any element that is not a string will be implicitly converted to a string.

##### Type

```
concatLines :: [String] -> String
```

##### Examples

Example 63.

lib.strings.concatLines

usage example

Located at lib/strings.nix:363 in `<nixpkgs>`.

#### `lib.strings.replaceString`

Given string `s`, replace every occurrence of the string `from` with the string `to`.

##### Inputs

**`from`**

The string to be replaced

**`to`**

The string to replace with

**`s`**

The original string where replacements will be made

##### Type

```
replaceString :: String -> String -> String -> String
```

##### Examples

Example 64.

lib.strings.replaceString

usage example

Located at lib/strings.nix:398 in `<nixpkgs>`.

#### `lib.strings.replicate`

Repeat a string `n` times, and concatenate the parts into a new string.

##### Inputs

**`n`**

1. Function argument

**`s`**

2. Function argument

##### Type

```
replicate :: Int -> String -> String
```

##### Examples

Example 65.

lib.strings.replicate

usage example

Located at lib/strings.nix:431 in `<nixpkgs>`.

#### `lib.strings.trim`

Remove leading and trailing whitespace from a string `s`.

Whitespace is defined as any of the following characters: " ", “\t” “\r” “\n”

##### Inputs

**`s`**

The string to trim

##### Type

```
trim :: String -> String
```

##### Examples

Example 66.

lib.strings.trim

usage example

Located at lib/strings.nix:461 in `<nixpkgs>`.

#### `lib.strings.trimWith`

Remove leading and/or trailing whitespace from a string `s`.

To remove both leading and trailing whitespace, you can also use `trim`

Whitespace is defined as any of the following characters: " ", “\t” “\r” “\n”

##### Inputs

**`config` (Attribute set)**

**`start`**

Whether to trim leading whitespace (`false` by default)

**`end`**

Whether to trim trailing whitespace (`false` by default)

**`s`**

The string to trim

##### Type

```
trimWith :: { start :: Bool; end :: Bool; } -> String -> String
```

##### Examples

Example 67.

lib.strings.trimWith

usage example

Located at lib/strings.nix:505 in `<nixpkgs>`.

#### `lib.strings.makeSearchPath`

Construct a Unix-style, colon-separated search path consisting of the given `subDir` appended to each of the given paths.

##### Inputs

**`subDir`**

Directory name to append

**`paths`**

List of base paths

##### Type

```
makeSearchPath :: String -> [String] -> String
```

##### Examples

Example 68.

lib.strings.makeSearchPath

usage example

Located at lib/strings.nix:566 in `<nixpkgs>`.

#### `lib.strings.makeSearchPathOutput`

Construct a Unix-style search path by appending the given `subDir` to the specified `output` of each of the packages.

If no output by the given name is found, fallback to `.out` and then to the default.

##### Inputs

**`output`**

Package output to use

**`subDir`**

Directory name to append

**`pkgs`**

List of packages

##### Type

```
makeSearchPathOutput :: String -> String -> [Derivation] -> String
```

##### Examples

Example 69.

lib.strings.makeSearchPathOutput

usage example

Located at lib/strings.nix:604 in `<nixpkgs>`.

#### `lib.strings.makeLibraryPath`

Construct a library search path (such as RPATH) containing the libraries for a set of packages

##### Inputs

**`packages`**

List of packages

##### Type

```
makeLibraryPath :: [Derivation] -> String
```

##### Examples

Example 70.

lib.strings.makeLibraryPath

usage example

Located at lib/strings.nix:637 in `<nixpkgs>`.

#### `lib.strings.makeIncludePath`

Construct an include search path (such as C_INCLUDE_PATH) containing the header files for a set of packages or paths.

##### Inputs

**`packages`**

List of packages

##### Type

```
makeIncludePath :: [Derivation] -> String
```

##### Examples

Example 71.

lib.strings.makeIncludePath

usage example

Located at lib/strings.nix:668 in `<nixpkgs>`.

#### `lib.strings.makeBinPath`

Construct a binary search path (such as $PATH) containing the binaries for a set of packages.

##### Inputs

**`packages`**

List of packages

##### Type

```
makeBinPath :: [Derivation] -> String
```

##### Examples

Example 72.

lib.strings.makeBinPath

usage example

Located at lib/strings.nix:696 in `<nixpkgs>`.

#### `lib.strings.normalizePath`

Normalize path, removing extraneous /s

##### Inputs

**`s`**

1. Function argument

##### Type

```
normalizePath :: String -> String
```

##### Examples

Example 73.

lib.strings.normalizePath

usage example

Located at lib/strings.nix:723 in `<nixpkgs>`.

#### `lib.strings.optionalString`

Depending on the boolean `cond`, return either the given string or the empty string. Useful to concatenate against a bigger string.

##### Inputs

**`cond`**

Condition

**`string`**

String to return if condition is true

##### Type

```
optionalString :: Bool -> String -> String
```

##### Examples

Example 74.

lib.strings.optionalString

usage example

Located at lib/strings.nix:766 in `<nixpkgs>`.

#### `lib.strings.hasPrefix`

Determine whether a string has given prefix.

##### Inputs

**`pref`**

Prefix to check for

**`str`**

Input string

##### Type

```
hasPrefix :: String -> String -> Bool
```

##### Examples

Example 75.

lib.strings.hasPrefix

usage example

Located at lib/strings.nix:798 in `<nixpkgs>`.

#### `lib.strings.hasSuffix`

Determine whether a string has given suffix.

##### Inputs

**`suffix`**

Suffix to check for

**`content`**

Input string

##### Type

```
hasSuffix :: String -> String -> Bool
```

##### Examples

Example 76.

lib.strings.hasSuffix

usage example

Located at lib/strings.nix:841 in `<nixpkgs>`.

#### `lib.strings.hasInfix`

Determine whether a string contains the given infix

##### Inputs

**`infix`**

1. Function argument

**`content`**

2. Function argument

##### Type

```
hasInfix :: String -> String -> Bool
```

##### Examples

Example 77.

lib.strings.hasInfix

usage example

Located at lib/strings.nix:891 in `<nixpkgs>`.

#### `lib.strings.stringToCharacters`

Convert a string `s` to a list of characters (i.e. singleton strings). This allows you to, e.g., map a function over each character. However, note that this will likely be horribly inefficient; Nix is not a general purpose programming language. Complex string manipulations should, if appropriate, be done in a derivation. Also note that Nix treats strings as a list of bytes and thus doesn’t handle unicode.

##### Inputs

**`s`**

1. Function argument

##### Type

```
stringToCharacters :: String -> [String]
```

##### Examples

Example 78.

lib.strings.stringToCharacters

usage example

Located at lib/strings.nix:938 in `<nixpkgs>`.

#### `lib.strings.stringAsChars`

Manipulate a string character by character and replace them by strings before concatenating the results.

##### Inputs

**`f`**

Function to map over each individual character

**`s`**

Input string

##### Type

```
stringAsChars :: (String -> String) -> String -> String
```

##### Examples

Example 79.

lib.strings.stringAsChars

usage example

Located at lib/strings.nix:969 in `<nixpkgs>`.

#### `lib.strings.charToInt`

Convert char to ascii value, must be in printable range

##### Inputs

**`c`**

1. Function argument

##### Type

```
charToInt :: String -> Int
```

##### Examples

Example 80.

lib.strings.charToInt

usage example

Located at lib/strings.nix:1003 in `<nixpkgs>`.

#### `lib.strings.escape`

Escape occurrence of the elements of `list` in `string` by prefixing it with a backslash.

##### Inputs

**`list`**

1. Function argument

**`string`**

2. Function argument

##### Type

```
escape :: [String] -> String -> String
```

##### Examples

Example 81.

lib.strings.escape

usage example

Located at lib/strings.nix:1034 in `<nixpkgs>`.

#### `lib.strings.escapeC`

Escape occurrence of the element of `list` in `string` by converting to its ASCII value and prefixing it with \x. Only works for printable ascii characters.

##### Inputs

**`list`**

1. Function argument

**`string`**

2. Function argument

##### Type

```
escapeC :: [String] -> String -> String
```

##### Examples

Example 82.

lib.strings.escapeC

usage example

Located at lib/strings.nix:1066 in `<nixpkgs>`.

#### `lib.strings.escapeURL`

Escape the `string` so it can be safely placed inside a URL query.

##### Inputs

**`string`**

1. Function argument

##### Type

```
escapeURL :: String -> String
```

##### Examples

Example 83.

lib.strings.escapeURL

usage example

Located at lib/strings.nix:1098 in `<nixpkgs>`.

#### `lib.strings.escapeShellArg`

Quote `string` to be used safely within the Bourne shell if it has any special characters.

##### Inputs

**`string`**

1. Function argument

##### Type

```
escapeShellArg :: String -> String
```

##### Examples

Example 84.

lib.strings.escapeShellArg

usage example

Located at lib/strings.nix:1200 in `<nixpkgs>`.

#### `lib.strings.escapeShellArgs`

Quote all arguments that have special characters to be safely passed to the Bourne shell.

##### Inputs

**`args`**

1. Function argument

##### Type

```
escapeShellArgs :: [String] -> String
```

##### Examples

Example 85.

lib.strings.escapeShellArgs

usage example

Located at lib/strings.nix:1236 in `<nixpkgs>`.

#### `lib.strings.isValidPosixName`

Test whether the given `name` is a valid POSIX shell variable name.

##### Inputs

**`name`**

1. Function argument

##### Type

```
isValidPosixName :: String -> Bool
```

##### Examples

Example 86.

lib.strings.isValidPosixName

usage example

Located at lib/strings.nix:1265 in `<nixpkgs>`.

#### `lib.strings.toShellVar`

Translate a Nix value into a shell variable declaration, with proper escaping.

The value can be a string (mapped to a regular variable), a list of strings (mapped to a Bash-style array) or an attribute set of strings (mapped to a Bash-style associative array). Note that “string” includes string-coercible values like paths or derivations.

Strings are translated into POSIX sh-compatible code; lists and attribute sets assume a shell that understands Bash syntax (e.g. Bash or ZSH).

##### Inputs

**`name`**

1. Function argument

**`value`**

2. Function argument

##### Type

```
toShellVar :: String -> (String | [String] | { [String] :: String }) -> String
```

##### Examples

Example 87.

lib.strings.toShellVar

usage example

Located at lib/strings.nix:1305 in `<nixpkgs>`.

#### `lib.strings.toShellVars`

Translate an attribute set `vars` into corresponding shell variable declarations using `toShellVar`.

##### Inputs

**`vars`**

1. Function argument

##### Type

```
toShellVars :: {
  [String] :: String | [String] | { [String] :: String };
} -> String
```

##### Examples

Example 88.

lib.strings.toShellVars

usage example

Located at lib/strings.nix:1351 in `<nixpkgs>`.

#### `lib.strings.escapeNixString`

Turn a string `s` into a Nix expression representing that string

##### Inputs

**`s`**

1. Function argument

##### Type

```
escapeNixString :: String -> String
```

##### Examples

Example 89.

lib.strings.escapeNixString

usage example

Located at lib/strings.nix:1378 in `<nixpkgs>`.

#### `lib.strings.escapeRegex`

Turn a string `s` into an exact regular expression

##### Inputs

**`s`**

1. Function argument

##### Type

```
escapeRegex :: String -> String
```

##### Examples

Example 90.

lib.strings.escapeRegex

usage example

Located at lib/strings.nix:1405 in `<nixpkgs>`.

#### `lib.strings.escapeNixIdentifier`

Quotes a string `s` if it can’t be used as an identifier directly.

##### Inputs

**`s`**

1. Function argument

##### Type

```
escapeNixIdentifier :: String -> String
```

##### Examples

Example 91.

lib.strings.escapeNixIdentifier

usage example

Located at lib/strings.nix:1434 in `<nixpkgs>`.

#### `lib.strings.escapeXML`

Escapes a string `s` such that it is safe to include verbatim in an XML document.

##### Inputs

**`s`**

1. Function argument

##### Type

```
escapeXML :: String -> String
```

##### Examples

Example 92.

lib.strings.escapeXML

usage example

Located at lib/strings.nix:1483 in `<nixpkgs>`.

#### `lib.strings.toLower`

Converts an ASCII string `s` to lower-case.

##### Inputs

**`s`**

The string to convert to lower-case.

##### Type

```
toLower :: String -> String
```

##### Examples

Example 93.

lib.strings.toLower

usage example

Located at lib/strings.nix:1517 in `<nixpkgs>`.

#### `lib.strings.toUpper`

Converts an ASCII string `s` to upper-case.

##### Inputs

**`s`**

The string to convert to upper-case.

##### Type

```
toUpper :: String -> String
```

##### Examples

Example 94.

lib.strings.toUpper

usage example

Located at lib/strings.nix:1544 in `<nixpkgs>`.

#### `lib.strings.toSentenceCase`

Converts the first character of a string `s` to upper-case.

##### Inputs

**`str`**

The string to convert to sentence case.

##### Type

```
toSentenceCase :: String -> String
```

##### Examples

Example 95.

lib.strings.toSentenceCase

usage example

Located at lib/strings.nix:1571 in `<nixpkgs>`.

#### `lib.strings.toCamelCase`

Converts a string to camelCase. Handles snake_case, PascalCase, kebab-case strings as well as strings delimited by spaces.

##### Inputs

**`string`**

The string to convert to camelCase

##### Type

```
toCamelCase :: String -> String
```

##### Examples

Example 96.

lib.strings.toCamelCase

usage example

Located at lib/strings.nix:1615 in `<nixpkgs>`.

#### `lib.strings.addContextFrom`

Appends string context from string like object `src` to `target`.

### Warning

This is an implementation detail of Nix and should be used carefully.

Strings in Nix carry an invisible `context` which is a list of strings representing store paths. If the string is later used in a derivation attribute, the derivation will properly populate the inputDrvs and inputSrcs.

##### Inputs

**`src`**

The string to take the context from. If the argument is not a string, it will be implicitly converted to a string.

**`target`**

The string to append the context to. If the argument is not a string, it will be implicitly converted to a string.

##### Type

```
addContextFrom :: String -> String -> String
```

##### Examples

Example 97.

lib.strings.addContextFrom

usage example

Located at lib/strings.nix:1690 in `<nixpkgs>`.

#### `lib.strings.splitString`

Cut a string with a separator and produces a list of strings which were separated by this separator.

##### Inputs

**`sep`**

1. Function argument

**`s`**

2. Function argument

##### Type

```
splitString :: String -> String -> [String]
```

##### Examples

Example 98.

lib.strings.splitString

usage example

Located at lib/strings.nix:1723 in `<nixpkgs>`.

#### `lib.strings.splitStringBy`

Splits a string into substrings based on a predicate that examines adjacent characters.

This function provides a flexible way to split strings by checking pairs of characters against a custom predicate function. Unlike simpler splitting functions, this allows for context-aware splitting based on character transitions and patterns.

##### Inputs

**`predicate`**

Function that takes two arguments (previous character and current character) and returns true when the string should be split at the current position. For the first character, previous will be “” (empty string).

**`keepSplit`**

Boolean that determines whether the splitting character should be kept as part of the result. If true, the character will be included at the beginning of the next substring; if false, it will be discarded.

**`str`**

The input string to split.

##### Return

A list of substrings from the original string, split according to the predicate.

##### Type

```
splitStringBy :: (String -> String -> Bool) -> Bool -> String -> [String]
```

##### Examples

Example 99.

lib.strings.splitStringBy

usage example

Located at lib/strings.nix:1793 in `<nixpkgs>`.

#### `lib.strings.removePrefix`

Returns a string without the specified prefix, if the prefix matches.

##### Inputs

**`prefix`**

Prefix to remove if it matches

**`str`**

Input string

##### Type

```
removePrefix :: String -> String -> String
```

##### Examples

Example 100.

lib.strings.removePrefix

usage example

Located at lib/strings.nix:1853 in `<nixpkgs>`.

#### `lib.strings.removeSuffix`

Returns a string without the specified suffix, if the suffix matches.

##### Inputs

**`suffix`**

Suffix to remove if it matches

**`str`**

Input string

##### Type

```
removeSuffix :: String -> String -> String
```

##### Examples

Example 101.

lib.strings.removeSuffix

usage example

Located at lib/strings.nix:1904 in `<nixpkgs>`.

#### `lib.strings.versionOlder`

Returns true if string `v1` denotes a version older than `v2`.

##### Inputs

**`v1`**

1. Function argument

**`v2`**

2. Function argument

##### Type

```
versionOlder :: String -> String -> Bool
```

##### Examples

Example 102.

lib.strings.versionOlder

usage example

Located at lib/strings.nix:1955 in `<nixpkgs>`.

#### `lib.strings.versionAtLeast`

Returns true if string `v1` denotes a version equal to or newer than `v2`.

##### Inputs

**`v1`**

1. Function argument

**`v2`**

2. Function argument

##### Type

```
versionAtLeast :: String -> String -> Bool
```

##### Examples

Example 103.

lib.strings.versionAtLeast

usage example

Located at lib/strings.nix:1989 in `<nixpkgs>`.

#### `lib.strings.getName`

This function takes an argument `x` that’s either a derivation or a derivation’s “name” attribute and extracts the name part from that argument.

##### Inputs

**`x`**

1. Function argument

##### Type

```
getName :: String | Derivation -> String
```

##### Examples

Example 104.

lib.strings.getName

usage example

Located at lib/strings.nix:2020 in `<nixpkgs>`.

#### `lib.strings.getVersion`

This function takes an argument `x` that’s either a derivation or a derivation’s “name” attribute and extracts the version part from that argument.

##### Inputs

**`x`**

1. Function argument

##### Type

```
getVersion :: String | Derivation -> String
```

##### Examples

Example 105.

lib.strings.getVersion

usage example

Located at lib/strings.nix:2055 in `<nixpkgs>`.

#### `lib.strings.nameFromURL`

Extract name and version from a URL as shown in the examples.

Separator `sep` is used to determine the end of the extension.

##### Inputs

**`url`**

1. Function argument

**`sep`**

2. Function argument

##### Type

```
nameFromURL :: String -> String
```

##### Examples

Example 106.

lib.strings.nameFromURL

usage example

Located at lib/strings.nix:2093 in `<nixpkgs>`.

#### `lib.strings.cmakeOptionType`

Create a `"-D<feature>:<type>=<value>"` string that can be passed to typical CMake invocations.

##### Inputs

**`type`**

The type of the feature to be set, as described in the CMake set documentation the possible values (case insensitive) are: BOOL FILEPATH PATH STRING INTERNAL LIST

**`feature`**

The feature to be set

**`feature`**

The feature to be set

**`value`**

The desired value

##### Type

```
cmakeOptionType :: String -> String -> String -> String
```

##### Examples

Example 107.

lib.strings.cmakeOptionType

usage example

Located at lib/strings.nix:2141 in `<nixpkgs>`.

#### `lib.strings.cmakeBool`

Create a `"-D<condition>={TRUE,FALSE}"` string that can be passed to typical CMake invocations.

##### Inputs

**`condition`**

The condition to be made true or false

**`flag`**

The controlling flag of the condition

##### Type

```
cmakeBool :: String -> Bool -> String
```

##### Examples

Example 108.

lib.strings.cmakeBool

usage example

Located at lib/strings.nix:2187 in `<nixpkgs>`.

#### `lib.strings.cmakeFeature`

Create a `"-D<feature>:STRING=<value>"` string that can be passed to typical CMake invocations. This is the most typical usage, so it deserves a special case.

##### Inputs

**`feature`**

The feature to be set

**`value`**

The desired value

##### Type

```
cmakeFeature :: String -> String -> String
```

##### Examples

Example 109.

lib.strings.cmakeFeature

usage example

Located at lib/strings.nix:2223 in `<nixpkgs>`.

#### `lib.strings.mesonOption`

Create a `"-D<feature>=<value>"` string that can be passed to typical Meson invocations.

##### Inputs

**`feature`**

The feature to be set

**`value`**

The desired value

##### Type

```
mesonOption :: String -> String -> String
```

##### Examples

Example 110.

lib.strings.mesonOption

usage example

Located at lib/strings.nix:2258 in `<nixpkgs>`.

#### `lib.strings.mesonBool`

Create a `"-D<condition>={true,false}"` string that can be passed to typical Meson invocations.

##### Inputs

**`condition`**

The condition to be made true or false

**`flag`**

The controlling flag of the condition

##### Type

```
mesonBool :: String -> Bool -> String
```

##### Examples

Example 111.

lib.strings.mesonBool

usage example

Located at lib/strings.nix:2295 in `<nixpkgs>`.

#### `lib.strings.mesonEnable`

Create a `"-D<feature>={enabled,disabled}"` string that can be passed to typical Meson invocations.

##### Inputs

**`feature`**

The feature to be enabled or disabled

**`flag`**

The controlling flag

##### Type

```
mesonEnable :: String -> Bool -> String
```

##### Examples

Example 112.

lib.strings.mesonEnable

usage example

Located at lib/strings.nix:2332 in `<nixpkgs>`.

#### `lib.strings.enableFeature`

Create an `"--{enable,disable}-<feature>"` string that can be passed to standard GNU Autoconf scripts.

##### Inputs

**`flag`**

1. Function argument

**`feature`**

2. Function argument

##### Type

```
enableFeature :: Bool -> String -> String
```

##### Examples

Example 113.

lib.strings.enableFeature

usage example

Located at lib/strings.nix:2369 in `<nixpkgs>`.

#### `lib.strings.enableFeatureAs`

Create an `"--{enable-<feature>=<value>,disable-<feature>}"` string that can be passed to standard GNU Autoconf scripts.

##### Inputs

**`flag`**

1. Function argument

**`feature`**

2. Function argument

**`value`**

3. Function argument

##### Type

```
enableFeatureAs :: Bool -> String -> String -> String
```

##### Examples

Example 114.

lib.strings.enableFeatureAs

usage example

Located at lib/strings.nix:2409 in `<nixpkgs>`.

#### `lib.strings.withFeature`

Create an `"--{with,without}-<feature>"` string that can be passed to standard GNU Autoconf scripts.

##### Inputs

**`flag`**

1. Function argument

**`feature`**

2. Function argument

##### Type

```
withFeature :: Bool -> String -> String
```

##### Examples

Example 115.

lib.strings.withFeature

usage example

Located at lib/strings.nix:2444 in `<nixpkgs>`.

#### `lib.strings.withFeatureAs`

Create an `"--{with-<feature>=<value>,without-<feature>}"` string that can be passed to standard GNU Autoconf scripts.

##### Inputs

**`flag`**

1. Function argument

**`feature`**

2. Function argument

**`value`**

3. Function argument

##### Type

```
withFeatureAs :: Bool -> String -> String -> String
```

##### Examples

Example 116.

lib.strings.withFeatureAs

usage example

Located at lib/strings.nix:2483 in `<nixpkgs>`.

#### `lib.strings.fixedWidthString`

Create a fixed width string with additional prefix to match required width.

This function will fail if the input string is longer than the requested length.

##### Inputs

**`width`**

1. Function argument

**`filler`**

2. Function argument

**`str`**

3. Function argument

##### Type

```
fixedWidthString :: Int -> String -> String -> String
```

##### Examples

Example 117.

lib.strings.fixedWidthString

usage example

Located at lib/strings.nix:2522 in `<nixpkgs>`.

#### `lib.strings.fixedWidthNumber`

Format a number adding leading zeroes up to fixed width.

##### Inputs

**`width`**

1. Function argument

**`n`**

2. Function argument

##### Type

```
fixedWidthNumber :: Int -> Int -> String
```

##### Examples

Example 118.

lib.strings.fixedWidthNumber

usage example

Located at lib/strings.nix:2560 in `<nixpkgs>`.

#### `lib.strings.floatToString`

Convert a float to a string, but emit a warning when precision is lost during the conversion

##### Inputs

**`float`**

1. Function argument

##### Type

```
floatToString :: Float -> String
```

##### Examples

Example 119.

lib.strings.floatToString

usage example

Located at lib/strings.nix:2591 in `<nixpkgs>`.

#### `lib.strings.isConvertibleWithToString`

Check whether a list or other value `x` can be passed to `toString`.

Many types of value are coercible to string this way, including `int`, `float`, `null`, `bool`, `list` of similarly coercible values.

##### Inputs

**`val`**

1. Function argument

##### Type

```
isConvertibleWithToString :: Any -> Bool
```

Located at lib/strings.nix:2616 in `<nixpkgs>`.

#### `lib.strings.isStringLike`

Check whether a value can be coerced to a string. The value must be a string, path, or attribute set.

String-like values can be used without explicit conversion in string interpolations and in most functions that expect a string.

##### Inputs

**`x`**

1. Function argument

##### Type

```
isStringLike :: Any -> Bool
```

Located at lib/strings.nix:2645 in `<nixpkgs>`.

#### `lib.strings.isStorePath`

Check whether a value `x` is a store path.

##### Inputs

**`x`**

1. Function argument

##### Type

```
isStorePath :: Any -> Bool
```

##### Examples

Example 120.

lib.strings.isStorePath

usage example

Located at lib/strings.nix:2678 in `<nixpkgs>`.

#### `lib.strings.toInt`

Parse a string as an int. Does not support parsing of integers with preceding zero due to ambiguity between zero-padded and octal numbers. See `toIntBase10`.

##### Inputs

**`str`**

A string to be interpreted as an int.

##### Type

```
toInt :: String -> Int
```

##### Examples

Example 121.

lib.strings.toInt

usage example

Located at lib/strings.nix:2735 in `<nixpkgs>`.

#### `lib.strings.toIntBase10`

Parse a string as a base 10 int. This supports parsing of zero-padded integers.

##### Inputs

**`str`**

A string to be interpreted as an int.

##### Type

```
toIntBase10 :: String -> Int
```

##### Examples

Example 122.

lib.strings.toIntBase10

usage example

Located at lib/strings.nix:2805 in `<nixpkgs>`.

#### `lib.strings.fileContents`

Read the contents of a file removing the trailing \n

##### Inputs

**`file`**

1. Function argument

##### Type

```
fileContents :: Path -> String
```

##### Examples

Example 123.

lib.strings.fileContents

usage example

Located at lib/strings.nix:2866 in `<nixpkgs>`.

#### `lib.strings.sanitizeDerivationName`

Creates a valid derivation name from a potentially invalid one.

##### Inputs

**`string`**

1. Function argument

##### Type

```
sanitizeDerivationName :: String -> String
```

##### Examples

Example 124.

lib.strings.sanitizeDerivationName

usage example

Located at lib/strings.nix:2897 in `<nixpkgs>`.

#### `lib.strings.levenshtein`

Computes the Levenshtein distance between two strings `a` and `b`.

Complexity O(n*m) where n and m are the lengths of the strings. Algorithm adjusted from this stackoverflow comment

##### Inputs

**`a`**

1. Function argument

**`b`**

2. Function argument

##### Type

```
levenshtein :: String -> String -> Int
```

##### Examples

Example 125.

lib.strings.levenshtein

usage example

Located at lib/strings.nix:2959 in `<nixpkgs>`.

#### `lib.strings.commonPrefixLength`

Returns the length of the prefix that appears in both strings `a` and `b`.

##### Inputs

**`a`**

1. Function argument

**`b`**

2. Function argument

##### Type

```
commonPrefixLength :: String -> String -> Int
```

Located at lib/strings.nix:2996 in `<nixpkgs>`.

#### `lib.strings.commonSuffixLength`

Returns the length of the suffix common to both strings `a` and `b`.

##### Inputs

**`a`**

1. Function argument

**`b`**

2. Function argument

##### Type

```
commonSuffixLength :: String -> String -> Int
```

Located at lib/strings.nix:3028 in `<nixpkgs>`.

#### `lib.strings.levenshteinAtMost`

Returns whether the levenshtein distance between two strings `a` and `b` is at most some value `k`.

Complexity is O(min(n,m)) for k <= 2 and O(n*m) otherwise

##### Inputs

**`k`**

Distance threshold

**`a`**

String `a`

**`b`**

String `b`

##### Type

```
levenshteinAtMost :: Int -> String -> String -> Bool
```

##### Examples

Example 126.

lib.strings.levenshteinAtMost

usage example

Located at lib/strings.nix:3084 in `<nixpkgs>`.

### lib.versions: version string functions

#### `lib.versions.splitVersion`

Break a version string into its component parts.

##### Type

```
splitVersion :: String -> [String]
```

##### Examples

Example 127.

splitVersion

usage example

Located at lib/versions.nix:28 in `<nixpkgs>`.

#### `lib.versions.major`

Get the major version string from a string.

##### Inputs

**`v`**

1. Function argument

##### Type

```
major :: String -> String
```

##### Examples

Example 128.

major

usage example

Located at lib/versions.nix:56 in `<nixpkgs>`.

#### `lib.versions.minor`

Get the minor version string from a string.

##### Inputs

**`v`**

1. Function argument

##### Type

```
minor :: String -> String
```

##### Examples

Example 129.

minor

usage example

Located at lib/versions.nix:84 in `<nixpkgs>`.

#### `lib.versions.patch`

Get the patch version string from a string.

##### Inputs

**`v`**

1. Function argument

##### Type

```
patch :: String -> String
```

##### Examples

Example 130.

patch

usage example

Located at lib/versions.nix:112 in `<nixpkgs>`.

#### `lib.versions.majorMinor`

Get string of the first two parts (major and minor) of a version string.

##### Inputs

**`v`**

1. Function argument

##### Type

```
majorMinor :: String -> String
```

##### Examples

Example 131.

majorMinor

usage example

Located at lib/versions.nix:141 in `<nixpkgs>`.

#### `lib.versions.pad`

Pad a version string with zeros to match the given number of components.

##### Inputs

**`n`**

1. Function argument

**`version`**

2. Function argument

##### Type

```
pad :: Int -> String -> String
```

##### Examples

Example 132.

pad

usage example

Located at lib/versions.nix:177 in `<nixpkgs>`.

### lib.trivial: miscellaneous functions

#### `lib.trivial.id`

The identity function For when you need a function that does “nothing”.

##### Inputs

**`x`**

The value to return

##### Type

```
id :: a -> a
```

Located at lib/trivial.nix:63 in `<nixpkgs>`.

#### `lib.trivial.const`

The constant function

Ignores the second argument. If called with only one argument, constructs a function that always returns a static value.

##### Inputs

**`x`**

Value to return

**`y`**

Value to ignore

##### Type

```
const :: a -> b -> a
```

##### Examples

Example 133.

lib.trivial.const

usage example

Located at lib/trivial.nix:98 in `<nixpkgs>`.

#### `lib.trivial.pipe`

Pipes a value through a list of functions, left to right.

##### Inputs

**`value`**

Value to start piping.

**`fns`**

List of functions to apply sequentially.

##### Type

```
pipe :: a -> [(a -> b) (b -> c) ... (x -> y) (y -> z)] -> z
```

##### Examples

Example 134.

lib.trivial.pipe

usage example

Located at lib/trivial.nix:152 in `<nixpkgs>`.

#### `lib.trivial.concat`

Concatenate two lists

##### Inputs

**`x`**

1. Function argument

**`y`**

2. Function argument

##### Type

```
concat :: [a] -> [a] -> [a]
```

##### Examples

Example 135.

lib.trivial.concat

usage example

Located at lib/trivial.nix:191 in `<nixpkgs>`.

#### `lib.trivial."or"` {#function-library-lib.trivial.“or”}

boolean “or”

##### Inputs

**`x`**

1. Function argument

**`y`**

2. Function argument

##### Type

```
or :: Bool -> Bool -> Bool
```

#### `lib.trivial.and`

boolean “and”

##### Inputs

**`x`**

1. Function argument

**`y`**

2. Function argument

##### Type

```
and :: Bool -> Bool -> Bool
```

Located at lib/trivial.nix:233 in `<nixpkgs>`.

#### `lib.trivial.xor`

boolean “exclusive or”

##### Inputs

**`x`**

1. Function argument

**`y`**

2. Function argument

##### Type

```
xor :: bool -> bool -> bool
```

Located at lib/trivial.nix:256 in `<nixpkgs>`.

#### `lib.trivial.bitNot`

bitwise “not”

##### Type

```
bitNot :: Number -> Number
```

Located at lib/trivial.nix:267 in `<nixpkgs>`.

#### `lib.trivial.boolToString`

Convert a boolean to a string.

This function uses the strings “true” and “false” to represent boolean values. Calling `toString` on a bool instead returns “1” and “” (sic!).

##### Inputs

**`b`**

1. Function argument

##### Type

```
boolToString :: Bool -> String
```

Located at lib/trivial.nix:288 in `<nixpkgs>`.

#### `lib.trivial.boolToYesNo`

Converts a boolean to a string.

This function uses the strings “yes” and “no” to represent boolean values.

##### Inputs

**`b`**

The boolean to convert

##### Type

```
boolToYesNo :: Bool -> String
```

Located at lib/trivial.nix:308 in `<nixpkgs>`.

#### `lib.trivial.mergeAttrs`

Merge two attribute sets shallowly, right side trumps left

##### Inputs

**`x`**

Left attribute set

**`y`**

Right attribute set (higher precedence for equal keys)

##### Type

```
mergeAttrs :: AttrSet -> AttrSet -> AttrSet
```

##### Examples

Example 136.

lib.trivial.mergeAttrs

usage example

Located at lib/trivial.nix:340 in `<nixpkgs>`.

#### `lib.trivial.flip`

Flip the order of the arguments of a binary function.

##### Inputs

**`f`**

1. Function argument

**`a`**

2. Function argument

**`b`**

3. Function argument

##### Type

```
flip :: (a -> b -> c) -> (b -> a -> c)
```

##### Examples

Example 137.

lib.trivial.flip

usage example

Located at lib/trivial.nix:376 in `<nixpkgs>`.

#### `lib.trivial.defaultTo`

Returns `maybeValue` if not null, otherwise return `default`.

##### Inputs

**`default`**

1. Function argument

**`maybeValue`**

2. Function argument

##### Type

```
defaultTo :: a -> (b | Null) -> (b | a)
```

##### Examples

Example 138.

lib.trivial.defaultTo

usage example

Located at lib/trivial.nix:414 in `<nixpkgs>`.

#### `lib.trivial.mapNullable`

Apply function if the supplied argument is non-null.

##### Inputs

**`f`**

Function to call

**`a`**

Argument to check for null before passing it to `f`

##### Type

```
mapNullable :: (a -> b) -> (a | Null) -> (b | Null)
```

##### Examples

Example 139.

lib.trivial.mapNullable

usage example

Located at lib/trivial.nix:448 in `<nixpkgs>`.

#### `lib.trivial.version`

Returns the current full nixpkgs version number.

Located at lib/trivial.nix:455 in `<nixpkgs>`.

#### `lib.trivial.release`

Returns the current nixpkgs release number as string.

Located at lib/trivial.nix:460 in `<nixpkgs>`.

#### `lib.trivial.oldestSupportedRelease`

The latest release that is supported, at the time of release branch-off, if applicable.

Ideally, out-of-tree modules should be able to evaluate cleanly with all supported Nixpkgs versions (master, release and old release until EOL). So if possible, deprecation warnings should take effect only when all out-of-tree expressions/libs/modules can upgrade to the new way without losing support for supported Nixpkgs versions.

This release number allows deprecation warnings to be implemented such that they take effect as soon as the oldest release reaches end of life.

Located at lib/trivial.nix:475 in `<nixpkgs>`.

#### `lib.trivial.isInOldestRelease`

Whether a feature is supported in all supported releases (at the time of release branch-off, if applicable). See `oldestSupportedRelease`.

##### Inputs

**`release`**

Release number of feature introduction as an integer, e.g. 2111 for 21.11. Set it to the upcoming release, matching the nixpkgs/.version file.

Located at lib/trivial.nix:490 in `<nixpkgs>`.

#### `lib.trivial.oldestSupportedReleaseIsAtLeast`

Alias for `isInOldestRelease` introduced in 24.11. Use `isInOldestRelease` in expressions outside of Nixpkgs for greater compatibility.

Located at lib/trivial.nix:499 in `<nixpkgs>`.

#### `lib.trivial.codeName`

Returns the current nixpkgs release code name.

On each release the first letter is bumped and a new animal is chosen starting with that new letter.

Located at lib/trivial.nix:507 in `<nixpkgs>`.

#### `lib.trivial.versionSuffix`

Returns the current nixpkgs version suffix as string.

Located at lib/trivial.nix:512 in `<nixpkgs>`.

#### `lib.trivial.revisionWithDefault`

Attempts to return the the current revision of nixpkgs and returns the supplied default value otherwise.

##### Inputs

**`default`**

Default value to return if revision can not be determined

##### Type

```
revisionWithDefault :: String -> String
```

Located at lib/trivial.nix:534 in `<nixpkgs>`.

#### `lib.trivial.inNixShell`

Determine whether the function is being called from inside a Nix shell.

##### Type

```
inNixShell :: Bool
```

Located at lib/trivial.nix:559 in `<nixpkgs>`.

#### `lib.trivial.inPureEvalMode`

Determine whether the function is being called from inside pure-eval mode by seeing whether `builtins` contains `currentSystem`. If not, we must be in pure-eval mode.

##### Type

```
inPureEvalMode :: Bool
```

Located at lib/trivial.nix:572 in `<nixpkgs>`.

#### `lib.trivial.min`

Returns minimum of two numbers.

##### Inputs

**`x`**

1. Function argument

**`y`**

2. Function argument

##### Type

```
min :: Number -> Number -> Number
```

Located at lib/trivial.nix:595 in `<nixpkgs>`.

#### `lib.trivial.max`

Returns maximum of two numbers.

##### Inputs

**`x`**

1. Function argument

**`y`**

2. Function argument

##### Type

```
max :: Number -> Number -> Number
```

Located at lib/trivial.nix:616 in `<nixpkgs>`.

#### `lib.trivial.mod`

Integer modulus

##### Inputs

**`base`**

1. Function argument

**`int`**

2. Function argument

##### Type

```
mod :: Int -> Int -> Int
```

##### Examples

Example 140.

lib.trivial.mod

usage example

Located at lib/trivial.nix:650 in `<nixpkgs>`.

#### `lib.trivial.compare`

C-style comparisons

a < b, compare a b => -1 a == b, compare a b => 0 a > b, compare a b => 1

##### Inputs

**`a`**

1. Function argument

**`b`**

2. Function argument

##### Type

```
compare :: a -> a -> Int
```

Located at lib/trivial.nix:677 in `<nixpkgs>`.

#### `lib.trivial.splitByAndCompare`

Split type into two subtypes by predicate `p`, take all elements of the first subtype to be less than all the elements of the second subtype, compare elements of a single subtype with `yes` and `no` respectively.

##### Inputs

**`p`**

Predicate

**`yes`**

Comparison function if predicate holds for both values

**`no`**

Comparison function if predicate holds for neither value

**`a`**

First value to compare

**`b`**

Second value to compare

##### Type

```
splitByAndCompare :: (a -> Bool) -> (a -> a -> Int) -> (a -> a -> Int) -> (a -> a -> Int)
```

##### Examples

Example 141.

lib.trivial.splitByAndCompare

usage example

Located at lib/trivial.nix:738 in `<nixpkgs>`.
