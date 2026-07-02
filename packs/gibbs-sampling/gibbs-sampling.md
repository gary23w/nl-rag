---
title: "Gibbs sampling"
source: https://en.wikipedia.org/wiki/Gibbs_sampling
domain: gibbs-sampling
license: CC-BY-SA-4.0
tags: Gibbs sampling, conjugate prior, slice sampling, conditional probability distribution
fetched: 2026-07-02
---

# Gibbs sampling

In statistics, **Gibbs sampling** or a **Gibbs sampler** is a Markov chain Monte Carlo (MCMC) algorithm for sampling from a specified multivariate probability distribution when direct sampling from the joint distribution is difficult, but sampling from the conditional distribution is more practical. This sequence can be used to approximate the joint distribution (e.g., to generate a histogram of the distribution); to approximate the marginal distribution of one of the variables, or some subset of the variables (for example, the unknown parameters or latent variables); or to compute an integral (such as the expected value of one of the variables). Typically, some of the variables correspond to observations whose values are known, and hence do not need to be sampled.

Gibbs sampling is commonly used as a means of statistical inference, especially Bayesian inference. It is a randomized algorithm (i.e. an algorithm that makes use of random numbers), and is an alternative to deterministic algorithms for statistical inference such as the expectation–maximization algorithm (EM).

As with other MCMC algorithms, Gibbs sampling generates a Markov chain of samples, each of which is correlated with nearby samples. As a result, care must be taken if independent samples are desired. Samples from the beginning of the chain (the *burn-in period*) may not accurately represent the desired distribution and are usually discarded.

## Introduction

Gibbs sampling is named after the physicist Josiah Willard Gibbs, in reference to an analogy between the sampling algorithm and statistical physics. The algorithm was described by brothers Stuart and Donald Geman in 1984, some eight decades after the death of Gibbs, and became popularized in the statistics community for calculating marginal probability distribution, especially the posterior distribution.

In its basic version, Gibbs sampling is a special case of the Metropolis–Hastings algorithm. However, in its extended versions (see below), it can be considered a general framework for sampling from a large set of variables by sampling each variable (or in some cases, each group of variables) in turn, and can incorporate the Metropolis–Hastings algorithm (or methods such as slice sampling) to implement one or more of the sampling steps.

Gibbs sampling is applicable when the joint distribution is not known explicitly or is difficult to sample from directly, but the conditional distribution of each variable is known and is easy (or at least, easier) to sample from. The Gibbs sampling algorithm generates an instance from the distribution of each variable in turn, conditional on the current values of the other variables. It can be shown that the sequence of samples constitutes a Markov chain, and the stationary distribution of that Markov chain is just the sought-after joint distribution.

Gibbs sampling is particularly well-adapted to sampling the posterior distribution of a Bayesian network, since Bayesian networks are typically specified as a collection of conditional distributions.

## Implementation

Gibbs sampling, in its basic incarnation, is a special case of the Metropolis–Hastings algorithm. The point of Gibbs sampling is that given a multivariate distribution it is simpler to sample from a conditional distribution than to marginalize by integrating over a joint distribution. Suppose we want to obtain k samples of a n -dimensional random vector $\mathbf {X} =(X_{1},\dots ,X_{n})$ . We proceed iteratively:

- Begin with some initial value $\mathbf {X} ^{(0)}$ .
- Given a sample $\mathbf {X} ^{(i)}=\left(x_{1}^{(i)},\dots ,x_{n}^{(i)}\right)$ , to obtain the next sample $\mathbf {X} ^{(i+1)}=\left(x_{1}^{(i+1)},x_{2}^{(i+1)},\dots ,x_{n}^{(i+1)}\right)$ , we can sample each component $x_{j}^{(i+1)}$ from the distribution of $X_{j}$ , conditioned on all the components sampled so far: we condition on $X_{\ell }^{(i+1)}$ for all $\ell \leq j-1$ , and on $X_{\ell }^{(i)}$ for $j+1\leq \ell \leq n$ . In other words, we sample $x_{j}^{(i+1)}$ according to the distribution $P\left(X_{j}=\cdot |X_{1}=x_{1}^{(i+1)},\dots ,X_{j-1}=x_{j-1}^{(i+1)},X_{j+1}=x_{j+1}^{(i)},\dots ,X_{n}=x_{n}^{(i)}\right)$ .

