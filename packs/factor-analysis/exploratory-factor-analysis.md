---
title: "Exploratory factor analysis"
source: https://en.wikipedia.org/wiki/Exploratory_factor_analysis
domain: factor-analysis
license: CC-BY-SA-4.0
tags: factor analysis, exploratory factor analysis, varimax rotation, latent variable
fetched: 2026-07-02
---

# Exploratory factor analysis

In multivariate statistics, **exploratory factor analysis** (**EFA**) is a statistical method used to uncover the underlying structure of a relatively large set of variables. EFA is a technique within factor analysis whose overarching goal is to identify the underlying relationships between measured variables. It is commonly used by researchers when developing a scale (a *scale* is a collection of questions used to measure a particular research topic) and serves to identify a set of latent constructs underlying a battery of measured variables. It should be used when the researcher has no *a priori* hypothesis about factors or patterns of measured variables. *Measured variables* are any one of several attributes of people that may be observed and measured. Examples of measured variables could be the physical height, weight, and pulse rate of a human being. Usually, researchers would have a large number of measured variables, which are assumed to be related to a smaller number of "unobserved" factors. Researchers must carefully consider the number of measured variables to include in the analysis. EFA procedures are more accurate when each factor is represented by multiple measured variables in the analysis.

EFA is based on the common factor model. In this model, manifest variables are expressed as a function of common factors, unique factors, and errors of measurement. Each unique factor influences only one manifest variable, and does not explain correlations between manifest variables. Common factors influence more than one manifest variable and "factor loadings" are measures of the influence of a common factor on a manifest variable. For the EFA procedure, we are more interested in identifying the common factors and the related manifest variables.

EFA assumes that any indicator/measured variable may be associated with any factor. When developing a scale, researchers should use EFA first before moving on to confirmatory factor analysis. EFA is essential to determine underlying factors/constructs for a set of measured variables; while confirmatory factor analysis allows the researcher to test the hypothesis that a relationship between the observed variables and their underlying latent factor(s)/construct(s) exists. EFA requires the researcher to make a number of important decisions about how to conduct the analysis because there is no one set method.

## Fitting procedures

Fitting procedures are used to estimate the factor loadings and unique variances of the model (*Factor loadings* are the regression coefficients between items and factors and measure the influence of a common factor on a measured variable). There are several factor analysis fitting methods to choose from, however there is little information on all of their strengths and weaknesses and many don't even have an exact name that is used consistently. Principal axis factoring (PAF) and maximum likelihood (ML) are two extraction methods that are generally recommended. In general, ML or PAF give the best results, depending on whether data are normally-distributed or if the assumption of normality has been violated.

### Maximum likelihood (ML)

The maximum likelihood method has many advantages in that it allows researchers to compute of a wide range of indexes of the goodness of fit of the model, it allows researchers to test the statistical significance of factor loadings, calculate correlations among factors and compute confidence intervals for these parameters. ML is the best choice when data are normally distributed because “it allows for the computation of a wide range of indexes of the goodness of fit of the model [and] permits statistical significance testing of factor loadings and correlations among factors and the computation of confidence intervals”.

### Principal axis factoring (PAF)

Called “principal” axis factoring because the first factor accounts for as much common variance as possible, then the second factor next most variance, and so on. PAF is a descriptive procedure so it is best to use when the focus is just on your sample and you do not plan to generalize the results beyond your sample. A downside of PAF is that it provides a limited range of goodness-of-fit indexes compared to ML and does not allow for the computation of confidence intervals and significance tests.

## Selecting the appropriate number of factors

When selecting how many factors to include in a model, researchers must try to balance parsimony (a model with relatively few factors) and plausibility (that there are enough factors to adequately account for correlations among measured variables).

*Overfactoring* occurs when too many factors are included in a model and may lead researchers to put forward constructs with little theoretical value.

