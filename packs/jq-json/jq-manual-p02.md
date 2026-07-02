---
title: "jq 1.8 Manual (part 2/4)"
source: https://jqlang.github.io/jq/manual/
domain: jq-json
license: CC-BY-SA-4.0
tags: jq json, json processor, command-line json, json filter
fetched: 2026-07-02
part: 2/4
---

## Builtin operators and functions

Some jq operators (for instance, `+`) do different things depending on the type of their arguments (arrays, numbers, etc.). However, jq never does implicit type conversions. If you try to add a string to an object you'll get an error message and no result.

Please note that all numbers are converted to IEEE754 double precision floating point representation. Arithmetic and logical operators are working with these converted doubles. Results of all such operations are also limited to the double precision.

The only exception to this behaviour of number is a snapshot of original number literal. When a number which originally was provided as a literal is never mutated until the end of the program then it is printed to the output in its original literal form. This also includes cases when the original literal would be truncated when converted to the IEEE754 double precision floating point number.

### Addition: `+`

The operator `+` takes two filters, applies them both to the same input, and adds the results together. What "adding" means depends on the types involved:

- **Numbers** are added by normal arithmetic.
- **Arrays** are added by being concatenated into a larger array.
- **Strings** are added by being joined into a larger string.
- **Objects** are added by merging, that is, inserting all the key-value pairs from both objects into a single combined object. If both objects contain a value for the same key, the object on the right of the `+` wins. (For recursive merge use the `*` operator.)

`null` can be added to any value, and returns the other value unchanged.

| Command | jq '.a + 1' |
|---|---|
| Input | {"a": 7} |
| Output | 8 |
| Run |   |

| Command | jq '.a + .b' |
|---|---|
| Input | {"a": [1,2], "b": [3,4]} |
| Output | [1,2,3,4] |
| Run |   |

| Command | jq '.a + null' |
|---|---|
| Input | {"a": 1} |
| Output | 1 |
| Run |   |

| Command | jq '.a + 1' |
|---|---|
| Input | {} |
| Output | 1 |
| Run |   |

| Command | jq '{a: 1} + {b: 2} + {c: 3} + {a: 42}' |
|---|---|
| Input | null |
| Output | {"a": 42, "b": 2, "c": 3} |
| Run |   |

### Subtraction: `-`

As well as normal arithmetic subtraction on numbers, the `-` operator can be used on arrays to remove all occurrences of the second array's elements from the first array.

| Command | jq '4 - .a' |
|---|---|
| Input | {"a":3} |
| Output | 1 |
| Run |   |

| Command | jq '. - ["xml", "yaml"]' |
|---|---|
| Input | ["xml", "yaml", "json"] |
| Output | ["json"] |
| Run |   |

### Multiplication, division, modulo: `*`, `/`, `%`

These infix operators behave as expected when given two numbers. Division by zero raises an error. `x % y` computes x modulo y.

Multiplying a string by a number produces the concatenation of that string that many times. `"x" * 0` produces `""`.

Dividing a string by another splits the first using the second as separators.

Multiplying two objects will merge them recursively: this works like addition but if both objects contain a value for the same key, and the values are objects, the two are merged with the same strategy.

| Command | jq '10 / . * 3' |
|---|---|
| Input | 5 |
| Output | 6 |
| Run |   |

| Command | jq '. / ", "' |
|---|---|
| Input | "a, b,c,d, e" |
| Output | ["a","b,c,d","e"] |
| Run |   |

| Command | jq '{"k": {"a": 1, "b": 2}} * {"k": {"a": 0,"c": 3}}' |
|---|---|
| Input | null |
| Output | {"k": {"a": 0, "b": 2, "c": 3}} |
| Run |   |

| Command | jq '.[] \| (1 / .)?' |
|---|---|
| Input | [1,0,-1] |
| Output | 1 |
|   | -1 |
| Run |   |

### `abs`

The builtin function `abs` is defined naively as: `if . < 0 then - . else . end`.

For numeric input, this is the absolute value. See the section on the identity filter for the implications of this definition for numeric input.

To compute the absolute value of a number as a floating point number, you may wish use `fabs`.

| Command | jq 'map(abs)' |
|---|---|
| Input | [-10, -1.1, -1e-1] |
| Output | [10,1.1,1e-1] |
| Run |   |

### `length`

The builtin function `length` gets the length of various different types of value:

