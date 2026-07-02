---
title: "starlark/spec.md at master · bazelbuild/starlark · GitHub (part 3/4)"
source: https://github.com/bazelbuild/starlark/blob/master/spec.md
domain: starlark
license: Apache-2.0
tags: starlark language, bazel build language, python-like config dialect, starlark scripting
fetched: 2026-07-02
part: 3/4
---

## Statements

```
Statement  = DefStmt | IfStmt | ForStmt | SimpleStmt .
SimpleStmt = SmallStmt {';' SmallStmt} [';'] '\n' .
SmallStmt  = ReturnStmt
           | BreakStmt | ContinueStmt | PassStmt
           | AssignStmt
           | ExprStmt
           | LoadStmt
           .
```

### Pass statements

A `pass` statement does nothing. Use a `pass` statement when the syntax requires a statement but no behavior is required, such as the body of a function that does nothing.

```
PassStmt = 'pass' .
```

Example:

```highlight
def noop():
   pass

def list_to_dict(items):
  # Convert list of tuples to dict
  m = {}
  for k, m[k] in items:
    pass
  return m
```

### Assignments

An assignment statement has the form `lhs = rhs`. It evaluates the expression on the right-hand side then assigns its value (or values) to the variable (or variables) on the left-hand side.

```
AssignStmt = Expressions '=' Expressions .
```

The expression on the left-hand side is called a *target*. The simplest target is the name of a variable, but a target may also have the form of a subscript expression to update the element of a list or dictionary, or the form of a dot expression to update the field of an object. These forms may be nested.

```highlight
k = 1
a[i] = v
o.f = ""
o.g(1)[2] = None
```

Compound targets may consist of a comma-separated list of subtargets, optionally surrounded by parentheses or square brackets. These too may be nested. An assignment to a compound target checks that the right-hand value is a sequence with the same number of elements as the target. Each element of the sequence is then assigned to the corresponding element of the target, recursively applying the same logic.

```highlight
a, b = 2, 3
(x, y) = f()
[zero, one, two] = range(3)
[] = ()
```

The same process for assigning a value to a target expression is used in `for` statements and in comprehension `for` clauses.

### Augmented assignments

An augmented assignment, which has the form `lhs op= rhs` updates the variable `lhs` by applying a binary arithmetic operator `op` (one of `+`, `-`, `*`, `/`, `//`, `%`, `&`, `|`, `^`, `<<`, `>>`) to the previous value of `lhs` and the value of `rhs`.

```
AssignStmt = Expressions ('=' | '+=' | '-=' | '*=' | '/=' | '//=' | '%=' | '&=' | '|=' | '^=' | '<<=' | '>>=') Expressions .
```

The left-hand side must be a simple target: a name, a subscript expression, or a dot expression.

```highlight
x -= 1
x.filename += ".sky"
a[index()] *= 2
```

Any subexpressions in the target on the left-hand side are evaluated exactly once, before the evaluation of `rhs`. The first two assignments above are thus equivalent to:

```highlight
x = x - 1
x.filename = x.filename + ".sky"
```

and the third assignment is similar in effect to the following two statements but does not declare a new temporary variable `i`:

```highlight
i = index()
a[i] = a[i] * 2
```

### Function definitions

A `def` statement creates a named function and assigns it to a variable.

```
DefStmt = 'def' identifier '(' [Parameters [',']] ')' ':' Suite .
```

Example:

```highlight
def twice(x):
    return x * 2

str(twice)              # "<function f>"
twice(2)                # 4
twice("two")            # "twotwo"
```

The function's name is preceded by the `def` keyword and followed by the parameter list (which is enclosed in parentheses), a colon, and then an indented block of statements which form the body of the function.

The parameter list is a comma-separated list whose elements are of several kinds. First come zero or more required parameters, which are simple identifiers; all calls must provide an argument value for these parameters.

The required parameters are followed by zero or more optional parameters, of the form `name=expression`. The expression specifies the default value for the parameter for use in calls that do not provide an argument value for it.

The required parameters are optionally followed by a single parameter name preceded by a `*`. This is the called the *varargs* parameter, and it accumulates surplus positional arguments specified by a call. It is conventionally named `*args`.

