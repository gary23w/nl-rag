---
title: "Support vector machine"
source: https://en.wikipedia.org/wiki/Support_vector_machine
domain: text-classification
license: CC-BY-SA-4.0
tags: text classification, document categorization, supervised text labeling, bag of words features, class probability scoring
fetched: 2026-07-02
---

# Support vector machine

In machine learning, **support vector machines** (**SVMs**, also **support vector networks**) are supervised max-margin models with associated learning algorithms that analyze data for classification and regression analysis. Developed at AT&T Bell Laboratories, SVMs are one of the most studied models, being based on statistical learning frameworks of VC theory proposed by Vapnik (1982, 1995) and Chervonenkis (1974).

In addition to performing linear classification, SVMs can efficiently perform non-linear classification using the *kernel trick*, representing the data only through a set of pairwise similarity comparisons between the original data points using a kernel function, which transforms them into coordinates in a higher-dimensional feature space. Thus, SVMs use the kernel trick to implicitly map their inputs into high-dimensional feature spaces, where linear classification can be performed. Being max-margin models, SVMs are resilient to noisy data (e.g., misclassified examples). SVMs can also be used for regression tasks, where the objective becomes $\epsilon$ -sensitive.

The support vector clustering algorithm, created by Hava Siegelmann and Vladimir Vapnik, applies the statistics of support vectors, developed in the support vector machines algorithm, to categorize unlabeled data. These data sets require unsupervised learning approaches, which attempt to find natural clustering of the data into groups, and then to map new data according to these clusters.

The popularity of SVMs is likely due to their amenability to theoretical analysis, and their flexibility in being applied to a wide variety of tasks, including structured prediction problems. It is not clear that SVMs have better predictive performance than other linear models, such as logistic regression and linear regression.

## Motivation

Classifying data is a common task in machine learning. Suppose some given data points each belong to one of two classes, and the goal is to decide which class a *new* data point will be in. In the case of support vector machines, a data point is viewed as a p -dimensional vector (a list of p numbers), and we want to know whether we can separate such points with a $(p-1)$ -dimensional hyperplane. This is called a linear classifier. There are many hyperplanes that might classify the data. One reasonable choice as the best hyperplane is the one that represents the largest separation, or margin, between the two classes. So we choose the hyperplane so that the distance from it to the nearest data point on each side is maximized. If such a hyperplane exists, it is known as the *maximum-margin hyperplane* and the linear classifier it defines is known as a *maximum-margin classifier*; or equivalently, the *perceptron of optimal stability*.

More formally, a support vector machine constructs a hyperplane or set of hyperplanes in a high or infinite-dimensional space, which can be used for classification, regression, or other tasks like outlier detection. Intuitively, a good separation is achieved by the hyperplane that has the largest distance to the nearest training-data point of any class (so-called functional margin), since in general the larger the margin, the lower the generalization error of the classifier. A lower generalization error means that the implementer is less likely to experience overfitting.

Whereas the original problem may be stated in a finite-dimensional space, it often happens that the sets to discriminate are not linearly separable in that space. For this reason, it was proposed that the original finite-dimensional space be mapped into a much higher-dimensional space, presumably making the separation easier in that space. To keep the computational load reasonable, the mappings used by SVM schemes are designed to ensure that dot products of pairs of input data vectors may be computed easily in terms of the variables in the original space, by defining them in terms of a kernel function $k(x,y)$ selected to suit the problem. The hyperplanes in the higher-dimensional space are defined as the set of points whose dot product with a vector in that space is constant, where such a set of vectors is an orthogonal (and thus minimal) set of vectors that defines a hyperplane. The vectors defining the hyperplanes can be chosen to be linear combinations with parameters $\alpha _{i}$ of images of feature vectors $x_{i}$ that occur in the data base. With this choice of a hyperplane, the points x in the feature space that are mapped into the hyperplane are defined by the relation $\textstyle \sum _{i}\alpha _{i}k(x_{i},x)={\text{constant}}.$ Note that if $k(x,y)$ becomes small as y grows further away from x , each term in the sum measures the degree of closeness of the test point x to the corresponding data base point $x_{i}$ . In this way, the sum of kernels above can be used to measure the relative nearness of each test point to the data points originating in one or the other of the sets to be discriminated. Note the fact that the set of points x mapped into any hyperplane can be quite convoluted as a result, allowing much more complex discrimination between sets that are not convex at all in the original space.

## Applications

SVMs can be used to solve various real-world problems:

- SVMs are helpful in text and hypertext categorization, as their application can significantly reduce the need for labeled training instances in both the standard inductive and transductive settings. Some methods for shallow semantic parsing are based on support vector machines.
- Classification of images can also be performed using SVMs. Experimental results show that SVMs achieve significantly higher search accuracy than traditional query refinement schemes after just three to four rounds of relevance feedback. This is also true for image segmentation systems, including those using a modified version SVM that uses the privileged approach as suggested by Vapnik.
- Classification of satellite data like SAR data using supervised SVM.
- Hand-written characters can be recognized using SVM.
- The SVM algorithm has been widely applied in the biological and other sciences. They have been used to classify proteins with up to 90% of the compounds classified correctly. Permutation tests based on SVM weights have been suggested as a mechanism for interpretation of SVM models. Support vector machine weights have also been used to interpret SVM models in the past. Posthoc interpretation of support vector machine models in order to identify features used by the model to make predictions is a relatively new area of research with special significance in the biological sciences.

## History

The original SVM algorithm was invented by Vladimir N. Vapnik and Alexey Ya. Chervonenkis in 1964. In 1992, Bernhard Boser, Isabelle Guyon and Vladimir Vapnik suggested a way to create nonlinear classifiers by applying the kernel trick to maximum-margin hyperplanes. The "soft margin" incarnation, as is commonly used in software packages, was proposed by Corinna Cortes and Vapnik in 1993 and published in 1995.

## Linear SVM

We are given a training dataset of n points of the form $(\mathbf {x} _{1},y_{1}),\ldots ,(\mathbf {x} _{n},y_{n}),$ where the $y_{i}$ are either 1 or −1, each indicating the class to which the point $\mathbf {x} _{i}$ belongs. Each $\mathbf {x} _{i}$ is a p -dimensional real vector. We want to find the "maximum-margin hyperplane" that divides the group of points $\mathbf {x} _{i}$ for which $y_{i}=1$ from the group of points for which $y_{i}=-1$ , which is defined so that the distance between the hyperplane and the nearest point $\mathbf {x} _{i}$ from either group is maximized.

Any hyperplane can be written as the set of points $\mathbf {x}$ satisfying $\mathbf {w} ^{\mathsf {T}}\mathbf {x} -b=0,$ where $\mathbf {w}$ is the (not necessarily normalized) normal vector to the hyperplane. This is much like Hesse normal form, except that $\mathbf {w}$ is not necessarily a unit vector. The parameter ${\tfrac {b}{\|\mathbf {w} \|}}$ determines the offset of the hyperplane from the origin along the normal vector $\mathbf {w}$ .

Warning: most of the literature on the subject defines the bias so that $\mathbf {w} ^{\mathsf {T}}\mathbf {x} +b=0.$

### Hard-margin

If the training data is linearly separable, we can select two parallel hyperplanes that separate the two classes of data, so that the distance between them is as large as possible. The region bounded by these two hyperplanes is called the "margin", and the maximum-margin hyperplane is the hyperplane that lies halfway between them. With a normalized or standardized dataset, these hyperplanes can be described by the equations

$\mathbf {w} ^{\mathsf {T}}\mathbf {x} -b=1$

(anything on or above this boundary is of one class, with label 1)

and

$\mathbf {w} ^{\mathsf {T}}\mathbf {x} -b=-1$

(anything on or below this boundary is of the other class, with label −1).

Geometrically, the distance between these two hyperplanes is ${\tfrac {2}{\|\mathbf {w} \|}}$ , so to maximize the distance between the planes we want to minimize $\|\mathbf {w} \|$ . The distance is computed using the distance from a point to a plane equation. We also have to prevent data points from falling into the margin, we add the following constraint: for each i either $\mathbf {w} ^{\mathsf {T}}\mathbf {x} _{i}-b\geq 1\,,{\text{ if }}y_{i}=1,$ or $\mathbf {w} ^{\mathsf {T}}\mathbf {x} _{i}-b\leq -1\,,{\text{ if }}y_{i}=-1.$ These constraints state that each data point must lie on the correct side of the margin.

This can be rewritten as

| $y_{i}(\mathbf {w} ^{\mathsf {T}}\mathbf {x} _{i}-b)\geq 1,\quad {\text{ for all }}1\leq i\leq n.$ |   | 1 |
|---|---|---|

We can put this together to get the optimization problem:

${\begin{aligned}&{\underset {\mathbf {w} ,\;b}{\operatorname {minimize} }}&&{\frac {1}{2}}\|\mathbf {w} \|^{2}\\&{\text{subject to}}&&y_{i}(\mathbf {w} ^{\top }\mathbf {x} _{i}-b)\geq 1\quad \forall i\in \{1,\dots ,n\}\end{aligned}}$

