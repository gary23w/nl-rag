---
title: "starlark/spec.md at master · bazelbuild/starlark · GitHub (part 1/4)"
source: https://github.com/bazelbuild/starlark/blob/master/spec.md
domain: starlark
license: Apache-2.0
tags: starlark language, bazel build language, python-like config dialect, starlark scripting
fetched: 2026-07-02
part: 1/4
---

### Uh oh!

There was an error while loading. Please reload this page.

bazelbuild

/

starlark

Public

- Notifications You must be signed in to change notification settings
- Fork 176
- Star


## Expand file tree

More file actions

More file actions


## Latest commit


## History

History

History


## File metadata and controls

4838 lines (3697 loc) · 157 KB

Outline

# Starlark Language Specification

Starlark is a dialect of Python intended for use as a configuration language. A Starlark interpreter is typically embedded within a larger application, and this application may define additional domain-specific functions and data types beyond those provided by the core language. For example, Starlark is embedded within (and was originally developed for) the Bazel build tool.

This document was derived from the description of the Go implementation of Starlark. It was influenced by the Python specification, Copyright 1990–2017, Python Software Foundation, and the Go specification, Copyright 2009–2017, The Go Authors. It is now maintained by the Bazel team.


## Overview

Starlark is an untyped dynamic language with high-level data types, first-class functions with lexical scope, and automatic memory management or *garbage collection*.

Starlark is strongly influenced by Python, Starlark syntax is a strict subset of Python and Starlark semantics is almost a subset of that language. In particular, its data types and syntax for statements and expressions will be very familiar to any Python programmer. However, Starlark is intended not for writing applications but for expressing configuration: its programs are short-lived and have no external side effects and their main result is structured data or side effects on the host application.

Starlark is intended to be simple. There are no user-defined types, no inheritance, no reflection, no exceptions, no explicit memory management. Execution is finite. The language does not allow recursion or unbounded loops.

Starlark is suitable for use in highly parallel applications. An application may invoke the Starlark interpreter concurrently from many threads, without the possibility of a data race, because shared data structures become immutable due to *freezing*.

The language is deterministic and hermetic. Executing the same file with the same interpreter leads to the same result. By default, user code cannot interact with the environment.


## Contents

- Overview
- Contents
- Lexical elements
  - String literals
  - Bytes literals
  - Special tokens
- Data types
  - None
  - Booleans
  - Integers
  - Floating-point numbers
  - Strings
  - Bytes
  - Lists
  - Tuples
  - Dictionaries
  - Sets
  - Functions
  - Built-in functions
- Name binding and variables
- Value concepts
  - Identity and mutation
  - Freezing a value
  - Hashing
  - Collection types
  - Iteration
  - Indexing
- Expressions
  - Identifiers
  - Literals
  - Parenthesized expressions
  - Dictionary expressions
  - List expressions
  - Unary operators
  - Binary operators
  - Conditional expressions
  - Comprehensions
  - Function and method calls
  - Dot expressions
  - Subscript expressions
  - Slice expressions
  - Lambda expressions
- Statements
  - Pass statements
  - Assignments
  - Augmented assignments
  - Function definitions
  - Return statements
  - Expression statements
  - If statements
  - For statements
  - Break and Continue
  - Load statements
- Module execution
- Built-in constants and functions
  - None
  - True and False
  - abs
  - any
  - all
  - bool
  - bytes
  - dict
  - dir
  - enumerate
  - fail
  - float
  - getattr
  - hasattr
  - hash
  - int
  - len
  - list
  - max
  - min
  - print
  - range
  - repr
  - reversed
  - set
  - sorted
  - str
  - tuple
  - type
  - zip
- Built-in methods
  - bytes·elems
  - dict·clear
  - dict·get
  - dict·items
  - dict·keys
  - dict·pop
  - dict·popitem
  - dict·setdefault
  - dict·update
  - dict·values
  - list·append
  - list·clear
  - list·extend
  - list·index
  - list·insert
  - list·pop
  - list·remove
  - set·add
  - set·clear
  - set·difference
  - set·difference_update
  - set·discard
  - set·intersection
  - set·intersection_update
  - set·isdisjoint
  - set·issubset
  - set·issuperset
  - set·pop
  - set·remove
  - set·symmetric_difference
  - set·symmetric_difference_update
  - set·union
  - set·update
  - string·capitalize
  - string·count
  - string·elems
  - string·endswith
  - string·find
  - string·format
  - string·index
  - string·isalnum
  - string·isalpha
  - string·isdigit
  - string·islower
  - string·isspace
  - string·istitle
  - string·isupper
  - string·join
  - string·lower
  - string·lstrip
  - string·partition
  - string·removeprefix
  - string·removesuffix
  - string·replace
  - string·rfind
  - string·rindex
  - string·rpartition
  - string·rsplit
  - string·rstrip
  - string·split
  - string·splitlines
  - string·startswith
  - string·strip
  - string·title
  - string·upper
- Grammar reference


## Lexical elements

Starlark syntax (but not semantics) is a strict subset of Python syntax. Practically it means, tools working with Python AST can be used to work with Starlark files.

