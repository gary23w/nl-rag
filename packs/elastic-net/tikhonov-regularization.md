---
title: "Ridge regression"
source: https://en.wikipedia.org/wiki/Tikhonov_regularization
domain: elastic-net
license: CC-BY-SA-4.0
tags: elastic net, penalized regression, regularization path, sparse model
fetched: 2026-07-02
---

# Ridge regression

(Redirected from

Tikhonov regularization

)

**Ridge regression** (also known as **Tikhonov regularization**, named for Andrey Tikhonov) is a method of estimating the coefficients of multiple-regression models in scenarios where the variables are highly correlated. It has been used in many fields including econometrics, chemistry, and engineering. It is a method of regularization of ill-posed problems. It is particularly useful to mitigate the problem of multicollinearity in linear regression, which commonly occurs in models with large numbers of parameters. In general, the method provides improved efficiency in parameter estimation problems in exchange for a tolerable amount of bias (see bias–variance tradeoff).

The theory was first introduced by Hoerl and Kennard in 1970 in their *Technometrics* papers "Ridge regressions: biased estimation of nonorthogonal problems" and "Ridge regressions: applications in nonorthogonal problems".

Ridge regression was developed as a possible solution to the imprecision of least square estimators when linear regression models have some multicollinear (highly correlated) independent variables—by creating a ridge regression estimator (RR). This provides a more precise ridge parameters estimate, as its variance and mean square estimator are often smaller than the least square estimators previously derived.

## Overview

In the ordinary least squares solution of

$\mathbf {Y} =\mathbf {X} {\boldsymbol {\beta }}+{\boldsymbol {\varepsilon }},\,$

the problem of a near-singular moment matrix $\mathbf {X} ^{\mathsf {T}}\mathbf {X}$ is alleviated by adding positive elements to the diagonals, thereby decreasing its condition number. Compared to the ordinary least squares estimator, the simple ridge estimator has an extra term $\lambda \mathbf {I}$ in the denominator: ${\hat {\boldsymbol {\beta }}}_{\lambda }=\left(\mathbf {X} ^{\mathsf {T}}\mathbf {X} +\lambda \mathbf {I} \right)^{-1}\mathbf {X} ^{\mathsf {T}}\mathbf {Y}$ where $\mathbf {Y}$ is the regressand or response vector, $\mathbf {X}$ is the design matrix, $\mathbf {I}$ is the identity matrix, and the ridge (or Tikhonov) regularization parameter $\lambda \geq 0$ serves as the constant shifting the diagonals of the moment matrix. It can be shown that this estimator is the solution to the least squares problem subject to the constraint ${\boldsymbol {\beta }}^{\mathsf {T}}{\boldsymbol {\beta }}=c$ , which can be expressed as a Lagrangian minimization: ${\text{argmin}}_{\boldsymbol {\beta }}\,\|\mathbf {Y} -\mathbf {X} {\boldsymbol {\beta }}\|^{2}+\lambda \left({\boldsymbol {\beta }}^{\mathsf {T}}{\boldsymbol {\beta }}-c\right)$ which shows that $\lambda$ is nothing but the Lagrange multiplier of the constraint. In fact, there is a one-to-one relationship between c and $\lambda$ and since, in practice, we do not know c , we define $\lambda$ heuristically or find it via additional data-fitting strategies, see Determination of the Tikhonov parameter below.

Note that as $\lambda \downarrow 0$ , the constraint eventually becomes non-binding, and the ridge estimator converges to the minimum-norm ordinary least squares estimator, here denoted as ${\hat {\boldsymbol {\beta }}}={\hat {\boldsymbol {\beta }}}_{0}$ :

$\lim _{\lambda \downarrow 0}{\hat {\boldsymbol {\beta }}}_{\lambda }=\mathbf {X} ^{+}\mathbf {Y} ={\hat {\boldsymbol {\beta }}}_{0},$ with $\mathbf {X} ^{+}$ denoting the pseudoinverse of $\mathbf {X}$ .

## Determination of the Tikhonov parameter

