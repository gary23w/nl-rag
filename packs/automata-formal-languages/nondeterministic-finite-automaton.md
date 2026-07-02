---
title: "Nondeterministic finite automaton"
source: https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton
domain: automata-formal-languages
license: CC-BY-SA-4.0
tags: automata, automaton, finite state machine, formal language, context-free grammar, turing machine
fetched: 2026-07-02
---

# Nondeterministic finite automaton

In automata theory, a finite-state machine is called a deterministic finite automaton (DFA), if

- each of its transitions is *uniquely* determined by its source state and input symbol, and
- reading an input symbol is required for each state transition.

A **nondeterministic finite automaton** (**NFA**), or **nondeterministic finite-state machine**, does not need to obey these restrictions. In particular, every DFA is also an NFA. Sometimes the term **NFA** is used in a narrower sense, referring to an NFA that is *not* a DFA, but not in this article.

Using the subset construction algorithm, each NFA can be translated to an equivalent DFA; i.e., a DFA recognizing the same formal language. Like DFAs, NFAs only recognize regular languages.

NFAs were introduced in 1959 by Michael O. Rabin and Dana Scott, who also showed their equivalence to DFAs. NFAs are used in the implementation of regular expressions: Thompson's construction is an algorithm for compiling a regular expression to an NFA that can efficiently perform pattern matching on strings. Conversely, Kleene's algorithm can be used to convert an NFA into a regular expression (whose size is generally exponential in the input automaton).

NFAs have been generalized in multiple ways, e.g., nondeterministic finite automata with ε-moves, finite-state transducers, pushdown automata, alternating automata, ω-automata, and probabilistic automata. Besides the DFAs, other known special cases of NFAs are unambiguous finite automata (UFA) and self-verifying finite automata (SVFA).

## Informal introduction

There are at least two equivalent ways to describe the behavior of an NFA. The first way makes use of the nondeterminism in the name of an NFA. For each input symbol, the NFA transitions to a new state until all input symbols have been consumed. In each step, the automaton nondeterministically "chooses" one of the applicable transitions. If there exists at least one "lucky run", i.e. some sequence of choices leading to an accepting state after completely consuming the input, it is accepted. Otherwise, i.e. if no choice sequence at all can consume all the input and lead to an accepting state, the input is rejected.

In the second way, the NFA consumes a string of input symbols, one by one. In each step, whenever two or more transitions are applicable, it "clones" itself into appropriately many copies, each one following a different transition. If no transition is applicable, the current copy is in a dead end, and it "dies". If, after consuming the complete input, any of the copies is in an accept state, the input is accepted, else, it is rejected.

## Formal definition

For a more elementary introduction of the formal definition, see automata theory.

### Automaton

An *NFA* is represented formally by a 5-tuple, $(Q,\Sigma ,\delta ,q_{0},F)$ , consisting of

- a finite set of states Q ,
- a finite set of input symbols called the alphabet $\Sigma$ ,
- a transition function $\delta$  : $Q\times \Sigma \rightarrow {\mathcal {P}}(Q)$ ,
- an initial (or start) state $q_{0}\in Q$ , and
- a set of accepting (or final) states $F\subseteq Q$ .

Here, ${\mathcal {P}}(Q)$ denotes the power set of Q .

### Recognized language

Given an NFA $M=(Q,\Sigma ,\delta ,q_{0},F)$ , its recognized language is denoted by $L(M)$ , and is defined as the set of all strings over the alphabet $\Sigma$ that are accepted by M .

Loosely corresponding to the above informal explanations, there are several equivalent formal definitions of a string $w=a_{1}a_{2}...a_{n}$ being accepted by M :

- w is accepted if a sequence of states, $r_{0},r_{1},...,r_{n}$ , exists in Q such that:
  1. $r_{0}=q_{0}$
  2. $r_{i+1}\in \delta (r_{i},a_{i+1})$ , for $i=0,\ldots ,n-1$
  3. $r_{n}\in F$ .

In words, the first condition says that the machine starts in the start state

$q_{0}$

. The second condition says that given each character of string

