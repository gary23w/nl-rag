---
title: "Local regression"
source: https://en.wikipedia.org/wiki/Local_regression
domain: scatter-bubble-charts
license: CC-BY-SA-4.0
tags: scatter plot, bubble chart, scatterplot smoothing, local regression
fetched: 2026-07-02
---

# Local regression

**Local regression** or **local polynomial regression**, also known as **moving regression**, is a generalization of the moving average and polynomial regression. Its most common methods, initially developed for scatterplot smoothing, are **LOESS** (**locally estimated scatterplot smoothing**) and **LOWESS** (**locally weighted scatterplot smoothing**), both pronounced /ˈloʊɛs/ *LOH-ess*. They are two strongly related non-parametric regression methods that combine multiple regression models in a *k*-nearest-neighbor-based meta-model. In some fields, LOESS is known and commonly referred to as Savitzky–Golay filter (proposed 15 years before LOESS).

LOESS and LOWESS thus build on "classical" methods, such as linear and nonlinear least squares regression. They address situations in which the classical procedures do not perform well or cannot be effectively applied without undue labor. LOESS combines much of the simplicity of linear least squares regression with the flexibility of nonlinear regression. It does this by fitting simple models to localized subsets of the data to build up a function that describes the deterministic part of the variation in the data, point by point. In fact, one of the chief attractions of this method is that the data analyst is not required to specify a global function of any form to fit a model to the data, only to fit segments of the data.

The trade-off for these features is increased computation. Because it is so computationally intensive, LOESS would have been practically impossible to use in the era when least squares regression was being developed. Most other modern methods for process modelling are similar to LOESS in this respect. These methods have been consciously designed to use our current computational ability to the fullest possible advantage to achieve goals not easily achieved by traditional approaches.

A smooth curve through a set of data points obtained with this statistical technique is called a *loess curve*, particularly when each smoothed value is given by a weighted quadratic least squares regression over the span of values of the *y*-axis scattergram criterion variable. When each smoothed value is given by a weighted linear least squares regression over the span, this is known as a *lowess curve.* However, some authorities treat *lowess* and loess as synonyms.

## History

Local regression and closely related procedures have a long and rich history, having been discovered and rediscovered in different fields on multiple occasions. An early work by Robert Henderson studying the problem of graduation (a term for smoothing used in Actuarial literature) introduced local regression using cubic polynomials.

Specifically, let $Y_{j}$ denote an ungraduated sequence of observations. Following Henderson, suppose that only the terms from $Y_{-h}$ to $Y_{h}$ are to be taken into account when computing the graduated value of $Y_{0}$ , and $W_{j}$ is the weight to be assigned to $Y_{j}$ . Henderson then uses a local polynomial approximation $a+bj+cj^{2}+dj^{3}$ , and sets up the following four equations for the coefficients:

${\begin{aligned}\sum _{j=-h}^{h}(a+bj+cj^{2}+dj^{3})W_{j}&=\sum _{j=-h}^{h}W_{j}Y_{j}\\\sum _{j=-h}^{h}(aj+bj^{2}+cj^{3}+dj^{4})W_{j}&=\sum _{j=-h}^{h}jW_{j}Y_{j}\\\sum _{j=-h}^{h}(aj^{2}+bj^{3}+cj^{4}+dj^{5})W_{j}&=\sum _{j=-h}^{h}j^{2}W_{j}Y_{j}\\\sum _{j=-h}^{h}(aj^{3}+bj^{4}+cj^{5}+dj^{6})W_{j}&=\sum _{j=-h}^{h}j^{3}W_{j}Y_{j}\end{aligned}}$

Solving these equations for the polynomial coefficients yields the graduated value, ${\hat {Y}}_{0}=a$ .

