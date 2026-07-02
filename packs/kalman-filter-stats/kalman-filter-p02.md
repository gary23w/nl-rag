---
title: "Kalman filter (part 2/2)"
source: https://en.wikipedia.org/wiki/Kalman_filter
domain: kalman-filter-stats
license: CC-BY-SA-4.0
tags: Kalman filter, extended Kalman filter, unscented transform, particle filter
fetched: 2026-07-02
part: 2/2
---

## Relationship to recursive Bayesian estimation

The Kalman filter can be presented as one of the simplest dynamic Bayesian networks. The Kalman filter calculates estimates of the true values of states recursively over time using incoming measurements and a mathematical process model. Similarly, recursive Bayesian estimation calculates estimates of an unknown probability density function (PDF) recursively over time using incoming measurements and a mathematical process model.

In recursive Bayesian estimation, the true state is assumed to be an unobserved Markov process, and the measurements are the observed states of a hidden Markov model (HMM).

Because of the Markov assumption, the true state is conditionally independent of all earlier states given the immediately previous state.

$p(\mathbf {x} _{k}\mid \mathbf {x} _{0},\dots ,\mathbf {x} _{k-1})=p(\mathbf {x} _{k}\mid \mathbf {x} _{k-1})$

Similarly, the measurement at the *k*-th timestep is dependent only upon the current state and is conditionally independent of all other states given the current state.

$p(\mathbf {z} _{k}\mid \mathbf {x} _{0},\dots ,\mathbf {x} _{k})=p(\mathbf {z} _{k}\mid \mathbf {x} _{k})$

Using these assumptions the probability distribution over all states of the hidden Markov model can be written simply as:

$p\left(\mathbf {x} _{0},\dots ,\mathbf {x} _{k},\mathbf {z} _{1},\dots ,\mathbf {z} _{k}\right)=p\left(\mathbf {x} _{0}\right)\prod _{i=1}^{k}p\left(\mathbf {z} _{i}\mid \mathbf {x} _{i}\right)p\left(\mathbf {x} _{i}\mid \mathbf {x} _{i-1}\right)$

However, when a Kalman filter is used to estimate the state **x**, the probability distribution of interest is that associated with the current states conditioned on the measurements up to the current timestep. This is achieved by marginalizing out the previous states and dividing by the probability of the measurement set.

This results in the *predict* and *update* phases of the Kalman filter written probabilistically. The probability distribution associated with the predicted state is the sum (integral) of the products of the probability distribution associated with the transition from the (*k* − 1)-th timestep to the *k*-th and the probability distribution associated with the previous state, over all possible $x_{k-1}$ .

$p\left(\mathbf {x} _{k}\mid \mathbf {Z} _{k-1}\right)=\int p\left(\mathbf {x} _{k}\mid \mathbf {x} _{k-1}\right)p\left(\mathbf {x} _{k-1}\mid \mathbf {Z} _{k-1}\right)\,d\mathbf {x} _{k-1}$

The measurement set up to time *t* is

$\mathbf {Z} _{t}=\left\{\mathbf {z} _{1},\dots ,\mathbf {z} _{t}\right\}$

The probability distribution of the update is proportional to the product of the measurement likelihood and the predicted state.

$p\left(\mathbf {x} _{k}\mid \mathbf {Z} _{k}\right)={\frac {p\left(\mathbf {z} _{k}\mid \mathbf {x} _{k}\right)p\left(\mathbf {x} _{k}\mid \mathbf {Z} _{k-1}\right)}{p\left(\mathbf {z} _{k}\mid \mathbf {Z} _{k-1}\right)}}$

The denominator

$p\left(\mathbf {z} _{k}\mid \mathbf {Z} _{k-1}\right)=\int p\left(\mathbf {z} _{k}\mid \mathbf {x} _{k}\right)p\left(\mathbf {x} _{k}\mid \mathbf {Z} _{k-1}\right)\,d\mathbf {x} _{k}$

is a normalization term.

The remaining probability density functions are

${\begin{aligned}p\left(\mathbf {x} _{k}\mid \mathbf {x} _{k-1}\right)&={\mathcal {N}}\left(\mathbf {F} _{k}\mathbf {x} _{k-1}+\mathbf {B} _{k}\mathbf {u} _{k},\mathbf {Q} _{k}\right)\\p\left(\mathbf {z} _{k}\mid \mathbf {x} _{k}\right)&={\mathcal {N}}\left(\mathbf {H} _{k}\mathbf {x} _{k},\mathbf {R} _{k}\right)\\p\left(\mathbf {x} _{k-1}\mid \mathbf {Z} _{k-1}\right)&={\mathcal {N}}\left({\hat {\mathbf {x} }}_{k-1},\mathbf {P} _{k-1}\right)\end{aligned}}$

The PDF at the previous timestep is assumed inductively to be the estimated state and covariance. This is justified because, as an optimal estimator, the Kalman filter makes best use of the measurements, therefore the PDF for $\mathbf {x} _{k}$ given the measurements $\mathbf {Z} _{k}$ is the Kalman filter estimate.


## Marginal likelihood

Related to the recursive Bayesian interpretation described above, the Kalman filter can be viewed as a generative model, i.e., a process for *generating* a stream of random observations **z** = (**z**0, **z**1, **z**2, ...). Specifically, the process is

1. Sample a hidden state $\mathbf {x} _{0}$ from the Gaussian prior distribution $p\left(\mathbf {x} _{0}\right)={\mathcal {N}}\left({\hat {\mathbf {x} }}_{0\mid 0},\mathbf {P} _{0\mid 0}\right)$ .
2. Sample an observation $\mathbf {z} _{0}$ from the observation model $p\left(\mathbf {z} _{0}\mid \mathbf {x} _{0}\right)={\mathcal {N}}\left(\mathbf {H} _{0}\mathbf {x} _{0},\mathbf {R} _{0}\right)$ .
3. For $k=1,2,3,\ldots$ , do
  1. Sample the next hidden state $\mathbf {x} _{k}$ from the transition model $p\left(\mathbf {x} _{k}\mid \mathbf {x} _{k-1}\right)={\mathcal {N}}\left(\mathbf {F} _{k}\mathbf {x} _{k-1}+\mathbf {B} _{k}\mathbf {u} _{k},\mathbf {Q} _{k}\right).$
  2. Sample an observation $\mathbf {z} _{k}$ from the observation model $p\left(\mathbf {z} _{k}\mid \mathbf {x} _{k}\right)={\mathcal {N}}\left(\mathbf {H} _{k}\mathbf {x} _{k},\mathbf {R} _{k}\right).$

