---
title: "Stochastic simulation"
source: https://en.wikipedia.org/wiki/Stochastic_simulation
domain: discrete-event-simulation
license: CC-BY-SA-4.0
tags: discrete-event simulation, stochastic simulation, poisson point process, queueing theory
fetched: 2026-07-02
---

# Stochastic simulation

A **stochastic simulation** is a simulation of a system that has variables that can change stochastically (randomly) with individual probabilities.

Realizations of these random variables are generated and inserted into a model of the system. Outputs of the model are recorded, and then the process is repeated with a new set of random values. These steps are repeated until a sufficient amount of data is gathered. In the end, the distribution of the outputs shows the most probable estimates as well as a frame of expectations regarding what ranges of values the variables are more or less likely to fall in.

Often random variables inserted into the model are created on a computer with a random number generator (RNG). The U(0,1) uniform distribution outputs of the random number generator are then transformed into random variables with probability distributions that are used in the system model.

## Etymology

*Stochastic* originally meant "pertaining to conjecture"; from Greek stokhastikos "able to guess, conjecturing": from stokhazesthai "guess"; from stokhos "a guess, aim, target, mark". The sense of "randomly determined" was first recorded in 1934, from German Stochastik.

## Discrete-event simulation

In order to determine the next event in a stochastic simulation, the rates of all possible changes to the state of the model are computed, and then ordered in an array. Next, the cumulative sum of the array is taken, and the final cell contains the number R, where R is the total event rate. This cumulative array is now a discrete cumulative distribution, and can be used to choose the next event by picking a random number z~U(0,R) and choosing the first event, such that z is less than the rate associated with that event.

### Probability distributions

A probability distribution is used to describe the potential outcome of a random variable.

Limits the outcomes where the variable can only take on discrete values.

#### Bernoulli distribution

A random variable X is Bernoulli-distributed with parameter p if it has two possible outcomes usually encoded 1 (success or default) or 0 (failure or survival) where the probabilities of success and failure are $P(X=1)=p$ and $P(X=0)=1-p$ where $0\leq p\leq 1$ .

To produce a random variable X with a Bernoulli distribution from a U(0,1) uniform distribution made by a random number generator, we define $X={\begin{cases}1,&{\text{if }}0\leq U<p\\0,&{\text{if }}1\geq U\geq p\end{cases}}$ such that the probability for $P(X=1)=P(0\leq U<p)=p$ and $P(X=0)=P(1\geq U\geq p)=1-p$ .

##### Example: Toss of coin

Define $X={\begin{cases}1&{\text{if heads comes up}}\\0&{\text{if tails comes up}}\end{cases}}$ For a fair coin, both realizations are equally likely. We can generate realizations of this random variable X from a $U(1,0)$ uniform distribution provided by a random number generator (RNG) by having $X=1$ if the RNG outputs a value between 0 and 0.5 and $X=0$ if the RNG outputs a value between 0.5 and 1. ${\begin{aligned}P(X=1)&=P(0\leq U<1/2)=1/2\\P(X=0)&=P(1\geq U\geq 1/2)=1/2\end{aligned}}$ Of course, the two outcomes may not be equally likely (e.g. success of medical treatment).

#### Binomial distribution

A binomial distributed random variable Y with parameters *n* and *p* is obtained as the sum of *n* independent and identically Bernoulli-distributed random variables *X*1, *X*2, ..., *X**n*

Example: A coin is tossed three times. Find the probability of getting exactly two heads. This problem can be solved by looking at the sample space. There are three ways to get two heads.

HHH,

HHT, HTH, THH

, TTH, THT, HTT, TTT

The answer is 3/8 (= 0.375).

#### Poisson distribution

A poisson process is a process where events occur randomly in an interval of time or space. The probability distribution for Poisson processes with constant rate *λ* per time interval is given by the following equation. $P(k{\text{ events in interval}})={\frac {\lambda ^{k}e^{-\lambda }}{k!}}$

Defining $N(t)$ as the number of events that occur in the time interval t $P(N(t)=k)={\frac {(t\lambda )^{k}}{k!}}e^{-t\lambda }$

It can be shown that inter-arrival times for events is exponentially distributed with a cumulative distribution function (CDF) of $F(t)=1-e^{-t\lambda }$ . The inverse of the exponential CDF is given by $t=-{\frac {1}{\lambda }}\ln(u)$ where u is an $U(0,1)$ uniformly distributed random variable.

Simulating a Poisson process with a constant rate $\lambda$ for the number of events N that occur in interval $[t_{\text{start}},t_{\text{end}}]$ can be carried out with the following algorithm.

