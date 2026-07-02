---
title: "Econometrics"
source: https://en.wikipedia.org/wiki/Econometrics
domain: econometrics
license: CC-BY-SA-4.0
tags: econometrics, instrumental variables, panel data, gauss-markov theorem
fetched: 2026-07-02
---

# Econometrics

**Econometrics** is an application of statistical methods to economic data in order to give empirical content to economic relationships. More precisely, it is "the quantitative analysis of actual economic phenomena based on the concurrent development of theory and observation, related by appropriate methods of inference." An introductory economics textbook describes econometrics as allowing economists "to sift through mountains of data to extract simple relationships." Jan Tinbergen is one of the two founding fathers of econometrics. The other, Ragnar Frisch, also coined the term in the sense in which it is used today.

A basic tool for econometrics is the multiple linear regression model. *Econometric theory* uses statistical theory and mathematical statistics to evaluate and develop econometric methods. Econometricians try to find estimators that have desirable statistical properties including unbiasedness, efficiency, and consistency. *Applied econometrics* uses theoretical econometrics and real-world data for assessing economic theories, developing econometric models, analysing economic history, and forecasting.

## History

The origins of econometrics can be traced to the development of the least squares method in the early nineteenth century. Initially applied in astronomy and geodesy to estimate celestial motions and other physical phenomena, least squares later became a foundational technique in regression analysis.

The development of statistical and econometric methods was influenced by earlier contributions to political arithmetic and quantitative social inquiry by figures such as Gregory King, Francis Ysidro Edgeworth, Vilfredo Pareto, and Sir William Petty. Early econometric research was exemplified by works such as Henry Ludwell Moore's *Synthetic Economics*.

As statistical applications expanded to classification problems, linear discriminant analysis (LDA) was introduced in 1936 to predict categorical outcomes. Logistic regression emerged during the 1940s as an alternative approach for modeling binary outcomes. In the early 1970s, the generalized linear model (GLM) framework was developed, unifying linear and logistic regression within a broader class of statistical models.

Throughout much of the twentieth century, statistical learning methods were predominantly linear because non-linear techniques were computationally demanding. Improvements in computing power during the 1980s facilitated the development and adoption of non-linear approaches, including classification and regression trees (CART), generalized additive models (GAMs), and artificial neural networks. During the 1990s, support vector machines (SVMs) emerged as another important class of predictive models.

## Basic models: linear regression

A basic tool for econometrics is the multiple linear regression model. In modern econometrics, other statistical tools are frequently used, but linear regression is still the most frequently used starting point for an analysis. Estimating a linear regression on two variables can be visualized as fitting a line through data points representing paired values of the independent and dependent variables.

One of the earliest uses of linear regression was in 1889 by British statistician Udny Yule. Yule was seeking to causally identify a relationship between public assistance and the number of impoverished people in England. Using two time periods from the 1871 and 1881 census data at the county level, he estimated the effect of receiving social assistance on the rate of poverty. While it would likely not meet the threshold today, given concerns of two-way causality and bias in the error term, his regression specification was the following:

${\text{Poverty}}_{c}=\alpha _{c}+\delta _{c}\cdot {\text{Assistance}}_{c}+\beta _{1}{\text{Old}}_{c}+\beta _{2}{\text{Population}}_{c}+\epsilon _{c}$

Another example, one that is rarely used today, can be found in macroeconomics. Consider Okun's law, which relates GDP growth to the unemployment rate. This relationship is represented in a linear regression where the change in unemployment rate ( $\Delta \ {\text{Unemployment}}$ ) is a function of an intercept ( $\beta _{0}$ ), a given value of GDP growth multiplied by a slope coefficient $\beta _{1}$ and an error term, $\varepsilon$ :

$\Delta \ {\text{Unemployment}}=\beta _{0}+\beta _{1}{\text{Growth}}+\varepsilon .$

