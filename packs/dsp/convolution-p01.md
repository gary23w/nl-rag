---
title: "Convolution (part 1/2)"
source: https://en.wikipedia.org/wiki/Convolution
domain: dsp
license: CC-BY-SA-4.0
tags: dsp, digital signal processing, fft, fourier transform, digital filter, sampling rate
fetched: 2026-07-02
part: 1/2
---

# Convolution

In mathematics (in particular, functional analysis), **convolution** is a mathematical operation on two functions f {\displaystyle f} ({\displaystyle f}) and g {\displaystyle g} ({\displaystyle g}) that produces a third function f ∗ g {\displaystyle f*g} ({\displaystyle f*g}), as the integral of the product of the two functions after one is reflected about the y-axis and shifted. The term *convolution* refers to both the resulting function and to the process of computing it. The integral is evaluated for all values of shift, producing the convolution function. The choice of which function is reflected and shifted before the integral does not change the integral result (see commutativity). Graphically, it expresses how the 'shape' of one function is modified by the other.

Some features of convolution are similar to cross-correlation: for real-valued functions, of a continuous or discrete variable, convolution f ∗ g {\displaystyle f*g} ({\displaystyle f*g}) differs from cross-correlation f ⋆ g {\displaystyle f\star g} ({\displaystyle f\star g}) only in that either f ( x ) {\displaystyle f(x)} ({\displaystyle f(x)}) or g ( x ) {\displaystyle g(x)} ({\displaystyle g(x)}) is reflected about the y-axis in convolution; thus it is a cross-correlation of g ( − x ) {\displaystyle g(-x)} ({\displaystyle g(-x)}) and f ( x ) {\displaystyle f(x)} ({\displaystyle f(x)}), or f ( − x ) {\displaystyle f(-x)} ({\displaystyle f(-x)}) and g ( x ) {\displaystyle g(x)} ({\displaystyle g(x)}). For complex-valued functions, the cross-correlation operator is the adjoint of the convolution operator.

Convolution has applications that include probability, statistics, acoustics, spectroscopy, signal processing and image processing, computer vision and human vision, geophysics, engineering, physics, and differential equations.

The convolution can be defined for functions on Euclidean space and other groups (as algebraic structures). For example, periodic functions, such as the discrete-time Fourier transform, can be defined on a circle and convolved by periodic convolution. (See row 18 at DTFT § Properties.) A *discrete convolution* can be defined for functions on the set of integers.

Generalizations of convolution have applications in the field of numerical analysis and numerical linear algebra, and in the design and implementation of finite impulse response filters in signal processing.

Computing the inverse of the convolution operation is known as deconvolution.


## Definition

The convolution of f {\displaystyle f} ({\displaystyle f}) and g {\displaystyle g} ({\displaystyle g}) is written f ∗ g {\displaystyle f*g} ({\displaystyle f*g}), denoting the operator with the symbol ∗ {\displaystyle *} ({\displaystyle *}). It is defined as the integral of the product of the two functions after one is reflected about the y-axis and shifted. As such, it is a particular kind of integral transform:

(

f

∗

g

)

(

t

)

:=

∫

−

∞

∞

f

(

τ

)

g

(

t

−

τ

)

d

τ

.

{\displaystyle (f*g)(t):=\int _{-\infty }^{\infty }f(\tau )g(t-\tau )\,d\tau .}

An equivalent definition is (see commutativity):

(

f

∗

g

)

(

t

)

:=

∫

−

∞

∞

f

(

t

−

τ

)

g

(

τ

)

d

τ

.

{\displaystyle (f*g)(t):=\int _{-\infty }^{\infty }f(t-\tau )g(\tau )\,d\tau .}

While the symbol t {\displaystyle t} ({\displaystyle t}) is used above, it need not represent the time domain. At each t {\displaystyle t} ({\displaystyle t}), the convolution formula can be described as the area under the function f ( τ ) {\displaystyle f(\tau )} ({\displaystyle f(\tau )}) weighted by the function g ( − τ ) {\displaystyle g(-\tau )} ({\displaystyle g(-\tau )}) shifted by the amount t {\displaystyle t} ({\displaystyle t}). As t {\displaystyle t} ({\displaystyle t}) changes, the weighting function g ( t − τ ) {\displaystyle g(t-\tau )} ({\displaystyle g(t-\tau )}) emphasizes different parts of the input function f ( τ ) {\displaystyle f(\tau )} ({\displaystyle f(\tau )}); If t {\displaystyle t} ({\displaystyle t}) is a positive value, then g ( t − τ ) {\displaystyle g(t-\tau )} ({\displaystyle g(t-\tau )}) is equal to g ( − τ ) {\displaystyle g(-\tau )} ({\displaystyle g(-\tau )}) that slides or is shifted along the τ {\displaystyle \tau } ({\displaystyle \tau })-axis toward the right (toward + ∞ {\displaystyle +\infty } ({\displaystyle +\infty })) by the amount of t {\displaystyle t} ({\displaystyle t}), while if t {\displaystyle t} ({\displaystyle t}) is a negative value, then g ( t − τ ) {\displaystyle g(t-\tau )} ({\displaystyle g(t-\tau )}) is equal to g ( − τ ) {\displaystyle g(-\tau )} ({\displaystyle g(-\tau )}) that slides or is shifted toward the left (toward − ∞ {\displaystyle -\infty } ({\displaystyle -\infty })) by the amount of | t | {\displaystyle |t|} ({\displaystyle |t|}).

For functions f {\displaystyle f} ({\displaystyle f}), g {\displaystyle g} ({\displaystyle g}) supported on only [ 0 , ∞ ) {\displaystyle [0,\infty )} ({\displaystyle [0,\infty )}) (i.e., zero for negative arguments), the integration limits can be truncated, resulting in:

(

f

∗

g

)

(

t

)

=

∫

0

t

f

(

τ

)

g

(

t

−

τ

)

d

τ

for

f

,

g

:

[

0

,

∞

)

→

R

.

{\displaystyle (f*g)(t)=\int _{0}^{t}f(\tau )g(t-\tau )\,d\tau \quad \ {\text{for }}f,g:[0,\infty )\to \mathbb {R} .}

For the multi-dimensional formulation of convolution, see *domain of definition* (below).

### Notation

A common engineering notational convention is:

f

(

t

)

∗

g

(

t

)

:=

∫

−

∞

∞

f

(

τ

)

g

(

t

−

τ

)

d

τ

⏟

(

f

∗

g

)

(

t

)

,

{\displaystyle f(t)*g(t)\mathrel {:=} \underbrace {\int _{-\infty }^{\infty }f(\tau )g(t-\tau )\,d\tau } _{(f*g)(t)},}

