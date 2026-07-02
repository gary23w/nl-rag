---
title: "Laplace transform (part 2/2)"
source: https://en.wikipedia.org/wiki/Laplace_transform
domain: ordinary-differential-equations
license: CC-BY-SA-4.0
tags: ordinary differential equation, initial value problem, boundary value problem, laplace transform
fetched: 2026-07-02
part: 2/2
---

## Examples and applications

The Laplace transform is used frequently in engineering and physics; the output of a linear time-invariant system can be calculated by convolving its unit impulse response with the input signal. Performing this calculation in Laplace space turns the convolution into a multiplication; the latter being easier to solve because of its algebraic form. For more information, see control theory. The Laplace transform is invertible on a large class of functions. Given a mathematical or functional description of an input or output to a system, the Laplace transform provides an alternative functional description that often simplifies the process of analyzing the behavior of the system, or in synthesizing a new system based on a set of specifications.

The Laplace transform can also be used to solve differential equations and is used extensively in mechanical engineering and electrical engineering. The Laplace transform reduces a linear differential equation to an algebraic equation, which can then be solved by the formal rules of algebra. The original differential equation can then be solved by applying the inverse Laplace transform. English electrical engineer Oliver Heaviside first proposed a similar scheme, although without using the Laplace transform; and the resulting operational calculus is credited as the Heaviside calculus.

### Evaluating improper integrals

Let ⁠ ${\mathcal {L}}\left\{f(t)\right\}=F(s)$ ⁠. Then (see the table above) $\partial _{s}{\mathcal {L}}\left\{{\frac {f(t)}{t}}\right\}=\partial _{s}\int _{0}^{\infty }{\frac {f(t)}{t}}e^{-st}\,dt=-\int _{0}^{\infty }f(t)e^{-st}dt=-F(s)$

From which one gets: ${\mathcal {L}}\left\{{\frac {f(t)}{t}}\right\}=\int _{s}^{\infty }F(p)\,dp.$

In the limit ⁠ $s\rightarrow 0$ ⁠, one gets $\int _{0}^{\infty }{\frac {f(t)}{t}}\,dt=\int _{0}^{\infty }F(p)\,dp,$ provided that the interchange of limits can be justified. This is often possible as a consequence of the final value theorem. Even when the interchange cannot be justified the calculation can be suggestive. For example, with *a* ≠ 0 ≠ *b*, proceeding formally one has ${\begin{aligned}\int _{0}^{\infty }{\frac {\cos(at)-\cos(bt)}{t}}\,dt&=\int _{0}^{\infty }\left({\frac {p}{p^{2}+a^{2}}}-{\frac {p}{p^{2}+b^{2}}}\right)\,dp\\[6pt]&=\left[{\frac {1}{2}}\ln {\frac {p^{2}+a^{2}}{p^{2}+b^{2}}}\right]_{0}^{\infty }={\frac {1}{2}}\ln {\frac {b^{2}}{a^{2}}}=\ln \left|{\frac {b}{a}}\right|.\end{aligned}}$

### Complex impedance of a capacitor

In the theory of electrical circuits, the current flow in a capacitor is proportional to the capacitance and rate of change in the electrical potential (with equations as for the SI unit system). Symbolically, this is expressed by the differential equation $i=C{dv \over dt},$ where *C* is the capacitance of the capacitor, *i* = *i*(*t*) is the electric current through the capacitor as a function of time, and *v* = *v*(*t*) is the voltage across the terminals of the capacitor, also as a function of time.

Taking the Laplace transform of this equation, we obtain $I(s)=C(sV(s)-V_{0}),$ where ${\begin{aligned}I(s)&={\mathcal {L}}\{i(t)\},\\V(s)&={\mathcal {L}}\{v(t)\},\end{aligned}}$ and $V_{0}=v(0).$

Solving for *V*(*s*) we have $V(s)={I(s) \over sC}+{V_{0} \over s}.$

The definition of the complex impedance *Z* (in ohms) is the ratio of the complex voltage *V* divided by the complex current *I* while holding the initial state *V*0 at zero: $Z(s)=\left.{V(s) \over I(s)}\right|_{V_{0}=0}.$

Using this definition and the previous equation, we find: $Z(s)={\frac {1}{sC}},$ which is the correct expression for the complex impedance of a capacitor. In addition, the Laplace transform has large applications in control theory.

### Impulse response

Consider a linear time-invariant system with transfer function $H(s)={\frac {1}{(s+\alpha )(s+\beta )}}.$

