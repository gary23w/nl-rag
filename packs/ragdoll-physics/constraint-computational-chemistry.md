---
title: "Constraint (computational chemistry)"
source: https://en.wikipedia.org/wiki/Constraint_(computational_chemistry)
domain: ragdoll-physics
license: CC-BY-SA-4.0
tags: ragdoll physics, ragdoll simulation, articulated body physics, physics-driven character
fetched: 2026-07-02
---

# Constraint (computational chemistry)

In computational chemistry, a **constraint algorithm** is a method for satisfying the Newtonian motion of a rigid body which consists of mass points. A restraint algorithm is used to ensure that the distance between mass points is maintained. The general steps involved are: (i) choose novel unconstrained coordinates (internal coordinates), (ii) introduce explicit constraint forces, (iii) minimize constraint forces implicitly by the technique of Lagrange multipliers or projection methods.

Constraint algorithms are often applied to molecular dynamics simulations. Although such simulations are sometimes performed using internal coordinates that automatically satisfy the bond-length, bond-angle and torsion-angle constraints, simulations may also be performed using explicit or implicit constraint forces for these three constraints. However, explicit constraint forces give rise to inefficiency; more computational power is required to get a trajectory of a given length. Therefore, internal coordinates and implicit-force constraint solvers are generally preferred.

Constraint algorithms achieve computational efficiency by neglecting motion along some degrees of freedom. For instance, in atomistic molecular dynamics, typically the length of covalent bonds to hydrogen are constrained; however, constraint algorithms should not be used if vibrations along these degrees of freedom are important for the phenomenon being studied.

## Mathematical background

The motion of a set of *N* particles can be described by a set of second-order ordinary differential equations, Newton's second law, which can be written in matrix form

$\mathbf {M} \cdot {\frac {d^{2}\mathbf {q} }{dt^{2}}}=\mathbf {f} =-{\frac {\partial V}{\partial \mathbf {q} }}$

where **M** is a *mass matrix* and **q** is the vector of generalized coordinates that describe the particles' positions. For example, the vector **q** may be a *3N* Cartesian coordinates of the particle positions **r***k*, where *k* runs from 1 to *N*; in the absence of constraints, **M** would be the *3N*x*3N* diagonal square matrix of the particle masses. The vector **f** represents the generalized forces and the scalar *V*(**q**) represents the potential energy, both of which are functions of the generalized coordinates **q**.

If *M* constraints are present, the coordinates must also satisfy *M* time-independent algebraic equations

$g_{j}(\mathbf {q} )=0$

where the index *j* runs from 1 to *M*. For brevity, these functions *g**i* are grouped into an *M*-dimensional vector **g** below. The task is to solve the combined set of differential-algebraic (DAE) equations, instead of just the ordinary differential equations (ODE) of Newton's second law.

This problem was studied in detail by Joseph Louis Lagrange, who laid out most of the methods for solving it. The simplest approach is to define new generalized coordinates that are unconstrained; this approach eliminates the algebraic equations and reduces the problem once again to solving an ordinary differential equation. Such an approach is used, for example, in describing the motion of a rigid body; the position and orientation of a rigid body can be described by six independent, unconstrained coordinates, rather than describing the positions of the particles that make it up and the constraints among them that maintain their relative distances. The drawback of this approach is that the equations may become unwieldy and complex; for example, the mass matrix **M** may become non-diagonal and depend on the generalized coordinates.

A second approach is to introduce explicit forces that work to maintain the constraint; for example, one could introduce strong spring forces that enforce the distances among mass points within a "rigid" body. The two difficulties of this approach are that the constraints are not satisfied exactly, and the strong forces may require very short time-steps, making simulations inefficient computationally.

A third approach is to use a method such as Lagrange multipliers or projection to the constraint manifold to determine the coordinate adjustments necessary to satisfy the constraints.

