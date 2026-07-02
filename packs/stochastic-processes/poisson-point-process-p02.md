---
title: "Poisson point process (part 2/2)"
source: https://en.wikipedia.org/wiki/Poisson_point_process
domain: stochastic-processes
license: CC-BY-SA-4.0
tags: stochastic process, wiener process, brownian motion, stochastic calculus
fetched: 2026-07-02
part: 2/2
---

## Point process operations

Mathematical operations can be performed on point processes to get new point processes and develop new mathematical models for the locations of certain objects. One example of an operation is known as thinning which entails deleting or removing the points of some point process according to a rule, creating a new process with the remaining points (the deleted points also form a point process).

### Thinning

For the Poisson process, the independent $\textstyle p(x)$ -thinning operations results in another Poisson point process. More specifically, a $\textstyle p(x)$ -thinning operation applied to a Poisson point process with intensity measure $\textstyle \Lambda$ gives a point process of removed points that is also Poisson point process $\textstyle {N}_{p}$ with intensity measure $\textstyle \Lambda _{p}$ , which for a bounded Borel set $\textstyle B$ is given by:

$\Lambda _{p}(B)=\int _{B}p(x)\,\Lambda (\mathrm {d} x)$

This thinning result of the Poisson point process is sometimes known as **Prekopa's theorem**. Furthermore, after randomly thinning a Poisson point process, the kept or remaining points also form a Poisson point process, which has the intensity measure

$\Lambda _{p}(B)=\int _{B}(1-p(x))\,\Lambda (\mathrm {d} x).$

The two separate Poisson point processes formed respectively from the removed and kept points are stochastically independent of each other. In other words, if a region is known to contain $\textstyle n$ kept points (from the original Poisson point process), then this will have no influence on the random number of removed points in the same region. This ability to randomly create two independent Poisson point processes from one is sometimes known as *splitting* the Poisson point process.

### Superposition

If there is a countable collection of point processes $\textstyle N_{1},N_{2},\dots$ , then their superposition, or, in set theory language, their union, which is

$N=\bigcup _{i=1}^{\infty }N_{i},$

also forms a point process. In other words, any points located in any of the point processes $\textstyle N_{1},N_{2}\dots$ will also be located in the superposition of these point processes $\textstyle {N}$ .

#### Superposition theorem

The **superposition theorem** of the Poisson point process says that the superposition of independent Poisson point processes $\textstyle N_{1},N_{2}\dots$ with mean measures $\textstyle \Lambda _{1},\Lambda _{2},\dots$ will also be a Poisson point process with mean measure

$\Lambda =\sum _{i=1}^{\infty }\Lambda _{i}.$

In other words, the union of two (or countably more) Poisson processes is another Poisson process. If a point ${\textstyle x}$ is sampled from a countable ${\textstyle n}$ union of Poisson processes, then the probability that the point $\textstyle x$ belongs to the ${\textstyle j}$ th Poisson process ${\textstyle N_{j}}$ is given by:

$\Pr\{x\in N_{j}\}={\frac {\Lambda _{j}}{\sum _{i=1}^{n}\Lambda _{i}}}.$

For two homogeneous Poisson processes with intensities ${\textstyle \lambda _{1},\lambda _{2}\dots }$ , the two previous expressions reduce to

$\lambda =\sum _{i=1}^{\infty }\lambda _{i},$

and

$\Pr\{x\in N_{j}\}={\frac {\lambda _{j}}{\sum _{i=1}^{n}\lambda _{i}}}.$

### Clustering

The operation clustering is performed when each point $\textstyle x$ of some point process $\textstyle {N}$ is replaced by another (possibly different) point process. If the original process $\textstyle {N}$ is a Poisson point process, then the resulting process $\textstyle {N}_{c}$ is called a Poisson cluster point process.

### Random displacement

A mathematical model may require randomly moving points of a point process to other locations on the underlying mathematical space, which gives rise to a point process operation known as displacement or translation. The Poisson point process has been used to model, for example, the movement of plants between generations, owing to the displacement theorem, which loosely says that the random independent displacement of points of a Poisson point process (on the same underlying space) forms another Poisson point process.

#### Displacement theorem

One version of the displacement theorem involves a Poisson point process $\textstyle {N}$ on $\textstyle \mathbb {R} ^{d}$ with intensity function $\textstyle \lambda (x)$ . It is then assumed the points of $\textstyle {N}$ are randomly displaced somewhere else in $\textstyle \mathbb {R} ^{d}$ so that each point's displacement is independent and that the displacement of a point formerly at $\textstyle x$ is a random vector with a probability density $\textstyle \rho (x,\cdot )$ . Then the new point process $\textstyle N_{D}$ is also a Poisson point process with intensity function

$\lambda _{D}(y)=\int _{\mathbb {R} ^{d}}\lambda (x)\rho (x,y)\,\mathrm {d} x.$

