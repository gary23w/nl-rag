---
title: "Bias of an estimator"
source: https://en.wikipedia.org/wiki/Bias_of_an_estimator
domain: jackknife-resampling
license: CC-BY-SA-4.0
tags: jackknife resampling, bias estimator, standard error, resampling method
fetched: 2026-07-02
---

# Bias of an estimator

In statistics, the **bias of an estimator** (or **bias function**) is the difference between this estimator's expected value and the true value of the parameter being estimated. An estimator or decision rule with zero bias is called ***unbiased***. In statistics, "bias" is an *objective* property of an estimator. Bias is a distinct concept from consistency: consistent estimators converge in probability to the true value of the parameter, but may be biased or unbiased (see bias versus consistency for more).

All else being equal, an unbiased estimator is preferable to a biased estimator, although in practice, biased estimators (with generally small bias) are frequently used. When a biased estimator is used, bounds of the bias are calculated. A biased estimator may be used for various reasons: because an unbiased estimator does not exist without further assumptions about a population; because an estimator is difficult to compute (as in unbiased estimation of standard deviation); because a biased estimator may be unbiased with respect to different measures of central tendency; because a biased estimator gives a lower value of some loss function (particularly mean squared error) compared with unbiased estimators (notably in shrinkage estimators); or because in some cases being unbiased is too strong a condition, and the only unbiased estimators are not useful.

Bias can also be measured with respect to the median, rather than the mean (expected value), in which case one distinguishes *median*-unbiased from the usual *mean*-unbiasedness property. Mean-unbiasedness is not preserved under non-linear transformations, though median-unbiasedness is (see § Effect of transformations); for example, the sample variance is a biased estimator for the population variance. These are all illustrated below.

An unbiased estimator for a parameter need not always exist. For example, there is no unbiased estimator for the reciprocal of the parameter of a binomial random variable.

## Definition

Suppose we have a statistical model, parameterized by a real number *θ*, giving rise to a probability distribution for observed data, $P_{\theta }(x)=P(x\mid \theta )$ , and a statistic ${\hat {\theta }}$ which serves as an estimator of *θ* based on any observed data x . That is, we assume that our data follows some unknown distribution $P(x\mid \theta )$ (where *θ* is a fixed, unknown constant that is part of this distribution), and then we construct some estimator ${\hat {\theta }}$ that maps observed data to values that we hope are close to *θ*. The **bias** of ${\hat {\theta }}$ relative to $\theta$ is defined as $\operatorname {Bias} ({\hat {\theta }},\theta )=\operatorname {Bias} _{\theta }\left[\,{\hat {\theta }}\,\right]=\operatorname {E} _{x\mid \theta }\left[\,{\hat {\theta }}\,\right]-\theta =\operatorname {E} _{x\mid \theta }\left[{\hat {\theta }}-\theta \right],$

where $\operatorname {E} _{x\mid \theta }$ denotes expected value over the distribution $P(x\mid \theta )$ (i.e., averaging over all possible observations x ). The second equation follows since *θ* is measurable with respect to the conditional distribution $P(x\mid \theta )$ .

An estimator is said to be **unbiased** if its bias is zero for all values of the parameter *θ*, or equivalently, if the expected value of the estimator matches that of the parameter. Unbiasedness is not guaranteed to carry over. For example, if ${\hat {\theta }}$ is an unbiased estimator for parameter *θ*, it is not guaranteed in general that g( ${\hat {\theta }}$ ) is an unbiased estimator for *g(θ)*, unless *g* is a linear function.

In a simulation experiment concerning the properties of an estimator, the bias of the estimator may be assessed using the mean signed difference.

## Examples

### Sample variance

The sample variance highlights two different issues about bias and risk. First, the “naive” estimator that divides by *n* is biased downward because the sample mean is estimated from the same data. Multiplying by *n/(n−1)* (Bessel’s correction) yields an unbiased estimator. Second, unbiasedness does not imply minimum mean squared error.

Suppose *X*1, ..., *X**n* are independent and identically distributed (i.i.d.) random variables with expectation *μ* and variance *σ*2. If the sample mean and uncorrected sample variance are defined as

