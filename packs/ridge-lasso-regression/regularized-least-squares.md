---
title: "Regularized least squares"
source: https://en.wikipedia.org/wiki/Regularized_least_squares
domain: ridge-lasso-regression
license: CC-BY-SA-4.0
tags: ridge regression, lasso regression, shrinkage estimator, L2 regularization
fetched: 2026-07-02
---

# Regularized least squares

**Regularized least squares** (**RLS**) is a family of methods for solving the least-squares problem while using regularization to further constrain the resulting solution.

RLS is used for two main reasons. The first comes up when the number of variables in the linear system exceeds the number of observations. In such settings, the ordinary least-squares problem is ill-posed and is therefore impossible to fit because the associated optimization problem has infinitely many solutions. RLS allows the introduction of further constraints that uniquely determine the solution.

The second reason for using RLS arises when the learned model suffers from poor generalization. RLS can be used in such cases to improve the generalizability of the model by constraining it at training time. This constraint can either force the solution to be "sparse" in some way or to reflect other prior knowledge about the problem such as information about correlations between features. A Bayesian understanding of this can be reached by showing that RLS methods are often equivalent to priors on the solution to the least-squares problem.

## General formulation

Consider a learning setting given by a probabilistic space $(X\times Y,\rho (X,Y))$ , $Y\in R$ . Let $S=\{x_{i},y_{i}\}_{i=1}^{n}$ denote a training set of n pairs i.i.d. with respect to the joint distribution $\rho$ . Let $V:Y\times R\to [0;\infty )$ be a loss function. Define F as the space of the functions such that expected risk: $\varepsilon (f)=\int V(y,f(x))\,d\rho (x,y)$ is well defined. The main goal is to minimize the expected risk: $\inf _{f\in F}\varepsilon (f)$ Since the problem cannot be solved exactly there is a need to specify how to measure the quality of a solution. A good learning algorithm should provide an estimator with a small risk.

As the joint distribution $\rho$ is typically unknown, the empirical risk is taken. For regularized least squares the square loss function is introduced: $\varepsilon (f)={\frac {1}{n}}\sum _{i=1}^{n}V(y_{i},f(x_{i}))={\frac {1}{n}}\sum _{i=1}^{n}(y_{i}-f(x_{i}))^{2}$

However, if the functions are from a relatively unconstrained space, such as the set of square-integrable functions on X , this approach may overfit the training data, and lead to poor generalization. Thus, it should somehow constrain or penalize the complexity of the function f . In RLS, this is accomplished by choosing functions from a reproducing kernel Hilbert space (RKHS) ${\mathcal {H}}$ , and adding a regularization term to the objective function, proportional to the norm of the function in ${\mathcal {H}}$ : $\inf _{f\in F}\varepsilon (f)+\lambda R(f),\lambda >0$

## Kernel formulation

### Definition of RKHS

A RKHS can be defined by a symmetric positive-definite kernel function $K(x,z)$ with the reproducing property: $\langle K_{x},f\rangle _{\mathcal {H}}=f(x),$ where $K_{x}(z)=K(x,z)$ . The RKHS for a kernel K consists of the completion of the space of functions spanned by $\left\{K_{x}\mid x\in X\right\}$ : ${\textstyle f(x)=\sum _{i=1}^{n}\alpha _{i}K_{x_{i}}(x),\,f\in {\mathcal {H}}}$ , where all $\alpha _{i}$ are real numbers. Some commonly used kernels include the linear kernel, inducing the space of linear functions: $K(x,z)=x^{\mathsf {T}}z,$ the polynomial kernel, inducing the space of polynomial functions of order d : $K(x,z)=\left(x^{\mathsf {T}}z+1\right)^{d},$ and the Gaussian kernel: $K(x,z)=e^{-{\left\|x-z\right\|^{2}}/{\sigma ^{2}}}.$

Note that for an arbitrary loss function V , this approach defines a general class of algorithms named Tikhonov regularization. For instance, using the hinge loss leads to the support vector machine algorithm, and using the epsilon-insensitive loss leads to support vector regression.