w

, the machine will transition from state to state according to the transition function

$\delta$

. The last condition says that the machine accepts

w

if the last input of

w

causes the machine to halt in one of the accepting states. In order for

w

to be accepted by

M

, it is not required that every state sequence ends in an accepting state, it is sufficient if one does. Otherwise,

i.e.

if it is impossible at all to get from

$q_{0}$

to a state from

F

by following

w

, it is said that the automaton

rejects

the string. The set of strings

M

accepts is the

language

recognized

by

M

and this language is denoted by

$L(M)$

.

- Alternatively, w is accepted if $\delta ^{*}(q_{0},w)\cap F\not =\emptyset$ , where $\delta ^{*}:Q\times \Sigma ^{*}\rightarrow {\mathcal {P}}(Q)$ is defined recursively by:
  1. $\delta ^{*}(r,\varepsilon )=\{r\}$ where $\varepsilon$ is the empty string, and
  2. $\delta ^{*}(r,xa)=\bigcup _{r'\in \delta ^{*}(r,x)}\delta (r',a)$ for all $x\in \Sigma ^{*},a\in \Sigma$ .

In words,

$\delta ^{*}(r,x)$

is the set of all states reachable from state

r

by consuming the string

x

. The string

w

is accepted if some accepting state in

F

can be reached from the start state

$q_{0}$

by consuming

w

.

### Initial state

The above automaton definition uses a *single initial state*, which is not necessary. Sometimes, NFAs are defined with a set of initial states. There is an easy construction that translates an NFA with multiple initial states to an NFA with a single initial state, which provides a convenient notation.

## Example

|   |   |
|---|---|
|   |   |

The following automaton M, with a binary alphabet, determines if the input ends with a 1. Let $M=(\{p,q\},\{0,1\},\delta ,p,\{q\})$ where the transition function $\delta$ can be defined by this state transition table (cf. upper left picture):

${\begin{array}{|c|cc|}{\bcancel {{}_{\text{State}}\quad {}^{\text{Input}}}}&0&1\\\hline p&\{p\}&\{p,q\}\\q&\emptyset &\emptyset \end{array}}$

Since the set $\delta (p,1)$ contains more than one state, M is nondeterministic. The language of M can be described by the regular language given by the regular expression `(0|1)*1`.

All possible state sequences for the input string "1011" are shown in the lower picture.

The string is accepted by M since one state sequence satisfies the above definition; it does not matter that other sequences fail to do so. The picture can be interpreted in a couple of ways:

- In terms of the above "lucky-run" explanation, each path in the picture denotes a sequence of choices of M.
- In terms of the "cloning" explanation, each vertical column shows all clones of M at a given point in time, multiple arrows emanating from a node indicate cloning, a node without emanating arrows indicating the "death" of a clone.

The feasibility to read the same picture in two ways also indicates the equivalence of both above explanations.

- Considering the first of the above formal definitions, "1011" is accepted since when reading it M may traverse the state sequence $\langle r_{0},r_{1},r_{2},r_{3},r_{4}\rangle =\langle p,p,p,p,q\rangle$ , which satisfies conditions 1 to 3.
- Concerning the second formal definition, bottom-up computation shows that $\delta ^{*}(p,\varepsilon )=\{p\}$ , hence $\delta ^{*}(p,1)=\delta (p,1)=\{p,q\}$ , hence $\delta ^{*}(p,10)=\delta (p,0)\cup \delta (q,0)=\{p\}\cup \{\}$ , hence $\delta ^{*}(p,101)=\delta (p,1)=\{p,q\}$ , and hence $\delta ^{*}(p,1011)=\delta (p,1)\cup \delta (q,1)=\{p,q\}\cup \{\}$ ; since that set is not disjoint from $\{q\}$ , the string "1011" is accepted.

In contrast, the string "10" is rejected by M (all possible state sequences for that input are shown in the upper right picture), since there is no way to reach the only accepting state, q, by reading the final 0 symbol. While q can be reached after consuming the initial "1", this does not mean that the input "10" is accepted; rather, it means that an input string "1" would be accepted.

