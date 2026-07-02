---
title: "Parity function"
source: https://en.wikipedia.org/wiki/Parity_function
domain: circuit-complexity
license: CC-BY-SA-4.0
tags: circuit complexity, circuit lower bound, ac0 class, natural proofs barrier
fetched: 2026-07-02
---

# Parity function

In Boolean algebra, a **parity function** is a Boolean function whose value is one if and only if the input vector has an odd number of ones. The parity function of two inputs is also known as the XOR function.

The parity function is notable for its role in theoretical investigation of circuit complexity of Boolean functions.

The output of the parity function is the parity bit.

## Definition

The n -variable parity function is the Boolean function $f:\{0,1\}^{n}\to \{0,1\}$ with the property that $f(x)=1$ if and only if the number of ones in the vector $x\in \{0,1\}^{n}$ is odd. In other words, f is defined as follows:

$f(x)=x_{1}\oplus x_{2}\oplus \dots \oplus x_{n}$

where $\oplus$ denotes exclusive or.

## Properties

Parity only depends on the number of ones and is therefore a symmetric Boolean function.

The *n*-variable parity function and its negation are the only Boolean functions for which all disjunctive normal forms have the maximal number of 2 *n* − 1 monomials of length *n* and all conjunctive normal forms have the maximal number of 2 *n* − 1 clauses of length *n*.

## Computational complexity

Some of the earliest work in computational complexity was 1961 bound of Bella Subbotovskaya showing the size of a Boolean formula computing parity must be at least $\Omega (n^{3/2})$ . This work uses the method of random restrictions. This exponent of $3/2$ has been increased through careful analysis to $1.63$ by Paterson and Zwick (1993) and then to 2 by Håstad (1998).

In the early 1980s, Merrick Furst, James Saxe and Michael Sipser and independently Miklós Ajtai established super-polynomial lower bounds on the size of constant-depth Boolean circuits for the parity function, i.e., they showed that polynomial-size constant-depth circuits cannot compute the parity function. Similar results were also established for the majority, multiplication and transitive closure functions, by reduction from the parity function.

Håstad (1987) established tight exponential lower bounds on the size of constant-depth Boolean circuits for the parity function. Håstad's Switching Lemma is the key technical tool used for these lower bounds and Johan Håstad was awarded the Gödel Prize for this work in 1994. The precise result is that depth-k circuits with AND, OR, and NOT gates require size $\exp(\Omega (n^{\frac {1}{k-1}}))$ to compute the parity function. This is asymptotically almost optimal as there are depth-k circuits computing parity which have size $\exp(O(n^{\frac {1}{k-1}})t)$ .

## Infinite version

An infinite parity function is a function $f\colon \{0,1\}^{\omega }\to \{0,1\}$ mapping every infinite binary string to 0 or 1, having the following property: if w and v are infinite binary strings differing only on finitely many coordinates, then $f(w)=f(v)$ if and only if w and v differ on an even number of coordinates.

Assuming axiom of choice it can be proved that parity functions exist and there are $2^{2^{\aleph _{0}}}$ many of them; as many as the number of all functions from $\{0,1\}^{\omega }$ to $\{0,1\}$ . It is enough to take one representative per equivalence class of relation $\approx$ defined as follows: $w\approx v$ if w and v differ at finite number of coordinates. Having such representatives, we can map all of them to 0 ; the rest of f values are deducted unambiguously.

Another construction of an infinite parity function can be done using a non-principal ultrafilter U on $\omega$ . The existence of non-principal ultrafilters on $\omega$ follows from – and is strictly weaker than – the axiom of choice. For any $w:\omega \to \{0,1\}$ we consider the set $A_{w}=\{n\in \omega \mid \{k\leq n\mid w(k)=0\}{\text{ is even}}\}$ . The infinite parity function f is defined by mapping w to 0 if and only if $A_{w}$ is an element of the ultrafilter.

It is necessary to assume at least some amount of choice to prove that infinite parity functions exist. If f is an infinite parity function and we consider the inverse image $f^{-1}[0]$ as a subset of the Cantor space $\{0,1\}^{\omega }$ , then $f^{-1}[0]$ is a non-measurable set and does not have the property of Baire. Without the axiom of choice, it is consistent (relative to ZF) that all subsets of the Cantor space are measurable and have the property of Baire and thus that no infinite parity function exists; this holds in the Solovay model, for instance.
