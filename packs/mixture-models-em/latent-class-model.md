---
title: "Latent class model"
source: https://en.wikipedia.org/wiki/Latent_class_model
domain: mixture-models-em
license: CC-BY-SA-4.0
tags: mixture model, expectation maximization, Gaussian mixture model, latent class model
fetched: 2026-07-02
---

# Latent class model

In statistics, a **latent class model** (**LCM**) is a model for clustering multivariate discrete data. It assumes that the data arise from a mixture of discrete distributions, within each of which the variables are independent. It is called a latent class model because the class to which each data point belongs is unobserved (or latent).

**Latent class analysis** (**LCA**) is a subset of structural equation modeling used to find groups or subtypes of cases in multivariate categorical data. These groups or subtypes of cases are called "latent classes".

When faced with the following situation, a researcher might opt to use LCA to better understand the data: Symptoms a, b, c, and d have been recorded in a variety of patients diagnosed with diseases X, Y, and Z. Disease X is associated with symptoms a, b, and c; disease Y is linked to symptoms b, c, and d; and disease Z is connected to symptoms a, c, and d.

In this context, the LCA would attempt to detect the presence of latent classes (i.e., the disease entities), thus creating patterns of association in the symptoms. As in factor analysis, LCA can also be used to classify cases according to their maximum likelihood class membership probability.

The key criterion for resolving the LCA is identifying latent classes in which the observed symptom associations are effectively rendered null. This is because within each class, the diseases responsible for the symptoms create a structure of dependencies. As a result, the symptoms become conditionally independent, meaning that, given the class a case belongs to, the symptoms are no longer related to one another.

## Model

Within each latent class, the observed variables are statistically independent—an essential aspect of latent class modeling. Usually, the observed variables are statistically dependent. By introducing the latent variable, independence is restored in the sense that within classes, variables are independent (local independence). Therefore, the association between the observed variables is explained by the classes of the latent variable (McCutcheon, 1987).

In one form, the LCM is written as

$p_{i_{1},i_{2},\ldots ,i_{N}}\approx \sum _{t}^{T}p_{t}\,\prod _{n}^{N}p_{i_{n},t}^{n},$

where T is the number of latent classes and $p_{t}$ are the so-called recruitment or unconditional probabilities that should sum to one. $p_{i_{n},t}^{n}$ are the marginal or conditional probabilities.

For a two-way latent class model, the form is

$p_{ij}\approx \sum _{t}^{T}p_{t}\,p_{it}\,p_{jt}.$

This two-way model is related to probabilistic latent semantic analysis and non-negative matrix factorization.

The probability model used in LCA is closely related to the Naive Bayes classifier. The main difference is that in LCA, the class membership of an individual is a latent variable, whereas in Naive Bayes classifiers, the class membership is an observed label.

There are a number of methods with distinct names and uses that share a common relationship. Cluster analysis is, like LCA, used to discover taxon-like groups of cases in data. Multivariate mixture estimation (MME) is applicable to continuous data and assumes that such data arise from a mixture of distributions, such as a set of heights arising from a mixture of men and women. If a multivariate mixture estimation is constrained so that measures must be uncorrelated within each distribution, it is termed latent profile analysis. Modified to handle discrete data, this constrained analysis is known as LCA. Discrete latent trait models further constrain the classes to form from segments of a single dimension, allocating members to classes based on that dimension. An example would be assigning cases to social classes based on ability or merit.

In a practical instance, the variables could be multiple choice items of a political questionnaire. In this case, the data consists of an N-way contingency table with answers to the items for a number of respondents. In this example, the latent variable refers to political opinion, and the latent classes to political groups. Given group membership, the conditional probabilities specify the chance that certain answers are chosen.

## Application

LCA may be used in many fields, such as: collaborative filtering, *Behavior Genetics* and Evaluation of diagnostic tests.
