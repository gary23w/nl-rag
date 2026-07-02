---
title: "Wilcoxon signed-rank test"
source: https://en.wikipedia.org/wiki/Wilcoxon_signed-rank_test
domain: nonparametric-tests
license: CC-BY-SA-4.0
tags: nonparametric statistics, rank correlation, sign test, Spearman correlation
fetched: 2026-07-02
---

# Wilcoxon signed-rank test

The **Wilcoxon signed-rank test** is a non-parametric rank test for statistical hypothesis testing used either to test the location of a population based on a sample of data, or to compare the locations of two populations using two matched samples. The one-sample version serves a purpose similar to that of the one-sample Student's *t*-test. For two matched samples, it is a paired difference test like the paired Student's *t*-test (also known as the "*t*-test for matched pairs" or "*t*-test for dependent samples"). The Wilcoxon test is a good alternative to the t-test when the normal distribution of the differences between paired individuals cannot be assumed. Instead, it assumes a weaker hypothesis that the distribution of this difference is symmetric around a central value and it aims to test whether this center value differs significantly from zero. The Wilcoxon test is a more powerful alternative to the sign test because it considers the magnitude of the differences, but it requires this moderately strong assumption of symmetry.

## History

The test is named after Frank Wilcoxon (1892–1965) who, in a single paper, proposed both it and the rank-sum test for two independent samples. The test was popularized by Sidney Siegel (1956) in his influential textbook on non-parametric statistics. Siegel used the symbol *T* for the test statistic, and consequently, the test is sometimes referred to as the **Wilcoxon *T*-test**.

## Test procedure

There are two variants of the signed-rank test. From a theoretical point of view, the one-sample test is more fundamental because the paired sample test is performed by converting the data to the situation of the one-sample test. However, most practical applications of the signed-rank test arise from paired data.

For a paired sample test, the data consists of a sample $(X_{1},Y_{1}),\dots ,(X_{n},Y_{n})$ . Each data point in the sample is a pair of measurements. In the simplest case, the measurements are on an interval scale. Then they may be converted to real numbers, and the paired sample test is converted to a one-sample test by replacing each pair of numbers $(X_{i},Y_{i})$ by its difference $X_{i}-Y_{i}$ . In general, it must be possible to rank the differences between the pairs. This requires that the data be on an *ordered metric* scale, a type of scale that carries more information than an ordinal scale but may have less than an interval scale.

The data for a one-sample test is a sample in which each observation is a real number: $X_{1},\dots ,X_{n}$ . Assume for simplicity that the observations in the sample have distinct absolute values and that no observation equals zero. (Zeros and ties introduce several Complications; see below.) The test is performed as follows:

1. Compute $|X_{1}|,\dots ,|X_{n}|.$
2. Sort $|X_{1}|,\dots ,|X_{n}|$ , and use this sorted list to assign ranks $R_{1},\dots ,R_{n}$ : The rank of the smallest observation is one, the rank of the next smallest is two, and so on.
3. Let $\operatorname {sgn}$ denote the sign function: $\operatorname {sgn}(x)=1$ if $x>0$ and $\operatorname {sgn}(x)=-1$ if $x<0$ . The test statistic is the *signed-rank sum* T : $T=\sum _{i=1}^{N}\operatorname {sgn}(X_{i})R_{i}.$
4. Produce a p -value by comparing T to its distribution under the null hypothesis.

The ranks are defined so that $R_{i}$ is the number of j for which $|X_{j}|\leq |X_{i}|$ . Additionally, if $\sigma :\{1,\dots ,n\}\to \{1,\dots ,n\}$ is such that $|X_{\sigma (1)}|<\dots <|X_{\sigma (n)}|$ , then $R_{\sigma (i)}=i$ for all i .

