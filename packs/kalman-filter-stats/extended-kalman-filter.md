---
title: "Extended Kalman filter"
source: https://en.wikipedia.org/wiki/Extended_Kalman_filter
domain: kalman-filter-stats
license: CC-BY-SA-4.0
tags: Kalman filter, extended Kalman filter, unscented transform, particle filter
fetched: 2026-07-02
---

# Extended Kalman filter

In estimation theory, the **extended Kalman filter** (**EKF**) is the nonlinear version of the Kalman filter which linearizes about an estimate of the current mean and covariance. In the case of well defined transition models, the EKF has been considered the *de facto* standard in the theory of nonlinear state estimation, navigation systems and GPS.

## History

The papers establishing the mathematical foundations of Kalman type filters were published between 1959 and 1961. Named after the Hungarian-American mathematician, engineer, and inventor Rudolf E. Kálmán, the Kalman filter is the optimal linear estimator for *linear* system models with additive independent white noise in both the transition and the measurement systems. Unfortunately, in engineering, most systems are *nonlinear*, so attempts were made to apply this filtering method to nonlinear systems; most of this work was done at NASA Ames. The EKF adapted techniques from calculus, namely multivariate Taylor series expansions, to linearize a model about a working point. If the system model (as described below) is not well known or is inaccurate, then Monte Carlo methods, especially particle filters, are employed for estimation. Monte Carlo techniques predate the existence of the EKF but are more computationally expensive for any moderately dimensioned state-space.

## Formulation

In the extended Kalman filter, the state transition and observation models don't need to be linear functions of the state but may instead be differentiable functions.

${\boldsymbol {x}}_{k}=f({\boldsymbol {x}}_{k-1},{\boldsymbol {u}}_{k-1})+{\boldsymbol {w}}_{k-1}$

${\boldsymbol {z}}_{k}=h({\boldsymbol {x}}_{k})+{\boldsymbol {v}}_{k}$

Here **w***k* and **v***k* are the process and observation noises which are both assumed to be zero mean multivariate Gaussian noises with covariance **Q***k* and **R***k* respectively. **u***k* is the control vector.

The function *f* can be used to compute the predicted state from the previous estimate and similarly the function *h* can be used to compute the predicted measurement from the predicted state. However, *f* and *h* cannot be applied to the covariance directly. Instead a matrix of partial derivatives (the Jacobian) is computed.

At each time step, the Jacobian is evaluated with current predicted states. These matrices can be used in the Kalman filter equations. This process essentially linearizes the non-linear function around the current estimate.

See the Kalman Filter article for notational remarks.

## Discrete-time predict and update equations

Notation ${\hat {\mathbf {x} }}_{n\mid m}$ represents the estimate of $\mathbf {x}$ at time *n* given observations up to and including at time *m* ≤ *n*.

### Predict

| Predicted state estimate | ${\hat {\boldsymbol {x}}}_{k\|k-1}=f({\hat {\boldsymbol {x}}}_{k-1\|k-1},{\boldsymbol {u}}_{k-1})$ |
|---|---|
| Predicted covariance estimate | ${\boldsymbol {P}}_{k\|k-1}={{\boldsymbol {F}}_{k}}{\boldsymbol {P}}_{k-1\|k-1}{{\boldsymbol {F}}_{k}^{T}}+{\boldsymbol {Q}}_{k-1}$ |

### Update

