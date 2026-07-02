---
title: "Haskell/Type basics"
source: https://en.wikibooks.org/wiki/Haskell/Type_basics
domain: haskell
license: CC-BY-SA-4.0 (Wikibooks)
tags: haskell, ghc, hackage, cabal
fetched: 2026-07-02
---

# Haskell/Type basics

<

Haskell

In programming, **Types** are used to group similar values into categories. In Haskell, the type system is a powerful way of reducing the number of mistakes in your code.

## Introduction

Programming deals with different sorts of entities. For example, consider adding two numbers together:

$2+3$

What are 2 and 3? Well, they are numbers. What about the plus sign in the middle? That's certainly not a number, but it stands for an operation which we can do with two numbers – namely, addition.

Similarly, consider a program that asks you for your name and then greets you with a "Hello" message. Neither your name nor the word Hello are numbers. What are they then? We might refer to all words and sentences and so forth as text. It's normal in programming to use a slightly more esoteric word: *String*, which is short for "string of characters".

Haskell has a rule that all type names have to begin with a capital letter. We shall adhere to this convention henceforth.

Databases illustrate clearly the concept of types. For example, say we had a table in a database to store details about a person's contacts; a kind of personal telephone book. The contents might look like this:

| First Name | Last Name | Address | Telephone number |
|---|---|---|---|
| Sherlock | Holmes | 221B Baker Street London | 743756 |
| Bob | Jones | 99 Long Road Street Villestown | 655523 |

The fields in each entry contain values. Sherlock is a value as is 99 Long Road Street Villestown as well as 655523. Let's classify the values in this example in terms of types. "First Name" and "Last Name" contain text, so we say that the values are of type String.

At first glance, we might classify address as a String. However, the semantics behind an innocent address are quite complex. Many human conventions dictate how we interpret addresses. For example, if the beginning of the address text contains a number it is likely the number of the house. If not, then it's probably the name of the house – except if it starts with "PO Box", in which case it's just a postal box address and doesn't indicate where the person lives at all. Each part of the address has its own meaning.

In principle, we can indeed say that addresses are Strings, but that doesn't capture many important features of addresses. When we describe something as a String, all that we are saying is that it is a sequence of characters (letters, numbers, etc). Recognizing something as a specialized type is far more meaningful. If we know something is an Address, we instantly know much more about the piece of data – for instance, that we can interpret it using the "human conventions" that give meaning to addresses.

We might also apply this rationale to the telephone numbers. We could specify a TelephoneNumber type. Then, if we were to come across some arbitrary sequence of digits which happened to be of type TelephoneNumber we would have access to a lot more information than if it were just a Number – for instance, we could start looking for things such as area and country codes on the initial digits.

Another reason not to consider the telephone numbers as Numbers is that doing arithmetic with them makes no sense. What is the meaning and expected effect of, say, multiplying a TelephoneNumber by 100? It would not allow calling anyone by phone. Also, each digit comprising a telephone number is important; we cannot accept losing some of them by rounding or even by omitting leading zeros.

### Why types are useful

How does it help us program well to describe and categorize things? Once we define a type, we can specify what we can or cannot do with it. That makes it far easier to manage larger programs and avoid errors.

## Using the interactive `:type` command

Let's explore how types work using GHCi. The type of any expression can be checked with `:type` (or shortened to `:t`) command. Try this on the boolean values from the previous module:

**Example:** Exploring the types of boolean values in GHCi

```
Prelude> :type True
True :: Bool
Prelude> :type False
False :: Bool
Prelude> :t (3 < 5)
(3 < 5) :: Bool
```

The symbol `::`, which will appear in a couple other places, can be read as simply "is of type", and indicates a *type signature*.

`:type` reveals that truth values in Haskell are of type `Bool`, as illustrated above for the two possible values, `True` and `False`, as well as for a sample expression that will evaluate to one of them. Note that boolean values are not just for value comparisons. `Bool` captures the semantics of a yes/no answer, so it can represent any information of such kind – say, whether a name was found in a spreadsheet, or whether a user has toggled an on/off option.

### Characters and strings

