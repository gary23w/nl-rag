---
title: "Normal distribution (part 1/3)"
source: https://en.wikipedia.org/wiki/Normal_distribution
domain: statistics-fundamentals
license: CC-BY-SA-4.0
tags: statistics fundamentals, probability, statistical inference, hypothesis testing, probability distribution
fetched: 2026-07-02
part: 1/3
---

# Normal distribution

In probability theory and statistics, a **normal distribution** or **Gaussian distribution** is a type of continuous probability distribution for a real-valued random variable. The general form of its probability density function is $f(x)={\frac {1}{\sqrt {2\pi \sigma ^{2}}}}\exp {\left(-{\frac {(x-\mu )^{2}}{2\sigma ^{2}}}\right)}\,.$ The parameter ⁠ $\mu$ ⁠ is the mean or expectation of the distribution (and also its median and mode), while the parameter ${\textstyle \sigma ^{2}}$ is the variance. The standard deviation of the distribution is the positive value ⁠ $\sigma$ ⁠ (sigma). A random variable with a Gaussian distribution is said to be **normally distributed** and is called a **normal deviate**.

Normal distributions are important in statistics and are often used in the natural and social sciences to represent real-valued random variables whose distributions are not known. Their importance is partly due to the central limit theorem. It states that the average of many statistically independent samples (observations) of a random variable with finite mean and variance is itself a random variable—whose distribution converges to a normal distribution as the number of samples increases. Therefore, physical quantities that are expected to be the sum of many independent processes, such as measurement errors, often have distributions that are nearly normal.

Moreover, Gaussian distributions have some unique properties that are valuable in analytic studies. For instance, any linear combination of a fixed collection of independent normal deviates is a normal deviate. Many results and methods, such as propagation of uncertainty and least squares parameter fitting, can be derived analytically in explicit form when the relevant variables are normally distributed.

A normal distribution is sometimes informally called a **bell curve**. However, many other distributions are bell-shaped (such as the Cauchy, Student's t, and logistic distributions). (For other names, see *Naming*.)

The univariate probability distribution is generalized for vectors in the multivariate normal distribution and for matrices in the matrix normal distribution.


## Definitions

### Standard normal distribution

The simplest case of a normal distribution is known as the **standard normal distribution** or **unit normal distribution**. This is a special case when ${\textstyle \mu =0}$ and ${\textstyle \sigma ^{2}=1}$ , and it is described by this probability density function (or density): $\varphi (z)={\frac {e^{-z^{2}/2}}{\sqrt {2\pi }}}\,.$ The variable ⁠ z ⁠ has a mean of 0 and a variance and standard deviation of 1. The density ${\textstyle \varphi (z)}$ has its peak value ${\textstyle {\frac {1}{\sqrt {2\pi }}}}$ at ${\textstyle z=0}$ and inflection points at ${\textstyle z=+1}$ and ⁠ $z=-1$ ⁠.

Although the density above is most commonly known as the *standard normal,* a few authors have used that term to describe other versions of the normal distribution. Carl Friedrich Gauss, for example, once defined the standard normal as ${\textstyle \varphi (z)={\frac {1}{\sqrt {\pi }}}e^{-z^{2}},}$ which has a variance of ⁠ ${\tfrac {1}{2}}$ ⁠, and Stephen Stigler once defined the standard normal as ${\textstyle \varphi (z)=e^{-\pi z^{2}},}$ which has a simple functional form and a variance of ${\textstyle \sigma ^{2}={\frac {1}{2\pi }}.}$

### General normal distribution

If ⁠ Z ⁠ is a standard normal deviate, then ${\textstyle X=\sigma Z+\mu }$ will have a normal distribution with expected value ⁠ $\mu$ ⁠ and standard deviation ⁠ $\sigma$ ⁠. This is equivalent to saying that the standard normal distribution ⁠ Z ⁠ can be scaled/stretched by a factor of ⁠ $\sigma$ ⁠ and shifted by ⁠ $\mu$ ⁠ to yield a different normal distribution, called ⁠ X ⁠.

Conversely, if ⁠ X ⁠ is a normal deviate with parameters ⁠ $\mu$ ⁠ and ${\textstyle \sigma ^{2}}$ , then this ⁠ X ⁠ distribution can be re-scaled and shifted via the formula ${\textstyle Z=(X-\mu )/\sigma }$ to convert it to the standard normal distribution. This variate is also called the standardized form of ⁠ X ⁠.

In particular, the probability density function for ⁠ X ⁠ can be written in terms of the standard normal distribution ⁠ $\varphi$ ⁠ (with zero mean and unit variance): $f(x\mid \mu ,\sigma ^{2})={\frac {1}{\sigma }}\varphi \left({\frac {x-\mu }{\sigma }}\right)\,.$ The probability density must be scaled by ${\textstyle 1/\sigma }$ so that the integral is still 1.

### Notation

The probability density function of the standard normal distribution is commonly denoted by the Greek letter phi, ⁠ $\phi$ ⁠. The variant form ⁠ $\varphi$ ⁠ is also used.

The cumulative distribution function of the standard normal distribution is commonly denoted by the capital Greek letter phi, ⁠ $\Phi$ ⁠.

The normal distribution is often referred to as ${\textstyle N(\mu ,\sigma ^{2})}$ or ⁠ ${\mathcal {N}}(\mu ,\sigma ^{2})$ ⁠. When a random variable ⁠ X ⁠ is normally distributed with mean ⁠ $\mu$ ⁠ and standard deviation ⁠ $\sigma$ ⁠, one may write

$X\sim {\mathcal {N}}(\mu ,\sigma ^{2}).$

### Alternative parameterizations

Some authors advocate using the precision ⁠ $\tau$ ⁠ as the parameter defining the width of the distribution, instead of the standard deviation ⁠ $\sigma$ ⁠ or the variance ⁠ $\sigma ^{2}$ ⁠. The precision is normally defined as the reciprocal of the variance, ⁠ $1/\sigma ^{2}$ ⁠. The formula for the distribution then becomes $f(x)={\sqrt {\frac {\tau }{2\pi }}}e^{-\tau (x-\mu )^{2}/2}.$

This choice is claimed to have advantages in numerical computations when ⁠ $\sigma$ ⁠ is very close to zero, and simplifies formulas in some contexts, such as in the Bayesian inference of variables with multivariate normal distribution.

Alternatively, the reciprocal of the standard deviation ${\textstyle \tau '=1/\sigma }$ might be defined as the *precision*, in which case the expression of the normal distribution becomes $f(x)={\frac {\tau '}{\sqrt {2\pi }}}e^{-(\tau ')^{2}(x-\mu )^{2}/2}.$

According to Stigler, this formulation is advantageous because of a much simpler and easier-to-remember formula, and simple approximate formulas for the quantiles of the distribution.

Normal distributions form an exponential family with natural parameters ${\textstyle \textstyle \theta _{1}={\frac {\mu }{\sigma ^{2}}}}$ and ${\textstyle \textstyle \theta _{2}=-{\frac {1}{2\sigma ^{2}}}}$ , and natural statistics x and *x*2. The dual expectation parameters for normal distribution are *η*1 = *μ* and *η*2 = *μ*2 + *σ*2.

### Cumulative distribution function

The cumulative distribution function (CDF) of the standard normal distribution, usually denoted with the capital Greek letter ⁠ $\Phi$ ⁠, is the integral $\Phi (x)={\frac {1}{\sqrt {2\pi }}}\int _{-\infty }^{x}e^{-t^{2}/2}\,dt\,.$

The related error function ${\textstyle \operatorname {erf} (x)}$ gives the probability of a random variable, with normal distribution of mean 0 and variance 1/2, falling in the range ⁠ $[-x,x]$ ⁠. That is: $\operatorname {erf} (x)={\frac {1}{\sqrt {\pi }}}\int _{-x}^{x}e^{-t^{2}}\,dt={\frac {2}{\sqrt {\pi }}}\int _{0}^{x}e^{-t^{2}}\,dt\,.$

These integrals cannot be expressed in terms of elementary functions, and are often said to be special functions. However, many numerical approximations are known; see below for more.

The two functions are closely related, namely $\Phi (x)={\frac {1}{2}}\left[1+\operatorname {erf} \left({\frac {x}{\sqrt {2}}}\right)\right].$

For a generic normal distribution with density ⁠ f ⁠, mean ⁠ $\mu$ ⁠ and variance ${\textstyle \sigma ^{2}}$ , the cumulative distribution function is $F(x)=\Phi {\left({\frac {x-\mu }{\sigma }}\right)}={\frac {1}{2}}\left[1+\operatorname {erf} \left({\frac {x-\mu }{\sigma {\sqrt {2}}}}\right)\right].$

The probability that x lies between a and b with a < b is therefore $\operatorname {P} (a<x\leq b)={\frac {1}{2}}\left[\operatorname {erf} \left({\frac {b-\mu }{\sigma {\sqrt {2}}}}\right)-\operatorname {erf} \left({\frac {a-\mu }{\sigma {\sqrt {2}}}}\right)\right]$

The complement of the standard normal cumulative distribution function, ${\textstyle Q(x)=1-\Phi (x)}$ , is often called the Q-function, especially in engineering texts. It gives the probability that the value of a standard normal random variable ⁠ X ⁠ will exceed ⁠ x ⁠: ⁠ $P(X>x)$ ⁠. Other definitions of the ⁠ Q ⁠-function, all of which are simple transformations of ⁠ $\Phi$ ⁠, are also used occasionally.

The graph of the standard normal cumulative distribution function ⁠ $\Phi$ ⁠ has 2-fold rotational symmetry around the point (0,1/2); that is, ⁠ $\Phi (-x)=1-\Phi (x)$ ⁠. Its antiderivative (indefinite integral) can be expressed as follows: $\int \Phi (x)\,dx=x\Phi (x)+\varphi (x)+C.$

An asymptotic expansion of the cumulative distribution function for large x can be derived using integration by parts: $\Phi (x)={\frac {1}{2}}+{\frac {1}{\sqrt {2\pi }}}e^{-x^{2}/2}\sum _{n=0}^{\infty }{\frac {1}{(2n+1)!!}}x^{2n+1}\,.$ where ${\textstyle !!}$ denotes the double factorial. For more, see Error function § Asymptotic expansion.

#### Taylor series representation

The Taylor series for the normal distribution ⁠ $\varphi$ ⁠ can be derived by substituting ⁠ $-{\tfrac {1}{2}}x^{2}$ ⁠ into the Taylor series for the exponential function:

$\varphi (x)={\frac {1}{\sqrt {2\pi }}}\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{n!\,2^{n}}}x^{2n}$

This series can be integrated term by term to obtain the Taylor series for the cumulative distribution function:

$\Phi (x)={\frac {1}{2}}+{\frac {1}{\sqrt {2\pi }}}\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{n!\,2^{n}(2n+1)}}x^{2n+1}.$ However, this series is ineffective for calculation due to slow convergence, except when ⁠ x ⁠ is small.

