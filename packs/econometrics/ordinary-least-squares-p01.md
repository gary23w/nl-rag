---
title: "Ordinary least squares (part 1/2)"
source: https://en.wikipedia.org/wiki/Ordinary_least_squares
domain: econometrics
license: CC-BY-SA-4.0
tags: econometrics, instrumental variables, panel data, gauss-markov theorem
fetched: 2026-07-02
part: 1/2
---

# Ordinary least squares

In statistics, **ordinary least squares** (**OLS**) is a type of linear least squares method for choosing the unknown parameters in a linear regression model by the principle of least squares: minimizing the sum of the squares of the differences between the observed dependent variable (values of the variable being observed) in the input dataset and the output of the (linear) function of the independent variable. Some sources consider OLS to be linear regression.

Geometrically, this is seen as the sum of the squared distances, parallel to the axis of the dependent variable, between each data point in the set and the corresponding point on the regression surface—the smaller the differences, the better the model fits the data. The resulting estimator can be expressed by a simple formula, especially in the case of a simple linear regression, in which there is a single regressor on the right side of the regression equation.

The OLS estimator is consistent for the level-one fixed effects when the regressors are exogenous and forms perfect colinearity (rank condition), consistent for the variance estimate of the residuals when regressors have finite fourth moments and—by the Gauss–Markov theorem—optimal in the class of linear unbiased estimators when the errors are homoscedastic and serially uncorrelated. Under these conditions, the method of OLS provides minimum-variance mean-unbiased estimation when the errors have finite variances. Under the additional assumption that the errors are normally distributed with zero mean, OLS is the maximum likelihood estimator that outperforms any non-linear unbiased estimator.


## Linear model

Suppose the data consists of n observations $\left\{\mathbf {x} _{i},y_{i}\right\}_{i=1}^{n}$ . Each observation i includes a scalar response $y_{i}$ and a column vector $\mathbf {x} _{i}$ of p parameters (regressors), i.e., $\mathbf {x} _{i}=\left[x_{i1},x_{i2},\dots ,x_{ip}\right]^{\operatorname {T} }$ . In a linear regression model, the response variable, $y_{i}$ , is a linear function of the regressors:

$y_{i}=\beta _{1}\ x_{i1}+\beta _{2}\ x_{i2}+\cdots +\beta _{p}\ x_{ip}+\varepsilon _{i},$

or in vector form,

$y_{i}=\mathbf {x} _{i}^{\operatorname {T} }{\boldsymbol {\beta }}+\varepsilon _{i},\,$

where $\mathbf {x} _{i}$ , as introduced previously, is a column vector of the i -th observation of all the explanatory variables; ${\boldsymbol {\beta }}$ is a $p\times 1$ vector of unknown parameters; and the scalar $\varepsilon _{i}$ represents unobserved random variables (errors) of the i -th observation. $\varepsilon _{i}$ accounts for the influences upon the responses $y_{i}$ from sources other than the explanatory variables $\mathbf {x} _{i}$ . This model can also be written in matrix notation as

$\mathbf {y} =\mathbf {X} {\boldsymbol {\beta }}+{\boldsymbol {\varepsilon }},\,$

where $\mathbf {y}$ and ${\boldsymbol {\varepsilon }}$ are $n\times 1$ vectors of the response variables and the errors of the n observations, and $\mathbf {X}$ is an $n\times p$ matrix of regressors, also sometimes called the design matrix, whose row i is $\mathbf {x} _{i}^{\operatorname {T} }$ and contains the i -th observations on all the explanatory variables.

Typically, a constant term is included in the set of regressors $\mathbf {X}$ , say, by taking $x_{i1}=1$ for all $i=1,\dots ,n$ . The coefficient $\beta _{1}$ corresponding to this regressor is called the *intercept*. Without the intercept, the fitted line is forced to cross the origin when $x_{i}={\vec {0}}$ .

Regressors do not have to be independent for estimation to be consistent e.g. they may be non-linearly dependent. Short of perfect multicollinearity, parameter estimates may still be consistent; however, as multicollinearity rises the standard error around such estimates increases and reduces the precision of such estimates. When there is perfect multicollinearity, it is no longer possible to obtain unique estimates for the coefficients to the related regressors; estimation for these parameters cannot converge (thus, it cannot be consistent).

As a concrete example where regressors are non-linearly dependent yet estimation may still be consistent, we might suspect the response depends linearly both on a value and its square; in which case we would include one regressor whose value is just the square of another regressor. In that case, the model would be *quadratic* in the second regressor, but none-the-less is still considered a *linear* model because the model *is* still linear in the parameters ( ${\boldsymbol {\beta }}$ ).

### Matrix/vector formulation

Consider an overdetermined system

$\sum _{j=1}^{p}x_{ij}\beta _{j}=y_{i},\ (i=1,2,\dots ,n),$

of n linear equations in p unknown coefficients, $\beta _{1},\beta _{2},\dots ,\beta _{p}$ , with $n>p$ . This can be written in matrix form as

$\mathbf {X} {\boldsymbol {\beta }}=\mathbf {y} ,$

where

