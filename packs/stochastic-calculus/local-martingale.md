---
title: "Local martingale"
source: https://en.wikipedia.org/wiki/Local_martingale
domain: stochastic-calculus
license: CC-BY-SA-4.0
tags: stochastic calculus, stochastic differential equation, wiener process, feynman-kac formula
fetched: 2026-07-02
---

# Local martingale

In mathematics, a **local martingale** is a type of stochastic process, satisfying the localized version of the martingale property. Every martingale is a local martingale; every bounded local martingale is a martingale; in particular, every local martingale that is bounded from below is a supermartingale, and every local martingale that is bounded from above is a submartingale; however, a local martingale is not in general a martingale, because its expectation can be distorted by large values of small probability. In particular, a driftless diffusion process is a local martingale, but not necessarily a martingale.

Local martingales are essential in stochastic analysis (see Itô calculus, semimartingale, and Girsanov theorem).

## Definition

Let $(\Omega ,F,P)$ be a probability space; let $F_{*}=\{F_{t}\mid t\geq 0\}$ be a filtration of F ; let $X\colon [0,\infty )\times \Omega \rightarrow S$ be an $F_{*}$ -adapted stochastic process on the set S . Then X is called an $F_{*}$ -**local martingale** if there exists a sequence of $F_{*}$ -stopping times $\tau _{k}\colon \Omega \to [0,\infty )$ such that

- the $\tau _{k}$ are almost surely increasing: $P\left\{\tau _{k}<\tau _{k+1}\right\}=1$ ;
- the $\tau _{k}$ diverge almost surely: $P\left\{\lim _{k\to \infty }\tau _{k}=\infty \right\}=1$ ;
- the stopped process $X_{t}^{\tau _{k}}:=X_{\min\{t,\tau _{k}\}}$ is an $F_{*}$ -martingale for every k .

## Examples

### Example 1

