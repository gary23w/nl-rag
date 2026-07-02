---
title: "Particle filter (part 1/2)"
source: https://en.wikipedia.org/wiki/Particle_filter
domain: signal-estimation
license: CC-BY-SA-4.0
tags: estimation theory, kalman filter, maximum likelihood estimation, particle filter
fetched: 2026-07-02
part: 1/2
---

# Particle filter

**Particle filters**, also known as **sequential Monte Carlo** methods, are a set of Monte Carlo algorithms used to find approximate solutions for filtering problems for nonlinear state-space systems, such as signal processing and Bayesian statistical inference. The filtering problem consists of estimating the internal states in dynamical systems when partial observations are made and random perturbations are present in the sensors as well as in the dynamical system. The objective is to compute the posterior distributions of the states of a Markov process, given the noisy and partial observations. The term "particle filters" was first coined in 1996 by Pierre Del Moral about mean-field interacting particle methods used in fluid mechanics since the beginning of the 1960s. The term "Sequential Monte Carlo" was coined by Jun S. Liu and Rong Chen in 1998.

Particle filtering uses a set of particles (also called samples) to represent the posterior distribution of a stochastic process given the noisy and/or partial observations. The state-space model can be nonlinear and the initial state and noise distributions can take any form required. Particle filter techniques provide a well-established methodology for generating samples from the required distribution without requiring assumptions about the state-space model or the state distributions. However, these methods do not perform well when applied to very high-dimensional systems.

Particle filters update their prediction in an approximate (statistical) manner. The samples from the distribution are represented by a set of particles; each particle has a likelihood weight assigned to it that represents the probability of that particle being sampled from the probability density function. Weight disparity leading to weight collapse is a common issue encountered in these filtering algorithms. However, it can be mitigated by including a resampling step before the weights become uneven. Several adaptive resampling criteria can be used including the variance of the weights and the relative entropy concerning the uniform distribution. In the resampling step, the particles with negligible weights are replaced by new particles in the proximity of the particles with higher weights.

From the statistical and probabilistic point of view, particle filters may be interpreted as mean-field particle interpretations of Feynman-Kac probability measures. These particle integration techniques were developed in molecular chemistry and computational physics by Theodore E. Harris and Herman Kahn in 1951, Marshall N. Rosenbluth and Arianna W. Rosenbluth in 1955, and more recently by Jack H. Hetherington in 1984. In computational physics, these Feynman-Kac type path particle integration methods are also used in Quantum Monte Carlo, and more specifically Diffusion Monte Carlo methods. Feynman-Kac interacting particle methods are also strongly related to mutation-selection genetic algorithms currently used in evolutionary computation to solve complex optimization problems.

The particle filter methodology is used to solve Hidden Markov Model (HMM) and nonlinear filtering problems. With the notable exception of linear-Gaussian signal-observation models (Kalman filter) or wider classes of models (Benes filter), Mireille Chaleyat-Maurel and Dominique Michel proved in 1984 that the sequence of posterior distributions of the random states of a signal, given the observations (a.k.a. optimal filter), has no finite recursion. Various other numerical methods based on fixed grid approximations, Markov Chain Monte Carlo techniques, conventional linearization, extended Kalman filters, or determining the best linear system (in the expected cost-error sense) are unable to cope with large-scale systems, unstable processes, or insufficiently smooth nonlinearities.

Particle filters and Feynman-Kac particle methodologies find application in signal and image processing, Bayesian inference, machine learning, risk analysis and rare event sampling, engineering and robotics, artificial intelligence, bioinformatics, phylogenetics, computational science, economics and mathematical finance, molecular chemistry, computational physics, pharmacokinetics, quantitative risk and insurance and other fields.


## History

### Heuristic-like algorithms

From a statistical and probabilistic viewpoint, particle filters belong to the class of branching/genetic type algorithms, and mean-field type interacting particle methodologies. The interpretation of these particle methods depends on the scientific discipline. In Evolutionary Computing, mean-field genetic type particle methodologies are often used as heuristic and natural search algorithms (a.k.a. Metaheuristic). In computational physics and molecular chemistry, they are used to solve Feynman-Kac path integration problems or to compute Boltzmann-Gibbs measures, top eigenvalues, and ground states of Schrödinger operators. In Biology and Genetics, they represent the evolution of a population of individuals or genes in some environment.

The origins of mean-field type evolutionary computational techniques can be traced back to 1950 and 1954 with Alan Turing's work on genetic type mutation-selection learning machines and the articles by Nils Aall Barricelli at the Institute for Advanced Study in Princeton, New Jersey. The first trace of particle filters in statistical methodology dates back to the mid-1950s; the 'Poor Man's Monte Carlo', that was proposed by John Hammersley et al., in 1954, contained hints of the genetic type particle filtering methods used today. In 1963, Nils Aall Barricelli simulated a genetic type algorithm to mimic the ability of individuals to play a simple game. In evolutionary computing literature, genetic-type mutation-selection algorithms became popular through the seminal work of John Holland in the early 1970s, particularly his book published in 1975.

In Biology and Genetics, the Australian geneticist Alex Fraser also published in 1957 a series of papers on the genetic type simulation of artificial selection of organisms. The computer simulation of the evolution by biologists became more common in the early 1960s, and the methods were described in books by Fraser and Burnell (1970) and Crosby (1973). Fraser's simulations included all of the essential elements of modern mutation-selection genetic particle algorithms.

From the mathematical viewpoint, the conditional distribution of the random states of a signal given some partial and noisy observations is described by a Feynman-Kac probability on the random trajectories of the signal weighted by a sequence of likelihood potential functions. Quantum Monte Carlo, and more specifically Diffusion Monte Carlo methods can also be interpreted as a mean-field genetic type particle approximation of Feynman-Kac path integrals. The origins of Quantum Monte Carlo methods are often attributed to Enrico Fermi and Robert Richtmyer who developed in 1948 a mean-field particle interpretation of neutron chain reactions, but the first heuristic-like and genetic type particle algorithm (a.k.a. Resampled or Reconfiguration Monte Carlo methods) for estimating ground state energies of quantum systems (in reduced matrix models) is due to Jack H. Hetherington in 1984. One can also quote the earlier seminal works of Theodore E. Harris and Herman Kahn in particle physics, published in 1951, using mean-field but heuristic-like genetic methods for estimating particle transmission energies. In molecular chemistry, the use of genetic heuristic-like particle methodologies (a.k.a. pruning and enrichment strategies) can be traced back to 1955 with the seminal work of Marshall N. Rosenbluth and Arianna W. Rosenbluth.

The use of genetic particle algorithms in advanced signal processing and Bayesian inference is more recent. In January 1993, Genshiro Kitagawa developed a "Monte Carlo filter", a slightly modified version of this article appeared in 1996. In April 1993, Neil J. Gordon et al., published in their seminal work an application of genetic type algorithm in Bayesian statistical inference. The authors named their algorithm 'the bootstrap filter', and demonstrated that compared to other filtering methods, their bootstrap algorithm does not require any assumption about that state space or the noise of the system. Independently, the ones by Pierre Del Moral and Himilcon Carvalho, Pierre Del Moral, André Monin, and Gérard Salut on particle filters published in the mid-1990s. Particle filters were also developed in signal processing in early 1989–1992 by P. Del Moral, J.C. Noyer, G. Rigal, and G. Salut in the LAAS-CNRS in a series of restricted and classified research reports with STCAN (Service Technique des Constructions et Armes Navales), the IT company DIGILOG, and the LAAS-CNRS (the Laboratory for Analysis and Architecture of Systems) on RADAR/SONAR and GPS signal processing problems.

