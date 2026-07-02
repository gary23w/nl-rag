---
title: "Evidence lower bound"
source: https://en.wikipedia.org/wiki/Evidence_lower_bound
domain: variational-inference-math
license: CC-BY-SA-4.0
tags: variational bayesian methods, evidence lower bound, mean field theory, kullback-leibler divergence
fetched: 2026-07-02
---

# Evidence lower bound

In variational Bayesian methods, the **evidence lower bound** (often abbreviated **ELBO**, also sometimes called the **variational lower bound** or **negative variational free energy**) is a useful lower bound on the log-likelihood of some observed data.

The ELBO is useful because it provides a guarantee on the worst-case for the log-likelihood of some distribution (e.g. $p(X)$ ) which models a set of data. The actual log-likelihood may be higher (indicating an even better fit to the distribution) because the ELBO includes a Kullback-Leibler divergence (KL divergence) term which decreases the ELBO due to an internal part of the model being inaccurate despite good fit of the model overall. Thus improving the ELBO score indicates either improving the likelihood of the model $p(X)$ or the fit of a component internal to the model, or both, and the ELBO score makes a good loss function, e.g., for training a deep neural network to improve both the model overall and the internal component. (The internal component is $q_{\phi }(\cdot |x)$ , defined in detail later in this article.)

## Definition

Let X and Z be random variables, jointly distributed with distribution $p_{\theta }$ . For example, $p_{\theta }(X)$ is the marginal distribution of X , and $p_{\theta }(Z\mid X)$ is the conditional distribution of Z given X . Then, for a sample $x\sim p_{\text{data}}$ , and any distribution $q_{\phi }$ , the ELBO is defined as $L(\phi ,\theta ;x):=\mathbb {E} _{z\sim q_{\phi }(\cdot |x)}\left[\ln {\frac {p_{\theta }(x,z)}{q_{\phi }(z|x)}}\right].$ The ELBO can equivalently be written as

${\begin{aligned}L(\phi ,\theta ;x)=&\mathbb {E} _{z\sim q_{\phi }(\cdot |x)}\left[\ln {}p_{\theta }(x,z)\right]+H[q_{\phi }(z|x)]\\=&\mathbb {\ln } {}\,p_{\theta }(x)-D_{KL}(q_{\phi }(z|x)||p_{\theta }(z|x)).\\\end{aligned}}$

In the first line, $H[q_{\phi }(z|x)]$ is the entropy of $q_{\phi }$ , which relates the ELBO to the Helmholtz free energy. In the second line, $\ln p_{\theta }(x)$ is called the *evidence* for x , and $D_{KL}(q_{\phi }(z|x)||p_{\theta }(z|x))$ is the Kullback-Leibler divergence between $q_{\phi }$ and $p_{\theta }$ . Since the Kullback-Leibler divergence is non-negative, $L(\phi ,\theta ;x)$ forms a lower bound on the evidence (*ELBO inequality*) $\ln p_{\theta }(x)\geq \mathbb {\mathbb {E} } _{z\sim q_{\phi }(\cdot |x)}\left[\ln {\frac {p_{\theta }(x,z)}{q_{\phi }(z\vert x)}}\right].$

## Motivation

### Variational Bayesian inference

Suppose we have an observable random variable X , and we want to find its true distribution $p^{*}$ . This would allow us to generate data by sampling, and estimate probabilities of future events. In general, it is impossible to find $p^{*}$ exactly, forcing us to search for a good **approximation*.***

That is, we define a sufficiently large parametric family $\{p_{\theta }\}_{\theta \in \Theta }$ of distributions, then solve for $\min _{\theta }L(p_{\theta },p^{*})$ for some loss function L . One possible way to solve this is by considering small variation from $p_{\theta }$ to $p_{\theta +\delta \theta }$ , and solve for $L(p_{\theta },p^{*})-L(p_{\theta +\delta \theta },p^{*})=0$ . This is a problem in the calculus of variations, thus it is called the **variational method**.

Since there are not many explicitly parametrized distribution families (all the classical distribution families, such as the normal distribution, the Gumbel distribution, etc, are far too simplistic to model the true distribution), we consider *implicitly parametrized* probability distributions:

- First, define a simple distribution $p(z)$ over a latent random variable Z . Usually a normal distribution or a uniform distribution suffices.
- Next, define a family of complicated functions $f_{\theta }$ (such as a deep neural network) parametrized by $\theta$ .
- Finally, define a way to convert any $f_{\theta }(z)$ into a distribution (in general simple too, but unrelated to $p(z)$ ) over the observable random variable X . For example, let $f_{\theta }(z)=(f_{1}(z),f_{2}(z))$ have two outputs, then we can define the corresponding distribution over X to be the normal distribution ${\mathcal {N}}(f_{1}(z),e^{f_{2}(z)})$ .

