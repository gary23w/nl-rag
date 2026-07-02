---
title: "Exponential family (part 2/2)"
source: https://en.wikipedia.org/wiki/Exponential_family
domain: generalized-linear-models
license: CC-BY-SA-4.0
tags: generalized linear model, link function, exponential family, quasi-likelihood
fetched: 2026-07-02
part: 2/2
---

## Moments and cumulants of the sufficient statistic

### Normalization of the distribution

We start with the normalization of the probability distribution. In general, any non-negative function *f*(*x*) that serves as the kernel of a probability distribution (the part encoding all dependence on *x*) can be made into a proper distribution by normalizing: i.e.

$p(x)={\frac {1}{Z}}f(x)$

where

$Z=\int _{x}f(x)\,dx.$

The factor *Z* is sometimes termed the *normalizer* or *partition function*, based on an analogy to statistical physics.

In the case of an exponential family where $p(x;{\boldsymbol {\eta }})=g({\boldsymbol {\eta }})h(x)e^{{\boldsymbol {\eta }}\cdot \mathbf {T} (x)},$

the kernel is $K(x)=h(x)e^{{\boldsymbol {\eta }}\cdot \mathbf {T} (x)}$ and the partition function is $Z=\int _{x}h(x)e^{{\boldsymbol {\eta }}\cdot \mathbf {T} (x)}\,dx.$

Since the distribution must be normalized, we have

${\begin{aligned}1&=\int _{x}g({\boldsymbol {\eta }})h(x)e^{{\boldsymbol {\eta }}\cdot \mathbf {T} (x)}\,dx\\&=g({\boldsymbol {\eta }})\int _{x}h(x)e^{{\boldsymbol {\eta }}\cdot \mathbf {T} (x)}\,dx\\[1ex]&=g({\boldsymbol {\eta }})Z.\end{aligned}}$

In other words, $g({\boldsymbol {\eta }})={\frac {1}{Z}}$ or equivalently $A({\boldsymbol {\eta }})=-\log g({\boldsymbol {\eta }})=\log Z.$

This justifies calling *A* the *log-normalizer* or *log-partition function*.

### Moment-generating function of the sufficient statistic

Now, the moment-generating function of *T*(*x*) is

${\begin{aligned}M_{T}(u)&\equiv \operatorname {E} \left[\exp \left(u^{\mathsf {T}}T(x)\right)\mid \eta \right]\\&=\int _{x}h(x)\,\exp \left[(\eta +u)^{\mathsf {T}}T(x)-A(\eta )\right]\,dx\\[1ex]&=e^{A(\eta +u)-A(\eta )}\end{aligned}}$

proving the earlier statement that

$K(u\mid \eta )=A(\eta +u)-A(\eta )$

is the cumulant generating function for *T*.

An important subclass of exponential families are the natural exponential families, which have a similar form for the moment-generating function for the distribution of x.

#### Differential identities for cumulants

In particular, using the properties of the cumulant generating function,

$\operatorname {E} (T_{j})={\frac {\partial A(\eta )}{\partial \eta _{j}}}$

and

$\operatorname {cov} \left(T_{i},\,T_{j}\right)={\frac {\partial ^{2}A(\eta )}{\partial \eta _{i}\,\partial \eta _{j}}}.$

The first two raw moments and all mixed second moments can be recovered from these two identities. Higher-order moments and cumulants are obtained by higher derivatives. This technique is often useful when *T* is a complicated function of the data, whose moments are difficult to calculate by integration.

Another way to see this that does not rely on the theory of cumulants is to begin from the fact that the distribution of an exponential family must be normalized, and differentiate. We illustrate using the simple case of a one-dimensional parameter, but an analogous derivation holds more generally.

In the one-dimensional case, we have $p(x)=g(\eta )h(x)e^{\eta T(x)}.$

This must be normalized, so

$1=\int _{x}p(x)\,dx=\int _{x}g(\eta )h(x)e^{\eta T(x)}\,dx=g(\eta )\int _{x}h(x)e^{\eta T(x)}\,dx.$

Take the derivative of both sides with respect to η:

${\begin{aligned}0&=g(\eta ){\frac {d}{d\eta }}\int _{x}h(x)e^{\eta T(x)}\,dx+g'(\eta )\int _{x}h(x)e^{\eta T(x)}\,dx\\[1ex]&=g(\eta )\int _{x}h(x)\left({\frac {d}{d\eta }}e^{\eta T(x)}\right)\,dx+g'(\eta )\int _{x}h(x)e^{\eta T(x)}\,dx\\[1ex]&=g(\eta )\int _{x}h(x)e^{\eta T(x)}T(x)\,dx+g'(\eta )\int _{x}h(x)e^{\eta T(x)}\,dx\\[1ex]&=\int _{x}T(x)g(\eta )h(x)e^{\eta T(x)}\,dx+{\frac {g'(\eta )}{g(\eta )}}\int _{x}g(\eta )h(x)e^{\eta T(x)}\,dx\\[1ex]&=\int _{x}T(x)p(x)\,dx+{\frac {g'(\eta )}{g(\eta )}}\int _{x}p(x)\,dx\\[1ex]&=\operatorname {E} [T(x)]+{\frac {g'(\eta )}{g(\eta )}}\\[1ex]&=\operatorname {E} [T(x)]+{\frac {d}{d\eta }}\log g(\eta )\end{aligned}}$

Therefore, $\operatorname {E} [T(x)]=-{\frac {d}{d\eta }}\log g(\eta )={\frac {d}{d\eta }}A(\eta ).$

#### Example 1

As an introductory example, consider the gamma distribution, whose distribution is defined by

$p(x)={\frac {\beta ^{\alpha }}{\Gamma (\alpha )}}x^{\alpha -1}e^{-\beta x}.$

Referring to the above table, we can see that the natural parameter is given by

${\begin{aligned}\eta _{1}&=\alpha -1,\\\eta _{2}&=-\beta ,\end{aligned}}$

the reverse substitutions are

${\begin{aligned}\alpha &=\eta _{1}+1,\\\beta &=-\eta _{2},\end{aligned}}$

the sufficient statistics are (log *x*, x), and the log-partition function is

$A(\eta _{1},\eta _{2})=\log \Gamma (\eta _{1}+1)-(\eta _{1}+1)\log(-\eta _{2}).$

We can find the mean of the sufficient statistics as follows. First, for *η*1:

${\begin{aligned}\operatorname {E} [\log x]&={\frac {\partial }{\partial \eta _{1}}}A(\eta _{1},\eta _{2})\\[0.5ex]&={\frac {\partial }{\partial \eta _{1}}}\left[\log \Gamma (\eta _{1}+1)-(\eta _{1}+1)\log(-\eta _{2})\right]\\[1ex]&=\psi (\eta _{1}+1)-\log(-\eta _{2})\\[1ex]&=\psi (\alpha )-\log \beta ,\end{aligned}}$

Where $\psi (x)$ is the digamma function (derivative of log gamma), and we used the reverse substitutions in the last step.

Now, for *η*2:

${\begin{aligned}\operatorname {E} [x]&={\frac {\partial }{\partial \eta _{2}}}A(\eta _{1},\eta _{2})\\[1ex]&={\frac {\partial }{\partial \eta _{2}}}\left[\log \Gamma (\eta _{1}+1)-(\eta _{1}+1)\log(-\eta _{2})\right]\\[1ex]&=-(\eta _{1}+1){\frac {1}{-\eta _{2}}}(-1)={\frac {\eta _{1}+1}{-\eta _{2}}}={\frac {\alpha }{\beta }},\end{aligned}}$

again making the reverse substitution in the last step.

To compute the variance of x, we just differentiate again:

${\begin{aligned}\operatorname {Var} (x)&={\frac {\partial ^{2}}{\partial \eta _{2}^{2}}}A{\left(\eta _{1},\eta _{2}\right)}={\frac {\partial }{\partial \eta _{2}}}{\frac {\eta _{1}+1}{-\eta _{2}}}\\[1ex]&={\frac {\eta _{1}+1}{\eta _{2}^{2}}}={\frac {\alpha }{\beta ^{2}}}.\end{aligned}}$

