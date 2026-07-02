---
title: "M/M/1 queue"
source: https://en.wikipedia.org/wiki/M/M/1_queue
domain: queueing-theory
license: CC-BY-SA-4.0
tags: queueing theory, birth-death process, kendall notation, little's law
fetched: 2026-07-02
---

# M/M/1 queue

In queueing theory, a discipline within the mathematical theory of probability, an **M/M/1 queue** represents the queue length in a system having a single server, where arrivals are determined by a Poisson process and job service times have an exponential distribution. The model name is written in Kendall's notation. The model is the most elementary of queueing models and an attractive object of study as closed-form expressions can be obtained for many metrics of interest in this model. An extension of this model with more than one server is the M/M/c queue.

## Model definition

An M/M/1 queue is a stochastic process whose state space is the set {0,1,2,3,...} where the value corresponds to the number of customers in the system, including any currently in service.

- Arrivals occur at rate λ according to a Poisson process and move the process from state *i* to *i* + 1.
- Service times have an exponential distribution with rate parameter μ in the M/M/1 queue, where 1/μ is the mean service time.
- All arrival times and services times are (usually) assumed to be independent of one another.
- A single server serves customers one at a time from the front of the queue, according to a first-come, first-served discipline. When the service is complete the customer leaves the queue and the number of customers in the system reduces by one.
- The buffer is of infinite size, so there is no limit on the number of customers it can contain.

The model can be described as a continuous time Markov chain with transition rate matrix

$Q={\begin{pmatrix}-\lambda &\lambda \\\mu &-(\mu +\lambda )&\lambda \\&\mu &-(\mu +\lambda )&\lambda \\&&\mu &-(\mu +\lambda )&\lambda &\\&&&&\ddots \end{pmatrix}}$

on the state space {0,1,2,3,...}. This is the same continuous time Markov chain as in a birth–death process. The state space diagram for this chain is as below.

## Stationary analysis

The model is considered stable only if λ < μ. If, on average, arrivals happen faster than service completions the queue will grow indefinitely long and the system will not have a stationary distribution. The stationary distribution is the limiting distribution for large values of *t*.

Various performance measures can be computed explicitly for the M/M/1 queue. We write ρ = λ/μ for the utilization of the buffer and require ρ < 1 for the queue to be stable. ρ represents the average proportion of time which the server is occupied.

The probability that the stationary process is in state *i* (contains *i* customers, including those in service) is

$\pi _{i}=(1-\rho )\rho ^{i}.\,$

### Average number of customers in the system

We see that the number of customers in the system is geometrically distributed with parameter 1 − *ρ*. Thus the average number of customers in the system is *ρ*/(1 − *ρ*) and the variance of number of customers in the system is *ρ*/(1 − *ρ*)2. This result holds for any work conserving service regime, such as processor sharing.

### Busy period of server

The busy period is the time period measured between the instant a customer arrives to an empty system until the instant a customer departs leaving behind an empty system. The busy period has probability density function

$f(t)={\begin{cases}{\frac {1}{t{\sqrt {\rho }}}}e^{-(\lambda +\mu )t}I_{1}(2t{\sqrt {\lambda \mu }})&t>0\\0&{\text{otherwise}}\end{cases}}$

where *I*1 is a modified Bessel function of the first kind, obtained by using Laplace transforms and inverting the solution.

The Laplace transform of the M/M/1 busy period is given by

$\mathbb {E} (e^{-sF})={\frac {1}{2\lambda }}(\lambda +\mu +s-{\sqrt {(\lambda +\mu +s)^{2}-4\lambda \mu }})$

which gives the moments of the busy period, in particular the mean is 1/(*μ* − *λ*) and variance is given by

${\frac {1}{\mu ^{2}(1-\rho )^{2}}}.$

### Response time

The average response time or sojourn time (total time a customer spends in the system) does not depend on scheduling discipline and can be computed using Little's law as 1/(*μ* − *λ*). The average time spent waiting is 1/(*μ* − *λ*) − 1/*μ* = *ρ*/(*μ* − *λ*). The distribution of response times experienced does depend on scheduling discipline.

#### First-come, first-served discipline

For customers who arrive and find the queue as a stationary process, the response time they experience (the sum of both waiting time and service time) has Laplace transform (*μ* − *λ*)/(*s* + *μ* − *λ*) and therefore probability density function

$f(t)={\begin{cases}(\mu -\lambda )e^{-(\mu -\lambda )t}&t>0\\0&{\text{otherwise.}}\end{cases}}$

#### Processor sharing discipline

In an M/M/1-PS queue there is no waiting line and all jobs receive an equal proportion of the service capacity. Suppose the single server serves at rate 16 and there are 4 jobs in the system, each job will experience service at rate 4. The rate at which jobs receive service changes each time a job arrives at or departs from the system.

For customers who arrive to find the queue as a stationary process, the Laplace transform of the distribution of response times experienced by customers was published in 1970, for which an integral representation is known. The waiting time distribution (response time less service time) for a customer requiring *x* amount of service has transform

$W^{\ast }(s|x)={\frac {(1-\rho )(1-\rho r^{2})e^{-[\lambda (1-r)+s]x}}{(1-\rho r^{2})-\rho (1-r)^{2}e^{-(\mu /r-\lambda r)x}}}$

where *r* is the smaller root of the equation

$\lambda r^{2}-(\lambda +\mu +s)r+\mu =0.$

The mean response time for a job arriving and requiring amount *x* of service can therefore be computed as *x μ*/(*μ* − *λ*). An alternative approach computes the same results using a spectral expansion method.

## Transient solution

We can write a probability mass function dependent on *t* to describe the probability that the M/M/1 queue is in a particular state at a given time. We assume that the queue is initially in state *i* and write *p**k*(*t*) for the probability of being in state *k* at time *t*. Then

$p_{k}(t)=e^{-(\lambda +\mu )t}\left[\rho ^{\frac {k-i}{2}}I_{k-i}(at)+\rho ^{\frac {k-i-1}{2}}I_{k+i+1}(at)+(1-\rho )\rho ^{k}\sum _{j=k+i+2}^{\infty }\rho ^{-j/2}I_{j}(at)\right]$

where i is the initial number of customers in the station at time $t=0$ , $\rho =\lambda /\mu$ , $a=2{\sqrt {\lambda \mu }}$ and $I_{k}$ is the modified Bessel function of the first kind. Moments for the transient solution can be expressed as the sum of two monotone functions.

## Diffusion approximation

When the utilization *ρ* is close to 1 the process can be approximated by a reflected Brownian motion with drift parameter *λ* – *μ* and variance parameter *λ* + *μ*. This heavy traffic limit was first introduced by John Kingman.
