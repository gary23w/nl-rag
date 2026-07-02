---
title: "Birth–death process"
source: https://en.wikipedia.org/wiki/Birth%E2%80%93death_process
domain: queueing-theory
license: CC-BY-SA-4.0
tags: queueing theory, birth-death process, kendall notation, little's law
fetched: 2026-07-02
---

# Birth–death process

The **birth–death process** (or **birth-and-death process**) is a special case of continuous-time Markov process where the state transitions are of only two types: "births", which increase the state variable by one and "deaths", which decrease the state by one. It was introduced by William Feller. The model's name comes from a common application, the use of such models to represent the current size of a population where the transitions are literal births and deaths. Birth–death processes have many applications in demography, queueing theory, performance engineering, epidemiology, biology and other areas. They may be used, for example, to study the evolution of bacteria, the number of people with a disease within a population, or the number of customers in line at the supermarket.

## Definition

When a birth occurs, the process goes from state *n* to *n* + 1. When a death occurs, the process goes from state *n* to state *n* − 1. The process is specified by positive birth rates $\{\lambda _{i}\}_{i=0\dots \infty }$ and positive death rates $\{\mu _{i}\}_{i=1\dots \infty }$ . The number of individuals in the process at time t is denoted by $X(t)$ . The process has the Markov property and $P_{i,j}(t)={\mathsf {P}}\{X(t+s)=j|X(s)=i\}$ describes how $X(t)$ changes through time. For small $\Delta t>0$ , the function $P_{i,j}(\Delta t)$ is assumed to satisfy the following properties:

$P_{i,i+1}(\Delta t)=\lambda _{i}\Delta t+o(\Delta t),\quad i\geq 0,$

$P_{i,i-1}(\Delta t)=\mu _{i}\Delta t+o(\Delta t),\quad i\geq 1,$

$P_{i,i}(\Delta t)=1-(\lambda _{i}+\mu _{i})\Delta t+o(\Delta t),\quad i\geq 1.$

This process is represented by the following figure with the states of the process (i.e. the number of individuals in the population) depicted by the circles, and transitions between states indicated by the arrows.

(State diagram of a birth-death process)

## Recurrence and transience

For recurrence and transience in Markov processes see Section 5.3 from Markov chain.

### Conditions for recurrence and transience

Conditions for recurrence and transience were established by Samuel Karlin and James McGregor.

A birth-and-death process is

recurrent

if and only if

$\sum _{i=1}^{\infty }\prod _{n=1}^{i}{\frac {\mu _{n}}{\lambda _{n}}}=\infty .$

A birth-and-death process is

ergodic

if and only if

$\sum _{i=1}^{\infty }\prod _{n=1}^{i}{\frac {\mu _{n}}{\lambda _{n}}}=\infty \quad {\text{and}}\quad \sum _{i=1}^{\infty }\prod _{n=1}^{i}{\frac {\lambda _{n-1}}{\mu _{n}}}<\infty .$

A birth-and-death process is

null-recurrent

if and only if

$\sum _{i=1}^{\infty }\prod _{n=1}^{i}{\frac {\mu _{n}}{\lambda _{n}}}=\infty \quad {\text{and}}\quad \sum _{i=1}^{\infty }\prod _{n=1}^{i}{\frac {\lambda _{n-1}}{\mu _{n}}}=\infty .$

By using the **extended Bertrand's test**, the conditions for recurrence, transience, ergodicity and null-recurrence can be derived in a more explicit form.

For integer $K\geq 1,$ let $\ln _{(K)}(x)$ denote the K th iterate of natural logarithm, i.e. $\ln _{(1)}(x)=\ln(x)$ and for any $2\leq k\leq K$ , $\ln _{(k)}(x)=\ln _{(k-1)}(\ln(x))$ .

Then, the conditions for recurrence and transience of a birth-and-death process are as follows.

The birth-and-death process is transient if there exist

$c>1,$

$K\geq 1$

and

$n_{0}$

such that for all

$n>n_{0}$

${\frac {\lambda _{n}}{\mu _{n}}}\geq 1+{\frac {1}{n}}+{\frac {1}{n}}\sum _{k=1}^{K-1}{\frac {1}{\prod _{j=1}^{k}\ln _{(j)}(n)}}+{\frac {c}{n\prod _{j=1}^{K}\ln _{(j)}(n)}},$

