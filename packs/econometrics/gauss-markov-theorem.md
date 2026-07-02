---
title: "Gauss–Markov theorem"
source: https://en.wikipedia.org/wiki/Gauss%E2%80%93Markov_theorem
domain: econometrics
license: CC-BY-SA-4.0
tags: econometrics, instrumental variables, panel data, gauss-markov theorem
fetched: 2026-07-02
---

# Gauss–Markov theorem

In statistics, the **Gauss–Markov theorem** (or simply **Gauss theorem** for some authors) states that the ordinary least squares (OLS) estimator has the lowest sampling variance (variance of the estimator across samples) within the class of linear unbiased estimators, if the errors in the linear regression model are uncorrelated, have equal variances and expectation value of zero. The errors do not need to be normal, nor do they need to be independent and identically distributed (only uncorrelated with mean zero and homoscedastic with finite variance). The requirement that the estimator be unbiased cannot be dropped, since biased estimators exist with lower variance. See, for example, the James–Stein estimator (which also drops linearity), ridge regression, or simply any degenerate estimator.

The theorem was named after Carl Friedrich Gauss and Andrey Markov, although Gauss' work significantly predates Markov's. But while Gauss derived the result under the assumption of independence and normality, Markov reduced the assumptions to the form stated above. A further generalization to non-spherical errors was given by Alexander Aitken.

## Scalar case statement

Suppose we are given two random variables $X,Y$ and that we want to find the best linear estimator of Y given X , using the best linear estimator ${\hat {Y}}=\alpha X+\mu ,$ where the parameters $\alpha$ and $\mu$ are both real numbers.

Such an estimator ${\hat {Y}}$ would have the same mean and standard deviation as Y , that is, $\mu _{\hat {Y}}=\mu _{Y},\sigma _{\hat {Y}}=\sigma _{Y}$ .

Therefore, if the vector X has respective mean and standard deviation $\mu _{x},\sigma _{x}$ , the best linear estimator would be ${\hat {Y}}=\sigma _{y}{\frac {(X-\mu _{x})}{\sigma _{x}}}+\mu _{y},$ since ${\hat {Y}}$ has the same mean and standard deviation as Y .

## Statement

Suppose we have, in matrix notation, the linear relationship $y=X\beta +\varepsilon ,\quad (y,\varepsilon \in \mathbb {R} ^{n},\beta \in \mathbb {R} ^{K}{\text{ and }}X\in \mathbb {R} ^{n\times K}),$ where $\beta _{j}$ are non-random but *un*observable parameters, $X_{ij}$ are non-random and observable (called the "explanatory variables"), $\varepsilon _{i}$ are random, and so $y_{i}$ are random. The random variables $\varepsilon _{i}$ are called the "disturbance", "noise" or simply "error" (will be contrasted with "residual" later in the article; see errors and residuals in statistics). Note that to include a constant in the model above, one can choose to introduce the constant as a variable $\beta _{K+1}$ with a newly introduced last column of X being unity i.e., $X_{i(K+1)}=1$ for all i . Note that though $y_{i}$ , as sample responses, are observable, the following statements and arguments including assumptions, proofs and the others assume under the *only* condition of knowing $X_{ij},$ *but not* $y_{i}.$

The ***Gauss–Markov assumptions*** concern the set of error random variables $\varepsilon _{i}$ :

- They have mean zero: $\operatorname {E} [\varepsilon _{i}]=0.$
- They are homoscedastic, that is, all have the same finite variance: $\operatorname {Var} (\varepsilon _{i})=\sigma ^{2}<\infty$ for all i .
- Distinct error terms are uncorrelated: $\operatorname {Cov} (\varepsilon _{i},\varepsilon _{j})=0,\forall i\neq j.$