The varargs parameter may be followed by zero or more parameters, again of the forms `name` or `name=expression`, but these parameters differ from earlier ones in that they are *keyword-only*: if a call provides their values, it must do so as keyword arguments, not positional ones.

Note that even though keyword-only arguments are declared after `*args` in a function's definition, they nevertheless must appear before `*args` in a call to the function.

```highlight
def g(a, *args, b=2, c):
  print(a, b, c, args)

g(1, 3)                 # error: function g missing 1 argument (c)
g(1, *[4, 5], c=3)      # error: keyword argument c may not follow *args
g(1, 4, c=3)            # "1 2 3 (4,)"
g(1, c=3, *[4, 5])      # "1 2 3 (4, 5)"
```

A non-variadic function may also declare keyword-only parameters, by using a bare `*` in place of the `*args` parameter. This form does not declare a parameter but marks the boundary between the earlier parameters and the keyword-only parameters. This form must be followed by at least one optional parameter.

```highlight
def f(a, *, b=2, c):
  print(a, b, c)

f(1)                    # error: function f missing 1 argument (c)
f(1, 3)                 # error: function f accepts 1 positional argument (2 given)
f(1, c=3)               # "1 2 3"
```

Finally, there may be an optional parameter name preceded by `**`. This is called the *keyword arguments* parameter, and accumulates in a dictionary any surplus `name=value` arguments that do not match a prior parameter. It is conventionally named `**kwargs`.

Here are some example parameter lists:

```highlight
def f(): pass
def f(a, b, c): pass
def f(a, b, c=1): pass
def f(a, b, c=1, *args): pass
def f(a, b, c=1, *args, **kwargs): pass
def f(**kwargs): pass
def f(a, b, c=1, *, d=1): pass
```

Execution of a `def` statement creates a new function object. The function object contains: the syntax of the function body; the default value for each optional parameter; a reference to each free variable appearing within the function body; and the global dictionary of the current module.

```highlight
def f(x):
  res = []
  def get_x():
    res.append(x)
  get_x()
  x = 2
  get_x()

f(1) # returns [1, 2]
```

### Return statements

A `return` statement ends the execution of a function and returns a value to the caller of the function.

```
ReturnStmt = 'return' [Expressions] .
```

A return statement may have zero, one, or more result expressions separated by commas. With no expressions, the function has the result `None`. With a single expression, the function's result is the value of that expression. With multiple expressions, the function's result is a tuple.

```highlight
return                  # returns None
return 1                # returns 1
return 1, 2             # returns (1, 2)
```

### Expression statements

An expression statement evaluates an expression and discards its result.

```
ExprStmt = Expressions .
```

Any expression may be used as a statement, but an expression statement is most often used to call a function for its side effects.

```highlight
list.append(1)
```

### If statements

An `if` statement evaluates an expression (the *condition*), then, if the truth value of the condition is `True`, executes a list of statements.

```
IfStmt = 'if' Expression ':' Suite {'elif' Expression ':' Suite} ['else' ':' Suite] .
```

Example:

```highlight
if score >= 100:
    print("You win!")
    return
```

An `if` statement may have an `else` block defining a second list of statements to be executed if the condition is false.

```highlight
if score >= 100:
        print("You win!")
        return
else:
        print("Keep trying...")
        continue
```

It is common for the `else` block to contain another `if` statement. To avoid increasing the nesting depth unnecessarily, the `else` and following `if` may be combined as `elif`:

```highlight
if x > 0:
        result = 1
elif x < 0:
        result = -1
else:
        result = 0
```

An `if` statement is permitted only within a function definition. An `if` statement at top level results in a static error.

### For statements

A `for` statement evaluates its operand, which must be an iterable value. Then, for each element of the iterable, the loop assigns the successive element values to one or more variables and executes a list of statements, the *loop body*.

```
ForStmt = 'for' LoopVariables 'in' Expressions ':' Suite .
```

Example:

```highlight
for x in range(10):
   print(10)
```

The assignment of each value to the loop variables follows the same rules as an ordinary assignment. In this example, two-element lists are repeatedly assigned to the pair of variables (a, i):

```highlight
for a, i in [["a", 1], ["b", 2], ["c", 3]]:
  print(a, i)                          # prints "a 1", "b 2", "c 3"
```

