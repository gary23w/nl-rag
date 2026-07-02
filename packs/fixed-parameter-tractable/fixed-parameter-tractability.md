---
title: "Parameterized complexity"
source: https://en.wikipedia.org/wiki/Fixed-parameter_tractability
domain: fixed-parameter-tractable
license: CC-BY-SA-4.0
tags: fixed parameter tractable, bounded search tree, iterative compression, color coding technique
fetched: 2026-07-02
---

# Parameterized complexity

(Redirected from

Fixed-parameter tractability

)

In computer science, **parameterized complexity** is a branch of computational complexity theory that focuses on classifying computational problems according to their inherent difficulty with respect to *multiple* parameters of the input or output. The complexity of a problem is then measured as a function of those parameters. This allows the classification of NP-hard problems on a finer scale than in the classical setting, where the complexity of a problem is only measured as a function of the number of bits in the input. This appears to have been first demonstrated in Gurevich, Stockmeyer & Vishkin (1984). The first systematic work on parameterized complexity was done by Downey & Fellows (1999).

The existence of efficient, exact, and deterministic solving algorithms for NP-complete, or otherwise NP-hard, problems is considered unlikely, if input parameters are not fixed; all known solving algorithms for these problems require time that is exponential (so in particular super-polynomial) in the total size of the input. However, some problems can be solved by algorithms that are exponential only in the size of a fixed parameter while polynomial in the size of the input.

Under the assumption that P ≠ NP, there exist many natural problems that require super-polynomial running time when complexity is measured in terms of the input size only but that are computable in a time that is polynomial in the input size and exponential or worse in a parameter k. Hence, if k is fixed at a small value and the growth of the function over k is relatively small then such problems can still be considered "tractable" despite their traditional classification as "intractable".

Such an algorithm is called a fixed-parameter tractable (FPT) algorithm, because the problem can be solved efficiently (i.e., in polynomial time) for constant values of the fixed parameter. A parameterized problem that allows for such an FPT algorithm is said to be a **fixed-parameter tractable** problem and belongs to the class FPT, and the early name of the theory of parameterized complexity was **fixed-parameter tractability**.

## Setup

Many problems have the following form: given an object x and a nonnegative integer k, does x have some property that depends on k?

For instance, for the vertex cover problem, the parameter can be the number of vertices in the cover. The minimal vertex cover problem asks:

In many applications, for example when modelling error correction, one can assume the parameter to be "small" compared to the total input size. Then it is challenging to find an algorithm that is exponential *only* in k, and not in the input size.

In this way, parameterized complexity can be seen as *two-dimensional* complexity theory. This concept is formalized as follows:

A

parameterized problem

is a language

$L\subseteq \Sigma ^{*}\times \mathbb {N}$

, where

$\Sigma$

is a finite alphabet. The second component is called the

parameter

of the problem.

A parameterized problem

L

is

fixed-parameter tractable

if the question "

$(x,k)\in L$

?" can be decided in running time

$f(k)\cdot |x|^{O(1)}$

, where

f

is an arbitrary function depending only on

k

. The corresponding

complexity class

is called

FPT

.

A parameterized problem uses the

natural parameter

when its parameter is the size of the solution to the problem.

For example, there is an algorithm that solves the vertex cover problem in $O(kn+1.274^{k})$ time, where n is the number of vertices and k is the size of the vertex cover. This means that vertex cover is fixed-parameter tractable with the size of the solution as the parameter (its natural parameter).

## Complexity classes

### FPT

**FPT** (fixed parameter tractable) is the class of decision problems decidable in deterministic time $f(k)\cdot {|x|}^{O(1)}$ , where f is a computable function. Typically, this function is thought of as single exponential, such as $2^{O(k)}$ , but the definition admits functions that grow even faster. This is essential for a large part of the early history of this class. The crucial part of the definition is to exclude functions of the form $f(n,k)$ , such as $k^{n}$ .

The class **FPL** (fixed parameter linear) is the class of problems solvable in time $f(k)\cdot |x|$ for some computable function f. FPL is thus a subclass of FPT. An example is the Boolean satisfiability problem, parameterised by the number of variables. A given formula of size m with k variables can be checked by brute force in time $O(2^{k}m)$ . A vertex cover of size k in a graph of order n can be found in time $O(2^{k}n)$ , so the vertex cover problem is also in FPL.

