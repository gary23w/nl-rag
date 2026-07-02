---
title: "Outlier"
source: https://en.wikipedia.org/wiki/Outlier
domain: anomaly-detection
license: CC-BY-SA-4.0
tags: anomaly detection, outlier detection, novelty detection, isolation forest, fraud detection
fetched: 2026-07-02
---

# Outlier

In statistics, an **outlier** is a data point that differs significantly from other observations. An outlier may be due to a variability in the measurement, an indication of novel data, or it may be the result of experimental error; the latter are sometimes excluded from the data set. An outlier can be an indication of exciting possibility, but can also cause serious problems in statistical analyses.

Outliers can occur by chance in any distribution, but they can indicate novel behaviour or structures in the data-set, measurement error, or that the population has a heavy-tailed distribution. In the case of measurement error, one wishes to discard them or use statistics that are robust to outliers, while in the case of heavy-tailed distributions, they indicate that the distribution has high skewness and that one should be very cautious in using tools or intuitions that assume a normal distribution. A frequent cause of outliers is a mixture of two distributions, which may be two distinct sub-populations, or may indicate 'correct trial' versus 'measurement error'; this is modeled by a mixture model.

In most larger samplings of data, some data points will be further away from the sample mean than what is deemed reasonable. This can be due to incidental systematic error or flaws in the theory that generated an assumed family of probability distributions, or it may be that some observations are far from the center of the data. Outlier points can therefore indicate faulty data, erroneous procedures, or areas where a certain theory might not be valid. However, in large samples, a small number of outliers is to be expected (and not due to any anomalous condition).

Outliers, being the most extreme observations, may include the sample maximum or sample minimum, or both, depending on whether they are extremely high or low. However, the sample maximum and minimum are not always outliers because they may not be unusually far from other observations.

Naive interpretation of statistics derived from data sets that include outliers may be misleading. For example, if one is calculating the average temperature of 10 objects in a room, and nine of them are between 20 and 25 degrees Celsius, but an oven is at 175 °C, the median of the data will be between 20 and 25 °C but the mean temperature will be between 35.5 and 40 °C. In this case, the median better reflects the temperature of a randomly sampled object (but not the temperature in the room) than the mean; naively interpreting the mean as "a typical sample", equivalent to the median, is incorrect. As illustrated in this case, outliers may indicate data points that belong to a different population than the rest of the sample set.

Estimators capable of coping with outliers are said to be robust: the median is a robust statistic of central tendency, while the mean is not.

## Occurrence and causes

In the case of normally distributed data, the three sigma rule means that roughly 1 in 22 observations will differ by twice the standard deviation or more from the mean, and 1 in 370 will deviate by three times the standard deviation. In a sample of 1000 observations, the presence of up to five observations deviating from the mean by more than three times the standard deviation is within the range of what can be expected, being less than twice the expected number and hence within 1 standard deviation of the expected number – see Poisson distribution – and not indicate an anomaly. If the sample size is only 100, however, just three such outliers are already reason for concern, being more than 11 times the expected number.

In general, if the nature of the population distribution is known *a priori*, it is possible to test if the number of outliers deviate significantly from what can be expected: for a given cutoff (so samples fall beyond the cutoff with probability *p*) of a given distribution, the number of outliers will follow a binomial distribution with parameter *p*, which can generally be well-approximated by the Poisson distribution with λ = *pn*. Thus if one takes a normal distribution with cutoff 3 standard deviations from the mean, *p* is approximately 0.3%, and thus for 1000 trials one can approximate the number of samples whose deviation exceeds 3 sigmas by a Poisson distribution with λ = 3.

### Causes

Outliers can have many anomalous causes. A physical apparatus for taking measurements may have suffered a transient malfunction. There may have been an error in data transmission or transcription. Outliers arise due to changes in system behaviour, fraudulent behaviour, human error, instrument error or simply through natural deviations in populations. A sample may have been contaminated with elements from outside the population being examined. Alternatively, an outlier could be the result of a flaw in the assumed theory, calling for further investigation by the researcher. Additionally, the pathological appearance of outliers of a certain form appears in a variety of datasets, indicating that the causative mechanism for the data might differ at the extreme end (King effect).

