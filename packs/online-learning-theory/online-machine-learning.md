---
title: "Online machine learning"
source: https://en.wikipedia.org/wiki/Online_machine_learning
domain: online-learning-theory
license: CC-BY-SA-4.0
tags: online learning theory, sequential prediction, perceptron mistake bound, multiplicative weights
fetched: 2026-07-02
---

# Online machine learning

In computer science, **online machine learning** is a method of machine learning in which data becomes available in a sequential order and is used to update the best predictor for future data at each step, as opposed to batch learning techniques which generate the best predictor by learning on the entire training data set at once. Online learning is a common technique used in areas of machine learning where it is computationally infeasible to train over the entire dataset, requiring the need of out-of-core algorithms. It is also used in situations where it is necessary for the algorithm to dynamically adapt to new patterns in the data, or when the data itself is generated as a function of time, e.g., prediction of prices in the financial international markets. Online learning algorithms may be prone to catastrophic interference, a problem that can be addressed by incremental learning approaches.

Online machine learning algorithms find applications in a wide variety of fields such as sponsored search to maximize ad revenue, portfolio optimization, shortest path prediction (with stochastic weights, e.g. traffic on roads for a maps application), spam filtering, real-time fraud detection, dynamic pricing for e-commerce, etc. There is also growing interest in usage of online learning paradigms for LLMs to enable continuous, real-time adaptation after the initial training.

## Introduction

In the setting of supervised learning, a function of $f:X\to Y$ is to be learned, where X is thought of as a space of inputs and Y as a space of outputs, that predicts well on instances that are drawn from a joint probability distribution $p(x,y)$ on $X\times Y$ . In reality, the learner never knows the true distribution $p(x,y)$ over instances. Instead, the learner usually has access to a training set of examples $(x_{1},y_{1}),\ldots ,(x_{n},y_{n})$ . In this setting, the loss function is given as $V:Y\times Y\to \mathbb {R}$ , such that $V(f(x),y)$ measures the difference between the predicted value $f(x)$ and the true value y . The ideal goal is to select a function $f\in {\mathcal {H}}$ , where ${\mathcal {H}}$ is a space of functions called a hypothesis space, so that some notion of total loss is minimized. Depending on the type of model (statistical or adversarial), one can devise different notions of loss, which lead to different learning algorithms.

## Statistical view of online learning

In statistical learning models, the training sample $(x_{i},y_{i})$ are assumed to have been drawn from the true distribution $p(x,y)$ and the objective is to minimize the expected "risk" $I[f]=\mathbb {E} [V(f(x),y)]=\int V(f(x),y)\,dp(x,y)\ .$ A common paradigm in this situation is to estimate a function ${\hat {f}}$ through empirical risk minimization or regularized empirical risk minimization (usually Tikhonov regularization). The choice of loss function here gives rise to several well-known learning algorithms such as regularized least squares and support vector machines. A purely online model in this category would learn based on just the new input $(x_{t+1},y_{t+1})$ , the current best predictor $f_{t}$ and some extra stored information (which is usually expected to have storage requirements independent of training data size). For many formulations, for example nonlinear kernel methods, true online learning is not possible, though a form of hybrid online learning with recursive algorithms can be used where $f_{t+1}$ is permitted to depend on $f_{t}$ and all previous data points $(x_{1},y_{1}),\ldots ,(x_{t},y_{t})$ . In this case, the space requirements are no longer guaranteed to be constant since it requires storing all previous data points, but the solution may take less time to compute with the addition of a new data point, as compared to batch learning techniques.

A common strategy to overcome the above issues is to learn using mini-batches, which process a small batch of $b\geq 1$ data points at a time, this can be considered as pseudo-online learning for b much smaller than the total number of training points. Mini-batch techniques are used with repeated passing over the training data to obtain optimized out-of-core versions of machine learning algorithms, for example, stochastic gradient descent. When combined with backpropagation, this is currently the de facto training method for training artificial neural networks.

### Example: linear least squares

The simple example of linear least squares is used to explain a variety of ideas in online learning. The ideas are general enough to be applied to other settings, for example, with other convex loss functions.

### Batch learning

