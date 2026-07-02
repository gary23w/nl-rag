---
title: "Nixpkgs Reference Manual (part 4/6)"
source: https://nixos.org/manual/nixpkgs/stable/
domain: nix-language
license: CC-BY-SA-4.0
tags: nix language, nix lang, nixos, nixpkgs, nix expression
fetched: 2026-07-02
part: 4/6
---

#### `lib.trivial.importJSON`

Reads a JSON file.

##### Examples

Example 142.

lib.trivial.importJSON

usage example

##### Inputs

**`path`**

1. Function argument

##### Type

```
importJSON :: Path -> Any
```

Located at lib/trivial.nix:794 in `<nixpkgs>`.

#### `lib.trivial.importTOML`

Reads a TOML file.

##### Examples

Example 143.

lib.trivial.importTOML

usage example

##### Inputs

**`path`**

1. Function argument

##### Type

```
importTOML :: Path -> Any
```

Located at lib/trivial.nix:841 in `<nixpkgs>`.

#### `lib.trivial.warn`

`warn` *`message`* *`value`*

Print a warning before returning the second argument.

See `builtins.warn` (Nix >= 2.23). On older versions, the Nix 2.23 behavior is emulated with `builtins.trace`, including the `NIX_ABORT_ON_WARN` behavior, but not the `nix.conf` setting or command line option.

##### Inputs

***`message`* (String)**

Warning message to print before evaluating *`value`*.

***`value`* (any value)**

Value to return as-is.

##### Type

```
warn :: String -> a -> a
```

Located at lib/trivial.nix:867 in `<nixpkgs>`.

#### `lib.trivial.warnIf`

`warnIf` *`condition`* *`message`* *`value`*

Like `warn`, but only warn when the first argument is `true`.

##### Inputs

***`condition`* (Boolean)**

`true` to trigger the warning before continuing with *`value`*.

***`message`* (String)**

Warning message to print before evaluating

***`value`* (any value)**

Value to return as-is.

##### Type

```
warnIf :: Bool -> String -> a -> a
```

Located at lib/trivial.nix:914 in `<nixpkgs>`.

#### `lib.trivial.warnIfNot`

`warnIfNot` *`condition`* *`message`* *`value`*

Like `warnIf`, but negated: warn if the first argument is `false`.

##### Inputs

***`condition`***

`false` to trigger the warning before continuing with `val`.

***`message`***

Warning message to print before evaluating *`value`*.

***`value`***

Value to return as-is.

##### Type

```
warnIfNot :: Bool -> String -> a -> a
```

Located at lib/trivial.nix:941 in `<nixpkgs>`.

#### `lib.trivial.throwIfNot`

Like the `assert b; e` expression, but with a custom error message and without the semicolon.

If true, return the identity function, `r: r`.

If false, throw the error message.

Calls can be juxtaposed using function application, as `(r: r) a = a`, so `(r: r) (r: r) a = a`, and so forth.

##### Inputs

**`cond`**

1. Function argument

**`msg`**

2. Function argument

##### Type

```
throwIfNot :: Bool -> String -> a -> (a | Never)
```

##### Examples

Example 144.

lib.trivial.throwIfNot

usage example

Located at lib/trivial.nix:982 in `<nixpkgs>`.

#### `lib.trivial.throwIf`

Like `throwIfNot`, but negated (throw if the first argument is `true`).

##### Inputs

**`cond`**

1. Function argument

**`msg`**

2. Function argument

##### Type

```
throwIf :: Bool -> String -> a -> (a | Never)
```

Located at lib/trivial.nix:1003 in `<nixpkgs>`.

#### `lib.trivial.checkListOfEnum`

Check if the elements in a list are valid values from a enum, returning the identity function, or throwing an error message otherwise.

##### Inputs

**`msg`**

1. Function argument

**`valid`**

2. Function argument

**`given`**

3. Function argument

##### Type

```
checkListOfEnum :: String -> [a] -> [a] -> ((b -> b) | Never)
```

##### Examples

Example 145.

lib.trivial.checkListOfEnum

usage example

Located at lib/trivial.nix:1041 in `<nixpkgs>`.

#### `lib.trivial.setFunctionArgs`

Add metadata about expected function arguments to a function. The metadata should match the format given by builtins.functionArgs, i.e. a set from expected argument to a bool representing whether that argument has a default or not.

This function is necessary because you can’t dynamically create a function of the `{ a, b ? foo, ... }:` format, but some facilities like `callPackage` expect to be able to query expected arguments.

##### Inputs

**`f`**

1. Function argument

**`args`**

2. Function argument

##### Type

```
setFunctionArgs : (a -> b) -> { [String] :: Bool } -> (a -> b)
```

Located at lib/trivial.nix:1081 in `<nixpkgs>`.

#### `lib.trivial.functionArgs`

Extract the expected function arguments from a function. This works both with nix-native `{ a, b ? foo, ... }:` style functions and functions with args set with `setFunctionArgs`. It has the same return type and semantics as `builtins.functionArgs`.

##### Inputs

**`f`**

1. Function argument

##### Type

```
functionArgs : (a -> b) -> { [String] :: Bool }
```

