---
title: "Power-flow study"
source: https://en.wikipedia.org/wiki/Power-flow_study
domain: power-grid-systems
license: CC-BY-SA-4.0
tags: electrical grid, power transmission, power distribution, power-system protection
fetched: 2026-07-02
---

# Power-flow study

In power engineering, a **power-flow study** is a numerical analysis of the flow of electric power in an interconnected system. It is also known as **power-flow analysis**, **load-flow study** or **load-flow analysis**, with or without the hyphen. It analyzes the power systems in normal steady-state operation and may analyze the system’s capability to adequately supply the connected load. The principal information obtained from the power-flow study is the magnitude and phase angle of the voltage at each bus, and the real power and reactive power flowing in each line. The total system losses and individual line losses are also tabulated. A power-flow study usually uses simplified notations such as a one-line diagram and per-unit system.

In terms of its approach to uncertainties, power-flow study can be divided to deterministic power-flow study and uncertainty-concerned power-flow study. Deterministic power-flow study does not take into account the uncertainties arising from both power generations and load behaviors. To take the uncertainties into consideration, there are several approaches that has been used such as probabilistic, possibilistic, information gap decision theory, robust optimization, and interval analysis.

Performing a power-flow study on an existing system provides insight and recommendations as to the system operation and optimization of control settings to obtain maximum capacity while minimizing the operating costs. Power-flow studies are important for planning future expansion of power systems as well as in determining the best operation of existing systems, especially for the optimal operations of groups of generating units. A power-flow study is especially valuable for a system with multiple load centers, such as a refinery complex.

Commercial power systems are usually too complex to allow for hand solution of the power flow. Special-purpose network analyzers were built between 1929 and the early 1960s to provide laboratory-scale physical models of power systems. Large-scale digital computers replaced the analog methods with numerical solutions.

In addition to a power-flow study, computer programs perform related calculations such as short-circuit fault analysis, stability studies (transient and steady-state), unit commitment and economic dispatch. In particular, some programs use linear programming to find the *optimal power flow*, the conditions which give the lowest cost per kilowatt hour delivered.

## Model

An *alternating current power-flow model* is a model used in electrical engineering to analyze power grids. It provides a nonlinear system of equations which describes the energy flow through each transmission line. The problem is non-linear because the power flow into load impedances is a function of the square of the applied voltages. Due to nonlinearity, in many cases the analysis of large network via AC power-flow model is not feasible, and a linear (but less accurate) DC power-flow model is used instead.

Usually, analysis of a three-phase power system is simplified by assuming balanced loading of all three phases. Sinusoidal steady-state operation is assumed, with no transient changes in power flow or voltage due to load or generation changes, meaning all current and voltage waveforms are sinusoidal with no DC offset and have the same constant frequency. The previous assumption is the same as assuming the power system is linear time-invariant (even though the system of equations is nonlinear), driven by sinusoidal sources of same frequency, and operating in steady-state, which allows to use phasor analysis, another simplification. A further simplification is to use the per-unit system to represent all voltages, power flows, and impedances, scaling the actual target system values to some convenient base. A system one-line diagram is the basis to build a mathematical model of the generators, loads, buses, and transmission lines of the system, and their electrical impedances and ratings.

DC power flow (also known as DC load flow, or DCLF) gives estimations of lines power flows on AC power systems. Despite the name, DC power flow is not an analysis on direct current, but rather on alternating current; the name comes from the linearity of the analysis, which resembles analysis on direct current. DC power flow looks only at active power flows and neglects reactive power flows. This method is non-iterative and absolutely convergent but less accurate than AC Load Flow solutions. DC power flow is used wherever repetitive and fast load flow estimations are required.

## Power-flow problem formulation

The goal of a power-flow study is to obtain complete voltage angles and magnitude information for each bus in a power system for specified load and generator real power and voltage conditions. Once this information is known, real and reactive power flow on each branch as well as generator reactive power output can be analytically determined. Due to the nonlinear nature of this problem, numerical methods are employed to obtain a solution that is within an acceptable tolerance.