Both of these series describe entire functions, which converge for all real and complex values of ⁠ x ⁠.

#### Recursive computation with Taylor series

The recurrence relation for Hermite polynomials He*n*(*x*) may be used to efficiently construct the Taylor series expansion about any point *x*0: $\Phi (x)=\sum _{n=0}^{\infty }{\frac {\Phi ^{(n)}(x_{0})}{n!}}(x-x_{0})^{n}\,,$ where: ${\begin{aligned}\Phi ^{(0)}(x_{0})&={\frac {1}{\sqrt {2\pi }}}\int _{-\infty }^{x_{0}}e^{-t^{2}/2}\,dt\\\Phi ^{(1)}(x_{0})&={\frac {1}{\sqrt {2\pi }}}e^{-x_{0}^{2}/2}\\\Phi ^{(n)}(x_{0})&=-\left(x_{0}\Phi ^{(n-1)}(x_{0})+(n-2)\Phi ^{(n-2)}(x_{0})\right),&n\geq 2\,.\end{aligned}}$

#### Standard deviation and coverage

About 68% of values drawn from a normal distribution are within one standard deviation σ from the mean; about 95% of the values lie within two standard deviations; and about 99.7% are within three standard deviations. This is known as the 68–95–99.7 (empirical) rule, or the *3-sigma rule*.

More precisely, the probability that a normal deviate lies in the range between ${\textstyle \mu -n\sigma }$ and ${\textstyle \mu +n\sigma }$ is given by $F(\mu +n\sigma )-F(\mu -n\sigma )=\Phi (n)-\Phi (-n)=\operatorname {erf} \left({\frac {n}{\sqrt {2}}}\right).$ To 12 significant digits, the values for ${\textstyle n=1,2,\ldots ,6}$ are:

| ⁠ n ⁠ | ${\textstyle p=F(\mu +n\sigma )-F(\mu -n\sigma )}$ | ${\textstyle 1-p}$ | ${\textstyle {\text{or }}1{\text{ in }}(1-p)}$ | OEIS |
|---|---|---|---|---|
| 1 | 0.682689492137 | 0.317310507863 | 3 .15148718753 | OEIS: A178647 |
| 2 | 0.954499736104 | 0.045500263896 | 21 .9778945080 | OEIS: A110894 |
| 3 | 0.997300203937 | 0.002699796063 | 370 .398347345 | OEIS: A270712 |
| 4 | 0.999936657516 | 0.000063342484 | 15787 .1927673 |   |
| 5 | 0.999999426697 | 0.000000573303 | 1744277 .89362 |   |
| 6 | 0.999999998027 | 0.000000001973 | 506797345 .897 |   |

For large ⁠ n ⁠, one can use the approximation $1-p\approx {\frac {\sqrt {2}}{n{\sqrt {\pi e^{n^{2}}}}}}$

#### Quantile function

