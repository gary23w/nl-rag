---
title: "Brouwer fixed-point theorem"
source: https://en.wikipedia.org/wiki/Brouwer_fixed-point_theorem
domain: fixed-point-iteration
license: CC-BY-SA-4.0
tags: fixed-point iteration, banach fixed-point theorem, contraction mapping, anderson acceleration
fetched: 2026-07-02
---

# Brouwer fixed-point theorem

**Brouwer's fixed-point theorem** is a fixed-point theorem in topology, named after L. E. J. (Bertus) Brouwer. It states that for any continuous function f mapping a nonempty compact convex set to itself, there is a point $x_{0}$ such that $f(x_{0})=x_{0}$ . The simplest forms of Brouwer's theorem are for continuous functions f from a closed interval I in the real numbers to itself or from a closed disk D to itself. A more general form than the latter is for continuous functions from a nonempty convex compact subset K of Euclidean space to itself.

Among hundreds of fixed-point theorems, Brouwer's is particularly well known, due in part to its use across numerous fields of mathematics. In its original field, this result is one of the key theorems characterizing the topology of Euclidean spaces, along with the Jordan curve theorem, the hairy ball theorem, the invariance of dimension and the Borsuk–Ulam theorem. This gives it a place among the fundamental theorems of topology. The theorem is also used for proving deep results about differential equations and is covered in most introductory courses on differential geometry. It appears in unlikely fields such as game theory. In economics, Brouwer's fixed-point theorem and its extension, the Kakutani fixed-point theorem, play a central role in the proof of existence of general equilibrium in market economies as developed in the 1950s by economics Nobel prize winners Kenneth Arrow and Gérard Debreu.

The theorem was first studied in view of work on differential equations by the French mathematicians around Henri Poincaré and Charles Émile Picard. Proving results such as the Poincaré–Bendixson theorem requires the use of topological methods. This work at the end of the 19th century opened into several successive versions of the theorem. The case of differentiable mappings of the *n*-dimensional closed ball was first proved in 1910 by Jacques Hadamard and the general case for continuous mappings by Brouwer in 1911.

## Statement

The theorem has several formulations, depending on the context in which it is used and its degree of generalization. The simplest is sometimes given as follows:

**In the plane**

Every

continuous function

from a

closed

disk

to itself has at least one fixed point.

This can be generalized to an arbitrary finite dimension:

**In Euclidean space**

Every continuous function from a

closed ball

of a

Euclidean space

into itself has a fixed point.

A slightly more general version is as follows:

**Convex compact set**

Every continuous function from a nonempty

convex

compact

subset

K

of a Euclidean space to

K

itself has a fixed point.

An even more general form is better known under a different name:

**Schauder fixed point theorem**

Every continuous function from a nonempty convex compact subset

K

of a

Banach space

to

K

itself has a fixed point.

## Importance of the pre-conditions

The theorem holds only for functions that are *endomorphisms* (functions that have the same set as the domain and codomain) and for nonempty sets that are *compact* (thus, in particular, bounded and closed) and *convex* (or homeomorphic to convex). The following examples show why the pre-conditions are important.

### The function *f* as an endomorphism

Consider the function

$f(x)=x+1$

with domain $[-1,1]$ . The range of the function is $[0,2]$ . Thus, f is not an endomorphism.

### Boundedness

Consider the function

$f(x)=x+1,$

which is a continuous function from $\mathbb {R}$ to itself. As it shifts every point to the right, it cannot have a fixed point. The space $\mathbb {R}$ is convex and closed, but not bounded.

### Closedness

Consider the function

$f(x)={\frac {x+1}{2}},$

which is a continuous function from the open interval $(-1,1)$ to itself. Since the point $x=1$ is not part of the interval, there is no point in the domain such that $f(x)=x$ . The set $(-1,1)$ is convex and bounded, but not closed. On the other hand, the function f does have a fixed point in the *closed* interval $[-1,1]$ , namely $x=1$ . The closed interval $[-1,1]$ is compact, the open interval $(-1,1)$ is not.

### Convexity

Convexity is not strictly necessary for Brouwer's fixed-point theorem. Because the properties involved (continuity, being a fixed point) are invariant under homeomorphisms, Brouwer's fixed-point theorem is equivalent to forms in which the domain is required to be a closed unit ball $D^{n}$ . For the same reason it holds for every set that is homeomorphic to a closed ball (and therefore also closed, bounded, connected, without holes, etc.).

The following example shows that Brouwer's fixed-point theorem does not work for domains with holes. Consider the function $f(x)=-x$ , which is a continuous function from the unit circle to itself. Since $-x\neq x$ holds for any point of the unit circle, f has no fixed point. The analogous example works for the n -dimensional sphere (or any symmetric domain that does not contain the origin). The unit circle is closed and bounded, but it has a hole (and so it is not convex). The function f *does* have a fixed point for the unit disc, since it takes the origin to itself.

A formal generalization of Brouwer's fixed-point theorem for "hole-free" domains can be derived from the Lefschetz fixed-point theorem.
