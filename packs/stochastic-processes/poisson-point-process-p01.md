---
title: "Poisson point process (part 1/2)"
source: https://en.wikipedia.org/wiki/Poisson_point_process
domain: stochastic-processes
license: CC-BY-SA-4.0
tags: stochastic process, wiener process, brownian motion, stochastic calculus
fetched: 2026-07-02
part: 1/2
---

# Poisson point process

In probability theory, statistics and related fields, a **Poisson point process** (also known as: **Poisson random measure**, **Poisson random point field** and **Poisson point field**) is a type of mathematical object that consists of points randomly located on a mathematical space with the essential feature that the points occur independently of one another. The process's name derives from the fact that the number of points in any given finite region follows a Poisson distribution. The process and the distribution are named after French mathematician Siméon Denis Poisson. The process itself was discovered independently and repeatedly in several settings, including experiments on radioactive decay, telephone call arrivals and actuarial science.

This point process is used as a mathematical model for seemingly random processes in numerous disciplines including astronomy, biology, ecology, geology, seismology, physics, economics, image processing, and telecommunications.

The Poisson point process is often defined on the real number line, where it can be viewed as a stochastic process. It is used, for example, in queueing theory to model random events distributed in time, such as the arrival of customers at a store, phone calls at an telephone exchange, or the occurrence of earthquakes. In the plane, the point process—also known as a **spatial Poisson process**—can represent the locations of scattered objects such as transmitters in a wireless network, particles colliding into a particle detector, or trees in a forest. The process is widely used in mathematical models and in related fields, including spatial point processes, stochastic geometry, spatial statistics and continuum percolation theory.

The point process depends on a single mathematical object, which, depending on the context, may be a constant, a locally integrable function or, in more general settings, a Radon measure. In the first case, the constant, known as the **rate** or **intensity**, is the average density of the points in the Poisson process located in some region of space. The resulting point process is called a **homogeneous** or **stationary Poisson point process**. In the second case, the point process is called an **inhomogeneous** or **nonhomogeneous** **Poisson point process**, and the average density of points depend on the location of the underlying space of the Poisson point process. The word *point* is often omitted, but there are other *Poisson processes* of objects, which, instead of points, consist of more complicated mathematical objects such as lines and polygons, and such processes can be based on the Poisson point process. Both the homogeneous and nonhomogeneous Poisson point processes are particular cases of the generalized renewal process.


## Overview of definitions

Depending on the setting, the process has several equivalent definitions as well as definitions of varying generality owing to its many applications and characterizations. The Poisson point process can be defined, studied and used in one dimension, for example, on the real line, where it can be interpreted as a counting process or part of a queueing model; in higher dimensions such as the plane where it plays a role in stochastic geometry and spatial statistics; or on more general mathematical spaces. Consequently, the notation, terminology and level of mathematical rigour used to define and study the Poisson point process and points processes in general vary according to the context.

Despite all this, the Poisson point process has two key properties—the Poisson property and the independence property— that play an essential role in all settings where the Poisson point process is used. The two properties are not logically independent; indeed, the Poisson distribution of point counts implies the independence property, while in the converse direction the assumptions that: (i) the point process is simple, (ii) has no fixed atoms, and (iii) is a.s. boundedly finite are required.

### Poisson distribution of point counts

A Poisson point process is characterized via the Poisson distribution. The Poisson distribution is the probability distribution of a random variable ${\textstyle N}$ (called a *Poisson random variable*) such that the probability that $\textstyle N$ equals $\textstyle n$ is given by:

$\Pr\{N=n\}={\frac {\Lambda ^{n}}{n!}}e^{-\Lambda }$

where ${\textstyle n!}$ denotes factorial and the parameter ${\textstyle \Lambda }$ determines the shape of the distribution. (In fact, ${\textstyle \Lambda }$ equals the expected value of ${\textstyle N}$ .)

By definition, a Poisson point process has the property that the number of points in a bounded region of the process's underlying space is a Poisson-distributed random variable.

### Complete independence

Consider a collection of disjoint and bounded subregions of the underlying space. By definition, the number of points of a Poisson point process in each bounded subregion will be completely independent of all the others.

This property is known under several names such as *complete randomness*, *complete independence*, or *independent scattering* and is common to all Poisson point processes. In other words, there is a lack of interaction between different regions and the points in general, which motivates the Poisson process being sometimes called a *purely* or *completely* random process.


## Homogeneous Poisson point process

If a Poisson point process has a parameter of the form ${\textstyle \Lambda =\nu \lambda }$ , where ${\textstyle \nu }$ is Lebesgue measure (that is, it assigns length, area, or volume to sets) and ${\textstyle \lambda }$ is a constant, then the point process is called a homogeneous or stationary Poisson point process. The parameter, called **rate** or **intensity**, is related to the expected (or average) number of Poisson points existing in some bounded region, where *rate* is usually used when the underlying space has one dimension. The parameter ${\textstyle \lambda }$ can be interpreted as the average number of points per some unit of extent such as length, area, volume, or time, depending on the underlying mathematical space, and it is also called the *mean density* or *mean rate*; see Terminology.

### Interpreted as a counting process