The quantile function of a distribution is the inverse of the cumulative distribution function. The quantile function of the standard normal distribution is called the probit function, and can be expressed in terms of the inverse error function: $\Phi ^{-1}(p)={\sqrt {2}}\operatorname {erf} ^{-1}(2p-1),\quad p\in (0,1).$ For a normal random variable with mean ⁠ $\mu$ ⁠ and variance ${\textstyle \sigma ^{2}}$ , the quantile function is $F^{-1}(p)=\mu +\sigma \Phi ^{-1}(p)=\mu +\sigma {\sqrt {2}}\operatorname {erf} ^{-1}(2p-1),\quad p\in (0,1).$ The quantile ${\textstyle \Phi ^{-1}(p)}$ of the standard normal distribution is commonly denoted as ⁠ $z_{p}$ ⁠. These values are used in hypothesis testing, construction of confidence intervals and Q–Q plots. A normal random variable ⁠ X ⁠ will exceed ${\textstyle \mu +z_{p}\sigma }$ with probability ${\textstyle 1-p}$ , and will lie outside the interval ${\textstyle \mu \pm z_{p}\sigma }$ with probability ⁠ $2(1-p)$ ⁠. In particular, the quantile ${\textstyle z_{0.975}}$ is 1.96; therefore a normal random variable will lie outside the interval ${\textstyle \mu \pm 1.96\sigma }$ in only 5% of cases.

The following table gives the quantile ${\textstyle z_{p}}$ such that ⁠ X ⁠ will lie in the range ${\textstyle \mu \pm z_{p}\sigma }$ with a specified probability ⁠ p ⁠. These values are useful to determine tolerance interval for sample averages and other statistical estimators with normal (or asymptotically normal) distributions. The following table shows ${\textstyle {\sqrt {2}}\operatorname {erf} ^{-1}(p)=\Phi ^{-1}\left({\frac {p+1}{2}}\right)}$ , not ${\textstyle \Phi ^{-1}(p)}$ as defined above.

| ⁠ p ⁠ | ${\textstyle z_{p}}$ |   | ⁠ p ⁠ | ${\textstyle z_{p}}$ |
|---|---|---|---|---|
| 0.80 | 1.281551565545 | 0.999 | 3.290526731492 |   |
| 0.90 | 1.644853626951 | 0.9999 | 3.890591886413 |   |
| 0.95 | 1.959963984540 | 0.99999 | 4.417173413469 |   |
| 0.98 | 2.326347874041 | 0.999999 | 4.891638475699 |   |
| 0.99 | 2.575829303549 | 0.9999999 | 5.326723886384 |   |
| 0.995 | 2.807033768344 | 0.99999999 | 5.730728868236 |   |
| 0.998 | 3.090232306168 | 0.999999999 | 6.109410204869 |   |

For small ⁠ p ⁠, the quantile function has the useful asymptotic expansion ${\textstyle \Phi ^{-1}(p)=-{\sqrt {\ln {\frac {1}{p^{2}}}-\ln \ln {\frac {1}{p^{2}}}-\ln(2\pi )}}+{\mathcal {o}}(1).}$

#### Using root finding to compute the quantile function

Any of the described approaches for computing the cumulative distribution function ${\textstyle \Phi (x)}$ can be used with Newton's method (or another root-finding algorithm such as Halley's method) to find the value of ⁠ x ⁠ for which ⁠ $\Phi (x)=q$ ⁠ for some desired quantile ⁠ q ⁠. For example, starting with an initial, approximately correct guess ⁠ $x_{0}$ ⁠, increasingly better approximations ⁠ $x_{1}$ ⁠, ⁠ $x_{2}$ ⁠, ... can be calculated iteratively using Newton's method with $x_{n}=x_{n-1}-{\frac {\Phi (x_{n-1})-q}{\varphi (x_{n-1})}}\,.$


## Properties

The normal distribution is the only distribution whose cumulants beyond the first two (i.e., other than the mean and variance) are zero. It is also the continuous distribution with the maximum entropy for a specified mean and variance. Geary has shown, assuming that the mean and variance are finite, that the normal distribution is the only distribution where the mean and variance calculated from a set of independent draws are independent of each other.

The normal distribution is a subclass of the elliptical distributions. The normal distribution is symmetric about its mean, and is non-zero over the entire real line. As such it may not be a suitable model for variables that are inherently positive or strongly skewed, such as the weight of a person or the price of a share of stock. Such variables may be better described by other distributions, such as the log-normal distribution or the Pareto distribution.

The value of the normal density is practically zero when the value ⁠ x ⁠ lies more than a few standard deviations away from the mean (e.g., a spread of three standard deviations covers all but 0.27% of the total distribution). Therefore, it may not be an appropriate model when one expects a significant fraction of outliers—values that lie many standard deviations away from the mean—and least squares and other statistical inference methods that are optimal for normally distributed variables often become highly unreliable when applied to such data. In those cases, a more heavy-tailed distribution should be assumed and appropriate robust statistical inference methods applied.

The Gaussian distribution belongs to the family of stable distributions which are the attractors of sums of independent, identically distributed distributions whether or not the mean or variance is finite. Except for the Gaussian which is a limiting case, all stable distributions have heavy tails and infinite variance. It is one of the few distributions that are stable and that have probability density functions that can be expressed analytically, the others being the Cauchy distribution and the Lévy distribution.

### Symmetries and derivatives

The normal distribution with density ${\textstyle f(x)}$ (mean ⁠ $\mu$ ⁠ and variance ${\textstyle \sigma ^{2}>0}$ ) has the following properties:

- It is symmetric around the point ${\textstyle x=\mu ,}$ which is at the same time the mode, the median and the mean of the distribution.
- It is unimodal: its first derivative is positive for ${\textstyle x<\mu ,}$ negative for ${\textstyle x>\mu ,}$ and zero only at ${\textstyle x=\mu .}$
- The area bounded by the curve and the ⁠ x ⁠-axis is unity (i.e. equal to one).
- Its first derivative is ${\textstyle f'(x)=-{\frac {x-\mu }{\sigma ^{2}}}f(x).}$
- Its second derivative is ${\textstyle f''(x)={\frac {(x-\mu )^{2}-\sigma ^{2}}{\sigma ^{4}}}f(x).}$
- Its density has two inflection points (where the second derivative of ⁠ f ⁠ is zero and changes sign), located one standard deviation away from the mean, namely at ${\textstyle x=\mu -\sigma }$ and ${\textstyle x=\mu +\sigma .}$
- Its density is log-concave.
- Its density is infinitely differentiable, indeed supersmooth of order 2.

Furthermore, the density ⁠ $\varphi$ ⁠ of the standard normal distribution (i.e. ${\textstyle \mu =0}$ and ${\textstyle \sigma =1}$ ) also has the following properties:

- Its first derivative is ${\textstyle \varphi '(x)=-x\varphi (x).}$
- Its second derivative is ${\textstyle \varphi ''(x)=(x^{2}-1)\varphi (x)}$
- More generally, its nth derivative is ${\textstyle \varphi ^{(n)}(x)=(-1)^{n}\operatorname {He} _{n}(x)\varphi (x),}$ where ${\textstyle \operatorname {He} _{n}(x)}$ is the nth (probabilist) Hermite polynomial.
- The probability that a normally distributed variable ⁠ X ⁠ with known ⁠ $\mu$ ⁠ and ${\textstyle \sigma ^{2}}$ is in a particular set, can be calculated given that the fraction ${\textstyle Z=(X-\mu )/\sigma }$ has a standard normal distribution.

### Moments

The plain and absolute moments of a variable ⁠ X ⁠ are the expected values of ${\textstyle X^{p}}$ and ${\textstyle |X|^{p}}$ , respectively. If the expected value ⁠ $\mu$ ⁠ of ⁠ X ⁠ is zero, these parameters are called *central moments;* otherwise, these parameters are called *non-central moments.* Usually we are interested only in moments with integer order ⁠ p ⁠.

If ⁠ X ⁠ has a normal distribution, the non-central moments exist and are finite for any ⁠ p ⁠ whose real part is greater than −1. For any non-negative integer ⁠ p ⁠, the plain central moments are: $\operatorname {E} \left[(X-\mu )^{p}\right]={\begin{cases}0&{\text{if }}p{\text{ is odd,}}\\\sigma ^{p}(p-1)!!&{\text{if }}p{\text{ is even.}}\end{cases}}$ Here ${\textstyle n!!}$ denotes the double factorial, that is, the product of all numbers from ⁠ n ⁠ to 1 that have the same parity as ${\textstyle n.}$

The central absolute moments coincide with plain moments for all even orders, but are nonzero for odd orders. For any non-negative integer ${\textstyle p,}$

${\begin{aligned}\operatorname {E} \left[|X-\mu |^{p}\right]&=\sigma ^{p}(p-1)!!\cdot {\begin{cases}{\sqrt {\frac {2}{\pi }}}&{\text{if }}p{\text{ is odd}}\\1&{\text{if }}p{\text{ is even}}\end{cases}}\\[8pt]&=\sigma ^{p}\cdot {\frac {2^{p/2}\Gamma \left({\frac {p+1}{2}}\right)}{\sqrt {\pi }}}.\end{aligned}}$ The last formula is valid also for any non-integer ${\textstyle p>-1.}$ When the mean ${\textstyle \mu \neq 0,}$ the plain and absolute moments can be expressed in terms of confluent hypergeometric functions ${\textstyle {}_{1}F_{1}}$ and ${\textstyle U.}$ ${\begin{aligned}\operatorname {E} \left[X^{p}\right]&=\sigma ^{p}\cdot {\left(-i{\sqrt {2}}\right)}^{p}\,U{\left(-{\frac {p}{2}},{\frac {1}{2}},-{\frac {\mu ^{2}}{2\sigma ^{2}}}\right)},\\\operatorname {E} \left[|X|^{p}\right]&=\sigma ^{p}\cdot 2^{p/2}{\frac {\Gamma {\left({\frac {1+p}{2}}\right)}}{\sqrt {\pi }}}\,{}_{1}F_{1}{\left(-{\frac {p}{2}},{\frac {1}{2}},-{\frac {\mu ^{2}}{2\sigma ^{2}}}\right)}.\end{aligned}}$

These expressions remain valid even when ⁠ $p>-1$ ⁠ is not an integer. See also generalized Hermite polynomials.

| Order | Non-central moment, $\operatorname {E} \left[X^{p}\right]$ | Central moment, $\operatorname {E} \left[(X-\mu )^{p}\right]$ |
|---|---|---|
| 0 | ⁠ 1 ⁠ | ⁠ 1 ⁠ |
| 1 | ⁠ $\mu$ ⁠ | ⁠ 0 ⁠ |
| 2 | ${\textstyle \mu ^{2}+\sigma ^{2}}$ | ${\textstyle \sigma ^{2}}$ |
| 3 | ${\textstyle \mu ^{3}+3\mu \sigma ^{2}}$ | ⁠ 0 ⁠ |
| 4 | ${\textstyle \mu ^{4}+6\mu ^{2}\sigma ^{2}+3\sigma ^{4}}$ | ${\textstyle 3\sigma ^{4}}$ |
| 5 | ${\textstyle \mu ^{5}+10\mu ^{3}\sigma ^{2}+15\mu \sigma ^{4}}$ | ⁠ 0 ⁠ |
| 6 | ${\textstyle \mu ^{6}+15\mu ^{4}\sigma ^{2}+45\mu ^{2}\sigma ^{4}+15\sigma ^{6}}$ | ${\textstyle 15\sigma ^{6}}$ |
| 7 | ${\textstyle \mu ^{7}+21\mu ^{5}\sigma ^{2}+105\mu ^{3}\sigma ^{4}+105\mu \sigma ^{6}}$ | ⁠ 0 ⁠ |
| 8 | ${\textstyle \mu ^{8}+28\mu ^{6}\sigma ^{2}+210\mu ^{4}\sigma ^{4}+420\mu ^{2}\sigma ^{6}+105\sigma ^{8}}$ | ${\textstyle 105\sigma ^{8}}$ |

The expectation of ⁠ X ⁠ conditioned on the event that ⁠ X ⁠ lies in an interval ${\textstyle [a,b]}$ is given by $\operatorname {E} \left[X\mid a<X<b\right]=\mu -\sigma ^{2}{\frac {f(b)-f(a)}{F(b)-F(a)}}\,,$ where ⁠ f ⁠ and ⁠ F ⁠ respectively are the density and the cumulative distribution function of ⁠ X ⁠. For ${\textstyle b=\infty }$ this is known as the inverse Mills ratio. Note that above, density ⁠ f ⁠ of ⁠ X ⁠ is used instead of standard normal density as in inverse Mills ratio, so here we have ${\textstyle \sigma ^{2}}$ instead of ⁠ $\sigma$ ⁠.

### Fourier transform and characteristic function

The Fourier transform of a normal density ⁠ f ⁠ with mean ⁠ $\mu$ ⁠ and variance ${\textstyle \sigma ^{2}}$ is

${\hat {f}}(t)=\int _{-\infty }^{\infty }f(x)e^{-itx}\,dx=e^{-i\mu t}e^{-{\frac {1}{2}}\sigma ^{2}t^{2}}\,,$

where ⁠ i ⁠ is the imaginary unit. If the mean ${\textstyle \mu =0}$ , the first factor is 1, and the Fourier transform is, apart from a constant factor, a normal density on the frequency domain, with mean 0 and variance ⁠ $1/\sigma ^{2}$ ⁠. In particular, the standard normal distribution ⁠ $\varphi$ ⁠ is an eigenfunction of the Fourier transform.

In probability theory, the Fourier transform of the probability distribution of a real-valued random variable ⁠ X ⁠ is closely connected to the characteristic function ${\textstyle \varphi _{X}(t)}$ of that variable, which is defined as the expected value of ${\textstyle e^{itX}}$ , as a function of the real variable ⁠ t ⁠ (the frequency parameter of the Fourier transform). This definition can be analytically extended to a complex-value variable ⁠ t ⁠. The relation between both is: $\varphi _{X}(t)={\hat {f}}(-t)\,.$

The real and imaginary parts of ${\hat {f}}(t)=\operatorname {E} [e^{-itx}]=e^{-i\mu t}e^{-{\frac {1}{2}}\sigma ^{2}t^{2}}$ give: $\operatorname {E} [\cos(tx)]=\cos(\mu t)e^{-{\frac {1}{2}}\sigma ^{2}t^{2}}$ and $\operatorname {E} [\sin(tx)]=\sin(\mu t)e^{-{\frac {1}{2}}\sigma ^{2}t^{2}}.$

Similarly, $\operatorname {E} [\cosh(tx)]=\cosh(\mu t)e^{{\frac {1}{2}}\sigma ^{2}t^{2}}$ and $\operatorname {E} [\sinh(tx)]=\sinh(\mu t)e^{{\frac {1}{2}}\sigma ^{2}t^{2}}.$

These formulas evaluated at $t=1$ give the expected value of these basic trigonometric and hyperbolic functions over a Gaussian random variable $X\sim N(\mu ,\sigma ^{2})$ , which also could be seen as consequences of the Isserlis's theorem.

### Moment- and cumulant-generating functions

The moment generating function of a real random variable ⁠ X ⁠ is the expected value of ${\textstyle e^{tX}}$ , as a function of the real parameter ⁠ t ⁠. For a normal distribution with density ⁠ f ⁠, mean ⁠ $\mu$ ⁠ and variance ${\textstyle \sigma ^{2}}$ , the moment generating function exists and is equal to

$M(t)=\operatorname {E} \left[e^{tX}\right]={\hat {f}}(it)=e^{\mu t}e^{\sigma ^{2}t^{2}/2}\,.$ For any ⁠ k ⁠, the coefficient of ⁠ $t^{k}/k!$ ⁠ in the moment generating function (expressed as an exponential power series in ⁠ t ⁠) is the normal distribution's expected value ⁠ $\operatorname {E} [X^{k}]$ ⁠.

The cumulant generating function is the logarithm of the moment generating function, namely $g(t)=\ln M(t)=\mu t+{\tfrac {1}{2}}\sigma ^{2}t^{2}\,.$

The coefficients of this exponential power series define the cumulants, but because this is a quadratic polynomial in ⁠ t ⁠, only the first two cumulants are nonzero, namely the mean ⁠ $\mu$ ⁠ and the variance ⁠ $\sigma ^{2}$ ⁠.

Some authors prefer to instead work with the characteristic function E[*e**itX*] = *e**iμt* − *σ*2*t*2/2 and ln E[*e**itX*] = *iμt* − ⁠1/2⁠*σ*2*t*2.

### Stein operator and class

Within Stein's method the Stein operator and class of a random variable ${\textstyle X\sim {\mathcal {N}}(\mu ,\sigma ^{2})}$ are ${\textstyle {\mathcal {A}}f(x)=\sigma ^{2}f'(x)-(x-\mu )f(x)}$ and ${\textstyle {\mathcal {F}}}$ the class of all absolutely continuous functions ⁠ $\textstyle f:\mathbb {R} \to \mathbb {R}$ ⁠ such that ⁠ $\operatorname {E} [\vert f'(X)\vert ]<\infty$ ⁠.

### Zero-variance limit

In the limit when ${\textstyle \sigma ^{2}}$ approaches zero, the probability density ${\textstyle f}$ approaches zero everywhere except at ${\textstyle \mu }$ , where it approaches ${\textstyle \infty }$ , while its integral remains equal to 1. An extension of the normal distribution to the case with zero variance can be defined using the Dirac delta measure ${\textstyle \delta _{\mu }}$ , although the resulting random variables are not absolutely continuous and thus do not have probability density functions. The cumulative distribution function of such a random variable is then the Heaviside step function translated by the mean ${\textstyle \mu }$ , namely $F(x)={\begin{cases}0&{\text{if }}x<\mu \\1&{\text{if }}x\geq \mu .\end{cases}}$

### Maximum entropy

Of all probability distributions over the reals with a specified finite mean ⁠ $\mu$ ⁠ and finite variance ⁠ $\sigma ^{2}$ ⁠, the normal distribution ${\textstyle N(\mu ,\sigma ^{2})}$ is the one with maximum entropy. To see this, let ⁠ X ⁠ be a continuous random variable with probability density ⁠ $f(x)$ ⁠. The entropy of ⁠ X ⁠ is defined as $H(X)=-\int _{-\infty }^{\infty }f(x)\ln f(x)\,dx\,,$ where ${\textstyle f(x)\log f(x)}$ is understood to be zero whenever ⁠ $f(x)=0$ ⁠. This functional can be maximized, subject to the constraints that the distribution is properly normalized and has a specified mean and variance, by using variational calculus. A function with three Lagrange multipliers is defined: $L=-\int _{-\infty }^{\infty }f(x)\ln f(x)\,dx-\lambda _{0}\left(1-\int _{-\infty }^{\infty }f(x)\,dx\right)-\lambda _{1}\left(\mu -\int _{-\infty }^{\infty }f(x)x\,dx\right)-\lambda _{2}\left(\sigma ^{2}-\int _{-\infty }^{\infty }f(x)(x-\mu )^{2}\,dx\right)\,.$

At maximum entropy, a small variation ${\textstyle \delta f(x)}$ about ${\textstyle f(x)}$ will produce a variation ${\textstyle \delta L}$ about ⁠ L ⁠ which is equal to 0: $0=\delta L=\int _{-\infty }^{\infty }\delta f(x)\left(-\ln f(x)-1+\lambda _{0}+\lambda _{1}x+\lambda _{2}(x-\mu )^{2}\right)\,dx\,.$

Since this must hold for any small ⁠ $\delta f(x)$ ⁠, the factor multiplying ⁠ $\delta f(x)$ ⁠ must be zero, and solving for ⁠ $f(x)$ ⁠ yields: $f(x)=\exp \left(-1+\lambda _{0}+\lambda _{1}x+\lambda _{2}(x-\mu )^{2}\right)\,.$

The Lagrange constraints that ⁠ $f(x)$ ⁠ is properly normalized and has the specified mean and variance are satisfied if and only if ⁠ $\lambda _{0}$ ⁠, ⁠ $\lambda _{1}$ ⁠, and ⁠ $\lambda _{2}$ ⁠ are chosen so that $f(x)={\frac {1}{\sqrt {2\pi \sigma ^{2}}}}e^{-{\frac {(x-\mu )^{2}}{2\sigma ^{2}}}}\,.$ The entropy of a normal distribution ${\textstyle X\sim N(\mu ,\sigma ^{2})}$ is equal to $H(X)={\tfrac {1}{2}}(1+\ln 2\sigma ^{2}\pi )\,,$ which is independent of the mean ⁠ $\mu$ ⁠.

### Other properties

1. If the characteristic function ${\textstyle \phi _{X}}$ of some random variable ⁠ X ⁠ is of the form ${\textstyle \phi _{X}(t)=\exp Q(t)}$ in a neighborhood of zero, where ${\textstyle Q(t)}$ is a polynomial, then the **Marcinkiewicz theorem** (named after Józef Marcinkiewicz) asserts that ⁠ Q ⁠ can be at most a quadratic polynomial, and therefore ⁠ X ⁠ is a normal random variable. The consequence of this result is that the normal distribution is the only distribution with a finite number (two) of non-zero cumulants.
2. If ⁠ X ⁠ and ⁠ Y ⁠ are jointly normal and uncorrelated, then they are independent. The requirement that ⁠ X ⁠ and ⁠ Y ⁠ should be *jointly* normal is essential; without it the property does not hold.[proof] For non-normal random variables uncorrelatedness does not imply independence.
3. The Kullback–Leibler divergence of one normal distribution ${\textstyle X_{1}\sim N(\mu _{1},\sigma _{1}^{2})}$ from another ${\textstyle X_{2}\sim N(\mu _{2},\sigma _{2}^{2})}$ is given by: $D_{\mathrm {KL} }(X_{1}\parallel X_{2})={\frac {(\mu _{1}-\mu _{2})^{2}}{2\sigma _{2}^{2}}}+{\frac {1}{2}}\left({\frac {\sigma _{1}^{2}}{\sigma _{2}^{2}}}-1-\ln {\frac {\sigma _{1}^{2}}{\sigma _{2}^{2}}}\right)$ The Hellinger distance between the same distributions is equal to $H^{2}(X_{1},X_{2})=1-{\sqrt {\frac {2\sigma _{1}\sigma _{2}}{\sigma _{1}^{2}+\sigma _{2}^{2}}}}\exp \left(-{\frac {1}{4}}{\frac {(\mu _{1}-\mu _{2})^{2}}{\sigma _{1}^{2}+\sigma _{2}^{2}}}\right)$
4. The Fisher information matrix for a normal distribution w.r.t. ⁠ $\mu$ ⁠ and ${\textstyle \sigma ^{2}}$ is diagonal and takes the form ${\mathcal {I}}(\mu ,\sigma ^{2})={\begin{pmatrix}{\frac {1}{\sigma ^{2}}}&0\\0&{\frac {1}{2\sigma ^{4}}}\end{pmatrix}}$
5. The conjugate prior of the mean of a normal distribution is another normal distribution. Specifically, if ${\textstyle x_{1},\ldots ,x_{n}}$ are iid ${\textstyle \sim N(\mu ,\sigma ^{2})}$ and the prior is ${\textstyle \mu \sim N(\mu _{0},\sigma _{0}^{2})}$ , then the posterior distribution for the estimator of ⁠ $\mu$ ⁠ will be $\mu \mid x_{1},\ldots ,x_{n}\sim {\mathcal {N}}\left({\frac {{\frac {\sigma ^{2}}{n}}\mu _{0}+\sigma _{0}^{2}{\bar {x}}}{{\frac {\sigma ^{2}}{n}}+\sigma _{0}^{2}}},\left({\frac {n}{\sigma ^{2}}}+{\frac {1}{\sigma _{0}^{2}}}\right)^{-1}\right)$
6. The family of normal distributions not only forms an exponential family (EF), but in fact forms a natural exponential family (NEF) with quadratic variance function (NEF-QVF). Many properties of normal distributions generalize to properties of NEF-QVF distributions, NEF distributions, or EF distributions generally. NEF-QVF distributions comprises 6 families, including Poisson, Gamma, binomial, and negative binomial distributions, while many of the common families studied in probability and statistics are NEF or EF.
7. In information geometry, the family of normal distributions forms a statistical manifold with constant curvature ⁠ $-1$ ⁠. The same family is flat with respect to the (±1)-connections ${\textstyle \nabla ^{(e)}}$ and ${\textstyle \nabla ^{(m)}}$ .
8. If ${\textstyle X_{1},\dots ,X_{n}}$ are distributed according to ${\textstyle N(0,\sigma ^{2})}$ , then ${\textstyle E[\max _{i}X_{i}]\leq \sigma {\sqrt {2\ln n}}}$ . Note that there is no assumption of independence.

### Central limit theorem

The central limit theorem states that under certain (fairly common) conditions, the sum of many random variables will have an approximately normal distribution. More specifically, where ${\textstyle X_{1},\ldots ,X_{n}}$ are independent and identically distributed random variables with the same arbitrary distribution, zero mean, and variance ${\textstyle \sigma ^{2}}$ and ⁠ Z ⁠ is their mean scaled by ${\textstyle {\sqrt {n}}}$ $Z={\sqrt {n}}{\biggl (}{\frac {1}{n}}\sum _{i=1}^{n}X_{i}{\biggr )}$ Then, as ⁠ n ⁠ increases, the probability distribution of ⁠ Z ⁠ will tend to the normal distribution with zero mean and variance ⁠ $\sigma ^{2}$ ⁠.

The theorem can be extended to variables ${\textstyle (X_{i})}$ that are not independent and/or not identically distributed if certain constraints are placed on the degree of dependence and the moments of the distributions.

Many test statistics, scores, and estimators encountered in practice contain sums of certain random variables in them, and even more estimators can be represented as sums of random variables through the use of influence functions. The central limit theorem implies that those statistical parameters will have asymptotically normal distributions.

The central limit theorem also implies that certain distributions can be approximated by the normal distribution, for example:

- The binomial distribution ${\textstyle B(n,p)}$ is approximately normal with mean ${\textstyle np}$ and variance ${\textstyle np(1-p)}$ for large ⁠ n ⁠ and for ⁠ p ⁠ not too close to 0 or 1.
- The Poisson distribution with parameter ⁠ $\lambda$ ⁠ is approximately normal with mean ⁠ $\lambda$ ⁠ and variance ⁠ $\lambda$ ⁠, for large values of ⁠ $\lambda$ ⁠.
- The chi-squared distribution ${\textstyle \chi ^{2}(k)}$ is approximately normal with mean ⁠ k ⁠ and variance ${\textstyle 2k}$ , for large ⁠ k ⁠.
- The Student's t-distribution ${\textstyle t(\nu )}$ is approximately normal with mean 0 and variance 1 when ⁠ $\nu$ ⁠ is large.

Whether these approximations are sufficiently accurate depends on the purpose for which they are needed, and the rate of convergence to the normal distribution. It is typically the case that such approximations are less accurate in the tails of the distribution.

A general upper bound for the approximation error in the central limit theorem is given by the Berry–Esseen theorem, improvements of the approximation are given by the Edgeworth expansions.

This theorem can also be used to justify modeling the sum of many uniform noise sources as Gaussian noise. See AWGN.

### Operations and functions of normal variables

#### Operations on a single normal variable

If ⁠ X ⁠ is distributed normally with mean ⁠ $\mu$ ⁠ and variance ${\textstyle \sigma ^{2}}$ , then

- ${\textstyle aX+b}$ , for any real numbers ⁠ a ⁠ and ⁠ b ⁠, is also normally distributed, with mean ${\textstyle a\mu +b}$ and variance ${\textstyle a^{2}\sigma ^{2}}$ . That is, the family of normal distributions is closed under linear transformations.
- The exponential of ⁠ X ⁠ is distributed log-normally: ${\textstyle e^{X}\sim \ln(N(\mu ,\sigma ^{2}))}$ .
- The standard sigmoid of ⁠ X ⁠ is logit-normally distributed: ${\textstyle \sigma (X)\sim P({\mathcal {N}}(\mu ,\,\sigma ^{2}))}$ .
- The absolute value of ⁠ X ⁠ has folded normal distribution: ${\textstyle {\left|X\right|\sim N_{f}(\mu ,\sigma ^{2})}}$ . If ${\textstyle \mu =0}$ this is known as the half-normal distribution.
- The absolute value of normalized residuals, ${\textstyle |X-\mu |/\sigma }$ , has chi distribution with one degree of freedom: ${\textstyle |X-\mu |/\sigma \sim \chi _{1}}$ .
- The square of ${\textstyle X/\sigma }$ has the noncentral chi-squared distribution with one degree of freedom: ${\textstyle X^{2}/\sigma ^{2}\sim \chi _{1}^{2}(\mu ^{2}/\sigma ^{2})}$ . If ${\textstyle \mu =0}$ , the distribution is called simply chi-squared.
- The log-likelihood of a normal variable ⁠ x ⁠ is simply the log of its probability density function: $\ln p(x)=-{\frac {1}{2}}\left({\frac {x-\mu }{\sigma }}\right)^{2}-\ln \left(\sigma {\sqrt {2\pi }}\right).$ Since this is a scaled and shifted square of a standard normal variable, it is distributed as a scaled and shifted chi-squared variable.
- The distribution of the variable ⁠ X ⁠ restricted to an interval ${\textstyle [a,b]}$ is called the truncated normal distribution.
- ${\textstyle (X-\mu )^{-2}}$ has a Lévy distribution with location 0 and scale ${\textstyle \sigma ^{-2}}$ .

##### Operations on two independent normal variables

- If ${\textstyle X_{1}}$ and ${\textstyle X_{2}}$ are two independent normal random variables, with means ${\textstyle \mu _{1}}$ , ${\textstyle \mu _{2}}$ and variances ${\textstyle \sigma _{1}^{2}}$ , ${\textstyle \sigma _{2}^{2}}$ , then their sum ${\textstyle X_{1}+X_{2}}$ will also be normally distributed,[proof] with mean ${\textstyle \mu _{1}+\mu _{2}}$ and variance ${\textstyle \sigma _{1}^{2}+\sigma _{2}^{2}}$ .
- In particular, if ⁠ X ⁠ and ⁠ Y ⁠ are independent normal deviates with zero mean and variance ${\textstyle \sigma ^{2}}$ , then ${\textstyle X+Y}$ and ${\textstyle X-Y}$ are also independent and normally distributed, with zero mean and variance ${\textstyle 2\sigma ^{2}}$ . This is a special case of the polarization identity.
- If ${\textstyle X_{1}}$ , ${\textstyle X_{2}}$ are two independent normal deviates with mean ⁠ $\mu$ ⁠ and variance ${\textstyle \sigma ^{2}}$ , and ⁠ a ⁠, ⁠ b ⁠ are arbitrary real numbers, then the variable $X_{3}={\frac {aX_{1}+bX_{2}-(a+b)\mu }{\sqrt {a^{2}+b^{2}}}}+\mu$ is also normally distributed with mean ⁠ $\mu$ ⁠ and variance ${\textstyle \sigma ^{2}}$ . It follows that the normal distribution is stable (with exponent ${\textstyle \alpha =2}$ ).
- If ${\textstyle X_{k}\sim {\mathcal {N}}(m_{k},\sigma _{k}^{2})}$ , ${\textstyle k\in \{0,1\}}$ are normal distributions, then their normalized geometric mean ${\textstyle {\frac {1}{\int _{\mathbb {R} ^{n}}X_{0}^{\alpha }(x)X_{1}^{1-\alpha }(x)\,{\text{d}}x}}X_{0}^{\alpha }X_{1}^{1-\alpha }}$ is a normal distribution ${\textstyle {\mathcal {N}}(m_{\alpha },\sigma _{\alpha }^{2})}$ with ${\textstyle m_{\alpha }={\frac {\alpha m_{0}\sigma _{1}^{2}+(1-\alpha )m_{1}\sigma _{0}^{2}}{\alpha \sigma _{1}^{2}+(1-\alpha )\sigma _{0}^{2}}}}$ and ${\textstyle \sigma _{\alpha }^{2}={\frac {\sigma _{0}^{2}\sigma _{1}^{2}}{\alpha \sigma _{1}^{2}+(1-\alpha )\sigma _{0}^{2}}}}$ .

##### Operations on two independent standard normal variables

If ${\textstyle X_{1}}$ and ${\textstyle X_{2}}$ are two independent standard normal random variables with mean 0 and variance 1, then

- Their sum and difference is distributed normally with mean zero and variance two: ${\textstyle X_{1}\pm X_{2}\sim {\mathcal {N}}(0,2)}$ .
- Their product ${\textstyle Z=X_{1}X_{2}}$ follows the product distribution with density function ${\textstyle f_{Z}(z)=\pi ^{-1}K_{0}(|z|)}$ where ${\textstyle K_{0}}$ is the modified Bessel function of the second kind. This distribution is symmetric around zero, unbounded at ${\textstyle z=0}$ , and has the characteristic function ${\textstyle \phi _{Z}(t)=(1+t^{2})^{-1/2}}$ .
- Their ratio follows the standard Cauchy distribution: ${\textstyle X_{1}/X_{2}\sim \operatorname {Cauchy} (0,1)}$ .
- Their Euclidean norm ${\textstyle {\sqrt {X_{1}^{2}+X_{2}^{2}}}}$ has the Rayleigh distribution.

#### Operations on multiple independent normal variables

- Any linear combination of independent normal deviates is a normal deviate.
- If ${\textstyle X_{1},X_{2},\ldots ,X_{n}}$ are independent standard normal random variables, then the sum of their squares has the chi-squared distribution with ⁠ n ⁠ degrees of freedom $X_{1}^{2}+\cdots +X_{n}^{2}\sim \chi _{n}^{2}.$
- If ${\textstyle X_{1},X_{2},\ldots ,X_{n}}$ are independent normally distributed random variables with means ⁠ $\mu$ ⁠ and variances ${\textstyle \sigma ^{2}}$ , then their sample mean is independent from the sample standard deviation, which can be demonstrated using Basu's theorem or Cochran's theorem. The ratio of these two quantities will have the Student's t-distribution with ${\textstyle n-1}$ degrees of freedom: $t={\frac {{\overline {X}}-\mu }{S/{\sqrt {n}}}}={\frac {{\frac {1}{n}}(X_{1}+\cdots +X_{n})-\mu }{\sqrt {{\frac {1}{n(n-1)}}\left[(X_{1}-{\overline {X}})^{2}+\cdots +(X_{n}-{\overline {X}})^{2}\right]}}}\sim t_{n-1}.$
- If ${\textstyle X_{1},X_{2},\ldots ,X_{n}}$ , ${\textstyle Y_{1},Y_{2},\ldots ,Y_{m}}$ are independent standard normal random variables, then the ratio of their normalized sums of squares will have the F-distribution with (*n*, *m*) degrees of freedom: $F={\frac {\left(X_{1}^{2}+X_{2}^{2}+\cdots +X_{n}^{2}\right)/n}{\left(Y_{1}^{2}+Y_{2}^{2}+\cdots +Y_{m}^{2}\right)/m}}\sim F_{n,m}.$

#### Operations on multiple correlated normal variables

- A quadratic form of a normal vector, i.e. a quadratic function ${\textstyle q=\sum x_{i}^{2}+\sum x_{j}+c}$ of multiple independent or correlated normal variables, is a generalized chi-square variable.

### Operations on the density function

The split normal distribution is most directly defined in terms of joining scaled sections of the density functions of different normal distributions and rescaling the density to integrate to one. The truncated normal distribution results from rescaling a section of a single density function.

### Infinite divisibility and Cramér's theorem

For any positive integer n, any normal distribution with mean ⁠ $\mu$ ⁠ and variance ${\textstyle \sigma ^{2}}$ is the distribution of the sum of n independent normal deviates, each with mean ${\textstyle {\frac {\mu }{n}}}$ and variance ${\textstyle {\frac {\sigma ^{2}}{n}}}$ . This property is called infinite divisibility.

Conversely, if ${\textstyle X_{1}}$ and ${\textstyle X_{2}}$ are independent random variables and their sum ${\textstyle X_{1}+X_{2}}$ has a normal distribution, then both ${\textstyle X_{1}}$ and ${\textstyle X_{2}}$ must be normal deviates.

This result is known as Cramér's decomposition theorem, and is equivalent to saying that the convolution of two distributions is normal if and only if both are normal. Cramér's theorem implies that a linear combination of independent non-Gaussian variables will never have an exactly normal distribution, although it may approach it arbitrarily closely.

### The Kac–Bernstein theorem

The Kac–Bernstein theorem states that if ${\textstyle X}$ and ⁠ Y ⁠ are independent and ${\textstyle X+Y}$ and ${\textstyle X-Y}$ are also independent, then both X and Y must necessarily have normal distributions.

More generally, if ${\textstyle X_{1},\ldots ,X_{n}}$ are independent random variables, then two distinct linear combinations ${\textstyle \sum {a_{k}X_{k}}}$ and ${\textstyle \sum {b_{k}X_{k}}}$ will be independent if and only if all ${\textstyle X_{k}}$ are normal and ${\textstyle \sum {a_{k}b_{k}\sigma _{k}^{2}=0}}$ , where ${\textstyle \sigma _{k}^{2}}$ denotes the variance of ${\textstyle X_{k}}$ .

### Extensions

The notion of normal distribution, being one of the most important distributions in probability theory, has been extended far beyond the standard framework of the univariate (that is one-dimensional) case (Case 1). All these extensions are also called *normal* or *Gaussian* laws, so a certain ambiguity in names exists.

- The multivariate normal distribution describes the Gaussian law in the k-dimensional Euclidean space. A vector *X* ∈ **R***k* is multivariate-normally distributed if any linear combination of its components Σ*k* *j*=1*a**j* *X**j* has a (univariate) normal distribution. The variance of X is a *k* × *k* symmetric positive-definite matrix V. The multivariate normal distribution is a special case of the elliptical distributions. As such, its iso-density loci in the *k* = 2 case are ellipses and in the case of arbitrary k are ellipsoids.
- Rectified Gaussian distribution a rectified version of normal distribution with all the negative elements reset to 0.
- Complex normal distribution deals with the complex normal vectors. A complex vector *X* ∈ **C***k* is said to be normal if both its real and imaginary components jointly possess a 2*k*-dimensional multivariate normal distribution. The variance-covariance structure of X is described by two matrices: the **variance** matrix Γ, and the **relation** matrix C.
- Matrix normal distribution describes the case of normally distributed matrices.
- Gaussian processes are the normally distributed stochastic processes. These can be viewed as elements of some infinite-dimensional Hilbert space H, and thus are the analogues of multivariate normal vectors for the case *k* = ∞. A random element *h* ∈ *H* is said to be normal if for any constant *a* ∈ *H* the scalar product (*a*, *h*) has a (univariate) normal distribution. The variance structure of such Gaussian random element can be described in terms of the linear *covariance operator* *K*: *H* → *H*. Several Gaussian processes became popular enough to have their own names:
  - Brownian motion;
  - Brownian bridge; and
  - Ornstein–Uhlenbeck process.
- Gaussian q-distribution is an abstract mathematical construction that represents a q-analogue of the normal distribution.
- the q-Gaussian is an analogue of the Gaussian distribution, in the sense that it maximises the Tsallis entropy, and is one type of Tsallis distribution. This distribution is different from the Gaussian q-distribution above.
- The Kaniadakis κ-Gaussian distribution is a generalization of the Gaussian distribution which arises from the Kaniadakis statistics, being one of the Kaniadakis distributions.

A random variable X has a two-piece normal distribution if it has a distribution $f_{X}(x)={\begin{cases}N(\mu ,\sigma _{1}^{2}),&{\text{ if }}x\leq \mu \\N(\mu ,\sigma _{2}^{2}),&{\text{ if }}x\geq \mu \end{cases}}$ where μ is the mean and *σ*2 1  and *σ*2 2  are the variances of the distribution to the left and right of the mean respectively.

The mean E(*X*), variance V(*X*), and third central moment T(*X*) of this distribution have been determined ${\begin{aligned}\operatorname {E} (X)&=\mu +{\sqrt {\frac {2}{\pi }}}(\sigma _{2}-\sigma _{1}),\\\operatorname {V} (X)&=\left(1-{\frac {2}{\pi }}\right)(\sigma _{2}-\sigma _{1})^{2}+\sigma _{1}\sigma _{2},\\\operatorname {T} (X)&={\sqrt {\frac {2}{\pi }}}(\sigma _{2}-\sigma _{1})\left[\left({\frac {4}{\pi }}-1\right)(\sigma _{2}-\sigma _{1})^{2}+\sigma _{1}\sigma _{2}\right].\end{aligned}}$

One of the main practical uses of the Gaussian law is to model the empirical distributions of many different random variables encountered in practice. In such case a possible extension would be a richer family of distributions, having more than two parameters and therefore being able to fit the empirical distribution more accurately. The examples of such extensions are:

- Pearson distribution — a four-parameter family of probability distributions that extend the normal law to include different skewness and kurtosis values.
- The generalized normal distribution, also known as the exponential power distribution, allows for distribution tails with thicker or thinner asymptotic behaviors.
