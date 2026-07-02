---
title: "Markov chain (part 1/2)"
source: https://en.wikipedia.org/wiki/Markov_chain
domain: diffusion-models
license: CC-BY-SA-4.0
tags: diffusion model, denoising diffusion, score based model, generative markov process
fetched: 2026-07-02
part: 1/2
---

# Markov chain

In probability theory and statistics, a **Markov chain** or **Markov process** is a stochastic process describing a sequence of possible events in which the probability of each event depends only on the state attained in the previous event. Informally, this may be thought of as, "What happens next depends only on the state of affairs *now*." A countably infinite sequence, in which the chain moves state at discrete time steps, gives a discrete-time Markov chain (DTMC). A continuous-time process is called a continuous-time Markov chain (CTMC). Markov processes are named in honor of the Russian mathematician Andrey Markov.

Markov chains have many applications as statistical models of real-world processes. They provide the basis for general stochastic simulation methods known as Markov chain Monte Carlo, which are used for simulating sampling from complex probability distributions, and have found application in areas including Bayesian statistics, biology, chemistry, economics, finance, information theory, physics, signal processing, and speech processing.

The adjectives *Markovian* and *Markov* are used to describe something that is related to a Markov process.


## Principles

### Definition

A Markov process is a stochastic process that satisfies the Markov property (sometimes characterized as "memorylessness"). In simpler terms, it is a process for which predictions can be made regarding future outcomes based solely on its present state and—most importantly—such predictions are just as good as the ones that could be made knowing the process's full history. In other words, conditional on the present state of the system, its future and past states are independent.

A Markov chain is a type of Markov process that has either a discrete state space or a discrete index set (often representing time), but the precise definition of a Markov chain varies. For example, it is common to define a Markov chain as a Markov process in either discrete or continuous time with a countable state space (thus regardless of the nature of time), but it is also common to define a Markov chain as having discrete time in either countable or continuous state space (thus regardless of the state space).

### Types of Markov chains

The system's state space and time parameter index need to be specified. The following table gives an overview of the different instances of Markov processes for different levels of state space generality for both discrete and continuous time:

|   | Countable state space | Continuous or general state space |
|---|---|---|
| Discrete-time | (discrete-time) Markov chain on a countable or finite state space | Markov chain on a measurable state space (for example, Harris chain) |
| Continuous-time | Continuous-time Markov process or Markov jump process | Any continuous stochastic process with the Markov property (for example, the Wiener process) |

Note that there is no definitive agreement in the literature on the use of some of the terms that signify special cases of Markov processes. Usually the term "Markov chain" is reserved for a process with a discrete set of times, that is, a **discrete-time Markov chain (DTMC)**, but a few authors use the term "Markov process" to refer to a **continuous-time Markov chain (CTMC)** without explicit mention. In addition, there are other extensions of Markov processes that are referred to as such but do not necessarily fall within any of these four categories (see Markov model). Moreover, the time index need not necessarily be real-valued; like with the state space, there are conceivable processes that move through index sets with other mathematical constructs. Notice that the general state space continuous-time Markov chain is general to such a degree that it has no designated term.

While the time parameter is usually discrete, the state space of a Markov chain does not have any generally agreed-on restrictions: the term may refer to a process on an arbitrary state space. However, many applications of Markov chains employ finite or countably infinite state spaces, which have a more straightforward statistical analysis. Besides time-index and state-space parameters, there are many other variations, extensions and generalizations (see Variations). For simplicity, most of this article concentrates on the discrete-time, discrete state-space case, unless mentioned otherwise.

### Transitions

The changes of state of the system are called transitions. The probabilities associated with various state changes are called transition probabilities. The process is characterized by a state space, a transition matrix describing the probabilities of particular transitions, and an initial state (or initial distribution) across the state space. By convention, we assume all possible states and transitions have been included in the definition of the process, so there is always a next state, and the process does not terminate.

A discrete-time random process involves a system which is in a certain state at each step, with the state changing randomly between steps. The steps are often thought of as moments in time, but they can equally well refer to physical distance or any other discrete measurement. Formally, the steps are the integers or natural numbers, and the random process is a mapping of these to states. The Markov property states that the conditional probability distribution for the system at the next step (and in fact at all future steps) depends only on the current state of the system, and not additionally on the state of the system at previous steps.

Since the system changes randomly, it is generally impossible to predict with certainty the state of a Markov chain at a given point in the future. However, the statistical properties of the system's future can be predicted. In many applications, it is these statistical properties that are important.


## History

Andrey Markov studied Markov processes in the early 20th century, publishing his first paper on the topic in 1906. Markov processes in continuous time were discovered long before his work in the early 20th century in the form of the Poisson process. Markov was interested in studying an extension of independent random sequences, motivated by a disagreement with Pavel Nekrasov who claimed independence was necessary for the weak law of large numbers to hold. In his first paper on Markov chains, published in 1906, Markov showed that under certain conditions the average outcomes of the Markov chain would converge to a fixed vector of values, so proving a weak law of large numbers without the independence assumption, which had been commonly regarded as a requirement for such mathematical laws to hold. Markov later used Markov chains to study the distribution of vowels in Eugene Onegin, written by Alexander Pushkin, and proved a central limit theorem for such chains.

