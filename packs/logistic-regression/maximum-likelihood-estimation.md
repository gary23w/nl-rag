---
title: "Maximum likelihood estimation"
source: https://en.wikipedia.org/wiki/Maximum_likelihood_estimation
domain: logistic-regression
license: CC-BY-SA-4.0
tags: logistic regression, logit, odds ratio, probit model
fetched: 2026-07-02
---

# Maximum likelihood estimation

In statistics, **maximum likelihood estimation** (**MLE**) is a method of estimating the parameters of an assumed probability distribution, given some observed data. This is achieved by maximizing a likelihood function so that, under the assumed statistical model, the observed data is most probable. The point in the parameter space that maximizes the likelihood function is called the maximum likelihood estimate. The logic of maximum likelihood is both intuitive and flexible, and as such the method has become a dominant means of statistical inference.

If the likelihood function is differentiable, the derivative test for finding maxima can be applied. In some cases, the first-order conditions of the likelihood function can be solved analytically; for instance, the ordinary least squares estimator for a linear regression model maximizes the likelihood when the random errors are assumed to have normal distributions with the same variance.

From the perspective of Bayesian inference, MLE is generally equivalent to maximum a posteriori (MAP) estimation with a prior distribution that is uniform in the region of interest. In frequentist inference, MLE is a special case of an extremum estimator, with the objective function being the likelihood.

## Principles

We model a set of observations as a random sample from an unknown joint probability distribution which is expressed in terms of a set of parameters. The goal of maximum likelihood estimation is to determine the parameters for which the observed data have the highest joint probability. We write the parameters governing the joint distribution as a vector $\;\theta =\left[\theta _{1},\,\theta _{2},\,\ldots ,\,\theta _{k}\right]^{\mathsf {T}}\;$ so that this distribution falls within a parametric family $\;\{f(\cdot \,;\theta )\mid \theta \in \Theta \}\;,$ where $\,\Theta \,$ is called the *parameter space*, a finite-dimensional subset of Euclidean space. Evaluating the joint density at the observed data sample $\;\mathbf {y} =(y_{1},y_{2},\ldots ,y_{n})\;$ gives a real-valued function, ${\mathcal {L}}_{n}(\theta )={\mathcal {L}}_{n}(\theta ;\mathbf {y} )=f_{n}(\mathbf {y} ;\theta )\;,$ which is called the likelihood function. For independent random variables, $f_{n}(\mathbf {y} ;\theta )$ will be the product of univariate density functions: $f_{n}(\mathbf {y} ;\theta )=\prod _{k=1}^{n}\,f_{k}^{\mathsf {univar}}(y_{k};\theta )~.$

The goal of maximum likelihood estimation is to find the values of the model parameters that maximize the likelihood function over the parameter space, that is: ${\hat {\theta }}={\underset {\theta \in \Theta }{\operatorname {arg\;max} }}\,{\mathcal {L}}_{n}(\theta \,;\mathbf {y} )~.$

Intuitively, this selects the parameter values that make the observed data most probable. The specific value $~{\hat {\theta }}={\hat {\theta }}_{n}(\mathbf {y} )\in \Theta ~$ that maximizes the likelihood function $\,{\mathcal {L}}_{n}\,$ is called the maximum likelihood estimate. Further, if the function $\;{\hat {\theta }}_{n}:\mathbb {R} ^{n}\to \Theta \;$ so defined is measurable, then it is called the maximum likelihood estimator. It is generally a function defined over the sample space, i.e. taking a given sample as its argument. A sufficient but not necessary condition for its existence is for the likelihood function to be continuous over a parameter space $\,\Theta \,$ that is compact. For an open $\,\Theta \,$ the likelihood function may increase without ever reaching a supremum value.

In practice, it is often convenient to work with the natural logarithm of the likelihood function, called the log-likelihood: $\ell (\theta \,;\mathbf {y} )=\ln {\mathcal {L}}_{n}(\theta \,;\mathbf {y} )~.$ Since the logarithm is a monotonic function, the maximum of $\;\ell (\theta \,;\mathbf {y} )\;$ occurs at the same value of $\theta$ as does the maximum of $\,{\mathcal {L}}_{n}~.$ If $\ell (\theta \,;\mathbf {y} )$ is differentiable in $\,\Theta \,,$ necessary conditions for the occurrence of a maximum (or a minimum) are ${\frac {\partial \ell }{\partial \theta _{1}}}=0,\quad {\frac {\partial \ell }{\partial \theta _{2}}}=0,\quad \ldots ,\quad {\frac {\partial \ell }{\partial \theta _{k}}}=0~,$ known as the likelihood equations. For some models, these equations can be explicitly solved for $\,{\widehat {\theta \,}}\,,$ but in general no closed-form solution to the maximization problem is known or available, and an MLE can only be found via numerical optimization. Another problem is that in finite samples, there may exist multiple roots for the likelihood equations. Whether the identified root $\,{\widehat {\theta \,}}\,$ of the likelihood equations is indeed a (local) maximum depends on whether the matrix of second-order partial and cross-partial derivatives, the so-called Hessian matrix

$\mathbf {H} \left({\widehat {\theta \,}}\right)={\begin{bmatrix}\left.{\frac {\partial ^{2}\ell }{\partial \theta _{1}^{2}}}\right|_{\theta ={\widehat {\theta \,}}}&\left.{\frac {\partial ^{2}\ell }{\partial \theta _{1}\,\partial \theta _{2}}}\right|_{\theta ={\widehat {\theta \,}}}&\dots &\left.{\frac {\partial ^{2}\ell }{\partial \theta _{1}\,\partial \theta _{k}}}\right|_{\theta ={\widehat {\theta \,}}}\\\left.{\frac {\partial ^{2}\ell }{\partial \theta _{2}\,\partial \theta _{1}}}\right|_{\theta ={\widehat {\theta \,}}}&\left.{\frac {\partial ^{2}\ell }{\partial \theta _{2}^{2}}}\right|_{\theta ={\widehat {\theta \,}}}&\dots &\left.{\frac {\partial ^{2}\ell }{\partial \theta _{2}\,\partial \theta _{k}}}\right|_{\theta ={\widehat {\theta \,}}}\\\vdots &\vdots &\ddots &\vdots \\\left.{\frac {\partial ^{2}\ell }{\partial \theta _{k}\,\partial \theta _{1}}}\right|_{\theta ={\widehat {\theta \,}}}&\left.{\frac {\partial ^{2}\ell }{\partial \theta _{k}\,\partial \theta _{2}}}\right|_{\theta ={\widehat {\theta \,}}}&\dots &\left.{\frac {\partial ^{2}\ell }{\partial \theta _{k}^{2}}}\right|_{\theta ={\widehat {\theta \,}}}\end{bmatrix}}~,$