where the empty sum for $K=1$ is assumed to be 0.

The birth-and-death process is recurrent if there exist

$K\geq 1$

and

$n_{0}$

such that for all

$n>n_{0}$

${\frac {\lambda _{n}}{\mu _{n}}}\leq 1+{\frac {1}{n}}+{\frac {1}{n}}\sum _{k=1}^{K}{\frac {1}{\prod _{j=1}^{k}\ln _{(j)}(n)}}.$

Wider classes of birth-and-death processes, for which the conditions for recurrence and transience can be established, can be found in.

### Application

Consider one-dimensional random walk $S_{t},\ t=0,1,\ldots ,$ that is defined as follows. Let $S_{0}=1$ , and $S_{t}=S_{t-1}+e_{t},\ t\geq 1,$ where $e_{t}$ takes values $\pm 1$ , and the distribution of $S_{t}$ is defined by the following conditions:

${\mathsf {P}}\{S_{t+1}=S_{t}+1|S_{t}>0\}={\frac {1}{2}}+{\frac {\alpha _{S_{t}}}{S_{t}}},\quad {\mathsf {P}}\{S_{t+1}=S_{t}-1|S_{t}>0\}={\frac {1}{2}}-{\frac {\alpha _{S_{t}}}{S_{t}}},\quad {\mathsf {P}}\{S_{t+1}=1|S_{t}=0\}=1,$

where $\alpha _{n}$ satisfy the condition $0<\alpha _{n}<\min\{C,n/2\},C>0$ .

The random walk described here is a discrete time analogue of the birth-and-death process (see Markov chain) with the birth rates

$\lambda _{n}={\frac {1}{2}}+{\frac {\alpha _{n}}{n}},$

and the death rates

$\mu _{n}={\frac {1}{2}}-{\frac {\alpha _{n}}{n}}$

.

So, recurrence or transience of the random walk is associated with recurrence or transience of the birth-and-death process.

The random walk is transient if there exist

$c>1$

,

$K\geq 1$

and

$n_{0}$

such that for all

$n>n_{0}$

$\alpha _{n}\geq {\frac {1}{4}}\left(1+\sum _{k=1}^{K-1}\prod _{j=1}^{k}{\frac {1}{\ln _{(j)}(n)}}+c\prod _{j=1}^{K}{\frac {1}{\ln _{(j)}(n)}}\right),$

where the empty sum for $K=1$ is assumed to be zero.

The random walk is recurrent if there exist

$K\geq 1$

and

$n_{0}$

such that for all

$n>n_{0}$

$\alpha _{n}\leq {\frac {1}{4}}\left(1+\sum _{k=1}^{K}\prod _{j=1}^{k}{\frac {1}{\ln _{(j)}(n)}}\right).$

## Stationary solution

If a birth-and-death process is ergodic, then there exists steady-state probabilities $\pi _{k}=\lim _{t\to \infty }p_{k}(t),$ where $p_{k}(t)$ is the probability that the birth-and-death process is in state k at time $t.$ The limit exists, independent of the initial values $p_{k}(0),$ and is calculated by the relations:

$\pi _{k}=\pi _{0}\prod _{i=1}^{k}{\frac {\lambda _{i-1}}{\mu _{i}}},\quad k=1,2,\ldots ,$

$\pi _{0}={\frac {1}{1+\sum _{k=1}^{\infty }\prod _{i=1}^{k}{\frac {\lambda _{i-1}}{\mu _{i}}}}}.$

These limiting probabilities are obtained from the infinite system of differential equations for $p_{k}(t):$

$p_{0}^{\prime }(t)=\mu _{1}p_{1}(t)-\lambda _{0}p_{0}(t)\,$

$p_{k}^{\prime }(t)=\lambda _{k-1}p_{k-1}(t)+\mu _{k+1}p_{k+1}(t)-(\lambda _{k}+\mu _{k})p_{k}(t),k=1,2,\ldots ,\,$

and the initial condition $\sum _{k=0}^{\infty }p_{k}(t)=1.$