Located at lib/trivial.nix:1105 in `<nixpkgs>`.

#### `lib.trivial.isFunction`

Check whether something is a function or something annotated with function args.

##### Inputs

**`f`**

1. Function argument

##### Type

```
isFunction : Any -> Bool
```

Located at lib/trivial.nix:1127 in `<nixpkgs>`.

#### `lib.trivial.mirrorFunctionArgs`

`mirrorFunctionArgs f g` creates a new function `g'` with the same behavior as `g` (`g' x == g x`) but its function arguments mirroring `f` (`lib.functionArgs g' == lib.functionArgs f`).

##### Inputs

**`f`**

Function to provide the argument metadata

**`g`**

Function to set the argument metadata to

##### Type

```
mirrorFunctionArgs :: (a -> b) -> (a -> c) -> (a -> c)
```

##### Examples

Example 146.

lib.trivial.mirrorFunctionArgs

usage example

Located at lib/trivial.nix:1177 in `<nixpkgs>`.

#### `lib.trivial.toFunction`

Turns any non-callable values into constant functions. Returns callable values as is.

##### Inputs

**`v`**

Any value

##### Examples

Example 147.

lib.trivial.toFunction

usage example

Located at lib/trivial.nix:1211 in `<nixpkgs>`.

#### `lib.trivial.fromHexString`

Convert a hexadecimal string to it’s integer representation.

##### Type

```
fromHexString :: String -> Int
```

##### Examples

Example 148.

lib.trivial.fromHexString

usage examples

Located at lib/trivial.nix:1234 in `<nixpkgs>`.

#### `lib.trivial.toHexString`

Convert the given positive integer to a string of its hexadecimal representation.

##### Type

```
toHexString :: Int -> String
```

##### Examples

Example 149.

lib.trivial.toHexString

usage example

Located at lib/trivial.nix:1274 in `<nixpkgs>`.

#### `lib.trivial.toBaseDigits`

`toBaseDigits base i` converts the positive integer `i` to a list of its digits in the given base.

##### Inputs

**`base`**

1. Function argument

**`i`**

2. Function argument

##### Type

```
toBaseDigits :: Int -> Int -> [Int]
```

##### Examples

Example 150.

lib.trivial.toBaseDigits

Located at lib/trivial.nix:1321 in `<nixpkgs>`.

### lib.fixedPoints: explicit recursion functions

#### `lib.fixedPoints.fix`

`fix f` computes the fixed point of the given function `f`. In other words, the return value is `x` in `x = f x`.

`f` must be a lazy function. This means that `x` must be a value that can be partially evaluated, such as an attribute set, a list, or a function. This way, `f` can use one part of `x` to compute another part.

**Relation to syntactic recursion**

This section explains `fix` by refactoring from syntactic recursion to a call of `fix` instead.

For context, Nix lets you define attributes in terms of other attributes syntactically using the `rec { }` syntax.

```
nix-repl> rec {
  foo = "foo";
  bar = "bar";
  foobar = foo + bar;
}
{ bar = "bar"; foo = "foo"; foobar = "foobar"; }
```

This is convenient when constructing a value to pass to a function for example, but an equivalent effect can be achieved with the `let` binding syntax:

```
nix-repl> let self = {
  foo = "foo";
  bar = "bar";
  foobar = self.foo + self.bar;
}; in self
{ bar = "bar"; foo = "foo"; foobar = "foobar"; }
```

But in general you can get more reuse out of `let` bindings by refactoring them to a function.

```
nix-repl> f = self: {
  foo = "foo";
  bar = "bar";
  foobar = self.foo + self.bar;
}
```

This is where `fix` comes in, it contains the syntactic recursion that’s not in `f` anymore.

```
nix-repl> fix = f:
  let self = f self; in self;
```

By applying `fix` we get the final result.

```
nix-repl> fix f
{ bar = "bar"; foo = "foo"; foobar = "foobar"; }
```

Such a refactored `f` using `fix` is not useful by itself. See `extends` for an example use case. There `self` is also often called `final`.

##### Inputs

**`f`**

1. Function argument

##### Type

```
fix :: (a -> a) -> a
```

##### Examples

Example 151.

lib.fixedPoints.fix

usage example

Located at lib/fixed-points.nix:92 in `<nixpkgs>`.

#### `lib.fixedPoints.fix'`

A variant of `fix` that records the original recursive attribute set in the result, in an attribute named `__unfix__`.

This is useful in combination with the `extends` function to implement deep overriding.

##### Inputs

**`f`**

1. Function argument

##### Type

```
fix' :: (a -> a) -> a
```

Located at lib/fixed-points.nix:118 in `<nixpkgs>`.

#### `lib.fixedPoints.converge`

Returns the fixpoint that `f` converges to when called iteratively, starting with the input `x`.

```
nix-repl> converge (x: x / 2) 16
0
```

##### Inputs

**`f`**

1. Function argument

**`x`**

2. Function argument

##### Type

```
converge :: (a -> a) -> a -> a
```

Located at lib/fixed-points.nix:152 in `<nixpkgs>`.