In 1912 Henri Poincaré studied Markov chains on finite groups with an aim to study card shuffling. Other early uses of Markov chains include a diffusion model, introduced by Paul and Tatyana Ehrenfest in 1907, and a branching process, introduced by Francis Galton and Henry William Watson in 1873, preceding the work of Markov. After the work of Galton and Watson, it was later revealed that their branching process had been independently discovered and studied around three decades earlier by Irénée-Jules Bienaymé. Starting in 1928, Maurice Fréchet became interested in Markov chains, eventually resulting in him publishing in 1938 a detailed study on Markov chains.

Andrey Kolmogorov developed in a 1931 paper a large part of the early theory of continuous-time Markov processes. Kolmogorov was partly inspired by Louis Bachelier's 1900 work on fluctuations in the stock market as well as Norbert Wiener's work on Einstein's model of Brownian movement. He introduced and studied a particular set of Markov processes known as diffusion processes, where he derived a set of differential equations describing the processes. Independent of Kolmogorov's work, Sydney Chapman derived in a 1928 paper an equation, now called the Chapman–Kolmogorov equation, in a less mathematically rigorous way than Kolmogorov, while studying Brownian movement. The differential equations are now called the Kolmogorov equations or the Kolmogorov–Chapman equations. Other mathematicians who contributed significantly to the foundations of Markov processes include William Feller, starting in 1930s, and then later Eugene Dynkin, starting in the 1950s.


## Examples

- Mark V. Shaney is a third-order Markov chain program, and a Markov text generator. It ingests the sample text (the Tao Te Ching, or the posts of a Usenet group) and creates a massive list of every sequence of three successive words (triplet) which occurs in the text. It then chooses two words at random, and looks for a word which follows those two in one of the triplets in its massive list. If there is more than one, it picks at random (identical triplets count separately, so a sequence which occurs twice is twice as likely to be picked as one which only occurs once). It then adds that word to the generated text. Then, in the same way, it picks a triplet that starts with the second and third words in the generated text, and that gives a fourth word. It adds the fourth word, then repeats with the third and fourth words, and so on.

- Random walks based on integers and the gambler's ruin problem are examples of Markov processes. Some variations of these processes were studied hundreds of years earlier in the context of independent variables. Two important examples of Markov processes are the Wiener process, also known as the Brownian motion process, and the Poisson process, which are considered the most important and central stochastic processes in the theory of stochastic processes. These two processes are Markov processes in continuous time, while random walks on the integers and the gambler's ruin problem are examples of Markov processes in discrete time.
- A famous Markov chain is the so-called "drunkard's walk", a random walk on the number line where, at each step, the position may change by +1 or −1 with equal probability. From any position there are two possible transitions, to the next or previous integer. The transition probabilities depend only on the current position, not on the manner in which the position was reached. For example, the transition probabilities from 5 to 4 and 5 to 6 are both 0.5, and all other transition probabilities from 5 are 0. These probabilities are independent of whether the system was previously in 4 or 6.
- A series of independent states (for example, a series of coin flips) satisfies the formal definition of a Markov chain. However, the theory is usually applied only when the probability distribution of the next state depends on the current one.

### A non-Markov example

Suppose that there is a coin purse containing five coins worth 25¢ (quarters), five coins worth 10¢ (dimes) and five coins worth 5¢ (nickels). One by one, coins are randomly drawn from the purse and are set on a table. If $X_{n}$ represents the total value of the coins set on the table after n draws, with $X_{0}=0$ , then the sequence $\{X_{n}:n\in \mathbb {N} \}$ is *not* a Markov process.

To see why this is the case, suppose that in the first six draws, all five nickels and a quarter are drawn. Thus $X_{6}=\$0.50$ . If we know not just $X_{6}$ , but the earlier values as well, then we can determine which coins have been drawn, and we know that the next coin will not be a nickel; so we can determine that $X_{7}\geq \$0.60$ with probability 1. But if we do not know the earlier values, then based only on the value $X_{6}$ we might guess that we had drawn four dimes and two nickels, in which case it would certainly be possible to draw another nickel next. Thus, our guesses about $X_{7}$ are impacted by our knowledge of values prior to $X_{6}$ .

However, it is possible to model this scenario as a Markov process. Instead of defining $X_{n}$ to represent the *total value* of the coins on the table, we could define $X_{n}$ to represent the *count* of the various coin types on the table. For instance, $X_{6}=1,0,5$ could be defined to represent the state where there is one quarter, zero dimes, and five nickels on the table after 6 one-by-one draws. This new model could be represented by $6\times 6\times 6=216$ possible states, where each state represents the number of coins of each type (from 0 to 5) that are on the table. (Not all of these states are reachable within 6 draws.)