The optimal regularization parameter $\lambda$ is usually unknown and in practice needs to be estimated. Typically, a data-driven choice for the Tikhonov regularization parameter $\lambda$ is accomplished either via cross-validation, or via a plug-in procedure, as follows.

### Generalized cross-validation estimator

A common data-driven choice for $\lambda$ is the minimizer of the cross-validation loss or its generalizations. For example, Grace Wahba proved that the optimal parameter, in the sense of generalized cross-validation minimizes

$G={\frac {\operatorname {RSS} }{\tau ^{2}}}={\frac {\left\|\mathbf {X} {\hat {\boldsymbol {\beta }}}-\mathbf {Y} \right\|^{2}}{\left[\operatorname {tr} \left(\mathbf {I} -\mathbf {X} \left(\mathbf {X} ^{\mathsf {T}}\mathbf {X} +\lambda ^{2}\mathbf {I} \right)^{-1}\mathbf {X} ^{\mathsf {T}}\right)\right]^{2}}},$ where $\operatorname {RSS}$ is the residual sum of squares, and $\tau$ is the effective number of degrees of freedom.

### Plug-in estimator

Assume that $\mathbf {X}$ is an $n\times p$ matrix and define the matrix $\Omega :=(\mathbf {X} ^{\top }\mathbf {X} /n)^{+}$ . Then, consider the following choice for the Tikhonov regularization parameter:

$\lambda ^{*}:={\frac {\varsigma ^{2}\mathrm {tr} (\Omega )}{{\boldsymbol {\beta }}^{\top }\Omega {\boldsymbol {\beta }}+3\varsigma ^{2}\mathrm {tr} (\Omega ^{2})/n}},$

where $\varsigma ^{2}$ is the variance of the noise ${\boldsymbol {\varepsilon }}=\mathbf {Y} -\mathbf {X} {\boldsymbol {\beta }}$ , that is, $\mathrm {Var} ({\boldsymbol {\varepsilon }})=\varsigma ^{2}\mathbf {I}$ . It can be shown that the ridge estimator ${\hat {\boldsymbol {\beta }}}_{\lambda ^{*}}$ enjoys smaller expected in-sample risk than the minimum-norm least-squares estimator ${\hat {\boldsymbol {\beta }}}_{0}=\mathbf {X} ^{+}\mathbf {Y}$ . More precisely,

$\mathbb {E} \|\mathbf {Y} '-\mathbf {X} {\hat {\boldsymbol {\beta }}}_{0}\|^{2}\geq \mathbb {E} \|\mathbf {Y} '-\mathbf {X} {\hat {\boldsymbol {\beta }}}_{\lambda ^{*}}\|^{2}+{\frac {\varsigma ^{2}}{n}}\lambda ^{*}\mathrm {tr} (\Omega ),$

where the expectations treat $\mathbf {X}$ as fixed and $\mathbf {Y} '$ is *test response* data, independent from $\mathbf {Y}$ (and hence independent from the estimators ${\hat {\boldsymbol {\beta }}}_{0}$ and ${\hat {\boldsymbol {\beta }}}_{\lambda ^{*}}$ ).

Of course, in practice the formula for $\lambda ^{*}$ is used by plugging in statistical estimators for the unknown parameters ${\boldsymbol {\beta }}$ and $\varsigma ^{2}$ . When $n>p$ , the most natural estimators for these parameters are the usual least-squares ones:

${\hat {\boldsymbol {\beta }}}=\mathbf {X} ^{+}\mathbf {Y} ,\qquad {\hat {\varsigma }}^{2}={\frac {\|\mathbf {Y} -\mathbf {X} {\hat {\boldsymbol {\beta }}}\|^{2}}{n-p}}.$ Replacing the unknown ${\boldsymbol {\beta }},\varsigma ^{2}$ in the formula for $\lambda ^{*}$ with the corresponding ${\hat {\boldsymbol {\beta }}},{\hat {\varsigma }}^{2}$ thus gives the so-called *plug-in estimator* ${\widehat {\lambda }}^{*}$ for the optimal $\lambda ^{*}$ .

Alternative approaches to the data-driven selection of the Tikhonov regularization parameter include the discrepancy principle, L-curve method, restricted maximum likelihood.

