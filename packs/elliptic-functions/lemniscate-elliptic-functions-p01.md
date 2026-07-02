---
title: "Lemniscate elliptic functions (part 1/2)"
source: https://en.wikipedia.org/wiki/Lemniscate_elliptic_functions
domain: elliptic-functions
license: CC-BY-SA-4.0
tags: elliptic function, jacobi elliptic functions, weierstrass elliptic function, theta function
fetched: 2026-07-02
part: 1/2
---

# Lemniscate elliptic functions

In mathematics, the **lemniscate elliptic functions** are elliptic functions related to the arc length of the lemniscate of Bernoulli. They were first studied by Giulio Fagnano in 1718 and later by Leonhard Euler and Carl Friedrich Gauss, among others.

The **lemniscate sine** and **lemniscate cosine** functions, usually written with the symbols sl and cl (sometimes the symbols sinlem and coslem or sin lemn and cos lemn are used instead), are analogous to the trigonometric functions sine and cosine. While the trigonometric sine relates the arc length to the chord length in a unit-diameter circle $x^{2}+y^{2}=x,$ the lemniscate sine relates the arc length to the chord length of a lemniscate ${\bigl (}x^{2}+y^{2}{\bigr )}{}^{2}=x^{2}-y^{2}.$

The lemniscate functions have periods related to a number $\varpi =$ 2.622057... called the lemniscate constant, the ratio of a lemniscate's perimeter to its diameter. This number is a quartic analog of the (quadratic) $\pi =$ 3.141592..., ratio of perimeter to diameter of a circle.

As complex functions, sl and cl have a square period lattice (a multiple of the Gaussian integers) with fundamental periods $\{(1+i)\varpi ,(1-i)\varpi \},$ and are a special case of two Jacobi elliptic functions on that lattice, $\operatorname {sl} z=\operatorname {sn} (z;-1),$ $\operatorname {cl} z=\operatorname {cd} (z;-1)$ .

Similarly, the **hyperbolic lemniscate sine** slh and **hyperbolic lemniscate cosine** clh have a square period lattice with fundamental periods ${\bigl \{}{\sqrt {2}}\varpi ,{\sqrt {2}}\varpi i{\bigr \}}.$

The lemniscate functions and the hyperbolic lemniscate functions are related to the Weierstrass elliptic function $\wp (z;a,0)$ .


## Lemniscate sine and cosine functions

### Definitions

The lemniscate functions sl and cl can be defined as the solution to the initial value problem:

${\frac {\mathrm {d} }{\mathrm {d} z}}\operatorname {sl} z={\bigl (}1+\operatorname {sl} ^{2}z{\bigr )}\operatorname {cl} z,\ {\frac {\mathrm {d} }{\mathrm {d} z}}\operatorname {cl} z=-{\bigl (}1+\operatorname {cl} ^{2}z{\bigr )}\operatorname {sl} z,\ \operatorname {sl} 0=0,\ \operatorname {cl} 0=1,$

or equivalently as the inverses of an elliptic integral, the Schwarz–Christoffel map from the complex unit disk to a square with corners ${\big \{}{\tfrac {1}{2}}\varpi ,{\tfrac {1}{2}}\varpi i,-{\tfrac {1}{2}}\varpi ,-{\tfrac {1}{2}}\varpi i{\big \}}\colon$

$z=\int _{0}^{\operatorname {sl} z}{\frac {\mathrm {d} t}{\sqrt {1-t^{4}}}}=\int _{\operatorname {cl} z}^{1}{\frac {\mathrm {d} t}{\sqrt {1-t^{4}}}}.$

Beyond that square, the functions can be extended to the complex plane via analytic continuation by successive reflections.

By comparison, the circular sine and cosine can be defined as the solution to the initial value problem:

${\frac {\mathrm {d} }{\mathrm {d} z}}\sin z=\cos z,\ {\frac {\mathrm {d} }{\mathrm {d} z}}\cos z=-\sin z,\ \sin 0=0,\ \cos 0=1,$

or as inverses of a map from the upper half-plane to a half-infinite strip with real part between $-{\tfrac {1}{2}}\pi ,{\tfrac {1}{2}}\pi$ and positive imaginary part:

$z=\int _{0}^{\sin z}{\frac {\mathrm {d} t}{\sqrt {1-t^{2}}}}=\int _{\cos z}^{1}{\frac {\mathrm {d} t}{\sqrt {1-t^{2}}}}.$

### Relation to the lemniscate constant

The lemniscate functions have minimal real period ⁠ $2\varpi$ ⁠, minimal imaginary period ⁠ $2\varpi i$ ⁠ and fundamental complex periods $(1+i)\varpi$ and $(1-i)\varpi$ for a constant ⁠ $\varpi$ ⁠ called the *lemniscate constant*,

$\varpi =2\int _{0}^{1}{\frac {\mathrm {d} t}{\sqrt {1-t^{4}}}}={\frac {{\sqrt {2}}\pi ^{\frac {3}{2}}}{2\left(\Gamma \left({\frac {3}{4}}\right)\right)^{2}}}=2.62205\ldots$

The lemniscate functions satisfy the basic relation $\operatorname {cl} z={\operatorname {sl} }{\bigl (}{\tfrac {1}{2}}\varpi -z{\bigr )},$ analogous to the relation $\cos z={\sin }{\bigl (}{\tfrac {1}{2}}\pi -z{\bigr )}.$

The lemniscate constant ⁠ $\varpi$ ⁠ is a close analog of the circle constant ⁠ $\pi$ ⁠, and many identities involving ⁠ $\pi$ ⁠ have analogues involving ⁠ $\varpi$ ⁠, as identities involving the trigonometric functions have analogues involving the lemniscate functions. For example, Viète's formula for ⁠ $\pi$ ⁠ can be written:

${\frac {2}{\pi }}={\sqrt {\frac {1}{2}}}\cdot {\sqrt {{\frac {1}{2}}+{\frac {1}{2}}{\sqrt {\frac {1}{2}}}}}\cdot {\sqrt {{\frac {1}{2}}+{\frac {1}{2}}{\sqrt {{\frac {1}{2}}+{\frac {1}{2}}{\sqrt {\frac {1}{2}}}}}}}\cdots$

An analogous formula for ⁠ $\varpi$ ⁠ is:

${\frac {2}{\varpi }}={\sqrt {\frac {1}{2}}}\cdot {\sqrt {{\frac {1}{2}}+{\frac {1}{2}}{\bigg /}\!{\sqrt {\frac {1}{2}}}}}\cdot {\sqrt {{\frac {1}{2}}+{\frac {1}{2}}{\Bigg /}\!{\sqrt {{\frac {1}{2}}+{\frac {1}{2}}{\bigg /}\!{\sqrt {\frac {1}{2}}}}}}}\cdots$

The Machin formula for ⁠ $\pi$ ⁠ is ${\textstyle {\tfrac {1}{4}}\pi =4\arctan {\tfrac {1}{5}}-\arctan {\tfrac {1}{239}},}$ and several similar formulas for ⁠ $\pi$ ⁠ can be developed using trigonometric angle sum identities, e.g. Euler's formula ${\textstyle {\tfrac {1}{4}}\pi =\arctan {\tfrac {1}{2}}+\arctan {\tfrac {1}{3}}}$ . Analogous formulas can be developed for ⁠ $\varpi$ ⁠, including the following found by Gauss: ${\tfrac {1}{2}}\varpi =2\operatorname {arcsl} {\tfrac {1}{2}}+\operatorname {arcsl} {\tfrac {7}{23}}.$

The lemniscate and circle constants were found by Gauss to be related to each-other by the arithmetic-geometric mean ⁠ M ⁠:

${\frac {\pi }{\varpi }}=M{\left(1,{\sqrt {2}}\!~\right)}$


## Argument identities

### Zeros, poles and symmetries

The lemniscate functions cl and sl are even and odd functions, respectively,

${\begin{aligned}\operatorname {cl} (-z)&=\operatorname {cl} z\\[6mu]\operatorname {sl} (-z)&=-\operatorname {sl} z\end{aligned}}$

At translations of ${\tfrac {1}{2}}\varpi ,$ cl and sl are exchanged, and at translations of ${\tfrac {1}{2}}i\varpi$ they are additionally rotated and reciprocated:

${\begin{aligned}{\operatorname {cl} }{\bigl (}z\pm {\tfrac {1}{2}}\varpi {\bigr )}&=\mp \operatorname {sl} z,&{\operatorname {cl} }{\bigl (}z\pm {\tfrac {1}{2}}i\varpi {\bigr )}&={\frac {\mp i}{\operatorname {sl} z}}\\[6mu]{\operatorname {sl} }{\bigl (}z\pm {\tfrac {1}{2}}\varpi {\bigr )}&=\pm \operatorname {cl} z,&{\operatorname {sl} }{\bigl (}z\pm {\tfrac {1}{2}}i\varpi {\bigr )}&={\frac {\pm i}{\operatorname {cl} z}}\end{aligned}}$

Doubling these to translations by a unit-Gaussian-integer multiple of $\varpi$ (that is, $\pm \varpi$ or $\pm i\varpi$ ), negates each function, an involution:

${\begin{aligned}\operatorname {cl} (z+\varpi )&=\operatorname {cl} (z+i\varpi )=-\operatorname {cl} z\\[4mu]\operatorname {sl} (z+\varpi )&=\operatorname {sl} (z+i\varpi )=-\operatorname {sl} z\end{aligned}}$

As a result, both functions are invariant under translation by an even-Gaussian-integer multiple of $\varpi$ . That is, a displacement $(a+bi)\varpi ,$ with $a+b=2k$ for integers ⁠ a ⁠, ⁠ b ⁠, and ⁠ k ⁠.

${\begin{aligned}{\operatorname {cl} }{\bigl (}z+(1+i)\varpi {\bigr )}&={\operatorname {cl} }{\bigl (}z+(1-i)\varpi {\bigr )}=\operatorname {cl} z\\[4mu]{\operatorname {sl} }{\bigl (}z+(1+i)\varpi {\bigr )}&={\operatorname {sl} }{\bigl (}z+(1-i)\varpi {\bigr )}=\operatorname {sl} z\end{aligned}}$

This makes them elliptic functions (doubly periodic meromorphic functions in the complex plane) with a diagonal square period lattice of fundamental periods $(1+i)\varpi$ and $(1-i)\varpi$ . Elliptic functions with a square period lattice are more symmetrical than arbitrary elliptic functions, following the symmetries of the square.

Reflections and quarter-turn rotations of lemniscate function arguments have simple expressions:

${\begin{aligned}\operatorname {cl} {\bar {z}}&={\overline {\operatorname {cl} z}}\\[6mu]\operatorname {sl} {\bar {z}}&={\overline {\operatorname {sl} z}}\\[4mu]\operatorname {cl} iz&={\frac {1}{\operatorname {cl} z}}\\[6mu]\operatorname {sl} iz&=i\operatorname {sl} z\end{aligned}}$

The sl function has simple zeros at Gaussian integer multiples of ⁠ $\varpi$ ⁠, complex numbers of the form $a\varpi +b\varpi i$ for integers ⁠ a ⁠ and ⁠ b ⁠. It has simple poles at Gaussian half-integer multiples of ⁠ $\varpi$ ⁠, complex numbers of the form ${\bigl (}a+{\tfrac {1}{2}}{\bigr )}\varpi +{\bigl (}b+{\tfrac {1}{2}}{\bigr )}\varpi i$ , with residues $(-1)^{a-b+1}i$ . The cl function is reflected and offset from the sl function, $\operatorname {cl} z={\operatorname {sl} }{\bigl (}{\tfrac {1}{2}}\varpi -z{\bigr )}$ . It has zeros for arguments ${\bigl (}a+{\tfrac {1}{2}}{\bigr )}\varpi +b\varpi i$ and poles for arguments $a\varpi +{\bigl (}b+{\tfrac {1}{2}}{\bigr )}\varpi i,$ with residues $(-1)^{a-b}i.$

Also

$\operatorname {sl} z=\operatorname {sl} w\leftrightarrow z=(-1)^{m+n}w+(m+ni)\varpi$

for some $m,n\in \mathbb {Z}$ and

