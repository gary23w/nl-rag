---
title: "State-space representation"
source: https://en.wikipedia.org/wiki/State-space_representation
domain: control-systems
license: CC-BY-SA-4.0
tags: control theory, pid controller, feedback loop, control system, kalman filter, servo
fetched: 2026-07-02
---

# State-space representation

In control engineering and system identification, a **state-space representation** is a mathematical model of a physical system that uses state variables to track how inputs shape system behavior over time through first-order differential equations or difference equations. These state variables change based on their current values and inputs, while outputs depend on the states and sometimes the inputs too. The **state space** (also called **time-domain approach** and equivalent to phase space in certain dynamical systems) is a geometric space where the axes are these state variables, and the system’s state is represented by a state vector.

For linear, time-invariant, and finite-dimensional systems, the equations can be written in matrix form, offering a compact alternative to the frequency domain’s Laplace transforms for multiple-input and multiple-output (MIMO) systems. Unlike the frequency domain approach, it works for systems beyond just linear ones with zero initial conditions. This approach turns systems theory into an algebraic framework, making it possible to use Kronecker structures for efficient analysis.

State-space models are applied in fields such as economics, statistics, computer science, electrical engineering, and neuroscience. In econometrics, for example, state-space models can be used to decompose a time series into trend and cycle, compose individual indicators into a composite index, identify turning points of the business cycle, and estimate GDP using latent and unobserved time series. Many applications rely on the Kalman Filter or a state observer to produce estimates of the current unknown state variables using their previous observations.

## State variables

The internal state variables are the smallest possible subset of system variables that can represent the entire state of the system at any given time. The minimum number of state variables required to represent a given system, n , is usually equal to the order of the system's defining differential equation, but not necessarily. If the system is represented in transfer function form, the minimum number of state variables is equal to the order of the transfer function's denominator after it has been reduced to a proper fraction. It is important to understand that converting a state-space realization to a transfer function form may lose some internal information about the system, and may provide a description of a system which is stable, when the state-space realization is unstable at certain points. In electric circuits, the number of state variables is often, though not always, the same as the number of energy storage elements in the circuit such as capacitors and inductors. The state variables defined must be linearly independent, i.e., no state variable can be written as a linear combination of the other state variables.

## Linear systems

The most general state-space representation of a linear system with p inputs, q outputs and n state variables is written in the following form: ${\dot {\mathbf {x} }}(t)=\mathbf {A} (t)\mathbf {x} (t)+\mathbf {B} (t)\mathbf {u} (t)$ $\mathbf {y} (t)=\mathbf {C} (t)\mathbf {x} (t)+\mathbf {D} (t)\mathbf {u} (t)$

where:

- $\mathbf {x} (\cdot )$ is called the "state vector", $\mathbf {x} (t)\in \mathbb {R} ^{n}$ ;
- $\mathbf {y} (\cdot )$ is called the "output vector", $\mathbf {y} (t)\in \mathbb {R} ^{q}$ ;
- $\mathbf {u} (\cdot )$ is called the "input (or control) vector", $\mathbf {u} (t)\in \mathbb {R} ^{p}$ ;
- $\mathbf {A} (\cdot )$ is the "state (or system) matrix", $\dim[\mathbf {A} (\cdot )]=n\times n$ ,
- $\mathbf {B} (\cdot )$ is the "input matrix", $\dim[\mathbf {B} (\cdot )]=n\times p$ ,
- $\mathbf {C} (\cdot )$ is the "output matrix", $\dim[\mathbf {C} (\cdot )]=q\times n$ ,
- $\mathbf {D} (\cdot )$ is the "feedthrough (or feedforward) matrix" (in cases where the system model does not have a direct feedthrough, $\mathbf {D} (\cdot )$ is the zero matrix), $\dim[\mathbf {D} (\cdot )]=q\times p$ ,
- ${\dot {\mathbf {x} }}(t):={\frac {d}{dt}}\mathbf {x} (t)$ .

