---
title: "Taylor series (part 2/2)"
source: https://en.wikipedia.org/wiki/Taylor_series
domain: calculus
license: CC-BY-SA-4.0
tags: calculus, differential calculus, integral calculus, differentiation, antiderivative
fetched: 2026-07-02
part: 2/2
---

## List of Maclaurin series of some common functions

Several important Maclaurin series expansions follow. All these expansions are valid for complex arguments x. For multivalued complex functions, such as logarithms, fractional powers, and inverse trigonometric functions, a principal branch is understood.

### Exponential function

The exponential function *e**x* (with base e) has Maclaurin series e x = ∑ n = 0 ∞ x n n ! = 1 + x + x 2 2 ! + x 3 3 ! + ⋯ . {\displaystyle e^{x}=\sum _{n=0}^{\infty }{\frac {x^{n}}{n!}}=1+x+{\frac {x^{2}}{2!}}+{\frac {x^{3}}{3!}}+\cdots .} ({\displaystyle e^{x}=\sum _{n=0}^{\infty }{\frac {x^{n}}{n!}}=1+x+{\frac {x^{2}}{2!}}+{\frac {x^{3}}{3!}}+\cdots .}) It converges for all x.

The exponential generating function of the Bell numbers is the exponential function of the predecessor of the exponential function: exp ⁡ ( exp ⁡ x − 1 ) = ∑ n = 0 ∞ B n n ! x n {\displaystyle \exp(\exp {x}-1)=\sum _{n=0}^{\infty }{\frac {B_{n}}{n!}}x^{n}} ({\displaystyle \exp(\exp {x}-1)=\sum _{n=0}^{\infty }{\frac {B_{n}}{n!}}x^{n}})

### Natural logarithm

The natural logarithm (with base e) has Maclaurin series ln ⁡ ( 1 − x ) = − ∑ n = 1 ∞ x n n = − x − x 2 2 − x 3 3 − ⋯ , ln ⁡ ( 1 + x ) = ∑ n = 1 ∞ ( − 1 ) n + 1 x n n = x − x 2 2 + x 3 3 − ⋯ . {\displaystyle {\begin{aligned}\ln(1-x)&=-\sum _{n=1}^{\infty }{\frac {x^{n}}{n}}=-x-{\frac {x^{2}}{2}}-{\frac {x^{3}}{3}}-\cdots ,\\\ln(1+x)&=\sum _{n=1}^{\infty }(-1)^{n+1}{\frac {x^{n}}{n}}=x-{\frac {x^{2}}{2}}+{\frac {x^{3}}{3}}-\cdots .\end{aligned}}} ({\displaystyle {\begin{aligned}\ln(1-x)&=-\sum _{n=1}^{\infty }{\frac {x^{n}}{n}}=-x-{\frac {x^{2}}{2}}-{\frac {x^{3}}{3}}-\cdots ,\\\ln(1+x)&=\sum _{n=1}^{\infty }(-1)^{n+1}{\frac {x^{n}}{n}}=x-{\frac {x^{2}}{2}}+{\frac {x^{3}}{3}}-\cdots .\end{aligned}}})

The last series is known as Mercator series, named after Nicholas Mercator since it was published in his 1668 treatise *Logarithmotechnia*. Both of these series converge for |*x*| < 1. In addition, the series for ln(1 − *x*) converges for *x* = −1, and the series for ln(1 + *x*) converges for *x* = 1.

### Geometric series

The geometric series and its derivatives have Maclaurin series 1 1 − x = ∑ n = 0 ∞ x n 1 ( 1 − x ) 2 = ∑ n = 1 ∞ n x n − 1 1 ( 1 − x ) 3 = ∑ n = 2 ∞ ( n − 1 ) n 2 x n − 2 . {\displaystyle {\begin{aligned}{\frac {1}{1-x}}&=\sum _{n=0}^{\infty }x^{n}\\{\frac {1}{(1-x)^{2}}}&=\sum _{n=1}^{\infty }nx^{n-1}\\{\frac {1}{(1-x)^{3}}}&=\sum _{n=2}^{\infty }{\frac {(n-1)n}{2}}x^{n-2}.\end{aligned}}} ({\displaystyle {\begin{aligned}{\frac {1}{1-x}}&=\sum _{n=0}^{\infty }x^{n}\\{\frac {1}{(1-x)^{2}}}&=\sum _{n=1}^{\infty }nx^{n-1}\\{\frac {1}{(1-x)^{3}}}&=\sum _{n=2}^{\infty }{\frac {(n-1)n}{2}}x^{n-2}.\end{aligned}}})

