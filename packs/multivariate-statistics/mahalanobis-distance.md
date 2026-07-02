---
title: "Mahalanobis distance"
source: https://en.wikipedia.org/wiki/Mahalanobis_distance
domain: multivariate-statistics
license: CC-BY-SA-4.0
tags: multivariate statistics, covariance matrix, Mahalanobis distance, multivariate normal
fetched: 2026-07-02
---

# Mahalanobis distance

The **Mahalanobis distance** is a measure of the distance between a point P and a probability distribution D , introduced by P. C. Mahalanobis in 1936. The mathematical details of Mahalanobis distance first appeared in the *Journal of The Asiatic Society of Bengal* in 1936. Mahalanobis's definition was prompted by the problem of identifying the similarities of skulls based on measurements (the earliest work related to similarities of skulls are from 1922 and another later work is from 1927). R.C. Bose later obtained the sampling distribution of Mahalanobis distance, under the assumption of equal dispersion.

It is a multivariate generalization of the square of the standard score $z=(x-\mu )/\sigma$ : how many standard deviations away P is from the mean of D . This distance is zero for P at the mean of D and grows as P moves away from the mean along each principal component axis. If each of these axes is re-scaled to have unit variance, and whitened to be uncorrelated, then the Mahalanobis distance corresponds to standard Euclidean distance in the transformed space. The Mahalanobis distance is thus unitless, scale-invariant, and takes into account the correlations of the data set.

## Definition

Given a probability distribution Q on $\mathbb {R} ^{N}$ , with mean ${\vec {\mu }}=(\mu _{1},\mu _{2},\mu _{3},\dots ,\mu _{N})^{\mathsf {T}}$ and positive semi-definite covariance matrix $\mathbf {\Sigma }$ , the Mahalanobis distance of a point ${\vec {x}}=(x_{1},x_{2},x_{3},\dots ,x_{N})^{\mathsf {T}}$ from Q is $d_{M}({\vec {x}},Q)={\sqrt {({\vec {x}}-{\vec {\mu }})^{\mathsf {T}}\mathbf {\Sigma } ^{-1}({\vec {x}}-{\vec {\mu }})}}.$ Given two points ${\vec {x}}$ and ${\vec {y}}$ in $\mathbb {R} ^{N}$ , the Mahalanobis distance between them with respect to Q is $d_{M}({\vec {x}},{\vec {y}};Q)={\sqrt {({\vec {x}}-{\vec {y}})^{\mathsf {T}}\mathbf {\Sigma } ^{-1}({\vec {x}}-{\vec {y}})}}.$ which means that $d_{M}({\vec {x}},Q)=d_{M}({\vec {x}},{\vec {\mu }};Q)$ .

Since $\mathbf {\Sigma }$ is positive semi-definite, so is $\mathbf {\Sigma } ^{-1}$ . Thus, the square roots are always defined.

We can find useful decompositions of the squared Mahalanobis distance that help to explain some reasons for the outlyingness of multivariate observations and also provide a graphical tool for identifying outliers.

By the spectral theorem, $\mathbf {\Sigma }$ can be decomposed as $\mathbf {\Sigma } =\mathbf {S} ^{T}\mathbf {S}$ for some real $N\times N$ matrix. One choice for $\mathbf {S}$ is the symmetric square root of $\mathbf {\Sigma }$ , which is the standard deviation matrix. This gives us the equivalent definition $d_{M}({\vec {x}},{\vec {y}};Q)=\|\mathbf {S} ^{-1}({\vec {x}}-{\vec {y}})\|$ where $\|\cdot \|$ is the Euclidean norm. That is, the Mahalanobis distance is the Euclidean distance after a whitening transformation.

The existence of $\mathbf {S}$ is guaranteed by the spectral theorem, but it is not unique. Different choices have different theoretical and practical advantages.

In practice, the distribution Q is usually the sample distribution from a set of IID samples from an underlying unknown distribution, so $\mu$ is the sample mean, and $\mathbf {\Sigma }$ is the covariance matrix of the samples.

