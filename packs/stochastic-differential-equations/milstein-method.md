---
title: "Milstein method"
source: https://en.wikipedia.org/wiki/Milstein_method
domain: stochastic-differential-equations
license: CC-BY-SA-4.0
tags: stochastic differential equation, euler-maruyama method, milstein method, langevin equation
fetched: 2026-07-02
---

# Milstein method

In mathematics, the **Milstein method** is a technique for the approximate numerical solution of a stochastic differential equation. It is named after Grigori Milstein who first published it in 1974.

## Description

Consider the autonomous Itō stochastic differential equation: $\mathrm {d} X_{t}=a(X_{t})\,\mathrm {d} t+b(X_{t})\,\mathrm {d} W_{t}$ with initial condition $X_{0}=x_{0}$ , where $W_{t}$ denotes the Wiener process, and suppose that we wish to solve this SDE on some interval of time  $[0,T]$ . Then the **Milstein approximation** to the true solution X is the Markov chain Y defined as follows:

- Partition the interval $[0,T]$ into N equal subintervals of width $\Delta t>0$ : $0=\tau _{0}<\tau _{1}<\dots <\tau _{N}=T{\text{ with }}\tau _{n}:=n\Delta t{\text{ and }}\Delta t={\frac {T}{N}}$
- Set $Y_{0}=x_{0};$
- Recursively define $Y_{n}$ for $1\leq n\leq N$ by: $Y_{n+1}=Y_{n}+a(Y_{n})\Delta t+b(Y_{n})\Delta W_{n}+{\frac {1}{2}}b(Y_{n})b'(Y_{n})\left((\Delta W_{n})^{2}-\Delta t\right)$ where $b'$ denotes the derivative of $b(x)$ with respect to x and: $\Delta W_{n}=W_{\tau _{n+1}}-W_{\tau _{n}}$ are independent and identically distributed normal random variables with expected value zero and variance $\Delta t$ . Then $Y_{n}$ will approximate $X_{\tau _{n}}$ for $0\leq n\leq N$ , and increasing N will yield a better approximation.

Note that when $b'(Y_{n})=0$ (i.e. the diffusion term does not depend on $X_{t}$ ) this method is equivalent to the Euler–Maruyama method.

The Milstein scheme has both weak and strong order of convergence $\Delta t$ which is superior to the Euler–Maruyama method, which in turn has the same weak order of convergence $\Delta t$ but inferior strong order of convergence ${\sqrt {\Delta t}}$ .

## Intuitive derivation

For this derivation, we will only look at geometric Brownian motion (GBM), the stochastic differential equation of which is given by: $\mathrm {d} X_{t}=\mu X\mathrm {d} t+\sigma XdW_{t}$ with real constants $\mu$ and $\sigma$ . Using Itō's lemma we get: $\mathrm {d} \ln X_{t}=\left(\mu -{\frac {1}{2}}\sigma ^{2}\right)\mathrm {d} t+\sigma \mathrm {d} W_{t}$

Thus, the solution to the GBM SDE is: ${\begin{aligned}X_{t+\Delta t}&=X_{t}\exp \left\{\int _{t}^{t+\Delta t}\left(\mu -{\frac {1}{2}}\sigma ^{2}\right)\mathrm {d} t+\int _{t}^{t+\Delta t}\sigma \mathrm {d} W_{u}\right\}\\&\approx X_{t}\left(1+\mu \Delta t-{\frac {1}{2}}\sigma ^{2}\Delta t+\sigma \Delta W_{t}+{\frac {1}{2}}\sigma ^{2}(\Delta W_{t})^{2}\right)\\&=X_{t}+a(X_{t})\Delta t+b(X_{t})\Delta W_{t}+{\frac {1}{2}}b(X_{t})b'(X_{t})((\Delta W_{t})^{2}-\Delta t)\end{aligned}}$ where $a(x)=\mu x,~b(x)=\sigma x$

The numerical solution is presented in the graphic for three different trajectories.

### Computer implementation

The following Python code implements the Milstein method and uses it to solve the SDE describing geometric Brownian motion defined by ${\begin{cases}dY_{t}=\mu Y\,{\mathrm {d} }t+\sigma Y\,{\mathrm {d} }W_{t}\\Y_{0}=Y_{\text{init}}\end{cases}}$

```mw
# -*- coding: utf-8 -*-
# Milstein Method

import numpy as np
import matplotlib.pyplot as plt

class Model:
    """Stochastic model constants."""
    mu = 3
    sigma = 1

def dW(dt):
    """Random sample normal distribution."""
    return np.random.normal(loc=0.0, scale=np.sqrt(dt))

def run_simulation():
    """ Return the result of one full simulation."""
    # One second and thousand grid points
    T_INIT = 0
    T_END = 1
    N = 1000 # Compute 1000 grid points
    DT = float(T_END - T_INIT) / N
    TS = np.arange(T_INIT, T_END + DT, DT)

    Y_INIT = 1

    # Vectors to fill
    ys = np.zeros(N + 1)
    ys[0] = Y_INIT
    for i in range(1, TS.size):
        t = (i - 1) * DT
        y = ys[i - 1]
        dw = dW(DT)

        # Sum up terms as in the Milstein method
        ys[i] = y + \
            Model.mu * y * DT + \
            Model.sigma * y * dw + \
            (Model.sigma**2 / 2) * y * (dw**2 - DT)

    return TS, ys

def plot_simulations(num_sims: int):
    """Plot several simulations in one image."""
    for _ in range(num_sims):
        plt.plot(*run_simulation())

    plt.xlabel("time (s)")
    plt.ylabel("y")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    NUM_SIMS = 2
    plot_simulations(NUM_SIMS)
```