- The length of a **string** is the number of Unicode codepoints it contains (which will be the same as its JSON-encoded length in bytes if it's pure ASCII).
- The length of a **number** is its absolute value.
- The length of an **array** is the number of elements.
- The length of an **object** is the number of key-value pairs.
- The length of **null** is zero.
- It is an error to use `length` on a **boolean**.

| Command | jq '.[] \| length' |
|---|---|
| Input | [[1,2], "string", {"a":2}, null, -5] |
| Output | 2 |
|   | 6 |
|   | 1 |
|   | 0 |
|   | 5 |
| Run |   |

### `utf8bytelength`

The builtin function `utf8bytelength` outputs the number of bytes used to encode a string in UTF-8.

| Command | jq 'utf8bytelength' |
|---|---|
| Input | "\u03bc" |
| Output | 2 |
| Run |   |

### `keys`, `keys_unsorted`

The builtin function `keys`, when given an object, returns its keys in an array.

The keys are sorted "alphabetically", by unicode codepoint order. This is not an order that makes particular sense in any particular language, but you can count on it being the same for any two objects with the same set of keys, regardless of locale settings.

When `keys` is given an array, it returns the valid indices for that array: the integers from 0 to length-1.

The `keys_unsorted` function is just like `keys`, but if the input is an object then the keys will not be sorted, instead the keys will roughly be in insertion order.

| Command | jq 'keys' |
|---|---|
| Input | {"abc": 1, "abcd": 2, "Foo": 3} |
| Output | ["Foo", "abc", "abcd"] |
| Run |   |

| Command | jq 'keys' |
|---|---|
| Input | [42,3,35] |
| Output | [0,1,2] |
| Run |   |

### `has(key)`

The builtin function `has` returns whether the input object has the given key, or the input array has an element at the given index.

`has($key)` has the same effect as checking whether `$key` is a member of the array returned by `keys`, although `has` will be faster.

| Command | jq 'map(has("foo"))' |
|---|---|
| Input | [{"foo": 42}, {}] |
| Output | [true, false] |
| Run |   |

| Command | jq 'map(has(2))' |
|---|---|
| Input | [[0,1], ["a","b","c"]] |
| Output | [false, true] |
| Run |   |

### `in`

The builtin function `in` returns whether or not the input key is in the given object, or the input index corresponds to an element in the given array. It is, essentially, an inversed version of `has`.

| Command | jq '.[] \| in({"foo": 42})' |
|---|---|
| Input | ["foo", "bar"] |
| Output | true |
|   | false |
| Run |   |

| Command | jq 'map(in([0,1]))' |
|---|---|
| Input | [2, 0] |
| Output | [false, true] |
| Run |   |

### `map(f)`, `map_values(f)`

For any filter `f`, `map(f)` and `map_values(f)` apply `f` to each of the values in the input array or object, that is, to the values of `.[]`.

In the absence of errors, `map(f)` always outputs an array whereas `map_values(f)` outputs an array if given an array, or an object if given an object.

When the input to `map_values(f)` is an object, the output object has the same keys as the input object except for those keys whose values when piped to `f` produce no values at all.

The key difference between `map(f)` and `map_values(f)` is that the former simply forms an array from all the values of `($x|f)` for each value, `$x`, in the input array or object, but `map_values(f)` only uses `first($x|f)`.

Specifically, for object inputs, `map_values(f)` constructs the output object by examining in turn the value of `first(.[$k]|f)` for each key, `$k`, of the input. If this expression produces no values, then the corresponding key will be dropped; otherwise, the output object will have that value at the key, `$k`.

Here are some examples to clarify the behavior of `map` and `map_values` when applied to arrays. These examples assume the input is `[1]` in all cases:

```
map(.+1)          #=>  [2]
map(., .)         #=>  [1,1]
map(empty)        #=>  []

map_values(.+1)   #=>  [2]
map_values(., .)  #=>  [1]
map_values(empty) #=>  []
```

`map(f)` is equivalent to `[.[] | f]` and `map_values(f)` is equivalent to `.[] |= f`.

In fact, these are their implementations.

| Command | jq 'map(.+1)' |
|---|---|
| Input | [1,2,3] |
| Output | [2,3,4] |
| Run |   |

| Command | jq 'map_values(.+1)' |
|---|---|
| Input | {"a": 1, "b": 2, "c": 3} |
| Output | {"a": 2, "b": 3, "c": 4} |
| Run |   |

| Command | jq 'map(., .)' |
|---|---|
| Input | [1,2] |
| Output | [1,1,2,2] |
| Run |   |

| Command | jq 'map_values(. // empty)' |
|---|---|
| Input | {"a": null, "b": true, "c": false} |
| Output | {"b":true} |
| Run |   |

### `pick(pathexps)`

Emit the projection of the input object or array defined by the specified sequence of path expressions, such that if `p` is any one of these specifications, then `(. | p)` will evaluate to the same value as `(. | pick(pathexps) | p)`. For arrays, negative indices and `.[m:n]` specifications should not be used.

| Command | jq 'pick(.a, .b.c, .x)' |
|---|---|
| Input | {"a": 1, "b": {"c": 2, "d": 3}, "e": 4} |
| Output | {"a":1,"b":{"c":2},"x":null} |
| Run |   |

| Command | jq 'pick(.[2], .[0], .[0])' |
|---|---|
| Input | [1,2,3,4] |
| Output | [1,null,3] |
| Run |   |

### `path(path_expression)`

Outputs array representations of the given path expression in `.`. The outputs are arrays of strings (object keys) and/or numbers (array indices).

Path expressions are jq expressions like `.a`, but also `.[]`. There are two types of path expressions: ones that can match exactly, and ones that cannot. For example, `.a.b.c` is an exact match path expression, while `.a[].b` is not.

`path(exact_path_expression)` will produce the array representation of the path expression even if it does not exist in `.`, if `.` is `null` or an array or an object.

`path(pattern)` will produce array representations of the paths matching `pattern` if the paths exist in `.`.

Note that the path expressions are not different from normal expressions. The expression `path(..|select(type=="boolean"))` outputs all the paths to boolean values in `.`, and only those paths.

| Command | jq 'path(.a[0].b)' |
|---|---|
| Input | null |
| Output | ["a",0,"b"] |
| Run |   |

| Command | jq '[path(..)]' |
|---|---|
| Input | {"a":[{"b":1}]} |
| Output | [[],["a"],["a",0],["a",0,"b"]] |
| Run |   |

### `del(path_expression)`

The builtin function `del` removes a key and its corresponding value from an object.

| Command | jq 'del(.foo)' |
|---|---|
| Input | {"foo": 42, "bar": 9001, "baz": 42} |
| Output | {"bar": 9001, "baz": 42} |
| Run |   |

| Command | jq 'del(.[1, 2])' |
|---|---|
| Input | ["foo", "bar", "baz"] |
| Output | ["foo"] |
| Run |   |

### `getpath(PATHS)`

The builtin function `getpath` outputs the values in `.` found at each path in `PATHS`.

| Command | jq 'getpath(["a","b"])' |
|---|---|
| Input | null |
| Output | null |
| Run |   |

| Command | jq '[getpath(["a","b"], ["a","c"])]' |
|---|---|
| Input | {"a":{"b":0, "c":1}} |
| Output | [0, 1] |
| Run |   |

### `setpath(PATHS; VALUE)`

The builtin function `setpath` sets the `PATHS` in `.` to `VALUE`.

| Command | jq 'setpath(["a","b"]; 1)' |
|---|---|
| Input | null |
| Output | {"a": {"b": 1}} |
| Run |   |

| Command | jq 'setpath(["a","b"]; 1)' |
|---|---|
| Input | {"a":{"b":0}} |
| Output | {"a": {"b": 1}} |
| Run |   |

| Command | jq 'setpath([0,"a"]; 1)' |
|---|---|
| Input | null |
| Output | [{"a":1}] |
| Run |   |

### `delpaths(PATHS)`

The builtin function `delpaths` deletes the `PATHS` in `.`. `PATHS` must be an array of paths, where each path is an array of strings and numbers.

| Command | jq 'delpaths([["a","b"]])' |
|---|---|
| Input | {"a":{"b":1},"x":{"y":2}} |
| Output | {"a":{},"x":{"y":2}} |
| Run |   |

### `to_entries`, `from_entries`, `with_entries(f)`

These functions convert between an object and an array of key-value pairs. If `to_entries` is passed an object, then for each `k: v` entry in the input, the output array includes `{"key": k, "value": v}`.

`from_entries` does the opposite conversion, and `with_entries(f)` is a shorthand for `to_entries | map(f) | from_entries`, useful for doing some operation to all keys and values of an object. `from_entries` accepts `"key"`, `"Key"`, `"name"`, `"Name"`, `"value"`, and `"Value"` as keys.

| Command | jq 'to_entries' |
|---|---|
| Input | {"a": 1, "b": 2} |
| Output | [{"key":"a", "value":1}, {"key":"b", "value":2}] |
| Run |   |

| Command | jq 'from_entries' |
|---|---|
| Input | [{"key":"a", "value":1}, {"key":"b", "value":2}] |
| Output | {"a": 1, "b": 2} |
| Run |   |

| Command | jq 'with_entries(.key \|= "KEY_" + .)' |
|---|---|
| Input | {"a": 1, "b": 2} |
| Output | {"KEY_a": 1, "KEY_b": 2} |
| Run |   |

### `select(boolean_expression)`

The function `select(f)` produces its input unchanged if `f` returns true for that input, and produces no output otherwise.

It's useful for filtering lists: `[1,2,3] | map(select(. >= 2))` will give you `[2,3]`.

| Command | jq 'map(select(. >= 2))' |
|---|---|
| Input | [1,5,3,0,7] |
| Output | [5,3,7] |
| Run |   |

| Command | jq '.[] \| select(.id == "second")' |
|---|---|
| Input | [{"id": "first", "val": 1}, {"id": "second", "val": 2}] |
| Output | {"id": "second", "val": 2} |
| Run |   |

### `arrays`, `objects`, `iterables`, `booleans`, `numbers`, `normals`, `finites`, `strings`, `nulls`, `values`, `scalars`

These built-ins select only inputs that are arrays, objects, iterables (arrays or objects), booleans, numbers, normal numbers, finite numbers, strings, null, non-null values, and non-iterables, respectively.

| Command | jq '.[]\|numbers' |
|---|---|
| Input | [[],{},1,"foo",null,true,false] |
| Output | 1 |
| Run |   |

### `empty`

`empty` returns no results. None at all. Not even `null`.

It's useful on occasion. You'll know if you need it :)

