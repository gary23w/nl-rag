---
title: "Model selection"
source: https://en.wikipedia.org/wiki/Model_selection
domain: cross-validation-stats
license: CC-BY-SA-4.0
tags: cross-validation, model overfitting, model selection, hyperparameter optimization
fetched: 2026-07-02
---

# Model selection

**Model selection** is the task of selecting a model from among various candidates on the basis of performance criterion to choose the best one. In the context of machine learning and more generally statistical analysis, this may be the selection of a statistical model from a set of candidate models, given data. In the simplest cases, a pre-existing set of data is considered. However, the task can also involve the design of experiments such that the data collected is well-suited to the problem of model selection. Given candidate models of similar predictive or explanatory power, the simplest model is most likely to be the best choice (Occam's razor).

Konishi & Kitagawa (2008, p. 75) state, "The majority of the problems in statistical inference can be considered to be problems related to statistical modeling". Relatedly, Cox (2006, p. 197) has said, "How [the] translation from subject-matter problem to statistical model is done is often the most critical part of an analysis".

Model selection may also refer to the problem of selecting a few representative models from a large set of computational models for the purpose of decision making or optimization under uncertainty.

In machine learning, algorithmic approaches to model selection include feature selection, hyperparameter optimization, and statistical learning theory.

## Introduction

In its most basic forms, model selection is one of the fundamental tasks of scientific inquiry. Determining the principle that explains a series of observations is often linked directly to a mathematical model predicting those observations. For example, when Galileo performed his inclined plane experiments, he demonstrated that the motion of the balls fitted the parabola predicted by his model .

Of the countless number of possible mechanisms and processes that could have produced the data, how can one even begin to choose the best model? The mathematical approach commonly taken decides among a set of candidate models; this set must be chosen by the researcher. Often simple models such as polynomials are used, at least initially . Burnham & Anderson (2002) emphasize throughout their book the importance of choosing models based on sound scientific principles, such as understanding of the phenomenological processes or mechanisms (e.g., chemical reactions) underlying the data.

Once the set of candidate models has been chosen, the statistical analysis allows us to select the best of these models. What is meant by *best* is controversial. A good model selection technique will balance goodness of fit with simplicity. More complex models will be better able to adapt their shape to fit the data (for example, a fifth-order polynomial can exactly fit six points), but the additional parameters may not represent anything useful. (Perhaps those six points are really just randomly distributed about a straight line.) Goodness of fit is generally determined using a likelihood ratio approach, or an approximation of this, leading to a chi-squared test. The complexity is generally measured by counting the number of parameters in the model.

Model selection techniques can be considered as estimators of some physical quantity, such as the probability of the model producing the given data. The bias and variance are both important measures of the quality of this estimator; efficiency is also often considered.

A standard example of model selection is that of curve fitting, where, given a set of points and other background knowledge (e.g. points are a result of i.i.d. samples), we must select a curve that describes the function that generated the points.

## Two directions of model selection

There are two main objectives in inference and learning from data. One is for scientific discovery, also called statistical inference, understanding of the underlying data-generating mechanism and interpretation of the nature of the data. Another objective of learning from data is for predicting future or unseen observations, also called Statistical Prediction. In the second objective, the data scientist does not necessarily concern an accurate probabilistic description of the data. Of course, one may also be interested in both directions.

In line with the two different objectives, model selection can also have two directions: model selection for inference and model selection for prediction. The first direction is to identify the best model for the data, which will preferably provide a reliable characterization of the sources of uncertainty for scientific interpretation. For this goal, it is significantly important that the selected model is not too sensitive to the sample size. Accordingly, an appropriate notion for evaluating model selection is the selection consistency, meaning that the most robust candidate will be consistently selected given sufficiently many data samples.

The second direction is to choose a model as machinery to offer excellent predictive performance. For the latter, however, the selected model may simply be the lucky winner among a few close competitors, yet the predictive performance can still be the best possible. If so, the model selection is fine for the second goal (prediction), but the use of the selected model for insight and interpretation may be severely unreliable and misleading. Moreover, for very complex models selected this way, even predictions may be unreasonable for data only slightly different from those on which the selection was made.

## Methods to assist in choosing the set of candidate models

- Data transformation (statistics)
- Exploratory data analysis
- Model specification
- Scientific method

## Criteria

Below is a list of criteria for model selection. The most commonly used information criteria are (i) the Akaike information criterion and (ii) the Bayes factor and/or the Bayesian information criterion (which to some extent approximates the Bayes factor), see Stoica & Selen (2004) for a review.

- Akaike information criterion (AIC), a measure of the goodness fit of an estimated statistical model
- Bayes factor
- Bayesian information criterion (BIC), also known as the Schwarz information criterion, a statistical criterion for model selection
- Bridge criterion (BC), a statistical criterion that can attain the better performance of AIC and BIC despite the appropriateness of model specification.
- Cross-validation
- Deviance information criterion (DIC), another Bayesian oriented model selection criterion
- False discovery rate
- Focused information criterion (FIC), a selection criterion sorting statistical models by their effectiveness for a given focus parameter
- Hannan–Quinn information criterion, an alternative to the Akaike and Bayesian criteria
- Kashyap information criterion (KIC) is a powerful alternative to AIC and BIC, because KIC uses Fisher information matrix
- Likelihood-ratio test
- Mallows's *Cp*
- Minimum description length
- Minimum message length (MML)
- PRESS statistic, also known as the PRESS criterion
- Quasi information criterion (QIC), for model selection where the log-likelihood is replaced by the quasi log-likelihood (e.g., generalized estimating equations)
- Structural risk minimization
- Stepwise regression
- Watanabe–Akaike information criterion (WAIC), also called the widely applicable information criterion
- Extended Bayesian Information Criterion (EBIC) is an extension of ordinary Bayesian information criterion (BIC) for models with high parameter spaces.
- Extended Fisher Information Criterion (EFIC) is a model selection criterion for linear regression models.
- Constrained Minimum Criterion (CMC) is a frequentist method for regression model selection based on the following geometric observations. In the parameter vector space of the full model, every vector represents a model. There exists a ball centered on the true parameter vector of the full model in which the true model is the smallest model (in $L_{0}$ norm). As the sample size goes to infinity, the MLE for the true parameter vector converges to and thus pulls the shrinking likelihood ratio confidence region to the true parameter vector. The confidence region will be inside the ball with probability tending to one. The CMC selects the smallest model in this region. When the region captures the true parameter vector, the CMC selection is the true model. Hence, the probability that the CMC selection is the true model is greater than or equal to the confidence level.

Among these criteria, cross-validation is typically the most accurate, and computationally the most expensive, for supervised learning problems.

Burnham & Anderson (2002, §6.3) say the following:

> There is a variety of model selection methods. However, from the point of view of statistical performance of a method, and intended context of its use, there are only two distinct classes of methods: These have been labeled *efficient* and *consistent*. (...) Under the frequentist paradigm for model selection one generally has three main approaches: (I) optimization of some selection criteria, (II) tests of hypotheses, and (III) ad hoc methods.