Finally, there are various hybrid approaches in which different sets of constraints are satisfied by different methods, e.g., internal coordinates, explicit forces and implicit-force solutions.

## Internal coordinate methods

The simplest approach to satisfying constraints in energy minimization and molecular dynamics is to represent the mechanical system in so-called *internal coordinates* corresponding to unconstrained independent degrees of freedom of the system. For example, the dihedral angles of a protein are an independent set of coordinates that specify the positions of all the atoms without requiring any constraints. The difficulty of such internal-coordinate approaches is twofold: the Newtonian equations of motion become much more complex and the internal coordinates may be difficult to define for cyclic systems of constraints, e.g., in ring puckering or when a protein has a disulfide bond.

The original methods for efficient recursive energy minimization in internal coordinates were developed by Gō and coworkers.

Efficient recursive, internal-coordinate constraint solvers were extended to molecular dynamics. Analogous methods were applied later to other systems.

## Lagrange multiplier-based methods

In most of molecular dynamics simulations that use constraint algorithms, constraints are enforced using the method of Lagrange multipliers. Given a set of *n* linear (holonomic) constraints at the time *t*,

$\sigma _{k}(t):=\|\mathbf {x} _{k\alpha }(t)-\mathbf {x} _{k\beta }(t)\|^{2}-d_{k}^{2}=0,\quad k=1\ldots n$

where $\scriptstyle \mathbf {x} _{k\alpha }(t)$ and $\scriptstyle \mathbf {x} _{k\beta }(t)$ are the positions of the two particles involved in the *k*th constraint at the time *t* and $d_{k}$ is the prescribed inter-particle distance.

The forces due to these constraints are added in the equations of motion, resulting in, for each of the *N* particles in the system

${\frac {\partial ^{2}\mathbf {x} _{i}(t)}{\partial t^{2}}}m_{i}=-{\frac {\partial }{\partial \mathbf {x} _{i}}}\left[V(\mathbf {x} _{i}(t))-\sum _{k=1}^{n}\lambda _{k}\sigma _{k}(t)\right],\quad i=1\ldots N.$

Adding the constraint forces does not change the total energy, as the net work done by the constraint forces (taken over the set of particles that the constraints act on) is zero. Note that the sign on $\lambda _{k}$ is arbitrary and some references have an opposite sign.

From integrating both sides of the equation with respect to the time, the constrained coordinates of particles at the time, $t+\Delta t$ , are given,

$\mathbf {x} _{i}(t+\Delta t)={\hat {\mathbf {x} }}_{i}(t+\Delta t)+\sum _{k=1}^{n}\lambda _{k}{\frac {\partial \sigma _{k}(t)}{\partial \mathbf {x} _{i}}}\left(\Delta t\right)^{2}m_{i}^{-1},\quad i=1\ldots N$

where ${\hat {\mathbf {x} }}_{i}(t+\Delta t)$ is the unconstrained (or uncorrected) position of the *i*th particle after integrating the unconstrained equations of motion.

To satisfy the constraints $\sigma _{k}(t+\Delta t)$ in the next timestep, the Lagrange multipliers should be determined as the following equation,

$\sigma _{k}(t+\Delta t):=\left\|\mathbf {x} _{k\alpha }(t+\Delta t)-\mathbf {x} _{k\beta }(t+\Delta t)\right\|^{2}-d_{k}^{2}=0.$

This implies solving a system of n non-linear equations

$\sigma _{j}(t+\Delta t):=\left\|{\hat {\mathbf {x} }}_{j\alpha }(t+\Delta t)-{\hat {\mathbf {x} }}_{j\beta }(t+\Delta t)+\sum _{k=1}^{n}\lambda _{k}\left(\Delta t\right)^{2}\left[{\frac {\partial \sigma _{k}(t)}{\partial \mathbf {x} _{j\alpha }}}m_{j\alpha }^{-1}-{\frac {\partial \sigma _{k}(t)}{\partial \mathbf {x} _{j\beta }}}m_{j\beta }^{-1}\right]\right\|^{2}-d_{j}^{2}=0,\quad j=1\ldots n$

