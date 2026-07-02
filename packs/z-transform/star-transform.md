---
title: "Starred transform"
source: https://en.wikipedia.org/wiki/Star_transform
domain: z-transform
license: CC-BY-SA-4.0
tags: z-transform, bilinear transform, region of convergence, digital filter
fetched: 2026-07-02
---

# Starred transform

(Redirected from

Star transform

)

In applied mathematics, the **starred transform**, or **star transform**, is a discrete-time variation of the Laplace transform, so-named because of the asterisk or "star" in the customary notation of the sampled signals. The transform is an operator of a continuous-time function $x(t)$ , which is transformed to a function $X^{*}(s)$ in the following manner:

${\begin{aligned}X^{*}(s)={\mathcal {L}}[x(t)\cdot \delta _{T}(t)]={\mathcal {L}}[x^{*}(t)],\end{aligned}}$

where $\delta _{T}(t)$ is a Dirac comb function, with period of time T.

The starred transform is a convenient mathematical abstraction that represents the Laplace transform of an *impulse sampled* function $x^{*}(t)$ , which is the output of an *ideal sampler*, whose input is a continuous function, $x(t)$ .

The starred transform is similar to the Z transform, with a simple change of variables, where the starred transform is explicitly declared in terms of the sampling period (T), while the Z transform is performed on a discrete signal and is independent of the sampling period. This makes the starred transform a de-normalized version of the one-sided Z-transform, as it restores the dependence on sampling parameter *T*.

## Relation to Laplace transform

Since $X^{*}(s)={\mathcal {L}}[x^{*}(t)]$ , where:

${\begin{aligned}x^{*}(t)\ {\stackrel {\mathrm {def} }{=}}\ x(t)\cdot \delta _{T}(t)&=x(t)\cdot \sum _{n=0}^{\infty }\delta (t-nT).\end{aligned}}$

Then per the convolution theorem, the starred transform is equivalent to the complex convolution of ${\mathcal {L}}[x(t)]=X(s)$ and ${\mathcal {L}}[\delta _{T}(t)]={\frac {1}{1-e^{-Ts}}}$ , hence:

$X^{*}(s)={\frac {1}{2\pi j}}\int _{c-j\infty }^{c+j\infty }{X(p)\cdot {\frac {1}{1-e^{-T(s-p)}}}\cdot dp}.$

This line integration is equivalent to integration in the positive sense along a closed contour formed by such a line and an infinite semicircle that encloses the poles of X(s) in the left half-plane of *p*. The result of such an integration (per the residue theorem) would be:

$X^{*}(s)=\sum _{\lambda ={\text{poles of }}X(s)}\operatorname {Res} \limits _{p=\lambda }{\bigg [}X(p){\frac {1}{1-e^{-T(s-p)}}}{\bigg ]}.$

Alternatively, the aforementioned line integration is equivalent to integration in the negative sense along a closed contour formed by such a line and an infinite semicircle that encloses the infinite poles of ${\frac {1}{1-e^{-T(s-p)}}}$ in the right half-plane of *p*. The result of such an integration would be:

$X^{*}(s)={\frac {1}{T}}\sum _{k=-\infty }^{\infty }X\left(s-j{\tfrac {2\pi }{T}}k\right)+{\frac {x(0)}{2}}.$

## Relation to Z transform

Given a Z-transform, *X*(*z*), the corresponding starred transform is a simple substitution**:**

${\bigg .}X^{*}(s)=X(z){\bigg |}_{\displaystyle z=e^{sT}}$

This substitution restores the dependence on *T*.

It's interchangeable,

${\bigg .}X(z)=X^{*}(s){\bigg |}_{\displaystyle e^{sT}=z}$

${\bigg .}X(z)=X^{*}(s){\bigg |}_{\displaystyle s={\frac {\ln(z)}{T}}}$

## Properties of the starred transform

**Property 1:**   $X^{*}(s)$ is periodic in s with period $j{\tfrac {2\pi }{T}}.$

$X^{*}(s+j{\tfrac {2\pi }{T}}k)=X^{*}(s)$

**Property 2:**  If $X(s)$ has a pole at $s=s_{1}$ , then $X^{*}(s)$ must have poles at $s=s_{1}+j{\tfrac {2\pi }{T}}k$ , where $\scriptstyle k=0,\pm 1,\pm 2,\ldots$
