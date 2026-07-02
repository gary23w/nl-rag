---
title: "jq(1) (part 2/3)"
source: https://man.archlinux.org/man/jq.1
domain: jq-json
license: CC-BY-SA-4.0
tags: jq json, json processor, command-line json, json filter
fetched: 2026-07-02
part: 2/3
---

## inside

The filter **inside(b)** will produce true if the input is completely contained within b. It is, essentially, an inversed version of **contains**.

```
jq ´inside("foobar")´
   "bar"
=> true
jq ´inside(["foobar", "foobaz", "blarp"])´
   ["baz", "bar"]
=> true
jq ´inside(["foobar", "foobaz", "blarp"])´
   ["bazzzzz", "bar"]
=> false
jq ´inside({"foo": 12, "bar":[1,2,{"barp":12, "blip":13}]})´
   {"foo": 12, "bar": [{"barp": 12}]}
=> true
jq ´inside({"foo": 12, "bar":[1,2,{"barp":12, "blip":13}]})´
   {"foo": 12, "bar": [{"barp": 15}]}
=> false
```


## startswith(str)

Outputs **true** if . starts with the given string argument.

```
jq ´[.[]|startswith("foo")]´
   ["fo", "foo", "barfoo", "foobar", "barfoob"]
=> [false, true, false, true, false]
```


## endswith(str)

Outputs **true** if . ends with the given string argument.

```
jq ´[.[]|endswith("foo")]´
   ["foobar", "barfoo"]
=> [false, true]
```


## combinations, combinations(n)

Outputs all combinations of the elements of the arrays in the input array. If given an argument **n**, it outputs all combinations of **n** repetitions of the input array.

```
jq ´combinations´
   [[1,2], [3, 4]]
=> [1, 3], [1, 4], [2, 3], [2, 4]
jq ´combinations(2)´
   [0, 1]
=> [0, 0], [0, 1], [1, 0], [1, 1]
```


## ltrimstr(str)

Outputs its input with the given prefix string removed, if it starts with it.

```
jq ´[.[]|ltrimstr("foo")]´
   ["fo", "foo", "barfoo", "foobar", "afoo"]
=> ["fo","","barfoo","bar","afoo"]
```


## rtrimstr(str)

Outputs its input with the given suffix string removed, if it ends with it.

```
jq ´[.[]|rtrimstr("foo")]´
   ["fo", "foo", "barfoo", "foobar", "foob"]
=> ["fo","","bar","foobar","foob"]
```


## trimstr(str)

Outputs its input with the given string removed at both ends, if it starts or ends with it.

```
jq ´[.[]|trimstr("foo")]´
   ["fo", "foo", "barfoo", "foobarfoo", "foob"]
=> ["fo","","bar","bar","b"]
```


## trim, ltrim, rtrim

**trim** trims both leading and trailing whitespace.

**ltrim** trims only leading (left side) whitespace.

**rtrim** trims only trailing (right side) whitespace.

Whitespace characters are the usual **" "**, **"\n"** **"\t"**, **"\r"** and also all characters in the Unicode character database with the whitespace property. Note that what considers whitespace might change in the future.

```
jq ´trim, ltrim, rtrim´
   " abc "
=> "abc", "abc ", " abc"
```


## explode

Converts an input string into an array of the string´s codepoint numbers.

```
jq ´explode´
   "foobar"
=> [102,111,111,98,97,114]
```


## implode

The inverse of explode.

```
jq ´implode´
   [65, 66, 67]
=> "ABC"
```


## split(str)

Splits an input string on the separator argument.

**split** can also split on regex matches when called with two arguments (see the regular expressions section below).

```
jq ´split(", ")´
   "a, b,c,d, e, "
=> ["a","b,c,d","e",""]
```


## join(str)

Joins the array of elements given as input, using the argument as separator. It is the inverse of **split**: that is, running **split("foo") | join("foo")** over any input string returns said input string.

Numbers and booleans in the input are converted to strings. Null values are treated as empty strings. Arrays and objects in the input are not supported.

```
jq ´join(", ")´
   ["a","b,c,d","e"]
=> "a, b,c,d, e"
jq ´join(" ")´
   ["a",1,2.3,true,null,false]
=> "a 1 2.3 true  false"
```


## ascii_downcase, ascii_upcase

Emit a copy of the input string with its alphabetic characters (a-z and A-Z) converted to the specified case.

```
jq ´ascii_upcase´
   "useful but not for é"
=> "USEFUL BUT NOT FOR é"
```


## while(cond; update)

The **while(cond; update)** function allows you to repeatedly apply an update to **.** until **cond** is false.

Note that **while(cond; update)** is internally defined as a recursive jq function. Recursive calls within **while** will not consume additional memory if **update** produces at most one output for each input. See advanced topics below.

```
jq ´[while(.<100; .*2)]´
   1
=> [1,2,4,8,16,32,64]
```


## repeat(exp)

The **repeat(exp)** function allows you to repeatedly apply expression **exp** to **.** until an error is raised.

Note that **repeat(exp)** is internally defined as a recursive jq function. Recursive calls within **repeat** will not consume additional memory if **exp** produces at most one output for each input. See advanced topics below.

