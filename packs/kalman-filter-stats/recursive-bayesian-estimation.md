---
title: "Recursive Bayesian estimation"
source: https://en.wikipedia.org/wiki/Recursive_Bayesian_estimation
domain: kalman-filter-stats
license: CC-BY-SA-4.0
tags: Kalman filter, extended Kalman filter, unscented transform, particle filter
fetched: 2026-07-02
---

# Recursive Bayesian estimation

In probability theory, statistics, and machine learning, **recursive Bayesian estimation**, also known as a **Bayes filter**, is a general probabilistic approach for estimating an unknown probability density function (PDF) recursively over time using incoming measurements and a mathematical process model. The process relies heavily upon mathematical concepts and models that are theorized within a study of prior and posterior probabilities known as Bayesian statistics.

## In robotics

A Bayes filter is an algorithm used in computer science for calculating the probabilities of multiple beliefs to allow a robot to infer its position and orientation. Essentially, Bayes filters allow robots to continuously update their most likely position within a coordinate system, based on the most recently acquired sensor data. This is a recursive algorithm. It consists of two parts: prediction and innovation. If the variables are normally distributed and the transitions are linear, the Bayes filter becomes equal to the Kalman filter.

In a simple example, a robot moving throughout a grid may have several different sensors that provide it with information about its surroundings. The robot may begin with certainty that it is at position (0,0). However, as it moves further and further from its original position, the robot has continuously less certainty about its position; using a Bayes filter, a probability can be assigned to the robot's belief about its current position, and that probability can be continuously updated from additional sensor information.

## Model

The measurements z are the manifestations of a hidden Markov model (HMM), which means the true state x is assumed to be an unobserved Markov process. The following picture presents a Bayesian network of a HMM.

Because of the Markov assumption, the probability of the current true state given the immediately previous one is conditionally independent of the other earlier states.

$p({\textbf {x}}_{k}|{\textbf {x}}_{k-1},{\textbf {x}}_{k-2},\dots ,{\textbf {x}}_{0})=p({\textbf {x}}_{k}|{\textbf {x}}_{k-1})$

Similarly, the measurement at the *k*-th timestep is dependent only upon the current state, so is conditionally independent of all other states given the current state.

$p({\textbf {z}}_{k}|{\textbf {x}}_{k},{\textbf {x}}_{k-1},\dots ,{\textbf {x}}_{0})=p({\textbf {z}}_{k}|{\textbf {x}}_{k})$

Using these assumptions the probability distribution over all states of the HMM can be written simply as

$p({\textbf {x}}_{0},\dots ,{\textbf {x}}_{k},{\textbf {z}}_{1},\dots ,{\textbf {z}}_{k})=p({\textbf {x}}_{0})\prod _{i=1}^{k}p({\textbf {z}}_{i}|{\textbf {x}}_{i})p({\textbf {x}}_{i}|{\textbf {x}}_{i-1}).$

However, when using the Kalman filter to estimate the state **x**, the probability distribution of interest is associated with the current states conditioned on the measurements up to the current timestep. (This is achieved by marginalising out the previous states and dividing by the probability of the measurement set.)

This leads to the *predict* and *update* steps of the Kalman filter written probabilistically. The probability distribution associated with the predicted state is the sum (integral) of the products of the probability distribution associated with the transition from the (*k* - 1)-th timestep to the *k*-th and the probability distribution associated with the previous state, over all possible $x_{k-1}$ .

$p({\textbf {x}}_{k}|{\textbf {z}}_{1:k-1})=\int p({\textbf {x}}_{k}|{\textbf {x}}_{k-1})p({\textbf {x}}_{k-1}|{\textbf {z}}_{1:k-1})\,d{\textbf {x}}_{k-1}$

The probability distribution of update is proportional to the product of the measurement likelihood and the predicted state.

$p({\textbf {x}}_{k}|{\textbf {z}}_{1:k})={\frac {p({\textbf {z}}_{k}|{\textbf {x}}_{k})p({\textbf {x}}_{k}|{\textbf {z}}_{1:k-1})}{p({\textbf {z}}_{k}|{\textbf {z}}_{1:k-1})}}\propto p({\textbf {z}}_{k}|{\textbf {x}}_{k})p({\textbf {x}}_{k}|{\textbf {z}}_{1:k-1})$

The denominator

$p({\textbf {z}}_{k}|{\textbf {z}}_{1:k-1})=\int p({\textbf {z}}_{k}|{\textbf {x}}_{k})p({\textbf {x}}_{k}|{\textbf {z}}_{1:k-1})d{\textbf {x}}_{k}$

is constant relative to x , so we can always substitute it for a coefficient $\alpha$ , which can usually be ignored in practice. The numerator can be calculated and then simply normalized, since its integral must be unity.

## Applications

- Kalman filter, a recursive Bayesian filter for multivariate normal distributions
- Particle filter, a sequential Monte Carlo (SMC) based technique, which models the PDF using a set of discrete points
- **Grid-based estimators**, which subdivide the PDF into a deterministic discrete grid

## Sequential Bayesian filtering

Sequential Bayesian filtering is the extension of the Bayesian estimation for the case when the observed value changes in time. It is a method to estimate the real value of an observed variable that evolves in time.

There are several variations:

**filtering**

when estimating the

current

value given past and current observations,

**smoothing**

when estimating

past

values given past and current observations, and

**prediction**

when estimating a probable

future

value given past and current observations.

The notion of Sequential Bayesian filtering is extensively used in control and robotics.
