---
title: "Martingale (probability theory)"
source: https://en.wikipedia.org/wiki/Submartingale
domain: martingale-theory
license: CC-BY-SA-4.0
tags: martingale theory, stopping time, conditional expectation, optional stopping theorem
fetched: 2026-07-02
---

# Martingale (probability theory)

(Redirected from

Submartingale

)

In probability theory, a **martingale** is a stochastic process in which the expected value of the next observation, given all prior observations, is equal to the most recent value. In other words, the conditional expectation of the next value, given the past, is equal to the present value. Martingales are used to model fair games, where future expected winnings are equal to the current amount regardless of past outcomes.

## History

Originally, *martingale* referred to a class of betting strategies that was popular in 18th-century France.

The historical development of the concept can be summarized as follows:

- The simplest of these strategies was designed for a game in which the gambler wins their stake if a coin comes up heads and loses it if the coin comes up tails.
- The strategy had the gambler double their bet after every loss so that the first win would recover all previous losses plus win a profit equal to the original stake.
- As the gambler's wealth and available time jointly approach infinity, their probability of eventually flipping heads approaches 1, which makes the martingale betting strategy seem like a sure thing.
- However, the exponential growth of the bets eventually bankrupts its users due to finite bankrolls. Stopped Brownian motion, which is a martingale process, can be used to model the trajectory of such games.
- The concept of the martingale in probability theory was introduced by Paul Lévy in 1934, though he did not formally name it.
- The term "martingale" was introduced later by Ville (1939), who also extended the definition to continuous martingales.
- Much of the original development of the theory was done by Joseph Leo Doob among others. Part of the motivation for that early work was to mathematically prove the impossibility of successful betting strategies in games of chance.

## Definitions

A basic definition of a discrete-time martingale is a discrete-time stochastic process (i.e., a sequence of random variables) $X_{1},X_{2},X_{3},\dots$ that satisfies for any time n :

$\mathbf {E} [\vert X_{n}\vert ]<\infty$

$\mathbf {E} [X_{n+1}\mid X_{1},\ldots ,X_{n}]=X_{n}.$

That is, the conditional expected value of the next observation, given all the past observations, is equal to the most recent observation.

### Martingale sequences with respect to another sequence

More generally, a sequence $Y_{1},Y_{2},Y_{3},\dots$ is said to be a **martingale with respect to** another sequence $X_{1},X_{2},X_{3},\dots$ if for all n :

$\mathbf {E} [\vert Y_{n}\vert ]<\infty$

$\mathbf {E} [Y_{n+1}\mid X_{1},\ldots ,X_{n}]=Y_{n}.$

Similarly, a **continuous-time martingale with respect to** the stochastic process $X_{t}$ is a stochastic process $Y_{t}$ such that for all t :

$\mathbf {E} [\vert Y_{t}\vert ]<\infty$

$\mathbf {E} [Y_{t}\mid \{X_{\tau },\tau \leq s\}]=Y_{s}\quad \forall s\leq t.$

This expresses the property that the conditional expectation of an observation at time t , given all the observations up to time s , is equal to the observation at time s (provided that $s\leq t$ ). The second property implies that $Y_{n}$ is measurable with respect to $X_{1},\dots ,X_{n}$ .

### General definition

In full generality, a stochastic process $Y:T\times \Omega \to S$ taking values in a Banach space S with norm $\lVert \cdot \rVert _{S}$ is a **martingale with respect to a filtration** $\Sigma _{*}$ **and probability measure** $\mathbb {P}$ if:

- $\Sigma _{*}$ is a filtration of the underlying probability space $(\Omega ,\Sigma ,\mathbb {P} )$ ;
- Y is adapted to the filtration $\Sigma _{*}$ , i.e., for each t in the index set T , the random variable $Y_{t}$ is a $\Sigma _{t}$ -measurable function;
- for each t , $Y_{t}$ lies in the *Lp* space $L^{1}(\Omega ,\Sigma _{t},\mathbb {P} ;S)$ , i.e.,