$\mathbf {X} ={\begin{bmatrix}X_{11}&X_{12}&\cdots &X_{1p}\\X_{21}&X_{22}&\cdots &X_{2p}\\\vdots &\vdots &\ddots &\vdots \\X_{n1}&X_{n2}&\cdots &X_{np}\end{bmatrix}},\qquad {\boldsymbol {\beta }}={\begin{bmatrix}\beta _{1}\\\beta _{2}\\\vdots \\\beta _{p}\end{bmatrix}},\qquad \mathbf {y} ={\begin{bmatrix}y_{1}\\y_{2}\\\vdots \\y_{n}\end{bmatrix}}.$

(Note: for a linear model as above, not all elements in $\mathbf {X}$ contains information on the data points. The first column is populated with ones, $X_{i1}=1$ . Only the other columns contain actual data. So here p is equal to the number of regressors plus one).

Such a system usually has no exact solution, so the goal is instead to find the coefficients ${\boldsymbol {\beta }}$ which fit the equations "best", in the sense of solving the quadratic minimization problem

${\hat {\boldsymbol {\beta }}}={\underset {\boldsymbol {\beta }}{\operatorname {arg\,min} }}\,S({\boldsymbol {\beta }}),$

where the objective function

S

is given by:

$S({\boldsymbol {\beta }})=\sum _{i=1}^{n}\left|y_{i}-\sum _{j=1}^{p}X_{ij}\beta _{j}\right|^{2}=\left\|\mathbf {y} -\mathbf {X} {\boldsymbol {\beta }}\right\|^{2}.$

A justification for choosing this criterion is given in Properties below. This minimization problem has a unique solution, provided that the p columns of the matrix $\mathbf {X}$ are linearly independent, given by solving the so-called *normal equations*:

$\left(\mathbf {X} ^{\operatorname {T} }\mathbf {X} \right){\hat {\boldsymbol {\beta }}}=\mathbf {X} ^{\operatorname {T} }\mathbf {y} \ .$

The matrix $\mathbf {X} ^{\operatorname {T} }\mathbf {X}$ is known as the *normal matrix* or Gram matrix and the matrix $\mathbf {X} ^{\operatorname {T} }\mathbf {y}$ is known as the moment matrix of regressand by regressors. Finally, ${\hat {\boldsymbol {\beta }}}$ is the coefficient vector of the least-squares hyperplane, expressed as

${\hat {\boldsymbol {\beta }}}=\left(\mathbf {X} ^{\top }\mathbf {X} \right)^{-1}\mathbf {X} ^{\top }\mathbf {y} .$

or

${\hat {\boldsymbol {\beta }}}={\boldsymbol {\beta }}+\left(\mathbf {X} ^{\top }\mathbf {X} \right)^{-1}\mathbf {X} ^{\top }{\boldsymbol {\varepsilon }}.$


## Estimation

Suppose *b* is a "candidate" value for the parameter vector *β*. The quantity *yi* − *xi*T*b*, called the *residual* for the *i*-th observation, measures the vertical distance between the data point (*xi*, *yi*) and the hyperplane *y* = *x*T*b*, and thus assesses the degree of fit between the actual data and the model. The *sum of squared residuals* (*SSR*) (also called the *error sum of squares* (*ESS*) or *residual sum of squares* (*RSS*)) is a measure of the overall model fit:

$S(b)=\sum _{i=1}^{n}(y_{i}-x_{i}^{\operatorname {T} }b)^{2}=(y-Xb)^{\operatorname {T} }(y-Xb),$

where *T* denotes the matrix transpose, and the rows of *X*, denoting the values of all the independent variables associated with a particular value of the dependent variable, are *Xi = xi*T. The value of *b* which minimizes this sum is called the **OLS estimator for *β***. The function *S*(*b*) is quadratic in *b* with positive-definite Hessian, and therefore this function possesses a unique global minimum at $b={\hat {\beta }}$ , which can be given by the explicit formula[proof]

${\hat {\beta }}=\operatorname {argmin} _{b\in \mathbb {R} ^{p}}S(b)=(X^{\operatorname {T} }X)^{-1}X^{\operatorname {T} }y\ .$

The product *N* = *X*T *X* is a Gram matrix, and its inverse, *Q* = *N*−1, is the *cofactor matrix* of *β*, closely related to its covariance matrix, *C**β*. The matrix (*X*T *X*)−1 *X*T = *Q* *X*T is called the Moore–Penrose pseudoinverse matrix of *X*. This formulation highlights the point that estimation can be carried out if, and only if, there is no perfect multicollinearity between the explanatory variables (which would cause the Gram matrix to have no inverse).


## Prediction

After we have estimated *β*, the *fitted values* (or *predicted values*) from the regression will be

${\hat {y}}=X{\hat {\beta }}=Py,$

where *P* = *X*(*X*T*X*)−1*X*T is the *projection matrix* onto the space *V* spanned by the columns of *X*. This matrix *P* is also sometimes called the *hat matrix* because it "puts a hat" onto the variable *y*. Another matrix, closely related to *P* is the *annihilator* matrix *M* = *In* − *P*; this is a projection matrix onto the space orthogonal to *V*. Both matrices *P* and *M* are symmetric and idempotent (meaning that *P*2 = *P* and *M*2 = *M*), and relate to the data matrix *X* via identities *PX* = *X* and *MX* = 0. Matrix *M* creates the *residuals* from the regression:

${\hat {\varepsilon }}=y-{\hat {y}}=y-X{\hat {\beta }}=My=M(X\beta +\varepsilon )=(MX)\beta +M\varepsilon =M\varepsilon .$

The variances of the predicted values $s_{{\hat {y}}_{i}}^{2}$ are found in the main diagonal of the variance-covariance matrix of predicted values:

$C_{\hat {y}}=s^{2}P,$

where *P* is the projection matrix and *s*2 is the sample variance. The full matrix is very large; its diagonal elements can be calculated individually as:

$s_{{\hat {y}}_{i}}^{2}=s^{2}X_{i}(X^{T}X)^{-1}X_{i}^{T},$

where *X*i is the *i*-th row of matrix *X*.


## Sample statistics

Using these residuals we can estimate the sample variance *s*2 using the *reduced chi-squared* statistic:

$s^{2}={\frac {{\hat {\varepsilon }}^{\mathrm {T} }{\hat {\varepsilon }}}{n-p}}={\frac {(My)^{\mathrm {T} }My}{n-p}}={\frac {y^{\mathrm {T} }M^{\mathrm {T} }My}{n-p}}={\frac {y^{\mathrm {T} }My}{n-p}}={\frac {S({\hat {\beta }})}{n-p}},\qquad {\hat {\sigma }}^{2}={\frac {n-p}{n}}\;s^{2}$

The denominator, *n*−*p*, is the statistical degrees of freedom. The first quantity, *s*2, is the OLS estimate for *σ*2, whereas the second, $\scriptstyle {\hat {\sigma }}^{2}$ , is the MLE estimate for *σ*2. The two estimators are quite similar in large samples; the first estimator is always unbiased, while the second estimator is biased but has a smaller mean squared error. In practice *s*2 is used more often, since it is more convenient for the hypothesis testing. The square root of *s*2 is called the *regression standard error*, *standard error of the regression*, or *standard error of the equation*.

It is common to assess the goodness-of-fit of the OLS regression by comparing how much the initial variation in the sample can be reduced by regressing onto *X*. The *coefficient of determination* *R*2 is defined as a ratio of "explained" variance to the "total" variance of the dependent variable *y*, in the cases where the regression sum of squares equals the sum of squares of residuals:

$R^{2}={\frac {\sum ({\hat {y}}_{i}-{\overline {y}})^{2}}{\sum (y_{i}-{\overline {y}})^{2}}}={\frac {y^{\mathrm {T} }P^{\mathrm {T} }LPy}{y^{\mathrm {T} }Ly}}=1-{\frac {y^{\mathrm {T} }My}{y^{\mathrm {T} }Ly}}=1-{\frac {\rm {RSS}}{\rm {TSS}}}$

where TSS is the *total sum of squares* for the dependent variable, ${\textstyle L=I_{n}-{\frac {1}{n}}J_{n}}$ , and ${\textstyle J_{n}}$ is an *n*×*n* matrix of ones. ( L is a centering matrix which is equivalent to regression on a constant; it simply subtracts the mean from a variable.) In order for *R*2 to be meaningful, the matrix *X* of data on regressors must contain a column vector of ones to represent the constant whose coefficient is the regression intercept. In that case, *R*2 will always be a number between 0 and 1, with values close to 1 indicating a good degree of fit.

### Simple linear regression model

If the data matrix *X* contains only two variables, a constant and a scalar regressor *xi*, then this is called the "simple regression model". This case is often considered in the beginner statistics classes, as it provides much simpler formulas even suitable for manual calculation. The parameters are commonly denoted as (*α*, *β*):

$y_{i}=\alpha +\beta x_{i}+\varepsilon _{i}.$

The least squares estimates in this case are given by simple formulas

${\begin{aligned}{\widehat {\beta }}&={\frac {\sum _{i=1}^{n}{(x_{i}-{\bar {x}})(y_{i}-{\bar {y}})}}{\sum _{i=1}^{n}{(x_{i}-{\bar {x}})^{2}}}}\\[2pt]{\widehat {\alpha }}&={\bar {y}}-{\widehat {\beta }}\,{\bar {x}}\ ,\end{aligned}}$


## Alternative derivations

In the previous section the least squares estimator ${\hat {\beta }}$ was obtained as a value that minimizes the sum of squared residuals of the model. However it is also possible to derive the same estimator from other approaches. In all cases the formula for OLS estimator remains the same: ^*β* = (*X*T*X*)−1*X*T*y*; the only difference is in how we interpret this result.

### Projection

For mathematicians, OLS is an approximate solution to an overdetermined system of linear equations *Xβ* ≈ *y*, where *β* is the unknown. Assuming the system cannot be solved exactly (the number of equations *n* is much larger than the number of unknowns *p*), we are looking for a solution that could provide the smallest discrepancy between the right- and left- hand sides. In other words, we are looking for the solution that satisfies

${\hat {\beta }}={\rm {arg}}\min _{\beta }\,\lVert \mathbf {y} -\mathbf {X} {\boldsymbol {\beta }}\rVert ^{2},$