The $\mathbf {w}$ and b that solve this problem determine the final classifier, $\mathbf {x} \mapsto \operatorname {sgn}(\mathbf {w} ^{\mathsf {T}}\mathbf {x} -b)$ , where $\operatorname {sgn}(\cdot )$ is the sign function.

An important consequence of this geometric description is that the max-margin hyperplane is completely determined by those $\mathbf {x} _{i}$ that lie nearest to it (explained below). These $\mathbf {x} _{i}$ are called *support vectors*.

### Soft-margin

To extend SVM to cases in which the data are not linearly separable, the *hinge loss* function is helpful $\max \left(0,1-y_{i}(\mathbf {w} ^{\mathsf {T}}\mathbf {x} _{i}-b)\right).$

Note that $y_{i}$ is the *i*-th target (i.e., in this case, 1 or −1), and $\mathbf {w} ^{\mathsf {T}}\mathbf {x} _{i}-b$ is the *i*-th output.

This function is zero if the constraint in **(1)** is satisfied, in other words, if $\mathbf {x} _{i}$ lies on the correct side of the margin. For data on the wrong side of the margin, the function's value is proportional to the distance from the margin.

The goal of the optimization then is to minimize:

$\lVert \mathbf {w} \rVert ^{2}+C\left[{\frac {1}{n}}\sum _{i=1}^{n}\max \left(0,1-y_{i}(\mathbf {w} ^{\mathsf {T}}\mathbf {x} _{i}-b)\right)\right],$

where the parameter $C>0$ determines the trade-off between increasing the margin size and ensuring that the $\mathbf {x} _{i}$ lie on the correct side of the margin (Note we can add a weight to either term in the equation above). By deconstructing the hinge loss, this optimization problem can be formulated into the following:

${\begin{aligned}&{\underset {\mathbf {w} ,\;b,\;\mathbf {\zeta } }{\operatorname {minimize} }}&&\|\mathbf {w} \|_{2}^{2}+C\sum _{i=1}^{n}\zeta _{i}\\&{\text{subject to}}&&y_{i}(\mathbf {w} ^{\top }\mathbf {x} _{i}-b)\geq 1-\zeta _{i},\quad \zeta _{i}\geq 0\quad \forall i\in \{1,\dots ,n\}\end{aligned}}$

Thus, for large values of C , it will behave similar to the hard-margin SVM, if the input data are linearly classifiable, but will still learn if a classification rule is viable or not.

## Nonlinear kernels

The original maximum-margin hyperplane algorithm proposed by Vapnik in 1963 constructed a linear classifier. However, in 1992, Bernhard Boser, Isabelle Guyon and Vladimir Vapnik suggested a way to create nonlinear classifiers by applying the kernel trick (originally proposed by Aizerman et al.) to maximum-margin hyperplanes. The kernel trick, where dot products are replaced by kernels, is easily derived in the dual representation of the SVM problem. This allows the algorithm to fit the maximum-margin hyperplane in a transformed feature space. The transformation may be nonlinear and the transformed space high-dimensional; although the classifier is a hyperplane in the transformed feature space, it may be nonlinear in the original input space.

It is noteworthy that working in a higher-dimensional feature space increases the generalization error of support vector machines, although given enough samples the algorithm still performs well.

Some common kernels include:

- Polynomial (homogeneous): $k(\mathbf {x} _{i},\mathbf {x} _{j})=(\mathbf {x} _{i}\cdot \mathbf {x} _{j})^{d}$ . Particularly, when $d=1$ , this becomes the linear kernel.
- Polynomial (inhomogeneous): $k(\mathbf {x} _{i},\mathbf {x} _{j})=(\mathbf {x} _{i}\cdot \mathbf {x} _{j}+r)^{d}$ .
- Gaussian radial basis function: $k(\mathbf {x} _{i},\mathbf {x} _{j})=\exp \left(-\gamma \left\|\mathbf {x} _{i}-\mathbf {x} _{j}\right\|^{2}\right)$ for $\gamma >0$ . Sometimes parametrized using $\gamma =1/(2\sigma ^{2})$ .
- Sigmoid function (Hyperbolic tangent): $k(\mathbf {x_{i}} ,\mathbf {x_{j}} )=\tanh(\kappa \mathbf {x} _{i}\cdot \mathbf {x} _{j}+c)$ for some (not every) $\kappa >0$ and $c<0$ .