When the affine span of the samples is not the entire $\mathbb {R} ^{N}$ , the covariance matrix would not be positive-definite, which means the above definition would not work. However, in general, the Mahalanobis distance is preserved under any full-rank affine transformation of the affine span of the samples. So in case the affine span is not the entire $\mathbb {R} ^{N}$ , the samples can be first orthogonally projected to $\mathbb {R} ^{n}$ , where n is the dimension of the affine span of the samples, then the Mahalanobis distance can be computed as usual.

## Intuitive explanation

Consider the problem of estimating the probability that a test point in *N*-dimensional Euclidean space belongs to a set, where we are given sample points that definitely belong to that set. Our first step would be to find the centroid or center of mass of the sample points. Intuitively, the closer the point in question is to this center of mass, the more likely it is to belong to the set.

However, we also need to know if the set is spread out over a large range or a small range, so that we can decide whether a given distance from the center is noteworthy or not. The simplistic approach is to estimate the standard deviation of the distances of the sample points from the center of mass. If the distance between the test point and the center of mass is less than one standard deviation, then we might conclude that it is highly probable that the test point belongs to the set. The further away it is, the more likely that the test point should not be classified as belonging to the set.

This intuitive approach can be made quantitative by defining the normalized distance between the test point and the set to be ${\frac {\lVert x-\mu \rVert _{2}}{\sigma }}$ , which reads: ${\frac {{\text{testpoint}}-{\text{sample mean}}}{\text{standard deviation}}}$ . By plugging this into the normal distribution, we can derive the probability of the test point belonging to the set.

The drawback of the above approach was that we assumed that the sample points are distributed about the center of mass in a spherical manner. Were the distribution to be decidedly non-spherical, for instance ellipsoidal, then we would expect the probability of the test point belonging to the set to depend not only on the distance from the center of mass, but also on the direction. In those directions where the ellipsoid has a short axis the test point must be closer, while in those where the axis is long the test point can be further away from the center.

Putting this on a mathematical basis, the ellipsoid that best represents the set's probability distribution can be estimated by building the covariance matrix of the samples. The Mahalanobis distance is the distance of the test point from the center of mass divided by the width of the ellipsoid in the direction of the test point.

## Normal distributions

For a normal distribution in any number of dimensions, the probability density of an observation ${\vec {x}}$ is uniquely determined by the Mahalanobis distance d :

${\begin{aligned}\Pr[{\vec {x}}]\,d{\vec {x}}&={\frac {1}{\sqrt {\det(2\pi \mathbf {\Sigma } )}}}\exp \left(-{\frac {({\vec {x}}-{\vec {\mu }})^{\mathsf {T}}\mathbf {\Sigma } ^{-1}({\vec {x}}-{\vec {\mu }})}{2}}\right)\,d{\vec {x}}\\[6pt]&={\frac {1}{\sqrt {\det(2\pi \mathbf {\Sigma } )}}}\exp \left(-{\frac {d^{2}}{2}}\right)\,d{\vec {x}}.\end{aligned}}$

Specifically, $d^{2}$ follows the chi-squared distribution with n degrees of freedom, where n is the number of dimensions of the normal distribution. If the number of dimensions is 2, for example, the probability of a particular calculated d being less than some threshold t is $1-e^{-t^{2}/2}$ . To determine a threshold to achieve a particular probability, p , use ${\textstyle t={\sqrt {-2\ln(1-p)}}}$ , for 2 dimensions. For number of dimensions other than 2, the cumulative chi-squared distribution should be consulted.

In a normal distribution, the region where the Mahalanobis distance is less than one (i.e. the region inside the ellipsoid at distance one) is exactly the region where the probability distribution is concave.

The Mahalanobis distance is proportional, for a normal distribution, to the square root of the negative log-likelihood (after adding a constant so the minimum is at zero).

