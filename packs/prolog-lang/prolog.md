---
title: "Prolog"
source: https://en.wikipedia.org/wiki/Prolog
domain: prolog-lang
license: CC-BY-SA-4.0
tags: prolog language, prolog lang, swi-prolog, logic programming
fetched: 2026-07-02
---

# Prolog

**Prolog** is a logic programming language that has its origins in artificial intelligence, automated theorem proving, and computational linguistics.

Prolog has its roots in first-order logic, a formal logic. Unlike many other programming languages, Prolog is intended primarily as a declarative programming language: the program is a set of facts and rules, which define relations. A computation is initiated by running a *query* over the program.

Prolog was one of the first logic programming languages and remains the most popular such language today, with several free and commercial implementations available. The language has been used for theorem proving, expert systems, term rewriting, type systems, automated planning, and question answering as well as its original intended field of use, natural language processing.

Prolog is a Turing-complete, general-purpose programming language, which is well-suited for intelligent knowledge-processing applications.

## History

| Year | Aix-Marseille | ISO/IEC Standard |
|---|---|---|
| 1972 | Prolog 0 | —N/a |
| 1973 | Prolog I | —N/a |
| 1982 | Prolog II | —N/a |
| 1990 | Prolog III | —N/a |
| 1995 | —N/a | 13211-1:1995 |
| 1996 | Prolog IV | —N/a |
| 2000 | —N/a | 13211-2:2000 |
| 2007 | —N/a | 13211-1:1995/Cor 1:2007 |
| 2012 | —N/a | 13211-1:1995/Cor 2:2012 |
| 2017 | —N/a | 13211-1:1995/Cor 3:2017 |
| 2025 | —N/a | 13211-3:2025 |

The name *Prolog* was chosen by Philippe Roussel, at the suggestion of his wife, as an abbreviation for ****Pro**grammation en **log**ique** (French for *Programming in logic*). It was created around 1972 by Alain Colmerauer with Philippe Roussel, from the *Artificial Intelligence Group* of the Faculty of Sciences of Luminy of Aix-Marseille II University of France. It was based on Robert Kowalski's procedural interpretation of Horn clauses, and it was motivated in part by the desire to reconcile the use of logic as a declarative knowledge representation language with the procedural representation of knowledge that was popular in North America in the late 1960s and early 1970s. According to Robert Kowalski, the first Prolog system was developed in 1972 by Colmerauer and Phillipe Roussel. The first implementation of Prolog was an interpreter written in Fortran by Gerard Battani and Henri Meloni. David H. D. Warren took this interpreter to the University of Edinburgh, and there implemented an alternative front-end, which came to define the "***Edinburgh Prolog***" syntax used by most modern implementations. Warren also implemented the first compiler for Prolog, creating the influential DEC-10 Prolog in collaboration with Fernando Pereira. Warren later generalised the ideas behind DEC-10 Prolog, to create the Warren Abstract Machine (**WAM**).

European AI researchers favored Prolog while Americans favored Lisp, reportedly causing many nationalistic debates on the merits of the languages. Much of the modern development of Prolog came from the impetus of the Fifth Generation Computer Systems project (FGCS), which developed a variant of Prolog named *Kernel Language* for its first operating system.

Pure Prolog was originally restricted to the use of a resolution theorem prover with Horn clauses of the form:

```
H :- B1, ..., Bn.
```

The application of the theorem-prover treats such clauses as procedures:

```
to show/solve H, show/solve B1 and ... and Bn.
```

Pure Prolog was soon extended, however, to include negation as failure, in which negative conditions of the form not(Bi) are shown by trying and failing to solve the corresponding positive conditions Bi.

Subsequent extensions of Prolog by the original team introduced constraint logic programming abilities into the implementations.

### Impact

Although Prolog is widely used in research and education, Prolog and other logic programming languages have not had a significant impact on the computer industry in general. Most applications are small by industrial standards, with few exceeding 100,000 lines of code. Programming in the large is considered to be complex because not all Prolog compilers support modules, and there are compatibility problems between the module systems of the major Prolog compilers. Portability of Prolog code across implementations has also been a problem, but developments since 2007 have meant: "the portability within the family of Edinburgh/Quintus derived Prolog implementations is good enough to allow for maintaining portable real-world applications."

