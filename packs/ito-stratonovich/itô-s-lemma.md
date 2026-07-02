---
title: "Itô's lemma"
source: https://en.wikipedia.org/wiki/It%C3%B4%27s_lemma
domain: ito-stratonovich
license: CC-BY-SA-4.0
tags: ito calculus, stratonovich integral, quadratic variation, wiener process
fetched: 2026-07-02
---

# Itô's lemma

In mathematics, **Itô's lemma** or **Itô's formula** (also called the **Itô–Doeblin formula**) is an identity used in Itô calculus to find the differential of a time-dependent function of a stochastic process. It serves as the stochastic calculus counterpart of the chain rule. It can be heuristically derived by forming the Taylor series expansion of the function up to its second derivatives and retaining terms up to first order in the time increment and second order in the Wiener process increment. The lemma is widely employed in mathematical finance, and its best known application is in the derivation of the Black–Scholes equation for option values.

This result was discovered by Japanese mathematician Kiyoshi Itô in 1951.

## Motivation

Suppose we are given the stochastic differential equation $dX_{t}=\mu _{t}\ dt+\sigma _{t}\ dB_{t},$ where *B**t* is a Wiener process and the functions $\mu _{t},\sigma _{t}$ are deterministic (not stochastic) functions of time. In general, it's not possible to write a solution $X_{t}$ directly in terms of $B_{t}.$ However, we can formally write an integral solution $X_{t}=\int _{0}^{t}\mu _{s}\ ds+\int _{0}^{t}\sigma _{s}\ dB_{s}.$

This expression lets us easily read off the mean and variance of $X_{t}$ (which has no higher moments). First, notice that every $\mathrm {d} B_{t}$ individually has mean 0, so the expected value of $X_{t}$ is simply the integral of the drift function: $\mathrm {E} [X_{t}]=\int _{0}^{t}\mu _{s}\ ds.$

Similarly, because the $dB$ terms have variance 1 and no correlation with one another, the variance of $X_{t}$ is simply the integral of the variance of each infinitesimal step in the random walk: $\mathrm {Var} [X_{t}]=\int _{0}^{t}\sigma _{s}^{2}\ ds.$

However, sometimes we are faced with a stochastic differential equation for a more complex process $Y_{t},$ in which the process appears on both sides of the differential equation. That is, say $dY_{t}=a_{1}(Y_{t},t)\ dt+a_{2}(Y_{t},t)\ dB_{t},$ for some functions $a_{1}$ and $a_{2}.$ In this case, we cannot immediately write a formal solution as we did for the simpler case above. Instead, we hope to write the process $Y_{t}$ as a function of a simpler process $X_{t}$ taking the form above. That is, we want to identify three functions $f(t,x),\mu _{t},$ and $\sigma _{t},$ such that $Y_{t}=f(t,X_{t})$ and $dX_{t}=\mu _{t}\ dt+\sigma _{t}\ dB_{t}.$ In practice, Ito's lemma is used in order to find this transformation. Finally, once we have transformed the problem into the simpler type of problem, we can determine the mean and higher moments of the process.

## Derivation

We derive Itô's lemma by expanding a Taylor series and applying the rules of stochastic calculus.

Suppose $X_{t}$ is an Itô drift-diffusion process that satisfies the stochastic differential equation

$dX_{t}=\mu _{t}\,dt+\sigma _{t}\,dB_{t},$

where *B**t* is a Wiener process.

If *f*(*t*,*x*) is a twice-differentiable scalar function, its expansion in a Taylor series is

${\begin{aligned}{\frac {\Delta f(t)}{dt}}dt&=f(t+dt,x)-f(t,x)\\&={\frac {\partial f}{\partial t}}\,dt+{\frac {1}{2}}{\frac {\partial ^{2}f}{\partial t^{2}}}\,(dt)^{2}+\cdots \\[1ex]{\frac {\Delta f(x)}{dx}}dx&=f(t,x+dx)-f(t,x)\\&={\frac {\partial f}{\partial x}}\,dx+{\frac {1}{2}}{\frac {\partial ^{2}f}{\partial x^{2}}}\,(dx)^{2}+\cdots \end{aligned}}$

