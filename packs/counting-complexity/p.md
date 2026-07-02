---
title: "♯P - Wikipedia"
source: https://en.wikipedia.org/wiki/%E2%99%AFP
domain: counting-complexity
license: CC-BY-SA-4.0
tags: counting complexity, permanent computation, toda theorem, counting problem
fetched: 2026-07-02
---

# ♯P

In computational complexity theory, the complexity class **#P** (pronounced "sharp P" or, sometimes "number P" or "hash P") is the set of the counting problems associated with the decision problems in the set **NP**. More formally, **#P** is the class of function problems of the form "compute *f*(*x*)", where *f* is the number of accepting paths of a nondeterministic Turing machine running in polynomial time. Unlike most well-known complexity classes, it is not a class of decision problems but a class of function problems. The most difficult, representative problems of this class are #P-complete.

## Relation to decision problems

An **NP** decision problem can often be stated in the form "Are there any solutions that satisfy certain constraints?" For example:

- Are there any subsets of a list of integers that add up to zero? (subset sum problem)
- Are there any Hamiltonian cycles in a given graph with cost less than 100? (traveling salesman problem)
- Are there any variable assignments that satisfy a given CNF (conjunctive normal form) formula? (Boolean satisfiability problem or SAT)
- Does a univariate real polynomial have any positive roots? (root finding)

Corresponding **#P** function problems ask "how many" rather than "are there any". For example:

- How many subsets of a list of integers add up to zero?
- How many Hamiltonian cycles in a given graph have cost less than 100?
- How many variable assignments satisfy a given CNF formula?
- How many roots of a univariate real polynomial are positive?

Clearly, a **#P** problem must be at least as hard as the corresponding **NP** problem. If it's easy to count answers, then it must be easy to tell whether there are any answers—just count them and see whether the count is greater than zero. Some of these problems, such as root counting, are easy enough to be in FP, while others are #P-complete.

One consequence of Toda's theorem is that a polynomial-time machine with a **#P** oracle (**P****#P**) can solve all problems in **PH**, the entire polynomial hierarchy. In fact, the polynomial-time machine only needs to make one **#P** query to solve any problem in **PH**. This is an indication of the extreme difficulty of solving **#P**-complete problems exactly.

Surprisingly, some **#P** problems that are believed to be difficult correspond to easy (for example linear-time) **P** problems. For more information on this, see #P-complete.

The closest decision problem class to **#P** is **PP**, which asks whether a majority (more than half) of the computation paths accept. This finds the most significant bit in the **#P** problem answer. The decision problem class **⊕P** (pronounced "Parity-P") instead asks for the least significant bit of the **#P** answer.

## Formal definitions

**#P** is formally defined as follows:

#P

is the set of all functions

$f:\{0,1\}^{*}\to \mathbb {N}$

such that there is a polynomial-time

nondeterministic Turing machine

M

such that for all

$x\in \{0,1\}^{*}$

,

$f(x)$

equals the number of accepting branches in

M

's computation graph on

x

.

**#P** can also be equivalently defined in terms of a verifer. A decision problem is in **NP** if there exists a polynomial-time checkable certificate to a given problem instance—that is, **NP** asks whether there exists a proof of membership for the input that can be checked for correctness in polynomial time. Questions in **#P** ask *how many* certificates there exist for a problem instance that can be checked for correctness in polynomial time. In this context, **#P** is defined as follows:

#P

is the set of functions

$f:\{0,1\}^{*}\to \mathbb {N}$

such that there exists a polynomial

$p:\mathbb {N} \to \mathbb {N}$

and a polynomial-time

deterministic Turing machine

V

, called the verifier, such that for every

$x\in \{0,1\}^{*}$

,

$f(x)={\Big |}{\big \{}y\in \{0,1\}^{p(|x|)}:V(x,y)=1{\big \}}{\Big |}$

.

(In other words,

$f(x)$

equals the size of the set containing all of the polynomial-size certificates).

## History

The complexity class **#P** was first defined by Leslie Valiant in a 1979 article on the computation of the permanent of a square matrix, in which he proved that permanent is #P-complete.

Larry Stockmeyer has proved that for every #P problem P there exists a randomized algorithm using an oracle for SAT, which given an instance a of P and $\epsilon >0$ returns with high probability a number x such that $(1-\epsilon )P(a)\leq x\leq (1+\epsilon )P(a)$ . The runtime of the algorithm is polynomial in a and $1/\epsilon$ . The algorithm is based on the leftover hash lemma.
