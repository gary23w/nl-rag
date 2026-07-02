---
title: "Decision problem"
source: https://en.wikipedia.org/wiki/Decision_problem
domain: computability-theory
license: CC-BY-SA-4.0
tags: computability theory, turing machine, halting problem, church-turing thesis
fetched: 2026-07-02
---

# Decision problem

In computability theory and computational complexity theory, a **decision problem** is a computational problem that can be posed as a yes–no question on a set of input values. An example of a decision problem is deciding whether a given natural number is prime. Another example is the problem, "given two numbers *x* and *y*, does *x* evenly divide *y*?"

A **decision procedure** for a decision problem is an algorithmic method that answers the yes-no question on all inputs, and a decision problem is called **decidable** if there is a decision procedure for it. For example, the decision problem "given two numbers *x* and *y*, does *x* evenly divide *y*?" is decidable since there is a decision procedure called long division that gives the steps for determining whether *x* evenly divides *y* and the correct answer, *YES* or *NO*, accordingly. Some of the most important problems in mathematics are **undecidable**, e.g. the halting problem.

The field of computational complexity theory categorizes *decidable* decision problems by how difficult they are to solve. "Difficult", in this sense, is described in terms of the computational resources needed by the most efficient algorithm for a certain problem. On the other hand, the field of recursion theory categorizes *undecidable* decision problems by Turing degree, which is a measure of the noncomputability inherent in any solution.

## Definition

A *decision problem* is the formal language of all inputs for which the output (the answer to the yes-no question on a given input) is *YES*.

- These inputs can be natural numbers, but can also be values of some other kind, like binary strings or strings over some other alphabet.

- For example, if every input can be encoded by the alphabet $\{0,1\}$ , then a decision problem is a subset $L\subseteq \{0,1\}^{*}$ .

- For another example, using an encoding such as Gödel numbering, any string can be encoded as a natural number, via which a decision problem can be defined as a subset of the natural numbers. Therefore, the decision procedure of a decision problem is to compute the characteristic function of a subset of the natural numbers.

## Examples

A classic example of a decidable decision problem is the set of prime numbers. It is possible to effectively decide whether a given natural number is prime by testing every possible nontrivial factor. Although much more efficient procedures of primality testing are known, the existence of any effective procedure is enough to establish decidability.

## Decidability

- A decision problem is *decidable* or *effectively solvable* if the set of inputs for which the answer is *YES* is a recursive set.
- A decision problem is *partially decidable*, *semidecidable*, *solvable*, or *provable* if the set of inputs for which the answer is *YES* is a recursively enumerable set.

Problems that are not decidable are *undecidable*, which means it is not possible to create an algorithm (efficient or not) that solves them. The halting problem is an important undecidable decision problem; for more examples, see list of undecidable problems.

## Complete problems

Decision problems can be ordered according to many-one reducibility and related to feasible reductions such as polynomial-time reductions. A decision problem *P* is said to be *complete* for a set of decision problems *S* if *P* is a member of *S* and every problem in *S* can be reduced to *P*. Complete decision problems are used in computational complexity theory to characterize complexity classes of decision problems. For example, the Boolean satisfiability problem is complete for the class NP of decision problems under polynomial-time reducibility.

## Function problems

Decision problems are closely related to function problems, which can have answers that are more complex than a simple *YES* or *NO*. A corresponding function problem is "given two numbers *x* and *y*, what is *x* divided by *y*?".

A function problem consists of a partial function *f*; the informal "problem" is to compute the values of *f* on the inputs for which it is defined.

Every function problem can be turned into a decision problem; the decision problem is just the graph of the associated function. (The graph of a function *f* is the set of pairs (*x*,*y*) such that *f*(*x*) = *y*.) If this decision problem were effectively solvable then the function problem would be as well. This reduction does not respect computational complexity, however. For example, it is possible for the graph of a function to be decidable in polynomial time (in which case running time is computed as a function of the pair (*x*,*y*)) when the function is not computable in polynomial time (in which case running time is computed as a function of *x* alone). The function *f*(*x*) = 2*x* has this property.

Every decision problem can be converted into the function problem of computing the characteristic function of the set associated to the decision problem. If this function is computable then the associated decision problem is decidable. However, this reduction is more liberal than the standard reduction used in computational complexity (sometimes called polynomial-time many-one reduction); for example, the complexity of the characteristic functions of an NP-complete problem and its co-NP-complete complement is exactly the same even though the underlying decision problems may not be considered equivalent in some typical models of computation.

## Optimization problems

Unlike decision problems, for which there is only one correct answer for each input, optimization problems are concerned with finding the *best* answer to a particular input. Optimization problems arise naturally in many applications, such as the traveling salesman problem and many questions in linear programming.

Function and optimization problems are often transformed into decision problems by considering the question of whether the output is *equal to* or *less than or equal to* a given value. This allows the complexity of the corresponding decision problem to be studied; and in many cases the original function or optimization problem can be solved by solving its corresponding decision problem. For example, in the traveling salesman problem, the optimization problem is to produce a tour with minimal weight. The associated decision problem is: for each *N*, to decide whether the graph has any tour with weight less than *N*. By repeatedly answering the decision problem, it is possible to find the minimal weight of a tour.

Because the theory of decision problems is very well developed, research in complexity theory has typically focused on decision problems. Optimization problems themselves are still of interest in computability theory, as well as in fields such as operations research.