The kernel is related to the transform $\varphi (\mathbf {x} _{i})$ by the equation $k(\mathbf {x} _{i},\mathbf {x} _{j})=\varphi (\mathbf {x} _{i})\cdot \varphi (\mathbf {x} _{j})$ . The value **w** is also in the transformed space, with ${\textstyle \mathbf {w} =\sum _{i}\alpha _{i}y_{i}\varphi (\mathbf {x} _{i})}$ . Dot products with **w** for classification can again be computed by the kernel trick, i.e. ${\textstyle \mathbf {w} \cdot \varphi (\mathbf {x} )=\sum _{i}\alpha _{i}y_{i}k(\mathbf {x} _{i},\mathbf {x} )}$ .

## Computing the SVM classifier

Computing the (soft-margin) SVM classifier amounts to minimizing an expression of the form

| $\left[{\frac {1}{n}}\sum _{i=1}^{n}\max \left(0,1-y_{i}(\mathbf {w} ^{\mathsf {T}}\mathbf {x} _{i}-b)\right)\right]+\lambda \\|\mathbf {w} \\|^{2}.$ |   | 2 |
|---|---|---|

We focus on the soft-margin classifier since, as noted above, choosing a sufficiently small value for $\lambda$ yields the hard-margin classifier for linearly classifiable input data. The classical approach, which involves reducing **(2)** to a quadratic programming problem, is detailed below. Then, more recent approaches such as sub-gradient descent and coordinate descent will be discussed.

### Primal

Minimizing **(2)** can be rewritten as a constrained optimization problem with a differentiable objective function in the following way.

For each $i\in \{1,\,\ldots ,\,n\}$ we introduce a variable $\zeta _{i}=\max \left(0,1-y_{i}(\mathbf {w} ^{\mathsf {T}}\mathbf {x} _{i}-b)\right)$ . Note that $\zeta _{i}$ is the smallest nonnegative number satisfying $y_{i}(\mathbf {w} ^{\mathsf {T}}\mathbf {x} _{i}-b)\geq 1-\zeta _{i}.$

Thus we can rewrite the optimization problem as follows

${\begin{aligned}&{\text{minimize }}{\frac {1}{n}}\sum _{i=1}^{n}\zeta _{i}+\lambda \|\mathbf {w} \|^{2}\\[0.5ex]&{\text{subject to }}y_{i}\left(\mathbf {w} ^{\mathsf {T}}\mathbf {x} _{i}-b\right)\geq 1-\zeta _{i}\,{\text{ and }}\,\zeta _{i}\geq 0,\,{\text{for all }}i.\end{aligned}}$

This is called the *primal* problem.

### Dual

By solving for the Lagrangian dual of the above problem, one obtains the simplified problem

${\begin{aligned}&{\text{maximize}}\,\,f(c_{1}\ldots c_{n})=\sum _{i=1}^{n}c_{i}-{\frac {1}{2}}\sum _{i=1}^{n}\sum _{j=1}^{n}y_{i}c_{i}(\mathbf {x} _{i}^{\mathsf {T}}\mathbf {x} _{j})y_{j}c_{j},\\&{\text{subject to }}\sum _{i=1}^{n}c_{i}y_{i}=0,\,{\text{and }}0\leq c_{i}\leq {\frac {1}{2n\lambda }}\;{\text{for all }}i.\end{aligned}}$

This is called the *dual* problem. Since the dual maximization problem is a quadratic function of the $c_{i}$ subject to linear constraints, it is efficiently solvable by quadratic programming algorithms.

Here, the variables $c_{i}$ are defined such that

$\mathbf {w} =\sum _{i=1}^{n}c_{i}y_{i}\mathbf {x} _{i}.$

Moreover, $c_{i}=0$ exactly when $\mathbf {x} _{i}$ lies on the correct side of the margin, and $0<c_{i}<(2n\lambda )^{-1}$ when $\mathbf {x} _{i}$ lies on the margin's boundary. It follows that $\mathbf {w}$ can be written as a linear combination of the support vectors.

The offset, b , can be recovered by finding an $\mathbf {x} _{i}$ on the margin's boundary and solving $y_{i}(\mathbf {w} ^{\mathsf {T}}\mathbf {x} _{i}-b)=1\iff b=\mathbf {w} ^{\mathsf {T}}\mathbf {x} _{i}-y_{i}.$

(Note that $y_{i}^{-1}=y_{i}$ since $y_{i}=\pm 1$ .)

### Kernel trick