In turn, the last system of differential equations is derived from the system of difference equations that describes the dynamic of the system in a small time $\Delta t$ . During this small time $\Delta t$ only three types of transitions are considered as one death, or one birth, or no birth nor death. The probability of the first two of these transitions has the order of $\Delta t$ . Other transitions during this small interval $\Delta t$ such as *more than one birth*, or *more than one death*, or *at least one birth and at least one death* have the probabilities that are of smaller order than $\Delta t$ , and hence are negligible in derivations. If the system is in state *k*, then the probability of birth during an interval $\Delta t$ is $\lambda _{k}\Delta t+o(\Delta t)$ , the probability of death is $\mu _{k}\Delta t+o(\Delta t)$ , and the probability of no birth and no death is $1-\lambda _{k}\Delta t-\mu _{k}\Delta t+o(\Delta t)$ . For a population process, "birth" is the transition towards increasing the population size by 1 while "death" is the transition towards decreasing the population size by 1.

## Examples of birth-death processes

A pure birth process is a birth–death process where $\mu _{i}=0$ for all $i\geq 0$ .

A **pure death process** is a birth–death process where $\lambda _{i}=0$ for all $i\geq 0$ .

*M/M/1 model* and *M/M/c model*, both used in queueing theory, are birth–death processes used to describe customers in an infinite queue.

## Use in phylodynamics

Birth–death processes are used in phylodynamics as a prior distribution for phylogenies, i.e. a binary tree in which birth events correspond to branches of the tree and death events correspond to leaf nodes. Notably, they are used in viral phylodynamics to understand the transmission process and how the number of people infected changes through time.

The use of generalized birth-death processes in phylodynamics has stimulated investigations into the degree to which the rates of birth and death can be identified from data. While the model is unidentifiable in general, the subset of models that are typically used are identifiable.

## Use in queueing theory