Software developed in Prolog has been criticised for having a high performance penalty compared to conventional programming languages. In particular, Prolog's non-deterministic evaluation strategy can be problematic when programming deterministic computations, or when even using "don't care non-determinism" (where a single choice is made instead of backtracking over all possibilities). Cuts and other language constructs may have to be used to achieve desirable performance, destroying one of Prolog's main attractions, the ability to run programs "backwards and forwards".

Prolog is not purely declarative: because of constructs like the cut operator, a procedural reading of a Prolog program is needed to understand it. The order of clauses in a Prolog program is significant, as the execution strategy of the language depends on it. Other logic programming languages, such as Datalog, are truly declarative but restrict the language. As a result, many practical Prolog programs are written to conform to Prolog's depth-first search order, rather than as purely declarative logic programs.

### Use in industry

Prolog has been used in Watson. Watson uses IBM's DeepQA software and the Apache UIMA (Unstructured Information Management Architecture) framework. The system was written in various languages, including Java, C++, and Prolog, and runs on the SUSE Linux Enterprise Server 11 operating system using Apache Hadoop framework to provide distributed computing. Prolog is used for pattern matching over natural language parse trees. The developers have stated: "We required a language in which we could conveniently express pattern matching rules over the parse trees and other annotations (such as named entity recognition results), and a technology that could execute these rules very efficiently. We found that Prolog was the ideal choice for the language due to its simplicity and expressiveness." Prolog is being used in the Low-Code Development Platform GeneXus, which is focused around AI. Open source graph database TerminusDB is implemented in Prolog. TerminusDB is designed for collaboratively building and curating knowledge graphs.

## Syntax and semantics

In Prolog, program logic is expressed in terms of relations, and a computation is initiated by running a *query* over these relations. Relations and queries are constructed using Prolog's single data type, the *term*. Relations are defined by *clauses*. Given a query, the Prolog engine attempts to find a resolution refutation of the negated query. If the negated query can be refuted, i.e., an instantiation for all free variables is found that makes the union of clauses and the singleton set consisting of the negated query false, it follows that the original query, with the found instantiation applied, is a logical consequence of the program. This makes Prolog (and other logic programming languages) particularly useful for database, symbolic mathematics, and language parsing applications. Because Prolog allows impure predicates, checking the truth value of certain special predicates may have some deliberate side effect, such as printing a value to the screen. Because of this, the programmer is permitted to use some amount of conventional imperative programming when the logical paradigm is inconvenient. It has a purely logical subset, called "pure Prolog", as well as a number of extralogical features.

### Data types

Prolog's single data type is the *term*. Terms are either *atoms*, *numbers*, *variables* or *compound terms*.

- An **atom** is a symbol name starting with a lower case letter or guarded by quotes. Examples of atoms include `x`, `red`, `'Taco'`, `'some atom'`, and `'p(a)'`.
- **Numbers** can be floats or integers. Most of the major Prolog systems support arbitrary length integer numbers.
- **Variables** are denoted by a string consisting of letters, numbers and underscore characters, and beginning with an upper-case letter or underscore. Variables closely resemble variables in logic in that they are placeholders for arbitrary terms.
- A **compound term** is composed of an atom called a "functor" and a number of "arguments", which are again terms. Compound terms are ordinarily written as a functor followed by a comma-separated list of argument terms, which is contained in parentheses. The number of arguments is called the term's arity. An atom can be regarded as a compound term with arity zero. An example of a compound term is `person_friends(zelda,[tom,jim])`.

Special cases of compound terms:

- A *List* is an ordered collection of terms. It is denoted by square brackets with the terms separated by commas, or in the case of the empty list, by `[]`. For example, `[1,2,3,4]` or `[red,green,blue]`.
- *Strings*: A sequence of characters surrounded by quotes is equivalent to either a list of (numeric) character codes, a list of characters (atoms of length 1), or an atom depending on the value of the Prolog flag `double_quotes`. For example, `"to be, or not to be"`.

