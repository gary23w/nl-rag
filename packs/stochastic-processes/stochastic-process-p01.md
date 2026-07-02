---
title: "Stochastic process (part 1/2)"
source: https://en.wikipedia.org/wiki/Stochastic_process
domain: stochastic-processes
license: CC-BY-SA-4.0
tags: stochastic process, wiener process, brownian motion, stochastic calculus
fetched: 2026-07-02
part: 1/2
---

# Stochastic process

In probability theory and related fields a **stochastic** (/stəˈkæstɪk/) or **random process** is a mathematical object usually defined as a family of random variables in a probability space, where the index of the family often has the interpretation of time. Stochastic processes are widely used as mathematical models of systems and phenomena that appear to vary in a random manner. Examples include the growth of a bacterial population, an electrical current fluctuating due to thermal noise, or the movement of a gas molecule. Stochastic processes have applications in many disciplines such as biology, chemistry, ecology, neuroscience, physics, image processing, signal processing, control theory, information theory, computer science, and telecommunications. Furthermore, seemingly random changes in financial markets have motivated the extensive use of stochastic processes in finance.

Applications and real-world phenomena have repeatedly motivated mathematicians to propose new stochastic processes. Two classic examples are the Wiener process (also called the Brownian motion process) and the Poisson process. Louis Bachelier used the Wiener process to model price changes on the Paris Bourse, while A. K. Erlang used the Poisson process to model the number of phone calls occurring in a given period of time. These two processes are widely treated as central to the theory of stochastic processes, and they were invented repeatedly and independently, both before and after Bachelier and Erlang, in different settings and countries.

The term **random function** is also used to refer to a stochastic or random process, because a stochastic process can also be interpreted as a random element in a function space. The terms *stochastic process* and *random process* are used interchangeably, often with no specific mathematical space for the set that indexes the random variables. But often these two terms are used when the random variables are indexed by the integers or an interval of the real line. If the random variables are indexed by the Cartesian plane or some higher-dimensional Euclidean space, then the collection of random variables is usually called a random field instead. The values of a stochastic process are not always numbers and can be vectors or other mathematical objects.

Based on their mathematical properties, stochastic processes can be grouped into various categories, which include random walks, martingales, Markov processes, Lévy processes, Gaussian processes, random fields, renewal processes, and branching processes. The study of stochastic processes uses mathematical knowledge and techniques from probability, calculus, linear algebra, set theory, and topology as well as branches of mathematical analysis such as real analysis, measure theory, Fourier analysis, and functional analysis. The theory of stochastic processes is considered to be an important contribution to mathematics and it continues to be an active topic of research for both theoretical reasons and applications.


## Introduction

A stochastic or random process can be defined as a collection of random variables that is indexed by some mathematical set, meaning that each random variable of the stochastic process is uniquely associated with an element in the set. The set used to index the random variables is called the index set. Historically, the index set was some subset of the real line, such as the natural numbers, giving the index set the interpretation of time. Each random variable in the collection takes values from the same mathematical space known as the **state space**. This state space can be, for example, the integers, the real line or n -dimensional Euclidean space. An **increment** is the amount that a stochastic process changes between two index values, often interpreted as two points in time. A stochastic process can have many outcomes, due to its randomness, and a single outcome of a stochastic process is called, among other names, a **sample function** or **realization**.

### Classifications

A stochastic process can be classified in different ways, for example, by its state space, its index set, or the dependence among the random variables. One common way of classification is by the cardinality of the index set and the state space.

When interpreted as time, if the index set of a stochastic process has a finite or countable number of elements, such as a finite set of numbers, the set of integers, or the natural numbers, then the stochastic process is said to be in **discrete time**. If the index set is some interval of the real line, then time is said to be **continuous**. The two types of stochastic processes are respectively referred to as **discrete-time** and **continuous-time stochastic processes**. Discrete-time stochastic processes are considered easier to study because continuous-time processes require more advanced mathematical techniques and knowledge, particularly due to the index set being uncountable. If the index set is the integers, or some subset of them, then the stochastic process can also be called a **random sequence**.