```
jq ´[repeat(.*2, error)?]´
   1
=> [2]
```


## until(cond; next)

The **until(cond; next)** function allows you to repeatedly apply the expression **next**, initially to **.** then to its own output, until **cond** is true. For example, this can be used to implement a factorial function (see below).

Note that **until(cond; next)** is internally defined as a recursive jq function. Recursive calls within **until()** will not consume additional memory if **next** produces at most one output for each input. See advanced topics below.

```
jq ´[.,1]|until(.[0] < 1; [.[0] - 1, .[1] * .[0]])|.[1]´
   4
=> 24
```


## recurse(f), recurse, recurse(f; condition)

The **recurse(f)** function allows you to search through a recursive structure, and extract interesting data from all levels. Suppose your input represents a filesystem:

```
{"name": "/", "children": [
  {"name": "/bin", "children": [
    {"name": "/bin/ls", "children": []},
    {"name": "/bin/sh", "children": []}]},
  {"name": "/home", "children": [
    {"name": "/home/stephen", "children": [
      {"name": "/home/stephen/jq", "children": []}]}]}]}
```

Now suppose you want to extract all of the filenames present. You need to retrieve **.name**, **.children[].name**, **.children[].children[].name**, and so on. You can do this with:

```
recurse(.children[]) | .name
```

When called without an argument, **recurse** is equivalent to **recurse(.[]?)**.

**recurse(f)** is identical to **recurse(f; true)** and can be used without concerns about recursion depth.

**recurse(f; condition)** is a generator which begins by emitting . and then emits in turn .|f, .|f|f, .|f|f|f, ... so long as the computed value satisfies the condition. For example, to generate all the integers, at least in principle, one could write **recurse(.+1; true)**.

The recursive calls in **recurse** will not consume additional memory whenever **f** produces at most a single output for each input.

```
jq ´recurse(.foo[])´
   {"foo":[{"foo": []}, {"foo":[{"foo":[]}]}]}
=> {"foo":[{"foo":[]},{"foo":[{"foo":[]}]}]}, {"foo":[]}, {"foo":[{"foo":[]}]}, {"foo":[]}
jq ´recurse´
   {"a":0,"b":[1]}
=> {"a":0,"b":[1]}, 0, [1], 1
jq ´recurse(. * .; . < 20)´
   2
=> 2, 4, 16
```


## walk(f)

The **walk(f)** function applies f recursively to every component of the input entity. When an array is encountered, f is first applied to its elements and then to the array itself; when an object is encountered, f is first applied to all the values and then to the object. In practice, f will usually test the type of its input, as illustrated in the following examples. The first example highlights the usefulness of processing the elements of an array of arrays before processing the array itself. The second example shows how all the keys of all the objects within the input can be considered for alteration.

```
jq ´walk(if type == "array" then sort else . end)´
   [[4, 1, 7], [8, 5, 2], [3, 6, 9]]
=> [[1,4,7],[2,5,8],[3,6,9]]
jq ´walk( if type == "object" then with_entries( .key |= sub( "^_+"; "") ) else . end )´
   [ { "_a": { "__b": 2 } } ]
=> [{"a":{"b":2}}]
```


## have_literal_numbers

This builtin returns true if jq´s build configuration includes support for preservation of input number literals.


## have_decnum

This builtin returns true if jq was built with "decnum", which is the current literal number preserving numeric backend implementation for jq.


## $JQ_BUILD_CONFIGURATION

This builtin binding shows the jq executable´s build configuration. Its value has no particular format, but it can be expected to be at least the **./configure** command-line arguments, and may be enriched in the future to include the version strings for the build tooling used.

Note that this can be overridden in the command-line with **--arg** and related options.


## $ENV, env

**$ENV** is an object representing the environment variables as set when the jq program started.

**env** outputs an object representing jq´s current environment.

At the moment there is no builtin for setting environment variables.

```
jq ´$ENV.PAGER´
   null
=> "less"
jq ´env.PAGER´
   null
=> "less"
```


## transpose

Transpose a possibly jagged matrix (an array of arrays). Rows are padded with nulls so the result is always rectangular.

```
jq ´transpose´
   [[1], [2,3]]
=> [[1,2],[null,3]]
```


## bsearch(x)

**bsearch(x)** conducts a binary search for x in the input array. If the input is sorted and contains x, then **bsearch(x)** will return its index in the array; otherwise, if the array is sorted, it will return (-1 - ix) where ix is an insertion point such that the array would still be sorted after the insertion of x at ix. If the array is not sorted, **bsearch(x)** will return an integer that is probably of no interest.

```
jq ´bsearch(0)´
   [0,1]
=> 0
jq ´bsearch(0)´
   [1,2,3]
=> -1
jq ´bsearch(4) as $ix | if $ix < 0 then .[-(1+$ix)] = 4 else . end´
   [1,2,3]
=> [1,2,3,4]
```


## String interpolation: \(exp)

Inside a string, you can put an expression inside parens after a backslash. Whatever the expression returns will be interpolated into the string.

```
jq ´"The input was \(.), which is one less than \(.+1)"´
   42
=> "The input was 42, which is one less than 43"
```


## Convert to/from JSON

