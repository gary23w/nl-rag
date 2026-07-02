---
title: "Missing data"
source: https://en.wikipedia.org/wiki/Missing_data
domain: pandas-dataframe
license: CC-BY-SA-4.0
tags: python pandas, pandas dataframe, data analysis python
fetched: 2026-07-02
---

# Missing data

In statistics, **missing data**, or **missing values**, occur when no data value is stored for the variable in an observation. Missing data are a common occurrence and can have a significant effect on the conclusions that can be drawn from the data.

Missing data can occur because of nonresponse: no information is provided for one or more items or for a whole unit ("subject"). Some items are more likely to generate a nonresponse than others: for example items about private subjects such as income. Attrition is a type of missingness that can occur in longitudinal studies—for instance studying development where a measurement is repeated after a certain period of time. Missingness occurs when participants drop out before the test ends and one or more measurements are missing.

Data often are missing in research in economics, sociology, and political science because governments or private entities choose not to, or fail to, report critical statistics, or because the information is not available. Sometimes missing values are caused by the researcher—for example, when data collection is done improperly or mistakes are made in data entry.

These forms of missingness take different types, with different impacts on the validity of conclusions from research: Missing completely at random, missing at random, and missing not at random. Missing data can be handled similarly as censored data.

## Types

Understanding the reasons why data are missing is important for handling the remaining data correctly. If values are missing completely at random, the data sample is likely still representative of the population. But if the values are missing systematically, analysis may be biased. For example, in a study of the relation between IQ and income, if participants with an above-average IQ tend to skip the question ‘What is your salary?’, analyses that do not take into account this missing at random (MAR pattern (see below)) may falsely fail to find a positive association between IQ and salary. Because of these problems, methodologists routinely advise researchers to design studies to minimize the occurrence of missing values. Graphical models can be used to describe the missing data mechanism in detail.

### Missing completely at random

Values in a data set are **missing completely at random (MCAR)** if the events that lead to any particular data-item being missing are independent both of observable variables and of unobservable parameters of interest, and occur entirely at random. When data are MCAR, the analysis performed on the data is unbiased; however, data are rarely MCAR.

In the case of MCAR, the missingness of data is unrelated to any study variable: thus, the participants with completely observed data are in effect a random sample of all the participants assigned a particular intervention. With MCAR, the random assignment of treatments is assumed to be preserved, but that is usually an unrealistically strong assumption in practice.

### Missing at random

**Missing at random (MAR)** occurs when the missingness is not random, but where missingness can be fully accounted for by variables where there is complete information. Since MAR is an assumption that is impossible to verify statistically, we must rely on its substantive reasonableness. An example is that males are less likely to fill in a depression survey but this has nothing to do with their level of depression, after accounting for maleness. Depending on the analysis method, these data can still induce parameter bias in analyses due to the contingent emptiness of cells (male, very high depression may have zero entries). However, if the parameter is estimated with Full Information Maximum Likelihood, MAR will provide asymptotically unbiased estimates.

### Missing not at random

**Missing not at random (MNAR)** (also known as nonignorable nonresponse) is data that is neither MAR nor MCAR (i.e. the value of the variable that's missing is related to the reason it's missing). To extend the previous example, this would occur if men failed to fill in a depression survey *because* of their level of depression.

Samuelson and Spirer (1992) discussed how missing and/or distorted data about demographics, law enforcement, and health could be indicators of patterns of human rights violations. They gave several fairly well documented examples.

### Structured missingness

Missing data can also arise in subtle ways that are not well accounted for in classical theory. An increasingly encountered problem arises in which data may not be MAR but missing values exhibit an association or structure, either explicitly or implicitly. Such missingness has been described as ‘structured missingness’.

Structured missingness commonly arises when combining information from multiple studies, each of which may vary in its design and measurement set and therefore only contain a subset of variables from the union of measurement modalities. In these situations, missing values may relate to the various sampling methodologies used to collect the data or reflect characteristics of the wider population of interest, and so may impart useful information. For instance, in a health context, structured missingness has been observed as a consequence of linking clinical, genomic and imaging data.

The presence of structured missingness may be a hindrance to make effective use of data at scale, including through both classical statistical and current machine learning methods. For example, there might be bias inherent in the reasons why some data might be missing in patterns, which might have implications in predictive fairness for machine learning models. Furthermore, established methods for dealing with missing data, such as imputation, do not usually take into account the structure of the missing data and so development of new formulations is needed to deal with structured missingness appropriately or effectively. Finally, characterising structured missingness within the classical framework of MCAR, MAR, and MNAR is a work in progress.

### Planned missingness

Missing data can also be a deliberate part of study design. Specifically, planned missingness is a research design strategy, employed in survey research, in which data are intentionally left uncollected from individual respondents (typically by administering randomly sampled subsets of items to each participant) to reduce burden while preserving the ability to estimate parameters for the full item set across the sample.

## Techniques of dealing with missing data

Missing data reduces the representativeness of the sample and can therefore distort inferences about the population. Generally speaking, there are three main approaches to handle missing data: (1) *Imputation*—where values are filled in the place of missing data, (2) *omission*—where samples with invalid data are discarded from further analysis and (3) *analysis*—by directly applying methods unaffected by the missing values. One systematic review addressing the prevention and handling of missing data for patient-centered outcomes research identified 10 standards as necessary for the prevention and handling of missing data. These include standards for study design, study conduct, analysis, and reporting.

