---
title: "Non-linear least squares"
source: https://en.wikipedia.org/wiki/Nonlinear_least_squares
domain: nonlinear-regression
license: CC-BY-SA-4.0
tags: nonlinear regression, curve fitting, levenberg marquardt, gauss newton
fetched: 2026-07-02
---

# Non-linear least squares

(Redirected from

Nonlinear least squares

)

**Non-linear least squares** is the form of least squares analysis used to fit a set of *m* observations with a model that is non-linear in *n* unknown parameters (*m* ≥ *n*). It is used in some forms of nonlinear regression. The basis of the method is to approximate the model by a linear one and to refine the parameters by successive iterations. There are many similarities to linear least squares, but also some significant differences. In economic theory, the non-linear least squares method is applied in (i) the probit regression, (ii) threshold regression, (iii) smooth regression, (iv) logistic link regression, (v) Box–Cox transformed regressors ( $m(x,\theta _{i})=\theta _{1}+\theta _{2}x^{(\theta _{3})}$ ).

## Theory

Consider a set of m data points, $(x_{1},y_{1}),(x_{2},y_{2}),\dots ,(x_{m},y_{m}),$ and a curve (model function) ${\hat {y}}=f(x,{\boldsymbol {\beta }}),$ that in addition to the variable x also depends on n parameters, ${\boldsymbol {\beta }}=(\beta _{1},\beta _{2},\dots ,\beta _{n}),$ with $m\geq n.$ It is desired to find the vector ${\boldsymbol {\beta }}$ of parameters such that the curve fits best the given data in the least squares sense, that is, the sum of squares $S=\sum _{i=1}^{m}r_{i}^{2}$ is minimized, where the residuals (in-sample prediction errors) *ri* are given by $r_{i}=y_{i}-f(x_{i},{\boldsymbol {\beta }})$ for $i=1,2,\dots ,m.$

The minimum value of S occurs when the gradient is zero. Since the model contains n parameters there are n gradient equations: ${\frac {\partial S}{\partial \beta _{j}}}=2\sum _{i}r_{i}{\frac {\partial r_{i}}{\partial \beta _{j}}}=0\quad (j=1,\ldots ,n).$

In a nonlinear system, the derivatives ${\textstyle {\frac {\partial r_{i}}{\partial \beta _{j}}}}$ are functions of both the independent variable and the parameters, so in general these gradient equations do not have a closed solution. Instead, initial values must be chosen for the parameters. Then, the parameters are refined iteratively, that is, the values are obtained by successive approximation, $\beta _{j}\approx \beta _{j}^{k+1}=\beta _{j}^{k}+\Delta \beta _{j}.$

Here, k is an iteration number and the vector of increments, $\Delta {\boldsymbol {\beta }}$ is known as the shift vector. At each iteration the model is linearized by approximation to a first-order Taylor polynomial expansion about ${\boldsymbol {\beta }}^{k}$ $f(x_{i},{\boldsymbol {\beta }})\approx f(x_{i},{\boldsymbol {\beta }}^{k})+\sum _{j}{\frac {\partial f(x_{i},{\boldsymbol {\beta }}^{k})}{\partial \beta _{j}}}\left(\beta _{j}-\beta _{j}^{k}\right)=f(x_{i},{\boldsymbol {\beta }}^{k})+\sum _{j}J_{ij}\,\Delta \beta _{j}.$ The Jacobian matrix, **J**, is a function of constants, the independent variable *and* the parameters, so it changes from one iteration to the next. Thus, in terms of the linearized model, ${\frac {\partial r_{i}}{\partial \beta _{j}}}=-J_{ij}$ and the residuals are given by $\Delta y_{i}=y_{i}-f(x_{i},{\boldsymbol {\beta }}^{k}),$ $r_{i}=y_{i}-f(x_{i},{\boldsymbol {\beta }})=\left(y_{i}-f(x_{i},{\boldsymbol {\beta }}^{k})\right)+\left(f(x_{i},{\boldsymbol {\beta }}^{k})-f(x_{i},{\boldsymbol {\beta }})\right)\approx \Delta y_{i}-\sum _{s=1}^{n}J_{is}\Delta \beta _{s}.$

Substituting these expressions into the gradient equations, they become $-2\sum _{i=1}^{m}J_{ij}\left(\Delta y_{i}-\sum _{s=1}^{n}J_{is}\ \Delta \beta _{s}\right)=0,$ which, on rearrangement, become n simultaneous linear equations, the **normal equations** $\sum _{i=1}^{m}\sum _{s=1}^{n}J_{ij}J_{is}\ \Delta \beta _{s}=\sum _{i=1}^{m}J_{ij}\ \Delta y_{i}\qquad (j=1,\dots ,n).$