which has to be interpreted carefully to avoid confusion. For instance, f ( t ) ∗ g ( t − t 0 ) {\displaystyle f(t)*g(t-t_{0})} ({\displaystyle f(t)*g(t-t_{0})}) is equivalent to ( f ∗ g ) ( t − t 0 ) {\displaystyle (f*g)(t-t_{0})} ({\displaystyle (f*g)(t-t_{0})}), but f ( t − t 0 ) ∗ g ( t − t 0 ) {\displaystyle f(t-t_{0})*g(t-t_{0})} ({\displaystyle f(t-t_{0})*g(t-t_{0})}) is in fact equivalent to ( f ∗ g ) ( t − 2 t 0 ) {\displaystyle (f*g)(t-2t_{0})} ({\displaystyle (f*g)(t-2t_{0})}).

### Relations with other transforms

Given two functions f ( t ) {\displaystyle f(t)} ({\displaystyle f(t)}) and g ( t ) {\displaystyle g(t)} ({\displaystyle g(t)}) with bilateral Laplace transforms (two-sided Laplace transform)

F

(

s

)

=

∫

−

∞

∞

e

−

s

u

f

(

u

)

d

u

{\displaystyle F(s)=\int _{-\infty }^{\infty }e^{-su}\ f(u)\ {\text{d}}u}

and

G

(

s

)

=

∫

−

∞

∞

e

−

s

v

g

(

v

)

d

v

{\displaystyle G(s)=\int _{-\infty }^{\infty }e^{-sv}\ g(v)\ {\text{d}}v}

respectively, the convolution operation ( f ∗ g ) ( t ) {\displaystyle (f*g)(t)} ({\displaystyle (f*g)(t)}) can be defined as the inverse Laplace transform of the product of F ( s ) {\displaystyle F(s)} ({\displaystyle F(s)}) and G ( s ) {\displaystyle G(s)} ({\displaystyle G(s)}). More precisely,

F

(

s

)

⋅

G

(

s

)

=

∫

−

∞

∞

e

−

s

u

f

(

u

)

d

u

⋅

∫

−

∞

∞

e

−

s

v

g

(

v

)

d

v

=

∫

−

∞

∞

∫

−

∞

∞

e

−

s

(

u

+

v

)

f

(

u

)

g

(

v

)

d

u

d

v

{\displaystyle {\begin{aligned}F(s)\cdot G(s)&=\int _{-\infty }^{\infty }e^{-su}\ f(u)\ {\text{d}}u\cdot \int _{-\infty }^{\infty }e^{-sv}\ g(v)\ {\text{d}}v\\&=\int _{-\infty }^{\infty }\int _{-\infty }^{\infty }e^{-s(u+v)}\ f(u)\ g(v)\ {\text{d}}u\ {\text{d}}v\end{aligned}}}

Let t = u + v {\displaystyle t=u+v} ({\displaystyle t=u+v}), then

F

(

s

)

⋅

G

(

s

)

=

∫

−

∞

∞

∫

−

∞

∞

e

−

s

t

f

(

u

)

g

(

t

−

u

)

d

u

d

t

=

∫

−

∞

∞

e

−

s

t

∫

−

∞

∞

f

(

u

)

g

(

t

−

u

)

d

u

⏟

(

f

∗

g

)

(

t

)

d

t

=

∫

−

∞

∞

e

−

s

t

(

f

∗

g

)

(

t

)

d

t

.

{\displaystyle {\begin{aligned}F(s)\cdot G(s)&=\int _{-\infty }^{\infty }\int _{-\infty }^{\infty }e^{-st}\ f(u)\ g(t-u)\ {\text{d}}u\ {\text{d}}t\\&=\int _{-\infty }^{\infty }e^{-st}\underbrace {\int _{-\infty }^{\infty }f(u)\ g(t-u)\ {\text{d}}u} _{(f*g)(t)}\ {\text{d}}t\\&=\int _{-\infty }^{\infty }e^{-st}(f*g)(t)\ {\text{d}}t.\end{aligned}}}

Note that F ( s ) ⋅ G ( s ) {\displaystyle F(s)\cdot G(s)} ({\displaystyle F(s)\cdot G(s)}) is the bilateral Laplace transform of ( f ∗ g ) ( t ) {\displaystyle (f*g)(t)} ({\displaystyle (f*g)(t)}). A similar derivation can be done using the unilateral Laplace transform (one-sided Laplace transform).

The convolution operation also describes the output (in terms of the input) of an important class of operations known as *linear time-invariant* (LTI). See LTI system theory for a derivation of convolution as the result of LTI constraints. In terms of the Fourier transforms of the input and output of an LTI operation, no new frequency components are created. The existing ones are only modified (amplitude and/or phase). In other words, the output transform is the pointwise product of the input transform with a third transform (known as a transfer function). See Convolution theorem for a derivation of that property of convolution. Conversely, convolution can be derived as the inverse Fourier transform of the pointwise product of two Fourier transforms.


## Visual explanation