### Rules and facts

Prolog programs describe relations, defined by means of clauses. Pure Prolog is restricted to Horn clauses. Two types of Horn clauses are used to define Prolog programs: rules and facts. A rule is of the form

```mw
Head :- Body.
```

and is read as "Head is true if Body is true". A rule's body consists of calls to predicates, which are called the rule's **goals**. The built-in logical operator `,/2` (meaning an arity 2 operator with name `,`) denotes conjunction of goals, and `;/2` denotes disjunction. Conjunctions and disjunctions can only appear in the body, not in the head of a rule.

Clauses with empty bodies are called **facts**. An example of a fact is:

```mw
human(socrates).
```

which is equivalent to the rule:

```mw
human(socrates) :- true.
```

The built-in predicate `true/0` is always true.

Given the above fact, one can ask:

*is socrates a human?*

```mw
 ?- human(socrates).
 Yes
```

*what things are humans?*

```mw
 ?- human(X).
 X = socrates
```

Clauses with bodies are called **rules**. An example of a rule is:

```mw
mortal(X) :- human(X).
```

If we add that rule and ask *what things are mortals?*

```mw
 ?- mortal(X).
 X = socrates
```

### Predicates and programs

A *predicate* (or *procedure definition*) is a collection of clauses whose heads have the same name and arity. We use the notation *name/arity* to refer to predicates. A *logic program* is a set of predicates. For example, the following Prolog program, which defines some family relations, has four predicates:

```mw
mother_child(trude, sally).

father_child(tom, sally).
father_child(tom, erica).
father_child(mike, tom).

sibling(X, Y)      :- parent_child(Z, X), parent_child(Z, Y), not(X = Y).

parent_child(X, Y) :- father_child(X, Y).
parent_child(X, Y) :- mother_child(X, Y).
```

Predicate `father_child/2` has three clauses, all of which are facts, and predicate `parent_child/2` has two clauses, both are rules.

Due to the relational nature of many built-in predicates, they can typically be used in several directions. For example, `length/2` can be used to determine the length of a list (`length(List, L)`, given a list `List`), and to generate a list skeleton of a given length (`length(X, 5)`), and to generate both list skeletons and their lengths together (`length(X, L)`). Similarly, `append/3` can be used both to append two lists (`append(ListA, ListB, X)` given lists `ListA` and `ListB`), and to split a given list into parts (`append(X, Y, List)`, given a list `List`). For this reason, a comparatively small set of library predicates suffices for many Prolog programs.

As a general purpose language, Prolog also provides various built-in predicates to perform routine activities like input/output, using graphics and otherwise communicating with the operating system. These predicates are not given a relational meaning and are only useful for the side-effects they exhibit on the system. For example, the predicate `write/1` displays a term on the screen.

### Loops and recursion

Iterative algorithms can be implemented by means of recursive predicates.

Consider the `parent_child/2` predicate defined in the family relation program above. The following Prolog program defines the *ancestor* relation:

```mw
ancestor(X, Y) :- parent_child(X, Y).
ancestor(X, Y) :- parent_child(X, Z), ancestor(Z, Y).
```

It expresses that X is an ancestor of Y if X is parent of Y or X is parent of an ancestor of Y. It is recursive because it is defined in terms of itself (there is a call to predicate `ancestor/2` in the body of the second clause).

### Execution

Execution of a Prolog program is initiated by the user's posting of a single goal, called the query. Logically, the Prolog engine tries to find a resolution refutation of the negated query. The resolution method used by Prolog is called SLD resolution. If the negated query can be refuted, it follows that the query, with the appropriate variable bindings in place, is a logical consequence of the program. In that case, all generated variable bindings are reported to the user, and the query is said to have succeeded. Operationally, Prolog's execution strategy can be thought of as a generalization of function calls in other languages, one difference being that multiple clause heads can match a given call. In that case, the system creates a choice-point, unifies the goal with the clause head of the first alternative, and continues with the goals of that first alternative. If any goal fails in the course of executing the program, all variable bindings that were made since the most recent choice-point was created are undone, and execution continues with the next alternative of that choice-point. This execution strategy is called chronological backtracking. For example, given the family relation program defined above, the following query will be evaluated to true:

```mw
 ?- sibling(sally, erica).
 Yes
```

This is obtained as follows: Initially, the only matching clause-head for the query `sibling(sally, erica)` is the first one, so proving the query is equivalent to proving the body of that clause with the appropriate variable bindings in place, i.e., the conjunction `(parent_child(Z, sally), parent_child(Z, erica))`. The next goal to be proved is the leftmost one of this conjunction, i.e., `parent_child(Z, sally)`. Two clause heads match this goal. The system creates a choice-point and tries the first alternative, whose body is `father_child(Z, sally)`. This goal can be proved using the fact `father_child(tom, sally)`, so the binding `Z = tom` is generated, and the next goal to be proved is the second part of the above conjunction: `parent_child(tom, erica)`. Again, this can be proved by the corresponding fact. Since all goals could be proved, the query succeeds. Since the query contained no variables, no bindings are reported to the user. A query with variables, like:

```mw
?- father_child(Father, Child).
```

enumerates all valid answers on backtracking.

Notice that with the code as stated above, the query `?- sibling(sally, sally).` also succeeds. One would insert additional goals to describe the relevant restrictions, if desired.

### Negation

The built-in Prolog predicate `\+/1` provides negation as failure, which allows for non-monotonic reasoning. The goal `\+ illegal(X)` in the rule

```mw
legal(X) :- \+ illegal(X).
```

is evaluated as follows: Prolog attempts to prove `illegal(X)`. If a proof for that goal can be found, the original goal (i.e., `\+ illegal(X)`) fails. If no proof can be found, the original goal succeeds. Therefore, the `\+/1` prefix operator is called the "not provable" operator, since the query `?- \+ Goal.` succeeds if Goal is not provable. This kind of negation is sound if its argument is "ground" (i.e. contains no variables). Soundness is lost if the argument contains variables and the proof procedure is complete. In particular, the query `?- legal(X).` now cannot be used to enumerate all things that are legal.

## Programming in Prolog

In Prolog, loading code is referred to as *consulting*. Prolog can be used interactively by entering queries at the Prolog prompt `?-`. If there is no solution, Prolog writes `no`. If a solution exists then it is printed. If there are multiple solutions to the query, then these can be requested by entering a semi-colon `;`. There are guidelines on good programming practice to improve code efficiency, readability and maintainability.

Here follow some example programs written in Prolog.

### Hello World

Example of a basic query in a couple of popular Prolog dialects:

| SWI-Prolog | GNU Prolog |
|---|---|
| ?- write('Hello World!'), nl. Hello World! true. ?- | \| ?- write('Hello World!'), nl. Hello World! yes \| ?- |

This comparison shows the prompt ("?-" vs "| ?-") and resolution status ("true". vs "yes", "false". vs "no") can differ from one Prolog implementation to another.

### Compiler optimization

Any computation can be expressed declaratively as a sequence of state transitions. As an example, an optimizing compiler with three optimization passes could be implemented as a relation between an initial program and its optimized form:

```mw
program_optimized(Prog0, Prog) :-
    optimization_pass_1(Prog0, Prog1),
    optimization_pass_2(Prog1, Prog2),
    optimization_pass_3(Prog2, Prog).
```

or equivalently using DCG notation:

```mw
program_optimized --> optimization_pass_1, optimization_pass_2, optimization_pass_3.
```

### Quicksort

The quicksort sorting algorithm, relating a list to its sorted version:

```mw
partition([], _, [], []).
partition([X|Xs], Pivot, Smalls, Bigs) :-
    (   X @< Pivot ->
        Smalls = [X|Rest],
        partition(Xs, Pivot, Rest, Bigs)
    ;   Bigs = [X|Rest],
        partition(Xs, Pivot, Smalls, Rest)
    ).

quicksort([])     --> [].
quicksort([X|Xs]) -->
    { partition(Xs, X, Smaller, Bigger) },
    quicksort(Smaller), [X], quicksort(Bigger).
```

