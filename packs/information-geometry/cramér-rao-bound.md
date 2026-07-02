---
title: "Cramér–Rao bound"
source: https://en.wikipedia.org/wiki/Cram%C3%A9r%E2%80%93Rao_bound
domain: information-geometry
license: CC-BY-SA-4.0
tags: information geometry, fisher information metric, statistical manifold, bregman divergence
fetched: 2026-07-02
---

# Cramér–Rao bound

In estimation theory and statistics, the **Cramér–Rao bound** (**CRB**) relates to estimation of a deterministic (fixed, though unknown) parameter. The result is named in honor of Harald Cramér and Calyampudi Radhakrishna Rao, but has also been derived independently by Maurice Fréchet, Georges Darmois, and by Alexander Aitken and Harold Silverstone. It is also known as Fréchet–Cramér–Rao or Fréchet–Darmois–Cramér–Rao lower bound. It states that the precision of any unbiased estimator is at most the Fisher information; or (equivalently) the reciprocal of the Fisher information is a lower bound on its variance.

An unbiased estimator that achieves this bound is said to be (fully) *efficient*. Such a solution achieves the lowest possible mean squared error among all unbiased methods, and is, therefore, the minimum variance unbiased (MVU) estimator. However, in some cases, no unbiased technique exists which achieves the bound. This may occur either if for any unbiased estimator, there exists another with a strictly smaller variance, or if an MVU estimator exists, but its variance is strictly greater than the inverse of the Fisher information.

The Cramér–Rao bound can also be used to bound the variance of *biased* estimators of given bias. In some cases, a biased approach can result in both a variance and a mean squared error that are *below* the unbiased Cramér–Rao lower bound; see estimator bias.

Significant progress over the Cramér–Rao lower bound was proposed by Anil Kumar Bhattacharyya through a series of works, called Bhattacharyya bound.

## Statement

The Cramér–Rao bound is stated in this section for several increasingly general cases, beginning with the case in which the parameter is a scalar and its estimator is unbiased. All versions of the bound require certain regularity conditions, which hold for most well-behaved distributions. These conditions are listed later in this section.

### Scalar unbiased case

Suppose $\theta$ is an unknown deterministic parameter that is to be estimated from n independent observations (measurements) of x , each from a distribution according to some probability density function $f(x;\theta )$ . The variance of any *unbiased* estimator ${\hat {\theta }}$ of $\theta$ is then bounded by the reciprocal of the Fisher information $I(\theta )$ :

$\operatorname {var} ({\hat {\theta }})\geq {\frac {1}{I(\theta )}}$

where the Fisher information $I(\theta )$ is defined by

$I(\theta )=n\operatorname {E} _{X;\theta }\left[\left({\frac {\partial \ell (X;\theta )}{\partial \theta }}\right)^{2}\right]$

and $\ell (x;\theta )=\log(f(x;\theta ))$ is the natural logarithm of the likelihood function for a single sample x and $\operatorname {E} _{x;\theta }$ denotes the expected value with respect to the density $f(x;\theta )$ of X . If not indicated, in what follows, the expectation is taken with respect to X .

If $\ell (x;\theta )$ is twice differentiable and certain regularity conditions hold, then the Fisher information can also be defined as follows:

$I(\theta )=-n\operatorname {E} _{X;\theta }\left[{\frac {\partial ^{2}\ell (X;\theta )}{\partial \theta ^{2}}}\right]$

The efficiency of an unbiased estimator ${\hat {\theta }}$ measures how close this estimator's variance comes to this lower bound; estimator efficiency is defined as

$e({\hat {\theta }})={\frac {I(\theta )^{-1}}{\operatorname {var} ({\hat {\theta }})}}$

or the minimum possible variance for an unbiased estimator divided by its actual variance. The Cramér–Rao lower bound thus gives

$e({\hat {\theta }})\leq 1$

.

### General scalar case

A more general form of the bound can be obtained by considering a biased estimator $T(X)$ , whose expectation is not $\theta$ but a function of this parameter, say, $\psi (\theta )$ . Hence $E\{T(X)\}-\theta =\psi (\theta )-\theta$ is not generally equal to 0. In this case, the bound is given by

