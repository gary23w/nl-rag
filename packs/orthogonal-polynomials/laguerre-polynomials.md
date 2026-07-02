---
title: "Laguerre polynomials"
source: https://en.wikipedia.org/wiki/Laguerre_polynomials
domain: orthogonal-polynomials
license: CC-BY-SA-4.0
tags: orthogonal polynomials, hermite polynomials, chebyshev polynomials, jacobi polynomials
fetched: 2026-07-02
---

# Laguerre polynomials

In mathematics, the **Laguerre polynomials**, named after Edmond Laguerre (1834–1886), are nontrivial solutions of **Laguerre's differential equation:** $xy''+(1-x)y'+ny=0,\ y=L(x)$ which is a second-order linear differential equation. This equation has nonsingular solutions only if n is a non-negative integer.

Sometimes the name **Laguerre polynomials** is used for solutions of $xy''+(\alpha +1-x)y'+ny=0~.$ where n is still a non-negative integer. Then they are also named **generalized Laguerre polynomials**, as will be done here (alternatively **associated Laguerre polynomials** or, rarely, **Sonine polynomials**, after their inventor Nikolay Yakovlevich Sonin).

More generally, a **Laguerre function** is a solution when n is not necessarily a non-negative integer.

The Laguerre polynomials are also used for Gauss–Laguerre quadrature to numerically compute integrals of the form $\int _{0}^{\infty }f(x)e^{-x}\,dx.$

These polynomials, usually denoted *L*0, *L*1, ..., are a polynomial sequence which may be defined by the Rodrigues formula,

$L_{n}(x)={\frac {e^{x}}{n!}}{\frac {d^{n}}{dx^{n}}}\left(e^{-x}x^{n}\right)={\frac {1}{n!}}\left({\frac {d}{dx}}-1\right)^{n}x^{n},$ reducing to the closed form of a following section.

They are orthogonal polynomials with respect to an inner product $\langle f,g\rangle =\int _{0}^{\infty }f(x)g(x)e^{-x}\,dx.$

The rook polynomials in combinatorics are more or less the same as Laguerre polynomials, up to elementary changes of variables. Further see the Tricomi–Carlitz polynomials.

The Laguerre polynomials arise in quantum mechanics, in the radial part of the solution of the Schrödinger equation for a one-electron atom. They also describe the static Wigner functions of oscillator systems in quantum mechanics in phase space. They further enter in the quantum mechanics of the Morse potential and of the 3D isotropic harmonic oscillator.

Physicists sometimes use a definition for the Laguerre polynomials that is larger by a factor of *n*! than the definition used here. (Likewise, some physicists may use somewhat different definitions of the so-called associated Laguerre polynomials.)

## Recursive definition, closed form, and generating function

One can also define the Laguerre polynomials recursively, defining the first two polynomials as $L_{0}(x)=1$ $L_{1}(x)=1-x$ and then using the following recurrence relation for any *k* ≥ 1: $L_{k+1}(x)={\frac {(2k+1-x)L_{k}(x)-kL_{k-1}(x)}{k+1}}.$ Furthermore, $xL'_{n}(x)=nL_{n}(x)-nL_{n-1}(x).$

In solution of some boundary value problems, the characteristic values can be useful: $L_{k}(0)=1,L_{k}'(0)=-k.$

The **closed form** is $L_{n}(x)=\sum _{k=0}^{n}{\binom {n}{k}}{\frac {(-1)^{k}}{k!}}x^{k}.$

The generating function for them likewise follows, $\sum _{n=0}^{\infty }t^{n}L_{n}(x)={\frac {1}{1-t}}e^{-tx/(1-t)}.$ The operator form is $L_{n}(x)={\frac {1}{n!}}e^{x}{\frac {d^{n}}{dx^{n}}}(x^{n}e^{-x})$

Polynomials of negative index can be expressed using the ones with positive index: $L_{-n}(x)=e^{x}L_{n-1}(-x).$

| *n* | $L_{n}(x)\,$ |
|---|---|
| 0 | $1\,$ |
| 1 | $-x+1\,$ |
| 2 | ${\tfrac {1}{2}}(x^{2}-4x+2)\,$ |
| 3 | ${\tfrac {1}{6}}(-x^{3}+9x^{2}-18x+6)\,$ |
| 4 | ${\tfrac {1}{24}}(x^{4}-16x^{3}+72x^{2}-96x+24)\,$ |
| 5 | ${\tfrac {1}{120}}(-x^{5}+25x^{4}-200x^{3}+600x^{2}-600x+120)\,$ |
| 6 | ${\tfrac {1}{720}}(x^{6}-36x^{5}+450x^{4}-2400x^{3}+5400x^{2}-4320x+720)\,$ |
| 7 | ${\tfrac {1}{5040}}(-x^{7}+49x^{6}-882x^{5}+7350x^{4}-29400x^{3}+52920x^{2}-35280x+5040)\,$ |
| 8 | ${\tfrac {1}{40320}}(x^{8}-64x^{7}+1568x^{6}-18816x^{5}+117600x^{4}-376320x^{3}+564480x^{2}-322560x+40320)\,$ |
| 9 | ${\tfrac {1}{362880}}(-x^{9}+81x^{8}-2592x^{7}+42336x^{6}-381024x^{5}+1905120x^{4}-5080320x^{3}+6531840x^{2}-3265920x+362880)\,$ |
| 10 | ${\tfrac {1}{3628800}}(x^{10}-100x^{9}+4050x^{8}-86400x^{7}+1058400x^{6}-7620480x^{5}+31752000x^{4}-72576000x^{3}+81648000x^{2}-36288000x+3628800)\,$ |
| *n* | ${\tfrac {1}{n!}}((-x)^{n}+n^{2}(-x)^{n-1}+\dots +{\binom {n}{k}}^{2}{k!}(-x)^{n-k}+\dots +n({n!})(-x)+n!)\,$ |

