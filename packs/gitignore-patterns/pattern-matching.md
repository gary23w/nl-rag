---
title: "Pattern matching"
source: https://en.wikipedia.org/wiki/Pattern_matching
domain: gitignore-patterns
license: CC-BY-SA-4.0
tags: gitignore patterns, git ignore rules, glob ignore patterns, version control exclusion
fetched: 2026-07-02
---

# Pattern matching

In computer science, **pattern matching** is the act of checking a given sequence of tokens for the presence of the constituents of some pattern. In contrast to pattern recognition, the match usually must be exact: "either it will or will not be a match." The patterns generally have the form of either sequences or tree structures. Uses of pattern matching include outputting the locations (if any) of a pattern within a token sequence, to output some component of the matched pattern, and to substitute the matching pattern with some other token sequence (i.e., search and replace).

Sequence patterns (e.g., a text string) are often described using regular expressions and matched using techniques such as backtracking.

Tree patterns are used in some programming languages as a general tool to process data based on its structure, e.g. C#, F#, Haskell, Java, ML, Python, Racket, Ruby, Rust, Scala, Swift and the symbolic mathematics language Mathematica have special syntax for expressing tree patterns and a language construct for conditional execution and value retrieval based on it.

Often it is possible to give alternative patterns that are tried one by one, which yields a powerful conditional programming construct. Pattern matching sometimes includes support for guards.

## History

Early programming languages with pattern matching constructs include COMIT (1957), SNOBOL (1962), which introduced pattern matching as a core, first-class language capability for string and text manipulation. This paradigm evolved into structured, tree-based data evaluation with Refal (1968), which used pattern matching to manipulate symbolic expressions. The concept was soon adapted into logic programming with Prolog (1972), where pattern matching took the form of structural unification to resolve logical queries. Functional programming languages rapidly adopted and formalized the feature across the late 1970s and early 1980s, beginning with the St Andrews Static Language (SASL) (1976), NPL (1977), and the Kent Recursive Calculator (KRC) (1981).

The pattern matching feature of function arguments in the language ML (1973) and its dialect Standard ML (1983) heavily formalized compile-time exhaustiveness checking. This approach has been carried over to some other functional programming languages that were influenced by them, such as Haskell (1990), Scala (2004), and F# (2005). The pattern matching construct with the `match` keyword that was introduced in the ML dialect Caml (1985) was followed by languages such as OCaml (1996), F# (2005), F* (2011), and Rust (2015). Over time, multi-paradigm languages begin implementing algebraic data types and pattern matching natively, culminating in modern implementations like Python's `match-case` syntax (2021) and Java's pattern matching enhancements (2023).

Many text editors support pattern matching of various kinds to facilitate advanced search-and-replace capabilities. The QED editor, designed by Ken Thompson, was a pioneer in supporting regular expression searching. Thompson's implementation of regular expression parsing in QED laid the groundwork for the text search utilities in ed, sed, and grep. Furthermore, some versions of the TECO editor supported advanced matching features, including the logical OR operator in searches.

Computer algebra systems (CAS) generally support pattern matching on algebraic expressions to achieve symbolic simplification and integration. Early systems like Macsyma (1968) used semantic pattern matching to recognize algebraic equivalence; for example, its internal engine could successfully match both `3x2 + 4` and `(x + 1)(x + 6)` as occurrences of a "quadratic in x" pattern template. Modern computer algebra systems, including Mathematica and Maple, rely heavily on pattern-matching rules to transform user expressions, find analytical solutions to differential equations, and build user-defined simplification frameworks.

## Terminology

Pattern matching involves specialized terminology.

**Matching**

The act of comparing a

scrutinee

to a

pattern

(or collection of patterns), possibly selecting a

continuation

, extracting

bindings

, performing a

substitution

, or any combination of these. Also known as

destructuring

.

**Pattern**

Syntax describing expected structure in the

scrutinee

, plus specification of portions of the scrutinee to extract (

bindings

) or ignore (

wildcards

). Pattern languages can be rich; see below for terminology denoting specific kinds of pattern.

**Scrutinee**

The value to be examined and matched against a pattern. In most cases, this will be a data structure of some kind, with type

dual to

the pattern being applied. Also known as the

subject value

or

discriminant

.

**Continuation**