This defines a family of joint distributions $p_{\theta }$ over $(X,Z)$ . It is very easy to sample $(x,z)\sim p_{\theta }$ : simply sample $z\sim p$ , then compute $f_{\theta }(z)$ , and finally sample $x\sim p_{\theta }(\cdot |z)$ using $f_{\theta }(z)$ .

In other words, we have a **generative model** for both the observable and the latent. Now, we consider a distribution $p_{\theta }$ good, if it is a close approximation of $p^{*}$ : $p_{\theta }(X)\approx p^{*}(X)$ since the distribution on the right side is over X only, the distribution on the left side must marginalize the latent variable Z away. In general, it's impossible to perform the integral $p_{\theta }(x)=\int p_{\theta }(x|z)p(z)dz$ , forcing us to perform another approximation.

Since $p_{\theta }(x)={\frac {p_{\theta }(x|z)p(z)}{p_{\theta }(z|x)}}$ (Bayes' rule), it suffices to find a good approximation of $p_{\theta }(z|x)$ . So define another distribution family $q_{\phi }(z|x)$ and use it to approximate $p_{\theta }(z|x)$ . This is a **discriminative model** for the latent.

The entire situation is summarized in the following table:

| X : observable | $X,Z$ | Z : latent |
|---|---|---|
| $p^{*}(x)\approx p_{\theta }(x)\approx {\frac {p_{\theta }(x\|z)p(z)}{q_{\phi }(z\|x)}}$ approximable |   | $p(z)$ , easy |
|   | $p_{\theta }(x\|z)p(z)$ , easy |   |
| $p_{\theta }(z\|x)\approx q_{\phi }(z\|x)$ approximable |   | $p_{\theta }(x\|z)$ , easy |

In **Bayesian** language, X is the observed evidence, and Z is the latent/unobserved. The distribution p over Z is the *prior distribution* over Z , $p_{\theta }(x|z)$ is the likelihood function, and $p_{\theta }(z|x)$ is the *posterior* *distribution* over Z .

Given an observation x , we can *infer* what z likely gave rise to x by computing $p_{\theta }(z|x)$ . The usual Bayesian method is to estimate the integral $p_{\theta }(x)=\int p_{\theta }(x|z)p(z)dz$ , then compute by Bayes' rule $p_{\theta }(z|x)={\frac {p_{\theta }(x|z)p(z)}{p_{\theta }(x)}}$ . This is expensive to perform in general, but if we can simply find a good approximation $q_{\phi }(z|x)\approx p_{\theta }(z|x)$ for most $x,z$ , then we can infer z from x cheaply. Thus, the search for a good $q_{\phi }$ is also called **amortized inference**.

All in all, we have found a problem of **variational Bayesian inference**.

### Deriving the ELBO

A basic result in variational inference is that minimizing the Kullback–Leibler divergence (KL-divergence) is equivalent to maximizing the log-likelihood: $\mathbb {E} _{x\sim p^{*}(x)}[\ln p_{\theta }(x)]=-H(p^{*})-D_{\mathit {KL}}(p^{*}(x)\|p_{\theta }(x))$ where $H(p^{*})=-\mathbb {\mathbb {E} } _{x\sim p^{*}}[\ln p^{*}(x)]$ is the entropy of the true distribution. So if we can maximize $\mathbb {E} _{x\sim p^{*}(x)}[\ln p_{\theta }(x)]$ , we can minimize $D_{\mathit {KL}}(p^{*}(x)\|p_{\theta }(x))$ , and consequently find an accurate approximation $p_{\theta }\approx p^{*}$ .

To maximize $\mathbb {E} _{x\sim p^{*}(x)}[\ln p_{\theta }(x)]$ , we simply sample many $x_{i}\sim p^{*}(x)$ , i.e. use importance sampling $N\max _{\theta }\mathbb {E} _{x\sim p^{*}(x)}[\ln p_{\theta }(x)]\approx \max _{\theta }\sum _{i}\ln p_{\theta }(x_{i})$ where N is the number of samples drawn from the true distribution. This approximation can be seen as overfitting.

In order to maximize $\sum _{i}\ln p_{\theta }(x_{i})$ , it's necessary to find $\ln p_{\theta }(x)$ : $\ln p_{\theta }(x)=\ln \int p_{\theta }(x|z)p(z)dz$ This usually has no closed form and must be estimated. The usual way to estimate integrals is Monte Carlo integration with importance sampling: $\int p_{\theta }(x|z)p(z)dz=\mathbb {E} _{z\sim q_{\phi }(\cdot |x)}\left[{\frac {p_{\theta }(x,z)}{q_{\phi }(z|x)}}\right]$ where $q_{\phi }(z|x)$ is a sampling distribution over z that we use to perform the Monte Carlo integration.

So we see that if we sample $z\sim q_{\phi }(\cdot |x)$ , then ${\frac {p_{\theta }(x,z)}{q_{\phi }(z|x)}}$ is an unbiased estimator of $p_{\theta }(x)$ . Unfortunately, this does not give us an unbiased estimator of $\ln p_{\theta }(x)$ , because $\ln$ is nonlinear. Indeed, we have by Jensen's inequality, $\ln p_{\theta }(x)=\ln \mathbb {E} _{z\sim q_{\phi }(\cdot |x)}\left[{\frac {p_{\theta }(x,z)}{q_{\phi }(z|x)}}\right]\geq \mathbb {E} _{z\sim q_{\phi }(\cdot |x)}\left[\ln {\frac {p_{\theta }(x,z)}{q_{\phi }(z|x)}}\right]$ In fact, all the obvious estimators of $\ln p_{\theta }(x)$ are biased downwards, because no matter how many samples of $z_{i}\sim q_{\phi }(\cdot |x)$ we take, we have by Jensen's inequality: $\mathbb {E} _{z_{i}\sim q_{\phi }(\cdot |x)}\left[\ln \left({\frac {1}{N}}\sum _{i}{\frac {p_{\theta }(x,z_{i})}{q_{\phi }(z_{i}|x)}}\right)\right]\leq \ln \mathbb {E} _{z_{i}\sim q_{\phi }(\cdot |x)}\left[{\frac {1}{N}}\sum _{i}{\frac {p_{\theta }(x,z_{i})}{q_{\phi }(z_{i}|x)}}\right]=\ln p_{\theta }(x)$ Subtracting the right side, we see that the problem comes down to a biased estimator of zero: $\mathbb {E} _{z_{i}\sim q_{\phi }(\cdot |x)}\left[\ln \left({\frac {1}{N}}\sum _{i}{\frac {p_{\theta }(z_{i}|x)}{q_{\phi }(z_{i}|x)}}\right)\right]\leq 0$ At this point, we could branch off towards the development of an importance-weighted autoencoder, but we will instead continue with the simplest case with $N=1$ : $\ln p_{\theta }(x)=\ln \mathbb {E} _{z\sim q_{\phi }(\cdot |x)}\left[{\frac {p_{\theta }(x,z)}{q_{\phi }(z|x)}}\right]\geq \mathbb {E} _{z\sim q_{\phi }(\cdot |x)}\left[\ln {\frac {p_{\theta }(x,z)}{q_{\phi }(z|x)}}\right]$ The tightness of the inequality has a closed form: $\ln p_{\theta }(x)-\mathbb {E} _{z\sim q_{\phi }(\cdot |x)}\left[\ln {\frac {p_{\theta }(x,z)}{q_{\phi }(z|x)}}\right]=D_{\mathit {KL}}(q_{\phi }(\cdot |x)\|p_{\theta }(\cdot |x))\geq 0$ We have thus obtained the ELBO function: $L(\phi ,\theta ;x):=\ln p_{\theta }(x)-D_{\mathit {KL}}(q_{\phi }(\cdot |x)\|p_{\theta }(\cdot |x))$

### Maximizing the ELBO

For fixed x , the optimization $\max _{\theta ,\phi }L(\phi ,\theta ;x)$ simultaneously attempts to maximize $\ln p_{\theta }(x)$ and minimize $D_{\mathit {KL}}(q_{\phi }(\cdot |x)\|p_{\theta }(\cdot |x))$ . If the parametrization for $p_{\theta }$ and $q_{\phi }$ are flexible enough, we would obtain some ${\hat {\phi }},{\hat {\theta }}$ , such that we have simultaneously

$\ln p_{\hat {\theta }}(x)\approx \max _{\theta }\ln p_{\theta }(x);\quad q_{\hat {\phi }}(\cdot |x)\approx p_{\hat {\theta }}(\cdot |x)$ Since $\mathbb {E} _{x\sim p^{*}(x)}[\ln p_{\theta }(x)]=-H(p^{*})-D_{\mathit {KL}}(p^{*}(x)\|p_{\theta }(x))$ we have $\ln p_{\hat {\theta }}(x)\approx \max _{\theta }-H(p^{*})-D_{\mathit {KL}}(p^{*}(x)\|p_{\theta }(x))$ and so ${\hat {\theta }}\approx \arg \min D_{\mathit {KL}}(p^{*}(x)\|p_{\theta }(x))$ In other words, maximizing the ELBO would simultaneously allow us to obtain an accurate generative model $p_{\hat {\theta }}\approx p^{*}$ and an accurate discriminative model $q_{\hat {\phi }}(\cdot |x)\approx p_{\hat {\theta }}(\cdot |x)$ .

## Main forms

The ELBO has many possible expressions, each with some different emphasis.

$\mathbb {E} _{z\sim q_{\phi }(\cdot |x)}\left[\ln {\frac {p_{\theta }(x,z)}{q_{\phi }(z|x)}}\right]=\int q_{\phi }(z|x)\ln {\frac {p_{\theta }(x,z)}{q_{\phi }(z|x)}}dz$

The above form shows that if we sample $z\sim q_{\phi }(\cdot |x)$ , then $\ln {\frac {p_{\theta }(x,z)}{q_{\phi }(z|x)}}$ is an unbiased estimator of the ELBO.

$\ln \ p_{\theta }(x)-D_{\mathit {KL}}(q_{\phi }(\cdot |x)\;\|\;p_{\theta }(\cdot |x))$

The above form shows that the ELBO is a lower bound on the evidence $\ln \ p_{\theta }(x)$ , and that maximizing the ELBO with respect to $\phi$ is equivalent to minimizing the KL-divergence from $p_{\theta }(\cdot |x)$ to $q_{\phi }(\cdot |x)$ .

$\mathbb {E} _{z\sim q_{\phi }(\cdot |x)}[\ln \ p_{\theta }(x|z)]-D_{\mathit {KL}}(q_{\phi }(\cdot |x)\;\|\;p(\cdot ))$

where again, $\cdot$ ranges over values of z . The above form shows that maximizing the ELBO attempts to concentrate $q_{\phi }(\cdot |x)$ on those z that achieve high $\ln \ p_{\theta }(x|z)$ (in other words, high-likelihood explanations of the observed x ) but also to keep $q_{\phi }(\cdot |x)$ close to the prior $p(\cdot )$ . In practice, this form provides a lower-variance unbiased estimator of the ELBO in the special case when the approximate posterior and the prior are both parameterized as Gaussians, since then the KL term (though it is itself an expectation) has a closed-form expression, so only the first expectation term needs to be estimated by sampling z .

### Data-processing inequality

Suppose we take N independent samples from $p^{*}$ , and collect them in the dataset $D=\{x_{1},...,x_{N}\}$ , then we have empirical distribution $q_{D}(x)={\frac {1}{N}}\sum _{i}\delta _{x_{i}}$ .

Fitting $p_{\theta }(x)$ to $q_{D}(x)$ can be done, as usual, by maximizing the loglikelihood $\ln \ p_{\theta }(D)$ : $D_{\mathit {KL}}(q_{D}(x)\|p_{\theta }(x))=-{\frac {1}{N}}\sum _{i}\ln \ p_{\theta }(x_{i})-H(q_{D})=-{\frac {1}{N}}\ln \ p_{\theta }(D)-H(q_{D})$ Now, by the ELBO inequality, we can bound $\ln \ p_{\theta }(D)$ , and thus $D_{\mathit {KL}}(q_{D}(x)\|p_{\theta }(x))\leq -{\frac {1}{N}}L(\phi ,\theta ;D)-H(q_{D})$ The right-hand-side simplifies to a KL-divergence, and so we get: $D_{\mathit {KL}}(q_{D}(x)\|p_{\theta }(x))\leq -{\frac {1}{N}}\sum _{i}L(\phi ,\theta ;x_{i})-H(q_{D})=D_{\mathit {KL}}(q_{D,\phi }(x,z);p_{\theta }(x,z))$ This result can be interpreted as a special case of the data processing inequality.

In this interpretation, maximizing $L(\phi ,\theta ;D)=\sum _{i}L(\phi ,\theta ;x_{i})$ is minimizing $D_{\mathit {KL}}(q_{D,\phi }(x,z);p_{\theta }(x,z))$ , which upper-bounds the real quantity of interest $D_{\mathit {KL}}(q_{D}(x);p_{\theta }(x))$ via the data-processing inequality. That is, we append a latent space to the observable space, paying the price of a weaker inequality for the sake of more computationally efficient minimization of the KL-divergence.
