---
title: "Laplace distribution"
source: https://en.wikipedia.org/wiki/Laplace_distribution
domain: differential-privacy-applied
license: CC-BY-SA-4.0
tags: differential privacy, local differential privacy, privacy budget epsilon, randomized response, statistical disclosure control
fetched: 2026-07-02
---

# Laplace distribution

In probability theory and statistics, the **Laplace distribution** is a continuous probability distribution named after Pierre-Simon Laplace. It is also sometimes called the **double exponential distribution**, because it can be thought of as two exponential distributions (with an additional location parameter) spliced together along the x-axis, although the term is also sometimes used to refer to the Gumbel distribution. The difference between two independent identically distributed exponential random variables is governed by a Laplace distribution, as is a Brownian motion evaluated at an exponentially distributed random time. Increments of Laplace motion or a variance gamma process evaluated over the time scale also have a Laplace distribution.

## Definitions

### Probability density function

A random variable has a $\operatorname {Laplace} (\mu ,b)$ distribution if its probability density function is

$f(x\mid \mu ,b)={\frac {1}{2b}}e^{-{\frac {|x-\mu |}{b}}},$

where $\mu$ is a location parameter, and $b>0$ , which is sometimes referred to as the "diversity", is a scale parameter. If $\mu =0$ and $b=1$ , the positive half-line is exactly an exponential distribution scaled by 1/2.

The probability density function of the Laplace distribution is also reminiscent of the normal distribution; however, whereas the normal distribution is expressed in terms of the squared difference from the mean $\mu$ , the Laplace density is expressed in terms of the absolute difference from the mean. Consequently, the Laplace distribution has fatter tails than the normal distribution. It is a special case of the generalized normal distribution and the hyperbolic distribution. Continuous symmetric distributions that have exponential tails, like the Laplace distribution, but which have probability density functions that are differentiable at the mode include the logistic distribution, hyperbolic secant distribution, and the Champernowne distribution.

### Cumulative distribution function

The Laplace distribution is easy to integrate (if one distinguishes two symmetric cases) due to the use of the absolute value function. Its cumulative distribution function is as follows: ${\begin{aligned}F(x)&=\int _{-\infty }^{x}\!\!f(u)\,\mathrm {d} u={\begin{cases}{\frac {1}{2}}\exp \left({\frac {x-\mu }{b}}\right)&{\mbox{if }}x<\mu \\1-{\frac {1}{2}}\exp \left(-{\frac {x-\mu }{b}}\right)&{\mbox{if }}x\geq \mu \end{cases}}\\&={\tfrac {1}{2}}+{\tfrac {1}{2}}\operatorname {sgn}(x-\mu )\left(1-\exp \left(-{\frac {|x-\mu |}{b}}\right)\right).\end{aligned}}$

The inverse cumulative distribution function is given by

$F^{-1}(p)=\mu -b\,\operatorname {sgn}(p-0.5)\,\ln(1-2|p-0.5|).$

## Properties

### Moments

$\mu _{r}'={\frac {1}{2}}\sum _{k=0}^{r}\left[{\frac {r!}{(r-k)!}}b^{k}\mu ^{(r-k)}\left\{1+(-1)^{k}\right\}\right].$

