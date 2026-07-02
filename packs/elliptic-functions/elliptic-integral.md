---
title: "Elliptic integral"
source: https://en.wikipedia.org/wiki/Elliptic_integral
domain: elliptic-functions
license: CC-BY-SA-4.0
tags: elliptic function, jacobi elliptic functions, weierstrass elliptic function, theta function
fetched: 2026-07-02
---

# Elliptic integral

In integral calculus, an **elliptic integral** is one of a number of related functions defined as the value of certain integrals, which were first studied by Giulio Fagnano and Leonhard Euler (c. 1750). Their name originates from their connection with the problem of finding the arc length of an ellipse.

Modern mathematics defines an "elliptic integral" as any function *f* which can be expressed in the form

$f(x)=\int _{c}^{x}R{\left({\textstyle t,{\sqrt {P(t)}}}\right)}\,dt,$

where *R* is a rational function of its two arguments, *P* is a polynomial of degree 3 or 4 with no repeated roots, and *c* is a constant.

In general, integrals in this form cannot be expressed in terms of elementary functions. Exceptions to this general rule are when *P* has repeated roots, when *R*(*x*, *y*) contains no odd powers of *y*, and when the integral is pseudo-elliptic. However, with the appropriate reduction formula, every elliptic integral can be brought into a form that involves integrals over rational functions and the three Legendre canonical forms, also known as the elliptic integrals of the first, second and third kind.

Besides the Legendre form given below, the elliptic integrals may also be expressed in Carlson symmetric form. Additional insight into the theory of the elliptic integral may be gained through the study of the Schwarz–Christoffel mapping. Historically, elliptic functions were discovered as inverse functions of elliptic integrals.

## Argument notation

*Incomplete elliptic integrals* are functions of two arguments; *complete elliptic integrals* are functions of a single argument. These arguments are expressed in a variety of different but equivalent ways as they give the same elliptic integral. Most texts adhere to a canonical naming scheme, using the following naming conventions.

For expressing one argument:

- *α*, the *modular angle*
- *k* = sin *α*, the *elliptic modulus* or *eccentricity*
- *m* = *k*2 = sin2 *α*, the *parameter*

Each of the above three quantities is completely determined by any of the others (given that they are non-negative). Thus, they can be used interchangeably.

The other argument can likewise be expressed as *φ*, the *amplitude*, or as *x* or *u*, where *x* = sin *φ* = sn *u* and sn is one of the Jacobian elliptic functions.

Specifying the value of any one of these quantities determines the others. Note that *u* also depends on *m*. Some additional relationships involving *u* include $\cos \varphi =\operatorname {cn} u,\quad {\textrm {and}}\quad {\sqrt {1-m\sin ^{2}\varphi }}=\operatorname {dn} u.$

The latter is sometimes called the *delta amplitude* and written as Δ(*φ*) = dn *u*. Sometimes the literature also refers to the *complementary parameter*, the *complementary modulus,* or the *complementary modular angle*. These are further defined in the article on quarter periods.

In this notation, the use of a vertical bar as delimiter indicates that the argument following it is the "parameter" (as defined above), while the backslash indicates that it is the modular angle. The use of a semicolon implies that the argument preceding it is the sine of the amplitude: $F(\varphi ,\sin \alpha )=F\left(\varphi \mid \sin ^{2}\alpha \right)=F(\varphi \setminus \alpha )=F(\sin \varphi ;\sin \alpha ).$ This potentially confusing use of different argument delimiters is traditional in elliptic integrals and much of the notation is compatible with that used in the reference book by Abramowitz and Stegun and that used in the integral tables by Gradshteyn and Ryzhik.

There are still other conventions for the notation of elliptic integrals employed in the literature. The notation with interchanged arguments, *F*(*k*, *φ*), is often encountered; and similarly *E*(*k*, *φ*) for the integral of the second kind. Abramowitz and Stegun substitute the integral of the first kind, *F*(*φ*, *k*), for the argument φ in their definition of the integrals of the second and third kinds, unless this argument is followed by a vertical bar: i.e. *E*(*F*(*φ*, *k*) | *k*2) for *E*(*φ* | *k*2). Moreover, their complete integrals employ the *parameter* *k*2 as argument in place of the modulus *k*, i.e. *K*(*k*2) rather than *K*(*k*). And the integral of the third kind defined by Gradshteyn and Ryzhik, Π(*φ*, *n*, *k*), puts the amplitude φ first and not the "characteristic" n.

Thus one must be careful with the notation when using these functions, because various reputable references and software packages use different conventions in the definitions of the elliptic functions. For example, Wolfram's Mathematica software and Wolfram Alpha define the complete elliptic integral of the first kind in terms of the parameter *m*, instead of the elliptic modulus *k*.

## Incomplete elliptic integral of the first kind

The **incomplete elliptic integral of the first kind** F is defined as

$F(\varphi ,k)=F\left(\varphi \mid k^{2}\right)=F(\sin \varphi ;k)=\int _{0}^{\varphi }{\frac {d\theta }{\sqrt {1-k^{2}\sin ^{2}\theta }}}.$

This is Legendre's trigonometric form of the elliptic integral; substituting *t* = sin *θ* and *x* = sin *φ*, one obtains Jacobi's algebraic form:

$F(x;k)=\int _{0}^{x}{\frac {dt}{\sqrt {\left(1-t^{2}\right)\left(1-k^{2}t^{2}\right)}}}.$