The normal equations are written in matrix notation as $\left(\mathbf {J} ^{\mathsf {T}}\mathbf {J} \right)\Delta {\boldsymbol {\beta }}=\mathbf {J} ^{\mathsf {T}}\ \Delta \mathbf {y} .$

These equations form the basis for the Gauss–Newton algorithm for a non-linear least squares problem.

Note the sign convention in the definition of the Jacobian matrix in terms of the derivatives. Formulas linear in J may appear with factor of $-1$ in other articles or the literature.

### Extension by weights

When the observations are not equally reliable, a weighted sum of squares may be minimized, $S=\sum _{i=1}^{m}W_{ii}r_{i}^{2}.$

Each element of the diagonal weight matrix **W** should, ideally, be equal to the reciprocal of the error variance of the measurement. The normal equations are then, more generally, $\left(\mathbf {J} ^{\mathsf {T}}\mathbf {WJ} \right)\Delta {\boldsymbol {\beta }}=\mathbf {J} ^{\mathsf {T}}\mathbf {W} \ \Delta \mathbf {y} .$

## Geometrical interpretation

In linear least squares the objective function, S, is a quadratic function of the parameters. $S=\sum _{i}W_{ii}\left(y_{i}-\sum _{j}X_{ij}\beta _{j}\right)^{2}$ When there is only one parameter the graph of S with respect to that parameter will be a parabola. With two or more parameters the contours of S with respect to any pair of parameters will be concentric ellipses (assuming that the normal equations matrix $\mathbf {X} ^{\mathsf {T}}\mathbf {WX}$ is positive definite). The minimum parameter values are to be found at the centre of the ellipses. The geometry of the general objective function can be described as paraboloid elliptical. In NLLSQ the objective function is quadratic with respect to the parameters only in a region close to its minimum value, where the truncated Taylor series is a good approximation to the model. $S\approx \sum _{i}W_{ii}\left(y_{i}-\sum _{j}J_{ij}\beta _{j}\right)^{2}$ The more the parameter values differ from their optimal values, the more the contours deviate from elliptical shape. A consequence of this is that initial parameter estimates should be as close as practicable to their (unknown!) optimal values. It also explains how divergence can come about as the Gauss–Newton algorithm is convergent only when the objective function is approximately quadratic in the parameters.

## Computation

### Initial parameter estimates

Some problems of ill-conditioning and divergence can be corrected by finding initial parameter estimates that are near to the optimal values. A good way to do this is by computer simulation. Both the observed and calculated data are displayed on a screen. The parameters of the model are adjusted by hand until the agreement between observed and calculated data is reasonably good. Although this will be a subjective judgment, it is sufficient to find a good starting point for the non-linear refinement. Initial parameter estimates can be created using transformations or linearizations. Better still evolutionary algorithms such as the Stochastic Funnel Algorithm can lead to the convex basin of attraction that surrounds the optimal parameter estimates. Hybrid algorithms that use randomization and elitism, followed by Newton methods have been shown to be useful and computationally efficient.

### Solution

Any method among the ones described below can be applied to find a solution.

### Convergence criteria

The common sense criterion for convergence is that the sum of squares does not increase from one iteration to the next. However this criterion is often difficult to implement in practice, for various reasons. A useful convergence criterion is $\left|{\frac {S^{k}-S^{k+1}}{S^{k}}}\right|<0.0001.$ The value 0.0001 is somewhat arbitrary and may need to be changed. In particular it may need to be increased when experimental errors are large. An alternative criterion is $\left|{\frac {\Delta \beta _{j}}{\beta _{j}}}\right|<0.001,\qquad j=1,\dots ,n.$

Again, the numerical value is somewhat arbitrary; 0.001 is equivalent to specifying that each parameter should be refined to 0.1% precision. This is reasonable when it is less than the largest relative standard deviation on the parameters.

### Calculation of the Jacobian by numerical approximation

There are models for which it is either very difficult or even impossible to derive analytical expressions for the elements of the Jacobian. Then, the numerical approximation ${\frac {\partial f(x_{i},{\boldsymbol {\beta }})}{\partial \beta _{j}}}\approx {\frac {\delta f(x_{i},{\boldsymbol {\beta }})}{\delta \beta _{j}}}$ is obtained by calculation of $f(x_{i},{\boldsymbol {\beta }})$ for $\beta _{j}$ and $\beta _{j}+\delta \beta _{j}$ . The increment, $\delta \beta _{j}$ , size should be chosen so the numerical derivative is not subject to approximation error by being too large, or round-off error by being too small.