All are convergent for |*x*| < 1. These are special cases of the binomial series given in the next section.

### Binomial series

The binomial series is the power series

( 1 + x ) α = ∑ n = 0 ∞ ( α n ) x n {\displaystyle (1+x)^{\alpha }=\sum _{n=0}^{\infty }{\binom {\alpha }{n}}x^{n}} ({\displaystyle (1+x)^{\alpha }=\sum _{n=0}^{\infty }{\binom {\alpha }{n}}x^{n}})

whose coefficients are the generalized binomial coefficients

( α n ) = ∏ k = 1 n α − k + 1 k = α ( α − 1 ) ⋯ ( α − n + 1 ) n ! . {\displaystyle {\binom {\alpha }{n}}=\prod _{k=1}^{n}{\frac {\alpha -k+1}{k}}={\frac {\alpha (\alpha -1)\cdots (\alpha -n+1)}{n!}}.} ({\displaystyle {\binom {\alpha }{n}}=\prod _{k=1}^{n}{\frac {\alpha -k+1}{k}}={\frac {\alpha (\alpha -1)\cdots (\alpha -n+1)}{n!}}.})

(If *n* = 0, this product is an empty product and has value 1.) It converges for |*x*| < 1 for any real or complex number α.

When *α* = −1, this is essentially the infinite geometric series mentioned in the previous section. The special cases *α* = ⁠1/2⁠ and *α* = −⁠1/2⁠ give the square root function and its inverse: ( 1 + x ) 1 2 = 1 + 1 2 x − 1 8 x 2 + 1 16 x 3 − 5 128 x 4 + 7 256 x 5 − ⋯ = ∑ n = 0 ∞ ( − 1 ) n − 1 ( 2 n ) ! 4 n ( n ! ) 2 ( 2 n − 1 ) x n , ( 1 + x ) − 1 2 = 1 − 1 2 x + 3 8 x 2 − 5 16 x 3 + 35 128 x 4 − 63 256 x 5 + ⋯ = ∑ n = 0 ∞ ( − 1 ) n ( 2 n ) ! 4 n ( n ! ) 2 x n . {\displaystyle {\begin{aligned}(1+x)^{\frac {1}{2}}&=1+{\frac {1}{2}}x-{\frac {1}{8}}x^{2}+{\frac {1}{16}}x^{3}-{\frac {5}{128}}x^{4}+{\frac {7}{256}}x^{5}-\cdots &=\sum _{n=0}^{\infty }{\frac {(-1)^{n-1}(2n)!}{4^{n}(n!)^{2}(2n-1)}}x^{n},\\(1+x)^{-{\frac {1}{2}}}&=1-{\frac {1}{2}}x+{\frac {3}{8}}x^{2}-{\frac {5}{16}}x^{3}+{\frac {35}{128}}x^{4}-{\frac {63}{256}}x^{5}+\cdots &=\sum _{n=0}^{\infty }{\frac {(-1)^{n}(2n)!}{4^{n}(n!)^{2}}}x^{n}.\end{aligned}}} ({\displaystyle {\begin{aligned}(1+x)^{\frac {1}{2}}&=1+{\frac {1}{2}}x-{\frac {1}{8}}x^{2}+{\frac {1}{16}}x^{3}-{\frac {5}{128}}x^{4}+{\frac {7}{256}}x^{5}-\cdots &=\sum _{n=0}^{\infty }{\frac {(-1)^{n-1}(2n)!}{4^{n}(n!)^{2}(2n-1)}}x^{n},\\(1+x)^{-{\frac {1}{2}}}&=1-{\frac {1}{2}}x+{\frac {3}{8}}x^{2}-{\frac {5}{16}}x^{3}+{\frac {35}{128}}x^{4}-{\frac {63}{256}}x^{5}+\cdots &=\sum _{n=0}^{\infty }{\frac {(-1)^{n}(2n)!}{4^{n}(n!)^{2}}}x^{n}.\end{aligned}}})