### Arbitrary kernel

The representer theorem guarantees that the solution can be written as: $f(x)=\sum _{i=1}^{n}c_{i}K(x_{i},x)$ for some $c\in \mathbb {R} ^{n}$ .

The minimization problem can be expressed as: $\min _{c\in \mathbb {R} ^{n}}{\frac {1}{n}}\left\|Y-Kc\right\|_{\mathbb {R} ^{n}}^{2}+\lambda \left\|f\right\|_{H}^{2},$ where, with some abuse of notation, the $i,j$ entry of kernel matrix K (as opposed to kernel function $K(\cdot ,\cdot )$ ) is $K(x_{i},x_{j})$ .

For such a function, ${\begin{aligned}\left\|f\right\|_{H}^{2}&=\langle f,f\rangle _{H}\\[1ex]&=\left\langle \sum _{i=1}^{n}c_{i}K(x_{i},\cdot ),\sum _{j=1}^{n}c_{j}K(x_{j},\cdot )\right\rangle _{H}\\[1ex]&=\sum _{i=1}^{n}\sum _{j=1}^{n}c_{i}c_{j}\left\langle K(x_{i},\cdot ),K(x_{j},\cdot )\right\rangle _{H}\\&=\sum _{i=1}^{n}\sum _{j=1}^{n}c_{i}c_{j}K(x_{i},x_{j})\\&=c^{\mathsf {T}}Kc,\end{aligned}}$

The following minimization problem can be obtained: $\min _{c\in \mathbb {R} ^{n}}{\frac {1}{n}}\left\|Y-Kc\right\|_{\mathbb {R} ^{n}}^{2}+\lambda c^{\mathsf {T}}Kc.$

As the sum of convex functions is convex, the solution is unique and its minimum can be found by setting the gradient with respect to c to 0 : $-{\frac {1}{n}}K\left(Y-Kc\right)+\lambda Kc=0\Rightarrow K\left(K+\lambda nI\right)c=KY\Rightarrow c=\left(K+\lambda nI\right)^{-1}Y,$ where $c\in \mathbb {R} ^{n}.$

#### Complexity

The complexity of training is basically the cost of computing the kernel matrix plus the cost of solving the linear system which is roughly $O(n^{3})$ . The computation of the kernel matrix for the linear or Gaussian kernel is $O(n^{2}D)$ . The complexity of testing is $O(n)$ .

### Prediction

The prediction at a new test point $x_{*}$ is: $f(x_{*})=\sum _{i=1}^{n}c_{i}K(x_{i},x_{*})=K(X,X_{*})^{\mathsf {T}}c$

### Linear kernel

For convenience a vector notation is introduced. Let X be an $n\times d$ matrix, where the rows are input vectors, and Y a $n\times 1$ vector where the entries are corresponding outputs. In terms of vectors, the kernel matrix can be written as $K=XX^{\mathsf {T}}$ . The learning function can be written as: $f(x_{*})=K_{x_{*}}c=x_{*}^{\mathsf {T}}X^{\mathsf {T}}c=x_{*}^{\mathsf {T}}w$

Here we define $w=X^{\mathsf {T}}c,w\in \mathbb {R} ^{d}$ . The objective function can be rewritten as: ${\begin{aligned}{\frac {1}{n}}\left\|Y-Kc\right\|_{\mathbb {R} ^{n}}^{2}+\lambda c^{\mathsf {T}}Kc&={\frac {1}{n}}\left\|y-XX^{\mathsf {T}}c\right\|_{\mathbb {R} ^{n}}^{2}+\lambda c^{\mathsf {T}}XX^{\mathsf {T}}c\\[1ex]&={\frac {1}{n}}\left\|y-Xw\right\|_{\mathbb {R} ^{n}}^{2}+\lambda \left\|w\right\|_{\mathbb {R} ^{d}}^{2}\end{aligned}}$

