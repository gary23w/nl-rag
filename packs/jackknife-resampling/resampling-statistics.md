---
title: "Resampling (statistics)"
source: https://en.wikipedia.org/wiki/Resampling_(statistics)
domain: jackknife-resampling
license: CC-BY-SA-4.0
tags: jackknife resampling, bias estimator, standard error, resampling method
fetched: 2026-07-02
---

# Resampling (statistics)

In statistics, **resampling** is the creation of new samples based on one observed sample. Resampling methods are:

1. Permutation tests (also re-randomization tests) for generating counterfactual samples
2. Bootstrapping
3. Cross validation
4. Jackknife

## Permutation tests

Permutation tests rely on resampling the original data assuming the null hypothesis. Based on the resampled data it can be concluded how likely the original data is to occur under the null hypothesis.

## Bootstrap

Bootstrapping is a statistical method for estimating the sampling distribution of an estimator by sampling with replacement from the original sample, most often with the purpose of deriving robust estimates of standard errors and confidence intervals of a population parameter like a mean, median, proportion, odds ratio, correlation coefficient or regression coefficient. It has been called the **plug-in principle**, as it is the method of estimation of functionals of a population distribution by evaluating the same functionals at the empirical distribution based on a sample.

For example, when estimating the population mean, this method uses the sample mean; to estimate the population median, it uses the sample median; to estimate the population regression line, it uses the sample regression line.

It may also be used for constructing hypothesis tests. It is often used as a robust alternative to inference based on parametric assumptions when those assumptions are in doubt, or where parametric inference is impossible or requires very complicated formulas for the calculation of standard errors. Bootstrapping techniques are also used in the updating-selection transitions of particle filters, genetic type algorithms and related resample/reconfiguration Monte Carlo methods used in computational physics. In this context, the bootstrap is used to replace sequentially empirical weighted probability measures by empirical measures. The bootstrap allows to replace the samples with low weights by copies of the samples with high weights.

## Cross-validation

Cross-validation is a statistical method for validating a predictive model. Subsets of the data are held out for use as validating sets; a model is fit to the remaining data (a training set) and used to predict for the validation set. Averaging the quality of the predictions across the validation sets yields an overall measure of prediction accuracy. Cross-validation is employed repeatedly in building decision trees.

One form of cross-validation leaves out a single observation at a time; this is similar to the jackknife. Another, *K*-fold cross-validation, splits the data into *K* subsets; each is held out in turn as the validation set.

This avoids "self-influence". For comparison, in regression analysis methods such as linear regression, each *y* value draws the regression line toward itself, making the prediction of that value appear more accurate than it really is. Cross-validation applied to linear regression predicts the *y* value for each observation without using that observation.

This is often used for deciding how many predictor variables to use in regression. Without cross-validation, adding predictors always reduces the residual sum of squares (or possibly leaves it unchanged). In contrast, the cross-validated mean-square error will tend to decrease if valuable predictors are added, but increase if worthless predictors are added.

### Monte Carlo cross-validation

Subsampling is an alternative method for approximating the sampling distribution of an estimator. The two key differences to the bootstrap are:

1. the resample size is smaller than the sample size and
2. resampling is done without replacement.

The advantage of subsampling is that it is valid under much weaker conditions compared to the bootstrap. In particular, a set of sufficient conditions is that the rate of convergence of the estimator is known and that the limiting distribution is continuous. In addition, the resample (or subsample) size must tend to infinity together with the sample size but at a smaller rate, so that their ratio converges to zero. While subsampling was originally proposed for the case of independent and identically distributed (iid) data only, the methodology has been extended to cover time series data as well; in this case, one resamples blocks of subsequent data rather than individual data points. There are many cases of applied interest where subsampling leads to valid inference whereas bootstrapping does not; for example, such cases include examples where the rate of convergence of the estimator is not the square root of the sample size or when the limiting distribution is non-normal. When both subsampling and the bootstrap are consistent, the bootstrap is typically more accurate. RANSAC is a popular algorithm using subsampling.

### Jackknife cross-validation

Jackknifing (jackknife cross-validation), is used in statistical inference to estimate the bias and standard error (variance) of a statistic, when a random sample of observations is used to calculate it. Historically, this method preceded the invention of the bootstrap with Quenouille inventing this method in 1949 and Tukey extending it in 1958. This method was foreshadowed by Mahalanobis who in 1946 suggested repeated estimates of the statistic of interest with half the sample chosen at random. He coined the name 'interpenetrating samples' for this method.