1. Begin with $N=0$ and $t=t_{\text{start}}$
2. Generate random variable u from $U(0,1)$ uniform distribution
3. Update the time with $t=t-\ln(u)/\lambda$
4. If $t>t_{\text{end}}$ , then stop. Else continue to step 5.
5. $N=N+1$
6. Continue to step 2

### Methods

#### Direct and first reaction methods

Published by Dan Gillespie in 1977, and is a linear search on the cumulative array. See Gillespie algorithm.

Gillespie’s Stochastic Simulation Algorithm (SSA) is essentially an exact procedure for numerically simulating the time evolution of a well-stirred chemically reacting system by taking proper account of the randomness inherent in such a system.

It is rigorously based on the same microphysical premise that underlies the chemical master equation and gives a more realistic representation of a system’s evolution than the deterministic reaction rate equation (RRE) represented mathematically by ODEs.

As with the chemical master equation, the SSA converges, in the limit of large numbers of reactants, to the same solution as the law of mass action.

#### Next reaction method

Published 2000 by Gibson and Bruck the next reaction method improves over the first reaction method by reducing the amount of random numbers that need to be generated. To make the sampling of reactions more efficient, an indexed [priority queue] is used to store the reaction times. To make the computation of reaction propensities more efficient, a dependency graph is also used. This dependency graph tells which reaction propensities to update after a particular reaction has fired. While more efficient, the next reaction method requires more complex data structures than either direct simulation or the first reaction method.

#### Optimised and sorting direct methods

Published 2004 and 2005. These methods sort the cumulative array to reduce the average search depth of the algorithm. The former runs a presimulation to estimate the firing frequency of reactions, whereas the latter sorts the cumulative array on-the-fly.

#### Logarithmic direct method

Published in 2006. This is a binary search on the cumulative array, thus reducing the worst-case time complexity of reaction sampling to O (log M).

#### Partial-propensity methods

Published in 2009, 2010, and 2011 (Ramaswamy 2009, 2010, 2011). Use factored-out, partial reaction propensities to reduce the computational cost to scale with the number of species in the network, rather than the (larger) number of reactions. Four variants exist:

- PDM, the partial-propensity direct method. Has a computational cost that scales linearly with the number of different species in the reaction network, independent of the coupling class of the network (Ramaswamy 2009).
- SPDM, the sorting partial-propensity direct method. Uses dynamic bubble sort to reduce the pre-factor of the computational cost in multi-scale reaction networks where the reaction rates span several orders of magnitude (Ramaswamy 2009).
- PSSA-CR, the partial-propensity SSA with composition-rejection sampling. Reduces the computational cost to constant time (i.e., independent of network size) for weakly coupled networks (Ramaswamy 2010) using composition-rejection sampling (Slepoy 2008).
- dPDM, the delay partial-propensity direct method. Extends PDM to reaction networks that incur time delays (Ramaswamy 2011) by providing a partial-propensity variant of the delay-SSA method (Bratsun 2005, Cai 2007).

The use of partial-propensity methods is limited to elementary chemical reactions, i.e., reactions with at most two different reactants. Every non-elementary chemical reaction can be equivalently decomposed into a set of elementary ones, at the expense of a linear (in the order of the reaction) increase in network size.

### Approximate Methods

A general drawback of stochastic simulations is that for big systems, too many events happen which cannot all be taken into account in a simulation. The following methods can dramatically improve simulation speed by some approximations.

#### τ leaping method

Since the SSA method keeps track of each transition, it would be impractical to implement for certain applications due to high time complexity. Gillespie proposed an approximation algorithm, the tau-leaping method which decreases computational time with minimal loss of accuracy. Instead of taking incremental steps in time, keeping track of *X*(*t*) at each time step as in the SSA method, the tau-leaping method leaps from one subinterval to the next, approximating how many transitions take place during a given subinterval. It is assumed that the value of the leap, τ, is small enough that there is no significant change in the value of the transition rates along the subinterval [*t*, *t* + *τ*]. This condition is known as the leap condition. The tau-leaping method thus has the advantage of simulating many transitions in one leap while not losing significant accuracy, resulting in a speed up in computational time.

#### Conditional Difference Method

This method approximates reversible processes (which includes random walk/diffusion processes) by taking only net rates of the opposing events of a reversible process into account. The main advantage of this method is that it can be implemented with a simple if-statement replacing the previous transition rates of the model with new, effective rates. The model with the replaced transition rates can thus be solved, for instance, with the conventional SSA.

## Continuous simulation

While in discrete state space it is clearly distinguished between particular states (values) in continuous space it is not possible due to certain continuity. The system usually change over time, variables of the model, then change continuously as well. Continuous simulation thereby simulates the system over time, given differential equations determining the rates of change of state variables. Example of continuous system is *the predator/prey model* or cart-pole balancing