The impulse response is the inverse Laplace transform of this transfer function: $h(t)={\mathcal {L}}^{-1}\{H(s)\}.$

**Partial fraction expansion**

To evaluate this inverse transform, we begin by expanding *H*(*s*) using the method of partial fraction expansion, ${\frac {1}{(s+\alpha )(s+\beta )}}={P \over s+\alpha }+{R \over s+\beta }.$

The unknown constants *P* and *R* are the residues located at the corresponding poles of the transfer function. Each residue represents the relative contribution of that singularity to the transfer function's overall shape.

By the residue theorem, the inverse Laplace transform depends only upon the poles and their residues. To find the residue *P*, we multiply both sides of the equation by *s* + *α* to get ${\frac {1}{s+\beta }}=P+{R(s+\alpha ) \over s+\beta }.$

Then by letting *s* = −*α*, the contribution from *R* vanishes and all that is left is $P=\left.{1 \over s+\beta }\right|_{s=-\alpha }={1 \over \beta -\alpha }.$

Similarly, the residue *R* is given by $R=\left.{1 \over s+\alpha }\right|_{s=-\beta }={1 \over \alpha -\beta }.$

Note that $R={-1 \over \beta -\alpha }=-P$ and so the substitution of *R* and *P* into the expanded expression for *H*(*s*) gives $H(s)=\left({\frac {1}{\beta -\alpha }}\right)\cdot \left({1 \over s+\alpha }-{1 \over s+\beta }\right).$

