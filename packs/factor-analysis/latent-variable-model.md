---
title: "Latent variable model"
source: https://en.wikipedia.org/wiki/Latent_variable_model
domain: factor-analysis
license: CC-BY-SA-4.0
tags: factor analysis, exploratory factor analysis, varimax rotation, latent variable
fetched: 2026-07-02
---

# Latent variable model

A **latent variable model** is a statistical model that relates a set of observable variables (also called *manifest variables* or *indicators*) to a set of latent variables. Latent variable models are applied across a wide range of fields such as biology, computer science, and social science. Common use cases for latent variable models include applications in psychometrics (e.g., summarizing responses to a set of survey questions with a factor analysis model positing a smaller number of psychological attributes, such as the trait extraversion, that are presumed to cause the survey question responses), and natural language processing (e.g., a topic model summarizing a corpus of texts with a number of "topics").

It is assumed that the responses on the indicators or manifest variables are the result of an individual's position on the latent variable(s), and that the manifest variables have nothing in common after controlling for the latent variable (local independence).

Different types of latent variable models can be grouped according to whether the manifest and latent variables are categorical or continuous:

|   | Manifest variables |   |
|---|---|---|
| Latent variables | Continuous | Categorical |
| Continuous | Factor analysis | Item response theory |
| Categorical | Latent profile analysis | Latent class analysis |

The Rasch model represents the simplest form of item response theory. Mixture models are central to latent profile analysis.

In factor analysis and latent trait analysis the latent variables are treated as continuous normally distributed variables, and in latent profile analysis and latent class analysis as from a multinomial distribution. The manifest variables in factor analysis and latent profile analysis are continuous and in most cases, their conditional distribution given the latent variables is assumed to be normal. In latent trait analysis and latent class analysis, the manifest variables are discrete. These variables could be dichotomous, ordinal or nominal variables. Their conditional distributions are assumed to be binomial or multinomial.