If the state space is the integers or natural numbers, then the stochastic process is called a **discrete** or **integer-valued stochastic process**. If the state space is the real line, then the stochastic process is referred to as a **real-valued stochastic process** or a **process with continuous state space**. If the state space is n -dimensional Euclidean space, then the stochastic process is called a n -**dimensional vector process** or n -**vector process**.

### Etymology

The word *stochastic* in English was originally used as an adjective with the definition "pertaining to conjecturing", and stemming from a Greek word meaning "to aim at a mark, guess", and the Oxford English Dictionary gives the year 1662 as its earliest occurrence. In his work on probability *Ars Conjectandi*, originally published in Latin in 1713, Jakob Bernoulli used the phrase "Ars Conjectandi sive Stochastice", which has been translated to "the art of conjecturing or stochastics". This phrase was used, with reference to Bernoulli, by Ladislaus Bortkiewicz who in 1917 wrote in German the word *stochastik* with a sense meaning random. The term *stochastic process* first appeared in English in a 1934 paper by Joseph Doob. For the term and a specific mathematical definition, Doob cited another 1934 paper, where the term *stochastischer Prozeß* was used in German by Aleksandr Khinchin, though the German term had been used earlier, for example, by Andrei Kolmogorov in 1931.

According to the Oxford English Dictionary, early occurrences of the word *random* in English with its current meaning, which relates to chance or luck, date back to the 16th century, while earlier recorded usages started in the 14th century as a noun meaning "impetuosity, great speed, force, or violence (in riding, running, striking, etc.)". The word itself comes from a Middle French word meaning "speed, haste", and it is probably derived from a French verb meaning "to run" or "to gallop". The first written appearance of the term *random process* pre-dates *stochastic process*, which the Oxford English Dictionary also gives as a synonym, and was used in an article by Francis Edgeworth published in 1888.

### Terminology

The definition of a stochastic process varies, but a stochastic process is traditionally defined as a collection of random variables indexed by some set. The terms *random process* and *stochastic process* are considered synonyms and are used interchangeably, without the index set being precisely specified. Both "collection", or "family" are used while instead of "index set", sometimes the terms "parameter set" or "parameter space" are used.

The term *random function* is also used to refer to a stochastic or random process, though sometimes it is only used when the stochastic process takes real values. This term is also used when the index sets are mathematical spaces other than the real line, while the terms *stochastic process* and *random process* are usually used when the index set is interpreted as time, and other terms are used such as *random field* when the index set is n -dimensional Euclidean space $\mathbb {R} ^{n}$ or a manifold.

### Notation

A stochastic process can be denoted, among other ways, by $\{X(t)\}_{t\in T}$ , $\{X_{t}\}_{t\in T}$ , $\{X_{t}\}$ $\{X(t)\}$ or simply as X . Some authors mistakenly write $X(t)$ even though it is an abuse of function notation. For example, $X(t)$ or $X_{t}$ are used to refer to the random variable with the index t , and not the entire stochastic process. If the index set is $T=[0,\infty )$ , then one can write, for example, $(X_{t},t\geq 0)$ to denote the stochastic process.


## Examples

### Bernoulli process

One of the simplest stochastic processes is the Bernoulli process, which is a sequence of independent and identically distributed (iid) random variables, where each random variable takes either the value one or zero, say one with probability p and zero with probability $1-p$ . This process can be linked to an idealisation of repeatedly flipping a coin, where the probability of obtaining a head is taken to be p and its value is one, while the value of a tail is zero. In other words, a Bernoulli process is a sequence of iid Bernoulli random variables, where each idealised coin flip is an example of a Bernoulli trial.

### Random walk

