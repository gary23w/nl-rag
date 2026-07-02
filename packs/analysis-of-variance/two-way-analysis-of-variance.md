---
title: "Two-way analysis of variance"
source: https://en.wikipedia.org/wiki/Two-way_analysis_of_variance
domain: analysis-of-variance
license: CC-BY-SA-4.0
tags: analysis of variance, F-test, sum of squares, post hoc analysis
fetched: 2026-07-02
---

# Two-way analysis of variance

In statistics, the **two-way analysis of variance** (**ANOVA**) is used to study how two categorical independent variables affect one continuous dependent variable. It extends the One-way analysis of variance (one-way ANOVA) by allowing both factors to be analyzed at the same time. A two-way ANOVA evaluates the main effect of each independent variable and if there is any interaction between them.

Researchers use this test to see if two factors act independent or combined to influence a Dependent variable. It is used in the fields of Psychology, Agriculture, Education, and Biomedical research. For example, it can be used to study how fertilizer type and water level together affect plant growth. The analysis produces F-statistics that indicate whether observed differences between groups are statistically significant.

## History

The two-way analysis of variance was developed in the early twentieth century during the rise of modern Experimental design. In 1925, Ronald Fisher mentioned the two-way ANOVA in his book, *Statistical Methods for Research Workers* (chapters 7 and 8). Through his work, Fisher showed that variation in experimental results could be traced to multiple causes.

In 1934, Frank Yates extended Fisher's approach by proposing computational procedures for cases with unequal sample sizes (unbalanced designs). This made the method more practical for real world experiments. Later research refined the theory of two-way ANOVA, including a Yasunori Fujikoshi's 1993 review which focused on models with unbalanced data.

With the rise of statistical computing in the late twentieth century, two-way ANOVA became widely available in software such as SAS (software), SPSS, and R (software). In 2005, Andrew Gelman proposed a new interpretation of ANOVA, as a multilevel model, framing it as a way to describe hierarchical sources of variation rather than a single hypothesis test. This view remains influential in modern statistics.

The development of the two-way ANOVA provided the foundation for analyzing factorial data. The next section describes how data are arranged for this type of analysis.

## Data set

Consider a data set in which a dependent variable may be influenced by two factors which are potential sources of variation. The first factor has I levels ( $i\in \{1,\ldots ,I\}$ ) and the second has J levels ( $j\in \{1,\ldots ,J\}$ ). Each combination $(i,j)$ defines a treatment, for a total of $I\times J$ treatments. The number of replicates for treatment $(i,j)$ i denoted by $n_{ij}$ , and let k be the index of the replicate in this treatment ( $k\in \{1,\ldots ,n_{ij}\}$ ).

From these data, we can build a contingency table, where

$n_{i+}=\sum _{j=1}^{J}n_{ij}$ and $n_{+j}=\sum _{i=1}^{I}n_{ij}$ ,

and the total number of replicates is equal to

$n=\sum _{i,j}n_{ij}=\sum _{i}n_{i+}=\sum _{j}n_{+j}$ .

The distribution of observations cross treatments determines whether the design is balanced or unbalanced. The experimental design is balanced if each treatment has the same number of replicates, K. In these cases, the design is orthogonal, which allows the effects of both factors to be distinguished independently. Thus,

$\forall i,j\;n_{ij}=K$ ,

and

$\forall i,j\;n_{ij}={\frac {n_{i+}\cdot n_{+j}}{n}}$ .

Consider an agricultural study examining how fertilizer type (factor A) and irrigation level (factor B) influence plan growth. Each fertilizer-irrigation combination represents a treatment, and several plants are measured within each group as replicates:

| **Fertilizer Type** | **Low Irrigation** | **High Irrigation** |
|---|---|---|
| None | 7, 2, 1 | 7, 6 |
| Nitrate | 11, 6 | 11, 7, 3 |
| Phosphate | 5, 3, 4 | 11, 4 |

This table shows a typical two-way layout where the rows represent one factor, columns represent another, and each cell represents a treatment combination. This layout forms the foundation for analyzing how both factors and their interactions affect the dependent variable.

This data structure forms the basis of the statistical model used in a two-way ANOVA. By defining each treatment combination mathematically, the model can describe how the factors and their interactions influence the response variable.

## Model

