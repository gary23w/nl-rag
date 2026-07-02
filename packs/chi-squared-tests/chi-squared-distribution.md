---
title: "Chi-squared distribution"
source: https://en.wikipedia.org/wiki/Chi-squared_distribution
domain: chi-squared-tests
license: CC-BY-SA-4.0
tags: chi-squared test, contingency table, goodness of fit, G-test
fetched: 2026-07-02
---

# Chi-squared distribution

In probability theory and statistics, the **$\chi ^{2}$ -distribution** with k degrees of freedom is the distribution of a sum of the squares of k independent standard normal random variables.

The chi-squared distribution $\chi _{k}^{2}$ is a special case of the gamma distribution and the univariate Wishart distribution. Specifically if $X\sim \chi _{k}^{2}$ then ${\textstyle X\sim {\text{Gamma}}(\alpha ={\frac {k}{2}},\theta =2)}$ (where $\alpha$ is the shape parameter and $\theta$ the scale parameter of the gamma distribution) and $X\sim {\text{W}}_{1}(1,k)$ .

The **scaled chi-squared distribution** $s^{2}\chi _{k}^{2}$ is a reparametrization of the gamma distribution and the univariate Wishart distribution. Specifically if $X\sim s^{2}\chi _{k}^{2}$ then ${\textstyle X\sim {\text{Gamma}}(\alpha ={\frac {k}{2}},\theta =2s^{2})}$ and $X\sim {\text{W}}_{1}(s^{2},k)$ .

The chi-squared distribution is one of the most widely used probability distributions in inferential statistics, notably in hypothesis testing and in construction of confidence intervals. This distribution is sometimes called the **central chi-squared distribution**, a special case of the more general noncentral chi-squared distribution.

The chi-squared distribution is used in the common chi-squared tests for goodness of fit of an observed distribution to a theoretical one, the independence of two criteria of classification of qualitative data, and in finding the confidence interval for estimating the population standard deviation of a normal distribution from a sample standard deviation. Many other statistical tests also use this distribution, such as Friedman's analysis of variance by ranks.

## Definitions

If *Z*1, ..., *Z**k* are independent, standard normal random variables, then the sum of their squares, $X\ =\sum _{i=1}^{k}Z_{i}^{2},$ is distributed according to the chi-squared distribution with k degrees of freedom.

This is usually denoted as $X\ \sim \ \chi ^{2}(k)\ \ {\text{or}}\ \ X\ \sim \ \chi _{k}^{2}.$

The chi-squared distribution has one parameter: a positive integer k that specifies the number of degrees of freedom (the number of random variables *Z**i* being summed).

### Introduction

The chi-squared distribution is used primarily in hypothesis testing, and to a lesser extent for confidence intervals for population variance when the underlying distribution is normal. Unlike more widely known distributions such as the normal distribution and the exponential distribution, the chi-squared distribution is not as often applied in the direct modeling of natural phenomena. It arises in the following hypothesis tests, among others:

- Chi-squared test of independence in contingency tables
- Chi-squared test of goodness of fit of observed data to hypothetical distributions
- Likelihood-ratio test for nested models
- Log-rank test in survival analysis
- Cochran–Mantel–Haenszel test for stratified contingency tables
- Wald test
- Score test

It is also a component of the definition of the *t*-distribution and the *F*-distribution used in *t*-tests, analysis of variance, and regression analysis.

The primary reason for which the chi-squared distribution is extensively used in hypothesis testing is its relationship to the normal distribution. Many hypothesis tests use a test statistic, such as the *t*-statistic in a *t*-test. For these hypothesis tests, as the sample size, n, increases, the sampling distribution of the test statistic approaches the normal distribution (central limit theorem). Because the test statistic (such as t) is asymptotically normally distributed, provided the sample size is sufficiently large, the distribution used for hypothesis testing may be approximated by a normal distribution. Testing hypotheses using a normal distribution is well understood and relatively easy. The simplest chi-squared distribution is the square of a standard normal distribution. So wherever a normal distribution could be used for a hypothesis test, a chi-squared distribution could be used.