In some languages, when multiple alternative patterns are applied to a scrutinee, when one alternative matches, an associated code fragment is executed in an environment extended with the matching pattern's

bindings

. This code fragment is the

continuation

associated with the pattern.

**Substitution**

Replacement of a portion of a scrutinee data structure with some computed value. The computation may depend on the replaced portion of the scrutinee as well as on other bindings extracted from the scrutinee.

### Terminology of patterns

While some concepts are relatively common to many pattern languages, other pattern languages include unique or unusual extensions.

**Binding**

A way of associating a

name

with a portion of the scrutinee, so that the name is

bound to

that portion when the continuation executes. For example, in Rust,

match

v

{

(

a

,

b

)

=>

..

.

}

expects

v

to be a pair, and

a

and

b

are bindings bringing variables of the same name into scope in the continuation ("

...

").

**Wildcard**

Often written as a single underscore,

_

, the wildcard pattern accepts all values without examining them further, ignoring their structure. Also known as

discard

, the

wild pattern

, the

catch-all pattern

, or as a

hole

.

**Guard**

A

guard

is an expression that must succeed (or yield Boolean true) as a final step before considering a pattern to have successfully matched. In some languages (e.g.

Erlang

), guards are written using a restricted subset of the full language; in others (e.g.

Haskell

), guards may use the full language.

**Predicate**

Some pattern languages allow user-defined

predicate

functions to be embedded in a pattern. The predicate is applied to the portion of the scrutinee corresponding to the position of the predicate in the pattern; if the predicate responds with Boolean false, the pattern is considered to have failed. For example, in Racket, the pattern

(

list

(

?

even?

)

...

)

first expects a list, and then applies the predicate

even?

to each element; the overall pattern thus succeeds only when the scrutinee is a list of even numbers.

**View pattern**

Languages like Haskell

and Racket

include

view patterns

, where a user-defined function transforms the portion of the scrutinee corresponding to the position of the view pattern before continuing the match. View patterns generalize predicate patterns, allowing further matching on the result of the function rather than simply expecting a Boolean value.

**Constraint**

Some pattern languages allow direct comparison of portions of the scrutinee with previously-computed (or constant) data structures. For example, the pattern

(

==

expr

)

in Racket compares the value against the result of evaluating

expr

. In Erlang, mention of any variable already in scope in a pattern causes it to act as a constraint in this way (instead of as a binding).

**Literal pattern; atomic pattern**

Patterns that match simple atomic data such as

123

or

"hello"

are called

literal patterns

.

**Compound pattern**

Patterns that destructure compound values such as lists, hash tables, tuples, structures or records, with sub-patterns for each of the values making up the compound data structure, are called

compound patterns

.

**Alternative (`or`-pattern)**

Many languages allow multiple alternatives at the top-level of a pattern matching construct, each associated with a

continuation

; some languages allow alternatives

within

a pattern. In most cases, such alternatives have additional constraints placed on them: for example, every alternative may be required to produce the same set of

bindings

(at the same types).

**Macros**

Some languages allow macros in pattern context to allow abstraction over patterns. For example, in Racket,

match expanders

perform this role.

## Types

### Primitive patterns

The simplest pattern in pattern matching is an explicit value or a variable. For an example, consider a simple function definition in Haskell syntax (function parameters are not in parentheses but are separated by spaces, = is not assignment but definition):

```mw
f 0 = 1
```

Here, 0 is a single value pattern. Now, whenever f is given 0 as argument the pattern matches and the function returns 1. With any other argument, the matching and thus the function fail. As the syntax supports alternative patterns in function definitions, we can continue the definition extending it to take more generic arguments:

```mw
f n = n * f (n-1)
```

Here, the first `n` is a single variable pattern, which will match absolutely any argument and bind it to name n to be used in the rest of the definition. In Haskell (unlike at least Hope), patterns are tried in order so the first definition still applies in the very specific case of the input being 0, while for any other argument the function returns `n * f (n-1)` with n being the argument.

The wildcard pattern (often written as `_`) is also simple: like a variable name, it matches any value, but does not bind the value to any name. Algorithms for matching wildcards in simple string-matching situations have been developed in a number of recursive and non-recursive varieties.

### Tree patterns

More complex patterns can be built from the primitive ones of the previous section, usually in the same way as values are built by combining other values. The difference then is that with variable and wildcard parts, a pattern does not build into a single value, but matches a group of values that are the combination of the concrete elements and the elements that are allowed to vary within the structure of the pattern.

A tree pattern describes a part of a tree by starting with a node and specifying some branches and nodes and leaving some unspecified with a variable or wildcard pattern. It may help to think of the abstract syntax tree of a programming language and algebraic data types.

#### Haskell

In Haskell, the following line defines an algebraic data type `Color` that has a single data constructor `ColorConstructor` that wraps an integer and a string.

```mw
data Color = ColorConstructor Integer String
```

The constructor is a node in a tree and the integer and string are leaves in branches.

When we want to write functions to make `Color` an abstract data type, we wish to write functions to interface with the data type, and thus we want to extract some data from the data type, for example, just the string or just the integer part of `Color`.

If we pass a variable that is of type Color, how can we get the data out of this variable? For example, for a function to get the integer part of `Color`, we can use a simple tree pattern and write:

```mw
integerPart (ColorConstructor theInteger _) = theInteger
```

As well:

```mw
stringPart (ColorConstructor _ theString) = theString
```

The creations of these functions can be automated by Haskell's data record syntax.

#### OCaml

This OCaml example which defines a red–black tree and a function to re-balance it after element insertion shows how to match on a more complex structure generated by a recursive data type. The compiler verifies at compile-time that the list of cases is exhaustive and none are redundant.

```mw
type color = Red | Black
type 'a tree = Empty | Tree of color * 'a tree * 'a * 'a tree

let rebalance t = match t with
    | Tree (Black, Tree (Red, Tree (Red, a, x, b), y, c), z, d)
    | Tree (Black, Tree (Red, a, x, Tree (Red, b, y, c)), z, d)                                  
    | Tree (Black, a, x, Tree (Red, Tree (Red, b, y, c), z, d))
    | Tree (Black, a, x, Tree (Red, b, y, Tree (Red, c, z, d)))
        ->  Tree (Red, Tree (Black, a, x, b), y, Tree (Black, c, z, d))
    | _ -> t (* the 'catch-all' case if no previous pattern matches *)
```

## Usage

### Filtering data with patterns

Pattern matching can be used to filter data of a certain structure. For instance, in Haskell a list comprehension could be used for this kind of filtering:

```mw
[A x|A x <- [A 1, B 1, A 2, B 2]]
```

evaluates to

```
[A 1, A 2]
```

### Pattern matching in Mathematica

In Mathematica, the only structure that exists is the tree, which is populated by symbols. In the Haskell syntax used thus far, this could be defined as

```mw
data SymbolTree = Symbol String [SymbolTree]
```

An example tree could then look like

```mw
Symbol "a" [Symbol "b" [], Symbol "c" []]
```

In the traditional, more suitable syntax, the symbols are written as they are and the levels of the tree are represented using `[]`, so that for instance `a[b,c]` is a tree with a as the parent, and b and c as the children.

A pattern in Mathematica involves putting "_" at positions in that tree. For instance, the pattern

```
A[_]
```

will match elements such as A[1], A[2], or more generally A[*x*] where *x* is any entity. In this case, `A` is the concrete element, while `_` denotes the piece of tree that can be varied. A symbol prepended to `_` binds the match to that variable name while a symbol appended to `_` restricts the matches to nodes of that symbol. Note that even blanks themselves are internally represented as `Blank[]` for `_` and `Blank[x]` for `_x`.

The Mathematica function `Cases` filters elements of the first argument that match the pattern in the second argument:

```mw
Cases[{a[1], b[1], a[2], b[2]}, a[_] ]
```

evaluates to

```mw
{a[1], a[2]}
```

Pattern matching applies to the *structure* of expressions. In the example below,

```mw
Cases[ {a[b], a[b, c], a[b[c], d], a[b[c], d[e]], a[b[c], d, e]}, a[b[_], _] ]
```

returns

```mw
{a[b[c],d], a[b[c],d[e]]}
```

because only these elements will match the pattern `a[b[_],_]` above.

In Mathematica, it is also possible to extract structures as they are created in the course of computation, regardless of how or where they appear. The function `Trace` can be used to monitor a computation, and return the elements that arise which match a pattern. For example, we can define the Fibonacci sequence as

```mw
fib[0|1]:=1
fib[n_]:= fib[n-1] + fib[n-2]
```

Then, we can ask the question: Given fib[3], what is the sequence of recursive Fibonacci calls?

```mw
Trace[fib[3], fib[_]]
```

returns a structure that represents the occurrences of the pattern `fib[_]` in the computational structure:

```mw
{fib[3],{fib[2],{fib[1]},{fib[0]}},{fib[1]}}
```

#### Declarative programming

In symbolic programming languages, it is easy to have patterns as arguments to functions or as elements of data structures. A consequence of this is the ability to use patterns to declaratively make statements about pieces of data and to flexibly instruct functions how to operate.

For instance, the Mathematica function `Compile` can be used to make more efficient versions of the code. In the following example the details do not particularly matter; what matters is that the subexpression `{{com[_], Integer}}` instructs `Compile` that expressions of the form `com[_]` can be assumed to be integers for the purposes of compilation:

```mw
com[i_] := Binomial[2i, i]
Compile[{x, {i, _Integer}}, x^com[i], {{com[_],  Integer}}]
```

Mailboxes in Erlang also work this way.

The Curry–Howard correspondence between proofs and programs relates ML-style pattern matching to case analysis and proof by exhaustion.

### Pattern matching and strings

By far the most common form of pattern matching involves strings of characters. In many programming languages, a particular syntax of strings is used to represent regular expressions, which are patterns describing string characters.

However, it is possible to perform some string pattern matching within the same framework that has been discussed throughout this article.

#### Tree patterns for strings

In Mathematica, strings are represented as trees of root StringExpression and all the characters in order as children of the root. Thus, to match "any amount of trailing characters", a new wildcard ___ is needed in contrast to _ that would match only a single character.

In Haskell and functional programming languages in general, strings are represented as functional lists of characters. A functional list is defined as an empty list, or an element constructed on an existing list. In Haskell syntax:

```mw
[] -- an empty list
x:xs -- an element x constructed on a list xs
```

The structure for a list with some elements is thus `element:list`. When pattern matching, we assert that a certain piece of data is equal to a certain pattern. For example, in the function:

```mw
head (element:list) = element
```

We assert that the first element of `head`'s argument is called element, and the function returns this. We know that this is the first element because of the way lists are defined, a single element constructed onto a list. This single element must be the first. The empty list would not match the pattern at all, as an empty list does not have a head (the first element that is constructed).

In the example, we have no use for `list`, so we can disregard it, and thus write the function:

```mw
head (element:_) = element
```

The equivalent Mathematica transformation is expressed as

```
head[element, ]:=element
```

#### Example string patterns

In Mathematica, for instance,

```mw
StringExpression["a",_]
```

will match a string that has two characters and begins with "a".

The same pattern in Haskell:

```mw
['a', _]
```

Symbolic entities can be introduced to represent many different classes of relevant features of a string. For instance,

```
StringExpression[LetterCharacter, DigitCharacter]
```

will match a string that consists of a letter first, and then a number.

In Haskell, guards could be used to achieve the same matches:

```mw
[letter, digit] | isAlpha letter && isDigit digit
```

The main advantage of symbolic string manipulation is that it can be completely integrated with the rest of the programming language, rather than being a separate, special purpose subunit. The entire power of the language can be leveraged to build up the patterns themselves or analyze and transform the programs that contain them.

#### SNOBOL

SNOBOL (*StriNg Oriented and symBOlic Language*) is a computer programming language developed between 1962 and 1967 at AT&T Bell Laboratories by David J. Farber, Ralph E. Griswold and Ivan P. Polonsky.

SNOBOL4 stands apart from most programming languages by having patterns as a first-class data type (*i.e.* a data type whose values can be manipulated in all ways permitted to any other data type in the programming language) and by providing operators for pattern concatenation and alternation. Strings generated during execution can be treated as programs and executed.

SNOBOL was quite widely taught in larger US universities in the late 1960s and early 1970s and was widely used in the 1970s and 1980s as a text manipulation language in the humanities.

Since SNOBOL's creation, newer languages such as AWK and Perl have made string manipulation by means of regular expressions fashionable. SNOBOL4 patterns, however, subsume Backus–Naur form (BNF) grammars, which are equivalent to context-free grammars and more powerful than regular expressions.