#### `lib.fixedPoints.extends`

Extend a function using an overlay.

Overlays allow modifying and extending fixed-point functions, specifically ones returning attribute sets. A fixed-point function is a function which is intended to be evaluated by passing the result of itself as the argument. This is possible due to Nix’s lazy evaluation.

A fixed-point function returning an attribute set has the form

```
final: {
  # attributes
}
```

where `final` refers to the lazily evaluated attribute set returned by the fixed-point function.

An overlay to such a fixed-point function has the form

```
final: prev: {
  # attributes
}
```

where `prev` refers to the result of the original function to `final`, and `final` is the result of the composition of the overlay and the original function.

Applying an overlay is done with `extends`:

```
let
  f = final: {
    # attributes
  };
  overlay = final: prev: {
    # attributes
  };
in extends overlay f;
```

To get the value of `final`, use `lib.fix`:

```
let
  f = final: {
    # attributes
  };
  overlay = final: prev: {
    # attributes
  };
  g = extends overlay f;
in fix g
```

### Note

The argument to the given fixed-point function after applying an overlay will *not* refer to its own return value, but rather to the value after evaluating the overlay function.

The given fixed-point function is called with a separate argument than if it was evaluated with `lib.fix`.

Example 152. Extend a fixed-point function with an overlay

##### Inputs

**`overlay`**

The overlay to apply to the fixed-point function

**`f`**

The fixed-point function

##### Type

```
extends :: (AttrSet -> AttrSet -> AttrSet) # The overlay to apply to the fixed-point function
        -> (AttrSet -> AttrSet) # A fixed-point function
        -> (AttrSet -> AttrSet) # The resulting fixed-point function
```

##### Examples

Example 153.

lib.fixedPoints.extends

usage example

Located at lib/fixed-points.nix:325 in `<nixpkgs>`.

#### `lib.fixedPoints.composeExtensions`

Compose two overlay functions and return a single overlay function that combines them. For more details see: `composeManyExtensions`.

Located at lib/fixed-points.nix:340 in `<nixpkgs>`.

#### `lib.fixedPoints.composeManyExtensions`

Composes a list of `overlays` and returns a single overlay function that combines them.

### Note

The result is produced by using the update operator `//`. This means nested values of previous overlays are not merged recursively. In other words, previously defined attributes are replaced, ignoring the previous value, unless referenced by the overlay; for example `final: prev: { foo = final.foo + 1; }`.

##### Inputs

**`extensions`**

A list of overlay functions

### Note

The order of the overlays in the list is important.

Each overlay function takes two arguments, by convention `final` and `prev`, and returns an attribute set.

- `final` is the result of the fixed-point function, with all overlays applied.
- `prev` is the result of the previous overlay function(s).

##### Type

```
# Pseudo code
let
  #               final      prev
  #                 ↓          ↓
  OverlayFn = { ... } -> { ... } -> { ... };
in
composeManyExtensions :: [OverlayFn] -> OverlayFn
```

##### Examples

Example 154.

lib.fixedPoints.composeManyExtensions

usage example

Located at lib/fixed-points.nix:412 in `<nixpkgs>`.

#### `lib.fixedPoints.makeExtensible`

Create an overridable, recursive attribute set. For example:

```
nix-repl> obj = makeExtensible (final: { })

nix-repl> obj
{ __unfix__ = «lambda»; extend = «lambda»; }

nix-repl> obj = obj.extend (final: prev: { foo = "foo"; })

nix-repl> obj
{ __unfix__ = «lambda»; extend = «lambda»; foo = "foo"; }

nix-repl> obj = obj.extend (final: prev: { foo = prev.foo + " + "; bar = "bar"; foobar = final.foo + final.bar; })

nix-repl> obj
{ __unfix__ = «lambda»; bar = "bar"; extend = «lambda»; foo = "foo + "; foobar = "foo + bar"; }
```

Located at lib/fixed-points.nix:434 in `<nixpkgs>`.

#### `lib.fixedPoints.makeExtensibleWithCustomName`

Same as `makeExtensible` but the name of the extending attribute is customized.

##### Inputs

**`extenderName`**

1. Function argument

**`rattrs`**

2. Function argument

Located at lib/fixed-points.nix:450 in `<nixpkgs>`.

#### `lib.fixedPoints.toExtension`

Convert to an extending function (overlay).

`toExtension` is the `toFunction` for extending functions (a.k.a. extensions or overlays). It converts a non-function or a single-argument function to an extending function, while returning a two-argument function as-is.

That is, it takes a value of the shape `x`, `prev: x`, or `final: prev: x`, and returns `final: prev: x`, assuming `x` is not a function.

This function takes care of the input to `stdenv.mkDerivation`’s `overrideAttrs` function. It bridges the gap between `<pkg>.overrideAttrs` before and after the overlay-style support.

##### Inputs

**`f`**

The function or value to convert to an extending function.

##### Type

```
toExtension :: b' -> Any -> Any -> b'
or
toExtension :: (a -> b') -> Any -> a -> b'
or
toExtension :: (a -> a -> b) -> a -> a -> b
where b' = ! Callable

Set a = b = b' = AttrSet & ! Callable to make toExtension return an extending function.
```