| Command | jq '1, empty, 2' |
|---|---|
| Input | null |
| Output | 1 |
|   | 2 |
| Run |   |

| Command | jq '[1,2,empty,3]' |
|---|---|
| Input | null |
| Output | [1,2,3] |
| Run |   |

### `error`, `error(message)`

Produces an error with the input value, or with the message given as the argument. Errors can be caught with try/catch; see below.

| Command | jq 'try error catch .' |
|---|---|
| Input | "error message" |
| Output | "error message" |
| Run |   |

| Command | jq 'try error("invalid value: \(.)") catch .' |
|---|---|
| Input | 42 |
| Output | "invalid value: 42" |
| Run |   |

### `halt`

Stops the jq program with no further outputs. jq will exit with exit status `0`.

### `halt_error`, `halt_error(exit_code)`

Stops the jq program with no further outputs. The input will be printed on `stderr` as raw output (i.e., strings will not have double quotes) with no decoration, not even a newline.

The given `exit_code` (defaulting to `5`) will be jq's exit status.

For example, `"Error: something went wrong\n"|halt_error(1)`.

### `$__loc__`

Produces an object with a "file" key and a "line" key, with the filename and line number where `$__loc__` occurs, as values.

| Command | jq 'try error("\($__loc__)") catch .' |
|---|---|
| Input | null |
| Output | "{\"file\":\"<top-level>\",\"line\":1}" |
| Run |   |

### `paths`, `paths(node_filter)`

`paths` outputs the paths to all the elements in its input (except it does not output the empty list, representing . itself).

`paths(f)` outputs the paths to any values for which `f` is `true`. That is, `paths(type == "number")` outputs the paths to all numeric values.

| Command | jq '[paths]' |
|---|---|
| Input | [1,[[],{"a":2}]] |
| Output | [[0],[1],[1,0],[1,1],[1,1,"a"]] |
| Run |   |

| Command | jq '[paths(type == "number")]' |
|---|---|
| Input | [1,[[],{"a":2}]] |
| Output | [[0],[1,1,"a"]] |
| Run |   |

### `add`, `add(generator)`

The filter `add` takes as input an array, and produces as output the elements of the array added together. This might mean summed, concatenated or merged depending on the types of the elements of the input array - the rules are the same as those for the `+` operator (described above).

If the input is an empty array, `add` returns `null`.

`add(generator)` operates on the given generator rather than the input.

| Command | jq 'add' |
|---|---|
| Input | ["a","b","c"] |
| Output | "abc" |
| Run |   |

| Command | jq 'add' |
|---|---|
| Input | [1, 2, 3] |
| Output | 6 |
| Run |   |

| Command | jq 'add' |
|---|---|
| Input | [] |
| Output | null |
| Run |   |

| Command | jq 'add(.[].a)' |
|---|---|
| Input | [{"a":3}, {"a":5}, {"b":6}] |
| Output | 8 |
| Run |   |

### `any`, `any(condition)`, `any(generator; condition)`

The filter `any` takes as input an array of boolean values, and produces `true` as output if any of the elements of the array are `true`.

If the input is an empty array, `any` returns `false`.

The `any(condition)` form applies the given condition to the elements of the input array.

The `any(generator; condition)` form applies the given condition to all the outputs of the given generator.

| Command | jq 'any' |
|---|---|
| Input | [true, false] |
| Output | true |
| Run |   |

| Command | jq 'any' |
|---|---|
| Input | [false, false] |
| Output | false |
| Run |   |

| Command | jq 'any' |
|---|---|
| Input | [] |
| Output | false |
| Run |   |

### `all`, `all(condition)`, `all(generator; condition)`

The filter `all` takes as input an array of boolean values, and produces `true` as output if all of the elements of the array are `true`.

The `all(condition)` form applies the given condition to the elements of the input array.

The `all(generator; condition)` form applies the given condition to all the outputs of the given generator.

If the input is an empty array, `all` returns `true`.

| Command | jq 'all' |
|---|---|
| Input | [true, false] |
| Output | false |
| Run |   |