A *linear estimator* of $\beta _{j}$ is a linear combination ${\widehat {\beta }}_{j}=c_{1j}y_{1}+\cdots +c_{nj}y_{n},$ in which the coefficients $c_{ij}$ are not allowed to depend on the underlying coefficients $\beta _{j}$ , since those are not observable, but are allowed to depend on the values $X_{ij}$ , since these data are observable. (The dependence of the coefficients on each $X_{ij}$ is typically nonlinear; the estimator is linear in each $y_{i}$ and hence in each random $\varepsilon ,$ which is why this is "linear" regression.) The estimator is said to be *unbiased* if and only if $\operatorname {E} [{\hat {\beta }}_{j}]=\beta _{j}$ regardless of the values of $X_{ij}$ . Now, let ${\textstyle \sum _{j=1}^{K}\lambda _{j}\beta _{j}}$ be some linear combination of the coefficients. Then the *mean squared error* of the corresponding estimation is $\operatorname {E} \left[\left(\sum _{j=1}^{K}\lambda _{j}({\hat {\beta }}_{j}-\beta _{j})\right)^{2}\right],$ in other words, it is the expectation of the square of the weighted sum (across parameters) of the differences between the estimators and the corresponding parameters to be estimated. (Since we are considering the case in which all the parameter estimates are unbiased, this mean squared error is the same as the variance of the linear combination.) The *best linear unbiased estimator* (BLUE) of the vector $\beta$ of parameters $\beta _{j}$ is one with the smallest mean squared error for every vector $\lambda$ of linear combination parameters. This is equivalent to the condition that $\operatorname {Var} ({\tilde {\beta }})-\operatorname {Var} ({\hat {\beta }})$ is a positive semi-definite matrix for every other linear unbiased estimator ${\widetilde {\beta }}$ .

The *ordinary least squares estimator* (OLS) is the function ${\widehat {\beta }}=(X^{\mathsf {T}}X)^{-1}X^{\mathsf {T}}y$ of y and X (where $X^{\mathsf {T}}$ denotes the transpose of X ) that minimizes the *sum of squares of residuals* (misprediction amounts): $\sum _{i=1}^{n}(y_{i}-{\hat {y}}_{i})^{2}=\sum _{i=1}^{n}\left(y_{i}-\sum _{j=1}^{K}{\hat {\beta }}_{j}X_{ij}\right)^{2}.$

The theorem now states that the OLS estimator is a best linear unbiased estimator (BLUE).

The main idea of the proof is that the least-squares estimator is uncorrelated with every linear unbiased estimator of zero, i.e., with every linear combination $a_{1}y_{1}+\cdots +a_{n}y_{n}$ whose coefficients do not depend upon the unobservable $\beta$ but whose expected value is always zero.

### Remark

Proof that the OLS indeed *minimizes* the sum of squares of residuals may proceed as follows with a calculation of the Hessian matrix and showing that it is positive definite.

The MSE function we want to minimize is $f(\beta _{0},\beta _{1},\dots ,\beta _{p})=\sum _{i=1}^{n}(y_{i}-\beta _{0}-\beta _{1}x_{i1}-\dots -\beta _{p}x_{ip})^{2}$ for a multiple regression model with *p* variables. The first derivative is ${\begin{aligned}{\frac {d}{d{\boldsymbol {\beta }}}}f&=-2X^{\operatorname {T} }\left(\mathbf {y} -X{\boldsymbol {\beta }}\right)\\&=-2{\begin{bmatrix}\sum _{i=1}^{n}(y_{i}-\dots -\beta _{p}x_{ip})\\\sum _{i=1}^{n}x_{i1}(y_{i}-\dots -\beta _{p}x_{ip})\\\vdots \\\sum _{i=1}^{n}x_{ip}(y_{i}-\dots -\beta _{p}x_{ip})\end{bmatrix}}\\&=\mathbf {0} _{p+1},\end{aligned}}$ where $X^{\operatorname {T} }$ is the design matrix $X={\begin{bmatrix}1&x_{11}&\cdots &x_{1p}\\1&x_{21}&\cdots &x_{2p}\\&&\vdots \\1&x_{n1}&\cdots &x_{np}\end{bmatrix}}\in \mathbb {R} ^{n\times (p+1)};\qquad n\geq p+1$