In this general formulation, all matrices are allowed to be time-variant (i.e. their elements can depend on time); however, in the common LTI case, matrices will be time invariant. The time variable t can be continuous (e.g. $t\in \mathbb {R}$ ) or discrete (e.g. $t\in \mathbb {Z}$ ). In the latter case, the time variable k is usually used instead of t . Hybrid systems allow for time domains that have both continuous and discrete parts. Depending on the assumptions made, the state-space model representation can assume the following forms:

| System type | State-space model |
|---|---|
| Continuous time-invariant | ${\dot {\mathbf {x} }}(t)=\mathbf {A} \mathbf {x} (t)+\mathbf {B} \mathbf {u} (t)$ $\mathbf {y} (t)=\mathbf {C} \mathbf {x} (t)+\mathbf {D} \mathbf {u} (t)$ |
| Continuous time-variant | ${\dot {\mathbf {x} }}(t)=\mathbf {A} (t)\mathbf {x} (t)+\mathbf {B} (t)\mathbf {u} (t)$ $\mathbf {y} (t)=\mathbf {C} (t)\mathbf {x} (t)+\mathbf {D} (t)\mathbf {u} (t)$ |
| Explicit discrete time-invariant | $\mathbf {x} (k+1)=\mathbf {A} \mathbf {x} (k)+\mathbf {B} \mathbf {u} (k)$ $\mathbf {y} (k)=\mathbf {C} \mathbf {x} (k)+\mathbf {D} \mathbf {u} (k)$ |
| Explicit discrete time-variant | $\mathbf {x} (k+1)=\mathbf {A} (k)\mathbf {x} (k)+\mathbf {B} (k)\mathbf {u} (k)$ $\mathbf {y} (k)=\mathbf {C} (k)\mathbf {x} (k)+\mathbf {D} (k)\mathbf {u} (k)$ |
| Laplace domain of continuous time-invariant | $s\mathbf {X} (s)-\mathbf {x} (0)=\mathbf {A} \mathbf {X} (s)+\mathbf {B} \mathbf {U} (s)$ $\mathbf {Y} (s)=\mathbf {C} \mathbf {X} (s)+\mathbf {D} \mathbf {U} (s)$ |
| Z-domain of discrete time-invariant | $z\mathbf {X} (z)-z\mathbf {x} (0)=\mathbf {A} \mathbf {X} (z)+\mathbf {B} \mathbf {U} (z)$ $\mathbf {Y} (z)=\mathbf {C} \mathbf {X} (z)+\mathbf {D} \mathbf {U} (z)$ |

### Example: continuous-time LTI case

Stability and natural response characteristics of a continuous-time LTI system (i.e., linear with matrices that are constant with respect to time) can be studied from the eigenvalues of the matrix $\mathbf {A}$ . The stability of a time-invariant state-space model can be determined by looking at the system's transfer function in factored form. It will then look something like this:

$\mathbf {G} (s)=k{\frac {(s-z_{1})(s-z_{2})(s-z_{3})}{(s-p_{1})(s-p_{2})(s-p_{3})(s-p_{4})}}.$

The denominator of the transfer function is equal to the characteristic polynomial found by taking the determinant of $s\mathbf {I} -\mathbf {A}$ , $\lambda (s)=\left|s\mathbf {I} -\mathbf {A} \right|.$ The roots of this polynomial (the eigenvalues) are the system transfer function's poles (i.e., the singularities where the transfer function's magnitude is unbounded). These poles can be used to analyze whether the system is asymptotically stable or marginally stable. An alternative approach to determining stability, which does not involve calculating eigenvalues, is to analyze the system's Lyapunov stability.

The zeros found in the numerator of $\mathbf {G} (s)$ can similarly be used to determine whether the system is minimum phase.

The system may still be **input–output stable** (see BIBO stable) even though it is not internally stable. This may be the case if unstable poles are canceled out by zeros (i.e., if those singularities in the transfer function are removable).

### Controllability

