---
title: "Percentile"
source: https://en.wikipedia.org/wiki/Percentile
domain: exemplars-metrics
license: CC-BY-SA-4.0
tags: metric exemplar, trace to metric link, histogram exemplar, high resolution sample
fetched: 2026-07-02
---

# Percentile

In statistics, a **percentile** or **percentile score**, also known as **centile** (often denoted as $P_{k}$ or Pk, for a given percentage *k*), is a score greater than a given percentage of all scores (or data point value) in a sample. I.e., a score in the *k*-th percentile would be above approximately *k*% of all scores in its sample. For example, the 97th percentile (P97) is the value such that 97% of the data points are less than it.

Percentiles are a type of quantiles, obtained by a subdivision into 100 groups. The 25th percentile (P25) is also known as the first *quartile* (*Q*1), the 50th percentile (P50) as the *median* or second quartile (*Q*2), and the 75th percentile (P75) as the third quartile (*Q*3). For example, the 50th percentile (median) is the score *below* (or *at or below*, depending on the definition) which 50% of the scores in the distribution are found.

Percentiles are expressed in the same unit of measurement as the input scores, *not* in percent; for example, if the scores refer to human weight, the corresponding percentiles will be expressed in kilograms or pounds. In the limit of an infinite sample size, the percentile approximates the *percentile function*, the inverse of the cumulative distribution function.

A related quantity is the *percentile rank* of a given score, expressed as a percentage, which represents the fraction of scores in its distribution that are less than it, an exclusive definition. Percentile scores and percentile ranks are often used in the reporting of test scores from norm-referenced tests, but, as just noted, they are not the same. For percentile ranks, a score is given and a percentage is computed. Percentile ranks are exclusive: if the percentile rank for a specified score is 90%, then 90% of the scores were lower. In contrast, for percentiles a percentage is given and a corresponding score is determined, which can be either exclusive or inclusive. The score for a specified percentage (e.g., 90th) indicates a score below which (exclusive definition) or at or below which (inclusive definition) other scores in the distribution fall.

## Definitions

There is no standard definition of percentile; however, all definitions yield similar results when the number of observations is very large and the probability distribution is continuous. In the limit, as the sample size approaches infinity, the 100*p*th percentile (0<*p*<1) approximates the inverse of the cumulative distribution function (CDF) thus formed, evaluated at *p*, as *p* approximates the CDF. This can be seen as a consequence of the Glivenko–Cantelli theorem. Some methods for calculating the percentiles are given below.

## In the normal distribution

The methods given in the *calculation methods* section (below) are approximations for use in small-sample statistics. In general terms, for very large populations following a normal distribution, percentiles may often be represented by reference to a normal curve plot. The normal distribution is plotted along an axis scaled to standard deviations, or sigma ( $\sigma$ ) units. Mathematically, the normal distribution extends to negative infinity on the left and positive infinity on the right. Note, however, that only a very small proportion of individuals in a population will fall outside the −3*σ* to +3*σ* range. For example, with human heights very few people are above the +3*σ* height level.

Percentiles represent the area under the normal curve, increasing from left to right. Each standard deviation represents a fixed percentile. Thus, rounding to two decimal places, −3*σ* is the 0.13th percentile, −2*σ* the 2.28th percentile, −1*σ* the 15.87th percentile, 0*σ* the 50th percentile (both the mean and median of the distribution), +1*σ* the 84.13rd percentile, +2*σ* the 97.72nd percentile, and +3*σ* the 99.87th percentile. This is related to the 68–95–99.7 rule or the three-sigma rule. Note that in theory the 0th percentile falls at negative infinity and the 100th percentile at positive infinity, although in many practical applications, such as test results, natural lower and/or upper limits are enforced.

## Applications

When Internet service provider bill "burstable" internet bandwidth, the 95th or 98th percentile usually cuts off the top 5% or 2% of bandwidth peaks in each month, and then bills at the nearest rate. In this way, infrequent peaks are ignored, and the customer is charged in a fairer way. The reason this statistic is so useful in measuring data throughput is that it gives a very accurate picture of the cost of the bandwidth. The 95th percentile says that 95% of the time, the usage is below this amount: so, the remaining 5% of the time, the usage is above that amount.

Physicians will often use infant and children's weight and height to assess their growth in comparison to national median and other percentiles which are found in growth charts.

The 85th percentile speed of traffic on a road is often used as a guideline in setting speed limits and assessing whether such a limit is too high or low.

In finance, value at risk is a standard measure to assess (in a model-dependent way) the quantity under which the value of the portfolio is not expected to sink within a given period of time and given a confidence value.

## Calculation methods

Interpolated and nearest-rank, exclusive and inclusive, percentiles for 10-score distribution

There are many formulas or algorithms for a percentile score. Hyndman and Fan identified nine and most statistical and spreadsheet software use one of the methods they describe. Algorithms either return the value of a score that exists in the set of scores (nearest-rank methods) or interpolate between existing scores and are either exclusive or inclusive.