| Command | jq 'all' |
|---|---|
| Input | [true, true] |
| Output | true |
| Run |   |

| Command | jq 'all' |
|---|---|
| Input | [] |
| Output | true |
| Run |   |

### `flatten`, `flatten(depth)`

The filter `flatten` takes as input an array of nested arrays, and produces a flat array in which all arrays inside the original array have been recursively replaced by their values. You can pass an argument to it to specify how many levels of nesting to flatten.

`flatten(2)` is like `flatten`, but going only up to two levels deep.

| Command | jq 'flatten' |
|---|---|
| Input | [1, [2], [[3]]] |
| Output | [1, 2, 3] |
| Run |   |

| Command | jq 'flatten(1)' |
|---|---|
| Input | [1, [2], [[3]]] |
| Output | [1, 2, [3]] |
| Run |   |

| Command | jq 'flatten' |
|---|---|
| Input | [[]] |
| Output | [] |
| Run |   |

| Command | jq 'flatten' |
|---|---|
| Input | [{"foo": "bar"}, [{"foo": "baz"}]] |
| Output | [{"foo": "bar"}, {"foo": "baz"}] |
| Run |   |

### `range(upto)`, `range(from; upto)`, `range(from; upto; by)`

The `range` function produces a range of numbers. `range(4; 10)` produces 6 numbers, from 4 (inclusive) to 10 (exclusive). The numbers are produced as separate outputs. Use `[range(4; 10)]` to get a range as an array.

The one argument form generates numbers from 0 to the given number, with an increment of 1.

The two argument form generates numbers from `from` to `upto` with an increment of 1.

The three argument form generates numbers `from` to `upto` with an increment of `by`.

| Command | jq 'range(2; 4)' |
|---|---|
| Input | null |
| Output | 2 |
|   | 3 |
| Run |   |

| Command | jq '[range(2; 4)]' |
|---|---|
| Input | null |
| Output | [2,3] |
| Run |   |

| Command | jq '[range(4)]' |
|---|---|
| Input | null |
| Output | [0,1,2,3] |
| Run |   |

| Command | jq '[range(0; 10; 3)]' |
|---|---|
| Input | null |
| Output | [0,3,6,9] |
| Run |   |

| Command | jq '[range(0; 10; -1)]' |
|---|---|
| Input | null |
| Output | [] |
| Run |   |

| Command | jq '[range(0; -5; -1)]' |
|---|---|
| Input | null |
| Output | [0,-1,-2,-3,-4] |
| Run |   |

### `floor`

The `floor` function returns the floor of its numeric input.

| Command | jq 'floor' |
|---|---|
| Input | 3.14159 |
| Output | 3 |
| Run |   |

### `sqrt`

The `sqrt` function returns the square root of its numeric input.

| Command | jq 'sqrt' |
|---|---|
| Input | 9 |
| Output | 3 |
| Run |   |

### `tonumber`

The `tonumber` function parses its input as a number. It will convert correctly-formatted strings to their numeric equivalent, leave numbers alone, and give an error on all other input.

| Command | jq '.[] \| tonumber' |
|---|---|
| Input | [1, "1"] |
| Output | 1 |
|   | 1 |
| Run |   |

### `toboolean`

The `toboolean` function parses its input as a boolean. It will convert correctly-formatted strings to their boolean equivalent, leave booleans alone, and give an error on all other input.

| Command | jq '.[] \| toboolean' |
|---|---|
| Input | ["true", "false", true, false] |
| Output | true |
|   | false |
|   | true |
|   | false |
| Run |   |

### `tostring`

The `tostring` function prints its input as a string. Strings are left unchanged, and all other values are JSON-encoded.

| Command | jq '.[] \| tostring' |
|---|---|
| Input | [1, "1", [1]] |
| Output | "1" |
|   | "1" |
|   | "[1]" |
| Run |   |

### `type`

The `type` function returns the type of its argument as a string, which is one of null, boolean, number, string, array or object.

| Command | jq 'map(type)' |
|---|---|
| Input | [0, false, [], {}, null, "hello"] |
| Output | ["number", "boolean", "array", "object", "null", "string"] |
| Run |   |

### `infinite`, `nan`, `isinfinite`, `isnan`, `isfinite`, `isnormal`

Some arithmetic operations can yield infinities and "not a number" (NaN) values. The `isinfinite` builtin returns `true` if its input is infinite. The `isnan` builtin returns `true` if its input is a NaN. The `infinite` builtin returns a positive infinite value. The `nan` builtin returns a NaN. The `isnormal` builtin returns true if its input is a normal number.

Note that division by zero raises an error.

Currently most arithmetic operations operating on infinities, NaNs, and sub-normals do not raise errors.

| Command | jq '.[] \| (infinite * .) < 0' |
|---|---|
| Input | [-1, 1] |
| Output | true |
|   | false |
| Run |   |

| Command | jq 'infinite, nan \| type' |
|---|---|
| Input | null |
| Output | "number" |
|   | "number" |
| Run |   |

### `sort`, `sort_by(path_expression)`

The `sort` functions sorts its input, which must be an array. Values are sorted in the following order:

- `null`
- `false`
- `true`
- numbers
- strings, in alphabetical order (by unicode codepoint value)
- arrays, in lexical order
- objects

The ordering for objects is a little complex: first they're compared by comparing their sets of keys (as arrays in sorted order), and if their keys are equal then the values are compared key by key.

`sort_by` may be used to sort by a particular field of an object, or by applying any jq filter. `sort_by(f)` compares two elements by comparing the result of `f` on each element. When `f` produces multiple values, it firstly compares the first values, and the second values if the first values are equal, and so on.

| Command | jq 'sort' |
|---|---|
| Input | [8,3,null,6] |
| Output | [null,3,6,8] |
| Run |   |

| Command | jq 'sort_by(.foo)' |
|---|---|
| Input | [{"foo":4, "bar":10}, {"foo":3, "bar":10}, {"foo":2, "bar":1}] |
| Output | [{"foo":2, "bar":1}, {"foo":3, "bar":10}, {"foo":4, "bar":10}] |
| Run |   |

| Command | jq 'sort_by(.foo, .bar)' |
|---|---|
| Input | [{"foo":4, "bar":10}, {"foo":3, "bar":20}, {"foo":2, "bar":1}, {"foo":3, "bar":10}] |
| Output | [{"foo":2, "bar":1}, {"foo":3, "bar":10}, {"foo":3, "bar":20}, {"foo":4, "bar":10}] |
| Run |   |

