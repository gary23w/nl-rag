---
title: "Response surface methodology"
source: https://en.wikipedia.org/wiki/Response_surface_methodology
domain: response-surface-methodology
license: CC-BY-SA-4.0
tags: response surface methodology, central composite design, Box Behnken, optimal design
fetched: 2026-07-02
---

# Response surface methodology

In statistics, **response surface methodology** (**RSM**) explores the relationships between several explanatory variables and one or more response variables. RSM is an empirical model which employs the use of mathematical and statistical techniques to relate input variables, otherwise known as factors, to the response. RSM became very useful because other methods available, such as the theoretical model, could be very cumbersome to use, time-consuming, inefficient, error-prone, and unreliable. The method was introduced by George E. P. Box and K. B. Wilson in 1951. The main idea of RSM is to use a sequence of designed experiments to obtain an optimal response. Box and Wilson suggest using a second-degree polynomial model to do this. They acknowledge that this model is only an approximation, but they use it because such a model is easy to estimate and apply, even when little is known about the process.

Statistical approaches such as RSM can be employed to maximize the production of a special substance by optimization of operational factors. Of late, for formulation optimization, the RSM, using proper **design of experiments** (**DoE**), has become extensively used. In contrast to conventional methods, the interaction among process variables can be determined by statistical techniques.

## Basic approach of response surface methodology

An easy way to estimate a first-degree polynomial model is to use a factorial experiment or a fractional factorial design. This is sufficient to determine which explanatory variables affect the response variable(s) of interest. Once it is suspected that only significant explanatory variables are left, then a more complicated design, such as a central composite design can be implemented to estimate a second-degree polynomial model, which is still only an approximation at best. However, the second-degree model can be used to optimize (maximize, minimize, or attain a specific target for) the response variable(s) of interest.

## Important RSM properties and features

**Orthogonality**

The property that allows individual effects of the k-factors to be estimated independently without (or with minimal) confounding. Also orthogonality provides minimum variance estimates of the model coefficient so that they are uncorrelated.

**Rotatability**

The property of rotating points of the design about the center of the factor space. The moments of the distribution of the design points are constant.

**Uniformity**

A third property of CCD designs used to control the number of center points is uniform precision (or Uniformity).

## Special geometries

### Cube

Cubic designs are discussed by Kiefer, by Atkinson, Donev, and Tobias and by Hardin and Sloane.

### Sphere

Spherical designs are discussed by Kiefer and by Hardin and Sloane.

### Simplex geometry and mixture experiments

Mixture experiments are discussed in many books on the design of experiments, and in the response-surface methodology textbooks of Box and Draper and of Atkinson, Donev and Tobias. An extensive discussion and survey appears in the advanced textbook by John Cornell.

## Extensions

### Multiple objective functions

Some extensions of response surface methodology deal with the multiple response problem. Multiple response variables create difficulty because what is optimal for one response may not be optimal for other responses. Other extensions are used to reduce variability in a single response while targeting a specific value, or attaining a near maximum or minimum while preventing variability in that response from getting too large.

## Practical concerns

Response surface methodology uses statistical models, and therefore practitioners need to be aware that even the best statistical model is an approximation to reality. In practice, both the models and the parameter values are unknown, and subject to uncertainty on top of ignorance. Of course, an estimated optimum point need not be optimum in reality, because of the errors of the estimates and of the inadequacies of the model.

Nonetheless, response surface methodology has an effective track-record of helping researchers improve products and services: For example, Box's original response-surface modeling enabled chemical engineers to improve a process that had been stuck at a saddle-point for years. The engineers had not been able to afford to fit a cubic three-level design to estimate a quadratic model, and their biased linear-models estimated the gradient to be zero. Box's design reduced the costs of experimentation so that a quadratic model could be fit, which led to a (long-sought) ascent direction.
