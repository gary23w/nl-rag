---
title: "Datalog"
source: https://en.wikipedia.org/wiki/Datalog
domain: datomic
license: CC-BY-SA-4.0
tags: datomic database, immutable database, datalog query, temporal database
fetched: 2026-07-02
---

# Datalog

**Datalog** is a declarative logic programming language. While it is syntactically a subset of Prolog, Datalog generally uses a bottom-up rather than top-down evaluation model. This difference yields significantly different behavior and properties from Prolog. It is often used as a query language for deductive databases. Datalog has been applied to problems in data integration, networking, program analysis, and more.

## Example

A Datalog program consists of *facts*, which are statements that are held to be true, and *rules*, which say how to deduce new facts from known facts. For example, here are two facts that mean *xerces is a parent of brooke* and *brooke is a parent of damocles*:

```mw
parent(xerces, brooke).
parent(brooke, damocles).
```

The names are written in lowercase because strings beginning with an uppercase letter stand for variables. Here are two rules:

```mw
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
```

The `:-` symbol is read as "if", and the comma is read "and", so these rules mean:

- *X is an ancestor of Y if X is a parent of Y.*
- *X is an ancestor of Y if X is a parent of some Z, and Z is an ancestor of Y.*

The meaning of a program is defined to be the set of all of the facts that can be deduced using the initial facts and the rules. This program's meaning is given by the following facts:

```mw
parent(xerces, brooke).
parent(brooke, damocles).
ancestor(xerces, brooke).
ancestor(brooke, damocles).
ancestor(xerces, damocles).
```

Some Datalog implementations don't deduce all possible facts, but instead answer *queries*:

```mw
?- ancestor(xerces, X).
```

This query asks: *Who are all the X that xerces is an ancestor of?* For this example, it would return *brooke* and *damocles*.

## Comparison to relational databases

The non-recursive subset of Datalog is closely related to query languages for relational databases, such as SQL. The following table maps between Datalog, relational algebra, and SQL concepts:

| Datalog | Relational algebra | SQL |
|---|---|---|
| Relation | Relation | Table |
| Fact | Tuple | Row |
| Rule | —N/a | Materialized view |
| Query | Select | Query |

More formally, non-recursive Datalog corresponds precisely to unions of conjunctive queries, or equivalently, negation-free relational algebra.

| Schematic translation from non-recursive Datalog into SQL |
|---|
| s(x, y). t(y). r(A, B) :- s(A, B), t(B). CREATE TABLE s ( z0 TEXT NONNULL, z1 TEXT NONNULL, PRIMARY KEY (z0, z1) ); CREATE TABLE t ( z0 TEXT NONNULL PRIMARY KEY ); INSERT INTO s VALUES ('x', 'y'); INSERT INTO t VALUES ('y'); CREATE VIEW r AS SELECT s.z0, s.z1 FROM s, t WHERE s.z1 = t.z0; |

## Syntax

A Datalog program consists of a list of *rules* (Horn clauses). If *constant* and *variable* are two countable sets of constants and variables respectively and *relation* is a countable set of predicate symbols, then the following BNF grammar expresses the structure of a Datalog program:

```mw
<program> ::= <rule> <program> | ""
<rule> ::= <atom> ":-" <atom-list> "."
<atom> ::= <relation> "(" <term-list> ")"
<atom-list> ::= <atom> | <atom> "," <atom-list> | ""
<term> ::= <constant> | <variable>
<term-list> ::= <term> | <term> "," <term-list> | ""
```

Atoms are also referred to as **literals**. The atom to the left of the `:-` symbol is called the **head** of the rule; the atoms to the right are the **body**. Every Datalog program must satisfy the condition that every variable that appears in the head of a rule also appears in the body (this condition is sometimes called the **range restriction**).

There are two common conventions for variable names: capitalizing variables, or prefixing them with a question mark `?`.

Note that under this definition, Datalog does *not* include negation nor aggregates; see § Extensions for more information about those constructs.

Rules with empty bodies are called **facts**. For example, the following rule is a fact:

```mw
r(x) :- .
```