Suppose that Z is a random variable sampled from the standard normal distribution, where the mean is 0 and the variance is 1 : $Z\sim N(0,1)$ . Now, consider the random variable $X=Z^{2}$ . The distribution of the random variable X is an example of a chi-squared distribution: $\ X\ \sim \ \chi _{1}^{2}$ . The subscript 1 indicates that this particular chi-squared distribution is constructed from only 1 standard normal distribution. A chi-squared distribution constructed by squaring a single standard normal distribution is said to have 1 degree of freedom. Thus, as the sample size for a hypothesis test increases, the distribution of the test statistic approaches a normal distribution. Just as extreme values of the normal distribution have low probability (and give small p-values), extreme values of the chi-squared distribution have low probability.

An additional reason that the chi-squared distribution is widely used is that it turns up as the large sample distribution of generalized likelihood ratio tests (LRT). LRTs have several desirable properties; in particular, simple LRTs commonly provide the highest power to reject the null hypothesis (Neyman–Pearson lemma) and this leads also to optimality properties of generalised LRTs. However, the normal and chi-squared approximations are only valid asymptotically. For this reason, it is preferable to use the *t* distribution rather than the normal approximation or the chi-squared approximation for a small sample size. Similarly, in analyses of contingency tables, the chi-squared approximation will be poor for a small sample size, and it is preferable to use Fisher's exact test. Ramsey shows that the exact binomial test is always more powerful than the normal approximation.

Lancaster shows the connections among the binomial, normal, and chi-squared distributions, as follows. De Moivre and Laplace established that a binomial distribution could be approximated by a normal distribution. Specifically they showed the asymptotic normality of the random variable

$\chi ={\frac {m-Np}{\sqrt {Npq}}}$

where m is the observed number of successes in N trials, where the probability of success is p , and $q=1-p$ .

Squaring both sides of the equation gives

$\chi ^{2}={\frac {\left(m-Np\right)^{2}}{Npq}}$

Using $N=Np+N(1-p)$ , $N=m+(N-m)$ , and $q=1-p$ , this equation can be rewritten as

$\chi ^{2}={\frac {\left(m-Np\right)^{2}}{Np}}+{\frac {\left(N-m-Nq\right)^{2}}{Nq}}$

The expression on the right is of the form that Karl Pearson would generalize to the form

$\chi ^{2}=\sum _{i=1}^{n}{\frac {\left(O_{i}-E_{i}\right)^{2}}{E_{i}}}$

where

- $\chi ^{2}$ = Pearson's cumulative test statistic, which asymptotically approaches a $\chi ^{2}$ distribution;
- $O_{i}$ = the number of observations of type i ;
- $E_{i}=Np_{i}$ = the expected (theoretical) frequency of type i , asserted by the null hypothesis that the fraction of type i in the population is $p_{i}$ ; and
- n = the number of cells in the table.

In the case of a binomial outcome (flipping a coin), the binomial distribution may be approximated by a normal distribution (for sufficiently large n ). Because the square of a standard normal distribution is the chi-squared distribution with one degree of freedom, the probability of a result such as 1 heads in 10 trials can be approximated either by using the normal distribution directly, or the chi-squared distribution for the normalised, squared difference between observed and expected value. However, many problems involve more than the two possible outcomes of a binomial, and instead require 3 or more categories, which leads to the multinomial distribution. Just as de Moivre and Laplace sought for and found the normal approximation to the binomial, Pearson sought for and found a degenerate multivariate normal approximation to the multinomial distribution (the numbers in each category add up to the total sample size, which is considered fixed). Pearson showed that the chi-squared distribution arose from such a multivariate normal approximation to the multinomial distribution, taking careful account of the statistical dependence (negative correlations) between numbers of observations in different categories.

### Probability density function

The probability density function (pdf) of the chi-squared distribution is $f(x;\,k)={\begin{cases}{\dfrac {x^{k/2-1}e^{-x/2}}{2^{k/2}\,\Gamma {\left({\frac {k}{2}}\right)}}},&x>0;\\0,&{\text{otherwise}}.\end{cases}}$ where ${\textstyle \Gamma (k/2)}$ denotes the gamma function, which has closed-form values for integer k .