A Starlark program consists of one or more modules. Each module is defined by a single UTF-8-encoded text file.

Starlark grammar is introduced gradually throughout this document as shown below, and a complete Starlark grammar reference is provided at the end.

Grammar notation:

```
- lowercase and 'quoted' items are lexical tokens.
- Capitalized names denote grammar productions.
- (...) implies grouping.
- x | y means either x or y.
- [x] means x is optional.
- {x} means x is repeated zero or more times.
- The end of each declaration is marked with a period.
```

The contents of a Starlark file are broken into a sequence of tokens of five kinds: white space, punctuation, keywords, identifiers, and literals. Each token is formed from the longest sequence of characters that would form a valid token of each kind.

```
File = {Statement | newline} eof .
```

*White space* consists of spaces (U+0020), tabs (U+0009), carriage returns (U+000D), and newlines (U+000A). Within a line, white space has no effect other than to delimit the previous token, but newlines, and spaces at the start of a line, are significant tokens.

*Comments*: A hash character (`#`) appearing outside of a string or bytes literal marks the start of a comment; the comment extends to the end of the line, not including the newline character. Comments are treated like other white space.

*Punctuation*: The following punctuation characters or sequences of characters are tokens:

```
+    -    *    /    //   %    **
~    &    |    ^    <<   >>
.    ,    =    ;    :
(    )    [    ]    {    }
<    >    >=   <=   ==   !=
+=   -=   *=   /=   //=  %=
&=   |=   ^=   <<=  >>=
```

*Keywords*: The following tokens are keywords and may not be used as identifiers:

```
and            else           load
break          for            not
continue       if             or
def            in             pass
elif           lambda         return
```

The tokens below also may not be used as identifiers although they do not appear in the grammar; they are reserved as possible future keywords:

```
as             global
assert         import
async          is
await          nonlocal
class          raise
del            try
except         while
finally        with
from           yield
```

*Identifiers*: an identifier is a sequence of Unicode letters, decimal digits, and underscores (`_`), not starting with a digit. Identifiers are used as names for values.

Examples:

```
None    True    len
x       index   starts_with     arg0
```

*Literals*: literals are tokens that denote specific values. Starlark has integer, floating-point, string, and bytes literals.

```
0                               # int
123                             # decimal int
0x7f                            # hexadecimal int
0o755                           # octal int

0.0     0.       .0             # float
1e10    1e+10    1e-10
1.1e10  1.1e+10  1.1e-10

"hello"      'hello'            # string
'''hello'''  """hello"""        # triple-quoted string
r'hello'     r"hello"           # raw string literal

b"hello"     b'hello'           # bytes
b'''hello''' b"""hello"""       # triple-quoted bytes
rb'hello'    br"hello"          # raw bytes literal
```

Integer and floating-point literal tokens are defined by the following grammar:

```
int         = decimal_lit | octal_lit | hex_lit | 0 .
decimal_lit = ('1' … '9') {decimal_digit} .
octal_lit   = '0' ('o' | 'O') octal_digit {octal_digit} .
hex_lit     = '0' ('x' | 'X') hex_digit {hex_digit} .

float     = decimals '.' [decimals] [exponent]
          | decimals exponent
          | '.' decimals [exponent]
          .
decimals  = decimal_digit {decimal_digit} .
exponent  = ('e'|'E') ['+'|'-'] decimals .

decimal_digit = '0' … '9' .
octal_digit   = '0' … '7' .
hex_digit     = '0' … '9' | 'A' … 'F' | 'a' … 'f' .
```

It is a static error if a floating-point literal denotes a value whose magnitude is too large to be represented as a finite `float` value.

### String literals

A Starlark string literal denotes a string value. In its simplest form, it consists of the desired text surrounded by matching single- or double-quotation marks:

```highlight
"abc"
'abc'
```

Literal occurrences of the chosen quotation mark character must be escaped by a preceding backslash. So, if a string contains several of one kind of quotation mark, it may be convenient to quote the string using the other kind, as in these examples:

```highlight
'Have you read "To Kill a Mockingbird?"'
"Yes, it's a classic."
"Have you read \"To Kill a Mockingbird?\""
'Yes, it\'s a classic.'
```

#### String escapes

Within a string literal, the backslash character `\` indicates the start of an *escape sequence*, a notation for expressing things that are impossible or awkward to write directly.

The following *traditional escape sequences* represent the ASCII control codes 7-13:

```
\a   \x07 alert or bell
\b   \x08 backspace
\f   \x0C form feed
\n   \x0A line feed
\r   \x0D carriage return
\t   \x09 horizontal tab
\v   \x0B vertical tab
```

A *literal backslash* is written using the escape `\\`.

An *escaped newline*---that is, a backslash at the end of a line---is ignored, allowing a long string to be split across multiple lines of the source file.

```highlight
"abc\
def"			# "abcdef"
```

An *octal escape* encodes a single string element using its octal value. It consists of a backslash followed by one, two, or three octal digits [0-7]. Simiarly, a *hexadecimal escape* encodes a single string element using its hexadecimal value. It consists of `\x` followed by two hexadecimal digits [0-9a-fA-F]. It is an error if the value of an octal or hexadecimal escape is greater than decimal 127.

```highlight
'\0'			# "\x00"  a string containing a single NUL element
'\12'			# "\n"    octal 12 = decimal 10
'\101-\132'		# "A-Z"
'\119'			# "\t9"   = "\11" + "9"