Consider the setting of supervised learning with f being a linear function to be learned: $f(x_{j})=\langle w,x_{j}\rangle =w\cdot x_{j}$ where $x_{j}\in \mathbb {R} ^{d}$ is a vector of inputs (data points) and $w\in \mathbb {R} ^{d}$ is a linear filter vector. The goal is to compute the filter vector w . To this end, a square loss function $V(f(x_{j}),y_{j})=(f(x_{j})-y_{j})^{2}=(\langle w,x_{j}\rangle -y_{j})^{2}$ is used to compute the vector w that minimizes the empirical loss $I_{n}[w]=\sum _{j=1}^{n}V(\langle w,x_{j}\rangle ,y_{j})=\sum _{j=1}^{n}(x_{j}^{\mathsf {T}}w-y_{j})^{2}$ where $y_{j}\in \mathbb {R} .$

Let X be the $i\times d$ data matrix and $y\in \mathbb {R} ^{i}$ is the column vector of target values after the arrival of the first i data points. Assuming that the covariance matrix $\Sigma _{i}=X^{\mathsf {T}}X$ is invertible (otherwise it is preferential to proceed in a similar fashion with Tikhonov regularization), the best solution $f^{*}(x)=\langle w^{*},x\rangle$ to the linear least squares problem is given by $w^{*}=(X^{\mathsf {T}}X)^{-1}X^{\mathsf {T}}y=\Sigma _{i}^{-1}\sum _{j=1}^{i}x_{j}y_{j}.$

Now, calculating the covariance matrix $\Sigma _{i}=\sum _{j=1}^{i}x_{j}x_{j}^{\mathsf {T}}$ takes time $O(id^{2})$ , inverting the $d\times d$ matrix takes time $O(d^{3})$ , while the rest of the multiplication takes time $O(d^{2})$ , giving a total time of $O(id^{2}+d^{3})$ . When there are n total points in the dataset, to recompute the solution after the arrival of every datapoint $i=1,\ldots ,n$ , the naive approach will have a total complexity $O(n^{2}d^{2}+nd^{3})$ . Note that when storing the matrix $\Sigma _{i}$ , then updating it at each step needs only adding $x_{i+1}x_{i+1}^{\mathsf {T}}$ , which takes $O(d^{2})$ time, reducing the total time to $O(nd^{2}+nd^{3})=O(nd^{3})$ , but with an additional storage space of $O(d^{2})$ to store $\Sigma _{i}$ .

### Online learning: recursive least squares

The recursive least squares (RLS) algorithm considers an online approach to the least squares problem. It can be shown that by initialising $\textstyle w_{0}=0\in \mathbb {R} ^{d}$ and $\textstyle \Gamma _{0}=I\in \mathbb {R} ^{d\times d}$ , the solution of the linear least squares problem given in the previous section can be computed by the following iteration: $\Gamma _{i}=\Gamma _{i-1}-{\frac {\Gamma _{i-1}x_{i}x_{i}^{\mathsf {T}}\Gamma _{i-1}}{1+x_{i}^{\mathsf {T}}\Gamma _{i-1}x_{i}}}$ $w_{i}=w_{i-1}-\Gamma _{i}x_{i}\left(x_{i}^{\mathsf {T}}w_{i-1}-y_{i}\right)$ The above iteration algorithm can be proved using induction on i . The proof also shows that $\Gamma _{i}=\Sigma _{i}^{-1}$ . One can look at RLS also in the context of adaptive filters (see RLS).

The complexity for n steps of this algorithm is $O(nd^{2})$ , which is an order of magnitude faster than the corresponding batch learning complexity. The storage requirements at every step i here are to store the matrix $\Gamma _{i}$ , which is constant at $O(d^{2})$ . For the case when $\Sigma _{i}$ is not invertible, consider the regularised version of the problem loss function $\sum _{j=1}^{n}\left(x_{j}^{\mathsf {T}}w-y_{j}\right)^{2}+\lambda \left\|w\right\|_{2}^{2}$ . Then, it's easy to show that the same algorithm works with $\Gamma _{0}=(I+\lambda I)^{-1}$ , and the iterations proceed to give $\Gamma _{i}=(\Sigma _{i}+\lambda I)^{-1}$ .

### Stochastic gradient descent

