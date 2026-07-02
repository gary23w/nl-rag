---
title: "Partition of sums of squares"
source: https://en.wikipedia.org/wiki/Sum_of_squares_(statistics)
domain: analysis-of-variance
license: CC-BY-SA-4.0
tags: analysis of variance, F-test, sum of squares, post hoc analysis
fetched: 2026-07-02
---

# Partition of sums of squares

(Redirected from

Sum of squares (statistics)

)

The **partition of sums of squares** is a concept that permeates much of inferential statistics and descriptive statistics. More properly, it is the **partitioning of sums of squared deviations or errors**. Mathematically, the sum of squared deviations is an unscaled, or unadjusted measure of dispersion (also called variability). When scaled for the number of degrees of freedom, it estimates the variance, or spread of the observations about their mean value. Partitioning of the sum of squared deviations into various components allows the overall variability in a dataset to be ascribed to different types or sources of variability, with the relative importance of each being quantified by the size of each component of the overall sum of squares.

## Background

The distance from any point in a collection of data, to the mean of the data, is the deviation. This can be written as $y_{i}-{\overline {y}}$ , where $y_{i}$ is the ith data point, and ${\overline {y}}$ is the estimate of the mean. If all such deviations are squared, then summed, as in $\sum _{i=1}^{n}\left(y_{i}-{\overline {y}}\,\right)^{2}$ , this gives the "sum of squares" for these data.

When more data are added to the collection the sum of squares will increase, except in unlikely cases such as the new data being equal to the mean. So usually, the sum of squares will grow with the size of the data collection. That is a manifestation of the fact that it is unscaled.

In many cases, the number of degrees of freedom is simply the number of data points in the collection, minus one. We write this as *n* − 1, where *n* is the number of data points.

Scaling (also known as normalizing) means adjusting the sum of squares so that it does not grow as the size of the data collection grows. This is important when we want to compare samples of different sizes, such as a sample of 100 people compared to a sample of 20 people. If the sum of squares were not normalized, its value would always be larger for the sample of 100 people than for the sample of 20 people. To scale the sum of squares, we divide it by the degrees of freedom, i.e., calculate the sum of squares per degree of freedom, or variance. Standard deviation, in turn, is the square root of the variance.

The above describes how the sum of squares is used in descriptive statistics; see the article on total sum of squares for an application of this broad principle to inferential statistics.

## Partitioning the sum of squares in linear regression

**Theorem.** Given a linear regression model $y_{i}=\beta _{0}+\beta _{1}x_{i1}+\cdots +\beta _{p}x_{ip}+\varepsilon _{i}$ *including a constant* $\beta _{0}$ , based on a sample $(y_{i},x_{i1},\ldots ,x_{ip}),\,i=1,\ldots ,n$ containing *n* observations, the total sum of squares $\mathrm {TSS} =\sum _{i=1}^{n}(y_{i}-{\bar {y}})^{2}$ can be partitioned as follows into the explained sum of squares (ESS) and the residual sum of squares (RSS):

$\mathrm {TSS} =\mathrm {ESS} +\mathrm {RSS} ,$

where this equation is equivalent to each of the following forms:

${\begin{aligned}\left\|y-{\bar {y}}\mathbf {1} \right\|^{2}&=\left\|{\hat {y}}-{\bar {y}}\mathbf {1} \right\|^{2}+\left\|{\hat {\varepsilon }}\right\|^{2},\quad \mathbf {1} =(1,1,\ldots ,1)^{T},\\\sum _{i=1}^{n}(y_{i}-{\bar {y}})^{2}&=\sum _{i=1}^{n}({\hat {y}}_{i}-{\bar {y}})^{2}+\sum _{i=1}^{n}(y_{i}-{\hat {y}}_{i})^{2},\\\sum _{i=1}^{n}(y_{i}-{\bar {y}})^{2}&=\sum _{i=1}^{n}({\hat {y}}_{i}-{\bar {y}})^{2}+\sum _{i=1}^{n}{\hat {\varepsilon }}_{i}^{2},\\\end{aligned}}$

where

${\hat {y}}_{i}$

is the value estimated by the regression line having

${\hat {b}}_{0}$

,

${\hat {b}}_{1}$

, ...,

${\hat {b}}_{p}$

as the estimated

coefficients

.

### Proof