Because Starlark loops always iterate over a finite iterable (assuming the host application does not define an unbounded type), they are guaranteed to terminate, unlike loops in most languages which can execute an arbitrary and perhaps unbounded number of iterations.

Within the body of a `for` loop, `break` and `continue` statements may be used to stop the execution of the loop or advance to the next iteration.

In Starlark, a `for` statement is permitted only within a function definition. A `for` statement at top level results in a static error.

### Break and Continue

The `break` and `continue` statements terminate the current iteration of a `for` statement. Whereas the `continue` statement resumes the loop at the next iteration, a `break` statement terminates the entire loop.

```
BreakStmt    = 'break' .
ContinueStmt = 'continue' .
```

Example:

```highlight
for x in range(10):
    if x%2 == 1:
        continue        # skip odd numbers
    if x > 7:
        break           # stop at 8
    print(x)            # prints "0", "2", "4", "6"
```

Both statements affect only the innermost lexically enclosing loop. It is a static error to use a `break` or `continue` statement outside a loop.

### Load statements

The `load` statement loads another Starlark module, extracts one or more values from it, and binds them to names in the current module.

Syntactically, a load statement looks like a function call `load(...)`.

```
LoadStmt = 'load' '(' string {',' [identifier '='] string} [','] ')' .
```

A load statement requires at least two "arguments". The first must be a literal string; it identifies the module to load. Its interpretation is determined by the application into which the Starlark interpreter is embedded, and is not specified here.

During execution, the application determines what action to take for a load statement. A typical implementation locates and executes a Starlark file, populating a cache of files executed so far to avoid duplicate work, to obtain a module, which is a mapping from global names to values.

The remaining arguments are a mixture of literal strings, such as `"x"`, or named literal strings, such as `y="x"`.

The literal string (`"x"`), which must denote a valid identifier not starting with `_`, specifies the name to extract from the loaded module. In effect, names starting with `_` are not exported. The name (`y`) specifies the local name; if no name is given, the local name matches the quoted name.

```highlight
load("module.sky", "x", "y", "z")       # assigns x, y, and z
load("module.sky", "x", y2="y", "z")    # assigns x, y2, and z
```

A load statement within a function is a static error.


## Module execution

Each Starlark file defines a *module*, which is a mapping from the names of global variables to their values. When a Starlark file is executed, whether directly by the application or indirectly through a `load` statement, a new Starlark thread is created, and this thread executes all the top-level statements in the file. Because `if` statements and `for` statements cannot appear outside of a function, control flows from top to bottom.

If execution reaches the end of the file, module initialization is successful. At that point, the value of each of the module's global variables is frozen, rendering subsequent mutation impossible. The module is then ready for use by another Starlark thread, such as one executing a load statement. Such threads may access values or call functions defined in the loaded module.

A Starlark thread may carry state on behalf of the application into which it is embedded, and application-defined functions may behave differently depending on this thread state. Because module initialization always occurs in a new thread, thread state is never carried from a higher-level module into a lower-level one. The initialization behavior of a module is thus independent of whichever module triggered its initialization.

If a Starlark thread encounters an error, execution stops and the error is reported to the application, along with a backtrace showing the stack of active function calls at the time of the error. If an error occurs during initialization of a Starlark module, any active `load` statements waiting for initialization of the module also fail.

Starlark provides no mechanism by which errors can be handled within the language.


## Built-in constants and functions

The outermost block of the Starlark environment is known as the "predeclared" block. It defines a number of fundamental values and functions needed by all Starlark programs, such as `None`, `True`, `False`, and `len`, and possibly additional application-specific names.

These names are not reserved words so Starlark programs are free to redefine them in a smaller block such as a function body or even at the top level of a module. However, doing so may be confusing to the reader. Nonetheless, this rule permits names to be added to the predeclared block in later versions of the language (or application-specific dialect) without breaking existing programs.

As with built-in functions, built-in methods accept only positional arguments except where noted. The parameter names serve merely as documentation.

### None

`None` is the distinguished value of the type `NoneType`.

### True and False

`True` and `False` are the two values of type `bool`.

### abs

`abs(x)` takes either an integer or a float, and returns the absolute value of that number (a non-negative number with the same magnitude).

### any

`any(x)` returns `True` if any element of the collection `x` is true. If the collection is empty, it returns `False`.

### all

`all(x)` returns `False` if any element of the collection `x` is false. If the collection is empty, it returns `True`.