When this $w_{i}=w_{i-1}-\Gamma _{i}x_{i}\left(x_{i}^{\mathsf {T}}w_{i-1}-y_{i}\right)$ is replaced by $w_{i}=w_{i-1}-\gamma _{i}x_{i}\left(x_{i}^{\mathsf {T}}w_{i-1}-y_{i}\right)=w_{i-1}-\gamma _{i}\nabla V(\langle w_{i-1},x_{i}\rangle ,y_{i})$ or $\Gamma _{i}\in \mathbb {R} ^{d\times d}$ by $\gamma _{i}\in \mathbb {R}$ , this becomes the stochastic gradient descent algorithm. In this case, the complexity for n steps of this algorithm reduces to $O(nd)$ . The storage requirements at every step i are constant at $O(d)$ .

However, the stepsize $\gamma _{i}$ needs to be chosen carefully to solve the expected risk minimization problem, as detailed above. By choosing a decaying step size $\gamma _{i}\approx {\frac {1}{\sqrt {i}}},$ one can prove the convergence of the average iterate ${\textstyle {\overline {w}}_{n}={\frac {1}{n}}\sum _{i=1}^{n}w_{i}}$ . This setting is a special case of stochastic optimization, a well known problem in optimization.

### Incremental stochastic gradient descent

In practice, one can perform multiple stochastic gradient passes (also called cycles or epochs) over the data. The algorithm thus obtained is called incremental gradient method and corresponds to an iteration $w_{i}=w_{i-1}-\gamma _{i}\nabla V(\langle w_{i-1},x_{t_{i}}\rangle ,y_{t_{i}})$ The main difference with the stochastic gradient method is that here a sequence $t_{i}$ is chosen to decide which training point is visited in the i -th step. Such a sequence can be stochastic or deterministic. The number of iterations is then decoupled to the number of points (each point can be considered more than once). The incremental gradient method can be shown to provide a minimizer to the empirical risk. Incremental techniques can be advantageous when considering objective functions made up of a sum of many terms e.g. an empirical error corresponding to a very large dataset.

### Kernel methods

Kernels can be used to extend the above algorithms to non-parametric models (or models where the parameters form an infinite dimensional space). The corresponding procedure will no longer be truly online and instead involve storing all the data points, but is still faster than the brute force method. This discussion is restricted to the case of the square loss, though it can be extended to any convex loss. It can be shown by an easy induction that if $X_{i}$ is the data matrix and $w_{i}$ is the output after i steps of the SGD algorithm, then, $w_{i}=X_{i}^{\mathsf {T}}c_{i}$ where $c_{i}=((c_{i})_{1},(c_{i})_{2},...,(c_{i})_{i})\in \mathbb {R} ^{i}$ and the sequence $c_{i}$ satisfies the recursion: $c_{0}=0$ $(c_{i})_{j}=(c_{i-1})_{j},j=1,2,...,i-1$ and $(c_{i})_{i}=\gamma _{i}{\Big (}y_{i}-\sum _{j=1}^{i-1}(c_{i-1})_{j}\langle x_{j},x_{i}\rangle {\Big )}$ Notice that here $\langle x_{j},x_{i}\rangle$ is just the standard Kernel on $\mathbb {R} ^{d}$ , and the predictor is of the form $f_{i}(x)=\langle w_{i-1},x\rangle =\sum _{j=1}^{i-1}(c_{i-1})_{j}\langle x_{j},x\rangle .$

Now, if a general kernel K is introduced instead and let the predictor be $f_{i}(x)=\sum _{j=1}^{i-1}(c_{i-1})_{j}K(x_{j},x)$ then the same proof will also show that predictor minimising the least squares loss is obtained by changing the above recursion to $(c_{i})_{i}=\gamma _{i}{\Big (}y_{i}-\sum _{j=1}^{i-1}(c_{i-1})_{j}K(x_{j},x_{i}){\Big )}$ The above expression requires storing all the data for updating $c_{i}$ . The total time complexity for the recursion when evaluating for the n -th datapoint is $O(n^{2}dk)$ , where k is the cost of evaluating the kernel on a single pair of points. Thus, the use of the kernel has allowed the movement from a finite dimensional parameter space $\textstyle w_{i}\in \mathbb {R} ^{d}$ to a possibly infinite dimensional feature represented by a kernel K by instead performing the recursion on the space of parameters $\textstyle c_{i}\in \mathbb {R} ^{i}$ , whose dimension is the same as the size of the training dataset. In general, this is a consequence of the representer theorem.