is negative semi-definite at ${\widehat {\theta \,}}$ , as this indicates local concavity. Conveniently, most common probability distributions – in particular the exponential family – are logarithmically concave.

### Restricted parameter space

While the domain of the likelihood function—the parameter space—is generally a finite-dimensional subset of Euclidean space, additional restrictions sometimes need to be incorporated into the estimation process. The parameter space can be expressed as $\Theta =\left\{\theta :\theta \in \mathbb {R} ^{k},\;h(\theta )=0\right\}~,$

where $\;h(\theta )=\left[h_{1}(\theta ),h_{2}(\theta ),\ldots ,h_{r}(\theta )\right]\;$ is a vector-valued function mapping $\,\mathbb {R} ^{k}\,$ into $\;\mathbb {R} ^{r}~.$ Estimating the true parameter $\theta$ belonging to $\Theta$ then, as a practical matter, means to find the maximum of the likelihood function subject to the constraint $~h(\theta )=0~.$

Theoretically, the most natural approach to this constrained optimization problem is the method of substitution, that is "filling out" the restrictions $\;h_{1},h_{2},\ldots ,h_{r}\;$ to a set $\;h_{1},h_{2},\ldots ,h_{r},h_{r+1},\ldots ,h_{k}\;$ in such a way that $\;h^{\ast }=\left[h_{1},h_{2},\ldots ,h_{k}\right]\;$ is a one-to-one function from $\mathbb {R} ^{k}$ to itself, and reparameterize the likelihood function by setting $\;\phi _{i}=h_{i}(\theta _{1},\theta _{2},\ldots ,\theta _{k})~.$ Because of the equivariance of the maximum likelihood estimator, the properties of the MLE apply to the restricted estimates also. For instance, in a multivariate normal distribution the covariance matrix $\,\Sigma \,$ must be positive-definite; this restriction can be imposed by replacing $\;\Sigma =\Gamma ^{\mathsf {T}}\Gamma \;,$ where $\Gamma$ is a real upper triangular matrix and $\Gamma ^{\mathsf {T}}$ is its transpose.

In practice, restrictions are usually imposed using the method of Lagrange which, given the constraints as defined above, leads to the *restricted likelihood equations* ${\frac {\partial \ell }{\partial \theta }}-{\frac {\partial h(\theta )^{\mathsf {T}}}{\partial \theta }}\lambda =0$ and $h(\theta )=0\;,$

where $~\lambda =\left[\lambda _{1},\lambda _{2},\ldots ,\lambda _{r}\right]^{\mathsf {T}}~$ is a column-vector of Lagrange multipliers and $\;{\frac {\partial h(\theta )^{\mathsf {T}}}{\partial \theta }}\;$ is the k × r Jacobian matrix of partial derivatives. Naturally, if the constraints are not binding at the maximum, the Lagrange multipliers should be zero. This in turn allows for a statistical test of the "validity" of the constraint, known as the Lagrange multiplier test.

### Nonparametric maximum likelihood estimation

Nonparametric maximum likelihood estimation can be performed using the empirical likelihood.

## Properties

A maximum likelihood estimator is an extremum estimator obtained by maximizing, as a function of *θ*, the objective function ${\widehat {\ell \,}}(\theta \,;x)$ . If the data are independent and identically distributed, then we have ${\widehat {\ell \,}}(\theta \,;x)=\sum _{i=1}^{n}\ln f(x_{i}\mid \theta ),$ this being the sample analogue of the expected log-likelihood $\ell (\theta )=\operatorname {\mathbb {E} } [\,\ln f(x_{i}\mid \theta )\,]$ , where this expectation is taken with respect to the true density.

Maximum-likelihood estimators have no optimum properties for finite samples, in the sense that (when evaluated on finite samples) other estimators may have greater concentration around the true parameter-value. However, like other estimation methods, maximum likelihood estimation possesses a number of attractive limiting properties: As the sample size increases to infinity, sequences of maximum likelihood estimators have these properties:

- Consistency: the sequence of MLEs converges in probability to the value being estimated.
- Equivariance: If ${\hat {\theta }}$ is the maximum likelihood estimator for $\theta$ , and if $g(\theta )$ is a bijective transform of $\theta$ , then the maximum likelihood estimator for $\alpha =g(\theta )$ is ${\hat {\alpha }}=g({\hat {\theta }})$ . The equivariance property can be generalized to non-bijective transforms, although it applies in that case on the maximum of an induced likelihood function which is not the true likelihood in general.
- Efficiency, i.e. it achieves the Cramér–Rao lower bound when the sample size tends to infinity. This means that no consistent estimator has lower asymptotic mean squared error than the MLE (or other estimators attaining this bound), which also means that MLE has asymptotic normality.
- Second-order efficiency after correction for bias.

### Consistency

Under the conditions outlined below, the maximum likelihood estimator is consistent. The consistency means that if the data were generated by $f(\cdot \,;\theta _{0})$ and we have a sufficiently large number of observations *n*, then it is possible to find the value of *θ*0 with arbitrary precision. In mathematical terms this means that as *n* goes to infinity the estimator ${\widehat {\theta \,}}$ converges in probability to its true value:

${\widehat {\theta \,}}_{\mathrm {mle} }\ {\xrightarrow {\text{p}}}\ \theta _{0}.$

Under slightly stronger conditions, the estimator converges almost surely (or *strongly*):

${\widehat {\theta \,}}_{\mathrm {mle} }\ {\xrightarrow {\text{a.s.}}}\ \theta _{0}.$

In practical applications, data is never generated by $f(\cdot \,;\theta _{0})$ . Rather, $f(\cdot \,;\theta _{0})$ is a model, often in idealized form, of the process generated by the data. It is a common aphorism in statistics that *all models are wrong*. Thus, true consistency does not occur in practical applications. Nevertheless, consistency is often considered to be a desirable property for an estimator to have.

