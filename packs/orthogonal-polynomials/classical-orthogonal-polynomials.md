---
title: "Classical orthogonal polynomials"
source: https://en.wikipedia.org/wiki/Classical_orthogonal_polynomials
domain: orthogonal-polynomials
license: CC-BY-SA-4.0
tags: orthogonal polynomials, hermite polynomials, chebyshev polynomials, jacobi polynomials
fetched: 2026-07-02
---

# Classical orthogonal polynomials

In mathematics, the **classical orthogonal polynomials** are the most widely used orthogonal polynomials: the Hermite polynomials, Laguerre polynomials, Jacobi polynomials (including as a special case the Gegenbauer polynomials, Chebyshev polynomials, and Legendre polynomials).

They have many important applications in such areas as mathematical physics (in particular, the theory of random matrices), approximation theory, numerical analysis, and many others.

Classical orthogonal polynomials appeared in the early 19th century in the works of Adrien-Marie Legendre, who introduced the Legendre polynomials. In the late 19th century, the study of continued fractions to solve the moment problem by P. L. Chebyshev and then A.A. Markov and T.J. Stieltjes led to the general notion of orthogonal polynomials.

For given polynomials $Q,L:\mathbb {R} \to \mathbb {R}$ and $\forall \,n\in \mathbb {N} _{0}$ the classical orthogonal polynomials $f_{n}:\mathbb {R} \to \mathbb {R}$ are characterized by being solutions of the differential equation

$Q(x)\,f_{n}^{\prime \prime }+L(x)\,f_{n}^{\prime }+\lambda _{n}f_{n}=0$

with to be determined constants $\lambda _{n}\in \mathbb {R}$ . The Wikipedia article Rodrigues' formula has a proof that the polynomials obtained from the Rodrigues' formula obey a differential equation of this form and also derives $\lambda _{n}$ .

There are several more general definitions of orthogonal classical polynomials; for example, Andrews & Askey (1985) use the term for all polynomials in the Askey scheme.

## Definition

In general, the orthogonal polynomials $P_{n}$ with respect to a weight $W:\mathbb {R} \rightarrow \mathbb {R} ^{+}$ satisfy

${\begin{aligned}&\deg P_{n}=n~,\quad n=0,1,2,\ldots \\&\int P_{m}(x)\,P_{n}(x)\,W(x)\,dx=0~,\quad m\neq n~.\end{aligned}}$

The relations above define $P_{n}$ up to multiplication by a number. Various normalisations are used to fix the constant, e.g.

$\int P_{n}(x)^{2}W(x)\,dx=1~.$

The classical orthogonal polynomials correspond to the following three families of weights:

${\begin{aligned}{\text{(Jacobi)}}\quad &W(x)={\begin{cases}(1-x)^{\alpha }(1+x)^{\beta }~,&-1\leq x\leq 1\\0~,&{\text{otherwise}}\end{cases}}\\{\text{(Hermite)}}\quad &W(x)=\exp(-x^{2})\\{\text{(Laguerre)}}\quad &W(x)={\begin{cases}x^{\alpha }\exp(-x)~,&x\geq 0\\0~,&{\text{otherwise}}\end{cases}}\end{aligned}}$

The standard normalisation (also called *standardization*) is detailed below.

### Jacobi polynomials

For $\alpha ,\,\beta >-1$ the Jacobi polynomials are given by the formula

$P_{n}^{(\alpha ,\beta )}(z)={\frac {(-1)^{n}}{2^{n}n!}}(1-z)^{-\alpha }(1+z)^{-\beta }{\frac {d^{n}}{dz^{n}}}\left\{(1-z)^{\alpha }(1+z)^{\beta }(1-z^{2})^{n}\right\}~.$

They are normalised (standardized) by

$P_{n}^{(\alpha ,\beta )}(1)={n+\alpha \choose n},$

and satisfy the orthogonality condition

${\begin{aligned}&\int _{-1}^{1}(1-x)^{\alpha }(1+x)^{\beta }P_{m}^{(\alpha ,\beta )}(x)P_{n}^{(\alpha ,\beta )}(x)\;dx\\={}&{\frac {2^{\alpha +\beta +1}}{2n+\alpha +\beta +1}}{\frac {\Gamma (n+\alpha +1)\Gamma (n+\beta +1)}{\Gamma (n+\alpha +\beta +1)n!}}\delta _{nm}.\end{aligned}}$

The Jacobi polynomials are solutions to the differential equation

$(1-x^{2})y''+(\beta -\alpha -(\alpha +\beta +2)x)y'+n(n+\alpha +\beta +1)y=0~.$

#### Important special cases

The Jacobi polynomials with $\alpha =\beta$ are called the Gegenbauer polynomials (with parameter $\gamma =\alpha +1/2$ )