*Underfactoring* occurs when too few factors are included in a model. If not enough factors are included in a model, there is likely to be substantial error. Measured variables that load onto a factor not included in the model can falsely load on factors that are included, altering true factor loadings. This can result in rotated solutions in which two factors are combined into a single factor, obscuring the true factor structure.

There are a number of procedures designed to determine the optimal number of factors to retain in EFA. Broadly speaking, most of the existing procedures approach the determination of the appropriate number of factors (1) by inspecting patterns of eigenvalues of the covariance matrix, or (2) treating it as a model selection problem. Existing approaches include: Kaiser's (1960) eigenvalue-greater-than-one rule (or K1 rule), Cattell's (1966) scree plot, Revelle and Rocklin's (1979) very simple structure criterion, model comparison techniques, Raiche, Roipel, and Blais's (2006) acceleration factor and optimal coordinates, Velicer's (1976) minimum average partial, Horn's (1965) parallel analysis, and Ruscio and Roche's (2012) comparison data. Recent simulation studies assessing the robustness of such techniques suggest that the latter five can better assist practitioners to judiciously model data. These five modern techniques are now easily accessible through integrated use of IBM SPSS Statistics software (SPSS) and R (R Development Core Team, 2011). See Courtney (2013) for guidance on how to carry out these procedures for continuous, ordinal, and heterogenous (continuous and ordinal) data.

With the exception of Revelle and Rocklin's (1979) very simple structure criterion, model comparison techniques, and Velicer's (1976) minimum average partial, all other procedures rely on the analysis of eigenvalues. The *eigenvalue* of a factor represents the amount of variance of the variables accounted for by that factor. The lower the eigenvalue, the less that factor contributes to explaining the variance of the variables.

A short description of each of the nine procedures mentioned above is provided below.

### Kaiser's (1960) eigenvalue-greater-than-one rule (K1 or Kaiser criterion)

Kaiser's criterion, named after the American psychologist Henry Felix Kaiser, determines the number of factors by compute the eigenvalues for the correlation matrix and counting how many of these eigenvalues are greater than 1. This number is the number of factors to include in the model. A disadvantage of this procedure is that it is quite arbitrary (e.g., an eigenvalue of 1.01 is included whereas an eigenvalue of .99 is not). This procedure often leads to overfactoring, and sometimes underfactoring, and is widely regarded as suboptimal in comparison to more modern methods. A variation of the K1 criterion has been created to lessen the severity of the criterion's problems where a researcher calculates confidence intervals for each eigenvalue and retains only factors which have the entire confidence interval greater than 1.0.

### Cattell's (1966) scree plot

Compute the eigenvalues for the correlation matrix and plot the values from largest to smallest. Examine the graph to determine the last substantial drop in the magnitude of eigenvalues. The number of plotted points before the last drop is the number of factors to include in the model. This method has been criticized because of its subjective nature (i.e., there is no clear objective definition of what constitutes a substantial drop). As this procedure is subjective, Courtney (2013) does not recommend it.

### Revelle and Rocklin (1979) very simple structure

Revelle and Rocklin's (1979) VSS criterion operationalizes this tendency by assessing the extent to which the original correlation matrix is reproduced by a simplified pattern matrix, in which only the highest loading for each item is retained, all other loadings being set to zero. The VSS criterion for assessing the extent of replication can take values between 0 and 1, and is a measure of the goodness-of-fit of the factor solution. The VSS criterion is gathered from factor solutions that involve one factor (k = 1) to a user-specified theoretical maximum number of factors. Thereafter, the factor solution that provides the highest VSS criterion determines the optimal number of interpretable factors in the matrix. In an attempt to accommodate datasets where items covary with more than one factor (i.e., more factorially complex data), the criterion can also be carried out with simplified pattern matrices in which the highest two loadings are retained, with the rest set to zero (Max VSS complexity 2). Courtney also does not recommend VSS because of lack of robust simulation research concerning the performance of the VSS criterion.