The homogeneous Poisson point process, when considered on the positive half-line, can be defined as a counting process, a type of stochastic process, which can be denoted as ${\textstyle \{N(t),t\geq 0\}}$ . A counting process represents the total number of occurrences or events that have happened up to and including time ${\textstyle t}$ . A counting process is a homogeneous Poisson counting process with rate ${\textstyle \lambda >0}$ if it has the following three properties:

- ${\textstyle N(0)=0;}$
- has independent increments; and
- the number of events (or points) in any interval of length ${\textstyle t}$ is a Poisson random variable with parameter (or mean) ${\textstyle \lambda t}$ .

The last property implies:

$\operatorname {E} [N(t)]=\lambda t.$

In other words, the probability of the random variable ${\textstyle N(t)}$ being equal to ${\textstyle n}$ is given by:

$\Pr\{N(t)=n\}={\frac {(\lambda t)^{n}}{n!}}e^{-\lambda t}.$

The Poisson counting process can also be defined by stating that the time differences between events of the counting process are exponential variables with mean ${\textstyle 1/\lambda }$ . The time differences between the events or arrivals are known as **interarrival** or **interoccurrence** times.

### Interpreted as a point process on the real line

Interpreted as a point process, a Poisson point process can be defined on the real line by considering the number of points of the process in the interval ${\textstyle (a,b]}$ . For the homogeneous Poisson point process on the real line with parameter ${\textstyle \lambda >0}$ , the probability of this random number of points, written here as ${\textstyle N(a,b]}$ , being equal to some counting number ${\textstyle n}$ is given by:

$\Pr\{N(a,b]=n\}={\frac {[\lambda (b-a)]^{n}}{n!}}e^{-\lambda (b-a)},$

For some positive integer ${\textstyle k}$ , the homogeneous Poisson point process has the finite-dimensional distribution given by:

$\Pr\{N(a_{i},b_{i}]=n_{i},i=1,\dots ,k\}=\prod _{i=1}^{k}{\frac {[\lambda (b_{i}-a_{i})]^{n_{i}}}{n_{i}!}}e^{-\lambda (b_{i}-a_{i})},$

where the real numbers ${\textstyle a_{i}<b_{i}\leq a_{i+1}}$ .

In other words, ${\textstyle N(a,b]}$ is a Poisson random variable with mean ${\textstyle \lambda (b-a)}$ , where ${\textstyle a\leq b}$ . Furthermore, the number of points in any two disjoint intervals, say, ${\textstyle (a_{1},b_{1}]}$ and ${\textstyle (a_{2},b_{2}]}$ are independent of each other, and this extends to any finite number of disjoint intervals. In the queueing theory context, one can consider a point existing (in an interval) as an *event*, but this is different to the word event in the probability theory sense. It follows that ${\textstyle \lambda }$ is the expected number of *arrivals* that occur per unit of time.

#### Key properties

The previous definition has two important features shared by Poisson point processes in general:

- the number of arrivals in each finite interval has a Poisson distribution;
- the number of arrivals in disjoint intervals are independent random variables.

Furthermore, it has a third feature related to just the homogeneous Poisson point process:

- the Poisson distribution of the number of arrivals in each interval ${\textstyle (a+t,b+t]}$ only depends on the interval's length ${\textstyle b-a}$ .

In other words, for any finite ${\textstyle t>0}$ , the random variable ${\textstyle N(a+t,b+t]}$ is independent of ${\textstyle t}$ , so it is also called a stationary Poisson process.

#### Law of large numbers

The quantity ${\textstyle \lambda (b_{i}-a_{i})}$ can be interpreted as the expected or average number of points occurring in the interval ${\textstyle (a_{i},b_{i}]}$ , namely:

$\operatorname {E} [N(a_{i},b_{i})]=\lambda (b_{i}-a_{i}),$

where $\operatorname {E}$ denotes the expectation operator. In other words, the parameter ${\textstyle \lambda }$ of the Poisson process coincides with the *density* of points. Furthermore, the homogeneous Poisson point process adheres to its own form of the (strong) law of large numbers. More specifically, with probability one:

$\lim _{t\rightarrow \infty }{\frac {N(t)}{t}}=\lambda ,$

where ${\textstyle \lim }$ denotes the limit of a function, and $\lambda$ is expected number of arrivals occurred per unit of time.

#### Memoryless property

The distance between two consecutive points of a point process on the real line will be an exponential random variable with parameter ${\textstyle \lambda }$ (or equivalently, mean ${\textstyle 1/\lambda }$ ). This implies that the points have the memoryless property: the existence of one point existing in a finite interval does not affect the probability (distribution) of other points existing, but this property has no natural equivalence when the Poisson process is defined on a space with higher dimensions.

#### Orderliness and simplicity

A point process with stationary increments is sometimes said to be *orderly* or *regular* if:

$\Pr\{N(t,t+\delta ]>1\}=o(\delta ),$

where little-o notation is being used. A point process is called a **simple point process** when the probability of any of its two points coinciding in the same position, on the underlying space, is zero. For point processes in general on the real line, the property of orderliness implies that the process is simple, which is the case for the homogeneous Poisson point process.

#### Martingale characterization

On the real line, the homogeneous Poisson point process has a connection to the theory of martingales via the following characterization: a point process is the homogeneous Poisson point process if and only if

$N(-\infty ,t]-\lambda t,$

is a martingale.

#### Relationship to other processes