Let *W**t* be the Wiener process and *T* = min{ *t* : *W**t* = −1 } the time of first hit of −1. The stopped process *W*min{ *t*, *T* } is a martingale. Its expectation is 0 at all times; nevertheless, its limit (as *t* → ∞) is equal to −1 almost surely (a kind of gambler's ruin). A time change leads to a process

$\displaystyle X_{t}={\begin{cases}W_{\min \left({\tfrac {t}{1-t}},T\right)}&{\text{for }}0\leq t<1,\\-1&{\text{for }}1\leq t<\infty .\end{cases}}$

The process $X_{t}$ is continuous almost surely; nevertheless, its expectation is discontinuous,

$\displaystyle \operatorname {E} X_{t}={\begin{cases}0&{\text{for }}0\leq t<1,\\-1&{\text{for }}1\leq t<\infty .\end{cases}}$

This process is not a martingale. However, it is a local martingale. A localizing sequence may be chosen as $\tau _{k}=\min\{t:X_{t}=k\}$ if there is such *t*, otherwise $\tau _{k}=k$ . This sequence diverges almost surely, since $\tau _{k}=k$ for all *k* large enough (namely, for all *k* that exceed the maximal value of the process *X*). The process stopped at τ*k* is a martingale.

### Example 2

Let *W**t* be the Wiener process and *ƒ* a measurable function such that $\operatorname {E} |f(W_{1})|<\infty .$ Then the following process is a martingale:

${\displaystyle X_{t}=\operatorname {E} (f(W_{1})\mid F_{t})={\begin{cases}f_{1-t}(W_{t})&{\text{for }}0\leq t<1,\\f(W_{1})&{\text{for }}1\leq t<\infty$

where

$f_{s}(x)=\operatorname {E} f(x+W_{s})=\int f(x+y){\frac {1}{\sqrt {2\pi s}}}\mathrm {e} ^{-y^{2}/(2s)}\,dy.$

The Dirac delta function $\delta$ (strictly speaking, not a function), being used in place of $f,$ leads to a process defined informally as $Y_{t}=\operatorname {E} (\delta (W_{1})\mid F_{t})$ and formally as

$Y_{t}={\begin{cases}\delta _{1-t}(W_{t})&{\text{for }}0\leq t<1,\\0&{\text{for }}1\leq t<\infty ,\end{cases}}$

where

$\delta _{s}(x)={\frac {1}{\sqrt {2\pi s}}}\mathrm {e} ^{-x^{2}/(2s)}.$

The process $Y_{t}$ is continuous almost surely (since $W_{1}\neq 0$ almost surely), nevertheless, its expectation is discontinuous,

$\operatorname {E} Y_{t}={\begin{cases}1/{\sqrt {2\pi }}&{\text{for }}0\leq t<1,\\0&{\text{for }}1\leq t<\infty .\end{cases}}$

This process is not a martingale. However, it is a local martingale. A localizing sequence may be chosen as $\tau _{k}=\min\{t:Y_{t}=k\}.$

### Example 3

Let $Z_{t}$ be the complex-valued Wiener process, and

$X_{t}=\ln |Z_{t}-1|\,.$

The process $X_{t}$ is continuous almost surely (since $Z_{t}$ does not hit 1, almost surely), and is a local martingale, since the function $u\mapsto \ln |u-1|$ is harmonic (on the complex plane without the point 1). A localizing sequence may be chosen as $\tau _{k}=\min\{t:X_{t}=-k\}.$ Nevertheless, the expectation of this process is non-constant; moreover,

$\operatorname {E} X_{t}\to \infty$

as

$t\to \infty ,$

which can be deduced from the fact that the mean value of $\ln |u-1|$ over the circle $|u|=r$ tends to infinity as $r\to \infty$ . (In fact, it is equal to $\ln r$ for *r* ≥ 1 but to 0 for *r* ≤ 1).

## Martingales via local martingales

Let $M_{t}$ be a local martingale. In order to prove that it is a martingale it is sufficient to prove that $M_{t}^{\tau _{k}}\to M_{t}$ in *L*1 (as $k\to \infty$ ) for every *t*, that is, $\operatorname {E} |M_{t}^{\tau _{k}}-M_{t}|\to 0;$ here $M_{t}^{\tau _{k}}=M_{t\wedge \tau _{k}}$ is the stopped process. The given relation $\tau _{k}\to \infty$ implies that $M_{t}^{\tau _{k}}\to M_{t}$ almost surely. The dominated convergence theorem ensures the convergence in *L*1 provided that

$\textstyle (*)\quad \operatorname {E} \sup _{k}|M_{t}^{\tau _{k}}|<\infty$

for every

t

.

Thus, Condition (*) is sufficient for a local martingale $M_{t}$ being a martingale. A stronger condition

$\textstyle (**)\quad \operatorname {E} \sup _{s\in [0,t]}|M_{s}|<\infty$

for every

t

is also sufficient.

*Caution.* The weaker condition

$\textstyle \sup _{s\in [0,t]}\operatorname {E} |M_{s}|<\infty$

for every

t

is not sufficient. Moreover, the condition

$\textstyle \sup _{t\in [0,\infty )}\operatorname {E} \mathrm {e} ^{|M_{t}|}<\infty$

is still not sufficient; for a counterexample see Example 3 above.

A special case:

$\textstyle M_{t}=f(t,W_{t}),$

where $W_{t}$ is the Wiener process, and $f:[0,\infty )\times \mathbb {R} \to \mathbb {R}$ is twice continuously differentiable. The process $M_{t}$ is a local martingale if and only if *f* satisfies the PDE

${\Big (}{\frac {\partial }{\partial t}}+{\frac {1}{2}}{\frac {\partial ^{2}}{\partial x^{2}}}{\Big )}f(t,x)=0.$

However, this PDE itself does not ensure that $M_{t}$ is a martingale. In order to apply (**) the following condition on *f* is sufficient: for every $\varepsilon >0$ and *t* there exists $C=C(\varepsilon ,t)$ such that

$\textstyle |f(s,x)|\leq C\mathrm {e} ^{\varepsilon x^{2}}$

for all $s\in [0,t]$ and $x\in \mathbb {R} .$

## Technical details

1. For the times before 1 it is a martingale since a stopped Brownian motion is. After the instant 1 it is constant. It remains to check it at the instant 1. By the bounded convergence theorem the expectation at 1 is the limit of the expectation at (*n*-1)/*n* (as *n* tends to infinity), and the latter does not depend on *n*. The same argument applies to the conditional expectation.