### Mathematical foundations

From 1950 to 1996, all the publications on particle filters, and genetic algorithms, including the pruning and resample Monte Carlo methods introduced in computational physics and molecular chemistry, present natural and heuristic-like algorithms applied to different situations without a single proof of their consistency, nor a discussion on the bias of the estimates and genealogical and ancestral tree-based algorithms.

The mathematical foundations and the first rigorous analysis of these particle algorithms are due to Pierre Del Moral in 1996. The article also contains proof of the unbiased properties of a particle approximation of likelihood functions and unnormalized conditional probability measures. The unbiased particle estimator of the likelihood functions presented in this article is used today in Bayesian statistical inference.

Dan Crisan, Jessica Gaines, and Terry Lyons, as well as Pierre Del Moral, and Terry Lyons, created branching-type particle techniques with various population sizes around the end of the 1990s. P. Del Moral, A. Guionnet, and L. Miclo made more advances in this subject in 2000. Pierre Del Moral and Alice Guionnet proved the first central limit theorems in 1999, and Pierre Del Moral and Laurent Miclo proved them in 2000. The first uniform convergence results concerning the time parameter for particle filters were developed at the end of the 1990s by Pierre Del Moral and Alice Guionnet. The first rigorous analysis of genealogical tree-based particle filter smoothers is due to P. Del Moral and L. Miclo in 2001

The theory on Feynman-Kac particle methodologies and related particle filter algorithms was developed in 2000 and 2004 in the books. These abstract probabilistic models encapsulate genetic type algorithms, particle, and bootstrap filters, interacting Kalman filters (a.k.a. Rao–Blackwellized particle filter), importance sampling and resampling style particle filter techniques, including genealogical tree-based and particle backward methodologies for solving filtering and smoothing problems. Other classes of particle filtering methodologies include genealogical tree-based models, backward Markov particle models, adaptive mean-field particle models, island-type particle models, particle Markov chain Monte Carlo methodologies, Sequential Monte Carlo samplers and Sequential Monte Carlo Approximate Bayesian Computation methods and Sequential Monte Carlo ABC based Bayesian Bootstrap.


## The filtering problem

### Objective

A particle filter's goal is to estimate the posterior density of state variables given observation variables. The particle filter is intended for use with a hidden Markov Model, in which the system includes both hidden and observable variables. The observable variables (observation process) are linked to the hidden variables (state-process) via a known functional form. Similarly, the probabilistic description of the dynamical system defining the evolution of the state variables is known.

A generic particle filter estimates the posterior distribution of the hidden states using the observation measurement process. With respect to a state-space such as the one below:

${\begin{array}{cccccccccc}X_{0}&\to &X_{1}&\to &X_{2}&\to &X_{3}&\to &\cdots &{\text{signal}}\\\downarrow &&\downarrow &&\downarrow &&\downarrow &&\cdots &\\Y_{0}&&Y_{1}&&Y_{2}&&Y_{3}&&\cdots &{\text{observation}}\end{array}}$

the filtering problem is to estimate **sequentially** the values of the hidden states $X_{k}$ , given the values of the observation process $Y_{0},\cdots ,Y_{k},$ at any time step *k*.

All Bayesian estimates of $X_{k}$ follow from the posterior density $p(x_{k}|y_{0},y_{1},...,y_{k})$ . The particle filter methodology provides an approximation of these conditional probabilities using the empirical measure associated with a genetic type particle algorithm. In contrast, the Markov Chain Monte Carlo or importance sampling approach would model the full posterior $p(x_{0},x_{1},...,x_{k}|y_{0},y_{1},...,y_{k})$ .

### The Signal-Observation model

Particle methods often assume $X_{k}$ and the observations $Y_{k}$ can be modeled in this form:

- $X_{0},X_{1},\cdots$ is a Markov process on $\mathbb {R} ^{d_{x}}$ (for some $d_{x}\geqslant 1$ ) that evolves according to the transition probability density $p(x_{k}|x_{k-1})$ . This model is also often written in a synthetic way as $X_{k}|X_{k-1}=x_{k}\sim p(x_{k}|x_{k-1})$

with an initial probability density

$p(x_{0})$

.

- The observations $Y_{0},Y_{1},\cdots$ take values in some state space on $\mathbb {R} ^{d_{y}}$ (for some $d_{y}\geqslant 1$ ) and are conditionally independent provided that $X_{0},X_{1},\cdots$ are known. In other words, each $Y_{k}$ only depends on $X_{k}$ . In addition, we assume conditional distribution for $Y_{k}$ given $X_{k}=x_{k}$ are absolutely continuous, and in a synthetic way we have $Y_{k}|X_{k}=y_{k}\sim p(y_{k}|x_{k})$

An example of system with these properties is:

$X_{k}=g(X_{k-1})+W_{k-1}$

$Y_{k}=h(X_{k})+V_{k}$

where both $W_{k}$ and $V_{k}$ are mutually independent sequences with known probability density functions and *g* and *h* are known functions. These two equations can be viewed as state space equations and look similar to the state space equations for the Kalman filter. If the functions *g* and *h* in the above example are linear, and if both $W_{k}$ and $V_{k}$ are Gaussian, the Kalman filter finds the exact Bayesian filtering distribution. If not, Kalman filter-based methods are a first-order approximation (EKF) or a second-order approximation (UKF in general, but if the probability distribution is Gaussian a third-order approximation is possible).

The assumption that the initial distribution and the transitions of the Markov chain are continuous for the Lebesgue measure can be relaxed. To design a particle filter we simply need to assume that we can sample the transitions $X_{k-1}\to X_{k}$ of the Markov chain $X_{k},$ and to compute the likelihood function $x_{k}\mapsto p(y_{k}|x_{k})$ (see for instance the genetic selection mutation description of the particle filter given below). The continuous assumption on the Markov transitions of $X_{k}$ is only used to derive in an informal (and rather abusive) way different formulae between posterior distributions using the Bayes' rule for conditional densities.

### Approximate Bayesian computation models

In certain problems, the conditional distribution of observations, given the random states of the signal, may fail to have a density; the latter may be impossible or too complex to compute. In this situation, an additional level of approximation is necessitated. One strategy is to replace the signal $X_{k}$ by the Markov chain ${\mathcal {X}}_{k}=\left(X_{k},Y_{k}\right)$ and to introduce a virtual observation of the form

${\mathcal {Y}}_{k}=Y_{k}+\epsilon {\mathcal {V}}_{k}\quad {\mbox{for some parameter}}\quad \epsilon \in [0,1]$

for some sequence of independent random variables ${\mathcal {V}}_{k}$ with known probability density functions. The central idea is to observe that

${\text{Law}}\left(X_{k}|{\mathcal {Y}}_{0}=y_{0},\cdots ,{\mathcal {Y}}_{k}=y_{k}\right)\approx _{\epsilon \downarrow 0}{\text{Law}}\left(X_{k}|Y_{0}=y_{0},\cdots ,Y_{k}=y_{k}\right)$