## Properties

If such sampling is performed, these important facts hold:

- The samples approximate the joint distribution of all variables.
- The marginal distribution of any subset of variables can be approximated by simply considering the samples for that subset of variables, ignoring the rest.
- The expected value of any variable can be approximated by averaging over all the samples.

When performing the sampling:

- The initial values of the variables can be determined randomly or by some other algorithm such as expectation–maximization.
- It is not actually necessary to determine an initial value for the first variable sampled.
- It is common to ignore some number of samples at the beginning (the so-called *burn-in period*), and then consider only every n th sample when averaging values to compute an expectation. For example, the first 1,000 samples might be ignored, and then every 100th sample averaged, throwing away all the rest. The reason for this is that (1) the stationary distribution of the Markov chain is the desired joint distribution over the variables, but it may take a while for that stationary distribution to be reached; (2) successive samples are not independent of each other but form a Markov chain with some amount of correlation. Sometimes, algorithms can be used to determine the amount of autocorrelation between samples and the value of n (the period between samples that are actually used) computed from this, but in practice there is a fair amount of "black magic" involved.
- The process of simulated annealing is often used to reduce the "random walk" behavior in the early part of the sampling process (i.e. the tendency to move slowly around the sample space, with a high amount of autocorrelation between samples, rather than moving around quickly, as is desired). Other techniques that may reduce autocorrelation are *collapsed Gibbs sampling*, *blocked Gibbs sampling*, and *ordered overrelaxation*; see below.

### Relation of conditional distribution and joint distribution

Furthermore, the conditional distribution of one variable given all others is proportional to the joint distribution, i.e., for all possible value $(x_{i})_{1\leq i\leq n}$ of $\mathbf {X}$ :

$P(X_{j}=x_{j}\mid (X_{i}=x_{i})_{i\neq j})={\frac {P((X_{i}=x_{i})_{i})}{P((X_{i}=x_{i})_{i\neq j})}}\propto P((X_{i}=x_{i})_{i})$

"Proportional to" in this case means that the denominator is not a function of $x_{j}$ and thus is the same for all values of $x_{j}$ ; it forms part of the normalization constant for the distribution over $x_{j}$ . In practice, to determine the nature of the conditional distribution of a factor $x_{j}$ , it is easiest to factor the joint distribution according to the individual conditional distributions defined by the graphical model over the variables, ignore all factors that are not functions of $x_{j}$ (all of which, together with the denominator above, constitute the normalization constant), and then reinstate the normalization constant at the end, as necessary. In practice, this means doing one of three things:

1. If the distribution is discrete, the individual probabilities of all possible values of $x_{j}$ are computed, and then summed to find the normalization constant.
2. If the distribution is continuous and of a known form, the normalization constant will also be known.
3. In other cases, the normalization constant can usually be ignored, as most sampling methods do not require it.

## Inference

Gibbs sampling is commonly used for statistical inference (e.g. determining the best value of a parameter, such as determining the number of people likely to shop at a particular store on a given day, the candidate a voter will most likely vote for, etc.). The idea is that observed data is incorporated into the sampling process by creating separate variables for each piece of observed data and fixing the variables in question to their observed values, rather than sampling from those variables. The distribution of the remaining variables is then effectively a posterior distribution conditioned on the observed data.

The most likely value of a desired parameter (the mode) could then simply be selected by choosing the sample value that occurs most commonly; this is essentially equivalent to maximum a posteriori estimation of a parameter. (Since the parameters are usually continuous, it is often necessary to "bin" the sampled values into one of a finite number of ranges or "bins" in order to get a meaningful estimate of the mode.) More commonly, however, the expected value (mean or average) of the sampled values is chosen; this is a Bayes estimator that takes advantage of the additional data about the entire distribution that is available from Bayesian sampling, whereas a maximization algorithm such as expectation maximization (EM) is capable of only returning a single point from the distribution. For example, for a unimodal distribution the mean (expected value) is usually similar to the mode (most common value), but if the distribution is skewed in one direction, the mean will be moved in that direction, which effectively accounts for the extra probability mass in that direction. (If a distribution is multimodal, the expected value may not return a meaningful point, and any of the modes is typically a better choice.)