To establish consistency, the following conditions are sufficient.

1. Identification of the model: $\theta \neq \theta _{0}\quad \Leftrightarrow \quad f(\cdot \mid \theta )\neq f(\cdot \mid \theta _{0}).$ In other words, different parameter values *θ* correspond to different distributions within the model. If this condition did not hold, there would be some value *θ*1 such that *θ*0 and *θ*1 generate an identical distribution of the observable data. Then we would not be able to distinguish between these two parameters even with an infinite amount of data—these parameters would have been observationally equivalent. The identification condition is absolutely necessary for the ML estimator to be consistent. When this condition holds, the limiting likelihood function *ℓ*(*θ*|·) has unique global maximum at *θ*0.
2. Compactness: the parameter space Θ of the model is compact. The identification condition establishes that the log-likelihood has a unique global maximum. Compactness implies that the likelihood cannot approach the maximum value arbitrarily close at some other point (as demonstrated for example in the picture on the right). Compactness is only a sufficient condition and not a necessary condition. Compactness can be replaced by some other conditions, such as: both concavity of the log-likelihood function and compactness of some (nonempty) upper level sets of the log-likelihood function, orexistence of a compact neighborhood N of θ0 such that outside of N the log-likelihood function is less than the maximum by at least some ε > 0.
3. Continuity: the function ln *f*(*x* | *θ*) is continuous in θ for almost all values of x: $\operatorname {\mathbb {P} } {\Bigl [}\;\ln f(x\mid \theta )\;\in \;C^{0}(\Theta )\;{\Bigr ]}=1.$ The continuity here can be replaced with a slightly weaker condition of upper semi-continuity.
4. Dominance: there exists *D*(*x*) integrable with respect to the distribution *f*(*x* | *θ*0) such that ${\Bigl |}\ln f(x\mid \theta ){\Bigr |}<D(x)\quad {\text{ for all }}\theta \in \Theta .$ By the uniform law of large numbers, the dominance condition together with continuity establish the uniform convergence in probability of the log-likelihood: $\sup _{\theta \in \Theta }\left|{\widehat {\ell \,}}(\theta \mid x)-\ell (\theta )\,\right|\ \xrightarrow {\text{p}} \ 0.$

The dominance condition can be employed in the case of i.i.d. observations. In the non-i.i.d. case, the uniform convergence in probability can be checked by showing that the sequence ${\widehat {\ell \,}}(\theta \mid x)$ is stochastically equicontinuous.

If one wants to demonstrate that the ML estimator ${\widehat {\theta \,}}$ converges to *θ*0 almost surely, then a stronger condition of uniform convergence almost surely has to be imposed: $\sup _{\theta \in \Theta }\left\|\;{\widehat {\ell \,}}(\theta \mid x)-\ell (\theta )\;\right\|\ \xrightarrow {\text{a.s.}} \ 0.$

Additionally, if (as assumed above) the data were generated by $f(\cdot \,;\theta _{0})$ , then under certain conditions, it can also be shown that the maximum likelihood estimator converges in distribution to a normal distribution. Specifically, ${\sqrt {n}}\left({\widehat {\theta \,}}_{\mathrm {mle} }-\theta _{0}\right)\ \xrightarrow {d} \ {\mathcal {N}}\left(0,\,I^{-1}\right)$ where *I* is the Fisher information matrix.

### Functional invariance

The maximum likelihood estimator selects the parameter value which gives the observed data the largest possible probability (or probability density, in the continuous case). If the parameter consists of a number of components, then we define their separate maximum likelihood estimators, as the corresponding component of the MLE of the complete parameter. Consistent with this, if ${\widehat {\theta \,}}$ is the MLE for $\theta$ , and if $g(\theta )$ is any transformation of $\theta$ , then the MLE for $\alpha =g(\theta )$ is by definition

${\widehat {\alpha }}=g(\,{\widehat {\theta \,}}\,).\,$

It maximizes the so-called profile likelihood:

${\bar {L}}(\alpha )=\sup _{\theta :\alpha =g(\theta )}L(\theta ).\,$

The MLE is also equivariant with respect to certain transformations of the data. If $y=g(x)$ where g is one to one and does not depend on the parameters to be estimated, then the density functions satisfy

$f_{Y}(y)=f_{X}(g^{-1}(y))\,|(g^{-1}(y))^{\prime }|$

and hence the likelihood functions for X and Y differ only by a factor that does not depend on the model parameters.

For example, the MLE parameters of the log-normal distribution are the same as those of the normal distribution fitted to the logarithm of the data. In fact, in the log-normal case if $X\sim {\mathcal {N}}(0,1)$ , then $Y=g(X)=e^{X}$ follows a log-normal distribution. The density of Y follows with $f_{X}$ standard Normal and $g^{-1}(y)=\log(y)$ , $|(g^{-1}(y))^{\prime }|={\frac {1}{y}}$ for $y>0$ .

### Efficiency

As assumed above, if the data were generated by $~f(\cdot \,;\theta _{0})~,$ then under certain conditions, it can also be shown that the maximum likelihood estimator converges in distribution to a normal distribution. It is √*n* -consistent and asymptotically efficient, meaning that it reaches the Cramér–Rao bound. Specifically,

${\sqrt {n\,}}\,\left({\widehat {\theta \,}}_{\text{mle}}-\theta _{0}\right)\ \ \xrightarrow {d} \ \ {\mathcal {N}}\left(0,\ {\mathcal {I}}^{-1}\right)~,$ where $~{\mathcal {I}}~$ is the Fisher information matrix: ${\mathcal {I}}_{jk}=\operatorname {\mathbb {E} } \,{\biggl [}\;-{\frac {\partial ^{2}\ln f_{\theta _{0}}(X_{t})}{\partial \theta _{j}\,\partial \theta _{k}}}\;{\biggr ]}~.$

In particular, it means that the bias of the maximum likelihood estimator is equal to zero up to the order ⁠1/√n ⁠.

### Second-order efficiency after correction for bias

However, when we consider the higher-order terms in the expansion of the distribution of this estimator, it turns out that *θ*mle has bias of order 1⁄n. This bias is equal to (componentwise)

