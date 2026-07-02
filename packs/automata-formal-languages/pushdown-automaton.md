---
title: "Pushdown automaton"
source: https://en.wikipedia.org/wiki/Pushdown_automaton
domain: automata-formal-languages
license: CC-BY-SA-4.0
tags: automata, automaton, finite state machine, formal language, context-free grammar, turing machine
fetched: 2026-07-02
---

# Pushdown automaton

Classes of automata

In the theory of computation, a branch of theoretical computer science, a **pushdown automaton** (**PDA**) is a type of automaton that employs a stack.

Pushdown automata are used in theories about what can be computed by machines. They are more capable than finite-state machines but less capable than Turing machines (see below). Deterministic pushdown automata can recognize all deterministic context-free languages while nondeterministic ones can recognize all context-free languages, with the former often used in parser design.

The term "pushdown" refers to the fact that the stack can be regarded as being "pushed down" like a tray dispenser at a cafeteria, since the operations never work on elements other than the top element. A **stack automaton**, by contrast, does allow access to and operations on deeper elements. Stack automata can recognize a strictly larger set of languages than pushdown automata. A nested stack automaton allows full access, and also allows stacked values to be entire sub-stacks rather than just single finite symbols.

## Informal description

A finite-state machine only considers the input signal and the current state: it has no stack to work with and therefore is unable to access previous values of the input. It can only choose a new state, the result of following the transition. A **pushdown automaton (PDA)** differs from a finite state machine in two ways:

1. It can use the top of the stack to decide which transition to take.
2. It can manipulate the stack as part of performing a transition.

A pushdown automaton reads a given input string from left to right. In each step, it chooses a transition by indexing a table by input symbol, current state, and the symbol at the top of the stack. A pushdown automaton can also manipulate the stack, as part of performing a transition. The manipulation can be to push a particular symbol to the top of the stack, or to pop off the top of the stack. The automaton can alternatively ignore the stack, and leave it as it is.

Put together: Given an input symbol, current state, and stack symbol, the automaton can follow a transition to another state, and optionally manipulate (push or pop) the stack.

If, in every situation, at most one such transition action is possible, then the automaton is called a **deterministic pushdown automaton (DPDA)**. In general, if several actions are possible, then the automaton is called a **general**, or **nondeterministic**, **PDA**. A given input string may drive a nondeterministic pushdown automaton to one of several configuration sequences; if one of them leads to an accepting configuration after reading the complete input string, the latter is said to belong to the *language accepted by the automaton*.

## Formal definition

We use standard formal language notation: $\Gamma ^{*}$ denotes the set of finite-length strings over alphabet $\Gamma$ and $\varepsilon$ denotes the empty string.

A PDA is formally defined as a 7-tuple:

$M=(Q,\Sigma ,\Gamma ,\delta ,q_{0},Z,F)$ where

- Q is a finite set of *states*
- $\Sigma$ is a finite set which is called the *input alphabet*
- $\Gamma$ is a finite set which is called the *stack alphabet*
- $\delta$ is a finite subset of $Q\times (\Sigma \cup \{\varepsilon \})\times \Gamma \times Q\times \Gamma ^{*}$ , the *transition relation*
- $q_{0}\in Q$ is the *start state*
- $Z\in \Gamma$ is the *initial stack symbol*
- $F\subseteq Q$ is the set of *accepting states*

An element $(p,a,A,q,\alpha )\in \delta$ is a transition of M . It has the intended meaning that M , in state $p\in Q$ , on the input $a\in \Sigma \cup \{\varepsilon \}$ and with $A\in \Gamma$ as topmost stack symbol, may read a , change the state to q , pop A , replacing it by pushing $\alpha \in \Gamma ^{*}$ . The $(\Sigma \cup \{\varepsilon \})$ component of the transition relation is used to formalize that the PDA can either read a letter from the input, or proceed leaving the input untouched.

In many texts the transition relation is replaced by an (equivalent) formalization, where

- $\delta$ is the *transition function*, mapping $Q\times (\Sigma \cup \{\varepsilon \})\times \Gamma$ into finite subsets of $Q\times \Gamma ^{*}$

Here $\delta (p,a,A)$ contains all possible actions in state p with A on the stack, while reading a on the input. One writes for example $\delta (p,a,A)=\{(q,BA)\}$ precisely when $(q,BA)\in \{(q,BA)\},(q,BA)\in \delta (p,a,A),$ because $((p,a,A),\{(q,BA)\})\in \delta$ . Note that *finite* in this definition is essential.