The set of facts is called the **extensional database** or **EDB** of the Datalog program. The set of tuples computed by evaluating the Datalog program is called the **intensional database** or **IDB**.

### Syntactic sugar

Many implementations of logic programming extend the above grammar to allow writing facts without the `:-`, like so:

```mw
r(x).
```

Some also allow writing 0-ary relations without parentheses, like so:

```mw
p :- q.
```

These are merely abbreviations (syntactic sugar); they have no impact on the semantics of the program.

## Semantics

| Program | edge(x, y). edge(y, z). path(A, B) :- edge(A, B). path(A, C) :- path(A, B), edge(B, C). |
|---|---|
| Herbrand universe | `x`, `y`, `z` |
| Herbrand base | `edge(x, x)`, `edge(x, y)`, ..., `edge(z, z)`, `path(x, x)`, ..., `path(z, z)` |
| Herbrand model | `edge(x, y)`, `edge(y, z)`, `path(x, y)`, `path(y, z)`, `path(x, z)` |

There are three widely-used approaches to the semantics of Datalog programs: model-theoretic, fixed-point, and proof-theoretic. These three approaches can be proven equivalent.

An atom is called **ground** if none of its subterms are variables. Intuitively, each of the semantics define the meaning of a program to be the set of all ground atoms that can be deduced from the rules of the program, starting from the facts.

### Model theoretic

A rule is called ground if all of its atoms (head and body) are ground. A rule *R*2 is a *ground instance* of another rule *R*1 if *R*2 is the result of a substitution of constants for all the variables in *R*1. The *Herbrand base* of a Datalog program is the set of all ground atoms that can be made with the constants appearing in the program. The **Herbrand model** of a Datalog program is the smallest subset of the Herbrand base such that, for each ground instance of each rule in the program, if the atoms in the body of the rule are in the set, then so is the head. The model-theoretic semantics define the minimal Herbrand model to be the meaning of the program.

### Fixed-point

Let I be the power set of the Herbrand base of a program *P*. The *immediate consequence operator* for *P* is a map T from I to I that adds all of the new ground atoms that can be derived from the rules of the program in a single step. The least-fixed-point semantics define the least fixed point of T to be the meaning of the program; this coincides with the minimal Herbrand model.

The fixpoint semantics suggest an algorithm for computing the minimal model: Start with the set of ground facts in the program, then repeatedly add consequences of the rules until a fixpoint is reached. This algorithm is called naïve evaluation.

### Proof-theoretic

The proof-theoretic semantics defines the meaning of a Datalog program to be the set of facts with corresponding *proof trees*. Intuitively, a proof tree shows how to derive a fact from the facts and rules of a program.

One might be interested in knowing whether or not a particular ground atom appears in the minimal Herbrand model of a Datalog program, perhaps without caring much about the rest of the model. A top-down reading of the proof trees described above suggests an algorithm for computing the results of such *queries*. This reading informs the SLD resolution algorithm, which forms the basis for the evaluation of Prolog.

## Evaluation

There are many different ways to evaluate a Datalog program, with different performance characteristics.

### Bottom-up evaluation strategies

Bottom-up evaluation strategies start with the facts in the program and repeatedly apply the rules until either some goal or query is established, or until the complete minimal model of the program is produced.

#### Naïve evaluation

*Naïve evaluation* mirrors the fixpoint semantics for Datalog programs. Naïve evaluation uses a set of "known facts", which is initialized to the facts in the program. It proceeds by repeatedly enumerating all ground instances of each rule in the program. If each atom in the body of the ground instance is in the set of known facts, then the head atom is added to the set of known facts. This process is repeated until a fixed point is reached, and no more facts may be deduced. Naïve evaluation produces the entire minimal model of the program.

#### Semi-naïve evaluation

Semi-naïve evaluation is a bottom-up evaluation strategy that can be asymptotically faster than naïve evaluation. In naïve evaluation, the same facts may be discovered over and over again, while semi-naïve evaluation avoids this repeated computation by only working with the new tuples generated in the previous iteration.

#### Performance considerations