| Express each function in terms of a dummy variable τ . {\displaystyle \tau .} ({\displaystyle \tau .})Reflect one of the functions: g ( τ ) {\displaystyle g(\tau )} ({\displaystyle g(\tau )}) → g ( − τ ) . {\displaystyle g(-\tau ).} ({\displaystyle g(-\tau ).})Add an offset of the independent variable, t {\displaystyle t} ({\displaystyle t}), which allows g ( − τ ) {\displaystyle g(-\tau )} ({\displaystyle g(-\tau )}) to slide along the τ {\displaystyle \tau } ({\displaystyle \tau })-axis. If t is a positive value, then g ( t − τ ) {\displaystyle g(t-\tau )} ({\displaystyle g(t-\tau )}) is equal to g ( − τ ) {\displaystyle g(-\tau )} ({\displaystyle g(-\tau )}) that slides or is shifted along the τ {\displaystyle \tau } ({\displaystyle \tau })-axis toward the right (toward + ∞ {\displaystyle +\infty } ({\displaystyle +\infty })) by the amount of t {\displaystyle t} ({\displaystyle t}). If t {\displaystyle t} ({\displaystyle t}) is a negative value, then g ( t − τ ) {\displaystyle g(t-\tau )} ({\displaystyle g(t-\tau )}) is equal to g ( − τ ) {\displaystyle g(-\tau )} ({\displaystyle g(-\tau )}) that slides or is shifted toward the left (toward − ∞ {\displaystyle -\infty } ({\displaystyle -\infty })) by the amount of \| t \| {\displaystyle \|t\|} ({\displaystyle \|t\|}).Start t {\displaystyle t} ({\displaystyle t}) at − ∞ {\displaystyle -\infty } ({\displaystyle -\infty }) and slide it all the way to + ∞ {\displaystyle +\infty } ({\displaystyle +\infty }). Wherever the two functions intersect, find the integral of their product. In other words, at time t {\displaystyle t} ({\displaystyle t}), compute the area under the function f ( τ ) {\displaystyle f(\tau )} ({\displaystyle f(\tau )}) weighted by the weighting function g ( t − τ ) . {\displaystyle g(t-\tau ).} ({\displaystyle g(t-\tau ).}) The resulting waveform (not shown here) is the convolution of functions f {\displaystyle f} ({\displaystyle f}) and g {\displaystyle g} ({\displaystyle g}). If f ( t ) {\displaystyle f(t)} ({\displaystyle f(t)}) is a unit impulse, the result of this process is simply g ( t ) {\displaystyle g(t)} ({\displaystyle g(t)}). Formally: ∫ − ∞ ∞ δ ( τ ) g ( t − τ ) d τ = g ( t ) {\displaystyle \int _{-\infty }^{\infty }\delta (\tau )g(t-\tau )\,d\tau =g(t)} ({\displaystyle \int _{-\infty }^{\infty }\delta (\tau )g(t-\tau )\,d\tau =g(t)}) |   |
|---|---|
| In this example, the red-colored "pulse",   g ( τ ) , {\displaystyle \ g(\tau ),} ({\displaystyle \ g(\tau ),}) is an even function (   g ( − τ ) = g ( τ )   ) , {\displaystyle (\ g(-\tau )=g(\tau )\ ),} ({\displaystyle (\ g(-\tau )=g(\tau )\ ),}) so convolution is equivalent to correlation. A snapshot of this "movie" shows functions g ( t − τ ) {\displaystyle g(t-\tau )} ({\displaystyle g(t-\tau )}) and f ( τ ) {\displaystyle f(\tau )} ({\displaystyle f(\tau )}) (in blue) for some value of parameter t , {\displaystyle t,} ({\displaystyle t,}) which is arbitrarily defined as the distance along the τ {\displaystyle \tau } ({\displaystyle \tau }) axis from the point τ = 0 {\displaystyle \tau =0} ({\displaystyle \tau =0}) to the center of the red pulse. The amount of yellow is the area of the product f ( τ ) ⋅ g ( t − τ ) , {\displaystyle f(\tau )\cdot g(t-\tau ),} ({\displaystyle f(\tau )\cdot g(t-\tau ),}) computed by the convolution/correlation integral. The movie is created by continuously changing t {\displaystyle t} ({\displaystyle t}) and recomputing the integral. The result (shown in black) is a function of t , {\displaystyle t,} ({\displaystyle t,}) but is plotted on the same axis as τ , {\displaystyle \tau ,} ({\displaystyle \tau ,}) for convenience and comparison. |   |
| In this depiction, f ( τ ) {\displaystyle f(\tau )} ({\displaystyle f(\tau )}) could represent the response of a resistor-capacitor circuit to a narrow pulse that occurs at τ = 0. {\displaystyle \tau =0.} ({\displaystyle \tau =0.}) In other words, if g ( τ ) = δ ( τ ) , {\displaystyle g(\tau )=\delta (\tau ),} ({\displaystyle g(\tau )=\delta (\tau ),}) the result of convolution is just f ( t ) . {\displaystyle f(t).} ({\displaystyle f(t).}) But when g ( τ ) {\displaystyle g(\tau )} ({\displaystyle g(\tau )}) is the wider pulse (in red), the response is a "smeared" version of f ( t ) . {\displaystyle f(t).} ({\displaystyle f(t).}) It begins at t = − 0.5 , {\displaystyle t=-0.5,} ({\displaystyle t=-0.5,}) because we defined t {\displaystyle t} ({\displaystyle t}) as the distance from the τ = 0 {\displaystyle \tau =0} ({\displaystyle \tau =0}) axis to the *center* of the wide pulse (instead of the leading edge). |   |


## Historical developments

One of the earliest uses of the convolution integral appeared in D'Alembert's derivation of Taylor's theorem in *Recherches sur différents points importants du système du monde,* published in 1754.

Also, an expression of the type:

∫

f

(

u

)

⋅

g

(

x

−

u

)

d

u

{\displaystyle \int f(u)\cdot g(x-u)\,du}

is used by Sylvestre François Lacroix on page 505 of his book entitled *Treatise on differences and series*, which is the last of 3 volumes of the encyclopedic series: *Traité du calcul différentiel et du calcul intégral*, Chez Courcier, Paris, 1797–1800. Soon thereafter, convolution operations appear in the works of Pierre Simon Laplace, Jean-Baptiste Joseph Fourier, Siméon Denis Poisson, and others. The term itself did not come into wide use until the 1950s or 1960s. Prior to that it was sometimes known as *Faltung* (which means *folding* in German), *composition product*, *superposition integral*, and *Carson's integral*. Yet it appears as early as 1903, though the definition is rather unfamiliar in older uses.

The operation:

∫

0

t

φ

(

s

)

ψ

(

t

−

s

)

d

s

,

0

≤

t

<

∞

,

{\displaystyle \int _{0}^{t}\varphi (s)\psi (t-s)\,ds,\quad 0\leq t<\infty ,}

is a particular case of composition products considered by the Italian mathematician Vito Volterra in 1913.


## Circular convolution

When a function g T {\displaystyle g_{T}} ({\displaystyle g_{T}}) is periodic, with period T {\displaystyle T} ({\displaystyle T}), then for functions, f {\displaystyle f} ({\displaystyle f}), such that f ∗ g T {\displaystyle f*g_{T}} ({\displaystyle f*g_{T}}) exists, the convolution is also periodic and identical to:

(

f

∗

g

T

)

(

t

)

≡

∫

t

0

t

0

+

T

[

∑

k

=

−

∞

∞

f

(

τ

+

k

T

)

]

g

T

(

t

−

τ

)

d

τ

,

{\displaystyle (f*g_{T})(t)\equiv \int _{t_{0}}^{t_{0}+T}\left[\sum _{k=-\infty }^{\infty }f(\tau +kT)\right]g_{T}(t-\tau )\,d\tau ,}

where t 0 {\displaystyle t_{0}} ({\displaystyle t_{0}}) is an arbitrary choice. The summation is called a periodic summation of the function f {\displaystyle f} ({\displaystyle f}).

When g T {\displaystyle g_{T}} ({\displaystyle g_{T}}) is a periodic summation of another function, g {\displaystyle g} ({\displaystyle g}), then f ∗ g T {\displaystyle f*g_{T}} ({\displaystyle f*g_{T}}) is known as a *circular* or *cyclic* convolution of f {\displaystyle f} ({\displaystyle f}) and g {\displaystyle g} ({\displaystyle g}).

And if the periodic summation above is replaced by f T {\displaystyle f_{T}} ({\displaystyle f_{T}}), the operation is called a *periodic* convolution of f T {\displaystyle f_{T}} ({\displaystyle f_{T}}) and g T {\displaystyle g_{T}} ({\displaystyle g_{T}}).


