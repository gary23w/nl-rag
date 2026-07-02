---
title: "Z-transform"
source: https://en.wikipedia.org/wiki/Z-transform
domain: z-transform
license: CC-BY-SA-4.0
tags: z-transform, bilinear transform, region of convergence, digital filter
fetched: 2026-07-02
---

# Z-transform

In mathematics and signal processing, the **Z-transform** converts a discrete-time signal, which is a sequence of real or complex numbers, into a complex valued frequency-domain (the **z-domain** or **z-plane**) representation.

It can be considered a discrete-time counterpart of the Laplace transform (the *s-domain* or *s-plane*). This similarity is explored in the theory of time-scale calculus.

While the continuous-time Fourier transform is evaluated on the s-domain's vertical axis (the imaginary axis), the discrete-time Fourier transform is evaluated along the z-domain's unit circle. The s-domain's left half-plane maps to the area inside the z-domain's unit circle, while the s-domain's right half-plane maps to the area outside of the z-domain's unit circle.

In signal processing, one of the means of designing digital filters is to take analog designs, subject them to a bilinear transform which maps them from the s-domain to the z-domain, and then produce the digital filter by inspection, manipulation, or numerical approximation. Such methods tend not to be accurate except in the vicinity of the complex unity, i.e. at low frequencies.

## History

The basic idea now known as the Z-transform was known to Laplace, and it was re-introduced in 1947 by W. Hurewicz and others as a way to treat sampled-data control systems used with radar. It gives a tractable way to solve linear, constant-coefficient difference equations. It was later dubbed "the z-transform" by Ragazzini and Zadeh in the sampled-data control group at Columbia University in 1952.

The modified or advanced Z-transform was later developed and popularized by E. I. Jury.

The idea contained within the Z-transform is also known in mathematical literature as the method of generating functions which can be traced back as early as 1730 when it was introduced by de Moivre in conjunction with probability theory. From a mathematical view the Z-transform can also be viewed as a Laurent series where one views the sequence of numbers under consideration as the (Laurent) expansion of an analytic function.

## Definition

The Z-transform can be defined as either a *one-sided* or *two-sided* transform (similarly to the one-sided Laplace transform and the two-sided Laplace transform).

### Bilateral Z-transform

The *bilateral* or *two-sided* Z-transform of a discrete-time signal $x[n]$ is the formal power series $X(z)$ defined as:

$X(z)={\mathcal {Z}}\{x[n]\}=\sum _{n=-\infty }^{\infty }x[n]z^{-n}$

where n is an integer and z is, in general, a complex number. In polar form, z may be written as:

$z=Ae^{i\phi }=A\cdot (\cos {\phi }+i\sin {\phi })$

where A is the magnitude of ⁠ z ⁠, i is the imaginary unit, and $\phi$ is the *complex argument* (also referred to as *angle* or *phase*) in radians.

### Unilateral Z-transform

Alternatively, in cases where $x[n]$ is defined only for ⁠ $n\geq 0$ ⁠, the *single-sided* or *unilateral* Z-transform is defined as:

$X(z)={\mathcal {Z}}\{x[n]\}=\sum _{n=0}^{\infty }x[n]z^{-n}.$

In signal processing, this definition can be used to evaluate the Z-transform of the unit impulse response of a discrete-time causal system.

An important example of the unilateral Z-transform is the probability-generating function, where the component $x[n]$ is the probability that a discrete random variable takes the value ⁠ n ⁠. The properties of Z-transforms (listed in *§ Properties*) have useful interpretations in the context of probability theory.

## Inverse Z-transform

The *inverse* Z-transform is:

$x[n]={\mathcal {Z}}^{-1}\{X(z)\}={\frac {1}{2\pi i}}\oint _{C}X(z)z^{n-1}dz$

where C is a counterclockwise closed path encircling the origin and entirely in the region of convergence (ROC). In the case where the ROC is causal (see Example 2), this means the path C must encircle all of the poles of ⁠ $X(z)$ ⁠.

A special case of this contour integral occurs when C is the unit circle. This contour can be used when the ROC includes the unit circle, which is always guaranteed when $X(z)$ is stable, that is, when all the poles are inside the unit circle. With this contour, the inverse Z-transform simplifies to the inverse discrete-time Fourier transform, or Fourier series, of the periodic values of the Z-transform around the unit circle:

$x[n]={\frac {1}{2\pi }}\int _{-\pi }^{\pi }X(e^{i\omega })e^{i\omega n}d\omega .$

The Z-transform with a finite range of n and a finite number of uniformly spaced z values can be computed efficiently via Bluestein's FFT algorithm. The discrete-time Fourier transform (DTFT)—not to be confused with the discrete Fourier transform (DFT)—is a special case of such a Z-transform obtained by restricting z to lie on the unit circle.

