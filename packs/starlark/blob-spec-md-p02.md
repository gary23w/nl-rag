---
title: "starlark/spec.md at master · bazelbuild/starlark · GitHub (part 2/4)"
source: https://github.com/bazelbuild/starlark/blob/master/spec.md
domain: starlark
license: Apache-2.0
tags: starlark language, bazel build language, python-like config dialect, starlark scripting
fetched: 2026-07-02
part: 2/4
---

## Name binding and variables

After a Starlark file is parsed, but before its execution begins, the Starlark interpreter checks statically that the program is well formed. For example, `break` and `continue` statements may appear only within a `for` statement; `if`, `for`, and `return` statements may appear only within a function; and `load` statements may appear only outside any function.

*Name resolution* is the static checking process that resolves names to variable bindings. During execution, names refer to variables. Statically, names denote places in the code where variables are created; these places are called *bindings*. A name may denote different bindings at different places in the program. The region of text in which a particular name refers to the same binding is called that binding's *scope*.

Four Starlark constructs bind names, as illustrated in the example below: `load` statements (`a` and `b`), `def` statements (`c`), function parameters (`d`), and assignments (`e`, `h`, including the augmented assignment `e += h`). Variables may be assigned or re-assigned explicitly (`e`, `h`), or implicitly, as in a `for` statement (`f`) or comprehension `for` clause (`g`, `i`).

```highlight
load("lib.star", "a", b="B")

def c(d):
  e = 0
  for f in d:
     print([True for g in f])
     e += 1

h = [2*i for i in a]
```

The environment of a Starlark program is structured as a tree of *lexical blocks*, each of which may contain name bindings. The tree of blocks is parallel to the syntax tree. Blocks are of five kinds.

At the root of the tree is the *predeclared* block, which binds several names implicitly. The set of predeclared names includes the universal constant values `None`, `True`, and `False`, and various built-in functions such as `len` and `list`; these functions are immutable and stateless. An application may pre-declare additional names to provide domain-specific functions to that file, for example. These additional functions may have side effects on the application. Starlark programs cannot change the set of predeclared bindings or assign new values to them (but they can be redefined in a smaller block).

Nested beneath the predeclared block is the *module* block, which contains the bindings of the current module. Bindings in the module block (such as `a`, `b`, `c`, and `h` in the example) are called *global* and may be visible to other modules. The module block is empty at the start of the file and is populated by top-level binding statements, but an application may pre-bind one or more global names, to provide domain-specific functions to that file, for example.

Nested beneath the module block is the *file* block, which contains bindings local to the current file. Names in this block (such as `a` and `b` in the example) are bound only by `load` statements. The sets of names bound in the file block and in the module block do not overlap: it is an error for a load statement to bind the name of a global, or for a top-level statement to bind a name bound by a load statement.

A file block contains a *function* block for each top-level function, and a *comprehension* block for each top-level comprehension. Bindings in either of these kinds of block, and in the file block itself, are called *local*. (In the example, the bindings for `e`, `f`, `g`, and `i` are all local.) Additional functions and comprehensions, and their blocks, may be nested in any order, to any depth.

If name is bound anywhere within a block, all uses of the name within the block are treated as references to that binding, even if the use appears before the binding. This is true even at the top level, unlike Python. The binding of `y` on the last line of the example below makes `y` local to the function `hello`, so the use of `y` in the print statement also refers to the local `y`, even though it appears earlier.

```highlight
y = "goodbye"

def hello():
  for x in (1, 2):
    if x == 2:
      print(y) # prints "hello"
    if x == 1:
      y = "hello"
```

It is a dynamic error to evaluate a reference to a local variable before it has been bound:

```highlight
def f():
  print(x)              # dynamic error: local variable x referenced before assignment
  x = "hello"
```

The same is true for global variables:

```highlight
print(x)                # dynamic error: global variable x referenced before assignment
x = "hello"
```

The same is also true for nested loops in comprehensions. In the (unnatural) examples below, the scope of the variables `x`, `y`, and `z` is the entire compehension block, except the operand of the first loop (`[]` or `[1]`), which is resolved in the enclosing environment. The second loop may thus refer to variables defined by the third (`z`), even though such references would fail if actually executed.

```
[1//0 for x in [] for y in z for z in ()]   # []   (no error)
[1//0 for x in [1] for y in z for z in ()]  # dynamic error: local variable z referenced before assignment
```

It is a static error to refer to a name that has no binding at all.

```
def f():
  if False:
    g()                   # static error: undefined: g
```

(This behavior differs from Python, which treats such references as global, and thus does not report an error until the expression is evaluated.)

