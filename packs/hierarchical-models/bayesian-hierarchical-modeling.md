---
title: "Bayesian hierarchical modeling"
source: https://en.wikipedia.org/wiki/Bayesian_hierarchical_modeling
domain: hierarchical-models
license: CC-BY-SA-4.0
tags: multilevel model, hierarchical modeling, shrinkage estimator, hyperparameter prior
fetched: 2026-07-02
---

# Bayesian hierarchical modeling

**Bayesian hierarchical modelling** is a statistical model written in multiple levels (hierarchical form) that estimates the posterior distribution of model parameters using the Bayesian method. The sub-models combine to form the hierarchical model, and Bayes' theorem is used to integrate them with the observed data and account for all the uncertainty that is present. This integration enables calculation of updated posterior over the (hyper)parameters, effectively updating prior beliefs in light of the observed data.

Frequentist statistics may yield conclusions seemingly incompatible with those offered by Bayesian statistics due to the Bayesian treatment of the parameters as random variables and its use of subjective information in establishing assumptions on these parameters. As the approaches answer different questions the formal results are not technically contradictory but the two approaches disagree over which answer is relevant to particular applications. Bayesians argue that relevant information regarding decision-making and updating beliefs cannot be ignored and that hierarchical modeling has the potential to overrule classical methods in applications where respondents give multiple observational data. Moreover, the model has proven to be robust, with the posterior distribution less sensitive to the more flexible hierarchical priors.

Hierarchical modeling, as its name implies, retains nested data structure, and is used when information is available at several different levels of observational units. For example, in epidemiological modeling to describe infection trajectories for multiple countries, observational units are countries, and each country has its own time-based profile of daily infected cases. In decline curve analysis to describe oil or gas production decline curve for multiple wells, observational units are oil or gas wells in a reservoir region, and each well has each own time-based profile of oil or gas production rates (usually, barrels per month). Hierarchical modeling is used to devise computation based strategies for multiparameter problems.

## Philosophy

Statistical methods and models commonly involve multiple parameters that can be regarded as related or connected in such a way that the problem implies a dependence of the joint probability model for these parameters. Individual degrees of belief, expressed in the form of probabilities, come with uncertainty. Amidst this is the change of the degrees of belief over time. As was stated by Professor José M. Bernardo and Professor Adrian F. Smith, "The actuality of the learning process consists in the evolution of individual and subjective beliefs about the reality." These subjective probabilities are more directly involved in the mind rather than the physical probabilities. Hence, it is with this need of updating beliefs that Bayesians have formulated an alternative statistical model which takes into account the prior occurrence of a particular event.

## Bayes' theorem

The assumed occurrence of a real-world event will typically modify preferences between certain options. This is done by modifying the degrees of belief attached, by an individual, to the events defining the options.

Suppose in a study of the effectiveness of cardiac treatments, with the patients in hospital *j* having survival probability $\theta _{j}$ , the survival probability will be updated with the occurrence of *y*, the event in which a controversial serum is created which, as believed by some, increases survival in cardiac patients.

In order to make updated probability statements about $\theta _{j}$ , given the occurrence of event *y*, we must begin with a model providing a joint probability distribution for $\theta _{j}$ and *y*. This can be written as a product of the two distributions that are often referred to as the prior distribution $P(\theta )$ and the sampling distribution $P(y\mid \theta )$ respectively:

$P(\theta ,y)=P(\theta )P(y\mid \theta )$

Using the basic property of conditional probability, the posterior distribution will yield:

$P(\theta \mid y)={\frac {P(\theta ,y)}{P(y)}}={\frac {P(y\mid \theta )P(\theta )}{P(y)}}$

This equation, showing the relationship between the conditional probability and the individual events, is known as Bayes' theorem. This simple expression encapsulates the technical core of Bayesian inference which aims to deconstruct the probability, $P(\theta \mid y)$ , relative to solvable subsets of its supportive evidence.

## Exchangeability