'\x00'			# "\x00"  a string containing a single NUL element
'\x0A'			# "\n"    hexadecimal A = decimal 10
"\x41-\x5A"             # "A-Z"
```

A *Unicode escape* denotes the UTF-K encoding of a single, valid Unicode code point, where K is the implementation-defined number of bits in each string element (see strings). The `\uXXXX` form, with exactly four hexadecimal digits, denotes a 16-bit code point, and the `\UXXXXXXXX`, with exactly eight digits, denotes a 32-bit code point. It is an error if the value lies in the surrogate range (U+D800 to U+DFFF) or is greater than U+10FFFF.

```highlight
'\u0041'		# "A", an ASCII letter (U+0041)
'\u0414' 		# "Д", a Cyrillic capital letter (U+0414)
'\u754c                 # "界", a Chinese character (U+754C)
'\U0001F600'            # "😀", an Emoji (U+1F600)
```

The length of the encoding of a single Unicode code point may vary based on the implementation's value of K:

```highlight
len("A") 		# 1
len("Д") 		# 2 (UTF-8) or 1 (UTF-16)
len("界")               # 3 (UTF-8) or 1 (UTF-16)
len("😀")               # 4 (UTF-8) or 2 (UTF-16)
```

Although string values may be capable of representing any sequence of elements, string *literals* can denote only sequences of UTF-K code units that are valid encodings of text. (Any literal syntax capable of representing arbitrary element sequences would inherently be non-portable across implementations.) Consequently, when the `repr` function is applied to a string containing an invalid encoding, its result is not a valid string literal.

An ordinary string literal may not contain an unescaped newline, but a *multiline string literal* may spread over multiple source lines. It is denoted using three quotation marks at start and end. Within it, unescaped newlines and quotation marks (or even pairs of quotation marks) have their literal meaning, but three quotation marks end the literal. This makes it easy to quote large blocks of text with few escapes.

```
haiku = '''
Yesterday it worked.
Today it is not working.
That's computers. Sigh.
'''
```

Regardless of the platform's convention for text line endings---for example, a linefeed (\n) on UNIX, or a carriage return followed by a linefeed (\r\n) on Microsoft Windows---an unescaped line ending in a multiline string literal always denotes a line feed (\n).

Starlark also supports *raw string literals*, which look like an ordinary single- or double-quotation preceded by `r`. Within a raw string literal, there is no special processing of backslash escapes, other than an escaped quotation mark (which denotes a literal quotation mark), or an escaped newline (which denotes a backslash followed by a newline). This form of quotation is typically used when writing strings that contain many quotation marks or backslashes (such as regular expressions or shell commands) to reduce the burden of escaping:

```highlight
"a\nb"		# "a\nb"  = 'a' + '\n' + 'b'
r"a\nb"		# "a\\nb" = 'a' + '\\' + 'n' + 'b'
"a\
b"		# "ab"
r"a\
b"		# "a\\\nb"
```

It is an error for a backslash to appear within a string literal other than as part of one of the escapes described above.

### Bytes literals

A Starlark bytes literal denotes a bytes value, and looks like a string literal, in any of its various forms (single-quoted, double-quoted, triple-quoted, raw) preceded by the letter `b`.

```highlight
b"abc"       b'abc'
b"""abc"""   b'''abc'''
br"abc"      br'abc'
rb"abc"      rb'abc'
```

A raw bytes literal may be indicated by either a `br` or `rb` prefix.

Non-escaped text within a bytes literal denotes the UTF-8 encoding of that text. Bytes literals support the same escape sequences as text strings, with the following differences:

- Octal and hexadecimal escapes may specify any byte value from zero (`\000` or `\x00`) to 255 (`\377` or `\xFF`).
- A Unicode escape `\uXXXX` or `\UXXXXXXXX` denotes the byte sequence of the UTF-8 encoding of the specified 16- or 32-bit code point. (As with text strings, the code point value must not lie in the surrogate range.)

Any valid string literal that, with a `b` prefix, is also a valid bytes literal is equivalent in the sense that the bytes value is the UTF-8 encoding of the string value.

### Special tokens

Starlark is space-sensitive language, and indentation is used to denote a block of statements.

Unlike Python, indentation can only be composed of space characters (U+0020), not tabs.

TODO: define indent, outdent, semicolon, newline, eof


## Data types

These are the main data types built in to the interpreter:

```
NoneType                     # the type of None
bool                         # True or False
int                          # a signed integer of arbitrary magnitude
float                        # an IEEE 754 double-precision floating-point number
string                       # a text string, with Unicode encoded as UTF-8 or UTF-16
bytes                        # a byte string
list                         # a sequence of values, usually homogeneous in nature
tuple                        # an unmodifiable sequence of values
dict                         # an associative mapping from keys to values
set                          # a collection of unique values
function                     # a function
```

Some functions, such as the `range` function, return instances of special-purpose types that don't appear in this list. Additional data types may be defined by the host application into which the interpreter is embedded, and those data types may participate in basic operations of the language such as arithmetic, comparison, indexing, and function calls.

Some operations, like `bool(x)` or `str(x)`, can be applied to any Starlark value, while others, like integer indexing `a[i]`, apply only to certain types. The *value concepts* section explains the groupings of types by the operators they support.

### None

`None` is a distinguished value used to indicate the absence of any other value. For example, the result of a call to a function that contains no return statement is `None`.

`None` is equal only to itself. Its type is `"NoneType"`. The truth value of `None` is `False`.

### Booleans

There are two Boolean values, `True` and `False`, representing the truth or falsehood of a predicate. The type of a Boolean is `"bool"`.

Boolean values are typically used as conditions in `if` statements, although any Starlark value may be used in this way. Aside from `False` itself, the following core language values are considered false in a condition:

- `None`
- numerical 0 (`0`, `0.0` and `-0.0`)
- the empty string (`""`) and empty bytes (`b""`)
- the empty collections `[]`, `()`, `{}`, and `set()`

All other core language values are considered true. Application-defined types determine their own truth value.

Any value may be explicitly converted to a Boolean using the built-in `bool` function.

True and False may be converted to the values 1 and 0 using the `int` function, but Booleans are not numbers. Testing a non-Boolean value for equality to a Boolean using `==` returns `False`, regardless of whether they have the same truth value.

```highlight
"A" if 1 + 1 else "B"                   # "A"
"A" if 0.0 else "B"                     # "B"