This process has identical structure to the hidden Markov model, except that the discrete state and observations are replaced with continuous variables sampled from Gaussian distributions.

In some applications, it is useful to compute the *probability* that a Kalman filter with a given set of parameters (prior distribution, transition and observation models, and control inputs) would generate a particular observed signal. This probability is known as the marginal likelihood because it integrates over ("marginalizes out") the values of the hidden state variables, so it can be computed using only the observed signal. The marginal likelihood can be useful to evaluate different parameter choices, or to compare the Kalman filter against other models using Bayesian model comparison.

It is straightforward to compute the marginal likelihood as a side effect of the recursive filtering computation. By the chain rule, the likelihood can be factored as the product of the probability of each observation given previous observations,

$p(\mathbf {z} )=\prod _{k=0}^{T}p\left(\mathbf {z} _{k}\mid \mathbf {z} _{k-1},\ldots ,\mathbf {z} _{0}\right)$

,

and because the Kalman filter describes a Markov process, all relevant information from previous observations is contained in the current state estimate ${\hat {\mathbf {x} }}_{k\mid k-1},\mathbf {P} _{k\mid k-1}.$ Thus the marginal likelihood is given by

${\begin{aligned}p(\mathbf {z} )&=\prod _{k=0}^{T}\int p\left(\mathbf {z} _{k}\mid \mathbf {x} _{k}\right)p\left(\mathbf {x} _{k}\mid \mathbf {z} _{k-1},\ldots ,\mathbf {z} _{0}\right)d\mathbf {x} _{k}\\&=\prod _{k=0}^{T}\int {\mathcal {N}}\left(\mathbf {z} _{k};\mathbf {H} _{k}\mathbf {x} _{k},\mathbf {R} _{k}\right){\mathcal {N}}\left(\mathbf {x} _{k};{\hat {\mathbf {x} }}_{k\mid k-1},\mathbf {P} _{k\mid k-1}\right)d\mathbf {x} _{k}\\&=\prod _{k=0}^{T}{\mathcal {N}}\left(\mathbf {z} _{k};\mathbf {H} _{k}{\hat {\mathbf {x} }}_{k\mid k-1},\mathbf {R} _{k}+\mathbf {H} _{k}\mathbf {P} _{k\mid k-1}\mathbf {H} _{k}^{\textsf {T}}\right)\\&=\prod _{k=0}^{T}{\mathcal {N}}\left(\mathbf {z} _{k};\mathbf {H} _{k}{\hat {\mathbf {x} }}_{k\mid k-1},\mathbf {S} _{k}\right),\end{aligned}}$

i.e., a product of Gaussian densities, each corresponding to the density of one observation **z***k* under the current filtering distribution $\mathbf {H} _{k}{\hat {\mathbf {x} }}_{k\mid k-1},\mathbf {S} _{k}$ . This can easily be computed as a simple recursive update; however, to avoid numeric underflow, in a practical implementation it is usually desirable to compute the *log* marginal likelihood $\ell =\log p(\mathbf {z} )$ instead. Adopting the convention $\ell ^{(-1)}=0$ , this can be done via the recursive update rule

$\ell ^{(k)}=\ell ^{(k-1)}-{\frac {1}{2}}\left({\tilde {\mathbf {y} }}_{k}^{\textsf {T}}\mathbf {S} _{k}^{-1}{\tilde {\mathbf {y} }}_{k}+\log \left|\mathbf {S} _{k}\right|+d_{y}\log 2\pi \right),$

where $d_{y}$ is the dimension of the measurement vector.

An important application where such a (log) likelihood of the observations (given the filter parameters) is used is multi-target tracking. For example, consider an object tracking scenario where a stream of observations is the input, however, it is unknown how many objects are in the scene (or, the number of objects is known but is greater than one). For such a scenario, it can be unknown apriori which observations/measurements were generated by which object. A multiple hypothesis tracker (MHT) typically will form different track association hypotheses, where each hypothesis can be considered as a Kalman filter (for the linear Gaussian case) with a specific set of parameters associated with the hypothesized object. Thus, it is important to compute the likelihood of the observations for the different hypotheses under consideration, such that the most-likely one can be found.


## Information filter

In cases where the dimension of the observation vector **y** is bigger than the dimension of the state space vector **x**, the information filter can avoid the inversion of a bigger matrix in the Kalman gain calculation at the price of inverting a smaller matrix in the prediction step, thus saving computing time. Additionally, the information filter allows for system information initialization according to ${I_{1|0}=P_{1|0}^{-1}=0}$ , which would not be possible for the regular Kalman filter. In the information filter, or inverse covariance filter, the estimated covariance and estimated state are replaced by the information matrix and information vector respectively. These are defined as:

${\begin{aligned}\mathbf {Y} _{k\mid k}&=\mathbf {P} _{k\mid k}^{-1}\\{\hat {\mathbf {y} }}_{k\mid k}&=\mathbf {P} _{k\mid k}^{-1}{\hat {\mathbf {x} }}_{k\mid k}\end{aligned}}$

Similarly the predicted covariance and state have equivalent information forms, defined as:

${\begin{aligned}\mathbf {Y} _{k\mid k-1}&=\mathbf {P} _{k\mid k-1}^{-1}\\{\hat {\mathbf {y} }}_{k\mid k-1}&=\mathbf {P} _{k\mid k-1}^{-1}{\hat {\mathbf {x} }}_{k\mid k-1}\end{aligned}}$