Quenouille invented this method with the intention of reducing the bias of the sample estimate. Tukey extended this method by assuming that if the replicates could be considered identically and independently distributed, then an estimate of the variance of the sample parameter could be made and that it would be approximately distributed as a t variate with *n*−1 degrees of freedom (*n* being the sample size).

The basic idea behind the jackknife variance estimator lies in systematically recomputing the statistic estimate, leaving out one or more observations at a time from the sample set. From this new set of replicates of the statistic, an estimate for the bias and an estimate for the variance of the statistic can be calculated. Jackknife is equivalent to the random (subsampling) leave-one-out cross-validation, it only differs in the goal.

For many statistical parameters the jackknife estimate of variance tends asymptotically to the true value almost surely. In technical terms one says that the jackknife estimate is consistent. The jackknife is consistent for the sample means, sample variances, central and non-central t-statistics (with possibly non-normal populations), sample coefficient of variation, maximum likelihood estimators, least squares estimators, correlation coefficients and regression coefficients.

It is not consistent for the sample median. In the case of a unimodal variate the ratio of the jackknife variance to the sample variance tends to be distributed as one half the square of a chi square distribution with two degrees of freedom.

Instead of using the jackknife to estimate the variance, it may instead be applied to the log of the variance. This transformation may result in better estimates particularly when the distribution of the variance itself may be non normal.

The jackknife, like the original bootstrap, is dependent on the independence of the data. Extensions of the jackknife to allow for dependence in the data have been proposed. One such extension is the delete-a-group method used in association with Poisson sampling.

#### Comparison of bootstrap and jackknife

Both methods, the bootstrap and the jackknife, estimate the variability of a statistic from the variability of that statistic between subsamples, rather than from parametric assumptions. For the more general jackknife, the delete-m observations jackknife, the bootstrap can be seen as a random approximation of it. Both yield similar numerical results, which is why each can be seen as approximation to the other. Although there are huge theoretical differences in their mathematical insights, the main practical difference for statistics users is that the bootstrap gives different results when repeated on the same data, whereas the jackknife gives exactly the same result each time. Because of this, the jackknife is popular when the estimates need to be verified several times before publishing (e.g., official statistics agencies). On the other hand, when this verification feature is not crucial and it is of interest not to have a number but just an idea of its distribution, the bootstrap is preferred (e.g., studies in physics, economics, biological sciences).

Whether to use the bootstrap or the jackknife may depend more on operational aspects than on statistical concerns of a survey. The jackknife, originally used for bias reduction, is more of a specialized method and only estimates the variance of the point estimator. This can be enough for basic statistical inference (e.g., hypothesis testing, confidence intervals). The bootstrap, on the other hand, first estimates the whole distribution (of the point estimator) and then computes the variance from that. While powerful and easy, this can become highly computationally intensive.

"The bootstrap can be applied to both variance and distribution estimation problems. However, the bootstrap variance estimator is not as good as the jackknife or the balanced repeated replication (BRR) variance estimator in terms of the empirical results. Furthermore, the bootstrap variance estimator usually requires more computations than the jackknife or the BRR. Thus, the bootstrap is mainly recommended for distribution estimation."

There is a special consideration with the jackknife, particularly with the delete-1 observation jackknife. It should only be used with smooth, differentiable statistics (e.g., totals, means, proportions, ratios, odd ratios, regression coefficients, etc.; not with medians or quantiles). This could become a practical disadvantage. This disadvantage is usually the argument favoring bootstrapping over jackknifing. More general jackknifes than the delete-1, such as the delete-m jackknife or the delete-all-but-2 Hodges–Lehmann estimator, overcome this problem for the medians and quantiles by relaxing the smoothness requirements for consistent variance estimation.

Usually the jackknife is easier to apply to complex sampling schemes than the bootstrap. Complex sampling schemes may involve stratification, multiple stages (clustering), varying sampling weights (non-response adjustments, calibration, post-stratification) and under unequal-probability sampling designs. Theoretical aspects of both the bootstrap and the jackknife can be found in Shao and Tu (1995), whereas a basic introduction is accounted in Wolter (2007). The bootstrap estimate of model prediction bias is more precise than jackknife estimates with linear models such as linear discriminant function or multiple regression.