##### Examples

Example 155.

lib.fixedPoints.toExtension

usage example

Located at lib/fixed-points.nix:512 in `<nixpkgs>`.

### lib.lists: list manipulation functions

General list operations.

#### `lib.lists.singleton`

Create a list consisting of a single element. `singleton x` is sometimes more convenient with respect to indentation than `[x]` when x spans multiple lines.

##### Inputs

**`x`**

1. Function argument

##### Type

```
singleton :: a -> [a]
```

##### Examples

Example 156.

lib.lists.singleton

usage example

Located at lib/lists.nix:59 in `<nixpkgs>`.

#### `lib.lists.forEach`

Apply the function to each element in the list. Same as `map`, but arguments flipped.

##### Inputs

**`xs`**

1. Function argument

**`f`**

2. Function argument

##### Type

```
forEach :: [a] -> (a -> b) -> [b]
```

##### Examples

Example 157.

lib.lists.forEach

usage example

Located at lib/lists.nix:94 in `<nixpkgs>`.

#### `lib.lists.foldr`

“right fold” a binary function `op` between successive elements of `list` with `nul` as the starting value, i.e., `foldr op nul [x_1 x_2 ... x_n] == op x_1 (op x_2 ... (op x_n nul))`.

##### Inputs

**`op`**

1. Function argument

**`nul`**

2. Function argument

**`list`**

3. Function argument

##### Type

```
foldr :: (a -> b -> b) -> b -> [a] -> b
```

##### Examples

Example 158.

lib.lists.foldr

usage example

Located at lib/lists.nix:137 in `<nixpkgs>`.

#### `lib.lists.fold`

`fold` is an alias of `foldr` for historic reasons.

### Warning

This function will be removed in 26.05.

Located at lib/lists.nix:152 in `<nixpkgs>`.

#### `lib.lists.foldl`

“left fold”, like `foldr`, but from the left:

`foldl op nul [x_1 x_2 ... x_n] == op (... (op (op nul x_1) x_2) ... x_n)`.

##### Inputs

**`op`**

1. Function argument

**`nul`**

2. Function argument

**`list`**

3. Function argument

##### Type

```
foldl :: (b -> a -> b) -> b -> [a] -> b
```

##### Examples

Example 159.

lib.lists.foldl

usage example

Located at lib/lists.nix:195 in `<nixpkgs>`.

#### `lib.lists.foldl'`

Reduce a list by applying a binary operator from left to right, starting with an initial accumulator.

Before each application of the operator, the accumulator value is evaluated. This behavior makes this function stricter than `foldl`.

Unlike `builtins.foldl'`, the initial accumulator argument is evaluated before the first iteration.

A call like

```
foldl' op acc₀ [ x₀ x₁ x₂ ... xₙ₋₁ xₙ ]
```

is (denotationally) equivalent to the following, but with the added benefit that `foldl'` itself will never overflow the stack.

```
let
  acc₁   = builtins.seq acc₀   (op acc₀   x₀  );
  acc₂   = builtins.seq acc₁   (op acc₁   x₁  );
  acc₃   = builtins.seq acc₂   (op acc₂   x₂  );
  ...
  accₙ   = builtins.seq accₙ₋₁ (op accₙ₋₁ xₙ₋₁);
  accₙ₊₁ = builtins.seq accₙ   (op accₙ   xₙ  );
in
accₙ₊₁

# Or ignoring builtins.seq
op (op (... (op (op (op acc₀ x₀) x₁) x₂) ...) xₙ₋₁) xₙ
```

##### Inputs

**`op`**

The binary operation to run, where the two arguments are:

1. `acc`: The current accumulator value: Either the initial one for the first iteration, or the result of the previous iteration
2. `x`: The corresponding list element for this iteration

**`acc`**

The initial accumulator value.

The accumulator value is evaluated in any case before the first iteration starts.

To avoid evaluation even before the `list` argument is given an eta expansion can be used:

```
list: lib.foldl' op acc list
```

**`list`**

The list to fold

##### Type

```
foldl' :: (a -> b -> a) -> a -> [b] -> a
```

##### Examples

Example 160.

lib.lists.foldl'

usage example

Located at lib/lists.nix:278 in `<nixpkgs>`.

#### `lib.lists.imap0`

Map with index starting from 0

##### Inputs

**`f`**

1. Function argument

**`list`**

2. Function argument

##### Type

```
imap0 :: (Int -> a -> b) -> [a] -> [b]
```

##### Examples

Example 161.

lib.lists.imap0

usage example

Located at lib/lists.nix:315 in `<nixpkgs>`.

#### `lib.lists.imap1`

Map with index starting from 1

##### Inputs

**`f`**

1. Function argument

**`list`**

2. Function argument

##### Type

```
imap1 :: (Int -> a -> b) -> [a] -> [b]
```

##### Examples

Example 162.

lib.lists.imap1

usage example

Located at lib/lists.nix:347 in `<nixpkgs>`.

#### `lib.lists.ifilter0`