where ‖·‖ is the standard *L*2 norm in the *n*-dimensional Euclidean space **R***n*. The predicted quantity *Xβ* is just a certain linear combination of the vectors of regressors. Thus, the residual vector *y* − *Xβ* will have the smallest length when *y* is projected orthogonally onto the linear subspace spanned by the columns of *X*. The OLS estimator ${\hat {\beta }}$ in this case can be interpreted as the coefficients of vector decomposition of ^*y* = *Py* along the basis of *X*.

In other words, the gradient equations at the minimum can be written as:

$(\mathbf {y} -\mathbf {X} {\hat {\boldsymbol {\beta }}})^{\top }\mathbf {X} =0.$

A geometrical interpretation of these equations is that the vector of residuals, $\mathbf {y} -X{\hat {\boldsymbol {\beta }}}$ is orthogonal to the column space of *X*, since the dot product $(\mathbf {y} -\mathbf {X} {\hat {\boldsymbol {\beta }}})\cdot \mathbf {X} \mathbf {v}$ is equal to zero for *any* conformal vector, **v**. This means that $\mathbf {y} -\mathbf {X} {\boldsymbol {\hat {\beta }}}$ is the shortest of all possible vectors $\mathbf {y} -\mathbf {X} {\boldsymbol {\beta }}$ , that is, the variance of the residuals is the minimum possible. This is illustrated at the right.

Introducing ${\hat {\boldsymbol {\gamma }}}$ and a matrix *K* with the assumption that a matrix $[\mathbf {X} \ \mathbf {K} ]$ is non-singular and *K*T *X* = 0 (cf. Orthogonal projections), the residual vector should satisfy the following equation:

${\hat {\mathbf {r} }}:=\mathbf {y} -\mathbf {X} {\hat {\boldsymbol {\beta }}}=\mathbf {K} {\hat {\boldsymbol {\gamma }}}.$

The equation and solution of linear least squares are thus described as follows:

${\begin{aligned}\mathbf {y} &={\begin{bmatrix}\mathbf {X} &\mathbf {K} \end{bmatrix}}{\begin{bmatrix}{\hat {\boldsymbol {\beta }}}\\{\hat {\boldsymbol {\gamma }}}\end{bmatrix}},\\{}\Rightarrow {\begin{bmatrix}{\hat {\boldsymbol {\beta }}}\\{\hat {\boldsymbol {\gamma }}}\end{bmatrix}}&={\begin{bmatrix}\mathbf {X} &\mathbf {K} \end{bmatrix}}^{-1}\mathbf {y} ={\begin{bmatrix}\left(\mathbf {X} ^{\top }\mathbf {X} \right)^{-1}\mathbf {X} ^{\top }\\\left(\mathbf {K} ^{\top }\mathbf {K} \right)^{-1}\mathbf {K} ^{\top }\end{bmatrix}}\mathbf {y} .\end{aligned}}$

Another way of looking at it is to consider the regression line to be a weighted average of the lines passing through the combination of any two points in the dataset. Although this way of calculation is more computationally expensive, it provides a better intuition on OLS.

### Maximum likelihood

The OLS estimator is identical to the maximum likelihood estimator (MLE) under the normality assumption for the error terms.[proof] This normality assumption has historical importance, as it provided the basis for the early work in linear regression analysis by Yule and Pearson. From the properties of MLE, we can infer that the OLS estimator is asymptotically efficient (in the sense of attaining the Cramér–Rao bound for variance) if the normality assumption is satisfied.

### Generalized method of moments

In iid case the OLS estimator can also be viewed as a GMM estimator arising from the moment conditions

$\mathrm {E} {\big [}\,x_{i}\left(y_{i}-x_{i}^{\operatorname {T} }\beta \right)\,{\big ]}=0.$

These moment conditions state that the regressors should be uncorrelated with the errors. Since *xi* is a *p*-vector, the number of moment conditions is equal to the dimension of the parameter vector *β*, and thus the system is exactly identified. This is the so-called classical GMM case, when the estimator does not depend on the choice of the weighting matrix.

Note that the original strict exogeneity assumption E[*εi* | *xi*] = 0 implies a far richer set of moment conditions than stated above. In particular, this assumption implies that for any vector-function ƒ, the moment condition E[*ƒ*(*xi*)·*εi*] = 0 will hold. However it can be shown using the Gauss–Markov theorem that the optimal choice of function ƒ is to take *ƒ*(*x*) = *x*, which results in the moment equation posted above.


## Assumptions

There are several different frameworks in which the linear regression model can be cast in order to make the OLS technique applicable. Each of these settings produces the same formulas and same results. The only difference is the interpretation and the assumptions which have to be imposed in order for the method to give meaningful results. The choice of the applicable framework depends mostly on the nature of data in hand, and on the inference task which has to be performed.

One of the lines of difference in interpretation is whether to treat the regressors as random variables, or as predefined constants. In the first case (**random design**) the regressors *xi* are random and sampled together with the *yi*'s from some population, as in an observational study. This approach allows for more natural study of the asymptotic properties of the estimators. In the other interpretation (**fixed design**), the regressors *X* are treated as known constants set by a design, and *y* is sampled conditionally on the values of *X* as in an experiment. For practical purposes, this distinction is often unimportant, since estimation and inference is carried out while conditioning on *X*. All results stated in this article are within the random design framework.

