---
title: "Dynamical system (part 2/2)"
source: https://en.wikipedia.org/wiki/Dynamical_system
domain: dynamical-systems-math
license: CC-BY-SA-4.0
tags: dynamical system, phase space, bifurcation theory, lyapunov stability
fetched: 2026-07-02
part: 2/2
---

## Linear dynamical systems

Linear dynamical systems are at the heart of any system engineering and system theory curriculum. Historically linear systems up to the 1970s reflected most of system theory as a whole (i.e. before the widespread availability of computers). They include the basic features of any dynamical system, such as attenuation saturation and oscillation, and at least locally they can approximate also any non linear systems.

Linear dynamical systems can be solved in terms of simple functions such as exponentials and simple trigonometric functions (i.e. complex exponentials), and the behavior of all orbits can be classified.

In a linear system the phase space is the *N*-dimensional Euclidean space, so any point in phase space can be represented by a vector with *N* numbers. N dimensional Linear dynamical systems are also not chaotic

The analysis of linear systems is also simplified and possible because they satisfy a superposition principle: if *u*(*t*) and *w*(*t*) satisfy a linear differential equation that describe a system, then so will a linear combination $\alpha u(t)+\beta w(t)$ . With superposition is possible to generate new solutions from known ones, therefore is just necessary to classify the fundamental solutions to know all of them.

### Flows

For a flow, the vector field v(*x*) is an affine function of the position in the phase space, that is, ${\dot {x}}=v(x)=Ax+b,$ with *A* a matrix, *b* a vector of numbers and *x* the position vector. The solution to this system can be found by using the superposition principle (linearity). The case *b* ≠ 0 with *A* = 0 is just a straight line in the direction of *b*: $\Phi ^{t}(x_{1})=x_{1}+bt.$

When *b* is zero and *A* ≠ 0 the origin is an equilibrium (or singular) point of the flow, that is, if *x*0 = 0, then the orbit remains there. For other initial conditions, the equation of motion is given by the exponential of a matrix: for an initial point *x*0, $\Phi ^{t}(x_{0})=e^{tA}x_{0}.$

When *b* = 0, the eigenvalues of *A* determine the structure of the phase space. From the eigenvalues and the eigenvectors of *A* it is possible to determine if an initial point will converge or diverge to the equilibrium point at the origin.

The distance between two different initial conditions in the case *A* ≠ 0 will change exponentially in most cases, either converging exponentially fast towards a point, or diverging exponentially fast. Linear systems display sensitive dependence on initial conditions in the case of divergence. For nonlinear systems this is one of the (necessary but not sufficient) conditions for chaotic behavior.

### Maps

A discrete-time, affine dynamical system has the form of a matrix difference equation: $x_{n+1}=Ax_{n}+b,$ with *A* a matrix and *b* a vector. As in the continuous case, the change of coordinates *x* → *x* + (1 − *A*) –1*b* removes the term *b* from the equation. In the new coordinate system, the origin is a fixed point of the map and the solutions are of the linear system *A* *n**x*0. The solutions for the map are no longer curves, but points that hop in the phase space. The orbits are organized in curves, or fibers, which are collections of points that map into themselves under the action of the map.

As in the continuous case, the eigenvalues and eigenvectors of *A* determine the structure of phase space. For example, if *u*1 is an eigenvector of *A*, with a real eigenvalue smaller than one, then the straight lines given by the points along *α* *u*1, with *α* ∈ **R**, is an invariant curve of the map. Points in this straight line run into the fixed point.

There are also many other discrete dynamical systems such as Chaotic maps.

### Local dynamics

The qualitative properties of dynamical systems do not change under a smooth change of coordinates (this is sometimes taken as a definition of qualitative): a *singular point* of the vector field (a point where *v*(*x*) = 0) will remain a singular point under smooth transformations; a *periodic orbit* is a loop in phase space and smooth deformations of the phase space cannot alter it being a loop. It is in the neighborhood of singular points and periodic orbits that the structure of a phase space of a dynamical system can be well understood. In the qualitative study of dynamical systems, the approach is to show that there is a change of coordinates (usually unspecified, but computable) that makes the dynamical system as simple as possible.

### Rectification

A flow in most small patches of the phase space can be made very simple. If *y* is a point where the vector field *v*(*y*) ≠ 0, then there is a change of coordinates for a region around *y* where the vector field becomes a series of parallel vectors of the same magnitude. This is known as the rectification theorem.

