---
title: "Kalman filter (part 3/3)"
source: https://en.wikipedia.org/wiki/Kalman_filter
domain: control-systems
license: CC-BY-SA-4.0
tags: control theory, pid controller, feedback loop, control system, kalman filter, servo
fetched: 2026-07-02
part: 3/3
---

## Hybrid Kalman filter

Most physical systems are represented as continuous-time models while discrete-time measurements are made frequently for state estimation via a digital processor. Therefore, the system model and measurement model are given by

x

˙

(

t

)

=

F

(

t

)

x

(

t

)

+

B

(

t

)

u

(

t

)

+

w

(

t

)

,

w

(

t

)

∼

N

(

0

,

Q

(

t

)

)

z

k

=

H

k

x

k

+

v

k

,

v

k

∼

N

(

0

,

R

k

)

{\displaystyle {\begin{aligned}{\dot {\mathbf {x} }}(t)&=\mathbf {F} (t)\mathbf {x} (t)+\mathbf {B} (t)\mathbf {u} (t)+\mathbf {w} (t),&\mathbf {w} (t)&\sim N\left(\mathbf {0} ,\mathbf {Q} (t)\right)\\\mathbf {z} _{k}&=\mathbf {H} _{k}\mathbf {x} _{k}+\mathbf {v} _{k},&\mathbf {v} _{k}&\sim N(\mathbf {0} ,\mathbf {R} _{k})\end{aligned}}}

where

x

k

=

x

(

t

k

)

{\displaystyle \mathbf {x} _{k}=\mathbf {x} (t_{k})}

.

### Initialize

x

^

0

∣

0

=

E

[

x

(

t

0

)

]

,

P

0

∣

0

=

Var

⁡

[

x

(

t

0

)

]

{\displaystyle {\hat {\mathbf {x} }}_{0\mid 0}=E\left[\mathbf {x} (t_{0})\right],\mathbf {P} _{0\mid 0}=\operatorname {Var} \left[\mathbf {x} \left(t_{0}\right)\right]}

### Predict

x

^

˙

(

t

)

=

F

(

t

)

x

^

(

t

)

+

B

(

t

)

u

(

t

)

, with

x

^

(

t

k

−

1

)

=

x

^

k

−

1

∣

k

−

1

⇒

x

^

k

∣

k

−

1

=

x

^

(

t

k

)

P

˙

(

t

)

=

F

(

t

)

P

(

t

)

+

P

(

t

)

F

(

t

)

T

+

Q

(

t

)

, with

P

(

t

k

−

1

)

=

P

k

−

1

∣

k

−

1

⇒

P

k

∣

k

−

1

=

P

(

t

k

)

{\displaystyle {\begin{aligned}{\dot {\hat {\mathbf {x} }}}(t)&=\mathbf {F} (t){\hat {\mathbf {x} }}(t)+\mathbf {B} (t)\mathbf {u} (t){\text{, with }}{\hat {\mathbf {x} }}\left(t_{k-1}\right)={\hat {\mathbf {x} }}_{k-1\mid k-1}\\\Rightarrow {\hat {\mathbf {x} }}_{k\mid k-1}&={\hat {\mathbf {x} }}\left(t_{k}\right)\\{\dot {\mathbf {P} }}(t)&=\mathbf {F} (t)\mathbf {P} (t)+\mathbf {P} (t)\mathbf {F} (t)^{\textsf {T}}+\mathbf {Q} (t){\text{, with }}\mathbf {P} \left(t_{k-1}\right)=\mathbf {P} _{k-1\mid k-1}\\\Rightarrow \mathbf {P} _{k\mid k-1}&=\mathbf {P} \left(t_{k}\right)\end{aligned}}}

The prediction equations are derived from those of continuous-time Kalman filter without update from measurements, i.e., $\mathbf {K} (t)=0$ . The predicted state and covariance are calculated respectively by solving a set of differential equations with the initial value equal to the estimate at the previous step.

For the case of linear time invariant systems, the continuous time dynamics can be exactly discretized into a discrete time system using matrix exponentials.

### Update

K

k

=

P

k

∣

k

−

1

H

k

T

(

H

k

P

k

∣

k

−

1

H

k

T

+

R

k

)

−

1

x

^

k

∣

k

=

x

^

k

∣

k

−

1

+

K

k

(

z

k

−

H

k

x

^

k

∣

k

−

1

)

P

k

∣

k

=

(

I

−

K

k

H

k

)

P

k

∣

k

−

1

{\displaystyle {\begin{aligned}\mathbf {K} _{k}&=\mathbf {P} _{k\mid k-1}\mathbf {H} _{k}^{\textsf {T}}\left(\mathbf {H} _{k}\mathbf {P} _{k\mid k-1}\mathbf {H} _{k}^{\textsf {T}}+\mathbf {R} _{k}\right)^{-1}\\{\hat {\mathbf {x} }}_{k\mid k}&={\hat {\mathbf {x} }}_{k\mid k-1}+\mathbf {K} _{k}\left(\mathbf {z} _{k}-\mathbf {H} _{k}{\hat {\mathbf {x} }}_{k\mid k-1}\right)\\\mathbf {P} _{k\mid k}&=\left(\mathbf {I} -\mathbf {K} _{k}\mathbf {H} _{k}\right)\mathbf {P} _{k\mid k-1}\end{aligned}}}

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