The **tojson** and **fromjson** builtins dump values as JSON texts or parse JSON texts into values, respectively. The **tojson** builtin differs from **tostring** in that **tostring** returns strings unmodified, while **tojson** encodes strings as JSON strings.

```
jq ´[.[]|tostring]´
   [1, "foo", ["foo"]]
=> ["1","foo","[\"foo\"]"]
jq ´[.[]|tojson]´
   [1, "foo", ["foo"]]
=> ["1","\"foo\"","[\"foo\"]"]
jq ´[.[]|tojson|fromjson]´
   [1, "foo", ["foo"]]
=> [1,"foo",["foo"]]
```


## Format strings and escaping

The **@foo** syntax is used to format and escape strings, which is useful for building URLs, documents in a language like HTML or XML, and so forth. **@foo** can be used as a filter on its own, the possible escapings are:

****@text**:**

Calls

tostring

, see that function for details.

****@json**:**

Serializes the input as JSON.

****@html**:**

Applies HTML/XML escaping, by mapping the characters

<>&´"

to their entity equivalents

&lt;

,

&gt;

,

&amp;

,

&apos;

,

&quot;

.

****@uri**:**

Applies percent-encoding, by mapping all reserved URI characters to a

%XX

sequence.

****@urid**:**

The inverse of

@uri

, applies percent-decoding, by mapping all

%XX

sequences to their corresponding URI characters.

****@csv**:**

The input must be an array, and it is rendered as CSV with double quotes for strings, and quotes escaped by repetition.

****@tsv**:**

The input must be an array, and it is rendered as TSV (tab-separated values). Each input array will be printed as a single line. Fields are separated by a single tab (ascii

0x09

). Input characters line-feed (ascii

0x0a

), carriage-return (ascii

0x0d

), tab (ascii

0x09

) and backslash (ascii

0x5c

) will be output as escape sequences

\n

,

\r

,

\t

,

\\

respectively.

****@sh**:**

The input is escaped suitable for use in a command-line for a POSIX shell. If the input is an array, the output will be a series of space-separated strings.

****@base64**:**

The input is converted to base64 as specified by RFC 4648.

****@base64d**:**

The inverse of

@base64

, input is decoded as specified by RFC 4648. Note\: If the decoded string is not UTF-8, the results are undefined.

This syntax can be combined with string interpolation in a useful way. You can follow a **@foo** token with a string literal. The contents of the string literal will *not* be escaped. However, all interpolations made inside that string literal will be escaped. For instance,

```
@uri "https://www.google.com/search?q=\(.search)"
```

will produce the following output for the input **{"search":"what is jq?"}**:

```
"https://www.google.com/search?q=what%20is%20jq%3F"
```

Note that the slashes, question mark, etc. in the URL are not escaped, as they were part of the string literal.

```
jq ´@html´
   "This works if x < y"
=> "This works if x &lt; y"
jq ´@sh "echo \(.)"´
   "O´Hara´s Ale"
=> "echo ´O´\\´´Hara´\\´´s Ale´"
jq ´@base64´
   "This is a message"
=> "VGhpcyBpcyBhIG1lc3NhZ2U="
jq ´@base64d´
   "VGhpcyBpcyBhIG1lc3NhZ2U="
=> "This is a message"
```


## Dates

jq provides some basic date handling functionality, with some high-level and low-level builtins. In all cases these builtins deal exclusively with time in UTC.

The **fromdateiso8601** builtin parses datetimes in the ISO 8601 format to a number of seconds since the Unix epoch (1970-01-01T00:00:00Z). The **todateiso8601** builtin does the inverse.

The **fromdate** builtin parses datetime strings. Currently **fromdate** only supports ISO 8601 datetime strings, but in the future it will attempt to parse datetime strings in more formats.

The **todate** builtin is an alias for **todateiso8601**.

The **now** builtin outputs the current time, in seconds since the Unix epoch.

Low-level jq interfaces to the C-library time functions are also provided: **strptime**, **strftime**, **strflocaltime**, **mktime**, **gmtime**, and **localtime**. Refer to your host operating system´s documentation for the format strings used by **strptime** and **strftime**. Note: these are not necessarily stable interfaces in jq, particularly as to their localization functionality.

The **gmtime** builtin consumes a number of seconds since the Unix epoch and outputs a "broken down time" representation of Greenwich Mean Time as an array of numbers representing (in this order): the year, the month (zero-based), the day of the month (one-based), the hour of the day, the minute of the hour, the second of the minute, the day of the week, and the day of the year -- all one-based unless otherwise stated. The day of the week number may be wrong on some systems for dates before March 1st 1900, or after December 31 2099.

The **localtime** builtin works like the **gmtime** builtin, but using the local timezone setting.

The **mktime** builtin consumes "broken down time" representations of time output by **gmtime** and **strptime**.

The **strptime(fmt)** builtin parses input strings matching the **fmt** argument. The output is in the "broken down time" representation consumed by **mktime** and output by **gmtime**.

The **strftime(fmt)** builtin formats a time (GMT) with the given format. The **strflocaltime** does the same, but using the local timezone setting.

The format strings for **strptime** and **strftime** are described in typical C library documentation. The format string for ISO 8601 datetime is **"%Y-%m-%dT%H:%M:%SZ"**.

