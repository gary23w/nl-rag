---
title: "Robust statistics"
source: https://en.wikipedia.org/wiki/Robust_statistics
domain: robust-regression
license: CC-BY-SA-4.0
tags: robust regression, M-estimator, robust statistics, influential observation
fetched: 2026-07-02
---

# Robust statistics

**Robust statistics** are statistics that maintain their properties even if the underlying distributional assumptions are incorrect. Robust statistical methods have been developed for many common problems, such as estimating location, scale, and regression parameters. One motivation is to produce statistical methods that are not unduly affected by outliers. Another motivation is to provide methods with good performance when there are small departures from a parametric distribution. For example, robust methods work well for mixtures of two normal distributions with different standard deviations; under this model, non-robust methods like a t-test work poorly.

## Introduction

Robust statistics seek to provide methods that emulate popular statistical methods, but are not unduly affected by outliers or other small departures from model assumptions. In statistics, classical estimation methods rely heavily on assumptions that are often not met in practice. In particular, it is often assumed that the data errors are normally distributed, at least approximately, or that the central limit theorem can be relied on to produce normally distributed estimates. Unfortunately, when there are outliers in the data, classical estimators often have very poor performance, when judged using the *breakdown point* and the *influence function* described below.

The practical effect of problems seen in the influence function can be studied empirically by examining the sampling distribution of proposed estimators under a mixture model, where one mixes in a small amount (1–5% is often sufficient) of contamination. For instance, one may use a mixture of 95% a normal distribution, and 5% a normal distribution with the same mean but significantly higher standard deviation (representing outliers).

Robust parametric statistics can proceed in two ways:

- by designing estimators so that a pre-selected behaviour of the influence function is achieved
- by replacing estimators that are optimal under the assumption of a normal distribution with estimators that are optimal for, or at least derived for, other distributions; for example, using the *t*-distribution with low degrees of freedom (high kurtosis) or with a mixture of two or more distributions.

Robust estimates have been studied for the following problems:

- estimating location parameters
- estimating scale parameters
- estimating regression coefficients
- estimation of model-states in models expressed in state-space form, for which the standard method is equivalent to a Kalman filter.

## Definition

There are various definitions of a "robust statistic". Strictly speaking, a **robust statistic** is resistant to errors in the results, produced by deviations from assumptions (e.g., of normality). This means that if the assumptions are only approximately met, the **robust estimator** will still have a reasonable efficiency, and reasonably small bias, as well as being asymptotically unbiased, meaning having a bias tending towards 0 as the sample size tends towards infinity.

Usually, the most important case is **distributional robustness** - robustness to breaking of the assumptions about the underlying distribution of the data. Classical statistical procedures are typically sensitive to "longtailedness" (e.g., when the distribution of the data has longer tails than the assumed normal distribution). This implies that they will be strongly affected by the presence of outliers in the data, and the estimates they produce may be heavily distorted if there are extreme outliers in the data, compared to what they would be if the outliers were not included in the data.

By contrast, more robust estimators that are not so sensitive to distributional distortions such as longtailedness are also resistant to the presence of outliers. Thus, in the context of robust statistics, *distributionally robust* and *outlier-resistant* are effectively synonymous. For one perspective on research in robust statistics up to 2000, see Portnoy & He (2000).

Some experts prefer the term **resistant statistics** for distributional robustness, and reserve 'robustness' for non-distributional robustness, e.g., robustness to violation of assumptions about the probability model or estimator, but this is a minority usage. Plain 'robustness' to mean 'distributional robustness' is common.

When considering how robust an estimator is to the presence of outliers, it is useful to test what happens when an extreme outlier is **added** to the dataset, and to test what happens when an extreme outlier **replaces** one of the existing data points, and then to consider the effect of multiple additions or replacements.

## Examples

The mean is not a robust measure of central tendency. If the dataset is, e.g., the values {2,3,5,6,9}, then if we add another datapoint with value -1000 or +1000 to the data, the resulting mean will be very different from the mean of the original data. Similarly, if we replace one of the values with a datapoint of value -1000 or +1000 then the resulting mean will be very different from the mean of the original data.

The median is a robust measure of central tendency. Taking the same dataset {2,3,5,6,9}, if we add another datapoint with value -1000 or +1000 then the median will change slightly, but it will still be similar to the median of the original data. If we replace one of the values with a data point of value -1000 or +1000 then the resulting median will still be similar to the median of the original data.