### `group_by(path_expression)`

`group_by(.foo)` takes as input an array, groups the elements having the same `.foo` field into separate arrays, and produces all of these arrays as elements of a larger array, sorted by the value of the `.foo` field.

Any jq expression, not just a field access, may be used in place of `.foo`. The sorting order is the same as described in the `sort` function above.

| Command | jq 'group_by(.foo)' |
|---|---|
| Input | [{"foo":1, "bar":10}, {"foo":3, "bar":100}, {"foo":1, "bar":1}] |
| Output | [[{"foo":1, "bar":10}, {"foo":1, "bar":1}], [{"foo":3, "bar":100}]] |
| Run |   |

### `min`, `max`, `min_by(path_exp)`, `max_by(path_exp)`

Find the minimum or maximum element of the input array.

The `min_by(path_exp)` and `max_by(path_exp)` functions allow you to specify a particular field or property to examine, e.g. `min_by(.foo)` finds the object with the smallest `foo` field.

| Command | jq 'min' |
|---|---|
| Input | [5,4,2,7] |
| Output | 2 |
| Run |   |

| Command | jq 'max_by(.foo)' |
|---|---|
| Input | [{"foo":1, "bar":14}, {"foo":2, "bar":3}] |
| Output | {"foo":2, "bar":3} |
| Run |   |

### `unique`, `unique_by(path_exp)`

The `unique` function takes as input an array and produces an array of the same elements, in sorted order, with duplicates removed.

The `unique_by(path_exp)` function will keep only one element for each value obtained by applying the argument. Think of it as making an array by taking one element out of every group produced by `group`.

| Command | jq 'unique' |
|---|---|
| Input | [1,2,5,3,5,3,1,3] |
| Output | [1,2,3,5] |
| Run |   |

| Command | jq 'unique_by(.foo)' |
|---|---|
| Input | [{"foo": 1, "bar": 2}, {"foo": 1, "bar": 3}, {"foo": 4, "bar": 5}] |
| Output | [{"foo": 1, "bar": 2}, {"foo": 4, "bar": 5}] |
| Run |   |

| Command | jq 'unique_by(length)' |
|---|---|
| Input | ["chunky", "bacon", "kitten", "cicada", "asparagus"] |
| Output | ["bacon", "chunky", "asparagus"] |
| Run |   |

### `reverse`

This function reverses an array.

| Command | jq 'reverse' |
|---|---|
| Input | [1,2,3,4] |
| Output | [4,3,2,1] |
| Run |   |

### `contains(element)`

The filter `contains(b)` will produce true if b is completely contained within the input. A string B is contained in a string A if B is a substring of A. An array B is contained in an array A if all elements in B are contained in any element in A. An object B is contained in object A if all of the values in B are contained in the value in A with the same key. All other types are assumed to be contained in each other if they are equal.

| Command | jq 'contains("bar")' |
|---|---|
| Input | "foobar" |
| Output | true |
| Run |   |

| Command | jq 'contains(["baz", "bar"])' |
|---|---|
| Input | ["foobar", "foobaz", "blarp"] |
| Output | true |
| Run |   |

| Command | jq 'contains(["bazzzzz", "bar"])' |
|---|---|
| Input | ["foobar", "foobaz", "blarp"] |
| Output | false |
| Run |   |

| Command | jq 'contains({foo: 12, bar: [{barp: 12}]})' |
|---|---|
| Input | {"foo": 12, "bar":[1,2,{"barp":12, "blip":13}]} |
| Output | true |
| Run |   |

| Command | jq 'contains({foo: 12, bar: [{barp: 15}]})' |
|---|---|
| Input | {"foo": 12, "bar":[1,2,{"barp":12, "blip":13}]} |
| Output | false |
| Run |   |

### `indices(s)`

Outputs an array containing the indices in `.` where `s` occurs. The input may be an array, in which case if `s` is an array then the indices output will be those where all elements in `.` match those of `s`.

| Command | jq 'indices(", ")' |
|---|---|
| Input | "a,b, cd, efg, hijk" |
| Output | [3,7,12] |
| Run |   |

| Command | jq 'indices(1)' |
|---|---|
| Input | [0,1,2,1,3,1,4] |
| Output | [1,3,5] |
| Run |   |

| Command | jq 'indices([1,2])' |
|---|---|
| Input | [0,1,2,3,1,4,2,5,1,2,6,7] |
| Output | [1,8] |
| Run |   |

### `index(s)`, `rindex(s)`

Outputs the index of the first (`index`) or last (`rindex`) occurrence of `s` in the input.

| Command | jq 'index(", ")' |
|---|---|
| Input | "a,b, cd, efg, hijk" |
| Output | 3 |
| Run |   |

| Command | jq 'index(1)' |
|---|---|
| Input | [0,1,2,1,3,1,4] |
| Output | 1 |
| Run |   |

| Command | jq 'index([1,2])' |
|---|---|
| Input | [0,1,2,3,1,4,2,5,1,2,6,7] |
| Output | 1 |
| Run |   |

| Command | jq 'rindex(", ")' |
|---|---|
| Input | "a,b, cd, efg, hijk" |
| Output | 12 |
| Run |   |

| Command | jq 'rindex(1)' |
|---|---|
| Input | [0,1,2,1,3,1,4] |
| Output | 5 |
| Run |   |

| Command | jq 'rindex([1,2])' |
|---|---|
| Input | [0,1,2,3,1,4,2,5,1,2,6,7] |
| Output | 8 |
| Run |   |

### `inside`

The filter `inside(b)` will produce true if the input is completely contained within b. It is, essentially, an inversed version of `contains`.

| Command | jq 'inside("foobar")' |
|---|---|
| Input | "bar" |
| Output | true |
| Run |   |

| Command | jq 'inside(["foobar", "foobaz", "blarp"])' |
|---|---|
| Input | ["baz", "bar"] |
| Output | true |
| Run |   |

| Command | jq 'inside(["foobar", "foobaz", "blarp"])' |
|---|---|
| Input | ["bazzzzz", "bar"] |
| Output | false |
| Run |   |

| Command | jq 'inside({"foo": 12, "bar":[1,2,{"barp":12, "blip":13}]})' |
|---|---|
| Input | {"foo": 12, "bar": [{"barp": 12}]} |
| Output | true |
| Run |   |