Suppose that the first draw results in state $X_{1}=0,1,0$ . The probability of achieving $X_{2}$ now depends on $X_{1}$ ; for example, the state $X_{2}=1,0,1$ is not possible. After the second draw, the third draw depends on which coins have so far been drawn, but no longer only on the coins that were drawn for the first state (since probabilistically important information has since been added to the scenario). In this way, the likelihood of the $X_{n}=i,j,k$ state depends exclusively on the outcome of the $X_{n-1}=\ell ,m,p$ state.


## Formal definition

### Discrete-time Markov chain

A discrete-time Markov chain is a sequence of random variables *X*1, *X*2, *X*3, ... with the Markov property, namely that the probability of moving to the next state depends only on the present state and not on the previous states:

$\Pr(X_{n+1}=x\mid X_{1}=x_{1},X_{2}=x_{2},\ldots ,X_{n}=x_{n})=\Pr(X_{n+1}=x\mid X_{n}=x_{n}),$

if both

conditional probabilities

are well defined, that is, if

$\Pr(X_{1}=x_{1},\ldots ,X_{n}=x_{n})>0.$

The possible values of *X**i* form a countable set *S* called the state space of the chain.

#### Variations

- Time-homogeneous Markov chains are processes where $\Pr(X_{n+1}=x\mid X_{n}=y)=\Pr(X_{n}=x\mid X_{n-1}=y)$ for all *n*. The probability of the transition is independent of *n*.
- Stationary Markov chains are processes where $\Pr(X_{0}=x_{0},X_{1}=x_{1},\ldots ,X_{k}=x_{k})=\Pr(X_{n}=x_{0},X_{n+1}=x_{1},\ldots ,X_{n+k}=x_{k})$ for all *n* and *k*. Every stationary chain can be proved to be time-homogeneous by Bayes' rule.A necessary and sufficient condition for a time-homogeneous Markov chain to be stationary is that the distribution of $X_{0}$ is a stationary distribution of the Markov chain.
- A Markov chain with memory (or a Markov chain of order *m*) where *m* is finite, is a process satisfying ${\begin{aligned}{}&\Pr(X_{n}=x_{n}\mid X_{n-1}=x_{n-1},X_{n-2}=x_{n-2},\dots ,X_{1}=x_{1})\\=&\Pr(X_{n}=x_{n}\mid X_{n-1}=x_{n-1},X_{n-2}=x_{n-2},\dots ,X_{n-m}=x_{n-m}){\text{ for }}n>m\end{aligned}}$ In other words, the future state depends on the past *m* states. It is possible to construct a chain $(Y_{n})$ from $(X_{n})$ which has the 'classical' Markov property by taking as state space the ordered *m*-tuples of *X* values, i.e., $Y_{n}=\left(X_{n},X_{n-1},\ldots ,X_{n-m+1}\right)$ .

### Finite state space

If the state space is finite, the transition probability distribution can be represented by a matrix, called the transition matrix, with the (*i*, *j*)th element of **P** equal to

$p_{ij}=\Pr(X_{n+1}=j\mid X_{n}=i).$

Since each row of **P** sums to one and all elements are non-negative, **P** is a right stochastic matrix.

#### Stationary distribution relation to eigenvectors and simplices

A stationary distribution π is a (row) vector, whose entries are non-negative and sum to 1, is unchanged by the operation of transition matrix **P** on it and so is defined by

$\pi \mathbf {P} =\pi .$

By comparing this definition with that of an eigenvector we see that the two concepts are related and that

$\pi ={\frac {e}{\sum _{i}{e_{i}}}}$

is a normalized ( ${\textstyle \sum _{i}\pi _{i}=1}$ ) multiple of a left eigenvector **e** of the transition matrix **P** with an eigenvalue of 1. If there is more than one unit eigenvector then a weighted sum of the corresponding stationary states is also a stationary state. But for a Markov chain one is usually more interested in a stationary state that is the limit of the sequence of distributions for some initial distribution.

The values of a stationary distribution $\textstyle \pi _{i}$ are associated with the state space of **P** and its eigenvectors have their relative proportions preserved. Since the components of π are positive and the constraint that their sum is unity can be rewritten as ${\textstyle \sum _{i}1\cdot \pi _{i}=1}$ we see that the dot product of π with a vector whose components are all 1 is unity and that π lies on a simplex.

#### Time-homogeneous Markov chain with a finite state space

If the Markov chain is time-homogeneous, then the transition matrix **P** is the same after each step, so the *k*-step transition probability can be computed as the *k*-th power of the transition matrix, **P***k*.

If the Markov chain is irreducible and aperiodic, then there is a unique stationary distribution π. Additionally, in this case **P***k* converges to a rank-one matrix in which each row is the stationary distribution π:

$\lim _{k\to \infty }\mathbf {P} ^{k}=\mathbf {1} \pi$

