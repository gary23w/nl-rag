---
title: "Separation logic"
source: https://en.wikipedia.org/wiki/Concurrent_separation_logic
domain: separation-logic
license: CC-BY-SA-4.0
tags: separation logic, separating conjunction, heap assertion, frame rule
fetched: 2026-07-02
---

# Separation logic

(Redirected from

Concurrent separation logic

)

In computer science, **separation logic** is an extension of Hoare logic, a way of reasoning about programs. It was developed by John C. Reynolds, Peter O'Hearn, Samin Ishtiaq and Hongseok Yang, drawing upon early work by Rod Burstall. The assertion language of separation logic is a special case of the logic of bunched implications (BI). A CACM review article by O'Hearn charts developments in the subject to early 2019.

## Overview

Separation logic facilitates reasoning about:

- programs that manipulate pointer data structures—including information hiding in the presence of pointers;
- *"transfer of ownership"* (avoidance of semantic frame axioms); and
- virtual separation (modular reasoning) between concurrent modules.

Separation logic supports the developing field of research described by Peter O'Hearn and others as *local reasoning*, whereby specifications and proofs of a program component mention only the portion of memory used by the component, and not the entire global state of the system. Applications include automated program verification (where an algorithm checks the validity of another algorithm) and automated parallelization of software.

## Assertions: operators and semantics

Separation logic assertions describe "states" consisting of a *store* and a *heap*, roughly corresponding to the state of local (or *stack-allocated*) variables and *dynamically-allocated* objects in common programming languages such as C and Java. A store s is a function mapping variables to values. A heap h is a partial function mapping memory addresses to values. Two heaps h and $h'$ are *disjoint* (denoted $h\,\bot \,h'$ ) if their domains do not overlap (i.e., for every memory address $\ell$ , at least one of $h(\ell )$ and $h'(\ell )$ is undefined).

The logic allows to prove judgements of the form $s,h\models P$ , where s is a store, h is a heap, and P is an *assertion* over the given store and heap. Separation logic assertions (denoted as P , Q , R ) contain the standard Boolean connectives and, in addition, $\mathbf {e} \mathbf {m} \mathbf {p}$ , $e\mapsto e'$ , $P\ast Q$ , and $P{-\!\!\ast }\,Q$ , where e and $e'$ are expressions.

- The constant $\mathbf {e} \mathbf {m} \mathbf {p}$ asserts that the heap is *empty*, i.e., $s,h\models \mathbf {e} \mathbf {m} \mathbf {p}$ when h is undefined for all addresses.
- The binary operator $\mapsto$ takes an address and a value and asserts that the heap is defined at exactly one location, mapping the given address to the given value. I.e., $s,h\models e\mapsto e'$ when $h([\![e]\!]_{s})=[\![e']\!]_{s}$ (where $[\![e]\!]_{s}$ denotes the value of expression e evaluated in store s ) and h is otherwise undefined.
- The binary operator $\ast$ (pronounced *star* or *separating conjunction*) asserts that the heap can be split into two *disjoint* parts where its two arguments hold, respectively. I.e., $s,h\models P\ast Q$ when there exist $h_{1},h_{2}$ such that $h_{1}\,\bot \,h_{2}$ and $h=h_{1}\cup h_{2}$ and $s,h_{1}\models P$ and $s,h_{2}\models Q$ .
- The binary operator $-\!\!\ast$ (pronounced *magic wand* or *separating implication*) asserts that extending the heap with a disjoint part that satisfies its first argument results in a heap that satisfies its second argument. I.e,. $s,h\models P-\!\!\ast \,Q$ when for every heap $h'\,\bot \,h$ such that $s,h'\models P$ , also $s,h\cup h'\models Q$ holds.

The operators $\ast$ and $-\!\!\ast$ share some properties with the classical conjunction and implication operators. They can be combined using an inference rule similar to modus ponens

${\frac {s,h\models P\ast (P-\!\!\ast \,Q)}{s,h\models Q}}$

and they form an adjunction, i.e., $s,h\cup h'\models P\ast Q\Rightarrow R$ if and only if $s,h\models P\Rightarrow Q-\!\!\ast \,R$ for $h\,\bot \,h'$ ; more precisely, the adjoint operators are $\_\ast Q$ and $Q-\!\!\ast \,\_$ .

## Reasoning about programs: triples and proof rules

In separation logic, Hoare triples have a slightly different meaning than in Hoare logic. The triple $\{P\}\ C\ \{Q\}$ asserts that if the program C executes from an initial state satisfying the precondition P then the program will *not go wrong* (e.g., have undefined behaviour), and if it terminates, then the final state will satisfy the postcondition Q . In essence, during its execution, C may access only memory locations whose existence is asserted in the precondition or that have been allocated by C itself.