The following three methods are often used for the evaluation of the inverse -transform,

### Direct evaluation by contour integration

This method involves applying the Cauchy Residue Theorem to evaluate the inverse Z-transform. By integrating around a closed contour in the complex plane, the residues at the poles of the Z-transform function inside the ROC are summed. This technique is particularly useful when working with functions expressed in terms of complex variables.

### Expansion into a series of terms in the variables *z* and *z*−1

In this method, the Z-transform is expanded into a power series. This approach is useful when the Z-transform function is rational, allowing for the approximation of the inverse by expanding into a series and determining the signal coefficients term by term.

### Partial-fraction expansion and table lookup

This technique decomposes the Z-transform into a sum of simpler fractions, each corresponding to known Z-transform pairs. The inverse Z-transform is then determined by looking up each term in a standard table of Z-transform pairs. This method is widely used for its efficiency and simplicity, especially when the original function can be easily broken down into recognizable components.

#### Example

A) Determine the inverse Z-transform of the following by series expansion method, $X(z)={\frac {1}{1-1.5\,z^{-1}+0.5\,z^{-2}}}$

Solution:

Case 1:

ROC: $\left\vert z\right\vert >1$

Since the ROC is the exterior of a circle, $x(n)$ is causal (signal existing for ⁠ $n\geq 0$ ⁠). $X(z)={1 \over 1-{3 \over 2}z^{-1}+{1 \over 2}z^{-2}}=1+{{3 \over 2}z^{-1}}+{{7 \over 4}z^{-2}}+{{15 \over 8}z^{-3}}+{{31 \over 16}z^{-4}}+\ldots .$ Thus, ${\begin{aligned}x(n)&=\left\{1,{\frac {3}{2}},{\frac {7}{4}},{\frac {15}{8}},{\frac {31}{16}}\ldots \right\}\\&\qquad \!\uparrow \\\end{aligned}}$ (arrow indicates term at ⁠ $x(0)=1$ ⁠).

Note that in each step of long division process we eliminate lowest power term of ⁠ $z^{-1}$ ⁠.

Case 2:

ROC: $\left\vert z\right\vert <0.5$

Since the ROC is the interior of a circle, $x(n)$ is anticausal (signal existing for ⁠ $n<0$ ⁠).

By performing long division we get $X(z)={\frac {1}{1-{\frac {3}{2}}z^{-1}+{\frac {1}{2}}z^{-2}}}=2z^{2}+6z^{3}+14z^{4}+30z^{5}+\ldots$

${\begin{aligned}x(n)&=\{30,14,6,2,0,0\}\\&\qquad \qquad \qquad \quad \ \ \,\uparrow \\\end{aligned}}$

(arrow indicates term at

⁠

$x(0)=0$

⁠

).

Note that in each step of long division process we eliminate lowest power term of ⁠ z ⁠.

*Note:*

1. When the signal is causal, we get positive powers of z and when the signal is anticausal, we get negative powers of ⁠ z ⁠.
2. $z^{k}$ indicates term at $x(-k)$ and $z^{-k}$ indicates term at ⁠ $x(k)$ ⁠.

B) Determine the inverse Z-transform of the following by series expansion method,

Eliminating negative powers if z and dividing by ⁠ z ⁠, ${\frac {X(z)}{z}}={\frac {z^{2}}{z(z^{2}-1.5\,z+0.5)}}={\frac {z}{z^{2}-1.5\,z+0.5}}$

By partial fraction expansion, ${\begin{aligned}{\frac {X(z)}{z}}&={\frac {z}{(z-1)(z-0.5)}}={\frac {A_{1}}{z-0.5}}+{\frac {A_{2}}{z-1}}\\[4pt]&A_{1}=\left.{\frac {(z-0.5)X(z)}{z}}\right\vert _{z=0.5}={\frac {0.5}{(0.5-1)}}=-1\\[4pt]&A_{2}=\left.{\frac {(z-1)X(z)}{z}}\right\vert _{z=1}={\frac {1}{1-0.5}}={2}\\[4pt]{\frac {X(z)}{z}}&={\frac {2}{z-1}}-{\frac {1}{z-0.5}}\end{aligned}}$

Case 1:

ROC: $\left\vert z\right\vert >1$

Both the terms are causal, hence $x(n)$ is causal.

${\begin{aligned}x(n)&=2{(1)^{n}}u(n)-1{(0.5)^{n}}u(n)\\&=(2-(0.5)^{n})u(n)\\\end{aligned}}$

Case 2:

ROC: $\left\vert z\right\vert <0.5$

Both the terms are anticausal, hence $x(n)$ is anticausal.