### Model comparison techniques

Choose the best model from a series of models that differ in complexity. Researchers use goodness-of-fit measures to fit models beginning with a model with zero factors and gradually increase the number of factors. The goal is to ultimately choose a model that explains the data significantly better than simpler models (with fewer factors) and explains the data as well as more complex models (with more factors).

There are different methods that can be used to assess model fit:

- **Likelihood ratio statistic:** Used to test the null hypothesis that a model has perfect model fit. It should be applied to models with an increasing number of factors until the result is nonsignificant, indicating that the model is not rejected as good model fit of the population. This statistic should be used with a large sample size and normally distributed data. There are some drawbacks to the likelihood ratio test. First, when there is a large sample size, even small discrepancies between the model and the data result in model rejection. When there is a small sample size, even large discrepancies between the model and data may not be significant, which leads to underfactoring. Another disadvantage of the likelihood ratio test is that the null hypothesis of perfect fit is an unrealistic standard.
- **Root mean square error of approximation (RMSEA) fit index:** RMSEA is an estimate of the discrepancy between the model and the data per degree of freedom for the model. According to common rules of thumb, values less than .05 constitute good fit, values between 0.05 and 0.08 constitute acceptable fit, a values between 0.08 and 0.10 constitute marginal fit and values greater than 0.10 indicate poor fit . An advantage of the RMSEA fit index is that it provides confidence intervals which allow researchers to compare a series of models with varying numbers of factors.
- **Information Criteria:** Information criteria such as Akaike Information Criterion (AIC) or the Bayesian Information Criterion (BIC) can be used to trade-off model fit with model complexity and select an optimal number of factors.
- **Out-of-sample Prediction Errors (PE):** Using the connection between model-implied covariance matrices and standardized regression weights, the number of factors can be selected using out-of-sample prediction errors. In other words, the PE approach tests the ability of a factor model with *k* factors to predict scores on *p* items in held-out respondents, using the model-implied covariance structure to derive item-level regressions (e.g., predicting item *i* as a linear combination of all other items, with coefficients given by the inverse covariance matrix), selecting the value of *k* that best predicts out-of-sample item scores. In an extensive 2022 simulation study, Haslbeck and van Bork found that the PE method compares favorably with the best-performing existing methods (e.g., parallel analysis, exploratory graph analysis, AIC).

### Optimal Coordinate and Acceleration Factor

In an attempt to overcome the subjective weakness of Cattell's (1966) scree test, presented two families of non-graphical solutions. The first method, coined the optimal coordinate (OC), attempts to determine the location of the scree by measuring the gradients associated with eigenvalues and their preceding coordinates. The second method, coined the acceleration factor (AF), pertains to a numerical solution for determining the coordinate where the slope of the curve changes most abruptly. Both of these methods have out-performed the K1 method in simulation. In the Ruscio and Roche study (2012), the OC method was correct 74.03% of the time rivaling the PA technique (76.42%). The AF method was correct 45.91% of the time with a tendency toward under-estimation. Both the OC and AF methods, generated with the use of Pearson correlation coefficients, were reviewed in Ruscio and Roche's (2012) simulation study. Results suggested that both techniques performed quite well under ordinal response categories of two to seven (C = 2-7) and quasi-continuous (C = 10 or 20) data situations. Given the accuracy of these procedures under simulation, they are highly recommended for determining the number of factors to retain in EFA. It is one of Courtney's 5 recommended modern procedures.

### Velicer's Minimum Average Partial test (MAP)