Random walks are stochastic processes that are usually defined as sums of iid random variables or random vectors in Euclidean space, so they are processes that change in discrete time. But some also use the term to refer to processes that change in continuous time, particularly the Wiener process used in financial models, which has led to some confusion, resulting in its criticism. There are various other types of random walks, defined so their state spaces can be other mathematical objects, such as lattices and groups, and in general they are highly studied and have many applications in different disciplines.

A classic example of a random walk is known as the *simple random walk*, which is a stochastic process in discrete time with the integers as the state space, and is based on a Bernoulli process, where each Bernoulli variable takes either the value positive one or negative one. In other words, the simple random walk takes place on the integers, and its value increases by one with probability, say, p , or decreases by one with probability $1-p$ , so the index set of this random walk is the natural numbers, while its state space is the integers. If $p=0.5$ , this random walk is called a symmetric random walk.

### Wiener process

The Wiener process is a stochastic process with stationary and independent increments that are normally distributed based on the size of the increments. The Wiener process is named after Norbert Wiener, who proved its mathematical existence, but the process is also called the Brownian motion process or just Brownian motion due to its historical connection as a model for Brownian movement in liquids.

Playing a central role in the theory of probability, the Wiener process is often considered the most important and studied stochastic process, with connections to other stochastic processes. Its index set and state space are the non-negative numbers and real numbers, respectively, so it has both continuous index set and states space. But the process can be defined more generally so its state space can be n -dimensional Euclidean space. If the mean of any increment is zero, then the resulting Wiener or Brownian motion process is said to have zero drift. If the mean of the increment for any two points in time is equal to the time difference multiplied by some constant $\mu$ , which is a real number, then the resulting stochastic process is said to have drift $\mu$ .

Almost surely, a sample path of a Wiener process is continuous everywhere but nowhere differentiable. It can be considered as a continuous version of the simple random walk. The process arises as the mathematical limit of other stochastic processes such as certain random walks rescaled, which is the subject of Donsker's theorem or invariance principle, also known as the functional central limit theorem.

The Wiener process is a member of some important families of stochastic processes, including Markov processes, Lévy processes and Gaussian processes. The process also has many applications and is the main stochastic process used in stochastic calculus. It plays a central role in quantitative finance, where it is used, for example, in the Black–Scholes–Merton model. The process is also used in different fields, including the majority of natural sciences as well as some branches of social sciences, as a mathematical model for various random phenomena.

### Poisson process

The Poisson process is a stochastic process that has different forms and definitions. It can be defined as a counting process, which is a stochastic process that represents the random number of points or events up to some time. The number of points of the process that are located in the interval from zero to some given time is a Poisson random variable that depends on that time and some parameter. This process has the natural numbers as its state space and the non-negative numbers as its index set. This process is also called the Poisson counting process, since it can be interpreted as an example of a counting process.

If a Poisson process is defined with a single positive constant, then the process is called a homogeneous Poisson process. The homogeneous Poisson process is a member of important classes of stochastic processes such as Markov processes and Lévy processes.

The homogeneous Poisson process can be defined and generalized in different ways. It can be defined such that its index set is the real line, and this stochastic process is also called the stationary Poisson process. If the parameter constant of the Poisson process is replaced with some non-negative integrable function of t , the resulting process is called an inhomogeneous or nonhomogeneous Poisson process, where the average density of points of the process is no longer constant. Serving as a fundamental process in queueing theory, the Poisson process is an important process for mathematical models, where it finds applications for models of events randomly occurring in certain time windows.

Defined on the real line, the Poisson process can be interpreted as a stochastic process, among other random objects. But then it can be defined on the n -dimensional Euclidean space or other mathematical spaces, where it is often interpreted as a random set or a random counting measure, instead of a stochastic process. In this setting, the Poisson process, also called the Poisson point process, is one of the most important objects in probability theory, both for applications and theoretical reasons. But it has been remarked that the Poisson process does not receive as much attention as it should, partly due to it often being considered just on the real line, and not on other mathematical spaces.


## Definitions

### Stochastic process

