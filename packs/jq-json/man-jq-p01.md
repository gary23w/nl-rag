---
title: "jq(1) (part 1/3)"
source: https://man.archlinux.org/man/jq.1
domain: jq-json
license: CC-BY-SA-4.0
tags: jq json, json processor, command-line json, json filter
fetched: 2026-07-02
part: 1/3
---

# jq(1)

| JQ(1) |   | JQ(1) |
|---|---|---|

# NAME

**jq** - Command-line JSON processor

# SYNOPSIS

**jq** [*options*...] *filter* [*files*...]

**jq** can transform JSON in various ways, by selecting, iterating, reducing and otherwise mangling JSON documents. For instance, running the command **jq ´map(.price) | add´** will take an array of JSON objects as input and return the sum of their "price" fields.

**jq** can accept text input as well, but by default, **jq** reads a stream of JSON entities (including numbers and other literals) from **stdin**. Whitespace is only needed to separate entities such as 1 and 2, and true and false. One or more *files* may be specified, in which case **jq** will read input from those instead.

The *options* are described in the [INVOKING JQ] section; they mostly concern input and output formatting. The *filter* is written in the jq language and specifies how to transform the input file or document.

# FILTERS

A jq program is a "filter": it takes an input, and produces an output. There are a lot of builtin filters for extracting a particular field of an object, or converting a number to a string, or various other standard tasks.

Filters can be combined in various ways - you can pipe the output of one filter into another filter, or collect the output of a filter into an array.

Some filters produce multiple results, for instance there´s one that produces all the elements of its input array. Piping that filter into a second runs the second filter for each element of the array. Generally, things that would be done with loops and iteration in other languages are just done by gluing filters together in jq.

It´s important to remember that every filter has an input and an output. Even literals like "hello" or 42 are filters - they take an input but always produce the same literal as output. Operations that combine two filters, like addition, generally feed the same input to both and combine the results. So, you can implement an averaging filter as **add / length** - feeding the input array both to the **add** filter and the **length** filter and then performing the division.

But that´s getting ahead of ourselves. :) Let´s start with something simpler:

# INVOKING JQ

jq filters run on a stream of JSON data. The input to jq is parsed as a sequence of whitespace-separated JSON values which are passed through the provided filter one at a time. The output(s) of the filter are written to standard output, as a sequence of newline-separated JSON data.

The simplest and most common filter (or jq program) is **.**, which is the identity operator, copying the inputs of the jq processor to the output stream. Because the default behavior of the jq processor is to read JSON texts from the input stream, and to pretty-print outputs, the **.** program´s main use is to validate and pretty-print the inputs. The jq programming language is quite rich and allows for much more than just validation and pretty-printing.