## Discrete convolution

For complex-valued functions f {\displaystyle f} ({\displaystyle f}) and g {\displaystyle g} ({\displaystyle g}) defined on the set Z {\displaystyle \mathbb {Z} } ({\displaystyle \mathbb {Z} }) of integers, the *discrete convolution* of f {\displaystyle f} ({\displaystyle f}) and g {\displaystyle g} ({\displaystyle g}) is given by:

(

f

∗

g

)

[

n

]

=

∑

m

=

−

∞

∞

f

[

m

]

g

[

n

−

m

]

,

{\displaystyle (f*g)[n]=\sum _{m=-\infty }^{\infty }f[m]g[n-m],}

or equivalently (see commutativity) by:

(

f

∗

g

)

[

n

]

=

∑

m

=

−

∞

∞

f

[

n

−

m

]

g

[

m

]

.

{\displaystyle (f*g)[n]=\sum _{m=-\infty }^{\infty }f[n-m]g[m].}

The convolution of two finite sequences is defined by extending the sequences to finitely supported functions on the set of integers. When the sequences are the coefficients of two polynomials, then the coefficients of the ordinary product of the two polynomials are the convolution of the original two sequences. This is known as the Cauchy product of the coefficients of the sequences.

Thus, when g is non-zero over a finite interval [−*m*,+*m*] (representing, for instance, a finite impulse response), a finite summation may be used:

(

f

∗

g

)

[

n

]

=

∑

m

=

−

M

M

f

[

n

−

m

]

g

[

m

]

.

{\displaystyle (f*g)[n]=\sum _{m=-M}^{M}f[n-m]g[m].}

### Circular discrete convolution

When a function g N {\displaystyle g_{_{N}}} ({\displaystyle g_{_{N}}}) is periodic, with period N , {\displaystyle N,} ({\displaystyle N,}) then for functions, f , {\displaystyle f,} ({\displaystyle f,}) such that f ∗ g N {\displaystyle f*g_{_{N}}} ({\displaystyle f*g_{_{N}}}) exists, the convolution is also periodic and identical to**:**

(

f

∗

g

N

)

[

n

]

≡

∑

m

=

0

N

−

1

(

∑

k

=

−

∞

∞

f

[

m

+

k

N

]

)

g

N

[

n

−

m

]

.

{\displaystyle (f*g_{_{N}})[n]\equiv \sum _{m=0}^{N-1}\left(\sum _{k=-\infty }^{\infty }{f}[m+kN]\right)g_{_{N}}[n-m].}

The summation on k {\displaystyle k} ({\displaystyle k}) is called a periodic summation of the function f . {\displaystyle f.} ({\displaystyle f.})

If g N {\displaystyle g_{_{N}}} ({\displaystyle g_{_{N}}}) is a periodic summation of another function, g , {\displaystyle g,} ({\displaystyle g,}) then f ∗ g N {\displaystyle f*g_{_{N}}} ({\displaystyle f*g_{_{N}}}) is known as a circular convolution of f {\displaystyle f} ({\displaystyle f}) and g . {\displaystyle g.} ({\displaystyle g.})

When the non-zero durations of both f {\displaystyle f} ({\displaystyle f}) and g {\displaystyle g} ({\displaystyle g}) are limited to the interval [ 0 , N − 1 ] , {\displaystyle [0,N-1],} ({\displaystyle [0,N-1],})  f ∗ g N {\displaystyle f*g_{_{N}}} ({\displaystyle f*g_{_{N}}}) reduces to these common forms**:**

| ( f ∗ g N ) [ n ] = ∑ m = 0 N − 1 f [ m ] g N [ n − m ] = ∑ m = 0 n f [ m ] g [ n − m ] + ∑ m = n + 1 N − 1 f [ m ] g [ N + n − m ] = ∑ m = 0 N − 1 f [ m ] g [ ( n − m ) mod N ] ≜ ( f ∗ N g ) [ n ] {\displaystyle {\begin{aligned}\left(f*g_{N}\right)[n]&=\sum _{m=0}^{N-1}f[m]g_{N}[n-m]\\&=\sum _{m=0}^{n}f[m]g[n-m]+\sum _{m=n+1}^{N-1}f[m]g[N+n-m]\\[2pt]&=\sum _{m=0}^{N-1}f[m]g[(n-m)_{\bmod {N}}]\\[2pt]&\triangleq \left(f*_{N}g\right)[n]\end{aligned}}} ({\displaystyle {\begin{aligned}\left(f*g_{N}\right)[n]&=\sum _{m=0}^{N-1}f[m]g_{N}[n-m]\\&=\sum _{m=0}^{n}f[m]g[n-m]+\sum _{m=n+1}^{N-1}f[m]g[N+n-m]\\[2pt]&=\sum _{m=0}^{N-1}f[m]g[(n-m)_{\bmod {N}}]\\[2pt]&\triangleq \left(f*_{N}g\right)[n]\end{aligned}}}) |   | Eq.1 |
|---|---|---|

The notation f ∗ N g {\displaystyle f*_{N}g} ({\displaystyle f*_{N}g}) for *cyclic convolution* denotes convolution over the cyclic group of integers modulo *N*.

Circular convolution arises most often in the context of fast convolution with a fast Fourier transform (FFT) algorithm.

### Fast convolution algorithms

In many situations, discrete convolutions can be converted to circular convolutions so that fast transforms with a convolution property can be used to implement the computation. For example, convolution of digit sequences is the kernel operation in multiplication of multi-digit numbers, which can therefore be efficiently implemented with transform techniques (Knuth 1997, §4.3.3.C; von zur Gathen & Gerhard 2003, §8.2).

**Eq.1** requires N arithmetic operations per output value and *N*2 operations for N outputs. That can be significantly reduced with any of several fast algorithms. Digital signal processing and other applications typically use fast convolution algorithms to reduce the cost of the convolution to O(N log N) complexity.

The most common fast convolution algorithms use fast Fourier transform (FFT) algorithms via the circular convolution theorem. Specifically, the circular convolution of two finite-length sequences is found by taking an FFT of each sequence, multiplying pointwise, and then performing an inverse FFT. Convolutions of the type defined above are then efficiently implemented using that technique in conjunction with zero-extension and/or discarding portions of the output. Other fast convolution algorithms, such as the Schönhage–Strassen algorithm or the Mersenne transform, use fast Fourier transforms in other rings. The Winograd method is used as an alternative to the FFT. It significantly speeds up 1D, 2D, and 3D convolution.

