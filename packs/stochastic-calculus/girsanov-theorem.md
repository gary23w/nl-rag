---
title: "Girsanov theorem"
source: https://en.wikipedia.org/wiki/Girsanov_theorem
domain: stochastic-calculus
license: CC-BY-SA-4.0
tags: stochastic calculus, stochastic differential equation, wiener process, feynman-kac formula
fetched: 2026-07-02
---

# Girsanov theorem

In probability theory, **Girsanov's theorem** or the **Cameron-Martin-Girsanov theorem** explains how stochastic processes change under changes in measure. The theorem is especially important in the theory of financial mathematics as it explains how to convert from the physical measure, which describes the probability that an underlying instrument (such as a share price or interest rate) will take a particular value or values, to the risk-neutral measure which is a very useful tool for evaluating the value of derivatives on the underlying instrument.

## History

Results of this type were first proved by Cameron-Martin in the 1940s and by Igor Girsanov in 1960. They have been subsequently extended to more general classes of process culminating in the general form of Lenglart (1977).

## Significance

Girsanov's theorem is important in the general theory of stochastic processes since it enables the key result that if *Q* is a measure that is absolutely continuous with respect to *P* then every *P*-semimartingale is a *Q*-semimartingale.

## Statement of theorem

We state the theorem first for the special case when the underlying stochastic process is a Wiener process. This special case is sufficient for risk-neutral pricing in the Black–Scholes model.

Let $\{W_{t}\}$ be a Wiener process on the Wiener probability space $\{\Omega ,{\mathcal {F}},P\}$ . Let $X_{t}$ be a measurable process adapted to the natural filtration of the Wiener process $\{{\mathcal {F}}_{t}^{W}\}$ ; we assume that the usual conditions have been satisfied.

Given an adapted process $X_{t}$ define

$Z_{t}={\mathcal {E}}(X)_{t},\,$

where ${\mathcal {E}}(X)$ is the stochastic exponential of *X* with respect to *W*, i.e.

${\mathcal {E}}(X)_{t}=\exp \left(X_{t}-{\frac {1}{2}}[X]_{t}\right),$

and $[X]_{t}$ denotes the quadratic variation of the process *X*.

If $Z_{t}$ is a martingale then a probability measure *Q* can be defined on $\{\Omega ,{\mathcal {F}}\}$ such that the Radon–Nikodym derivative of *Q* with respect to *P* satisfies

$\left.{\frac {dQ}{dP}}\right|_{{\mathcal {F}}_{t}}=Z_{t}={\mathcal {E}}(X)_{t}$

.

Then for each *t* the measure *Q* restricted to the unaugmented sigma fields ${\mathcal {F}}_{t}^{o}$ is equivalent to *P* restricted to

${\mathcal {F}}_{t}^{o}.\,$

Furthermore, if $Y_{t}$ is a local martingale under *P* then the process

${\tilde {Y}}_{t}=Y_{t}-\left[Y,X\right]_{t}$

is a *Q* local martingale on the filtered probability space $\{\Omega ,F,Q,\{{\mathcal {F}}_{t}^{W}\}\}$ .

## Corollary

If *X* is a continuous process and *W* is a Brownian motion under measure *P* then

${\tilde {W}}_{t}=W_{t}-\left[W,X\right]_{t}$

is a Brownian motion under *Q*.

The fact that ${\tilde {W}}_{t}$ is continuous is trivial; by Girsanov's theorem it is a *Q* local martingale, and by computing

$\left[{\tilde {W}}\right]_{t}=\left[W\right]_{t}=t$

it follows by Levy's characterization of Brownian motion that this is a *Q* Brownian motion.

In many common applications, the process *X* is defined by

$X_{t}=\int _{0}^{t}Y_{s}\,dW_{s}.$

For *X* of this form then a necessary and sufficient condition for ${\mathcal {E}}(X)$ to be a martingale is Novikov's condition which requires that