if not mylist:
    empty = True

1 == True                               # False
bool(1) == True                         # True
```

### Integers

The Starlark integer type represents integers. Its type is `"int"`.

Integers may be positive or negative, and arbitrarily large. Integer arithmetic is exact. Integers are totally ordered; comparisons follow mathematical tradition.

The `+` and `-` operators perform addition and subtraction, respectively. The `*` operator performs multiplication.

The `//` and `%` operations on integers compute floored division and remainder of floored division, respectively. If the signs of the operands differ, the sign of the remainder `x % y` matches that of the divisor, `y`. For all finite x and y (y ≠ 0), `(x // y) * y + (x % y) == x`. The `/` operator implements floating-point division, and yields a `float` result even when its operands are both of type `int`.

Integers, including negative values, may be interpreted as bit vectors. Negative values use two's complement representation. The `|`, `&`, and `^` operators implement bitwise OR, AND, and XOR, respectively. The unary `~` operator yields the bitwise inversion of its integer argument. The `<<` and `>>` operators shift the first argument to the left or right by the number of bits given by the second argument.

Any bool, number, or string may be interpreted as an integer by using the `int` built-in function.

An integer used in a Boolean context is considered true if it is non-zero.

```highlight
100 // 5 * 9 + 32               # 212
3 // 2                          # 1
111111111 * 111111111           # 12345678987654321
int("0xffff", 16)               # 65535
```

### Floating-point numbers

The Starlark floating-point data type represents an IEEE 754 double-precision floating-point number. Its type is `"float"`.

Arithmetic on floats using the `+`, `-`, `*`, `/`, `//`, and `%` operators follows the IEEE 754 standard. However, computing the division or remainder of division by zero is a dynamic error.

An arithmetic operation applied to a mixture of `float` and `int` operands works as if the `int` operand were first converted to a `float`. For example, `3.141 + 1` is equivalent to `3.141 + float(1)`. The implicit conversion fails if the `int` value is too large to be represented as a `float`.

There are two floating-point division operators: `x / y` yields the floating-point quotient of `x` and `y`, whereas `x // y` yields `floor(x / y)`, that is, the largest representable integer value not greater than `x / y`. Although the resulting number is integral, it is represented as a `float` if either operand is a `float`.

The `%` operation computes the remainder of floored division. As with the corresponding operation on integers, if the signs of the operands differ, the sign of the remainder `x % y` matches that of the divisor, `y`.

All float values are ordered, so they may be compared using operators such as `==` and `<`, and sorted using `sorted`.

IEEE 754 defines two zero values, +0.0 and -0.0. They compare equal to each other.

IEEE 754 defines two infinite float values `+Inf` and `-Inf`, which represent numbers greater/less than all finite float values.

IEEE 754 defines many "not a number" (NaN) values. They are non-finite, and represent the results of dubious operations such as `Inf / Inf`. All NaN values compare equal to each other, but greater than any non-NaN `float` value. (Starlark does not follow the IEEE 754 standard for NaN comparisons, which requires that all comparisons with NaN are false, except NaN != NaN.)

A comparison operation may be applied to a mixture of int and float values. The result of such comparisons is mathematically exact, even if neither operand can be exactly represented by the type of the other.

