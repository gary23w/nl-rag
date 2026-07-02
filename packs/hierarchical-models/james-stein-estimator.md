---
title: "James–Stein estimator"
source: https://en.wikipedia.org/wiki/James–Stein_estimator
domain: hierarchical-models
license: CC-BY-SA-4.0
tags: multilevel model, hierarchical modeling, shrinkage estimator, hyperparameter prior
fetched: 2026-07-02
---

# James–Stein estimator

The **James–Stein estimator** is an estimator of the mean ${\boldsymbol {\theta }}:=(\theta _{1},\theta _{2},\dots \theta _{m})$ for a multivariate random variable ${\boldsymbol {Y}}:=(Y_{1},Y_{2},\dots Y_{m})$ .

It arose sequentially in two main published papers. The earlier version of the estimator was developed in 1956, when Charles Stein reached a relatively shocking conclusion that while the then-usual estimate of the mean, the sample mean, is admissible when $m\leq 2$ , it is inadmissible when $m\geq 3$ . Stein proposed a possible improvement to the estimator that shrinks the sample mean ${\boldsymbol {\theta }}$ towards a more central mean vector ${\boldsymbol {\nu }}$ (which can be chosen a priori or commonly as the "average of averages" of the sample means, given all samples share the same size). This observation is commonly referred to as Stein's example or paradox. In 1961, Willard James and Charles Stein simplified the original process.

It can be shown that the James–Stein estimator dominates the "ordinary" least squares approach in the sense that the James–Stein estimator has a lower mean squared error than the "ordinary" least squares estimator for all ${\boldsymbol {\theta }}$ . This is possible because the James–Stein estimator is biased, so that the Gauss–Markov theorem does not apply.

Similar to the Hodges' estimator, the James-Stein estimator is superefficient and non-regular at ${\boldsymbol {\theta }}=\mathbf {0}$ .

## Setting

Let ${\mathbf {Y} }\sim N_{m}({\boldsymbol {\theta }},\sigma ^{2}I),\,$ where the vector ${\boldsymbol {\theta }}$ is the unknown mean of ${\mathbf {Y} }$ , which is m -variate normally distributed and with known covariance matrix $\sigma ^{2}I$ .

We are interested in obtaining an estimate, ${\widehat {\boldsymbol {\theta }}}$ , of ${\boldsymbol {\theta }}$ , based on a single observation, ${\mathbf {y} }$ , of ${\mathbf {Y} }$ .

In real-world application, this is a common situation in which a set of parameters is sampled, and the samples are corrupted by independent Gaussian noise. Since this noise has mean of zero, it may be reasonable to use the samples themselves as an estimate of the parameters. This approach is the least squares estimator, which is ${\widehat {\boldsymbol {\theta }}}_{LS}={\mathbf {Y} }$ .

Stein demonstrated that in terms of mean squared error $\operatorname {E} \left[\left\|{\boldsymbol {\theta }}-{\widehat {\boldsymbol {\theta }}}\right\|^{2}\right]$ , the least squares estimator, ${\widehat {\boldsymbol {\theta }}}_{LS}$ , is sub-optimal to shrinkage based estimators, such as the **James–Stein estimator**, ${\widehat {\boldsymbol {\theta }}}_{JS}$ . The paradoxical result, that there is a (possibly) better and never any worse estimate of ${\boldsymbol {\theta }}$ in mean squared error as compared to the sample mean, became known as Stein's example.

## Formulation

If $\sigma ^{2}$ is known, the James–Stein estimator is given by

${\widehat {\boldsymbol {\theta }}}_{JS}=\left(1-{\frac {(m-2)\sigma ^{2}}{\|{\mathbf {Y} }\|^{2}}}\right){\mathbf {Y} }.$

James and Stein showed that the above estimator dominates ${\widehat {\boldsymbol {\theta }}}_{LS}$ for any $m\geq 3$ , meaning that the James–Stein estimator has a lower mean squared error (MSE) than the maximum likelihood estimator. By definition, this makes the least squares estimator inadmissible when $m\geq 3$ .

Notice that if $(m-2)\sigma ^{2}<\|{\mathbf {Y} }\|^{2}$ then this estimator simply takes the natural estimator $\mathbf {Y}$ and shrinks it towards the origin **0**. In fact this is not the only direction of shrinkage that works. Let ${\boldsymbol {\nu }}$ be an arbitrary fixed vector of dimension m . Then there exists an estimator of the James–Stein type that shrinks toward ${\boldsymbol {\nu }}$ , namely

