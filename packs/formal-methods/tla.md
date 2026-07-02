---
title: "TLA+"
source: https://en.wikipedia.org/wiki/TLA%2B
domain: formal-methods
license: CC-BY-SA-4.0
tags: formal verification, model checking, tla+, hoare logic, design by contract, static analysis
fetched: 2026-07-02
---

# TLA+

**TLA+** is a formal specification language developed by Leslie Lamport. It is used for designing, modelling, documentation, and verification of programs, especially concurrent systems and distributed systems. TLA+ is considered to be exhaustively-testable pseudocode, and its use likened to drawing blueprints for software systems; *TLA* is an acronym for Temporal Logic of Actions.

For design and documentation, TLA+ fulfills the same purpose as informal technical specifications. However, TLA+ specifications are written in a formal language of logic and mathematics, and the precision of specifications written in this language is intended to uncover design flaws before system implementation is underway.

Since TLA+ specifications are written in a formal language, they are amenable to finite model checking. The model checker finds all possible system behaviours up to some number of execution steps, and examines them for violations of desired invariance properties such as safety and liveness. TLA+ specifications use basic set theory to define safety (bad things won't happen) and temporal logic to define liveness (good things eventually happen).

TLA+ is also used to write machine-checked proofs of correctness both for algorithms and mathematical theorems. The proofs are written in a declarative, hierarchical style independent of any single theorem prover backend. Both formal and informal structured mathematical proofs can be written in TLA+; the language is similar to LaTeX, and tools exist to translate TLA+ specifications to LaTeX documents.

TLA+ was introduced in 1999, following several decades of research into a verification method for concurrent systems. Ever since, a toolchain has been developed, including an IDE and a distributed model checker. The pseudocode-like language PlusCal was created in 2009; it transpiles to TLA+ and is useful for specifying sequential algorithms. TLA+2 was announced in 2014, expanding language support for proof constructs. The current TLA+ reference is The TLA+ Hyperbook by Leslie Lamport.

## History

Modern temporal logic was developed by Arthur Prior in 1957, then called tense logic. Although Amir Pnueli was the first to seriously study the applications of temporal logic to computer science, Prior speculated on its use a decade earlier in 1967:

> The usefulness of systems of this sort [on discrete time] does not depend on any serious metaphysical assumption that time is discrete; they are applicable in limited fields of discourse in which we are concerned only with what happens next in a sequence of discrete states, e.g. in the working of a digital computer.

Pnueli researched the use of temporal logic in specifying and reasoning about computer programs, introducing linear temporal logic in 1977. LTL became an important tool for analysis of concurrent programs, easily expressing properties such as mutual exclusion and freedom from deadlock.

Concurrent with Pnueli's work on LTL, academics were working to generalize Hoare logic for verification of multiprocess programs. Leslie Lamport became interested in the problem after peer review found an error in a paper he submitted on mutual exclusion. Ed Ashcroft introduced invariance in his 1975 paper "Proving Assertions About Parallel Programs", which Lamport used to generalize Floyd's method in his 1977 paper "Proving Correctness of Multiprocess Programs". Lamport's paper also introduced safety and liveness as generalizations of partial correctness and termination, respectively. This method was used to verify the first concurrent garbage collection algorithm in a 1978 paper with Edsger Dijkstra.

Lamport first encountered Pnueli's LTL during a 1978 seminar at Stanford organized by Susan Owicki. According to Lamport, "I was sure that temporal logic was some kind of abstract nonsense that would never have any practical application, but it seemed like fun, so I attended." In 1980 he published "'Sometime' is Sometimes 'Not Never'", which became one of the most frequently-cited papers in the temporal logic literature. Lamport worked on writing temporal logic specifications during his time at SRI, but found the approach to be impractical:

> However, I became disillusioned with temporal logic when I saw how Schwartz, Melliar-Smith, and Fritz Vogt were spending days trying to specify a simple FIFO queue – arguing over whether the properties they listed were sufficient. I realized that, despite its aesthetic appeal, writing a specification as a conjunction of temporal properties just didn't work in practice.

His search for a practical method of specification resulted in the 1983 paper "Specifying Concurrent Programming Modules", which introduced the idea of describing state transitions as Boolean-valued functions of primed and unprimed variables. Work continued throughout the 1980s, and Lamport began publishing papers on the temporal logic of actions in 1990; however, it was not formally introduced until "The Temporal Logic of Actions" was published in 1994. TLA enabled the use of actions in temporal formulas, which according to Lamport "provides an elegant way to formalize and systematize all the reasoning used in concurrent system verification."

TLA specifications mostly consisted of ordinary non-temporal mathematics, which Lamport found less cumbersome than a purely temporal specification. TLA provided a mathematical foundation to the specification language TLA+, introduced with the paper "Specifying Concurrent Systems with TLA+" in 1999. Later that same year, Yuan Yu wrote the TLC model checker for TLA+ specifications; TLC was used to find errors in the cache coherence protocol for a Compaq multiprocessor.

Lamport published a full textbook on TLA+ in 2002, titled "Specifying Systems: The TLA+ Language and Tools for Software Engineers". PlusCal was introduced in 2009, and the TLA+ proof system (TLAPS) in 2012. TLA+2 was announced in 2014, adding some additional language constructs as well as greatly increasing in-language support for the proof system. Lamport is engaged in creating an updated TLA+ reference, "The TLA+ Hyperbook". The incomplete work is available from his official website. Lamport is also creating The TLA+ Video Course, described therein as "a work in progress that consists of the beginning of a series of video lectures to teach programmers and software engineers how to write their own TLA+ specifications".

## Language

TLA+ specifications are organized into modules. Modules can extend (import) other modules to use their functionality. Although the TLA+ standard is specified in typeset mathematical symbols, existing TLA+ tools use LaTeX-like symbol definitions in ASCII. TLA+ uses several terms which require definition:

- *State* – an assignment of values to variables
- *Behaviour* – a sequence of states
- *Step* – a pair of successive states in a behavior
- *Stuttering step* – a step during which variables are unchanged
- *Next-state relation* – a relation describing how variables can change in any step
- *State function* – an expression containing variables and constants that is not a next-state relation
- *State predicate* – a Boolean-valued state function
- *Invariant* – a state predicate true in all reachable states
- *Temporal formula* – an expression containing statements in temporal logic

### Safety

TLA+ concerns itself with defining the set of all correct system behaviours. For example, a one-bit clock ticking endlessly between 0 and 1 could be specified as follows:

```mw
VARIABLE clock

Init == clock \in {0, 1}

Tick == IF clock = 0 THEN clock' = 1 ELSE clock' = 0

Spec == Init /\ [][Tick]_<<clock>>
```

The next-state relation **Tick** sets *clock*′ (the value of *clock* in the next state) to 1 if *clock* is 0, and 0 if *clock* is 1. The state predicate **Init** is true if the value of *clock* is either 0 or 1. **Spec** is a temporal formula asserting all behaviours of one-bit clock must initially satisfy **Init** and have all steps either match **Tick** or be stuttering steps. Two such behaviours are:

```mw
0 -> 1 -> 0 -> 1 -> 0 -> ...

1 -> 0 -> 1 -> 0 -> 1 -> ...
```

The safety properties of the one-bit clock – the set of reachable system states – are adequately described by the spec.

### Liveness

The above spec disallows strange states for the one-bit clock, but does not say the clock will ever tick. For example, the following perpetually-stuttering behaviours are accepted:

```mw
0 -> 0 -> 0 -> 0 -> 0 -> ...

1 -> 1 -> 1 -> 1 -> 1 -> ...
```

A clock which does not tick is not useful, so these behaviours should be disallowed. One solution is to disable stuttering, but TLA+ requires stuttering always be enabled; a stuttering step represents a change to some part of the system not described in the spec, and is useful for refinement. To ensure the clock must eventually tick, weak fairness is asserted for **Tick**:

```mw
Spec == Init /\ [][Tick]_<<clock>> /\ WF_<<clock>>(Tick)
```

Weak fairness over an action means if that action is continuously enabled, it must eventually be taken. With weak fairness on **Tick** only a finite number of stuttering steps are permitted between ticks. This temporal logical statement about **Tick** is called a liveness assertion. In general, a liveness assertion should be *machine-closed*: it shouldn't constrain the set of reachable states, only the set of possible behaviours.

Most specifications do not require assertion of liveness properties. Safety properties suffice both for model checking and guidance in system implementation.

### Operators

TLA+ is based on ZF, so operations on variables involve set manipulation. The language includes set membership, union, intersection, difference, powerset, and subset operators. First-order logic operators such as ∨, ∧, ¬, ⇒, ↔, ≡ are also included, as well as universal and existential quantifiers ∀ and ∃. Hilbert's ε is provided as the CHOOSE operator, which uniquely selects an arbitrary set element. Arithmetic operators over reals, integers, and natural numbers are available from the standard modules.

Temporal logic operators are built into TLA+. Temporal formulas use $\Box P$ to mean *P* is always true, and $\Diamond P$ to mean *P* is eventually true. The operators are combined into $\Box \Diamond P$ to mean *P* is true infinitely often, or $\Diamond \Box P$ to mean eventually *P* will always be true. Other temporal operators include weak and strong fairness. Weak fairness WFe(*A*) means if action *A* is enabled *continuously* (i.e. without interruptions), it must eventually be taken. Strong fairness SFe(*A*) means if action *A* is enabled *continually* (repeatedly, with or without interruptions), it must eventually be taken.

Temporal existential and universal quantification are included in TLA+, although without support from the tools.

User-defined operators are similar to macros. Operators differ from functions in that their domain need not be a set: for example, the set membership operator has the category of sets as its domain, which is not a valid set in ZFC (since its existence leads to Russell's paradox). Recursive and anonymous user-defined operators were added in TLA+2.

### Data structures

The foundational data structure of TLA+ is the set. Sets are either explicitly enumerated or constructed from other sets using operators or with `{x \in S : p}` where *p* is some condition on *x*, or `{e : x \in S}` where *e* is some function of *x*. The unique empty set is represented as `{}`.

Functions in TLA+ assign a value to each element in their domain, a set. `[S -> T]` is the set of all functions with f[*x*] in *T*, for each *x* in the domain set *S*. For example, the TLA+ function `Double[x \in Nat] == x*2` is an element of the set `[Nat -> Nat]` so `Double \in [Nat -> Nat]` is a true statement in TLA+. Functions are also defined with `[x \in S |-> e]` for some expression *e*, or by modifying an existing function `[f EXCEPT ![v1] = v2]`.

Records are a type of function in TLA+. The record `[name |-> "John", age |-> 35]` is a record with fields name and age, accessed with `r.name` and `r.age`, and belonging to the set of records `[name : String, age : Nat]`.

Tuples are included in TLA+. They are explicitly defined with `<<e1,e2,e3>>` or constructed with operators from the standard Sequences module. Sets of tuples are defined by Cartesian product; for example, the set of all pairs of natural numbers is defined `Nat \X Nat`.

## Standard modules

TLA+ has a set of standard modules containing common operators. They are distributed with the syntactic analyzer. The TLC model checker uses Java implementations for improved performance.

- **FiniteSets**: Module for working with finite sets. Provides *IsFiniteSet(S)* and *Cardinality(S)* operators.
- **Sequences**: Defines operators on tuples such as *Len(S)*, *Head(S)*, *Tail(S)*, *Append(S, E)*, concatenation, and filter.
- **Bags**: Module for working with multisets. Provides primitive set operation analogues and duplicate counting.
- **Naturals**: Defines the Natural numbers along with inequality and arithmetic operators.
- **Integers**: Defines the Integers.
- **Reals**: Defines the Real numbers along with division and infinity.
- **RealTime**: Provides definitions useful in real-time system specifications.
- **TLC**: Provides utility functions for model-checked specifications, such as logging and assertions.

Standard modules are imported with the `EXTENDS` or `INSTANCE` statements.

## Tools

### IDE

An integrated development environment is implemented on top of Eclipse. It includes an editor with error and syntax highlighting, plus a GUI front-end to several other TLA+ tools:

- The SANY syntactic analyzer, which parses and checks the spec for syntax errors.
- The LaTeX translator, to generate pretty-printed specs.
- The PlusCal translator.
- The TLC model checker.
- The TLAPS proof system.

The IDE is distributed in The TLA Toolbox.

### Model checker

The TLC model checker builds a finite state model of TLA+ specifications for checking invariance properties. TLC generates a set of initial states satisfying the spec, then performs a breadth-first search over all defined state transitions. Execution stops when all state transitions lead to states which have already been discovered. If TLC discovers a state which violates a system invariant, it halts and provides a state trace path to the offending state. TLC provides a method of declaring model symmetries to defend against combinatorial explosion. It also parallelizes the state exploration step, and can run in distributed mode to spread the workload across a large number of computers.

As an alternative to exhaustive breadth-first search, TLC can use depth-first search or generate random behaviours. TLC operates on a subset of TLA+; the model must be finite and enumerable, and some temporal operators are not supported. In distributed mode TLC cannot check liveness properties, nor check random or depth-first behaviours. TLC is available as a command line tool or bundled with the TLA toolbox.

### Proof system

The TLA+ Proof System, or TLAPS, mechanically checks proofs written in TLA+. It was developed at the Microsoft Research-INRIA Joint Centre to prove correctness of concurrent and distributed algorithms. The proof language is designed to be independent of any particular theorem prover; proofs are written in a declarative style, and transformed into individual obligations which are sent to back-end provers. The primary back-end provers are Isabelle and Zenon, with fallback to SMT solvers CVC3, Yices, and Z3. TLAPS proofs are hierarchically structured, easing refactoring and enabling non-linear development: work can begin on later steps before all prior steps are verified, and difficult steps are decomposed into smaller sub-steps. TLAPS works well with TLC, as the model checker quickly finds small errors before verification is begun. In turn, TLAPS can prove system properties which are beyond the capabilities of finite model checking.

TLAPS does not currently support reasoning with real numbers, nor most temporal operators. Isabelle and Zenon generally cannot prove arithmetic proof obligations, requiring use of the SMT solvers. TLAPS has been used to prove correctness of Byzantine Paxos, the Memoir security architecture, components of the Pastry distributed hash table, and the Spire consensus algorithm. It is distributed separately from the rest of the TLA+ tools and is free software, distributed under the BSD license. TLA+2 greatly expanded language support for proof constructs.

## Industry use

At Microsoft, a critical bug was discovered in the Xbox 360 memory module during the process of writing a specification in TLA+. TLA+ was used to write formal proofs of correctness for Byzantine Paxos and components of the Pastry distributed hash table.

Amazon Web Services has used TLA+ since 2011. TLA+ model checking uncovered bugs in DynamoDB, S3, EBS, and an internal distributed lock manager; some bugs required state traces of 35 steps. Model checking was also used to verify aggressive optimizations. In addition, TLA+ specifications were found to hold value as documentation and design aids.

Microsoft Azure used TLA+ to design Cosmos DB, a globally-distributed database with five different consistency models.

Altreonic NV used TLA+ to model check OpenComRTOS.

## Examples

A key-value store with snapshot isolation:

```mw
--------------------------- MODULE KeyValueStore ---------------------------
CONSTANTS   Key,            \* The set of all keys.
            Val,            \* The set of all values.
            TxId            \* The set of all transaction IDs.
VARIABLES   store,          \* A data store mapping keys to values.
            tx,             \* The set of open snapshot transactions.
            snapshotStore,  \* Snapshots of the store for each transaction.
            written,        \* A log of writes performed within each transaction.
            missed          \* The set of writes invisible to each transaction.
----------------------------------------------------------------------------
NoVal ==    \* Choose something to represent the absence of a value.
    CHOOSE v : v \notin Val

Store ==    \* The set of all key-value stores.
    [Key -> Val \cup {NoVal}]

Init == \* The initial predicate.
    /\ store = [k \in Key |-> NoVal]        \* All store values are initially NoVal.
    /\ tx = {}                              \* The set of open transactions is initially empty.
    /\ snapshotStore =                      \* All snapshotStore values are initially NoVal.
        [t \in TxId |-> [k \in Key |-> NoVal]]
    /\ written = [t \in TxId |-> {}]        \* All write logs are initially empty.
    /\ missed = [t \in TxId |-> {}]         \* All missed writes are initially empty.
    
TypeInvariant ==    \* The type invariant.
    /\ store \in Store
    /\ tx \subseteq TxId
    /\ snapshotStore \in [TxId -> Store]
    /\ written \in [TxId -> SUBSET Key]
    /\ missed \in [TxId -> SUBSET Key]
    
TxLifecycle ==
    /\ \A t \in tx :    \* If store != snapshot & we haven't written it, we must have missed a write.
        \A k \in Key : (store[k] /= snapshotStore[t][k] /\ k \notin written[t]) => k \in missed[t]
    /\ \A t \in TxId \ tx : \* Checks transactions are cleaned up after disposal.
        /\ \A k \in Key : snapshotStore[t][k] = NoVal
        /\ written[t] = {}
        /\ missed[t] = {}

OpenTx(t) ==    \* Open a new transaction.
    /\ t \notin tx
    /\ tx' = tx \cup {t}
    /\ snapshotStore' = [snapshotStore EXCEPT ![t] = store]
    /\ UNCHANGED <<written, missed, store>>

Add(t, k, v) == \* Using transaction t, add value v to the store under key k.
    /\ t \in tx
    /\ snapshotStore[t][k] = NoVal
    /\ snapshotStore' = [snapshotStore EXCEPT ![t][k] = v]
    /\ written' = [written EXCEPT ![t] = @ \cup {k}]
    /\ UNCHANGED <<tx, missed, store>>
    
Update(t, k, v) ==  \* Using transaction t, update the value associated with key k to v.
    /\ t \in tx
    /\ snapshotStore[t][k] \notin {NoVal, v}
    /\ snapshotStore' = [snapshotStore EXCEPT ![t][k] = v]
    /\ written' = [written EXCEPT ![t] = @ \cup {k}]
    /\ UNCHANGED <<tx, missed, store>>
    
Remove(t, k) == \* Using transaction t, remove key k from the store.
    /\ t \in tx
    /\ snapshotStore[t][k] /= NoVal
    /\ snapshotStore' = [snapshotStore EXCEPT ![t][k] = NoVal]
    /\ written' = [written EXCEPT ![t] = @ \cup {k}]
    /\ UNCHANGED <<tx, missed, store>>
    
RollbackTx(t) ==    \* Close the transaction without merging writes into store.
    /\ t \in tx
    /\ tx' = tx \ {t}
    /\ snapshotStore' = [snapshotStore EXCEPT ![t] = [k \in Key |-> NoVal]]
    /\ written' = [written EXCEPT ![t] = {}]
    /\ missed' = [missed EXCEPT ![t] = {}]
    /\ UNCHANGED store

CloseTx(t) ==   \* Close transaction t, merging writes into store.
    /\ t \in tx
    /\ missed[t] \cap written[t] = {}   \* Detection of write-write conflicts.
    /\ store' =                         \* Merge snapshotStore writes into store.
        [k \in Key |-> IF k \in written[t] THEN snapshotStore[t][k] ELSE store[k]]
    /\ tx' = tx \ {t}
    /\ missed' =    \* Update the missed writes for other open transactions.
        [otherTx \in TxId |-> IF otherTx \in tx' THEN missed[otherTx] \cup written[t] ELSE {}]
    /\ snapshotStore' = [snapshotStore EXCEPT ![t] = [k \in Key |-> NoVal]]
    /\ written' = [written EXCEPT ![t] = {}]

Next == \* The next-state relation.
    \/ \E t \in TxId : OpenTx(t)
    \/ \E t \in tx : \E k \in Key : \E v \in Val : Add(t, k, v)
    \/ \E t \in tx : \E k \in Key : \E v \in Val : Update(t, k, v)
    \/ \E t \in tx : \E k \in Key : Remove(t, k)
    \/ \E t \in tx : RollbackTx(t)
    \/ \E t \in tx : CloseTx(t)
        
Spec == \* Initialize state with Init and transition with Next.
    Init /\ [][Next]_<<store, tx, snapshotStore, written, missed>>
----------------------------------------------------------------------------
THEOREM Spec => [](TypeInvariant /\ TxLifecycle)
=============================================================================
```
