---
title: "Randomized rounding"
source: https://en.wikipedia.org/wiki/Randomized_rounding
domain: randomized-algorithms-deep
license: CC-BY-SA-4.0
tags: randomized algorithm, monte carlo algorithm, probabilistic method, chernoff bound
fetched: 2026-07-02
---

# Randomized rounding

In computer science and operations research, **randomized rounding** is a widely used approach for designing and analyzing approximation algorithms.

Many combinatorial optimization problems are computationally intractable to solve exactly (to optimality). For such problems, randomized rounding can be used to design fast (polynomial time) approximation algorithms—that is, algorithms that are guaranteed to return an approximately optimal solution given any input.

The basic idea of randomized rounding is to convert an optimal solution of a relaxation of the problem into an approximately-optimal solution to the original problem. The resulting algorithm is usually analyzed using the probabilistic method.

## Overview

The basic approach has three steps:

1. Formulate the problem to be solved as an integer linear program (ILP).
2. Compute an optimal fractional solution x to the linear programming relaxation (LP) of the ILP.
3. Round the fractional solution x of the LP to an integer solution $x'$ of the ILP.

(Although the approach is most commonly applied with linear programs, other kinds of relaxations are sometimes used. For example, see Goemans' and Williamson's max-cut approximation algorithm, which is based on a semidefinite program which can be derived from the first level of the sum of squares hierarchy.)

In the first step, the challenge is to choose a suitable integer linear program. Familiarity with linear programming, in particular modelling using linear programs and integer linear programs, is required. For many problems, there is a natural integer linear program that works well, such as in the Set Cover example below. (The integer linear program should have a small integrality gap; indeed randomized rounding is often used to prove bounds on integrality gaps.)

In the second step, the optimal fractional solution can typically be computed in polynomial time using any standard linear programming algorithm.

In the third step, the fractional solution must be converted into an integer solution (and thus a solution to the original problem). This is called *rounding* the fractional solution. The resulting integer solution should (provably) have cost not much larger than the cost of the fractional solution. This will ensure that the cost of the integer solution is not much larger than the cost of the optimal integer solution.

The main technique used to do the third step (rounding) is to use randomization, and then to use probabilistic arguments to bound the increase in cost due to the rounding (following the probabilistic method from combinatorics). Therein, probabilistic arguments are used to show the existence of discrete structures with desired properties. In this context, one uses such arguments to show the following:

Given any fractional solution

x

of the LP, with positive probability the randomized rounding process produces an integer solution

$x'$

that approximates

x

according to some desired criterion.

Finally, to make the third step computationally efficient, one either shows that $x'$ approximates x with high probability (so that the step can remain randomized) or one derandomizes the rounding step, typically using the method of conditional probabilities. The latter method converts the randomized rounding process into an efficient deterministic process that is guaranteed to reach a good outcome.

## Example: the set cover problem

The following example illustrates how randomized rounding can be used to design an approximation algorithm for the set cover problem. Fix any instance $\langle c,{\mathcal {S}}\rangle$ of set cover over a universe ${\mathcal {U}}$ .

### Computing the fractional solution

For **step 1**, let IP be the standard integer linear program for set cover for this instance.

For **step 2**, let LP be the linear programming relaxation of IP, and compute an optimal solution $x^{*}$ to LP using any standard linear programming algorithm. This takes time polynomial in the input size. The feasible solutions to LP are the vectors x that assign each set $s\in {\mathcal {S}}$ a non-negative weight $x_{s}$ , such that, for each element $e\in {\mathcal {U}}$ , $x'$ *covers* e —the total weight assigned to the sets containing e is at least 1, that is,

$\sum _{s\ni e}x_{s}\geq 1.$

The optimal solution $x^{*}$ is a feasible solution whose cost

$\sum _{s\in {\mathcal {S}}}c(S)x_{s}^{*}$

is as small as possible. Note that any set cover ${\mathcal {C}}$ for ${\mathcal {S}}$ gives a feasible solution x (where $x_{s}=1$ for $s\in {\mathcal {C}}$ , $x_{s}=0$ otherwise). The cost of this ${\mathcal {C}}$ equals the cost of x , that is,

$\sum _{s\in {\mathcal {C}}}c(s)=\sum _{s\in {\mathcal {S}}}c(s)x_{s}.$

In other words, the linear program LP is a relaxation of the given set-cover problem.

Since $x^{*}$ has minimum cost among feasible solutions to the LP, *the cost of $x^{*}$ is a lower bound on the cost of the optimal set cover*.

### Randomized rounding step