${\overline {X}}\,={\frac {1}{n}}\sum _{i=1}^{n}X_{i}\qquad S^{2}={\frac {1}{n}}\sum _{i=1}^{n}\left(X_{i}-{\overline {X}}\right)^{2}\qquad$

then *S*2 is a biased estimator of *σ*2. This follows immediately from the law of total variance because

$\underbrace {\operatorname {Var} (X)} _{\sigma ^{2}}=\underbrace {\operatorname {E} \left[\operatorname {Var} \left(X\mid {\bar {X}}\right)\right]} _{E[S^{2}]}+\underbrace {\operatorname {Var} \left(\operatorname {E} \left[X\mid {\bar {X}}\right]\right)} _{\sigma ^{2}/n},\quad \implies E[S^{2}]={\frac {n-1}{n}}\sigma ^{2}.$

In other words, the expected value of the uncorrected sample variance does not equal the population variance *σ*2, unless multiplied by a normalization factor. The ratio between the biased (uncorrected) and unbiased estimates of the variance is known as Bessel's correction. The sample mean, on the other hand, is an unbiased estimator of the population mean *μ*. The equality of the second term on the right-hand side in the equation above can be understood in terms of Bienaymé's identity,

${\begin{aligned}\operatorname {Var} \left(\operatorname {E} [X\mid {\bar {X}}]\right)&=\operatorname {Var} \left({\overline {X}}\right)=\operatorname {Var} \left({\frac {1}{n}}\sum _{i=1}^{n}X_{i}\right)\\[1ex]&={\frac {1}{n^{2}}}\sum _{i=1}^{n}\operatorname {Var} \left(X_{i}\right)={\frac {1}{n^{2}}}n\sigma ^{2}={\frac {\sigma ^{2}}{n}}.\end{aligned}}$

The reason that an uncorrected sample variance, *S*2, is biased stems from the fact that the sample mean is an ordinary least squares (OLS) estimator for *μ*: ${\overline {X}}$ is the number that makes the sum ${\textstyle \sum _{i=1}^{n}(X_{i}-{\overline {X}})^{2}}$ as small as possible. That is, when any other number is plugged into this sum, the sum can only increase. In particular, the choice $\mu \neq {\overline {X}}$ gives,

${\frac {1}{n}}\sum _{i=1}^{n}(X_{i}-{\overline {X}})^{2}<{\frac {1}{n}}\sum _{i=1}^{n}(X_{i}-\mu )^{2},$ and then ${\begin{aligned}\operatorname {E} [S^{2}]&=\operatorname {E} {\bigg [}{\frac {1}{n}}\sum _{i=1}^{n}(X_{i}-{\overline {X}})^{2}{\bigg ]}<\operatorname {E} {\bigg [}{\frac {1}{n}}\sum _{i=1}^{n}(X_{i}-\mu )^{2}{\bigg ]}=\sigma ^{2}.\end{aligned}}$

The above discussion can be understood in geometric terms: the vector ${\vec {C}}=(X_{1}-\mu ,\ldots ,X_{n}-\mu )$ can be decomposed into the "mean part" and "variance part" by projecting to the direction of ${\vec {u}}=(1,\ldots ,1)$ and to that direction's orthogonal complement hyperplane. One gets ${\vec {A}}=({\overline {X}}-\mu ,\ldots ,{\overline {X}}-\mu )$ for the part along ${\vec {u}}$ and ${\vec {B}}=(X_{1}-{\overline {X}},\ldots ,X_{n}-{\overline {X}})$ for the complementary part. Since this is an orthogonal decomposition, Pythagorean theorem says $|{\vec {C}}|^{2}=|{\vec {A}}|^{2}+|{\vec {B}}|^{2}$ , and taking expectations we get $n\sigma ^{2}=n\operatorname {E} \left[({\overline {X}}-\mu )^{2}\right]+n\operatorname {E} [S^{2}]$ , as above (but times n ). If the distribution of ${\vec {C}}$ is rotationally symmetric, as in the case when $X_{i}$ are sampled from a Gaussian, then on average, the dimension along ${\vec {u}}$ contributes to $|{\vec {C}}|^{2}$ equally as the $n-1$ directions perpendicular to ${\vec {u}}$ , so that $\operatorname {E} \left[({\overline {X}}-\mu )^{2}\right]={\frac {\sigma ^{2}}{n}}$ and $\operatorname {E} [S^{2}]={\frac {n-1}{n}}\sigma ^{2}$ . This is in fact true in general, as explained above.

