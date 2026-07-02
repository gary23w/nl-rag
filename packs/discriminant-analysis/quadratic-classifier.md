---
title: "Quadratic classifier"
source: https://en.wikipedia.org/wiki/Quadratic_classifier
domain: discriminant-analysis
license: CC-BY-SA-4.0
tags: linear discriminant analysis, discriminant function, linear classifier, multiclass classification
fetched: 2026-07-02
---

# Quadratic classifier

In statistics, a **quadratic classifier** is a statistical classifier that uses a quadratic decision surface to separate measurements of two or more classes of objects or events. It is a more general version of the linear classifier.

## The classification problem

Statistical classification considers a set of vectors of observations **x** of an object or event, each of which has a known type *y*. This set is referred to as the training set. The problem is then to determine, for a given new observation vector, what the best class should be. For a quadratic classifier, the correct solution is assumed to be quadratic in the measurements, so *y* will be decided based on $\mathbf {x^{T}Ax} +\mathbf {b^{T}x} +c$

In the special case where each observation consists of two measurements, this means that the surfaces separating the classes will be conic sections (i.e., either a line, a circle or ellipse, a parabola or a hyperbola). In this sense, we can state that a quadratic model is a generalization of the linear model, and its use is justified by the desire to extend the classifier's ability to represent more complex separating surfaces.

## Quadratic discriminant analysis

Quadratic discriminant analysis (QDA) is closely related to linear discriminant analysis (LDA), where it is assumed that the measurements from each class are normally distributed. Unlike LDA however, in QDA there is no assumption that the covariance of each of the classes is identical. When the normality assumption is true, the best possible test for the hypothesis that a given measurement is from a given class is the likelihood ratio test. Suppose there are only two groups, with means $\mu _{0},\mu _{1}$ and covariance matrices $\Sigma _{0},\Sigma _{1}$ corresponding to $y=0$ and $y=1$ respectively. Then the likelihood ratio is given by ${\text{Likelihood ratio}}={\frac {{\sqrt {|2\pi \Sigma _{1}|}}^{-1}\exp \left(-{\frac {1}{2}}(\mathbf {x} -{\boldsymbol {\mu }}_{1})^{T}\Sigma _{1}^{-1}(\mathbf {x} -{\boldsymbol {\mu }}_{1})\right)}{{\sqrt {|2\pi \Sigma _{0}|}}^{-1}\exp \left(-{\frac {1}{2}}(\mathbf {x} -{\boldsymbol {\mu }}_{0})^{T}\Sigma _{0}^{-1}(\mathbf {x} -{\boldsymbol {\mu }}_{0})\right)}}<t$ for some threshold t . After some rearrangement, it can be shown that the resulting separating surface between the classes is a quadratic. The sample estimates of the mean vector and variance-covariance matrices will substitute the population quantities in this formula.

## Other

While QDA is the most commonly used method for obtaining a classifier, other methods are also possible. One such method is to create a longer measurement vector from the old one by adding all pairwise products of individual measurements. For instance, the vector $[x_{1},\;x_{2},\;x_{3}]$ would become $[x_{1},\;x_{2},\;x_{3},\;x_{1}^{2},\;x_{1}x_{2},\;x_{1}x_{3},\;x_{2}^{2},\;x_{2}x_{3},\;x_{3}^{2}].$

Finding a quadratic classifier for the original measurements would then become the same as finding a linear classifier based on the expanded measurement vector. This observation has been used in extending neural network models; the "circular" case, which corresponds to introducing only the sum of pure quadratic terms $\;x_{1}^{2}+x_{2}^{2}+x_{3}^{2}+\cdots \;$ with no mixed products ( $\;x_{1}x_{2},\;x_{1}x_{3},\;\ldots \;$ ), has been proven to be the optimal compromise between extending the classifier's representation power and controlling the risk of overfitting (Vapnik-Chervonenkis dimension).

For linear classifiers based only on dot products, these expanded measurements do not have to be actually computed, since the dot product in the higher-dimensional space is simply related to that in the original space. This is an example of the so-called kernel trick, which can be applied to linear discriminant analysis as well as the support vector machine.