${\begin{aligned}\sum _{i=1}^{n}(y_{i}-{\overline {y}})^{2}&=\sum _{i=1}^{n}(y_{i}-{\overline {y}}+{\hat {y}}_{i}-{\hat {y}}_{i})^{2}=\sum _{i=1}^{n}(({\hat {y}}_{i}-{\bar {y}})+\underbrace {(y_{i}-{\hat {y}}_{i})} _{{\hat {\varepsilon }}_{i}})^{2}\\&=\sum _{i=1}^{n}(({\hat {y}}_{i}-{\bar {y}})^{2}+2{\hat {\varepsilon }}_{i}({\hat {y}}_{i}-{\bar {y}})+{\hat {\varepsilon }}_{i}^{2})\\&=\sum _{i=1}^{n}({\hat {y}}_{i}-{\bar {y}})^{2}+\sum _{i=1}^{n}{\hat {\varepsilon }}_{i}^{2}+2\sum _{i=1}^{n}{\hat {\varepsilon }}_{i}({\hat {y}}_{i}-{\bar {y}})\\&=\sum _{i=1}^{n}({\hat {y}}_{i}-{\bar {y}})^{2}+\sum _{i=1}^{n}{\hat {\varepsilon }}_{i}^{2}+2\sum _{i=1}^{n}{\hat {\varepsilon }}_{i}({\hat {\beta }}_{0}+{\hat {\beta }}_{1}x_{i1}+\cdots +{\hat {\beta }}_{p}x_{ip}-{\overline {y}})\\&=\sum _{i=1}^{n}({\hat {y}}_{i}-{\bar {y}})^{2}+\sum _{i=1}^{n}{\hat {\varepsilon }}_{i}^{2}+2({\hat {\beta }}_{0}-{\overline {y}})\underbrace {\sum _{i=1}^{n}{\hat {\varepsilon }}_{i}} _{0}+2{\hat {\beta }}_{1}\underbrace {\sum _{i=1}^{n}{\hat {\varepsilon }}_{i}x_{i1}} _{0}+\cdots +2{\hat {\beta }}_{p}\underbrace {\sum _{i=1}^{n}{\hat {\varepsilon }}_{i}x_{ip}} _{0}\\&=\sum _{i=1}^{n}({\hat {y}}_{i}-{\bar {y}})^{2}+\sum _{i=1}^{n}{\hat {\varepsilon }}_{i}^{2}=\mathrm {ESS} +\mathrm {RSS} \\\end{aligned}}$

The requirement that the model include a constant or equivalently that the design matrix contain a column of ones ensures that $\sum _{i=1}^{n}{\hat {\varepsilon }}_{i}=0$ , i.e. ${\hat {\varepsilon }}^{T}\mathbf {1} =0$ .

The proof can also be expressed in vector form, as follows:

${\begin{aligned}SS_{\text{total}}=\Vert \mathbf {y} -{\bar {y}}\mathbf {1} \Vert ^{2}&=\Vert \mathbf {y} -{\bar {y}}\mathbf {1} +\mathbf {\hat {y}} -\mathbf {\hat {y}} \Vert ^{2},\\&=\Vert \left(\mathbf {\hat {y}} -{\bar {y}}\mathbf {1} \right)+\left(\mathbf {y} -\mathbf {\hat {y}} \right)\Vert ^{2},\\&=\Vert {\mathbf {\hat {y}} -{\bar {y}}\mathbf {1} }\Vert ^{2}+\Vert {\hat {\varepsilon }}\Vert ^{2}+2{\hat {\varepsilon }}^{T}\left(\mathbf {\hat {y}} -{\bar {y}}\mathbf {1} \right),\\&=SS_{\text{regression}}+SS_{\text{error}}+2{\hat {\varepsilon }}^{T}\left(X{\hat {\beta }}-{\bar {y}}\mathbf {1} \right),\\&=SS_{\text{regression}}+SS_{\text{error}}+2\left({\hat {\varepsilon }}^{T}X\right){\hat {\beta }}-2{\bar {y}}\underbrace {{\hat {\varepsilon }}^{T}\mathbf {1} } _{0},\\&=SS_{\text{regression}}+SS_{\text{error}}.\end{aligned}}$

The elimination of terms in the last line, used the fact that

${\hat {\varepsilon }}^{T}X=\left(\mathbf {y} -\mathbf {\hat {y}} \right)^{T}X=\mathbf {y} ^{T}(I-X(X^{T}X)^{-1}X^{T})^{T}X={\mathbf {y} }^{T}(X^{T}-X^{T})^{T}={\mathbf {0} }.$

### Further partitioning

Note that the residual sum of squares can be further partitioned as the lack-of-fit sum of squares plus the sum of squares due to pure error.