The particle filter associated with the Markov process ${\mathcal {X}}_{k}=\left(X_{k},Y_{k}\right)$ given the partial observations ${\mathcal {Y}}_{0}=y_{0},\cdots ,{\mathcal {Y}}_{k}=y_{k},$ is defined in terms of particles evolving in $\mathbb {R} ^{d_{x}+d_{y}}$ with a likelihood function given with some obvious abusive notation by $p({\mathcal {Y}}_{k}|{\mathcal {X}}_{k})$ . These probabilistic techniques are closely related to Approximate Bayesian Computation (ABC). In the context of particle filters, these ABC particle filtering techniques were introduced in 1998 by P. Del Moral, J. Jacod and P. Protter. They were further developed by P. Del Moral, A. Doucet and A. Jasra.

### The nonlinear filtering equation

Bayes' rule for conditional probability gives:

$p(x_{0},\cdots ,x_{k}|y_{0},\cdots ,y_{k})={\frac {p(y_{0},\cdots ,y_{k}|x_{0},\cdots ,x_{k})p(x_{0},\cdots ,x_{k})}{p(y_{0},\cdots ,y_{k})}}$

where

${\begin{aligned}p(y_{0},\cdots ,y_{k})&=\int p(y_{0},\cdots ,y_{k}|x_{0},\cdots ,x_{k})p(x_{0},\cdots ,x_{k})dx_{0}\cdots dx_{k}\\p(y_{0},\cdots ,y_{k}|x_{0},\cdots ,x_{k})&=\prod _{l=0}^{k}p(y_{l}|x_{l})\\p(x_{0},\cdots ,x_{k})&=p_{0}(x_{0})\prod _{l=1}^{k}p(x_{l}|x_{l-1})\end{aligned}}$

Particle filters are also an approximation, but with enough particles they can be much more accurate. The nonlinear filtering equation is given by the recursion