$\operatorname {var} (T)\geq {\frac {[\psi '(\theta )]^{2}}{I(\theta )}}$

where $\psi '(\theta )$ is the derivative of $\psi (\theta )$ (by $\theta$ ), and $I(\theta )$ is the Fisher information defined above.

### Bound on the variance of biased estimators

Apart from being a bound on estimators of functions of the parameter, this approach can be used to derive a bound on the variance of biased estimators with a given bias, as follows. Consider an estimator ${\hat {\theta }}$ with bias $b(\theta )=E\{{\hat {\theta }}\}-\theta$ , and let $\psi (\theta )=b(\theta )+\theta$ . By the result above, any unbiased estimator whose expectation is $\psi (\theta )$ has variance greater than or equal to $(\psi '(\theta ))^{2}/I(\theta )$ . Thus, any estimator ${\hat {\theta }}$ whose bias is given by a function $b(\theta )$ satisfies

$\operatorname {var} \left({\hat {\theta }}\right)\geq {\frac {[1+b'(\theta )]^{2}}{I(\theta )}}.$

The unbiased version of the bound is a special case of this result, with $b(\theta )=0$ .

It's trivial to have a small variance − an "estimator" that is constant has a variance of zero. But from the above equation, we find that the mean squared error of a biased estimator is bounded by

$\operatorname {E} \left(({\hat {\theta }}-\theta )^{2}\right)\geq {\frac {[1+b'(\theta )]^{2}}{I(\theta )}}+b(\theta )^{2},$

using the standard decomposition of the MSE. Note, however, that if $1+b'(\theta )<1$ this bound might be less than the unbiased Cramér–Rao bound $1/I(\theta )$ . For instance, in the example of estimating variance below, $1+b'(\theta )={\frac {n}{n+2}}<1$ .

### Multivariate case

Extending the Cramér–Rao bound to multiple parameters, define a parameter column vector

${\boldsymbol {\theta }}=\left[\theta _{1},\theta _{2},\dots ,\theta _{d}\right]^{T}\in \mathbb {R} ^{d}$

with probability density function $f(x;{\boldsymbol {\theta }})$ which satisfies the two regularity conditions below.

The Fisher information matrix is a $d\times d$ matrix with element $I_{m,k}$ defined as

$I_{m,k}=\operatorname {E} \left[{\frac {\partial }{\partial \theta _{m}}}\log f\left(x;{\boldsymbol {\theta }}\right){\frac {\partial }{\partial \theta _{k}}}\log f\left(x;{\boldsymbol {\theta }}\right)\right]=-\operatorname {E} \left[{\frac {\partial ^{2}}{\partial \theta _{m}\,\partial \theta _{k}}}\log f\left(x;{\boldsymbol {\theta }}\right)\right].$

Let ${\boldsymbol {T}}(X)$ be an estimator of any vector function of parameters, ${\boldsymbol {T}}(X)=(T_{1}(X),\ldots ,T_{d}(X))^{T}$ , and denote its expectation vector $\operatorname {E} [{\boldsymbol {T}}(X)]$ by ${\boldsymbol {\psi }}({\boldsymbol {\theta }})$ . The Cramér–Rao bound then states that the covariance matrix of ${\boldsymbol {T}}(X)$ satisfies

$I\left({\boldsymbol {\theta }}\right)\geq \phi (\theta )^{T}\operatorname {cov} _{\boldsymbol {\theta }}\left({\boldsymbol {T}}(X)\right)^{-1}\phi (\theta )$

,

$\operatorname {cov} _{\boldsymbol {\theta }}\left({\boldsymbol {T}}(X)\right)\geq \phi (\theta )I\left({\boldsymbol {\theta }}\right)^{-1}\phi (\theta )^{T}$

where

- The matrix inequality $A\geq B$ is understood to mean that the matrix $A-B$ is positive semidefinite, and
- $\phi (\theta ):=\partial {\boldsymbol {\psi }}({\boldsymbol {\theta }})/\partial {\boldsymbol {\theta }}$ is the Jacobian matrix whose $ij$ element is given by $\partial \psi _{i}({\boldsymbol {\theta }})/\partial \theta _{j}$ .

If ${\boldsymbol {T}}(X)$ is an unbiased estimator of ${\boldsymbol {\theta }}$ (i.e., ${\boldsymbol {\psi }}\left({\boldsymbol {\theta }}\right)={\boldsymbol {\theta }}$ ), then the Cramér–Rao bound reduces to

$\operatorname {cov} _{\boldsymbol {\theta }}\left({\boldsymbol {T}}(X)\right)\geq I\left({\boldsymbol {\theta }}\right)^{-1}.$

If it is inconvenient to compute the inverse of the Fisher information matrix, then one can simply take the reciprocal of the corresponding diagonal element to find a (possibly loose) lower bound.

$\operatorname {var} _{\boldsymbol {\theta }}(T_{m}(X))=\left[\operatorname {cov} _{\boldsymbol {\theta }}\left({\boldsymbol {T}}(X)\right)\right]_{mm}\geq \left[I\left({\boldsymbol {\theta }}\right)^{-1}\right]_{mm}\geq {\frac {1}{I\left({\boldsymbol {\theta }}\right)_{mm}}}.$

### Regularity conditions

The bound relies on two weak regularity conditions on the probability density function, $f(x;\theta )$ , and the estimator $T(X)$ :

- The Fisher information is always defined; equivalently, for all x such that $f(x;\theta )>0$ , ${\frac {\partial }{\partial \theta }}\log f(x;\theta )$ exists, and is finite.
- The operations of integration with respect to x and differentiation with respect to $\theta$ can be interchanged in the expectation of T ; that is, ${\frac {\partial }{\partial \theta }}\left[\int T(x)f(x;\theta )\,dx\right]=\int T(x)\left[{\frac {\partial }{\partial \theta }}f(x;\theta )\right]\,dx$ whenever the right-hand side is finite. This condition can often be confirmed by using the fact that integration and differentiation can be swapped when either of the following cases hold:
  1. The function $f(x;\theta )$ has bounded support in x , and the bounds do not depend on $\theta$ ;
  2. The function $f(x;\theta )$ has infinite support, is continuously differentiable, and the integral converges uniformly for all $\theta$ .

## Proof

### Proof for the general case based on the Chapman–Robbins bound

Proof based on.

Proof

**First equation:**

Let $\delta$ be an infinitesimal, then for any $v\in \mathbb {R} ^{n}$ , plugging $\theta '=\theta +\delta v$ in, we have ${\displaystyle (E_{\theta '}[T]-E_{\theta }[T])=v^{T}\phi (\theta )\delta$

Plugging this into multivariate Chapman–Robbins bound gives $I(\theta )\geq \phi (\theta )\operatorname {Cov} _{\theta }[T]^{-1}\phi (\theta )^{T}$ .

**Second equation:**

It suffices to prove this for scalar case, with $h(X)$ taking values in $\mathbb {R}$ . Because for general $T(X)$ , we can take any $v\in \mathbb {R} ^{m}$ , then defining ${\textstyle h:=\sum _{j}v_{j}T_{j}}$ , the scalar case gives $\operatorname {Var} _{\theta }[h]=v^{T}\operatorname {Cov} _{\theta }[T]v\geq v^{T}\phi (\theta )I(\theta )^{-1}\phi (\theta )^{T}v$ This holds for all $v\in \mathbb {R} ^{m}$ , so we can conclude $\operatorname {Cov} _{\theta }[T]\geq \phi (\theta )I(\theta )^{-1}\phi (\theta )^{T}$ The scalar case states that $\operatorname {Var} _{\theta }[h]\geq \phi (\theta )^{T}I(\theta )^{-1}\phi (\theta )$ with $\phi (\theta ):=\nabla _{\theta }E_{\theta }[h]$ .

Let $\delta$ be an infinitesimal, then for any $v\in \mathbb {R} ^{n}$ , taking $\theta '=\theta +\delta v$ in the single-variate Chapman–Robbins bound gives $\operatorname {Var} _{\theta }[h]\geq {\frac {\langle v,\phi (\theta )\rangle ^{2}}{v^{T}I(\theta )v}}$ .

By linear algebra, $\sup _{v\neq 0}{\frac {\langle w,v\rangle ^{2}}{v^{T}Mv}}=w^{T}M^{-1}w$ for any positive-definite matrix M , thus we obtain $\operatorname {Var} _{\theta }[h]\geq \phi (\theta )^{T}I(\theta )^{-1}\phi (\theta ).$

### A standalone proof for the general scalar case

For the general scalar case:

Assume that $T=t(X)$ is an estimator with expectation $\psi (\theta )$ (based on the observations X ), i.e. that $\operatorname {E} (T)=\psi (\theta )$ . The goal is to prove that, for all $\theta$ ,

$\operatorname {var} (t(X))\geq {\frac {[\psi ^{\prime }(\theta )]^{2}}{I(\theta )}}.$

Let X be a random variable with probability density function $f(x;\theta )$ . Here $T=t(X)$ is a statistic, which is used as an estimator for $\psi (\theta )$ . Define V as the score:

$V={\frac {\partial }{\partial \theta }}\ln f(X;\theta )={\frac {1}{f(X;\theta )}}{\frac {\partial }{\partial \theta }}f(X;\theta )$

where the chain rule is used in the final equality above. Then the expectation of V , written $\operatorname {E} (V)$ , is zero. This is because:

$\operatorname {E} (V)=\int f(x;\theta )\left[{\frac {1}{f(x;\theta )}}{\frac {\partial }{\partial \theta }}f(x;\theta )\right]\,dx={\frac {\partial }{\partial \theta }}\int f(x;\theta )\,dx=0$

where the integral and partial derivative have been interchanged (justified by the second regularity condition).

If we consider the covariance $\operatorname {cov} (V,T)$ of V and T , we have $\operatorname {cov} (V,T)=\operatorname {E} (VT)$ , because $\operatorname {E} (V)=0$ . Expanding this expression we have

${\begin{aligned}\operatorname {cov} (V,T)&=\operatorname {E} \left(T\cdot \left[{\frac {1}{f(X;\theta )}}{\frac {\partial }{\partial \theta }}f(X;\theta )\right]\right)\\[6pt]&=\int t(x)\left[{\frac {1}{f(x;\theta )}}{\frac {\partial }{\partial \theta }}f(x;\theta )\right]f(x;\theta )\,dx\\[6pt]&={\frac {\partial }{\partial \theta }}\left[\int t(x)f(x;\theta )\,dx\right]={\frac {\partial }{\partial \theta }}E(T)=\psi ^{\prime }(\theta )\end{aligned}}$

again because the integration and differentiation operations commute (second condition).

The Cauchy–Schwarz inequality shows that

${\sqrt {\operatorname {var} (T)\operatorname {var} (V)}}\geq \left|\operatorname {cov} (V,T)\right|=\left|\psi ^{\prime }(\theta )\right|$

therefore

$\operatorname {var} (T)\geq {\frac {[\psi ^{\prime }(\theta )]^{2}}{\operatorname {var} (V)}}={\frac {[\psi ^{\prime }(\theta )]^{2}}{I(\theta )}}$

which proves the proposition.

## Examples

### Multivariate normal distribution

For the case of a *d*-variate normal distribution

${\boldsymbol {x}}\sim {\mathcal {N}}_{d}\left({\boldsymbol {\mu }}({\boldsymbol {\theta }}),{\boldsymbol {C}}({\boldsymbol {\theta }})\right)$

the Fisher information matrix has elements

$I_{m,k}={\frac {\partial {\boldsymbol {\mu }}^{T}}{\partial \theta _{m}}}{\boldsymbol {C}}^{-1}{\frac {\partial {\boldsymbol {\mu }}}{\partial \theta _{k}}}+{\frac {1}{2}}\operatorname {tr} \left({\boldsymbol {C}}^{-1}{\frac {\partial {\boldsymbol {C}}}{\partial \theta _{m}}}{\boldsymbol {C}}^{-1}{\frac {\partial {\boldsymbol {C}}}{\partial \theta _{k}}}\right)$

where "tr" is the trace.

For example, let $w[j]$ be a sample of n independent observations with unknown mean $\theta$ and known variance $\sigma ^{2}$ .

$w[j]\sim {\mathcal {N}}_{d,n}\left(\theta {\boldsymbol {1}},\sigma ^{2}{\boldsymbol {I}}\right).$

Then the Fisher information is a scalar given by

$I(\theta )=\left({\frac {\partial {\boldsymbol {\mu }}(\theta )}{\partial \theta }}\right)^{T}{\boldsymbol {C}}^{-1}\left({\frac {\partial {\boldsymbol {\mu }}(\theta )}{\partial \theta }}\right)=\sum _{i=1}^{n}{\frac {1}{\sigma ^{2}}}={\frac {n}{\sigma ^{2}}},$

and so the Cramér–Rao bound is

$\operatorname {var} ({\hat {\theta }})\geq {\frac {\sigma ^{2}}{n}}.$

### Normal variance with known mean

Suppose *X* is a normally distributed random variable with known mean $\mu$ and unknown variance $\sigma ^{2}$ . Consider the following statistic:

$T={\frac {\sum _{i=1}^{n}(X_{i}-\mu )^{2}}{n}}.$

Then *T* is unbiased for $\sigma ^{2}$ , as $E(T)=\sigma ^{2}$ . What is the variance of *T*?

$\operatorname {var} (T)=\operatorname {var} \left({\frac {\sum _{i=1}^{n}(X_{i}-\mu )^{2}}{n}}\right)={\frac {\sum _{i=1}^{n}\operatorname {var} (X_{i}-\mu )^{2}}{n^{2}}}={\frac {n\operatorname {var} (X-\mu )^{2}}{n^{2}}}={\frac {1}{n}}\left[\operatorname {E} \left\{(X-\mu )^{4}\right\}-\left(\operatorname {E} \{(X-\mu )^{2}\}\right)^{2}\right]$

(the second equality follows directly from the definition of variance and the fact that $X_{i}$ 's are independent). The first term is the fourth moment about the mean and has value $3(\sigma ^{2})^{2}$ ; the second is the square of the variance, or $(\sigma ^{2})^{2}$ . Thus

$\operatorname {var} (T)={\frac {2(\sigma ^{2})^{2}}{n}}.$

Now, what is the Fisher information in the sample? Recall that the score V is defined as

$V={\frac {\partial }{\partial \sigma ^{2}}}\log \left[L(\sigma ^{2},X)\right]$

where L is the likelihood function. Thus in this case,

$\log \left[L(\sigma ^{2},X)\right]=\log \left[{\frac {1}{\sqrt {2\pi \sigma ^{2}}}}e^{-(X-\mu )^{2}/{2\sigma ^{2}}}\right]=-\log({\sqrt {2\pi \sigma ^{2}}})-{\frac {(X-\mu )^{2}}{2\sigma ^{2}}}$

$V={\frac {\partial }{\partial \sigma ^{2}}}\log \left[L(\sigma ^{2},X)\right]={\frac {\partial }{\partial \sigma ^{2}}}\left[-\log({\sqrt {2\pi \sigma ^{2}}})-{\frac {(X-\mu )^{2}}{2\sigma ^{2}}}\right]=-{\frac {1}{2\sigma ^{2}}}+{\frac {(X-\mu )^{2}}{2(\sigma ^{2})^{2}}}$

where the second equality is from elementary calculus. Thus, the information in a single observation is just minus the expectation of the derivative of V , or

$I=-\operatorname {E} \left({\frac {\partial V}{\partial \sigma ^{2}}}\right)=-\operatorname {E} \left(-{\frac {(X-\mu )^{2}}{(\sigma ^{2})^{3}}}+{\frac {1}{2(\sigma ^{2})^{2}}}\right)={\frac {\sigma ^{2}}{(\sigma ^{2})^{3}}}-{\frac {1}{2(\sigma ^{2})^{2}}}={\frac {1}{2(\sigma ^{2})^{2}}}.$

Thus the information in a sample of n independent observations is just n times this, or ${\frac {n}{2(\sigma ^{2})^{2}}}.$

The Cramér–Rao bound states that

$\operatorname {var} (T)\geq {\frac {1}{I}}.$

In this case, the inequality is saturated (equality is achieved), showing that the estimator is efficient.

However, we can achieve a lower mean squared error using a biased estimator. The estimator

$T={\frac {\sum _{i=1}^{n}(X_{i}-\mu )^{2}}{n+2}}.$

obviously has a smaller variance, which is in fact

$\operatorname {var} (T)={\frac {2n(\sigma ^{2})^{2}}{(n+2)^{2}}}.$

Its bias is

$\left(1-{\frac {n}{n+2}}\right)\sigma ^{2}={\frac {2\sigma ^{2}}{n+2}}$

so its mean squared error is

$\operatorname {MSE} (T)=\left({\frac {2n}{(n+2)^{2}}}+{\frac {4}{(n+2)^{2}}}\right)(\sigma ^{2})^{2}={\frac {2(\sigma ^{2})^{2}}{n+2}}$

which is less than what unbiased estimators can achieve according to the Cramér–Rao bound.

When the mean is not known, the minimum mean squared error estimate of the variance of a sample from Gaussian distribution is achieved by dividing by $n+1$ , rather than $n-1$ or $n+2$ .
