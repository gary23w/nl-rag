---
title: "Hilbert transform"
source: https://en.wikipedia.org/wiki/Hilbert_transform
domain: integral-transforms
license: CC-BY-SA-4.0
tags: integral transform, hilbert transform, hartley transform, convolution theorem
fetched: 2026-07-02
---

# Hilbert transform

In mathematics and signal processing, the **Hilbert transform** is a specific singular integral that takes a function, *u*(*t*) of a real variable and produces another function of a real variable H(*u*)(*t*). The Hilbert transform is given by the Cauchy principal value of the convolution with the function $1/(\pi t)$ (see § Definition). The Hilbert transform has a particularly simple representation in the frequency domain: It imparts a phase shift of ±90° (π/2 radians) to every frequency component of a function, the sign of the shift depending on the sign of the frequency (see § Relationship with the Fourier transform). The Hilbert transform is important in signal processing, where it is a component of the analytic representation of a real-valued signal *u*(*t*). The Hilbert transform was first introduced by David Hilbert in this setting, to solve a special case of the Riemann–Hilbert problem for analytic functions.

## Definition

The Hilbert transform of u can be thought of as the convolution of *u*(*t*) with the function *h*(*t*) = ⁠1/π*t*⁠, known as the Cauchy kernel. Because 1/t is not integrable across *t* = 0, the integral defining the convolution does not always converge. Instead, the Hilbert transform is defined using the Cauchy principal value (denoted here by p.v.). Explicitly, the Hilbert transform of a function (or signal) *u*(*t*) is given by

$\operatorname {H} (u)(t)={\frac {1}{\pi }}\,\operatorname {p.v.} \int _{-\infty }^{+\infty }{\frac {u(\tau )}{t-\tau }}\,\mathrm {d} \tau ,$

provided this integral exists as a principal value. This is precisely the convolution of u with the tempered distribution p.v. ⁠1/π*t*⁠. Alternatively, by changing variables, the principal-value integral can be written explicitly as

$\operatorname {H} (u)(t)={\frac {2}{\pi }}\,\lim _{\varepsilon \to 0}\int _{\varepsilon }^{\infty }{\frac {u(t-\tau )-u(t+\tau )}{2\tau }}\,\mathrm {d} \tau .$

When the Hilbert transform is applied twice in succession to a function u, the result is

$\operatorname {H} {\bigl (}\operatorname {H} (u){\bigr )}(t)=-u(t),$

provided the integrals defining both iterations converge in a suitable sense. In particular, the inverse transform is $-\operatorname {H}$ . This fact can most easily be seen by considering the effect of the Hilbert transform on the Fourier transform of *u*(*t*) (see § Relationship with the Fourier transform below).

For an analytic function in the upper half-plane, the Hilbert transform describes the relationship between the real part and the imaginary part of the boundary values. That is, if *f*(*z*) is analytic in the upper half complex plane {*z* : Im{*z*} > 0}, and *u*(*t*) = Re{*f* (*t* + 0·*i*)}, then Im{*f*(*t* + 0·*i*)} = H(*u*)(*t*) up to an additive constant, provided this Hilbert transform exists.

### Notation

In signal processing the Hilbert transform of *u*(*t*) is commonly denoted by ${\hat {u}}(t)$ . However, in mathematics, this notation is already extensively used to denote the Fourier transform of *u*(*t*). Occasionally, the Hilbert transform may be denoted by ${\tilde {u}}(t)$ . Furthermore, many sources define the Hilbert transform as the negative of the one defined here.

## History

The Hilbert transform arose in Hilbert's 1905 work on a problem Riemann posed concerning analytic functions, which has come to be known as the Riemann–Hilbert problem. Hilbert's work was mainly concerned with the Hilbert transform for functions defined on the circle. Some of his earlier work related to the Discrete Hilbert Transform dates back to lectures he gave in Göttingen. The results were later published by Hermann Weyl in his dissertation. Schur improved Hilbert's results about the discrete Hilbert transform and extended them to the integral case. These results were restricted to the spaces *L*2 and ℓ2. In 1928, Marcel Riesz proved that the Hilbert transform can be defined for *u* in $L^{p}(\mathbb {R} )$ (Lp space) for 1 < *p* < ∞, that the Hilbert transform is a bounded operator on $L^{p}(\mathbb {R} )$ for 1 < *p* < ∞, and that similar results hold for the Hilbert transform on the circle as well as the discrete Hilbert transform. The Hilbert transform was a motivating example for Antoni Zygmund and Alberto Calderón during their study of singular integrals. Their investigations have played a fundamental role in modern harmonic analysis. Various generalizations of the Hilbert transform, such as the bilinear and trilinear Hilbert transforms are still active areas of research today.

## Relationship with the Fourier transform

The Hilbert transform is a multiplier operator. The multiplier of H is *σ*H(*ω*) = −*i* sgn(*ω*), where sgn is the signum function. Therefore:

${\mathcal {F}}{\bigl (}\operatorname {H} (u){\bigr )}(\omega )=-i\operatorname {sgn}(\omega )\cdot {\mathcal {F}}(u)(\omega ),$

where ${\mathcal {F}}$ denotes the Fourier transform. Since sgn(*x*) = sgn(2π*x*), it follows that this result applies to the three common definitions of ${\mathcal {F}}$ .

By Euler's formula, $\sigma _{\operatorname {H} }(\omega )={\begin{cases}~~i=e^{+i\pi /2}&{\text{if }}\omega <0\\~~0&{\text{if }}\omega =0\\-i=e^{-i\pi /2}&{\text{if }}\omega >0\end{cases}}$

Therefore, H(*u*)(*t*) has the effect of shifting the phase of the negative frequency components of *u*(*t*) by +90° (π⁄2 radians) and the phase of the positive frequency components by −90°, and *i*·H(*u*)(*t*) has the effect of restoring the positive frequency components while shifting the negative frequency ones an additional +90°, resulting in their negation (i.e., a multiplication by −1).

When the Hilbert transform is applied twice, the phase of the negative and positive frequency components of *u*(*t*) are respectively shifted by +180° and −180°, which are equivalent amounts. The signal is negated; i.e., H(H(*u*)) = −*u*, because

$\left(\sigma _{\operatorname {H} }(\omega )\right)^{2}=e^{\pm i\pi }=-1\quad {\text{for }}\omega \neq 0.$

## Table of selected Hilbert transforms

In the following table, the frequency parameter $\omega$ is real.

| Signal $u(t)$ | Hilbert transform $\operatorname {H} (u)(t)$ |
|---|---|
| $\sin(\omega t+\varphi )$ | ${\begin{array}{lll}\sin \left(\omega t+\varphi -{\tfrac {\pi }{2}}\right)=-\cos \left(\omega t+\varphi \right),\quad \omega >0\\\sin \left(\omega t+\varphi +{\tfrac {\pi }{2}}\right)=\cos \left(\omega t+\varphi \right),\quad \omega <0\end{array}}$ |
| $\cos(\omega t+\varphi )$ | ${\begin{array}{lll}\cos \left(\omega t+\varphi -{\tfrac {\pi }{2}}\right)=\sin \left(\omega t+\varphi \right),\quad \omega >0\\\cos \left(\omega t+\varphi +{\tfrac {\pi }{2}}\right)=-\sin \left(\omega t+\varphi \right),\quad \omega <0\end{array}}$ |
| $e^{i\omega t}$ | ${\begin{array}{lll}e^{i\left(\omega t-{\tfrac {\pi }{2}}\right)},\quad \omega >0\\e^{i\left(\omega t+{\tfrac {\pi }{2}}\right)},\quad \omega <0\end{array}}$ |
| $e^{-i\omega t}$ | ${\begin{array}{lll}e^{-i\left(\omega t-{\tfrac {\pi }{2}}\right)},\quad \omega >0\\e^{-i\left(\omega t+{\tfrac {\pi }{2}}\right)},\quad \omega <0\end{array}}$ |
| $1 \over t^{2}+1$ | $t \over t^{2}+1$ |
| $e^{-t^{2}}$ | ${\frac {2}{\sqrt {\pi \,}}}F(t)$ (see Dawson function) |
| **Sinc function** $\sin(t) \over t$ | $1-\cos(t) \over t$ |
| **Dirac delta function** $\delta (t)$ | ${1 \over \pi t}$ |
| **Characteristic function** $\chi _{[a,b]}(t)$ | ${{\frac {1}{\,\pi \,}}\ln \left\vert {\frac {t-a}{t-b}}\right\vert }$ |

**Notes**

1. Some authors (e.g., Bracewell) use our −H as their definition of the forward transform. A consequence is that the right column of this table would be negated.
2. The Hilbert transform of the sin and cos functions can be defined by taking the principal value of the integral at infinity. This definition agrees with the result of defining the Hilbert transform distributionally.

An extensive table of Hilbert transforms is available. Note that the Hilbert transform of a constant is zero.

## Domain of definition

It is by no means obvious that the Hilbert transform is well-defined at all, as the improper integral defining it must converge in a suitable sense. However, the Hilbert transform is well-defined for a broad class of functions, namely those in $L^{p}(\mathbb {R} )$ for 1 < *p* < ∞.

More precisely, if u is in $L^{p}(\mathbb {R} )$ for 1 < *p* < ∞, then the limit defining the improper integral

$\operatorname {H} (u)(t)={\frac {2}{\pi }}\lim _{\varepsilon \to 0}\int _{\varepsilon }^{\infty }{\frac {u(t-\tau )-u(t+\tau )}{2\tau }}\,d\tau$

