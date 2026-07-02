---
title: "Feynman–Kac formula"
source: https://en.wikipedia.org/wiki/Feynman%E2%80%93Kac_formula
domain: stochastic-calculus
license: CC-BY-SA-4.0
tags: stochastic calculus, stochastic differential equation, wiener process, feynman-kac formula
fetched: 2026-07-02
---

# Feynman–Kac formula

The **Feynman–Kac formula**, named after Richard Feynman and Mark Kac, establishes a link between parabolic partial differential equations and stochastic processes. In 1947, when Kac and Feynman were both faculty members at Cornell University, Kac attended a presentation of Feynman's and remarked that the two of them were working on the same thing from different directions. The Feynman–Kac formula resulted, which proves rigorously a real-valued analogy to Feynman's path integrals. The complex case, needed in quantum mechanics, is still an open question.

The formula offers a method of solving certain partial differential equations by simulating random paths of a stochastic process. Conversely, it can be used to compute an important class of expectations of random processes by deterministic means.

## Theorem

Consider the partial differential equation ${\frac {\partial }{\partial t}}u(x,t)+\mu (x,t){\frac {\partial }{\partial x}}u(x,t)+{\tfrac {1}{2}}\sigma ^{2}(x,t){\frac {\partial ^{2}}{\partial x^{2}}}u(x,t)-V(x,t)u(x,t)+f(x,t)=0,$ defined for all $x\in \mathbb {R}$ and $t\in [0,T]$ , subject to the terminal condition $u(x,T)=\psi (x),$ where $\mu ,\sigma ,\psi ,V,f$ are known functions, T is a parameter, and $u:\mathbb {R} \times [0,T]\to \mathbb {R}$ is the unknown function. Then the Feynman–Kac formula expresses $u(x,t)$ as a conditional expectation of a certain random variable:

$u(x,t)=\mathbb {E} \left[e^{-\int _{t}^{T}V(X_{s},s)\,\mathrm {d} s}\psi (X_{T})+\int _{t}^{T}e^{-\int _{t}^{\tau }V(X_{s},s)\,\mathrm {d} s}f(X_{\tau },\tau )\,\mathrm {d} \tau \,\,{\Bigg |}\,\,X_{t}=x\right]$

where $X_{t}$ is an Itô process satisfying the stochastic differential equation $dX_{t}=\mu (X_{t},t)\,dt+\sigma (X_{t},t)\,dW_{t},$ and $W_{t}$ is the Wiener process (also called Brownian motion).

### Intuitive interpretation

Suppose that $X_{t}$ describes the position at time t of a particle that evolves according to the diffusion process $dX_{t}=\mu (X_{t},t)\,dt+\sigma (X_{t},t)\,dW_{t}.$ Let the particle incur "cost" at a rate of $f(X_{s},s)$ at location $X_{s}$ at time s . Let it incur a final cost at time T of $\psi (X_{T})$ .

Also, allow the particle to decay. If the particle is at location $X_{s}$ at time s , then it decays with rate $V(X_{s},s)$ . After the particle has decayed away, all future cost is zero.

Then $u(x,t)$ is the expected cost-to-go, if the particle starts at $(t,X_{t}=x).$

## Partial proof

A proof that the above expected-value formula is a solution of the differential equation is long, difficult and not presented here. It is however reasonably straightforward to show that, *if a solution exists*, it must have the above form. The proof of that lesser result is as follows:

### Derivation

Assume that $u(x,t)$ satisfies the PDE:

${\frac {\partial u}{\partial t}}+\mu {\frac {\partial u}{\partial x}}+{\frac {1}{2}}\sigma ^{2}{\frac {\partial ^{2}u}{\partial x^{2}}}-Vu+f=0$

with terminal condition $u(x,T)=\psi (x).$ Further let $X_{t}$ be a stochastic process as defined above.

Let $g(t,s)=e^{-\int _{t}^{s}V(X_{r},r)dr}$ . Its differential satisfies:

$dg(t,s)=-V(X_{s},s)g(t,s)\,ds.$

Define the stochastic process:

$Y_{s}=g(t,s)u(X_{s},s)+\int _{t}^{s}g(t,\tau )f(X_{\tau },\tau )\,d\tau$

for $s\in [t,T]$ . At boundary times:

$Y_{t}=u(X_{t},t),\quad Y_{T}=g(t,T)\psi (X_{T})+\int _{t}^{T}g(t,\tau )f(X_{\tau },\tau )\,d\tau .$

If $Y_{s}$ is a martingale, then we have

$u(x,t)=\mathbb {E} [Y_{T}\mid Y_{t}=u(x,t)]=\mathbb {E} [Y_{T}\mid X_{t}=x]$

which is what we want to show. So we just need to prove $Y_{s}$ is a martingale.

We assume $X_{s}$ follows the SDE

$dX_{s}=\mu (X_{s},s)\,ds+\sigma (X_{s},s)\,dW_{s}.$

By Itô's lemma:

$du(X_{s},s)=\left({\frac {\partial u}{\partial s}}+\mu {\frac {\partial u}{\partial x}}+{\frac {1}{2}}\sigma ^{2}{\frac {\partial ^{2}u}{\partial x^{2}}}\right)ds+\sigma {\frac {\partial u}{\partial x}}dW_{s}.$

Differentiate $Y_{s}$ :

$dY_{s}=d\left[g(t,s)u(X_{s},s)\right]+g(t,s)f(X_{s},s)\,ds.$

Expand $d[gu]$ :

$d[gu]=g\,du+u\,dg+\underbrace {d[g,u]} _{=0}.$

Substitute $dg=-Vg\,ds$ and $du$ :

$d[gu]=g\left({\frac {\partial u}{\partial s}}+\mu {\frac {\partial u}{\partial x}}+{\frac {1}{2}}\sigma ^{2}{\frac {\partial ^{2}u}{\partial x^{2}}}\right)ds$

$\qquad \quad +\;g\sigma {\frac {\partial u}{\partial x}}\,dW_{s}\;-\;Vgu\,ds.$

Add the integral term:

$dY_{s}=\left[g\left({\frac {\partial u}{\partial s}}+\mu {\frac {\partial u}{\partial x}}+{\frac {1}{2}}\sigma ^{2}{\frac {\partial ^{2}u}{\partial x^{2}}}\right)-Vgu+gf\right]ds+g\sigma {\frac {\partial u}{\partial x}}dW_{s}.$

For $Y_{s}$ to be a martingale, the drift term must vanish:

${\frac {\partial u}{\partial s}}+\mu {\frac {\partial u}{\partial x}}+{\frac {1}{2}}\sigma ^{2}{\frac {\partial ^{2}u}{\partial x^{2}}}-Vu+f=0.$

### Remarks

- The proof above that a solution must have the given form is essentially that of with modifications to account for $f(x,t)$ .
- The expectation formula above is also valid for *N*-dimensional Itô diffusions. The corresponding partial differential equation for $u:\mathbb {R} ^{N}\times [0,T]\to \mathbb {R}$ becomes: ${\frac {\partial u}{\partial t}}+\sum _{i=1}^{N}\mu _{i}(x,t){\frac {\partial u}{\partial x_{i}}}+{\frac {1}{2}}\sum _{i=1}^{N}\sum _{j=1}^{N}\gamma _{ij}(x,t){\frac {\partial ^{2}u}{\partial x_{i}\partial x_{j}}}-r(x,t)\,u=f(x,t),$ where, $\gamma _{ij}(x,t)=\sum _{k=1}^{N}\sigma _{ik}(x,t)\sigma _{jk}(x,t),$ i.e. $\gamma =\sigma \sigma ^{\mathrm {T} }$ , where $\sigma ^{\mathrm {T} }$ denotes the transpose of $\sigma$ .
- More succinctly, letting A be the infinitesimal generator of the diffusion process, ${\frac {\partial u}{\partial t}}+Au-r(x,t)\,u=f(x,t).$
- This expectation can then be approximated using Monte Carlo or quasi-Monte Carlo methods.

## Original formulation about Wiener functionals

When originally published by Kac in 1949, the formula was presented as a means for determining the distribution of certain Wiener functionals. Suppose we wish to find the expected value of the function $\exp \left(-\int _{0}^{t}V(x(\tau ))\,d\tau \right)$ in the case where *x*(*t*) is some realization of a diffusion process starting at *x*(0) = 0. The Feynman–Kac formula says that this expectation is equivalent to the integral of a solution to a corresponding diffusion equation. Specifically, under the conditions that $V(x)\geq 0$ , $\mathbb {E} \left[\exp \left(-\int _{0}^{t}V(x(\tau ))\,d\tau \right)\right]=\int _{-\infty }^{\infty }w(x,t)\,dx$ where *w*(*x*, *t*) is the solution to the parabolic partial differential equation ${\frac {\partial w}{\partial t}}={\frac {1}{2}}{\frac {\partial ^{2}w}{\partial x^{2}}}-V(x)w$ with initial condition *w*(*x*, 0) = *δ*(*x*).

The Feynman–Kac formula can also be used to evaluate functional integrals of a certain form. If, for example, $I=\int f(x(0))\exp \left(-\int _{0}^{t}V(x(\tau ))\,d\tau \right)g(x(t))\,Dx$ where the notation $Dx$ refers to integration taken over all random walks $x:[0,t]\to \mathbb {R}$ , then $I=\int _{-\infty }^{\infty }w(x,t)g(x)\,dx$ where *w*(*x*, *t*) is the solution to ${\frac {\partial w}{\partial t}}={\frac {1}{2}}{\frac {\partial ^{2}w}{\partial x^{2}}}-V(x)w$ with initial condition *w*(*x*, 0) = *f*(*x*).

## Example

In practical applications, the Feynman–Kac formula can be used with numerical methods like Euler-Maruyama to numerically approximate solutions to partial differential equations. For instance, it can be applied to the convection–diffusion partial differential equation (PDE):