## History

Tikhonov regularization was invented independently in many different contexts. It became widely known through its application to integral equations in the works of Andrey Tikhonov and David L. Phillips. Some authors use the term **Tikhonov–Phillips regularization**. The finite-dimensional case was expounded by Arthur E. Hoerl, who took a statistical approach, and by Manus Foster, who interpreted this method as a Wiener–Kolmogorov (Kriging) filter. Following Hoerl, it is known in the statistical literature as ridge regression, named after ridge analysis ("ridge" refers to the path from the constrained maximum).

## Tikhonov regularization for linear equations

Suppose that for a known real matrix A and vector $\mathbf {b}$ , we wish to find a vector $\mathbf {x}$ such that $A\mathbf {x} =\mathbf {b} ,$ where $\mathbf {x}$ and $\mathbf {b}$ may be of different sizes and A may even be non-square.

The standard approach is ordinary least squares linear regression. However, if no $\mathbf {x}$ satisfies the equation or more than one $\mathbf {x}$ does—that is, the solution is not unique—the problem is said to be ill posed. In such cases, ordinary least squares estimation leads to an overdetermined, or more often an underdetermined system of equations. Most real-world phenomena have the effect of low-pass filters in the forward direction where A maps $\mathbf {x}$ to $\mathbf {b}$ . Therefore, in solving the inverse-problem, the inverse mapping operates as a high-pass filter that has the undesirable tendency of amplifying noise (eigenvalues / singular values are largest in the reverse mapping where they were smallest in the forward mapping). In addition, ordinary least squares implicitly nullifies every element of the reconstructed version of $\mathbf {x}$ that is in the null-space of A , rather than allowing for a model to be used as a prior for $\mathbf {x}$ . Ordinary least squares seeks to minimize the sum of squared residuals, which can be compactly written as $\left\|A\mathbf {x} -\mathbf {b} \right\|_{2}^{2},$ where $\|\cdot \|_{2}$ is the Euclidean norm.

In order to give preference to a particular solution with desirable properties, a regularization term can be included in this minimization: $\left\|A\mathbf {x} -\mathbf {b} \right\|_{2}^{2}+\left\|\Gamma \mathbf {x} \right\|_{2}^{2}=\left\|{\mathcal {A}}\mathbf {x} -{\mathcal {b}}\right\|_{2}^{2},$ where ${\mathcal {A}}={\begin{pmatrix}A\\\Gamma \end{pmatrix}}$ and ${\mathcal {b}}={\begin{pmatrix}\mathbf {b} \\{\boldsymbol {0}}\end{pmatrix}}$ , for some suitably chosen **Tikhonov matrix** $\Gamma$ . In many cases, this matrix is chosen as a scalar multiple of the identity matrix ( $\Gamma =\alpha I$ ), giving preference to solutions with smaller norms; this is known as ***L*2 regularization**. In other cases, high-pass operators (e.g., a difference operator or a weighted Fourier operator) may be used to enforce smoothness if the underlying vector is believed to be mostly continuous. This regularization improves the conditioning of the problem, thus enabling a direct numerical solution. Treating it as an ordinary least squares problem with augmented matrices ${\mathcal {A}}$ and ${\mathcal {b}}$ , the solution is ${\hat {\mathbf {x} }}=({\mathcal {A}}^{\mathsf {T}}{\mathcal {A}})^{-1}{\mathcal {A}}^{\mathsf {T}}\mathbf {\mathcal {b}} =(A^{\mathsf {T}}A+\Gamma ^{\mathsf {T}}\Gamma )^{-1}A^{\mathsf {T}}\mathbf {b} .$ The effect of regularization may be varied by the scale of the matrix $\Gamma$ . For $\Gamma =0$ this reduces to the unregularized least-squares solution, provided that (*A*T*A*)−1 exists. Note that in case of a complex matrix A , as usual the transpose $A^{\mathsf {T}}$ has to be replaced by the Hermitian transpose $A^{\mathsf {H}}$ .

*L*2 regularization is used in many contexts aside from linear regression, such as classification with logistic regression or support vector machines, and matrix factorization.

