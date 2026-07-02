---
title: "PPAD (complexity)"
source: https://en.wikipedia.org/wiki/PPAD_(complexity)
domain: nash-equilibrium-computation
license: CC-BY-SA-4.0
tags: nash equilibrium computation, lemke howson algorithm, ppad complete, fixed point argument
fetched: 2026-07-02
---

# PPAD (complexity)

In computer science, **PPAD** ("Polynomial Parity Arguments on Directed graphs") is a complexity class introduced by Christos Papadimitriou in 1994. PPAD is a subclass of TFNP based on functions that can be shown to be total by a parity argument. The class attracted significant attention in the field of algorithmic game theory because it contains the problem of computing a Nash equilibrium: this problem was shown to be complete for PPAD by Daskalakis, Goldberg and Papadimitriou with at least 3 players and later extended by Chen and Deng to 2 players.

## Definition

PPAD is a subset of the class TFNP, the class of function problems in FNP that are guaranteed to be total. The TFNP formal definition is given as follows:

A binary relation P(

x

,

y

) is in TFNP if and only if there is a deterministic polynomial time algorithm that can determine whether P(

x

,

y

) holds given both

x

and

y

, and for every

x

, there exists a

y

such that P(

x

,

y

) holds.

Subclasses of TFNP are defined based on the type of mathematical proof used to prove that a solution always exists. Informally, PPAD is the subclass of TFNP where the guarantee that there exists a *y* such that P(*x*,*y*) holds is based on a parity argument on a directed graph. The class is formally defined by specifying one of its complete problems, known as *End-Of-The-Line*:

G is a (possibly exponentially large) directed graph with every

vertex

having at most one predecessor and at most one successor. G is specified by giving a polynomial-time computable function f(

v

) (polynomial in the size of

v

) that returns the predecessor and successor (if they exist) of the vertex

v

. Given a vertex

s

in G with no predecessor, find a vertex

t≠s

with no predecessor or no successor. (The input to the problem is the source vertex

s

and the function f(

v

)). In other words, we want any source or sink of the directed graph other than

s

.

Such a *t* must exist if an *s* does, because the structure of G means that vertices with only one neighbour come in pairs. In particular, given *s*, we can find such a *t* at the other end of the string starting at *s*. (Note that this may take exponential time if we just evaluate f repeatedly.)

## Proving membership in PPAD

In many cases, when a problem is said to "be in PPAD", it often means that finding an *approximate* solution to the problem is in PPAD. This is often necessary, as in many cases, the solutions might involve irrational numbers, and thus cannot be output in finite time.

However, there are cases in which solutions with rational numbers are guaranteed to exist. For such cases, Filos-Ratsikas, Hansen, Høgh and Hollender present a general method for proving that computing an *exact* solution belongs to PPAD.

## Relations to other complexity classes

PPAD is contained in (but not known to be equal to) PPA (the corresponding class of parity arguments for *undirected* graphs) which is contained in TFNP. PPAD is also contained in (but not known to be equal to) PPP, another subclass of TFNP. It contains CLS.

PPAD is a class of problems that are believed to be hard, but obtaining PPAD-completeness is a weaker evidence of intractability than that of obtaining NP-completeness. PPAD problems cannot be NP-complete, for the technical reason that NP is a class of decision problems, but the answer of PPAD problems is always yes, as a solution is known to exist, even though it might be hard to find that solution. However, PPAD and NP are closely related. While the question whether a Nash equilibrium exists for a given game cannot be NP-hard because the answer is always yes, the question whether a *second* equilibrium exists is NP complete. Examples of PPAD-complete problems include finding Nash equilibria, computing fixed points in Brouwer functions, and finding Arrow-Debreu equilibria in markets.

Fearnley, Goldberg, Hollender and Savani proved that a complexity class called CLS is equal to the intersection of PPAD and PLS.

Etessami and Yannakakis (who invented the related class FIXP) write that "The piecewise-linear fragment of FIXP equals PPAD". In other words, the problems in PPAD are the problems in FIXP in which the input function is piecewise-linear.