For $\alpha =\beta =0$ , these are called the Legendre polynomials (for which the interval of orthogonality is [−1, 1] and the weight function is simply 1):

$P_{0}(x)=1,\,P_{1}(x)=x,\,P_{2}(x)={\frac {3x^{2}-1}{2}},\,P_{3}(x)={\frac {5x^{3}-3x}{2}},\ldots$

For $\alpha =\beta =\pm 1/2$ , one obtains the Chebyshev polynomials (of the second and first kind, respectively).

### Hermite polynomials

The Hermite polynomials are defined by

$H_{n}(x)=(-1)^{n}e^{x^{2}}{\frac {d^{n}}{dx^{n}}}e^{-x^{2}}=e^{x^{2}/2}{\bigg (}x-{\frac {d}{dx}}{\bigg )}^{n}e^{-x^{2}/2}$

They satisfy the orthogonality condition

$\int _{-\infty }^{\infty }H_{n}(x)H_{m}(x)e^{-x^{2}}\,dx={\sqrt {\pi }}2^{n}n!\delta _{mn}~,$

and the differential equation

$y''-2xy'+2n\,y=0~.$

### Laguerre polynomials

The generalised Laguerre polynomials are defined by

$L_{n}^{(\alpha )}(x)={x^{-\alpha }e^{x} \over n!}{d^{n} \over dx^{n}}\left(e^{-x}x^{n+\alpha }\right)$

(the classical Laguerre polynomials correspond to $\alpha =0$ .)

They satisfy the orthogonality relation

$\int _{0}^{\infty }x^{\alpha }e^{-x}L_{n}^{(\alpha )}(x)L_{m}^{(\alpha )}(x)\,dx={\frac {\Gamma (n+\alpha +1)}{n!}}\delta _{n,m}~,$

and the differential equation

$x\,y''+(\alpha +1-x)\,y'+n\,y=0~.$

## Differential equation

The classical orthogonal polynomials arise from a differential equation of the form

$Q(x)\,f''+L(x)\,f'+\lambda f=0$

where *Q* is a given quadratic (at most) polynomial, and *L* is a given linear polynomial. The function *f*, and the constant *λ*, are to be found.

(Note that it makes sense for such an equation to have a polynomial solution.

Each term in the equation is a polynomial, and the degrees are consistent.)

This is a Sturm–Liouville type of equation. Such equations generally have singularities in their solution functions f except for particular values of *λ*. They can be thought of as eigenvector/eigenvalue problems: Letting *D* be the differential operator, $D(f)=Qf''+Lf'$ , and changing the sign of *λ*, the problem is to find the eigenvectors (eigenfunctions) f, and the corresponding eigenvalues *λ*, such that f does not have singularities and *D*(*f*) = *λf*.

The solutions of this differential equation have singularities unless *λ* takes on specific values. There is a series of numbers *λ*0, *λ*1, *λ*2, ... that led to a series of polynomial solutions *P*0, *P*1, *P*2, ... if one of the following sets of conditions are met:

1. *Q* is actually quadratic, *L* is linear, *Q* has two distinct real roots, the root of *L* lies strictly between the roots of *Q*, and the leading terms of *Q* and *L* have the same sign.
2. *Q* is not actually quadratic, but is linear, *L* is linear, the roots of *Q* and *L* are different, and the leading terms of *Q* and *L* have the same sign if the root of *L* is less than the root of *Q*, or vice versa.
3. *Q* is just a nonzero constant, *L* is linear, and the leading term of *L* has the opposite sign of *Q*.

These three cases lead to the **Jacobi-like**, **Laguerre-like**, and **Hermite-like** polynomials, respectively.

In each of these three cases, we have the following:

- The solutions are a series of polynomials *P*0, *P*1, *P*2, ..., each *P**n* having degree *n*, and corresponding to a number λ*n*.
- The interval of orthogonality is bounded by whatever roots *Q* has.
- The root of *L* is inside the interval of orthogonality.
- Letting $R(x)=e^{\int {\frac {L(x)}{Q(x)}}\,dx}$ , the polynomials are orthogonal under the weight function $W(x)={\frac {R(x)}{Q(x)}}$
- *W*(*x*) has no zeros or infinities inside the interval, though it may have zeros or infinities at the end points.
- *W*(*x*) gives a finite inner product to any polynomials.
- *W*(*x*) can be made to be greater than 0 in the interval. (Negate the entire differential equation if necessary so that *Q*(*x*) > 0 inside the interval.)