The Hessian matrix of second derivatives is ${\mathcal {H}}=2{\begin{bmatrix}n&\sum _{i=1}^{n}x_{i1}&\cdots &\sum _{i=1}^{n}x_{ip}\\\sum _{i=1}^{n}x_{i1}&\sum _{i=1}^{n}x_{i1}^{2}&\cdots &\sum _{i=1}^{n}x_{i1}x_{ip}\\\vdots &\vdots &\ddots &\vdots \\\sum _{i=1}^{n}x_{ip}&\sum _{i=1}^{n}x_{ip}x_{i1}&\cdots &\sum _{i=1}^{n}x_{ip}^{2}\end{bmatrix}}=2X^{\operatorname {T} }X$

Assuming the columns of X are linearly independent so that $X^{\operatorname {T} }X$ is invertible, let $X={\begin{bmatrix}\mathbf {v_{1}} &\mathbf {v_{2}} &\cdots &\mathbf {v} _{p+1}\end{bmatrix}}$ , then $k_{1}\mathbf {v_{1}} +\dots +k_{p+1}\mathbf {v} _{p+1}=\mathbf {0} \iff k_{1}=\dots =k_{p+1}=0$

Now let $\mathbf {k} =(k_{1},\dots ,k_{p+1})^{T}\in \mathbb {R} ^{(p+1)\times 1}$ be an eigenvector of ${\mathcal {H}}$ .

$\mathbf {k} \neq \mathbf {0} \implies \left(k_{1}\mathbf {v_{1}} +\dots +k_{p+1}\mathbf {v} _{p+1}\right)^{2}>0$

In terms of vector multiplication, this means ${\begin{bmatrix}k_{1}&\cdots &k_{p+1}\end{bmatrix}}{\begin{bmatrix}\mathbf {v_{1}} \\\vdots \\\mathbf {v} _{p+1}\end{bmatrix}}{\begin{bmatrix}\mathbf {v_{1}} &\cdots &\mathbf {v} _{p+1}\end{bmatrix}}{\begin{bmatrix}k_{1}\\\vdots \\k_{p+1}\end{bmatrix}}=\mathbf {k} ^{\operatorname {T} }{\mathcal {H}}\mathbf {k} =\lambda \mathbf {k} ^{\operatorname {T} }\mathbf {k} >0$ where $\lambda$ is the eigenvalue corresponding to $\mathbf {k}$ . Moreover, $\mathbf {k} ^{\operatorname {T} }\mathbf {k} =\sum _{i=1}^{p+1}k_{i}^{2}>0\implies \lambda >0$

Finally, as eigenvector $\mathbf {k}$ was arbitrary, it means all eigenvalues of ${\mathcal {H}}$ are positive, therefore ${\mathcal {H}}$ is positive definite. Thus, ${\boldsymbol {\beta }}=\left(X^{\operatorname {T} }X\right)^{-1}X^{\operatorname {T} }Y$ is indeed a global minimum.

Or, just see that for all vectors $\mathbf {v} ,\mathbf {v} ^{\operatorname {T} }X^{\operatorname {T} }X\mathbf {v} =\|\mathbf {X} \mathbf {v} \|^{2}\geq 0$ . So the Hessian is positive definite if full rank.

## Proof

Let ${\tilde {\beta }}=Cy$ be another linear estimator of $\beta$ with $C=(X^{\operatorname {T} }X)^{-1}X^{\operatorname {T} }+D$ where D is a $K\times n$ non-zero matrix. As we're restricting to *unbiased* estimators, minimum mean squared error implies minimum variance. The goal is therefore to show that such an estimator has a variance no smaller than that of ${\widehat {\beta }},$ the OLS estimator. We calculate:

${\begin{aligned}\operatorname {E} \left[{\tilde {\beta }}\right]&=\operatorname {E} [Cy]\\&=\operatorname {E} \left[\left((X^{\operatorname {T} }X)^{-1}X^{\operatorname {T} }+D\right)(X\beta +\varepsilon )\right]\\&=\left((X^{\operatorname {T} }X)^{-1}X^{\operatorname {T} }+D\right)X\beta +\left((X^{\operatorname {T} }X)^{-1}X^{\operatorname {T} }+D\right)\operatorname {E} [\varepsilon ]\\&=\left((X^{\operatorname {T} }X)^{-1}X^{\operatorname {T} }+D\right)X\beta &&\operatorname {E} [\varepsilon ]=0\\&=(X^{\operatorname {T} }X)^{-1}X^{\operatorname {T} }X\beta +DX\beta \\&=(I_{K}+DX)\beta .\\\end{aligned}}$

Therefore, since $\beta$ is **un**observable, ${\tilde {\beta }}$ is unbiased if and only if $DX=0$ . Then:

${\begin{aligned}\operatorname {Var} \left({\tilde {\beta }}\right)&=\operatorname {Var} (Cy)\\&=C{\text{ Var}}(y)C^{\operatorname {T} }\\&=\sigma ^{2}CC^{\operatorname {T} }\\&=\sigma ^{2}\left((X^{\operatorname {T} }X)^{-1}X^{\operatorname {T} }+D\right)\left(X(X^{\operatorname {T} }X)^{-1}+D^{\operatorname {T} }\right)\\&=\sigma ^{2}\left((X^{\operatorname {T} }X)^{-1}X^{\operatorname {T} }X(X^{\operatorname {T} }X)^{-1}+(X^{\operatorname {T} }X)^{-1}X^{\operatorname {T} }D^{\operatorname {T} }+DX(X^{\operatorname {T} }X)^{-1}+DD^{\operatorname {T} }\right)\\&=\sigma ^{2}(X^{\operatorname {T} }X)^{-1}+\sigma ^{2}(X^{\operatorname {T} }X)^{-1}(DX)^{\operatorname {T} }+\sigma ^{2}DX(X^{\operatorname {T} }X)^{-1}+\sigma ^{2}DD^{\operatorname {T} }\\&=\sigma ^{2}(X^{\operatorname {T} }X)^{-1}+\sigma ^{2}DD^{\operatorname {T} }&&DX=0\\&=\operatorname {Var} \left({\widehat {\beta }}\right)+\sigma ^{2}DD^{\operatorname {T} }&&\sigma ^{2}(X^{\operatorname {T} }X)^{-1}=\operatorname {Var} \left({\widehat {\beta }}\right)\end{aligned}}$

Since $DD^{\operatorname {T} }$ is a positive semidefinite matrix, $\operatorname {Var} \left({\tilde {\beta }}\right)$ exceeds $\operatorname {Var} \left({\widehat {\beta }}\right)$ by a positive semidefinite matrix.

### Remarks on the proof

As it has been stated before, the condition of $\operatorname {Var} \left({\tilde {\beta }}\right)-\operatorname {Var} \left({\widehat {\beta }}\right)$ is a positive semidefinite matrix is equivalent to the property that the best linear unbiased estimator of $\ell ^{\operatorname {T} }\beta$ is $\ell ^{\operatorname {T} }{\widehat {\beta }}$ (best in the sense that it has minimum variance). To see this, let $\ell ^{\operatorname {T} }{\tilde {\beta }}$ another linear unbiased estimator of $\ell ^{\operatorname {T} }\beta$ .

${\begin{aligned}\operatorname {Var} \left(\ell ^{\operatorname {T} }{\tilde {\beta }}\right)&=\ell ^{\operatorname {T} }\operatorname {Var} \left({\tilde {\beta }}\right)\ell \\&=\sigma ^{2}\ell ^{\operatorname {T} }(X^{\operatorname {T} }X)^{-1}\ell +\ell ^{\operatorname {T} }DD^{\operatorname {T} }\ell \\&=\operatorname {Var} \left(\ell ^{\operatorname {T} }{\widehat {\beta }}\right)+(D^{\operatorname {T} }\ell )^{\operatorname {T} }(D^{\operatorname {T} }\ell )\\&\geq \operatorname {Var} \left(\ell ^{\operatorname {T} }{\widehat {\beta }}\right)\end{aligned}}$

