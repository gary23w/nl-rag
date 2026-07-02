---
title: "jq 1.8 Manual (part 1/4)"
source: https://jqlang.github.io/jq/manual/
domain: jq-json
license: CC-BY-SA-4.0
tags: jq json, json processor, command-line json, json filter
fetched: 2026-07-02
part: 1/4
---

# jq 1.8 Manual

*For other versions, see 1.8, 1.7, 1.6, 1.5, 1.4, 1.3 or development version.*

A jq program is a "filter": it takes an input, and produces an output. There are a lot of builtin filters for extracting a particular field of an object, or converting a number to a string, or various other standard tasks.

Filters can be combined in various ways - you can pipe the output of one filter into another filter, or collect the output of a filter into an array.

Some filters produce multiple results, for instance there's one that produces all the elements of its input array. Piping that filter into a second runs the second filter for each element of the array. Generally, things that would be done with loops and iteration in other languages are just done by gluing filters together in jq.

It's important to remember that every filter has an input and an output. Even literals like "hello" or 42 are filters - they take an input but always produce the same literal as output. Operations that combine two filters, like addition, generally feed the same input to both and combine the results. So, you can implement an averaging filter as `add / length` - feeding the input array both to the `add` filter and the `length` filter and then performing the division.

But that's getting ahead of ourselves. :) Let's start with something simpler:


## Invoking jq

jq filters run on a stream of JSON data. The input to jq is parsed as a sequence of whitespace-separated JSON values which are passed through the provided filter one at a time. The output(s) of the filter are written to standard output, as a sequence of newline-separated JSON data.

The simplest and most common filter (or jq program) is `.`, which is the identity operator, copying the inputs of the jq processor to the output stream. Because the default behavior of the jq processor is to read JSON texts from the input stream, and to pretty-print outputs, the `.` program's main use is to validate and pretty-print the inputs. The jq programming language is quite rich and allows for much more than just validation and pretty-printing.

Note: it is important to mind the shell's quoting rules. As a general rule it's best to always quote (with single-quote characters on Unix shells) the jq program, as too many characters with special meaning to jq are also shell meta-characters. For example, `jq "foo"` will fail on most Unix shells because that will be the same as `jq foo`, which will generally fail because `foo is not defined`. When using the Windows command shell (cmd.exe) it's best to use double quotes around your jq program when given on the command-line (instead of the `-f program-file` option), but then double-quotes in the jq program need backslash escaping. When using the Powershell (`powershell.exe`) or the Powershell Core (`pwsh`/`pwsh.exe`), use single-quote characters around the jq program and backslash-escaped double-quotes (`\"`) inside the jq program.

- Unix shells: `jq '.["foo"]'`
- Powershell: `jq '.[\"foo\"]'`
- Windows command shell: `jq ".[\"foo\"]"`

Note: jq allows user-defined functions, but every jq program must have a top-level expression.

You can affect how jq reads and writes its input and output using some command-line options:

- `--null-input` / `-n`:

Don't read any input at all. Instead, the filter is run once using `null` as the input. This is useful when using jq as a simple calculator or to construct JSON data from scratch.

- `--raw-input` / `-R`:

Don't parse the input as JSON. Instead, each line of text is passed to the filter as a string. If combined with `--slurp`, then the entire input is passed to the filter as a single long string.

- `--slurp` / `-s`:

Instead of running the filter for each JSON object in the input, read the entire input stream into a large array and run the filter just once.

- `--compact-output` / `-c`:

By default, jq pretty-prints JSON output. Using this option will result in more compact output by instead putting each JSON object on a single line.

- `--raw-output` / `-r`:

With this option, if the filter's result is a string then it will be written directly to standard output rather than being formatted as a JSON string with quotes. This can be useful for making jq filters talk to non-JSON-based systems.

- `--raw-output0`:

Like `-r` but jq will print NUL instead of newline after each output. This can be useful when the values being output can contain newlines. When the output value contains NUL, jq exits with non-zero code.

- `--join-output` / `-j`:

Like `-r` but jq won't print a newline after each output.

- `--ascii-output` / `-a`:

jq usually outputs non-ASCII Unicode codepoints as UTF-8, even if the input specified them as escape sequences (like "\u03bc"). Using this option, you can force jq to produce pure ASCII output with every non-ASCII character replaced with the equivalent escape sequence.

- `--sort-keys` / `-S`:

Output the fields of each object with the keys in sorted order.

- `--color-output` / `-C` and `--monochrome-output` / `-M`:

By default, jq outputs colored JSON if writing to a terminal. You can force it to produce color even if writing to a pipe or a file using `-C`, and disable color with `-M`. When the `NO_COLOR` environment variable is not empty, jq disables colored output by default, but you can enable it by `-C`.

Colors can be configured with the `JQ_COLORS` environment variable (see below).

- `--tab`:

Use a tab for each indentation level instead of two spaces.

- `--indent n`:

Use the given number of spaces (no more than 7) for indentation.

- `--unbuffered`:

Flush the output after each JSON object is printed (useful if you're piping a slow data source into jq and piping jq's output elsewhere).

- `--stream`:

Parse the input in streaming fashion, outputting arrays of path and leaf values (scalars and empty arrays or empty objects). For example, `"a"` becomes `[[],"a"]`, and `[[],"a",["b"]]` becomes `[[0],[]]`, `[[1],"a"]`, and `[[2,0],"b"]`.

This is useful for processing very large inputs. Use this in conjunction with filtering and the `reduce` and `foreach` syntax to reduce large inputs incrementally.

- `--stream-errors`:

Like `--stream`, but invalid JSON inputs yield array values where the first element is the error and the second is a path. For example, `["a",n]` produces `["Invalid literal at line 1, column 7",[1]]`.

Implies `--stream`. Invalid JSON inputs produce no error values when `--stream` without `--stream-errors`.

- `--seq`:

Use the `application/json-seq` MIME type scheme for separating JSON texts in jq's input and output. This means that an ASCII RS (record separator) character is printed before each value on output and an ASCII LF (line feed) is printed after every output. Input JSON texts that fail to parse are ignored (but warned about), discarding all subsequent input until the next RS. This mode also parses the output of jq without the `--seq` option.

- `-f` / `--from-file`:

Read the filter from a file rather than from a command line, like awk's -f option. This changes the filter argument to be interpreted as a filename, instead of the source of a program.

- `-L directory` / `--library-path directory`:

Prepend `directory` to the search list for modules. If this option is used then no builtin search list is used. See the section on modules below.

- `--arg name value`:

This option passes a value to the jq program as a predefined variable. If you run jq with `--arg foo bar`, then `$foo` is available in the program and has the value `"bar"`. Note that `value` will be treated as a string, so `--arg foo 123` will bind `$foo` to `"123"`.

Named arguments are also available to the jq program as `$ARGS.named`. When the name is not a valid identifier, this is the only way to access it.

- `--argjson name JSON-text`:

This option passes a JSON-encoded value to the jq program as a predefined variable. If you run jq with `--argjson foo 123`, then `$foo` is available in the program and has the value `123`.

- `--slurpfile variable-name filename`:

This option reads all the JSON texts in the named file and binds an array of the parsed JSON values to the given global variable. If you run jq with `--slurpfile foo bar`, then `$foo` is available in the program and has an array whose elements correspond to the texts in the file named `bar`.

- `--rawfile variable-name filename`:

This option reads in the named file and binds its content to the given global variable. If you run jq with `--rawfile foo bar`, then `$foo` is available in the program and has a string whose content is set to the text in the file named `bar`.

- `--args`:

Remaining arguments are positional string arguments. These are available to the jq program as `$ARGS.positional[]`.

- `--jsonargs`:

Remaining arguments are positional JSON text arguments. These are available to the jq program as `$ARGS.positional[]`.

- `--exit-status` / `-e`:

Sets the exit status of jq to 0 if the last output value was neither `false` nor `null`, 1 if the last output value was either `false` or `null`, or 4 if no valid result was ever produced. Normally jq exits with 2 if there was any usage problem or system error, 3 if there was a jq program compile error, or 0 if the jq program ran.

Another way to set the exit status is with the `halt_error` builtin function.

- `--binary` / `-b`:

Windows users using WSL, MSYS2, or Cygwin, should use this option when using a native jq.exe, otherwise jq will turn newlines (LFs) into carriage-return-then-newline (CRLF).

- `--version` / `-V`:

Output the jq version and exit with zero.

- `--build-configuration`:

Output the build configuration of jq and exit with zero. This output has no supported format or structure and may change without notice in future releases.

- `--help` / `-h`:

Output the jq help and exit with zero.

- `--`:

Terminates argument processing. Remaining arguments are not interpreted as options.

- `--run-tests [filename]`:

Runs the tests in the given file or standard input. This must be the last option given and does not honor all preceding options. The input consists of comment lines, empty lines, and program lines followed by one input line, as many lines of output as are expected (one per output), and a terminating empty line. Compilation failure tests start with a line containing only `%%FAIL`, then a line containing the program to compile, then a line containing an error message to compare to the actual.

Be warned that this option can change backwards-incompatibly.


## Basic filters

### Identity: `.`

The absolute simplest filter is `.` . This filter takes its input and produces the same value as output. That is, this is the identity operator.

Since jq by default pretty-prints all output, a trivial program consisting of nothing but `.` can be used to format JSON output from, say, `curl`.

Although the identity filter never modifies the value of its input, jq processing can sometimes make it appear as though it does. For example, using the current implementation of jq, we would see that the expression:

```
1E1234567890 | .
```

produces `1.7976931348623157e+308` on at least one platform. This is because, in the process of parsing the number, this particular version of jq has converted it to an IEEE754 double-precision representation, losing precision.

The way in which jq handles numbers has changed over time and further changes are likely within the parameters set by the relevant JSON standards. Moreover, build configuration options can alter how jq processes numbers.

The following remarks are therefore offered with the understanding that they are intended to be descriptive of the current version of jq and should not be interpreted as being prescriptive:

(1) Any arithmetic operation on a number that has not already been converted to an IEEE754 double precision representation will trigger a conversion to the IEEE754 representation.

(2) jq will attempt to maintain the original decimal precision of number literals (if the `--disable-decnum` build configuration option was not used), but in expressions such `1E1234567890`, precision will be lost if the exponent is too large.

(3) Comparisons are carried out using the untruncated big decimal representation of numbers if available, as illustrated in one of the following examples.

The examples below use the builtin function `have_decnum` in order to demonstrate the expected effects of using / not using the `--disable-decnum` build configuration option, and also to allow automated tests derived from these examples to pass regardless of whether that option is used.

| Command | jq '.' |
|---|---|
| Input | "Hello, world!" |
| Output | "Hello, world!" |
| Run |   |

| Command | jq '.' |
|---|---|
| Input | 0.12345678901234567890123456789 |
| Output | 0.12345678901234567890123456789 |
| Run |   |

| Command | jq '[., tojson] == if have_decnum then [12345678909876543212345,"12345678909876543212345"] else [12345678909876543000000,"12345678909876543000000"] end' |
|---|---|
| Input | 12345678909876543212345 |
| Output | true |
| Run |   |

| Command | jq '[1234567890987654321,-1234567890987654321 \| tojson] == if have_decnum then ["1234567890987654321","-1234567890987654321"] else ["1234567890987654400","-1234567890987654400"] end' |
|---|---|
| Input | null |
| Output | true |
| Run |   |

| Command | jq '. < 0.12345678901234567890123456788' |
|---|---|
| Input | 0.12345678901234567890123456789 |
| Output | false |
| Run |   |

| Command | jq 'map([., . == 1]) \| tojson == if have_decnum then "[[1,true],[1.000,true],[1.0,true],[1.00,true]]" else "[[1,true],[1,true],[1,true],[1,true]]" end' |
|---|---|
| Input | [1, 1.000, 1.0, 100e-2] |
| Output | true |
| Run |   |

