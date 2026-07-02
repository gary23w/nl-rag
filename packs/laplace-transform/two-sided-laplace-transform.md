---
title: "Two-sided Laplace transform"
source: https://en.wikipedia.org/wiki/Two-sided_Laplace_transform
domain: laplace-transform
license: CC-BY-SA-4.0
tags: laplace transform, inverse laplace transform, transfer function, final value theorem
fetched: 2026-07-02
---

# Two-sided Laplace transform

In mathematics, the **two-sided Laplace transform** or **bilateral Laplace transform** is an integral transform equivalent to probability's moment-generating function. Two-sided Laplace transforms are closely related to the Fourier transform, the Mellin transform, the Z-transform and the ordinary or one-sided Laplace transform. If ⁠ $f(t)$ ⁠ is a real- or complex-valued function of the real variable ⁠ t ⁠ defined for all real numbers, then the two-sided Laplace transform is defined by the integral

${\mathcal {B}}\{f\}(s)=F(s)=\int _{-\infty }^{\infty }e^{-st}f(t)\,dt.$

The integral is most commonly understood as an improper integral, which converges if and only if both integrals

$\int _{0}^{\infty }e^{-st}f(t)\,dt,\quad \int _{-\infty }^{0}e^{-st}f(t)\,dt$

exist. There seems to be no generally accepted notation for the two-sided transform; the ${\mathcal {B}}$ used here recalls "bilateral". The two-sided transform used by some authors is

${\mathcal {T}}\{f\}(s)=s{\mathcal {B}}\{f\}(s)=sF(s)=s\int _{-\infty }^{\infty }e^{-st}f(t)\,dt.$

In pure mathematics the argument ⁠ t ⁠ can be any variable, and Laplace transforms are used to study how differential operators transform the function.

In science and engineering applications, the argument ⁠ t ⁠ often represents time (in seconds), and the function ⁠ $f(t)$ ⁠ often represents a signal or waveform that varies with time. In these cases, the signals are transformed by filters, that work like a mathematical operator, but with a restriction. They have to be causal, which means that the output at a given time ⁠ t ⁠ cannot depend on an input that occurs at later time ⁠ $t'$ ⁠. In population ecology, the argument ⁠ t ⁠ often represents spatial displacement in a dispersal kernel.

When working with functions of time, ⁠ $f(t)$ ⁠ is called the **time domain** representation of the signal, while ⁠ $F(s)$ ⁠ is called the **s-domain** (or *Laplace domain*) representation. The inverse transformation then represents a *synthesis* of the signal as the sum of its frequency components taken over all frequencies, whereas the forward transformation represents the *analysis* of the signal into its frequency components.

## Relationship to the Fourier transform

The Fourier transform can be defined in terms of the two-sided Laplace transform ⁠ F ⁠ of a function ⁠ f ⁠:

${\mathcal {F}}\{f(t)\}=\left.F(s)\right|_{s=i\omega }=F(i\omega ).$

Note that definitions of the Fourier transform differ, and in particular

${\mathcal {F}}\{f(t)\}=\left.F(s)\right|_{s=i\omega }={\frac {1}{\sqrt {2\pi }}}{\mathcal {B}}\{f(t)\}(s)$

is often used instead. In terms of the Fourier transform, we may also obtain the two-sided Laplace transform where ⁠ $\Re (s)=0$ ⁠, as

${\mathcal {B}}\{f(t)\}(s)={\mathcal {F}}\{f(t)\}(-is).$

The Fourier transform of a function is defined over real frequencies, i.e. for pure imaginary ⁠ s ⁠ (where ⁠ $\Re (s)=0$ ⁠); for functions ⁠ f ⁠ that are upper-bounded in an absolute sense by an exponential function, the above definition converges in a strip ⁠ $a<\Im (s)<b$ ⁠ for some ⁠ a ⁠ and ⁠ b ⁠, which may not include the imaginary ⁠ s ⁠-axis.

