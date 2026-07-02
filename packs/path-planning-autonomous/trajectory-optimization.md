---
title: "Trajectory optimization"
source: https://en.wikipedia.org/wiki/Trajectory_optimization
domain: path-planning-autonomous
license: CC-BY-SA-4.0
tags: motion planning, rapidly exploring random tree, occupancy grid, trajectory optimization
fetched: 2026-07-02
---

# Trajectory optimization

**Trajectory optimization** is the process of designing a trajectory that minimizes (or maximizes) some measure of performance while satisfying a set of constraints. Generally speaking, trajectory optimization is a technique for computing an open-loop solution to an optimal control problem. It is often used for systems where computing the full closed-loop solution is not required, impractical or impossible. If a trajectory optimization problem can be solved at a rate given by the inverse of the Lipschitz constant, then it can be used iteratively to generate a closed-loop solution in the sense of Caratheodory. If only the first step of the trajectory is executed for an infinite-horizon problem, then this is known as Model Predictive Control (MPC).

Although the idea of trajectory optimization has been around for hundreds of years (calculus of variations, brachistochrone problem), it only became practical for real-world problems with the advent of the computer. Many of the original applications of trajectory optimization were in the aerospace industry, computing rocket and missile launch trajectories. More recently, trajectory optimization has also been used in a wide variety of industrial process and robotics applications.

## History

Trajectory optimization first showed up in 1697, with the introduction of the brachystochrone problem: find the shape of a wire such that a bead sliding along it will move between two points in the minimum time. The interesting thing about this problem is that it is optimizing over a curve (the shape of the wire), rather than a single number. The most famous of the solutions was computed using calculus of variations.

In the 1950s, the digital computer started to make trajectory optimization practical for solving real-world problems. The first optimal control approaches grew out of the calculus of variations, based on the research of Gilbert Ames Bliss and Bryson in America, and Pontryagin in Russia. Pontryagin's maximum principle is of particular note. These early researchers created the foundation of what we now call indirect methods for trajectory optimization.

Much of the early work in trajectory optimization was focused on computing rocket thrust profiles, both in a vacuum and in the atmosphere. This early research discovered many basic principles that are still used today. Another successful application was the climb to altitude trajectories for the early jet aircraft. Because of the high drag associated with the transonic drag region and the low thrust of early jet aircraft, trajectory optimization was the key to maximizing climb to altitude performance. Optimal control based trajectories were responsible for some of the world records. In these situations, the pilot followed a Mach versus altitude schedule based on optimal control solutions.

One of the important early problems in trajectory optimization was that of the singular arc, where Pontryagin's maximum principle fails to yield a complete solution. An example of a problem with singular control is the optimization of the thrust of a missile flying at a constant altitude and which is launched at low speed. Here the problem is one of a bang-bang control at maximum possible thrust until the singular arc is reached. Then the solution to the singular control provides a lower variable thrust until burnout. At that point bang-bang control provides that the control or thrust go to its minimum value of zero. This solution is the foundation of the boost-sustain rocket motor profile widely used today to maximize missile performance.

## Applications

There are a wide variety of applications for trajectory optimization, primarily in robotics: industry, manipulation, walking, path-planning, and aerospace. It can also be used for modeling and estimation.

### Robotic manipulators

Depending on the configuration, open-chain robotic manipulators require a degree of trajectory optimization. For instance, a robotic arm with 7 joints and 7 links (7-DOF) is a redundant system where one cartesian position of an end-effector can correspond to an infinite number of joint angle positions, thus this redundancy can be used to optimize a trajectory to, for example, avoid any obstacles in the workspace or minimize the torque in the joints. Computing the desired path for robotic manipulators is useful in industrial manufacturing.

### Manufacturing and processing

Trajectory optimization is used in manufacturing, particularly for controlling chemical processes. It has also been proposed for liquids processing, such as for evaporators or for desalination.

### Walking robots

There are a variety of different applications for trajectory optimization within the field of walking robotics. For example, one paper used trajectory optimization of bipedal gaits on a simple model to show that walking is energetically favorable for moving at a low speed and running is energetically favorable for moving at a high speed. Like in many other applications, trajectory optimization can be used to compute a nominal trajectory, around which a stabilizing controller is built. Trajectory optimization can be applied in detailed motion planning complex humanoid robots, such as Atlas. Finally, trajectory optimization can be used for path-planning of robots with complicated dynamics constraints, using reduced complexity models.

### Aerospace

Trajectory optimization is often used to compute trajectories for quadrotor helicopters. These applications typically used highly specialized algorithms. One interesting application shown by the U.Penn GRASP Lab is computing a trajectory that allows a quadrotor to fly through a hoop as it is thrown. Another, this time by the ETH Zurich Flying Machine Arena, involves two quadrotors tossing a pole back and forth between them, with it balanced like an inverted pendulum. The problem of computing minimum-energy trajectories for a quadcopter, has also been recently studied.

