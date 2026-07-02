---
title: "Elastic net regularization"
source: https://en.wikipedia.org/wiki/Elastic_net_regularization
domain: elastic-net
license: CC-BY-SA-4.0
tags: elastic net, penalized regression, regularization path, sparse model
fetched: 2026-07-02
---

# Elastic net regularization

In statistics and, in particular, in the fitting of linear or logistic regression models, the **elastic net** is a regularized regression method that linearly combines the *L*1 and *L*2 penalties of the lasso and ridge methods. Nevertheless, elastic net regularization is typically more accurate than both methods with regard to reconstruction.

## Specification

The elastic net method overcomes the limitations of the LASSO (least absolute shrinkage and selection operator) method which uses a penalty function based on

$\|\beta \|_{1}=\textstyle \sum _{j=1}^{p}|\beta _{j}|.$

Use of this penalty function has several limitations. For example, in the "large *p*, small *n*" case (high-dimensional data with few examples), the LASSO selects at most *n* variables before it saturates. Also if there is a group of highly correlated variables, then the LASSO tends to select one variable from a group and ignore the others. To overcome these limitations, the elastic net adds a quadratic part ( $\|\beta \|^{2}$ ) to the penalty, which when used alone is ridge regression (known also as Tikhonov regularization). The estimates from the elastic net method are defined by

${\hat {\beta }}\equiv {\underset {\beta }{\operatorname {argmin} }}(\|y-X\beta \|^{2}+\lambda _{2}\|\beta \|^{2}+\lambda _{1}\|\beta \|_{1}).$

The quadratic penalty term makes the loss function strongly convex, and it therefore has a unique minimum. The elastic net method includes the LASSO and ridge regression: in other words, each of them is a special case where $\lambda _{1}=\lambda ,\lambda _{2}=0$ or $\lambda _{1}=0,\lambda _{2}=\lambda$ . Meanwhile, the naive version of elastic net method finds an estimator in a two-stage procedure : first for each fixed $\lambda _{2}$ it finds the ridge regression coefficients, and then does a LASSO type shrinkage. This kind of estimation incurs a double amount of shrinkage, which leads to increased bias and poor predictions. To improve the prediction performance, sometimes the coefficients of the naive version of elastic net is rescaled by multiplying the estimated coefficients by $(1+\lambda _{2})$ .

Examples of where the elastic net method has been applied are:

- Support vector machine
- Metric learning
- Portfolio optimization
- Cancer prognosis

## Reduction to support vector machine

It was proven in 2014 that the elastic net can be reduced to the linear support vector machine. A similar reduction was previously proven for the LASSO in 2014. The authors showed that for every instance of the elastic net, an artificial binary classification problem can be constructed such that the hyper-plane solution of a linear support vector machine (SVM) is identical to the solution $\beta$ (after re-scaling). The reduction immediately enables the use of highly optimized SVM solvers for elastic net problems. It also enables the use of GPU acceleration, which is often already used for large-scale SVM solvers. The reduction is a simple transformation of the original data and regularization constants

$X\in {\mathbb {R} }^{n\times p},y\in {\mathbb {R} }^{n},\lambda _{1}\geq 0,\lambda _{2}\geq 0$

into new artificial data instances and a regularization constant that specify a binary classification problem and the SVM regularization constant

$X_{2}\in {\mathbb {R} }^{2p\times n},y_{2}\in \{-1,1\}^{2p},C\geq 0.$

Here, $y_{2}$ consists of binary labels ${-1,1}$ . When $2p>n$ it is typically faster to solve the linear SVM in the primal, whereas otherwise the dual formulation is faster. Some authors have referred to the transformation as Support Vector Elastic Net (SVEN), and provided the following MATLAB pseudo-code:

```mw
function β=SVEN(X, y, t, λ2);
    [n,p] = size(X); 
    X2 = [bsxfun(@minus, X, y./t); bsxfun(@plus, X, y./t)]’;
    Y2 = [ones(p,1);-ones(p,1)];
    if 2p > n then 
        w = SVMPrimal(X2, Y2, C = 1/(2*λ2));
        α = C * max(1-Y2.*(X2*w), 0); 
    else
        α = SVMDual(X2, Y2, C = 1/(2*λ2)); 
    end if
    β = t * (α(1:p) - α(p+1:2p)) / sum(α);
```

## Software

- "Glmnet: Lasso and elastic-net regularized generalized linear models" is a software which is implemented as an R source package and as a MATLAB toolbox. This includes fast algorithms for estimation of generalized linear models with ℓ1 (the lasso), ℓ2 (ridge regression) and mixtures of the two penalties (the elastic net) using cyclical coordinate descent, computed along a regularization path.
- JMP Pro 11 includes elastic net regularization, using the Generalized Regression personality with Fit Model.
- "pensim: Simulation of high-dimensional data and parallelized repeated penalized regression" implements an alternate, parallelised "2D" tuning method of the ℓ parameters, a method claimed to result in improved prediction accuracy.
- scikit-learn includes linear regression and logistic regression with elastic net regularization.
- SVEN, a Matlab implementation of Support Vector Elastic Net. This solver reduces the Elastic Net problem to an instance of SVM binary classification and uses a Matlab SVM solver to find the solution. Because SVM is easily parallelizable, the code can be faster than Glmnet on modern hardware.
- SpaSM, a Matlab implementation of sparse regression, classification and principal component analysis, including elastic net regularized regression.
- Apache Spark provides support for Elastic Net Regression in its MLlib machine learning library. The method is available as a parameter of the more general LinearRegression class.
- SAS (software) The SAS procedure Glmselect and SAS Viya procedure Regselect support the use of elastic net regularization for model selection.