| Innovation or measurement residual | ${\tilde {\boldsymbol {y}}}_{k}={\boldsymbol {z}}_{k}-h({\hat {\boldsymbol {x}}}_{k\|k-1})$ |
|---|---|
| Innovation (or residual) covariance | ${\boldsymbol {S}}_{k}={{\boldsymbol {H}}_{k}}{\boldsymbol {P}}_{k\|k-1}{{\boldsymbol {H}}_{k}^{T}}+{\boldsymbol {R}}_{k}$ |
| *Near-optimal* Kalman gain | ${\boldsymbol {K}}_{k}={\boldsymbol {P}}_{k\|k-1}{{\boldsymbol {H}}_{k}^{T}}{\boldsymbol {S}}_{k}^{-1}$ |
| Updated state estimate | ${\hat {\boldsymbol {x}}}_{k\|k}={\hat {\boldsymbol {x}}}_{k\|k-1}+{\boldsymbol {K}}_{k}{\tilde {\boldsymbol {y}}}_{k}$ |
| Updated covariance estimate | ${\boldsymbol {P}}_{k\|k}=({\boldsymbol {I}}-{\boldsymbol {K}}_{k}{{\boldsymbol {H}}_{k}}){\boldsymbol {P}}_{k\|k-1}$ |

where the state transition and observation matrices are defined to be the following Jacobians

${{\boldsymbol {F}}_{k}}=\left.{\frac {\partial f}{\partial {\boldsymbol {x}}}}\right\vert _{{\hat {\boldsymbol {x}}}_{k-1|k-1},{\boldsymbol {u}}_{k-1}}$

${{\boldsymbol {H}}_{k}}=\left.{\frac {\partial h}{\partial {\boldsymbol {x}}}}\right\vert _{{\hat {\boldsymbol {x}}}_{k|k-1}}$

## Disadvantages and alternatives

Unlike its linear counterpart, the extended Kalman filter in general is *not* an optimal estimator (it is optimal if the measurement and the state transition model are both linear, as in that case the extended Kalman filter is identical to the regular one). In addition, if the initial estimate of the state is wrong, or if the process is modeled incorrectly, the filter may quickly diverge, owing to its linearization. Another problem with the extended Kalman filter is that the estimated covariance matrix tends to underestimate the true covariance matrix and therefore risks becoming inconsistent in the statistical sense without the addition of "stabilising noise" .

More generally one should consider the infinite dimensional nature of the nonlinear filtering problem and the inadequacy of a simple mean and variance-covariance estimator to fully represent the optimal filter. It should also be noted that the extended Kalman filter may give poor performances even for very simple one-dimensional systems such as the cubic sensor, where the optimal filter can be bimodal and as such cannot be effectively represented by a single mean and variance estimator, having a rich structure, or similarly for the quadratic sensor. In such cases the projection filters have been studied as an alternative, having been applied also to navigation. Other general nonlinear filtering methods like full particle filters may be considered in this case.

Having stated this, the extended Kalman filter can give reasonable performance, and is arguably the de facto standard in navigation systems and GPS.

## Generalizations

### Continuous-time extended Kalman filter

**Model**

${\begin{aligned}{\dot {\mathbf {x} }}(t)&=f{\bigl (}\mathbf {x} (t),\mathbf {u} (t){\bigr )}\\\mathbf {z} (t)&=h{\bigl (}\mathbf {x} (t){\bigr )}(t)\end{aligned}}$

**Initialize**

${\hat {\mathbf {x} }}(t_{0})=E{\bigl [}\mathbf {x} (t_{0}){\bigr ]}{\text{, }}\mathbf {P} (t_{0})=Var{\bigl [}\mathbf {x} (t_{0}){\bigr ]}$

**Predict-Update**

${\begin{aligned}{\dot {\hat {\mathbf {x} }}}(t)&=f{\bigl (}{\hat {\mathbf {x} }}(t),\mathbf {u} (t){\bigr )}+\mathbf {K} (t){\Bigl (}\mathbf {z} (t)-h{\bigl (}{\hat {\mathbf {x} }}(t){\bigr )}{\Bigr )}\\{\dot {\mathbf {P} }}(t)&=\mathbf {F} (t)\mathbf {P} (t)+\mathbf {P} (t)\mathbf {F} (t)^{T}-\mathbf {K} (t)\mathbf {H} (t)\mathbf {P} (t)+\mathbf {Q} (t)\\\mathbf {K} (t)&=\mathbf {P} (t)\mathbf {H} (t)^{T}\mathbf {S} (t)^{-1}\\\mathbf {F} (t)&=\left.{\frac {\partial f}{\partial \mathbf {x} }}\right\vert _{{\hat {\mathbf {x} }}(t),\mathbf {u} (t)}\\\mathbf {H} (t)&=\left.{\frac {\partial h}{\partial \mathbf {x} }}\right\vert _{{\hat {\mathbf {x} }}(t)}\end{aligned}}$