The *rectification theorem* says that away from singular points the dynamics of a point in a small patch is a straight line. The patch can sometimes be enlarged by stitching several patches together, and when this works out in the whole phase space *M* the dynamical system is *integrable*. In most cases the patch cannot be extended to the entire phase space. There may be singular points in the vector field (where *v*(*x*) = 0); or the patches may become smaller and smaller as some point is approached. The more subtle reason is a global constraint, where the trajectory starts out in a patch, and after visiting a series of other patches comes back to the original one. If the next time the orbit loops around phase space in a different way, then it is impossible to rectify the vector field in the whole series of patches.

### Near periodic orbits

In general, in the neighborhood of a periodic orbit the rectification theorem cannot be used. Poincaré developed an approach that transforms the analysis near a periodic orbit to the analysis of a map. Pick a point *x*0 in the orbit γ and consider the points in phase space in that neighborhood that are perpendicular to *v*(*x*0). These points are a Poincaré section *S*(*γ*, *x*0), of the orbit. The flow now defines a map, the Poincaré map *F* : *S* → *S*, for points starting in *S* and returning to *S*. Not all these points will take the same amount of time to come back, but the times will be close to the time it takes *x*0.

The intersection of the periodic orbit with the Poincaré section is a fixed point of the Poincaré map *F*. By a translation, the point can be assumed to be at *x* = 0. The Taylor series of the map is *F*(*x*) = *J* · *x* + O(*x*2), so a change of coordinates *h* can only be expected to simplify *F* to its linear part $h^{-1}\circ F\circ h(x)=J\cdot x.$

This is known as the conjugation equation. Finding conditions for this equation to hold has been one of the major tasks of research in dynamical systems. Poincaré first approached it assuming all functions to be analytic and in the process discovered the non-resonant condition. If *λ*1, ..., *λ**ν* are the eigenvalues of *J* they will be resonant if one eigenvalue is an integer linear combination of two or more of the others. As terms of the form *λ**i* – Σ (multiples of other eigenvalues) occurs in the denominator of the terms for the function *h*, the non-resonant condition is also known as the small divisor problem.

### Conjugation results

The results on the existence of a solution to the conjugation equation depend on the eigenvalues of *J* and the degree of smoothness required from *h*. As *J* does not need to have any special symmetries, its eigenvalues will typically be complex numbers. When the eigenvalues of *J* are not in the unit circle, the dynamics near the fixed point *x*0 of *F* is called *hyperbolic* and when the eigenvalues are on the unit circle and complex, the dynamics is called *elliptic*.

In the hyperbolic case, the Hartman–Grobman theorem gives the conditions for the existence of a continuous function that maps the neighborhood of the fixed point of the map to the linear map *J* · *x*. The hyperbolic case is also *structurally stable*. Small changes in the vector field will only produce small changes in the Poincaré map and these small changes will reflect in small changes in the position of the eigenvalues of *J* in the complex plane, implying that the map is still hyperbolic.

The Kolmogorov–Arnold–Moser (KAM) theorem gives the behavior near an elliptic point.


## Bifurcation theory

When the evolution map Φ*t* (or the vector field it is derived from) depends on a parameter μ, the structure of the phase space will also depend on this parameter. Small changes may produce no qualitative changes in the phase space until a special value *μ*0 is reached. At this point the phase space changes qualitatively and the dynamical system is said to have gone through a bifurcation.

Bifurcation theory considers a structure in phase space (typically a fixed point, a periodic orbit, or an invariant torus) and studies its behavior as a function of the parameter *μ*. At the bifurcation point the structure may change its stability, split into new structures, or merge with other structures. By using Taylor series approximations of the maps and an understanding of the differences that may be eliminated by a change of coordinates, it is possible to catalog the bifurcations of dynamical systems.

The bifurcations of a hyperbolic fixed point *x*0 of a system family *Fμ* can be characterized by the eigenvalues of the first derivative of the system *DF**μ*(*x*0) computed at the bifurcation point. For a map, the bifurcation will occur when there are eigenvalues of *DFμ* on the unit circle. For a flow, it will occur when there are eigenvalues on the imaginary axis. For more information, see the main article on Bifurcation theory.

Some bifurcations can lead to very complicated structures in phase space. For example, the Ruelle–Takens scenario describes how a periodic orbit bifurcates into a torus and the torus into a strange attractor. In another example, Feigenbaum period-doubling describes how a stable periodic orbit goes through a series of period-doubling bifurcations.