Filter a list for elements that satisfy a predicate function. The predicate function is called with both the index and value for each element. It must return `true`/`false` to include/exclude a given element in the result. This function is strict in the result of the predicate function for each element. This function has O(n) complexity.

Also see `builtins.filter` (available as `lib.lists.filter`), which can be used instead when the index isn’t needed.

##### Inputs

**`ipred`**

The predicate function, it takes two arguments:

- (int): the index of the element.
- (a): the value of the element.

It must return `true`/`false` to include/exclude a given element from the result.

**`list`**

The list to filter using the predicate.

##### Type

```
ifilter0 :: (Int -> a -> Bool) -> [a] -> [a]
```

##### Examples

Example 163.

lib.lists.ifilter0

usage example

Located at lib/lists.nix:388 in `<nixpkgs>`.

#### `lib.lists.concatMap`

Map and concatenate the result.

##### Type

```
concatMap :: (a -> [b]) -> [a] -> [b]
```

##### Examples

Example 164.

lib.lists.concatMap

usage example

Located at lib/lists.nix:414 in `<nixpkgs>`.

#### `lib.lists.flatten`

Flatten the argument into a single list; that is, nested lists are spliced into the top-level lists.

##### Inputs

**`x`**

1. Function argument

##### Type

```
flatten :: [a | [a | [a | ...]]] -> [a]
```

##### Examples

Example 165.

lib.lists.flatten

usage example

Located at lib/lists.nix:445 in `<nixpkgs>`.

#### `lib.lists.remove`

Remove elements equal to `e` from a list. Useful for `buildInputs`.

##### Inputs

**`e`**

Element to remove from `list`

**`list`**

The list

##### Type

```
remove :: a -> [a] -> [a]
```

##### Examples

Example 166.

lib.lists.remove

usage example

Located at lib/lists.nix:477 in `<nixpkgs>`.

#### `lib.lists.findSingle`

Find the sole element in the list matching the specified predicate.

Returns `default` if no such element exists, or `multiple` if there are multiple matching elements.

##### Inputs

**`pred`**

Predicate

**`default`**

Default value to return if element was not found.

**`multiple`**

Default value to return if more than one element was found

**`list`**

Input list

##### Type

```
findSingle :: (a -> Bool) -> a -> a -> [a] -> a
```

##### Examples

Example 167.

lib.lists.findSingle

usage example

Located at lib/lists.nix:525 in `<nixpkgs>`.

#### `lib.lists.findFirstIndex`

Find the first index in the list matching the specified predicate or return `default` if no such element exists.

##### Inputs

**`pred`**

Predicate

**`default`**

Default value to return

**`list`**

Input list

##### Type

```
findFirstIndex :: (a -> Bool) -> b -> [a] -> (Int | b)
```

##### Examples

Example 168.

lib.lists.findFirstIndex

usage example

Located at lib/lists.nix:575 in `<nixpkgs>`.

#### `lib.lists.findFirst`

Find the first element in the list matching the specified predicate or return `default` if no such element exists.

##### Inputs

**`pred`**

Predicate

**`default`**

Default value to return

**`list`**

Input list

##### Type

```
findFirst :: (a -> Bool) -> a -> [a] -> a
```

##### Examples

Example 169.

lib.lists.findFirst

usage example

Located at lib/lists.nix:645 in `<nixpkgs>`.

#### `lib.lists.any`

Returns true if function `pred` returns true for at least one element of `list`.

##### Inputs

**`pred`**

Predicate

**`list`**

Input list

##### Type

```
any :: (a -> Bool) -> [a] -> Bool
```

##### Examples

Example 170.

lib.lists.any

usage example

Located at lib/lists.nix:685 in `<nixpkgs>`.

#### `lib.lists.all`

Returns true if function `pred` returns true for all elements of `list`.

##### Inputs

**`pred`**

Predicate

**`list`**

Input list

##### Type

```
all :: (a -> Bool) -> [a] -> Bool
```

##### Examples

Example 171.

lib.lists.all

usage example

Located at lib/lists.nix:720 in `<nixpkgs>`.

#### `lib.lists.count`

Count how many elements of `list` match the supplied predicate function.

##### Inputs

**`pred`**

Predicate

##### Type

```
count :: (a -> Bool) -> [a] -> Int
```

##### Examples

Example 172.

lib.lists.count

usage example

Located at lib/lists.nix:749 in `<nixpkgs>`.

#### `lib.lists.optional`

Return a singleton list or an empty list, depending on a boolean value. Useful when building lists with optional elements (e.g. `++ optional (system == "i686-linux") firefox`).

##### Inputs

**`cond`**

1. Function argument

**`elem`**

2. Function argument

##### Type

```
optional :: Bool -> a -> [a]
```

##### Examples

Example 173.

lib.lists.optional

usage example

Located at lib/lists.nix:785 in `<nixpkgs>`.

#### `lib.lists.optionals`

Returns a list or an empty list, depending on a boolean value.

##### Inputs

**`cond`**

Condition

**`elems`**

List to return if condition is true

##### Type

```
optionals :: Bool -> [a] -> [a]
```

##### Examples

Example 174.

lib.lists.optionals