### Computations

In order to formalize the semantics of the pushdown automaton, a description of the current situation is introduced. Any 3-tuple $(p,w,\beta )\in Q\times \Sigma ^{*}\times \Gamma ^{*}$ is called an *instantaneous description* (ID) of M , which includes the current state, the part of the input tape that has not been read, and the contents of the stack (top-most symbol written first). The transition relation $\delta$ defines the step-relation $\vdash _{M}$ of M on instantaneous descriptions. For instruction $(p,a,A,q,\alpha )\in \delta$ there exists a step $(p,ax,A\gamma )\vdash _{M}(q,x,\alpha \gamma )$ , for every $x\in \Sigma ^{*}$ and every $\gamma \in \Gamma ^{*}$ .

In general, pushdown automata are nondeterministic, meaning that in a given instantaneous description $(p,w,\beta )$ there may be several possible steps. Any of these steps can be chosen in a computation. With the above definition, in each step a single symbol (top of the stack) is always popped, and replaced with as many symbols as necessary. As a consequence, no step is defined when the stack is empty.

Computations of the pushdown automaton are sequences of steps. The computation starts in the initial state $q_{0}$ with the initial stack symbol Z on the stack, and a string w on the input tape—thus, with initial description $(q_{0},w,Z)$ .

There are two modes of accepting. The pushdown automaton either accepts by final state, which means that after reading its input the automaton reaches an accepting state (in F ), or else it accepts by empty stack ( $\varepsilon$ ), which means that after reading its input the automaton empties its stack. The first acceptance mode uses the internal memory (state), the second the external memory (stack).

Formally one defines

1. $L(M)=\{w\in \Sigma ^{*}|(q_{0},w,Z)\vdash _{M}^{*}(f,\varepsilon ,\gamma )$ with $f\in F$ and $\gamma \in \Gamma ^{*}\}$ (final state)
2. $N(M)=\{w\in \Sigma ^{*}|(q_{0},w,Z)\vdash _{M}^{*}(q,\varepsilon ,\varepsilon )$ with $q\in Q\}$ (empty stack)

Here $\vdash _{M}^{*}$ represents the reflexive and transitive closure of the step relation $\vdash _{M}$ , meaning any number of consecutive steps (zero, one or more).

For each single pushdown automaton, these two languages need have no relation; they may be equal, but usually this is not the case. A specification of the automaton should also include the intended mode of acceptance. Taken over all pushdown automata, both acceptance conditions define the same family of languages.

**Theorem.** For each pushdown automaton M one may construct a pushdown automaton $M'$ such that $L(M)=N(M')$ , and vice versa, for each pushdown automaton M one may construct a pushdown automaton $M'$ such that $N(M)=L(M')$

## Example

The following is the formal description of the PDA which recognizes the language $\{0^{n}1^{n}\mid n\geq 0\}$ by final state:

$M=(Q,\ \Sigma ,\ \Gamma ,\ \delta ,\ q_{0},\ Z,\ F)$ , where

- **states:** $Q=\{p,q,r\}$
- **input alphabet:** $\Sigma =\{0,1\}$
- **stack alphabet:** $\Gamma =\{A,Z\}$
- **start state:** $q_{0}=p$
- **start stack symbol:** Z
- **accepting states:** $F=\{r\}$

The transition relation $\delta$ consists of the following six instructions:

$(p,0,Z,p,AZ)$

,

$(p,0,A,p,AA)$

,

$(p,\epsilon ,Z,q,Z)$

,

$(p,\epsilon ,A,q,A)$

,

$(q,1,A,q,\epsilon )$

, and

$(q,\epsilon ,Z,r,Z)$

.

In words, the first two instructions say that in state p any time the symbol 0 is read, one A is pushed onto the stack. Pushing symbol A on top of another A is formalized as replacing top A by AA (and similarly for pushing symbol A on top of a Z).

The third and fourth instructions say that, at any moment the automaton may move from state p to state q.

The fifth instruction says that in state q, for each symbol 1 read, one A is popped.

Finally, the sixth instruction says that the machine may move from state q to accepting state r only when Z is the top stack symbol. In this PDA, that is equivalent to the stack consisting of a single Z, since Z is only used as the bottom-of-stack marker and no transition pushes another Z above it.

There seems to be no generally used representation for PDA. Here we have depicted the instruction $(p,a,A,q,\alpha )$ by an edge from state p to state q labelled by $a;A/\alpha$ (read a from input string; replace A at top of stack by $\alpha$ ).

