---
title: "Poisson distribution"
source: https://en.wikipedia.org/wiki/Poisson_distribution
domain: queueing-theory
license: CC-BY-SA-4.0
tags: queueing theory, birth-death process, kendall notation, little's law
fetched: 2026-07-02
---

# Poisson distribution

In probability theory and statistics, the **Poisson distribution** (/ˈpwɑːsɒn/) is a discrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval of time if these events occur with a known constant mean rate and independently of the time since the last event. It can also be used for the number of events in other types of intervals than time, and in dimension greater than 1 (e.g., number of events in a given area or volume). The Poisson distribution is named after French mathematician Siméon Denis Poisson. It plays an important role for discrete-stable distributions.

Under a Poisson distribution with the expectation of λ events in a given interval, the probability of k events in the same interval is: ${\frac {\lambda ^{k}e^{-\lambda }}{k!}}.$ For instance, consider a call center which receives an average of *λ* = 3 calls per minute at all times of day. If the number of calls received in any two given disjoint time intervals is independent, then the number k of calls received during any minute has a Poisson probability distribution. Receiving *k* = 1 to 4 calls then has a probability of about 0.77, while receiving 0 or at least 5 calls has a probability of about 0.23.

A classic example used to motivate the Poisson distribution is the number of radioactive decay events during a fixed observation period.

## History

The introduction of the Poisson distribution is credited to French mathematician and physicist Siméon Denis Poisson (1781–1840), who published it together with his probability theory in *Recherches sur la probabilité des jugements en matière criminelle et en matière civile* (1837). This work theorizes about the number of wrongful convictions in a given country by focusing on certain random variables N that count the number of events that take place during a time interval of given length. However, similar results had already been given in 1711 by Abraham de Moivre in *De Mensura Sortis seu; de Probabilitate Eventuum in Ludis a Casu Fortuito Pendentibus* . This makes it an example of Stigler's law and it has prompted some authors to argue that the Poisson distribution should bear the name of de Moivre.

In 1860, Simon Newcomb fitted the Poisson distribution to the number of stars found in a unit of space. A further practical application was made by Ladislaus Bortkiewicz in 1898. Bortkiewicz showed that the frequency with which soldiers in the Prussian army were accidentally killed by horse kicks could be well modeled by a Poisson distribution..

## Definitions

### Probability mass function

A discrete random variable X is said to have a Poisson distribution with parameter $\lambda >0$ if it has a probability mass function given by: $f(k;\lambda )=\Pr(X{=}k)={\frac {\lambda ^{k}e^{-\lambda }}{k!}},$ where

- k is the number of occurrences ( $k=0,1,2,\ldots$ )
- e is Euler's number ( $e=2.71828\ldots$ )
- *k*! = *k*(*k–*1) ··· (3)(2)(1) is the factorial.

The positive real number λ is equal to the expected value of X and also to its variance. $\lambda =\operatorname {E} (X)=\operatorname {Var} (X).$

The Poisson distribution can be applied to systems with a large number of possible events, each of which is rare. The number of such events that occur during a fixed time interval is, under the right circumstances, a random number with a Poisson distribution.

The equation can be adapted if, instead of the average number of events $\lambda ,$ we are given the average rate r at which events occur. Then $\lambda =rt,$ and: $P(k{\text{ events in interval }}t)={\frac {(rt)^{k}e^{-rt}}{k!}}.$

### Examples

The Poisson distribution may be useful to model events such as:

- the number of meteorites greater than one-meter diameter that strike Earth in a year;
- the number of laser photons hitting a detector in a particular time interval;
- the number of students achieving a low and high mark in an exam; and
- locations of defects and dislocations in materials.

Examples of the occurrence of random points in space are: the locations of asteroid impacts with earth (2-dimensional), the locations of imperfections in a material (3-dimensional), and the locations of trees in a forest (2-dimensional).

### Assumptions and validity

The Poisson distribution is an appropriate model if the following assumptions are true:

- k, a nonnegative integer, is the number of times an event occurs in an interval.
- The occurrence of one event does not affect the probability of a second event.
- The average rate at which events occur is independent of any occurrences.
- Two events cannot occur at exactly the same instant.

If these conditions are true, then k is a Poisson random variable; the distribution of k is a Poisson distribution.

The Poisson distribution is also the limit of a binomial distribution, for which the probability of success for each trial is $p={\frac {\lambda }{n}}$ , where $\lambda$ is the expectation and n is the number of trials, in the limit that $n\to \infty$ with $\lambda$ kept constant (see Related distributions):

$\lim _{n\to \infty }{\dbinom {n}{k}}\left({\frac {\lambda }{n}}\right)^{k}\,\left(1-{\frac {\lambda }{n}}\right)^{n-k}={\frac {\lambda ^{k}}{k!}}\,e^{-\lambda }$

The Poisson distribution may also be derived from the differential equations

${\frac {d\,P_{k}(t)}{dt}}=\lambda \,{\Big (}P_{k-1}(t)-P_{k}(t){\Big )}$

with initial conditions $P_{k}(0)=\delta _{k0}$ and evaluated at $t=1$

#### Examples of probability for Poisson distributions

| On a particular river, overflow floods occur once every 100 years on average. Calculate the probability of k = 0, 1, 2, 3, 4, 5, or 6 overflow floods in a 100-year interval, assuming the Poisson model is appropriate. Because the average event rate is one overflow flood per 100 years, *λ* = 1 ${\begin{aligned}P(k{\text{ overflow floods in 100 years}})&={\frac {\lambda ^{k}e^{-\lambda }}{k!}}={\frac {1^{k}e^{-1}}{k!}}\\P(k=0{\text{ overflow floods in 100 years}})&={\frac {1^{0}e^{-1}}{0!}}={\frac {e^{-1}}{1}}\approx 0.368\\P(k=1{\text{ overflow flood in 100 years}})&={\frac {1^{1}e^{-1}}{1!}}={\frac {e^{-1}}{1}}\approx 0.368\\P(k=2{\text{ overflow floods in 100 years}})&={\frac {1^{2}e^{-1}}{2!}}={\frac {e^{-1}}{2}}\approx 0.184\end{aligned}}$ | k *P*(*k* overflow floods in 100 years) 0 0.368 1 0.368 2 0.184 3 0.061 4 0.015 5 0.003 6 0.0005 The probability for 0 to 6 overflow floods in a 100-year period. |
|---|---|