The first term is the objective function from ordinary least squares (OLS) regression, corresponding to the residual sum of squares. The second term is a regularization term, not present in OLS, which penalizes large w values. As a smooth finite dimensional problem is considered and it is possible to apply standard calculus tools. In order to minimize the objective function, the gradient is calculated with respect to w and set it to zero: $X^{\mathsf {T}}Xw-X^{\mathsf {T}}y+\lambda nw=0$ $w=\left(X^{\mathsf {T}}X+\lambda nI\right)^{-1}X^{\mathsf {T}}y$

This solution closely resembles that of standard linear regression, with an extra term $\lambda I$ . If the assumptions of OLS regression hold, the solution $w=\left(X^{\mathsf {T}}X\right)^{-1}X^{\mathsf {T}}y$ , with $\lambda =0$ , is an unbiased estimator, and is the minimum-variance linear unbiased estimator, according to the Gauss–Markov theorem. The term $\lambda nI$ therefore leads to a biased solution; however, it also tends to reduce variance. This is easy to see, as the covariance matrix of the w -values is proportional to $\left(X^{\mathsf {T}}X+\lambda nI\right)^{-1}$ , and therefore large values of $\lambda$ will lead to lower variance. Therefore, manipulating $\lambda$ corresponds to trading-off bias and variance. For problems with high-variance w estimates, such as cases with relatively small n or with correlated regressors, the optimal prediction accuracy may be obtained by using a nonzero $\lambda$ , and thus introducing some bias to reduce variance. Furthermore, it is not uncommon in machine learning to have cases where $n<d$ , in which case $X^{\mathsf {T}}X$ is rank-deficient, and a nonzero $\lambda$ is necessary to compute $\left(X^{\mathsf {T}}X+\lambda nI\right)^{-1}$ .

#### Complexity

The parameter $\lambda$ controls the invertibility of the matrix $X^{\mathsf {T}}X+\lambda nI$ . Several methods can be used to solve the above linear system, Cholesky decomposition being probably the method of choice, since the matrix $X^{\mathsf {T}}X+\lambda nI$ is symmetric and positive definite. The complexity of this method is $O(nD^{2})$ for training and $O(D)$ for testing. The cost $O(nD^{2})$ is essentially that of computing $X^{\mathsf {T}}X$ , whereas the inverse computation (or rather the solution of the linear system) is roughly $O(D^{3})$ .

## Feature maps and Mercer's theorem

In this section it will be shown how to extend RLS to any kind of reproducing kernel K. Instead of linear kernel a feature map is considered $\Phi :X\to F$ for some Hilbert space F , called the feature space. In this case the kernel is defined as: The matrix X is now replaced by the new data matrix $\Phi$ , where $\Phi _{ij}=\varphi _{j}(x_{i})$ , or the j -th component of the $\varphi (x_{i})$ . $K(x,x')=\langle \Phi (x),\Phi (x')\rangle _{F}.$ It means that for a given training set $K=\Phi \Phi ^{\mathsf {T}}$ . Thus, the objective function can be written as $\min _{c\in \mathbb {R} ^{n}}\left\|Y-\Phi \Phi ^{\mathsf {T}}c\right\|_{\mathbb {R} ^{n}}^{2}+\lambda c^{\mathsf {T}}\Phi \Phi ^{\mathsf {T}}c.$

This approach is known as the kernel trick. This technique can significantly simplify the computational operations. If F is high dimensional, computing $\varphi (x_{i})$ may be rather intensive. If the explicit form of the kernel function is known, we just need to compute and store the $n\times n$ kernel matrix K .

In fact, the Hilbert space F need not be isomorphic to $\mathbb {R} ^{m}$ , and can be infinite dimensional. This follows from Mercer's theorem, which states that a continuous, symmetric, positive definite kernel function can be expressed as $K(x,z)=\sum _{i=1}^{\infty }\sigma _{i}e_{i}(x)e_{i}(z)$ where $e_{i}(x)$ form an orthonormal basis for $\ell ^{2}(X)$ , and $\sigma _{i}\in \mathbb {R}$ . If feature maps is defined $\varphi (x)$ with components $\varphi _{i}(x)={\sqrt {\sigma _{i}}}e_{i}(x)$ , it follows that $K(x,z)=\langle \varphi (x),\varphi (z)\rangle$ . This demonstrates that any kernel can be associated with a feature map, and that RLS generally consists of linear RLS performed in some possibly higher-dimensional feature space. While Mercer's theorem shows how one feature map that can be associated with a kernel, in fact multiple feature maps can be associated with a given reproducing kernel. For instance, the map $\varphi (x)=K_{x}$ satisfies the property $K(x,z)=\langle \varphi (x),\varphi (z)\rangle$ for an arbitrary reproducing kernel.