Equivalently, in terms of the amplitude and modular angle one has: $F(\varphi \setminus \alpha )=F(\varphi ,\sin \alpha )=\int _{0}^{\varphi }{\frac {d\theta }{\sqrt {1-\left(\sin \theta \sin \alpha \right)^{2}}}}.$

With *x* = sn(*u*, *k*) one has: $F(x;k)=u;$ demonstrating that this Jacobian elliptic function is a simple inverse of the incomplete elliptic integral of the first kind.

The incomplete elliptic integral of the first kind has following addition theorem: $F\left[\arctan(x),k\right]+F\left[\arctan(y),k\right]=F\left[\arctan \left({\frac {x{\sqrt {k'^{2}y^{2}+1}}}{\sqrt {y^{2}+1}}}\right)+\arctan \left({\frac {y{\sqrt {k'^{2}x^{2}+1}}}{\sqrt {x^{2}+1}}}\right),k\right]$

The elliptic modulus can be transformed that way: $F\left[\arcsin(x),k\right]={\frac {2}{1+{\sqrt {1-k^{2}}}}}F{\left[\arcsin \left({\frac {\left(1+{\sqrt {1-k^{2}}}\right)x}{1+{\sqrt {1-k^{2}x^{2}}}}}\right),{\frac {1-{\sqrt {1-k^{2}}}}{1+{\sqrt {1-k^{2}}}}}\right]}$

## Incomplete elliptic integral of the second kind

The **incomplete elliptic integral of the second kind** *E* in Legendre's trigonometric form is

$E(\varphi ,k)=E\left(\varphi \,|\,k^{2}\right)=E(\sin \varphi ;k)=\int _{0}^{\varphi }{\sqrt {1-k^{2}\sin ^{2}\theta }}\,d\theta .$

Substituting *t* = sin *θ* and *x* = sin *φ*, one obtains Jacobi's algebraic form:

$E(x;k)=\int _{0}^{x}{\frac {\sqrt {1-k^{2}t^{2}}}{\sqrt {1-t^{2}}}}\,dt.$

Equivalently, in terms of the amplitude and modular angle: $E(\varphi \setminus \alpha )=E(\varphi ,\sin \alpha )=\int _{0}^{\varphi }{\sqrt {1-\left(\sin \theta \sin \alpha \right)^{2}}}\,d\theta .$

Relations with the Jacobi elliptic functions include ${\begin{aligned}E{\left(\operatorname {sn} (u;k);k\right)}=\int _{0}^{u}\operatorname {dn} ^{2}(w;k)\,dw&=u-k^{2}\int _{0}^{u}\operatorname {sn} ^{2}(w;k)\,dw\\[1ex]&=\left(1-k^{2}\right)u+k^{2}\int _{0}^{u}\operatorname {cn} ^{2}(w;k)\,dw.\end{aligned}}$

The meridian arc length from the equator to latitude *φ* is written in terms of *E*: $m(\varphi )=a\left(E(\varphi ,e)+{\frac {d^{2}}{d\varphi ^{2}}}E(\varphi ,e)\right),$ where *a* is the semi-major axis, and *e* is the eccentricity.

