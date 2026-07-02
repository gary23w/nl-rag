---
title: "Convolution"
source: https://en.wikipedia.org/wiki/Convolution
domain: fourier-analysis
license: CC-BY-SA-4.0
tags: fourier analysis, fourier transform, fourier series, fast fourier transform
fetched: 2026-07-02
---

# Convolution

In mathematics (in particular, functional analysis), **convolution** is a mathematical operation on two functions f and g that produces a third function $f*g$ , as the integral of the product of the two functions after one is reflected about the y-axis and shifted. The term *convolution* refers to both the resulting function and to the process of computing it. The integral is evaluated for all values of shift, producing the convolution function. The choice of which function is reflected and shifted before the integral does not change the integral result (see commutativity). Graphically, it expresses how the 'shape' of one function is modified by the other.

Some features of convolution are similar to cross-correlation: for real-valued functions, of a continuous or discrete variable, convolution $f*g$ differs from cross-correlation $f\star g$ only in that either $f(x)$ or $g(x)$ is reflected about the y-axis in convolution; thus it is a cross-correlation of $g(-x)$ and $f(x)$ , or $f(-x)$ and $g(x)$ . For complex-valued functions, the cross-correlation operator is the adjoint of the convolution operator.

Convolution has applications that include probability, statistics, acoustics, spectroscopy, signal processing and image processing, computer vision and human vision, geophysics, engineering, physics, and differential equations.

The convolution can be defined for functions on Euclidean space and other groups (as algebraic structures). For example, periodic functions, such as the discrete-time Fourier transform, can be defined on a circle and convolved by periodic convolution. (See row 18 at DTFT § Properties.) A *discrete convolution* can be defined for functions on the set of integers.

Generalizations of convolution have applications in the field of numerical analysis and numerical linear algebra, and in the design and implementation of finite impulse response filters in signal processing.

Computing the inverse of the convolution operation is known as deconvolution.

## Definition

The convolution of f and g is written $f*g$ , denoting the operator with the symbol * . It is defined as the integral of the product of the two functions after one is reflected about the y-axis and shifted. As such, it is a particular kind of integral transform:

$(f*g)(t):=\int _{-\infty }^{\infty }f(\tau )g(t-\tau )\,d\tau .$

An equivalent definition is (see commutativity):

$(f*g)(t):=\int _{-\infty }^{\infty }f(t-\tau )g(\tau )\,d\tau .$

While the symbol t is used above, it need not represent the time domain. At each t , the convolution formula can be described as the area under the function $f(\tau )$ weighted by the function $g(-\tau )$ shifted by the amount t . As t changes, the weighting function $g(t-\tau )$ emphasizes different parts of the input function $f(\tau )$ ; If t is a positive value, then $g(t-\tau )$ is equal to $g(-\tau )$ that slides or is shifted along the $\tau$ -axis toward the right (toward $+\infty$ ) by the amount of t , while if t is a negative value, then $g(t-\tau )$ is equal to $g(-\tau )$ that slides or is shifted toward the left (toward $-\infty$ ) by the amount of $|t|$ .

For functions f , g supported on only $[0,\infty )$ (i.e., zero for negative arguments), the integration limits can be truncated, resulting in:

$(f*g)(t)=\int _{0}^{t}f(\tau )g(t-\tau )\,d\tau \quad \ {\text{for }}f,g:[0,\infty )\to \mathbb {R} .$

For the multi-dimensional formulation of convolution, see *domain of definition* (below).

### Notation

A common engineering notational convention is:

$f(t)*g(t)\mathrel {:=} \underbrace {\int _{-\infty }^{\infty }f(\tau )g(t-\tau )\,d\tau } _{(f*g)(t)},$

which has to be interpreted carefully to avoid confusion. For instance, $f(t)*g(t-t_{0})$ is equivalent to $(f*g)(t-t_{0})$ , but $f(t-t_{0})*g(t-t_{0})$ is in fact equivalent to $(f*g)(t-2t_{0})$ .

### Relations with other transforms

Given two functions $f(t)$ and $g(t)$ with bilateral Laplace transforms (two-sided Laplace transform)

$F(s)=\int _{-\infty }^{\infty }e^{-su}\ f(u)\ {\text{d}}u$

and

$G(s)=\int _{-\infty }^{\infty }e^{-sv}\ g(v)\ {\text{d}}v$

respectively, the convolution operation $(f*g)(t)$ can be defined as the inverse Laplace transform of the product of $F(s)$ and $G(s)$ . More precisely,

${\begin{aligned}F(s)\cdot G(s)&=\int _{-\infty }^{\infty }e^{-su}\ f(u)\ {\text{d}}u\cdot \int _{-\infty }^{\infty }e^{-sv}\ g(v)\ {\text{d}}v\\&=\int _{-\infty }^{\infty }\int _{-\infty }^{\infty }e^{-s(u+v)}\ f(u)\ g(v)\ {\text{d}}u\ {\text{d}}v\end{aligned}}$

