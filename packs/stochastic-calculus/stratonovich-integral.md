---
title: "Stratonovich integral"
source: https://en.wikipedia.org/wiki/Stratonovich_integral
domain: stochastic-calculus
license: CC-BY-SA-4.0
tags: stochastic calculus, stochastic differential equation, wiener process, feynman-kac formula
fetched: 2026-07-02
---

# Stratonovich integral

In stochastic processes, the **Stratonovich integral** or **Fisk–Stratonovich integral** (developed simultaneously by Ruslan Stratonovich and Donald Fisk) is a stochastic integral, the most common alternative to the Itô integral. Although the Itô integral is the usual choice in applied mathematics, the Stratonovich integral is frequently used in physics.

In some circumstances, integrals in the Stratonovich definition are easier to manipulate. Unlike the Itô calculus, Stratonovich integrals are defined such that the chain rule of ordinary calculus holds.

Perhaps the most common situation in which these are encountered is as the solution to Stratonovich stochastic differential equations (SDEs). These are equivalent to Itô SDEs and it is possible to convert between the two whenever one definition is more convenient.

## Definition

The Stratonovich integral can be defined in a manner similar to the Riemann integral, that is as a limit of Riemann sums. Suppose that $W:[0,T]\times \Omega \to \mathbb {R}$ is a Wiener process and $X:[0,T]\times \Omega \to \mathbb {R}$ is a semimartingale adapted to the natural filtration of the Wiener process. Then the **Stratonovich integral**

$\int _{0}^{T}X_{t}\circ \mathrm {d} W_{t}$