${\begin{aligned}x(n)&=-2{(1)^{n}}u(-n-1)-(-1{(0.5)^{n}}u(-n-1))\\&=((0.5)^{n}-2)u(-n-1)\\\end{aligned}}$

Case 3:

ROC: $0.5<\left\vert z\right\vert <1$

One of the terms is causal (⁠ $p=0.5$ ⁠ provides the causal part) and other is anticausal (⁠ $p=1$ ⁠ provides the anticausal part), hence $x(n)$ is both sided.

${\begin{aligned}x(n)&=-2{(1)^{n}}u(-n-1)-1{(0.5)^{n}}u(n)\\&=-2u(-n-1)-(0.5)^{n}u(n)\\\end{aligned}}$

## Region of convergence

The region of convergence (ROC) is the set of points in the complex plane for which the Z-transform summation absolutely converges:

$\mathrm {ROC} =\left\{z:\sum _{n=-\infty }^{\infty }\left|x[n]z^{-n}\right|<\infty \right\}$

### Example 1 (no ROC)

Let ⁠ $x[n]=(0.5)^{n}$ ⁠. Expanding $x[n]$ on the interval $(-\infty ,\infty )$ it becomes

$x[n]=\left\{\dots ,(0.5)^{-3},(0.5)^{-2},(0.5)^{-1},1,0.5,(0.5)^{2},(0.5)^{3},\dots \right\}=\left\{\dots ,2^{3},2^{2},2,1,0.5,(0.5)^{2},(0.5)^{3},\dots \right\}.$

Looking at the sum

$\sum _{n=-\infty }^{\infty }x[n]z^{-n}\to \infty .$

Therefore, there are no values of z that satisfy this condition.

### Example 2 (causal ROC)

Let $x[n]=(0.5)^{n}\,u[n]$ (where u is the Heaviside step function). Expanding $x[n]$ on the interval $(-\infty ,\infty )$ it becomes

$x[n]=\left\{\dots ,0,0,0,1,0.5,(0.5)^{2},(0.5)^{3},\dots \right\}.$

Looking at the sum

$\sum _{n=-\infty }^{\infty }x[n]z^{-n}=\sum _{n=0}^{\infty }(0.5)^{n}z^{-n}=\sum _{n=0}^{\infty }\left({\frac {0.5}{z}}\right)^{n}={\frac {1}{1-0.5\,z^{-1}}}.$

The last equality arises from the infinite geometric series and the equality only holds if ⁠ $\vert 0.5\,z^{-1}\vert <1$ ⁠, which can be rewritten in terms of z as ⁠ $\vert z\vert >0.5$ ⁠. Thus, the ROC is ⁠ $\vert z\vert >0.5$ ⁠. In this case the ROC is the complex plane with a disc of radius ⁠ $0.5$ ⁠ at the origin "punched out".

### Example 3 (anticausal ROC)

Let $x[n]=-(0.5)^{n}\,u[-n-1]$ (where u is the Heaviside step function). Expanding $x[n]$ on the interval $(-\infty ,\infty )$ it becomes

$x[n]=\left\{\dots ,-(0.5)^{-3},-(0.5)^{-2},-(0.5)^{-1},0,0,0,0,\dots \right\}.$

Looking at the sum

${\begin{aligned}\sum _{n=-\infty }^{\infty }x[n]\,z^{-n}&=-\sum _{n=-\infty }^{-1}(0.5)^{n}\,z^{-n}\\&=-\sum _{m=1}^{\infty }\left({\frac {z}{0.5}}\right)^{m}\\&=-{\frac {(0.5)^{-1}z}{1-(0.5)^{-1}z}}\\&=-{\frac {1}{0.5\,z^{-1}-1}}\\&={\frac {1}{1-0.5\,z^{-1}}}\\\end{aligned}}$

and using the infinite geometric series again, the equality only holds if $|(0.5)^{-1}z|<1$ which can be rewritten in terms of z as ⁠ $\vert z\vert <0.5$ ⁠. Thus, the ROC is ⁠ $\vert z\vert <0.5$ ⁠. In this case the ROC is a disc centered at the origin and of radius ⁠ $0.5$ ⁠.

What differentiates this example from the previous example is *only* the ROC. This is intentional to demonstrate that the transform result alone is insufficient.

### Examples conclusion

Examples 2 and 3 clearly show that the Z-transform $X(z)$ of $x[n]$ is unique when and only when specifying the ROC. Creating the pole–zero plot for the causal and anticausal case show that the ROC for either case does not include the pole that is at ⁠ $0.5$ ⁠. This extends to cases with multiple poles: the ROC will *never* contain poles.

In example 2, the causal system yields a ROC that includes $|z|=\infty$ while the anticausal system in example 3 yields an ROC that includes ⁠ $\vert z\vert =0$ ⁠.