where **1** is the column vector with all entries equal to 1. This is stated by the Perron–Frobenius theorem. If, by whatever means, ${\textstyle \lim _{k\to \infty }\mathbf {P} ^{k}}$ is found, then the stationary distribution of the Markov chain in question can be easily determined for any starting distribution, as will be explained below.

For some stochastic matrices **P**, the limit ${\textstyle \lim _{k\to \infty }\mathbf {P} ^{k}}$ does not exist while the stationary distribution does, as shown by this example:

$\mathbf {P} ={\begin{pmatrix}0&1\\1&0\end{pmatrix}}\qquad \mathbf {P} ^{2k}=I\qquad \mathbf {P} ^{2k+1}=\mathbf {P}$

${\begin{pmatrix}{\frac {1}{2}}&{\frac {1}{2}}\end{pmatrix}}{\begin{pmatrix}0&1\\1&0\end{pmatrix}}={\begin{pmatrix}{\frac {1}{2}}&{\frac {1}{2}}\end{pmatrix}}$

(This example illustrates a periodic Markov chain.)

Because there are a number of different special cases to consider, the process of finding this limit if it exists can be a lengthy task. However, there are many techniques that can assist in finding this limit. Let **P** be an *n*×*n* matrix, and define ${\textstyle \mathbf {Q} =\lim _{k\to \infty }\mathbf {P} ^{k}.}$

It is always true that

$\mathbf {QP} =\mathbf {Q} .$

Subtracting **Q** from both sides and factoring then yields

$\mathbf {Q} (\mathbf {P} -\mathbf {I} _{n})=\mathbf {0} _{n,n},$

where **I***n* is the identity matrix of size *n*, and **0***n*,*n* is the zero matrix of size *n*×*n*. Multiplying together stochastic matrices always yields another stochastic matrix, so **Q** must be a stochastic matrix (see the definition above). It is sometimes sufficient to use the matrix equation above and the fact that **Q** is a stochastic matrix to solve for **Q**. Including the fact that the sum of each the rows in **P** is 1, there are *n+1* equations for determining *n* unknowns, so it is computationally easier if on the one hand one selects one row in **Q** and substitutes each of its elements by one, and on the other one substitutes the corresponding element (the one in the same column) in the vector **0**, and next left-multiplies this latter vector by the inverse of transformed former matrix to find **Q**.

Here is one method for doing so: first, define the function *f*(**A**) to return the matrix **A** with its right-most column replaced with all 1's. If [*f*(**P** − **I***n*)]−1 exists then

$\mathbf {Q} =f(\mathbf {0} _{n,n})[f(\mathbf {P} -\mathbf {I} _{n})]^{-1}.$

Explain: The original matrix equation is equivalent to a

system of n×n linear equations

in

n

×

n

variables. And there are

n

more linear equations from the fact that

Q

is a right

stochastic matrix

whose each row sums to 1. So it needs any

n

×

n

independent linear equations of the (

n

×

n

+

n

) equations to solve for the

n

×

n

variables. In this example, the

n

equations from "

Q

multiplied by the right-most column of (

P

-

I

n

)" have been replaced by the

n

stochastic ones.

One thing to notice is that if **P** has an element **P***i*,*i* on its main diagonal that is equal to 1 and the *i*th row or column is otherwise filled with 0's, then that row or column will remain unchanged in all of the subsequent powers **P***k*. Hence, the *i*th row or column of **Q** will have the 1 and the 0's in the same positions as in **P**.

#### Convergence speed to the stationary distribution

As stated earlier, from the equation ${\boldsymbol {\pi }}={\boldsymbol {\pi }}\mathbf {P} ,$ (if exists) the stationary (or steady state) distribution **π** is a left eigenvector of row stochastic matrix **P**. Then assuming that **P** is diagonalizable or equivalently that **P** has *n* linearly independent eigenvectors, speed of convergence is elaborated as follows. (For non-diagonalizable, that is, defective matrices, one may start with the Jordan normal form of **P** and proceed with a bit more involved set of arguments in a similar way.)

Let **U** be the matrix of eigenvectors (each normalized to having an L2 norm equal to 1) where each column is a left eigenvector of **P** and let **Σ** be the diagonal matrix of left eigenvalues of **P**, that is, **Σ** = diag(*λ*1,*λ*2,*λ*3,...,*λ**n*). Then by eigendecomposition

$\mathbf {P} =\mathbf {U\Sigma U} ^{-1}.$

Let the eigenvalues be enumerated such that:

$1=|\lambda _{1}|>|\lambda _{2}|\geq |\lambda _{3}|\geq \cdots \geq |\lambda _{n}|.$

Since **P** is a row stochastic matrix, its largest left eigenvalue is 1. If there is a unique stationary distribution, then the largest eigenvalue and the corresponding eigenvector is unique too (because there is no other **π** which solves the stationary distribution equation above). Let **u***i* be the *i*-th column of **U** matrix, that is, **u***i* is the left eigenvector of **P** corresponding to λ*i*. Also let **x** be a length *n* row vector that represents a valid probability distribution; since the eigenvectors **u***i* span $\mathbb {R} ^{n},$ we can write