## Design patterns of Prolog

A design pattern is a general reusable solution to a commonly occurring problem in software design. Some design patterns in Prolog are skeletons, techniques, cliches, program schemata, logic description schemata, and higher-order programming.

## Higher-order programming

A higher-order predicate is a predicate that takes one or more other predicates as arguments. Although support for higher-order programming takes Prolog outside the domain of first-order logic, which does not allow quantification over predicates, ISO Prolog now has some built-in higher-order predicates such as `call/1`, `call/2`, `call/3`, `findall/3`, `setof/3`, and `bagof/3`. Furthermore, since arbitrary Prolog goals can be constructed and evaluated at run-time, it is easy to write higher-order predicates like `maplist/2`, which applies an arbitrary predicate to each member of a given list, and `sublist/3`, which filters elements that satisfy a given predicate, also allowing for currying.

To convert solutions from temporal representation (answer substitutions on backtracking) to spatial representation (terms), Prolog has various all-solutions predicates that collect all answer substitutions of a given query in a list. This can be used for list comprehension. For example, perfect numbers equal the sum of their proper divisors:

```mw
 perfect(N) :-
     between(1, inf, N), U is N // 2,
     findall(D, (between(1,U,D), N mod D =:= 0), Ds),
     sumlist(Ds, N).
```

This can be used to enumerate perfect numbers, and to check if a number is perfect.

As another example, the predicate `maplist` applies a predicate `P` to all corresponding positions in a pair of lists:

```mw
maplist(_, [], []).
maplist(P, [X|Xs], [Y|Ys]) :-
   call(P, X, Y),
   maplist(P, Xs, Ys).
```

When `P` is a predicate that for all `X`, `P(X,Y)` unifies `Y` with a single unique value, `maplist(P, Xs, Ys)` is equivalent to applying the map function in functional programming as `Ys = map(Function, Xs)`.

Higher-order programming style in Prolog was pioneered in HiLog and λProlog.

## Modules

For programming in the large, Prolog provides a module system, which is in the ISO Standard. However, while most Prolog systems support structuring the code into modules, virtually no implementation adheres to the modules part of the ISO standard. Instead, most Prolog systems have decided to support as *de-facto* module standard the Quintus/SICStus module system. However, further convenience predicates concerning modules are provided by some implementations only and often have subtle differences in their semantics.

Some systems chose to implement module concepts as source-to-source compilation into base ISO Prolog, as is the case of Logtalk. GNU Prolog initially diverted from ISO modules, opting instead for Contextual Logic Programming, in which unit (module) loading and unloading can be made dynamically. Ciao designed a strict module system that, while being basically compatible with the *de-facto* standard used by other Prolog systems, is amenable to precise static analysis, supports term hiding, and facilitates programming in the large. XSB takes a different approach and offers an *atom-based* module system. The latter two Prolog systems allow controlling the *visibility of terms* in addition to that of predicates.

## Parsing

There is a special notation called definite clause grammars. A rule defined via `-->/2` instead of `:-/2` is expanded by the preprocessor (`expand_term/2`, a facility analogous to macros in other languages) according to a few straightforward rewriting rules, resulting in ordinary Prolog clauses. Most notably, the rewriting equips the predicate with two additional arguments, which can be used to implicitly thread state around, analogous to monads in other languages. Definite clause grammars are often used to write parsers or list generators, as they also provide a convenient interface to difference lists.

## Meta-interpreters and reflection

Prolog is a homoiconic language and provides many facilities for reflective programming (reflection). Its implicit execution strategy makes it possible to write a concise meta-circular evaluator (also called *meta-interpreter*) for pure Prolog code:

```mw
solve(true).
solve((Subgoal1,Subgoal2)) :-
    solve(Subgoal1),
    solve(Subgoal2).
solve(Head) :-
    clause(Head, Body),
    solve(Body).
```

where `true` represents an empty conjunction, and `clause(Head, Body)` unifies with clauses in the database of the form `Head :- Body`.