### Explanation

The following illustrates how the above PDA computes on different input strings. The subscript M from the step symbol $\vdash$ is here omitted.

1. Input string = 0011. There are various computations, depending on the moment the move from state p to state q is made. Only one of these is accepting. $(p,0011,Z)\vdash (q,0011,Z)\vdash (r,0011,Z)$ The final state is accepting, but the input is not accepted this way as it has not been read. $(p,0011,Z)\vdash (p,011,AZ)\vdash (q,011,AZ)$ No further steps possible. $(p,0011,Z)\vdash (p,011,AZ)\vdash (p,11,AAZ)\vdash (q,11,AAZ)\vdash (q,1,AZ)\vdash (q,\epsilon ,Z)\vdash (r,\epsilon ,Z)$ Accepting computation: ends in accepting state, while complete input has been read.
2. Input string = 00111. Again there are various computations. None of these is accepting. $(p,00111,Z)\vdash (q,00111,Z)\vdash (r,00111,Z)$ The final state is accepting, but the input is not accepted this way as it has not been read. $(p,00111,Z)\vdash (p,0111,AZ)\vdash (q,0111,AZ)$ No further steps possible. $(p,00111,Z)\vdash (p,0111,AZ)\vdash (p,111,AAZ)\vdash (q,111,AAZ)\vdash (q,11,AZ)\vdash (q,1,Z)\vdash (r,1,Z)$ The final state is accepting, but the input is not accepted this way as it has not been (completely) read.

## Context-free languages

Every context-free grammar can be transformed into an equivalent nondeterministic pushdown automaton. The derivation process of the grammar is simulated in a leftmost way. Where the grammar rewrites a nonterminal, the PDA takes the topmost nonterminal from its stack and replaces it by the right-hand part of a grammatical rule (*expand*). Where the grammar generates a terminal symbol, the PDA reads a symbol from input when it is the topmost symbol on the stack (*match*). In a sense the stack of the PDA contains the unprocessed data of the grammar, corresponding to a pre-order traversal of a derivation tree.

Technically, given a context-free grammar, the PDA has a single state, 1, and its transition relation is constructed as follows.

1. $(1,\varepsilon ,A,1,\alpha )$ for each rule $A\to \alpha$ (*expand*)
2. $(1,a,a,1,\varepsilon )$ for each terminal symbol a (*match*)

The PDA accepts by empty stack. Its initial stack symbol is the grammar's start symbol.

For a context-free grammar in Greibach normal form, defining (1,γ) ∈ δ(1,*a*,*A*) for each grammar rule *A* → *a*γ also yields an equivalent nondeterministic pushdown automaton.

The converse, finding a grammar for a given PDA, is not that easy. The trick is to code two states of the PDA into the nonterminals of the grammar.

**Theorem.** For each pushdown automaton M one may construct a context-free grammar G such that $N(M)=L(G)$ .

The language of strings accepted by a deterministic pushdown automaton (DPDA) is called a deterministic context-free language. Not all context-free languages are deterministic. As a consequence, the DPDA is a strictly weaker variant of the PDA. Even for regular languages, there is a size explosion problem: for any recursive function f and for arbitrarily large integers n , there is a PDA of size n describing a regular language whose smallest DPDA has at least $f(n)$ states. For many non-regular PDAs, any equivalent DPDA would require an unbounded number of states.

A finite automaton with access to two stacks is a more powerful device, equivalent in power to a Turing machine. A linear bounded automaton is a device which is more powerful than a pushdown automaton but less so than a Turing machine.

## Turing machines

A pushdown automaton is computationally equivalent to a "restricted" Turing Machine (TM) with two tapes, which is restricted in the following manner. On the first tape, the TM can only read the input and move from left to right (i.e., it cannot make changes). On the second tape, it can only "push" and "pop" data; i.e., the TM can read, write, and move left and right on the second tape, with the restriction that the only action it can perform at each step is to either delete the left-most character in the string (pop) or add an extra character left to the left-most character in the string (push).