## Ergodic systems

In many dynamical systems, it is possible to choose the coordinates of the system so that the volume (really a ν-dimensional volume) in phase space is invariant. This happens for mechanical systems derived from Newton's laws as long as the coordinates are the position and the momentum and the volume is measured in units of (position) × (momentum). The flow takes points of a subset *A* into the points Φ *t*(*A*) and invariance of the phase space means that $\mathrm {vol} (A)=\mathrm {vol} (\Phi ^{t}(A)).$ In the Hamiltonian formalism, given a coordinate it is possible to derive the appropriate (generalized) momentum such that the associated volume is preserved by the flow. The volume is said to be computed by the Liouville measure.

In a Hamiltonian system, not all possible configurations of position and momentum can be reached from an initial condition. Because of energy conservation, only the states with the same energy as the initial condition are accessible. The states with the same energy form an energy shell Ω, a sub-manifold of the phase space. The volume of the energy shell, computed using the Liouville measure, is preserved under evolution.

For systems where the volume is preserved by the flow, Poincaré discovered the recurrence theorem: Assume the phase space has a finite Liouville volume and let *F* be a phase space volume-preserving map and *A* a subset of the phase space. Then almost every point of *A* returns to *A* infinitely often. The Poincaré recurrence theorem was used by Zermelo to object to Boltzmann's derivation of the increase in entropy in a dynamical system of colliding atoms.

One of the questions raised by Boltzmann's work was the possible equality between time averages and space averages, what he called the ergodic hypothesis. The hypothesis states that the length of time a typical trajectory spends in a region *A* is vol(*A*)/vol(Ω).

The ergodic hypothesis turned out not to be the essential property needed for the development of statistical mechanics and a series of other ergodic-like properties were introduced to capture the relevant aspects of physical systems. Koopman approached the study of ergodic systems by the use of functional analysis. An observable *a* is a function that to each point of the phase space associates a number (say instantaneous pressure, or average height). The value of an observable can be computed at another time by using the evolution function φ t. This introduces an operator *U* *t*, the transfer operator, $(U^{t}a)(x)=a(\Phi ^{-t}(x)).$

By studying the spectral properties of the linear operator *U* it becomes possible to classify the ergodic properties of Φ *t*. In using the Koopman approach of considering the action of the flow on an observable function, the finite-dimensional nonlinear problem involving Φ *t* gets mapped into an infinite-dimensional linear problem involving *U*.

The Liouville measure restricted to the energy surface Ω is the basis for the averages computed in equilibrium statistical mechanics. An average in time along a trajectory is equivalent to an average in space computed with the Boltzmann factor exp(−β*H*). This idea has been generalized by Sinai, Bowen, and Ruelle (SRB) to a larger class of dynamical systems that includes dissipative systems. SRB measures replace the Boltzmann factor and they are defined on attractors of chaotic systems.


## Nonlinear dynamical systems and chaos

### Chaotic systems

Simple nonlinear dynamical systems, including piecewise linear systems, can exhibit strongly unpredictable behavior, which might seem to be random, despite the fact that they are fundamentally deterministic. This unpredictable behavior has been called *chaos*. Hyperbolic systems are precisely defined dynamical systems that exhibit the properties ascribed to chaotic systems. In hyperbolic systems the tangent spaces perpendicular to an orbit can be decomposed into a combination of two parts: one with the points that converge towards the orbit (the *stable manifold*) and another of the points that diverge from the orbit (the *unstable manifold*).

This branch of mathematics deals with the long-term qualitative behavior of dynamical systems. Here, the focus is not on finding precise solutions to the equations defining the dynamical system (which is often hopeless), but rather to answer questions like "Will the system settle down to a steady state in the long term, and if so, what are the possible attractors?" or "Does the long-term behavior of the system depend on its initial condition?"

The chaotic behavior of complex systems is not the issue. Meteorology has been known for years to involve complex—even chaotic—behavior. Chaos theory has been so surprising because chaos can be found within almost trivial systems. The Pomeau–Manneville scenario of the logistic map and the Fermi–Pasta–Ulam–Tsingou problem arose with just second-degree polynomials; the horseshoe map is piecewise linear.

### Solutions of finite duration