## Generalized Laguerre polynomials

For arbitrary real α the polynomial solutions of the differential equation $x\,y''+\left(\alpha +1-x\right)y'+n\,y=0$ are called **generalized Laguerre polynomials**, or **associated Laguerre polynomials**.

One can also define the generalized Laguerre polynomials recursively, defining the first two polynomials as $L_{0}^{(\alpha )}(x)=1$ $L_{1}^{(\alpha )}(x)=1+\alpha -x$

and then using the following recurrence relation for any *k* ≥ 1: $L_{k+1}^{(\alpha )}(x)={\frac {(2k+1+\alpha -x)L_{k}^{(\alpha )}(x)-(k+\alpha )L_{k-1}^{(\alpha )}(x)}{k+1}}.$

The simple Laguerre polynomials are the special case *α* = 0 of the generalized Laguerre polynomials: $L_{n}^{(0)}(x)=L_{n}(x).$

The Rodrigues formula for them is $L_{n}^{(\alpha )}(x)={x^{-\alpha }e^{x} \over n!}{d^{n} \over dx^{n}}\left(e^{-x}x^{n+\alpha }\right)={\frac {x^{-\alpha }}{n!}}\left({\frac {d}{dx}}-1\right)^{n}x^{n+\alpha }.$

The generating function for them is $\sum _{n=0}^{\infty }t^{n}L_{n}^{(\alpha )}(x)={\frac {1}{(1-t)^{\alpha +1}}}e^{-tx/(1-t)}.$

### Properties

- Laguerre functions are defined by confluent hypergeometric functions and Kummer's transformation as $L_{n}^{(\alpha )}(x):={n+\alpha \choose n}M(-n,\alpha +1,x).$ where ${\textstyle {n+\alpha \choose n}}$ is a generalized binomial coefficient. When n is an integer the function reduces to a polynomial of degree n. It has the alternative expression $L_{n}^{(\alpha )}(x)={\frac {(-1)^{n}}{n!}}U(-n,\alpha +1,x)$ in terms of Kummer's function of the second kind.
- The closed form for these generalized Laguerre polynomials of degree n is $L_{n}^{(\alpha )}(x)=\sum _{i=0}^{n}(-1)^{i}{n+\alpha \choose n-i}{\frac {x^{i}}{i!}}$ derived by applying Leibniz's theorem for differentiation of a product to Rodrigues' formula.
- Laguerre polynomials have a differential operator representation, much like the closely related Hermite polynomials. Namely, let $D={\frac {d}{dx}}$ and consider the differential operator $M=xD^{2}+(\alpha +1)D$ . Then $\exp(-tM)x^{n}=(-1)^{n}t^{n}n!L_{n}^{(\alpha )}\left({\frac {x}{t}}\right)$ .
- The first few generalized Laguerre polynomials are:

| *n* | $L_{n}^{(\alpha )}(x)\,$ |
|---|---|
| 0 | $1\,$ |
| 1 | $-x+\alpha +1\,$ |
| 2 | ${\tfrac {1}{2}}(x^{2}-2\left(\alpha +2\right)x+\left(\alpha +1\right)\left(\alpha +2\right))\,$ |
| 3 | ${\tfrac {1}{6}}(-x^{3}+3\left(\alpha +3\right)x^{2}-3\left(\alpha +2\right)\left(\alpha +3\right)x+\left(\alpha +1\right)\left(\alpha +2\right)\left(\alpha +3\right))\,$ |
| 4 | ${\tfrac {1}{24}}(x^{4}-4\left(\alpha +4\right)x^{3}+6\left(\alpha +3\right)\left(\alpha +4\right)x^{2}-4\left(\alpha +2\right)\cdots \left(\alpha +4\right)x+\left(\alpha +1\right)\cdots \left(\alpha +4\right))\,$ |
| 5 | ${\tfrac {1}{120}}(-x^{5}+5\left(\alpha +5\right)x^{4}-10\left(\alpha +4\right)\left(\alpha +5\right)x^{3}+10\left(\alpha +3\right)\cdots \left(\alpha +5\right)x^{2}-5\left(\alpha +2\right)\cdots \left(\alpha +5\right)x+\left(\alpha +1\right)\cdots \left(\alpha +5\right))\,$ |
| 6 | ${\tfrac {1}{720}}(x^{6}-6\left(\alpha +6\right)x^{5}+15\left(\alpha +5\right)\left(\alpha +6\right)x^{4}-20\left(\alpha +4\right)\cdots \left(\alpha +6\right)x^{3}+15\left(\alpha +3\right)\cdots \left(\alpha +6\right)x^{2}-6\left(\alpha +2\right)\cdots \left(\alpha +6\right)x+\left(\alpha +1\right)\cdots \left(\alpha +6\right))\,$ |
| 7 | ${\tfrac {1}{5040}}(-x^{7}+7\left(\alpha +7\right)x^{6}-21\left(\alpha +6\right)\left(\alpha +7\right)x^{5}+35\left(\alpha +5\right)\cdots \left(\alpha +7\right)x^{4}-35\left(\alpha +4\right)\cdots \left(\alpha +7\right)x^{3}+21\left(\alpha +3\right)\cdots \left(\alpha +7\right)x^{2}-7\left(\alpha +2\right)\cdots \left(\alpha +7\right)x+\left(\alpha +1\right)\cdots \left(\alpha +7\right))\,$ |
| 8 | ${\tfrac {1}{40320}}(x^{8}-8\left(\alpha +8\right)x^{7}+28\left(\alpha +7\right)\left(\alpha +8\right)x^{6}-56\left(\alpha +6\right)\cdots \left(\alpha +8\right)x^{5}+70\left(\alpha +5\right)\cdots \left(\alpha +8\right)x^{4}-56\left(\alpha +4\right)\cdots \left(\alpha +8\right)x^{3}+28\left(\alpha +3\right)\cdots \left(\alpha +8\right)x^{2}-8\left(\alpha +2\right)\cdots \left(\alpha +8\right)x+\left(\alpha +1\right)\cdots \left(\alpha +8\right))\,$ |
| 9 | ${\tfrac {1}{362880}}(-x^{9}+9\left(\alpha +9\right)x^{8}-36\left(\alpha +8\right)\left(\alpha +9\right)x^{7}+84\left(\alpha +7\right)\cdots \left(\alpha +9\right)x^{6}-126\left(\alpha +6\right)\cdots \left(\alpha +9\right)x^{5}+126\left(\alpha +5\right)\cdots \left(\alpha +9\right)x^{4}-84\left(\alpha +4\right)\cdots \left(\alpha +9\right)x^{3}+36\left(\alpha +3\right)\cdots \left(\alpha +9\right)x^{2}-9\left(\alpha +2\right)\cdots \left(\alpha +9\right)x+\left(\alpha +1\right)\cdots \left(\alpha +9\right))\,$ |
| 10 | ${\tfrac {1}{3628800}}(x^{10}-10\left(\alpha +10\right)x^{9}+45\left(\alpha +9\right)\left(\alpha +10\right)x^{8}-120\left(\alpha +8\right)\cdots \left(\alpha +10\right)x^{7}+210\left(\alpha +7\right)\cdots \left(\alpha +10\right)x^{6}-252\left(\alpha +6\right)\cdots \left(\alpha +10\right)x^{5}+210\left(\alpha +5\right)\cdots \left(\alpha +10\right)x^{4}-120\left(\alpha +4\right)\cdots \left(\alpha +10\right)x^{3}+45\left(\alpha +3\right)\cdots \left(\alpha +10\right)x^{2}-10\left(\alpha +2\right)\cdots \left(\alpha +10\right)x+\left(\alpha +1\right)\cdots \left(\alpha +10\right))\,$ |