Suppose now that we would like to learn a nonlinear classification rule which corresponds to a linear classification rule for the transformed data points $\varphi (\mathbf {x} _{i}).$ Moreover, we are given a kernel function k which satisfies $k(\mathbf {x} _{i},\mathbf {x} _{j})=\varphi (\mathbf {x} _{i})\cdot \varphi (\mathbf {x} _{j})$ .

We know the classification vector $\mathbf {w}$ in the transformed space satisfies

$\mathbf {w} =\sum _{i=1}^{n}c_{i}y_{i}\varphi (\mathbf {x} _{i}),$

where, the $c_{i}$ are obtained by solving the optimization problem

${\begin{aligned}{\text{maximize}}\,\,f(c_{1}\ldots c_{n})&=\sum _{i=1}^{n}c_{i}-{\frac {1}{2}}\sum _{i=1}^{n}\sum _{j=1}^{n}y_{i}c_{i}(\varphi (\mathbf {x} _{i})\cdot \varphi (\mathbf {x} _{j}))y_{j}c_{j}\\&=\sum _{i=1}^{n}c_{i}-{\frac {1}{2}}\sum _{i=1}^{n}\sum _{j=1}^{n}y_{i}c_{i}k(\mathbf {x} _{i},\mathbf {x} _{j})y_{j}c_{j}\\{\text{subject to }}\sum _{i=1}^{n}c_{i}y_{i}&=0,\,{\text{and }}0\leq c_{i}\leq {\frac {1}{2n\lambda }}\;{\text{for all }}i.\end{aligned}}$

The coefficients $c_{i}$ can be solved for using quadratic programming, as before. Again, we can find some index i such that $0<c_{i}<(2n\lambda )^{-1}$ , so that $\varphi (\mathbf {x} _{i})$ lies on the boundary of the margin in the transformed space, and then solve

${\begin{aligned}b=\mathbf {w} ^{\mathsf {T}}\varphi (\mathbf {x} _{i})-y_{i}&=\left[\sum _{j=1}^{n}c_{j}y_{j}\varphi (\mathbf {x} _{j})\cdot \varphi (\mathbf {x} _{i})\right]-y_{i}\\&=\left[\sum _{j=1}^{n}c_{j}y_{j}k(\mathbf {x} _{j},\mathbf {x} _{i})\right]-y_{i}.\end{aligned}}$

Finally,

$\mathbf {z} \mapsto \operatorname {sgn}(\mathbf {w} ^{\mathsf {T}}\varphi (\mathbf {z} )-b)=\operatorname {sgn} \left(\left[\sum _{i=1}^{n}c_{i}y_{i}k(\mathbf {x} _{i},\mathbf {z} )\right]-b\right).$

### Modern methods

Recent algorithms for finding the SVM classifier include sub-gradient descent and coordinate descent. Both techniques have proven to offer significant advantages over the traditional approach when dealing with large, sparse datasets—sub-gradient methods are especially efficient when there are many training examples, and coordinate descent when the dimension of the feature space is high.

#### Sub-gradient descent

Sub-gradient descent algorithms for the SVM work directly with the expression

$f(\mathbf {w} ,b)=\left[{\frac {1}{n}}\sum _{i=1}^{n}\max \left(0,1-y_{i}(\mathbf {w} ^{\mathsf {T}}\mathbf {x} _{i}-b)\right)\right]+\lambda \|\mathbf {w} \|^{2}.$

Note that f is a convex function of $\mathbf {w}$ and b . As such, traditional gradient descent (or SGD) methods can be adapted, where instead of taking a step in the direction of the function's gradient, a step is taken in the direction of a vector selected from the function's sub-gradient. This approach has the advantage that, for certain implementations, the number of iterations does not scale with n , the number of data points.

#### Coordinate descent

Coordinate descent algorithms for the SVM work from the dual problem

${\begin{aligned}&{\text{maximize}}\,\,f(c_{1}\ldots c_{n})=\sum _{i=1}^{n}c_{i}-{\frac {1}{2}}\sum _{i=1}^{n}\sum _{j=1}^{n}y_{i}c_{i}(x_{i}\cdot x_{j})y_{j}c_{j},\\&{\text{subject to }}\sum _{i=1}^{n}c_{i}y_{i}=0,\,{\text{and }}0\leq c_{i}\leq {\frac {1}{2n\lambda }}\;{\text{for all }}i.\end{aligned}}$

For each $i\in \{1,\,\ldots ,\,n\}$ , iteratively, the coefficient $c_{i}$ is adjusted in the direction of $\partial f/\partial c_{i}$ . Then, the resulting vector of coefficients $(c_{1}',\,\ldots ,\,c_{n}')$ is projected onto the nearest vector of coefficients that satisfies the given constraints. (Typically Euclidean distances are used.) The process is then repeated until a near-optimal vector of coefficients is obtained. The resulting algorithm is extremely fast in practice, although few performance guarantees have been proven.