Naïve and semi-naïve evaluation both evaluate recursive Datalog rules by repeatedly applying them to a set of known facts until a fixed point is reached. In each iteration, rules are only run for "one step", i.e., non-recursively. As mentioned above, each non-recursive Datalog rule corresponds precisely to a conjunctive query. Therefore, many of the techniques from database theory used to speed up conjunctive queries are applicable to bottom-up evaluation of Datalog, such as

- Index selection
- Query optimization, especially join order
- Join algorithms
- Selection of data structures used to store relations; common choices include hash tables and B-trees, other possibilities include disjoint set data structures (for storing equivalence relations), bries (a variant of tries), binary decision diagrams, and even SMT formulas

Many such techniques are implemented in modern bottom-up Datalog engines such as Soufflé. Some Datalog engines integrate SQL databases directly.

Bottom-up evaluation of Datalog is also amenable to parallelization. Parallel Datalog engines are generally divided into two paradigms:

- In the shared-memory, multi-core setting, Datalog engines execute on a single node. Coordination between threads may be achieved using locking or lock-free data structures. The shared-memory setting may be further divided into single instruction, multiple data and multiple instruction, multiple data paradigms:
  - Datalog engines that execute on graphics processing units fall into the SIMD paradigm.
  - Datalog engines using OpenMP are instances of the MIMD paradigm.
- In the shared-nothing setting, Datalog engines execute on a cluster of nodes. Such engines generally operate by splitting relations into disjoint subsets based on a hash function, performing computations (joins) on each node, and then exchanging newly-generated tuples over the network. Examples include Datalog engines based on MPI, Hadoop, and Spark.

### Top-down evaluation strategies

SLD resolution is sound and complete for Datalog programs.

### Magic sets

Top-down evaluation strategies begin with a *query* or *goal*. Bottom-up evaluation strategies can answer queries by computing the entire minimal model and matching the query against it, but this can be inefficient if the answer only depends on a small subset of the entire model. The *magic sets* algorithm takes a Datalog program and a query, and produces a more efficient program that computes the same answer to the query while still using bottom-up evaluation. A variant of the magic sets algorithm has been shown to produce programs that, when evaluated using semi-naïve evaluation, are as efficient as top-down evaluation.

## Complexity

The decision problem formulation of Datalog evaluation is as follows: "Given a Datalog program P split into a set of facts (EDB) E and a set of rules R, and a ground atom A. Is A in the minimal model of P?" In this formulation, there are three variations of the computational complexity of evaluating Datalog programs:

- The **data complexity** is the complexity of the decision problem when A and E are inputs and R is fixed.
- The **program complexity** is the complexity of the decision problem when A and R are inputs and E is fixed.
- The **combined complexity** is the complexity of the decision problem when A, E, and R are inputs.

With respect to data complexity, the decision problem for Datalog is P-complete (See Theorem 4.4 in ). P-completeness for data complexity means that there exists a fixed Datalog query for which evaluation is P-complete. The proof is based on *Datalog metainterpreter* for propositional logic programs.

With respect to program complexity, the decision problem is EXPTIME-complete. In particular, evaluating Datalog programs always terminates; Datalog is not Turing-complete.

Some extensions to Datalog do not preserve these complexity bounds. Extensions implemented in some Datalog engines, such as algebraic data types, can even make the resulting language Turing-complete.

## Extensions

Several extensions have been made to Datalog, e.g., to support negation, aggregate functions, inequalities, to allow object-oriented programming, or to allow disjunctions as heads of clauses. These extensions have significant impacts on the language's semantics and on the implementation of a corresponding interpreter.

Datalog is a syntactic subset of Prolog, disjunctive Datalog, answer set programming, DatalogZ, and constraint logic programming. When evaluated as an answer set program, a Datalog program yields a single answer set, which is exactly its minimal model.

Many implementations of Datalog extend Datalog with additional features; see § Datalog engines for more information.

### Aggregation

Datalog can be extended to support aggregate functions.

Notable Datalog engines that implement aggregation include:

- LogicBlox
- Soufflé

### Negation

Adding negation to Datalog complicates its semantics, leading to whole new languages and strategies for evaluation. For example, the language that results from adding negation with the stable model semantics is exactly answer set programming.

