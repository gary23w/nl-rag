---
title: "Exponential family (part 1/2)"
source: https://en.wikipedia.org/wiki/Exponential_family
domain: generalized-linear-models
license: CC-BY-SA-4.0
tags: generalized linear model, link function, exponential family, quasi-likelihood
fetched: 2026-07-02
part: 1/2
---

# Exponential family

In probability and statistics, an **exponential family** is a parametric set of probability distributions of a certain form, specified below. This special form is chosen for mathematical convenience, including the enabling of the user to calculate expectations, covariances using differentiation based on some useful algebraic properties, as well as for generality, as exponential families are in a sense very natural sets of distributions to consider. The term **exponential class** is sometimes used in place of "exponential family", or the older term **Koopman–Darmois family**. Sometimes loosely referred to as *the* exponential family, this class of distributions is distinct because they all possess a variety of desirable properties, most importantly the existence of a sufficient statistic.

The concept of exponential families is credited to E. J. G. Pitman, G. Darmois, and B. O. Koopman in 1935–1936. Exponential families of distributions provide a general framework for selecting a possible alternative parameterisation of a parametric family of distributions, in terms of natural parameters, and for defining useful sample statistics, called the natural sufficient statistics of the family.


## Nomenclature difficulty

The terms "distribution" and "family" are often used loosely: Specifically, *an* exponential family is a *set* of distributions, where the specific distribution varies with the parameter; however, a parametric *family* of distributions is often referred to as "*a* distribution" (like "the normal distribution", meaning "the family of normal distributions"), and the set of all exponential families is sometimes loosely referred to as "the" exponential family.


## Definition

Most of the commonly used distributions form an exponential family or subset of an exponential family, listed in the subsection below. The subsections following it are a sequence of increasingly more general mathematical definitions of an exponential family. A casual reader may wish to restrict attention to the first and simplest definition, which corresponds to a single-parameter family of discrete or continuous probability distributions.

### Examples of exponential family distributions

Exponential families include many of the most common distributions. Among many others, exponential families includes the following:

- normal
- exponential
- gamma
- chi-squared
- beta
- Dirichlet
- Bernoulli
- categorical
- Poisson
- Wishart
- inverse Wishart
- geometric

A number of common distributions are exponential families, but only when certain parameters are fixed and known. For example:

- binomial (with fixed number of trials)
- multinomial (with fixed number of trials)
- negative binomial (with fixed number of failures)

Note that in each case, the parameters which must be fixed are those that set a limit on the range of values that can possibly be observed.

Examples of common distributions that are *not* exponential families are Student's *t*, most mixture distributions, and even the family of uniform distributions when the bounds are not fixed. See the section below on examples for more discussion.

### Scalar parameter

The value of $\theta$ is called the *parameter* of the family.

A single-parameter exponential family is a set of probability distributions whose probability density function (or probability mass function, for the case of a discrete distribution) can be expressed in the form

$f_{X}{\left(x\,{\big |}\,\theta \right)}=h(x)\,\exp \left[\eta (\theta )\cdot T(x)-A(\theta )\right]$

where *T*(*x*), *h*(*x*), *η*(*θ*), and *A*(*θ*) are known functions. The function *h*(*x*) must be non-negative.

An alternative, equivalent form often given is

$f_{X}{\left(x\ {\big |}\ \theta \right)}=h(x)\,g(\theta )\,\exp \left[\eta (\theta )\cdot T(x)\right]$

or equivalently

$f_{X}{\left(x\ {\big |}\ \theta \right)}=\exp \left[\eta (\theta )\cdot T(x)-A(\theta )+B(x)\right].$

In terms of log probability, $\log(f_{X}{\left(x\ {\big |}\ \theta \right)})=\eta (\theta )\cdot T(x)-A(\theta )+B(x).$

Note that $g(\theta )=e^{-A(\theta )}$ and $h(x)=e^{B(x)}$ .

#### Support must be independent of θ

Importantly, the *support* of $f_{X}{\left(x{\big |}\theta \right)}$ (all the possible x values for which $f_{X}\!\left(x{\big |}\theta \right)$ is greater than 0 ) is required to *not* depend on $\theta ~.$ This requirement can be used to exclude a parametric family distribution from being an exponential family.

For example: The Pareto distribution has a pdf which is defined for $x\geq x_{\mathsf {m}}$ (the minimum value, $x_{m}\ ,$ being the scale parameter) and its support, therefore, has a lower limit of $x_{\mathsf {m}}~.$ Since the support of $f_{\alpha ,x_{m}}\!(x)$ is dependent on the value of the parameter, the family of Pareto distributions does not form an exponential family of distributions (at least when $x_{m}$ is unknown).

Another example: Bernoulli-type distributions – binomial, negative binomial, geometric distribution, and similar – can only be included in the exponential class if the number of Bernoulli trials, n, is treated as a fixed constant – excluded from the free parameter(s) $\theta$ – since the allowed number of trials sets the limits for the number of "successes" or "failures" that can be observed in a set of trials.

#### Vector valued x and θ

Often x is a vector of measurements, in which case $T(x)$ may be a function from the space of possible values of x to the real numbers.

More generally, $\eta (\theta )$ and $T(x)$ can each be vector-valued such that $\eta (\theta )\cdot T(x)$ is real-valued. However, see the discussion below on vector parameters, regarding the *curved* exponential family.

#### Canonical formulation

If $\eta (\theta )=\theta \ ,$ then the exponential family is said to be in *canonical form*. By defining a transformed parameter $\eta =\eta (\theta )\ ,$ it is always possible to convert an exponential family to canonical form. The canonical form is non-unique, since $\eta (\theta )$ can be multiplied by any nonzero constant, provided that *T*(*x*) is multiplied by that constant's reciprocal, or a constant *c* can be added to $\eta (\theta )$ and *h*(*x*) multiplied by $\exp \left[{-c}\cdot T(x)\,\right]$ to offset it. In the special case that $\eta (\theta )=\theta$ and *T*(*x*) = *x*, then the family is called a *natural exponential family*.

Even when x is a scalar, and there is only a single parameter, the functions $\eta (\theta )$ and $T(x)$ can still be vectors, as described below.

The function $A(\theta )\ ,$ or equivalently $g(\theta )\ ,$ is automatically determined once the other functions have been chosen, since it must assume a form that causes the distribution to be normalized (sum or integrate to one over the entire domain). Furthermore, both of these functions can always be written as functions of $\eta \ ,$ even when $\eta (\theta )$ is not a one-to-one function, i.e. two or more different values of $\theta$ map to the same value of $\eta (\theta )\ ,$ and hence $\eta (\theta )$ cannot be inverted. In such a case, all values of $\theta$ mapping to the same $\eta (\theta )$ will also have the same value for $A(\theta )$ and $g(\theta )~.$

### Factorization of the variables involved

What is important to note, and what characterizes all exponential family variants, is that the parameter(s) and the observation variable(s) must factorize (can be separated into products each of which involves only one type of variable), either directly or within either part (the base or exponent) of an exponentiation operation. Generally, this means that all of the factors constituting the density or mass function must be of one of the following forms:

${\begin{aligned}f(x),&&c^{f(x)},&&{[f(x)]}^{c},&&{[f(x)]}^{g(\theta )},&&{[f(x)]}^{h(x)g(\theta )},\\g(\theta ),&&c^{g(\theta )},&&{[g(\theta )]}^{c},&&{[g(\theta )]}^{f(x)},&&~~{\mathsf {or}}~~{[g(\theta )]}^{h(x)j(\theta )},\end{aligned}}$

where *f* and *h* are arbitrary functions of x, the observed statistical variable; *g* and *j* are arbitrary functions of $\theta ,$ the fixed parameters defining the shape of the distribution; and *c* is any arbitrary constant expression (i.e. a number or an expression that does not change with either x or $\theta$ ).

There are further restrictions on how many such factors can occur. For example, the two expressions:

${[f(x)g(\theta )]}^{h(x)j(\theta )},\qquad {[f(x)]}^{h(x)j(\theta )}{[g(\theta )]}^{h(x)j(\theta )},$

are the same, i.e. a product of two "allowed" factors. However, when rewritten into the factorized form,

${\begin{aligned}{\left[f(x)g(\theta )\right]}^{h(x)j(\theta )}&={\left[f(x)\right]}^{h(x)j(\theta )}{\left[g(\theta )\right]}^{h(x)j(\theta )}\\[4pt]&=\exp \left\{{[h(x)\log f(x)]j(\theta )+h(x)[j(\theta )\log g(\theta )]}\right\},\end{aligned}}$

it can be seen that it cannot be expressed in the required form. (However, a form of this sort is a member of a *curved exponential family*, which allows multiple factorized terms in the exponent.)

To see why an expression of the form

${[f(x)]}^{g(\theta )}$

qualifies, ${[f(x)]}^{g(\theta )}=e^{g(\theta )\log f(x)}$

and hence factorizes inside of the exponent. Similarly,

${[f(x)]}^{h(x)g(\theta )}=e^{h(x)g(\theta )\log f(x)}=e^{[h(x)\log f(x)]g(\theta )}$

and again factorizes inside of the exponent.

A factor consisting of a sum where both types of variables are involved (e.g. a factor of the form $1+f(x)g(\theta )$ ) cannot be factorized in this fashion (except in some cases where occurring directly in an exponent); this is why, for example, the Cauchy distribution and Student's *t* distribution are not exponential families.

### Vector parameter

The definition in terms of one *real-number* parameter can be extended to one *real-vector* parameter

${\boldsymbol {\theta }}\equiv {\begin{bmatrix}\theta _{1}&\theta _{2}&\cdots &\theta _{s}\end{bmatrix}}^{\mathsf {T}}.$

A family of distributions is said to belong to a vector exponential family if the probability density function (or probability mass function, for discrete distributions) can be written as

$f_{X}(x\mid {\boldsymbol {\theta }})=h(x)\,\exp \left(\sum _{i=1}^{s}\eta _{i}({\boldsymbol {\theta }})T_{i}(x)-A({\boldsymbol {\theta }})\right)~,$

or in a more compact form,

$f_{X}(x\mid {\boldsymbol {\theta }})=h(x)\,\exp \left[{\boldsymbol {\eta }}({\boldsymbol {\theta }})\cdot \mathbf {T} (x)-A({\boldsymbol {\theta }})\right]$

This form writes the sum as a dot product of vector-valued functions ${\boldsymbol {\eta }}({\boldsymbol {\theta }})$ and *T*(*x*).

An alternative, equivalent form often seen is

$f_{X}(x\mid {\boldsymbol {\theta }})=h(x)\,g({\boldsymbol {\theta }})\,\exp \left[{\boldsymbol {\eta }}({\boldsymbol {\theta }})\cdot \mathbf {T} (x)\right]$

As in the scalar valued case, the exponential family is said to be in *canonical form* if

$\eta _{i}({\boldsymbol {\theta }})=\theta _{i}~,\quad \forall i\,.$

A vector exponential family is said to be *curved* if the dimension of

${\boldsymbol {\theta }}\equiv {\begin{bmatrix}\theta _{1}&\theta _{2}&\cdots &\theta _{d}\end{bmatrix}}^{\mathsf {T}}$

is less than the dimension of the vector

${\boldsymbol {\eta }}({\boldsymbol {\theta }})\equiv {\begin{bmatrix}\eta _{1}{\!({\boldsymbol {\theta }})}&\eta _{2}{\!({\boldsymbol {\theta }})}&\cdots &\eta _{s}{\!({\boldsymbol {\theta }})}\end{bmatrix}}^{\mathsf {T}}~.$

That is, if the *dimension*, d, of the parameter vector is less than the *number of functions*, s, of the parameter vector in the above representation of the probability density function. Most common distributions in the exponential family are *not* curved, and many algorithms designed to work with any exponential family implicitly or explicitly assume that the distribution is not curved.

Just as in the case of a scalar-valued parameter, the function $A({\boldsymbol {\theta }})$ or equivalently $g({\boldsymbol {\theta }})$ is automatically determined by the normalization constraint, once the other functions have been chosen. Even if ${\boldsymbol {\eta }}({\boldsymbol {\theta }})$ is not one-to-one, functions $A({\boldsymbol {\eta }})$ and $g({\boldsymbol {\eta }})$ can be defined by requiring that the distribution is normalized for each value of the natural parameter ${\boldsymbol {\eta }}$ . This yields the *canonical form*

$f_{X}(x\mid {\boldsymbol {\eta }})=h(x)\exp \left[{\boldsymbol {\eta }}\cdot \mathbf {T} (x)-A({\boldsymbol {\eta }})\right],$

or equivalently

$f_{X}(x\mid {\boldsymbol {\eta }})=h(x)g({\boldsymbol {\eta }})\exp \left[{\boldsymbol {\eta }}\cdot \mathbf {T} (x)\right].$

The above forms may sometimes be seen with ${\boldsymbol {\eta }}^{\mathsf {T}}\mathbf {T} (x)$ in place of ${\boldsymbol {\eta }}\cdot \mathbf {T} (x)\,$ . These are exactly equivalent formulations, merely using different notation for the dot product.

### Vector parameter, vector variable

The vector-parameter form over a single scalar-valued random variable can be trivially expanded to cover a joint distribution over a vector of random variables. The resulting distribution is simply the same as the above distribution for a scalar-valued random variable with each occurrence of the scalar x replaced by the vector

$\mathbf {x} ={\begin{bmatrix}x_{1}&x_{2}&\cdots &x_{k}\end{bmatrix}}^{\mathsf {T}}.$

The dimensions k of the random variable need not match the dimension d of the parameter vector, nor (in the case of a curved exponential function) the dimension s of the natural parameter ${\boldsymbol {\eta }}$ and sufficient statistic **T**(**x**) .

The distribution in this case is written as

$f_{X}{\left(\mathbf {x} \mid {\boldsymbol {\theta }}\right)}=h(\mathbf {x} )\,\exp \!\left[\sum _{i=1}^{s}\eta _{i}({\boldsymbol {\theta }})T_{i}(\mathbf {x} )-A({\boldsymbol {\theta }})\right]$