Note: it is important to mind the shell´s quoting rules. As a general rule it´s best to always quote (with single-quote characters on Unix shells) the jq program, as too many characters with special meaning to jq are also shell meta-characters. For example, **jq "foo"** will fail on most Unix shells because that will be the same as **jq foo**, which will generally fail because **foo is not defined**. When using the Windows command shell (cmd.exe) it´s best to use double quotes around your jq program when given on the command-line (instead of the **-f program-file** option), but then double-quotes in the jq program need backslash escaping. When using the Powershell (**powershell.exe**) or the Powershell Core (**pwsh**/**pwsh.exe**), use single-quote characters around the jq program and backslash-escaped double-quotes (**\"**) inside the jq program.

- Unix shells: **jq ´.["foo"]´**
- Powershell: **jq ´.[\"foo\"]´**
- Windows command shell: **jq ".[\"foo\"]"**

Note: jq allows user-defined functions, but every jq program must have a top-level expression.

You can affect how jq reads and writes its input and output using some command-line options:

****--null-input** / **-n**:**

Don´t read any input at all. Instead, the filter is run once using

null

as the input. This is useful when using jq as a simple calculator or to construct JSON data from scratch.

****--raw-input** / **-R**:**

Don´t parse the input as JSON. Instead, each line of text is passed to the filter as a string. If combined with

--slurp

, then the entire input is passed to the filter as a single long string.

****--slurp** / **-s**:**

Instead of running the filter for each JSON object in the input, read the entire input stream into a large array and run the filter just once.

****--compact-output** / **-c**:**

By default, jq pretty-prints JSON output. Using this option will result in more compact output by instead putting each JSON object on a single line.

****--raw-output** / **-r**:**

With this option, if the filter´s result is a string then it will be written directly to standard output rather than being formatted as a JSON string with quotes. This can be useful for making jq filters talk to non-JSON-based systems.

****--raw-output0**:**

Like

-r

but jq will print NUL instead of newline after each output. This can be useful when the values being output can contain newlines. When the output value contains NUL, jq exits with non-zero code.

****--join-output** / **-j**:**

Like

-r

but jq won´t print a newline after each output.

****--ascii-output** / **-a**:**

jq usually outputs non-ASCII Unicode codepoints as UTF-8, even if the input specified them as escape sequences (like "\u03bc"). Using this option, you can force jq to produce pure ASCII output with every non-ASCII character replaced with the equivalent escape sequence.

****--sort-keys** / **-S**:**

Output the fields of each object with the keys in sorted order.

****--color-output** / **-C** and **--monochrome-output** / **-M**:**

By default, jq outputs colored JSON if writing to a terminal. You can force it to produce color even if writing to a pipe or a file using

-C

, and disable color with

-M

. When the

NO_COLOR

environment variable is not empty, jq disables colored output by default, but you can enable it by

-C

.

Colors can be configured with the

JQ_COLORS

environment variable (see below).

****--tab**:**

Use a tab for each indentation level instead of two spaces.

****--indent n**:**

Use the given number of spaces (no more than 7) for indentation.

****--unbuffered**:**

Flush the output after each JSON object is printed (useful if you´re piping a slow data source into jq and piping jq´s output elsewhere).

****--stream**:**

Parse the input in streaming fashion, outputting arrays of path and leaf values (scalars and empty arrays or empty objects). For example,

"a"

becomes

[[],"a"]

, and

[[],"a",["b"]]

becomes

[[0],[]]

,

[[1],"a"]

, and

[[2,0],"b"]

.

This is useful for processing very large inputs. Use this in conjunction with filtering and the

reduce

and

foreach

syntax to reduce large inputs incrementally.

****--stream-errors**:**

Like

--stream

, but invalid JSON inputs yield array values where the first element is the error and the second is a path. For example,

["a",n]

produces

["Invalid literal at line 1, column 7",[1]]

.

Implies

--stream

. Invalid JSON inputs produce no error values when

--stream

without

--stream-errors

.

****--seq**:**

Use the

application/json-seq

MIME type scheme for separating JSON texts in jq´s input and output. This means that an ASCII RS (record separator) character is printed before each value on output and an ASCII LF (line feed) is printed after every output. Input JSON texts that fail to parse are ignored (but warned about), discarding all subsequent input until the next RS. This mode also parses the output of jq without the

--seq

option.

****-f** / **--from-file**:**

Read the filter from a file rather than from a command line, like awk´s -f option. This changes the filter argument to be interpreted as a filename, instead of the source of a program.

****-L directory** / **--library-path directory**:**

Prepend

directory

to the search list for modules. If this option is used then no builtin search list is used. See the section on modules below.

****--arg name value**:**

This option passes a value to the jq program as a predefined variable. If you run jq with

--arg foo bar

, then

$foo

is available in the program and has the value

"bar"

. Note that

value

will be treated as a string, so

--arg foo 123

will bind

$foo

to

"123"

.

Named arguments are also available to the jq program as

$ARGS.named

. When the name is not a valid identifier, this is the only way to access it.

****--argjson name JSON-text**:**

This option passes a JSON-encoded value to the jq program as a predefined variable. If you run jq with

--argjson foo 123

, then

$foo

is available in the program and has the value

123

.

****--slurpfile variable-name filename**:**

This option reads all the JSON texts in the named file and binds an array of the parsed JSON values to the given global variable. If you run jq with

--slurpfile foo bar

, then

$foo

is available in the program and has an array whose elements correspond to the texts in the file named

bar

.

****--rawfile variable-name filename**:**

This option reads in the named file and binds its content to the given global variable. If you run jq with

--rawfile foo bar

, then

$foo

is available in the program and has a string whose content is set to the text in the file named

bar

.

****--args**:**

Remaining arguments are positional string arguments. These are available to the jq program as

$ARGS.positional[]

.

****--jsonargs**:**

Remaining arguments are positional JSON text arguments. These are available to the jq program as

$ARGS.positional[]

.

****--exit-status** / **-e**:**

Sets the exit status of jq to 0 if the last output value was neither

false

nor

null

, 1 if the last output value was either

false

or

null

, or 4 if no valid result was ever produced. Normally jq exits with 2 if there was any usage problem or system error, 3 if there was a jq program compile error, or 0 if the jq program ran.

Another way to set the exit status is with the

halt_error

builtin function.

****--binary** / **-b**:**

Windows users using WSL, MSYS2, or Cygwin, should use this option when using a native jq.exe, otherwise jq will turn newlines (LFs) into carriage-return-then-newline (CRLF).

****--version** / **-V**:**

Output the jq version and exit with zero.

****--build-configuration**:**

Output the build configuration of jq and exit with zero. This output has no supported format or structure and may change without notice in future releases.

****--help** / **-h**:**

Output the jq help and exit with zero.

****--**:**

Terminates argument processing. Remaining arguments are not interpreted as options.

****--run-tests [filename]**:**

Runs the tests in the given file or standard input. This must be the last option given and does not honor all preceding options. The input consists of comment lines, empty lines, and program lines followed by one input line, as many lines of output as are expected (one per output), and a terminating empty line. Compilation failure tests start with a line containing only

%%FAIL

, then a line containing the program to compile, then a line containing an error message to compare to the actual.

Be warned that this option can change backwards-incompatibly.

# BASIC FILTERS


## Identity: .

The absolute simplest filter is **.** . This filter takes its input and produces the same value as output. That is, this is the identity operator.

Since jq by default pretty-prints all output, a trivial program consisting of nothing but **.** can be used to format JSON output from, say, **curl**.

Although the identity filter never modifies the value of its input, jq processing can sometimes make it appear as though it does. For example, using the current implementation of jq, we would see that the expression:

```
1E1234567890 | .
```

produces **1.7976931348623157e+308** on at least one platform. This is because, in the process of parsing the number, this particular version of jq has converted it to an IEEE754 double-precision representation, losing precision.

The way in which jq handles numbers has changed over time and further changes are likely within the parameters set by the relevant JSON standards. Moreover, build configuration options can alter how jq processes numbers.

The following remarks are therefore offered with the understanding that they are intended to be descriptive of the current version of jq and should not be interpreted as being prescriptive:

(1) Any arithmetic operation on a number that has not already been converted to an IEEE754 double precision representation will trigger a conversion to the IEEE754 representation.

(2) jq will attempt to maintain the original decimal precision of number literals (if the **--disable-decnum** build configuration option was not used), but in expressions such **1E1234567890**, precision will be lost if the exponent is too large.

(3) Comparisons are carried out using the untruncated big decimal representation of numbers if available, as illustrated in one of the following examples.

The examples below use the builtin function **have_decnum** in order to demonstrate the expected effects of using / not using the **--disable-decnum** build configuration option, and also to allow automated tests derived from these examples to pass regardless of whether that option is used.

```
jq ´.´
   "Hello, world!"
=> "Hello, world!"
jq ´.´
   0.12345678901234567890123456789
=> 0.12345678901234567890123456789
jq ´[., tojson] == if have_decnum then [12345678909876543212345,"12345678909876543212345"] else [12345678909876543000000,"12345678909876543000000"] end´
   12345678909876543212345
=> true
jq ´[1234567890987654321,-1234567890987654321 | tojson] == if have_decnum then ["1234567890987654321","-1234567890987654321"] else ["1234567890987654400","-1234567890987654400"] end´
   null
=> true
jq ´. < 0.12345678901234567890123456788´
   0.12345678901234567890123456789
=> false
jq ´map([., . == 1]) | tojson == if have_decnum then "[[1,true],[1.000,true],[1.0,true],[1.00,true]]" else "[[1,true],[1,true],[1,true],[1,true]]" end´
   [1, 1.000, 1.0, 100e-2]
=> true
jq ´. as $big | [$big, $big + 1] | map(. > 10000000000000000000000000000000) | . == if have_decnum then [true, false] else [false, false] end´
   10000000000000000000000000000001
=> true
```


## Object Identifier-Index: .foo, .foo.bar

The simplest *useful* filter has the form **.foo**. When given a JSON object (aka dictionary or hash) as input, **.foo** produces the value at the key "foo" if the key is present, or null otherwise.

A filter of the form **.foo.bar** is equivalent to **.foo | .bar**.

The **.foo** syntax only works for simple, identifier-like keys, that is, keys that are all made of alphanumeric characters and underscore, and which do not start with a digit.

If the key contains special characters or starts with a digit, you need to surround it with double quotes like this: **."foo$"**, or else **.["foo$"]**.

For example **.["foo::bar"]** and **.["foo.bar"]** work while **.foo::bar** does not.

```
jq ´.foo´
   {"foo": 42, "bar": "less interesting data"}
=> 42
jq ´.foo´
   {"notfoo": true, "alsonotfoo": false}
=> null
jq ´.["foo"]´
   {"foo": 42}
=> 42
```


## Optional Object Identifier-Index: .foo?

Just like **.foo**, but does not output an error when **.** is not an object.

```
jq ´.foo?´
   {"foo": 42, "bar": "less interesting data"}
=> 42
jq ´.foo?´
   {"notfoo": true, "alsonotfoo": false}
=> null
jq ´.["foo"]?´
   {"foo": 42}
=> 42
jq ´[.foo?]´
   [1,2]
=> []
```


## Object Index: .[<string>]

You can also look up fields of an object using syntax like **.["foo"]** (**.foo** above is a shorthand version of this, but only for identifier-like strings).


## Array Index: .[<number>]

When the index value is an integer, **.[<number>]** can index arrays. Arrays are zero-based, so **.[2]** returns the third element.

Negative indices are allowed, with -1 referring to the last element, -2 referring to the next to last element, and so on.

```
jq ´.[0]´
   [{"name":"JSON", "good":true}, {"name":"XML", "good":false}]
=> {"name":"JSON", "good":true}
jq ´.[2]´
   [{"name":"JSON", "good":true}, {"name":"XML", "good":false}]
=> null
jq ´.[-2]´
   [1,2,3]
=> 2
```


## Array/String Slice: .[<number>:<number>]

The **.[<number>:<number>]** syntax can be used to return a subarray of an array or substring of a string. The array returned by **.[10:15]** will be of length 5, containing the elements from index 10 (inclusive) to index 15 (exclusive). Either index may be negative (in which case it counts backwards from the end of the array), or omitted (in which case it refers to the start or end of the array). Indices are zero-based.

```
jq ´.[2:4]´
   ["a","b","c","d","e"]
=> ["c", "d"]
jq ´.[2:4]´
   "abcdefghi"
=> "cd"
jq ´.[:3]´
   ["a","b","c","d","e"]
=> ["a", "b", "c"]
jq ´.[-2:]´
   ["a","b","c","d","e"]
=> ["d", "e"]
```


## Array/Object Value Iterator: .[]

If you use the **.[index]** syntax, but omit the index entirely, it will return *all* of the elements of an array. Running **.[]** with the input **[1,2,3]** will produce the numbers as three separate results, rather than as a single array. A filter of the form **.foo[]** is equivalent to **.foo | .[]**.

You can also use this on an object, and it will return all the values of the object.

Note that the iterator operator is a generator of values.

```
jq ´.[]´
   [{"name":"JSON", "good":true}, {"name":"XML", "good":false}]
=> {"name":"JSON", "good":true}, {"name":"XML", "good":false}
jq ´.[]´
   []
=> 
jq ´.foo[]´
   {"foo":[1,2,3]}
=> 1, 2, 3
jq ´.[]´
   {"a": 1, "b": 1}
=> 1, 1
```


## .[]?

Like **.[]**, but no errors will be output if . is not an array or object. A filter of the form **.foo[]?** is equivalent to **.foo | .[]?**.


## Comma: ,

If two filters are separated by a comma, then the same input will be fed into both and the two filters´ output value streams will be concatenated in order: first, all of the outputs produced by the left expression, and then all of the outputs produced by the right. For instance, filter **.foo, .bar**, produces both the "foo" fields and "bar" fields as separate outputs.

The **,** operator is one way to construct generators.

```
jq ´.foo, .bar´
   {"foo": 42, "bar": "something else", "baz": true}
=> 42, "something else"
jq ´.user, .projects[]´
   {"user":"stedolan", "projects": ["jq", "wikiflow"]}
=> "stedolan", "jq", "wikiflow"
jq ´.[4,2]´
   ["a","b","c","d","e"]
=> "e", "c"
```


## Pipe: |

The | operator combines two filters by feeding the output(s) of the one on the left into the input of the one on the right. It´s similar to the Unix shell´s pipe, if you´re used to that.

If the one on the left produces multiple results, the one on the right will be run for each of those results. So, the expression **.[] | .foo** retrieves the "foo" field of each element of the input array. This is a cartesian product, which can be surprising.

Note that **.a.b.c** is the same as **.a | .b | .c**.

Note too that **.** is the input value at the particular stage in a "pipeline", specifically: where the **.** expression appears. Thus **.a | . | .b** is the same as **.a.b**, as the **.** in the middle refers to whatever value **.a** produced.

```
jq ´.[] | .name´
   [{"name":"JSON", "good":true}, {"name":"XML", "good":false}]
=> "JSON", "XML"
```


## Parenthesis

Parenthesis work as a grouping operator just as in any typical programming language.

```
jq ´(. + 2) * 5´
   1
=> 15
```

# TYPES AND VALUES

jq supports the same set of datatypes as JSON - numbers, strings, booleans, arrays, objects (which in JSON-speak are hashes with only string keys), and "null".

Booleans, null, strings and numbers are written the same way as in JSON. Just like everything else in jq, these simple values take an input and produce an output - **42** is a valid jq expression that takes an input, ignores it, and returns 42 instead.

Numbers in jq are internally represented by their IEEE754 double precision approximation. Any arithmetic operation with numbers, whether they are literals or results of previous filters, will produce a double precision floating point result.

However, when parsing a literal jq will store the original literal string. If no mutation is applied to this value then it will make to the output in its original form, even if conversion to double would result in a loss.


## Array construction: []

As in JSON, **[]** is used to construct arrays, as in **[1,2,3]**. The elements of the arrays can be any jq expression, including a pipeline. All of the results produced by all of the expressions are collected into one big array. You can use it to construct an array out of a known quantity of values (as in **[.foo, .bar, .baz]**) or to "collect" all the results of a filter into an array (as in **[.items[].name]**)

Once you understand the "," operator, you can look at jq´s array syntax in a different light: the expression **[1,2,3]** is not using a built-in syntax for comma-separated arrays, but is instead applying the **[]** operator (collect results) to the expression 1,2,3 (which produces three different results).

If you have a filter **X** that produces four results, then the expression **[X]** will produce a single result, an array of four elements.

```
jq ´[.user, .projects[]]´
   {"user":"stedolan", "projects": ["jq", "wikiflow"]}
=> ["stedolan", "jq", "wikiflow"]
jq ´[ .[] | . * 2]´
   [1, 2, 3]
=> [2, 4, 6]
```


## Object Construction: {}

Like JSON, **{}** is for constructing objects (aka dictionaries or hashes), as in: **{"a": 42, "b": 17}**.

If the keys are "identifier-like", then the quotes can be left off, as in **{a:42, b:17}**. Variable references as key expressions use the value of the variable as the key. Key expressions other than constant literals, identifiers, or variable references, need to be parenthesized, e.g., **{("a"+"b"):59}**.

The value can be any expression (although you may need to wrap it in parentheses if, for example, it contains colons), which gets applied to the {} expression´s input (remember, all filters have an input and an output).

```
{foo: .bar}
```

will produce the JSON object **{"foo": 42}** if given the JSON object **{"bar":42, "baz":43}** as its input. You can use this to select particular fields of an object: if the input is an object with "user", "title", "id", and "content" fields and you just want "user" and "title", you can write

```
{user: .user, title: .title}
```

Because that is so common, there´s a shortcut syntax for it: **{user, title}**.

If one of the expressions produces multiple results, multiple dictionaries will be produced. If the input´s

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

Variable references as keys use the value of the variable as the key. Without a value then the variable´s name becomes the key and its value becomes the value,

```
"f o o" as $foo | "b a r" as $bar | {$foo, $bar:$foo}
```

produces

```
{"foo":"f o o","b a r":"f o o"}
jq ´{user, title: .titles[]}´
   {"user":"stedolan","titles":["JQ Primer", "More JQ"]}
=> {"user":"stedolan", "title": "JQ Primer"}, {"user":"stedolan", "title": "More JQ"}
jq ´{(.user): .titles}´
   {"user":"stedolan","titles":["JQ Primer", "More JQ"]}
=> {"stedolan": ["JQ Primer", "More JQ"]}
```


## Recursive Descent: ..

Recursively descends **.**, producing every value. This is the same as the zero-argument **recurse** builtin (see below). This is intended to resemble the XPath **//** operator. Note that **..a** does not work; use **.. | .a** instead. In the example below we use **.. | .a?** to find all the values of object keys "a" in any object found "below" **.**.

This is particularly useful in conjunction with **path(EXP)** (also see below) and the **?** operator.

```
jq ´.. | .a?´
   [[{"a":1}]]
=> 1
```

# BUILTIN OPERATORS AND FUNCTIONS

Some jq operators (for instance, **+**) do different things depending on the type of their arguments (arrays, numbers, etc.). However, jq never does implicit type conversions. If you try to add a string to an object you´ll get an error message and no result.

Please note that all numbers are converted to IEEE754 double precision floating point representation. Arithmetic and logical operators are working with these converted doubles. Results of all such operations are also limited to the double precision.

The only exception to this behaviour of number is a snapshot of original number literal. When a number which originally was provided as a literal is never mutated until the end of the program then it is printed to the output in its original literal form. This also includes cases when the original literal would be truncated when converted to the IEEE754 double precision floating point number.


## Addition: +

The operator **+** takes two filters, applies them both to the same input, and adds the results together. What "adding" means depends on the types involved:

- **Numbers** are added by normal arithmetic.
- **Arrays** are added by being concatenated into a larger array.
- **Strings** are added by being joined into a larger string.
- **Objects** are added by merging, that is, inserting all the key-value pairs from both objects into a single combined object. If both objects contain a value for the same key, the object on the right of the **+** wins. (For recursive merge use the ***** operator.)

**null** can be added to any value, and returns the other value unchanged.

```
jq ´.a + 1´
   {"a": 7}
=> 8
jq ´.a + .b´
   {"a": [1,2], "b": [3,4]}
=> [1,2,3,4]
jq ´.a + null´
   {"a": 1}
=> 1
jq ´.a + 1´
   {}
=> 1
jq ´{a: 1} + {b: 2} + {c: 3} + {a: 42}´
   null
=> {"a": 42, "b": 2, "c": 3}
```


## Subtraction: -

As well as normal arithmetic subtraction on numbers, the **-** operator can be used on arrays to remove all occurrences of the second array´s elements from the first array.

```
jq ´4 - .a´
   {"a":3}
=> 1
jq ´. - ["xml", "yaml"]´
   ["xml", "yaml", "json"]
=> ["json"]
```


## Multiplication, division, modulo: *, /, %

These infix operators behave as expected when given two numbers. Division by zero raises an error. **x % y** computes x modulo y.

Multiplying a string by a number produces the concatenation of that string that many times. **"x" * 0** produces **""**.

Dividing a string by another splits the first using the second as separators.

Multiplying two objects will merge them recursively: this works like addition but if both objects contain a value for the same key, and the values are objects, the two are merged with the same strategy.

```
jq ´10 / . * 3´
   5
=> 6
jq ´. / ", "´
   "a, b,c,d, e"
=> ["a","b,c,d","e"]
jq ´{"k": {"a": 1, "b": 2}} * {"k": {"a": 0,"c": 3}}´
   null
=> {"k": {"a": 0, "b": 2, "c": 3}}
jq ´.[] | (1 / .)?´
   [1,0,-1]
=> 1, -1
```


## abs

The builtin function **abs** is defined naively as: **if . < 0 then - . else . end**.

For numeric input, this is the absolute value. See the section on the identity filter for the implications of this definition for numeric input.

To compute the absolute value of a number as a floating point number, you may wish use **fabs**.

```
jq ´map(abs)´
   [-10, -1.1, -1e-1]
=> [10,1.1,1e-1]
```


## length

The builtin function **length** gets the length of various different types of value:

- The length of a **string** is the number of Unicode codepoints it contains (which will be the same as its JSON-encoded length in bytes if it´s pure ASCII).
- The length of a **number** is its absolute value.
- The length of an **array** is the number of elements.
- The length of an **object** is the number of key-value pairs.
- The length of **null** is zero.
- It is an error to use **length** on a **boolean**.

```
jq ´.[] | length´
   [[1,2], "string", {"a":2}, null, -5]
=> 2, 6, 1, 0, 5
```


## utf8bytelength

The builtin function **utf8bytelength** outputs the number of bytes used to encode a string in UTF-8.

```
jq ´utf8bytelength´
   "\u03bc"
=> 2
```


## keys, keys_unsorted

The builtin function **keys**, when given an object, returns its keys in an array.

The keys are sorted "alphabetically", by unicode codepoint order. This is not an order that makes particular sense in any particular language, but you can count on it being the same for any two objects with the same set of keys, regardless of locale settings.

When **keys** is given an array, it returns the valid indices for that array: the integers from 0 to length-1.

The **keys_unsorted** function is just like **keys**, but if the input is an object then the keys will not be sorted, instead the keys will roughly be in insertion order.

```
jq ´keys´
   {"abc": 1, "abcd": 2, "Foo": 3}
=> ["Foo", "abc", "abcd"]
jq ´keys´
   [42,3,35]
=> [0,1,2]
```


## has(key)

The builtin function **has** returns whether the input object has the given key, or the input array has an element at the given index.

**has($key)** has the same effect as checking whether **$key** is a member of the array returned by **keys**, although **has** will be faster.

```
jq ´map(has("foo"))´
   [{"foo": 42}, {}]
=> [true, false]
jq ´map(has(2))´
   [[0,1], ["a","b","c"]]
=> [false, true]
```


## in

The builtin function **in** returns whether or not the input key is in the given object, or the input index corresponds to an element in the given array. It is, essentially, an inversed version of **has**.

```
jq ´.[] | in({"foo": 42})´
   ["foo", "bar"]
=> true, false
jq ´map(in([0,1]))´
   [2, 0]
=> [false, true]
```


## map(f), map_values(f)

For any filter **f**, **map(f)** and **map_values(f)** apply **f** to each of the values in the input array or object, that is, to the values of **.[]**.

In the absence of errors, **map(f)** always outputs an array whereas **map_values(f)** outputs an array if given an array, or an object if given an object.

When the input to **map_values(f)** is an object, the output object has the same keys as the input object except for those keys whose values when piped to **f** produce no values at all.

The key difference between **map(f)** and **map_values(f)** is that the former simply forms an array from all the values of **($x|f)** for each value, **$x**, in the input array or object, but **map_values(f)** only uses **first($x|f)**.

Specifically, for object inputs, **map_values(f)** constructs the output object by examining in turn the value of **first(.[$k]|f)** for each key, **$k**, of the input. If this expression produces no values, then the corresponding key will be dropped; otherwise, the output object will have that value at the key, **$k**.

Here are some examples to clarify the behavior of **map** and **map_values** when applied to arrays. These examples assume the input is **[1]** in all cases:

```
map(.+1)          #=>  [2]
map(., .)         #=>  [1,1]
map(empty)        #=>  []
map_values(.+1)   #=>  [2]
map_values(., .)  #=>  [1]
map_values(empty) #=>  []
```

**map(f)** is equivalent to **[.[] | f]** and **map_values(f)** is equivalent to **.[] |= f**.

In fact, these are their implementations.

```
jq ´map(.+1)´
   [1,2,3]
=> [2,3,4]
jq ´map_values(.+1)´
   {"a": 1, "b": 2, "c": 3}
=> {"a": 2, "b": 3, "c": 4}
jq ´map(., .)´
   [1,2]
=> [1,1,2,2]
jq ´map_values(. // empty)´
   {"a": null, "b": true, "c": false}
=> {"b":true}
```


## pick(pathexps)

Emit the projection of the input object or array defined by the specified sequence of path expressions, such that if **p** is any one of these specifications, then **(. | p)** will evaluate to the same value as **(. | pick(pathexps) | p)**. For arrays, negative indices and **.[m:n]** specifications should not be used.

```
jq ´pick(.a, .b.c, .x)´
   {"a": 1, "b": {"c": 2, "d": 3}, "e": 4}
=> {"a":1,"b":{"c":2},"x":null}
jq ´pick(.[2], .[0], .[0])´
   [1,2,3,4]
=> [1,null,3]
```


## path(path_expression)

Outputs array representations of the given path expression in **.**. The outputs are arrays of strings (object keys) and/or numbers (array indices).

Path expressions are jq expressions like **.a**, but also **.[]**. There are two types of path expressions: ones that can match exactly, and ones that cannot. For example, **.a.b.c** is an exact match path expression, while **.a[].b** is not.

**path(exact_path_expression)** will produce the array representation of the path expression even if it does not exist in **.**, if **.** is **null** or an array or an object.

**path(pattern)** will produce array representations of the paths matching **pattern** if the paths exist in **.**.

Note that the path expressions are not different from normal expressions. The expression **path(..|select(type=="boolean"))** outputs all the paths to boolean values in **.**, and only those paths.

```
jq ´path(.a[0].b)´
   null
=> ["a",0,"b"]
jq ´[path(..)]´
   {"a":[{"b":1}]}
=> [[],["a"],["a",0],["a",0,"b"]]
```


## del(path_expression)

The builtin function **del** removes a key and its corresponding value from an object.

```
jq ´del(.foo)´
   {"foo": 42, "bar": 9001, "baz": 42}
=> {"bar": 9001, "baz": 42}
jq ´del(.[1, 2])´
   ["foo", "bar", "baz"]
=> ["foo"]
```


## getpath(PATHS)

The builtin function **getpath** outputs the values in **.** found at each path in **PATHS**.

```
jq ´getpath(["a","b"])´
   null
=> null
jq ´[getpath(["a","b"], ["a","c"])]´
   {"a":{"b":0, "c":1}}
=> [0, 1]
```


## setpath(PATHS; VALUE)

The builtin function **setpath** sets the **PATHS** in **.** to **VALUE**.

```
jq ´setpath(["a","b"]; 1)´
   null
=> {"a": {"b": 1}}
jq ´setpath(["a","b"]; 1)´
   {"a":{"b":0}}
=> {"a": {"b": 1}}
jq ´setpath([0,"a"]; 1)´
   null
=> [{"a":1}]
```


## delpaths(PATHS)

The builtin function **delpaths** deletes the **PATHS** in **.**. **PATHS** must be an array of paths, where each path is an array of strings and numbers.

```
jq ´delpaths([["a","b"]])´
   {"a":{"b":1},"x":{"y":2}}
=> {"a":{},"x":{"y":2}}
```


## to_entries, from_entries, with_entries(f)

These functions convert between an object and an array of key-value pairs. If **to_entries** is passed an object, then for each **k: v** entry in the input, the output array includes **{"key": k, "value": v}**.

**from_entries** does the opposite conversion, and **with_entries(f)** is a shorthand for **to_entries | map(f) | from_entries**, useful for doing some operation to all keys and values of an object. **from_entries** accepts **"key"**, **"Key"**, **"name"**, **"Name"**, **"value"**, and **"Value"** as keys.

```
jq ´to_entries´
   {"a": 1, "b": 2}
=> [{"key":"a", "value":1}, {"key":"b", "value":2}]
jq ´from_entries´
   [{"key":"a", "value":1}, {"key":"b", "value":2}]
=> {"a": 1, "b": 2}
jq ´with_entries(.key |= "KEY_" + .)´
   {"a": 1, "b": 2}
=> {"KEY_a": 1, "KEY_b": 2}
```


## select(boolean_expression)

The function **select(f)** produces its input unchanged if **f** returns true for that input, and produces no output otherwise.

It´s useful for filtering lists: **[1,2,3] | map(select(. >= 2))** will give you **[2,3]**.

```
jq ´map(select(. >= 2))´
   [1,5,3,0,7]
=> [5,3,7]
jq ´.[] | select(.id == "second")´
   [{"id": "first", "val": 1}, {"id": "second", "val": 2}]
=> {"id": "second", "val": 2}
```


## arrays, objects, iterables, booleans, numbers, normals, finites, strings, nulls, values, scalars

These built-ins select only inputs that are arrays, objects, iterables (arrays or objects), booleans, numbers, normal numbers, finite numbers, strings, null, non-null values, and non-iterables, respectively.

```
jq ´.[]|numbers´
   [[],{},1,"foo",null,true,false]
=> 1
```


## empty

**empty** returns no results. None at all. Not even **null**.

It´s useful on occasion. You´ll know if you need it :)

```
jq ´1, empty, 2´
   null
=> 1, 2
jq ´[1,2,empty,3]´
   null
=> [1,2,3]
```


## error, error(message)

Produces an error with the input value, or with the message given as the argument. Errors can be caught with try/catch; see below.

```
jq ´try error catch .´
   "error message"
=> "error message"
jq ´try error("invalid value: \(.)") catch .´
   42
=> "invalid value: 42"
```


## halt

Stops the jq program with no further outputs. jq will exit with exit status **0**.


## halt_error, halt_error(exit_code)

Stops the jq program with no further outputs. The input will be printed on **stderr** as raw output (i.e., strings will not have double quotes) with no decoration, not even a newline.

The given **exit_code** (defaulting to **5**) will be jq´s exit status.

For example, **"Error: something went wrong\n"|halt_error(1)**.


## $__loc__

Produces an object with a "file" key and a "line" key, with the filename and line number where **$__loc__** occurs, as values.

```
jq ´try error("\($__loc__)") catch .´
   null
=> "{\"file\":\"<top-level>\",\"line\":1}"
```


## paths, paths(node_filter)

**paths** outputs the paths to all the elements in its input (except it does not output the empty list, representing . itself).

**paths(f)** outputs the paths to any values for which **f** is **true**. That is, **paths(type == "number")** outputs the paths to all numeric values.

```
jq ´[paths]´
   [1,[[],{"a":2}]]
=> [[0],[1],[1,0],[1,1],[1,1,"a"]]
jq ´[paths(type == "number")]´
   [1,[[],{"a":2}]]
=> [[0],[1,1,"a"]]
```


## add, add(generator)

The filter **add** takes as input an array, and produces as output the elements of the array added together. This might mean summed, concatenated or merged depending on the types of the elements of the input array - the rules are the same as those for the **+** operator (described above).

If the input is an empty array, **add** returns **null**.

**add(generator)** operates on the given generator rather than the input.

```
jq ´add´
   ["a","b","c"]
=> "abc"
jq ´add´
   [1, 2, 3]
=> 6
jq ´add´
   []
=> null
jq ´add(.[].a)´
   [{"a":3}, {"a":5}, {"b":6}]
=> 8
```


## any, any(condition), any(generator; condition)

The filter **any** takes as input an array of boolean values, and produces **true** as output if any of the elements of the array are **true**.

If the input is an empty array, **any** returns **false**.

The **any(condition)** form applies the given condition to the elements of the input array.

The **any(generator; condition)** form applies the given condition to all the outputs of the given generator.

```
jq ´any´
   [true, false]
=> true
jq ´any´
   [false, false]
=> false
jq ´any´
   []
=> false
```


## all, all(condition), all(generator; condition)

The filter **all** takes as input an array of boolean values, and produces **true** as output if all of the elements of the array are **true**.

The **all(condition)** form applies the given condition to the elements of the input array.

The **all(generator; condition)** form applies the given condition to all the outputs of the given generator.

If the input is an empty array, **all** returns **true**.

```
jq ´all´
   [true, false]
=> false
jq ´all´
   [true, true]
=> true
jq ´all´
   []
=> true
```


## flatten, flatten(depth)

The filter **flatten** takes as input an array of nested arrays, and produces a flat array in which all arrays inside the original array have been recursively replaced by their values. You can pass an argument to it to specify how many levels of nesting to flatten.

flatten(2) is like **flatten**, but going only up to two levels deep.

```
jq ´flatten´
   [1, [2], [[3]]]
=> [1, 2, 3]
jq ´flatten(1)´
   [1, [2], [[3]]]
=> [1, 2, [3]]
jq ´flatten´
   [[]]
=> []
jq ´flatten´
   [{"foo": "bar"}, [{"foo": "baz"}]]
=> [{"foo": "bar"}, {"foo": "baz"}]
```


## range(upto), range(from; upto), range(from; upto; by)

The **range** function produces a range of numbers. **range(4; 10)** produces 6 numbers, from 4 (inclusive) to 10 (exclusive). The numbers are produced as separate outputs. Use **[range(4; 10)]** to get a range as an array.

The one argument form generates numbers from 0 to the given number, with an increment of 1.

The two argument form generates numbers from **from** to **upto** with an increment of 1.

The three argument form generates numbers **from** to **upto** with an increment of **by**.

```
jq ´range(2; 4)´
   null
=> 2, 3
jq ´[range(2; 4)]´
   null
=> [2,3]
jq ´[range(4)]´
   null
=> [0,1,2,3]
jq ´[range(0; 10; 3)]´
   null
=> [0,3,6,9]
jq ´[range(0; 10; -1)]´
   null
=> []
jq ´[range(0; -5; -1)]´
   null
=> [0,-1,-2,-3,-4]
```


## floor

The **floor** function returns the floor of its numeric input.

```
jq ´floor´
   3.14159
=> 3
```


## sqrt

The **sqrt** function returns the square root of its numeric input.

```
jq ´sqrt´
   9
=> 3
```


## tonumber

The **tonumber** function parses its input as a number. It will convert correctly-formatted strings to their numeric equivalent, leave numbers alone, and give an error on all other input.

```
jq ´.[] | tonumber´
   [1, "1"]
=> 1, 1
```


## toboolean

The **toboolean** function parses its input as a boolean. It will convert correctly-formatted strings to their boolean equivalent, leave booleans alone, and give an error on all other input.

```
jq ´.[] | toboolean´
   ["true", "false", true, false]
=> true, false, true, false
```


## tostring

The **tostring** function prints its input as a string. Strings are left unchanged, and all other values are JSON-encoded.

```
jq ´.[] | tostring´
   [1, "1", [1]]
=> "1", "1", "[1]"
```


## type

The **type** function returns the type of its argument as a string, which is one of null, boolean, number, string, array or object.

```
jq ´map(type)´
   [0, false, [], {}, null, "hello"]
=> ["number", "boolean", "array", "object", "null", "string"]
```


## infinite, nan, isinfinite, isnan, isfinite, isnormal

Some arithmetic operations can yield infinities and "not a number" (NaN) values. The **isinfinite** builtin returns **true** if its input is infinite. The **isnan** builtin returns **true** if its input is a NaN. The **infinite** builtin returns a positive infinite value. The **nan** builtin returns a NaN. The **isnormal** builtin returns true if its input is a normal number.

Note that division by zero raises an error.

Currently most arithmetic operations operating on infinities, NaNs, and sub-normals do not raise errors.

```
jq ´.[] | (infinite * .) < 0´
   [-1, 1]
=> true, false
jq ´infinite, nan | type´
   null
=> "number", "number"
```


## sort, sort_by(path_expression)

The **sort** functions sorts its input, which must be an array. Values are sorted in the following order:

- **null**
- **false**
- **true**
- numbers
- strings, in alphabetical order (by unicode codepoint value)
- arrays, in lexical order
- objects

The ordering for objects is a little complex: first they´re compared by comparing their sets of keys (as arrays in sorted order), and if their keys are equal then the values are compared key by key.

**sort_by** may be used to sort by a particular field of an object, or by applying any jq filter. **sort_by(f)** compares two elements by comparing the result of **f** on each element. When **f** produces multiple values, it firstly compares the first values, and the second values if the first values are equal, and so on.

```
jq ´sort´
   [8,3,null,6]
=> [null,3,6,8]
jq ´sort_by(.foo)´
   [{"foo":4, "bar":10}, {"foo":3, "bar":10}, {"foo":2, "bar":1}]
=> [{"foo":2, "bar":1}, {"foo":3, "bar":10}, {"foo":4, "bar":10}]
jq ´sort_by(.foo, .bar)´
   [{"foo":4, "bar":10}, {"foo":3, "bar":20}, {"foo":2, "bar":1}, {"foo":3, "bar":10}]
=> [{"foo":2, "bar":1}, {"foo":3, "bar":10}, {"foo":3, "bar":20}, {"foo":4, "bar":10}]
```


## group_by(path_expression)

**group_by(.foo)** takes as input an array, groups the elements having the same **.foo** field into separate arrays, and produces all of these arrays as elements of a larger array, sorted by the value of the **.foo** field.

Any jq expression, not just a field access, may be used in place of **.foo**. The sorting order is the same as described in the **sort** function above.

```
jq ´group_by(.foo)´
   [{"foo":1, "bar":10}, {"foo":3, "bar":100}, {"foo":1, "bar":1}]
=> [[{"foo":1, "bar":10}, {"foo":1, "bar":1}], [{"foo":3, "bar":100}]]
```


## min, max, min_by(path_exp), max_by(path_exp)

Find the minimum or maximum element of the input array.

The **min_by(path_exp)** and **max_by(path_exp)** functions allow you to specify a particular field or property to examine, e.g. **min_by(.foo)** finds the object with the smallest **foo** field.

```
jq ´min´
   [5,4,2,7]
=> 2
jq ´max_by(.foo)´
   [{"foo":1, "bar":14}, {"foo":2, "bar":3}]
=> {"foo":2, "bar":3}
```


## unique, unique_by(path_exp)

The **unique** function takes as input an array and produces an array of the same elements, in sorted order, with duplicates removed.

The **unique_by(path_exp)** function will keep only one element for each value obtained by applying the argument. Think of it as making an array by taking one element out of every group produced by **group**.

```
jq ´unique´
   [1,2,5,3,5,3,1,3]
=> [1,2,3,5]
jq ´unique_by(.foo)´
   [{"foo": 1, "bar": 2}, {"foo": 1, "bar": 3}, {"foo": 4, "bar": 5}]
=> [{"foo": 1, "bar": 2}, {"foo": 4, "bar": 5}]
jq ´unique_by(length)´
   ["chunky", "bacon", "kitten", "cicada", "asparagus"]
=> ["bacon", "chunky", "asparagus"]
```


## reverse

This function reverses an array.

```
jq ´reverse´
   [1,2,3,4]
=> [4,3,2,1]
```


## contains(element)

The filter **contains(b)** will produce true if b is completely contained within the input. A string B is contained in a string A if B is a substring of A. An array B is contained in an array A if all elements in B are contained in any element in A. An object B is contained in object A if all of the values in B are contained in the value in A with the same key. All other types are assumed to be contained in each other if they are equal.

```
jq ´contains("bar")´
   "foobar"
=> true
jq ´contains(["baz", "bar"])´
   ["foobar", "foobaz", "blarp"]
=> true
jq ´contains(["bazzzzz", "bar"])´
   ["foobar", "foobaz", "blarp"]
=> false
jq ´contains({foo: 12, bar: [{barp: 12}]})´
   {"foo": 12, "bar":[1,2,{"barp":12, "blip":13}]}
=> true
jq ´contains({foo: 12, bar: [{barp: 15}]})´
   {"foo": 12, "bar":[1,2,{"barp":12, "blip":13}]}
=> false
```


## indices(s)

Outputs an array containing the indices in **.** where **s** occurs. The input may be an array, in which case if **s** is an array then the indices output will be those where all elements in **.** match those of **s**.

```
jq ´indices(", ")´
   "a,b, cd, efg, hijk"
=> [3,7,12]
jq ´indices(1)´
   [0,1,2,1,3,1,4]
=> [1,3,5]
jq ´indices([1,2])´
   [0,1,2,3,1,4,2,5,1,2,6,7]
=> [1,8]
```


## index(s), rindex(s)

Outputs the index of the first (**index**) or last (**rindex**) occurrence of **s** in the input.

```
jq ´index(", ")´
   "a,b, cd, efg, hijk"
=> 3
jq ´index(1)´
   [0,1,2,1,3,1,4]
=> 1
jq ´index([1,2])´
   [0,1,2,3,1,4,2,5,1,2,6,7]
=> 1
jq ´rindex(", ")´
   "a,b, cd, efg, hijk"
=> 12
jq ´rindex(1)´
   [0,1,2,1,3,1,4]
=> 5
jq ´rindex([1,2])´
   [0,1,2,3,1,4,2,5,1,2,6,7]
=> 8
```