It is a static error to bind a global variable already explicitly bound in the file:

```highlight
x = 1
x = 2                   # static error: cannot reassign global x declared on line 1
```

If a name was pre-bound by the application, the Starlark program may explicitly bind it, but only once.

An augmented assignment statement such as `x += 1` is considered a binding of `x`. It is therefore a static error to use it on a global variable.

A name appearing after a dot, such as `split` in `get_filename().split('/')`, is not resolved statically. The dot expression `.split` is a dynamic operation on the value returned by `get_filename()`.


## Value concepts

Starlark has over a dozen core data types. An application that embeds the Starlark intepreter may define additional types that behave like Starlark values. All values, whether core or application-defined, implement a few basic behaviors:

```
str(x)		-- return a string representation of x
type(x)		-- return a string describing the type of x
bool(x)		-- convert x to a Boolean truth value
hash(x)		-- return a hash code for x
```

### Identity and mutation

Starlark is an imperative language: programs consist of sequences of statements executed for their side effects. For example, an assignment statement updates the value held by a variable, and calls to some built-in functions such as `print` change the state of the application that embeds the interpreter.

Values of some data types, such as `NoneType`, `bool`, `int`, `float`, `string`, and `bytes`, are *immutable*; they can never change. Immutable values have no notion of *identity*: it is impossible for a Starlark program to tell whether two integers, for instance, are represented by the same object; it can tell only whether they are equal.

Values of other data types, such as `list` and `dict`, are *mutable*: they may be modified by a statement such as `a[i] = 0` or `items.clear()`. Although `tuple` and `function` values are not directly mutable, they may refer to mutable values indirectly, so for this reason we consider them mutable too. Starlark values of these types are actually *references* to variables.

Copying a reference to a variable, using an assignment statement for instance, creates an *alias* for the variable, and the effects of operations applied to the variable through one alias are visible through all others.

```highlight
x = []                          # x refers to a new empty list variable
y = x                           # y becomes an alias for x
x.append(1)                     # changes the variable referred to by x
print(y)                        # "[1]"; y observes the mutation
```

Starlark uses *call-by-value* parameter passing: in a function call, argument values are assigned to function parameters as if by assignment statements. If the values are references, the caller and callee may refer to the same variables, so if the called function changes the variable referred to by a parameter, the effect may also be observed by the caller:

```highlight
def f(y):
    y.append(1)                 # changes the variable referred to by x

x = []                          # x refers to a new empty list variable
f(x)                            # f's parameter y becomes an alias for x
print(x)                        # "[1]"; x observes the mutation
```

As in all imperative languages, understanding *aliasing*, the relationship between reference values and the variables to which they refer, is crucial to writing correct programs.

### Freezing a value

Starlark has a feature unusual among imperative programming languages: a mutable value may be *frozen* so that all subsequent attempts to mutate it fail with a dynamic error; the value, and all other values reachable from it, become *immutable*.

Immediately after execution of a Starlark module, all values in its top-level environment are frozen. Because all the global variables of an initialized Starlark module are immutable, the module may be published to and used by other threads in a parallel program without the need for locks. For example, the Bazel build system loads and executes BUILD and .bzl files in parallel, and two modules being executed concurrently may freely access variables or call functions from a third without the possibility of a race condition.

### Hashing

The `dict` data type is implemented using hash tables, so only *hashable* values are suitable as keys of a `dict`. Attempting to use a non-hashable value as the key in a dictionary results in a dynamic error.

The hash of a value is an unspecified integer chosen so that two equal values have the same hash, in other words, `x == y => hash(x) == hash(y)`. A hashable value has the same hash throughout its lifetime.

Values of the types `NoneType`, `bool`, `int`, `float`, `string`, and `bytes`, which are all immutable, are hashable.

Values of mutable types such as `list` and `dict` are not hashable, unless they have become immutable due to *freezing*.

A `tuple` value is hashable only if all its elements are hashable. Thus `("localhost", 80)` is hashable but `([127, 0, 0, 1], 80)` is not.

Values of the types `function` and `builtin_function_or_method` are also hashable. Although functions are not necessarily immutable, as they may be closures that refer to mutable variables, instances of these types are compared by reference identity (see Comparisons), so their hash values are derived from their identity.

### Collection types

Starlark defines several abstract data types. Although these are not directly referenced by name in Starlark programs, they are useful concepts for understanding what operations a type supports and for documenting what types a function expects.