The solution to the power-flow problem begins with identifying the known and unknown variables in the system. The known and unknown variables are dependent on the type of bus. A bus without any generators connected to it is called a Load Bus. With one exception, a bus with at least one generator connected to it is called a Generator Bus. The exception is one arbitrarily-selected bus that has a generator. This bus is referred to as the slack bus.

In the power-flow problem, it is assumed that the real power $P_{D}$ and reactive power $Q_{D}$ at each Load Bus are known. For this reason, Load Buses are also known as PQ Buses. For Generator Buses, it is assumed that the real power generated $P_{G}$ and the voltage magnitude $|V|$ is known. For the Slack Bus, it is assumed that the voltage magnitude $|V|$ and voltage phase $\theta$ are known. Therefore, for each Load Bus, both the voltage magnitude and angle are unknown and must be solved for; for each Generator Bus, the voltage angle must be solved for; there are no variables that must be solved for the Slack Bus. In a system with N buses and R generators, there are then $2(N-1)-(R-1)$ unknowns.

In order to solve for the $2(N-1)-(R-1)$ unknowns, there must be $2(N-1)-(R-1)$ equations that do not introduce any new unknown variables. The possible equations to use are power balance equations, which can be written for real and reactive power for each bus. The real power balance equation is:

$0=-P_{i}+\sum _{k=1}^{N}|V_{i}||V_{k}|(G_{ik}\cos \theta _{ik}+B_{ik}\sin \theta _{ik})$

where $P_{i}$ is the net active power injected at bus *i*, $G_{ik}$ is the real part of the element in the bus admittance matrix YBUS corresponding to the $i_{th}$ row and $k_{th}$ column, $B_{ik}$ is the imaginary part of the element in the YBUS corresponding to the $i_{th}$ row and $k_{th}$ column and $\theta _{ik}$ is the difference in voltage angle between the $i_{th}$ and $k_{th}$ buses ( $\theta _{ik}=\theta _{i}-\theta _{k}$ ). The reactive power balance equation is:

$0=-Q_{i}+\sum _{k=1}^{N}|V_{i}||V_{k}|(G_{ik}\sin \theta _{ik}-B_{ik}\cos \theta _{ik})$

where $Q_{i}$ is the net reactive power injected at bus *i*.

Equations included are the real and reactive power balance equations for each Load Bus and the real power balance equation for each Generator Bus. Only the real power balance equation is written for a Generator Bus because the net reactive power injected is assumed to be unknown and therefore including the reactive power balance equation would result in an additional unknown variable. For similar reasons, there are no equations written for the Slack Bus.

In many transmission systems, the impedance of the power network lines is primarily inductive, i.e. the phase angles of the power lines impedance are usually relatively large and very close to 90 degrees. There is thus a strong coupling between real power and voltage angle, and between reactive power and voltage magnitude, while the coupling between real power and voltage magnitude, as well as reactive power and voltage angle, is weak. As a result, real power is usually transmitted from the bus with higher voltage angle to the bus with lower voltage angle, and reactive power is usually transmitted from the bus with higher voltage magnitude to the bus with lower voltage magnitude. However, this approximation does not hold when the phase angle of the power line impedance is relatively small.

## Newton–Raphson solution method

There are several different methods of solving the resulting nonlinear system of equations. The most popular is a variation of the Newton–Raphson method. The Newton-Raphson method is an iterative method which begins with initial guesses of all unknown variables (voltage magnitude and angles at Load Buses and voltage angles at Generator Buses). Next, a Taylor Series is written, with the higher order terms ignored, for each of the power balance equations included in the system of equations. The result is a linear system of equations that can be expressed as:

${\begin{bmatrix}\Delta \theta \\\Delta |V|\end{bmatrix}}=-J^{-1}{\begin{bmatrix}\Delta P\\\Delta Q\end{bmatrix}}$