## Bayesian interpretation

Least squares can be viewed as a likelihood maximization under an assumption of normally distributed residuals. This is because the exponent of the Gaussian distribution is quadratic in the data, and so is the least-squares objective function. In this framework, the regularization terms of RLS can be understood to be encoding priors on w . For instance, Tikhonov regularization corresponds to a normally distributed prior on w that is centered at 0. To see this, first note that the OLS objective is proportional to the log-likelihood function when each sampled $y^{i}$ is normally distributed around $w^{\mathsf {T}}\cdot x^{i}$ . Then observe that a normal prior on w centered at 0 has a log-probability of the form $\log P(w)=q-\alpha \sum _{j=1}^{d}w_{j}^{2}$ where q and $\alpha$ are constants that depend on the variance of the prior and are independent of w . Thus, minimizing the logarithm of the likelihood times the prior is equivalent to minimizing the sum of the OLS loss function and the ridge regression regularization term.

This gives a more intuitive interpretation for why Tikhonov regularization leads to a unique solution to the least-squares problem: there are infinitely many vectors w satisfying the constraints obtained from the data, but since we come to the problem with a prior belief that w is normally distributed around the origin, we will end up choosing a solution with this constraint in mind.

Other regularization methods correspond to different priors. See the list below for more details.

## Specific methods

The following is a list of possible choices of the regularization function $R(\cdot )$ , along with the name for each one, the corresponding prior if there is a simple one, and ways for computing the solution to the resulting optimization problem.

| Name | Regularization function | Corresponding prior | Methods for solving |
|---|---|---|---|
| Tikhonov regularization | $\left\\|w\right\\|_{2}^{2}$ | Normal | Closed form |
| Lasso regression | $\left\\|w\right\\|_{1}$ | Laplace | Proximal gradient descent, least angle regression |
| $\ell _{0}$ penalization | $\left\\|w\right\\|_{0}$ | – | Forward selection, Backward elimination, use of priors such as spike and slab |
| Elastic nets | $\beta \left\\|w\right\\|_{1}+(1-\beta )\left\\|w\right\\|_{2}^{2}$ | Normal and Laplace mixture | Proximal gradient descent |
| Total variation regularization | $\sum _{j=1}^{d-1}\left\|w_{j+1}-w_{j}\right\|$ | – | Split–Bregman method, among others |

### Ridge regression (or Tikhonov regularization)

One particularly common choice for the penalty function R is the squared $\ell _{2}$ norm, i.e., $R(w)=\sum _{j=1}^{d}w_{j}^{2}$ and the solution is found as ${\hat {w}}={\text{argmin}}_{w\in \mathbb {R} ^{d}}{\frac {1}{n}}\left\|Y-Xw\right\|_{2}^{2}+\lambda \sum _{j=1}^{d}\left|w_{j}\right|^{2}$ The most common names for this are called Tikhonov regularization and ridge regression. It admits a closed-form solution for w : ${\hat {w}}=\left({\frac {1}{n}}X^{\mathsf {T}}X+\lambda I\right)^{-1}{\frac {1}{n}}X^{\mathsf {T}}Y=\left(X^{\mathsf {T}}X+n\lambda I\right)^{-1}X^{\mathsf {T}}Y$ The name ridge regression alludes to the fact that the $\lambda I$ term adds positive entries along the diagonal "ridge" of the sample covariance matrix ${\frac {1}{n}}X^{\mathsf {T}}X$ .