Described in terms of breakdown points, the median has a breakdown point of 50%, meaning that half the points must be outliers before the median can be moved outside the range of the non-outliers, while the mean has a breakdown point of 0, as a single large observation can throw it off.

The median absolute deviation and interquartile range are robust measures of statistical dispersion, while the standard deviation and range are not.

Trimmed estimators and Winsorised estimators are general methods to make statistics more robust. L-estimators are a general class of simple statistics, often robust, while M-estimators are a general class of robust statistics, and are now the preferred solution, though they can be quite involved to calculate.

### Speed-of-light data

Gelman et al. in Bayesian Data Analysis (2004) consider a data set relating to speed-of-light measurements made by Simon Newcomb. The data sets for that book can be found via the Classic data sets page, and the book's website contains more information on the data.

Although the bulk of the data looks to be more or less normally distributed, there are two obvious outliers. These outliers have a large effect on the mean, dragging it towards them, and away from the center of the bulk of the data. Thus, if the mean is intended as a measure of the location of the center of the data, it is, in a sense, biased when outliers are present.

Also, the distribution of the mean is known to be asymptotically normal due to the central limit theorem. However, outliers can make the distribution of the mean non-normal, even for fairly large data sets. Besides this non-normality, the mean is also inefficient in the presence of outliers and less variable measures of location are available.

### Estimation of location

The plot below shows a density plot of the speed-of-light data, together with a rug plot (panel (a)). Also shown is a normal Q–Q plot (panel (b)). The outliers are visible in these plots.

Panels (c) and (d) of the plot show the bootstrap distribution of the mean (c) and the 10% trimmed mean (d). The trimmed mean is a simple, robust estimator of location that deletes a certain percentage of observations (10% here) *from each end* of the data, then computes the mean in the usual way. The analysis was performed in R and 10,000 bootstrap samples were used for each of the raw and trimmed means.

The distribution of the mean is clearly much wider than that of the 10% trimmed mean (the plots are on the same scale). Also whereas the distribution of the trimmed mean appears to be close to normal, the distribution of the raw mean is quite skewed to the left. So, in this sample of 66 observations, only 2 outliers cause the central limit theorem to be inapplicable.

Robust statistical methods, of which the trimmed mean is a simple example, seek to outperform classical statistical methods in the presence of outliers, or, more generally, when underlying parametric assumptions are not quite correct.

Whilst the trimmed mean performs well relative to the mean in this example, better robust estimates are available. In fact, the mean, median and trimmed mean are all special cases of M-estimators. Details appear in the sections below.

### Estimation of scale

The outliers in the speed-of-light data have more than just an adverse effect on the mean; the usual estimate of scale is the standard deviation, and this quantity is even more badly affected by outliers because the squares of the deviations from the mean go into the calculation, so the outliers' effects are exacerbated.

The plots below show the bootstrap distributions of the standard deviation, the median absolute deviation (MAD) and the Rousseeuw–Croux (Qn) estimator of scale. The plots are based on 10,000 bootstrap samples for each estimator, with some Gaussian noise added to the resampled data (smoothed bootstrap). Panel (a) shows the distribution of the standard deviation, (b) of the MAD and (c) of Qn.

The distribution of standard deviation is erratic and wide, a result of the outliers. The MAD is better behaved, and Qn is a little bit more efficient than MAD. This simple example demonstrates that when outliers are present, the standard deviation cannot be recommended as an estimate of scale.

### Manual screening for outliers

Traditionally, statisticians would manually screen data for outliers, and remove them, usually checking the source of the data to see whether the outliers were erroneously recorded. Indeed, in the speed-of-light example above, it is easy to see and remove the two outliers prior to proceeding with any further analysis. However, in modern times, data sets often consist of large numbers of variables being measured on large numbers of experimental units. Therefore, manual screening for outliers is often impractical.

Outliers can often interact in such a way that they mask each other. As a simple example, consider a small univariate data set containing one modest and one large outlier. The estimated standard deviation will be grossly inflated by the large outlier. The result is that the modest outlier looks relatively normal. As soon as the large outlier is removed, the estimated standard deviation shrinks, and the modest outlier now looks unusual.

This problem of masking gets worse as the complexity of the data increases. For example, in regression problems, diagnostic plots are used to identify outliers. However, it is common that once a few outliers have been removed, others become visible. The problem is even worse in higher dimensions.