## Empirical risk minimization

The soft-margin support vector machine described above is an example of an empirical risk minimization (ERM) algorithm for the *hinge loss*. Seen this way, support vector machines belong to a natural class of algorithms for statistical inference, and many of its unique features are due to the behavior of the hinge loss. This perspective can provide further insight into how and why SVMs work, and allow us to better analyze their statistical properties.

### Risk minimization

In supervised learning, one is given a set of training examples $X_{1}\ldots X_{n}$ with labels $y_{1}\ldots y_{n}$ , and wishes to predict $y_{n+1}$ given $X_{n+1}$ . To do so one forms a hypothesis, f , such that $f(X_{n+1})$ is a "good" approximation of $y_{n+1}$ . A "good" approximation is usually defined with the help of a *loss function,* $\ell (y,z)$ , which characterizes how bad z is as a prediction of y . We would then like to choose a hypothesis that minimizes the *expected risk:*

$\varepsilon (f)=\mathbb {E} \left[\ell (y_{n+1},f(X_{n+1}))\right].$

In most cases, we don't know the joint distribution of $X_{n+1},\,y_{n+1}$ outright. In these cases, a common strategy is to choose the hypothesis that minimizes the *empirical risk:*

${\hat {\varepsilon }}(f)={\frac {1}{n}}\sum _{k=1}^{n}\ell (y_{k},f(X_{k})).$

Under certain assumptions about the sequence of random variables $X_{k},\,y_{k}$ (for example, that they are generated by a finite Markov process), if the set of hypotheses being considered is small enough, the minimizer of the empirical risk will closely approximate the minimizer of the expected risk as n grows large. This approach is called *empirical risk minimization,* or ERM.

### Regularization and stability

In order for the minimization problem to have a well-defined solution, we have to place constraints on the set ${\mathcal {H}}$ of hypotheses being considered. If ${\mathcal {H}}$ is a normed space (as is the case for SVM), a particularly effective technique is to consider only those hypotheses f for which $\lVert f\rVert _{\mathcal {H}}<k$ . This is equivalent to imposing a *regularization penalty* ${\mathcal {R}}(f)=\lambda _{k}\lVert f\rVert _{\mathcal {H}}$ , and solving the new optimization problem

${\hat {f}}=\mathrm {arg} \min _{f\in {\mathcal {H}}}{\hat {\varepsilon }}(f)+{\mathcal {R}}(f).$

This approach is called *Tikhonov regularization.*

More generally, ${\mathcal {R}}(f)$ can be some measure of the complexity of the hypothesis f , so that simpler hypotheses are preferred.

### SVM and the hinge loss

Recall that the (soft-margin) SVM classifier ${\hat {\mathbf {w} }},b:\mathbf {x} \mapsto \operatorname {sgn}({\hat {\mathbf {w} }}^{\mathsf {T}}\mathbf {x} -b)$ is chosen to minimize the following expression:

$\left[{\frac {1}{n}}\sum _{i=1}^{n}\max \left(0,1-y_{i}(\mathbf {w} ^{\mathsf {T}}\mathbf {x} -b)\right)\right]+\lambda \|\mathbf {w} \|^{2}.$

In light of the above discussion, we see that the SVM technique is equivalent to empirical risk minimization with Tikhonov regularization, where in this case the loss function is the hinge loss

$\ell (y,z)=\max \left(0,1-yz\right).$

From this perspective, SVM is closely related to other fundamental classification algorithms such as regularized least-squares and logistic regression. The difference between the three lies in the choice of loss function: regularized least-squares amounts to empirical risk minimization with the square-loss, $\ell _{sq}(y,z)=(y-z)^{2}$ ; logistic regression employs the log-loss,

$\ell _{\log }(y,z)=\ln(1+e^{-yz}).$

#### Target functions

The difference between the hinge loss and these other loss functions is best stated in terms of *target functions -* the function that minimizes expected risk for a given pair of random variables $X,\,y$ .

In particular, let $y_{x}$ denote y conditional on the event that $X=x$ . In the classification setting, we have:

$y_{x}={\begin{cases}1&{\text{with probability }}p_{x}\\-1&{\text{with probability }}1-p_{x}\end{cases}}$

The optimal classifier is therefore:

$f^{*}(x)={\begin{cases}1&{\text{if }}p_{x}\geq 1/2\\-1&{\text{otherwise}}\end{cases}}$