All of these calculations can be done using integration, making use of various properties of the gamma function, but this requires significantly more work.

#### Example 2

As another example consider a real valued random variable X with density

$p_{\theta }(x)={\frac {\theta e^{-x}}{\left(1+e^{-x}\right)^{\theta +1}}}$

indexed by shape parameter $\theta \in (0,\infty )$ (this is called the skew-logistic distribution). The density can be rewritten as

${\frac {e^{-x}}{1+e^{-x}}}\exp[-\theta \log \left(1+e^{-x})+\log(\theta )\right]$

Notice this is an exponential family with natural parameter

$\eta =-\theta ,$

sufficient statistic

$T=\log \left(1+e^{-x}\right),$

and log-partition function

$A(\eta )=-\log(\theta )=-\log(-\eta )$

So using the first identity,

$\operatorname {E} \left[\log \left(1+e^{-X}\right)\right]=\operatorname {E} (T)={\frac {\partial A(\eta )}{\partial \eta }}={\frac {\partial }{\partial \eta }}[-\log(-\eta )]={\frac {1}{-\eta }}={\frac {1}{\theta }},$

and using the second identity

$\operatorname {var} \left[\log \left(1+e^{-X}\right)\right]={\frac {\partial ^{2}A(\eta )}{\partial \eta ^{2}}}={\frac {\partial }{\partial \eta }}\left[{\frac {1}{-\eta }}\right]={\frac {1}{{\left(-\eta \right)}^{2}}}={\frac {1}{\theta ^{2}}}.$

This example illustrates a case where using this method is very simple, but the direct calculation would be nearly impossible.

#### Example 3

The final example is one where integration would be extremely difficult. This is the case of the Wishart distribution, which is defined over matrices. Even taking derivatives is a bit tricky, as it involves matrix calculus, but the respective identities are listed in that article.

From the above table, we can see that the natural parameter is given by

${\begin{aligned}{\boldsymbol {\eta }}_{1}&=-{\tfrac {1}{2}}\mathbf {V} ^{-1},\\\eta _{2}&={\hphantom {-}}{\tfrac {1}{2}}\left(n-p-1\right),\end{aligned}}$

the reverse substitutions are

${\begin{aligned}\mathbf {V} &=-{\tfrac {1}{2}}{\boldsymbol {\eta }}_{1}^{-1},\\n&=2\eta _{2}+p+1,\end{aligned}}$

and the sufficient statistics are $(\mathbf {X} ,\log |\mathbf {X} |).$

The log-partition function is written in various forms in the table, to facilitate differentiation and back-substitution. We use the following forms:

${\begin{aligned}A({\boldsymbol {\eta }}_{1},n)&=-{\frac {n}{2}}\log \left|-{\boldsymbol {\eta }}_{1}\right|+\log \Gamma _{p}{\left({\frac {n}{2}}\right)},\\[1ex]A(\mathbf {V} ,\eta _{2})&=\left(\eta _{2}+{\frac {p+1}{2}}\right)\log \left(2^{p}\left|\mathbf {V} \right|\right)+\log \Gamma _{p}{\left(\eta _{2}+{\frac {p+1}{2}}\right)}.\end{aligned}}$

**Expectation of **X** (associated with ***η***1)**

To differentiate with respect to ***η***1, we need the following matrix calculus identity:

${\frac {\partial \log |a\mathbf {X} |}{\partial \mathbf {X} }}=(\mathbf {X} ^{-1})^{\mathsf {T}}$

Then:

${\begin{aligned}\operatorname {E} [\mathbf {X} ]&={\frac {\partial }{\partial {\boldsymbol {\eta }}_{1}}}A\left({\boldsymbol {\eta }}_{1},\ldots \right)\\[1ex]&={\frac {\partial }{\partial {\boldsymbol {\eta }}_{1}}}\left[-{\frac {n}{2}}\log \left|-{\boldsymbol {\eta }}_{1}\right|+\log \Gamma _{p}{\left({\frac {n}{2}}\right)}\right]\\[1ex]&=-{\frac {n}{2}}({\boldsymbol {\eta }}_{1}^{-1})^{\mathsf {T}}\\[1ex]&={\frac {n}{2}}(-{\boldsymbol {\eta }}_{1}^{-1})^{\mathsf {T}}\\[1ex]&=n(\mathbf {V} )^{\mathsf {T}}\\[1ex]&=n\mathbf {V} \end{aligned}}$