- If $X\sim {\textrm {Laplace}}(\mu ,b)$ then $kX+c\sim {\textrm {Laplace}}(k\mu +c,|k|b)$ .
- If $X\sim {\textrm {Laplace}}(0,1)$ then $bX\sim {\textrm {Laplace}}(0,b)$ .
- If $X\sim {\textrm {Laplace}}(0,b)$ then $\left|X\right|\sim {\textrm {Exponential}}\left(b^{-1}\right)$ (exponential distribution).
- If $X,Y\sim {\textrm {Exponential}}(\lambda )$ then $X-Y\sim {\textrm {Laplace}}\left(0,\lambda ^{-1}\right)$ ．
- If $X\sim {\textrm {Laplace}}(\mu ,b)$ then $\left|X-\mu \right|\sim {\textrm {Exponential}}(b^{-1})$ .
- If $X\sim {\textrm {Laplace}}(\mu ,b)$ then $X\sim {\textrm {EPD}}(\mu ,b,1)$ (exponential power distribution).
- If $X_{1},...,X_{4}\sim {\textrm {N}}(0,1)$ (normal distribution) then $X_{1}X_{2}-X_{3}X_{4}\sim {\textrm {Laplace}}(0,1)$ and $(X_{1}^{2}-X_{2}^{2}+X_{3}^{2}-X_{4}^{2})/2\sim {\textrm {Laplace}}(0,1)$ .
- If $X_{i}\sim {\textrm {Laplace}}(\mu ,b)$ then ${\frac {\displaystyle 2}{b}}\sum _{i=1}^{n}|X_{i}-\mu |\sim \chi ^{2}(2n)$ (chi-squared distribution).
- If $X,Y\sim {\textrm {Laplace}}(\mu ,b)$ then ${\tfrac {|X-\mu |}{|Y-\mu |}}\sim \operatorname {F} (2,2)$ . (F-distribution)
- If $X,Y\sim {\textrm {U}}(0,1)$ (uniform distribution) then $\log(X/Y)\sim {\textrm {Laplace}}(0,1)$ .
- If $X\sim {\textrm {Exponential}}(\lambda )$ and $Y\sim {\textrm {Bernoulli}}(0.5)$ (Bernoulli distribution) independent of X , then $X(2Y-1)\sim {\textrm {Laplace}}\left(0,\lambda ^{-1}\right)$ .
- If $X\sim {\textrm {Exponential}}(\lambda )$ and $Y\sim {\textrm {Exponential}}(\nu )$ independent of X , then $\lambda X-\nu Y\sim {\textrm {Laplace}}(0,1)$ ．
- If X has a Rademacher distribution and $Y\sim {\textrm {Exponential}}(\lambda )$ then $XY\sim {\textrm {Laplace}}(0,1/\lambda )$ .
- If $V\sim {\textrm {Exponential}}(1)$ and $Z\sim N(0,1)$ independent of V , then $X=\mu +b{\sqrt {2V}}Z\sim \mathrm {Laplace} (\mu ,b)$ .
- If $X\sim {\textrm {GeometricStable}}(2,0,\lambda ,0)$ (geometric stable distribution) then $X\sim {\textrm {Laplace}}(0,\lambda )$ .
- The Laplace distribution is a limiting case of the hyperbolic distribution.
- If $X|Y\sim {\textrm {N}}(\mu ,Y^{2})$ with $Y\sim {\textrm {Rayleigh}}(b)$ (Rayleigh distribution) then $X\sim {\textrm {Laplace}}(\mu ,b)$ . Note that if $Y\sim {\textrm {Rayleigh}}(b)$ , then $Y^{2}\sim {\textrm {Gamma}}(1,2b^{2})$ with ${\textrm {E}}(Y^{2})=2b^{2}$ , which in turn equals the exponential distribution ${\textrm {Exp}}(1/(2b^{2}))$ .
- Given an integer $n\geq 1$ , if $X_{i},Y_{i}\sim \Gamma \left({\frac {1}{n}},b\right)$ (gamma distribution, using $k,\theta$ characterization), then $\sum _{i=1}^{n}\left({\frac {\mu }{n}}+X_{i}-Y_{i}\right)\sim {\textrm {Laplace}}(\mu ,b)$ (infinite divisibility)
- If *X* has a Laplace distribution, then *Y* = *e**X* has a log-Laplace distribution; conversely, if *X* has a log-Laplace distribution, then its logarithm has a Laplace distribution.

### Probability of a Laplace being greater than another

Let $X,Y$ be independent laplace random variables: $X\sim {\textrm {Laplace}}(\mu _{X},b_{X})$ and $Y\sim {\textrm {Laplace}}(\mu _{Y},b_{Y})$ , and we want to compute $P(X>Y)$ .

The probability of $P(X>Y)$ can be reduced (using the properties below) to $P(\mu +bZ_{1}>Z_{2})$ , where $Z_{1},Z_{2}\sim {\textrm {Laplace}}(0,1)$ . This probability is equal to

$P(\mu +bZ_{1}>Z_{2})={\begin{cases}{\frac {b^{2}e^{\mu /b}-e^{\mu }}{2(b^{2}-1)}},&{\text{when }}\mu <0\\1-{\frac {b^{2}e^{-\mu /b}-e^{-\mu }}{2(b^{2}-1)}},&{\text{when }}\mu >0\\\end{cases}}$

When $b=1$ , both expressions are replaced by their limit as $b\to 1$ :

$P(\mu +Z_{1}>Z_{2})={\begin{cases}e^{\mu }{\frac {(2-\mu )}{4}},&{\text{when }}\mu <0\\1-e^{-\mu }{\frac {(2+\mu )}{4}},&{\text{when }}\mu >0\\\end{cases}}$

To compute the case for $\mu >0$ , note that $P(\mu +Z_{1}>Z_{2})=1-P(\mu +Z_{1}<Z_{2})=1-P(-\mu -Z_{1}>-Z_{2})=1-P(-\mu +Z_{1}>Z_{2})$

since $Z\sim -Z$ when $Z\sim {\textrm {Laplace}}(0,1)$ .

### Relation to the exponential distribution