Or more compactly as

$f_{X}{\left(\mathbf {x} \mid {\boldsymbol {\theta }}\right)}=h(\mathbf {x} )\,\exp \left[{\boldsymbol {\eta }}({\boldsymbol {\theta }})\cdot \mathbf {T} (\mathbf {x} )-A({\boldsymbol {\theta }})\right]$

Or alternatively as

$f_{X}{\left(\mathbf {x} \mid {\boldsymbol {\theta }}\right)}=g({\boldsymbol {\theta }})\,h(\mathbf {x} )\,\exp \left[{\boldsymbol {\eta }}({\boldsymbol {\theta }})\cdot \mathbf {T} (\mathbf {x} )\right]$

### Measure-theoretic formulation

We use cumulative distribution functions (CDF) in order to encompass both discrete and continuous distributions.

Suppose H is a non-decreasing function of a real variable. Then Lebesgue–Stieltjes integrals with respect to $dH(\mathbf {x} )$ are integrals with respect to the *reference measure* of the exponential family generated by H .

Any member of that exponential family has cumulative distribution function

$dF{\left(\mathbf {x} \mid {\boldsymbol {\theta }}\right)}=\exp \left[{\boldsymbol {\eta }}(\theta )\cdot \mathbf {T} (\mathbf {x} )-A({\boldsymbol {\theta }})\right]~dH(\mathbf {x} )\,.$

*H*(*x*) is a Lebesgue–Stieltjes integrator for the reference measure. When the reference measure is finite, it can be normalized and H is actually the cumulative distribution function of a probability distribution. If F is absolutely continuous with a density $f(x)$ with respect to a reference measure $dx$ (typically Lebesgue measure), one can write $dF(x)=f(x)\,dx$ . In this case, H is also absolutely continuous and can be written $dH(x)=h(x)\,dx$ so the formulas reduce to that of the previous paragraphs. If F is discrete, then H is a step function (with steps on the support of F).

Alternatively, we can write the probability measure directly as

$P\left(d\mathbf {x} \mid {\boldsymbol {\theta }}\right)=\exp \left[{\boldsymbol {\eta }}(\theta )\cdot \mathbf {T} (\mathbf {x} )-A({\boldsymbol {\theta }})\right]~\mu (d\mathbf {x} )\,.$

for some reference measure $\mu \,$ .


## Interpretation

In the definitions above, the functions *T*(*x*), *η*(*θ*), and *A*(*η*) were arbitrary. However, these functions have important interpretations in the resulting probability distribution.

- *T*(*x*) is a *sufficient statistic* of the distribution. For exponential families, the sufficient statistic is a function of the data that holds all information the data x provides with regard to the unknown parameter values. This means that, for any data sets x and y , the likelihood ratio is the same, that is ${\frac {f(x;\theta _{1})}{f(x;\theta _{2})}}={\frac {f(y;\theta _{1})}{f(y;\theta _{2})}}$ if *T*(*x*) = *T*(*y*). This is true even if x and y are not equal to each other. The dimension of *T*(*x*) equals the number of parameters of θ and encompasses all of the information regarding the data related to the parameter θ. The sufficient statistic of a set of independent identically distributed data observations is simply the sum of individual sufficient statistics, and encapsulates all the information needed to describe the posterior distribution of the parameters, given the data (and hence to derive any desired estimate of the parameters). (This important property is discussed further below.)
- η is called the *natural parameter*. The set of values of η for which the function $f_{X}(x;\eta )$ is integrable is called the *natural parameter space*. It can be shown that the natural parameter space is always convex.
- *A*(*η*) is called the *log-partition function* because it is the logarithm of a normalization factor, without which $f_{X}(x;\theta )$ would not be a probability distribution: $A(\eta )=\log \left(\int _{X}h(x)\,\exp \left[\eta (\theta )\cdot T(x)\right]\,dx\right)$

The function A is important in its own right, because the mean, variance and other moments of the sufficient statistic *T*(*x*) can be derived simply by differentiating *A*(*η*). For example, because log(*x*) is one of the components of the sufficient statistic of the gamma distribution, $\operatorname {\mathcal {E}} [\log x]$ can be easily determined for this distribution using *A*(*η*). Technically, this is true because $K{\left(u\mid \eta \right)}=A(\eta +u)-A(\eta )\,,$ is the cumulant generating function of the sufficient statistic.


## Properties

Exponential families have a large number of properties that make them extremely useful for statistical analysis. In many cases, it can be shown that *only* exponential families have these properties. Examples:

- Exponential families are the only families with sufficient statistics that can summarize arbitrary amounts of independent identically distributed data using a fixed number of values. (Pitman–Koopman–Darmois theorem)
- Exponential families have conjugate priors, an important property in Bayesian statistics.
- The posterior predictive distribution of an exponential-family random variable with a conjugate prior can always be written in closed form (provided that the normalizing factor of the exponential-family distribution can itself be written in closed form).
- In the mean-field approximation in variational Bayes (used for approximating the posterior distribution in large Bayesian networks), the best approximating posterior distribution of an exponential-family node (a node is a random variable in the context of Bayesian networks) with a conjugate prior is in the same family as the node.

Given an exponential family defined by $f_{X}{\!(x\mid \theta )}=h(x)\exp \left[\theta \cdot T(x)-A(\theta )\right]$ , where $\Theta$ is the parameter space, such that $\theta \in \Theta \subset \mathbb {R} ^{k}$ . Then

- If $\Theta$ has nonempty interior in $\mathbb {R} ^{k}$ , then given any IID samples $X_{1},...,X_{n}\sim f_{X}$ , the statistic ${\textstyle T(X_{1},\dots ,X_{n}):=\sum _{i=1}^{n}T(X_{i})}$ is a complete statistic for $\theta$ .
- T is a minimal statistic for $\theta$ if and only if for all $\theta _{1},\theta _{2}\in \Theta$ , and $x_{1},x_{2}$ in the support of X , if $(\theta _{1}-\theta _{2})\cdot [T(x_{1})-T(x_{2})]=0$ , then $\theta _{1}=\theta _{2}$ or $x_{1}=x_{2}$ .


## Examples

It is critical, when considering the examples in this section, to remember the discussion above about what it means to say that a "distribution" is an exponential family, and in particular to keep in mind that the set of parameters that are allowed to vary is critical in determining whether a "distribution" is or is not an exponential family.

The normal, exponential, log-normal, gamma, chi-squared, beta, Dirichlet, Bernoulli, categorical, Poisson, geometric, inverse Gaussian, ALAAM, von Mises, and von Mises-Fisher distributions are all exponential families.

Some distributions are exponential families only if some of their parameters are held fixed. The family of Pareto distributions with a fixed minimum bound *x*m form an exponential family. The families of binomial and multinomial distributions with fixed number of trials *n* but unknown probability parameter(s) are exponential families. The family of negative binomial distributions with fixed number of failures (a.k.a. stopping-time parameter) *r* is an exponential family. However, when any of the above-mentioned fixed parameters are allowed to vary, the resulting family is not an exponential family.