- The coefficient of the leading term is (−1)*n*/*n*!;
- The constant term, which is the value at 0, is $L_{n}^{(\alpha )}(0)={n+\alpha \choose n}={\frac {\Gamma (n+\alpha +1)}{n!\,\Gamma (\alpha +1)}};$
- The discriminant is $\operatorname {Disc} \left(L_{n}^{(\alpha )}\right)=\prod _{j=1}^{n}j^{j-2n+2}(j+\alpha )^{j-1}$

### As a contour integral

Given the generating function specified above, the polynomials may be expressed in terms of a contour integral $L_{n}^{(\alpha )}(x)={\frac {1}{2\pi i}}\oint _{C}{\frac {e^{-xt/(1-t)}}{(1-t)^{\alpha +1}\,t^{n+1}}}\;dt,$ where the contour circles the origin once in a counterclockwise direction without enclosing the essential singularity at 1

### Recurrence relations

The addition formula for Laguerre polynomials: $L_{n}^{(\alpha _{1}+\dots +\alpha _{r}+r-1)}\left(x_{1}+\dots +x_{r}\right)=\sum _{m_{1}+\dots +m_{r}=n}L_{m_{1}}^{(\alpha _{1})}\left(x_{1}\right)\cdots L_{m_{r}}^{(\alpha _{r})}\left(x_{r}\right).$ Laguerre's polynomials satisfy the recurrence relations $L_{n}^{(\alpha )}(x)=\sum _{i=0}^{n}L_{n-i}^{(\alpha +i)}(y){\frac {(y-x)^{i}}{i!}},$ in particular $L_{n}^{(\alpha +1)}(x)=\sum _{i=0}^{n}L_{i}^{(\alpha )}(x)$ and $L_{n}^{(\alpha )}(x)=\sum _{i=0}^{n}{\alpha -\beta +n-i-1 \choose n-i}L_{i}^{(\beta )}(x),$ or $L_{n}^{(\alpha )}(x)=\sum _{i=0}^{n}{\alpha -\beta +n \choose n-i}L_{i}^{(\beta -i)}(x);$ moreover ${\begin{aligned}L_{n}^{(\alpha )}(x)-\sum _{j=0}^{\Delta -1}{n+\alpha \choose n-j}(-1)^{j}{\frac {x^{j}}{j!}}&=(-1)^{\Delta }{\frac {x^{\Delta }}{(\Delta -1)!}}\sum _{i=0}^{n-\Delta }{\frac {n+\alpha \choose n-\Delta -i}{(n-i){n \choose i}}}L_{i}^{(\alpha +\Delta )}(x)\\[6pt]&=(-1)^{\Delta }{\frac {x^{\Delta }}{(\Delta -1)!}}\sum _{i=0}^{n-\Delta }{\frac {n+\alpha -i-1 \choose n-\Delta -i}{(n-i){n \choose i}}}L_{i}^{(n+\alpha +\Delta -i)}(x)\end{aligned}}$

They can be used to derive the four 3-point-rules ${\begin{aligned}L_{n}^{(\alpha )}(x)&=L_{n}^{(\alpha +1)}(x)-L_{n-1}^{(\alpha +1)}(x)=\sum _{j=0}^{k}{k \choose j}(-1)^{j}L_{n-j}^{(\alpha +k)}(x),\\[10pt]nL_{n}^{(\alpha )}(x)&=(n+\alpha )L_{n-1}^{(\alpha )}(x)-xL_{n-1}^{(\alpha +1)}(x),\\[10pt]&{\text{or }}\\{\frac {x^{k}}{k!}}L_{n}^{(\alpha )}(x)&=\sum _{i=0}^{k}(-1)^{i}{n+i \choose i}{n+\alpha \choose k-i}L_{n+i}^{(\alpha -k)}(x),\\[10pt]nL_{n}^{(\alpha +1)}(x)&=(n-x)L_{n-1}^{(\alpha +1)}(x)+(n+\alpha )L_{n-1}^{(\alpha )}(x)\\[10pt]xL_{n}^{(\alpha +1)}(x)&=(n+\alpha )L_{n-1}^{(\alpha )}(x)-(n-x)L_{n}^{(\alpha )}(x);\end{aligned}}$

combined they give this additional, useful recurrence relations ${\begin{aligned}L_{n}^{(\alpha )}(x)&=\left(2+{\frac {\alpha -1-x}{n}}\right)L_{n-1}^{(\alpha )}(x)-\left(1+{\frac {\alpha -1}{n}}\right)L_{n-2}^{(\alpha )}(x)\\[10pt]&={\frac {\alpha +1-x}{n}}L_{n-1}^{(\alpha +1)}(x)-{\frac {x}{n}}L_{n-2}^{(\alpha +2)}(x)\end{aligned}}$

Since $L_{n}^{(\alpha )}(x)$ is a monic polynomial of degree n in $\alpha$ , there is the partial fraction decomposition ${\begin{aligned}{\frac {n!\,L_{n}^{(\alpha )}(x)}{(\alpha +1)_{n}}}&=1-\sum _{j=1}^{n}(-1)^{j}{\frac {j}{\alpha +j}}{n \choose j}L_{n}^{(-j)}(x)\\&=1-\sum _{j=1}^{n}{\frac {x^{j}}{\alpha +j}}\,\,{\frac {L_{n-j}^{(j)}(x)}{(j-1)!}}\\&=1-x\sum _{i=1}^{n}{\frac {L_{n-i}^{(-\alpha )}(x)L_{i-1}^{(\alpha +1)}(-x)}{\alpha +i}}.\end{aligned}}$ The second equality follows by the following identity, valid for integer *i* and n and immediate from the expression of $L_{n}^{(\alpha )}(x)$ in terms of Charlier polynomials: ${\frac {(-x)^{i}}{i!}}L_{n}^{(i-n)}(x)={\frac {(-x)^{n}}{n!}}L_{i}^{(n-i)}(x).$ For the third equality apply the fourth and fifth identities of this section.

### Derivatives

Differentiating the power series representation of a generalized Laguerre polynomial k times leads to ${\frac {d^{k}}{dx^{k}}}L_{n}^{(\alpha )}(x)={\begin{cases}(-1)^{k}L_{n-k}^{(\alpha +k)}(x)&{\text{if }}k\leq n,\\0&{\text{otherwise.}}\end{cases}}$

This points to a special case (*α* = 0) of the formula above: for integer *α* = *k* the generalized polynomial may be written $L_{n}^{(k)}(x)=(-1)^{k}{\frac {d^{k}L_{n+k}(x)}{dx^{k}}},$ the shift by k sometimes causing confusion with the usual parenthesis notation for a derivative.

Moreover, the following equation holds: ${\frac {1}{k!}}{\frac {d^{k}}{dx^{k}}}x^{\alpha }L_{n}^{(\alpha )}(x)={n+\alpha \choose k}x^{\alpha -k}L_{n}^{(\alpha -k)}(x),$ which generalizes with Cauchy's formula to $L_{n}^{(\alpha ')}(x)=(\alpha '-\alpha ){\alpha '+n \choose \alpha '-\alpha }\int _{0}^{x}{\frac {t^{\alpha }(x-t)^{\alpha '-\alpha -1}}{x^{\alpha '}}}L_{n}^{(\alpha )}(t)\,dt.$

The derivative with respect to the second variable α has the form, ${\frac {d}{d\alpha }}L_{n}^{(\alpha )}(x)=\sum _{i=0}^{n-1}{\frac {L_{i}^{(\alpha )}(x)}{n-i}}.$ The generalized Laguerre polynomials obey the differential equation $xL_{n}^{(\alpha )\prime \prime }(x)+(\alpha +1-x)L_{n}^{(\alpha )\prime }(x)+nL_{n}^{(\alpha )}(x)=0,$ which may be compared with the equation obeyed by the *k*th derivative of the ordinary Laguerre polynomial,

$xL_{n}^{[k]\prime \prime }(x)+(k+1-x)L_{n}^{[k]\prime }(x)+(n-k)L_{n}^{[k]}(x)=0,$ where $L_{n}^{[k]}(x)\equiv {\frac {d^{k}L_{n}(x)}{dx^{k}}}$ for this equation only.

In Sturm–Liouville form the differential equation is

$-\left(x^{\alpha +1}e^{-x}\cdot L_{n}^{(\alpha )}(x)^{\prime }\right)'=n\cdot x^{\alpha }e^{-x}\cdot L_{n}^{(\alpha )}(x),$

which shows that *L**(α)* *n* is an eigenvector for the eigenvalue n.

### Orthogonality

The generalized Laguerre polynomials are orthogonal over [0, ∞) with respect to the measure with weighting function *xα* *e*−*x*:

$\int _{0}^{\infty }x^{\alpha }e^{-x}L_{n}^{(\alpha )}(x)L_{m}^{(\alpha )}(x)dx={\frac {\Gamma (n+\alpha +1)}{n!}}\delta _{n,m},$

which follows from

$\int _{0}^{\infty }x^{\alpha '-1}e^{-x}L_{n}^{(\alpha )}(x)dx={\alpha -\alpha '+n \choose n}\Gamma (\alpha ').$

If $\Gamma (x,\alpha +1,1)$ denotes the gamma distribution then the orthogonality relation can be written as

$\int _{0}^{\infty }L_{n}^{(\alpha )}(x)L_{m}^{(\alpha )}(x)\Gamma (x,\alpha +1,1)dx={n+\alpha \choose n}\delta _{n,m}.$

The associated, symmetric kernel polynomial has the representations (Christoffel–Darboux formula)

${\begin{aligned}K_{n}^{(\alpha )}(x,y)&:={\frac {1}{\Gamma (\alpha +1)}}\sum _{i=0}^{n}{\frac {L_{i}^{(\alpha )}(x)L_{i}^{(\alpha )}(y)}{\alpha +i \choose i}}\\[4pt]&={\frac {1}{\Gamma (\alpha +1)}}{\frac {L_{n}^{(\alpha )}(x)L_{n+1}^{(\alpha )}(y)-L_{n+1}^{(\alpha )}(x)L_{n}^{(\alpha )}(y)}{{\frac {x-y}{n+1}}{n+\alpha \choose n}}}\\[4pt]&={\frac {1}{\Gamma (\alpha +1)}}\sum _{i=0}^{n}{\frac {x^{i}}{i!}}{\frac {L_{n-i}^{(\alpha +i)}(x)L_{n-i}^{(\alpha +i+1)}(y)}{{\alpha +n \choose n}{n \choose i}}};\end{aligned}}$

recursively

$K_{n}^{(\alpha )}(x,y)={\frac {y}{\alpha +1}}K_{n-1}^{(\alpha +1)}(x,y)+{\frac {1}{\Gamma (\alpha +1)}}{\frac {L_{n}^{(\alpha +1)}(x)L_{n}^{(\alpha )}(y)}{\alpha +n \choose n}}.$

Moreover,

$y^{\alpha }e^{-y}K_{n}^{(\alpha )}(\cdot ,y)\to \delta (y-\cdot ).$

Turán's inequalities can be derived here, which is $L_{n}^{(\alpha )}(x)^{2}-L_{n-1}^{(\alpha )}(x)L_{n+1}^{(\alpha )}(x)=\sum _{k=0}^{n-1}{\frac {\alpha +n-1 \choose n-k}{n{n \choose k}}}L_{k}^{(\alpha -1)}(x)^{2}>0.$

The following integral is needed in the quantum mechanical treatment of the hydrogen atom,

$\int _{0}^{\infty }x^{\alpha +1}e^{-x}\left[L_{n}^{(\alpha )}(x)\right]^{2}dx={\frac {(n+\alpha )!}{n!}}(2n+\alpha +1).$

### Series expansions

Let a function have the (formal) series expansion $f(x)=\sum _{i=0}^{\infty }f_{i}^{(\alpha )}L_{i}^{(\alpha )}(x).$

Then $f_{i}^{(\alpha )}=\int _{0}^{\infty }{\frac {L_{i}^{(\alpha )}(x)}{i+\alpha \choose i}}\cdot {\frac {x^{\alpha }e^{-x}}{\Gamma (\alpha +1)}}\cdot f(x)\,dx.$

The series converges in the associated Hilbert space *L*2[0, ∞) if and only if

$\|f\|_{L^{2}}^{2}:=\int _{0}^{\infty }{\frac {x^{\alpha }e^{-x}}{\Gamma (\alpha +1)}}|f(x)|^{2}\,dx=\sum _{i=0}^{\infty }{i+\alpha \choose i}|f_{i}^{(\alpha )}|^{2}<\infty .$

#### Further examples of expansions

Monomials are represented as ${\frac {x^{n}}{n!}}=\sum _{i=0}^{n}(-1)^{i}{n+\alpha \choose n-i}L_{i}^{(\alpha )}(x),$ while binomials have the parametrization ${n+x \choose n}=\sum _{i=0}^{n}{\frac {\alpha ^{i}}{i!}}L_{n-i}^{(x+i)}(\alpha ).$

This leads directly to $e^{-\gamma x}=\sum _{i=0}^{\infty }{\frac {\gamma ^{i}}{(1+\gamma )^{i+\alpha +1}}}L_{i}^{(\alpha )}(x)\qquad {\text{convergent iff }}\Re (\gamma )>-{\tfrac {1}{2}}$ for the exponential function. The incomplete gamma function has the representation $\Gamma (\alpha ,x)=x^{\alpha }e^{-x}\sum _{i=0}^{\infty }{\frac {L_{i}^{(\alpha )}(x)}{1+i}}\qquad \left(\Re (\alpha )>-1,x>0\right).$

### Asymptotics

#### In terms of elementary functions

For any fixed positive integer M , fixed real number $\alpha$ , fixed and bounded interval $[c,d]\subset (0,+\infty )$ , uniformly for $x\in [c,d]$ , at $n\to \infty$ : $L_{n}^{(\alpha )}\left(x\right)={\frac {n^{{\frac {1}{2}}\alpha -{\frac {1}{4}}}{\mathrm {e} }^{{\frac {1}{2}}x}}{{\pi }^{\frac {1}{2}}x^{{\frac {1}{2}}\alpha +{\frac {1}{4}}}}}\left(\cos \theta _{n}^{(\alpha )}(x)\left(\sum _{m=0}^{M-1}{\frac {a_{m}(x)}{n^{{\frac {1}{2}}m}}}+O\left({\frac {1}{n^{{\frac {1}{2}}M}}}\right)\right)+\sin \theta _{n}^{(\alpha )}(x)\left(\sum _{m=1}^{M-1}{\frac {b_{m}(x)}{n^{{\frac {1}{2}}m}}}+O\left({\frac {1}{n^{{\frac {1}{2}}M}}}\right)\right)\right)$ where $\theta _{n}^{(\alpha )}(x):=2(nx)^{\frac {1}{2}}-\left({\tfrac {1}{2}}\alpha +{\tfrac {1}{4}}\right)\pi .$ and $a_{0},b_{1},a_{1},b_{2},\dots$ are functions depending on $\alpha ,x$ but not n , and regular for $x>0$ . The first few ones are: ${\begin{aligned}&a_{0}(x)=1\\&a_{1}(x)=0\\&b_{1}(x)={\frac {1}{48x^{\frac {1}{2}}}}\left(4x^{2}-24(\alpha +1)x+3-12\alpha ^{2}\right)\end{aligned}}$ This is Perron's formula. There is also a generalization for $x\in \mathbb {C} \setminus [0,\infty )$ . Fejér's formula is a special case of Perron's formula with $M=1$ .

#### In terms of Bessel functions

The Mehler–Heine formula states:

$\lim _{n\to \infty }n^{-\alpha }L_{n}^{(\alpha )}\left({\frac {z^{2}}{4n}}\right)=\left({\frac {z}{2}}\right)^{-\alpha }J_{\alpha }(z),$

where $J_{\alpha }$ is a Bessel function of the first kind.

See also:.

#### In terms of Airy functions

Let $\nu =4n+2\alpha +2$ . Let $\operatorname {Ai}$ be the Airy function. Let $\alpha$ be arbitrary and real, $\epsilon$ and $\omega$ be positive and fixed.

The Plancherel–Rotach asymptotics formulas:

- for $x=\nu \cos ^{2}\varphi$ and $\epsilon \leq \varphi \leq {\tfrac {\pi }{2}}-\epsilon n^{-1/2}$ , uniformly at $n\to \infty$ :

$e^{-x/2}L_{n}^{(\alpha )}(x)=(-1)^{n}(\pi \sin \varphi )^{-1/2}x^{-\alpha /2-1/4}n^{\alpha /2-1/4}{\big \{}\sin \left[\left(n+{\tfrac {\alpha +1}{2}}\right)(\sin 2\varphi -2\varphi )+3\pi /4\right]+(nx)^{-1/2}{\mathcal {O}}(1){\big \}}$

- for $x=\nu \cosh ^{2}\varphi$ and $\epsilon \leq \varphi \leq \omega$ , uniformly at $n\to \infty$ :

$e^{-x/2}L_{n}^{(\alpha )}(x)={\tfrac {1}{2}}(-1)^{n}(\pi \sinh \varphi )^{-1/2}x^{-\alpha /2-1/4}n^{\alpha /2-1/4}\exp \left[\left(n+{\tfrac {\alpha +1}{2}}\right)(2\varphi -\sinh 2\varphi )\right]\{1+{\mathcal {O}}\left(n^{-1}\right)\}$

- for $x=\nu -2(2n/3)^{1/3}t$ and t complex and bounded, uniformly at $n\to \infty$ :

$e^{-x/2}L_{n}^{(\alpha )}(x)=(-1)^{n}\pi ^{-1}2^{-\alpha -1/3}3^{1/3}n^{-1/3}{\bigg \{}\pi \operatorname {Ai} (-3^{-1/3}t)+{\mathcal {O}}\left(n^{-2/3}\right){\bigg \}}$

See DLMF for higher-order terms.

## Zeroes

### Notation

$j_{\alpha ,m}$ is the m -th positive zero of the Bessel function $J_{\alpha }(x)$ .

$a_{m}$ is the m -th zero of the Airy function $\operatorname {Ai} (x)$ , in descending order: $0>a_{1}>a_{2}>\cdots$ .

$\nu =4n+2\alpha +2$ .

If $\alpha >-1$ , then $L_{n}^{(\alpha )}$ has n real roots. Thus in this section we assume $\alpha >-1$ by default.

$x_{1}<\dots <x_{n}$ are the real roots of $L_{n}^{(\alpha )}$ .

Note that $\left((-1)^{n-i}L_{n-i}^{(\alpha )}\right)_{i=0}^{n}$ is a Sturm chain.

### Inequalities

For $\alpha >-1$ , we have these bounds:

- $x_{1}<{\frac {(\alpha +1)(\alpha +2)}{n+\alpha +1}}$
- $x_{1}<{\frac {(\alpha +1)(\alpha +3)}{2n+\alpha +1}}$
- $x_{1}<{\frac {(\alpha +1)(\alpha +2)(\alpha +4)(2n+\alpha +1)}{(\alpha +1)^{2}(\alpha +2)+n(5\alpha +11)(n+\alpha +1)}}$
- $x_{n}\leq 2n+\alpha -1+2{\sqrt {(n-2)(n+\alpha -1)}}$ when $n\geq 2$
- $x_{n}>4n+\alpha -16{\sqrt {2n}}$
- $x_{n}>3n-4$
- $x_{n}>2n+\alpha -1$
- $x_{n}>2n+\alpha -2+{\sqrt {n^{2}-2n+\alpha n+2}}$
- ${\begin{aligned}&(n+2)x_{1}&\geq \left(n-1-{\sqrt {n^{2}+(n+2)(\alpha +1)}}\right)^{2}-1\\&(n+2)x_{n}&\leq \left(n-1+{\sqrt {n^{2}+(n+2)(\alpha +1)}}\right)^{2}-1\end{aligned}}$
- ${\begin{aligned}x_{1}&>{\frac {1}{2}}\nu -3-{\sqrt {1+4(n-1)(n+\alpha -1)}}\\x_{n}&<{\frac {1}{2}}\nu -3+{\sqrt {1+4(n-1)(n+\alpha -1)}}\end{aligned}}$

For fixed $k=1,\dots ,n$ , ${\begin{aligned}\nu x_{k}&>j_{\alpha ,k}^{2}\\x_{k}&<{\frac {j_{\alpha ,k}^{2}}{\nu /2+{\sqrt {(\nu /2)^{2}-j_{\alpha ,k}^{2}}}}}\quad {\text{ if }}\nu /2>j_{\alpha ,k}\\x_{k}&<\left[\nu ^{1/2}+2^{-1/3}\nu ^{-1/6}a_{n-k+1}\right]^{2}\quad {\text{ if }}|\alpha |\geqslant 1/4\\x_{k}&<\nu +2^{\frac {2}{3}}a_{k}\nu ^{\frac {1}{3}}+2^{-{\frac {2}{3}}}a_{k}^{2}\nu ^{-{\frac {1}{3}}}\end{aligned}}$ For fixed k , we have $\lim _{n\to \infty }\nu x_{k}=j_{\alpha ,k}^{2}$ , so the first inequality is sharp.

See also.

### Electrostatics

The zeroes satisfy the **Stieltjes relations**: ${\begin{aligned}\sum _{1\leq j\leq n,i\neq j}{\frac {1}{x_{i}-x_{j}}}&={\frac {1}{2}}\left(1-{\frac {\alpha +1}{x_{i}}}\right)\\\sum _{1\leq j\leq n}{\frac {1}{x_{j}}}&={\frac {n}{\alpha +1}}\\\sum _{1\leq j\leq n,i\neq j}{\frac {1}{(x_{i}-x_{j})^{2}}}&=-{\frac {(\alpha +1)(\alpha +5)}{12x_{i}^{2}}}+{\frac {2n+\alpha +1}{6x_{i}}}-{\frac {1}{12}}\\\sum _{1\leq j\leq n,i\neq j}{\frac {1}{(x_{i}-x_{j})^{3}}}&=-{\frac {(\alpha +1)(\alpha +3)}{8x_{i}^{3}}}+{\frac {2n+\alpha +1}{8x_{i}^{2}}}\\\end{aligned}}$ The first relation can be interpreted physically. Fix an electric particle at origin with charge $+{\frac {\alpha +1}{2}}$ , and produce a constant electric field of strength $-{\frac {1}{2}}$ . Then, place n electric particles with charge $+1$ . The first relation states that the zeroes of $L_{n}^{(\alpha )}$ are the equilibrium positions of the particles.

As the zeroes specify the polynomial up to scaling, this provides an alternative way to uniquely characterize the Laguerre polynomials.

The zeroes also satisfy $\sum _{i=1}^{n}{\frac {1}{x-x_{i}}}=-\sum _{k=0}^{\infty }S_{k+1}x^{k},\quad S_{k}:=\sum _{i=1}^{n}x_{i}^{-k}$ which allows the following bound $S_{m}^{-1/m}<x_{1}<S_{m}/S_{m+1},\quad m=1,2,\ldots$

### Limit distribution

Let $F_{n}(t):={\frac {1}{n}}\#\{i:x_{i}\leq t\}$ be the cumulative distribution function for the roots, then we have the limit law $\lim _{n\to \infty }F_{n}(4nt)={\frac {2}{\pi }}\int _{0}^{t}{\sqrt {\frac {1-s}{s}}}ds\quad \forall t\in (0,1]$ which can be interpreted as the limit distribution of the Wishart ensemble spectrum.

For fixed $\alpha >-1$ and fixed k , as $n\to \infty$ , ${\begin{aligned}x_{n+1-k}=&\nu +2^{2/3}a_{k}\nu ^{1/3}+{\frac {1}{5}}2^{4/3}a_{k}^{2}\nu ^{-1/3}+\left({\frac {11}{35}}-\alpha ^{2}-{\frac {12}{175}}a_{k}^{3}\right)\nu ^{-1}\\&+\left({\frac {16}{1575}}a_{k}+{\frac {92}{7875}}a_{k}^{4}\right)2^{2/3}\nu ^{-5/3}-\left({\frac {15152}{3031875}}a_{k}^{5}+{\frac {1088}{121275}}a_{k}^{2}\right)2^{1/3}\nu ^{-7/3}+{\mathcal {O}}\left(\nu ^{-3}\right),\end{aligned}}$

For $\alpha \in (-1,0)$ , ${\begin{aligned}x_{1}={\frac {\alpha +1}{n}}&+{\frac {n-1}{2}}\left({\frac {\alpha +1}{n}}\right)^{2}-{\frac {n^{2}+3n-4}{12}}\left({\frac {\alpha +1}{n}}\right)^{3}\\&+{\frac {7n^{3}+6n^{2}+23n-36}{144}}\left({\frac {\alpha +1}{n}}\right)^{4}\\&-{\frac {293n^{4}+210n^{3}+235n^{2}+990n-1728}{8640}}\left({\frac {\alpha +1}{n}}\right)^{5}+\cdots \end{aligned}}$

## In quantum mechanics

In quantum mechanics the Schrödinger equation for the hydrogen-like atom is exactly solvable by separation of variables in spherical coordinates. The radial part of the wave function is a (generalized) Laguerre polynomial.

Vibronic transitions in the Franck-Condon approximation can also be described using Laguerre polynomials.

## Multiplication theorems

Erdélyi gives the following two multiplication theorems

${\begin{aligned}&t^{n+1+\alpha }e^{(1-t)z}L_{n}^{(\alpha )}(zt)=\sum _{k=n}^{\infty }{k \choose n}\left(1-{\frac {1}{t}}\right)^{k-n}L_{k}^{(\alpha )}(z),\\[6pt]&e^{(1-t)z}L_{n}^{(\alpha )}(zt)=\sum _{k=0}^{\infty }{\frac {(1-t)^{k}z^{k}}{k!}}L_{n}^{(\alpha +k)}(z).\end{aligned}}$

## Relation to Hermite polynomials

The generalized Laguerre polynomials are related to the Hermite polynomials: ${\begin{aligned}H_{2n}(x)&=(-1)^{n}2^{2n}n!L_{n}^{(-1/2)}(x^{2})\\[4pt]H_{2n+1}(x)&=(-1)^{n}2^{2n+1}n!xL_{n}^{(1/2)}(x^{2})\end{aligned}}$ where the *H**n*(*x*) are the Hermite polynomials based on the weighting function exp(−*x*2), the so-called "physicist's version."

Because of this, the generalized Laguerre polynomials arise in the treatment of the quantum harmonic oscillator.

Applying the addition formula, $(-1)^{n}2^{2n}n!\,L_{n}^{\left({\frac {r}{2}}-1\right)}{\Bigl (}z_{1}^{2}+\cdots +z_{r}^{2}{\Bigr )}=\sum _{m_{1}+\cdots +m_{r}=n}\prod _{i=1}^{r}H_{2m_{i}}(z_{i}).$

## Relation to hypergeometric functions

The Laguerre polynomials may be defined in terms of hypergeometric functions, specifically the confluent hypergeometric functions, as $L_{n}^{(\alpha )}(x)={n+\alpha \choose n}M(-n,\alpha +1,x)={\frac {(\alpha +1)_{n}}{n!}}\,_{1}F_{1}(-n,\alpha +1,x)$ where $(a)_{n}$ is the Pochhammer symbol (which in this case represents the rising factorial).

## Hardy–Hille formula

The generalized Laguerre polynomials satisfy the Hardy–Hille formula $\sum _{n=0}^{\infty }{\frac {n!\,\Gamma \left(\alpha +1\right)}{\Gamma \left(n+\alpha +1\right)}}L_{n}^{(\alpha )}(x)L_{n}^{(\alpha )}(y)t^{n}={\frac {1}{(1-t)^{\alpha +1}}}e^{-(x+y)t/(1-t)}\,_{0}F_{1}\left(;\alpha +1;{\frac {xyt}{(1-t)^{2}}}\right),$ where the series on the left converges for $\alpha >-1$ and $|t|<1$ . Using the identity $\,_{0}F_{1}(;\alpha +1;z)=\,\Gamma (\alpha +1)z^{-\alpha /2}I_{\alpha }\left(2{\sqrt {z}}\right),$ (see generalized hypergeometric function), this can also be written as $\sum _{n=0}^{\infty }{\frac {n!}{\Gamma (1+\alpha +n)}}L_{n}^{(\alpha )}(x)L_{n}^{(\alpha )}(y)t^{n}={\frac {1}{(xyt)^{\alpha /2}(1-t)}}e^{-(x+y)t/(1-t)}I_{\alpha }\left({\frac {2{\sqrt {xyt}}}{1-t}}\right).$ where $I_{\alpha }$ denotes the modified Bessel function of the first kind, defined as $I_{\alpha }(z)=\sum _{k=0}^{\infty }{\frac {1}{k!\,\Gamma (k+\alpha +1)}}\left({\frac {z}{2}}\right)^{2k+\alpha }$ This formula is a generalization of the Mehler kernel for Hermite polynomials, which can be recovered from it by setting the Hermite polynomials as a special case of the associated Laguerre polynomials.

Substitute $t\mapsto -t/y$ and take the $y\to \infty$ limit, we obtain $\sum _{n=0}^{\infty }{\frac {t^{n}}{\Gamma (n+1+\alpha )}}L_{n}^{(\alpha )}(x)={\frac {e^{t}}{(-xt)^{\alpha /2}}}I_{\alpha }(2{\sqrt {-xt}}).$ The formula is named after G. H. Hardy and Einar Hille.

## Physics convention

The generalized Laguerre polynomials are used to describe the quantum wavefunction for hydrogen atom orbitals. The convention used throughout this article expresses the generalized Laguerre polynomials as

$L_{n}^{(\alpha )}(x)={\frac {\Gamma (\alpha +n+1)}{\Gamma (\alpha +1)n!}}\,_{1}F_{1}(-n;\alpha +1;x),$

where $\,_{1}F_{1}(a;b;x)$ is the confluent hypergeometric function. In the physics literature, the generalized Laguerre polynomials are instead defined as

${\bar {L}}_{n}^{(\alpha )}(x)={\frac {\left[\Gamma (\alpha +n+1)\right]^{2}}{\Gamma (\alpha +1)n!}}\,_{1}F_{1}(-n;\alpha +1;x).$

The physics version is related to the standard version by

${\bar {L}}_{n}^{(\alpha )}(x)=(n+\alpha )!L_{n}^{(\alpha )}(x).$

There is yet another, albeit less frequently used, convention in the physics literature

${\tilde {L}}_{n}^{(\alpha )}(x)=(-1)^{\alpha }{\bar {L}}_{n-\alpha }^{(\alpha )}.$

## Umbral calculus convention

Generalized Laguerre polynomials are linked to umbral calculus by being Sheffer sequences for $D/(D-I)$ when multiplied by $n!$ . In umbral calculus convention, the default Laguerre polynomials are defined to be ${\mathcal {L}}_{n}(x)=n!L_{n}^{(-1)}(x)=\sum _{k=0}^{n}L(n,k)(-x)^{k}$ where ${\textstyle L(n,k)={\binom {n-1}{k-1}}{\frac {n!}{k!}}}$ are the signless Lah numbers. ${\textstyle ({\mathcal {L}}_{n}(x))_{n\in \mathbb {N} }}$ is a sequence of polynomials of binomial type, *i.e.* they satisfy ${\mathcal {L}}_{n}(x+y)=\sum _{k=0}^{n}{\binom {n}{k}}{\mathcal {L}}_{k}(x){\mathcal {L}}_{n-k}(y)$