| In this example, it is reported that the average number of goals in a World Cup soccer match is approximately 2.5 and the Poisson model is appropriate. Because the average event rate is 2.5 goals per match, *λ* = 2.5. ${\begin{aligned}P(k{\text{ goals in a match}})&={\frac {2.5^{k}e^{-2.5}}{k!}}\\P(k=0{\text{ goals in a match}})&={\frac {2.5^{0}e^{-2.5}}{0!}}={\frac {e^{-2.5}}{1}}\approx 0.082\\P(k=1{\text{ goal in a match}})&={\frac {2.5^{1}e^{-2.5}}{1!}}={\frac {2.5e^{-2.5}}{1}}\approx 0.205\\P(k=2{\text{ goals in a match}})&={\frac {2.5^{2}e^{-2.5}}{2!}}={\frac {6.25e^{-2.5}}{2}}\approx 0.257\end{aligned}}$ | k *P*(*k* goals in a World Cup soccer match) 0 0.082 1 0.205 2 0.257 3 0.213 4 0.133 5 0.067 6 0.028 7 0.010 The probability for 0 to 7 goals in a match. |
|---|---|

### Examples that violate the Poisson assumptions

The number of students who arrive at the student union per minute will likely not follow a Poisson distribution, because the rate is not constant (low rate during class time, high rate between class times) and the arrivals of individual students are not independent (students tend to come in groups). The non-constant arrival rate may be modeled as a mixed Poisson distribution, and the arrival of groups rather than individual students as a compound Poisson process.

The number of magnitude 5 earthquakes per year in a country may not follow a Poisson distribution if one large earthquake increases the probability of aftershocks of similar magnitude.

Examples in which at least one event is guaranteed are not Poisson distributed; but may be modeled using a zero-truncated Poisson distribution.

Count distributions in which the number of intervals with zero events is higher than predicted by a Poisson model may be modeled using a zero-inflated model.

## Properties

### Descriptive statistics

- The expected value of a Poisson random variable is λ.
- The variance of a Poisson random variable is also λ.
- The coefficient of variation is ${\textstyle \lambda ^{-1/2},}$ while the index of dispersion is 1.
- The mean absolute deviation about the mean is $\operatorname {E} [\ |X-\lambda |\ ]={\frac {2\lambda ^{\lfloor \lambda \rfloor +1}e^{-\lambda }}{\lfloor \lambda \rfloor !}}.$
- The mode of a Poisson-distributed random variable with non-integer λ is equal to $\lfloor \lambda \rfloor ,$ which is the largest integer less than or equal to λ. This is also written as floor(*λ*). When λ is a positive integer, the modes are λ and *λ* − 1.
- All of the cumulants of the Poisson distribution are equal to the expected value λ. The n-th factorial moment of the Poisson distribution is *λ**n*.
- The expected value of a Poisson process is sometimes decomposed into the product of *intensity* and *exposure* (or more generally expressed as the integral of an "intensity function" over time or space, sometimes described as "exposure").

### Median

Bounds for the median ( $\nu$ ) of the distribution are known and are sharp: $\lambda -\ln 2\leq \nu <\lambda +{\frac {1}{3}}.$

### Higher moments

The higher non-centered moments *m**k* of the Poisson distribution are Touchard polynomials in λ: $m_{k}=\sum _{i=0}^{k}\lambda ^{i}{\begin{Bmatrix}k\\i\end{Bmatrix}},$ where the braces { } denote Stirling numbers of the second kind. In other words, $E[X]=\lambda ,\quad E[X(X-1)]=\lambda ^{2},\quad E[X(X-1)(X-2)]=\lambda ^{3},\cdots$ When the expected value is set to *λ* = 1, Dobinski's formula implies that the n‑th moment is equal to the number of partitions of a set of size n.

A simple upper bound is: $m_{k}=E[X^{k}]\leq \left({\frac {k}{\log(k/\lambda +1)}}\right)^{k}\leq \lambda ^{k}\exp \left({\frac {k^{2}}{2\lambda }}\right).$

### Sums of Poisson-distributed random variables

If $X_{i}\sim \operatorname {Pois} (\lambda _{i})$ for $i=1,\dotsc ,n$ are independent, then ${\textstyle \sum _{i=1}^{n}X_{i}\sim \operatorname {Pois} \left(\sum _{i=1}^{n}\lambda _{i}\right).}$ A converse is Raikov's theorem, which says that if the sum of two independent random variables is Poisson-distributed, then so are each of those two independent random variables.

### Maximum entropy

It is a maximum-entropy distribution among the set of generalized binomial distributions $B_{n}(\lambda )$ with mean $\lambda$ and $n\to \infty$ , where a generalized binomial distribution is defined as a distribution of the sum of N independent but not identically distributed Bernoulli variables.

### Other properties