Although some of the variables typically correspond to parameters of interest, others are uninteresting ("nuisance") variables introduced into the model to properly express the relationships among variables. Although the sampled values represent the joint distribution over all variables, the nuisance variables can simply be ignored when computing expected values or modes; this is equivalent to marginalizing over the nuisance variables. When a value for multiple variables is desired, the expected value is simply computed over each variable separately. (When computing the mode, however, all variables must be considered together.)

Supervised learning, unsupervised learning and semi-supervised learning (aka learning with missing values) can all be handled by simply fixing the values of all variables whose values are known, and sampling from the remainder.

For observed data, there will be one variable for each observation—rather than, for example, one variable corresponding to the sample mean or sample variance of a set of observations. In fact, there generally will be no variables at all corresponding to concepts such as "sample mean" or "sample variance". Instead, in such a case there will be variables representing the unknown true mean and true variance, and the determination of sample values for these variables results automatically from the operation of the Gibbs sampler.

Generalized linear models (i.e. variations of linear regression) can sometimes be handled by Gibbs sampling as well. For example, probit regression for determining the probability of a given binary (yes/no) choice, with normally distributed priors placed over the regression coefficients, can be implemented with Gibbs sampling because it is possible to add additional variables and take advantage of conjugacy. However, logistic regression cannot be handled this way. One possibility is to approximate the logistic function with a mixture (typically 7–9) of normal distributions. More commonly, however, Metropolis–Hastings is used instead of Gibbs sampling.

## Mathematical background

Suppose that a sample $\left.X\right.$ is taken from a distribution depending on a parameter vector $\theta \in \Theta \,\!$ of length $\left.d\right.$ , with prior distribution $g(\theta _{1},\ldots ,\theta _{d})$ . It may be that $\left.d\right.$ is very large and that numerical integration to find the marginal densities of the $\left.\theta _{i}\right.$ would be computationally expensive. Then an alternative method of calculating the marginal densities is to create a Markov chain on the space $\left.\Theta \right.$ by repeating these two steps:

1. Pick a random index $1\leq j\leq d$
2. Pick a new value for $\left.\theta _{j}\right.$ according to $g(\theta _{1},\ldots ,\theta _{j-1},\,\cdot \,,\theta _{j+1},\ldots ,\theta _{d})$

These steps define a reversible Markov chain with the desired invariant distribution $\left.g\right.$ . This can be proved as follows. Define $x\sim _{j}y$ if $\left.x_{i}=y_{i}\right.$ for all $i\neq j$ and let $\left.p_{xy}\right.$ denote the probability of a jump from $x\in \Theta$ to $y\in \Theta$ . Then, the transition probabilities are

$p_{xy}={\begin{cases}{\frac {1}{d}}{\frac {g(y)}{\sum _{z\in \Theta :z\sim _{j}x}g(z)}}&x\sim _{j}y\\0&{\text{otherwise}}\end{cases}}$

So

$g(x)p_{xy}={\frac {1}{d}}{\frac {g(x)g(y)}{\sum _{z\in \Theta :z\sim _{j}x}g(z)}}={\frac {1}{d}}{\frac {g(y)g(x)}{\sum _{z\in \Theta :z\sim _{j}y}g(z)}}=g(y)p_{yx}$

since $x\sim _{j}y$ is an equivalence relation. Thus the detailed balance equations are satisfied, implying the chain is reversible and it has invariant distribution $\left.g\right.$ .

In practice, the index $\left.j\right.$ is not chosen at random, and the chain cycles through the indexes in order. In general this gives a non-stationary Markov process, but each individual step will still be reversible, and the overall process will still have the desired stationary distribution (as long as the chain can access all states under the fixed ordering).