### Estimating a Poisson probability

A far more extreme case of a biased estimator being better than any unbiased estimator arises from the Poisson distribution. Suppose that *X* has a Poisson distribution with expectation *λ*. Suppose it is desired to estimate $\operatorname {P} (X=0)^{2}=e^{-2\lambda }\quad$

with a sample of size 1. (For example, when incoming calls at a telephone switchboard are modeled as a Poisson process, and *λ* is the average number of calls per minute, then *e*−2*λ* (the estimand) is the probability that no calls arrive in the next two minutes.)

Since the expectation of an unbiased estimator *δ*(*X*) is equal to the estimand, i.e. $\operatorname {E} (\delta (X))=\sum _{x=0}^{\infty }\delta (x){\frac {\lambda ^{x}e^{-\lambda }}{x!}}=e^{-2\lambda },$

the only function of the data constituting an unbiased estimator is $\delta (x)=(-1)^{x}.\,$

To see this, note that when decomposing e−*λ* from the above expression for expectation, the sum that is left is a Taylor series expansion of e−*λ* as well, yielding e−*λ*e−*λ* = e−2*λ* (see Characterizations of the exponential function).

If the observed value of *X* is 100, then the estimate is 1, although the true value of the quantity being estimated is very likely to be near 0, which is the opposite extreme. And, if *X* is observed to be 101, then the estimate is even more absurd: It is −1, although the quantity being estimated must be positive.

The (biased) maximum likelihood estimator $e^{-2{X}}\quad$

is far better than this unbiased estimator. Not only is its value always positive but it is also more accurate in the sense that its mean squared error $e^{-4\lambda }-2e^{\lambda (1/e^{2}-3)}+e^{\lambda (1/e^{4}-1)}\,$

is smaller; compare the unbiased estimator's MSE of $1-e^{-4\lambda }.\,$

The MSEs are functions of the true value *λ*. The bias of the maximum-likelihood estimator is: $e^{\lambda (1/e^{2}-1)}-e^{-2\lambda }.\,$

### Maximum of a discrete uniform distribution

The bias of maximum-likelihood estimators can be substantial. Consider a case where *n* tickets numbered from 1 to *n* are placed in a box and one is selected at random, giving a value *X*. If *n* is unknown, then the maximum-likelihood estimator of *n* is *X*, even though the expectation of *X* given *n* is only (*n* + 1)/2; we can be certain only that *n* is at least *X* and is probably more. In this case, the natural unbiased estimator is 2*X* − 1.

## Median-unbiased estimators

The theory of median-unbiased estimators was revived by George W. Brown in 1947:

> An estimate of a one-dimensional parameter θ will be said to be median-unbiased, if, for fixed θ, the median of the distribution of the estimate is at the value θ; i.e., the estimate underestimates just as often as it overestimates. This requirement seems for most purposes to accomplish as much as the mean-unbiased requirement and has the additional property that it is invariant under one-to-one transformation.

Further properties of median-unbiased estimators have been noted by Lehmann, Birnbaum, van der Vaart and Pfanzagl. In particular, median-unbiased estimators exist in cases where mean-unbiased and maximum-likelihood estimators do not exist. They are invariant under one-to-one transformations.

There are methods of construction median-unbiased estimators for probability distributions that have monotone likelihood-functions, such as one-parameter exponential families, to ensure that they are optimal (in a sense analogous to minimum-variance property considered for mean-unbiased estimators). One such procedure is an analogue of the Rao–Blackwell procedure for mean-unbiased estimators: The procedure holds for a smaller class of probability distributions than does the Rao–Blackwell procedure for mean-unbiased estimation but for a larger class of loss-functions.

## Bias with respect to other loss functions

Any minimum-variance *mean*-unbiased estimator minimizes the risk (expected loss) with respect to the squared-error loss function (among mean-unbiased estimators), as observed by Gauss. A minimum-average absolute deviation *median*-unbiased estimator minimizes the risk with respect to the absolute loss function (among median-unbiased estimators), as observed by Laplace. Other loss functions are used in statistics, particularly in robust statistics.

## Effect of transformations

