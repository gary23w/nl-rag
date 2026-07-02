---
title: "Runge–Kutta method (SDE)"
source: https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_method_(SDE)
domain: stochastic-differential-equations
license: CC-BY-SA-4.0
tags: stochastic differential equation, euler-maruyama method, milstein method, langevin equation
fetched: 2026-07-02
---

# Runge–Kutta method (SDE)

In mathematics of stochastic systems, the **Runge–Kutta method** is a technique for the approximate numerical solution of a stochastic differential equation. It is a generalisation of the Runge–Kutta method for ordinary differential equations to stochastic differential equations (SDEs). Importantly, the method does not involve knowing derivatives of the coefficient functions in the SDEs.

## Most basic scheme

Consider the Itō diffusion X satisfying the following Itō stochastic differential equation $dX_{t}=a(X_{t})\,dt+b(X_{t})\,dW_{t},$ with initial condition $X_{0}=x_{0}$ , where $W_{t}$ stands for the Wiener process, and suppose that we wish to solve this SDE on some interval of time $[0,T]$ . Then the basic **Runge–Kutta approximation** to the true solution X is the Markov chain Y defined as follows:

- partition the interval $[0,T]$ into N subintervals of width $\delta =T/N>0$ : $0=\tau _{0}<\tau _{1}<\dots <\tau _{N}=T;$
- set $Y_{0}:=x_{0}$ ;
- recursively compute $Y_{n}$ for $1\leq n\leq N$ by $Y_{n+1}:=Y_{n}+a(Y_{n})\delta +b(Y_{n})\Delta W_{n}+{\frac {1}{2}}\left(b({\hat {\Upsilon }}_{n})-b(Y_{n})\right)\left((\Delta W_{n})^{2}-\delta \right)\delta ^{-1/2},$ where $\Delta W_{n}=W_{\tau _{n+1}}-W_{\tau _{n}}$ and ${\hat {\Upsilon }}_{n}=Y_{n}+a(Y_{n})\delta +b(Y_{n})\delta ^{1/2}.$

The random variables $\Delta W_{n}$ are independent and identically distributed normal random variables with expected value zero and variance $\delta$ .

This scheme has strong order 1, meaning that the approximation error of the actual solution at a fixed time scales with the time step $\delta$ . It has also weak order 1, meaning that the error on the statistics of the solution scales with the time step $\delta$ . See the references for complete and exact statements.

The functions a and b can be time-varying without any complication. The method can be generalized to the case of several coupled equations; the principle is the same but the equations become longer.

## Variation of the Improved Euler is flexible

A newer Runge—Kutta scheme also of strong order 1 straightforwardly reduces to the improved Euler scheme for deterministic ODEs. Consider the vector stochastic process ${\vec {X}}(t)\in \mathbb {R} ^{n}$ that satisfies the general Ito SDE $d{\vec {X}}={\vec {a}}(t,{\vec {X}})\,dt+{\vec {b}}(t,{\vec {X}})\,dW,$ where drift ${\vec {a}}$ and volatility ${\vec {b}}$ are sufficiently smooth functions of their arguments. Given time step h , and given the value ${\vec {X}}(t_{k})={\vec {X}}_{k}$ , estimate ${\vec {X}}(t_{k+1})$ by ${\vec {X}}_{k+1}$ for time $t_{k+1}=t_{k}+h$ via ${\begin{array}{l}{\vec {K}}_{1}=h{\vec {a}}(t_{k},{\vec {X}}_{k})+(\Delta W_{k}-S_{k}{\sqrt {h}}){\vec {b}}(t_{k},{\vec {X}}_{k}),\\{\vec {K}}_{2}=h{\vec {a}}(t_{k+1},{\vec {X}}_{k}+{\vec {K}}_{1})+(\Delta W_{k}+S_{k}{\sqrt {h}}){\vec {b}}(t_{k+1},{\vec {X}}_{k}+{\vec {K}}_{1}),\\{\vec {X}}_{k+1}={\vec {X}}_{k}+{\frac {1}{2}}({\vec {K}}_{1}+{\vec {K}}_{2}),\end{array}}$

- where $\Delta W_{k}={\sqrt {h}}Z_{k}$ for normal random $Z_{k}\sim N(0,1)$ ;
- and where $S_{k}=\pm 1$ , each alternative chosen with probability $1/2$ .

The above describes only one time step. Repeat this time step $(t_{m}-t_{0})/h$ times in order to integrate the SDE from time $t=t_{0}$ to $t=t_{m}$ .

The scheme integrates Stratonovich SDEs to $O(h)$ provided one sets $S_{k}=0$ throughout (instead of choosing $\pm 1$ ).

## Higher order Runge-Kutta schemes

Higher-order schemes also exist, but become increasingly complex. Rößler developed many schemes for Ito SDEs, whereas Komori developed schemes for Stratonovich SDEs. Rackauckas extended these schemes to allow for adaptive-time stepping via Rejection Sampling with Memory (RSwM), resulting in orders of magnitude efficiency increases in practical biological models, along with coefficient optimization for improved stability.
