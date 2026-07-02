---
title: "Stan (software)"
source: https://en.wikipedia.org/wiki/Stan_(software)
domain: stan-language
license: CC-BY-SA-4.0
tags: stan language, statistical modeling language, hamiltonian monte carlo, bayesian estimation
fetched: 2026-07-02
---

# Stan (software)

**Stan** is a probabilistic programming language for statistical inference written in C++. The Stan language is used to specify a (Bayesian) statistical model with an imperative program calculating the log probability density function.

Stan is licensed under the New BSD License. Stan is named in honour of Stanislaw Ulam, pioneer of the Monte Carlo method.

Stan was created by a development team consisting of 52 members that includes Andrew Gelman, Bob Carpenter, Daniel Lee, Ben Goodrich, and others.

## Example

A simple linear regression model can be described as $y_{n}=\alpha +\beta x_{n}+\epsilon _{n}$ , where $\epsilon _{n}\sim {\text{normal}}(0,\sigma )$ . This can also be expressed as $y_{n}\sim {\text{normal}}(\alpha +\beta X_{n},\sigma )$ . The latter form can be written in Stan as the following:

```mw
data {
  int<lower=0> N;
  vector[N] x;
  vector[N] y;
}
parameters {
  real alpha;
  real beta;
  real<lower=0> sigma;
}
model {
  y ~ normal(alpha + beta * x, sigma);
}
```

## Interfaces

The Stan language itself can be accessed through several interfaces:

- CmdStan – a command-line executable for the shell,
- CmdStanR and rstan – R software libraries,
- CmdStanPy and PyStan – libraries for the Python programming language,
- CmdStan.rb - library for the Ruby programming language,
- MatlabStan – integration with the MATLAB numerical computing environment,
- Stan.jl – integration with the Julia programming language,
- StataStan – integration with Stata.
- Stan Playground - online at [1]

In addition, higher-level interfaces are provided with packages using Stan as backend, primarily in the R language:

- *rstanarm* provides a drop-in replacement for frequentist models provided by base R and *lme4* using the R formula syntax;
- *brms* provides a wide array of linear and nonlinear models using the R formula syntax;
- *prophet* provides automated procedures for time series forecasting.

## Algorithms

Stan implements gradient-based Markov chain Monte Carlo (MCMC) algorithms for Bayesian inference, stochastic, gradient-based variational Bayesian methods for approximate Bayesian inference, and gradient-based optimization for penalized maximum likelihood estimation.

- MCMC algorithms:
  - Hamiltonian Monte Carlo (HMC)
  - No-U-Turn sampler (NUTS), a variant of HMC and Stan's default MCMC engine
- Variational inference algorithms:
  - Automatic Differentiation Variational Inference
  - Pathfinder: Parallel quasi-Newton variational inference
- Optimization algorithms:
  - Limited-memory BFGS (L-BFGS) (Stan's default optimization algorithm)
  - Broyden–Fletcher–Goldfarb–Shanno algorithm (BFGS)
  - Laplace's approximation for classical standard error estimates and approximate Bayesian posteriors

## Automatic differentiation

Stan implements reverse-mode automatic differentiation to calculate gradients of the model, which is required by HMC, NUTS, L-BFGS, BFGS, and variational inference. The automatic differentiation within Stan can be used outside of the probabilistic programming language.

## Usage

Stan is used in fields including social science, pharmaceutical statistics, market research, and medical imaging.