On the real line, the Poisson process is a type of continuous-time Markov process known as a birth process, a special case of the birth–death process (with just births and zero deaths). More complicated processes with the Markov property, such as Markov arrival processes, have been defined where the Poisson process is a special case.

#### Restricted to the half-line

If the homogeneous Poisson process is considered just on the half-line ${\textstyle [0,\infty )}$ , which can be the case when ${\textstyle t}$ represents time then the resulting process is not truly invariant under translation. In that case the Poisson process is no longer stationary, according to some definitions of stationarity.

#### Applications

There have been many applications of the homogeneous Poisson process on the real line in an attempt to model seemingly random and independent events occurring. It has a fundamental role in queueing theory, which is the probability field of developing suitable stochastic models to represent the random arrival and departure of certain phenomena. For example, customers arriving and being served or phone calls arriving at a phone exchange can be both studied with techniques from queueing theory.

#### Generalizations

The homogeneous Poisson process on the real line is considered one of the simplest stochastic processes for counting random numbers of points. This process can be generalized in a number of ways. One possible generalization is to extend the distribution of interarrival times from the exponential distribution to other distributions, which introduces the stochastic process known as a renewal process. Another generalization is to define the Poisson point process on higher dimensional spaces such as the plane.

### Spatial Poisson point process

A **spatial Poisson process** is a Poisson point process defined in the plane $\textstyle \mathbb {R} ^{2}$ . For its mathematical definition, one first considers a bounded, open or closed (or more precisely, Borel measurable) region ${\textstyle B}$ of the plane. The number of points of a point process $\textstyle N$ existing in this region $\textstyle B\subset \mathbb {R} ^{2}$ is a random variable, denoted by $\textstyle N(B)$ . If the points belong to a homogeneous Poisson process with parameter $\textstyle \lambda >0$ , then the probability of $\textstyle n$ points existing in $\textstyle B$ is given by:

$\Pr\{N(B)=n\}={\frac {(\lambda |B|)^{n}}{n!}}e^{-\lambda |B|}$

where $\textstyle |B|$ denotes the area of $\textstyle B$ .

For some finite integer $\textstyle k\geq 1$ , we can give the finite-dimensional distribution of the homogeneous Poisson point process by first considering a collection of disjoint, bounded Borel (measurable) sets $\textstyle B_{1},\dots ,B_{k}$ . The number of points of the point process $\textstyle N$ existing in $\textstyle B_{i}$ can be written as $\textstyle N(B_{i})$ . Then the homogeneous Poisson point process with parameter $\textstyle \lambda >0$ has the finite-dimensional distribution:

$\Pr\{N(B_{i})=n_{i},i=1,\dots ,k\}=\prod _{i=1}^{k}{\frac {(\lambda |B_{i}|)^{n_{i}}}{n_{i}!}}e^{-\lambda |B_{i}|}.$

#### Applications

The spatial Poisson point process features prominently in spatial statistics, stochastic geometry, and continuum percolation theory. This point process is applied in various physical sciences such as a model developed for alpha particles being detected. In recent years, it has been frequently used to model seemingly disordered spatial configurations of certain wireless communication networks. For example, models for cellular or mobile phone networks have been developed where it is assumed the phone network transmitters, known as base stations, are positioned according to a homogeneous Poisson point process.

### Defined in higher dimensions

The previous homogeneous Poisson point process immediately extends to higher dimensions by replacing the notion of area with (high dimensional) volume. For some bounded region $\textstyle B$ of Euclidean space $\textstyle \mathbb {R} ^{d}$ , if the points form a homogeneous Poisson process with parameter $\textstyle \lambda >0$ , then the probability of $\textstyle n$ points existing in $\textstyle B\subset \mathbb {R} ^{d}$ is given by:

$\Pr\{N(B)=n\}={\frac {(\lambda |B|)^{n}}{n!}}e^{-\lambda |B|}$

where $\textstyle |B|$ now denotes the $\textstyle d$ -dimensional volume of $\textstyle B$ . Furthermore, for a collection of disjoint, bounded Borel sets $\textstyle B_{1},\dots ,B_{k}\subset \mathbb {R} ^{d}$ , let $\textstyle N(B_{i})$ denote the number of points of $\textstyle N$ existing in $\textstyle B_{i}$ . Then the corresponding homogeneous Poisson point process with parameter $\textstyle \lambda >0$ has the finite-dimensional distribution:

$\Pr\{N(B_{i})=n_{i},i=1,\dots ,k\}=\prod _{i=1}^{k}{\frac {(\lambda |B_{i}|)^{n_{i}}}{n_{i}!}}e^{-\lambda |B_{i}|}.$

Homogeneous Poisson point processes do not depend on the position of the underlying space through its parameter $\textstyle \lambda$ , which implies it is both a stationary process (invariant to translation) and an isotropic (invariant to rotation) stochastic process. Similarly to the one-dimensional case, the homogeneous point process is restricted to some bounded subset of ${\textstyle \mathbb {R} ^{d}}$ , then depending on some definitions of stationarity, the process is no longer stationary.

### Points are uniformly distributed