## Gibbs sampler in Bayesian inference and its relation to information theory

Let y denote observations generated from the sampling distribution $f(y|\theta )$ and $\pi (\theta )$ be a prior supported on the parameter space $\Theta$ . Then one of the central goals of the Bayesian statistics is to approximate the posterior density

$\pi (\theta |y)={\frac {f(y|\theta )\cdot \pi (\theta )}{m(y)}}$

where the marginal likelihood $m(y)=\int _{\Theta }f(y|\theta )\cdot \pi (\theta )d\theta$ is assumed to be finite for all y .

To explain the Gibbs sampler, we additionally assume that the parameter space $\Theta$ is decomposed as

$\Theta =\prod _{i=1}^{K}\Theta _{i}=\Theta _{1}\times \cdots \Theta _{i}\times \cdots \times \Theta _{K},\quad \quad (K>1)$

,

where $\times$ represents the Cartesian product. Each component parameter space $\Theta _{i}$ can be a set of scalar components, subvectors, or matrices.

Define a set $\Theta _{-i}$ that complements the $\Theta _{i}$ . Essential ingredients of the Gibbs sampler is the i -th full conditional posterior distribution for each $i=1,\cdots ,K$

$\pi (\theta _{i}|\theta _{-i},y)=\pi (\theta _{i}|\theta _{1},\cdots ,\theta _{i-1},\theta _{i+1},\cdots ,\theta _{K},y)$

.

The following algorithm details a generic Gibbs sampler:

${\text{Initialize: pick arbitrary starting value}}\,\,\theta ^{(1)}=(\theta _{1}^{(1)},\theta _{2}^{(1)},\cdots ,\theta _{i}^{(1)},\theta _{i+1}^{(1)},\cdots ,\theta _{K}^{(1)})$

${\text{Iterate a Cycle:}}\,$

$\quad \quad {\text{Step 1. draw}}\,\,\theta _{1}^{(s+1)}\sim \pi (\theta _{1}|\theta _{2}^{(s)},\theta _{3}^{(s)},\cdots ,\theta _{K}^{(s)},y)$

$\quad \quad {\text{Step 2. draw}}\,\,\theta _{2}^{(s+1)}\sim \pi (\theta _{2}|\theta _{1}^{(s+1)},\theta _{3}^{(s)},\cdots ,\theta _{K}^{(s)},y)$

$\quad \quad \quad \vdots$

$\quad \quad {\text{Step i. draw}}\,\,\theta _{i}^{(s+1)}\sim \pi (\theta _{i}|\theta _{1}^{(s+1)},\theta _{2}^{(s+1)},\cdots ,\theta _{i-1}^{(s+1)},\theta _{i+1}^{(s)},\cdots ,\theta _{K}^{(s)},y)$

$\quad \quad {\text{Step i+1. draw}}\,\,\theta _{i+1}^{(s+1)}\sim \pi (\theta _{i+1}|\theta _{1}^{(s+1)},\theta _{2}^{(s+1)},\cdots ,\theta _{i}^{(s+1)},\theta _{i+2}^{(s)},\cdots ,\theta _{K}^{(s)},y)$

$\quad \quad \quad \vdots$

$\quad \quad {\text{Step K. draw}}\,\,\theta _{K}^{(s+1)}\sim \pi (\theta _{K}|\theta _{1}^{(s+1)},\theta _{2}^{(s+1)},\cdots ,\theta _{K-1}^{(s+1)},y)$

${\text{end Iterate}}$

Note that Gibbs sampler is operated by the iterative Monte Carlo scheme within a cycle. The S number of samples $\{\theta ^{(s)}\}_{s=1}^{S}$ drawn by the above algorithm formulates Markov Chains with the invariant distribution to be the target density $\pi (\theta |y)$ .

Now, for each $i=1,\cdots ,K$ , define the following information theoretic quantities:

$I(\theta _{i};\theta _{-i})={\text{KL}}(\pi (\theta |y)||\pi (\theta _{i}|y)\cdot \pi (\theta _{-i}|y))=\int _{\Theta }\pi (\theta |y)\log {\bigg (}{\frac {\pi (\theta |y)}{\pi (\theta _{i}|y)\cdot \pi (\theta _{-i}|y)}}{\bigg )}d\theta ,$

$H(\theta _{-i})=-\int _{\Theta _{-i}}\pi (\theta _{-i}|y)\log \pi (\theta _{-i}|y)d\theta _{-i},$

$H(\theta _{-i}|\theta _{i})=-\int _{\Theta }\pi (\theta |y)\log \pi (\theta _{-i}|\theta _{i},y)d\theta ,$

namely, posterior mutual information, posterior differential entropy, and posterior conditional differential entropy, respectively. We can similarly define information theoretic quantities $I(\theta _{-i};\theta _{i})$ , $H(\theta _{i})$ , and $H(\theta _{i}|\theta _{-i})$ by interchanging the i and $-i$ in the defined quantities. Then, the following K equations hold.

$I(\theta _{i};\theta _{-i})=H(\theta _{-i})-H(\theta _{-i}|\theta _{i})=H(\theta _{i})-H(\theta _{i}|\theta _{-i})=I(\theta _{-i};\theta _{i}),\quad (i=1,\cdots ,K)$ .

The mutual information $I(\theta _{i};\theta _{-i})$ quantifies the reduction in uncertainty of random quantity $\theta _{i}$ once we know $\theta _{-i}$ , a posteriori. It vanishes if and only if $\theta _{i}$ and $\theta _{-i}$ are marginally independent, a posterior. The mutual information $I(\theta _{i};\theta _{-i})$ can be interpreted as the quantity that is transmitted from the i -th step to the $i+1$ -th step within a single cycle of the Gibbs sampler.

## Variations and extensions

Numerous variations of the basic Gibbs sampler exist. The goal of these variations is to reduce the autocorrelation between samples sufficiently to overcome any added computational costs.

### Blocked Gibbs sampler

- A **blocked Gibbs sampler** groups two or more variables together and samples from their joint distribution conditioned on all other variables, rather than sampling from each one individually. For example, in a hidden Markov model, a blocked Gibbs sampler might sample from all the latent variables making up the Markov chain in one go, using the forward-backward algorithm.

### Collapsed Gibbs sampler

- A **collapsed Gibbs sampler** integrates out (marginalizes over) one or more variables when sampling for some other variable. For example, imagine that a model consists of three variables *A*, *B*, and *C*. A simple Gibbs sampler would sample from *p*(*A* | *B*,*C*), then *p*(*B* | *A*,*C*), then *p*(*C* | *A*,*B*). A collapsed Gibbs sampler might replace the sampling step for *A* with a sample taken from the marginal distribution *p*(*A* | *C*), with variable *B* integrated out in this case. Alternatively, variable *B* could be collapsed out entirely, alternately sampling from *p*(*A* | *C*) and *p*(*C* | *A*) and not sampling over *B* at all. The distribution over a variable *A* that arises when collapsing a parent variable *B* is called a compound distribution; sampling from this distribution is generally tractable when *B* is the conjugate prior for *A*, particularly when *A* and *B* are members of the exponential family. For more information, see the article on compound distributions or Liu (1994).

#### Implementing a collapsed Gibbs sampler

##### Collapsing Dirichlet distributions

In hierarchical Bayesian models with categorical variables, such as latent Dirichlet allocation and various other models used in natural language processing, it is quite common to collapse out the Dirichlet distributions that are typically used as prior distributions over the categorical variables. The result of this collapsing introduces dependencies among all the categorical variables dependent on a given Dirichlet prior, and the joint distribution of these variables after collapsing is a Dirichlet-multinomial distribution. The conditional distribution of a given categorical variable in this distribution, conditioned on the others, assumes an extremely simple form that makes Gibbs sampling even easier than if the collapsing had not been done. The rules are as follows:

1. Collapsing out a Dirichlet prior node affects only the parent and children nodes of the prior. Since the parent is often a constant, it is typically only the children that we need to worry about.
2. Collapsing out a Dirichlet prior introduces dependencies among all the categorical children dependent on that prior — but *no* extra dependencies among any other categorical children. (This is important to keep in mind, for example, when there are multiple Dirichlet priors related by the same hyperprior. Each Dirichlet prior can be independently collapsed and affects only its direct children.)
3. After collapsing, the conditional distribution of one dependent children on the others assumes a very simple form: The probability of seeing a given value is proportional to the sum of the corresponding hyperprior for this value, and the count of all of the *other dependent nodes* assuming the same value. Nodes not dependent on the same prior **must not** be counted. The same rule applies in other iterative inference methods, such as variational Bayes or expectation maximization; however, if the method involves keeping partial counts, then the partial counts for the value in question must be summed across all the other dependent nodes. Sometimes this summed up partial count is termed the *expected count* or similar. The probability is *proportional to* the resulting value; the actual probability must be determined by normalizing across all the possible values that the categorical variable can take (i.e. adding up the computed result for each possible value of the categorical variable, and dividing all the computed results by this sum).
4. If a given categorical node has dependent children (e.g. when it is a latent variable in a mixture model), the value computed in the previous step (expected count plus prior, or whatever is computed) must be multiplied by the actual conditional probabilities (*not* a computed value that is proportional to the probability!) of all children given their parents. See the article on the Dirichlet-multinomial distribution for a detailed discussion.
5. In the case where the group membership of the nodes dependent on a given Dirichlet prior may change dynamically depending on some other variable (e.g. a categorical variable indexed by another latent categorical variable, as in a topic model), the same expected counts are still computed, but need to be done carefully so that the correct set of variables is included. See the article on the Dirichlet-multinomial distribution for more discussion, including in the context of a topic model.

##### Collapsing other conjugate priors

In general, any conjugate prior can be collapsed out, if its only children have distributions conjugate to it. The relevant math is discussed in the article on compound distributions. If there is only one child node, the result will often assume a known distribution. For example, collapsing an inverse-gamma-distributed variance out of a network with a single Gaussian child will yield a Student's t-distribution. (For that matter, collapsing both the mean and variance of a single Gaussian child will still yield a Student's t-distribution, provided both are conjugate, i.e. Gaussian mean, inverse-gamma variance.)

If there are multiple child nodes, they will all become dependent, as in the Dirichlet-categorical case. The resulting joint distribution will have a closed form that resembles in some ways the compound distribution, although it will have a product of a number of factors, one for each child node, in it.

In addition, and most importantly, the resulting conditional distribution of one of the child nodes given the others (and also given the parents of the collapsed node(s), but *not* given the children of the child nodes) will have the same density as the posterior predictive distribution of all the remaining child nodes. Furthermore, the posterior predictive distribution has the same density as the basic compound distribution of a single node, although with different parameters. The general formula is given in the article on compound distributions.

For example, given a Bayes network with a set of conditionally independent identically distributed Gaussian-distributed nodes with conjugate prior distributions placed on the mean and variance, the conditional distribution of one node given the others after compounding out both the mean and variance will be a Student's t-distribution. Similarly, the result of compounding out the gamma prior of a number of Poisson-distributed nodes causes the conditional distribution of one node given the others to assume a negative binomial distribution.

In these cases where compounding produces a well-known distribution, efficient sampling procedures often exist, and using them will often (although not necessarily) be more efficient than not collapsing, and instead sampling both prior and child nodes separately. However, in the case where the compound distribution is not well-known, it may not be easy to sample from, since it generally will not belong to the exponential family and typically will not be log-concave (which would make it easy to sample using adaptive rejection sampling, since a closed form always exists).