${\displaystyle \mathbf {E} _{\mathbb {P} }[\lVert Y_{t}\rVert _{S}]<+\infty$

- for all s and t with $s<t$ and all $F\in \Sigma _{s}$ ,

$\mathbf {E} _{\mathbb {P} }\left[(Y_{t}-Y_{s})\chi _{F}\right]=0,$

where

$\chi _{F}$

denotes the

indicator function

of the event

F

. In Grimmett and Stirzaker's

Probability and Random Processes

, this last condition is denoted as:

$Y_{s}=\mathbf {E} _{\mathbb {P} }[Y_{t}\mid \Sigma _{s}],$

which is a general form of

conditional expectation

.

This is also called the martingale property.

The property of being a martingale involves both the filtration *and* the probability measure (with respect to which the expectations are taken). It is possible that Y could be a martingale with respect to one measure but not another one; the Girsanov theorem offers a way to find a measure with respect to which an Itō process is a martingale.

In the Banach space setting the conditional expectation is also denoted in operator notation as $\mathbf {E} ^{\Sigma _{s}}Y_{t}$ .

## Examples of martingales

- An unbiased random walk, in any number of dimensions, is an example of a martingale. For example, consider a 1-dimensional random walk where at each time step a move to the right or left is equally likely.
- A gambler's fortune (capital) is a martingale if all the betting games which the gambler plays are fair. Suppose $X_{n}$ is the gambler's fortune after n tosses of a fair coin, such that the gambler wins $1 if the coin toss outcome is heads and loses $1 if the outcome is tails. The gambler's conditional expected fortune after the next game, given the history, is equal to his present fortune.
- Let $Y_{n}=X_{n}^{2}-n$ where $X_{n}$ is the gambler's fortune from the prior example. Then the sequence $\{Y_{n}:n=1,2,3,\dots \}$ is a martingale. This can be used to show that the gambler's total gain or loss varies roughly between plus or minus the square root of the number of games played.
- de Moivre's martingale: Suppose the coin toss outcomes are unfair (biased), with probability p of coming up heads and probability $q=1-p$ of tails. Let

$X_{n+1}=X_{n}\pm 1$

with "+" in case of "heads" and "−" in case of "tails". Let

$Y_{n}=(q/p)^{X_{n}}$

Then

$\{Y_{n}:n=1,2,3,\dots \}$

is a martingale with respect to

$\{X_{n}:n=1,2,3,\dots \}$

. To show this:

${\begin{aligned}\mathbf {E} [Y_{n+1}\mid X_{1},\dots ,X_{n}]&=p(q/p)^{X_{n}+1}+q(q/p)^{X_{n}-1}\\[6pt]&=p(q/p)(q/p)^{X_{n}}+q(p/q)(q/p)^{X_{n}}\\[6pt]&=q(q/p)^{X_{n}}+p(q/p)^{X_{n}}=(q/p)^{X_{n}}=Y_{n}.\end{aligned}}$

- Pólya's urn contains a number of different-coloured marbles; at each iteration a marble is randomly selected from the urn and replaced with several more of that same colour. For any given colour, the fraction of marbles in the urn with that colour is a martingale.
- Likelihood-ratio testing in statistics: A random variable X is thought to be distributed according either to probability density f or to a different probability density g . A random sample $X_{1},\dots ,X_{n}$ is taken. Let $Y_{n}$ be the "likelihood ratio":

$Y_{n}=\prod _{i=1}^{n}{\frac {g(X_{i})}{f(X_{i})}}$

If

X

is actually distributed according to the density

f

rather than

g

, then

$\{Y_{n}\}$

is a martingale with respect to

$\{X_{n}\}$

.

- **Doob martingale:** Let Y be any random variable with a finite expected value, and let $\{{\mathcal {F}}_{n}\}$ be a filtration. The sequence defined by $X_{n}=\mathbf {E} [Y\mid {\mathcal {F}}_{n}]$ is a martingale. This represents the sequentially updated best estimate of Y as more information becomes available.

- In an ecological community, the number of individuals of any particular species of fixed size is a function of time, and may be viewed as a sequence of random variables. This sequence is a martingale under the unified neutral theory of biodiversity and biogeography.
- In population genetics, the frequency of an allele in a population of fixed size evolving under genetic drift (with no mutation or selection) follows a martingale. This is a defining feature of the Wright–Fisher model.
- If $\{N_{t}:t\geq 0\}$ is a Poisson process with intensity $\lambda$ , then the compensated Poisson process $\{N_{t}-\lambda t:t\geq 0\}$ is a continuous-time martingale with right-continuous/left-limit sample paths.
- **Exponential martingale:** If $W_{t}$ is a standard one-dimensional Brownian motion, then the process $Z_{t}=\exp \left(\theta W_{t}-{\frac {1}{2}}\theta ^{2}t\right)$ is a continuous-time martingale for any real parameter $\theta$ . This process plays a critical role in stochastic calculus and the Girsanov theorem for changing probability measures.
- **Wald's martingale:** If $X_{1},X_{2},\dots$ are independent and identically distributed random variables with moment-generating function $M(\theta )=\mathbf {E} [\exp(\theta X_{1})]$ , and their partial sums are denoted by $S_{n}=X_{1}+\dots +X_{n}$ , then the sequence $W_{n}=\exp(\theta S_{n})/M(\theta )^{n}$ is a martingale.
- **Asset pricing in mathematical finance:** By the fundamental theorem of asset pricing, in an arbitrage-free market, the discounted price of any tradable asset is a martingale under the risk-neutral measure. For example, if $S_{t}$ is a stock price and r is the risk-free interest rate, then $e^{-rt}S_{t}$ is a martingale under the equivalent martingale measure.
- A d -dimensional process $M=(M^{(1)},\dots ,M^{(d)})$ in some space $S^{d}$ is a martingale if each component $T_{i}(M)=M^{(i)}$ is a one-dimensional martingale in S .

## Submartingales, supermartingales, and relationship to harmonic functions

There are two generalizations of a martingale that include cases when the current observation $X_{n}$ is not necessarily equal to the future conditional expectation, but instead acts as an upper or lower bound on the conditional expectation.

These generalizations reflect the relationship between martingale theory and potential theory (the study of harmonic functions):

- Just as a continuous-time martingale satisfies $\mathbf {E} [X_{t}\mid \{X_{\tau }:\tau \leq s\}]-X_{s}=0$ for all $s\leq t$ , a harmonic function f satisfies the partial differential equation $\Delta f=0$ where $\Delta$ is the Laplacian operator.
- Given a Brownian motion process $W_{t}$ and a harmonic function f , the resulting process $f(W_{t})$ is also a martingale.

**Submartingales:**

- A discrete-time **submartingale** is a sequence $X_{1},X_{2},X_{3},\dots$ of integrable random variables satisfying:

$\mathbf {E} [X_{n+1}\mid X_{1},\ldots ,X_{n}]\geq X_{n}.$

- Likewise, a continuous-time submartingale satisfies:

$\mathbf {E} [X_{t}\mid \{X_{\tau }:\tau \leq s\}]\geq X_{s}\quad \forall s\leq t.$

- In potential theory, a subharmonic function f satisfies $\Delta f\geq 0$ . Any subharmonic function bounded above by a harmonic function for all points on the boundary of a ball is bounded above by the harmonic function inside the ball.
- Similarly, if a submartingale and a martingale have equivalent expectations for a given time, the history of the submartingale tends to be bounded above by the history of the martingale. Roughly speaking, the prefix "sub-" is consistent because the current observation $X_{n}$ is *less than* (or equal to) the conditional expectation. Consequently, the process tends to increase in future time.

**Supermartingales:**

- Analogously, a discrete-time **supermartingale** satisfies:

$\mathbf {E} [X_{n+1}\mid X_{1},\ldots ,X_{n}]\leq X_{n}.$

- Likewise, a continuous-time supermartingale satisfies:

$\mathbf {E} [X_{t}\mid \{X_{\tau }:\tau \leq s\}]\leq X_{s}\quad \forall s\leq t.$

- In potential theory, a superharmonic function f satisfies $\Delta f\leq 0$ .
- Roughly speaking, the prefix "super-" is consistent because the current observation $X_{n}$ is *greater than* (or equal to) the conditional expectation. Consequently, the process tends to decrease in future time.

### Examples of submartingales and supermartingales

- Every martingale is also a submartingale and a supermartingale. Conversely, any stochastic process that is *both* a submartingale and a supermartingale is a martingale.
- Consider again the gambler who wins $1 when a coin comes up heads and loses $1 when it comes up tails. Suppose now that the coin may be biased, coming up heads with probability p .
  - If $p=1/2$ , the gambler on average neither wins nor loses money, and the fortune over time is a martingale.
  - If $p<1/2$ , the gambler loses money on average, and the fortune over time is a supermartingale.
  - If $p>1/2$ , the gambler wins money on average, and the fortune over time is a submartingale.
- A convex function of a martingale is a submartingale, by Jensen's inequality. For example, the square of the gambler's fortune in the fair coin game is a submartingale (which also follows from the fact that $X_{n}^{2}-n$ is a martingale). Similarly, a concave function of a martingale is a supermartingale.

## Martingales and stopping times

A stopping time with respect to a sequence of random variables $X_{1},X_{2},X_{3},\dots$ is a random variable $\tau$ with the property that for each t , the occurrence or non-occurrence of the event $\tau =t$ depends only on the values of $X_{1},X_{2},\dots ,X_{t}$ . The intuition behind the definition is that at any particular time t , you can look at the sequence so far and tell if it is time to stop. An example might be the time at which a gambler leaves the gambling table, which might depend on previous winnings, but not on games that haven't been played yet.

In some contexts the concept of *stopping time* is defined by requiring only that the occurrence or non-occurrence of the event $\tau =t$ is probabilistically independent of $X_{t+1},X_{t+2},\dots$ but not completely determined by the history up to time t .

One of the basic properties of martingales is that, if $(X_{t})_{t>0}$ is a (sub-/super-) martingale and $\tau$ is a stopping time, then the corresponding stopped process $(X_{t}^{\tau })_{t>0}$ defined by $X_{t}^{\tau }:=X_{\min\{\tau ,t\}}$ is also a (sub-/super-) martingale.

The concept of a stopped martingale leads to a series of important theorems, including the optional stopping theorem which states that, under certain conditions, the expected value of a martingale at a stopping time is equal to its initial value.

## Martingale problem

The martingale problem is a framework in stochastic analysis for characterizing solutions to stochastic differential equations (SDEs) through martingale conditions.

### General Martingale Problem (A, μ)

Let E be a Polish space with Borel $\sigma$ -algebra ${\mathcal {E}}$ , and let ${\mathcal {P}}(E)$ be the set of probability measures on E . Suppose $A:{\mathcal {D}}(A)\to C(E)$ is a Markov pregenerator, where ${\mathcal {D}}(A)$ is a dense subspace of $C(E)$ . A probability measure $\mathbb {P}$ on the Skorokhod space $D_{E}[0,\infty )$ solves the martingale problem $(A,\mu )$ for $\mu \in {\mathcal {P}}(E)$ if:

- For every $\Gamma \in {\mathcal {E}}$ , $\mathbb {P} (\zeta _{0}\in \Gamma )=\mu (\Gamma ).$
- For every $f\in {\mathcal {D}}(A)$ , the process $f(\zeta _{t})-\int _{0}^{t}Af(\zeta _{s})\,ds$ is a local martingale under $\mathbb {P}$ with respect to its natural filtration.

If $\mu =\delta _{\eta }$ (the Dirac measure at $\eta$ ), then $\mathbb {P}$ is said to solve the martingale problem for A with initial point $\eta$ .

### Martingale Problem for Diffusions M(a, b)

A process $X=(X_{t})_{t\geq 0}$ on a filtered probability space $(\Omega ,{\mathcal {F}},({\mathcal {F}}_{t}),\mathbb {P} )$ solves the martingale problem $M(a,b)$ for measurable functions $a:\mathbb {R} ^{d}\to \mathbb {S} _{+}^{d}$ and $b:\mathbb {R} ^{d}\to \mathbb {R} ^{d}$ if:

- For each $1\leq i\leq d$ , $M_{t}^{i}=X_{t}^{i}-\int _{0}^{t}b_{i}(X_{s})\,ds$ is a local martingale.
- For each $1\leq i,j\leq d$ , $M_{t}^{i}M_{t}^{j}-\int _{0}^{t}a_{ij}(X_{s})\,ds$ is a local martingale.

### Connection to Stochastic Differential Equations

Solutions to $M(a,b)$ correspond (in a weak sense) to solutions of the SDE $dX_{t}=b(X_{t})\,dt+\sigma (X_{t})\,dB_{t}$ , where $\sigma \sigma ^{\top }=a$ . One sees this by applying the generator A to simple functions such as $x_{i}$ or $x_{i}x_{j}$ , thereby recovering the drift b and the diffusion matrix a .

## Applications in Mathematical Finance

Martingales form the foundational mathematics behind modern quantitative finance and asset pricing theory.

- **The Fundamental Theorem of Asset Pricing:** This theorem states that a financial market is free of arbitrage if and only if there exists a risk-neutral probability measure (also known as an equivalent martingale measure).
- **Risk-Neutral Pricing:** Under this equivalent martingale measure, the discounted price process of any tradable asset is a martingale. This implies that the current price of an asset is exactly equal to the expected value of its future discounted payoffs.
- **Derivatives Pricing:** Models such as the Black–Scholes model rely heavily on martingale representations. By finding the correct martingale measure via the Girsanov theorem, complex financial derivatives and options can be priced accurately without needing to predict the actual real-world direction of the stock market.
