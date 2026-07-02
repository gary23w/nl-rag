---
title: "Variational Bayesian methods (part 1/2)"
source: https://en.wikipedia.org/wiki/Variational_Bayesian_methods
domain: variational-bayes
license: CC-BY-SA-4.0
tags: variational Bayesian methods, evidence lower bound, Kullback Leibler divergence, mean field
fetched: 2026-07-02
part: 1/2
---

# Variational Bayesian methods

**Variational Bayesian methods** are a family of techniques for approximating intractable integrals arising in Bayesian inference and machine learning. They are typically used in complex statistical models consisting of observed variables (usually termed "data") as well as unknown parameters and latent variables, with various sorts of relationships among the three types of random variables, as might be described by a graphical model. As typical in Bayesian inference, the parameters and latent variables are grouped together as "unobserved variables". Variational Bayesian methods are primarily used for two purposes:

1. To provide an analytical approximation to the posterior probability of the unobserved variables, in order to do statistical inference over these variables.
2. To derive a lower bound for the marginal likelihood (sometimes called the *evidence*) of the observed data (i.e. the marginal probability of the data given the model, with marginalization performed over unobserved variables). This is typically used for performing model selection, the general idea being that a higher marginal likelihood for a given model indicates a better fit of the data by that model and hence a greater probability that the model in question was the one that generated the data. (See also the Bayes factor article.)

In the former purpose (that of approximating a posterior probability), variational Bayes is an alternative to Monte Carlo sampling methods—particularly, Markov chain Monte Carlo methods such as Gibbs sampling—for taking a fully Bayesian approach to statistical inference over complex distributions that are difficult to evaluate directly or sample. In particular, whereas Monte Carlo techniques provide a numerical approximation to the exact posterior using a set of samples, variational Bayes provides a locally-optimal, exact analytical solution to an approximation of the posterior.

Variational Bayes can be seen as an extension of the expectation–maximization (EM) algorithm from maximum likelihood (ML) or maximum a posteriori (MAP) estimation of the single most probable value of each parameter to fully Bayesian estimation which computes (an approximation to) the entire posterior distribution of the parameters and latent variables. As in EM, it finds a set of optimal parameter values, and it has the same alternating structure as does EM, based on a set of interlocked (mutually dependent) equations that cannot be solved analytically.

For many applications, variational Bayes produces solutions of comparable accuracy to Gibbs sampling at greater speed. However, deriving the set of equations used to update the parameters iteratively often requires a large amount of work compared with deriving the comparable Gibbs sampling equations. This is the case even for many models that are conceptually quite simple, as is demonstrated below in the case of a basic non-hierarchical model with only two parameters and no latent variables.


## Mathematical derivation

### Problem

In variational inference, the posterior distribution over a set of unobserved variables $\mathbf {Z} =\{Z_{1}\dots Z_{n}\}$ given some data $\mathbf {X}$ is approximated by a so-called **variational distribution**, $Q(\mathbf {Z} ):$

$P(\mathbf {Z} \mid \mathbf {X} )\approx Q(\mathbf {Z} ).$

The distribution $Q(\mathbf {Z} )$ is restricted to belong to a family of distributions of simpler form than $P(\mathbf {Z} \mid \mathbf {X} )$ (e.g. a family of Gaussian distributions), selected with the intention of making $Q(\mathbf {Z} )$ similar to the true posterior, $P(\mathbf {Z} \mid \mathbf {X} )$ .

The similarity (or dissimilarity) is measured in terms of a dissimilarity function $d(Q;P)$ and hence inference is performed by selecting the distribution $Q(\mathbf {Z} )$ that minimizes $d(Q;P)$ .

### KL divergence

The most common type of variational Bayes uses the Kullback–Leibler divergence (KL-divergence) of *Q* from *P* as the choice of dissimilarity function. This choice makes this minimization tractable. The KL-divergence is defined as

$D_{\mathrm {KL} }(Q\parallel P)\triangleq \sum _{\mathbf {Z} }Q(\mathbf {Z} )\log {\frac {Q(\mathbf {Z} )}{P(\mathbf {Z} \mid \mathbf {X} )}}.$

Note that *Q* and *P* are reversed from what one might expect. This use of reversed KL-divergence is conceptually similar to the expectation–maximization algorithm. (Using the KL-divergence in the other way produces the expectation propagation algorithm.)

### Intractability

Variational techniques are typically used to form an approximation for:

$P(\mathbf {Z} \mid \mathbf {X} )={\frac {P(\mathbf {X} \mid \mathbf {Z} )P(\mathbf {Z} )}{P(\mathbf {X} )}}={\frac {P(\mathbf {X} \mid \mathbf {Z} )P(\mathbf {Z} )}{\int _{\mathbf {Z} }P(\mathbf {X} ,\mathbf {Z} ')\,d\mathbf {Z} '}}$

The marginalization over $\mathbf {Z}$ to calculate $P(\mathbf {X} )$ in the denominator is typically intractable, because, for example, the search space of $\mathbf {Z}$ is combinatorially large. Therefore, we seek an approximation, using $Q(\mathbf {Z} )\approx P(\mathbf {Z} \mid \mathbf {X} )$ .

### Evidence lower bound

Given that $P(\mathbf {Z} \mid \mathbf {X} )={\frac {P(\mathbf {X} ,\mathbf {Z} )}{P(\mathbf {X} )}}$ , the KL-divergence above can also be written as

${\begin{array}{rl}D_{\mathrm {KL} }(Q\parallel P)&=\sum _{\mathbf {Z} }Q(\mathbf {Z} )\left[\log {\frac {Q(\mathbf {Z} )}{P(\mathbf {Z} ,\mathbf {X} )}}+\log P(\mathbf {X} )\right]\\&=\sum _{\mathbf {Z} }Q(\mathbf {Z} )\left[\log Q(\mathbf {Z} )-\log P(\mathbf {Z} ,\mathbf {X} )\right]+\sum _{\mathbf {Z} }Q(\mathbf {Z} )\left[\log P(\mathbf {X} )\right]\end{array}}$

Because $P(\mathbf {X} )$ is a constant with respect to $\mathbf {Z}$ and $\sum _{\mathbf {Z} }Q(\mathbf {Z} )=1$ because $Q(\mathbf {Z} )$ is a distribution, we have

$D_{\mathrm {KL} }(Q\parallel P)=\sum _{\mathbf {Z} }Q(\mathbf {Z} )\left[\log Q(\mathbf {Z} )-\log P(\mathbf {Z} ,\mathbf {X} )\right]+\log P(\mathbf {X} )$

which, according to the definition of expected value (for a discrete random variable), can be written as follows

$D_{\mathrm {KL} }(Q\parallel P)=\mathbb {E} _{\mathbf {Q} }\left[\log Q(\mathbf {Z} )-\log P(\mathbf {Z} ,\mathbf {X} )\right]+\log P(\mathbf {X} )$

which can be rearranged to become

${\begin{array}{rl}\log P(\mathbf {X} )&=D_{\mathrm {KL} }(Q\parallel P)-\mathbb {E} _{\mathbf {Q} }\left[\log Q(\mathbf {Z} )-\log P(\mathbf {Z} ,\mathbf {X} )\right]\\&=D_{\mathrm {KL} }(Q\parallel P)+{\mathcal {L}}(Q)\end{array}}$

As the *log-evidence* $\log P(\mathbf {X} )$ is fixed with respect to Q , maximizing the final term ${\mathcal {L}}(Q)$ minimizes the KL divergence of Q from P . By appropriate choice of Q , ${\mathcal {L}}(Q)$ becomes tractable to compute and to maximize. Hence we have both an analytical approximation Q for the posterior $P(\mathbf {Z} \mid \mathbf {X} )$ , and a lower bound ${\mathcal {L}}(Q)$ for the log-evidence $\log P(\mathbf {X} )$ (since the KL-divergence is non-negative).

The lower bound ${\mathcal {L}}(Q)$ is known as the (negative) **variational free energy** in analogy with thermodynamic free energy because it can also be expressed as a negative energy $\operatorname {E} _{Q}[\log P(\mathbf {Z} ,\mathbf {X} )]$ plus the entropy of Q . The term ${\mathcal {L}}(Q)$ is also known as **Evidence Lower Bound**, abbreviated as **ELBO**, to emphasize that it is a lower (worst-case) bound on the log-evidence of the data.

### Proofs

By the generalized Pythagorean theorem of Bregman divergence, of which KL-divergence is a special case, it can be shown that:

$D_{\mathrm {KL} }(Q\parallel P)\geq D_{\mathrm {KL} }(Q\parallel Q^{*})+D_{\mathrm {KL} }(Q^{*}\parallel P),\forall Q^{*}\in {\mathcal {C}}$

where ${\mathcal {C}}$ is a convex set and the equality holds if:

$Q=Q^{*}\triangleq \arg \min _{Q\in {\mathcal {C}}}D_{\mathrm {KL} }(Q\parallel P).$

In this case, the global minimizer $Q^{*}(\mathbf {Z} )=q^{*}(\mathbf {Z} _{1}\mid \mathbf {Z} _{2})q^{*}(\mathbf {Z} _{2})=q^{*}(\mathbf {Z} _{2}\mid \mathbf {Z} _{1})q^{*}(\mathbf {Z} _{1}),$ with $\mathbf {Z} =\{\mathbf {Z_{1}} ,\mathbf {Z_{2}} \},$ can be found as follows:

${\begin{array}{rl}q^{*}(\mathbf {Z} _{2})&={\frac {P(\mathbf {X} )}{\zeta (\mathbf {X} )}}{\frac {P(\mathbf {Z} _{2}\mid \mathbf {X} )}{\exp(D_{\mathrm {KL} }(q^{*}(\mathbf {Z} _{1}\mid \mathbf {Z} _{2})\parallel P(\mathbf {Z} _{1}\mid \mathbf {Z} _{2},\mathbf {X} )))}}\\&={\frac {1}{\zeta (\mathbf {X} )}}\exp \mathbb {E} _{q^{*}(\mathbf {Z} _{1}\mid \mathbf {Z} _{2})}\left(\log {\frac {P(\mathbf {Z} ,\mathbf {X} )}{q^{*}(\mathbf {Z} _{1}\mid \mathbf {Z} _{2})}}\right),\end{array}}$

in which the normalizing constant is:

${\begin{array}{rl}\zeta (\mathbf {X} )&=P(\mathbf {X} )\int _{\mathbf {Z} _{2}}{\frac {P(\mathbf {Z} _{2}\mid \mathbf {X} )}{\exp(D_{\mathrm {KL} }(q^{*}(\mathbf {Z} _{1}\mid \mathbf {Z} _{2})\parallel P(\mathbf {Z} _{1}\mid \mathbf {Z} _{2},\mathbf {X} )))}}\\&=\int _{\mathbf {Z} _{2}}\exp \mathbb {E} _{q^{*}(\mathbf {Z} _{1}\mid \mathbf {Z} _{2})}\left(\log {\frac {P(\mathbf {Z} ,\mathbf {X} )}{q^{*}(\mathbf {Z} _{1}\mid \mathbf {Z} _{2})}}\right).\end{array}}$

The term $\zeta (\mathbf {X} )$ is often called the evidence lower bound (**ELBO**) in practice, since $P(\mathbf {X} )\geq \zeta (\mathbf {X} )=\exp({\mathcal {L}}(Q^{*}))$ , as shown above.

By interchanging the roles of $\mathbf {Z} _{1}$ and $\mathbf {Z} _{2},$ we can iteratively compute the approximated $q^{*}(\mathbf {Z} _{1})$ and $q^{*}(\mathbf {Z} _{2})$ of the true model's marginals $P(\mathbf {Z} _{1}\mid \mathbf {X} )$ and $P(\mathbf {Z} _{2}\mid \mathbf {X} ),$ respectively. Although this iterative scheme is guaranteed to converge monotonically, the converged $Q^{*}$ is only a local minimizer of $D_{\mathrm {KL} }(Q\parallel P)$ .

If the constrained space ${\mathcal {C}}$ is confined within independent space, i.e. $q^{*}(\mathbf {Z} _{1}\mid \mathbf {Z} _{2})=q^{*}(\mathbf {Z_{1}} ),$ the above iterative scheme will become the so-called mean field approximation $Q^{*}(\mathbf {Z} )=q^{*}(\mathbf {Z} _{1})q^{*}(\mathbf {Z} _{2}),$ as shown below.


## Mean field approximation

The variational distribution $Q(\mathbf {Z} )$ is usually assumed to factorize over some partition of the latent variables, i.e. for some partition of the latent variables $\mathbf {Z}$ into $\mathbf {Z} _{1}\dots \mathbf {Z} _{M}$ ,

$Q(\mathbf {Z} )=\prod _{i=1}^{M}q_{i}(\mathbf {Z} _{i}\mid \mathbf {X} )$

It can be shown using the calculus of variations (hence the name "variational Bayes") that the "best" distribution $q_{j}^{*}$ for each of the factors $q_{j}$ (in terms of the distribution minimizing the KL divergence, as described above) satisfies:

$q_{j}^{*}(\mathbf {Z} _{j}\mid \mathbf {X} )={\frac {e^{\operatorname {E} _{q_{-j}^{*}}[\ln p(\mathbf {Z} ,\mathbf {X} )]}}{\int e^{\operatorname {E} _{q_{-j}^{*}}[\ln p(\mathbf {Z} ,\mathbf {X} )]}\,d\mathbf {Z} _{j}}}$

where $\operatorname {E} _{q_{-j}^{*}}[\ln p(\mathbf {Z} ,\mathbf {X} )]$ is the expectation of the logarithm of the joint probability of the data and latent variables, taken with respect to $q^{*}$ over all variables not in the partition: refer to Lemma 4.1 of for a derivation of the distribution $q_{j}^{*}(\mathbf {Z} _{j}\mid \mathbf {X} )$ .

In practice, we usually work in terms of logarithms, i.e.:

$\ln q_{j}^{*}(\mathbf {Z} _{j}\mid \mathbf {X} )=\operatorname {E} _{q_{-j}^{*}}[\ln p(\mathbf {Z} ,\mathbf {X} )]+{\text{constant}}$

The constant in the above expression is related to the normalizing constant (the denominator in the expression above for $q_{j}^{*}$ ) and is usually reinstated by inspection, as the rest of the expression can usually be recognized as being a known type of distribution (e.g. Gaussian, gamma, etc.).

Using the properties of expectations, the expression $\operatorname {E} _{q_{-j}^{*}}[\ln p(\mathbf {Z} ,\mathbf {X} )]$ can usually be simplified into a function of the fixed hyperparameters of the prior distributions over the latent variables and of expectations (and sometimes higher moments such as the variance) of latent variables not in the current partition (i.e. latent variables not included in $\mathbf {Z} _{j}$ ). This creates circular dependencies between the parameters of the distributions over variables in one partition and the expectations of variables in the other partitions. This naturally suggests an iterative algorithm, much like EM (the expectation–maximization algorithm), in which the expectations (and possibly higher moments) of the latent variables are initialized in some fashion (perhaps randomly), and then the parameters of each distribution are computed in turn using the current values of the expectations, after which the expectation of the newly computed distribution is set appropriately according to the computed parameters. An algorithm of this sort is guaranteed to converge.

In other words, for each of the partitions of variables, by simplifying the expression for the distribution over the partition's variables and examining the distribution's functional dependency on the variables in question, the family of the distribution can usually be determined (which in turn determines the value of the constant). The formula for the distribution's parameters will be expressed in terms of the prior distributions' hyperparameters (which are known constants), but also in terms of expectations of functions of variables in other partitions. Usually these expectations can be simplified into functions of expectations of the variables themselves (i.e. the means); sometimes expectations of squared variables (which can be related to the variance of the variables), or expectations of higher powers (i.e. higher moments) also appear. In most cases, the other variables' distributions will be from known families, and the formulas for the relevant expectations can be looked up. However, those formulas depend on those distributions' parameters, which depend in turn on the expectations about other variables. The result is that the formulas for the parameters of each variable's distributions can be expressed as a series of equations with mutual, nonlinear dependencies among the variables. Usually, it is not possible to solve this system of equations directly. However, as described above, the dependencies suggest a simple iterative algorithm, which in most cases is guaranteed to converge. An example will make this process clearer.


## A duality formula for variational inference

The following theorem is referred to as a duality formula for variational inference. It explains some important properties of the variational distributions used in variational Bayes methods.

Theorem Consider two probability spaces $(\Theta ,{\mathcal {F}},P)$ and $(\Theta ,{\mathcal {F}},Q)$ with $Q\ll P$ . Assume that there is a common dominating probability measure $\lambda$ such that $P\ll \lambda$ and $Q\ll \lambda$ . Let h denote any real-valued random variable on $(\Theta ,{\mathcal {F}},P)$ that satisfies $\exp h\in L_{1}(P)$ . Then the following equality holds

$\log E_{P}[\exp h]={\text{sup}}_{Q\ll P}\{E_{Q}[h]-D_{\text{KL}}(Q\parallel P)\}.$

Further, the supremum on the right-hand side is attained if and only if it holds

${\frac {q(\theta )}{p(\theta )}}={\frac {\exp h(\theta )}{E_{P}[\exp h]}},$

almost surely with respect to probability measure Q , where $p(\theta )=dP/d\lambda$ and $q(\theta )=dQ/d\lambda$ denote the Radon–Nikodym derivatives of the probability measures P and Q with respect to $\lambda$ , respectively.


## A basic example

Consider a simple non-hierarchical Bayesian model consisting of a set of i.i.d. observations from a Gaussian distribution, with unknown mean and variance. In the following, we work through this model in great detail to illustrate the workings of the variational Bayes method.

For mathematical convenience, in the following example we work in terms of the precision — i.e. the reciprocal of the variance (or in a multivariate Gaussian, the inverse of the covariance matrix) — rather than the variance itself. (From a theoretical standpoint, precision and variance are equivalent since there is a one-to-one correspondence between the two.)

### The mathematical model

We place conjugate prior distributions on the unknown mean $\mu$ and precision $\tau$ , i.e. the mean also follows a Gaussian distribution while the precision follows a gamma distribution. In other words:

${\begin{aligned}\tau &\sim \operatorname {Gamma} (a_{0},b_{0})\\\mu |\tau &\sim {\mathcal {N}}(\mu _{0},(\lambda _{0}\tau )^{-1})\\\{x_{1},\dots ,x_{N}\}&\sim {\mathcal {N}}(\mu ,\tau ^{-1})\\N&={\text{number of data points}}\end{aligned}}$

The hyperparameters $\mu _{0},\lambda _{0},a_{0}$ and $b_{0}$ in the prior distributions are fixed, given values. They can be set to small positive numbers to give broad prior distributions indicating ignorance about the prior distributions of $\mu$ and $\tau$ .

We are given N data points $\mathbf {X} =\{x_{1},\ldots ,x_{N}\}$ and our goal is to infer the posterior distribution $q(\mu ,\tau )=p(\mu ,\tau \mid x_{1},\ldots ,x_{N})$ of the parameters $\mu$ and $\tau .$

### The joint probability

The joint probability of all variables can be rewritten as

$p(\mathbf {X} ,\mu ,\tau )=p(\mathbf {X} \mid \mu ,\tau )p(\mu \mid \tau )p(\tau )$

where the individual factors are

${\begin{aligned}p(\mathbf {X} \mid \mu ,\tau )&=\prod _{n=1}^{N}{\mathcal {N}}(x_{n}\mid \mu ,\tau ^{-1})\\p(\mu \mid \tau )&={\mathcal {N}}\left(\mu \mid \mu _{0},(\lambda _{0}\tau )^{-1}\right)\\p(\tau )&=\operatorname {Gamma} (\tau \mid a_{0},b_{0})\end{aligned}}$

where

${\begin{aligned}{\mathcal {N}}(x\mid \mu ,\sigma ^{2})&={\frac {1}{\sqrt {2\pi \sigma ^{2}}}}e^{\frac {-(x-\mu )^{2}}{2\sigma ^{2}}}\\\operatorname {Gamma} (\tau \mid a,b)&={\frac {1}{\Gamma (a)}}b^{a}\tau ^{a-1}e^{-b\tau }\end{aligned}}$

### Factorized approximation

Assume that $q(\mu ,\tau )=q(\mu )q(\tau )$ , i.e. that the posterior distribution factorizes into independent factors for $\mu$ and $\tau$ . This type of assumption underlies the variational Bayesian method. The true posterior distribution does not in fact factor this way (in fact, in this simple case, it is known to be a Gaussian-gamma distribution), and hence the result we obtain will be an approximation.

### Derivation of *q*(*μ*)

Then

${\begin{aligned}\ln q_{\mu }^{*}(\mu )&=\operatorname {E} _{\tau }\left[\ln p(\mathbf {X} \mid \mu ,\tau )+\ln p(\mu \mid \tau )+\ln p(\tau )\right]+C\\&=\operatorname {E} _{\tau }\left[\ln p(\mathbf {X} \mid \mu ,\tau )\right]+\operatorname {E} _{\tau }\left[\ln p(\mu \mid \tau )\right]+\operatorname {E} _{\tau }\left[\ln p(\tau )\right]+C\\&=\operatorname {E} _{\tau }\left[\ln \prod _{n=1}^{N}{\mathcal {N}}\left(x_{n}\mid \mu ,\tau ^{-1}\right)\right]+\operatorname {E} _{\tau }\left[\ln {\mathcal {N}}\left(\mu \mid \mu _{0},(\lambda _{0}\tau )^{-1}\right)\right]+C_{2}\\&=\operatorname {E} _{\tau }\left[\ln \prod _{n=1}^{N}{\sqrt {\frac {\tau }{2\pi }}}e^{-{\frac {(x_{n}-\mu )^{2}\tau }{2}}}\right]+\operatorname {E} _{\tau }\left[\ln {\sqrt {\frac {\lambda _{0}\tau }{2\pi }}}e^{-{\frac {(\mu -\mu _{0})^{2}\lambda _{0}\tau }{2}}}\right]+C_{2}\\&=\operatorname {E} _{\tau }\left[\sum _{n=1}^{N}\left({\frac {1}{2}}(\ln \tau -\ln 2\pi )-{\frac {(x_{n}-\mu )^{2}\tau }{2}}\right)\right]+\operatorname {E} _{\tau }\left[{\frac {1}{2}}(\ln \lambda _{0}+\ln \tau -\ln 2\pi )-{\frac {(\mu -\mu _{0})^{2}\lambda _{0}\tau }{2}}\right]+C_{2}\\&=\operatorname {E} _{\tau }\left[\sum _{n=1}^{N}-{\frac {(x_{n}-\mu )^{2}\tau }{2}}\right]+\operatorname {E} _{\tau }\left[-{\frac {(\mu -\mu _{0})^{2}\lambda _{0}\tau }{2}}\right]+\operatorname {E} _{\tau }\left[\sum _{n=1}^{N}{\frac {1}{2}}(\ln \tau -\ln 2\pi )\right]+\operatorname {E} _{\tau }\left[{\frac {1}{2}}(\ln \lambda _{0}+\ln \tau -\ln 2\pi )\right]+C_{2}\\&=\operatorname {E} _{\tau }\left[\sum _{n=1}^{N}-{\frac {(x_{n}-\mu )^{2}\tau }{2}}\right]+\operatorname {E} _{\tau }\left[-{\frac {(\mu -\mu _{0})^{2}\lambda _{0}\tau }{2}}\right]+C_{3}\\&=-{\frac {\operatorname {E} _{\tau }[\tau ]}{2}}\left\{\sum _{n=1}^{N}(x_{n}-\mu )^{2}+\lambda _{0}(\mu -\mu _{0})^{2}\right\}+C_{3}\end{aligned}}$

In the above derivation, C , $C_{2}$ and $C_{3}$ refer to values that are constant with respect to $\mu$ . Note that the term $\operatorname {E} _{\tau }[\ln p(\tau )]$ is not a function of $\mu$ and will have the same value regardless of the value of $\mu$ . Hence in line 3 we can absorb it into the constant term at the end. We do the same thing in line 7.

The last line is simply a quadratic polynomial in $\mu$ . Since this is the logarithm of $q_{\mu }^{*}(\mu )$ , we can see that $q_{\mu }^{*}(\mu )$ itself is a Gaussian distribution.

With a certain amount of tedious math (expanding the squares inside of the braces, separating out and grouping the terms involving $\mu$ and $\mu ^{2}$ and completing the square over $\mu$ ), we can derive the parameters of the Gaussian distribution:

${\begin{aligned}\ln q_{\mu }^{*}(\mu )&=-{\frac {\operatorname {E} _{\tau }[\tau ]}{2}}\left\{\sum _{n=1}^{N}(x_{n}-\mu )^{2}+\lambda _{0}(\mu -\mu _{0})^{2}\right\}+C_{3}\\&=-{\frac {\operatorname {E} _{\tau }[\tau ]}{2}}\left\{\sum _{n=1}^{N}(x_{n}^{2}-2x_{n}\mu +\mu ^{2})+\lambda _{0}(\mu ^{2}-2\mu _{0}\mu +\mu _{0}^{2})\right\}+C_{3}\\&=-{\frac {\operatorname {E} _{\tau }[\tau ]}{2}}\left\{\left(\sum _{n=1}^{N}x_{n}^{2}\right)-2\left(\sum _{n=1}^{N}x_{n}\right)\mu +\left(\sum _{n=1}^{N}\mu ^{2}\right)+\lambda _{0}\mu ^{2}-2\lambda _{0}\mu _{0}\mu +\lambda _{0}\mu _{0}^{2}\right\}+C_{3}\\&=-{\frac {\operatorname {E} _{\tau }[\tau ]}{2}}\left\{(\lambda _{0}+N)\mu ^{2}-2\left(\lambda _{0}\mu _{0}+\sum _{n=1}^{N}x_{n}\right)\mu +\left(\sum _{n=1}^{N}x_{n}^{2}\right)+\lambda _{0}\mu _{0}^{2}\right\}+C_{3}\\&=-{\frac {\operatorname {E} _{\tau }[\tau ]}{2}}\left\{(\lambda _{0}+N)\mu ^{2}-2\left(\lambda _{0}\mu _{0}+\sum _{n=1}^{N}x_{n}\right)\mu \right\}+C_{4}\\&=-{\frac {\operatorname {E} _{\tau }[\tau ]}{2}}\left\{(\lambda _{0}+N)\mu ^{2}-2\left({\frac {\lambda _{0}\mu _{0}+\sum _{n=1}^{N}x_{n}}{\lambda _{0}+N}}\right)(\lambda _{0}+N)\mu \right\}+C_{4}\\&=-{\frac {\operatorname {E} _{\tau }[\tau ]}{2}}\left\{(\lambda _{0}+N)\left(\mu ^{2}-2\left({\frac {\lambda _{0}\mu _{0}+\sum _{n=1}^{N}x_{n}}{\lambda _{0}+N}}\right)\mu \right)\right\}+C_{4}\\&=-{\frac {\operatorname {E} _{\tau }[\tau ]}{2}}\left\{(\lambda _{0}+N)\left(\mu ^{2}-2\left({\frac {\lambda _{0}\mu _{0}+\sum _{n=1}^{N}x_{n}}{\lambda _{0}+N}}\right)\mu +\left({\frac {\lambda _{0}\mu _{0}+\sum _{n=1}^{N}x_{n}}{\lambda _{0}+N}}\right)^{2}-\left({\frac {\lambda _{0}\mu _{0}+\sum _{n=1}^{N}x_{n}}{\lambda _{0}+N}}\right)^{2}\right)\right\}+C_{4}\\&=-{\frac {\operatorname {E} _{\tau }[\tau ]}{2}}\left\{(\lambda _{0}+N)\left(\mu ^{2}-2\left({\frac {\lambda _{0}\mu _{0}+\sum _{n=1}^{N}x_{n}}{\lambda _{0}+N}}\right)\mu +\left({\frac {\lambda _{0}\mu _{0}+\sum _{n=1}^{N}x_{n}}{\lambda _{0}+N}}\right)^{2}\right)\right\}+C_{5}\\&=-{\frac {\operatorname {E} _{\tau }[\tau ]}{2}}\left\{(\lambda _{0}+N)\left(\mu -{\frac {\lambda _{0}\mu _{0}+\sum _{n=1}^{N}x_{n}}{\lambda _{0}+N}}\right)^{2}\right\}+C_{5}\\&=-{\frac {1}{2}}(\lambda _{0}+N)\operatorname {E} _{\tau }[\tau ]\left(\mu -{\frac {\lambda _{0}\mu _{0}+\sum _{n=1}^{N}x_{n}}{\lambda _{0}+N}}\right)^{2}+C_{5}\end{aligned}}$

Note that all of the above steps can be shortened by using the formula for the sum of two quadratics.

In other words:

${\begin{aligned}q_{\mu }^{*}(\mu )&\sim {\mathcal {N}}(\mu \mid \mu _{N},\lambda _{N}^{-1})\\\mu _{N}&={\frac {\lambda _{0}\mu _{0}+N{\bar {x}}}{\lambda _{0}+N}}\\\lambda _{N}&=(\lambda _{0}+N)\operatorname {E} _{\tau }[\tau ]\\{\bar {x}}&={\frac {1}{N}}\sum _{n=1}^{N}x_{n}\end{aligned}}$

### Derivation of q(τ)

The derivation of $q_{\tau }^{*}(\tau )$ is similar to above, although we omit some of the details for the sake of brevity.

${\begin{aligned}\ln q_{\tau }^{*}(\tau )&=\operatorname {E} _{\mu }[\ln p(\mathbf {X} \mid \mu ,\tau )+\ln p(\mu \mid \tau )]+\ln p(\tau )+{\text{constant}}\\&=(a_{0}-1)\ln \tau -b_{0}\tau +{\frac {1}{2}}\ln \tau +{\frac {N}{2}}\ln \tau -{\frac {\tau }{2}}\operatorname {E} _{\mu }\left[\sum _{n=1}^{N}(x_{n}-\mu )^{2}+\lambda _{0}(\mu -\mu _{0})^{2}\right]+{\text{constant}}\end{aligned}}$

Exponentiating both sides, we can see that $q_{\tau }^{*}(\tau )$ is a gamma distribution. Specifically:

${\begin{aligned}q_{\tau }^{*}(\tau )&\sim \operatorname {Gamma} (\tau \mid a_{N},b_{N})\\a_{N}&=a_{0}+{\frac {N+1}{2}}\\b_{N}&=b_{0}+{\frac {1}{2}}\operatorname {E} _{\mu }\left[\sum _{n=1}^{N}(x_{n}-\mu )^{2}+\lambda _{0}(\mu -\mu _{0})^{2}\right]\end{aligned}}$

### Algorithm for computing the parameters

Let us recap the conclusions from the previous sections:

${\begin{aligned}q_{\mu }^{*}(\mu )&\sim {\mathcal {N}}(\mu \mid \mu _{N},\lambda _{N}^{-1})\\\mu _{N}&={\frac {\lambda _{0}\mu _{0}+N{\bar {x}}}{\lambda _{0}+N}}\\\lambda _{N}&=(\lambda _{0}+N)\operatorname {E} _{\tau }[\tau ]\\{\bar {x}}&={\frac {1}{N}}\sum _{n=1}^{N}x_{n}\end{aligned}}$

and

${\begin{aligned}q_{\tau }^{*}(\tau )&\sim \operatorname {Gamma} (\tau \mid a_{N},b_{N})\\a_{N}&=a_{0}+{\frac {N+1}{2}}\\b_{N}&=b_{0}+{\frac {1}{2}}\operatorname {E} _{\mu }\left[\sum _{n=1}^{N}(x_{n}-\mu )^{2}+\lambda _{0}(\mu -\mu _{0})^{2}\right]\end{aligned}}$

In each case, the parameters for the distribution over one of the variables depend on expectations taken with respect to the other variable. We can expand the expectations, using the standard formulas for the expectations of moments of the Gaussian and gamma distributions:

${\begin{aligned}\operatorname {E} [\tau \mid a_{N},b_{N}]&={\frac {a_{N}}{b_{N}}}\\\operatorname {E} \left[\mu \mid \mu _{N},\lambda _{N}^{-1}\right]&=\mu _{N}\\\operatorname {E} \left[X^{2}\right]&=\operatorname {Var} (X)+(\operatorname {E} [X])^{2}\\\operatorname {E} \left[\mu ^{2}\mid \mu _{N},\lambda _{N}^{-1}\right]&=\lambda _{N}^{-1}+\mu _{N}^{2}\end{aligned}}$

Applying these formulas to the above equations is trivial in most cases, but the equation for $b_{N}$ takes more work:

${\begin{aligned}b_{N}&=b_{0}+{\frac {1}{2}}\operatorname {E} _{\mu }\left[\sum _{n=1}^{N}(x_{n}-\mu )^{2}+\lambda _{0}(\mu -\mu _{0})^{2}\right]\\&=b_{0}+{\frac {1}{2}}\operatorname {E} _{\mu }\left[(\lambda _{0}+N)\mu ^{2}-2\left(\lambda _{0}\mu _{0}+\sum _{n=1}^{N}x_{n}\right)\mu +\left(\sum _{n=1}^{N}x_{n}^{2}\right)+\lambda _{0}\mu _{0}^{2}\right]\\&=b_{0}+{\frac {1}{2}}\left[(\lambda _{0}+N)\operatorname {E} _{\mu }[\mu ^{2}]-2\left(\lambda _{0}\mu _{0}+\sum _{n=1}^{N}x_{n}\right)\operatorname {E} _{\mu }[\mu ]+\left(\sum _{n=1}^{N}x_{n}^{2}\right)+\lambda _{0}\mu _{0}^{2}\right]\\&=b_{0}+{\frac {1}{2}}\left[(\lambda _{0}+N)\left(\lambda _{N}^{-1}+\mu _{N}^{2}\right)-2\left(\lambda _{0}\mu _{0}+\sum _{n=1}^{N}x_{n}\right)\mu _{N}+\left(\sum _{n=1}^{N}x_{n}^{2}\right)+\lambda _{0}\mu _{0}^{2}\right]\\\end{aligned}}$

We can then write the parameter equations as follows, without any expectations:

${\begin{aligned}\mu _{N}&={\frac {\lambda _{0}\mu _{0}+N{\bar {x}}}{\lambda _{0}+N}}\\\lambda _{N}&=(\lambda _{0}+N){\frac {a_{N}}{b_{N}}}\\{\bar {x}}&={\frac {1}{N}}\sum _{n=1}^{N}x_{n}\\a_{N}&=a_{0}+{\frac {N+1}{2}}\\b_{N}&=b_{0}+{\frac {1}{2}}\left[(\lambda _{0}+N)\left(\lambda _{N}^{-1}+\mu _{N}^{2}\right)-2\left(\lambda _{0}\mu _{0}+\sum _{n=1}^{N}x_{n}\right)\mu _{N}+\left(\sum _{n=1}^{N}x_{n}^{2}\right)+\lambda _{0}\mu _{0}^{2}\right]\end{aligned}}$

Note that there are circular dependencies among the formulas for $\lambda _{N}$ and $b_{N}$ . This naturally suggests an EM-like algorithm:

1. Compute $\sum _{n=1}^{N}x_{n}$ and $\sum _{n=1}^{N}x_{n}^{2}.$ Use these values to compute $\mu _{N}$ and $a_{N}.$
2. Initialize $\lambda _{N}$ to some arbitrary value.
3. Use the current value of $\lambda _{N},$ along with the known values of the other parameters, to compute $b_{N}$ .
4. Use the current value of $b_{N},$ along with the known values of the other parameters, to compute $\lambda _{N}$ .
5. Repeat the last two steps until convergence (i.e. until neither value has changed more than some small amount).

We then have values for the hyperparameters of the approximating distributions of the posterior parameters, which we can use to compute any properties we want of the posterior — e.g. its mean and variance, a 95% highest-density region (the smallest interval that includes 95% of the total probability), etc.

It can be shown that this algorithm is guaranteed to converge to a local maximum.

Note also that the posterior distributions have the same form as the corresponding prior distributions. We did *not* assume this; the only assumption we made was that the distributions factorize, and the form of the distributions followed naturally. It turns out (see below) that the fact that the posterior distributions have the same form as the prior distributions is not a coincidence, but a general result whenever the prior distributions are members of the exponential family, which is the case for most of the standard distributions.


## Further discussion

### Step-by-step recipe

The above example shows the method by which the variational-Bayesian approximation to a posterior probability density in a given Bayesian network is derived:

1. Describe the network with a graphical model, identifying the observed variables (data) $\mathbf {X}$ and unobserved variables (parameters ${\boldsymbol {\Theta }}$ and latent variables $\mathbf {Z}$ ) and their conditional probability distributions. Variational Bayes will then construct an approximation to the posterior probability $p(\mathbf {Z} ,{\boldsymbol {\Theta }}\mid \mathbf {X} )$ . The approximation has the basic property that it is a factorized distribution, i.e. a product of two or more independent distributions over disjoint subsets of the unobserved variables.
2. Partition the unobserved variables into two or more subsets, over which the independent factors will be derived. There is no universal procedure for doing this; creating too many subsets yields a poor approximation, while creating too few makes the entire variational Bayes procedure intractable. Typically, the first split is to separate the parameters and latent variables; often, this is enough by itself to produce a tractable result. Assume that the partitions are called $\mathbf {Z} _{1},\ldots ,\mathbf {Z} _{M}$ .
3. For a given partition $\mathbf {Z} _{j}$ , write down the formula for the best approximating distribution $q_{j}^{*}(\mathbf {Z} _{j}\mid \mathbf {X} )$ using the basic equation $\ln q_{j}^{*}(\mathbf {Z} _{j}\mid \mathbf {X} )=\operatorname {E} _{i\neq j}[\ln p(\mathbf {Z} ,\mathbf {X} )]+{\text{constant}}$ .
4. Fill in the formula for the joint probability distribution using the graphical model. Any component conditional distributions that don't involve any of the variables in $\mathbf {Z} _{j}$ can be ignored; they will be folded into the constant term.
5. Simplify the formula and apply the expectation operator, following the above example. Ideally, this should simplify into expectations of basic functions of variables not in $\mathbf {Z} _{j}$ (e.g. first or second raw moments, expectation of a logarithm, etc.). In order for the variational Bayes procedure to work well, these expectations should generally be expressible analytically as functions of the parameters and/or hyperparameters of the distributions of these variables. In all cases, these expectation terms are constants with respect to the variables in the current partition.
6. The functional form of the formula with respect to the variables in the current partition indicates the type of distribution. In particular, exponentiating the formula generates the probability density function (PDF) of the distribution (or at least, something proportional to it, with unknown normalization constant). In order for the overall method to be tractable, it should be possible to recognize the functional form as belonging to a known distribution. Significant mathematical manipulation may be required to convert the formula into a form that matches the PDF of a known distribution. When this can be done, the normalization constant can be reinstated by definition, and equations for the parameters of the known distribution can be derived by extracting the appropriate parts of the formula.
7. When all expectations can be replaced analytically with functions of variables not in the current partition, and the PDF put into a form that allows identification with a known distribution, the result is a set of equations expressing the values of the optimum parameters as functions of the parameters of variables in other partitions.
8. When this procedure can be applied to all partitions, the result is a set of mutually linked equations specifying the optimum values of all parameters.
9. An expectation–maximization (EM) type procedure is then applied, picking an initial value for each parameter and the iterating through a series of steps, where at each step we cycle through the equations, updating each parameter in turn. This is guaranteed to converge.

### Most important points

Due to all of the mathematical manipulations involved, it is easy to lose track of the big picture. The important things are:

1. The idea of variational Bayes is to construct an analytical approximation to the posterior probability of the set of unobserved variables (parameters and latent variables), given the data. This means that the form of the solution is similar to other Bayesian inference methods, such as Gibbs sampling — i.e. a distribution that seeks to describe everything that is known about the variables. As in other Bayesian methods — but unlike e.g. in expectation–maximization (EM) or other maximum likelihood methods — both types of unobserved variables (i.e. parameters and latent variables) are treated the same, i.e. as random variables. Estimates for the variables can then be derived in the standard Bayesian ways, e.g. calculating the mean of the distribution to get a single point estimate or deriving a credible interval, highest density region, etc.
2. "Analytical approximation" means that a formula can be written down for the posterior distribution. The formula generally consists of a product of well-known probability distributions, each of which *factorizes* over a set of unobserved variables (i.e. it is conditionally independent of the other variables, given the observed data). This formula is not the true posterior distribution, but an approximation to it; in particular, it will generally agree fairly closely in the lowest moments of the unobserved variables, e.g. the mean and variance.
3. The result of all of the mathematical manipulations is (1) the identity of the probability distributions making up the factors, and (2) mutually dependent formulas for the parameters of these distributions. The actual values of these parameters are computed numerically, through an alternating iterative procedure much like EM.

### Compared with expectation–maximization (EM)

Variational Bayes (VB) is often compared with expectation–maximization (EM). The actual numerical procedure is quite similar, in that both are alternating iterative procedures that successively converge on optimum parameter values. The initial steps to derive the respective procedures are also vaguely similar, both starting out with formulas for probability densities and both involving significant amounts of mathematical manipulations.

However, there are a number of differences. Most important is *what* is being computed.

- EM computes point estimates of posterior distribution of those random variables that can be categorized as "parameters", but only estimates of the actual posterior distributions of the latent variables (at least in "soft EM", and often only when the latent variables are discrete). The point estimates computed are the modes of these parameters; no other information is available.
- VB, on the other hand, computes estimates of the actual posterior distribution of all variables, both parameters and latent variables. When point estimates need to be derived, generally the mean is used rather than the mode, as is normal in Bayesian inference. Concomitant with this, the parameters computed in VB do *not* have the same significance as those in EM. EM computes optimum values of the parameters of the Bayes network itself. VB computes optimum values of the parameters of the distributions used to approximate the parameters and latent variables of the Bayes network. For example, a typical Gaussian mixture model will have parameters for the mean and variance of each of the mixture components. EM would directly estimate optimum values for these parameters. VB, however, would first fit a distribution to these parameters — typically in the form of a prior distribution, e.g. a normal-scaled inverse gamma distribution — and would then compute values for the parameters of this prior distribution, i.e. essentially hyperparameters. In this case, VB would compute optimum estimates of the four parameters of the normal-scaled inverse gamma distribution that describes the joint distribution of the mean and variance of the component.