Unlike the discrete-time extended Kalman filter, the prediction and update steps are coupled in the continuous-time extended Kalman filter.

#### Discrete-time measurements

Most physical systems are represented as continuous-time models while discrete-time measurements are frequently taken for state estimation via a digital processor. Therefore, the system model and measurement model are given by

${\begin{aligned}{\dot {\mathbf {x} }}(t)&=f{\bigl (}\mathbf {x} (t),\mathbf {u} (t){\bigr )}+\mathbf {w} (t)&\mathbf {w} (t)&\sim {\mathcal {N}}{\bigl (}\mathbf {0} ,\mathbf {Q} (t){\bigr )}\\\mathbf {z} _{k}&=h(\mathbf {x} _{k})+\mathbf {v} _{k}&\mathbf {v} _{k}&\sim {\mathcal {N}}(\mathbf {0} ,\mathbf {R} _{k})\end{aligned}}$

where $\mathbf {x} _{k}=\mathbf {x} (t_{k})$ .

**Initialize**

${\hat {\mathbf {x} }}_{0|0}=E{\bigl [}\mathbf {x} (t_{0}){\bigr ]},\mathbf {P} _{0|0}=E{\bigl [}\left(\mathbf {x} (t_{0})-{\hat {\mathbf {x} }}(t_{0})\right)\left(\mathbf {x} (t_{0})-{\hat {\mathbf {x} }}(t_{0})\right)^{T}{\bigr ]}$

**Predict**

${\begin{aligned}{\text{solve }}&{\begin{cases}{\dot {\hat {\mathbf {x} }}}(t)=f{\bigl (}{\hat {\mathbf {x} }}(t),\mathbf {u} (t){\bigr )}\\{\dot {\mathbf {P} }}(t)=\mathbf {F} (t)\mathbf {P} (t)+\mathbf {P} (t)\mathbf {F} (t)^{T}+\mathbf {Q} (t)\end{cases}}\qquad {\text{with }}{\begin{cases}{\hat {\mathbf {x} }}(t_{k-1})={\hat {\mathbf {x} }}_{k-1|k-1}\\\mathbf {P} (t_{k-1})=\mathbf {P} _{k-1|k-1}\end{cases}}\\\Rightarrow &{\begin{cases}{\hat {\mathbf {x} }}_{k|k-1}={\hat {\mathbf {x} }}(t_{k})\\\mathbf {P} _{k|k-1}=\mathbf {P} (t_{k})\end{cases}}\end{aligned}}$

where

$\mathbf {F} (t)=\left.{\frac {\partial f}{\partial \mathbf {x} }}\right\vert _{{\hat {\mathbf {x} }}(t),\mathbf {u} (t)}$

**Update**

$\mathbf {K} _{k}=\mathbf {P} _{k|k-1}\mathbf {H} _{k}^{T}{\bigl (}\mathbf {H} _{k}\mathbf {P} _{k|k-1}\mathbf {H} _{k}^{T}+\mathbf {R} _{k}{\bigr )}^{-1}$

${\hat {\mathbf {x} }}_{k|k}={\hat {\mathbf {x} }}_{k|k-1}+\mathbf {K} _{k}{\bigl (}\mathbf {z} _{k}-h({\hat {\mathbf {x} }}_{k|k-1}){\bigr )}$

$\mathbf {P} _{k|k}=(\mathbf {I} -\mathbf {K} _{k}\mathbf {H} _{k})\mathbf {P} _{k|k-1}$

where

${\textbf {H}}_{k}=\left.{\frac {\partial h}{\partial {\textbf {x}}}}\right\vert _{{\hat {\textbf {x}}}_{k|k-1}}$