${\widehat {\boldsymbol {\theta }}}_{JS}=\left(1-{\frac {(m-2)\sigma ^{2}}{\|{\mathbf {Y} }-{\boldsymbol {\nu }}\|^{2}}}\right)({\mathbf {Y} }-{\boldsymbol {\nu }})+{\boldsymbol {\nu }},\qquad m\geq 3.$

The James–Stein estimator dominates the usual estimator for any ${\boldsymbol {\nu }}$ . A natural question to ask is whether the improvement over the usual estimator is independent of the choice of ${\boldsymbol {\nu }}$ . The answer is no. The improvement is small if $\|{{\boldsymbol {\theta }}-{\boldsymbol {\nu }}}\|$ is large. Thus to get a very great improvement some knowledge of the location of ${\boldsymbol {\theta }}$ is necessary. Of course this is the quantity we are trying to estimate so we don't have this knowledge a priori. But we may have some guess as to what the mean vector is. This can be considered a disadvantage of the estimator: the choice is not objective as it may depend on the beliefs of the researcher. Nonetheless, James and Stein's result is that *any* finite guess ${\boldsymbol {\nu }}$ improves the expected MSE over the maximum-likelihood estimator, which is tantamount to using an infinite ${\boldsymbol {\nu }}$ , surely a poor guess.

## Interpretation

Seeing the James–Stein estimator as an empirical Bayes method gives some intuition to this result: One assumes that ${\boldsymbol {\theta }}$ itself is a random variable with prior distribution $\sim N(0,A)$ , where A is estimated from the data itself. Estimating A only gives an advantage compared to the maximum-likelihood estimator when the dimension m is large enough; hence it does not work for $m\leq 2$ . The James–Stein estimator is a member of a class of Bayesian estimators that dominate the maximum-likelihood estimator.

A consequence of the above discussion is the following counterintuitive result: When three or more unrelated parameters are measured, their total MSE can be reduced by using a combined estimator such as the James–Stein estimator; whereas when each parameter is estimated separately, the least squares (LS) estimator is admissible. A quirky example would be estimating the speed of light, tea consumption in Taiwan, and hog weight in Montana, all together. The James–Stein estimator always improves upon the *total* MSE, i.e., the sum of the expected squared errors of each component. Therefore, the total MSE in measuring light speed, tea consumption, and hog weight would improve by using the James–Stein estimator. However, any particular component (such as the speed of light) would improve for some parameter values, and deteriorate for others. Thus, although the James–Stein estimator dominates the LS estimator when three or more parameters are estimated, any single component does not dominate the respective component of the LS estimator.

The conclusion from this hypothetical example is that measurements should be combined if one is interested in minimizing their total MSE. For example, in a telecommunication setting, it is reasonable to combine channel tap measurements in a channel estimation scenario, as the goal is to minimize the total channel estimation error.

The James–Stein estimator has also found use in fundamental quantum theory, where the estimator has been used to improve the theoretical bounds of the entropic uncertainty principle for more than three measurements.

An intuitive derivation and interpretation is given by the Galtonian perspective. Under this interpretation, we aim to predict the population means using the imperfectly measured sample means. The equation of the OLS estimator in a hypothetical regression of the population means on the sample means gives an estimator of the form of either the James–Stein estimator (when we force the OLS intercept to equal 0) or of the Efron-Morris estimator (when we allow the intercept to vary).

## Positive-part James–Stein shrinkage operator

Despite the intuition that the James–Stein estimator shrinks the unbiased least-squares estimator ${\mathbf {Y} }$ *toward* ${\boldsymbol {\nu }}$ , the estimator actually moves *away* from ${\boldsymbol {\nu }}$ for small values of $\|{\mathbf {Y} }-{\boldsymbol {\nu }}\|,$ as the multiplier on ${\mathbf {Y} }-{\boldsymbol {\nu }}$ is then negative. This can be remedied by replacing this multiplier by zero when it is negative. To this end, define the *positive-part James-Stein shrinkage operator*:

$S_{\lambda }(x)=x\left[1-\left(\lambda /x\right)^{2}\right]_{+},$

where $x_{+}=\max\{0,x\}$ , and apply this operator component-wise to the (unbiased) least-squares estimator of ${\boldsymbol {\theta }}-{\boldsymbol {\nu }}$ (with known ${\boldsymbol {\nu }}$ ) for each $i=1,\ldots ,m$ :

${\widehat {\theta }}_{i}^{+}-\nu _{i}=S_{\lambda _{i}}(Y_{i}-\nu _{i}),\quad \lambda _{i}:=\sigma {\sqrt {m-2}}\,{\frac {|Y_{i}-\nu _{i}|}{\|\mathbf {Y} -{\boldsymbol {\nu }}\|}}.$

