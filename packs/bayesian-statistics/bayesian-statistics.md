---
title: "Bayesian statistics"
source: https://en.wikipedia.org/wiki/Bayesian_statistics
domain: bayesian-statistics
license: CC-BY-SA-4.0
tags: bayesian statistics, conjugate prior, posterior probability, credible interval
fetched: 2026-07-02
---

# Bayesian statistics

**Bayesian statistics** (/ˈbeɪziən/ *BAY-zee-ən* or /ˈbeɪʒən/ *BAY-zhən*) is a theory in the field of statistics based on the Bayesian interpretation of probability, where probability expresses a *degree of belief* in an event. The degree of belief may be based on prior knowledge about the event, such as the results of previous experiments, or on personal beliefs about the event. This differs from a number of other interpretations of probability, such as the frequentist interpretation, which views probability as the limit of the relative frequency of an event after many trials. More concretely, analysis in Bayesian methods codifies prior knowledge in the form of a prior distribution.

Bayesian statistical methods use Bayes' theorem to compute and update probabilities after obtaining new data. Bayes' theorem describes the conditional probability of an event based on data as well as prior information or beliefs about the event or conditions related to the event. For example, in Bayesian inference, Bayes' theorem can be used to estimate the parameters of a probability distribution or statistical model. Since Bayesian statistics treats probability as a degree of belief, Bayes' theorem can directly assign a probability distribution that quantifies the belief to the parameter or set of parameters.

Bayesian statistics is named after Thomas Bayes, who formulated a specific case of Bayes' theorem in a paper published in 1763. In several papers spanning from the late 18th to the early 19th centuries, Pierre-Simon Laplace developed the Bayesian interpretation of probability. Laplace used methods now considered Bayesian to solve a number of statistical problems. While many Bayesian methods were developed by later authors, the term "Bayesian" was not commonly used to describe these methods until the 1950s. Throughout much of the 20th century, Bayesian methods were viewed unfavorably by many statisticians due to philosophical and practical considerations. Many of these methods required much computation, and most widely used approaches during that time were based on the frequentist interpretation. However, with the advent of powerful computers and new algorithms like Markov chain Monte Carlo, Bayesian methods have gained increasing prominence in statistics in the 21st century.

## Bayes' theorem

Bayes' theorem is used in Bayesian methods to update probabilities, which are degrees of belief, after obtaining new data. Given two events A and B , the conditional probability of A given that B is true is expressed as follows:

$P(A\mid B)={\frac {P(B\mid A)P(A)}{P(B)}}$

where $P(B)\neq 0$ . Although Bayes' theorem is a fundamental result of probability theory, it has a specific interpretation in Bayesian statistics. In the above equation, A usually represents a proposition (such as the statement that a coin lands on heads fifty percent of the time) and B represents the evidence, or new data that is to be taken into account (such as the result of a series of coin flips). $P(A)$ is the prior probability of A which expresses one's beliefs about A before evidence is taken into account. The prior probability may also quantify prior knowledge or information about A . $P(B\mid A)$ is the likelihood function, which can be interpreted as the probability of the evidence B given that A is true. The likelihood quantifies the extent to which the evidence B supports the proposition A . $P(A\mid B)$ is the posterior probability, the probability of the proposition A after taking the evidence B into account. Essentially, Bayes' theorem updates one's prior beliefs $P(A)$ after considering the new evidence B .

The probability of the evidence $P(B)$ can be calculated using the law of total probability. If $\{A_{1},A_{2},\dots ,A_{n}\}$ is a partition of the sample space, which is the set of all outcomes of an experiment, then,

$P(B)=P(B\mid A_{1})P(A_{1})+P(B\mid A_{2})P(A_{2})+\dots +P(B\mid A_{n})P(A_{n})=\sum _{i}P(B\mid A_{i})P(A_{i})$

When there are an infinite number of outcomes, it is necessary to integrate over all outcomes to calculate $P(B)$ using the law of total probability. Often, $P(B)$ is difficult to calculate as the calculation would involve sums or integrals that would be time-consuming to evaluate, so often only the product of the prior and likelihood is considered, since the evidence does not change in the same analysis. The posterior is proportional to this product:

$P(A\mid B)\propto P(B\mid A)P(A)$

The maximum a posteriori, which is the mode of the posterior and is often computed in Bayesian statistics using mathematical optimization methods, remains the same. The posterior can be approximated even without computing the exact value of $P(B)$ with methods such as Markov chain Monte Carlo or variational Bayesian methods.

### Construction

The classical textbook equation for the posterior in Bayesian statistics is usually stated as $\pi (\theta \mid x)={\mathcal {L}}(x\mid \theta )\cdot {\frac {\pi (\theta )}{\int _{\Theta }{\mathcal {L}}(x\mid \theta ')\cdot \pi (\theta ')\;d\theta '}}$ where $\pi (\theta \mid x)$ is the updated probability of $\theta$ being the true parameter after collecting the data x , ${\mathcal {L}}(x\mid \theta )$ is the likelihood of collecting the data x given the parameter $\theta$ , $\pi (\theta )$ is the prior belief of $\theta$ 's likelihood and the integral in the denominator gives the probability of collecting the data x .

Mathematically, this version of Bayes' theorem can be constructed in the following way: Suppose $(\Omega ,\Sigma _{\Omega },\lbrace P_{\theta }\mid \theta \in \Theta \rbrace )$ to be some parametric statistical model and $(\Theta ,\Sigma _{\Theta },\pi )$ to be a probability space over the parameter space. We can construct a new probability space $(\Theta \times \Omega ,\Sigma _{\Theta }\otimes \Sigma _{\Omega },Q)$ where Q is a sort of product measure defined as: $Q(M):=(\pi \otimes P_{\cdot })(M)=\int _{\Theta }P_{\theta '}(M_{\theta '})\;d\pi (\theta '),$ where $M_{\theta '}:=\{\omega \in \Omega \mid (\theta ',\omega )\in M\})$ .

