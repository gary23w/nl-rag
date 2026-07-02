---
title: "Fourier series"
source: https://en.wikipedia.org/wiki/Fourier_series
domain: fourier-analysis
license: CC-BY-SA-4.0
tags: fourier analysis, fourier transform, fourier series, fast fourier transform
fetched: 2026-07-02
---

# Fourier series

A **Fourier series** (/ˈfʊrieɪ, -iər/) is a series expansion of a periodic function into a sum of trigonometric functions. The Fourier series is an example of a trigonometric series. By expressing a function as a sum of sines and cosines, many problems involving the function become easier to analyze because trigonometric functions are well understood. For example, Fourier series were first used by Joseph Fourier to find solutions to the heat equation. This application is possible because the derivatives of trigonometric functions fall into simple patterns. Fourier series cannot be used to approximate arbitrary functions, because most functions have infinitely many terms in their Fourier series, and the series do not always converge. Well-behaved functions, for example smooth functions, have Fourier series that converge to the original function. The coefficients of the Fourier series are determined by integrals of the function multiplied by trigonometric functions, described in Fourier series § Definition.

The study of the convergence of Fourier series focus on the behaviors of the *partial sums*, which means studying the behavior of the sum as more and more terms from the series are summed. The figures below illustrate some partial Fourier series results for the components of a square wave.

