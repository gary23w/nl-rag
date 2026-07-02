---
title: "Haskell/Variables and functions"
source: https://en.wikibooks.org/wiki/Haskell/Variables_and_functions
domain: haskell
license: CC-BY-SA-4.0 (Wikibooks)
tags: haskell, ghc, hackage, cabal
fetched: 2026-07-02
---

# Haskell/Variables and functions

<

Haskell

*All the examples in this chapter can be saved into a Haskell source file and then evaluated by loading that file into GHCi. Do not include the "Prelude>" prompts part of any example. When that prompt is shown, it means you can type the following code into an environment like GHCi. Otherwise, you should put the code in a file and run it.*

## Variables

In the last chapter, we used GHCi as a calculator. Of course, that's only practical for short calculations. For longer calculations and for writing Haskell programs, we want to keep track of intermediate results.

We can store intermediate results by assigning them names. These names are called *variables*. When a program runs, each variable is substituted for the *value* to which it refers. For instance, consider the following calculation:

```
Prelude> 3.141592653 * 5^2
78.539816325
```

That is the approximate area of a circle with radius `5`, according to the formula $A=\pi r^{2}$ . Of course, it is cumbersome to type in the digits of $\pi \approx 3.141592653$ , or even to remember more than the first few. Programming helps us avoid mindless repetition and rote memorization by delegating these tasks to a machine. That way, our minds stay free to deal with more interesting ideas. For the present case, Haskell already includes a variable named `pi` that stores over a dozen digits of $\pi$ for us. This allows for not just clearer code, but also greater precision:

```
Prelude> pi
3.141592653589793
Prelude> pi * 5^2
78.53981633974483
```

Note that the variable `pi` and its value, `3.141592653589793`, can be used interchangeably in calculations.

## Haskell source files

Beyond momentary operations in GHCi, you will save your code in Haskell source files (basically plain text) with the extension `.hs`. Work with these files using a text editor appropriate for coding (see the Wikipedia article on text editors). Proper source code editors will provide *syntax highlighting*, which colors the code in relevant ways to make reading and understanding easier. Vim and Emacs are popular choices among Haskell programmers, but have a bit of a learning curve to be able to fully benefit from their features. Visual Studio Code is also popular among Haskell programmers and is easier for beginners to use.

To keep things tidy, create a directory (i.e. a folder) in your computer to save the Haskell files you will create while doing the exercises in this book. Call the directory something like `HaskellWikibook`. Then, create a new file in that directory called `Varfun.hs` with the following code:

```mw
r = 5.0
```

That code defines the variable `r` as the value `5.0`.

Note: make sure that there are no spaces at the beginning of the line because Haskell is sensitive to whitespace.

Next, with your terminal at the HaskellWikibook directory, start GHCi and load the Varfun.hs file using the `:load` command:

```
Prelude> :load Varfun.hs
[1 of 1] Compiling Main             ( Varfun.hs, interpreted )
Ok, modules loaded: Main.
```

Note that `:load` can be abbreviated as `:l` (as in `:l Varfun.hs`).

If GHCi gives an error like `Could not find module 'Varfun.hs'`, you are probably running GHCi in the wrong directory or saved your file in the wrong directory. You can use the `:cd` command to change directories within GHCi (for instance, `:cd HaskellWikibook`).

With the file loaded, GHCi's prompt changes from "Prelude" to "*Main". You can now use the newly defined variable `r` in your calculations:

```
*Main> r
5.0
*Main> pi * r^2
78.53981633974483
```

So, we calculated the area of a circle with radius of 5.0 using the well-known formula $\pi r^{2}$ . This worked because we defined `r` in our Varfun.hs file and `pi` comes from the standard Haskell libraries.

Next, we'll make the area formula easier to quickly access by defining a variable name for it. Change the contents of the source file to:

```mw
r = 5.0
area = pi * r ^ 2
```

Save the file. Then, assuming you kept GHCi running with the file still loaded, type `:reload` (or abbreviate version `:r`):