For non-linear autonomous ODEs it is possible under some conditions to develop solutions of finite duration, meaning here that in these solutions the system will reach the value zero at some time, called an ending time, and then stay there forever after. This can occur only when system trajectories are not uniquely determined forwards and backwards in time by the dynamics, thus solutions of finite duration imply a form of "backwards-in-time unpredictability" closely related to the forwards-in-time unpredictability of chaos. This behavior cannot happen for Lipschitz continuous differential equations according to the proof of the Picard-Lindelof theorem. These solutions are non-Lipschitz functions at their ending times and cannot be analytical functions on the whole real line.

As example, the equation: $y'=-{\text{sgn}}(y){\sqrt {|y|}},\,\,y(0)=1$ Admits the finite duration solution: $y(t)={\frac {1}{4}}\left(1-{\frac {t}{2}}+\left|1-{\frac {t}{2}}\right|\right)^{2}$ that is zero for $t\geq 2$ and is not Lipschitz continuous at its ending time $t=2.$


## Algebraic dynamical system

Algebraic dynamical systems can be considered as a special algebraic case of the classical geometric definition. This is based on an algebraic time evolution map as the group action or implicitly as a system of algebraic equations instead of ODEs. From a measure theoretic perspective, the manifold is a measure space, a variety, an algebraic group, and a topological group: the focus is then on symmetries, and ergodic theory behavior. These systems are often studied with methods from abstract algebra, algebraic geometry and Galois theory.

In the context of Algebraic quantum field theory the measure space can be a C*-algebra, namely observables are not just algebras of functions but an operator algebra, and this is treated together with a global gauge group (i.e. a group of constraints that leaves the observable invariant).

In the context of machine learning the neural network itself (e.g. Recursive neural network, diffusion models) can be treated as a set of algebraic equations (often these are finite approximations such as gradient descent, there is a concept of time step, evolution dynamics across the network, and eventually there is a separate set of algebraic constraints such as enforcing unwanted behaviors.

In the context of geometry and number theory, typically one studies the iterations of a rational map over specific number fields, this area is called Algebraic Dynamics, it studies things such as the rational points of algebraic curves, and is deeply connected to Arithmetic dynamics

One such examples is the Poncelet map, where a point is moving in successive steps between two given conics, and the equations are algebraic (i.e. tangents and intersections). Another example can be a billiard with a border that is an algebraic curve, such as an elliptic billiard, in this case the dynamics is defined by reflections.

Note that algebraic curves are differentiable almost every where (a part from a finite number of points), therefore one can study them with analytic methods. In these two examples, the continuous dynamics is piecewise linear, the important events are typically discrete, albeit may be still an infinite or even measurable set (such as an ergodic trajectory in the billiard), the important events are when an algebraic equation applies (such as a reflection on a border). These systems can therefore be studied as discrete dynamical systems too.


## Effective Dynamics

Effective dynamics is the coarse-graining of equations of motion that describe a system at a certain scale, or a specific behaviour, typically getting rid of certain degrees of freedom. Instead of solving the microstate, i.e. the exact interactions for all atoms, molecules, or neural network nodes, effective dynamics models an "effective" force, energy or set of parameters and equations that describe the aggregate effect.

Typically effective dynamics arises from simplifying or specializing complex non linear phenomena, a major way to achieve this is with ensemble averages and this links it deeply with Ergodic theory and the Renormalization group. Key aspect of effective dynamics is the concept of emergence, such as: linear behaviour emergence from non linear equations as in solitons or linear emergence from ensemble averages, emergence of order and degrees of freedom in phase transitions such as in the Landau theory, emergence of prime number patterns in percolation dynamics.

Examples of these approaches are Effective Field Theories,Reynolds Averaged Navier-Stokes (RANS), disordered quantum systems, thermodynamics and Phase transitions.


## Category theory for dynamical systems

In the period between 2000 and 2020, category theory has been applied to system theory (e.g. to open systems and subsystems) and to dynamical systems. The motivation is to study common properties across dynamical systems, topological dynamical systems (i.e. with compact state space), and measure preserving dynamical systems (e.g. hamiltonian systems). It is also possible to draw an analogy between group representation theory (such as irreducible representations) and ergodic decomposition i.e. that every invariant (i.e. conservative) measure is a mixture of ergodic ones, in an analogous fashion to the central limit theorem. Ultimately this can be compared to the fundamental theorem of arithmetic and to prime number decomposition.