In addition to the standard rules from Hoare logic, separation logic supports the following very important rule:

${\frac {\{P\}\ C\ \{Q\}}{\{P\ast R\}\ C\ \{Q\ast R\}}}~{\mathsf {mod}}(C)\cap {\mathsf {fv}}(R)=\emptyset$

This is known as the **frame rule** (named after the frame problem) and enables local reasoning. It says that a program that executes safely in a small state (satisfying P ), can also execute in any bigger state (satisfying $P\ast R$ ) and that its execution will not affect the additional part of the state (and so R will remain true in the postcondition). The side condition enforces this by specifying that none of the variables modified by C occur free in R , i.e. none of them are in the 'free variable' set ${\mathsf {fv}}$ of R .

## Separation algebras

More generally, separation logic can be seen as a way of reasoning about *separation algebras*. A separation algebra may be defined in several ways, but is often presented as a cancellative, partial commutative monoid. More concretely, it is a set *A*, partial binary operation $\oplus :A\times A\rightharpoonup A$ and constant *u* satisfying the following identities, where in the first three laws, if any side of the equation is defined, all sides are defined:

- Associativity: For all *x*, *y* and *z*, $(x\oplus y)\oplus z=x\oplus (y\oplus z)$
- Commutativity: For all *x* and *y*, $x\oplus y=y\oplus x$
- Identity: For all *x*, $x\oplus u=x=u\oplus x$
- Cancellativity: For all *x*, *y* and *z*, if $x\oplus z=y\oplus z$ then $x=y$

It can be shown that the presentation of stacks and heaps above gives rise to a separation algebra: take *A* to be the set of all heaps, the binary operation $\oplus$ to be the union of two heaps (only defined when the heaps are disjoint), and *u* to be the empty heap. In some definitions, cancellativity is omitted, but this does not necessarily pose a problem.

Many assertions can be given semantics purely in terms of a separation algebra; in particular, for an assertion *P* we can assign to it a certain subset of *A*, denoted $[\![P]\!]$ , as follows:

- $[\![false]\!]=\emptyset$
- $[\![P\Rightarrow Q]\!]=\{h|h\in [\![P]\!]\Rightarrow h\in [\![Q]\!]\}$
- $[\![\forall x.P]\!]=\{h|\forall v.h\in [\![P[x:=v]]\!]\}$
- $[\![\mathbf {e} \mathbf {m} \mathbf {p} ]\!]=\{u\}$
- $[\![P\ast Q]\!]=\{h_{1}\oplus h_{2}|h_{1}\in [\![P]\!]\wedge h_{2}\in [\![Q]\!]\}$
- $[\![P{-\!\!\ast }\,Q]\!]=\{h|\forall h'.h'\,\bot \,h\wedge h'\in [\![P]\!]\Rightarrow h\oplus h'\in [\![Q]\!]\}$

The rules for $\land$ , $\vee$ , $\neg$ and $\exists$ are omitted but are easily derived from the above, while the semantics of $e\mapsto e'$ are given by the separation algebra in question.

## Sharing

Separation logic leads to simple proofs of pointer manipulation for data structures that exhibit regular sharing patterns which can be described simply using separating conjunctions; examples include singly and doubly linked lists and varieties of trees. Graphs and DAGs and other data structures with more general sharing are more difficult for both formal and informal proof. Separation logic has, nonetheless, been applied successfully to reasoning about programs with general sharing.

In their POPL'01 paper, O'Hearn and Ishtiaq explained how the magic wand connective ${-\!\!*}$ could be used to reason in the presence of sharing, at least in principle. For example, in the triple

$\{(x\mapsto -)\ast ((x\mapsto 42){-\!\!*}P)\}\ [x]=42\ \{P\}$

we obtain the weakest precondition for a statement that mutates the heap at location x , and this works for any postcondition, not only one that is laid out neatly using the separating conjunction. This idea was taken much further by Yang, who used ${-\!\!*}$ to provide localized reasoning about mutations in the classic Schorr-Waite graph marking algorithm. Finally, one of the most recent works in this direction is that of Hobor and Villard, who employ not only ${-\!\!*}$ but also a connective $\cup \,\!\!\!\!\!*$ which has variously been called overlapping conjunction or sepish, and which can be used to describe overlapping data structures: $P\cup \!\!\!\!\!*Q$ holds of a heap h when P and Q hold for subheaps $h_{P}$ and $h_{Q}$ whose union is h , but which possibly have a nonempty portion $h_{P}\cap h_{Q}$ in common. Abstractly, $P\cup \!\!\!\!\!*Q$ can be seen to be a version of the fusion connective of relevance logic.