Henderson went further. In preceding years, many 'summation formula' methods of graduation had been developed, which derived graduation rules based on summation formulae (convolution of the series of observations with a chosen set of weights). Two such rules are the 15-point and 21-point rules of Spencer (1904). These graduation rules were carefully designed to have a quadratic-reproducing property: If the ungraduated values exactly follow a quadratic formula, then the graduated values equal the ungraduated values. This is an important property: a simple moving average, by contrast, cannot adequately model peaks and troughs in the data. Henderson's insight was to show that *any* such graduation rule can be represented as a local cubic (or quadratic) fit for an appropriate choice of weights.

Further discussions of the historical work on graduation and local polynomial fitting can be found in Macaulay (1931), Cleveland and Loader (1995); and Murray and Bellhouse (2019).

The Savitzky-Golay filter, introduced by Abraham Savitzky and Marcel J. E. Golay (1964) significantly expanded the method. Like the earlier graduation work, their focus was data with an equally-spaced predictor variable, where (excluding boundary effects) local regression can be represented as a convolution. Savitzky and Golay published extensive sets of convolution coefficients for different orders of polynomial and smoothing window widths.

Local regression methods started to appear extensively in statistics literature in the 1970s; for example, Charles J. Stone (1977), Vladimir Katkovnik (1979) and William S. Cleveland (1979). Katkovnik (1985) is the earliest book devoted primarily to local regression methods.

Theoretical work continued to appear throughout the 1990s. Important contributions include Jianqing Fan and Irène Gijbels (1992) studying efficiency properties, and David Ruppert and Matthew P. Wand (1994) developing an asymptotic distribution theory for multivariate local regression.

An important extension of local regression is Local Likelihood Estimation, formulated by Robert Tibshirani and Trevor Hastie (1987). This replaces the local least-squares criterion with a likelihood-based criterion, thereby extending the local regression method to the Generalized linear model setting; for example binary data, count data or censored data.

Practical implementations of local regression began appearing in statistical software in the 1980s. Cleveland (1981) introduces the LOWESS routines, intended for smoothing scatterplots. This implements local linear fitting with a single predictor variable, and also introduces robustness downweighting to make the procedure resistant to outliers. An entirely new implementation, LOESS, is described in Cleveland and Susan J. Devlin (1988). LOESS is a multivariate smoother, able to handle spatial data with two (or more) predictor variables, and uses (by default) local quadratic fitting. Both LOWESS and LOESS are implemented in the S and R programming languages. See also Cleveland's Local Fitting Software.

While Local Regression, LOWESS and LOESS are sometimes used interchangeably, this usage should be considered incorrect. Local Regression is a general term for the fitting procedure; LOWESS and LOESS are two distinct implementations.

## Model definition

Local regression uses a data set consisting of observations one or more ‘independent’ or ‘predictor’ variables, and a ‘dependent’ or ‘response’ variable. The dataset will consist of a number n observations. The observations of the predictor variable can be denoted $x_{1},\ldots ,x_{n}$ , and corresponding observations of the response variable by $Y_{1},\ldots ,Y_{n}$ .

For ease of presentation, the development below assumes a single predictor variable; the extension to multiple predictors (when the $x_{i}$ are vectors) is conceptually straightforward. A functional relationship between the predictor and response variables is assumed: $Y_{i}=\mu (x_{i})+\epsilon _{i}$ where $\mu (x)$ is the unknown ‘smooth’ regression function to be estimated, and represents the conditional expectation of the response, given a value of the predictor variables. In theoretical work, the ‘smoothness’ of this function can be formally characterized by placing bounds on higher order derivatives. The $\epsilon _{i}$ represents random error; for estimation purposes these are assumed to have mean zero. Stronger assumptions (e.g., independence and equal variance) may be made when assessing properties of the estimates.

Local regression then estimates the function $\mu (x)$ , for one value of x at a time. Since the function is assumed to be smooth, the most informative data points are those whose $x_{i}$ values are close to x . This is formalized with a bandwidth h and a kernel or weight function $W(\cdot )$ , with observations assigned weights $w_{i}(x)=W{\left({\frac {x_{i}-x}{h}}\right)}.$ A typical choice of W , used by Cleveland in LOWESS, is $W(u)=(1-|u|^{3})^{3}$ for $|u|<1$ , although any similar function (peaked at $u=0$ and small or 0 for large values of u ) can be used. Questions of bandwidth selection and specification (how large should h be, and should it vary depending upon the fitting point x ?) are deferred for now.