simultaneously for the n unknown Lagrange multipliers $\lambda _{k}$ .

This system of n non-linear equations in n unknowns is commonly solved using Newton–Raphson method where the solution vector ${\underline {\lambda }}$ is updated using

${\underline {\lambda }}^{(l+1)}\leftarrow {\underline {\lambda }}^{(l)}-\mathbf {J} _{\sigma }^{-1}{\underline {\sigma }}(t+\Delta t)$

where $\mathbf {J} _{\sigma }$ is the Jacobian of the equations σ*k*:

$\mathbf {J} =\left({\begin{array}{cccc}{\frac {\partial \sigma _{1}}{\partial \lambda _{1}}}&{\frac {\partial \sigma _{1}}{\partial \lambda _{2}}}&\cdots &{\frac {\partial \sigma _{1}}{\partial \lambda _{n}}}\\[5pt]{\frac {\partial \sigma _{2}}{\partial \lambda _{1}}}&{\frac {\partial \sigma _{2}}{\partial \lambda _{2}}}&\cdots &{\frac {\partial \sigma _{2}}{\partial \lambda _{n}}}\\[5pt]\vdots &\vdots &\ddots &\vdots \\[5pt]{\frac {\partial \sigma _{n}}{\partial \lambda _{1}}}&{\frac {\partial \sigma _{n}}{\partial \lambda _{2}}}&\cdots &{\frac {\partial \sigma _{n}}{\partial \lambda _{n}}}\end{array}}\right).$

Since not all particles contribute to all of constraints, $\mathbf {J} _{\sigma }$ is a block matrix and can be solved individually to block-unit of the matrix. In other words, $\mathbf {J} _{\sigma }$ can be solved individually for each molecule.

Instead of constantly updating the vector ${\underline {\lambda }}$ , the iteration can be started with ${\underline {\lambda }}^{(0)}=\mathbf {0}$ , resulting in simpler expressions for $\sigma _{k}(t)$ and ${\frac {\partial \sigma _{k}(t)}{\partial \lambda _{j}}}$ . In this case

$J_{ij}=\left.{\frac {\partial \sigma _{j}}{\partial \lambda _{i}}}\right|_{\mathbf {\lambda } =0}=2\left[{\hat {x}}_{j\alpha }-{\hat {x}}_{j\beta }\right]\left[{\frac {\partial \sigma _{i}}{\partial x_{j\alpha }}}m_{j\alpha }^{-1}-{\frac {\partial \sigma _{i}}{\partial x_{j\beta }}}m_{j\beta }^{-1}\right].$

then $\lambda$ is updated to

$\mathbf {\lambda } _{j}=-\mathbf {J} ^{-1}\left[\left\|{\hat {\mathbf {x} }}_{j\alpha }(t+\Delta t)-{\hat {\mathbf {x} }}_{j\beta }(t+\Delta t)\right\|^{2}-d_{j}^{2}\right].$

After each iteration, the unconstrained particle positions are updated using

${\hat {\mathbf {x} }}_{i}(t+\Delta t)\leftarrow {\hat {\mathbf {x} }}_{i}(t+\Delta t)+\sum _{k=1}^{n}\lambda _{k}{\frac {\partial \sigma _{k}}{\partial \mathbf {x} _{i}}}\left(\Delta t\right)^{2}m_{i}^{-1}.$

The vector is then reset to

${\underline {\lambda }}=\mathbf {0} .$

The above procedure is repeated until the solution of constraint equations, $\sigma _{k}(t+\Delta t)$ , converges to a prescribed tolerance of a numerical error.

Although there are a number of algorithms to compute the Lagrange multipliers, these difference is rely only on the methods to solve the system of equations. For this methods, quasi-Newton methods are commonly used.

### The SETTLE algorithm

