---
title: "Negative binomial distribution"
source: https://en.wikipedia.org/wiki/Negative_binomial_distribution
domain: poisson-regression
license: CC-BY-SA-4.0
tags: poisson regression, count data, overdispersion, negative binomial
fetched: 2026-07-02
---

# Negative binomial distribution

In probability theory and statistics, the **negative binomial distribution**, also called a **Pascal distribution**, is a discrete probability distribution that models the number of failures in a sequence of independent and identically distributed Bernoulli trials before a specified/constant/fixed number of successes r occur. (Sometimes the roles are swapped: the number of failures is fixed and the number of successes is modeled.) For example, we can define rolling a 6 on some dice as a success, and rolling any other number as a failure, and ask how many failure rolls will occur before we see the third success ( $r=3$ ). In such a case, the probability distribution of the number of failures that appear will be a negative binomial distribution.

An alternative formulation is to model the number of total trials (instead of the number of failures). In fact, for a specified (non-random) number of successes (*r*), the number of failures (*n* − *r*) is random because the number of total trials (*n*) is random. For example, we could use the negative binomial distribution to model the number of days n (random) a certain machine works (specified by r) before it breaks down.

The negative binomial distribution has a variance $\mu /p$ , with the distribution becoming identical to Poisson in the limit $p\to 1$ for a given mean $\mu$ (i.e. when the failures are increasingly rare). Here $p\in [0,1]$ is the success probability of each Bernoulli trial. This can make the distribution a useful overdispersed alternative to the Poisson distribution, for example for a robust modification of Poisson regression. In epidemiology, it has been used to model disease transmission for infectious diseases where the likely number of onward infections may vary considerably from individual to individual and from setting to setting. More generally, it may be appropriate where events have positively correlated occurrences causing a larger variance than if the occurrences were independent, due to a positive covariance term.

The term "negative binomial" is likely due to the fact that a certain binomial coefficient that appears in the formula for the probability mass function of the distribution can be written more simply with negative numbers.

## Definitions

Imagine a sequence of independent Bernoulli trials: each trial has two potential outcomes called "success" and "failure." In each trial the probability of success is p and of failure is $1-p$ . We observe this sequence until a predefined number r of successes occurs. Then the random number of observed failures, X , follows the **negative binomial** distribution: $X\sim \operatorname {NB} (r,p)$

### Probability mass function

The probability mass function of the negative binomial distribution is $f(k;r,p)\equiv \Pr(X=k)={\binom {k+r-1}{k}}(1-p)^{k}p^{r}$ where r is the number of successes, *X* = *k* is the number of failures before the r-th success, and p is the probability of success on each trial.

Here, the quantity in parentheses is the binomial coefficient, and is equal to ${\binom {k+r-1}{k}}={\frac {(k+r-1)!}{(r-1)!\,k!}}={\frac {(k+r-1)(k+r-2)\dotsm (r)}{k!}}={\frac {\Gamma (k+r)}{k!\ \Gamma (r)}}=\left(\!\!{r \choose k}\!\!\right).$ Note that Γ(*r*) is the Gamma function, and $\textstyle \left(\!\!{r \choose k}\!\!\right)$ is the multiset coefficient.

There are k failures chosen from *k* + *r* − 1 trials rather than *k* + *r* because the last of the *k* + *r* trials is by definition a success.

This quantity can alternatively be written in the following manner, explaining the name "negative binomial":

${\begin{aligned}&{\frac {(k+r-1)\dotsm (r)}{k!}}\\[10pt]={}&(-1)^{k}{\frac {\overbrace {(-r)(-r-1)(-r-2)\dotsm (-r-k+1)} ^{k{\text{ factors}}}}{k!}}=(-1)^{k}{\binom {-r}{{\phantom {-}}k}}.\end{aligned}}$

Note that by the last expression and the binomial series, for every 0 ≤ *p* < 1 and $q=1-p$ ,

$p^{-r}=(1-q)^{-r}=\sum _{k=0}^{\infty }{\binom {-r}{{\phantom {-}}k}}(-q)^{k}=\sum _{k=0}^{\infty }{\binom {k+r-1}{k}}q^{k}$

hence the terms of the probability mass function indeed add up to one as below. $\sum _{k=0}^{\infty }{\binom {k+r-1}{k}}\left(1-p\right)^{k}p^{r}=p^{-r}p^{r}=1$

To understand the above definition of the probability mass function, note that the probability for every specific sequence of r successes and k failures is *p**r*(1 − *p*)*k*, because the outcomes of the *k* + *r* trials are supposed to happen independently. Since the r-th success always comes last, it remains to choose the k trials with failures out of the remaining *k* + *r* − 1 trials. The above binomial coefficient, due to its combinatorial interpretation, gives precisely the number of all these sequences of length *k* + *r* − 1.