A local model (usually a low-order polynomial with degree $p\leq 3$ ), expressed as $\mu (x_{i})\approx \beta _{0}+\beta _{1}(x_{i}-x)+\ldots +\beta _{p}(x_{i}-x)^{p}$ is then fitted by weighted least squares: choose regression coefficients $({\hat {\beta }}_{0},\ldots ,{\hat {\beta }}_{p})$ to minimize $\sum _{i=1}^{n}w_{i}(x)\left(Y_{i}-\beta _{0}-\beta _{1}(x_{i}-x)-\ldots -\beta _{p}(x_{i}-x)^{p}\right)^{2}.$ The local regression estimate of $\mu (x)$ is then simply the intercept estimate: ${\hat {\mu }}(x)={\hat {\beta }}_{0}$ while the remaining coefficients can be interpreted (up to a factor of $p!$ ) as derivative estimates.

It is to be emphasized that the above procedure produces the estimate ${\hat {\mu }}(x)$ for one value of x . When considering a new value of x , a new set of weights $w_{i}(x)$ must be computed, and the regression coefficient estimated afresh.

### Matrix representation of the local regression estimate

As with all least squares estimates, the estimated regression coefficients can be expressed in closed form (see Weighted least squares for details): ${\hat {\boldsymbol {\beta }}}=\left(\mathbf {X^{\textsf {T}}WX} \right)^{-1}\mathbf {X^{\textsf {T}}W} \mathbf {y}$ where ${\hat {\boldsymbol {\beta }}}$ is a vector of the local regression coefficients; $\mathbf {X}$ is the $n\times (p+1)$ design matrix with entries $(x_{i}-x)^{j}$ ; $\mathbf {W}$ is a diagonal matrix of the smoothing weights $w_{i}(x)$ ; and $\mathbf {y}$ is a vector of the responses $Y_{i}$ .

This matrix representation is crucial for studying the theoretical properties of local regression estimates. With appropriate definitions of the design and weight matrices, it immediately generalizes to the multiple-predictor setting.

## Selection issues: bandwidth, local model, fitting criteria

Implementation of local regression requires specification and selection of several components:

1. The bandwidth, and more generally the localized subsets of the data.
2. The degree of local polynomial, or more generally, the form of the local model.
3. The choice of weight function $W(\cdot )$ .
4. The choice of fitting criterion (least squares or something else).

Each of these components has been the subject of extensive study; a summary is provided below.

### Localized subsets of data; Bandwidth

The bandwidth h controls the resolution of the local regression estimate. If *h* is too small, the estimate may show high-resolution features that represent noise in the data, rather than any real structure in the mean function. Conversely, if *h* is too large, the estimate will only show low-resolution features, and important structure may be lost. This is the *bias-variance tradeoff*; if *h* is too small, the estimate exhibits large variation; while at large *h*, the estimate exhibits large bias.

Careful choice of bandwidth is therefore crucial when applying local regression. Mathematical methods for bandwidth selection require, firstly, formal criteria to assess the performance of an estimate. One such criterion is prediction error: if a new observation is made at ${\tilde {x}}$ , how well does the estimate ${\hat {\mu }}({\tilde {x}})$ predict the new response ${\tilde {Y}}$ ?