The classical model focuses on the "finite sample" estimation and inference, meaning that the number of observations *n* is fixed. This contrasts with the other approaches, which study the asymptotic behavior of OLS, and in which the behavior at a large number of samples is studied. To prove finite sample unbiasedness of the OLS estimator, we require the following assumptions.

- **Exogeneity**. The regressors do not covary with the error term: $\mathbb {E} [\varepsilon _{i}x_{i}]=0.$ This requires, for example, that there are no omitted variables that covary with observed variables and affect the response variable. An alternative (but stronger) statement that is often required when explaining linear regression in mathematical statistics is that the predictor variables *x* can be treated as fixed values, rather than random variables. This stronger form means, for example, that the predictor variables are assumed to be error-free, that is, not contaminated with measurement error. Although this assumption is not realistic in many settings, dropping it leads to more complex errors-in-variables models, instrumental variable models and the like.
- **Linearity**, or **correct specification**. This means that the mean of the response variable is a linear combination of the parameters (regression coefficients) and the predictor variables. Note that this assumption is much less restrictive than it may at first seem. Because the predictor variables are treated as fixed values (see above), linearity is really only a restriction on the parameters. The predictor variables themselves can be arbitrarily transformed, and in fact multiple copies of the same underlying predictor variable can be added, each one transformed differently. This technique is used, for example, in polynomial regression, which uses linear regression to fit the response variable as an arbitrary polynomial function (up to a given degree) of a predictor variable. With this much flexibility, models such as polynomial regression often have "too much power", in that they tend to overfit the data. As a result, some kind of regularization must typically be used to prevent unreasonable solutions coming out of the estimation process. Common examples are ridge regression and lasso regression. Bayesian linear regression can also be used, which by its nature is more or less immune to the problem of overfitting. (In fact, ridge regression and lasso regression can both be viewed as special cases of Bayesian linear regression, with particular types of prior distributions placed on the regression coefficients.)
- **Constant variance** or **homoscedasticity**. This means that the variance of the errors does not depend on the values of the predictor variables: $\mathbb {E} [\varepsilon _{i}^{2}|x_{i}]=\sigma ^{2}.$ Thus the variability of the responses for given fixed values of the predictors is the same regardless of how large or small the responses are. This is often not the case, as a variable whose mean is large will typically have a greater variance than one whose mean is small. For example, a person whose income is predicted to be $100,000 may easily have an actual income of $80,000 or $120,000—i.e., a standard deviation of around $20,000—while another person with a predicted income of $10,000 is unlikely to have the same $20,000 standard deviation, since that would imply their actual income could vary anywhere between −$10,000 and $30,000. (In fact, as this shows, in many cases—often the same cases where the assumption of normally distributed errors fails—the variance or standard deviation should be predicted to be proportional to the mean, rather than constant.) The absence of homoscedasticity is called heteroscedasticity. In order to check this assumption, a plot of residuals versus predicted values (or the values of each individual predictor) can be examined for a "fanning effect" (i.e., increasing or decreasing vertical spread as one moves left to right on the plot). A plot of the absolute or squared residuals versus the predicted values (or each predictor) can also be examined for a trend or curvature. Formal tests can also be used; see Heteroscedasticity. The presence of heteroscedasticity will result in an overall "average" estimate of variance being used instead of one that takes into account the true variance structure. This leads to less precise (but in the case of ordinary least squares, not biased) parameter estimates and biased standard errors, resulting in misleading tests and interval estimates. The mean squared error for the model will also be wrong. Various estimation techniques including weighted least squares and the use of heteroscedasticity-consistent standard errors can handle heteroscedasticity in a quite general way. Bayesian linear regression techniques can also be used when the variance is assumed to be a function of the mean. It is also possible in some cases to fix the problem by applying a transformation to the response variable (e.g., fitting the logarithm of the response variable using a linear regression model, which implies that the response variable itself has a log-normal distribution rather than a normal distribution).

- **Uncorrelatedness of errors**. This assumes that the errors of the response variables are uncorrelated with each other: $\mathbb {E} [\varepsilon _{i}\varepsilon _{j}|x_{i},x_{j}]=0.$ Some methods such as generalized least squares are capable of handling correlated errors, although they typically require significantly more data unless some sort of regularization is used to bias the model towards assuming uncorrelated errors. Bayesian linear regression is a general way of handling this issue. Full statistical independence is a stronger condition than mere lack of correlation and is often not needed, although it implies mean-independence.
- **Lack of perfect multicollinearity** in the predictors. For standard least squares estimation methods, the design matrix *X* must have full column rank *p*: $\Pr \!{\big [}\,\operatorname {rank} (X)=p\,{\big ]}=1.$ If this assumption is violated, perfect multicollinearity exists in the predictor variables, meaning a linear relationship exists between two or more predictor variables. Multicollinearity can be caused by accidentally duplicating a variable in the data, using a linear transformation of a variable along with the original (e.g., the same temperature measurements expressed in Fahrenheit and Celsius), or including a linear combination of multiple variables in the model, such as their mean. It can also happen if there is too little data available compared to the number of parameters to be estimated (e.g., fewer data points than regression coefficients). Near violations of this assumption, where predictors are highly but not perfectly correlated, can reduce the precision of parameter estimates (see Variance inflation factor). In the case of perfect multicollinearity, the parameter vector ***β*** will be non-identifiable—it has no unique solution. In such a case, only some of the parameters can be identified (i.e., their values can only be estimated within some linear subspace of the full parameter space **R***p*). See partial least squares regression. Methods for fitting linear models with multicollinearity have been developed, some of which require additional assumptions such as "effect sparsity"—that a large fraction of the effects are exactly zero. Note that the more computationally expensive iterated algorithms for parameter estimation, such as those used in generalized linear models, do not suffer from this problem.