As mentioned above, as a general rule, the support of an exponential family must remain the same across all parameter settings in the family. This is why the above cases (e.g. binomial with varying number of trials, Pareto with varying minimum bound) are not exponential families — in all of the cases, the parameter in question affects the support (particularly, changing the minimum or maximum possible value). For similar reasons, neither the discrete uniform distribution nor continuous uniform distribution are exponential families as one or both bounds vary.

The Weibull distribution with fixed shape parameter *k* is an exponential family. Unlike in the previous examples, the shape parameter does not affect the support; the fact that allowing it to vary makes the Weibull non-exponential is due rather to the particular form of the Weibull's probability density function (*k* appears in the exponent of an exponent).

In general, distributions that result from a finite or infinite mixture of other distributions, e.g. mixture model densities and compound probability distributions, are *not* exponential families. Examples are typical Gaussian mixture models as well as many heavy-tailed distributions that result from compounding (i.e. infinitely mixing) a distribution with a prior distribution over one of its parameters, e.g. the Student's *t*-distribution (compounding a normal distribution over a gamma-distributed precision prior), and the beta-binomial and Dirichlet-multinomial distributions. Other examples of distributions that are not exponential families are the F-distribution, Cauchy distribution, hypergeometric distribution and logistic distribution.

Following are some detailed examples of the representation of some useful distribution as exponential families.

### Normal distribution: unknown mean, known variance

As a first example, consider a random variable distributed normally with unknown mean μ and *known* variance *σ*2. The probability density function is then

$f_{\sigma }(x;\mu )={\frac {1}{\sqrt {2\pi \sigma ^{2}}}}e^{-(x-\mu )^{2}/2\sigma ^{2}}.$

This is a single-parameter exponential family, as can be seen by setting

${\begin{aligned}T_{\sigma }(x)&={\frac {x}{\sigma }},&h_{\sigma }(x)&={\frac {1}{\sqrt {2\pi \sigma ^{2}}}}e^{-x^{2}/2\sigma ^{2}},\\[4pt]A_{\sigma }(\mu )&={\frac {\mu ^{2}}{2\sigma ^{2}}},&\eta _{\sigma }(\mu )&={\frac {\mu }{\sigma }}.\end{aligned}}$

If *σ* = 1 this is in canonical form, as then *η*(*μ*) = *μ*.

### Normal distribution: unknown mean and unknown variance

Next, consider the case of a normal distribution with unknown mean and unknown variance. The probability density function is then

$f(y;\mu ,\sigma ^{2})={\frac {1}{\sqrt {2\pi \sigma ^{2}}}}e^{-(y-\mu )^{2}/2\sigma ^{2}}.$

This is an exponential family which can be written in canonical form by defining

${\begin{aligned}h(y)&={\frac {1}{\sqrt {2\pi }}},&{\boldsymbol {\eta }}&=\left[{\frac {\mu }{\sigma ^{2}}},~-{\frac {1}{2\sigma ^{2}}}\right],\\T(y)&=\left(y,y^{2}\right)^{\mathsf {T}},&A({\boldsymbol {\eta }})&={\frac {\mu ^{2}}{2\sigma ^{2}}}+\log |\sigma |=-{\frac {\eta _{1}^{2}}{4\eta _{2}}}+{\frac {1}{2}}\log \left|{\frac {1}{2\eta _{2}}}\right|\end{aligned}}$

### Binomial distribution

As an example of a discrete exponential family, consider the binomial distribution with *known* number of trials n. The probability mass function for this distribution is $f(x)={\binom {n}{x}}p^{x}{\left(1-p\right)}^{n-x},\quad x\in \{0,1,2,\ldots ,n\}.$ This can equivalently be written as $f(x)={\binom {n}{x}}\exp \left[x\log \left({\frac {p}{1-p}}\right)+n\log(1-p)\right],$ which shows that the binomial distribution is an exponential family, whose natural parameter is $\eta =\log {\frac {p}{1-p}}.$ This function of *p* is known as logit.


## Table of distributions

The following table shows how to rewrite a number of common distributions as exponential-family distributions with natural parameters. Refer to the flashcards for main exponential families.

For a scalar variable and scalar parameter, the form is as follows:

$f_{X}(x\mid \theta )=h(x)\exp \left[\eta ({\theta })T(x)-A(\eta )\right]$

For a scalar variable and vector parameter:

${\begin{aligned}f_{X}(x\mid {\boldsymbol {\theta }})&=h(x)\,\exp \left[{\boldsymbol {\eta }}({\boldsymbol {\theta }})\cdot \mathbf {T} (x)-A({\boldsymbol {\eta }})\right]\\[4pt]f_{X}(x\mid {\boldsymbol {\theta }})&=h(x)\,g({\boldsymbol {\theta }})\,\exp \left[{\boldsymbol {\eta }}({\boldsymbol {\theta }})\cdot \mathbf {T} (x)\right]\end{aligned}}$

For a vector variable and vector parameter:

$f_{X}(\mathbf {x} \mid {\boldsymbol {\theta }})=h(\mathbf {x} )\,\exp \left[{\boldsymbol {\eta }}({\boldsymbol {\theta }})\cdot \mathbf {T} (\mathbf {x} )-A({\boldsymbol {\eta }})\right]$

The above formulas choose the functional form of the exponential-family with a log-partition function $A({\boldsymbol {\eta }})$ . The reason for this is so that the moments of the sufficient statistics can be calculated easily, simply by differentiating this function. Alternative forms involve either parameterizing this function in terms of the normal parameter ${\boldsymbol {\theta }}$ instead of the natural parameter, and/or using a factor $g({\boldsymbol {\eta }})$ outside of the exponential. The relation between the latter and the former is: ${\begin{aligned}A({\boldsymbol {\eta }})&=-\log g({\boldsymbol {\eta }}),\\[2pt]g({\boldsymbol {\eta }})&=e^{-A({\boldsymbol {\eta }})}\end{aligned}}$ To convert between the representations involving the two types of parameter, use the formulas below for writing one type of parameter in terms of the other.