In **step 3**, we must convert the minimum-cost fractional set cover $x^{*}$ into a feasible integer solution $x'$ (corresponding to a true set cover). The rounding step should produce an $x'$ that, with positive probability, has cost within a small factor of the cost of $x^{*}$ .Then (since the cost of $x^{*}$ is a lower bound on the cost of the optimal set cover), the cost of $x'$ will be within a small factor of the optimal cost.

As a starting point, consider the most natural rounding scheme:

For each set

$s\in {\mathcal {S}}$

in turn, take

$x'_{s}=1$

with probability

$\min(1,x_{s}^{*})$

, otherwise take

$x'_{s}=0$

.

With this rounding scheme, the expected cost of the chosen sets is at most $\sum _{s}c(s)x_{s}^{*}$ , the cost of the fractional cover. This is good. Unfortunately the coverage is not good. When the variables $x_{s}^{*}$ are small, the probability that an element e is not covered is about

$\prod _{s\ni e}1-x_{s}^{*}\approx \prod _{s\ni e}\exp(-x_{s}^{*})=\exp {\Big (}-\sum _{s\ni e}x_{s}^{*}{\Big )}\approx \exp(-1).$

So only a constant fraction of the elements will be covered in expectation.

To make $x'$ cover every element with high probability, the standard rounding scheme first *scales up* the rounding probabilities by an appropriate factor $\lambda >1$ . Here is the standard rounding scheme:

Fix a parameter

$\lambda \geq 1$

. For each set

$s\in {\mathcal {S}}$

in turn,

take

$x'_{s}=1$

with probability

$\min(\lambda x_{s}^{*},1)$

, otherwise take

$x'_{s}=0$

.

Scaling the probabilities up by $\lambda$ increases the expected cost by $\lambda$ , but makes coverage of all elements likely. The idea is to choose $\lambda$ as small as possible so that all elements are provably covered with non-zero probability. Here is a detailed analysis.

#### Lemma (approximation guarantee for rounding scheme)

Fix

$\lambda =\ln(2|{\mathcal {U}}|)$

. With positive probability, the rounding scheme returns a set cover

$x'$

of cost at most

$2\ln(2|{\mathcal {U}}|)c\cdot x^{*}$

(and thus of cost

$O(\log |{\mathcal {U}}|)$

times the cost of the optimal set cover).

(Note: with care the $O(\log |{\mathcal {U}}|)$ can be reduced to $\ln(|{\mathcal {U}}|)+O(\log \log |{\mathcal {U}}|)$ .)

#### Proof

The output $x'$ of the random rounding scheme has the desired properties as long as none of the following "bad" events occur:

1. the cost $c\cdot x'$ of $x'$ exceeds $2\lambda c\cdot x^{*}$ , or
2. for some element e , $x'$ fails to cover e .

The expectation of each $x'_{s}$ is at most $\lambda x_{s}^{*}$ . By linearity of expectation, the expectation of $c\cdot x'$ is at most $\sum _{s}c(s)\lambda x_{s}^{*}=\lambda c\cdot x^{*}$ . Thus, by Markov's inequality, the probability of the first bad event above is at most $1/2$ .

For the remaining bad events (one for each element e ), note that, since $\sum _{s\ni e}x_{s}^{*}\geq 1$ for any given element e , the probability that e is not covered is

${\begin{aligned}\prod _{s\ni e}{\big (}1-\min(\lambda x_{s}^{*},1){\big )}&<\prod _{s\ni e}\exp({-}\lambda x_{s}^{*})=\exp {\Big (}{-}\lambda \sum _{s\ni e}x_{s}^{*}{\Big )}\\&\leq \exp({-}\lambda )=1/(2|{\mathcal {U}}|).\end{aligned}}$

(This uses the inequality $1+z\leq e^{z}$ , which is strict for $z\neq 0$ .)

Thus, for each of the $|{\mathcal {U}}|$ elements, the probability that the element is not covered is less than $1/(2{\mathcal {U}})$ .

By the union bound, the probability that one of the $1+|{\mathcal {U}}|$ bad events happens is less than $1/2+|{\mathcal {U}}|/(2{\mathcal {U}})=1$ . Thus, with positive probability there are no bad events and $x'$ is a set cover of cost at most $2\lambda c\cdot x^{*}$ . QED

### Derandomization using the method of conditional probabilities

The lemma above shows the *existence* of a set cover of cost $O(\log(|{\mathcal {U}}|)c\cdot x^{*}$ ). In this context our goal is an efficient approximation algorithm, not just an existence proof, so we are not done.

One approach would be to increase $\lambda$ a little bit, then show that the probability of success is at least, say, 1/4. With this modification, repeating the random rounding step a few times is enough to ensure a successful outcome with high probability.

That approach weakens the approximation ratio. We next describe a different approach that yields a deterministic algorithm that is guaranteed to match the approximation ratio of the existence proof above. The approach is called the method of conditional probabilities.