- `Collection`: A type that is: Examples include `list`, `tuple`, `set`, and `dict` (its elements are its keys), but not `string` or `bytes` since they are not iterable.
  - *iterable* (can appear on the right-hand side of a `for` loop, whether that be a `for` statement or comprehension `for` clause),
  - can have its length taken via the `len()` function, and
  - supports testing for membership via the `in` operator.
- `Sequence`: A `Collection` that additionally supports subscript and slicing expressions, following the semantics of indexing. `list` and `tuple` are `Sequence`s, but not `set` or `dict`.
- `Mapping`: A `Collection` of keys associated with values, where a value can be retrieved by subscripting with the key. `dict` is the only example of a `Mapping` in the core language.

Applications may define additional data structures that may or may not have a particular abstract data type. If it does have the type, it must support all of its required operations, but the converse is not necessarily true.

### Iteration

It is a dynamic error to mutate a collection such as a list, set, or dictionary while iterating over it. This helps avoid a common source of errors and implementation pitfalls. For example, the following code snippet is syntactically valid in both Python and Starlark:

```highlight
a = [5, 11, 12, 13, 8]
for x in a:
    if x > 10:
        a.remove(x)
```

In Python, the result is `[5, 12, 8]` -- the `12` is missed due to the implicit iterator's internal integer indexing. But in Starlark, an error is raised at the attempt to mutate `a` inside the loop. The same code would succeed with the correct result in both languages if the loop were rewritten as `for x in list(a)`.

Unlike Python 3, the result of certain methods like `enumerate()` or `zip()` is a new list rather than an iterator object. Loops over such lists will not prevent modifying the original list.

### Indexing

Many Starlark operators and functions require an index operand `i`, such as `a[i]` or `list.insert(i, x)`. Others require two indices `i` and `j` that indicate the start and end of a subsequence, such as `a[i:j]`, `list.index(x, i, j)`, or `string.find(x, i, j)`. All such operations follow similar conventions, described here.

Indexing in Starlark is *zero-based*. The first element of a string or list has index 0, the next 1, and so on. The last element of a sequence of length `n` has index `n-1`.

```highlight
"hello"[0]			# "h"
"hello"[4]			# "o"
"hello"[5]			# error: index out of range
```

For subsequence operations that require two indices, the first is *inclusive* and the second *exclusive*. Thus `a[i:j]` indicates the sequence starting with element `i` up to but not including element `j`. The length of this subsequence is `j-i`. This convention is known as *half-open indexing*.

```highlight
"hello"[1:4]			# "ell"
```

Either or both of the index operands may be omitted. If omitted, the first is treated equivalent to 0 and the second is equivalent to the length of the sequence:

```highlight
"hello"[1:]                     # "ello"
"hello"[:4]                     # "hell"
```

It is permissible to supply a negative integer to an indexing operation. The effective index is computed from the supplied value by the following two-step procedure. First, if the value is negative, the length of the sequence is added to it. This provides a convenient way to address the final elements of the sequence:

```highlight
"hello"[-1]                     # "o",  like "hello"[4]
"hello"[-3:-1]                  # "ll", like "hello"[2:4]
```

Second, for subsequence operations, if the value is still negative, it is replaced by zero, or if it is greater than the length `n` of the sequence, it is replaced by `n`. In effect, the index is "truncated" to the nearest value in the range `[0:n]`.

```highlight
"hello"[-1000:1000]		# "hello"
```

This truncation step does not apply to indices of individual elements:

```highlight
"hello"[-6]		# error: index out of range
"hello"[-5]		# "h"
"hello"[4]		# "o"
"hello"[5]		# error: index out of range
```


## Expressions

An expression specifies the computation of a value.

The Starlark grammar defines several categories of expression. An *operand* is an expression consisting of a single token (such as an identifier or a literal), or a bracketed expression. Operands are self-delimiting. An operand may be followed by any number of dot, call, or slice suffixes, to form a *primary* expression. In some places in the Starlark grammar where an expression is expected, it is legal to provide a comma-separated list of expressions denoting a tuple. The grammar uses `Expressions` where a multiple-component expression is allowed, and `Expression` where it accepts an expression of only a single component.

```
Expressions = Expression {',' Expression} .

Expression = IfExpr | PrimaryExpr | UnaryExpr | BinaryExpr | LambdaExpr .

PrimaryExpr = Operand
            | PrimaryExpr DotSuffix
            | PrimaryExpr CallSuffix
            | PrimaryExpr SubscriptSuffix
            .

Operand = identifier
        | int | float | string | bytes
        | ListExpr | ListComp
        | DictExpr | DictComp
        | '(' [Expressions] [,] ')'
        .

DotSuffix       = '.' identifier .
CallSuffix      = '(' [Arguments [',']] ')' .
SubscriptSuffix = '[' [Expressions] [':' Expression [':' Expression]] ']'
                | '[' Expressions ']'
                .
```