where $\Delta P$ and $\Delta Q$ are called the mismatch equations:

$\Delta P_{i}=-P_{i}+\sum _{k=1}^{N}|V_{i}||V_{k}|(G_{ik}\cos \theta _{ik}+B_{ik}\sin \theta _{ik})$ $\Delta Q_{i}=-Q_{i}+\sum _{k=1}^{N}|V_{i}||V_{k}|(G_{ik}\sin \theta _{ik}-B_{ik}\cos \theta _{ik})$

and J is a matrix of partial derivatives known as a Jacobian: $J={\begin{bmatrix}{\dfrac {\partial \Delta P}{\partial \theta }}&{\dfrac {\partial \Delta P}{\partial |V|}}\\{\dfrac {\partial \Delta Q}{\partial \theta }}&{\dfrac {\partial \Delta Q}{\partial |V|}}\end{bmatrix}}$ .

The linearized system of equations is solved to determine the next guess (*m* + 1) of voltage magnitude and angles based on:

$\theta _{m+1}=\theta _{m}+\Delta \theta \,$ $|V|_{m+1}=|V|_{m}+\Delta |V|\,$

The process continues until a stopping condition is met. A common stopping condition is to terminate if the norm of the mismatch equations is below a specified tolerance.

A rough outline of solution of the power-flow problem is:

1. Make an initial guess of all unknown voltage magnitudes and angles. It is common to use a "flat start" in which all voltage angles are set to zero and all voltage magnitudes are set to 1.0 p.u.
2. Solve the power balance equations using the most recent voltage angle and magnitude values.
3. Linearize the system around the most recent voltage angle and magnitude values
4. Solve for the change in voltage angle and magnitude
5. Update the voltage magnitude and angles
6. Check the stopping conditions, if met then terminate, else go to step 2.

## Other power-flow methods

- Gauss–Seidel method: This is the earliest devised method. It shows slower rates of convergence compared to other iterative methods, but it uses very little memory and does not need to solve a matrix system.
- Fast-decoupled-load-flow method is a variation on Newton–Raphson that exploits the approximate decoupling of active and reactive flows in well-behaved power networks, and additionally fixes the value of the Jacobian during the iteration in order to avoid costly matrix decompositions. Also referred to as "fixed-slope, decoupled NR". Within the algorithm, the Jacobian matrix gets inverted only once, and there are three assumptions. Firstly, the conductance between the buses is zero. Secondly, the magnitude of the bus voltage is one per unit. Thirdly, the sine of phases between buses is zero. Fast decoupled load flow can return the answer within seconds whereas the Newton Raphson method takes much longer. This is useful for real-time management of power grids.
- Holomorphic embedding load flow method: A recently developed method based on advanced techniques of complex analysis. It is direct and guarantees the calculation of the correct (operative) branch, out of the multiple solutions present in the power-flow equations.
- Backward-Forward Sweep (BFS) method: A method developed to take advantage of the radial structure of most modern distribution grids. It involves choosing an initial voltage profile and separating the original system of equations of grid components into two separate systems and solving one, using the last results of the other, until convergence is achieved. Solving for the currents with the voltages given is called the backward sweep (BS) and solving for the voltages with the currents given is called the forward sweep (FS).
- Laurent Power Flow (LPF) method: Power flow formulation that provides guarantee of uniqueness of solution and independence on initial conditions for electrical distribution systems. The LPF is based on the current injection method (CIM) and applies the Laurent series expansion. The main characteristics of this formulation are its proven numerical convergence and stability, and its computational advantages, showing to be at least ten times faster than the BFS method both in balanced and unbalanced networks. Since it is based on the system's admittance matrix, the formulation is able to consider radial and meshed network topologies without additional modifications (contrary to the compensation-based BFS). The simplicity and computational efficiency of the LPF method make it an attractive option for recursive power flow problems, such as those encountered in time-series analyses, metaheuristics, probabilistic analysis, reinforcement learning applied to power systems, and other related applications.
