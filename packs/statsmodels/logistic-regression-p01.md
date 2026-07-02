---
title: "Logistic regression (part 1/3)"
source: https://en.wikipedia.org/wiki/Logistic_regression
domain: statsmodels
license: BSD-3-Clause
tags: statsmodels library, regression analysis, generalized linear model, analysis of variance
fetched: 2026-07-02
part: 1/3
---

# Logistic regression

In statistics, a **logistic model** (or **logit model**) is a statistical model that models the log-odds of an event as a linear combination of one or more independent variables. In regression analysis, **logistic regression** (or **logit regression**) estimates the parameters of a logistic model (the coefficients in the linear or non linear combinations). In binary logistic regression there is a single binary dependent variable, coded by an indicator variable, where the two values are labeled "0" and "1", while the independent variables can each be a binary variable (two classes, coded by an indicator variable) or a continuous variable (any real value). The corresponding probability of the value labeled "1" can vary between 0 (certainly the value "0") and 1 (certainly the value "1"), hence the labeling; the function that converts log-odds to probability is the logistic function, hence the name. The unit of measurement for the log-odds scale is called a *logit*, from ***log**istic un**it***, hence the alternative names. See § Background and § Definition for formal mathematics, and § Example for a worked example.

Binary variables are widely used in statistics to model the probability of a certain class or event taking place, such as the probability of a team winning, of a patient being healthy, etc. (see § Applications), and the logistic model has been the most commonly used model for binary regression since about 1970. Binary variables can be generalized to categorical variables when there are more than two possible values (e.g. whether an image is of a cat, dog, lion, etc.), and the binary logistic regression generalized to multinomial logistic regression. If the multiple categories are ordered, one can use the ordinal logistic regression (for example the proportional odds ordinal logistic model). See § Extensions for further extensions. The logistic regression model itself simply models probability of output in terms of input and does not perform statistical classification (it is not a classifier), though it can be used to make a classifier, for instance by choosing a cutoff value and classifying inputs with probability greater than the cutoff as one class, below the cutoff as the other; this is a common way to make a binary classifier.

Analogous linear models for binary variables with a different sigmoid function instead of the logistic function (to convert the linear combination to a probability) can also be used, most notably the probit model; see § Alternatives. The defining characteristic of the logistic model is that increasing one of the independent variables multiplicatively scales the odds of the given outcome at a *constant* rate, with each independent variable having its own parameter; for a binary dependent variable this generalizes the odds ratio. More abstractly, the logistic function is the natural parameter for the Bernoulli distribution, and in this sense is the "simplest" way to convert a real number to a probability.

The parameters of a logistic regression are most commonly estimated by maximum-likelihood estimation (MLE). This does not have a closed-form expression, unlike linear least squares; see § Model fitting. Logistic regression by MLE plays a similarly basic role for binary or categorical responses as linear regression by ordinary least squares (OLS) plays for scalar responses: it is a simple, well-analyzed baseline model; see § Comparison with linear regression for discussion. The logistic regression as a general statistical model was originally developed and popularized primarily by Joseph Berkson, beginning in Berkson (1944), where he coined "logit"; see § History.


## Applications

### General

Logistic regression is used in various fields, including machine learning, most medical fields, and social sciences. For example, the Trauma and Injury Severity Score (TRISS), which is widely used to predict mortality in injured patients, was originally developed by Boyd *et al.* using logistic regression. Many other medical scales used to assess severity of a patient have been developed using logistic regression. Logistic regression may be used to predict the risk of developing a given disease (e.g. diabetes; coronary heart disease), based on observed characteristics of the patient (age, sex, body mass index, results of various blood tests, etc.). Another example might be to predict whether a Nepalese voter will vote Nepali Congress or Communist Party of Nepal or for any other party, based on age, income, sex, race, state of residence, votes in previous elections, etc. The technique can also be used in engineering, especially for predicting the probability of failure of a given process, system or product. It is also used in marketing applications such as prediction of a customer's propensity to purchase a product or halt a subscription, etc. In economics, it can be used to predict the likelihood of a person ending up in the labor force, and a business application would be to predict the likelihood of a homeowner defaulting on a mortgage. Conditional random fields, an extension of logistic regression to sequential data, are used in natural language processing. Disaster planners and engineers rely on these models to predict decisions taken by householders or building occupants in small-scale and large-scales evacuations, such as building fires, wildfires, hurricanes among others. These models help in the development of reliable disaster managing plans and safer design for the built environment.