Upon observing variation among all n data points, for instance via a histogram, "probability may be used to describe such variation". Let us hence denote by $Y_{ijk}$ the random variable which observed value $y_{ijk}$ is the k -th measure for treatment $(i,j)$ . The two-way ANOVA models all these variables as varying independently and normally around a mean, $\mu _{ij}$ , with a constant variance, $\sigma ^{2}$ (homoscedasticity):

$Y_{ijk}\,|\,\mu _{ij},\sigma ^{2}\;{\overset {\mathrm {i.i.d.} }{\sim }}\;{\mathcal {N}}(\mu _{ij},\sigma ^{2})$ .

Specifically, the mean of the response variable is modeled as a linear combination of the explanatory variables:

$\mu _{ij}=\mu +\alpha _{i}+\beta _{j}+\gamma _{ij}$ ,

Where:

- $\mu$ is the grand mean of all observations
- $\alpha _{i}$ is the main effect of level i of the first factor
- $\beta _{j}$ is the main effect of the level j of the second factor
- $\gamma _{ij}$ is the interaction effect, representing how the combination of the two factors deviates from the sum of their separate effects.

Another equivalent way of describing the two-way ANOVA is by mentioning that, besides the variation explained by the factors, there remains some statistical noise. This amount of unexplained variation is handled via the introduction of one random variable per data point, $\epsilon _{ijk}$ , called error. These n random variables are seen as deviations from the means, and are assumed to be independent and normally distributed:

$Y_{ijk}=\mu _{ij}+\epsilon _{ijk}{\text{ with }}\epsilon _{ijk}{\overset {\mathrm {i.i.d.} }{\sim }}{\mathcal {N}}(0,\sigma ^{2})$ .

The mathematical model relies on several assumptions to ensure validity. These assumptions link the theoretical formulation of ANOVA to the conditions required for accurate interpretation of the results.

## Assumptions

The validity of a two-way ANOVA depends on several assumptions about the model and the data. These conditions ensure that the statistical tests used to compare factor effects are reliable and that the results can be meaningfully interpreted. Following Gelman and Hill, the assumptions of the ANOVA, and more generally the general linear model, are, in decreasing order of importance:

1. Relevance of the data: The data must represent the question under investigation. For example, in the fertilizer-irrigation study the measurements of plant growth should directly reflect the treatments being compared, not unrelated variation like soil differences or measurement errors.
2. Additivity and linearity: The mean of the response variable is influenced additively and linearly by the factors, unless an interaction term is included. This means that the effects of each factor combine in a way to predict the outcome, and the deviations from additivity are represented by the interaction term.
3. Independence of errors: the errors (or residuals) must be independent across observations. In the fertilizer-irrigation example, the growth of one plant should not influence the growth measurement of another. Otherwise, the assumption of independence is violated.
4. Homogeneity of variance: The variance of the dependent variable should be approximately equal across all treatment combinations (Homoscedasticity). This ensures that no group disproportionately influences the overall results.
5. Normality of residuals: The residuals within each treatment combination should follow an approximately Normal distribution. This assumption allows for valid F-test and confidence intervals in small samples, though ANOVA is robust to moderate deviations from normality when sample sizes are large.

Violations of these assumptions can distort significance tests by inflating Type I error rates or reducing Statistical power. When these conditions are not met, researchers may apply data transformations, use Nonparametric tests, or adopt Generalized linear model to better accommodate the data.

Once these assumptions are reasonably satisfied, the model parameters can be estimated to quantify the main and interaction effects of the factors.

Once these assumptions are satisfied, the model parameters can be established. Parameter estimation quantifies the contributions of each factor and their interaction within the overall analysis.

## Parameter estimation

After verifying that the data meet the assumptions of ANOVA (e.g., normality and equal variance), the next step is to estimate the model parameters. The goal of parameter estimation is to find the values that best describe how the factors and their interaction affect the outcome.

To ensure *identifiability* of parameters in a two-way ANOVA model, sum-to-zero constraints are typically imposed on the factor effects:

$\sum _{i}\alpha _{i}=\sum _{j}\beta _{j}=\sum _{i}\gamma _{ij}=\sum _{j}\gamma _{ij}=0$

These constraints remove parameter overlap, allowing the main and interaction effects to be appropriately estimated.

In a balanced design (where every group or treatment combination has the same number of samples), the values for each factor and their interaction can be estimated using the average response from each cell and the overall means. Under the assumption or normally distributed errors, these least-squares (LS) estimates are the same as maximum likelihood estimates.