| Command | jq '. as $big \| [$big, $big + 1] \| map(. > 10000000000000000000000000000000) \| . == if have_decnum then [true, false] else [false, false] end' |
|---|---|
| Input | 10000000000000000000000000000001 |
| Output | true |
| Run |   |

### Object Identifier-Index: `.foo`, `.foo.bar`

The simplest *useful* filter has the form `.foo`. When given a JSON object (aka dictionary or hash) as input, `.foo` produces the value at the key "foo" if the key is present, or null otherwise.

A filter of the form `.foo.bar` is equivalent to `.foo | .bar`.

The `.foo` syntax only works for simple, identifier-like keys, that is, keys that are all made of alphanumeric characters and underscore, and which do not start with a digit.

If the key contains special characters or starts with a digit, you need to surround it with double quotes like this: `."foo$"`, or else `.["foo$"]`.

For example `.["foo::bar"]` and `.["foo.bar"]` work while `.foo::bar` does not.

| Command | jq '.foo' |
|---|---|
| Input | {"foo": 42, "bar": "less interesting data"} |
| Output | 42 |
| Run |   |

| Command | jq '.foo' |
|---|---|
| Input | {"notfoo": true, "alsonotfoo": false} |
| Output | null |
| Run |   |

| Command | jq '.["foo"]' |
|---|---|
| Input | {"foo": 42} |
| Output | 42 |
| Run |   |

### Optional Object Identifier-Index: `.foo?`

Just like `.foo`, but does not output an error when `.` is not an object.

| Command | jq '.foo?' |
|---|---|
| Input | {"foo": 42, "bar": "less interesting data"} |
| Output | 42 |
| Run |   |

| Command | jq '.foo?' |
|---|---|
| Input | {"notfoo": true, "alsonotfoo": false} |
| Output | null |
| Run |   |

| Command | jq '.["foo"]?' |
|---|---|
| Input | {"foo": 42} |
| Output | 42 |
| Run |   |

| Command | jq '[.foo?]' |
|---|---|
| Input | [1,2] |
| Output | [] |
| Run |   |

### Object Index: `.[<string>]`

You can also look up fields of an object using syntax like `.["foo"]` (`.foo` above is a shorthand version of this, but only for identifier-like strings).

### Array Index: `.[<number>]`

When the index value is an integer, `.[<number>]` can index arrays. Arrays are zero-based, so `.[2]` returns the third element.

Negative indices are allowed, with -1 referring to the last element, -2 referring to the next to last element, and so on.

| Command | jq '.[0]' |
|---|---|
| Input | [{"name":"JSON", "good":true}, {"name":"XML", "good":false}] |
| Output | {"name":"JSON", "good":true} |
| Run |   |

| Command | jq '.[2]' |
|---|---|
| Input | [{"name":"JSON", "good":true}, {"name":"XML", "good":false}] |
| Output | null |
| Run |   |

| Command | jq '.[-2]' |
|---|---|
| Input | [1,2,3] |
| Output | 2 |
| Run |   |

### Array/String Slice: `.[<number>:<number>]`

The `.[<number>:<number>]` syntax can be used to return a subarray of an array or substring of a string. The array returned by `.[10:15]` will be of length 5, containing the elements from index 10 (inclusive) to index 15 (exclusive). Either index may be negative (in which case it counts backwards from the end of the array), or omitted (in which case it refers to the start or end of the array). Indices are zero-based.

| Command | jq '.[2:4]' |
|---|---|
| Input | ["a","b","c","d","e"] |
| Output | ["c", "d"] |
| Run |   |

| Command | jq '.[2:4]' |
|---|---|
| Input | "abcdefghi" |
| Output | "cd" |
| Run |   |

| Command | jq '.[:3]' |
|---|---|
| Input | ["a","b","c","d","e"] |
| Output | ["a", "b", "c"] |
| Run |   |

| Command | jq '.[-2:]' |
|---|---|
| Input | ["a","b","c","d","e"] |
| Output | ["d", "e"] |
| Run |   |