For univariate parameters, median-unbiased estimators remain median-unbiased under transformations that preserve order (or reverse order). Note that, when a transformation is applied to a mean-unbiased estimator, the result need not be a mean-unbiased estimator of its corresponding population statistic. By Jensen's inequality, a convex function as transformation will introduce positive bias, while a concave function will introduce negative bias, and a function of mixed convexity may introduce bias in either direction, depending on the specific function and distribution. That is, for a non-linear function *f* and a mean-unbiased estimator *U* of a parameter *p*, the composite estimator *f*(*U*) need not be a mean-unbiased estimator of *f*(*p*). For example, the square root of the unbiased estimator of the population variance is *not* a mean-unbiased estimator of the population standard deviation: the square root of the unbiased sample variance, the corrected sample standard deviation, is biased. The bias depends both on the sampling distribution of the estimator and on the transform, and can be quite involved to calculate – see unbiased estimation of standard deviation for a discussion in this case.

## Bias, variance and mean squared error

While bias quantifies the *average* difference to be expected between an estimator and an underlying parameter, an estimator based on a finite sample can additionally be expected to differ from the parameter due to the randomness in the sample. An estimator that minimises the bias will not necessarily minimise the mean square error. One measure which is used to try to reflect both types of difference is the mean square error, $\operatorname {MSE} ({\hat {\theta }})=\operatorname {E} {\big [}({\hat {\theta }}-\theta )^{2}{\big ]}.$ This can be shown to be equal to the square of the bias, plus the variance: ${\begin{aligned}\operatorname {MSE} ({\hat {\theta }})=&(\operatorname {E} [{\hat {\theta }}]-\theta )^{2}+\operatorname {E} [\,({\hat {\theta }}-\operatorname {E} [\,{\hat {\theta }}\,])^{2}\,]\\=&(\operatorname {Bias} ({\hat {\theta }},\theta ))^{2}+\operatorname {Var} ({\hat {\theta }})\end{aligned}}$

When the parameter is a vector, an analogous decomposition applies: $\operatorname {MSE} ({\hat {\theta }})=\operatorname {trace} (\operatorname {Cov} ({\hat {\theta }}))+\left\Vert \operatorname {Bias} ({\hat {\theta }},\theta )\right\Vert ^{2}$ where $\operatorname {trace} (\operatorname {Cov} ({\hat {\theta }}))$ is the trace (diagonal sum) of the covariance matrix of the estimator and $\left\Vert \operatorname {Bias} ({\hat {\theta }},\theta )\right\Vert ^{2}$ is the square vector norm.

### Example: Estimation of population variance

For example, suppose an estimator of the form

$T^{2}=c\sum _{i=1}^{n}\left(X_{i}-{\overline {X}}\,\right)^{2}=cnS^{2}$

is sought for the population variance as above, but this time to minimise the MSE:

${\begin{aligned}\operatorname {MSE} =&\operatorname {E} \left[(T^{2}-\sigma ^{2})^{2}\right]\\=&\left(\operatorname {E} \left[T^{2}-\sigma ^{2}\right]\right)^{2}+\operatorname {Var} (T^{2})\end{aligned}}$

If the variables *X*1 ... *X**n* follow a normal distribution, then *nS*2/σ2 has a chi-squared distribution with *n* − 1 degrees of freedom, giving:

$\operatorname {E} [nS^{2}]=(n-1)\sigma ^{2}{\text{ and }}\operatorname {Var} (nS^{2})=2(n-1)\sigma ^{4}.$

and so

$\operatorname {MSE} =(c(n-1)-1)^{2}\sigma ^{4}+2c^{2}(n-1)\sigma ^{4}$

With a little algebra it can be confirmed that it is *c* = 1/(*n* + 1) which minimises this combined loss function, rather than *c* = 1/(*n* − 1) which minimises just the square of the bias.

More generally it is only in restricted classes of problems that there will be an estimator that minimises the MSE independently of the parameter values.

However it is very common that there may be perceived to be a *bias–variance tradeoff*, such that a small increase in bias can be traded for a larger decrease in variance, resulting in a more desirable estimator overall.

## Bayesian view

Most bayesians are rather unconcerned about unbiasedness (at least in the formal sampling-theory sense above) of their estimates. For example, Gelman and coauthors (1995) write: "From a Bayesian perspective, the principle of unbiasedness is reasonable in the limit of large samples, but otherwise it is potentially misleading."