When only the linear term is retained, this simplifies to the binomial approximation.

### Trigonometric functions

The usual trigonometric functions and their inverses have the following Maclaurin series: sin ⁡ x = ∑ n = 0 ∞ ( − 1 ) n ( 2 n + 1 ) ! x 2 n + 1 = x − x 3 3 ! + x 5 5 ! − ⋯ for all  x cos ⁡ x = ∑ n = 0 ∞ ( − 1 ) n ( 2 n ) ! x 2 n = 1 − x 2 2 ! + x 4 4 ! − ⋯ for all  x tan ⁡ x = ∑ n = 1 ∞ B 2 n ( − 4 ) n ( 1 − 4 n ) ( 2 n ) ! x 2 n − 1 = x + x 3 3 + 2 x 5 15 + ⋯ for  | x | < π 2 sec ⁡ x = ∑ n = 0 ∞ ( − 1 ) n E 2 n ( 2 n ) ! x 2 n = 1 + x 2 2 + 5 x 4 24 + ⋯ for  | x | < π 2 arcsin ⁡ x = ∑ n = 0 ∞ ( 2 n ) ! 4 n ( n ! ) 2 ( 2 n + 1 ) x 2 n + 1 = x + x 3 6 + 3 x 5 40 + ⋯ for  | x | ≤ 1 arccos ⁡ x = π 2 − arcsin ⁡ x = π 2 − x − x 3 6 − 3 x 5 40 − ⋯ for  | x | ≤ 1 arctan ⁡ x = ∑ n = 0 ∞ ( − 1 ) n 2 n + 1 x 2 n + 1 = x − x 3 3 + x 5 5 − ⋯ for  | x | ≤ 1 ,   x ≠ ± i {\displaystyle {\begin{aligned}\sin x&=\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{(2n+1)!}}x^{2n+1}&&=x-{\frac {x^{3}}{3!}}+{\frac {x^{5}}{5!}}-\cdots &&{\text{for all }}x\\[6pt]\cos x&=\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{(2n)!}}x^{2n}&&=1-{\frac {x^{2}}{2!}}+{\frac {x^{4}}{4!}}-\cdots &&{\text{for all }}x\\[6pt]\tan x&=\sum _{n=1}^{\infty }{\frac {B_{2n}(-4)^{n}\left(1-4^{n}\right)}{(2n)!}}x^{2n-1}&&=x+{\frac {x^{3}}{3}}+{\frac {2x^{5}}{15}}+\cdots &&{\text{for }}|x|<{\frac {\pi }{2}}\\[6pt]\sec x&=\sum _{n=0}^{\infty }{\frac {(-1)^{n}E_{2n}}{(2n)!}}x^{2n}&&=1+{\frac {x^{2}}{2}}+{\frac {5x^{4}}{24}}+\cdots &&{\text{for }}|x|<{\frac {\pi }{2}}\\[6pt]\arcsin x&=\sum _{n=0}^{\infty }{\frac {(2n)!}{4^{n}(n!)^{2}(2n+1)}}x^{2n+1}&&=x+{\frac {x^{3}}{6}}+{\frac {3x^{5}}{40}}+\cdots &&{\text{for }}|x|\leq 1\\[6pt]\arccos x&={\frac {\pi }{2}}-\arcsin x&&={\frac {\pi }{2}}-x-{\frac {x^{3}}{6}}-{\frac {3x^{5}}{40}}-\cdots &&{\text{for }}|x|\leq 1\\[6pt]\arctan x&=\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{2n+1}}x^{2n+1}&&=x-{\frac {x^{3}}{3}}+{\frac {x^{5}}{5}}-\cdots &&{\text{for }}|x|\leq 1,\ x\neq \pm i\end{aligned}}} ({\displaystyle {\begin{aligned}\sin x&=\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{(2n+1)!}}x^{2n+1}&&=x-{\frac {x^{3}}{3!}}+{\frac {x^{5}}{5!}}-\cdots &&{\text{for all }}x\\[6pt]\cos x&=\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{(2n)!}}x^{2n}&&=1-{\frac {x^{2}}{2!}}+{\frac {x^{4}}{4!}}-\cdots &&{\text{for all }}x\\[6pt]\tan x&=\sum _{n=1}^{\infty }{\frac {B_{2n}(-4)^{n}\left(1-4^{n}\right)}{(2n)!}}x^{2n-1}&&=x+{\frac {x^{3}}{3}}+{\frac {2x^{5}}{15}}+\cdots &&{\text{for }}|x|<{\frac {\pi }{2}}\\[6pt]\sec x&=\sum _{n=0}^{\infty }{\frac {(-1)^{n}E_{2n}}{(2n)!}}x^{2n}&&=1+{\frac {x^{2}}{2}}+{\frac {5x^{4}}{24}}+\cdots &&{\text{for }}|x|<{\frac {\pi }{2}}\\[6pt]\arcsin x&=\sum _{n=0}^{\infty }{\frac {(2n)!}{4^{n}(n!)^{2}(2n+1)}}x^{2n+1}&&=x+{\frac {x^{3}}{6}}+{\frac {3x^{5}}{40}}+\cdots &&{\text{for }}|x|\leq 1\\[6pt]\arccos x&={\frac {\pi }{2}}-\arcsin x&&={\frac {\pi }{2}}-x-{\frac {x^{3}}{6}}-{\frac {3x^{5}}{40}}-\cdots &&{\text{for }}|x|\leq 1\\[6pt]\arctan x&=\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{2n+1}}x^{2n+1}&&=x-{\frac {x^{3}}{3}}+{\frac {x^{5}}{5}}-\cdots &&{\text{for }}|x|\leq 1,\ x\neq \pm i\end{aligned}}})