A stochastic process is defined as a collection of random variables defined on a common probability space $(\Omega ,{\mathcal {F}},P)$ , where $\Omega$ is a sample space, ${\mathcal {F}}$ is a $\sigma$ -algebra, and P is a probability measure; and the random variables, indexed by some set T , all take values in the same mathematical space S , which must be measurable with respect to some $\sigma$ -algebra $\Sigma$ .

In other words, for a given probability space $(\Omega ,{\mathcal {F}},P)$ and a measurable space $(S,\Sigma )$ , a stochastic process is a collection of S -valued random variables, which can be written as:

$\{X(t):t\in T\}.$

Historically, in many problems from the natural sciences a point $t\in T$ had the meaning of time, so $X(t)$ is a random variable representing a value observed at time t . A stochastic process can also be written as $\{X(t,\omega ):t\in T\}$ to reflect that it is actually a function of two variables, $t\in T$ and $\omega \in \Omega$ .

There are other ways to consider a stochastic process, with the above definition being considered the traditional one. For example, a stochastic process can be interpreted or defined as a $S^{T}$ -valued random variable, where $S^{T}$ is the space of all the possible functions from the set T into the space S . However this alternative definition as a "function-valued random variable" in general requires additional regularity assumptions to be well-defined.

### Index set

The set T is called the **index set** or **parameter set** of the stochastic process. Often this set is some subset of the real line, such as the natural numbers or an interval, giving the set T the interpretation of time. In addition to these sets, the index set T can be another set with a total order or a more general set, such as the Cartesian plane $\mathbb {R} ^{2}$ or n -dimensional Euclidean space, where an element $t\in T$ can represent a point in space. That said, many results and theorems are only possible for stochastic processes with a totally ordered index set.

### State space

The mathematical space S of a stochastic process is called its *state space*. This mathematical space can be defined using integers, real lines, n -dimensional Euclidean spaces, complex planes, or more abstract mathematical spaces. The state space is defined using elements that reflect the different values that the stochastic process can take.

### Sample function

A **sample function** is a single outcome of a stochastic process, so it is formed by taking a single possible value of each random variable of the stochastic process. More precisely, if $\{X(t,\omega ):t\in T\}$ is a stochastic process, then for any point $\omega \in \Omega$ , the mapping

$X(\cdot ,\omega ):T\rightarrow S,$

is called a sample function, a **realization**, or, particularly when T is interpreted as time, a **sample path** of the stochastic process $\{X(t,\omega ):t\in T\}$ . This means that for a fixed $\omega \in \Omega$ , there exists a sample function that maps the index set T to the state space S . Other names for a sample function of a stochastic process include **trajectory**, **path function** or **path**.

### Increment

An **increment** of a stochastic process is the difference between two random variables of the same stochastic process. For a stochastic process with an index set that can be interpreted as time, an increment is how much the stochastic process changes over a certain time period. For example, if $\{X(t):t\in T\}$ is a stochastic process with state space S and index set $T=[0,\infty )$ , then for any two non-negative numbers $t_{1}\in [0,\infty )$ and $t_{2}\in [0,\infty )$ such that $t_{1}\leq t_{2}$ , the difference $X_{t_{2}}-X_{t_{1}}$ is a S -valued random variable known as an increment. When interested in the increments, often the state space S is the real line or the natural numbers, but it can be n -dimensional Euclidean space or more abstract spaces such as Banach spaces.

### Further definitions

#### Law

For a stochastic process $X\colon \Omega \rightarrow S^{T}$ defined on the probability space $(\Omega ,{\mathcal {F}},P)$ , the **law** of stochastic process X is defined as the pushforward measure:

$\mu =P\circ X^{-1},$

where P is a probability measure, the symbol $\circ$ denotes function composition and $X^{-1}$ is the pre-image of the measurable function or, equivalently, the $S^{T}$ -valued random variable X , where $S^{T}$ is the space of all the possible S -valued functions of $t\in T$ , so the law of a stochastic process is a probability measure.

For a measurable subset B of $S^{T}$ , the pre-image of X gives

