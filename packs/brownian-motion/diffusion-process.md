---
title: "Diffusion process"
source: https://en.wikipedia.org/wiki/Diffusion_process
domain: brownian-motion
license: CC-BY-SA-4.0
tags: brownian motion, diffusion process, fokker-planck equation, ornstein-uhlenbeck process
fetched: 2026-07-02
---

# Diffusion process

In probability theory and statistics, **diffusion processes** are a class of continuous-time Markov process with almost surely continuous sample paths. Diffusion processes are stochastic in nature and hence are used to model many real-life stochastic systems. Brownian motion, reflected Brownian motion and Ornstein–Uhlenbeck processes are examples of diffusion processes. It is used heavily in statistical physics, statistical analysis, information theory, data science, neural networks, finance and marketing.

A sample path of a diffusion process models the trajectory of a particle embedded in a flowing fluid and subjected to random displacements due to collisions with other particles, which is called Brownian motion. The position of the particle is then random; its probability density function as a function of space and time is governed by a convection–diffusion equation.

## Mathematical definition

A *diffusion process* is a Markov process with continuous sample paths for which the Kolmogorov forward equation is the Fokker–Planck equation.

A diffusion process is defined by the following properties. Let $a^{ij}(x,t)$ be uniformly continuous coefficients and $b^{i}(x,t)$ be bounded, Borel measurable drift terms. There is a unique family of probability measures $\mathbb {P} _{a;b}^{\xi ,\tau }$ (for $\tau \geq 0$ , $\xi \in \mathbb {R} ^{d}$ ) on the canonical space $\Omega =C([0,\infty ),\mathbb {R} ^{d})$ , with its Borel $\sigma$ -algebra, such that:

1. (Initial Condition) The process starts at $\xi$ at time $\tau$ : $\mathbb {P} _{a;b}^{\xi ,\tau }[\psi \in \Omega :\psi (t)=\xi {\text{ for }}0\leq t\leq \tau ]=1.$

2. (Local Martingale Property) For every $f\in C^{2,1}(\mathbb {R} ^{d}\times [\tau ,\infty ))$ , the process

$M_{t}^{[f]}=f(\psi (t),t)-f(\psi (\tau ),\tau )-\int _{\tau }^{t}{\bigl (}L_{a;b}+{\tfrac {\partial }{\partial s}}{\bigr )}f(\psi (s),s)\,ds$ is a local martingale under $\mathbb {P} _{a;b}^{\xi ,\tau }$ for $t\geq \tau$ , with $M_{t}^{[f]}=0$ for $t\leq \tau$ .

This family $\mathbb {P} _{a;b}^{\xi ,\tau }$ is called the ${\mathcal {L}}_{a;b}$ -diffusion.

## SDE Construction and Infinitesimal Generator

It is clear that if we have an ${\mathcal {L}}_{a;b}$ -diffusion, i.e. $(X_{t})_{t\geq 0}$ on $(\Omega ,{\mathcal {F}},{\mathcal {F}}_{t},\mathbb {P} _{a;b}^{\xi ,\tau })$ , then $X_{t}$ satisfies the SDE $dX_{t}^{i}={\frac {1}{2}}\,\sum _{k=1}^{d}\sigma _{k}^{i}(X_{t})\,dB_{t}^{k}+b^{i}(X_{t})\,dt$ . In contrast, one can construct this diffusion from that SDE if $a^{ij}(x,t)=\sum _{k}\sigma _{i}^{k}(x,t)\,\sigma _{j}^{k}(x,t)$ and $\sigma ^{ij}(x,t)$ , $b^{i}(x,t)$ are Lipschitz continuous. To see this, let $X_{t}$ solve the SDE starting at $X_{\tau }=\xi$ . For $f\in C^{2,1}(\mathbb {R} ^{d}\times [\tau ,\infty ))$ , apply Itô's formula: $df(X_{t},t)={\bigl (}{\frac {\partial f}{\partial t}}+\sum _{i=1}^{d}b^{i}{\frac {\partial f}{\partial x_{i}}}+v\sum _{i,j=1}^{d}a^{ij}\,{\frac {\partial ^{2}f}{\partial x_{i}\partial x_{j}}}{\bigr )}\,dt+\sum _{i,k=1}^{d}{\frac {\partial f}{\partial x_{i}}}\,\sigma _{k}^{i}\,dB_{t}^{k}.$ Rearranging gives $f(X_{t},t)-f(X_{\tau },\tau )-\int _{\tau }^{t}{\bigl (}{\frac {\partial f}{\partial s}}+L_{a;b}f{\bigr )}\,ds=\int _{\tau }^{t}\sum _{i,k=1}^{d}{\frac {\partial f}{\partial x_{i}}}\,\sigma _{k}^{i}\,dB_{s}^{k},$ whose right‐hand side is a local martingale, matching the local‐martingale property in the diffusion definition. The law of $X_{t}$ defines $\mathbb {P} _{a;b}^{\xi ,\tau }$ on $\Omega =C([0,\infty ),\mathbb {R} ^{d})$ with the correct initial condition and local martingale property. Uniqueness follows from the Lipschitz continuity of $\sigma \!,\!b$ . In fact, $L_{a;b}+{\tfrac {\partial }{\partial s}}$ coincides with the infinitesimal generator ${\mathcal {A}}$ of this process. If $X_{t}$ solves the SDE, then for $f(\mathbf {x} ,t)\in C^{2}(\mathbb {R} ^{d}\times \mathbb {R} ^{+})$ , the generator ${\mathcal {A}}$ is ${\mathcal {A}}f(\mathbf {x} ,t)=\sum _{i=1}^{d}b_{i}(\mathbf {x} ,t)\,{\frac {\partial f}{\partial x_{i}}}+v\sum _{i,j=1}^{d}a_{ij}(\mathbf {x} ,t)\,{\frac {\partial ^{2}f}{\partial x_{i}\partial x_{j}}}+{\frac {\partial f}{\partial t}}.$