If one sequence is much longer than the other, zero-extension of the shorter sequence and fast circular convolution is not the most computationally efficient method available. Instead, decomposing the longer sequence into blocks and convolving each block allows for faster algorithms such as the overlap–save method and overlap–add method. A hybrid convolution method that combines block and FIR algorithms allows for a zero input-output latency that is useful for real-time convolution computations.


## Domain of definition

The convolution of two complex-valued functions on **R***d* is itself a complex-valued function on **R***d*, defined by:

(

f

∗

g

)

(

x

)

=

∫

R

d

f

(

y

)

g

(

x

−

y

)

d

y

=

∫

R

d

f

(

x

−

y

)

g

(

y

)

d

y

,

{\displaystyle (f*g)(x)=\int _{\mathbf {R} ^{d}}f(y)g(x-y)\,dy=\int _{\mathbf {R} ^{d}}f(x-y)g(y)\,dy,}

and is well-defined only if f and g decay sufficiently rapidly at infinity in order for the integral to exist. Conditions for the existence of the convolution may be tricky, since a blow-up in g at infinity can be easily offset by sufficiently rapid decay in f. The question of existence thus may involve different conditions on f and g:

### Compactly supported functions

If f and g are compactly supported continuous functions, then their convolution exists, and is also compactly supported and continuous (Hörmander 1983, Chapter 1). More generally, if either function (say f) is compactly supported and the other is locally integrable, then the convolution *f*∗*g* is well-defined and continuous.

Convolution of f and g is also well defined when both functions are locally square integrable on **R** and supported on an interval of the form [*a*, +∞) (or both supported on [−∞, *a*]).

### Integrable functions

The convolution of f and g exists if f and g are both Lebesgue integrable functions in *L*1(**R***d*), and in this case *f*∗*g* is also integrable (Stein & Weiss 1971, Theorem 1.3). This is a consequence of Tonelli's theorem. This is also true for functions in *L*1, under the discrete convolution, or more generally for the convolution on any group.

Likewise, if *f* ∈ *L*1(**R***d*)  and  *g* ∈ *L**p*(**R***d*)  where 1 ≤ *p* ≤ ∞, then  *f***g* ∈ *L**p*(**R***d*), and

‖

f

∗

g

‖

p

≤

‖

f

‖

1

‖

g

‖

p

.

{\displaystyle \|{f}*g\|_{p}\leq \|f\|_{1}\|g\|_{p}.}

In the particular case *p* = 1, this shows that *L*1 is a Banach algebra under the convolution (and equality of the two sides holds if f and g are non-negative almost everywhere).

More generally, Young's inequality implies that the convolution is a continuous bilinear map between suitable *L**p* spaces. Specifically, if 1 ≤ *p*, *q*, *r* ≤ ∞ satisfy:

1

p

+

1

q

=

1

r

+

1

,

{\displaystyle {\frac {1}{p}}+{\frac {1}{q}}={\frac {1}{r}}+1,}

then

‖

f

∗

g

‖

r

≤

‖

f

‖

p

‖

g

‖

q

,

f

∈

L

p

,

g

∈

L

q

,

{\displaystyle \left\Vert f*g\right\Vert _{r}\leq \left\Vert f\right\Vert _{p}\left\Vert g\right\Vert _{q},\quad f\in L^{p},\ g\in L^{q},}

so that the convolution is a continuous bilinear mapping from *L**p*×*L**q* to *L**r*. The Young inequality for convolution is also true in other contexts (circle group, convolution on **Z**). The preceding inequality is not sharp on the real line: when 1 < *p*, *q*, *r* < ∞, there exists a constant *B**p*,*q* < 1 such that:

‖

f

∗

g

‖

r

≤

B

p

,

q

‖

f

‖

p

‖

g

‖

q

,

f

∈

L

p

,

g

∈

L

q

.

{\displaystyle \left\Vert f*g\right\Vert _{r}\leq B_{p,q}\left\Vert f\right\Vert _{p}\left\Vert g\right\Vert _{q},\quad f\in L^{p},\ g\in L^{q}.}

The optimal value of *B**p*,*q* was discovered in 1975 and independently in 1976, see Brascamp–Lieb inequality.

A stronger estimate is true provided 1 < *p*, *q*, *r* < ∞:

‖

f

∗

g

‖

r

≤

C

p

,

q

‖

f

‖

p

‖

g

‖

q

,

w

{\displaystyle \|f*g\|_{r}\leq C_{p,q}\|f\|_{p}\|g\|_{q,w}}

where ‖ g ‖ q , w {\displaystyle \|g\|_{q,w}} ({\displaystyle \|g\|_{q,w}}) is the weak *L**q* norm. Convolution also defines a bilinear continuous map L p , w × L q , w → L r , w {\displaystyle L^{p,w}\times L^{q,w}\to L^{r,w}} ({\displaystyle L^{p,w}\times L^{q,w}\to L^{r,w}}) for 1 < p , q , r < ∞ {\displaystyle 1<p,q,r<\infty } ({\displaystyle 1<p,q,r<\infty }), owing to the weak Young inequality:

‖

f

∗

g

‖

r

,

w

≤

C

p

,

q

‖

f

‖

p

,

w

‖

g

‖

r

,

w

.

{\displaystyle \|f*g\|_{r,w}\leq C_{p,q}\|f\|_{p,w}\|g\|_{r,w}.}

### Functions of rapid decay