Then use the total derivative and the definition of the partial derivative $f_{y}=\lim _{dy\to 0}{\frac {\Delta f(y)}{dy}}$ :

${\begin{aligned}df&=f_{t}dt+f_{x}dx\\[1ex]&=\lim _{dx\to 0 \atop dt\to 0}{\frac {\partial f}{\partial t}}\,dt+{\frac {\partial f}{\partial x}}\,dx+{\frac {1}{2}}\left({\frac {\partial ^{2}f}{\partial t^{2}}}\,(dt)^{2}+{\frac {\partial ^{2}f}{\partial x^{2}}}\,(dx)^{2}\right)+\cdots .\end{aligned}}$

Substituting $x=X_{t}$ and therefore $dx=dX_{t}=\mu _{t}\,dt+\sigma _{t}\,dB_{t}$ , we get

${\begin{aligned}df=\lim _{dB_{t}\to 0 \atop dt\to 0}\;&{\frac {\partial f}{\partial t}}\,dt+{\frac {\partial f}{\partial x}}\left(\mu _{t}\,dt+\sigma _{t}\,dB_{t}\right)\\&+{\frac {1}{2}}\left[{\frac {\partial ^{2}f}{\partial t^{2}}}\,{\left(dt\right)}^{2}+{\frac {\partial ^{2}f}{\partial x^{2}}}\left(\mu _{t}^{2}\,{\left(dt\right)}^{2}+2\mu _{t}\sigma _{t}\,dt\,dB_{t}+\sigma _{t}^{2}\,{\left(dB_{t}\right)}^{2}\right)\right]+\cdots .\end{aligned}}$

In the limit $dt\to 0$ , the terms $(dt)^{2}$ and $dt\,dB_{t}$ tend to zero faster than $dt$ . $(dB_{t})^{2}$ is $O(dt)$ (due to the quadratic variation of a Wiener process which says $B_{t}^{2}=O(t)$ ), so setting $(dt)^{2},dt\,dB_{t}$ and $(dx)^{3}$ terms to zero and substituting $dt$ for $(dB_{t})^{2}$ , and then collecting the $dt$ terms, we obtain

$df=\lim _{dt\to 0}\left({\frac {\partial f}{\partial t}}+\mu _{t}{\frac {\partial f}{\partial x}}+{\frac {\sigma _{t}^{2}}{2}}{\frac {\partial ^{2}f}{\partial x^{2}}}\right)dt+\sigma _{t}{\frac {\partial f}{\partial x}}\,dB_{t}$

as required.

Alternatively,

$df=\lim _{dt\to 0}\left({\frac {\partial f}{\partial t}}+{\frac {\sigma _{t}^{2}}{2}}{\frac {\partial ^{2}f}{\partial x^{2}}}\right)dt+{\frac {\partial f}{\partial x}}\,dX_{t}$

## Geometric intuition

Suppose we know that $X_{t},X_{t+dt}$ are two jointly-Gaussian distributed random variables, and f is nonlinear but has a continuous second derivative, then in general, neither of $f(X_{t}),f(X_{t+dt})$ is Gaussian, and their joint distribution is also not Gaussian. However, since $X_{t+dt}\mid X_{t}$ is Gaussian, we might still find $f(X_{t+dt})\mid f(X_{t})$ is Gaussian. This is not true when $dt$ is finite, but when $dt$ becomes infinitesimal, this becomes true.

