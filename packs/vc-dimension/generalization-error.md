---
title: "Generalization error"
source: https://en.wikipedia.org/wiki/Generalization_error
domain: vc-dimension
license: CC-BY-SA-4.0
tags: vapnik chervonenkis dimension, shattering set, growth function, sauer shelah lemma
fetched: 2026-07-02
---

# Generalization error

For supervised learning applications in machine learning and statistical learning theory, **generalization error** (also known as the **out-of-sample error** or the **risk**) is a measure of how accurately an algorithm is able to predict outcomes for previously unseen data. As learning algorithms are evaluated on finite samples, the evaluation of a learning algorithm may be sensitive to sampling error. As a result, measurements of prediction error on the current data may not provide much information about the algorithm's predictive ability on new, unseen data. The generalization error can be minimized by avoiding overfitting in the learning algorithm. The performance of machine learning algorithms is commonly visualized by learning curve plots that show estimates of the generalization error throughout the learning process.

## Definition

In a learning problem, the goal is to develop a function $f_{n}({\vec {x}})$ that predicts output values y for each input datum ${\vec {x}}$ . The subscript n indicates that the function $f_{n}$ is developed based on a data set of n data points. The **generalization error** or **expected loss** or **risk** $I[f]$ of a particular function f over all possible values of ${\vec {x}}$ and y is the expected value of the loss function $V(f)$ :

$I[f]=\int _{X\times Y}V(f({\vec {x}}),y)\rho ({\vec {x}},y)d{\vec {x}}dy,$

where $\rho ({\vec {x}},y)$ is the unknown joint probability distribution for ${\vec {x}}$ and y .

Without knowing the joint probability distribution $\rho$ , it is impossible to compute $I[f]$ . Instead, we can compute the error on sample data, which is called **empirical error** (or **empirical risk**). Given n data points, the empirical error of a candidate function f is:

$I_{n}[f]={\frac {1}{n}}\sum _{i=1}^{n}V(f({\vec {x}}_{i}),y_{i})$

An algorithm is said to generalize if:

$\lim _{n\rightarrow \infty }I[f]-I_{n}[f]=0$

Of particular importance is the **generalization error** $I[f_{n}]$ of the data-dependent function $f_{n}$ that is found by a learning algorithm based on the sample. Again, for an unknown probability distribution, $I[f_{n}]$ cannot be computed. Instead, the aim of many problems in statistical learning theory is to bound or characterize the difference of the generalization error and the empirical error in probability:

$P_{G}=P(I[f_{n}]-I_{n}[f_{n}]\leq \epsilon )\geq 1-\delta _{n}$

That is, the goal is to characterize the probability $1-\delta _{n}$ that the generalization error is less than the empirical error plus some error bound $\epsilon$ (generally dependent on $\delta$ and n ). For many types of algorithms, it has been shown that an algorithm has generalization bounds if it meets certain stability criteria. Specifically, if an algorithm is symmetric (the order of inputs does not affect the result), has bounded loss and meets two stability conditions, it will generalize. The first stability condition, leave-one-out cross-validation stability, says that to be stable, the prediction error for each data point when leave-one-out cross validation is used must converge to zero as $n\rightarrow \infty$ . The second condition, expected-to-leave-one-out error stability (also known as hypothesis stability if operating in the $L_{1}$ norm) is met if the prediction on a left-out datapoint does not change when a single data point is removed from the training dataset.

These conditions can be formalized as:

### Leave-one-out cross-validation Stability

An algorithm L has $CVloo$ stability if for each n , there exists a $\beta _{CV}^{(n)}$ and $\delta _{CV}^{(n)}$ such that:

$\forall i\in \{1,...,n\},\mathbb {P} _{S}\{|V(f_{S^{i}},z_{i})-V(f_{S},z_{i})|\leq \beta _{CV}^{(n)}\}\geq 1-\delta _{CV}^{(n)}$

and $\beta _{CV}^{(n)}$ and $\delta _{CV}^{(n)}$ go to zero as n goes to infinity.

### Expected-leave-one-out error Stability

An algorithm L has $Eloo_{err}$ stability if for each n there exists a $\beta _{EL}^{m}$ and a $\delta _{EL}^{m}$ such that:

$\forall i\in \{1,...,n\},\mathbb {P} _{S}\left\{\left|I[f_{S}]-{\frac {1}{n}}\sum _{i=1}^{N}V\left(f_{S^{i}},z_{i}\right)\right|\leq \beta _{EL}^{(n)}\right\}\geq 1-\delta _{EL}^{(n)}$

with $\beta _{EL}^{(n)}$ and $\delta _{EL}^{(n)}$ going to zero for $n\rightarrow \infty$ .

For leave-one-out stability in the $L_{1}$ norm, this is the same as hypothesis stability:

$\mathbb {E} _{S,z}[|V(f_{S},z)-V(f_{S^{i}},z)|]\leq \beta _{H}^{(n)}$

with $\beta _{H}^{(n)}$ going to zero as n goes to infinity.

### Algorithms with proven stability

A number of algorithms have been proven to be stable and as a result have bounds on their generalization error. A list of these algorithms and the papers that proved stability is available here.

## Relation to overfitting

The concepts of generalization error and overfitting are closely related. Overfitting occurs when the learned function $f_{S}$ becomes sensitive to the noise in the sample. As a result, the function will perform well on the training set but not perform well on other data from the joint probability distribution of x and y . Thus, the more overfitting occurs, the larger the generalization error.

The amount of overfitting can be tested using cross-validation methods, that split the sample into simulated training samples and testing samples. The model is then trained on a training sample and evaluated on the testing sample. The testing sample is previously unseen by the algorithm and so represents a random sample from the joint probability distribution of x and y . This test sample allows us to approximate the expected error and as a result approximate a particular form of the generalization error.

Many algorithms exist to prevent overfitting. The minimization algorithm can penalize more complex functions (known as Tikhonov regularization), or the hypothesis space can be constrained, either explicitly in the form of the functions or by adding constraints to the minimization function (Ivanov regularization).

The approach to finding a function that does not overfit is at odds with the goal of finding a function that is sufficiently complex to capture the particular characteristics of the data. This is known as the bias–variance tradeoff. Keeping a function simple to avoid overfitting may introduce a bias in the resulting predictions, while allowing it to be more complex leads to overfitting and a higher variance in the predictions. It is impossible to minimize both simultaneously.
