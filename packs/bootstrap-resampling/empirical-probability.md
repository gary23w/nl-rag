---
title: "Empirical probability"
source: https://en.wikipedia.org/wiki/Empirical_probability
domain: bootstrap-resampling
license: CC-BY-SA-4.0
tags: bootstrapping statistics, confidence interval, empirical distribution, standard error
fetched: 2026-07-02
---

# Empirical probability

In probability theory and statistics, the **empirical probability** or **experimental probability** of an event is an estimate of the probability of the event occurring. A common estimator for the empirical probability is the relative frequency, calculated as the ratio of the number of recorded event outcomes to the total number of trials. It is produced by means not of a theoretical sample space but of an empirical sample. More generally, empirical probability may be estimated from experience and observation.

Mathematically, given an event A in a sample space, the relative frequency of A is the ratio ⁠ ${\tfrac {m}{n}},$ ⁠ m being the number of outcomes in which the event A occurs, and n being the total number of outcomes of the experiment.

In simple cases, where the result of a trial only determines whether or not the specified event has occurred, modelling using a binomial distribution might be appropriate and then the empirical estimate is the maximum likelihood estimate. It is the Bayesian estimate for the same case if certain assumptions are made for the prior distribution of the probability. If a trial yields more information, the empirical probability can be improved on by adopting further assumptions in the form of a statistical model: if such a model is fitted, it can be used to derive an estimate of the probability of the specified event

## Advantages and disadvantages

### Advantages

An advantage of estimating probabilities using empirical probabilities is that this procedure is relatively free of assumptions.

For example, consider estimating the probability among a population of men that they satisfy two conditions:

1. that they are over 6 feet in height.
2. that they prefer strawberry jam to raspberry jam.

A direct estimate could be found by counting the number of men who satisfy both conditions to give the empirical probability of the combined condition. An alternative estimate could be found by multiplying the proportion of men who are over 6 feet in height with the proportion of men who prefer strawberry jam to raspberry jam, but this estimate relies on the assumption that the two conditions are statistically independent.

### Disadvantages

A disadvantage in using empirical probabilities arises in estimating probabilities which are either very close to zero, or very close to one. In these cases very large sample sizes would be needed in order to estimate such probabilities to a good standard of relative accuracy. Here statistical models can help, depending on the context, and in general one can hope that such models would provide improvements in accuracy compared to empirical probabilities, provided that the assumptions involved actually do hold.

For example, consider estimating the probability that the lowest of the daily-maximum temperatures at a site in February in any one year is less than zero degrees Celsius. A record of such temperatures in past years could be used to estimate this probability. A model-based alternative would be to select a family of probability distributions and fit it to the dataset containing past years′ values. The fitted distribution would provide an alternative estimate of the desired probability. This alternative method can provide an estimate of the probability even if all values in the record are greater than zero.

## Mixed nomenclature

The phrase *a-posteriori probability* is also used as an alternative to "empirical probability" or "relative frequency". The use of the phrase "a-posteriori" is reminiscent of terms in Bayesian statistics, but is not directly related to Bayesian inference, where *a-posteriori probability* is occasionally used to refer to posterior probability, which is different even though it has a confusingly similar name.

The term *a-posteriori probability*, in its meaning suggestive of "empirical probability", may be used in conjunction with *a priori probability* which represents an estimate of a probability not based on any observations, but based on deductive reasoning.