An example of a problem that is thought not to be in FPT is graph coloring parameterised by the number of colors. It is known that 3-coloring is NP-hard, and an algorithm for graph k-coloring in time $f(k)n^{O(1)}$ for $k=3$ would run in polynomial time in the size of the input. Thus, if graph coloring parameterised by the number of colors were in FPT, then P = NP.

There are a number of alternative definitions of FPT. For example, the running-time requirement can be replaced by $f(k)+|x|^{O(1)}$ . Also, a parameterised problem is in FPT if it has a so-called kernel. Kernelization is a preprocessing technique that reduces the original instance to its "hard kernel", a possibly much smaller instance that is equivalent to the original instance but has a size that is bounded by a function in the parameter.

FPT is closed under a parameterised notion of reductions called ***fpt-reductions***. We say that one parameterized problem L fpt-reduces to $L'$ iff there exists two functions $(x,k)\mapsto x',k\mapsto k'$ , such that

- $(x,k)\in L$ iff $(x',k')\in L'$
- $(x,k)\mapsto x'$ is itself fixed parameter tractable.
  - That is, there exists a constant c , and a function $k\mapsto k''$ , such that $(x,k)\mapsto x'$ is computable in time $\leq k''|x|^{c}$

Obviously, FPT contains all polynomial-time computable problems. Moreover, it contains all optimisation problems in NP that allow an efficient polynomial-time approximation scheme (EPTAS).

### XP

**XP** is the class of parameterized problems that can be solved in time $n^{f(k)}$ for some computable function f.

These problems are called slicewise polynomial, in the sense that each "slice" of fixed *k* has a polynomial-time algorithm, although with a possibly different exponent for each *k*. Compare this with FPT, which merely allows a different constant prefactor for each value of k.

XP strictly contains FPT by diagonalization.

### para-NP

**para-NP** is the class of decision problems decidable in nondeterministic time $f(k)\cdot |x|^{O(1)}$ for some computable function f.

${\textsf {FPT}}={\textsf {para-NP}}$ if and only if ${\textsf {P}}={\textsf {NP}}$ .