If the homogeneous point process is defined on the real line as a mathematical model for occurrences of some phenomenon, then it has the characteristic that the positions of these occurrences or events on the real line (often interpreted as time) will be uniformly distributed. More specifically, if an event occurs (according to this process) in an interval $\textstyle (a,b]$ where $\textstyle a\leq b$ , then its location will be a uniform random variable defined on that interval. Furthermore, the homogeneous point process is sometimes called the *uniform* Poisson point process (see Terminology). This uniformity property extends to higher dimensions in the Cartesian coordinate, but not in, for example, polar coordinates.


## Inhomogeneous Poisson point process

The **inhomogeneous** or **nonhomogeneous** **Poisson point process** (see Terminology) is a Poisson point process with a Poisson parameter set as some location-dependent function in the underlying space on which the Poisson process is defined. For Euclidean space $\textstyle \mathbb {R} ^{d}$ , this is achieved by introducing a locally integrable positive function $\lambda \colon \mathbb {R} ^{d}\to [0,\infty )$ , such that for every bounded region $\textstyle B$ the ( $\textstyle d$ -dimensional) volume integral of $\textstyle \lambda (x)$ over region $\textstyle B$ is finite. In other words, if this integral, denoted by $\textstyle \Lambda (B)$ , is:

$\Lambda (B)=\int _{B}\lambda (x)\,\mathrm {d} x<\infty ,$

where $\textstyle {\mathrm {d} x}$ is a ( $\textstyle d$ -dimensional) volume element, then for every collection of disjoint bounded Borel measurable sets $\textstyle B_{1},\dots ,B_{k}$ , an inhomogeneous Poisson process with (intensity) function $\textstyle \lambda (x)$ has the finite-dimensional distribution:

$\Pr\{N(B_{i})=n_{i},i=1,\dots ,k\}=\prod _{i=1}^{k}{\frac {(\Lambda (B_{i}))^{n_{i}}}{n_{i}!}}e^{-\Lambda (B_{i})}.$

Furthermore, $\textstyle \Lambda (B)$ has the interpretation of being the expected number of points of the Poisson process located in the bounded region $\textstyle B$ , namely

$\Lambda (B)=\operatorname {E} [N(B)].$

### Defined on the real line

On the real line, the inhomogeneous or non-homogeneous Poisson point process has mean measure given by a one-dimensional integral. For two real numbers $\textstyle a$ and $\textstyle b$ , where $\textstyle a\leq b$ , denote by $\textstyle N(a,b]$ the number points of an inhomogeneous Poisson process with intensity function $\textstyle \lambda (t)$ occurring in the interval $\textstyle (a,b]$ . The probability of $\textstyle n$ points existing in the above interval $\textstyle (a,b]$ is given by:

$\Pr\{N(a,b]=n\}={\frac {[\Lambda (a,b)]^{n}}{n!}}e^{-\Lambda (a,b)}.$

where the mean or intensity measure is:

$\Lambda (a,b)=\int _{a}^{b}\lambda (t)\,\mathrm {d} t,$

which means that the random variable $\textstyle N(a,b]$ is a Poisson random variable with mean $\textstyle \operatorname {E} [N(a,b]]=\Lambda (a,b)$ .

A feature of the one-dimension setting, is that an inhomogeneous Poisson process can be transformed into a homogeneous by a monotone transformation or mapping, which is achieved with the inverse of $\textstyle \Lambda$ .

#### Counting process interpretation

The inhomogeneous Poisson point process, when considered on the positive half-line, is also sometimes defined as a counting process. With this interpretation, the process, which is sometimes written as $\textstyle \{N(t),t\geq 0\}$ , represents the total number of occurrences or events that have happened up to and including time $\textstyle t$ . A counting process is said to be an inhomogeneous Poisson counting process if it has the four properties:

- $\textstyle N(0)=0;$
- has independent increments;
- $\textstyle \Pr\{N(t+h)-N(t)=1\}=\lambda (t)h+o(h);$ and
- $\textstyle \Pr\{N(t+h)-N(t)\geq 2\}=o(h),$

where $\textstyle o(h)$ is asymptotic or little-o notation for $\textstyle o(h)/h\rightarrow 0$ as $\textstyle h\rightarrow 0$ . In the case of point processes with refractoriness (e.g., neural spike trains) a stronger version of property 4 applies: $\Pr\{N(t+h)-N(t)\geq 2\}=o(h^{2})$ .

The above properties imply that $\textstyle N(t+h)-N(t)$ is a Poisson random variable with the parameter (or mean)

$\operatorname {E} [N(t+h)-N(t)]=\int _{t}^{t+h}\lambda (s)\,ds,$

which implies

$\operatorname {E} [N(h)]=\int _{0}^{h}\lambda (s)\,ds.$

### Spatial Poisson process

An inhomogeneous Poisson process defined in the plane $\textstyle \mathbb {R} ^{2}$ is called a **spatial Poisson process** It is defined with intensity function and its intensity measure is obtained performing a surface integral of its intensity function over some region. For example, its intensity function (as a function of Cartesian coordinates ${\textstyle x}$ and $\textstyle y$ ) can be

$\lambda (x,y)=e^{-(x^{2}+y^{2})},$

so the corresponding intensity measure is given by the surface integral

$\Lambda (B)=\int _{B}e^{-(x^{2}+y^{2})}\,\mathrm {d} x\,\mathrm {d} y,$

where ${\textstyle B}$ is some bounded region in the plane ${\textstyle \mathbb {R} ^{2}}$ .

### In higher dimensions