## Equivalence to DFA

A deterministic finite automaton (DFA) can be seen as a special kind of NFA, in which for each state and symbol, the transition function has exactly one state. Thus, it is clear that every formal language that can be recognized by a DFA can be recognized by an NFA.

Conversely, for each NFA, there is a DFA such that it recognizes the same formal language. The DFA can be constructed using the powerset construction.

This result shows that NFAs, despite their additional flexibility, are unable to recognize languages that cannot be recognized by some DFA. It is also important in practice for converting easier-to-construct NFAs into more efficiently executable DFAs. However, if the NFA has *n* states, the resulting DFA may have up to 2*n* states, which sometimes makes the construction impractical for large NFAs.

## NFA with ε-moves

Nondeterministic finite automaton with ε-moves (NFA-ε) is a further generalization to NFA. In this kind of automaton, the transition function is additionally defined on the empty string ε. A transition without consuming an input symbol is called an ε-transition and is represented in state diagrams by an arrow labeled "ε". ε-transitions provide a convenient way of modeling systems whose current states are not precisely known: i.e., if we are modeling a system and it is not clear whether the current state (after processing some input string) should be q or q', then we can add an ε-transition between these two states, thus putting the automaton in both states simultaneously.

### Formal definition

An *NFA-ε* is represented formally by a 5-tuple, $(Q,\Sigma ,\delta ,q_{0},F)$ , consisting of

- a finite set of states Q
- a finite set of input symbols called the alphabet $\Sigma$
- a transition function $\delta :Q\times (\Sigma \cup \{\varepsilon \})\rightarrow {\mathcal {P}}(Q)$
- an *initial* (or *start*) state $q_{0}\in Q$
- a set of states F distinguished as *accepting* (or *final*) *states* $F\subseteq Q$ .

Here, ${\mathcal {P}}(Q)$ denotes the power set of Q and $\varepsilon$ denotes empty string.

### ε-closure of a state or set of states

For a state $q\in Q$ , let $E(q)$ denote the set of states that are reachable from q by following ε-transitions in the transition function $\delta$ , i.e., $p\in E(q)$ if there is a sequence of states $q_{1},...,q_{k}$ such that

- $q_{1}=q$ ,
- $q_{i+1}\in \delta (q_{i},\varepsilon )$ for each $1\leq i<k$ , and
- $q_{k}=p$ .

$E(q)$ is known as the **epsilon closure**, (also **ε-closure**) of q .

The ε-closure of a set P of states of an NFA is defined as the set of states reachable from any state in P following ε-transitions. Formally, for $P\subseteq Q$ , define $E(P)=\bigcup \limits _{q\in P}E(q)$ .

### Extended transition function

Similar to NFA without ε-moves, the transition function $\delta$ of an NFA-ε can be extended to strings. Informally, $\delta ^{*}(q,w)$ denotes the set of all states the automaton may have reached when starting in state $q\in Q$ and reading the string $w\in \Sigma ^{*}.$ The function $\delta ^{*}:Q\times \Sigma ^{*}\rightarrow {\mathcal {P}}(Q)$ can be defined recursively as follows.

- $\delta ^{*}(q,\varepsilon )=E(q)$ , for each state $q\in Q,$ and where E denotes the epsilon closure;

Informally:

Reading the empty string may drive the automaton from state

q

to any state of the epsilon closure of

$q.$

- ${\textstyle \delta ^{*}(q,wa)=\bigcup _{r\in \delta ^{*}(q,w)}E(\delta (r,a)),}$ for each state $q\in Q,$ each string $w\in \Sigma ^{*}$ and each symbol $a\in \Sigma .$

Informally:

Reading the string

w

may drive the automaton from state

q

to any state

r

in the recursively computed set

$\delta ^{*}(q,w)$

; after that, reading the symbol

a

may drive it from

r

to any state in the epsilon closure of

$\delta (r,a).$

The automaton is said to accept a string w if

$\delta ^{*}(q_{0},w)\cap F\neq \emptyset ,$

that is, if reading w may drive the automaton from its start state $q_{0}$ to some accepting state in $F.$

