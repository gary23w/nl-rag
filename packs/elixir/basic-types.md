---
title: "Basic types"
source: https://hexdocs.pm/elixir/basic-types.html
domain: elixir
license: Apache-2.0
tags: elixir, hexdocs, iex
fetched: 2026-07-02
---

# Basic types

Copy Markdown

View Source

In this chapter we will learn more about Elixir basic types: integers, floats, booleans, atoms, and strings. Other data types, such as lists and tuples, will be explored in the next chapter.

```
iex> 1          # integer
iex> 0x1F       # integer
iex> 1.0        # float
iex> true       # boolean
iex> :atom      # atom / symbol
iex> "elixir"   # string
iex> [1, 2, 3]  # list
iex> {1, 2, 3}  # tuple
```

## Basic arithmetic

Open up `iex` and type the following expressions:

```
iex> 1 + 2
3
iex> 5 * 5
25
iex> 10 / 2
5.0
```

Notice that `10 / 2` returned a float `5.0` instead of an integer `5`. This is expected. In Elixir, the operator `/` always returns a float. If you want to do integer division or get the division remainder, you can invoke the `div` and `rem` functions:

```
iex> div(10, 2)
5
iex> div 10, 2
5
iex> rem 10, 3
1
```

Notice that Elixir allows you to drop the parentheses when invoking functions that expect one or more arguments. This feature gives a cleaner syntax when writing declarations and control-flow constructs. However, Elixir developers generally prefer to use parentheses.

Elixir also supports shortcut notations for entering binary, octal, and hexadecimal numbers:

```
iex> 0b1010
10
iex> 0o777
511
iex> 0x1F
31
```

Float numbers require a dot followed by at least one digit and also support `e` for scientific notation:

```
iex> 1.0
1.0
iex> 1.0e-10
1.0e-10
```

Floats in Elixir are 64-bit precision.

You can invoke the `round` function to get the closest integer to a given float, or the `trunc` function to get the integer part of a float.

```
iex> round(3.58)
4
iex> trunc(3.58)
3
```

Finally, as we work with different data types, we will learn that Elixir provides several predicate functions to check for the type of a value. For example, `is_integer` can be used to check if a value is an integer or not:

```
iex> is_integer(1)
true
iex> is_integer(2.0)
false
```

You can also use `is_float` or `is_number` to check, respectively, if an argument is a float, or either an integer or float.

## Booleans and `nil`

Elixir supports `true` and `false` as booleans:

```
iex> true
true
iex> true == false
false
```

Elixir also provides three boolean operators: `or`, `and`, and `not`. These operators are strict in the sense that they expect something that evaluates to a boolean (`true` or `false`) as their first argument:

```
iex> true and true
true
iex> false or is_boolean(true)
true
```

Providing a non-boolean will raise an exception:

```
iex> 1 and true
** (BadBooleanError) expected a boolean on left-side of "and", got: 1
```

`or` and `and` are short-circuit operators. They only execute the right side if the left side is not enough to determine the result:

```
iex> false and raise("This error will never be raised")
false
iex> true or raise("This error will never be raised")
true
```

Elixir also provides the concept of `nil`, to indicate the absence of a value, and a set of logical operators that also manipulate `nil`: `||/2`, `&&/2`, and `!/1`. For these operators, `false` and `nil` are considered "falsy", all other values are considered "truthy":

```
# or
iex> 1 || true
1
iex> false || 11
11

# and
iex> nil && 13
nil
iex> true && 17
17

# not
iex> !true
false
iex> !1
false
iex> !nil
true
```

Similarly, values like `0` and `""`, which some other programming languages consider to be "falsy", are also "truthy" in Elixir.

As a rule of thumb, use `and`, `or` and `not` when you are expecting booleans. If any of the arguments are non-boolean, use `&&`, `||` and `!`.

## Atoms

An atom is a constant whose value is its own name. Some other languages call these symbols. They are often useful to enumerate over distinct values, such as:

```
iex> :apple
:apple
iex> :orange
:orange
iex> :watermelon
:watermelon
```

Atoms are equal if their names are equal.

```
iex> :apple == :apple
true
iex> :apple == :orange
false
```

Often they are used to express the state of an operation, by using values such as `:ok` and `:error`.

The booleans `true` and `false` are also atoms:

```
iex> true == :true
true
iex> is_atom(false)
true
iex> is_boolean(:false)
true
```

Elixir allows you to skip the leading `:` for the atoms `false`, `true` and `nil`.

## Strings

Strings in Elixir are delimited by double quotes, and they are encoded in UTF-8:

```
iex> "hellö"
"hellö"
```

> Note: if you are running on Windows, there is a chance your terminal does not use UTF-8 by default. You can change the encoding of your current session by running `chcp 65001` before entering IEx.

You can concatenate two strings with the `<>` operator:

```
iex> "hello " <> "world!"
"hello world!"
```

Elixir also supports string interpolation:

```
iex> string = "world"
iex> "hello #{string}!"
"hello world!"
```

String concatenation requires both sides to be strings but interpolation supports any data type that may be converted to a string:

```
iex> number = 42
iex> "i am #{number} years old!"
"i am 42 years old!"
```

Strings can have line breaks in them. You can introduce them using escape sequences:

```
iex> "hello
...> world"
"hello\nworld"
iex> "hello\nworld"
"hello\nworld"
```

You can print a string using the `IO.puts` function from the `IO` module:

```
iex> IO.puts("hello\nworld")
hello
world
:ok
```

Notice that the `IO.puts` function returns the atom `:ok` after printing.

Strings in Elixir are represented internally by contiguous sequences of bytes known as binaries:

```
iex> is_binary("hellö")
true
```

We can also get the number of bytes in a string:

```
iex> byte_size("hellö")
6
```

Notice that the number of bytes in that string is 6, even though it has 5 graphemes. That's because the grapheme "ö" takes 2 bytes to be represented in UTF-8. We can get the actual length of the string, based on the number of graphemes, by using the `String.length` function:

```
iex> String.length("hellö")
5
```

The `String` module contains a bunch of functions that operate on strings as defined in the Unicode standard:

```
iex> String.upcase("hellö")
"HELLÖ"
```

## Structural comparison

Elixir also provides `==`, `!=`, `<=`, `>=`, `<` and `>` as comparison operators. We can compare numbers:

```
iex> 1 == 1
true
iex> 1 != 2
true
iex> 1 < 2
true
```

But also atoms, strings, booleans, etc:

```
iex> "foo" == "foo"
true
iex> "foo" == "bar"
false
```

Integers and floats compare the same if they have the same value:

```
iex> 1 == 1.0
true
iex> 1 == 2.0
false
```

However, you can use the strict comparison operator `===` and `!==` if you want to distinguish between integers and floats:

```
iex> 1 === 1.0
false
```

The comparison operators in Elixir can compare across any data type. We say these operators perform *structural comparison*. For more information, you can read our documentation on Structural vs Semantic comparisons.

Elixir also provides data-types for expressing collections, such as lists and tuples, which we'll learn next. When we talk about concurrency and fault-tolerance via processes, we will also discuss ports, pids, and references, but that will come in later chapters. Let's move forward.

← Previous Page

Introduction

Next Page →

Lists and tuples