### bool

`bool(x)` interprets `x` as a Boolean value---`True` or `False`. With no argument, `bool()` returns `False`.

### bytes

`bytes(x)` converts its argument to a `bytes`.

If x is a `bytes`, the result is x.

If x is a string, the result is a `bytes` whose elements are the UTF-8 encoding of the string. Each element of the string that is not part of a valid encoding of a code point is replaced by the UTF-8 encoding of the replacement character, U+FFFD.

If x is an iterable of int values, the result is a `bytes` whose elements are those integers. It is an error if any element is not in the range 0-255.

```highlight
bytes("hello 😃")		# b"hello 😃"
bytes(b"hello 😃")		# b"hello 😃"
bytes("hello 😃"[:-1])          # b"hello ���"
bytes([65, 66, 67])		# b"ABC"
bytes(65)			# error: got int, want string, bytes, or iterable of int
```

### dict

`dict` creates a dictionary. It accepts up to one positional argument, which is interpreted as an iterable of two-element sequences (pairs), each specifying a key/value pair in the resulting dictionary.

`dict` also accepts any number of keyword arguments, each of which specifies a key/value pair in the resulting dictionary; each keyword is treated as a string.

```highlight
dict()                          # {}, empty dictionary
dict([(1, 2), (3, 4)])          # {1: 2, 3: 4}
dict([(1, 2), ["a", "b"]])      # {1: 2, "a": "b"}
dict(one=1, two=2)              # {"one": 1, "two", 1}
dict([(1, 2)], x=3)             # {1: 2, "x": 3}
```

With no arguments, `dict()` returns a new empty dictionary.

`dict(x)` where x is a dictionary returns a new copy of x.

### dir

`dir(x)` returns a new sorted list of the names of the attributes (fields and methods) of its operand. The attributes of a value `x` are the names `f` such that `x.f` is a valid expression.

For example,

```highlight
dir("hello")                    # ['capitalize', 'count', ...], the methods of a string
```

Several types known to the interpreter, such as list, string, and dict, have methods, but none have fields. However, an application may define types with fields that may be read or set by statements such as these:

```
y = x.f
x.f = y
```

### enumerate

`enumerate(x)` returns a list consisting of pairs `(i, v)`, where each successive `v` is the next item of collection `x`, and where `i` starts at 0 and is incremented sequentially. (For sequences, `i` is the index of `v` in `x`, but `enumerate()` can be used on non-sequence collections too.)

The optional second parameter, `start`, specifies an integer value to add to each index.

```highlight
enumerate(["zero", "one", "two"])               # [(0, "zero"), (1, "one"), (2, "two")]
enumerate(["one", "two"], 1)                    # [(1, "one"), (2, "two")]
```

### fail

The `fail(*args)` function causes execution to fail with an error message that includes the string forms of the argument values. The precise formatting depends on the implementation.

```highlight
fail("oops")			# "fail: oops"
fail("oops", 1, False)		# "fail: oops 1 False"
```

### float

`float(x)` interprets its argument as a floating-point number.

If x is a `float`, the result is x.

If x is an `int`, the result is the floating-point value nearest x. The call fails if x is too large to represent as a finite `float`.

If x is a `bool`, the result is `1.0` for `True` and `0.0` for `False`.

If x is a string, the string is interpreted as a floating-point literal. The function also recognizes the names `Inf` (or `Infinity`) and `NaN`, optionally preceded by a `+` or `-` sign. These construct the IEEE 754 non-finite values. Letter case is not significant. The call fails if the literal denotes a value too large to represent as a finite `float`.

With no argument, `float()` returns `0.0`.

### getattr

`getattr(x, name[, default])` returns the value of the attribute (field or method) of x named `name` if it exists. If not, it either returns `default` (if specified) or raises an error.

`getattr(x, "f")` is equivalent to `x.f`.

```highlight
getattr("banana", "split")("a")	       		# ["b", "n", "n", ""], equivalent to "banana".split("a")
getattr("banana", "myattr", "mydefault")	# "mydefault"
```

The three-argument form `getattr(x, name, default)` returns the provided `default` value instead of failing.

### hasattr

`hasattr(x, name)` reports whether x has an attribute (field or method) named `name`.

### hash

