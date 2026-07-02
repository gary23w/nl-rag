---
title: "Panel data"
source: https://en.wikipedia.org/wiki/Panel_data
domain: econometrics
license: CC-BY-SA-4.0
tags: econometrics, instrumental variables, panel data, gauss-markov theorem
fetched: 2026-07-02
---

# Panel data

In statistics and econometrics, **panel data** and **longitudinal data** are both multi-dimensional data involving measurements over time. Panel data is a subset of longitudinal data where observations are for the same subjects each time.

Time series and cross-sectional data can be thought of as special cases of panel data that are in one dimension only (one panel member or individual for the former, one time point for the latter). A literature search often involves time series, cross-sectional, or panel data.

A study that uses panel data is called a longitudinal study or panel study.

## Example

| person | year | income | age | sex |
|---|---|---|---|---|
| 1 | 2016 | 1300 | 27 | 1 |
| 1 | 2017 | 1600 | 28 | 1 |
| 1 | 2018 | 2000 | 29 | 1 |
| 2 | 2016 | 2000 | 38 | 2 |
| 2 | 2017 | 2300 | 39 | 2 |
| 2 | 2018 | 2400 | 40 | 2 |

| person | year | income | age | sex |
|---|---|---|---|---|
| 1 | 2016 | 1600 | 23 | 1 |
| 1 | 2017 | 1500 | 24 | 1 |
| 2 | 2016 | 1900 | 41 | 2 |
| 2 | 2017 | 2000 | 42 | 2 |
| 2 | 2018 | 2100 | 43 | 2 |
| 3 | 2017 | 3300 | 34 | 1 |

In the **multiple response permutation procedure** (**MRPP**) example above, two datasets with a panel structure are shown and the objective is to test whether there's a significant difference between people in the sample data. Individual characteristics (income, age, sex) are collected for different persons and different years. In the first dataset, two persons (1, 2) are observed every year for three years (2016, 2017, 2018). In the second dataset, three persons (1, 2, 3) are observed two times (person 1), three times (person 2), and one time (person 3), respectively, over three years (2016, 2017, 2018); in particular, person 1 is not observed in year 2018 and person 3 is not observed in 2016 or 2018.

A **balanced panel** (e.g., the first dataset above) is a dataset in which *each* panel member (i.e., person) is observed *every* year. Consequently, if a balanced panel contains N panel members and T periods, the number of observations ( n ) in the dataset is necessarily $n=N\cdot T$ .

An **unbalanced panel** (e.g., the second dataset above) is a dataset in which *at least one* panel member is not observed every period. Therefore, if an unbalanced panel contains N panel members and T periods, then the following strict inequality holds for the number of observations ( n ) in the dataset: $n<N\cdot T$ .

Both datasets above are structured in the **long format**, which is where one row holds one observation per time. Another way to structure panel data would be the **wide format** where one row represents one observational unit for *all* points in time (for the example, the wide format would have only two (first example) or three (second example) rows of data with additional columns for each time-varying variable (income, age).

## Analysis

A panel has the form

$X_{it},\quad i=1,\dots ,N,\quad t=1,\dots ,T,$

where i is the individual dimension and t is the time dimension. A general panel data regression model is written as $y_{it}=\alpha +\beta 'X_{it}+u_{it}$ . Different assumptions can be made on the precise structure of this general model. Two important models are the fixed effects model and the random effects model.

Consider a generic panel data model:

$y_{it}=\alpha +\beta 'X_{it}+u_{it},$

$u_{it}=\mu _{i}+v_{it}.$

$\mu _{i}$ are individual-specific, time-invariant effects (e.g., in a panel of countries this could include geography, climate, etc.) which are fixed over time, whereas $v_{it}$ is a time-varying random component.

If $\mu _{i}$ is unobserved, and correlated with at least one of the independent variables, then it will cause omitted variable bias in a standard OLS regression. However, panel data methods, such as the fixed effects estimator or alternatively, the first-difference estimator can be used to control for it.

If $\mu _{i}$ is not correlated with any of the independent variables, ordinary least squares linear regression methods can be used to yield unbiased and consistent estimates of the regression parameters. However, because $\mu _{i}$ is fixed over time, it will induce serial correlation in the error term of the regression. This means that more efficient estimation techniques are available. Random effects is one such method: it is a special case of feasible generalized least squares which controls for the structure of the serial correlation induced by $\mu _{i}$ .

### Dynamic panel data

Dynamic panel data describes the case where a lag of the dependent variable is used as regressor:

$y_{it}=\alpha +\beta 'X_{it}+\gamma y_{it-1}+u_{it}.$

The presence of the lagged dependent variable violates strict exogeneity, that is, endogeneity may occur. The fixed effect estimator and the first differences estimator both rely on the assumption of strict exogeneity. Hence, if $u_{i}$ is believed to be correlated with one of the independent variables, an alternative estimation technique must be used. Instrumental variables or GMM techniques are commonly used in this situation, such as the Arellano–Bond estimator. While estimating this we should have the proper information about the instrumental variables.

## Data sets which have a panel design

- *German* Socio-Economic Panel (SOEP)
- Household, Income and Labour Dynamics in Australia Survey (HILDA)
- British Household Panel Survey (BHPS)
- Survey of Income and Program Participation (SIPP)
- Lifelong Labour Market Database (LLMDB)
- Panel Study of Income Dynamics (PSID)
- China Family Panel Studies (CFPS)
- National Longitudinal Surveys (NLSY)
- Labour Force Survey (LFS)

## Data sets which have a multi-dimensional panel design