### Application to existing fit results

Since Tikhonov Regularization simply adds a quadratic term to the objective function in optimization problems, it is possible to do so after the unregularised optimisation has taken place. E.g., if the above problem with $\Gamma =0$ yields the solution ${\hat {\mathbf {x} }}_{0}$ , the solution in the presence of $\Gamma \neq 0$ can be expressed as: ${\hat {\mathbf {x} }}=B{\hat {\mathbf {x} }}_{0},$ with the "regularisation matrix" $B=\left(A^{\mathsf {T}}A+\Gamma ^{\mathsf {T}}\Gamma \right)^{-1}A^{\mathsf {T}}A$ .

If the parameter fit comes with a covariance matrix of the estimated parameter uncertainties $V_{0}$ , then the regularisation matrix will be $B=(V_{0}^{-1}+\Gamma ^{\mathsf {T}}\Gamma )^{-1}V_{0}^{-1},$ and the regularised result will have a new covariance $V=BV_{0}B^{\mathsf {T}}.$

In the context of arbitrary likelihood fits, this is valid, as long as the quadratic approximation of the likelihood function is valid. This means that, as long as the perturbation from the unregularised result is small, one can regularise any result that is presented as a best fit point with a covariance matrix. No detailed knowledge of the underlying likelihood function is needed.

### Generalized Tikhonov regularization

For general multivariate normal distributions for $\mathbf {x}$ and the data error, one can apply a transformation of the variables to reduce to the case above. Equivalently, one can seek an $\mathbf {x}$ to minimize $\left\|A\mathbf {x} -\mathbf {b} \right\|_{P}^{2}+\left\|\mathbf {x} -\mathbf {x} _{0}\right\|_{Q}^{2},$ where we have used $\left\|\mathbf {x} \right\|_{Q}^{2}$ to stand for the weighted norm squared $\mathbf {x} ^{\mathsf {T}}Q\mathbf {x}$ (compare with the Mahalanobis distance). In the Bayesian interpretation P is the inverse covariance matrix of $\mathbf {b}$ , $\mathbf {x} _{0}$ is the expected value of $\mathbf {x}$ , and Q is the inverse covariance matrix of $\mathbf {x}$ .

The Tikhonov matrix is not explicitly included because the corresponding regularization term $\left\|\Gamma \mathbf {x} -\mathbf {x} _{0}'\right\|_{Q'}^{2}$ reduces to above with $\Gamma \mathbf {x} _{0}=\mathbf {x} _{0}'$ and $Q=\Gamma ^{T}Q'\Gamma$ . For normal regularization where $Q'=I$ , the Tikhonov matrix then appears in the Cholesky factorization $Q=\Gamma ^{\mathsf {T}}\Gamma$ and is considered a whitening filter.

This generalized problem has an optimal solution ${\hat {\mathbf {x} }}$ which can be written explicitly using the formula $\mathbf {\hat {\mathbf {x} }} =\left(A^{\mathsf {T}}PA+Q\right)^{-1}\left(A^{\mathsf {T}}P\mathbf {b} +Q\mathbf {x} _{0}\right)=\mathbf {x} _{0}+\left(A^{\mathsf {T}}PA+Q\right)^{-1}\left(A^{\mathsf {T}}P\left(\mathbf {b} -A\mathbf {x} _{0}\right)\right).$

## Lavrentyev regularization

In some situations, one can avoid using the transpose $A^{\mathsf {T}}$ , as proposed by Mikhail Lavrentyev. For example, if A is symmetric positive definite, i.e. $A=A^{\mathsf {T}}>0$ , so is its inverse $A^{-1}$ , which can thus be used to set up the weighted norm squared $\left\|\mathbf {x} \right\|_{P}^{2}=\mathbf {x} ^{\mathsf {T}}A^{-1}\mathbf {x}$ in the generalized Tikhonov regularization, leading to minimizing $\left\|A\mathbf {x} -\mathbf {b} \right\|_{A^{-1}}^{2}+\left\|\mathbf {x} -\mathbf {x} _{0}\right\|_{Q}^{2}$ or, equivalently up to a constant term, $\mathbf {x} ^{\mathsf {T}}\left(A+Q\right)\mathbf {x} -2\mathbf {x} ^{\mathsf {T}}\left(\mathbf {b} +Q\mathbf {x} _{0}\right).$

