---
title: "Kendall rank correlation coefficient"
source: https://en.wikipedia.org/wiki/Kendall_rank_correlation_coefficient
domain: nonparametric-tests
license: CC-BY-SA-4.0
tags: nonparametric statistics, rank correlation, sign test, Spearman correlation
fetched: 2026-07-02
---

# Kendall rank correlation coefficient

In statistics, the **Kendall rank correlation coefficient**, commonly referred to as **Kendall's τ coefficient** (after the Greek letter τ, tau), is a statistic used to measure the ordinal association between two measured quantities. A **τ test** is a non-parametric hypothesis test for statistical dependence based on the τ coefficient. It is a measure of rank correlation: the similarity of the orderings of the data when ranked by each of the quantities. It is named after Maurice Kendall, who developed it in 1938, though Gustav Fechner had proposed a similar measure in the context of time series in 1897.

Intuitively, the Kendall correlation between two variables will be high when observations have a similar or identical rank (i.e. relative position label of the observations within the variable: 1st, 2nd, 3rd, etc.) between the two variables, and low when observations have a dissimilar or fully reversed rank between the two variables.

Both Kendall's $\tau$ and Spearman's $\rho$ can be formulated as special cases of a more general correlation coefficient. Its notions of concordance and discordance also appear in other areas of statistics, like the Rand index in cluster analysis.

## Definition

Let $(x_{1},y_{1}),...,(x_{n},y_{n})$ be a set of observations of the joint random variables *X* and *Y*, such that all the values of ( $x_{i}$ ) and ( $y_{i}$ ) are unique. (See the section Accounting for ties for ways of handling non-unique values.) Any pair of observations $(x_{i},y_{i})$ and $(x_{j},y_{j})$ , where $i<j$ , are said to be *concordant* if the sort order of $(x_{i},x_{j})$ and *$(y_{i},y_{j})$* agrees: that is, if either both $x_{i}>x_{j}$ and $y_{i}>y_{j}$ holds or both $x_{i}<x_{j}$ and $y_{i}<y_{j}$ ; otherwise they are said to be *discordant*.

In the absence of ties, the Kendall τ coefficient is defined as:

$\tau ={\frac {({\text{number of concordant pairs}})-({\text{number of discordant pairs}})}{({\text{number of pairs}})}}=1-{\frac {2({\text{number of discordant pairs}})}{n \choose 2}}.$

for $i<j<n$ where ${n \choose 2}={n(n-1) \over 2}$ is the binomial coefficient for the number of ways to choose two items from n items.

The number of discordant pairs is equal to the inversion number that permutes the y-sequence into the same order as the x-sequence.

### Properties

The denominator is the total number of pair combinations, so the coefficient must be in the range −1 ≤ *τ* ≤ 1.

- If the agreement between the two rankings is perfect (i.e., the two rankings are the same) the coefficient has value 1.
- If the disagreement between the two rankings is perfect (i.e., one ranking is the reverse of the other) the coefficient has value −1.
- If *X* and *Y* are independent random variables and not constant, then the expectation of the coefficient is zero.
- An explicit expression for Kendall's rank coefficient is $\tau ={\frac {2}{n(n-1)}}\sum _{i<j}\operatorname {sgn}(x_{i}-x_{j})\operatorname {sgn}(y_{i}-y_{j})$ .

## Hypothesis test

The Kendall rank coefficient is often used as a test statistic in a statistical hypothesis test to establish whether two variables may be regarded as statistically dependent. This test is non-parametric, as it does not rely on any assumptions on the distributions of *X* or *Y* or the distribution of (*X*,*Y*).

Under the null hypothesis of independence of *X* and *Y*, the sampling distribution of *τ* has an expected value of zero. The precise distribution cannot be characterized in terms of common distributions, but may be calculated exactly for small samples; for larger samples, it is common to use an approximation to the normal distribution, with mean zero and variance ${\textstyle 2(2n+5)/9n(n-1)}$ .