is a random variable ${\displaystyle$ defined as the limit in mean square of

$\sum _{i=0}^{k-1}{\frac {X_{t_{i+1}}+X_{t_{i}}}{2}}\left(W_{t_{i+1}}-W_{t_{i}}\right)$

as the mesh of the partition $0=t_{0}<t_{1}<\dots <t_{k}=T$ of $[0,T]$ tends to 0 (in the style of a Riemann–Stieltjes integral). The circle $\circ$ is a notational device, used to distinguish this integral from the Itô integral.

## Calculation

Many integration techniques of ordinary calculus can be used for the Stratonovich integral, e.g.: if $f:\mathbb {R} \to \mathbb {R}$ is a smooth function, then

$\int _{0}^{T}f'(W_{t})\circ \mathrm {d} W_{t}=f(W_{T})-f(W_{0})$

and more generally, if $f:\mathbb {R} \times \mathbb {R} \to \mathbb {R}$ is a smooth function, then

$\int _{0}^{T}{\partial f \over \partial W}(W_{t},t)\circ \mathrm {d} W_{t}+\int _{0}^{T}{\partial f \over \partial t}(W_{t},t)\,\mathrm {d} t=f(W_{T},T)-f(W_{0},0).$

This latter rule is akin to the chain rule of ordinary calculus.

### Numerical methods

Stochastic integrals can rarely be solved in analytic form, making stochastic numerical integration an important topic in all uses of stochastic integrals. Various numerical approximations converge to the Stratonovich integral, and variations of these are used to solve Stratonovich SDEs (Kloeden & Platen 1992). Note however that the most widely used Euler scheme (the Euler–Maruyama method) for the numeric solution of Langevin equations requires the equation to be in Itô form.

## Differential notation

If $X_{t},Y_{t}$ , and $Z_{t}$ are stochastic processes such that

$X_{T}-X_{0}=\int _{0}^{T}Y_{t}\circ \mathrm {d} W_{t}+\int _{0}^{T}Z_{t}\,\mathrm {d} t$

for all $T>0$ , we also write

$\mathrm {d} X=Y\circ \mathrm {d} W+Z\,\mathrm {d} t.$

This notation is often used to formulate stochastic differential equations (SDEs), which are really equations about stochastic integrals. It is compatible with the notation from ordinary calculus, for instance

$\mathrm {d} (t^{2}\,W^{3})=3t^{2}W^{2}\circ \mathrm {d} W+2tW^{3}\,\mathrm {d} t.$

## Comparison with the Itô integral

The Itô integral of the process X with respect to the Wiener process W is denoted by $\int _{0}^{T}X_{t}\,\mathrm {d} W_{t}$ (without the circle). For its definition, the same procedure is used as above in the definition of the Stratonovich integral, except for choosing the value of the process X at the left-hand endpoint of each subinterval, i.e.,

$X_{t_{i}}$

in place of

${\frac {X_{t_{i+1}}+X_{t_{i}}}{2}}$

This integral does not obey the ordinary chain rule as the Stratonovich integral does; instead one has to use the slightly more complicated Itô's lemma.

Conversion between Itô and Stratonovich integrals may be performed using the formula

$\int _{0}^{T}f(W_{t},t)\circ \mathrm {d} W_{t}={\frac {1}{2}}\int _{0}^{T}{\frac {\partial f}{\partial W}}f(W_{t},t)\,\mathrm {d} t+\int _{0}^{T}f(W_{t},t)\,\mathrm {d} W_{t},$

where f is any continuously differentiable function of two variables W and t and the last integral is an Itô integral (Kloeden & Platen 1992, p. 101).

Langevin equations exemplify the importance of specifying the interpretation (Stratonovich or Itô) in a given problem. Suppose $X_{t}$ is a time-homogeneous Itô diffusion with continuously differentiable diffusion coefficient $\sigma$ , i.e. it satisfies the SDE $\mathrm {d} X_{t}=\mu (X_{t})\,\mathrm {d} t+\sigma (X_{t})\,\mathrm {d} W_{t}$ . In order to get the corresponding Stratonovich version, the term $\sigma (X_{t})\,\mathrm {d} W_{t}$ (in Itô interpretation) should translate to $\sigma (X_{t})\circ \mathrm {d} W_{t}$ (in Stratonovich interpretation) as

$\int _{0}^{T}\sigma (X_{t})\circ \mathrm {d} W_{t}={\frac {1}{2}}\int _{0}^{T}{\frac {d\sigma }{dx}}(X_{t})\sigma (X_{t})\,\mathrm {d} t+\int _{0}^{T}\sigma (X_{t})\,\mathrm {d} W_{t}.$

Obviously, if $\sigma$ is independent of $X_{t}$ , the two interpretations will lead to the same form for the Langevin equation. In that case, the noise term is called "additive" (since the noise term $dW_{t}$ is multiplied by only a fixed coefficient). Otherwise, if $\sigma =\sigma (X_{t})$ , the Langevin equation in Itô form may in general differ from that in Stratonovich form, in which case the noise term is called multiplicative (i.e., the noise $dW_{t}$ is multiplied by a function of $X_{t}$ that is $\sigma (X_{t})$ ).

More generally, for any two semimartingales X and Y

$\int _{0}^{T}X_{s-}\circ \mathrm {d} Y_{s}=\int _{0}^{T}X_{s-}\,\mathrm {d} Y_{s}+{\frac {1}{2}}[X,Y]_{T}^{c},$

where $[X,Y]_{T}^{c}$ is the continuous part of the covariation.

## Stratonovich integrals in applications

The Stratonovich integral lacks the important property of the Itô integral, which does not "look into the future". In many real-world applications, such as modelling stock prices, one only has information about past events, and hence the Itô interpretation is more natural. In financial mathematics the Itô interpretation is usually used.

In physics, however, stochastic integrals occur as the solutions of Langevin equations. A Langevin equation is a coarse-grained version of a more microscopic model (Risken 1996); depending on the problem in consideration, Stratonovich or Itô interpretation or even more exotic interpretations such as the isothermal interpretation, are appropriate. The Stratonovich interpretation is the most frequently used interpretation within the physical sciences.

The Wong–Zakai theorem states that physical systems with non-white noise spectrum characterized by a finite noise correlation time $\tau$ can be approximated by a Langevin equations with white noise in Stratonovich interpretation in the limit where $\tau$ tends to zero.

Because the Stratonovich calculus satisfies the ordinary chain rule, stochastic differential equations (SDEs) in the Stratonovich sense are more straightforward to define on differentiable manifolds, rather than just on $\mathbb {R} ^{n}$ . The tricky chain rule of the Itô calculus makes it a more awkward choice for manifolds.

## Stratonovich interpretation and supersymmetric theory of SDEs

In the supersymmetric theory of SDEs, one considers the evolution operator obtained by averaging the pullback induced on the exterior algebra of the phase space by the stochastic flow determined by an SDE. In this context, it is then natural to use the Stratonovich interpretation of SDEs.