jq may not support some or all of this date functionality on some systems. In particular, the **%u** and **%j** specifiers for **strptime(fmt)** are not supported on macOS.

```
jq ´fromdate´
   "2015-03-05T23:51:47Z"
=> 1425599507
jq ´strptime("%Y-%m-%dT%H:%M:%SZ")´
   "2015-03-05T23:51:47Z"
=> [2015,2,5,23,51,47,4,63]
jq ´strptime("%Y-%m-%dT%H:%M:%SZ")|mktime´
   "2015-03-05T23:51:47Z"
=> 1425599507
```


## SQL-Style Operators

jq provides a few SQL-style operators.

****INDEX(stream; index_expression)**:**

This builtin produces an object whose keys are computed by the given index expression applied to each value from the given stream.

****JOIN($idx; stream; idx_expr; join_expr)**:**

This builtin joins the values from the given stream to the given index. The index´s keys are computed by applying the given index expression to each value from the given stream. An array of the value in the stream and the corresponding value from the index is fed to the given join expression to produce each result.

****JOIN($idx; stream; idx_expr)**:**

Same as

JOIN($idx; stream; idx_expr; .)

.

****JOIN($idx; idx_expr)**:**

This builtin joins the input

.

to the given index, applying the given index expression to

.

to compute the index key. The join operation is as described above.

****IN(s)**:**

This builtin outputs

true

if

.

appears in the given stream, otherwise it outputs

false

.

****IN(source; s)**:**

This builtin outputs

true

if any value in the source stream appears in the second stream, otherwise it outputs

false

.


## builtins

Returns a list of all builtin functions in the format **name/arity**. Since functions with the same name but different arities are considered separate functions, **all/0**, **all/1**, and **all/2** would all be present in the list.

# CONDITIONALS AND COMPARISONS


## ==, !=

The expression ´a == b´ will produce ´true´ if the results of evaluating a and b are equal (that is, if they represent equivalent JSON values) and ´false´ otherwise. In particular, strings are never considered equal to numbers. In checking for the equality of JSON objects, the ordering of keys is irrelevant. If you´re coming from JavaScript, please note that jq´s **==** is like JavaScript´s **===**, the "strict equality" operator.

!= is "not equal", and ´a != b´ returns the opposite value of ´a == b´

```
jq ´. == false´
   null
=> false
jq ´. == {"b": {"d": (4 + 1e-20), "c": 3}, "a":1}´
   {"a":1, "b": {"c": 3, "d": 4}}
=> true
jq ´.[] == 1´
   [1, 1.0, "1", "banana"]
=> true, true, false, false
```


## if-then-else-end

**if A then B else C end** will act the same as **B** if **A** produces a value other than false or null, but act the same as **C** otherwise.

**if A then B end** is the same as **if A then B else . end**. That is, the **else** branch is optional, and if absent is the same as **.**. This also applies to **elif** with absent ending **else** branch.

Checking for false or null is a simpler notion of "truthiness" than is found in JavaScript or Python, but it means that you´ll sometimes have to be more explicit about the condition you want. You can´t test whether, e.g. a string is empty using **if .name then A else B end**; you´ll need something like **if .name == "" then A else B end** instead.

If the condition **A** produces multiple results, then **B** is evaluated once for each result that is not false or null, and **C** is evaluated once for each false or null.

More cases can be added to an if using **elif A then B** syntax.

```
jq ´if . == 0 then
  "zero"
elif . == 1 then
  "one"
else
  "many"
end´
   2
=> "many"
```


## >, >=, <=, <

The comparison operators **>**, **>=**, **<=**, **<** return whether their left argument is greater than, greater than or equal to, less than or equal to or less than their right argument (respectively).

The ordering is the same as that described for **sort**, above.

```
jq ´. < 5´
   2
=> true
```


## and, or, not

jq supports the normal Boolean operators **and**, **or**, **not**. They have the same standard of truth as if expressions - **false** and **null** are considered "false values", and anything else is a "true value".

If an operand of one of these operators produces multiple results, the operator itself will produce a result for each input.

**not** is in fact a builtin function rather than an operator, so it is called as a filter to which things can be piped rather than with special syntax, as in **.foo and .bar | not**.

These three only produce the values **true** and **false**, and so are only useful for genuine Boolean operations, rather than the common Perl/Python/Ruby idiom of "value_that_may_be_null or default". If you want to use this form of "or", picking between two values rather than evaluating a condition, see the **//** operator below.

```
jq ´42 and "a string"´
   null
=> true
jq ´(true, false) or false´
   null
=> true, false
jq ´(true, true) and (true, false)´
   null
=> true, false, true, false
jq ´[true, false | not]´
   null
=> [false, true]
```


## Alternative operator: //

The **//** operator produces all the values of its left-hand side that are neither **false** nor **null**. If the left-hand side produces no values other than **false** or **null**, then **//** produces all the values of its right-hand side.

A filter of the form **a // b** produces all the results of **a** that are not **false** or **null**. If **a** produces no results, or no results other than **false** or **null**, then **a // b** produces the results of **b**.

