---
title: "Gaussian process"
source: https://en.wikipedia.org/wiki/Gaussian_process
domain: stochastic-processes
license: CC-BY-SA-4.0
tags: stochastic process, wiener process, brownian motion, stochastic calculus
fetched: 2026-07-02
---

# Gaussian process

In probability theory and statistics, a **Gaussian process** is a stochastic process (a collection of random variables indexed by time or space), such that every finite collection of those random variables has a multivariate normal distribution. The distribution of a Gaussian process is the joint distribution of all those (infinitely many) random variables, and as such, it is a distribution over functions with a continuous domain, e.g. time or space.

The concept of Gaussian processes is named after Carl Friedrich Gauss because it is based on the notion of the Gaussian distribution (normal distribution). Gaussian processes can be seen as an infinite-dimensional generalization of multivariate normal distributions.

Gaussian processes are useful in statistical modelling, benefiting from properties inherited from the normal distribution. For example, if a random process is modelled as a Gaussian process, the distributions of various derived quantities can be obtained explicitly. Such quantities include the average value of the process over a range of times and the error in estimating the average using sample values at a small set of times. While exact models often scale poorly as the amount of data increases, multiple approximation methods have been developed which often retain good accuracy while drastically reducing computation time.

## Definition

A time continuous stochastic process $\left\{X_{t};t\in T\right\}$ is Gaussian if and only if for every finite set of indices $t_{1},\ldots ,t_{k}$ in the index set T

$\mathbf {X} _{t_{1},\ldots ,t_{k}}=(X_{t_{1}},\ldots ,X_{t_{k}})$

is a multivariate Gaussian random variable. As the sum of independent and Gaussian distributed random variables is again Gaussian distributed, that is the same as saying every linear combination of $(X_{t_{1}},\ldots ,X_{t_{k}})$ has a univariate Gaussian (or normal) distribution.

Using characteristic functions of random variables with i denoting the imaginary unit such that $i^{2}=-1$ , the Gaussian property can be formulated as follows: $\left\{X_{t};t\in T\right\}$ is Gaussian if and only if, for every finite set of indices $t_{1},\ldots ,t_{k}$ , there are real-valued $\sigma _{\ell j}^{2}$ , $\mu _{\ell }$ with $\sigma _{jj}^{2}>0$ such that the following equality holds for all $s_{1},s_{2},\ldots ,s_{k}\in \mathbb {R}$ ,

${\mathbb {E} }\left[\exp \left(i\sum _{\ell =1}^{k}s_{\ell }\,\mathbf {X} _{t_{\ell }}\right)\right]=\exp \left(-{\tfrac {1}{2}}\sum _{\ell ,j}\sigma _{\ell j}^{2}s_{\ell }s_{j}+i\sum _{\ell }\mu _{\ell }s_{\ell }\right),$

or ${\mathbb {E} }\left[{\mathrm {e} }^{i\,\mathbf {s} \,(\mathbf {X} _{t}-\mathbf {\mu } )}\right]={\mathrm {e} }^{-\mathbf {s} \,\sigma ^{2}\,\mathbf {s} /2}$ . The numbers $\sigma _{\ell j}^{2}$ and $\mu _{\ell }$ can be shown to be the covariances and means of the variables in the process.

## Stationarity

For general stochastic processes strict-sense stationarity implies wide-sense stationarity but not every wide-sense stationary stochastic process is strict-sense stationary. However, for a Gaussian stochastic process the two concepts are equivalent.

Therefore, stationary Gaussian process is completely determined by its one-parameter mean function and covariance function.

## Example

There is an explicit representation for stationary Gaussian processes. A simple example of this representation is

$X_{t}=\cos(at)\,\xi _{1}+\sin(at)\,\xi _{2}$

where $\xi _{1}$ and $\xi _{2}$ are independent random variables with the standard normal distribution.

## Covariance functions

A key fact of Gaussian processes is that they can be completely defined by their second-order statistics. Thus, if a Gaussian process is assumed to have mean zero, defining the covariance function completely defines the process' behaviour. Importantly the non-negative definiteness of this function enables its spectral decomposition using the Karhunen–Loève expansion. Basic aspects that can be defined through the covariance function are the process' stationarity, isotropy, smoothness and periodicity.

