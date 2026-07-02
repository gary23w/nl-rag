---
title: "Big O notation (part 2/2)"
source: https://en.wikipedia.org/wiki/Big_O_notation
domain: algorithms
license: CC-BY-SA-4.0
tags: algorithm, sorting, complexity, big-o, dynamic programming
fetched: 2026-07-02
part: 2/2
---

## Little-o notation

For real or complex-valued functions of a real variable x {\displaystyle x} ({\displaystyle x}) with g ( x ) > 0 {\displaystyle g(x)>0} ({\displaystyle g(x)>0}) for sufficiently large x {\displaystyle x} ({\displaystyle x}), one writes

f

(

x

)

=

o

(

g

(

x

)

)

as

x

→

∞

{\displaystyle f(x)=o(g(x))\quad {\text{ as }}x\to \infty }

if lim x → ∞ f ( x ) g ( x ) = 0. {\displaystyle \lim _{x\to \infty }{\frac {f(x)}{g(x)}}=0.} ({\displaystyle \lim _{x\to \infty }{\frac {f(x)}{g(x)}}=0.}) That is, for every positive constant ε there exists a constant x 0 {\displaystyle x_{0}} ({\displaystyle x_{0}}) such that

|

f

(

x

)

|

≤

ε

g

(

x

)

for all

x

≥

x

0

.

{\displaystyle |f(x)|\leq \varepsilon g(x)\quad {\text{ for all }}x\geq x_{0}.}

Intuitively, this means that g ( x ) {\displaystyle g(x)} ({\displaystyle g(x)}) grows much faster than f ( x ) {\displaystyle f(x)} ({\displaystyle f(x)}), or equivalently f ( x ) {\displaystyle f(x)} ({\displaystyle f(x)}) grows much slower than g ( x ) {\displaystyle g(x)} ({\displaystyle g(x)}). For example, one has

200

x

=

o

(

x

2

)

{\displaystyle 200x=o(x^{2})}

and

1

/

x

=

o

(

1

)

,

{\displaystyle 1/x=o(1),}

both as

x

→

∞

.

{\displaystyle x\to \infty .}

When one is interested in the behavior of a function for large values of x {\displaystyle x} ({\displaystyle x}), little-o notation makes a *stronger statement* than the corresponding big-O notation: every function that is little-o of g {\displaystyle g} ({\displaystyle g}) is also big-O of g {\displaystyle g} ({\displaystyle g}) on some interval [ a , ∞ ) {\displaystyle [a,\infty )} ({\displaystyle [a,\infty )}), but not every function that is big-O of g {\displaystyle g} ({\displaystyle g}) is little-o of g {\displaystyle g} ({\displaystyle g}). For example, 2 x 2 = O ( x 2 ) {\displaystyle 2x^{2}=O(x^{2})} ({\displaystyle 2x^{2}=O(x^{2})}) but 2 x 2 ≠ o ( x 2 ) {\displaystyle 2x^{2}\neq o(x^{2})} ({\displaystyle 2x^{2}\neq o(x^{2})}) for x ≥ 1 {\displaystyle x\geq 1} ({\displaystyle x\geq 1}).

Little-o respects a number of arithmetic operations. For example,

if

c

{\displaystyle c}

is a nonzero constant and

f

=

o

(

g

)

{\displaystyle f=o(g)}

then

c

⋅

f

=

o

(

g

)

{\displaystyle c\cdot f=o(g)}

, and

if

f

=

o

(

F

)

{\displaystyle f=o(F)}

and

g

=

o

(

G

)

{\displaystyle g=o(G)}

then

f

⋅

g

=

o

(

F

⋅

G

)

.

{\displaystyle f\cdot g=o(F\cdot G).}

if

f

=

o

(

F

)

{\displaystyle f=o(F)}

and

g

=

o

(

G

)

{\displaystyle g=o(G)}

then

f

+

g

=

o

(

F

+

G

)

{\displaystyle f+g=o(F+G)}

It also satisfies a transitivity relation:

if

f

=

o

(

g

)

{\displaystyle f=o(g)}

and

g

=

o

(

h

)

{\displaystyle g=o(h)}

then

f

=

o

(

h

)

.

{\displaystyle f=o(h).}

Little-o can also be generalized to the finite case: f ( x ) = o ( g ( x ) )  as  x → x 0 {\displaystyle f(x)=o(g(x))\quad {\text{ as }}x\to x_{0}} ({\displaystyle f(x)=o(g(x))\quad {\text{ as }}x\to x_{0}}) if lim x → x 0 f ( x ) g ( x ) = 0. {\displaystyle \lim _{x\to x_{0}}{\frac {f(x)}{g(x)}}=0.} ({\displaystyle \lim _{x\to x_{0}}{\frac {f(x)}{g(x)}}=0.}) In other words, f ( x ) = α ( x ) g ( x ) {\displaystyle f(x)=\alpha (x)g(x)} ({\displaystyle f(x)=\alpha (x)g(x)}) for some α ( x ) {\displaystyle \alpha (x)} ({\displaystyle \alpha (x)}) with lim x → x 0 α ( x ) = 0 {\displaystyle \lim _{x\to x_{0}}\alpha (x)=0} ({\displaystyle \lim _{x\to x_{0}}\alpha (x)=0}).

This definition is especially useful in the computation of limits using Taylor series. For example:

sin ⁡ x = x − x 3 3 ! + … = x + o ( x 2 )  as  x → 0 {\displaystyle \sin x=x-{\frac {x^{3}}{3!}}+\ldots =x+o(x^{2}){\text{ as }}x\to 0} ({\displaystyle \sin x=x-{\frac {x^{3}}{3!}}+\ldots =x+o(x^{2}){\text{ as }}x\to 0}), so lim x → 0 sin ⁡ x x = lim x → 0 x + o ( x 2 ) x = lim x → 0 1 + o ( x ) = 1 {\displaystyle \lim _{x\to 0}{\frac {\sin x}{x}}=\lim _{x\to 0}{\frac {x+o(x^{2})}{x}}=\lim _{x\to 0}1+o(x)=1} ({\displaystyle \lim _{x\to 0}{\frac {\sin x}{x}}=\lim _{x\to 0}{\frac {x+o(x^{2})}{x}}=\lim _{x\to 0}1+o(x)=1})