| PC: percentile specified | 0.10 | 0.25 | 0.50 | 0.75 | 0.90 |
|---|---|---|---|---|---|
| N: Number of scores | 10 | 10 | 10 | 10 | 10 |
| OR: ordinal rank = PC × N | 1 | 2.5 | 5 | 7.5 | 9 |
| Rank: >OR / ≥OR | 2/1 | 3/3 | 6/5 | 8/8 | 10/9 |
| Score at rank (exc/inc) | 2/1 | 3/3 | 4/3 | 5/5 | 7/5 |

The figure shows a 10-score distribution, illustrates the percentile scores that result from these different algorithms, and serves as an introduction to the examples given subsequently. The simplest are nearest-rank methods that return a score from the distribution, although compared to interpolation methods, results can be a bit crude. The Nearest-Rank Methods table shows the computational steps for exclusive and inclusive methods.

| PC: percentile specified | 0.10 | 0.25 | 0.50 | 0.75 | 0.90 |
|---|---|---|---|---|---|
| N: number of scores | 10 | 10 | 10 | 10 | 10 |
| OR: PC×(N+1) / PC×(N−1)+1 | 1.1/1.9 | 2.75/3.25 | 5.5/5.5 | 8.25/7.75 | 9.9/9.1 |
| LoRank: OR truncated | 1/1 | 2/3 | 5/5 | 8/7 | 9/9 |
| HIRank: OR rounded up | 2/2 | 3/4 | 6/6 | 9/8 | 10/10 |
| LoScore: score at LoRank | 1/1 | 2/3 | 3/3 | 5/4 | 5/5 |
| HiScore: score at HiRank | 2/2 | 3/3 | 4/4 | 5/5 | 7/7 |
| Difference: HiScore − LoScore | 1/1 | 1/0 | 1/1 | 0/1 | 2/2 |
| Mod: fractional part of OR | 0.1/0.9 | 0.75/0.25 | 0.5/0.5 | 0.25/0.75 | 0.9/0.1 |
| Interpolated score (exc/inc) = LoScore + Mod × Difference | 1.1/1.9 | 2.75/3 | 3.5/3.5 | 5/4.75 | 6.8/5.2 |

Interpolation methods, as the name implies, can return a score that is between scores in the distribution. Algorithms used by statistical programs typically use interpolation methods, for example, the percentile.exc and percentile.inc functions in Microsoft Excel. The Interpolated Methods table shows the computational steps.

### The nearest-rank method

One definition of percentile, often given in texts, is that the *P*-th percentile $(0<P\leq 100)$ of a list of *N* ordered values (sorted from least to greatest) is the smallest value in the list such that at least *P* percent of the data is less than or equal to that value.

This is calculated by first calculating the ordinal rank and then taking the value from the ordered list that corresponds to that rank. The ordinal rank *n* is calculated using the formula

$n=\left\lceil {\frac {P}{100}}\times N\right\rceil .$

- Using the nearest-rank method on lists with fewer than 100 distinct values can result in the same value being used for more than one percentile.
- A percentile calculated using the nearest-rank method will always be a member of the original ordered list.
- The 100th percentile is defined to be the largest value in the ordered list.
- This method is also called the "empirical distribution function" method.
- The 50th percentile calculated using this method is equal to the usual value of the median if *N* is odd, but not if *N* is even.

### The CDF method

The CDF method was described, e.g. by Langford.

Given the order statistics

$\{v_{(i)},i=1,2,\ldots ,N:v_{(i+1)}\geq v_{(i)},\forall i=1,2,\ldots ,N-1\},$

calculate $x={\frac {P}{100}}\times N$ . The percentile is

$v(x)={\begin{cases}v_{(1)}{\text{, for }}x=0,\\v_{(\lceil x\rceil )}{\text{, for }}x\notin \{0,1,2,\ldots ,N-1\},\\{\frac {v_{(x)}+v_{(x+1)}}{2}}{\text{, for }}x\in \{1,2,\ldots ,N-1\}.\end{cases}}$

- The 50th percentile calculated using this method is equal to the usual value of the median.

- Doubling the data leaves the calculated percentile value unchanged.

CDF percentile values for ordered list {15, 20, 35, 40, 50},

$N=5$

Percentage

P

$0\leq P<20$

$P=20$

$20<P<40$

$P=40$

$40<P<60$

$P=60$

$60<P<80$

$P=80$

$80<P\leq 100$

$x={\frac {P}{100}}\times N$

$0\leq x<1$

$x=1$

$1<x<2$

$x=2$

$2<x<3$

$x=3$

$3<x<4$

$x=4$

$4<x\leq 5$

Percentile

15

17.5

20

27.5

35

37.5

40

45

50

### The linear interpolation between closest ranks method

An alternative to rounding used in many applications is to use linear interpolation between adjacent ranks.

Given the order statistics

$\{v_{(i)},i=1,2,\ldots ,N:v_{(i+1)}\geq v_{(i)},\forall i=1,2,\ldots ,N-1\},$

the linear interpolation is simply accomplished by calculating