The incomplete elliptic integral of the second kind has following addition theorem: ${\begin{aligned}&E{\left[\arctan(x),k\right]}+E{\left[\arctan(y),k\right]}\\[1ex]&\quad =E{\left[\arctan \left({\frac {x{\sqrt {k'^{2}y^{2}+1}}}{\sqrt {y^{2}+1}}}\right)+\arctan \left({\frac {y{\sqrt {k'^{2}x^{2}+1}}}{\sqrt {x^{2}+1}}}\right),k\right]}\\[1ex]&\qquad +{\frac {k^{2}xy}{k'^{2}x^{2}y^{2}+x^{2}+y^{2}+1}}\left({\frac {x{\sqrt {k'^{2}y^{2}+1}}}{\sqrt {y^{2}+1}}}+{\frac {y{\sqrt {k'^{2}x^{2}+1}}}{\sqrt {x^{2}+1}}}\right)\end{aligned}}$

The elliptic modulus can be transformed that way: ${\begin{aligned}E{\left[\arcsin(x),k\right]}&=\left(1+{\sqrt {1-k^{2}}}\right)E{\left[\arcsin \left({\frac {\left(1+{\sqrt {1-k^{2}}}\right)x}{1+{\sqrt {1-k^{2}x^{2}}}}}\right),{\frac {1-{\sqrt {1-k^{2}}}}{1+{\sqrt {1-k^{2}}}}}\right]}\\[.5ex]&\quad -{\sqrt {1-k^{2}}}F{\left[\arcsin(x),k\right]}+{\frac {k^{2}x{\sqrt {1-x^{2}}}}{1+{\sqrt {1-k^{2}x^{2}}}}}\end{aligned}}$

## Incomplete elliptic integral of the third kind

The **incomplete elliptic integral of the third kind** Π is $\Pi (n;\varphi \setminus \alpha )=\int _{0}^{\varphi }{\frac {1}{1-n\sin ^{2}\theta }}{\frac {d\theta }{\sqrt {1-\left(\sin \theta \sin \alpha \right)^{2}}}}$

or

$\Pi (n;\varphi \,|\,m)=\int _{0}^{\sin \varphi }{\frac {1}{1-nt^{2}}}{\frac {dt}{\sqrt {\left(1-mt^{2}\right)\left(1-t^{2}\right)}}}.$

The number *n* is called the **characteristic** and can take on any value, independently of the other arguments. Note though that the value Π(1; ⁠π/2⁠ | *m*) is infinite, for any *m*.

A relation with the Jacobian elliptic functions is $\Pi \left(n;\,\operatorname {am} (u;k);\,k\right)=\int _{0}^{u}{\frac {dw}{1-n\,\operatorname {sn} ^{2}(w;k)}}.$

The meridian arc length from the equator to latitude *φ* is also related to a special case of Π:

$m(\varphi )=a\left(1-e^{2}\right)\Pi \left(e^{2};\varphi \,|\,e^{2}\right).$

## Complete elliptic integral of the first kind

Elliptic Integrals are said to be 'complete' when the amplitude *φ* = ⁠π/2⁠ and therefore *x* = 1. The **complete elliptic integral of the first kind** *K* may thus be defined as $K(k)=\int _{0}^{\tfrac {\pi }{2}}{\frac {d\theta }{\sqrt {1-k^{2}\sin ^{2}\theta }}}=\int _{0}^{1}{\frac {dt}{\sqrt {\left(1-t^{2}\right)\left(1-k^{2}t^{2}\right)}}},$ or more compactly in terms of the incomplete integral of the first kind as $K(k)=F\left({\tfrac {\pi }{2}},k\right)=F\left({\tfrac {\pi }{2}}\,|\,k^{2}\right)=F(1;k).$

It can be expressed as a power series $K(k)={\frac {\pi }{2}}\sum _{n=0}^{\infty }\left({\frac {(2n)!}{2^{2n}(n!)^{2}}}\right)^{2}k^{2n}={\frac {\pi }{2}}\sum _{n=0}^{\infty }\left(P_{2n}(0)\right)^{2}k^{2n},$

where *P**n* is the Legendre polynomials, which is equivalent to

$K(k)={\frac {\pi }{2}}\left(1+\left({\frac {1}{2}}\right)^{2}k^{2}+\left({\frac {1\cdot 3}{2\cdot 4}}\right)^{2}k^{4}+\cdots +\left({\frac {\left(2n-1\right)!!}{\left(2n\right)!!}}\right)^{2}k^{2n}+\cdots \right),$

where *n*!! denotes the double factorial. In terms of the Gauss hypergeometric function, the complete elliptic integral of the first kind can be expressed as

$K(k)={\tfrac {\pi }{2}}\,{}_{2}F_{1}\left({\tfrac {1}{2}},{\tfrac {1}{2}};1;k^{2}\right).$

The complete elliptic integral of the first kind is sometimes called the quarter period. It can be computed very efficiently in terms of the arithmetic–geometric mean: $K(k)={\frac {\pi }{2\operatorname {agm} \left(1,{\sqrt {1-k^{2}}}\right)}}.$

Therefore, the modulus can be transformed as:

${\begin{aligned}K(k)&={\frac {\pi }{2\operatorname {agm} \left(1,{\sqrt {1-k^{2}}}\right)}}\\[4pt]&={\frac {\pi }{2\operatorname {agm} \left({\frac {1}{2}}+{\frac {\sqrt {1-k^{2}}}{2}},{\sqrt[{4}]{1-k^{2}}}\right)}}\\[4pt]&={\frac {\pi }{\left(1+{\sqrt {1-k^{2}}}\right)\operatorname {agm} \left(1,{\frac {2{\sqrt[{4}]{1-k^{2}}}}{1+{\sqrt {1-k^{2}}}}}\right)}}\\[4pt]&={\frac {2}{1+{\sqrt {1-k^{2}}}}}K{\left({\frac {1-{\sqrt {1-k^{2}}}}{1+{\sqrt {1-k^{2}}}}}\right)}\end{aligned}}$

This expression is valid for all $n\in \mathbb {N}$ and 0 ≤ *k* ≤ 1:

$K(k)=n\left[\sum _{a=1}^{n}\operatorname {dn} \left({\frac {2a}{n}}K(k);k\right)\right]^{-1}K\left[k^{n}\prod _{a=1}^{n}\operatorname {sn} \left({\frac {2a-1}{n}}K(k);k\right)^{2}\right]$

### Relation to the gamma function

If *k*2 = *λ*(*i*√*r*) and $r\in \mathbb {Q} ^{+}$ (where λ is the modular lambda function), then *K*(*k*) is expressible in closed form in terms of the gamma function. For example, *r* = 2, *r* = 3 and *r* = 7 give, respectively,

$K{\left({\sqrt {2}}-1\right)}={\frac {\Gamma {\left({\frac {1}{8}}\right)}\Gamma {\left({\frac {3}{8}}\right)}{\sqrt {{\sqrt {2}}+1}}}{8{\sqrt[{4}]{2}}{\sqrt {\pi }}}},$

and

$K\left({\frac {{\sqrt {3}}-1}{2{\sqrt {2}}}}\right)={\frac {1}{8\pi }}{\sqrt[{4}]{3}}\,{\sqrt[{3}]{4}}\,\Gamma \left({\frac {1}{3}}\right)^{3}$

and

$K\left({\frac {3-{\sqrt {7}}}{4{\sqrt {2}}}}\right)={\frac {\Gamma \left({\frac {1}{7}}\right)\Gamma \left({\frac {2}{7}}\right)\Gamma \left({\frac {4}{7}}\right)}{4{\sqrt[{4}]{7}}\pi }}.$

More generally, the condition that ${\frac {iK'}{K}}={\frac {iK\left({\sqrt {1-k^{2}}}\right)}{K(k)}}$ be in an imaginary quadratic field is sufficient. For instance, if *k* = *e*5*πi*/6, then ⁠*iK*′/*K*⁠ = *e*2*πi*/3 and

$K{\left(e^{5\pi i/6}\right)}={\frac {e^{-\pi i/12}\Gamma ^{3}{\left({\frac {1}{3}}\right)}{\sqrt[{4}]{3}}}{4{\sqrt[{3}]{2}}\pi }}.$

The second formula above, written as ${\frac {\Gamma \left({\frac {1}{3}}\right)^{3}}{\pi }}=2^{7/3}\,3^{-1/4}\,K{\left({\tfrac {{\sqrt {3}}-1}{2{\sqrt {2}}}}\right)}$ , can be completed by 5 equations showing that ${\frac {\Gamma \left({\frac {1}{k}}\right)^{k/2}}{\sqrt {\pi }}}$ is a period for all even divisors k of $24$ :

${\begin{aligned}{\frac {\Gamma \left({\frac {1}{4}}\right)^{2}}{\sqrt {\pi }}}&=4\,K\left({\tfrac {1}{\sqrt {2}}}\right)\\[1ex]{\frac {\Gamma \left({\frac {1}{6}}\right)^{3}}{\sqrt {\pi }}}&=2^{11/3}\cdot 3\cdot K\left({\tfrac {{\sqrt {3}}-1}{2{\sqrt {2}}}}\right)^{2}\\[1ex]{\frac {\Gamma \left({\frac {1}{8}}\right)^{4}}{\sqrt {\pi }}}&=2^{17/2}\,K\left({\tfrac {1}{\sqrt {2}}}\right)\,K\left({\sqrt {2}}-1\right)^{2}\\[1ex]{\frac {\Gamma \left({\frac {1}{12}}\right)^{6}}{\sqrt {\pi }}}&=2^{55/6}\,3^{7/4}\,({\sqrt {3}}+1)^{3}\,K\left({\tfrac {{\sqrt {3}}-1}{2{\sqrt {2}}}}\right)^{2}\,K\left({\tfrac {1}{\sqrt {2}}}\right)^{3}\\[1ex]{\frac {\Gamma \left({\frac {1}{24}}\right)^{12}}{\sqrt {\pi }}}&=2^{89/3}3^{25/4}({\sqrt {2}}+1)^{6}({\sqrt {3}}-1)^{3}K\!\left({\tfrac {1}{\sqrt {2}}}\right)^{3}K\!\left({\tfrac {{\sqrt {3}}-1}{2{\sqrt {2}}}}\right)^{4}K\!\left((2-{\sqrt {3}})({\sqrt {3}}-{\sqrt {2}})\right)^{6}\end{aligned}}$

### Asymptotic expressions

$K\left(k\right)\approx {\frac {\pi }{2}}+{\frac {\pi }{8}}{\frac {k^{2}}{1-k^{2}}}-{\frac {\pi }{16}}{\frac {k^{4}}{1-k^{2}}}$ This approximation has a relative precision better than 3×10−4 for *k* < ⁠1/2⁠. Keeping only the first two terms is correct to 0.01 precision for *k* < ⁠1/2⁠.

### Differential equation

The differential equation for the elliptic integral of the first kind is ${\frac {d}{dk}}\left(k\left(1-k^{2}\right){\frac {dK(k)}{dk}}\right)=k\,K(k)$

A second solution to this equation is $K\left({\sqrt {1-k^{2}}}\right)$ . This solution satisfies the relation ${\frac {d}{dk}}K(k)={\frac {E(k)}{k\left(1-k^{2}\right)}}-{\frac {K(k)}{k}}.$

### Continued fraction

A continued fraction expansion is: ${\begin{aligned}{\frac {K(k)}{2\pi }}&=-{\frac {1}{4}}+\sum _{n=0}^{\infty }{\frac {q^{n}}{1+q^{2n}}}\\&=-{\frac {1}{4}}+{\cfrac {1}{1-q+{\cfrac {\left(1-q\right)^{2}}{1-q^{3}+{\cfrac {q\left(1-q^{2}\right)^{2}}{1-q^{5}+{\cfrac {q^{2}\left(1-q^{3}\right)^{2}}{1-q^{7}+{\cfrac {q^{3}\left(1-q^{4}\right)^{2}}{1-q^{9}+\cdots }}}}}}}}}},\end{aligned}}$ where the nome is $q=q(k)=\exp[-\pi K'(k)/K(k)]$ in its definition.

### Inverting the period ratio

Here, we use the complete elliptic integral of the first kind with the *parameter* m instead, because the squaring function introduces problems when inverting in the complex plane. So let $K[m]=\int _{0}^{\pi /2}{\dfrac {d\theta }{\sqrt {1-m\sin ^{2}\theta }}}$ and let $\theta _{2}(\tau )=2e^{\pi i\tau /4}\sum _{n=0}^{\infty }q^{n(n+1)},\quad q=e^{\pi i\tau },\,\operatorname {Im} \tau >0,$ $\theta _{3}(\tau )=1+2\sum _{n=1}^{\infty }q^{n^{2}},\quad q=e^{\pi i\tau },\,\operatorname {Im} \tau >0$ be the theta functions.

The equation $\tau =i{\frac {K[1-m]}{K[m]}}$ can then be solved (provided that a solution m exists) by $m={\frac {\theta _{2}(\tau )^{4}}{\theta _{3}(\tau )^{4}}}$ which is in fact the modular lambda function.

For the purposes of computation, the error analysis is given by $\left|{e}^{-\pi i\tau /4}\theta _{2}\!\left(\tau \right)-2\sum _{n=0}^{N-1}{q}^{n\left(n+1\right)}\right|\leq {\begin{cases}{\frac {2{\left|q\right|}^{N\left(N+1\right)}}{1-\left|q\right|^{2N+1}}},&\left|q\right|^{2N+1}<1\\\infty ,&{\text{otherwise}}\\\end{cases}}\;$ $\left|\theta _{3}\!\left(\tau \right)-\left(1+2\sum _{n=1}^{N-1}{q}^{n^{2}}\right)\right|\leq {\begin{cases}{\frac {2{\left|q\right|}^{N^{2}}}{1-\left|q\right|^{2N+1}}},&\left|q\right|^{2N+1}<1\\\infty ,&{\text{otherwise}}\\\end{cases}}\;$ where $N\in \mathbb {Z} _{\geq 1}$ and $\operatorname {Im} \tau >0$ .

Also $K[m]={\frac {\pi }{2}}\theta _{3}(\tau )^{2},\quad \tau =i{\frac {K[1-m]}{K[m]}}$ where $m\in \mathbb {C} \setminus \{0,1\}$ .

## Complete elliptic integral of the second kind

The **complete elliptic integral of the second kind** *E* is defined as

$E(k)=\int _{0}^{\tfrac {\pi }{2}}{\sqrt {1-k^{2}\sin ^{2}\theta }}\,d\theta =\int _{0}^{1}{\frac {\sqrt {1-k^{2}t^{2}}}{\sqrt {1-t^{2}}}}\,dt,$

or more compactly in terms of the incomplete integral of the second kind *E*(*φ*,*k*) as

$E(k)=E\left({\tfrac {\pi }{2}},k\right)=E(1;k).$

For an ellipse with semi-major axis *a* and semi-minor axis *b* and eccentricity *e* = √1 − *b*2/*a*2, the complete elliptic integral of the second kind *E*(*e*) is equal to one quarter of the circumference *C* of the ellipse measured in units of the semi-major axis *a*. In other words:

$C=4aE(e).$

The complete elliptic integral of the second kind can be expressed as a power series

$E(k)={\frac {\pi }{2}}\sum _{n=0}^{\infty }\left({\frac {(2n)!}{2^{2n}\left(n!\right)^{2}}}\right)^{2}{\frac {k^{2n}}{1-2n}},$

which is equivalent to

$E(k)={\frac {\pi }{2}}\left(1-\left({\frac {1}{2}}\right)^{2}{\frac {k^{2}}{1}}-\left({\frac {1\cdot 3}{2\cdot 4}}\right)^{2}{\frac {k^{4}}{3}}-\cdots -\left({\frac {(2n-1)!!}{(2n)!!}}\right)^{2}{\frac {k^{2n}}{2n-1}}-\cdots \right).$

In terms of the Gauss hypergeometric function, the complete elliptic integral of the second kind can be expressed as

$E(k)={\tfrac {\pi }{2}}\,{}_{2}F_{1}\left({\tfrac {1}{2}},-{\tfrac {1}{2}};1;k^{2}\right).$

The modulus can be transformed that way: $E(k)=\left(1+{\sqrt {1-k^{2}}}\right)\,E\left({\frac {1-{\sqrt {1-k^{2}}}}{1+{\sqrt {1-k^{2}}}}}\right)-{\sqrt {1-k^{2}}}\,K(k)$

### Computation

Like the integral of the first kind, the complete elliptic integral of the second kind can be computed very efficiently using the arithmetic–geometric mean.

Define sequences an and gn, where *a*0 = 1, *g*0 = √1 − *k*2 = *k*′ and the recurrence relations *a**n* + 1 = ⁠*an* + *gn*/2⁠, *g**n* + 1 = √*an gn* hold. Furthermore, define $c_{n}={\sqrt {\left|a_{n}^{2}-g_{n}^{2}\right|}}.$

By definition,

$a_{\infty }=\lim _{n\to \infty }a_{n}=\lim _{n\to \infty }g_{n}=\operatorname {agm} \left(1,{\sqrt {1-k^{2}}}\right).$

Also

$\lim _{n\to \infty }c_{n}=0.$

Then

$E(k)={\frac {\pi }{2a_{\infty }}}\left(1-\sum _{n=0}^{\infty }2^{n-1}c_{n}^{2}\right).$

In practice, the arithmetic-geometric mean would simply be computed up to some limit. This formula converges quadratically for all |*k*| ≤ 1. To speed up computation further, the relation *c**n* + 1 = ⁠*cn*2/4*a**n* + 1⁠ can be used.

Furthermore, if *k*2 = *λ*(*i*√*r*) and $r\in \mathbb {Q} ^{+}$ (where λ is the modular lambda function), then *E*(*k*) is expressible in closed form in terms of $K(k)={\frac {\pi }{2\operatorname {agm} \left(1,{\sqrt {1-k^{2}}}\right)}}$ and hence can be computed without the need for the infinite summation term. For example, *r* = 1, *r* = 3 and *r* = 7 give, respectively,

$E{\left({\frac {1}{\sqrt {2}}}\right)}={\frac {1}{2}}K{\left({\frac {1}{\sqrt {2}}}\right)}+{\frac {\pi }{4K{\left({\frac {1}{\sqrt {2}}}\right)}}},$

and

$E{\left({\frac {{\sqrt {3}}-1}{2{\sqrt {2}}}}\right)}={\frac {3+{\sqrt {3}}}{6}}K{\left({\frac {{\sqrt {3}}-1}{2{\sqrt {2}}}}\right)}+{\frac {\pi {\sqrt {3}}}{12K{\left({\frac {{\sqrt {3}}-1}{2{\sqrt {2}}}}\right)}}},$

and

$E\left({\frac {3-{\sqrt {7}}}{4{\sqrt {2}}}}\right)={\frac {7+2{\sqrt {7}}}{14}}K\left({\frac {3-{\sqrt {7}}}{4{\sqrt {2}}}}\right)+{\frac {\pi {\sqrt {7}}}{28K\left({\frac {3-{\sqrt {7}}}{4{\sqrt {2}}}}\right)}}.$

### Derivative and differential equation

${\frac {dE(k)}{dk}}={\frac {E(k)-K(k)}{k}}$ $\left(k^{2}-1\right){\frac {d}{dk}}\left(k\;{\frac {dE(k)}{dk}}\right)=kE(k)$

A second solution to this equation is *E*(√1 − *k*2) − *K*(√1 − *k*2).

## Complete elliptic integral of the third kind

The **complete elliptic integral of the third kind** Π can be defined as

$\Pi (n,k)=\int _{0}^{\frac {\pi }{2}}{\frac {d\theta }{\left(1-n\sin ^{2}\theta \right){\sqrt {1-k^{2}\sin ^{2}\theta }}}}.$

Note that sometimes the elliptic integral of the third kind is defined with an inverse sign for the *characteristic* *n*, $\Pi '(n,k)=\int _{0}^{\frac {\pi }{2}}{\frac {d\theta }{\left(1+n\sin ^{2}\theta \right){\sqrt {1-k^{2}\sin ^{2}\theta }}}}.$

Just like the complete elliptic integrals of the first and second kind, the complete elliptic integral of the third kind can be computed very efficiently using the arithmetic-geometric mean.

### Partial derivatives

${\begin{aligned}{\frac {\partial \Pi (n,k)}{\partial n}}&={\frac {1}{2\left(k^{2}-n\right)(n-1)}}\left(E(k)+{\frac {1}{n}}\left(k^{2}-n\right)K(k)+{\frac {1}{n}}\left(n^{2}-k^{2}\right)\Pi (n,k)\right)\\[8pt]{\frac {\partial \Pi (n,k)}{\partial k}}&={\frac {k}{n-k^{2}}}\left({\frac {E(k)}{k^{2}-1}}+\Pi (n,k)\right)\end{aligned}}$

## Jacobi zeta function

In 1829, Jacobi defined the **Jacobi zeta function**: $Z(\varphi ,k)=E(\varphi ,k)-{\frac {E(k)}{K(k)}}F(\varphi ,k).$ It is periodic in $\varphi$ with minimal period $\pi$ . It is related to the Jacobi zn function by $Z(\varphi ,k)=\operatorname {zn} (F(\varphi ,k),k)$ . In the literature (e.g. Whittaker and Watson (1927)), sometimes Z means Wikipedia's $\operatorname {zn}$ . Some authors (e.g. King (1924)) use Z for both Wikipedia's Z and $\operatorname {zn}$ .

## Legendre's relation

The Legendre's relation or *Legendre Identity* shows the relation of the integrals K and E of an elliptic modulus and its anti-related counterpart in an integral equation of second degree:

For two modules that are Pythagorean counterparts to each other, this relation is valid:

$K(\varepsilon )E{\left({\sqrt {1-\varepsilon ^{2}}}\right)}+E(\varepsilon )K{\left({\sqrt {1-\varepsilon ^{2}}}\right)}-K(\varepsilon )K{\left({\sqrt {1-\varepsilon ^{2}}}\right)}={\frac {\pi }{2}}$

For example: $K({\color {blueviolet}{\tfrac {3}{5}}})E({\color {blue}{\tfrac {4}{5}}})+E({\color {blueviolet}{\tfrac {3}{5}}})K({\color {blue}{\tfrac {4}{5}}})-K({\color {blueviolet}{\tfrac {3}{5}}})K({\color {blue}{\tfrac {4}{5}}})={\tfrac {1}{2}}\pi$

And for two modules that are tangential counterparts to each other, the following relationship is valid:

$(1+\varepsilon )K(\varepsilon )E({\tfrac {1-\varepsilon }{1+\varepsilon }})+{\tfrac {2}{1+\varepsilon }}E(\varepsilon )K({\tfrac {1-\varepsilon }{1+\varepsilon }})-2K(\varepsilon )K({\tfrac {1-\varepsilon }{1+\varepsilon }})={\tfrac {1}{2}}\pi$

For example: ${\tfrac {4}{3}}K({\color {blue}{\tfrac {1}{3}}})E({\color {green}{\tfrac {1}{2}}})+{\tfrac {3}{2}}E({\color {blue}{\tfrac {1}{3}}})K({\color {green}{\tfrac {1}{2}}})-2K({\color {blue}{\tfrac {1}{3}}})K({\color {green}{\tfrac {1}{2}}})={\tfrac {1}{2}}\pi$

The Legendre's relation for tangential modular counterparts results directly from the Legendre's identity for Pythagorean modular counterparts by using the Landen modular transformation on the Pythagorean counter modulus.

### Special identity for the lemniscatic case

For the lemniscatic case, the elliptic modulus or specific eccentricity ε is equal to half the square root of two. Legendre's identity for the lemniscatic case can be proved as follows:

According to the Chain rule these derivatives hold:

${\frac {\mathrm {d} }{\mathrm {d} y}}\,K{\left({\frac {1}{\sqrt {2}}}\right)}-F\left[\arccos(xy);{\frac {1}{\sqrt {2}}}\right]={\frac {{\sqrt {2}}\,x}{\sqrt {1-x^{4}y^{4}}}}$ ${\frac {\mathrm {d} }{\mathrm {d} y}}\,2E{\left({\frac {1}{\sqrt {2}}}\right)}-K{\left({\frac {1}{\sqrt {2}}}\right)}-2E\left[\arccos(xy);{\frac {1}{\sqrt {2}}}\right]+F\left[\arccos(xy);{\frac {1}{\sqrt {2}}}\right]={\frac {{\sqrt {2}}\,x^{3}y^{2}}{\sqrt {1-x^{4}y^{4}}}}$

By using the Fundamental theorem of calculus these formulas can be generated:

$K{\left({\frac {1}{\sqrt {2}}}\right)}-F{\left(\arccos(x);{\frac {1}{\sqrt {2}}}\right)}=\int _{0}^{1}{\frac {{\sqrt {2}}\,x}{\sqrt {1-x^{4}y^{4}}}}\,\mathrm {d} y$ $2E{\left({\frac {1}{\sqrt {2}}}\right)}-K{\left({\frac {1}{\sqrt {2}}}\right)}-2E{\left(\arccos(x);{\frac {1}{\sqrt {2}}}\right)}+F{\left(\arccos(x);{\frac {1}{\sqrt {2}}}\right)}=\int _{0}^{1}{\frac {{\sqrt {2}}\,x^{3}y^{2}}{\sqrt {1-x^{4}y^{4}}}}\,\mathrm {d} y$

The Linear combination of the two now mentioned integrals leads to the following formula:

${\frac {\sqrt {2}}{\sqrt {1-x^{4}}}}\left\{2E\left({\frac {1}{\sqrt {2}}}\right)-K\left({\frac {1}{\sqrt {2}}}\right)-2E\left[\arccos(x);{\frac {1}{\sqrt {2}}}\right]+F\left[\arccos(x);{\frac {1}{\sqrt {2}}}\right]\right\}\,+$ $+\,{\frac {{\sqrt {2}}\,x^{2}}{\sqrt {1-x^{4}}}}\left\{K\left({\frac {1}{\sqrt {2}}}\right)-F\left[\arccos(x);{\frac {1}{\sqrt {2}}}\right]\right\}=\int _{0}^{1}{\frac {2\,x^{3}(y^{2}+1)}{\sqrt {(1-x^{4})(1-x^{4}\,y^{4})}}}\,\mathrm {d} y$

By forming the original antiderivative related to x from the function now shown using the Product rule this formula results:

${\begin{aligned}&\left[K{\left({\frac {1}{\sqrt {2}}}\right)}-F{\left(\arccos(x);{\frac {1}{\sqrt {2}}}\right)}\right]\left[2E{\left({\frac {1}{\sqrt {2}}}\right)}-K{\left({\frac {1}{\sqrt {2}}}\right)}-2E{\left(\arccos(x);{\frac {1}{\sqrt {2}}}\right)}+F{\left(\arccos(x);{\frac {1}{\sqrt {2}}}\right)}\right]\\[1ex]&=\int _{0}^{1}{\frac {1}{y^{2}}}(y^{2}+1)\left[{\text{artanh}}(y^{2})-{\text{artanh}}\left({\frac {{\sqrt {1-x^{4}}}\,y^{2}}{\sqrt {1-x^{4}y^{4}}}}\right)\right]\mathrm {d} y\end{aligned}}$

If the value $x=1$ is inserted in this integral identity, then the following identity emerges:

${\begin{aligned}K{\left({\frac {1}{\sqrt {2}}}\right)}\left[2\,E\left({\frac {1}{\sqrt {2}}}\right)-K\left({\frac {1}{\sqrt {2}}}\right)\right]&=\int _{0}^{1}{\frac {1}{y^{2}}}(y^{2}+1)\,{\text{artanh}}(y^{2})\,\mathrm {d} y\\&=\left[2\arctan(y)-{\frac {1}{y}}(1-y^{2})\,{\text{artanh}}(y^{2})\right]_{y=0}^{y=1}\\&=2\arctan(1)={\frac {\pi }{2}}\end{aligned}}$

This is how this lemniscatic excerpt from Legendre's identity appears:

$2E\left({\frac {1}{\sqrt {2}}}\right)K\left({\frac {1}{\sqrt {2}}}\right)-K\left({\frac {1}{\sqrt {2}}}\right)^{2}={\frac {\pi }{2}}$

### Generalization for the overall case

Now the modular general case is worked out. For this purpose, the derivatives of the complete elliptic integrals are derived after the modulus $\varepsilon$ and then they are combined. And then the Legendre's identity balance is determined.

Because the derivative of the *circle function* is the negative product of the *identical mapping function* and the reciprocal of the circle function:

${\frac {\mathrm {d} }{\mathrm {d} \varepsilon }}{\sqrt {1-\varepsilon ^{2}}}=-\,{\frac {\varepsilon }{\sqrt {1-\varepsilon ^{2}}}}$

These are the derivatives of K and E shown in this article in the sections above:

${\frac {\mathrm {d} }{\mathrm {d} \varepsilon }}K(\varepsilon )={\frac {1}{\varepsilon (1-\varepsilon ^{2})}}\left[E(\varepsilon )-(1-\varepsilon ^{2})K(\varepsilon )\right]$ ${\frac {\mathrm {d} }{\mathrm {d} \varepsilon }}E(\varepsilon )=-\,{\frac {1}{\varepsilon }}\left[K(\varepsilon )-E(\varepsilon )\right]$

In combination with the derivative of the circle function these derivatives are valid then:

${\frac {\mathrm {d} }{\mathrm {d} \varepsilon }}K({\sqrt {1-\varepsilon ^{2}}})={\frac {1}{\varepsilon (1-\varepsilon ^{2})}}\left[\varepsilon ^{2}K({\sqrt {1-\varepsilon ^{2}}})-E({\sqrt {1-\varepsilon ^{2}}})\right]$ ${\frac {\mathrm {d} }{\mathrm {d} \varepsilon }}E({\sqrt {1-\varepsilon ^{2}}})={\frac {\varepsilon }{1-\varepsilon ^{2}}}\left[K({\sqrt {1-\varepsilon ^{2}}})-E({\sqrt {1-\varepsilon ^{2}}})\right]$

Legendre's identity includes products of any two complete elliptic integrals. For the derivation of the function side from the equation scale of Legendre's identity, the Product rule is now applied in the following:

${\frac {\mathrm {d} }{\mathrm {d} \varepsilon }}K(\varepsilon )E({\sqrt {1-\varepsilon ^{2}}})={\frac {1}{\varepsilon (1-\varepsilon ^{2})}}\left[E(\varepsilon )E({\sqrt {1-\varepsilon ^{2}}})-K(\varepsilon )E({\sqrt {1-\varepsilon ^{2}}})+\varepsilon ^{2}K(\varepsilon )K({\sqrt {1-\varepsilon ^{2}}})\right]$ ${\frac {\mathrm {d} }{\mathrm {d} \varepsilon }}E(\varepsilon )K({\sqrt {1-\varepsilon ^{2}}})={\frac {1}{\varepsilon (1-\varepsilon ^{2})}}\left[-E(\varepsilon )E({\sqrt {1-\varepsilon ^{2}}})+E(\varepsilon )K({\sqrt {1-\varepsilon ^{2}}})-(1-\varepsilon ^{2})K(\varepsilon )K({\sqrt {1-\varepsilon ^{2}}})\right]$ ${\frac {\mathrm {d} }{\mathrm {d} \varepsilon }}K(\varepsilon )K({\sqrt {1-\varepsilon ^{2}}})={\frac {1}{\varepsilon (1-\varepsilon ^{2})}}\left[E(\varepsilon )K({\sqrt {1-\varepsilon ^{2}}})-K(\varepsilon )E({\sqrt {1-\varepsilon ^{2}}})-(1-2\varepsilon ^{2})K(\varepsilon )K({\sqrt {1-\varepsilon ^{2}}})\right]$

Of these three equations, adding the top two equations and subtracting the bottom equation gives this result:

${\frac {\mathrm {d} }{\mathrm {d} \varepsilon }}\left[K(\varepsilon )E({\sqrt {1-\varepsilon ^{2}}})+E(\varepsilon )K({\sqrt {1-\varepsilon ^{2}}})-K(\varepsilon )K({\sqrt {1-\varepsilon ^{2}}})\right]=0$

In relation to the $\varepsilon$ the equation balance constantly gives the value zero.

The previously determined result shall be combined with the Legendre equation to the modulus $\varepsilon =1/{\sqrt {2}}$ that is worked out in the section before:

$2E\left({\frac {1}{\sqrt {2}}}\right)K\left({\frac {1}{\sqrt {2}}}\right)-K\left({\frac {1}{\sqrt {2}}}\right)^{2}={\frac {\pi }{2}}$

The combination of the last two formulas gives the following result:

$K(\varepsilon )E({\sqrt {1-\varepsilon ^{2}}})+E(\varepsilon )K({\sqrt {1-\varepsilon ^{2}}})-K(\varepsilon )K({\sqrt {1-\varepsilon ^{2}}})={\tfrac {1}{2}}\pi$

Because if the derivative of a continuous function constantly takes the value zero, then the concerned function is a constant function. This means that this function results in the same function value for each abscissa value $\varepsilon$ and the associated function graph is therefore a horizontal straight line.