### Asymptotic notation

A relation related to little-o is the *asymptotic* notation ∼ {\displaystyle \sim } ({\displaystyle \sim }). For real valued functions f , g {\displaystyle f,g} ({\displaystyle f,g}), the expression f ( x ) ∼ g ( x )  as  x → ∞ {\displaystyle f(x)\sim g(x)\quad {\text{ as }}x\to \infty } ({\displaystyle f(x)\sim g(x)\quad {\text{ as }}x\to \infty }) means lim x → ∞ f ( x ) g ( x ) = 1. {\displaystyle \lim _{x\to \infty }{\frac {f(x)}{g(x)}}=1.} ({\displaystyle \lim _{x\to \infty }{\frac {f(x)}{g(x)}}=1.}) One can connect this to little-o by observing that f ( x ) ∼ g ( x ) {\displaystyle f(x)\sim g(x)} ({\displaystyle f(x)\sim g(x)}) is also equivalent to f ( x ) = ( 1 + o ( 1 ) ) g ( x ) {\displaystyle f(x)=(1+o(1))g(x)} ({\displaystyle f(x)=(1+o(1))g(x)}). Here o ( 1 ) {\displaystyle o(1)} ({\displaystyle o(1)}) refers to a function tending to zero as x → ∞ {\displaystyle x\to \infty } ({\displaystyle x\to \infty }). One reads this as " f ( x ) {\displaystyle f(x)} ({\displaystyle f(x)}) is *asymptotic to* g ( x ) {\displaystyle g(x)} ({\displaystyle g(x)})". For nonzero functions on the same (finite or infinite) domain, ∼ {\displaystyle \sim } ({\displaystyle \sim }) forms an equivalence relation.

One of the most famous theorems using the notation ∼ {\displaystyle \sim } ({\displaystyle \sim }) is Stirling's formula n ! ∼ ( n e ) n 2 π n  as  n → ∞ . {\displaystyle n!\sim {\bigg (}{\frac {n}{e}}{\bigg )}^{n}{\sqrt {2\pi n}}\quad {\text{ as }}n\to \infty .} ({\displaystyle n!\sim {\bigg (}{\frac {n}{e}}{\bigg )}^{n}{\sqrt {2\pi n}}\quad {\text{ as }}n\to \infty .}) In number theory, the famous prime number theorem states that π ( x ) ∼ x log ⁡ x  as  x → ∞ , {\displaystyle \pi (x)\sim {\frac {x}{\log x}}\quad {\text{ as }}x\to \infty ,} ({\displaystyle \pi (x)\sim {\frac {x}{\log x}}\quad {\text{ as }}x\to \infty ,}) where π ( x ) {\displaystyle \pi (x)} ({\displaystyle \pi (x)}) is the number of primes which are at most x {\displaystyle x} ({\displaystyle x}) and log {\displaystyle \log } ({\displaystyle \log }) is the natural logarithm of x {\displaystyle x} ({\displaystyle x}).

As with little-o, there is a version with finite limits (two-sided or one-sided) as well, for example sin ⁡ x ∼ x  as  x → 0. {\displaystyle \sin x\sim x\quad {\text{ as }}x\to 0.} ({\displaystyle \sin x\sim x\quad {\text{ as }}x\to 0.})

Further examples: x a = o a , b ( e b x )  as  x → ∞ ,  for any positive constants  a , b , {\displaystyle x^{a}=o_{a,b}(e^{bx})\quad {\text{ as }}x\to \infty ,{\text{ for any positive constants }}a,b,} ({\displaystyle x^{a}=o_{a,b}(e^{bx})\quad {\text{ as }}x\to \infty ,{\text{ for any positive constants }}a,b,}) f ( x ) = g ( x ) + o ( 1 ) ⟺ e f ( x ) ∼ e g ( x ) ( x → ∞ ) . {\displaystyle f(x)=g(x)+o(1)\quad \Longleftrightarrow \quad e^{f(x)}\sim e^{g(x)}\quad (x\to \infty ).} ({\displaystyle f(x)=g(x)+o(1)\quad \Longleftrightarrow \quad e^{f(x)}\sim e^{g(x)}\quad (x\to \infty ).}) ∑ n = 1 ∞ 1 n s ∼ 1 s − 1 ( s → 1 + ) . {\displaystyle \sum _{n=1}^{\infty }{\frac {1}{n^{s}}}\sim {\frac {1}{s-1}}\quad (s\to 1^{+}).} ({\displaystyle \sum _{n=1}^{\infty }{\frac {1}{n^{s}}}\sim {\frac {1}{s-1}}\quad (s\to 1^{+}).}) The last asymptotic is a basic property of the Riemann zeta function.

### Knuth's little 𝜔

For eventually positive, real valued functions f , g , {\displaystyle f,g,} ({\displaystyle f,g,}) the notation f ( x ) = ω ( g ( x ) )  as  x → ∞ {\displaystyle f(x)=\omega (g(x))\quad {\text{ as }}x\to \infty } ({\displaystyle f(x)=\omega (g(x))\quad {\text{ as }}x\to \infty }) means lim x → ∞ f ( x ) g ( x ) = ∞ . {\displaystyle \lim _{x\to \infty }{\frac {f(x)}{g(x)}}=\infty .} ({\displaystyle \lim _{x\to \infty }{\frac {f(x)}{g(x)}}=\infty .}) In other words, g ( x ) = o ( f ( x ) ) {\displaystyle g(x)=o(f(x))} ({\displaystyle g(x)=o(f(x))}). Roughly speaking, this means that f ( x ) {\displaystyle f(x)} ({\displaystyle f(x)}) grows much faster than does g ( x ) {\displaystyle g(x)} ({\displaystyle g(x)}).

### The Hardy–Littlewood Ω notation

In 1914 G. H. Hardy and J. E. Littlewood introduced the new symbol   Ω , {\displaystyle \ \Omega ,} ({\displaystyle \ \Omega ,}) which is defined as follows:

f

(

x

)

=

Ω

(

g

(

x

)

)

{\displaystyle f(x)=\Omega (g(x))\quad }

as

x

→

∞

{\displaystyle \quad x\to \infty \quad }

if

lim sup

x

→

∞

|

f

(

x

)

g

(

x

)

|

>

0

.

{\displaystyle \quad \limsup _{x\to \infty }\ \left|{\frac {\ f(x)\ }{g(x)}}\right|>0~.}

Thus   f ( x ) = Ω ( g ( x ) )   {\displaystyle ~f(x)=\Omega (g(x))~} ({\displaystyle ~f(x)=\Omega (g(x))~}) is the negation of   f ( x ) = o ( g ( x ) )   . {\displaystyle ~f(x)=o(g(x))~.} ({\displaystyle ~f(x)=o(g(x))~.})

In 1916 the same authors introduced the two new symbols   Ω R   {\displaystyle \ \Omega _{R}\ } ({\displaystyle \ \Omega _{R}\ }) and   Ω L   , {\displaystyle \ \Omega _{L}\ ,} ({\displaystyle \ \Omega _{L}\ ,}) defined as:

f

(

x

)

=

Ω

R

(

g

(

x

)

)

{\displaystyle f(x)=\Omega _{R}(g(x))\quad }

as

x

→

∞

{\displaystyle \quad x\to \infty \quad }

if

lim sup

x

→

∞

f

(

x

)

g

(

x

)

>

0

;

{\displaystyle \quad \limsup _{x\to \infty }\ {\frac {\ f(x)\ }{g(x)}}>0\ ;}

f

(

x

)

=

Ω

L

(

g

(

x

)

)

{\displaystyle f(x)=\Omega _{L}(g(x))\quad }

as

x

→

∞

{\displaystyle \quad x\to \infty \quad }

if

lim inf

x

→

∞

f

(

x

)

g

(

x

)

<

0

.

{\displaystyle \quad ~\liminf _{x\to \infty }\ {\frac {\ f(x)\ }{g(x)}}<0~.}

These symbols were used by E. Landau, with the same meanings, in 1924. Authors that followed Landau, however, use a different notation for the same definitions: The symbol   Ω R   {\displaystyle \ \Omega _{R}\ } ({\displaystyle \ \Omega _{R}\ }) has been replaced by the current notation   Ω +   {\displaystyle \ \Omega _{+}\ } ({\displaystyle \ \Omega _{+}\ }) with the same definition, and   Ω L   {\displaystyle \ \Omega _{L}\ } ({\displaystyle \ \Omega _{L}\ }) became   Ω −   . {\displaystyle \ \Omega _{-}~.} ({\displaystyle \ \Omega _{-}~.})

These three symbols   Ω   , Ω +   , Ω −   , {\displaystyle \ \Omega \ ,\Omega _{+}\ ,\Omega _{-}\ ,} ({\displaystyle \ \Omega \ ,\Omega _{+}\ ,\Omega _{-}\ ,}) as well as   f ( x ) = Ω ± ( g ( x ) )   {\displaystyle \ f(x)=\Omega _{\pm }(g(x))\ } ({\displaystyle \ f(x)=\Omega _{\pm }(g(x))\ }) (meaning that   f ( x ) = Ω + ( g ( x ) )   {\displaystyle \ f(x)=\Omega _{+}(g(x))\ } ({\displaystyle \ f(x)=\Omega _{+}(g(x))\ }) and   f ( x ) = Ω − ( g ( x ) )   {\displaystyle \ f(x)=\Omega _{-}(g(x))\ } ({\displaystyle \ f(x)=\Omega _{-}(g(x))\ }) are both satisfied), are now currently used in analytic number theory.

#### Simple examples

We have

sin

⁡

x

=

Ω

(

1

)

{\displaystyle \sin x=\Omega (1)\quad }

as

x

→

∞

,

{\displaystyle \quad x\to \infty \ ,}

and more precisely

sin

⁡

x

=

Ω

±

(

1

)

{\displaystyle \sin x=\Omega _{\pm }(1)\quad }

as

x

→

∞

,

{\displaystyle \quad x\to \infty ,~}

where Ω ± {\displaystyle \Omega _{\pm }} ({\displaystyle \Omega _{\pm }}) means that the left side is both Ω + ( 1 ) {\displaystyle \Omega _{+}(1)} ({\displaystyle \Omega _{+}(1)}) and Ω − ( 1 ) {\displaystyle \Omega _{-}(1)} ({\displaystyle \Omega _{-}(1)}),

We have

1

+

sin

⁡

x

=

Ω

(

1

)

{\displaystyle 1+\sin x=\Omega (1)\quad }

as

x

→

∞

,

{\displaystyle \quad x\to \infty \ ,}

and more precisely

1

+

sin

⁡

x

=

Ω

+

(

1

)

{\displaystyle 1+\sin x=\Omega _{+}(1)\quad }

as

x

→

∞

;

{\displaystyle \quad x\to \infty \ ;}

however

1

+

sin

⁡

x

≠

Ω

−

(

1

)

{\displaystyle 1+\sin x\neq \Omega _{-}(1)\quad }

as

x

→

∞

.

{\displaystyle \quad x\to \infty ~.}

### Family of Bachmann–Landau notations

For understanding the formal definitions, consult the list of logic symbols used in mathematics.