Now let's try `:t` on something new. Literal characters are entered by enclosing them with single quotation marks. For instance, this is the single letter H:

**Example:** Using the :type command in GHCi on a literal character

```
Prelude> :t 'H'
'H' :: Char
```

So, literal character values have type `Char` (short for "character"). Now, single quotation marks only work for individual characters, so if we need to enter longer text – that is, a string of characters – we use *double* quotation marks instead:

**Example:** Using the :t command in GHCi on a literal string

```
Prelude> :t "Hello World"
"Hello World" :: [Char]
```

Why did we get `Char` again? The difference is the square brackets. `[Char]` means a number of characters chained together, forming a *list* of characters. Haskell considers all Strings to be lists of characters. Lists in general are important entities in Haskell, and we will cover them in more detail in a little while.

| Exercises |
|---|
| Try using `:type` on the literal value `"H"` (notice the double quotes). What happens? Why? Try using `:type` on the literal value `'Hello World'` (notice the single quotes). What happens? Why? |

Incidentally, Haskell allows for *type synonyms*, which work pretty much like synonyms in human languages (words that mean the same thing – say, 'big' and 'large'). In Haskell, type synonyms are alternative names for types. For instance, `String` is defined as a synonym of `[Char]`, and so we can freely substitute one with the other. Therefore, to say:

```mw
"Hello World" :: String
```

is also perfectly valid, and in many cases a lot more readable. From here on we'll mostly refer to text values as `String`, rather than `[Char]`.

## Functional types

So far, we have seen how values (strings, booleans, characters, etc.) have types and how these types help us to categorize and describe them. Now, the big twist that makes Haskell's type system truly powerful: *Functions* have types as well. Let's look at some examples to see how that works.

### Example: `not`

We can negate boolean values with `not` (e.g. `not True` evaluates to `False` and vice-versa). To figure out the type of a function, we consider two things: the type of values it takes as its input and the type of value it returns. In this example, things are easy. `not` takes a `Bool` (the `Bool` to be negated), and returns a `Bool` (the negated `Bool`). The notation for writing that down is:

**Example:** Type signature for `not`

```mw
not :: Bool -> Bool
```

You can read this as "`not` is a function from things of type `Bool` to things of type `Bool`".

Using :t on a function will work just as expected:

```
Prelude> :t not
not :: Bool -> Bool
```

The description of a function's type is in terms of the types of argument(s) it takes and the type of value it evaluates to.

### Example: `chr` and `ord`

Text presents a problem to computers. At its lowest level, a computer only knows binary 1s and 0s. To represent text, every character is first converted to a number, then that number is converted to binary and stored. That's how a piece of text (which is just a sequence of characters) is encoded into binary. Normally, we're only interested in how to encode characters into their numerical representations, because the computer takes care of the conversion to binary numbers without our intervention.

