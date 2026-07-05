---
title: "Arithmetic mean"
source: https://en.wikipedia.org/wiki/Arithmetic_mean
domain: beale-number
license: CC-BY-SA-4.0
tags: beale number
fetched: 2026-07-05
---

# Arithmetic mean

In mathematics and statistics, the **arithmetic mean** ( /ˌærɪθˈmɛtɪk/ ⓘ *arr-ith-MET-ik*), **arithmetic average**, or just the *mean* or *average* is the sum of a collection of numbers divided by the count of numbers in the collection. The collection is often a set of results from an experiment, an observational study, or a survey. The term "arithmetic mean" is preferred in some contexts in mathematics and statistics because it helps to distinguish it from other types of means, such as geometric and harmonic.

Arithmetic means are also frequently used in economics, anthropology, history, and almost every other academic field to some extent. For example, per capita income is the arithmetic average of the income of a nation's population.

While the arithmetic mean is often used to report central tendencies, it is not a robust statistic: it is greatly influenced by outliers (values much larger or smaller than most others). For skewed distributions, such as the distribution of income for which a few people's incomes are substantially higher than most people's, the arithmetic mean may not coincide with one's notion of "middle". In that case, robust statistics, such as the median, may provide a better description of central tendency.

## Definition

The arithmetic mean of a set of observed data is equal to the sum of the numerical values of each observation, divided by the total number of observations. Symbolically, for a data set consisting of the values $x_{1},\dots ,x_{n}$ , the arithmetic mean is defined by the formula:

${x}={\frac {1}{n}}\left(\sum _{i=1}^{n}{x_{i}}\right)={\frac {x_{1}+x_{2}+\dots +x_{n}}{n}}$

In simpler terms, the formula for the arithmetic mean is:

${\frac {\text{Sum of all values}}{\text{Number of values}}}$

For example, if the monthly salaries of 5 employees are $\{2500,2700,2300,2650,2450\}$ , then the arithmetic mean is:

${\frac {2500+2700+2300+2650+2450}{5}}=2520$

If the data set is a statistical population (i.e. consists of every possible observation and not just a subset of them), then the mean of that population is called the *population mean* and denoted by the Greek letter $\mu$ . If the data set is a statistical sample (a subset of the population), it is called the *sample mean* (which for a data set X is denoted as ${\overline {X}}$ ).

The arithmetic mean can be similarly defined for vectors in multiple dimensions, not only scalar values; this is often referred to as a centroid. More generally, because the arithmetic mean is a convex combination (meaning its coefficients sum to 1 ), it can be defined on a convex space, not only a vector space.

## History

Statistician Churchill Eisenhart, senior researcher fellow at the U. S. National Bureau of Standards, traced the history of the arithmetic mean in detail. In the modern age, it started to be used as a way of combining various observations that should be identical, but were not such as estimates of the direction of magnetic north. In 1635, mathematician Henry Gellibrand described as "meane" the midpoint of a lowest and highest number, not quite the arithmetic mean. In 1668, a person known as "D. B." was quoted in the Transactions of the Royal Society describing "taking the mean" of five values:

> In this Table, he [Capt. Sturmy] notes the greatest difference to be 14 minutes; and so taking the mean for the true Variation, he concludes it then and there to be just 1. deg. 27. min.

— D.B., p. 726

## Motivating properties

The arithmetic mean has several properties that make it interesting, especially as a measure of central tendency. These include:

- If numbers $x_{1},\dotsc ,x_{n}$ have a mean ${\bar {x}}$ , then $(x_{1}-{\bar {x}})+\dotsb +(x_{n}-{\bar {x}})=0$ . Since $x_{i}-{\bar {x}}$ is the distance from a given number to the mean, one way to interpret this property is by saying that the numbers to the left of the mean are balanced by the numbers to the right. The mean is the only number for which the residuals (deviations from the estimate) sum to zero. This can also be interpreted as saying that the mean is translationally invariant in the sense that for any real number a , ${\overline {x+a}}={\bar {x}}+a$ .
- If it is required to use a single number as a "typical" value for a set of known numbers $x_{1},\dotsc ,x_{n}$ , then the arithmetic mean of the numbers does this best since it minimizes the sum of squared deviations from the typical value: the sum of $(x_{i}-{\bar {x}})^{2}$ . The sample mean is also the best single predictor because it has the lowest root mean squared error. If the arithmetic mean of a population of numbers is desired, then the estimate of it that is unbiased is the arithmetic mean of a sample drawn from the population.