### Array/Object Value Iterator: `.[]`

If you use the `.[index]` syntax, but omit the index entirely, it will return *all* of the elements of an array. Running `.[]` with the input `[1,2,3]` will produce the numbers as three separate results, rather than as a single array. A filter of the form `.foo[]` is equivalent to `.foo | .[]`.

You can also use this on an object, and it will return all the values of the object.

Note that the iterator operator is a generator of values.

| Command | jq '.[]' |
|---|---|
| Input | [{"name":"JSON", "good":true}, {"name":"XML", "good":false}] |
| Output | {"name":"JSON", "good":true} |
|   | {"name":"XML", "good":false} |
| Run |   |

| Command | jq '.[]' |
|---|---|
| Input | [] |
| Output | none |
| Run |   |

| Command | jq '.foo[]' |
|---|---|
| Input | {"foo":[1,2,3]} |
| Output | 1 |
|   | 2 |
|   | 3 |
| Run |   |

| Command | jq '.[]' |
|---|---|
| Input | {"a": 1, "b": 1} |
| Output | 1 |
|   | 1 |
| Run |   |

### `.[]?`

Like `.[]`, but no errors will be output if . is not an array or object. A filter of the form `.foo[]?` is equivalent to `.foo | .[]?`.

### Comma: `,`

If two filters are separated by a comma, then the same input will be fed into both and the two filters' output value streams will be concatenated in order: first, all of the outputs produced by the left expression, and then all of the outputs produced by the right. For instance, filter `.foo, .bar`, produces both the "foo" fields and "bar" fields as separate outputs.

The `,` operator is one way to construct generators.

| Command | jq '.foo, .bar' |
|---|---|
| Input | {"foo": 42, "bar": "something else", "baz": true} |
| Output | 42 |
|   | "something else" |
| Run |   |

| Command | jq '.user, .projects[]' |
|---|---|
| Input | {"user":"stedolan", "projects": ["jq", "wikiflow"]} |
| Output | "stedolan" |
|   | "jq" |
|   | "wikiflow" |
| Run |   |

| Command | jq '.[4,2]' |
|---|---|
| Input | ["a","b","c","d","e"] |
| Output | "e" |
|   | "c" |
| Run |   |

### Pipe: `|`

The | operator combines two filters by feeding the output(s) of the one on the left into the input of the one on the right. It's similar to the Unix shell's pipe, if you're used to that.

If the one on the left produces multiple results, the one on the right will be run for each of those results. So, the expression `.[] | .foo` retrieves the "foo" field of each element of the input array. This is a cartesian product, which can be surprising.

Note that `.a.b.c` is the same as `.a | .b | .c`.

Note too that `.` is the input value at the particular stage in a "pipeline", specifically: where the `.` expression appears. Thus `.a | . | .b` is the same as `.a.b`, as the `.` in the middle refers to whatever value `.a` produced.

| Command | jq '.[] \| .name' |
|---|---|
| Input | [{"name":"JSON", "good":true}, {"name":"XML", "good":false}] |
| Output | "JSON" |
|   | "XML" |
| Run |   |

### Parenthesis

Parenthesis work as a grouping operator just as in any typical programming language.

| Command | jq '(. + 2) * 5' |
|---|---|
| Input | 1 |
| Output | 15 |
| Run |   |


## Types and Values

jq supports the same set of datatypes as JSON - numbers, strings, booleans, arrays, objects (which in JSON-speak are hashes with only string keys), and "null".

Booleans, null, strings and numbers are written the same way as in JSON. Just like everything else in jq, these simple values take an input and produce an output - `42` is a valid jq expression that takes an input, ignores it, and returns 42 instead.

Numbers in jq are internally represented by their IEEE754 double precision approximation. Any arithmetic operation with numbers, whether they are literals or results of previous filters, will produce a double precision floating point result.

However, when parsing a literal jq will store the original literal string. If no mutation is applied to this value then it will make to the output in its original form, even if conversion to double would result in a loss.