- The Poisson distributions are infinitely divisible probability distributions.
- The directed Kullback–Leibler divergence of $P=\operatorname {Pois} (\lambda )$ from $P_{0}=\operatorname {Pois} (\lambda _{0})$ is given by $\operatorname {D} _{\text{KL}}(P\parallel P_{0})=\lambda _{0}-\lambda +\lambda \log {\frac {\lambda }{\lambda _{0}}}.$
- If $\lambda \geq 1$ is an integer, then $Y\sim \operatorname {Pois} (\lambda )$ satisfies $\Pr(Y\geq E[Y])\geq {\frac {1}{2}}$ and $\Pr(Y\leq E[Y])\geq {\frac {1}{2}}.$
- Bounds for the tail probabilities of a Poisson random variable $X\sim \operatorname {Pois} (\lambda )$ can be derived using a Chernoff bound argument. ${\begin{aligned}P(X\geq x)&\leq {\frac {\left(e\lambda \right)^{x}e^{-\lambda }}{x^{x}}},&{\text{ for }}x>\lambda ,\\[1ex]P(X\leq x)&\leq {\frac {\left(e\lambda \right)^{x}e^{-\lambda }}{x^{x}}},&{\text{ for }}x<\lambda .\end{aligned}}$
- The upper tail probability can be tightened (by a factor of at least two) as follows: $P(X\geq x)\leq {\frac {e^{-\operatorname {D} _{\text{KL}}(Q\parallel P)}}{\max {(2,{\sqrt {4\pi \operatorname {D} _{\text{KL}}(Q\parallel P)}}})}},{\text{ for }}x>\lambda ,$ where $\operatorname {D} _{\text{KL}}(Q\parallel P)$ is the Kullback–Leibler divergence of $Q=\operatorname {Pois} (x)$ from $P=\operatorname {Pois} (\lambda )$ .
- Inequalities that relate the cumulative distribution function of a Poisson random variable $X\sim \operatorname {Pois} (\lambda )$ to the cumulative distribution function $\Phi$ of the standard normal distribution are as follows:

$\Phi {\left(\operatorname {sign} (k-\lambda ){\sqrt {2\operatorname {D} _{\text{KL}}(Q_{-}\parallel P)}}\right)}<P(X\leq k)<\Phi {\left(\operatorname {sign} (k+1-\lambda ){\sqrt {2\operatorname {D} _{\text{KL}}(Q_{+}\parallel P)}}\right)},{\text{ for }}k>0,$ where $\operatorname {D} _{\text{KL}}(Q_{-}\parallel P)$ is the Kullback–Leibler divergence of $Q_{-}=\operatorname {Pois} (k)$ from $P=\operatorname {Pois} (\lambda )$ and $\operatorname {D} _{\text{KL}}(Q_{+}\parallel P)$ is the Kullback–Leibler divergence of $Q_{+}=\operatorname {Pois} (k+1)$ from P .

### Poisson races

Let $X\sim \operatorname {Pois} (\lambda )$ and $Y\sim \operatorname {Pois} (\mu )$ be independent random variables, with $\lambda <\mu ,$ then we have that ${\frac {e^{-({\sqrt {\mu }}-{\sqrt {\lambda }})^{2}}}{(\lambda +\mu )^{2}}}-{\frac {e^{-(\lambda +\mu )}}{2{\sqrt {\lambda \mu }}}}-{\frac {e^{-(\lambda +\mu )}}{4\lambda \mu }}\leq P(X-Y\geq 0)\leq e^{-({\sqrt {\mu }}-{\sqrt {\lambda }})^{2}}$

The upper bound is proved using a standard Chernoff bound.

The lower bound can be proved by noting that $P(X-Y\geq 0\mid X+Y=i)$ is the probability that ${\textstyle Z\geq {\frac {i}{2}},}$ where ${\textstyle Z\sim \operatorname {Bin} \left(i,{\frac {\lambda }{\lambda +\mu }}\right),}$ which is bounded below by ${\textstyle {\frac {1}{(i+1)^{2}}}e^{-iD\left(0.5\|{\frac {\lambda }{\lambda +\mu }}\right)},}$ where D is relative entropy (See the entry on bounds on tails of binomial distributions for details). Further noting that $X+Y\sim \operatorname {Pois} (\lambda +\mu ),$ and computing a lower bound on the unconditional probability gives the result. More details can be found in the appendix of Kamath et al.

### As a Binomial distribution with infinitesimal time-steps

The Poisson distribution can be derived as a limiting case to the binomial distribution as the number of trials goes to infinity and the expected number of successes remains fixed — see law of rare events below. Therefore, it can be used as an approximation of the binomial distribution if n is sufficiently large and p is sufficiently small. The Poisson distribution is a good approximation of the binomial distribution if n is at least 20 and p is smaller than or equal to 0.05, and an excellent approximation if *n* ≥ 100 and *np* ≤ 10. Letting $F_{\mathrm {B} }$ and $F_{\mathrm {P} }$ be the respective cumulative density functions of the binomial and Poisson distributions, one has: $F_{\mathrm {B} }(k;n,p)\ \approx \ F_{\mathrm {P} }(k;\lambda =np).$ One derivation of this uses probability-generating functions. Consider a Bernoulli trial (coin-flip) whose probability of one success (or expected number of successes) is $\lambda \leq 1$ within a given interval. Split the interval into n parts, and perform a trial in each subinterval with probability ${\tfrac {\lambda }{n}}$ . The probability of k successes out of n trials over the entire interval is then given by the binomial distribution $p_{k}^{(n)}={\binom {n}{k}}\left({\frac {\lambda }{n}}\right)^{\!k}\left(1{-}{\frac {\lambda }{n}}\right)^{\!n-k},$ whose generating function is: $P^{(n)}(x)=\sum _{k=0}^{n}p_{k}^{(n)}x^{k}=\left(1-{\frac {\lambda }{n}}+{\frac {\lambda }{n}}x\right)^{n}.$ Taking the limit as n increases to infinity (with x fixed) and applying the product limit definition of the exponential function, this reduces to the generating function of the Poisson distribution: $\lim _{n\to \infty }P^{(n)}(x)=\lim _{n\to \infty }\left(1{+}{\tfrac {\lambda (x-1)}{n}}\right)^{n}=e^{\lambda (x-1)}=\sum _{k=0}^{\infty }e^{-\lambda }{\frac {\lambda ^{k}}{k!}}x^{k}.$

### General