```highlight
(type(1.0), type(1))            # ("float", "int")
1.0 == 1			# True

big = (1<<53)+1			# first int not exactly representable as float
(big + 0.0) == big		# False (addition caused rounding down)
(big + 0.0) - big		# 0.0   (both operands subject to rounding down)
```

Any bool, number, or string may be interpreted as a floating-point number by using the `float` built-in function.

A float used in a Boolean context is considered true if it is non-zero (not equal to 0.0 or -0.0). A NaN value is thus considered true.

```highlight
1.23e45 * 1.23e45                               # 1.5129e+90
1.111111111111111 * 1.111111111111111           # 1.23457
3.0 / 2                                         # 1.5
3 / 2.0                                         # 1.5
float(3) / 2                                    # 1.5
3.0 // 2.0                                      # 1.0
```

### Strings

A string is an immutable array of elements that encode Unicode text. The type of a string is `"string"`.

For reasons of efficiency and interoperability with the host language, the number of bits in each string element, which we call K, is specified to be either 8 or 16, depending on the implementation. For example, in the Go and Rust implementations, each string element is an 8-bit value (a byte) and Unicode text is encoded as UTF-8, whereas in the Java implementation, string elements are 16-bit values (Java `char`s) and Unicode text is encoded as UTF-16.

An implementation may permit strings to hold arbitrary values of the element type, including sequences that do not encode valid Unicode text; or, it may disallow invalid sequences, and operations that would form them.

The built-in `len` function returns the number of elements in a string.

Strings may be concatenated with the `+` operator.

Strings support indexing and slicing. The result of both operations is another string (with length 1, in the case of indexing).

Strings are hashable, and thus may be used as keys in a dictionary.

Strings are totally ordered lexicographically, so strings may be compared using operators such as `==` and `<`. (Beware that the UTF-16 string encoding is not order-preserving with respect to code point values.)

Strings are *not* iterable, so they cannot be used as the operand of a `for` loop or of methods that expect iterables (such as the `list()` constructor). One must instead explicitly call a method of a string value to obtain an iterable view of its elements. Because strings are not iterable, they are not considered to be subtypes of `Collection` or `Sequence`. (Starlark deviates from Python here to avoid a common pitfall in which a single string is mistakenly used where a list of strings was intended, resulting in exploding the string into its individual characters.)

Any value may formatted as a string using the `str` or `repr` built-in functions, the `str % tuple` operator, or the `str.format` method.

A string used in a Boolean context is considered true if it is non-empty.

Strings have several built-in methods:

- `capitalize`
- `count`
- `elems`
- `endswith`
- `find`
- `format`
- `index`
- `isalnum`
- `isalpha`
- `isdigit`
- `islower`
- `isspace`
- `istitle`
- `isupper`
- `join`
- `lower`
- `lstrip`
- `partition`
- `removeprefix`
- `removesuffix`
- `replace`
- `rfind`
- `rindex`
- `rpartition`
- `rsplit`
- `rstrip`
- `split`
- `splitlines`
- `startswith`
- `strip`
- `title`
- `upper`

### Bytes

A *bytes* is an immutable array of integers in the range 0-255. The type of a bytes is `"bytes"`.

Unlike a string, which is intended for text, a bytes may represent binary data, such as the contents of an arbitrary file, without loss.

The built-in `len` function returns the number of elements (bytes) in a `bytes`.

Two bytes values may be concatenated with the `+` operator.

Bytes may be indexed and sliced. The result of indexing is the value of the byte at the given position, as an integer. The result of slicing is another bytes object.

The comparison `x in b`, where `b` is a bytes value and `x` is an integer in the range [0, 255], tests whether `x`'s value is an element of `b`. If `x` is instead another bytes value, the comparison tests whether `x` is contained as a consecutive subsequence of `b` (analogous to substrings of a string). It is an error if `x` is an out-of-range integer, or any other type of value.

Like strings, bytes values are hashable, totally ordered, and considered True if they are non-empty. They are not iterable, and not a subtype of `Collection` nor `Sequence`.

A bytes value has these methods:

- `elems`

```
TODO(https://github.com/bazelbuild/starlark/issues/112)
- more methods: likely the same as string (minus those concerned with text):
    join
    {start,end}with
    {r,}{find,index,partition,split,strip}
    replace
TODO: encode, decode methods?
TODO: ord, chr.
TODO: string.elems(), string.elem_ords(), string.codepoint_ords()
```

### Lists

A list is a mutable sequence of values. The type of a list is `"list"`.

Lists are a subtype of `Sequence`. The number of elements may be retrieved with the built-in `len()` function. Lists can be indexed to retrieve a single element, and sliced to produce a new list. Lists can be iterated over by `for` loops.

List may be constructed using bracketed list notation:

```highlight
[]              # an empty list
[1]             # a 1-element list
[1, 2]          # a 2-element list
```

Lists can also be constructed from any iterable by using the built-in `list` function.

List elements may be added using the `append` or `extend` methods, removed using the `remove` method, or reordered by assignments such as `list[i] = list[j]`.

The concatenation operation `x + y` yields a new list containing all the elements of the two lists x and y.