Robust methods provide automatic ways of detecting, downweighting (or removing), and flagging outliers, largely removing the need for manual screening. Care must be taken; initial data showing the ozone hole first appearing over Antarctica were rejected as outliers by non-human screening.

### Variety of applications

Although this article deals with general principles for univariate statistical methods, robust methods also exist for regression problems, generalized linear models, and parameter estimation of various distributions.

## Measures of robustness

The basic tools used to describe and measure robustness are the *breakdown point*, the *influence function* and the *sensitivity curve*.

### Breakdown point

Intuitively, the breakdown point of an estimator is the proportion of incorrect observations (e.g. arbitrarily large observations) an estimator can handle before giving an incorrect (e.g., arbitrarily large) result. Usually, the asymptotic (infinite sample) limit is quoted as the breakdown point, although the finite-sample breakdown point may be more useful. For example, given n independent random variables $(X_{1},\dots ,X_{n})$ and the corresponding realizations $x_{1},\dots ,x_{n}$ , we can use ${\overline {X_{n}}}:={\frac {X_{1}+\cdots +X_{n}}{n}}$ to estimate the mean. Such an estimator has a breakdown point of 0 (or finite-sample breakdown point of $1/n$ ) because we can make ${\overline {x}}$ arbitrarily large just by changing any of $x_{1},\dots ,x_{n}$ .

The higher the breakdown point of an estimator, the more robust it is. Intuitively, we can understand that a breakdown point cannot exceed 50% because if more than half of the observations are contaminated, it is not possible to distinguish between the underlying distribution and the contaminating distribution Rousseeuw & Leroy (1987). Therefore, the maximum breakdown point is 0.5 and there are estimators which achieve such a breakdown point. For example, the median has a breakdown point of 0.5. The X% trimmed mean has a breakdown point of X%, for the chosen level of X. Huber (1981) and Maronna et al. (2019) contain more details. The level and the power breakdown points of tests are investigated in He, Simpson & Portnoy (1990).

Statistics with high breakdown points are sometimes called **resistant statistics.**

#### Example: speed-of-light data

In the speed-of-light example, removing the two lowest observations causes the mean to change from 26.2 to 27.75, a change of 1.55. The estimate of scale produced by the Qn method is 6.3. We can divide this by the square root of the sample size to get a robust standard error, and we find this quantity to be 0.78. Thus, the change in the mean resulting from removing two outliers is approximately twice the robust standard error.

The 10% trimmed mean for the speed-of-light data is 27.43. Removing the two lowest observations and recomputing gives 27.67. The trimmed mean is less affected by the outliers and has a higher breakdown point.

If we replace the lowest observation, −44, by −1000, the mean becomes 11.73, whereas the 10% trimmed mean is still 27.43. In many areas of applied statistics, it is common for data to be log-transformed to make them near symmetrical. Very small values become large negative when log-transformed, and zeroes become negatively infinite. Therefore, this example is of practical interest.

### Empirical influence function

The empirical influence function is a measure of the dependence of the estimator on the value of any one of the points in the sample. It is a model-free measure in the sense that it simply relies on calculating the estimator again with a different sample. On the right is Tukey's biweight function, which, as we will later see, is an example of what a "good" (in a sense defined later on) empirical influence function should look like.

In mathematical terms, an influence function is defined as a vector in the space of the estimator, which is in turn defined for a sample which is a subset of the population:

1. $(\Omega ,{\mathcal {A}},P)$ is a probability space,
2. $({\mathcal {X}},\Sigma )$ is a measurable space (state space),
3. $\Theta$ is a parameter space of dimension $p\in \mathbb {N} ^{*}$ ,
4. $(\Gamma ,S)$ is a measurable space,

For example,

1. $(\Omega ,{\mathcal {A}},P)$ is any probability space,
2. $({\mathcal {X}},\Sigma )=(\mathbb {R} ,{\mathcal {B}})$ ,
3. $\Theta =\mathbb {R} \times \mathbb {R} ^{+}$
4. $(\Gamma ,S)=(\mathbb {R} ,{\mathcal {B}})$ ,

The empirical influence function is defined as follows.

Let $n\in \mathbb {N} ^{*}$ and $X_{1},\dots ,X_{n}:(\Omega ,{\mathcal {A}})\to ({\mathcal {X}},\Sigma )$ are i.i.d. and $(x_{1},\dots ,x_{n})$ is a sample from these variables. $T_{n}:({\mathcal {X}}^{n},\Sigma ^{n})\to (\Gamma ,S)$ is an estimator. Let $i\in \{1,\dots ,n\}$ . The empirical influence function $EIF_{i}$ at observation i is defined by:

$EIF_{i}:x\in {\mathcal {X}}\mapsto n\cdot (T_{n}(x_{1},\dots ,x_{i-1},x,x_{i+1},\dots ,x_{n})-T_{n}(x_{1},\dots ,x_{i-1},x_{i},x_{i+1},\dots ,x_{n}))$

What this means is that we are replacing the *i*-th value in the sample by an arbitrary value and looking at the output of the estimator. Alternatively, the EIF is defined as the effect, scaled by n+1 instead of n, on the estimator of adding the point x to the sample.

### Influence function and sensitivity curve

Instead of relying solely on the data, we could use the distribution of the random variables. The approach is quite different from that of the previous paragraph. What we are now trying to do is to see what happens to an estimator when we change the distribution of the data slightly: it assumes a *distribution,* and measures sensitivity to change in this distribution. By contrast, the empirical influence assumes a *sample set,* and measures sensitivity to change in the samples.

Let A be a convex subset of the set of all finite signed measures on $\Sigma$ . We want to estimate the parameter $\theta \in \Theta$ of a distribution F in A . Let the functional $T:A\to \Gamma$ be the asymptotic value of some estimator sequence $(T_{n})_{n\in \mathbb {N} }$ . We will suppose that this functional is Fisher consistent, i.e. $\forall \theta \in \Theta ,T(F_{\theta })=\theta$ . This means that at the model F , the estimator sequence asymptotically measures the correct quantity.

Let G be some distribution in A . What happens when the data doesn't follow the model F exactly but another, slightly different, "going towards" G ?

We're looking at: $dT_{G-F}(F)=\lim _{t\to 0^{+}}{\frac {T(tG+(1-t)F)-T(F)}{t}},$

which is the one-sided Gateaux derivative of T at F , in the direction of $G-F$ .

Let $x\in {\mathcal {X}}$ . $\Delta _{x}$ is the probability measure which gives mass 1 to $\{x\}$ . We choose $G=\Delta _{x}$ . The influence function is then defined by:

$IF(x;T;F):=\lim _{t\to 0^{+}}{\frac {T(t\Delta _{x}+(1-t)F)-T(F)}{t}}.$

It describes the effect of an infinitesimal contamination at the point x on the estimate we are seeking, standardized by the mass t of the contamination (the asymptotic bias caused by contamination in the observations). For a robust estimator, we want a bounded influence function, that is, one which does not go to infinity as x becomes arbitrarily large.

The empirical influence function uses the empirical distribution function ${\hat {F}}$ instead of the distribution function F , making use of the drop-in principle.

### Desirable properties

Properties of an influence function that bestow it with desirable performance are:

1. Finite rejection point $\rho ^{*}$ ,
2. Small gross-error sensitivity $\gamma ^{*}$ ,
3. Small local-shift sensitivity $\lambda ^{*}$ .

#### Rejection point

$\rho ^{*}:=\inf _{r>0}\{r:IF(x;T;F)=0,|x|>r\}$

#### Gross-error sensitivity

$\gamma ^{*}(T;F):=\sup _{x\in {\mathcal {X}}}|IF(x;T;F)|$

#### Local-shift sensitivity

$\lambda ^{*}(T;F):=\sup _{(x,y)\in {\mathcal {X}}^{2} \atop x\neq y}\left\|{\frac {IF(y;T;F)-IF(x;T;F)}{y-x}}\right\|$

This value, which looks a lot like a Lipschitz constant, represents the effect of shifting an observation slightly from x to a neighbouring point y , i.e., add an observation at y and remove one at x .

## M-estimators

*(The mathematical context of this paragraph is given in the section on empirical influence functions.)*

Historically, several approaches to robust estimation were proposed, including R-estimators and L-estimators. However, M-estimators now appear to dominate the field as a result of their generality, their potential for high breakdown points and comparatively high efficiency. See Huber (1981).

M-estimators are not inherently robust. However, they can be designed to achieve favourable properties, including robustness. M-estimator are a generalization of maximum likelihood estimators (MLEs) which is determined by maximizing ${\textstyle \prod _{i=1}^{n}f(x_{i})}$ or, equivalently, minimizing ${\textstyle \sum _{i=1}^{n}-\log f(x_{i})}$ . In 1964, Huber proposed to generalize this to the minimization of ${\textstyle \sum _{i=1}^{n}\rho (x_{i})}$ , where $\rho$ is some function. MLE are therefore a special case of M-estimators (hence the name: "*M*aximum likelihood type" estimators).

