---
title: "jq 1.8 Manual (part 3/4)"
source: https://jqlang.github.io/jq/manual/
domain: jq-json
license: CC-BY-SA-4.0
tags: jq json, json processor, command-line json, json filter
fetched: 2026-07-02
part: 3/4
---

## Conditionals and Comparisons

### `==`, `!=`

The expression 'a == b' will produce 'true' if the results of evaluating a and b are equal (that is, if they represent equivalent JSON values) and 'false' otherwise. In particular, strings are never considered equal to numbers. In checking for the equality of JSON objects, the ordering of keys is irrelevant. If you're coming from JavaScript, please note that jq's `==` is like JavaScript's `===`, the "strict equality" operator.

!= is "not equal", and 'a != b' returns the opposite value of 'a == b'

| Command | jq '. == false' |
|---|---|
| Input | null |
| Output | false |
| Run |   |

| Command | jq '. == {"b": {"d": (4 + 1e-20), "c": 3}, "a":1}' |
|---|---|
| Input | {"a":1, "b": {"c": 3, "d": 4}} |
| Output | true |
| Run |   |

| Command | jq '.[] == 1' |
|---|---|
| Input | [1, 1.0, "1", "banana"] |
| Output | true |
|   | true |
|   | false |
|   | false |
| Run |   |

### if-then-else-end

`if A then B else C end` will act the same as `B` if `A` produces a value other than false or null, but act the same as `C` otherwise.

`if A then B end` is the same as `if A then B else . end`. That is, the `else` branch is optional, and if absent is the same as `.`. This also applies to `elif` with absent ending `else` branch.

Checking for false or null is a simpler notion of "truthiness" than is found in JavaScript or Python, but it means that you'll sometimes have to be more explicit about the condition you want. You can't test whether, e.g. a string is empty using `if .name then A else B end`; you'll need something like `if .name == "" then A else B end` instead.

If the condition `A` produces multiple results, then `B` is evaluated once for each result that is not false or null, and `C` is evaluated once for each false or null.

More cases can be added to an if using `elif A then B` syntax.

| Command | jq 'if . == 0 then "zero" elif . == 1 then "one" else "many" end' |
|---|---|
| Input | 2 |
| Output | "many" |
| Run |   |

### `>`, `>=`, `<=`, `<`

The comparison operators `>`, `>=`, `<=`, `<` return whether their left argument is greater than, greater than or equal to, less than or equal to or less than their right argument (respectively).

The ordering is the same as that described for `sort`, above.

| Command | jq '. < 5' |
|---|---|
| Input | 2 |
| Output | true |
| Run |   |

### `and`, `or`, `not`

jq supports the normal Boolean operators `and`, `or`, `not`. They have the same standard of truth as if expressions - `false` and `null` are considered "false values", and anything else is a "true value".

If an operand of one of these operators produces multiple results, the operator itself will produce a result for each input.

`not` is in fact a builtin function rather than an operator, so it is called as a filter to which things can be piped rather than with special syntax, as in `.foo and .bar | not`.

These three only produce the values `true` and `false`, and so are only useful for genuine Boolean operations, rather than the common Perl/Python/Ruby idiom of "value_that_may_be_null or default". If you want to use this form of "or", picking between two values rather than evaluating a condition, see the `//` operator below.

| Command | jq '42 and "a string"' |
|---|---|
| Input | null |
| Output | true |
| Run |   |

| Command | jq '(true, false) or false' |
|---|---|
| Input | null |
| Output | true |
|   | false |
| Run |   |

| Command | jq '(true, true) and (true, false)' |
|---|---|
| Input | null |
| Output | true |
|   | false |
|   | true |
|   | false |
| Run |   |

| Command | jq '[true, false \| not]' |
|---|---|
| Input | null |
| Output | [false, true] |
| Run |   |

### Alternative operator: `//`

The `//` operator produces all the values of its left-hand side that are neither `false` nor `null`. If the left-hand side produces no values other than `false` or `null`, then `//` produces all the values of its right-hand side.

A filter of the form `a // b` produces all the results of `a` that are not `false` or `null`. If `a` produces no results, or no results other than `false` or `null`, then `a // b` produces the results of `b`.