Since Prolog programs are themselves sequences of Prolog terms (`:-/2` is an infix operator) that are easily read and inspected using built-in mechanisms (like `read/1`), it is possible to write customized interpreters that augment Prolog with domain-specific features. For example, Sterling and Shapiro present a meta-interpreter that performs reasoning with uncertainty, reproduced here with slight modifications:

```mw
solve(true, 1) :- !.
solve((Subgoal1,Subgoal2), Certainty) :-
    !,
    solve(Subgoal1, Certainty1),
    solve(Subgoal2, Certainty2),
    Certainty is min(Certainty1, Certainty2).
solve(Goal, 1) :-
    builtin(Goal), !,
    Goal.
solve(Head, Certainty) :-
    clause_cf(Head, Body, Certainty1),
    solve(Body, Certainty2),
    Certainty is Certainty1 * Certainty2.
```

This interpreter uses a table of built-in Prolog predicates of the form

```mw
builtin(A is B).
builtin(read(X)).
% etc.
```

and clauses represented as `clause_cf(Head, Body, Certainty)`. Given those, it can be called as `solve(Goal, Certainty)` to execute `Goal` and obtain a measure of certainty about the result.

## Turing completeness

Pure Prolog is based on a subset of first-order predicate logic, Horn clauses, which is Turing-complete. Turing completeness of Prolog can be shown by using it to simulate a Turing machine:

```mw
turing(Tape0, Tape) :-
    perform(q0, [], Ls, Tape0, Rs),
    reverse(Ls, Ls1),
    append(Ls1, Rs, Tape).

perform(qf, Ls, Ls, Rs, Rs) :- !.
perform(Q0, Ls0, Ls, Rs0, Rs) :-
    symbol(Rs0, Sym, RsRest),
    once(rule(Q0, Sym, Q1, NewSym, Action)),
    action(Action, Ls0, Ls1, [NewSym|RsRest], Rs1),
    perform(Q1, Ls1, Ls, Rs1, Rs).

symbol([], b, []).
symbol([Sym|Rs], Sym, Rs).

action(left, Ls0, Ls, Rs0, Rs) :- left(Ls0, Ls, Rs0, Rs).
action(stay, Ls, Ls, Rs, Rs).
action(right, Ls0, [Sym|Ls0], [Sym|Rs], Rs).

left([], [], Rs0, [b|Rs0]).
left([L|Ls], Ls, Rs, [L|Rs]).
```

A simple example Turing machine is specified by the facts:

```mw
rule(q0, 1, q0, 1, right).
rule(q0, b, qf, 1, stay).
```

This machine performs incrementation by one of a number in unary encoding: It loops over any number of "1" cells and appends an additional "1" at the end. Example query and result:

```mw
?- turing([1,1,1], Ts).
Ts = [1, 1, 1, 1] ;
```

This illustrates how any computation can be expressed declaratively as a sequence of state transitions, implemented in Prolog as a relation between successive states of interest.

## Implementation

### ISO Prolog

The International Organization for Standardization (ISO) Prolog technical standard consists of two parts. ISO/IEC 13211-1, published in 1995, aims to standardize the existing practices of the many implementations of the core elements of Prolog. It has clarified aspects of the language that were previously ambiguous and leads to portable programs. There are three corrigenda: Cor.1:2007, Cor.2:2012, and Cor.3:2017. ISO/IEC 13211-2, published in 2000, adds support for modules to the standard. The standard is maintained by the ISO/IEC JTC1/SC22/WG17 working group. ANSI X3J17 is the US Technical Advisory Group for the standard.

### Compilation

For efficiency, Prolog code is typically compiled to abstract machine code, often influenced by the register-based Warren Abstract Machine instruction set. Some implementations employ abstract interpretation to derive type and mode information of predicates at compile time, or compile to real machine code for high performance. Devising efficient implementation methods for Prolog code is a field of active research in the logic programming community, and various other execution methods are employed in some implementations. These include clause binarization and stack-based virtual machines.

### Tail recursion