The deterministic algorithm emulates the randomized rounding scheme: it considers each set $s\in {\mathcal {S}}$ in turn, and chooses $x'_{s}\in \{0,1\}$ . But instead of making each choice *randomly* based on $x^{*}$ , it makes the choice *deterministically*, so as to *keep the conditional probability of failure, given the choices so far, below 1*.

#### Bounding the conditional probability of failure

We want to be able to set each variable $x'_{s}$ in turn so as to keep the conditional probability of failure below 1. To do this, we need a good bound on the conditional probability of failure. The bound will come by refining the original existence proof. That proof implicitly bounds the probability of failure by the expectation of the random variable

$F={\frac {c\cdot x'}{2\lambda c\cdot x^{*}}}+|{\mathcal {U}}^{(m)}|$

,

where

${\mathcal {U}}^{(m)}={\Big \{}e:\prod _{s\ni e}(1-x'_{s})=1{\Big \}}$

is the set of elements left uncovered at the end.

The random variable F may appear a bit mysterious, but it mirrors the probabilistic proof in a systematic way. The first term in F comes from applying Markov's inequality to bound the probability of the first bad event (the cost is too high). It contributes at least 1 to F if the cost of $x'$ is too high. The second term counts the number of bad events of the second kind (uncovered elements). It contributes at least 1 to F if $x'$ leaves any element uncovered. Thus, in any outcome where F is less than 1, $x'$ must cover all the elements and have cost meeting the desired bound from the lemma. In short, if the rounding step fails, then $F\geq 1$ . This implies (by Markov's inequality) that *$E[F]$ is an upper bound on the probability of failure.* Note that the argument above is implicit already in the proof of the lemma, which also shows by calculation that $E[F]<1$ .

To apply the method of conditional probabilities, we need to extend the argument to bound the *conditional* probability of failure as the rounding step proceeds. Usually, this can be done in a systematic way, although it can be technically tedious.

So, what about the *conditional* probability of failure as the rounding step iterates through the sets? Since $F\geq 1$ in any outcome where the rounding step fails, by Markov's inequality, the *conditional* probability of failure is at most the *conditional* expectation of F .

Next we calculate the conditional expectation of F , much as we calculated the unconditioned expectation of F in the original proof. Consider the state of the rounding process at the end of some iteration t . Let $S^{(t)}$ denote the sets considered so far (the first t sets in ${\mathcal {S}}$ ). Let $x^{(t)}$ denote the (partially assigned) vector $x'$ (so $x_{s}^{(t)}$ is determined only if $s\in S^{(t)}$ ). For each set $s\not \in S^{(t)}$ , let $p_{s}=\min(\lambda x_{s}^{*},1)$ denote the probability with which $x'_{s}$ will be set to 1. Let ${\mathcal {U}}^{(t)}$ contain the not-yet-covered elements. Then the conditional expectation of F , given the choices made so far, that is, given $x^{(t)}$ , is

$E[F|x^{(t)}]~=~{\frac {\sum _{s\in S^{(t)}}c(s)x'_{s}+\sum _{s\not \in S^{(t)}}c(s)p_{s}}{2\lambda c\cdot x^{*}}}~+~\sum _{e\in {\mathcal {U}}^{(t)}}\prod _{s\not \in S^{(t)},s\ni e}(1-p_{s}).$

Note that $E[F|x^{(t)}]$ is determined only after iteration t .

#### Keeping the conditional probability of failure below 1

To keep the conditional probability of failure below 1, it suffices to keep the conditional expectation of F below 1. To do this, it suffices to keep the conditional expectation of F from increasing. This is what the algorithm will do. It will set $x'_{s}$ in each iteration to ensure that

$E[F|x^{(m)}]\leq E[F|x^{(m-1)}]\leq \cdots \leq E[F|x^{(1)}]\leq E[F|x^{(0)}]<1$

(where $m=|{\mathcal {S}}|$ ).

In the t th iteration, how can the algorithm set $x'_{s'}$ to ensure that $E[F|x^{(t)}]\leq E[F|S^{(t-1)}]$ ? It turns out that it can simply set $x'_{s'}$ so as to *minimize* the resulting value of $E[F|x^{(t)}]$ .

To see why, focus on the point in time when iteration t starts. At that time, $E[F|x^{(t-1)}]$ is determined, but $E[F|x^{(t)}]$ is not yet determined --- it can take two possible values depending on how $x'_{s'}$ is set in iteration t . Let $E^{(t-1)}$ denote the value of $E[F|x'^{(t-1)}]$ . Let $E_{0}^{(t)}$ and $E_{1}^{(t)}$ , denote the two possible values of $E[F|x^{(t)}]$ , depending on whether $x'_{s'}$ is set to 0, or 1, respectively. By the definition of conditional expectation,

$E^{(t-1)}~=~\Pr[x'_{s'}=0]E_{0}^{(t)}+\Pr[x'_{s'}=1]E_{1}^{(t)}.$

Since a weighted average of two quantities is always at least the minimum of those two quantities, it follows that

$E^{(t-1)}~\geq ~\min(E_{0}^{(t)},E_{1}^{(t)}).$

Thus, setting $x'_{s'}$ so as to minimize the resulting value of $E[F|x^{(t)}]$ will guarantee that $E[F|x^{(t)}]\leq E[F|x^{(t-1)}]$ . This is what the algorithm will do.

In detail, what does this mean? Considered as a function of $x'_{s'}$ (with all other quantities fixed) $E[F|x^{(t)}]$ is a linear function of $x'_{s'}$ , and the coefficient of $x'_{s'}$ in that function is