$b_{h}\;\equiv \;\operatorname {\mathbb {E} } {\biggl [}\;\left({\widehat {\theta }}_{\mathrm {mle} }-\theta _{0}\right)_{h}\;{\biggr ]}\;=\;{\frac {1}{\,n\,}}\,\sum _{i,j,k=1}^{m}\;{\mathcal {I}}^{hi}\;{\mathcal {I}}^{jk}\left({\frac {1}{\,2\,}}\,K_{ijk}\;+\;J_{j,ik}\right)$

where ${\mathcal {I}}^{jk}$ (with superscripts) denotes the (*j,k*)-th component of the *inverse* Fisher information matrix ${\mathcal {I}}^{-1}$ , and

${\frac {1}{\,2\,}}\,K_{ijk}\;+\;J_{j,ik}\;=\;\operatorname {\mathbb {E} } \,{\biggl [}\;{\frac {1}{2}}{\frac {\partial ^{3}\ln f_{\theta _{0}}(X_{t})}{\partial \theta _{i}\;\partial \theta _{j}\;\partial \theta _{k}}}+{\frac {\;\partial \ln f_{\theta _{0}}(X_{t})\;}{\partial \theta _{j}}}\,{\frac {\;\partial ^{2}\ln f_{\theta _{0}}(X_{t})\;}{\partial \theta _{i}\,\partial \theta _{k}}}\;{\biggr ]}~.$

Using these formulae it is possible to estimate the second-order bias of the maximum likelihood estimator, and *correct* for that bias by subtracting it: ${\widehat {\theta \,}}_{\text{mle}}^{*}={\widehat {\theta \,}}_{\text{mle}}-{\widehat {b\,}}~.$ This estimator is unbiased up to the terms of order ⁠1/ n ⁠, and is called the **bias-corrected maximum likelihood estimator**.

This bias-corrected estimator is *second-order efficient* (at least within the curved exponential family), meaning that it has minimal mean squared error among all second-order bias-corrected estimators, up to the terms of the order ⁠1/ n2 ⁠ . It is possible to continue this process, that is to derive the third-order bias-correction term, and so on. However, the maximum likelihood estimator is *not* third-order efficient.

### Relation to Bayesian inference

A maximum likelihood estimator coincides with the most probable Bayesian estimator given a uniform prior distribution on the parameters. Indeed, the maximum a posteriori estimate is the parameter θ that maximizes the probability of θ given the data, given by Bayes' theorem:

$\operatorname {\mathbb {P} } (\theta \mid x_{1},x_{2},\ldots ,x_{n})={\frac {f(x_{1},x_{2},\ldots ,x_{n}\mid \theta )\operatorname {\mathbb {P} } (\theta )}{\operatorname {\mathbb {P} } (x_{1},x_{2},\ldots ,x_{n})}}$

where $\operatorname {\mathbb {P} } (\theta )$ is the prior distribution for the parameter θ and where $\operatorname {\mathbb {P} } (x_{1},x_{2},\ldots ,x_{n})$ is the probability of the data averaged over all parameters. Since the denominator is independent of θ, the Bayesian estimator is obtained by maximizing $f(x_{1},x_{2},\ldots ,x_{n}\mid \theta )\operatorname {\mathbb {P} } (\theta )$ with respect to θ. If we further assume that the prior $\operatorname {\mathbb {P} } (\theta )$ is a uniform distribution, the Bayesian estimator is obtained by maximizing the likelihood function $f(x_{1},x_{2},\ldots ,x_{n}\mid \theta )$ . Thus the Bayesian estimator coincides with the maximum likelihood estimator for a uniform prior distribution $\operatorname {\mathbb {P} } (\theta )$ .

#### Application of maximum-likelihood estimation in Bayes decision theory

In many practical applications in machine learning, maximum-likelihood estimation is used as the model for parameter estimation.

The Bayesian Decision theory is about designing a classifier that minimizes total expected risk, especially, when the costs (the loss function) associated with different decisions are equal, the classifier is minimizing the error over the whole distribution.

Thus, the Bayes Decision Rule is stated as

"decide

$\;w_{1}\;$

if

$~\operatorname {\mathbb {P} } (w_{1}|x)\;>\;\operatorname {\mathbb {P} } (w_{2}|x)~;~$

otherwise decide

$\;w_{2}\;$

"

where $\;w_{1}\,,w_{2}\;$ are predictions of different classes. From a perspective of minimizing error, it can also be stated as $w={\underset {w}{\operatorname {arg\;max} }}\;\int _{-\infty }^{\infty }\operatorname {\mathbb {P} } ({\text{ error}}\mid x)\operatorname {\mathbb {P} } (x)\,\operatorname {d} x~$ where $\operatorname {\mathbb {P} } ({\text{ error}}\mid x)=\operatorname {\mathbb {P} } (w_{1}\mid x)~$ if we decide $\;w_{2}\;$ and $\;\operatorname {\mathbb {P} } ({\text{ error}}\mid x)=\operatorname {\mathbb {P} } (w_{2}\mid x)\;$ if we decide $\;w_{1}\;.$

By applying Bayes' theorem $\operatorname {\mathbb {P} } (w_{i}\mid x)={\frac {\operatorname {\mathbb {P} } (x\mid w_{i})\operatorname {\mathbb {P} } (w_{i})}{\operatorname {\mathbb {P} } (x)}},$ and if we further assume the zero-or-one loss function, which is a same loss for all errors, the Bayes Decision rule can be reformulated as: $h_{\text{Bayes}}={\underset {w}{\operatorname {arg\;max} }}\,{\bigl [}\,\operatorname {\mathbb {P} } (x\mid w)\,\operatorname {\mathbb {P} } (w)\,{\bigr ]}\;,$ where $h_{\text{Bayes}}$ is the prediction and $\;\operatorname {\mathbb {P} } (w)\;$ is the prior probability.

### Relation to minimizing Kullback–Leibler divergence and cross entropy

Finding ${\hat {\theta }}$ that maximizes the likelihood is asymptotically equivalent to finding the ${\hat {\theta }}$ that defines a probability distribution ( $Q_{\hat {\theta }}$ ) that has a minimal distance, in terms of Kullback–Leibler divergence, to the real probability distribution from which our data were generated (i.e., generated by $P_{\theta _{0}}$ ). In an ideal world, P and Q are the same (and the only thing unknown is $\theta$ that defines P), but even if they are not and the model we use is misspecified, still the MLE will give us the "closest" distribution (within the restriction of a model Q that depends on ${\hat {\theta }}$ ) to the real distribution $P_{\theta _{0}}$ .