The state controllability condition implies that it is possible – by admissible inputs – to steer the states from any initial value to any final value within some finite time window. A continuous time-invariant linear state-space model is **controllable** if and only if $\operatorname {rank} {\begin{bmatrix}\mathbf {B} &\mathbf {A} \mathbf {B} &\mathbf {A} ^{2}\mathbf {B} &\cdots &\mathbf {A} ^{n-1}\mathbf {B} \end{bmatrix}}=n,$ where rank is the number of linearly independent rows in a matrix, and where *n* is the number of state variables.

### Observability

Observability is a measure for how well internal states of a system can be inferred by knowledge of its external outputs. The observability and controllability of a system are mathematical duals (i.e., as controllability provides that an input is available that brings any initial state to any desired final state, observability provides that knowing an output trajectory provides enough information to predict the initial state of the system).

A continuous time-invariant linear state-space model is **observable** if and only if $\operatorname {rank} {\begin{bmatrix}\mathbf {C} \\\mathbf {C} \mathbf {A} \\\vdots \\\mathbf {C} \mathbf {A} ^{n-1}\end{bmatrix}}=n.$

### Transfer function

The "transfer function" of a continuous time-invariant linear state-space model can be derived in the following way:

First, taking the Laplace transform of ${\dot {\mathbf {x} }}(t)=\mathbf {A} \mathbf {x} (t)+\mathbf {B} \mathbf {u} (t)$

yields $s\mathbf {X} (s)-\mathbf {x} (0)=\mathbf {A} \mathbf {X} (s)+\mathbf {B} \mathbf {U} (s).$ Next, we simplify for $\mathbf {X} (s)$ , giving $(s\mathbf {I} -\mathbf {A} )\mathbf {X} (s)=\mathbf {x} (0)+\mathbf {B} \mathbf {U} (s)$ and thus $\mathbf {X} (s)=(s\mathbf {I} -\mathbf {A} )^{-1}\mathbf {x} (0)+(s\mathbf {I} -\mathbf {A} )^{-1}\mathbf {B} \mathbf {U} (s).$

Substituting for $\mathbf {X} (s)$ in the output equation

$\mathbf {Y} (s)=\mathbf {C} \mathbf {X} (s)+\mathbf {D} \mathbf {U} (s),$ giving $\mathbf {Y} (s)=\mathbf {C} ((s\mathbf {I} -\mathbf {A} )^{-1}\mathbf {x} (0)+(s\mathbf {I} -\mathbf {A} )^{-1}\mathbf {B} \mathbf {U} (s))+\mathbf {D} \mathbf {U} (s).$

Assuming zero initial conditions $\mathbf {x} (0)=\mathbf {0}$ and a single-input single-output (SISO) system, the transfer function is defined as the ratio of output and input $G(s)=Y(s)/U(s)$ . For a multiple-input multiple-output (MIMO) system, however, this ratio is not defined. Therefore, assuming zero initial conditions, the transfer function matrix is derived from $\mathbf {Y} (s)=\mathbf {G} (s)\mathbf {U} (s)$

using the method of equating the coefficients which yields

$\mathbf {G} (s)=\mathbf {C} (s\mathbf {I} -\mathbf {A} )^{-1}\mathbf {B} +\mathbf {D} .$

Consequently, $\mathbf {G} (s)$ is a matrix with the dimension $q\times p$ which contains transfer functions for each input output combination. Due to the simplicity of this matrix notation, the state-space representation is commonly used for multiple-input, multiple-output systems. The Rosenbrock system matrix provides a bridge between the state-space representation and its transfer function.

### Canonical realizations

Any given transfer function which is strictly proper can easily be transferred into state-space by the following approach (this example is for a 4-dimensional, single-input, single-output system):

Given a transfer function, expand it to reveal all coefficients in both the numerator and denominator. This should result in the following form:

${\begin{aligned}\mathbf {G} (s)&={\frac {n_{1}s^{3}+n_{2}s^{2}+n_{3}s+n_{4}}{s^{4}+d_{1}s^{3}+d_{2}s^{2}+d_{3}s+d_{4}}}\\\\&={\frac {n_{1}s^{-1}+n_{2}s^{-2}+n_{3}s^{-3}+n_{4}s^{-4}}{1+d_{1}s^{-1}+d_{2}s^{-2}+d_{3}s^{-3}+d_{4}s^{-4}}}\ .\end{aligned}}$