Performance is often assessed using a squared-error loss function. The mean squared prediction error is ${\begin{aligned}\operatorname {E} \left[{\tilde {Y}}-{\hat {\mu }}({\tilde {x}})\right]^{2}&=\operatorname {E} \left[{\tilde {Y}}-\mu (x)+\mu (x)-{\hat {\mu }}({\tilde {x}})\right]^{2}\\&=\operatorname {E} \left[{\tilde {Y}}-\mu (x)\right]^{2}+\operatorname {E} \left[\mu (x)-{\hat {\mu }}({\tilde {x}})\right]^{2}.\end{aligned}}$ The first term $E\left({\tilde {Y}}-\mu (x)\right)^{2}$ is the random variation of the observation; this is entirely independent of the local regression estimate. The second term, $\operatorname {E} \left[\mu (x)-{\hat {\mu }}({\tilde {x}})\right]^{2}$ is the mean squared estimation error. This relation shows that, for squared error loss, minimizing prediction error and estimation error are equivalent problems.

In global bandwidth selection, these measures can be integrated over the x space ("mean integrated squared error", often used in theoretical work), or averaged over the actual $x_{i}$ (more useful for practical implementations). Some standard techniques from model selection can be readily adapted to local regression:

1. Cross Validation, which estimates the mean-squared prediction error.
2. Mallow's Cp and Akaike's Information Criterion, which estimate mean squared estimation error.
3. Other methods which attempt to estimate bias and variance variance components of the estimation error directly.

Any of these criteria can be minimized to produce an automatic bandwidth selector. Cleveland and Devlin prefer a graphical method (the *M*-plot) to visually display the bias-variance trade-off and guide bandwidth choice.

One question not addressed above is, how should the bandwidth depend upon the fitting point x ? Often a constant bandwidth is used, while LOWESS and LOESS prefer a nearest-neighbor bandwidth, meaning *h* is smaller in regions with many data points. Formally, the smoothing parameter, $\alpha$ , is the fraction of the total number *n* of data points that are used in each local fit. The subset of data used in each weighted least squares fit thus comprises the $n\alpha$ points (rounded to the next largest integer) whose explanatory variables' values are closest to the point at which the response is being estimated.

More sophisticated methods attempt to choose the bandwidth *adaptively*; that is, choose a bandwidth at each fitting point x by applying criteria such as cross-validation locally within the smoothing window. An early example of this is Jerome H. Friedman's "supersmoother", which uses cross-validation to choose among local linear fits at different bandwidths.

### Degree of local polynomials

Most sources, in both theoretical and computational work, use low-order polynomials as the local model, with polynomial degree ranging from 0 to 3.

The degree 0 (local constant) model is equivalent to a kernel smoother; usually credited to Èlizbar Nadaraya (1964) and G. S. Watson (1964). This is the simplest model to use, but can suffer from bias when fitting near boundaries of the dataset.

Local linear (degree 1) fitting can substantially reduce the boundary bias.

Local quadratic (degree 2) and local cubic (degree 3) can result in improved fits, particularly when the underlying mean function $\mu (x)$ has substantial curvature, or equivalently a large second derivative.

In theory, higher orders of polynomial can lead to faster convergence of the estimate ${\hat {\mu }}(x)$ to the true mean $\mu (x)$ , *provided that $\mu (x)$ has a sufficient number of derivatives*. See C. J. Stone (1980). Generally, it takes a large sample size for this faster convergence to be realized. There are also computational and stability issues that arise, particularly for multivariate smoothing. It is generally not recommended to use local polynomials with degree greater than 3.

As with bandwidth selection, methods such as cross-validation can be used to compare the fits obtained with different degrees of polynomial.

### Weight function

As mentioned above, the weight function gives the most weight to the data points nearest the point of estimation and the least weight to the data points that are furthest away. The use of the weights is based on the idea that points near each other in the explanatory variable space are more likely to be related to each other in a simple way than points that are further apart. Following this logic, points that are likely to follow the local model best influence the local model parameter estimates the most. Points that are less likely to actually conform to the local model have less influence on the local model parameter estimates.

Cleveland (1979) sets out four requirements for the weight function:

1. Non-negative: $W(x)>0$ for $|x|<1$ .
2. Symmetry: $W(-x)=W(x)$ .
3. Monotone: $W(x)$ is a nonincreasing function for $x\geq 0$ .
4. Bounded support: $W(x)=0$ for $|x|\geq 1$ .