The key idea is that $X_{t+dt}=X_{t}+\mu _{t}\,dt+dW_{t}$ has a deterministic part and a noisy part. When f is nonlinear, the noisy part has a deterministic contribution. If f is convex, then the deterministic contribution is positive (by Jensen's inequality).

To find out how large the contribution is, we write $X_{t+dt}=X_{t}+\mu _{t}\,dt+\sigma _{t}{\sqrt {dt}}\,z$ , where z is a standard Gaussian, then perform Taylor expansion. ${\begin{aligned}f(X_{t+dt})={}&f(X_{t})+f'(X_{t})\mu _{t}\,dt+f'(X_{t})\sigma _{t}{\sqrt {dt}}\,z\\[1ex]&+{\frac {1}{2}}f''(X_{t})\left(\sigma _{t}^{2}z^{2}\,dt+2\mu _{t}\sigma _{t}z\,dt^{3/2}+\mu _{t}^{2}dt^{2}\right)+o(dt)\\[2ex]={}&\left[f(X_{t})+f'(X_{t})\mu _{t}\,dt+{\frac {1}{2}}f''(X_{t})\sigma _{t}^{2}\,dt+o(dt)\right]\\[1ex]&+\left[f'(X_{t})\sigma _{t}{\sqrt {dt}}\,z+{\frac {1}{2}}f''(X_{t})\sigma _{t}^{2}\left(z^{2}-1\right)\,dt+o(dt)\right]\end{aligned}}$ We have split it into two parts, a deterministic part, and a random part with mean zero. The random part is non-Gaussian, but the non-Gaussian parts decay faster than the Gaussian part, and at the $dt\to 0$ limit, only the Gaussian part remains. The deterministic part has the expected $f(X_{t})+f'(X_{t})\mu _{t}\,dt$ , but also a part contributed by the convexity: ${\textstyle {\frac {1}{2}}f''(X_{t})\sigma _{t}^{2}\,dt}$ .

To understand why there should be a contribution due to convexity, consider the simplest case of geometric Brownian walk (of the stock market): $S_{t+dt}=S_{t}(1+dB_{t})$ . In other words, $d(\ln S_{t})=dB_{t}$ . Let $X_{t}=\ln S_{t}$ , then $S_{t}=e^{X_{t}}$ , and $X_{t}$ is a Brownian walk. However, although the expectation of $X_{t}$ remains constant, the expectation of $S_{t}$ grows. Intuitively it is because the downside is limited at zero, but the upside is unlimited. That is, while $X_{t}$ is normally distributed, $S_{t}$ is log-normally distributed.

## Mathematical formulation of Itô's lemma

In the following subsections we discuss versions of Itô's lemma for different types of stochastic processes.

### Itô drift-diffusion processes (due to: Kunita–Watanabe)

In its simplest form, Itô's lemma states the following: for an Itô drift-diffusion process

$dX_{t}=\mu _{t}\,dt+\sigma _{t}\,dB_{t}$

and any twice differentiable scalar function *f*(*t*,*x*) of two real variables *t* and *x*, one has

$df(t,X_{t})=\left({\frac {\partial f}{\partial t}}+\mu _{t}{\frac {\partial f}{\partial x}}+{\frac {\sigma _{t}^{2}}{2}}{\frac {\partial ^{2}f}{\partial x^{2}}}\right)dt+\sigma _{t}{\frac {\partial f}{\partial x}}\,dB_{t}.$

This immediately implies that *f*(*t*,*X**t*) is itself an Itô drift-diffusion process.

In higher dimensions, if $\mathbf {X} _{t}=(X_{t}^{1},X_{t}^{2},\ldots ,X_{t}^{n})^{T}$ is a vector of Itô processes such that

$d\mathbf {X} _{t}={\boldsymbol {\mu }}_{t}\,dt+\mathbf {G} _{t}\,d\mathbf {B} _{t}$

for a vector ${\boldsymbol {\mu }}_{t}$ and matrix $\mathbf {G} _{t}$ , Itô's lemma then states that

${\begin{aligned}df(t,\mathbf {X} _{t})&={\frac {\partial f}{\partial t}}\,dt+\left(\nabla _{\mathbf {X} }f\right)^{T}\,d\mathbf {X} _{t}+{\frac {1}{2}}\left(d\mathbf {X} _{t}\right)^{T}\left(H_{\mathbf {X} }f\right)\,d\mathbf {X} _{t},\\[4pt]&=\left\{{\frac {\partial f}{\partial t}}+\left(\nabla _{\mathbf {X} }f\right)^{T}{\boldsymbol {\mu }}_{t}+{\frac {1}{2}}\operatorname {Tr} \left[\mathbf {G} _{t}^{T}\left(H_{\mathbf {X} }f\right)\mathbf {G} _{t}\right]\right\}\,dt+\left(\nabla _{\mathbf {X} }f\right)^{T}\mathbf {G} _{t}\,d\mathbf {B} _{t}\end{aligned}}$

where $\nabla _{\mathbf {X} }f$ is the gradient of *f* w.r.t. *X*, *H***X** *f* is the Hessian matrix of *f* w.r.t. *X*, and Tr is the trace operator.

### Poisson jump processes

We may also define functions on discontinuous stochastic processes.

Let h be the jump intensity. The Poisson process model for jumps is that the probability of one jump in the interval [*t*, *t* + Δ*t*] is *h*Δ*t* plus higher order terms. h could be a constant, a deterministic function of time, or a stochastic process. The survival probability *ps*(*t*) is the probability that no jump has occurred in the interval [0, *t*]. The change in the survival probability is

$dp_{s}(t)=-p_{s}(t)h(t)\,dt,$

so

$p_{s}(t)=\exp \left(-\int _{0}^{t}h(u)\,du\right).$

Let *S*(*t*) be a discontinuous stochastic process. Write $S(t^{-})$ for the value of *S* as we approach *t* from the left. Write $d_{j}S(t)$ for the non-infinitesimal change in *S*(*t*) as a result of a jump. Then

$d_{j}S(t)=\lim _{\Delta t\to 0}\left[S(t+\Delta t)-S(t^{-})\right].$

Let *z* be the magnitude of the jump and let $\eta (S(t^{-}),z)$ be the distribution of *z*. The expected magnitude of the jump is

$\operatorname {E} [d_{j}S(t)]=h(S(t^{-}))\,dt\int _{z}z\eta (S(t^{-}),z)\,dz.$

Now, define the *compensated process* $J_{S}(t)$ associated with $S(t)$ , which simply means that we subtract off the mean change in $S(t)$ so that $J_{S}(t)$ is a martingale. Hence the increment to $J_{S}(t)$ is:

${\begin{aligned}dJ_{S}(t)&=d_{j}S(t)-\operatorname {E} [d_{j}S(t)]\\[1ex]&=S(t)-S(t^{-})-\left(h(S(t^{-}))\int _{z}z\eta \left(S(t^{-}),z\right)\,dz\right)\,dt.\end{aligned}}$

Then

${\begin{aligned}d_{j}S(t)&=E[d_{j}S(t)]+dJ_{S}(t)\\[1ex]&=h(S(t^{-}))\left(\int _{z}z\eta (S(t^{-}),z)\,dz\right)dt+dJ_{S}(t).\end{aligned}}$

Consider a function $g(S(t),t)$ of the jump process *dS*(*t*). If *S*(*t*) jumps by Δ*s* then *g*(*t*) jumps by Δ*g*. Δ*g* is drawn from distribution $\eta _{g}()$ which may depend on $g(t^{-})$ , *dg* and $S(t^{-})$ . The jump part of g is

$g(t)-g(t^{-})=h(t)\,dt\int _{\Delta g}\,\Delta g\eta _{g}(\cdot )\,d\Delta g+dJ_{g}(t).$

If S contains drift, diffusion and jump parts, then Itô's Lemma for $g(S(t),t)$ is

${\begin{aligned}dg(t)={}&\left({\frac {\partial g}{\partial t}}+\mu {\frac {\partial g}{\partial S}}+{\frac {\sigma ^{2}}{2}}{\frac {\partial ^{2}g}{\partial S^{2}}}+h(t)\int _{\Delta g}\left(\Delta g\eta _{g}(\cdot )\,d{\Delta }g\right)\,\right)dt\\&+{\frac {\partial g}{\partial S}}\sigma \,dW(t)+dJ_{g}(t).\end{aligned}}$

Itô's lemma for a process which is the sum of a drift-diffusion process and a jump process is just the sum of the Itô's lemma for the individual parts.

### Discontinuous semimartingales

Itô's lemma can also be applied to general d-dimensional semimartingales, which need not be continuous. In general, a semimartingale is a càdlàg process, and an additional jump term needs to be added to the Itô's formula. For any cadlag process *Yt*, the left limit in t is denoted by *Yt−*, which is a left-continuous process. The jumps are written as Δ*Yt* = *Yt* − *Yt−*. Then, Itô's lemma states that if *X* = (*X*1, *X*2, ..., *Xd*) is a d-dimensional semimartingale and *f* is a twice continuously differentiable real valued function on **R***d* then *f*(*X*) is a semimartingale, and

${\begin{aligned}f(X_{t})=f(X_{0})&+\sum _{i=1}^{d}\int _{0}^{t}f_{i}(X_{s-})\,dX_{s}^{i}+{\frac {1}{2}}\sum _{i,j=1}^{d}\int _{0}^{t}f_{i,j}(X_{s-})\,d[X^{i},X^{j}]_{s}\\&+\sum _{s\leq t}\left(\Delta f(X_{s})-\sum _{i=1}^{d}f_{i}(X_{s-})\,\Delta X_{s}^{i}-{\frac {1}{2}}\sum _{i,j=1}^{d}f_{i,j}(X_{s-})\,\Delta X_{s}^{i}\,\Delta X_{s}^{j}\right).\end{aligned}}$

This differs from the formula for continuous semi-martingales by the last term summing over the jumps of *X*, which ensures that the jump of the right hand side at time t is Δ*f*(*Xt*).

## Examples

### Geometric Brownian motion

A process S is said to follow a geometric Brownian motion with constant volatility *σ* and constant drift *μ* if it satisfies the stochastic differential equation $dS_{t}=\sigma S_{t}\,dB_{t}+\mu S_{t}\,dt$ , for a Brownian motion *B*. Applying Itô's lemma with $f(S_{t})=\log(S_{t})$ gives

${\begin{aligned}df&=f'(S_{t})\,dS_{t}+{\frac {1}{2}}f''(S_{t})\,{\left(dS_{t}\right)}^{2}\\[4pt]&={\frac {1}{S_{t}}}\,dS_{t}+{\frac {1}{2}}\left(-S_{t}^{-2}\right)\left(S_{t}^{2}\sigma ^{2}\,dt\right)\\[4pt]&={\frac {1}{S_{t}}}\left(\sigma S_{t}\,dB_{t}+\mu S_{t}\,dt\right)-{\frac {\sigma ^{2}}{2}}\,dt\\[4pt]&=\sigma \,dB_{t}+\left(\mu -{\tfrac {\sigma ^{2}}{2}}\right)dt.\end{aligned}}$

It follows that

$\log(S_{t})=\log(S_{0})+\sigma B_{t}+\left(\mu -{\tfrac {\sigma ^{2}}{2}}\right)t,$

exponentiating gives the expression for *S*,

$S_{t}=S_{0}\exp \left(\sigma B_{t}+\left(\mu -{\tfrac {\sigma ^{2}}{2}}\right)t\right).$

The correction term of − ⁠*σ*2/2⁠ corresponds to the difference between the median and mean of the log-normal distribution, or equivalently for this distribution, the geometric mean and arithmetic mean, with the median (geometric mean) being lower. This is due to the AM–GM inequality, and corresponds to the logarithm being concave (or convex upwards), so the correction term can accordingly be interpreted as a convexity correction. This is an infinitesimal version of the fact that the annualized return is less than the average return, with the difference proportional to the variance. See geometric moments of the log-normal distribution for further discussion.

The same factor of ⁠*σ*2/2⁠ appears in the *d*1 and *d*2 auxiliary variables of the Black–Scholes formula, and can be interpreted as a consequence of Itô's lemma.

### Doléans-Dade exponential

The Doléans-Dade exponential (or stochastic exponential) of a continuous semimartingale *X* can be defined as the solution to the SDE *dY* = *Y dX* with initial condition *Y*0 = 1. It is sometimes denoted by Ɛ(*X*). Applying Itô's lemma with *f*(*Y*) = log(*Y*) gives

${\begin{aligned}d\log(Y)&={\frac {1}{Y}}\,dY-{\frac {1}{2Y^{2}}}\,d[Y]\\[6pt]&=dX-{\tfrac {1}{2}}\,d[X].\end{aligned}}$

Exponentiating gives the solution

$Y_{t}=\exp \left(X_{t}-X_{0}-{\tfrac {1}{2}}[X]_{t}\right).$

### Black–Scholes formula

Itô's lemma can be used to derive the Black–Scholes equation for an option. Suppose a stock price follows a geometric Brownian motion given by the stochastic differential equation *dS* = *S*(*σ* *dB* + *μ* *dt*). Then, if the value of an option at time t is *f*(*t*, *St*), Itô's lemma gives

$df(t,S_{t})=\left({\frac {\partial f}{\partial t}}+{\frac {1}{2}}\left(S_{t}\sigma \right)^{2}{\frac {\partial ^{2}f}{\partial S^{2}}}\right)\,dt+{\frac {\partial f}{\partial S}}\,dS_{t}.$

The term ⁠∂*f*/∂*S*⁠ *dS* represents the change in value in time *dt* of the trading strategy consisting of holding an amount ⁠∂ *f*/∂*S*⁠ of the stock. If this trading strategy is followed, and any cash held is assumed to grow at the risk free rate r, then the total value *V* of this portfolio satisfies the SDE

$dV_{t}=r\left(V_{t}-{\frac {\partial f}{\partial S}}S_{t}\right)\,dt+{\frac {\partial f}{\partial S}}\,dS_{t}.$

This strategy replicates the option if *V* = *f*(*t*,*S*). Combining these equations gives the celebrated Black–Scholes equation

${\frac {\partial f}{\partial t}}+{\frac {\sigma ^{2}S^{2}}{2}}{\frac {\partial ^{2}f}{\partial S^{2}}}+rS{\frac {\partial f}{\partial S}}-rf=0.$

### Product rule for Itô processes

Let $\mathbf {X} _{t}$ be a two-dimensional Ito process with SDE: $d\mathbf {X} _{t}=d{\begin{pmatrix}X_{t}^{1}\\X_{t}^{2}\end{pmatrix}}={\begin{pmatrix}\mu _{t}^{1}\\\mu _{t}^{2}\end{pmatrix}}dt+{\begin{pmatrix}\sigma _{t}^{1}\\\sigma _{t}^{2}\end{pmatrix}}\,dB_{t}$

Then we can use the multi-dimensional form of Ito's lemma to find an expression for $d(X_{t}^{1}X_{t}^{2})$ .

We have $\mu _{t}={\begin{pmatrix}\mu _{t}^{1}\\\mu _{t}^{2}\end{pmatrix}}$ and $\mathbf {G} ={\begin{pmatrix}\sigma _{t}^{1}\\\sigma _{t}^{2}\end{pmatrix}}$ .

We set $f(t,\mathbf {X} _{t})=X_{t}^{1}X_{t}^{2}$ and observe that ${\frac {\partial f}{\partial t}}=0$ , $(\nabla _{\mathbf {X} }f)^{T}={\begin{pmatrix}X_{t}^{2}&X_{t}^{1}\end{pmatrix}}$ , and $H_{\mathbf {X} }f={\begin{pmatrix}0&1\\1&0\end{pmatrix}}$

Substituting these values in the multi-dimensional version of the lemma gives us:

${\begin{aligned}d(X_{t}^{1}X_{t}^{2})&=df(t,\mathbf {X} _{t})\\&=0\cdot dt+{\begin{pmatrix}X_{t}^{2}&X_{t}^{1}\end{pmatrix}}\,d\mathbf {X} _{t}+{\frac {1}{2}}{\begin{pmatrix}dX_{t}^{1}&dX_{t}^{2}\end{pmatrix}}{\begin{pmatrix}0&1\\1&0\end{pmatrix}}{\begin{pmatrix}dX_{t}^{1}\\dX_{t}^{2}\end{pmatrix}}\\[1ex]&=X_{t}^{2}\,dX_{t}^{1}+X_{t}^{1}\,dX_{t}^{2}+dX_{t}^{1}\,dX_{t}^{2}\end{aligned}}$

This is a generalisation of Leibniz's product rule to Ito processes, which are non-differentiable.

Further, using the second form of the multidimensional version above gives us

${\begin{aligned}d(X_{t}^{1}X_{t}^{2})&=\left\{0+{\begin{pmatrix}X_{t}^{2}&X_{t}^{1}\end{pmatrix}}{\begin{pmatrix}\mu _{t}^{1}\\\mu _{t}^{2}\end{pmatrix}}+{\frac {1}{2}}\operatorname {Tr} \left[{\begin{pmatrix}\sigma _{t}^{1}&\sigma _{t}^{2}\end{pmatrix}}{\begin{pmatrix}0&1\\1&0\end{pmatrix}}{\begin{pmatrix}\sigma _{t}^{1}\\\sigma _{t}^{2}\end{pmatrix}}\right]\right\}dt\\[1ex]&\qquad +\left(X_{t}^{2}\sigma _{t}^{1}+X_{t}^{1}\sigma _{t}^{2}\right)dB_{t}\\[2ex]&=\left(X_{t}^{2}\mu _{t}^{1}+X_{t}^{1}\mu _{t}^{2}+\sigma _{t}^{1}\sigma _{t}^{2}\right)dt+\left(X_{t}^{2}\sigma _{t}^{1}+X_{t}^{1}\sigma _{t}^{2}\right)dB_{t}\end{aligned}}$

so we see that the product $X_{t}^{1}X_{t}^{2}$ is itself an Itô drift-diffusion process.

## Itô's formula for functions with finite quadratic variation

Hans Föllmer provided a non-probabilistic proof of the Itô formula and showed that it holds for all functions with finite quadratic variation.

Let $f\in C^{2}$ be a real-valued function and $x:[0,\infty ]\to \mathbb {R}$ a right-continuous function with left limits and finite quadratic variation $[x]$ . Then ${\begin{aligned}f(x_{t})=f(x_{0})&+\int _{0}^{t}f'(x_{s-})\,\mathrm {d} x_{s}+{\frac {1}{2}}\int _{]0,t]}f''(x_{s-})\,d[x]_{s}\\&+\sum _{0\leq s\leq t}\left[f(x_{s})-f(x_{s-})-f'(x_{s-})\Delta x_{s}-{\frac {1}{2}}f''(x_{s-})(\Delta x_{s})^{2}\right].\end{aligned}}$

where the quadratic variation of x is defined as a limit along a sequence of partitions $D_{n}$ of $[0,t]$ with step decreasing to zero:

$[x](t)=\lim _{n\to \infty }\sum _{t_{k}^{n}\in D_{n}}\left(x_{t_{k+1}^{n}}-x_{t_{k}^{n}}\right)^{2}.$

## Higher-order Itô formula

Rama Cont and Nicolas Perkowski extended the Itô formula to functions with finite p-th variation where $p\geq 2$ is an arbitrarily large integer.

Given a continuous function with finite p-th variation

$[x]^{p}(t)=\lim _{n\to \infty }\sum _{t_{k}^{n}\in D_{n}}{\left(x_{t_{k+1}^{n}}-x_{t_{k}^{n}}\right)}^{p},$

Cont and Perkowski's change of variable formula states that for any $f\in C^{p}(\mathbb {R} ^{d},\mathbb {R} )$ :

${\begin{aligned}f(x_{t})={}&f(x_{0})+\int _{0}^{t}\nabla _{p-1}f(x_{s-})\,\mathrm {d} x_{s}+{\frac {1}{p!}}\int _{]0,t]}f^{p}(x_{s-})\,d[x]_{s}^{p}\end{aligned}}$

where the first integral is defined as a limit of compensated left Riemann sums along a sequence of partitions $D_{n}$ :

${\begin{aligned}\int _{0}^{t}\nabla _{p-1}f(x_{s-})\,\mathrm {d} x_{s}:={}&\sum _{t_{k}^{n}\in D_{n}}\sum _{k=1}^{p-1}{\frac {f^{k}(x_{t_{k}^{n}})}{k!}}\left(x_{t_{k+1}^{n}}-x_{t_{k}^{n}}\right)^{k}.\end{aligned}}$ An extension to the case of fractional regularity (non-integer p ) was obtained by Cont and Jin.

## Infinite-dimensional formulas

There exist some extensions to infinite-dimensional spaces (e.g. Pardoux, Gyöngy-Krylov, Brzezniak-van Neerven-Veraar-Weis).