The usual starting point of a statistical analysis is the assumption that the *n* values $y_{1},y_{2},\ldots ,y_{n}$ are exchangeable. If no information – other than data *y* – is available to distinguish any of the $\theta _{j}$ 's from any others, and no ordering or grouping of the parameters can be made, one must assume symmetry of prior distribution parameters. This symmetry is represented probabilistically by exchangeability. Generally, it is useful and appropriate to model data from an exchangeable distribution as independently and identically distributed, given some unknown parameter vector $\theta$ , with distribution $P(\theta )$ .

### Finite exchangeability

For a fixed number *n*, the set $y_{1},y_{2},\ldots ,y_{n}$ is exchangeable if the joint probability $P(y_{1},y_{2},\ldots ,y_{n})$ is invariant under permutations of the indices. That is, for every permutation $\pi$ or $(\pi _{1},\pi _{2},\ldots ,\pi _{n})$ of (1, 2, …, *n*), $P(y_{1},y_{2},\ldots ,y_{n})=P(y_{\pi _{1}},y_{\pi _{2}},\ldots ,y_{\pi _{n}}).$

The following is an exchangeable, but not independent and identical (iid), example: Consider an urn with a red ball and a blue ball inside, with probability ${\frac {1}{2}}$ of drawing either. Balls are drawn without replacement, i.e. after one ball is drawn from the n balls, there will be $n-1$ remaining balls left for the next draw.

${\text{Let }}Y_{i}={\begin{cases}1,&{\text{if the }}i{\text{th ball is red}},\\0,&{\text{otherwise}}.\end{cases}}$

The probability of selecting a red ball in the first draw and a blue ball in the second draw is equal to the probability of selecting a blue ball on the first draw and a red on the second, both of which are 1/2:

$P(y_{1}=1,y_{2}=0)=P(y_{1}=0,y_{2}=1)={\frac {1}{2}}$

.

This makes $y_{1}$ and $y_{2}$ exchangeable.

But the probability of selecting a red ball on the second draw given that the red ball has already been selected in the first is 0. This is not equal to the probability that the red ball is selected in the second draw, which is 1/2:

$P(y_{2}=1\mid y_{1}=1)=0\neq P(y_{2}=1)={\frac {1}{2}}$

.

Thus, $y_{1}$ and $y_{2}$ are not independent.

If $x_{1},\ldots ,x_{n}$ are independent and identically distributed, then they are exchangeable, but the converse is not necessarily true.

### Infinite exchangeability

Infinite exchangeability is the property that every finite subset of an infinite sequence $y_{1}$ , $y_{2},\ldots$ is exchangeable. For any *n*, the sequence $y_{1},y_{2},\ldots ,y_{n}$ is exchangeable.

## Hierarchical models

### Components

Bayesian hierarchical modeling makes use of two important concepts in deriving the posterior distribution, namely:

1. Hyperparameters: parameters of the prior distribution
2. Hyperpriors: distributions of Hyperparameters

Suppose a random variable *Y* follows a normal distribution with parameter $\theta$ as the mean and 1 as the variance, that is $Y\mid \theta \sim N(\theta ,1)$ . The tilde relation $\sim$ can be read as "has the distribution of" or "is distributed as". Suppose also that the parameter $\theta$ has a distribution given by a normal distribution with mean $\mu$ and variance 1, i.e. $\theta \mid \mu \sim N(\mu ,1)$ . Furthermore, $\mu$ follows another distribution given, for example, by the standard normal distribution, ${\text{N}}(0,1)$ . The parameter $\mu$ is called the hyperparameter, while its distribution given by ${\text{N}}(0,1)$ is an example of a hyperprior distribution. The notation of the distribution of *Y* changes as another parameter is added, i.e. $Y\mid \theta ,\mu \sim N(\theta ,1)$ . If there is another stage, say, $\mu$ following another normal distribution with a mean of $\beta$ and a variance of $\epsilon$ , then $\mu \sim N(\beta ,\epsilon )$ , ${\mbox{ }}$ $\beta$ and $\epsilon$ can also be called hyperparameters with hyperprior distributions.

### Framework

Let $y_{j}$ be an observation and $\theta _{j}$ a parameter governing the data generating process for $y_{j}$ . Assume further that the parameters $\theta _{1},\theta _{2},\ldots ,\theta _{j}$ are generated exchangeably from a common population, with distribution governed by a hyperparameter $\phi$ . The Bayesian hierarchical model contains the following stages:

${\text{Stage I: }}y_{j}\mid \theta _{j},\phi \sim P(y_{j}\mid \theta _{j},\phi )$

${\text{Stage II: }}\theta _{j}\mid \phi \sim P(\theta _{j}\mid \phi )$

${\text{Stage III: }}\phi \sim P(\phi )$

The likelihood, as seen in stage I is $P(y_{j}\mid \theta _{j},\phi )$ , with $P(\theta _{j},\phi )$ as its prior distribution. Note that the likelihood depends on $\phi$ only through $\theta _{j}$ .

The prior distribution from stage I can be broken down into:

$P(\theta _{j},\phi )=P(\theta _{j}\mid \phi )P(\phi )$

[from the definition of conditional probability]

With $\phi$ as its hyperparameter with hyperprior distribution, $P(\phi )$ .

Thus, the posterior distribution is proportional to:

$P(\phi ,\theta _{j}\mid y)\propto P(y_{j}\mid \theta _{j},\phi )P(\theta _{j},\phi )$

[using Bayes' Theorem]

$P(\phi ,\theta _{j}\mid y)\propto P(y_{j}\mid \theta _{j})P(\theta _{j}\mid \phi )P(\phi )$

### Example calculation

As an example, a teacher wants to estimate how well a student did on the SAT. The teacher uses the current grade point average (GPA) of the student for an estimate. Their current GPA, denoted by Y , has a likelihood given by some probability function with parameter $\theta$ , i.e. $Y\mid \theta \sim P(Y\mid \theta )$ . This parameter $\theta$ is the SAT score of the student. The SAT score is viewed as a sample coming from a common population distribution indexed by another parameter $\phi$ , which is the high school grade of the student (freshman, sophomore, junior or senior). That is, $\theta \mid \phi \sim P(\theta \mid \phi )$ . Moreover, the hyperparameter $\phi$ follows its own distribution given by $P(\phi )$ , a hyperprior.

These relationships can be used to calculate the likelihood of a specific SAT score relative to a particular GPA:

$P(\theta ,\phi \mid Y)\propto P(Y\mid \theta ,\phi )P(\theta ,\phi )$

$P(\theta ,\phi \mid Y)\propto P(Y\mid \theta )P(\theta \mid \phi )P(\phi )$

All information in the problem will be used to solve for the posterior distribution. Instead of solving only using the prior distribution and the likelihood function, using hyperpriors allows a more nuanced distinction of relationships between given variables.

### 2-stage hierarchical model

In general, the joint posterior distribution of interest in 2-stage hierarchical models is:

$P(\theta ,\phi \mid Y)={P(Y\mid \theta ,\phi )P(\theta ,\phi ) \over P(Y)}={P(Y\mid \theta )P(\theta \mid \phi )P(\phi ) \over P(Y)}$

$P(\theta ,\phi \mid Y)\propto P(Y\mid \theta )P(\theta \mid \phi )P(\phi )$

### 3-stage hierarchical model

For 3-stage hierarchical models, the posterior distribution is given by:

$P(\theta ,\phi ,X\mid Y)={P(Y\mid \theta )P(\theta \mid \phi )P(\phi \mid X)P(X) \over P(Y)}$

$P(\theta ,\phi ,X\mid Y)\propto P(Y\mid \theta )P(\theta \mid \phi )P(\phi \mid X)P(X)$

## Bayesian nonlinear mixed-effects model

A three stage version of Bayesian hierarchical modeling could be used to calculate probability at 1) an individual level, 2) at the level of population and 3) the prior, which is an assumed probability distribution that takes place before evidence is initially acquired:

### Stage 1: Individual-Level Model

${y}_{ij}=f(t_{ij};\theta _{1i},\theta _{2i},\ldots ,\theta _{li},\ldots ,\theta _{Ki})+\epsilon _{ij},\quad \epsilon _{ij}\sim N(0,\sigma ^{2}),\quad i=1,\ldots ,N,\,j=1,\ldots ,M_{i}.$

