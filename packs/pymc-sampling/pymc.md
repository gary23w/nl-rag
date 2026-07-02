---
title: "PyMC"
source: https://en.wikipedia.org/wiki/PyMC
domain: pymc-sampling
license: CC-BY-SA-4.0
tags: pymc library, hamiltonian monte carlo, bayesian modeling, markov chain sampling
fetched: 2026-07-02
---

# PyMC

**PyMC** (formerly known as PyMC3) is a probabilistic programming library for Python. It can be used for Bayesian statistical modeling and probabilistic machine learning.

PyMC performs inference based on advanced Markov chain Monte Carlo and/or variational fitting algorithms. It is a rewrite from scratch of the previous version of the PyMC software. Unlike PyMC2, which had used Fortran extensions for performing computations, PyMC relies on PyTensor, a Python library that allows defining, optimizing, and efficiently evaluating mathematical expressions involving multi-dimensional arrays. From version 3.8 PyMC relies on ArviZ to handle plotting, diagnostics, and statistical checks. PyMC and Stan are the two most popular probabilistic programming tools. PyMC is an open source project, developed by the community and has been fiscally sponsored by NumFOCUS.

PyMC has been used to solve inference problems in several scientific domains, including astronomy, epidemiology, molecular biology, crystallography, chemistry, ecology and psychology. Previous versions of PyMC were also used widely, for example in climate science, public health, neuroscience, and parasitology.

After Theano announced plans to discontinue development in 2017, the PyMC team evaluated TensorFlow Probability as a computational backend, but decided in 2020 to fork Theano under the name Aesara. Large parts of the Theano codebase have been refactored and compilation through JAX and Numba were added. The PyMC team has released the revised computational backend under the name PyTensor and continues the development of PyMC.

## Inference engines

PyMC implements non-gradient-based and gradient-based Markov chain Monte Carlo (MCMC) algorithms for Bayesian inference and stochastic, gradient-based variational Bayesian methods for approximate Bayesian inference.

- MCMC-based algorithms:
  - No-U-Turn sampler (NUTS), a variant of Hamiltonian Monte Carlo and PyMC's default engine for continuous variables
  - Metropolis–Hastings, PyMC's default engine for discrete variables
  - Sequential Monte Carlo for static posteriors
  - Sequential Monte Carlo for approximate Bayesian computation
- Variational inference algorithms:
  - Black-box Variational Inference