For tactical missiles, the flight profiles are determined by the thrust and lift histories. These histories can be controlled by a number of means including such techniques as using an angle of attack command history or an altitude/downrange schedule that the missile must follow. Each combination of missile design factors, desired missile performance, and system constraints results in a new set of optimal control parameters.

Guidance strategies for spacecraft are normally determined through solving a trajectory optimization problem. A thrust profile, describing the variation of the magnitude and direction of the force exerted by an onboard thruster, is computed, typically with the goal of minimizing the propellant or time required to reach a destination.

## Terminology

**Decision variables**

The set of unknowns to be found using optimization.

**Trajectory optimization problem**

A special type of optimization problem where the decision variables are functions, rather than real numbers.

**Parameter optimization**

Any optimization problem where the decision variables are real numbers.

**Nonlinear program**

A class of constrained parameter optimization where either the objective function or constraints are nonlinear.

**Indirect method**

An indirect method for solving a trajectory optimization problem proceeds in three steps: 1) Analytically construct the necessary and sufficient conditions for optimality, 2) Discretize these conditions, constructing a constrained parameter optimization problem, 3) Solve that optimization problem.

**Direct method**

A direct method for solving a trajectory optimization problem consists of two steps: 1) Discretize the trajectory optimization problem directly, converting it into a constrained parameter optimization problem, 2) Solve that optimization problem.

**Transcription**

The process by which a trajectory optimization problem is converted into a parameter optimization problem. This is sometimes referred to as discretization. Transcription methods generally fall into two categories: shooting methods and collocation methods.

**Shooting method**

A transcription method that is based on simulation, typically using explicit Runge--Kutta schemes.

**Collocation method (Simultaneous Method)**

A transcription method that is based on

function approximation

, typically using implicit Runge--Kutta schemes.

**Pseudospectral method (Global Collocation)**

A transcription method that represents the entire trajectory as a single high-order orthogonal polynomial.

**Mesh (Grid)**

After transcription, the formerly continuous trajectory is now represented by a discrete set of points, known as mesh points or grid points.

**Mesh refinement**

The process by which the discretization mesh is improved by solving a sequence of trajectory optimization problems. Mesh refinement is either performed by sub-dividing a trajectory segment or by increasing the order of the polynomial representing that segment.

**Multi-phase trajectory optimization problem**

Trajectory optimization over a system with

hybrid dynamics

can be achieved by posing it as a multi-phase trajectory optimization problem. This is done by composing a sequence of standard trajectory optimization problems that are connected using constraints.

## Trajectory optimization techniques

The techniques to any optimization problems can be divided into two categories: indirect and direct. An indirect method works by analytically constructing the necessary and sufficient conditions for optimality, which are then solved numerically. A direct method attempts a direct numerical solution by constructing a sequence of continually improving approximations to the optimal solution.

The optimal control problem is an infinite-dimensional optimization problem, since the decision variables are functions, rather than real numbers. All solution techniques perform transcription, a process by which the trajectory optimization problem (optimizing over functions) is converted into a constrained parameter optimization problem (optimizing over real numbers). Generally, this constrained parameter optimization problem is a non-linear program, although in special cases it can be reduced to a quadratic program or linear program.

### Single shooting

Single shooting is the simplest type of trajectory optimization technique. The basic idea is similar to how you would aim a cannon: pick a set of parameters for the trajectory, simulate the entire thing, and then check to see if you hit the target. The entire trajectory is represented as a single segment, with a single constraint, known as a defect constraint, requiring that the final state of the simulation matches the desired final state of the system. Single shooting is effective for problems that are either simple or have an extremely good initialization. Both the indirect and direct formulation tend to have difficulties otherwise.

### Multiple shooting

Multiple shooting is a simple extension to single shooting that renders it far more effective. Rather than representing the entire trajectory as a single simulation (segment), the algorithm breaks the trajectory into many shorter segments, and a defect constraint is added between each. The result is large sparse non-linear program, which tends to be easier to solve than the small dense programs produced by single shooting. The particular sparsity structure can be exploited by tailored numerical solvers as implemented in the open-source software package acados.

### Direct collocation

Direct collocation methods work by approximating the state and control trajectories using polynomial splines. These methods are sometimes referred to as direct transcription. **Trapezoidal collocation** is a commonly used low-order direct collocation method. The dynamics, path objective, and control are all represented using linear splines, and the dynamics are satisfied using trapezoidal quadrature. **Hermite-Simpson Collocation** is a common medium-order direct collocation method. The state is represented by a cubic-Hermite spline, and the dynamics are satisfied using Simpson quadrature.