and the measurement covariance and measurement vector, which are defined as:

${\begin{aligned}\mathbf {I} _{k}&=\mathbf {H} _{k}^{\textsf {T}}\mathbf {R} _{k}^{-1}\mathbf {H} _{k}\\\mathbf {i} _{k}&=\mathbf {H} _{k}^{\textsf {T}}\mathbf {R} _{k}^{-1}\mathbf {z} _{k}\end{aligned}}$

The information update now becomes a trivial sum.

${\begin{aligned}\mathbf {Y} _{k\mid k}&=\mathbf {Y} _{k\mid k-1}+\mathbf {I} _{k}\\{\hat {\mathbf {y} }}_{k\mid k}&={\hat {\mathbf {y} }}_{k\mid k-1}+\mathbf {i} _{k}\end{aligned}}$

The main advantage of the information filter is that *N* measurements can be filtered at each time step simply by summing their information matrices and vectors.

${\begin{aligned}\mathbf {Y} _{k\mid k}&=\mathbf {Y} _{k\mid k-1}+\sum _{j=1}^{N}\mathbf {I} _{k,j}\\{\hat {\mathbf {y} }}_{k\mid k}&={\hat {\mathbf {y} }}_{k\mid k-1}+\sum _{j=1}^{N}\mathbf {i} _{k,j}\end{aligned}}$

To predict the information filter the information matrix and vector can be converted back to their state space equivalents, or alternatively the information space prediction can be used.

${\begin{aligned}\mathbf {M} _{k}&=\left[\mathbf {F} _{k}^{-1}\right]^{\textsf {T}}\mathbf {Y} _{k-1\mid k-1}\mathbf {F} _{k}^{-1}\\\mathbf {C} _{k}&=\mathbf {M} _{k}\left[\mathbf {M} _{k}+\mathbf {Q} _{k}^{-1}\right]^{-1}\\\mathbf {L} _{k}&=\mathbf {I} -\mathbf {C} _{k}\\\mathbf {Y} _{k\mid k-1}&=\mathbf {L} _{k}\mathbf {M} _{k}+\mathbf {C} _{k}\mathbf {Q} _{k}^{-1}\mathbf {C} _{k}^{\textsf {T}}\\{\hat {\mathbf {y} }}_{k\mid k-1}&=\mathbf {L} _{k}\left[\mathbf {F} _{k}^{-1}\right]^{\textsf {T}}{\hat {\mathbf {y} }}_{k-1\mid k-1}\end{aligned}}$


## Fixed-lag smoother

The optimal fixed-lag smoother provides the optimal estimate of ${\hat {\mathbf {x} }}_{k-N\mid k}$ for a given fixed-lag N using the measurements from $\mathbf {z} _{1}$ to $\mathbf {z} _{k}$ . It can be derived using the previous theory via an augmented state, and the main equation of the filter is the following:

${\begin{bmatrix}{\hat {\mathbf {x} }}_{t\mid t}\\{\hat {\mathbf {x} }}_{t-1\mid t}\\\vdots \\{\hat {\mathbf {x} }}_{t-N+1\mid t}\\\end{bmatrix}}={\begin{bmatrix}\mathbf {I} \\0\\\vdots \\0\\\end{bmatrix}}{\hat {\mathbf {x} }}_{t\mid t-1}+{\begin{bmatrix}0&\ldots &0\\\mathbf {I} &0&\vdots \\\vdots &\ddots &\vdots \\0&\ldots &\mathbf {I} \\\end{bmatrix}}{\begin{bmatrix}{\hat {\mathbf {x} }}_{t-1\mid t-1}\\{\hat {\mathbf {x} }}_{t-2\mid t-1}\\\vdots \\{\hat {\mathbf {x} }}_{t-N+1\mid t-1}\\\end{bmatrix}}+{\begin{bmatrix}\mathbf {K} ^{(0)}\\\mathbf {K} ^{(1)}\\\vdots \\\mathbf {K} ^{(N-1)}\\\end{bmatrix}}\mathbf {y} _{t\mid t-1}$

where:

- ${\hat {\mathbf {x} }}_{t\mid t-1}$ is estimated via a standard Kalman filter;
- $\mathbf {y} _{t\mid t-1}=\mathbf {z} _{t}-\mathbf {H} {\hat {\mathbf {x} }}_{t\mid t-1}$ is the innovation produced considering the estimate of the standard Kalman filter;
- the various ${\hat {\mathbf {x} }}_{t-i\mid t}$ with $i=1,\ldots ,N-1$ are new variables; i.e., they do not appear in the standard Kalman filter;
- the gains are computed via the following scheme: $\mathbf {K} ^{(i+1)}=\mathbf {P} ^{(i)}\mathbf {H} ^{\textsf {T}}\left[\mathbf {H} \mathbf {P} \mathbf {H} ^{\textsf {T}}+\mathbf {R} \right]^{-1}$

and

$\mathbf {P} ^{(i)}=\mathbf {P} \left[\left(\mathbf {F} -\mathbf {K} \mathbf {H} \right)^{\textsf {T}}\right]^{i}$

where

$\mathbf {P}$

and

$\mathbf {K}$

are the prediction error covariance and the gains of the standard Kalman filter (i.e.,

$\mathbf {P} _{t\mid t-1}$

).

If the estimation error covariance is defined so that

$\mathbf {P} _{i}:=E\left[\left(\mathbf {x} _{t-i}-{\hat {\mathbf {x} }}_{t-i\mid t}\right)^{*}\left(\mathbf {x} _{t-i}-{\hat {\mathbf {x} }}_{t-i\mid t}\right)\mid z_{1}\ldots z_{t}\right],$

then we have that the improvement on the estimation of $\mathbf {x} _{t-i}$ is given by:

$\mathbf {P} -\mathbf {P} _{i}=\sum _{j=0}^{i}\left[\mathbf {P} ^{(j)}\mathbf {H} ^{\textsf {T}}\left(\mathbf {H} \mathbf {P} \mathbf {H} ^{\textsf {T}}+\mathbf {R} \right)^{-1}\mathbf {H} \left(\mathbf {P} ^{(i)}\right)^{\textsf {T}}\right]$


