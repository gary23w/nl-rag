---
title: "Coefficient of determination"
source: https://en.wikipedia.org/wiki/Coefficient_of_determination
domain: linear-regression
license: CC-BY-SA-4.0
tags: linear regression, ordinary least squares, regression coefficients, least squares
fetched: 2026-07-02
---

# Coefficient of determination

In statistics, the **coefficient of determination**, denoted *R*2 or *r*2 and pronounced "R squared", is the proportion of the variation in the dependent variable that is predictable from the independent variable(s). It is a statistic used in the context of statistical models whose main purpose is either the prediction of future outcomes or the testing of hypotheses, on the basis of other related information. It provides a measure of how well observed outcomes are replicated by the model, based on the proportion of total variation of outcomes explained by the model.

There are several definitions of *R*2 that are only sometimes equivalent. In simple linear regression (which includes an intercept), *r*2 is simply the square of the sample *correlation coefficient* (*r*), between the observed outcomes and the observed predictor values. If additional regressors are included, *R*2 is the square of the *coefficient of multiple correlation*. In both such cases, the coefficient of determination is always smaller than 1 and usually greater than 0.

Cases where *R*2 is negative can arise when the predictions that are being compared to the corresponding outcomes have not been derived from a model-fitting procedure using those data. Even if a model-fitting procedure has been used, *R*2 may still be negative, for example when linear regression is conducted without including an intercept, or when a non-linear function is used to fit the data. In cases where negative values arise, the mean of the data provides a better fit to the outcomes than do the fitted function values, according to this particular criterion.

The coefficient of determination can be more intuitively informative than MAE, MAPE, MSE, and RMSE in regression analysis evaluation, as the former can be expressed as a percentage, whereas the latter measures have arbitrary ranges. It also proved more robust for poor fits compared to SMAPE on certain test datasets.

When evaluating the goodness-of-fit of simulated (*Y*pred) versus measured (*Y*obs) values, it is not appropriate to base this on the *R*2 of the linear regression (i.e., *Y*obs=*m*·*Y*pred + b). The *R*2 quantifies the degree of any linear correlation between *Y*obs and *Y*pred, while for the goodness-of-fit evaluation only one specific linear correlation should be taken into consideration: *Y*obs=1·*Y*pred + 0 (i.e., the 1:1 line).

## Definitions

A data set has *n* values marked *y*1, ..., *y**n* (collectively known as *y**i* or as a vector ***y***=[*y*1, ..., *y**n*]T), each associated with a fitted (or modeled, or predicted) value *f*1, ..., *f**n* (known as *f**i*, or sometimes *ŷ**i*, as a vector ***f***).

Define the residuals as *e**i*=*y**i* − *f**i* (forming a vector ***e***).

If ${\bar {y}}$ is the mean of the observed data: ${\bar {y}}={\frac {1}{n}}\sum _{i=1}^{n}y_{i}$ then the variability of the data set can be measured with two sums of squares formulas:

- The sum of squares of residuals, also called the residual sum of squares: $SS_{\text{res}}=\sum _{i}(y_{i}-f_{i})^{2}=\sum _{i}e_{i}^{2}\,$
- The total sum of squares (proportional to the variance of the data): $SS_{\text{tot}}=\sum _{i}(y_{i}-{\bar {y}})^{2}$

The most general definition of the coefficient of determination is $R^{2}=1-{SS_{\rm {res}} \over SS_{\rm {tot}}}$

In the best case, the modeled values exactly match the observed values, which results in $SS_{\text{res}}=0$ and *R*2=1. A baseline model, which always predicts *y*, will have *R*2=0.

### Relation to unexplained variance