If the Poisson process is homogeneous with $\textstyle \lambda (x)=\lambda >0$ and if $\rho (x,y)$ is a function of $y-x$ , then

$\lambda _{D}(y)=\lambda .$

In other words, after each random and independent displacement of points, the original Poisson point process still exists.

The displacement theorem can be extended such that the Poisson points are randomly displaced from one Euclidean space $\textstyle \mathbb {R} ^{d}$ to another Euclidean space $\textstyle \mathbb {R} ^{d'}$ , where $\textstyle d'\geq 1$ is not necessarily equal to $\textstyle d$ .

### Mapping

Another property that is considered useful is the ability to map a Poisson point process from one underlying space to another space.

#### Mapping theorem

If the mapping (or transformation) adheres to some conditions, then the resulting mapped (or transformed) collection of points also form a Poisson point process, and this result is sometimes referred to as the **mapping theorem**. The theorem involves some Poisson point process with mean measure $\textstyle \Lambda$ on some underlying space. If the locations of the points are mapped (that is, the point process is transformed) according to some function to another underlying space, then the resulting point process is also a Poisson point process but with a different mean measure $\textstyle \Lambda '$ .

More specifically, one can consider a (Borel measurable) function $\textstyle f$ that maps a point process $\textstyle {N}$ with intensity measure $\textstyle \Lambda$ from one space $\textstyle S$ , to another space $\textstyle T$ in such a manner so that the new point process $\textstyle {N}'$ has the intensity measure:

$\Lambda (B)'=\Lambda (f^{-1}(B))$

with no atoms, where $\textstyle B$ is a Borel set and $\textstyle f^{-1}$ denotes the inverse of the function $\textstyle f$ . If $\textstyle {N}$ is a Poisson point process, then the new process $\textstyle {N}'$ is also a Poisson point process with the intensity measure $\textstyle \Lambda '$ .


## Approximations with Poisson point processes

The tractability of the Poisson process means that sometimes it is convenient to approximate a non-Poisson point process with a Poisson one. The overall aim is to approximate both the number of points of some point process and the location of each point by a Poisson point process. There a number of methods that can be used to justify, informally or rigorously, approximating the occurrence of random events or phenomena with suitable Poisson point processes. The more rigorous methods involve deriving upper bounds on the probability metrics between the Poisson and non-Poisson point processes, while other methods can be justified by less formal heuristics.

### Clumping heuristic

One method for approximating random events or phenomena with Poisson processes is called the **clumping heuristic**. The general heuristic or principle involves using the Poisson point process (or Poisson distribution) to approximate events, which are considered rare or unlikely, of some stochastic process. In some cases these rare events are close to being independent, hence a Poisson point process can be used. When the events are not independent, but tend to occur in clusters or *clumps*, then if these clumps are suitably defined such that they are approximately independent of each other, then the number of clumps occurring will be close to a Poisson random variable and the locations of the clumps will be close to a Poisson process.

### Stein's method

Stein's method is a mathematical technique originally developed for approximating random variables such as Gaussian and Poisson variables, which has also been applied to point processes. Stein's method can be used to derive upper bounds on probability metrics, which give way to quantify how different two random mathematical objects vary stochastically. Upperbounds on probability metrics such as total variation and Wasserstein distance have been derived.

Researchers have applied Stein's method to Poisson point processes in a number of ways, such as using Palm calculus. Techniques based on Stein's method have been developed to factor into the upper bounds the effects of certain point process operations such as thinning and superposition. Stein's method has also been used to derive upper bounds on metrics of Poisson and other processes such as the Cox point process, which is a Poisson process with a random intensity measure.


## Convergence to a Poisson point process

In general, when an operation is applied to a general point process the resulting process is usually not a Poisson point process. For example, if a point process, other than a Poisson, has its points randomly and independently displaced, then the process would not necessarily be a Poisson point process. However, under certain mathematical conditions for both the original point process and the random displacement, it has been shown via limit theorems that if the points of a point process are repeatedly displaced in a random and independent manner, then the finite-distribution of the point process will converge (weakly) to that of a Poisson point process.

Similar convergence results have been developed for thinning and superposition operations that show that such repeated operations on point processes can, under certain conditions, result in the process converging to a Poisson point processes, provided a suitable rescaling of the intensity measure (otherwise values of the intensity measure of the resulting point processes would approach zero or infinity). Such convergence work is directly related to the results known as the Palm–Khinchin equations, which has its origins in the work of Conny Palm and Aleksandr Khinchin, and help explains why the Poisson process can often be used as a mathematical model of various random phenomena.


## Generalizations of Poisson point processes

The Poisson point process can be generalized by, for example, changing its intensity measure or defining on more general mathematical spaces. These generalizations can be studied mathematically as well as used to mathematically model or represent physical phenomena.

### Poisson-type random measures

The Poisson-type random measures (PT) are a family of three random counting measures which are closed under restriction to a subspace, i.e. closed under Point process operation#Thinning. These random measures are examples of the mixed binomial process and share the distributional self-similarity property of the Poisson random measure. They are the only members of the canonical non-negative power series family of distributions to possess this property and include the Poisson distribution, negative binomial distribution, and binomial distribution. The Poisson random measure is independent on disjoint subspaces, whereas the other PT random measures (negative binomial and binomial) have positive and negative covariances. The PT random measures are discussed and include the Poisson random measure, negative binomial random measure, and binomial random measure.

### Poisson point processes on more general spaces

For mathematical models the Poisson point process is often defined in Euclidean space, but has been generalized to more abstract spaces and plays a fundamental role in the study of random measures, which requires an understanding of mathematical fields such as probability theory, measure theory and topology.

In general, the concept of distance is of practical interest for applications, while topological structure is needed for Palm distributions, meaning that point processes are usually defined on mathematical spaces with metrics. Furthermore, a realization of a point process can be considered as a counting measure, so points processes are types of random measures known as random counting measures. In this context, the Poisson and other point processes have been studied on a locally compact second countable Hausdorff space.

### Cox point process

A **Cox point process**, **Cox process** or **doubly stochastic Poisson process** is a generalization of the Poisson point process by letting its intensity measure $\textstyle \Lambda$ to be also random and independent of the underlying Poisson process. The process is named after David Cox who introduced it in 1955, though other Poisson processes with random intensities had been independently introduced earlier by Lucien Le Cam and Maurice Quenouille. The intensity measure may be a realization of random variable or a random field. For example, if the logarithm of the intensity measure is a Gaussian random field, then the resulting process is known as a *log Gaussian Cox process*. More generally, the intensity measures is a realization of a non-negative locally finite random measure. Cox point processes exhibit a *clustering* of points, which can be shown mathematically to be larger than those of Poisson point processes. The generality and tractability of Cox processes has resulted in them being used as models in fields such as spatial statistics and wireless networks.

### Marked Poisson point process

For a given point process, each random point of a point process can have a random mathematical object, known as a **mark**, randomly assigned to it. These marks can be as diverse as integers, real numbers, lines, geometrical objects or other point processes. The pair consisting of a point of the point process and its corresponding mark is called a marked point, and all the marked points form a **marked point process**. It is often assumed that the random marks are independent of each other and identically distributed, yet the mark of a point can still depend on the location of its corresponding point in the underlying (state) space. If the underlying point process is a Poisson point process, then the resulting point process is a **marked Poisson point process**.

#### Marking theorem

If a general point process is defined on some mathematical space and the random marks are defined on another mathematical space, then the marked point process is defined on the Cartesian product of these two spaces. For a marked Poisson point process with independent and identically distributed marks, the **marking theorem** states that this marked point process is also a (non-marked) Poisson point process defined on the aforementioned Cartesian product of the two mathematical spaces, which is not true for general point processes.

### Compound Poisson point process

The **compound Poisson point process** or **compound Poisson process** is formed by adding random values or weights to each point of Poisson point process defined on some underlying space, so the process is constructed from a marked Poisson point process, where the marks form a collection of independent and identically distributed non-negative random variables. In other words, for each point of the original Poisson process, there is an independent and identically distributed non-negative random variable, and then the compound Poisson process is formed from the sum of all the random variables corresponding to points of the Poisson process located in some region of the underlying mathematical space.

If there is a marked Poisson point process formed from a Poisson point process $\textstyle N$ (defined on, for example, $\textstyle \mathbb {R} ^{d}$ ) and a collection of independent and identically distributed non-negative marks $\textstyle \{M_{i}\}$ such that for each point $\textstyle x_{i}$ of the Poisson process $\textstyle N$ there is a non-negative random variable $\textstyle M_{i}$ , the resulting compound Poisson process is then:

$C(B)=\sum _{i=1}^{N(B)}M_{i},$

where $\textstyle B\subset \mathbb {R} ^{d}$ is a Borel measurable set.

If general random variables $\textstyle \{M_{i}\}$ take values in, for example, $\textstyle d$ -dimensional Euclidean space $\textstyle \mathbb {R} ^{d}$ , the resulting compound Poisson process is an example of a Lévy process provided that it is formed from a homogeneous Point process $\textstyle N$ defined on the non-negative numbers $\textstyle [0,\infty )$ .

### Failure process with the exponential smoothing of intensity functions

The failure process with the exponential smoothing of intensity functions (FP-ESI) is an extension of the nonhomogeneous Poisson process. The intensity function of an FP-ESI is an exponential smoothing function of the intensity functions at the last time points of event occurrences and outperforms other nine stochastic processes on 8 real-world failure datasets when the models are used to fit the datasets, where the model performance is measured in terms of AIC (Akaike information criterion) and BIC (Bayesian information criterion).