Minimizing ${\textstyle \sum _{i=1}^{n}\rho (x_{i})}$ can often be done by differentiating $\rho$ and solving ${\textstyle \sum _{i=1}^{n}\psi (x_{i})=0}$ , where ${\textstyle \psi (x)={\frac {d\rho (x)}{dx}}}$ (if $\rho$ has a derivative).

Several choices of $\rho$ and $\psi$ have been proposed. The two figures below show four $\rho$ functions and their corresponding $\psi$ functions.

For squared errors, $\rho (x)$ increases at an accelerating rate, whilst for absolute errors, it increases at a constant rate. When Winsorizing is used, a mixture of these two effects is introduced: for small values of x, $\rho$ increases at the squared rate, but once the chosen threshold is reached (1.5 in this example), the rate of increase becomes constant. This Winsorised estimator is also known as the Huber loss function.

Tukey's biweight (also known as bisquare) function behaves in a similar way to the squared error function at first, but for larger errors, the function tapers off.

### Properties of M-estimators

M-estimators do not necessarily relate to a probability density function. Therefore, off-the-shelf approaches to inference that arise from likelihood theory can not, in general, be used.

It can be shown that M-estimators are asymptotically normally distributed so that as long as their standard errors can be computed, an approximate approach to inference is available.

Since M-estimators are normal only asymptotically, for small sample sizes it might be appropriate to use an alternative approach to inference, such as the bootstrap. However, M-estimates are not necessarily unique (i.e., there might be more than one solution that satisfies the equations). Also, it is possible that any particular bootstrap sample can contain more outliers than the estimator's breakdown point. Therefore, some care is needed when designing bootstrap schemes.

Of course, as we saw with the speed-of-light example, the mean is only normally distributed asymptotically and when outliers are present the approximation can be very poor even for quite large samples. However, classical statistical tests, including those based on the mean, are typically bounded above by the nominal size of the test. The same is not true of M-estimators and the type I error rate can be substantially above the nominal level.

These considerations do not "invalidate" M-estimation in any way. They merely make clear that some care is needed in their use, as is true of any other method of estimation.

### Influence function of an M-estimator

It can be shown that the influence function of an M-estimator T is proportional to $\psi$ , which means we can derive the properties of such an estimator (such as its rejection point, gross-error sensitivity or local-shift sensitivity) when we know its $\psi$ function.

$IF(x;T,F)=M^{-1}\psi (x,T(F))$

with the $p\times p$ given by:

$M=-\int _{\mathcal {X}}\left({\frac {\partial \psi (x,\theta )}{\partial \theta }}\right)_{T(F)}\,dF(x).$

### Choice of *ψ* and *ρ*

In many practical situations, the choice of the $\psi$ function is not critical to gaining a good robust estimate, and many choices will give similar results that offer great improvements, in terms of efficiency and bias, over classical estimates in the presence of outliers.

Theoretically, $\psi$ functions are to be preferred, and Tukey's biweight (also known as bisquare) function is a popular choice. Maronna et al. recommend the biweight function with efficiency at the normal set to 85%.

## Robust parametric approaches

M-estimators do not necessarily relate to a density function and so are not fully parametric. Fully parametric approaches to robust modeling and inference, both Bayesian and likelihood approaches, usually deal with heavy-tailed distributions such as Student's *t*-distribution.

For the *t*-distribution with $\nu$ degrees of freedom, it can be shown that

$\psi (x)={\frac {x}{x^{2}+\nu }}.$

For $\nu =1$ , the *t*-distribution is equivalent to the Cauchy distribution. The degrees of freedom is sometimes known as the *kurtosis parameter*. It is the parameter that controls how heavy the tails are. In principle, $\nu$ can be estimated from the data in the same way as any other parameter. In practice, it is common for there to be multiple local maxima when $\nu$ is allowed to vary. As such, it is common to fix $\nu$ at a value around 4 or 6. The figure below displays the $\psi$ -function for 4 different values of $\nu$ .

### Example: speed-of-light data

For the speed-of-light data, allowing the kurtosis parameter to vary and maximizing the likelihood, we get

${\hat {\mu }}=27.40,\quad {\hat {\sigma }}=3.81,\quad {\hat {\nu }}=2.13.$

Fixing $\nu =4$ and maximizing the likelihood gives