### Supervised machine learning

Logistic regression is a supervised machine learning algorithm widely used for binary classification tasks, such as identifying whether an email is spam or not and diagnosing diseases by assessing the presence or absence of specific conditions based on patient test results. This approach utilizes the logistic (or sigmoid) function to transform a linear combination of input features into a probability value ranging between 0 and 1. This probability indicates the likelihood that a given input corresponds to one of two predefined categories. The essential mechanism of logistic regression is grounded in the logistic function's ability to model the probability of binary outcomes accurately. With its distinctive S-shaped curve, the logistic function effectively maps any real-valued number to a value within the 0 to 1 interval. This feature renders it particularly suitable for binary classification tasks, such as sorting emails into "spam" or "not spam". By calculating the probability that the dependent variable will be categorized into a specific group, logistic regression provides a probabilistic framework that supports informed decision-making.


## Example

### Problem

As a simple example, we can use a logistic regression with one explanatory variable and two categories to answer the following question:

> A group of 20 students spends between 0 and 6 hours studying for an exam. How does the number of hours spent studying affect the probability of the student passing the exam?

The reason for using logistic regression for this problem is that the values of the dependent variable, pass and fail, while represented by "1" and "0", are not cardinal numbers. If the problem was changed so that pass/fail was replaced with the grade 0–100 (cardinal numbers), then simple regression analysis could be used.

The table shows the number of hours each student spent studying, and whether they passed (1) or failed (0).

Hours (

x

k

)

0.50

0.75

1.00

1.25

1.50

1.75

1.75

2.00

2.25

2.50

2.75

3.00

3.25

3.50

4.00

4.25

4.50

4.75

5.00

5.50

Pass (

y

k

)

0

0

0

0

0

0

1

0

1

0

1

0

1

0

1

1

1

1

1

1

We wish to fit a logistic function to the data consisting of the hours studied (*xk*) and the outcome of the test (*yk* =1 for pass, 0 for fail). The data points are indexed by the subscript *k* which runs from $k=1$ to $k=K=20$ . The *x* variable is called the "explanatory variable", and the *y* variable is called the "categorical variable" consisting of two categories: "pass" or "fail" corresponding to the categorical values 1 and 0 respectively.

### Model

The logistic function is of the form:

$p(x)={\frac {1}{1+e^{-(x-\mu )/s}}}$

where *μ* is a location parameter (the midpoint of the curve, where $p(\mu )=1/2$ ) and *s* is a scale parameter. This expression may be rewritten as:

$p(x)={\frac {1}{1+e^{-(\beta _{0}+\beta _{1}x)}}}$

where $\beta _{0}=-\mu /s$ and is known as the intercept (it is the *vertical* intercept or *y*-intercept of the line $y=\beta _{0}+\beta _{1}x$ ), and $\beta _{1}=1/s$ (inverse scale parameter or rate parameter): these are the *y*-intercept and slope of the log-odds as a function of *x*. Conversely, $\mu =-\beta _{0}/\beta _{1}$ and $s=1/\beta _{1}$ .

Note that this model is actually an oversimplification, as it implies that every student will pass if they study indefinitely (limit = 1).

### Fit

The usual measure of goodness of fit for a logistic regression uses logistic loss (or log loss), the negative log-likelihood. For a given *xk* and *yk*, write $p_{k}=p(x_{k})$ . The ⁠ $p_{k}$ ⁠ are the probabilities that the corresponding ⁠ $y_{k}$ ⁠ will equal one, and ⁠ $1-p_{k}$ ⁠ are the probabilities that they will be zero (see Bernoulli distribution). We wish to find the values of ⁠ $\beta _{0}$ ⁠ and ⁠ $\beta _{1}$ ⁠ which give the "best fit" to the data. For comparison of a "best fit" to the data, see the case of linear regression. There, the sum of the squared deviations of the fit from the data points (*yk*), the squared error loss, is taken as a measure of the goodness of fit, and the best fit is obtained when this loss is *minimized*.

The log loss for the *k*-th point ⁠ $\ell _{k}$ ⁠ is:

$\ell _{k}={\begin{cases}-\ln p_{k}&{\text{ if }}y_{k}=1,\\-\ln(1-p_{k})&{\text{ if }}y_{k}=0.\end{cases}}$

