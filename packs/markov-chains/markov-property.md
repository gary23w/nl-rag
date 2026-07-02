---
title: "Markov property"
source: https://en.wikipedia.org/wiki/Markov_property
domain: markov-chains
license: CC-BY-SA-4.0
tags: markov chain, markov property, stochastic matrix, hidden markov model
fetched: 2026-07-02
---

# Markov property

In probability theory and statistics, the **Markov property** is the memoryless property of a stochastic process, which means that its future evolution is independent of its history. It is named after the Russian mathematician Andrey Markov. The term **strong Markov property** is similar to the Markov property, except that the meaning of "present" is defined in terms of a random variable known as a stopping time.

The term **Markov assumption** is used to describe a model where the Markov property is assumed to hold, such as a hidden Markov model.

A Markov random field extends this property to two or more dimensions or to random variables defined for an interconnected network of items. An example of a model for such a field is the Ising model.

A discrete-time stochastic process satisfying the Markov property is known as a Markov chain.

## Introduction

A stochastic process has the Markov property if the conditional probability distribution of future states of the process (conditional on both past and present values) depends only upon the present state; that is, given the present, the future does not depend on the past. A process with this property is said to be **Markov** or **Markovian** and known as a **Markov process**. Two famous classes of Markov process are the Markov chain and Brownian motion.

Note that there is a subtle, often overlooked and very important point that is often missed in the plain English statement of the definition: the statespace of the process is constant through time. The conditional description involves a fixed "bandwidth". For example, without this restriction we could augment any process to one which includes the complete history from a given initial condition and it would be made to be Markovian. But the state space would be of increasing dimensionality over time and does not meet the definition.

## History

## Definition

Let $(\Omega ,{\mathcal {F}},P)$ be a probability space with a filtration $({\mathcal {F}}_{s},\ s\in I)$ , for some (totally ordered) index set I ; and let $(S,\Sigma )$ be a measurable space. An $(S,\Sigma )$ -valued stochastic process $X=\{X_{t}:\Omega \to S\}_{t\in I}$ adapted to the filtration is said to possess the *Markov property* if, for each $A\in \Sigma$ and each $s,t\in I$ with $s<t$ ,

$P(X_{t}\in A\mid {\mathcal {F}}_{s})=P(X_{t}\in A\mid X_{s}).$

In the case where S is a discrete set with the discrete sigma algebra and $I=\mathbb {N}$ , this can be reformulated as follows:

$P(X_{n+1}=x_{n+1}\mid X_{n}=x_{n},\dots ,X_{1}=x_{1})=P(X_{n+1}=x_{n+1}\mid X_{n}=x_{n}){\text{ for all }}n\in \mathbb {N} .$

In other words, the distribution of X at time $n+1$ depend solely on the state of X at time n and is independent of the state of the process at any time previous to n , which corresponds precisely to the intuition described in the introduction.

If $I=[0,\infty )$ , then X is called *time-homogeneous* if for all $t,s\geq 0$ the weak Markov property holds:

$P(X_{t+s}\in A\mid {\mathcal {F}}_{s})=P(X_{t}\in A\mid X_{0}=x)|_{x=X_{s}}=:P^{X_{s}}(X_{t}\in A)$

.

The newly introduced probability measure $P^{x}(X_{t}\in \cdot )$ , $x\in S$ , has the following intuition: It gives the probability that the process X lies in some set at time t , when it was started in x at time zero. The function $P_{t}(x,A):=P^{x}(X_{t}\in A)$ , $(t,x,A)\in \mathbb {R} _{+}\times S\times \Sigma$ , is also called the *transition function* of X and the collection $(P_{t})_{t\geq 0}$ its *transition semigroup*.

## Alternative formulations

There exists multiple alternative formulations of the elementary Markov property described above. The following are all equivalent:

- For all $t\geq 0$ the $\sigma$ -algebras ${\mathcal {F}}_{t}$ and ${\mathcal {F}}_{t}':=\sigma (X_{s}:s\geq t)$ are conditionally independent given $X_{t}$ . In other words, for all $A\in {\mathcal {F}}_{t}$ , $B\in {\mathcal {F}}_{t}'$ :

$P(A\cap B\mid X_{t})=P(A\mid X_{t})P(B\mid X_{t})$ .

- For all $t\geq 0$ , $B\in {\mathcal {F}}_{t}'$ :

$P(B\mid {\mathcal {F}}_{t})=P(B\mid X_{t})$ .

- For all $t\geq 0$ , $A\in {\mathcal {F}}_{t}$ :

$P(A\mid {\mathcal {F}}_{t}^{'})=P(A\mid X_{t})$ .

- For all $t\geq 0$ and $Y:\Omega \rightarrow \mathbb {R}$ bounded and ${\mathcal {F}}_{t}'$ -measurable

$\operatorname {E} [Y\mid {\mathcal {F}}_{t}]=\operatorname {E} [Y\mid X_{t}]$ .

- For all $t\geq s\geq 0$ and $f:S\rightarrow \mathbb {R}$ bounded and measurable

$\operatorname {E} [f(X_{t})\mid {\mathcal {F}}_{s}]=\operatorname {E} [f(X_{t})\mid X_{s}]$ .

- For all $t\geq s\geq 0$ and $f:S\rightarrow \mathbb {R}$ continuous with compact support

$\operatorname {E} [f(X_{t})\mid {\mathcal {F}}_{s}]=\operatorname {E} [f(X_{t})\mid X_{s}]$ .

- For all $0\leq s_{1}<...<s_{n}<s<t$ and $f:S\rightarrow \mathbb {R}$ continuous with compact support

$\operatorname {E} [f(X_{t})\mid X_{s},X_{s_{n}},...,X_{s_{1}}]=\operatorname {E} [f(X_{t})\mid X_{s}]$ .

If there exists a so-called *shift-semigroup* $(\theta _{t})_{t\geq 0}$ , i.e., functions $\theta _{t}:\Omega \to \Omega$ such that

1. $\theta _{0}=\mathrm {id} _{\Omega }$ ,
2. $\theta _{t}\circ \theta _{s}=\theta _{t+s}\quad \forall s,t\geq 0$ (semigroup property),
3. $X_{t}\circ \theta _{s}=X_{t+s}\quad \forall s,t\geq 0$ ,

then the Markov property is equivalent to:

- For all $t\geq 0$ and $\Lambda \in {\mathcal {F}}_{0}'$

$P(\theta _{t}^{-1}(\Lambda )\mid {\mathcal {F}}_{t})=P(\theta _{t}^{-1}(\Lambda )\mid X_{t})$ .

- For all $t\geq 0$ and $Y:\Omega \rightarrow \mathbb {R}$ bounded and ${\mathcal {F}}_{0}'$ -measurable

$\operatorname {E} [Y\circ \theta _{t}\mid {\mathcal {F}}_{t}]=\operatorname {E} [Y\circ \theta _{t}\mid X_{t}]$ .

Depending on the situation, some formulations might be easier to verify or to use than others.

## Strong Markov property

Suppose that $X=(X_{t}:t\geq 0)$ is a stochastic process on a probability space $(\Omega ,{\mathcal {F}},P)$ with natural filtration $\{{\mathcal {F}}_{t}\}_{t\geq 0}$ . Then for any stopping time $\tau$ on $\Omega$ , we can define

${\mathcal {F}}_{\tau }=\{A\in {\mathcal {F}}:\forall t\geq 0,\{\tau \leq t\}\cap A\in {\mathcal {F}}_{t}\}$

.

Then X is said to have the strong Markov property if, for each stopping time $\tau$ , conditional on the event $\{\tau <\infty \}$ , we have that for each $t\geq 0$ , $X_{\tau +t}$ is independent of ${\mathcal {F}}_{\tau }$ given $X_{\tau }$ . This is equivalent to

$P(X_{\tau +t}\in A,\tau <\infty \mid {\mathcal {F}}_{\tau })=1_{\{\tau <\infty \}}P(X_{t}\in A\mid X_{0}=X_{\tau })$

for all

$A\in {\mathcal {F}}$

,

where $1_{\{\tau <\infty \}}$ denotes to indicator function of the set $\{\tau <\infty \}$ .

The strong Markov property implies the ordinary Markov property since by taking the stopping time $\tau =t$ , the ordinary Markov property can be deduced. The converse is in general not true.

The strong Markov property only leads to non-trivial results in continuous time (i.e., results which do not hold with merely the Markov property), as in the discrete case the strong and the elementary Markov property are equivalent.

## Feller property

Although the strong Markov property is in general stronger than the elementary Markov property, it is fulfilled by Markov processes with sufficiently "nice" regularity properties.

A continuous time Markov process is said to have the *Feller property*, if its transition semigroup $(P_{t})_{t\geq 0}$ (see above) fulfills

1. $P_{t}f:=\int f(x)P_{t}(\cdot ,dx)\in C_{0}(S)$ for all $f\in C_{0}(S)$ ,
2. $\lim _{t\to 0}||P_{t}f-f||_{\infty }=0$ for all $f\in C_{0}(S)$ ,

where $C_{0}(S)$ denotes the set of continuous functions vanishing at infinity and $||\cdot ||_{\infty }$ the sup norm. Then one can show that (if the filtration is augmented) such a process has a version with right-continuous (even càdlàg) paths, which in turn fulfills the strong Markov property.

## Examples

### Intuitive example

Assume that an urn contains two red balls and one green ball. One ball was drawn yesterday, one ball was drawn today, and the final ball will be drawn tomorrow. All of the draws are "without replacement".

Suppose you know that today's ball was red, but you have no information about yesterday's ball. The chance that tomorrow's ball will be red is 1/2. That's because the only two remaining outcomes for this random experiment are:

| Day | Outcome 1 | Outcome 2 |
|---|---|---|
| Yesterday | Red | Green |
| Today | Red | Red |
| Tomorrow | Green | Red |

On the other hand, if you know that both today and yesterday's balls were red, then you are guaranteed to get a green ball tomorrow.

This discrepancy shows that the probability distribution for tomorrow's color depends not only on the present value, but is also affected by information about the past. This stochastic process of observed colors doesn't have the Markov property. Using the same experiment above, if sampling "without replacement" is changed to sampling "with replacement," the process of observed colors will have the Markov property.

### Stochastic processes

Many prominent stochastic processes are Markov processes: The Brownian motion, the Brownian bridge, the stochastic exponential, the Ornstein-Uhlenbeck process and the Poisson process have the Markov property.

More generally, any semimartingale X with values in $\mathbb {R} ^{n}$ that is given by the stochastic differential equation

$X_{t}=X_{0}+\sum _{i=1}^{d}{\Big [}\int _{0}^{t}g_{i}(X_{s})ds+\int _{0}^{t}f_{i}(X_{s})dB_{s}^{i}{\Big ]}$

,

where $B=(B^{1},...,B^{d})$ is a d -dimensional Brownian motion and $f_{1},...,f_{d},g_{1},...,g_{d}:\mathbb {R} ^{n}\to \mathbb {R} ^{n}$ are autonomous (i.e., they do not depend on time) Lipschitz functions, is time-homogeneous and has the strong Markov property. If $f_{1},...,f_{d},g_{1},...,g_{d}$ are not autonomous, then X still has the elementary Markov property.

## Applications

### Forecasting

In the fields of predictive modelling and probabilistic forecasting, the Markov property is considered desirable since it may enable the reasoning and resolution of the problem that otherwise would not be possible to be resolved because of its intractability. Such a model is known as a Markov model.

### Markov Chain Monte Carlo

An application of the Markov property in a generalized form is in Markov chain Monte Carlo computations in the context of Bayesian statistics.