For derivations of the pdf in the cases of one, two and k degrees of freedom, see Proofs related to chi-squared distribution.

### Cumulative distribution function

Its cumulative distribution function is: $F(x;\,k)={\frac {\gamma {\left({\frac {k}{2}},\,{\frac {x}{2}}\right)}}{\Gamma {\left({\frac {k}{2}}\right)}}}=P{\left({\frac {k}{2}},\,{\frac {x}{2}}\right)},$ where $\gamma (s,t)$ is the lower incomplete gamma function and ${\textstyle P(s,t)}$ is the regularized gamma function.

In a special case of $k=2$ this function has the simple form: $F(x;\,2)=1-e^{-x/2}$ which can be easily derived by integrating ${\textstyle f(x;\,2)={\frac {1}{2}}e^{-x/2}}$ directly. The integer recurrence of the gamma function makes it easy to compute $F(x;\,k)$ for other small, even k .

Tables of the chi-squared cumulative distribution function are widely available and the function is included in many spreadsheets and all statistical packages.

Letting $z\equiv x/k$ , Chernoff bounds on the lower and upper tails of the CDF may be obtained. For the cases when $0<z<1$ (which include all of the cases when this CDF is less than half): $F(zk;\,k)\leq (ze^{1-z})^{k/2}.$

The tail bound for the cases when $z>1$ , similarly, is $1-F(zk;\,k)\leq (ze^{1-z})^{k/2}.$

For another approximation for the CDF modeled after the cube of a Gaussian, see under Noncentral chi-squared distribution.

## Properties

### Cochran's theorem

The following is a special case of Cochran's theorem.

**Theorem.** If $Z_{1},...,Z_{n}$ are independent identically distributed (i.i.d.), standard normal random variables, then ${\textstyle \sum _{t=1}^{n}\left(Z_{t}-{\bar {Z}}\right)^{2}\sim \chi _{n-1}^{2}}$ where ${\textstyle {\bar {Z}}={\frac {1}{n}}\sum _{t=1}^{n}Z_{t}.}$

[Proof]

**Proof.** Let $Z\sim {\mathcal {N}}({\bar {0}},1\!\!1)$ be a vector of n independent normally distributed random variables, and ${\bar {Z}}$ their average. Then $\sum _{t=1}^{n}(Z_{t}-{\bar {Z}})^{2}~=~\sum _{t=1}^{n}Z_{t}^{2}-n{\bar {Z}}^{2}~=~Z^{\top }[1\!\!1-{\textstyle {\frac {1}{n}}}{\bar {1}}{\bar {1}}^{\top }]Z~=:~Z^{\top }\!MZ$ where $1\!\!1$ is the identity matrix and ${\bar {1}}$ the all ones vector. M has one eigenvector $b_{1}:={\textstyle {\frac {1}{\sqrt {n}}}}{\bar {1}}$ with eigenvalue 0 , and $n-1$ eigenvectors $b_{2},...,b_{n}$ (all orthogonal to $b_{1}$ ) with eigenvalue 1 , which can be chosen so that $Q:=(b_{1},...,b_{n})$ is an orthogonal matrix. Since also $X:=Q^{\top }\!Z\sim {\mathcal {N}}({\bar {0}},Q^{\top }\!1\!\!1Q)={\mathcal {N}}({\bar {0}},1\!\!1)$ , we have $\sum _{t=1}^{n}(Z_{t}-{\bar {Z}})^{2}~=~Z^{\top }\!MZ~=~X^{\top }\!Q^{\top }\!MQX~=~X_{2}^{2}+...+X_{n}^{2}~\sim ~\chi _{n-1}^{2},$ which proves the claim.

### Additivity

