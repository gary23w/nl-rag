---
title: "NL (complexity)"
source: https://en.wikipedia.org/wiki/NL_(complexity)
domain: logspace
license: CC-BY-SA-4.0
tags: logarithmic space, log space reduction, undirected connectivity, symmetric turing machine
fetched: 2026-07-02
---

# NL (complexity)

Unsolved problem in computer science

⁠

${\mathsf {L{\overset {?}{=}}NL}}$

⁠

More unsolved problems in computer science

In computational complexity theory, **NL** (**N**ondeterministic **L**ogarithmic-space) is the complexity class containing decision problems that can be solved by a nondeterministic Turing machine using a logarithmic amount of memory space.

**NL** is a generalization of **L**, the class for logspace problems on a deterministic Turing machine. Since any deterministic Turing machine is also a nondeterministic Turing machine, we have that **L** is contained in **NL**.

**NL** can be formally defined in terms of the computational resource nondeterministic space (or NSPACE) as **NL** = **NSPACE**(log *n*).

Important results in complexity theory allow us to relate this complexity class with other classes, telling us about the relative power of the resources involved. Results in the field of algorithms, on the other hand, tell us which problems can be solved with this resource. Like much of complexity theory, many important questions about **NL** are still open (see Unsolved problems in computer science).

Occasionally **NL** is referred to as **RL** due to its probabilistic definition below; however, this name is more frequently used to refer to randomized logarithmic space, which is not known to equal **NL**.

## Definitions

There are several equivalent definitions of the **NL** class.

### Standard definition

**NL** is the complexity class of decision problems that can be solved by a nondeterministic Turing machine (NTM) using a logarithmic amount of memory space.

In more detail, a language L is NL iff there exists a NTM M such that

- M runs on logspace.
- M always halts.

- If $x\in L$ , then there exists at least one computational trace of $M(x)$ that results in the machine halting in an accepting state.
- If $x\not \in L$ , then all computational traces of $M(x)$ results in the machine halting in an unaccepting state.

### Probabilistic definition

Suppose *C* is the complexity class of decision problems solvable in logarithmithic space with probabilistic Turing machines that never accept incorrectly but are allowed to reject incorrectly less than 1/3 of the time; this is called *one-sided error*. The constant 1/3 is arbitrary; any *x* with 0 ≤ *x* < 1/2 would suffice.

It turns out that *C* = **NL**. Notice that *C*, unlike its deterministic counterpart **L**, is not limited to polynomial time, because although it has a polynomial number of configurations it can use randomness to escape an infinite loop. If we do limit it to polynomial time, we get the class **RL**, which is contained in but not known or believed to equal **NL**.

There is a simple algorithm that establishes that *C* = **NL**. Clearly *C* is contained in **NL**, since:

- If the string is not in the language, both reject along all computation paths.
- If the string is in the language, an **NL** algorithm accepts along at least one computation path and a *C* algorithm accepts along at least two-thirds of its computation paths.

To show that **NL** is contained in *C*, we simply take an **NL** algorithm and choose a random computation path of length *n*, and execute this 2*n* times. Because no computation path exceeds length *n*, and because there are 2*n* computation paths in all, we have a good chance of hitting the accepting one (bounded below by a constant).

The only problem is that we don't have room in log space for a binary counter that goes up to 2*n*. To get around this we replace it with a *randomized* counter, which simply flips *n* coins and stops and rejects if they all land on heads. Since this event has probability 2−*n*, we expect to take 2*n* steps on average before stopping. It only needs to keep a running total of the number of heads in a row it sees, which it can count in log space.

Because of the Immerman–Szelepcsényi theorem, according to which NL is closed under complements, the one-sided error in these probabilistic computations can be replaced by zero-sided error. That is, these problems can be solved by probabilistic Turing machines that use logarithmic space and never make errors. The corresponding complexity class that also requires the machine to use only polynomial time is called ZPLP.

Thus, when we only look at space, it seems that randomization and nondeterminism are equally powerful.

### Certificate definition

**NL** can equivalently be characterised by certificates, analogous to classes such as **NP**. Let a *verifier* be a deterministic logarithmic-space bounded deterministic Turing machine that has an additional read-only read-once input tape (that is, the verifier may only move the read-head forwards, never backwards).

A language L is in **NL** if and only if

- There exists a polynomial function p .
- There exists a verifier $TM$ .
- For any x , $x\in L$ iff there exists a certificate u with length $|u|\leq p(|x|)$ , such that $TM(x,u)=1$ .

In words, it means that if a sentence is in the language, then there exists a polynomial-length proof that it is in the language. It does not say anything about the case where the sentence is *not* in the language, though by the Immerman–Szelepcsényi theorem, it is clear that there exists some verifier that can verify both $x\in L$ and $x\not \in L$ .

Note that the read-once condition is necessary. If the verifier can read forwards and backwards, this extends the class to the **NP** class.

Cem Say and Abuzer Yakaryılmaz have proven that the deterministic logarithmic-space Turing machine in the statement above can be replaced by a bounded-error probabilistic constant-space Turing machine that is allowed to use only a constant number of random bits.

### Descriptive definition

In descriptive complexity theory, **NL** is defined as those languages expressible in first-order logic with an added transitive closure operator.

## Closure properties

The class NL is closed under the operations complementation, union, and therefore intersection, concatenation, and Kleene star.

## NL-completeness

A problem is **NL-complete** if it is **NL**, and any problem in **NL** is log-space reducible to it.

Problems that are known to be **NL**-complete including ST-connectivity and 2-satisfiability.

ST-connectivity asks, for nodes *S* and *T* in a directed graph, whether *T* is reachable from *S*.

2-satisfiability asks, given a propositional formula of which each clause is the disjunction of two literals, if there is a variable assignment that makes the formula true. An example instance, where $\neg$ indicates *not*, might be:

$(x_{1}\vee \neg x_{3})\wedge (\neg x_{2}\vee x_{3})\wedge (\neg x_{1}\vee \neg x_{2})$

## Containments

It is known that NL is contained in P, since there is a polynomial-time algorithm for 2-satisfiability, but it is not known whether NL = P or whether L = NL. It is known that NL = co-NL, where co-NL is the class of languages whose complements are in NL. This result (the Immerman–Szelepcsényi theorem) was independently discovered by Neil Immerman and Róbert Szelepcsényi in 1987; they received the 1995 Gödel Prize for this work.

In circuit complexity, NL can be placed within the NC hierarchy. In Papadimitriou 1994, Theorem 16.1, we have:

${\mathsf {NC_{1}\subseteq L\subseteq NL\subseteq NC_{2}}}$

.

More precisely, NL is contained in AC1. It is known that NL is equal to ZPL, the class of problems solvable by randomized algorithms in logarithmic space and unbounded time, with no error. It is not, however, known or believed to be equal to RLP or ZPLP, the polynomial-time restrictions of RL and ZPL, which some authors refer to as RL and ZPL.

We can relate NL to deterministic space using Savitch's theorem, which tells us that any nondeterministic algorithm can be simulated by a deterministic machine in at most quadratically more space. From Savitch's theorem, we have directly that:

${\mathsf {NL\subseteq SPACE}}(\log ^{2}n)\ \ \ \ {\text{equivalently, }}{\mathsf {NL\subseteq L}}^{2}.$

This was the strongest deterministic-space inclusion known in 1994 (Papadimitriou 1994 Problem 16.4.10, "Symmetric space"). Since larger space classes are not affected by quadratic increases, the nondeterministic and deterministic classes are known to be equal, so that for example we have PSPACE = NPSPACE.
