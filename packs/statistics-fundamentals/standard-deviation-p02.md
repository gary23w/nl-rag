---
title: "Standard deviation (part 2/2)"
source: https://en.wikipedia.org/wiki/Standard_deviation
domain: statistics-fundamentals
license: CC-BY-SA-4.0
tags: statistics fundamentals, probability, statistical inference, hypothesis testing, probability distribution
fetched: 2026-07-02
part: 2/2
---

## Relationship between standard deviation and mean

The mean and the standard deviation of a set of data are descriptive statistics usually reported together. In a certain sense, the standard deviation is a "natural" measure of statistical dispersion if the center of the data is measured about the mean. This is because the standard deviation from the mean is smaller than from any other point. The precise statement is the following: suppose *x*1, ..., *x**n* are real numbers and define the function:

σ ( r ) = 1 N − 1 ∑ i = 1 N ( x i − r ) 2 . {\displaystyle \sigma (r)={\sqrt {{\frac {1}{N-1}}\sum _{i=1}^{N}\left(x_{i}-r\right)^{2}}}.} ({\displaystyle \sigma (r)={\sqrt {{\frac {1}{N-1}}\sum _{i=1}^{N}\left(x_{i}-r\right)^{2}}}.})

Using calculus or by completing the square, it is possible to show that *σ*(*r*) has a unique minimum at the mean:

r = x ¯ . {\displaystyle r={\bar {x}}.\,} ({\displaystyle r={\bar {x}}.\,})

Variability can also be measured by the coefficient of variation, which is the ratio of the standard deviation to the mean. It is a dimensionless number.

### Standard deviation of the mean

Often, we want some information about the precision of the mean we obtained. We can obtain this by determining the standard deviation of the sampled mean. Assuming statistical independence of the values in the sample, the **standard deviation of the mean** (**SDOM**) is related to the standard deviation of the distribution by:

σ mean = 1 N σ , {\displaystyle \sigma _{\text{mean}}={\frac {1}{\sqrt {N}}}\sigma ,} ({\displaystyle \sigma _{\text{mean}}={\frac {1}{\sqrt {N}}}\sigma ,})

where N is the number of observations in the sample used to estimate the mean. This can easily be proven with (see basic properties of the variance): var ⁡ ( X ) = σ X 2 var ⁡ ( X 1 + X 2 ) = var ⁡ ( X 1 ) + var ⁡ ( X 2 ) {\displaystyle {\begin{aligned}\operatorname {var} (X)&=\sigma _{X}^{2}\\\operatorname {var} (X_{1}+X_{2})&=\operatorname {var} (X_{1})+\operatorname {var} (X_{2})\\\end{aligned}}} ({\displaystyle {\begin{aligned}\operatorname {var} (X)&=\sigma _{X}^{2}\\\operatorname {var} (X_{1}+X_{2})&=\operatorname {var} (X_{1})+\operatorname {var} (X_{2})\\\end{aligned}}}) (Statistical independence is assumed.) var ⁡ ( c X 1 ) ≡ c 2 var ⁡ ( X 1 ) {\displaystyle \operatorname {var} (cX_{1})\equiv c^{2}\,\operatorname {var} (X_{1})} ({\displaystyle \operatorname {var} (cX_{1})\equiv c^{2}\,\operatorname {var} (X_{1})})

hence var ⁡ ( mean ) = var ⁡ ( 1 N ∑ i = 1 N X i ) = 1 N 2 var ⁡ ( ∑ i = 1 N X i ) = 1 N 2 ∑ i = 1 N var ⁡ ( X i ) = N N 2 var ⁡ ( X ) = 1 N var ⁡ ( X ) . {\displaystyle {\begin{aligned}\operatorname {var} ({\text{mean}})&=\operatorname {var} \left({\frac {1}{N}}\sum _{i=1}^{N}X_{i}\right)={\frac {1}{N^{2}}}\operatorname {var} \left(\sum _{i=1}^{N}X_{i}\right)\\&={\frac {1}{N^{2}}}\sum _{i=1}^{N}\operatorname {var} (X_{i})={\frac {N}{N^{2}}}\operatorname {var} (X)={\frac {1}{N}}\operatorname {var} (X).\end{aligned}}} ({\displaystyle {\begin{aligned}\operatorname {var} ({\text{mean}})&=\operatorname {var} \left({\frac {1}{N}}\sum _{i=1}^{N}X_{i}\right)={\frac {1}{N^{2}}}\operatorname {var} \left(\sum _{i=1}^{N}X_{i}\right)\\&={\frac {1}{N^{2}}}\sum _{i=1}^{N}\operatorname {var} (X_{i})={\frac {N}{N^{2}}}\operatorname {var} (X)={\frac {1}{N}}\operatorname {var} (X).\end{aligned}}})

