---
title: "Referential transparency"
source: https://en.wikipedia.org/wiki/Referential_transparency
domain: miranda-language
license: CC-BY-SA-4.0
tags: miranda language, david turner computer scientist, lazy evaluation, purely functional programming, referential transparency
fetched: 2026-07-02
---

# Referential transparency

In analytic philosophy and computer science, **referential transparency** and **referential opacity** are properties of linguistic constructions, and by extension of languages. A linguistic construction is called *referentially transparent* when for any expression built from it, replacing a subexpression with another one that denotes the same value does not change the value of the expression. Otherwise, it is called *referentially opaque*. Each expression built from a referentially opaque linguistic construction states something about a subexpression, whereas each expression built from a referentially transparent linguistic construction states something not about a subexpression, meaning that the subexpressions are ‘transparent’ to the expression, acting merely as ‘references’ to something else. For example, the linguistic construction ‘_ was wise’ is referentially transparent (e.g., *Socrates was wise* is equivalent to *The founder of Western philosophy was wise*) but ‘_ said _’ is referentially opaque (e.g., *Xenophon said ‘Socrates was wise’* is not equivalent to *Xenophon said ‘The founder of Western philosophy was wise’*).

Referential transparency, in programming languages, depends on semantic equivalences among denotations of expressions, or on contextual equivalence of expressions themselves. That is, referential transparency depends on the semantics of the language. So, both declarative languages and imperative languages can have referentially transparent positions, referentially opaque positions, or (usually) both, according to the semantics they are given.

The importance of referentially transparent positions is that they allow the programmer and the compiler to reason about program behavior as a rewrite system at those positions. This can help in proving correctness, simplifying an algorithm, assisting in modifying code without breaking it, or optimizing code by means of memoization, common subexpression elimination, lazy evaluation, constant folding, or parallelization.

## History

The concept originated in Alfred North Whitehead and Bertrand Russell's *Principia Mathematica* (1910–1913):

> A proposition as the vehicle of truth or falsehood is a particular occurrence, while a proposition considered factually is a class of similar occurrences. It is the proposition considered factually that occurs in such statements as “*A* believes *p*“ and “*p* is about *A*.”
> 
> Of course it is possible to make statements about the particular fact “Socrates is Greek.” We may say how many centimetres long it is; we may say it is black; and so on. But these are not the statements that a philosopher or logician is tempted to make.
> 
> When an assertion occurs, it is made by means of a particular fact, which is an instance of the proposition asserted. But this particular fact is, so to speak, “transparent”; nothing is said about it, but by means of it something is said about something else. It is this “transparent” quality that belongs to propositions as they occur in truth-functions. This belongs to *p* when *p* is asserted, but not when we say “*p* is true.”

It was adopted in analytic philosophy in Willard Van Orman Quine's *Word and Object* (1960):

> When a singular term is used in a sentence purely to specify its object, and the sentence is true of the object, then certainly the sentence will stay true when any other singular term is substituted that designates the same object. Here we have a criterion for what may be called *purely referential position*: the position must be subject to the *substitutivity of identity*.
> 
> […]
> 
> Referential transparency has to do with constructions (§ 11); modes of containment, more specifically, of singular terms or sentences in singular terms or sentences. I call a mode of containment φ referentially transparent if, whenever an occurrence of a singular term t is purely referential in a term or sentence *ψ*(*t*), it is purely referential also in the containing term or sentence *φ*(*ψ*(*t*)).

The term appeared in its contemporary computer science usage in the discussion of variables in programming languages in Christopher Strachey's seminal set of lecture notes *Fundamental Concepts in Programming Languages* (1967):

> One of the most useful properties of expressions is that called by Quine [4] *referential transparency*. In essence this means that if we wish to find the value of an expression which contains a sub-expression, the only thing we need to know about the sub-expression is its value. Any other features of the sub-expression, such as its internal structure, the number and nature of its components, the order in which they are evaluated or the colour of the ink in which they are written, are irrelevant to the value of the main expression.