The update equations are identical to those of discrete-time extended Kalman filter.

### Higher-order extended Kalman filters

The above recursion is a first-order extended Kalman filter (EKF). Higher order EKFs may be obtained by retaining more terms of the Taylor series expansions. For example, second and third order EKFs have been described. However, higher order EKFs tend to only provide performance benefits when the measurement noise is small.

### Non-additive noise formulation and equations

The typical formulation of the **EKF** involves the assumption of additive process and measurement noise. This assumption, however, is not necessary for **EKF** implementation. Instead, consider a more general system of the form:

${\boldsymbol {x}}_{k}=f({\boldsymbol {x}}_{k-1},{\boldsymbol {u}}_{k-1},{\boldsymbol {w}}_{k-1})$

${\boldsymbol {z}}_{k}=h({\boldsymbol {x}}_{k},{\boldsymbol {v}}_{k})$

Here **w***k* and **v***k* are the process and observation noises which are both assumed to be zero mean multivariate Gaussian noises with covariance **Q***k* and **R***k* respectively. Then the covariance prediction and innovation equations become

${\boldsymbol {P}}_{k|k-1}={{\boldsymbol {F}}_{k-1}}{{\boldsymbol {P}}_{k-1|k-1}}{{\boldsymbol {F}}_{k-1}^{T}}{+}{{\boldsymbol {L}}_{k-1}}{{\boldsymbol {Q}}_{k-1}}{{\boldsymbol {L}}_{k-1}^{T}}$

${\boldsymbol {S}}_{k}={{\boldsymbol {H}}_{k}}{{\boldsymbol {P}}_{k|k-1}}{{\boldsymbol {H}}_{k}^{T}}{+}{{\boldsymbol {M}}_{k}}{{\boldsymbol {R}}_{k}}{{\boldsymbol {M}}_{k}^{T}}$

where the matrices ${\boldsymbol {L}}_{k-1}$ and ${\boldsymbol {M}}_{k}$ are Jacobian matrices:

${{\boldsymbol {L}}_{k-1}}=\left.{\frac {\partial f}{\partial {\boldsymbol {w}}}}\right\vert _{{\hat {\boldsymbol {x}}}_{k-1|k-1},{\boldsymbol {u}}_{k-1}}$

${{\boldsymbol {M}}_{k}}=\left.{\frac {\partial h}{\partial {\boldsymbol {v}}}}\right\vert _{{\hat {\boldsymbol {x}}}_{k|k-1}}$

The predicted state estimate and measurement residual are evaluated at the mean of the process and measurement noise terms, which is assumed to be zero. Otherwise, the non-additive noise formulation is implemented in the same manner as the additive noise **EKF**.

### Implicit extended Kalman filter

In certain cases, the observation model of a nonlinear system cannot be solved for ${\boldsymbol {z}}_{k}$ , but can be expressed by the implicit function:

$h({\boldsymbol {x}}_{k},{\boldsymbol {z'}}_{k})={\boldsymbol {0}}$

where ${\boldsymbol {z}}_{k}={\boldsymbol {z'}}_{k}+{\boldsymbol {v}}_{k}$ are the noisy observations.

The conventional extended Kalman filter can be applied with the following substitutions:

${{\boldsymbol {R}}_{k}}\leftarrow {{\boldsymbol {J}}_{k}}{{\boldsymbol {R}}_{k}}{{\boldsymbol {J}}_{k}^{T}}$

${\tilde {\boldsymbol {y}}}_{k}\leftarrow -h({\hat {\boldsymbol {x}}}_{k|k-1},{\boldsymbol {z}}_{k})$

where:

${{\boldsymbol {J}}_{k}}=\left.{\frac {\partial h}{\partial {\boldsymbol {z}}}}\right\vert _{{\hat {\boldsymbol {x}}}_{k|k-1},{\boldsymbol {z}}_{k}}$

Here the original observation covariance matrix ${{\boldsymbol {R}}_{k}}$ is transformed, and the innovation ${\tilde {\boldsymbol {y}}}_{k}$ is defined differently. The Jacobian matrix ${{\boldsymbol {H}}_{k}}$ is defined as before, but determined from the implicit observation model $h({\boldsymbol {x}}_{k},{\boldsymbol {z}}_{k})$ .

## Modifications and alternatives

### Iterated extended Kalman filter

The iterated extended Kalman filter improves the linearization of the extended Kalman filter by recursively modifying the centre point of the Taylor expansion. This reduces the linearization error at the cost of increased computational requirements.

### Robust extended Kalman filter

The robust extended Kalman filter arises by linearizing the signal model about the current state estimate and using the linear Kalman filter to predict the next estimate. This attempts to produce a locally optimal filter, however, it is not necessarily stable because the solutions of the underlying Riccati equation are not guaranteed to be positive definite. One way of improving performance is the faux algebraic Riccati technique which trades off optimality for stability. The familiar structure of the extended Kalman filter is retained but stability is achieved by selecting a positive definite solution to a faux algebraic Riccati equation for the gain design.

Another way of improving extended Kalman filter performance is to employ the H-infinity results from robust control. Robust filters are obtained by adding a positive definite term to the design Riccati equation. The additional term is parametrized by a scalar which the designer may tweak to achieve a trade-off between mean-square-error and peak error performance criteria.

### Invariant extended Kalman filter

The invariant extended Kalman filter (IEKF) is a modified version of the EKF for nonlinear systems possessing symmetries (or *invariances*). It combines the advantages of both the EKF and the recently introduced symmetry-preserving filters. Instead of using a linear correction term based on a linear output error, the IEKF uses a geometrically adapted correction term based on an invariant output error; in the same way the gain matrix is not updated from a linear state error, but from an invariant state error. The main benefit is that the gain and covariance equations converge to constant values on a much bigger set of trajectories than equilibrium points as it is the case for the EKF, which results in a better convergence of the estimation.

### Unscented Kalman filters

A nonlinear Kalman filter which shows promise as an improvement over the EKF is the unscented Kalman filter (UKF). In the UKF, the probability density is approximated by a deterministic sampling of points which represent the underlying distribution as a Gaussian. The nonlinear transformation of these points are intended to be an estimation of the posterior distribution, the moments of which can then be derived from the transformed samples. The transformation is known as the unscented transform. The UKF tends to be more robust and more accurate than the EKF in its estimation of error in all the directions.

> "The extended Kalman filter (EKF) is probably the most widely used estimation algorithm for nonlinear systems. However, more than 35 years of experience in the estimation community has shown that is difficult to implement, difficult to tune, and only reliable for systems that are almost linear on the time scale of the updates. Many of these difficulties arise from its use of linearization."

A 2012 paper includes simulation results which suggest that some published variants of the UKF fail to be as accurate as the Second Order Extended Kalman Filter (SOEKF), also known as the augmented Kalman filter. The SOEKF predates the UKF by approximately 35 years with the moment dynamics first described by Bass et al. The difficulty in implementing any Kalman-type filters for nonlinear state transitions stems from the numerical stability issues required for precision, however the UKF does not escape this difficulty in that it uses linearization as well, namely linear regression. The stability issues for the UKF generally stem from the numerical approximation to the square root of the covariance matrix, whereas the stability issues for both the EKF and the SOEKF stem from possible issues in the Taylor Series approximation along the trajectory.

### Ensemble Kalman Filter

The UKF was in fact predated by the Ensemble Kalman filter, invented by Evensen in 1994. It has the advantage over the UKF that the number of ensemble members used can be much smaller than the state dimension, allowing for applications in very high-dimensional systems, such as weather prediction, with state-space sizes of a billion or more.

### Fuzzy Kalman Filter

Fuzzy Kalman filter with a new method to represent possibility distributions was recently proposed to replace probability distributions by possibility distributions in order to obtain a genuine possibilistic filter, enabling the use of non-symmetric process and observation noises as well as higher inaccuracies in both process and observation models.
