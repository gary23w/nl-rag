---
title: "Anonymous function"
source: https://en.wikipedia.org/wiki/Anonymous_function
domain: aws-lambda
license: CC-BY-SA-4.0
tags: aws lambda, serverless function, lambda function, function as a service
fetched: 2026-07-02
---

# Anonymous function

In computer programming, an **anonymous function** (**function literal**, **lambda function**, or **block**) is a function definition that is not bound to an identifier. Anonymous functions are often arguments being passed to higher-order functions or used for constructing the result of a higher-order function that needs to return a function. If the function is only used once, or a limited number of times, an anonymous function may be syntactically lighter than using a named function. Anonymous functions are ubiquitous in functional programming languages and other languages with first-class functions, where they fulfil the same role for the function type as literals do for other data types.

Anonymous functions originate in the work of Alonzo Church in his invention of the lambda calculus, in which all functions are anonymous, in 1936, before electronic computers. In several programming languages, anonymous functions are introduced using the keyword *lambda*, and anonymous functions are often referred to as **lambdas** or **lambda abstractions**. Anonymous functions have been a feature of programming languages since Lisp in 1958, and a growing number of modern programming languages support anonymous functions.

## Names

The names "lambda abstraction", "lambda function", and "lambda expression" refer to the notation of function abstraction in lambda calculus, where the usual function $f(x)=M$ would be written $(\lambda x.M)$ , and where M is an expression that uses x . Compare to the Python syntax of `lambda x: M`.

The name "arrow function" refers to the mathematical "maps to" symbol, $x\mapsto M$ . Compare to the JavaScript syntax of `x => M`.

## Uses

Anonymous functions can encapsulate functionality that does not require naming and is intended for short-term or localized use. Some notable examples include closures and currying.

The use of anonymous functions is a matter of style. Using them is never the only way to solve a problem; each anonymous function could instead be defined as a named function and called by name. Anonymous functions often provide a briefer notation than defining named functions. In languages that do not permit the definition of named functions in local scopes, anonymous functions may provide encapsulation via localized scope, however the code in the body of such anonymous function may not be re-usable, or amenable to separate testing. Short/simple anonymous functions used in expressions may be easier to read and understand than separately defined named functions, though lacking a descriptive name may reduce code readability.

In some programming languages, anonymous functions are commonly implemented for very specific purposes such as binding events to callbacks or instantiating the function for particular values, which may be more efficient in a Dynamic programming language, more readable, and less error-prone than calling a named function.

The following examples are written in Python 3.

### Sorting

Many languages provide a generic function that sorts a list (or array) of objects into an order determined by a comparison function which compares two objects to determine if they are equal or if one is greater or less than the other. Using an anonymous comparison function expression passed as an argument to a generic sort function is often more concise than creating a named comparison function.

Consider this Python code sorting a list of strings by length of the string:

```mw
a: list[str] = ["house", "car", "bike"]
a.sort(key = lambda x: len(x))
print(a)
# prints ['car', 'bike', 'house']
```

The anonymous function in this example is the lambda expression:

```mw
lambda x: len(x)
```

The anonymous function accepts one argument, `x`, and returns the length of its argument, which is then used by the `sort()` method as the criteria for sorting.

Basic syntax of a lambda function in Python is

```mw
lambda arg1, arg2, arg3, ...: <operation on the arguments returning a value>
```

The expression returned by the lambda function can be assigned to a variable and used in the code at multiple places.

```mw
from typing import Callable

add: Callable[[int], int] = lambda a: a + a
print(add(20))
# prints 40
```

Another example would be sorting items in a list by the name of their class (in Python, everything has a class):

```mw
a: list[int | str] = [10, "number", 11.2]
a.sort(key=lambda x: x.__class__.__name__)
print(a)
# prints [11.2, 10, 'number']
```

Note that `11.2` has class name "`float`", `10` has class name "`int`", and `'number'` has class name "`str`". The sorted order is "`float`", "`int`", then "`str`".

### Closures

Closures are functions evaluated in an environment containing bound variables. The following example binds the variable "threshold" within an anonymous function that compares input values to this threshold.

```mw
def comp(threshold: int) -> Callable[[int], bool]:
    return lambda x: x < threshold
```

This can be used as a sort of generator of comparison functions:

```mw
func_a: Callable[[int], bool] = comp(10)
func_b: Callable[[int], bool] = comp(20)

print(func_a(5), func_a(8), func_a(13), func_a(21))
# prints True True False False

print(func_b(5), func_b(8), func_b(13), func_b(21))
# prints True True True False
```

It would be impractical to create a function for every possible comparison function and may be too inconvenient to keep the threshold around for further use. Regardless of the reason why a closure is used, the anonymous function is the entity that contains the functionality that does the comparing.

### Currying

Currying transforms a function that takes multiple arguments into a sequence of functions each accepting a single argument. In this example, a function that performs division by any integer is transformed into one that performs division by a set integer.

```mw
def divide(x: int, y: int) -> float:
    return x / y

def divisor(d: int) -> Callable[[int], float]:
    return lambda x: divide(x, d)

half: Callable[[int], float] = divisor(2)
third: Callable[[int], float] = divisor(3)

print(half(32), third(32))
# prints 16.0 10.666666666666666

print(half(40), third(40))
# prints 20.0 13.333333333333334
```

While the use of anonymous functions is perhaps not common with currying, it still can be used. In the above example, the function divisor generates functions with a specified divisor. The functions half and third curry the divide function with a fixed divisor.

The divisor function also forms a closure by binding the variable `d`.

### Higher-order functions

A higher-order function is a function that takes a function as an argument or returns one as a result. This technique is frequently employed to tailor the behavior of a generically defined function, such as a loop or recursion pattern. Anonymous functions are a convenient way to specify such function arguments. The following examples are in Python 3.

#### Map

The map function performs a function call on each element of a list. The following example squares every element in an array with an anonymous function.

```mw
a: list[int] = [1, 2, 3, 4, 5, 6]
print(list(map(lambda x: x * x, a)))
# prints [1, 4, 9, 16, 25, 36]
```

The anonymous function takes an argument and returns its square. The above form is discouraged by the creators of the language, who maintain that the form presented below has the same meaning and is more aligned with the philosophy of the language:

```mw
a: list[int] = [1, 2, 3, 4, 5, 6]
print([x * x for x in a])
# prints [1, 4, 9, 16, 25, 36]
```

#### Filter

The filter function returns all elements from a list that evaluate True when passed to a certain function.

```mw
a: list[int] = [1, 2, 3, 4, 5, 6]
print(list(filter(lambda x: x % 2 == 0, a)))
# prints [2, 4, 6]
```

The anonymous function checks if the argument passed to it is even. The same as with map, the form below is considered more appropriate:

```mw
a: list[int] = [1, 2, 3, 4, 5, 6]
print([x for x in a if x % 2 == 0])
# prints [2, 4, 6]
```

#### Fold

A fold function runs over all elements in a structure (for lists usually left-to-right, a "left fold", called `reduce` in Python), accumulating a value as it goes. This can be used to combine all elements of a structure into one value, for example:

```mw
a: list[int] = [1, 2, 3, 4, 5]
print(functools.reduce(lambda x, y: x * y, a))
# prints 120
```

This performs

$\left(\left(\left(1\times 2\right)\times 3\right)\times 4\right)\times 5=120.$

The anonymous function here is the multiplication of the two arguments.

A fold does not necessarily produce a single scalar value; it can also generate structured results such as lists. Instead, both map and filter can be created using fold. In map, the value that is accumulated is a new list, containing the results of applying a function to each element of the original list. In filter, the value that is accumulated is a new list containing only those elements that match the given condition.

## List of languages

The following is a list of programming languages that support unnamed anonymous functions fully, or partly as some variant, or not at all.

The following table illustrates several common patterns. Notably, languages like C, Pascal, and Object Pascal—which traditionally do not support anonymous functions—are all statically typed languages. However, statically typed languages can support anonymous functions. For example, the ML languages are statically typed and fundamentally include anonymous functions, and Delphi, a dialect of Object Pascal, has been extended to support anonymous functions, as has C++ (by the C++11 standard). Second, the languages that treat functions as first-class functions (Dylan, Haskell, JavaScript, Lisp, ML, Perl, Python, Ruby, Scheme) generally have anonymous function support so that functions can be defined and passed around as easily as other data types.