The coefficients can now be inserted directly into the state-space model by the following approach: ${\dot {\mathbf {x} }}(t)={\begin{bmatrix}0&1&0&0\\0&0&1&0\\0&0&0&1\\-d_{4}&-d_{3}&-d_{2}&-d_{1}\end{bmatrix}}\mathbf {x} (t)+{\begin{bmatrix}0\\0\\0\\1\end{bmatrix}}\mathbf {u} (t)$

$\mathbf {y} (t)={\begin{bmatrix}n_{4}&n_{3}&n_{2}&n_{1}\end{bmatrix}}\mathbf {x} (t).$

This state-space realization is called **controllable canonical form** because the resulting model is guaranteed to be controllable (i.e., because the control enters a chain of integrators, it has the ability to move every state).

The transfer function coefficients can also be used to construct another type of canonical form ${\dot {\mathbf {x} }}(t)={\begin{bmatrix}0&0&0&-d_{4}\\1&0&0&-d_{3}\\0&1&0&-d_{2}\\0&0&1&-d_{1}\end{bmatrix}}\mathbf {x} (t)+{\begin{bmatrix}n_{4}\\n_{3}\\n_{2}\\n_{1}\end{bmatrix}}\mathbf {u} (t)$ $\mathbf {y} (t)={\begin{bmatrix}0&0&0&1\end{bmatrix}}\mathbf {x} (t).$

This state-space realization is called **observable canonical form** because the resulting model is guaranteed to be observable (i.e., because the output exits from a chain of integrators, every state has an effect on the output).

### Proper transfer functions

Transfer functions which are only proper (and not strictly proper) can also be realised quite easily. The trick here is to separate the transfer function into two parts: a strictly proper part and a constant. $\mathbf {G} (s)=\mathbf {G} _{\mathrm {SP} }(s)+\mathbf {G} (\infty ).$

The strictly proper transfer function can then be transformed into a canonical state-space realization using techniques shown above. The state-space realization of the constant is trivially $\mathbf {y} (t)=\mathbf {G} (\infty )\mathbf {u} (t)$ . Together we then get a state-space realization with matrices *A*, *B* and *C* determined by the strictly proper part, and matrix *D* determined by the constant.

Here is an example to clear things up a bit: $\mathbf {G} (s)={\frac {s^{2}+3s+3}{s^{2}+2s+1}}={\frac {s+2}{s^{2}+2s+1}}+1$ which yields the following controllable realization ${\dot {\mathbf {x} }}(t)={\begin{bmatrix}-2&-1\\1&0\\\end{bmatrix}}\mathbf {x} (t)+{\begin{bmatrix}1\\0\end{bmatrix}}\mathbf {u} (t)$ $\mathbf {y} (t)={\begin{bmatrix}1&2\end{bmatrix}}\mathbf {x} (t)+{\begin{bmatrix}1\end{bmatrix}}\mathbf {u} (t)$ Notice how the output also depends directly on the input. This is due to the $\mathbf {G} (\infty )$ constant in the transfer function.

A common method for feedback is to multiply the output by a matrix *K* and setting this as the input to the system: $\mathbf {u} (t)=K\mathbf {y} (t)$ . Since the values of *K* are unrestricted the values can easily be negated for negative feedback. The presence of a negative sign (the common notation) is merely a notational one and its absence has no impact on the end results.

${\dot {\mathbf {x} }}(t)=A\mathbf {x} (t)+B\mathbf {u} (t)$ $\mathbf {y} (t)=C\mathbf {x} (t)+D\mathbf {u} (t)$

becomes

${\dot {\mathbf {x} }}(t)=A\mathbf {x} (t)+BK\mathbf {y} (t)$ $\mathbf {y} (t)=C\mathbf {x} (t)+DK\mathbf {y} (t)$