### Stage 2: Population Model

$\theta _{li}=\alpha _{l}+\sum _{b=1}^{P}\beta _{lb}x_{ib}+\eta _{li},\quad \eta _{li}\sim N(0,\omega _{l}^{2}),\quad i=1,\ldots ,N,\,l=1,\ldots ,K.$

### Stage 3: Prior

$\sigma ^{2}\sim \pi (\sigma ^{2}),\quad \alpha _{l}\sim \pi (\alpha _{l}),\quad (\beta _{l1},\ldots ,\beta _{lb},\ldots ,\beta _{lP})\sim \pi (\beta _{l1},\ldots ,\beta _{lb},\ldots ,\beta _{lP}),\quad \omega _{l}^{2}\sim \pi (\omega _{l}^{2}),\quad l=1,\ldots ,K.$

Here, $y_{ij}$ denotes the continuous response of the i -th subject at the time point $t_{ij}$ , and $x_{ib}$ is the b -th covariate of the i -th subject. Parameters involved in the model are written in Greek letters. The variable $f(t;\theta _{1},\ldots ,\theta _{K})$ is a known function parameterized by the K -dimensional vector $(\theta _{1},\ldots ,\theta _{K})$ .

Typically, f is a `nonlinear' function and describes the temporal trajectory of individuals. In the model, $\epsilon _{ij}$ and $\eta _{li}$ describe within-individual variability and between-individual variability, respectively. If the prior is not considered, the relationship reduces to a frequentist nonlinear mixed-effect model.

A central task in the application of the Bayesian nonlinear mixed-effect models is to evaluate posterior density:

$\pi (\{\theta _{li}\}_{i=1,l=1}^{N,K},\sigma ^{2},\{\alpha _{l}\}_{l=1}^{K},\{\beta _{lb}\}_{l=1,b=1}^{K,P},\{\omega _{l}\}_{l=1}^{K}|\{y_{ij}\}_{i=1,j=1}^{N,M_{i}})$

$\propto \pi (\{y_{ij}\}_{i=1,j=1}^{N,M_{i}},\{\theta _{li}\}_{i=1,l=1}^{N,K},\sigma ^{2},\{\alpha _{l}\}_{l=1}^{K},\{\beta _{lb}\}_{l=1,b=1}^{K,P},\{\omega _{l}\}_{l=1}^{K})$

$=\underbrace {\pi (\{y_{ij}\}_{i=1,j=1}^{N,M_{i}}|\{\theta _{li}\}_{i=1,l=1}^{N,K},\sigma ^{2})} _{\text{Stage 1: Individual-Level Model}}\times \underbrace {\pi (\{\theta _{li}\}_{i=1,l=1}^{N,K}|\{\alpha _{l}\}_{l=1}^{K},\{\beta _{lb}\}_{l=1,b=1}^{K,P},\{\omega _{l}\}_{l=1}^{K})} _{\text{Stage 2: Population Model}}\times \underbrace {p(\sigma ^{2},\{\alpha _{l}\}_{l=1}^{K},\{\beta _{lb}\}_{l=1,b=1}^{K,P},\{\omega _{l}\}_{l=1}^{K})} _{\text{Stage 3: Prior}}$

The panel on the right displays Bayesian research cycle using Bayesian nonlinear mixed-effects model. A research cycle using the Bayesian nonlinear mixed-effects model comprises two steps: (a) standard research cycle and (b) Bayesian-specific workflow.

A standard research cycle involves 1) literature review, 2) defining a problem and 3) specifying the research question and hypothesis. Bayesian-specific workflow stratifies this approach to include three sub-steps: (b)–(i) formalizing prior distributions based on background knowledge and prior elicitation; (b)–(ii) determining the likelihood function based on a nonlinear function f ; and (b)–(iii) making a posterior inference. The resulting posterior inference can be used to start a new research cycle.

## Applications

Hierarchical Bayesian frameworks have been applied for modeling, e.g., Reinforcement learning and decision-making tasks, antigen mutation effects on the immune system, and ecological processes affecting species distribution, to mention a few. PyMC is a flexible open source Python package supporting such modeling.