Resulting in: σ mean = σ N . {\displaystyle \sigma _{\text{mean}}={\frac {\sigma }{\sqrt {N}}}.} ({\displaystyle \sigma _{\text{mean}}={\frac {\sigma }{\sqrt {N}}}.})

In order to estimate the standard deviation of the mean *σ*mean it is necessary to know the standard deviation of the entire population σ beforehand. However, in most applications this parameter is unknown. For example, if a series of 10 measurements of a previously unknown quantity is performed in a laboratory, it is possible to calculate the resulting sample mean and sample standard deviation, but it is impossible to calculate the standard deviation of the mean. However, one can estimate the standard deviation of the entire population from the sample, and thus obtain an estimate for the standard error of the mean.


## Rapid calculation methods

The following two formulas can represent a running (repeatedly updated) standard deviation. A set of two power sums *s*1 and *s*2 are computed over a set of N values of x, denoted as *x*1, ..., *x**N*:

s j = ∑ k = 1 N x k j . {\displaystyle s_{j}=\sum _{k=1}^{N}{x_{k}^{j}}.} ({\displaystyle s_{j}=\sum _{k=1}^{N}{x_{k}^{j}}.})

Given the results of these running summations, the values N, *s*1, *s*2 can be used at any time to compute the *current* value of the running standard deviation:

σ = N s 2 − ( s 1 ) 2 N . {\displaystyle \sigma ={\frac {\sqrt {Ns_{2}-(s_{1})^{2}}}{N}}.} ({\displaystyle \sigma ={\frac {\sqrt {Ns_{2}-(s_{1})^{2}}}{N}}.})

Where N, as mentioned above, is the size of the set of values (or can also be regarded as *s*0).

Similarly for sample standard deviation,

s = N s 2 − ( s 1 ) 2 N ( N − 1 ) . {\displaystyle s={\sqrt {\frac {Ns_{2}-(s_{1})^{2}}{N(N-1)}}}.} ({\displaystyle s={\sqrt {\frac {Ns_{2}-(s_{1})^{2}}{N(N-1)}}}.})

In a computer implementation, as the two *s**j* sums become large, we need to consider round-off error, arithmetic overflow, and arithmetic underflow. The method below calculates the running sums method with reduced rounding errors. This is a "one pass" algorithm for calculating variance of n samples without the need to store prior data during the calculation. Applying this method to a time series will result in successive values of standard deviation corresponding to n data points as n grows larger with each new sample, rather than a constant-width sliding window calculation.

For *k* = 1, ..., *n*:

A 0 = 0 A k = A k − 1 + x k − A k − 1 k {\displaystyle {\begin{aligned}A_{0}&=0\\A_{k}&=A_{k-1}+{\frac {x_{k}-A_{k-1}}{k}}\end{aligned}}} ({\displaystyle {\begin{aligned}A_{0}&=0\\A_{k}&=A_{k-1}+{\frac {x_{k}-A_{k-1}}{k}}\end{aligned}}})

where A is the mean value. Q 0 = 0 Q k = Q k − 1 + k − 1 k ( x k − A k − 1 ) 2 = Q k − 1 + ( x k − A k − 1 ) ( x k − A k ) {\displaystyle {\begin{aligned}Q_{0}&=0\\Q_{k}&=Q_{k-1}+{\frac {k-1}{k}}\left(x_{k}-A_{k-1}\right)^{2}\\&=Q_{k-1}+\left(x_{k}-A_{k-1}\right)\left(x_{k}-A_{k}\right)\end{aligned}}} ({\displaystyle {\begin{aligned}Q_{0}&=0\\Q_{k}&=Q_{k-1}+{\frac {k-1}{k}}\left(x_{k}-A_{k-1}\right)^{2}\\&=Q_{k-1}+\left(x_{k}-A_{k-1}\right)\left(x_{k}-A_{k}\right)\end{aligned}}})

Note: *Q*1 = 0 since *k* − 1 = 0 or *x*1 = *A*1.

Sample variance: s n 2 = Q n n − 1 {\displaystyle s_{n}^{2}={\frac {Q_{n}}{n-1}}} ({\displaystyle s_{n}^{2}={\frac {Q_{n}}{n-1}}})

Population variance: σ n 2 = Q n n {\displaystyle \sigma _{n}^{2}={\frac {Q_{n}}{n}}} ({\displaystyle \sigma _{n}^{2}={\frac {Q_{n}}{n}}})