Let $t=u+v$ , then

${\begin{aligned}F(s)\cdot G(s)&=\int _{-\infty }^{\infty }\int _{-\infty }^{\infty }e^{-st}\ f(u)\ g(t-u)\ {\text{d}}u\ {\text{d}}t\\&=\int _{-\infty }^{\infty }e^{-st}\underbrace {\int _{-\infty }^{\infty }f(u)\ g(t-u)\ {\text{d}}u} _{(f*g)(t)}\ {\text{d}}t\\&=\int _{-\infty }^{\infty }e^{-st}(f*g)(t)\ {\text{d}}t.\end{aligned}}$

Note that $F(s)\cdot G(s)$ is the bilateral Laplace transform of $(f*g)(t)$ . A similar derivation can be done using the unilateral Laplace transform (one-sided Laplace transform).

The convolution operation also describes the output (in terms of the input) of an important class of operations known as *linear time-invariant* (LTI). See LTI system theory for a derivation of convolution as the result of LTI constraints. In terms of the Fourier transforms of the input and output of an LTI operation, no new frequency components are created. The existing ones are only modified (amplitude and/or phase). In other words, the output transform is the pointwise product of the input transform with a third transform (known as a transfer function). See Convolution theorem for a derivation of that property of convolution. Conversely, convolution can be derived as the inverse Fourier transform of the pointwise product of two Fourier transforms.

## Visual explanation

| Express each function in terms of a dummy variable $\tau .$ Reflect one of the functions: $g(\tau )$ → $g(-\tau ).$ Add an offset of the independent variable, t , which allows $g(-\tau )$ to slide along the $\tau$ -axis. If t is a positive value, then $g(t-\tau )$ is equal to $g(-\tau )$ that slides or is shifted along the $\tau$ -axis toward the right (toward $+\infty$ ) by the amount of t . If t is a negative value, then $g(t-\tau )$ is equal to $g(-\tau )$ that slides or is shifted toward the left (toward $-\infty$ ) by the amount of $\|t\|$ .Start t at $-\infty$ and slide it all the way to $+\infty$ . Wherever the two functions intersect, find the integral of their product. In other words, at time t , compute the area under the function $f(\tau )$ weighted by the weighting function $g(t-\tau ).$ The resulting waveform (not shown here) is the convolution of functions f and g . If $f(t)$ is a unit impulse, the result of this process is simply $g(t)$ . Formally: $\int _{-\infty }^{\infty }\delta (\tau )g(t-\tau )\,d\tau =g(t)$ |   |
|---|---|
| In this example, the red-colored "pulse", $\ g(\tau ),$ is an even function $(\ g(-\tau )=g(\tau )\ ),$ so convolution is equivalent to correlation. A snapshot of this "movie" shows functions $g(t-\tau )$ and $f(\tau )$ (in blue) for some value of parameter $t,$ which is arbitrarily defined as the distance along the $\tau$ axis from the point $\tau =0$ to the center of the red pulse. The amount of yellow is the area of the product $f(\tau )\cdot g(t-\tau ),$ computed by the convolution/correlation integral. The movie is created by continuously changing t and recomputing the integral. The result (shown in black) is a function of $t,$ but is plotted on the same axis as $\tau ,$ for convenience and comparison. |   |
| In this depiction, $f(\tau )$ could represent the response of a resistor-capacitor circuit to a narrow pulse that occurs at $\tau =0.$ In other words, if $g(\tau )=\delta (\tau ),$ the result of convolution is just $f(t).$ But when $g(\tau )$ is the wider pulse (in red), the response is a "smeared" version of $f(t).$ It begins at $t=-0.5,$ because we defined t as the distance from the $\tau =0$ axis to the *center* of the wide pulse (instead of the leading edge). |   |

## Historical developments

One of the earliest uses of the convolution integral appeared in D'Alembert's derivation of Taylor's theorem in *Recherches sur différents points importants du système du monde,* published in 1754.

Also, an expression of the type:

$\int f(u)\cdot g(x-u)\,du$

is used by Sylvestre François Lacroix on page 505 of his book entitled *Treatise on differences and series*, which is the last of 3 volumes of the encyclopedic series: *Traité du calcul différentiel et du calcul intégral*, Chez Courcier, Paris, 1797–1800. Soon thereafter, convolution operations appear in the works of Pierre Simon Laplace, Jean-Baptiste Joseph Fourier, Siméon Denis Poisson, and others. The term itself did not come into wide use until the 1950s or 1960s. Prior to that it was sometimes known as *Faltung* (which means *folding* in German), *composition product*, *superposition integral*, and *Carson's integral*. Yet it appears as early as 1903, though the definition is rather unfamiliar in older uses.