| **Proof.** |
|---|
| For simplicity of notation, let's assume that P=Q. Let there be *n* i.i.d data samples $\mathbf {y} =(y_{1},y_{2},\ldots ,y_{n})$ from some probability $y\sim P_{\theta _{0}}$ , that we try to estimate by finding ${\hat {\theta }}$ that will maximize the likelihood using $P_{\theta }$ , then: ${\begin{aligned}{\hat {\theta }}&={\underset {\theta }{\operatorname {arg\,max} }}\,L_{P_{\theta }}(\mathbf {y} )={\underset {\theta }{\operatorname {arg\,max} }}\,P_{\theta }(\mathbf {y} )={\underset {\theta }{\operatorname {arg\,max} }}\,P(\mathbf {y} \mid \theta )\\&={\underset {\theta }{\operatorname {arg\,max} }}\,\prod _{i=1}^{n}P(y_{i}\mid \theta )={\underset {\theta }{\operatorname {arg\,max} }}\,\sum _{i=1}^{n}\log P(y_{i}\mid \theta )\\&={\underset {\theta }{\operatorname {arg\,max} }}\,\left(\sum _{i=1}^{n}\log P(y_{i}\mid \theta )-\sum _{i=1}^{n}\log P(y_{i}\mid \theta _{0})\right)={\underset {\theta }{\operatorname {arg\,max} }}\,\sum _{i=1}^{n}\left(\log P(y_{i}\mid \theta )-\log P(y_{i}\mid \theta _{0})\right)\\&={\underset {\theta }{\operatorname {arg\,max} }}\,\sum _{i=1}^{n}\log {\frac {P(y_{i}\mid \theta )}{P(y_{i}\mid \theta _{0})}}={\underset {\theta }{\operatorname {arg\,min} }}\,\sum _{i=1}^{n}\log {\frac {P(y_{i}\mid \theta _{0})}{P(y_{i}\mid \theta )}}={\underset {\theta }{\operatorname {arg\,min} }}\,{\frac {1}{n}}\sum _{i=1}^{n}\log {\frac {P(y_{i}\mid \theta _{0})}{P(y_{i}\mid \theta )}}\\&={\underset {\theta }{\operatorname {arg\,min} }}\,{\frac {1}{n}}\sum _{i=1}^{n}h_{\theta }(y_{i})\quad {\underset {n\to \infty }{\longrightarrow }}\quad {\underset {\theta }{\operatorname {arg\,min} }}\,E[h_{\theta }(y)]\\&={\underset {\theta }{\operatorname {arg\,min} }}\,\int P_{\theta _{0}}(y)h_{\theta }(y)dy={\underset {\theta }{\operatorname {arg\,min} }}\,\int P_{\theta _{0}}(y)\log {\frac {P(y\mid \theta _{0})}{P(y\mid \theta )}}dy\\&={\underset {\theta }{\operatorname {arg\,min} }}\,D_{\text{KL}}(P_{\theta _{0}}\parallel P_{\theta })\end{aligned}}$ Where $h_{\theta }(x)=\log {\frac {P(x\mid \theta _{0})}{P(x\mid \theta )}}$ . Using *h* helps see how we are using the law of large numbers to move from the average of *h*(*x*) to the expectancy of it using the law of the unconscious statistician. The first several transitions have to do with laws of logarithm and that finding ${\hat {\theta }}$ that maximizes some function will also be the one that maximizes some monotonic transformation of that function (i.e.: adding/multiplying by a constant). Since cross entropy is just Shannon's entropy plus KL divergence, and since the entropy of $P_{\theta _{0}}$ is constant, then the MLE is also asymptotically minimizing cross entropy. |

### Prediction bias

Maximum likelihood estimates of parameters can be substituted into expressions for the probability density function, cumulative distribution function, or quantile function, to generate predictions of probabilities or quantiles of out-of-sample events. This method for predicting probabilities is recommended in statistics text-books and actuarial textbooks, and is widely used in the scientific literature. However, maximum likelihood prediction fails to propagate the uncertainty around the maximum likelihood parameter estimates into the prediction. As a result, the predicted probabilities are not well calibrated, and should not be expected to correspond to the frequencies of out-of-sample events. In particular, tail exceedance probabilities and tail exceedance quantiles are typically underestimated, sometimes dramatically. The underestimation is largest when there is little training data, many parameters being estimated, and for the far tail. For cases where this prediction bias is a problem, Bayesian predictions can provide a solution if the prior is chosen so as to reduce or eliminate the bias.

## Examples

### Discrete uniform distribution

Consider a case where *n* tickets numbered from 1 to *n* are placed in a box and one is selected at random (*see uniform distribution*); thus, the sample size is 1. If *n* is unknown, then the maximum likelihood estimator ${\widehat {n}}$ of *n* is the number *m* on the drawn ticket. (The likelihood is 0 for *n* < *m*, 1⁄*n* for *n* ≥ *m*, and this is greatest when *n* = *m*. Note that the maximum likelihood estimate of *n* occurs at the lower extreme of possible values {*m*, *m* + 1, ...}, rather than somewhere in the "middle" of the range of possible values, which would result in less bias.) The expected value of the number *m* on the drawn ticket, and therefore the expected value of ${\widehat {n}}$ , is (*n* + 1)/2. As a result, with a sample size of 1, the maximum likelihood estimator for *n* will systematically underestimate *n* by (*n* − 1)/2.

### Discrete distribution, finite parameter space

Suppose one wishes to determine just how biased an unfair coin is. Call the probability of tossing a 'head' *p*. The goal then becomes to determine *p*.

Suppose the coin is tossed 80 times: i.e. the sample might be something like *x*1 = H, *x*2 = T, ..., *x*80 = T, and the count of the number of heads "H" is observed.

