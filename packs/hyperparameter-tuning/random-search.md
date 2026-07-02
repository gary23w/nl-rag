---
title: "Random search"
source: https://en.wikipedia.org/wiki/Random_search
domain: hyperparameter-tuning
license: CC-BY-SA-4.0
tags: hyperparameter tuning, grid search, random search, bayesian optimization, model selection
fetched: 2026-07-02
---

# Random search

**Random search (RS)** is a family of numerical optimization methods that do not require the gradient of the optimization problem, and RS can hence be used on functions that are not continuous or differentiable. Such optimization methods are also known as direct-search, derivative-free, or black-box methods.

Anderson in 1953 reviewed the progress of methods in finding maximum or minimum of problems using a series of guesses distributed with a certain order or pattern in the parameter searching space, e.g. a confounded design with exponentially distributed spacings/steps. This search goes on sequentially on each parameter and refines iteratively on the best guesses from the last sequence. The pattern can be a grid (factorial) search of all parameters, a sequential search on each parameter, or a combination of both. The method was developed to screen the experimental conditions in chemical reactions by a number of scientists listed in Anderson's paper. A MATLAB code reproducing the sequential procedure for the general non-linear regression of an example mathematical model can be found here (JCFit @ GitHub).

The name "random search" is attributed to Rastrigin who made an early presentation of RS along with basic mathematical analysis. RS works by iteratively moving to better positions in the search space, which are sampled from a hypersphere surrounding the current position.

The algorithm described herein is a type of local random search, where every iteration is dependent on the prior iteration's candidate solution. There are alternative random search methods that sample from the entirety of the search space (for example pure random search or uniform global random search), but these are not described in this article.

Random search has been used in artificial neural network for hyper-parameter optimization.

If good parts of the search space occupy 5% of the volume the chances of hitting a good configuration in search space is 5%. The probability of finding at least one good configuration is above 95% after trying out 60 configurations ( $1-0.95^{60}=0.953>0.95$ , making use of the counterprobability).

## Algorithm

Let *f*: ℝ*n* → ℝ be the fitness or cost function which must be minimized. Let **x** ∈ ℝ*n* designate a position or candidate solution in the search-space. The basic RS algorithm can then be described as:

1. Initialize **x** with a random position in the search-space.
2. Until a termination criterion is met (e.g. number of iterations performed, or adequate fitness reached), repeat the following:
  1. Sample a new position **y** from the hypersphere of a given radius surrounding the current position **x** (see e.g. Marsaglia's technique for sampling a hypersphere.)
  2. If *f*(**y**) < *f*(**x**) then move to the new position by setting **x** = **y**

## Variants

Truly random search is purely by luck and varies from very costive to very lucky, but the structured random search is strategic. A number of RS variants have been introduced in the literature with structured sampling in the searching space:

- Friedman-Savage procedure: Sequentially search each parameter with a set of guesses that have a space pattern between the initial guess and the boundaries. An example of exponentially distributed steps can be found here in a MATLAB code (JCFit @ GitHub). This example code converges 1-2 orders of magnitude slower than the Levenberg–Marquardt algorithm, with an example also provided in the GitHub.
- Fixed Step Size Random Search (FSSRS) is Rastrigin's basic algorithm which samples from a hypersphere of fixed radius.
- Optimum Step Size Random Search (OSSRS) by Schumer and Steiglitz is primarily a theoretical study on how to optimally adjust the radius of the hypersphere so as to allow for speedy convergence to the optimum. The actual implementation of the OSSRS needs to approximate this optimal radius by repeated sampling and is therefore expensive to execute.
- Adaptive Step Size Random Search (ASSRS) by Schumer and Steiglitz attempts to heuristically adapt the hypersphere's radius: two new candidate solutions are generated, one with the current nominal step size and one with a larger step-size. The larger step size becomes the new nominal step size if and only if it leads to a larger improvement. If for several iterations neither of the steps leads to an improvement, the nominal step size is reduced.
- Optimized Relative Step Size Random Search (ORSSRS) by Schrack and Choit approximate the optimal step size by a simple exponential decrease. However, the formula for computing the decrease factor is somewhat complicated.