It follows from the definition of the chi-squared distribution that the sum of independent chi-squared variables is also chi-squared distributed. Specifically, if $X_{i},i={\overline {1,n}}$ are independent chi-squared variables with $k_{i}$ , $i={\overline {1,n}}$ degrees of freedom, respectively, then $Y=X_{1}+\cdots +X_{n}$ is chi-squared distributed with $k_{1}+\cdots +k_{n}$ degrees of freedom.

### Sample mean

The sample mean of n i.i.d. chi-squared variables of degree k is distributed according to a gamma distribution with shape $\alpha$ and scale $\theta$ parameters: ${\overline {X}}={\frac {1}{n}}\sum _{i=1}^{n}X_{i}\sim \operatorname {Gamma} \left(\alpha {=}{\tfrac {nk}{2}},\,\theta {=}{\tfrac {2}{n}}\right)\qquad {\text{where }}X_{i}\sim \chi ^{2}(k)$

Asymptotically, given that for a shape parameter $\alpha$ going to infinity, a Gamma distribution converges towards a normal distribution with expectation $\mu =\alpha \theta$ and variance $\sigma ^{2}=\alpha \theta ^{2}$ , the sample mean converges towards:

${\overline {X}}\xrightarrow {n\to \infty } N{\left(\mu {=}k,\,\sigma ^{2}{=}{\tfrac {2k}{n}}\right)}$

Note that we would have obtained the same result invoking instead the central limit theorem, noting that for each chi-squared variable of degree k the expectation is k , and its variance $2k$ (and hence the variance of the sample mean ${\overline {X}}$ being ${\textstyle \sigma ^{2}={\tfrac {2k}{n}}}$ ).

### Entropy

The differential entropy is given by ${\begin{aligned}h&=\int _{0}^{\infty }f(x;\,k)\ln f(x;\,k)\,dx\\&={\frac {k}{2}}+\ln \left[2\,\Gamma {\left({\frac {k}{2}}\right)}\right]+\left(1-{\frac {k}{2}}\right)\psi \!\left({\frac {k}{2}}\right),\end{aligned}}$ where $\psi (x)$ is the Digamma function.

The chi-squared distribution is the maximum entropy probability distribution for a random variate X for which $\operatorname {E} (X)=k$ and $\operatorname {E} (\ln(X))=\psi (k/2)+\ln(2)$ are fixed. Since the chi-squared is in the family of gamma distributions, this can be derived by substituting appropriate values in the Expectation of the log moment of gamma. For derivation from more basic principles, see the derivation in moment-generating function of the sufficient statistic.

### Noncentral moments

The noncentral moments (raw moments) of a chi-squared distribution with k degrees of freedom are given by ${\begin{aligned}\operatorname {E} (X^{m})&=k(k+2)(k+4)\cdots (k+2m-2)\\[1ex]&=2^{m}{\frac {\Gamma {\left(m+{\frac {k}{2}}\right)}}{\Gamma {\left({\frac {k}{2}}\right)}}}.\end{aligned}}$

### Cumulants

The cumulants are readily obtained by a power series expansion of the logarithm of the characteristic function: $\kappa _{n}=2^{n-1}(n-1)!\,k$ with cumulant generating function ${\textstyle \ln \operatorname {E} [e^{tX}]=-{\frac {k}{2}}\ln(1-2t)}$ .

### Concentration

The chi-squared distribution exhibits strong concentration around its mean. The standard Laurent-Massart bounds are: $\Pr(X-k\geq 2{\sqrt {kx}}+2x)\leq e^{-x}$ $\Pr(k-X\geq 2{\sqrt {kx}})\leq e^{-x}$ One consequence is that, if $Z\sim N(0,1)^{k}$ is a Gaussian random vector in $\mathbb {R} ^{k}$ , then as the dimension k grows, the squared length of the vector is concentrated tightly around k with a width $k^{1/2+\alpha }$ : $\Pr \left(\left\|Z\right\|^{2}\in \left[k-2k^{1/2+\alpha },\;k+2k^{1/2+\alpha }+2k^{\alpha }\right]\right)\geq 1-e^{-k^{\alpha }}$ where the exponent $\alpha$ can be chosen as any value in $\mathbb {R}$ .

