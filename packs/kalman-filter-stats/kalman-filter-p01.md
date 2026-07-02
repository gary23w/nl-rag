---
title: "Kalman filter (part 1/2)"
source: https://en.wikipedia.org/wiki/Kalman_filter
domain: kalman-filter-stats
license: CC-BY-SA-4.0
tags: Kalman filter, extended Kalman filter, unscented transform, particle filter
fetched: 2026-07-02
part: 1/2
---

# Kalman filter

In statistics and control theory, **Kalman filtering** (also known as **linear quadratic estimation**) is an algorithm that uses a series of measurements observed over time, including statistical noise and other inaccuracies, to produce estimates of unknown variables that tend to be more accurate than those based on a single measurement, by estimating a joint probability distribution over the variables for each time-step. The filter is constructed as a mean squared error minimiser, but an alternative derivation of the filter is also provided showing how the filter relates to maximum likelihood statistics. The filter is named after Rudolf E. Kálmán.

Kalman filtering has numerous technological applications. A common application is for guidance, navigation, and control of vehicles, particularly aircraft, spacecraft and ships positioned dynamically. Furthermore, Kalman filtering is much applied in time series analysis tasks such as signal processing and econometrics. Kalman filtering is also important for robotic motion planning and control, and can be used for trajectory optimization. Kalman filtering also works for modeling the central nervous system's control of movement. Due to the time delay between issuing motor commands and receiving sensory feedback, the use of Kalman filters provides a realistic model for making estimates of the current state of a motor system and issuing updated commands.

The algorithm works via a two-phase process: a *prediction phase* and an *update phase*. In the prediction phase, the Kalman filter produces estimates of the current state variables, including their uncertainties. Once the outcome of the next measurement (necessarily corrupted with some error, including random noise) is observed, these estimates are updated using a weighted average, with more weight given to estimates with greater certainty. The algorithm is recursive. It can operate in real time, using only the present input measurements and the state calculated previously and its uncertainty matrix; no additional past information is required.

Optimality of Kalman filtering assumes that errors have a normal (Gaussian) distribution. In the words of Rudolf E. Kálmán, "The following assumptions are made about random processes: Physical random phenomena may be thought of as due to primary random sources exciting dynamic systems. The primary sources are assumed to be independent gaussian random processes with zero mean; the dynamic systems will be linear." Regardless of Gaussianity, however, if the process and measurement covariances are known, then the Kalman filter is the best possible *linear* estimator in the minimum mean-square-error sense, although there may be better nonlinear estimators. It is a common misconception (perpetuated in the literature) that the Kalman filter cannot be rigorously applied unless all noise processes are assumed to be Gaussian.

Extensions and generalizations of the method have also been developed, such as the extended Kalman filter and the unscented Kalman filter which work on nonlinear systems. The basis is a hidden Markov model such that the state space of the latent variables is continuous and all latent and observed variables have Gaussian distributions. Kalman filtering has been used successfully in multi-sensor fusion, and distributed sensor networks to develop distributed or consensus Kalman filtering.


## History

The filtering method is named for Hungarian émigré Rudolf E. Kálmán, although Thorvald Nicolai Thiele and Peter Swerling developed a similar algorithm earlier. Richard S. Bucy of the Johns Hopkins Applied Physics Laboratory contributed to the theory, causing it to be known sometimes as Kalman–Bucy filtering. Kalman was inspired to derive the Kalman filter by applying state variables to the Wiener filtering problem. Stanley F. Schmidt is generally credited with developing the first implementation of a Kalman filter. He realized that the filter could be divided into two distinct parts, with one part for time periods between sensor outputs and another part for incorporating measurements. It was during a visit by Kálmán to the NASA Ames Research Center that Schmidt saw the applicability of Kálmán's ideas to the nonlinear problem of trajectory estimation for the Apollo program resulting in its incorporation in the Apollo navigation computer.

This digital filter is sometimes termed the *Stratonovich–Kalman–Bucy filter* because it is a special case of a more general, nonlinear filter developed by the Soviet mathematician Ruslan Stratonovich. In fact, some of the special case linear filter's equations appeared in papers by Stratonovich that were published before the summer of 1961, when Kalman met with Stratonovich during a conference in Moscow.

This Kalman filtering was first described and developed partially in technical papers by Swerling (1958), Kalman (1960) and Kalman and Bucy (1961).

> The Apollo computer used 2k of magnetic core RAM and 36k wire rope [...]. The CPU was built from ICs [...]. Clock speed was under 100 kHz [...]. The fact that the MIT engineers were able to pack such good software (one of the very first applications of the Kalman filter) into such a tiny computer is truly remarkable.

— Interview with Jack Crenshaw, by Matthew Reed, TRS-80.org (2009)

Kalman filters have been vital in the implementation of the navigation systems of U.S. Navy nuclear ballistic missile submarines, and in the guidance and navigation systems of cruise missiles such as the U.S. Navy's Tomahawk missile and the U.S. Air Force's Air Launched Cruise Missile. They are also used in the guidance and navigation systems of reusable launch vehicles and the attitude control and navigation systems of spacecraft which dock at the International Space Station.


## Overview of the calculation

Kalman filtering uses a system's dynamic model (e.g., physical laws of motion), known control inputs to that system, and multiple sequential measurements (such as from sensors) to form an estimate of the system's varying quantities (its state) that is better than the estimate obtained by using only one measurement alone. As such, it is a common sensor fusion and data fusion algorithm.

Noisy sensor data, approximations in the equations that describe the system evolution, and external factors that are not accounted for, all limit how well it is possible to determine the system's state. The Kalman filter deals effectively with the uncertainty due to noisy sensor data and, to some extent, with random external factors. The Kalman filter produces an estimate of the state of the system as an average of the system's predicted state and of the new measurement using a weighted average. The purpose of the weights is that values with better (i.e., smaller) estimated uncertainty are "trusted" more. The weights are calculated from the covariance, a measure of the estimated uncertainty of the prediction of the system's state. The result of the weighted average is a new state estimate that lies between the predicted and measured state, and has a better estimated uncertainty than either alone. This process is repeated at every time step, with the new estimate and its covariance informing the prediction used in the following iteration. This means that Kalman filter works recursively and requires only the last "best guess", rather than the entire history, of a system's state to calculate a new state.

