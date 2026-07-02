---
title: "Euler–Maruyama method"
source: https://en.wikipedia.org/wiki/Euler%E2%80%93Maruyama_method
domain: stochastic-differential-equations
license: CC-BY-SA-4.0
tags: stochastic differential equation, euler-maruyama method, milstein method, langevin equation
fetched: 2026-07-02
---

# Euler–Maruyama method

In Itô calculus, the **Euler–Maruyama method** (also simply called the **Euler method**) is a method for the approximate numerical solution of a stochastic differential equation (SDE). It is an extension of the Euler method for ordinary differential equations to stochastic differential equations named after Leonhard Euler and Gisiro Maruyama. The same generalization cannot be done for any arbitrary deterministic method.

## Definition

Consider the stochastic differential equation (see Itô calculus)

$\mathrm {d} X_{t}=a(X_{t},t)\,\mathrm {d} t+b(X_{t},t)\,\mathrm {d} W_{t},$

with initial condition *X*0 = *x*0, where *W**t* denotes the Wiener process, and suppose that we wish to solve this SDE on some interval of time [0, *T*]. Then the **Euler–Maruyama approximation** to the true solution *X* is the Markov chain *Y* defined as follows:

- Partition the interval [0, *T*] into *N* equal subintervals of width $\Delta t>0$ :

$0=\tau _{0}<\tau _{1}<\cdots <\tau _{N}=T{\text{ and }}\Delta t=T/N;$

- Set *Y*0 = *x*0
- Recursively define *Y**n* for 0 ≤ *n* ≤ *N-1* by

$\,Y_{n+1}=Y_{n}+a(Y_{n},\tau _{n})\,\Delta t+b(Y_{n},\tau _{n})\,\Delta W_{n},$

where

$\Delta W_{n}=W_{\tau _{n+1}}-W_{\tau _{n}}.$

The random variables Δ*W**n* are independent and identically distributed normal random variables with expected value zero and variance Δ*t*.

### Derivation

The Euler-Maruyama formula can be derived by considering the integral form of the Itô SDE

$X_{\tau _{n+1}}=X_{\tau _{n}}+\int _{\tau _{n}}^{\tau _{n+1}}a(X_{s},s)\,ds+\int _{\tau _{n}}^{\tau _{n+1}}b(X_{s},s)\,dW_{s}$

and approximating $a(X_{s},s)\approx a(X_{n},\tau _{n})$ and $b(X_{s},s)\approx b(X_{n},\tau _{n})$ on the small time interval $[\tau _{n},\tau _{n+1}]$ .

## Strong and weak convergence

Like other approximation methods, the accuracy of the Euler–Maruyama scheme is analyzed through comparison to an underlying continuous solution. Let X denote an Itô process over $[0,T]$ , equal to

$X_{t}=X_{0}+\int _{0}^{t}\mu (s,X_{s})ds+\int _{0}^{t}\sigma (s,X_{s})dW_{s}$

at time $t\in [0,T]$ , where $\mu$ and $\sigma$ denote deterministic "drift" and "diffusion" functions, respectively, and $W_{t}$ is the Wiener process. As discrete approximations of continuous processes are typically assessed through comparison between their respective final states at $T>0$ , a natural convergence criterion for such discrete processes is

$\lim _{N\to \infty }\mathbb {E} \left[\left|{\hat {X}}_{N}-X_{T}\right|\right]=0.$

Here, ${\hat {X}}_{N}$ corresponds to the final state of the discrete process ${\hat {X}}$ , which approximates $X_{T}$ by taking N steps of length $\Delta t=T/N$ . Iterative schemes satisfying the above condition are said to strongly converge to the continuous process X , which automatically implies their satisfaction of the weak convergence criterion,

$\lim _{N\to \infty }\left|\mathbb {E} \left[g({\hat {X}}_{N})\right]-\left[g(X_{T})\right]\right|=0,$

for any bounded and continuous function g . More specifically, if there exists a constant K and $\gamma _{s},\delta _{0}>0$ such that

$\mathbb {E} \left[\left|{\hat {X}}_{N}-X_{T}\right|\right]\leq K\delta _{0}^{\gamma _{s}}$

for any $\delta \in (0,\delta _{0})$ , the approximation converges strongly with order $\gamma _{s}$ to the continuous process X ; likewise, ${\hat {X}}$ converges weakly to X with order $\gamma _{w}$ if the same inequality holds for the expectation of $g({\hat {X}}_{N})-g(X_{T})$ . Strong order $\gamma _{s}$ convergence implies weak order $\gamma _{w}\geq \gamma _{s}$ convergence: exemplifying this, it was shown in 1972 that the Euler–Maruyama method strongly converges with order $\gamma _{s}=1/2$ to any Itô process, provided $\mu ,\sigma$ satisfy Lipschitz continuity and linear growth conditions with respect to x , and in 1974, the Euler–Maruyama scheme was proven to converge weakly with order $\gamma _{w}=1$ to Itô processes governed by the same such $\mu ,\sigma$ , provided that their derivatives also satisfy similar conditions.

## Example with geometric Brownian motion

A simple case to analyze is geometric Brownian motion, which satisfies the SDE

$dX_{t}=\lambda X_{t}\,dt+\sigma X_{t}\,dW_{t}$

for fixed $\lambda$ and $\sigma$ . Applying Itô’s lemma to $\ln X_{t}$ yields the closed-form solution

$X_{t}=X_{0}\exp \left(\left(\lambda -{\tfrac {1}{2}}\sigma ^{2}\right)t+\sigma W_{t}\right)$

Discretising with Euler–Maruyama gives the time-step updates

$Y_{n+1}=\left(1+\lambda \Delta t+\sigma \Delta W_{n}\right)Y_{n}=Y_{0}\prod _{k=0}^{n}\left(1+\lambda \Delta t+\sigma \Delta W_{k}\right)$

By using a Taylor series expansion of the exponential function in the analytic solution, we can get a formula for the exact update in a time-step.

${\begin{aligned}X_{\tau _{k+1}}&=X_{\tau _{k}}\exp \left((\lambda -{\tfrac {1}{2}}\sigma ^{2})\Delta t+\sigma \Delta W_{k}\right)\\&=X_{\tau _{k}}\left[1+\lambda \Delta t+\sigma \Delta W_{k}+{\tfrac {1}{2}}\sigma ^{2}\left((\Delta W_{k})^{2}-\Delta t\right)+O\left(\Delta t^{3/2}\right)\right]\\\end{aligned}}$

Summing the local errors between the analytic and Euler-Maruyama solutions over each of the $N=T/\Delta t$ steps gives the strong error estimate

$\mathbb {E} \left[\,|X_{T}-Y_{N}|\,\right]=O\left({\sqrt {\Delta t}}\right)$

confirming strong order $1/2$ convergence.

Another numerical aspect to consider is stability. The path's second moment is $\mathbb {E} |X_{t}|^{2}\propto \exp \left((2\lambda +\sigma ^{2})t\right)$ , so long-time decay of the solution occurs only when $2\lambda +\sigma ^{2}<0$ . The Euler–Maruyama scheme preserves variance decay in this case provided that $\Delta t\leq {\frac {-1}{\lambda ^{2}}}\left(2\lambda +\sigma ^{2}\right)$ .

## Application

An area that has benefited significantly from SDEs is mathematical biology. As many biological processes are both stochastic and continuous in nature, numerical methods of solving SDEs are highly valuable in the field.
