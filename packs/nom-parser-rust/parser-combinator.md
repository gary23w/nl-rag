---
title: "Parser combinator"
source: https://en.wikipedia.org/wiki/Parser_combinator
domain: nom-parser-rust
license: CC-BY-SA-4.0
tags: nom parser, rust parser combinator, byte parsing rust, nom combinator library
fetched: 2026-07-02
---

# Parser combinator

In computer programming, a **parser combinator** is a higher-order function that accepts several parsers as input and returns a new parser as its output. In this context, a parser is a function accepting strings as input and returning some structure as output, typically a parse tree or a set of indices representing locations in the string where parsing stopped successfully. Parser combinators enable a recursive descent parsing strategy that facilitates modular piecewise construction and testing. This parsing technique is called **combinatory parsing**.

Parsers using combinators have been used extensively in the prototyping of compilers and processors for domain-specific languages such as natural-language user interfaces to databases, where complex and varied semantic actions are closely integrated with syntactic processing. In 1989, Richard Frost and John Launchbury demonstrated use of parser combinators to construct natural-language interpreters. Graham Hutton also used higher-order functions for basic parsing in 1992 and monadic parsing in 1996. S. D. Swierstra also exhibited the practical aspects of parser combinators in 2001. In 2008, Frost, Hafiz and Callaghan described a set of parser combinators in the functional programming language Haskell that solve the long-standing problem of accommodating left recursion, and work as a complete top-down parsing tool in polynomial time and space.

## Basic idea

In any programming language that has first-class functions, parser combinators can be used to combine basic parsers to construct parsers for more complex rules. For example, a production rule of a context-free grammar (CFG) may have one or more alternatives and each alternative may consist of a sequence of non-terminal(s) and/or terminal(s), or the alternative may consist of a single non-terminal or terminal or the empty string. If a simple parser is available for each of these alternatives, a parser combinator can be used to combine each of these parsers, returning a new parser which can recognise any or all of the alternatives.

In languages that support operator overloading, a parser combinator can take the form of an infix operator, used to glue different parsers to form a complete rule. Parser combinators thereby enable parsers to be defined in an embedded style, in code which is similar in structure to the rules of the formal grammar. As such, implementations can be thought of as executable specifications with all the associated advantages such as readability.

## The combinators

To keep the discussion relatively straightforward, we discuss parser combinators in terms of *recognizers* only. If the input string is of length `#input` and its members are accessed through an index `j`, a recognizer is a parser which returns, as output, a set of indices representing indices at which the parser successfully finished recognizing a sequence of tokens that begin at index `j`. An empty result set indicates that the recognizer failed to recognize any sequence beginning at index `j`.

- The `empty` recognizer recognizes the empty string. This parser always succeeds, returning a singleton set containing the input index:

$empty(j)=\{j\}$

- A recognizer `term ***x***` recognizes the terminal `x`. If the token at index `j` in the input string is `x`, this parser returns a singleton set containing `j + 1`; otherwise, it returns the empty set.

$term(x,j)={\begin{cases}\left\{\right\},&j\geq \#input\\\left\{j+1\right\},&j^{th}{\mbox{ element of }}input=x\\\left\{\right\},&{\mbox{otherwise}}\end{cases}}$

Given two recognizers `p` and `q`, we can define two major parser combinators, one for matching alternative rules and one for sequencing rules:

- The ‘alternative’ parser combinator, ⊕, applies each of the recognizers on the same index `j` and returns the union of the finishing indices of the recognizers:

$(p\oplus q)(j)=p(j)\cup q(j)$

- The 'sequence' combinator, ⊛, applies the first recognizer `p` to the input index `j`, and for each finishing index applies the second recognizer `q` with that as a starting index. It returns the union of the finishing indices returned from all invocations of `q`:

$(p\circledast q)(j)=\bigcup \{q(k):k\in p(j)\}$

There may be multiple distinct ways to parse a string while finishing at the same index, indicating an ambiguous grammar. Simple recognizers do not acknowledge these ambiguities; each possible finishing index is listed only once in the result set. For a more complete set of results, a more complicated object such as a parse tree must be returned.

## Examples

Consider a highly ambiguous context-free grammar, `s ::= ‘x’ s s | ε`. Using the combinators defined earlier, we can modularly define executable notations of this grammar in a modern functional programming language (e.g., Haskell) as `s = term ‘x’ <*> s <*> s <+> empty`. When the recognizer `s` is applied at index `2` of the input sequence `x x x x x` it would return a result set `{2,3,4,5}`, indicating that there were matches starting at index 2 and finishing at any index between 2 and 5 inclusive.

## Shortcomings and solutions

Parser combinators, like all recursive descent parsers, are not limited to the context-free grammars and thus do no global search for ambiguities in the LL(*k*) parsing Firstk and Followk sets. Thus, ambiguities are not known until run-time if and until the input triggers them. In such cases, the recursive descent parser may default (perhaps unknown to the grammar designer) to one of the possible ambiguous paths, resulting in semantic confusion (aliasing) in the use of the language. This leads to bugs by users of ambiguous programming languages, which are not reported at compile-time, and which are introduced not by human error, but by ambiguous grammar. The only solution that eliminates these bugs is to remove the ambiguities and use a context-free grammar.

The simple implementations of parser combinators have some shortcomings, which are common in top-down parsing. Naïve combinatory parsing requires exponential time and space when parsing an ambiguous context-free grammar. In 1996, Frost and Szydlowski demonstrated how memoization can be used with parser combinators to reduce the time complexity to polynomial. Later Frost used monads to construct the combinators for systematic and correct threading of memo-table throughout the computation.

Like any top-down recursive descent parsing, the conventional parser combinators (like the combinators described above) will not terminate while processing a left-recursive grammar (e.g. `s ::= s <*> term ‘x’|empty`). A recognition algorithm that accommodates ambiguous grammars with direct left-recursive rules is described by Frost and Hafiz in 2006. The algorithm curtails the otherwise ever-growing left-recursive parse by imposing depth restrictions. That algorithm was extended to a complete parsing algorithm to accommodate indirect as well as direct left-recursion in polynomial time, and to generate compact polynomial-size representations of the potentially exponential number of parse trees for highly ambiguous grammars by Frost, Hafiz and Callaghan in 2007. This extended algorithm accommodates indirect left recursion by comparing its ‘computed context’ with ‘current context’. The same authors also described their implementation of a set of parser combinators written in the Haskell language based on the same algorithm.