$\operatorname {sl} ((1\pm i)z)=(1\pm i){\frac {\operatorname {sl} z}{\operatorname {sl} 'z}}.$

The last formula is a special case of complex multiplication. Analogous formulas can be given for $\operatorname {sl} ((n+mi)z)$ where $n+mi$ is any Gaussian integer – the function $\operatorname {sl}$ has complex multiplication by $\mathbb {Z} [i]$ .

There are also infinite series reflecting the distribution of the zeros and poles of sl:

${\frac {1}{\operatorname {sl} z}}=\sum _{(n,k)\in \mathbb {Z} ^{2}}{\frac {(-1)^{n+k}}{z+n\varpi +k\varpi i}}$

$\operatorname {sl} z=-i\sum _{(n,k)\in \mathbb {Z} ^{2}}{\frac {(-1)^{n+k}}{z+(n+1/2)\varpi +(k+1/2)\varpi i}}.$

### Pythagorean-like identity

The lemniscate functions satisfy a Pythagorean-like identity:

$\operatorname {cl^{2}} z+\operatorname {sl^{2}} z+\operatorname {cl^{2}} z\,\operatorname {sl^{2}} z=1$

As a result, the parametric equation $(x,y)=(\operatorname {cl} t,\operatorname {sl} t)$ parametrizes the quartic curve $x^{2}+y^{2}+x^{2}y^{2}=1.$

This identity can alternately be rewritten:

${\bigl (}1+\operatorname {cl^{2}} z{\bigr )}{\bigl (}1+\operatorname {sl^{2}} z{\bigr )}=2$

$\operatorname {cl^{2}} z={\frac {1-\operatorname {sl^{2}} z}{1+\operatorname {sl^{2}} z}},\quad \operatorname {sl^{2}} z={\frac {1-\operatorname {cl^{2}} z}{1+\operatorname {cl^{2}} z}}$

Defining a tangent-sum operator as $a\oplus b\mathrel {:=} \tan(\arctan a+\arctan b)={\frac {a+b}{1-ab}},$ gives:

$\operatorname {cl^{2}} z\oplus \operatorname {sl^{2}} z=1.$

### Derivatives and integrals

The derivatives are as follows:

${\begin{aligned}{\frac {\mathrm {d} }{\mathrm {d} z}}\operatorname {cl} z=\operatorname {cl'} z&=-{\bigl (}1+\operatorname {cl^{2}} z{\bigr )}\operatorname {sl} z=-{\frac {2\operatorname {sl} z}{\operatorname {sl} ^{2}z+1}}\\\operatorname {cl'^{2}} z&=1-\operatorname {cl^{4}} z\\[5mu]{\frac {\mathrm {d} }{\mathrm {d} z}}\operatorname {sl} z=\operatorname {sl'} z&={\bigl (}1+\operatorname {sl^{2}} z{\bigr )}\operatorname {cl} z={\frac {2\operatorname {cl} z}{\operatorname {cl} ^{2}z+1}}\\\operatorname {sl'^{2}} z&=1-\operatorname {sl^{4}} z\end{aligned}}$

${\begin{aligned}{\frac {\mathrm {d} }{\mathrm {d} z}}\,{\tilde {\operatorname {cl} }}\,z&=-2\,{\tilde {\operatorname {sl} }}\,z\,\operatorname {cl} z-{\frac {{\tilde {\operatorname {sl} }}\,z}{\operatorname {cl} z}}\\{\frac {\mathrm {d} }{\mathrm {d} z}}\,{\tilde {\operatorname {sl} }}\,z&=2\,{\tilde {\operatorname {cl} }}\,z\,\operatorname {cl} z-{\frac {{\tilde {\operatorname {cl} }}\,z}{\operatorname {cl} z}}\end{aligned}}$

The second derivatives of lemniscate sine and lemniscate cosine are their negative duplicated cubes:

${\frac {\mathrm {d} ^{2}}{\mathrm {d} z^{2}}}\operatorname {cl} z=-2\operatorname {cl^{3}} z$

${\frac {\mathrm {d} ^{2}}{\mathrm {d} z^{2}}}\operatorname {sl} z=-2\operatorname {sl^{3}} z$

The lemniscate functions can be integrated using the inverse tangent function:

${\begin{aligned}\int \operatorname {cl} z\mathop {\mathrm {d} z} &=\arctan \operatorname {sl} z+C\\\int \operatorname {sl} z\mathop {\mathrm {d} z} &=-\arctan \operatorname {cl} z+C\\\int {\tilde {\operatorname {cl} }}\,z\,\mathrm {d} z&={\frac {{\tilde {\operatorname {sl} }}\,z}{\operatorname {cl} z}}+C\\\int {\tilde {\operatorname {sl} }}\,z\,\mathrm {d} z&=-{\frac {{\tilde {\operatorname {cl} }}\,z}{\operatorname {cl} z}}+C\end{aligned}}$

### Argument sum and multiple identities

Like the trigonometric functions, the lemniscate functions satisfy argument sum and difference identities. The original identity used by Fagnano for bisection of the lemniscate was:

$\operatorname {sl} (u+v)={\frac {\operatorname {sl} u\,\operatorname {sl'} v+\operatorname {sl} v\,\operatorname {sl'} u}{1+\operatorname {sl^{2}} u\,\operatorname {sl^{2}} v}}$

The derivative and Pythagorean-like identities can be used to rework the identity used by Fagano in terms of sl and cl. Defining a tangent-sum operator $a\oplus b\mathrel {:=} \tan(\arctan a+\arctan b)$ and tangent-difference operator $a\ominus b\mathrel {:=} a\oplus (-b),$ the argument sum and difference identities can be expressed as:

${\begin{aligned}\operatorname {cl} (u+v)&=\operatorname {cl} u\,\operatorname {cl} v\ominus \operatorname {sl} u\,\operatorname {sl} v={\frac {\operatorname {cl} u\,\operatorname {cl} v-\operatorname {sl} u\,\operatorname {sl} v}{1+\operatorname {sl} u\,\operatorname {cl} u\,\operatorname {sl} v\,\operatorname {cl} v}}\\[2mu]\operatorname {cl} (u-v)&=\operatorname {cl} u\,\operatorname {cl} v\oplus \operatorname {sl} u\,\operatorname {sl} v\\[2mu]\operatorname {sl} (u+v)&=\operatorname {sl} u\,\operatorname {cl} v\oplus \operatorname {cl} u\,\operatorname {sl} v={\frac {\operatorname {sl} u\,\operatorname {cl} v+\operatorname {cl} u\,\operatorname {sl} v}{1-\operatorname {sl} u\,\operatorname {cl} u\,\operatorname {sl} v\,\operatorname {cl} v}}\\[2mu]\operatorname {sl} (u-v)&=\operatorname {sl} u\,\operatorname {cl} v\ominus \operatorname {cl} u\,\operatorname {sl} v\end{aligned}}$

These resemble their trigonometric analogs:

${\begin{aligned}\cos(u\pm v)&=\cos u\,\cos v\mp \sin u\,\sin v\\[6mu]\sin(u\pm v)&=\sin u\,\cos v\pm \cos u\,\sin v\end{aligned}}$

In particular, to compute the complex-valued functions in real components,

${\begin{aligned}\operatorname {cl} (x+iy)&={\frac {\operatorname {cl} x-i\operatorname {sl} x\,\operatorname {sl} y\,\operatorname {cl} y}{\operatorname {cl} y+i\operatorname {sl} x\,\operatorname {cl} x\,\operatorname {sl} y}}\\[4mu]&={\frac {\operatorname {cl} x\,\operatorname {cl} y\left(1-\operatorname {sl} ^{2}x\,\operatorname {sl} ^{2}y\right)}{\operatorname {cl} ^{2}y+\operatorname {sl} ^{2}x\,\operatorname {cl} ^{2}x\,\operatorname {sl} ^{2}y}}-i{\frac {\operatorname {sl} x\,\operatorname {sl} y\left(\operatorname {cl} ^{2}x+\operatorname {cl} ^{2}y\right)}{\operatorname {cl} ^{2}y+\operatorname {sl} ^{2}x\,\operatorname {cl} ^{2}x\,\operatorname {sl} ^{2}y}}\\[12mu]\operatorname {sl} (x+iy)&={\frac {\operatorname {sl} x+i\operatorname {cl} x\,\operatorname {sl} y\,\operatorname {cl} y}{\operatorname {cl} y-i\operatorname {sl} x\,\operatorname {cl} x\,\operatorname {sl} y}}\\[4mu]&={\frac {\operatorname {sl} x\,\operatorname {cl} y\left(1-\operatorname {cl} ^{2}x\,\operatorname {sl} ^{2}y\right)}{\operatorname {cl} ^{2}y+\operatorname {sl} ^{2}x\,\operatorname {cl} ^{2}x\,\operatorname {sl} ^{2}y}}+i{\frac {\operatorname {cl} x\,\operatorname {sl} y\left(\operatorname {sl} ^{2}x+\operatorname {cl} ^{2}y\right)}{\operatorname {cl} ^{2}y+\operatorname {sl} ^{2}x\,\operatorname {cl} ^{2}x\,\operatorname {sl} ^{2}y}}\end{aligned}}$

Gauss discovered that

${\frac {\operatorname {sl} (u-v)}{\operatorname {sl} (u+v)}}={\frac {\operatorname {sl} ((1+i)u)-\operatorname {sl} ((1+i)v)}{\operatorname {sl} ((1+i)u)+\operatorname {sl} ((1+i)v)}}$

where $u,v\in \mathbb {C}$ such that both sides are well-defined.

Also

$\operatorname {sl} (u+v)\operatorname {sl} (u-v)={\frac {\operatorname {sl} ^{2}u-\operatorname {sl} ^{2}v}{1+\operatorname {sl} ^{2}u\operatorname {sl} ^{2}v}}$

where $u,v\in \mathbb {C}$ such that both sides are well-defined; this resembles the trigonometric analog

$\sin(u+v)\sin(u-v)=\sin ^{2}u-\sin ^{2}v.$

Bisection formulas:

$\operatorname {cl} ^{2}{\tfrac {1}{2}}x={\frac {1+\operatorname {cl} x{\sqrt {1+\operatorname {sl} ^{2}x}}}{1+{\sqrt {1+\operatorname {sl} ^{2}x}}}}$

$\operatorname {sl} ^{2}{\tfrac {1}{2}}x={\frac {1-\operatorname {cl} x{\sqrt {1+\operatorname {sl} ^{2}x}}}{1+{\sqrt {1+\operatorname {sl} ^{2}x}}}}$

Duplication formulas:

$\operatorname {cl} 2x={\frac {-1+2\,\operatorname {cl} ^{2}x+\operatorname {cl} ^{4}x}{1+2\,\operatorname {cl} ^{2}x-\operatorname {cl} ^{4}x}}$

$\operatorname {sl} 2x=2\,\operatorname {sl} x\,\operatorname {cl} x{\frac {1+\operatorname {sl} ^{2}x}{1+\operatorname {sl} ^{4}x}}$

Triplication formulas:

$\operatorname {cl} 3x={\frac {-3\,\operatorname {cl} x+6\,\operatorname {cl} ^{5}x+\operatorname {cl} ^{9}x}{1+6\,\operatorname {cl} ^{4}x-3\,\operatorname {cl} ^{8}x}}$

$\operatorname {sl} 3x={\frac {\color {red}{3}\,\color {black}{\operatorname {sl} x-\,}\color {green}{6}\,\color {black}{\operatorname {sl} ^{5}x-\,}\color {blue}{1}\,\color {black}{\operatorname {sl} ^{9}x}}{\color {blue}{1}\,\color {black}{+\,}\,\color {green}{6}\,\color {black}{\operatorname {sl} ^{4}x-\,}\color {red}{3}\,\color {black}{\operatorname {sl} ^{8}x}}}$

Note the "reverse symmetry" of the coefficients of numerator and denominator of $\operatorname {sl} 3x$ . This phenomenon can be observed in multiplication formulas for $\operatorname {sl} \beta x$ where $\beta =m+ni$ whenever $m,n\in \mathbb {Z}$ and $m+n$ is odd.

### Lemnatomic polynomials

Let L be the lattice

$L=\mathbb {Z} (1+i)\varpi +\mathbb {Z} (1-i)\varpi .$

Furthermore, let $K=\mathbb {Q} (i)$ , ${\mathcal {O}}=\mathbb {Z} [i]$ , $z\in \mathbb {C}$ , $\beta =m+in$ , $\gamma =m'+in'$ (where $m,n,m',n'\in \mathbb {Z}$ ), $m+n$ be odd, $m'+n'$ be odd, $\gamma \equiv 1\,\operatorname {mod} \,2(1+i)$ and $\operatorname {sl} \beta z=M_{\beta }(\operatorname {sl} z)$ . Then

$M_{\beta }(x)=i^{\varepsilon }x{\frac {P_{\beta }(x^{4})}{Q_{\beta }(x^{4})}}$

for some coprime polynomials $P_{\beta }(x),Q_{\beta }(x)\in {\mathcal {O}}[x]$ and some $\varepsilon \in \{0,1,2,3\}$ where

$xP_{\beta }(x^{4})=\prod _{\gamma |\beta }\Lambda _{\gamma }(x)$

and

$\Lambda _{\beta }(x)=\prod _{[\alpha ]\in ({\mathcal {O}}/\beta {\mathcal {O}})^{\times }}(x-\operatorname {sl} \alpha \delta _{\beta })$

where $\delta _{\beta }$ is any $\beta$ -torsion generator (i.e. $\delta _{\beta }\in (1/\beta )L$ and $[\delta _{\beta }]\in (1/\beta )L/L$ generates $(1/\beta )L/L$ as an ${\mathcal {O}}$ -module). Examples of $\beta$ -torsion generators include $2\varpi /\beta$ and $(1+i)\varpi /\beta$ . The polynomial $\Lambda _{\beta }(x)\in {\mathcal {O}}[x]$ is called the $\beta$ -th **lemnatomic polynomial**. It is monic and is irreducible over K . The lemnatomic polynomials are the "lemniscate analogs" of the cyclotomic polynomials,

$\Phi _{k}(x)=\prod _{[a]\in (\mathbb {Z} /k\mathbb {Z} )^{\times }}(x-\zeta _{k}^{a}).$

The $\beta$ -th lemnatomic polynomial $\Lambda _{\beta }(x)$ is the minimal polynomial of $\operatorname {sl} \delta _{\beta }$ in $K[x]$ . For convenience, let $\omega _{\beta }=\operatorname {sl} (2\varpi /\beta )$ and ${\tilde {\omega }}_{\beta }=\operatorname {sl} ((1+i)\varpi /\beta )$ . So for example, the minimal polynomial of $\omega _{5}$ (and also of ${\tilde {\omega }}_{5}$ ) in $K[x]$ is

$\Lambda _{5}(x)=x^{16}+52x^{12}-26x^{8}-12x^{4}+1,$

and

$\omega _{5}={\sqrt[{4}]{-13+6{\sqrt {5}}+2{\sqrt {85-38{\sqrt {5}}}}}}$

${\tilde {\omega }}_{5}={\sqrt[{4}]{-13-6{\sqrt {5}}+2{\sqrt {85+38{\sqrt {5}}}}}}$

(an equivalent expression is given in the table below). Another example is

$\Lambda _{-1+2i}(x)=x^{4}-1+2i$

which is the minimal polynomial of $\omega _{-1+2i}$ (and also of ${\tilde {\omega }}_{-1+2i}$ ) in $K[x].$

If p is prime and $\beta$ is positive and odd, then

$\operatorname {deg} \Lambda _{\beta }=\beta ^{2}\prod _{p|\beta }\left(1-{\frac {1}{p}}\right)\left(1-{\frac {(-1)^{(p-1)/2}}{p}}\right)$

which can be compared to the cyclotomic analog

$\operatorname {deg} \Phi _{k}=k\prod _{p|k}\left(1-{\frac {1}{p}}\right).$

### Specific values

Just as for the trigonometric functions, values of the lemniscate functions can be computed for divisions of the lemniscate into ⁠ n ⁠ parts of equal length, using only basic arithmetic and square roots, if and only if ⁠ n ⁠ is of the form $n=2^{k}p_{1}p_{2}\cdots p_{m}$ where ⁠ k ⁠ is a non-negative integer and each ⁠ $p_{i}$ ⁠ (if any) is a distinct Fermat prime.

| n | $\operatorname {cl} n\varpi$ | $\operatorname {sl} n\varpi$ |
|---|---|---|
| 1 | $-1$ | 0 |
| ${\tfrac {5}{6}}$ | $-{\sqrt[{4}]{2{\sqrt {3}}-3}}$ | ${\tfrac {1}{2}}{\bigl (}{\sqrt {3}}+1-{\sqrt[{4}]{12}}{\bigr )}$ |
| ${\tfrac {3}{4}}$ | $-{\sqrt {{\sqrt {2}}-1}}$ | ${\sqrt {{\sqrt {2}}-1}}$ |
| ${\tfrac {2}{3}}$ | $-{\tfrac {1}{2}}{\bigl (}{\sqrt {3}}+1-{\sqrt[{4}]{12}}{\bigr )}$ | ${\sqrt[{4}]{2{\sqrt {3}}-3}}$ |
| ${\tfrac {1}{2}}$ | 0 | 1 |
| ${\tfrac {1}{3}}$ | ${\tfrac {1}{2}}{\bigl (}{\sqrt {3}}+1-{\sqrt[{4}]{12}}{\bigr )}$ | ${\sqrt[{4}]{2{\sqrt {3}}-3}}$ |
| ${\tfrac {1}{4}}$ | ${\sqrt {{\sqrt {2}}-1}}$ | ${\sqrt {{\sqrt {2}}-1}}$ |
| ${\tfrac {1}{6}}$ | ${\sqrt[{4}]{2{\sqrt {3}}-3}}$ | ${\tfrac {1}{2}}{\bigl (}{\sqrt {3}}+1-{\sqrt[{4}]{12}}{\bigr )}$ |


## Relation to geometric shapes

### Arc length of Bernoulli's lemniscate

${\mathcal {L}}$ , the lemniscate of Bernoulli with unit distance from its center to its furthest point (i.e. with unit "half-width"), is essential in the theory of the lemniscate elliptic functions. It can be characterized in at least three ways:

**Angular characterization:** Given two points A and B which are unit distance apart, let $B'$ be the reflection of B about A . Then ${\mathcal {L}}$ is the closure of the locus of the points P such that $|APB-APB'|$ is a right angle.

**Focal characterization:** ${\mathcal {L}}$ is the locus of points in the plane such that the product of their distances from the two focal points $F_{1}={\bigl (}{-{\tfrac {1}{\sqrt {2}}}},0{\bigr )}$ and $F_{2}={\bigl (}{\tfrac {1}{\sqrt {2}}},0{\bigr )}$ is the constant ${\tfrac {1}{2}}$ .

**Explicit coordinate characterization:** ${\mathcal {L}}$ is a quartic curve satisfying the polar equation $r^{2}=\cos 2\theta$ or the Cartesian equation ${\bigl (}x^{2}+y^{2}{\bigr )}{}^{2}=x^{2}-y^{2}.$

The perimeter of ${\mathcal {L}}$ is $2\varpi$ .

The points on ${\mathcal {L}}$ at distance r from the origin are the intersections of the circle $x^{2}+y^{2}=r^{2}$ and the hyperbola $x^{2}-y^{2}=r^{4}$ . The intersection in the positive quadrant has Cartesian coordinates:

${\big (}x(r),y(r){\big )}={\biggl (}\!{\sqrt {{\tfrac {1}{2}}r^{2}{\bigl (}1+r^{2}{\bigr )}}},\,{\sqrt {{\tfrac {1}{2}}r^{2}{\bigl (}1-r^{2}{\bigr )}}}\,{\biggr )}.$

Using this parametrization with $r\in [0,1]$ for a quarter of ${\mathcal {L}}$ , the arc length from the origin to a point ${\big (}x(r),y(r){\big )}$ is:

${\begin{aligned}&\int _{0}^{r}{\sqrt {x'(t)^{2}+y'(t)^{2}}}\mathop {\mathrm {d} t} \\&\quad {}=\int _{0}^{r}{\sqrt {{\frac {(1+2t^{2})^{2}}{2(1+t^{2})}}+{\frac {(1-2t^{2})^{2}}{2(1-t^{2})}}}}\mathop {\mathrm {d} t} \\[6mu]&\quad {}=\int _{0}^{r}{\frac {\mathrm {d} t}{\sqrt {1-t^{4}}}}\\[6mu]&\quad {}=\operatorname {arcsl} r.\end{aligned}}$

Likewise, the arc length from $(1,0)$ to ${\big (}x(r),y(r){\big )}$ is:

${\begin{aligned}&\int _{r}^{1}{\sqrt {x'(t)^{2}+y'(t)^{2}}}\mathop {\mathrm {d} t} \\&\quad {}=\int _{r}^{1}{\frac {\mathrm {d} t}{\sqrt {1-t^{4}}}}\\[6mu]&\quad {}=\operatorname {arccl} r={\tfrac {1}{2}}\varpi -\operatorname {arcsl} r.\end{aligned}}$

Or in the inverse direction, the lemniscate sine and cosine functions give the distance from the origin as functions of arc length from the origin and the point $(1,0)$ , respectively.

Analogously, the circular sine and cosine functions relate the chord length to the arc length for the unit diameter circle with polar equation $r=\cos \theta$ or Cartesian equation $x^{2}+y^{2}=x,$ using the same argument above but with the parametrization:

${\big (}x(r),y(r){\big )}={\biggl (}r^{2},\,{\sqrt {r^{2}{\bigl (}1-r^{2}{\bigr )}}}\,{\biggr )}.$

Alternatively, just as the unit circle $x^{2}+y^{2}=1$ is parametrized in terms of the arc length s from the point $(1,0)$ by

$(x(s),y(s))=(\cos s,\sin s),$

${\mathcal {L}}$ is parametrized in terms of the arc length s from the point $(1,0)$ by

$(x(s),y(s))=\left({\frac {\operatorname {cl} s}{\sqrt {1+\operatorname {sl} ^{2}s}}},{\frac {\operatorname {sl} s\operatorname {cl} s}{\sqrt {1+\operatorname {sl} ^{2}s}}}\right)=\left({\tilde {\operatorname {cl} }}\,s,{\tilde {\operatorname {sl} }}\,s\right).$

The notation ${\tilde {\operatorname {cl} }},\,{\tilde {\operatorname {sl} }}$ is used solely for the purposes of this article; in references, notation for general Jacobi elliptic functions is used instead.

The lemniscate integral and lemniscate functions satisfy an argument duplication identity discovered by Fagnano in 1718:

$\int _{0}^{z}{\frac {\mathrm {d} t}{\sqrt {1-t^{4}}}}=2\int _{0}^{u}{\frac {\mathrm {d} t}{\sqrt {1-t^{4}}}},\quad {\text{if }}z={\frac {2u{\sqrt {1-u^{4}}}}{1+u^{4}}}{\text{ and }}0\leq u\leq {\sqrt {{\sqrt {2}}-1}}.$

Later mathematicians generalized this result. Analogously to the constructible polygons in the circle, the lemniscate can be divided into ⁠ n ⁠ sections of equal arc length using only straightedge and compass if and only if ⁠ n ⁠ is of the form $n=2^{k}p_{1}p_{2}\cdots p_{m}$ where ⁠ k ⁠ is a non-negative integer and each ⁠ $p_{i}$ ⁠ (if any) is a distinct Fermat prime. The "if" part of the theorem was proved by Niels Abel in 1827–1828, and the "only if" part was proved by Michael Rosen in 1981. Equivalently, the lemniscate can be divided into ⁠ n ⁠ sections of equal arc length using only straightedge and compass if and only if $\varphi (n)$ is a power of two (where $\varphi$ is Euler's totient function). The lemniscate is *not* assumed to be already drawn, as that would go against the rules of straightedge and compass constructions; instead, it is assumed that we are given only two points by which the lemniscate is defined, such as its center and radial point (one of the two points on the lemniscate such that their distance from the center is maximal) or its two foci.

Let $r_{j}=\operatorname {sl} {\dfrac {2j\varpi }{n}}$ . Then the ⁠ n ⁠-division points for ${\mathcal {L}}$ are the points

$\left(r_{j}{\sqrt {{\tfrac {1}{2}}{\bigl (}1+r_{j}^{2}{\bigr )}}},\ (-1)^{\left\lfloor 4j/n\right\rfloor }{\sqrt {{\tfrac {1}{2}}r_{j}^{2}{\bigl (}1-r_{j}^{2}{\bigr )}}}\right),\quad j\in \{1,2,\ldots ,n\}$

where $\lfloor \cdot \rfloor$ is the floor function. See below for some specific values of $\operatorname {sl} {\dfrac {2\varpi }{n}}$ .

### Arc length of rectangular elastica

The inverse lemniscate sine also describes the arc length ⁠ s ⁠ relative to the ⁠ x ⁠ coordinate of the rectangular elastica. This curve has ⁠ y ⁠ coordinate and arc length:

$y=\int _{x}^{1}{\frac {t^{2}\mathop {\mathrm {d} t} }{\sqrt {1-t^{4}}}},\quad s=\operatorname {arcsl} x=\int _{0}^{x}{\frac {\mathrm {d} t}{\sqrt {1-t^{4}}}}$

The rectangular elastica solves a problem posed by Jacob Bernoulli, in 1691, to describe the shape of an idealized flexible rod fixed in a vertical orientation at the bottom end, and pulled down by a weight from the far end until it has been bent horizontal. Bernoulli's proposed solution established Euler–Bernoulli beam theory, further developed by Euler in the 18th century.

### Elliptic characterization

Let C be a point on the ellipse $x^{2}+2y^{2}=1$ in the first quadrant and let D be the projection of C on the unit circle $x^{2}+y^{2}=1$ . The distance r between the origin A and the point C is a function of $\varphi$ (the angle $BAC$ where $B=(1,0)$ ; equivalently the length of the circular arc $BD$ ). The parameter u is given by

$u=\int _{0}^{\varphi }r(\theta )\,\mathrm {d} \theta =\int _{0}^{\varphi }{\frac {\mathrm {d} \theta }{\sqrt {1+\sin ^{2}\theta }}}.$

If E is the projection of D on the x-axis and if F is the projection of C on the x-axis, then the lemniscate elliptic functions are given by

$\operatorname {cl} u={\overline {AF}},\quad \operatorname {sl} u={\overline {DE}},$

${\tilde {\operatorname {cl} }}\,u={\overline {AF}}{\overline {AC}},\quad {\tilde {\operatorname {sl} }}\,u={\overline {AF}}{\overline {FC}}.$


## Series Identities

### Power series

The power series expansion of the lemniscate sine at the origin is

$\operatorname {sl} z=\sum _{n=0}^{\infty }a_{n}z^{n}=z-12{\frac {z^{5}}{5!}}+3024{\frac {z^{9}}{9!}}-4390848{\frac {z^{13}}{13!}}+\cdots ,\quad |z|<{\tfrac {\varpi }{\sqrt {2}}}$

where the coefficients $a_{n}$ are determined as follows:

$n\not \equiv 1{\pmod {4}}\implies a_{n}=0,$

$a_{1}=1,\,\forall n\in \mathbb {N} _{0}:\,a_{n+2}=-{\frac {2}{(n+1)(n+2)}}\sum _{i+j+k=n}a_{i}a_{j}a_{k}$

where $i+j+k=n$ stands for all three-term compositions of n . For example, to evaluate $a_{13}$ , it can be seen that there are only six compositions of $13-2=11$ that give a nonzero contribution to the sum: $11=9+1+1=1+9+1=1+1+9$ and $11=5+5+1=5+1+5=1+5+5$ , so

$a_{13}=-{\tfrac {2}{12\cdot 13}}(a_{9}a_{1}a_{1}+a_{1}a_{9}a_{1}+a_{1}a_{1}a_{9}+a_{5}a_{5}a_{1}+a_{5}a_{1}a_{5}+a_{1}a_{5}a_{5})=-{\tfrac {11}{15600}}.$

The expansion can be equivalently written as

$\operatorname {sl} z=\sum _{n=0}^{\infty }p_{2n}{\frac {z^{4n+1}}{(4n+1)!}},\quad \left|z\right|<{\frac {\varpi }{\sqrt {2}}}$

where

$p_{n+2}=-12\sum _{j=0}^{n}{\binom {2n+2}{2j+2}}p_{n-j}\sum _{k=0}^{j}{\binom {2j+1}{2k+1}}p_{k}p_{j-k},\quad p_{0}=1,\,p_{1}=0.$

The power series expansion of ${\tilde {\operatorname {sl} }}$ at the origin is

${\tilde {\operatorname {sl} }}\,z=\sum _{n=0}^{\infty }\alpha _{n}z^{n}=z-9{\frac {z^{3}}{3!}}+153{\frac {z^{5}}{5!}}-4977{\frac {z^{7}}{7!}}+\cdots ,\quad \left|z\right|<{\frac {\varpi }{2}}$

where $\alpha _{n}=0$ if n is even and

$\alpha _{n}={\sqrt {2}}{\frac {\pi }{\varpi }}{\frac {(-1)^{(n-1)/2}}{n!}}\sum _{k=1}^{\infty }{\frac {(2k\pi /\varpi )^{n+1}}{\cosh k\pi }},\quad \left|\alpha _{n}\right|\sim 2^{n+5/2}{\frac {n+1}{\varpi ^{n+2}}}$

if n is odd.

The expansion can be equivalently written as

${\tilde {\operatorname {sl} }}\,z=\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{2^{n+1}}}\left(\sum _{l=0}^{n}2^{l}{\binom {2n+2}{2l+1}}s_{l}t_{n-l}\right){\frac {z^{2n+1}}{(2n+1)!}},\quad \left|z\right|<{\frac {\varpi }{2}}$

where

$s_{n+2}=3s_{n+1}+24\sum _{j=0}^{n}{\binom {2n+2}{2j+2}}s_{n-j}\sum _{k=0}^{j}{\binom {2j+1}{2k+1}}s_{k}s_{j-k},\quad s_{0}=1,\,s_{1}=3,$

$t_{n+2}=3t_{n+1}+3\sum _{j=0}^{n}{\binom {2n+2}{2j+2}}t_{n-j}\sum _{k=0}^{j}{\binom {2j+1}{2k+1}}t_{k}t_{j-k},\quad t_{0}=1,\,t_{1}=3.$

For the lemniscate cosine,

$\operatorname {cl} {z}=1-\sum _{n=0}^{\infty }(-1)^{n}\left(\sum _{l=0}^{n}2^{l}{\binom {2n+2}{2l+1}}q_{l}r_{n-l}\right){\frac {z^{2n+2}}{(2n+2)!}}=1-2{\frac {z^{2}}{2!}}+12{\frac {z^{4}}{4!}}-216{\frac {z^{6}}{6!}}+\cdots ,\quad \left|z\right|<{\frac {\varpi }{2}},$

${\tilde {\operatorname {cl} }}\,z=\sum _{n=0}^{\infty }(-1)^{n}2^{n}q_{n}{\frac {z^{2n}}{(2n)!}}=1-3{\frac {z^{2}}{2!}}+33{\frac {z^{4}}{4!}}-819{\frac {z^{6}}{6!}}+\cdots ,\quad \left|z\right|<{\frac {\varpi }{2}}$

where

$r_{n+2}=3\sum _{j=0}^{n}{\binom {2n+2}{2j+2}}r_{n-j}\sum _{k=0}^{j}{\binom {2j+1}{2k+1}}r_{k}r_{j-k},\quad r_{0}=1,\,r_{1}=0,$

$q_{n+2}={\tfrac {3}{2}}q_{n+1}+6\sum _{j=0}^{n}{\binom {2n+2}{2j+2}}q_{n-j}\sum _{k=0}^{j}{\binom {2j+1}{2k+1}}q_{k}q_{j-k},\quad q_{0}=1,\,q_{1}={\tfrac {3}{2}}.$

### Ramanujan's cos/cosh identity

Ramanujan's famous cos/cosh identity states that if

$R(s)={\frac {\pi }{\varpi {\sqrt {2}}}}\sum _{n\in \mathbb {Z} }{\frac {\cos(2n\pi s/\varpi )}{\cosh n\pi }},$

then

$R(s)^{-2}+R(is)^{-2}=2,\quad \left|\operatorname {Re} s\right|<{\frac {\varpi }{2}},\left|\operatorname {Im} s\right|<{\frac {\varpi }{2}}.$

There is a close relation between the lemniscate functions and $R(s)$ . Indeed,

${\tilde {\operatorname {sl} }}\,s=-{\frac {\mathrm {d} }{\mathrm {d} s}}R(s)\quad \left|\operatorname {Im} s\right|<{\frac {\varpi }{2}}$

${\tilde {\operatorname {cl} }}\,s={\frac {\mathrm {d} }{\mathrm {d} s}}{\sqrt {1-R(s)^{2}}},\quad \left|\operatorname {Re} s-{\frac {\varpi }{2}}\right|<{\frac {\varpi }{2}},\,\left|\operatorname {Im} s\right|<{\frac {\varpi }{2}}$

and

$R(s)={\frac {1}{\sqrt {1+\operatorname {sl} ^{2}s}}},\quad \left|\operatorname {Im} s\right|<{\frac {\varpi }{2}}.$

### Continued fractions

For $z\in \mathbb {C} \setminus \{0\}$ :

$\int _{0}^{\infty }e^{-tz{\sqrt {2}}}\operatorname {cl} t\,\mathrm {d} t={\cfrac {1/{\sqrt {2}}}{z+{\cfrac {a_{1}}{z+{\cfrac {a_{2}}{z+{\cfrac {a_{3}}{z+\ddots }}}}}}}},\quad a_{n}={\frac {n^{2}}{4}}((-1)^{n+1}+3)$

$\int _{0}^{\infty }e^{-tz{\sqrt {2}}}\operatorname {sl} t\operatorname {cl} t\,\mathrm {d} t={\cfrac {1/2}{z^{2}+b_{1}-{\cfrac {a_{1}}{z^{2}+b_{2}-{\cfrac {a_{2}}{z^{2}+b_{3}-\ddots }}}}}},\quad a_{n}=n^{2}(4n^{2}-1),\,b_{n}=3(2n-1)^{2}$

### Methods of computation

> A fast algorithm, returning approximations to $\operatorname {sl} x$ (which get closer to $\operatorname {sl} x$ with increasing N ), is the following:
> 
> - $a_{0}\leftarrow 1;$ $b_{0}\leftarrow {\tfrac {1}{\sqrt {2}}};$ $c_{0}\leftarrow {\sqrt {\tfrac {1}{2}}}$
> - **for each** $n\geq 1$ **do** $a_{n}\leftarrow {\tfrac {1}{2}}(a_{n-1}+b_{n-1});$ $b_{n}\leftarrow {\sqrt {a_{n-1}b_{n-1}}};$ $c_{n}\leftarrow {\tfrac {1}{2}}(a_{n-1}-b_{n-1})$ **if** $c_{n}<{\textrm {tolerance}}$ **then** $N\leftarrow n;$ **break**
> - $\phi _{N}\leftarrow 2^{N}a_{N}{\sqrt {2}}x$
> - **for each** ⁠ n ⁠ from ⁠ N ⁠ to ⁠ 0 ⁠ **do** $\phi _{n-1}\leftarrow {\tfrac {1}{2}}\left(\phi _{n}+{\arcsin }{\left({\frac {c_{n}}{a_{n}}}\sin \phi _{n}\right)}\right)$
> - **return** ${\frac {\sin \phi _{0}}{\sqrt {2-\sin ^{2}\phi _{0}}}}$
> 
> This is effectively using the arithmetic-geometric mean and is based on Landen's transformations.

Several methods of computing $\operatorname {sl} x$ involve first making the change of variables $\pi x=\varpi {\tilde {x}}$ and then computing $\operatorname {sl} (\varpi {\tilde {x}}/\pi ).$

A hyperbolic series method:

$\operatorname {sl} \left({\frac {\varpi }{\pi }}x\right)={\frac {\pi }{\varpi }}\sum _{n\in \mathbb {Z} }{\frac {(-1)^{n}}{\cosh(x-(n+1/2)\pi )}},\quad x\in \mathbb {C}$

${\frac {1}{\operatorname {sl} (\varpi x/\pi )}}={\frac {\pi }{\varpi }}\sum _{n\in \mathbb {Z} }{\frac {(-1)^{n}}{{\sinh }{\left(x-n\pi \right)}}}={\frac {\pi }{\varpi }}\sum _{n\in \mathbb {Z} }{\frac {(-1)^{n}}{\sin(x-n\pi i)}},\quad x\in \mathbb {C}$

Fourier series method:

$\operatorname {sl} {\Bigl (}{\frac {\varpi }{\pi }}x{\Bigr )}={\frac {2\pi }{\varpi }}\sum _{n=0}^{\infty }{\frac {(-1)^{n}\sin((2n+1)x)}{\cosh((n+1/2)\pi )}},\quad \left|\operatorname {Im} x\right|<{\frac {\pi }{2}}$

$\operatorname {cl} \left({\frac {\varpi }{\pi }}x\right)={\frac {2\pi }{\varpi }}\sum _{n=0}^{\infty }{\frac {\cos((2n+1)x)}{\cosh((n+1/2)\pi )}},\quad \left|\operatorname {Im} x\right|<{\frac {\pi }{2}}$

${\frac {1}{\operatorname {sl} (\varpi x/\pi )}}={\frac {\pi }{\varpi }}\left({\frac {1}{\sin x}}-4\sum _{n=0}^{\infty }{\frac {\sin((2n+1)x)}{e^{(2n+1)\pi }+1}}\right),\quad \left|\operatorname {Im} x\right|<\pi$

The lemniscate functions can be computed more rapidly by

${\begin{aligned}\operatorname {sl} {\Bigl (}{\frac {\varpi }{\pi }}x{\Bigr )}&={\frac {{\theta _{1}}{\left(x,e^{-\pi }\right)}}{{\theta _{3}}{\left(x,e^{-\pi }\right)}}},\quad x\in \mathbb {C} \\\operatorname {cl} {\Bigl (}{\frac {\varpi }{\pi }}x{\Bigr )}&={\frac {{\theta _{2}}{\left(x,e^{-\pi }\right)}}{{\theta _{4}}{\left(x,e^{-\pi }\right)}}},\quad x\in \mathbb {C} \end{aligned}}$

where

${\begin{aligned}\theta _{1}(x,e^{-\pi })&=\sum _{n\in \mathbb {Z} }(-1)^{n+1}e^{-\pi (n+1/2+x/\pi )^{2}}=\sum _{n\in \mathbb {Z} }(-1)^{n}e^{-\pi (n+1/2)^{2}}\sin((2n+1)x),\\\theta _{2}(x,e^{-\pi })&=\sum _{n\in \mathbb {Z} }(-1)^{n}e^{-\pi (n+x/\pi )^{2}}=\sum _{n\in \mathbb {Z} }e^{-\pi (n+1/2)^{2}}\cos((2n+1)x),\\\theta _{3}(x,e^{-\pi })&=\sum _{n\in \mathbb {Z} }e^{-\pi (n+x/\pi )^{2}}=\sum _{n\in \mathbb {Z} }e^{-\pi n^{2}}\cos 2nx,\\\theta _{4}(x,e^{-\pi })&=\sum _{n\in \mathbb {Z} }e^{-\pi (n+1/2+x/\pi )^{2}}=\sum _{n\in \mathbb {Z} }(-1)^{n}e^{-\pi n^{2}}\cos 2nx\end{aligned}}$

are the Jacobi theta functions.

Fourier series for the logarithm of the lemniscate sine:

$\ln \operatorname {sl} \left({\frac {\varpi }{\pi }}x\right)=\ln 2-{\frac {\pi }{4}}+\ln \sin x+2\sum _{n=1}^{\infty }{\frac {(-1)^{n}\cos 2nx}{n(e^{n\pi }+(-1)^{n})}},\quad \left|\operatorname {Im} x\right|<{\frac {\pi }{2}}$

The following series identities were discovered by Ramanujan:

${\frac {\varpi ^{2}}{\pi ^{2}\operatorname {sl} ^{2}(\varpi x/\pi )}}={\frac {1}{\sin ^{2}x}}-{\frac {1}{\pi }}-8\sum _{n=1}^{\infty }{\frac {n\cos 2nx}{e^{2n\pi }-1}},\quad \left|\operatorname {Im} x\right|<\pi$

$\arctan \operatorname {sl} {\Bigl (}{\frac {\varpi }{\pi }}x{\Bigr )}=2\sum _{n=0}^{\infty }{\frac {\sin((2n+1)x)}{(2n+1)\cosh((n+1/2)\pi )}},\quad \left|\operatorname {Im} x\right|<{\frac {\pi }{2}}$

The functions ${\tilde {\operatorname {sl} }}$ and ${\tilde {\operatorname {cl} }}$ analogous to $\sin$ and $\cos$ on the unit circle have the following Fourier and hyperbolic series expansions:

${\tilde {\operatorname {sl} }}\,s=2{\sqrt {2}}{\frac {\pi ^{2}}{\varpi ^{2}}}\sum _{n=1}^{\infty }{\frac {n\sin(2n\pi s/\varpi )}{\cosh n\pi }},\quad \left|\operatorname {Im} s\right|<{\frac {\varpi }{2}}$

${\tilde {\operatorname {cl} }}\,s={\sqrt {2}}{\frac {\pi ^{2}}{\varpi ^{2}}}\sum _{n=0}^{\infty }{\frac {(2n+1)\cos((2n+1)\pi s/\varpi )}{\sinh((n+1/2)\pi )}},\quad \left|\operatorname {Im} s\right|<{\frac {\varpi }{2}}$

${\tilde {\operatorname {sl} }}\,s={\frac {\pi ^{2}}{\varpi ^{2}{\sqrt {2}}}}\sum _{n\in \mathbb {Z} }{\frac {\sinh(\pi (n+s/\varpi ))}{\cosh ^{2}(\pi (n+s/\varpi ))}},\quad s\in \mathbb {C}$

${\tilde {\operatorname {cl} }}\,s={\frac {\pi ^{2}}{\varpi ^{2}{\sqrt {2}}}}\sum _{n\in \mathbb {Z} }{\frac {(-1)^{n}}{\cosh ^{2}(\pi (n+s/\varpi ))}},\quad s\in \mathbb {C}$

The following identities come from product representations of the theta functions:

$\mathrm {sl} {\Bigl (}{\frac {\varpi }{\pi }}x{\Bigr )}=2e^{-\pi /4}\sin x\prod _{n=1}^{\infty }{\frac {1-2e^{-2n\pi }\cos 2x+e^{-4n\pi }}{1+2e^{-(2n-1)\pi }\cos 2x+e^{-(4n-2)\pi }}},\quad x\in \mathbb {C}$

$\mathrm {cl} {\Bigl (}{\frac {\varpi }{\pi }}x{\Bigr )}=2e^{-\pi /4}\cos x\prod _{n=1}^{\infty }{\frac {1+2e^{-2n\pi }\cos 2x+e^{-4n\pi }}{1-2e^{-(2n-1)\pi }\cos 2x+e^{-(4n-2)\pi }}},\quad x\in \mathbb {C}$

A similar formula involving the $\operatorname {sn}$ function can be given.

### The lemniscate functions as a ratio of entire functions

Since the lemniscate sine is a meromorphic function in the whole complex plane, it can be written as a ratio of entire functions. Gauss showed that sl has the following product expansion, reflecting the distribution of its zeros and poles:

$\operatorname {sl} z={\frac {M(z)}{N(z)}}$

where

$M(z)=z\prod _{\alpha }\left(1-{\frac {z^{4}}{\alpha ^{4}}}\right),\quad N(z)=\prod _{\beta }\left(1-{\frac {z^{4}}{\beta ^{4}}}\right).$

Here, $\alpha$ and $\beta$ denote, respectively, the zeros and poles of sl which are in the quadrant $\operatorname {Re} z>0,\operatorname {Im} z\geq 0$ . A proof can be found in. Importantly, the infinite products converge to the same value for all possible orders in which their terms can be multiplied, as a consequence of uniform convergence.

| Proof of the infinite product for the lemniscate sine |
|---|
| **Proof by logarithmic differentiation** It can be easily seen (using uniform and absolute convergence arguments to justify interchanging of limiting operations) that ${\frac {M'(z)}{M(z)}}=-\sum _{n=0}^{\infty }2^{4n}\mathrm {H} _{4n}{\frac {z^{4n-1}}{(4n)!}},\quad \left\|z\right\|<\varpi$ (where $\mathrm {H} _{n}$ are the Hurwitz numbers defined in Lemniscate elliptic functions § Hurwitz numbers) and ${\frac {N'(z)}{N(z)}}=(1+i){\frac {M'((1+i)z)}{M((1+i)z)}}-{\frac {M'(z)}{M(z)}}.$ Therefore ${\frac {N'(z)}{N(z)}}=\sum _{n=0}^{\infty }2^{4n}(1-(-1)^{n}2^{2n})\mathrm {H} _{4n}{\frac {z^{4n-1}}{(4n)!}},\quad \left\|z\right\|<{\frac {\varpi }{\sqrt {2}}}.$ It is known that ${\frac {1}{\operatorname {sl} ^{2}z}}=\sum _{n=0}^{\infty }2^{4n}(4n-1)\mathrm {H} _{4n}{\frac {z^{4n-2}}{(4n)!}},\quad \left\|z\right\|<\varpi .$ Then from ${\frac {\mathrm {d} }{\mathrm {d} z}}{\frac {\operatorname {sl} 'z}{\operatorname {sl} z}}=-{\frac {1}{\operatorname {sl} ^{2}z}}-\operatorname {sl} ^{2}z$ and $\operatorname {sl} ^{2}z={\frac {1}{\operatorname {sl} ^{2}z}}-{\frac {(1+i)^{2}}{\operatorname {sl} ^{2}((1+i)z)}}$ we get ${\frac {\operatorname {sl} 'z}{\operatorname {sl} z}}=-\sum _{n=0}^{\infty }2^{4n}(2-(-1)^{n}2^{2n})\mathrm {H} _{4n}{\frac {z^{4n-1}}{(4n)!}},\quad \left\|z\right\|<{\frac {\varpi }{\sqrt {2}}}.$ Hence ${\frac {\operatorname {sl} 'z}{\operatorname {sl} z}}={\frac {M'(z)}{M(z)}}-{\frac {N'(z)}{N(z)}},\quad \left\|z\right\|<{\frac {\varpi }{\sqrt {2}}}.$ Therefore $\operatorname {sl} z=C{\frac {M(z)}{N(z)}}$ for some constant C for $\left\|z\right\|<\varpi /{\sqrt {2}}$ but this result holds for all $z\in \mathbb {C}$ by analytic continuation. Using $\lim _{z\to 0}{\frac {\operatorname {sl} z}{z}}=1$ gives $C=1$ which completes the proof. $\blacksquare$ **Proof by Liouville's theorem** Let $f(z)={\frac {M(z)}{N(z)}}={\frac {(1+i)M(z)^{2}}{M((1+i)z)}},$ with patches at removable singularities. The shifting formulas $M(z+2\varpi )=e^{2{\frac {\pi }{\varpi }}(z+\varpi )}M(z),\quad M(z+2\varpi i)=e^{-2{\frac {\pi }{\varpi }}(iz-\varpi )}M(z)$ imply that f is an elliptic function with periods $2\varpi$ and $2\varpi i$ , just as $\operatorname {sl}$ . It follows that the function g defined by $g(z)={\frac {\operatorname {sl} z}{f(z)}},$ when patched, is an elliptic function without poles. By Liouville's theorem, it is a constant. By using $\operatorname {sl} z=z+\operatorname {O} (z^{5})$ , $M(z)=z+\operatorname {O} (z^{5})$ and $N(z)=1+\operatorname {O} (z^{4})$ , this constant is 1 , which proves the theorem. $\blacksquare$ |

Gauss conjectured that $\ln N(\varpi )=\pi /2$ (this later turned out to be true) and commented that this “is most remarkable and a proof of this property promises the most serious increase in analysis”. Gauss expanded the products for M and N as infinite series (see below). He also discovered several identities involving the functions M and N , such as

$N(z)={\frac {M((1+i)z)}{(1+i)M(z)}},\quad z\notin \varpi \mathbb {Z} [i]$

and

$N(2z)=M(z)^{4}+N(z)^{4}.$

Thanks to a certain theorem on splitting limits, we are allowed to multiply out the infinite products and collect like powers of z . Doing so gives the following power series expansions that are convergent everywhere in the complex plane:

$M(z)=z-2{\frac {z^{5}}{5!}}-36{\frac {z^{9}}{9!}}+552{\frac {z^{13}}{13!}}+\cdots ,\quad z\in \mathbb {C}$

$N(z)=1+2{\frac {z^{4}}{4!}}-4{\frac {z^{8}}{8!}}+408{\frac {z^{12}}{12!}}+\cdots ,\quad z\in \mathbb {C} .$

This can be contrasted with the power series of $\operatorname {sl}$ which has only finite radius of convergence (because it is not entire).

We define S and T by

$S(z)=N\left({\frac {z}{1+i}}\right)^{2}-iM\left({\frac {z}{1+i}}\right)^{2},\quad T(z)=S(iz).$

Then the lemniscate cosine can be written as

$\operatorname {cl} z={\frac {S(z)}{T(z)}}$

where

$S(z)=1-{\frac {z^{2}}{2!}}-{\frac {z^{4}}{4!}}-3{\frac {z^{6}}{6!}}+17{\frac {z^{8}}{8!}}-9{\frac {z^{10}}{10!}}+111{\frac {z^{12}}{12!}}+\cdots ,\quad z\in \mathbb {C}$

$T(z)=1+{\frac {z^{2}}{2!}}-{\frac {z^{4}}{4!}}+3{\frac {z^{6}}{6!}}+17{\frac {z^{8}}{8!}}+9{\frac {z^{10}}{10!}}+111{\frac {z^{12}}{12!}}+\cdots ,\quad z\in \mathbb {C} .$

Furthermore, the identities

$M(2z)=2M(z)N(z)S(z)T(z),$

$S(2z)=S(z)^{4}-2M(z)^{4},$

$T(2z)=T(z)^{4}-2M(z)^{4}$

and the Pythagorean-like identities

$M(z)^{2}+S(z)^{2}=N(z)^{2},$

$M(z)^{2}+N(z)^{2}=T(z)^{2}$

hold for all $z\in \mathbb {C}$ .

The quasi-addition formulas

$M(z+w)M(z-w)=M(z)^{2}N(w)^{2}-N(z)^{2}M(w)^{2},$

$N(z+w)N(z-w)=N(z)^{2}N(w)^{2}+M(z)^{2}M(w)^{2}$

(where $z,w\in \mathbb {C}$ ) imply further multiplication formulas for M and N by recursion.

Gauss' M and N satisfy the following system of differential equations:

$M(z)M''(z)=M'(z)^{2}-N(z)^{2},$

$N(z)N''(z)=N'(z)^{2}+M(z)^{2}$

where $z\in \mathbb {C}$ . Both M and N satisfy the differential equation

$X(z)X''''(z)=4X'(z)X'''(z)-3X''(z)^{2}+2X(z)^{2},\quad z\in \mathbb {C} .$

The functions can be also expressed by integrals involving elliptic functions:

$M(z)=z\exp \left(-\int _{0}^{z}\int _{0}^{w}\left({\frac {1}{\operatorname {sl} ^{2}v}}-{\frac {1}{v^{2}}}\right)\,\mathrm {d} v\,\mathrm {d} w\right),$

$N(z)=\exp \left(\int _{0}^{z}\int _{0}^{w}\operatorname {sl} ^{2}v\,\mathrm {d} v\,\mathrm {d} w\right)$

where the contours do not cross the poles; while the innermost integrals are path-independent, the outermost ones are path-dependent; however, the path dependence cancels out with the non-injectivity of the complex exponential function.

An alternative way of expressing the lemniscate functions as a ratio of entire functions involves the theta functions (see Lemniscate elliptic functions § Methods of computation); the relation between $M,N$ and $\theta _{1},\theta _{3}$ is

$M(z)=2^{-1/4}e^{\pi z^{2}/(2\varpi ^{2})}{\sqrt {\frac {\pi }{\varpi }}}\theta _{1}\left({\frac {\pi z}{\varpi }},e^{-\pi }\right),$

$N(z)=2^{-1/4}e^{\pi z^{2}/(2\varpi ^{2})}{\sqrt {\frac {\pi }{\varpi }}}\theta _{3}\left({\frac {\pi z}{\varpi }},e^{-\pi }\right)$

where $z\in \mathbb {C}$ .