The operation:

$\int _{0}^{t}\varphi (s)\psi (t-s)\,ds,\quad 0\leq t<\infty ,$

is a particular case of composition products considered by the Italian mathematician Vito Volterra in 1913.

## Circular convolution

When a function $g_{T}$ is periodic, with period T , then for functions, f , such that $f*g_{T}$ exists, the convolution is also periodic and identical to:

$(f*g_{T})(t)\equiv \int _{t_{0}}^{t_{0}+T}\left[\sum _{k=-\infty }^{\infty }f(\tau +kT)\right]g_{T}(t-\tau )\,d\tau ,$

where $t_{0}$ is an arbitrary choice. The summation is called a periodic summation of the function f .

When $g_{T}$ is a periodic summation of another function, g , then $f*g_{T}$ is known as a *circular* or *cyclic* convolution of f and g .

And if the periodic summation above is replaced by $f_{T}$ , the operation is called a *periodic* convolution of $f_{T}$ and $g_{T}$ .

## Discrete convolution

For complex-valued functions f and g defined on the set $\mathbb {Z}$ of integers, the *discrete convolution* of f and g is given by:

$(f*g)[n]=\sum _{m=-\infty }^{\infty }f[m]g[n-m],$

or equivalently (see commutativity) by:

$(f*g)[n]=\sum _{m=-\infty }^{\infty }f[n-m]g[m].$

The convolution of two finite sequences is defined by extending the sequences to finitely supported functions on the set of integers. When the sequences are the coefficients of two polynomials, then the coefficients of the ordinary product of the two polynomials are the convolution of the original two sequences. This is known as the Cauchy product of the coefficients of the sequences.

Thus, when g is non-zero over a finite interval [−*m*,+*m*] (representing, for instance, a finite impulse response), a finite summation may be used:

$(f*g)[n]=\sum _{m=-M}^{M}f[n-m]g[m].$

### Circular discrete convolution

When a function $g_{_{N}}$ is periodic, with period $N,$ then for functions, $f,$ such that $f*g_{_{N}}$ exists, the convolution is also periodic and identical to**:**

$(f*g_{_{N}})[n]\equiv \sum _{m=0}^{N-1}\left(\sum _{k=-\infty }^{\infty }{f}[m+kN]\right)g_{_{N}}[n-m].$

The summation on k is called a periodic summation of the function $f.$

If $g_{_{N}}$ is a periodic summation of another function, $g,$ then $f*g_{_{N}}$ is known as a circular convolution of f and $g.$

When the non-zero durations of both f and g are limited to the interval $[0,N-1],$   $f*g_{_{N}}$ reduces to these common forms**:**

| ${\begin{aligned}\left(f*g_{N}\right)[n]&=\sum _{m=0}^{N-1}f[m]g_{N}[n-m]\\&=\sum _{m=0}^{n}f[m]g[n-m]+\sum _{m=n+1}^{N-1}f[m]g[N+n-m]\\[2pt]&=\sum _{m=0}^{N-1}f[m]g[(n-m)_{\bmod {N}}]\\[2pt]&\triangleq \left(f*_{N}g\right)[n]\end{aligned}}$ |   | Eq.1 |
|---|---|---|

The notation $f*_{N}g$ for *cyclic convolution* denotes convolution over the cyclic group of integers modulo *N*.

Circular convolution arises most often in the context of fast convolution with a fast Fourier transform (FFT) algorithm.

### Fast convolution algorithms

In many situations, discrete convolutions can be converted to circular convolutions so that fast transforms with a convolution property can be used to implement the computation. For example, convolution of digit sequences is the kernel operation in multiplication of multi-digit numbers, which can therefore be efficiently implemented with transform techniques (Knuth 1997, §4.3.3.C; von zur Gathen & Gerhard 2003, §8.2).

**Eq.1** requires N arithmetic operations per output value and *N*2 operations for N outputs. That can be significantly reduced with any of several fast algorithms. Digital signal processing and other applications typically use fast convolution algorithms to reduce the cost of the convolution to O(N log N) complexity.

The most common fast convolution algorithms use fast Fourier transform (FFT) algorithms via the circular convolution theorem. Specifically, the circular convolution of two finite-length sequences is found by taking an FFT of each sequence, multiplying pointwise, and then performing an inverse FFT. Convolutions of the type defined above are then efficiently implemented using that technique in conjunction with zero-extension and/or discarding portions of the output. Other fast convolution algorithms, such as the Schönhage–Strassen algorithm or the Mersenne transform, use fast Fourier transforms in other rings. The Winograd method is used as an alternative to the FFT. It significantly speeds up 1D, 2D, and 3D convolution.