The measurements' certainty-grading and current-state estimate are important considerations. It is common to discuss the filter's response in terms of the Kalman filter's *gain*. The Kalman gain is the weight given to the measurements and current-state estimate, and can be "tuned" to achieve a particular performance. With a high gain, the filter places more weight on the most recent measurements, and thus conforms to them more responsively. With a low gain, the filter conforms to the model predictions more closely. At the extremes, a high gain (close to one) will result in a more jumpy estimated trajectory, while a low gain (close to zero) will smooth out noise but decrease the responsiveness.

When performing the actual calculations for the filter (as discussed below), the state estimate and covariances are coded into matrices because of the multiple dimensions involved in a single set of calculations. This allows for a representation of linear relationships between different state variables (such as position, velocity, and acceleration) in any of the transition models or covariances.


## Example application

As an example application, consider the problem of determining the precise location of a truck. The truck can be equipped with a GPS unit that provides an estimate of the position within a few meters. The GPS estimate is likely to be noisy; readings 'jump around' rapidly, though remaining within a few meters of the real position. In addition, since the truck is expected to follow the laws of physics, its position can also be estimated by integrating its velocity over time, determined by keeping track of wheel revolutions and the angle of the steering wheel. This is a technique known as dead reckoning. Typically, the dead reckoning will provide a very smooth estimate of the truck's position, but it will drift over time as small errors accumulate.

For this example, the Kalman filter can be thought of as operating in two distinct phases: predict and update. In the prediction phase, the truck's old position will be modified according to the physical laws of motion (the dynamic or "state transition" model). Not only will a new position estimate be calculated, but also a new covariance will be calculated as well. Perhaps the covariance is proportional to the speed of the truck because we are more uncertain about the accuracy of the dead reckoning position estimate at high speeds but very certain about the position estimate at low speeds. Next, in the update phase, a measurement of the truck's position is taken from the GPS unit. Along with this measurement comes some amount of uncertainty, and its covariance relative to that of the prediction from the previous phase determines how much the new measurement will affect the updated prediction. Ideally, as the dead reckoning estimates tend to drift away from the real position, the GPS measurement should pull the position estimate back toward the real position but not disturb it to the point of becoming noisy and rapidly jumping.


## Technical description and context

The Kalman filter is an efficient recursive filter estimating the internal state of a linear dynamic system from a series of noisy measurements. It is used in a wide range of engineering and econometric applications from radar and computer vision to estimation of structural macroeconomic models, and is an important topic in control theory and control systems engineering. Together with the linear-quadratic regulator (LQR), the Kalman filter solves the linear–quadratic–Gaussian control problem (LQG). The Kalman filter, the linear-quadratic regulator, and the linear–quadratic–Gaussian controller are solutions to what arguably are the most fundamental problems of control theory.

In most applications, the internal state is much larger (has more degrees of freedom) than the few "observable" parameters which are measured. However, by combining a series of measurements, the Kalman filter can estimate the entire internal state.

For the Dempster–Shafer theory, each state equation or observation is considered a special case of a linear belief function and the Kalman filtering is a special case of combining linear belief functions on a join-tree or Markov tree. Additional methods include belief filtering which use Bayes or evidential updates to the state equations.

A wide variety of Kalman filters exists by now: Kalman's original formulation - now termed the "simple" Kalman filter, the Kalman–Bucy filter, Schmidt's "extended" filter, the information filter, and a variety of "square-root" filters that were developed by Bierman, Thornton, and many others. Perhaps the most commonly used type of very simple Kalman filter is the phase-locked loop, which is now ubiquitous in radios, especially frequency modulation (FM) radios, television sets, satellite communications receivers, outer space communications systems, and nearly any other electronic communications equipment.


## Underlying dynamic system model

Kalman filtering is based on linear dynamic systems discretized in the time domain. They are modeled on a Markov chain built on linear operators perturbed by errors that may include Gaussian noise. The state of the target system refers to the ground truth (yet hidden) system configuration of interest, which is represented as a vector of real numbers. At each discrete time increment, a linear operator is applied to the state to generate the new state, with some noise mixed in, and optionally some information from the controls on the system if they are known. Then, another linear operator mixed with more noise generates the measurable outputs (i.e., observation) from the true ("hidden") state. The Kalman filter may be regarded as analogous to the hidden Markov model, with the difference that the hidden state variables have values in a continuous space as opposed to a discrete state space as for the hidden Markov model. There is a strong analogy between the equations of a Kalman Filter and those of the hidden Markov model. A review of this and other models is given in Roweis and Ghahramani (1999) and Hamilton (1994), Chapter 13.

In order to use the Kalman filter to estimate the internal state of a process given only a sequence of noisy observations, one must model the process in accordance with the following framework. This means specifying the matrices, for each time-step *k*, following:

- $\mathbf {F} _{k}$ , the state-transition model;
- $\mathbf {H} _{k}$ , the observation model;
- $\mathbf {Q} _{k}$ , the covariance of the process noise;
- $\mathbf {R} _{k}$ , the covariance of the observation noise;
- and sometimes $\mathbf {B} _{k}$ , the control-input model as described below; if $\mathbf {B} _{k}$ is included, then there is also
- $\mathbf {u} _{k}$ , the control vector, representing the controlling input into control-input model.

As seen below, it is common in many applications that the matrices $\mathbf {F}$ , $\mathbf {H}$ , $\mathbf {Q}$ , $\mathbf {R}$ , and $\mathbf {B}$ are constant across time, in which case their k index may be dropped.

The Kalman filter model assumes the true state at time k is evolved from the state at $k-1$ according to

$\mathbf {x} _{k}=\mathbf {F} _{k}\mathbf {x} _{k-1}+\mathbf {B} _{k}\mathbf {u} _{k}+\mathbf {w} _{k}$

where