### Online convex optimization

Online convex optimization (OCO) is a general framework for decision making which leverages convex optimization to allow for efficient algorithms. The framework is that of repeated game playing as follows:

For $t=1,2,...,T$

- Learner receives input $x_{t}$
- Learner outputs $w_{t}$ from a fixed convex set S
- Nature sends back a convex loss function $v_{t}:S\rightarrow \mathbb {R}$ .
- Learner suffers loss $v_{t}(w_{t})$ and updates its model

The goal is to minimize regret, or the difference between cumulative loss and the loss of the best fixed point $u\in S$ in hindsight. As an example, consider the case of online least squares linear regression. Here, the weight vectors come from the convex set $S=\mathbb {R} ^{d}$ , and nature sends back the convex loss function $v_{t}(w)=(\langle w,x_{t}\rangle -y_{t})^{2}$ . Note here that $y_{t}$ is implicitly sent with $v_{t}$ .

Some online prediction problems however cannot fit in the framework of OCO. For example, in online classification, the prediction domain and the loss functions are not convex. In such scenarios, two simple techniques for convexification are used: randomisation and surrogate loss functions .

Some simple online convex optimisation algorithms are:

#### Follow the leader (FTL)

The simplest learning rule to try is to select (at the current step) the hypothesis that has the least loss over all past rounds. This algorithm is called Follow the leader, and round t is simply given by: $w_{t}=\mathop {\operatorname {arg\,min} } _{w\in S}\sum _{i=1}^{t-1}v_{i}(w)$ This method can thus be looked as a greedy algorithm. For the case of online quadratic optimization (where the loss function is $v_{t}(w)=\left\|w-x_{t}\right\|_{2}^{2}$ ), one can show a regret bound that grows as $\log(T)$ . However, similar bounds cannot be obtained for the FTL algorithm for other important families of models like online linear optimization. To do so, one modifies FTL by adding regularisation.

#### Follow the regularised leader (FTRL)

This is a natural modification of FTL that is used to stabilise the FTL solutions and obtain better regret bounds. A regularisation function $R:S\to \mathbb {R}$ is chosen and learning performed in round t as follows: $w_{t}=\mathop {\operatorname {arg\,min} } _{w\in S}\sum _{i=1}^{t-1}v_{i}(w)+R(w)$ As a special example, consider the case of online linear optimisation i.e. where nature sends back loss functions of the form $v_{t}(w)=\langle w,z_{t}\rangle$ . Also, let $S=\mathbb {R} ^{d}$ . Suppose the regularisation function ${\textstyle R(w)={\frac {1}{2\eta }}\left\|w\right\|_{2}^{2}}$ is chosen for some positive number $\eta$ . Then, one can show that the regret minimising iteration becomes $w_{t+1}=-\eta \sum _{i=1}^{t}z_{i}=w_{t}-\eta z_{t}$ Note that this can be rewritten as $w_{t+1}=w_{t}-\eta \nabla v_{t}(w_{t})$ , which looks exactly like online gradient descent.

If S is instead some convex subspace of $\mathbb {R} ^{d}$ , S would need to be projected onto, leading to the modified update rule $w_{t+1}=\Pi _{S}(-\eta \sum _{i=1}^{t}z_{i})=\Pi _{S}(\eta \theta _{t+1})$ This algorithm is known as lazy projection, as the vector $\theta _{t+1}$ accumulates the gradients. It is also known as Nesterov's dual averaging algorithm. In this scenario of linear loss functions and quadratic regularisation, the regret is bounded by $O({\sqrt {T}})$ , and thus the average regret goes to 0 as desired.

### Online subgradient descent (OSD)

The above proved a regret bound for linear loss functions $v_{t}(w)=\langle w,z_{t}\rangle$ . To generalise the algorithm to any convex loss function, the subgradient $\partial v_{t}(w_{t})$ of $v_{t}$ is used as a linear approximation to $v_{t}$ near $w_{t}$ , leading to the online subgradient descent algorithm:

Initialise parameter $\eta ,w_{1}=0$

For $t=1,2,...,T$