$v(x)={\begin{cases}v_{(1)}{\text{, for }}x\leq 1,\\v_{(N)}{\text{, for }}x=N,\\v_{(\lfloor x\rfloor )}+(x{\bmod {1}})(v_{(\lfloor x\rfloor +1)}-v_{(\lfloor x\rfloor )}){\text{, for }}1<x<N.\end{cases}}$

, where $\lfloor x\rfloor$ uses the floor function to represent the integral part of x, whereas $x{\bmod {1}}$ uses the mod function to represent its fractional part (the remainder after division by 1).

This way, $v(i)=v_{(i)}{\text{, for }}i=1,2,\ldots ,N.$

As we can see, x is the continuous version of the subscript i, linearly interpolating v between adjacent nodes.

There are two ways in which the variant approaches differ. The first is in the linear relationship between the *rank* x, the *percent rank* $P=100p$ , and a constant that is a function of the sample size N:

$x=f(p,N)=(N+c_{1})p+c_{2}.$

There is the additional requirement that the midpoint of the range $(1,N)$ , corresponding to the median, occur at $p=0.5$ :

${\begin{aligned}f(0.5,N)&={\frac {N+c_{1}}{2}}+c_{2}={\frac {N+1}{2}}\\\therefore 2c_{2}+c_{1}&=1\end{aligned}},$

and our revised function now has just one degree of freedom, looking like this:

$x=f(p,N)=(N+1-2C)p+C.$

The second way in which the variants differ is in the definition of the function near the margins of the $[0,1]$ range of p: $f(p,N)$ should produce, or be forced to produce, a result in the range $[1,N]$ , which may mean the absence of a one-to-one correspondence in the wider region. One author has suggested a choice of $C={\tfrac {1}{2}}(1+\xi )$ where ξ is the shape of the Generalized extreme value distribution which is the extreme value limit of the sampled distribution.

#### First variant, *C* = 1/2

(Sources: Matlab "prctile" function,)

$x=f(p)={\begin{cases}Np+{\frac {1}{2}},\forall p\in \left[p_{1},p_{N}\right],\\1,\forall p\in \left[0,p_{1}\right],\\N,\forall p\in \left[p_{N},1\right].\end{cases}}$

where

$p_{i}={\frac {1}{N}}\left(i-{\frac {1}{2}}\right),i\in [1,N]\cap \mathbb {N}$

$\therefore p_{1}={\frac {1}{2N}},p_{N}={\frac {2N-1}{2N}}.$

Furthermore, let

$P_{i}=100p_{i}.$

The inverse relationship is restricted to a narrower region:

$p={\frac {1}{N}}\left(x-{\frac {1}{2}}\right),x\in (1,N)\cap \mathbb {R} .$

#### Second variant, *C* = 1

[Source: Some software packages, including NumPy and Microsoft Excel (up to and including version 2013 by means of the PERCENTILE.INC function). Noted as an alternative by NIST.]

$x=f(p,N)=p(N-1)+1{\text{, }}p\in [0,1]$

$\therefore p={\frac {x-1}{N-1}}{\text{, }}x\in [1,N].$

Note that the $x\leftrightarrow p$ relationship is one-to-one for $p\in [0,1]$ , the only one of the three variants with this property; hence the "INC" suffix, for *inclusive*, on the Excel function.

#### Third variant, *C* = 0

(The primary variant recommended by NIST. Adopted by Microsoft Excel since 2010 by means of PERCENTIL.EXC function. However, as the "EXC" suffix indicates, the Excel version *excludes* both endpoints of the range of *p*, i.e., $p\in (0,1)$ , whereas the "INC" version, the second variant, does not; in fact, any number smaller than ${\frac {1}{N+1}}$ is also excluded and would cause an error.)

$x=f(p,N)={\begin{cases}1{\text{, }}p\in \left[0,{\frac {1}{N+1}}\right]\\p(N+1){\text{, }}p\in \left({\frac {1}{N+1}},{\frac {N}{N+1}}\right)\\N{\text{, }}p\in \left[{\frac {N}{N+1}},1\right]\end{cases}}.$

The inverse is restricted to a narrower region:

$p={\frac {x}{N+1}}{\text{, }}x\in (0,N).$

### The weighted percentile method

In addition to the percentile function, there is also a *weighted percentile*, where the percentage in the total weight is counted instead of the total number. There is no standard function for a weighted percentile. One method extends the above approach in a natural way.

Suppose we have positive weights $w_{1},w_{2},w_{3},\dots ,w_{N}$ associated, respectively, with our *N* sorted sample values. Let

$S_{N}=\sum _{k=1}^{N}w_{k},$

the sum of the weights. Then the formulas above are generalized by taking

$p_{n}={\frac {1}{S_{N}}}\left(S_{n}-{\frac {w_{n}}{2}}\right)$

when

$C=1/2$

,

or

$p_{n}={\frac {S_{n}-Cw_{n}}{S_{N}+(1-2C)w_{n}}}$

for general

C

,

and

$v=v_{k}+{\frac {P-p_{k}}{p_{k+1}-p_{k}}}(v_{k+1}-v_{k}).$

The 50% weighted percentile is known as the weighted median.