In a general form, *R*2 can be seen to be related to the fraction of variance unexplained (FVU), since the second term compares the unexplained variance (variance of the model's errors) with the total variance (of the data): $R^{2}=1-{\text{FVU}}$

### As explained variance

A larger value of *R*2 implies a more successful regression model. Suppose *R*2=0.49. This implies that 49% of the variability of the dependent variable in the data set has been accounted for, and the remaining 51% of the variability is still unaccounted for. For regression models, the regression sum of squares, also called the explained sum of squares, is defined as

$SS_{\text{reg}}=\sum _{i}(f_{i}-{\bar {y}})^{2}$

In some cases, as in simple linear regression, the total sum of squares equals the sum of the two other sums of squares defined above:

$SS_{\text{res}}+SS_{\text{reg}}=SS_{\text{tot}}$

See Partitioning in the general OLS model for a derivation of this result for one case where the relation holds. When this relation does hold, the above definition of *R*2 is equivalent to

$R^{2}={\frac {SS_{\text{reg}}}{SS_{\text{tot}}}}={\frac {SS_{\text{reg}}/n}{SS_{\text{tot}}/n}}$

where *n* is the number of observations (cases) on the variables.

In this form *R*2 is expressed as the ratio of the explained variance (variance of the model's predictions, which is *SS*reg / *n*) to the total variance (sample variance of the dependent variable, which is *SS*tot / *n*).

This partition of the sum of squares holds for instance when the model values *ƒ**i* have been obtained by linear regression. A milder sufficient condition reads as follows: The model has the form

$f_{i}={\widehat {\alpha }}+{\widehat {\beta }}q_{i}$

where the *q**i* are arbitrary values that may or may not depend on *i* or on other free parameters (the common choice *q**i* = *x**i* is just one special case), and the coefficient estimates ${\widehat {\alpha }}$ and ${\widehat {\beta }}$ are obtained by minimizing the residual sum of squares.

This set of conditions is an important one and it has a number of implications for the properties of the fitted residuals and the modelled values. In particular, under these conditions:

${\bar {f}}={\bar {y}}.\,$

### As squared correlation coefficient

In linear least squares multiple regression (with fitted intercept and slope), *R*2 equals $\rho ^{2}(y,f)$ the square of the Pearson correlation coefficient between the observed y and modeled (predicted) f data values of the dependent variable.

In a linear least squares regression with a single explanator (with fitted intercept and slope), this is also equal to $\rho ^{2}(y,x)$ the squared Pearson correlation coefficient between the dependent variable y and explanatory variable x .

It should not be confused with the correlation coefficient between two explanatory variables, defined as

$\rho _{{\widehat {\alpha }},{\widehat {\beta }}}={\operatorname {cov} \left({\widehat {\alpha }},{\widehat {\beta }}\right) \over \sigma _{\widehat {\alpha }}\sigma _{\widehat {\beta }}},$

where the covariance between two coefficient estimates, as well as their standard deviations, are obtained from the covariance matrix of the coefficient estimates, $(X^{T}X)^{-1}$ .

Under more general modeling conditions, where the predicted values might be generated from a model different from linear least squares regression, an *R*2 value can be calculated as the square of the correlation coefficient between the original y and modeled f data values. In this case, the value is not directly a measure of how good the modeled values are, but rather a measure of how good a predictor might be constructed from the modeled values (by creating a revised predictor of the form *α* + *βƒ**i*). According to Everitt, this usage is specifically the definition of the term "coefficient of determination": the square of the correlation between two (general) variables.

## Interpretation

*R*2 is a measure of the goodness of fit of a model. In regression, the *R*2 coefficient of determination is a statistical measure of how well the regression predictions approximate the real data points. An *R*2 of 1 indicates that the regression predictions perfectly fit the data.

Values of *R*2 outside the range 0 to 1 occur when the model fits the data worse than the worst possible least-squares predictor (equivalent to a horizontal hyperplane at a height equal to the mean of the observed data). This occurs when a wrong model was chosen, or nonsensical constraints were applied by mistake. If equation 1 of Kvålseth is used (this is the equation used most often), *R*2 can be less than zero. If equation 2 of Kvålseth is used, *R*2 can be greater than one.

In all instances where *R*2 is used, the predictors are calculated by ordinary least-squares regression: that is, by minimizing *SS*res. In this case, *R*2 increases as the number of variables in the model is increased (*R*2 is monotone increasing with the number of variables included—it will never decrease). This illustrates a drawback to one possible use of *R*2, where one might keep adding variables (kitchen sink regression) to increase the *R*2 value. For example, if one is trying to predict the sales of a model of car from the car's gas mileage, price, and engine power, one can include probably irrelevant factors such as the first letter of the model's name or the height of the lead engineer designing the car because the *R*2 will never decrease as variables are added and will likely experience an increase due to chance alone.

This leads to the alternative approach of looking at the adjusted *R*2. The explanation of this statistic is almost the same as *R*2 but it penalizes the statistic as extra variables are included in the model. For cases other than fitting by ordinary least squares, the *R*2 statistic can be calculated as above and may still be a useful measure. If fitting is by weighted least squares or generalized least squares, alternative versions of *R*2 can be calculated appropriate to those statistical frameworks, while the "raw" *R*2 may still be useful if it is more easily interpreted. Values for *R*2 can be calculated for any type of predictive model, which need not have a statistical basis.

### In a multiple linear model

Consider a linear model with more than a single explanatory variable, of the form

$Y_{i}=\beta _{0}+\sum _{j=1}^{p}\beta _{j}X_{i,j}+\varepsilon _{i},$

where, for the *i*th case, ${Y_{i}}$ is the response variable, $X_{i,1},\dots ,X_{i,p}$ are *p* regressors, and $\varepsilon _{i}$ is a mean zero error term. The quantities $\beta _{0},\dots ,\beta _{p}$ are unknown coefficients, whose values are estimated by least squares. The coefficient of determination *R*2 is a measure of the global fit of the model. Specifically, *R*2 is an element of [0, 1] and represents the proportion of variability in *Y**i* that may be attributed to some linear combination of the regressors (explanatory variables) in *X*.

*R*2 is often interpreted as the proportion of response variation "explained" by the regressors in the model. Thus, *R*2 = 1 indicates that the fitted model explains all variability in y , while *R*2 = 0 indicates no 'linear' relationship (for straight line regression, this means that the straight line model is a constant line (slope = 0, intercept =  ${\bar {y}}$ ) between the response variable and regressors). An interior value such as *R*2 = 0.7 may be interpreted as follows: "Seventy percent of the variance in the response variable can be explained by the explanatory variables. The remaining thirty percent can be attributed to unknown, lurking variables or inherent variability."

A caution that applies to *R*2, as to other statistical descriptions of correlation and association is that "correlation does not imply causation". In other words, while correlations may sometimes provide valuable clues in uncovering causal relationships among variables, a non-zero estimated correlation between two variables is not, on its own, evidence that changing the value of one variable would result in changes in the values of other variables. For example, the practice of carrying matches (or a lighter) is correlated with incidence of lung cancer, but carrying matches does not cause cancer (in the standard sense of "cause").

In case of a single regressor, fitted by least squares, *R*2 is the square of the Pearson product-moment correlation coefficient relating the regressor and the response variable. More generally, *R*2 is the square of the correlation between the constructed predictor and the response variable. With more than one regressor, the *R*2 can be referred to as the coefficient of multiple determination.

### Inflation of *R*2

In least squares regression using typical data, *R*2 is at least weakly increasing with an increase in number of regressors in the model. Because increases in the number of regressors increase the value of *R*2, *R*2 alone cannot be used as a meaningful comparison of models with very different numbers of independent variables. For a meaningful comparison between two models, an F-test can be performed on the residual sum of squares , similar to the F-tests in Granger causality, though this is not always appropriate. As a reminder of this, some authors denote *R*2 by *R**q*2, where *q* is the number of columns in *X* (the number of explanators including the constant).

To demonstrate this property, first recall that the objective of least squares linear regression is

$\min _{b}SS_{\text{res}}(b)\Rightarrow \min _{b}\sum _{i}(y_{i}-X_{i}b)^{2}\,$

where *Xi* is a row vector of values of explanatory variables for case *i* and *b* is a column vector of coefficients of the respective elements of *Xi*.

The optimal value of the objective is weakly smaller as more explanatory variables are added and hence additional columns of X (the explanatory data matrix whose *i*th row is *Xi*) are added, by the fact that less constrained minimization leads to an optimal cost which is weakly smaller than more constrained minimization does. Given the previous conclusion and noting that $SS_{tot}$ depends only on *y*, the non-decreasing property of *R*2 follows directly from the definition above.

The intuitive reason that using an additional explanatory variable cannot lower the *R*2 is this: Minimizing $SS_{\text{res}}$ is equivalent to maximizing *R*2. When the extra variable is included, the data always have the option of giving it an estimated coefficient of zero, leaving the predicted values and the *R*2 unchanged. The only way that the optimization problem will give a non-zero coefficient is if doing so improves the *R*2.

The above gives an analytical explanation of the inflation of *R*2. Next, an example based on ordinary least square from a geometric perspective is shown below.

A simple case to be considered first:

$Y=\beta _{0}+\beta _{1}\cdot X_{1}+\varepsilon \,$

This equation describes the ordinary least squares regression model with one regressor. The prediction is shown as the red vector in the figure on the right. Geometrically, it is the projection of true value onto a model space in $\mathbb {R}$ (without intercept). The residual is shown as the red line.

$Y=\beta _{0}+\beta _{1}\cdot X_{1}+\beta _{2}\cdot X_{2}+\varepsilon \,$

This equation corresponds to the ordinary least squares regression model with two regressors. The prediction is shown as the blue vector in the figure on the right. Geometrically, it is the projection of true value onto a larger model space in $\mathbb {R} ^{2}$ (without intercept). Noticeably, the values of $\beta _{0}$ and $\beta _{0}$ are not the same as in the equation for smaller model space as long as $X_{1}$ and $X_{2}$ are not zero vectors. Therefore, the equations are expected to yield different predictions (i.e., the blue vector is expected to be different from the red vector). The least squares regression criterion ensures that the residual is minimized. In the figure, the blue line representing the residual is orthogonal to the model space in $\mathbb {R} ^{2}$ , giving the minimal distance from the space.

The smaller model space is a subspace of the larger one, and thereby the residual of the smaller model is guaranteed to be larger. Comparing the red and blue lines in the figure, the blue line is orthogonal to the space, and any other line would be larger than the blue one. Considering the calculation for *R*2, a smaller value of $SS_{tot}$ will lead to a larger value of *R*2, meaning that adding regressors will result in inflation of *R*2.

### Caveats

*R*2 does not indicate whether:

- the independent variables are a cause of the changes in the dependent variable;
- omitted-variable bias exists;
- the correct regression was used;
- the most appropriate set of independent variables has been chosen;
- there is collinearity present in the data on the explanatory variables;
- the model might be improved by using transformed versions of the existing set of independent variables;
- there are enough data points to make a solid conclusion;
- there are a few outliers in an otherwise good sample.

## Extensions

### Adjusted *R*2

The use of an adjusted *R*2 (one common notation is ${\bar {R}}^{2}$ , pronounced "R bar squared"; another is $R_{\text{a}}^{2}$ or $R_{\text{adj}}^{2}$ ) is an attempt to account for the phenomenon of the *R*2 automatically increasing when extra explanatory variables are added to the model. There are many different ways of adjusting. By far the most used one, to the point that it is typically just referred to as adjusted *R*, is the correction proposed by Mordecai Ezekiel. The adjusted *R*2 is defined as

${\bar {R}}^{2}={1-{SS_{\text{res}}/{\text{df}}_{\text{res}} \over SS_{\text{tot}}/{\text{df}}_{\text{tot}}}}$

where df*res* is the degrees of freedom of the estimate of the population variance around the model, and df*tot* is the degrees of freedom of the estimate of the population variance around the mean. df*res* is given in terms of the sample size *n* and the number of variables *p* in the model, df*res*=*n* − *p* − 1. df*tot* is given in the same way, but with *p* being zero for the mean (i.e., df*tot*=*n* − 1).

Inserting the degrees of freedom and using the definition of *R*2, it can be rewritten as:

${\bar {R}}^{2}=1-(1-R^{2}){n-1 \over n-p-1}$

where *p* is the total number of explanatory variables in the model (excluding the intercept), and *n* is the sample size.

The adjusted *R*2 can be negative, and its value will always be less than or equal to that of *R*2. Unlike *R*2, the adjusted *R*2 increases only when the increase in *R*2 (due to the inclusion of a new explanatory variable) is more than one would expect to see by chance. If a set of explanatory variables with a predetermined hierarchy of importance are introduced into a regression one at a time, with the adjusted *R*2 computed each time, the level at which adjusted *R*2 reaches a maximum, and decreases afterward, would be the regression with the ideal combination of having the best fit without excess/unnecessary terms.

The adjusted *R*2 can be interpreted as an instance of the bias-variance tradeoff. When we consider the performance of a model, a lower error represents a better performance. When the model becomes more complex, the variance will increase whereas the square of bias will decrease, and these two metrics add up to be the total error. Combining these two trends, the bias-variance tradeoff describes a relationship between the performance of the model and its complexity, which is shown as a u-shape curve on the right. For the adjusted *R*2 specifically, the model complexity (i.e. number of parameters) affects the *R*2 and the term / frac and thereby captures their attributes in the overall performance of the model.

*R*2 can be interpreted as the variance of the model, which is influenced by the model complexity. A high *R*2 indicates a lower bias error because the model can better explain the change of Y with predictors. For this reason, we make fewer (erroneous) assumptions, and this results in a lower bias error. Meanwhile, to accommodate fewer assumptions, the model tends to be more complex. Based on bias-variance tradeoff, a higher complexity will lead to a decrease in bias and a better performance (below the optimal line). In *R*2, the term (1 − *R*2) will be lower with high complexity and resulting in a higher *R*2, consistently indicating a better performance.

On the other hand, the term/frac term is reversely affected by the model complexity. The term/frac will increase when adding regressors (i.e., increased model complexity) and lead to worse performance. Based on bias-variance tradeoff, a higher model complexity (beyond the optimal line) leads to increasing errors and a worse performance.

Considering the calculation of *R*2, more parameters will increase the *R*2 and lead to an increase in *R*2. Nevertheless, adding more parameters will increase the term/frac and thus decrease *R*2. These two trends construct a reverse u-shape relationship between model complexity and *R*2, which is in consistent with the u-shape trend of model complexity versus overall performance. Unlike *R*2, which will always increase when model complexity increases, *R*2 will increase only when the bias eliminated by the added regressor is greater than the variance introduced simultaneously. Using *R*2 instead of *R*2 could thereby prevent overfitting.

Following the same logic, adjusted *R*2 can be interpreted as a less biased estimator of the population *R*2, whereas the observed sample *R*2 is a positively biased estimate of the population value. Adjusted *R*2 is more appropriate when evaluating model fit (the variance in the dependent variable accounted for by the independent variables) and in comparing alternative models in the feature selection stage of model building.

The principle behind the adjusted *R*2 statistic can be seen by rewriting the ordinary *R*2 as

$R^{2}={1-{{\text{VAR}}_{\text{res}} \over {\text{VAR}}_{\text{tot}}}}$

where ${\text{VAR}}_{\text{res}}=SS_{\text{res}}/n$ and ${\text{VAR}}_{\text{tot}}=SS_{\text{tot}}/n$ are the sample variances of the estimated residuals and the dependent variable respectively, which can be seen as biased estimates of the population variances of the errors and of the dependent variable. These estimates are replaced by statistically unbiased versions: ${\text{VAR}}_{\text{res}}=SS_{\text{res}}/(n-p)$ and ${\text{VAR}}_{\text{tot}}=SS_{\text{tot}}/(n-1)$ .

Despite using unbiased estimators for the population variances of the error and the dependent variable, adjusted *R*2 is not an unbiased estimator of the population *R*2, which results by using the population variances of the errors and the dependent variable instead of estimating them. Ingram Olkin and John W. Pratt derived the minimum-variance unbiased estimator for the population *R*2, which is known as Olkin–Pratt estimator. Comparisons of different approaches for adjusting *R*2 concluded that in most situations either an approximate version of the Olkin–Pratt estimator or the exact Olkin–Pratt estimator should be preferred over (Ezekiel) adjusted *R*2.

### Coefficient of partial determination

The coefficient of partial determination can be defined as the proportion of variation that cannot be explained in a reduced model, but can be explained by the predictors specified in a full model. This coefficient is used to provide insight into whether or not one or more additional predictors may be useful in a more fully specified regression model.

The calculation for the partial *R*2 is relatively straightforward after estimating two models and generating the ANOVA tables for them. The calculation for the partial *R*2 is

${\frac {SS_{\text{ res, reduced}}-SS_{\text{ res, full}}}{SS_{\text{ res, reduced}}}},$

which is analogous to the usual coefficient of determination:

${\frac {SS_{\text{tot}}-SS_{\text{res}}}{SS_{\text{tot}}}}.$

### Generalizing and decomposing *R*2

As explained above, model selection heuristics such as the adjusted *R*2 criterion and the F-test examine whether the total *R*2 sufficiently increases to determine if a new regressor should be added to the model. If a regressor is added to the model that is highly correlated with other regressors which have already been included, then the total *R*2 will hardly increase, even if the new regressor is of relevance. As a result, the above-mentioned heuristics will ignore relevant regressors when cross-correlations are high.

Alternatively, one can decompose a generalized version of *R*2 to quantify the relevance of deviating from a hypothesis. As Hoornweg (2018) shows, several shrinkage estimators – such as Bayesian linear regression, ridge regression, and the (adaptive) lasso – make use of this decomposition of *R*2 when they gradually shrink parameters from the unrestricted OLS solutions towards the hypothesized values. Let us first define the linear regression model as

$y=X\beta +\varepsilon .$

It is assumed that the matrix *X* is standardized with Z-scores and that the column vector y is centered to have a mean of zero. Let the column vector $\beta _{0}$ refer to the hypothesized regression parameters and let the column vector b denote the estimated parameters. We can then define

$R^{2}=1-{\frac {(y-Xb)'(y-Xb)}{(y-X\beta _{0})'(y-X\beta _{0})}}.$

An *R*2 of 75% means that the in-sample accuracy improves by 75% if the data-optimized *b* solutions are used instead of the hypothesized $\beta _{0}$ values. In the special case that $\beta _{0}$ is a vector of zeros, we obtain the traditional *R*2 again.

The individual effect on *R*2 of deviating from a hypothesis can be computed with $R^{\otimes }$ ('R-outer'). This p times p matrix is given by

$R^{\otimes }=(X'{\tilde {y}}_{0})(X'{\tilde {y}}_{0})'(X'X)^{-1}({\tilde {y}}_{0}'{\tilde {y}}_{0})^{-1},$

where ${\tilde {y}}_{0}=y-X\beta _{0}$ . The diagonal elements of $R^{\otimes }$ exactly add up to *R*2. If regressors are uncorrelated and $\beta _{0}$ is a vector of zeros, then the $j^{\text{th}}$ diagonal element of $R^{\otimes }$ simply corresponds to the *r*2 value between $x_{j}$ and y . When regressors $x_{i}$ and $x_{j}$ are correlated, $R_{ii}^{\otimes }$ might increase at the cost of a decrease in $R_{jj}^{\otimes }$ . As a result, the diagonal elements of $R^{\otimes }$ may be smaller than 0 and, in more exceptional cases, larger than 1. To deal with such uncertainties, several shrinkage estimators implicitly take a weighted average of the diagonal elements of $R^{\otimes }$ to quantify the relevance of deviating from a hypothesized value. Click on the lasso for an example.

### *R*2 in logistic regression

In the case of logistic regression, usually fit by maximum likelihood, there are several choices of pseudo-*R*2.

One is the generalized *R*2 originally proposed by Cox & Snell, and independently by Magee:

$R^{2}=1-\left({{\mathcal {L}}(0) \over {\mathcal {L}}({\widehat {\theta }})}\right)^{2/n}$

where ${\mathcal {L}}(0)$ is the likelihood of the model with only the intercept, ${{\mathcal {L}}({\widehat {\theta }})}$ is the likelihood of the estimated model (i.e., the model with a given set of parameter estimates) and *n* is the sample size. It is easily rewritten to:

$R^{2}=1-e^{{\frac {2}{n}}(\ln({\mathcal {L}}(0))-\ln({\mathcal {L}}({\widehat {\theta }})))}=1-e^{-D/n}$

where *D* is the test statistic of the likelihood ratio test.

Nico Nagelkerke noted that it had the following properties:

1. It is consistent with the classical coefficient of determination when both can be computed;
2. Its value is maximised by the maximum likelihood estimation of a model;
3. It is asymptotically independent of the sample size;
4. The interpretation is the proportion of the variation explained by the model;
5. The values are between 0 and 1, with 0 denoting that model does not explain any variation and 1 denoting that it perfectly explains the observed variation;
6. It does not have any unit.

However, in the case of a logistic model, where ${\mathcal {L}}({\widehat {\theta }})$ cannot be greater than 1, *R*2 is between 0 and $R_{\max }^{2}=1-({\mathcal {L}}(0))^{2/n}$ : thus, Nagelkerke suggested the possibility to define a scaled *R*2 as *R*2/*R*2max.

## Comparison with residual statistics

Occasionally, residual statistics are used for indicating goodness of fit. The norm of residuals is calculated as the square-root of the sum of squares of residuals (SSR):

${\text{norm of residuals}}={\sqrt {SS_{\text{res}}}}=\|e\|.$

Similarly, the reduced chi-square is calculated as the SSR divided by the degrees of freedom.

Both *R*2 and the norm of residuals have their relative merits. For least squares analysis *R*2 varies between 0 and 1, with larger numbers indicating better fits and 1 representing a perfect fit. The norm of residuals varies from 0 to infinity with smaller numbers indicating better fits and zero indicating a perfect fit. One advantage and disadvantage of *R*2 is the $SS_{\text{tot}}$ term acts to normalize the value. If the *yi* values are all multiplied by a constant, the norm of residuals will also change by that constant but *R*2 will stay the same. As a basic example, for the linear least squares fit to the set of data:

| x | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| y | 1.9 | 3.7 | 5.8 | 8.0 | 9.6 |

*R*2=0.998, and norm of residuals=0.302. If all values of *y* are multiplied by 1000 (for example, in an SI prefix change), then *R*2 remains the same, but norm of residuals=302.

Another single-parameter indicator of fit is the RMSE of the residuals, or standard deviation of the residuals. This would have a value of 0.135 for the above example given that the fit was linear with an unforced intercept.

## History

The creation of the coefficient of determination has been attributed to the geneticist Sewall Wright and was first published in 1921.
