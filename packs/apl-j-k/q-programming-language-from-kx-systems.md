---
title: "Q (programming language from Kx Systems)"
source: https://en.wikipedia.org/wiki/Q_(programming_language_from_Kx_Systems)
domain: apl-j-k
license: CC-BY-SA-4.0
tags: j language, k language, array programming language, iverson notation, apl language
fetched: 2026-07-02
---

# Q (programming language from Kx Systems)

**Q** is a programming language for array processing, developed by Arthur Whitney. It is proprietary software, commercialized by KX Systems. Q serves as the query language for kdb+, a disk based and in-memory, column-based database. Kdb+ is based on the language k, a terse variant of the language APL. Q is a thin wrapper library around k, providing a more readable, English-like interface. One of the use cases is financial time series analysis, as one could do inexact time matches. An example is to match the a bid and the ask before that. Both timestamps slightly differ and are matched anyway.

## Overview

The fundamental building blocks of q are *atoms*, *lists*, and *functions*. Atoms are scalars and include the data types numeric, character, date, and time. Lists are ordered collections of atoms (or other lists) upon which the higher level data structures *dictionaries* and *tables* are internally constructed. A dictionary is a map of a list of keys to a list of values. A table is a transposed dictionary of symbol keys and equal length lists (columns) as values. A *keyed table*, analogous to a table with a primary key placed on it, is a dictionary where the keys and values are arranged as two tables.

The following code demonstrates the relationships of the data structures. Expressions to evaluate appear prefixed with the `q)` prompt, with the output of the evaluation shown beneath:

```mw
q)`john / an atom of type symbol
`john
q)50    / an atom of type integer
50

q)`john`jack / a list of symbols
`john`jack
q)50 60 / a list of integers
50 60

q)`john`jack!50 60 / a list of symbols and a list of integers combined to form a dictionary
john| 50
jack| 60

q)`name`age!(`john`jack;50 60) / an arrangement termed a column dictionary
name| john jack
age | 50   60

q)flip `name`age!(`john`jack;50 60) / when transposed via the function "flip", the column dictionary becomes a table
name age
--------
john 50
jack 60

q)(flip (enlist `name)!enlist `john`jack)!flip (enlist `age)!enlist 50 60  / two equal length tables combined as a dictionary become a keyed table
name| age
----| ---
john| 50
jack| 60
```

These entities are manipulated via functions, which include the built-in functions that come with Q (which are defined as K macros) and user-defined functions. Functions are a data type, and can be placed in lists, dictionaries and tables, or passed to other functions as parameters.

## Examples

Like K, Q is interpreted and the result of the evaluation of an expression is immediately displayed, unless terminated with a semi-colon. The "Hello, World!" program is thus trivial:

```mw
q)"Hello world!"
"Hello world!"
```

The following expression sorts a list of strings stored in the variable x descending by their lengths:

```mw
x@idesc count each x
```

The expression is evaluated from right to left as follows:

1. "count each x" returns the length of each word in the list x.
2. "idesc" returns the indices that would sort a list of values in descending order.
3. @ use the integer values on the right to index into the original list of strings.

The factorial function can be implemented directly in Q as

```mw
{prd 1+til x}
```

or recursively as

```mw
{$[x=0;1;x*.z.s[x-1]]}
```

Note that in both cases the function implicitly takes a single argument called x - in general it is possible to use up to three implicit arguments, named x, y and z, or to give arguments local variable bindings explicitly.

In the direct implementation, the expression "til x" enumerates the integers from 0 to x-1, "1+" adds 1 to every element of the list and "prd" returns the product of the list.

In the recursive implementation, the syntax "$[condition; expr1; expr2]" is a ternary conditional - if the condition is true then expr1 is returned; otherwise expr2 is returned. The expression ".z.s" is loosely equivalent to 'this' in Java or 'self' in Python - it is a reference to the containing object, and enables functions in q to call themselves.

When x is an integer greater than 2, the following function will return 1 if it is a prime, otherwise 0:

```mw
{min x mod 2_til x}
```

The function is evaluated from right to left:

1. "til x" enumerate the non-negative integers less than x.
2. "2_" drops the first two elements of the enumeration (0 and 1).
3. "x mod" performs modulo division between the original integer and each value in the truncated list.
4. "min" find the minimum value of the list of modulo result.

The q programming language contains its own table query syntax called qSQL, which resembles traditional SQL but has important differences, mainly due to the fact that the underlying tables are oriented by column, rather than by row.

```mw
q)show t:([] name:`john`jack`jill`jane; age: 50 60 50 20) / define a simple table and assign to "t"
name age
--------
john 50
jack 60
jill 50
jane 20
```

```mw
 q)select from t where name like "ja*",age>50
 name age
 --------
 jack 60
 
 q)select rows:count i by age from t
 age| rows
 ---| ----
 20 | 1
 50 | 2
 60 | 1
```
