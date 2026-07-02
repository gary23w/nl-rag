---
title: "Main effect"
source: https://en.wikipedia.org/wiki/Main_effect
domain: factorial-design
license: CC-BY-SA-4.0
tags: factorial experiment, fractional factorial, main effect, Plackett Burman
fetched: 2026-07-02
---

# Main effect

In the design of experiments and analysis of variance, a **main effect** is the effect of an independent variable on a dependent variable averaged across the levels of any other independent variables. The term is frequently used in the context of factorial designs and regression models to distinguish main effects from interaction effects.

Relative to a factorial design, under an analysis of variance, a main effect test will test the hypotheses expected such as H0, the null hypothesis. Running a hypothesis for a main effect will test whether there is evidence of an effect of different treatments. However, a main effect test is nonspecific and will not allow for a localization of specific mean pairwise comparisons (simple effects). A main effect test will merely look at whether overall there is something about a particular factor that is making a difference. In other words, it is a test examining differences amongst the levels of a single factor (averaging over the other factor and/or factors). Main effects are essentially the overall effect of a factor.

## Definition

A factor averaged over all other levels of the effects of other factors is termed as main effect (also known as marginal effect). The contrast of a factor between levels over all levels of other factors is the main effect. The difference between the marginal means of all the levels of a factor is the main effect of the response variable on that factor. Main effects are the primary independent variables or factors tested in the experiment. Main effect is the specific effect of a factor or independent variable regardless of other parameters in the experiment. In design of experiment, it is referred to as a factor but in regression analysis it is referred to as the independent variable.

## Estimating Main Effects

In factorial designs, thus two levels each of factor A and B in a factorial design, the main effects of two factors say A and B can be calculated. The main effect of A is given by

$A={1 \over 2n}[ab+a-b-1]$

The main effect of B is given by

$B={1 \over 2n}[ab+b-a-1]$

Where n is total number of replicates. We use factor level 1 to denote the low level, and level 2 to denote the high level. The letter "a" represent the factor combination of level 2 of A and level 1 of B and "b" represents the factor combination of level 1 of A and level 2 of B. "ab" is the represents both factors at level 2. Finally, 1 represents when both factors are set to level 1.

## Hypothesis Testing for Two Way Factorial Design.

Consider a two-way factorial design in which factor A has 3 levels and factor B has 2 levels with only 1 replicate. There are 6 treatments with 5 degrees of freedom. in this example, we have two null hypotheses. The first for Factor A is: $H_{0}:\alpha _{1}=\alpha _{2}=\alpha _{3}=0$ and the second for Factor B is: $H_{0}:\beta _{1}=\beta _{2}=0$ . The main effect for factor A can be computed with 2 degrees of freedom. This variation is summarized by the sum of squares denoted by the term SSA. Likewise the variation from factor B can be computed as SSB with 1 degree of freedom. The expected value for the mean of the responses in column i is $\mu +\beta _{j}$ while the expected value for the mean of the responses in row j is $\mu +\alpha _{i}$ where i corresponds to the level of factor in factor A and j corresponds to the level of factor in factor B. $\alpha _{i}$ and $\beta _{j}$ are main effects. SSA and SSB are main-effects sums of squares. The two remaining degrees of freedom can be used to describe the variation that comes from the interaction between the two factors and can be denoted as SSAB. A table can show the layout of this particular design with the main effects (where $x_{ij}$ is the observation of the ith level of factor B and the jth level of factor A):

| Factor/Levels | $\alpha _{1}$ | $\alpha _{2}$ | $\alpha _{3}$ |
|---|---|---|---|
| $\beta _{1}$ | $x_{11}$ | $x_{12}$ | $x_{13}$ |
| $\beta _{2}$ | $x_{21}$ | $x_{22}$ | $x_{23}$ |

## Example

Take a $2^{2}$ factorial design (2 levels of two factors) testing the taste ranking of fried chicken at two fast food restaurants. Let taste testers rank the chicken from 1 to 10 (best tasting), for factor X: "spiciness" and factor Y: "crispiness." Level X1 is for "not spicy" chicken and X2 is for "spicy" chicken. Level Y1 is for "not crispy" and level Y2 is for "crispy" chicken. Suppose that five people (5 replicates) tasted all four kinds of chicken and gave a ranking of 1-10 for each. The hypotheses of interest would be: Factor X is: $H_{0}:X_{1}=X_{2}=0$ and for Factor Y is: $H_{0}:Y_{1}=Y_{2}=0$ . The table of hypothetical results is given here:

| Factor Combination | I | II | III | IV | V | Total |
|---|---|---|---|---|---|---|
| Not Spicy, Not Crispy (X1,Y1) | 3 | 2 | 6 | 1 | 9 | 21 |
| Not Spicy, Crispy (X1, Y2) | 7 | 2 | 4 | 2 | 8 | 23 |
| Spicy, Not Crispy (X2, Y1) | 5 | 5 | 6 | 1 | 8 | 25 |
| Spicy, Crispy (X2, Y2) | 9 | 10 | 8 | 6 | 8 | 41 |

The "Main Effect" of X (spiciness) when we are at Y1 (not crunchy) is given as:

${\frac {[X_{2}Y_{1}]-[X_{1}Y_{1}]}{n}}$ where n is the number of replicates. Likewise, the "Main Effect" of X at Y2 (crunchy) is given as:

${\frac {[X_{2}Y_{2}]-[X_{1}Y_{2}]}{n}}$ , upon which we can take the simple average of these two to determine the overall **main effect** of the Factor X, which results as the above

formula, written here as:

$A=X={1 \over 2n}[ab+a-b-1]$ = ${\frac {[X_{2}Y_{2}]+[X_{2}Y_{1}]-[X_{1}Y_{2}]-[X_{1}Y_{1}]}{2n}}$

Likewise, for Y, the overall **main effect** will be:

$B=Y={1 \over 2n}[ab+b-a-1]$ = ${\frac {[X_{2}Y_{2}]+[X_{1}Y_{2}]-[X_{2}Y_{1}]-[X_{1}Y_{1}]}{2n}}$

For the Chicken tasting experiment, we would have the resulting **main effects**:

$X:{\frac {[25]-[21]+[41]-[23]}{2*5}}=2.2$

$Y:{\frac {[41]-[25]+[23]-[21]}{2*5}}=1.8$