`hash(x)` returns an integer hash of a string or bytes x such that two equal values have the same hash. In other words `x == y` implies `hash(x) == hash(y)`. Any other type of argument in an error, even if it is suitable as the key of a dict.

In the interests of reproducibility of Starlark program behavior over time and across implementations, the specific hash function for bytes is 32-bit FNV-1a, and the hash function for strings is the same as that implemented by java.lang.String.hashCode, a simple polynomial accumulator over the UTF-16 transcoding of the string:

```highlight
s[0]*31^(n-1) + s[1]*31^(n-2) + ... + s[n-1]
```

### int

`int(x[, base])` interprets its argument as an integer.

If `x` is an `int`, the result is `x`.

If x is a `float`, the result is the integer value nearest to x, truncating towards zero. It is an error if x is not finite (`NaN` or infinity).

If x is a `bool`, the result is 0 for `False` or 1 for `True`.

If x is a string, it is interpreted as a sequence of digits in the specified base, decimal by default.

If `base` is zero, x is interpreted like an integer literal, the base being inferred from an optional base prefix such as `0b`, `0o`, or `0x` preceding the first digit.

When a nonzero `base` is provided explicitly, its value must be between 2 and 36. The letters `a-z` represent the digits 11 through 35. A matching base prefix is also permitted, and has no effect.

Irrespective of base, the string may start with an optional `+` or `-`, indicating the sign of the result.

```highlight
int("21")          # 21
int("1234", 16)    # 4660
int("0x1234", 16)  # 4660
int("0x1234", 0)   # 4660
int("0b0", 16)     # 176
int("0b111", 0)    # 7
int("0x1234")      # error (invalid base 10 number)
```

### len

`len(x)` returns the number of elements in its argument.

It is a dynamic error if its argument is not a collection, string, or bytes. (Applications may define additional types acceptable to `len()`.)

### list

`list` constructs a list.

`list(x)` returns a new list containing the elements of the iterable `x`.

With no argument, `list()` returns a new empty list.

### max

`max(x)` returns the greatest element in the collection `x`.

It is an error if any element does not support ordered comparison, or if the collection is empty.

The optional named parameter `key` specifies a function to be applied to each element, whose result is used for the comparison in place of the element.

```highlight
max([3, 1, 4, 1, 5, 9])                         # 9
max("two", "three", "four")                     # "two", the lexicographically greatest
max("two", "three", "four", key=len)            # "three", the longest
```

### min

`min(x)` returns the least element in the collection `x`.

It is an error if any element does not support ordered comparison, or if the collection is empty.

The optional named parameter `key` specifies a function to be applied to each element, whose result is used for the comparison in place of the element.

```highlight
min([3, 1, 4, 1, 5, 9])                         # 1
min("two", "three", "four")                     # "four", the lexicographically least
min("two", "three", "four", key=len)            # "two", the shortest
```

### print

`print(*args, sep=" ")` prints its arguments, followed by a newline. Arguments are formatted as if by `str(x)` and separated with a space, unless an alternative separator is specified by a `sep` named argument.

Example:

```highlight
print(1, "hi", x=3)                             # "1 hi x=3\n"
print("hello", "world")                         # "hello world\n"
print("hello", "world", sep=", ")               # "hello, world\n"
```

Typically the formatted string is printed to the standard error file, but the exact behavior is a property of the Starlark thread and is determined by the host application.

### range

`range` returns an immutable sequence of integers defined by the specified interval and stride.

```highlight
range(stop)                             # equivalent to range(0, stop)
range(start, stop)                      # equivalent to range(start, stop, 1)
range(start, stop, step)
```

`range` requires between one and three integer arguments. With one argument, `range(stop)` returns the ascending sequence of non-negative integers less than `stop`. With two arguments, `range(start, stop)` returns only integers not less than `start`.

With three arguments, `range(start, stop, step)` returns integers formed by successively adding `step` to `start` until the value meets or passes `stop`. A call to `range` fails if the value of `step` is zero.

A call to `range` does not materialize the entire sequence, but returns a fixed-size value of type `"range"` that represents the parameters that define the sequence. The `range` value is iterable and may be indexed efficiently.

```highlight
list(range(10))                         # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(3, 10))                      # [3, 4, 5, 6, 7, 8, 9]
list(range(3, 10, 2))                   # [3, 5, 7, 9]
list(range(10, 3, -2))                  # [10, 8, 6, 4]
```