Asymptotic efficiency of weight functions has been considered by V. A. Epanechnikov (1969) in the context of kernel density estimation; J. Fan (1993) has derived similar results for local regression. They conclude that the quadratic kernel, $W(x)=1-x^{2}$ for $|x|\leq 1$ has greatest efficiency under a mean-squared-error loss function. See "kernel functions in common use" for more discussion of different kernels and their efficiencies.

Considerations other than MSE are also relevant to the choice of weight function. Smoothness properties of $W(x)$ directly affect smoothness of the estimate ${\hat {\mu }}(x)$ . In particular, the quadratic kernel is not differentiable at $x=\pm 1$ , and ${\hat {\mu }}(x)$ is not differentiable as a result. The tri-cube weight function, $W(x)=(1-|x|^{3})^{3};|x|<1$ has been used in LOWESS and other local regression software; this combines higher-order differentiability with a high MSE efficiency.

One criticism of weight functions with bounded support is that they can lead to numerical problems (i.e. an unstable or singular design matrix) when fitting in regions with sparse data. For this reason, some authors choose to use the Gaussian kernel, or others with unbounded support.

### Choice of fitting criterion

As described above, local regression uses a locally weighted least squares criterion to estimate the regression parameters. This inherits many of the advantages (ease of implementation and interpretation; good properties when errors are normally distributed) and disadvantages (sensitivity to extreme values and outliers; inefficiency when errors have unequal variance or are not normally distributed) usually associated with least squares regression.

These disadvantages can be addressed by replacing the local least-squares estimation by something else. Two such ideas are presented here: local likelihood estimation, which applies local estimation to the generalized linear model, and robust local regression, which localizes methods from robust regression.

#### Local likelihood estimation

In local likelihood estimation, developed in Tibshirani and Hastie (1987), the observations $Y_{i}$ are assumed to come from a parametric family of distributions, with a known probability density function (or mass function, for discrete data), $Y_{i}\sim f(y,\theta (x_{i})),$ where the parameter function $\theta (x)$ is the unknown quantity to be estimated. To estimate $\theta (x)$ at a particular point x , the local likelihood criterion is $\sum _{i=1}^{n}w_{i}(x)\log \left[f{\left(Y_{i},\beta _{0}+\beta _{1}(x_{i}-x)+\dots +\beta _{p}\left(x_{i}-x\right)^{p}\right)}\right].$ Estimates of the regression coefficients (in, particular, ${\hat {\beta }}_{0}$ ) are obtained by maximizing the local likelihood criterion, and the local likelihood estimate is ${\hat {\theta }}(x)={\hat {\beta }}_{0}.$

When $f(y,\theta (x))$ is the normal distribution and $\theta (x)$ is the mean function, the local likelihood method reduces to the standard local least-squares regression. For other likelihood families, there is (usually) no closed-form solution for the local likelihood estimate, and iterative procedures such as iteratively reweighted least squares must be used to compute the estimate.

*Example* (local logistic regression). All response observations are 0 or 1, and the mean function is the "success" probability, $\mu (x_{i})=\Pr(Y_{i}=1|x_{i})$ . Since $\mu (x_{i})$ must be between 0 and 1, a local polynomial model should not be used for $\mu (x)$ directly. Insead, the logistic transformation $\theta (x)=\log \left({\frac {\mu (x)}{1-\mu (x)}}\right)$ can be used; equivalently, ${\begin{aligned}1-\mu (x)&={\frac {1}{1+e^{\theta (x)}}};\\\mu (x)&={\frac {e^{\theta (x)}}{1+e^{\theta (x)}}}\end{aligned}}$ and the mass function is $f(Y_{i},\theta (x_{i}))={\frac {e^{Y_{i}\theta (x_{i})}}{1+e^{\theta (x_{i})}}}.$

An asymptotic theory for local likelihood estimation is developed in J. Fan, Nancy E. Heckman and M.P.Wand (1995); the book Loader (1999) discusses many more applications of local likelihood.