The signed-rank sum T is closely related to two other test statistics. The *positive-rank sum* $T^{+}$ and the *negative-rank sum* $T^{-}$ are defined by ${\begin{aligned}T^{+}&=\sum _{1\leq i\leq n,\ X_{i}>0}R_{i},\\T^{-}&=\sum _{1\leq i\leq n,\ X_{i}<0}R_{i}.\end{aligned}}$ Because $T^{+}+T^{-}$ equals the sum of all the ranks, which is $1+2+\dots +n=n(n+1)/2$ , these three statistics are related by: ${\begin{aligned}T^{+}&={\frac {n(n+1)}{2}}-T^{-}={\frac {n(n+1)}{4}}+{\frac {T}{2}},\\T^{-}&={\frac {n(n+1)}{2}}-T^{+}={\frac {n(n+1)}{4}}-{\frac {T}{2}},\\T&=T^{+}-T^{-}=2T^{+}-{\frac {n(n+1)}{2}}={\frac {n(n+1)}{2}}-2T^{-}.\end{aligned}}$ Because T , $T^{+}$ , and $T^{-}$ carry the same information, any of them may be used as the test statistic.

The positive-rank sum and negative-rank sum have alternative interpretations that are useful for the theory behind the test. Define the *Walsh average* $W_{ij}$ to be ${\tfrac {1}{2}}(X_{i}+X_{j})$ . Then: ${\begin{aligned}T^{+}=\#\{W_{ij}>0\colon 1\leq i\leq j\leq n\},\\T^{-}=\#\{W_{ij}<0\colon 1\leq i\leq j\leq n\}.\end{aligned}}$

## Null and alternative hypotheses

### One-sample test

The one-sample Wilcoxon signed-rank test can be used to test whether data comes from a symmetric population with a specified center (which corresponds to median, mean and pseudomedian). If the population center is known, then it can be used to test whether data is symmetric about its center.

To explain the null and alternative hypotheses formally, assume that the data consists of independent and identically distributed samples from a distribution F . If F can be assumed symmetric, then the null and alternative hypotheses are the following:

**Null hypothesis *H*0**

F

is symmetric about

$\mu =0$

.

**One-sided alternative hypothesis *H*1**

F

is symmetric about

$\mu <0$

.

**One-sided alternative hypothesis *H*2**

F

is symmetric about

$\mu >0$

.

**Two-sided alternative hypothesis *H*3**

F

is symmetric about

$\mu \neq 0$

.

If in addition $\Pr(X=\mu )=0$ , then $\mu$ is a median of F . If this median is unique, then the Wilcoxon signed-rank sum test becomes a test for the location of the median. When the mean of F is defined, then the mean is $\mu$ , and the test is also a test for the location of the mean.

The hypothesis that the data are IID can be weakened. Each data point may be taken from a different distribution, as long as all the distributions are assumed to be continuous and symmetric about a common point $\mu _{0}$ . The data points are not required to be independent as long as the conditional distribution of each observation given the others is symmetric about $\mu _{0}$ .

### Paired data test

Because the paired data test arises from taking paired differences, its null and alternative hypotheses can be derived from those of the one-sample test. In each case, they become assertions about the behavior of the differences $X_{i}-Y_{i}$ .

Let $F(x,y)$ be the joint cumulative distribution of the pairs $(X_{i},Y_{i})$ . If we assume that there exists a $\mu$ such that $X_{i}-Y_{i}$ is symmetric about $\mu$ , the null and alternative hypotheses are:

**Null hypothesis *H*0**

The observations

$X_{i}-Y_{i}$

are symmetric about

$\mu =0$

.

**One-sided alternative hypothesis *H*1**

The observations

$X_{i}-Y_{i}$

are symmetric about

$\mu <0$

.

**One-sided alternative hypothesis *H*2**

The observations

$X_{i}-Y_{i}$

are symmetric about

$\mu >0$

.

**Two-sided alternative hypothesis *H*3**

The observations

$X_{i}-Y_{i}$

are symmetric about

$\mu \neq 0$

.

These can also be expressed more directly in terms of the original pairs:

**Null hypothesis *H*0**

The observations

$(X_{i},Y_{i})$

are

exchangeable

, meaning that

$(X_{i},Y_{i})$

and

$(Y_{i},X_{i})$

have the same distribution. Equivalently,

$F(x,y)=F(y,x)$

.

**One-sided alternative hypothesis *H*1**

For some

$\mu <0$

, the pairs

$(X_{i},Y_{i})$

and

$(Y_{i}+\mu ,X_{i}-\mu )$

have the same distribution.

**One-sided alternative hypothesis *H*2**

For some

$\mu >0$

, the pairs

$(X_{i},Y_{i})$

and

$(Y_{i}+\mu ,X_{i}-\mu )$

have the same distribution.

**Two-sided alternative hypothesis *H*3**

For some

$\mu \neq 0$

, the pairs

$(X_{i},Y_{i})$

and

$(Y_{i}+\mu ,X_{i}-\mu )$

have the same distribution.

The null hypothesis of exchangeability can arise from a matched pair experiment with a treatment group and a control group. Randomizing the treatment and control within each pair makes the observations exchangeable. For an exchangeable distribution, $X_{i}-Y_{i}$ has the same distribution as $Y_{i}-X_{i}$ , and therefore, under the null hypothesis, the distribution is symmetric about zero.

## Zeros and ties

In real data, it sometimes happens that there is an observation $X_{i}$ in the sample which equals zero or a pair $(X_{i},Y_{i})$ with $X_{i}=Y_{i}$ . It can also happen that there are tied observations. This means that for some $i\neq j$ , we have $X_{i}=X_{j}$ (in the one-sample case) or $X_{i}-Y_{i}=X_{j}-Y_{j}$ (in the paired sample case). This is particularly common for discrete data. When this happens, the test procedure defined above is usually undefined because there is no way to uniquely rank the data. (The sole exception is if there is a single observation $X_{i}$ which is zero and no other zeros or ties.) Because of this, the test statistic needs to be modified.

### Zeros

Wilcoxon's original paper did not address the question of observations (or, in the paired sample case, differences) that equal zero. However, in later surveys, he recommended removing zeros from the sample. Then the standard signed-rank test could be applied to the resulting data, as long as there were no ties. This is now called the *reduced sample procedure.*

Pratt observed that the reduced sample procedure can lead to paradoxical behavior. He gives the following example. Suppose that we are in the one-sample situation and have the following thirteen observations:

0, 2, 3, 4, 6, 7, 8, 9, 11, 14, 15, 17, −18.

The reduced sample procedure removes the zero. To the remaining data, it assigns the signed ranks:

1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, −12.

This has a one-sided *p*-value of $55/2^{12}$ , and therefore the sample is not significantly positive at any significance level $\alpha <55/2^{12}\approx 0.0134$ . Pratt argues that one would expect that decreasing the observations should certainly not make the data appear more positive. However, if the zero observation is decreased by an amount less than 2, or if all observations are decreased by an amount less than 1, then the signed ranks become:

−1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, −13.

This has a one-sided *p*-value of $109/2^{13}$ . Therefore the sample would be judged significantly positive at any significance level $\alpha >109/2^{13}\approx 0.0133$ . The paradox is that, if $\alpha$ is between $109/2^{13}$ and $55/2^{12}$ , then *decreasing* an insignificant sample causes it to appear significantly *positive*.

Pratt therefore proposed the *signed-rank zero procedure.* This procedure includes the zeros when ranking the observations in the sample. However, it excludes them from the test statistic, or equivalently it defines $\operatorname {sgn}(0)=0$ . Pratt proved that the signed-rank zero procedure has several desirable behaviors not shared by the reduced sample procedure:

1. Increasing the observed values does not make a significantly positive sample insignificant, and it does not make an insignificant sample significantly negative.
2. If the distribution of the observations is symmetric, then the values of $\mu$ which the test does not reject form an interval.
3. A sample is significantly positive, not significant, or significantly negative, if and only if it is so when the zeros are assigned arbitrary non-zero signs, if and only if it is so when the zeros are replaced with non-zero values which are smaller in absolute value than any non-zero observation.
4. For a fixed significance threshold $\alpha$ , and for a test which is randomized to have level exactly $\alpha$ , the probability of calling a set of observations significantly positive (respectively, significantly negative) is a non-decreasing (respectively, non-increasing) function of the observations.

Pratt remarks that, when the signed-rank zero procedure is combined with the average rank procedure for resolving ties, the resulting test is a consistent test against the alternative hypothesis that, for all $i\neq j$ , $\Pr(X_{i}+X_{j}>0)$ and $\Pr(X_{i}+X_{j}<0)$ differ by at least a fixed constant that is independent of i and j .

The signed-rank zero procedure has the disadvantage that, when zeros occur, the null distribution of the test statistic changes, so tables of *p*-values can no longer be used.

When the data is on a Likert scale with equally spaced categories, the signed-rank zero procedure is more likely to maintain the Type I error rate than the reduced sample procedure.

From the viewpoint of statistical efficiency, there is no perfect rule for handling zeros. Conover found examples of null and alternative hypotheses that show that neither Wilcoxon's and Pratt's methods are uniformly better than the other. When comparing a discrete uniform distribution to a distribution where probabilities linearly increase from left to right, Pratt's method outperforms Wilcoxon's. When testing a binomial distribution centered at zero to see whether the parameter of each Bernoulli trial is ${\tfrac {1}{2}}$ , Wilcoxon's method outperforms Pratt's.

### Ties

When the data does not have ties, the ranks $R_{i}$ are used to calculate the test statistic. In the presence of ties, the ranks are not defined. There are two main approaches to resolving this.

The most common procedure for handling ties, and the one originally recommended by Wilcoxon, is called the *average rank* or *midrank procedure.* This procedure assigns numbers between 1 and *n* to the observations, with two observations getting the same number if and only if they have the same absolute value. These numbers are conventionally called ranks even though the set of these numbers is not equal to $\{1,\dots ,n\}$ (except when there are no ties). The rank assigned to an observation is the average of the possible ranks it would have if the ties were broken in all possible ways. Once the ranks are assigned, the test statistic is computed in the same way as usual.

For example, suppose that the observations satisfy $|X_{3}|<|X_{2}|=|X_{5}|<|X_{6}|<|X_{1}|=|X_{4}|=|X_{7}|.$ In this case, $X_{3}$ is assigned rank 1, $X_{2}$ and $X_{5}$ are assigned rank $(2+3)/2=2.5$ , $X_{6}$ is assigned rank 4, and $X_{1}$ , $X_{4}$ , and $X_{7}$ are assigned rank $(5+6+7)/3=6$ . Formally, suppose that there is a set of observations all having the same absolute value v , that $k-1$ observations have absolute value less than v , and that $\ell$ observations have absolute value less than or equal to v . If the ties among the observations with absolute value v were broken, then these observations would occupy ranks k through $\ell$ . The average rank procedure therefore assigns them the rank $(k+\ell )/2$ .

Under the average rank procedure, the null distribution is different in the presence of ties. The average rank procedure also has some disadvantages that are similar to those of the reduced sample procedure for zeros. It is possible that a sample can be judged significantly positive by the average rank procedure; but increasing some of the values so as to break the ties, or breaking the ties in any way whatsoever, results in a sample that the test judges to be not significant. However, increasing all the observed values by the same amount cannot turn a significantly positive result into an insignificant one, nor an insignificant one into a significantly negative one. Furthermore, if the observations are distributed symmetrically, then the values of $\mu$ which the test does not reject form an interval.

The other common option for handling ties is a tiebreaking procedure. In a tiebreaking procedure, the observations are assigned distinct ranks in the set $\{1,\dots ,n\}$ . The rank assigned to an observation depends on its absolute value and the tiebreaking rule. Observations with smaller absolute values are always given smaller ranks, just as in the standard rank-sum test. The tiebreaking rule is used to assign ranks to observations with the same absolute value. One advantage of tiebreaking rules is that they allow the use of standard tables for computing *p*-values.

*Random tiebreaking* breaks the ties at random. Under random tiebreaking, the null distribution is the same as when there are no ties, but the result of the test depends not only on the data but on additional random choices. Averaging the ranks over the possible random choices results in the average rank procedure. One could also report the probability of rejection over all random choices. Random tiebreaking has the advantage that the probability that a sample is judged significantly positive does not decrease when some observations are increased. *Conservative tiebreaking* breaks the ties in favor of the null hypothesis. When performing a one-sided test in which negative values of T tend to be more significant, ties are broken by assigning lower ranks to negative observations and higher ranks to positive ones. When the test makes positive values of T significant, ties are broken the other way, and when large absolute values of T are significant, ties are broken so as to make $|T|$ as small as possible. Pratt observes that when ties are likely, the conservative tiebreaking procedure "presumably has low power, since it amounts to breaking all ties in favor of the null hypothesis."

The average rank procedure can disagree with tiebreaking procedures. Pratt gives the following example. Suppose that the observations are:

1, 1, 1, 1, 2, 3, −4.

The average rank procedure assigns these the signed ranks

2.5, 2.5, 2.5, 2.5, 5, 6, −7.

This sample is significantly positive at the one-sided level $\alpha =14/2^{7}$ . On the other hand, any tiebreaking rule will assign the ranks

1, 2, 3, 4, 5, 6, −7.

At the same one-sided level $\alpha =14/2^{7}$ , this is not significant.

Two other options for handling ties are based around averaging the results of tiebreaking. In the *average statistic* method, the test statistic T is computed for every possible way of breaking ties, and the final statistic is the mean of the tie-broken statistics. In the *average probability* method, the *p*-value is computed for every possible way of breaking ties, and the final *p*-value is the mean of the tie-broken *p*-values.

## Computing the null distribution

Computing *p*-values requires knowing the distribution of T under the null hypothesis. There is no closed formula for this distribution. However, for small values of n , the distribution may be computed exactly. Under the null hypothesis that the data is symmetric about zero, each $X_{i}$ is exactly as likely to be positive as it is negative. Therefore the probability that $T=t$ under the null hypothesis is equal to the number of sign combinations that yield $T=t$ divided by the number of possible sign combinations $2^{n}$ . This can be used to compute the exact distribution of T under the null hypothesis.

Computing the distribution of T by considering all possibilities requires computing $2^{n}$ sums, which is intractable for all but the smallest n . However, there is an efficient recursion for the distribution of $T^{+}$ . Define $u_{n}(t^{+})$ to be the number of sign combinations for which $T^{+}=t^{+}$ . This is equal to the number of subsets of $\{1,\dots ,n\}$ which sum to $t^{+}$ . The base cases of the recursion are $u_{0}(0)=1$ , $u_{0}(t^{+})=0$ for all $t^{+}\neq 0$ , and $u_{n}(t^{+})=0$ for all $t<0$ or $t>n(n+1)/2$ . The recursive formula is $u_{n}(t^{+})=u_{n-1}(t^{+})+u_{n-1}(t^{+}-n).$ The formula is true because every subset of $\{1,\dots ,n\}$ which sums to $t^{+}$ either does not contain n , in which case it is also a subset of $\{1,\dots ,n-1\}$ , or it does contain n , in which case removing n from the subset produces a subset of $\{1,\dots ,n-1\}$ which sums to $t^{+}-n$ . Under the null hypothesis, the probability mass function of $T^{+}$ satisfies $\Pr(T^{+}=t^{+})=u_{n}(t^{+})/2^{n}$ . The function $u_{n}$ is closely related to the integer partition function.

If $p_{n}(t^{+})$ is the probability that $T^{+}=t^{+}$ under the null hypothesis when there are n observations in the sample, then $p_{n}(t^{+})$ satisfies a similar recursion: $2p_{n}(t^{+})=p_{n-1}(t^{+})+p_{n-1}(t^{+}-n)$ with similar boundary conditions. There is also a recursive formula for the cumulative distribution function $\Pr(T^{+}\leq t^{+})$ .

For very large n , even the above recursion is too slow. In this case, the null distribution can be approximated. The null distributions of T , $T^{+}$ , and $T^{-}$ are asymptotically normal with means and variances: ${\begin{aligned}\mathbf {E} [T^{+}]&=\mathbf {E} [T^{-}]={\frac {n(n+1)}{4}},\\\mathbf {E} [T]&=0,\\\operatorname {Var} (T^{+})&=\operatorname {Var} (T^{-})={\frac {n(n+1)(2n+1)}{24}},\\\operatorname {Var} (T)&={\frac {n(n+1)(2n+1)}{6}}.\end{aligned}}$

Better approximations can be produced using Edgeworth expansions. Using a fourth-order Edgeworth expansion shows that: $\Pr(T^{+}\leq k)\approx \Phi (t)+\phi (t){\Big (}{\frac {3n^{2}+3n-1}{10n(n+1)(2n+1)}}{\Big )}(t^{3}-3t),$ where $t={\frac {k+{\tfrac {1}{2}}-{\frac {n(n+1)}{4}}}{\sqrt {\frac {n(n+1)(2n+1)}{24}}}}.$ The technical underpinnings of these expansions are rather involved, because conventional Edgeworth expansions apply to sums of IID continuous random variables, while $T^{+}$ is a sum of non-identically distributed discrete random variables. The final result, however, is that the above expansion has an error of $O(n^{-3/2})$ , just like a conventional fourth-order Edgeworth expansion.

The moment generating function of T has the exact formula: $M(t)={\frac {1}{2^{n}}}\prod _{j=1}^{n}(1+e^{jt}).$

When zeros are present and the signed-rank zero procedure is used, or when ties are present and the average rank procedure is used, the null distribution of T changes. Cureton derived a normal approximation for this situation. Suppose that the original number of observations was n and the number of zeros was z . The tie correction is $c=\sum t^{3}-t,$ where the sum is over all the sizes t of each group of tied observations. The expectation of T is still zero, while the expectation of $T^{+}$ is $\mathbf {E} [T^{+}]={\frac {n(n+1)}{4}}-{\frac {z(z+1)}{4}}.$ If $\sigma ^{2}={\frac {n(n+1)(2n+1)-z(z+1)(2z+1)-c/2}{6}},$ then ${\begin{aligned}\operatorname {Var} (T)&=\sigma ^{2},\\\operatorname {Var} (T^{+})&=\sigma ^{2}/4.\end{aligned}}$

## Alternative statistics

Wilcoxon originally defined the Wilcoxon rank-sum statistic to be $\min(T^{+},T^{-})$ . Early authors such as Siegel followed Wilcoxon. This is appropriate for two-sided hypothesis tests, but it cannot be used for one-sided tests.

Instead of assigning ranks between 1 and *n*, it is also possible to assign ranks between 0 and $n-1$ . These are called *modified ranks*. The modified signed-rank sum $T_{0}$ , the modified positive-rank sum $T_{0}^{+}$ , and the modified negative-rank sum $T_{0}^{-}$ are defined analogously to T , $T^{+}$ , and $T^{-}$ but with the modified ranks in place of the ordinary ranks. The probability that the sum of two independent F -distributed random variables is positive can be estimated as $2T_{0}^{+}/(n(n-1))$ . When consideration is restricted to continuous distributions, this is a minimum variance unbiased estimator of $p_{2}$ .

## Example

| i $x_{2,i}$ $x_{1,i}$ $x_{2,i}-x_{1,i}$ $\operatorname {sgn}$ $\operatorname {abs}$ 1 125 110 1 15 2 115 122  –1 7 3 130 125 1 5 4 140 120 1 20 5 140 140   0 6 115 124  –1 9 7 140 123 1 17 8 125 137  –1 12 9 140 135 1 5 10 135 145  –1 10 | order by absolute difference | i $x_{2,i}$ $x_{1,i}$ $x_{2,i}-x_{1,i}$ $\operatorname {sgn}$ ${\text{abs}}$ $R_{i}$ $\operatorname {sgn} \cdot R_{i}$ 5 140 140   0     3 130 125 1 5 1.5 1.5 9 140 135 1 5 1.5 1.5 2 115 122  –1 7 3  –3 6 115 124  –1 9 4  –4 10 135 145  –1 10 5  –5 8 125 137  –1 12 6  –6 1 125 110 1 15 7 7 7 140 123 1 17 8 8 4 140 120 1 20 9 9 |
|---|---|---|

$\operatorname {sgn}$ is the sign function, $\operatorname {abs}$ is the absolute value, and $R_{i}$ is the rank. Notice that pairs 3 and 9 are tied in absolute value. They would be ranked 1 and 2, so each gets the average of those ranks, 1.5.

$W=1.5+1.5-3-4-5-6+7+8+9=9$

$|W|<W_{\operatorname {crit} (\alpha =0.05,\ 9{\text{, two-sided}})}=15$

$\therefore {\text{failed to reject }}H_{0}$

that the median of pairwise differences is different from zero.

The

p

-value for this result is

$0.6113$

## Effect size

To compute an effect size for the signed-rank test, one can use the rank-biserial correlation.

If the test statistic *T* is reported, the rank correlation r is equal to the test statistic *T* divided by the total rank sum *S*, or *r* = *T*/*S*. Using the above example, the test statistic is *T* = 9. The sample size of 9 has a total rank sum of *S* = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9) = 45. Hence, the rank correlation is 9/45, so *r* = 0.20.

If the test statistic *T* is reported, an equivalent way to compute the rank correlation is with the difference in proportion between the two rank sums, which is the Kerby (2014) simple difference formula. To continue with the current example, the sample size is 9, so the total rank sum is 45. *T* is the smaller of the two rank sums, so *T* is 3 + 4 + 5 + 6 = 18. From this information alone, the remaining rank sum can be computed, because it is the total sum *S* minus *T*, or in this case 45 − 18 = 27. Next, the two rank-sum proportions are 27/45 = 60% and 18/45 = 40%. Finally, the rank correlation is the difference between the two proportions (.60 minus .40), hence *r* = .20.

## Software implementations

- R includes an implementation of the test as `wilcox.test(x,y, paired=TRUE)`, where x and y are vectors of equal length.
- ALGLIB includes implementation of the Wilcoxon signed-rank test in C++, C#, Delphi, Visual Basic, etc.
- GNU Octave implements various one-tailed and two-tailed versions of the test in the `wilcoxon_test` function.
- SciPy includes an implementation of the Wilcoxon signed-rank test in Python.
- Accord.NET includes an implementation of the Wilcoxon signed-rank test in C# for .NET applications.
- MATLAB implements this test using "Wilcoxon rank sum test" as `[p,h] = signrank(x,y)` also returns a logical value indicating the test decision. The result h = 1 indicates a rejection of the null hypothesis, and h = 0 indicates a failure to reject the null hypothesis at the 5% significance level.
- Julia HypothesisTests package includes the Wilcoxon signed-rank test as `value(SignedRankTest(x, y))`.
- SAS PROC UNIVARIATE includes the Wilcoxon-Signed Rank Test in the frame titles "Tests for Location" as "Signed Rank". Even though this procedure calculates an S-Statistic rather than a W-Statistic, the resulting p-value can still be used for this test. Also SAS with PROC NPAR1WAY contains many non-parametric test and also sports exact test using a bayesian mcmc approach.
  - SAS Documentation