${\frac {\partial }{\partial t}}u(x,t)+b{\frac {\partial }{\partial x}}u(x,t)=-\sigma ^{2}{\frac {\partial ^{2}}{\partial x^{2}}}u(x,t)$

Consider the convection–diffusion PDE with parameters $b=1$ , $\sigma =1$ and terminal condition $u(x,T)=e^{-x^{2}}$ with $T=1$ . Then the PDE can be solved analytically:

$u(x,t)={\frac {1}{\sqrt {5-4t}}}\exp \left(-{\frac {(1-t+x)^{2}}{5-4t}}\right)$

Applying the Feynman-Kac formula, the solution can also be written as the conditional expectation:

$u(x,t)=\mathbb {E} \left[e^{-X_{T}^{2}}\,{\bigl |}\,X_{t}=x\right]$

where X is an Itô process governed by the SDE $dX_{t}=dt+{\sqrt {2}}dW_{t}$ and $W_{t}$ is a Wiener process. Then using the Euler-Maruyama method, the SDE can be numerically integrated forwards in time from the initial condition $(x_{0},t_{0})$ till the terminal time $T,$ yielding simulated values of $X_{T}$ . To approximate the expectation in the Feynman-Kac method, the simulation is repeated N times. These are often called realizations. The solution is then estimated by the Monte Carlo average

$u(x_{0},t_{0})\approx {\frac {1}{N}}\sum _{i=1}^{N}\exp \left(-\left(X_{T}^{(i)}\right)^{2}\right)$

The figure below compares the analytical solution with the numerical approximation obtained using the Euler–Maruyama method with $N=1000$ . The left-hand plots show vertical slices of the gradient plot on the right, with each vertical line on the surface corresponding to a colored curve on the left. While the numerical solution exhibits some noise, it closely follows the shape of the exact solution. Increasing the number of simulations N or decreasing the Euler–Maruyama time step improves the accuracy and reduces the variance of the approximation.

This example illustrates how stochastic simulation, enabled by the Feynman–Kac formula and numerical methods like Euler–Maruyama, can approximate PDE solutions. In practice, such stochastic approaches are especially valuable when dealing with high-dimensional systems or complex geometries where traditional PDE solvers become computationally prohibitive. One key advantage of the SDE-based method is its natural parallelism—each simulation, or realization, can be computed independently—making it well-suited for high-performance computing environments. While stochastic simulations introduce variance, this can be mitigated by increasing the number of realizations or refining the time discretization. Thus, stochastic differential equations provide a flexible and scalable alternative to deterministic PDE solvers, particularly in contexts where uncertainty is intrinsic or dimensionality poses a computational barrier. In contrast to traditional PDE solvers, which typically require solving for the entire solution over a grid, this method enables direct computation at specific points in space and time. This targeted approach allows computational resources to be focused on regions of interest, potentially resulting in substantial efficiency gains.

## Applications

### Finance

In quantitative finance, the Feynman–Kac formula is used to efficiently calculate solutions to the Black–Scholes equation to price options on stocks and zero-coupon bond prices in affine term structure models.

For example, consider a stock price $S_{t}$ undergoing geometric Brownian motion $dS_{t}=\left(r_{t}dt+\sigma _{t}dW_{t}\right)S_{t}$ where $r_{t}$ is the risk-free interest rate and $\sigma _{t}$ is the volatility. Equivalently, by Itô's lemma, $d\ln S_{t}=\left(r_{t}-{\tfrac {1}{2}}\sigma _{t}^{2}\right)dt+\sigma _{t}\,dW_{t}.$ Now consider a European call option on an $S_{t}$ expiring at time T with strike K . At expiry, it is worth $(X_{T}-K)^{+}.$ Then, the risk-neutral price of the option, at time t and stock price x , is $u(x,t)=\operatorname {E} \left[e^{-\int _{t}^{T}r_{s}ds}(S_{T}-K)^{+}|\ln S_{t}=\ln x\right].$ Plugging into the Feynman–Kac formula, we obtain the Black–Scholes equation: ${\begin{cases}\partial _{t}u+Au-r_{t}u=0\\u(x,T)=(x-K)^{+}\end{cases}}$ where ${\textstyle A=(r_{t}-\sigma _{t}^{2}/2)\partial _{\ln x}+{\frac {1}{2}}\sigma _{t}^{2}\partial _{\ln x}^{2}=r_{t}x\partial _{x}+{\frac {1}{2}}\sigma _{t}^{2}x^{2}\partial _{x}^{2}.}$ More generally, consider an option expiring at time T with payoff $g(S_{T})$ . The same calculation shows that its price $u(x,t)$ satisfies ${\begin{cases}\partial _{t}u+Au-r_{t}u=0\\u(x,T)=g(x).\end{cases}}$ Some other options like the American option do not have a fixed expiry. Some options have value at expiry determined by the past stock prices. For example, an **average option** has a payoff that is not determined by the underlying price at expiry but by the average underlying price over some predetermined period of time. For these, the Feynman–Kac formula does not directly apply.

### Quantum mechanics

In quantum chemistry, it is used to solve the Schrödinger equation with the pure diffusion Monte Carlo method.