If one sequence is much longer than the other, zero-extension of the shorter sequence and fast circular convolution is not the most computationally efficient method available. Instead, decomposing the longer sequence into blocks and convolving each block allows for faster algorithms such as the overlap–save method and overlap–add method. A hybrid convolution method that combines block and FIR algorithms allows for a zero input-output latency that is useful for real-time convolution computations.

## Domain of definition

The convolution of two complex-valued functions on **R***d* is itself a complex-valued function on **R***d*, defined by:

$(f*g)(x)=\int _{\mathbf {R} ^{d}}f(y)g(x-y)\,dy=\int _{\mathbf {R} ^{d}}f(x-y)g(y)\,dy,$

and is well-defined only if f and g decay sufficiently rapidly at infinity in order for the integral to exist. Conditions for the existence of the convolution may be tricky, since a blow-up in g at infinity can be easily offset by sufficiently rapid decay in f. The question of existence thus may involve different conditions on f and g:

### Compactly supported functions

If f and g are compactly supported continuous functions, then their convolution exists, and is also compactly supported and continuous (Hörmander 1983, Chapter 1). More generally, if either function (say f) is compactly supported and the other is locally integrable, then the convolution *f*∗*g* is well-defined and continuous.

Convolution of f and g is also well defined when both functions are locally square integrable on **R** and supported on an interval of the form [*a*, +∞) (or both supported on [−∞, *a*]).

### Integrable functions

The convolution of f and g exists if f and g are both Lebesgue integrable functions in *L*1(**R***d*), and in this case *f*∗*g* is also integrable (Stein & Weiss 1971, Theorem 1.3). This is a consequence of Tonelli's theorem. This is also true for functions in *L*1, under the discrete convolution, or more generally for the convolution on any group.

Likewise, if *f* ∈ *L*1(**R***d*)  and  *g* ∈ *L**p*(**R***d*)  where 1 ≤ *p* ≤ ∞, then  *f***g* ∈ *L**p*(**R***d*), and

$\|{f}*g\|_{p}\leq \|f\|_{1}\|g\|_{p}.$

In the particular case *p* = 1, this shows that *L*1 is a Banach algebra under the convolution (and equality of the two sides holds if f and g are non-negative almost everywhere).

More generally, Young's inequality implies that the convolution is a continuous bilinear map between suitable *L**p* spaces. Specifically, if 1 ≤ *p*, *q*, *r* ≤ ∞ satisfy:

${\frac {1}{p}}+{\frac {1}{q}}={\frac {1}{r}}+1,$

then

$\left\Vert f*g\right\Vert _{r}\leq \left\Vert f\right\Vert _{p}\left\Vert g\right\Vert _{q},\quad f\in L^{p},\ g\in L^{q},$

so that the convolution is a continuous bilinear mapping from *L**p*×*L**q* to *L**r*. The Young inequality for convolution is also true in other contexts (circle group, convolution on **Z**). The preceding inequality is not sharp on the real line: when 1 < *p*, *q*, *r* < ∞, there exists a constant *B**p*,*q* < 1 such that:

$\left\Vert f*g\right\Vert _{r}\leq B_{p,q}\left\Vert f\right\Vert _{p}\left\Vert g\right\Vert _{q},\quad f\in L^{p},\ g\in L^{q}.$

The optimal value of *B**p*,*q* was discovered in 1975 and independently in 1976, see Brascamp–Lieb inequality.

A stronger estimate is true provided 1 < *p*, *q*, *r* < ∞:

$\|f*g\|_{r}\leq C_{p,q}\|f\|_{p}\|g\|_{q,w}$

where $\|g\|_{q,w}$ is the weak *L**q* norm. Convolution also defines a bilinear continuous map $L^{p,w}\times L^{q,w}\to L^{r,w}$ for $1<p,q,r<\infty$ , owing to the weak Young inequality:

$\|f*g\|_{r,w}\leq C_{p,q}\|f\|_{p,w}\|g\|_{r,w}.$

### Functions of rapid decay