## Concurrent separation logic

A Concurrent Separation Logic (CSL), a version of separation logic for concurrent programs, was originally proposed by Peter O'Hearn, using a proof rule

${\frac {\{P_{1}\}C_{1}\{Q_{1}\}\quad \{P_{2}\}C_{2}\{Q_{2}\}}{\{P_{1}*P_{2}\}C_{1}\parallel C_{2}\{Q_{1}*Q_{2}\}}}$

which allows independent reasoning about threads that access separate storage. O'Hearn's proof rules adapted an early approach of Tony Hoare to reasoning about concurrency, replacing the use of scoping constraints to ensure separation by reasoning in separation logic. In addition to extending Hoare's approach to apply in the presence of heap-allocated pointers, O'Hearn showed how reasoning in concurrent separation logic could track dynamic ownership transfer of heap portions between processes; examples in the paper include a pointer-transferring buffer, and a memory manager.

Commenting on the early classical work on interference freedom by Susan Owicki and David Gries, O'Hearn says that explicit checking for non-interference isn't necessary because his system rules out interference in an implicit way, by the nature of the way proofs are constructed.

A model for concurrent separation logic was first provided by Stephen Brookes in a companion paper to O'Hearn's. The soundness of the logic had been a difficult problem, and in fact a counterexample of John Reynolds had shown the unsoundness of an earlier, unpublished version of the logic; the issue raised by Reynolds's example is described briefly in O'Hearn's paper, and more thoroughly in Brookes's.

At first it appeared that CSL was well suited to what Dijkstra had called loosely connected processes, but perhaps not to fine-grained concurrent algorithms with significant interference. However, gradually it was realized that the basic approach of CSL was considerably more powerful than first envisaged, if one employed non-standard models of the logical connectives and even the Hoare triples.

By suitable choice of separation algebra, it was surprisingly found that the proof rules of abstract versions of concurrent separation logic could be used to reason about interfering concurrent processes, for example by encoding the rely-guarantee technique which had been originally proposed to reason about interference; in this work the elements of the model were considered not resources, but rather "views" of the program state, and a non-standard interpretation of Hoare triples accompanies the non-standard reading of pre and postconditions. Finally, CSL-style principles have been used to compose reasoning about program histories instead of program states, in order to provide modular techniques for reasoning about fine-grained concurrent algorithms.

Versions of CSL have been included in many interactive and semi-automatic (or "in-between") verification tools as described in the next section. A particularly significant verification effort is that of the μC/OS-II kernel mentioned there. But, although steps have been made, as of yet CSL-style reasoning has been included in comparatively few tools in the automatic program analysis category (and none mentioned in the next section).

O'Hearn and Brookes are co-recipients of the 2016 Gödel Prize for their invention of Concurrent Separation Logic.

### Fractional permissions

Plain concurrent separation logic is able to describe ownership transfer, wherein one thread may completely gives control over individual heap locations to another thread, but this isn't enough to reason about many concurrent programs—in particular, each heap cell may be shared by many threads so long as each thread only reads from the cell and does not write to it, or alternatively it may be written to so long as only one thread can do the writing.

This may be achieved by annotating each $\mapsto$ assertion with a fractional permission $\pi \in (0,1]$ as $e\,{\overset {\pi }{\mapsto }}\,e'$ . When *π* = 1, the thread has full ownership of the heap cell and therefore may write to it:

$\{x\,{\overset {1}{\mapsto }}\,\_\}\,[x]:=a\,\{x\,{\overset {1}{\mapsto }}\,a\}$

When *π* < 1, the thread only has shared access, and therefore may only read:

$\{x\,{\overset {\pi }{\mapsto }}\,v\}\,a:=[x]\,\{x\,{\overset {\pi }{\mapsto }}\,v\ast a=v\}$

Importantly, permissions may be infinitely split, allowing an arbitrary number of threads to read from the same location (with the fractional permission keeping track of when the number of threads has reduced to one again):

$x\,{\overset {\pi _{1}+\pi _{2}}{\mapsto }}\,v\iff x\,{\overset {\pi _{1}}{\mapsto }}\,v\ast x\,{\overset {\pi _{2}}{\mapsto }}\,v$

Note that the actual magnitudes of the permissions less than one are immaterial and only required for tracking purposes; a program should not concern itself over whether any given permission is 0.1 or 0.9, as it is able to read from the heap cell all the same.

To allow for two heaps to both consider the same memory location, some modification is required to the definition of heaps and their disjointness. In particular, every heap location is assigned a fractional permission (and thus $s,h\vdash e\,{\overset {\pi }{\mapsto }}\,e'$ semantically means that in heap *h*, location *e* has value *e'* with permission *π*), and two heaps are disjoint if, for every location that is in both heaps, their values are equal and the sum of their fractional permissions does not exceed one. The operation of merging two heaps will correspondingly add together permissions for those duplicated locations.