usage example

Located at lib/lists.nix:819 in `<nixpkgs>`.

#### `lib.lists.toList`

If argument is a list, return it; else, wrap it in a singleton list. If you’re using this, you should almost certainly reconsider if there isn’t a more “well-typed” approach.

##### Inputs

**`x`**

1. Function argument

##### Type

```
toList :: (a | [a]) -> [a]
```

##### Examples

Example 175.

lib.lists.toList

usage example

Located at lib/lists.nix:851 in `<nixpkgs>`.

#### `lib.lists.range`

Returns a list of integers from `first` up to and including `last`.

##### Inputs

**`first`**

First integer in the range

**`last`**

Last integer in the range

##### Type

```
range :: Int -> Int -> [Int]
```

##### Examples

Example 176.

lib.lists.range

usage example

Located at lib/lists.nix:885 in `<nixpkgs>`.

#### `lib.lists.replicate`

Returns a list with `n` copies of an element.

##### Inputs

**`n`**

1. Function argument

**`elem`**

2. Function argument

##### Type

```
replicate :: Int -> a -> [a]
```

##### Examples

Example 177.

lib.lists.replicate

usage example

Located at lib/lists.nix:919 in `<nixpkgs>`.

#### `lib.lists.partition`

Splits the elements of a list in two lists, `right` and `wrong`, depending on the evaluation of a predicate.

##### Inputs

**`pred`**

Predicate

**`list`**

Input list

##### Type

```
partition :: (a -> Bool) -> [a] -> { right :: [a]; wrong :: [a]; }
```

##### Examples

Example 178.

lib.lists.partition

usage example

Located at lib/lists.nix:952 in `<nixpkgs>`.

#### `lib.lists.groupBy'`

Splits the elements of a list into many lists, using the return value of a predicate. Predicate should return a string which becomes keys of attrset `groupBy` returns. `groupBy'` allows to customise the combining function and initial value

##### Inputs

**`op`**

1. Function argument

**`nul`**

2. Function argument

**`pred`**

3. Function argument

**`lst`**

4. Function argument

##### Type

```
groupBy' :: (a -> b -> a) -> a -> (b -> String) -> [b] -> { [String] :: a }
```

##### Examples

Example 179.

lib.lists.groupBy'

usage example

Located at lib/lists.nix:1007 in `<nixpkgs>`.

#### `lib.lists.zipListsWith`

Merges two lists of the same size together. If the sizes aren’t the same the merging stops at the shortest. How both lists are merged is defined by the first argument.

##### Inputs

**`f`**

Function to zip elements of both lists

**`fst`**

First list

**`snd`**

Second list

##### Type

```
zipListsWith :: (a -> b -> c) -> [a] -> [b] -> [c]
```

##### Examples

Example 180.

lib.lists.zipListsWith

usage example

Located at lib/lists.nix:1059 in `<nixpkgs>`.

#### `lib.lists.zipLists`

Merges two lists of the same size together. If the sizes aren’t the same the merging stops at the shortest.

##### Inputs

**`fst`**

First list

**`snd`**

Second list

##### Type

```
zipLists :: [a] -> [b] -> [{ fst :: a; snd :: b; }]
```

##### Examples

Example 181.

lib.lists.zipLists

usage example

Located at lib/lists.nix:1094 in `<nixpkgs>`.

#### `lib.lists.reverseList`

Reverse the order of the elements of a list.

##### Inputs

**`xs`**

1. Function argument

##### Type

```
reverseList :: [a] -> [a]
```

##### Examples

Example 182.

lib.lists.reverseList

usage example

Located at lib/lists.nix:1122 in `<nixpkgs>`.

#### `lib.lists.listDfs`

Depth-First Search (DFS) for lists `list != []`.

`before a b == true` means that `b` depends on `a` (there’s an edge from `b` to `a`).

##### Inputs

**`stopOnCycles`**

1. Function argument

**`before`**

2. Function argument

**`list`**

3. Function argument

##### Type

```
listDfs :: Bool -> (a -> a -> Bool) -> [a] -> ({ minimal :: a; visited :: [a]; rest :: [a]; } | { cycle :: a; loops :: [a]; visited :: [a]; rest :: [a]; })
```

##### Examples

Example 183.

lib.lists.listDfs

usage example

Located at lib/lists.nix:1175 in `<nixpkgs>`.

#### `lib.lists.toposort`

Sort a list based on a partial ordering using DFS. This implementation is O(N^2), if your ordering is linear, use `sort` instead.

`before a b == true` means that `b` should be after `a` in the result.

##### Inputs

**`before`**

1. Function argument

**`list`**

2. Function argument

##### Type

```
toposort :: (a -> a -> Bool) -> [a] -> ({ result :: [a]; } | { cycle :: [a]; loops :: [a]; })
```

##### Examples

Example 184.

lib.lists.toposort

usage example

Located at lib/lists.nix:1246 in `<nixpkgs>`.

#### `lib.lists.sort`

Sort a list based on a comparator function which compares two elements and returns true if the first argument is strictly below the second argument. The returned list is sorted in an increasing order. The implementation does a quick-sort.