In some practical application, the experimenters can control the level of missingness, and prevent missing values before gathering the data. For example, in computer questionnaires, it is often not possible to skip a question. A question has to be answered, otherwise one cannot continue to the next. So missing values due to the participant are eliminated by this type of questionnaire, though this method may not be permitted by an ethics board overseeing the research. In survey research, it is common to make multiple efforts to contact each individual in the sample, often sending letters to attempt to persuade those who have decided not to participate to change their minds. However, such techniques can either help or hurt in terms of reducing the negative inferential effects of missing data, because the kind of people who are willing to be persuaded to participate after initially refusing or not being home are likely to be significantly different from the kinds of people who will still refuse or remain unreachable after additional effort.

In situations where missing values are likely to occur, the researcher is often advised on planning to use methods of data analysis methods that are robust to missingness. An analysis is robust when we are confident that mild to moderate violations of the technique's key assumptions will produce little or no bias, or distortion in the conclusions drawn about the population.

### Imputation

Some data analysis techniques are not robust to missingness, and require to "fill in", or impute the missing data. Rubin (1987) argued that repeating imputation even a few times (five or less) enormously improves the quality of estimation. For many practical purposes, two or three imputations capture most of the relative efficiency that could be captured with a larger number of imputations. However, a too-small number of imputations can lead to a substantial loss of statistical power, and some scholars now recommend 20 to 100 or more. Any multiply-imputed data analysis must be repeated for each of the imputed data sets and, in some cases, the relevant statistics must be combined in a relatively complicated way. Multiple imputation is not conducted in specific disciplines, as there is a lack of training or misconceptions about them. Methods such as listwise deletion have been used to impute data but it has been found to introduce additional bias. There is a beginner guide that provides a step-by-step instruction how to impute data.

The expectation-maximization algorithm is an approach in which values of the statistics which would be computed if a complete dataset were available are estimated (imputed), taking into account the pattern of missing data. In this approach, values for individual missing data-items are not usually imputed.

#### Interpolation

In the mathematical field of numerical analysis, interpolation is a method of constructing new data points within the range of a discrete set of known data points.

In the comparison of two paired samples with missing data, a test statistic that uses all available data without the need for imputation is the partially overlapping samples t-test. This is valid under normality and assuming MCAR

### Partial deletion

Methods which involve reducing the data available to a dataset having no missing values include:

- Listwise deletion/casewise deletion
- Pairwise deletion

### Full analysis

Methods which take full account of all information available, without the distortion resulting from using imputed values as if they were actually observed:

- Generative approaches:
  - The expectation-maximization algorithm
  - full information maximum likelihood estimation
- Discriminative approaches:
  - Max-margin classification of data with absent features

Partial identification methods may also be used.

## Model-based techniques

Model based techniques, often using graphs, offer additional tools for testing missing data types (MCAR, MAR, MNAR) and for estimating parameters under missing data conditions. For example, a test for refuting MAR/MCAR reads as follows:

For any three variables *X,Y*, and *Z* where *Z* is fully observed and *X* and *Y* partially observed, the data should satisfy: $X\perp \!\!\!\perp R_{y}|(R_{x},Z)$ .

In words, the observed portion of *X* should be independent on the missingness status of *Y,* conditional on every value of *Z*. Failure to satisfy this condition indicates that the problem belongs to the MNAR category.

(Remark: These tests are necessary for variable-based MAR which is a slight variation of event-based MAR.)

When data falls into MNAR category, techniques are available for consistently estimating parameters when certain conditions hold in the model. For example, if *Y* explains the reason for missingness in *X,* and *Y* itself has missing values, the joint probability distribution of *X* and *Y* can still be estimated if the missingness of *Y* is random. The estimand in this case will be:

${\begin{aligned}P(X,Y)&=P(X|Y)P(Y)\\&=P(X|Y,R_{x}=0,R_{y}=0)P(Y|R_{y}=0)\end{aligned}}$

where $R_{x}=0$ and $R_{y}=0$ denote the observed portions of their respective variables.

Different model structures may yield different estimands and different procedures of estimation whenever consistent estimation is possible. The preceding estimand calls for first estimating $P(X|Y)$ from complete data and multiplying it by $P(Y)$ estimated from cases in which *Y* is observed regardless of the status of *X*. Moreover, in order to obtain a consistent estimate it is crucial that the first term be $P(X|Y)$ as opposed to $P(Y|X)$ .

In many cases model based techniques permit the model structure to undergo refutation tests. Any model which implies the independence between a partially observed variable *X* and the missingness indicator of another variable *Y* (i.e. $R_{y}$ ), conditional on $R_{x}$ can be submitted to the following refutation test: $X\perp \!\!\!\perp R_{y}|R_{x}=0$ .

Finally, the estimands that emerge from these techniques are derived in closed form and do not require iterative procedures such as Expectation Maximization that are susceptible to local optima.

A special class of problems appears when the probability of the missingness depends on time. For example, in the trauma databases the probability to lose data about the trauma outcome depends on the day after trauma. In these cases various non-stationary Markov chain models are applied.
