---
title: "Lyapunov exponent"
source: https://en.wikipedia.org/wiki/Lyapunov_exponent
domain: chaos-theory
license: CC-BY-SA-4.0
tags: chaos theory, butterfly effect, lyapunov exponent, strange attractor
fetched: 2026-07-02
---

# Lyapunov exponent

Explanations of the Lyapunov exponent

In mathematics, the **Lyapunov exponent** or **Lyapunov characteristic exponent** of a dynamical system is a quantity that characterizes the exponential rate of separation of infinitesimally close trajectories. Quantitatively, two trajectories in phase space with initial separation vector ${\boldsymbol {\delta }}_{0}$ diverge (provided that the divergence can be treated within the linearized approximation) at a rate given by

$|{\boldsymbol {\delta }}(t)|\approx e^{\lambda t}|{\boldsymbol {\delta }}_{0}|$

where $\lambda$ is the Lyapunov exponent.

The rate of separation can be different for different orientations of initial separation vector. Thus, there is a **spectrum of Lyapunov exponents**—equal in number to the dimensionality of the phase space. It is common to refer to the largest one as the **maximal Lyapunov exponent** (MLE), because it determines a notion of predictability for a dynamical system. A positive MLE is usually taken as an indication that the system is chaotic (provided some other conditions are met, e.g., phase space compactness). This is because for the MLE to be more than 0, the average derivative needs to be more than 1, since we find its logarithms. If the average derivatives are above 1, it means that the function grows exponentially, which makes it so that any small change between initial values increase from their original value, so the function is divergent. If it is less than 0, it means that the average derivative is less than 1, which means that the function is decreasing, which would make any changes in the initial values decrease over time, making the function convergent. Note that an arbitrary initial separation vector will typically contain some component in the direction associated with the MLE, and because of the exponential growth rate, the effect of the other exponents will diminish over time.

The exponent is named after Aleksandr Lyapunov.

## Definition of the maximal Lyapunov exponent

The maximal Lyapunov exponent can be defined as follows: $\lambda =\lim _{t\to \infty }\lim _{|{\boldsymbol {\delta }}_{0}|\to 0}{\frac {1}{t}}\ln {\frac {|{\boldsymbol {\delta }}(t)|}{|{\boldsymbol {\delta }}_{0}|}}$

The limit $|{\boldsymbol {\delta }}_{0}|\to 0$ ensures the validity of the linear approximation at any time.

For discrete time system (maps or fixed point iterations) $x_{n+1}=f(x_{n})$ , for an orbit starting with $x_{0}$ this translates into: $\lambda (x_{0})=\lim _{n\to \infty }{\frac {1}{n}}\sum _{i=0}^{n-1}\ln |f'(x_{i})|$

## Definition of the Lyapunov spectrum

For a dynamical system with evolution equation ${\dot {x}}_{i}=f_{i}(x)$ in an *n*–dimensional phase space, the spectrum of Lyapunov exponents $\{\lambda _{1},\lambda _{2},\ldots ,\lambda _{n}\}\,,$ in general, depends on the starting point $x_{0}$ . However, we will usually be interested in the attractor (or attractors) of a dynamical system, and there will normally be one set of exponents associated with each attractor. The choice of starting point may determine which attractor the system ends up on, if there is more than one. (For Hamiltonian systems, which do not have attractors, this is not a concern.) The Lyapunov exponents describe the behavior of vectors in the tangent space of the phase space and are defined from the Jacobian matrix $J_{ij}(t)=\left.{\frac {df_{i}(x)}{dx_{j}}}\right|_{x(t)}$ this Jacobian defines the evolution of the tangent vectors, given by the matrix Y , via the equation ${\dot {Y}}=JY$ with the initial condition $Y_{ij}(0)=\delta _{ij}$ . The matrix Y describes how a small change at the point $x(0)$ propagates to the final point $x(t)$ . The limit $\Lambda =\lim _{t\rightarrow \infty }{\frac {1}{2t}}\log(Y(t)Y^{T}(t))$ defines a matrix $\Lambda$ (the conditions for the existence of the limit are given by the Oseledets theorem). The Lyapunov exponents $\lambda _{i}$ are defined by the eigenvalues of $\Lambda$ .

The set of Lyapunov exponents will be the same for almost all starting points of an ergodic component of the dynamical system.

## Lyapunov exponent for time-varying linearization

To introduce Lyapunov exponent consider a fundamental matrix $X(t)$ (e.g., for linearization along a stationary solution $x_{0}$ in a continuous system), the fundamental matrix is $\exp \left(\left.{\frac {df^{t}(x)}{dx}}\right|_{x_{0}}t\right)$ consisting of the linearly-independent solutions of the first-order approximation of the system. The singular values $\{\alpha _{j}{\big (}X(t){\big )}\}_{1}^{n}$ of the matrix $X(t)$ are the square roots of the eigenvalues of the matrix $X(t)^{*}X(t)$ . The largest Lyapunov exponent $\lambda _{\mathrm {max} }$ is as follows $\lambda _{\mathrm {max} }=\max \limits _{j}\limsup _{t\rightarrow \infty }{\frac {1}{t}}\ln \alpha _{j}{\big (}X(t){\big )}.$ Lyapunov proved that if the system of the first approximation is regular (e.g., all systems with constant and periodic coefficients are regular) and its largest Lyapunov exponent is negative, then the solution of the original system is asymptotically Lyapunov stable. Later, it was stated by O. Perron that the requirement of regularity of the first approximation is substantial.