In systems with multiple poles it is possible to have a ROC that includes neither $|z|=\infty$ nor ⁠ $\vert z\vert =0$ ⁠. The ROC creates a circular band. For example,

$x[n]=(0.5)^{n}\,u[n]-(0.75)^{n}\,u[-n-1]$

has poles at ⁠ $0.5$ ⁠ and ⁠ $0.75$ ⁠. The ROC will be ⁠ $0.5<\vert z\vert <0.75$ ⁠, which includes neither the origin nor infinity. Such a system is called a mixed-causality system as it contains a causal term $(0.5)^{n}\,u[n]$ and an anticausal term ⁠ $-(0.75)^{n}\,u[-n-1]$ ⁠.

The stability of a system can also be determined by knowing the ROC alone. If the ROC contains the unit circle (i.e., ⁠ $\vert z\vert =1$ ⁠) then the system is stable. In the above systems the causal system (Example 2) is stable because ⁠ $\vert z\vert >0.5$ ⁠ contains the unit circle.

Let us assume we are provided a Z-transform of a system without a ROC (i.e., an ambiguous ⁠ $x[n]$ ⁠). We can determine a unique $x[n]$ provided we desire the following:

- Stability
- Causality

For stability the ROC must contain the unit circle. If we need a causal system then the ROC must contain infinity and the system function will be a right-sided sequence. If we need an anticausal system then the ROC must contain the origin and the system function will be a left-sided sequence. If we need both stability and causality, all the poles of the system function must be inside the unit circle.

The unique $x[n]$ can then be found.

## Properties