When $\lambda =0$ , i.e., in the case of ordinary least squares, the condition that $d>n$ causes the sample covariance matrix ${\frac {1}{n}}X^{\mathsf {T}}X$ to not have full rank and so it cannot be inverted to yield a unique solution. This is why there can be an infinitude of solutions to the ordinary least squares problem when $d>n$ . However, when $\lambda >0$ , i.e., when ridge regression is used, the addition of $\lambda I$ to the sample covariance matrix ensures that all of its eigenvalues will be strictly greater than 0. In other words, it becomes invertible, and the solution is then unique.

Compared to ordinary least squares, ridge regression is not unbiased. It accepts bias to reduce variance and the mean square error.

#### Simplifications and automatic regularization

If we want to find ${\hat {w}}$ for different values of the regularization coefficient $\lambda$ (which we denote ${\hat {w}}(\lambda )$ ) we may use the eigenvalue decomposition of the covariance matrix ${\frac {1}{n}}X^{\mathsf {T}}X=Q{\text{diag}}(\alpha _{1},\ldots ,\alpha _{d})Q^{\mathsf {T}}$ where columns of $Q\in \mathbb {R} ^{d\times d}$ are the eigenvectors of ${\frac {1}{n}}X^{\mathsf {T}}X$ and $\alpha _{1},\ldots ,\alpha _{d}$ - its d eigenvalues.

The solution in then given by ${\hat {w}}(\lambda )=Q{\text{diag}}^{-1}(\alpha _{1}+\lambda ,\ldots ,\alpha _{d}+\lambda )Z$ where $Z={\frac {1}{n}}Q^{\mathsf {T}}X^{\mathsf {T}}Y=[Z_{1},\ldots ,Z_{d}]^{\mathsf {T}}.$

Using the above results, the algorithm for finding a maximum likelihood estimate of $\lambda$ may be defined as follows:

$\lambda \leftarrow {\frac {1}{n}}\sum _{i=1}^{d}{\frac {\alpha _{i}}{\alpha _{i}+\lambda }}\left[{\frac {{\frac {1}{n}}\|Y-X{\hat {w}}(\lambda )\|^{2}}{\|{\hat {w}}(\lambda )\|^{2}}}+\lambda \right].$

This algorithm, for automatic (as opposed to heuristic) regularization, is obtained as a fixed point solution in the maximum likelihood estimation of the parameters. Although the guarantees of convergence are not provided, the examples indicate that a satisfactory solution may be obtained after a couple of iterations.

The eigenvalue decomposition simplifies derivation of the algorithm and also simplifies the calculations: $\|{\hat {w}}(\lambda )\|^{2}=\sum _{i=1}^{d}{\frac {|Z_{i}|^{2}}{(\alpha _{i}+\lambda )^{2}}},$ ${\frac {1}{n}}\|Y-X{\hat {w}}(\lambda )\|^{2}=\sum _{i=1}^{d}{\frac {|Z_{i}|^{2}}{\alpha _{i}+\lambda }}.$

An alternative fixed-point algorithm known as Gull-McKay algorithm $\lambda \leftarrow {\frac {{\frac {1}{n}}\|Y-X{\hat {w}}(\lambda )\|^{2}}{\left[{\frac {n}{\sum _{i=1}^{d}{\frac {\alpha _{i}}{\alpha _{i}+\lambda }}}}-1\right]\|{\hat {w}}(\lambda )\|^{2}}}$ usually has a faster convergence, but may be used only if $n>\sum _{i=1}^{d}{\frac {\alpha _{i}}{\alpha _{i}+\lambda }}$ . Thus, while it can be used without problems for $n>d$ caution is recommended for $n<d$ .

### Lasso regression

The least absolute selection and shrinkage (LASSO) method is another popular choice. In lasso regression, the lasso penalty function R is the $\ell _{1}$ norm, i.e. $R(w)=\sum _{j=1}^{d}\left|w_{j}\right|$ ${\frac {1}{n}}\left\|Y-Xw\right\|_{2}^{2}+\lambda \sum _{j=1}^{d}|w_{j}|\rightarrow \min _{w\in \mathbb {R} ^{d}}$