Laplace transform is often used in control theory and signal processing, as it generally deals with linear causal system responses that may grow exponentially. The Fourier transform integral fails to converge for exponentially growing signals, which means that a linear, shift-invariant system described by it is stable or critical. The Laplace transform, on the other hand, will somewhere converge for every (causal) impulse response that grows at most exponentially. Since there are no superexponentially growing linear feedback networks, Laplace transform based analysis and solution of linear, shift-invariant systems, takes its most general form in the context of Laplace, rather than Fourier, transforms.

Laplace transform theory falls within the ambit of more general integral transforms, or even general harmonic analysis. In that framework and nomenclature, Laplace transforms are simply a form of Fourier analysis, though more general.

## Relationship to other integral transforms

If *u* is the Heaviside step function, equal to zero when its argument is less than zero, to one-half when its argument equals zero, and to one when its argument is greater than zero, then the Laplace transform ⁠ ${\mathcal {L}}$ ⁠ may be defined in terms of the two-sided Laplace transform by

${\mathcal {L}}\{f\}={\mathcal {B}}\{fu\}.$

On the other hand, we also have

${\mathcal {B}}\{f\}={\mathcal {L}}\{f\}+{\mathcal {L}}\{f\circ m\}\circ m,$

where ⁠ $m:\mathbb {R} \to \mathbb {R} :x\mapsto -x$ ⁠ is the function that multiplies by minus one, so either version of the Laplace transform can be defined in terms of the other.

The Mellin transform may be defined in terms of the two-sided Laplace transform by

${\mathcal {M}}\{f\}={\mathcal {B}}\{f\circ {\exp }\circ m\},$

with ⁠ m ⁠ as above, and conversely we can get the two-sided transform from the Mellin transform by

${\mathcal {B}}\{f\}={\mathcal {M}}\{f\circ m\circ \log \}.$

The moment-generating function of a continuous probability density function ⁠ $f(x)$ ⁠ can be expressed as ⁠ ${\mathcal {B}}\{f\}(-s)$ ⁠.

## Properties

The following properties can be found in Bracewell (2000) and Oppenheim & Willsky (1997)