The resulting estimator ${\widehat {\boldsymbol {\theta }}}^{+}$ of ${\boldsymbol {\theta }}$ is called the *positive-part James–Stein estimator* and can be written in vector notation as:

${\widehat {\boldsymbol {\theta }}}^{+}-{\boldsymbol {\nu }}=\left(1-{\frac {(m-2)\sigma ^{2}}{\|{\mathbf {Y} }-{\boldsymbol {\nu }}\|^{2}}}\right)_{+}({\mathbf {Y} }-{\boldsymbol {\nu }}).$

This estimator has a smaller risk than the basic James–Stein estimator for $m\geq 4$ . It follows that the basic James–Stein estimator is itself inadmissible.

It turns out, however, that the positive-part estimator is also inadmissible. This follows from a more general result which requires admissible estimators to be smooth.

## Positive-part James–Stein shrinkage and model selection

Recall the initial setup:

${\mathbf {Y} }\sim N({\boldsymbol {\theta }},\sigma ^{2}I),\,$

where the variance coefficient $\sigma ^{2}$ is known and we wish to estimate the unknown (mean response) coefficient ${\boldsymbol {\theta }}=\mathbb {E} \mathbf {Y}$ . In the more general setting of linear regression, the mean response is instead given by

$\mathbb {E} \mathbf {Y} =\mathbf {X} {\boldsymbol {\theta }},$

where $\mathbf {X} =[\mathbf {v} _{1},\ldots ,\mathbf {v} _{m}]$ is a matrix with m columns. As in the previous section, we can use the *positive-part James-Stein shrinkage operator* to obtain a shrinkage estimator of ${\boldsymbol {\theta }}$ . In particular, any ${\widehat {\boldsymbol {\theta }}}$ that satisfies the *James-Stein KKT conditions*:

${\hat {\theta }}_{i}=S_{\frac {\sigma }{\|\mathbf {v} _{i}\|}}{\bigg (}{\hat {\theta }}_{i}+{\frac {\mathbf {v} _{i}^{\top }(\mathbf {Y} -\mathbf {X} {\widehat {\boldsymbol {\theta }}})}{\|\mathbf {v} _{i}\|^{2}}}{\bigg )},\quad i=1,\ldots ,m$

is a (positive-part) James-Stein estimator of ${\boldsymbol {\theta }}$ with the useful property that it performs both shrinkage and model selection simultaneously. This is because, depending on the value of the known $\sigma ^{2}$ , there is a (possibly empty) set ${\mathcal {S}}\subseteq \{1,\ldots ,m\}$ such that

${\hat {\theta }}_{i}=0,\quad i\in {\mathcal {S}}.$

In other words, some (or all) of the $\theta _{i}$ could be estimated as exactly zero, which is equivalent to the selection of a suitable linear regression model.

## Further extensions

The James–Stein estimator may seem at first sight to be a result of some peculiarity of the problem setting. In fact, the estimator exemplifies a very wide-ranging effect; namely, the fact that the "ordinary" or least squares estimator is often inadmissible for simultaneous estimation of several parameters. This effect has been called Stein's phenomenon, and has been demonstrated for several different problem settings, some of which are briefly outlined below.

- James and Stein demonstrated that the estimator presented above can still be used when the variance $\sigma ^{2}$ is unknown, by replacing it with the standard estimator of the variance, ${\widehat {\sigma }}^{2}={\frac {1}{m}}\sum (Y_{i}-{\overline {Y}})^{2}$ . The dominance result still holds under the same condition, namely, $m>2$ .
- All the results above are for the case when only a single observation vector **y** is available. For the more general case when n vectors are available, we consider the estimator ${\widehat {\boldsymbol {\theta }}}_{JS}=\left(1-{\frac {(m-2){\frac {\sigma ^{2}}{n}}}{\|{\overline {\mathbf {Y} }}\|^{2}}}\right){\overline {\mathbf {Y} }},$ where ${\overline {\mathbf {Y} }}$ is the m -length average of the n observations, so that, ${\overline {\mathbf {Y} }}\sim N_{m}{\Big (}{\boldsymbol {\theta }},{\frac {\sigma ^{2}}{n}}I{\Big )}$ .
- The work of James and Stein has been extended to the case of a general measurement covariance matrix, i.e., where measurements may be statistically dependent and may have differing variances. A similar dominating estimator can be constructed, with a suitably generalized dominance condition. This can be used to construct a linear regression technique which outperforms the standard application of the LS estimator.
- Stein's result has been extended to a wide class of distributions and loss functions. However, this theory provides only an existence result, in that explicit dominating estimators were not actually exhibited. It is quite difficult to obtain explicit estimators improving upon the usual estimator without specific restrictions on the underlying distributions.