This is useful for providing defaults: **.foo // 1** will evaluate to **1** if there´s no **.foo** element in the input. It´s similar to how **or** is sometimes used in Python (jq´s **or** operator is reserved for strictly Boolean operations).

Note: **some_generator // defaults_here** is not the same as **some_generator | . // defaults_here**. The latter will produce default values for all non-**false**, non-**null** values of the left-hand side, while the former will not. Precedence rules can make this confusing. For example, in **false, 1 // 2** the left-hand side of **//** is **1**, not **false, 1** -- **false, 1 // 2** parses the same way as **false, (1 // 2)**. In **(false, null, 1) | . // 42** the left-hand side of **//** is **.**, which always produces just one value, while in **(false, null, 1) // 42** the left-hand side is a generator of three values, and since it produces a value other **false** and **null**, the default **42** is not produced.

```
jq ´empty // 42´
   null
=> 42
jq ´.foo // 42´
   {"foo": 19}
=> 19
jq ´.foo // 42´
   {}
=> 42
jq ´(false, null, 1) // 42´
   null
=> 1
jq ´(false, null, 1) | . // 42´
   null
=> 42, 42, 1
```


## try-catch

Errors can be caught by using **try EXP catch EXP**. The first expression is executed, and if it fails then the second is executed with the error message. The output of the handler, if any, is output as if it had been the output of the expression to try.

The **try EXP** form uses **empty** as the exception handler.

```
jq ´try .a catch ". is not an object"´
   true
=> ". is not an object"
jq ´[.[]|try .a]´
   [{}, true, {"a":1}]
=> [null, 1]
jq ´try error("some exception") catch .´
   true
=> "some exception"
```


## Breaking out of control structures

A convenient use of try/catch is to break out of control structures like **reduce**, **foreach**, **while**, and so on.

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

The **break $label_name** expression will cause the program to act as though the nearest (to the left) **label $label_name** produced **empty**.

The relationship between the **break** and corresponding **label** is lexical: the label has to be "visible" from the break.

To break out of a **reduce**, for example:

```
label $out | reduce .[] as $item (null; if .==false then break $out else ... end)
```

The following jq program produces a syntax error:

```
break $out
```

because no label **$out** is visible.


## Error Suppression / Optional Operator: ?

The **?** operator, used as **EXP?**, is shorthand for **try EXP**.

```
jq ´[.[] | .a?]´
   [{}, true, {"a":1}]
=> [null, 1]
jq ´[.[] | tonumber?]´
   ["1", "invalid", "3", 4]
=> [1, 3, 4]
```

# REGULAR EXPRESSIONS

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
- FILTER is one of **test**, **match**, or **capture**, as described below.

Since REGEX must evaluate to a JSON string, some characters that are needed to form a regular expression must be escaped. For example, the regular expression **\s** signifying a whitespace character would be written as **"\\s"**.

FLAGS is a string consisting of one of more of the supported flags:

- **g** - Global search (find all matches, not just the first)
- **i** - Case insensitive search
- **m** - Multi line mode (**.** will match newlines)
- **n** - Ignore empty matches
- **p** - Both s and m modes are enabled
- **s** - Single line mode (**^** -> **\A**, **$** -> **\Z**)
- **l** - Find longest possible matches
- **x** - Extended regex format (ignore whitespace and comments)

To match a whitespace with the **x** flag, use **\s**, e.g.

```
jq -n ´"a b" | test("a\\sb"; "x")´
```

Note that certain flags may also be specified within REGEX, e.g.

```
jq -n ´("test", "TEst", "teST", "TEST") | test("(?i)te(?-i)st")´
```

evaluates to: **true**, **true**, **false**, **false**.


## test(val), test(regex; flags)

Like **match**, but does not return match objects, only **true** or **false** for whether or not the regex matches the input.

```
jq ´test("foo")´
   "foo"
=> true
jq ´.[] | test("a b c # spaces are ignored"; "ix")´
   ["xabcd", "ABC"]
=> true, true
```


## match(val), match(regex; flags)

**match** outputs an object for each match it finds. Matches have the following fields:

- **offset** - offset in UTF-8 codepoints from the beginning of the input
- **length** - length in UTF-8 codepoints of the match
- **string** - the string that it matched
- **captures** - an array of objects representing capturing groups.

Capturing group objects have the following fields:

- **offset** - offset in UTF-8 codepoints from the beginning of the input
- **length** - length in UTF-8 codepoints of this capturing group
- **string** - the string that was captured
- **name** - the name of the capturing group (or **null** if it was unnamed)

Capturing groups that did not match anything return an offset of -1

```
jq ´match("(abc)+"; "g")´
   "abc abc"
=> {"offset": 0, "length": 3, "string": "abc", "captures": [{"offset": 0, "length": 3, "string": "abc", "name": null}]}, {"offset": 4, "length": 3, "string": "abc", "captures": [{"offset": 4, "length": 3, "string": "abc", "name": null}]}
jq ´match("foo")´
   "foo bar foo"
=> {"offset": 0, "length": 3, "string": "foo", "captures": []}
jq ´match(["foo", "ig"])´
   "foo bar FOO"
=> {"offset": 0, "length": 3, "string": "foo", "captures": []}, {"offset": 8, "length": 3, "string": "FOO", "captures": []}
jq ´match("foo (?<bar123>bar)? foo"; "ig")´
   "foo bar foo foo  foo"
=> {"offset": 0, "length": 11, "string": "foo bar foo", "captures": [{"offset": 4, "length": 3, "string": "bar", "name": "bar123"}]}, {"offset": 12, "length": 8, "string": "foo  foo", "captures": [{"offset": -1, "length": 0, "string": null, "name": "bar123"}]}
jq ´[ match("."; "g")] | length´
   "abc"
=> 3
```