Velicer's (1976) MAP test “involves a complete principal components analysis followed by the examination of a series of matrices of partial correlations” (p. 397). The squared correlation for Step “0” (see Figure 4) is the average squared off-diagonal correlation for the unpartialed correlation matrix. On Step 1, the first principal component and its associated items are partialed out. Thereafter, the average squared off-diagonal correlation for the subsequent correlation matrix is computed for Step 1. On Step 2, the first two principal components are partialed out and the resultant average squared off-diagonal correlation is again computed. The computations are carried out for k minus one steps (k representing the total number of variables in the matrix). Finally, the average squared correlations for all steps are lined up and the step number that resulted in the lowest average squared partial correlation determines the number of components or factors to retain (Velicer, 1976). By this method, components are maintained as long as the variance in the correlation matrix represents systematic variance, as opposed to residual or error variance. Although methodologically akin to principal components analysis, the MAP technique has been shown to perform quite well in determining the number of factors to retain in multiple simulation studies. However, in a very small minority of cases MAP may grossly overestimate the number of factors in a dataset for unknown reasons. This procedure is made available through SPSS's user interface. See Courtney (2013) for guidance. This is one of his five recommended modern procedures.

### Parallel analysis

To carry out the PA test, users compute the eigenvalues for the correlation matrix and plot the values from largest to smallest and then plot a set of random eigenvalues. The number of eigenvalues before the intersection points indicates how many factors to include in your model. This procedure can be somewhat arbitrary (i.e. a factor just meeting the cutoff will be included and one just below will not). Moreover, the method is very sensitive to sample size, with PA suggesting more factors in datasets with larger sample sizes. Despite its shortcomings, this procedure performs very well in simulation studies and is one of Courtney's recommended procedures. PA has been implemented in a number of commonly used statistics programs such as R and SPSS.

### Ruscio and Roche's comparison data

In 2012 Ruscio and Roche introduced the comparative data (CD) procedure in an attempt improve to upon the PA method. The authors state that "rather than generating random datasets, which only take into account sampling error, multiple datasets with known factorial structures are analyzed to determine which best reproduces the profile of eigenvalues for the actual data" (p. 258). The strength of the procedure is its ability to not only incorporate sampling error, but also the factorial structure and multivariate distribution of the items. Ruscio and Roche's (2012) simulation study determined that the CD procedure outperformed many other methods aimed at determining the correct number of factors to retain. In that study, the CD technique, making use of Pearson correlations accurately predicted the correct number of factors 87.14% of the time. However, the simulated study never involved more than five factors. Therefore, the applicability of the CD procedure to estimate factorial structures beyond five factors is yet to be tested. Courtney includes this procedure in his recommended list and gives guidelines showing how it can be easily carried out from within SPSS's user interface.

In 2023, Goretzko and Ruscio proposed the Comparison Data Forest as an extension of the CD approach.

### Convergence of multiple tests

A review of 60 journal articles by Henson and Roberts (2006) found that none used multiple modern techniques in an attempt to find convergence, such as PA and Velicer's (1976) minimum average partial (MAP) procedures. Ruscio and Roche (2012) simulation study demonstrated the empirical advantage of seeking convergence. When the CD and PA procedures agreed, the accuracy of the estimated number of factors was correct 92.2% of the time. Ruscio and Roche (2012) demonstrated that when further tests were in agreement, the accuracy of the estimation could be increased even further.

### Tailoring Courtney's recommended procedures for ordinal and continuous data

Recent simulation studies in the field of psychometrics suggest that the parallel analysis, minimum average partial, and comparative data techniques can be improved for different data situations. For example, in simulation studies, the performance of the minimum average partial test, when ordinal data is concerned, can be improved by utilizing polychoric correlations, as opposed to Pearson correlations. Courtney (2013) details how each of these three procedures can be optimized and carried out simultaneously from within the SPSS interface.

## Factor rotation

Factor rotation is a commonly employed step in EFA, used to aide interpretation of factor matrixes. For any solution with two or more factors there are an infinite number of orientations of the factors that will explain the data equally well. Because there is no unique solution, a researcher must select a single solution from the infinite possibilities. The goal of factor rotation is to rotate factors in multidimensional space to arrive at a solution with best simple structure, where simple structure refers to a factor matrix with *m* columns in which:

1. Each row (denoting the loadings of a single item on all *m* factors) contains at least one zero
2. Each column (denoting the loadings of all items on a single factor) contains at least *m* zeros
3. All pairs of columns (i.e., factors) have several rows (i.e., items) with a zero loading in one column but not the other (i.e., all pairs of factors have several items that can differentiate the factors)
4. If *m* ≥ 4, all pairs of columns should have several rows with zeros in both columns
5. All pairs of columns should have few rows with non-zero loadings in both columns (i.e., there should be few items with cross-loadings)

There are two main types of factor rotation: orthogonal and oblique rotation.

### Orthogonal rotation

Orthogonal rotations constrain factors to be perpendicular to each other and hence uncorrelated. An advantage of orthogonal rotation is its simplicity and conceptual clarity, although there are several disadvantages. In the social sciences, there is often a theoretical basis for expecting constructs to be correlated, therefore orthogonal rotations may not be very realistic because they do not allow this. Also, because orthogonal rotations require factors to be uncorrelated, they are less likely to produce solutions with simple structure.

Varimax rotation is an orthogonal rotation of the factor axes to maximize the variance of the squared loadings of a factor (column) on all the variables (rows) in a factor matrix, which has the effect of differentiating the original variables by extracted factor. Each factor will tend to have either large or small loadings of any particular variable. A varimax solution yields results which make it as easy as possible to identify each variable with a single factor. This is the most common orthogonal rotation option.

Quartimax rotation is an orthogonal rotation that maximizes the squared loadings for each variable rather than each factor. This minimizes the number of factors needed to explain each variable. This type of rotation often generates a general factor on which most variables are loaded to a high or medium degree.

Equimax rotation is a compromise between varimax and quartimax criteria.

### Oblique rotation

Oblique rotations permit correlations among factors. An advantage of oblique rotation is that it produces solutions with better simple structure when factors are expected to correlate, and it produces estimates of correlations among factors. These rotations may produce solutions similar to orthogonal rotation if the factors do not correlate with each other.

Several oblique rotation procedures are commonly used. Direct oblimin rotation is the standard oblique rotation method. Promax rotation is often seen in older literature because it is easier to calculate than oblimin. Other oblique methods include direct quartimin rotation and Harris-Kaiser orthoblique rotation.

### Unrotated solution

Common factor analysis software is capable of producing an unrotated solution. This refers to the result of a principal axis factoring with no further rotation. The so-called unrotated solution is in fact an orthogonal rotation that maximizes the variance of the first factors. The unrotated solution tends to give a general factor with loadings for most of the variables. This may be useful if many variables are correlated with each other, as revealed by one or a few dominating eigenvalues on a scree plot.

The usefulness of an unrotated solution was emphasized by a meta analysis of studies of cultural differences. This revealed that many published studies of cultural differences have given similar factor analysis results, but rotated differently. Factor rotation has obscured the similarity between the results of different studies and the existence of a strong general factor, while the unrotated solutions were much more similar.

## Factor interpretation

Factor loadings are numerical values that indicate the strength and direction of a factor on a measured variable. Factor loadings indicate how strongly the factor influences the measured variable. In order to label the factors in the model, researchers should examine the factor pattern to see which items load highly on which factors and then determine what those items have in common. Whatever the items have in common will indicate the meaning of the factor. Interpretation has long been noted as an important, but difficult, part of the analytic process.

However, while exploratory factor analysis is a powerful tool for uncovering underlying structures among variables, it is crucial to avoid reliance on it without adequate theorizing. Armstrong's critique highlights that EFA, when conducted without a theoretical framework, can lead to misleading interpretations. For instance, in a hypothetical case study involving the analysis of various physical properties of metals, the results of EFA failed to identify the true underlying factors, instead producing an "over-factored" model that obscured the simplicity of the relationships amongst the observed variables. Similarly, poorly designed survey items can lead to spurious factor structures.