### Parameter errors, confidence limits, residuals etc.

Some information is given in the corresponding section on the Weighted least squares page.

### Multiple minima

Multiple minima can occur in a variety of circumstances some of which are:

- A parameter is raised to a power of two or more. For example, when fitting data to a Lorentzian curve $f(x_{i},{\boldsymbol {\beta }})={\frac {\alpha }{1+\left({\frac {\gamma -x_{i}}{\beta }}\right)^{2}}}$ where $\alpha$ is the height, $\gamma$ is the position and $\beta$ is the half-width at half height, there are two solutions for the half-width, ${\hat {\beta }}$ and $-{\hat {\beta }}$ which give the same optimal value for the objective function.
- Two parameters can be interchanged without changing the value of the model. A simple example is when the model contains the product of two parameters, since $\alpha \beta$ will give the same value as $\beta \alpha$ .
- A parameter is in a trigonometric function, such as $\sin \beta$ , which has identical values at ${\hat {\beta }}+2n\pi$ . See Levenberg–Marquardt algorithm for an example.

Not all multiple minima have equal values of the objective function. False minima, also known as local minima, occur when the objective function value is greater than its value at the so-called global minimum. To be certain that the minimum found is the global minimum, the refinement should be started with widely differing initial values of the parameters. When the same minimum is found regardless of starting point, it is likely to be the global minimum.

When multiple minima exist there is an important consequence: the objective function will have a stationary point (e.g. a maximum or a saddle point) somewhere between two minima. The normal equations matrix is not positive definite at a stationary point in the objective function, because the gradient vanishes and no unique direction of descent exists. Refinement from a point (a set of parameter values) close to a stationary point will be ill-conditioned and should be avoided as a starting point. For example, when fitting a Lorentzian the normal equations matrix is not positive definite when the half-width of the Lorentzian is zero.

### Transformation to a linear model

A non-linear model can sometimes be transformed into a linear one. Such an approximation is, for instance, often applicable in the vicinity of the best estimator, and it is one of the basic assumption in most iterative minimization algorithms. When a linear approximation is valid, the model can directly be used for inference with a generalized least squares, where the equations of the Linear Template Fit apply.

Another example of a linear approximation would be when the model is a simple exponential function, $f(x_{i},{\boldsymbol {\beta }})=\alpha e^{\beta x_{i}},$ which can be transformed into a linear model by taking logarithms. $\log f(x_{i},{\boldsymbol {\beta }})=\log \alpha +\beta x_{i}$ Graphically this corresponds to working on a semi-log plot. The sum of squares becomes $S=\sum _{i}(\log y_{i}-\log \alpha -\beta x_{i})^{2}.$ This procedure should be avoided unless the errors are multiplicative and log-normally distributed because it can give misleading results. This comes from the fact that whatever the experimental errors on *y* might be, the errors on log *y* are different. Therefore, when the transformed sum of squares is minimized, different results will be obtained both for the parameter values and their calculated standard deviations. However, with multiplicative errors that are log-normally distributed, this procedure gives unbiased and consistent parameter estimates.

Another example is furnished by Michaelis–Menten kinetics, used to determine two parameters $V_{\max }$ and $K_{m}$ : $v={\frac {V_{\max }[S]}{K_{m}+[S]}}.$ The Lineweaver–Burk plot ${\frac {1}{v}}={\frac {1}{V_{\max }}}+{\frac {K_{m}}{V_{\max }[S]}}$ of ${\textstyle {\frac {1}{v}}}$ against ${\textstyle {\frac {1}{[S]}}}$ is linear in the parameters ${\textstyle {\frac {1}{V_{\max }}}}$ and ${\textstyle {\frac {K_{m}}{V_{\max }}}}$ but very sensitive to data error and strongly biased toward fitting the data in a particular range of the independent variable $[S]$ .

## Algorithms

### Gauss–Newton method

The normal equations $\left(\mathbf {J} ^{\mathsf {T}}\mathbf {WJ} \right)\Delta {\boldsymbol {\beta }}=\left(\mathbf {J} ^{\mathsf {T}}\mathbf {W} \right)\Delta \mathbf {y}$ may be solved for $\Delta {\boldsymbol {\beta }}$ by Cholesky decomposition, as described in linear least squares. The parameters are updated iteratively ${\boldsymbol {\beta }}^{k+1}={\boldsymbol {\beta }}^{k}+\Delta {\boldsymbol {\beta }}$ where *k* is an iteration number. While this method may be adequate for simple models, it will fail if divergence occurs. Therefore, protection against divergence is essential.