Now, let $A_{\theta }:=\lbrace \theta \rbrace \times \Omega$ and $B_{x}:=\Theta \times \lbrace x\rbrace$ , then we get: $Q(\theta )=Q(A_{\theta })=\int _{\lbrace \theta \rbrace }P_{\theta '}(\Omega )\;d\pi (\theta ')=\pi (\lbrace \theta \rbrace )\cdot P_{\theta }(\Omega )=\pi (\theta )$

and hence

$Q(x\mid \theta )={\frac {Q(B_{x}\cap A_{\theta })}{Q(A_{\theta })}}={\frac {\pi (\theta )\cdot P_{\theta }(\lbrace x\rbrace )}{\pi (\theta )}}=P_{\theta }(x)$

both as empirically might be expected. Thus, Bayes' theorem states:

$Q(\theta \mid x)=P_{\theta }(x)\cdot {\frac {\pi (\theta )}{Q(x)}}$

If $\pi \ll \lambda$ (i.e. absolutely continuous w.r.t. the Lebesgue measure ), then there exists a density such that $\pi (\theta )={\frac {d\pi }{d\lambda }}(\theta )$ and we can write:

$Q(x)=\int _{\Theta }P_{\theta '}(x)\;d\pi (\theta ')=\int _{\Theta }P_{\theta '}(x)\cdot \pi (\theta ')\;d\theta '$

Else, if $\pi \ll \nu$ (absolutely continuous w.r.t. counting measure), analogous we can write:

$Q(x)=\int _{\Theta }P_{\theta '}(x)\cdot \pi (\theta ')\;d\nu (\theta ')=\sum _{i}P_{\theta _{i}}(x)\cdot \pi (\theta _{i})$

Thus, by identifying $Q(\theta \mid x)$ with $\pi (\theta \mid x)$ and ${\mathcal {L}}(x\mid \theta )$ with $P_{\theta }(x)$ we arrive at the classical equation stated above.

## Bayesian methods

The general set of statistical techniques can be divided into a number of activities, many of which have special Bayesian versions.

### Bayesian inference

Bayesian inference refers to statistical inference where uncertainty in inferences is quantified using probability. In classical frequentist inference, model parameters and hypotheses are considered to be fixed. Probabilities are not assigned to parameters or hypotheses in frequentist inference. For example, it would not make sense in frequentist inference to directly assign a probability to an event that can only happen once, such as the result of the next flip of a fair coin. However, it would make sense to state that the proportion of heads approaches one-half as the number of coin flips increases.

Statistical models specify a set of statistical assumptions and processes that represent how the sample data are generated. Statistical models have a number of parameters that can be modified. For example, a coin can be represented as samples from a Bernoulli distribution, which models two possible outcomes. The Bernoulli distribution has a single parameter equal to the probability of one outcome, which in most cases is the probability of landing on heads. Devising a good model for the data is central in Bayesian inference. In most cases, models only approximate the true process, and may not take into account certain factors influencing the data. In Bayesian inference, probabilities can be assigned to model parameters. Parameters can be represented as random variables. Bayesian inference uses Bayes' theorem to update probabilities after more evidence is obtained or known. Furthermore, Bayesian methods allow for placing priors on entire models and calculating their posterior probabilities using Bayes' theorem. These posterior probabilities are proportional to the product of the prior and the marginal likelihood, where the marginal likelihood is the integral of the sampling density over the prior distribution of the parameters. In complex models, marginal likelihoods are generally computed numerically.

### Statistical modeling

The formulation of statistical models using Bayesian statistics has the identifying feature of requiring the specification of prior distributions for any unknown parameters. Indeed, parameters of prior distributions may themselves have prior distributions, leading to Bayesian hierarchical modeling, also known as multi-level modeling. A special case is Bayesian networks.

For conducting a Bayesian statistical analysis, best practices are discussed by van de Schoot et al.

### Design of experiments

The Bayesian design of experiments includes a concept called 'influence of prior beliefs'. This approach uses sequential analysis techniques to include the outcome of earlier experiments in the design of the next experiment. This is achieved by updating 'beliefs' through the use of prior and posterior distribution. This allows the design of experiments to make good use of resources of all types. An example of this is the multi-armed bandit problem.

### Exploratory analysis of Bayesian models

Exploratory analysis of Bayesian models is an adaptation or extension of the exploratory data analysis approach to the needs and peculiarities of Bayesian modeling. In the words of Persi Diaconis:

> Exploratory data analysis seeks to reveal structure, or simple descriptions in data. We look at numbers or graphs and try to find patterns. We pursue leads suggested by background information, imagination, patterns perceived, and experience with other data analyses

The inference process generates a posterior distribution, which has a central role in Bayesian statistics, together with other distributions like the posterior predictive distribution and the prior predictive distribution. The correct visualization, analysis, and interpretation of these distributions is key to properly answer the questions that motivate the inference process.

When working with Bayesian models there are a series of related tasks that need to be addressed besides inference itself:

- Diagnoses of the quality of the inference, this is needed when using numerical methods such as Markov chain Monte Carlo techniques
- Model criticism, including evaluations of both model assumptions and model predictions
- Comparison of models, including model selection or model averaging
- Preparation of the results for a particular audience

All these tasks are part of the Exploratory analysis of Bayesian models approach and successfully performing them is central to the iterative and interactive modeling process. These tasks require both numerical and visual summaries.
