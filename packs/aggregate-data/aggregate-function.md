---
title: "Aggregate function"
source: https://en.wikipedia.org/wiki/Aggregate_function
domain: aggregate-data
license: CC-BY-SA-4.0
tags: aggregate data
fetched: 2026-07-03
---

# Aggregate function

In database management, an **aggregate function** or **aggregation function** is a function where multiple values are processed together to form a single summary statistic.

Common aggregate functions include:

- Average (i.e., arithmetic mean)
- Count
- Maximum
- Median
- Minimum
- Mode
- Range
- Sum

Others include:

- Nanmean (mean ignoring NaN values, also known as "nil" or "null")
- Stddev

Formally, an aggregate function takes as input a set, a multiset (bag), or a list from some input domain *I* and outputs an element of an output domain *O*. The input and output domains may be the same, such as for `SUM`, or may be different, such as for `COUNT`.

Aggregate functions occur commonly in numerous programming languages, in spreadsheets, and in relational algebra.

The `listagg` function, as defined in the SQL:2016 standard aggregates data from multiple rows into a single concatenated string.

In the entity relationship diagram, aggregation is represented as seen in Figure 1 with a rectangle around the relationship and its entities to indicate that it is being treated as an aggregate entity.

## Decomposable aggregate functions

Aggregate functions present a bottleneck, because they potentially require having all input values at once. In distributed computing, it is desirable to divide such computations into smaller pieces, and distribute the work, usually computing in parallel, via a divide and conquer algorithm.

Some aggregate functions can be computed by computing the aggregate for subsets, and then aggregating these aggregates; examples include COUNT, MAX, MIN, and SUM. In other cases the aggregate can be computed by computing auxiliary numbers for subsets, aggregating these auxiliary numbers, and finally computing the overall number at the end; examples include AVERAGE (tracking sum and count, dividing at the end) and RANGE (tracking max and min, subtracting at the end). In other cases the aggregate cannot be computed without analyzing the entire set at once, though in some cases approximations can be distributed; examples include DISTINCT COUNT (Count-distinct problem), MEDIAN, and MODE.

Such functions are called **decomposable aggregation functions** or **decomposable aggregate functions**. The simplest may be referred to as **self-decomposable aggregation functions**, which are defined as those functions f such that there is a *merge operator* ⁠ $\diamond$ ⁠ such that

$f(X\uplus Y)=f(X)\diamond f(Y)$

where ⁠ $\uplus$ ⁠ is the union of multisets (see monoid homomorphism).

For example, SUM:

$\operatorname {SUM} ({x})=x$

, for a singleton;

$\operatorname {SUM} (X\uplus Y)=\operatorname {SUM} (X)+\operatorname {SUM} (Y)$

, meaning that merge

⁠

$\diamond$

⁠

is simply addition.

COUNT:

$\operatorname {COUNT} ({x})=1$

,

$\operatorname {COUNT} (X\uplus Y)=\operatorname {COUNT} (X)+\operatorname {COUNT} (Y)$

.

MAX:

$\operatorname {MAX} ({x})=x$

,

$\operatorname {MAX} (X\uplus Y)=\max {\bigl (}\operatorname {MAX} (X),\operatorname {MAX} (Y){\bigr )}$

.

MIN:

${\textstyle \operatorname {MIN} ({x})=x}$

,

$\operatorname {MIN} (X\uplus Y)=\min {\bigl (}\operatorname {MIN} (X),\operatorname {MIN} (Y){\bigr )}$

.

Note that self-decomposable aggregation functions can be combined (formally, taking the product) by applying them separately, so for instance one can compute both the SUM and COUNT at the same time, by tracking two numbers.

More generally, one can define a **decomposable aggregation function** f as one that can be expressed as the composition of a final function g and a self-decomposable aggregation function h, $f=g\circ h,f(X)=g(h(X))$ . For example, AVERAGE=SUM/COUNT and RANGE=MAX−MIN.

In the MapReduce framework, these steps are known as InitialReduce (value on individual record/singleton set), Combine (binary merge on two aggregations), and FinalReduce (final function on auxiliary values), and moving decomposable aggregation before the Shuffle phase is known as an InitialReduce step,

Decomposable aggregation functions are important in online analytical processing (OLAP), as they allow aggregation queries to be computed on the pre-computed results in the OLAP cube, rather than on the base data. For example, it is easy to support COUNT, MAX, MIN, and SUM in OLAP, since these can be computed for each cell of the OLAP cube and then summarized ("rolled up"), but it is difficult to support MEDIAN, as that must be computed for every view separately.

## Other decomposable aggregate functions

In order to calculate the average and standard deviation from aggregate data, it is necessary to have available for each group: the total of values (Σxi = SUM(x)), the number of values (N=COUNT(x)) and the total of squares of the values (Σxi2=SUM(x2)) of each groups. `AVG`: $\operatorname {AVG} (X\uplus Y)={\bigl (}\operatorname {AVG} (X)*\operatorname {COUNT} (X)+\operatorname {AVG} (Y)*\operatorname {COUNT} (Y){\bigr )}/{\bigl (}\operatorname {COUNT} (X)+\operatorname {COUNT} (Y){\bigr )}$ or $\operatorname {AVG} (X\uplus Y)={\bigl (}\operatorname {SUM} (X)+\operatorname {SUM} (Y){\bigr )}/{\bigl (}\operatorname {COUNT} (X)+\operatorname {COUNT} (Y){\bigr )}$ or, only if COUNT(X)=COUNT(Y) $\operatorname {AVG} (X\uplus Y)={\bigl (}\operatorname {AVG} (X)+\operatorname {AVG} (Y){\bigr )}/2$ `SUM(x2)`: The sum of squares of the values is important in order to calculate the Standard Deviation of groups $\operatorname {SUM} (X^{2}\uplus Y^{2})=\operatorname {SUM} (X^{2})+\operatorname {SUM} (Y^{2})$ `STDDEV`: For a finite population with equal probabilities at all points, we have $\operatorname {STDDEV} (X)=s(x)={\sqrt {{\frac {1}{N}}\sum _{i=1}^{N}(x_{i}-{\overline {x}})^{2}}}={\sqrt {{\frac {1}{N}}\left(\sum _{i=1}^{N}x_{i}^{2}\right)-({\overline {x}})^{2}}}={\sqrt {\operatorname {SUM} (x^{2})/\operatorname {COUNT} (x)-\operatorname {AVG} (x)^{2}}}$

This means that the standard deviation is equal to the square root of the difference between the average of the squares of the values and the square of the average value. $\operatorname {STDDEV} (X\uplus Y)={\sqrt {\operatorname {SUM} (X^{2}\uplus Y^{2})/\operatorname {COUNT} (X\uplus Y)-\operatorname {AVG} (X\uplus Y)^{2}}}$ $\operatorname {STDDEV} (X\uplus Y)={\sqrt {{\bigl (}\operatorname {SUM} (X^{2})+\operatorname {SUM} (Y^{2}){\bigr )}/{\bigl (}\operatorname {COUNT} (X)+\operatorname {COUNT} (Y){\bigr )}-{\bigl (}(\operatorname {SUM} (X)+\operatorname {SUM} (Y))/(\operatorname {COUNT} (X)+\operatorname {COUNT} (Y)){\bigr )}^{2}}}$