#### Shift-cutting

If divergence occurs, a simple expedient is to reduce the length of the shift vector, $\Delta {\boldsymbol {\beta }}$ , by a fraction, *f* ${\boldsymbol {\beta }}^{k+1}={\boldsymbol {\beta }}^{k}+f\ \Delta {\boldsymbol {\beta }}.$ For example, the length of the shift vector may be successively halved until the new value of the objective function is less than its value at the last iteration. The fraction, *f* could be optimized by a line search. As each trial value of *f* requires the objective function to be re-calculated it is not worth optimizing its value too stringently.

When using shift-cutting, the direction of the shift vector remains unchanged. This limits the applicability of the method to situations where the direction of the shift vector is not very different from what it would be if the objective function were approximately quadratic in the parameters, ${\boldsymbol {\beta }}^{k}.$

#### Marquardt parameter

If divergence occurs and the direction of the shift vector is so far from its "ideal" direction that shift-cutting is not very effective, that is, the fraction, *f* required to avoid divergence is very small, the direction must be changed. This can be achieved by using the Marquardt parameter. In this method the normal equations are modified $\left(\mathbf {J} ^{\mathsf {T}}\mathbf {WJ} +\lambda \mathbf {I} \right)\Delta {\boldsymbol {\beta }}=\left(\mathbf {J} ^{\mathsf {T}}\mathbf {W} \right)\Delta \mathbf {y}$ where $\lambda$ is the Marquardt parameter and **I** is an identity matrix. Increasing the value of $\lambda$ has the effect of changing both the direction and the length of the shift vector. The shift vector is rotated towards the direction of steepest descent when $\lambda \mathbf {I} \gg \mathbf {J} ^{\mathsf {T}}\mathbf {WJ} ,\ {\Delta {\boldsymbol {\beta }}}\approx {\frac {1}{\lambda }}\mathbf {J} ^{\mathsf {T}}\mathbf {W} \ \Delta \mathbf {y} .$ $\mathbf {J} ^{\mathsf {T}}\mathbf {W} \,\Delta \mathbf {y}$ is the steepest descent vector. So, when $\lambda$ becomes very large, the shift vector becomes a small fraction of the steepest descent vector.

Various strategies have been proposed for the determination of the Marquardt parameter. As with shift-cutting, it is wasteful to optimize this parameter too stringently. Rather, once a value has been found that brings about a reduction in the value of the objective function, that value of the parameter is carried to the next iteration, reduced if possible, or increased if need be. When reducing the value of the Marquardt parameter, there is a cut-off value below which it is safe to set it to zero, that is, to continue with the unmodified Gauss–Newton method. The cut-off value may be set equal to the smallest singular value of the Jacobian. A bound for this value is given by $1/\operatorname {tr} \left(\mathbf {J} ^{\mathsf {T}}\mathbf {WJ} \right)^{-1}$ where tr is the trace function.

### QR decomposition

The minimum in the sum of squares can be found by a method that does not involve forming the normal equations. The residuals with the linearized model can be written as $\mathbf {r} =\Delta \mathbf {y} -\mathbf {J} \,\Delta {\boldsymbol {\beta }}.$ The Jacobian is subjected to an orthogonal decomposition; the QR decomposition will serve to illustrate the process. $\mathbf {J} =\mathbf {QR}$ where **Q** is an orthogonal $m\times m$ matrix and **R** is an $m\times n$ matrix which is partitioned into an $n\times n$ block, $\mathbf {R} _{n}$ , and a $(m-n)\times n$ zero block. $\mathbf {R} _{n}$ is upper triangular.

$\mathbf {R} ={\begin{bmatrix}\mathbf {R} _{n}\\\mathbf {0} \end{bmatrix}}$

The residual vector is left-multiplied by $\mathbf {Q} ^{\mathsf {T}}$ .

$\mathbf {Q} ^{\mathsf {T}}\mathbf {r} =\mathbf {Q} ^{\mathsf {T}}\ \Delta \mathbf {y} -\mathbf {R} \ \Delta {\boldsymbol {\beta }}={\begin{bmatrix}\left(\mathbf {Q} ^{\mathsf {T}}\ \Delta \mathbf {y} -\mathbf {R} \ \Delta {\boldsymbol {\beta }}\right)_{n}\\\left(\mathbf {Q} ^{\mathsf {T}}\ \Delta \mathbf {y} \right)_{m-n}\end{bmatrix}}$