Prolog systems typically implement a well-known optimization method called tail call optimization for deterministic predicates exhibiting tail recursion or, more generally, tail calls: A clause's stack frame is discarded before performing a call in a tail position. Therefore, deterministic tail-recursive predicates are executed with constant stack space, like loops in other languages.

### Term indexing

Finding clauses that are unifiable with a term in a query is linear in the number of clauses. Term indexing uses a data structure that enables sub-linear-time lookups. Indexing only affects program performance, it does not affect semantics. Most Prologs only use indexing on the first term, as indexing on all terms is expensive, but techniques based on *field-encoded words* or *superimposed codewords* provide fast indexing across the full query and head.

### Hashing

Some Prolog systems, such as WIN-PROLOG and SWI-Prolog, now implement hashing to help handle large datasets more efficiently. This tends to yield very large performance gains when working with large corpora such as WordNet.

### Tabling

Some Prolog systems, (B-Prolog, XSB, SWI-Prolog, YAP, and Ciao), implement a memoization method called *tabling*, which frees the user from manually storing intermediate results. Tabling is a space–time tradeoff; execution time can be reduced by using more memory to store intermediate results:

> Subgoals encountered in a query evaluation are maintained in a table, along with answers to these subgoals. If a subgoal is re-encountered, the evaluation reuses information from the table rather than re-performing resolution against program clauses.

Tabling can be extended in various directions. It can support recursive predicates through **SLG resolution** or linear tabling. In a multi-threaded Prolog system tabling results could be kept private to a thread or shared among all threads. And in incremental tabling, tabling might react to changes.

### Implementation in hardware

During the Fifth Generation Computer Systems project, there were attempts to implement Prolog in hardware with the aim of achieving faster execution with dedicated architectures. Furthermore, Prolog has a number of properties that may allow speed-up through parallel execution. A more recent approach has been to compile restricted Prolog programs to a field-programmable gate array. However, rapid progress in general-purpose hardware has consistently overtaken more specialised architectures.

In 1982, computers operated at around 10,000 to 100,000 logical inferences per second (LIPS). The FGCS planned to produce computers operating at 0.1 to 1 GLIPS. The Institute for New Generation Computer Technology documents estimated that 1 LIP took about 100 operations on a conventional computer. The plan was to produce at the end of the project (in 1992) a machine with 1000 processors achieving 1 GLIPS, implying at least 1 MLIPS per processor.

Sega implemented Prolog for use with the Sega AI Computer, released for the Japanese market in 1986. Prolog was used for reading natural language inputs, in the Japanese language, via a touch pad.

## Extensions

Various implementations have been developed from Prolog to extend logic programming abilities in many directions. These include types, modes, constraint logic programming (CLP), object-oriented logic programming, concurrency, linear logic, functional and higher-order logic programming abilities, plus interoperability with knowledge bases:

### Types

Prolog is an untyped language. Attempts to introduce and extend Prolog with types began in the 1980s, and continue as of 2008. Type information is useful not only for type safety but also for reasoning about Prolog programs.

### Modes

| Mode specifier | Interpretation |
|---|---|
| `+` | `nonvar` on entry |
| `-` | `var` on entry |
| `?` | Not specified |

The syntax of Prolog does not specify which arguments of a predicate are inputs and which are outputs. However, this information is significant and it is recommended that it be included in the comments. Modes provide valuable information when reasoning about Prolog programs and can also be used to accelerate execution.

### Constraints

Constraint logic programming extends Prolog to include concepts from constraint satisfaction. A constraint logic program allows constraints in the body of clauses, such as: `A(X,Y) :- X+Y>0.` It is suited to large-scale combinatorial optimisation problems and is thus useful for applications in industrial settings, such as automated time-tabling and production scheduling. Most Prolog systems ship with at least one constraint solver for finite domains, and often also with solvers for other domains like rational numbers.

### Object-orientation

Flora-2 is an object-oriented knowledge representation and reasoning system based on F-logic and incorporates HiLog, transaction logic, and defeasible reasoning.