Since the cumulant generating function for $\chi ^{2}(k)$ is ${\textstyle K(t)=-{\frac {k}{2}}\ln(1-2t)}$ , and its convex dual is ${\textstyle K^{*}(q)={\frac {1}{2}}\left(q-k+k\ln {\frac {k}{q}}\right)}$ , the standard Chernoff bound yields ${\begin{aligned}\ln \Pr(X\geq (1+\varepsilon )k)&\leq -{\frac {k}{2}}\left(\varepsilon -\ln(1+\varepsilon )\right)\\\ln \Pr(X\leq (1-\varepsilon )k)&\leq -{\frac {k}{2}}\left(-\varepsilon -\ln(1-\varepsilon )\right)\end{aligned}}$ where $0<\varepsilon <1$ . By the union bound, $Pr(X\in (1\pm \varepsilon )k)\geq 1-2e^{-{\frac {k}{2}}({\frac {1}{2}}\varepsilon ^{2}-{\frac {1}{3}}\varepsilon ^{3})}$ This result is used in proving the Johnson–Lindenstrauss lemma.

### Asymptotic properties

By the central limit theorem, because the chi-squared distribution is the sum of k independent random variables with finite mean and variance, it converges to a normal distribution for large k . For many practical purposes, for $k>50$ the distribution is sufficiently close to a normal distribution, so the difference is ignorable. Specifically, if $X\sim \chi ^{2}(k)$ , then as k tends to infinity, the distribution of $(X-k)/{\sqrt {2k}}$ tends to a standard normal distribution. However, convergence is slow as the skewness is ${\textstyle {\sqrt {8/k}}}$ and the excess kurtosis is $12/k$ .

The sampling distribution of $\ln(\chi ^{2})$ converges to normality much faster than the sampling distribution of $\chi ^{2}$ , as the logarithmic transform removes much of the asymmetry.

Other functions of the chi-squared distribution converge more rapidly to a normal distribution. Some examples are:

- If $X\sim \chi ^{2}(k)$ then ${\sqrt {2X}}$ is approximately normally distributed with mean ${\sqrt {2k-1}}$ and unit variance (1922, by R. A. Fisher, see (18.23), p. 426 of Johnson).
- If $X\sim \chi ^{2}(k)$ then ${\textstyle {\sqrt[{3}]{X/k}}}$ is approximately normally distributed with mean $1-{\frac {2}{9k}}$ and variance ${\frac {2}{9k}}.$ This is known as the **Wilson–Hilferty transformation**, see (18.24), p. 426 of Johnson.
  - This normalizing transformation leads directly to the commonly used median approximation $k{\bigg (}1-{\frac {2}{9k}}{\bigg )}^{3}\;$ by back-transforming from the mean, which is also the median, of the normal distribution.