| ${\begin{aligned}p(x_{k}\|y_{0},\cdots ,y_{k-1})&{\stackrel {\text{updating}}{\longrightarrow }}p(x_{k}\|y_{0},\cdots ,y_{k})={\frac {p(y_{k}\|x_{k})p(x_{k}\|y_{0},\cdots ,y_{k-1})}{\int p(y_{k}\|x'_{k})p(x'_{k}\|y_{0},\cdots ,y_{k-1})dx'_{k}}}\\&{\stackrel {\text{prediction}}{\longrightarrow }}p(x_{k+1}\|y_{0},\cdots ,y_{k})=\int p(x_{k+1}\|x_{k})p(x_{k}\|y_{0},\cdots ,y_{k})dx_{k}\end{aligned}}$ |   | Eq. 1 |
|---|---|---|

with the convention $p(x_{0}|y_{0},\cdots ,y_{k-1})=p(x_{0})$ for *k* = 0. The nonlinear filtering problem consists in computing these conditional distributions sequentially.

### Feynman-Kac formulation

We fix a time horizon n and a sequence of observations $Y_{0}=y_{0},\cdots ,Y_{n}=y_{n}$ , and for each *k* = 0, ..., *n* we set:

$G_{k}(x_{k})=p(y_{k}|x_{k}).$

In this notation, for any bounded function *F* on the set of trajectories of $X_{k}$ from the origin *k* = 0 up to time *k* = *n*, we have the Feynman-Kac formula

${\begin{aligned}\int F(x_{0},\cdots ,x_{n})p(x_{0},\cdots ,x_{n}|y_{0},\cdots ,y_{n})dx_{0}\cdots dx_{n}&={\frac {\int F(x_{0},\cdots ,x_{n})\left\{\prod \limits _{k=0}^{n}p(y_{k}|x_{k})\right\}p(x_{0},\cdots ,x_{n})dx_{0}\cdots dx_{n}}{\int \left\{\prod \limits _{k=0}^{n}p(y_{k}|x_{k})\right\}p(x_{0},\cdots ,x_{n})dx_{0}\cdots dx_{n}}}\\&={\frac {E\left(F(X_{0},\cdots ,X_{n})\prod \limits _{k=0}^{n}G_{k}(X_{k})\right)}{E\left(\prod \limits _{k=0}^{n}G_{k}(X_{k})\right)}}\end{aligned}}$

Feynman-Kac path integration models arise in a variety of scientific disciplines, including in computational physics, biology, information theory and computer sciences. Their interpretations are dependent on the application domain. For instance, if we choose the indicator function $G_{n}(x_{n})=1_{A}(x_{n})$ of some subset of the state space, they represent the conditional distribution of a Markov chain given it stays in a given tube; that is, we have:

$E\left(F(X_{0},\cdots ,X_{n})|X_{0}\in A,\cdots ,X_{n}\in A\right)={\frac {E\left(F(X_{0},\cdots ,X_{n})\prod \limits _{k=0}^{n}G_{k}(X_{k})\right)}{E\left(\prod \limits _{k=0}^{n}G_{k}(X_{k})\right)}}$

and

$P\left(X_{0}\in A,\cdots ,X_{n}\in A\right)=E\left(\prod \limits _{k=0}^{n}G_{k}(X_{k})\right)$

as soon as the normalizing constant is strictly positive.


## Particle filters

### A Genetic type particle algorithm

Initially, such an algorithm starts with *N* independent random variables $\left(\xi _{0}^{i}\right)_{1\leqslant i\leqslant N}$ with common probability density $p(x_{0})$ . The genetic algorithm selection-mutation transitions

$\xi _{k}:=\left(\xi _{k}^{i}\right)_{1\leqslant i\leqslant N}{\stackrel {\text{selection}}{\longrightarrow }}{\widehat {\xi }}_{k}:=\left({\widehat {\xi }}_{k}^{i}\right)_{1\leqslant i\leqslant N}{\stackrel {\text{mutation}}{\longrightarrow }}\xi _{k+1}:=\left(\xi _{k+1}^{i}\right)_{1\leqslant i\leqslant N}$

mimic/approximate the updating-prediction transitions of the optimal filter evolution (**Eq. 1**):

- **During the selection-updating transition** we sample *N* (conditionally) independent random variables ${\widehat {\xi }}_{k}:=\left({\widehat {\xi }}_{k}^{i}\right)_{1\leqslant i\leqslant N}$ with common (conditional) distribution

$\sum _{i=1}^{N}{\frac {p(y_{k}|\xi _{k}^{i})}{\sum _{j=1}^{N}p(y_{k}|\xi _{k}^{j})}}\delta _{\xi _{k}^{i}}(dx_{k})$

where $\delta _{a}$ stands for the **Dirac measure** at a given state a.

- **During the mutation-prediction transition,** from each selected particle ${\widehat {\xi }}_{k}^{i}$ we sample independently a transition

${\widehat {\xi }}_{k}^{i}\longrightarrow \xi _{k+1}^{i}\sim p(x_{k+1}|{\widehat {\xi }}_{k}^{i}),\qquad i=1,\cdots ,N.$

In the above displayed formulae $p(y_{k}|\xi _{k}^{i})$ stands for the likelihood function $x_{k}\mapsto p(y_{k}|x_{k})$ evaluated at $x_{k}=\xi _{k}^{i}$ , and $p(x_{k+1}|{\widehat {\xi }}_{k}^{i})$ stands for the conditional density $p(x_{k+1}|x_{k})$ evaluated at $x_{k}={\widehat {\xi }}_{k}^{i}$ .

At each time *k*, we have the particle approximations

${\widehat {p}}(dx_{k}|y_{0},\cdots ,y_{k}):={\frac {1}{N}}\sum _{i=1}^{N}\delta _{{\widehat {\xi }}_{k}^{i}}(dx_{k})\approx _{N\uparrow \infty }p(dx_{k}|y_{0},\cdots ,y_{k})\approx _{N\uparrow \infty }\sum _{i=1}^{N}{\frac {p(y_{k}|\xi _{k}^{i})}{\sum _{i=1}^{N}p(y_{k}|\xi _{k}^{j})}}\delta _{\xi _{k}^{i}}(dx_{k})$

and

${\widehat {p}}(dx_{k}|y_{0},\cdots ,y_{k-1}):={\frac {1}{N}}\sum _{i=1}^{N}\delta _{\xi _{k}^{i}}(dx_{k})\approx _{N\uparrow \infty }p(dx_{k}|y_{0},\cdots ,y_{k-1})$

In Genetic algorithms and Evolutionary computing community, the mutation-selection Markov chain described above is often called the genetic algorithm with proportional selection. Several branching variants, including with random population sizes have also been proposed in the articles.

### Monte Carlo principles

Particle methods, like all sampling-based approaches (e.g., Markov Chain Monte Carlo), generate a set of samples that approximate the filtering density

$p(x_{k}|y_{0},\cdots ,y_{k}).$

For example, we may have *N* samples from the approximate posterior distribution of $X_{k}$ , where the samples are labeled with superscripts as:

${\widehat {\xi }}_{k}^{1},\cdots ,{\widehat {\xi }}_{k}^{N}.$

Then, expectations with respect to the filtering distribution are approximated by

| $\int f(x_{k})p(x_{k}\|y_{0},\cdots ,y_{k})\,dx_{k}\approx _{N\uparrow \infty }{\frac {1}{N}}\sum _{i=1}^{N}f\left({\widehat {\xi }}_{k}^{i}\right)=\int f(x_{k}){\widehat {p}}(dx_{k}\|y_{0},\cdots ,y_{k})$ |   | Eq. 2 |
|---|---|---|

with

${\widehat {p}}(dx_{k}|y_{0},\cdots ,y_{k})={\frac {1}{N}}\sum _{i=1}^{N}\delta _{{\widehat {\xi }}_{k}^{i}}(dx_{k})$

where $\delta _{a}$ stands for the **Dirac measure** at a given state a. The function *f*, in the usual way for Monte Carlo, can give all the moments etc. of the distribution up to some approximation error. When the approximation equation (**Eq. 2**) is satisfied for any bounded function *f* we write

$p(dx_{k}|y_{0},\cdots ,y_{k}):=p(x_{k}|y_{0},\cdots ,y_{k})dx_{k}\approx _{N\uparrow \infty }{\widehat {p}}(dx_{k}|y_{0},\cdots ,y_{k})={\frac {1}{N}}\sum _{i=1}^{N}\delta _{{\widehat {\xi }}_{k}^{i}}(dx_{k})$

Particle filters can be interpreted as a genetic type particle algorithm evolving with mutation and selection transitions. We can keep track of the ancestral lines

$\left({\widehat {\xi }}_{0,k}^{i},{\widehat {\xi }}_{1,k}^{i},\cdots ,{\widehat {\xi }}_{k-1,k}^{i},{\widehat {\xi }}_{k,k}^{i}\right)$

of the particles $i=1,\cdots ,N$ . The random states ${\widehat {\xi }}_{l,k}^{i}$ , with the lower indices l=0,...,k, stands for the ancestor of the individual ${\widehat {\xi }}_{k,k}^{i}={\widehat {\xi }}_{k}^{i}$ at level l=0,...,k. In this situation, we have the approximation formula

| ${\begin{aligned}\int F(x_{0},\cdots ,x_{k})p(x_{0},\cdots ,x_{k}\|y_{0},\cdots ,y_{k})\,dx_{0}\cdots dx_{k}&\approx _{N\uparrow \infty }{\frac {1}{N}}\sum _{i=1}^{N}F\left({\widehat {\xi }}_{0,k}^{i},{\widehat {\xi }}_{1,k}^{i},\cdots ,{\widehat {\xi }}_{k,k}^{i}\right)\\&=\int F(x_{0},\cdots ,x_{k}){\widehat {p}}(d(x_{0},\cdots ,x_{k})\|y_{0},\cdots ,y_{k})\end{aligned}}$ |   | Eq. 3 |
|---|---|---|

with the empirical measure

${\widehat {p}}(d(x_{0},\cdots ,x_{k})|y_{0},\cdots ,y_{k}):={\frac {1}{N}}\sum _{i=1}^{N}\delta _{\left({\widehat {\xi }}_{0,k}^{i},{\widehat {\xi }}_{1,k}^{i},\cdots ,{\widehat {\xi }}_{k,k}^{i}\right)}(d(x_{0},\cdots ,x_{k}))$

Here *F* stands for any founded function on the path space of the signal. In a more synthetic form (**Eq. 3**) is equivalent to

${\begin{aligned}p(d(x_{0},\cdots ,x_{k})|y_{0},\cdots ,y_{k})&:=p(x_{0},\cdots ,x_{k}|y_{0},\cdots ,y_{k})\,dx_{0}\cdots dx_{k}\\&\approx _{N\uparrow \infty }{\widehat {p}}(d(x_{0},\cdots ,x_{k})|y_{0},\cdots ,y_{k})\\&:={\frac {1}{N}}\sum _{i=1}^{N}\delta _{\left({\widehat {\xi }}_{0,k}^{i},\cdots ,{\widehat {\xi }}_{k,k}^{i}\right)}(d(x_{0},\cdots ,x_{k}))\end{aligned}}$

Particle filters can be interpreted in many different ways. From the probabilistic point of view they coincide with a mean-field particle interpretation of the nonlinear filtering equation. The updating-prediction transitions of the optimal filter evolution can also be interpreted as the classical genetic type selection-mutation transitions of individuals. The sequential importance resampling technique provides another interpretation of the filtering transitions coupling importance sampling with the bootstrap resampling step. Last, but not least, particle filters can be seen as an acceptance-rejection methodology equipped with a recycling mechanism.

### Mean-field particle simulation

#### The general probabilistic principle

The nonlinear filtering evolution can be interpreted as a dynamical system in the set of probability measures of the form $\eta _{n+1}=\Phi _{n+1}\left(\eta _{n}\right)$ where $\Phi _{n+1}$ stands for some mapping from the set of probability distribution into itself. For instance, the evolution of the one-step optimal predictor $\eta _{n}(dx_{n})=p(x_{n}|y_{0},\cdots ,y_{n-1})dx_{n}$

satisfies a nonlinear evolution starting with the probability distribution $\eta _{0}(dx_{0})=p(x_{0})dx_{0}$ . One of the simplest ways to approximate these probability measures is to start with *N* independent random variables $\left(\xi _{0}^{i}\right)_{1\leqslant i\leqslant N}$ with common probability distribution $\eta _{0}(dx_{0})=p(x_{0})dx_{0}$ . Suppose we have defined a sequence of *N* random variables $\left(\xi _{n}^{i}\right)_{1\leqslant i\leqslant N}$ such that

${\frac {1}{N}}\sum _{i=1}^{N}\delta _{\xi _{n}^{i}}(dx_{n})\approx _{N\uparrow \infty }\eta _{n}(dx_{n})$

At the next step we sample *N* (conditionally) independent random variables $\xi _{n+1}:=\left(\xi _{n+1}^{i}\right)_{1\leqslant i\leqslant N}$ with common law .

$\Phi _{n+1}\left({\frac {1}{N}}\sum _{i=1}^{N}\delta _{\xi _{n}^{i}}\right)\approx _{N\uparrow \infty }\Phi _{n+1}\left(\eta _{n}\right)=\eta _{n+1}$

#### A particle interpretation of the filtering equation

We illustrate this mean-field particle principle in the context of the evolution of the one step optimal predictors

| $p(x_{k}\|y_{0},\cdots ,y_{k-1})dx_{k}\to p(x_{k+1}\|y_{0},\cdots ,y_{k})=\int p(x_{k+1}\|x'_{k}){\frac {p(y_{k}\|x_{k}')p(x'_{k}\|y_{0},\cdots ,y_{k-1})dx'_{k}}{\int p(y_{k}\|x''_{k})p(x''_{k}\|y_{0},\cdots ,y_{k-1})dx''_{k}}}$ |   | Eq. 4 |
|---|---|---|

For *k* = 0 we use the convention $p(x_{0}|y_{0},\cdots ,y_{-1}):=p(x_{0})$ .

By the law of large numbers, we have

${\widehat {p}}(dx_{0})={\frac {1}{N}}\sum _{i=1}^{N}\delta _{\xi _{0}^{i}}(dx_{0})\approx _{N\uparrow \infty }p(x_{0})dx_{0}$

in the sense that

$\int f(x_{0}){\widehat {p}}(dx_{0})={\frac {1}{N}}\sum _{i=1}^{N}f(\xi _{0}^{i})\approx _{N\uparrow \infty }\int f(x_{0})p(dx_{0})dx_{0}$

for any bounded function f . We further assume that we have constructed a sequence of particles $\left(\xi _{k}^{i}\right)_{1\leqslant i\leqslant N}$ at some rank *k* such that

${\widehat {p}}(dx_{k}|y_{0},\cdots ,y_{k-1}):={\frac {1}{N}}\sum _{i=1}^{N}\delta _{\xi _{k}^{i}}(dx_{k})\approx _{N\uparrow \infty }~p(x_{k}~|~y_{0},\cdots ,y_{k-1})dx_{k}$

in the sense that for any bounded function f we have

$\int f(x_{k}){\widehat {p}}(dx_{k}|y_{0},\cdots ,y_{k-1})={\frac {1}{N}}\sum _{i=1}^{N}f(\xi _{k}^{i})\approx _{N\uparrow \infty }\int f(x_{k})p(dx_{k}|y_{0},\cdots ,y_{k-1})dx_{k}$

In this situation, replacing $p(x_{k}|y_{0},\cdots ,y_{k-1})dx_{k}$ by the empirical measure ${\widehat {p}}(dx_{k}|y_{0},\cdots ,y_{k-1})$ in the evolution equation of the one-step optimal filter stated in (**Eq. 4**) we find that

$p(x_{k+1}|y_{0},\cdots ,y_{k})\approx _{N\uparrow \infty }\int p(x_{k+1}|x'_{k}){\frac {p(y_{k}|x_{k}'){\widehat {p}}(dx'_{k}|y_{0},\cdots ,y_{k-1})}{\int p(y_{k}|x''_{k}){\widehat {p}}(dx''_{k}|y_{0},\cdots ,y_{k-1})}}$

Notice that the right hand side in the above formula is a weighted probability mixture

$\int p(x_{k+1}|x'_{k}){\frac {p(y_{k}|x_{k}'){\widehat {p}}(dx'_{k}|y_{0},\cdots ,y_{k-1})}{\int p(y_{k}|x''_{k}){\widehat {p}}(dx''_{k}|y_{0},\cdots ,y_{k-1})}}=\sum _{i=1}^{N}{\frac {p(y_{k}|\xi _{k}^{i})}{\sum _{i=1}^{N}p(y_{k}|\xi _{k}^{j})}}p(x_{k+1}|\xi _{k}^{i})=:{\widehat {q}}(x_{k+1}|y_{0},\cdots ,y_{k})$

where $p(y_{k}|\xi _{k}^{i})$ stands for the density $p(y_{k}|x_{k})$ evaluated at $x_{k}=\xi _{k}^{i}$ , and $p(x_{k+1}|\xi _{k}^{i})$ stands for the density $p(x_{k+1}|x_{k})$ evaluated at $x_{k}=\xi _{k}^{i}$ for $i=1,\cdots ,N.$

Then, we sample *N* independent random variable $\left(\xi _{k+1}^{i}\right)_{1\leqslant i\leqslant N}$ with common probability density ${\widehat {q}}(x_{k+1}|y_{0},\cdots ,y_{k})$ so that

${\widehat {p}}(dx_{k+1}|y_{0},\cdots ,y_{k}):={\frac {1}{N}}\sum _{i=1}^{N}\delta _{\xi _{k+1}^{i}}(dx_{k+1})\approx _{N\uparrow \infty }{\widehat {q}}(x_{k+1}|y_{0},\cdots ,y_{k})dx_{k+1}\approx _{N\uparrow \infty }p(x_{k+1}|y_{0},\cdots ,y_{k})dx_{k+1}$

Iterating this procedure, we design a Markov chain such that

${\widehat {p}}(dx_{k}|y_{0},\cdots ,y_{k-1}):={\frac {1}{N}}\sum _{i=1}^{N}\delta _{\xi _{k}^{i}}(dx_{k})\approx _{N\uparrow \infty }p(dx_{k}|y_{0},\cdots ,y_{k-1}):=p(x_{k}|y_{0},\cdots ,y_{k-1})dx_{k}$

Notice that the optimal filter is approximated at each time step k using the Bayes' formulae

$p(dx_{k}|y_{0},\cdots ,y_{k})\approx _{N\uparrow \infty }{\frac {p(y_{k}|x_{k}){\widehat {p}}(dx_{k}|y_{0},\cdots ,y_{k-1})}{\int p(y_{k}|x'_{k}){\widehat {p}}(dx'_{k}|y_{0},\cdots ,y_{k-1})}}=\sum _{i=1}^{N}{\frac {p(y_{k}|\xi _{k}^{i})}{\sum _{j=1}^{N}p(y_{k}|\xi _{k}^{j})}}~\delta _{\xi _{k}^{i}}(dx_{k})$

The terminology "mean-field approximation" comes from the fact that we replace at each time step the probability measure $p(dx_{k}|y_{0},\cdots ,y_{k-1})$ by the empirical approximation ${\widehat {p}}(dx_{k}|y_{0},\cdots ,y_{k-1})$ . The mean-field particle approximation of the filtering problem is far from being unique. Several strategies are developed in the books.

### Some convergence results

The analysis of the convergence of particle filters was started in 1996 and in 2000 in the book and the series of articles. More recent developments can be found in the books, When the filtering equation is stable (in the sense that it corrects any erroneous initial condition), the bias and the variance of the particle particle estimates

$I_{k}(f):=\int f(x_{k})p(dx_{k}|y_{0},\cdots ,y_{k-1})\approx _{N\uparrow \infty }{\widehat {I}}_{k}(f):=\int f(x_{k}){\widehat {p}}(dx_{k}|y_{0},\cdots ,y_{k-1})$

are controlled by the non asymptotic uniform estimates

$\sup _{k\geqslant 0}\left\vert E\left({\widehat {I}}_{k}(f)\right)-I_{k}(f)\right\vert \leqslant {\frac {c_{1}}{N}}$

$\sup _{k\geqslant 0}E\left(\left[{\widehat {I}}_{k}(f)-I_{k}(f)\right]^{2}\right)\leqslant {\frac {c_{2}}{N}}$

for any function *f* bounded by 1, and for some finite constants $c_{1},c_{2}.$ In addition, for any $x\geqslant 0$ :

$\mathbf {P} \left(\left|{\widehat {I}}_{k}(f)-I_{k}(f)\right|\leqslant c_{1}{\frac {x}{N}}+c_{2}{\sqrt {\frac {x}{N}}}\land \sup _{0\leqslant k\leqslant n}\left|{\widehat {I}}_{k}(f)-I_{k}(f)\right|\leqslant c{\sqrt {\frac {x\log(n)}{N}}}\right)>1-e^{-x}$

for some finite constants $c_{1},c_{2}$ related to the asymptotic bias and variance of the particle estimate, and some finite constant *c*. The same results are satisfied if we replace the one step optimal predictor by the optimal filter approximation.


## Genealogical trees and Unbiasedness properties

### Genealogical tree based particle smoothing

Tracing back in time the ancestral lines

$\left({\widehat {\xi }}_{0,k}^{i},{\widehat {\xi }}_{1,k}^{i},\cdots ,{\widehat {\xi }}_{k-1,k}^{i},{\widehat {\xi }}_{k,k}^{i}\right),\quad \left(\xi _{0,k}^{i},\xi _{1,k}^{i},\cdots ,\xi _{k-1,k}^{i},\xi _{k,k}^{i}\right)$

of the individuals ${\widehat {\xi }}_{k}^{i}\left(={\widehat {\xi }}_{k,k}^{i}\right)$ and $\xi _{k}^{i}\left(={\xi }_{k,k}^{i}\right)$ at every time step *k*, we also have the particle approximations

${\begin{aligned}{\widehat {p}}(d(x_{0},\cdots ,x_{k})|y_{0},\cdots ,y_{k})&:={\frac {1}{N}}\sum _{i=1}^{N}\delta _{\left({\widehat {\xi }}_{0,k}^{i},\cdots ,{\widehat {\xi }}_{0,k}^{i}\right)}(d(x_{0},\cdots ,x_{k}))\\&\approx _{N\uparrow \infty }p(d(x_{0},\cdots ,x_{k})|y_{0},\cdots ,y_{k})\\&\approx _{N\uparrow \infty }\sum _{i=1}^{N}{\frac {p(y_{k}|\xi _{k,k}^{i})}{\sum _{j=1}^{N}p(y_{k}|\xi _{k,k}^{j})}}\delta _{\left(\xi _{0,k}^{i},\cdots ,\xi _{0,k}^{i}\right)}(d(x_{0},\cdots ,x_{k}))\\&\ \\{\widehat {p}}(d(x_{0},\cdots ,x_{k})|y_{0},\cdots ,y_{k-1})&:={\frac {1}{N}}\sum _{i=1}^{N}\delta _{\left(\xi _{0,k}^{i},\cdots ,\xi _{k,k}^{i}\right)}(d(x_{0},\cdots ,x_{k}))\\&\approx _{N\uparrow \infty }p(d(x_{0},\cdots ,x_{k})|y_{0},\cdots ,y_{k-1})\\&:=p(x_{0},\cdots ,x_{k}|y_{0},\cdots ,y_{k-1})dx_{0},\cdots ,dx_{k}\end{aligned}}$

These empirical approximations are equivalent to the particle integral approximations

${\begin{aligned}\int F(x_{0},\cdots ,x_{n}){\widehat {p}}(d(x_{0},\cdots ,x_{k})|y_{0},\cdots ,y_{k})&:={\frac {1}{N}}\sum _{i=1}^{N}F\left({\widehat {\xi }}_{0,k}^{i},\cdots ,{\widehat {\xi }}_{0,k}^{i}\right)\\&\approx _{N\uparrow \infty }\int F(x_{0},\cdots ,x_{n})p(d(x_{0},\cdots ,x_{k})|y_{0},\cdots ,y_{k})\\&\approx _{N\uparrow \infty }\sum _{i=1}^{N}{\frac {p(y_{k}|\xi _{k,k}^{i})}{\sum _{j=1}^{N}p(y_{k}|\xi _{k,k}^{j})}}F\left(\xi _{0,k}^{i},\cdots ,\xi _{k,k}^{i}\right)\\&\ \\\int F(x_{0},\cdots ,x_{n}){\widehat {p}}(d(x_{0},\cdots ,x_{k})|y_{0},\cdots ,y_{k-1})&:={\frac {1}{N}}\sum _{i=1}^{N}F\left(\xi _{0,k}^{i},\cdots ,\xi _{k,k}^{i}\right)\\&\approx _{N\uparrow \infty }\int F(x_{0},\cdots ,x_{n})p(d(x_{0},\cdots ,x_{k})|y_{0},\cdots ,y_{k-1})\end{aligned}}$

for any bounded function *F* on the random trajectories of the signal. As shown in the evolution of the genealogical tree coincides with a mean-field particle interpretation of the evolution equations associated with the posterior densities of the signal trajectories. For more details on these path space models, we refer to the books.

### Unbiased particle estimates of likelihood functions

We use the product formula

$p(y_{0},\cdots ,y_{n})=\prod _{k=0}^{n}p(y_{k}|y_{0},\cdots ,y_{k-1})$

with

$p(y_{k}|y_{0},\cdots ,y_{k-1})=\int p(y_{k}|x_{k})p(dx_{k}|y_{0},\cdots ,y_{k-1})$

and the conventions $p(y_{0}|y_{0},\cdots ,y_{-1})=p(y_{0})$ and $p(x_{0}|y_{0},\cdots ,y_{-1})=p(x_{0}),$ for *k* = 0. Replacing $p(x_{k}|y_{0},\cdots ,y_{k-1})dx_{k}$ by the empirical approximation

${\widehat {p}}(dx_{k}|y_{0},\cdots ,y_{k-1}):={\frac {1}{N}}\sum _{i=1}^{N}\delta _{\xi _{k}^{i}}(dx_{k})\approx _{N\uparrow \infty }p(dx_{k}|y_{0},\cdots ,y_{k-1})$

in the above displayed formula, we design the following unbiased particle approximation of the likelihood function

$p(y_{0},\cdots ,y_{n})\approx _{N\uparrow \infty }{\widehat {p}}(y_{0},\cdots ,y_{n})=\prod _{k=0}^{n}{\widehat {p}}(y_{k}|y_{0},\cdots ,y_{k-1})$

with

${\widehat {p}}(y_{k}|y_{0},\cdots ,y_{k-1})=\int p(y_{k}|x_{k}){\widehat {p}}(dx_{k}|y_{0},\cdots ,y_{k-1})={\frac {1}{N}}\sum _{i=1}^{N}p(y_{k}|\xi _{k}^{i})$

where $p(y_{k}|\xi _{k}^{i})$ stands for the density $p(y_{k}|x_{k})$ evaluated at $x_{k}=\xi _{k}^{i}$ . The design of this particle estimate and the unbiasedness property has been proved in 1996 in the article. Refined variance estimates can be found in and.

### Backward particle smoothers

Using Bayes' rule, we have the formula

$p(x_{0},\cdots ,x_{n}|y_{0},\cdots ,y_{n-1})=p(x_{n}|y_{0},\cdots ,y_{n-1})p(x_{n-1}|x_{n},y_{0},\cdots ,y_{n-1})\cdots p(x_{1}|x_{2},y_{0},y_{1})p(x_{0}|x_{1},y_{0})$

Notice that

${\begin{aligned}p(x_{k-1}|x_{k},(y_{0},\cdots ,y_{k-1}))&\propto p(x_{k}|x_{k-1})p(x_{k-1}|(y_{0},\cdots ,y_{k-1}))\\p(x_{k-1}|(y_{0},\cdots ,y_{k-1})&\propto p(y_{k-1}|x_{k-1})p(x_{k-1}|(y_{0},\cdots ,y_{k-2})\end{aligned}}$

This implies that

$p(x_{k-1}|x_{k},(y_{0},\cdots ,y_{k-1}))={\frac {p(y_{k-1}|x_{k-1})p(x_{k}|x_{k-1})p(x_{k-1}|y_{0},\cdots ,y_{k-2})}{\int p(y_{k-1}|x'_{k-1})p(x_{k}|x'_{k-1})p(x'_{k-1}|y_{0},\cdots ,y_{k-2})dx'_{k-1}}}$

Replacing the one-step optimal predictors $p(x_{k-1}|(y_{0},\cdots ,y_{k-2}))dx_{k-1}$ by the particle empirical measures

${\widehat {p}}(dx_{k-1}|(y_{0},\cdots ,y_{k-2}))={\frac {1}{N}}\sum _{i=1}^{N}\delta _{\xi _{k-1}^{i}}(dx_{k-1})\left(\approx _{N\uparrow \infty }p(dx_{k-1}|(y_{0},\cdots ,y_{k-2})):={p}(x_{k-1}|(y_{0},\cdots ,y_{k-2}))dx_{k-1}\right)$

we find that

${\begin{aligned}p(dx_{k-1}|x_{k},(y_{0},\cdots ,y_{k-1}))&\approx _{N\uparrow \infty }{\widehat {p}}(dx_{k-1}|x_{k},(y_{0},\cdots ,y_{k-1}))\\&:={\frac {p(y_{k-1}|x_{k-1})p(x_{k}|x_{k-1}){\widehat {p}}(dx_{k-1}|y_{0},\cdots ,y_{k-2})}{\int p(y_{k-1}|x'_{k-1})~p(x_{k}|x'_{k-1}){\widehat {p}}(dx'_{k-1}|y_{0},\cdots ,y_{k-2})}}\\&=\sum _{i=1}^{N}{\frac {p(y_{k-1}|\xi _{k-1}^{i})p(x_{k}|\xi _{k-1}^{i})}{\sum _{j=1}^{N}p(y_{k-1}|\xi _{k-1}^{j})p(x_{k}|\xi _{k-1}^{j})}}\delta _{\xi _{k-1}^{i}}(dx_{k-1})\end{aligned}}$

We conclude that

$p(d(x_{0},\cdots ,x_{n})|(y_{0},\cdots ,y_{n-1}))\approx _{N\uparrow \infty }{\widehat {p}}_{backward}(d(x_{0},\cdots ,x_{n})|(y_{0},\cdots ,y_{n-1}))$

with the backward particle approximation

${\begin{aligned}{\widehat {p}}_{backward}(d(x_{0},\cdots ,x_{n})|(y_{0},\cdots ,y_{n-1}))={\widehat {p}}(dx_{n}|(y_{0},\cdots ,y_{n-1})){\widehat {p}}(dx_{n-1}|x_{n},(y_{0},\cdots ,y_{n-1}))\cdots {\widehat {p}}(dx_{1}|x_{2},(y_{0},y_{1})){\widehat {p}}(dx_{0}|x_{1},y_{0})\end{aligned}}$

The probability measure

${\widehat {p}}_{backward}(d(x_{0},\cdots ,x_{n})|(y_{0},\cdots ,y_{n-1}))$

is the probability of the random paths of a Markov chain $\left(\mathbb {X} _{k,n}^{\flat }\right)_{0\leqslant k\leqslant n}$ running backward in time from time k=n to time k=0, and evolving at each time step k in the state space associated with the population of particles $\xi _{k}^{i},i=1,\cdots ,N.$

- Initially (at time k=n) the chain $\mathbb {X} _{n,n}^{\flat }$ chooses randomly a state with the distribution

${\widehat {p}}(dx_{n}|(y_{0},\cdots ,y_{n-1}))={\frac {1}{N}}\sum _{i=1}^{N}\delta _{\xi _{n}^{i}}(dx_{n})$

- From time k to the time (k-1), the chain starting at some state $\mathbb {X} _{k,n}^{\flat }=\xi _{k}^{i}$ for some $i=1,\cdots ,N$ at time k moves at time (k-1) to a random state $\mathbb {X} _{k-1,n}^{\flat }$ chosen with the discrete weighted probability

${\widehat {p}}(dx_{k-1}|\xi _{k}^{i},(y_{0},\cdots ,y_{k-1}))=\sum _{j=1}^{N}{\frac {p(y_{k-1}|\xi _{k-1}^{j})p(\xi _{k}^{i}|\xi _{k-1}^{j})}{\sum _{l=1}^{N}p(y_{k-1}|\xi _{k-1}^{l})p(\xi _{k}^{i}|\xi _{k-1}^{l})}}~\delta _{\xi _{k-1}^{j}}(dx_{k-1})$

In the above displayed formula, ${\widehat {p}}(dx_{k-1}|\xi _{k}^{i},(y_{0},\cdots ,y_{k-1}))$ stands for the conditional distribution ${\widehat {p}}(dx_{k-1}|x_{k},(y_{0},\cdots ,y_{k-1}))$ evaluated at $x_{k}=\xi _{k}^{i}$ . In the same vein, $p(y_{k-1}|\xi _{k-1}^{j})$ and $p(\xi _{k}^{i}|\xi _{k-1}^{j})$ stand for the conditional densities $p(y_{k-1}|x_{k-1})$ and $p(x_{k}|x_{k-1})$ evaluated at $x_{k}=\xi _{k}^{i}$ and $x_{k-1}=\xi _{k-1}^{j}.$ These models allows to reduce integration with respect to the densities $p((x_{0},\cdots ,x_{n})|(y_{0},\cdots ,y_{n-1}))$ in terms of matrix operations with respect to the Markov transitions of the chain described above. For instance, for any function $f_{k}$ we have the particle estimates

${\begin{aligned}\int p(d(x_{0},\cdots ,x_{n})&|(y_{0},\cdots ,y_{n-1}))f_{k}(x_{k})\\&\approx _{N\uparrow \infty }\int {\widehat {p}}_{backward}(d(x_{0},\cdots ,x_{n})|(y_{0},\cdots ,y_{n-1}))f_{k}(x_{k})\\&=\int {\widehat {p}}(dx_{n}|(y_{0},\cdots ,y_{n-1})){\widehat {p}}(dx_{n-1}|x_{n},(y_{0},\cdots ,y_{n-1}))\cdots {\widehat {p}}(dx_{k}|x_{k+1},(y_{0},\cdots ,y_{k}))f_{k}(x_{k})\\&=\underbrace {\left[{\tfrac {1}{N}},\cdots ,{\tfrac {1}{N}}\right]} _{N{\text{ times}}}\mathbb {M} _{n-1}\cdots \mathbb {M} _{k}{\begin{bmatrix}f_{k}(\xi _{k}^{1})\\\vdots \\f_{k}(\xi _{k}^{N})\end{bmatrix}}\end{aligned}}$

where

$\mathbb {M} _{k}=(\mathbb {M} _{k}(i,j))_{1\leqslant i,j\leqslant N}:\qquad \mathbb {M} _{k}(i,j)={\frac {p(\xi _{k}^{i}|\xi _{k-1}^{j})~p(y_{k-1}|\xi _{k-1}^{j})}{\sum \limits _{l=1}^{N}p(\xi _{k}^{i}|\xi _{k-1}^{l})p(y_{k-1}|\xi _{k-1}^{l})}}$

This also shows that if

${\overline {F}}(x_{0},\cdots ,x_{n}):={\frac {1}{n+1}}\sum _{k=0}^{n}f_{k}(x_{k})$

then

${\begin{aligned}\int {\overline {F}}(x_{0},\cdots ,x_{n})p(d(x_{0},\cdots ,x_{n})|(y_{0},\cdots ,y_{n-1}))&\approx _{N\uparrow \infty }\int {\overline {F}}(x_{0},\cdots ,x_{n}){\widehat {p}}_{backward}(d(x_{0},\cdots ,x_{n})|(y_{0},\cdots ,y_{n-1}))\\&={\frac {1}{n+1}}\sum _{k=0}^{n}\underbrace {\left[{\tfrac {1}{N}},\cdots ,{\tfrac {1}{N}}\right]} _{N{\text{ times}}}\mathbb {M} _{n-1}\mathbb {M} _{n-2}\cdots \mathbb {M} _{k}{\begin{bmatrix}f_{k}(\xi _{k}^{1})\\\vdots \\f_{k}(\xi _{k}^{N})\end{bmatrix}}\end{aligned}}$

Particle smoothing can also be achieved in a single online pass through a fixed-lag approximation.

### Some convergence results

We shall assume that filtering equation is stable, in the sense that it corrects any erroneous initial condition.

In this situation, the **particle approximations of the likelihood functions** are unbiased and the relative variance is controlled by

$E\left({\widehat {p}}(y_{0},\cdots ,y_{n})\right)=p(y_{0},\cdots ,y_{n}),\qquad E\left(\left[{\frac {{\widehat {p}}(y_{0},\cdots ,y_{n})}{p(y_{0},\cdots ,y_{n})}}-1\right]^{2}\right)\leqslant {\frac {cn}{N}},$

for some finite constant *c*. In addition, for any $x\geqslant 0$ :

$\mathbf {P} \left(\left\vert {\frac {1}{n}}\log {{\widehat {p}}(y_{0},\cdots ,y_{n})}-{\frac {1}{n}}\log {p(y_{0},\cdots ,y_{n})}\right\vert \leqslant c_{1}{\frac {x}{N}}+c_{2}{\sqrt {\frac {x}{N}}}\right)>1-e^{-x}$

for some finite constants $c_{1},c_{2}$ related to the asymptotic bias and variance of the particle estimate, and for some finite constant *c*.

The bias and the variance of **the particle particle estimates based on the ancestral lines of the genealogical trees**

${\begin{aligned}I_{k}^{path}(F)&:=\int F(x_{0},\cdots ,x_{k})p(d(x_{0},\cdots ,x_{k})|y_{0},\cdots ,y_{k-1})\\&\approx _{N\uparrow \infty }{\widehat {I}}_{k}^{path}(F)\\&:=\int F(x_{0},\cdots ,x_{k}){\widehat {p}}(d(x_{0},\cdots ,x_{k})|y_{0},\cdots ,y_{k-1})\\&={\frac {1}{N}}\sum _{i=1}^{N}F\left(\xi _{0,k}^{i},\cdots ,\xi _{k,k}^{i}\right)\end{aligned}}$

are controlled by the non asymptotic uniform estimates

$\left|E\left({\widehat {I}}_{k}^{path}(F)\right)-I_{k}^{path}(F)\right|\leqslant {\frac {c_{1}k}{N}},\qquad E\left(\left[{\widehat {I}}_{k}^{path}(F)-I_{k}^{path}(F)\right]^{2}\right)\leqslant {\frac {c_{2}k}{N}},$

for any function *F* bounded by 1, and for some finite constants $c_{1},c_{2}.$ In addition, for any $x\geqslant 0$ :

$\mathbf {P} \left(\left|{\widehat {I}}_{k}^{path}(F)-I_{k}^{path}(F)\right|\leqslant c_{1}{\frac {kx}{N}}+c_{2}{\sqrt {\frac {kx}{N}}}\land \sup _{0\leqslant k\leqslant n}\left|{\widehat {I}}_{k}^{path}(F)-I_{k}^{path}(F)\right|\leqslant c{\sqrt {\frac {xn\log(n)}{N}}}\right)>1-e^{-x}$

for some finite constants $c_{1},c_{2}$ related to the asymptotic bias and variance of the particle estimate, and for some finite constant *c*. The same type of bias and variance estimates hold for the backward particle smoothers. For additive functionals of the form

${\overline {F}}(x_{0},\cdots ,x_{n}):={\frac {1}{n+1}}\sum _{0\leqslant k\leqslant n}f_{k}(x_{k})$

with

$I_{n}^{path}({\overline {F}})\approx _{N\uparrow \infty }I_{n}^{\flat ,path}({\overline {F}}):=\int {\overline {F}}(x_{0},\cdots ,x_{n}){\widehat {p}}_{backward}(d(x_{0},\cdots ,x_{n})|(y_{0},\cdots ,y_{n-1}))$

with functions $f_{k}$ bounded by 1, we have

$\sup _{n\geqslant 0}{\left\vert E\left({\widehat {I}}_{n}^{\flat ,path}({\overline {F}})\right)-I_{n}^{path}({\overline {F}})\right\vert }\leqslant {\frac {c_{1}}{N}}$

and

$E\left(\left[{\widehat {I}}_{n}^{\flat ,path}(F)-I_{n}^{path}(F)\right]^{2}\right)\leqslant {\frac {c_{2}}{nN}}+{\frac {c_{3}}{N^{2}}}$

for some finite constants $c_{1},c_{2},c_{3}.$ More refined estimates including exponentially small probability of errors are developed in.