The last line uses the fact that **V** is symmetric, and therefore it is the same when transposed.

**Expectation of log |**X**| (associated with *η*2)**

Now, for *η*2, we first need to expand the part of the log-partition function that involves the multivariate gamma function:

${\begin{aligned}\log \Gamma _{p}(a)&=\log \left(\pi ^{\frac {p(p-1)}{4}}\prod _{j=1}^{p}\Gamma {\left(a+{\frac {1-j}{2}}\right)}\right)\\&={\frac {p(p-1)}{4}}\log \pi +\sum _{j=1}^{p}\log \Gamma {\left(a+{\frac {1-j}{2}}\right)}\end{aligned}}$

We also need the digamma function:

$\psi (x)={\frac {d}{dx}}\log \Gamma (x).$

Then:

${\begin{aligned}\operatorname {E} [\log |\mathbf {X} |]&={\frac {\partial }{\partial \eta _{2}}}A\left(\ldots ,\eta _{2}\right)\\[1ex]&={\frac {\partial }{\partial \eta _{2}}}\left[-\left(\eta _{2}+{\frac {p+1}{2}}\right)\log \left(2^{p}\left|\mathbf {V} \right|\right)+\log \Gamma _{p}{\left(\eta _{2}+{\frac {p+1}{2}}\right)}\right]\\[1ex]&={\frac {\partial }{\partial \eta _{2}}}\left[\left(\eta _{2}+{\frac {p+1}{2}}\right)\log \left(2^{p}\left|\mathbf {V} \right|\right)\right]+{\frac {\partial }{\partial \eta _{2}}}\left[{\frac {p(p-1)}{4}}\log \pi \right]\\&{\hphantom {=}}+{\frac {\partial }{\partial \eta _{2}}}\sum _{j=1}^{p}\log \Gamma {\left(\eta _{2}+{\frac {p+1}{2}}+{\frac {1-j}{2}}\right)}\\[1ex]&=p\log 2+\log |\mathbf {V} |+\sum _{j=1}^{p}\psi {\left(\eta _{2}+{\frac {p+1}{2}}+{\frac {1-j}{2}}\right)}\\[1ex]&=p\log 2+\log |\mathbf {V} |+\sum _{j=1}^{p}\psi {\left({\frac {n-p-1}{2}}+{\frac {p+1}{2}}+{\frac {1-j}{2}}\right)}\\[1ex]&=p\log 2+\log |\mathbf {V} |+\sum _{j=1}^{p}\psi {\left({\frac {n+1-j}{2}}\right)}\end{aligned}}$

This latter formula is listed in the Wishart distribution article. Both of these expectations are needed when deriving the variational Bayes update equations in a Bayes network involving a Wishart distribution (which is the conjugate prior of the multivariate normal distribution).

Computing these formulas using integration would be much more difficult. The first one, for example, would require matrix integration.


## Entropy

### Relative entropy

The relative entropy (Kullback–Leibler divergence, KL divergence) of two distributions in an exponential family has a simple expression as the Bregman divergence between the natural parameters with respect to the log-normalizer. The relative entropy is defined in terms of an integral, while the Bregman divergence is defined in terms of a derivative and inner product, and thus is easier to calculate and has a closed-form expression (assuming the derivative has a closed-form expression). Further, the Bregman divergence in terms of the natural parameters and the log-normalizer equals the Bregman divergence of the dual parameters (expectation parameters), in the opposite order, for the convex conjugate function.