Moreover, equality holds if and only if $D^{\operatorname {T} }\ell =0$ . We calculate

${\begin{aligned}\ell ^{\operatorname {T} }{\tilde {\beta }}&=\ell ^{\operatorname {T} }\left(((X^{\operatorname {T} }X)^{-1}X^{\operatorname {T} }+D)Y\right)&&{\text{ from above}}\\&=\ell ^{\operatorname {T} }(X^{\operatorname {T} }X)^{-1}X^{\operatorname {T} }Y+\ell ^{\operatorname {T} }DY\\&=\ell ^{\operatorname {T} }{\widehat {\beta }}+(D^{\operatorname {T} }\ell )^{\operatorname {T} }Y\\&=\ell ^{\operatorname {T} }{\widehat {\beta }}&&D^{\operatorname {T} }\ell =0\end{aligned}}$

This proves that the equality holds if and only if $\ell ^{\operatorname {T} }{\tilde {\beta }}=\ell ^{\operatorname {T} }{\widehat {\beta }}$ which gives the uniqueness of the OLS estimator as a BLUE.

## Generalized least squares estimator

The generalized least squares (GLS), developed by Aitken, extends the Gauss–Markov theorem to the case where the error vector has a non-scalar covariance matrix. The Aitken estimator is also a BLUE.

## Gauss–Markov theorem as stated in econometrics

In most treatments of OLS, the regressors (parameters of interest) in the design matrix $\mathbf {X}$ are assumed to be fixed in repeated samples. This assumption is considered inappropriate for a predominantly nonexperimental science like econometrics. Instead, the assumptions of the Gauss–Markov theorem are stated conditional on $\mathbf {X}$ .

### Linearity

The dependent variable is assumed to be a linear function of the variables specified in the model. The specification must be linear in its parameters. This does not mean that there must be a linear relationship between the independent and dependent variables. The independent variables can take non-linear forms as long as the parameters are linear. The equation $y=\beta _{0}+\beta _{1}x^{2},$ qualifies as linear while $y=\beta _{0}+\beta _{1}^{2}x$ can be transformed to be linear by replacing $\beta _{1}^{2}$ by another parameter, say $\gamma$ . An equation with a parameter dependent on an independent variable does not qualify as linear, for example $y=\beta _{0}+\beta _{1}(x)\cdot x$ , where $\beta _{1}(x)$ is a function of x .

Data transformations are often used to convert an equation into a linear form. For example, the Cobb–Douglas function—often used in economics—is nonlinear:

$Y=AL^{\alpha }K^{1-\alpha }e^{\varepsilon }$

But it can be expressed in linear form by taking the natural logarithm of both sides:

$\ln Y=\ln A+\alpha \ln L+(1-\alpha )\ln K+\varepsilon =\beta _{0}+\beta _{1}\ln L+\beta _{2}\ln K+\varepsilon$

This assumption also covers specification issues: assuming that the proper functional form has been selected and there are no omitted variables.

One should be aware, however, that the parameters that minimize the residuals of the transformed equation do not necessarily minimize the residuals of the original equation.

### Strict exogeneity

For all n observations, the expectation—conditional on the regressors—of the error term is zero:

$\operatorname {E} [\,\varepsilon _{i}\mid \mathbf {X} ]=\operatorname {E} [\,\varepsilon _{i}\mid \mathbf {x} _{1},\dots ,\mathbf {x} _{n}]=0.$

where $\mathbf {x} _{i}={\begin{bmatrix}x_{i1}&x_{i2}&\cdots &x_{ik}\end{bmatrix}}^{\operatorname {T} }$ is the data vector of regressors for the *i*th observation, and consequently $\mathbf {X} ={\begin{bmatrix}\mathbf {x} _{1}^{\operatorname {T} }&\mathbf {x} _{2}^{\operatorname {T} }&\cdots &\mathbf {x} _{n}^{\operatorname {T} }\end{bmatrix}}^{\operatorname {T} }$ is the data matrix or design matrix.