solving the output equation for $\mathbf {y} (t)$ and substituting in the state equation results in

${\dot {\mathbf {x} }}(t)=\left(A+BK\left(I-DK\right)^{-1}C\right)\mathbf {x} (t)$ $\mathbf {y} (t)=\left(I-DK\right)^{-1}C\mathbf {x} (t)$

The advantage of this is that the eigenvalues of *A* can be controlled by setting *K* appropriately through eigendecomposition of $\left(A+BK\left(I-DK\right)^{-1}C\right)$ . This assumes that the closed-loop system is controllable or that the unstable eigenvalues of *A* can be made stable through appropriate choice of *K*.

#### Example

For a strictly proper system *D* equals zero. Another fairly common situation is when all states are outputs, i.e. *y* = *x*, which yields *C* = *I*, the identity matrix. This would then result in the simpler equations

${\dot {\mathbf {x} }}(t)=\left(A+BK\right)\mathbf {x} (t)$ $\mathbf {y} (t)=\mathbf {x} (t)$

This reduces the necessary eigendecomposition to just $A+BK$ .

In addition to feedback, an input, $r(t)$ , can be added such that $\mathbf {u} (t)=-K\mathbf {y} (t)+\mathbf {r} (t)$ .

${\dot {\mathbf {x} }}(t)=A\mathbf {x} (t)+B\mathbf {u} (t)$ $\mathbf {y} (t)=C\mathbf {x} (t)+D\mathbf {u} (t)$

becomes

${\dot {\mathbf {x} }}(t)=A\mathbf {x} (t)-BK\mathbf {y} (t)+B\mathbf {r} (t)$ $\mathbf {y} (t)=C\mathbf {x} (t)-DK\mathbf {y} (t)+D\mathbf {r} (t)$

solving the output equation for $\mathbf {y} (t)$ and substituting in the state equation results in

${\dot {\mathbf {x} }}(t)=\left(A-BK\left(I+DK\right)^{-1}C\right)\mathbf {x} (t)+B\left(I-K\left(I+DK\right)^{-1}D\right)\mathbf {r} (t)$ $\mathbf {y} (t)=\left(I+DK\right)^{-1}C\mathbf {x} (t)+\left(I+DK\right)^{-1}D\mathbf {r} (t)$

One fairly common simplification to this system is removing *D*, which reduces the equations to

${\dot {\mathbf {x} }}(t)=\left(A-BKC\right)\mathbf {x} (t)+B\mathbf {r} (t)$ $\mathbf {y} (t)=C\mathbf {x} (t)$

### Moving object example

A classical linear system is that of one-dimensional movement of an object (e.g., a cart). Newton's laws of motion for an object moving horizontally on a plane and attached to a wall with a spring:

$m{\ddot {y}}(t)=u(t)-b{\dot {y}}(t)-ky(t)$

where

- $y(t)$ is position; ${\dot {y}}(t)$ is velocity; ${\ddot {y}}(t)$ is acceleration
- $u(t)$ is an applied force
- b is the viscous friction coefficient
- k is the spring constant
- m is the mass of the object

The state equation would then become

${\begin{bmatrix}{\dot {\mathbf {x} }}_{1}(t)\\{\dot {\mathbf {x} }}_{2}(t)\end{bmatrix}}={\begin{bmatrix}0&1\\-{\frac {k}{m}}&-{\frac {b}{m}}\end{bmatrix}}{\begin{bmatrix}\mathbf {x} _{1}(t)\\\mathbf {x} _{2}(t)\end{bmatrix}}+{\begin{bmatrix}0\\{\frac {1}{m}}\end{bmatrix}}\mathbf {u} (t)$ $\mathbf {y} (t)=\left[{\begin{matrix}1&0\end{matrix}}\right]\left[{\begin{matrix}\mathbf {x_{1}} (t)\\\mathbf {x_{2}} (t)\end{matrix}}\right]$

where