Logtalk is an object-oriented logic programming language that can use most Prolog implementations as a back-end compiler. As a multi-paradigm language, it includes support for both prototypes and classes.

Oblog is a small, portable, object-oriented extension to Prolog by Margaret McDougall of EdCAAD, University of Edinburgh.

Objlog was a frame-based language combining objects and Prolog II from CNRS, Marseille, France.

Prolog++ was developed by Logic Programming Associates and first released in 1989 for MS-DOS PCs. Support for other platforms was added, and a second version was released in 1995. A book about Prolog++ by Chris Moss was published by Addison-Wesley in 1994.

Visual Prolog is a multi-paradigm language with interfaces, classes, implementations and object expressions.

### Graphics

Prolog systems that provide a graphics library are SWI-Prolog, Visual Prolog, WIN-PROLOG, and B-Prolog.

### Concurrency

Prolog-MPI is an open-source SWI-Prolog extension for distributed computing over the Message Passing Interface. Also there are various concurrent Prolog programming languages.

### Web programming

Some Prolog implementations, notably Visual Prolog, SWI-Prolog and Ciao, support server-side web programming with support for web protocols, HTML and XML. There are also extensions to support semantic web formats such as Resource Description Framework and Web Ontology Language. Prolog has also been suggested as a client-side language. In addition, Visual Prolog supports JSON-RPC and Websockets.

### Other

- F-logic extends Prolog with frames/objects for knowledge representation.
- Transaction logic extends Prolog with a logical theory of state-changing update operators. It has both a model-theoretic and procedural semantics.
- OW Prolog has been created in order to answer Prolog's lack of graphics and interface.

## Interfaces to other languages

Frameworks exist which can bridge between Prolog and other languages:

- The LPA Intelligence Server allows embedding LPA Prolog for Windows in other programming languages, including: C, C++, C#, Java, Visual Basic, Delphi, .NET, Lua, Python, and others. It exploits the dedicated string data type which LPA Prolog provides
- The Logic Server Application Programming Interface (API) allows both the extension and embedding of Prolog in C, C++, Java, Visual Basic, Delphi, .NET, and any language or environment which can call a .dll or .so. It is implemented for Amzi! Prolog + Logic Server but the API specification can be made available for any implementation.
- JPL is a bi-directional Java Prolog bridge which ships with SWI-Prolog by default, allowing Java and Prolog to call each other (recursively). It is known to have good concurrency support and is under active development.
- InterProlog, a programming library bridge between Java and Prolog, implementing bi-directional predicate/method calling between both languages. Java objects can be mapped into Prolog terms and vice versa. Allows the development of graphical user interfaces and other functions in Java while leaving logic processing in the Prolog layer. Supports XSB and SWI-Prolog.
- Prova provides native syntax integration with Java, agent messaging and reaction rules. Prova positions itself as a rule-based scripting (RBS) system for middleware. The language breaks new ground in combining imperative and declarative programming.
- PROL An embeddable Prolog engine for Java. It includes a small IDE and a few libraries.
- GNU Prolog for Java is an implementation of ISO Prolog as a Java library (gnu.prolog)
- Ciao provides interfaces to C, C++, Java, and relational databases.
- C#-Prolog is a Prolog interpreter written in (managed) C#. Can easily be integrated in C# programs. Characteristics: reliable and fairly fast interpreter, command line interface, Windows-interface, builtin DCG, XML-predicates, SQL-predicates, extendible. The complete source code is available, including a parser generator that can be used for adding special purpose extensions.
- tuProlog is a lightweight Prolog system for distributed applications and infrastructures, intentionally designed around a minimal core, to be either statically or dynamically configured by loading/unloading libraries of predicates. tuProlog natively supports multi-paradigm programming, providing a clean, seamless integration model between Prolog and mainstream object-oriented languages, namely Java, for tuProlog Java version, and any .NET-based language (C#, F#..), for tuProlog .NET version.
- Janus is a bi-directional interface between Prolog and Python using portable low-level primitives. It was initially developed for XSB by Anderson and Swift, but has been adopted as a joint initiative by the XSB, Ciao and SWI-Prolog teams.