## capture(val), capture(regex; flags)

Collects the named captures in a JSON object, with the name of each capture as the key, and the matched string as the corresponding value.

```
jq ´capture("(?<a>[a-z]+)-(?<n>[0-9]+)")´
   "xyzzy-14"
=> { "a": "xyzzy", "n": "14" }
```


## scan(regex), scan(regex; flags)

Emit a stream of the non-overlapping substrings of the input that match the regex in accordance with the flags, if any have been specified. If there is no match, the stream is empty. To capture all the matches for each input string, use the idiom **[ expr ]**, e.g. **[ scan(regex) ]**. If the regex contains capturing groups, the filter emits a stream of arrays, each of which contains the captured strings.

```
jq ´scan("c")´
   "abcdefabc"
=> "c", "c"
jq ´scan("(a+)(b+)")´
   "abaabbaaabbb"
=> ["a","b"], ["aa","bb"], ["aaa","bbb"]
```


## split(regex; flags)

Splits an input string on each regex match.

For backwards compatibility, when called with a single argument, **split** splits on a string, not a regex.

```
jq ´split(", *"; null)´
   "ab,cd, ef"
=> ["ab","cd","ef"]
```


## splits(regex), splits(regex; flags)

These provide the same results as their **split** counterparts, but as a stream instead of an array.

```
jq ´splits(", *")´
   "ab,cd,   ef, gh"
=> "ab", "cd", "ef", "gh"
jq ´splits(",? *"; "n")´
   "ab,cd ef,  gh"
=> "ab", "cd", "ef", "gh"
```


## sub(regex; tostring), sub(regex; tostring; flags)

Emit the string obtained by replacing the first match of regex in the input string with **tostring**, after interpolation. **tostring** should be a jq string or a stream of such strings, each of which may contain references to named captures. The named captures are, in effect, presented as a JSON object (as constructed by **capture**) to **tostring**, so a reference to a captured variable named "x" would take the form: **"\(.x)"**.

```
jq ´sub("[^a-z]*(?<x>[a-z]+)"; "Z\(.x)"; "g")´
   "123abc456def"
=> "ZabcZdef"
jq ´[sub("(?<a>.)"; "\(.a|ascii_upcase)", "\(.a|ascii_downcase)")]´
   "aB"
=> ["AB","aB"]
```


## gsub(regex; tostring), gsub(regex; tostring; flags)

**gsub** is like **sub** but all the non-overlapping occurrences of the regex are replaced by **tostring**, after interpolation. If the second argument is a stream of jq strings, then **gsub** will produce a corresponding stream of JSON strings.

```
jq ´gsub("(?<x>.)[^a]*"; "+\(.x)-")´
   "Abcabc"
=> "+A-+a-"
jq ´[gsub("p"; "a", "b")]´
   "p"
=> ["a","b"]
```

# ADVANCED FEATURES

Variables are an absolute necessity in most programming languages, but they´re relegated to an "advanced feature" in jq.

In most languages, variables are the only means of passing around data. If you calculate a value, and you want to use it more than once, you´ll need to store it in a variable. To pass a value to another part of the program, you´ll need that part of the program to define a variable (as a function parameter, object member, or whatever) in which to place the data.

It is also possible to define functions in jq, although this is is a feature whose biggest use is defining jq´s standard library (many jq functions such as **map** and **select** are in fact written in jq).

jq has reduction operators, which are very powerful but a bit tricky. Again, these are mostly used internally, to define some useful bits of jq´s standard library.

It may not be obvious at first, but jq is all about generators (yes, as often found in other languages). Some utilities are provided to help deal with generators.

Some minimal I/O support (besides reading JSON from standard input, and writing JSON to standard output) is available.

Finally, there is a module/library system.


## Variable / Symbolic Binding Operator: ... as $identifier | ...

In jq, all filters have an input and an output, so manual plumbing is not necessary to pass a value from one part of a program to the next. Many expressions, for instance **a + b**, pass their input to two distinct subexpressions (here **a** and **b** are both passed the same input), so variables aren´t usually necessary in order to use a value twice.

For instance, calculating the average value of an array of numbers requires a few variables in most languages - at least one to hold the array, perhaps one for each element or for a loop counter. In jq, it´s simply **add / length** - the **add** expression is given the array and produces its sum, and the **length** expression is given the array and produces its length.

So, there´s generally a cleaner way to solve most problems in jq than defining variables. Still, sometimes they do make things easier, so jq lets you define variables using **expression as $variable**. All variable names start with **$**. Here´s a slightly uglier version of the array-averaging example:

```
length as $array_length | add / $array_length
```