Note that the lasso penalty function is convex but not strictly convex. Unlike Tikhonov regularization, this scheme does not have a convenient closed-form solution: instead, the solution is typically found using quadratic programming or more general convex optimization methods, as well as by specific algorithms such as the least-angle regression algorithm.

An important difference between lasso regression and Tikhonov regularization is that lasso regression forces more entries of w to actually equal 0 than would otherwise. In contrast, while Tikhonov regularization forces entries of w to be small, it does not force more of them to be 0 than would be otherwise. Thus, LASSO regularization is more appropriate than Tikhonov regularization in cases in which we expect the number of non-zero entries of w to be small, and Tikhonov regularization is more appropriate when we expect that entries of w will generally be small but not necessarily zero. Which of these regimes is more relevant depends on the specific data set at hand.

Besides feature selection described above, LASSO has some limitations. Ridge regression provides better accuracy in the case $n>d$ for highly correlated variables. In another case, $n<d$ , LASSO selects at most n variables. Moreover, LASSO tends to select some arbitrary variables from group of highly correlated samples, so there is no grouping effect.

### *ℓ*0 Penalization

${\frac {1}{n}}\left\|Y-Xw\right\|_{2}^{2}+\lambda \left\|w_{j}\right\|_{0}\rightarrow \min _{w\in \mathbb {R} ^{d}}$ The most extreme way to enforce sparsity is to say that the actual magnitude of the coefficients of w does not matter; rather, the only thing that determines the complexity of w is the number of non-zero entries. This corresponds to setting $R(w)$ to be the $\ell _{0}$ norm of w . This regularization function, while attractive for the sparsity that it guarantees, is very difficult to solve because doing so requires optimization of a function that is not even weakly convex. Lasso regression is the minimal possible relaxation of $\ell _{0}$ penalization that yields a weakly convex optimization problem.

### Elastic net

For any non-negative $\lambda _{1}$ and $\lambda _{2}$ the objective has the following form: ${\frac {1}{n}}\left\|Y-Xw\right\|_{2}^{2}+\lambda _{1}\sum _{j=1}^{d}\left|w_{j}\right|+\lambda _{2}\sum _{j=1}^{d}\left|w_{j}\right|^{2}\rightarrow \min _{w\in \mathbb {R} ^{d}}$

Let $\alpha ={\frac {\lambda _{1}}{\lambda _{1}+\lambda _{2}}}$ , then the solution of the minimization problem is described as: ${\frac {1}{n}}\left\|Y-Xw\right\|_{2}^{2}\rightarrow \min _{w\in \mathbb {R} ^{d}}{\text{ s.t. }}(1-\alpha )\left\|w\right\|_{1}+\alpha \left\|w\right\|_{2}\leq t$ for some t .

Consider $(1-\alpha )\left\|w\right\|_{1}+\alpha \left\|w\right\|_{2}\leq t$ as an Elastic Net penalty function.

When $\alpha =1$ , elastic net becomes ridge regression, whereas $\alpha =0$ it becomes Lasso. $\forall \alpha \in (0,1]$ Elastic Net penalty function doesn't have the first derivative at 0 and it is strictly convex $\forall \alpha >0$ taking the properties both lasso regression and ridge regression.

One of the main properties of the Elastic Net is that it can select groups of correlated variables. The difference between weight vectors of samples $x_{i}$ and $x_{j}$ is given by: $\left|w_{i}^{*}(\lambda _{1},\lambda _{2})-w_{j}^{*}(\lambda _{1},\lambda _{2})\right|\leq {\frac {\sum _{i=1}^{n}|y_{i}|}{\lambda _{2}}}{\sqrt {2(1-\rho _{ij})}},$ where $\rho _{ij}=x_{i}^{\mathsf {T}}x_{j}$ .

If $x_{i}$ and $x_{j}$ are highly correlated ( $\rho _{ij}\to 1$ ), the weight vectors are very close. In the case of negatively correlated samples ( $\rho _{ij}\to -1$ ) the samples $-x_{j}$ can be taken. To summarize, for highly correlated variables the weight vectors tend to be equal up to a sign in the case of negative correlated variables.