The SETTLE algorithm solves the system of non-linear equations analytically for $n=3$ constraints in constant time. Although it does not scale to larger numbers of constraints, it is very often used to constrain rigid water molecules, which are present in almost all biological simulations and are usually modelled using three constraints (e.g. SPC/E and TIP3P water models).

### The SHAKE algorithm

The SHAKE algorithm was first developed for satisfying a bond geometry constraint during molecular dynamics simulations. The method was then generalised to handle any holonomic constraint, such as those required to maintain constant bond angles, or molecular rigidity.

In SHAKE algorithm, the system of non-linear constraint equations is solved using the Gauss–Seidel method which approximates the solution of the linear system of equations using the Newton–Raphson method;

${\underline {\lambda }}=-\mathbf {J} _{\sigma }^{-1}{\underline {\sigma }}.$

This amounts to assuming that $\mathbf {J} _{\sigma }$ is diagonally dominant and solving the k th equation only for the k unknown. In practice, we compute

${\begin{aligned}\lambda _{k}&\leftarrow {\frac {\sigma _{k}(t)}{\partial \sigma _{k}(t)/\partial \lambda _{k}}},\\[5pt]\mathbf {x} _{k\alpha }&\leftarrow \mathbf {x} _{k\alpha }+\lambda _{k}{\frac {\partial \sigma _{k}(t)}{\partial \mathbf {x} _{k\alpha }}},\\[5pt]\mathbf {x} _{k\beta }&\leftarrow \mathbf {x} _{k\beta }+\lambda _{k}{\frac {\partial \sigma _{k}(t)}{\partial \mathbf {x} _{k\beta }}},\end{aligned}}$

for all $k=1\ldots n$ iteratively until the constraint equations $\sigma _{k}(t+\Delta t)$ are solved to a given tolerance.

The calculation cost of each iteration is ${\mathcal {O}}(n)$ , and the iterations themselves converge linearly.

A noniterative form of SHAKE was developed later on.

Several variants of the SHAKE algorithm exist. Although they differ in how they compute or apply the constraints themselves, the constraints are still modelled using Lagrange multipliers which are computed using the Gauss–Seidel method.

The original SHAKE algorithm is capable of constraining both rigid and flexible molecules (e.g. water, benzene and biphenyl) and introduces negligible error or energy drift into a molecular dynamics simulation. One issue with SHAKE is that the number of iterations required to reach a certain level of convergence does rise as molecular geometry becomes more complex. To reach 64 bit computer accuracy (a relative tolerance of $\approx 10^{-16}$ ) in a typical molecular dynamics simulation at a temperature of 310K, a 3-site water model having 3 constraints to maintain molecular geometry requires an average of 9 iterations (which is 3 per site per time-step). A 4-site butane model with 5 constraints needs 17 iterations (22 per site), a 6-site benzene model with 12 constraints needs 36 iterations (72 per site), while a 12-site biphenyl model with 29 constraints requires 92 iterations (229 per site per time-step). Hence the CPU requirements of the SHAKE algorithm can become significant, particularly if a molecular model has a high degree of rigidity.

A later extension of the method, QSHAKE (Quaternion SHAKE) was developed as a faster alternative for molecules composed of rigid units, but it is not as general purpose. It works satisfactorily for *rigid* loops such as aromatic ring systems but QSHAKE fails for flexible loops, such as when a protein has a disulfide bond.

Further extensions include RATTLE, WIGGLE, and MSHAKE.

While RATTLE works the same way as SHAKE, yet using the Velocity Verlet time integration scheme, WIGGLE extends SHAKE and RATTLE by using an initial estimate for the Lagrange multipliers $\lambda _{k}$ based on the particle velocities. It is worth mentioning that MSHAKE computes corrections on the constraint *forces*, achieving better convergence.