An alternate interpretation of the probability mass function's binomial coefficient arises when considering the equivalent multiset coefficient $\textstyle \left(\!\!{r \choose k}\!\!\right)$ . A sequence of trials ending in r successes can be represented by a tuple of r non-negative integers, where each integer represents the number of failures seen before the next success. Then by applying stars and bars, it can be seen that the number of such tuples that sum to k (and hence represent k total failures and r total successes) is given by $\textstyle \left(\!\!{r \choose k}\!\!\right)$ .

### Cumulative distribution function

The cumulative distribution function can be expressed in terms of the regularized incomplete beta function: $F(k;r,p)\equiv \Pr(X\leq k)=I_{p}(r,k+1).$ (This formula is using the same parameterization as in the article's table, with r the number of successes, and $p=r/(r+\mu )$ with $\mu$ the mean.)

It can also be expressed in terms of the cumulative distribution function of the binomial distribution: $F(k;r,p)=F_{\text{binomial}}(k;n=k+r,1-p).$

### Alternative formulations

Some sources may define the negative binomial distribution slightly differently from the primary one here. The most common variations are where the random variable X is counting different things. These variations can be seen in the table here:

|   | X is counting... | Probability mass function | Formula | Alternate formula (using equivalent binomial) | Alternate formula (simplified using: ${\textstyle n=k+r}$ ) | Support |
|---|---|---|---|---|---|---|
| 1 | k failures, given r successes | ${\textstyle f(k;r,p)\equiv \Pr(X=k)=}$ | ${\textstyle {\binom {k+r-1}{k}}p^{r}(1-p)^{k}}$ | ${\textstyle {\binom {k+r-1}{r-1}}p^{r}(1-p)^{k}}$ | ${\textstyle {\binom {n-1}{k}}p^{r}(1-p)^{k}}$ | ${\text{for }}k=0,1,2,\ldots$ |
| 2 | n trials, given r successes | ${\textstyle f(n;r,p)\equiv \Pr(X=n)=}$ | ${\textstyle {\binom {n-1}{r-1}}p^{r}(1-p)^{n-r}}$ | ${\textstyle {\binom {n-1}{n-r}}p^{r}(1-p)^{n-r}}$ | ${\text{for }}n=r,r+1,r+2,\dotsc$ |   |
| 3 | n trials, given r failures | ${\textstyle f(n;r,p)\equiv \Pr(X=n)=}$ | ${\textstyle {\binom {n-1}{r-1}}p^{n-r}(1-p)^{r}}$ | ${\textstyle {\binom {n-1}{n-r}}p^{n-r}(1-p)^{r}}$ | ${\textstyle {\binom {n-1}{k}}p^{k}(1-p)^{r}}$ |   |
| 4 | k successes, given r failures | ${\textstyle f(k;r,p)\equiv \Pr(X=k)=}$ | ${\textstyle {\binom {k+r-1}{k}}p^{k}(1-p)^{r}}$ | ${\textstyle {\binom {k+r-1}{r-1}}p^{k}(1-p)^{r}}$ | ${\text{for }}k=0,1,2,\ldots$ |   |
| - | k successes, given n trials | ${\textstyle f(k;n,p)\equiv \Pr(X=k)=}$ | This is the binomial distribution not the negative binomial: ${\textstyle {\binom {n}{k}}p^{k}(1-p)^{n-k}={\binom {n}{n-k}}p^{k}(1-p)^{n-k}={\binom {n}{k}}p^{k}(1-p)^{r}}$ | ${\text{for }}k=0,1,2,\dotsc ,n$ |   |   |

Each of the four definitions of the negative binomial distribution can be expressed in slightly different but equivalent ways. The first alternative formulation is simply an equivalent form of the binomial coefficient, that is: ${\textstyle {\binom {a}{b}}={\binom {a}{a-b}}\quad {\text{for }}\ 0\leq b\leq a}$ . The second alternate formulation somewhat simplifies the expression by recognizing that the total number of trials is simply the number of successes and failures, that is: ${\textstyle n=r+k}$ . These second formulations may be more intuitive to understand, however they are perhaps less practical as they have more terms.

- The definition where X is the number of n **trials** that occur for a given number of r **successes** is similar to the primary definition, except that the number of trials is given instead of the number of failures. This adds r to the value of the random variable, shifting its support and mean.
- The definition where X is the number of k **successes** (or n **trials**) that occur for a given number of r **failures** is similar to the primary definition used in this article, except that numbers of failures and successes are switched when considering what is being counted and what is given. Note however, that p still refers to the probability of "success".
- The definition of the negative binomial distribution can be extended to the case where the parameter r can take on a positive real value. Although it is impossible to visualize a non-integer number of "failures", we can still formally define the distribution through its probability mass function. The problem of extending the definition to real-valued (positive) r boils down to extending the binomial coefficient to its real-valued counterpart, based on the gamma function: ${\binom {k+r-1}{k}}={\frac {(k+r-1)(k+r-2)\dotsm (r)}{k!}}={\frac {\Gamma (k+r)}{k!\,\Gamma (r)}}$ After substituting this expression in the original definition, we say that X has a negative binomial (or **Pólya**) distribution if it has a probability mass function: $f(k;r,p)\equiv \Pr(X=k)={\frac {\Gamma (k+r)}{k!\,\Gamma (r)}}(1-p)^{k}p^{r}\quad {\text{for }}k=0,1,2,\dotsc$ Here r is a real, positive number.

In negative binomial regression, the distribution is specified in terms of its mean, ${\textstyle m={\frac {r(1-p)}{p}}}$ , which is then related to explanatory variables as in linear regression or other generalized linear models. From the expression for the mean m, one can derive ${\textstyle p={\frac {r}{m+r}}}$ and ${\textstyle 1-p={\frac {m}{m+r}}}$ . Then, substituting these expressions in the one for the probability mass function when r is real-valued, yields this parametrization of the probability mass function in terms of m:

$\Pr(X=k)={\frac {\Gamma (r+k)}{k!\,\Gamma (r)}}\left({\frac {r}{r+m}}\right)^{r}\left({\frac {m}{r+m}}\right)^{k}\quad {\text{for }}k=0,1,2,\dotsc$ The variance can then be written as ${\textstyle m+{\frac {m^{2}}{r}}}$ . Some authors prefer to set ${\textstyle \alpha ={\frac {1}{r}}}$ , and express the variance as ${\textstyle m+\alpha m^{2}}$ . In this context, and depending on the author, either the parameter r or its reciprocal α is referred to as the "dispersion parameter", "shape parameter" or "clustering coefficient", or the "heterogeneity" or "aggregation" parameter. The term "aggregation" is particularly used in ecology when describing counts of individual organisms. Decrease of the aggregation parameter r towards zero corresponds to increasing aggregation of the organisms; increase of r towards infinity corresponds to absence of aggregation, as can be described by Poisson regression.

### Alternative parameterizations

Sometimes the distribution is parameterized in terms of its mean μ and variance *σ*2: ${\begin{aligned}&p={\frac {\mu }{\sigma ^{2}}},\\[6pt]&r={\frac {\mu ^{2}}{\sigma ^{2}-\mu }},\\[3pt]&\Pr(X=k)={k+{\frac {\mu ^{2}}{\sigma ^{2}-\mu }}-1 \choose k}\left(1-{\frac {\mu }{\sigma ^{2}}}\right)^{k}\left({\frac {\mu }{\sigma ^{2}}}\right)^{\mu ^{2}/(\sigma ^{2}-\mu )}\\&\operatorname {E} (X)=\mu \\&\operatorname {Var} (X)=\sigma ^{2}.\end{aligned}}$

Another popular parameterization uses r and the failure odds β: ${\begin{aligned}&p={\frac {1}{1+\beta }}\\&\Pr(X=k)={k+r-1 \choose k}\left({\frac {\beta }{1+\beta }}\right)^{k}\left({\frac {1}{1+\beta }}\right)^{r}\\&\operatorname {E} (X)=r\beta \\&\operatorname {Var} (X)=r\beta (1+\beta ).\end{aligned}}$

### Examples

#### Length of hospital stay

Hospital length of stay is an example of real-world data that can be modelled well with a negative binomial distribution via negative binomial regression.

#### Selling candy

Pat Collis is required to sell candy bars to raise money for the 6th grade field trip. Pat is (somewhat harshly) not supposed to return home until five candy bars have been sold. So the child goes door to door, selling candy bars. At each house, there is a 0.6 probability of selling one candy bar and a 0.4 probability of selling nothing.

*What's the probability of selling the last candy bar at the* n-th *house?*

Successfully selling candy enough times is what defines our stopping criterion (as opposed to failing to sell it), so k in this case represents the number of failures and r represents the number of successes. Recall that the NB(*r*, *p*) distribution describes the probability of k failures and r successes in *k* + *r* Bernoulli(*p*) trials with success on the last trial. Selling five candy bars means getting five successes. The number of trials (i.e. houses) this takes is therefore *k* + 5 = *n*. The random variable we are interested in is the number of houses, so we substitute *k* = *n* − 5 into a NB(5, 0.4) mass function and obtain the following mass function of the distribution of houses (for *n* ≥ 5):

$f(n)={\binom {(n-5)+5-1}{n-5}}\;(1-0.4)^{5}\;0.4^{n-5}={n-1 \choose n-5}\;3^{5}\;{\frac {2^{n-5}}{5^{n}}}.$

*What's the probability that Pat finishes on the tenth house?*

$f(10)={\frac {979776}{9765625}}\approx 0.10033.\,$

*What's the probability that Pat finishes on or before reaching the eighth house?*

To finish on or before the eighth house, Pat must finish at the fifth, sixth, seventh, or eighth house. Sum those probabilities: ${\begin{aligned}f(5)&={\frac {243}{3125}}\approx 0.07776\\f(6)&={\frac {486}{3125}}\approx 0.15552\\f(7)&={\frac {2916}{15625}}\approx 0.18662\\f(8)&={\frac {13608}{78125}}\approx 0.17418\end{aligned}}$ $\sum _{j=5}^{8}f(j)={\frac {46413}{78125}}\approx 0.59409.$

*What's the probability that Pat exhausts all 30 houses that happen to stand in the neighborhood?*

This can be expressed as the probability that Pat does not finish on the fifth through the thirtieth house: $1-\sum _{j=5}^{30}f(j)=1-I_{0.4}(5,30-5+1)\approx 1-0.999999823=0.000000177.$

Because of the rather high probability that Pat will sell to each house (60 percent), the probability of her *not* fulfilling her quest is vanishingly slim.

## Properties

### Expectation

The expected total number of trials needed to see r successes is ${\frac {r}{p}}$ . Thus, the expected number of *failures* would be this value, minus the successes: $\operatorname {E} [\operatorname {NB} (r,p)]={\frac {r}{p}}-r={\frac {r(1-p)}{p}}$

### Expectation of successes

The expected total number of failures in a negative binomial distribution with parameters (*r*, *p*) is *r*(1 − *p*)/*p*. To see this, imagine an experiment simulating the negative binomial is performed many times. That is, a set of trials is performed until r successes are obtained, then another set of trials, and then another etc. Write down the number of trials performed in each experiment: *a*, *b*, *c*, ... and set *a* + *b* + *c* + ... = *N*. Now we would expect about *Np* successes in total. Say the experiment was performed n times. Then there are *nr* successes in total. So we would expect *nr* = *Np*, so *N*/*n* = *r*/*p*. See that *N*/*n* is just the average number of trials per experiment. That is what we mean by "expectation". The average number of failures per experiment is *N*/*n* − *r* = *r*/*p* − *r* = *r*(1 − *p*)/*p*. This agrees with the mean given in the box on the right-hand side of this page.

A rigorous derivation can be done by representing the negative binomial distribution as the sum of waiting times. Let $X_{r}\sim \operatorname {NB} (r,p)$ with the convention X represents the number of failures observed before r successes with the probability of success being p . And let $Y_{i}\sim \mathrm {Geom} (p)$ where $Y_{i}$ represents the number of failures before seeing a success. We can think of $Y_{i}$ as the waiting time (number of failures) between the i th and $(i-1)$ th success. Thus $X_{r}=Y_{1}+Y_{2}+\cdots +Y_{r}.$ The mean is $\operatorname {E} [X_{r}]=\operatorname {E} [Y_{1}]+\operatorname {E} [Y_{2}]+\cdots +\operatorname {E} [Y_{r}]={\frac {r(1-p)}{p}},$ which follows from the fact $\operatorname {E} [Y_{i}]=(1-p)/p$ .

### Variance

When counting the number of failures before the r-th success, the variance is *r*(1 − *p*)/*p*2. When counting the number of successes before the r-th failure, as in alternative formulation (3) above, the variance is *rp*/(1 − *p*)2.

### Relation to the binomial theorem

Suppose Y is a random variable with a binomial distribution with parameters n and p. Assume *p* + *q* = 1, with *p*, *q* ≥ 0, then

$1=1^{n}=(p+q)^{n}.$

Using Newton's binomial theorem, this can equally be written as:

$(p+q)^{n}=\sum _{k=0}^{\infty }{\binom {n}{k}}p^{k}q^{n-k},$

in which the upper bound of summation is infinite. In this case, the binomial coefficient

${\binom {n}{k}}={n(n-1)(n-2)\cdots (n-k+1) \over k!}.$

is defined when n is a real number, instead of just a positive integer. But in our case of the binomial distribution it is zero when *k* > *n*. We can then say, for example

$(p+q)^{8.3}=\sum _{k=0}^{\infty }{\binom {8.3}{k}}p^{k}q^{8.3-k}.$

Now suppose *r* > 0 and we use a negative exponent:

$1=p^{r}\cdot p^{-r}=p^{r}(1-q)^{-r}=p^{r}\sum _{k=0}^{\infty }{\binom {-r}{k}}(-q)^{k}.$

Then all of the terms are positive, and the term

$p^{r}{\binom {-r}{k}}(-q)^{k}={\binom {k+r-1}{k}}p^{r}q^{k}$

is just the probability that the number of failures before the r-th success is equal to k, provided r is an integer. (If r is a negative non-integer, so that the exponent is a positive non-integer, then some of the terms in the sum above are negative, so we do not have a probability distribution on the set of all nonnegative integers.)

Now we also allow non-integer values of r.

Recall from above that

The sum of independent negative-binomially distributed random variables

r

1

and

r

2

with the same value for parameter

p

is negative-binomially distributed with the same

p

but with

r

-value

r

1

+

r

2

.

This property persists when the definition is thus generalized, and affords a quick way to see that the negative binomial distribution is infinitely divisible.

### Recurrence relations

The following recurrence relations hold:

For the probability mass function ${\begin{cases}(k+1)\Pr(X=k+1)-(1-p)\Pr(X=k)(k+r)=0,\\[5pt]\Pr(X=0)=(1-p)^{r}.\end{cases}}$

For the moments $m_{k}=\mathbb {E} (X^{k}),$ $m_{k+1}=rPm_{k}+(P^{2}+P){dm_{k} \over dP},\quad P:=(1-p)/p,\quad m_{0}=1.$

For the cumulants $\kappa _{k+1}=(Q-1)Q{d\kappa _{k} \over dQ},\quad Q:=1/p,\quad \kappa _{1}=r(Q-1).$

- The geometric distribution on {0, 1, 2, 3, ... } is a special case of the negative binomial distribution, with $\operatorname {Geom} (p)=\operatorname {NB} (1,\,p).\,$
- The negative binomial distribution is a special case of the discrete phase-type distribution.
- The negative binomial distribution is a special case of discrete compound Poisson distribution.

### Poisson distribution

Consider a sequence of negative binomial random variables where the stopping parameter r goes to infinity, while the probability p of success in each trial goes to one, in such a way as to keep the mean of the distribution (i.e. the expected number of failures) constant. Denoting this mean as λ, the parameter p will be *p* = *r*/(*r* + *λ*) ${\begin{aligned}{\text{Mean:}}\quad &\lambda ={\frac {(1-p)r}{p}}\quad \Rightarrow \quad p={\frac {r}{r+\lambda }},\\{\text{Variance:}}\quad &\lambda \left(1+{\frac {\lambda }{r}}\right)>\lambda ,\quad {\text{thus always overdispersed}}.\end{aligned}}$

Under this parametrization the probability mass function will be $f(k;r,p)={\frac {\Gamma (k+r)}{k!\cdot \Gamma (r)}}(1-p)^{k}p^{r}={\frac {\lambda ^{k}}{k!}}\cdot {\frac {\Gamma (r+k)}{\Gamma (r)\;(r+\lambda )^{k}}}\cdot {\frac {1}{\left(1+{\frac {\lambda }{r}}\right)^{r}}}$

Now if we consider the limit as *r* → ∞, the second factor will converge to one, and the third to the exponent function: $\lim _{r\to \infty }f(k;r,p)={\frac {\lambda ^{k}}{k!}}\cdot 1\cdot {\frac {1}{e^{\lambda }}},$ which is the mass function of a Poisson-distributed random variable with expected value λ.

In other words, the alternatively parameterized negative binomial distribution converges to the Poisson distribution and r controls the deviation from the Poisson. This makes the negative binomial distribution suitable as a robust alternative to the Poisson, which approaches the Poisson for large r, but which has larger variance than the Poisson for small r. $\operatorname {Poisson} (\lambda )=\lim _{r\to \infty }\operatorname {NB} \left(r,{\frac {r}{r+\lambda }}\right).$

### Gamma–Poisson mixture

The negative binomial distribution also arises as a continuous mixture of Poisson distributions (i.e. a compound probability distribution) where the mixing distribution of the Poisson rate is a gamma distribution. That is, we can view the negative binomial as a Poisson(*λ*) distribution, where λ is itself a random variable, distributed as a gamma distribution with shape r and scale *θ* = (1 − *p*)/*p* or correspondingly rate *β* = *p*/(1 − *p*).

To display the intuition behind this statement, consider two independent Poisson processes, "Success" and "Failure", with intensities p and 1 − *p*. Together, the Success and Failure processes are equivalent to a single Poisson process of intensity 1, where an occurrence of the process is a success if a corresponding independent coin toss comes up heads with probability p; otherwise, it is a failure. If r is a counting number, the coin tosses show that the count of successes before the r-th failure follows a negative binomial distribution with parameters r and 1 − *p*. The count is also, however, the count of the Success Poisson process at the random time T of the r-th occurrence in the Failure Poisson process. The Success count follows a Poisson distribution with mean *pT*, where T is the waiting time for r occurrences in a Poisson process of intensity 1 − *p*, i.e., T is gamma-distributed with shape parameter r and intensity 1 − *p*. Thus, the negative binomial distribution is equivalent to a Poisson distribution with mean *pT*, where the random variate T is gamma-distributed with shape parameter r and intensity (1 − *p*). The preceding paragraph follows, because *λ* = *pT* is gamma-distributed with shape parameter r and intensity (1 − *p*)/*p*.

The following formal derivation (which does not depend on r being a counting number) confirms the intuition.

${\begin{aligned}&\int _{0}^{\infty }f_{\operatorname {Poisson} (\lambda )}(k)\times f_{\operatorname {Gamma} \left(r,\,{\frac {p}{1-p}}\right)}(\lambda )\,\mathrm {d} \lambda \\[8pt]={}&\int _{0}^{\infty }{\frac {\lambda ^{k}}{k!}}e^{-\lambda }\times {\frac {1}{\Gamma (r)}}\left({\frac {p}{1-p}}\lambda \right)^{r-1}e^{-{\frac {p}{1-p}}\lambda }\,\left({\frac {p}{1-p}}\,\right)\mathrm {d} \lambda \\[8pt]={}&\left({\frac {p}{1-p}}\right)^{r}{\frac {1}{k!\,\Gamma (r)}}\int _{0}^{\infty }\lambda ^{r+k-1}e^{-\lambda {\frac {p+1-p}{1-p}}}\;\mathrm {d} \lambda \\[8pt]={}&\left({\frac {p}{1-p}}\right)^{r}{\frac {1}{k!\,\Gamma (r)}}\Gamma (r+k)(1-p)^{k+r}\int _{0}^{\infty }f_{\operatorname {Gamma} \left(k+r,{\frac {1}{1-p}}\right)}(\lambda )\;\mathrm {d} \lambda \\[8pt]={}&{\frac {\Gamma (r+k)}{k!\;\Gamma (r)}}\;(1-p)^{k}\,p^{r}\\[8pt]={}&f(k;r,p).\end{aligned}}$

Because of this, the negative binomial distribution is also known as the **gamma–Poisson (mixture) distribution**. The negative binomial distribution was originally derived as a limiting case of the gamma-Poisson distribution.

### Distribution of a sum of geometrically distributed random variables

If *Y**r* is a random variable following the negative binomial distribution with parameters r and p, and support {0, 1, 2, ...}, then *Y**r* is a sum of r independent variables following the geometric distribution (on {0, 1, 2, ...}) with parameter p. As a result of the central limit theorem, *Y**r* (properly scaled and shifted) is therefore approximately normal for sufficiently large r.

Furthermore, if *B**s*+*r* is a random variable following the binomial distribution with parameters *s* + *r* and p, then

${\begin{aligned}\Pr(Y_{r}\leq s)&{}=1-I_{p}(s+1,r)\\[5pt]&{}=1-I_{p}((s+r)-(r-1),(r-1)+1)\\[5pt]&{}=1-\Pr(B_{s+r}\leq r-1)\\[5pt]&{}=\Pr(B_{s+r}\geq r)\\[5pt]&{}=\Pr({\text{after }}s+r{\text{ trials, there are at least }}r{\text{ successes}}).\end{aligned}}$

In this sense, the negative binomial distribution is the "inverse" of the binomial distribution.

The sum of independent negative-binomially distributed random variables *r*1 and *r*2 with the same value for parameter p is negative-binomially distributed with the same p but with r-value *r*1 + *r*2.

The negative binomial distribution is infinitely divisible, i.e., if Y has a negative binomial distribution, then for any positive integer n, there exist independent identically distributed random variables *Y*1, ..., *Y**n* whose sum has the same distribution that Y has.

### Representation as compound Poisson distribution

The negative binomial distribution NB(*r*, *p*) can be represented as a compound Poisson distribution: Let ${\textstyle (Y_{n})_{n\,\in \,\mathbb {N} }}$ denote a sequence of independent and identically distributed random variables, each one having the logarithmic series distribution Log(*p*), with probability mass function

$f(k;r,p)={\frac {-p^{k}}{k\ln(1-p)}},\qquad k\in {\mathbb {N} }.$

Let N be a random variable, independent of the sequence, and suppose that N has a Poisson distribution with mean λ = −*r* ln(1 − *p*). Then the random sum

$X=\sum _{n=1}^{N}Y_{n}$

is NB(*r*, *p*)-distributed. To prove this, we calculate the probability generating function *G**X* of X, which is the composition of the probability generating functions *G**N* and *G**Y*1. Using

$G_{N}(z)=\exp(\lambda (z-1)),\qquad z\in \mathbb {R} ,$

and

$G_{Y_{1}}(z)={\frac {\ln(1-pz)}{\ln(1-p)}},\qquad |z|<{\frac {1}{p}},$

we obtain

${\begin{aligned}G_{X}(z)&=G_{N}(G_{Y_{1}}(z))\\[4pt]&=\exp \left[\lambda \left({\frac {\ln(1-pz)}{\ln(1-p)}}-1\right)\right]\\[1ex]&=\exp \left[-r\left(\ln(1-pz)-\ln(1-p)\right)\right]\\[1ex]&=\left({\frac {1-p}{1-pz}}\right)^{r},\qquad |z|<{\frac {1}{p}},\end{aligned}}$

which is the probability generating function of the NB(*r*, *p*) distribution. This last expression can be written as ⁠ $C(1-pz)^{-r}$ ⁠ for a constant C. The name "negative binomial distribution" is reflected in this binomial ⁠ $(1-pz)$ ⁠ with a negative term being raised to a negative power ⁠ $-r$ ⁠.

The following table describes four distributions related to the number of successes in a sequence of draws:

|   | With replacements | No replacements |
|---|---|---|
| Given number of draws | binomial distribution | hypergeometric distribution |
| Given number of failures | negative binomial distribution | negative hypergeometric distribution |

### (*a*,*b*,0) class of distributions

The negative binomial, along with the Poisson and binomial distributions, is a member of the (*a*, *b*, 0) class of distributions. All three of these distributions are special cases of the Panjer distribution. They are also members of a natural exponential family.

## Statistical inference

### Parameter estimation

#### MVUE for *p*

Suppose p is unknown and an experiment is conducted where it is decided ahead of time that sampling will continue until r successes are found. A sufficient statistic for the experiment is k, the number of failures.

In estimating p, the minimum variance unbiased estimator is

${\widehat {p}}={\frac {r-1}{r+k-1}}.$

#### Maximum likelihood estimation

When r is known, the maximum likelihood estimate of p is

${\widetilde {p}}={\frac {r}{r+k}},$

but this is a biased estimate. Its inverse (*r* + *k*)/*r*, is an unbiased estimate of 1/*p*, however.

When r is unknown, the maximum likelihood estimator for p and r together only exists for samples for which the sample variance is larger than the sample mean. The likelihood function for N iid observations (*k*1, ..., *k**N*) is

$L(r,p)=\prod _{i=1}^{N}f(k_{i};r,p)\,\!$

from which we calculate the log-likelihood function

$\ell (r,p)=\sum _{i=1}^{N}\left[\ln \Gamma (k_{i}+r)-\ln(k_{i}!)+k_{i}\ln(1-p)\right]+N\left[r\ln p-\ln \Gamma (r)\right].$

To find the maximum we take the partial derivatives with respect to r and p and set them equal to zero:

${\frac {\partial \ell (r,p)}{\partial p}}=-\left[\sum _{i=1}^{N}k_{i}{\frac {1}{1-p}}\right]+Nr{\frac {1}{p}}=0$ and

${\frac {\partial \ell (r,p)}{\partial r}}=\left[\sum _{i=1}^{N}\psi (k_{i}+r)\right]-N\psi (r)+N\ln(p)=0$

where

$\psi (k)={\frac {\Gamma '(k)}{\Gamma (k)}}\!$ is the digamma function.

Solving the first equation for p gives:

$p={\frac {Nr}{Nr+\sum _{i=1}^{N}k_{i}}}$

Substituting this in the second equation gives:

${\frac {\partial \ell (r,p)}{\partial r}}=\left[\sum _{i=1}^{N}\psi (k_{i}+r)\right]-N\psi (r)+N\ln \left({\frac {r}{r+\sum _{i=1}^{N}k_{i}/N}}\right)=0$

This equation cannot be solved for r in closed form. If a numerical solution is desired, an iterative technique such as Newton's method can be used. Alternatively, the expectation–maximization algorithm can be used.

## Occurrence and applications

### Waiting time in a Bernoulli process

Let k and r be integers with k non-negative and r positive. In a sequence of independent Bernoulli trials with success probability p, the negative binomial gives the probability of k successes and r failures, with a failure on the last trial. Therefore, the negative binomial distribution represents the probability distribution of the number of successes before the r-th failure in a Bernoulli process, with probability p of successes on each trial.

Consider the following example. Suppose we repeatedly throw a die, and consider a 1 to be a failure. The probability of success on each trial is 5/6. The number of successes before the third failure belongs to the infinite set { 0, 1, 2, 3, ... }. That number of successes is a negative-binomially distributed random variable.

When *r* = 1 we get the probability distribution of number of successes before the first failure (i.e. the probability of the first failure occurring on the (*k* + 1)-st trial), which is a geometric distribution: $f(k;r,p)=(1-p)\cdot p^{k}$

### Overdispersed Poisson

The negative binomial distribution, especially in its alternative parameterization described above, can be used as an alternative to the Poisson distribution. It is especially useful for discrete data over an unbounded positive range whose sample variance exceeds the sample mean. In such cases, the observations are overdispersed with respect to a Poisson distribution, for which the mean is equal to the variance. Hence a Poisson distribution is not an appropriate model. Since the negative binomial distribution has one more parameter than the Poisson, the second parameter can be used to adjust the variance independently of the mean. See Cumulants of some discrete probability distributions.

An application of this is to annual counts of tropical cyclones in the North Atlantic or to monthly to 6-monthly counts of wintertime extratropical cyclones over Europe, for which the variance is greater than the mean. In the case of modest overdispersion, this may produce substantially similar results to an overdispersed Poisson distribution.

Negative binomial modeling is widely employed in ecology and biodiversity research for analyzing count data where overdispersion is very common. This is because overdispersion is indicative of biological aggregation, such as species or communities forming clusters. Ignoring overdispersion can lead to significantly inflated model parameters, resulting in misleading statistical inferences. The negative binomial distribution effectively addresses overdispersed counts by permitting the variance to vary quadratically with the mean. An additional dispersion parameter governs the slope of the quadratic term, determining the severity of overdispersion. The model's quadratic mean-variance relationship proves to be a realistic approach for handling overdispersion, as supported by empirical evidence from many studies. Overall, the NB model offers two attractive features: (1) the convenient interpretation of the dispersion parameter as an index of clustering or aggregation, and (2) its tractable form, featuring a closed expression for the probability mass function.

In genetics, the negative binomial distribution is commonly used to model data in the form of discrete sequence read counts from high-throughput RNA and DNA sequencing experiments.

In epidemiology of infectious diseases, the negative binomial has been used as a better option than the Poisson distribution to model overdispersed counts of secondary infections from one infected case (super-spreading events).

### Multiplicity observations (physics)

The negative binomial distribution has been the most effective statistical model for a broad range of multiplicity observations in particle collision experiments, e.g., $p{\bar {p}},\ hh,\ hA,\ AA,\ e^{+}e^{-}$ (See for an overview), and is argued to be a scale-invariant property of matter, providing the best fit for astronomical observations, where it predicts the number of galaxies in a region of space. The phenomenological justification for the effectiveness of the negative binomial distribution in these contexts remained unknown for fifty years, since their first observation in 1973. In 2023, a proof from first principles was eventually demonstrated by Scott V. Tezlaf, where it was shown that the negative binomial distribution emerges from symmetries in the dynamical equations of a canonical ensemble of particles in Minkowski space. Roughly, given an expected number of trials $\langle n\rangle$ and expected number of successes $\langle r\rangle$ , where

${\begin{aligned}\langle {\mathcal {n}}\rangle -\langle r\rangle &=k,&\langle p\rangle &={\frac {\langle r\rangle }{\langle {\mathcal {n}}\rangle }}\\[1ex]\implies \langle {\mathcal {n}}\rangle &={\frac {k}{1-\langle p\rangle }},&\langle {r}\rangle &={\frac {k\langle p\rangle }{1-\langle p\rangle }},\end{aligned}}$

an isomorphic set of equations can be identified with the parameters of a relativistic current density of a canonical ensemble of massive particles, via

${\begin{aligned}c^{2}\left\langle \rho ^{2}\right\rangle -\left\langle j^{2}\right\rangle &=c^{2}\rho _{0}^{2},&\left\langle \beta _{v}^{2}\right\rangle &={\frac {\left\langle j^{2}\right\rangle }{c^{2}\langle \rho ^{2}\rangle }}\\[1ex]\implies c^{2}\left\langle \rho ^{2}\right\rangle &={\frac {c^{2}\rho _{0}^{2}}{1-\left\langle \beta _{v}^{2}\right\rangle }},&\left\langle j^{2}\right\rangle &={\frac {c^{2}\rho _{0}^{2}\left\langle \beta _{v}^{2}\right\rangle }{1-\left\langle \beta _{v}^{2}\right\rangle }},\end{aligned}}$

where $\rho _{0}$ is the rest density, $\langle \rho ^{2}\rangle$ is the relativistic mean square density, $\langle j^{2}\rangle$ is the relativistic mean square current density, and $\langle \beta _{v}^{2}\rangle =\langle v^{2}\rangle /c^{2}$ , where $\langle v^{2}\rangle$ is the mean square speed of the particle ensemble and c is the speed of light—such that one can establish the following bijective map:

${\begin{aligned}c^{2}\rho _{0}^{2}&\mapsto k,&\langle \beta _{v}^{2}\rangle &\mapsto \langle p\rangle ,\\[1ex]c^{2}\langle \rho ^{2}\rangle &\mapsto \langle {\mathcal {n}}\rangle ,&\langle j^{2}\rangle &\mapsto \langle r\rangle .\end{aligned}}$

A rigorous alternative proof of the above correspondence has also been demonstrated through quantum mechanics via the Feynman path integral.

## History

This distribution was first studied in 1713 by Pierre Remond de Montmort in his *Essay d'analyse sur les jeux de hazard*, as the distribution of the number of trials required in an experiment to obtain a given number of successes. It had previously been mentioned by Pascal.