exists for almost every t. The limit function is also in $L^{p}(\mathbb {R} )$ and is in fact the limit in the mean of the improper integral as well. That is,

${\frac {2}{\pi }}\int _{\varepsilon }^{\infty }{\frac {u(t-\tau )-u(t+\tau )}{2\tau }}\,\mathrm {d} \tau \to \operatorname {H} (u)(t)$

as *ε* → 0 in the Lp norm, as well as pointwise almost everywhere, by the Titchmarsh theorem.

In the case *p* = 1, the Hilbert transform still converges pointwise almost everywhere, but may itself fail to be integrable, even locally. In particular, convergence in the mean does not in general happen in this case. The Hilbert transform of an *L*1 function does converge, however, in *L*1-weak, and the Hilbert transform is a bounded operator from *L*1 to *L*1,w. (In particular, since the Hilbert transform is also a multiplier operator on *L*2, Marcinkiewicz interpolation and a duality argument furnishes an alternative proof that H is bounded on *L**p*.)

## Properties

### Boundedness

If 1 < *p* < ∞, then the Hilbert transform on $L^{p}(\mathbb {R} )$ is a bounded linear operator, meaning that there exists a constant Cp such that

$\left\|\operatorname {H} u\right\|_{p}\leq C_{p}\left\|u\right\|_{p}$

for all $u\in L^{p}(\mathbb {R} )$ .

The best constant $C_{p}$ is given by $C_{p}={\begin{cases}\tan {\frac {\pi }{2p}}&{\text{if}}~1<p\leq 2\\[4pt]\cot {\frac {\pi }{2p}}&{\text{if}}~2<p<\infty \end{cases}}$

An easy way to find the best $C_{p}$ for p being a power of 2 is through the so-called Cotlar's identity that $(\operatorname {H} f)^{2}=f^{2}+2\operatorname {H} (f\operatorname {H} f)$ for all real valued f. The same best constants hold for the periodic Hilbert transform.

The boundedness of the Hilbert transform implies the $L^{p}(\mathbb {R} )$ convergence of the symmetric partial sum operator $S_{R}f=\int _{-R}^{R}{\hat {f}}(\xi )e^{2\pi ix\xi }\,\mathrm {d} \xi$

to f in $L^{p}(\mathbb {R} )$ .

### Anti-self adjointness

The Hilbert transform is an anti-self adjoint operator relative to the duality pairing between $L^{p}(\mathbb {R} )$ and the dual space $L^{q}(\mathbb {R} )$ , where p and q are Hölder conjugates and 1 < *p*, *q* < ∞. Symbolically,

$\langle \operatorname {H} u,v\rangle =\langle u,-\operatorname {H} v\rangle$

for $u\in L^{p}(\mathbb {R} )$ and $v\in L^{q}(\mathbb {R} )$ .

### Inverse transform

The Hilbert transform is an anti-involution, meaning that

$\operatorname {H} {\bigl (}\operatorname {H} \left(u\right){\bigr )}=-u$

provided each transform is well-defined. Since H preserves the space $L^{p}(\mathbb {R} )$ , this implies in particular that the Hilbert transform is invertible on $L^{p}(\mathbb {R} )$ , and that

$\operatorname {H} ^{-1}=-\operatorname {H}$

### Complex structure

Because H2 = −I ("I" is the identity operator) on the real Banach space of *real*-valued functions in $L^{p}(\mathbb {R} )$ , the Hilbert transform defines a linear complex structure on this Banach space. In particular, when *p* = 2, the Hilbert transform gives the Hilbert space of real-valued functions in $L^{2}(\mathbb {R} )$ the structure of a *complex* Hilbert space.

The (complex) eigenstates of the Hilbert transform admit representations as holomorphic functions in the upper and lower half-planes in the Hardy space H2 by the Paley–Wiener theorem.

### Differentiation

Formally, the derivative of the Hilbert transform is the Hilbert transform of the derivative, i.e. these two linear operators commute:

$\operatorname {H} \left({\frac {\mathrm {d} u}{\mathrm {d} t}}\right)={\frac {\mathrm {d} }{\mathrm {d} t}}\operatorname {H} (u)$

Iterating this identity,

$\operatorname {H} \left({\frac {\mathrm {d} ^{k}u}{\mathrm {d} t^{k}}}\right)={\frac {\mathrm {d} ^{k}}{\mathrm {d} t^{k}}}\operatorname {H} (u)$

This is rigorously true as stated provided u and its first k derivatives belong to $L^{p}(\mathbb {R} )$ . One can check this easily in the frequency domain, where differentiation becomes multiplication by ω.

### Convolutions

The Hilbert transform can formally be realized as a convolution with the tempered distribution

$h(t)=\operatorname {p.v.} {\frac {1}{\pi \,t}}$

Thus formally,

$\operatorname {H} (u)=h*u$