The probability of tossing tails is 1 − *p* (so here *p* is *θ* above). Suppose the outcome is 49 heads and 31 tails, and suppose the coin was taken from a box containing three coins: one which gives heads with probability *p* = 1⁄3, one which gives heads with probability *p* = 1⁄2 and another which gives heads with probability *p* = 2⁄3. The coins have lost their labels, so which one it was is unknown. Using maximum likelihood estimation, the coin that has the largest likelihood can be found, given the data that were observed. By using the probability mass function of the binomial distribution with sample size equal to 80, number successes equal to 49 but for different values of *p* (the "probability of success"), the likelihood function (defined below) takes one of three values:

${\begin{aligned}\operatorname {\mathbb {P} } {\bigl [}\;\mathrm {H} =49\mid p={\tfrac {1}{3}}\;{\bigr ]}&={\binom {80}{49}}({\tfrac {1}{3}})^{49}(1-{\tfrac {1}{3}})^{31}\approx 0.000,\\[6pt]\operatorname {\mathbb {P} } {\bigl [}\;\mathrm {H} =49\mid p={\tfrac {1}{2}}\;{\bigr ]}&={\binom {80}{49}}({\tfrac {1}{2}})^{49}(1-{\tfrac {1}{2}})^{31}\approx 0.012,\\[6pt]\operatorname {\mathbb {P} } {\bigl [}\;\mathrm {H} =49\mid p={\tfrac {2}{3}}\;{\bigr ]}&={\binom {80}{49}}({\tfrac {2}{3}})^{49}(1-{\tfrac {2}{3}})^{31}\approx 0.054~.\end{aligned}}$

The likelihood is maximized when p = 2⁄3, and so this is the *maximum likelihood estimate* for p.

### Discrete distribution, continuous parameter space

Now suppose that there was only one coin but its p could have been any value 0 ≤ p ≤ 1 . The likelihood function to be maximised is $L(p)=f_{D}(\mathrm {H} =49\mid p)={\binom {80}{49}}p^{49}(1-p)^{31}~,$

and the maximisation is over all possible values 0 ≤ p ≤ 1 .

One way to maximize this function is by differentiating with respect to p and setting to zero:

${\begin{aligned}0&={\frac {\partial }{\partial p}}\left({\binom {80}{49}}p^{49}(1-p)^{31}\right)~,\\[8pt]0&=49p^{48}(1-p)^{31}-31p^{49}(1-p)^{30}\\[8pt]&=p^{48}(1-p)^{30}\left[49(1-p)-31p\right]\\[8pt]&=p^{48}(1-p)^{30}\left[49-80p\right]~.\end{aligned}}$

This is a product of three terms. The first term is 0 when p = 0. The second is 0 when p = 1. The third is zero when p = 49⁄80. The solution that maximizes the likelihood is clearly p = 49⁄80 (since p = 0 and p = 1 result in a likelihood of 0). Thus the *maximum likelihood estimator* for p is 49⁄80.

This result is easily generalized by substituting a letter such as s in the place of 49 to represent the observed number of 'successes' of our Bernoulli trials, and a letter such as n in the place of 80 to represent the number of Bernoulli trials. Exactly the same calculation yields s⁄n which is the maximum likelihood estimator for any sequence of n Bernoulli trials resulting in s 'successes'.

### Continuous distribution, continuous parameter space

For the normal distribution ${\mathcal {N}}(\mu ,\sigma ^{2})$ which has probability density function

$f(x\mid \mu ,\sigma ^{2})={\frac {1}{{\sqrt {2\pi \sigma ^{2}}}\ }}\exp \left(-{\frac {(x-\mu )^{2}}{2\sigma ^{2}}}\right),$

the corresponding probability density function for a sample of n independent identically distributed normal random variables (the likelihood) is

$f(x_{1},\ldots ,x_{n}\mid \mu ,\sigma ^{2})=\prod _{i=1}^{n}f(x_{i}\mid \mu ,\sigma ^{2})=\left({\frac {1}{2\pi \sigma ^{2}}}\right)^{n/2}\exp \left(-{\frac {\sum _{i=1}^{n}(x_{i}-\mu )^{2}}{2\sigma ^{2}}}\right).$

This family of distributions has two parameters: *θ* = (*μ*, *σ*); so we maximize the likelihood, ${\mathcal {L}}(\mu ,\sigma ^{2})=f(x_{1},\ldots ,x_{n}\mid \mu ,\sigma ^{2})$ , over both parameters simultaneously, or if possible, individually.

Since the logarithm function itself is a continuous strictly increasing function over the range of the likelihood, the values which maximize the likelihood will also maximize its logarithm (the log-likelihood itself is not necessarily strictly increasing). The log-likelihood can be written as follows:

$\log \left({\mathcal {L}}(\mu ,\sigma ^{2})\right)=-{\frac {n}{2}}\log(2\pi \sigma ^{2})-{\frac {1}{2\sigma ^{2}}}\sum _{i=1}^{n}\left(x_{i}-\mu \right)^{2}$

(Note: the log-likelihood is closely related to information entropy and Fisher information.)

We now compute the derivatives of this log-likelihood as follows.

${\begin{aligned}0&={\frac {\partial }{\partial \mu }}\log \left({\mathcal {L}}(\mu ,\sigma ^{2})\right)=0-{\frac {-2n({\bar {x}}-\mu )}{2\sigma ^{2}}}.\end{aligned}}$ where ${\bar {x}}$ is the sample mean. This is solved by

${\widehat {\mu }}={\bar {x}}=\sum _{i=1}^{n}{\frac {\,x_{i}\,}{n}}.$

This is indeed the maximum of the function, since it is the only turning point in μ and the second derivative is strictly less than zero. Its expected value is equal to the parameter μ of the given distribution,

$\operatorname {\mathbb {E} } {\bigl [}\;{\widehat {\mu }}\;{\bigr ]}=\mu ,\,$

which means that the maximum likelihood estimator ${\widehat {\mu }}$ is unbiased.

Similarly we differentiate the log-likelihood with respect to σ and equate to zero:

${\begin{aligned}0&={\frac {\partial }{\partial \sigma }}\log {\Bigl (}{\mathcal {L}}(\mu ,\sigma ^{2}){\Bigr )}=-{\frac {\,n\,}{\sigma }}+{\frac {1}{\sigma ^{3}}}\sum _{i=1}^{n}(\,x_{i}-\mu \,)^{2}.\end{aligned}}$

which is solved by