- $\mathbf {F} _{k}$ is the state transition model which is applied to the previous state **x***k*−1;
- $\mathbf {B} _{k}$ is the control-input model which is applied to the control vector $\mathbf {u} _{k}$ ;
- $\mathbf {w} _{k}$ is the process noise, which is assumed to be drawn from a zero mean multivariate normal distribution, ${\mathcal {N}}$ , with covariance, $\mathbf {Q} _{k}$ : $\mathbf {w} _{k}\sim {\mathcal {N}}\left(0,\mathbf {Q} _{k}\right)$ .

If $\mathbf {Q}$ is independent of time, one may, following Roweis and Ghahramani, write $\mathbf {w} _{\bullet }$ instead of $\mathbf {w} _{k}$ to emphasize that the noise has no explicit knowledge of time.

At time k an observation (or measurement) $\mathbf {z} _{k}$ of the true state $\mathbf {x} _{k}$ is made according to

$\mathbf {z} _{k}=\mathbf {H} _{k}\mathbf {x} _{k}+\mathbf {v} _{k}$

where

- $\mathbf {H} _{k}$ is the observation model, which maps the true state space into the observed space and
- $\mathbf {v} _{k}$ is the observation noise, which is assumed to be zero mean Gaussian white noise with covariance $\mathbf {R} _{k}$ : $\mathbf {v} _{k}\sim {\mathcal {N}}\left(0,\mathbf {R} _{k}\right)$ .

Analogously to the situation for $\mathbf {w} _{k}$ , one may write $\mathbf {v} _{\bullet }$ instead of $\mathbf {v} _{k}$ if $\mathbf {R}$ is independent of time.

The initial state, and the noise vectors at each step $\{\mathbf {x} _{0},\mathbf {w} _{1},\dots ,\mathbf {w} _{k},\mathbf {v} _{1},\dots ,\mathbf {v} _{k}\}$ are all assumed to be mutually independent.

Many real-time dynamic systems do not exactly conform to this model. In fact, unmodeled dynamics can seriously degrade the filter performance, even when it was supposed to work with unknown stochastic signals as inputs. The reason for this is that the effect of unmodeled dynamics depends on the input, and, therefore, can bring the estimation algorithm to instability (it diverges). On the other hand, independent white noise signals will not make the algorithm diverge. The problem of distinguishing between measurement noise and unmodeled dynamics is a difficult one and is treated as a problem of control theory using robust control.


## Details

The Kalman filter is a recursive estimator. This means that only the estimated state from the previous time step and the current measurement are needed to compute the estimate for the current state. In contrast to batch estimation techniques, no history of observations and/or estimates is required. In what follows, the notation ${\hat {\mathbf {x} }}_{n\mid m}$ represents the estimate of $\mathbf {x}$ at time *n* given observations up to and including at time *m* ≤ *n*.

The state of the filter is represented by two variables:

- ${\hat {\mathbf {x} }}_{k\mid k}$ , the *a posteriori* state estimate mean at time *k* given observations up to and including at time *k*;
- $\mathbf {P} _{k\mid k}$ , the *a posteriori* estimate covariance matrix (a measure of the estimated accuracy of the state estimate).

The algorithm structure of the Kalman filter resembles that of Alpha beta filter. The Kalman filter can be written as a single equation; however, it is most often conceptualized as two distinct phases: "Predict" and "Update". The predict phase uses the state estimate from the previous timestep to produce an estimate of the state at the current timestep. This predicted state estimate is also known as the *a priori* state estimate because, although it is an estimate of the state at the current timestep, it does not include observation information from the current timestep. In the update phase, the innovation (the pre-fit residual), i.e. the difference between the current *a priori* prediction and the current observation information, is multiplied by the optimal Kalman gain and combined with the previous state estimate to refine the state estimate. This improved estimate based on the current observation is termed the *a posteriori* state estimate.

Typically, the two phases alternate, with the prediction advancing the state until the next scheduled observation, and the update incorporating the observation. However, this is not necessary; if an observation is unavailable for some reason, the update may be skipped and multiple prediction procedures performed. Likewise, if multiple independent observations are available at the same time, multiple update procedures may be performed (typically with different observation matrices **H***k*).

### Predict

| Predicted (*a priori*) state estimate | ${\hat {\mathbf {x} }}_{k\mid k-1}=\mathbf {F} _{k}{\hat {\mathbf {x} }}_{k-1\mid k-1}+\mathbf {B} _{k}\mathbf {u} _{k}$ |
|---|---|
| Predicted (*a priori*) estimate covariance | ${\mathbf {P} }_{k\mid k-1}=\mathbf {F} _{k}\mathbf {P} _{k-1\mid k-1}\mathbf {F} _{k}^{\textsf {T}}+\mathbf {Q} _{k}$ |

### Update

| Innovation or measurement pre-fit residual | ${\tilde {\mathbf {y} }}_{k}=\mathbf {z} _{k}-\mathbf {H} _{k}{\hat {\mathbf {x} }}_{k\mid k-1}$ |
|---|---|
| Innovation (or pre-fit residual) covariance | $\mathbf {S} _{k}=\mathbf {H} _{k}{\mathbf {P} }_{k\mid k-1}\mathbf {H} _{k}^{\textsf {T}}+\mathbf {R} _{k}$ |
| *Optimal* Kalman gain | $\mathbf {K} _{k}={\mathbf {P} }_{k\mid k-1}\mathbf {H} _{k}^{\textsf {T}}\mathbf {S} _{k}^{-1}$ |
| Updated (*a posteriori*) state estimate | ${\hat {\mathbf {x} }}_{k\mid k}={\hat {\mathbf {x} }}_{k\mid k-1}+\mathbf {K} _{k}{\tilde {\mathbf {y} }}_{k}$ |
| Updated (*a posteriori*) estimate covariance (usual form) | $\mathbf {P} _{k\mid k}=\left(\mathbf {I} -\mathbf {K} _{k}\mathbf {H} _{k}\right)\mathbf {P} _{k\|k-1}$ |
| Updated (*a posteriori*) estimate covariance (Joseph form) | $\mathbf {P} _{k\mid k}=\left(\mathbf {I} -\mathbf {K} _{k}\mathbf {H} _{k}\right)\mathbf {P} _{k\mid k-1}\left(\mathbf {I} -\mathbf {K} _{k}\mathbf {H} _{k}\right)^{\textsf {T}}+\mathbf {K} _{k}\mathbf {R} _{k}\mathbf {K} _{k}^{\textsf {T}}$ |
| Measurement post-fit residual | ${\tilde {\mathbf {y} }}_{k\mid k}=\mathbf {z} _{k}-\mathbf {H} _{k}{\hat {\mathbf {x} }}_{k\mid k}$ |