- (A square wave (represented as the blue dot) is approximated by its sixth partial sum (represented as the purple dot), formed by summing the first six terms (represented as arrows) of the square wave's Fourier series. Each arrow starts at the vertical sum of all the arrows to its left (i.e. the previous partial sum).) A square wave (represented as the blue dot) is approximated by its sixth partial sum (represented as the purple dot), formed by summing the first six terms (represented as arrows) of the square wave's Fourier series. Each arrow starts at the vertical sum of all the arrows to its left (i.e. the previous partial sum).
- (The first four partial sums of the Fourier series for a square wave. As more harmonics are added, the partial sums converge to the square wave.) The first four partial sums of the Fourier series for a square wave. As more harmonics are added, the partial sums converge to the square wave.
- (Function '"`UNIQ--postMath-00000001-QINU`"' (in red) is a Fourier series sum of 6 harmonically related sine waves (in blue). Its Fourier transform '"`UNIQ--postMath-00000002-QINU`"' is a frequency-domain representation that reveals the amplitudes of the summed sine waves.) Function $s_{6}(x)$ (in red) is a Fourier series sum of 6 harmonically related sine waves (in blue). Its Fourier transform $S(f)$ is a frequency-domain representation that reveals the amplitudes of the summed sine waves.

Fourier series are closely related to the Fourier transform, a more general tool that can even find the frequency information for functions that are *not* periodic. Periodic functions can be identified with functions on a circle; for this reason Fourier series are the subject of Fourier analysis on the circle group, denoted by $\mathbb {T}$ or $S_{1}$ . The Fourier transform is also part of Fourier analysis, but is defined for functions on $\mathbb {R} ^{n}$ .

Since Fourier's time, many different approaches to defining and understanding the concept of Fourier series have been discovered, all of which are consistent with one another, but each of which emphasizes different aspects of the topic. Some of the more powerful and elegant approaches are based on mathematical ideas and tools that were not available in Fourier's time. Fourier originally defined the Fourier series for real-valued functions of real arguments, and used the sine and cosine functions in the series expansion. Many other Fourier-related transforms have since been defined, extending his initial idea to many applications and birthing an area of mathematics called Fourier analysis.

## History

The Fourier series is named in honor of Jean-Baptiste Joseph Fourier (1768–1830), who made important contributions to the study of trigonometric series, after preliminary investigations by Leonhard Euler, Jean le Rond d'Alembert, and Daniel Bernoulli. Fourier introduced the series for the purpose of solving the heat equation in a metal plate, publishing his initial results in his 1807 *Mémoire sur la propagation de la chaleur dans les corps solides* (*Treatise on the propagation of heat in solid bodies*), and publishing his *Théorie analytique de la chaleur* (*Analytical theory of heat*) in 1822. The *Mémoire* introduced Fourier analysis, specifically Fourier series. Through Fourier's research the fact was established that an arbitrary (at first, continuous and later generalized to any piecewise-smooth) function can be represented by a trigonometric series. The first announcement of this great discovery was made by Fourier in 1807, before the French Academy. Early ideas of decomposing a periodic function into the sum of simple oscillating functions date back to the 3rd century BC, when ancient astronomers proposed an empiric model of planetary motions, based on deferents and epicycles.

Independently of Fourier, astronomer Friedrich Wilhelm Bessel introduced Fourier series to solve Kepler's equation. His work was published in 1819, unaware of Fourier's work which remained unpublished until 1822.

The heat equation is a partial differential equation. Prior to Fourier's work, no solution to the heat equation was known in the general case, although particular solutions were known if the heat source behaved in a simple way, in particular, if the heat source was a sine or cosine wave. These simple solutions are now sometimes called eigensolutions. Fourier's idea was to model a complicated heat source as a superposition (or linear combination) of simple sine and cosine waves, and to write the solution as a superposition of the corresponding eigensolutions. This superposition or linear combination is called the Fourier series.

From a modern point of view, Fourier's results are somewhat informal, due to the lack of a precise notion of function and integral in the early nineteenth century. Later, Peter Gustav Lejeune Dirichlet and Bernhard Riemann expressed Fourier's results with greater precision and formality.

Although the original motivation was to solve the heat equation, it later became obvious that the same techniques could be applied to a wide array of mathematical and physical problems, and especially those involving linear differential equations with constant coefficients, for which the eigensolutions are sinusoids. The Fourier series has many such applications in electrical engineering, vibration analysis, acoustics, optics, signal processing, image processing, quantum mechanics, econometrics, shell theory, etc.

### Beginnings

Joseph Fourier wrote

> $\varphi (y)=a_{0}\cos {\frac {\pi y}{2}}+a_{1}\cos 3{\frac {\pi y}{2}}+a_{2}\cos 5{\frac {\pi y}{2}}+\cdots .$
> 
> Multiplying both sides by $\cos(2k+1){\frac {\pi y}{2}}$ , and then integrating from $y=-1$ to $y=+1$ yields:
> 
> $a_{k}=\int _{-1}^{1}\varphi (y)\cos(2k+1){\frac {\pi y}{2}}\,dy.$

— Joseph Fourier, Mémoire sur la propagation de la chaleur dans les corps solides (1807).

This immediately gives any coefficient *ak* of the trigonometric series for φ(*y*) for any function which has such an expansion. It works because if φ has such an expansion, then (under suitable convergence assumptions) the integral ${\begin{aligned}&\int _{-1}^{1}\varphi (y)\cos(2k+1){\frac {\pi y}{2}}\,dy\\&=\int _{-1}^{1}\left(a\cos {\frac {\pi y}{2}}\cos(2k+1){\frac {\pi y}{2}}+a'\cos 3{\frac {\pi y}{2}}\cos(2k+1){\frac {\pi y}{2}}+\cdots \right)\,dy\end{aligned}}$ can be carried out term-by-term. But all terms involving $\cos(2j+1){\frac {\pi y}{2}}\cos(2k+1){\frac {\pi y}{2}}$ for *j* ≠ *k* vanish when integrated from −1 to 1, leaving only the $k^{\text{th}}$ term, which is *1*.

In these few lines, which are close to the modern formalism used in Fourier series, Fourier revolutionized both mathematics and physics. Although similar trigonometric series were previously used by Euler, d'Alembert, Daniel Bernoulli and Gauss, Fourier believed that such trigonometric series could represent any arbitrary function. In what sense that is actually true is a somewhat subtle issue and the attempts over many years to clarify this idea have led to important discoveries in the theories of convergence, function spaces, and harmonic analysis.

When Fourier submitted a later competition essay in 1811, the committee (which included Lagrange, Laplace, Malus and Legendre, among others) concluded: "...the manner in which the author arrives at these equations is not exempt of difficulties and...his analysis to integrate them still leaves something to be desired on the score of generality and even rigour".

### Fourier's motivation

The Fourier series expansion of the sawtooth function (below) looks more complicated than the simple formula $s(x)={\tfrac {x}{\pi }}$ , so it is not immediately apparent why one would need the Fourier series. While there are many applications, Fourier's motivation was in solving the heat equation. For example, consider a metal plate in the shape of a square whose sides measure $\pi$ meters, with coordinates $(x,y)\in [0,\pi ]\times [0,\pi ]$ . If there is no heat source within the plate, and if three of the four sides are held at 0 degrees Celsius, while the fourth side, given by $y=\pi$ , is maintained at the temperature gradient $T(x,\pi )=x$ degrees Celsius, for x in $(0,\pi )$ , then one can show that the stationary heat distribution (or the heat distribution after a long time has elapsed) is given by

$T(x,y)=2\sum _{n=1}^{\infty }{\frac {(-1)^{n+1}}{n}}\sin(nx){\sinh(ny) \over \sinh(n\pi )}.$

Here, $\sinh$ is the hyperbolic sine function. This solution of the heat equation is obtained by multiplying each term of the equation from Analysis § Example by $\sinh(ny)/\sinh(n\pi )$ . While our example function $s(x)$ seems to have a needlessly complicated Fourier series, the heat distribution $T(x,y)$ is nontrivial. The function T cannot be written as a closed-form expression. This method of solving the heat problem was made possible by Fourier's work.

### Other applications

Another application is to solve the Basel problem by using Parseval's theorem. The example generalizes and one may compute ζ(2*n*), for any positive integer *n*.

## Definition

The Fourier series of a complex-valued *P*-periodic function $s(x)$ , integrable over the interval $[0,P]$ on the real line, is defined as a trigonometric series of the form $\sum _{n=-\infty }^{\infty }c_{n}e^{i2\pi {\tfrac {n}{P}}x},$ such that the *Fourier coefficients* $c_{n}$ are complex numbers defined by the integral $c_{n}={\frac {1}{P}}\int _{0}^{P}s(x)\ e^{-i2\pi {\tfrac {n}{P}}x}\,dx.$ The series does not necessarily converge (in the pointwise sense) and, even if it does, it is not necessarily equal to $s(x)$ . Only when certain conditions are satisfied (e.g. if $s(x)$ is continuously differentiable) does the Fourier series converge to $s(x)$ , i.e., $s(x)=\sum _{n=-\infty }^{\infty }c_{n}e^{i2\pi {\tfrac {n}{P}}x}.$ For functions satisfying the Dirichlet sufficiency conditions, pointwise convergence holds. However, these are not necessary conditions and there are many theorems about different types of convergence of Fourier series (e.g. uniform convergence or mean convergence). The definition naturally extends to the Fourier series of a (periodic) distribution s (also called *Fourier-Schwartz series*). Then the Fourier series converges to $s(x)$ in the distribution sense.

The process of determining the Fourier coefficients of a given function or signal is called ***analysis***, while forming the associated trigonometric series (or its various approximations) is called ***synthesis***.

### Synthesis

A Fourier series can be written in several equivalent forms, shown here as the $N^{\text{th}}$ partial sums $s_{N}(x)$ of the Fourier series of $s(x)$ :

Sine-cosine form

| $s_{N}(x)=a_{0}+\sum _{n=1}^{N}\left(a_{n}\cos \left(2\pi {\tfrac {n}{P}}x\right)+b_{n}\sin \left(2\pi {\tfrac {n}{P}}x\right)\right)$ |   | Eq.1 |
|---|---|---|

Exponential form

| $s_{N}(x)=\sum _{n=-N}^{N}c_{n}\ e^{i2\pi {\tfrac {n}{P}}x}$ |   | Eq.2 |
|---|---|---|

The harmonics are indexed by an integer, $n,$ which is also the number of cycles the corresponding sinusoids make in interval P . Therefore, the sinusoids have**:**

- a wavelength equal to ${\tfrac {P}{n}}$ in the same units as x .
- a frequency equal to ${\tfrac {n}{P}}$ in the reciprocal units of x .

These series can represent functions that are just a sum of one or more frequencies in the harmonic spectrum. In the limit $N\to \infty$ , a trigonometric series can also represent the intermediate frequencies or non-sinusoidal functions because of the infinite number of terms.

### Analysis

The coefficients can be given/assumed, such as a music synthesizer or time samples of a waveform. In the latter case, the exponential form of Fourier series synthesizes a discrete-time Fourier transform where variable x represents frequency instead of time. In general, the coefficients are determined by *analysis* of a given function $s(x)$ whose domain of definition is an interval of length P .

Fourier coefficients

| ${\begin{aligned}&a_{0}={\frac {1}{P}}\int _{P}s(x)\,dx&\\&a_{n}={\frac {2}{P}}\int _{P}s(x)\cos \left(2\pi {\tfrac {n}{P}}x\right)\,dx,\ &{\textrm {for}}~n\geq 1\\&b_{n}={\frac {2}{P}}\int _{P}s(x)\sin \left(2\pi {\tfrac {n}{P}}x\right)\,dx,\ &{\text{for}}~n\geq 1\\\end{aligned}}$ |   | Eq.3 |
|---|---|---|

The ${\tfrac {2}{P}}$ scale factor follows from substituting **Eq.1** into **Eq.3** and utilizing the orthogonality of the trigonometric system. The equivalence of **Eq.1** and **Eq.2** follows from Euler's formula $\cos x={\frac {e^{ix}+e^{-ix}}{2}},\quad \sin x={\frac {e^{ix}-e^{-ix}}{2i}},$ resulting in:

Exponential form coefficients

$c_{n}={\begin{cases}{\tfrac {1}{2}}(a_{n}-ib_{n})&{\text{if }}n>0,\\a_{n}&{\text{if }}n=0,\\{\tfrac {1}{2}}(a_{-n}+ib_{-n})&{\text{if }}n<0,\\\end{cases}}$

with $c_{0}$ being the mean value of s on the interval P . Conversely:

Inverse relationships

${\begin{aligned}a_{0}&=c_{0}&\\a_{n}&=c_{n}+c_{-n}\qquad &{\textrm {for}}~n>0\\b_{n}&=i(c_{n}-c_{-n})\qquad &{\textrm {for}}~n>0\end{aligned}}$

#### Example

Consider a sawtooth function: $s(x)=s(x+2\pi k)={\frac {x}{\pi }},\quad \mathrm {for} -\pi <x<\pi ,{\text{ and }}k\in \mathbb {Z} .$ In this case, the Fourier coefficients are given by ${\begin{aligned}a_{0}&=0.\\a_{n}&={\frac {1}{\pi }}\int _{-\pi }^{\pi }s(x)\cos(nx)\,dx=0,\quad n\geq 1.\\b_{n}&={\frac {1}{\pi }}\int _{-\pi }^{\pi }s(x)\sin(nx)\,dx\\&=-{\frac {2}{\pi n}}\cos(n\pi )+{\frac {2}{\pi ^{2}n^{2}}}\sin(n\pi )\\&={\frac {2\,(-1)^{n+1}}{\pi n}},\quad n\geq 1.\end{aligned}}$ It can be shown that the Fourier series converges to $s(x)$ at every point x where s is differentiable, and therefore: ${\begin{aligned}s(x)&=a_{0}+\sum _{n=1}^{\infty }\left[a_{n}\cos \left(nx\right)+b_{n}\sin \left(nx\right)\right]\\[4pt]&={\frac {2}{\pi }}\sum _{n=1}^{\infty }{\frac {(-1)^{n+1}}{n}}\sin(nx),\quad \mathrm {for} \ (x-\pi )\ {\text{is not a multiple of}}\ 2\pi .\end{aligned}}$ When $x=\pi$ , the Fourier series converges to 0, which is the half-sum of the left- and right-limit of s at $x=\pi$ . This is a particular instance of the Dirichlet theorem for Fourier series.

This example leads to a solution of the Basel problem.

### Amplitude-phase form

If the function $s(x)$ is real-valued then the Fourier series can also be represented as

Amplitude-phase form

| $s_{N}(x)=A_{0}+\sum _{n=1}^{N}A_{n}\cos \left(2\pi {\tfrac {n}{P}}x-\varphi _{n}\right)$ |   | Eq.4 |
|---|---|---|

where $A_{n}$ is the amplitude and $\varphi _{n}$ is the phase shift of the $n^{th}$ harmonic.

The equivalence of **Eq.4** and **Eq.1** follows from the trigonometric identity: $\cos \left(2\pi {\tfrac {n}{P}}x-\varphi _{n}\right)=\cos(\varphi _{n})\cos \left(2\pi {\tfrac {n}{P}}x\right)+\sin(\varphi _{n})\sin \left(2\pi {\tfrac {n}{P}}x\right),$ which implies $a_{n}=A_{n}\cos(\varphi _{n})\quad {\text{and}}\quad b_{n}=A_{n}\sin(\varphi _{n})$

are the rectangular coordinates of a vector written in polar coordinates as $A_{n}\angle \varphi _{n}=a_{n}+ib_{n}$ where $A_{n}={\sqrt {a_{n}^{2}+b_{n}^{2}}}\quad {\text{and}}\quad \varphi _{n}=\operatorname {atan2} (b_{n},a_{n})=-\operatorname {Arg} (c_{n})$

An example of determining the parameter $\varphi _{n}$ for one value of n is shown in Figure 2. It is the value of $\varphi$ at the maximum correlation between $s(x)$ and a cosine *template,* $\cos(2\pi {\tfrac {n}{P}}x-\varphi )$ . The blue graph is the cross-correlation function, also known as a matched filter:

${\begin{aligned}\mathrm {X} (\varphi )&=\int _{P}s(x)\cdot \cos \left(2\pi {\tfrac {n}{P}}x-\varphi \right)\,dx\quad \varphi \in \left[0,2\pi \right]\\&=\cos(\varphi )\underbrace {\int _{P}s(x)\cdot \cos \left(2\pi {\tfrac {n}{P}}x\right)dx} _{X(0)}+\sin(\varphi )\underbrace {\int _{P}s(x)\cdot \sin \left(2\pi {\tfrac {n}{P}}x\right)dx} _{X(\pi /2)}\end{aligned}}$

Fortunately, it is not necessary to evaluate this entire function, because its derivative is zero at the maximum: $X'(\varphi )=\sin(\varphi )\cdot X(0)-\cos(\varphi )\cdot X(\pi /2)=0,\quad {\textrm {at}}\ \varphi =\varphi _{n}.$ Hence $\varphi _{n}\equiv \arctan(b_{n}/a_{n})=\arctan(X(\pi /2)/X(0)).$

### Common notations

The notation $c_{n}$ is inadequate for discussing the Fourier coefficients of several different functions. Therefore, it is customarily replaced by a modified form of the function ( $s,$ in this case), such as ${\widehat {s}}(n)$ or $S[n],$ and functional notation often replaces subscripting**:**

${\begin{aligned}s(x)&=\sum _{n=-\infty }^{\infty }{\widehat {s}}(n)\cdot e^{i2\pi {\tfrac {n}{P}}x}&&\scriptstyle {\text{common mathematics notation}}\\&=\sum _{n=-\infty }^{\infty }S[n]\cdot e^{i2\pi {\tfrac {n}{P}}x}&&\scriptstyle {\text{common engineering notation}}\end{aligned}}$

In engineering, particularly when the variable x represents time, the coefficient sequence is called a frequency domain representation. Square brackets are often used to emphasize that the domain of this function is a discrete set of frequencies.

Another commonly used frequency domain representation uses the Fourier series coefficients to modulate a Dirac comb:

$S(f)\ \triangleq \ \sum _{n=-\infty }^{\infty }S[n]\cdot \delta \left(f-{\frac {n}{P}}\right),$

where f represents a continuous frequency domain. When variable x has units of seconds, f has units of hertz. The "teeth" of the comb are spaced at multiples (i.e. harmonics) of ${\tfrac {1}{P}}$ , which is called the fundamental frequency. $s(x)$ can be recovered from this representation by an inverse Fourier transform:

${\begin{aligned}{\mathcal {F}}^{-1}\{S(f)\}&=\int _{-\infty }^{\infty }\left(\sum _{n=-\infty }^{\infty }S[n]\cdot \delta \left(f-{\frac {n}{P}}\right)\right)e^{i2\pi fx}\,df,\\[6pt]&=\sum _{n=-\infty }^{\infty }S[n]\cdot \int _{-\infty }^{\infty }\delta \left(f-{\frac {n}{P}}\right)e^{i2\pi fx}\,df,\\[6pt]&=\sum _{n=-\infty }^{\infty }S[n]\cdot e^{i2\pi {\tfrac {n}{P}}x}\ \ \triangleq \ s(x).\end{aligned}}$

The constructed function $S(f)$ is therefore commonly referred to as a **Fourier transform**, even though the Fourier integral of a periodic function is not convergent at the harmonic frequencies.

## Table of common Fourier series

Some common pairs of periodic functions and their Fourier series coefficients are shown in the table below.

- $s(x)$ designates a periodic function with period $P.$
- $a_{0},a_{n},b_{n}$ designate the Fourier series coefficients (sine-cosine form) of the periodic function $s(x).$

| Time domain $s(x)$ | Plot | Frequency domain (sine-cosine form) ${\begin{aligned}&a_{0}\\&a_{n}\quad {\text{for }}n\geq 1\\&b_{n}\quad {\text{for }}n\geq 1\end{aligned}}$ | Remarks | Reference |
|---|---|---|---|---|
| $s(x)=A\left\|\sin \left({\frac {2\pi }{P}}x\right)\right\|\quad {\text{for }}0\leq x<P$ |   | ${\begin{aligned}a_{0}=&{\frac {2A}{\pi }}\\a_{n}=&{\begin{cases}{\frac {-4A}{\pi }}{\frac {1}{n^{2}-1}}&\quad n{\text{ even}}\\0&\quad n{\text{ odd}}\end{cases}}\\b_{n}=&0\\\end{aligned}}$ | Full-wave rectified sine |   |
| $s(x)={\begin{cases}A\sin \left({\frac {2\pi }{P}}x\right)&\quad {\text{for }}0\leq x<P/2\\0&\quad {\text{for }}P/2\leq x<P\\\end{cases}}$ |   | ${\begin{aligned}a_{0}=&{\frac {A}{\pi }}\\a_{n}=&{\begin{cases}{\frac {-2A}{\pi }}{\frac {1}{n^{2}-1}}&\quad n{\text{ even}}\\0&\quad n{\text{ odd}}\end{cases}}\\b_{n}=&{\begin{cases}{\frac {A}{2}}&\quad n=1\\0&\quad n>1\end{cases}}\\\end{aligned}}$ | Half-wave rectified sine |   |
| $s(x)={\begin{cases}A&\quad {\text{for }}0\leq x<D\cdot P\\0&\quad {\text{for }}D\cdot P\leq x<P\\\end{cases}}$ |   | ${\begin{aligned}a_{0}=&AD\\a_{n}=&{\frac {A}{n\pi }}\sin \left(2\pi nD\right)\\b_{n}=&{\frac {2A}{n\pi }}\left(\sin \left(\pi nD\right)\right)^{2}\\\end{aligned}}$ | $0\leq D\leq 1$ |   |
| $s(x)={\frac {Ax}{P}}\quad {\text{for }}0\leq x<P$ |   | ${\begin{aligned}a_{0}=&{\frac {A}{2}}\\a_{n}=&0\\b_{n}=&{\frac {-A}{n\pi }}\\\end{aligned}}$ |   |   |
| $s(x)=A-{\frac {Ax}{P}}\quad {\text{for }}0\leq x<P$ |   | ${\begin{aligned}a_{0}=&{\frac {A}{2}}\\a_{n}=&0\\b_{n}=&{\frac {A}{n\pi }}\\\end{aligned}}$ |   |   |
| $s(x)={\frac {4A}{P^{2}}}\left(x-{\frac {P}{2}}\right)^{2}\quad {\text{for }}0\leq x<P$ |   | ${\begin{aligned}a_{0}=&{\frac {A}{3}}\\a_{n}=&{\frac {4A}{\pi ^{2}n^{2}}}\\b_{n}=&0\\\end{aligned}}$ |   |   |

## Table of basic transformation rules

This table shows some mathematical operations in the time domain and the corresponding effect in the Fourier series coefficients. Notation:

- Complex conjugation is denoted by an asterisk.
- $s(x),r(x)$ designate P -periodic functions **or** functions defined only for $x\in [0,P].$
- $S[n],R[n]$ designate the Fourier series coefficients (exponential form) of s and $r.$

| Property | Time domain | Frequency domain (exponential form) | Remarks | Reference |
|---|---|---|---|---|
| Linearity | $a\cdot s(x)+b\cdot r(x)$ | $a\cdot S[n]+b\cdot R[n]$ | $a,b\in \mathbb {C}$ |   |
| Time reversal / Frequency reversal | $s(-x)$ | $S[-n]$ |   |   |
| Time conjugation | $s^{*}(x)$ | $S^{*}[-n]$ |   |   |
| Time reversal & conjugation | $s^{*}(-x)$ | $S^{*}[n]$ |   |   |
| Real part in time | $\operatorname {Re} {(s(x))}$ | ${\frac {1}{2}}(S[n]+S^{*}[-n])$ |   |   |
| Imaginary part in time | $\operatorname {Im} {(s(x))}$ | ${\frac {1}{2i}}(S[n]-S^{*}[-n])$ |   |   |
| Real part in frequency | ${\frac {1}{2}}(s(x)+s^{*}(-x))$ | $\operatorname {Re} {(S[n])}$ |   |   |
| Imaginary part in frequency | ${\frac {1}{2i}}(s(x)-s^{*}(-x))$ | $\operatorname {Im} {(S[n])}$ |   |   |
| Shift in time / Modulation in frequency | $s(x-x_{0})$ | $S[n]\cdot e^{-i2\pi {\tfrac {x_{0}}{P}}n}$ | $x_{0}\in \mathbb {R}$ |   |
| Shift in frequency / Modulation in time | $s(x)\cdot e^{i2\pi {\frac {n_{0}}{P}}x}$ | $S[n-n_{0}]\!$ | $n_{0}\in \mathbb {Z}$ |   |

## Properties

### Symmetry relations

When the real and imaginary parts of a complex function are decomposed into their even and odd parts, there are four components, denoted below by the subscripts **RE, RO, IE, and IO.** And there is a one-to-one mapping between the four components of a complex time function and the four components of its complex frequency transform:

${\begin{array}{rlcccccccc}{\mathsf {Time\ domain}}&s&=&s_{\mathrm {RE} }&+&s_{\mathrm {RO} }&+&i\ s_{\mathrm {IE} }&+&i\ s_{\mathrm {IO} }\\&{\Bigg \Updownarrow }{\mathcal {F}}&&{\Bigg \Updownarrow }{\mathcal {F}}&&\ \ {\Bigg \Updownarrow }{\mathcal {F}}&&\ \ {\Bigg \Updownarrow }{\mathcal {F}}&&\ \ {\Bigg \Updownarrow }{\mathcal {F}}\\{\mathsf {Frequency\ domain}}&S&=&S_{\mathrm {RE} }&+&i\ S_{\mathrm {IO} }\,&+&i\ S_{\mathrm {IE} }&+&S_{\mathrm {RO} }\end{array}}$

From this, various relationships are apparent, for example**:**

- The transform of a real-valued function $(s_{\mathrm {RE} }+s_{\mathrm {RO} })$ is the *conjugate symmetric* function $S_{\mathrm {RE} }+i\ S_{\mathrm {IO} }.$ Conversely, a *conjugate symmetric* transform implies a real-valued time-domain.
- The transform of an imaginary-valued function $(i\ s_{\mathrm {IE} }+i\ s_{\mathrm {IO} })$ is the *conjugate antisymmetric* function $S_{\mathrm {RO} }+i\ S_{\mathrm {IE} },$ and the converse is true.
- The transform of a *conjugate symmetric* function $(s_{\mathrm {RE} }+i\ s_{\mathrm {IO} })$ is the real-valued function $S_{\mathrm {RE} }+S_{\mathrm {RO} },$ and the converse is true.
- The transform of a *conjugate antisymmetric* function $(s_{\mathrm {RO} }+i\ s_{\mathrm {IE} })$ is the imaginary-valued function $i\ S_{\mathrm {IE} }+i\ S_{\mathrm {IO} },$ and the converse is true.

### Riemann–Lebesgue lemma

If S is integrable, ${\textstyle \lim _{|n|\to \infty }S[n]=0}$ , ${\textstyle \lim _{n\to +\infty }a_{n}=0}$ and ${\textstyle \lim _{n\to +\infty }b_{n}=0.}$

### Parseval's theorem

If s belongs to $L^{2}(P)$ (periodic over an interval of length P ) then: ${\frac {1}{P}}\int _{P}|s(x)|^{2}\,dx=\sum _{n=-\infty }^{\infty }{\Bigl |}S[n]{\Bigr |}^{2}.$

### Plancherel's theorem

If $c_{0},\,c_{\pm 1},\,c_{\pm 2},\ldots$ are coefficients and ${\textstyle \sum _{n=-\infty }^{\infty }|c_{n}|^{2}<\infty }$ then there is a unique function $s\in L^{2}(P)$ such that $S[n]=c_{n}$ for every n .

### Convolution theorems

Given P -periodic functions, $s_{P}$ and $r_{P}$ with Fourier series coefficients $S[n]$ and $R[n],$ $n\in \mathbb {Z} ,$

- The pointwise product**:** $h_{P}(x)\triangleq s_{P}(x)\cdot r_{P}(x)$ is also P -periodic, and its Fourier series coefficients are given by the discrete convolution of the S and R sequences**:** $H[n]=\{S*R\}[n].$
- The periodic convolution**:** $h_{P}(x)\triangleq \int _{P}s_{P}(\tau )\cdot r_{P}(x-\tau )\,d\tau$ is also P -periodic, with Fourier series coefficients**:** $H[n]=P\cdot S[n]\cdot R[n].$
- A doubly infinite sequence $\left\{c_{n}\right\}_{n\in Z}$ in $c_{0}(\mathbb {Z} )$ is the sequence of Fourier coefficients of a function in $L^{1}([0,2\pi ])$ if and only if it is a convolution of two sequences in $\ell ^{2}(\mathbb {Z} )$ . See

### Derivative property

If s is a P -periodic function on $\mathbb {R}$ which is k times differentiable, and its $k^{\text{th}}$ derivative is continuous, then s belongs to the function space $C^{k}(\mathbb {R} )$ .

- If $s\in C^{k}(\mathbb {R} )$ , then the Fourier coefficients of the $k^{\text{th}}$ derivative of s can be expressed in terms of the Fourier coefficients ${\widehat {s}}[n]$ of s , via the formula ${\widehat {s^{(k)}}}[n]=\left(i{\frac {2\pi n}{P}}\right)^{k}{\widehat {s}}[n].$ In particular, since for any fixed $k\geq 1$ we have ${\widehat {s^{(k)}}}[n]\to 0$ as $n\to \infty$ , it follows that $|n|^{k}{\widehat {s}}[n]$ tends to zero, i.e., the Fourier coefficients converge to zero faster than the $k^{\text{th}}$ power of $|n|$ .

### Compact groups

One of the interesting properties of the Fourier transform which we have mentioned, is that it carries convolutions to pointwise products. If that is the property which we seek to preserve, one can produce Fourier series on any compact group. Typical examples include those classical groups that are compact. This generalizes the Fourier transform to all spaces of the form *L*2(*G*), where *G* is a compact group, in such a way that the Fourier transform carries convolutions to pointwise products. The Fourier series exists and converges in similar ways to the [−*π*,*π*] case.

An alternative extension to compact groups is the Peter–Weyl theorem, which proves results about representations of compact groups analogous to those about finite groups.

### Riemannian manifolds

If the domain is not a group, then there is no intrinsically defined convolution. However, if X is a compact Riemannian manifold, it has a Laplace–Beltrami operator. The Laplace–Beltrami operator is the differential operator that corresponds to Laplace operator for the Riemannian manifold X . Then, by analogy, one can consider heat equations on X . Since Fourier arrived at his basis by attempting to solve the heat equation, the natural generalization is to use the eigensolutions of the Laplace–Beltrami operator as a basis. This generalizes Fourier series to spaces of the type $L^{2}(X)$ , where X is a Riemannian manifold. The Fourier series converges in ways similar to the $[-\pi ,\pi ]$ case. A typical example is to take X to be the sphere with the usual metric, in which case the Fourier basis consists of spherical harmonics.

### Locally compact Abelian groups

The generalization to compact groups discussed above does not generalize to noncompact, nonabelian groups. However, there is a straightforward generalization to Locally Compact Abelian (LCA) groups.

This generalizes the Fourier transform to $L^{1}(G)$ or $L^{2}(G)$ , where G is an LCA group. If G is compact, one also obtains a Fourier series, which converges similarly to the $[-\pi ,\pi ]$ case, but if G is noncompact, one obtains instead a Fourier integral. This generalization yields the usual Fourier transform when the underlying locally compact Abelian group is $\mathbb {R}$ .

## Extensions

### Fourier-Stieltjes series

Formally, the Fourier-Stieltjes series can be defined as the Fourier series whose coefficients are given by $c_{n}={\hat {\mu }}(n)={\frac {1}{P}}\int _{0}^{P}\ e^{-i2\pi {\tfrac {n}{P}}x}\,d\mu (x),\quad \forall n\in \mathbb {Z} ,$ for any $\mu \in M$ , where M is the space finite Borel measures on the interval $[0,P]$ . As such, when $\mu \in M$ , the function ${\hat {\mu }}(n)$ is also referred to as a Fourier-Stieltjes transform.

This follows from an earlier and more concrete representation of a Radon measure (i.e. a locally finite Borel measure) on $\mathbb {R}$ , given by F. Riesz. That is, if F is a function of bounded variation on the interval $[0,P]$ then the Fourier coefficients can be expressed by the Riemann-Stieltjes integral $c_{n}={\frac {1}{P}}\int _{0}^{P}\ e^{-i2\pi {\tfrac {n}{P}}x}\,dF(x),\quad \forall n\in \mathbb {Z} ,$ called the *Fourier-Stieltjes coefficients* of F . As the distributional derivative of F is a Radon measure, it is subject to the Lebesgue decomposition and can be expressed as $dF=F'dx+dF_{s}$ . If $dF_{s}=0$ the expression reduces to the original definition of the Fourier coefficients, hence a Fourier series is a Fourier-Stieltjes series.

The question whether or not $\mu$ exists for a given sequence of $c_{n}$ forms the basis of the trigonometric moment problem.

The Fourier series can be generalized still further from measures to distributions. If the Fourier coefficients are determined by a distribution $F\in {\mathcal {D}}'$ then the series is sometimes described as a *Fourier-Schwartz series*.

While it is often extremely difficult to decide whether a given series is a Fourier or a Fourier-Stieltjes series, deciding whether or not it is a Fourier-Schwartz series is relatively trivial.

### Fourier series on a square

We can also define the Fourier series for functions of two variables x and y in the square $[-\pi ,\pi ]\times [-\pi ,\pi ]$ : ${\begin{aligned}f(x,y)&=\sum _{j,k\in \mathbb {Z} }c_{j,k}e^{ijx}e^{iky},\\[5pt]c_{j,k}&={\frac {1}{4\pi ^{2}}}\int _{-\pi }^{\pi }\int _{-\pi }^{\pi }f(x,y)e^{-ijx}e^{-iky}\,dx\,dy.\end{aligned}}$

Aside from being useful for solving partial differential equations such as the heat equation, one notable application of Fourier series on the square is in image compression. In particular, the JPEG image compression standard uses the two-dimensional discrete cosine transform, a discrete form of the Fourier cosine transform, which uses only cosine as the basis function.

For two-dimensional arrays with a staggered appearance, half of the Fourier series coefficients disappear, due to additional symmetry.

### Fourier series of a Bravais-lattice-periodic function

A three-dimensional Bravais lattice is defined as the set of vectors of the form $\mathbf {R} =n_{1}\mathbf {a} _{1}+n_{2}\mathbf {a} _{2}+n_{3}\mathbf {a} _{3}$ where $n_{i}$ are integers and $\mathbf {a} _{i}$ are three linearly independent but not necessarily orthogonal vectors. Let us consider some function $f(\mathbf {r} )$ with the same periodicity as the Bravais lattice, *i.e.* $f(\mathbf {r} )=f(\mathbf {R} +\mathbf {r} )$ for any lattice vector $\mathbf {R}$ . This situation frequently occurs in solid-state physics where $f(\mathbf {r} )$ might, for example, represent the effective potential that an electron "feels" inside a periodic crystal. In presence of such a periodic potential, the quantum-mechanical description of the electron results in a periodically modulated plane-wave commonly known as Bloch state.

In order to develop $f(\mathbf {r} )$ in a Fourier series, it is convenient to introduce an auxiliary function $g(x_{1},x_{2},x_{3})\triangleq f(\mathbf {r} )=f{\left(x_{1}{\frac {\mathbf {a} _{1}}{a_{1}}}+x_{2}{\frac {\mathbf {a} _{2}}{a_{2}}}+x_{3}{\frac {\mathbf {a} _{3}}{a_{3}}}\right)}.$ Both $f(\mathbf {r} )$ and $g(x_{1},x_{2},x_{3})$ contain essentially the same information. However, instead of the position vector $\mathbf {r}$ , the arguments of g are coordinates $x_{1,2,3}$ along the unit vectors $\mathbf {a} _{i}/{a_{i}}$ of the Bravais lattice, such that g is an ordinary periodic function in these variables, $g(x_{1},x_{2},x_{3})=g(x_{1}+a_{1},x_{2},x_{3})=g(x_{1},x_{2}+a_{2},x_{3})=g(x_{1},x_{2},x_{3}+a_{3})\quad \forall \;x_{1},x_{2},x_{3}.$ This trick allows us to develop g as a multi-dimensional Fourier series, in complete analogy with the square-periodic function discussed in the previous section. Its Fourier coefficients are ${\begin{aligned}c(m_{1},m_{2},m_{3})={\frac {1}{a_{3}}}\int _{0}^{a_{3}}dx_{3}{\frac {1}{a_{2}}}\int _{0}^{a_{2}}dx_{2}{\frac {1}{a_{1}}}\int _{0}^{a_{1}}dx_{1}\,g(x_{1},x_{2},x_{3})\,e^{-i2\pi \left({\tfrac {m_{1}}{a_{1}}}x_{1}+{\tfrac {m_{2}}{a_{2}}}x_{2}+{\tfrac {m_{3}}{a_{3}}}x_{3}\right)}\end{aligned}},$ where $m_{1},m_{2},m_{3}$ are all integers. $c(m_{1},m_{2},m_{3})$ plays the same role as the coefficients $c_{j,k}$ in the previous section but in order to avoid double subscripts we note them as a function.

Once we have these coefficients, the function g can be recovered via the Fourier series $g(x_{1},x_{2},x_{3})=\sum _{m_{1},m_{2},m_{3}\in \mathbb {Z} }\,c(m_{1},m_{2},m_{3})\,e^{i2\pi \left({\tfrac {m_{1}}{a_{1}}}x_{1}+{\tfrac {m_{2}}{a_{2}}}x_{2}+{\tfrac {m_{3}}{a_{3}}}x_{3}\right)}.$ We would now like to abandon the auxiliary coordinates $x_{1,2,3}$ and to return to the original position vector $\mathbf {r}$ . This can be achieved by means of the reciprocal lattice whose vectors $\mathbf {b} _{1,2,3}$ are defined such that they are orthonormal (up to a factor $2\pi$ ) to the original Bravais vectors $\mathbf {a} _{1,2,3}$ , $\mathbf {a} _{i}\cdot \mathbf {b_{j}} =2\pi \delta _{ij},$ with $\delta _{ij}$ the Kronecker delta. With this, the scalar product between a reciprocal lattice vector $\mathbf {Q}$ and an arbitrary position vector $\mathbf {r}$ written in the Bravais lattice basis becomes $\mathbf {Q} \cdot \mathbf {r} =\left(m_{1}\mathbf {b} _{1}+m_{2}\mathbf {b} _{2}+m_{3}\mathbf {b} _{3}\right)\cdot \left(x_{1}{\frac {\mathbf {a} _{1}}{a_{1}}}+x_{2}{\frac {\mathbf {a} _{2}}{a_{2}}}+x_{3}{\frac {\mathbf {a} _{3}}{a_{3}}}\right)=2\pi \left(x_{1}{\frac {m_{1}}{a_{1}}}+x_{2}{\frac {m_{2}}{a_{2}}}+x_{3}{\frac {m_{3}}{a_{3}}}\right),$ which is exactly the expression occurring in the Fourier exponents. The Fourier series for $f(\mathbf {r} )=g(x_{1},x_{2},x_{3})$ can therefore be rewritten as a sum over all the reciprocal lattice vectors $\mathbf {Q} =m_{1}\mathbf {b} _{1}+m_{2}\mathbf {b} _{2}+m_{3}\mathbf {b} _{3}$ , $f(\mathbf {r} )=\sum _{\mathbf {Q} }c(\mathbf {Q} )\,e^{i\mathbf {Q} \cdot \mathbf {r} },$ and the coefficients are $c(\mathbf {Q} )={\frac {1}{a_{3}}}\int _{0}^{a_{3}}dx_{3}\,{\frac {1}{a_{2}}}\int _{0}^{a_{2}}dx_{2}\,{\frac {1}{a_{1}}}\int _{0}^{a_{1}}dx_{1}\,f\left(x_{1}{\frac {\mathbf {a} _{1}}{a_{1}}}+x_{2}{\frac {\mathbf {a} _{2}}{a_{2}}}+x_{3}{\frac {\mathbf {a} _{3}}{a_{3}}}\right)e^{-i\mathbf {Q} \cdot \mathbf {r} }.$ The remaining task will be to convert this integral over lattice coordinates back into a volume integral. The relation between the lattice coordinates $x_{1,2,3}$ and the original cartesian coordinates $\mathbf {r} =(x,y,z)$ is a linear system of equations, $\mathbf {r} =x_{1}{\frac {\mathbf {a} _{1}}{a_{1}}}+x_{2}{\frac {\mathbf {a} _{2}}{a_{2}}}+x_{3}{\frac {\mathbf {a} _{3}}{a_{3}}},$ which, when written in matrix form, ${\begin{bmatrix}x\\y\\z\end{bmatrix}}=\mathbf {J} {\begin{bmatrix}x_{1}\\x_{2}\\x_{3}\end{bmatrix}}={\begin{bmatrix}{\frac {\mathbf {a} _{1}}{a_{1}}},{\frac {\mathbf {a} _{2}}{a_{2}}},{\frac {\mathbf {a} _{3}}{a_{3}}}\end{bmatrix}}{\begin{bmatrix}x_{1}\\x_{2}\\x_{3}\end{bmatrix}}\,,$ involves a constant matrix $\mathbf {J}$ whose columns are the unit vectors $\mathbf {a} _{j}/a_{j}$ of the Bravais lattice. When changing variables from $\mathbf {r}$ to $(x_{1},x_{2},x_{3})$ in an integral, the same matrix $\mathbf {J}$ appears as a Jacobian matrix $\mathbf {J} ={\begin{bmatrix}{\dfrac {\partial x}{\partial x_{1}}}&{\dfrac {\partial x}{\partial x_{2}}}&{\dfrac {\partial x}{\partial x_{3}}}\\[12pt]{\dfrac {\partial y}{\partial x_{1}}}&{\dfrac {\partial y}{\partial x_{2}}}&{\dfrac {\partial y}{\partial x_{3}}}\\[12pt]{\dfrac {\partial z}{\partial x_{1}}}&{\dfrac {\partial z}{\partial x_{2}}}&{\dfrac {\partial z}{\partial x_{3}}}\end{bmatrix}}\,.$

Its determinant J is therefore also constant and can be inferred from any integral over any domain; here we choose to calculate the volume of the primitive unit cell $\Gamma$ in both coordinate systems: $V_{\Gamma }=\int _{\Gamma }d^{3}r=J\int _{0}^{a_{1}}dx_{1}\int _{0}^{a_{2}}dx_{2}\int _{0}^{a_{3}}dx_{3}=J\,a_{1}a_{2}a_{3}$ The unit cell being a parallelepiped, we have $V_{\Gamma }=\mathbf {a} _{1}\cdot (\mathbf {a} _{2}\times \mathbf {a} _{3})$ and thus $d^{3}r=Jdx_{1}dx_{2}dx_{3}={\frac {\mathbf {a} _{1}\cdot (\mathbf {a} _{2}\times \mathbf {a} _{3})}{a_{1}a_{2}a_{3}}}dx_{1}dx_{2}dx_{3}.$ This allows us to write $c(\mathbf {Q} )$ as the desired volume integral over the primitive unit cell $\Gamma$ in ordinary cartesian coordinates: $c(\mathbf {Q} )={\frac {1}{\mathbf {a} _{1}\cdot (\mathbf {a} _{2}\times \mathbf {a} _{3})}}\int _{\Gamma }d^{3}r\,f(\mathbf {r} )\cdot e^{-i\mathbf {Q} \cdot \mathbf {r} }\,.$

### Hilbert space

As the trigonometric series is a special class of orthogonal system, Fourier series can naturally be defined in the context of Hilbert spaces. For example, the space of square-integrable functions on $[-\pi ,\pi ]$ forms the Hilbert space $L^{2}([-\pi ,\pi ])$ . Its inner product, defined for any two elements f and g , is given by: $\langle f,g\rangle ={\frac {1}{2\pi }}\int _{-\pi }^{\pi }f(x){\overline {g(x)}}\,dx.$ This space is equipped with the orthonormal basis $\left\{e_{n}=e^{inx}:n\in \mathbb {Z} \right\}$ . Then the (generalized) Fourier series expansion of $f\in L^{2}([-\pi ,\pi ])$ , given by $f(x)=\sum _{n=-\infty }^{\infty }c_{n}e^{inx},$ can be written as $f=\sum _{n=-\infty }^{\infty }\langle f,e_{n}\rangle \,e_{n}.$

The sine-cosine form follows in a similar fashion. Indeed, the sines and cosines form an orthogonal set: $\int _{-\pi }^{\pi }\cos(mx)\,\cos(nx)\,dx={\frac {1}{2}}\int _{-\pi }^{\pi }\cos((n-m)x)+\cos((n+m)x)\,dx=\pi \delta _{mn},\quad m,n\geq 1,$ $\int _{-\pi }^{\pi }\sin(mx)\,\sin(nx)\,dx={\frac {1}{2}}\int _{-\pi }^{\pi }\cos((n-m)x)-\cos((n+m)x)\,dx=\pi \delta _{mn},\quad m,n\geq 1$ (where *δ**mn* is the Kronecker delta), and $\int _{-\pi }^{\pi }\cos(mx)\,\sin(nx)\,dx={\frac {1}{2}}\int _{-\pi }^{\pi }\sin((n+m)x)+\sin((n-m)x)\,dx=0;$ Hence, the set $\left\{{\frac {1}{\sqrt {2}}},{\frac {\cos x}{\sqrt {2}}},{\frac {\sin x}{\sqrt {2}}},\dots ,{\frac {\cos(nx)}{\sqrt {2}}},{\frac {\sin(nx)}{\sqrt {2}}},\dots \right\},$ also forms an orthonormal basis for $L^{2}([-\pi ,\pi ])$ . The density of their span is a consequence of the Stone–Weierstrass theorem, but follows also from the properties of classical kernels like the Fejér kernel.

## Fourier theorem proving convergence of Fourier series

In engineering, the Fourier series is generally assumed to converge except at jump discontinuities since the functions encountered in engineering are usually better-behaved than those in other disciplines. In particular, if s is continuous and the derivative of $s(x)$ (which may not exist everywhere) is square integrable, then the Fourier series of s converges absolutely and uniformly to $s(x)$ . If a function is square-integrable on the interval $[x_{0},x_{0}+P]$ , then the Fourier series converges to the function almost everywhere. It is possible to define Fourier coefficients for more general functions or distributions, in which case pointwise convergence often fails, and convergence in norm or weak convergence is usually studied.

- (Four partial sums (Fourier series) of lengths 1, 2, 3, and 4 terms, showing how the approximation to a square wave improves as the number of terms increases (animation)) Four partial sums (Fourier series) of lengths 1, 2, 3, and 4 terms, showing how the approximation to a square wave improves as the number of terms increases (animation)
- (Four partial sums (Fourier series) of lengths 1, 2, 3, and 4 terms, showing how the approximation to a sawtooth wave improves as the number of terms increases (animation)) Four partial sums (Fourier series) of lengths 1, 2, 3, and 4 terms, showing how the approximation to a sawtooth wave improves as the number of terms increases (animation)
- (Example of convergence to a somewhat arbitrary function. Note the development of the "ringing" (Gibbs phenomenon) at the transitions to/from the vertical sections.) Example of convergence to a somewhat arbitrary function. Note the development of the "ringing" (Gibbs phenomenon) at the transitions to/from the vertical sections.

The theorems proving that a Fourier series is a valid representation of any periodic function (that satisfies the Dirichlet conditions), and informal variations of them that do not specify the convergence conditions, are sometimes referred to generically as *Fourier's theorem* or *the Fourier theorem*.

### Least squares property

The earlier **Eq.2**:

$s_{N}(x)=\sum _{n=-N}^{N}S[n]\ e^{i2\pi {\tfrac {n}{P}}x},$

is a trigonometric polynomial of degree N that can be generally expressed as**:**

$p_{N}(x)=\sum _{n=-N}^{N}p[n]\ e^{i2\pi {\tfrac {n}{P}}x}.$

Parseval's theorem implies that:

**Theorem**—The trigonometric polynomial $s_{N}$ is the unique best trigonometric polynomial of degree N approximating $s(x)$ , in the sense that, for any trigonometric polynomial $p_{N}\neq s_{N}$ of degree N , we have: $\|s_{N}-s\|_{2}<\|p_{N}-s\|_{2},$ where the Hilbert space norm is defined as: $\|g\|_{2}={\sqrt {{1 \over P}\int _{P}|g(x)|^{2}\,dx}}.$

### Convergence theorems

Because of the least squares property, and because of the completeness of the Fourier basis, we obtain an elementary convergence result.

**Theorem**—If s belongs to $\textstyle L^{2}(P)$ , then $s_{N}$ converges to s in $\textstyle L^{2}(P)$ as $N\to \infty$ , that is: $\lim _{N\to \infty }\|s_{N}-s\|_{2}=0.$

If s is continuously differentiable, then $(in)S[n]$ is the n th Fourier coefficient of the first derivative $s'$ . Since $s'$ is continuous, and therefore bounded, it is square-integrable and its Fourier coefficients are square-summable. Then, by the Cauchy–Schwarz inequality,

${\biggl (}\sum _{n\neq 0}{\bigl |}S[n]{\bigr |}{\biggr )}^{2}\leq \sum _{n\neq 0}{\frac {1}{n^{2}}}\cdot \sum _{n\neq 0}{\bigl |}nS[n]{\bigr |}^{2}.$

This means that s is absolutely summable. The sum of this series is a continuous function, equal to s , since the Fourier series converges in $L^{1}$ to s :

**Theorem**—If $\textstyle s\in C^{1}(\mathbb {R} )$ , then $s_{N}$ converges to s uniformly.

This result can be proven easily if s is further assumed to be $\textstyle C^{2}$ , since in that case $\textstyle n^{2}S[n]$ tends to zero as $n\rightarrow \infty$ . More generally, the Fourier series is absolutely summable, thus converges uniformly to s , provided that s satisfies a Hölder condition of order $\alpha >{\tfrac {1}{2}}$ . In the absolutely summable case, the inequality:

$\sup _{x}{\bigl |}s(x)-s_{N}(x){\bigr |}\leq \sum _{|n|>N}{\bigl |}S[n]{\bigr |}$

proves uniform convergence.

Many other results concerning the convergence of Fourier series are known, ranging from the moderately simple result that the series converges at x if s is differentiable at x , to more sophisticated results such as Carleson's theorem which states that the Fourier series of an $\textstyle L^{2}$ function converges almost everywhere.

### Divergence

Since Fourier series have such good convergence properties, many are often surprised by some of the negative results. For example, the Fourier series of a continuous *T*-periodic function need not converge pointwise. The uniform boundedness principle yields a simple non-constructive proof of this fact.

In 1922, Andrey Kolmogorov published an article titled *Une série de Fourier-Lebesgue divergente presque partout* in which he gave an example of a Lebesgue-integrable function whose Fourier series diverges almost everywhere. He later constructed an example of an integrable function whose Fourier series diverges everywhere.

It is possible to give explicit examples of a continuous function whose Fourier series diverges at 0: for instance, the even and 2π-periodic function *f* defined for all *x* in [0,π] by

$f(x)=\sum _{n=1}^{\infty }{\frac {1}{n^{2}}}\sin \left[\left(2^{n^{3}}+1\right){\frac {x}{2}}\right].$

Because the function is even the Fourier series contains only cosines:

$\sum _{m=0}^{\infty }C_{m}\cos(mx).$

The coefficients are:

$C_{m}={\frac {1}{\pi }}\sum _{n=1}^{\infty }{\frac {1}{n^{2}}}\left\{{\frac {2}{2^{n^{3}}+1-2m}}+{\frac {2}{2^{n^{3}}+1+2m}}\right\}$

As m increases, the coefficients will be positive and increasing until they reach a value of about $C_{m}\approx 2/(n^{2}\pi )$ at $m=2^{n^{3}}/2$ for some n and then become negative (starting with a value around $-2/(n^{2}\pi )$ ) and getting smaller, before starting a new such wave. At $x=0$ the Fourier series is simply the running sum of $C_{m},$ and this builds up to around

${\frac {1}{n^{2}\pi }}\sum _{k=0}^{2^{n^{3}}/2}{\frac {2}{2k+1}}\sim {\frac {1}{n^{2}\pi }}\ln 2^{n^{3}}={\frac {n}{\pi }}\ln 2$

in the nth wave before returning to around zero, showing that the series does not converge at zero but reaches higher and higher peaks. Note that though the function is continuous, it is not differentiable.
