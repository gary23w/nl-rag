---
title: "Gradient boosting"
source: https://en.wikipedia.org/wiki/Gradient_boosting
domain: boosting-theory
license: CC-BY-SA-4.0
tags: boosting meta algorithm, weak learner, adaboost algorithm, margin theory
fetched: 2026-07-02
---

# Gradient boosting

**Gradient boosting** is a machine learning technique based on boosting in a functional space, where the target is *pseudo-residuals* instead of residuals as in traditional boosting. It gives a prediction model in the form of an ensemble of weak prediction models, i.e., models that make very few assumptions about the data, which are typically simple decision trees. When a decision tree is the weak learner, the resulting algorithm is called gradient-boosted trees; it usually outperforms random forest. As with other boosting methods, a gradient-boosted trees model is built in stages, but it generalizes the other methods by allowing optimization of an arbitrary differentiable loss function.

## History

The idea of gradient boosting originated in the observation by Leo Breiman that boosting can be interpreted as an optimization algorithm on a suitable cost function. Explicit regression gradient boosting algorithms were subsequently developed, by Jerome H. Friedman, (in 1999 and later in 2001) simultaneously with the more general functional gradient boosting perspective of Llew Mason, Jonathan Baxter, Peter Bartlett and Marcus Frean. The latter two papers introduced the view of boosting algorithms as iterative *functional gradient descent* algorithms. That is, algorithms that optimize a cost function over function space by iteratively choosing a function (weak hypothesis) that points in the negative gradient direction. This functional gradient view of boosting has led to the development of boosting algorithms in many areas of machine learning and statistics beyond regression and classification.

## Informal introduction

(This section follows the exposition by Cheng Li.)

Like other boosting methods, gradient boosting combines weak "learners" into a single strong learner iteratively. It is easiest to explain in the least-squares regression setting, where the goal is to teach a model F to predict values of the form ${\hat {y}}=F(x)$ by minimizing the mean squared error ${\tfrac {1}{n}}\sum _{i}({\hat {y}}_{i}-y_{i})^{2}$ , where i indexes over some training set of size n of actual values of the output variable y :

- ${\hat {y}}_{i}=$ the predicted value $F(x_{i})$
- $y_{i}=$ the observed value
- $n=$ the size of the sample, i.e. the number of observations in y

If the algorithm has M stages, at each stage m ( $1\leq m\leq M$ ), suppose some imperfect model $F_{m}$ (for low m , this model may simply predict ${\hat {y}}_{i}$ to be ${\bar {y}}$ , the mean of y ). In order to improve $F_{m}$ , our algorithm should add some new estimator, $h_{m}(x)$ . Thus,

$F_{m+1}(x_{i})=F_{m}(x_{i})+h_{m}(x_{i})=y_{i}$

or, equivalently,

$h_{m}(x_{i})=y_{i}-F_{m}(x_{i}).$

Therefore, gradient boosting will fit $h_{m}$ to the *residual* $y_{i}-F_{m}(x_{i})$ . As in other boosting variants, each $F_{m+1}$ attempts to correct the errors of its predecessor $F_{m}$ . A generalization of this idea to loss functions other than squared error, and to classification and ranking problems, follows from the observation that residuals $h_{m}(x_{i})$ for a given model are proportional to the negative gradients of the mean squared error (MSE) loss function (with respect to $F(x_{i})$ ):

$L_{\rm {MSE}}={\frac {1}{n}}\sum _{i=1}^{n}\left(y_{i}-F(x_{i})\right)^{2}$

$-{\frac {\partial L_{\rm {MSE}}}{\partial F(x_{i})}}={\frac {2}{n}}(y_{i}-F(x_{i}))={\frac {2}{n}}h_{m}(x_{i}).$

So, gradient boosting could be generalized to a gradient descent algorithm by plugging in a different loss and its gradient.

## Algorithm

Many supervised learning problems involve an output variable y and a vector of input variables x, related to each other with some probabilistic distribution. The goal is to find some function ${\hat {F}}(x)$ that best approximates the output variable from the values of input variables. This is formalized by introducing some loss function $L(y,F(x))$ and minimizing it in expectation:

${\hat {F}}=\operatorname {argmin} \limits _{F}\mathbb {E} _{x,y}[L(y,F(x))].$

The gradient boosting method assumes a real-valued y. It seeks an approximation ${\hat {F}}(x)$ in the form of a weighted sum of M functions $h_{m}(x)$ from some class ${\mathcal {H}}$ , called base (or weak) learners:

${\hat {F}}(x)=\sum _{m=1}^{M}\gamma _{m}h_{m}(x)+{\mbox{const}},$

where $\gamma _{m}$ is the weight at stage m . We are usually given a training set $\{(x_{1},y_{1}),\dots ,(x_{n},y_{n})\}$ of known values of x and corresponding values of y. In accordance with the empirical risk minimization principle, the method tries to find an approximation ${\hat {F}}(x)$ that minimizes the average value of the loss function on the training set, i.e., minimizes the empirical risk. It does so by starting with a model, consisting of a constant function $F_{0}(x)$ , and incrementally expands it in a greedy fashion:

$F_{0}(x)={\underset {h_{m}\in {\mathcal {H}}}{\arg \min }}\sum _{i=1}^{n}{L(y_{i},h_{m}(x_{i}))},$

$F_{m}(x)=F_{m-1}(x)+\left({\underset {h_{m}\in {\mathcal {H}}}{\operatorname {arg\,min} }}\left[\sum _{i=1}^{n}L(y_{i},F_{m-1}(x_{i})+h_{m}(x_{i}))\right]\right)(x),$

for $m\geq 1$ , where $h_{m}\in {\mathcal {H}}$ is a base learner function.

Unfortunately, choosing the best function $h_{m}$ at each step for an arbitrary loss function L is a computationally infeasible optimization problem in general. Therefore, we restrict our approach to a simplified version of the problem. The idea is to apply a steepest descent step to this minimization problem (functional gradient descent). The basic idea is to find a local minimum of the loss function by iterating on $F_{m-1}(x)$ . In fact, the local maximum-descent direction of the loss function is the negative gradient. Hence, moving a small amount $\gamma$ such that the linear approximation remains valid:

$F_{m}(x)=F_{m-1}(x)-\gamma \sum _{i=1}^{n}\nabla _{F_{m-1}}L(y_{i},F_{m-1}(x_{i}))$

where $\gamma >0$ . For small $\gamma$ , this implies that $L(y_{i},F_{m}(x_{i}))\leq L(y_{i},F_{m-1}(x_{i}))$ .

| Proof of functional form of derivative |
|---|
| To prove the following, consider the objective $O=\sum _{i=1}^{n}L(y_{i},F_{m-1}(x_{i})+h_{m}(x_{i}))$ Doing a Taylor expansion around the fixed point $F_{m-1}(x_{i})$ up to first order $O=\sum _{i=1}^{n}L(y_{i},F_{m-1}(x_{i})+h_{m}(x_{i}))\approx \sum _{i=1}^{n}L(y_{i},F_{m-1}(x_{i}))+h_{m}(x_{i})\nabla _{F_{m-1}L(y_{i},F_{m-1}(x_{i}))}+\cdots$ Now differentiating w.r.t. $h_{m}(x_{i})$ , only the derivative of the second term remains $\nabla _{F_{m-1}}L(y_{i},F_{m-1}(x_{i}))$ . This is the direction of steepest ascent and hence we must move in the opposite (i.e., negative) direction in order to move in the direction of steepest descent. |

Furthermore, we can optimize $\gamma$ by finding the $\gamma$ value for which the loss function has a minimum:

$\gamma _{m}={\underset {\gamma }{\operatorname {argmin} }}\sum _{i=1}^{n}L(y_{i},F_{m}(x_{i}))={\underset {\gamma }{\arg \min }}{\sum _{i=1}^{n}L\left(y_{i},F_{m-1}(x_{i})-\gamma \nabla _{F_{m-1}}L(y_{i},F_{m-1}(x_{i}))\right)}.$

If we considered the continuous case, i.e., where ${\mathcal {H}}$ is the set of arbitrary differentiable functions on $\mathbb {R}$ , we would update the model in accordance with the following equations

$F_{m}(x)=F_{m-1}(x)-\gamma _{m}\sum _{i=1}^{n}{\nabla _{F_{m-1}}L(y_{i},F_{m-1}(x_{i}))}$

where $\gamma _{m}$ is the step length, defined as $\gamma _{m}={\underset {\gamma }{\arg \min }}\sum _{i=1}^{n}L\left(y_{i},F_{m-1}(x_{i})-\gamma \nabla _{F_{m-1}}L(y_{i},F_{m-1}(x_{i}))\right).$ In the discrete case however, i.e. when the set ${\mathcal {H}}$ is finite, we choose the candidate function h closest to the gradient of L for which the coefficient γ may then be calculated with the aid of line search on the above equations. Note that this approach is a heuristic and therefore doesn't yield an exact solution to the given problem, but rather an approximation. In pseudocode, the generic gradient boosting method is:

Input: training set $\{(x_{i},y_{i})\}_{i=1}^{n},$ a differentiable loss function $L(y,F(x)),$ number of iterations M.

Algorithm:

1. Initialize model with a constant value: $F_{0}(x)={\underset {\gamma }{\arg \min }}\sum _{i=1}^{n}L(y_{i},\gamma ).$
2. For m = 1 to M:
  1. Compute so-called *pseudo-residuals*: $r_{im}=-\left[{\frac {\partial L(y_{i},F(x_{i}))}{\partial F(x_{i})}}\right]_{F(x)=F_{m-1}(x)}\quad {\text{for }}i=1,\ldots ,n.$
  2. Fit a base learner (or weak learner, e.g. tree) closed under scaling $h_{m}(x)$ to pseudo-residuals, i.e. train it using the training set $\{(x_{i},r_{im})\}_{i=1}^{n}$ .
  3. Compute multiplier $\gamma _{m}$ by solving the following one-dimensional optimization problem: $\gamma _{m}={\underset {\gamma }{\operatorname {argmin} }}\sum _{i=1}^{n}L\left(y_{i},F_{m-1}(x_{i})+\gamma h_{m}(x_{i})\right).$
  4. Update the model: $F_{m}(x)=F_{m-1}(x)+\gamma _{m}h_{m}(x).$
3. Output $F_{M}(x).$

## Gradient tree boosting

Gradient boosting is typically used with decision trees (especially CARTs) of a fixed size as base learners. For this special case, Friedman proposes a modification to gradient boosting method which improves the quality of fit of each base learner.

Generic gradient boosting at the *m*-th step would fit a decision tree $h_{m}(x)$ to pseudo-residuals. Let $J_{m}$ be the number of its leaves. The tree partitions the input space into $J_{m}$ disjoint regions $R_{1m},\ldots ,R_{J_{m}m}$ and predicts a constant value in each region. Using the indicator notation, the output of $h_{m}(x)$ for input *x* can be written as the sum:

$h_{m}(x)=\sum _{j=1}^{J_{m}}b_{jm}\mathbf {1} _{R_{jm}}(x),$

where $b_{jm}$ is the value predicted in the region $R_{jm}$ .

Then the coefficients $b_{jm}$ are multiplied by some value $\gamma _{m}$ , chosen using line search so as to minimize the loss function, and the model is updated as follows:

$F_{m}(x)=F_{m-1}(x)+\gamma _{m}h_{m}(x),\quad \gamma _{m}={\underset {\gamma }{\operatorname {arg\,min} }}\sum _{i=1}^{n}L(y_{i},F_{m-1}(x_{i})+\gamma h_{m}(x_{i})).$

Friedman proposes to modify this algorithm so that it chooses a separate optimal value $\gamma _{jm}$ for each of the tree's regions, instead of a single $\gamma _{m}$ for the whole tree. He calls the modified algorithm "TreeBoost". The coefficients $b_{jm}$ from the tree-fitting procedure can be then simply discarded and the model update rule becomes:

$F_{m}(x)=F_{m-1}(x)+\sum _{j=1}^{J_{m}}\gamma _{jm}\mathbf {1} _{R_{jm}}(x),\quad \gamma _{jm}={\underset {\gamma }{\operatorname {arg\,min} }}\sum _{x_{i}\in R_{jm}}L(y_{i},F_{m-1}(x_{i})+\gamma ).$

When the loss $L(\cdot ,\cdot )$ is mean-squared error (MSE) the coefficients $\gamma _{jm}$ coincide with the coefficients of the tree-fitting procedure $b_{jm}$ .

### Tree size

The number J of terminal nodes in the trees is a parameter which controls the maximum allowed level of interaction between variables in the model. With $J=2$ (decision stumps), no interaction between variables is allowed. With $J=3$ the model may include effects of the interaction between up to two variables, and so on. J can be adjusted for a data set at hand.

Hastie et al. comment that typically $4\leq J\leq 8$ work well for boosting and results are fairly insensitive to the choice of J in this range, $J=2$ is insufficient for many applications, and $J>10$ is unlikely to be required.

## Regularization

Fitting the training set too closely can lead to degradation of the model's generalization ability, that is, its performance on unseen examples. Several so-called regularization techniques reduce this overfitting effect by constraining the fitting procedure.

One natural regularization parameter is the number of gradient boosting iterations *M* (i.e. the number of base models). Increasing *M* reduces the error on training set, but increases risk of overfitting. An optimal value of *M* is often selected by monitoring prediction error on a separate validation data set.