The second formula for the updated (*a posteriori*) estimate covariance above is known as the "Joseph form" that is often used in applications (numerically more stable than the more simple usual formulation). Proof of the formulae is found in the *derivations* section, where the formula valid for any **K**k is also shown.

A more intuitive way to express the updated state estimate ( ${\hat {\mathbf {x} }}_{k\mid k}$ ) is:

${\hat {\mathbf {x} }}_{k\mid k}=(\mathbf {I} -\mathbf {K} _{k}\mathbf {H} _{k}){\hat {\mathbf {x} }}_{k\mid k-1}+\mathbf {K} _{k}\mathbf {z} _{k}$

This expression reminds us of a linear interpolation, $x=(1-t)(a)+t(b)$ for t between [0,1]. In our case:

- t is the matrix $\mathbf {K} _{k}\mathbf {H} _{k}$ that takes values from 0 (high error in the sensor) to I or a projection (low error).
- a is the internal state ${\hat {\mathbf {x} }}_{k\mid k-1}$ estimated from the model.
- b is the internal state $\mathbf {H} _{k}^{-1}\mathbf {z} _{k}$ estimated from the measurement, assuming $\mathbf {H} _{k}$ is nonsingular (which in many applications is not a reasonable assumption e.g. when the state dimension is greater than the observation dimension).

This expression also resembles the alpha beta filter update step.

### Invariants

If the model is accurate, and the values for ${\hat {\mathbf {x} }}_{0\mid 0}$ and $\mathbf {P} _{0\mid 0}$ accurately reflect the distribution of the initial state values, then the following invariants are preserved:

${\begin{aligned}\operatorname {E} [\mathbf {x} _{k}-{\hat {\mathbf {x} }}_{k\mid k}]&=\operatorname {E} [\mathbf {x} _{k}-{\hat {\mathbf {x} }}_{k\mid k-1}]=0\\\operatorname {E} [{\tilde {\mathbf {y} }}_{k}]&=0\end{aligned}}$

where $\operatorname {E} [\xi ]$ is the expected value of $\xi$ . That is, all estimates have a mean error of zero.

Also:

${\begin{aligned}\mathbf {P} _{k\mid k}&=\operatorname {cov} \left(\mathbf {x} _{k}-{\hat {\mathbf {x} }}_{k\mid k}\right)\\\mathbf {P} _{k\mid k-1}&=\operatorname {cov} \left(\mathbf {x} _{k}-{\hat {\mathbf {x} }}_{k\mid k-1}\right)\\\mathbf {S} _{k}&=\operatorname {cov} \left({\tilde {\mathbf {y} }}_{k}\right)\end{aligned}}$

so covariance matrices accurately reflect the covariance of estimates.

### Estimation of the noise covariances Q*k* and R*k*

Practical implementation of a Kalman Filter is often difficult due to the difficulty of getting a good estimate of the noise covariance matrices **Q***k* and **R***k*. Extensive research has been done to estimate these covariances from data. One practical method of doing this is the *autocovariance least-squares* (ALS) technique that uses the time-lagged autocovariances of routine operating data to estimate the covariances. The GNU Octave and Matlab code used to calculate the noise covariance matrices using the ALS technique is available online using the GNU General Public License.

*Field Kalman Filter* (FKF), a Bayesian algorithm, which allows simultaneous estimation of the state, parameters and noise covariance has been proposed. The FKF algorithm has a recursive formulation, good observed convergence, and relatively low complexity, thus suggesting that the FKF algorithm may possibly be a worthwhile alternative to the Autocovariance Least-Squares methods.

Another approach is the *Optimized Kalman Filter* (OKF), which considers the covariance matrices not as representatives of the noise, but rather, as parameters aimed to achieve the most accurate state estimation. These two views coincide under the KF assumptions, but often contradict each other in real systems. Thus, OKF's state estimation is more robust to modeling inaccuracies.

### Optimality and performance

The Kalman filter provides an optimal state estimation in cases where a) the model matches the real system perfectly, b) the entering noise is "white" (uncorrelated), and c) the covariances of the noise are known exactly. Correlated noise can also be treated using Kalman filters.

Several methods for the noise covariance estimation have been proposed during past decades, including ALS, mentioned in the section above. More generally, if the model assumptions do not match the real system perfectly, then optimal state estimation is not necessarily obtained by setting **Q***k* and **R***k* to the covariances of the noise. Instead, in that case, the parameters **Q***k* and **R***k* may be set to explicitly optimize the state estimation, e.g., using standard supervised learning.

After the covariances are set, it is useful to evaluate the performance of the filter; i.e., whether it is possible to improve the state estimation quality. If the Kalman filter works optimally, the innovation sequence (the output prediction error) is a white noise, therefore the whiteness property of the innovations measures filter performance. Several different methods can be used for this purpose. If the noise terms are distributed in a non-Gaussian manner, methods for assessing performance of the filter estimate, which use probability inequalities or large-sample theory, are known in the literature.


## Example application, technical

Consider a truck on frictionless, straight rails. Initially, the truck is stationary at position 0, but it is buffeted this way and that by random uncontrolled forces. We measure the position of the truck every Δ*t* seconds, but these measurements are imprecise; we want to maintain a model of the truck's position and velocity. We show here how we derive the model from which we create our Kalman filter.

Since $\mathbf {F} ,\mathbf {H} ,\mathbf {R} ,\mathbf {Q}$ are constant, their time indices are dropped.

The position and velocity of the truck are described by the linear state space

$\mathbf {x} _{k}={\begin{bmatrix}x\\{\dot {x}}\end{bmatrix}}$

where ${\dot {x}}$ is the velocity, that is, the derivative of position with respect to time.

We assume that between the (*k* − 1) and *k* timestep, uncontrolled forces cause a constant acceleration of *a**k* that is normally distributed with mean 0 and standard deviation *σ**a*. From Newton's laws of motion we conclude that