- As $k\to \infty$ , $(\chi _{k}^{2}-k)/{\sqrt {2k}}~{\xrightarrow {d}}\ N(0,1)\,$ (normal distribution)
- $\chi _{k}^{2}\sim {\chi '}_{k}^{2}(0)$ (noncentral chi-squared distribution with non-centrality parameter $\lambda =0$ )
- If $Y\sim \mathrm {F} (\nu _{1},\nu _{2})$ then $X=\lim _{\nu _{2}\to \infty }\nu _{1}Y$ has the chi-squared distribution $\chi _{\nu _{1}}^{2}$
  - As a special case, if $Y\sim \mathrm {F} (1,\nu _{2})\,$ then $X=\lim _{\nu _{2}\to \infty }Y\,$ has the chi-squared distribution $\chi _{1}^{2}$
- $\left\|{\boldsymbol {N}}_{i=1,\ldots ,k}(0,1)\right\|^{2}\sim \chi _{k}^{2}$ (The squared norm of *k* standard normally distributed variables is a chi-squared distribution with *k* degrees of freedom)
- If $X\sim \chi _{\nu }^{2}\,$ and $c>0\,$ , then $cX\sim \Gamma (k=\nu /2,\theta =2c)\,$ . (gamma distribution)
- If $X\sim \chi _{k}^{2}$ then ${\sqrt {X}}\sim \chi _{k}$ (chi distribution)
- If $X\sim \chi _{2}^{2}$ , then $X\sim \operatorname {exp} (1/2)$ is an exponential distribution. (See gamma distribution for more.)
- If $X\sim \chi _{2k}^{2}$ , then $X\sim \operatorname {Erlang} (k,1/2)$ is an Erlang distribution.
- If $X\sim \operatorname {Erlang} (k,\lambda )$ , then $2\lambda X\sim \chi _{2k}^{2}$
- If $X\sim \operatorname {Rayleigh} (1)\,$ (Rayleigh distribution) then $X^{2}\sim \chi _{2}^{2}\,$
- If $X\sim \operatorname {Maxwell} (1)\,$ (Maxwell distribution) then $X^{2}\sim \chi _{3}^{2}\,$
- If $X\sim \chi _{\nu }^{2}$ then ${\tfrac {1}{X}}\sim \operatorname {Inv-} \chi _{\nu }^{2}\,$ (Inverse-chi-squared distribution)
- The chi-squared distribution is a special case of type III Pearson distribution
- If $X\sim \chi _{\nu _{1}}^{2}\,$ and $Y\sim \chi _{\nu _{2}}^{2}\,$ are independent then ${\tfrac {X}{X+Y}}\sim \operatorname {Beta} ({\tfrac {\nu _{1}}{2}},{\tfrac {\nu _{2}}{2}})\,$ (beta distribution)
- If $X\sim \operatorname {U} (0,1)\,$ (uniform distribution) then $-2\log(X)\sim \chi _{2}^{2}\,$
- If $X_{i}\sim \operatorname {Laplace} (\mu ,\beta )\,$ then $\sum _{i=1}^{n}{\frac {2|X_{i}-\mu |}{\beta }}\sim \chi _{2n}^{2}\,$
- If $X_{i}$ follows the generalized normal distribution (version 1) with parameters $\mu ,\alpha ,\beta$ then $\sum _{i=1}^{n}{\frac {2|X_{i}-\mu |^{\beta }}{\alpha }}\sim \chi _{2n/\beta }^{2}\,$
- The chi-squared distribution is a transformation of Pareto distribution
- Student's t-distribution is a transformation of chi-squared distribution
- Student's t-distribution can be obtained from chi-squared distribution and normal distribution
- The noncentral beta distribution can be obtained as a transformation of chi-squared distribution and noncentral chi-squared distribution
- The noncentral t-distribution can be obtained from normal distribution and chi-squared distribution

A chi-squared variable with k degrees of freedom is defined as the sum of the squares of k independent standard normal random variables.

If Y is a k -dimensional Gaussian random vector with mean vector $\mu$ and rank k covariance matrix C , then $X=(Y-\mu )^{\mathsf {T}}C^{-1}(Y-\mu )$ is chi-squared distributed with k degrees of freedom.

The sum of squares of statistically independent unit-variance Gaussian variables which do *not* have mean zero yields a generalization of the chi-squared distribution called the noncentral chi-squared distribution.

If Y is a vector of k i.i.d. standard normal random variables and A is a $k\times k$ symmetric, idempotent matrix with rank $k-n$ , then the quadratic form $Y^{\mathsf {T}}\!AY$ is chi-square distributed with $k-n$ degrees of freedom.

If $\Sigma$ is a $p\times p$ positive-semidefinite covariance matrix with strictly positive diagonal entries, then for $X\sim N(0,\Sigma )$ and w a random p -vector independent of X such that $w_{1}+\cdots +w_{p}=1$ and $w_{i}\geq 0,i=1,\ldots ,p,$ then

${\frac {1}{{\tilde {w}}^{\mathsf {T}}\Sigma {\tilde {w}}}}\sim \chi _{1}^{2}.$ where ${\tilde {w}}=(w_{1}/X_{1},\dots ,w_{p}/X_{p})$ .

The chi-squared distribution is also naturally related to other distributions arising from the Gaussian. In particular,

- Y is F-distributed, $Y\sim F(k_{1},k_{2})$ if $Y={\frac {{X_{1}}/{k_{1}}}{{X_{2}}/{k_{2}}}}$ , where $X_{1}\sim \chi _{k_{1}}^{2}$ and $X_{2}\sim \chi _{k_{2}}^{2}$ are statistically independent.
- If $X_{1}\sim \chi _{k_{1}}^{2}$ and $X_{2}\sim \chi _{k_{2}}^{2}$ are statistically independent, then $X_{1}+X_{2}\sim \chi _{k_{1}+k_{2}}^{2}$ . If $X_{1}$ and $X_{2}$ are not independent, then $X_{1}+X_{2}$ is not chi-square distributed.

### Generalizations

The chi-squared distribution is obtained as the sum of the squares of k independent, zero-mean, unit-variance Gaussian random variables. Generalizations of this distribution can be obtained by summing the squares of other types of Gaussian random variables. Several such distributions are described below.

### Linear combination

If $X_{1},\ldots ,X_{n}$ are chi square random variables and $a_{1},\ldots ,a_{n}\in \mathbb {R} _{>0}$ , then the distribution of ${\textstyle X=\sum _{i=1}^{n}a_{i}X_{i}}$ is a special case of the generalized chi-squared distribution. A closed expression for this distribution is not known. It may be, however, approximated efficiently using the property of characteristic functions of chi-square random variables.

### Chi-squared distributions

#### Noncentral chi-squared distribution

The noncentral chi-squared distribution is obtained from the sum of the squares of independent Gaussian random variables having unit variance and *nonzero* means.

#### Generalized chi-squared distribution

The generalized chi-squared distribution is obtained from the quadratic form z'Az where z is a zero-mean Gaussian vector having an arbitrary covariance matrix, and A is an arbitrary matrix.

The chi-squared distribution $X\sim \chi _{k}^{2}$ is a special case of the gamma distribution, in that ${\textstyle X\sim \Gamma {\left({\tfrac {k}{2}},{\tfrac {1}{2}}\right)}}$ using the rate parameterization of the gamma distribution (or ${\textstyle X\sim \Gamma {\left({\tfrac {k}{2}},2\right)}}$ using the scale parameterization of the gamma distribution) where k is an integer.

Because the exponential distribution is also a special case of the gamma distribution, we also have that if $X\sim \chi _{2}^{2}$ , then ${\textstyle X\sim \operatorname {exp} \left({\tfrac {1}{2}}\right)}$ is an exponential distribution.

The Erlang distribution is also a special case of the gamma distribution and thus we also have that if $X\sim \chi _{k}^{2}$ with even k , then X is Erlang distributed with shape parameter $k/2$ and scale parameter $1/2$ .

## Occurrence and applications

The chi-squared distribution has numerous applications in inferential statistics, for instance in chi-squared tests and in estimating variances. It enters the problem of estimating the mean of a normally distributed population and the problem of estimating the slope of a regression line via its role in Student's t-distribution. It enters all analysis of variance problems via its role in the F-distribution, which is the distribution of the ratio of two independent chi-squared random variables, each divided by their respective degrees of freedom.

Following are some of the most common situations in which the chi-squared distribution arises from a Gaussian-distributed sample.

- if $X_{1},...,X_{n}$ are i.i.d. $N(\mu ,\sigma ^{2})$ random variables, then ${\textstyle \sum _{i=1}^{n}\left(X_{i}-{\bar {X}}\right)^{2}\sim \sigma ^{2}\chi _{n-1}^{2}}$ where ${\textstyle {\bar {X}}={\frac {1}{n}}\sum _{i=1}^{n}X_{i}}$ .
- The box below shows some statistics based on $X_{i}\sim N(\mu _{i},\sigma _{i}^{2}),i=1,\ldots ,k$ independent random variables that have probability distributions related to the chi-squared distribution:

| Name | Statistic |
|---|---|
| chi-squared distribution | $\sum _{i=1}^{k}\left({\frac {X_{i}-\mu _{i}}{\sigma _{i}}}\right)^{2}$ |
| noncentral chi-squared distribution | $\sum _{i=1}^{k}\left({\frac {X_{i}}{\sigma _{i}}}\right)^{2}$ |
| chi distribution | ${\sqrt {\sum _{i=1}^{k}\left({\frac {X_{i}-\mu _{i}}{\sigma _{i}}}\right)^{2}}}$ |
| noncentral chi distribution | ${\sqrt {\sum _{i=1}^{k}\left({\frac {X_{i}}{\sigma _{i}}}\right)^{2}}}$ |

The chi-squared distribution is also often encountered in magnetic resonance imaging.

## Computational methods

### Table of *χ*2 values vs *p*-values

The ${\textstyle p}$ -value is the probability of observing a test statistic *at least* as extreme in a chi-squared distribution. Accordingly, since the cumulative distribution function (CDF) for the appropriate degrees of freedom *(df)* gives the probability of having obtained a value *less extreme* than this point, subtracting the CDF value from 1 gives the *p*-value. A low *p*-value, below the chosen significance level, indicates statistical significance, i.e., sufficient evidence to reject the null hypothesis. A significance level of 0.05 is often used as the cutoff between significant and non-significant results.

The table below gives a number of *p*-values matching to $\chi ^{2}$ for the first 10 degrees of freedom.

Degrees of

freedom (df)

$\chi ^{2}$

value

1

0.004

0.02

0.06

0.15

0.46

1.07

1.64

2.71

3.84

6.63

10.83

2

0.10

0.21

0.45

0.71

1.39

2.41

3.22

4.61

5.99

9.21

13.82

3

0.35

0.58

1.01

1.42

2.37

3.66

4.64

6.25

7.81

11.34

16.27

4

0.71

1.06

1.65

2.20

3.36

4.88

5.99

7.78

9.49

13.28

18.47

5

1.14

1.61

2.34

3.00

4.35

6.06

7.29

9.24

11.07

15.09

20.52

6

1.63

2.20

3.07

3.83

5.35

7.23

8.56

10.64

12.59

16.81

22.46

7

2.17

2.83

3.82

4.67

6.35

8.38

9.80

12.02

14.07

18.48

24.32

8

2.73

3.49

4.59

5.53

7.34

9.52

11.03

13.36

15.51

20.09

26.12

9

3.32

4.17

5.38

6.39

8.34

10.66

12.24

14.68

16.92

21.67

27.88

10

3.94

4.87

6.18

7.27

9.34

11.78

13.44

15.99

18.31

23.21

29.59

p

-value

(probability)

0.95

0.90

0.80

0.70

0.50

0.30

0.20

0.10

0.05

0.01

0.001

These values can be calculated evaluating the quantile function (also known as "inverse CDF" or "ICDF") of the chi-squared distribution; e. g., the χ2 ICDF for *p* = 0.05 and df = 7 yields 2.1673 ≈ 2.17 as in the table above, noticing that 1 – *p* is the *p*-value from the table.

## History

This distribution was first described by the German geodesist and statistician Friedrich Robert Helmert in papers of 1875–6, where he computed the sampling distribution of the sample variance of a normal population. Thus in German this was traditionally known as the *Helmert'sche* ("Helmertian") or "Helmert distribution".

The distribution was independently rediscovered by the English mathematician Karl Pearson in the context of goodness of fit, for which he developed his Pearson's chi-squared test, published in 1900, with computed table of values published in (Elderton 1902), collected in (Pearson 1914, pp. xxxi–xxxiii, 26–28, Table XII). The name "chi-square" ultimately derives from Pearson's shorthand for the exponent in a multivariate normal distribution with the Greek letter Chi, writing −1⁄2*χ*2 for what would appear in modern notation as −1⁄2**x**TΣ−1**x** (Σ being the covariance matrix). The idea of a family of "chi-squared distributions", however, is not due to Pearson but arose as a further development due to Fisher in the 1920s.