$\mathbf {x} ^{\mathsf {T}}=\sum _{i=1}^{n}a_{i}\mathbf {u} _{i},\qquad a_{i}\in \mathbb {R} .$

If we multiply **x** with **P** from right and continue this operation with the results, in the end we get the stationary distribution **π**. In other words, **π** = **a**1 **u**1 ← **xPP**...**P** = **xP***k* as *k* → ∞. That means

${\begin{aligned}{\boldsymbol {\pi }}^{(k)}&=\mathbf {x} \left(\mathbf {U\Sigma U} ^{-1}\right)\left(\mathbf {U\Sigma U} ^{-1}\right)\cdots \left(\mathbf {U\Sigma U} ^{-1}\right)\\&=\mathbf {xU\Sigma } ^{k}\mathbf {U} ^{-1}\\&=\left(a_{1}\mathbf {u} _{1}^{\mathsf {T}}+a_{2}\mathbf {u} _{2}^{\mathsf {T}}+\cdots +a_{n}\mathbf {u} _{n}^{\mathsf {T}}\right)\mathbf {U\Sigma } ^{k}\mathbf {U} ^{-1}\\&=a_{1}\lambda _{1}^{k}\mathbf {u} _{1}^{\mathsf {T}}+a_{2}\lambda _{2}^{k}\mathbf {u} _{2}^{\mathsf {T}}+\cdots +a_{n}\lambda _{n}^{k}\mathbf {u} _{n}^{\mathsf {T}}&&u_{i}\bot u_{j}{\text{ for }}i\neq j\\&=\lambda _{1}^{k}\left\{a_{1}\mathbf {u} _{1}^{\mathsf {T}}+a_{2}\left({\frac {\lambda _{2}}{\lambda _{1}}}\right)^{k}\mathbf {u} _{2}^{\mathsf {T}}+a_{3}\left({\frac {\lambda _{3}}{\lambda _{1}}}\right)^{k}\mathbf {u} _{3}^{\mathsf {T}}+\cdots +a_{n}\left({\frac {\lambda _{n}}{\lambda _{1}}}\right)^{k}\mathbf {u} _{n}^{\mathsf {T}}\right\}\end{aligned}}$

