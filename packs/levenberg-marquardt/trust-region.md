---
title: "Trust region"
source: https://en.wikipedia.org/wiki/Trust_region
domain: levenberg-marquardt
license: CC-BY-SA-4.0
tags: levenberg marquardt algorithm, nonlinear least squares, damped gauss newton, trust region
fetched: 2026-07-02
---

# Trust region

In mathematical optimization, a **trust region** is the subset of the region of the objective function that is approximated using a model function (often a quadratic). If an adequate model of the objective function is found within the trust region, then the region is expanded; conversely, if the approximation is poor, then the region is contracted.

The fit is evaluated by comparing the ratio of expected improvement from the model approximation with the actual improvement observed in the objective function. Simple thresholding of the ratio is used as the criterion for expansion and contraction—a model function is "trusted" only in the region where it provides a reasonable approximation.

Trust-region methods are in some sense dual to line-search methods: trust-region methods first choose a step size (the size of the trust region) and then a step direction, while line-search methods first choose a step direction and then a step size.

The general idea behind trust region methods is known by many names; the earliest use of the term seems to be by Sorensen (1982). A popular textbook by Fletcher (1980) calls these algorithms **restricted-step methods**. Additionally, in an early foundational work on the method, Goldfeld, Quandt, and Trotter (1966) refer to it as **quadratic hill-climbing**.

## Example

Conceptually, in the Levenberg–Marquardt algorithm, the objective function is iteratively approximated by a quadratic surface, then using a linear solver, the estimate is updated. This alone may not converge nicely if the initial guess is too far from the optimum. For this reason, the algorithm instead restricts each step, preventing it from stepping "too far". It operationalizes "too far" as follows. Rather than solving $A\,\Delta x=b$ for $\Delta x$ , it solves ${\big (}A+\lambda \operatorname {diag} (A){\big )}\,\Delta x=b$ , where $\operatorname {diag} (A)$ is the diagonal matrix with the same diagonal as *A*, and λ is a parameter that controls the trust-region size. Geometrically, this adds a paraboloid centered at $\Delta x=0$ to the quadratic form, resulting in a smaller step.

The trick is to change the trust-region size (λ). At each iteration, the damped quadratic fit predicts a certain reduction in the cost function, $\Delta f_{\text{pred}}$ , which we would expect to be a smaller reduction than the true reduction. Given $\Delta x$ , we can evaluate

$\Delta f_{\text{actual}}=f(x)-f(x+\Delta x).$

By looking at the ratio $\Delta f_{\text{pred}}/\Delta f_{\text{actual}}$ , we can adjust the trust-region size. In general, we expect $\Delta f_{\text{pred}}$ to be a bit smaller than $\Delta f_{\text{actual}}$ , and so the ratio would be between, say, 0.25 and 0.5. If the ratio is more than 0.5, then we are damping the step too much, so expand the trust region (decrease λ) and iterate. If the ratio is smaller than 0.25, then the true function is diverging "too much" from the trust-region approximation, so shrink the trust region (increase λ) and try again.

Note that the Levenberg-Marquardt algorithm does not have an explicit trust region, and is instead often referred to as a damped Gauss-Newton method. A more fitting example of a trust region method would be Powell's dog leg method, where the update step magnitude is explicitly constrained to a trust region, c.f. Madsen et al. .