The log loss can be interpreted as the "surprisal" of the actual outcome ⁠ $y_{k}$ ⁠ relative to the prediction ⁠ $p_{k}$ ⁠, and is a measure of information content. Log loss is always greater than or equal to 0, equals 0 only in case of a perfect prediction (i.e., when $p_{k}=1$ and $y_{k}=1$ , or $p_{k}=0$ and $y_{k}=0$ ), and approaches infinity as the prediction gets worse (i.e., when $y_{k}=1$ and $p_{k}\to 0$ or $y_{k}=0$ and $p_{k}\to 1$ ), meaning the actual outcome is "more surprising". Since the value of the logistic function is always strictly between zero and one, the log loss is always greater than zero and less than infinity. Unlike in a linear regression, where the model can have zero loss at a point by passing through a data point (and zero loss overall if all points are on a line), in a logistic regression it is not possible to have zero loss at any points, since ⁠ $y_{k}$ ⁠ is either 0 or 1, but ⁠ $0<p_{k}<1$ ⁠.

These can be combined into a single expression:

$\ell _{k}=-y_{k}\ln p_{k}-(1-y_{k})\ln(1-p_{k}).$

This expression is more formally known as the cross-entropy of the predicted distribution ${\big (}p_{k},(1-p_{k}){\big )}$ from the actual distribution ${\big (}y_{k},(1-y_{k}){\big )}$ , as probability distributions on the two-element space of (pass, fail).

The sum of these, the total loss, is the overall negative log-likelihood ⁠ $-\ell$ ⁠, and the best fit is obtained for those choices of ⁠ $\beta _{0}$ ⁠ and ⁠ $\beta _{1}$ ⁠ for which ⁠ $-\ell$ ⁠ is *minimized*.

Alternatively, instead of *minimizing* the loss, one can *maximize* its inverse, the (positive) log-likelihood:

$\ell =\sum _{k:y_{k}=1}\ln(p_{k})+\sum _{k:y_{k}=0}\ln(1-p_{k})=\sum _{k=1}^{K}\left(\,y_{k}\ln(p_{k})+(1-y_{k})\ln(1-p_{k})\right)$

or equivalently maximize the likelihood function itself, which is the probability that the given data set is produced by a particular logistic function:

$L=\prod _{k:y_{k}=1}p_{k}\,\prod _{k:y_{k}=0}(1-p_{k})$

This method is known as maximum likelihood estimation.

### Parameter estimation

Since *ℓ* is nonlinear in ⁠ $\beta _{0}$ ⁠ and ⁠ $\beta _{1}$ ⁠, determining their optimum values will require numerical methods. One method of maximizing *ℓ* is to require the derivatives of *ℓ* with respect to ⁠ $\beta _{0}$ ⁠ and ⁠ $\beta _{1}$ ⁠ to be zero:

$0={\frac {\partial \ell }{\partial \beta _{0}}}=\sum _{k=1}^{K}(y_{k}-p_{k})$

$0={\frac {\partial \ell }{\partial \beta _{1}}}=\sum _{k=1}^{K}(y_{k}-p_{k})x_{k}$

and the maximization procedure can be accomplished by solving the above two equations for ⁠ $\beta _{0}$ ⁠ and ⁠ $\beta _{1}$ ⁠, which, again, will generally require the use of numerical methods.

The values of ⁠ $\beta _{0}$ ⁠ and ⁠ $\beta _{1}$ ⁠ which maximize *ℓ* and *L* using the above data are found to be:

$\beta _{0}\approx -4.1$

$\beta _{1}\approx 1.5$

which yields a value for *μ* and *s* of:

$\mu =-\beta _{0}/\beta _{1}\approx 2.7$

$s=1/\beta _{1}\approx 0.67$

### Predictions

The ⁠ $\beta _{0}$ ⁠ and ⁠ $\beta _{1}$ ⁠ coefficients may be entered into the logistic regression equation to estimate the probability of passing the exam.

For example, for a student who studies 2 hours, entering the value $x=2$ into the equation gives the estimated probability of passing the exam of 0.25:

$t=\beta _{0}+2\beta _{1}\approx -4.1+2\cdot 1.5=-1.1$

$p={\frac {1}{1+e^{-t}}}\approx 0.25={\text{Probability of passing exam}}$