This has no effect on the sum of squares since $S=\mathbf {r} ^{\mathsf {T}}\mathbf {Q} \mathbf {Q} ^{\mathsf {T}}\mathbf {r} =\mathbf {r} ^{\mathsf {T}}\mathbf {r}$ because **Q** is orthogonal. The minimum value of *S* is attained when the upper block is zero. Therefore, the shift vector is found by solving $\mathbf {R} _{n}\ \Delta {\boldsymbol {\beta }}=\left(\mathbf {Q} ^{\mathsf {T}}\ \Delta \mathbf {y} \right)_{n}.$

These equations are easily solved as **R** is upper triangular.

### Singular value decomposition

A variant of the method of orthogonal decomposition involves singular value decomposition, in which **R** is diagonalized by further orthogonal transformations.

$\mathbf {J} =\mathbf {U} {\boldsymbol {\Sigma }}\mathbf {V} ^{\mathsf {T}}$ where $\mathbf {U}$ is orthogonal, ${\boldsymbol {\Sigma }}$ is a diagonal matrix of singular values and $\mathbf {V}$ is the orthogonal matrix of the eigenvectors of $\mathbf {J} ^{\mathsf {T}}\mathbf {J}$ or equivalently the right singular vectors of $\mathbf {J}$ . In this case the shift vector is given by $\Delta {\boldsymbol {\beta }}=\mathbf {V} {\boldsymbol {\Sigma }}^{-1}\left(\mathbf {U} ^{\mathsf {T}}\ \Delta \mathbf {y} \right)_{n}.$

The relative simplicity of this expression is very useful in theoretical analysis of non-linear least squares. The application of singular value decomposition is discussed in detail in Lawson and Hanson.

### Gradient methods

There are many examples in the scientific literature where different methods have been used for non-linear data-fitting problems.

- Inclusion of second derivatives in The Taylor series expansion of the model function. This is Newton's method in optimization. $f(x_{i},{\boldsymbol {\beta }})=f^{k}(x_{i},{\boldsymbol {\beta }})+\sum _{j}J_{ij}\,\Delta \beta _{j}+{\frac {1}{2}}\sum _{j}\sum _{k}\Delta \beta _{j}\,\Delta \beta _{k}\,H_{jk_{(i)}},\ H_{jk_{(i)}}={\frac {\partial ^{2}f(x_{i},{\boldsymbol {\beta }})}{\partial \beta _{j}\,\partial \beta _{k}}}.$ The matrix **H** is known as the Hessian matrix. Although this model has better convergence properties near to the minimum, it is much worse when the parameters are far from their optimal values. Calculation of the Hessian adds to the complexity of the algorithm. This method is not in general use.
- Davidon–Fletcher–Powell method. This method, a form of pseudo-Newton method, is similar to the one above but calculates the Hessian by successive approximation, to avoid having to use analytical expressions for the second derivatives.
- Steepest descent. Although a reduction in the sum of squares is guaranteed when the shift vector points in the direction of steepest descent, this method often performs poorly. When the parameter values are far from optimal the direction of the steepest descent vector, which is normal (perpendicular) to the contours of the objective function, is very different from the direction of the Gauss–Newton vector. This makes divergence much more likely, especially as the minimum along the direction of steepest descent may correspond to a small fraction of the length of the steepest descent vector. When the contours of the objective function are very eccentric, due to there being high correlation between parameters, the steepest descent iterations, with shift-cutting, follow a slow, zig-zag trajectory towards the minimum.
- Conjugate gradient search. This is an improved steepest descent based method with good theoretical convergence properties, although it can fail on finite-precision digital computers even when used on quadratic problems.

Direct search methods depend on evaluations of the objective function at a variety of parameter values and do not use derivatives at all. They offer alternatives to the use of numerical derivatives in the Gauss–Newton method and gradient methods.

- Alternating variable search. Each parameter is varied in turn by adding a fixed or variable increment to it and retaining the value that brings about a reduction in the sum of squares. The method is simple and effective when the parameters are not highly correlated. It has very poor convergence properties, but may be useful for finding initial parameter estimates.
- Nelder–Mead (simplex) search. A simplex in this context is a polytope of *n* + 1 vertices in *n* dimensions; a triangle on a plane, a tetrahedron in three-dimensional space and so forth. Each vertex corresponds to a value of the objective function for a particular set of parameters. The shape and size of the simplex is adjusted by varying the parameters in such a way that the value of the objective function at the highest vertex always decreases. Although the sum of squares may initially decrease rapidly, it can converge to a nonstationary point on quasiconvex problems, by an example of M. J. D. Powell.

More detailed descriptions of these, and other, methods are available, in *Numerical Recipes*, together with computer code in various languages.