All angles are expressed in radians. The numbers *Bk* appearing in the expansions of tan *x* are the Bernoulli numbers. The *E**k* in the expansion of sec *x* are Euler numbers.

### Hyperbolic functions

The hyperbolic functions have Maclaurin series closely related to the series for the corresponding trigonometric functions: sinh ⁡ x = ∑ n = 0 ∞ x 2 n + 1 ( 2 n + 1 ) ! = x + x 3 3 ! + x 5 5 ! + ⋯ for all  x cosh ⁡ x = ∑ n = 0 ∞ x 2 n ( 2 n ) ! = 1 + x 2 2 ! + x 4 4 ! + ⋯ for all  x tanh ⁡ x = ∑ n = 1 ∞ B 2 n 4 n ( 4 n − 1 ) ( 2 n ) ! x 2 n − 1 = x − x 3 3 + 2 x 5 15 − 17 x 7 315 + ⋯ for  | x | < π 2 arsinh ⁡ x = ∑ n = 0 ∞ ( − 1 ) n ( 2 n ) ! 4 n ( n ! ) 2 ( 2 n + 1 ) x 2 n + 1 = x − x 3 6 + 3 x 5 40 − ⋯ for  | x | ≤ 1 artanh ⁡ x = ∑ n = 0 ∞ x 2 n + 1 2 n + 1 = x + x 3 3 + x 5 5 + ⋯ for  | x | ≤ 1 ,   x ≠ ± 1 {\displaystyle {\begin{aligned}\sinh x&=\sum _{n=0}^{\infty }{\frac {x^{2n+1}}{(2n+1)!}}&&=x+{\frac {x^{3}}{3!}}+{\frac {x^{5}}{5!}}+\cdots &&{\text{for all }}x\\[6pt]\cosh x&=\sum _{n=0}^{\infty }{\frac {x^{2n}}{(2n)!}}&&=1+{\frac {x^{2}}{2!}}+{\frac {x^{4}}{4!}}+\cdots &&{\text{for all }}x\\[6pt]\tanh x&=\sum _{n=1}^{\infty }{\frac {B_{2n}4^{n}\left(4^{n}-1\right)}{(2n)!}}x^{2n-1}&&=x-{\frac {x^{3}}{3}}+{\frac {2x^{5}}{15}}-{\frac {17x^{7}}{315}}+\cdots &&{\text{for }}|x|<{\frac {\pi }{2}}\\[6pt]\operatorname {arsinh} x&=\sum _{n=0}^{\infty }{\frac {(-1)^{n}(2n)!}{4^{n}(n!)^{2}(2n+1)}}x^{2n+1}&&=x-{\frac {x^{3}}{6}}+{\frac {3x^{5}}{40}}-\cdots &&{\text{for }}|x|\leq 1\\[6pt]\operatorname {artanh} x&=\sum _{n=0}^{\infty }{\frac {x^{2n+1}}{2n+1}}&&=x+{\frac {x^{3}}{3}}+{\frac {x^{5}}{5}}+\cdots &&{\text{for }}|x|\leq 1,\ x\neq \pm 1\end{aligned}}} ({\displaystyle {\begin{aligned}\sinh x&=\sum _{n=0}^{\infty }{\frac {x^{2n+1}}{(2n+1)!}}&&=x+{\frac {x^{3}}{3!}}+{\frac {x^{5}}{5!}}+\cdots &&{\text{for all }}x\\[6pt]\cosh x&=\sum _{n=0}^{\infty }{\frac {x^{2n}}{(2n)!}}&&=1+{\frac {x^{2}}{2!}}+{\frac {x^{4}}{4!}}+\cdots &&{\text{for all }}x\\[6pt]\tanh x&=\sum _{n=1}^{\infty }{\frac {B_{2n}4^{n}\left(4^{n}-1\right)}{(2n)!}}x^{2n-1}&&=x-{\frac {x^{3}}{3}}+{\frac {2x^{5}}{15}}-{\frac {17x^{7}}{315}}+\cdots &&{\text{for }}|x|<{\frac {\pi }{2}}\\[6pt]\operatorname {arsinh} x&=\sum _{n=0}^{\infty }{\frac {(-1)^{n}(2n)!}{4^{n}(n!)^{2}(2n+1)}}x^{2n+1}&&=x-{\frac {x^{3}}{6}}+{\frac {3x^{5}}{40}}-\cdots &&{\text{for }}|x|\leq 1\\[6pt]\operatorname {artanh} x&=\sum _{n=0}^{\infty }{\frac {x^{2n+1}}{2n+1}}&&=x+{\frac {x^{3}}{3}}+{\frac {x^{5}}{5}}+\cdots &&{\text{for }}|x|\leq 1,\ x\neq \pm 1\end{aligned}}})