Similarly, for a student who studies 4 hours, the estimated probability of passing the exam is 0.87:

$t=\beta _{0}+4\beta _{1}\approx -4.1+4\cdot 1.5=1.9$

$p={\frac {1}{1+e^{-t}}}\approx 0.87={\text{Probability of passing exam}}$

This table shows the estimated probability of passing the exam for several values of hours studying.

| Hours of study (*x*) | Passing exam |   |   |
|---|---|---|---|
| Log-odds (*t*) | Odds (*et*) | Probability (*p*) |   |
| 1 | −2.57 | 0.076 ≈ 1:13.1 | 0.07 |
| 2 | −1.07 | 0.34 ≈ 1:2.91 | 0.26 |
| ⁠ $\mu \approx 2.7$ ⁠ | 0 | 1 | ⁠1/2⁠ = 0.50 |
| 3 | 0.44 | 1.55 | 0.61 |
| 4 | 1.94 | 6.96 | 0.87 |
| 5 | 3.45 | 31.4 | 0.97 |

### Model evaluation

The logistic regression analysis gives the following output.

|   | Coefficient | Std. Error | *z*-value | *p*-value (Wald) |
|---|---|---|---|---|
| Intercept (*β*0) | −4.1 | 1.8 | −2.3 | 0.021 |
| Hours (*β*1) | 1.5 | 0.9 | 1.7 | 0.017 |

By the Wald test, the output indicates that hours studying is significantly associated with the probability of passing the exam ( $p=0.017$ ). Rather than the Wald method, the recommended method to calculate the *p*-value for logistic regression is the likelihood-ratio test (LRT), which for these data give $p\approx 0.00064$ (see § Deviance and likelihood ratio tests below).

### Generalizations

This simple model is an example of binary logistic regression, and has one explanatory variable and a binary categorical variable which can assume one of two categorical values. Multinomial logistic regression is the generalization of binary logistic regression to include any number of explanatory variables and any number of categories.


## Background

### Definition of the logistic function

An explanation of logistic regression can begin with an explanation of the standard logistic function. The logistic function is a sigmoid function, which takes any real input t , and outputs a value between zero and one. For the logit, this is interpreted as taking input log-odds and having output probability. The *standard* logistic function $\sigma :\mathbb {R} \rightarrow (0,1)$ is defined as follows:

$\sigma (t)={\frac {e^{t}}{e^{t}+1}}={\frac {1}{1+e^{-t}}}$

A graph of the logistic function on the *t*-interval (−6,6) is shown in Figure 1.

Let us assume that t is a linear function of a single explanatory variable x (the case where t is a *linear combination* of multiple explanatory variables is treated similarly). We can then express t as follows:

$t=\beta _{0}+\beta _{1}x$

And the general logistic function $p:\mathbb {R} \rightarrow (0,1)$ can now be written as:

$p(x)=\sigma (t)={\frac {1}{1+e^{-(\beta _{0}+\beta _{1}x)}}}$

In the logistic model, $p(x)$ is interpreted as the probability of the dependent variable Y equaling a success/case rather than a failure/non-case. It is clear that the response variables $Y_{i}$ are not identically distributed: $P(Y_{i}=1\mid X)$ differs from one data point $X_{i}$ to another, though they are independent given design matrix X and shared parameters $\beta$ .

### Definition of the inverse of the logistic function

We can now define the logit (log odds) function as the inverse $g=\sigma ^{-1}$ of the standard logistic function. It is easy to see that it satisfies:

$g(p(x))=\sigma ^{-1}(p(x))=\operatorname {logit} p(x)=\ln \left({\frac {p(x)}{1-p(x)}}\right)=\beta _{0}+\beta _{1}x,$

and equivalently, after exponentiating both sides we have the odds:

${\frac {p(x)}{1-p(x)}}=e^{\beta _{0}+\beta _{1}x}.$

### Interpretation of these terms

In the above equations, the terms are as follows:

- g is the logit function. The equation for $g(p(x))$ illustrates that the logit (i.e., log-odds or natural logarithm of the odds) is equivalent to the linear regression expression.
- $\ln$ denotes the natural logarithm.
- $p(x)$ is the probability that the dependent variable equals a case, given some linear combination of the predictors. The formula for $p(x)$ illustrates that the probability of the dependent variable equaling a case is equal to the value of the logistic function of the linear regression expression. This is important in that it shows that the value of the linear regression expression can vary from negative to positive infinity and yet, after transformation, the resulting expression for the probability $p(x)$ ranges between 0 and 1.
- $\beta _{0}$ is the intercept from the linear regression equation (the value of the criterion when the predictor is equal to zero).
- $\beta _{1}x$ is the regression coefficient multiplied by some value of the predictor.
- base e denotes the exponential function.