The `len` function applied to a `range` value returns its length. The truth value of a `range` value is `True` if its length is non-zero.

Range values are comparable: two `range` values compare equal if they denote the same sequence of integers, even if they were created using different parameters.

Range values are not hashable.

The `str` function applied to a `range` value yields a string of the form `range(10)`, `range(1, 10)`, or `range(1, 10, 2)`.

The `x in y` operator, where `y` is a range, reports whether `x` is equal to some member of the sequence `y`; the operation fails unless `x` is a number.

### repr

`repr(x)` formats its argument as a string.

All strings in the result are double-quoted.

```highlight
repr(1)                 # '1'
repr("x")               # '"x"'
repr([1, "x"])          # '[1, "x"]'
```

When applied to a string containing valid text, `repr` returns a string literal that denotes that string. When applied to a string containing an invalid UTF-K sequence, `repr` uses `\x` and `\u` escapes with out-of-range values to indicate the invalid elements; the result is not a valid literal.

```highlight
repr("🙂"[:1])		# "\xf0" (UTF-8) or "\ud83d" (UTF-16)
"\xf0"                  # error: non-ASCII hex escape
"\ud83d"                # error: invalid Unicode code point U+D83D
```

### reversed

`reversed(x)` returns a new list containing the elements of the collection `x` in reverse order.

```highlight
reversed(range(5))                              # [4, 3, 2, 1, 0]
reversed({"one": 1, "two": 2}.keys())           # ["two", "one"]
```

### set

`set(x)` returns a new set containing the unique elements of the iterable `x` in iteration order.

`set(x)` fails if any element of `x` is unhashable.

With no argument, `set()` returns a new empty set.

```highlight
set()                          # an empty set
set([3, 1, 1, 2])              # set([3, 1, 2]), a set of three elements
set({"k1": "v1", "k2": "v2"})  # set(["k1", "k2"]), a set of two elements
```

### sorted

`sorted(x)` returns a new list containing the elements of the collection x, in sorted order. The sort algorithm is stable, i.e., equal elements appear in the same relative order in the result.

The optional named boolean parameter `reverse`, if true, causes `sorted` to return results in reverse sorted order.

The optional named parameter `key` specifies a function of one argument to apply to obtain the value's sort key. The default behavior is the identity function. The `key` function is called exactly once per element of the sequence, in order, even for a single-element list.

```highlight
sorted([3, 1, 4, 1, 5, 9])                                 # [1, 1, 3, 4, 5, 9]
sorted([3, 1, 4, 1, 5, 9], reverse=True)                   # [9, 5, 4, 3, 1, 1]

sorted(["two", "three", "four"], key=len)                  # ["two", "four", "three"], shortest to longest
sorted(["two", "three", "four"], key=len, reverse=True)    # ["three", "four", "two"], longest to shortest
```

### str

`str(x)` formats its argument as a string.

If x is a string, the result is x (without quotation). All other strings, such as elements of a list of strings, are double-quoted.

```highlight
str(1)                          # '1'
str("x")                        # 'x'
str([1, "x"])                   # '[1, "x"]'
str(0.0)                        # '0.0'        (formatted as if by "%g")
str(b"abc")                     # 'abc'
```

The string form of a bytes value is the UTF-K decoding of the bytes. Each byte that is not part of a valid encoding is replaced by the UTF-K encoding of the replacement character, U+FFFD.

### tuple

`tuple(x)` returns a tuple containing the elements of the iterable `x`.

With no arguments, `tuple()` returns the empty tuple.

### type

`type(x)` returns a string describing the type of its operand.

```highlight
type(None)              # "NoneType"
type(0)                 # "int"
type(0.0)               # "float"
```

### zip

`zip()` returns a new list of n-tuples formed from corresponding elements of each of the n collections provided as arguments to `zip`. That is, the first tuple contains the first element of each of the collections, the second element contains the second element of each of the collections, and so on. The result list is only as long as the shortest of the input collections.

```highlight
zip()                                   # []
zip(range(5))                           # [(0,), (1,), (2,), (3,), (4,)]
zip(range(10), ["a", "b", "c"])         # [(0, "a"), (1, "b"), (2, "c")]
```
