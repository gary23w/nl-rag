---
title: "Yates analysis"
source: https://en.wikipedia.org/wiki/Yates_analysis
domain: factorial-design
license: CC-BY-SA-4.0
tags: factorial experiment, fractional factorial, main effect, Plackett Burman
fetched: 2026-07-02
---

# Yates analysis

In statistics, a **Yates analysis** is an approach to analyzing data obtained from a designed experiment where a factorial design has been used. Full- and fractional-factorial designs are common in designed experiments for engineering and scientific applications. In these designs, each factor is assigned two levels, typically called the low and high levels and referred to as "-" and "+". For computational purposes the factors are scaled so that the low level is assigned a value of -1 and the high level is assigned a value of +1.

A full factorial design contains all possible combinations of low/high levels for all the factors. A fractional factorial design contains a carefully chosen subset of these combinations. The criterion for choosing the subsets is discussed in detail in the fractional factorial designs article.

Formalized by Frank Yates, a Yates analysis exploits the special structure of these designs to generate least squares estimates for factor effects for all factors and all relevant interactions. The Yates analysis can be used to answer the following questions:

1. What is the ranked list of factors?
2. What is the goodness-of-fit (as measured by the residual standard deviation) for the various models?

The mathematical details of the Yates analysis are given in chapter 10 of Box, Hunter and Hunter (1978).

The Yates analysis is typically complemented by a number of graphical techniques such as the DOE mean plot and the DOE contour plot ("DOE" stands for "design of experiments").

## Yates' Order

Before performing a Yates analysis, the data should be arranged in "Yates' order". That is, given *k* factors, the *k*th column consists of 2(*k* - 1) minus signs (i.e., the low level of the factor) followed by 2(*k* - 1) plus signs (i.e., the high level of the factor). For example, for a full factorial design with three factors, the design matrix is

$---$

$+--$

$-+-$

$++-$

$--+$

$+-+$

$-++$

$+++$

To better understand and utilize the sign table above, one method of detailing the factors and treatment combinations is called modern notation. The notation is a shorthand that arises from taking the subscripts of each treatment combination, making them exponents, evaluating the resulting expression and using that as the new name of the treatment combination. Note that while the names look very much like algebraic expressions, they are simply names and no new values are assigned. Taking the 3-factor, 2-level model from above, in Yates' order the response variables are:

$a_{0}b_{0}c_{0},a_{1}b_{0}c_{0},a_{0}b_{1}c_{0},a_{1}b_{1}c_{0},a_{0}b_{0}c_{1},a_{1}b_{0}c_{1},a_{0}b_{1}c_{1},a_{1}b_{1}c_{1}$

which in modern notation becomes:

$1,a,b,ab,c,ac,bc,abc$

in which it is evident that the exponents in the modern notation names are simply the subscripts of the former (note that anything raised to the zeroth power is 1 and anything raised to the first power is itself). Each response variable then gets assigned row-wise to the table above. Thus the first row is for 1 , the second row is for a and so on. The signs in each column then represent the signs each response variable should take in the calculation of the effect estimates for that factor.

Determining the Yates' order for fractional factorial designs requires knowledge of the confounding structure of the fractional factorial design.

## Output

A Yates analysis generates the following output.