| Notation | Name | Description | Formal definition | Compact definition |
|---|---|---|---|---|
| f ( n ) = O ( g ( n ) ) {\displaystyle f(n)=O(g(n))} ({\displaystyle f(n)=O(g(n))}) or f ( n ) ≪ g ( n ) {\displaystyle f(n)\ll g(n)} ({\displaystyle f(n)\ll g(n)}) (Vinogradov's notation) | Big O; Big Oh; Big Omicron | \| f \| {\displaystyle \|f\|} ({\displaystyle \|f\|}) is bounded above by g (up to constant factor k {\displaystyle k} ({\displaystyle k})) | ∃ k > 0 ∀ n ∈ D : \| f ( n ) \| ≤ k g ( n ) {\displaystyle \exists k>0\,\forall n\in D\colon \|f(n)\|\leq k\,g(n)} ({\displaystyle \exists k>0\,\forall n\in D\colon \|f(n)\|\leq k\,g(n)}) | sup n ∈ D \| f ( n ) \| g ( n ) < ∞ {\displaystyle \sup _{n\in D}{\frac {\left\|f(n)\right\|}{g(n)}}<\infty } ({\displaystyle \sup _{n\in D}{\frac {\left\|f(n)\right\|}{g(n)}}<\infty }) |
| f ( n ) = o ( g ( n ) ) {\displaystyle f(n)=o(g(n))} ({\displaystyle f(n)=o(g(n))}) | Small O; Small Oh; Little O; Little Oh | f is dominated by g asymptotically (for any constant factor k {\displaystyle k} ({\displaystyle k})) | ∀ k > 0 ∃ n 0 ∀ n > n 0 : \| f ( n ) \| ≤ k g ( n ) {\displaystyle \forall k>0\,\exists n_{0}\,\forall n>n_{0}\colon \|f(n)\|\leq k\,g(n)} ({\displaystyle \forall k>0\,\exists n_{0}\,\forall n>n_{0}\colon \|f(n)\|\leq k\,g(n)}) | lim n → ∞ f ( n ) g ( n ) = 0 {\displaystyle \lim _{n\to \infty }{\frac {f(n)}{g(n)}}=0} ({\displaystyle \lim _{n\to \infty }{\frac {f(n)}{g(n)}}=0}) |
| f ( n ) = Ω ( g ( n ) ) {\displaystyle f(n)=\Omega (g(n))} ({\displaystyle f(n)=\Omega (g(n))}) | Big Omega in number theory (Hardy–Littlewood) | \| f \| {\displaystyle \|f\|} ({\displaystyle \|f\|}) is not dominated by g asymptotically | ∃ k > 0 ∀ n 0 ∃ n > n 0 : \| f ( n ) \| ≥ k g ( n ) {\displaystyle \exists k>0\,\forall n_{0}\,\exists n>n_{0}\colon \|f(n)\|\geq k\,g(n)} ({\displaystyle \exists k>0\,\forall n_{0}\,\exists n>n_{0}\colon \|f(n)\|\geq k\,g(n)}) | lim sup n → ∞ \| f ( n ) \| g ( n ) > 0 {\displaystyle \limsup _{n\to \infty }{\frac {\|f(n)\|}{g(n)}}>0} ({\displaystyle \limsup _{n\to \infty }{\frac {\|f(n)\|}{g(n)}}>0}) |
| f ( n ) = Ω + ( g ( n ) ) {\displaystyle f(n)=\Omega _{+}(g(n))} ({\displaystyle f(n)=\Omega _{+}(g(n))}) | Omega plus (Hardy–Littlewood) | f {\displaystyle f} ({\displaystyle f}) is not dominated by g asymptotically | ∃ k > 0 ∀ n 0 ∃ n > n 0 : f ( n ) ≥ k g ( n ) {\displaystyle \exists k>0\,\forall n_{0}\,\exists n>n_{0}\colon f(n)\geq k\,g(n)} ({\displaystyle \exists k>0\,\forall n_{0}\,\exists n>n_{0}\colon f(n)\geq k\,g(n)}) | lim sup n → ∞ f ( n ) g ( n ) > 0 {\displaystyle \limsup _{n\to \infty }{\frac {f(n)}{g(n)}}>0} ({\displaystyle \limsup _{n\to \infty }{\frac {f(n)}{g(n)}}>0}) |
| f ( n ) = Ω − ( g ( n ) ) {\displaystyle f(n)=\Omega _{-}(g(n))} ({\displaystyle f(n)=\Omega _{-}(g(n))}) | Omega minus (Hardy–Littlewood) | − f {\displaystyle -f} ({\displaystyle -f}) is not dominated by g asymptotically | ∃ k > 0 ∀ n 0 ∃ n > n 0 : − f ( n ) ≥ k g ( n ) {\displaystyle \exists k>0\,\forall n_{0}\,\exists n>n_{0}\colon -f(n)\geq k\,g(n)} ({\displaystyle \exists k>0\,\forall n_{0}\,\exists n>n_{0}\colon -f(n)\geq k\,g(n)}) | lim sup n → ∞ − f ( n ) g ( n ) > 0 {\displaystyle \limsup _{n\to \infty }{\frac {-f(n)}{g(n)}}>0} ({\displaystyle \limsup _{n\to \infty }{\frac {-f(n)}{g(n)}}>0}) |
| f ( n ) = Ω ± ( g ( n ) ) {\displaystyle f(n)=\Omega _{\pm }(g(n))} ({\displaystyle f(n)=\Omega _{\pm }(g(n))}) | Omega plus and minus | neither f {\displaystyle f} ({\displaystyle f}) nor − f {\displaystyle -f} ({\displaystyle -f}) is dominated by g asymptotically | f ( n ) = Ω + ( g ( n ) ) {\displaystyle f(n)=\Omega _{+}(g(n))} ({\displaystyle f(n)=\Omega _{+}(g(n))}) and f ( n ) = Ω − ( g ( n ) ) {\displaystyle f(n)=\Omega _{-}(g(n))} ({\displaystyle f(n)=\Omega _{-}(g(n))}) |   |
| f ( n ) ≍ g ( n ) {\displaystyle f(n)\asymp g(n)} ({\displaystyle f(n)\asymp g(n)}) (Hardy's notation) or f ( n ) = Θ ( g ( n ) ) {\displaystyle f(n)=\Theta (g(n))} ({\displaystyle f(n)=\Theta (g(n))}) (Knuth notation) | Of the same order as (Hardy); Big Theta (Knuth) | f is bounded by g both above (with constant factor k 2 {\displaystyle k_{2}} ({\displaystyle k_{2}})) and below (with constant factor k 1 {\displaystyle k_{1}} ({\displaystyle k_{1}})) | ∃ k 1 > 0 ∃ k 2 > 0 ∀ n ∈ D : {\displaystyle \exists k_{1}>0\,\exists k_{2}>0\,\forall n\in D\colon } ({\displaystyle \exists k_{1}>0\,\exists k_{2}>0\,\forall n\in D\colon }) k 1 g ( n ) ≤ f ( n ) ≤ k 2 g ( n ) {\displaystyle k_{1}\,g(n)\leq f(n)\leq k_{2}\,g(n)} ({\displaystyle k_{1}\,g(n)\leq f(n)\leq k_{2}\,g(n)}) | f ( n ) = O ( g ( n ) ) {\displaystyle f(n)=O(g(n))} ({\displaystyle f(n)=O(g(n))}) and g ( n ) = O ( f ( n ) ) {\displaystyle g(n)=O(f(n))} ({\displaystyle g(n)=O(f(n))}) |
| f ( n ) ∼ g ( n ) {\displaystyle f(n)\sim g(n)} ({\displaystyle f(n)\sim g(n)}) as n → a {\displaystyle n\to a} ({\displaystyle n\to a}), where a {\displaystyle a} ({\displaystyle a}) is finite, ∞ {\displaystyle \infty } ({\displaystyle \infty }) or − ∞ {\displaystyle -\infty } ({\displaystyle -\infty }) | Asymptotic equivalence | f is equal to g asymptotically | ∀ ε > 0 ∃ n 0 ∀ n > n 0 : \| f ( n ) g ( n ) − 1 \| < ε {\displaystyle \forall \varepsilon >0\,\exists n_{0}\,\forall n>n_{0}\colon \left\|{\frac {f(n)}{g(n)}}-1\right\|<\varepsilon } ({\displaystyle \forall \varepsilon >0\,\exists n_{0}\,\forall n>n_{0}\colon \left\|{\frac {f(n)}{g(n)}}-1\right\|<\varepsilon }) (in the case a = ∞ {\displaystyle a=\infty } ({\displaystyle a=\infty })) | lim n → a f ( n ) g ( n ) = 1 {\displaystyle \lim _{n\to a}{\frac {f(n)}{g(n)}}=1} ({\displaystyle \lim _{n\to a}{\frac {f(n)}{g(n)}}=1}) |
| f ( n ) = Ω ( g ( n ) ) {\displaystyle f(n)=\Omega (g(n))} ({\displaystyle f(n)=\Omega (g(n))}) (Knuth's notation), or f ( n ) ≫ g ( n ) {\displaystyle f(n)\gg g(n)} ({\displaystyle f(n)\gg g(n)}) (Vinogradov's notation) | Big Omega in complexity theory (Knuth) | f is bounded below by g, up to a constant factor | ∃ k > 0 ∀ n ∈ D : f ( n ) ≥ k g ( n ) {\displaystyle \exists k>0\,\forall n\in D\colon f(n)\geq k\,g(n)} ({\displaystyle \exists k>0\,\forall n\in D\colon f(n)\geq k\,g(n)}) | inf n ∈ D f ( n ) g ( n ) > 0 {\displaystyle \inf _{n\in D}{\frac {f(n)}{g(n)}}>0} ({\displaystyle \inf _{n\in D}{\frac {f(n)}{g(n)}}>0}) |
| f ( n ) = ω ( g ( n ) ) {\displaystyle f(n)=\omega (g(n))} ({\displaystyle f(n)=\omega (g(n))}) as n → a {\displaystyle n\to a} ({\displaystyle n\to a}), where a {\displaystyle a} ({\displaystyle a}) can be finite, ∞ {\displaystyle \infty } ({\displaystyle \infty }) or − ∞ {\displaystyle -\infty } ({\displaystyle -\infty }) | Small Omega; Little Omega | f dominates g asymptotically | ∀ k > 0 ∃ n 0 ∀ n > n 0 : f ( n ) > k g ( n ) {\displaystyle \forall k>0\,\exists n_{0}\,\forall n>n_{0}\colon f(n)>k\,g(n)} ({\displaystyle \forall k>0\,\exists n_{0}\,\forall n>n_{0}\colon f(n)>k\,g(n)}) (for a = ∞ {\displaystyle a=\infty } ({\displaystyle a=\infty })) | lim n → a f ( n ) g ( n ) = ∞ {\displaystyle \lim _{n\to a}{\frac {f(n)}{g(n)}}=\infty } ({\displaystyle \lim _{n\to a}{\frac {f(n)}{g(n)}}=\infty }) |

The limit definitions assume g ( n ) > 0 {\displaystyle g(n)>0} ({\displaystyle g(n)>0}) for n {\displaystyle n} ({\displaystyle n}) in a neighborhood of the limit; when the limit is ∞ {\displaystyle \infty } ({\displaystyle \infty }), this means that g ( n ) > 0 {\displaystyle g(n)>0} ({\displaystyle g(n)>0}) for sufficiently large n {\displaystyle n} ({\displaystyle n}).

Computer science and combinatorics use the big O {\displaystyle O} ({\displaystyle O}), big Theta Θ {\displaystyle \Theta } ({\displaystyle \Theta }), little o {\displaystyle o} ({\displaystyle o}), little omega ω {\displaystyle \omega } ({\displaystyle \omega }) and Knuth's big Omega Ω {\displaystyle \Omega } ({\displaystyle \Omega }) notations. Analytic number theory often uses the big O {\displaystyle O} ({\displaystyle O}), small o {\displaystyle o} ({\displaystyle o}), Hardy's ≍ {\displaystyle \asymp } ({\displaystyle \asymp }), Hardy–Littlewood's big Omega Ω {\displaystyle \Omega } ({\displaystyle \Omega }) (with or without the +, − or ± subscripts), Vinogradov's ≪ {\displaystyle \ll } ({\displaystyle \ll }) and ≫ {\displaystyle \gg } ({\displaystyle \gg }) notations and ∼ {\displaystyle \sim } ({\displaystyle \sim }) notations. The small omega ω {\displaystyle \omega } ({\displaystyle \omega }) notation is not used as often in analysis or in number theory.

### Quality of approximations using different notation

Informally, especially in computer science, the big O {\displaystyle O} ({\displaystyle O}) notation often can be used somewhat differently to describe an asymptotic tight bound where using big Theta Θ {\displaystyle \Theta } ({\displaystyle \Theta }) notation might be more factually appropriate in a given context . For example, when considering a function T ( n ) = 73 n 3 + 22 n 2 + 58 {\displaystyle T(n)=73n^{3}+22n^{2}+58} ({\displaystyle T(n)=73n^{3}+22n^{2}+58}), all of the following are generally acceptable, but tighter bounds (such as numbers 2,3 and 4 below) are usually strongly preferred over looser bounds (such as number 1 below).

1. T ( n ) = O ( n 100 ) {\displaystyle T(n)=O(n^{100})} ({\displaystyle T(n)=O(n^{100})})
2. T ( n ) = O ( n 3 ) {\displaystyle T(n)=O(n^{3})} ({\displaystyle T(n)=O(n^{3})})
3. T ( n ) = Θ ( n 3 ) {\displaystyle T(n)=\Theta (n^{3})} ({\displaystyle T(n)=\Theta (n^{3})})
4. T ( n ) ∼ 73 n 3 {\displaystyle T(n)\sim 73n^{3}} ({\displaystyle T(n)\sim 73n^{3}}) as n → ∞ {\displaystyle n\to \infty } ({\displaystyle n\to \infty }).

While all three statements are true, progressively more information is contained in each. In some fields, however, the big O notation (number 2 in the lists above) would be used more commonly than the big Theta notation (items numbered 3 in the lists above). For example, if T ( n ) {\displaystyle T(n)} ({\displaystyle T(n)}) represents the running time of a newly developed algorithm for input size n {\displaystyle n} ({\displaystyle n}), the inventors and users of the algorithm might be more inclined to put an upper bound on how long it will take to run without making an explicit statement about the lower bound or asymptotic behavior.

### Extensions to the Bachmann–Landau notations

Another notation sometimes used in computer science is O ~ {\displaystyle {\tilde {O}}} ({\displaystyle {\tilde {O}}}) (read *soft-O*), which hides polylogarithmic factors. There are two definitions in use: some authors use f ( n ) = O ~ ( g ( n ) ) {\displaystyle f(n)={\tilde {O}}(g(n))} ({\displaystyle f(n)={\tilde {O}}(g(n))}) as shorthand for f ( n ) = O ( g ( n ) log k ⁡ n ) {\displaystyle f(n)=O(g(n)\log ^{k}n)} ({\displaystyle f(n)=O(g(n)\log ^{k}n)}) for some k {\displaystyle k} ({\displaystyle k}), while others use it as shorthand for f ( n ) = O ( g ( n ) log k ⁡ g ( n ) ) {\displaystyle f(n)=O(g(n)\log ^{k}g(n))} ({\displaystyle f(n)=O(g(n)\log ^{k}g(n))}) . When g ( n ) {\displaystyle g(n)} ({\displaystyle g(n)}) is polynomial in n {\displaystyle n} ({\displaystyle n}), there is no difference; however, the latter definition allows one to say, e.g. that n 2 n = O ~ ( 2 n ) {\displaystyle n2^{n}={\tilde {O}}(2^{n})} ({\displaystyle n2^{n}={\tilde {O}}(2^{n})}) while the former definition allows for log k ⁡ n = O ~ ( 1 ) {\displaystyle \log ^{k}n={\tilde {O}}(1)} ({\displaystyle \log ^{k}n={\tilde {O}}(1)}) for any constant k {\displaystyle k} ({\displaystyle k}). Some authors write *O** for the same purpose as the latter definition. Essentially, it is less precise version of the big *O* notation, ignoring logarithmic factors in the growth-rate of the function. Since log k ⁡ n = o ( n ε ) {\displaystyle \log ^{k}n=o(n^{\varepsilon })} ({\displaystyle \log ^{k}n=o(n^{\varepsilon })}) for any constant k {\displaystyle k} ({\displaystyle k}) and any ε > 0 {\displaystyle \varepsilon >0} ({\displaystyle \varepsilon >0}), logarithmic factors are far less significant than powers of n {\displaystyle n} ({\displaystyle n}) and even more insignificant compared with exponentials.

Also, the *L* notation, defined as

L

n

[

α

,

c

]

=

e

(

c

+

o

(

1

)

)

(

ln

⁡

n

)

α

(

ln

⁡

ln

⁡

n

)

1

−

α

,

{\displaystyle L_{n}[\alpha ,c]=e^{(c+o(1))(\ln n)^{\alpha }(\ln \ln n)^{1-\alpha }},}

is convenient for functions that are between polynomial and exponential in terms of log ⁡ n {\displaystyle \log n} ({\displaystyle \log n}).

The generalization to functions taking values in any normed vector space is straightforward (replacing absolute values by norms), where f {\displaystyle f} ({\displaystyle f}) and g {\displaystyle g} ({\displaystyle g}) need not take their values in the same space. A generalization to functions g {\displaystyle g} ({\displaystyle g}) taking values in any topological group is also possible. The "limiting process" x → x 0 {\displaystyle x\to x_{0}} ({\displaystyle x\to x_{0}}) can also be generalized by introducing an arbitrary filter base, i.e. to directed nets f {\displaystyle f} ({\displaystyle f}) and g {\displaystyle g} ({\displaystyle g}). The o {\displaystyle o} ({\displaystyle o}) notation can be used to define derivatives and differentiability in quite general spaces, and also (asymptotical) equivalence of functions,

f

∼

g

⟺

(

f

−

g

)

∈

o

(

g

)

{\displaystyle f\sim g\iff (f-g)\in o(g)}

which is an equivalence relation and a more restrictive notion than the relationship " f {\displaystyle f} ({\displaystyle f}) is Θ ( g ) {\displaystyle \Theta (g)} ({\displaystyle \Theta (g)})" from above. (It reduces to lim f / g = 1 {\displaystyle \lim f/g=1} ({\displaystyle \lim f/g=1}) if f {\displaystyle f} ({\displaystyle f}) and g {\displaystyle g} ({\displaystyle g}) are positive real valued functions.) For example, 2 x = Θ ( x ) {\displaystyle 2x=\Theta (x)} ({\displaystyle 2x=\Theta (x)}) is, but 2 x − x ≠ o ( x ) {\displaystyle 2x-x\neq o(x)} ({\displaystyle 2x-x\neq o(x)}).


## History

In 1870, Paul du Bois-Reymond defined f ( x ) ≻ ϕ ( x ) {\displaystyle f(x)\succ \phi (x)} ({\displaystyle f(x)\succ \phi (x)}), f ( x ) ∼ ϕ ( x ) {\displaystyle f(x)\sim \phi (x)} ({\displaystyle f(x)\sim \phi (x)}) and f ( x ) ≺ ϕ ( x ) {\displaystyle f(x)\prec \phi (x)} ({\displaystyle f(x)\prec \phi (x)}) to mean, respectively, lim x → ∞ f ( x ) ϕ ( x ) = ∞ , lim x → ∞ f ( x ) ϕ ( x ) > 0 , lim x → ∞ f ( x ) ϕ ( x ) = 0. {\displaystyle \lim _{x\to \infty }{\frac {f(x)}{\phi (x)}}=\infty ,\quad \lim _{x\to \infty }{\frac {f(x)}{\phi (x)}}>0,\quad \lim _{x\to \infty }{\frac {f(x)}{\phi (x)}}=0.} ({\displaystyle \lim _{x\to \infty }{\frac {f(x)}{\phi (x)}}=\infty ,\quad \lim _{x\to \infty }{\frac {f(x)}{\phi (x)}}>0,\quad \lim _{x\to \infty }{\frac {f(x)}{\phi (x)}}=0.}) These were not widely adopted and are not used today. The first and third are symmetric: f ( x ) ≺ ϕ ( x ) {\displaystyle f(x)\prec \phi (x)} ({\displaystyle f(x)\prec \phi (x)}) means the same as ϕ ( x ) ≻ f ( x ) {\displaystyle \phi (x)\succ f(x)} ({\displaystyle \phi (x)\succ f(x)}). Landau later adopted ∼ {\displaystyle \sim } ({\displaystyle \sim }) with the narrower definition that the limit of f ( x ) / ϕ ( x ) {\displaystyle f(x)/\phi (x)} ({\displaystyle f(x)/\phi (x)}) equals 1.

The symbol O was first introduced by the number theorist Paul Bachmann in 1894, in the second volume of his book *Analytische Zahlentheorie* ("analytic number theory"). The number theorist Edmund Landau adopted it, and was thus inspired to introduce in 1909 the notation o; hence both are now called Landau symbols. These notations were used in applied mathematics during the 1950s for asymptotic analysis. The symbol Ω {\displaystyle \Omega } ({\displaystyle \Omega }) (in the sense "is not little *o* of") was introduced in 1914 by Hardy and Littlewood. Hardy and Littlewood also introduced in 1916 the left and right Ω {\displaystyle \Omega } ({\displaystyle \Omega }) symbols Ω R {\displaystyle \Omega _{R}} ({\displaystyle \Omega _{R}}), Ω L {\displaystyle \Omega _{L}} ({\displaystyle \Omega _{L}}) (now commonly denoted Ω + , Ω − {\displaystyle \Omega _{+},\Omega _{-}} ({\displaystyle \Omega _{+},\Omega _{-}})). This Ω {\displaystyle \Omega } ({\displaystyle \Omega }) notation has been commonly used in number theory since the 1950s.

Hardy introduced the symbols ≼ {\displaystyle \preccurlyeq } ({\displaystyle \preccurlyeq }) and advocated for Bois-Reymond's ≺ {\displaystyle \prec } ({\displaystyle \prec }) (as well as the already mentioned other symbols) in his 1910 tract "Orders of Infinity", but made use of them only in three papers (1910–1913). In his nearly 400 remaining papers and books he consistently used the Landau symbols O and o. Hardy's symbols ≼ {\displaystyle \preccurlyeq } ({\displaystyle \preccurlyeq }) and ≍ − {\displaystyle \mathbin {\,\asymp \;\;\;\;\!\!\!\!\!\!\!\!\!\!\!\!\!-} } ({\displaystyle \mathbin {\,\asymp \;\;\;\;\!\!\!\!\!\!\!\!\!\!\!\!\!-} }) are not used any more.

The symbol ∼ {\displaystyle \sim } ({\displaystyle \sim }), although it had been used before with different meanings, was given its modern definition by Landau in 1909 and by Hardy in 1910. On the same page, Hardy defined the symbol ≍ {\displaystyle \asymp } ({\displaystyle \asymp }), where f ( x ) ≍ g ( x ) {\displaystyle f(x)\asymp g(x)} ({\displaystyle f(x)\asymp g(x)}) means that both f ( x ) = O ( g ( x ) ) {\displaystyle f(x)=O(g(x))} ({\displaystyle f(x)=O(g(x))}) and g ( x ) = O ( f ( x ) ) {\displaystyle g(x)=O(f(x))} ({\displaystyle g(x)=O(f(x))}) are satisfied. The notation is still used in analytic number theory. Hardy also proposed the symbol ≍ − {\displaystyle \mathbin {\,\asymp \;\;\;\;\!\!\!\!\!\!\!\!\!\!\!\!\!-} } ({\displaystyle \mathbin {\,\asymp \;\;\;\;\!\!\!\!\!\!\!\!\!\!\!\!\!-} }), where f ≍ − g {\displaystyle f\mathbin {\,\asymp \;\;\;\;\!\!\!\!\!\!\!\!\!\!\!\!\!-} g} ({\displaystyle f\mathbin {\,\asymp \;\;\;\;\!\!\!\!\!\!\!\!\!\!\!\!\!-} g}) means that f ∼ K g {\displaystyle f\sim Kg} ({\displaystyle f\sim Kg}) for some constant K ≠ 0 {\displaystyle K\not =0} ({\displaystyle K\not =0}) (this corresponds to Bois-Reymond's notation f ∼ g {\displaystyle f\sim g} ({\displaystyle f\sim g})).

In the 1930s, Vinogradov popularized the notation f ( x ) ≪ g ( x ) {\displaystyle f(x)\ll g(x)} ({\displaystyle f(x)\ll g(x)}) and g ( x ) ≫ f ( x ) {\displaystyle g(x)\gg f(x)} ({\displaystyle g(x)\gg f(x)}), both of which mean f ( x ) = O ( g ( x ) ) {\displaystyle f(x)=O(g(x))} ({\displaystyle f(x)=O(g(x))}). This notation became standard in analytic number theory.

In the 1970s, big O was popularized in computer science by Donald Knuth, who proposed the different notation f ( x ) = Θ ( g ( x ) ) {\displaystyle f(x)=\Theta (g(x))} ({\displaystyle f(x)=\Theta (g(x))}) for Hardy's f ( x ) ≍ g ( x ) {\displaystyle f(x)\asymp g(x)} ({\displaystyle f(x)\asymp g(x)}), and proposed a different definition for the Hardy and Littlewood Omega notation.


## Matters of notation

### Arrows

In mathematics, an expression such as x → ∞ {\displaystyle x\to \infty } ({\displaystyle x\to \infty }) indicates the presence of a limit. In big-O notation and related notations Ω , Θ , ≫ , ≪ , ≍ {\displaystyle \Omega ,\Theta ,\gg ,\ll ,\asymp } ({\displaystyle \Omega ,\Theta ,\gg ,\ll ,\asymp }), there is no implied limit, in contrast with little-o, ∼ {\displaystyle \sim } ({\displaystyle \sim }) and ω {\displaystyle \omega } ({\displaystyle \omega }) notations. Notation such as f ( x ) = O ( g ( x ) ) ( x → ∞ ) {\displaystyle f(x)=O(g(x))\;\;(x\to \infty )} ({\displaystyle f(x)=O(g(x))\;\;(x\to \infty )}) can be considered an abuse of notation.

### Equals sign

Some consider f ( x ) = O ( g ( x ) ) {\displaystyle f(x)=O(g(x))} ({\displaystyle f(x)=O(g(x))}) to also be an abuse of notation, since the use of the equals sign could be misleading as it suggests a symmetry that this statement does not have. As de Bruijn says, O ( x ) = O ( x 2 ) {\displaystyle O(x)=O(x^{2})} ({\displaystyle O(x)=O(x^{2})}) is true but O ( x 2 ) = O ( x ) {\displaystyle O(x^{2})=O(x)} ({\displaystyle O(x^{2})=O(x)}) is not. Knuth describes such statements as "one-way equalities", since if the sides could be reversed, "we could deduce ridiculous things like n = n 2 {\displaystyle n=n^{2}} ({\displaystyle n=n^{2}}) from the identities n = O ( n 2 ) {\displaystyle n=O(n^{2})} ({\displaystyle n=O(n^{2})}) and n 2 = O ( n 2 ) {\displaystyle n^{2}=O(n^{2})} ({\displaystyle n^{2}=O(n^{2})}). In another letter, Knuth also pointed out that

> the equality sign is not symmetric with respect to such notations [as, in this notation,] mathematicians customarily use the '=' sign as they use the word 'is' in English: Aristotle is a man, but a man isn't necessarily Aristotle.

For these reasons, some advocate for using set notation and write f ( x ) ∈ O ( g ( x ) ) {\displaystyle f(x)\in O(g(x))} ({\displaystyle f(x)\in O(g(x))}), read as " f ( x ) {\displaystyle f(x)} ({\displaystyle f(x)}) is an element of O ( g ( x ) ) {\displaystyle O(g(x))} ({\displaystyle O(g(x))})", or " f ( x ) {\displaystyle f(x)} ({\displaystyle f(x)}) is in the set O ( g ( x ) ) {\displaystyle O(g(x))} ({\displaystyle O(g(x))})" – thinking of O ( g ( x ) ) {\displaystyle O(g(x))} ({\displaystyle O(g(x))}) as the class of all functions h ( x ) {\displaystyle h(x)} ({\displaystyle h(x)}) such that h ( x ) = O ( g ( x ) ) {\displaystyle h(x)=O(g(x))} ({\displaystyle h(x)=O(g(x))}). However, the use of the equals sign is customary. and is more convenient in more complex expressions of the form f ( x ) = g ( x ) + O ( h ( x ) ) = O ( k ( x ) ) . {\displaystyle f(x)=g(x)+O(h(x))=O(k(x)).} ({\displaystyle f(x)=g(x)+O(h(x))=O(k(x)).})

The Vinogradov notations ≪ {\displaystyle \ll } ({\displaystyle \ll }) and ≫ {\displaystyle \gg } ({\displaystyle \gg }), which are widely used in number theory do not suffer from this defect, as they more clearly indicate that big-O indicates an *inequality* rather than an *equality*. They also enjoy a symmetry that big-O notation lacks: f ( x ) ≪ g ( x ) {\displaystyle f(x)\ll g(x)} ({\displaystyle f(x)\ll g(x)}) means the same as g ( x ) ≫ f ( x ) {\displaystyle g(x)\gg f(x)} ({\displaystyle g(x)\gg f(x)}). In combinatorics and computer science, these notations are rarely seen.

### Typesetting

Big O is typeset as an italicized uppercase "O", as in the following example: O ( n 2 ) {\displaystyle O(n^{2})} ({\displaystyle O(n^{2})}). In TeX, it is produced by simply typing 'O' inside math mode. Unlike Greek-named Bachmann–Landau notations, it needs no special symbol. However, some authors use the calligraphic variant O {\displaystyle {\mathcal {O}}} ({\displaystyle {\mathcal {O}}}) instead.

The big-O originally stands for "order of" ("Ordnung", Bachmann 1894), and is thus a Latin letter. Neither Bachmann nor Landau ever call it "Omicron". The symbol was much later on (1976) viewed by Knuth as a capital omicron, probably in reference to his definition of the symbol Omega. The digit zero should not be used.
