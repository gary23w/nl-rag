---
title: "Miranda (programming language)"
source: https://en.wikipedia.org/wiki/Miranda_(programming_language)
domain: miranda-language
license: CC-BY-SA-4.0
tags: miranda language, david turner computer scientist, lazy evaluation, purely functional programming, referential transparency
fetched: 2026-07-02
---

# Miranda (programming language)

**Miranda** is a lazy, purely functional programming language designed by David Turner as a successor to his earlier programming languages SASL and KRC, using some concepts from ML and Hope. It was produced by Research Software Ltd. of England (which holds a trademark on the name *Miranda*) and was the first purely functional language to be commercially supported.

Miranda was first released in 1985 as a fast interpreter in C for Unix-flavour operating systems, with subsequent releases in 1987 and 1989. It had a strong influence on the later Haskell language. Turner stated that the benefits of Miranda over Haskell are: "Smaller language, simpler type system, simpler arithmetic".

In 2020 a version of Miranda was released as open source under a BSD licence. The code has been updated to conform to modern C standards (C11/C18) and to generate 64-bit binaries. This has been tested on operating systems including Debian, Ubuntu, WSL/Ubuntu, and macOS (Catalina).

## Name

The name *Miranda* is taken from the gerundive form of the latin verb *miror*, meaning "to be admired".

The logo features a rendition by John William Waterhouse of the character Miranda from Shakespeare's *The Tempest*.

## Overview

Miranda is a lazy, purely functional programming language. That is, it lacks side effects and imperative programming features. A Miranda program (called a *script*) is a set of equations that define various mathematical functions and algebraic data types. The word *set* is important here: the order of the equations is, in general, irrelevant, and there is no need to define an entity prior to its use.

Since the parsing algorithm makes intelligent use of layout (indentation, via off-side rule), bracketing statements are rarely needed and statement terminators are unneeded. This feature, inspired by ISWIM, is also used in occam and Haskell and was later popularized by Python.

Commentary is introduced into regular scripts by the characters `||` and continue to the end of the same line. An alternative commenting convention affects an entire source code file, known as a "literate script", in which every line is considered a comment unless it starts with a `>` sign.

Miranda's basic data types are `char`, `num` and `bool`. A character string is simply a list of `char`, while `num` is silently converted between two underlying forms: arbitrary-precision integers (a.k.a. bignums) by default, and regular floating point values as required.

Tuples are groups of elements of potentially mixed types, in a fixed order, analogous to records in Pascal-like languages, but with unnamed fields. They are delimited with parentheses:

```mw
  this_employee = ("Folland, Mary", 10560, False, 35)
```

The *list* instead is the most commonly used data structure in Miranda. It is written delimited by square brackets and with comma-separated elements, all of which must be of the same type:

```mw
  week_days = ["Mon","Tue","Wed","Thur","Fri"]
```

List concatenation is `++`, subtraction is `--`, construction is `:`, sizing is `#` and indexing is `!`, so:

```mw
  days = week_days ++ ["Sat","Sun"]
  days = "Nil":days
  days!0
 ⇒ "Nil"
  days = days -- ["Nil"]
  #days
 ⇒ 7
```

There are several list-building shortcuts: `..` is used for lists whose elements form an arithmetic series, with the possibility for specifying an increment other than 1:

```mw
  fac n   = product [1..n]
  odd_sum = sum [1,3..100]
```

More general and powerful list-building facilities are provided by "list comprehensions" (previously known as "ZF expressions"), which come in two main forms: an expression applied to a series of terms, e.g.:

```mw
  squares = [ n * n | n <- [1..] ]
```

(which is read: list of n squared where n is taken from the list of all positive integers) and a series where each term is a function of the previous one, e.g.:

```mw
  powers_of_2 = [ n | n <- 1, 2*n .. ]
```

As these two examples imply, Miranda allows for lists with an infinite number of elements, of which the simplest is the list of all positive integers: `[1..]`

The notation for function application is simply juxtaposition, as in `sin x`.

In Miranda, as in most other purely functional languages, functions are first-class citizens, which is to say that they can be passed as arguments to other functions, returned as results, or included as elements of data structures. What is more, a function with two or more parameters may be "partially parameterised", or curried, by supplying fewer arguments than the full number of parameters. This gives another function which, given the remaining parameters, will return a result. For example:

```mw
  add a b = a + b
  increment = add 1
```

is a roundabout way of creating a function "increment" which adds one to its argument. In reality, `add 4 7` takes the two-parameter function `add`, applies it to `4` obtaining a single-parameter function that adds four to its argument, then applies that to `7`.

Any function with two parameters (operands) can be turned into an infix operator (for example, given the definition of the `add` function above, the term `$add` is in every way equivalent to the `+` operator) and every infix operator taking two parameters can be turned into a corresponding function. Thus:

```mw
  increment = (+) 1
```

is the briefest way to create a function that adds one to its argument. Similarly, in

```mw
  half = (/ 2)
  reciprocal = (1 /)
```

two single-parameter functions are generated. The interpreter understands in each case which of the divide operator's two parameters is being supplied, giving functions which respectively divide a number by two and return its reciprocal.

Although Miranda is a strongly typed programming language, it does not insist on explicit type declarations. If a function's type is not explicitly declared, the interpreter infers it from the type of its parameters and how they are used within the function. In addition to the basic types (`char`, `num`, `bool`), it includes an "anything" type where the type of a parameter does not matter, as in the list-reversing function:

```mw
  rev [] = []
  rev (a:x) = rev x ++ [a]
```

which can be applied to a list of any data type, for which the explicit function type declaration would be:

```mw
  rev :: [*] -> [*]
```

Finally, it has mechanisms for creating and managing program modules whose internal functions are invisible to programs calling those modules.

## Sample code

The following Miranda script defines the list of all sublists of a given list

```mw
 sublists []     = [[]]
 sublists (x:xs) = [[x] ++ y | y <- ys] ++ ys
                   where ys = sublists xs
```

and this is a literate script for a function `primes` which gives the list of all prime numbers

```mw
> || The infinite list of all prime numbers.

The list of potential prime numbers starts as all integers from 2 onwards;
as each prime is returned, all the following numbers that can exactly be
divided by it are filtered out of the list of candidates.

> primes = sieve [2..]
> sieve (p:x) = p : sieve [n | n <- x; n mod p ~= 0]
```

Here, we have some more examples

```mw
max2 :: num -> num -> num
max2 a b = a, if a>b
         = b, otherwise

max3 :: num -> num -> num -> num
max3 a b c = max2 (max2 a b) (max2 a c)

fak :: num -> num
fak 0 = 1
fak n = n * fak (n-1)

itemnumber::[*]->num
itemnumber [] = 0
itemnumber (a:x) = 1 + itemnumber x

weekday::= Mo|Tu|We|Th|Fr|Sa|Su

isWorkDay :: weekday -> bool
isWorkDay Sa = False
isWorkDay Su = False
isWorkDay anyday = True

tree * ::= E| N (tree *) * (tree *)

nodecount :: tree * -> num
nodecount E = 0
nodecount (N l w r) = nodecount l + 1 + nodecount r

emptycount :: tree * -> num
emptycount E = 1
emptycount (N l w r) = emptycount l + emptycount r

treeExample = N ( N (N E 1 E) 3 (N E 4 E)) 5 (N (N E 6 E) 8 (N E 9 E))
weekdayTree = N ( N (N E Mo E) Tu (N E We E)) Th (N (N E Fr E) Sa (N E Su))

insert :: * -> stree * -> stree *
insert x E = N E x E
insert x (N l w E) = N l w x
insert x (N E w r) = N x w r
insert x (N l w r) = insert x l , if x <w
                   = insert x r , otherwise

list2searchtree :: [*] -> tree *
list2searchtree [] = E
list2searchtree [x] = N E x E
list2searchtree (x:xs) = insert x (list2searchtree xs)

maxel :: tree * -> *
maxel E = error "empty"
maxel (N l w E) = w
maxel (N l w r) = maxel r

minel :: tree * -> *
minel E = error "empty"
minel (N E w r) = w
minel (N l w r) = minel l

||Traversing: going through values of tree, putting them in list

preorder,inorder,postorder :: tree * -> [*]
inorder E = []
inorder N l w r = inorder l ++ [w] ++ inorder r

preorder E = []
preorder N l w r = [w] ++ preorder l ++ preorder r

postorder E = []
postorder N l w r = postorder l ++ postorder r ++ [w]

height :: tree * -> num
height E = 0
height (N l w r) = 1 + max2 (height l) (height r)

amount :: num -> num
amount x = x ,if x >= 0
amount x = x*(-1), otherwise

and :: bool -> bool -> bool
and True True = True
and x y = False

|| A AVL-Tree is a tree where the difference between the child nodes is not higher than 1
|| i still have to test this

isAvl :: tree * -> bool
isAvl E = True
isAvl (N l w r) = and (isAvl l) (isAvl r), if amount ((nodecount l) - (nodecount r)) < 2
                = False, otherwise

delete :: * -> tree * -> tree *
delete x E = E
delete x (N E x E) = E
delete x (N E x r) = N E (minel r) (delete (minel r) r)
delete x (N l x r) = N (delete (maxel l) l) (maxel l) r
delete x (N l w r) = N (delete x l) w (delete x r)
```