Geometrically, this assumption implies that $\mathbf {x} _{i}$ and $\varepsilon _{i}$ are orthogonal to each other, so that their inner product (i.e., their cross moment) is zero.

$\operatorname {E} [\,\mathbf {x} _{j}\cdot \varepsilon _{i}\,]={\begin{bmatrix}\operatorname {E} [\,{x}_{j1}\cdot \varepsilon _{i}\,]\\\operatorname {E} [\,{x}_{j2}\cdot \varepsilon _{i}\,]\\\vdots \\\operatorname {E} [\,{x}_{jk}\cdot \varepsilon _{i}\,]\end{bmatrix}}=\mathbf {0} \quad {\text{for all }}i,j\in n$

This assumption is violated if the explanatory variables are measured with error, or are endogenous. Endogeneity can be the result of simultaneity, where causality flows back and forth between both the dependent and independent variable. Instrumental variable techniques are commonly used to address this problem.

### Full rank

The sample data matrix $\mathbf {X}$ must have full column rank.

$\operatorname {rank} (\mathbf {X} )=k$

Otherwise $\mathbf {X} ^{\operatorname {T} }\mathbf {X}$ is not invertible and the OLS estimator cannot be computed.

A violation of this assumption is perfect multicollinearity, i.e. some explanatory variables are linearly dependent. One scenario in which this will occur is called "dummy variable trap," when a base dummy variable is not omitted resulting in perfect correlation between the dummy variables and the constant term.

Multicollinearity (as long as it is not "perfect") can be present resulting in a less efficient, but still unbiased estimate. The estimates will be less precise and highly sensitive to particular sets of data. Multicollinearity can be detected from condition number or the variance inflation factor, among other tests.

### Spherical errors

The outer product of the error vector must be spherical.

$\operatorname {E} [\,{\boldsymbol {\varepsilon }}{\boldsymbol {\varepsilon }}^{\operatorname {T} }\mid \mathbf {X} ]=\operatorname {Var} [\,{\boldsymbol {\varepsilon }}\mid \mathbf {X} ]={\begin{bmatrix}\sigma ^{2}&0&\cdots &0\\0&\sigma ^{2}&\cdots &0\\\vdots &\vdots &\ddots &\vdots \\0&0&\cdots &\sigma ^{2}\end{bmatrix}}=\sigma ^{2}\mathbf {I} \quad {\text{with }}\sigma ^{2}>0$

This implies the error term has uniform variance (homoscedasticity) and no serial correlation. If this assumption is violated, OLS is still unbiased, but inefficient. The term "spherical errors" will describe the multivariate normal distribution: if $\operatorname {Var} [\,{\boldsymbol {\varepsilon }}\mid \mathbf {X} ]=\sigma ^{2}\mathbf {I}$ in the multivariate normal density, then the equation $f(\varepsilon )=c$ is the formula for a ball centered at μ with radius σ in n-dimensional space.

Heteroskedasticity occurs when the amount of error is correlated with an independent variable. For example, in a regression on food expenditure and income, the error is correlated with income. Low income people generally spend a similar amount on food, while high income people may spend a very large amount or as little as low income people spend. Heteroskedastic can also be caused by changes in measurement practices. For example, as statistical offices improve their data, measurement error decreases, so the error term declines over time.

This assumption is violated when there is autocorrelation. Autocorrelation can be visualized on a data plot when a given observation is more likely to lie above a fitted line if adjacent observations also lie above the fitted regression line. Autocorrelation is common in time series data where a data series may experience "inertia." If a dependent variable takes a while to fully absorb a shock. Spatial autocorrelation can also occur geographic areas are likely to have similar errors. Autocorrelation may be the result of misspecification such as choosing the wrong functional form. In these cases, correcting the specification is one possible way to deal with autocorrelation.

When the spherical errors assumption may be violated, the generalized least squares estimator can be shown to be BLUE.