Violations of these assumptions can result in biased estimations of ***β***, biased standard errors, untrustworthy confidence intervals and significance tests. Beyond these assumptions, several other statistical properties of the data strongly influence the performance of different estimation methods:

- The statistical relationship between the error terms and the regressors plays an important role in determining whether an estimation procedure has desirable sampling properties such as being unbiased and consistent.
- The arrangement, or probability distribution of the predictor variables **x** has a major influence on the precision of estimates of ***β***. Sampling and design of experiments are highly developed subfields of statistics that provide guidance for collecting data in such a way to achieve a precise estimate of ***β***.


## Properties

### Finite sample properties

First of all, under the *strict exogeneity* assumption the OLS estimators $\scriptstyle {\hat {\beta }}$ and *s*2 are unbiased, meaning that their expected values coincide with the true values of the parameters:[proof]

$\operatorname {E} [\,{\hat {\beta }}\mid X\,]=\beta ,\quad \operatorname {E} [\,s^{2}\mid X\,]=\sigma ^{2}.$

If the strict exogeneity does not hold (as is the case with many time series models, where exogeneity is assumed only with respect to the past shocks but not the future ones), then these estimators will be biased in finite samples.

The *variance-covariance matrix* (or simply *covariance matrix*) of $\scriptstyle {\hat {\beta }}$ is equal to

$\operatorname {Var} [\,{\hat {\beta }}\mid X\,]=\sigma ^{2}\left(X^{\operatorname {T} }X\right)^{-1}=\sigma ^{2}Q.$

In particular, the standard error of each coefficient $\scriptstyle {\hat {\beta }}_{j}$ is equal to square root of the *j*-th diagonal element of this matrix. The estimate of this standard error is obtained by replacing the unknown quantity *σ*2 with its estimate *s*2. Thus,

${\widehat {\operatorname {s.\!e.} }}({\hat {\beta }}_{j})={\sqrt {s^{2}\left(X^{\operatorname {T} }X\right)_{jj}^{-1}}}$

It can also be easily shown that the estimator $\scriptstyle {\hat {\beta }}$ is uncorrelated with the residuals from the model:

$\operatorname {Cov} [\,{\hat {\beta }},{\hat {\varepsilon }}\mid X\,]=0.$

The *Gauss–Markov theorem* states that under the *spherical errors* assumption (that is, the errors should be uncorrelated and homoscedastic) the estimator $\scriptstyle {\hat {\beta }}$ is efficient in the class of linear unbiased estimators. This is called the *best linear unbiased estimator* (BLUE). Efficiency should be understood as if we were to find some other estimator $\scriptstyle {\tilde {\beta }}$ which would be linear in *y* and unbiased, then

$\operatorname {Var} [\,{\tilde {\beta }}\mid X\,]-\operatorname {Var} [\,{\hat {\beta }}\mid X\,]\geq 0$

in the sense that this is a nonnegative-definite matrix. This theorem establishes optimality only in the class of linear unbiased estimators, which is quite restrictive. Depending on the distribution of the error terms *ε*, other, non-linear estimators may provide better results than OLS.

#### Assuming normality

The properties listed so far are all valid regardless of the underlying distribution of the error terms. However, if you are willing to assume that the *normality assumption* holds (that is, that *ε* ~ *N*(0, *σ*2*In*)), then additional properties of the OLS estimators can be stated.

The estimator $\scriptstyle {\hat {\beta }}$ is normally distributed, with mean and variance as given before:

${\hat {\beta }}\ \sim \ {\mathcal {N}}{\big (}\beta ,\ \sigma ^{2}(X^{\mathrm {T} }X)^{-1}{\big )}.$

This estimator reaches the Cramér–Rao bound for the model, and thus is optimal in the class of all unbiased estimators. Note that unlike the Gauss–Markov theorem, this result establishes optimality among both linear and non-linear estimators, but only in the case of normally distributed error terms.

The estimator *s*2 will be proportional to the chi-squared distribution:

$s^{2}\ \sim \ {\frac {\sigma ^{2}}{n-p}}\cdot \chi _{n-p}^{2}$

The variance of this estimator is equal to 2*σ*4/(*n* − *p*), which does not attain the Cramér–Rao bound of 2*σ*4/*n*. However it was shown that there are no unbiased estimators of *σ*2 with variance smaller than that of the estimator *s*2. If we are willing to allow biased estimators, and consider the class of estimators that are proportional to the sum of squared residuals (SSR) of the model, then the best (in the sense of the mean squared error) estimator in this class will be ~*σ*2 = SSR */* (*n* − *p* + 2), which even beats the Cramér–Rao bound in case when there is only one regressor (*p* = 1).