### Orthogonal collocation

Orthogonal collocation is technically a subset of direct collocation, but the implementation details are so different that it can reasonably be considered its own set of methods. Orthogonal collocation differs from direct collocation in that it typically uses high-order splines, and each segment of the trajectory might be represented by a spline of a different order. The name comes from the use of orthogonal polynomials in the state and control splines.

### Pseudospectral discretization

In pseudospectral discretization the entire trajectory is represented by a collection of basis functions in the time domain (independent variable). The basis functions need not be polynomials. Pseudospectral discretization is also known as spectral collocation. When used to solve a trajectory optimization problem whose solution is smooth, a pseudospectral method will achieve spectral (exponential) convergence. If the trajectory is not smooth, the convergence is still very fast, faster than Runge-Kutta methods.

### Temporal Finite Elements

In 1990 Dewey H. Hodges and Robert R. Bless proposed a weak Hamiltonian finite element method for optimal control problems. The idea was to derive a weak variational form of first order necessary conditions for optimality, discretise the time domain in finite intervals and use a simple zero order polynomial representation of states, controls and adjoints over each interval.

### Differential dynamic programming

Differential dynamic programming, is a bit different than the other techniques described here. In particular, it does not cleanly separate the transcription and the optimization. Instead, it does a sequence of iterative forward and backward passes along the trajectory. Each forward pass satisfies the system dynamics, and each backward pass satisfies the optimality conditions for control. Eventually, this iteration converges to a trajectory that is both feasible and optimal.

### Diffusion-based trajectory optimization

In contrast to the aforementioned classical methods, generative machine learning methods may be used to generate a desirable trajectory. In particular, diffusion models learn to iteratively reverse a destructive forward process in which noise is added to data until it becomes noise itself by estimating the noise to remove at every time step. Thus given easily to sample random noise as input, the diffusion process will recover a plausible corresponding noise-free data point. Recent methods have parameterized trajectories as matrices of state-action pairs at consecutive time steps and trained a diffusion model to generate such a matrix. To address the issue of controllability of the generated samples, the Diffuser method proposes two techniques to steer the generated sample, thereby reducing the optimization problem to a sampling problem. First, *guided* diffusion can be used to incorporate a cost (or reward) function into the generation process. For this purpose the gradient of the cost function modifies the mean of the estimated noise at every time step. Second, for motion planning problems in which the start and the end states of the trajectory are known, and the trajectory needs to comply with constraints to find a viable path, an inpainting approach can be used. Similar to the first technique, a prior modifies the distribution of trajectories, which in this case assigns high probability to trajectories satisfying the constraints (e.g. arriving at a state s at time step t ), and zero probability to all other trajectories. As a result, sampling from this distribution will produce trajectories that satisfy the constraints.

## Comparison of techniques

There are many techniques to choose from when solving a trajectory optimization problem. There is no best method, but some methods might do a better job on specific problems. This section provides a rough understanding of the trade-offs between methods.

### Indirect vs. direct methods

When solving a trajectory optimization problem with an indirect method, you must explicitly construct the adjoint equations and their gradients. This is often difficult to do, but it gives an excellent accuracy metric for the solution. Direct methods are much easier to set up and solve, but do not have a built-in accuracy metric. As a result, direct methods are more widely used, especially in non-critical applications. Indirect methods still have a place in specialized applications, particularly aerospace, where accuracy is critical.

One place where indirect methods have particular difficulty is on problems with path inequality constraints. These problems tend to have solutions for which the constraint is partially active. When constructing the adjoint equations for an indirect method, the user must explicitly write down when the constraint is active in the solution, which is difficult to know a priori. One solution is to use a direct method to compute an initial guess, which is then used to construct a multi-phase problem where the constraint is prescribed. The resulting problem can then be solved accurately using an indirect method.

### Shooting vs. collocation

Single shooting methods are best used for problems where the control is very simple (or there is an extremely good initial guess). For example, a satellite mission planning problem where the only control is the magnitude and direction of an initial impulse from the engines.

Multiple shooting tends to be good for problems with relatively simple control, but complicated dynamics. Although path constraints can be used, they make the resulting nonlinear program relatively difficult to solve.

Direct collocation methods are good for problems where the accuracy of the control and the state are similar. These methods tend to be less accurate than others (due to their low-order), but are particularly robust for problems with difficult path constraints.

Orthogonal collocation methods are best for obtaining high-accuracy solutions to problems where the accuracy of the control trajectory is important. Some implementations have trouble with path constraints. These methods are particularly good when the solution is smooth.