In the plane, ${\textstyle \Lambda (B)}$ corresponds to a surface integral while in ${\textstyle \mathbb {R} ^{d}}$ the integral becomes a ( ${\textstyle d}$ -dimensional) volume integral.

### Applications

When the real line is interpreted as time, the inhomogeneous process is used in the fields of counting processes and in queueing theory. Examples of phenomena which have been represented by or appear as an inhomogeneous Poisson point process include:

- Goals being scored in a soccer game.
- Defects in a circuit board

In the plane, the Poisson point process is important in the related disciplines of stochastic geometry and spatial statistics. The intensity measure of this point process is dependent on the location of underlying space, which means it can be used to model phenomena with a density that varies over some region. In other words, the phenomena can be represented as points that have a location-dependent density. This processes has been used in various disciplines and uses include the study of salmon and sea lice in the oceans, forestry, and search problems.

### Interpretation of the intensity function

The Poisson intensity function ${\textstyle \lambda (x)}$ has an interpretation, considered intuitive, with the volume element ${\textstyle \mathrm {d} x}$ in the infinitesimal sense: ${\textstyle \lambda (x)\,\mathrm {d} x}$ is the infinitesimal probability of a point of a Poisson point process existing in a region of space with volume ${\textstyle \mathrm {d} x}$ located at ${\textstyle x}$ .

For example, given a homogeneous Poisson point process on the real line, the probability of finding a single point of the process in a small interval of width ${\textstyle \delta }$ is approximately ${\textstyle \lambda \delta }$ . In fact, such intuition is how the Poisson point process is sometimes introduced and its distribution derived.

### Simple point process

If a Poisson point process has an intensity measure that is a locally finite and diffuse (or non-atomic), then it is a **simple point process**. For a simple point process, the probability of a point existing at a single point or location in the underlying (state) space is either zero or one. This implies that, with probability one, no two (or more) points of a Poisson point process coincide in location in the underlying space.


## Simulation

Simulating a Poisson point process on a computer is usually done in a bounded region of space, known as a simulation *window*, and requires two steps: appropriately creating a random number of points and then suitably placing the points in a random manner. Both these two steps depend on the specific Poisson point process that is being simulated.

### Step 1: Number of points

The number of points ${\textstyle N}$ in the window, denoted here by ${\textstyle W}$ , needs to be simulated, which is done by using a (pseudo)-random number generating function capable of simulating Poisson random variables.

#### Homogeneous case

For the homogeneous case with the constant ${\textstyle \lambda }$ , the mean of the Poisson random variable ${\textstyle N}$ is set to ${\textstyle \lambda |W|}$ where ${\textstyle |W|}$ is the length, area or ( ${\textstyle d}$ -dimensional) volume of ${\textstyle W}$ .

#### Inhomogeneous case

For the inhomogeneous case, ${\textstyle \lambda |W|}$ is replaced with the ( ${\textstyle d}$ -dimensional) volume integral

$\Lambda (W)=\int _{W}\lambda (x)\,\mathrm {d} x$

### Step 2: Positioning of points

The second stage requires randomly placing the $\textstyle N$ points in the window $\textstyle W$ .

#### Homogeneous case

For the homogeneous case in one dimension, all points are uniformly and independently placed in the window or interval $\textstyle W$ . For higher dimensions in a Cartesian coordinate system, each coordinate is uniformly and independently placed in the window $\textstyle W$ . If the window is not a subspace of Cartesian space (for example, inside a unit sphere or on the surface of a unit sphere), then the points will not be uniformly placed in $\textstyle W$ , and suitable change of coordinates (from Cartesian) are needed.

#### Inhomogeneous (heterogeneous) case

For the inhomogeneous case, a couple of different methods can be used depending on the nature of the intensity function $\textstyle \lambda (x)$ . If the intensity function is sufficiently simple, then independent and random non-uniform (Cartesian or other) coordinates of the points can be generated. For example, simulating a Poisson point process on a circular window can be done for an isotropic intensity function (in polar coordinates $\textstyle r$ and $\textstyle \theta$ ), implying it is rotationally variant or independent of $\textstyle \theta$ but dependent on $\textstyle r$ , by a change of variable in $\textstyle r$ if the intensity function is sufficiently simple.

For more complicated intensity functions, one can use an acceptance-rejection method, which consists of using (or 'accepting') only certain random points and not using (or 'rejecting') the other points, based on the ratio:.

${\frac {\lambda (x_{i})}{\Lambda (W)}}={\frac {\lambda (x_{i})}{\int _{W}\lambda (x)\,\mathrm {d} x.}}$

where $\textstyle x_{i}$ is the point under consideration for acceptance or rejection.

That is, a location is uniformly randomly selected for consideration, then to determine whether to place a sample at that location a uniformly randomly drawn number in $[0,1]$ is compared to the probability density function ${\frac {\lambda (x)}{\Lambda (W)}}$ , accepting if it is smaller than the probability density function, and repeating until the previously chosen number of samples have been drawn.


## General Poisson point process

In measure theory, the Poisson point process can be further generalized to what is sometimes known as the **general Poisson point process** or **general Poisson process** by using a Radon measure $\textstyle \Lambda$ , which is a locally finite measure. In general, this Radon measure $\textstyle \Lambda$ can be atomic, which means multiple points of the Poisson point process can exist in the same location of the underlying space. In this situation, the number of points at $\textstyle x$ is a Poisson random variable with mean $\textstyle \Lambda ({x})$ . But sometimes the converse is assumed, so the Radon measure $\textstyle \Lambda$ is diffuse or non-atomic.