Fundamentally, the difference between the Bayesian approach and the sampling-theory approach above is that in the sampling-theory approach the parameter is taken as fixed, and then probability distributions of a statistic are considered, based on the predicted sampling distribution of the data. For a Bayesian, however, it is the *data* which are known, and fixed, and it is the unknown parameter for which an attempt is made to construct a probability distribution, using Bayes' theorem:

$p(\theta \mid D,I)\propto p(\theta \mid I)p(D\mid \theta ,I)$

Here the second term, the likelihood of the data given the unknown parameter value θ, depends just on the data obtained and the modelling of the data generation process. However a Bayesian calculation also includes the first term, the prior probability for θ, which takes account of everything the analyst may know or suspect about θ *before* the data comes in. This information plays no part in the sampling-theory approach; indeed any attempt to include it would be considered "bias" away from what was pointed to purely by the data. To the extent that Bayesian calculations include prior information, it is therefore essentially inevitable that their results will not be "unbiased" in sampling theory terms.

But the results of a Bayesian approach can differ from the sampling theory approach even if the Bayesian tries to adopt an "uninformative" prior.

For example, consider again the estimation of an unknown population variance σ2 of a Normal distribution with unknown mean, where it is desired to optimise *c* in the expected loss function

$\operatorname {ExpectedLoss} =\operatorname {E} \left[\left(cnS^{2}-\sigma ^{2}\right)^{2}\right]=\operatorname {E} \left[\sigma ^{4}\left(cn{\tfrac {S^{2}}{\sigma ^{2}}}-1\right)^{2}\right]$

A standard choice of uninformative prior for this problem is the Jeffreys prior, $\scriptstyle {p(\sigma ^{2})\;\propto \;1/\sigma ^{2}}$ , which is equivalent to adopting a rescaling-invariant flat prior for **ln(σ2)**.

One consequence of adopting this prior is that *S*2/σ2 remains a pivotal quantity, i.e. the probability distribution of *S*2/σ2 depends only on *S*2/σ2, independent of the value of *S*2 or σ2:

$p\left({\tfrac {S^{2}}{\sigma ^{2}}}\mid S^{2}\right)=p\left({\tfrac {S^{2}}{\sigma ^{2}}}\mid \sigma ^{2}\right)=g\left({\tfrac {S^{2}}{\sigma ^{2}}}\right)$

However, while

$\operatorname {E} _{p(S^{2}\mid \sigma ^{2})}\left[\sigma ^{4}\left(cn{\tfrac {S^{2}}{\sigma ^{2}}}-1\right)^{2}\right]=\sigma ^{4}\operatorname {E} _{p(S^{2}\mid \sigma ^{2})}\left[\left(cn{\tfrac {S^{2}}{\sigma ^{2}}}-1\right)^{2}\right]$

in contrast

$\operatorname {E} _{p(\sigma ^{2}\mid S^{2})}\left[\sigma ^{4}\left(cn{\tfrac {S^{2}}{\sigma ^{2}}}-1\right)^{2}\right]\neq \sigma ^{4}\operatorname {E} _{p(\sigma ^{2}\mid S^{2})}\left[\left(cn{\tfrac {S^{2}}{\sigma ^{2}}}-1\right)^{2}\right]$

— when the expectation is taken over the probability distribution of σ2 given *S*2, as it is in the Bayesian case, rather than *S*2 given σ2, one can no longer take σ4 as a constant and factor it out. The consequence of this is that, compared to the sampling-theory calculation, the Bayesian calculation puts more weight on larger values of σ2, properly taking into account (as the sampling-theory calculation cannot) that under this squared-loss function the consequence of underestimating large values of σ2 is more costly in squared-loss terms than that of overestimating small values of σ2.

The worked-out Bayesian calculation gives a scaled inverse chi-squared distribution with *n* − 1 degrees of freedom for the posterior probability distribution of σ2. The expected loss is minimised when *cnS*2 = <σ2>; this occurs when *c* = 1/(*n* − 3).

Even with an uninformative prior, therefore, a Bayesian calculation may not give the same expected-loss minimising result as the corresponding sampling-theory calculation.