- The arithmetic mean is independent of scale of the units of measurement, in the sense that ${\text{avg}}(ca_{1},\cdots ,ca_{n})=c\cdot {\text{avg}}(a_{1},\cdots ,a_{n}).$ So, for example, calculating a mean of liters and then converting to gallons is the same as converting to gallons first and then calculating the mean. This is also called first order homogeneity.

### Additional properties

- The arithmetic mean of a sample is always between the largest and smallest values in that sample.
- The arithmetic mean of any amount of equal-sized number groups together is the arithmetic mean of the arithmetic means of each group.

## Contrast with median

The arithmetic mean differs from the median, which is the value that separates the higher half and lower half of a data set. When the values in a data set form an arithmetic progression, the median and arithmetic mean are equal. For example, in the data set ${1,2,3,4}$ , both the mean and median are $2.5$ .

In other cases, the mean and median can differ significantly. For instance, in the data set ${1,2,4,8,16}$ , the arithmetic mean is $6.2$ , while the median is 4 . This occurs because the mean is sensitive to extreme values and may not accurately reflect the central tendency of most data points.

This distinction has practical implications across different fields. For example, since the 1980s, the median income in the United States has increased at a slower rate than the arithmetic mean income.

Similarly, in climate studies, daily mean temperature distributions tend to approximate a normal distribution, whereas annual or monthly rainfall totals often display a skewed distribution, with some periods having unusually high totals while most have relatively low amounts. In such cases, the median can provide a more representative measure of central tendency.

## Generalizations

### Weighted average

A weighted average, or weighted mean, is an average in which some data points count more heavily than others in that they are given more weight in the calculation. For example, the arithmetic mean of 3 and 5 is ${\frac {3+5}{2}}=4$ , or equivalently $3\cdot {\frac {1}{2}}+5\cdot {\frac {1}{2}}=4$ . In contrast, a *weighted* mean in which the first number receives, for example, twice as much weight as the second (perhaps because it is assumed to appear twice as often in the general population from which these numbers were sampled) would be calculated as $3\cdot {\frac {2}{3}}+5\cdot {\frac {1}{3}}={\frac {11}{3}}$ . Here the weights, which necessarily sum to one, are ${\frac {2}{3}}$ and ${\frac {1}{3}}$ , the former being twice the latter. The arithmetic mean (sometimes called the "unweighted average" or "equally weighted average") can be interpreted as a special case of a weighted average in which all weights are equal to the same number ( ${\frac {1}{2}}$ in the above example and ${\frac {1}{n}}$ in a situation with n numbers being averaged).

### Functions

In calculus, and especially multivariable calculus, the mean of a function is loosely defined as the average value of the function over its domain.

### Continuous probability distributions

If a numerical property, and any sample of data from it, can take on any value from a continuous range instead of, for example, just integers, then the probability of a number falling into some range of possible values can be described by integrating a continuous probability distribution across this range, even when the naive probability for a sample number taking one certain value from infinitely many is zero. In this context, the analog of a weighted average, in which there are infinitely many possibilities for the precise value of the variable in each range, is called the *mean of the probability distribution*. The most widely encountered probability distribution is called the normal distribution; it has the property that all measures of its central tendency, including not just the mean but also the median mentioned above and the mode (the three Ms), are equal. This equality does not hold for other probability distributions, as illustrated for the log-normal distribution here.

### Angles

Particular care is needed when using cyclic data, such as phases or angles. Taking the arithmetic mean of 1° and 359° yields a result of 180°. This is incorrect for two reasons:

1. Angle measurements are only defined up to an additive constant of 360° ( $2\pi$ or $\tau$ , if measuring in radians). Thus, these could easily be called 1° and −1°, or 361° and 719°, since each one of them produces a different average.
2. In this situation, 0° (or 360°) is geometrically a better *average* value: there is lower dispersion about it (the points are both 1° from it and 179° from 180°, the putative average).

In general application, such an oversight will lead to the average value artificially moving towards the middle of the numerical range. A solution to this problem is to use the optimization formulation (that is, define the mean as the central point: the point about which one has the lowest dispersion) and redefine the difference as a modular distance (i.e. the distance on the circle: so the modular distance between 1° and 359° is 2°, not 358°).

## Symbols and encoding

The arithmetic mean is often denoted by a bar (vinculum or macron), as in ${\bar {x}}$ .