| Property | Time domain | *s* domain | Strip of convergence | Comment |
|---|---|---|---|---|
| Definition | $f(t)$ | $F(s)={\mathcal {B}}\{f\}(s)=\int _{-\infty }^{\infty }f(t)\,e^{-st}\,dt$ | $\alpha <\Re (s)<\beta$ |   |
| Time scaling | $f(at)$ | ${\frac {1}{\|a\|}}F\left({s \over a}\right)$ | $\alpha <a^{-1}\,\Re (s)<\beta$ | $a\in \mathbb {R} \smallsetminus \{0\}$ |
| Reversal | $f(-t)$ | $F(-s)$ | $-\beta <\Re (s)<-\alpha$ |   |
| Frequency-domain derivative | $tf(t)$ | $-F'(s)$ | $\alpha <\Re (s)<\beta$ |   |
| Frequency-domain general derivative | $t^{n}f(t)$ | $(-1)^{n}\,F^{(n)}(s)$ | $\alpha <\Re (s)<\beta$ |   |
| Derivative | $f'(t)$ | $sF(s)$ | $\alpha <\Re (s)<\beta$ |   |
| General derivative | $f^{(n)}(t)$ | $s^{n}\,F(s)$ | $\alpha <\Re (s)<\beta$ |   |
| Frequency-domain integration | ${\frac {1}{t}}\,f(t)$ | $\int _{s}^{\infty }F(\sigma )\,d\sigma$ |   | only valid if the integral exists |
| Time-domain integral | $\int _{-\infty }^{t}f(\tau )\,d\tau$ | ${1 \over s}F(s)$ | $\max(\alpha ,0)<\Re (s)<\beta$ |   |
| Time-domain integral | $\int _{t}^{\infty }f(\tau )\,d\tau$ | ${1 \over s}F(s)$ | $\alpha <\Re (s)<\min(\beta ,0)$ |   |
| Frequency shifting | $e^{at}\,f(t)$ | $F(s-a)$ | $\alpha +\Re (a)<\Re (s)<\beta +\Re (a)$ |   |
| Time shifting | $f(t-a)$ | $e^{-as}\,F(s)$ | $\alpha <\Re (s)<\beta$ | $a\in \mathbb {R}$ |
| Modulation | $\cos(at)\,f(t)$ | ${\tfrac {1}{2}}F(s-ia)+{\tfrac {1}{2}}F(s+ia)$ | $\alpha <\Re (s)<\beta$ | $a\in \mathbb {R}$ |
| Finite difference | $f(t+{\tfrac {1}{2}}a)-f(t-{\tfrac {1}{2}}a)$ | $2\sinh({\tfrac {1}{2}}as)\,F(s)$ | $\alpha <\Re (s)<\beta$ | $a\in \mathbb {R}$ |
| Multiplication | $f(t)\,g(t)$ | ${\frac {1}{2\pi i}}\int _{c-i\infty }^{c+i\infty }F(\sigma )G(s-\sigma )\,d\sigma \$ | $\alpha _{f}+\alpha _{g}<\Re (s)<\beta _{f}+\beta _{g}$ | $\alpha _{f}<c<\beta _{f}$ . The integration is done along the vertical line ⁠ $\Re (\sigma )=c$ ⁠ inside the region of convergence. |
| Complex conjugation | ${\overline {f(t)}}$ | ${\overline {F({\overline {s}})}}$ | $\alpha <\Re (s)<\beta$ |   |
| Convolution | $(f*g)(t)=\int _{-\infty }^{\infty }f(\tau )\,g(t-\tau )\,d\tau$ | $F(s)\cdot G(s)\$ | $\max(\alpha _{f},\alpha _{g})<\Re (s)<\min(\beta _{f},\beta _{g})$ |   |
| Cross-correlation | $(f\star g)(t)=\int _{-\infty }^{\infty }{\overline {f(\tau )}}\,g(t+\tau )\,d\tau$ | ${\overline {F(-{\overline {s}})}}\cdot G(s)$ | $\max(-\beta _{f},\alpha _{g})<\Re (s)<\min(-\alpha _{f},\beta _{g})$ |   |

Most properties of the bilateral Laplace transform are very similar to properties of the unilateral Laplace transform, but there are some important differences:

|   | unilateral time domain | bilateral time domain | unilateral-'s' domain | bilateral-'s' domain |
|---|---|---|---|---|
| Differentiation | $f'(t)$ | $f'(t)$ | $sF(s)-f(0)$ | $sF(s)$ |
| Second-order differentiation | $f''(t)$ | $f''(t)$ | $s^{2}F(s)-sf(0)-f'(0)$ | $s^{2}F(s)$ |
| Convolution | $\int _{0}^{t}f(\tau )\,g(t-\tau )\,d\tau$ | $\int _{-\infty }^{\infty }f(\tau )\,g(t-\tau )\,d\tau$ | $F(s)\cdot G(s)$ | $F(s)\cdot G(s)$ |

### Parseval's theorem and Plancherel's theorem

Let ⁠ $f_{1}(t)$ ⁠ and ⁠ $f_{2}(t)$ ⁠ be functions with bilateral Laplace transforms ⁠ $F_{1}(s)$ ⁠ and ⁠ $F_{2}(s)$ ⁠ in the strips of convergence ⁠ $\alpha _{1,2}<\Re (s)<\beta _{1,2}$ ⁠. Let ⁠ $c\in \mathbb {R}$ ⁠ with ⁠ $\max(-\beta _{1},\alpha _{2})<c<\min(-\alpha _{1},\beta _{2})$ ⁠. Then Parseval's theorem holds:

$\int _{-\infty }^{\infty }{\overline {f_{1}(t)}}\,f_{2}(t)\,dt={\frac {1}{2\pi i}}\int _{c-i\infty }^{c+i\infty }{\overline {F_{1}(-{\overline {s}})}}\,F_{2}(s)\,ds$