That a PDA is weaker than a TM can be boiled down to the fact that the "pop" procedure deletes some data. In order to make a PDA as strong as a TM, we need to save this lost data somewhere; this can be achieved by introducing a second stack. In the aforementioned TM model of pushdown automata, this is equivalent to a TM with *three* tapes, wherein the first tape is the read-only input tape, and both the second and third tapes are "push" and "pop" (stack) tapes. In order for such a PDA to simulate any given TM, we give the input of the PDA to the first tape, while keeping both the stacks empty; it then goes on to push all the input from the input tape onto the first stack. When the entire input is transferred to the first stack, operation proceeds as in a normal TM: moving right on the tape is the same as popping a symbol from the first stack and pushing a (possibly updated) symbol onto the second stack, and moving left corresponds to popping a symbol from the second stack and pushing a (possibly updated) symbol onto the first stack—hence, we now have a two-stack PDA that can simulate any TM.

## Generalization

A generalized pushdown automaton (GPDA) is a PDA that writes an entire string of some known length to the stack or removes an entire string from the stack in one step.

A GPDA is formally defined as a 6-tuple:

$M=(Q,\ \Sigma ,\ \Gamma ,\ \delta ,\ q_{0},\ F)$

where $Q,\Sigma \,,\Gamma \,,q_{0}$ , and ⁠ F ⁠ are defined the same way as a PDA.

$\,\delta$

:

$Q\times \Sigma _{\epsilon }\times \Gamma ^{*}\longrightarrow P(Q\times \Gamma ^{*})$

is the transition function.

Computation rules for a GPDA are the same as a PDA except that the $a_{i+1}$ 's and $b_{i+1}$ 's are now strings instead of symbols.

Pushdown automata and generalized pushdown automata are equivalent in that if a language is recognized by a PDA, it is also recognized by a GPDA, and vice versa.

One can formulate an analytic proof for the equivalence of pushdown automata and generalized pushdown automata using the following simulation:

Let $\delta (q_{1},w,x_{1}x_{2}\cdot x_{m})\longrightarrow (q_{2},y_{1}y_{2}...y_{n})$ be a transition of the GPDA, where:

$q_{1},q_{2}\in Q,w\in \Sigma _{\epsilon },x_{1},x_{2},\ldots ,x_{m}\in \Gamma ^{*},m\geq 0,y_{1},y_{2},\ldots ,y_{n}\in \Gamma ^{*},n\geq 0$

Construct the following transitions for the PDA:

${\begin{array}{lcl}\delta '(q_{1},w,x_{1})&\longrightarrow &(p_{1},\epsilon )\\\delta '(p_{1},\epsilon ,x_{2})&\longrightarrow &(p_{2},\epsilon )\\&\vdots &\\\delta '(p_{m-1},\epsilon ,x_{m})&\longrightarrow &(p_{m},\epsilon )\\\delta '(p_{m},\epsilon ,\epsilon )&\longrightarrow &(p_{m+1},y_{n})\\\delta '(p_{m+1},\epsilon ,\epsilon )&\longrightarrow &(p_{m+2},y_{n-1})\\&\vdots &\\\delta '(p_{m+n-1},\epsilon ,\epsilon )&\longrightarrow &(q_{2},y_{1}).\end{array}}$

## Stack automata

As a generalization of pushdown automata, Ginsburg, Greibach, and Harrison (1967) investigated **stack automata**, which may additionally step left or right in the input string (surrounded by special endmarker symbols to prevent slipping out), and step up or down in the stack in read-only mode. A stack automaton is called *nonerasing* if it never pops from the stack. The class of languages accepted by nondeterministic, nonerasing stack automata is *NSPACE*(*n*2), which is a superset of the context-sensitive languages. The class of languages accepted by deterministic, nonerasing stack automata is *DSPACE*(*n*⋅log(*n*)).

## Alternating pushdown automata

An **alternating pushdown automaton** (APDA) is a pushdown automaton with a state set

- $Q=Q_{\exists }\cup Q_{\forall }$ where $Q_{\exists }\cap Q_{\forall }=\emptyset$ .

States in $Q_{\exists }$ and $Q_{\forall }$ are called *existential* resp. *universal*. In an existential state an APDA nondeterministically chooses the next state and accepts if *at least one* of the resulting computations accepts. In a universal state APDA moves to all next states and accepts if *all* the resulting computations accept.

The model was introduced by Chandra, Kozen and Stockmeyer. Ladner, Lipton and Stockmeyer proved that this model is equivalent to EXPTIME i.e. a language is accepted by some APDA if, and only if, it can be decided by an exponential-time algorithm.

Aizikowitz and Kaminski introduced *synchronized alternating pushdown automata* (SAPDA) that are equivalent to conjunctive grammars in the same way as nondeterministic PDA are equivalent to context-free grammars.