For the square-loss, the target function is the conditional expectation function, $f_{sq}(x)=\mathbb {E} \left[y_{x}\right]$ ; For the logistic loss, it's the logit function, $f_{\log }(x)=\ln \left(p_{x}/({1-p_{x}})\right)$ . While both of these target functions yield the correct classifier, as $\operatorname {sgn}(f_{sq})=\operatorname {sgn}(f_{\log })=f^{*}$ , they give us more information than we need. In fact, they give us enough information to completely describe the distribution of $y_{x}$ .

On the other hand, one can check that the target function for the hinge loss is *exactly* $f^{*}$ . Thus, in a sufficiently rich hypothesis space—or equivalently, for an appropriately chosen kernel—the SVM classifier will converge to the simplest function (in terms of ${\mathcal {R}}$ ) that correctly classifies the data. This extends the geometric interpretation of SVM—for linear classification, the empirical risk is minimized by any function whose margins lie between the support vectors, and the simplest of these is the max-margin classifier.

## Properties

SVMs belong to a family of generalized linear classifiers and can be interpreted as an extension of the perceptron. They can also be considered a special case of Tikhonov regularization. A special property is that they simultaneously minimize the empirical *classification error* and maximize the *geometric margin*; hence they are also known as **maximum margin classifiers**.

A comparison of the SVM to other classifiers has been made by Meyer, Leisch and Hornik.

### Parameter selection

The effectiveness of SVM depends on the selection of kernel, the kernel's parameters, and soft margin parameter $\lambda$ . A common choice is a Gaussian kernel, which has a single parameter *$\gamma$*. The best combination of $\lambda$ and $\gamma$ is often selected by a grid search with exponentially growing sequences of $\lambda$ and *$\gamma$*, for example, $\lambda \in \{2^{-5},2^{-3},\dots ,2^{13},2^{15}\}$ ; $\gamma \in \{2^{-15},2^{-13},\dots ,2^{1},2^{3}\}$ . Typically, each combination of parameter choices is checked using cross validation, and the parameters with best cross-validation accuracy are picked. Alternatively, recent work in Bayesian optimization can be used to select $\lambda$ and *$\gamma$* , often requiring the evaluation of far fewer parameter combinations than grid search. The final model, which is used for testing and for classifying new data, is then trained on the whole training set using the selected parameters.

### Issues

Potential drawbacks of the SVM include the following aspects:

- Requires full labeling of input data
- Uncalibrated class membership probabilities—SVM stems from Vapnik's theory which avoids estimating probabilities on finite data
- The SVM is only directly applicable for two-class tasks. Therefore, algorithms that reduce the multi-class task to several binary problems have to be applied; see the multi-class SVM section.
- Parameters of a solved model are difficult to interpret.

## Extensions

### Multiclass SVM

Multiclass SVM aims to assign labels to instances by using support vector machines, where the labels are drawn from a finite set of several elements.

The dominant approach for doing so is to reduce the single multiclass problem into multiple binary classification problems. Common methods for such reduction include:

- Building binary classifiers that distinguish between one of the labels and the rest (*one-versus-all*) or between every pair of classes (*one-versus-one*). Classification of new instances for the one-versus-all case is done by a winner-takes-all strategy, in which the classifier with the highest-output function assigns the class (it is important that the output functions be calibrated to produce comparable scores). For the one-versus-one approach, classification is done by a max-wins voting strategy, in which every classifier assigns the instance to one of the two classes, then the vote for the assigned class is increased by one vote, and finally the class with the most votes determines the instance classification.
- Directed acyclic graph SVM (DAGSVM)
- Error-correcting output codes

Crammer and Singer proposed a multiclass SVM method which casts the multiclass classification problem into a single optimization problem, rather than decomposing it into multiple binary classification problems. See also Lee, Lin and Wahba and Van den Burg and Groenen.

### Transductive support vector machines

Transductive support vector machines extend SVMs in that they could also treat partially labeled data in semi-supervised learning by following the principles of transduction. Here, in addition to the training set ${\mathcal {D}}$ , the learner is also given a set

${\mathcal {D}}^{\star }=\{\mathbf {x} _{i}^{\star }\mid \mathbf {x} _{i}^{\star }\in \mathbb {R} ^{p}\}_{i=1}^{k}$

of test examples to be classified. Formally, a transductive support vector machine is defined by the following primal optimization problem:

Minimize (in $\mathbf {w} ,b,\mathbf {y} ^{\star }$ )

${\frac {1}{2}}\|\mathbf {w} \|^{2}$