## Fixed-interval smoothers

The optimal fixed-interval smoother provides the optimal estimate of ${\hat {\mathbf {x} }}_{k\mid n}$ ( $k<n$ ) using the measurements from a fixed interval $\mathbf {z} _{1}$ to $\mathbf {z} _{n}$ . This is also called "Kalman Smoothing". There are several smoothing algorithms in common use.

### Rauch–Tung–Striebel

The Rauch–Tung–Striebel (RTS) smoother is an efficient two-pass algorithm for fixed interval smoothing.

The forward pass is the same as the regular Kalman filter algorithm. These *filtered* a-priori and a-posteriori state estimates ${\hat {\mathbf {x} }}_{k\mid k-1}$ , ${\hat {\mathbf {x} }}_{k\mid k}$ and covariances $\mathbf {P} _{k\mid k-1}$ , $\mathbf {P} _{k\mid k}$ are saved for use in the backward pass (for retrodiction).

In the backward pass, we compute the *smoothed* state estimates ${\hat {\mathbf {x} }}_{k\mid n}$ and covariances $\mathbf {P} _{k\mid n}$ . We start at the last time step and proceed backward in time using the following recursive equations:

${\begin{aligned}{\hat {\mathbf {x} }}_{k\mid n}&={\hat {\mathbf {x} }}_{k\mid k}+\mathbf {C} _{k}\left({\hat {\mathbf {x} }}_{k+1\mid n}-{\hat {\mathbf {x} }}_{k+1\mid k}\right)\\\mathbf {P} _{k\mid n}&=\mathbf {P} _{k\mid k}+\mathbf {C} _{k}\left(\mathbf {P} _{k+1\mid n}-\mathbf {P} _{k+1\mid k}\right)\mathbf {C} _{k}^{\textsf {T}}\end{aligned}}$

where

$\mathbf {C} _{k}=\mathbf {P} _{k\mid k}\mathbf {F} _{k+1}^{\textsf {T}}\mathbf {P} _{k+1\mid k}^{-1}.$

$\mathbf {x} _{k\mid k}$ is the a-posteriori state estimate of timestep k and $\mathbf {x} _{k+1\mid k}$ is the a-priori state estimate of timestep $k+1$ . The same notation applies to the covariance.

### Modified Bryson–Frazier smoother

An alternative to the RTS algorithm is the modified Bryson–Frazier (MBF) fixed interval smoother developed by Bierman. This also uses a backward pass that processes data saved from the Kalman filter forward pass. The equations for the backward pass involve the recursive computation of data which are used at each observation time to compute the smoothed state and covariance.

The recursive equations are

${\begin{aligned}{\tilde {\Lambda }}_{k}&=\mathbf {H} _{k}^{\textsf {T}}\mathbf {S} _{k}^{-1}\mathbf {H} _{k}+{\hat {\mathbf {C} }}_{k}^{\textsf {T}}{\hat {\Lambda }}_{k}{\hat {\mathbf {C} }}_{k}\\{\hat {\Lambda }}_{k-1}&=\mathbf {F} _{k}^{\textsf {T}}{\tilde {\Lambda }}_{k}\mathbf {F} _{k}\\{\hat {\Lambda }}_{n}&=0\\{\tilde {\lambda }}_{k}&=-\mathbf {H} _{k}^{\textsf {T}}\mathbf {S} _{k}^{-1}\mathbf {y} _{k}+{\hat {\mathbf {C} }}_{k}^{\textsf {T}}{\hat {\lambda }}_{k}\\{\hat {\lambda }}_{k-1}&=\mathbf {F} _{k}^{\textsf {T}}{\tilde {\lambda }}_{k}\\{\hat {\lambda }}_{n}&=0\end{aligned}}$

where $\mathbf {S} _{k}$ is the residual covariance and ${\hat {\mathbf {C} }}_{k}=\mathbf {I} -\mathbf {K} _{k}\mathbf {H} _{k}$ . The smoothed state and covariance can then be found by substitution in the equations

${\begin{aligned}\mathbf {P} _{k\mid n}&=\mathbf {P} _{k\mid k}-\mathbf {P} _{k\mid k}{\hat {\Lambda }}_{k}\mathbf {P} _{k\mid k}\\\mathbf {x} _{k\mid n}&=\mathbf {x} _{k\mid k}-\mathbf {P} _{k\mid k}{\hat {\lambda }}_{k}\end{aligned}}$

or

${\begin{aligned}\mathbf {P} _{k\mid n}&=\mathbf {P} _{k\mid k-1}-\mathbf {P} _{k\mid k-1}{\tilde {\Lambda }}_{k}\mathbf {P} _{k\mid k-1}\\\mathbf {x} _{k\mid n}&=\mathbf {x} _{k\mid k-1}-\mathbf {P} _{k\mid k-1}{\tilde {\lambda }}_{k}.\end{aligned}}$

An important advantage of the MBF is that it does not require finding the inverse of the covariance matrix. Bierman's derivation is based on the RTS smoother, which assumes that the underlying distributions are Gaussian. However, a derivation of the MBF based on the concept of the fixed point smoother, which does not require the Gaussian assumption, is given by Gibbs.

The MBF can also be used to perform consistency checks on the filter residuals and the difference between the value of a filter state after an update and the smoothed value of the state, that is $\mathbf {x} _{k\mid k}-\mathbf {x} _{k\mid n}$ .

### Minimum-variance smoother

The minimum-variance smoother can attain the best-possible error performance, provided that the models are linear, their parameters and the noise statistics are known precisely. This smoother is a time-varying state-space generalization of the optimal non-causal Wiener filter.

The smoother calculations are done in two passes. The forward calculations involve a one-step-ahead predictor and are given by