- $x_{1}(t)$ represents the position of the object
- $x_{2}(t)={\dot {x}}_{1}(t)$ is the velocity of the object
- ${\dot {x}}_{2}(t)={\ddot {x}}_{1}(t)$ is the acceleration of the object
- the output $\mathbf {y} (t)$ is the position of the object

The controllability test is then

${\begin{bmatrix}B&AB\end{bmatrix}}={\begin{bmatrix}{\begin{bmatrix}0\\{\frac {1}{m}}\end{bmatrix}}&{\begin{bmatrix}0&1\\-{\frac {k}{m}}&-{\frac {b}{m}}\end{bmatrix}}{\begin{bmatrix}0\\{\frac {1}{m}}\end{bmatrix}}\end{bmatrix}}={\begin{bmatrix}0&{\frac {1}{m}}\\{\frac {1}{m}}&-{\frac {b}{m^{2}}}\end{bmatrix}}$

which has full rank for all b and m . This means, that if initial state of the system is known ( $y(t)$ , ${\dot {y}}(t)$ , ${\ddot {y}}(t)$ ), and if the b and m are constants, then there is a force u that could move the cart into any other position in the system.

The observability test is then

${\begin{bmatrix}C\\CA\end{bmatrix}}={\begin{bmatrix}{\begin{bmatrix}1&0\end{bmatrix}}\\{\begin{bmatrix}1&0\end{bmatrix}}{\begin{bmatrix}0&1\\-{\frac {k}{m}}&-{\frac {b}{m}}\end{bmatrix}}\end{bmatrix}}={\begin{bmatrix}1&0\\0&1\end{bmatrix}}$

which also has full rank. Therefore, this system is both controllable and observable.

## Nonlinear systems

The more general form of a state-space model can be written as two functions.

${\dot {\mathbf {x} }}(t)=\mathbf {f} (t,x(t),u(t))$ $\mathbf {y} (t)=\mathbf {h} (t,x(t),u(t))$

The first is the state equation and the latter is the output equation. If the function $f(\cdot ,\cdot ,\cdot )$ is a linear combination of states and inputs then the equations can be written in matrix notation like above. The $u(t)$ argument to the functions can be dropped if the system is unforced (i.e., it has no inputs).

### Pendulum example

A classic nonlinear system is a simple unforced pendulum

$m\ell ^{2}{\ddot {\theta }}(t)=-m\ell g\sin \theta (t)-k\ell {\dot {\theta }}(t)$

where

- $\theta (t)$ is the angle of the pendulum with respect to the direction of gravity
- m is the mass of the pendulum (pendulum rod's mass is assumed to be zero)
- g is the gravitational acceleration
- k is coefficient of friction at the pivot point
- $\ell$ is the radius of the pendulum (to the center of gravity of the mass m )

The state equations are then

${\dot {x}}_{1}(t)=x_{2}(t)$ ${\dot {x}}_{2}(t)=-{\frac {g}{\ell }}\sin {x_{1}}(t)-{\frac {k}{m\ell }}{x_{2}}(t)$

where

- $x_{1}(t)=\theta (t)$ is the angle of the pendulum
- $x_{2}(t)={\dot {x}}_{1}(t)$ is the rotational velocity of the pendulum
- ${\dot {x}}_{2}={\ddot {x}}_{1}$ is the rotational acceleration of the pendulum

Instead, the state equation can be written in the general form

${\dot {\mathbf {x} }}(t)={\begin{bmatrix}{\dot {x}}_{1}(t)\\{\dot {x}}_{2}(t)\end{bmatrix}}=\mathbf {f} (t,x(t))={\begin{bmatrix}x_{2}(t)\\-{\frac {g}{\ell }}\sin {x_{1}}(t)-{\frac {k}{m\ell }}{x_{2}}(t)\end{bmatrix}}.$

The equilibrium/stationary points of a system are when ${\dot {x}}=0$ and so the equilibrium points of a pendulum are those that satisfy

${\begin{bmatrix}x_{1}\\x_{2}\end{bmatrix}}={\begin{bmatrix}n\pi \\0\end{bmatrix}}$

for integers *n*.