Moreover, the estimators $\scriptstyle {\hat {\beta }}$ and *s*2 are independent, the fact which comes in useful when constructing the t- and F-tests for the regression.

#### Influential observations

As was mentioned before, the estimator ${\hat {\beta }}$ is linear in *y*, meaning that it represents a linear combination of the dependent variables *yi*. The weights in this linear combination are functions of the regressors *X*, and generally are unequal. The observations with high weights are called **influential** because they have a more pronounced effect on the value of the estimator.

To analyze which observations are influential we remove a specific *j*-th observation and consider how much the estimated quantities are going to change (similarly to the jackknife method). It can be shown that the change in the OLS estimator for *β* will be equal to

${\hat {\beta }}^{(j)}-{\hat {\beta }}=-{\frac {1}{1-h_{j}}}(X^{\mathrm {T} }X)^{-1}x_{j}^{\mathrm {T} }{\hat {\varepsilon }}_{j}\,,$

where *hj* = *xj*T (*X*T*X*)−1*xj* is the *j*-th diagonal element of the hat matrix *P*, and *xj* is the vector of regressors corresponding to the *j*-th observation. Similarly, the change in the predicted value for *j*-th observation resulting from omitting that observation from the dataset will be equal to

${\hat {y}}_{j}^{(j)}-{\hat {y}}_{j}=x_{j}^{\mathrm {T} }{\hat {\beta }}^{(j)}-x_{j}^{\operatorname {T} }{\hat {\beta }}=-{\frac {h_{j}}{1-h_{j}}}\,{\hat {\varepsilon }}_{j}$

From the properties of the hat matrix, 0 ≤ *hj* ≤ 1, and they sum up to *p*, so that on average *hj* ≈ *p/n*. These quantities *hj* are called the **leverages**, and observations with high *hj* are called **leverage points**. Usually the observations with high leverage ought to be scrutinized more carefully, in case they are erroneous, or outliers, or in some other way atypical of the rest of the dataset.

#### Partitioned regression

Sometimes the variables and corresponding parameters in the regression can be logically split into two groups, so that the regression takes form

$y=X_{1}\beta _{1}+X_{2}\beta _{2}+\varepsilon ,$

where *X*1 and *X*2 have dimensions *n*×*p*1, *n*×*p*2, and *β*1, *β*2 are *p*1×1 and *p*2×1 vectors, with *p*1 + *p*2 = *p*.

The **Frisch–Waugh–Lovell theorem** states that in this regression the residuals ${\hat {\varepsilon }}$ and the OLS estimate $\scriptstyle {\hat {\beta }}_{2}$ will be numerically identical to the residuals and the OLS estimate for *β*2 in the following regression:

$M_{1}y=M_{1}X_{2}\beta _{2}+\eta \,,$

where *M*1 is the annihilator matrix for regressors *X*1.

The theorem can be used to establish a number of theoretical results. For example, having a regression with a constant and another regressor is equivalent to subtracting the means from the dependent variable and the regressor and then running the regression for the de-meaned variables but without the constant term.

### Large sample properties

The least squares estimators are point estimates of the linear regression model parameters *β*. However, generally we also want to know how close those estimates might be to the true values of parameters. In other words, we want to construct the interval estimates.

Since we have not made any assumption about the distribution of error term *εi*, it is impossible to infer the distribution of the estimators ${\hat {\beta }}$ and ${\hat {\sigma }}^{2}$ . Nevertheless, we can apply the central limit theorem to derive their *asymptotic* properties as sample size *n* goes to infinity. While the sample size is necessarily finite, it is customary to assume that *n* is "large enough" so that the true distribution of the OLS estimator is close to its asymptotic limit.

We can show that under the model assumptions, the least squares estimator for *β* is consistent (that is ${\hat {\beta }}$ converges in probability to *β*) and asymptotically normal:[proof]

$({\hat {\beta }}-\beta )\ {\xrightarrow {d}}\ {\mathcal {N}}{\big (}0,\;\sigma ^{2}Q_{xx}^{-1}{\big )},$

where $Q_{xx}=X^{\operatorname {T} }X.$

#### Inference

Using this asymptotic distribution, approximate two-sided confidence intervals for the *j*-th component of the vector ${\hat {\beta }}$ can be constructed as

$\beta _{j}\in {\bigg [}\ {\hat {\beta }}_{j}\pm q_{1-{\frac {\alpha }{2}}}^{{\mathcal {N}}(0,1)}\!{\sqrt {{\hat {\sigma }}^{2}\left[Q_{xx}^{-1}\right]_{jj}}}\ {\bigg ]}$

at the

1 −

α

confidence level,

where *q* denotes the quantile function of standard normal distribution, and [·]*jj* is the *j*-th diagonal element of a matrix.

Similarly, the least squares estimator for *σ*2 is also consistent and asymptotically normal (provided that the fourth moment of *εi* exists) with limiting distribution

$({\hat {\sigma }}^{2}-\sigma ^{2})\ {\xrightarrow {d}}\ {\mathcal {N}}\left(0,\;\operatorname {E} \left[\varepsilon _{i}^{4}\right]-\sigma ^{4}\right).$