### Array construction: `[]`

As in JSON, `[]` is used to construct arrays, as in `[1,2,3]`. The elements of the arrays can be any jq expression, including a pipeline. All of the results produced by all of the expressions are collected into one big array. You can use it to construct an array out of a known quantity of values (as in `[.foo, .bar, .baz]`) or to "collect" all the results of a filter into an array (as in `[.items[].name]`)

Once you understand the "," operator, you can look at jq's array syntax in a different light: the expression `[1,2,3]` is not using a built-in syntax for comma-separated arrays, but is instead applying the `[]` operator (collect results) to the expression 1,2,3 (which produces three different results).

If you have a filter `X` that produces four results, then the expression `[X]` will produce a single result, an array of four elements.

| Command | jq '[.user, .projects[]]' |
|---|---|
| Input | {"user":"stedolan", "projects": ["jq", "wikiflow"]} |
| Output | ["stedolan", "jq", "wikiflow"] |
| Run |   |

| Command | jq '[ .[] \| . * 2]' |
|---|---|
| Input | [1, 2, 3] |
| Output | [2, 4, 6] |
| Run |   |

### Object Construction: `{}`

Like JSON, `{}` is for constructing objects (aka dictionaries or hashes), as in: `{"a": 42, "b": 17}`.

If the keys are "identifier-like", then the quotes can be left off, as in `{a:42, b:17}`. Variable references as key expressions use the value of the variable as the key. Key expressions other than constant literals, identifiers, or variable references, need to be parenthesized, e.g., `{("a"+"b"):59}`.

The value can be any expression (although you may need to wrap it in parentheses if, for example, it contains colons), which gets applied to the {} expression's input (remember, all filters have an input and an output).

```
{foo: .bar}
```

will produce the JSON object `{"foo": 42}` if given the JSON object `{"bar":42, "baz":43}` as its input. You can use this to select particular fields of an object: if the input is an object with "user", "title", "id", and "content" fields and you just want "user" and "title", you can write

```
{user: .user, title: .title}
```

Because that is so common, there's a shortcut syntax for it: `{user, title}`.

If one of the expressions produces multiple results, multiple dictionaries will be produced. If the input's

```
{"user":"stedolan","titles":["JQ Primer", "More JQ"]}
```

then the expression

```
{user, title: .titles[]}
```

will produce two outputs:

```
{"user":"stedolan", "title": "JQ Primer"}
{"user":"stedolan", "title": "More JQ"}
```

Putting parentheses around the key means it will be evaluated as an expression. With the same input as above,

```
{(.user): .titles}
```

produces

```
{"stedolan": ["JQ Primer", "More JQ"]}
```

Variable references as keys use the value of the variable as the key. Without a value then the variable's name becomes the key and its value becomes the value,

```
"f o o" as $foo | "b a r" as $bar | {$foo, $bar:$foo}
```

produces

```
{"foo":"f o o","b a r":"f o o"}
```

| Command | jq '{user, title: .titles[]}' |
|---|---|
| Input | {"user":"stedolan","titles":["JQ Primer", "More JQ"]} |
| Output | {"user":"stedolan", "title": "JQ Primer"} |
|   | {"user":"stedolan", "title": "More JQ"} |
| Run |   |

| Command | jq '{(.user): .titles}' |
|---|---|
| Input | {"user":"stedolan","titles":["JQ Primer", "More JQ"]} |
| Output | {"stedolan": ["JQ Primer", "More JQ"]} |
| Run |   |

### Recursive Descent: `..`

Recursively descends `.`, producing every value. This is the same as the zero-argument `recurse` builtin (see below). This is intended to resemble the XPath `//` operator. Note that `..a` does not work; use `.. | .a` instead. In the example below we use `.. | .a?` to find all the values of object keys "a" in any object found "below" `.`.

This is particularly useful in conjunction with `path(EXP)` (also see below) and the `?` operator.

| Command | jq '.. \| .a?' |
|---|---|
| Input | [[{"a":1}]] |
| Output | 1 |
| Run |   |