${\widehat {\sigma }}^{2}={\frac {1}{n}}\sum _{i=1}^{n}(x_{i}-\mu )^{2}.$

Inserting the estimate $\mu ={\widehat {\mu }}$ we obtain

${\widehat {\sigma }}^{2}={\frac {1}{n}}\sum _{i=1}^{n}(x_{i}-{\bar {x}})^{2}={\frac {1}{n}}\sum _{i=1}^{n}x_{i}^{2}-{\frac {1}{n^{2}}}\sum _{i=1}^{n}\sum _{j=1}^{n}x_{i}x_{j}.$

To calculate its expected value, it is convenient to rewrite the expression in terms of zero-mean random variables (statistical error) $\delta _{i}\equiv \mu -x_{i}$ . Expressing the estimate in these variables yields

${\widehat {\sigma }}^{2}={\frac {1}{n}}\sum _{i=1}^{n}(\mu -\delta _{i})^{2}-{\frac {1}{n^{2}}}\sum _{i=1}^{n}\sum _{j=1}^{n}(\mu -\delta _{i})(\mu -\delta _{j}).$

Simplifying the expression above, utilizing the facts that $\operatorname {\mathbb {E} } {\bigl [}\;\delta _{i}\;{\bigr ]}=0$ and $\operatorname {E} {\bigl [}\;\delta _{i}^{2}\;{\bigr ]}=\sigma ^{2}$ , allows us to obtain

$\operatorname {\mathbb {E} } {\bigl [}\;{\widehat {\sigma }}^{2}\;{\bigr ]}={\frac {\,n-1\,}{n}}\sigma ^{2}.$

This means that the estimator ${\widehat {\sigma }}^{2}$ is biased for $\sigma ^{2}$ . It can also be shown that ${\widehat {\sigma }}$ is biased for $\sigma$ , but that both ${\widehat {\sigma }}^{2}$ and ${\widehat {\sigma }}$ are consistent.

Formally we say that the *maximum likelihood estimator* for $\theta =(\mu ,\sigma ^{2})$ is

${\widehat {\theta \,}}=\left({\widehat {\mu }},{\widehat {\sigma }}^{2}\right).$

In this case the MLEs could be obtained individually. In general this may not be the case, and the MLEs would have to be obtained simultaneously.

The normal log-likelihood at its maximum takes a particularly simple form:

$\log {\Bigl (}{\mathcal {L}}({\widehat {\mu }},{\widehat {\sigma }}){\Bigr )}={\frac {\,-n\;\;}{2}}{\bigl (}\,\log(2\pi {\widehat {\sigma }}^{2})+1\,{\bigr )}$

This maximum log-likelihood can be shown to be the same for more general least squares, even for non-linear least squares. This is often used in determining likelihood-based approximate confidence intervals and confidence regions, which are generally more accurate than those using the asymptotic normality discussed above.

## Non-independent variables

It may be the case that variables are correlated, or more generally, not independent. Two random variables $y_{1}$ and $y_{2}$ are independent only if their joint probability density function is the product of the individual probability density functions, i.e.

$f(y_{1},y_{2})=f(y_{1})f(y_{2})\,$

Suppose one constructs an order-*n* Gaussian vector out of random variables $(y_{1},\ldots ,y_{n})$ , where each variable has means given by $(\mu _{1},\ldots ,\mu _{n})$ . Furthermore, let the covariance matrix be denoted by ${\mathit {\Sigma }}$ . The joint probability density function of these *n* random variables then follows a multivariate normal distribution given by:

$f(y_{1},\ldots ,y_{n})={\frac {1}{(2\pi )^{n/2}{\sqrt {\det({\mathit {\Sigma }})}}}}\exp \left(-{\frac {1}{2}}\left[y_{1}-\mu _{1},\ldots ,y_{n}-\mu _{n}\right]{\mathit {\Sigma }}^{-1}\left[y_{1}-\mu _{1},\ldots ,y_{n}-\mu _{n}\right]^{\mathrm {T} }\right)$

In the bivariate case, the joint probability density function is given by:

$f(y_{1},y_{2})={\frac {1}{2\pi \sigma _{1}\sigma _{2}{\sqrt {1-\rho ^{2}}}}}\exp \left[-{\frac {1}{2(1-\rho ^{2})}}\left({\frac {(y_{1}-\mu _{1})^{2}}{\sigma _{1}^{2}}}-{\frac {2\rho (y_{1}-\mu _{1})(y_{2}-\mu _{2})}{\sigma _{1}\sigma _{2}}}+{\frac {(y_{2}-\mu _{2})^{2}}{\sigma _{2}^{2}}}\right)\right]$

In this and other cases where a joint density function exists, the likelihood function is defined as above, in the section "principles," using this density.

### Example

$X_{1},\ X_{2},\ldots ,\ X_{m}$ are counts in cells / boxes 1 up to m; each box has a different probability (think of the boxes being bigger or smaller) and we fix the number of balls that fall to be n : $x_{1}+x_{2}+\cdots +x_{m}=n$ . The probability of each box is $p_{i}$ , with a constraint: $p_{1}+p_{2}+\cdots +p_{m}=1$ . This is a case in which the $X_{i}$ *s* are not independent, the joint probability of a vector $x_{1},\ x_{2},\ldots ,x_{m}$ is called the multinomial and has the form:

$f(x_{1},x_{2},\ldots ,x_{m}\mid p_{1},p_{2},\ldots ,p_{m})={\frac {n!}{\prod x_{i}!}}\prod p_{i}^{x_{i}}={\binom {n}{x_{1},x_{2},\ldots ,x_{m}}}p_{1}^{x_{1}}p_{2}^{x_{2}}\cdots p_{m}^{x_{m}}$

Each box taken separately against all the other boxes is a binomial and this is an extension thereof.

The log-likelihood of this is:

$\ell (p_{1},p_{2},\ldots ,p_{m})=\log n!-\sum _{i=1}^{m}\log x_{i}!+\sum _{i=1}^{m}x_{i}\log p_{i}$

The constraint has to be taken into account and use the Lagrange multipliers:

$L(p_{1},p_{2},\ldots ,p_{m},\lambda )=\ell (p_{1},p_{2},\ldots ,p_{m})+\lambda \left(1-\sum _{i=1}^{m}p_{i}\right)$

By posing all the derivatives to be 0, the most natural estimate is derived