Stratified negation can be added to Datalog while retaining its model-theoretic and fixed-point semantics. Notable Datalog engines that implement stratified negation include:

- LogicBlox
- Soufflé

## Comparison to Prolog

Unlike in Prolog, statements of a Datalog program can be stated in any order. Datalog does not have Prolog's cut operator. This makes Datalog a fully declarative language.

In contrast to Prolog, Datalog

- disallows complex terms as arguments of predicates, e.g., `p(x, y)` is admissible but not `p(f(x), y)`,
- disallows negation,
- requires that every variable that appears in the head of a clause also appear in a literal in the body of the clause.

This article deals primarily with Datalog without negation (see also Syntax and semantics of logic programming § Negation). However, stratified negation is a common addition to Datalog; the following list contrasts Prolog with Datalog with stratified negation. Datalog with stratified negation

- also disallows complex terms as arguments of predicates,
- requires that every variable that appears in the head of a clause also appear in a positive (i.e., not negated) atom in the body of the clause,
- requires that every variable appearing in a negative literal in the body of a clause also appear in some positive literal in the body of the clause.

## Expressiveness

Datalog generalizes many other query languages. For instance, conjunctive queries and union of conjunctive queries can be expressed in Datalog. Datalog can also express regular path queries.

When we consider *ordered databases*, i.e., databases with an order relation on their active domain, then the Immerman–Vardi theorem implies that the expressive power of Datalog is precisely that of the class PTIME: a property can be expressed in Datalog if and only if it is computable in polynomial time.

The **boundedness problem** for Datalog asks, given a Datalog program, whether it is **bounded**, i.e., the maximal recursion depth reached when evaluating the program on an input database can be bounded by some constant. In other words, this question asks whether the Datalog program could be rewritten as a nonrecursive Datalog program, or, equivalently, as a union of conjunctive queries. Solving the boundedness problem on arbitrary Datalog programs is undecidable, but it can be made decidable by restricting to some fragments of Datalog.

## Datalog engines

Systems that implement languages inspired by Datalog, whether compilers, interpreters, libraries, or embedded DSLs, are referred to as **Datalog engines**. Datalog engines often implement extensions of Datalog, extending it with additional data types, foreign function interfaces, or support for user-defined lattices. Such extensions may allow for writing non-terminating or otherwise ill-defined programs.

Here is a short list of systems that are either based on Datalog or provide a Datalog interpreter:

### Free software/open source