**Theorem.** If the samples are independent, then the variance of ${\textstyle \tau _{A}}$ is given by ${\textstyle Var[\tau _{A}]=2(2n+5)/9n(n-1)}$ .

Proof

Proof

Valz & McLeod (1990;

1995

)

WLOG, we reorder the data pairs, so that ${\textstyle x_{1}<x_{2}<\cdots <x_{n}}$ . By assumption of independence, the order of ${\textstyle y_{1},...,y_{n}}$ is a permutation sampled uniformly at random from ${\textstyle S_{n}}$ , the permutation group on ${\textstyle 1:n}$ .

For each permutation, its unique ${\textstyle l}$ inversion code is ${\textstyle l_{0}l_{1}\cdots l_{n-1}}$ such that each ${\textstyle l_{i}}$ is in the range ${\textstyle 0:i}$ . Sampling a permutation uniformly is equivalent to sampling a ${\textstyle l}$ -inversion code uniformly, which is equivalent to sampling each ${\textstyle l_{i}}$ uniformly and independently.

Then we have ${\begin{aligned}E[\tau _{A}^{2}]&=E\left[\left(1-{\frac {4\sum _{i}l_{i}}{n(n-1)}}\right)^{2}\right]\\&=1-{\frac {8}{n(n-1)}}\sum _{i}E[l_{i}]+{\frac {16}{n^{2}(n-1)^{2}}}\sum _{ij}E[l_{i}l_{j}]\\&=1-{\frac {8}{n(n-1)}}\sum _{i}E[l_{i}]+{\frac {16}{n^{2}(n-1)^{2}}}\left(\sum _{ij}E[l_{i}]E[l_{j}]+\sum _{i}V[l_{i}]\right)\\&=1-{\frac {8}{n(n-1)}}\sum _{i}E[l_{i}]+{\frac {16}{n^{2}(n-1)^{2}}}\sum _{ij}E[l_{i}]E[l_{j}]+{\frac {16}{n^{2}(n-1)^{2}}}\left(\sum _{i}V[l_{i}]\right)\\&=\left(1-{\frac {4\sum _{i}E[l_{i}]}{n(n-1)}}\right)^{2}+{\frac {16}{n^{2}(n-1)^{2}}}\left(\sum _{i}V[l_{i}]\right)\end{aligned}}$

The first term is just ${\textstyle E[\tau _{A}]^{2}=0}$ . The second term can be calculated by noting that ${\textstyle l_{i}}$ is a uniform random variable on ${\textstyle 0:i}$ , so ${\textstyle E[l_{i}]={\frac {i}{2}}}$ and ${\textstyle E[l_{i}^{2}]={\frac {0^{2}+\cdots +i^{2}}{i+1}}={\frac {i(2i+1)}{6}}}$ , then using the sum of squares formula again.

**Asymptotic normality**—At the ${\textstyle n\to \infty }$ limit, ${\textstyle z_{A}={\frac {\tau _{A}}{\sqrt {Var[\tau _{A}]}}}={n_{C}-n_{D} \over {\sqrt {n(n-1)(2n+5)/18}}}}$ converges in distribution to the standard normal distribution.

Proof

Use a result from *A class of statistics with asymptotically normal distribution* Hoeffding (1948).

## Case of standard normal distributions

If ${\textstyle (x_{1},y_{1}),(x_{2},y_{2}),...,(x_{n},y_{n})}$ are independent and identically distributed samples from the same jointly normal distribution with a known Pearson correlation coefficient ${\textstyle r}$ , then the expectation of Kendall rank correlation has a closed-form formula.

**Greiner's equality**—If ${\textstyle X,Y}$ are jointly normal, with correlation ${\textstyle r}$ , then $r=\sin {\left({\frac {\pi }{2}}E[\tau _{A}]\right)}$

The name is credited to Richard Greiner (1909) by P. A. P. Moran.

Proof

Proof

Define the following quantities.