In queueing theory the birth–death process is the most fundamental example of a queueing model, the *M/M/C/K/ $\infty$ /FIFO* (in complete Kendall's notation) queue. This is a queue with Poisson arrivals, drawn from an infinite population, and *C* servers with exponentially distributed service times with *K* places in the queue. Despite the assumption of an infinite population this model is a good model for various telecommunication systems.

### M/M/1 queue

The **M/M/1** is a single server queue with an infinite buffer size. In a non-random environment the birth–death process in queueing models tend to be long-term averages, so the average rate of arrival is given as $\lambda$ and the average service time as $1/\mu$ . The birth and death process is an M/M/1 queue when,

$\lambda _{i}=\lambda {\text{ and }}\mu _{i}=\mu {\text{ for all }}i.\,$

The differential equations for the probability that the system is in state *k* at time *t* are

$p_{0}^{\prime }(t)=\mu p_{1}(t)-\lambda p_{0}(t),\,$

$p_{k}^{\prime }(t)=\lambda p_{k-1}(t)+\mu p_{k+1}(t)-(\lambda +\mu )p_{k}(t)\quad {\text{for }}k=1,2,\ldots \,$

### Pure birth process associated with an M/M/1 queue

Pure birth process with $\lambda _{k}\equiv \lambda$ is a particular case of the M/M/1 queueing process. We have the following system of differential equations:

$p_{0}^{\prime }(t)=-\lambda p_{0}(t),\,$

$p_{k}^{\prime }(t)=\lambda p_{k-1}(t)-\lambda p_{k}(t)\quad {\text{for }}k=1,2,\ldots \,$

Under the initial condition $p_{0}(0)=1$ and $p_{k}(0)=0,\ k=1,2,\ldots$ , the solution of the system is

$p_{k}(t)={\frac {(\lambda t)^{k}}{k!}}\mathrm {e} ^{-\lambda t}.$

That is, a (homogeneous) Poisson process is a pure birth process.

### M/M/c queue

The M/M/C is a multi-server queue with *C* servers and an infinite buffer. It characterizes by the following birth and death parameters:

$\mu _{i}=i\mu \quad {\text{ for }}i\leq C-1,\,$

and

$\mu _{i}=C\mu \quad {\text{ for }}i\geq C,\,$

with

$\lambda _{i}=\lambda \quad {\text{ for all }}i.\,$

The system of differential equations in this case has the form:

$p_{0}^{\prime }(t)=\mu p_{1}(t)-\lambda p_{0}(t),\,$

$p_{k}^{\prime }(t)=\lambda p_{k-1}(t)+(k+1)\mu p_{k+1}(t)-(\lambda +k\mu )p_{k}(t)\quad {\text{for }}k=1,2,\ldots ,C-1,\,$

$p_{k}^{\prime }(t)=\lambda p_{k-1}(t)+C\mu p_{k+1}(t)-(\lambda +C\mu )p_{k}(t)\quad {\text{for }}k\geq C.\,$

### Pure death process associated with an M/M/C queue

Pure death process with $\mu _{k}=k\mu$ is a particular case of the M/M/C queueing process. We have the following system of differential equations:

$p_{C}^{\prime }(t)=-C\mu p_{C}(t),\,$

$p_{k}^{\prime }(t)=(k+1)\mu p_{k+1}(t)-k\mu p_{k}(t)\quad {\text{for }}k=0,1,\ldots ,C-1.\,$

Under the initial condition $p_{C}(0)=1$ and $p_{k}(0)=0,\ k=0,1,\ldots ,C-1,$ we obtain the solution

$p_{k}(t)={\binom {C}{k}}\mathrm {e} ^{-k\mu t}\left(1-\mathrm {e} ^{-\mu t}\right)^{C-k},$

that presents the version of binomial distribution depending on time parameter t (see Binomial process).

### M/M/1/K queue

The M/M/1/K queue is a single server queue with a buffer of size *K*. This queue has applications in telecommunications, as well as in biology when a population has a capacity limit. In telecommunication we again use the parameters from the M/M/1 queue with,

$\lambda _{i}=\lambda \quad {\text{ for }}0\leq i<K,\,$

$\lambda _{i}=0\quad {\text{ for }}i\geq K,\,$

$\mu _{i}=\mu \quad {\text{ for }}1\leq i\leq K.\,$

In biology, particularly the growth of bacteria, when the population is zero there is no ability to grow so,

$\lambda _{0}=0.\,$

Additionally if the capacity represents a limit where the individual dies from over population,

$\mu _{K}=0.\,$

The differential equations for the probability that the system is in state *k* at time *t* are

$p_{0}^{\prime }(t)=\mu p_{1}(t)-\lambda p_{0}(t),$

$p_{k}^{\prime }(t)=\lambda p_{k-1}(t)+\mu p_{k+1}(t)-(\lambda +\mu )p_{k}(t)\quad {\text{ for }}k\leq K-1,\,$

$p_{K}^{\prime }(t)=\lambda p_{K-1}(t)-(\lambda +\mu )p_{K}(t),\,$

$p_{k}(t)=0\quad {\text{ for }}k>K.\,$

## Equilibrium

A queue is said to be in equilibrium if the steady state probabilities $\pi _{k}=\lim _{t\to \infty }p_{k}(t),\ k=0,1,\ldots ,$ exist. The condition for the existence of these steady-state probabilities in the case of M/M/1 queue is $\rho =\lambda /\mu <1$ and in the case of M/M/C queue is $\rho =\lambda /(C\mu )<1$ . The parameter $\rho$ is usually called load parameter or utilization parameter. Sometimes it is also called traffic intensity.

Using the M/M/1 queue as an example, the steady state equations are

$\lambda \pi _{0}=\mu \pi _{1},\,$

$(\lambda +\mu )\pi _{k}=\lambda \pi _{k-1}+\mu \pi _{k+1}.\,$

This can be reduced to

$\lambda \pi _{k}=\mu \pi _{k+1}{\text{ for }}k\geq 0.\,$

So, taking into account that $\pi _{0}+\pi _{1}+\ldots =1$ , we obtain

$\pi _{k}=(1-\rho )\rho ^{k}.$

## Bilateral birth-and-death process

Bilateral birth-and-death process is defined similarly to that standard one with the only difference that the birth and death rates $\lambda _{i}$ and $\mu _{i}$ are defined for the values of index parameter $i=0,\pm 1,\pm 2,\ldots$ . Following this, a bilateral birth-and-death process is recurrent if and only if

$\sum _{i=1}^{\infty }\prod _{n=1}^{i}{\frac {\mu _{n}}{\lambda _{n}}}=\infty \quad {\text{and}}\quad \sum _{i=1}^{\infty }\prod _{n=1}^{i}{\frac {\lambda _{-n}}{\mu _{-n}}}=\infty .$

The notions of ergodicity and null-recurrence are defined similarly by extending the corresponding notions of the standard birth-and-death process.