For most types, `x += y` is equivalent to `x = x + y`, except that it evaluates `x` only once, that is, it allocates a new list to hold the concatenation of `x` and `y`. However, if `x` refers to a list, the statement does not allocate a new list but instead mutates the original list in place, similar to `x.extend(y)`.

Lists are not hashable, so may not be used in the keys of a dictionary.

A list used in a Boolean context is considered true if it is non-empty.

A *list comprehension* creates a new list whose elements are the result of some expression applied to each element of another sequence.

```highlight
[x*x for x in [1, 2, 3, 4]]      # [1, 4, 9, 16]
```

A list value has these methods:

- `append`
- `clear`
- `extend`
- `index`
- `insert`
- `pop`
- `remove`

### Tuples

A tuple is an immutable sequence of values. The type of a tuple is `"tuple"`.

Like lists, tuple is a subtype of `Sequence`, and supports the same `len()`, indexing, slicing, and iteration operations. A slice of a tuple returns another tuple.

Tuples are constructed using parenthesized list notation:

```highlight
()                      # the empty tuple
(1,)                    # a 1-tuple
(1, 2)                  # a 2-tuple ("pair")
(1, 2, 3)               # a 3-tuple
```

Observe that for the 1-tuple, the trailing comma is necessary to distinguish it from the parenthesized expression `(1)`. 1-tuples are seldom used.

Starlark, unlike Python, does not permit a trailing comma to appear in an unparenthesized tuple expression:

```highlight
for k, v, in dict.items(): pass                 # syntax error at 'in'
_ = [(v, k) for k, v, in dict.items()]          # syntax error at 'in'

sorted(3, 1, 4, 1,)                             # ok
[1, 2, 3, ]                                     # ok
{1: 2, 3:4, }                                   # ok
```

Tuples can be constructed from any iterable by using the built-in `tuple` function.

Unlike lists, tuples cannot be modified. However, the mutable elements of a tuple may be modified.

Tuples are hashable if their elements are hashable, in which case they may be used as keys of a dictionary.

Tuples may be concatenated using the `+` operator. Note that it is not legal to directly concatenate a tuple with a list.

A tuple used in a Boolean context is considered true if it is non-empty.

### Dictionaries

A dictionary is a mutable mapping from keys to values. The type of a dictionary is `"dict"`.

Dictionaries provide constant-time operations to insert an element, to look up the value for a key, or to remove an element. Dictionaries are implemented using hash tables, so keys must be hashable. Hashable values include `None`, Booleans, numbers, strings, and bytes, and tuples composed from hashable values. Most mutable values, such as lists, dictionaries, and sets, are not hashable, unless they are frozen.

Attempting to use a non-hashable value as a key in a dictionary results in a dynamic error.

A dictionary expression specifies a dictionary as a set of key/value pairs enclosed in braces:

```highlight
coins = {
  "penny": 1,
  "nickel": 5,
  "dime": 10,
  "quarter": 25,
}
```

The expression `d[k]`, where `d` is a dictionary and `k` is a key, retrieves the value associated with the key. If the dictionary contains no such item, the operation fails:

```highlight
coins["penny"]          # 1
coins["dime"]           # 10
coins["silver dollar"]  # error: key not found
```

A key/value item may be added to a dictionary, or updated if the key is already present, by using `d[k]` on the left side of an assignment:

```highlight
len(coins)				# 4
coins["shilling"] = 20
len(coins)				# 5, item was inserted
coins["shilling"] = 5
len(coins)				# 5, existing item was updated
```

A dictionary can also be constructed using a dictionary comprehension, which evaluates a pair of expressions, the *key* and the *value*, for every element of another iterable such as a list. This example builds a mapping from each word to its length:

```highlight
words = ["able", "baker", "charlie"]
{x: len(x) for x in words}	# {"charlie": 7, "baker": 5, "able": 4}
```

Dictionaries are a subtype of `Mapping`. `len()` returns the number of entries. Iteration yields the keys in the order that they were inserted; updating the value associated with an existing key does not affect the iteration order.

```highlight
x = dict([("a", 1), ("b", 2)])          # {"a": 1, "b": 2}
x.update([("a", 3), ("c", 4)])          # {"a": 3, "b": 2, "c": 4}
```

```highlight
for name in coins:
  print(name, coins[name])	# prints "quarter 25", "dime 10", ...
```

Like all mutable values in Starlark, a dictionary can be frozen, and once frozen, all subsequent operations that attempt to update it will fail.

A dictionary used in a Boolean context is considered true if it is non-empty.

The binary `|` operation may be applied to two dictionaries. It yields a new dictionary whose set of keys is the union of the sets of keys of the two operands. The corresponding values are taken from the operands, where the value taken from the right operand takes precedence if both contain a given key. Iterating over the keys in the resulting dictionary first yields all keys in the left operand in insertion order, then all keys in the right operand that were not present in the left operand, again in insertion order.

There is also an augmented assignment version of the `|` operation. For two dictionaries `d1` and `d2`, the expression `d1 |= d2` behaves similar to `d1 = d1 | d2`, but mutates `d1` in-place rather than assigning a new dictionary to it.