The numbers *Bk* appearing in the series for tanh *x* are the Bernoulli numbers.

### Polylogarithmic functions

The polylogarithms have these defining identities: Li 2 ( x ) = ∑ n = 1 ∞ 1 n 2 x n Li 3 ( x ) = ∑ n = 1 ∞ 1 n 3 x n {\displaystyle {\begin{aligned}{\text{Li}}_{2}(x)&=\sum _{n=1}^{\infty }{\frac {1}{n^{2}}}x^{n}\\{\text{Li}}_{3}(x)&=\sum _{n=1}^{\infty }{\frac {1}{n^{3}}}x^{n}\end{aligned}}} ({\displaystyle {\begin{aligned}{\text{Li}}_{2}(x)&=\sum _{n=1}^{\infty }{\frac {1}{n^{2}}}x^{n}\\{\text{Li}}_{3}(x)&=\sum _{n=1}^{\infty }{\frac {1}{n^{3}}}x^{n}\end{aligned}}})

The Legendre chi functions are defined as follows: χ 2 ( x ) = ∑ n = 0 ∞ 1 ( 2 n + 1 ) 2 x 2 n + 1 χ 3 ( x ) = ∑ n = 0 ∞ 1 ( 2 n + 1 ) 3 x 2 n + 1 {\displaystyle {\begin{aligned}\chi _{2}(x)&=\sum _{n=0}^{\infty }{\frac {1}{(2n+1)^{2}}}x^{2n+1}\\\chi _{3}(x)&=\sum _{n=0}^{\infty }{\frac {1}{(2n+1)^{3}}}x^{2n+1}\end{aligned}}} ({\displaystyle {\begin{aligned}\chi _{2}(x)&=\sum _{n=0}^{\infty }{\frac {1}{(2n+1)^{2}}}x^{2n+1}\\\chi _{3}(x)&=\sum _{n=0}^{\infty }{\frac {1}{(2n+1)^{3}}}x^{2n+1}\end{aligned}}})