In unbalanced designs (where sample sizes differ), the estimates depend on which constraint system is used. Several weighting systems exist, including *C-*, *UV-*, and *W-restrictions*, which vary in how they handle unequal group sizes. Among these, the *W-restriction* approach, where weights are proportional to the number of observations in each cell, is often preferred because it produces clearer, more interpretable parameter estimates and preserves statistical properties such as orthogonality when possible.

## Hypothesis testing

In the classical two-way ANOVA, hypothesis testing is used to determine whether either factor, or their interaction, significantly influences the dependent variable. This is achieved by dividing the total variation in the data into parts, called the *sum of squares*, that correspond to:

1. Factor A (main effect)
2. Factor B (main effect)
3. The A x B interaction
4. Random error (residual variation)

Each *sum of squares* represents how much variation in the data is explained by that source.

The null hypotheses for these tests state that each effect equals zero. That is, neither factor nor their interaction influences the outcome. The corresponding null hypotheses are:

- $H_{0}^{(A)}:\alpha _{i}=0\ \forall i$
- $H_{0}^{(B)}:\beta _{j}=0\ \forall j$
- $H_{0}^{(AB)}:\gamma _{ij}=0\ \forall i,j$

Standard practice recommends testing the *interaction term* first. If the interaction is statistically significant, it indicates that the impact of one factor depends on the level of the other factor, and the interpretation should focus on simple effects within each level.

When the interaction term is not significant, it is appropriate to examine the two main effects separately. In unbalanced designs, results can vary slightly depending on the method used to calculate sums of squares. The three most common types are Type I (sequential), Type II (hierarchical), and Type III (marginal). Most statistical software programs use Type III sums of squares because they adjust each test for all other factors in the model, making the results easier to interpret in practice.

## Unbalanced designs

While two-way ANOVA works best with equal sample sizes, real-life experiments often have unequal group sizes, resulting in an unbalanced design. When the number of observations differs across treatment combinations, the two-way ANOVA no longer has orthogonality, meaning that the variation explained by one factor is no longer entirely independent of the other. This makes it harder to separate and interpret the effects of each factor.

In such cases, two approaches can be applied:

- Eliminating the influence of one factor before testing the other (*adjusted effects*).
- Ignoring the other factor (*unadjusted effects*).

These two methods give the same results only when the sample sizes are proportional across all levels. For most practical purposes, researchers use adjusted effects to ensure that each factor's test accounts for variation already explained by the other.

Modern statistical software (e.g., R, SPSS, SAS) implements this logic automatically, but it is essential to specify which type of *sum of squares* was used in reports. In balanced or proportional designs, all types produce identical outcomes.

## Example

The following hypothetical dataset provides a simple example of how two-way ANOVA separates total variation into components explained by two experimental factors: Fertilizer type and Environmental condition. The measurements represent plant yields collected under different combinations of fertilizer and environmental settings.

|   | Extra CO2 | Extra humidity |
|---|---|---|
| No fertilizer | 7, 2, 1 | 7, 6 |
| Nitrate | 11, 6 | 10, 7, 3 |
| Phosphate | 5, 3, 4 | 11, 4 |

From these results, the total variation (SSTotal) is divided into sums of squares for each main factor, their interaction, and random error. The ANOVA summary table below shows how much variation is attributed to each source.

| **Source of variation** | **Sum of squares** | **Degrees of freedom** | **Mean square** |
|---|---|---|---|
| Fertilizer | 525.43 | 2 | 262.72 |
| Environment | 519.27 | 1 | 519.27 |
| Fertilizer x Environment | 84.83 | 2 | 42.42 |
| Error | 9.43 | 9 | 1.05 |
| **Total** | **1138.96** | **14** | - |

Finally, the F-values for each effect are calculated by dividing the mean square of the factor by the mean square of the error:

$F_{A}={\frac {MS_{A}}{MS_{E}}},\quad F_{B}={\frac {MS_{B}}{MS_{E}}},\quad F_{A\times B}={\frac {MS_{A\times B}}{MS_{E}}}.$

If the interaction term is significant, it indicates that fertilizer type and environment influence yield in combination, and the next step would be to compare simple effects within each level. If the interaction is not significant, the two main effects can be interpreted separately. This kind of interpretation is standard in biometry and experimental design.