- ${\textstyle A^{+}:=\{(\Delta x,\Delta y):\Delta x\Delta y>0\}}$
- ${\textstyle \Delta _{i,j}:=(x_{i}-x_{j},y_{i}-y_{j})}$ is a point in ${\textstyle \mathbb {R} ^{2}}$ .

In the notation, we see that the number of concordant pairs, ${\textstyle n_{C}}$ , is equal to the number of ${\textstyle \Delta _{i,j}}$ that fall in the subset ${\textstyle A^{+}}$ . That is, ${\textstyle n_{C}=\sum _{1\leq i<j\leq n}1_{\Delta _{i,j}\in A^{+}}}$ .

Thus, $E[\tau _{A}]={\frac {4}{n(n-1)}}E[n_{C}]-1={\frac {4}{n(n-1)}}\sum _{1\leq i<j\leq n}Pr(\Delta _{i,j}\in A^{+})-1$

Since each ${\textstyle (x_{i},y_{i})}$ is an independent and identically distributed sample of the jointly normal distribution, the pairing does not matter, so each term in the summation is exactly the same, and so $E[\tau _{A}]=2Pr(\Delta _{1,2}\in A^{+})-1$ and it remains to calculate the probability. We perform this by repeated affine transforms.

First normalize ${\textstyle X,Y}$ by subtracting the mean and dividing the standard deviation. This does not change ${\textstyle \tau _{A}}$ . This gives us ${\begin{bmatrix}x\\y\end{bmatrix}}={\begin{bmatrix}1&r\\r&1\end{bmatrix}}^{1/2}{\begin{bmatrix}z\\w\end{bmatrix}}$ where ${\textstyle (Z,W)}$ is sampled from the standard normal distribution on ${\textstyle \mathbb {R} ^{2}}$ .

Thus, $\Delta _{1,2}={\sqrt {2}}{\begin{bmatrix}1&r\\r&1\end{bmatrix}}^{1/2}{\begin{bmatrix}(z_{1}-z_{2})/{\sqrt {2}}\\(w_{1}-w_{2})/{\sqrt {2}}\end{bmatrix}}$ where the vector ${\textstyle {\begin{bmatrix}(z_{1}-z_{2})/{\sqrt {2}}\\(w_{1}-w_{2})/{\sqrt {2}}\end{bmatrix}}}$ is still distributed as the standard normal distribution on ${\textstyle \mathbb {R} ^{2}}$ . It remains to perform some unenlightening tedious matrix exponentiations and trigonometry, which can be skipped over.

Thus, ${\textstyle \Delta _{1,2}\in A^{+}}$ iff ${\begin{bmatrix}(z_{1}-z_{2})/{\sqrt {2}}\\(w_{1}-w_{2})/{\sqrt {2}}\end{bmatrix}}\in {\frac {1}{\sqrt {2}}}{\begin{bmatrix}1&r\\r&1\end{bmatrix}}^{-1/2}A^{+}={\frac {1}{2{\sqrt {2}}}}{\begin{bmatrix}{\frac {1}{\sqrt {1+r}}}+{\frac {1}{\sqrt {1-r}}}&{\frac {1}{\sqrt {1+r}}}-{\frac {1}{\sqrt {1-r}}}\\{\frac {1}{\sqrt {1+r}}}-{\frac {1}{\sqrt {1-r}}}&{\frac {1}{\sqrt {1+r}}}+{\frac {1}{\sqrt {1-r}}}\end{bmatrix}}A^{+}$ where the subset on the right is a “squashed” version of two quadrants. Since the standard normal distribution is rotationally symmetric, we need only calculate the angle spanned by each squashed quadrant.

The first quadrant is the sector bounded by the two rays ${\textstyle (1,0),(0,1)}$ . It is transformed to the sector bounded by the two rays ${\textstyle ({\frac {1}{\sqrt {1+r}}}+{\frac {1}{\sqrt {1-r}}},{\frac {1}{\sqrt {1+r}}}-{\frac {1}{\sqrt {1-r}}})}$ and ${\textstyle ({\frac {1}{\sqrt {1+r}}}-{\frac {1}{\sqrt {1-r}}},{\frac {1}{\sqrt {1+r}}}+{\frac {1}{\sqrt {1-r}}})}$ . They respectively make angle ${\textstyle \theta }$ with the horizontal and vertical axis, where $\theta =\arctan {\frac {{\frac {1}{\sqrt {1+r}}}-{\frac {1}{\sqrt {1-r}}}}{{\frac {1}{\sqrt {1+r}}}+{\frac {1}{\sqrt {1-r}}}}}$