Finally, using the linearity property and the known transform for exponential decay (see *Item* #*3* in the *Table of Laplace Transforms*, above), we can take the inverse Laplace transform of *H*(*s*) to obtain $h(t)={\mathcal {L}}^{-1}\{H(s)\}={\frac {1}{\beta -\alpha }}\left(e^{-\alpha t}-e^{-\beta t}\right),$ which is the impulse response of the system.

**Convolution**

The same result can be achieved using the convolution property as if the system is a series of filters with transfer functions 1/(*s* + *α*) and 1/(*s* + *β*). That is, the inverse of $H(s)={\frac {1}{(s+\alpha )(s+\beta )}}={\frac {1}{s+\alpha }}\cdot {\frac {1}{s+\beta }}$ is ${\mathcal {L}}^{-1}\!\left\{{\frac {1}{s+\alpha }}\right\}*{\mathcal {L}}^{-1}\!\left\{{\frac {1}{s+\beta }}\right\}=e^{-\alpha t}*e^{-\beta t}=\int _{0}^{t}e^{-\alpha x}e^{-\beta (t-x)}\,dx={\frac {e^{-\alpha t}-e^{-\beta t}}{\beta -\alpha }}.$

### Phase delay

| Time function | Laplace transform |
|---|---|
| $\sin {(\omega t+\varphi )}$ | ${\frac {s\sin(\varphi )+\omega \cos(\varphi )}{s^{2}+\omega ^{2}}}$ |
| $\cos {(\omega t+\varphi )}$ | ${\frac {s\cos(\varphi )-\omega \sin(\varphi )}{s^{2}+\omega ^{2}}}.$ |

Starting with the Laplace transform, $X(s)={\frac {s\sin(\varphi )+\omega \cos(\varphi )}{s^{2}+\omega ^{2}}}$ we find the inverse by first rearranging terms in the fraction: ${\begin{aligned}X(s)&={\frac {s\sin(\varphi )}{s^{2}+\omega ^{2}}}+{\frac {\omega \cos(\varphi )}{s^{2}+\omega ^{2}}}\\&=\sin(\varphi )\left({\frac {s}{s^{2}+\omega ^{2}}}\right)+\cos(\varphi )\left({\frac {\omega }{s^{2}+\omega ^{2}}}\right).\end{aligned}}$

We are now able to take the inverse Laplace transform of our terms: ${\begin{aligned}x(t)&=\sin(\varphi ){\mathcal {L}}^{-1}\left\{{\frac {s}{s^{2}+\omega ^{2}}}\right\}+\cos(\varphi ){\mathcal {L}}^{-1}\left\{{\frac {\omega }{s^{2}+\omega ^{2}}}\right\}\\&=\sin(\varphi )\cos(\omega t)+\cos(\varphi )\sin(\omega t).\end{aligned}}$

This is just the sine of the sum of the arguments, yielding: $x(t)=\sin(\omega t+\varphi ).$

We can apply similar logic to find that ${\mathcal {L}}^{-1}\left\{{\frac {s\cos \varphi -\omega \sin \varphi }{s^{2}+\omega ^{2}}}\right\}=\cos {(\omega t+\varphi )}.$

### Statistical mechanics

In statistical mechanics, the Laplace transform of the density of states $g(E)$ defines the partition function. That is, the canonical partition function $Z(\beta )$ is given by $Z(\beta )=\int _{0}^{\infty }e^{-\beta E}g(E)\,dE$ and the inverse is given by $g(E)={\frac {1}{2\pi i}}\int _{\beta _{0}-i\infty }^{\beta _{0}+i\infty }e^{\beta E}Z(\beta )\,d\beta$

### Spatial (not time) structure from astronomical spectrum

The wide and general applicability of the Laplace transform and its inverse is illustrated by an application in astronomy which provides some information on the *spatial distribution* of matter of an astronomical source of radiofrequency thermal radiation too distant to resolve as more than a point, given its flux density spectrum, rather than relating the *time* domain with the spectrum (frequency domain).

Assuming certain properties of the object, e.g. spherical shape and constant temperature, calculations based on carrying out an inverse Laplace transformation on the spectrum of the object can produce the only possible model of the distribution of matter in it (density as a function of distance from the center) consistent with the spectrum. When independent information on the structure of an object is available, the inverse Laplace transform method has been found to be in good agreement.

### Birth and death processes

Consider a random walk, with steps $\{+1,-1\}$ occurring with probabilities ⁠ $p,q=1-p$ ⁠. Suppose also that the time step is a Poisson process, with parameter ⁠ $\lambda$ ⁠. Then the probability of the walk being at the lattice point n at time t is $P_{n}(t)=\int _{0}^{t}\lambda e^{-\lambda (t-s)}(pP_{n-1}(s)+qP_{n+1}(s))\,ds\quad (+e^{-\lambda t}\quad {\text{when}}\ n=0).$ This leads to a system of integral equations (or equivalently a system of differential equations). However, because it is a system of convolution equations, the Laplace transform converts it into a system of linear equations for $\pi _{n}(s)={\mathcal {L}}(P_{n})(s),$ namely: $\pi _{n}(s)={\frac {\lambda }{\lambda +s}}(p\pi _{n-1}(s)+q\pi _{n+1}(s))\quad (+{\frac {1}{\lambda +s}}\quad {\text{when}}\ n=0)$ which may now be solved by standard methods.

### Tauberian theory

The Laplace transform of the measure $\mu$ on $[0,\infty )$ is given by ${\mathcal {L}}\mu (s)=\int _{0}^{\infty }e^{-st}d\mu (t).$ It is intuitively clear that, for small ⁠ $s>0$ ⁠, the exponentially decaying integrand will become more sensitive to the concentration of the measure $\mu$ on larger subsets of the domain. To make this more precise, introduce the distribution function: $M(t)=\mu ([0,t)).$ Formally, we expect a limit of the following kind: $\lim _{s\to 0^{+}}{\mathcal {L}}\mu (s)=\lim _{t\to \infty }M(t).$ Tauberian theorems are theorems relating the asymptotics of the Laplace transform, as ⁠ $s\to 0^{+}$ ⁠, to those of the distribution of $\mu$ as ⁠ $t\to \infty$ ⁠. They are thus of importance in asymptotic formulae of probability and statistics, where often the spectral side has asymptotics that are simpler to infer.

Two Tauberian theorems of note are the Hardy–Littlewood Tauberian theorem and Wiener's Tauberian theorem. The Wiener theorem generalizes the Ikehara Tauberian theorem, which is the following statement:

Let ⁠ $A(x)$ ⁠ be a non-negative, monotonic nondecreasing function of ⁠ x ⁠, defined for ⁠ $0\leq x<\infty$ ⁠. Suppose that $f(s)=\int _{0}^{\infty }A(x)e^{-xs}\,dx$ converges for ⁠ $\Re (s)>1$ ⁠ to the function ⁠ $f(s)$ ⁠ and that, for some non-negative number ⁠ c ⁠, $f(s)-{\frac {c}{s-1}}$ has an extension as a continuous function for ⁠ $\Re (s)\geq 1$ ⁠. Then the limit as ⁠ x ⁠ goes to infinity of ⁠ $e^{-x}A(x)$ ⁠ is equal to ⁠ c ⁠.

This statement can be applied in particular to the logarithmic derivative of Riemann zeta function, and thus provides an extremely short way to prove the prime number theorem.