```
*Main> :reload
Compiling Main             ( Varfun.hs, interpreted )
Ok, modules loaded: Main.
*Main>
```

Now we have two variables `r` and `area`:

```
*Main> area
78.53981633974483
*Main> area / r
15.707963267948966
```

*Note*

The `let` *keyword* (a word with a special meaning) lets us define variables directly at the GHCi prompt without a source file. This looks like:

```
Prelude> let area = pi * 5 ^ 2
```

Although sometimes convenient, assigning variables entirely in GHCi this way is impractical for any complex tasks. We will usually want to use saved source files.

Besides the working code itself, source files may contain text *comments*. In Haskell there are two types of comment. The first starts with `--` and continues until the end of the line:

```mw
x = 5     -- x is 5.
y = 6     -- y is 6.
-- z = 7  -- z is not defined.
```

In this case, `x` and `y` are defined in actual Haskell code, but `z` is not.

The second type of comment is denoted by an enclosing `{- ... -}` and can span multiple lines:

```mw
answer = 2 * {-
  block comment, crossing lines and...
  -} 3 {- inline comment. -} * 7
```

By combining single- and multi-line commenting, it is possible to toggle between executed and commented-out code by adding or removing a single `}` character, respectively:

```mw
{--
foo :: String
foo = "bar"
--}
```

vs.

```mw
{--}
foo :: String
foo = "bar"
--}
```

We use comments for explaining parts of a program or making other notes in context. Beware of comment overuse as too many comments can make programs harder to read. Also, we must carefully update comments whenever we change the corresponding code. Outdated comments can cause significant confusion.

## Variables in imperative languages

Readers familiar with imperative programming will notice that variables in Haskell seem quite different from variables in languages like C. If you have no programming experience, you could skip this section, but it will help you understand the general situation when encountering the many cases (most Haskell textbooks, for example) where people discuss Haskell in reference to other programming languages.

*Imperative programming* treats variables as changeable locations in a computer's memory. That approach connects to the basic operating principles of computers. Imperative programs explicitly tell the computer what to do. Higher-level imperative languages are quite removed from direct computer assembly code instructions, but they retain the same step-by-step way of thinking. In contrast, *functional programming* offers a way to think in higher-level mathematical terms, defining how variables relate to one another, leaving the compiler to translate these to the step-by-step instructions that the computer can process.

Let's look at an example. The following code does not work in Haskell:

```mw
r = 5
r = 2
```

An imperative programmer may read this as first setting `r = 5` and then changing it to `r = 2`. In Haskell, however, the compiler will respond to the code above with an error: "multiple declarations of `r`". Within a given scope, a variable in Haskell gets defined only once and cannot change.

The variables in Haskell seem almost *invariable*, but they work like variables in mathematics. In a math classroom, you never see a variable change its value within a single problem.

In precise terms, Haskell variables are *immutable*. They vary only based on the data we enter into a program. We can't define `r` two ways in the same code, but we could change the value by changing the file. Let's update our code from above:

```mw
r = 2.0
area = pi * r ^ 2
```

Of course, that works just fine. We can change `r` in the one place where it is defined, and that will automatically update the value of all the rest of the code that uses the `r` variable.

Real-world Haskell programs work by leaving *some* variables unspecified in the code. The values then get defined when the program gets data from an external file, a database, or user input. For now, however, we will stick to defining variables internally. We will cover interaction with external data in later chapters.

Here's one more example of a major difference from imperative languages:

```mw
r = r + 1
```

Instead of "incrementing the variable `r`" (i.e. updating the value in memory), this Haskell code is a recursive definition of `r` (i.e. defining it in terms of itself). We will explain recursion in detail later on. For this specific case, if `r` had been defined with any value beforehand, then `r = r + 1` in Haskell would bring an error message. `r = r + 1` is akin to saying, in a mathematical context, that $5=5+1$ , which is plainly wrong.

Because their values do not change within a program, variables can be defined in any order. For example, the following fragments of code do exactly the same thing:

| y = x * 2 x = 3 | x = 3 y = x * 2 |
|---|---|