| Command | jq 'inside({"foo": 12, "bar":[1,2,{"barp":12, "blip":13}]})' |
|---|---|
| Input | {"foo": 12, "bar": [{"barp": 15}]} |
| Output | false |
| Run |   |

### `startswith(str)`

Outputs `true` if . starts with the given string argument.

| Command | jq '[.[]\|startswith("foo")]' |
|---|---|
| Input | ["fo", "foo", "barfoo", "foobar", "barfoob"] |
| Output | [false, true, false, true, false] |
| Run |   |

### `endswith(str)`

Outputs `true` if . ends with the given string argument.

| Command | jq '[.[]\|endswith("foo")]' |
|---|---|
| Input | ["foobar", "barfoo"] |
| Output | [false, true] |
| Run |   |

### `combinations`, `combinations(n)`

Outputs all combinations of the elements of the arrays in the input array. If given an argument `n`, it outputs all combinations of `n` repetitions of the input array.

| Command | jq 'combinations' |
|---|---|
| Input | [[1,2], [3, 4]] |
| Output | [1, 3] |
|   | [1, 4] |
|   | [2, 3] |
|   | [2, 4] |
| Run |   |

| Command | jq 'combinations(2)' |
|---|---|
| Input | [0, 1] |
| Output | [0, 0] |
|   | [0, 1] |
|   | [1, 0] |
|   | [1, 1] |
| Run |   |

### `ltrimstr(str)`

Outputs its input with the given prefix string removed, if it starts with it.

| Command | jq '[.[]\|ltrimstr("foo")]' |
|---|---|
| Input | ["fo", "foo", "barfoo", "foobar", "afoo"] |
| Output | ["fo","","barfoo","bar","afoo"] |
| Run |   |

### `rtrimstr(str)`

Outputs its input with the given suffix string removed, if it ends with it.

| Command | jq '[.[]\|rtrimstr("foo")]' |
|---|---|
| Input | ["fo", "foo", "barfoo", "foobar", "foob"] |
| Output | ["fo","","bar","foobar","foob"] |
| Run |   |

### `trimstr(str)`

Outputs its input with the given string removed at both ends, if it starts or ends with it.

| Command | jq '[.[]\|trimstr("foo")]' |
|---|---|
| Input | ["fo", "foo", "barfoo", "foobarfoo", "foob"] |
| Output | ["fo","","bar","bar","b"] |
| Run |   |

### `trim`, `ltrim`, `rtrim`

`trim` trims both leading and trailing whitespace.

`ltrim` trims only leading (left side) whitespace.

`rtrim` trims only trailing (right side) whitespace.

Whitespace characters are the usual `" "`, `"\n"` `"\t"`, `"\r"` and also all characters in the Unicode character database with the whitespace property. Note that what considers whitespace might change in the future.

| Command | jq 'trim, ltrim, rtrim' |
|---|---|
| Input | " abc " |
| Output | "abc" |
|   | "abc " |
|   | " abc" |
| Run |   |

### `explode`

Converts an input string into an array of the string's codepoint numbers.

| Command | jq 'explode' |
|---|---|
| Input | "foobar" |
| Output | [102,111,111,98,97,114] |
| Run |   |

### `implode`

The inverse of explode.

| Command | jq 'implode' |
|---|---|
| Input | [65, 66, 67] |
| Output | "ABC" |
| Run |   |

### `split(str)`

Splits an input string on the separator argument.

`split` can also split on regex matches when called with two arguments (see the regular expressions section below).

| Command | jq 'split(", ")' |
|---|---|
| Input | "a, b,c,d, e, " |
| Output | ["a","b,c,d","e",""] |
| Run |   |

### `join(str)`

Joins the array of elements given as input, using the argument as separator. It is the inverse of `split`: that is, running `split("foo") | join("foo")` over any input string returns said input string.

Numbers and booleans in the input are converted to strings. Null values are treated as empty strings. Arrays and objects in the input are not supported.

| Command | jq 'join(", ")' |
|---|---|
| Input | ["a","b,c,d","e"] |
| Output | "a, b,c,d, e" |
| Run |   |

| Command | jq 'join(" ")' |
|---|---|
| Input | ["a",1,2.3,true,null,false] |
| Output | "a 1 2.3 true false" |
| Run |   |

### `ascii_downcase`, `ascii_upcase`

Emit a copy of the input string with its alphabetic characters (a-z and A-Z) converted to the specified case.

| Command | jq 'ascii_upcase' |
|---|---|
| Input | "useful but not for é" |
| Output | "USEFUL BUT NOT FOR é" |
| Run |   |

### `while(cond; update)`

The `while(cond; update)` function allows you to repeatedly apply an update to `.` until `cond` is false.

Note that `while(cond; update)` is internally defined as a recursive jq function. Recursive calls within `while` will not consume additional memory if `update` produces at most one output for each input. See advanced topics below.

| Command | jq '[while(.<100; .*2)]' |
|---|---|
| Input | 1 |
| Output | [1,2,4,8,16,32,64] |
| Run |   |

### `repeat(exp)`

The `repeat(exp)` function allows you to repeatedly apply expression `exp` to `.` until an error is raised.

Note that `repeat(exp)` is internally defined as a recursive jq function. Recursive calls within `repeat` will not consume additional memory if `exp` produces at most one output for each input. See advanced topics below.

| Command | jq '[repeat(.*2, error)?]' |
|---|---|
| Input | 1 |
| Output | [2] |
| Run |   |

### `until(cond; next)`

The `until(cond; next)` function allows you to repeatedly apply the expression `next`, initially to `.` then to its own output, until `cond` is true. For example, this can be used to implement a factorial function (see below).

Note that `until(cond; next)` is internally defined as a recursive jq function. Recursive calls within `until()` will not consume additional memory if `next` produces at most one output for each input. See advanced topics below.

| Command | jq '[.,1]\|until(.[0] < 1; [.[0] - 1, .[1] * .[0]])\|.[1]' |
|---|---|
| Input | 4 |
| Output | 24 |
| Run |   |

### `recurse(f)`, `recurse`, `recurse(f; condition)`

The `recurse(f)` function allows you to search through a recursive structure, and extract interesting data from all levels. Suppose your input represents a filesystem:

```
{"name": "/", "children": [
  {"name": "/bin", "children": [
    {"name": "/bin/ls", "children": []},
    {"name": "/bin/sh", "children": []}]},
  {"name": "/home", "children": [
    {"name": "/home/stephen", "children": [
      {"name": "/home/stephen/jq", "children": []}]}]}]}
```

Now suppose you want to extract all of the filenames present. You need to retrieve `.name`, `.children[].name`, `.children[].children[].name`, and so on. You can do this with:

```
recurse(.children[]) | .name
```

When called without an argument, `recurse` is equivalent to `recurse(.[]?)`.

`recurse(f)` is identical to `recurse(f; true)` and can be used without concerns about recursion depth.

`recurse(f; condition)` is a generator which begins by emitting . and then emits in turn .|f, .|f|f, .|f|f|f, ... so long as the computed value satisfies the condition. For example, to generate all the integers, at least in principle, one could write `recurse(.+1; true)`.

The recursive calls in `recurse` will not consume additional memory whenever `f` produces at most a single output for each input.

| Command | jq 'recurse(.foo[])' |
|---|---|
| Input | {"foo":[{"foo": []}, {"foo":[{"foo":[]}]}]} |
| Output | {"foo":[{"foo":[]},{"foo":[{"foo":[]}]}]} |
|   | {"foo":[]} |
|   | {"foo":[{"foo":[]}]} |
|   | {"foo":[]} |
| Run |   |

| Command | jq 'recurse' |
|---|---|
| Input | {"a":0,"b":[1]} |
| Output | {"a":0,"b":[1]} |
|   | 0 |
|   | [1] |
|   | 1 |
| Run |   |

| Command | jq 'recurse(. * .; . < 20)' |
|---|---|
| Input | 2 |
| Output | 2 |
|   | 4 |
|   | 16 |
| Run |   |

### `walk(f)`

The `walk(f)` function applies f recursively to every component of the input entity. When an array is encountered, f is first applied to its elements and then to the array itself; when an object is encountered, f is first applied to all the values and then to the object. In practice, f will usually test the type of its input, as illustrated in the following examples. The first example highlights the usefulness of processing the elements of an array of arrays before processing the array itself. The second example shows how all the keys of all the objects within the input can be considered for alteration.

| Command | jq 'walk(if type == "array" then sort else . end)' |
|---|---|
| Input | [[4, 1, 7], [8, 5, 2], [3, 6, 9]] |
| Output | [[1,4,7],[2,5,8],[3,6,9]] |
| Run |   |

| Command | jq 'walk( if type == "object" then with_entries( .key \|= sub( "^_+"; "") ) else . end )' |
|---|---|
| Input | [ { "_a": { "__b": 2 } } ] |
| Output | [{"a":{"b":2}}] |
| Run |   |

### `have_literal_numbers`

This builtin returns true if jq's build configuration includes support for preservation of input number literals.

### `have_decnum`

This builtin returns true if jq was built with "decnum", which is the current literal number preserving numeric backend implementation for jq.

### `$JQ_BUILD_CONFIGURATION`

This builtin binding shows the jq executable's build configuration. Its value has no particular format, but it can be expected to be at least the `./configure` command-line arguments, and may be enriched in the future to include the version strings for the build tooling used.

Note that this can be overridden in the command-line with `--arg` and related options.

### `$ENV`, `env`

`$ENV` is an object representing the environment variables as set when the jq program started.

`env` outputs an object representing jq's current environment.

At the moment there is no builtin for setting environment variables.

| Command | jq '$ENV.PAGER' |
|---|---|
| Input | null |
| Output | "less" |
| Run |   |

| Command | jq 'env.PAGER' |
|---|---|
| Input | null |
| Output | "less" |
| Run |   |

### `transpose`

Transpose a possibly jagged matrix (an array of arrays). Rows are padded with nulls so the result is always rectangular.

| Command | jq 'transpose' |
|---|---|
| Input | [[1], [2,3]] |
| Output | [[1,2],[null,3]] |
| Run |   |

### `bsearch(x)`

`bsearch(x)` conducts a binary search for x in the input array. If the input is sorted and contains x, then `bsearch(x)` will return its index in the array; otherwise, if the array is sorted, it will return (-1 - ix) where ix is an insertion point such that the array would still be sorted after the insertion of x at ix. If the array is not sorted, `bsearch(x)` will return an integer that is probably of no interest.

| Command | jq 'bsearch(0)' |
|---|---|
| Input | [0,1] |
| Output | 0 |
| Run |   |

| Command | jq 'bsearch(0)' |
|---|---|
| Input | [1,2,3] |
| Output | -1 |
| Run |   |

| Command | jq 'bsearch(4) as $ix \| if $ix < 0 then .[-(1+$ix)] = 4 else . end' |
|---|---|
| Input | [1,2,3] |
| Output | [1,2,3,4] |
| Run |   |

### String interpolation: `\(exp)`

Inside a string, you can put an expression inside parens after a backslash. Whatever the expression returns will be interpolated into the string.

| Command | jq '"The input was \(.), which is one less than \(.+1)"' |
|---|---|
| Input | 42 |
| Output | "The input was 42, which is one less than 43" |
| Run |   |

### Convert to/from JSON

The `tojson` and `fromjson` builtins dump values as JSON texts or parse JSON texts into values, respectively. The `tojson` builtin differs from `tostring` in that `tostring` returns strings unmodified, while `tojson` encodes strings as JSON strings.

| Command | jq '[.[]\|tostring]' |
|---|---|
| Input | [1, "foo", ["foo"]] |
| Output | ["1","foo","[\"foo\"]"] |
| Run |   |

| Command | jq '[.[]\|tojson]' |
|---|---|
| Input | [1, "foo", ["foo"]] |
| Output | ["1","\"foo\"","[\"foo\"]"] |
| Run |   |

| Command | jq '[.[]\|tojson\|fromjson]' |
|---|---|
| Input | [1, "foo", ["foo"]] |
| Output | [1,"foo",["foo"]] |
| Run |   |

### Format strings and escaping

The `@foo` syntax is used to format and escape strings, which is useful for building URLs, documents in a language like HTML or XML, and so forth. `@foo` can be used as a filter on its own, the possible escapings are:

- `@text`:

Calls `tostring`, see that function for details.

- `@json`:

Serializes the input as JSON.

- `@html`:

Applies HTML/XML escaping, by mapping the characters `<>&'"` to their entity equivalents `&lt;`, `&gt;`, `&amp;`, `&apos;`, `&quot;`.

- `@uri`:

Applies percent-encoding, by mapping all reserved URI characters to a `%XX` sequence.

- `@urid`:

The inverse of `@uri`, applies percent-decoding, by mapping all `%XX` sequences to their corresponding URI characters.

- `@csv`:

The input must be an array, and it is rendered as CSV with double quotes for strings, and quotes escaped by repetition.

- `@tsv`:

The input must be an array, and it is rendered as TSV (tab-separated values). Each input array will be printed as a single line. Fields are separated by a single tab (ascii `0x09`). Input characters line-feed (ascii `0x0a`), carriage-return (ascii `0x0d`), tab (ascii `0x09`) and backslash (ascii `0x5c`) will be output as escape sequences `\n`, `\r`, `\t`, `\\` respectively.

- `@sh`:

The input is escaped suitable for use in a command-line for a POSIX shell. If the input is an array, the output will be a series of space-separated strings.

- `@base64`:

The input is converted to base64 as specified by RFC 4648.

- `@base64d`:

The inverse of `@base64`, input is decoded as specified by RFC 4648. Note\: If the decoded string is not UTF-8, the results are undefined.

This syntax can be combined with string interpolation in a useful way. You can follow a `@foo` token with a string literal. The contents of the string literal will *not* be escaped. However, all interpolations made inside that string literal will be escaped. For instance,

```
@uri "https://www.google.com/search?q=\(.search)"
```

will produce the following output for the input `{"search":"what is jq?"}`:

```
"https://www.google.com/search?q=what%20is%20jq%3F"
```

Note that the slashes, question mark, etc. in the URL are not escaped, as they were part of the string literal.

| Command | jq '@html' |
|---|---|
| Input | "This works if x < y" |
| Output | "This works if x &lt; y" |
| Run |   |

| Command | jq '@sh "echo \(.)"' |
|---|---|
| Input | "O'Hara's Ale" |
| Output | "echo 'O'\\''Hara'\\''s Ale'" |
| Run |   |

| Command | jq '@base64' |
|---|---|
| Input | "This is a message" |
| Output | "VGhpcyBpcyBhIG1lc3NhZ2U=" |
| Run |   |

| Command | jq '@base64d' |
|---|---|
| Input | "VGhpcyBpcyBhIG1lc3NhZ2U=" |
| Output | "This is a message" |
| Run |   |

### Dates

jq provides some basic date handling functionality, with some high-level and low-level builtins. In all cases these builtins deal exclusively with time in UTC.

The `fromdateiso8601` builtin parses datetimes in the ISO 8601 format to a number of seconds since the Unix epoch (1970-01-01T00:00:00Z). The `todateiso8601` builtin does the inverse.

The `fromdate` builtin parses datetime strings. Currently `fromdate` only supports ISO 8601 datetime strings, but in the future it will attempt to parse datetime strings in more formats.

The `todate` builtin is an alias for `todateiso8601`.

The `now` builtin outputs the current time, in seconds since the Unix epoch.

Low-level jq interfaces to the C-library time functions are also provided: `strptime`, `strftime`, `strflocaltime`, `mktime`, `gmtime`, and `localtime`. Refer to your host operating system's documentation for the format strings used by `strptime` and `strftime`. Note: these are not necessarily stable interfaces in jq, particularly as to their localization functionality.

The `gmtime` builtin consumes a number of seconds since the Unix epoch and outputs a "broken down time" representation of Greenwich Mean Time as an array of numbers representing (in this order): the year, the month (zero-based), the day of the month (one-based), the hour of the day, the minute of the hour, the second of the minute, the day of the week, and the day of the year -- all one-based unless otherwise stated. The day of the week number may be wrong on some systems for dates before March 1st 1900, or after December 31 2099.

The `localtime` builtin works like the `gmtime` builtin, but using the local timezone setting.

The `mktime` builtin consumes "broken down time" representations of time output by `gmtime` and `strptime`.

The `strptime(fmt)` builtin parses input strings matching the `fmt` argument. The output is in the "broken down time" representation consumed by `mktime` and output by `gmtime`.

The `strftime(fmt)` builtin formats a time (GMT) with the given format. The `strflocaltime` does the same, but using the local timezone setting.

The format strings for `strptime` and `strftime` are described in typical C library documentation. The format string for ISO 8601 datetime is `"%Y-%m-%dT%H:%M:%SZ"`.

jq may not support some or all of this date functionality on some systems. In particular, the `%u` and `%j` specifiers for `strptime(fmt)` are not supported on macOS.

| Command | jq 'fromdate' |
|---|---|
| Input | "2015-03-05T23:51:47Z" |
| Output | 1425599507 |
| Run |   |

| Command | jq 'strptime("%Y-%m-%dT%H:%M:%SZ")' |
|---|---|
| Input | "2015-03-05T23:51:47Z" |
| Output | [2015,2,5,23,51,47,4,63] |
| Run |   |

| Command | jq 'strptime("%Y-%m-%dT%H:%M:%SZ")\|mktime' |
|---|---|
| Input | "2015-03-05T23:51:47Z" |
| Output | 1425599507 |
| Run |   |

### SQL-Style Operators

jq provides a few SQL-style operators.

- `INDEX(stream; index_expression)`:

This builtin produces an object whose keys are computed by the given index expression applied to each value from the given stream.

- `JOIN($idx; stream; idx_expr; join_expr)`:

This builtin joins the values from the given stream to the given index. The index's keys are computed by applying the given index expression to each value from the given stream. An array of the value in the stream and the corresponding value from the index is fed to the given join expression to produce each result.

- `JOIN($idx; stream; idx_expr)`:

Same as `JOIN($idx; stream; idx_expr; .)`.

- `JOIN($idx; idx_expr)`:

This builtin joins the input `.` to the given index, applying the given index expression to `.` to compute the index key. The join operation is as described above.

- `IN(s)`:

This builtin outputs `true` if `.` appears in the given stream, otherwise it outputs `false`.

- `IN(source; s)`:

This builtin outputs `true` if any value in the source stream appears in the second stream, otherwise it outputs `false`.

### `builtins`

Returns a list of all builtin functions in the format `name/arity`. Since functions with the same name but different arities are considered separate functions, `all/0`, `all/1`, and `all/2` would all be present in the list.