This minimization problem has an optimal solution $\mathbf {x} ^{*}$ which can be written explicitly using the formula $\mathbf {x} ^{*}=\left(A+Q\right)^{-1}\left(\mathbf {b} +Q\mathbf {x} _{0}\right),$ which is nothing but the solution of the generalized Tikhonov problem where $A=A^{\mathsf {T}}=P^{-1}.$

The Lavrentyev regularization, if applicable, is advantageous to the original Tikhonov regularization, since the Lavrentyev matrix $A+Q$ can be better conditioned, i.e., have a smaller condition number, compared to the Tikhonov matrix $A^{\mathsf {T}}A+\Gamma ^{\mathsf {T}}\Gamma .$

## Regularization in Hilbert space

Typically discrete linear ill-conditioned problems result from discretization of integral equations, and one can formulate a Tikhonov regularization in the original infinite-dimensional context. In the above we can interpret A as a compact operator on Hilbert spaces, and x and b as elements in the domain and range of A . The operator $A^{*}A+\Gamma ^{\mathsf {T}}\Gamma$ is then a self-adjoint bounded invertible operator.

## Relation to singular-value decomposition and Wiener filter

With $\Gamma =\alpha I$ , this least-squares solution can be analyzed in a special way using the singular-value decomposition. Given the singular value decomposition $A=U\Sigma V^{\mathsf {T}}$ with singular values $\sigma _{i}$ , the Tikhonov regularized solution can be expressed as ${\hat {x}}=VDU^{\mathsf {T}}b,$ where D has diagonal values $D_{ii}={\frac {\sigma _{i}}{\sigma _{i}^{2}+\alpha ^{2}}}$ and is zero elsewhere. This demonstrates the effect of the Tikhonov parameter on the condition number of the regularized problem. For the generalized case, a similar representation can be derived using a generalized singular-value decomposition.

Finally, it is related to the Wiener filter: ${\hat {x}}=\sum _{i=1}^{q}f_{i}{\frac {u_{i}^{\mathsf {T}}b}{\sigma _{i}}}v_{i},$ where the Wiener weights are $f_{i}={\frac {\sigma _{i}^{2}}{\sigma _{i}^{2}+\alpha ^{2}}}$ and q is the rank of A .

## Relation to probabilistic formulation

The probabilistic formulation of an inverse problem introduces (when all uncertainties are Gaussian) a covariance matrix $C_{M}$ representing the *a priori* uncertainties on the model parameters, and a covariance matrix $C_{D}$ representing the uncertainties on the observed parameters. In the special case when these two matrices are diagonal and isotropic, $C_{M}=\sigma _{M}^{2}I$ and $C_{D}=\sigma _{D}^{2}I$ , and, in this case, the equations of inverse theory reduce to the equations above, with $\alpha ={\sigma _{D}}/{\sigma _{M}}$ .

## Bayesian interpretation

Although at first the choice of the solution to this regularized problem may look artificial, and indeed the matrix $\Gamma$ seems rather arbitrary, the process can be justified from a Bayesian point of view. Note that for an ill-posed problem one must necessarily introduce some additional assumptions in order to get a unique solution. Statistically, the prior probability distribution of x is sometimes taken to be a multivariate normal distribution. For simplicity here, the following assumptions are made: the means are zero; their components are independent; the components have the same standard deviation $\sigma _{x}$ . The data are also subject to errors, and the errors in b are also assumed to be independent with zero mean and standard deviation $\sigma _{b}$ . Under these assumptions the Tikhonov-regularized solution is the most probable solution given the data and the *a priori* distribution of x , according to Bayes' theorem.

If the assumption of normality is replaced by assumptions of homoscedasticity and uncorrelatedness of errors, and if one still assumes zero mean, then the Gauss–Markov theorem entails that the solution is the minimal unbiased linear estimator.