### Weighted calculation

When the values x k {\displaystyle x_{k}} ({\displaystyle x_{k}}) are weighted with unequal weights w k {\displaystyle w_{k}} ({\displaystyle w_{k}}), the power sums *s*0, s1, *s*2 are each computed as:

s j = ∑ k = 1 N w k x k j . {\displaystyle s_{j}=\sum _{k=1}^{N}w_{k}x_{k}^{j}.\,} ({\displaystyle s_{j}=\sum _{k=1}^{N}w_{k}x_{k}^{j}.\,})

And the standard deviation equations remain unchanged. *s*0 is now the sum of the weights and not the number of samples N.

The incremental method with reduced rounding errors can also be applied, with some additional complexity.

A running sum of weights must be computed for each k from 1 to n: W 0 = 0 W k = W k − 1 + w k {\displaystyle {\begin{aligned}W_{0}&=0\\W_{k}&=W_{k-1}+w_{k}\end{aligned}}} ({\displaystyle {\begin{aligned}W_{0}&=0\\W_{k}&=W_{k-1}+w_{k}\end{aligned}}})

and places where 1/*k* is used above must be replaced by w k / W k {\displaystyle w_{k}/W_{k}} ({\displaystyle w_{k}/W_{k}}): A 0 = 0 A k = A k − 1 + w k W k ( x k − A k − 1 ) Q 0 = 0 Q k = Q k − 1 + w k W k − 1 W k ( x k − A k − 1 ) 2 = Q k − 1 + w k ( x k − A k − 1 ) ( x k − A k ) {\displaystyle {\begin{aligned}A_{0}&=0\\A_{k}&=A_{k-1}+{\frac {w_{k}}{W_{k}}}\left(x_{k}-A_{k-1}\right)\\Q_{0}&=0\\Q_{k}&=Q_{k-1}+{\frac {w_{k}W_{k-1}}{W_{k}}}\left(x_{k}-A_{k-1}\right)^{2}\\&=Q_{k-1}+w_{k}\left(x_{k}-A_{k-1}\right)\left(x_{k}-A_{k}\right)\end{aligned}}} ({\displaystyle {\begin{aligned}A_{0}&=0\\A_{k}&=A_{k-1}+{\frac {w_{k}}{W_{k}}}\left(x_{k}-A_{k-1}\right)\\Q_{0}&=0\\Q_{k}&=Q_{k-1}+{\frac {w_{k}W_{k-1}}{W_{k}}}\left(x_{k}-A_{k-1}\right)^{2}\\&=Q_{k-1}+w_{k}\left(x_{k}-A_{k-1}\right)\left(x_{k}-A_{k}\right)\end{aligned}}})

In the final division, σ n 2 = Q n W n {\displaystyle \sigma _{n}^{2}={\frac {Q_{n}}{W_{n}}}\,} ({\displaystyle \sigma _{n}^{2}={\frac {Q_{n}}{W_{n}}}\,})

and s n 2 = Q n W n − 1 , {\displaystyle s_{n}^{2}={\frac {Q_{n}}{W_{n}-1}},} ({\displaystyle s_{n}^{2}={\frac {Q_{n}}{W_{n}-1}},})

or s n 2 = n ′ n ′ − 1 σ n 2 , {\displaystyle s_{n}^{2}={\frac {n'}{n'-1}}\sigma _{n}^{2},} ({\displaystyle s_{n}^{2}={\frac {n'}{n'-1}}\sigma _{n}^{2},})

where n is the total number of elements, and n′ is the number of elements with non-zero weights.

The above formulas become equal to the simpler formulas given above if weights are taken as equal to one.


## History

The term *standard deviation* was first used in writing by Karl Pearson in 1894, following his use of it in lectures. This was as a replacement for earlier alternative names for the same idea: for example, Gauss used *mean error*.


## Standard deviation index

The standard deviation index (SDI) is used in external quality assessments, particularly for medical laboratories. It is calculated as: SDI = Laboratory mean − Consensus group mean Consensus group standard deviation . {\displaystyle {\text{SDI}}={\frac {{\text{Laboratory mean}}-{\text{Consensus group mean}}}{\text{Consensus group standard deviation}}}.} ({\displaystyle {\text{SDI}}={\frac {{\text{Laboratory mean}}-{\text{Consensus group mean}}}{\text{Consensus group standard deviation}}}.})


## Alternatives

Standard deviation is algebraically simpler, though in practice less robust, than the average absolute deviation.