In addition to compactly supported functions and integrable functions, functions that have sufficiently rapid decay at infinity can also be convolved. An important feature of the convolution is that if *f* and *g* both decay rapidly, then *f*∗*g* also decays rapidly. In particular, if *f* and *g* are rapidly decreasing functions, then so is the convolution *f*∗*g*. Combined with the fact that convolution commutes with differentiation (see #Properties), it follows that the class of Schwartz functions is closed under convolution (Stein & Weiss 1971, Theorem 3.3).

### Distributions

If *f* is a smooth function that is compactly supported and *g* is a distribution, then *f*∗*g* is a smooth function defined by

∫

R

d

f

(

y

)

g

(

x

−

y

)

d

y

=

(

f

∗

g

)

(

x

)

∈

C

∞

(

R

d

)

.

{\displaystyle \int _{\mathbb {R} ^{d}}{f}(y)g(x-y)\,dy=(f*g)(x)\in C^{\infty }(\mathbb {R} ^{d}).}

More generally, it is possible to extend the definition of the convolution in a unique way with φ {\displaystyle \varphi } ({\displaystyle \varphi }) the same as *f* above, so that the associative law

f

∗

(

g

∗

φ

)

=

(

f

∗

g

)

∗

φ

{\displaystyle f*(g*\varphi )=(f*g)*\varphi }

remains valid in the case where *f* is a distribution, and *g* a compactly supported distribution (Hörmander 1983, §4.2).

### Measures

The convolution of any two Borel measures *μ* and *ν* of bounded variation is the measure μ ∗ ν {\displaystyle \mu *\nu } ({\displaystyle \mu *\nu }) defined by (Rudin 1962)

∫

R

d

f

(

x

)

d

(

μ

∗

ν

)

(

x

)

=

∫

R

d

∫

R

d

f

(

x

+

y

)

d

μ

(

x

)

d

ν

(

y

)

.

{\displaystyle \int _{\mathbf {R} ^{d}}f(x)\,d(\mu *\nu )(x)=\int _{\mathbf {R} ^{d}}\int _{\mathbf {R} ^{d}}f(x+y)\,d\mu (x)\,d\nu (y).}

In particular,

(

μ

∗

ν

)

(

A

)

=

∫

R

d

×

R

d

1

A

(

x

+

y

)

d

(

μ

×

ν

)

(

x

,

y

)

,

{\displaystyle (\mu *\nu )(A)=\int _{\mathbf {R} ^{d}\times \mathbf {R} ^{d}}1_{A}(x+y)\,d(\mu \times \nu )(x,y),}

where A ⊂ R d {\displaystyle A\subset \mathbf {R} ^{d}} ({\displaystyle A\subset \mathbf {R} ^{d}}) is a measurable set and 1 A {\displaystyle 1_{A}} ({\displaystyle 1_{A}}) is the indicator function of A {\displaystyle A} ({\displaystyle A}).

This agrees with the convolution defined above when μ and ν are regarded as distributions, as well as the convolution of L1 functions when μ and ν are absolutely continuous with respect to the Lebesgue measure.

The convolution of measures also satisfies the following version of Young's inequality

‖

μ

∗

ν

‖

≤

‖

μ

‖

‖

ν

‖

{\displaystyle \|\mu *\nu \|\leq \|\mu \|\|\nu \|}

where the norm is the total variation of a measure. Because the space of measures of bounded variation is a Banach space, convolution of measures can be treated with standard methods of functional analysis that may not apply for the convolution of distributions.


## Properties

### Algebraic properties

The convolution defines a product on the linear space of integrable functions. This product satisfies the following algebraic properties, which formally mean that the space of integrable functions with the product given by convolution is a commutative associative algebra without identity (Strichartz 1994, §3.3). Other linear spaces of functions, such as the space of continuous functions of compact support, are closed under the convolution, and so also form commutative associative algebras.

**Commutativity**

f

∗

g

=

g

∗

f

{\displaystyle f*g=g*f}

Proof: By definition:

(

f

∗

g

)

(

t

)

=

∫

−

∞

∞

f

(

τ

)

g

(

t

−

τ

)

d

τ

{\displaystyle (f*g)(t)=\int _{-\infty }^{\infty }f(\tau )g(t-\tau )\,d\tau }

Changing the variable of integration to

u

=

t

−

τ

{\displaystyle u=t-\tau }

the result follows.

**Associativity**

f

∗

(

g

∗

h

)

=

(

f

∗

g

)

∗

h

{\displaystyle f*(g*h)=(f*g)*h}

Proof: This follows from using

Fubini's theorem

(i.e., double integrals can be evaluated as iterated integrals in either order).

**Distributivity**

f

∗

(

g

+

h

)

=

(

f

∗

g

)

+

(

f

∗

h

)

{\displaystyle f*(g+h)=(f*g)+(f*h)}

Proof: This follows from linearity of the integral.

**Associativity with scalar multiplication**

a

(

f

∗

g

)

=

(

a

f

)

∗

g

{\displaystyle a(f*g)=(af)*g}

for any real (or complex) number

a

{\displaystyle a}

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

f

∗

δ

=

f

{\displaystyle f*\delta =f}

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

S

−

1

∗

S

=

δ

{\displaystyle S^{-1}*S=\delta }

from which an explicit formula for

S

−1

may be obtained.

The set of invertible distributions forms an

abelian group

under the convolution.

**Complex conjugation**

f

∗

g

¯

=

f

¯

∗

g

¯

{\displaystyle {\overline {f*g}}={\overline {f}}*{\overline {g}}}

**Time reversal**

If

q

(

t

)

=

r

(

t

)

∗

s

(

t

)

,

{\displaystyle q(t)=r(t)*s(t),}

then

q

(

−

t

)

=

r

(

−

t

)

∗

s

(

−

t

)

.

{\displaystyle q(-t)=r(-t)*s(-t).}

> Proof (using convolution theorem):
> 
> q ( t )   ⟺ F     Q ( f ) = R ( f ) S ( f ) {\displaystyle q(t)\ {\stackrel {\mathcal {F}}{\Longleftrightarrow }}\ \ Q(f)=R(f)S(f)} ({\displaystyle q(t)\ {\stackrel {\mathcal {F}}{\Longleftrightarrow }}\ \ Q(f)=R(f)S(f)})
> 
> q ( − t )   ⟺ F     Q ( − f ) = R ( − f ) S ( − f ) {\displaystyle q(-t)\ {\stackrel {\mathcal {F}}{\Longleftrightarrow }}\ \ Q(-f)=R(-f)S(-f)} ({\displaystyle q(-t)\ {\stackrel {\mathcal {F}}{\Longleftrightarrow }}\ \ Q(-f)=R(-f)S(-f)})
> 
> q ( − t ) = F − 1 { R ( − f ) S ( − f ) } = F − 1 { R ( − f ) } ∗ F − 1 { S ( − f ) } = r ( − t ) ∗ s ( − t ) {\displaystyle {\begin{aligned}q(-t)&={\mathcal {F}}^{-1}{\bigg \{}R(-f)S(-f){\bigg \}}\\&={\mathcal {F}}^{-1}{\bigg \{}R(-f){\bigg \}}*{\mathcal {F}}^{-1}{\bigg \{}S(-f){\bigg \}}\\&=r(-t)*s(-t)\end{aligned}}} ({\displaystyle {\begin{aligned}q(-t)&={\mathcal {F}}^{-1}{\bigg \{}R(-f)S(-f){\bigg \}}\\&={\mathcal {F}}^{-1}{\bigg \{}R(-f){\bigg \}}*{\mathcal {F}}^{-1}{\bigg \{}S(-f){\bigg \}}\\&=r(-t)*s(-t)\end{aligned}}})

**Relationship with differentiation**

(

f

∗

g

)

′

=

f

′

∗

g

=

f

∗

g

′

{\displaystyle (f*g)'=f'*g=f*g'}

Proof:

(

f

∗

g

)

′

=

d

d

t

∫

−

∞

∞

f

(

τ

)

g

(

t

−

τ

)

d

τ

=

∫

−

∞

∞

f

(

τ

)

∂

∂

t

g

(

t

−

τ

)

d

τ

=

∫

−

∞

∞

f

(

τ

)

g

′

(

t

−

τ

)

d

τ

=

f

∗

g

′

.

{\displaystyle {\begin{aligned}(f*g)'&={\frac {d}{dt}}\int _{-\infty }^{\infty }f(\tau )g(t-\tau )\,d\tau \\&=\int _{-\infty }^{\infty }f(\tau ){\frac {\partial }{\partial t}}g(t-\tau )\,d\tau \\&=\int _{-\infty }^{\infty }f(\tau )g'(t-\tau )\,d\tau =f*g'.\end{aligned}}}

**Relationship with integration**

If

F

(

t

)

=

∫

−

∞

t

f

(

τ

)

d

τ

,

{\textstyle F(t)=\int _{-\infty }^{t}f(\tau )d\tau ,}

and

G

(

t

)

=

∫

−

∞

t

g

(

τ

)

d

τ

,

{\textstyle G(t)=\int _{-\infty }^{t}g(\tau )\,d\tau ,}

then

(

F

∗

g

)

(

t

)

=

(

f

∗

G

)

(

t

)

=

∫

−

∞

t

(

f

∗

g

)

(

τ

)

d

τ

.

{\displaystyle (F*g)(t)=(f*G)(t)=\int _{-\infty }^{t}(f*g)(\tau )\,d\tau .}

### Integration

If *f* and *g* are integrable functions, then the integral of their convolution on the whole space is simply obtained as the product of their integrals:

∫

R

d

(

f

∗

g

)

(

x

)

d

x

=

(

∫

R

d

f

(

x

)

d

x

)

(

∫

R

d

g

(

x

)

d

x

)

.

{\displaystyle \int _{\mathbf {R} ^{d}}(f*g)(x)\,dx=\left(\int _{\mathbf {R} ^{d}}f(x)\,dx\right)\left(\int _{\mathbf {R} ^{d}}g(x)\,dx\right).}

This follows from Fubini's theorem. The same result holds if *f* and *g* are only assumed to be nonnegative measurable functions, by Tonelli's theorem.

### Differentiation

In the one-variable case,

d

d

x

(

f

∗

g

)

=

d

f

d

x

∗

g

=

f

∗

d

g

d

x

{\displaystyle {\frac {d}{dx}}(f*g)={\frac {df}{dx}}*g=f*{\frac {dg}{dx}}}

where d d x {\displaystyle {\frac {d}{dx}}} ({\displaystyle {\frac {d}{dx}}}) is the derivative. More generally, in the case of functions of several variables, an analogous formula holds with the partial derivative:

∂

∂

x

i

(

f

∗

g

)

=

∂

f

∂

x

i

∗

g

=

f

∗

∂

g

∂

x

i

.

{\displaystyle {\frac {\partial }{\partial x_{i}}}(f*g)={\frac {\partial f}{\partial x_{i}}}*g=f*{\frac {\partial g}{\partial x_{i}}}.}

A particular consequence of this is that the convolution can be viewed as a "smoothing" operation: the convolution of *f* and *g* is differentiable as many times as *f* and *g* are in total.

These identities hold for example under the condition that *f* and *g* are absolutely integrable and at least one of them has an absolutely integrable (L1) weak derivative, as a consequence of Young's convolution inequality. For instance, when *f* is continuously differentiable with compact support, and *g* is an arbitrary locally integrable function,

d

d

x

(

f

∗

g

)

=

d

f

d

x

∗

g

.

{\displaystyle {\frac {d}{dx}}(f*g)={\frac {df}{dx}}*g.}

These identities also hold much more broadly in the sense of tempered distributions if one of *f* or *g* is a rapidly decreasing tempered distribution, a compactly supported tempered distribution or a Schwartz function and the other is a tempered distribution. On the other hand, two positive integrable and infinitely differentiable functions may have a nowhere continuous convolution.

In the discrete case, the difference operator *D* *f*(*n*) = *f*(*n* + 1) − *f*(*n*) satisfies an analogous relationship:

D

(

f

∗

g

)

=

(

D

f

)

∗

g

=

f

∗

(

D

g

)

.

{\displaystyle D(f*g)=(Df)*g=f*(Dg).}

### Convolution theorem

The convolution theorem states that

F

{

f

∗

g

}

=

F

{

f

}

⋅

F

{

g

}

{\displaystyle {\mathcal {F}}\{f*g\}={\mathcal {F}}\{f\}\cdot {\mathcal {F}}\{g\}}

where F { f } {\displaystyle {\mathcal {F}}\{f\}} ({\displaystyle {\mathcal {F}}\{f\}}) denotes the Fourier transform of f {\displaystyle f} ({\displaystyle f}).

#### Convolution in other types of transformations

Versions of this theorem also hold for the Laplace transform, two-sided Laplace transform, Z-transform and Mellin transform.

#### Convolution on matrices

If W {\displaystyle {\mathcal {W}}} ({\displaystyle {\mathcal {W}}}) is the Fourier transform matrix, then

W

(

C

(

1

)

x

∗

C

(

2

)

y

)

=

(

W

C

(

1

)

∙

W

C

(

2

)

)

(

x

⊗

y

)

=

W

C

(

1

)

x

∘

W

C

(

2

)

y

{\displaystyle {\mathcal {W}}\left(C^{(1)}x\ast C^{(2)}y\right)=\left({\mathcal {W}}C^{(1)}\bullet {\mathcal {W}}C^{(2)}\right)(x\otimes y)={\mathcal {W}}C^{(1)}x\circ {\mathcal {W}}C^{(2)}y}

,

where ∙ {\displaystyle \bullet } ({\displaystyle \bullet }) is face-splitting product, ⊗ {\displaystyle \otimes } ({\displaystyle \otimes }) denotes Kronecker product, ∘ {\displaystyle \circ } ({\displaystyle \circ }) denotes Hadamard product (this result is an evolving of count sketch properties).

This can be generalized for appropriate matrices A , B {\displaystyle \mathbf {A} ,\mathbf {B} } ({\displaystyle \mathbf {A} ,\mathbf {B} }):

W

(

(

A

x

)

∗

(

B

y

)

)

=

(

(

W

A

)

∙

(

W

B

)

)

(

x

⊗

y

)

=

(

W

A

x

)

∘

(

W

B

y

)

{\displaystyle {\mathcal {W}}\left((\mathbf {A} x)\ast (\mathbf {B} y)\right)=\left(({\mathcal {W}}\mathbf {A} )\bullet ({\mathcal {W}}\mathbf {B} )\right)(x\otimes y)=({\mathcal {W}}\mathbf {A} x)\circ ({\mathcal {W}}\mathbf {B} y)}

from the properties of the face-splitting product.

### Translational equivariance

The convolution commutes with translations, meaning that

τ

x

(

f

∗

g

)

=

(

τ

x

f

)

∗

g

=

f

∗

(

τ

x

g

)

{\displaystyle \tau _{x}(f*g)=(\tau _{x}f)*g=f*(\tau _{x}g)}

where τ*x*f is the translation of the function *f* by *x* defined by

(

τ

x

f

)

(

y

)

=

f

(

y

−

x

)

.

{\displaystyle (\tau _{x}f)(y)=f(y-x).}

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

(

f

∗

g

)

(

x

)

=

∫

G

f

(

y

)

g

(

y

−

1

x

)

d

λ

(

y

)

.

{\displaystyle (f*g)(x)=\int _{G}f(y)g\left(y^{-1}x\right)\,d\lambda (y).}

It is not commutative in general. In typical cases of interest *G* is a locally compact Hausdorff topological group and λ is a (left-) Haar measure. In that case, unless *G* is unimodular, the convolution defined in this way is not the same as ∫ f ( x y − 1 ) g ( y ) d λ ( y ) {\textstyle \int f\left(xy^{-1}\right)g(y)\,d\lambda (y)} ({\textstyle \int f\left(xy^{-1}\right)g(y)\,d\lambda (y)}). The preference of one over the other is made so that convolution with a fixed function *g* commutes with left translation in the group:

L

h

(

f

∗

g

)

=

(

L

h

f

)

∗

g

.

{\displaystyle L_{h}(f*g)=(L_{h}f)*g.}

Furthermore, the convention is also required for consistency with the definition of the convolution of measures given below. However, with a right instead of a left Haar measure, the latter integral is preferred over the former.

On locally compact abelian groups, a version of the convolution theorem holds: the Fourier transform of a convolution is the pointwise product of the Fourier transforms. The circle group **T** with the Lebesgue measure is an immediate example. For a fixed *g* in *L*1(**T**), we have the following familiar operator acting on the Hilbert space *L*2(**T**):

T

f

(

x

)

=

1

2

π

∫

T

f

(

y

)

g

(

x

−

y

)

d

y

.

{\displaystyle T{f}(x)={\frac {1}{2\pi }}\int _{\mathbf {T} }{f}(y)g(x-y)\,dy.}

The operator *T* is compact. A direct calculation shows that its adjoint *T** is convolution with

g

¯

(

−

y

)

.

{\displaystyle {\bar {g}}(-y).}

By the commutativity property cited above, *T* is normal: *T** *T* = *TT** . Also, *T* commutes with the translation operators. Consider the family *S* of operators consisting of all such convolutions and the translation operators. Then *S* is a commuting family of normal operators. According to spectral theory, there exists an orthonormal basis {*hk*} that simultaneously diagonalizes *S*. This characterizes convolutions on the circle. Specifically, we have

h

k

(

x

)

=

e

i

k

x

,

k

∈

Z

,

{\displaystyle h_{k}(x)=e^{ikx},\quad k\in \mathbb {Z} ,\;}

which are precisely the characters of **T**. Each convolution is a compact multiplication operator in this basis. This can be viewed as a version of the convolution theorem discussed above.

A discrete example is a finite cyclic group of order *n*. Convolution operators are here represented by circulant matrices, and can be diagonalized by the discrete Fourier transform.

A similar result holds for compact groups (not necessarily abelian): the matrix coefficients of finite-dimensional unitary representations form an orthonormal basis in *L*2 by the Peter–Weyl theorem, and an analog of the convolution theorem continues to hold, along with many other aspects of harmonic analysis that depend on the Fourier transform.


## Convolution of measures

Let *G* be a (multiplicatively written) topological group. If μ and ν are Radon measures on *G*, then their convolution *μ*∗*ν* is defined as the pushforward measure of the group action and can be written as

(

μ

∗

ν

)

(

E

)

=

∬

1

E

(

x

y

)

d

μ

(

x

)

d

ν

(

y

)

{\displaystyle (\mu *\nu )(E)=\iint 1_{E}(xy)\,d\mu (x)\,d\nu (y)}

for each measurable subset *E* of *G*. The convolution is also a Radon measure, whose total variation satisfies

‖

μ

∗

ν

‖

≤

‖

μ

‖

‖

ν

‖

.

{\displaystyle \|\mu *\nu \|\leq \left\|\mu \right\|\left\|\nu \right\|.}

In the case when *G* is locally compact with (left-)Haar measure λ, and μ and ν are absolutely continuous with respect to a λ, so that each has a density function, then the convolution μ∗ν is also absolutely continuous, and its density function is just the convolution of the two separate density functions. In fact, if *either* measure is absolutely continuous with respect to the Haar measure, then so is their convolution.

If μ and ν are probability measures on the topological group (**R**,+), then the convolution *μ*∗*ν* is the probability distribution of the sum *X* + *Y* of two independent random variables *X* and *Y* whose respective distributions are μ and ν.


## Infimal convolution

In convex analysis, the **infimal convolution** of proper (not identically + ∞ {\displaystyle +\infty } ({\displaystyle +\infty })) convex functions f 1 , … , f m {\displaystyle f_{1},\dots ,f_{m}} ({\displaystyle f_{1},\dots ,f_{m}}) on R n {\displaystyle \mathbb {R} ^{n}} ({\displaystyle \mathbb {R} ^{n}}) is defined by: ( f 1 ∗ ⋯ ∗ f m ) ( x ) = inf x { f 1 ( x 1 ) + ⋯ + f m ( x m ) | x 1 + ⋯ + x m = x } . {\displaystyle (f_{1}*\cdots *f_{m})(x)=\inf _{x}\{f_{1}(x_{1})+\cdots +f_{m}(x_{m})|x_{1}+\cdots +x_{m}=x\}.} ({\displaystyle (f_{1}*\cdots *f_{m})(x)=\inf _{x}\{f_{1}(x_{1})+\cdots +f_{m}(x_{m})|x_{1}+\cdots +x_{m}=x\}.}) It can be shown that the infimal convolution of convex functions is convex. Furthermore, it satisfies an identity analogous to that of the Fourier transform of a traditional convolution, with the role of the Fourier transform is played instead by the Legendre transform: φ ∗ ( x ) = sup y ( x ⋅ y − φ ( y ) ) . {\displaystyle \varphi ^{*}(x)=\sup _{y}(x\cdot y-\varphi (y)).} ({\displaystyle \varphi ^{*}(x)=\sup _{y}(x\cdot y-\varphi (y)).}) We have: ( f 1 ∗ ⋯ ∗ f m ) ∗ ( x ) = f 1 ∗ ( x ) + ⋯ + f m ∗ ( x ) . {\displaystyle (f_{1}*\cdots *f_{m})^{*}(x)=f_{1}^{*}(x)+\cdots +f_{m}^{*}(x).} ({\displaystyle (f_{1}*\cdots *f_{m})^{*}(x)=f_{1}^{*}(x)+\cdots +f_{m}^{*}(x).})