### Identifiers

```
Operand = identifier
```

An identifier is a name that identifies a value.

Lookup of locals and globals may fail if not yet defined.

### Literals

Starlark supports literals of four different kinds:

```
Operand = int | float | string | bytes
```

Evaluation of an int, float, string, or bytes literal yields the value of that literal. See [Literals](#lexical elements) for details.

### Parenthesized expressions

```
Operand = '(' [Expressions] ')'
```

A single expression enclosed in parentheses yields the result of that expression. Explicit parentheses may be used for clarity, or to override the default association of subexpressions.

```highlight
1 + 2 * 3 + 4                   # 11
(1 + 2) * (3 + 4)               # 21
```

If the parentheses are empty, or contain a single expression followed by a comma, or contain two or more expressions, the expression yields a tuple.

```highlight
()                              # (), the empty tuple
(1,)                            # (1,), a tuple of length 1
(1, 2)                          # (1, 2), a 2-tuple or pair
(1, 2, 3)                       # (1, 2, 3), a 3-tuple or triple
```

In some contexts, such as a `return` or assignment statement or the operand of a `for` statement, a tuple may be expressed without parentheses.

```highlight
x, y = 1, 2

return 1, 2

for x in 1, 2:
   print(x)
```

Starlark (like Python 3) does not accept an unparenthesized tuple or lambda expression as the operand of a `for` clause in a comprehension:

```highlight
[2*x for x in 1, 2, 3]	       	# parse error: unexpected ','
[2*x for x in lambda: 0]       	# parse error: unexpected 'lambda'
```

### Dictionary expressions

A dictionary expression is a comma-separated list of colon-separated key/value expression pairs, enclosed in curly brackets, and it yields a new dictionary object. An optional comma may follow the final pair.

```
DictExpr = '{' [Entries [',']] '}' .
Entries  = Entry {',' Entry} .
Entry    = Expression ':' Expression .
```

Examples:

```highlight
{}
{"one": 1}
{"one": 1, "two": 2,}
```

The key and value expressions are evaluated in left-to-right order. Evaluation fails if the same key is used multiple times.

Only hashable values may be used as the keys of a dictionary.

### List expressions

A list expression is a comma-separated list of element expressions, enclosed in square brackets, and it yields a new list object. An optional comma may follow the last element expression.

```
ListExpr = '[' [Expressions [',']] ']' .
```

Element expressions are evaluated in left-to-right order.

Examples:

```highlight
[]                      # [], empty list
[1]                     # [1], a 1-element list
[1, 2, 3,]              # [1, 2, 3], a 3-element list
```

### Unary operators

There are four unary operators, all appearing before their operand: `+`, `-`, `~`, and `not`.

```
UnaryExpr = '+' Expression
          | '-' Expression
          | '~' Expression
          | 'not' Expression
          .
```

```
+ number        unary positive          (int, float)
- number        unary negation          (int, float)
~ number        unary bitwise inversion (int)
not x           logical negation        (any type)
```

The `+` and `-` operators may be applied to any number: `+` yields the operand unchanged, and `-` yields its negation. The `+` operator is never necessary in a correct program but may serve as an assertion that its operand is a number, or as documentation.

```highlight
if x > 0:
	return +1
elif x < 0:
	return -1
else:
	return 0
```

The `not` operator returns the negation of the truth value of its operand.

```highlight
not True                        # False
not False                       # True
not [1, 2, 3]                   # False
not ""                          # True
not 0                           # True
```

The `~` operator yields the bitwise inversion of its integer argument. The bitwise inversion of x is defined as -(x+1).

```highlight
~1                              # -2
~-1                             # 0
~0                              # -1
```

### Binary operators

Starlark has the following binary operators, arranged in order of increasing precedence:

```
or
and
==   !=   <   >   <=   >=   in   not in
|
^
&
<< >>
-   +
*   /   //   %
```

Comparison operators, `in`, and `not in` are non-associative, so the parser will not accept `0 <= i < n`. All other binary operators of equal precedence associate to the left.

```
BinaryExpr = Expression {Binop Expression} .

Binop = 'or'
      | 'and'
      | '==' | '!=' | '<' | '>' | '<=' | '>=' | 'in' | 'not' 'in'
      | '|'
      | '^'
      | '&'
      | '<<' | '>>'
      | '-' | '+'
      | '*' | '%' | '/' | '//'
      .
```

#### `or` and `and`

The `or` and `and` operators yield, respectively, the logical disjunction and conjunction of their arguments, which need not be Booleans. The expression `x or y` yields the value of `x` if its truth value is `True`, or the value of `y` otherwise.

```highlight
False or False		# False
False or True		# True
True  or False		# True
True  or True		# True

0 or "hello"		# "hello"
1 or "hello"		# 1
```

Similarly, `x and y` yields the value of `x` if its truth value is `False`, or the value of `y` otherwise.

```highlight
False and False		# False
False and True		# False
True  and False		# False
True  and True		# True

0 and "hello"		# 0
1 and "hello"		# "hello"
```

These operators use "short circuit" evaluation, so the second expression is not evaluated if the value of the first expression has already determined the result, allowing constructions like these:

```highlight
len(x) > 0 and x[0] == 1		# x[0] is not evaluated if x is empty
x and x[0] == 1
len(x) == 0 or x[0] == ""
not x or not x[0]
```

#### Comparisons

The `==` operator reports whether its operands are equal; the `!=` operator is its negation.

The operators `<`, `>`, `<=`, and `>=` perform an ordered comparison of their operands. It is an error to apply these operators to operands of unequal type, unless one of the operands is an `int` and the other is a `float`. Of the built-in types, only the following support ordered comparison, using the ordering relation shown:

```
bool            # False < True
int             # mathematical
float           # as defined by IEEE 754, except NaN > +Inf
string          # lexicographical
bytes           # lexicographical
tuple           # lexicographical
list            # lexicographical
```

Comparison of floating-point values follows the IEEE 754 standard for finite values (including -0.0) and for positive and negative infinity, but not for `NaN` values, for which the standard behavior would break several mathematical identities. Thus:

```
-Inf < -1e50 < -1.0 < -1e-50 < 0.0 < 1e-50 < 1.0 < 1e50 < +Inf < NaN
+0.0 == -0.0
NaN == NaN
```

Applications may define additional types that support ordered comparison. The application-defined comparison relation must be a strict weak ordering.

The remaining built-in types support only equality comparisons. Values of type `dict` compare equal if their elements compare equal, and values of type `function` are equal only to themselves.

```
dict                            # equal contents
function                        # identity
```

#### Arithmetic operations

The following table summarizes the binary arithmetic operations available for built-in types:

```
Arithmetic (int or float; result has type float unless both operands have type int)
   number + number              # addition
   number - number              # subtraction
   number * number              # multiplication
   number / number              # floating-point division (result is always a float)
   number // number             # floored division
   number % number              # remainder of floored division

Bitwise operations:
   int ^ int                    # bitwise XOR
   int & int                    # bitwise AND
   int | int                    # bitwise OR
   int << int                   # bitwise left shift
   int >> int                   # bitwise right shift (arithmetic)

Set operations:
   set & set                    # set intersection
   set - set                    # set difference
   set ^ set                    # set symmetric difference

Concatenation
   string + string
    bytes + bytes
     list + list
    tuple + tuple

Repetition (string/bytes/list/tuple)
      int * sequence
 sequence * int

String interpolation
   string % any                 # see String Interpolation

Set or dictionary union
     dict | dict                # see Dictionaries, Sets
```

The operands of the arithmetic operators `+`, `-`, `*`, `//`, and `%`, must both be numbers (`int` or `float`) but need not have the same type. The type of the result has type `int` only if both operands have that type. The result of floating-point division `/` always has type `float`.

The `&` operator requires two operands of type `int`, and yields the bitwise intersection (AND) of its operands. The `|` operator likewise computes bitwise union, and the `^` operator bitwise XOR (exclusive OR).

The `<<` and `>>` operators require two operands of type `int`. They shift the first operand to the left or right by the number of bits given by the second operand. Right shifts are arithmetic, not logical: they fill the vacated bits with copies of the sign bit. It is a dynamic error if the second operand is negative.

```highlight
0x12345678 & 0xFF               # 0x00000078
0x12345678 | 0xFF               # 0x123456FF
0b01011101 ^ 0b110101101        # 0b111110000
0b01011101 >> 2                 # 0b010111
0b01011101 << 2                 # 0b0101110100
-1 >> 100                       # -1
```

The `+` operator may be applied to non-numeric operands of the same type, such as two lists, two tuples, two strings, or two bytes, in which case it computes the concatenation of the two operands and yields a new value of the same type.

```highlight
"Hello, " + "world"		# "Hello, world"
(1, 2) + (3, 4)			# (1, 2, 3, 4)
[1, 2] + [3, 4]			# [1, 2, 3, 4]
```

The `*` operator may be applied to an integer *n* and a value of type `string`, `bytes`, `list`, or `tuple`, in which case it yields a new value of the same sequence type consisting of *n* repetitions of the original sequence. The order of the operands is immaterial. Negative values of *n* behave like zero.

```highlight
'mur' * 2               # 'murmur'
3 * (True, "a")         # (True, "a", True, "a", True, "a")
```

Applications may define additional types that support any subset of these operators.

#### Membership tests

```
      any in     sequence		(list, tuple, dict, set, string, bytes, range)
      any not in sequence
```

The `in` operator reports whether its first operand is a member of its second operand, which must be a list, tuple, dict, set, string, or bytes. The `not in` operator is its negation. Both return a Boolean.

The meaning of membership varies by the type of the second operand: the members of a list or tuple are its elements; the members of a dict are its keys; the members of a string or bytes are all its substrings. Additionally, the members of a bytes include the int values of its (byte) elements.

```highlight
1 in [1, 2, 3]                  # True
4 not in (1, 2, 3)              # True

d = {"one": 1, "two": 2}
"one" in d                      # True
"three" in d                    # False
1 in d                          # False

"nasty" in "dynasty"            # True
"a" in "banana"                 # True
"f" not in "way"                # True

b"nasty" in b"dynasty"          # True
97 in b"abc"                    # True (97 = 'a')
```

#### String interpolation

The expression `format % args` performs *string interpolation*, a simple form of template expansion. The `format` string is interpreted as a sequence of literal portions and *conversions*. Each conversion, which starts with a `%` character, is replaced by its corresponding value from `args`. The characters following `%` in each conversion determine which argument it uses and how to convert it to a string.

Each `%` character marks the start of a conversion specifier, unless it is immediately followed by another `%`, in which cases both characters together denote a single literal percent sign.

The conversion's operand is the next element of `args`, which must be a tuple with exactly one component per conversion, unless the format string contains only a single conversion, in which case `args` itself is its operand.

Starlark does not support the flag, width, and padding specifiers supported by Python's `%` and other variants of C's `printf`.

After the `%` comes a single letter indicating what operand types are valid and how to convert the operand `x` to a string:

```
%       none            literal percent sign
s       any             as if by str(x)
r       any             as if by repr(x)
d       number          signed integer decimal
o       number          signed octal, no 0o prefix
x       number          signed hexadecimal, lowercase, no 0x prefix
X       number          signed hexadecimal, uppercase, no 0x prefix
e       number          float exponential format, lowercase (1.230000e+12)
E       number          float exponential format, uppercase (1.230000E+12)
f       number          float decimal format                (1230000000000.000000)
F       number          same as %f
g       number          compact format, lowercase           (0.0, 1.1, 1200, 1e+45, 1.2e+12)
G       number          compact format, uppercase           (0.0, 1.1, 1200, 1e+45, 1.2E+12)
```

The compact form `%g` is also used by `str(float)`. Its result uses the least precision required to accurately represent the value, omits unnecessary trailing zeros in the significand (along with the decimal point itself if the significand has no fraction), and always contains a decimal point or an exponent and thus unambiguously denotes a `float`, not an `int`.

It is an error if the argument does not have the type required by the conversion specifier, except that ints may converted to floats and floats may truncated to ints. A Boolean argument is not considered a number.

Examples:

```highlight
"Hello %s" % "Bob"                              # "Hello Bob"

"Hello %s, your score is %d" % ("Bob", 75)      # "Hello Bob, your score is 75"
)
```

One subtlety: to use a tuple as the operand of a conversion in format string containing only a single conversion, you must wrap the tuple in a singleton tuple:

```highlight
"coordinates=%s" % (40, -74)	# error: too many arguments for format string
"coordinates=%s" % ((40, -74),)	# "coordinates=(40, -74)"
```

### Conditional expressions

A conditional expression has the form `a if cond else b`. It first evaluates the condition `cond`. If it's true, it evaluates `a` and yields its value; otherwise it yields the value of `b`.

```
IfExpr = Expression 'if' Expression 'else' Expression .
```

Example:

```highlight
"yes" if enabled else "no"
```

During parsing, the `if` operator, considered as a postfix operator on the "true" expression, has higher precedence than `else` (a prefix operator on the "false" expression), which in turn has higher precedence than the `lambda` prefix operator.

```highlight
a if b else (c if d else e)          # parens are redundant
(a if b else c) if d else e          # parens are required

lambda: (a if b else c)              # parens are redunant
(lambda: a) if b else c              # parens are required

a if b else lambda: (c if d else e)  # parens are redundant
a if b else (lambda: c if d else e)  # parens are required
(a if b else lambda: c) if d else e  # parens are required
```

### Comprehensions

A comprehension constructs new list or dictionary value by looping over one or more iterables and evaluating a *body* expression that produces successive elements of the result.

A list comprehension consists of a single expression followed by one or more *clauses*, the first of which must be a `for` clause. Each `for` clause resembles a `for` statement, and specifies an iterable operand and a set of variables to be assigned by successive values of the iterable. An `if` cause resembles an `if` statement, and specifies a condition that must be met for the body expression to be evaluated. A sequence of `for` and `if` clauses acts like a nested sequence of `for` and `if` statements.

```
ListComp = '[' Expression {CompClause} ']'.
DictComp = '{' Entry {CompClause} '}' .

CompClause = 'for' LoopVariables 'in' Expression
           | 'if' Expression .

LoopVariables = PrimaryExpr {',' PrimaryExpr} .
```

Examples:

```highlight
[x*x for x in range(5)]                 # [0, 1, 4, 9, 16]
[x*x for x in range(5) if x%2 == 0]     # [0, 4, 16]
[(x, y) for x in range(5)
        if x%2 == 0
        for y in range(5)
        if y > x]                       # [(0, 1), (0, 2), (0, 3), (0, 4), (2, 3), (2, 4)]
```

A dict comprehension resembles a list comprehension, but its body is a pair of expressions, `key: value`, separated by a colon, and its result is a dictionary containing the key/value pairs for which the body expression was evaluated. Evaluation fails if the value of any key is unhashable.

As with a `for` statement, the loop variables may exploit compound assignment:

```highlight
[x*y+z for (x, y), z in [((2, 3), 5), (("o", 2), "!")]]         # [11, 'oo!']
```

Starlark, following Python 3, does not accept an unparenthesized tuple as the operand of a `for` clause:

```highlight
[x*x for x in 1, 2, 3]		# parse error: unexpected comma
```

Comprehensions in Starlark, again following Python 3, define a new lexical block, so assignments to loop variables have no effect on variables of the same name in an enclosing block:

```highlight
x = 1
_ = [x for x in [2]]            # new variable x is local to the comprehension
print(x)                        # 1
```

### Function and method calls

```
CallSuffix = '(' [Arguments [',']] ')' .

Arguments = Argument {',' Argument} .
Argument  = Expression | identifier '=' Expression | '*' Expression | '**' Expression .
```

A value `f` of type `function` may be called using the expression `f(...)`. Applications may define additional types whose values may be called in the same way.

A method call such as `filename.endswith(".sky")` is the composition of two operations, `m = filename.endswith` and `m(".sky")`. The first, a dot operation, yields a *bound method*, a function value that pairs a receiver value (the `filename` string) with a choice of method (string·endswith).

Only built-in or application-defined types may have methods.

See Functions for an explanation of function parameter passing.

### Dot expressions

A dot expression `x.f` selects the attribute `f` (a field or method) of the value `x`.

Fields are possessed by none of the main Starlark data types, but some application-defined types have them. Methods belong to the built-in types `string`, `list`, `dict`, and `set` and to many application-defined types.

```
DotSuffix = '.' identifier .
```

A dot expression fails if the value does not have an attribute of the specified name.

Use the built-in function `hasattr(x, "f")` to ascertain whether a value has a specific attribute, or `dir(x)` to enumerate all its attributes. The `getattr(x, "f")` function can be used to select an attribute when the name `"f"` is not known statically.

A dot expression that selects a method typically appears within a call expression, as in these examples:

```highlight
["able", "baker", "charlie"].index("baker")     # 1
"banana".count("a")                             # 3
"banana".reverse()                              # error: string has no .reverse field or method
```

But when not called immediately, the dot expression evaluates to a *bound method*, that is, a method coupled to a specific receiver value. A bound method can be called like an ordinary function, without a receiver argument:

```highlight
f = "banana".count
f                                               # <built-in method count of string value>
f("a")                                          # 3
f("n")                                          # 2
```

### Subscript expressions

A subscript expression `a[x]` retrieves a value identified by `x` from the value `a`.

```
SubscriptSuffix = '[' Expressions ']' .
```

There are two main cases: indexing a sequence, and retrieving values of a mapping.

When `a` is a `Sequence` (such as a `list` or `tuple`), or another indexable object like `string` or `bytes`, the expression `a[i]` yields the `i`th element of `a`. Here, `i` must be an `int` value in the range `-n` ≤ `i` < `n`, where `n` is `len(a)`; any other index results in an error.

A valid negative index `i` behaves like the non-negative index `n+i`, allowing for convenient indexing relative to the end of the sequence.

```highlight
"abc"[0]                        # "a"
"abc"[1]                        # "b"
"abc"[-1]                       # "c"

("zero", "one", "two")[0]       # "zero"
("zero", "one", "two")[1]       # "one"
("zero", "one", "two")[-1]      # "two"
```

For a subscript expression `m[k]`, where the value of `m` is a `Mapping` (most commonly a `dict`) or any other mapping-like object, the expression retrieves the value that `m` associates with `k`. It is an error if `m` contains no such key `k`.

A subscript expression appearing on the left side of an assignment causes the specified sequence element or mapping value to be updated:

```highlight
a = range(10, 13)       # a == [10, 11, 12]
a[2] = 7                # a == [10, 11, 7]

coins = {}              # coins == {}
coins["suzie b"] = 100  # coins == {"suzie b": 100}
```

It is a dynamic error to attempt to update an element of an immutable type, such as a tuple or string, or a frozen value of a mutable type.

Starlark does not have a `del` statement like Python. Deleting the value associated with an index or key requires calling a method on the containing object.

### Slice expressions

The slice expression acts as a sort of indexing subscript expression that retrieves a range of elements rather than a single element. It applies to types that can be indexed with an integer as above, such as `Sequence`s, `string`, and `bytes`.

```
SubscriptSuffix = '[' [Expressions] [':' Expression [':' Expression]] ']' .
```

A slice expression `a[start:stop:stride]` yields a copy of `a` containing exactly the values whose indices are in the specified range. Conceptually, the range begins at `start`, progresses in increments of `stride`, and ends before reaching `stop`, without ever going out-of-bounds.

Each of the `start`, `stop`, and `stride` operands may be `None` or omitted entirely; otherwise, they must evaluate to integers. If `stride` is omitted then the second colon may optionally also be omitted. (The first colon is syntactically required in order to distinguish from a subscript expression.)

If `stride` is omitted its value defaults to 1. It is an error to specify a `stride` of 0.

The effective start and stop indices are computed from the three operands as follows. Let `n` be the length of the sequence.

**If the stride is positive:** If the `start` operand was omitted, it defaults to -infinity. If the `end` operand was omitted, it defaults to +infinity. For either operand, if a negative value was supplied, `n` is added to it. The `start` and `end` values are then "clamped" to the nearest value in the range 0 to `n`, inclusive.

**If the stride is negative:** If the `start` operand was omitted, it defaults to +infinity. If the `end` operand was omitted, it defaults to -infinity. For either operand, if a negative value was supplied, `n` is added to it. The `start` and `end` values are then "clamped" to the nearest value in the range -1 to `n`-1, inclusive.

```highlight
"abc"[1:]               # "bc"  (remove first element)
"abc"[:-1]              # "ab"  (remove last element)
"abc"[1:-1]             # "b"   (remove first and last element)
"banana"[1::2]          # "aaa" (select alternate elements starting at index 1)
"banana"[4::-2]         # "nnb" (select alternate elements in reverse, starting at index 4)
```

Unlike Python, Starlark does not allow a slice expression to be the target of an assignment, although it may appear as a subexpression in the target.

Slicing a tuple, string, or bytes may be more efficient than slicing a list because tuple, string, and bytes values are immutable, so the result of the operation can share the underlying representation of the original operand (when the stride is 1). By contrast, slicing a list requires the creation of a new list and copying of the necessary elements.

### Lambda expressions

A `lambda` expression yields a new function value.

```
LambdaExpr = 'lambda' [Parameters] ':' Expression .
```

Syntactically, a lambda expression consists of the keyword `lambda`, followed by a parameter list like that of a `def` statement but unparenthesized, then a colon `:`, and a single expression, the *function body*.

Example:

```highlight
def map(f, list):
    return [f(x) for x in list]

map(lambda x: 2*x, range(3))    # [2, 4, 6]
```

As with functions created by a `def` statement, a lambda function captures the syntax of its body, the default values of any optional parameters, a reference to each free variable appearing in its body, and the global dictionary of the current module.

The name of a function created by a lambda expression is `"lambda"`.

The two statements below are essentially equivalent, but the function created by the `def` statement is named `twice` and the function created by the lambda expression is named `lambda`.

```highlight
def twice(x):
   return x * 2

twice = lambda x: x * 2
```