subject to (for any $i=1,\dots ,n$ and any $j=1,\dots ,k$ )

${\begin{aligned}&y_{i}(\mathbf {w} \cdot \mathbf {x} _{i}-b)\geq 1,\\&y_{j}^{\star }(\mathbf {w} \cdot \mathbf {x} _{j}^{\star }-b)\geq 1,\end{aligned}}$

and

$y_{j}^{\star }\in \{-1,1\}.$

Transductive support vector machines were introduced by Vladimir N. Vapnik in 1998.

### Structured SVM

Structured support-vector machine is an extension of the traditional SVM model. While the SVM model is primarily designed for binary classification, multiclass classification, and regression tasks, structured SVM broadens its application to handle general structured output labels, for example parse trees, classification with taxonomies, sequence alignment and many more.

### Regression

A version of SVM for regression was proposed in 1996 by Vladimir N. Vapnik, Harris Drucker, Christopher J. C. Burges, Linda Kaufman and Alexander J. Smola. This method is called support vector regression (SVR). The model produced by support vector classification (as described above) depends only on a subset of the training data, because the cost function for building the model does not care about training points that lie beyond the margin. Analogously, the model produced by SVR depends only on a subset of the training data, because the cost function for building the model ignores any training data close to the model prediction. Another SVM version known as least-squares support vector machine (LS-SVM) has been proposed by Suykens and Vandewalle.

Training the original SVR means solving

minimize

${\tfrac {1}{2}}\|w\|^{2}$

subject to

$|y_{i}-\langle w,x_{i}\rangle -b|\leq \varepsilon$

where $x_{i}$ is a training sample with target value $y_{i}$ . The inner product plus intercept $\langle w,x_{i}\rangle +b$ is the prediction for that sample, and $\varepsilon$ is a free parameter that serves as a threshold: all predictions have to be within an $\varepsilon$ range of the true predictions. Slack variables are usually added into the above to allow for errors and to allow approximation in the case the above problem is infeasible.

### Bayesian SVM

In 2011 it was shown by Polson and Scott that the SVM admits a Bayesian interpretation through the technique of data augmentation. In this approach the SVM is viewed as a graphical model (where the parameters are connected via probability distributions). This extended view allows the application of Bayesian techniques to SVMs, such as flexible feature modeling, automatic hyperparameter tuning, and predictive uncertainty quantification. In 2017, a scalable version of the Bayesian SVM was developed by Florian Wenzel, enabling the application of Bayesian SVMs to big data. Florian Wenzel developed two different versions, a variational inference (VI) scheme for the Bayesian kernel support vector machine (SVM) and a stochastic version (SVI) for the linear Bayesian SVM.

## Implementation

The parameters of the maximum-margin hyperplane are derived by solving the optimization. There exist several specialized algorithms for quickly solving the quadratic programming (QP) problem that arises from SVMs, mostly relying on heuristics for breaking the problem down into smaller, more manageable chunks.

Another approach is to use an interior-point method that uses Newton-like iterations to find a solution of the Karush–Kuhn–Tucker conditions of the primal and dual problems. Instead of solving a sequence of broken-down problems, this approach directly solves the problem altogether. To avoid solving a linear system involving the large kernel matrix, a low-rank approximation to the matrix is often used in the kernel trick.

Another common method is Platt's sequential minimal optimization (SMO) algorithm, which breaks the problem down into 2-dimensional sub-problems that are solved analytically, eliminating the need for a numerical optimization algorithm and matrix storage. This algorithm is conceptually simple, easy to implement, generally faster, and has better scaling properties for difficult SVM problems.

The special case of linear support vector machines can be solved more efficiently by the same kind of algorithms used to optimize its close cousin, logistic regression; this class of algorithms includes sub-gradient descent (e.g., PEGASOS) and coordinate descent (e.g., LIBLINEAR). LIBLINEAR has some attractive training-time properties. Each convergence iteration takes time linear in the time taken to read the train data, and the iterations also have a Q-linear convergence property, making the algorithm extremely fast.

The general kernel SVMs can also be solved more efficiently using sub-gradient descent (e.g. P-packSVM), especially when parallelization is allowed.

Kernel SVMs are available in many machine-learning toolkits, including LIBSVM, MATLAB, SAS, SVMlight, kernlab, scikit-learn, Shogun, Weka, Shark, JKernelMachines, OpenCV and others.

Preprocessing of data (standardization) is highly recommended to enhance accuracy of classification. There are a few methods of standardization, such as min-max, normalization by decimal scaling, Z-score. Subtraction of mean and division by variance of each feature is usually used for SVM.