We´ll need a more complicated problem to find a situation where using variables actually makes our lives easier.

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

We use a variable, **$names**, to store the realnames object, so that we can refer to it later when looking up author usernames:

```
.realnames as $names | .posts[] | {title, author: $names[.author]}
```

The expression **exp as $x | ...** means: for each value of expression **exp**, run the rest of the pipeline with the entire original input, and with **$x** set to that value. Thus **as** functions as something of a foreach loop.

Just as **{foo}** is a handy way of writing **{foo: .foo}**, so **{$foo}** is a handy way of writing **{foo: $foo}**.

Multiple variables may be declared using a single **as** expression by providing a pattern that matches the structure of the input (this is known as "destructuring"):

```
. as {realnames: $names, posts: [$first, $second]} | ...
```

The variable declarations in array patterns (e.g., **. as [$first, $second]**) bind to the elements of the array in from the element at index zero on up, in order. When there is no value at the index for an array pattern element, **null** is bound to that variable.

Variables are scoped over the rest of the expression that defines them, so

```
.realnames as $names | (.posts[] | {title, author: $names[.author]})
```

will work, but

```
(.realnames as $names | .posts[]) | {title, author: $names[.author]}
```

won´t.

For programming language theorists, it´s more accurate to say that jq variables are lexically-scoped bindings. In particular there´s no way to change the value of a binding; one can only setup a new binding with the same name, but which will not be visible where the old one was.

```
jq ´.bar as $x | .foo | . + $x´
   {"foo":10, "bar":200}
=> 210
jq ´. as $i|[(.*2|. as $i| $i), $i]´
   5
=> [10,5]
jq ´. as [$a, $b, {c: $c}] | $a + $b + $c´
   [2, 3, {"c": 4, "d": 5}]
=> 9
jq ´.[] as [$a, $b] | {a: $a, b: $b}´
   [[0], [0, 1], [2, 1, 0]]
=> {"a":0,"b":null}, {"a":0,"b":1}, {"a":2,"b":1}
```


## Destructuring Alternative Operator: ?//

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

Or, if we aren´t sure if the input is an array of values or an object:

```
.[] as [$id, $kind, $user_id, $ts] ?// {$id, $kind, $user_id, $ts} | ...
```

Each alternative need not define all of the same variables, but all named variables will be available to the subsequent expression. Variables not matched in the alternative that succeeded will be **null**:

```
.resources[] as {$id, $kind, events: {$user_id, $ts}} ?// {$id, $kind, events: [{$first_user_id, $first_ts}]} | {$user_id, $first_user_id, $kind, $id, $ts, $first_ts}
```

Additionally, if the subsequent expression returns an error, the alternative operator will attempt to try the next binding. Errors that occur during the final alternative are passed through.

```
[[3]] | .[] as [$a] ?// [$b] | if $a != null then error("err: \($a)") else {$a,$b} end
jq ´.[] as {$a, $b, c: {$d, $e}} ?// {$a, $b, c: [{$d, $e}]} | {$a, $b, $d, $e}´
   [{"a": 1, "b": 2, "c": {"d": 3, "e": 4}}, {"a": 1, "b": 2, "c": [{"d": 3, "e": 4}]}]
=> {"a":1,"b":2,"d":3,"e":4}, {"a":1,"b":2,"d":3,"e":4}
jq ´.[] as {$a, $b, c: {$d}} ?// {$a, $b, c: [{$e}]} | {$a, $b, $d, $e}´
   [{"a": 1, "b": 2, "c": {"d": 3, "e": 4}}, {"a": 1, "b": 2, "c": [{"d": 3, "e": 4}]}]
=> {"a":1,"b":2,"d":3,"e":null}, {"a":1,"b":2,"d":null,"e":4}
jq ´.[] as [$a] ?// [$b] | if $a != null then error("err: \($a)") else {$a,$b} end´
   [[3]]
=> {"a":null,"b":3}
```


## Defining Functions

You can give a filter a name using "def" syntax:

```
def increment: . + 1;
```

From then on, **increment** is usable as a filter just like a builtin function (in fact, this is how many of the builtins are defined). A function may take arguments:

```
def map(f): [.[] | f];
```

Arguments are passed as *filters* (functions with no arguments), *not* as values. The same argument may be referenced multiple times with different inputs (here **f** is run for each element of the input array). Arguments to a function work more like callbacks than like value arguments. This is important to understand. Consider:

```
def foo(f): f|f;
5|foo(.*2)
```

The result will be 20 because **f** is **.*2**, and during the first invocation of **f** **.** will be 5, and the second time it will be 10 (5 * 2), so the result will be 20. Function arguments are filters, and filters expect an input when invoked.

If you want the value-argument behaviour for defining simple functions, you can just use a variable:

```
def addvalue(f): f as $f | map(. + $f);
```

Or use the short-hand:

```
def addvalue($f): ...;
```

With either definition, **addvalue(.foo)** will add the current input´s **.foo** field to each element of the array. Do note that calling **addvalue(.[])** will cause the **map(. + $f)** part to be evaluated once per value in the value of **.** at the call site.

Multiple definitions using the same function name are allowed. Each re-definition replaces the previous one for the same number of function arguments, but only for references from functions (or main program) subsequent to the re-definition. See also the section below on scoping.