The easiest way to convert characters to numbers is simply to write all the possible characters down, then number them. For example, we might decide that 'a' corresponds to 1, then 'b' to 2, and so on. This is what something called the ASCII standard is: take 128 commonly-used characters and number them (ASCII doesn't actually start with 'a', but the general idea is the same). Of course, it would be quite a chore to sit down and look up a character in a big lookup table every time we wanted to encode it, so we've got two functions that do it for us, `chr` (pronounced 'char') and `ord`:

**Example:** Type signatures for `chr` and `ord`

```mw
chr :: Int  -> Char
ord :: Char -> Int
```

We already know what `Char` means. The new type on the signatures above, `Int`, refers to integer numbers, and is one of quite a few different types of numbers. The type signature of `chr` tells us that it takes an argument of type `Int`, an integer number, and evaluates to a result of type Char. The converse is the case with `ord`: It takes things of type Char and returns things of type Int. With the info from the type signatures, it becomes immediately clear which of the functions encodes a character into a numeric code (`ord`) and which does the decoding back to a character (`chr`).

To make things more concrete, here are a few examples. Notice that the two functions aren't available by default; so before trying them in GHCi you need to use the `:module Data.Char` (or `:m Data.Char`) command to load the Data.Char module where they are defined.

**Example:** Function calls to `chr` and `ord`

```
Prelude> :m Data.Char
Prelude Data.Char> chr 97
'a'
Prelude Data.Char> chr 98
'b'
Prelude Data.Char> ord 'c'
99
```

### Functions with more than one argument

What would be the type of a function that takes more than one argument?

**Example:** A function with more than one argument

```mw
xor p q = (p || q) && not (p && q)
```

(`xor` is the exclusive-or function, which evaluates to `True` if either one or the other argument is `True`, *but not both*; and `False` otherwise.)

The general technique for forming the type of a function that accepts more than one argument is simply to write down all the types of the arguments in a row, in order (so in this case `p` first then `q`), then link them all with `->`. Finally, add the type of the result to the end of the row and stick a final `->` in just before it. In this example, we have:

1. Write down the types of the arguments. In this case, the use of `(||)` and `(&&)` gives away that `p` and `q` have to be of type `Bool`:
  ```
Bool                   Bool
^^ p is a Bool         ^^ q is a Bool as well
  ```
2. Fill in the gaps with `->`:
  ```
Bool -> Bool
  ```
3. Add in the result type and a final `->`. In our case, we're just doing some basic boolean operations so the result remains a Bool.
  ```
Bool -> Bool -> Bool
                 ^^ We're returning a Bool
             ^^ This is the extra -> that got added in 
  ```

The final signature, then, is:

**Example:** The signature of `xor`

```mw
xor :: Bool -> Bool -> Bool
```

### Real world example: `openWindow`

A library is a collection of common code used by many programs.

As you'll learn in the Haskell in Practice section of the course, one popular group of Haskell libraries are the GUI (**G**raphical **U**ser **I**nterface) ones. These provide functions for dealing with the visual things computer users are familiar with: menus, buttons, application windows, moving the mouse around, etc. One function from one of these libraries is called `openWindow`, and you can use it to open a new window in your application. For example, say you're writing a word processor, and the user has clicked on the 'Options' button. You need to open a new window which contains all the options that they can change. Let's look at the type signature for this function:

**Example:** `openWindow`

```mw
openWindow :: WindowTitle -> WindowSize -> Window
```

You don't know these types, but they're quite simple. All three of the types there, `WindowTitle`, `WindowSize` and `Window` are defined by the GUI library that provides `openWindow`. As we saw earlier, the two arrows mean that the first two types are the types of the parameters, and the last is the type of the result. `WindowTitle` holds the title of the window (which typically appears in a title bar at the very top of the window), and `WindowSize` specifies how big the window should be. The function then returns a value of type Window which represents the actual window.

So, even if you have never seen a function before or don't know how it actually works, a type signature can give you a general idea of what the function does. Make a habit of testing every new function you meet with :t. If you start doing that now, you'll not only learn about the standard library Haskell functions but also develop a useful kind of intuition about functions in Haskell.

| Exercises |
|---|
| What are the types of the following functions? For any functions involving numbers, you can just pretend the numbers are Ints. The `negate` function, which takes an Int and returns that Int with its sign swapped. For example, `negate 4 = -4`, and `negate (-2) = 2` The `(\|\|)` function, pronounced 'or', that takes two Bools and returns a third Bool which is True if either of the arguments were, and False otherwise. A `monthLength` function which takes a Bool which is True if we are considering a leap year and False otherwise, and an Int which is the number of a month; and returns another Int which is the number of days in that month. `f x y = not x && y` `g x = (2*x - 1)^2` |

## Type signatures in code

We have explored the basic theory behind types and how they apply to Haskell. Now, we will see how type signatures are used for annotating functions in source files. Consider the `xor` function from an earlier example:

**Example:** A function with its signature

```mw
xor :: Bool -> Bool -> Bool
xor p q = (p || q) && not (p && q)
```

That is all we have to do. For maximum clarity, type signatures go above the corresponding function definition.

The signatures we add in this way serve a dual role: they clarify the type of the functions both to human readers and to the compiler/interpreter.

### Type inference

If type signatures tell the interpreter (or compiler) about the function type, how did we write our earliest Haskell code without type signatures? Well, when you don't tell Haskell the types of your functions and variables it figures them out through a process called *type inference*. In essence, the compiler starts with the types of things it knows and then works out the types of the rest of the values. Consider a general example:

**Example:** Simple type inference

```mw
-- We're deliberately not providing a type signature for this function
isL c = c == 'l'
```

`isL` is a function that takes an argument `c` and returns the result of evaluating `c == 'l'`. Without a type signature, the type of `c` and the type of the result are not specified. In the expression `c == 'l'`, however, the compiler knows that `'l'` is a `Char`. Since `c` and `'l'` are being compared with equality with `(==)` and both arguments of `(==)` must have the same type, it follows that `c` must be a `Char`. Finally, since `isL c` is the result of `(==)` it must be a `Bool`. And thus we have a signature for the function:

**Example:** `isL` with a type

```mw
isL :: Char -> Bool
isL c = c == 'l'
```

Indeed, if you leave out the type signature, the Haskell compiler will discover it through this process. You can verify that by using :t on `isL` with or without a signature.

So why write type signatures if they will be inferred anyway? In some cases, the compiler lacks information to infer the type, and so the signature becomes obligatory. In some other cases, we can use a type signature to influence to a certain extent the final type of a function or value. These cases needn't concern us for now, but we have a few other reasons to include type signatures:

- **Documentation**: type signatures make your code easier to read. With most functions, the name of the function along with the type of the function is sufficient to guess what the function does. Of course, commenting your code helps, but having the types clearly stated helps too.
- **Debugging**: when you annotate a function with a type signature and then make a typo in the body of the function which changes the type of a variable, the compiler will tell you, *at compile-time*, that your function is wrong. Leaving off the type signature might allow your erroneous function to compile, and the compiler would assign it the wrong type. You wouldn't know until you ran your program that you made this mistake.

### Types and readability

A somewhat more realistic example will help us understand better how signatures can help documentation. The piece of code quoted below is a tiny *module* (modules are the typical way of preparing a library), and this way of organizing code is like that in the libraries bundled with GHC.

*Note*

Do not go crazy trying to understand how the functions here actually work; that is beside the point as we still have not covered many of the features being used. Just keep reading and play along.

**Example:** Module with type signatures

```mw
module StringManip where

import Data.Char

uppercase, lowercase :: String -> String
uppercase = map toUpper
lowercase = map toLower

capitalize :: String -> String
capitalize x =
  let capWord []     = []
      capWord (x:xs) = toUpper x : xs
  in unwords (map capWord (words x))
```

This tiny library provides three string manipulation functions. `uppercase` converts a string to upper case, `lowercase` to lower case, and `capitalize` capitalizes the first letter of every word. Each of these functions takes a `String` as argument and evaluates to another `String`. Even if we do not understand how these functions work, looking at the type signatures allows us to immediately know the types of the arguments and return values. Paired with sensible function names, we have enough information to figure out how we can use the functions.

Note that when functions have the same type we have the option of writing just one signature for all of them, by separating their names with commas, as above with `uppercase` and `lowercase`.

### Types prevent errors

The role of types in preventing errors is central to typed languages. When passing expressions around you have to make sure the types match up like they did here. If they don't, you'll get *type errors* when you try to compile; your program won't pass the *typecheck*. This helps reduce bugs in your programs. To take a very trivial example:

**Example:** A non-typechecking program

```mw
"hello" + " world"     -- type error
```

That line will cause a program to fail when compiling. You can't add two strings together. In all likelihood, the programmer intended to use the similar-looking concatenation operator, which can be used to join two strings together into a single one:

**Example:** Our erroneous program, fixed

```mw
"hello" ++ " world"    -- "hello world"
```

An easy typo to make, but Haskell catches the error when you tried to compile. You don't have to wait until you run the program for the bug to become apparent.

Updating a program commonly involves changes to types. If a change is unintended, or has unforeseen consequences, then it will show up when compiling. Haskell programmers often remark that once they have fixed all the type errors, and their programs compile, that they tend to "just work". The behavior may not always match the intention, but the program won't crash. Haskell has far fewer *run-time errors* (where your program goes wrong when you run it rather than when you compile) than other languages.