A point process $\textstyle {N}$ is a general Poisson point process with intensity $\textstyle \Lambda$ if it has the two following properties:

- the number of points in a bounded Borel set $\textstyle B$ is a Poisson random variable with mean $\textstyle \Lambda (B)$ . In other words, denote the total number of points located in $\textstyle B$ by $\textstyle {N}(B)$ , then the probability of random variable $\textstyle {N}(B)$ being equal to $\textstyle n$ is given by:

$\Pr\{N(B)=n\}={\frac {(\Lambda (B))^{n}}{n!}}e^{-\Lambda (B)}$

- the number of points in $\textstyle n$ disjoint Borel sets forms $\textstyle n$ independent random variables.

The Radon measure $\textstyle \Lambda$ maintains its previous interpretation of being the expected number of points of $\textstyle {N}$ located in the bounded region $\textstyle B$ , namely

$\Lambda (B)=\operatorname {E} [N(B)].$

Furthermore, if $\textstyle \Lambda$ is absolutely continuous such that it has a density (which is the Radon–Nikodym density or derivative) with respect to the Lebesgue measure, then for all Borel sets $\textstyle B$ it can be written as:

$\Lambda (B)=\int _{B}\lambda (x)\,\mathrm {d} x,$

where the density $\textstyle \lambda (x)$ is known, among other terms, as the intensity function.


## History

### Poisson distribution

Despite its name, the Poisson point process was neither discovered nor studied by its namesake. It is cited as an example of Stigler's law of eponymy. The name arises from the process's inherent relation to the Poisson distribution, derived by Poisson as a limiting case of the binomial distribution. It describes the probability of the sum of $\textstyle n$ Bernoulli trials with probability $\textstyle p$ , often likened to the number of heads (or tails) after $\textstyle n$ biased coin flips with the probability of a head (or tail) occurring being $\textstyle p$ . For some positive constant $\textstyle \Lambda >0$ , as $\textstyle n$ increases towards infinity and $\textstyle p$ decreases towards zero such that the product $\textstyle np=\Lambda$ is fixed, the Poisson distribution more closely approximates that of the binomial.

In 1841, Poisson derived the Poisson distribution by studying the binomial distribution in the limit as $\textstyle p$ goes to zero and $\textstyle n$ goes to infinity. The distribution appears only once in Poisson's work, and the result was not well known during his time. Over the following years, others used the distribution without citing Poisson, including Philipp Ludwig von Seidel and Ernst Abbe. At the end of the 19th century, Ladislaus Bortkiewicz revived interest in the distribution by citing Poisson and using real data on the number of deaths from horse kicks in the Prussian army.

### Discovery

There are a number of claims for early uses or discoveries of the Poisson point process. For example, John Michell in 1767, a decade before Poisson was born, was interested in the probability a star being within a certain region of another star under the erroneous assumption that the stars were "scattered by mere chance", and studied an example consisting of the six brightest stars in the Pleiades, without deriving the Poisson distribution. This work inspired Simon Newcomb to study the problem and to calculate the Poisson distribution as an approximation for the binomial distribution in 1860.

At the beginning of the 20th century the Poisson process (in one dimension) would arise independently in different situations. In Sweden 1903, Filip Lundberg published a thesis containing work, now considered fundamental and pioneering, where he proposed to model insurance claims with a homogeneous Poisson process.

In Denmark A.K. Erlang derived the Poisson distribution in 1909 when developing a mathematical model for the number of incoming phone calls in a finite time interval. Erlang unaware of Poisson's earlier work and assumed that the number phone calls arriving in each interval of time were independent of each other. He then found the limiting case, which is effectively recasting the Poisson distribution as a limit of the binomial distribution.

In 1910 Ernest Rutherford and Hans Geiger published experimental results on counting alpha particles. Their experimental work had mathematical contributions from Harry Bateman, who derived Poisson probabilities as a solution to a family of differential equations, though the solution had been derived earlier, resulting in the independent discovery of the Poisson process. After this time, there were many studies and applications of the Poisson process, but its early history is complicated, which has been explained by the various applications of the process in numerous fields by biologists, ecologists, engineers and various physical scientists.

### Early applications

The years after 1909 led to a number of studies and applications of the Poisson point process, however, its early history is complex, which has been explained by the various applications of the process in numerous fields by biologists, ecologists, engineers and others working in the physical sciences. The early results were published in different languages and in different settings, with no standard terminology and notation used. For example, in 1922 Swedish chemist and Nobel Laureate Theodor Svedberg proposed a model in which a spatial Poisson point process is the underlying process to study how plants are distributed in plant communities. A number of mathematicians started studying the process in the early 1930s, and important contributions were made by Andrey Kolmogorov, William Feller and Aleksandr Khinchin, among others. In the field of teletraffic engineering, mathematicians and statisticians studied and used Poisson and other point processes.

### History of terms

The Swede Conny Palm in his 1943 dissertation studied the Poisson and other point processes in the one-dimensional setting by examining them in terms of the statistical or stochastic dependence between the points in time. In his work exists the first known recorded use of the term *point processes* as *Punktprozesse* in German.