These asymptotic distributions can be used for prediction, testing hypotheses, constructing other estimators, etc.. As an example consider the problem of prediction. Suppose $x_{0}$ is some point within the domain of distribution of the regressors, and one wants to know what the response variable would have been at that point. The mean response is the quantity $y_{0}=x_{0}^{\mathrm {T} }\beta$ , whereas the predicted response is ${\hat {y}}_{0}=x_{0}^{\mathrm {T} }{\hat {\beta }}$ . Clearly the predicted response is a random variable, its distribution can be derived from that of ${\hat {\beta }}$ :

$\left({\hat {y}}_{0}-y_{0}\right)\ {\xrightarrow {d}}\ {\mathcal {N}}\left(0,\;\sigma ^{2}x_{0}^{\mathrm {T} }Q_{xx}^{-1}x_{0}\right),$

which allows construct confidence intervals for mean response $y_{0}$ to be constructed:

$y_{0}\in \left[\ x_{0}^{\mathrm {T} }{\hat {\beta }}\pm q_{1-{\frac {\alpha }{2}}}^{{\mathcal {N}}(0,1)}\!{\sqrt {{\hat {\sigma }}^{2}x_{0}^{\mathrm {T} }Q_{xx}^{-1}x_{0}}}\ \right]$

at the

1 −

α

confidence level.

#### Hypothesis testing

Two hypothesis tests are particularly widely used. First, one wants to know if the estimated regression equation is any better than simply predicting that all values of the response variable equal its sample mean (if not, it is said to have no explanatory power). The null hypothesis of no explanatory value of the estimated regression is tested using an F-test. If the calculated F-value is found to be large enough to exceed its critical value for the pre-chosen level of significance, the null hypothesis is rejected and the alternative hypothesis, that the regression has explanatory power, is accepted. Otherwise, the null hypothesis of no explanatory power is accepted.

Second, for each explanatory variable of interest, one wants to know whether its estimated coefficient differs significantly from zero—that is, whether this particular explanatory variable in fact has explanatory power in predicting the response variable. Here the null hypothesis is that the true coefficient is zero. This hypothesis is tested by computing the coefficient's t-statistic, as the ratio of the coefficient estimate to its standard error. If the t-statistic is larger than a predetermined value, the null hypothesis is rejected and the variable is found to have explanatory power, with its coefficient significantly different from zero. Otherwise, the null hypothesis of a zero value of the true coefficient is accepted.

In addition, the Chow test is used to test whether two subsamples both have the same underlying true coefficient values. The sum of squared residuals of regressions on each of the subsets and on the combined data set are compared by computing an F-statistic; if this exceeds a critical value, the null hypothesis of no difference between the two subsets is rejected; otherwise, it is accepted.

### Violations of assumptions

#### Time series model

In a time series model, we require the stochastic process {*xi*, *yi*} to be stationary and ergodic; if {*xi*, *yi*} is nonstationary, OLS results are often biased unless {*xi*, *yi*} is co-integrating.

We still require the regressors to be *strictly exogenous*: E[*xiεi*] = 0 for all *i* = 1, ..., *n*. If they are only predetermined, OLS is biased in finite sample;

Finally, the assumptions on the variance take the form of requiring that {*xiεi*} is a martingale difference sequence, with a finite matrix of second moments *Q**xxε*² = E[ *εi*2*xi xi*T ].

#### Constrained estimation

Suppose it is known that the coefficients in the regression satisfy a system of linear equations

$A\colon \quad Q^{\operatorname {T} }\beta =c,\,$

where *Q* is a *p*×*q* matrix of full rank, and *c* is a *q*×1 vector of known constants, where *q < p*. In this case least squares estimation is equivalent to minimizing the sum of squared residuals of the model subject to the constraint *A*. The **constrained least squares (CLS)** estimator can be given by an explicit formula:

${\hat {\beta }}^{c}={\hat {\beta }}-(X^{\operatorname {T} }X)^{-1}Q{\Big (}Q^{\operatorname {T} }(X^{\operatorname {T} }X)^{-1}Q{\Big )}^{-1}(Q^{\operatorname {T} }{\hat {\beta }}-c).$

This expression for the constrained estimator is valid as long as the matrix *XTX* is invertible. It was assumed from the beginning of this article that this matrix is of full rank, and it was noted that when the rank condition fails, *β* will not be identifiable. However it may happen that adding the restriction *A* makes *β* identifiable, in which case one would like to find the formula for the estimator. The estimator is equal to

${\hat {\beta }}^{c}=R(R^{\operatorname {T} }X^{\operatorname {T} }XR)^{-1}R^{\operatorname {T} }X^{\operatorname {T} }y+{\Big (}I_{p}-R(R^{\operatorname {T} }X^{\operatorname {T} }XR)^{-1}R^{\operatorname {T} }X^{\operatorname {T} }X{\Big )}Q(Q^{\operatorname {T} }Q)^{-1}c,$

where *R* is a *p*×(*p* − *q*) matrix such that the matrix [*Q R*] is non-singular, and *RTQ* = 0. Such a matrix can always be found, although generally it is not unique. The second formula coincides with the first in case when *XTX* is invertible.
