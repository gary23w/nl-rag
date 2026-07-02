---
title: "Probably approximately correct learning"
source: https://en.wikipedia.org/wiki/Probably_approximately_correct_learning
domain: learning-theory-pac
license: CC-BY-SA-4.0
tags: probably approximately correct, sample complexity, pac learnable, concept class
fetched: 2026-07-02
---

# Probably approximately correct learning

In computational learning theory, **probably approximately correct** (**PAC**) **learning** is a framework for mathematical analysis of machine learning. It was proposed in 1984 by Leslie Valiant.

In this framework, the learner receives samples and must select a generalization function (called the *hypothesis*) from a certain class of possible functions. The goal is that, with high probability (the "probably" part), the selected function will have low generalization error (the "approximately correct" part). The learner must be able to learn the concept given any arbitrary approximation ratio, probability of success, or distribution of the samples.

The model was later extended to treat noise (misclassified samples).

An important innovation of the PAC framework is the introduction of computational complexity theory concepts to machine learning. In particular, the learner is expected to find efficient functions (time and space requirements bounded to a polynomial of the example size), and the learner itself must implement an efficient procedure (requiring an example count bounded to a polynomial of the concept size, modified by the approximation and likelihood bounds).

## Definitions and terminology

In order to give the definition for something that is PAC-learnable, we first have to introduce some terminology.

For the following definitions, two examples will be used. The first is the problem of character recognition given an array of n bits encoding a binary-valued image. The other example is the problem of finding an interval that will correctly classify points within the interval as positive and the points outside of the range as negative.

Let X be a set called the *instance space* or the encoding of all the samples. In the character recognition problem, the instance space is $X=\{0,1\}^{n}$ . In the interval problem the instance space, X , is the set of all bounded intervals in $\mathbb {R}$ , where $\mathbb {R}$ denotes the set of all real numbers.

A *concept* is a subset $c\subset X$ . One concept is the set of all patterns of bits in $X=\{0,1\}^{n}$ that encode a picture of the letter "P". An example concept from the second example is the set of open intervals, $\{(a,b)\mid 0\leq a\leq \pi /2,\pi \leq b\leq {\sqrt {13}}\}$ , each of which contains only the positive points. A *concept class* C is a collection of concepts over X . This could be the set of all subsets of the array of bits that are skeletonized 4-connected (width of the font is 1).

Let $\operatorname {EX} (c,D)$ be a procedure that draws an example, x , using a probability distribution D and gives the correct label $c(x)$ , that is 1 if $x\in c$ and 0 otherwise.

Now, given $0<\epsilon ,\delta <1$ , assume there is an algorithm A and a polynomial p in $1/\epsilon ,1/\delta$ (and other relevant parameters of the class C ) such that, given a sample of size p drawn according to $\operatorname {EX} (c,D)$ , then, with probability of at least $1-\delta$ , A outputs a hypothesis $h\in C$ that has an average error less than or equal to $\epsilon$ on X with the same distribution D . Further if the above statement for algorithm A is true for every concept $c\in C$ and for every distribution D over X , and for all $0<\epsilon ,\delta <1$ then C is (efficiently) **PAC learnable** (or *distribution-free PAC learnable*). We can also say that A is a **PAC learning algorithm** for C .

## Equivalence

Under some regularity conditions these conditions are equivalent:

1. The concept class *C* is PAC learnable.
2. The VC dimension of *C* is finite.
3. *C* is a uniformly Glivenko-Cantelli class.
4. *C* is compressible in the sense of Littlestone and Warmuth