$\mathbf {x} _{k}=\mathbf {F} \mathbf {x} _{k-1}+\mathbf {G} a_{k}$

(there is no $\mathbf {B} u$ term since there are no known control inputs. Instead, *a**k* is the effect of an unknown input and $\mathbf {G}$ applies that effect to the state vector) where

${\begin{aligned}\mathbf {F} &={\begin{bmatrix}1&\Delta t\\0&1\end{bmatrix}}\\[4pt]\mathbf {G} &={\begin{bmatrix}{\frac {1}{2}}{\Delta t}^{2}\\[6pt]\Delta t\end{bmatrix}}\end{aligned}}$

so that

$\mathbf {x} _{k}=\mathbf {F} \mathbf {x} _{k-1}+\mathbf {w} _{k}$

where

${\begin{aligned}\mathbf {w} _{k}&\sim N(0,\mathbf {Q} )\\\mathbf {Q} &=\mathbf {G} \mathbf {G} ^{\textsf {T}}\sigma _{a}^{2}={\begin{bmatrix}{\frac {1}{4}}{\Delta t}^{4}&{\frac {1}{2}}{\Delta t}^{3}\\[6pt]{\frac {1}{2}}{\Delta t}^{3}&{\Delta t}^{2}\end{bmatrix}}\sigma _{a}^{2}.\end{aligned}}$

The matrix $\mathbf {Q}$ is not full rank (it is of rank one if $\Delta t\neq 0$ ). Hence, the distribution $N(0,\mathbf {Q} )$ is not absolutely continuous and has no probability density function. Another way to express this, avoiding explicit degenerate distributions is given by

$\mathbf {w} _{k}\sim \mathbf {G} \cdot N\left(0,\sigma _{a}^{2}\right).$

At each time phase, a noisy measurement of the true position of the truck is made. Let us suppose the measurement noise *v**k* is also distributed normally, with mean 0 and standard deviation *σ**z*.

$\mathbf {z} _{k}=\mathbf {Hx} _{k}+\mathbf {v} _{k}$

where

$\mathbf {H} ={\begin{bmatrix}1&0\end{bmatrix}}$

and

$\mathbf {R} =\mathrm {E} \left[\mathbf {v} _{k}\mathbf {v} _{k}^{\textsf {T}}\right]={\begin{bmatrix}\sigma _{z}^{2}\end{bmatrix}}$

We know the initial starting state of the truck with perfect precision, so we initialize

${\hat {\mathbf {x} }}_{0\mid 0}={\begin{bmatrix}0\\0\end{bmatrix}}$

and to tell the filter that we know the exact position and velocity, we give it a zero covariance matrix:

$\mathbf {P} _{0\mid 0}={\begin{bmatrix}0&0\\0&0\end{bmatrix}}$

If the initial position and velocity are not known perfectly, the covariance matrix should be initialized with suitable variances on its diagonal:

$\mathbf {P} _{0\mid 0}={\begin{bmatrix}\sigma _{x}^{2}&0\\0&\sigma _{\dot {x}}^{2}\end{bmatrix}}$

The filter will then prefer the information from the first measurements over the information already in the model.


## Asymptotic form

For simplicity, assume that the control input $\mathbf {u} _{k}=\mathbf {0}$ . Then the Kalman filter may be written:

${\hat {\mathbf {x} }}_{k\mid k}=\mathbf {F} _{k}{\hat {\mathbf {x} }}_{k-1\mid k-1}+\mathbf {K} _{k}[\mathbf {z} _{k}-\mathbf {H} _{k}\mathbf {F} _{k}{\hat {\mathbf {x} }}_{k-1\mid k-1}].$

A similar equation holds if we include a non-zero control input. Gain matrices $\mathbf {K} _{k}$ and covariance matrices $\mathbf {P} _{k\mid k}$ evolve independently of the measurements $\mathbf {z} _{k}$ . From above, the four equations needed for updating the matrices are as follows:

${\begin{aligned}\mathbf {P} _{k\mid k-1}&=\mathbf {F} _{k}\mathbf {P} _{k-1\mid k-1}\mathbf {F} _{k}^{\textsf {T}}+\mathbf {Q} _{k},\\\mathbf {S} _{k}&=\mathbf {H} _{k}\mathbf {P} _{k\mid k-1}\mathbf {H} _{k}^{\textsf {T}}+\mathbf {R} _{k},\\\mathbf {K} _{k}&=\mathbf {P} _{k\mid k-1}\mathbf {H} _{k}^{\textsf {T}}\mathbf {S} _{k}^{-1},\\\mathbf {P} _{k|k}&=\left(\mathbf {I} -\mathbf {K} _{k}\mathbf {H} _{k}\right)\mathbf {P} _{k|k-1}.\end{aligned}}$

Since these depend only on the model, and not the measurements, they may be computed offline. Convergence of the gain matrices $\mathbf {K} _{k}$ to an asymptotic matrix $\mathbf {K} _{\infty }$ applies for conditions established in Walrand and Dimakis. If the $\mathbf {P} _{k\mid k}$ series converges, then it converges exponentially to an asymptotic $\mathbf {P} _{\infty }$ , assuming non-zero plant noise. Recent analysis has shown that the *rate and nature* of this convergence can involve multiple coequal modes, including oscillatory components, depending on the eigenstructure of the Jacobian of the above Riccati map evaluated at $\mathbf {P} _{\infty }$ . For the moving truck example described above, with $\Delta t=1$ and $\sigma _{a}^{2}=\sigma _{z}^{2}=\sigma _{x}^{2}=\sigma _{\dot {x}}^{2}=1$ , simulation shows convergence in $10$ iterations.

Using the asymptotic gain, and assuming $\mathbf {H} _{k}$ and $\mathbf {F} _{k}$ are independent of k , the Kalman filter becomes a linear time-invariant filter:

${\hat {\mathbf {x} }}_{k}=\mathbf {F} {\hat {\mathbf {x} }}_{k-1}+\mathbf {K} _{\infty }[\mathbf {z} _{k}-\mathbf {H} \mathbf {F} {\hat {\mathbf {x} }}_{k-1}].$