In Haskell, there is no notion of "`x` being declared before `y`" or the other way around. Of course, using `y` will still require a value for `x`, but this is unimportant until you need a specific numeric value.

## Functions

Changing our program every time we want to calculate the area of new circle is both tedious and limited to one circle at a time. We could calculate two circles by duplicating all the code using new variables `r2` and `area2` for the second circle:

```mw
r  = 5
area  = pi * r ^ 2
r2 = 3
area2 = pi * r2 ^ 2
```

Of course, to eliminate this mindless repetition, we would prefer to have simply one *function* for area and then apply it to different radii.

A *function* takes an *argument* value (or *parameter*) and gives a result value (essentially the same as in mathematical functions). Defining functions in Haskell is like defining a variable, except that we take note of the function argument that we put on the left hand side of the equals sign. For instance, the following defines a function `area` which depends on an argument named `r`:

```mw
area r = pi * r ^ 2
```

Look closely at the syntax: the function name comes first (`area` in our example), followed by a space and then the argument (`r` in the example). Following the `=` sign, the *function definition* is a formula that uses the argument in context with other already defined terms.

Now, we can plug in different values for the argument in a *call* to the function. Save the code above in a file, load it into GHCi, and try the following:

```
*Main> area 5
78.53981633974483
*Main> area 3
28.274333882308138
*Main> area 17
907.9202768874502
```

Thus, we can *call* this function with different radii to calculate the area of any circle.

Our function here is defined mathematically as

$A(r)=\pi \cdot r^{2}$

In mathematics, the argument is enclosed between parentheses, as in $A(5)=78.54$ or $A(3)=28.27$ . Many programming languages likewise surround arguments with parentheses, as in `max(2, 3)`. But Haskell omits parentheses around a list of arguments (as well as commas between them): `max 2 3`.

We still use parentheses for grouping *expressions* (any code that gives a value) that must be evaluated together. Note how the following expressions are parsed differently:

```mw
5 * 3 + 2       -- 15 + 2 = 17 (multiplication is done before addition)
5 * (3 + 2)     -- 5 * 5 = 25 (thanks to the parentheses)
area 5 * 3      -- (area 5) * 3
area (5 * 3)    -- area 15
```

Note that Haskell functions take *precedence* over all other operators such as `+` and `*`, in the same way that, for instance, multiplication is done before addition in mathematics.

### Evaluation

What exactly happens when you enter an expression into GHCi? After you press the enter key, GHCi will *evaluate* the expression you have given. That means it will replace each function with its definition and calculate the results until a single value remains. For example, the evaluation of `area 5` proceeds as follows:

```
   area 5
=>    { replace the left-hand side  area r = ...  by the right-hand side  ... = pi * r^2 }
   pi * 5 ^ 2
=>    { replace  pi  by its numerical value }
   3.141592653589793 * 5 ^ 2
=>    { apply exponentiation (^) }
   3.141592653589793 * 25
=>    { apply multiplication (*) }
   78.53981633974483
```

As this shows, to *apply* or *call* a function means to replace the left-hand side of its definition by its right-hand side. When using GHCi, the results of a function call will then show on the screen.

Some more functions:

```mw
double x    = 2 * x
quadruple x = double (double x)
square x    = x * x
half   x    = x / 2
```

| Exercises |
|---|
| Explain how GHCi evaluates `quadruple 5`. Define a function that subtracts 12 from half its argument. |

### Multiple parameters

Functions can also take more than one argument. For example, a function for calculating the area of a rectangle given its length and width:

```mw
areaRect l w = l * w
```

```
*Main> areaRect 5 10
50
```

Another example that calculates the area of a triangle $\left(A={\frac {bh}{2}}\right)$ :

```mw
areaTriangle b h = (b * h) / 2
```

```
*Main> areaTriangle 3 9
13.5
```

As you can see, multiple arguments are separated by spaces. That's also why you sometimes have to use parentheses to group expressions. For instance, to quadruple a value `x`, you can't write:

```mw
quadruple x = double double x     -- error
```