| Distribution | Parameter(s) **θ** | Natural parameter(s) **η** | Inverse parameter mapping | Base measure *h*(*x*) | Sufficient statistic *T*(*x*) | Log-partition *A*(*η*) | Log-partition *A*(*θ*) |
|---|---|---|---|---|---|---|---|
| Bernoulli distribution | p | $\log {\frac {p}{1-p}}$ This is the logit function. | ${\frac {1}{1+e^{-\eta }}}={\frac {e^{\eta }}{1+e^{\eta }}}$ This is the logistic function. | 1 | x | $\log(1+e^{\eta })$ | $-\log(1-p)$ |
| binomial distribution with known number of trials n | p | $\log {\frac {p}{1-p}}$ | ${\frac {1}{1+e^{-\eta }}}={\frac {e^{\eta }}{1+e^{\eta }}}$ | ${\binom {n}{x}}$ | x | $n\log(1+e^{\eta })$ | $-n\log(1-p)$ |
| Poisson distribution | $\lambda$ | $\log \lambda$ | $e^{\eta }$ | ${\frac {1}{x!}}$ | x | $e^{\eta }$ | $\lambda$ |
| negative binomial distribution with known number of failures r | p | $\log(1-p)$ | $1-e^{\eta }$ | ${\binom {x{+}r{-}1}{x}}$ | x | $-r\log(1-e^{\eta })$ | $-r\log(p)$ |
| exponential distribution | $\lambda$ | $-\lambda$ | $-\eta$ | 1 | x | $-\log(-\eta )$ | $-\log \lambda$ |
| Pareto distribution with known minimum value $x_{m}$ | $\alpha$ | $-\alpha -1$ | $-1-\eta$ | 1 | $\log x$ | ${\begin{aligned}&-\log(-1-\eta )\\&+(1+\eta )\log x_{\mathrm {m} }\end{aligned}}$ | $-\log \left(\alpha x_{\mathrm {m} }^{\alpha }\right)$ |
| Weibull distribution with known shape k | $\lambda$ | $-{\frac {1}{\lambda ^{k}}}$ | $(-\eta )^{-1/k}$ | $x^{k-1}$ | $x^{k}$ | $\log \left(-{\frac {1}{\eta k}}\right)$ | $\log {\frac {\lambda ^{k}}{k}}$ |
| Laplace distribution with known mean $\mu$ | b | $-{\frac {1}{b}}$ | $-{\frac {1}{\eta }}$ | 1 | $\|x-\mu \|$ | $\log \left(-{\frac {2}{\eta }}\right)$ | $\log 2b$ |
| chi-squared distribution | $\nu$ | ${\frac {\nu }{2}}-1$ | $2(\eta +1)$ | $e^{-x/2}$ | $\log x$ | ${\begin{aligned}&\log \Gamma (\eta +1)\\&+(\eta +1)\log 2\end{aligned}}$ | ${\begin{aligned}&\log \Gamma {\left({\tfrac {\nu }{2}}\right)}\\&+{\tfrac {\nu }{2}}\log 2\end{aligned}}$ |
| normal distribution known variance | $\mu$ | ${\frac {\mu }{\sigma }}$ | $\sigma \eta$ | ${\frac {e^{-x^{2}/(2\sigma ^{2})}}{{\sqrt {2\pi }}\sigma }}$ | ${\frac {x}{\sigma }}$ | ${\frac {\eta ^{2}}{2}}$ | ${\frac {\mu ^{2}}{2\sigma ^{2}}}$ |
| continuous Bernoulli distribution | $\lambda$ | $\log {\frac {\lambda }{1-\lambda }}$ | ${\frac {e^{\eta }}{1+e^{\eta }}}$ | 1 | x | $\log {\frac {e^{\eta }-1}{\eta }}$ | ${\begin{aligned}&\log \left({\tfrac {1-2\lambda }{1-\lambda }}\right)\\[1ex]{}-{}&\log ^{2}\left({\tfrac {1}{\lambda }}-1\right)\end{aligned}}$ where log2 refers to the iterated logarithm |
| normal distribution | $\mu ,\ \sigma ^{2}$ | ${\begin{bmatrix}{\dfrac {\mu }{\sigma ^{2}}}\\[1ex]-{\dfrac {1}{2\sigma ^{2}}}\end{bmatrix}}$ | ${\begin{bmatrix}-{\dfrac {\eta _{1}}{2\eta _{2}}}\\[1ex]-{\dfrac {1}{2\eta _{2}}}\end{bmatrix}}$ | ${\frac {1}{\sqrt {2\pi }}}$ | ${\begin{bmatrix}x\\x^{2}\end{bmatrix}}$ | $-{\frac {\eta _{1}^{2}}{4\eta _{2}}}-{\frac {1}{2}}\log(-2\eta _{2})$ | ${\frac {\mu ^{2}}{2\sigma ^{2}}}+\log \sigma$ |
| log-normal distribution | $\mu ,\ \sigma ^{2}$ | ${\begin{bmatrix}{\dfrac {\mu }{\sigma ^{2}}}\\[1ex]-{\dfrac {1}{2\sigma ^{2}}}\end{bmatrix}}$ | ${\begin{bmatrix}-{\dfrac {\eta _{1}}{2\eta _{2}}}\\[1ex]-{\dfrac {1}{2\eta _{2}}}\end{bmatrix}}$ | ${\frac {1}{{\sqrt {2\pi }}x}}$ | ${\begin{bmatrix}\log x\\(\log x)^{2}\end{bmatrix}}$ | $-{\frac {\eta _{1}^{2}}{4\eta _{2}}}-{\frac {1}{2}}\log(-2\eta _{2})$ | ${\frac {\mu ^{2}}{2\sigma ^{2}}}+\log \sigma$ |
| inverse Gaussian distribution | $\mu ,\ \lambda$ | ${\begin{bmatrix}-{\dfrac {\lambda }{2\mu ^{2}}}\\[15pt]-{\dfrac {\lambda }{2}}\end{bmatrix}}$ | ${\begin{bmatrix}{\sqrt {\dfrac {\eta _{2}}{\eta _{1}}}}\\[15pt]-2\eta _{2}\end{bmatrix}}$ | ${\frac {1}{{\sqrt {2\pi }}x^{3/2}}}$ | ${\begin{bmatrix}x\\[5pt]{\dfrac {1}{x}}\end{bmatrix}}$ | $-2{\sqrt {\eta _{1}\eta _{2}}}-{\tfrac {1}{2}}\log(-2\eta _{2})$ | $-{\tfrac {\lambda }{\mu }}-{\tfrac {1}{2}}\log \lambda$ |
| gamma distribution | $\alpha ,\ \beta$ | ${\begin{bmatrix}\alpha -1\\-\beta \end{bmatrix}}$ | ${\begin{bmatrix}\eta _{1}+1\\-\eta _{2}\end{bmatrix}}$ | 1 | ${\begin{bmatrix}\log x\\x\end{bmatrix}}$ | ${\begin{aligned}&\log \Gamma (\eta _{1}+1)\\{}-{}&(\eta _{1}+1)\log(-\eta _{2})\end{aligned}}$ | $\log {\frac {\Gamma (\alpha )}{\beta ^{\alpha }}}$ |
| $k,\ \theta$ | ${\begin{bmatrix}k-1\\[5pt]-{\dfrac {1}{\theta }}\end{bmatrix}}$ | ${\begin{bmatrix}\eta _{1}+1\\[5pt]-{\dfrac {1}{\eta _{2}}}\end{bmatrix}}$ | $\log \left(\theta ^{k}\Gamma (k)\right)$ |   |   |   |   |
| inverse gamma distribution | $\alpha ,\ \beta$ | ${\begin{bmatrix}-\alpha -1\\-\beta \end{bmatrix}}$ | ${\begin{bmatrix}-\eta _{1}-1\\-\eta _{2}\end{bmatrix}}$ | 1 | ${\begin{bmatrix}\log x\\{\frac {1}{x}}\end{bmatrix}}$ | ${\begin{aligned}&\log \Gamma (-\eta _{1}-1)\\+&\left(\eta _{1}+1\right)\log(-\eta _{2})\end{aligned}}$ | $\log {\frac {\Gamma (\alpha )}{\beta ^{\alpha }}}$ |
| generalized inverse Gaussian distribution | $p,\ a,\ b$ | ${\begin{bmatrix}p-1\\-a/2\\-b/2\end{bmatrix}}$ | ${\begin{bmatrix}\eta _{1}+1\\-2\eta _{2}\\-2\eta _{3}\end{bmatrix}}$ | 1 | ${\begin{bmatrix}\log x\\x\\{\frac {1}{x}}\end{bmatrix}}$ | ${\begin{aligned}&\log 2K_{\eta _{1}+1}{\!\left({\sqrt {4\eta _{2}\eta _{3}}}\right)}\\[2pt]{}-{}&{\frac {\eta _{1}+1}{2}}\log {\frac {\eta _{2}}{\eta _{3}}}\end{aligned}}$ | ${\begin{aligned}&\log 2K_{p}({\sqrt {ab}})\\[2pt]&{}-{\frac {p}{2}}\log {\frac {a}{b}}\end{aligned}}$ |
| scaled inverse chi-squared distribution | $\nu ,\ \sigma ^{2}$ | ${\begin{bmatrix}-{\dfrac {\nu }{2}}-1\\[10pt]-{\dfrac {\nu \sigma ^{2}}{2}}\end{bmatrix}}$ | ${\begin{bmatrix}-2(\eta _{1}+1)\\[10pt]{\dfrac {\eta _{2}}{\eta _{1}+1}}\end{bmatrix}}$ | 1 | ${\begin{bmatrix}\log x\\{\frac {1}{x}}\end{bmatrix}}$ | ${\begin{aligned}&\log \Gamma (-\eta _{1}-1)\\[2pt]+&\left(\eta _{1}+1\right)\log(-\eta _{2})\end{aligned}}$ | ${\begin{aligned}&\log \Gamma {\left({\frac {\nu }{2}}\right)}\\[2pt]{}-{}&{\frac {\nu }{2}}\log {\frac {\nu \sigma ^{2}}{2}}\end{aligned}}$ |
| beta distribution (variant 1) | $\alpha ,\ \beta$ | ${\begin{bmatrix}\alpha \\\beta \end{bmatrix}}$ | ${\begin{bmatrix}\eta _{1}\\\eta _{2}\end{bmatrix}}$ | ${\frac {1}{x(1-x)}}$ | ${\begin{bmatrix}\log x\\\log(1{-}x)\end{bmatrix}}$ | $\log {\frac {\Gamma (\eta _{1})\,\Gamma (\eta _{2})}{\Gamma (\eta _{1}+\eta _{2})}}$ | $\log {\frac {\Gamma (\alpha )\,\Gamma (\beta )}{\Gamma (\alpha +\beta )}}$ |
| beta distribution (variant 2) | $\alpha ,\ \beta$ | ${\begin{bmatrix}\alpha -1\\\beta -1\end{bmatrix}}$ | ${\begin{bmatrix}\eta _{1}+1\\\eta _{2}+1\end{bmatrix}}$ | 1 | ${\begin{bmatrix}\log x\\\log(1{-}x)\end{bmatrix}}$ | $\log {\frac {\Gamma (\eta _{1}+1)\,\Gamma (\eta _{2}+1)}{\Gamma (\eta _{1}+\eta _{2}+2)}}$ | $\log {\frac {\Gamma (\alpha )\,\Gamma (\beta )}{\Gamma (\alpha +\beta )}}$ |
| multivariate normal distribution | ${\boldsymbol {\mu }},\ {\boldsymbol {\Sigma }}$ | ${\begin{bmatrix}{\boldsymbol {\Sigma }}^{-1}{\boldsymbol {\mu }}\\[5pt]-{\frac {1}{2}}{\boldsymbol {\Sigma }}^{-1}\end{bmatrix}}$ | ${\begin{bmatrix}-{\frac {1}{2}}{\boldsymbol {\eta }}_{2}^{-1}{\boldsymbol {\eta }}_{1}\\[5pt]-{\frac {1}{2}}{\boldsymbol {\eta }}_{2}^{-1}\end{bmatrix}}$ | $(2\pi )^{-{\frac {k}{2}}}$ | ${\begin{bmatrix}\mathbf {x} \\[5pt]\mathbf {x} \mathbf {x} ^{\mathsf {T}}\end{bmatrix}}$ | ${\begin{aligned}&-{\tfrac {1}{4}}{\boldsymbol {\eta }}_{1}^{\mathsf {T}}{\boldsymbol {\eta }}_{2}^{-1}{\boldsymbol {\eta }}_{1}\\&-{\tfrac {1}{2}}\log \left\|-2{\boldsymbol {\eta }}_{2}\right\|\end{aligned}}$ | ${\begin{aligned}&{\tfrac {1}{2}}{\boldsymbol {\mu }}^{\mathsf {T}}{\boldsymbol {\Sigma }}^{-1}{\boldsymbol {\mu }}\\+&{\tfrac {1}{2}}\log \left\|{\boldsymbol {\Sigma }}\right\|\end{aligned}}$ |
| categorical distribution (variant 1) | $p_{1},\ \ldots ,\,p_{k}$ where ${\textstyle \sum \limits _{i=1}^{k}p_{i}=1}$ | ${\begin{bmatrix}\log p_{1}\\\vdots \\\log p_{k}\end{bmatrix}}$ | ${\begin{bmatrix}e^{\eta _{1}}\\\vdots \\e^{\eta _{k}}\end{bmatrix}}$ where ${\textstyle \sum \limits _{i=1}^{k}e^{\eta _{i}}=1}$ | 1 | ${\begin{bmatrix}[x=1]\\\vdots \\{[x=k]}\end{bmatrix}}$ $[x=i]$ is the Iverson bracket | 0 | 0 |
| categorical distribution (variant 2) | $p_{1},\ \ldots ,\,p_{k}$ where ${\textstyle \sum \limits _{i=1}^{k}p_{i}=1}$ | ${\begin{bmatrix}\log p_{1}+C\\\vdots \\\log p_{k}+C\end{bmatrix}}$ | ${\frac {1}{C}}{\begin{bmatrix}e^{\eta _{1}}\\\vdots \\e^{\eta _{k}}\end{bmatrix}}$ where ${\textstyle C=\sum \limits _{i=1}^{k}e^{\eta _{i}}}$ | 1 | ${\begin{bmatrix}[x=1]\\\vdots \\{[x=k]}\end{bmatrix}}$ $[x=i]$ is the Iverson bracket | 0 | 0 |
| categorical distribution (variant 3) | $p_{1},\ \ldots ,\,p_{k}$ where ${\textstyle p_{k}=1-\sum \limits _{i=1}^{k-1}p_{i}}$ | ${\begin{bmatrix}\log {\dfrac {p_{1}}{p_{k}}}\\[10pt]\vdots \\[5pt]\log {\dfrac {p_{k-1}}{p_{k}}}\\[15pt]0\end{bmatrix}}$ This is the inverse softmax function, a generalization of the logit function. | ${\frac {1}{C_{1}}}{\begin{bmatrix}e^{\eta _{1}}\\[5pt]\vdots \\[5pt]e^{\eta _{k}}\end{bmatrix}}=$ ${\frac {1}{C_{2}}}{\begin{bmatrix}e^{\eta _{1}}\\[5pt]\vdots \\[5pt]e^{\eta _{k-1}}\\[5pt]1\end{bmatrix}}$ where ${\textstyle C_{1}=\sum \limits _{i=1}^{k}e^{\eta _{i}}}$ and ${\textstyle C_{2}=1+\sum \limits _{i=1}^{k-1}e^{\eta _{i}}}$ . This is the softmax function, a generalization of the logistic function. | 1 | ${\begin{bmatrix}[x=1]\\\vdots \\{[x=k]}\end{bmatrix}}$ $[x=i]$ is the Iverson bracket | ${\begin{aligned}&\textstyle \log \left(\sum \limits _{i=1}^{k}e^{\eta _{i}}\right)\\={}&\textstyle \log \left(1+\sum \limits _{i=1}^{k-1}e^{\eta _{i}}\right)\end{aligned}}$ | $-\log p_{k}$ |
| multinomial distribution (variant 1) with known number of trials n | $p_{1},\ \ldots ,\,p_{k}$ where ${\textstyle \sum \limits _{i=1}^{k}p_{i}=1}$ | ${\begin{bmatrix}\log p_{1}\\\vdots \\\log p_{k}\end{bmatrix}}$ | ${\begin{bmatrix}e^{\eta _{1}}\\\vdots \\e^{\eta _{k}}\end{bmatrix}}$ where ${\textstyle \sum \limits _{i=1}^{k}e^{\eta _{i}}=1}$ | ${\frac {n!}{\prod \limits _{i=1}^{k}x_{i}!}}$ | ${\begin{bmatrix}x_{1}\\\vdots \\x_{k}\end{bmatrix}}$ | 0 | 0 |
| multinomial distribution (variant 2) with known number of trials n | $p_{1},\ \ldots ,\,p_{k}$ where ${\textstyle \sum \limits _{i=1}^{k}p_{i}=1}$ | ${\begin{bmatrix}\log p_{1}+C\\\vdots \\\log p_{k}+C\end{bmatrix}}$ | ${\frac {1}{C}}{\begin{bmatrix}e^{\eta _{1}}\\\vdots \\e^{\eta _{k}}\end{bmatrix}}$ where ${\textstyle C=\sum \limits _{i=1}^{k}e^{\eta _{i}}}$ | ${\frac {n!}{\prod \limits _{i=1}^{k}x_{i}!}}$ | ${\begin{bmatrix}x_{1}\\\vdots \\x_{k}\end{bmatrix}}$ | 0 | 0 |
| multinomial distribution (variant 3) with known number of trials n | $p_{1},\ \ldots ,\,p_{k}$ where ${\textstyle p_{k}=1-\sum \limits _{i=1}^{k-1}p_{i}}$ | ${\begin{bmatrix}\log {\dfrac {p_{1}}{p_{k}}}\\[10pt]\vdots \\[5pt]\log {\dfrac {p_{k-1}}{p_{k}}}\\[15pt]0\end{bmatrix}}$ | ${\frac {1}{C_{1}}}{\begin{bmatrix}e^{\eta _{1}}\\[10pt]\vdots \\[5pt]e^{\eta _{k}}\end{bmatrix}}=$ ${\frac {1}{C_{2}}}{\begin{bmatrix}e^{\eta _{1}}\\[5pt]\vdots \\[5pt]e^{\eta _{k-1}}\\[5pt]1\end{bmatrix}}$ where ${\textstyle C_{1}=\sum \limits _{i=1}^{k}e^{\eta _{i}}}$ and ${\textstyle C_{2}=1+\sum \limits _{i=1}^{k-1}e^{\eta _{i}}}$ | ${\frac {n!}{\prod \limits _{i=1}^{k}x_{i}!}}$ | ${\begin{bmatrix}x_{1}\\\vdots \\x_{k}\end{bmatrix}}$ | ${\begin{aligned}&\textstyle n\log \left(\sum \limits _{i=1}^{k}e^{\eta _{i}}\right)\\[4pt]={}&\textstyle n\log \left(1+\sum \limits _{i=1}^{k-1}e^{\eta _{i}}\right)\end{aligned}}$ | $-n\log p_{k}$ |
| Dirichlet distribution (variant 1) | $\alpha _{1},\ \ldots ,\,\alpha _{k}$ | ${\begin{bmatrix}\alpha _{1}\\\vdots \\\alpha _{k}\end{bmatrix}}$ | ${\begin{bmatrix}\eta _{1}\\\vdots \\\eta _{k}\end{bmatrix}}$ | ${\frac {1}{\prod \limits _{i=1}^{k}x_{i}}}$ | ${\begin{bmatrix}\log x_{1}\\\vdots \\\log x_{k}\end{bmatrix}}$ | ${\begin{aligned}\textstyle \sum \limits _{i=1}^{k}\log \Gamma (\eta _{i})\\\textstyle -\log \Gamma {\left(\sum \limits _{i=1}^{k}\eta _{i}\right)}\end{aligned}}$ | ${\begin{aligned}&\textstyle \sum \limits _{i=1}^{k}\log \Gamma (\alpha _{i})\\{}-{}&\textstyle \log \Gamma {\left(\sum \limits _{i=1}^{k}\alpha _{i}\right)}\end{aligned}}$ |
| Dirichlet distribution (variant 2) | $\alpha _{1},\ \ldots ,\,\alpha _{k}$ | ${\begin{bmatrix}\alpha _{1}-1\\\vdots \\\alpha _{k}-1\end{bmatrix}}$ | ${\begin{bmatrix}\eta _{1}+1\\\vdots \\\eta _{k}+1\end{bmatrix}}$ | 1 | ${\begin{bmatrix}\log x_{1}\\\vdots \\\log x_{k}\end{bmatrix}}$ | ${\begin{aligned}&\textstyle \sum \limits _{i=1}^{k}\log \Gamma (\eta _{i}+1)\\{}-{}&\textstyle \log \Gamma {\left(\sum \limits _{i=1}^{k}(\eta _{i}+1)\right)}\end{aligned}}$ | ${\begin{aligned}&\textstyle \sum \limits _{i=1}^{k}\log \Gamma (\alpha _{i})\\{}-{}&\textstyle \log \Gamma {\left(\sum \limits _{i=1}^{k}\alpha _{i}\right)}\end{aligned}}$ |
| Wishart distribution | $\mathbf {V} ,\ n$ | ${\begin{bmatrix}-{\frac {1}{2}}\mathbf {V} ^{-1}\\[5pt]{\dfrac {n{-}p{-}1}{2}}\end{bmatrix}}$ | ${\begin{bmatrix}-{\frac {1}{2}}{\boldsymbol {\eta }}_{1}^{-1}\\[5pt]2\eta _{2}{+}p{+}1\end{bmatrix}}$ | 1 | ${\begin{bmatrix}\mathbf {X} \\\log \|\mathbf {X} \|\end{bmatrix}}$ | ${\begin{aligned}&-\left[\eta _{2}+{\tfrac {p+1}{2}}\right]\log \left\|-{\boldsymbol {\eta }}_{1}\right\|\\&+\log \Gamma _{p}{\left(\eta _{2}+{\tfrac {p+1}{2}}\right)}\\[1ex]=&-{\tfrac {n}{2}}\log \left\|-{\boldsymbol {\eta }}_{1}\right\|\\&+\log \Gamma _{p}{\left({\tfrac {n}{2}}\right)}\\[1ex]={}&\left[\eta _{2}+{\tfrac {p+1}{2}}\right]\log \left(2^{p}\left\|\mathbf {V} \right\|\right)\\&+\log \Gamma _{p}{\left(\eta _{2}+{\tfrac {p+1}{2}}\right)}\end{aligned}}$ Three variants with different parameterizations are given, to facilitate computing moments of the sufficient statistics. | ${\begin{aligned}&{\frac {n}{2}}\log \left(2^{p}\left\|\mathbf {V} \right\|\right)\\[2pt]&+\log \Gamma _{p}{\left({\frac {n}{2}}\right)}\end{aligned}}$ |
| **Note**: Uses the fact that $\operatorname {tr} (\mathbf {A} ^{\mathsf {T}}\mathbf {B} )=\operatorname {vec} (\mathbf {A} )\cdot \operatorname {vec} (\mathbf {B} ),$ i.e. the trace of a matrix product is much like a dot product. The matrix parameters are assumed to be vectorized (laid out in a vector) when inserted into the exponential form. Also, $\mathbf {V}$ and $\mathbf {X}$ are symmetric, so e.g. $\mathbf {V} ^{\mathsf {T}}=\mathbf {V} \ .$ |   |   |   |   |   |   |   |
| inverse Wishart distribution | $\mathbf {\Psi } ,\,m$ | $-{\frac {1}{2}}{\begin{bmatrix}{\boldsymbol {\Psi }}\\[5pt]m{+}p{+}1\end{bmatrix}}$ | $-{\begin{bmatrix}2{\boldsymbol {\eta }}_{1}\\[5pt]2\eta _{2}{+}p{+}1\end{bmatrix}}$ | 1 | ${\begin{bmatrix}\mathbf {X} ^{-1}\\\log \|\mathbf {X} \|\end{bmatrix}}$ | ${\begin{aligned}&\left[\eta _{2}+{\tfrac {p+1}{2}}\right]\log \left\|-{\boldsymbol {\eta }}_{1}\right\|\\&+\log \Gamma _{p}{\left(-\eta _{2}-{\tfrac {p+1}{2}}\right)}\\[1ex]=&-{\tfrac {m}{2}}\log \left\|-{\boldsymbol {\eta }}_{1}\right\|\\&+\log \Gamma _{p}{\left({\tfrac {m}{2}}\right)}\\[1ex]=&-\left[\eta _{2}+{\tfrac {p+1}{2}}\right]\log {\tfrac {2^{p}}{\left\|{\boldsymbol {\Psi }}\right\|}}\\&+\log \Gamma _{p}{\left(-\eta _{2}-{\tfrac {p+1}{2}}\right)}\end{aligned}}$ | ${\begin{aligned}{\frac {m}{2}}\log {\frac {2^{p}}{\|{\boldsymbol {\Psi }}\|}}\\[4pt]+\log \Gamma _{p}{\left({\frac {m}{2}}\right)}\end{aligned}}$ |
| normal-gamma distribution | $\alpha ,\ \beta ,\ \mu ,\ \lambda$ | ${\begin{bmatrix}\alpha -{\frac {1}{2}}\\-\beta -{\dfrac {\lambda \mu ^{2}}{2}}\\\lambda \mu \\-{\dfrac {\lambda }{2}}\end{bmatrix}}$ | ${\begin{bmatrix}\eta _{1}+{\frac {1}{2}}\\-\eta _{2}+{\dfrac {\eta _{3}^{2}}{4\eta _{4}}}\\-{\dfrac {\eta _{3}}{2\eta _{4}}}\\-2\eta _{4}\end{bmatrix}}$ | ${\dfrac {1}{\sqrt {2\pi }}}$ | ${\begin{bmatrix}\log \tau \\\tau \\\tau x\\\tau x^{2}\end{bmatrix}}$ | ${\begin{aligned}&\log \Gamma {\left(\eta _{1}+{\tfrac {1}{2}}\right)}\\[2pt]-{}&{\tfrac {1}{2}}\log \left(-2\eta _{4}\right)\\[2pt]-{}&\left(\eta _{1}+{\tfrac {1}{2}}\right)\log \left({\tfrac {\eta _{3}^{2}}{4\eta _{4}}}-\eta _{2}\right)\end{aligned}}$ | ${\begin{aligned}&\log \Gamma {\left(\alpha \right)}\\[2pt]&-\alpha \log \beta \\[2pt]&-{\tfrac {1}{2}}\log \lambda \end{aligned}}$ |