${\hat {p}}_{i}={\frac {x_{i}}{n}}$

Maximizing log likelihood, with and without constraints, can be an unsolvable problem in closed form, then we have to use iterative procedures.

## Iterative procedures

Except for special cases, the likelihood equations ${\frac {\partial \ell (\theta ;\mathbf {y} )}{\partial \theta }}=0$

cannot be solved explicitly for an estimator ${\widehat {\theta }}={\widehat {\theta }}(\mathbf {y} )$ . Instead, they need to be solved iteratively: starting from an initial guess of $\theta$ (say ${\widehat {\theta }}_{1}$ ), one seeks to obtain a convergent sequence $\left\{{\widehat {\theta }}_{r}\right\}$ . Many methods for this kind of optimization problem are available, but the most commonly used ones are algorithms based on an updating formula of the form ${\widehat {\theta }}_{r+1}={\widehat {\theta }}_{r}+\eta _{r}\mathbf {d} _{r}\left({\widehat {\theta }}\right)$

where the vector $\mathbf {d} _{r}\left({\widehat {\theta }}\right)$ indicates the descent direction of the *r*th "step," and the scalar $\eta _{r}$ captures the "step length," also known as the learning rate.

### Gradient descent method

(Note: here it is a maximization problem, so the sign before gradient is flipped)

$\eta _{r}\in \mathbb {R} ^{+}$ that is small enough for convergence and $\mathbf {d} _{r}\left({\widehat {\theta }}\right)=\nabla \ell \left({\widehat {\theta }}_{r};\mathbf {y} \right)$

Gradient descent method requires to calculate the gradient at the *r*-th iteration, but no need to calculate the inverse of second-order derivative, i.e., the Hessian matrix. Therefore, it is computationally faster than Newton–Raphson method.

### Newton–Raphson method

$\eta _{r}=1$ and $\mathbf {d} _{r}\left({\widehat {\theta }}\right)=-\mathbf {H} _{r}^{-1}\left({\widehat {\theta }}\right)\mathbf {s} _{r}\left({\widehat {\theta }}\right)$

where $\mathbf {s} _{r}({\widehat {\theta }})$ is the score and $\mathbf {H} _{r}^{-1}\left({\widehat {\theta }}\right)$ is the inverse of the Hessian matrix of the log-likelihood function, both evaluated the *r*th iteration. But because the calculation of the Hessian matrix is computationally costly, numerous alternatives have been proposed. The popular Berndt–Hall–Hall–Hausman algorithm approximates the Hessian with the outer product of the expected gradient, such that

$\mathbf {d} _{r}\left({\widehat {\theta }}\right)=-\left[{\frac {1}{n}}\sum _{t=1}^{n}{\frac {\partial \ell (\theta ;\mathbf {y} )}{\partial \theta }}\left({\frac {\partial \ell (\theta ;\mathbf {y} )}{\partial \theta }}\right)^{\mathsf {T}}\right]^{-1}\mathbf {s} _{r}\left({\widehat {\theta }}\right)$

### Quasi-Newton methods

Other quasi-Newton methods use more elaborate secant updates to give approximation of Hessian matrix.

#### Davidon–Fletcher–Powell formula

DFP formula finds a solution that is symmetric, positive-definite and closest to the current approximate value of second-order derivative: $\mathbf {H} _{k+1}=\left(I-\gamma _{k}y_{k}s_{k}^{\mathsf {T}}\right)\mathbf {H} _{k}\left(I-\gamma _{k}s_{k}y_{k}^{\mathsf {T}}\right)+\gamma _{k}y_{k}y_{k}^{\mathsf {T}},$

where

$y_{k}=\nabla \ell (x_{k}+s_{k})-\nabla \ell (x_{k}),$ $\gamma _{k}={\frac {1}{y_{k}^{\mathsf {T}}s_{k}}},$ $s_{k}=x_{k+1}-x_{k}.$

#### Broyden–Fletcher–Goldfarb–Shanno algorithm

BFGS also gives a solution that is symmetric and positive-definite:

$B_{k+1}=B_{k}+{\frac {y_{k}y_{k}^{\mathsf {T}}}{y_{k}^{\mathsf {T}}s_{k}}}-{\frac {B_{k}s_{k}s_{k}^{\mathsf {T}}B_{k}^{\mathsf {T}}}{s_{k}^{\mathsf {T}}B_{k}s_{k}}}\ ,$

where

$y_{k}=\nabla \ell (x_{k}+s_{k})-\nabla \ell (x_{k}),$ $s_{k}=x_{k+1}-x_{k}.$

BFGS method is not guaranteed to converge unless the function has a quadratic Taylor expansion near an optimum. However, BFGS can have acceptable performance even for non-smooth optimization instances

#### Fisher's scoring

Another popular method is to replace the Hessian with the Fisher information matrix, ${\mathcal {I}}(\theta )=\operatorname {\mathbb {E} } \left[\mathbf {H} _{r}\left({\widehat {\theta }}\right)\right]$ , giving us the Fisher scoring algorithm. This procedure is standard in the estimation of many methods, such as generalized linear models.

Although popular, quasi-Newton methods may converge to a stationary point that is not necessarily a local or global maximum, but rather a local minimum or a saddle point. Therefore, it is important to assess the validity of the obtained solution to the likelihood equations, by verifying that the Hessian, evaluated at the solution, is both negative definite and well-conditioned.

## History

Early users of maximum likelihood include Carl Friedrich Gauss, Pierre-Simon Laplace, Thorvald N. Thiele, and Francis Ysidro Edgeworth. It was Ronald Fisher however, between 1912 and 1922, who single-handedly created the modern version of the method.

Maximum-likelihood estimation finally transcended heuristic justification in a proof published by Samuel S. Wilks in 1938, now called Wilks' theorem. The theorem shows that the error in the logarithm of likelihood values for estimates from multiple independent observations is asymptotically *χ* 2-distributed, which enables convenient determination of a confidence region around any estimate of the parameters. The only difficult part of Wilks' proof depends on the expected value of the Fisher information matrix, which is provided by a theorem proven by Fisher. Wilks continued to improve on the generality of the theorem throughout his life, with his most general proof published in 1962.

Reviews of the development of maximum likelihood estimation have been provided by a number of authors.