## Definitions and detection

There is no rigid mathematical definition of what constitutes an outlier; determining whether or not an observation is an outlier is ultimately a subjective exercise.

There are various methods of outlier detection, some of which are treated as synonymous with novelty detection. Some are graphical such as normal probability plots. Others are model-based. Box plots are a hybrid.

Model-based methods which are commonly used for identification assume that the data are from a normal distribution, and identify observations which are deemed "unlikely" based on mean and standard deviation:

- Chauvenet's criterion
- Grubbs's test for outliers
- Dixon's *Q* test
- ASTM E178: Standard Practice for Dealing With Outlying Observations
- Mahalanobis distance and leverage are often used to detect outliers, especially in the development of linear regression models.
- Subspace and correlation based techniques for high-dimensional numerical data

### Peirce's criterion

> It is proposed to determine in a series of m observations the limit of error, beyond which all observations involving so great an error may be rejected, provided there are as many as n such observations. The principle upon which it is proposed to solve this problem is, that the proposed observations should be rejected when the probability of the system of errors obtained by retaining them is less than that of the system of errors obtained by their rejection multiplied by the probability of making so many, and no more, abnormal observations. (Quoted in the editorial note on page 516 to Peirce (1982 edition) from *A Manual of Astronomy* 2:558 by Chauvenet.)

### Tukey's fences

Other methods flag observations based on measures such as the interquartile range. For example, if $Q_{1}$ and $Q_{3}$ are the lower and upper quartiles respectively, then one could define an outlier to be any observation outside the range:

${\big [}Q_{1}-k(Q_{3}-Q_{1}),Q_{3}+k(Q_{3}-Q_{1}){\big ]}$

for some nonnegative constant k . John Tukey proposed this test, where $k=1.5$ indicates an "outlier", and $k=3$ indicates data that is "far out".

### In anomaly detection

In various domains such as, but not limited to, statistics, signal processing, finance, econometrics, manufacturing, networking and data mining, the task of *anomaly detection* may take other approaches. Some of these may be distance-based and density-based such as Local Outlier Factor (LOF). Some approaches may use the distance to the k-nearest neighbors to label observations as outliers or non-outliers.

### Modified Thompson Tau test

The modified Thompson Tau test is a method used to determine if an outlier exists in a data set. The strength of this method lies in the fact that it takes into account a data set's standard deviation, average and provides a statistically determined rejection zone; thus providing an objective method to determine if a data point is an outlier. How it works: First, a data set's average is determined. Next the absolute deviation between each data point and the average are determined. Thirdly, a rejection region is determined using the formula:

${\text{Rejection Region}}{=}{\frac {{t_{\alpha /2}}{\left(n-1\right)}}{{\sqrt {n}}{\sqrt {n-2+{t_{\alpha /2}^{2}}}}}}$

;

where $\scriptstyle {t_{\alpha /2}}$ is the critical value from the Student t distribution with *n*-2 degrees of freedom, *n* is the sample size, and s is the sample standard deviation. To determine if a value is an outlier: Calculate $\scriptstyle \delta =|(X-mean(X))/s|$ . If *δ* > Rejection Region, the data point is an outlier. If *δ* ≤ Rejection Region, the data point is not an outlier.

The modified Thompson Tau test is used to find one outlier at a time (largest value of *δ* is removed if it is an outlier). Meaning, if a data point is found to be an outlier, it is removed from the data set and the test is applied again with a new average and rejection region. This process is continued until no outliers remain in a data set.

Some work has also examined outliers for nominal (or categorical) data. In the context of a set of examples (or instances) in a data set, instance hardness measures the probability that an instance will be misclassified ( $1-p(y|x)$ where y is the assigned class label and x represent the input attribute value for an instance in the training set t). Ideally, instance hardness would be calculated by summing over the set of all possible hypotheses H:

${\begin{aligned}IH(\langle x,y\rangle )&=\sum _{H}(1-p(y,x,h))p(h|t)\\&=\sum _{H}p(h|t)-p(y,x,h)p(h|t)\\&=1-\sum _{H}p(y,x,h)p(h|t).\end{aligned}}$

Practically, this formulation is unfeasible as H is potentially infinite and calculating $p(h|t)$ is unknown for many algorithms. Thus, instance hardness can be approximated using a diverse subset $L\subset H$ :

$IH_{L}(\langle x,y\rangle )=1-{\frac {1}{|L|}}\sum _{j=1}^{|L|}p(y|x,g_{j}(t,\alpha ))$

where $g_{j}(t,\alpha )$ is the hypothesis induced by learning algorithm $g_{j}$ trained on training set t with hyperparameters $\alpha$ . Instance hardness provides a continuous value for determining if an instance is an outlier instance.

## Working with outliers

The choice of how to deal with an outlier should depend on the cause. Some estimators are highly sensitive to outliers, notably estimation of covariance matrices.

### Retention

Even when a normal distribution model is appropriate to the data being analyzed, outliers are expected for large sample sizes and should not automatically be discarded if that is the case. Instead, one should use a method that is robust to outliers to model or analyze data with naturally occurring outliers.

### Exclusion

When deciding whether to remove an outlier, the cause has to be considered. As mentioned earlier, if the outlier's origin can be attributed to an experimental error, or if it can be otherwise determined that the outlying data point is erroneous, it is generally recommended to remove it. However, it is more desirable to correct the erroneous value, if possible.

Removing a data point solely because it is an outlier, on the other hand, is a controversial practice, often frowned upon by many scientists and science instructors, as it typically invalidates statistical results. While mathematical criteria provide an objective and quantitative method for data rejection, they do not make the practice more scientifically or methodologically sound, especially in small sets or where a normal distribution cannot be assumed. Rejection of outliers is more acceptable in areas of practice where the underlying model of the process being measured and the usual distribution of measurement error are confidently known.

The two common approaches to exclude outliers are truncation (or trimming) and Winsorising. Trimming discards the outliers whereas Winsorising replaces the outliers with the nearest "nonsuspect" data. Exclusion can also be a consequence of the measurement process, such as when an experiment is not entirely capable of measuring such extreme values, resulting in censored data.

In regression problems, an alternative approach may be to only exclude points which exhibit a large degree of influence on the estimated coefficients, using a measure such as Cook's distance.

If a data point (or points) is excluded from the data analysis, this should be clearly stated on any subsequent report.

### Non-normal distributions

The possibility should be considered that the underlying distribution of the data is not approximately normal, having "fat tails". For instance, when sampling from a Cauchy distribution, the sample variance increases with the sample size, the sample mean fails to converge as the sample size increases, and outliers are expected at far larger rates than for a normal distribution. Even a slight difference in the fatness of the tails can make a large difference in the expected number of extreme values.

### Set-membership uncertainties

A set membership approach considers that the uncertainty corresponding to the *i*th measurement of an unknown random vector *x* is represented by a set *X*i (instead of a probability density function). If no outliers occur, *x* should belong to the intersection of all *X*i's. When outliers occur, this intersection could be empty, and we should relax a small number of the sets *X*i (as small as possible) in order to avoid any inconsistency. This can be done using the notion of *q*-relaxed intersection. As illustrated by the figure, the *q*-relaxed intersection corresponds to the set of all *x* which belong to all sets except *q* of them. Sets *X*i that do not intersect the *q*-relaxed intersection could be suspected to be outliers.

### Alternative models

In cases where the cause of the outliers is known, it may be possible to incorporate this effect into the model structure, for example by using a hierarchical Bayes model, or a mixture model.

### Choice of distance metrics

In cluster analysis, outliers can greatly distort the results. Thus, the handling of outliers has been an issue of much discussion.

Cluster analysis relies heavily on distance measures. It has been suggested that Manhattan distance, due to the lack of squaring disproportionately large difference values, is likely to handle outliers better than Euclidean distance.