1. The Iverson bracket is a generalization of the discrete delta-function: If the bracketed expression is true, the bracket has value 1; if the enclosed statement is false, the Iverson bracket is zero. There are many variant notations, e.g. wavey brackets: ⧙*a*=*b*⧘ is equivalent to the [*a*=*b*] notation used above.

The three variants of the categorical distribution and multinomial distribution are due to the fact that the parameters $p_{i}$ are constrained, such that

$\sum _{i=1}^{k}p_{i}=1\,.$

Thus, there are only $k-1$ independent parameters.

- Variant 1 uses k natural parameters with a simple relation between the standard and natural parameters; however, only $k-1$ of the natural parameters are independent, and the set of k natural parameters is nonidentifiable. The constraint on the usual parameters translates to a similar constraint on the natural parameters.
- Variant 2 demonstrates the fact that the entire set of natural parameters is nonidentifiable: Adding any constant value to the natural parameters has no effect on the resulting distribution. However, by using the constraint on the natural parameters, the formula for the normal parameters in terms of the natural parameters can be written in a way that is independent on the constant that is added.
- Variant 3 shows how to make the parameters identifiable in a convenient way by setting $C=-\log p_{k}\ .$ This effectively "pivots" around $p_{k}$ and causes the last natural parameter to have the constant value of 0. All the remaining formulas are written in a way that does not access $p_{k}$ , so that effectively the model has only $k-1$ parameters, both of the usual and natural kind.

Variants 1 and 2 are not actually standard exponential families at all. Rather they are *curved exponential families*, i.e. there are $k-1$ independent parameters embedded in a k -dimensional parameter space. Many of the standard results for exponential families do not apply to curved exponential families. An example is the log-partition function $A(x)$ , which has the value of 0 in the curved cases. In standard exponential families, the derivatives of this function correspond to the moments (more technically, the cumulants) of the sufficient statistics, e.g. the mean and variance. However, a value of 0 suggests that the mean and variance of all the sufficient statistics are uniformly 0, whereas in fact the mean of the i th sufficient statistic should be $p_{i}$ . (This does emerge correctly when using the form of $A(x)$ shown in variant 3.)
