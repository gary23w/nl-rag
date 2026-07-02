---
title: "NC (complexity)"
source: https://en.wikipedia.org/wiki/NC_(complexity)
domain: nc-class
license: CC-BY-SA-4.0
tags: nick class parallel, parallel random access machine, circuit depth, efficiently parallelizable
fetched: 2026-07-02
---

# NC (complexity)

Unsolved problem in computer science

⁠

${\mathsf {NC}}{\overset {?}{=}}{\mathsf {P}}$

⁠

More unsolved problems in computer science

In computational complexity theory, the class **NC** (for "Nick's Class") is the set of decision problems decidable in polylogarithmic time on a parallel computer with a polynomial number of processors. In other words, a problem with input size *n* is in **NC** if there exist constants *c* and *k* such that it can be solved in time *O*((log *n*)*c*) using *O*(*n**k*) parallel processors. Stephen Cook coined the name "Nick's class" after Nick Pippenger, who had done extensive research on circuits with polylogarithmic depth and polynomial size. As in the case of circuit complexity theory, usually the class has an extra constraint that the circuit family must be *uniform* (see below).

Just as the class **P** can be thought of as the tractable problems (Cobham's thesis), so **NC** can be thought of as the problems that can be efficiently solved on a parallel computer. **NC** is a subset of **P** because polylogarithmic parallel computations can be simulated by polynomial-time sequential ones. It is unknown whether **NC** = **P**, but most researchers suspect this to be false, meaning that there are probably some tractable problems that are "inherently sequential" and cannot significantly be sped up by using parallelism. Just as the class **NP-complete** can be thought of as "probably intractable", so the class **P-complete**, when using **NC** reductions, can be thought of as "probably not parallelizable" or "probably inherently sequential".

The parallel computer in the definition can be assumed to be a *parallel, random-access machine* (PRAM). That is a parallel computer with a central pool of memory, and any processor can access any bit of memory in constant time. The definition of **NC** is not affected by the choice of how the PRAM handles simultaneous access to a single bit by more than one processor. It can be CRCW, CREW, or EREW. See PRAM for descriptions of those models.

Equivalently, **NC** can be defined as those decision problems decidable by a uniform Boolean circuit (which can be calculated from the length of the input, for NC, we suppose we can compute the Boolean circuit of size *n* in logarithmic space in *n*) with polylogarithmic depth and a polynomial number of gates with a maximum fan-in of 2.

**RNC** is a class extending **NC** with access to randomness.

## Problems in NC

As with **P**, by a slight abuse of language, one might classify function problems and search problems as being in **NC**. **NC** is known to include many problems, including

- Integer addition, multiplication and division;
- Matrix multiplication, determinant, inverse, rank;
- Polynomial GCD, by a reduction to linear algebra using Sylvester matrix
- Finding a maximal matching.

Often algorithms for those problems had to be separately invented and could not be naïvely adapted from well-known algorithms – Gaussian elimination and Euclidean algorithm rely on operations performed in sequence. One might contrast ripple carry adder with a carry-lookahead adder.

### Example

An example of problem in NC1 is the parity check on a bit string. The problem consists in counting the number of 1s in a string made of 1 and 0. A simple solution consists in summing all the string's bits. Since addition is associative, $x_{1}+\cdots +x_{n}=\left(x_{1}+\cdots +x_{\frac {n}{2}}\right)+\left(x_{{\frac {n}{2}}+1}+\cdots +x_{n}\right).$ Recursively applying such property, it is possible to build a binary tree of length $O(\log(n))$ in which every sum between two bits $x_{i}$ and $x_{j}$ is expressible by means of basic logical operators, e.g. through the Boolean expression $(x_{i}\land \neg x_{j})\lor (\neg x_{i}\land x_{j})$ .

## The NC hierarchy

**NC***i* is the class of decision problems decidable by uniform Boolean circuits with a polynomial number of gates of at most two inputs and depth *O*((log *n*)*i*), or the class of decision problems solvable in time *O*((log *n*)*i*) on a parallel computer with a polynomial number of processors. Clearly,

${\mathsf {NC}}^{0}\subseteq {\mathsf {NC}}^{1}\subseteq \cdots \subseteq {\mathsf {NC}}^{i}\subseteq \cdots \subseteq {\mathsf {NC}}$

which forms the **NC**-hierarchy.

The smallest class, **NC***0*, is the class of functions definable by Boolean circuits with constant depth and bounded fan-in.

The next-smallest class, **NC***1*, is equal to **BW**4*0* , the set of all problems solvable by polynomial-size, bounded fan-in circuits of width 4 or less. This is true for both the uniform and nonuniform case (DLOGTIME-uniformity suffices).

One can relate the **NC** classes to the space classes **L**, **SL**, **NL**, **LOGCFL**, and **AC**.

${\mathsf {NC}}^{1}\subseteq {\mathsf {L}}={\mathsf {SL}}\subseteq {\mathsf {NL}}\subseteq {\mathsf {LOGCFL}}\subseteq {\mathsf {AC}}^{1}\subseteq {\mathsf {NC}}^{2}.$

The NC classes are related to the AC classes, which are defined similarly, but with gates having unbounded fan-in. For each *i*,

${\mathsf {NC}}^{i}\subseteq {\mathsf {AC}}^{i}\subseteq {\mathsf {AC}}^{i}[p]\subseteq {\mathsf {ACC}}^{i}\subseteq {\mathsf {TC}}^{i}\subseteq {\mathsf {NC}}^{i+1}$

As an immediate consequence of this, **NC** = **AC**.

Also, ${\mathsf {NC}}^{0}\subsetneq {\mathsf {AC}}^{0}\subsetneq {\mathsf {ACC}}^{0}$ .

Similarly, **NC** is equivalent to the problems solvable on an alternating Turing machine restricted to at most two options at each step with *O*(log *n*) space and $(\log n)^{O(1)}$ alternations.

It is a major open question whether ${\mathsf {TC}}^{0}\subsetneq {\mathsf {NC}}^{1}$ (Vollmer 1998, p. 126). A significant partial result states that if there exists some $\epsilon >0$ , and a problem in ${\mathsf {NC}}^{1}$ , such that it requires at least $\Omega (n^{1+\epsilon })$ gates in ${\mathsf {TC}}^{0}$ , then this can be bootstrapped so that it requires superpolynomial gates, and thus not in ${\mathsf {TC}}^{0}$ .

### Uniformity

There are various levels of uniformity being considered. A family of Boolean circuits is uniform if the schematics for any member of the family can be produced by a Turing machine under various resource constraints. With different levels of constraints, we would obtain possibly different complexity classes, with a more stringent constraint leading to a possibly smaller complexity class.

In the literature, the following uniformities have been considered for the **NC***1* class, arranged according to strength:

- **NC***1* itself. This is also called the $U_{E^{*}}$ -uniformity. It is equivalent to **ALOGTIME**.
- **LOGSPACE**.
- **P**.
- **Computable**. Any halting Turing machine is allowed.
- **Non-uniform**. This is the strongest case. The Boolean circuit family may contain arbitrary elements of the correct width and depth, even if the family cannot be generated by any algorithm.

By default, the literature uses **LOGSPACE** uniformity.

Because it is possible that ${\mathsf {NC}}^{1}\subsetneq {\mathsf {LOGSPACE}}$ , researchers may use **NC***1*-uniformity, since it is a possible strengthening. To avoid self-reference, **NC***1*-uniform **NC***1* is defined as follows: A **NC***1* Boolean circuit family is **NC***1*-uniform if the set of descriptions is decided by an **ALOGTIME** alternating Turing machine. The machine reads in a length- n description of a Boolean circuit, and halts in time $O(\log n)$ .

For higher classes **NC***2*, **NC***3*, ..., there are similar uniformities definable. However, for $k\geq 2$ , **NC***k*-uniform **NC***k* and **LOGSPACE**-uniform **NC***k* are equal, and both are equivalent to the following definition: The family is decided by an alternating Turing machine. The machine reads in a length- n description of a Boolean circuit, and halts in time $O((\log n)^{k})$ and space $O(\log n)$ .

### Open problem: Is NC proper?

Unsolved problem in computer science

Is the

${\mathsf {NC}}$

hierarchy proper?

More unsolved problems in computer science

One major open question in complexity theory is whether or not every containment in the **NC** hierarchy is proper. It was observed by Papadimitriou that, if **NC***i* = **NC***i*+1 for some *i*, then **NC***i* = **NC***j* for all *j* ≥ *i*, and as a result, **NC***i* = **NC**. This observation is known as **NC**-hierarchy collapse because even a single equality in the chain of containments

${\mathsf {NC}}^{1}\subseteq {\mathsf {NC}}^{2}\subseteq \cdots$

implies that the entire **NC** hierarchy "collapses" down to some level *i*. Thus, there are 2 possibilities:

1. ${\mathsf {NC}}^{1}\subsetneq \cdots \subsetneq {\mathsf {NC}}^{i}\subsetneq \cdots \subsetneq {\mathsf {NC}}^{i+j}\subsetneq \cdots {\mathsf {NC}}$
2. ${\mathsf {NC}}^{1}\subsetneq \cdots \subsetneq {\mathsf {NC}}^{i}=\cdots ={\mathsf {NC}}^{i+j}=\cdots {\mathsf {NC}}$

It is widely believed that (1) is the case, although no proof as to the truth of either statement has yet been discovered.

If there exists a problem that is **NC**-complete under **LOGSPACE** or **NC***1* reductions, then the **NC** hierarchy collapses.

## Barrington's theorem

A **branching program** with *n* variables of width *k* and length *m* consists of a sequence of *m* instructions. Each of the instructions is a tuple (*i*, *p*, *q*) where *i* is the index of variable to check (1 ≤ *i* ≤ *n*), and *p* and *q* are functions from {1, 2, ..., *k*} to {1, 2, ..., *k*}. Numbers 1, 2, ..., *k* are called states of the branching program. The program initially starts in state 1, and each instruction (*i*, *p*, *q*) changes the state from *x* to *p*(*x*) or *q*(*x*), depending on whether the *i*th variable is 0 or 1. The function mapping an input to a final state of the program is called the *yield* of the program (more precisely, the yield on an input is the function mapping any initial state to the corresponding final state). The program *accepts* a set $A\subseteq 2^{n}$ of variable values when there is some set of functions $F\subseteq k^{k}$ such that a variable sequence $x\in 2^{n}$ is in *A* precisely when its yield is in *F*.

A family of branching programs consists of a branching program with *n* variables for each *n*. It accepts a language when the *n* variable program accepts the language restricted to length *n* inputs.

It is easy to show that every language *L* on {0,1} can be recognized by a family of branching programs of width 5 and exponential length, or by a family of exponential width and linear length.

Every regular language on {0,1} can be recognized by a family of branching programs of constant width and linear number of instructions (since a DFA can be converted to a branching program). **BWBP** denotes the class of languages recognizable by a family of branching programs of bounded width and polynomial length.

**Barrington's theorem** says that **BWBP** is exactly nonuniform **NC**1. The proof uses the nonsolvability of the symmetric group S5.

The theorem is rather surprising. For instance, it implies that the majority function can be computed by a family of branching programs of constant width and polynomial size, while intuition might suggest that to achieve polynomial size, one needs a linear number of states.

### Proof of Barrington's theorem

A branching program of constant width and polynomial size can be easily converted (via divide-and-conquer) to a circuit in **NC**1.

Conversely, suppose a circuit in **NC**1 is given. Without loss of generality, assume it uses only AND and NOT gates.

**Lemma 1**—If there exists a branching program that sometimes works as a permutation *P* and sometimes as a permutation *Q*, by right-multiplying permutations in the first instruction by *α*, and in the last instruction left-multiplying by *β*, we can make a circuit of the same length that behaves as *β**P**α* or *β**Q**α*, respectively.

Call a branching program α-computing a circuit *C* if it works as identity when *C*'s output is 0, and as *α* when *C*'s output is 1.

As a consequence of Lemma 1 and the fact that all cycles of length 5 are conjugate, for any two 5-cycles *α*, *β*, if there exists a branching program α-computing a circuit *C*, then there exists a branching program β-computing the circuit *C*, of the same length.

**Lemma 2**—There exist 5-cycles *γ*, *δ* such that their commutator *ε*=*γδγ*−1*δ*−1 is a 5-cycle. For example, *γ* = (1 2 3 4 5), *δ* = (1 3 5 4 2) giving *ε* = (1 3 2 5 4).

Proof

We will now prove Barrington's theorem by induction:

Suppose we have a circuit *C* which takes inputs *x*1,...,*x**n* and assume that for all subcircuits *D* of *C* and 5-cycles α, there exists a branching program α-computing *D*. We will show that for all 5-cycles α, there exists a branching program α-computing *C*.

- If the circuit *C* simply outputs some input bit *xi*, the branching program we need has just one instruction: checking *xi*'s value (0 or 1), and outputting the identity or *α* (respectively).
- If the circuit *C* outputs ¬*A* for some different circuit *A*, create a branching program *α*−1-computing *A* and then multiply the output of the program by α. By Lemma 1, we get a branching program for *A* outputting the identity or α, i.e. *α*-computing ¬*A*=*C*.
- If the circuit *C* outputs *A*∧*B* for circuits *A* and *B*, join the branching programs that *γ*-compute *A*, *δ*-compute *B*, *γ*−1-compute *A*, and δ−1-compute B for a choice of 5-cycles γ and δ such that their commutator *ε*=*γδγ*−1*δ*−1 is also a 5-cycle. (The existence of such elements was established in Lemma 2.) If one or both of the circuits outputs 0, the resulting program will be the identity due to cancellation; if both circuits output 1, the resulting program will output the commutator *ε*. In other words, we get a program *ε*-computing *A*∧*B*. Because *ε* and *α* are two 5-cycles, they are conjugate, and hence there exists a program *α*-computing *A*∧*B* by Lemma 1.

By assuming the subcircuits have branching programs so that they are *α*-computing for all 5-cycles *α*∈*S*5, we have shown *C* also has this property, as required.

The size of the branching program is at most 4*d*, where *d* is the depth of the circuit. If the circuit has logarithmic depth, the branching program has polynomial length.