| Name | Year of latest release | Written in | Licence | Data sources | Description |
|---|---|---|---|---|---|
| *AbcDatalog* | 2023 | Java | BSD |   | Datalog engine that implements common evaluation algorithms; designed for extensibility, research use, and education |
| *Ascent* | 2023 | Rust | MIT License |   | A logic programming language (similar to Datalog) embedded in Rust via macros, supporting a Lattice and customized datastructure. |
| *bddbddb* | 2007 | Java | GNU LGPL |   | Datalog implementation designed to query Java bytecode including points-to analysis on large Java programs; using BDDs internally. |
| *Bloom (Bud)* | 2017 | Ruby | BSD 3-Clause |   | Ruby DSL for programming with data-centric constructs, based on the Dedalus extension of Datalog which adds a temporal dimension to the logic |
| *Cascalog* | 2014 | Clojure | Apache 2.0 | can query other DBMS | Data processing and querying library for Clojure and Java, designed to be used on Hadoop |
| *Clingo* | 2024 | C++ | MIT License |   | Answer Set Programming system that supports Datalog as a special case; its standalone grounder *gringo* suffices for plain Datalog |
| *ConceptBase* | 2025 | Prolog/C++/Java | BSD 2-Clause |   | deductive and object-oriented database system for conceptual modeling and metamodeling, which includes a Datalog query evaluator |
| *Coral* | 1997 | C++ | proprietary, free for some uses, open source |   | A deductive database system written in C++ with semi-naïve datalog evaluation. Developed 1988-1997. |
| *Crepe* | 2023 | Rust | Apache 2.0 or MIT |   | Rust library for expressing Datalog-like inferences, based on procedural macros |
| *Datafrog* | 2019 | Rust | Apache 2.0 or MIT |   | Lightweight Datalog engine intended to be embedded in other Rust programs |
| *Datafun* | 2016 | Racket | open source, no license in repository |   | Functional programming language that generalized Datalog on semilattices |
| *Datahike* | 2024 | Clojure | Eclipse Public License 1.0 | built-in database (in-memory or file) | Fork of DataScript with a durable backend based on a hitchhiker tree, using Datalog as query language |
| *Datalevin* | 2024 | Clojure | Eclipse Public License 1.0 | LMDB bindings | Fork of DataScript optimized for LMDB durable storage, using Datalog as query language |
| *Datalog (Erlang)* | 2019 | Erlang | Apache 2.0 |   | Library to support Datalog queries in Erlang, with data represented as streams of tuples |
| *Datalog (MITRE)* | 2016 | Lua | GNU LGPL |   | Lightweight deductive database system, designed to be small and usable on memory constrained devices |
| *Datalog (OCaml)* | 2019 | OCaml | BSD 2-clause |   | In-memory Datalog implementation for OCaml featuring bottom-up and top-down algorithms |
| *Datalog (Racket)* | 2022 | Racket | Apache 2.0 or MIT |   | Racket package for using Datalog |
| *Datalog Educational System* | 2025 | Prolog | GNU LGPL | DBMS connectors | Open-source implementation intended for teaching Datalog and SQL |
| *DataScript* | 2024 | Clojure | Eclipse Public License 1.0 | in-memory database | Immutable database that runs in a browser, using Datalog as query language |
| *Datomic* | 2024 | Clojure | closed source; binaries released under Apache 2.0 | bindings for DynamoDB, Cassandra, PostgreSQL and others | Distributed database running on cloud architectures; uses Datalog as query language |
| *DDlog* | 2021 | Rust | MIT License |   | Incremental, in-memory, typed Datalog engine; compiled in Rust; based on the differential dataflow library |
| *DLV* | 2023 | C++ | proprietary, free for some uses |   | Answer Set Programming system that supports Datalog as a special case |
| *Dyna1* | 2013 | Haskell | GNU AGPL v3 |   | Declarative programming language using Datalog for statistical AI programming; later Dyna versions do not use Datalog |
| *Flix* | 2024 | Java | Apache 2.0 |   | Functional and logic programming language inspired by Datalog extended with user-defined lattices and monotone filter/transfer functions |
| *Graal* | 2018 | Java | CeCILL v2.1 | RDF import, CSV import, DBMS connectors | Java toolkit dedicated to querying knowledge bases within the framework of existential rules (a.k.a. tuple-generating dependencies or Datalog+/-) |
| *Inter4QL* | 2020 | C++ | BSD |   | Interpreter for a database query language based on four-valued logic, supports Datalog as a special case |
| *IRIS* | 2016 | Java | GNU LGPL v2.1 |   | Logic programming system supporting Datalog and negation under the well-founded semantics; support for RDFS |
| *Jena* | 2024 | Java | Apache 2.0 | RDF import | Semantic web framework that includes a Datalog implementation as part of its general purpose rule engine; compatibility with RDF |
| *Mangle* | 2024 | Go | Apache 2.0 |   | Programming language for deductive database programming, supporting an extension of Datalog |
| *maplib* | 2025 | Rust | Apache 2.0, proprietary for some uses | RDF import, Polars data frames | Semantic web framework in Python that support Datalog reasoning for knowledge graphs as RDF |
| *Naga* | 2021 | Clojure | Eclipse Public License 1.0 | *Asami* graph database | Query engine that executes Datalog queries over the graph database; runs in browsers (memory), on JVM (memory/files), or natively (memory/files). |
| *Nemo* | 2024 | Rust | Apache 2.0 or MIT | RDF import, CSV import | In-memory rule engine for knowledge graph analysis and database transformations; compatible with RDF and SPARQL; supports tgds |
| *pyDatalog* | 2015 | Python | GNU LGPL | DBMS connectors from Python | Python library for interpreting Datalog queries |
| *RDFox* | 2025 | C++ | proprietary, free for some uses | in-memory database, RDF import, CSV import, DBMS connectors | Main-memory based RDF triple store with Datalog reasoning; supports incremental evaluation and high availability setups |
| *SociaLite* | 2016 | Java | Apache 2.0 | HDFS bindings | Datalog variant and engine for large-scale graph analysis |
| *Soufflé* | 2023 | C++ | UPL v1.0 | CSV import, sqlite3 bindings | Datalog engine originally designed for applications static program analysis; rule sets are either compiled to C++ programs or interpreted |
| *tclbdd* | 2015 | Tcl | BSD |   | Datalog implementation based on binary decision diagrams; designed to support development of an optimizing compiler for Tcl |
| *TerminusDB* | 2024 | Prolog/Rust | Apache 2.0 |   | Graph database and document store, that also features a Datalog-based query language |
| *XSB* | 2022 | C | GNU LGPL |   | A logic programming and deductive database system based on Prolog with tabling giving Datalog-like termination and efficiency, including incremental evaluation |
| *XTDB* (formerly *Crux*) | 2024 | Clojure | MPL 2.0 | bindings for Apache Kafka and others | Immutable database with time-travel, Datalog used as query language in XTDB 1.x (may change in XTDB 2.x) |
| *Minigraf* | 2026 | Rust | Apache 2.0 or MIT | Supports multiple runtimes including WASM, Android, iOS and native platforms like Linux, Windows and Mac. Also provides language bindings for C, Java, Python and Node.js. | Open-source, embeddable bi-temporal Datalog property graph database. It supports valid time, transaction time, and full bi-temporal queries in a Datalog query engine. |