| Property | Time domain | Z-domain | Proof | ROC |
|---|---|---|---|---|
| Definition of Z-transform | $x[n]$ | $X(z)$ | $X(z)={\mathcal {Z}}\{x[n]\}$ (definition of the z-transform) $x[n]={\mathcal {Z}}^{-1}\{X(z)\}$ (definition of the inverse z-transform) | $r_{2}<\|z\|<r_{1}$ |
| Linearity | $a_{1}x_{1}[n]+a_{2}x_{2}[n]$ | $a_{1}X_{1}(z)+a_{2}X_{2}(z)$ | ${\begin{aligned}X(z)&=\sum _{n=-\infty }^{\infty }(a_{1}x_{1}[n]+a_{2}x_{2}[n])z^{-n}\\&=a_{1}\sum _{n=-\infty }^{\infty }x_{1}[n]\,z^{-n}+a_{2}\sum _{n=-\infty }^{\infty }x_{2}[n]\,z^{-n}\\&=a_{1}X_{1}(z)+a_{2}X_{2}(z)\end{aligned}}$ | Contains ROC1 ∩ ROC2 |
| Time expansion | $x_{K}[n]={\begin{cases}x[r],&n=Kr\\0,&n\notin K\mathbb {Z} \end{cases}}$ with $K\mathbb {Z$ | $X(z^{K})$ | ${\begin{aligned}X_{K}(z)&=\sum _{n=-\infty }^{\infty }x_{K}[n]z^{-n}\\&=\sum _{r=-\infty }^{\infty }x[r]z^{-rK}\\&=\sum _{r=-\infty }^{\infty }x[r](z^{K})^{-r}\\&=X(z^{K})\end{aligned}}$ | $R^{\frac {1}{K}}$ |
| Decimation | $x[Kn]$ | ${\frac {1}{K}}\sum _{p=0}^{K-1}X\left(z^{\tfrac {1}{K}}\cdot e^{-i{\tfrac {2\pi }{K}}p}\right)$ | ohio-state.edu or ee.ic.ac.uk |   |
| Time delay | $x[n-k]$ with $k>0$ and $x:x[n]=0\ \forall \,n<0$ | $z^{-k}X(z)$ | ${\begin{aligned}{\mathcal {Z}}\{x[n-k]\}&=\sum _{n=0}^{\infty }x[n-k]z^{-n}\\&=\sum _{m=-k}^{\infty }x[m]z^{-(m+k)}&&m=n-k\\&=\sum _{m=-k}^{\infty }x[m]z^{-m}z^{-k}\\&=z^{-k}\sum _{m=-k}^{\infty }x[m]z^{-m}\\&=z^{-k}\sum _{m=0}^{\infty }x[m]z^{-m}&&x[\beta ]=0,\forall \beta <0\\&=z^{-k}X(z)\end{aligned}}$ | ROC, except $z=0$ if $k>0$ and $z=\infty$ if $k<0$ |
| Time advance | $x[n+k]$ with $k>0$ | Bilateral Z-transform: $z^{k}X(z)$ Unilateral Z-transform: $z^{k}\,X(z)-z^{k}\sum _{n=0}^{k-1}x[n]\,z^{-n}$ |   |   |
| First difference backward | $x[n]-x[n-1]$ with $x[n]=0$ for $n<0$ | $(1-z^{-1})\,X(z)$ |   | Contains the intersection of ROC of $X_{1}(z)$ and $z\neq 0$ |
| First difference forward | $x[n+1]-x[n]$ | $(z-1)\,X(z)-z\,x[0]$ |   |   |
| Time reversal | $x[-n]$ | $X(z^{-1})$ | ${\begin{aligned}{\mathcal {Z}}\{x(-n)\}&=\sum _{n=-\infty }^{\infty }x[-n]z^{-n}\\&=\sum _{m=-\infty }^{\infty }x[m]z^{m}\\&=\sum _{m=-\infty }^{\infty }x[m]{(z^{-1})}^{-m}\\&=X(z^{-1})\\\end{aligned}}$ | ${\tfrac {1}{r_{1}}}<\|z\|<{\tfrac {1}{r_{2}}}$ |
| Scaling in the z-domain | $a^{n}x[n]$ | $X(a^{-1}z)$ | ${\begin{aligned}{\mathcal {Z}}\left\{a^{n}x[n]\right\}&=\sum _{n=-\infty }^{\infty }a^{n}x[n]z^{-n}\\&=\sum _{n=-\infty }^{\infty }x[n](a^{-1}z)^{-n}\\&=X(a^{-1}z)\end{aligned}}$ | $\|a\|r_{2}<\|z\|<\|a\|r_{1}$ |
| Complex conjugation | $x^{*}[n]$ | $X^{*}(z^{*})$ | ${\begin{aligned}{\mathcal {Z}}\{x^{*}(n)\}&=\sum _{n=-\infty }^{\infty }x^{*}[n]z^{-n}\\&=\sum _{n=-\infty }^{\infty }\left[x[n](z^{*})^{-n}\right]^{*}\\&=\left[\sum _{n=-\infty }^{\infty }x[n](z^{*})^{-n}\right]^{*}\\&=X^{*}(z^{*})\end{aligned}}$ |   |
| Real part | $\operatorname {Re} \{x[n]\}$ | ${\tfrac {1}{2}}\left[X(z)+X^{*}(z^{*})\right]$ |   |   |
| Imaginary part | $\operatorname {Im} \{x[n]\}$ | ${\tfrac {1}{2i}}\left[X(z)-X^{*}(z^{*})\right]$ |   |   |
| Differentiation in the z-domain | $n\,x[n]$ | $-z{\frac {dX(z)}{dz}}$ | ${\begin{aligned}{\mathcal {Z}}\{n\,x(n)\}&=\sum _{n=-\infty }^{\infty }n\,x[n]z^{-n}\\&=z\sum _{n=-\infty }^{\infty }n\,x[n]z^{-n-1}\\&=-z\sum _{n=-\infty }^{\infty }x[n](-n\,z^{-n-1})\\&=-z\sum _{n=-\infty }^{\infty }x[n]{\frac {d}{dz}}(z^{-n})\\&=-z{\frac {dX(z)}{dz}}\end{aligned}}$ | ROC, if $X(z)$ is rational; ROC possibly excluding the boundary, if $X(z)$ is irrational |
| Convolution | $x_{1}[n]*x_{2}[n]$ | $X_{1}(z)\,X_{2}(z)$ | ${\begin{aligned}{\mathcal {Z}}\{x_{1}(n)*x_{2}(n)\}&={\mathcal {Z}}\left\{\sum _{l=-\infty }^{\infty }x_{1}[l]x_{2}[n-l]\right\}\\&=\sum _{n=-\infty }^{\infty }\left[\sum _{l=-\infty }^{\infty }x_{1}[l]x_{2}[n-l]\right]z^{-n}\\&=\sum _{l=-\infty }^{\infty }x_{1}[l]\left[\sum _{n=-\infty }^{\infty }x_{2}[n-l]z^{-n}\right]\\&=\left[\sum _{l=-\infty }^{\infty }x_{1}(l)z^{-l}\right]\!\!\left[\sum _{n=-\infty }^{\infty }x_{2}[n]z^{-n}\right]\\&=X_{1}(z)X_{2}(z)\end{aligned}}$ | Contains ROC1 ∩ ROC2 |
| Cross-correlation | $r_{x_{1},x_{2}}=x_{1}^{*}[-n]*x_{2}[n]$ | $R_{x_{1},x_{2}}(z)=X_{1}^{*}({\tfrac {1}{z^{*}}})X_{2}(z)$ |   | Contains the intersection of ROC of $X_{1}({\tfrac {1}{z^{*}}})$ and $X_{2}(z)$ |
| Accumulation | $\sum _{k=-\infty }^{n}x[k]$ | ${\frac {1}{1-z^{-1}}}X(z)$ | ${\begin{aligned}\sum _{n=-\infty }^{\infty }\sum _{k=-\infty }^{n}x[k]z^{-n}&=\sum _{n=-\infty }^{\infty }(x[n]+\cdots )z^{-n}\\&=X(z)\left(1+z^{-1}+z^{-2}+\cdots \right)\\&=X(z)\sum _{j=0}^{\infty }z^{-j}\\&=X(z){\frac {1}{1-z^{-1}}}\end{aligned}}$ |   |
| Multiplication | $x_{1}[n]\,x_{2}[n]$ | ${\frac {1}{2\pi i}}\oint _{C}X_{1}(v)X_{2}({\tfrac {z}{v}})v^{-1}\mathrm {d} v$ |   | - |

**Parseval's theorem**

$\sum _{n=-\infty }^{\infty }x_{1}[n]x_{2}^{*}[n]\quad =\quad {\frac {1}{2\pi i}}\oint _{C}X_{1}(v)X_{2}^{*}({\tfrac {1}{v^{*}}})v^{-1}\mathrm {d} v$

**Initial value theorem** : If $x[n]$ is causal, then $x[0]=\lim _{z\to \infty }X(z).$

**Final value theorem**: If the poles of $(z-1)X(z)$ are inside the unit circle, then $x[\infty ]=\lim _{z\to 1}(z-1)X(z).$

## Table of common Z-transform pairs

Here:

$u:n\mapsto u[n]={\begin{cases}1,&n\geq 0\\0,&n<0\end{cases}}$

is the unit (or Heaviside) step function and

$\delta :n\mapsto \delta [n]={\begin{cases}1,&n=0\\0,&n\neq 0\end{cases}}$

is the discrete-time unit impulse function (cf. Dirac delta function, which is a continuous-time version). The two functions are chosen together so that the unit step function is the accumulation (running total) of the unit impulse function.

|   | Signal, $x[n]$ | Z-transform, $X(z)$ | ROC |
|---|---|---|---|
| 1 | $\delta [n]$ | 1 | all *z* |
| 2 | $\delta [n-n_{0}]$ | $z^{-n_{0}}$ | $z\neq 0$ |
| 3 | $u[n]$ | ${\frac {1}{1-z^{-1}}}$ | $\|z\|>1$ |
| 4 | $-u[-n-1]$ | ${\frac {1}{1-z^{-1}}}$ | $\|z\|<1$ |
| 5 | $nu[n]$ | ${\frac {z^{-1}}{(1-z^{-1})^{2}}}$ | $\|z\|>1$ |
| 6 | $-nu[-n-1]$ | ${\frac {z^{-1}}{(1-z^{-1})^{2}}}$ | $\|z\|<1$ |
| 7 | $n^{2}u[n]$ | ${\frac {z^{-1}(1+z^{-1})}{(1-z^{-1})^{3}}}$ | $\|z\|>1$ |
| 8 | $-n^{2}u[-n-1]$ | ${\frac {z^{-1}(1+z^{-1})}{(1-z^{-1})^{3}}}$ | $\|z\|<1$ |
| 9 | $n^{3}u[n]$ | ${\frac {z^{-1}(1+4z^{-1}+z^{-2})}{(1-z^{-1})^{4}}}$ | $\|z\|>1$ |
| 10 | $-n^{3}u[-n-1]$ | ${\frac {z^{-1}(1+4z^{-1}+z^{-2})}{(1-z^{-1})^{4}}}$ | $\|z\|<1$ |
| 11 | $a^{n}u[n]$ | ${\frac {1}{1-az^{-1}}}$ | $\|z\|>\|a\|$ |
| 12 | $-a^{n}u[-n-1]$ | ${\frac {1}{1-az^{-1}}}$ | $\|z\|<\|a\|$ |
| 13 | $na^{n}u[n]$ | ${\frac {az^{-1}}{(1-az^{-1})^{2}}}$ | $\|z\|>\|a\|$ |
| 14 | $-na^{n}u[-n-1]$ | ${\frac {az^{-1}}{(1-az^{-1})^{2}}}$ | $\|z\|<\|a\|$ |
| 15 | $n^{2}a^{n}u[n]$ | ${\frac {az^{-1}(1+az^{-1})}{(1-az^{-1})^{3}}}$ | $\|z\|>\|a\|$ |
| 16 | $-n^{2}a^{n}u[-n-1]$ | ${\frac {az^{-1}(1+az^{-1})}{(1-az^{-1})^{3}}}$ | $\|z\|<\|a\|$ |
| 17 | $\left({\begin{array}{c}n+m-1\\m-1\end{array}}\right)a^{n}u[n]$ [14] | ⁠ ${\frac {1}{(1-az^{-1})^{m}}}$ ⁠, for positive integer m | $\|z\|>\|a\|$ |
| 18 | $(-1)^{m}\left({\begin{array}{c}-n-1\\m-1\end{array}}\right)a^{n}u[-n-m]$ | ⁠ ${\frac {1}{(1-az^{-1})^{m}}}$ ⁠, for positive integer m | $\|z\|<\|a\|$ |
| 19 | $\cos(\omega _{0}n)u[n]$ | ${\frac {1-z^{-1}\cos(\omega _{0})}{1-2z^{-1}\cos(\omega _{0})+z^{-2}}}$ | $\|z\|>1$ |
| 20 | $\sin(\omega _{0}n)u[n]$ | ${\frac {z^{-1}\sin(\omega _{0})}{1-2z^{-1}\cos(\omega _{0})+z^{-2}}}$ | $\|z\|>1$ |
| 21 | $a^{n}\cos(\omega _{0}n)u[n]$ | ${\frac {1-az^{-1}\cos(\omega _{0})}{1-2az^{-1}\cos(\omega _{0})+a^{2}z^{-2}}}$ | $\|z\|>\|a\|$ |
| 22 | $a^{n}\sin(\omega _{0}n)u[n]$ | ${\frac {az^{-1}\sin(\omega _{0})}{1-2az^{-1}\cos(\omega _{0})+a^{2}z^{-2}}}$ | $\|z\|>\|a\|$ |

## Relationship to Fourier series and Fourier transform

For values of z in the region ⁠ $\vert z\vert =1$ ⁠, known as the unit circle, we can express the transform as a function of a single real variable $\omega$ by defining ⁠ $z=e^{i\omega }$ ⁠. The bilateral transform reduces to a Fourier series:

| $\sum _{n=-\infty }^{\infty }x[n]\ z^{-n}=\sum _{n=-\infty }^{\infty }x[n]\ e^{-i\omega n},$ |   | Eq.1 |
|---|---|---|

which is also known as the discrete-time Fourier transform (DTFT) of the $x[n]$ sequence. This $2\pi$ -periodic function is the periodic summation of a Fourier transform, which makes it a widely used analysis tool. To understand this, let $X(f)$ be the Fourier transform of any function, ⁠ $x(t)$ ⁠, whose samples at some interval T equal the $x[n]$ sequence. Then the DTFT of the $x[n]$ sequence can be written as follows.

| $\underbrace {\sum _{n=-\infty }^{\infty }\overbrace {x(nT)} ^{x[n]}e^{-2i\pi fnT}} _{\text{DTFT}}={\frac {1}{T}}\sum _{k=-\infty }^{\infty }X(f-k/T),$ |   | Eq.2 |
|---|---|---|

where T has units of seconds, f has units of hertz. Comparison of the two series reveals that $\omega =2\pi fT$ is a normalized frequency with unit of *radian per sample*. The value $\omega =2\pi$ corresponds to ⁠ $f={\tfrac {1}{T}}$ ⁠. And now, with the substitution ⁠ $f={\tfrac {\omega }{2\pi T}}$ ⁠, **Eq.1** can be expressed in terms of $X({\tfrac {\omega -2\pi k}{2\pi T}})$ (a Fourier transform):

| $\sum _{n=-\infty }^{\infty }x[n]\ e^{-i\omega n}={\frac {1}{T}}\sum _{k=-\infty }^{\infty }\underbrace {X\left({\tfrac {\omega }{2\pi T}}-{\tfrac {k}{T}}\right)} _{X\left({\frac {\omega -2\pi k}{2\pi T}}\right)}.$ |   | Eq.3 |
|---|---|---|

As parameter *T* changes, the individual terms of **Eq.2** move farther apart or closer together along the *f*-axis. In **Eq.3** however, the centers remain 2π apart, while their widths expand or contract. When sequence $x(nT)$ represents the impulse response of an LTI system, these functions are also known as its frequency response. When the $x(nT)$ sequence is periodic, its DTFT is divergent at one or more harmonic frequencies, and zero at all other frequencies. This is often represented by the use of amplitude-variant Dirac delta functions at the harmonic frequencies. Due to periodicity, there are only a finite number of unique amplitudes, which are readily computed by the much simpler discrete Fourier transform (DFT). (See *Discrete-time Fourier transform § Periodic data*.)

## Relationship to Laplace transform

### Bilinear transform

The **bilinear transform** can be used to convert continuous-time filters (represented in the Laplace domain) into discrete-time filters (represented in the Z-domain), and vice versa. The following substitution is used:

$s={\frac {2}{T}}{\frac {(z-1)}{(z+1)}}$

to convert some function $H(s)$ in the Laplace domain to a function $H(z)$ in the Z-domain (Tustin transformation), or

$z=e^{sT}\approx {\frac {1+sT/2}{1-sT/2}}$

from the Z-domain to the Laplace domain. Through the bilinear transformation, the complex *s*-plane (of the Laplace transform) is mapped to the complex z-plane (of the z-transform). While this mapping is (necessarily) nonlinear, it is useful in that it maps the entire $i\omega$ axis of the *s*-plane onto the unit circle in the z-plane. As such, the Fourier transform (which is the Laplace transform evaluated on the $i\omega$ axis) becomes the discrete-time Fourier transform. This assumes that the Fourier transform exists; i.e., that the $i\omega$ axis is in the region of convergence of the Laplace transform.

### Starred transform

Given a one-sided Z-transform $X(z)$ of a time-sampled function, the corresponding **starred transform** produces a Laplace transform and restores the dependence on T (the sampling parameter):

${\bigg .}X^{*}(s)=X(z){\bigg |}_{\displaystyle z=e^{sT}}$

The inverse Laplace transform is a mathematical abstraction known as an *impulse-sampled* function.

## Linear constant-coefficient difference equation

The linear constant-coefficient difference (LCCD) equation is a representation for a linear system based on the autoregressive moving-average equation:

$\sum _{p=0}^{N}y[n-p]\alpha _{p}=\sum _{q=0}^{M}x[n-q]\beta _{q}.$

Both sides of the above equation can be divided by $\alpha _{0}$ if it is not zero. By normalizing with ⁠ $\alpha _{0}=1$ ⁠, the LCCD equation can be written

$y[n]=\sum _{q=0}^{M}x[n-q]\beta _{q}-\sum _{p=1}^{N}y[n-p]\alpha _{p}.$

This form of the LCCD equation is favorable to make it more explicit that the "current" output $y[n]$ is a function of past outputs ⁠ $y[n-p]$ ⁠, current input ⁠ $x[n]$ ⁠, and previous inputs ⁠ $x[n-q]$ ⁠.

### Transfer function

Taking the Z-transform of the above equation (using linearity and time-shifting laws) yields:

$Y(z)\sum _{p=0}^{N}z^{-p}\alpha _{p}=X(z)\sum _{q=0}^{M}z^{-q}\beta _{q}$

where $X(z)$ and $Y(z)$ are the Z-transform of $x[n]$ and ⁠ $y[n]$ ⁠, respectively. (Notation conventions typically use capitalized letters to refer to the Z-transform of a signal denoted by a corresponding lower case letter, similar to the convention used for notating Laplace transforms.)

Rearranging results in the system's transfer function:

$H(z)={\frac {Y(z)}{X(z)}}={\frac {\sum _{q=0}^{M}z^{-q}\beta _{q}}{\sum _{p=0}^{N}z^{-p}\alpha _{p}}}={\frac {\beta _{0}+z^{-1}\beta _{1}+z^{-2}\beta _{2}+\cdots +z^{-M}\beta _{M}}{\alpha _{0}+z^{-1}\alpha _{1}+z^{-2}\alpha _{2}+\cdots +z^{-N}\alpha _{N}}}.$

### Zeros and poles

From the fundamental theorem of algebra the numerator has M roots (corresponding to zeros of *H*) and the denominator has N roots (corresponding to poles). Rewriting the transfer function in terms of zeros and poles

$H(z)={\frac {(1-q_{1}z^{-1})(1-q_{2}z^{-1})\cdots (1-q_{M}z^{-1})}{(1-p_{1}z^{-1})(1-p_{2}z^{-1})\cdots (1-p_{N}z^{-1})}},$

where $q_{k}$ is the k th zero and $p_{k}$ is the k th pole. The zeros and poles are commonly complex and when plotted on the complex plane (z-plane) it is called the pole–zero plot.

In addition, there may also exist zeros and poles at $z=0$ and ⁠ $z=\infty$ ⁠. If we take these poles and zeros as well as multiple-order zeros and poles into consideration, the number of zeros and poles are always equal.

By factoring the denominator, partial fraction decomposition can be used, which can then be transformed back to the time domain. Doing so would result in the impulse response and the linear constant coefficient difference equation of the system.

### Output response

If such a system $H(z)$ is driven by a signal $X(z)$ then the output is ⁠ $Y(z)=H(z)X(z)$ ⁠. By performing partial fraction decomposition on $Y(z)$ and then taking the inverse Z-transform the output $y[n]$ can be found. In practice, it is often useful to fractionally decompose $\textstyle {\frac {Y(z)}{z}}$ before multiplying that quantity by z to generate a form of $Y(z)$ which has terms with easily computable inverse Z-transforms.