### Example

Let M be a NFA-ε, with a binary alphabet, that determines if the input contains an even number of 0s or an even number of 1s. Note that 0 occurrences is an even number of occurrences as well.

In formal notation, let $M=(\{S_{0},S_{1},S_{2},S_{3},S_{4}\},\{0,1\},\delta ,S_{0},\{S_{1},S_{3}\})$ where the transition relation $\delta$ can be defined by this state transition table:

| InputState | 0 | 1 | ε |
|---|---|---|---|
| *S*0 | {} | {} | {*S*1, *S*3} |
| *S*1 | {*S*2} | {*S*1} | {} |
| *S*2 | {*S*1} | {*S*2} | {} |
| *S*3 | {*S*3} | {*S*4} | {} |
| *S*4 | {*S*4} | {*S*3} | {} |

M can be viewed as the union of two DFAs: one with states $\{S_{1},S_{2}\}$ and the other with states $\{S_{3},S_{4}\}$ . The language of M can be described by the regular language given by this regular expression $(1^{*}01^{*}01^{*})^{*}\cup (0^{*}10^{*}10^{*})^{*}$ . We define M using ε-moves but M can be defined without using ε-moves.

### Equivalence to NFA

To show NFA-ε is equivalent to NFA, first note that NFA is a special case of NFA-ε, so it remains to show for every NFA-ε, there exists an equivalent NFA.

Given an NFA with epsilon moves $M=(Q,\Sigma ,\delta ,q_{0},F),$ define an NFA $M'=(Q,\Sigma ,\delta ',q_{0},F'),$ where

$F'={\begin{cases}F\cup \{q_{0}\}&{\text{ if }}E(q_{0})\cap F\neq \{\}\\F&{\text{ otherwise }}\\\end{cases}}$

and

$\delta '(q,a)=\delta ^{*}(q,a)$

for each state

$q\in Q$

and each symbol

$a\in \Sigma ,$

using the extended transition function

$\delta ^{*}$

defined above.

One has to distinguish the transition functions of M and $M',$ viz. $\delta$ and $\delta ',$ and their extensions to strings, $\delta ^{*}$ and $\delta '^{*},$ respectively. By construction, $M'$ has no ε-transitions.

One can prove that $\delta '^{*}(q_{0},w)=\delta ^{*}(q_{0},w)$ for each string $w\neq \varepsilon$ , by induction on the length of $w.$

Based on this, one can show that $\delta '^{*}(q_{0},w)\cap F'\neq \{\}$ if, and only if, $\delta ^{*}(q_{0},w)\cap F\neq \{\},$ for each string $w\in \Sigma ^{*}:$

- If $w=\varepsilon ,$ this follows from the definition of $F'.$
- Otherwise, let $w=va$ with $v\in \Sigma ^{*}$ and $a\in \Sigma .$

From

$\delta '^{*}(q_{0},w)=\delta ^{*}(q_{0},w)$

and

$F\subseteq F',$

we have

$\delta '^{*}(q_{0},w)\cap F'\neq \{\}\;\Leftarrow \;\delta ^{*}(q_{0},w)\cap F\neq \{\};$

we still have to show the "

$\Rightarrow$

" direction.

- If $\delta '^{*}(q_{0},w)$ contains a state in $F'\setminus \{q_{0}\},$ then $\delta ^{*}(q_{0},w)$ contains the same state, which lies in F .
- If $\delta '^{*}(q_{0},w)$ contains $q_{0},$ and $q_{0}\in F,$ then $\delta ^{*}(q_{0},w)$ also contains a state in $F,$ viz. $q_{0}.$
- If $\delta '^{*}(q_{0},w)$ contains $q_{0},$ and $q_{0}\not \in F,$ but $q_{0}\in F',$ then there exists a state in $E(q_{0})\cap F$ , and the same state must be in ${\textstyle \delta ^{*}(q_{0},w)=\bigcup _{r\in \delta ^{*}(q,v)}E(\delta (r,a)).}$

Since NFA is equivalent to DFA, NFA-ε is also equivalent to DFA.