- If $X_{1}\sim \mathrm {Pois} (\lambda _{1})\,$ and $X_{2}\sim \mathrm {Pois} (\lambda _{2})\,$ are independent, then the difference $Y=X_{1}-X_{2}$ follows a Skellam distribution.
- If $X_{1}\sim \mathrm {Pois} (\lambda _{1})\,$ and $X_{2}\sim \mathrm {Pois} (\lambda _{2})\,$ are independent, then the distribution of $X_{1}$ conditional on $X_{1}+X_{2}$ is a binomial distribution. Specifically, if $X_{1}+X_{2}=k,$ then $X_{1}|X_{1}+X_{2}=k\sim \mathrm {Binom} (k,\lambda _{1}/(\lambda _{1}+\lambda _{2})).$ More generally, if *X*1, *X*2, ..., *X**n* are independent Poisson random variables with parameters *λ*1, *λ*2, ..., *λ**n* then given $\sum _{j=1}^{n}X_{j}=k,$ it follows that $X_{i}{\Big |}\sum _{j=1}^{n}X_{j}=k\sim \mathrm {Binom} \left(k,{\frac {\lambda _{i}}{\sum _{j=1}^{n}\lambda _{j}}}\right).$ In fact, $\{X_{i}\}\sim \mathrm {Multinom} \left(k,\left\{{\frac {\lambda _{i}}{\sum _{j=1}^{n}\lambda _{j}}}\right\}\right).$
- If $X\sim \mathrm {Pois} (\lambda )\,$ and the distribution of Y conditional on *X* = *k* is a binomial distribution, $Y\mid (X=k)\sim \mathrm {Binom} (k,p),$ then the distribution of Y follows a Poisson distribution $Y\sim \mathrm {Pois} (\lambda \cdot p).$ In fact, if, conditional on $\{X=k\},$ $\{Y_{i}\}$ follows a multinomial distribution, $\{Y_{i}\}\mid (X=k)\sim \mathrm {Multinom} \left(k,p_{i}\right),$ then each $Y_{i}$ follows an independent Poisson distribution $Y_{i}\sim \mathrm {Pois} (\lambda \cdot p_{i}),\rho (Y_{i},Y_{j})=0.$
- The Poisson distribution is a special case of the discrete compound Poisson distribution (or stuttering Poisson distribution) with only a parameter. The discrete compound Poisson distribution can be deduced from the limiting distribution of univariate multinomial distribution. It is also a special case of a compound Poisson distribution.
- For sufficiently large values of λ, (say *λ* > 1000), the normal distribution with mean λ and variance λ (standard deviation ${\sqrt {\lambda }}$ ) is an excellent approximation to the Poisson. If λ is greater than about 10, then the normal distribution is a good approximation if an appropriate continuity correction is performed, i.e., if P(*X* ≤ *x*), where x is a non-negative integer, is replaced by P(*X* ≤ *x* + 0.5). $F_{\mathrm {Poisson} }(x;\lambda )\approx F_{\mathrm {normal} }(x;\mu =\lambda ,\sigma ^{2}=\lambda )$
- Variance-stabilizing transformation: If $X\sim \mathrm {Pois} (\lambda ),$ then $Y=2{\sqrt {X}}\approx {\mathcal {N}}(2{\sqrt {\lambda }};1),$ and $Y={\sqrt {X}}\approx {\mathcal {N}}({\sqrt {\lambda }};1/4).$ Under this transformation, the convergence to normality (as $\lambda$ increases) is far faster than the untransformed variable. Other, slightly more complicated, variance stabilizing transformations are available, one of which is Anscombe transform. See Data transformation (statistics) for more general uses of transformations.
- If for every *t* > 0 the number of arrivals in the time interval [0, *t*] follows the Poisson distribution with mean λt, then the sequence of inter-arrival times are independent and identically distributed exponential random variables having mean 1/*λ*.
- The cumulative distribution functions of the Poisson and chi-squared distributions are related in the following ways: $F_{\text{Poisson}}(k;\lambda )=1-F_{\chi ^{2}}(2\lambda ;2(k+1))\quad \quad {\text{ integer }}k,$ and $P(X=k)=F_{\chi ^{2}}(2\lambda ;2(k+1))-F_{\chi ^{2}}(2\lambda ;2k).$

### Poisson approximation

Assume $X_{1}\sim \operatorname {Pois} (\lambda _{1}),X_{2}\sim \operatorname {Pois} (\lambda _{2}),\dots ,X_{n}\sim \operatorname {Pois} (\lambda _{n})$ where $\lambda _{1}+\lambda _{2}+\dots +\lambda _{n}=1,$ then $(X_{1},X_{2},\dots ,X_{n})$ is multinomially distributed $(X_{1},X_{2},\dots ,X_{n})\sim \operatorname {Mult} (N,\lambda _{1},\lambda _{2},\dots ,\lambda _{n})$ conditioned on $N=X_{1}+X_{2}+\dots X_{n}.$

This means, among other things, that for any nonnegative function $f(x_{1},x_{2},\dots ,x_{n}),$ if $(Y_{1},Y_{2},\dots ,Y_{n})\sim \operatorname {Mult} (m,\mathbf {p} )$ is multinomially distributed, then $\operatorname {E} [f(Y_{1},Y_{2},\dots ,Y_{n})]\leq e{\sqrt {m}}\operatorname {E} [f(X_{1},X_{2},\dots ,X_{n})]$ where $(X_{1},X_{2},\dots ,X_{n})\sim \operatorname {Pois} (\mathbf {p} ).$

The factor of $e{\sqrt {m}}$ can be replaced by 2 if f is further assumed to be monotonically increasing or decreasing.

### Bivariate Poisson distribution

This distribution has been extended to the bivariate case. The generating function for this distribution is $g(u,v)=\exp[(\theta _{1}-\theta _{12})(u-1)+(\theta _{2}-\theta _{12})(v-1)+\theta _{12}(uv-1)]$ with $\theta _{1},\theta _{2}>\theta _{12}>0$

The marginal distributions are Poisson(*θ*1) and Poisson(*θ*2) and the correlation coefficient is limited to the range $0\leq \rho \leq \min \left\{{\sqrt {\frac {\theta _{1}}{\theta _{2}}}},{\sqrt {\frac {\theta _{2}}{\theta _{1}}}}\right\}$

A simple way to generate a bivariate Poisson distribution $X_{1},X_{2}$ is to take three independent Poisson distributions $Y_{1},Y_{2},Y_{3}$ with means $\lambda _{1},\lambda _{2},\lambda _{3}$ and then set $X_{1}=Y_{1}+Y_{3},X_{2}=Y_{2}+Y_{3}.$ The probability function of the bivariate Poisson distribution is $\Pr(X_{1}=k_{1},X_{2}=k_{2})=\exp \left(-\lambda _{1}-\lambda _{2}-\lambda _{3}\right){\frac {\lambda _{1}^{k_{1}}}{k_{1}!}}{\frac {\lambda _{2}^{k_{2}}}{k_{2}!}}\sum _{k=0}^{\min(k_{1},k_{2})}{\binom {k_{1}}{k}}{\binom {k_{2}}{k}}k!\left({\frac {\lambda _{3}}{\lambda _{1}\lambda _{2}}}\right)^{k}$

### Free Poisson distribution

The free Poisson distribution with jump size $\alpha$ and rate $\lambda$ arises in free probability theory as the limit of repeated free convolution $\left(\left(1-{\frac {\lambda }{N}}\right)\delta _{0}+{\frac {\lambda }{N}}\delta _{\alpha }\right)^{\boxplus N}$ as *N* → ∞.

In other words, let $X_{N}$ be random variables so that $X_{N}$ has value $\alpha$ with probability ${\textstyle {\frac {\lambda }{N}}}$ and value 0 with the remaining probability. Assume also that the family $X_{1},X_{2},\ldots$ are freely independent. Then the limit as $N\to \infty$ of the law of $X_{1}+\cdots +X_{N}$ is given by the Free Poisson law with parameters $\lambda ,\alpha .$

This definition is analogous to one of the ways in which the classical Poisson distribution is obtained from a (classical) Poisson process.

The measure associated to the free Poisson law is given by $\mu ={\begin{cases}(1-\lambda )\delta _{0}+\nu ,&{\text{if }}0\leq \lambda \leq 1\\\nu ,&{\text{if }}\lambda >1,\end{cases}}$ where $\nu ={\frac {1}{2\pi \alpha t}}{\sqrt {4\lambda \alpha ^{2}-(t-\alpha (1+\lambda ))^{2}}}\,dt$ and has support $[\alpha (1-{\sqrt {\lambda }})^{2},\alpha (1+{\sqrt {\lambda }})^{2}].$

This law also arises in random matrix theory as the Marchenko–Pastur law. Its free cumulants are equal to $\kappa _{n}=\lambda \alpha ^{n}.$

#### Some transforms of this law

We give values of some important transforms of the free Poisson law; the computation can be found in e.g. in the book *Lectures on the Combinatorics of Free Probability* by A. Nica and R. Speicher

The R-transform of the free Poisson law is given by $R(z)={\frac {\lambda \alpha }{1-\alpha z}}.$

The Cauchy transform (which is the negative of the Stieltjes transformation) is given by $G(z)={\frac {z+\alpha -\lambda \alpha -{\sqrt {(z-\alpha (1+\lambda ))^{2}-4\lambda \alpha ^{2}}}}{2\alpha z}}$

The S-transform is given by $S(z)={\frac {1}{z+\lambda }}$ in the case that $\alpha =1.$

## Statistical inference

### Parameter estimation

Given a sample of n measured values $k_{i}\in \{0,1,\dots \},$ for *i* = 1, ..., *n*, we wish to estimate the value of the parameter λ of the Poisson population from which the sample was drawn. The maximum likelihood estimate is

${\widehat {\lambda }}_{\mathrm {MLE} }={\frac {1}{n}}\sum _{i=1}^{n}k_{i}\ .$

Since each observation has expectation λ, so does the sample mean. Therefore, the maximum likelihood estimate is an unbiased estimator of λ. It is also an efficient estimator since its variance achieves the Cramér–Rao lower bound (CRLB). Hence it is minimum-variance unbiased. Also it can be proven that the sum (and hence the sample mean as it is a one-to-one function of the sum) is a complete and sufficient statistic for λ.

To prove sufficiency we may use the factorization theorem. Consider partitioning the probability mass function of the joint Poisson distribution for the sample into two parts: one that depends solely on the sample $\mathbf {x}$ , called $h(\mathbf {x} )$ , and one that depends on the parameter $\lambda$ and the sample $\mathbf {x}$ only through the function $T(\mathbf {x} ).$ Then $T(\mathbf {x} )$ is a sufficient statistic for $\lambda .$

$P(\mathbf {x} )=\prod _{i=1}^{n}{\frac {\lambda ^{x_{i}}e^{-\lambda }}{x_{i}!}}={\frac {1}{\prod _{i=1}^{n}x_{i}!}}\times \lambda ^{\sum _{i=1}^{n}x_{i}}e^{-n\lambda }$

The first term $h(\mathbf {x} )$ depends only on $\mathbf {x}$ . The second term $g(T(\mathbf {x} )|\lambda )$ depends on the sample only through ${\textstyle T(\mathbf {x} )=\sum _{i=1}^{n}x_{i}.}$ Thus, $T(\mathbf {x} )$ is sufficient.

To find the parameter λ that maximizes the probability function for the Poisson population, we can use the logarithm of the likelihood function:

${\begin{aligned}\ell (\lambda )&=\ln \prod _{i=1}^{n}f(k_{i}\mid \lambda )\\&=\sum _{i=1}^{n}\ln \!\left({\frac {e^{-\lambda }\lambda ^{k_{i}}}{k_{i}!}}\right)\\&=-n\lambda +\left(\sum _{i=1}^{n}k_{i}\right)\ln(\lambda )-\sum _{i=1}^{n}\ln(k_{i}!).\end{aligned}}$

We take the derivative of $\ell$ with respect to λ and compare it to zero:

${\frac {\mathrm {d} }{\mathrm {d} \lambda }}\ell (\lambda )=0\iff -n+\left(\sum _{i=1}^{n}k_{i}\right){\frac {1}{\lambda }}=0.\!$

Solving for λ gives a stationary point.

$\lambda ={\frac {\sum _{i=1}^{n}k_{i}}{n}}$

So λ is the average of the *k**i* values. Obtaining the sign of the second derivative of L at the stationary point will determine what kind of extreme value λ is.

${\frac {\partial ^{2}\ell }{\partial \lambda ^{2}}}=-\lambda ^{-2}\sum _{i=1}^{n}k_{i}$

Evaluating the second derivative *at the stationary point* gives:

${\frac {\partial ^{2}\ell }{\partial \lambda ^{2}}}=-{\frac {n^{2}}{\sum _{i=1}^{n}k_{i}}}$

which is the negative of n times the reciprocal of the average of the *k**i*. This expression is negative when the average is positive. If this is satisfied, then the stationary point maximizes the probability function.

For completeness, a family of distributions is said to be complete if and only if $E(g(T))=0$ implies that $P_{\lambda }(g(T)=0)=1$ for all $\lambda .$ If the individual $X_{i}$ are iid $\mathrm {Po} (\lambda ),$ then ${\textstyle T(\mathbf {x} )=\sum _{i=1}^{n}X_{i}\sim \mathrm {Po} (n\lambda ).}$ Knowing the distribution we want to investigate, it is easy to see that the statistic is complete.

$E(g(T))=\sum _{t=0}^{\infty }g(t){\frac {(n\lambda )^{t}e^{-n\lambda }}{t!}}=0$

For this equality to hold, $g(t)$ must be 0. This follows from the fact that none of the other terms will be 0 for all t in the sum and for all possible values of $\lambda .$ Hence, $E(g(T))=0$ for all $\lambda$ implies that $P_{\lambda }(g(T)=0)=1,$ and the statistic has been shown to be complete.

### Confidence interval

The confidence interval for the mean of a Poisson distribution can be expressed using the relationship between the cumulative distribution functions of the Poisson and chi-squared distributions. The chi-squared distribution is itself closely related to the gamma distribution, and this leads to an alternative expression. Given an observation k from a Poisson distribution with mean μ, a confidence interval for μ with confidence level 1 – *α* is

${\tfrac {1}{2}}\chi ^{2}(\alpha /2;2k)\leq \mu \leq {\tfrac {1}{2}}\chi ^{2}(1-\alpha /2;2k+2),$

or equivalently,

$F^{-1}(\alpha /2;k,1)\leq \mu \leq F^{-1}(1-\alpha /2;k+1,1),$

where $\chi ^{2}(p;n)$ is the quantile function (corresponding to a lower tail area p) of the chi-squared distribution with n degrees of freedom and $F^{-1}(p;n,1)$ is the quantile function of a gamma distribution with shape parameter n and scale parameter 1. This interval is 'exact' in the sense that its coverage probability is never less than the nominal 1 – *α*.

When quantiles of the gamma distribution are not available, an accurate approximation to this exact interval has been proposed (based on the Wilson–Hilferty transformation): $k\left(1-{\frac {1}{9k}}-{\frac {z_{\alpha /2}}{3{\sqrt {k}}}}\right)^{3}\leq \mu \leq (k+1)\left(1-{\frac {1}{9(k+1)}}+{\frac {z_{\alpha /2}}{3{\sqrt {k+1}}}}\right)^{3},$ where $z_{\alpha /2}$ denotes the standard normal deviate with upper tail area α / 2.

For application of these formulae in the same context as above (given a sample of n measured values *k**i* each drawn from a Poisson distribution with mean λ), one would set

$k=\sum _{i=1}^{n}k_{i},$ calculate an interval for *μ* = *nλ*, and then derive the interval for λ.

### Bayesian inference

In Bayesian inference, the conjugate prior for the rate parameter λ of the Poisson distribution is the gamma distribution. Let

$\lambda \sim \mathrm {Gamma} (\alpha ,\beta )$

denote that λ is distributed according to the gamma density g parameterized in terms of a shape parameter α and an inverse scale parameter β:

$g(\lambda \mid \alpha ,\beta )={\frac {\beta ^{\alpha }}{\Gamma (\alpha )}}\;\lambda ^{\alpha -1}\;e^{-\beta \,\lambda }\qquad {\text{ for }}\lambda >0\,\!.$

Then, given the same sample of n measured values *k**i* as before, and a prior of Gamma(*α*, *β*), the posterior distribution is

$\lambda \sim \mathrm {Gamma} {\left(\alpha +\sum _{i=1}^{n}k_{i},\beta +n\right)}.$

Note that the posterior mean is linear and is given by $E[\lambda \mid k_{1},\ldots ,k_{n}]={\frac {\alpha +\sum _{i=1}^{n}k_{i}}{\beta +n}}.$ It can be shown that gamma distribution is the only prior that induces linearity of the conditional mean. Moreover, a converse result exists which states that if the conditional mean is close to a linear function in the $L_{2}$ distance than the prior distribution of λ must be close to gamma distribution in Levy distance.

The posterior mean E[*λ*] approaches the maximum likelihood estimate ${\widehat {\lambda }}_{\mathrm {MLE} }$ in the limit as $\alpha \to 0,\beta \to 0,$ which follows immediately from the general expression of the mean of the gamma distribution.

The posterior predictive distribution for a single additional observation is a negative binomial distribution, sometimes called a gamma–Poisson distribution.

### Simultaneous estimation of multiple Poisson means

Suppose $X_{1},X_{2},\dots ,X_{p}$ is a set of independent random variables from a set of p Poisson distributions, each with a parameter $\lambda _{i},$ $i=1,\dots ,p,$ and we would like to estimate these parameters. Then, Clevenson and Zidek show that under the normalized squared error loss ${\textstyle L(\lambda ,{\hat {\lambda }})=\sum _{i=1}^{p}\lambda _{i}^{-1}({\hat {\lambda }}_{i}-\lambda _{i})^{2},}$ when $p>1,$ then, similar as in Stein's example for the Normal means, the MLE estimator ${\hat {\lambda }}_{i}=X_{i}$ is inadmissible.

In this case, a family of minimax estimators is given for any $0<c\leq 2(p-1)$ and $b\geq (p-2+p^{-1})$ as ${\hat {\lambda }}_{i}=\left(1-{\frac {c}{b+\sum _{i=1}^{p}X_{i}}}\right)X_{i},\qquad i=1,\dots ,p.$

## Occurrence and applications

Some applications of the Poisson distribution to count data (number of events):

- telecommunication: telephone calls arriving in a system,
- astronomy: photons arriving at a telescope,
- chemistry: the molar mass distribution of a living polymerization,
- biology: the number of mutations on a strand of DNA per unit length,
- management: customers arriving at a counter or call centre,
- finance and insurance: number of losses or claims occurring in a given period of time,
- seismology: asymptotic Poisson model of risk for large earthquakes,
- radioactivity: decays in a given time interval in a radioactive sample,
- optics: number of photons emitted in a single laser pulse (a major vulnerability of quantum key distribution protocols, known as photon number splitting).

More examples of counting events that may be modelled as Poisson processes include:

- soldiers killed by horse-kicks each year in each corps in the Prussian cavalry. This example was used in a book by Ladislaus Bortkiewicz (1868–1931),
- yeast cells used when brewing Guinness beer. This example was used by William Sealy Gosset (1876–1937),
- phone calls arriving at a call centre within a minute. This example was described by A.K. Erlang (1878–1929),
- goals in sports involving two competing teams,
- deaths per year in a given age group,
- jumps in a stock price in a given time interval,
- times a web server is accessed per minute (under an assumption of homogeneity),
- mutations in a given stretch of DNA after a certain amount of radiation,
- cells infected at a given multiplicity of infection,
- bacteria in a certain amount of liquid,
- photons arriving on a pixel circuit at a given illumination over a given time period,
- landing of V-1 flying bombs on London during World War II, investigated by R. D. Clarke in 1946.

In probabilistic number theory, Gallagher showed in 1976 that, if a certain version of the unproved prime r-tuple conjecture holds, then the counts of prime numbers in short intervals would obey a Poisson distribution.

### Law of rare events

The rate of an event is related to the probability of an event occurring in some small subinterval (of time, space or otherwise). In the case of the Poisson distribution, one assumes that there exists a small enough subinterval for which the probability of an event occurring twice is "negligible". With this assumption one can derive the Poisson distribution from the binomial one, given only the information of expected number of total events in the whole interval.

Let the total number of events in the whole interval be denoted by $\lambda .$ Divide the whole interval into n subintervals $I_{1},\dots ,I_{n}$ of equal size, such that $n>\lambda$ (since we are interested in only very small portions of the interval this assumption is meaningful). This means that the expected number of events in each of the n subintervals is equal to $\lambda /n.$

Now we assume that the occurrence of an event in the whole interval can be seen as a sequence of n Bernoulli trials, where the i -th Bernoulli trial corresponds to looking whether an event happens at the subinterval $I_{i}$ with probability $\lambda /n.$ The expected number of total events in n such trials would be $\lambda ,$ the expected number of total events in the whole interval. Hence for each subdivision of the interval we have approximated the occurrence of the event as a Bernoulli process of the form ${\textrm {B}}(n,\lambda /n).$ As we have noted before we want to consider only very small subintervals. Therefore, we take the limit as n goes to infinity.

In this case the binomial distribution converges to what is known as the Poisson distribution by the Poisson limit theorem.

In several of the above examples — such as the number of mutations in a given sequence of DNA — the events being counted are actually the outcomes of discrete trials, and would more precisely be modelled using the binomial distribution, that is $X\sim {\textrm {B}}(n,p).$

In such cases n is very large and p is very small (and so the expectation np is of intermediate magnitude). Then the distribution may be approximated by the less cumbersome Poisson distribution $X\sim {\textrm {Pois}}(np).$

This approximation is sometimes known as the *law of rare events*, since each of the n individual Bernoulli events rarely occurs.

The name "law of rare events" may be misleading because the total count of success events in a Poisson process need not be rare if the parameter np is not small. For example, the number of telephone calls to a busy switchboard in one hour follows a Poisson distribution with the events appearing frequent to the operator, but they are rare from the point of view of the average member of the population who is very unlikely to make a call to that switchboard in that hour.

The variance of the binomial distribution is 1 − *p* times that of the Poisson distribution, so almost equal when p is very small.

The word *law* is sometimes used as a synonym of probability distribution, and *convergence in law* means *convergence in distribution*. Accordingly, the Poisson distribution is sometimes called the "law of small numbers" because it is the probability distribution of the number of occurrences of an event that happens rarely but has very many opportunities to happen. *The Law of Small Numbers* is a book by Ladislaus Bortkiewicz about the Poisson distribution, published in 1898.

### Poisson point process

The Poisson distribution arises as the number of points of a Poisson point process located in some finite region. More specifically, if D is some region space, for example Euclidean space **R***d*, for which |*D*|, the area, volume or, more generally, the Lebesgue measure of the region is finite, and if *N*(*D*) denotes the number of points in D, then

$P(N(D)=k)={\frac {(\lambda |D|)^{k}e^{-\lambda |D|}}{k!}}.$

### Poisson regression and negative binomial regression

Poisson regression and negative binomial regression are useful for analyses where the dependent (response) variable is the count (0, 1, 2, ... ) of the number of events or occurrences in an interval.

### Biology

The Luria–Delbrück experiment tested against the hypothesis of Lamarckian evolution, which should result in a Poisson distribution.

Katz and Miledi measured the membrane potential with and without the presence of acetylcholine (ACh). When ACh is present, ion channels on the membrane would be open randomly at a small fraction of the time. As there are a large number of ion channels each open for a small fraction of the time, the total number of ion channels open at any moment is Poisson distributed. When ACh is not present, effectively no ion channels are open. The membrane potential is $V=N_{\text{open}}V_{\text{ion}}+V_{0}+V_{\text{noise}}$ . Subtracting the effect of noise, Katz and Miledi found the mean and variance of membrane potential to be $8.5\times 10^{-3}\;\mathrm {V}$ and $(29.2\times 10^{-6}\;\mathrm {V} )^{2}$ respectively, giving $V_{\text{ion}}=10^{-7}\;\mathrm {V}$ . (pp. 94-95)

During each cellular replication event, the number of mutations is roughly Poisson distributed. For example, the HIV virus has 10,000 base pairs, and has a mutation rate of about 1 per 30,000 base pairs, meaning the number of mutations per replication event is distributed as $\mathrm {Pois} (1/3)$ . (p. 64)

### Other applications in science

In a Poisson process, the number of observed occurrences fluctuates about its mean λ with a standard deviation $\sigma _{k}={\sqrt {\lambda }}.$ These fluctuations are denoted as *Poisson noise* or (particularly in electronics) as *shot noise*.

The correlation of the mean and standard deviation in counting independent discrete occurrences is useful scientifically. By monitoring how the fluctuations vary with the mean signal, one can estimate the contribution of a single occurrence, *even if that contribution is too small to be detected directly*. For example, the charge e on an electron can be estimated by correlating the magnitude of an electric current with its shot noise. If N electrons pass a point in a given time t on the average, the mean current is $I=eN/t$ ; since the current fluctuations should be of the order $\sigma _{I}=e{\sqrt {N}}/t$ (i.e., the standard deviation of the Poisson process), the charge e can be estimated from the ratio $t\sigma _{I}^{2}/I.$

An everyday example is the graininess that appears as photographs are enlarged; the graininess is due to Poisson fluctuations in the number of reduced silver grains, not to the individual grains themselves. By correlating the graininess with the degree of enlargement, one can estimate the contribution of an individual grain (which is otherwise too small to be seen unaided).

In causal set theory the discrete elements of spacetime follow a Poisson distribution in the volume.

The Poisson distribution also appears in quantum mechanics, especially quantum optics. Namely, for a quantum harmonic oscillator system in a coherent state, the probability of measuring a particular energy level has a Poisson distribution.

## Computational methods

The Poisson distribution poses two different tasks for dedicated software libraries: *evaluating* the distribution $P(k;\lambda )$ , and *drawing random numbers* according to that distribution.

### Evaluating the Poisson distribution

Computing $P(k;\lambda )$ for given k and $\lambda$ is a trivial task that can be accomplished by using the standard definition of $P(k;\lambda )$ in terms of exponential, power, and factorial functions. However, the conventional definition of the Poisson distribution contains two terms that can easily overflow on computers: *λ**k* and *k*!. The fraction of *λ**k* to *k*! can also produce a rounding error that is very large compared to *e*−*λ*, and therefore give an erroneous result. For numerical stability the Poisson probability mass function should therefore be evaluated as $\!f(k;\lambda )=\exp \left[k\ln \lambda -\lambda -\ln \Gamma (k+1)\right],$ which is mathematically equivalent but numerically stable. The natural logarithm of the Gamma function can be obtained using the `lgamma` function in the C standard library (C99 version) or R, the `gammaln` function in MATLAB or SciPy, or the `log_gamma` function in Fortran 2008 and later.

Some computing languages provide built-in functions to evaluate the Poisson distribution, namely

- R: function `dpois(x, lambda)`;
- Excel: function `POISSON( x, mean, cumulative)`, with a flag to specify the cumulative distribution;
- Mathematica: univariate Poisson distribution as `PoissonDistribution[ $\lambda$ ]`, bivariate Poisson distribution as `MultivariatePoissonDistribution[ $\theta _{12},$ { $\theta _{1}-\theta _{12},$ $\theta _{2}-\theta _{12}$ }]`,.

### Random variate generation

The less trivial task is to draw integer random variate from the Poisson distribution with given $\lambda .$

Solutions are provided by:

- R: function `rpois(n, lambda)`;
- GNU Scientific Library (GSL): function gsl_ran_poisson

A simple algorithm to generate random Poisson-distributed numbers (pseudo-random number sampling) has been given by Knuth:

```
algorithm poisson random number (Knuth):
    init:
        Let L ← e−λ, k ← 0 and p ← 1.
    do:
        k ← k + 1.
        Generate uniform random number u in [0,1] and let p ← p × u.
    while p > L.
    return k − 1.
```

The complexity is linear in the returned value k, which is λ on average. There are many other algorithms to improve this. Some are given in Ahrens & Dieter, see § References below.

For large values of λ, the value of *L* = *e*−*λ* may be so small that it is hard to represent. This can be solved by a change to the algorithm which uses an additional parameter STEP such that *e*−STEP does not underflow:

```
algorithm poisson random number (Junhao, based on Knuth):
    init:
        Let λLeft ← λ, k ← 0 and p ← 1.
    do:
        k ← k + 1.
        Generate uniform random number u in (0,1) and let p ← p × u.
        while p < 1 and λLeft > 0:
            if λLeft > STEP:
                p ← p × eSTEP
                λLeft ← λLeft − STEP
            else:
                p ← p × eλLeft
                λLeft ← 0
    while p > 1.
    return k − 1.
```

The choice of STEP depends on the threshold of overflow. For double precision floating point format the threshold is near *e*700, so 500 should be a safe *STEP*.

Other solutions for large values of λ include rejection sampling and using Gaussian approximation.

Inverse transform sampling is simple and efficient for small values of λ, and requires only one uniform random number u per sample. Cumulative probabilities are examined in turn until one exceeds u.

```
algorithm Poisson generator based upon the inversion by sequential search:
    init:
        Let x ← 0, p ← e−λ, s ← p.
        Generate uniform random number u in [0,1].
    while u > s do:
        x ← x + 1.
        p ← p × λ / x.
        s ← s + p.
    return x.
```