| Language | Support | Notes |
|---|---|---|
| ActionScript | (Green tick)Y |   |
| Ada | (Green tick)Y | Expression functions are a part of Ada2012, access-to-subprogram |
| ALGOL 68 | (Green tick)Y |   |
| APL | (Green tick)Y | Dyalog, ngn and dzaima APL fully support both dfns and tacit functions. GNU APL has rather limited support for dfns. |
| Assembly languages | (Red X)N |   |
| AHK | (Green tick)Y | Since AutoHotkey V2, anonymous functions are supported with a syntax similar to JavaScript. |
| Bash | (Green tick)Y | A library has been made to support anonymous functions in Bash. |
| C | (Red X)N | Support is provided in Clang and along with the LLVM compiler-rt lib. GCC support is given for a macro implementation which enables the possibility of use. See below for more details. |
| C# | (Green tick)Y |   |
| C++ | (Green tick)Y | As of the C++11 standard |
| CFML | (Green tick)Y | As of Railo 4, ColdFusion 10 |
| Clojure | (Green tick)Y |   |
| COBOL | (Red X)N | Micro Focus's non-standard Managed COBOL dialect supports lambdas, which are called anonymous delegates/methods. |
| Curl | (Green tick)Y |   |
| D | (Green tick)Y |   |
| Dart | (Green tick)Y |   |
| Delphi | (Green tick)Y |   |
| Dylan | (Green tick)Y |   |
| Eiffel | (Green tick)Y |   |
| Elm | (Green tick)Y |   |
| Elixir | (Green tick)Y |   |
| Erlang | (Green tick)Y |   |
| F# | (Green tick)Y |   |
| Excel | (Green tick)Y | Excel worksheet function, 2021 beta release |
| Factor | (Green tick)Y | "Quotations" support this |
| Fortran | (Red X)N |   |
| Frink | (Green tick)Y |   |
| Go | (Green tick)Y |   |
| Gosu | (Green tick)Y |   |
| Groovy | (Green tick)Y |   |
| Haskell | (Green tick)Y |   |
| Haxe | (Green tick)Y |   |
| Java | (Green tick)Y | Supported since Java 8. |
| JavaScript | (Green tick)Y |   |
| Julia | (Green tick)Y |   |
| Kotlin | (Green tick)Y |   |
| Lisp | (Green tick)Y |   |
| Logtalk | (Green tick)Y |   |
| Lua | (Green tick)Y |   |
| MUMPS | (Red X)N |   |
| Maple | (Green tick)Y |   |
| MATLAB | (Green tick)Y |   |
| Maxima | (Green tick)Y |   |
| Nim | (Green tick)Y |   |
| OCaml | (Green tick)Y |   |
| Octave | (Green tick)Y |   |
| Object Pascal | (Green tick)Y | Delphi, a dialect of Object Pascal, supports anonymous functions (formally, *anonymous methods*) natively since Delphi 2009. The Oxygene Object Pascal dialect also supports them. |
| Objective-C (Mac OS X 10.6+) | (Green tick)Y | Called blocks; in addition to Objective-C, blocks can also be used on C and C++ when programming on Apple's platform. |
| OpenSCAD | (Green tick)Y | Function Literal support was introduced with version 2021.01. |
| Pascal | (Red X)N |   |
| Perl | (Green tick)Y |   |
| PHP | (Green tick)Y | As of PHP 5.3.0, true anonymous functions are supported. Formerly, only partial anonymous functions were supported, which worked much like C#'s implementation. |
| PL/I | (Red X)N |   |
| Python | (Green tick)Y | Python supports anonymous functions through the lambda syntax, which supports only expressions, not statements. |
| R | (Green tick)Y |   |
| Racket | (Green tick)Y |   |
| Raku | (Green tick)Y |   |
| Rexx | (Red X)N |   |
| RPG | (Red X)N |   |
| Ruby | (Green tick)Y | Ruby's anonymous functions, inherited from Smalltalk, are called blocks. |
| Rust | (Green tick)Y |   |
| Scala | (Green tick)Y |   |
| Scheme | (Green tick)Y |   |
| Smalltalk | (Green tick)Y | Smalltalk's anonymous functions are called blocks. |
| Standard ML | (Green tick)Y |   |
| Swift | (Green tick)Y | Swift's anonymous functions are called Closures. |
| TypeScript | (Green tick)Y |   |
| Typst | (Green tick)Y |   |
| Tcl | (Green tick)Y |   |
| Vala | (Green tick)Y |   |
| Visual Basic .NET v9 | (Green tick)Y |   |
| Visual Prolog v 7.2 | (Green tick)Y |   |
| Wolfram Language | (Green tick)Y |   |
| Zig | (Red X)N |   |

## Examples
