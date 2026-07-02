---
title: "Verlet integration"
source: https://en.wikipedia.org/wiki/Verlet_integration
domain: fixed-timestep
license: CC-BY-SA-4.0
tags: fixed timestep, fixed time step, deterministic simulation step, physics timestep
fetched: 2026-07-02
---

# Verlet integration

**Verlet integration** (French pronunciation: [vɛʁˈlɛ]) is a numerical method used to integrate Newton's equations of motion. It is frequently used to calculate trajectories of particles in molecular dynamics simulations and computer graphics. The algorithm was first used in 1791 by Jean Baptiste Delambre and has been rediscovered many times since then, most recently by Loup Verlet in the 1960s for use in molecular dynamics. It was also used by P. H. Cowell and A. C. C. Crommelin in 1909 to compute the orbit of Halley's Comet, and by Carl Størmer in 1907 to study the trajectories of electrical particles in a magnetic field (hence it is also called **Størmer's method**). The Verlet integrator provides good numerical stability, as well as other properties that are important in physical systems such as time reversibility and preservation of the symplectic form on phase space, at no significant additional computational cost over the simple Euler method.

## Basic Størmer–Verlet

For a second-order differential equation of the type ${\ddot {\mathbf {x} }}(t)=\mathbf {A} {\bigl (}\mathbf {x} (t){\bigr )}$ with initial conditions $\mathbf {x} (t_{0})=\mathbf {x} _{0}$ and ${\dot {\mathbf {x} }}(t_{0})=\mathbf {v} _{0}$ , an approximate numerical solution $\mathbf {x} _{n}\approx \mathbf {x} (t_{n})$ at the times $t_{n}=t_{0}+n\,\Delta t$ with step size $\Delta t>0$ can be obtained by the following method:

1. set ${\textstyle \mathbf {x} _{1}=\mathbf {x} _{0}+\mathbf {v} _{0}\,\Delta t+{\tfrac {1}{2}}\mathbf {A} (\mathbf {x} _{0})\,\Delta t^{2}}$ ,
2. for *n* = 1, 2, ... iterate $\mathbf {x} _{n+1}=2\mathbf {x} _{n}-\mathbf {x} _{n-1}+\mathbf {A} (\mathbf {x} _{n})\,\Delta t^{2}.$

### Equations of motion

Newton's equation of motion for conservative physical systems is ${\boldsymbol {M}}{\ddot {\mathbf {x} }}(t)=F{\bigl (}\mathbf {x} (t){\bigr )}=-\nabla V{\bigl (}\mathbf {x} (t){\bigr )},$ or individually $m_{k}{\ddot {\mathbf {x} }}_{k}(t)=F_{k}{\bigl (}\mathbf {x} (t){\bigr )}=-\nabla _{\mathbf {x} _{k}}V{\left(\mathbf {x} (t)\right)},$ where

- t is the time,
- $\mathbf {x} (t)={\bigl (}\mathbf {x} _{1}(t),\ldots ,\mathbf {x} _{N}(t){\bigr )}$ is the ensemble of the position vector of N objects,
- V is the scalar potential function,
- F is the negative gradient of the potential, giving the ensemble of forces on the particles,
- ${\boldsymbol {M}}$ is the mass matrix, typically diagonal with blocks with mass $m_{k}$ for every particle.

This equation, for various choices of the potential function V , can be used to describe the evolution of diverse physical systems, from the motion of interacting molecules to the orbit of the planets.

After a transformation to bring the mass to the right side and forgetting the structure of multiple particles, the equation may be simplified to ${\ddot {\mathbf {x} }}(t)=\mathbf {A} {\bigl (}\mathbf {x} (t){\bigr )}$ with some suitable vector-valued function $\mathbf {A} (\mathbf {x} )$ representing the position-dependent acceleration. Typically, an initial position $\mathbf {x} (0)=\mathbf {x} _{0}$ and an initial velocity $\mathbf {v} (0)={\dot {\mathbf {x} }}(0)=\mathbf {v} _{0}$ are also given.

### Verlet integration (without velocities)

To discretize and numerically solve this initial value problem, a time step $\Delta t>0$ is chosen, and the sampling-point sequence $t_{n}=n\,\Delta t$ considered. The task is to construct a sequence of points $\mathbf {x} _{n}$ that closely follow the points $\mathbf {x} (t_{n})$ on the trajectory of the exact solution.

Where Euler's method uses the forward difference approximation to the first derivative in differential equations of order one, Verlet integration can be seen as using the central difference approximation to the second derivative: ${\begin{aligned}{\frac {\Delta ^{2}\mathbf {x} _{n}}{\Delta t^{2}}}&={\frac {{\frac {\mathbf {x} _{n+1}-\mathbf {x} _{n}}{\Delta t}}-{\frac {\mathbf {x} _{n}-\mathbf {x} _{n-1}}{\Delta t}}}{\Delta t}}\\[6pt]&={\frac {\mathbf {x} _{n+1}-2\mathbf {x} _{n}+\mathbf {x} _{n-1}}{\Delta t^{2}}}\\&=\mathbf {a} _{n}=\mathbf {A} (\mathbf {x} _{n}).\end{aligned}}$

*Verlet integration* in the form used as the *Størmer method* uses this equation to obtain the next position vector from the previous two without using the velocity as ${\begin{aligned}\mathbf {x} _{n+1}&=2\mathbf {x} _{n}-\mathbf {x} _{n-1}+\mathbf {a} _{n}\,\Delta t^{2},\\[6pt]\mathbf {a} _{n}&=\mathbf {A} (\mathbf {x} _{n}).\end{aligned}}$

### Discretisation error

The time symmetry inherent in the method reduces the level of local errors introduced into the integration by the discretization by removing all odd-degree terms, here the terms in $\Delta t$ of degree three. The local error is quantified by inserting the exact values $\mathbf {x} (t_{n-1}),\mathbf {x} (t_{n}),\mathbf {x} (t_{n+1})$ into the iteration and computing the Taylor expansions at time $t=t_{n}$ of the position vector $\mathbf {x} (t\pm \Delta t)$ in different time directions: ${\begin{aligned}\mathbf {x} (t{+}\Delta t)&=\mathbf {x} (t)+\mathbf {v} (t)\Delta t+{\frac {\mathbf {a} (t)\Delta t^{2}}{2}}+{\frac {\mathbf {b} (t)\Delta t^{3}}{6}}+{\mathcal {O}}{\left(\Delta t^{4}\right)}\\[1ex]\mathbf {x} (t{-}\Delta t)&=\mathbf {x} (t)-\mathbf {v} (t)\Delta t+{\frac {\mathbf {a} (t)\Delta t^{2}}{2}}-{\frac {\mathbf {b} (t)\Delta t^{3}}{6}}+{\mathcal {O}}{\left(\Delta t^{4}\right)},\end{aligned}}$ where $\mathbf {x}$ is the position, $\mathbf {v} ={\dot {\mathbf {x} }}$ the velocity, $\mathbf {a} ={\ddot {\mathbf {x} }}$ the acceleration, and $\mathbf {b} ={\dot {\mathbf {a} }}={\overset {\dots }{\mathbf {x} }}$ the jerk (third derivative of the position with respect to the time).

Adding these two expansions gives $\mathbf {x} (t{+}\Delta t)=2\mathbf {x} (t)-\mathbf {x} (t{-}\Delta t)+\mathbf {a} (t)\Delta t^{2}+{\mathcal {O}}{\left(\Delta t^{4}\right)}.$ We can see that the first- and third-order terms from the Taylor expansion cancel out, thus making the Verlet integrator an order more accurate than integration by simple Taylor expansion alone.

Caution should be applied to the fact that the acceleration here is computed from the exact solution, $\mathbf {a} (t)=\mathbf {A} {\bigl (}\mathbf {x} (t){\bigr )}$ , whereas in the iteration it is computed at the central iteration point, $\mathbf {a} _{n}=\mathbf {A} (\mathbf {x} _{n})$ . In computing the global error, that is the distance between exact solution and approximation sequence, those two terms do not cancel exactly, influencing the order of the global error.

### A simple example

To gain insight into the relation of local and global errors, it is helpful to examine simple examples where the exact solution, as well as the approximate solution, can be expressed in explicit formulas. The standard example for this task is the exponential function.

Consider the linear differential equation ${\ddot {x}}(t)=w^{2}x(t)$ with a constant w . Its exact basis solutions are $e^{wt}$ and $e^{-wt}$ .

The Størmer method applied to this differential equation leads to a linear recurrence relation $x_{n+1}-2x_{n}+x_{n-1}=h^{2}w^{2}x_{n},$ or $x_{n+1}-2\left(1+{\tfrac {1}{2}}\left(wh\right)^{2}\right)x_{n}+x_{n-1}=0.$ It can be solved by finding the roots of its characteristic polynomial $q^{2}-2\left(1+{\tfrac {1}{2}}(wh)^{2}\right)q+1=0$ . These are $q_{\pm }=1+{\tfrac {1}{2}}\left(wh\right)^{2}\pm wh{\sqrt {1+{\tfrac {1}{4}}\left(wh\right)^{2}}}.$ The basis solutions of the linear recurrence are $x_{n}=q_{+}^{n}$ and $x_{n}=q_{-}^{n}$ . To compare them with the exact solutions, Taylor expansions are computed: ${\begin{aligned}q_{+}&=1+{\tfrac {1}{2}}(wh)^{2}+wh\left(1+{\tfrac {1}{8}}(wh)^{2}-{\tfrac {3}{128}}(wh)^{4}+{\mathcal {O}}{\left(h^{6}\right)}\right)\\&=1+(wh)+{\tfrac {1}{2}}(wh)^{2}+{\tfrac {1}{8}}(wh)^{3}-{\tfrac {3}{128}}(wh)^{5}+{\mathcal {O}}{\left(h^{7}\right)}.\end{aligned}}$ The quotient of this series with the exponential $e^{wh}$ starts with $1-{\tfrac {1}{24}}(wh)^{3}+{\mathcal {O}}{\left(h^{5}\right)}$ , so ${\begin{aligned}q_{+}&=\left(1-{\tfrac {1}{24}}(wh)^{3}+{\mathcal {O}}{\left(h^{5}\right)}\right)e^{wh}\\&=e^{-{\frac {1}{24}}(wh)^{3}+{\mathcal {O}}\left(h^{5}\right)}\,e^{wh}.\end{aligned}}$ From there it follows that for the first basis solution the error can be computed as ${\begin{aligned}x_{n}=q_{+}^{n}&=e^{-{\frac {1}{24}}(wh)^{2}\,wt_{n}+{\mathcal {O}}\left(h^{4}\right)}\,e^{wt_{n}}\\&=e^{wt_{n}}\left(1-{\tfrac {1}{24}}(wh)^{2}\,wt_{n}+{\mathcal {O}}{\left(h^{4}\right)}\right)\\&=e^{wt_{n}}+{\mathcal {O}}{\left(h^{2}t_{n}e^{wt_{n}}\right)}.\end{aligned}}$ That is, although the local discretization error is of order 4, due to the second order of the differential equation the global error is of order 2, with a constant that grows exponentially in time.

### Starting the iteration

Note that at the start of the Verlet iteration at step $n=1$ , time $t=t_{1}=\Delta t$ , computing $\mathbf {x} _{2}$ , one already needs the position vector $\mathbf {x} _{1}$ at time $t=t_{1}$ . At first sight, this could give problems, because the initial conditions are known only at the initial time $t_{0}=0$ . However, from these the acceleration $\mathbf {a} _{0}=\mathbf {A} (\mathbf {x} _{0})$ is known, and a suitable approximation for the position at the first time step can be obtained using the Taylor polynomial of degree two: ${\begin{aligned}\mathbf {x} _{1}&=\mathbf {x} _{0}+\mathbf {v} _{0}\Delta t+{\tfrac {1}{2}}\mathbf {a} _{0}\Delta t^{2}\\&\approx \mathbf {x} (\Delta t)+{\mathcal {O}}{\left(\Delta t^{3}\right)}.\end{aligned}}$

The error on the first time step then is of order ${\mathcal {O}}{\left(\Delta t^{3}\right)}$ . This is not considered a problem because on a simulation over a large number of time steps, the error on the first time step is only a negligibly small amount of the total error, which at time $t_{n}$ is of the order ${\mathcal {O}}{\left(e^{Lt_{n}}\Delta t^{2}\right)}$ , both for the distance of the position vectors $\mathbf {x} _{n}$ to $\mathbf {x} (t_{n})$ as for the distance of the divided differences ${\tfrac {\mathbf {x} _{n+1}-\mathbf {x} _{n}}{\Delta t}}$ to ${\tfrac {\mathbf {x} (t_{n+1})-\mathbf {x} (t_{n})}{\Delta t}}$ . Moreover, to obtain this second-order global error, the initial error needs to be of at least third order.

### Non-constant time differences

A disadvantage of the Størmer–Verlet method is that if the time step ( $\Delta t$ ) changes, the method does not approximate the solution to the differential equation. This can be corrected using the formula $\mathbf {x} _{i+1}=\mathbf {x} _{i}+\left(\mathbf {x} _{i}-\mathbf {x} _{i-1}\right){\frac {\Delta t_{i}}{\Delta t_{i-1}}}+\mathbf {a} _{i}\Delta t_{i}^{2}.$

A more exact derivation uses the Taylor series (to second order) at $t_{i}$ for times $t_{i+1}=t_{i}+\Delta t_{i}$ and $t_{i-1}=t_{i}-\Delta t_{i-1}$ to obtain after elimination of $\mathbf {v} _{i}$ ${\frac {\mathbf {x} _{i+1}-\mathbf {x} _{i}}{\Delta t_{i}}}+{\frac {\mathbf {x} _{i-1}-\mathbf {x} _{i}}{\Delta t_{i-1}}}=\mathbf {a} _{i}\,{\frac {\Delta t_{i}+\Delta t_{i-1}}{2}},$ so that the iteration formula becomes $\mathbf {x} _{i+1}=\mathbf {x} _{i}+(\mathbf {x} _{i}-\mathbf {x} _{i-1}){\frac {\Delta t_{i}}{\Delta t_{i-1}}}+\mathbf {a} _{i}\,{\frac {\Delta t_{i}+\Delta t_{i-1}}{2}}\,\Delta t_{i}.$

### Computing velocities – Størmer–Verlet method

The velocities are not explicitly given in the basic Størmer equation, but often they are necessary for the calculation of certain physical quantities like the kinetic energy. This can create technical challenges in molecular dynamics simulations, because kinetic energy and instantaneous temperatures at time t cannot be calculated for a system until the positions are known at time $t+\Delta t$ . This deficiency can either be dealt with using the velocity Verlet algorithm or by estimating the velocity using the position terms and the mean value theorem: $\mathbf {v} (t)={\frac {\mathbf {x} (t{+}\Delta t)-\mathbf {x} (t{-}\Delta t)}{2\Delta t}}+{\mathcal {O}}{\left(\Delta t^{2}\right)}.$

Note that this velocity term is a step behind the position term, since this is for the velocity at time t , not $t+\Delta t$ , meaning that $\mathbf {v} _{n}={\tfrac {\mathbf {x} _{n+1}-\mathbf {x} _{n-1}}{2\Delta t}}$ is a second-order approximation to $\mathbf {v} (t_{n})$ . With the same argument, but halving the time step, $\mathbf {v} _{n+{\frac {1}{2}}}={\tfrac {\mathbf {x} _{n+1}-\mathbf {x} _{n}}{\Delta t}}$ is a second-order approximation to $\mathbf {v} {\left(t_{n+1/2}\right)}$ , with $t_{n+{\frac {1}{2}}}=t_{n}+{\tfrac {1}{2}}\Delta t$ .

One can shorten the interval to approximate the velocity at time $t+\Delta t$ at the cost of accuracy: $\mathbf {v} (t{+}\Delta t)={\frac {\mathbf {x} (t{+}\Delta t)-\mathbf {x} (t)}{\Delta t}}+{\mathcal {O}}(\Delta t).$

## Velocity Verlet

A related, and more commonly used algorithm is the velocity Verlet algorithm, similar to the leapfrog method, except that the velocity and position are calculated at the same value of the time variable (leapfrog does not, as the name suggests). This uses a similar approach, but explicitly incorporates velocity, solving the problem of the first time step in the basic Verlet algorithm:

${\begin{aligned}\mathbf {x} (t{+}\Delta t)&=\mathbf {x} (t)+\mathbf {v} (t)\,\Delta t+{\tfrac {1}{2}}\,\mathbf {a} (t)\Delta t^{2},\\[6pt]\mathbf {v} (t{+}\Delta t)&=\mathbf {v} (t)+{\frac {\mathbf {a} (t)+\mathbf {a} (t{+}\Delta t)}{2}}\Delta t.\end{aligned}}$

It can be shown that the error in the velocity Verlet is of the same order as in the basic Verlet. Note that the velocity algorithm is not necessarily more memory-consuming, because, in basic Verlet, we keep track of two vectors of position, while in velocity Verlet, we keep track of one vector of position and one vector of velocity. The standard implementation scheme of this algorithm is:

1. Calculate $\mathbf {v} \left(t+{\tfrac {1}{2}}\,\Delta t\right)=\mathbf {v} (t)+{\tfrac {1}{2}}\,\mathbf {a} (t)\,\Delta t$ .
2. Calculate $\mathbf {x} (t+\Delta t)=\mathbf {x} (t)+\mathbf {v} \left(t+{\tfrac {1}{2}}\,\Delta t\right)\,\Delta t$ .
3. Derive $\mathbf {a} (t+\Delta t)$ from the interaction potential using $\mathbf {x} (t+\Delta t)$ .
4. Calculate $\mathbf {v} (t+\Delta t)=\mathbf {v} \left(t+{\tfrac {1}{2}}\,\Delta t\right)+{\tfrac {1}{2}}\,\mathbf {a} (t+\Delta t)\Delta t$ .

This algorithm also works with variable time steps, and is identical to the 'kick-drift-kick' form of leapfrog method integration.

Eliminating the half-step velocity, this algorithm may be shortened to

1. Calculate $\mathbf {x} (t+\Delta t)=\mathbf {x} (t)+\mathbf {v} (t)\,\Delta t+{\tfrac {1}{2}}\,\mathbf {a} (t)\,\Delta t^{2}$ .
2. Derive $\mathbf {a} (t+\Delta t)$ from the interaction potential using $\mathbf {x} (t+\Delta t)$ .
3. Calculate $\mathbf {v} (t+\Delta t)=\mathbf {v} (t)+{\tfrac {1}{2}}\,{\bigl (}\mathbf {a} (t)+\mathbf {a} (t+\Delta t){\bigr )}\Delta t$ .

Note, however, that this algorithm assumes that acceleration $\mathbf {a} (t+\Delta t)$ only depends on position $\mathbf {x} (t+\Delta t)$ and does not depend on velocity $\mathbf {v} (t+\Delta t)$ .

One might note that the long-term results of velocity Verlet, and similarly of leapfrog are one order better than the semi-implicit Euler method. The algorithms are almost identical up to a shift by half a time step in the velocity. This can be proven by rotating the above loop to start at step 3 and then noticing that the acceleration term in step 1 could be eliminated by combining steps 2 and 4. The only difference is that the midpoint velocity in velocity Verlet is considered the final velocity in semi-implicit Euler method.

The global error of all Euler methods is of order one, whereas the global error of this method is, similar to the midpoint method, of order two. Additionally, if the acceleration indeed results from the forces in a conservative mechanical or Hamiltonian system, the energy of the approximation essentially oscillates around the constant energy of the exactly solved system, with a global error bound again of order one for semi-explicit Euler and order two for Verlet-leapfrog. The same goes for all other conserved quantities of the system like linear or angular momentum, that are always preserved or nearly preserved in a symplectic integrator.

The velocity Verlet method is a special case of the Newmark-beta method with $\beta =0$ and ${\textstyle \gamma ={\tfrac {1}{2}}}$ .

### Algorithmic representation

Since **velocity Verlet** is a generally useful algorithm in 3D applications, a solution written in C++ could look like below. This type of position integration will significantly increase accuracy in 3D simulations and games when compared with the regular Euler method.

```mw
struct Body
{
    Vec3d pos { 0.0, 0.0, 0.0 };
    Vec3d vel { 2.0, 0.0, 0.0 }; // 2 m/s along x-axis
    Vec3d acc { 0.0, 0.0, 0.0 }; // no acceleration at first
    double mass = 1.0; // 1kg

    /**
     * Updates pos and vel using "Velocity Verlet" integration
     * @param dt DeltaTime / time step [eg: 0.01]
     */
    void update(double dt)
    {
        Vec3d new_pos = pos + vel*dt + acc*(dt*dt*0.5);
        Vec3d new_acc = apply_forces();
        Vec3d new_vel = vel + (acc+new_acc)*(dt*0.5);
        pos = new_pos;
        vel = new_vel;
        acc = new_acc;
    }

    /**
     * To apply velocity to your objects, calculate the required Force vector instead
     * and apply the accumulated forces here.
     */
    Vec3d apply_forces() const
    {
        Vec3d new_acc = Vec3d{0.0, 0.0, -9.81 }; // 9.81 m/s² down in the z-axis
        // Apply any other forces here...
        // NOTE: Avoid depending on `vel` because Velocity Verlet assumes acceleration depends on position.
        return new_acc;
    }
};
```

## Error terms

The global truncation error of the Verlet method is ${\mathcal {O}}{\left(\Delta t^{2}\right)}$ , both for position and velocity. This is in contrast with the fact that the local error in position is only ${\mathcal {O}}{\left(\Delta t^{4}\right)}$ as described above. The difference is due to the accumulation of the local truncation error over all of the iterations.

The global error can be derived by noting the following:

$\operatorname {error} {\bigl (}x(t_{0}+\Delta t){\bigr )}={\mathcal {O}}{\left(\Delta t^{4}\right)}$

and

$x(t_{0}+2\Delta t)=2x(t_{0}+\Delta t)-x(t_{0})+\Delta t^{2}{\ddot {x}}(t_{0}+\Delta t)+{\mathcal {O}}{\left(\Delta t^{4}\right)}.$

Therefore

$\operatorname {error} {\bigl (}x(t_{0}+2\Delta t){\bigr )}=2\cdot \operatorname {error} {\bigl (}x(t_{0}+\Delta t){\bigr )}+{\mathcal {O}}{\left(\Delta t^{4}\right)}=3\,{\mathcal {O}}{\left(\Delta t^{4}\right)}.$

Similarly:

${\begin{aligned}\operatorname {error} {\bigl (}x(t_{0}+3\Delta t){\bigl )}&=6\,{\mathcal {O}}{\left(\Delta t^{4}\right)},\\[6px]\operatorname {error} {\bigl (}x(t_{0}+4\Delta t){\bigl )}&=10\,{\mathcal {O}}{\left(\Delta t^{4}\right)},\\[6px]\operatorname {error} {\bigl (}x(t_{0}+5\Delta t){\bigl )}&=15\,{\mathcal {O}}{\left(\Delta t^{4}\right)},\end{aligned}}$

which can be generalized to (it can be shown by induction, but it is given here without proof):

$\operatorname {error} {\bigl (}x(t_{0}+n\Delta t){\bigr )}={\frac {n(n+1)}{2}}\,{\mathcal {O}}\left(\Delta t^{4}\right).$

If we consider the global error in position between $x(t)$ and $x(t+T)$ , where $T=n\Delta t$ , it is clear that

$\operatorname {error} {\bigl (}x(t_{0}+T){\bigr )}=\left({\frac {T^{2}}{2\Delta t^{2}}}+{\frac {T}{2\Delta t}}\right){\mathcal {O}}{\left(\Delta t^{4}\right)},$

and therefore, the global (cumulative) error over a constant interval of time is given by

$\operatorname {error} {\bigr (}x(t_{0}+T){\bigl )}={\mathcal {O}}{\left(\Delta t^{2}\right)}.$

Because the velocity is determined in a non-cumulative way from the positions in the Verlet integrator, the global error in velocity is also ${\mathcal {O}}{\left(\Delta t^{2}\right)}$ .

In molecular dynamics simulations, the global error is typically far more important than the local error, and the Verlet integrator is therefore known as a second-order integrator.

## Constraints

Systems of multiple particles with constraints are simpler to solve with Verlet integration than with Euler methods. Constraints between points may be, for example, potentials constraining them to a specific distance or attractive forces. They may be modeled as springs connecting the particles. Using springs of infinite stiffness, the model may then be solved with a Verlet algorithm.

In one dimension, the relationship between the unconstrained positions ${\tilde {x}}_{i}^{(t)}$ and the actual positions $x_{i}^{(t)}$ of points i at time t , given a desired constraint distance of r , can be found with the algorithm

${\begin{aligned}d_{1}&=x_{2}^{(t)}-x_{1}^{(t)},\\[6px]d_{2}&=\|d_{1}\|,\\[6px]d_{3}&={\frac {d_{2}-r}{d_{2}}},\\[6px]x_{1}^{(t+\Delta t)}&={\tilde {x}}_{1}^{(t+\Delta t)}+{\tfrac {1}{2}}d_{1}d_{3},\\[6px]x_{2}^{(t+\Delta t)}&={\tilde {x}}_{2}^{(t+\Delta t)}-{\tfrac {1}{2}}d_{1}d_{3}.\end{aligned}}$

Verlet integration is useful because it directly relates the force to the position, rather than solving the problem using velocities.

Problems, however, arise when multiple constraining forces act on each particle. One way to solve this is to loop through every point in a simulation, so that at every point the constraint relaxation of the last is already used to speed up the spread of the information. In a simulation this may be implemented by using small time steps for the simulation, using a fixed number of constraint-solving steps per time step, or solving constraints until they are met by a specific deviation.

When approximating the constraints locally to first order, this is the same as the Gauss–Seidel method. For small matrices it is known that LU decomposition is faster. Large systems can be divided into clusters (for example, each ragdoll = cluster). Inside clusters the LU method is used, between clusters the Gauss–Seidel method is used. The matrix code can be reused: The dependency of the forces on the positions can be approximated locally to first order, and the Verlet integration can be made more implicit.

Sophisticated software, such as SuperLU exists to solve complex problems using sparse matrices. Specific techniques, such as using (clusters of) matrices, may be used to address the specific problem, such as that of force propagating through a sheet of cloth without forming a sound wave.

Another way to solve holonomic constraints is to use constraint algorithms.

## Collision reactions

One way of reacting to collisions is to use a penalty-based system, which basically applies a set force to a point upon contact. The problem with this is that it is very difficult to choose the force imparted. Use too strong a force, and objects will become unstable, too weak, and the objects will penetrate each other. Another way is to use projection collision reactions, which takes the offending point and attempts to move it the shortest distance possible to move it out of the other object.

The Verlet integration would automatically handle the velocity imparted by the collision in the latter case; however, note that this is not guaranteed to do so in a way that is consistent with collision physics (that is, changes in momentum are not guaranteed to be realistic). Instead of implicitly changing the velocity term, one would need to explicitly control the final velocities of the objects colliding (by changing the recorded position from the previous time step).

The two simplest methods for deciding on a new velocity are perfectly elastic and inelastic collisions. A slightly more complicated strategy that offers more control would involve using the coefficient of restitution.