Together, the two transformed quadrants span an angle of ${\textstyle \pi +4\theta }$ , so $Pr(\Delta _{1,2}\in A^{+})={\frac {\pi +4\theta }{2\pi }}$ and therefore $\sin {\left({\frac {\pi }{2}}E[\tau _{A}]\right)}=\sin(2\theta )=r$

## Accounting for ties

A pair $\{(x_{i},y_{i}),(x_{j},y_{j})\}$ is said to be *tied* if and only if $x_{i}=x_{j}$ or $y_{i}=y_{j}$ ; a tied pair is neither concordant nor discordant. When tied pairs arise in the data, the coefficient may be modified in a number of ways to keep it in the range [−1, 1]:

### Tau-a

The Tau statistic defined by Kendall in 1938 was retrospectively renamed Tau-a. It represents the strength of positive or negative association of two quantitative or ordinal variables without any adjustment for ties. It is defined as:

$\tau _{A}={\frac {n_{c}-n_{d}}{n_{0}}}$

where *n**c*, *n**d* and *n**0* are defined as in the next section.

When ties are present, $n_{c}+n_{d}<n_{0}$ , and the coefficient can never be equal to +1 or −1. Even a perfect equality of the two variables (X=Y) leads to a Tau-a < 1.

### Tau-b

The Tau-b statistic, unlike Tau-a, makes adjustments for ties. This Tau-b was first described by Kendall in 1945 under the name Tau-w as an extension of the original Tau statistic supporting ties. Values of Tau-b range from −1 (100% negative association, or perfect disagreement) to +1 (100% positive association, or perfect agreement). In case of the absence of association, Tau-b is equal to zero.

The Kendall Tau-b coefficient is defined as :

$\tau _{B}={\frac {n_{c}-n_{d}}{\sqrt {(n_{0}-n_{1})(n_{0}-n_{2})}}}$

where

${\begin{aligned}n_{0}&=n(n-1)/2\\n_{1}&=\sum _{i}t_{i}(t_{i}-1)/2\\n_{2}&=\sum _{j}u_{j}(u_{j}-1)/2\\n_{c}&={\text{Number of concordant pairs, i.e. pairs with }}0<i<j<n{\text{ where }}x_{i}<x_{j}{\text{ and }}y_{i}<y_{j}{\text{ or }}x_{i}>x_{j}{\text{ and }}y_{i}>y_{j}\\n_{d}&={\text{Number of discordant pairs, i.e. pairs where }}0<i<j<n{\text{ where }}x_{i}<x_{j}{\text{ and }}y_{i}>y_{j}{\text{ or }}x_{i}>x_{j}{\text{ and }}y_{i}<y_{j}\\t_{i}&={\text{Number of tied values in the }}i^{\text{th}}{\text{ group of ties for the empirical distribution of X}}\\u_{j}&={\text{Number of tied values in the }}j^{\text{th}}{\text{ group of ties for the empirical distribution of Y}}\end{aligned}}$

A simple algorithm developed in BASIC computes Tau-b coefficient using an alternative formula.

Be aware that some statistical packages, e.g. SPSS, use alternative formulas for computational efficiency, with double the 'usual' number of concordant and discordant pairs.

### Tau-c