The asymptotic gain $\mathbf {K} _{\infty }$ , if it exists, can be computed by first solving the following discrete Riccati equation for the asymptotic state covariance $\mathbf {P} _{\infty }$ :

$\mathbf {P} _{\infty }=\mathbf {F} \left(\mathbf {P} _{\infty }-\mathbf {P} _{\infty }\mathbf {H} ^{\textsf {T}}\left(\mathbf {H} \mathbf {P} _{\infty }\mathbf {H} ^{\textsf {T}}+\mathbf {R} \right)^{-1}\mathbf {H} \mathbf {P} _{\infty }\right)\mathbf {F} ^{\textsf {T}}+\mathbf {Q} .$

The asymptotic gain is then computed as before.

$\mathbf {K} _{\infty }=\mathbf {P} _{\infty }\mathbf {H} ^{\textsf {T}}\left(\mathbf {R} +\mathbf {H} \mathbf {P} _{\infty }\mathbf {H} ^{\textsf {T}}\right)^{-1}.$

Additionally, a form of the asymptotic Kalman filter more commonly used in control theory is given by

${\displaystyle {\hat {\mathbf {x} }}_{k+1}=\mathbf {F} {\hat {\mathbf {x} }}_{k}+\mathbf {B} \mathbf {u} _{k}+\mathbf {\overline {K}} _{\infty }[\mathbf {z} _{k}-\mathbf {H} {\hat {\mathbf {x} }}_{k}],}$

where

${\overline {\mathbf {K} }}_{\infty }=\mathbf {F} \mathbf {P} _{\infty }\mathbf {H} ^{\textsf {T}}\left(\mathbf {R} +\mathbf {H} \mathbf {P} _{\infty }\mathbf {H} ^{\textsf {T}}\right)^{-1}.$

This leads to an estimator of the form

${\displaystyle {\hat {\mathbf {x} }}_{k+1}=(\mathbf {F} -{\overline {\mathbf {K} }}_{\infty }\mathbf {H} ){\hat {\mathbf {x} }}_{k}+\mathbf {B} \mathbf {u} _{k}+\mathbf {\overline {K}} _{\infty }\mathbf {z} _{k}.}$


## Derivations

The Kalman filter can be derived as a generalized least squares method operating on previous data.

### Deriving the *posteriori* estimate covariance matrix

Starting with our invariant on the error covariance **P***k* | *k* as above

$\mathbf {P} _{k\mid k}=\operatorname {cov} \left(\mathbf {x} _{k}-{\hat {\mathbf {x} }}_{k\mid k}\right)$

substitute in the definition of ${\hat {\mathbf {x} }}_{k\mid k}$

$\mathbf {P} _{k\mid k}=\operatorname {cov} \left[\mathbf {x} _{k}-\left({\hat {\mathbf {x} }}_{k\mid k-1}+\mathbf {K} _{k}{\tilde {\mathbf {y} }}_{k}\right)\right]$

and substitute ${\tilde {\mathbf {y} }}_{k}$

$\mathbf {P} _{k\mid k}=\operatorname {cov} \left(\mathbf {x} _{k}-\left[{\hat {\mathbf {x} }}_{k\mid k-1}+\mathbf {K} _{k}\left(\mathbf {z} _{k}-\mathbf {H} _{k}{\hat {\mathbf {x} }}_{k\mid k-1}\right)\right]\right)$

and $\mathbf {z} _{k}$

$\mathbf {P} _{k\mid k}=\operatorname {cov} \left(\mathbf {x} _{k}-\left[{\hat {\mathbf {x} }}_{k\mid k-1}+\mathbf {K} _{k}\left(\mathbf {H} _{k}\mathbf {x} _{k}+\mathbf {v} _{k}-\mathbf {H} _{k}{\hat {\mathbf {x} }}_{k\mid k-1}\right)\right]\right)$

and by collecting the error vectors we get

$\mathbf {P} _{k\mid k}=\operatorname {cov} \left[\left(\mathbf {I} -\mathbf {K} _{k}\mathbf {H} _{k}\right)\left(\mathbf {x} _{k}-{\hat {\mathbf {x} }}_{k\mid k-1}\right)-\mathbf {K} _{k}\mathbf {v} _{k}\right]$

Since the measurement error **v***k* is uncorrelated with the other terms, this becomes

$\mathbf {P} _{k\mid k}=\operatorname {cov} \left[\left(\mathbf {I} -\mathbf {K} _{k}\mathbf {H} _{k}\right)\left(\mathbf {x} _{k}-{\hat {\mathbf {x} }}_{k\mid k-1}\right)\right]+\operatorname {cov} \left[\mathbf {K} _{k}\mathbf {v} _{k}\right]$

by the properties of vector covariance this becomes

$\mathbf {P} _{k\mid k}=\left(\mathbf {I} -\mathbf {K} _{k}\mathbf {H} _{k}\right)\operatorname {cov} \left(\mathbf {x} _{k}-{\hat {\mathbf {x} }}_{k\mid k-1}\right)\left(\mathbf {I} -\mathbf {K} _{k}\mathbf {H} _{k}\right)^{\textsf {T}}+\mathbf {K} _{k}\operatorname {cov} \left(\mathbf {v} _{k}\right)\mathbf {K} _{k}^{\textsf {T}}$

which, using our invariant on **P***k* | *k*−1 and the definition of **R***k* becomes

$\mathbf {P} _{k\mid k}=\left(\mathbf {I} -\mathbf {K} _{k}\mathbf {H} _{k}\right)\mathbf {P} _{k\mid k-1}\left(\mathbf {I} -\mathbf {K} _{k}\mathbf {H} _{k}\right)^{\textsf {T}}+\mathbf {K} _{k}\mathbf {R} _{k}\mathbf {K} _{k}^{\textsf {T}}$

This formula (sometimes known as the **Joseph form** of the covariance update equation) is valid for any value of **K***k*. It turns out that if **K***k* is the optimal Kalman gain, this can be simplified further as shown below.

### Kalman gain derivation

The Kalman filter is a minimum mean-square error (MMSE) estimator. The error in the *a posteriori* state estimation is