- Predict using $w_{t}$ , receive $f_{t}$ from nature.
- Choose $z_{t}\in \partial v_{t}(w_{t})$
- If $S=\mathbb {R} ^{d}$ , update as $w_{t+1}=w_{t}-\eta z_{t}$
- If $S\subset \mathbb {R} ^{d}$ , project cumulative gradients onto S i.e. $w_{t+1}=\Pi _{S}(\eta \theta _{t+1}),\theta _{t+1}=\theta _{t}+z_{t}$

One can use the OSD algorithm to derive $O({\sqrt {T}})$ regret bounds for the online version of SVM's for classification, which use the hinge loss $v_{t}(w)=\max\{0,1-y_{t}(w\cdot x_{t})\}$

### Other algorithms

Quadratically regularised FTRL algorithms lead to lazily projected gradient algorithms as described above. To use the above for arbitrary convex functions and regularisers, one uses online mirror descent. The optimal regularization in hindsight can be derived for linear loss functions, this leads to the AdaGrad algorithm. For the Euclidean regularisation, one can show a regret bound of $O({\sqrt {T}})$ , which can be improved further to a $O(\log T)$ for strongly convex and exp-concave loss functions.

## Continual learning

Continual learning means constantly improving the learned model by processing continuous streams of information. Continual learning capabilities are essential for software systems and autonomous agents interacting in an ever changing real world. However, continual learning is a challenge for machine learning and neural network models since the continual acquisition of incrementally available information from non-stationary data distributions generally leads to catastrophic forgetting.

## Interpretations of online learning

The paradigm of online learning has different interpretations depending on the choice of the learning model, each of which has distinct implications about the predictive quality of the sequence of functions $f_{1},f_{2},\ldots ,f_{n}$ . The prototypical stochastic gradient descent algorithm is used for this discussion. As noted above, its recursion is given by $w_{t}=w_{t-1}-\gamma _{t}\nabla V(\langle w_{t-1},x_{t}\rangle ,y_{t})$

The first interpretation consider the stochastic gradient descent method as applied to the problem of minimizing the expected risk $I[w]$ defined above. Indeed, in the case of an infinite stream of data, since the examples $(x_{1},y_{1}),(x_{2},y_{2}),\ldots$ are assumed to be drawn i.i.d. from the distribution $p(x,y)$ , the sequence of gradients of $V(\cdot ,\cdot )$ in the above iteration are an i.i.d. sample of stochastic estimates of the gradient of the expected risk $I[w]$ and therefore one can apply complexity results for the stochastic gradient descent method to bound the deviation $I[w_{t}]-I[w^{\ast }]$ , where $w^{\ast }$ is the minimizer of $I[w]$ . This interpretation is also valid in the case of a finite training set; although with multiple passes through the data the gradients are no longer independent, still complexity results can be obtained in special cases.

The second interpretation applies to the case of a finite training set and considers the SGD algorithm as an instance of incremental gradient descent method. In this case, one instead looks at the empirical risk: $I_{n}[w]={\frac {1}{n}}\sum _{i=1}^{n}V(\langle w,x_{i}\rangle ,y_{i})\ .$ Since the gradients of $V(\cdot ,\cdot )$ in the incremental gradient descent iterations are also stochastic estimates of the gradient of $I_{n}[w]$ , this interpretation is also related to the stochastic gradient descent method, but applied to minimize the empirical risk as opposed to the expected risk. Since this interpretation concerns the empirical risk and not the expected risk, multiple passes through the data are readily allowed and actually lead to tighter bounds on the deviations $I_{n}[w_{t}]-I_{n}[w_{n}^{\ast }]$ , where $w_{n}^{\ast }$ is the minimizer of $I_{n}[w]$ .

## Implementations

- Vowpal Wabbit: Open-source fast out-of-core online learning system which is notable for supporting a number of machine learning reductions, importance weighting and a selection of different loss functions and optimisation algorithms. It uses the hashing trick for bounding the size of the set of features independent of the amount of training data.
- scikit-learn: Provides out-of-core implementations of algorithms for
  - Classification: Perceptron, SGD classifier, Naive bayes classifier.
  - Regression: SGD Regressor, Passive Aggressive regressor.
  - Clustering: Mini-batch k-means.
  - Feature extraction: Mini-batch dictionary learning, Incremental PCA.