### Probability distributions

#### Normal distribution

The random variable X is said to be normally distributed with parameters μ and σ, abbreviated by *X* ∈ *N*(*μ*, *σ*2), if the density of the random variable is given by the formula $f_{X}(x)={\frac {1}{\sqrt {2\pi \sigma ^{2}}}}e^{-{\frac {(x-\mu )^{2}}{2\sigma ^{2}}}},\quad x\in \mathbb {R} .$

Many things actually are normally distributed, or very close to it. For example, height and intelligence are approximately normally distributed; measurement errors also often have a normal distribution.

#### Exponential distribution

Exponential distribution describes the time between events in a Poisson process, i.e. a process in which events occur continuously and independently at a constant average rate.

The exponential distribution is popular, for example, in queuing theory when we want to model the time we have to wait until a certain event takes place. Examples include the time until the next client enters the store, the time until a certain company defaults or the time until some machine has a defect.

#### Student's t-distribution

Student's t-distribution are used in finance as probabilistic models of assets returns. The density function of the t-distribution is given by the following equation: $f(t)={\frac {\Gamma ({\frac {\nu +1}{2}})}{{\sqrt {\nu \pi }}\,\Gamma ({\frac {\nu }{2}})}}\left(1+{\frac {t^{2}}{\nu }}\right)^{-{\frac {\nu +1}{2}}},$ where $\nu$ is the number of *degrees of freedom* and $\Gamma$ is the gamma function.

For large values of *n*, the t-distribution doesn't significantly differ from a standard normal distribution. Usually, for values *n* > 30, the t-distribution is considered as equal to the standard normal distribution.

#### Other distributions

- Generalized extreme value distribution

## Combined simulation

It is often possible to model one and the same system by use of completely different world views. Discrete event simulation of a problem as well as continuous event simulation of it (continuous simulation with the discrete events that disrupt the continuous flow) may lead eventually to the same answers. Sometimes however, the techniques can answer different questions about a system. If we necessarily need to answer all the questions, or if we don't know what purposes is the model going to be used for, it is convenient to apply combined continuous/discrete methodology. Similar techniques can change from a discrete, stochastic description to a deterministic, continuum description in a time-and space dependent manner. The use of this technique enables the capturing of noise due to small copy numbers, while being much faster to simulate than the conventional Gillespie algorithm. Furthermore, the use of the deterministic continuum description enables the simulations of arbitrarily large systems.

## Monte Carlo simulation

Monte Carlo is an estimation procedure. The main idea is that if it is necessary to know the average value of some random variable and its distribution cannot be stated, and if it is possible to take samples from the distribution, we can estimate it by taking the samples, independently, and averaging them. If there are sufficient samples, then the law of large numbers says the average must be close to the true value. The central limit theorem says that the average has a Gaussian distribution around the true value.

As a simple example, suppose we need to measure area of a shape with a complicated, irregular outline. The Monte Carlo approach is to draw a square around the shape and measure the square. Then we throw darts into the square, as uniformly as possible. The fraction of darts falling on the shape gives the ratio of the area of the shape to the area of the square. In fact, it is possible to cast almost any integral problem, or any averaging problem, into this form. It is necessary to have a good way to tell if you're inside the outline, and a good way to figure out how many darts to throw. Last but not least, we need to throw the darts uniformly, i.e., using a good random number generator.

### Application

There are wide possibilities for use of Monte Carlo Method:

- Statistic experiment using generation of random variables (e.g. dice)
- sampling method
- Mathematics (e.g. numerical integration, multiple integrals)
- Reliability Engineering
- Project Management (SixSigma)
- Experimental particle physics
- Simulations
- Risk Measurement/Risk Management (e.g. Portfolio value estimation)
- Economics (e.g. finding the best fitting demand curve)
- Process Simulation
- Operations Research

## Random number generators

Source:

For simulation experiments (including Monte Carlo) it is necessary to generate random numbers (as values of variables). The problem is that the computer is highly deterministic machine—basically, behind each process there is always an algorithm, a deterministic computation changing inputs to outputs; therefore it is not easy to generate uniformly spread random numbers over a defined interval or set.

A random number generator is a device capable of producing a sequence of numbers which cannot be "easily" identified with deterministic properties. This sequence is then called a *sequence of stochastic numbers*.

The algorithms typically rely on pseudorandom numbers, computer generated numbers mimicking true random numbers, to generate a realization, one possible outcome of a process.

Methods for obtaining random numbers have existed for a long time and are used in many different fields (such as gaming). However, these numbers suffer from a certain bias. Currently the best methods expected to produce truly random sequences are natural methods that take advantage of the random nature of quantum phenomena.
