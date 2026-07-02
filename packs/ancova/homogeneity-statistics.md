---
title: "Homogeneity and heterogeneity (statistics)"
source: https://en.wikipedia.org/wiki/Homogeneity_(statistics)
domain: ancova
license: CC-BY-SA-4.0
tags: analysis of covariance, covariate adjustment, confounding variable, adjusted mean
fetched: 2026-07-02
---

# Homogeneity and heterogeneity (statistics)

(Redirected from

Homogeneity (statistics)

)

In statistics, **homogeneity** and its opposite, **heterogeneity**, arise in describing the properties of a dataset, or several datasets. They relate to the validity of the often convenient assumption that the statistical properties of any one part of an overall dataset are the same as any other part. In meta-analysis, which combines data from any number of studies, homogeneity measures the differences or similarities between those studies' (see also study heterogeneity) estimates.

Homogeneity can be studied to several degrees of complexity. For example, considerations of homoscedasticity examine how much the variability of data-values changes throughout a dataset. However, questions of homogeneity apply to all aspects of statistical distributions, including the location parameter. Thus, a more detailed study would examine changes to the whole of the marginal distribution. An intermediate-level study might move from looking at the variability to studying changes in the skewness. In addition to these, questions of homogeneity also apply to the joint distributions.

The concept of homogeneity can be applied in many different ways. For certain types of statistical analysis, it is used to look for further properties that might need to be treated as varying within a dataset once some initial types of non-homogeneity have been dealt with.

## Of variance

In statistics, a sequence of random variables is homoscedastic (/ˌhoʊmoʊskəˈdæstɪk/) if all its random variables have the same finite variance; this is also known as homogeneity of variance. The complementary notion is called heteroscedasticity, also known as heterogeneity of variance. The term originates from the Ancient Greek σκεδάννυμι *skedánnymi*, 'to scatter'.

Assuming a variable is homoscedastic when in reality it is heteroscedastic (/ˌhɛtəroʊskəˈdæstɪk/) results in unbiased but inefficient point estimates and in biased estimates of standard errors, and may result in overestimating the goodness of fit as measured by the Pearson coefficient.

The existence of heteroscedasticity is a major concern in regression analysis and the analysis of variance, as it invalidates statistical tests of significance which assume that the modelling errors all have the same variance. While the ordinary least squares (OLS) estimator is still unbiased in the presence of heteroscedasticity, it is inefficient and inference based on the assumption of homoskedasticity is misleading. In that case, generalized least squares (GLS) was frequently used in the past. Nowadays, standard practice in econometrics is to include heteroskedasticity-consistent standard errors instead of using GLS, as GLS can exhibit strong bias in small samples if the actual skedastic function is unknown.

Because heteroscedasticity concerns expectations of the second moment of the errors, its presence is referred to as misspecification of the second order.

The econometrician Robert Engle was awarded the 2003 Nobel Memorial Prize for Economics for his studies on regression analysis in the presence of heteroscedasticity, which led to his formulation of the autoregressive conditional heteroscedasticity (ARCH) modeling technique.

## Examples

### Regression

Differences in the typical values across the dataset might initially be dealt with by constructing a regression model using certain explanatory variables to relate variations in the typical value to known quantities. There should then be a later stage of analysis to examine whether the errors in the predictions from the regression behave in the same way across the dataset. Thus, the question becomes one of the homogeneity of the distribution of the residuals, as the explanatory variables change. See regression analysis.

### Time series

The initial stages in analyzing a time series may involve plotting values against time to examine the series' homogeneity in various ways: stability across time as opposed to a trend, stability of local fluctuations over time.

### Combining information across sites

In hydrology, data series across a number of sites composed of annual values of the within-year annual maximum river flow are analysed. A common model is that the distributions of these values are the same for all sites apart from a simple scaling factor, so that the location and scale are linked in a simple way. There can then be questions of examining the homogeneity across sites of the distribution of the scaled values.

### Combining information sources

In meteorology, weather datasets are acquired over many years of record, and, as part of this, measurements at certain stations may cease occasionally while, at around the same time, measurements may start at nearby locations. There are then questions as to whether, if the records are combined to form a single longer set of records, those records can be considered homogeneous over time. An example of homogeneity testing of wind speed and direction data can be found in Romanić *et al*., 2015.

### Homogeneity within populations

Simple population surveys may assume that responses will be homogeneous across the whole population. Assessing the homogeneity of the population would involve examining whether the responses of certain identifiable subpopulations differ from those of others. For example, car owners may differ from non-car owners, or there may be differences between different age groups.

## Tests

A test for homogeneity, in the sense of exact equivalence of statistical distributions, can be based on an E-statistic. A location test tests the simpler hypothesis that distributions have the same location parameter.