The unknown parameters $\beta _{0}$ and $\beta _{1}$ can be estimated. Here $\beta _{0}$ is estimated to be 0.83 and $\beta _{1}$ is estimated to be -1.77. This means that if GDP growth increased by 1 percentage point, the unemployment rate would be predicted to drop by 1.77 * 1 points, other things held constant. The model could then be tested for statistical significance as to whether an increase in GDP growth is associated with a decrease in unemployment, as hypothesized. If the estimate of $\beta _{1}$ were not significantly different from 0, the test would fail to find evidence that changes in the growth rate and unemployment rate were related. The variance in a prediction of the dependent variable (unemployment) as a function of the independent variable (GDP growth) is given in polynomial least squares.

## Theory

Econometric theory uses statistical theory and mathematical statistics to evaluate and develop econometric methods. Econometricians try to find estimators that have desirable statistical properties including unbiasedness, efficiency, and consistency. An estimator is unbiased if its expected value is the true value of the parameter; it is consistent if it converges to the true value as the sample size gets larger, and it is efficient if the estimator has a lower standard error than other unbiased estimators for a given sample size. Ordinary least squares (OLS) is often used for estimation since it provides the BLUE or "best linear unbiased estimator" (where "best" means most efficient, unbiased estimator) given the Gauss-Markov assumptions. When these assumptions are violated, or other statistical properties are desired, other estimation techniques such as maximum likelihood estimation, generalized method of moments, or generalized least squares are used. Estimators that incorporate prior beliefs are advocated by those who favour Bayesian statistics over traditional, classical or "frequentist" approaches.

## Methods

*Applied econometrics* uses theoretical econometrics and real-world data for assessing economic theories, developing econometric models, analysing economic history, and forecasting.

Econometrics uses standard statistical models to study economic questions, but most often these are based on observational data, rather than data from controlled experiments. In this, the design of observational studies in econometrics is similar to the design of studies in other observational disciplines, such as astronomy, epidemiology, sociology, and political science. The study protocol guides analysis of data from an observational study, although exploratory data analysis may be useful for generating new hypotheses. Economics often analyses systems of equations and inequalities, such as supply and demand hypothesized to be in equilibrium. Consequently, the field of econometrics has developed methods for identification and estimation of simultaneous equations models. These methods are analogous to those used in other areas of science, such as system identification in systems analysis and control theory. Such methods may allow researchers to estimate models and investigate their empirical consequences, without directly manipulating the system.

In the absence of evidence from controlled experiments, econometricians often seek illuminating natural experiments or apply quasi-experimental methods to draw credible causal inference. The methods include regression discontinuity design, instrumental variables, and difference-in-differences.

## Example

A simple example of a relationship in econometrics from the field of labour economics is:

$\ln({\text{wage}})=\beta _{0}+\beta _{1}({\text{years of education}})+\varepsilon .$

This example assumes that the natural logarithm of a person's wage is a linear function of the number of years of education that person has acquired. The parameter $\beta _{1}$ measures the increase in the natural log of the wage attributable to one more year of education. The term $\varepsilon$ is a random variable representing all other factors that may have a direct influence on wage. The econometric goal is to estimate the parameters, $\beta _{0}{\mbox{ and }}\beta _{1}$ under specific assumptions about the random variable $\varepsilon$ . For example, if $\varepsilon$ is uncorrelated with years of education, then the equation can be estimated with ordinary least squares.

If the researcher could randomly assign people to different levels of education, the resulting data set would allow estimation of the effect of changes in years of education on wages. In reality, those experiments cannot be conducted. Instead, the econometrician observes the years of education and the wages paid to people who differ along many dimensions. Given this kind of data, the estimated coefficient on years of education in the equation above reflects both the effect of education on wages and the effect of other variables on wages, if those other variables were correlated with education. For example, people born in certain places may have higher wages and higher levels of education. Unless the econometrician controls for place of birth in the above equation, the effect of birthplace on wages may be falsely attributed to the effect of education on wages.

The most obvious way to control for birthplace is to include a measure of its effect in the equation above. Exclusion of birthplace, together with the assumption that $\epsilon$ is uncorrelated with education, produces a misspecified model. Another technique is to include in the equation additional set of measured covariates which are not instrumental variables, yet render $\beta _{1}$ identifiable. An overview of econometric methods used to study this problem were provided by Card (1999).

## Journals

The main journals that publish work in econometrics are:

- *Econometrica*, which is published by Econometric Society.
- *The Review of Economics and Statistics*, which is over 100 years old.
- *The Econometrics Journal*, which was established by the Royal Economic Society.
- The *Journal of Econometrics*, which also publishes the supplement *Annals of Econometrics.*
- *Econometric Theory*, which is a theoretical journal.
- The *Journal of Applied Econometrics*, which applies econometrics to a wide various problems.
- *Econometric Reviews*, which includes reviews on econometric books and software as well.
- The *Journal of Business & Economic Statistics,* which is published by the American Statistical Association.

## Limitations and criticisms

Integrating statistics into economic theory to make causal claims leads to disagreements within the discipline, prompting criticism of econometrics. Most of these criticisms have been resolved as a result of the credibility revolution and the improved rigor of the potential outcomes framework, which is used today by applied economists, microeconomists, and econometricians to generate causal inferences. While econometricians began developing methods in the mid-1960s to improve statistical measures, the 2009 publication of *Mostly Harmless Econometrics* by economists Joshua D. Angrist and Jörn-Steffen Pischke has summarized the advances in econometric modeling. Structural causal modeling, which attempts to formalize the limitations of quasi-experimental methods from a causal perspective and enables experimenters to quantify the risks of quasi-experimental research precisely, is the primary academic response to this critique.

Like other forms of statistical analysis, badly specified econometric models may show a spurious relationship where two variables are correlated but causally unrelated. In a study of the use of econometrics in major economics journals, McCloskey concluded that some economists report *p*-values (following the Fisherian tradition of tests of significance of point null-hypotheses) and neglect concerns of type II errors; some economists fail to report estimates of the size of effects (apart from statistical significance) and to discuss their economic importance. She also argues that some economists fail to use economic reasoning in model selection, especially when deciding which variables to include in a regression.

In some cases, economic variables cannot be experimentally manipulated as treatments randomly assigned to subjects. In such cases, economists rely on observational studies, often using data sets with many strongly associated covariates, resulting in enormous numbers of models with similar explanatory ability but different covariates and regression estimates. Regarding the plurality of models compatible with observational data-sets, Edward Leamer urged that "professionals ... properly withhold belief until an inference can be shown to be adequately insensitive to the choice of assumptions".

### Difficulties in model specification

Like other forms of statistical analysis, badly specified econometric models may show a spurious correlation where two variables are correlated but causally unrelated. Economist Ronald Coase is widely reported to have said "if you torture the data long enough it will confess". Deirdre McCloskey argues that in published econometric work, economists often fail to use economic reasoning for including or excluding variables, equivocate statistical significance with substantial significance, and fail to report the *power* of their findings.

Economic variables are observed in reality, and therefore are not readily isolated for experimental testing. Edward Leamer argued there was no essential difference between econometric analysis and randomized trials or controlled trials, provided the use of statistical techniques reduces the specification bias, the effects of collinearity between the variables, to the same order as the uncertainty due to the sample size. Today, this critique is unbinding, as advances in identification are stronger. Identification today may report the average treatment effect (ATE), the average treatment effect *on the treated* (ATT), or the *local* average treatment effect (LATE). Specification bias, or *selection bias* can be easily removed, through advances in sampling techniques and the ability to sample much larger populations through improved communications, data storage, and randomization techniques. Secondly, collinearity can be easily controlled for using instrumental variables. By reporting either ATT or LATE, we can control for or eliminate heterogeneous error, reporting only the effects within the defined group.

Economists, when using data, may have many explanatory variables they want to use that are highly collinear, such that researcher bias may be important in variable selection. Leamer argues that economists can mitigate this by running statistical tests with different specified models and discarding any inferences that prove to be "fragile", concluding that "professionals ... properly withhold belief until an inference can be shown to be adequately insensitive to the choice of assumptions." Today, this is known as p-hacking, and is not a failure of econometric methodology, but is instead a potential failure of a researcher who may be seeking to prove their own hypothesis. P-hacking is not accepted in economics, and the requirement to disclose original data and the code to perform statistical analysis. However Sala-I-Martin argued, it's possible to specify two models suggesting contrary relation between two variables. The phenomenon was labeled *emerging recalcitrant result* phenomenon by Robert Goldfarb. This is known as two-way causality, and should be discussed with respect to the underlying theory that the mechanism is attempting to capture.