It is believed that William Feller was the first in print to refer to it as the *Poisson process* in a 1940 paper. Although the Swede Ove Lundberg used the term *Poisson process* in his 1940 PhD dissertation, in which Feller was acknowledged as an influence, it has been claimed that Feller coined the term before 1940. It has been remarked that both Feller and Lundberg used the term as though it were well-known, implying it was already in spoken use by then. Feller worked from 1936 to 1939 alongside Harald Cramér at Stockholm University, where Lundberg was a PhD student under Cramér who did not use the term *Poisson process* in a book by him, finished in 1936, but did in subsequent editions, which his has led to the speculation that the term *Poisson process* was coined sometime between 1936 and 1939 at the Stockholm University.


## Terminology

The terminology of point process theory in general has been criticized for being too varied. In addition to the word *point* often being omitted, the homogeneous Poisson (point) process is also called a *stationary* Poisson (point) process, as well as *uniform* Poisson (point) process. The inhomogeneous Poisson point process, as well as being called *nonhomogeneous*, is also referred to as the *non-stationary* Poisson process.

The term *point process* has been criticized, as the term *process* can suggest over time and space, so *random point field*, resulting in the terms *Poisson random point field* or *Poisson point field* being also used. A point process is considered, and sometimes called, a random counting measure, hence the Poisson point process is also referred to as a *Poisson random measure*, a term used in the study of Lévy processes, but some choose to use the two terms for Poisson points processes defined on two different underlying spaces.

The underlying mathematical space of the Poisson point process is called a **carrier space**, or **state space**, though the latter term has a different meaning in the context of stochastic processes. In the context of point processes, the term "state space" can mean the space on which the point process is defined such as the real line, which corresponds to the index set or parameter set in stochastic process terminology.

The measure $\textstyle \Lambda$ is called the *intensity measure*, *mean measure*, or *parameter measure*, as there are no standard terms. If $\textstyle \Lambda$ has a derivative or density, denoted by $\textstyle \lambda (x)$ , is called the *intensity function* of the Poisson point process. For the homogeneous Poisson point process, the derivative of the intensity measure is simply a constant $\textstyle \lambda >0$ , which can be referred to as the *rate*, usually when the underlying space is the real line, or the *intensity*. It is also called the *mean rate* or the *mean density* or *rate*. For $\textstyle \lambda =1$ , the corresponding process is sometimes referred to as the *standard Poisson* (point) process.

The extent of the Poisson point process is sometimes called the *exposure*.


## Notation

The notation of the Poisson point process depends on its setting and the field it is being applied in. For example, on the real line, the Poisson process, both homogeneous or inhomogeneous, is sometimes interpreted as a counting process, and the notation $\textstyle \{N(t),t\geq 0\}$ is used to represent the Poisson process.

Another reason for varying notation is due to the theory of point processes, which has a couple of mathematical interpretations. For example, a simple Poisson point process may be considered as a random set, which suggests the notation $\textstyle x\in N$ , implying that $\textstyle x$ is a random point belonging to or being an element of the Poisson point process $\textstyle N$ . Another, more general, interpretation is to consider a Poisson or any other point process as a random counting measure, so one can write the number of points of a Poisson point process $\textstyle {N}$ being found or located in some (Borel measurable) region $\textstyle B$ as $\textstyle N(B)$ , which is a random variable. These different interpretations results in notation being used from mathematical fields such as measure theory and set theory.

For general point processes, sometimes a subscript on the point symbol, for example $\textstyle x$ , is included so one writes (with set notation) $\textstyle x_{i}\in N$ instead of $\textstyle x\in N$ , and $\textstyle x$ can be used for the bound variable in integral expressions such as Campbell's theorem, instead of denoting random points. Sometimes an uppercase letter denotes the point process, while a lowercase denotes a point from the process, so, for example, the point $\textstyle x$ or $\textstyle x_{i}$ belongs to or is a point of the point process $\textstyle X$ , and be written with set notation as $\textstyle x\in X$ or $\textstyle x_{i}\in X$ .

Furthermore, the set theory and integral or measure theory notation can be used interchangeably. For example, for a point process $\textstyle N$ defined on the Euclidean state space $\textstyle {\mathbb {R} ^{d}}$ and a (measurable) function $\textstyle f$ on $\textstyle \mathbb {R} ^{d}$ , the expression

$\int _{\mathbb {R} ^{d}}f(x)\,\mathrm {d} N(x)=\sum \limits _{x_{i}\in N}f(x_{i}),$