$E_{P}\left[\exp \left({\frac {1}{2}}\int _{0}^{T}Y_{s}^{2}\,ds\right)\right]<\infty .$

The stochastic exponential ${\mathcal {E}}(X)$ is the process *Z* which solves the stochastic differential equation

$Z_{t}=1+\int _{0}^{t}Z_{s}\,dX_{s}.\,$

The measure *Q* constructed above is not equivalent to *P* on ${\mathcal {F}}_{\infty }$ as this would only be the case if the Radon–Nikodym derivative were a uniformly integrable martingale, which the exponential martingale described above is not. On the other hand, as long as Novikov's condition is satisfied the measures are equivalent on ${\mathcal {F}}_{T}$ .

Additionally, then combining this above observation in this case, we see that the process

${\tilde {W}}_{t}=W_{t}-\int _{0}^{t}Y_{s}ds$

for $t\in [0,T]$ is a Q Brownian motion. This was Igor Girsanov's original formulation of the above theorem.

## Application to finance

This theorem can be used to show in the Black–Scholes model the unique risk-neutral measure, i.e. the measure in which the fair value of a derivative is the discounted expected value, Q, is specified by

${\frac {dQ}{dP}}={\mathcal {E}}\left(\int _{0}^{t}{\frac {r_{s}-\mu _{s}}{\sigma _{s}}}\,dW_{s}\right).$

## Application to Langevin equations

Another application of this theorem, also given in the original paper of Igor Girsanov, is for stochastic differential equations. Specifically, let us consider the equation

$dX_{t}=\mu (X_{t},t)dt+\sigma (X_{t},t)dW_{t},$

where $W_{t}$ denotes a Brownian motion. Here $\mu$ and $\sigma$ are fixed deterministic functions. We assume that this equation has a unique strong solution on $[0,T]$ . In this case Girsanov's theorem may be used to compute functionals of $X_{t}$ directly in terms a related functional for Brownian motion. More specifically, we have for any bounded functional $\Phi$ on continuous functions $C([0,T])$ that

$E\Phi (X)=E\left[\Phi (W)\exp \left(\int _{0}^{T}\mu (W_{s},s)dW_{s}-{\frac {1}{2}}\int _{0}^{T}\mu (W_{s},s)^{2}ds\right)\right].$

This follows by applying Girsanov's theorem, and the above observation, to the martingale process

$Y_{t}=\int _{0}^{t}\mu (W_{s},s)dW_{s}.$

In particular, with the notation above, the process

${\tilde {W}}_{t}=W_{t}-\int _{0}^{t}\mu (W_{s},s)ds$

is a Q Brownian motion. Rewriting this in differential form as

$dW_{t}=d{\tilde {W}}_{t}+\mu (W_{t},t)dt,$

we see that the law of $W_{t}$ under Q solves the equation defining $X_{t}$ , as ${\tilde {W}}_{t}$ is a Q Brownian motion. In particular, we see that the right-hand side may be written as $E_{Q}[\Phi (W)]$ , where Q is the measure taken with respect to the process Y, so the result now is just the statement of Girsanov's theorem.

A more general form of this application is that if both

$dX_{t}=\mu (X_{t},t)dt+\sigma (X_{t},t)dW_{t},$ $dY_{t}=(\mu (Y_{t},t)+\nu (Y_{t},t))dt+\sigma (Y_{t},t)dW_{t},$

admit unique strong solutions on $[0,T]$ , then for any bounded functional on $C([0,T])$ , we have that

$E\Phi (X)=E\left[\Phi (Y)\exp \left(-\int _{0}^{T}{\frac {\nu (Y_{s},s)}{\sigma (Y_{s},s)}}dW_{s}-{\frac {1}{2}}\int _{0}^{T}{\frac {\nu (Y_{s},s)^{2}}{\sigma (Y_{s},s)^{2}}}ds\right)\right].$