Tau-c (also called Stuart-Kendall Tau-c) was first defined by Stuart in 1953. Contrary to Tau-b, Tau-c can be equal to +1 or −1 for non-square (i.e. rectangular) contingency tables, i.e. when the underlying scales of both variables have different number of possible values. For instance, if the variable X has a continuous uniform distribution between 0 and 100 and Y is a dichotomous variable equal to 1 if X ≥ 50 and 0 if X < 50, the Tau-c statistic of X and Y is equal to 1 while Tau-b is equal to 0.707. A Tau-c equal to 1 can be interpreted as the best possible positive correlation conditional to marginal distributions while a Tau-b equal to 1 can be interpreted as the perfect positive monotonic correlation where the distribution of X conditional to Y has zero variance and the distribution of Y conditional to X has zero variance so that a bijective function f with f(X)=Y exists.

The Stuart-Kendall Tau-c coefficient is defined as:

$\tau _{C}={\frac {2(n_{c}-n_{d})}{n^{2}{\frac {(m-1)}{m}}}}=\tau _{A}{\frac {n-1}{n}}{\frac {m}{m-1}}$

where

${\begin{aligned}n_{c}&={\text{Number of concordant pairs}}\\n_{d}&={\text{Number of discordant pairs}}\\r&={\text{Number of rows of the contingency table (i.e. number of distinct }}x_{i}{\text{)}}\\c&={\text{Number of columns of the contingency table (i.e. number of distinct }}y_{i}{\text{)}}\\m&=\min(r,c)\end{aligned}}$

## Significance tests

When two quantities are statistically dependent, the distribution of $\tau$ is not easily characterizable in terms of known distributions. However, for $\tau _{A}$ the following statistic, $z_{A}$ , is approximately distributed as a standard normal when the variables are statistically independent:

$z_{A}={n_{c}-n_{d} \over {\sqrt {{\frac {1}{18}}v_{0}}}}$

where $v_{0}=n(n-1)(2n+5)$ .

Thus, to test whether two variables are statistically dependent, one computes $z_{A}$ , and finds the cumulative probability for a standard normal distribution at $-|z_{A}|$ . For a 2-tailed test, multiply that number by two to obtain the *p*-value. If the *p*-value is below a given significance level, one rejects the null hypothesis (at that significance level) that the quantities are statistically independent.

Numerous adjustments should be added to $z_{A}$ when accounting for ties. The following statistic, $z_{B}$ , has the same distribution as the $\tau _{B}$ distribution, and is again approximately equal to a standard normal distribution when the quantities are statistically independent:

$z_{B}={n_{c}-n_{d} \over {\sqrt {v}}}$

where

${\begin{array}{ccl}v&=&{\frac {1}{18}}v_{0}-(v_{t}+v_{u})/18+(v_{1}+v_{2})\\v_{0}&=&n(n-1)(2n+5)\\v_{t}&=&\sum _{i}t_{i}(t_{i}-1)(2t_{i}+5)\\v_{u}&=&\sum _{j}u_{j}(u_{j}-1)(2u_{j}+5)\\v_{1}&=&\sum _{i}t_{i}(t_{i}-1)\sum _{j}u_{j}(u_{j}-1)/(2n(n-1))\\v_{2}&=&\sum _{i}t_{i}(t_{i}-1)(t_{i}-2)\sum _{j}u_{j}(u_{j}-1)(u_{j}-2)/(9n(n-1)(n-2))\end{array}}$

This is sometimes referred to as the Mann-Kendall test.

## Algorithms

The direct computation of the numerator $n_{c}-n_{d}$ , involves two nested iterations, as characterized by the following pseudocode:

```
numer := 0
for i := 2..N do
    for j := 1..(i − 1) do
        numer := numer + sign(x[i] − x[j]) × sign(y[i] − y[j])
return numer
```

Although quick to implement, this algorithm is $O(n^{2})$ in complexity and becomes very slow on large samples. A more sophisticated algorithm built upon the Merge Sort algorithm can be used to compute the numerator in $O(n\cdot \log {n})$ time.

Begin by ordering your data points sorting by the first quantity, x , and secondarily (among ties in x ) by the second quantity, y . With this initial ordering, y is not sorted, and the core of the algorithm consists of computing how many steps a Bubble Sort would take to sort this initial y . An enhanced Merge Sort algorithm, with $O(n\log n)$ complexity, can be applied to compute the number of swaps, $S(y)$ , that would be required by a Bubble Sort to sort $y_{i}$ . Then the numerator for $\tau$ is computed as:

$n_{c}-n_{d}=n_{0}-n_{1}-n_{2}+n_{3}-2S(y),$

where $n_{3}$ is computed like $n_{1}$ and $n_{2}$ , but with respect to the joint ties in x and y .

A Merge Sort partitions the data to be sorted, y into two roughly equal halves, $y_{\mathrm {left} }$ and $y_{\mathrm {right} }$ , then sorts each half recursively, and then merges the two sorted halves into a fully sorted vector. The number of Bubble Sort swaps is equal to:

$S(y)=S(y_{\mathrm {left} })+S(y_{\mathrm {right} })+M(Y_{\mathrm {left} },Y_{\mathrm {right} })$

where $Y_{\mathrm {left} }$ and $Y_{\mathrm {right} }$ are the sorted versions of $y_{\mathrm {left} }$ and $y_{\mathrm {right} }$ , and $M(\cdot ,\cdot )$ characterizes the Bubble Sort swap-equivalent for a merge operation. $M(\cdot ,\cdot )$ is computed as depicted in the following pseudo-code:

```
function M(L[1..n], R[1..m]) is
    i := 1
    j := 1
    nSwaps := 0
    while i ≤ n and j ≤ m do
        if R[j] < L[i] then
            nSwaps := nSwaps + n − i + 1
            j := j + 1
        else
            i := i + 1
    return nSwaps
```

A side effect of the above steps is that you end up with both a sorted version of x and a sorted version of y . With these, the factors $t_{i}$ and $u_{j}$ used to compute $\tau _{B}$ are easily obtained in a single linear-time pass through the sorted arrays.

## Approximating Kendall rank correlation from a stream

Efficient algorithms for calculating the Kendall rank correlation coefficient as per the standard estimator have $O(n\cdot \log {n})$ time complexity. However, these algorithms necessitate the availability of all data to determine observation ranks, posing a challenge in sequential data settings where observations are revealed incrementally. Fortunately, algorithms do exist to estimate the Kendall rank correlation coefficient in sequential settings. These algorithms have $O(1)$ update time and space complexity, scaling efficiently with the number of observations. Consequently, when processing a batch of n observations, the time complexity becomes $O(n)$ , while space complexity remains a constant $O(1)$ .

The first such algorithm presents an approximation to the Kendall rank correlation coefficient based on coarsening the joint distribution of the random variables. Non-stationary data is treated via a moving window approach. This algorithm is simple and is able to handle discrete random variables along with continuous random variables without modification.

The second algorithm is based on Hermite series estimators and utilizes an alternative estimator for the exact Kendall rank correlation coefficient i.e. for the probability of concordance minus the probability of discordance of pairs of bivariate observations. This alternative estimator also serves as an approximation to the standard estimator. This algorithm is only applicable to continuous random variables, but it has demonstrated superior accuracy and potential speed gains compared to the first algorithm described, along with the capability to handle non-stationary data without relying on sliding windows. An efficient implementation of the Hermite series based approach is contained in the R package package hermiter.

## Software implementations

- R implements the test for $\tau _{B}$ `cor.test(x, y, method = "kendall")` in its "stats" package (also `cor(x, y, method = "kendall")` will work, but the latter does not return the p-value). All three versions of the coefficient are available in the "DescTools" package along with the confidence intervals: `KendallTauA(x,y,conf.level=0.95)` for $\tau _{A}$ , `KendallTauB(x,y,conf.level=0.95)` for $\tau _{B}$ , `StuartTauC(x,y,conf.level=0.95)` for $\tau _{C}$ . Fast batch estimates of the Kendall rank correlation coefficient along with sequential estimates are provided for in the package hermiter.
- For Python, the SciPy library implements the computation of $\tau _{B}$ in `scipy.stats.kendalltau`
- In Stata is implemented as `ktau *varlist*`.