However, *a priori* this may only be defined for u a distribution of compact support. It is possible to work somewhat rigorously with this since compactly supported functions (which are distributions *a fortiori*) are dense in *Lp*. Alternatively, one may use the fact that *h*(*t*) is the distributional derivative of the function log|*t*|/*π*; to wit

$\operatorname {H} (u)(t)={\frac {\mathrm {d} }{\mathrm {d} t}}\left({\frac {1}{\pi }}\left(u*\log {\bigl |}\cdot {\bigr |}\right)(t)\right)$

For most operational purposes the Hilbert transform can be treated as a convolution. For example, in a formal sense, the Hilbert transform of a convolution is the convolution of the Hilbert transform applied on *only one* of either of the factors:

$\operatorname {H} (u*v)=\operatorname {H} (u)*v=u*\operatorname {H} (v)$

This is rigorously true if u and v are compactly supported distributions since, in that case,

$h*(u*v)=(h*u)*v=u*(h*v)$

By passing to an appropriate limit, it is thus also true if *u* ∈ *Lp* and *v* ∈ *Lq* provided that

$1<{\frac {1}{p}}+{\frac {1}{q}}$

from a theorem due to Titchmarsh.

### Invariance

The Hilbert transform has the following invariance properties on $L^{2}(\mathbb {R} )$ .

- It commutes with translations. That is, it commutes with the operators *T**a* *f*(*x*) = *f*(*x* + *a*) for all a in $\mathbb {R} .$
- It commutes with positive dilations. That is it commutes with the operators *Mλ f* (*x*) = *f* (*λ x*) for all *λ* > 0.
- It anticommutes with the reflection *R f* (*x*) = *f* (−*x*).

Up to a multiplicative constant, the Hilbert transform is the only bounded operator on L2 with these properties.

In fact there is a wider set of operators that commute with the Hilbert transform. The group ${\text{SL}}(2,\mathbb {R} )$ acts by unitary operators U*g* on the space $L^{2}(\mathbb {R} )$ by the formula

$\operatorname {U} _{g}^{-1}f(x)={\frac {1}{cx+d}}\,f\left({\frac {ax+b}{cx+d}}\right)\,,\qquad g={\begin{bmatrix}a&b\\c&d\end{bmatrix}}~,\qquad {\text{ for }}~ad-bc=\pm 1.$

This unitary representation is an example of a principal series representation of $~{\text{SL}}(2,\mathbb {R} )~.$ In this case it is reducible, splitting as the orthogonal sum of two invariant subspaces, Hardy space $H^{2}(\mathbb {R} )$ and its conjugate. These are the spaces of *L*2 boundary values of holomorphic functions on the upper and lower halfplanes. $H^{2}(\mathbb {R} )$ and its conjugate consist of exactly those *L*2 functions with Fourier transforms vanishing on the negative and positive parts of the real axis respectively. Since the Hilbert transform is equal to H = −*i* (2*P* − I), with P being the orthogonal projection from $L^{2}(\mathbb {R} )$ onto $\operatorname {H} ^{2}(\mathbb {R} ),$ and I the identity operator, it follows that $\operatorname {H} ^{2}(\mathbb {R} )$ and its orthogonal complement are eigenspaces of H for the eigenvalues ±*i*. In other words, H commutes with the operators Ug. The restrictions of the operators Ug to $\operatorname {H} ^{2}(\mathbb {R} )$ and its conjugate give irreducible representations of ${\text{SL}}(2,\mathbb {R} )$ – the so-called limit of discrete series representations.

## Extending the domain of definition

### Hilbert transform of distributions

It is further possible to extend the Hilbert transform to certain spaces of distributions (Pandey 1996, Chapter 3). Since the Hilbert transform commutes with differentiation, and is a bounded operator on Lp, H restricts to give a continuous transform on the inverse limit of Sobolev spaces:

${\mathcal {D}}_{L^{p}}={\underset {n\to \infty }{\underset {\longleftarrow }{\lim }}}W^{n,p}(\mathbb {R} )$

The Hilbert transform can then be defined on the dual space of ${\mathcal {D}}_{L^{p}}$ , denoted ${\mathcal {D}}_{L^{p}}'$ , consisting of Lp distributions. This is accomplished by the duality pairing: For $u\in {\mathcal {D}}'_{L^{p}}$ , define:

$\operatorname {H} (u)\in {\mathcal {D}}'_{L^{p}}=\langle \operatorname {H} u,v\rangle \ \triangleq \ \langle u,-\operatorname {H} v\rangle ,\ {\text{for all}}\ v\in {\mathcal {D}}_{L^{p}}.$

It is possible to define the Hilbert transform on the space of tempered distributions as well by an approach due to Gel'fand and Shilov, but considerably more care is needed because of the singularity in the integral.

### Hilbert transform of bounded functions

The Hilbert transform can be defined for functions in $L^{\infty }(\mathbb {R} )$ as well, but it requires some modifications and caveats. Properly understood, the Hilbert transform maps $L^{\infty }(\mathbb {R} )$ to the Banach space of bounded mean oscillation (BMO) classes.

Interpreted naïvely, the Hilbert transform of a bounded function is clearly ill-defined. For instance, with *u* = sgn(*x*), the integral defining H(*u*) diverges almost everywhere to ±∞. To alleviate such difficulties, the Hilbert transform of an *L*∞ function is therefore defined by the following regularized form of the integral

$\operatorname {H} (u)(t)=\operatorname {p.v.} \int _{-\infty }^{\infty }u(\tau )\left\{h(t-\tau )-h_{0}(-\tau )\right\}\,\mathrm {d} \tau$

where as above *h*(*x*) = ⁠1/*πx*⁠ and

$h_{0}(x)={\begin{cases}0&{\text{if}}~|x|<1\\{\frac {1}{\pi \,x}}&{\text{if}}~|x|\geq 1\end{cases}}$

The modified transform H agrees with the original transform up to an additive constant on functions of compact support from a general result by Calderón and Zygmund. Furthermore, the resulting integral converges pointwise almost everywhere, and with respect to the BMO norm, to a function of bounded mean oscillation.

A deep result of Fefferman's work is that a function is of bounded mean oscillation if and only if it has the form *f* + H(*g*) for some $f,g\in L^{\infty }(\mathbb {R} )$ .

## Conjugate functions

The Hilbert transform can be understood in terms of a pair of functions *f*(*x*) and *g*(*x*) such that the function $F(x)=f(x)+i\,g(x)$ is the boundary value of a holomorphic function *F*(*z*) in the upper half-plane. Under these circumstances, if f and g are sufficiently integrable, then one is the Hilbert transform of the other.

Suppose that $f\in L^{p}(\mathbb {R} ).$ Then, by the theory of the Poisson integral, f admits a unique harmonic extension into the upper half-plane, and this extension is given by

$u(x+iy)=u(x,y)={\frac {1}{\pi }}\int _{-\infty }^{\infty }f(s)\;{\frac {y}{(x-s)^{2}+y^{2}}}\;\mathrm {d} s$

which is the convolution of f with the Poisson kernel

$P(x,y)={\frac {y}{\pi \,\left(x^{2}+y^{2}\right)}}$

Furthermore, there is a unique harmonic function v defined in the upper half-plane such that *F*(*z*) = *u*(*z*) + *i v*(*z*) is holomorphic and $\lim _{y\to \infty }v\,(x+i\,y)=0$

This harmonic function is obtained from f by taking a convolution with the *conjugate Poisson kernel*

$Q(x,y)={\frac {x}{\pi \,\left(x^{2}+y^{2}\right)}}.$

Thus $v(x,y)={\frac {1}{\pi }}\int _{-\infty }^{\infty }f(s)\;{\frac {x-s}{\,(x-s)^{2}+y^{2}\,}}\;\mathrm {d} s.$

Indeed, the real and imaginary parts of the Cauchy kernel are ${\frac {i}{\pi \,z}}=P(x,y)+i\,Q(x,y)$

so that *F* = *u* + *i v* is holomorphic by Cauchy's integral formula.

The function v obtained from u in this way is called the harmonic conjugate of u. The (non-tangential) boundary limit of *v*(*x*,*y*) as *y* → 0 is the Hilbert transform of f. Thus, succinctly, $\operatorname {H} (f)=\lim _{y\to 0}Q(-,y)\star f$

### Titchmarsh's theorem

Titchmarsh's theorem (named for E. C. Titchmarsh who included it in his 1937 work) makes precise the relationship between the boundary values of holomorphic functions in the upper half-plane and the Hilbert transform. It gives necessary and sufficient conditions for a complex-valued square-integrable function *F*(*x*) on the real line to be the boundary value of a function in the Hardy space H2(*U*) of holomorphic functions in the upper half-plane U.

The theorem states that the following conditions for a complex-valued square-integrable function $F:\mathbb {R} \to \mathbb {C}$ are equivalent:

- *F*(*x*) is the limit as *z* → *x* of a holomorphic function *F*(*z*) in the upper half-plane such that $\int _{-\infty }^{\infty }|F(x+i\,y)|^{2}\;\mathrm {d} x<K$
- The real and imaginary parts of *F*(*x*) are Hilbert transforms of each other.
- The Fourier transform ${\mathcal {F}}(F)(x)$ vanishes for *x* < 0.

A weaker result is true for functions of class Lp for *p* > 1. Specifically, if *F*(*z*) is a holomorphic function such that

$\int _{-\infty }^{\infty }|F(x+i\,y)|^{p}\;\mathrm {d} x<K$

for all y, then there is a complex-valued function *F*(*x*) in $L^{p}(\mathbb {R} )$ such that *F*(*x* + *i y*) → *F*(*x*) in the Lp norm as *y* → 0 (as well as holding pointwise almost everywhere). Furthermore,

$F(x)=f(x)+i\,g(x)$

where f is a real-valued function in $L^{p}(\mathbb {R} )$ and g is the Hilbert transform (of class Lp) of f.

This is not true in the case *p* = 1. In fact, the Hilbert transform of an *L*1 function f need not converge in the mean to another *L*1 function. Nevertheless, the Hilbert transform of f does converge almost everywhere to a finite function g such that

$\int _{-\infty }^{\infty }{\frac {|g(x)|^{p}}{1+x^{2}}}\;\mathrm {d} x<\infty$

This result is directly analogous to one by Andrey Kolmogorov for Hardy functions in the disc. Although usually called Titchmarsh's theorem, the result aggregates much work of others, including Hardy, Paley and Wiener (see Paley–Wiener theorem), as well as work by Riesz, Hille, and Tamarkin

### Riemann–Hilbert problem

One form of the Riemann–Hilbert problem seeks to identify pairs of functions *F*+ and *F*− such that *F*+ is holomorphic on the upper half-plane and *F*− is holomorphic on the lower half-plane, such that for x along the real axis, $F_{+}(x)-F_{-}(x)=f(x)$

where *f*(*x*) is some given real-valued function of $x\in \mathbb {R}$ . The left-hand side of this equation may be understood either as the difference of the limits of *F*± from the appropriate half-planes, or as a hyperfunction distribution. Two functions of this form are a solution of the Riemann–Hilbert problem.

Formally, if *F*± solve the Riemann–Hilbert problem $f(x)=F_{+}(x)-F_{-}(x)$

then the Hilbert transform of *f*(*x*) is given by $H(f)(x)=-i{\bigl (}F_{+}(x)+F_{-}(x){\bigr )}.$

## Hilbert transform on the circle

For a periodic function f the circular Hilbert transform is defined:

${\tilde {f}}(x)\triangleq {\frac {1}{2\pi }}\operatorname {p.v.} \int _{0}^{2\pi }f(t)\,\cot \left({\frac {x-t}{2}}\right)\,\mathrm {d} t$

The circular Hilbert transform is used in giving a characterization of Hardy space and in the study of the conjugate function in Fourier series. The kernel, $\cot \left({\frac {x-t}{2}}\right)$ is known as the **Hilbert kernel** since it was in this form the Hilbert transform was originally studied.

The Hilbert kernel (for the circular Hilbert transform) can be obtained by making the Cauchy kernel 1⁄x periodic. More precisely, for *x* ≠ 0

${\frac {1}{\,2\,}}\cot \left({\frac {x}{2}}\right)={\frac {1}{x}}+\sum _{n=1}^{\infty }\left({\frac {1}{x+2n\pi }}+{\frac {1}{\,x-2n\pi \,}}\right)$

Many results about the circular Hilbert transform may be derived from the corresponding results for the Hilbert transform from this correspondence.

Another more direct connection is provided by the Cayley transform *C*(*x*) = (*x* – *i*) / (*x* + *i*), which carries the real line onto the circle and the upper half plane onto the unit disk. It induces a unitary map

$U\,f(x)={\frac {1}{(x+i)\,{\sqrt {\pi }}}}\,f\left(C\left(x\right)\right)$

of *L*2(**T**) onto $L^{2}(\mathbb {R} ).$ The operator U carries the Hardy space *H*2(**T**) onto the Hardy space $H^{2}(\mathbb {R} )$ .

## Hilbert transform in signal processing

### Bedrosian's theorem

**Bedrosian's theorem** states that the Hilbert transform of the product of a low-pass and a high-pass signal with non-overlapping spectra is given by the product of the low-pass signal and the Hilbert transform of the high-pass signal, or

$\operatorname {H} \left(f_{\text{LP}}(t)\cdot f_{\text{HP}}(t)\right)=f_{\text{LP}}(t)\cdot \operatorname {H} \left(f_{\text{HP}}(t)\right),$

where *f*LP and *f*HP are the low- and high-pass signals respectively. A category of communication signals to which this applies is called the *narrowband signal model.* A member of that category is amplitude modulation of a high-frequency sinusoidal "carrier":

$u(t)=u_{m}(t)\cdot \cos(\omega t+\varphi ),$

where *u**m*(*t*) is the narrow bandwidth "message" waveform, such as voice or music. Then by Bedrosian's theorem:

$\operatorname {H} (u)(t)={\begin{cases}+u_{m}(t)\cdot \sin(\omega t+\varphi )&{\text{if }}\omega >0\\-u_{m}(t)\cdot \sin(\omega t+\varphi )&{\text{if }}\omega <0\end{cases}}$

### Analytic representation

A specific type of conjugate function is**:**

$u_{a}(t)\triangleq u(t)+i\cdot H(u)(t),$

known as the *analytic representation* of $u(t).$ The name reflects its mathematical tractability, due largely to Euler's formula. Applying Bedrosian's theorem to the narrowband model, the analytic representation is**:**

| ${\begin{aligned}u_{a}(t)&=u_{m}(t)\cdot \cos(\omega t+\varphi )+i\cdot u_{m}(t)\cdot \sin(\omega t+\varphi ),\quad \omega >0\\&=u_{m}(t)\cdot \left[\cos(\omega t+\varphi )+i\cdot \sin(\omega t+\varphi )\right],\quad \omega >0\\&=u_{m}(t)\cdot e^{i(\omega t+\varphi )},\quad \omega >0.\,\end{aligned}}$ |   | Eq.1 |
|---|---|---|

A Fourier transform property indicates that this complex heterodyne operation can shift all the negative frequency components of *u**m*(*t*) above 0 Hz. In that case, the imaginary part of the result is a Hilbert transform of the real part. This is an indirect way to produce Hilbert transforms.

### Angle (phase/frequency) modulation

The form:

$u(t)=A\cdot \cos(\omega t+\varphi _{m}(t))$

is called angle modulation, which includes both phase modulation and frequency modulation. The instantaneous frequency is   $\omega +\varphi _{m}^{\prime }(t).$   For sufficiently large ω, compared to $\varphi _{m}^{\prime }$ :

$\operatorname {H} (u)(t)\approx A\cdot \sin(\omega t+\varphi _{m}(t))$ and: $u_{a}(t)\approx A\cdot e^{i(\omega t+\varphi _{m}(t))}.$

### Single sideband modulation (SSB)

When *u**m*(*t*) in **Eq.1** is also an analytic representation (of a message waveform), that is:

$u_{m}(t)=m(t)+i\cdot {\widehat {m}}(t)$

the result is single-sideband modulation:

$u_{a}(t)=(m(t)+i\cdot {\widehat {m}}(t))\cdot e^{i(\omega t+\varphi )}$

whose transmitted component is:

${\begin{aligned}u(t)&=\operatorname {Re} \{u_{a}(t)\}\\&=m(t)\cdot \cos(\omega t+\varphi )-{\widehat {m}}(t)\cdot \sin(\omega t+\varphi )\end{aligned}}$

### Causality

The function $h(t)=1/(\pi t)$ presents two causality-based challenges to practical implementation in a convolution (in addition to its undefined value at 0):

- Its duration is infinite (technically *infinite support*). Finite-length *windowing* reduces the effective frequency range of the transform; shorter windows result in greater losses at low and high frequencies. See also quadrature filter.
- It is a non-causal filter. So a delayed version, $h(t-\tau ),$ is required. The corresponding output is subsequently delayed by $\tau .$ When creating the imaginary part of an analytic signal, the source (real part) must also be delayed by $\tau$ .

## Discrete Hilbert transform

For a discrete function, $u[n],$ with discrete-time Fourier transform (DTFT), $U(\omega )$ , and **discrete Hilbert transform** ${\widehat {u}}[n],$ the DTFT of ${\widehat {u}}[n]$ in the region −*π* < ω < *π* is given by**:**

$\operatorname {DTFT} ({\widehat {u}})=U(\omega )\cdot (-i\cdot \operatorname {sgn}(\omega )).$

The inverse DTFT, using the convolution theorem, is**:**

${\begin{aligned}{\widehat {u}}[n]&={\scriptstyle \mathrm {DTFT} ^{-1}}(U(\omega ))\ *\ {\scriptstyle \mathrm {DTFT} ^{-1}}(-i\cdot \operatorname {sgn}(\omega ))\\&=u[n]\ *\ {\frac {1}{2\pi }}\int _{-\pi }^{\pi }(-i\cdot \operatorname {sgn}(\omega ))\cdot e^{i\omega n}\,\mathrm {d} \omega \\&=u[n]\ *\ \underbrace {{\frac {1}{2\pi }}\left[\int _{-\pi }^{0}i\cdot e^{i\omega n}\,\mathrm {d} \omega -\int _{0}^{\pi }i\cdot e^{i\omega n}\,\mathrm {d} \omega \right]} _{h[n]},\end{aligned}}$

where

$h[n]\ \triangleq \ {\begin{cases}0,&{\text{if }}n{\text{ even}}\\{\frac {2}{\pi n}}&{\text{if }}n{\text{ odd}}\end{cases}}$

which is an infinite impulse response (IIR).

**Practical considerations**

**Method 1:** Direct convolution of streaming $u[n]$ data with an FIR approximation of $h[n],$ which we will designate by ${\tilde {h}}[n].$ Examples of truncated $h[n]$ are shown in figures 1 and 2. **Fig 1** has an odd number of anti-symmetric coefficients and is called Type III. This type inherently exhibits responses of zero magnitude at frequencies 0 and Nyquist, resulting in a bandpass filter shape. A Type IV design (even number of anti-symmetric coefficients) is shown in **Fig 2**. It has a highpass frequency response. Type III is the usual choice. for these reasons**:**

- A typical (i.e. properly filtered and sampled) $u[n]$ sequence has no useful components at the Nyquist frequency.
- The Type IV impulse response requires a ${\tfrac {1}{2}}$ sample shift in the $h[n]$ sequence. That causes the zero-valued coefficients to become non-zero, as seen in *Figure 2*. So a Type III design is potentially twice as efficient as Type IV.
- The group delay of a Type III design is an integer number of samples, which facilitates aligning ${\widehat {u}}[n]$ with $u[n]$ to create an analytic signal. The group delay of Type IV is halfway between two samples.

The abrupt truncation of $h[n]$ creates a rippling (Gibbs effect) of the flat frequency response. That can be mitigated by use of a window function to taper ${\tilde {h}}[n]$ to zero.

**Method 2:** Piecewise convolution. It is well known that direct convolution is computationally much more intensive than methods like **overlap-save** that give access to the efficiencies of the Fast Fourier transform via the convolution theorem. Specifically, the discrete Fourier transform (DFT) of a segment of $u[n]$ is multiplied pointwise with a DFT of the ${\tilde {h}}[n]$ sequence. An inverse DFT is done on the product, and the transient artifacts at the leading and trailing edges of the segment are discarded. Over-lapping input segments prevent gaps in the output stream. An equivalent time domain description is that segments of length N (an arbitrary parameter) are convolved with the periodic function**:**

${\tilde {h}}_{N}[n]\ \triangleq \sum _{m=-\infty }^{\infty }{\tilde {h}}[n-mN].$

When the duration of non-zero values of ${\tilde {h}}[n]$ is $M<N,$ the output sequence includes $N-M+1$ samples of ${\widehat {u}}.$   $M-1$ outputs are discarded from each block of $N,$ and the input blocks are overlapped by that amount to prevent gaps.

**Method 3:** Same as method 2, except the DFT of ${\tilde {h}}[n]$ is replaced by samples of the $-i\operatorname {sgn} (\omega )$ distribution (whose real and imaginary components are all just 0 or  $\pm 1.$ ) That convolves $u[n]$ with a periodic summation**:**

$h_{N}[n]\ \triangleq \sum _{m=-\infty }^{\infty }h[n-mN],$

for some arbitrary parameter, $N.$ $h[n]$ is not an FIR, so the edge effects extend throughout the entire transform. Deciding what to delete and the corresponding amount of overlap is an application-dependent design issue.

**Fig 3** depicts the difference between methods 2 and 3. Only half of the antisymmetric impulse response is shown, and only the non-zero coefficients. The blue graph corresponds to method 2 where $h[n]$ is truncated by a rectangular window function, rather than tapered. It is generated by a Matlab function, **hilb(65)**. Its transient effects are exactly known and readily discarded. The frequency response, which is determined by the function argument, is the only application-dependent design issue.

The red graph is $h_{512}[n],$ corresponding to method 3. It is the inverse DFT of the $-i\operatorname {sgn} (\omega )$ distribution. Specifically, it is the function that is convolved with a segment of $u[n]$ by the MATLAB function, **hilbert(u,512)**. The real part of the output sequence is the original input sequence, so that the complex output is an analytic representation of $u[n].$

When the input is a segment of a pure cosine, the resulting convolution for two different values of N is depicted in **Fig 4** (red and blue plots). Edge effects prevent the result from being a pure sine function (green plot). Since $h_{N}[n]$ is not an FIR sequence, the theoretical extent of the effects is the entire output sequence. But the differences from a sine function diminish with distance from the edges. Parameter N is the output sequence length. If it exceeds the length of the input sequence, the input is modified by appending zero-valued elements. In most cases, that reduces the magnitude of the edge distortions. But their duration is dominated by the inherent rise and fall times of the $h[n]$ impulse response.

**Fig 5** is an example of piecewise convolution, using both methods 2 (in blue) and 3 (red dots). A sine function is created by computing the Discrete Hilbert transform of a cosine function, which was processed in four overlapping segments, and pieced back together. As the FIR result (blue) shows, the distortions apparent in the IIR result (red) are not caused by the difference between $h[n]$ and $h_{N}[n]$ (green and red in **Fig 3**). The fact that $h_{N}[n]$ is tapered (*windowed*) is actually helpful in this context. The real problem is that it's not windowed enough. Effectively, $M=N,$ whereas the overlap-save method needs $M<N.$

## Number-theoretic Hilbert transform

The number theoretic Hilbert transform is an extension of the discrete Hilbert transform to integers modulo an appropriate prime number. In this it follows the generalization of discrete Fourier transform to number theoretic transforms. The number theoretic Hilbert transform can be used to generate sets of orthogonal discrete sequences.