A problem is **para-NP-hard** if it is ${\textsf {NP}}$ -hard already for a constant value of the parameter. That is, there is a "slice" of fixed k that is ${\textsf {NP}}$ -hard. A parameterized problem that is ${\textsf {para-NP}}$ -hard cannot belong to the class ${\textsf {XP}}$ , unless ${\textsf {P}}={\textsf {NP}}$ . A classic example of a ${\textsf {para-NP}}$ -hard parameterized problem is graph coloring, parameterized by the number k of colors, which is already ${\textsf {NP}}$ -hard for $k=3$ (see Graph coloring#Computational complexity).

## Hierarchies

In the parameterized complexity theory, there are some hierarchies of complexity classes. Each such class is closed under fpt-reduction. The most important ones are the ***W* hierarchy** and the ***A* hierarchy**.

### Preliminary definitions

In general, there are two ways to define a complexity class: machine-theoretically and logically. In machine theory, a class is defined as the set of decision problems solvable by a class of machines. In logic, a class is defined as the set of decision problems definable by a class of logical formulas.

#### Boolean circuits

The **Hamming weight** (**weight** for short) of a binary string is the number of ones appearing in it.

A Boolean circuit is an acyclic directed graph where the nodes are one of the following gates: AND, OR, NOT. A small gate is a gate with fan-in 0, 1, or 2. Other gates are big. The **weft** is the largest number of big gates achievable on any path from an input to the output. The **depth** is the largest number of gates (small or big) achievable on any path from an input to the output. By definition, weft ≤ depth.

A Boolean circuit is **monotone** iff it uses no NOT gate. A Boolean circuit is **antimonotone** iff it is of the form $\phi (\neg x_{1},\dots ,\neg x_{n})$ where $x_{1},\dots ,x_{n}$ are all its inputs, and $\phi$ is monotone.

#### Finite model theory

Given any:

- ${\mathcal {L}}$ , a first-order logical language with a finite set of relation symbols,
- $\Gamma$ , a set of first-order logical formulas in that language,

we define $\operatorname {p-MC} (\Gamma )$ to be the **parameterized model checking** problem for this tuple. Each problem instance is:

- Input: $\phi \in \Gamma$ , and a finite model A for the language ${\mathcal {L}}$
- Parameter: $|\phi |$
- Output: Whether $A\models \phi$

A $\Sigma _{t}$ formula is of the form $\exists x_{1,1:m_{1}}\forall x_{2,1:m_{2}}\dots Qx_{t,1:m_{t}}\psi (x)$ , such that the quantifiers are *alternating* between existence and for-all, and the formula inside $\psi (x)$ is quantifier-free (that is, written with just variables, Boolean connectives, and relations).

A $\Sigma _{t,s}$ formula is of the form $\exists x_{1,1:m_{1}}\forall x_{2,1:m_{2}}\dots Qx_{t,1:m_{t}}\psi (x)$ , with the extra condition that $m_{2}\leq s,m_{3}\leq s,\dots ,m_{t}\leq s$ .

### Definition

Machine-theoretically, a parameterized problem is in the class *W[w][d]*, if there is a fpt-reduction of the problem as follows:

- There exists constant integers $w,d$ , such that
- every instance $(x,k)$ is transformed in fpt-time to a Boolean circuit that has weft at most *w*, and depth at most *d*,
- $(x,k)\in L$ if and only if the circuit has a satisfying assignment of weight *k*.

Here we see that "W" stands for "weight". Note that in the above definition, $w,d$ are independent of $(x,k)$ , but the circuit itself depends on $(x,k)$ , and may change if one changes either x or k .

The class *W[w]* is then defined as their union: $W[w][1]\subset W[w][2]\subset \dots \subset W[w]:=\bigcup _{d\geq 1}W[w][d]$ More succinctly, *W[w]* is the set of problems fpt-reducible to a family of instance-specific Boolean circuits with weft $\leq w$ and depth bounded by some problem-specific constant.

A **normalized circuit** of weft *w* and depth *d* is a circuit, where the first $d-w$ layers contain only small gates, and the last w layers contain alternating big gates of AND and OR. One can iterate the associative laws and de Morgan distribution laws to normalize the circuit in fpt-time. Therefore, without loss of generality, we can consider only normalized circuits.

Model-theoretically, the class *W[t]* is defined as the class of problems fpt-reducible to $\operatorname {p-MC} (\Sigma _{t,1})$ .

While the *W* hierarchy is a hierarchy contained in NP, the *A* hierarchy more closely mimics the polynomial-time hierarchy from classical complexity. Machine-theoretically, the A hierarchy of problems are defined as problems that are fpt-reducible to computations by certain kinds of alternating Turing machines. The "A" stands for "alternating".

Model-theoretically, the class *A[t]* is defined as the class of problems fpt-reducible to $\operatorname {p-MC} (\Sigma _{t})$ .

For example, the *k*-clique problem can be specified as a model checking problem. The language has a single binary relation E , where $E(x,y)$ means " $x,y$ share an edge". Then, a finite model A is a graph, and it has a *k*-clique iff $A\models \phi _{k}$ , where $\phi _{k}:=\exists x_{1:k},\bigwedge _{1\leq i<j\leq n}E(x_{i},x_{j})$ This shows that the *k*-clique problem is in $A[1]$ .

A problem is ***A[i]*-complete** if it is *A[i]*, and any *A[i]* problem fpt-reduces to it.

### Basic properties

By definition, $W[0]\subset W[1]\subset \cdots ,\quad W[i]\subset A[i],\quad A[0]\subset A[1]\subset \cdots$ ${\mathsf {FPT}}=W[0]=A[0]$ :

- $W[0]=A[0]$ since $\Sigma _{0}$ has no quantifiers at all, so there is no difference between $\Sigma _{0}$ and $\Sigma _{0,1}$ .
- ${\mathsf {FPT}}\subset W[0]$ . For any FPT problem L can be trivially fpt-reduced thus: Solve the problem $(x,k)\in L$ in fpt-time, then output a trivial Yes/No circuit that does nothing except output the correct Boolean.
- ${\mathsf {FPT}}\supset W[0]$ . For any W[0] problem L , and any problem-instance $c\in L$ , the circuitry c has 0 weft and $\leq d$ depth, where d is fixed. Therefore, the output is determined by up to $2^{d}$ inputs. All other inputs are free for use. Therefore, one simply brute-force compute all $2^{2^{d}}$ possible inputs. If a certain input has weight k' and makes the circuit output True, then check if there are still enough inputs to fill the weight: $\#({\text{inputs of }}c)-2^{d}\geq k-k'$ .

$W[1]=A[1]$ .

### *W[1]*

Intuitively, problems in W[1] class can be interpreted of the form: Is there an object of size *k* with a certain locally-checkable property? In formula, it would be of the form $\bigvee _{u_{1},\dots ,u_{k}}({\text{object constructed according to }}u_{1},\dots ,u_{k}{\text{ has a certain local property}})$ In fact, *W[1]* collapses to *W[1, 2]*, the class of problems fpt-reducible to Boolean circuits of the form $\bigwedge _{i}(x_{i,1}\lor x_{i,2})$ . That is, a big AND over many OR of fan-in 2.

Examples of *W[1]*-complete problems include:

- Independent set
  - Input: a graph *G*
  - Parameter: an integer *k*
  - Output: Whether *G* contains an independent set of size *k*
- Clique
  - Input: a graph *G*
  - Parameter: an integer *k*
  - Output: Whether *G* contains a clique of size *k*
- Bipartite nonblocker
  - Input: a bipartite graph $(V_{1},V_{2},E)$
  - Parameter: an integer *k*
  - Output: Whether there exists a subset $S\subset V_{1}$ of size *k*, such that any $v\in V_{2}$ has a neighbor $u\not \in S$ . In other words, S does not block $V_{2}$ .
- Weight-*k* 2-satisfiability
  - Input: a conjunctive normal formula of form $\bigwedge _{i}(p_{i,1}\lor p_{i,2})$ , where *i* ranges over clauses.
  - Parameter: an integer *k*
  - Output: Whether there exists a weight-k satisfying assignment to the formula.
- Short Turing machine problem.
  - Input: nondeterministic Turing machine *M*, a string *x*, an integer *k*.
  - Output: Whether there exists one computational path, with which *M* accepts *x* in at most *k* steps.

Note that the plain nonblocker problem is FPT.

Note on the nondeterministic Turing machine. The machine may be specified by one of any of the standard formulations. One usually considers the one-tape Turing machine, but the short Turing machine problem remains *W[1]* even if we allow with *f*(*k*) tapes and even *f*(*k*) of *f*(*k*)-dimensional tapes, but even with this extension, the restriction to *f*(*k*) tape alphabet size is FPT. Crucially, because the machine *M* itself is part of the problem input, the input size *n* is bigger than the number of states of *M*. In this way, the Turing machine can take one of n possible computation paths per step, accessing $n^{O(k)}$ steps in total within time *k*. Thus, we see that *W[1]* is not obviously contained within *FPT*.

The independent set problem can be encoded thus. Given each graph $(V,E)$ , its independent set problem is encoded by the following weft-1 Boolean circuit: $\Phi _{\text{IS}}(V,E):=\bigwedge _{\{u,v\}\in E}(\neg x_{u}\lor \neg x_{v})$ where E is the set of edges in the graph. The graph has an independent set of size *k* iff there is a weight-*k* input to its Boolean circuit, such that it outputs 1.

The clique problem can be coded as $\Phi _{\text{clique}}(V,E):=\bigwedge _{\{u,v\}\subset V,u\neq v,\{u,v\}\not \in E}(\neg x_{u}\lor \neg x_{v})$ It checks that any pair vertices that don't make an edge cannot be chosen, so any chosen set of vertices is forced to be a clique.

The short Turing machine problem can be converted to a Boolean formula using the same proof idea as of the Cook–Levin theorem, which shows SAT is NP-complete by coding Turing machine computational traces as Boolean formulas. The following proof is from . Specifically, define the propositional variables:

- $s_{t,i,j,a,b}$ : at time *t*, the Turing machine is in state *i*, and transitions to state *j*, reading *a*, and writing *b*,
- $y_{t,p,a,b}$ : at time *t*, the tape position *p* has symbol *a*, and at time *(t+1)* has symbol *b*.

Of the indices, time *t* and tape position *p* range over *1:k*, The ranges of the indices to the Turing machine state *i, j*, transition *m*, and symbols *a, b* are determined by the description of the machine M, but they are both bounded within *1:n*.

Then, the formula $\Phi _{{\text{STM}},k}(M,x)$ is a conjunction of clauses enforcing the following constraints:

- Every Turing machine state transition is not disallowed by the nondeterministic transition rule. These look like $s_{t,i,j,a,b}\to \neg s_{t+1,i',j',a',b'}$ , in other words, $\neg s_{t,i,j,a,b}\lor \neg s_{t+1,i',j',a',b'}$ . There are $O(kn^{4})$ such clauses.
- The Turing machine cannot be at two positions at a time, and cannot make two transitions at a time.
- Every tape cell state transition is not disallowed by the nondeterministic transition rule.
- Every tape cell state cannot have two symbols at a time.
- At time 0, the Turing machine is not out of its initial state and position, and *x* is not unwritten on the tape.
- The Turing machine is not in an unaccepting state at time *k*.

A computational trace through the Turing machine is then fully specified by setting *k* variables of $s_{t,i,j,a,b}$ to True to indicate the Turing machine state transitions at each time, and setting $k^{2}$ variables of $y_{t,p,a,b}$ to True to indicate the tape state transition at each time. This reduces the short Turing machine problem to a problem of finding a weight- $(k+k^{2})$ satisfying assignment to a weft-1, depth-2, antimonotone Boolean circuit.

### *W[2]*

*W[2]* problems are intuitively of the form: Guess an object of size *k*, perform some local processing on the object, then perform one global processing.

Examples of *W*[2]-complete problems include

- deciding if a given graph contains a dominating set of size *k.*
- deciding if a given nondeterministic multi-tape Turing machine accepts within *k* steps ("short multi-tape Turing machine acceptance" problem). Crucially, the branching is allowed to depend on *n* (like the W[1] variant), as is the number of tapes. An alternate *W*[2]-complete formulation allows only single-tape Turing machines, but the alphabet size may depend on *n*.

The dominating set problem has formula $\Psi _{\text{dom}}(V,E)=\bigwedge _{u\in V}\bigvee _{v\in \operatorname {Neighbor} [u]}x_{v}$ .

### *W[i]*

Some problems are known to be *W[i]*-complete, though they are in a computationally generic form, and are usually studied within parameterized complexity theory itself. Empirically, as of 2013, almost all naturally-occurring parameterized problems that they have studied, turned out to be *W[0]*-complete, *W[1]*-complete, or *W[2]*-complete. The following are usually used:

- Weighted *i*-Normalized Satisfiability: Given a Boolean formula, written as an AND of ORs of ANDs of ... of possibly negated variables, with $i+1$ layers of alternating ANDs or ORs, can it be satisfied by setting exactly *k* variables to 1?
  - Proof sketch: Any *W[i]*-circuit can be normalized in fpt-time by iterating association law and de Morgan distributive law, thus showing this problem is *W[i]*-complete.
- If *i>0* is even, then
  - ${\text{monotone-}}W[i]=W[i]$ .
  - Weighted Monotone *i*-Normalized Satisfiability is *W[i]*-complete.
  - Weighted Monotone *(i+1)*-Normalized Satisfiability is in *W[i]*.
- If *i>0* is odd, then
  - ${\text{antimonotone-}}W[i]=W[i]$
  - Weighted Antionotone *i*-Normalized Satisfiability is *W[i]*-complete.
  - If $i\geq 3$ , then Weighted Antimonotone *(i+1)*-Normalized Satisfiability is in *W[i]*.

These problems are essentially "artificial", in that they are not studied except within the context of parameterized complexity. The literature reports few naturally occurring problems that are *W[i]*-complete for $i\geq 3$ :

- Detection of inclusion dependencies in relational databases is *W[3]*-complete.
- Certain problems in supply-chain models are *W[3]*-complete or *W[4]*-complete.

#### *W[SAT]*

*W[SAT]* is the class of problems fpt-reducible to weighted SAT problems:

- Input: a Boolean formula
- Parameter: *k*
- Output: Whether the formula has a weight-*k* satisfying assignment.

It contains all *W[t]*.

#### *W*[*P*]

*W[P]* is the class of problems fpt-reducible to the problem of weighted Boolean circuit problems:

- Input: a Boolean circuit
- Parameter: *k*
- Output: Whether there exists a weight-*k* input such that the circuit outputs True.

It contains *W[SAT]*, since a Boolean formula can be efficiently converted to a Boolean circuit. Note that the opposite is not true in general, since the equivalent Boolean formula to a Boolean circuit may be necessarily exponentially larger than the circuit.

Equivalently, it is the class of problems that can be decided by a nondeterministic $h(k)\cdot {|x|}^{O(1)}$ -time Turing machine that makes at most $O(f(k)\cdot \log n)$ nondeterministic choices in the computation on $(x,k)$ (a *k*-restricted Turing machine).

It is known that FPT is contained in W[P], and the inclusion is believed to be strict. However, resolving this issue would imply a solution to the P versus NP problem.

Other connections to unparameterised computational complexity are that FPT equals *W*[*P*] if and only if circuit satisfiability can be decided in time $\exp(o(n))m^{O(1)}$ , or if and only if there is a computable, nondecreasing, unbounded function f such that all languages recognised by a nondeterministic polynomial-time Turing machine using ⁠ $f(n)\log n$ ⁠ nondeterministic choices are in *P*.

*W*[*P*] can be loosely thought of as the class of problems where we have a set S of n items, and we want to find a subset $T\subset S$ of size k such that a certain property holds. We can encode a choice as a list of k integers, stored in binary. Since the highest any of these numbers can be is n, $\lceil \log _{2}n\rceil$ bits are needed for each number. Therefore $k\cdot \lceil \log _{2}n\rceil$ total bits are needed to encode a choice. Therefore we can select a subset $T\subset S$ with $O(k\cdot \log n)$ nondeterministic choices.

### Other classes

The *W** hierarchy is similar to the *W* hierarchy, but it parameterizes depth, rather than holding it constant. The *W*[t]* class is defined as the class of problems fpt-reducible to this problem:

- Input: a Boolean circuit of weft at most *t*, and depth at most *k*,
- Parameter: *k*
- Output: Whether the Boolean circuit has a weight-*k* satisfying assignment.

It is related to *W* by: $W^{*}[1]=W[1],\;W^{*}[2]=W[2],\;W[t]\subset W^{*}[t]\subset W[t+2],\quad \forall t\geq 1$ The *AW* hierarchy is obtained by adding alternation to the *W* hierarchy. The *AW[t]* class is defined as the class of problems fpt-reducible to this problem:

- Input: a Boolean circuit of weft at most *t*, and a partition of its inputs to $I_{1}\cup I_{2}\cup \cdots \cup I_{r}$
- Parameter: $(r,k_{1},\dots ,k_{r})$
- Output: Whether the Boolean circuit is satisfiable under alternating weight- $(k_{1},\dots ,k_{r})$ conditions.

The alternating weight- $(k_{1},\dots ,k_{r})$ is defined as follows:

- There exists a subset $J_{1}\subset I_{1}$ of size $k_{1}$ , such that if we set exactly those inputs to True and the others to False, then,
- for any subset $J_{2}\subset I_{2}$ of size $k_{2}$ , such that if we set exactly those inputs to True and the others to False, then,
- ...
- the Boolean circuit outputs True.

One can interpret this as a 2-player game, with the first player trying to make the circuit output True, and the second player trying to make the circuit output False. The first player makes a move by setting exactly $k_{1}$ inputs of $I_{1}$ to True and the others to False, then the second player makes a move on $I_{2}$ , etc. The circuit is under alternating weight- $(k_{1},\dots ,k_{r})$ conditions iff player 1 has a winning strategy.

It turns out that the hierarchy collapses: $AW[1]=AW[2]=\cdots$ . Thus, the literature writes just a common symbol for them: $AW[\ast ]:=AW[1]=AW[2]=\cdots$ .
