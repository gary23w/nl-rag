---
title: "Neural differential equation"
source: https://en.wikipedia.org/wiki/Neural_ordinary_differential_equation
domain: flow-matching
license: CC-BY-SA-4.0
tags: flow matching, continuous normalizing flow, optimal transport, generative ode
fetched: 2026-07-02
---

# Neural differential equation

(Redirected from

Neural ordinary differential equation

)

**Neural differential equations** are a class of models in machine learning that combine neural networks with the mathematical framework of differential equations. These models provide an alternative approach to neural network design, particularly for systems that evolve over time or through continuous transformations.

The most common type, a **neural ordinary differential equation (neural ODE)**, defines the evolution of a system's state using an ordinary differential equation whose dynamics are governed by a neural network: ${\frac {\mathrm {d} \mathbf {h} (t)}{\mathrm {d} t}}=f_{\theta }(\mathbf {h} (t),t).$ In this formulation, the neural network parameters *θ* determine how the state changes at each point in time. This approach contrasts with conventional neural networks, where information flows through discrete layers indexed by natural numbers. Neural ODEs instead use continuous layers indexed by positive real numbers, where the function $h:\mathbb {R} _{\geq 0}\to \mathbb {R}$ represents the network's state at any given layer depth *t*.

Neural ODEs can be understood as continuous-time control systems, where their ability to interpolate data can be interpreted in terms of controllability. They have found applications in time series analysis, generative modeling, and the study of complex dynamical systems.

## Connection with residual neural networks

Neural ODEs can be interpreted as a residual neural network with a continuum of layers rather than a discrete number of layers. Applying the Euler method with a unit time step to a neural ODE yields the forward propagation equation of a residual neural network:

$\mathbf {h} _{\ell +1}=f_{\theta }(\mathbf {h} _{\ell },\ell )+\mathbf {h} _{\ell },$

with ℓ being the ℓ-th layer of this residual neural network. While the forward propagation of a residual neural network is done by applying a sequence of transformations starting at the input layer, the forward propagation computation of a neural ODE is done by solving a differential equation. More precisely, the output $\mathbf {h} _{\text{out}}$ associated to the input $\mathbf {h} _{\text{in}}$ of the neural ODE is obtained by solving the initial value problem

${\frac {\mathrm {d} \mathbf {h} (t)}{\mathrm {d} t}}=f_{\theta }(\mathbf {h} (t),t),\quad \mathbf {h} (0)=\mathbf {h} _{\text{in}},$

and assigning the value $\mathbf {h} (T)$ to $\mathbf {h} _{\text{out}}$ .

## Universal differential equations

In physics-informed contexts where additional information is known, neural ODEs can be combined with an existing first-principles model to build a physics-informed neural network model called universal differential equations (UDE). For instance, an UDE version of the Lotka-Volterra model can be written as

${\begin{aligned}{\frac {dx}{dt}}&=\alpha x-\beta xy+f_{\theta }(x(t),y(t)),\\{\frac {dy}{dt}}&=-\gamma y+\delta xy+g_{\theta }(x(t),y(t)),\end{aligned}}$

where the terms $f_{\theta }$ and $g_{\theta }$ are correction terms parametrized by neural networks.