Dictionaries may be compared for equality using `==` and `!=`. Two dictionaries compare equal if they contain the same number of items and each key/value item (k, v) found in one dictionary is also present in the other. Dictionaries are not ordered; it is an error to compare two dictionaries with `<`.

A dictionary value has these methods:

- `clear`
- `get`
- `items`
- `keys`
- `pop`
- `popitem`
- `setdefault`
- `update`
- `values`

### Sets

A set is a mutable collection of unique values - the set's *elements*. The type of a set is `"set"`.

Sets provide constant-time operations to insert, remove, or check for the presence of a value. Sets are implemented using a hash table, and therefore, just like keys of a dictionary, elements of a set must be hashable. A value may be used as an element of a set if and only if it may be used as a key of a dictionary.

Sets may be constructed using the set() built-in function, which returns a set containing all the elements of its optional argument, which must be an iterable. Calling `set()` without an argument constructs an empty set. Sets have no literal syntax.

The `in` and `not in` operations check whether a value is (or is not) in a set:

```highlight
s = set(["a", "b", "c"])
"a" in s  # True
"z" in s  # False
```

A set is a subtype of `Collection`. Its size can be retrieved using the len() built-in function, and the order of iteration is the order in which elements were inserted. (Attempting to add an element that is already present is a no-op, and does not change the iteration order.)

```highlight
s = set(["z", "y", "z", "y"])
len(s)       # prints 2
s.add("x")
s.add("z")
len(s)       # prints 3
for e in s:
    print e  # prints "z", "y", "x"
```

A set used in Boolean context is true if and only if it is non-empty.

```highlight
s = set()
"non-empty" if s else "empty"  # "empty"
t = set(["x", "y"])
"non-empty" if t else "empty"  # "non-empty"
```

Sets may be compared for equality or inequality using `==` and `!=`. A set `s` is equal to `t` if and only if `t` is a set containing the same elements; iteration order is not significant. In particular, a set is *not* equal to the list of its elements. Sets are not ordered with respect to other sets, and an attempt to compare two sets using `<`, `<=`, `>`, `>=`, or to sort a sequence of sets, will fail.

```highlight
set() == set()              # True
set() != []                 # True
set([1, 2]) == set([2, 1])  # True
set([1, 2]) != [1, 2]       # True
```

The `|` operation on two sets returns the union of the two sets: a set containing the elements found in either one or both of the original sets.

```highlight
set([1, 2]) | set([3, 2])  # set([1, 2, 3])
```

The `&` operation on two sets returns the intersection of the two sets: a set containing only the elements found in both of the original sets.

```highlight
set([1, 2]) & set([2, 3])  # set([2])
set([1, 2]) & set([3, 4])  # set()
```

The `-` operation on two sets returns the difference of the two sets: a set containing the elements found in the left-hand side set but not the right-hand side set.

```highlight
set([1, 2]) - set([2, 3])  # set([1])
set([1, 2]) - set([3, 4])  # set([1, 2])
```

The `^` operation on two sets returns the symmetric difference of the two sets: a set containing the elements found in exactly one of the two original sets, but not in both.

```highlight
set([1, 2]) ^ set([2, 3])  # set([1, 3])
set([1, 2]) ^ set([3, 4])  # set([1, 2, 3, 4])
```

In each of the above operations, the elements of the resulting set retain their order from the two operand sets, with all elements that were drawn from the left-hand side ordered before any element that was only present in the right-hand side.

The corresponding augmented assignments, `|=`, `&=`, `-=`, and `^=`, modify the left-hand set in place.

```highlight
s = set([1, 2])
s |= set([2, 3, 4])     # s now equals set([1, 2, 3, 4])
s &= set([0, 1, 2, 3])  # s now equals set([1, 2, 3])
s -= set([0, 1])        # s now equals set([2, 3])
s ^= set([3, 4])        # s now equals set([2, 4])
```

Like all mutable values in Starlark, a set can be frozen, and once frozen, all subsequent operations that attempt to update it will fail.

A set has the following methods:

- `add`
- `clear`
- `difference`
- `difference_update`
- `discard`
- `intersection`
- `intersection_update`
- `isdisjoint`
- `issubset`
- `issuperset`
- `pop`
- `remove`
- `symmetric_difference`
- `symmetric_difference_update`
- `union`
- `update`

### Functions

A function value represents a function defined in Starlark. Its type is `"function"`. A function value used in a Boolean context is always considered true.

Functions defined by a `def` statement are named; functions defined by a `lambda` expression are anonymous.

Function definitions may be nested, and an inner function may refer to a local variable of an outer function. Starlark has no equivalent of Python's `nonlocal` keyword, and thus no way for an inner function cannot assign to a local variable of an outer function. However, the inner function may mutate the value of such variables until they become frozen.

A function definition defines zero or more named parameters. Starlark has a rich mechanism for passing arguments to functions.

The example below shows a definition and call of a function of two required parameters, `x` and `y`.

```highlight
def idiv(x, y):
  return x // y

idiv(6, 3)		# 2
```