### Definition of the odds

The odds of the dependent variable equaling a case (given some linear combination x of the predictors) is equivalent to the exponential function of the linear regression expression. This illustrates how the logit serves as a link function between the probability and the linear regression expression. Given that the logit ranges between negative and positive infinity, it provides an adequate criterion upon which to conduct linear regression and the logit is easily converted back into the odds.

So we define odds of the dependent variable equaling a case (given some linear combination x of the predictors) as follows:

${\text{odds}}=e^{\beta _{0}+\beta _{1}x}.$

### The odds ratio

For a continuous independent variable the odds ratio can be defined as:

$\mathrm {OR} ={\frac {\operatorname {odds} (x+1)}{\operatorname {odds} (x)}}={\frac {\left({\frac {p(x+1)}{1-p(x+1)}}\right)}{\left({\frac {p(x)}{1-p(x)}}\right)}}={\frac {e^{\beta _{0}+\beta _{1}(x+1)}}{e^{\beta _{0}+\beta _{1}x}}}=e^{\beta _{1}}$

This exponential relationship provides an interpretation for $\beta _{1}$ : The odds multiply by $e^{\beta _{1}}$ for every 1-unit increase in x.

For a binary independent variable the odds ratio is defined as ${\frac {ad}{bc}}$ where *a*, *b*, *c* and *d* are cells in a 2×2 contingency table.

### Multiple explanatory variables

If there are multiple explanatory variables, the above expression $\beta _{0}+\beta _{1}x$ can be revised to $\beta _{0}+\beta _{1}x_{1}+\beta _{2}x_{2}+\cdots +\beta _{m}x_{m}=\beta _{0}+\sum _{i=1}^{m}\beta _{i}x_{i}$ . Then when this is used in the equation relating the log odds of a success to the values of the predictors, the linear regression will be a multiple regression with *m* explanators; the parameters $\beta _{i}$ for all $i=0,1,2,\dots ,m$ are all estimated.

Again, the more traditional equations are:

$\log {\frac {p}{1-p}}=\beta _{0}+\beta _{1}x_{1}+\beta _{2}x_{2}+\cdots +\beta _{m}x_{m}$

and

$p={\frac {1}{1+b^{-(\beta _{0}+\beta _{1}x_{1}+\beta _{2}x_{2}+\cdots +\beta _{m}x_{m})}}}$

where usually $b=e$ .


## Definition

A dataset contains *N* points. Each point *i* consists of a set of *m* input variables *x*1,*i* ... *x**m,i* (also called independent variables, explanatory variables, predictor variables, features, or attributes), and a binary outcome variable *Y**i* (also known as a dependent variable, response variable, output variable, or class), i.e. it can assume only the two possible values 0 (often meaning "no" or "failure") or 1 (often meaning "yes" or "success"). The goal of logistic regression is to use the dataset to create a predictive model of the outcome variable.

As in linear regression, the outcome variables *Y**i* are assumed to depend on the explanatory variables *x*1,*i* ... *x**m,i*.

**Explanatory variables**

The explanatory variables may be of any type: real-valued, binary, categorical, etc. The main distinction is between continuous variables and discrete variables.

(Discrete variables referring to more than two possible choices are typically coded using dummy variables (or indicator variables), that is, separate explanatory variables taking the value 0 or 1 are created for each possible value of the discrete variable, with a 1 meaning "variable does have the given value" and a 0 meaning "variable does not have that value".)

**Outcome variables**

Formally, the outcomes *Y**i* are described as being Bernoulli-distributed data, where each outcome is determined by an unobserved probability *p**i* that is specific to the outcome at hand, but related to the explanatory variables. This can be expressed in any of the following equivalent forms:

${\begin{aligned}Y_{i}\mid x_{1,i},\ldots ,x_{m,i}\ &\sim \operatorname {Bernoulli} (p_{i})\\[5pt]\operatorname {\mathbb {E} } [Y_{i}\mid x_{1,i},\ldots ,x_{m,i}]&=p_{i}\\[5pt]\Pr(Y_{i}=y\mid x_{1,i},\ldots ,x_{m,i})&={\begin{cases}p_{i}&{\text{if }}y=1\\1-p_{i}&{\text{if }}y=0\end{cases}}\\[5pt]\Pr(Y_{i}=y\mid x_{1,i},\ldots ,x_{m,i})&=p_{i}^{y}(1-p_{i})^{(1-y)}\end{aligned}}$

The meanings of these four lines are:

1. The first line expresses the probability distribution of each *Y**i* : conditioned on the explanatory variables, it follows a Bernoulli distribution with parameters *p**i*, the probability of the outcome of 1 for trial *i*. As noted above, each separate trial has its own probability of success, just as each trial has its own explanatory variables. The probability of success *p**i* is not observed, only the outcome of an individual Bernoulli trial using that probability.
2. The second line expresses the fact that the expected value of each *Y**i* is equal to the probability of success *p**i*, which is a general property of the Bernoulli distribution. In other words, if we run a large number of Bernoulli trials using the same probability of success *p**i*, then take the average of all the 1 and 0 outcomes, then the result would be close to *p**i*. This is because doing an average this way simply computes the proportion of successes seen, which we expect to converge to the underlying probability of success.
3. The third line writes out the probability mass function of the Bernoulli distribution, specifying the probability of seeing each of the two possible outcomes.
4. The fourth line is another way of writing the probability mass function, which avoids having to write separate cases and is more convenient for certain types of calculations. This relies on the fact that *Y**i* can take only the value 0 or 1. In each case, one of the exponents will be 1, "choosing" the value under it, while the other is 0, "canceling out" the value under it. Hence, the outcome is either *p**i* or 1 − *p**i*, as in the previous line.

**Linear predictor function**

The basic idea of logistic regression is to use the mechanism already developed for linear regression by modeling the probability *p**i* using a linear predictor function, i.e. a linear combination of the explanatory variables and a set of regression coefficients that are specific to the model at hand but the same for all trials. The linear predictor function $f(i)$ for a particular data point *i* is written as:

$f(i)=\beta _{0}+\beta _{1}x_{1,i}+\cdots +\beta _{m}x_{m,i},$

where $\beta _{0},\ldots ,\beta _{m}$ are regression coefficients indicating the relative effect of a particular explanatory variable on the outcome.

The model is usually put into a more compact form as follows:

- The regression coefficients *β*0, *β*1, ..., *β**m* are grouped into a single vector ***β*** of size *m* + 1.
- For each data point *i*, an additional explanatory pseudo-variable *x*0,*i* is added, with a fixed value of 1, corresponding to the intercept coefficient *β*0.
- The resulting explanatory variables *x*0,*i*, *x*1,*i*, ..., *x**m,i* are then grouped into a single vector ***Xi*** of size *m* + 1.

This makes it possible to write the linear predictor function as follows:

$f(i)={\boldsymbol {\beta }}\cdot \mathbf {X} _{i},$

using the notation for a dot product between two vectors.

### Many explanatory variables, two categories

The above example of binary logistic regression on one explanatory variable can be generalized to binary logistic regression on any number of explanatory variables *x1, x2,...* and any number of categorical values $y=0,1,2,\dots$ .

To begin with, we may consider a logistic model with *M* explanatory variables, *x1*, *x2* ... *xM* and, as in the example above, two categorical values (*y* = 0 and 1). For the simple binary logistic regression model, we assumed a linear relationship between the predictor variable and the log-odds (also called logit) of the event that $y=1$ . This linear relationship may be extended to the case of *M* explanatory variables:

$t=\log _{b}{\frac {p}{1-p}}=\beta _{0}+\beta _{1}x_{1}+\beta _{2}x_{2}+\cdots +\beta _{M}x_{M}$

where *t* is the log-odds and $\beta _{i}$ are parameters of the model. An additional generalization has been introduced in which the base of the model (*b*) is not restricted to Euler's number *e*. In most applications, the base b of the logarithm is usually taken to be *e*. However, in some cases it can be easier to communicate results by working in base 2 or base 10.

For a more compact notation, we will specify the explanatory variables and the *β* coefficients as ⁠ $(M+1)$ ⁠-dimensional vectors:

${\boldsymbol {x}}=\{x_{0},x_{1},x_{2},\dots ,x_{M}\}$