## Verification and program analysis tools

Tools for reasoning about programs fall on a spectrum from fully automatic program analysis tools, which do not require any user input, to interactive tools where the human is intimately involved in the proof process. Many such tools have been developed; the following list includes a few representatives in each category.

- **Automatic Program Analyses.** These tools typically look for restricted classes of bugs (e.g., memory safety errors) or attempt to prove their absence, but fall short of proving full correctness.
  - A current example is Facebook Infer, a static analysis tool for Java, C, and Objective-C based on separation logic and bi-abduction. As of 2015 hundreds of bugs per month were being found by Infer and fixed by developers before being shipped to Facebook's mobile apps.
  - Other examples include SpaceInvader (one of the first SL analyzers), Predator (which has won several verification competitions), MemCAD (which mixes shape and numerical properties) and SLAyer (from Microsoft Research, focussed on data structures found in device drivers).
- **Interactive Proof.** Proofs have been done using embeddings of Separation Logic into interactive theorem provers such as Rocq (previously known as *Coq*) and HOL (proof assistant). In comparison to the program analysis work, these tools require more in the way of human effort but prove deeper properties, up to functional correctness.
  - A proof of the FSCQ file system where the specification includes behaviour under crashes as well as normal operation. This work won the best paper award at the 2015 Symposium on Operating System Principles.
  - Verification of a large fragment of the Rust type system and some of its standard libraries in the RustBelt project using the Iris framework for separation logic in Rocq.
  - Verification of an OpenSSL implementation of a cryptographic authentication algorithm, utilizing verifiable C
  - Verification of key modules of a commercial OS kernel, the μC/OS-II kernel, the first commercial *pre-emptive* kernel to have been verified.
  - Other examples include the Ynot library for the Rocq; the Holfoot embedding of Smallfoot in HOL; Fine-grained Concurrent Separation Logic, and Bedrock (a Rocq library for low-level programming).
- **In Between.** Many tools require more user intervention than program analyses, in that they expect the user to input assertions such as pre/post specs for functions or loop invariants, but after this input is given they attempt to be fully or almost fully automatic; this mode of verification goes back to classic works in the 1970s such as J King's verifier, and the Stanford Pascal Verifier. This style of verifier has recently been called auto active verification, a term which intends to evoke the way of interacting with a verifier via an assert-check loop, analogous to the interaction between a programmer and a type-checker.
  - The very first Separation Logic verifier, Smallfoot, was in this in-between category. It required the user to input pre/post specs, loop invariants, and resource invariants for locks. It introduced a method of symbolic execution, as well as an automatic way to infer frame axioms. Smallfoot included Concurrent Separation Logic.
  - SmallfootRG is a verifier for a marriage of separation logic and the classic rely/guarantee method for concurrent programs.
  - Heap Hop implements a separation logic for message passing, following the ideas in Singularity (operating system).
  - VeriFast is an advanced current tool in the in-between category. It has demonstrated proofs ranging from object-oriented patterns to highly concurrent algorithms and to systems programs.
  - Viper is a state-of-the-art automated verification infrastructure for permission-based reasoning. It mainly consists of a programming language and two verification backends, one based on symbolic execution and another one on verification condition generation (VCG). Based on the Viper infrastructure, several frontends for various programming languages have emerged: Gobra for Go, Nagini for Python, Prusti for Rust, and VerCors for C, Java, OpenCL, and OpenMP. These frontends translate the frontend programming language into Viper to then use a Viper verification backend for proving the input program's correctness.
  - The Mezzo Programming Language and Asynchronous Liquid Separation Types include ideas related to CSL in the type system for a programming language. The idea to include separation in a type system has earlier examples in Alias Types and Syntactic Control of Interference.

The distinction between interactive and in-between verifiers is not a sharp one. For example, Bedrock strives for a high degree of automation, in what it terms mostly-automatic verification, where Verifast sometimes requires annotations that resemble the tactics (little programs) used in interactive verifiers.

## Decidability and complexity

The satisfiability problem for a quantifier-free, multi-sorted fragment of separation logic parameterized over the sorts of locations and data can be shown to be PSPACE-complete. An algorithm for solving this fragment in DPLL(T)-based SMT solvers has been integrated into cvc5. Extending this result, satisfiability for an analog of the Bernays–Schönfinkel class for separation logic with uninterpreted memory locations can also be shown to be PSPACE-complete, whereas the problem is undecidable with interpreted memory locations (e.g., integers) or further quantifier alternations