### Perron effects of largest Lyapunov exponent sign inversion

In 1930 O. Perron constructed an example of a second-order system, where the first approximation has negative Lyapunov exponents along a zero solution of the original system but, at the same time, this zero solution of the original nonlinear system is Lyapunov unstable. Furthermore, in a certain neighborhood of this zero solution almost all solutions of the original system have positive Lyapunov exponents. Also, it is possible to construct a reverse example in which the first approximation has positive Lyapunov exponents along a zero solution of the original system but, at the same time, this zero solution of original nonlinear system is Lyapunov stable. The effect of sign inversion of Lyapunov exponents of solutions of the original system and the system of first approximation with the same initial data was subsequently called the Perron effect.

Perron's counterexample shows that a negative largest Lyapunov exponent does not, in general, indicate stability, and that a positive largest Lyapunov exponent does not, in general, indicate chaos.

Therefore, time-varying linearization requires additional justification.

## Basic properties

If the system is conservative (i.e., there is no dissipation), a volume element of the phase space will stay the same along a trajectory. Thus the sum of all Lyapunov exponents must be zero. If the system is dissipative, the sum of Lyapunov exponents is negative.

If the system is a flow and the trajectory does not converge to a single point, one exponent is always zero—the Lyapunov exponent corresponding to the eigenvalue of L with an eigenvector in the direction of the flow.

## Significance of the Lyapunov spectrum

The Lyapunov spectrum can be used to give an estimate of the rate of entropy production, of the fractal dimension, and of the Hausdorff dimension of the considered dynamical system. In particular from the knowledge of the Lyapunov spectrum it is possible to obtain the so-called Lyapunov dimension (or Kaplan–Yorke dimension) $D_{KY}$ , which is defined as follows: $D_{KY}=k+\sum _{i=1}^{k}{\frac {\lambda _{i}}{|\lambda _{k+1}|}}$ where k is the maximum integer such that the sum of the k largest exponents is still non-negative. $D_{KY}$ represents an upper bound for the information dimension of the system. Moreover, the sum of all the positive Lyapunov exponents gives an estimate of the Kolmogorov–Sinai entropy accordingly to Pesin's theorem. Along with widely used numerical methods for estimating and computing the Lyapunov dimension there is an effective analytical approach, which is based on the direct Lyapunov method with special Lyapunov-like functions. The Lyapunov exponents of bounded trajectory and the Lyapunov dimension of attractor are invariant under diffeomorphism of the phase space.

The multiplicative inverse of the largest Lyapunov exponent is sometimes referred in literature as Lyapunov time, and defines the characteristic *e*-folding time. For chaotic orbits, the Lyapunov time will be finite, whereas for regular orbits it will be infinite.

## Numerical calculation

Generally the calculation of Lyapunov exponents, as defined above, cannot be carried out analytically, and in most cases one must resort to numerical techniques. An early example, which also constituted the first demonstration of the exponential divergence of chaotic trajectories, was carried out by R. H. Miller in 1964. Currently, the most commonly used numerical procedure estimates the L matrix based on averaging several finite time approximations of the limit defining L .

One of the most used and effective numerical techniques to calculate the Lyapunov spectrum for a smooth dynamical system relies on periodic Gram–Schmidt orthonormalization of the Lyapunov vectors to avoid a misalignment of all the vectors along the direction of maximal expansion. The Lyapunov spectrum of various models are described. Source code is provided for several nonlinear systems, including the Hénon map, the Lorenz system, and a delay differential equation.

Calculating Lyapunov exponents from limited experimental data presents significant challenges. The primary difficulty arises because such data is typically confined to the system's attractor and does not explore the full phase space. This confinement results in a 'singular' dataset with minimal extension along certain directions. These singular directions are precisely those associated with the more negative Lyapunov exponents, making them notoriously difficult to determine accurately.

To address this, one effective technique is to use nonlinear mappings to model the evolution of small displacements from the attractor. This approach can dramatically improve the ability to recover the full Lyapunov spectrum, but it is highly sensitive to noise and requires very clean data to be effective.

## Local Lyapunov exponent

Whereas the (global) Lyapunov exponent gives a measure for the total predictability of a system, it is sometimes of interest to estimate the local predictability around a point *x*0 in phase space. This may be done through the eigenvalues of the Jacobian matrix *J*0(*x*0). These eigenvalues are also called local Lyapunov exponents. Local exponents are not invariant under a nonlinear change of coordinates.

## Conditional Lyapunov exponent

This term is normally used regarding synchronization of chaos, in which there are two systems that are coupled, usually in a unidirectional manner so that there is a drive (or master) system and a response (or slave) system. The conditional exponents are those of the response system with the drive system treated as simply the source of a (chaotic) drive signal. Synchronization occurs when all of the conditional exponents are negative.