## Formal definitions

There are three fundamental properties concerning substitutivity in formal languages: referential transparency, definiteness, and unfoldability.

Let’s denote syntactic equivalence with ≡ and semantic equivalence with =.

### Referential transparency

A *position* is defined by a sequence of natural numbers. The empty sequence is denoted by ε and the sequence constructor by ‘.’.

*Example.* — Position 2.1 in the expression (+ (∗ *e*1 *e*1) (∗ *e*2 *e*2)) is the place occupied by the first occurrence of *e*2.

Expression e *with* expression e′ *inserted at* position p is denoted by *e*[*e′*/*p*] and defined by

e

[

e′

/ε] ≡

e′

e

[

e′

/

i

.

p

] ≡ <Ω

e

1

…

e

i

[

e′

/

p

] …

e

n

>

if

e

≡ <Ω

e

1

…

e

i

…

e

n

>

else undefined, for all operators

Ω

and expressions

e

1

, …,

e

n

.

*Example.* — If *e* ≡ (+ (∗ *e*1 *e*1) (∗ *e*2 *e*2)) then *e*[*e*3/2.1] ≡ (+ (∗ *e*1 *e*1) (∗ *e*3 *e*2)).

Position p is *purely referential* in expression e is defined by

e

1

=

e

2

implies

e

[

e

1

/

p

] =

e

[

e

2

/

p

]

, for all expressions

e

1

,

e

2

.

In other words, a position is purely referential in an expression if and only if it is subject to the substitutivity of equals. ε is purely referential in all expressions.

Operator Ω is *referentially transparent* in place i is defined by

p

is purely referential in

e

i

implies

i

.

p

is purely referential in

e

≡ <Ω

e

1

…

e

i

…

e

n

>

, for all positions

p

and expressions

e

1

, …,

e

n

.

Otherwise Ω is *referentially opaque* in place i.

An operator is *referentially transparent* is defined by it is referentially transparent in all places. Otherwise it is *referentially opaque*.

A formal language is *referentially transparent* is defined by all its operators are referentially transparent. Otherwise it is *referentially opaque*.

*Example.* — The ‘_ lives in _’ operator is referentially transparent:

She lives in London.

Indeed, the second position is purely referential in the assertion because substituting *The capital of the United Kingdom* for *London* does not change the value of the assertion. The first position is also purely referential for the same substitutivity reason.

*Example.* — The ‘_ contains _’ and quote operators are referentially opaque:

‘London’ contains six letters.

Indeed, the first position is not purely referential in the statement because substituting *The capital of the United Kingdom* for *London* changes the value of the statement and the quotation. So in the first position, the ‘_ contains _’ and quote operators destroy the relation between an expression and the value that it denotes.

*Example.* — The ‘_ refers to _’ operator is referentially transparent, despite the referential opacity of the quote operator:

‘London’ refers to the largest city of the United Kingdom.

Indeed, the first position is purely referential in the statement, though it is not in the quotation, because substituting *The capital of the United Kingdom* for *London* does not change the value of the statement. So in the first position, the ‘_ refers to _’ operator restores the relation between an expression and the value that it denotes. The second position is also purely referential for the same substitutivity reason.

### Definiteness

A formal language is *definite* is defined by all the occurrences of a variable within its scope denote the same value.

*Example.* — Mathematics is definite:

3

x

2

+ 2

x

+ 17

.

Indeed, the two occurrences of x denote the same value.

### Unfoldability

A formal language is *unfoldable* is defined by all expressions are β-reducible.

*Example.* — The lambda calculus is unfoldable:

((λ

x

.

x

+ 1) 3)

.

Indeed, ((λ*x*.*x* + 1) 3) = (*x* + 1)[3/*x*].

### Relations between the properties

Referential transparency, definiteness, and unfoldability are independent. Definiteness implies unfoldability only for deterministic languages. Non-deterministic languages cannot have definiteness and unfoldability at the same time.