${\boldsymbol {\beta }}=\{\beta _{0},\beta _{1},\beta _{2},\dots ,\beta _{M}\}$

with an added explanatory variable *x0* =1. The logit may now be written as:

$t=\sum _{m=0}^{M}\beta _{m}x_{m}={\boldsymbol {\beta }}\cdot x$

Solving for the probability *p* that $y=1$ yields:

$p({\boldsymbol {x}})={\frac {b^{{\boldsymbol {\beta }}\cdot {\boldsymbol {x}}}}{1+b^{{\boldsymbol {\beta }}\cdot {\boldsymbol {x}}}}}={\frac {1}{1+b^{-{\boldsymbol {\beta }}\cdot {\boldsymbol {x}}}}}=S_{b}(t)$

,

where $S_{b}$ is the sigmoid function with base b . The above formula shows that once the $\beta _{m}$ are fixed, we can easily compute either the log-odds that $y=1$ for a given observation, or the probability that $y=1$ for a given observation. The main use-case of a logistic model is to be given an observation ${\boldsymbol {x}}$ , and estimate the probability $p({\boldsymbol {x}})$ that $y=1$ . The optimum beta coefficients may again be found by maximizing the log-likelihood. For *K* measurements, defining ${\boldsymbol {x}}_{k}$ as the explanatory vector of the *k*-th measurement, and $y_{k}$ as the categorical outcome of that measurement, the log likelihood may be written in a form very similar to the simple $M=1$ case above:

$\ell =\sum _{k=1}^{K}y_{k}\log _{b}(p({\boldsymbol {x_{k}}}))+\sum _{k=1}^{K}(1-y_{k})\log _{b}(1-p({\boldsymbol {x_{k}}}))$

As in the simple example above, finding the optimum *β* parameters will require numerical methods. One useful technique is to equate the derivatives of the log likelihood with respect to each of the *β* parameters to zero yielding a set of equations which will hold at the maximum of the log likelihood:

${\frac {\partial \ell }{\partial \beta _{m}}}=0=\sum _{k=1}^{K}y_{k}x_{mk}-\sum _{k=1}^{K}p({\boldsymbol {x}}_{k})x_{mk}$

where *xmk* is the value of the *xm* explanatory variable from the *k-th* measurement.

Consider an example with $M=2$ explanatory variables, $b=10$ , and coefficients $\beta _{0}=-3$ , $\beta _{1}=1$ , and $\beta _{2}=2$ which have been determined by the above method. To be concrete, the model is:

$t=\log _{10}{\frac {p}{1-p}}=-3+x_{1}+2x_{2}$

$p={\frac {b^{{\boldsymbol {\beta }}\cdot {\boldsymbol {x}}}}{1+b^{{\boldsymbol {\beta }}\cdot x}}}={\frac {b^{\beta _{0}+\beta _{1}x_{1}+\beta _{2}x_{2}}}{1+b^{\beta _{0}+\beta _{1}x_{1}+\beta _{2}x_{2}}}}={\frac {1}{1+b^{-(\beta _{0}+\beta _{1}x_{1}+\beta _{2}x_{2})}}}$

,

where *p* is the probability of the event that $y=1$ . This can be interpreted as follows:

- $\beta _{0}=-3$ is the *y*-intercept. It is the log-odds of the event that $y=1$ , when the predictors $x_{1}=x_{2}=0$ . By exponentiating, we can see that when $x_{1}=x_{2}=0$ the odds of the event that $y=1$ are 1-to-1000, or $10^{-3}$ . Similarly, the probability of the event that $y=1$ when $x_{1}=x_{2}=0$ can be computed as $1/(1000+1)=1/1001.$
- $\beta _{1}=1$ means that increasing $x_{1}$ by 1 increases the log-odds by 1 . So if $x_{1}$ increases by 1, the odds that $y=1$ increase by a factor of $10^{1}$ . The probability of $y=1$ has also increased, but it has not increased by as much as the odds have increased.
- $\beta _{2}=2$ means that increasing $x_{2}$ by 1 increases the log-odds by 2 . So if $x_{2}$ increases by 1, the odds that $y=1$ increase by a factor of $10^{2}.$ Note how the effect of $x_{2}$ on the log-odds is twice as great as the effect of $x_{1}$ , but the effect on the odds is 10 times greater. But the effect on the probability of $y=1$ is not as much as 10 times greater, it's only the effect on the odds that is 10 times greater.