Stationarity refers to the process' behaviour regarding the separation of any two points x and $x'$ . If the process is stationary, the covariance function depends only on $x-x'$ . For example, the Ornstein–Uhlenbeck process is stationary.

If the process depends only on $|x-x'|$ , the Euclidean distance (not the direction) between x and $x'$ , then the process is considered isotropic. A process that is concurrently stationary and isotropic is considered to be homogeneous; in practice these properties reflect the differences (or rather the lack of them) in the behaviour of the process given the location of the observer.

Ultimately Gaussian processes translate as taking priors on functions and the smoothness of these priors can be induced by the covariance function. If we expect that for "near-by" input points x and $x'$ their corresponding output points y and $y'$ to be "near-by" also, then the assumption of continuity is present. If we wish to allow for significant displacement then we might choose a rougher covariance function. Extreme examples of the behaviour is the Ornstein–Uhlenbeck covariance function and the squared exponential where the former is never differentiable and the latter infinitely differentiable.

Periodicity refers to inducing periodic patterns within the behaviour of the process. Formally, this is achieved by mapping the input x to a two dimensional vector $u(x)=\left(\cos(x),\sin(x)\right)$ .

### Usual covariance functions

There are a number of common covariance functions:

- Constant : $K_{\operatorname {C} }(x,x')=C$
- Linear: $K_{\operatorname {L} }(x,x')=x^{\mathsf {T}}x'$
- white Gaussian noise: $K_{\operatorname {GN} }(x,x')=\sigma ^{2}\delta _{x,x'}$
- Squared exponential: $K_{\operatorname {SE} }(x,x')=\exp \left(-{\tfrac {d^{2}}{2\ell ^{2}}}\right)$
- Ornstein–Uhlenbeck: $K_{\operatorname {OU} }(x,x')=\exp \left(-{\tfrac {d}{\ell }}\right)$
- Matérn: $K_{\operatorname {Matern} }(x,x')={\tfrac {2^{1-\nu }}{\Gamma (\nu )}}\left({\tfrac {{\sqrt {2\nu }}d}{\ell }}\right)^{\nu }K_{\nu }\left({\tfrac {{\sqrt {2\nu }}d}{\ell }}\right)$
- Periodic: $K_{\operatorname {P} }(x,x')=\exp \left(-{\tfrac {2}{\ell ^{2}}}\sin ^{2}(d/2)\right)$
- Rational quadratic: $K_{\operatorname {RQ} }(x,x')=\left(1+d^{2}\right)^{-\alpha },\quad \alpha \geq 0$

Here $d=|x-x'|$ , which is a result of the stationary process property, that is, for any stationary process the covariance function will only depend on d . The parameter $\ell$ is the characteristic length-scale of the process (practically, "how close" two points x and $x'$ have to be to influence each other significantly), *$\delta$* is the Kronecker delta and $\sigma$ the standard deviation of the noise fluctuations. Moreover, $K_{\nu }$ is the modified Bessel function of order $\nu$ and $\Gamma (\nu )$ is the gamma function evaluated at $\nu$ . Importantly, a complicated covariance function can be defined as a linear combination of other simpler covariance functions in order to incorporate different insights about the data-set at hand.

The inferential results are dependent on the values of the hyperparameters $\theta$ (e.g. $\ell$ and $\sigma$ ) defining the model's behaviour. A popular choice for $\theta$ is to provide *maximum a posteriori* (MAP) estimates of it with some chosen prior. If the prior is very near uniform, this is the same as maximizing the marginal likelihood of the process; the marginalization being done over the observed process values y . This approach is also known as *maximum likelihood II*, *evidence maximization*, or *empirical Bayes*.

## Continuity

For a Gaussian process, continuity in probability is equivalent to mean-square continuity and continuity with probability one is equivalent to sample continuity. The latter implies, but is not implied by, continuity in probability. Continuity in probability holds if and only if the mean and autocovariance are continuous functions. In contrast, sample continuity was challenging even for stationary Gaussian processes (as probably noted first by Andrey Kolmogorov), and more challenging for more general processes. As usual, by a sample continuous process one means a process that admits a sample continuous modification.

### Stationary case

For a stationary Gaussian process $X=(X_{t})_{t\in \mathbb {R} },$ some conditions on its spectrum are sufficient for sample continuity, but fail to be necessary. A necessary and sufficient condition, sometimes called Dudley–Fernique theorem, involves the function $\sigma$ defined by $\sigma (h)={\sqrt {{\mathbb {E} }\left[\left(X(t+h)-X(t)\right)^{2}\right]}}$ (the right-hand side does not depend on t due to stationarity). Continuity of X in probability is equivalent to continuity of $\sigma$ at $0.$ When convergence of $\sigma (h)$ to 0 (as $h\to 0$ ) is too slow, sample continuity of X may fail. Convergence of the following integrals matters: $I(\sigma )=\int _{0}^{1}{\frac {\sigma (h)}{h{\sqrt {\log(1/h)}}}}\,dh=\int _{0}^{\infty }2\sigma (e^{-x^{2}})\,dx,$ these two integrals being equal according to integration by substitution ${\textstyle h=e^{-x^{2}},}$ ${\textstyle x={\sqrt {\log(1/h)}}.}$ The first integrand need not be bounded as $h\to 0+,$ thus the integral may converge ( $I(\sigma )<\infty$ ) or diverge ( $I(\sigma )=\infty$ ). Taking for example ${\textstyle \sigma (e^{-x^{2}})={\tfrac {1}{x^{a}}}}$ for large $x,$ that is, ${\textstyle \sigma (h)=(\log(1/h))^{-a/2}}$ for small $h,$ one obtains $I(\sigma )<\infty$ when $a>1,$ and $I(\sigma )=\infty$ when $0<a\leq 1.$ In these two cases the function $\sigma$ is increasing on $[0,\infty ),$ but generally it is not. Moreover, the condition

(*)

there exists

$\varepsilon >0$

such that

$\sigma$

is monotone on

$[0,\varepsilon ]$

does not follow from continuity of $\sigma$ and the evident relations $\sigma (h)\geq 0$ (for all h ) and $\sigma (0)=0.$

**Theorem 1**—Let $\sigma$ be continuous and satisfy (*). Then the condition $I(\sigma )<\infty$ is necessary and sufficient for sample continuity of $X.$

Some history. Sufficiency was announced by Xavier Fernique in 1964, but the first proof was published by Richard M. Dudley in 1967. Necessity was proved by Michael B. Marcus and Lawrence Shepp in 1970.

There exist sample continuous processes X such that $I(\sigma )=\infty ;$ they violate condition (*). An example found by Marcus and Shepp is a random lacunary Fourier series $X_{t}=\sum _{n=1}^{\infty }c_{n}(\xi _{n}\cos \lambda _{n}t+\eta _{n}\sin \lambda _{n}t),$ where $\xi _{1},\eta _{1},\xi _{2},\eta _{2},\dots$ are independent random variables with standard normal distribution; frequencies $0<\lambda _{1}<\lambda _{2}<\dots$ are a fast growing sequence; and coefficients $c_{n}>0$ satisfy ${\textstyle \sum _{n}c_{n}<\infty .}$ The latter relation implies

${\textstyle {\mathbb {E} }\sum _{n}c_{n}(|\xi _{n}|+|\eta _{n}|)=\sum _{n}c_{n}{\mathbb {E} }[|\xi _{n}|+|\eta _{n}|]={\text{const}}\cdot \sum _{n}c_{n}<\infty ,}$

whence ${\textstyle \sum _{n}c_{n}(|\xi _{n}|+|\eta _{n}|)<\infty }$ almost surely, which ensures uniform convergence of the Fourier series almost surely, and sample continuity of $X.$

Its autocovariation function ${\mathbb {E} }[X_{t}X_{t+h}]=\sum _{n=1}^{\infty }c_{n}^{2}\cos \lambda _{n}h$ is nowhere monotone (see the picture), as well as the corresponding function $\sigma ,$ $\sigma (h)={\sqrt {2{\mathbb {E} }[X_{t}X_{t}]-2{\mathbb {E} }[X_{t}X_{t+h}]}}=2{\sqrt {\sum _{n=1}^{\infty }c_{n}^{2}\sin ^{2}{\frac {\lambda _{n}h}{2}}}}.$

## Brownian motion as the integral of Gaussian processes

A Wiener process (also known as Brownian motion) is the integral of a white noise generalized Gaussian process. It is not stationary, but it has stationary increments.

The Ornstein–Uhlenbeck process is a stationary Gaussian process.

The Brownian bridge is (like the Ornstein–Uhlenbeck process) an example of a Gaussian process whose increments are not independent.

The fractional Brownian motion is a Gaussian process whose covariance function is a generalisation of that of the Wiener process.

## RKHS structure and Gaussian process

Let f be a mean-zero Gaussian process $\left\{X_{t};t\in T\right\}$ with a non-negative definite covariance function K and let R be a symmetric and positive semidefinite function. Then, there exists a Gaussian process X which has the covariance R . Moreover, the reproducing kernel Hilbert space (RKHS) associated to R coincides with the Cameron–Martin theorem associated space $R(H)$ of X , and all the spaces $R(H)$ , $H_{X}$ , and ${\mathcal {H}}(K)$ are isometric. From now on, let ${\mathcal {H}}(R)$ be a reproducing kernel Hilbert space with positive definite kernel R .

Driscoll's zero-one law is a result characterizing the sample functions generated by a Gaussian process: $\lim _{n\to \infty }\operatorname {tr} [K_{n}R_{n}^{-1}]<\infty ,$ where $K_{n}$ and $R_{n}$ are the covariance matrices of all possible pairs of n points, implies $\Pr[f\in {\mathcal {H}}(R)]=1.$

Moreover, $\lim _{n\to \infty }\operatorname {tr} [K_{n}R_{n}^{-1}]=\infty$ implies $\Pr[f\in {\mathcal {H}}(R)]=0.$

This has significant implications when $K=R$ , as $\lim _{n\to \infty }\operatorname {tr} [R_{n}R_{n}^{-1}]=\lim _{n\to \infty }\operatorname {tr} [I]=\lim _{n\to \infty }n=\infty .$

As such, almost all sample paths of a mean-zero Gaussian process with positive definite kernel K will lie outside of the Hilbert space ${\mathcal {H}}(K)$ .

## Linearly constrained Gaussian processes

For many applications of interest some pre-existing knowledge about the system at hand is already given. Consider e.g. the case where the output of the Gaussian process corresponds to a magnetic field; here, the real magnetic field is bound by Maxwell's equations and a way to incorporate this constraint into the Gaussian process formalism would be desirable as this would likely improve the accuracy of the algorithm.

A method on how to incorporate linear constraints into Gaussian processes already exists:

Consider the (vector valued) output function $f(x)$ which is known to obey the linear constraint (i.e. ${\mathcal {F}}_{X}$ is a linear operator) ${\mathcal {F}}_{X}(f(x))=0.$ Then the constraint ${\mathcal {F}}_{X}$ can be fulfilled by choosing $f(x)={\mathcal {G}}_{X}(g(x))$ , where $g(x)\sim {\mathcal {GP}}(\mu _{g},K_{g})$ is modelled as a Gaussian process, and finding ${\mathcal {G}}_{X}$ such that ${\mathcal {F}}_{X}({\mathcal {G}}_{X}(g))=0\qquad \forall g.$ Given ${\mathcal {G}}_{X}$ and using the fact that Gaussian processes are closed under linear transformations, the Gaussian process for f obeying constraint ${\mathcal {F}}_{X}$ becomes $f(x)={\mathcal {G}}_{X}g\sim {\mathcal {GP}}({\mathcal {G}}_{X}\mu _{g},{\mathcal {G}}_{X}K_{g}{\mathcal {G}}_{X'}^{\mathsf {T}}).$ Hence, linear constraints can be encoded into the mean and covariance function of a Gaussian process.

## Applications

A Gaussian process can be used as a prior probability distribution over functions in Bayesian inference. Given any set of *N* points in the desired domain of the functions, take a multivariate Gaussian whose covariance matrix parameter is the Gram matrix of those *N* points with some desired kernel, and sample from that Gaussian. For solution of the multi-output prediction problem, Gaussian process regression for vector-valued function was developed. In this method, a 'big' covariance is constructed, which describes the correlations between all the input and output variables taken in *N* points in the desired domain. This approach was elaborated in detail for the matrix-valued Gaussian processes and generalised to processes with 'heavier tails' like Student-t processes.

Inference of continuous values with a Gaussian process prior is known as Gaussian process regression, or kriging; extending Gaussian process regression to multiple target variables is known as *cokriging*. Gaussian processes are thus useful as a powerful non-linear multivariate interpolation tool. Kriging is also used to extend Gaussian process in the case of mixed integer inputs.

Gaussian processes are also commonly used to tackle numerical analysis problems such as numerical integration, solving differential equations, or optimisation in the field of probabilistic numerics.

Gaussian processes can also be used in the context of mixture of experts models, for example. The underlying rationale of such a learning framework consists in the assumption that a given mapping cannot be well captured by a single Gaussian process model. Instead, the observation space is divided into subsets, each of which is characterized by a different mapping function; each of these is learned via a different Gaussian process component in the postulated mixture.

### Gaussian process prediction, or Kriging

When concerned with a general Gaussian process regression problem (Kriging), it is assumed that for a Gaussian process f observed at coordinates x , the vector of values ⁠ $f(x)$ ⁠ is just one sample from a multivariate Gaussian distribution of dimension equal to the number of observed coordinates ⁠ n ⁠. Therefore, under the assumption of a zero-mean distribution, ⁠ $f(x')\sim N(0,K(\theta ,x,x'))$ ⁠, where ⁠ $K(\theta ,x,x')$ ⁠ is the covariance matrix between all possible pairs ⁠ $(x,x')$ ⁠ for a given set of hyperparameters *θ*. As such the log marginal likelihood is:

$\log p(f(x')\mid \theta ,x)=-{\frac {1}{2}}\left(f^{\mathsf {T}}(x)K^{-1}(\theta ,x,x')f(x')+\log \det(K(\theta ,x,x'))+n\log 2\pi \right)$

and maximizing this marginal likelihood towards θ provides the complete specification of the Gaussian process *f*. One can briefly note at this point that the first term corresponds to a penalty term for a model's failure to fit observed values and the second term to a penalty term that increases proportionally to a model's complexity. Having specified θ, making predictions about unobserved values ⁠ $f(x^{*})$ ⁠ at coordinates *x** is then only a matter of drawing samples from the predictive distribution $p(y^{*}\mid x^{*},f(x),x)=N(y^{*}\mid A,B)$ where the posterior mean estimate A is defined as $A=K(\theta ,x^{*},x)K^{-1}(\theta ,x,x')f(x)$ and the posterior variance estimate *B* is defined as: $B=K(\theta ,x^{*},x^{*})-K(\theta ,x^{*},x)K^{-1}(\theta ,x,x')K^{\mathsf {T}}(\theta ,x^{*},x)$ where ⁠ $K(\theta ,x^{*},x)$ ⁠ is the covariance between the new coordinate of estimation *x** and all other observed coordinates *x* for a given hyperparameter vector θ, ⁠ $K(\theta ,x,x')$ ⁠ and ⁠ $f(x)$ ⁠ are defined as before and ⁠ $K(\theta ,x^{*},x^{*})$ ⁠ is the variance at point *x** as dictated by θ. Practically, the posterior mean estimate of ⁠ $f(x^{*})$ ⁠ (the "point estimate") is just a linear combination of the observations ⁠ $f(x)$ ⁠; in a similar manner the variance of ⁠ $f(x^{*})$ ⁠ is actually independent of the observations ⁠ $f(x)$ ⁠. A known bottleneck in Gaussian process prediction is that the computational complexity of inference and likelihood evaluation is cubic in the number of points |*x*|, and as such can become unfeasible for larger data sets. Works on sparse Gaussian processes, that usually are based on the idea of building a *representative set* for the given process *f*, try to circumvent this issue. The kriging method can be used in the latent level of a nonlinear mixed-effects model for a spatial functional prediction: this technique is called the latent kriging. Other classes of scalable Gaussian process for analyzing massive datasets have emerged from the Vecchia approximation and Nearest Neighbor Gaussian Processes (NNGP).

Often, the covariance has the form ${\textstyle K(\theta ,x,x')={\frac {1}{\sigma ^{2}}}{\tilde {K}}(\theta ,x,x')}$ , where $\sigma ^{2}$ is a scaling parameter. Examples are the Matérn class covariance functions. If this scaling parameter $\sigma ^{2}$ is either known or unknown (i.e. must be marginalized), then the posterior probability, $p(\theta \mid D)$ , i.e. the probability for the hyperparameters $\theta$ given a set of data pairs D of observations of x and $f(x)$ , admits an analytical expression.

### Bayesian neural networks as Gaussian processes

Bayesian neural networks are a particular type of Bayesian network that results from treating deep learning and artificial neural network models probabilistically, and assigning a prior distribution to their parameters. Computation in artificial neural networks is usually organized into sequential layers of artificial neurons. The number of neurons in a layer is called the layer width. As layer width grows large, many Bayesian neural networks reduce to a Gaussian process with a closed form compositional kernel. This Gaussian process is called the Neural Network Gaussian Process (NNGP) (not to be confused with the Nearest Neighbor Gaussian Process ). It allows predictions from Bayesian neural networks to be more efficiently evaluated, and provides an analytic tool to understand deep learning models.

### Physical applications

Gaussian processes have found increasing applications in many domains of the natural sciences due to their statistical modelling properties. Molecular property prediction has employed these process models in small molecular datasets due to their inference capabilities and computational costs. They are also being increasingly used as surrogate models for force field optimization.

#### Astrophysics

Gaussian processes have also found extensive use in astrophysical and astronomical settings. Gaussian processes can model correlated noise, a specific type of non-Gaussian noise dependent on some underlying unknown distribution correlated with observed values. This type of noise is often present in astronomical signals as instrumental systematics or as intrinsic to the observed object as a result of physical processes. Correlated noise is often a consideration for exoplanet transit events, and Gaussian processes have been used to de-trend these transit light curves (at timescales greater than that of the transit) to allow detection of weaker, more short-lived signals. These processes have also been used to disentangle planetary signals from stellar activity indicators inside radial velocity data, another method of exoplanet detection. This is done by training the Gaussian process model to optimize the hyperparameters of the kernel until it accurately recreates the noise components of the radial velocity data, which ultimately allows it to determine which signals are best defined as strictly periodic (which the planet should be) and which signals are best represented by the evolving, quasi-periodic kernel (which the star should be). Correlated noise produced by active regions on a star's photosphere (as a result of magnetic field interactions) can be of similar timescales as transit events, and Gaussian process models which handle sparsely sampled data are used to confirm exoplanet detections especially around young stars.

The variability of rotating, magnetically active Sun-like stars can be modeled fairly accurately using Gaussian processes. This quasi-periodic variability is often represented by a covariance function given as ${\text{K}}_{\text{QP}}(x,x')=\alpha ^{2}\exp \left(-{\frac {d^{2}}{2\lambda _{1}^{2}}}-\Gamma \sin ^{2}\left[{\frac {\pi d}{\lambda _{2}}}\right]\right)$ where parameter $\alpha$ is amplitude, $\lambda _{1}$ is period, and $\lambda _{2}$ is decoherence timescale. This covariance function allows for the limited but feasible determination of stellar periods as a result of parameter $\lambda _{1}$ but lacks physical information about where these active regions are on the star observed.

Gaussian processes are also used in the analysis of individual and populations of active galactic nuclei (AGNs) due to their stochastic variability in the optical and radio parts of the electromagnetic spectrum. Damped random walk kernels in particular have previously been used to identify the extent of broad-line emission regions around supermassive black holes using reverberation mapping, and these kernels can also be used to characterize light curve variations for large AGN populations.

Other astrophysical applications of Gaussian processes include models for pulsar timing and dispersion measure, gravitational wave structure and detector uncertainty (notably in the LIGO-Virgo-KAGRA collaboration), transient classification, and quasi-periodic oscillations.

## Computational issues

In practical applications, Gaussian process models are often evaluated on a grid leading to multivariate normal distributions. Using these models for prediction or parameter estimation using maximum likelihood requires evaluating a multivariate Gaussian density, which involves calculating the determinant and the inverse of the covariance matrix. Both of these operations have cubic computational complexity which means that even for grids of modest sizes, both operations can have a prohibitive computational cost. This drawback led to the development of multiple approximation methods.