```
jq ´def addvalue(f): . + [f]; map(addvalue(.[0]))´
   [[1,2],[10,20]]
=> [[1,2,1], [10,20,10]]
jq ´def addvalue(f): f as $x | map(. + $x); addvalue(.[0])´
   [[1,2],[10,20]]
=> [[1,2,1,2], [10,20,1,2]]
```


## Scoping

There are two types of symbols in jq: value bindings (a.k.a., "variables"), and functions. Both are scoped lexically, with expressions being able to refer only to symbols that have been defined "to the left" of them. The only exception to this rule is that functions can refer to themselves so as to be able to create recursive functions.

For example, in the following expression there is a binding which is visible "to the right" of it, **... | .*3 as $times_three | [. + $times_three] | ...**, but not "to the left". Consider this expression now, **... | (.*3 as $times_three | [. + $times_three]) | ...**: here the binding **$times_three** is *not* visible past the closing parenthesis.


## isempty(exp)

Returns true if **exp** produces no outputs, false otherwise.

```
jq ´isempty(empty)´
   null
=> true
jq ´isempty(.[])´
   []
=> true
jq ´isempty(.[])´
   [1,2,3]
=> false
```


## limit(n; expr)

The **limit** function extracts up to **n** outputs from **expr**.

```
jq ´[limit(3; .[])]´
   [0,1,2,3,4,5,6,7,8,9]
=> [0,1,2]
```


## skip(n; expr)

The **skip** function skips the first **n** outputs from **expr**.

```
jq ´[skip(3; .[])]´
   [0,1,2,3,4,5,6,7,8,9]
=> [3,4,5,6,7,8,9]
```


## first(expr), last(expr), nth(n; expr)

The **first(expr)** and **last(expr)** functions extract the first and last values from **expr**, respectively.

The **nth(n; expr)** function extracts the nth value output by **expr**. Note that **nth(n; expr)** doesn´t support negative values of **n**.

```
jq ´[first(range(.)), last(range(.)), nth(5; range(.))]´
   10
=> [0,9,5]
jq ´[first(empty), last(empty), nth(5; empty)]´
   null
=> []
```


## first, last, nth(n)

The **first** and **last** functions extract the first and last values from any array at **.**.

The **nth(n)** function extracts the nth value of any array at **.**.

```
jq ´[range(.)]|[first, last, nth(5)]´
   10
=> [0,9,5]
```


## reduce

The **reduce** syntax allows you to combine all of the results of an expression by accumulating them into a single answer. The form is **reduce EXP as $var (INIT; UPDATE)**. As an example, we´ll pass **[1,2,3]** to this expression:

```
reduce .[] as $item (0; . + $item)
```

For each result that **.[]** produces, **. + $item** is run to accumulate a running total, starting from 0 as the input value. In this example, **.[]** produces the results **1**, **2**, and **3**, so the effect is similar to running something like this:

```
0 | 1 as $item | . + $item |
    2 as $item | . + $item |
    3 as $item | . + $item
jq ´reduce .[] as $item (0; . + $item)´
   [1,2,3,4,5]
=> 15
jq ´reduce .[] as [$i,$j] (0; . + $i * $j)´
   [[1,2],[3,4],[5,6]]
=> 44
jq ´reduce .[] as {$x,$y} (null; .x += $x | .y += [$y])´
   [{"x":"a","y":1},{"x":"b","y":2},{"x":"c","y":3}]
=> {"x":"abc","y":[1,2,3]}
```


## foreach

The **foreach** syntax is similar to **reduce**, but intended to allow the construction of **limit** and reducers that produce intermediate results.

The form is **foreach EXP as $var (INIT; UPDATE; EXTRACT)**. As an example, we´ll pass **[1,2,3]** to this expression:

```
foreach .[] as $item (0; . + $item; [$item, . * 2])
```

Like the **reduce** syntax, **. + $item** is run for each result that **.[]** produces, but **[$item, . * 2]** is run for each intermediate values. In this example, since the intermediate values are **1**, **3**, and **6**, the **foreach** expression produces **[1,2]**, **[2,6]**, and **[3,12]**. So the effect is similar to running something like this:

```
0 | 1 as $item | . + $item | [$item, . * 2],
    2 as $item | . + $item | [$item, . * 2],
    3 as $item | . + $item | [$item, . * 2]
```

When **EXTRACT** is omitted, the identity filter is used. That is, it outputs the intermediate values as they are.

```
jq ´foreach .[] as $item (0; . + $item)´
   [1,2,3,4,5]
=> 1, 3, 6, 10, 15
jq ´foreach .[] as $item (0; . + $item; [$item, . * 2])´
   [1,2,3,4,5]
=> [1,2], [2,6], [3,12], [4,20], [5,30]
jq ´foreach .[] as $item (0; . + 1; {index: ., $item})´
   ["foo", "bar", "baz"]
=> {"index":1,"item":"foo"}, {"index":2,"item":"bar"}, {"index":3,"item":"baz"}
```


## Recursion

As described above, **recurse** uses recursion, and any jq function can be recursive. The **while** builtin is also implemented in terms of recursion.

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