- A factor identifier (from Yates' order). The specific identifier will vary depending on the program used to generate the Yates analysis. Dataplot, for example, uses the following for a 3-factor model.

1 = factor 1

2 = factor 2

3 = factor 3

12 = interaction of factor 1 and factor 2

13 = interaction of factor 1 and factor 3

23 = interaction of factor 2 and factor 3

123 = interaction of factors 1, 2, and 3

- A ranked list of important factors. That is, least squares estimated factor effects ordered from largest in magnitude (most significant) to smallest in magnitude (least significant).

To determine the magnitudes, the response variables are first arranged in Yates' order, as described in the aforementioned section above. Then, terms are added and subtracted pairwise to determine the next column. More specifically, given the values of the response variables (as they should have been obtained from the experiment directly) in Yates' order, the first two terms are added and that sum is now the first term in the new column. The next two terms are then added and that is the second term in the new column. Since the terms are added pairwise, half of the new column is now filled and should be composed entirely of the pairwise sums of the data. The second half of the column is found in an analogous manner, only the pairwise differences are taken, where the first term is subtracted from the second, the third from the fourth, and so on. Thus completes the column. Should more columns be needed, the same process is repeated, only using the new column. In other words, the nth column is generated from the (n-1)th column (Berger et al. calls this process "Yatesing the data"). In a $2^{k}$ design, k columns will be required, and the last column is the column used to calculate the effect estimates.

- A t-value for the individual factor effect estimates. The t-value is computed as

$t={\frac {e}{s_{e}}}$

where *e* is the estimated factor effect and *se* is the standard deviation of the estimated factor effect.

- The residual standard deviation that results from the model with the single term only. That is, the residual standard deviation from the model

${\textrm {response}}={\textrm {constant}}+0.5X_{i}$

where *Xi* is the estimate of the *i*th factor or interaction effect.

- The cumulative residual standard deviation that results from the model using the current term plus all terms preceding that term. That is,

${\textrm {response}}={\textrm {constant}}+0.5\mathrm {(all\ effect\ estimates\ down\ to\ and\ including\ the\ effect\ of\ interest)}$

This consists of a monotonically decreasing set of residual standard deviations (indicating a better fit as the number of terms in the model increases). The first cumulative residual standard deviation is for the model

${\textrm {response}}={\textrm {constant}}$

where the constant is the overall mean of the response variable. The last cumulative residual standard deviation is for the model

${\textrm {response}}={\textrm {constant}}+0.5\mathrm {(all\ factor\ and\ interaction\ estimates)}$

This last model will have a residual standard deviation of zero.

## Example

(Adapted from Berger et al., chapter 9) Say there is a study done where one is selling some product by mail and is trying to determine the effect of three factors (postage, product price, envelope size) on people's response rate (that is, will they buy the product). Each factor has two levels: for postage (labeled A), they are third-class (low) and first-class (high), for product price (labeled B) the low level is $9.95 and the high level is $12.95, and for envelope size (labeled C) the low level is #10 and the high level is 9x12. From the experiment, the following data are acquired. Note that the response rate is given as a proportion of the people who answered the survey (favorably and unfavorably) for each treatment combination.

| Treatmemt combination | Response rate |
|---|---|
| 1 | 0.062 |
| a | 0.074 |
| b | 0.010 |
| ab | 0.020 |
| c | 0.057 |
| ac | 0.082 |
| bc | 0.024 |
| abc | 0.027 |

Singling out factor A (postage) for calculation for now, the overall estimate for A must take into account the interaction effects of B and C on it as well. The four terms for calculation are:

1. a –1, estimate of A with B and C low
2. ab – b, estimate of A with B high and C low
3. ac – c, estimate of A with B low and C high
4. abc – bc, estimate of A with B and C high

The total estimate is the sum of these four terms divided by four. In other words, the estimate of A is

$E_{a}=(a+ab+ac+abc-1-b-c-bc)/4$

where the sum has been rearranged to have all the positive terms grouped together and the negatives together for ease of viewing. In Yates' order, the sum is written as

$E_{a}=(-1+a-b+ab-c+ac-bc+abc)/4$

The estimates for B and C can be determined in a similar fashion. Calculating the interaction effects is also similar, but the responses are averaged over all other effects not considered.

The full table of signs for a three-factor, two-level design is given to the right. Both the factors (columns) and the treatment combinations (rows) are written in Yates' order. The value of arranging the sum in Yates' order is now apparent, as only the signs need to be altered according to the table to produce the effect estimates for every treatment combination. Observe that the columns for A, B, and C are the same as those in the design matrix in the above Yates' order section. Observe also that the columns of the interaction effects can be produced by taking the dot product of the columns of the individual factors (i.e., multiplying the columns element-wise to produce another column of the same length). Note that all sums must divided by 4 to yield the actual effect estimate, as shown earlier. Using this table, the effect estimates are calculated as:

| Treatmemt combination | Effect estimate |
|---|---|
| A | 0.0125 |
| B | –0.0485 |
| AB | –0.0060 |
| C | 0.0060 |
| AC | 0.0015 |
| BC | 0.0045 |
| ABC | –0.0050 |

A positive value means that an increase in the factor creates an increase in the response rate, while a negative value means that that same factor increase actually produces a decrease in the response rate. Note however that these effects have not yet been determined to be statistically significant, only that there are such effects on the response rate for each factor. Statistical significance must be ascertained via other methods such as analysis of variance (ANOVA).

Further reading can be found in Berger et al., chapter 9.

## Parameter estimates as terms are added

In most cases of least squares fitting, the model coefficients for previously added terms change depending on what was successively added. For example, the *X*1 coefficient might change depending on whether or not an *X*2 term was included in the model. This is not the case when the design is orthogonal, as is a 23 full factorial design. For orthogonal designs, the estimates for the previously included terms do not change as additional terms are added. This means the ranked list of effect estimates simultaneously serves as the least squares coefficient estimates for progressively more complicated models.

## Model selection and validation

From the above Yates output, one can define the potential models from the Yates analysis. An important component of a Yates analysis is selecting the best model from the available potential models. The above step lists all the potential models. From this list, we want to select the most appropriate model. This requires balancing the following two goals.

1. We want the model to include all important factors.
2. We want the model to be parsimonious. That is, the model should be as simple as possible.

In short, we want our model to include all the important factors and interactions and to omit the unimportant factors and interactions. Note that the residual standard deviation alone is insufficient for determining the most appropriate model as it will always be decreased by adding additional factors. Instead, seven criteria are utilized to define important factors. These seven criteria are not all equally important, nor will they yield identical subsets, in which case a consensus subset or a weighted consensus subset must be extracted. In practice, some of these criteria may not apply in all situations, and some analysts may have additional criteria. These criteria are given as useful guidelines. Mosts analysts will focus on those criteria that they find most useful.

1. Practical significance of effects
2. Order of magnitude of effects
3. Statistical significance of effects
4. Probability plots of effects
5. Youden plot of averages
6. Practical significance of residual standard deviation
7. Statistical significance of residual standard deviation

The first four criteria focus on effect sizes with three numeric criteria and one graphical criterion. The fifth criterion focuses on averages. The last two criteria focus on the residual standard deviation of the model. Once a tentative model has been selected, the error term should follow the assumptions for a univariate measurement process. That is, the model should be validated by analyzing the residuals.

## Graphical presentation

Some analysts may prefer a more graphical presentation of the Yates results. In particular, the following plots may be useful:

1. Ordered data plot
2. Ordered absolute effects plot
3. Cumulative residual standard deviation plot

- Multi-factor analysis of variance
- DOE mean plot
- Block plot
- DOE contour plot
