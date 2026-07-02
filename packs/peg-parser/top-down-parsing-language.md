---
title: "Top-down parsing language"
source: https://en.wikipedia.org/wiki/Top-down_parsing_language
domain: peg-parser
license: CC-BY-SA-4.0
tags: parsing expression grammar, peg parser, packrat parsing, top-down parsing
fetched: 2026-07-02
---

# Top-down parsing language

**Top-Down Parsing Language** (**TDPL**) is a type of analytic formal grammar developed by Alexander Birman in the early 1970s in order to study formally the behavior of a common class of practical top-down parsers that support a limited form of backtracking. Birman originally named his formalism *the TMG Schema* (TS), after TMG, an early parser generator, but it was later given the name TDPL by Aho and Ullman in their classic anthology *The Theory of Parsing, Translation and Compiling*.

## Definition of a TDPL grammar

Formally, a **TDPL grammar** *G* is a quadruple consisting of the following components:

- A finite set *N* of *nonterminal symbols*.
- A finite set Σ of *terminal symbols* that is disjoint from *N*.
- A finite set *P* of *production rules*, where a rule has one of the following forms:
  - *A* → ε, where *A* is a nonterminal and ε is the empty string.
  - *A* → *f*, where *f* is a distinguished symbol representing *unconditional failure*.
  - *A* → *a*, where *a* is any terminal symbol.
  - *A* → *BC/D*, where *B*, *C*, and *D* are nonterminals.

### Interpretation of a grammar

A TDPL grammar can be viewed as an extremely minimalistic formal representation of a recursive descent parser, in which each of the nonterminals schematically represents a parsing function. Each of these nonterminal-functions takes as its input argument a string to be recognized, and yields one of two possible outcomes:

- *success*, in which case the function may optionally move forward or *consume* one or more characters of the input string supplied to it, or
- *failure*, in which case no input is consumed.

Note that a nonterminal-function may succeed without actually consuming any input, and this is considered an outcome distinct from failure.

A nonterminal *A* defined by a rule of the form *A* → ε always succeeds without consuming any input, regardless of the input string provided. Conversely, a rule of the form *A* → *f* always fails regardless of input. A rule of the form *A* → *a* succeeds if the next character in the input string is the terminal *a*, in which case the nonterminal succeeds and consumes that one terminal; if the next input character does not match (or there is no next character), then the nonterminal fails.

A nonterminal *A* defined by a rule of the form *A* → *BC/D* first recursively invokes nonterminal *B*, and if *B* succeeds, invokes *C* on the remainder of the input string left unconsumed by *B*. If both *B* and *C* succeed, then *A* in turn succeeds and consumes the same total number of input characters that *B* and *C* together did. If either *B* or *C* fails, however, then *A* backtracks to the original point in the input string where it was first invoked, and then invokes *D* on that original input string, returning whatever result *D* produces.

### Examples

The following TDPL grammar describes the regular language consisting of an arbitrary-length sequence of a's and b's:

S

→

AS/T

T

→

BS/E

A

→ a

B

→ b

E

→ ε

The following grammar describes the context-free Dyck language consisting of arbitrary-length strings of matched braces, such as '{}', '{{}{{}}}', etc.:

S

→

OT/E

T

→

SU/F

U

→

CS/F

O

→ {

C

→ }

E

→ ε

F

→

f

The above examples can be represented equivalently but much more succinctly in parsing expression grammar notation as `S ← (a/b)*` and `S ← ({S})*`, respectively.

## Generalized TDPL

A slight variation of TDPL, known as **Generalized TDPL** or GTDPL, greatly increases the apparent expressiveness of TDPL while retaining the same minimalist approach (though they are actually equivalent). In GTDPL, instead of TDPL's recursive rule form *A* → *BC/D*, the rule form *A* → *B[C,D]* is used. This rule is interpreted as follows: When nonterminal *A* is invoked on some input string, it first recursively invokes *B*. If *B* succeeds, then *A* subsequently invokes *C* on the remainder of the input left unconsumed by *B*, and returns the result of *C* to the original caller. If *B* fails, on the other hand, then *A* invokes *D* on the original input string, and passes the result back to the caller.

The important difference between this rule form and the *A* → *BC/D* rule form used in TDPL is that *C* and *D* are never *both* invoked in the same call to *A*: that is, the GTDPL rule acts more like a "pure" if/then/else construct using *B* as the condition.

In GTDPL it is straightforward to express interesting non-context-free languages such as the classic example {a*n*b*n*c*n*}.

A GTDPL grammar can be reduced to an equivalent TDPL grammar that recognizes the same language, although the process is not straightforward and may greatly increase the number of rules required. Also, both TDPL and GTDPL can be viewed as very restricted forms of parsing expression grammars, all of which represent the same class of grammars.