#### Robust local regression

To address the sensitivity to outliers, techniques from robust regression can be employed. In local M-estimation, the local least-squares criterion is replaced by a criterion of the form $\sum _{i=1}^{n}w_{i}(x)\,\rho {\left({\frac {Y_{i}-\beta _{0}-\dots -\beta _{p}(x_{i}-x)^{p}}{s}}\right)}$ where $\rho (\cdot )$ is a robustness function and s is a scale parameter. Discussion of the merits of different choices of robustness function is best left to the robust regression literature. The scale parameter s must also be estimated. References for local M-estimation include Katkovnik (1985) and Alexandre Tsybakov (1986).

The robustness iterations in LOWESS and LOESS correspond to the robustness function defined by $\rho '(u)=u(1-u^{2}/6)^{2};|u|<1$ and a robust global estimate of the scale parameter.

If $\rho (u)=|u|$ , the local $L_{1}$ criterion $\sum _{i=1}^{n}w_{i}(x)\left|Y_{i}-\beta _{0}-\ldots -\beta _{p}(x_{i}-x)^{p}\right|$ results; this does not require a scale parameter. When $p=0$ , this criterion is minimized by a locally weighted median; local $L_{1}$ regression can be interpreted as estimating the *median*, rather than *mean*, response. If the loss function is skewed, this becomes local quantile regression. See Keming Yu and M.C. Jones (1998).

A recent alternative is to modify the local regression weights rather than the loss function. Shulman (2025) proposes *robust local polynomial regression with similarity kernels*, in which the kernel weighting is generalized to incorporate both predictor and response variables; in one version, the local least-squares criterion is reweighted by an estimate of the conditional density ${\hat {f}}_{Y\mid X}(Y_{i}\mid X_{i})$ , so that observations with low estimated local conditional density are downweighted. This provides robustness to outliers and high-leverage points without the multiple robustness iterations used in methods such as LOWESS and LOESS.

## Advantages

As discussed above, the biggest advantage LOESS has over many other methods is the process of fitting a model to the sample data does not begin with the specification of a function. Instead the analyst only has to provide a smoothing parameter value and the degree of the local polynomial. In addition, LOESS is very flexible, making it ideal for modeling complex processes for which no theoretical models exist. These two advantages, combined with the simplicity of the method, make LOESS one of the most attractive of the modern regression methods for applications that fit the general framework of least squares regression but which have a complex deterministic structure.

Although it is less obvious than for some of the other methods related to linear least squares regression, LOESS also accrues most of the benefits typically shared by those procedures. The most important of those is the theory for computing uncertainties for prediction and calibration. Many other tests and procedures used for validation of least squares models can also be extended to LOESS models .

## Disadvantages

LOESS makes less efficient use of data than other least squares methods. It requires fairly large, densely sampled data sets in order to produce good models. This is because LOESS relies on the local data structure when performing the local fitting. Thus, LOESS provides less complex data analysis in exchange for greater experimental costs.

Another disadvantage of LOESS is the fact that it does not produce a regression function that is easily represented by a mathematical formula. This can make it difficult to transfer the results of an analysis to other people. In order to transfer the regression function to another person, they would need the data set and software for LOESS calculations. In nonlinear regression, on the other hand, it is only necessary to write down a functional form in order to provide estimates of the unknown parameters and the estimated uncertainty. Depending on the application, this could be either a major or a minor drawback to using LOESS. In particular, the simple form of LOESS can not be used for mechanistic modelling where fitted parameters specify particular physical properties of a system.

Finally, as discussed above, LOESS is a computationally intensive method (with the exception of evenly spaced data, where the regression can then be phrased as a non-causal finite impulse response filter). LOESS is also prone to the effects of outliers in the data set, like other least squares methods. There is an iterative, robust version of LOESS [Cleveland (1979)] that can be used to reduce LOESS' sensitivity to outliers, but too many extreme outliers can still overcome even the robust method; other non-iterative robust local regression methods have also been proposed.
