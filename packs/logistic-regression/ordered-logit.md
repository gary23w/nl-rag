---
title: "Ordered logit"
source: https://en.wikipedia.org/wiki/Ordered_logit
domain: logistic-regression
license: CC-BY-SA-4.0
tags: logistic regression, logit, odds ratio, probit model
fetched: 2026-07-02
---

# Ordered logit

In statistics, the **ordered logit model** or **proportional odds logistic regression** is an ordinal regression model—that is, a regression model for ordinal dependent variables—first considered by Peter McCullagh. For example, if one question on a survey is to be answered by a choice among "poor", "fair", "good", "very good" and "excellent", and the purpose of the analysis is to see how well that response can be predicted by the responses to other questions, some of which may be quantitative, then ordered logistic regression may be used. It can be thought of as an extension of the logistic regression model that applies to dichotomous dependent variables, allowing for more than two (ordered) response categories.

## The model and the proportional odds assumption

The model only applies to data that meet the *proportional odds assumption*, the meaning of which can be exemplified as follows. Suppose there are five outcomes: "poor", "fair", "good", "very good", and "excellent". We assume that the probabilities of these outcomes are given by *p*1(*x*), *p*2(*x*), *p*3(*x*), *p*4(*x*), *p*5(*x*), all of which are functions of some independent variable(s) *x*. Then, for a fixed value of *x,* the logarithms of the odds (not the logarithms of the probabilities) of answering in certain ways are:

${\begin{aligned}{\text{poor: }}&\log {\frac {p_{1}(x)}{p_{2}(x)+p_{3}(x)+p_{4}(x)+p_{5}(x)}},\\[8pt]{\text{poor or fair: }}&\log {\frac {p_{1}(x)+p_{2}(x)}{p_{3}(x)+p_{4}(x)+p_{5}(x)}},\\[8pt]{\text{poor, fair, or good: }}&\log {\frac {p_{1}(x)+p_{2}(x)+p_{3}(x)}{p_{4}(x)+p_{5}(x)}},\\[8pt]{\text{poor, fair, good, or very good: }}&\log {\frac {p_{1}(x)+p_{2}(x)+p_{3}(x)+p_{4}(x)}{p_{5}(x)}}\end{aligned}}$

The **proportional odds assumption** states that the numbers added to each of these logarithms to get the next are the same regardless of *x*. In other words, the difference between the logarithm of the odds of having poor or fair health minus the logarithm of odds of having poor health is the same regardless of *x*; similarly, the logarithm of the odds of having poor, fair, or good health minus the logarithm of odds of having poor or fair health is the same regardless of *x*; etc.

Examples of multiple-ordered response categories include bond ratings, opinion surveys with responses ranging from "strongly agree" to "strongly disagree," levels of state spending on government programs (high, medium, or low), the level of insurance coverage chosen (none, partial, or full), and employment status (not employed, employed part-time, or fully employed).

Ordered logit can be derived from a latent-variable model, similar to the one from which binary logistic regression can be derived. Suppose the underlying process to be characterized is

$y^{*}=\mathbf {x} ^{\mathsf {T}}\beta +\varepsilon ,\,$

where $y^{*}$ is an unobserved dependent variable (perhaps the exact level of agreement with the statement proposed by the pollster); $\mathbf {x}$ is the vector of independent variables; $\varepsilon$ is the error term, assumed to follow a standard logistic distribution; and $\beta$ is the vector of regression coefficients which we wish to estimate. Further suppose that while we cannot observe $y^{*}$ , we instead can only observe the categories of response

$y={\begin{cases}0&{\text{if }}y^{*}\leq \mu _{1},\\1&{\text{if }}\mu _{1}<y^{*}\leq \mu _{2},\\2&{\text{if }}\mu _{2}<y^{*}\leq \mu _{3},\\\vdots \\N&{\text{if }}\mu _{N}<y^{*}\end{cases}}$

where the parameters $\mu _{i}$ are the externally imposed endpoints of the observable categories. Then the ordered logit technique will use the observations on *y*, which are a form of censored data on *y**, to fit the parameter vector $\beta$ .

## Model fitting

As with most statistical models, maximum likelihood estimation or Bayesian inference are the most common ways of identifying the parameters. The estimated values indicate the direction and magnitude of the effect of each independent variable on the likelihood of the dependent variable falling into a higher category.

## Applications

Ordered logistic regressions have been used in multiple fields, such as transportation, marketing or disaster management.

In clinical research, the effect a drug may have on a patient may be modeled with ordinal regression. Independent variables may include the use or non-use of the drug, as well as control variables such as demographics and details from medical history. The dependent variable could be ranked on the following list: complete cure, improved symptoms, no change, worsened symptoms, or death.

Another example application are Likert-type items commonly employed in survey research, where respondents rate their agreement on an ordered scale (e.g., "Strongly disagree" to "Strongly agree"). The ordered logit model provides an appropriate fit to these data, preserving the ordering of response options while making no assumptions of the interval distances between options.