This is useful for providing defaults: `.foo // 1` will evaluate to `1` if there's no `.foo` element in the input. It's similar to how `or` is sometimes used in Python (jq's `or` operator is reserved for strictly Boolean operations).

Note: `some_generator // defaults_here` is not the same as `some_generator | . // defaults_here`. The latter will produce default values for all non-`false`, non-`null` values of the left-hand side, while the former will not. Precedence rules can make this confusing. For example, in `false, 1 // 2` the left-hand side of `//` is `1`, not `false, 1` -- `false, 1 // 2` parses the same way as `false, (1 // 2)`. In `(false, null, 1) | . // 42` the left-hand side of `//` is `.`, which always produces just one value, while in `(false, null, 1) // 42` the left-hand side is a generator of three values, and since it produces a value other `false` and `null`, the default `42` is not produced.

| Command | jq 'empty // 42' |
|---|---|
| Input | null |
| Output | 42 |
| Run |   |

| Command | jq '.foo // 42' |
|---|---|
| Input | {"foo": 19} |
| Output | 19 |
| Run |   |

| Command | jq '.foo // 42' |
|---|---|
| Input | {} |
| Output | 42 |
| Run |   |

| Command | jq '(false, null, 1) // 42' |
|---|---|
| Input | null |
| Output | 1 |
| Run |   |

| Command | jq '(false, null, 1) \| . // 42' |
|---|---|
| Input | null |
| Output | 42 |
|   | 42 |
|   | 1 |
| Run |   |

### try-catch

Errors can be caught by using `try EXP catch EXP`. The first expression is executed, and if it fails then the second is executed with the error message. The output of the handler, if any, is output as if it had been the output of the expression to try.

The `try EXP` form uses `empty` as the exception handler.

| Command | jq 'try .a catch ". is not an object"' |
|---|---|
| Input | true |
| Output | ". is not an object" |
| Run |   |

| Command | jq '[.[]\|try .a]' |
|---|---|
| Input | [{}, true, {"a":1}] |
| Output | [null, 1] |
| Run |   |

| Command | jq 'try error("some exception") catch .' |
|---|---|
| Input | true |
| Output | "some exception" |
| Run |   |

### Breaking out of control structures

A convenient use of try/catch is to break out of control structures like `reduce`, `foreach`, `while`, and so on.

For example:

```
# Repeat an expression until it raises "break" as an
# error, then stop repeating without re-raising the error.
# But if the error caught is not "break" then re-raise it.
try repeat(exp) catch if .=="break" then empty else error
```

jq has a syntax for named lexical labels to "break" or "go (back) to":

```
label $out | ... break $out ...
```

The `break $label_name` expression will cause the program to act as though the nearest (to the left) `label $label_name` produced `empty`.

The relationship between the `break` and corresponding `label` is lexical: the label has to be "visible" from the break.

To break out of a `reduce`, for example:

```
label $out | reduce .[] as $item (null; if .==false then break $out else ... end)
```

The following jq program produces a syntax error:

```
break $out
```

because no label `$out` is visible.

### Error Suppression / Optional Operator: `?`

The `?` operator, used as `EXP?`, is shorthand for `try EXP`.

| Command | jq '[.[] \| .a?]' |
|---|---|
| Input | [{}, true, {"a":1}] |
| Output | [null, 1] |
| Run |   |

| Command | jq '[.[] \| tonumber?]' |
|---|---|
| Input | ["1", "invalid", "3", 4] |
| Output | [1, 3, 4] |
| Run |   |


## Regular expressions

jq uses the Oniguruma regular expression library, as do PHP, TextMate, Sublime Text, etc, so the description here will focus on jq specifics.

Oniguruma supports several flavors of regular expression, so it is important to know that jq uses the "Perl NG" (Perl with named groups) flavor.

The jq regex filters are defined so that they can be used using one of these patterns:

```
STRING | FILTER(REGEX)
STRING | FILTER(REGEX; FLAGS)
STRING | FILTER([REGEX])
STRING | FILTER([REGEX, FLAGS])
```

where:

- STRING, REGEX, and FLAGS are jq strings and subject to jq string interpolation;
- REGEX, after string interpolation, should be a valid regular expression;
- FILTER is one of `test`, `match`, or `capture`, as described below.

Since REGEX must evaluate to a JSON string, some characters that are needed to form a regular expression must be escaped. For example, the regular expression `\s` signifying a whitespace character would be written as `"\\s"`.

FLAGS is a string consisting of one of more of the supported flags:

- `g` - Global search (find all matches, not just the first)
- `i` - Case insensitive search
- `m` - Multi line mode (`.` will match newlines)
- `n` - Ignore empty matches
- `p` - Both s and m modes are enabled
- `s` - Single line mode (`^` -> `\A`, `$` -> `\Z`)
- `l` - Find longest possible matches
- `x` - Extended regex format (ignore whitespace and comments)

To match a whitespace with the `x` flag, use `\s`, e.g.

```
jq -n '"a b" | test("a\\sb"; "x")'
```

Note that certain flags may also be specified within REGEX, e.g.

```
jq -n '("test", "TEst", "teST", "TEST") | test("(?i)te(?-i)st")'
```

evaluates to: `true`, `true`, `false`, `false`.

### `test(val)`, `test(regex; flags)`

Like `match`, but does not return match objects, only `true` or `false` for whether or not the regex matches the input.

| Command | jq 'test("foo")' |
|---|---|
| Input | "foo" |
| Output | true |
| Run |   |

| Command | jq '.[] \| test("a b c # spaces are ignored"; "ix")' |
|---|---|
| Input | ["xabcd", "ABC"] |
| Output | true |
|   | true |
| Run |   |

### `match(val)`, `match(regex; flags)`

**match** outputs an object for each match it finds. Matches have the following fields:

- `offset` - offset in UTF-8 codepoints from the beginning of the input
- `length` - length in UTF-8 codepoints of the match
- `string` - the string that it matched
- `captures` - an array of objects representing capturing groups.

Capturing group objects have the following fields:

- `offset` - offset in UTF-8 codepoints from the beginning of the input
- `length` - length in UTF-8 codepoints of this capturing group
- `string` - the string that was captured
- `name` - the name of the capturing group (or `null` if it was unnamed)

Capturing groups that did not match anything return an offset of -1

| Command | jq 'match("(abc)+"; "g")' |
|---|---|
| Input | "abc abc" |
| Output | {"offset": 0, "length": 3, "string": "abc", "captures": [{"offset": 0, "length": 3, "string": "abc", "name": null}]} |
|   | {"offset": 4, "length": 3, "string": "abc", "captures": [{"offset": 4, "length": 3, "string": "abc", "name": null}]} |
| Run |   |

| Command | jq 'match("foo")' |
|---|---|
| Input | "foo bar foo" |
| Output | {"offset": 0, "length": 3, "string": "foo", "captures": []} |
| Run |   |

| Command | jq 'match(["foo", "ig"])' |
|---|---|
| Input | "foo bar FOO" |
| Output | {"offset": 0, "length": 3, "string": "foo", "captures": []} |
|   | {"offset": 8, "length": 3, "string": "FOO", "captures": []} |
| Run |   |

| Command | jq 'match("foo (?<bar123>bar)? foo"; "ig")' |
|---|---|
| Input | "foo bar foo foo foo" |
| Output | {"offset": 0, "length": 11, "string": "foo bar foo", "captures": [{"offset": 4, "length": 3, "string": "bar", "name": "bar123"}]} |
|   | {"offset": 12, "length": 8, "string": "foo foo", "captures": [{"offset": -1, "length": 0, "string": null, "name": "bar123"}]} |
| Run |   |

| Command | jq '[ match("."; "g")] \| length' |
|---|---|
| Input | "abc" |
| Output | 3 |
| Run |   |

### `capture(val)`, `capture(regex; flags)`

Collects the named captures in a JSON object, with the name of each capture as the key, and the matched string as the corresponding value.

| Command | jq 'capture("(?<a>[a-z]+)-(?<n>[0-9]+)")' |
|---|---|
| Input | "xyzzy-14" |
| Output | { "a": "xyzzy", "n": "14" } |
| Run |   |

### `scan(regex)`, `scan(regex; flags)`

Emit a stream of the non-overlapping substrings of the input that match the regex in accordance with the flags, if any have been specified. If there is no match, the stream is empty. To capture all the matches for each input string, use the idiom `[ expr ]`, e.g. `[ scan(regex) ]`. If the regex contains capturing groups, the filter emits a stream of arrays, each of which contains the captured strings.

| Command | jq 'scan("c")' |
|---|---|
| Input | "abcdefabc" |
| Output | "c" |
|   | "c" |
| Run |   |

| Command | jq 'scan("(a+)(b+)")' |
|---|---|
| Input | "abaabbaaabbb" |
| Output | ["a","b"] |
|   | ["aa","bb"] |
|   | ["aaa","bbb"] |
| Run |   |

### `split(regex; flags)`

Splits an input string on each regex match.

For backwards compatibility, when called with a single argument, `split` splits on a string, not a regex.

| Command | jq 'split(", *"; null)' |
|---|---|
| Input | "ab,cd, ef" |
| Output | ["ab","cd","ef"] |
| Run |   |

### `splits(regex)`, `splits(regex; flags)`

These provide the same results as their `split` counterparts, but as a stream instead of an array.

| Command | jq 'splits(", *")' |
|---|---|
| Input | "ab,cd, ef, gh" |
| Output | "ab" |
|   | "cd" |
|   | "ef" |
|   | "gh" |
| Run |   |

| Command | jq 'splits(",? *"; "n")' |
|---|---|
| Input | "ab,cd ef, gh" |
| Output | "ab" |
|   | "cd" |
|   | "ef" |
|   | "gh" |
| Run |   |

### `sub(regex; tostring)`, `sub(regex; tostring; flags)`

Emit the string obtained by replacing the first match of regex in the input string with `tostring`, after interpolation. `tostring` should be a jq string or a stream of such strings, each of which may contain references to named captures. The named captures are, in effect, presented as a JSON object (as constructed by `capture`) to `tostring`, so a reference to a captured variable named "x" would take the form: `"\(.x)"`.

| Command | jq 'sub("[^a-z]*(?<x>[a-z]+)"; "Z\(.x)"; "g")' |
|---|---|
| Input | "123abc456def" |
| Output | "ZabcZdef" |
| Run |   |

| Command | jq '[sub("(?<a>.)"; "\(.a\|ascii_upcase)", "\(.a\|ascii_downcase)")]' |
|---|---|
| Input | "aB" |
| Output | ["AB","aB"] |
| Run |   |

### `gsub(regex; tostring)`, `gsub(regex; tostring; flags)`

`gsub` is like `sub` but all the non-overlapping occurrences of the regex are replaced by `tostring`, after interpolation. If the second argument is a stream of jq strings, then `gsub` will produce a corresponding stream of JSON strings.

| Command | jq 'gsub("(?<x>.)[^a]*"; "+\(.x)-")' |
|---|---|
| Input | "Abcabc" |
| Output | "+A-+a-" |
| Run |   |

| Command | jq '[gsub("p"; "a", "b")]' |
|---|---|
| Input | "p" |
| Output | ["a","b"] |
| Run |   |


## Advanced features

Variables are an absolute necessity in most programming languages, but they're relegated to an "advanced feature" in jq.

In most languages, variables are the only means of passing around data. If you calculate a value, and you want to use it more than once, you'll need to store it in a variable. To pass a value to another part of the program, you'll need that part of the program to define a variable (as a function parameter, object member, or whatever) in which to place the data.

It is also possible to define functions in jq, although this is is a feature whose biggest use is defining jq's standard library (many jq functions such as `map` and `select` are in fact written in jq).

jq has reduction operators, which are very powerful but a bit tricky. Again, these are mostly used internally, to define some useful bits of jq's standard library.

It may not be obvious at first, but jq is all about generators (yes, as often found in other languages). Some utilities are provided to help deal with generators.

Some minimal I/O support (besides reading JSON from standard input, and writing JSON to standard output) is available.

Finally, there is a module/library system.

### Variable / Symbolic Binding Operator: `... as $identifier | ...`

In jq, all filters have an input and an output, so manual plumbing is not necessary to pass a value from one part of a program to the next. Many expressions, for instance `a + b`, pass their input to two distinct subexpressions (here `a` and `b` are both passed the same input), so variables aren't usually necessary in order to use a value twice.

For instance, calculating the average value of an array of numbers requires a few variables in most languages - at least one to hold the array, perhaps one for each element or for a loop counter. In jq, it's simply `add / length` - the `add` expression is given the array and produces its sum, and the `length` expression is given the array and produces its length.

So, there's generally a cleaner way to solve most problems in jq than defining variables. Still, sometimes they do make things easier, so jq lets you define variables using `expression as $variable`. All variable names start with `$`. Here's a slightly uglier version of the array-averaging example:

```
length as $array_length | add / $array_length
```

We'll need a more complicated problem to find a situation where using variables actually makes our lives easier.

Suppose we have an array of blog posts, with "author" and "title" fields, and another object which is used to map author usernames to real names. Our input looks like:

```
{"posts": [{"title": "First post", "author": "anon"},
           {"title": "A well-written article", "author": "person1"}],
 "realnames": {"anon": "Anonymous Coward",
               "person1": "Person McPherson"}}
```

We want to produce the posts with the author field containing a real name, as in:

```
{"title": "First post", "author": "Anonymous Coward"}
{"title": "A well-written article", "author": "Person McPherson"}
```

We use a variable, `$names`, to store the realnames object, so that we can refer to it later when looking up author usernames:

```
.realnames as $names | .posts[] | {title, author: $names[.author]}
```

The expression `exp as $x | ...` means: for each value of expression `exp`, run the rest of the pipeline with the entire original input, and with `$x` set to that value. Thus `as` functions as something of a foreach loop.

Just as `{foo}` is a handy way of writing `{foo: .foo}`, so `{$foo}` is a handy way of writing `{foo: $foo}`.

Multiple variables may be declared using a single `as` expression by providing a pattern that matches the structure of the input (this is known as "destructuring"):

```
. as {realnames: $names, posts: [$first, $second]} | ...
```

The variable declarations in array patterns (e.g., `. as [$first, $second]`) bind to the elements of the array in from the element at index zero on up, in order. When there is no value at the index for an array pattern element, `null` is bound to that variable.

Variables are scoped over the rest of the expression that defines them, so

```
.realnames as $names | (.posts[] | {title, author: $names[.author]})
```

will work, but

```
(.realnames as $names | .posts[]) | {title, author: $names[.author]}
```

won't.

For programming language theorists, it's more accurate to say that jq variables are lexically-scoped bindings. In particular there's no way to change the value of a binding; one can only setup a new binding with the same name, but which will not be visible where the old one was.

| Command | jq '.bar as $x \| .foo \| . + $x' |
|---|---|
| Input | {"foo":10, "bar":200} |
| Output | 210 |
| Run |   |

| Command | jq '. as $i\|[(.*2\|. as $i\| $i), $i]' |
|---|---|
| Input | 5 |
| Output | [10,5] |
| Run |   |

| Command | jq '. as [$a, $b, {c: $c}] \| $a + $b + $c' |
|---|---|
| Input | [2, 3, {"c": 4, "d": 5}] |
| Output | 9 |
| Run |   |

| Command | jq '.[] as [$a, $b] \| {a: $a, b: $b}' |
|---|---|
| Input | [[0], [0, 1], [2, 1, 0]] |
| Output | {"a":0,"b":null} |
|   | {"a":0,"b":1} |
|   | {"a":2,"b":1} |
| Run |   |

### Destructuring Alternative Operator: `?//`

The destructuring alternative operator provides a concise mechanism for destructuring an input that can take one of several forms.

Suppose we have an API that returns a list of resources and events associated with them, and we want to get the user_id and timestamp of the first event for each resource. The API (having been clumsily converted from XML) will only wrap the events in an array if the resource has multiple events:

```
{"resources": [{"id": 1, "kind": "widget", "events": {"action": "create", "user_id": 1, "ts": 13}},
               {"id": 2, "kind": "widget", "events": [{"action": "create", "user_id": 1, "ts": 14}, {"action": "destroy", "user_id": 1, "ts": 15}]}]}
```

We can use the destructuring alternative operator to handle this structural change simply:

```
.resources[] as {$id, $kind, events: {$user_id, $ts}} ?// {$id, $kind, events: [{$user_id, $ts}]} | {$user_id, $kind, $id, $ts}
```

Or, if we aren't sure if the input is an array of values or an object:

```
.[] as [$id, $kind, $user_id, $ts] ?// {$id, $kind, $user_id, $ts} | ...
```

Each alternative need not define all of the same variables, but all named variables will be available to the subsequent expression. Variables not matched in the alternative that succeeded will be `null`:

```
.resources[] as {$id, $kind, events: {$user_id, $ts}} ?// {$id, $kind, events: [{$first_user_id, $first_ts}]} | {$user_id, $first_user_id, $kind, $id, $ts, $first_ts}
```

Additionally, if the subsequent expression returns an error, the alternative operator will attempt to try the next binding. Errors that occur during the final alternative are passed through.

```
[[3]] | .[] as [$a] ?// [$b] | if $a != null then error("err: \($a)") else {$a,$b} end
```

| Command | jq '.[] as {$a, $b, c: {$d, $e}} ?// {$a, $b, c: [{$d, $e}]} \| {$a, $b, $d, $e}' |
|---|---|
| Input | [{"a": 1, "b": 2, "c": {"d": 3, "e": 4}}, {"a": 1, "b": 2, "c": [{"d": 3, "e": 4}]}] |
| Output | {"a":1,"b":2,"d":3,"e":4} |
|   | {"a":1,"b":2,"d":3,"e":4} |
| Run |   |

| Command | jq '.[] as {$a, $b, c: {$d}} ?// {$a, $b, c: [{$e}]} \| {$a, $b, $d, $e}' |
|---|---|
| Input | [{"a": 1, "b": 2, "c": {"d": 3, "e": 4}}, {"a": 1, "b": 2, "c": [{"d": 3, "e": 4}]}] |
| Output | {"a":1,"b":2,"d":3,"e":null} |
|   | {"a":1,"b":2,"d":null,"e":4} |
| Run |   |

| Command | jq '.[] as [$a] ?// [$b] \| if $a != null then error("err: \($a)") else {$a,$b} end' |
|---|---|
| Input | [[3]] |
| Output | {"a":null,"b":3} |
| Run |   |

### Defining Functions

You can give a filter a name using "def" syntax:

```
def increment: . + 1;
```

From then on, `increment` is usable as a filter just like a builtin function (in fact, this is how many of the builtins are defined). A function may take arguments:

```
def map(f): [.[] | f];
```

Arguments are passed as *filters* (functions with no arguments), *not* as values. The same argument may be referenced multiple times with different inputs (here `f` is run for each element of the input array). Arguments to a function work more like callbacks than like value arguments. This is important to understand. Consider:

```
def foo(f): f|f;
5|foo(.*2)
```

The result will be 20 because `f` is `.*2`, and during the first invocation of `f` `.` will be 5, and the second time it will be 10 (5 * 2), so the result will be 20. Function arguments are filters, and filters expect an input when invoked.

If you want the value-argument behaviour for defining simple functions, you can just use a variable:

```
def addvalue(f): f as $f | map(. + $f);
```

Or use the short-hand:

```
def addvalue($f): ...;
```

With either definition, `addvalue(.foo)` will add the current input's `.foo` field to each element of the array. Do note that calling `addvalue(.[])` will cause the `map(. + $f)` part to be evaluated once per value in the value of `.` at the call site.

Multiple definitions using the same function name are allowed. Each re-definition replaces the previous one for the same number of function arguments, but only for references from functions (or main program) subsequent to the re-definition. See also the section below on scoping.

| Command | jq 'def addvalue(f): . + [f]; map(addvalue(.[0]))' |
|---|---|
| Input | [[1,2],[10,20]] |
| Output | [[1,2,1], [10,20,10]] |
| Run |   |

| Command | jq 'def addvalue(f): f as $x \| map(. + $x); addvalue(.[0])' |
|---|---|
| Input | [[1,2],[10,20]] |
| Output | [[1,2,1,2], [10,20,1,2]] |
| Run |   |

### Scoping

There are two types of symbols in jq: value bindings (a.k.a., "variables"), and functions. Both are scoped lexically, with expressions being able to refer only to symbols that have been defined "to the left" of them. The only exception to this rule is that functions can refer to themselves so as to be able to create recursive functions.

For example, in the following expression there is a binding which is visible "to the right" of it, `... | .*3 as $times_three | [. + $times_three] | ...`, but not "to the left". Consider this expression now, `... | (.*3 as $times_three | [. + $times_three]) | ...`: here the binding `$times_three` is *not* visible past the closing parenthesis.

### `isempty(exp)`

Returns true if `exp` produces no outputs, false otherwise.

| Command | jq 'isempty(empty)' |
|---|---|
| Input | null |
| Output | true |
| Run |   |

| Command | jq 'isempty(.[])' |
|---|---|
| Input | [] |
| Output | true |
| Run |   |

| Command | jq 'isempty(.[])' |
|---|---|
| Input | [1,2,3] |
| Output | false |
| Run |   |

### `limit(n; expr)`

The `limit` function extracts up to `n` outputs from `expr`.

| Command | jq '[limit(3; .[])]' |
|---|---|
| Input | [0,1,2,3,4,5,6,7,8,9] |
| Output | [0,1,2] |
| Run |   |

### `first(expr)`, `last(expr)`, `nth(n; expr)`

The `first(expr)` and `last(expr)` functions extract the first and last values from `expr`, respectively.

The `nth(n; expr)` function extracts the nth value output by `expr`. Note that `nth(n; expr)` doesn't support negative values of `n`.

| Command | jq '[first(range(.)), last(range(.)), nth(5; range(.))]' |
|---|---|
| Input | 10 |
| Output | [0,9,5] |
| Run |   |

| Command | jq '[first(empty), last(empty), nth(5; empty)]' |
|---|---|
| Input | null |
| Output | [] |
| Run |   |

### `first`, `last`, `nth(n)`

The `first` and `last` functions extract the first and last values from any array at `.`.

The `nth(n)` function extracts the nth value of any array at `.`.

| Command | jq '[range(.)]\|[first, last, nth(5)]' |
|---|---|
| Input | 10 |
| Output | [0,9,5] |
| Run |   |

### `reduce`

The `reduce` syntax allows you to combine all of the results of an expression by accumulating them into a single answer. The form is `reduce EXP as $var (INIT; UPDATE)`. As an example, we'll pass `[1,2,3]` to this expression:

```
reduce .[] as $item (0; . + $item)
```

For each result that `.[]` produces, `. + $item` is run to accumulate a running total, starting from 0 as the input value. In this example, `.[]` produces the results `1`, `2`, and `3`, so the effect is similar to running something like this:

```
0 | 1 as $item | . + $item |
    2 as $item | . + $item |
    3 as $item | . + $item
```

| Command | jq 'reduce .[] as $item (0; . + $item)' |
|---|---|
| Input | [1,2,3,4,5] |
| Output | 15 |
| Run |   |

| Command | jq 'reduce .[] as [$i,$j] (0; . + $i * $j)' |
|---|---|
| Input | [[1,2],[3,4],[5,6]] |
| Output | 44 |
| Run |   |

| Command | jq 'reduce .[] as {$x,$y} (null; .x += $x \| .y += [$y])' |
|---|---|
| Input | [{"x":"a","y":1},{"x":"b","y":2},{"x":"c","y":3}] |
| Output | {"x":"abc","y":[1,2,3]} |
| Run |   |

### `foreach`

The `foreach` syntax is similar to `reduce`, but intended to allow the construction of `limit` and reducers that produce intermediate results.

The form is `foreach EXP as $var (INIT; UPDATE; EXTRACT)`. As an example, we'll pass `[1,2,3]` to this expression:

```
foreach .[] as $item (0; . + $item; [$item, . * 2])
```

Like the `reduce` syntax, `. + $item` is run for each result that `.[]` produces, but `[$item, . * 2]` is run for each intermediate values. In this example, since the intermediate values are `1`, `3`, and `6`, the `foreach` expression produces `[1,2]`, `[2,6]`, and `[3,12]`. So the effect is similar to running something like this:

```
0 | 1 as $item | . + $item | [$item, . * 2],
    2 as $item | . + $item | [$item, . * 2],
    3 as $item | . + $item | [$item, . * 2]
```

When `EXTRACT` is omitted, the identity filter is used. That is, it outputs the intermediate values as they are.

| Command | jq 'foreach .[] as $item (0; . + $item)' |
|---|---|
| Input | [1,2,3,4,5] |
| Output | 1 |
|   | 3 |
|   | 6 |
|   | 10 |
|   | 15 |
| Run |   |

| Command | jq 'foreach .[] as $item (0; . + $item; [$item, . * 2])' |
|---|---|
| Input | [1,2,3,4,5] |
| Output | [1,2] |
|   | [2,6] |
|   | [3,12] |
|   | [4,20] |
|   | [5,30] |
| Run |   |

| Command | jq 'foreach .[] as $item (0; . + 1; {index: ., $item})' |
|---|---|
| Input | ["foo", "bar", "baz"] |
| Output | {"index":1,"item":"foo"} |
|   | {"index":2,"item":"bar"} |
|   | {"index":3,"item":"baz"} |
| Run |   |

### Recursion

As described above, `recurse` uses recursion, and any jq function can be recursive. The `while` builtin is also implemented in terms of recursion.

Tail calls are optimized whenever the expression to the left of the recursive call outputs its last value. In practice this means that the expression to the left of the recursive call should not produce more than one output for each input.

For example:

```
def recurse(f): def r: ., (f | select(. != null) | r); r;

def while(cond; update):
  def _while:
    if cond then ., (update | _while) else empty end;
  _while;

def repeat(exp):
  def _repeat:
    exp, _repeat;
  _repeat;
```

### Generators and iterators

Some jq operators and functions are actually generators in that they can produce zero, one, or more values for each input, just as one might expect in other programming languages that have generators. For example, `.[]` generates all the values in its input (which must be an array or an object), `range(0; 10)` generates the integers between 0 and 10, and so on.

Even the comma operator is a generator, generating first the values generated by the expression to the left of the comma, then the values generated by the expression on the right of the comma.

The `empty` builtin is the generator that produces zero outputs. The `empty` builtin backtracks to the preceding generator expression.

All jq functions can be generators just by using builtin generators. It is also possible to construct new generators using only recursion and the comma operator. If recursive calls are "in tail position" then the generator will be efficient. In the example below the recursive call by `_range` to itself is in tail position. The example shows off three advanced topics: tail recursion, generator construction, and sub-functions.

| Command | jq 'def range(init; upto; by): def _range: if (by > 0 and . < upto) or (by < 0 and . > upto) then ., ((.+by)\|_range) else empty end; if init == upto then empty elif by == 0 then init else init\|_range end; range(0; 10; 3)' |
|---|---|
| Input | null |
| Output | 0 |
|   | 3 |
|   | 6 |
|   | 9 |
| Run |   |

| Command | jq 'def while(cond; update): def _while: if cond then ., (update \| _while) else empty end; _while; [while(.<100; .*2)]' |
|---|---|
| Input | 1 |
| Output | [1,2,4,8,16,32,64] |
| Run |   |


## Math

jq currently only has IEEE754 double-precision (64-bit) floating point number support.

Besides simple arithmetic operators such as `+`, jq also has most standard math functions from the C math library. C math functions that take a single input argument (e.g., `sin()`) are available as zero-argument jq functions. C math functions that take two input arguments (e.g., `pow()`) are available as two-argument jq functions that ignore `.`. C math functions that take three input arguments are available as three-argument jq functions that ignore `.`.

Availability of standard math functions depends on the availability of the corresponding math functions in your operating system and C math library. Unavailable math functions will be defined but will raise an error.

One-input C math functions: `acos` `acosh` `asin` `asinh` `atan` `atanh` `cbrt` `ceil` `cos` `cosh` `erf` `erfc` `exp` `exp10` `exp2` `expm1` `fabs` `floor` `gamma` `j0` `j1` `lgamma` `log` `log10` `log1p` `log2` `logb` `nearbyint` `rint` `round` `significand` `sin` `sinh` `sqrt` `tan` `tanh` `tgamma` `trunc` `y0` `y1`.

Two-input C math functions: `atan2` `copysign` `drem` `fdim` `fmax` `fmin` `fmod` `frexp` `hypot` `jn` `ldexp` `modf` `nextafter` `nexttoward` `pow` `remainder` `scalb` `scalbln` `yn`.

Three-input C math functions: `fma`.

See your system's manual for more information on each of these.


## I/O

At this time jq has minimal support for I/O, mostly in the form of control over when inputs are read. Two builtins functions are provided for this, `input` and `inputs`, that read from the same sources (e.g., `stdin`, files named on the command-line) as jq itself. These two builtins, and jq's own reading actions, can be interleaved with each other. They are commonly used in combination with the null input option `-n` to prevent one input from being read implicitly.

Two builtins provide minimal output capabilities, `debug`, and `stderr`. (Recall that a jq program's output values are always output as JSON texts on `stdout`.) The `debug` builtin can have application-specific behavior, such as for executables that use the libjq C API but aren't the jq executable itself. The `stderr` builtin outputs its input in raw mode to stderr with no additional decoration, not even a newline.

Most jq builtins are referentially transparent, and yield constant and repeatable value streams when applied to constant inputs. This is not true of I/O builtins.

### `input`

Outputs one new input.

Note that when using `input` it is generally necessary to invoke jq with the `-n` command-line option, otherwise the first entity will be lost.

```
echo 1 2 3 4 | jq '[., input]' # [1,2] [3,4]
```

### `inputs`

Outputs all remaining inputs, one by one.

This is primarily useful for reductions over a program's inputs. Note that when using `inputs` it is generally necessary to invoke jq with the `-n` command-line option, otherwise the first entity will be lost.

```
echo 1 2 3 | jq -n 'reduce inputs as $i (0; . + $i)' # 6
```

### `debug`, `debug(msgs)`

These two filters are like `.` but have as a side-effect the production of one or more messages on stderr.

The message produced by the `debug` filter has the form

```
["DEBUG:",<input-value>]
```

where `<input-value>` is a compact rendition of the input value. This format may change in the future.

The `debug(msgs)` filter is defined as `(msgs | debug | empty), .` thus allowing great flexibility in the content of the message, while also allowing multi-line debugging statements to be created.

For example, the expression:

```
1 as $x | 2 | debug("Entering function foo with $x == \($x)", .) | (.+1)
```

would produce the value 3 but with the following two lines being written to stderr:

```
["DEBUG:","Entering function foo with $x == 1"]
["DEBUG:",2]
```

### `stderr`

Prints its input in raw and compact mode to stderr with no additional decoration, not even a newline.

### `input_filename`

Returns the name of the file whose input is currently being filtered. Note that this will not work well unless jq is running in a UTF-8 locale.

### `input_line_number`

Returns the line number of the input currently being filtered.


## Streaming

With the `--stream` option jq can parse input texts in a streaming fashion, allowing jq programs to start processing large JSON texts immediately rather than after the parse completes. If you have a single JSON text that is 1GB in size, streaming it will allow you to process it much more quickly.

However, streaming isn't easy to deal with as the jq program will have `[<path>, <leaf-value>]` (and a few other forms) as inputs.

Several builtins are provided to make handling streams easier.

The examples below use the streamed form of `["a",["b"]]`, which is `[[0],"a"],[[1,0],"b"],[[1,0]],[[1]]`.

Streaming forms include `[<path>, <leaf-value>]` (to indicate any scalar value, empty array, or empty object), and `[<path>]` (to indicate the end of an array or object). Future versions of jq run with `--stream` and `--seq` may output additional forms such as `["error message"]` when an input text fails to parse.

### `truncate_stream(stream_expression)`

Consumes a number as input and truncates the corresponding number of path elements from the left of the outputs of the given streaming expression.

| Command | jq 'truncate_stream([[0],"a"],[[1,0],"b"],[[1,0]],[[1]])' |
|---|---|
| Input | 1 |
| Output | [[0],"b"] |
|   | [[0]] |
| Run |   |

### `fromstream(stream_expression)`

Outputs values corresponding to the stream expression's outputs.

| Command | jq 'fromstream(1\|truncate_stream([[0],"a"],[[1,0],"b"],[[1,0]],[[1]]))' |
|---|---|
| Input | null |
| Output | ["b"] |
| Run |   |

### `tostream`

The `tostream` builtin outputs the streamed form of its input.

| Command | jq '. as $dot\|fromstream($dot\|tostream)\|.==$dot' |
|---|---|
| Input | [0,[1,{"a":1},{"b":2}]] |
| Output | true |
| Run |   |


## Assignment

Assignment works a little differently in jq than in most programming languages. jq doesn't distinguish between references to and copies of something - two objects or arrays are either equal or not equal, without any further notion of being "the same object" or "not the same object".

If an object has two fields which are arrays, `.foo` and `.bar`, and you append something to `.foo`, then `.bar` will not get bigger, even if you've previously set `.bar = .foo`. If you're used to programming in languages like Python, Java, Ruby, JavaScript, etc. then you can think of it as though jq does a full deep copy of every object before it does the assignment (for performance it doesn't actually do that, but that's the general idea).

This means that it's impossible to build circular values in jq (such as an array whose first element is itself). This is quite intentional, and ensures that anything a jq program can produce can be represented in JSON.

All the assignment operators in jq have path expressions on the left-hand side (LHS). The right-hand side (RHS) provides values to set to the paths named by the LHS path expressions.

Values in jq are always immutable. Internally, assignment works by using a reduction to compute new, replacement values for `.` that have had all the desired assignments applied to `.`, then outputting the modified value. This might be made clear by this example: `{a:{b:{c:1}}} | (.a.b|=3), .`. This will output `{"a":{"b":3}}` and `{"a":{"b":{"c":1}}}` because the last sub-expression, `.`, sees the original value, not the modified value.

Most users will want to use modification assignment operators, such as `|=` or `+=`, rather than `=`.

Note that the LHS of assignment operators refers to a value in `.`. Thus `$var.foo = 1` won't work as expected (`$var.foo` is not a valid or useful path expression in `.`); use `$var | .foo = 1` instead.

Note too that `.a,.b=0` does not set `.a` and `.b`, but `(.a,.b)=0` sets both.

### Update-assignment: `|=`

This is the "update" operator `|=`. It takes a filter on the right-hand side and works out the new value for the property of `.` being assigned to by running the old value through this expression. For instance, `(.foo, .bar) |= .+1` will build an object with the `foo` field set to the input's `foo` plus 1, and the `bar` field set to the input's `bar` plus 1.

The left-hand side can be any general path expression; see `path()`.

Note that the left-hand side of `|=` refers to a value in `.`. Thus `$var.foo |= . + 1` won't work as expected (`$var.foo` is not a valid or useful path expression in `.`); use `$var | .foo |= . + 1` instead.

If the right-hand side outputs no values (i.e., `empty`), then the left-hand side path will be deleted, as with `del(path)`.

If the right-hand side outputs multiple values, only the first one will be used (COMPATIBILITY NOTE: in jq 1.5 and earlier releases, it used to be that only the last one was used).

| Command | jq '(..\|select(type=="boolean")) \|= if . then 1 else 0 end' |
|---|---|
| Input | [true,false,[5,true,[true,[false]],false]] |
| Output | [1,0,[5,1,[1,[0]],0]] |
| Run |   |

### Arithmetic update-assignment: `+=`, `-=`, `*=`, `/=`, `%=`, `//=`

jq has a few operators of the form `a op= b`, which are all equivalent to `a |= . op b`. So, `+= 1` can be used to increment values, being the same as `|= . + 1`.

| Command | jq '.foo += 1' |
|---|---|
| Input | {"foo": 42} |
| Output | {"foo": 43} |
| Run |   |

### Plain assignment: `=`

This is the plain assignment operator. Unlike the others, the input to the right-hand side (RHS) is the same as the input to the left-hand side (LHS) rather than the value at the LHS path, and all values output by the RHS will be used (as shown below).

If the RHS of `=` produces multiple values, then for each such value jq will set the paths on the left-hand side to the value and then it will output the modified `.`. For example, `(.a,.b) = range(2)` outputs `{"a":0,"b":0}`, then `{"a":1,"b":1}`. The "update" assignment forms (see above) do not do this.

This example should show the difference between `=` and `|=`:

Provide input `{"a": {"b": 10}, "b": 20}` to the programs

```
.a = .b
```

and

```
.a |= .b
```

The former will set the `a` field of the input to the `b` field of the input, and produce the output `{"a": 20, "b": 20}`. The latter will set the `a` field of the input to the `a` field's `b` field, producing `{"a": 10, "b": 20}`.

| Command | jq '.a = .b' |
|---|---|
| Input | {"a": {"b": 10}, "b": 20} |
| Output | {"a":20,"b":20} |
| Run |   |

| Command | jq '.a \|= .b' |
|---|---|
| Input | {"a": {"b": 10}, "b": 20} |
| Output | {"a":10,"b":20} |
| Run |   |

| Command | jq '(.a, .b) = range(3)' |
|---|---|
| Input | null |
| Output | {"a":0,"b":0} |
|   | {"a":1,"b":1} |
|   | {"a":2,"b":2} |
| Run |   |

| Command | jq '(.a, .b) \|= range(3)' |
|---|---|
| Input | null |
| Output | {"a":0,"b":0} |
| Run |   |

### Complex assignments

Lots more things are allowed on the left-hand side of a jq assignment than in most languages. We've already seen simple field accesses on the left hand side, and it's no surprise that array accesses work just as well:

```
.posts[0].title = "JQ Manual"
```

What may come as a surprise is that the expression on the left may produce multiple results, referring to different points in the input document:

```
.posts[].comments |= . + ["this is great"]
```

That example appends the string "this is great" to the "comments" array of each post in the input (where the input is an object with a field "posts" which is an array of posts).

When jq encounters an assignment like 'a = b', it records the "path" taken to select a part of the input document while executing a. This path is then used to find which part of the input to change while executing the assignment. Any filter may be used on the left-hand side of an equals - whichever paths it selects from the input will be where the assignment is performed.

This is a very powerful operation. Suppose we wanted to add a comment to blog posts, using the same "blog" input above. This time, we only want to comment on the posts written by "stedolan". We can find those posts using the "select" function described earlier:

```
.posts[] | select(.author == "stedolan")
```

The paths provided by this operation point to each of the posts that "stedolan" wrote, and we can comment on each of them in the same way that we did before:

```
(.posts[] | select(.author == "stedolan") | .comments) |=
    . + ["terrible."]
```