demonstrates two different ways to write a summation over a point process (see also Campbell's theorem (probability)). More specifically, the integral notation on the left-hand side is interpreting the point process as a random counting measure while the sum on the right-hand side suggests a random set interpretation.


## Functionals and moment measures

In probability theory, operations are applied to random variables for different purposes. Sometimes these operations are regular expectations that produce the average or variance of a random variable. Others, such as characteristic functions (or Laplace transforms) of a random variable can be used to uniquely identify or characterize random variables and prove results like the central limit theorem. In the theory of point processes there exist analogous mathematical tools which usually exist in the forms of measures and functionals instead of moments and functions respectively.

### Laplace functionals

For a Poisson point process $\textstyle N$ with intensity measure $\textstyle \Lambda$ on some space X , the Laplace functional is given by:

$L_{N}(f)=\mathbb {E} e^{-\int _{X}f(x)\,N(\mathrm {d} x)}=e^{-\int _{X}(1-e^{-f(x)})\Lambda (\mathrm {d} x)},$

One version of Campbell's theorem involves the Laplace functional of the Poisson point process.

### Probability generating functionals

The probability generating function of non-negative integer-valued random variable leads to the probability generating functional being defined analogously with respect to any non-negative bounded function $\textstyle v$ on $\textstyle \mathbb {R} ^{d}$ such that $\textstyle 0\leq v(x)\leq 1$ . For a point process $\textstyle {N}$ the probability generating functional is defined as:

$G(v)=\operatorname {E} \left[\prod _{x\in N}v(x)\right]$

where the product is performed for all the points in ${\textstyle N}$ . If the intensity measure $\textstyle \Lambda$ of $\textstyle {N}$ is locally finite, then the ${\textstyle G}$ is well-defined for any measurable function $\textstyle u$ on $\textstyle \mathbb {R} ^{d}$ . For a Poisson point process with intensity measure $\textstyle \Lambda$ the generating functional is given by:

$G(v)=e^{-\int _{\mathbb {R} ^{d}}[1-v(x)]\,\Lambda (\mathrm {d} x)},$

which in the homogeneous case reduces to

$G(v)=e^{-\lambda \int _{\mathbb {R} ^{d}}[1-v(x)]\,\mathrm {d} x}.$

### Moment measure

For a general Poisson point process with intensity measure $\textstyle \Lambda$ the first moment measure is its intensity measure:

$M^{1}(B)=\Lambda (B),$

which for a homogeneous Poisson point process with constant intensity $\textstyle \lambda$ means:

$M^{1}(B)=\lambda |B|,$

where $\textstyle |B|$ is the length, area or volume (or more generally, the Lebesgue measure) of $\textstyle B$ .

### The Mecke equation

The Mecke equation characterizes the Poisson point process. Let $\mathbb {N} _{\sigma }$ be the space of all $\sigma$ -finite measures on some general space ${\mathcal {Q}}$ . A point process $\eta$ with intensity $\lambda$ on ${\mathcal {Q}}$ is a Poisson point process if and only if for all measurable functions $f:{\mathcal {Q}}\times \mathbb {N} _{\sigma }\to \mathbb {R} _{+}$ the following holds

$E\left[\int f(x,\eta )\eta (\mathrm {d} x)\right]=\int E\left[f(x,\eta +\delta _{x})\right]\lambda (\mathrm {d} x)$

For further details see.

### Factorial moment measure

For a general Poisson point process with intensity measure $\textstyle \Lambda$ the $\textstyle n$ -th factorial moment measure is given by the expression:

$M^{(n)}(B_{1}\times \cdots \times B_{n})=\prod _{i=1}^{n}[\Lambda (B_{i})],$

where $\textstyle \Lambda$ is the intensity measure or first moment measure of $\textstyle {N}$ , which for some Borel set $\textstyle B$ is given by

$\Lambda (B)=M^{1}(B)=\operatorname {E} [N(B)].$

For a homogeneous Poisson point process the $\textstyle n$ -th factorial moment measure is simply:

$M^{(n)}(B_{1}\times \cdots \times B_{n})=\lambda ^{n}\prod _{i=1}^{n}|B_{i}|,$

where $\textstyle |B_{i}|$ is the length, area, or volume (or more generally, the Lebesgue measure) of $\textstyle B_{i}$ . Furthermore, the $\textstyle n$ -th factorial moment density is:

$\mu ^{(n)}(x_{1},\dots ,x_{n})=\lambda ^{n}.$


## Avoidance function

The **avoidance function** or **void probability** $\textstyle v$ of a point process $\textstyle {N}$ is defined in relation to some set $\textstyle B$ , which is a subset of the underlying space $\textstyle \mathbb {R} ^{d}$ , as the probability of no points of $\textstyle {N}$ existing in $\textstyle B$ . More precisely, for a test set $\textstyle B$ , the avoidance function is given by:

$v(B)=\Pr\{N(B)=0\}.$

For a general Poisson point process $\textstyle {N}$ with intensity measure $\textstyle \Lambda$ , its avoidance function is given by:

$v(B)=e^{-\Lambda (B)}$

### Rényi’s theorem

Simple point processes are completely characterized by their void probabilities. In other words, complete information of a simple point process is captured entirely in its void probabilities, and two simple point processes have the same void probabilities if and if only if they are the same point processes. The case for Poisson process is sometimes known as **Rényi’s theorem**, which is named after Alfréd Rényi who discovered the result for the case of a homogeneous point process in one dimension.

In one form Rényi’s theorem says that, if $\textstyle \Lambda$ is a diffuse (or non-atomic) Radon measure on $\textstyle \mathbb {R} ^{d}$ and $\textstyle N$ is a locally finite simple point process on $\textstyle \mathbb {R} ^{d}$ such that for any set $\textstyle A$ being a finite union of rectangles there holds true:

$\Pr\{N(A)=0\}=v(A)=e^{-\Lambda (A)}$

,

then $\textstyle N$ is a Poisson point process with intensity measure $\textstyle \Lambda$ .