A Laplace random variable can be represented as the difference of two independent and identically distributed (iid) exponential random variables. One way to show this is by using the characteristic function approach. For any set of independent continuous random variables, for any linear combination of those variables, its characteristic function (which uniquely determines the distribution) can be acquired by multiplying the corresponding characteristic functions.

Consider two i.i.d random variables $X,Y\sim {\textrm {Exponential}}(\lambda )$ . The characteristic functions for $X,-Y$ are

${\frac {\lambda }{-it+\lambda }},\quad {\frac {\lambda }{it+\lambda }}$

respectively. On multiplying these characteristic functions (equivalent to the characteristic function of the sum of the random variables $X+(-Y)$ ), the result is

${\frac {\lambda ^{2}}{(-it+\lambda )(it+\lambda )}}={\frac {\lambda ^{2}}{t^{2}+\lambda ^{2}}}.$

This is the same as the characteristic function for $Z\sim {\textrm {Laplace}}(0,1/\lambda )$ , which is

${\frac {1}{1+{\frac {t^{2}}{\lambda ^{2}}}}}.$

### Sargan distributions

Sargan distributions are a system of distributions of which the Laplace distribution is a core member. A p th order Sargan distribution has density $f_{p}(x)={\tfrac {1}{2}}\exp(-\alpha |x|){\frac {\displaystyle 1+\sum _{j=1}^{p}\beta _{j}\alpha ^{j}|x|^{j}}{\displaystyle 1+\sum _{j=1}^{p}j!\beta _{j}}},$ for parameters $\alpha \geq 0,\beta _{j}\geq 0$ . The Laplace distribution results for $p=0$ .

## Statistical inference

Given n independent and identically distributed samples $x_{1},x_{2},...,x_{n}$ , the maximum likelihood (MLE) estimator of $\mu$ is the sample median, ${\hat {\mu }}=\mathrm {med} (x).$

The MLE estimator of b is the mean absolute deviation from the median, ${\hat {b}}={\frac {1}{n}}\sum _{i=1}^{n}|x_{i}-{\hat {\mu }}|.$ revealing a link between the Laplace distribution and least absolute deviations. A correction for small samples can be applied as follows: ${\hat {b}}^{*}={\hat {b}}\cdot n/(n-2)$ (see: exponential distribution#Parameter estimation).

## Occurrence and applications

The Laplacian distribution has been used in speech recognition to model priors on DFT coefficients and in JPEG image compression to model AC coefficients generated by a DCT.

- The addition of noise drawn from a Laplacian distribution, with scaling parameter appropriate to a function's sensitivity, to the output of a statistical database query is the most common means to provide differential privacy in statistical databases.

- In regression analysis, the least absolute deviations estimate arises as the maximum likelihood estimate if the errors have a Laplace distribution.
- The Lasso can be thought of as a Bayesian regression with a Laplacian prior for the coefficients.
- In hydrology the Laplace distribution is applied to extreme events such as annual maximum one-day rainfalls and river discharges. The blue picture illustrates an example of fitting the Laplace distribution to ranked annually maximum one-day rainfalls showing also the 90% confidence belt based on the binomial distribution. The rainfall data are represented by plotting positions as part of the cumulative frequency analysis.
- The Laplace distribution has applications in finance. For example, S.G. Kou developed a model for financial instrument prices incorporating a Laplace distribution (in some cases an asymmetric Laplace distribution) to address problems of skewness, kurtosis and the volatility smile that often occur when using a normal distribution for pricing these instruments.

The Laplace distribution, being a

composite

or

double

distribution, is applicable in situations where the lower values originate under different external conditions than the higher ones so that they follow a different pattern.

## Random variate generation

Given a random variable U drawn from the uniform distribution in the interval $\left(-1/2,1/2\right)$ , the random variable

$X=\mu -b\,\operatorname {sgn}(U)\,\ln(1-2|U|)$

has a Laplace distribution with parameters $\mu$ and b . This follows from the inverse cumulative distribution function given above.

A ${\textrm {Laplace}}(0,b)$ variate can also be generated as the difference of two i.i.d. ${\textrm {Exponential}}(1/b)$ random variables. Equivalently, ${\textrm {Laplace}}(0,1)$ can also be generated as the logarithm of the ratio of two i.i.d. uniform random variables.

## History

This distribution is often referred to as "Laplace's first law of errors". He published it in 1774, modeling the frequency of an error as an exponential function of its magnitude once its sign was disregarded. Laplace would later replace this model with his "second law of errors", based on the normal distribution, after the discovery of the central limit theorem.

Keynes published a paper in 1911 based on his earlier thesis wherein he showed that the Laplace distribution minimised the absolute deviation from the median.