## Other forms of multivariate location and scatter

The sample mean and covariance matrix can be quite sensitive to outliers, therefore other approaches for calculating the multivariate location and scatter of data are also commonly used when calculating the Mahalanobis distance. The Minimum Covariance Determinant approach estimates multivariate location and scatter from a subset numbering h data points that has the smallest variance-covariance matrix determinant. The Minimum Volume Ellipsoid approach is similar to the Minimum Covariance Determinant approach in that it works with a subset of size h data points, but the Minimum Volume Ellipsoid estimates multivariate location and scatter from the ellipsoid of minimal volume that encapsulates the h data points. Each method varies in its definition of the distribution of the data, and therefore produces different Mahalanobis distances. The Minimum Covariance Determinant and Minimum Volume Ellipsoid approaches are more robust to samples that contain outliers, while the sample mean and covariance matrix tends to be more reliable with small and biased data sets.

## Relationship to normal random variables

In general, given a normal (Gaussian) random variable X with variance $S=1$ and mean $\mu =0$ , any other normal random variable R (with mean $\mu _{1}$ and variance $S_{1}$ ) can be defined in terms of X by the equation $R=\mu _{1}+{\sqrt {S_{1}}}X.$ Conversely, to recover a normalized random variable from any normal random variable, one can typically solve for $X=(R-\mu _{1})/{\sqrt {S_{1}}}$ . If we square both sides, and take the square-root, we will get an equation for a metric that looks a lot like the Mahalanobis distance:

$D={\sqrt {X^{2}}}={\sqrt {(R-\mu _{1})^{2}/S_{1}}}={\sqrt {(R-\mu _{1})S_{1}^{-1}(R-\mu _{1})}}.$

The resulting magnitude is always non-negative and varies with the distance of the data from the mean, attributes that are convenient when trying to define a model for the data.

## Relationship to leverage

Mahalanobis distance is closely related to the leverage statistic, h , but has a different scale:

$D^{2}=(N-1)\left(h-{\tfrac {1}{N}}\right).$

## Applications

Mahalanobis distance is widely used in cluster analysis and classification techniques. It is closely related to Hotelling's T-square distribution used for multivariate statistical testing and Fisher's linear discriminant analysis that is used for supervised classification.

In order to use the Mahalanobis distance to classify a test point as belonging to one of *N* classes, one first estimates the covariance matrix of each class, usually based on samples known to belong to each class. Then, given a test sample, one computes the Mahalanobis distance to each class, and classifies the test point as belonging to that class for which the Mahalanobis distance is minimal.

Mahalanobis distance and leverage are often used to detect outliers, especially in the development of linear regression models. A point that has a greater Mahalanobis distance from the rest of the sample population of points is said to have higher leverage since it has a greater influence on the slope or coefficients of the regression equation. Mahalanobis distance is also used to determine multivariate outliers. Regression techniques can be used to determine if a specific case within a sample population is an outlier via the combination of two or more variable scores. Even for normal distributions, a point can be a multivariate outlier even if it is not a univariate outlier for any variable (consider a probability density concentrated along the line $x_{1}=x_{2}$ , for example), making Mahalanobis distance a more sensitive measure than checking dimensions individually.

Mahalanobis distance has also been used in ecological niche modelling, as the convex elliptical shape of the distances relates well to the concept of the fundamental niche.

Another example of usage is in finance, where Mahalanobis distance has been used to compute an indicator called the "turbulence index", which is a statistical measure of financial markets abnormal behaviour.

## Software implementations

Many programming languages and statistical packages, such as R, Python, etc., include implementations of Mahalanobis distance.

| Language/program | Function | Ref. |
|---|---|---|
| Julia | `mahalanobis(x, y, Q)` |   |
| MATLAB | `mahal(x, y)` |   |
| R | `mahalanobis(x, center, cov, inverted = FALSE, ...)` |   |
| SciPy (Python) | `mahalanobis(u, v, VI)` |   |