A final modification to the SHAKE algorithm is the P-SHAKE algorithm that is applied to very rigid or semi-rigid molecules. P-SHAKE computes and updates a pre-conditioner which is applied to the constraint gradients before the SHAKE iteration, causing the Jacobian $\mathbf {J} _{\sigma }$ to become diagonal or strongly diagonally dominant. The thus de-coupled constraints converge much faster (quadratically as opposed to linearly) at a cost of ${\mathcal {O}}(n^{2})$ .

### The M-SHAKE algorithm

The M-SHAKE algorithm solves the non-linear system of equations using Newton's method directly. In each iteration, the linear system of equations

${\underline {\lambda }}=-\mathbf {J} _{\sigma }^{-1}{\underline {\sigma }}$

is solved exactly using an LU decomposition. Each iteration costs ${\mathcal {O}}(n^{3})$ operations, yet the solution converges quadratically, requiring fewer iterations than SHAKE.

This solution was first proposed in 1986 by Ciccotti and Ryckaert under the title "the matrix method", yet differed in the solution of the linear system of equations. Ciccotti and Ryckaert suggest inverting the matrix $\mathbf {J} _{\sigma }$ directly, yet doing so only once, in the first iteration. The first iteration then costs ${\mathcal {O}}(n^{3})$ operations, whereas the following iterations cost only ${\mathcal {O}}(n^{2})$ operations (for the matrix-vector multiplication). This improvement comes at a cost though, since the Jacobian is no longer updated, convergence is only linear, albeit at a much faster rate than for the SHAKE algorithm.

Several variants of this approach based on sparse matrix techniques were studied by Barth *et al.*.

### SHAPE algorithm

The SHAPE algorithm is a multicenter analog of SHAKE for constraining rigid bodies of three or more centers. Like SHAKE, an unconstrained step is taken and then corrected by directly calculating and applying the rigid body rotation matrix that satisfies:

$L^{\text{rigid}}\left(t+{\frac {\Delta t}{2}}\right)=L^{\text{nonrigid}}\left(t+{\frac {\Delta t}{2}}\right)$

This approach involves a single 3×3 matrix diagonalization followed by three or four rapid Newton iterations to determine the rotation matrix. SHAPE provides the identical trajectory that is provided with fully converged iterative SHAKE, yet it is found to be more efficient and more accurate than SHAKE when applied to systems involving three or more centers. It extends the ability of SHAKE like constraints to linear systems with three or more atoms, planar systems with four or more atoms, and to significantly larger rigid structures where SHAKE is intractable. It also allows rigid bodies to be linked with one or two common centers (e.g. peptide planes) by solving rigid body constraints iteratively in the same basic manner that SHAKE is used for atoms involving more than one SHAKE constraint.

### LINCS algorithm

An alternative constraint method, LINCS (Linear Constraint Solver) was developed in 1997 by Hess, Bekker, Berendsen and Fraaije, and was based on the 1986 method of Edberg, Evans and Morriss (EEM), and a modification thereof by Baranyai and Evans (BE).

LINCS applies Lagrange multipliers to the constraint forces and solves for the multipliers by using a series expansion to approximate the inverse of the Jacobian $\mathbf {J} _{\sigma }$ :

$(\mathbf {I} -\mathbf {J} _{\sigma })^{-1}=\mathbf {I} +\mathbf {J} _{\sigma }+\mathbf {J} _{\sigma }^{2}+\mathbf {J} _{\sigma }^{3}+\cdots$

in each step of the Newton iteration. This approximation only works for matrices with eigenvalues smaller than 1, making the LINCS algorithm suitable only for molecules with low connectivity.

LINCS has been reported to be 3–4 times faster than SHAKE.

## Hybrid methods

Hybrid methods have also been introduced in which the constraints are divided into two groups; the constraints of the first group are solved using internal coordinates whereas those of the second group are solved using constraint forces, e.g., by a Lagrange multiplier or projection method. This approach was pioneered by Lagrange, and result in *Lagrange equations of the mixed type*.