Fixing an exponential family with log-normalizer ⁠ A ⁠ (with convex conjugate ⁠ $A^{*}$ ⁠), writing $P_{A,\theta }$ for the distribution in this family corresponding a fixed value of the natural parameter ⁠ $\theta$ ⁠ (writing ⁠ $\theta '$ ⁠ for another value, and with ⁠ $\eta ,\eta '$ ⁠ for the corresponding dual expectation/moment parameters), writing KL for the KL divergence, and ⁠ $B_{A}$ ⁠ for the Bregman divergence, the divergences are related as: $\operatorname {KL} (P_{A,\theta }\parallel P_{A,\theta '})=B_{A}(\theta '\parallel \theta )=B_{A^{*}}(\eta \parallel \eta ').$

The KL divergence is conventionally written with respect to the *first* parameter, while the Bregman divergence is conventionally written with respect to the *second* parameter, and thus this can be read as "the relative entropy is equal to the Bregman divergence defined by the log-normalizer on the swapped natural parameters", or equivalently as "equal to the Bregman divergence defined by the dual to the log-normalizer on the expectation parameters".

### Maximum-entropy derivation

Exponential families arise naturally as the answer to the following question: what is the maximum-entropy distribution consistent with given constraints on expected values?

The information entropy of a probability distribution *dF*(*x*) can only be computed with respect to some other probability distribution (or, more generally, a positive measure), and both measures must be mutually absolutely continuous. Accordingly, we need to pick a *reference measure* *dH*(*x*) with the same support as *dF*(*x*).

The entropy of *dF*(*x*) relative to *dH*(*x*) is

$S[dF\mid dH]=-\int {\frac {dF}{dH}}\log {\frac {dF}{dH}}\,dH$

or

$S[dF\mid dH]=\int \log {\frac {dH}{dF}}\,dF$

where *dF*/*dH* and *dH*/*dF* are Radon–Nikodym derivatives. The ordinary definition of entropy for a discrete distribution supported on a set *I*, namely

$S=-\sum _{i\in I}p_{i}\log p_{i}$

*assumes*, though this is seldom pointed out, that *dH* is chosen to be the counting measure on *I*.

Consider now a collection of observable quantities (random variables) *Ti*. The probability distribution *dF* whose entropy with respect to *dH* is greatest, subject to the conditions that the expected value of *T**i* be equal to *ti*, is an exponential family with *dH* as reference measure and (*T*1, ..., *Tn*) as sufficient statistic.

The derivation is a simple variational calculation using Lagrange multipliers. Normalization is imposed by letting *T*0 = 1 be one of the constraints. The natural parameters of the distribution are the Lagrange multipliers, and the normalization factor is the Lagrange multiplier associated to *T*0.

For examples of such derivations, see Maximum entropy probability distribution.


## Role in statistics

### Classical estimation: sufficiency

According to the **Pitman–Koopman–Darmois theorem**, among families of probability distributions whose domain does not vary with the parameter being estimated, only in exponential families is there a sufficient statistic whose dimension remains bounded as sample size increases.

Less tersely, suppose *Xk*, (where *k* = 1, 2, 3, ... *n*) are independent, identically distributed random variables. Only if their distribution is one of the *exponential family* of distributions is there a sufficient statistic ***T***(*X*1, ..., *Xn*) whose number of scalar components does not increase as the sample size *n* increases; the statistic ***T*** may be a vector or a single scalar number, but whatever it is, its size will neither grow nor shrink when more data are obtained.

As a counterexample if these conditions are relaxed, the family of uniform distributions (either discrete or continuous, with either or both bounds unknown) has a sufficient statistic, namely the sample maximum, sample minimum, and sample size, but does not form an exponential family, as the domain varies with the parameters.

### Bayesian estimation: conjugate distributions

Exponential families are also important in Bayesian statistics. In Bayesian statistics a prior distribution is multiplied by a likelihood function and then normalised to produce a posterior distribution. In the case of a likelihood which belongs to an exponential family there exists a conjugate prior, which is often also in an exponential family. A conjugate prior π for the parameter ${\boldsymbol {\eta }}$ of an exponential family

$f(x\mid {\boldsymbol {\eta }})=h(x)\,\exp \left[{\boldsymbol {\eta }}^{\mathsf {T}}\mathbf {T} (x)-A({\boldsymbol {\eta }})\right]$

is given by

$p_{\pi }({\boldsymbol {\eta }}\mid {\boldsymbol {\chi }},\nu )=f({\boldsymbol {\chi }},\nu )\,\exp \left[{\boldsymbol {\eta }}^{\mathsf {T}}{\boldsymbol {\chi }}-\nu A({\boldsymbol {\eta }})\right],$

or equivalently

$p_{\pi }({\boldsymbol {\eta }}\mid {\boldsymbol {\chi }},\nu )=f({\boldsymbol {\chi }},\nu )\,g({\boldsymbol {\eta }})^{\nu }\,\exp \left({\boldsymbol {\eta }}^{\mathsf {T}}{\boldsymbol {\chi }}\right),\qquad {\boldsymbol {\chi }}\in \mathbb {R} ^{s}$

where *s* is the dimension of ${\boldsymbol {\eta }}$ and $\nu >0$ and ${\boldsymbol {\chi }}$ are hyperparameters (parameters controlling parameters). $\nu$ corresponds to the effective number of observations that the prior distribution contributes, and ${\boldsymbol {\chi }}$ corresponds to the total amount that these pseudo-observations contribute to the sufficient statistic over all observations and pseudo-observations. $f({\boldsymbol {\chi }},\nu )$ is a normalization constant that is automatically determined by the remaining functions and serves to ensure that the given function is a probability density function (i.e. it is normalized). $A({\boldsymbol {\eta }})$ and equivalently $g({\boldsymbol {\eta }})$ are the same functions as in the definition of the distribution over which π is the conjugate prior.

A conjugate prior is one which, when combined with the likelihood and normalised, produces a posterior distribution which is of the same type as the prior. For example, if one is estimating the success probability of a binomial distribution, then if one chooses to use a beta distribution as one's prior, the posterior is another beta distribution. This makes the computation of the posterior particularly simple. Similarly, if one is estimating the parameter of a Poisson distribution the use of a gamma prior will lead to another gamma posterior. Conjugate priors are often very flexible and can be very convenient. However, if one's belief about the likely value of the theta parameter of a binomial is represented by (say) a bimodal (two-humped) prior distribution, then this cannot be represented by a beta distribution. It can however be represented by using a mixture density as the prior, here a combination of two beta distributions; this is a form of hyperprior.

An arbitrary likelihood will not belong to an exponential family, and thus in general no conjugate prior exists. The posterior will then have to be computed by numerical methods.

To show that the above prior distribution is a conjugate prior, we can derive the posterior.

First, assume that the probability of a single observation follows an exponential family, parameterized using its natural parameter:

$p_{F}(x\mid {\boldsymbol {\eta }})=h(x)\,g({\boldsymbol {\eta }})\,\exp \left[{\boldsymbol {\eta }}^{\mathsf {T}}\mathbf {T} (x)\right]$

Then, for data $\mathbf {X} =(x_{1},\ldots ,x_{n})$ , the likelihood is computed as follows:

$p(\mathbf {X} \mid {\boldsymbol {\eta }})=\left(\prod _{i=1}^{n}h(x_{i})\right)g({\boldsymbol {\eta }})^{n}\exp \left({\boldsymbol {\eta }}^{\mathsf {T}}\sum _{i=1}^{n}\mathbf {T} (x_{i})\right)$

Then, for the above conjugate prior:

${\begin{aligned}p_{\pi }({\boldsymbol {\eta }}\mid {\boldsymbol {\chi }},\nu )&=f({\boldsymbol {\chi }},\nu )g({\boldsymbol {\eta }})^{\nu }\exp({\boldsymbol {\eta }}^{\mathsf {T}}{\boldsymbol {\chi }})\propto g({\boldsymbol {\eta }})^{\nu }\exp({\boldsymbol {\eta }}^{\mathsf {T}}{\boldsymbol {\chi }})\end{aligned}}$

We can then compute the posterior as follows:

${\begin{aligned}p({\boldsymbol {\eta }}\mid \mathbf {X} ,{\boldsymbol {\chi }},\nu )&\propto p(\mathbf {X} \mid {\boldsymbol {\eta }})p_{\pi }({\boldsymbol {\eta }}\mid {\boldsymbol {\chi }},\nu )\\&=\left(\prod _{i=1}^{n}h(x_{i})\right)g({\boldsymbol {\eta }})^{n}\exp \left({\boldsymbol {\eta }}^{\mathsf {T}}\sum _{i=1}^{n}\mathbf {T} (x_{i})\right)f({\boldsymbol {\chi }},\nu )g({\boldsymbol {\eta }})^{\nu }\exp({\boldsymbol {\eta }}^{\mathsf {T}}{\boldsymbol {\chi }})\\&\propto g({\boldsymbol {\eta }})^{n}\exp \left({\boldsymbol {\eta }}^{\mathsf {T}}\sum _{i=1}^{n}\mathbf {T} (x_{i})\right)g({\boldsymbol {\eta }})^{\nu }\exp({\boldsymbol {\eta }}^{\mathsf {T}}{\boldsymbol {\chi }})\\&=g({\boldsymbol {\eta }})^{\nu +n}\exp \left({\boldsymbol {\eta }}^{\mathsf {T}}\left({\boldsymbol {\chi }}+\sum _{i=1}^{n}\mathbf {T} (x_{i})\right)\right)\end{aligned}}$

The last line is the kernel of the posterior distribution, i.e.

$p({\boldsymbol {\eta }}\mid \mathbf {X} ,{\boldsymbol {\chi }},\nu )=p_{\pi }\left({\boldsymbol {\eta }}\left|~{\boldsymbol {\chi }}+\sum _{i=1}^{n}\mathbf {T} (x_{i}),\nu +n\right.\right)$

This shows that the posterior has the same form as the prior.

The data **X** enters into this equation *only* in the expression

$\mathbf {T} (\mathbf {X} )=\sum _{i=1}^{n}\mathbf {T} (x_{i}),$

which is termed the sufficient statistic of the data. That is, the value of the sufficient statistic is sufficient to completely determine the posterior distribution. The actual data points themselves are not needed, and all sets of data points with the same sufficient statistic will have the same distribution. This is important because the dimension of the sufficient statistic does not grow with the data size — it has only as many components as the components of ${\boldsymbol {\eta }}$ (equivalently, the number of parameters of the distribution of a single data point).

The update equations are as follows:

${\begin{aligned}{\boldsymbol {\chi }}'&={\boldsymbol {\chi }}+\mathbf {T} (\mathbf {X} )\\&={\boldsymbol {\chi }}+\sum _{i=1}^{n}\mathbf {T} (x_{i})\\\nu '&=\nu +n\end{aligned}}$

This shows that the update equations can be written simply in terms of the number of data points and the sufficient statistic of the data. This can be seen clearly in the various examples of update equations shown in the conjugate prior page. Because of the way that the sufficient statistic is computed, it necessarily involves sums of components of the data (in some cases disguised as products or other forms — a product can be written in terms of a sum of logarithms). The cases where the update equations for particular distributions don't exactly match the above forms are cases where the conjugate prior has been expressed using a different parameterization than the one that produces a conjugate prior of the above form — often specifically because the above form is defined over the natural parameter ${\boldsymbol {\eta }}$ while conjugate priors are usually defined over the actual parameter ${\boldsymbol {\theta }}.$

### Unbiased estimation

If the likelihood $z|\eta \sim e^{\eta z}f_{1}(\eta )f_{0}(z)$ is an exponential family, then the unbiased estimator of $\eta$ is $-{\frac {d}{dz}}\ln f_{0}(z)$ .

### Hypothesis testing: uniformly most powerful tests

A one-parameter exponential family has a monotone non-decreasing likelihood ratio in the sufficient statistic *T*(*x*), provided that *η*(*θ*) is non-decreasing. As a consequence, there exists a uniformly most powerful test for testing the hypothesis *H*0: *θ* ≥ *θ*0 *vs*. *H*1: *θ* < *θ*0.

### Generalized linear models

Exponential families form the basis for the distribution functions used in generalized linear models (GLM), a class of model that encompasses many of the commonly used regression models in statistics. Examples include logistic regression using the binomial family and Poisson regression.