${\frac {c_{s'}}{2\lambda c\cdot x^{*}}}~-~\sum _{e\in s'\cap {\mathcal {U}}_{t-1}}\prod _{s\not \in S^{(t)},s\ni e}(1-p_{s}).$

Thus, the algorithm should set $x'_{s'}$ to 0 if this expression is positive, and 1 otherwise. This gives the following algorithm.

### Randomized-rounding algorithm for set cover

**input:** set system ${\mathcal {S}}$ , universe ${\mathcal {U}}$ , cost vector c

**output:** set cover $x'$ (a solution to the standard integer linear program for set cover)

1. Compute a min-cost fractional set cover $x^{*}$ (an optimal solution to the LP relaxation).
2. Let $\lambda \leftarrow \ln(2|{\mathcal {U}}|)$ . Let $p_{s}\leftarrow \min(\lambda x_{s}^{*},1)$ for each $s\in {\mathcal {S}}$ .
3. For each $s'\in {\mathcal {S}}$ do:
  1. Let ${\mathcal {S}}\leftarrow {\mathcal {S}}-\{s'\}$ .   ( ${\mathcal {S}}$ contains the not-yet-decided sets.)
  2. If    ${\frac {c_{s'}}{2\lambda c\cdot x^{*}}}>\sum _{e\in s'\cap {\mathcal {U}}}\prod _{s\in {\mathcal {S}},s\ni e}(1-p_{s})$ then set $x'_{s}\leftarrow 0$ , else set $x'_{s}\leftarrow 1$ and ${\mathcal {U}}\leftarrow {\mathcal {U}}-s'$ .   ( ${\mathcal {U}}$ contains the not-yet-covered elements.)
4. Return $x'$ .

#### lemma (approximation guarantee for algorithm)

The algorithm above returns a set cover

$x'$

of cost at most

$2\ln(2|{\mathcal {U}}|)$

times the minimum cost of any (fractional) set cover.

#### proof

The algorithm ensures that the conditional expectation of F , $E[F\,|\,x^{(t)}]$ , does not increase at each iteration. Since this conditional expectation is initially less than 1 (as shown previously), the algorithm ensures that the conditional expectation stays below 1. Since the conditional probability of failure is at most the conditional expectation of F , in this way the algorithm ensures that the conditional probability of failure stays below 1. Thus, at the end, when all choices are determined, the algorithm reaches a successful outcome. That is, the algorithm above returns a set cover $x'$ of cost at most $2\ln(2|{\mathcal {U}}|)$ times the minimum cost of any (fractional) set cover.

### Remarks

In the example above, the algorithm was guided by the conditional expectation of a random variable F . In some cases, instead of an exact conditional expectation, an *upper bound* (or sometimes a lower bound) on some conditional expectation is used instead. This is called a pessimistic estimator.

## Comparison to other applications of the probabilistic method

The randomized rounding step differs from most applications of the probabilistic method in two respects:

1. The computational complexity of the rounding step is important. It should be implementable by a fast (e.g. polynomial time) algorithm.
2. The probability distribution underlying the random experiment is a function of the solution x of a relaxation of the problem instance. This fact is crucial to proving the performance guarantee of the approximation algorithm --- that is, that for any problem instance, the algorithm returns a solution that approximates the *optimal solution for that specific instance*. In comparison, applications of the probabilistic method in combinatorics typically show the existence of structures whose features depend on other parameters of the input. For example, consider Turán's theorem, which can be stated as "any graph with n vertices of average degree d must have an independent set of size at least $n/(d+1)$ . (See this for a probabilistic proof of Turán's theorem.) While there are graphs for which this bound is tight, there are also graphs which have independent sets much larger than $n/(d+1)$ . Thus, the size of the independent set shown to exist by Turán's theorem in a graph may, in general, be much smaller than the maximum independent set for that graph.