In the case where the child nodes of the collapsed nodes themselves have children, the conditional distribution of one of these child nodes given all other nodes in the graph will have to take into account the distribution of these second-level children. In particular, the resulting conditional distribution will be proportional to a product of the compound distribution as defined above, and the conditional distributions of all of the child nodes given their parents (but not given their own children). This follows from the fact that the full conditional distribution is proportional to the joint distribution. If the child nodes of the collapsed nodes are continuous, this distribution will generally not be of a known form, and may well be difficult to sample from despite the fact that a closed form can be written, for the same reasons as described above for non-well-known compound distributions. However, in the particular case that the child nodes are discrete, sampling is feasible, regardless of whether the children of these child nodes are continuous or discrete. In fact, the principle involved here is described in fair detail in the article on the Dirichlet-multinomial distribution.

### Gibbs sampler with ordered overrelaxation

- A Gibbs sampler with **ordered overrelaxation** samples a given odd number of candidate values for $x_{j}^{(i)}$ at any given step and sorts them, along with the single value for $x_{j}^{(i-1)}$ according to some well-defined ordering. If $x_{j}^{(i-1)}$ is the *s*th smallest in the sorted list then the $x_{j}^{(i)}$ is selected as the *s*th largest in the sorted list. For more information, see Neal (1995).

### Other extensions

It is also possible to extend Gibbs sampling in various ways. For example, in the case of variables whose conditional distribution is not easy to sample from, a single iteration of slice sampling or the Metropolis–Hastings algorithm can be used to sample from the variables in question. It is also possible to incorporate variables that are not random variables, but whose value is deterministically computed from other variables. Generalized linear models, e.g. logistic regression (aka "maximum entropy models"), can be incorporated in this fashion. (BUGS, for example, allows this type of mixing of models.)

## Failure modes

There are two ways that Gibbs sampling can fail. The first is when there are islands of high-probability states, with no paths between them. For example, consider a probability distribution over 2-bit vectors, where the vectors (0,0) and (1,1) each have probability ⁠1/2⁠, but the other two vectors (0,1) and (1,0) have probability zero. Gibbs sampling will become trapped in one of the two high-probability vectors, and will never reach the other one. More generally, for any distribution over high-dimensional, real-valued vectors, if two particular elements of the vector are perfectly correlated (or perfectly anti-correlated), those two elements will become stuck, and Gibbs sampling will never be able to change them.

The second problem can happen even when all states have nonzero probability and there is only a single island of high-probability states. For example, consider a probability distribution over 100-bit vectors, where the all-zeros vector occurs with probability ⁠1/2⁠, and all other vectors are equally probable, and so have a probability of ${\frac {1}{2(2^{100}-1)}}$ each. If you want to estimate the probability of the zero vector, it would be sufficient to take 100 or 1000 samples from the true distribution. That would very likely give an answer very close to ⁠1/2⁠. But you would probably have to take more than $2^{100}$ samples from Gibbs sampling to get the same result. No computer could do this in a lifetime.

This problem occurs no matter how long the burn-in period is. This is because in the true distribution, the zero vector occurs half the time, and those occurrences are randomly mixed in with the nonzero vectors. Even a small sample will see both zero and nonzero vectors. But Gibbs sampling will alternate between returning only the zero vector for long periods (about $2^{99}$ in a row), then only nonzero vectors for long periods (about $2^{99}$ in a row). Thus convergence to the true distribution is extremely slow, requiring much more than $2^{99}$ steps; taking this many steps is not computationally feasible in a reasonable time period. The slow convergence here can be seen as a consequence of the curse of dimensionality. A problem like this can be solved by block sampling the entire 100-bit vector at once. (This assumes that the 100-bit vector is part of a larger set of variables. If this vector is the only thing being sampled, then block sampling is equivalent to not doing Gibbs sampling at all, which by hypothesis would be difficult.)

## Software

- The OpenBUGS software (*Bayesian inference Using Gibbs Sampling*) does a Bayesian analysis of complex statistical models using Markov chain Monte Carlo.

- JAGS (*Just another Gibbs sampler*) is a GPL program for analysis of Bayesian hierarchical models using Markov Chain Monte Carlo.

- Church is free software for performing Gibbs inference over arbitrary distributions that are specified as probabilistic programs.

- PyMC is an open source Python library for Bayesian learning of general Probabilistic Graphical Models.
- Turing is an open source Julia library for Bayesian Inference using probabilistic programming.