$\mathbf {x} _{k}-{\hat {\mathbf {x} }}_{k\mid k}$

We seek to minimize the expected value of the square of the magnitude of this vector, $\operatorname {E} \left[\left\|\mathbf {x} _{k}-{\hat {\mathbf {x} }}_{k|k}\right\|^{2}\right]$ . This is equivalent to minimizing the trace of the *a posteriori* estimate covariance matrix $\mathbf {P} _{k|k}$ . By expanding out the terms in the equation above and collecting, we get:

${\begin{aligned}\mathbf {P} _{k\mid k}&=\mathbf {P} _{k\mid k-1}-\mathbf {K} _{k}\mathbf {H} _{k}\mathbf {P} _{k\mid k-1}-\mathbf {P} _{k\mid k-1}\mathbf {H} _{k}^{\textsf {T}}\mathbf {K} _{k}^{\textsf {T}}+\mathbf {K} _{k}\left(\mathbf {H} _{k}\mathbf {P} _{k\mid k-1}\mathbf {H} _{k}^{\textsf {T}}+\mathbf {R} _{k}\right)\mathbf {K} _{k}^{\textsf {T}}\\[6pt]&=\mathbf {P} _{k\mid k-1}-\mathbf {K} _{k}\mathbf {H} _{k}\mathbf {P} _{k\mid k-1}-\mathbf {P} _{k\mid k-1}\mathbf {H} _{k}^{\textsf {T}}\mathbf {K} _{k}^{\textsf {T}}+\mathbf {K} _{k}\mathbf {S} _{k}\mathbf {K} _{k}^{\textsf {T}}\end{aligned}}$

The trace is minimized when its matrix derivative with respect to the gain matrix is zero. Using the gradient matrix rules and the symmetry of the matrices involved we find that

${\frac {\partial \;\operatorname {tr} (\mathbf {P} _{k\mid k})}{\partial \;\mathbf {K} _{k}}}=-2\left(\mathbf {H} _{k}\mathbf {P} _{k\mid k-1}\right)^{\textsf {T}}+2\mathbf {K} _{k}\mathbf {S} _{k}=0.$

Solving this for **K***k* yields the Kalman gain:

${\begin{aligned}\mathbf {K} _{k}\mathbf {S} _{k}&=\left(\mathbf {H} _{k}\mathbf {P} _{k\mid k-1}\right)^{\textsf {T}}=\mathbf {P} _{k\mid k-1}\mathbf {H} _{k}^{\textsf {T}}\\\Rightarrow \mathbf {K} _{k}&=\mathbf {P} _{k\mid k-1}\mathbf {H} _{k}^{\textsf {T}}\mathbf {S} _{k}^{-1}\end{aligned}}$

This gain, which is known as the *optimal Kalman gain*, is the one that yields MMSE estimates when used.

### Simplification of the *posteriori* error covariance formula

The formula used to calculate the *a posteriori* error covariance can be simplified when the Kalman gain equals the optimal value derived above. Multiplying both sides of our Kalman gain formula on the right by **S***k***K***k*T, it follows that

$\mathbf {K} _{k}\mathbf {S} _{k}\mathbf {K} _{k}^{\textsf {T}}=\mathbf {P} _{k\mid k-1}\mathbf {H} _{k}^{\textsf {T}}\mathbf {K} _{k}^{\textsf {T}}$

Referring back to our expanded formula for the *a posteriori* error covariance,

$\mathbf {P} _{k\mid k}=\mathbf {P} _{k\mid k-1}-\mathbf {K} _{k}\mathbf {H} _{k}\mathbf {P} _{k\mid k-1}-\mathbf {P} _{k\mid k-1}\mathbf {H} _{k}^{\textsf {T}}\mathbf {K} _{k}^{\textsf {T}}+\mathbf {K} _{k}\mathbf {S} _{k}\mathbf {K} _{k}^{\textsf {T}}$

we find the last two terms cancel out, giving

$\mathbf {P} _{k\mid k}=\mathbf {P} _{k\mid k-1}-\mathbf {K} _{k}\mathbf {H} _{k}\mathbf {P} _{k\mid k-1}=(\mathbf {I} -\mathbf {K} _{k}\mathbf {H} _{k})\mathbf {P} _{k\mid k-1}$

This formula is computationally cheaper and thus nearly always used in practice, but is only correct for the optimal gain. If arithmetic precision is unusually low causing problems with numerical stability, or if a non-optimal Kalman gain is deliberately used, this simplification cannot be applied; the *a posteriori* error covariance formula as derived above (Joseph form) must be used.


## Sensitivity analysis

The Kalman filtering equations provide an estimate of the state ${\hat {\mathbf {x} }}_{k\mid k}$ and its error covariance $\mathbf {P} _{k\mid k}$ recursively. The estimate and its quality depend on the system parameters and the noise statistics fed as inputs to the estimator. This section analyzes the effect of uncertainties in the statistical inputs to the filter. In the absence of reliable statistics or the true values of noise covariance matrices $\mathbf {Q} _{k}$ and $\mathbf {R} _{k}$ , the expression

$\mathbf {P} _{k\mid k}=\left(\mathbf {I} -\mathbf {K} _{k}\mathbf {H} _{k}\right)\mathbf {P} _{k\mid k-1}\left(\mathbf {I} -\mathbf {K} _{k}\mathbf {H} _{k}\right)^{\textsf {T}}+\mathbf {K} _{k}\mathbf {R} _{k}\mathbf {K} _{k}^{\textsf {T}}$

no longer provides the actual error covariance. In other words, $\mathbf {P} _{k\mid k}\neq E\left[\left(\mathbf {x} _{k}-{\hat {\mathbf {x} }}_{k\mid k}\right)\left(\mathbf {x} _{k}-{\hat {\mathbf {x} }}_{k\mid k}\right)^{\textsf {T}}\right]$ . In most real-time applications, the covariance matrices that are used in designing the Kalman filter are different from the actual (true) noise covariances matrices. This sensitivity analysis describes the behavior of the estimation error covariance when the noise covariances as well as the system matrices $\mathbf {F} _{k}$ and $\mathbf {H} _{k}$ that are fed as inputs to the filter are incorrect. Thus, the sensitivity analysis describes the robustness (or sensitivity) of the estimator to misspecified statistical and parametric inputs to the estimator.