### Multinomial logistic regression: Many explanatory variables and many categories

In the above cases of two categories (binomial logistic regression), the categories were indexed by "0" and "1", and we had two probabilities: The probability that the outcome was in category 1 was given by $p({\boldsymbol {x}})$ and the probability that the outcome was in category 0 was given by $1-p({\boldsymbol {x}})$ . The sum of these probabilities equals 1, which must be true, since "0" and "1" are the only possible categories in this setup.

In general, if we have ⁠ $M+1$ ⁠ explanatory variables (including *x0*) and ⁠ $N+1$ ⁠ categories, we will need ⁠ $N+1$ ⁠ separate probabilities, one for each category, indexed by *n*, which describe the probability that the categorical outcome *y* will be in category *y=n*, conditional on the vector of covariates **x**. The sum of these probabilities over all categories must equal 1. Using the mathematically convenient base *e*, these probabilities are:

$p_{n}({\boldsymbol {x}})={\frac {e^{{\boldsymbol {\beta }}_{n}\cdot {\boldsymbol {x}}}}{1+\sum _{u=1}^{N}e^{{\boldsymbol {\beta }}_{u}\cdot {\boldsymbol {x}}}}}$

for

$n=1,2,\dots ,N$

$p_{0}({\boldsymbol {x}})=1-\sum _{n=1}^{N}p_{n}({\boldsymbol {x}})={\frac {1}{1+\sum _{u=1}^{N}e^{{\boldsymbol {\beta }}_{u}\cdot {\boldsymbol {x}}}}}$

Each of the probabilities except $p_{0}({\boldsymbol {x}})$ will have their own set of regression coefficients ${\boldsymbol {\beta }}_{n}$ . It can be seen that, as required, the sum of the $p_{n}({\boldsymbol {x}})$ over all categories *n* is 1. The selection of $p_{0}({\boldsymbol {x}})$ to be defined in terms of the other probabilities is artificial. Any of the probabilities could have been selected to be so defined. This special value of *n* is termed the "pivot index", and the log-odds (*tn*) are expressed in terms of the pivot probability and are again expressed as a linear combination of the explanatory variables:

$t_{n}=\ln \left({\frac {p_{n}({\boldsymbol {x}})}{p_{0}({\boldsymbol {x}})}}\right)={\boldsymbol {\beta }}_{n}\cdot {\boldsymbol {x}}$

Note also that for the simple case of $N=1$ , the two-category case is recovered, with $p({\boldsymbol {x}})=p_{1}({\boldsymbol {x}})$ and $p_{0}({\boldsymbol {x}})=1-p_{1}({\boldsymbol {x}})$ .

The log-likelihood that a particular set of *K* measurements or data points will be generated by the above probabilities can now be calculated. Indexing each measurement by *k*, let the *k*-th set of measured explanatory variables be denoted by ${\boldsymbol {x}}_{k}$ and their categorical outcomes be denoted by $y_{k}$ which can be equal to any integer in [0,N]. The log-likelihood is then:

$\ell =\sum _{k=1}^{K}\sum _{n=0}^{N}\Delta (n,y_{k})\,\ln(p_{n}({\boldsymbol {x}}_{k}))$

where $\Delta (n,y_{k})$ is an indicator function which equals 1 if *yk = n* and zero otherwise. In the case of two explanatory variables, this indicator function was defined as *yk* when *n* = 1 and *1-yk* when *n* = 0. This was convenient, but not necessary. Again, the optimum beta coefficients may be found by maximizing the log-likelihood function generally using numerical methods. A possible method of solution is to set the derivatives of the log-likelihood with respect to each beta coefficient equal to zero and solve for the beta coefficients:

${\frac {\partial \ell }{\partial \beta _{nm}}}=0=\sum _{k=1}^{K}\Delta (n,y_{k})x_{mk}-\sum _{k=1}^{K}p_{n}({\boldsymbol {x}}_{k})x_{mk}$

where $\beta _{nm}$ is the *m*-th coefficient of the ${\boldsymbol {\beta }}_{n}$ vector and $x_{mk}$ is the *m*-th explanatory variable of the *k*-th measurement. Once the beta coefficients have been estimated from the data, we will be able to estimate the probability that any subsequent set of explanatory variables will result in any of the possible outcome categories.