$X^{-1}(B)=\{\omega \in \Omega :X(\omega )\in B\},$

so the law of a X can be written as:

$\mu (B)=P(\{\omega \in \Omega :X(\omega )\in B\}).$

The law of a stochastic process or a random variable is also called the **probability law**, **probability distribution**, or the **distribution**.

#### Finite-dimensional probability distributions

For a stochastic process X with law $\mu$ , its **finite-dimensional distribution** for $t_{1},\dots ,t_{n}\in T$ is defined as:

$\mu _{t_{1},\dots ,t_{n}}=P\circ (X({t_{1}}),\dots ,X({t_{n}}))^{-1},$

This measure $\mu _{t_{1},..,t_{n}}$ is the joint distribution of the random vector $(X({t_{1}}),\dots ,X({t_{n}}))$ ; it can be viewed as a "projection" of the law $\mu$ onto a finite subset of T .

For any measurable subset C of the n -fold Cartesian power $S^{n}=S\times \dots \times S$ , the finite-dimensional distributions of a stochastic process X can be written as:

${\displaystyle \mu _{t_{1},\dots ,t_{n}}(C)=P{\Big (}{\big \{}\omega \in \Omega$

The finite-dimensional distributions of a stochastic process satisfy two mathematical conditions known as consistency conditions.

#### Stationarity

**Stationarity** is a mathematical property that a stochastic process has when all the random variables of that stochastic process are identically distributed. In other words, if X is a stationary stochastic process, then for any $t\in T$ the random variable $X_{t}$ has the same distribution, which means that for any set of n index set values $t_{1},\dots ,t_{n}$ , the corresponding n random variables

$X_{t_{1}},\dots X_{t_{n}},$

all have the same probability distribution. The index set of a stationary stochastic process is usually interpreted as time, so it can be the integers or the real line. But the concept of stationarity also exists for point processes and random fields, where the index set is not interpreted as time.

When the index set T can be interpreted as time, a stochastic process is said to be stationary if its finite-dimensional distributions are invariant under translations of time. This type of stochastic process can be used to describe a physical system that is in steady state, but still experiences random fluctuations. The intuition behind stationarity is that as time passes the distribution of the stationary stochastic process remains the same. A sequence of random variables forms a stationary stochastic process only if the random variables are identically distributed.

A stochastic process with the above definition of stationarity is sometimes said to be strictly stationary, but there are other forms of stationarity. One example is when a discrete-time or continuous-time stochastic process X is said to be stationary in the wide sense, then the process X has a finite second moment for all $t\in T$ and the covariance of the two random variables $X_{t}$ and $X_{t+h}$ depends only on the number h for all $t\in T$ . Khinchin introduced the related concept of **stationarity in the wide sense**, which has other names including **covariance stationarity** or **stationarity in the broad sense**.

#### Filtration

A filtration is an increasing sequence of sigma-algebras defined in relation to some probability space and an index set that has some total order relation, such as in the case of the index set being some subset of the real numbers. More formally, if a stochastic process has an index set with a total order, then a filtration $\{{\mathcal {F}}_{t}\}_{t\in T}$ , on a probability space $(\Omega ,{\mathcal {F}},P)$ is a family of sigma-algebras such that ${\mathcal {F}}_{s}\subseteq {\mathcal {F}}_{t}\subseteq {\mathcal {F}}$ for all $s\leq t$ , where $t,s\in T$ and $\leq$ denotes the total order of the index set T . With the concept of a filtration, it is possible to study the amount of information contained in a stochastic process $X_{t}$ at $t\in T$ , which can be interpreted as time t . The intuition behind a filtration ${\mathcal {F}}_{t}$ is that as time t passes, more and more information on $X_{t}$ is known or available, which is captured in ${\mathcal {F}}_{t}$ , resulting in finer and finer partitions of $\Omega$ .

#### Modification

A **modification** of a stochastic process is another stochastic process, which is closely related to the original stochastic process. More precisely, a stochastic process X that has the same index set T , state space S , and probability space $(\Omega ,{\cal {F}},P)$ as another stochastic process Y is said to be a modification of X if for all $t\in T$ the following

$P(X_{t}=Y_{t})=1,$

holds. Two stochastic processes that are modifications of each other have the same finite-dimensional law and they are said to be **stochastically equivalent** or **equivalent**.

Instead of modification, the term **version** is also used, however some authors use the term version when two stochastic processes have the same finite-dimensional distributions, but they may be defined on different probability spaces, so two processes that are modifications of each other, are also versions of each other, in the latter sense, but not the converse.

If a continuous-time real-valued stochastic process meets certain moment conditions on its increments, then the Kolmogorov continuity theorem says that there exists a modification of this process that has continuous sample paths with probability one, so the stochastic process has a continuous modification or version. The theorem can also be generalized to random fields so the index set is n -dimensional Euclidean space as well as to stochastic processes with metric spaces as their state spaces.

#### Indistinguishable

Two stochastic processes X and Y defined on the same probability space $(\Omega ,{\mathcal {F}},P)$ with the same index set T and set space S are said be **indistinguishable** if the following

$P(X_{t}=Y_{t}{\text{ for all }}t\in T)=1,$

holds. If two X and Y are modifications of each other and are almost surely continuous, then X and Y are indistinguishable.

#### Separability

**Separability** is a property of a stochastic process based on its index set in relation to the probability measure. The property is assumed so that functionals of stochastic processes or random fields with uncountable index sets can form random variables. For a stochastic process to be separable, in addition to other conditions, its index set must be a separable space, which means that the index set has a dense countable subset.

More precisely, a real-valued continuous-time stochastic process X on a probability space $(\Omega ,{\cal {F}},P)$ is separable iff its index set T has a dense countable subset $U\subset T$ and there is a set $\Omega _{0}\subset \Omega$ of probability zero, so $P(\Omega _{0})=0$ , such that for every open set $G\subset T$ and every closed set $F\subset \mathbb {R} =(-\infty ,\infty )$ , the two events $\{X_{t}\in F{\text{ for all }}t\in G\cap U\}$ and $\{X_{t}\in F{\text{ for all }}t\in G\}$ differ from each other at most on a subset of $\Omega _{0}$ . The definition of separability can also be stated for other index sets and state spaces, such as in the case of random fields, where the index set as well as the state space can be n -dimensional Euclidean space.

The concept of separability of a stochastic process was introduced by Joseph Doob. The underlying idea of separability is to make a countable set of points of the index set determine the properties of the stochastic process. Any stochastic process with a countable index set already meets the separability conditions, so discrete-time stochastic processes are always separable. A theorem by Doob, sometimes known as Doob’s separability theorem, says that any real-valued continuous-time stochastic process has a separable modification. Versions of this theorem also exist for more general stochastic processes with index sets and state spaces other than the real line.

#### Independence

Two stochastic processes X and Y defined on the same probability space $(\Omega ,{\mathcal {F}},P)$ with the same index set T are said be **independent** if for all $n\in \mathbb {N}$ and for every choice of epochs $t_{1},\ldots ,t_{n}\in T$ , the random vectors $\left(X(t_{1}),\ldots ,X(t_{n})\right)$ and $\left(Y(t_{1}),\ldots ,Y(t_{n})\right)$ are independent.

#### Uncorrelatedness

Two stochastic processes $\left\{X_{t}\right\}$ and $\left\{Y_{t}\right\}$ are called **uncorrelated** if their cross-covariance $\operatorname {K} _{\mathbf {X} \mathbf {Y} }(t_{1},t_{2})=\operatorname {E} \left[\left(X(t_{1})-\mu _{X}(t_{1})\right)\left(Y(t_{2})-\mu _{Y}(t_{2})\right)\right]$ is zero for all times. Formally:

$\left\{X_{t}\right\},\left\{Y_{t}\right\}{\text{ uncorrelated}}\quad \iff \quad \operatorname {K} _{\mathbf {X} \mathbf {Y} }(t_{1},t_{2})=0\quad \forall t_{1},t_{2}$

.

#### Independence implies uncorrelatedness

If two stochastic processes X and Y are independent, then they are also uncorrelated.

#### Orthogonality

Two stochastic processes $\left\{X_{t}\right\}$ and $\left\{Y_{t}\right\}$ are called **orthogonal** if their cross-correlation $\operatorname {R} _{\mathbf {X} \mathbf {Y} }(t_{1},t_{2})=\operatorname {E} [X(t_{1}){\overline {Y(t_{2})}}]$ is zero for all times. Formally:

$\left\{X_{t}\right\},\left\{Y_{t}\right\}{\text{ orthogonal}}\quad \iff \quad \operatorname {R} _{\mathbf {X} \mathbf {Y} }(t_{1},t_{2})=0\quad \forall t_{1},t_{2}$

.

#### Skorokhod space

A **Skorokhod space**, also written as **Skorohod space**, is a mathematical space of all the functions that are right-continuous with left limits, defined on some interval of the real line such as $[0,1]$ or $[0,\infty )$ , and take values on the real line or on some metric space. Such functions are known as càdlàg or cadlag functions, based on the acronym of the French phrase *continue à droite, limite à gauche*. A Skorokhod function space, introduced by Anatoliy Skorokhod, is often denoted with the letter D , so the function space is also referred to as space D . The notation of this function space can also include the interval on which all the càdlàg functions are defined, so, for example, $D[0,1]$ denotes the space of càdlàg functions defined on the unit interval $[0,1]$ .

Skorokhod function spaces are frequently used in the theory of stochastic processes because it often assumed that the sample functions of continuous-time stochastic processes belong to a Skorokhod space. Such spaces contain continuous functions, which correspond to sample functions of the Wiener process. But the space also has functions with discontinuities, which means that the sample functions of stochastic processes with jumps, such as the Poisson process (on the real line), are also members of this space.

#### Regularity

In the context of mathematical construction of stochastic processes, the term **regularity** is used when discussing and assuming certain conditions for a stochastic process to resolve possible construction issues. For example, to study stochastic processes with uncountable index sets, it is assumed that the stochastic process adheres to some type of regularity condition such as the sample functions being continuous.


## Further examples

### Markov processes and chains

Markov processes are stochastic processes, traditionally in discrete or continuous time, that have the Markov property, which means the next value of the Markov process depends on the current value, but it is conditionally independent of the previous values of the stochastic process. In other words, the behavior of the process in the future is stochastically independent of its behavior in the past, given the current state of the process.

The Brownian motion process and the Poisson process (in one dimension) are both examples of Markov processes in continuous time, while random walks on the integers and the gambler's ruin problem are examples of Markov processes in discrete time.

A Markov chain is a type of Markov process that has either discrete state space or discrete index set (often representing time), but the precise definition of a Markov chain varies. For example, it is common to define a Markov chain as a Markov process in either discrete or continuous time with a countable state space (thus regardless of the nature of time), but it has been also common to define a Markov chain as having discrete time in either countable or continuous state space (thus regardless of the state space). It has been argued that the first definition of a Markov chain, where it has discrete time, now tends to be used, despite the second definition having been used by researchers like Joseph Doob and Kai Lai Chung.

Markov processes form an important class of stochastic processes and have applications in many areas. For example, they are the basis for a general stochastic simulation method known as Markov chain Monte Carlo, which is used for simulating random objects with specific probability distributions, and has found application in Bayesian statistics.

The concept of the Markov property was originally for stochastic processes in continuous and discrete time, but the property has been adapted for other index sets such as n -dimensional Euclidean space, which results in collections of random variables known as Markov random fields.

### Martingale

A martingale is a discrete-time or continuous-time stochastic process with the property that, at every instant, given the current value and all the past values of the process, the conditional expectation of every future value is equal to the current value. In discrete time, if this property holds for the next value, then it holds for all future values. The exact mathematical definition of a martingale requires two other conditions coupled with the mathematical concept of a filtration, which is related to the intuition of increasing available information as time passes. Martingales are usually defined to be real-valued, but they can also be complex-valued or even more general.

A symmetric random walk and a Wiener process (with zero drift) are both examples of martingales, respectively, in discrete and continuous time. For a sequence of independent and identically distributed random variables $X_{1},X_{2},X_{3},\dots$ with zero mean, the stochastic process formed from the successive partial sums $X_{1},X_{1}+X_{2},X_{1}+X_{2}+X_{3},\dots$ is a discrete-time martingale. In this aspect, discrete-time martingales generalize the idea of partial sums of independent random variables.

Martingales can also be created from stochastic processes by applying some suitable transformations, which is the case for the homogeneous Poisson process (on the real line) resulting in a martingale called the *compensated Poisson process*. Martingales can also be built from other martingales. For example, there are martingales based on the martingale the Wiener process, forming continuous-time martingales.

Martingales mathematically formalize the idea of a 'fair game' where it is possible form reasonable expectations for payoffs, and they were originally developed to show that it is not possible to gain an 'unfair' advantage in such a game. But now they are used in many areas of probability, which is one of the main reasons for studying them. Many problems in probability have been solved by finding a martingale in the problem and studying it. Martingales will converge, given some conditions on their moments, so they are often used to derive convergence results, due largely to martingale convergence theorems.

Martingales have many applications in statistics, but it has been remarked that its use and application are not as widespread as it could be in the field of statistics, particularly statistical inference. They have found applications in areas in probability theory such as queueing theory and Palm calculus and other fields such as economics and finance.

### Lévy process

Lévy processes are types of stochastic processes that can be considered as generalizations of random walks in continuous time. These processes have many applications in fields such as finance, fluid mechanics, physics and biology. The main defining characteristics of these processes are their stationarity and independence properties, so they were known as *processes with stationary and independent increments*. In other words, a stochastic process X is a Lévy process if for n non-negatives numbers, $0\leq t_{1}\leq \dots \leq t_{n}$ , the corresponding $n-1$ increments

$X_{t_{2}}-X_{t_{1}},\dots ,X_{t_{n}}-X_{t_{n-1}},$

are all independent of each other, and the distribution of each increment only depends on the difference in time.

A Lévy process can be defined such that its state space is some abstract mathematical space, such as a Banach space, but the processes are often defined so that they take values in Euclidean space. The index set is the non-negative numbers, so $I=[0,\infty )$ , which gives the interpretation of time. Important stochastic processes such as the Wiener process, the homogeneous Poisson process (in one dimension), and subordinators are all Lévy processes.

### Random field

A random field is a collection of random variables indexed by a n -dimensional Euclidean space or some manifold. In general, a random field can be considered an example of a stochastic or random process, where the index set is not necessarily a subset of the real line. But there is a convention that an indexed collection of random variables is called a random field when the index has two or more dimensions. If the specific definition of a stochastic process requires the index set to be a subset of the real line, then the random field can be considered as a generalization of stochastic process.

### Point process

A point process is a collection of points randomly located on some mathematical space such as the real line, n -dimensional Euclidean space, or more abstract spaces. Sometimes the term *point process* is not preferred, as historically the word *process* denoted an evolution of some system in time, so a point process is also called a **random point field**. There are different interpretations of a point process, such a random counting measure or a random set. Some authors regard a point process and stochastic process as two different objects such that a point process is a random object that arises from or is associated with a stochastic process, though it has been remarked that the difference between point processes and stochastic processes is not clear.

Other authors consider a point process as a stochastic process, where the process is indexed by sets of the underlying space on which it is defined, such as the real line or n -dimensional Euclidean space. Other stochastic processes such as renewal and counting processes are studied in the theory of point processes.