Because of the constant of integration, the quantity *R*(*x*) is determined only up to an arbitrary positive multiplicative constant. It will be used only in homogeneous differential equations (where this doesn't matter) and in the definition of the weight function (which can also be indeterminate.) The tables below will give the "official" values of *R*(*x*) and *W*(*x*).

### Rodrigues' formula

Under the assumptions of the preceding section, *P**n*(*x*) is proportional to ${\frac {1}{W(x)}}\ {\frac {d^{n}}{dx^{n}}}\left(W(x)[Q(x)]^{n}\right).$

This is known as Rodrigues' formula, after Olinde Rodrigues. It is often written

$P_{n}(x)={\frac {1}{{e_{n}}W(x)}}\ {\frac {d^{n}}{dx^{n}}}\left(W(x)[Q(x)]^{n}\right)$

where the numbers *e**n* depend on the standardization. The standard values of *e**n* will be given in the tables below.

### The numbers *λ**n*

Under the assumptions of the preceding section, we have

$\lambda _{n}=-n\left({\frac {n-1}{2}}Q''+L'\right).$

(Since *Q* is quadratic and *L* is linear, $Q''$ and $L'$ are constants, so these are just numbers.)

### Second form for the differential equation

Let

$R(x)=e^{\int {\frac {L(x)}{Q(x)}}\,dx}.$

Then

$(Ry')'=R\,y''+R'\,y'=R\,y''+{\frac {R\,L}{Q}}\,y'.$

Now multiply the differential equation

$Q\,y''+L\,y'+\lambda y=0$

by *R*/*Q*, getting

$R\,y''+{\frac {R\,L}{Q}}\,y'+{\frac {R\,\lambda }{Q}}\,y=0$

or

$(Ry')'+{\frac {R\,\lambda }{Q}}\,y=0.$

This is the standard Sturm–Liouville form for the equation.

### Third form for the differential equation

Let $S(x)={\sqrt {R(x)}}=e^{\int {\frac {L(x)}{2\,Q(x)}}\,dx}.$

Then

$S'={\frac {S\,L}{2\,Q}}.$

Now multiply the differential equation

$Q\,y''+L\,y'+\lambda y=0$

by *S*/*Q*, getting

$S\,y''+{\frac {S\,L}{Q}}\,y'+{\frac {S\,\lambda }{Q}}\,y=0$

or

$S\,y''+2\,S'\,y'+{\frac {S\,\lambda }{Q}}\,y=0$

But $(S\,y)''=S\,y''+2\,S'\,y'+S''\,y$ , so

$(S\,y)''+\left({\frac {S\,\lambda }{Q}}-S''\right)\,y=0,$

or, letting *u* = *Sy*,

$u''+\left({\frac {\lambda }{Q}}-{\frac {S''}{S}}\right)\,u=0.$

### Formulas involving derivatives

Under the assumptions of the preceding section, let *P*[*r*] *n* denote the *r*-th derivative of *P**n*. (We put the "r" in brackets to avoid confusion with an exponent.) *P*[*r*] *n* is a polynomial of degree *n* − *r*. Then we have the following:

- (orthogonality) For fixed r, the polynomial sequence *P*[*r*] *r*, *P*[*r*] *r* + 1, *P*[*r*] *r* + 2, ... are orthogonal, weighted by $WQ^{r}$ .
- (generalized Rodrigues' formula) *P*[*r*] *n* is proportional to ${\frac {1}{W(x)[Q(x)]^{r}}}\ {\frac {d^{n-r}}{dx^{n-r}}}\left(W(x)[Q(x)]^{n}\right).$
- (differential equation) *P*[*r*] *n* is a solution of ${Q}\,y''+(rQ'+L)\,y'+[\lambda _{n}-\lambda _{r}]\,y=0$ , where λ*r* is the same function as λ*n*, that is, $\lambda _{r}=-r\left({\frac {r-1}{2}}Q''+L'\right)$
- (differential equation, second form) *P*[*r*] *n* is a solution of $(RQ^{r}y')'+[\lambda _{n}-\lambda _{r}]RQ^{r-1}\,y=0$

There are also some mixed recurrences. In each of these, the numbers *a*, *b*, and *c* depend on *n* and *r*, and are unrelated in the various formulas.

- $P_{n}^{[r]}=aP_{n+1}^{[r+1]}+bP_{n}^{[r+1]}+cP_{n-1}^{[r+1]}$
- $P_{n}^{[r]}=(ax+b)P_{n}^{[r+1]}+cP_{n-1}^{[r+1]}$
- $QP_{n}^{[r+1]}=(ax+b)P_{n}^{[r]}+cP_{n-1}^{[r]}$

There are an enormous number of other formulas involving orthogonal polynomials in various ways. Here is a tiny sample of them, relating to the Chebyshev, associated Laguerre, and Hermite polynomials:

- $2\,T_{m}(x)\,T_{n}(x)=T_{m+n}(x)+T_{m-n}(x)$
- $H_{2n}(x)=(-4)^{n}\,n!\,L_{n}^{(-1/2)}(x^{2})$
- $H_{2n+1}(x)=2(-4)^{n}\,n!\,x\,L_{n}^{(1/2)}(x^{2})$

### Orthogonality

The differential equation for a particular *λ* may be written (omitting explicit dependence on x)

$Q{\ddot {f}}_{n}+L{\dot {f}}_{n}+\lambda _{n}f_{n}=0$

multiplying by $(R/Q)f_{m}$ yields

$Rf_{m}{\ddot {f}}_{n}+{\frac {R}{Q}}Lf_{m}{\dot {f}}_{n}+{\frac {R}{Q}}\lambda _{n}f_{m}f_{n}=0$

and reversing the subscripts yields

$Rf_{n}{\ddot {f}}_{m}+{\frac {R}{Q}}Lf_{n}{\dot {f}}_{m}+{\frac {R}{Q}}\lambda _{m}f_{n}f_{m}=0$

subtracting and integrating:

$\int _{a}^{b}\left[R(f_{m}{\ddot {f}}_{n}-f_{n}{\ddot {f}}_{m})+{\frac {R}{Q}}L(f_{m}{\dot {f}}_{n}-f_{n}{\dot {f}}_{m})\right]\,dx+(\lambda _{n}-\lambda _{m})\int _{a}^{b}{\frac {R}{Q}}f_{m}f_{n}\,dx=0$

but it can be seen that

${\frac {d}{dx}}\left[R(f_{m}{\dot {f}}_{n}-f_{n}{\dot {f}}_{m})\right]=R(f_{m}{\ddot {f}}_{n}-f_{n}{\ddot {f}}_{m})\,\,+\,\,R{\frac {L}{Q}}(f_{m}{\dot {f}}_{n}-f_{n}{\dot {f}}_{m})$

so that:

$\left[R(f_{m}{\dot {f}}_{n}-f_{n}{\dot {f}}_{m})\right]_{a}^{b}\,\,+\,\,(\lambda _{n}-\lambda _{m})\int _{a}^{b}{\frac {R}{Q}}f_{m}f_{n}\,dx=0$

If the polynomials *f* are such that the term on the left is zero, and $\lambda _{m}\neq \lambda _{n}$ for $m\neq n$ , then the orthogonality relationship will hold:

$\int _{a}^{b}{\frac {R}{Q}}f_{m}f_{n}\,dx=0$

for $m\neq n$ .

## Derivation from differential equation

All of the polynomial sequences arising from the differential equation above are equivalent, under scaling and/or shifting of the domain, and standardizing of the polynomials, to more restricted classes. Those restricted classes are exactly "classical orthogonal polynomials".

- Every Jacobi-like polynomial sequence can have its domain shifted and/or scaled so that its interval of orthogonality is [−1, 1], and has *Q* = 1 − *x*2. They can then be standardized into the **Jacobi polynomials** $P_{n}^{(\alpha ,\beta )}$ . There are several important subclasses of these: **Gegenbauer**, **Legendre**, and two types of **Chebyshev**.
- Every Laguerre-like polynomial sequence can have its domain shifted, scaled, and/or reflected so that its interval of orthogonality is $[0,\infty )$ , and has *Q* = *x*. They can then be standardized into the **Associated Laguerre polynomials** $L_{n}^{(\alpha )}$ . The plain **Laguerre polynomials** $\ L_{n}$ are a subclass of these.
- Every Hermite-like polynomial sequence can have its domain shifted and/or scaled so that its interval of orthogonality is $(-\infty ,\infty )$ , and has Q = 1 and L(0) = 0. They can then be standardized into the **Hermite polynomials** $H_{n}$ .

Because all polynomial sequences arising from a differential equation in the manner described above are trivially equivalent to the classical polynomials, the actual classical polynomials are always used.

### Jacobi polynomial

The Jacobi-like polynomials, once they have had their domain shifted and scaled so that the interval of orthogonality is [−1, 1], still have two parameters to be determined. They are $\alpha$ and $\beta$ in the Jacobi polynomials, written $P_{n}^{(\alpha ,\beta )}$ . We have $Q(x)=1-x^{2}$ and $L(x)=\beta -\alpha -(\alpha +\beta +2)\,x$ . Both $\alpha$ and $\beta$ are required to be greater than −1. (This puts the root of L inside the interval of orthogonality.)

When $\alpha$ and $\beta$ are not equal, these polynomials are not symmetrical about *x* = 0.

The differential equation

$(1-x^{2})\,y''+(\beta -\alpha -[\alpha +\beta +2]\,x)\,y'+\lambda \,y=0\qquad {\text{with}}\qquad \lambda =n(n+1+\alpha +\beta )$

is **Jacobi's equation**.

For further details, see Jacobi polynomials.

### Gegenbauer polynomials

When one sets the parameters $\alpha$ and $\beta$ in the Jacobi polynomials equal to each other, one obtains the **Gegenbauer** or **ultraspherical** polynomials. They are written $C_{n}^{(\alpha )}$ , and defined as

$C_{n}^{(\alpha )}(x)={\frac {\Gamma (2\alpha \!+\!n)\,\Gamma (\alpha \!+\!1/2)}{\Gamma (2\alpha )\,\Gamma (\alpha \!+\!n\!+\!1/2)}}\!\ P_{n}^{(\alpha -1/2,\alpha -1/2)}(x).$

We have $Q(x)=1-x^{2}$ and $L(x)=-(2\alpha +1)\,x$ . The parameter $\alpha$ is required to be greater than −1/2.

(Incidentally, the standardization given in the table below would make no sense for *α* = 0 and *n* ≠ 0, because it would set the polynomials to zero. In that case, the accepted standardization sets $C_{n}^{(0)}(1)={\frac {2}{n}}$ instead of the value given in the table.)

Ignoring the above considerations, the parameter $\alpha$ is closely related to the derivatives of $C_{n}^{(\alpha )}$ :

$C_{n}^{(\alpha +1)}(x)={\frac {1}{2\alpha }}\!\ {\frac {d}{dx}}C_{n+1}^{(\alpha )}(x)$

or, more generally:

$C_{n}^{(\alpha +m)}(x)={\frac {\Gamma (\alpha )}{2^{m}\Gamma (\alpha +m)}}\!\ C_{n+m}^{(\alpha )[m]}(x).$

All the other classical Jacobi-like polynomials (Legendre, etc.) are special cases of the Gegenbauer polynomials, obtained by choosing a value of $\alpha$ and choosing a standardization.

For further details, see Gegenbauer polynomials.

### Legendre polynomials

The differential equation is

$(1-x^{2})\,y''-2x\,y'+\lambda \,y=0\qquad {\text{with}}\qquad \lambda =n(n+1).$

This is **Legendre's equation**.

The second form of the differential equation is:

${\frac {d}{dx}}[(1-x^{2})\,y']+\lambda \,y=0.$

The recurrence relation is

$(n+1)\,P_{n+1}(x)=(2n+1)x\,P_{n}(x)-n\,P_{n-1}(x).$

A mixed recurrence is

$P_{n+1}^{[r+1]}(x)=P_{n-1}^{[r+1]}(x)+(2n+1)\,P_{n}^{[r]}(x).$

Rodrigues' formula is

$P_{n}(x)=\,{\frac {1}{2^{n}n!}}\ {\frac {d^{n}}{dx^{n}}}\left([x^{2}-1]^{n}\right).$

For further details, see Legendre polynomials.

#### Associated Legendre polynomials

The Associated Legendre polynomials, denoted $P_{\ell }^{(m)}(x)$ where $\ell$ and m are integers with $0\leqslant m\leqslant \ell$ , are defined as

$P_{\ell }^{(m)}(x)=(-1)^{m}\,(1-x^{2})^{m/2}\ P_{\ell }^{[m]}(x).$

The *m* in parentheses (to avoid confusion with an exponent) is a parameter. The *m* in brackets denotes the *m*-th derivative of the Legendre polynomial.

These "polynomials" are misnamed—they are not polynomials when *m* is odd.

They have a recurrence relation:

$(\ell +1-m)\,P_{\ell +1}^{(m)}(x)=(2\ell +1)x\,P_{\ell }^{(m)}(x)-(\ell +m)\,P_{\ell -1}^{(m)}(x).$

For fixed *m*, the sequence $P_{m}^{(m)},P_{m+1}^{(m)},P_{m+2}^{(m)},\dots$ are orthogonal over [−1, 1], with weight 1.

For given *m*, $P_{\ell }^{(m)}(x)$ are the solutions of

$(1-x^{2})\,y''-2xy'+\left[\lambda -{\frac {m^{2}}{1-x^{2}}}\right]\,y=0\qquad {\text{ with }}\qquad \lambda =\ell (\ell +1).$

### Chebyshev polynomials

The differential equation is

$(1-x^{2})\,y''-x\,y'+\lambda \,y=0\qquad {\text{with}}\qquad \lambda =n^{2}.$

This is **Chebyshev's equation**.

The recurrence relation is

$T_{n+1}(x)=2x\,T_{n}(x)-T_{n-1}(x).$

Rodrigues' formula is

$T_{n}(x)={\frac {\Gamma (1/2){\sqrt {1-x^{2}}}}{(-2)^{n}\,\Gamma (n+1/2)}}\ {\frac {d^{n}}{dx^{n}}}\left([1-x^{2}]^{n-1/2}\right).$

These polynomials have the property that, in the interval of orthogonality,

$T_{n}(x)=\cos(n\,\arccos(x)).$

(To prove it, use the recurrence formula.)

This means that all their local minima and maxima have values of −1 and +1, that is, the polynomials are "level". Because of this, expansion of functions in terms of Chebyshev polynomials is sometimes used for polynomial approximations in computer math libraries.

Some authors use versions of these polynomials that have been shifted so that the interval of orthogonality is [0, 1] or [−2, 2].

There are also **Chebyshev polynomials of the second kind**, denoted $U_{n}$

We have:

$U_{n}={\frac {1}{n+1}}\,T_{n+1}'.$

For further details, including the expressions for the first few polynomials, see Chebyshev polynomials.

### Laguerre polynomials

The most general Laguerre-like polynomials, after the domain has been shifted and scaled, are the Associated Laguerre polynomials (also called generalized Laguerre polynomials), denoted $L_{n}^{(\alpha )}$ . There is a parameter $\alpha$ , which can be any real number strictly greater than −1. The parameter is put in parentheses to avoid confusion with an exponent. The plain Laguerre polynomials are simply the $\alpha =0$ version of these:

$L_{n}(x)=L_{n}^{(0)}(x).$

The differential equation is

$x\,y''+(\alpha +1-x)\,y'+\lambda \,y=0{\text{ with }}\lambda =n.$

This is **Laguerre's equation**.

The second form of the differential equation is

$(x^{\alpha +1}\,e^{-x}\,y')'+\lambda \,x^{\alpha }\,e^{-x}\,y=0.$

The recurrence relation is

$(n+1)\,L_{n+1}^{(\alpha )}(x)=(2n+1+\alpha -x)\,L_{n}^{(\alpha )}(x)-(n+\alpha )\,L_{n-1}^{(\alpha )}(x).$

Rodrigues' formula is

$L_{n}^{(\alpha )}(x)={\frac {x^{-\alpha }e^{x}}{n!}}\ {\frac {d^{n}}{dx^{n}}}\left(x^{n+\alpha }\,e^{-x}\right).$

The parameter $\alpha$ is closely related to the derivatives of $L_{n}^{(\alpha )}$ :

$L_{n}^{(\alpha +1)}(x)=-{\frac {d}{dx}}L_{n+1}^{(\alpha )}(x)$

or, more generally:

$L_{n}^{(\alpha +m)}(x)=(-1)^{m}L_{n+m}^{(\alpha )[m]}(x).$

Laguerre's equation can be manipulated into a form that is more useful in applications:

$u=x^{\frac {\alpha -1}{2}}e^{-x/2}L_{n}^{(\alpha )}(x)$

is a solution of

$u''+{\frac {2}{x}}\,u'+\left[{\frac {\lambda }{x}}-{\frac {1}{4}}-{\frac {\alpha ^{2}-1}{4x^{2}}}\right]\,u=0{\text{ with }}\lambda =n+{\frac {\alpha +1}{2}}.$

This can be further manipulated. When $\ell ={\frac {\alpha -1}{2}}$ is an integer, and $n\geq \ell +1$ :

$u=x^{\ell }e^{-x/2}L_{n-\ell -1}^{(2\ell +1)}(x)$

is a solution of

$u''+{\frac {2}{x}}\,u'+\left[{\frac {\lambda }{x}}-{\frac {1}{4}}-{\frac {\ell (\ell +1)}{x^{2}}}\right]\,u=0{\text{ with }}\lambda =n.$

The solution is often expressed in terms of derivatives instead of associated Laguerre polynomials:

$u=x^{\ell }e^{-x/2}L_{n+\ell }^{[2\ell +1]}(x).$

This equation arises in quantum mechanics, in the radial part of the solution of the Schrödinger equation for a one-electron atom.

Physicists often use a definition for the Laguerre polynomials that is larger, by a factor of $(n!)$ , than the definition used here.

For further details, including the expressions for the first few polynomials, see Laguerre polynomials.

### Hermite polynomials

The differential equation is

$y''-2xy'+\lambda \,y=0,\qquad {\text{with}}\qquad \lambda =2n.$

This is **Hermite's equation**.

The second form of the differential equation is

$(e^{-x^{2}}\,y')'+e^{-x^{2}}\,\lambda \,y=0.$

The third form is

$(e^{-x^{2}/2}\,y)''+(\lambda +1-x^{2})(e^{-x^{2}/2}\,y)=0.$

The recurrence relation is

$H_{n+1}(x)=2x\,H_{n}(x)-2n\,H_{n-1}(x).$

Rodrigues' formula is

$H_{n}(x)=(-1)^{n}\,e^{x^{2}}\ {\frac {d^{n}}{dx^{n}}}\left(e^{-x^{2}}\right).$

The first few Hermite polynomials are

$H_{0}(x)=1$

$H_{1}(x)=2x$

$H_{2}(x)=4x^{2}-2$

$H_{3}(x)=8x^{3}-12x$

$H_{4}(x)=16x^{4}-48x^{2}+12$

One can define the **associated Hermite functions**

$\psi _{n}(x)=(h_{n})^{-1/2}\,e^{-x^{2}/2}H_{n}(x).$

Because the multiplier is proportional to the square root of the weight function, these functions are orthogonal over $(-\infty ,\infty )$ with no weight function.

The third form of the differential equation above, for the associated Hermite functions, is

$\psi ''+(\lambda +1-x^{2})\psi =0.$

The associated Hermite functions arise in many areas of mathematics and physics. In quantum mechanics, they are the solutions of Schrödinger's equation for the harmonic oscillator. They are also eigenfunctions (with eigenvalue (−*i* *n*) of the continuous Fourier transform.

Many authors, particularly probabilists, use an alternate definition of the Hermite polynomials, with a weight function of $e^{-x^{2}/2}$ instead of $e^{-x^{2}}$ . If the notation *He* is used for these Hermite polynomials, and *H* for those above, then these may be characterized by

$He_{n}(x)=2^{-n/2}\,H_{n}\left({\frac {x}{\sqrt {2}}}\right).$

For further details, see Hermite polynomials.

## Characterizations of classical orthogonal polynomials

There are several conditions that single out the classical orthogonal polynomials from the others.

The first condition was found by Sonine (and later by Hahn), who showed that (up to linear changes of variable) the classical orthogonal polynomials are the only ones such that their derivatives are also orthogonal polynomials.

Bochner characterized classical orthogonal polynomials in terms of their recurrence relations.

Tricomi characterized classical orthogonal polynomials as those that have a certain analogue of the Rodrigues formula.

## Table of classical orthogonal polynomials

The following table summarises the properties of the classical orthogonal polynomials.

| Name, and conventional symbol | Chebyshev, $\ T_{n}$ | Chebyshev (second kind), $\ U_{n}$ | Legendre, $\ P_{n}$ | Hermite, $\ H_{n}$ |
|---|---|---|---|---|
| Limits of orthogonality | $-1,1$ | $-1,1$ | $-1,1$ | $-\infty ,\infty$ |
| Weight, $W(x)$ | $(1-x^{2})^{-1/2}$ | $(1-x^{2})^{1/2}$ | 1 | $e^{-x^{2}}$ |
| Standardization | $T_{n}(1)=1$ | $U_{n}(1)=n+1$ | $P_{n}(1)=1$ | Lead term $=2^{n}$ |
| Square of norm | $\left\{{\begin{matrix}\pi &:~n=0\\\pi /2&:~n\neq 0\end{matrix}}\right.$ | $\pi /2$ | ${\frac {2}{2n+1}}$ | $2^{n}\,n!\,{\sqrt {\pi }}$ |
| Leading term | $2^{n-1}$ | $2^{n}$ | ${\frac {(2n)!}{2^{n}\,(n!)^{2}}}$ | $2^{n}$ |
| Second term, $k'_{n}$ | 0 | 0 | 0 | 0 |
| Q | $1-x^{2}$ | $1-x^{2}$ | $1-x^{2}$ | 1 |
| L | $-x$ | $-3x$ | $-2x$ | $-2x$ |
| $R(x)=e^{\int {\frac {L(x)}{Q(x)}}\,dx}$ | $(1-x^{2})^{1/2}$ | $(1-x^{2})^{3/2}$ | $1-x^{2}$ | $e^{-x^{2}}$ |
| Constant in diff. equation, $\lambda _{n}$ | $n^{2}$ | $n(n+2)$ | $n(n+1)$ | $2n$ |
| Constant in Rodrigues' formula, $e_{n}$ | $(-2)^{n}\,{\frac {\Gamma (n+1/2)}{\sqrt {\pi }}}$ | $2(-2)^{n}\,{\frac {\Gamma (n+3/2)}{(n+1)\,{\sqrt {\pi }}}}$ | $(-2)^{n}\,n!$ | $(-1)^{n}$ |
| Recurrence relation, $a_{n}$ | 2 | 2 | ${\frac {2n+1}{n+1}}$ | 2 |
| Recurrence relation, $b_{n}$ | 0 | 0 | 0 | 0 |
| Recurrence relation, $c_{n}$ | 1 | 1 | ${\frac {n}{n+1}}$ | $2n$ |

| Name, and conventional symbol | Associated Laguerre, $L_{n}^{(\alpha )}$ | Laguerre, $\ L_{n}$ |
|---|---|---|
| Limits of orthogonality | $0,\infty$ | $0,\infty$ |
| Weight, $W(x)$ | $x^{\alpha }e^{-x}$ | $e^{-x}$ |
| Standardization | Lead term $={\frac {(-1)^{n}}{n!}}$ | Lead term $={\frac {(-1)^{n}}{n!}}$ |
| Square of norm, $h_{n}$ | ${\frac {\Gamma (n+\alpha +1)}{n!}}$ | 1 |
| Leading term, $k_{n}$ | ${\frac {(-1)^{n}}{n!}}$ | ${\frac {(-1)^{n}}{n!}}$ |
| Second term, $k'_{n}$ | ${\frac {(-1)^{n+1}(n+\alpha )}{(n-1)!}}$ | ${\frac {(-1)^{n+1}n}{(n-1)!}}$ |
| Q | x | x |
| L | $\alpha +1-x$ | $1-x$ |
| $R(x)=e^{\int {\frac {L(x)}{Q(x)}}\,dx}$ | $x^{\alpha +1}\,e^{-x}$ | $x\,e^{-x}$ |
| Constant in diff. equation, $\lambda _{n}$ | n | n |
| Constant in Rodrigues' formula, $e_{n}$ | $n!$ | $n!$ |
| Recurrence relation, $a_{n}$ | ${\frac {-1}{n+1}}$ | ${\frac {-1}{n+1}}$ |
| Recurrence relation, $b_{n}$ | ${\frac {2n+1+\alpha }{n+1}}$ | ${\frac {2n+1}{n+1}}$ |
| Recurrence relation, $c_{n}$ | ${\frac {n+\alpha }{n+1}}$ | ${\frac {n}{n+1}}$ |

| Name, and conventional symbol | Gegenbauer, $C_{n}^{(\alpha )}$ | Jacobi, $P_{n}^{(\alpha ,\beta )}$ |
|---|---|---|
| Limits of orthogonality | $-1,1$ | $-1,1$ |
| Weight, $W(x)$ | $(1-x^{2})^{\alpha -1/2}$ | $(1-x)^{\alpha }(1+x)^{\beta }$ |
| Standardization | $C_{n}^{(\alpha )}(1)={\frac {\Gamma (n+2\alpha )}{n!\,\Gamma (2\alpha )}}$ if $\alpha \neq 0$ | $P_{n}^{(\alpha ,\beta )}(1)={\frac {\Gamma (n+1+\alpha )}{n!\,\Gamma (1+\alpha )}}$ |
| Square of norm, $h_{n}$ | ${\frac {\pi \,2^{1-2\alpha }\Gamma (n+2\alpha )}{n!(n+\alpha )(\Gamma (\alpha ))^{2}}}$ | ${\frac {2^{\alpha +\beta +1}\,\Gamma (n\!+\!\alpha \!+\!1)\,\Gamma (n\!+\!\beta \!+\!1)}{n!(2n\!+\!\alpha \!+\!\beta \!+\!1)\Gamma (n\!+\!\alpha \!+\!\beta \!+\!1)}}$ |
| Leading term, $k_{n}$ | ${\frac {\Gamma (2n+2\alpha )\Gamma (1/2+\alpha )}{n!\,2^{n}\,\Gamma (2\alpha )\Gamma (n+1/2+\alpha )}}$ | ${\frac {\Gamma (2n+1+\alpha +\beta )}{n!\,2^{n}\,\Gamma (n+1+\alpha +\beta )}}$ |
| Second term, $k'_{n}$ | 0 | ${\frac {(\alpha -\beta )\,\Gamma (2n+\alpha +\beta )}{(n-1)!\,2^{n}\,\Gamma (n+1+\alpha +\beta )}}$ |
| Q | $1-x^{2}$ | $1-x^{2}$ |
| L | $-(2\alpha +1)\,x$ | $\beta -\alpha -(\alpha +\beta +2)\,x$ |
| $R(x)=e^{\int {\frac {L(x)}{Q(x)}}\,dx}$ | $(1-x^{2})^{\alpha +1/2}$ | $(1-x)^{\alpha +1}(1+x)^{\beta +1}$ |
| Constant in diff. equation, $\lambda _{n}$ | $n(n+2\alpha )$ | $n(n+1+\alpha +\beta )$ |
| Constant in Rodrigues' formula, $e_{n}$ | ${\frac {(-2)^{n}\,n!\,\Gamma (2\alpha )\,\Gamma (n\!+\!1/2\!+\!\alpha )}{\Gamma (n\!+\!2\alpha )\Gamma (\alpha \!+\!1/2)}}$ | $(-2)^{n}\,n!$ |
| Recurrence relation, $a_{n}$ | ${\frac {2(n+\alpha )}{n+1}}$ | ${\frac {(2n+1+\alpha +\beta )(2n+2+\alpha +\beta )}{2(n+1)(n+1+\alpha +\beta )}}$ |
| Recurrence relation, $b_{n}$ | 0 | ${\frac {({\alpha }^{2}-{\beta }^{2})(2n+1+\alpha +\beta )}{2(n+1)(2n+\alpha +\beta )(n+1+\alpha +\beta )}}$ |
| Recurrence relation, $c_{n}$ | ${\frac {n+2{\alpha }-1}{n+1}}$ | ${\frac {(n+\alpha )(n+\beta )(2n+2+\alpha +\beta )}{(n+1)(n+1+\alpha +\beta )(2n+\alpha +\beta )}}$ |