See also `sortOn`, which applies the default comparison on a function-derived property, and may be more efficient.

##### Inputs

**`comparator`**

1. Function argument

**`list`**

2. Function argument

##### Type

```
sort :: (a -> a -> Bool) -> [a] -> [a]
```

##### Examples

Example 185.

lib.lists.sort

usage example

Located at lib/lists.nix:1305 in `<nixpkgs>`.

#### `lib.lists.sortOn`

Sort a list based on the default comparison of a derived property `b`.

The items are returned in `b`-increasing order.

**Performance**:

The passed function `f` is only evaluated once per item, unlike an unprepared `sort` using `f p < f q`.

**Laws**:

```
sortOn f == sort (p: q: f p < f q)
```

##### Inputs

**`f`**

1. Function argument

**`list`**

2. Function argument

##### Type

```
sortOn :: (a -> b) -> [a] -> [a], for comparable b
```

##### Examples

Example 186.

lib.lists.sortOn

usage example

Located at lib/lists.nix:1350 in `<nixpkgs>`.

#### `lib.lists.compareLists`

Compare two lists element-by-element with a comparison function `cmp`.

List elements are compared pairwise in order by the provided comparison function `cmp`, the first non-equal pair of elements determines the result.

### Note

The `<` operator can also be used to compare lists using a boolean condition. (e.g. `[1 2] < [1 3]` is `true`). See also language operators for more information.

##### Inputs

**`cmp`**

The comparison function `a: b: ...` must return:

- `0` if `a` and `b` are equal
- `1` if `a` is greater than `b`
- `-1` if `a` is less than `b`

See lib.compare for a an example implementation.

**`a`**

The first list

**`b`**

The second list

##### Type

```
compareLists :: (a -> a -> Int) -> [a] -> [a] -> Int
```

##### Examples

Example 187.

lib.lists.compareLists

usage examples

Located at lib/lists.nix:1420 in `<nixpkgs>`.

#### `lib.lists.naturalSort`

Sort list using “Natural sorting”. Numeric portions of strings are sorted in numeric order.

##### Inputs

**`lst`**

1. Function argument

##### Type

```
naturalSort :: [String] -> [String]
```

##### Examples

Example 188.

lib.lists.naturalSort

usage example

Located at lib/lists.nix:1463 in `<nixpkgs>`.

#### `lib.lists.take`

Returns the first (at most) N elements of a list.

##### Inputs

**`count`**

Number of elements to take

**`list`**

Input list

##### Type

```
take :: Int -> [a] -> [a]
```

##### Examples

Example 189.

lib.lists.take

usage example

Located at lib/lists.nix:1507 in `<nixpkgs>`.

#### `lib.lists.takeEnd`

Returns the last (at most) N elements of a list.

##### Inputs

**`count`**

Maximum number of elements to pick

**`list`**

Input list

##### Type

```
takeEnd :: Int -> [a] -> [a]
```

##### Examples

Example 190.

lib.lists.takeEnd

usage example

Located at lib/lists.nix:1541 in `<nixpkgs>`.

#### `lib.lists.drop`

Remove the first (at most) N elements of a list.

##### Inputs

**`count`**

Number of elements to drop

**`list`**

Input list

##### Type

```
drop :: Int -> [a] -> [a]
```

##### Examples

Example 191.

lib.lists.drop

usage example

Located at lib/lists.nix:1575 in `<nixpkgs>`.

#### `lib.lists.dropEnd`

Remove the last (at most) N elements of a list.

##### Inputs

**`count`**

Number of elements to drop

**`list`**

Input list

##### Type

```
dropEnd :: Int -> [a] -> [a]
```

##### Examples

Example 192.

lib.lists.dropEnd

usage example

Located at lib/lists.nix:1609 in `<nixpkgs>`.

#### `lib.lists.hasPrefix`

Whether the first list is a prefix of the second list.

##### Inputs

**`list1`**

1. Function argument

**`list2`**

2. Function argument

##### Type

```
hasPrefix :: [a] -> [a] -> Bool
```

##### Examples

Example 193.

lib.lists.hasPrefix

usage example

Located at lib/lists.nix:1643 in `<nixpkgs>`.

#### `lib.lists.removePrefix`

Remove the first list as a prefix from the second list. Error if the first list isn’t a prefix of the second list.

##### Inputs

**`list1`**

1. Function argument

**`list2`**

2. Function argument

##### Type

```
removePrefix :: [a] -> [a] -> [a]
```

##### Examples

Example 194.

lib.lists.removePrefix

usage example

Located at lib/lists.nix:1678 in `<nixpkgs>`.

#### `lib.lists.sublist`

Returns a list consisting of at most `count` elements of `list`, starting at index `start`.

##### Inputs

**`start`**

Index at which to start the sublist

**`count`**

Number of elements to take

**`list`**

Input list

##### Type

```
sublist :: Int -> Int -> [a] -> [a]
```

##### Examples

Example 195.

lib.lists.sublist

usage example

Located at lib/lists.nix:1722 in `<nixpkgs>`.

#### `lib.lists.commonPrefix`

The common prefix of two lists.