${\begin{aligned}{\hat {\mathbf {x} }}_{k+1\mid k}&=(\mathbf {F} _{k}-\mathbf {K} _{k}\mathbf {H} _{k}){\hat {\mathbf {x} }}_{k\mid k-1}+\mathbf {K} _{k}\mathbf {z} _{k}\\\alpha _{k}&=-\mathbf {S} _{k}^{-{\frac {1}{2}}}\mathbf {H} _{k}{\hat {\mathbf {x} }}_{k\mid k-1}+\mathbf {S} _{k}^{-{\frac {1}{2}}}\mathbf {z} _{k}\end{aligned}}$

The above system is known as the inverse Wiener-Hopf factor. The backward recursion is the adjoint of the above forward system. The result of the backward pass $\beta _{k}$ may be calculated by operating the forward equations on the time-reversed $\alpha _{k}$ and time reversing the result. In the case of output estimation, the smoothed estimate is given by

${\hat {\mathbf {y} }}_{k\mid N}=\mathbf {z} _{k}-\mathbf {R} _{k}\beta _{k}$

Taking the causal part of this minimum-variance smoother yields

${\hat {\mathbf {y} }}_{k\mid k}=\mathbf {z} _{k}-\mathbf {R} _{k}\mathbf {S} _{k}^{-{\frac {1}{2}}}\alpha _{k}$

which is identical to the minimum-variance Kalman filter. The above solutions minimize the variance of the output estimation error. Note that the Rauch–Tung–Striebel smoother derivation assumes that the underlying distributions are Gaussian, whereas the minimum-variance solutions do not. Optimal smoothers for state estimation and input estimation can be constructed similarly.

A continuous-time version of the above smoother is described in.

Expectation–maximization algorithms may be employed to calculate approximate maximum likelihood estimates of unknown state-space parameters within minimum-variance filters and smoothers. Often uncertainties remain within problem assumptions. A smoother that accommodates uncertainties can be designed by adding a positive definite term to the Riccati equation.

In cases where the models are nonlinear, step-wise linearizations may be within the minimum-variance filter and smoother recursions (extended Kalman filtering).


## Frequency-weighted Kalman filters

Pioneering research on the perception of sounds at different frequencies was conducted by Fletcher and Munson in the 1930s. Their work led to a standard way of weighting measured sound levels within investigations of industrial noise and hearing loss. Frequency weightings have since been used within filter and controller designs to manage performance within bands of interest.

Typically, a frequency shaping function is used to weight the average power of the error spectral density in a specified frequency band. Let $\mathbf {y} -{\hat {\mathbf {y} }}$ denote the output estimation error exhibited by a conventional Kalman filter. Also, let $\mathbf {W}$ denote a causal frequency weighting transfer function. The optimum solution which minimizes the variance of $\mathbf {W} \left(\mathbf {y} -{\hat {\mathbf {y} }}\right)$ arises by simply constructing $\mathbf {W} ^{-1}{\hat {\mathbf {y} }}$ .

The design of $\mathbf {W}$ remains an open question. One way of proceeding is to identify a system which generates the estimation error and setting $\mathbf {W}$ equal to the inverse of that system. This procedure may be iterated to obtain mean-square error improvement at the cost of increased filter order. The same technique can be applied to smoothers.


## Nonlinear filters

The basic Kalman filter is limited to a linear assumption. More complex systems, however, can be nonlinear. The nonlinearity can be associated either with the process model or with the observation model or with both.

The most common variants of Kalman filters for non-linear systems are the Extended Kalman Filter and Unscented Kalman filter. The suitability of which filter to use depends on the non-linearity indices of the process and observation model.

### Extended Kalman filter

In the extended Kalman filter (EKF), the state transition and observation models need not be linear functions of the state but may instead be nonlinear functions. These functions are of differentiable type.

${\begin{aligned}\mathbf {x} _{k}&=f(\mathbf {x} _{k-1},\mathbf {u} _{k})+\mathbf {w} _{k}\\\mathbf {z} _{k}&=h(\mathbf {x} _{k})+\mathbf {v} _{k}\end{aligned}}$

The function *f* can be used to compute the predicted state from the previous estimate and similarly the function *h* can be used to compute the predicted measurement from the predicted state. However, *f* and *h* cannot be applied to the covariance directly. Instead a matrix of partial derivatives (the Jacobian) is computed.

At each timestep the Jacobian is evaluated with current predicted states. These matrices can be used in the Kalman filter equations. This process essentially linearizes the nonlinear function around the current estimate.

### Unscented Kalman filter

When the state transition and observation models—that is, the predict and update functions f and h —are highly nonlinear, the extended Kalman filter can give particularly poor performance. This is because the covariance is propagated through linearization of the underlying nonlinear model. The unscented Kalman filter (UKF) uses a deterministic sampling technique known as the unscented transformation (UT) to pick a minimal set of sample points (called sigma points) around the mean. The sigma points are then propagated through the nonlinear functions, from which a new mean and covariance estimate are formed. The resulting filter depends on how the transformed statistics of the UT are calculated and which set of sigma points are used. It should be remarked that it is always possible to construct new UKFs in a consistent way. For certain systems, the resulting UKF more accurately estimates the true mean and covariance. This can be verified with Monte Carlo sampling or Taylor series expansion of the posterior statistics. In addition, this technique removes the requirement to explicitly calculate Jacobians, which for complex functions can be a difficult task in itself (i.e., requiring complicated derivatives if done analytically or being computationally costly if done numerically), if not impossible (if those functions are not differentiable).

#### Sigma points

For a random vector $\mathbf {x} =(x_{1},\dots ,x_{L})$ , sigma points are any set of vectors

$\{\mathbf {s} _{0},\dots ,\mathbf {s} _{N}\}={\bigl \{}{\begin{pmatrix}s_{0,1}&s_{0,2}&\ldots &s_{0,L}\end{pmatrix}},\dots ,{\begin{pmatrix}s_{N,1}&s_{N,2}&\ldots &s_{N,L}\end{pmatrix}}{\bigr \}}$

attributed with

- first-order weights $W_{0}^{a},\dots ,W_{N}^{a}$ that fulfill