In addition to compactly supported functions and integrable functions, functions that have sufficiently rapid decay at infinity can also be convolved. An important feature of the convolution is that if *f* and *g* both decay rapidly, then *f*∗*g* also decays rapidly. In particular, if *f* and *g* are rapidly decreasing functions, then so is the convolution *f*∗*g*. Combined with the fact that convolution commutes with differentiation (see #Properties), it follows that the class of Schwartz functions is closed under convolution (Stein & Weiss 1971, Theorem 3.3).

### Distributions

If *f* is a smooth function that is compactly supported and *g* is a distribution, then *f*∗*g* is a smooth function defined by

$\int _{\mathbb {R} ^{d}}{f}(y)g(x-y)\,dy=(f*g)(x)\in C^{\infty }(\mathbb {R} ^{d}).$

More generally, it is possible to extend the definition of the convolution in a unique way with $\varphi$ the same as *f* above, so that the associative law

$f*(g*\varphi )=(f*g)*\varphi$

remains valid in the case where *f* is a distribution, and *g* a compactly supported distribution (Hörmander 1983, §4.2).

### Measures

The convolution of any two Borel measures *μ* and *ν* of bounded variation is the measure $\mu *\nu$ defined by (Rudin 1962)

$\int _{\mathbf {R} ^{d}}f(x)\,d(\mu *\nu )(x)=\int _{\mathbf {R} ^{d}}\int _{\mathbf {R} ^{d}}f(x+y)\,d\mu (x)\,d\nu (y).$

In particular,

$(\mu *\nu )(A)=\int _{\mathbf {R} ^{d}\times \mathbf {R} ^{d}}1_{A}(x+y)\,d(\mu \times \nu )(x,y),$

where $A\subset \mathbf {R} ^{d}$ is a measurable set and $1_{A}$ is the indicator function of A .

This agrees with the convolution defined above when μ and ν are regarded as distributions, as well as the convolution of L1 functions when μ and ν are absolutely continuous with respect to the Lebesgue measure.

The convolution of measures also satisfies the following version of Young's inequality

$\|\mu *\nu \|\leq \|\mu \|\|\nu \|$

where the norm is the total variation of a measure. Because the space of measures of bounded variation is a Banach space, convolution of measures can be treated with standard methods of functional analysis that may not apply for the convolution of distributions.

## Properties

### Algebraic properties

The convolution defines a product on the linear space of integrable functions. This product satisfies the following algebraic properties, which formally mean that the space of integrable functions with the product given by convolution is a commutative associative algebra without identity (Strichartz 1994, §3.3). Other linear spaces of functions, such as the space of continuous functions of compact support, are closed under the convolution, and so also form commutative associative algebras.

**Commutativity**

$f*g=g*f$

Proof: By definition:

$(f*g)(t)=\int _{-\infty }^{\infty }f(\tau )g(t-\tau )\,d\tau$

Changing the variable of integration to

$u=t-\tau$

the result follows.

**Associativity**

$f*(g*h)=(f*g)*h$

Proof: This follows from using

Fubini's theorem

(i.e., double integrals can be evaluated as iterated integrals in either order).

**Distributivity**

$f*(g+h)=(f*g)+(f*h)$

Proof: This follows from linearity of the integral.

**Associativity with scalar multiplication**

$a(f*g)=(af)*g$

for any real (or complex) number

a

.

**Multiplicative identity**

No algebra of functions possesses an identity for the convolution. The lack of identity is typically not a major inconvenience, since most collections of functions on which the convolution is performed can be convolved with a

delta distribution

(a unitary impulse, centered at zero) or, at the very least (as is the case of

L

1

) admit

approximations to the identity

. The linear space of compactly supported distributions does, however, admit an identity under the convolution. Specifically,

$f*\delta =f$

where

δ

is the delta distribution.

**Inverse element**

Some distributions

S

have an

inverse element

S

−1

for the convolution which then must satisfy

$S^{-1}*S=\delta$

from which an explicit formula for

S

−1

may be obtained.

The set of invertible distributions forms an

abelian group

under the convolution.

**Complex conjugation**

${\overline {f*g}}={\overline {f}}*{\overline {g}}$

**Time reversal**

If

$q(t)=r(t)*s(t),$

then

$q(-t)=r(-t)*s(-t).$

> Proof (using convolution theorem):
> 
> $q(t)\ {\stackrel {\mathcal {F}}{\Longleftrightarrow }}\ \ Q(f)=R(f)S(f)$
> 
> $q(-t)\ {\stackrel {\mathcal {F}}{\Longleftrightarrow }}\ \ Q(-f)=R(-f)S(-f)$
> 
> ${\begin{aligned}q(-t)&={\mathcal {F}}^{-1}{\bigg \{}R(-f)S(-f){\bigg \}}\\&={\mathcal {F}}^{-1}{\bigg \{}R(-f){\bigg \}}*{\mathcal {F}}^{-1}{\bigg \{}S(-f){\bigg \}}\\&=r(-t)*s(-t)\end{aligned}}$

**Relationship with differentiation**

$(f*g)'=f'*g=f*g'$

Proof:

${\begin{aligned}(f*g)'&={\frac {d}{dt}}\int _{-\infty }^{\infty }f(\tau )g(t-\tau )\,d\tau \\&=\int _{-\infty }^{\infty }f(\tau ){\frac {\partial }{\partial t}}g(t-\tau )\,d\tau \\&=\int _{-\infty }^{\infty }f(\tau )g'(t-\tau )\,d\tau =f*g'.\end{aligned}}$

**Relationship with integration**

If

${\textstyle F(t)=\int _{-\infty }^{t}f(\tau )d\tau ,}$

and

${\textstyle G(t)=\int _{-\infty }^{t}g(\tau )\,d\tau ,}$

then

$(F*g)(t)=(f*G)(t)=\int _{-\infty }^{t}(f*g)(\tau )\,d\tau .$

### Integration

If *f* and *g* are integrable functions, then the integral of their convolution on the whole space is simply obtained as the product of their integrals:

$\int _{\mathbf {R} ^{d}}(f*g)(x)\,dx=\left(\int _{\mathbf {R} ^{d}}f(x)\,dx\right)\left(\int _{\mathbf {R} ^{d}}g(x)\,dx\right).$

This follows from Fubini's theorem. The same result holds if *f* and *g* are only assumed to be nonnegative measurable functions, by Tonelli's theorem.

### Differentiation

In the one-variable case,

${\frac {d}{dx}}(f*g)={\frac {df}{dx}}*g=f*{\frac {dg}{dx}}$

where ${\frac {d}{dx}}$ is the derivative. More generally, in the case of functions of several variables, an analogous formula holds with the partial derivative:

${\frac {\partial }{\partial x_{i}}}(f*g)={\frac {\partial f}{\partial x_{i}}}*g=f*{\frac {\partial g}{\partial x_{i}}}.$

A particular consequence of this is that the convolution can be viewed as a "smoothing" operation: the convolution of *f* and *g* is differentiable as many times as *f* and *g* are in total.

These identities hold for example under the condition that *f* and *g* are absolutely integrable and at least one of them has an absolutely integrable (L1) weak derivative, as a consequence of Young's convolution inequality. For instance, when *f* is continuously differentiable with compact support, and *g* is an arbitrary locally integrable function,

${\frac {d}{dx}}(f*g)={\frac {df}{dx}}*g.$

These identities also hold much more broadly in the sense of tempered distributions if one of *f* or *g* is a rapidly decreasing tempered distribution, a compactly supported tempered distribution or a Schwartz function and the other is a tempered distribution. On the other hand, two positive integrable and infinitely differentiable functions may have a nowhere continuous convolution.

In the discrete case, the difference operator *D* *f*(*n*) = *f*(*n* + 1) − *f*(*n*) satisfies an analogous relationship:

$D(f*g)=(Df)*g=f*(Dg).$

### Convolution theorem

The convolution theorem states that

${\mathcal {F}}\{f*g\}={\mathcal {F}}\{f\}\cdot {\mathcal {F}}\{g\}$

where ${\mathcal {F}}\{f\}$ denotes the Fourier transform of f .

#### Convolution in other types of transformations

Versions of this theorem also hold for the Laplace transform, two-sided Laplace transform, Z-transform and Mellin transform.

#### Convolution on matrices

If ${\mathcal {W}}$ is the Fourier transform matrix, then

${\mathcal {W}}\left(C^{(1)}x\ast C^{(2)}y\right)=\left({\mathcal {W}}C^{(1)}\bullet {\mathcal {W}}C^{(2)}\right)(x\otimes y)={\mathcal {W}}C^{(1)}x\circ {\mathcal {W}}C^{(2)}y$

,

where $\bullet$ is face-splitting product, $\otimes$ denotes Kronecker product, $\circ$ denotes Hadamard product (this result is an evolving of count sketch properties).

This can be generalized for appropriate matrices $\mathbf {A} ,\mathbf {B}$ :

${\mathcal {W}}\left((\mathbf {A} x)\ast (\mathbf {B} y)\right)=\left(({\mathcal {W}}\mathbf {A} )\bullet ({\mathcal {W}}\mathbf {B} )\right)(x\otimes y)=({\mathcal {W}}\mathbf {A} x)\circ ({\mathcal {W}}\mathbf {B} y)$

from the properties of the face-splitting product.

### Translational equivariance

The convolution commutes with translations, meaning that

$\tau _{x}(f*g)=(\tau _{x}f)*g=f*(\tau _{x}g)$

where τ*x*f is the translation of the function *f* by *x* defined by

$(\tau _{x}f)(y)=f(y-x).$

If *f* is a Schwartz function, then *τxf* is the convolution with a translated Dirac delta function *τ**x**f* = *f* ∗ *τ**x* *δ*. So translation invariance of the convolution of Schwartz functions is a consequence of the associativity of convolution.

Furthermore, under certain conditions, convolution is the most general translation invariant operation. Informally speaking, the following holds

Suppose that

S

is a bounded

linear operator

acting on functions which commutes with translations:

S

(

τ

x

f

) =

τ

x

(

Sf

) for all

x

. Then

S

is given as convolution with a function (or distribution)

g

S

; that is

Sf

=

g

S

∗

f

.

Thus some translation invariant operations can be represented as convolution. Convolutions play an important role in the study of time-invariant systems, and especially LTI system theory. The representing function *g**S* is the impulse response of the transformation *S*.

A more precise version of the theorem quoted above requires specifying the class of functions on which the convolution is defined, and also requires assuming in addition that *S* must be a continuous linear operator with respect to the appropriate topology. It is known, for instance, that every continuous translation invariant continuous linear operator on *L*1 is the convolution with a finite Borel measure. More generally, every continuous translation invariant continuous linear operator on *L**p* for 1 ≤ *p* < ∞ is the convolution with a tempered distribution whose Fourier transform is bounded. To wit, they are all given by bounded Fourier multipliers.

## Convolutions on groups

If *G* is a suitable group endowed with a measure λ, and if *f* and *g* are real or complex valued integrable functions on *G*, then we can define their convolution by

$(f*g)(x)=\int _{G}f(y)g\left(y^{-1}x\right)\,d\lambda (y).$

It is not commutative in general. In typical cases of interest *G* is a locally compact Hausdorff topological group and λ is a (left-) Haar measure. In that case, unless *G* is unimodular, the convolution defined in this way is not the same as ${\textstyle \int f\left(xy^{-1}\right)g(y)\,d\lambda (y)}$ . The preference of one over the other is made so that convolution with a fixed function *g* commutes with left translation in the group:

$L_{h}(f*g)=(L_{h}f)*g.$

Furthermore, the convention is also required for consistency with the definition of the convolution of measures given below. However, with a right instead of a left Haar measure, the latter integral is preferred over the former.

On locally compact abelian groups, a version of the convolution theorem holds: the Fourier transform of a convolution is the pointwise product of the Fourier transforms. The circle group **T** with the Lebesgue measure is an immediate example. For a fixed *g* in *L*1(**T**), we have the following familiar operator acting on the Hilbert space *L*2(**T**):

$T{f}(x)={\frac {1}{2\pi }}\int _{\mathbf {T} }{f}(y)g(x-y)\,dy.$

The operator *T* is compact. A direct calculation shows that its adjoint *T** is convolution with

${\bar {g}}(-y).$

By the commutativity property cited above, *T* is normal: *T** *T* = *TT** . Also, *T* commutes with the translation operators. Consider the family *S* of operators consisting of all such convolutions and the translation operators. Then *S* is a commuting family of normal operators. According to spectral theory, there exists an orthonormal basis {*hk*} that simultaneously diagonalizes *S*. This characterizes convolutions on the circle. Specifically, we have

$h_{k}(x)=e^{ikx},\quad k\in \mathbb {Z} ,\;$

which are precisely the characters of **T**. Each convolution is a compact multiplication operator in this basis. This can be viewed as a version of the convolution theorem discussed above.

A discrete example is a finite cyclic group of order *n*. Convolution operators are here represented by circulant matrices, and can be diagonalized by the discrete Fourier transform.

A similar result holds for compact groups (not necessarily abelian): the matrix coefficients of finite-dimensional unitary representations form an orthonormal basis in *L*2 by the Peter–Weyl theorem, and an analog of the convolution theorem continues to hold, along with many other aspects of harmonic analysis that depend on the Fourier transform.

## Convolution of measures

Let *G* be a (multiplicatively written) topological group. If μ and ν are Radon measures on *G*, then their convolution *μ*∗*ν* is defined as the pushforward measure of the group action and can be written as

$(\mu *\nu )(E)=\iint 1_{E}(xy)\,d\mu (x)\,d\nu (y)$

for each measurable subset *E* of *G*. The convolution is also a Radon measure, whose total variation satisfies

$\|\mu *\nu \|\leq \left\|\mu \right\|\left\|\nu \right\|.$

In the case when *G* is locally compact with (left-)Haar measure λ, and μ and ν are absolutely continuous with respect to a λ, so that each has a density function, then the convolution μ∗ν is also absolutely continuous, and its density function is just the convolution of the two separate density functions. In fact, if *either* measure is absolutely continuous with respect to the Haar measure, then so is their convolution.

If μ and ν are probability measures on the topological group (**R**,+), then the convolution *μ*∗*ν* is the probability distribution of the sum *X* + *Y* of two independent random variables *X* and *Y* whose respective distributions are μ and ν.

## Infimal convolution

In convex analysis, the **infimal convolution** of proper (not identically $+\infty$ ) convex functions $f_{1},\dots ,f_{m}$ on $\mathbb {R} ^{n}$ is defined by: $(f_{1}*\cdots *f_{m})(x)=\inf _{x}\{f_{1}(x_{1})+\cdots +f_{m}(x_{m})|x_{1}+\cdots +x_{m}=x\}.$ It can be shown that the infimal convolution of convex functions is convex. Furthermore, it satisfies an identity analogous to that of the Fourier transform of a traditional convolution, with the role of the Fourier transform is played instead by the Legendre transform: $\varphi ^{*}(x)=\sup _{y}(x\cdot y-\varphi (y)).$ We have: $(f_{1}*\cdots *f_{m})^{*}(x)=f_{1}^{*}(x)+\cdots +f_{m}^{*}(x).$

## Bialgebras

Let (*X*, Δ, ∇, *ε*, *η*) be a bialgebra with comultiplication Δ, multiplication ∇, unit η, and counit *ε*. The convolution is a product defined on the endomorphism algebra End(*X*) as follows. Let *φ*, *ψ* ∈ End(*X*), that is, *φ*, *ψ*: *X* → *X* are functions that respect all algebraic structure of *X*, then the convolution *φ*∗*ψ* is defined as the composition

$X\mathrel {\xrightarrow {\Delta } } X\otimes X\mathrel {\xrightarrow {\phi \otimes \psi } } X\otimes X\mathrel {\xrightarrow {\nabla } } X.$

The convolution appears notably in the definition of Hopf algebras (Kassel 1995, §III.3). A bialgebra is a Hopf algebra if and only if it has an antipode: an endomorphism *S* such that

$S*\operatorname {id} _{X}=\operatorname {id} _{X}*S=\eta \circ \varepsilon .$

## Applications

Convolution and related operations are found in many applications in science, engineering and mathematics.

- Convolutional neural networks apply multiple cascaded *convolution* kernels with applications in machine vision and artificial intelligence. Though these are actually **cross-correlations** rather than convolutions.
- In non-neural-network-based image processing
  - In digital image processing convolutional filtering plays an important role in many important algorithms in edge detection and related processes (see Kernel (image processing))
  - In optics, an out-of-focus photograph is a convolution of the sharp image with a lens function. The photographic term for this is bokeh.
  - In image processing applications such as adding blurring.
- In digital data processing
  - In analytical chemistry, Savitzky–Golay smoothing filters are used for the analysis of spectroscopic data. They can improve signal-to-noise ratio with minimal distortion of the spectra
  - In statistics, a weighted moving average is a convolution.
- In acoustics, reverberation is the convolution of the original sound with echoes from objects surrounding the sound source.
  - In digital signal processing, convolution is used to map the impulse response of a real room on a digital audio signal.
  - In electronic music convolution is the imposition of a spectral or rhythmic structure on a sound. Often this envelope or structure is taken from another sound. The convolution of two signals is the filtering of one through the other.
- In electrical engineering, the convolution of one function (the input signal) with a second function (the impulse response) gives the output of a linear time-invariant system (LTI). At any given moment, the output is an accumulated effect of all the prior values of the input function, with the most recent values typically having the most influence (expressed as a multiplicative factor). The impulse response function provides that factor as a function of the elapsed time since each input value occurred.
- In physics, wherever there is a linear system with a "superposition principle", a convolution operation makes an appearance. For instance, in spectroscopy line broadening due to the Doppler effect on its own gives a Gaussian spectral line shape and collision broadening alone gives a Lorentzian line shape. When both effects are operative, the line shape is a convolution of Gaussian and Lorentzian, a Voigt function.
  - In time-resolved fluorescence spectroscopy, the excitation signal can be treated as a chain of delta pulses, and the measured fluorescence is a sum of exponential decays from each delta pulse.
  - In computational fluid dynamics, the large eddy simulation (LES) turbulence model uses the convolution operation to lower the range of length scales necessary in computation thereby reducing computational cost.
- In probability theory, the probability distribution of the sum of two independent random variables is the convolution of their individual distributions.
  - In kernel density estimation, a distribution is estimated from sample points by convolution with a kernel, such as an isotropic Gaussian.
- In radiotherapy treatment planning systems, most part of all modern codes of calculation applies a convolution-superposition algorithm.
- In structural reliability, the reliability index can be defined based on the convolution theorem.
  - The definition of reliability index for limit state functions with nonnormal distributions can be established corresponding to the joint distribution function. In fact, the joint distribution function can be obtained using the convolution theory.
- In Smoothed-particle hydrodynamics, simulations of fluid dynamics are calculated using particles, each with surrounding kernels. For any given particle i , some physical quantity $A_{i}$ is calculated as a convolution of $A_{j}$ with a weighting function, where j denotes the neighbors of particle i : those that are located within its kernel. The convolution is approximated as a summation over each neighbor.
- In Fractional calculus convolution is instrumental in various definitions of fractional integral and fractional derivative.