${\hat {\mu }}=27.49,\quad {\hat {\sigma }}=4.51.$

A pivotal quantity is a function of data, whose underlying population distribution is a member of a parametric family, that is not dependent on the values of the parameters. An ancillary statistic is such a function that is also a statistic, meaning that it is computed in terms of the data alone. Such functions are robust to parameters in the sense that they are independent of the values of the parameters, but not robust to the model in the sense that they assume an underlying model (parametric family), and in fact, such functions are often very sensitive to violations of the model assumptions. Thus test statistics, frequently constructed in terms of these to not be sensitive to assumptions about parameters, are still very sensitive to model assumptions.

## Replacing outliers and missing values

Replacing missing data is called imputation. If there are relatively few missing points, there are some models which can be used to estimate values to complete the series, such as replacing missing values with the mean or median of the data. Simple linear regression can also be used to estimate missing values. In addition, outliers can sometimes be accommodated in the data through the use of trimmed means, other scale estimators apart from standard deviation (e.g., MAD) and Winsorization. In calculations of a trimmed mean, a fixed percentage of data is dropped from each end of an ordered data, thus eliminating the outliers. The mean is then calculated using the remaining data. Winsorizing involves accommodating an outlier by replacing it with the next highest or next smallest value as appropriate.

However, using these types of models to predict missing values or outliers in a long time series is difficult and often unreliable, particularly if the number of values to be in-filled is relatively high in comparison with total record length. The accuracy of the estimate depends on how good and representative the model is and how long the period of missing values extends. When dynamic evolution is assumed in a series, the missing data point problem becomes an exercise in multivariate analysis (rather than the univariate approach of most traditional methods of estimating missing values and outliers). In such cases, a multivariate model will be more representative than a univariate one for predicting missing values. The Kohonen self organising map (KSOM) offers a simple and robust multivariate model for data analysis, thus providing good possibilities to estimate missing values, taking into account their relationship or correlation with other pertinent variables in the data record.

Standard Kalman filters are not robust to outliers. To this end Ting, Theodorou & Schaal (2007) have recently shown that a modification of Masreliez's theorem can deal with outliers.

One common approach to handle outliers in data analysis is to perform outlier detection first, followed by an efficient estimation method (e.g., the least squares). While this approach is often useful, one must keep in mind two challenges. First, an outlier detection method that relies on a non-robust initial fit can suffer from the effect of masking, that is, a group of outliers can mask each other and escape detection. Second, if a high breakdown initial fit is used for outlier detection, the follow-up analysis might inherit some of the inefficiencies of the initial estimator.

## Use in machine learning

Although influence functions have a long history in statistics, they were not widely used in machine learning due to several challenges. One of the primary obstacles is that traditional influence functions rely on expensive second-order derivative computations and assume model differentiability and convexity. These assumptions are limiting, especially in modern machine learning, where models are often non-differentiable, non-convex, and operate in high-dimensional spaces.

Koh & Liang (2017) addressed these challenges by introducing methods to efficiently approximate influence functions using second-order optimization techniques, such as those developed by Pearlmutter (1994), Martens (2010), and Agarwal, Bullins & Hazan (2017). Their approach remains effective even when the assumptions of differentiability and convexity degrade, enabling influence functions to be used in the context of non-convex deep learning models. They demonstrated that influence functions are a powerful and versatile tool that can be applied to a variety of tasks in machine learning, including:

- Understanding Model Behavior: Influence functions help identify which training points are most “responsible” for a given prediction, offering insights into how models generalize from training data.

- Debugging Models: Influence functions can assist in identifying domain mismatches—when the training data distribution does not match the test data distribution—which can cause models with high training accuracy to perform poorly on test data, as shown by Ben-David et al. (2010). By revealing which training examples contribute most to errors, developers can address these mismatches.

- Dataset Error Detection: Noisy or corrupted labels are common in real-world data, especially when crowdsourced or adversarially attacked. Influence functions allow human experts to prioritize reviewing only the most impactful examples in the training set, facilitating efficient error detection and correction.

- Adversarial Attacks: Models that rely heavily on a small number of influential training points are vulnerable to adversarial perturbations. These perturbed inputs can significantly alter predictions and pose security risks in machine learning systems where attackers have access to the training data (See adversarial machine learning).

Koh and Liang’s contributions have opened the door for influence functions to be used in various applications across machine learning, from interpretability to security, marking a significant advance in their applicability.