And the formulas presented below are called *inverse tangent integrals*: Ti 2 ( x ) = ∑ n = 0 ∞ ( − 1 ) n ( 2 n + 1 ) 2 x 2 n + 1 Ti 3 ( x ) = ∑ n = 0 ∞ ( − 1 ) n ( 2 n + 1 ) 3 x 2 n + 1 {\displaystyle {\begin{aligned}{\text{Ti}}_{2}(x)&=\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{(2n+1)^{2}}}x^{2n+1}\\{\text{Ti}}_{3}(x)&=\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{(2n+1)^{3}}}x^{2n+1}\end{aligned}}} ({\displaystyle {\begin{aligned}{\text{Ti}}_{2}(x)&=\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{(2n+1)^{2}}}x^{2n+1}\\{\text{Ti}}_{3}(x)&=\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{(2n+1)^{3}}}x^{2n+1}\end{aligned}}})

These formulas occur in statistical mechanics. Integrals encountered in Bose–Einstein and Fermi–Dirac statistics can be expressed in terms of polylogarithms. The inverse tangent integral value Ti 2 ( 1 / 3 ) {\displaystyle {\text{Ti}}_{2}(1/{\sqrt {3}})} ({\displaystyle {\text{Ti}}_{2}(1/{\sqrt {3}})}) appears in the per-site entropy of spanning trees on a large triangular lattice.

### Elliptic functions

The complete elliptic integrals of first kind K and of second kind E can be defined as follows: 2 π K ( x ) = ∑ n = 0 ∞ [ ( 2 n ) ! ] 2 16 n ( n ! ) 4 x 2 n 2 π E ( x ) = ∑ n = 0 ∞ [ ( 2 n ) ! ] 2 ( 1 − 2 n ) 16 n ( n ! ) 4 x 2 n {\displaystyle {\begin{aligned}{\frac {2}{\pi }}K(x)&=\sum _{n=0}^{\infty }{\frac {[(2n)!]^{2}}{16^{n}(n!)^{4}}}x^{2n}\\{\frac {2}{\pi }}E(x)&=\sum _{n=0}^{\infty }{\frac {[(2n)!]^{2}}{(1-2n)16^{n}(n!)^{4}}}x^{2n}\end{aligned}}} ({\displaystyle {\begin{aligned}{\frac {2}{\pi }}K(x)&=\sum _{n=0}^{\infty }{\frac {[(2n)!]^{2}}{16^{n}(n!)^{4}}}x^{2n}\\{\frac {2}{\pi }}E(x)&=\sum _{n=0}^{\infty }{\frac {[(2n)!]^{2}}{(1-2n)16^{n}(n!)^{4}}}x^{2n}\end{aligned}}})

The Jacobi theta functions describe the world of the elliptic modular functions and they have these Taylor series: ϑ 00 ( x ) = 1 + 2 ∑ n = 1 ∞ x n 2 ϑ 01 ( x ) = 1 + 2 ∑ n = 1 ∞ ( − 1 ) n x n 2 {\displaystyle {\begin{aligned}\vartheta _{00}(x)&=1+2\sum _{n=1}^{\infty }x^{n^{2}}\\\vartheta _{01}(x)&=1+2\sum _{n=1}^{\infty }(-1)^{n}x^{n^{2}}\end{aligned}}} ({\displaystyle {\begin{aligned}\vartheta _{00}(x)&=1+2\sum _{n=1}^{\infty }x^{n^{2}}\\\vartheta _{01}(x)&=1+2\sum _{n=1}^{\infty }(-1)^{n}x^{n^{2}}\end{aligned}}})