This theorem is proved by applying the inverse Laplace transform on the convolution theorem in form of the cross-correlation.

Let ⁠ $f(t)$ ⁠ be a function with bilateral Laplace transform ⁠ $F(s)$ ⁠ in the strip of convergence ⁠ $\alpha <\Re (s)<\beta$ ⁠. Let ⁠ $c\in \mathbb {R}$ ⁠ with ⁠ $\alpha <c<\beta$ ⁠. Then the Plancherel theorem holds:

$\int _{-\infty }^{\infty }e^{-2c\,t}\,|f(t)|^{2}\,dt={\frac {1}{2\pi }}\int _{-\infty }^{\infty }|F(c+ir)|^{2}\,dr$

### Uniqueness

For any two functions ⁠ f ⁠ and ⁠ g ⁠ for which the two-sided Laplace transforms ⁠ ${\mathcal {T}}\{f\}$ ⁠, ⁠ ${\mathcal {T}}\{g\}$ ⁠ exist, if ⁠ ${\mathcal {T}}\{f\}={\mathcal {T}}\{g\}$ ⁠, i.e. ⁠ ${\mathcal {T}}\{f\}(s)={\mathcal {T}}\{g\}(s)$ ⁠ for every value of ⁠ $s\in \mathbb {R}$ ⁠, then ⁠ $f=g$ ⁠ almost everywhere.

## Region of convergence

Bilateral transform requirements for convergence are more difficult than for unilateral transforms. The region of convergence will be normally smaller.

If ⁠ f ⁠ is a locally integrable function (or more generally a Borel measure locally of bounded variation), then the Laplace transform ⁠ $F(s)$ ⁠ of ⁠ f ⁠ converges provided that the limit

$\lim _{R\to \infty }\int _{0}^{R}f(t)e^{-st}\,dt$

exists. The Laplace transform converges absolutely if the integral

$\int _{0}^{\infty }\left|f(t)e^{-st}\right|\,dt$

exists (as a proper Lebesgue integral). The Laplace transform is usually understood as conditionally convergent, meaning that it converges in the former instead of the latter sense.

The set of values for which ⁠ $F(s)$ ⁠ converges absolutely is either of the form ⁠ $\Re (s)>a$ ⁠ or else ⁠ $\Re (s)\geq a$ ⁠, where ⁠ a ⁠ is an extended real constant, ⁠ $-\infty \leq a\leq \infty$ ⁠. (This follows from the dominated convergence theorem.) The constant ⁠ a ⁠ is known as the abscissa of absolute convergence, and depends on the growth behavior of ⁠ $f(t)$ ⁠. Analogously, the two-sided transform converges absolutely in a strip of the form ⁠ $a<\Re (s)<b$ ⁠, and possibly including the lines ⁠ $\Re (s)=a$ ⁠ or ⁠ $\Re (s)=b$ ⁠. The subset of values of ⁠ s ⁠ for which the Laplace transform converges absolutely is called the region of absolute convergence or the domain of absolute convergence. In the two-sided case, it is sometimes called the strip of absolute convergence. The Laplace transform is analytic in the region of absolute convergence.

Similarly, the set of values for which ⁠ $F(s)$ ⁠ converges (conditionally or absolutely) is known as the region of conditional convergence, or simply the **region of convergence** (ROC). If the Laplace transform converges (conditionally) at ⁠ $s=s_{0}$ ⁠, then it automatically converges for all ⁠ s ⁠ with ⁠ $\Re (s)>\Re (s_{0})$ ⁠). Therefore, the region of convergence is a half-plane of the form ⁠ $\Re (s)>a$ ⁠, possibly including some points of the boundary line ⁠ $\Re (s)=a$ ⁠. In the region of convergence, ⁠ $\Re (s)>\Re (s_{0})$ ⁠), the Laplace transform of ⁠ f ⁠ can be expressed by integrating by parts as the integral