### Non-free software

- FoundationDB provides a free-of-charge database binding for pyDatalog, with a tutorial on its use.
- Leapsight Semantic Dataspace (LSD) is a distributed deductive database that offers high availability, fault tolerance, operational simplicity, and scalability. LSD uses Leaplog (a Datalog implementation) for querying and reasoning and was created by Leapsight.
- LogicBlox, a commercial implementation of Datalog used for web-based retail planning and insurance applications.
- Profium Sense is a native RDF compliant graph database written in Java. It provides Datalog evaluation support of user defined rules.
- .QL, a commercial object-oriented variant of Datalog created by Semmle for analyzing source code to detect security vulnerabilities.
- SecPAL a security policy language developed by Microsoft Research.
- Stardog is a graph database, implemented in Java. It provides support for RDF and all OWL 2 profiles providing extensive reasoning capabilities, including datalog evaluation.
- StrixDB: a commercial RDF graph store, SPARQL compliant with Lua API and Datalog inference capabilities. Could be used as httpd (Apache HTTP Server) module or standalone (although beta versions are under the Perl Artistic License 2.0).

## Uses and influence

Datalog is quite limited in its expressivity. It is not Turing-complete, and doesn't include basic data types such as integers or strings. This parsimony is appealing from a theoretical standpoint, but it means Datalog *per se* is rarely used as a programming language or knowledge representation language. Most Datalog engines implement substantial extensions of Datalog. However, Datalog has a strong influence on such implementations, and many authors don't bother to distinguish them from Datalog as presented in this article. Accordingly, the applications discussed in this section include applications of realistic implementations of Datalog-based languages.

Datalog has been applied to problems in data integration, information extraction, networking, security, cloud computing and machine learning. Google has developed an extension to Datalog for big data processing.

Datalog has seen application in static program analysis. The Soufflé dialect has been used to write pointer analyses for Java and a control-flow analysis for Scheme. Datalog has been integrated with SMT solvers to make it easier to write certain static analyses. The Flix dialect is also suited to writing static program analyses.

Some widely used database systems include ideas and algorithms developed for Datalog. For example, the SQL:1999 standard includes recursive queries, and the Magic Sets algorithm (initially developed for the faster evaluation of Datalog queries) is implemented in IBM's DB2.

## History

The origins of Datalog date back to the beginning of logic programming, but it became prominent as a separate area around 1977 when Hervé Gallaire and Jack Minker organized a workshop on logic and databases. David Maier is credited with coining the term Datalog.
