---
title: "Fundamental solution"
source: https://en.wikipedia.org/wiki/Fundamental_solution
domain: greens-functions
license: CC-BY-SA-4.0
tags: green's function, fundamental solution, method of images, propagator function
fetched: 2026-07-02
---

# Fundamental solution

In mathematics, a **fundamental solution** for a linear partial differential operator L is a formulation in the language of distribution theory of the older idea of a Green's function (although unlike Green's functions, fundamental solutions do not address boundary conditions).

In terms of the Dirac delta function *δ*(*x*), a fundamental solution F is a solution of the inhomogeneous equation

LF

=

δ

(

x

)

.

Here F is *a priori* only assumed to be a distribution.

This concept has long been utilized for the Laplacian in two and three dimensions. It was investigated for all dimensions for the Laplacian by Marcel Riesz.

The existence of a fundamental solution for any operator with constant coefficients — the most important case, directly linked to the possibility of using convolution to solve an arbitrary right hand side — was shown by Bernard Malgrange and Leon Ehrenpreis, and a proof is available in Joel Smoller (1994). In the context of functional analysis, fundamental solutions are usually developed via the Fredholm alternative and explored in Fredholm theory.

## Example

Consider the following differential equation *Lf* = sin(*x*) with $L={\frac {d^{2}}{dx^{2}}}.$

The fundamental solutions can be obtained by solving *LF* = *δ*(*x*), explicitly, ${\frac {d^{2}}{dx^{2}}}F(x)=\delta (x)\,.$

Since for the unit step function (also known as the Heaviside function) H we have ${\frac {d}{dx}}H(x)=\delta (x)\,,$ there is a solution ${\frac {d}{dx}}F(x)=H(x)+C\,.$ Here C is an arbitrary constant introduced by the integration. For convenience, set *C* = −1/2.

After integrating ${\frac {dF}{dx}}$ and choosing the new integration constant as zero, one has $F(x)=xH(x)-{\frac {1}{2}}x={\frac {1}{2}}|x|~.$

## Motivation

Once the fundamental solution is found, it is straightforward to find a solution of the original equation, through convolution of the fundamental solution and the desired right hand side.

Fundamental solutions also play an important role in the numerical solution of partial differential equations by the boundary element method.

### Application to the example

Consider the operator L and the differential equation mentioned in the example, ${\frac {d^{2}}{dx^{2}}}f(x)=\sin(x)\,.$

We can find the solution $f(x)$ of the original equation by convolution (denoted by an asterisk) of the right-hand side $\sin(x)$ with the fundamental solution ${\textstyle F(x)={\frac {1}{2}}|x|}$ : $f(x)=(F*\sin )(x):=\int _{-\infty }^{\infty }{\frac {1}{2}}|x-y|\sin(y)\,dy\,.$

This shows that some care must be taken when working with functions which do not have enough regularity (e.g. compact support, *L*1 integrability) since, we know that the desired solution is *f*(*x*) = −sin(*x*), while the above integral diverges for all x. The two expressions for f are, however, equal as distributions.

### An example that more clearly works

${\frac {d^{2}}{dx^{2}}}f(x)=I(x)\,,$ where I is the characteristic (indicator) function of the unit interval [0,1]. In that case, it can be verified that the convolution of *I* with *F*(*x*) = |*x*|/2 is $(I*F)(x)={\begin{cases}{\frac {1}{2}}x^{2}-{\frac {1}{2}}x+{\frac {1}{4}},&0\leq x\leq 1\\|{\frac {1}{2}}x-{\frac {1}{4}}|,&{\text{otherwise}}\end{cases}}$ which is a solution, i.e., has second derivative equal to I.

### Proof that the convolution is a solution

Denote the convolution of functions F and g as *F* ∗ *g*. Say we are trying to find the solution of *Lf* = *g*(*x*). We want to prove that *F* ∗ *g* is a solution of the previous equation, i.e. we want to prove that *L*(*F* ∗ *g*) = *g*. When applying the differential operator with constant coefficients, L, to the convolution, it is known that $L(F*g)=(LF)*g\,,$ provided L has constant coefficients.

If F is the fundamental solution, the right side of the equation reduces to $\delta *g~.$

But since the delta function is an identity element for convolution, this is simply *g*(*x*). Summing up, $L(F*g)=(LF)*g=\delta (x)*g(x)=\int _{-\infty }^{\infty }\delta (x-y)g(y)\,dy=g(x)\,.$

Therefore, if F is the fundamental solution, the convolution *F* ∗ *g* is one solution of *Lf* = *g*(*x*). This does not mean that it is the only solution. Several solutions for different initial conditions can be found.

## Fundamental solutions for some partial differential equations

The following can be obtained by means of Fourier transform:

### Laplace equation

For the Laplace equation, $[-\Delta ]\Phi (\mathbf {x} ,\mathbf {x} ')=\delta (\mathbf {x} -\mathbf {x} ')$ the fundamental solutions in two and three dimensions, respectively, are $\Phi _{\textrm {2D}}(\mathbf {x} ,\mathbf {x} ')=-{\frac {1}{2\pi }}\ln |\mathbf {x} -\mathbf {x} '|,\qquad \Phi _{\textrm {3D}}(\mathbf {x} ,\mathbf {x} ')={\frac {1}{4\pi |\mathbf {x} -\mathbf {x} '|}}~.$

### Screened Poisson equation

For the screened Poisson equation, $[-\Delta +k^{2}]\Phi (\mathbf {x} ,\mathbf {x} ')=\delta (\mathbf {x} -\mathbf {x} '),\quad k\in \mathbb {R} ,$ the fundamental solutions are $\Phi _{\textrm {2D}}(\mathbf {x} ,\mathbf {x} ')={\frac {1}{2\pi }}K_{0}(k|\mathbf {x} -\mathbf {x} '|),\qquad \Phi _{\textrm {3D}}(\mathbf {x} ,\mathbf {x} ')={\frac {\exp(-k|\mathbf {x} -\mathbf {x} '|)}{4\pi |\mathbf {x} -\mathbf {x} '|}},$ where $K_{0}$ is a modified Bessel function of the second kind.

In higher dimensions the fundamental solution of the screened Poisson equation is given by the Bessel potential.

### Biharmonic equation

For the Biharmonic equation, $[-\Delta ^{2}]\Phi (\mathbf {x} ,\mathbf {x} ')=\delta (\mathbf {x} -\mathbf {x} ')$ the biharmonic equation has the fundamental solutions $\Phi _{\textrm {2D}}(\mathbf {x} ,\mathbf {x} ')=-{\frac {|\mathbf {x} -\mathbf {x} '|^{2}}{8\pi }}\ln |\mathbf {x} -\mathbf {x} '|,\qquad \Phi _{\textrm {3D}}(\mathbf {x} ,\mathbf {x} ')={\frac {|\mathbf {x} -\mathbf {x} '|}{8\pi }}~.$

## Signal processing

In signal processing, the analog of the fundamental solution of a differential equation is called the impulse response of a filter.