1. $\sum _{j=0}^{N}W_{j}^{a}=1$
2. for all $i=1,\dots ,L$ : $E[x_{i}]=\sum _{j=0}^{N}W_{j}^{a}s_{j,i}$

- second-order weights $W_{0}^{c},\dots ,W_{N}^{c}$ that fulfill

1. $\sum _{j=0}^{N}W_{j}^{c}=1$
2. for all pairs $(i,l)\in \{1,\dots ,L\}^{2}:E[x_{i}x_{l}]=\sum _{j=0}^{N}W_{j}^{c}s_{j,i}s_{j,l}$ .

A simple choice of sigma points and weights for $\mathbf {x} _{k-1\mid k-1}$ in the UKF algorithm is

${\begin{aligned}\mathbf {s} _{0}&={\hat {\mathbf {x} }}_{k-1\mid k-1}\\-1&<W_{0}^{a}=W_{0}^{c}<1\\\mathbf {s} _{j}&={\hat {\mathbf {x} }}_{k-1\mid k-1}+{\sqrt {\frac {L}{1-W_{0}}}}\mathbf {A} _{j},\quad j=1,\dots ,L\\\mathbf {s} _{L+j}&={\hat {\mathbf {x} }}_{k-1\mid k-1}-{\sqrt {\frac {L}{1-W_{0}}}}\mathbf {A} _{j},\quad j=1,\dots ,L\\W_{j}^{a}&=W_{j}^{c}={\frac {1-W_{0}}{2L}},\quad j=1,\dots ,2L\end{aligned}}$

where ${\hat {\mathbf {x} }}_{k-1\mid k-1}$ is the mean estimate of $\mathbf {x} _{k-1\mid k-1}$ . The vector $\mathbf {A} _{j}$ is the *j*th column of $\mathbf {A}$ where $\mathbf {P} _{k-1\mid k-1}=\mathbf {AA} ^{\textsf {T}}$ . Typically, $\mathbf {A}$ is obtained via Cholesky decomposition of $\mathbf {P} _{k-1\mid k-1}$ . With some care the filter equations can be expressed in such a way that $\mathbf {A}$ is evaluated directly without intermediate calculations of $\mathbf {P} _{k-1\mid k-1}$ . This is referred to as the *square-root unscented Kalman filter*.

The weight of the mean value, $W_{0}$ , can be chosen arbitrarily.

Another popular parameterization (which generalizes the above) is

${\begin{aligned}\mathbf {s} _{0}&={\hat {\mathbf {x} }}_{k-1\mid k-1}\\W_{0}^{a}&={\frac {\alpha ^{2}\kappa -L}{\alpha ^{2}\kappa }}\\W_{0}^{c}&=W_{0}^{a}+1-\alpha ^{2}+\beta \\\mathbf {s} _{j}&={\hat {\mathbf {x} }}_{k-1\mid k-1}+\alpha {\sqrt {\kappa }}\mathbf {A} _{j},\quad j=1,\dots ,L\\\mathbf {s} _{L+j}&={\hat {\mathbf {x} }}_{k-1\mid k-1}-\alpha {\sqrt {\kappa }}\mathbf {A} _{j},\quad j=1,\dots ,L\\W_{j}^{a}&=W_{j}^{c}={\frac {1}{2\alpha ^{2}\kappa }},\quad j=1,\dots ,2L.\end{aligned}}$

$\alpha$ and $\kappa$ control the spread of the sigma points. $\beta$ is related to the distribution of x . Note that this is an overparameterization in the sense that any one of $\alpha$ , $\beta$ and $\kappa$ can be chosen arbitrarily.

Appropriate values depend on the problem at hand, but a typical recommendation is $\alpha =1$ , $\beta =0$ , and $\kappa \approx 3L/2$ . If the true distribution of x is Gaussian, $\beta =2$ is optimal.

#### Predict

As with the EKF, the UKF prediction can be used independently from the UKF update, in combination with a linear (or indeed EKF) update, or vice versa.

Given estimates of the mean and covariance, ${\hat {\mathbf {x} }}_{k-1\mid k-1}$ and $\mathbf {P} _{k-1\mid k-1}$ , one obtains $N=2L+1$ sigma points as described in the section above. The sigma points are propagated through the transition function *f*.

$\mathbf {x} _{j}=f\left(\mathbf {s} _{j}\right)\quad j=0,\dots ,2L$

.

The propagated sigma points are weighed to produce the predicted mean and covariance.

${\begin{aligned}{\hat {\mathbf {x} }}_{k\mid k-1}&=\sum _{j=0}^{2L}W_{j}^{a}\mathbf {x} _{j}\\\mathbf {P} _{k\mid k-1}&=\sum _{j=0}^{2L}W_{j}^{c}\left(\mathbf {x} _{j}-{\hat {\mathbf {x} }}_{k\mid k-1}\right)\left(\mathbf {x} _{j}-{\hat {\mathbf {x} }}_{k\mid k-1}\right)^{\textsf {T}}+\mathbf {Q} _{k}\end{aligned}}$

where $W_{j}^{a}$ are the first-order weights of the original sigma points, and $W_{j}^{c}$ are the second-order weights. The matrix $\mathbf {Q} _{k}$ is the covariance of the transition noise, $\mathbf {w} _{k}$ .

#### Update

Given prediction estimates ${\hat {\mathbf {x} }}_{k\mid k-1}$ and $\mathbf {P} _{k\mid k-1}$ , a new set of $N=2L+1$ sigma points $\mathbf {s} _{0},\dots ,\mathbf {s} _{2L}$ with corresponding first-order weights $W_{0}^{a},\dots W_{2L}^{a}$ and second-order weights $W_{0}^{c},\dots ,W_{2L}^{c}$ is calculated. These sigma points are transformed through the measurement function h .

$\mathbf {z} _{j}=h(\mathbf {s} _{j}),\,\,j=0,1,\dots ,2L$

.

Then the empirical mean and covariance of the transformed points are calculated.