Since **π** is parallel to **u**1(normalized by L2 norm) and **π**(*k*) is a probability vector, **π**(*k*) approaches to **a**1 **u**1 = **π** as *k* → ∞ with a speed in the order of *λ*2/*λ*1 exponentially. This follows because $|\lambda _{2}|\geq \cdots \geq |\lambda _{n}|,$ hence *λ*2/*λ*1 is the dominant term. The smaller the ratio is, the faster the convergence is. Random noise in the state distribution **π** can also speed up this convergence to the stationary distribution.

### Continuous-time Markov chain

A continuous-time Markov chain $(X_{t})_{t\geq 0}$ is defined by a finite or countable state space *S*, a transition rate matrix *Q* with dimensions equal to that of the state space and initial probability distribution defined on the state space. For *i* ≠ *j*, the elements *q**ij* are non-negative and describe the rate of the process transitions from state *i* to state *j*. The elements *q**ii* are chosen such that each row of the transition rate matrix sums to zero, while the row-sums of a probability transition matrix in a (discrete) Markov chain are all equal to one.

There are three equivalent definitions of the process.

#### Infinitesimal definition

Let $X_{t}$ be the random variable describing the state of the process at time *t*, and assume the process is in a state *i* at time *t*. Then, knowing $X_{t}=i$ , $X_{t+h}=j$ is independent of previous values $\left(X_{s}:s<t\right)$ , and as *h* → 0 for all *j* and for all *t*, $\Pr(X(t+h)=j\mid X(t)=i)=\delta _{ij}+q_{ij}h+o(h),$ where $\delta _{ij}$ is the Kronecker delta, using the little-o notation. The $q_{ij}$ can be seen as measuring how quickly the transition from *i* to *j* happens.

#### Jump chain/holding time definition

Define a discrete-time Markov chain *Y**n* to describe the *n*th jump of the process and variables *S*1, *S*2, *S*3, ... to describe holding times in each of the states where *S**i* follows the exponential distribution with rate parameter −*q**Y**i**Y**i*.

#### Transition probability definition

For any value *n* = 0, 1, 2, 3, ... and times indexed up to this value of *n*: *t*0, *t*1, *t*2, ... and all states recorded at these times *i*0, *i*1, *i*2, *i*3, ... it holds that

$\Pr(X_{t_{n+1}}=i_{n+1}\mid X_{t_{0}}=i_{0},X_{t_{1}}=i_{1},\ldots ,X_{t_{n}}=i_{n})=p_{i_{n}i_{n+1}}(t_{n+1}-t_{n})$

where *p**ij* is the solution of the forward equation (a first-order differential equation)

$P'(t)=P(t)Q$

with initial condition P(0) is the identity matrix.

#### Locally interacting Markov chains

"Locally interacting Markov chains" are Markov chains with an evolution that takes into account the state of other Markov chains. This corresponds to the situation when the state space has a (Cartesian-) product form. See interacting particle system and stochastic cellular automata (probabilistic cellular automata). See for instance *Interaction of Markov Processes* or.

### Discrete-time Markov process with general state space

#### Harris chains

Many results for discrete-time Markov chains with finite state space can be generalized to chains with uncountable state space through Harris chains.

The use of Markov chains in Markov chain Monte Carlo methods covers cases where the process follows a continuous state space.

### Continuous-time Markov process with general state space

The definition of Markov processes in continuous time with general state space is more technical than the above.

A continuous-time Markov process $X=(X_{t})_{t\geq 0}$ is a stochastic process adapted to a filtration $\mathbb {F} =({\mathcal {F}}_{t})_{t\geq 0}$ with values in a locally compact Polish space $(S,{\mathcal {B}}(S))$ (e.g., $(\mathbb {R} ,{\mathcal {B}}(\mathbb {R} ))$ ). The latter essentially ensures that the conditional expectations of $X_{t}$ are regular, which, in simple terms, means that they behave "nicely". Then X is called a *Markov process*, if it satisfies the Markov property, i.e., for all $t\geq s\geq 0$ and $A\in {\mathcal {B}}(S)$

$P(X_{t}\in A\mid {\mathcal {F}}_{s})=P(X_{t}\in A\mid X_{s})$

.

Moreover, X is called *time-homogeneous*, if it satisfies the weak Markov property for all $t,s\geq 0$ :

$P(X_{t+s}\in A\mid {\mathcal {F}}_{s})=P(X_{t}\in A\mid X_{0}=x)|_{x=X_{s}}=:P_{t}(X_{s},A)$

.

The function $(t,x,A)\mapsto P_{t}(x,A)$ is the so-called *transition function* of X and $(P_{t})_{t\geq 0}$ the *transition semigroup* of the process. Transition functions are generalizations of the transition matrices used in the setting with finite state space.

In a more abstract way, Markov processes can also be defined or constructed the other way around: Let $(P_{t})_{t\geq 0}$ be a transition semigroup, i.e.,

1. $P_{t}$ is Markov kernel for all $t\geq 0$ ,
2. $P_{t+s}(x,A)=\int _{S}P_{t}(y,A)P_{s}(x,dy)\quad \forall t,s\geq 0,x\in \mathbb {R} ,A\in {\mathcal {B}}(S)$ (Chapman-Kolmogorov-equation),
3. $P_{0}(x,\cdot )=\delta _{x}$ ,

where $\delta _{x}$ is the Dirac-measure in x , and $X:\Omega \times [0,\infty )\to S$ . Then X is a homogeneous Markov process w.r.t. the natural filtration $\mathbb {F} ^{X}=(\sigma (X_{s}:0\leq s\leq t))_{t\geq 0}$ , if for all $0\leq t_{1}<...<t_{n}$ , $A_{1},...,A_{n}\in {\mathcal {B}}(S)$ the underlying probability measure P satisfies

$P(X_{t_{1}}\in A_{1},...,X_{t_{n}}\in A_{n}\mid X_{0}=x)=\int _{A_{1}}...\int _{A_{n-1}}P_{t_{n}-t_{n-1}}(x_{n-1},A_{n})\cdots P_{t_{1}}(x,dx_{1})$

.

Or, if no probability measure P has been specified, the above equation defines a measure $P^{x}:=P(\cdot \mid X_{0}=x)$ on $\sigma (X_{s}:s\geq 0)$ under which the process X started in x is a Markov process by construction.

In other words, Markov processes can be defined either as stochastic processes X on a filtered probability space, or indirectly in terms of a transition semigroup (i.e., the transition probabilities of the process), which induces a probability space under which X has the Markov property.


## Properties

Two states are said to *communicate* with each other if both are reachable from one another by a sequence of transitions that have positive probability. This is an equivalence relation which yields a set of communicating classes. A class is *closed* if the probability of leaving the class is zero. A Markov chain is *irreducible* if there is one communicating class, the state space.

A state *i* has period *k* if *k* is the greatest common divisor of the number of transitions by which *i* can be reached, starting from *i*. That is:

$k=\gcd\{n>0:\Pr(X_{n}=i\mid X_{0}=i)>0\}$

The state is *periodic* if $k>1$ ; otherwise $k=1$ and the state is *aperiodic*.

A state *i* is said to be *transient* if, starting from *i*, there is a non-zero probability that the chain will never return to *i*. It is called *recurrent* (or *persistent*) otherwise. For a recurrent state *i*, the mean *hitting time* is defined as:

$M_{i}=E[T_{i}]=\sum _{n=1}^{\infty }n\cdot f_{ii}^{(n)}$

where

$f_{ii}^{(n)}:=\Pr(\min\{m>0:X_{m}=i\}=n\mid X_{0}=i)$

.

State *i* is *positive recurrent* if $M_{i}$ is finite and *null recurrent* otherwise. Periodicity, transience, recurrence and positive and null recurrence are class properties — that is, if one state has the property then all states in its communicating class have the property.

A state *i* is called *absorbing* if there are no outgoing transitions from the state.

### Irreducibility

Since periodicity is a class property, if a Markov chain is irreducible, then all its states have the same period. In particular, if one state is aperiodic, then the whole Markov chain is aperiodic.

If a finite Markov chain is irreducible, then all states are positive recurrent, and it has a unique stationary distribution given by $\pi _{i}=1/E[T_{i}]$ .

### Ergodicity

A state *i* is said to be *ergodic* if it is aperiodic and positive recurrent. In other words, a state *i* is ergodic if it is recurrent, has a period of 1, and has finite mean recurrence time.

If all states in an irreducible Markov chain are ergodic, then the chain is said to be ergodic. Equivalently, there exists some integer k such that all entries of $M^{k}$ are positive.

It can be shown that a finite state irreducible Markov chain is ergodic if it has an aperiodic state.

A Markov chain with more than one state and just one out-going transition per state is either not irreducible or not aperiodic, hence cannot be ergodic.

#### Terminology

Some authors call any irreducible, positive recurrent Markov chains ergodic, even periodic ones. In fact, merely irreducible Markov chains correspond to ergodic processes, defined according to ergodic theory.

Some authors call a matrix *primitive* if there exists some integer k such that all entries of $M^{k}$ are positive. Some authors call it *regular*.

#### Index of primitivity

The *index of primitivity*, or *exponent*, of a regular matrix, is the smallest k such that all entries of $M^{k}$ are positive. The exponent is purely a graph-theoretic property, since it depends only on whether each entry of M is zero or positive, and therefore can be found on a directed graph with $\mathrm {sign} (M)$ as its adjacency matrix.

There are several combinatorial results about the exponent when there are finitely many states. Let n be the number of states, then

- The exponent is $\leq (n-1)^{2}+1$ . The only case where it is an equality is when the graph of M goes like $1\to 2\to \dots \to n\to 1{\text{ and }}2$ .
- If M has $k\geq 1$ diagonal entries, then its exponent is $\leq 2n-k-1$ .
- If $\mathrm {sign} (M)$ is symmetric, then $M^{2}$ has positive diagonal entries, which by previous proposition means its exponent is $\leq 2n-2$ .
- (Dulmage-Mendelsohn theorem) The exponent is $\leq n+s(n-2)$ where s is the girth of the graph. It can be improved to $\leq (d+1)+s(d+1-2)$ , where d is the diameter of the graph.

### Measure-preserving dynamical system

If a Markov chain has a stationary distribution, then it can be converted to a measure-preserving dynamical system: Let the probability space be $\Omega =\Sigma ^{\mathbb {N} }$ , where $\Sigma$ is the set of all states for the Markov chain. Let the sigma-algebra on the probability space be generated by the cylinder sets. Let the probability measure be generated by the stationary distribution, and the Markov chain transition. Let $T:\Omega \to \Omega$ be the shift operator: $T(X_{0},X_{1},\dots )=(X_{1},\dots )$ . Similarly we can construct such a dynamical system with $\Omega =\Sigma ^{\mathbb {Z} }$ instead.

Since *irreducible* Markov chains with finite state spaces have a unique stationary distribution, the above construction is unambiguous for irreducible Markov chains.

In ergodic theory, a measure-preserving dynamical system is called *ergodic* if any measurable subset S such that $T^{-1}(S)=S$ implies $S=\emptyset$ or $\Omega$ (up to a null set).

The terminology is inconsistent. Given a Markov chain with a stationary distribution that is strictly positive on all states, the Markov chain is *irreducible* if its corresponding measure-preserving dynamical system is *ergodic*.

### Markovian representations

In some cases, apparently non-Markovian processes may still have Markovian representations, constructed by expanding the concept of the "current" and "future" states. For example, let *X* be a non-Markovian process. Then define a process *Y*, such that each state of *Y* represents a time-interval of states of *X*. Mathematically, this takes the form:

$Y(t)={\big \{}X(s):s\in [a(t),b(t)]\,{\big \}}.$

If *Y* has the Markov property, then it is a Markovian representation of *X*.

An example of a non-Markovian process with a Markovian representation is an autoregressive time series of order greater than one.

### Hitting times

The *hitting time* is the time, starting in a given set of states, until the chain arrives in a given state or set of states. The distribution of such a time period has a phase type distribution. The simplest such distribution is that of a single exponentially distributed transition.

#### Expected hitting times

For a subset of states *A* ⊆ *S*, the vector *k**A* of hitting times (where element $k_{i}^{A}$ represents the expected value, starting in state *i* that the chain enters one of the states in the set *A*) is the minimal non-negative solution to

${\begin{aligned}k_{i}^{A}=0&{\text{ for }}i\in A\\-\sum _{j\in S}q_{ij}k_{j}^{A}=1&{\text{ for }}i\notin A.\end{aligned}}$

### Time reversal

For a general Markov process X in continuous time (a CTMC or a process with general state space), the reverse process ${\overleftarrow {X}}=(X_{T-t})_{t\in [0,T]}$ from a fixed time $T>0$ is again a Markov process. This follows directly from the Markov property: Informally speaking, the future and the past are independent given the present. Under time-reversal, their roles are just interchanged. However, the reverse process is not time-homogeneous in general. If for some random time $\tau$ (not necessarily a stopping time) the stopped process $X^{\tau }=(X_{t\land \tau })_{t\geq 0}$ is a time-homogeneous Markov process, then the reverse process ${\overleftarrow {X^{\tau }}}=(X_{\tau -t\land \tau }1_{\{\tau <\infty \}})_{t\geq 0}$ is again time-homogeneous.

If X is a CTMC, then by Kelly's lemma ${\overleftarrow {X}}$ has the same stationary distribution as the forward process.

A chain is said to be *reversible* if the reversed process is the same as the forward process (in distribution). Kolmogorov's criterion states that the necessary and sufficient condition for a Markov chain to be reversible is that the product of transition rates around a closed loop must be the same in both directions.

### Embedded Markov chain

One method of finding the stationary probability distribution, π, of an ergodic continuous-time Markov chain, *Q*, is by first finding its **embedded Markov chain (EMC)**. Strictly speaking, the EMC is a regular discrete-time Markov chain, sometimes referred to as a **jump process**. Each element of the one-step transition probability matrix of the EMC, *S*, is denoted by *s**ij*, and represents the conditional probability of transitioning from state *i* into state *j*. These conditional probabilities may be found by

$s_{ij}={\begin{cases}{\frac {q_{ij}}{\sum _{k\neq i}q_{ik}}}&{\text{if }}i\neq j\\0&{\text{otherwise}}.\end{cases}}$

From this, *S* may be written as

$S=I-\left(\operatorname {diag} (Q)\right)^{-1}Q$

where *I* is the identity matrix and diag(*Q*) is the diagonal matrix formed by selecting the main diagonal from the matrix *Q* and setting all other elements to zero.

To find the stationary probability distribution vector, we must next find $\varphi$ such that

$\varphi S=\varphi ,$

with $\varphi$ being a row vector, such that all elements in $\varphi$ are greater than 0 and $\|\varphi \|_{1}$ = 1. From this, π may be found as

$\pi ={-\varphi (\operatorname {diag} (Q))^{-1} \over \left\|\varphi (\operatorname {diag} (Q))^{-1}\right\|_{1}}.$

(*S* may be periodic, even if *Q* is not. Once π is found, it must be normalized to a unit vector.)

Another discrete-time process that may be derived from a continuous-time Markov chain is a δ-skeleton—the (discrete-time) Markov chain formed by observing *X*(*t*) at intervals of δ units of time. The random variables *X*(0), *X*(δ), *X*(2δ), ... give the sequence of states visited by the δ-skeleton.


## Special types of Markov chains

### Markov model

Markov models are used to model changing systems. There are 4 main types of models, that generalize Markov chains depending on whether every sequential state is observable or not, and whether the system is to be adjusted on the basis of observations made:

|   | System state is fully observable | System state is partially observable |
|---|---|---|
| System is autonomous | Markov chain | Hidden Markov model |
| System is controlled | Markov decision process | Partially observable Markov decision process |

### Bernoulli scheme

A Bernoulli scheme is a special case of a Markov chain where the transition probability matrix has identical rows, which means that the next state is independent of even the current state (in addition to being independent of the past states). A Bernoulli scheme with only two possible states is known as a Bernoulli process.

Note, however, by the Ornstein isomorphism theorem, that every aperiodic and irreducible Markov chain is isomorphic to a Bernoulli scheme; thus, one might equally claim that Markov chains are a "special case" of Bernoulli schemes. The isomorphism generally requires a complicated recoding. The isomorphism theorem is even a bit stronger: it states that *any* stationary stochastic process is isomorphic to a Bernoulli scheme; the Markov chain is just one such example.

### Subshift of finite type

When the Markov matrix is replaced by the adjacency matrix of a finite graph, the resulting shift is termed a **topological Markov chain** or a **subshift of finite type**. A Markov matrix that is compatible with the adjacency matrix can then provide a measure on the subshift. Many chaotic dynamical systems are isomorphic to topological Markov chains; examples include diffeomorphisms of closed manifolds, the Prouhet–Thue–Morse system, the Chacon system, sofic systems, context-free systems and block-coding systems.