A call may provide arguments to function parameters either by position, as in the example above, or by name, as in first two calls below, or by a mixture of the two forms, as in the third call below. All the positional arguments must precede all the named arguments. Named arguments may improve clarity, especially in functions of several parameters.

```highlight
idiv(x=6, y=3)		# 2
idiv(y=3, x=6)		# 2

idiv(6, y=3)		# 2
```

**Optional parameters:** A parameter declaration may specify a default value using `name=value` syntax; such a parameter is *optional*. The default value expression is evaluated during execution of the `def` statement, and the default value forms part of the function value. All optional parameters must follow all non-optional parameters. A function call may omit arguments for any suffix of the optional parameters; the effective values of those arguments are supplied by the function's parameter defaults.

```highlight
def f(x, y=3):
  return x, y

f(1, 2)	# (1, 2)
f(1)	# (1, 3)
```

If a function parameter's default value is a mutable expression, modifications to the value during one call may be observed by subsequent calls. Beware of this when using lists or dicts as default values. If the function becomes frozen, its parameters' default values become frozen too.

```highlight
# module a.sky
def f(x, list=[]):
  list.append(x)
  return list

f(4, [1,2,3])           # [1, 2, 3, 4]
f(1)                    # [1]
f(2)                    # [1, 2], not [2]!

# module b.sky
load("a.sky", "f")
f(3)                    # error: cannot append to frozen list
```

**Variadic functions:** Some functions allow callers to provide an arbitrary number of arguments. After all required and optional parameters, a function definition may specify a *variadic arguments list* or *varargs* parameter, indicated by a star preceding the parameter name: `*args`. Any surplus positional arguments provided by the caller are formed into a tuple and assigned to the `args` parameter.

```highlight
def f(x, y, *args):
  return x, y, args

f(1, 2)                 # (1, 2, ())
f(1, 2, 3, 4)           # (1, 2, (3, 4))
```

**Keyword-variadic functions:** Some functions allow callers to provide an arbitrary sequence of `name=value` keyword arguments. A function definition may include a final *keyword arguments dictionary* or *kwargs* parameter, indicated by a double-star preceding the parameter name: `**kwargs`. Any surplus named arguments that do not correspond to named parameters are collected in a new dictionary and assigned to the `kwargs` parameter:

```highlight
def f(x, y, **kwargs):
  return x, y, kwargs

f(1, 2)                 # (1, 2, {})
f(x=2, y=1)             # (2, 1, {})
f(x=2, y=1, z=3)        # (2, 1, {"z": 3})
```

It is a static error if any two parameters of a function have the same name.

Just as a function definition may accept an arbitrary number of positional or named arguments, a function call may provide an arbitrary number of positional or named arguments supplied by a list or dictionary:

```highlight
def f(a, b, c=5):
  return a * b + c

f(*[2, 3])              # 11
f(*[2, 3, 7])           # 13
f(*[2])                 # error: f takes at least 2 arguments (1 given)

f(**dict(b=3, a=2))             # 11
f(**dict(c=7, a=2, b=3))        # 13
f(**dict(a=2))                  # error: f takes at least 2 arguments (1 given)
f(**dict(d=4))                  # error: f got unexpected keyword argument "d"
```

Once the parameters have been successfully bound to the arguments supplied by the call, the sequence of statements that comprise the function body is executed.

It is a static error if a function call has two named arguments of the same name, such as `f(x=1, x=2)`. A call that provides a `**kwargs` argument may yet have two values for the same name, such as `f(x=1, **dict(x=2))`. This results in a dynamic error.

Function arguments are evaluated in the order they appear in the call.

Unlike Python, Starlark does not allow more than one `*args` argument in a call, and if a `*args` argument is present it must appear after all positional and named arguments. In particular, even though keyword-only arguments (see below) are declared after `*args` in a function's definition, they nevertheless must appear before `*args` in a call to the function.

A function call completes normally after the execution of either a `return` statement, or of the last statement in the function body. The result of the function call is the value of the return statement's operand, or `None` if the return statement had no operand or if the function completeted without executing a return statement.

```highlight
def f(x):
  if x == 0:
    return
  if x < 0:
    return -x
  print(x)

f(1)            # returns None after printing "1"
f(0)            # returns None without printing
f(-1)           # returns 1 without printing
```

It is a dynamic error for a function to call itself or another function value with the same declaration.

```highlight
def fib(x):
  if x < 2:
    return x
  return fib(x-2) + fib(x-1)	# dynamic error: function fib called recursively

fib(5)
```

This rule, combined with the invariant that all loops are iterations over finite sequences, implies that Starlark programs are not Turing-complete. However, an implementation may allow clients to disable this check, allowing unbounded recursion.

### Built-in functions

A built-in function is a function or method implemented by the interpreter or the application into which the interpreter is embedded. Its type is `"builtin_function_or_method"`.

A built-in function value used in a Boolean context is always considered true.

Many built-in functions are predeclared in the environment; see Name Resolution. Some built-in functions such as `len` are *universal*, that is, available to all Starlark programs. The host application may predeclare additional built-in functions in the environment of a specific module.

Except where noted, built-in functions accept only positional arguments.