## Closure properties

The set of languages recognized by NFAs is closed under the following operations. These closure operations are used in Thompson's construction algorithm, which constructs an NFA from any regular expression. They can also be used to prove that NFAs recognize exactly the regular languages.

- Union (cf. picture); that is, if the language *L*1 is accepted by some NFA *A*1 and *L*2 by some *A*2, then an NFA *A*u can be constructed that accepts the language *L*1∪*L*2.
- Intersection; similarly, from *A*1 and *A*2 an NFA *A*i can be constructed that accepts *L*1∩*L*2.
- Concatenation
- Negation; similarly, from *A*1 an NFA *A*n can be constructed that accepts Σ*\*L*1.
- Kleene closure

Since NFAs are equivalent to nondeterministic finite automaton with ε-moves (NFA-ε), the above closures are proved using closure properties of NFA-ε.

## Properties

The machine starts in the specified initial state and reads in a string of symbols from its alphabet. The automaton uses the state transition function Δ to determine the next state using the current state, and the symbol just read or the empty string. However, "the next state of an NFA depends not only on the current input event, but also on an arbitrary number of subsequent input events. Until these subsequent events occur it is not possible to determine which state the machine is in". If, when the automaton has finished reading, it is in an accepting state, the NFA is said to accept the string, otherwise it is said to reject the string.

The set of all strings accepted by an NFA is the language the NFA accepts. This language is a regular language.

For every NFA a deterministic finite automaton (DFA) can be found that accepts the same language. Therefore, it is possible to convert an existing NFA into a DFA for the purpose of implementing a (perhaps) simpler machine. This can be performed using the powerset construction, which may lead to an exponential rise in the number of necessary states. For a formal proof of the powerset construction, please see the Powerset construction article.

## Implementation

There are many ways to implement an NFA:

- Convert to the equivalent DFA. In some cases this may cause exponential blowup in the number of states.
- Keep a set data structure of all states which the NFA might currently be in. On the consumption of an input symbol, unite the results of the transition function applied to all current states to get the set of next states; if ε-moves are allowed, include all states reachable by such a move (ε-closure). Each step requires at most *s*2 computations, where *s* is the number of states of the NFA. On the consumption of the last input symbol, if one of the current states is a final state, the machine accepts the string. A string of length *n* can be processed in time *O*(*ns*2), and space *O*(*s*).
- Create multiple copies. For each *n* way decision, the NFA creates up to *n*−1 copies of the machine. Each will enter a separate state. If, upon consuming the last input symbol, at least one copy of the NFA is in the accepting state, the NFA will accept. (This, too, requires linear storage with respect to the number of NFA states, as there can be one machine for every NFA state.)
- Explicitly propagate tokens through the transition structure of the NFA and match whenever a token reaches the final state. This is sometimes useful when the NFA should encode additional context about the events that triggered the transition. (For an implementation that uses this technique to keep track of object references have a look at Tracematches.)

## Complexity

- One can solve in linear time the emptiness problem for NFA, i.e., check whether the language of a given NFA is empty. To do this, we can simply perform a depth-first search from the initial state and check if some final state can be reached.
- It is PSPACE-complete to test, given an NFA, whether it is *universal*, i.e., if there is a string that it does not accept. As a consequence, the same is true of the *inclusion problem*, i.e., given two NFAs, is the language of one a subset of the language of the other.
- Given as input an NFA *A* and an integer n, the counting problem of determining how many words of length *n* are accepted by *A* is intractable; it is **#P**-hard. In fact, this problem is complete (under parsimonious reductions) for the complexity class SpanL.

## Application of NFA

NFAs and DFAs are equivalent in that if a language is recognized by an NFA, it is also recognized by a DFA and vice versa. The establishment of such equivalence is important and useful. It is useful because constructing an NFA to recognize a given language is sometimes much easier than constructing a DFA for that language. It is important because NFAs can be used to reduce the complexity of the mathematical work required to establish many important properties in the theory of computation. For example, it is much easier to prove closure properties of regular languages using NFAs than DFAs.