##### Inputs

**`list1`**

1. Function argument

**`list2`**

2. Function argument

##### Type

```
commonPrefix :: [a] -> [a] -> [a]
```

##### Examples

Example 196.

lib.lists.commonPrefix

usage example

Located at lib/lists.nix:1770 in `<nixpkgs>`.

#### `lib.lists.last`

Returns the last element of a list.

This function throws an error if the list is empty.

##### Inputs

**`list`**

1. Function argument

##### Type

```
last :: [a] -> a
```

##### Examples

Example 197.

lib.lists.last

usage example

Located at lib/lists.nix:1811 in `<nixpkgs>`.

#### `lib.lists.init`

Returns all elements but the last.

This function throws an error if the list is empty.

##### Inputs

**`list`**

1. Function argument

##### Type

```
init :: [a] -> [a]
```

##### Examples

Example 198.

lib.lists.init

usage example

Located at lib/lists.nix:1844 in `<nixpkgs>`.

#### `lib.lists.crossLists`

Returns the image of the cross product of some lists by a function.

##### Examples

Example 199.

lib.lists.crossLists

usage example

Located at lib/lists.nix:1869 in `<nixpkgs>`.

#### `lib.lists.unique`

Remove duplicate elements from the `list`. O(n^2) complexity.

### Note

If the list only contains strings and order is not important, the complexity can be reduced to O(n log n) by using `lib.lists.uniqueStrings` instead.

##### Inputs

**`list`**

Input list

##### Type

```
unique :: [a] -> [a]
```

##### Examples

Example 200.

lib.lists.unique

usage example

Located at lib/lists.nix:1901 in `<nixpkgs>`.

#### `lib.lists.uniqueStrings`

Removes duplicate strings from the `list`. O(n log n) complexity.

### Note

Order is not preserved.

All elements of the list must be strings without context.

This function fails when the list contains a non-string element or a string with context. In that case use `lib.lists.unique` instead.

##### Inputs

**`list`**

List of strings

##### Type

```
uniqueStrings :: [String] -> [String]
```

##### Examples

Example 201.

lib.lists.uniqueStrings

usage example

Located at lib/lists.nix:1938 in `<nixpkgs>`.

#### `lib.lists.allUnique`

Check if list contains only unique elements. O(n^2) complexity.

##### Inputs

**`list`**

1. Function argument

##### Type

```
allUnique :: [a] -> Bool
```

##### Examples

Example 202.

lib.lists.allUnique

usage example

Located at lib/lists.nix:1968 in `<nixpkgs>`.

#### `lib.lists.intersectLists`

Intersects list `list1` and another list (`list2`).

O(nm) complexity.

##### Inputs

**`list1`**

First list

**`list2`**

Second list

##### Type

```
intersectLists :: [a] -> [a] -> [a]
```

##### Examples

Example 203.

lib.lists.intersectLists

usage example

Located at lib/lists.nix:2002 in `<nixpkgs>`.

#### `lib.lists.subtractLists`

Subtracts list `e` from another list (`list2`).

O(nm) complexity.

##### Inputs

**`e`**

First list

**`list2`**

Second list

##### Type

```
subtractLists :: [a] -> [a] -> [a]
```

##### Examples

Example 204.

lib.lists.subtractLists

usage example

Located at lib/lists.nix:2036 in `<nixpkgs>`.

#### `lib.lists.mutuallyExclusive`

Test if two lists have no common element. It should be slightly more efficient than `intersectLists a b == []`.

##### Inputs

**`a`**

1. Function argument

**`b`**

2. Function argument

##### Type

```
mutuallyExclusive :: [a] -> [a] -> Bool
```

Located at lib/lists.nix:2058 in `<nixpkgs>`.

#### `lib.lists.concatAttrValues`

Concatenate all attributes of an attribute set. This assumes that every attribute of the set is a list.

##### Inputs

**`set`**

Attribute set with attributes that are lists

##### Type

```
concatAttrValues :: { [String] :: [a] } -> [a]
```

##### Examples

Example 205.

lib.concatAttrValues

usage example

Located at lib/lists.nix:2087 in `<nixpkgs>`.

#### `lib.lists.replaceElemAt`

Replaces a list’s nth element with a new element

##### Inputs

**`list`**

Input list

**`idx`**

index to replace

**`newElem`**

new element to replace with

##### Type

```
replaceElemAt :: [a] -> Int -> a -> [a]
```

##### Examples

Example 206.

replaceElemAt

usage example

Located at lib/lists.nix:2120 in `<nixpkgs>`.

### lib.debug: debugging functions

Collection of functions useful for debugging broken nix expressions.

- `trace`-like functions take two values, print the first to stderr and return the second.
- `traceVal`-like functions take one argument which both printed and returned.
- `traceSeq`-like functions fully evaluate their traced value before printing (not just to “weak head normal form” like trace does by default).
- Functions that end in `-Fn` take an additional function as their first argument, which is applied to the traced value before it is printed.

#### `lib.debug.traceIf`

Conditionally trace the supplied message, based on a predicate.

##### Inputs

**`pred`**

Predicate to check

**`msg`**