${\begin{aligned}{\hat {\mathbf {z} }}&=\sum _{j=0}^{2L}W_{j}^{a}\mathbf {z} _{j}\\[6pt]{\hat {\mathbf {S} }}_{k}&=\sum _{j=0}^{2L}W_{j}^{c}(\mathbf {z} _{j}-{\hat {\mathbf {z} }})(\mathbf {z} _{j}-{\hat {\mathbf {z} }})^{\textsf {T}}+\mathbf {R_{k}} \end{aligned}}$

where $\mathbf {R} _{k}$ is the covariance matrix of the observation noise, $\mathbf {v} _{k}$ . Additionally, the cross covariance matrix is also needed

${\begin{aligned}\mathbf {C_{xz}} &=\sum _{j=0}^{2L}W_{j}^{c}(\mathbf {x} _{j}-{\hat {\mathbf {x} }}_{k|k-1})(\mathbf {z} _{j}-{\hat {\mathbf {z} }})^{\textsf {T}}.\end{aligned}}$

The Kalman gain is

${\begin{aligned}\mathbf {K} _{k}=\mathbf {C_{xz}} {\hat {\mathbf {S} }}_{k}^{-1}.\end{aligned}}$

The updated mean and covariance estimates are

${\begin{aligned}{\hat {\mathbf {x} }}_{k\mid k}&={\hat {\mathbf {x} }}_{k|k-1}+\mathbf {K} _{k}(\mathbf {z} _{k}-{\hat {\mathbf {z} }})\\\mathbf {P} _{k\mid k}&=\mathbf {P} _{k\mid k-1}-\mathbf {K} _{k}{\hat {\mathbf {S} }}_{k}\mathbf {K} _{k}^{\textsf {T}}.\end{aligned}}$

### Discriminative Kalman filter

When the observation model $p(\mathbf {z} _{k}\mid \mathbf {x} _{k})$ is highly non-linear and/or non-Gaussian, it may prove advantageous to apply Bayes' rule and estimate

$p(\mathbf {z} _{k}\mid \mathbf {x} _{k})\approx {\frac {p(\mathbf {x} _{k}\mid \mathbf {z} _{k})}{p(\mathbf {x} _{k})}}$

where $p(\mathbf {x} _{k}\mid \mathbf {z} _{k})\approx {\mathcal {N}}(g(\mathbf {z} _{k}),Q(\mathbf {z} _{k}))$ for nonlinear functions $g,Q$ . This replaces the generative specification of the standard Kalman filter with a discriminative model for the latent states given observations.

Under a stationary state model

${\begin{aligned}p(\mathbf {x} _{1})&={\mathcal {N}}(0,\mathbf {T} ),\\p(\mathbf {x} _{k}\mid \mathbf {x} _{k-1})&={\mathcal {N}}(\mathbf {F} \mathbf {x} _{k-1},\mathbf {C} ),\end{aligned}}$

where $\mathbf {T} =\mathbf {F} \mathbf {T} \mathbf {F} ^{\intercal }+\mathbf {C}$ , if

$p(\mathbf {x} _{k}\mid \mathbf {z} _{1:k})\approx {\mathcal {N}}({\hat {\mathbf {x} }}_{k|k-1},\mathbf {P} _{k|k-1}),$

then given a new observation $\mathbf {z} _{k}$ , it follows that

$p(\mathbf {x} _{k+1}\mid \mathbf {z} _{1:k+1})\approx {\mathcal {N}}({\hat {\mathbf {x} }}_{k+1|k},\mathbf {P} _{k+1|k})$

where

${\begin{aligned}\mathbf {M} _{k+1}&=\mathbf {F} \mathbf {P} _{k|k-1}\mathbf {F} ^{\intercal }+\mathbf {C} ,\\\mathbf {P} _{k+1|k}&=(\mathbf {M} _{k+1}^{-1}+Q(\mathbf {z} _{k})^{-1}-\mathbf {T} ^{-1})^{-1},\\{\hat {\mathbf {x} }}_{k+1|k}&=\mathbf {P} _{k+1|k}(\mathbf {M} _{k+1}^{-1}\mathbf {F} {\hat {\mathbf {x} }}_{k|k-1}+\mathbf {P} _{k+1|k}^{-1}g(\mathbf {z} _{k})).\end{aligned}}$

Note that this approximation requires $Q(\mathbf {z} _{k})^{-1}-\mathbf {T} ^{-1}$ to be positive-definite; in the case that it is not,

$\mathbf {P} _{k+1|k}=(\mathbf {M} _{k+1}^{-1}+Q(\mathbf {z} _{k})^{-1})^{-1}$

is used instead. Such an approach proves particularly useful when the dimensionality of the observations is much greater than that of the latent states and can be used to build filters that are particularly robust to nonstationarities in the observation model.


## Adaptive Kalman filter

Adaptive Kalman filters allow to adapt for process dynamics which are not modeled in the process model $\mathbf {F} (t)$ , which happens for example in the context of a maneuvering target when a constant velocity (reduced order) Kalman filter is employed for tracking.


## Kalman–Bucy filter

Kalman–Bucy filtering (named for Richard Snowden Bucy) is a continuous time version of Kalman filtering.

It is based on the state space model

${\begin{aligned}{\frac {d}{dt}}\mathbf {x} (t)&=\mathbf {F} (t)\mathbf {x} (t)+\mathbf {B} (t)\mathbf {u} (t)+\mathbf {w} (t)\\\mathbf {z} (t)&=\mathbf {H} (t)\mathbf {x} (t)+\mathbf {v} (t)\end{aligned}}$

where $\mathbf {Q} (t)$ and $\mathbf {R} (t)$ represent the intensities of the two white noise terms $\mathbf {w} (t)$ and $\mathbf {v} (t)$ , respectively.

The filter consists of two differential equations, one for the state estimate and one for the covariance:

${\begin{aligned}{\frac {d}{dt}}{\hat {\mathbf {x} }}(t)&=\mathbf {F} (t){\hat {\mathbf {x} }}(t)+\mathbf {B} (t)\mathbf {u} (t)+\mathbf {K} (t)\left(\mathbf {z} (t)-\mathbf {H} (t){\hat {\mathbf {x} }}(t)\right)\\{\frac {d}{dt}}\mathbf {P} (t)&=\mathbf {F} (t)\mathbf {P} (t)+\mathbf {P} (t)\mathbf {F} ^{\textsf {T}}(t)+\mathbf {Q} (t)-\mathbf {K} (t)\mathbf {R} (t)\mathbf {K} ^{\textsf {T}}(t)\end{aligned}}$

where the Kalman gain is given by

$\mathbf {K} (t)=\mathbf {P} (t)\mathbf {H} ^{\textsf {T}}(t)\mathbf {R} ^{-1}(t)$

Note that in this expression for $\mathbf {K} (t)$ the covariance of the observation noise $\mathbf {R} (t)$ represents at the same time the covariance of the prediction error (or *innovation*) ${\tilde {\mathbf {y} }}(t)=\mathbf {z} (t)-\mathbf {H} (t){\hat {\mathbf {x} }}(t)$ ; these covariances are equal only in the case of continuous time.

The distinction between the prediction and update steps of discrete-time Kalman filtering does not exist in continuous time.

The second differential equation, for the covariance, is an example of a Riccati equation. Nonlinear generalizations to Kalman–Bucy filters include continuous time extended Kalman filter.


## Hybrid Kalman filter

Most physical systems are represented as continuous-time models while discrete-time measurements are made frequently for state estimation via a digital processor. Therefore, the system model and measurement model are given by

${\begin{aligned}{\dot {\mathbf {x} }}(t)&=\mathbf {F} (t)\mathbf {x} (t)+\mathbf {B} (t)\mathbf {u} (t)+\mathbf {w} (t),&\mathbf {w} (t)&\sim N\left(\mathbf {0} ,\mathbf {Q} (t)\right)\\\mathbf {z} _{k}&=\mathbf {H} _{k}\mathbf {x} _{k}+\mathbf {v} _{k},&\mathbf {v} _{k}&\sim N(\mathbf {0} ,\mathbf {R} _{k})\end{aligned}}$

where

$\mathbf {x} _{k}=\mathbf {x} (t_{k})$

.

### Initialize

${\hat {\mathbf {x} }}_{0\mid 0}=E\left[\mathbf {x} (t_{0})\right],\mathbf {P} _{0\mid 0}=\operatorname {Var} \left[\mathbf {x} \left(t_{0}\right)\right]$

### Predict

${\begin{aligned}{\dot {\hat {\mathbf {x} }}}(t)&=\mathbf {F} (t){\hat {\mathbf {x} }}(t)+\mathbf {B} (t)\mathbf {u} (t){\text{, with }}{\hat {\mathbf {x} }}\left(t_{k-1}\right)={\hat {\mathbf {x} }}_{k-1\mid k-1}\\\Rightarrow {\hat {\mathbf {x} }}_{k\mid k-1}&={\hat {\mathbf {x} }}\left(t_{k}\right)\\{\dot {\mathbf {P} }}(t)&=\mathbf {F} (t)\mathbf {P} (t)+\mathbf {P} (t)\mathbf {F} (t)^{\textsf {T}}+\mathbf {Q} (t){\text{, with }}\mathbf {P} \left(t_{k-1}\right)=\mathbf {P} _{k-1\mid k-1}\\\Rightarrow \mathbf {P} _{k\mid k-1}&=\mathbf {P} \left(t_{k}\right)\end{aligned}}$

The prediction equations are derived from those of continuous-time Kalman filter without update from measurements, i.e., $\mathbf {K} (t)=0$ . The predicted state and covariance are calculated respectively by solving a set of differential equations with the initial value equal to the estimate at the previous step.

For the case of linear time invariant systems, the continuous time dynamics can be exactly discretized into a discrete time system using matrix exponentials.

### Update

${\begin{aligned}\mathbf {K} _{k}&=\mathbf {P} _{k\mid k-1}\mathbf {H} _{k}^{\textsf {T}}\left(\mathbf {H} _{k}\mathbf {P} _{k\mid k-1}\mathbf {H} _{k}^{\textsf {T}}+\mathbf {R} _{k}\right)^{-1}\\{\hat {\mathbf {x} }}_{k\mid k}&={\hat {\mathbf {x} }}_{k\mid k-1}+\mathbf {K} _{k}\left(\mathbf {z} _{k}-\mathbf {H} _{k}{\hat {\mathbf {x} }}_{k\mid k-1}\right)\\\mathbf {P} _{k\mid k}&=\left(\mathbf {I} -\mathbf {K} _{k}\mathbf {H} _{k}\right)\mathbf {P} _{k\mid k-1}\end{aligned}}$

The update equations are identical to those of the discrete-time Kalman filter.


## Variants for the recovery of sparse signals

The traditional Kalman filter has also been employed for the recovery of sparse, possibly dynamic, signals from noisy observations. Recent works utilize notions from the theory of compressed sensing/sampling, such as the restricted isometry property and related probabilistic recovery arguments, for sequentially estimating the sparse state in intrinsically low-dimensional systems.


## Relation to Gaussian processes

Since linear Gaussian state-space models lead to Gaussian processes, Kalman filters can be viewed as sequential solvers for Gaussian process regression.


## Applications

- Attitude and heading reference systems
- Autopilot
- Electric battery state of charge (SoC) estimation
- Brain–computer interfaces
- Tracking and vertex fitting of charged particles in particle detectors
- Tracking of objects in computer vision
- Dynamic positioning in shipping
- Economics, in particular macroeconomics, time series analysis, and econometrics
- Inertial guidance system
- Nuclear medicine – single photon emission computed tomography image restoration
- Orbit determination
- Power system state estimation
- Radar tracker
- Satellite navigation systems
- Seismology
- Sensorless control of AC motor variable-frequency drives
- Simultaneous localization and mapping
- Speech enhancement
- Visual odometry
- Weather forecasting
- Navigation system
- 3D modeling
- Structural health monitoring
- Human sensorimotor processing