Kennedy (1998, p 1-2) reports econometricians as being accused of *using sledgehammers to crack open peanuts*. That is they use a wide range of complex statistical techniques *while turning a blind eye to data deficiencies and the many questionable assumptions required for the application of these techniques*. Kennedy quotes Stefan Valavanis's 1959 Econometrics textbook's critique of practice:

> Econometric theory is like an exquisitely balanced French recipe, spelling out precisely with how many turns to mix the sauce, how many carats of spice to add, and for how many milliseconds to bake the mixture at exactly 474 degrees of temperature. But when the statistical cook turns to raw materials, he finds that hearts of cactus fruit are unavailable, so he substitutes chunks of cantaloupe; where the recipe calls for vermicelli he used shredded wheat; and he substitutes green garment die for curry, ping-pong balls for turtles eggs, and for Chalifougnac vintage 1883, a can of turpentine. (1959, p.83)

### Macroeconomic critiques

Looking primarily at macroeconomics, Lawrence Summers has criticized econometric formalism, arguing that "the empirical facts of which we are most confident and which provide the most secure basis for theory are those that require the least sophisticated statistical analysis to perceive." **Summers is not critiquing the methodology itself** but instead its usefulness in developing macroeconomic theory.

He looks at two well-cited macroeconometric studies (Hansen & Singleton (1982, 1983), and Bernanke (1986)), and argues that while both make brilliant use of econometric methods, neither paper speaks to formal theoretical proof. Noting that in the natural sciences, "investigators rush to check out the validity of claims made by rival laboratories and then build on them," Summers points out that this rarely happen in economics, which to him is a result of the fact that "the results [of econometric studies] are rarely an important input to theory creation or the evolution of professional opinion more generally." To Summers:

> Successful empirical research has been characterized by attempts to gauge the strength of associations rather than to estimate structural parameters, verbal characterizations of how causal relations might operate rather than explicit mathematical models, and the skillful use of carefully chosen natural experiments rather than sophisticated statistical technique to achieve identification.

#### Lucas critique

Robert Lucas criticised the use of overly simplistic econometric models of the macroeconomy to predict the implications of economic policy, arguing that the structural relationships observed in historical models break down when decision-makers adjust their preferences in response to policy changes. Lucas argued that policy conclusions drawn from contemporary large-scale macroeconometric models were invalid, as economic actors would revise their expectations about the future and adjust their behaviour accordingly. A good macroeconometric model should incorporate microfoundations to model the effects of policy change, with equations representing economic representative agents responding to economic changes based on rational expectations of the future; implying their pattern of behaviour might be quite different if economic policy changed.

### Austrian School critique

The current-day Austrian School of Economics typically rejects much of econometric modeling. The historical data used to make econometric models, they claim, represent behavior under circumstances idiosyncratic to the past; thus, econometric models show correlational rather than causal relationships. Econometricians have addressed this criticism by adopting quasi-experimental methodologies. Austrian school economists remain skeptical of these corrected models, maintaining their belief that statistical methods are unsuited to the social sciences.

The Austrian School holds that the counterfactual must be known for a causal relationship to be established. The counterfactual changes could then be extracted from the observed changes, leaving only the changes attributable to the variable. Meeting this critique is very challenging since "there is no dependable method for ascertaining the uniquely correct counterfactual" for historical data. For non-historical data, the Austrian critique is met with randomized controlled trials. Randomized controlled trials must be purposefully prepared, which historical data is not. The use of randomized controlled trials is becoming more common in social science research. In the United States, for example, the Education Sciences Reform Act of 2002 made funding for education research contingent on scientific validity defined in part as "experimental designs using random assignment, when feasible." In answering questions of causation, parametric statistics only address the Austrian critique in randomized controlled trials.

If the data is not from a randomized controlled trial, econometricians meet the Austrian critique with quasi-experimental methodologies, including identifying and exploiting natural experiments. These methodologies attempt to extract the counterfactual post hoc, thereby justifying the use of parametric statistical tools. Since parametric statistics depends on any observation following a Gaussian distribution, which is only guaranteed by the central limit theorem in a randomization methodology, the use of tools such as the confidence interval will be outside of their specification: the amount of selection bias will always be unknown.