$F(s)=(s-s_{0})\int _{0}^{\infty }e^{-(s-s_{0})t}\beta (t)\,dt,\quad \beta (u)=\int _{0}^{u}e^{-s_{0}t}f(t)\,dt.$

That is, in the region of convergence ⁠ $F(s)$ ⁠ can effectively be expressed as the absolutely convergent Laplace transform of some other function. In particular, it is analytic.

There are several Paley–Wiener theorems concerning the relationship between the decay properties of ⁠ f ⁠ and the properties of the Laplace transform within the region of convergence.

In engineering applications, a function corresponding to a linear time-invariant (LTI) system is *stable* if every bounded input produces a bounded output.

## Causality

Bilateral transforms do not respect causality. They make sense when applied over generic functions but when working with functions of time (signals) unilateral transforms are preferred.

## Table of selected bilateral Laplace transforms

Following list of interesting examples for the bilateral Laplace transform can be deduced from the corresponding Fourier or unilateral Laplace transformations (see also Bracewell (2000)):

| Function | Time domain ⁠ $f(t)={\mathcal {B}}^{-1}\{F\}(t)$ ⁠ | Laplace s-domain ⁠ $F(s)={\mathcal {B}}\{f\}(s)$ ⁠ | Region of convergence | Comment |
|---|---|---|---|---|
| Rectangular impulse | $f(t)=\left\{{\begin{aligned}1&\quad {\text{if}}\;\|t\|<{\tfrac {1}{2}}\\{\tfrac {1}{2}}&\quad {\text{if}}\;\|t\|={\tfrac {1}{2}}\\0&\quad {\text{if}}\;\|t\|>{\tfrac {1}{2}}\end{aligned}}\right.$ | $2s^{-1}\,\sinh {\frac {s}{2}}$ | $-\infty <\Re (s)<\infty$ |   |
| Triangular impulse | $f(t)=\left\{{\begin{aligned}1-\|t\|&\quad {\text{if}}\;\|t\|\leq 1\\0&\quad {\text{if}}\;\|t\|>1\end{aligned}}\right.$ | $\left(2s^{-1}\,\sinh {\frac {s}{2}}\right)^{2}$ | $-\infty <\Re (s)<\infty$ |   |
| Gaussian impulse | $\exp \left(-a^{2}\,t^{2}-b\,t\right)$ | ${\frac {\sqrt {\pi }}{a}}\,\exp {\frac {(s+b)^{2}}{4\,a^{2}}}$ | $-\infty <\Re (s)<\infty$ | $\Re (a^{2})>0$ |
| Exponential decay | $e^{-at}\,u(t)=\left\{{\begin{aligned}&0&&\;{\text{if}}\;t<0&\\&e^{-at}&&\;{\text{if}}\;0<t&\end{aligned}}\right.$ | ${\frac {1}{s+a}}$ | $-\Re (a)<\Re (s)<\infty$ | $u(t)$ is the Heaviside step function |
| Exponential growth | $-e^{-at}\,u(-t)=\left\{{\begin{aligned}&-e^{-at}&&\;{\text{if}}\;t<0&\\&0&&\;{\text{if}}\;0<t&\end{aligned}}\right.$ | ${\frac {1}{s+a}}$ | $-\infty <\Re (s)<-\Re (a)$ |   |
|   | $e^{-\|t\|}$ | ${\frac {2}{1-s^{2}}}$ | $-1<\Re (s)<1$ |   |
|   | $e^{-a\|t\|}$ | ${\frac {2a}{a^{2}-s^{2}}}$ | $-\Re (a)<\Re (s)<\Re (a)$ | $\Re (a)>0$ |
|   | ${\frac {1}{\cosh t}}$ | ${\frac {\pi }{\cos(\pi s/2)}}$ | $-1<\Re (s)<1$ |   |
|   | ${\frac {1}{1+e^{-t}}}$ | ${\frac {\pi }{\sin(\pi s)}}$ | $0<\Re (s)<1$ |   |