This discussion is limited to the error sensitivity analysis for the case of statistical uncertainties. Here the actual noise covariances are denoted by $\mathbf {Q} _{k}^{a}$ and $\mathbf {R} _{k}^{a}$ respectively, whereas the design values used in the estimator are $\mathbf {Q} _{k}$ and $\mathbf {R} _{k}$ respectively. The actual error covariance is denoted by $\mathbf {P} _{k\mid k}^{a}$ and $\mathbf {P} _{k\mid k}$ as computed by the Kalman filter is referred to as the Riccati variable. When $\mathbf {Q} _{k}\equiv \mathbf {Q} _{k}^{a}$ and $\mathbf {R} _{k}\equiv \mathbf {R} _{k}^{a}$ , this means that $\mathbf {P} _{k\mid k}=\mathbf {P} _{k\mid k}^{a}$ . While computing the actual error covariance using $\mathbf {P} _{k\mid k}^{a}=E\left[\left(\mathbf {x} _{k}-{\hat {\mathbf {x} }}_{k\mid k}\right)\left(\mathbf {x} _{k}-{\hat {\mathbf {x} }}_{k\mid k}\right)^{\textsf {T}}\right]$ , substituting for ${\widehat {\mathbf {x} }}_{k\mid k}$ and using the fact that $E\left[\mathbf {w} _{k}\mathbf {w} _{k}^{\textsf {T}}\right]=\mathbf {Q} _{k}^{a}$ and $E\left[\mathbf {v} _{k}\mathbf {v} _{k}^{\textsf {T}}\right]=\mathbf {R} _{k}^{a}$ , results in the following recursive equations for $\mathbf {P} _{k\mid k}^{a}$  :

$\mathbf {P} _{k\mid k-1}^{a}=\mathbf {F} _{k}\mathbf {P} _{k-1\mid k-1}^{a}\mathbf {F} _{k}^{\textsf {T}}+\mathbf {Q} _{k}^{a}$

and

$\mathbf {P} _{k\mid k}^{a}=\left(\mathbf {I} -\mathbf {K} _{k}\mathbf {H} _{k}\right)\mathbf {P} _{k\mid k-1}^{a}\left(\mathbf {I} -\mathbf {K} _{k}\mathbf {H} _{k}\right)^{\textsf {T}}+\mathbf {K} _{k}\mathbf {R} _{k}^{a}\mathbf {K} _{k}^{\textsf {T}}$

While computing $\mathbf {P} _{k\mid k}$ , by design the filter implicitly assumes that $E\left[\mathbf {w} _{k}\mathbf {w} _{k}^{\textsf {T}}\right]=\mathbf {Q} _{k}$ and $E\left[\mathbf {v} _{k}\mathbf {v} _{k}^{\textsf {T}}\right]=\mathbf {R} _{k}$ . The recursive expressions for $\mathbf {P} _{k\mid k}^{a}$ and $\mathbf {P} _{k\mid k}$ are identical except for the presence of $\mathbf {Q} _{k}^{a}$ and $\mathbf {R} _{k}^{a}$ in place of the design values $\mathbf {Q} _{k}$ and $\mathbf {R} _{k}$ respectively. Researches have been done to analyze Kalman filter system's robustness.


## Factored form

One problem with the Kalman filter is its numerical stability. If the process noise covariance **Q***k* is small, round-off error often causes a small positive eigenvalue of the state covariance matrix **P** to be computed as a negative number. This renders the numerical representation of **P** indefinite, while its true form is positive-definite.

Positive definite matrices have the property that they have a factorization into the product of a non-singular, lower-triangular matrix **S** and its transpose : **P** = **S**·**S**T . The factor **S** can be computed efficiently using the Cholesky factorization algorithm. This product form of the covariance matrix **P** is guaranteed to be symmetric, and for all 1 <= k <= n, the k-th diagonal element **P**kk is equal to the square of the euclidean norm of the k-th row of **S**, which is necessarily positive. An equivalent form, which avoids many of the square root operations involved in the Cholesky factorization algorithm, yet preserves the desirable numerical properties, is the U-D decomposition form, **P** = **U**·**D**·**U**T, where **U** is a unit triangular matrix (with unit diagonal), and **D** is a diagonal matrix.

Between the two, the U-D factorization uses the same amount of storage, and somewhat less computation, and is the most commonly used triangular factorization. (Early literature on the relative efficiency is somewhat misleading, as it assumed that square roots were much more time-consuming than divisions, while on 21st-century computers they are only slightly more expensive.)

Efficient algorithms for the Kalman prediction and update steps in the factored form were developed by G. J. Bierman and C. L. Thornton.

The **L**·**D**·**L**T decomposition of the innovation covariance matrix **S**k is the basis for another type of numerically efficient and robust square root filter. The algorithm starts with the LU decomposition as implemented in the Linear Algebra PACKage (LAPACK). These results are further factored into the **L**·**D**·**L**T structure with methods given by Golub and Van Loan (algorithm 4.1.2) for a symmetric nonsingular matrix. Any singular covariance matrix is pivoted so that the first diagonal partition is nonsingular and well-conditioned. The pivoting algorithm must retain any portion of the innovation covariance matrix directly corresponding to observed state-variables **H**k·**x**k|k-1 that are associated with auxiliary observations in **y**k. The **l**·**d**·**l**t square-root filter requires orthogonalization of the observation vector. This may be done with the inverse square-root of the covariance matrix for the auxiliary variables using Method 2 in Higham (2002, p. 263).


## Parallel form

The Kalman filter is efficient for sequential data processing on central processing units (CPUs), but in its original form it is inefficient on parallel architectures such as graphics processing units (GPUs). It is however possible to express the filter-update routine in terms of an associative operator using the formulation in Särkkä and García-Fernández (2021). The filter solution can then be retrieved by the use of a prefix sum algorithm which can be efficiently implemented on GPU. This reduces the computational complexity from $O(N)$ in the number of time steps to $O(\log(N))$ .