Another regularization parameter for tree boosting is tree depth. The higher this value the more likely the model will overfit the training data.

### Shrinkage

An important part of gradient boosting is regularization by shrinkage which uses a modified update rule:

$F_{m}(x)=F_{m-1}(x)+\nu \cdot \gamma _{m}h_{m}(x),\quad 0<\nu \leq 1,$

where parameter $\nu$ is called the "learning rate".

Empirically, it has been found that using small learning rates (such as $\nu <0.1$ ) yields dramatic improvements in models' generalization ability over gradient boosting without shrinking ( $\nu =1$ ). However, it comes at the price of increasing computational time both during training and querying: lower learning rate requires more iterations.

### Stochastic gradient boosting

Soon after the introduction of gradient boosting, Friedman proposed a minor modification to the algorithm, motivated by Breiman's bootstrap aggregation ("bagging") method. Specifically, he proposed that at each iteration of the algorithm, a base learner should be fit on a subsample of the training set drawn at random without replacement. Friedman observed a substantial improvement in gradient boosting's accuracy with this modification.

Subsample size is some constant fraction f of the size of the training set. When $f=1$ , the algorithm is deterministic and identical to the one described above. Smaller values of f introduce randomness into the algorithm and help prevent overfitting, acting as a kind of regularization. The algorithm also becomes faster, because regression trees have to be fit to smaller datasets at each iteration. Friedman obtained that $0.5\leq f\leq 0.8$ leads to good results for small and moderate sized training sets. Therefore, f is typically set to 0.5, meaning that one half of the training set is used to build each base learner.

Also, like in bagging, subsampling allows one to define an out-of-bag error of the prediction performance improvement by evaluating predictions on those observations which were not used in the building of the next base learner. Out-of-bag estimates help avoid the need for an independent validation dataset, but often underestimate actual performance improvement and the optimal number of iterations.

### Number of observations in leaves

Gradient tree boosting implementations often also use regularization by limiting the minimum number of observations in trees' terminal nodes. It is used in the tree building process by ignoring any splits that lead to nodes containing fewer than this number of training set instances.

Imposing this limit helps to reduce variance in predictions at leaves.

### Complexity penalty

Another useful regularization technique for gradient boosted model is to penalize its complexity. For gradient boosted trees, model complexity can be defined as the proportional number of leaves in the trees. The joint optimization of loss and model complexity corresponds to a post-pruning algorithm to remove branches that fail to reduce the loss by a threshold.

Other kinds of regularization such as an $\ell _{2}$ penalty on the leaf values can also be used to avoid overfitting.

## Usage

Gradient boosting can be used in the field of learning to rank. The commercial web search engines Yahoo and Yandex use variants of gradient boosting in their machine-learned ranking engines. Gradient boosting is also utilized in High Energy Physics in data analysis. At the Large Hadron Collider (LHC), variants of gradient boosting Deep Neural Networks (DNN) were successful in reproducing the results of non-machine learning methods of analysis on datasets used to discover the Higgs boson. Gradient boosting decision tree was also applied in earth and geological studies – for example quality evaluation of sandstone reservoir.

## Names

The method goes by a variety of names. Friedman introduced his regression technique as a "Gradient Boosting Machine" (GBM). Mason, Baxter et al. described the generalized abstract class of algorithms as "functional gradient boosting". Friedman et al. describe an advancement of gradient boosted models as Multiple Additive Regression Trees (MART); Elith et al. describe that approach as "Boosted Regression Trees" (BRT).

A popular open-source implementation for R calls it a "Generalized Boosting Model", however packages expanding this work use BRT. Yet another name is TreeNet, after an early commercial implementation from Salford System's Dan Steinberg, one of researchers who pioneered the use of tree-based methods.

## Feature importance ranking

Gradient boosting can be used for feature importance ranking, which is usually based on aggregating importance function of the base learners. For example, if a gradient boosted trees algorithm is developed using entropy-based decision trees, the ensemble algorithm ranks the importance of features based on entropy as well with the caveat that it is averaged out over all base learners.

## Disadvantages

While boosting can increase the accuracy of a base learner, such as a decision tree or linear regression, it sacrifices intelligibility and interpretability. For example, following the path that a decision tree takes to make its decision is trivial and self-explained, but following the paths of hundreds or thousands of trees is much harder. To achieve both performance and interpretability, some model compression techniques allow transforming an XGBoost into a single "born-again" decision tree that approximates the same decision function. Furthermore, its implementation may be more difficult due to the higher computational demand.