That would apply a function named `double` to the two arguments `double` and `x`. Note that *functions can be arguments to other functions* (you will see why later). To make this example work, we need to put parentheses around the argument:

```mw
quadruple x = double (double x)
```

Arguments are always passed in the order given. For example:

```mw
minus x y = x - y
```

```
*Main> minus 10 5
5
*Main> minus 5 10
-5
```

Here, `minus 10 5` evaluates to `10 - 5`, but `minus 5 10` evaluates to `5 - 10` because the order changes.

| Exercises |
|---|
| Write a function to calculate the volume of a box. Approximately how many stones are the famous pyramids at Giza made up of? Hint: you will need estimates for the volume of the pyramids and the volume of each block. |

### On combining functions

Of course, you can use functions that you have already defined to define new functions, just like you can use the predefined functions like addition `(+)` or multiplication `(*)` (operators are defined as functions in Haskell). For example, to calculate the area of a square, we can reuse our function that calculates the area of a rectangle:

```mw
areaRect l w = l * w
areaSquare s = areaRect s s
```

```
*Main> areaSquare 5
25
```

After all, a square is just a rectangle with equal sides.

| Exercises |
|---|
| Write a function to calculate the volume of a cylinder. The volume of a cylinder is the area of the base, which is a circle (you already programmed this function in this chapter, so reuse it) multiplied by the height. |

## Local definitions

### `where` clauses

When defining a function, we sometimes want to define intermediate results that are *local* to the function. For instance, consider Heron's formula $A={\sqrt {s(s-a)(s-b)(s-c)}}$ for calculating the area of a triangle with sides `a`, `b`, and `c`:

```mw
heron a b c = sqrt (s * (s - a) * (s - b) * (s - c))
    where
    s = (a + b + c) / 2
```

The variable `s` is half the perimeter of the triangle and it would be tedious to write it out four times in the argument of the square root function `sqrt`.

Simply writing the definitions in sequence does not work...

```mw
heron a b c = sqrt (s * (s - a) * (s - b) * (s - c))
s = (a + b + c) / 2                                   -- a, b, and c are not defined here
```

... because the variables `a`, `b`, `c` are only available in the right-hand side of the function `heron`, but the definition of `s` as written here is not part of the right-hand side of `heron`. To make it part of the right-hand side, we use the `where` keyword.

Note that both the `where` and the local definitions are *indented* by 4 spaces, to distinguish them from subsequent definitions. Here is another example that shows a mix of local and top-level definitions:

```mw
areaTriangleTrig  a b c = c * height / 2   -- use trigonometry
    where
    cosa   = (b ^ 2 + c ^ 2 - a ^ 2) / (2 * b * c)
    sina   = sqrt (1 - cosa ^ 2)
    height = b * sina
areaTriangleHeron a b c = result           -- use Heron's formula
    where
    result = sqrt (s * (s - a) * (s - b) * (s - c))
    s      = (a + b + c) / 2
```

### Scope

If you look closely at the previous example, you'll notice that we have used the variable names `a`, `b`, `c` twice, once for each of the two area functions. How does that work?

Consider the following GHCi sequence:

```
Prelude> let r = 0
Prelude> let area r = pi * r ^ 2
Prelude> area 5
78.53981633974483
```

It would have been an unpleasant surprise to return `0` for the area because of the earlier `let r = 0` definition getting in the way. That does not happen because when you defined `r` the second time you are talking about a *different* `r`. This may seem confusing, but consider how many people have the name John, and yet for any context with only one John, we can talk about "John" with no confusion. Programming has a notion similar to context, called *scope*.

We will not explain the technicalities behind scope right now. Just keep in mind that the value of a parameter is strictly what you pass in when you call the function, regardless of what the variable was called in the function's definition. That said, appropriately unique names for variables do make the code easier for human readers to understand.

## Summary

1. Variables store values (which can be any arbitrary Haskell expression).
2. Variables do not change within a scope.
3. Functions help you write reusable code.
4. Functions can accept more than one parameter.

We also learned about non-code text comments within a source file.
