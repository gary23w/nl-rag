---
title: "Lemniscate elliptic functions (part 2/2)"
source: https://en.wikipedia.org/wiki/Lemniscate_elliptic_functions
domain: elliptic-functions
license: CC-BY-SA-4.0
tags: elliptic function, jacobi elliptic functions, weierstrass elliptic function, theta function
fetched: 2026-07-02
part: 2/2
---

## Relation to other functions

### Relation to Weierstrass and Jacobi elliptic functions

The lemniscate functions are closely related to the Weierstrass elliptic function $\wp (z;1,0)$ (the "lemniscatic case"), with invariants ⁠ $g_{2}=1$ ⁠ and ⁠ $g_{3}=0$ ⁠. This lattice has fundamental periods $\omega _{1}={\sqrt {2}}\varpi ,$ and $\omega _{2}=i\omega _{1}$ . The associated constants of the Weierstrass function are $e_{1}={\tfrac {1}{2}},\ e_{2}=0,\ e_{3}=-{\tfrac {1}{2}}.$

The related case of a Weierstrass elliptic function with ⁠ $g_{2}=a$ ⁠, ⁠ $g_{3}=0$ ⁠ may be handled by a scaling transformation. However, this may involve complex numbers. If it is desired to remain within real numbers, there are two cases to consider: ⁠ $a>0$ ⁠ and ⁠ $a<0$ ⁠. The period parallelogram is either a square or a rhombus. The Weierstrass elliptic function $\wp (z;-1,0)$ is called the "pseudolemniscatic case".

The square of the lemniscate sine can be represented as

$\operatorname {sl} ^{2}z={\frac {1}{\wp (z;4,0)}}={\frac {i}{2\wp ((1-i)z;-1,0)}}={-2\wp }{\left({\sqrt {2}}z+(i-1){\frac {\varpi }{\sqrt {2}}};1,0\right)}$

where the second and third argument of $\wp$ denote the lattice invariants ⁠ $g_{2}$ ⁠ and ⁠ $g_{3}$ ⁠. The lemniscate sine is a rational function in the Weierstrass elliptic function and its derivative:

$\operatorname {sl} z=-2{\frac {\wp (z;-1,0)}{\wp '(z;-1,0)}}.$

The lemniscate functions can also be written in terms of Jacobi elliptic functions. The Jacobi elliptic functions $\operatorname {sn}$ and $\operatorname {cd}$ with positive real elliptic modulus have an "upright" rectangular lattice aligned with real and imaginary axes. Alternately, the functions $\operatorname {sn}$ and $\operatorname {cd}$ with modulus ⁠ i ⁠ (and $\operatorname {sd}$ and $\operatorname {cn}$ with modulus $1/{\sqrt {2}}$ ) have a square period lattice rotated 1/8 turn.

$\operatorname {sl} z=\operatorname {sn} (z;i)=\operatorname {sc} (z;{\sqrt {2}})={{\tfrac {1}{\sqrt {2}}}\operatorname {sd} }\left({\sqrt {2}}z;{\tfrac {1}{\sqrt {2}}}\right)$

$\operatorname {cl} z=\operatorname {cd} (z;i)=\operatorname {dn} (z;{\sqrt {2}})={\operatorname {cn} }\left({\sqrt {2}}z;{\tfrac {1}{\sqrt {2}}}\right)$

where the second arguments denote the elliptic modulus k .

The functions ${\tilde {\operatorname {sl} }}$ and ${\tilde {\operatorname {cl} }}$ can also be expressed in terms of Jacobi elliptic functions:

${\tilde {\operatorname {sl} }}\,z=\operatorname {cd} (z;i)\operatorname {sd} (z;i)=\operatorname {dn} (z;{\sqrt {2}})\operatorname {sn} (z;{\sqrt {2}})={\tfrac {1}{\sqrt {2}}}\operatorname {cn} \left({\sqrt {2}}z;{\tfrac {1}{\sqrt {2}}}\right)\operatorname {sn} \left({\sqrt {2}}z;{\tfrac {1}{\sqrt {2}}}\right),$

${\tilde {\operatorname {cl} }}\,z=\operatorname {cd} (z;i)\operatorname {nd} (z;i)=\operatorname {dn} (z;{\sqrt {2}})\operatorname {cn} (z;{\sqrt {2}})=\operatorname {cn} \left({\sqrt {2}}z;{\tfrac {1}{\sqrt {2}}}\right)\operatorname {dn} \left({\sqrt {2}}z;{\tfrac {1}{\sqrt {2}}}\right).$

### Relation to the modular lambda function

The lemniscate sine can be used for the computation of values of the modular lambda function:

$\prod _{k=1}^{n}\;{\operatorname {sl} }{\left({\frac {2k-1}{2n+1}}{\frac {\varpi }{2}}\right)}={\sqrt[{8}]{\frac {\lambda ((2n+1)i)}{1-\lambda ((2n+1)i)}}}$

For example:

${\begin{aligned}&{\operatorname {sl} }{\bigl (}{\tfrac {1}{14}}\varpi {\bigr )}\,{\operatorname {sl} }{\bigl (}{\tfrac {3}{14}}\varpi {\bigr )}\,{\operatorname {sl} }{\bigl (}{\tfrac {5}{14}}\varpi {\bigr )}\\[7mu]&\quad {}={\sqrt[{8}]{\frac {\lambda (7i)}{1-\lambda (7i)}}}={\tan }{\Bigl (}{{\tfrac {1}{2}}\operatorname {arccsc} }{\Bigl (}{\tfrac {1}{2}}{\sqrt {8{\sqrt {7}}+21}}+{\tfrac {1}{2}}{\sqrt {7}}+1{\Bigr )}{\Bigr )}\\[7mu]&\quad {}={\frac {2}{2+{\sqrt {7}}+{\sqrt {21+8{\sqrt {7}}}}+{\sqrt {2{14+6{\sqrt {7}}+{\sqrt {455+172{\sqrt {7}}}}}}}}}\\[18mu]&{\operatorname {sl} }{\bigl (}{\tfrac {1}{18}}\varpi {\bigr )}\,{\operatorname {sl} }{\bigl (}{\tfrac {3}{18}}\varpi {\bigr )}\,{\operatorname {sl} }{\bigl (}{\tfrac {5}{18}}\varpi {\bigr )}\,{\operatorname {sl} }{\bigl (}{\tfrac {7}{18}}\varpi {\bigr )}\\&\quad {}={\sqrt[{8}]{\frac {\lambda (9i)}{1-\lambda (9i)}}}=\tan \left({\vphantom {\frac {\Big |}{\Big |}}}\right.{\frac {\pi }{4}}-\arctan \left({\vphantom {\frac {\Big |}{\Big |}}}\right.{\frac {2{\sqrt[{3}]{2{\sqrt {3}}-2}}-2{\sqrt[{3}]{2-{\sqrt {3}}}}+{\sqrt {3}}-1}{\sqrt[{4}]{12}}}\left.\left.{\vphantom {\frac {\Big |}{\Big |}}}\right)\right)\end{aligned}}$


## Inverse functions

The inverse function of the lemniscate sine is the lemniscate arcsine, defined as

$\operatorname {arcsl} x=\int _{0}^{x}{\frac {\mathrm {d} t}{\sqrt {1-t^{4}}}}.$

It can also be represented by the hypergeometric function:

$\operatorname {arcsl} x=x\,{}_{2}F_{1}{\bigl (}{\tfrac {1}{2}},{\tfrac {1}{4}};{\tfrac {5}{4}};x^{4}{\bigr )}$

which can be easily seen by using the binomial series.

The inverse function of the lemniscate cosine is the lemniscate arccosine. This function is defined by following expression:

$\operatorname {arccl} x=\int _{x}^{1}{\frac {\mathrm {d} t}{\sqrt {1-t^{4}}}}={\tfrac {1}{2}}\varpi -\operatorname {arcsl} x$

For ⁠ x ⁠ in the interval $-1\leq x\leq 1$ , $\operatorname {sl} \operatorname {arcsl} x=x$ and $\operatorname {cl} \operatorname {arccl} x=x$

For the halving of the lemniscate arc length these formulas are valid:

${\begin{aligned}{\operatorname {sl} }{\bigl (}{\tfrac {1}{2}}\operatorname {arcsl} x{\bigr )}&={\sin }{\bigl (}{\tfrac {1}{2}}\arcsin x{\bigr )}\,{\operatorname {sech} }{\bigl (}{\tfrac {1}{2}}\operatorname {arsinh} x{\bigr )}\\{\operatorname {sl} }{\bigl (}{\tfrac {1}{2}}\operatorname {arcsl} x{\bigr )}^{2}&={\tan }{\bigl (}{\tfrac {1}{4}}\arcsin x^{2}{\bigr )}\end{aligned}}$

Furthermore there are the so called Hyperbolic lemniscate area functions:

$\operatorname {aslh} (x)=\int _{0}^{x}{\frac {1}{\sqrt {y^{4}+1}}}\mathrm {d} y={\tfrac {1}{2}}F\left(2\arctan x;{\tfrac {1}{\sqrt {2}}}\right)$

$\operatorname {aclh} (x)=\int _{x}^{\infty }{\frac {1}{\sqrt {y^{4}+1}}}\mathrm {d} y={\tfrac {1}{2}}F\left(2\operatorname {arccot} x;{\tfrac {1}{\sqrt {2}}}\right)$

$\operatorname {aclh} (x)={\frac {\varpi }{\sqrt {2}}}-\operatorname {aslh} (x)$

$\operatorname {aslh} (x)={\sqrt {2}}\operatorname {arcsl} \left(x{\Big /}{\sqrt {\textstyle 1+{\sqrt {x^{4}+1}}}}\right)$

$\operatorname {arcsl} (x)={\sqrt {2}}\operatorname {aslh} \left(x{\Big /}{\sqrt {\textstyle 1+{\sqrt {1-x^{4}}}}}\right)$

### Expression using elliptic integrals

The lemniscate arcsine and the lemniscate arccosine can also be expressed by the Legendre-Form:

These functions can be displayed directly by using the incomplete elliptic integral of the first kind:

$\operatorname {arcsl} x={\frac {1}{\sqrt {2}}}F\left({\arcsin }{\frac {{\sqrt {2}}x}{\sqrt {1+x^{2}}}};{\frac {1}{\sqrt {2}}}\right)$

$\operatorname {arcsl} x=2({\sqrt {2}}-1)F\left({\arcsin }{\frac {({\sqrt {2}}+1)x}{{\sqrt {1+x^{2}}}+1}};({\sqrt {2}}-1)^{2}\right)$

The arc lengths of the lemniscate can also be expressed by only using the arc lengths of ellipses (calculated by elliptic integrals of the second kind):

${\begin{aligned}\operatorname {arcsl} x={}&{\frac {2+{\sqrt {2}}}{2}}E\left({\arcsin }{\frac {({\sqrt {2}}+1)x}{{\sqrt {1+x^{2}}}+1}};({\sqrt {2}}-1)^{2}\right)\\[5mu]&\ \ -E\left({\arcsin }{\frac {{\sqrt {2}}x}{\sqrt {1+x^{2}}}};{\frac {1}{\sqrt {2}}}\right)+{\frac {x{\sqrt {1-x^{2}}}}{{\sqrt {2}}(1+x^{2}+{\sqrt {1+x^{2}}})}}\end{aligned}}$

The lemniscate arccosine has this expression:

$\operatorname {arccl} x={\frac {1}{\sqrt {2}}}F\left(\arccos x;{\frac {1}{\sqrt {2}}}\right)$

### Use in integration

The lemniscate arcsine can be used to integrate many functions. Here is a list of important integrals (the constants of integration are omitted):

$\int {\frac {1}{\sqrt {1-x^{4}}}}\,\mathrm {d} x=\operatorname {arcsl} x$

$\int {\frac {1}{\sqrt {(x^{2}+1)(2x^{2}+1)}}}\,\mathrm {d} x={\operatorname {arcsl} }{\frac {x}{\sqrt {x^{2}+1}}}$

$\int {\frac {1}{\sqrt {x^{4}+6x^{2}+1}}}\,\mathrm {d} x={\operatorname {arcsl} }{\frac {{\sqrt {2}}x}{\sqrt {{\sqrt {x^{4}+6x^{2}+1}}+x^{2}+1}}}$

$\int {\frac {1}{\sqrt {x^{4}+1}}}\,\mathrm {d} x={{\sqrt {2}}\operatorname {arcsl} }{\frac {x}{\sqrt {{\sqrt {x^{4}+1}}+1}}}$

$\int {\frac {1}{\sqrt[{4}]{(1-x^{4})^{3}}}}\,\mathrm {d} x={{\sqrt {2}}\operatorname {arcsl} }{\frac {x}{\sqrt {1+{\sqrt {1-x^{4}}}}}}$

$\int {\frac {1}{\sqrt[{4}]{(x^{4}+1)^{3}}}}\,\mathrm {d} x={\operatorname {arcsl} }{\frac {x}{\sqrt[{4}]{x^{4}+1}}}$

$\int {\frac {1}{\sqrt[{4}]{(1-x^{2})^{3}}}}\,\mathrm {d} x={2\operatorname {arcsl} }{\frac {x}{1+{\sqrt {1-x^{2}}}}}$

$\int {\frac {1}{\sqrt[{4}]{(x^{2}+1)^{3}}}}\,\mathrm {d} x={2\operatorname {arcsl} }{\frac {x}{{\sqrt {x^{2}+1}}+1}}$

$\int {\frac {1}{\sqrt[{4}]{(ax^{2}+bx+c)^{3}}}}\,\mathrm {d} x={{\frac {2{\sqrt {2}}}{\sqrt[{4}]{4a^{2}c-ab^{2}}}}\operatorname {arcsl} }{\frac {2ax+b}{{\sqrt {4a(ax^{2}+bx+c)}}+{\sqrt {4ac-b^{2}}}}}$

$\int {\sqrt {\operatorname {sech} x}}\,\mathrm {d} x={2\operatorname {arcsl} }\tanh {\tfrac {1}{2}}x$

$\int {\sqrt {\sec x}}\,\mathrm {d} x={2\operatorname {arcsl} }\tan {\tfrac {1}{2}}x$


## Hyperbolic lemniscate functions

### Fundamental information

For convenience, let $\sigma ={\sqrt {2}}\varpi$ . $\sigma$ is the "squircular" analog of $\pi$ (see below). The decimal expansion of $\sigma$ (i.e. $3.7081\ldots$ ) appears in entry 34e of chapter 11 of Ramanujan's second notebook.

The hyperbolic lemniscate sine (slh) and cosine (clh) can be defined as inverses of elliptic integrals as follows:

$z\mathrel {\overset {*}{=}} \int _{0}^{\operatorname {slh} z}{\frac {\mathrm {d} t}{\sqrt {1+t^{4}}}}=\int _{\operatorname {clh} z}^{\infty }{\frac {\mathrm {d} t}{\sqrt {1+t^{4}}}}$

where in $(*)$ , z is in the square with corners $\{\sigma /2,\sigma i/2,-\sigma /2,-\sigma i/2\}$ . Beyond that square, the functions can be analytically continued to meromorphic functions in the whole complex plane.

The complete integral has the value:

$\int _{0}^{\infty }{\frac {\mathrm {d} t}{\sqrt {t^{4}+1}}}={\tfrac {1}{4}}\mathrm {B} {\bigl (}{\tfrac {1}{4}},{\tfrac {1}{4}}{\bigr )}={\frac {\sigma }{2}}=1.85407\;46773\;01371\ldots$

Therefore, the two defined functions have following relation to each other:

$\operatorname {slh} z={\operatorname {clh} }{{\Bigl (}{\frac {\sigma }{2}}-z{\Bigr )}}$

The product of hyperbolic lemniscate sine and hyperbolic lemniscate cosine is equal to one:

$\operatorname {slh} z\,\operatorname {clh} z=1$

The functions $\operatorname {slh}$ and $\operatorname {clh}$ have a square period lattice with fundamental periods $\{\sigma ,\sigma i\}$ .

The hyperbolic lemniscate functions can be expressed in terms of lemniscate sine and lemniscate cosine:

$\operatorname {slh} {\bigl (}{\sqrt {2}}z{\bigr )}={\frac {(1+\operatorname {cl} ^{2}z)\operatorname {sl} z}{{\sqrt {2}}\operatorname {cl} z}}$

$\operatorname {clh} {\bigl (}{\sqrt {2}}z{\bigr )}={\frac {(1+\operatorname {sl} ^{2}z)\operatorname {cl} z}{{\sqrt {2}}\operatorname {sl} z}}$

But there is also a relation to the Jacobi elliptic functions with the elliptic modulus one by square root of two:

$\operatorname {slh} z={\frac {\operatorname {sn} (z;1/{\sqrt {2}})}{\operatorname {cd} (z;1/{\sqrt {2}})}}$

$\operatorname {clh} z={\frac {\operatorname {cd} (z;1/{\sqrt {2}})}{\operatorname {sn} (z;1/{\sqrt {2}})}}$

The hyperbolic lemniscate sine has following imaginary relation to the lemniscate sine:

$\operatorname {slh} z={\frac {1-i}{\sqrt {2}}}\operatorname {sl} \left({\frac {1+i}{\sqrt {2}}}z\right)={\frac {\operatorname {sl} \left({\sqrt[{4}]{-1}}z\right)}{\sqrt[{4}]{-1}}}$

This is analogous to the relationship between hyperbolic and trigonometric sine:

$\sinh z=-i\sin(iz)={\frac {\sin \left({\sqrt[{2}]{-1}}z\right)}{\sqrt[{2}]{-1}}}$

### Relation to quartic Fermat curve

#### Hyperbolic Lemniscate Tangent and Cotangent

This image shows the standardized superelliptic Fermat squircle curve of the fourth degree:

In a quartic Fermat curve $x^{4}+y^{4}=1$ (sometimes called a squircle) the hyperbolic lemniscate sine and cosine are analogous to the tangent and cotangent functions in a unit circle $x^{2}+y^{2}=1$ (the quadratic Fermat curve). If the origin and a point on the curve are connected to each other by a line ⁠ L ⁠, the hyperbolic lemniscate sine of twice the enclosed area between this line and the x-axis is the y-coordinate of the intersection of ⁠ L ⁠ with the line $x=1$ . Just as $\pi$ is the area enclosed by the circle $x^{2}+y^{2}=1$ , the area enclosed by the squircle $x^{4}+y^{4}=1$ is $\sigma$ . Moreover,

$M(1,1/{\sqrt {2}})={\frac {\pi }{\sigma }}$

where M is the arithmetic–geometric mean.

The hyperbolic lemniscate sine satisfies the argument addition identity:

$\operatorname {slh} (a+b)={\frac {\operatorname {slh} a\operatorname {slh} 'b+\operatorname {slh} b\operatorname {slh} 'a}{1-\operatorname {slh} ^{2}a\,\operatorname {slh} ^{2}b}}$

When u is real, the derivative and the original antiderivative of $\operatorname {slh}$ and $\operatorname {clh}$ can be expressed in this way:

| ${\frac {\mathrm {d} }{\mathrm {d} u}}\operatorname {slh} (u)={\sqrt {1+\operatorname {slh} (u)^{4}}}$ ${\frac {\mathrm {d} }{\mathrm {d} u}}\operatorname {clh} (u)=-{\sqrt {1+\operatorname {clh} (u)^{4}}}$ ${\frac {\mathrm {d} }{\mathrm {d} u}}\,{\frac {1}{2}}\operatorname {arsinh} {\bigl [}\operatorname {slh} (u)^{2}{\bigr ]}=\operatorname {slh} (u)$ ${\frac {\mathrm {d} }{\mathrm {d} u}}-\,{\frac {1}{2}}\operatorname {arsinh} {\bigl [}\operatorname {clh} (u)^{2}{\bigr ]}=\operatorname {clh} (u)$ |
|---|

There are also the Hyperbolic lemniscate tangent and the Hyperbolic lemniscate cotangent as further functions:

The functions tlh and ctlh fulfill the identities described in the differential equation mentioned:

${\text{tlh}}({\sqrt {2}}\,u)=\sin _{4}({\sqrt {2}}\,u)=\operatorname {sl} (u){\sqrt {\frac {\operatorname {cl} ^{2}u+1}{\operatorname {sl} ^{2}u+\operatorname {cl} ^{2}u}}}$

${\text{ctlh}}({\sqrt {2}}\,u)=\cos _{4}({\sqrt {2}}\,u)=\operatorname {cl} (u){\sqrt {\frac {\operatorname {sl} ^{2}u+1}{\operatorname {sl} ^{2}u+\operatorname {cl} ^{2}u}}}$

The functional designation sl stands for the lemniscatic sine and the designation cl stands for the lemniscatic cosine. In addition, those relations to the Jacobi elliptic functions are valid:

${\text{tlh}}(u)={\frac {{\text{sn}}(u;{\tfrac {1}{2}}{\sqrt {2}})}{\sqrt[{4}]{{\text{cd}}(u;{\tfrac {1}{2}}{\sqrt {2}})^{4}+{\text{sn}}(u;{\tfrac {1}{2}}{\sqrt {2}})^{4}}}}$

${\text{ctlh}}(u)={\frac {{\text{cd}}(u;{\tfrac {1}{2}}{\sqrt {2}})}{\sqrt[{4}]{{\text{cd}}(u;{\tfrac {1}{2}}{\sqrt {2}})^{4}+{\text{sn}}(u;{\tfrac {1}{2}}{\sqrt {2}})^{4}}}}$

When u is real, the derivative and quarter period integral of $\operatorname {tlh}$ and $\operatorname {ctlh}$ can be expressed in this way:

| ${\frac {\mathrm {d} }{\mathrm {d} u}}\operatorname {tlh} (u)=\operatorname {ctlh} (u)^{3}$ ${\frac {\mathrm {d} }{\mathrm {d} u}}\operatorname {ctlh} (u)=-\operatorname {tlh} (u)^{3}$ $\int _{0}^{\varpi /{\sqrt {2}}}\operatorname {tlh} (u)\,\mathrm {d} u={\frac {\varpi }{2}}$ $\int _{0}^{\varpi /{\sqrt {2}}}\operatorname {ctlh} (u)\,\mathrm {d} u={\frac {\varpi }{2}}$ |
|---|

#### Derivation of the Hyperbolic Lemniscate functions

The horizontal and vertical coordinates of this superellipse are dependent on twice the enclosed area w = 2A, so the following conditions must be met:

$x(w)^{4}+y(w)^{4}=1$

${\frac {\mathrm {d} }{\mathrm {d} w}}x(w)=-y(w)^{3}$

${\frac {\mathrm {d} }{\mathrm {d} w}}y(w)=x(w)^{3}$

$x(w=0)=1$

$y(w=0)=0$

The solutions to this system of equations are as follows:

$x(w)=\operatorname {cl} ({\tfrac {1}{2}}{\sqrt {2}}w)[\operatorname {sl} ({\tfrac {1}{2}}{\sqrt {2}}w)^{2}+1]^{1/2}[\operatorname {sl} ({\tfrac {1}{2}}{\sqrt {2}}w)^{2}+\operatorname {cl} ({\tfrac {1}{2}}{\sqrt {2}}w)^{2}]^{-1/2}$

$y(w)=\operatorname {sl} ({\tfrac {1}{2}}{\sqrt {2}}w)[\operatorname {cl} ({\tfrac {1}{2}}{\sqrt {2}}w)^{2}+1]^{1/2}[\operatorname {sl} ({\tfrac {1}{2}}{\sqrt {2}}w)^{2}+\operatorname {cl} ({\tfrac {1}{2}}{\sqrt {2}}w)^{2}]^{-1/2}$

The following therefore applies to the quotient:

${\frac {y(w)}{x(w)}}={\frac {\operatorname {sl} ({\tfrac {1}{2}}{\sqrt {2}}w)[\operatorname {cl} ({\tfrac {1}{2}}{\sqrt {2}}w)^{2}+1]^{1/2}}{\operatorname {cl} ({\tfrac {1}{2}}{\sqrt {2}}w)[\operatorname {sl} ({\tfrac {1}{2}}{\sqrt {2}}w)^{2}+1]^{1/2}}}=\operatorname {slh} (w)$

The functions x(w) and y(w) are called **cotangent hyperbolic lemniscatus** and **hyperbolic tangent**.

$x(w)={\text{ctlh}}(w)$

$y(w)={\text{tlh}}(w)$

The sketch also shows the fact that the derivation of the Areasinus hyperbolic lemniscatus function is equal to the reciprocal of the square root of the successor of the fourth power function.

### Specific values

This list shows the values of the **Hyperbolic Lemniscate Sine** accurately. Recall that,

$\int _{0}^{\infty }{\frac {\operatorname {d} t}{\sqrt {t^{4}+1}}}={\tfrac {1}{4}}\mathrm {B} {\bigl (}{\tfrac {1}{4}},{\tfrac {1}{4}}{\bigr )}={\frac {\varpi }{\sqrt {2}}}={\frac {\sigma }{2}}=1.85407\ldots$

whereas ${\tfrac {1}{2}}\mathrm {B} {\bigl (}{\tfrac {1}{2}},{\tfrac {1}{2}}{\bigr )}={\tfrac {\pi }{2}},$ so the values below such as ${\operatorname {slh} }{\bigl (}{\tfrac {\varpi }{2{\sqrt {2}}}}{\bigr )}={\operatorname {slh} }{\bigl (}{\tfrac {\sigma }{4}}{\bigr )}=1$ are analogous to the trigonometric ${\sin }{\bigl (}{\tfrac {\pi }{2}}{\bigr )}=1$ .

$\operatorname {slh} \,\left({\frac {\varpi }{2{\sqrt {2}}}}\right)=1$

$\operatorname {slh} \,\left({\frac {\varpi }{3{\sqrt {2}}}}\right)={\frac {1}{\sqrt[{4}]{3}}}{\sqrt[{4}]{2{\sqrt {3}}-3}}$

$\operatorname {slh} \,\left({\frac {2\varpi }{3{\sqrt {2}}}}\right)={\sqrt[{4}]{2{\sqrt {3}}+3}}$

$\operatorname {slh} \,\left({\frac {\varpi }{4{\sqrt {2}}}}\right)={\frac {1}{\sqrt[{4}]{2}}}({\sqrt {{\sqrt {2}}+1}}-1)$

$\operatorname {slh} \,\left({\frac {3\varpi }{4{\sqrt {2}}}}\right)={\frac {1}{\sqrt[{4}]{2}}}({\sqrt {{\sqrt {2}}+1}}+1)$

$\operatorname {slh} \,\left({\frac {\varpi }{5{\sqrt {2}}}}\right)={\frac {1}{\sqrt[{4}]{8}}}{\sqrt {{\sqrt {5}}-1}}{\sqrt {{\sqrt[{4}]{20}}-{\sqrt {{\sqrt {5}}+1}}}}=2{\sqrt[{4}]{{\sqrt {5}}-2}}{\sqrt {\sin({\tfrac {1}{20}}\pi )\sin({\tfrac {3}{20}}\pi )}}$

$\operatorname {slh} \,\left({\frac {2\varpi }{5{\sqrt {2}}}}\right)={\frac {1}{2{\sqrt[{4}]{2}}}}({\sqrt {5}}+1){\sqrt {{\sqrt[{4}]{20}}-{\sqrt {{\sqrt {5}}+1}}}}=2{\sqrt[{4}]{{\sqrt {5}}+2}}{\sqrt {\sin({\tfrac {1}{20}}\pi )\sin({\tfrac {3}{20}}\pi )}}$

$\operatorname {slh} \,\left({\frac {3\varpi }{5{\sqrt {2}}}}\right)={\frac {1}{\sqrt[{4}]{8}}}{\sqrt {{\sqrt {5}}-1}}{\sqrt {{\sqrt[{4}]{20}}+{\sqrt {{\sqrt {5}}+1}}}}=2{\sqrt[{4}]{{\sqrt {5}}-2}}{\sqrt {\cos({\tfrac {1}{20}}\pi )\cos({\tfrac {3}{20}}\pi )}}$

$\operatorname {slh} \,\left({\frac {4\varpi }{5{\sqrt {2}}}}\right)={\frac {1}{2{\sqrt[{4}]{2}}}}({\sqrt {5}}+1){\sqrt {{\sqrt[{4}]{20}}+{\sqrt {{\sqrt {5}}+1}}}}=2{\sqrt[{4}]{{\sqrt {5}}+2}}{\sqrt {\cos({\tfrac {1}{20}}\pi )\cos({\tfrac {3}{20}}\pi )}}$

$\operatorname {slh} \,\left({\frac {\varpi }{6{\sqrt {2}}}}\right)={\frac {1}{2}}({\sqrt {2{\sqrt {3}}+3}}+1)(1-{\sqrt[{4}]{2{\sqrt {3}}-3}})$

$\operatorname {slh} \,\left({\frac {5\varpi }{6{\sqrt {2}}}}\right)={\frac {1}{2}}({\sqrt {2{\sqrt {3}}+3}}+1)(1+{\sqrt[{4}]{2{\sqrt {3}}-3}})$

That table shows the most important values of the **Hyperbolic Lemniscate Tangent and Cotangent** functions:

| z | $\operatorname {clh} z$ | $\operatorname {slh} z$ | $\operatorname {ctlh} z=\cos _{4}z$ | $\operatorname {tlh} z=\sin _{4}z$ |
|---|---|---|---|---|
| 0 | $\infty$ | 0 | 1 | 0 |
| ${\tfrac {1}{4}}\sigma$ | 1 | 1 | $1{\big /}{\sqrt[{4}]{2}}$ | $1{\big /}{\sqrt[{4}]{2}}$ |
| ${\tfrac {1}{2}}\sigma$ | 0 | $\infty$ | 0 | 1 |
| ${\tfrac {3}{4}}\sigma$ | $-1$ | $-1$ | $-1{\big /}{\sqrt[{4}]{2}}$ | $1{\big /}{\sqrt[{4}]{2}}$ |
| $\sigma$ | $\infty$ | 0 | $-1$ | 0 |


## Number theory

In algebraic number theory, every finite abelian extension of the Gaussian rationals $\mathbb {Q} (i)$ is a subfield of $\mathbb {Q} (i,\omega _{n})$ for some positive integer n . This is analogous to the Kronecker–Weber theorem for the rational numbers $\mathbb {Q}$ which is based on division of the circle – in particular, every finite abelian extension of $\mathbb {Q}$ is a subfield of $\mathbb {Q} (\zeta _{n})$ for some positive integer n . Both are special cases of Kronecker's Jugendtraum, which became Hilbert's twelfth problem.

The field $\mathbb {Q} (i,\operatorname {sl} (\varpi /n))$ (for positive odd n ) is the extension of $\mathbb {Q} (i)$ generated by the x - and y -coordinates of the $(1+i)n$ -torsion points on the elliptic curve $y^{2}=4x^{3}+x$ .

### Hurwitz numbers

The Bernoulli numbers $\mathrm {B} _{n}$ can be defined by

$\mathrm {B} _{n}=\lim _{z\to 0}{\frac {\mathrm {d} ^{n}}{\mathrm {d} z^{n}}}{\frac {z}{e^{z}-1}},\quad n\geq 0$

and appear in

$\sum _{k\in \mathbb {Z} \setminus \{0\}}{\frac {1}{k^{2n}}}=(-1)^{n-1}\mathrm {B} _{2n}{\frac {(2\pi )^{2n}}{(2n)!}}=2\zeta (2n),\quad n\geq 1$

where $\zeta$ is the Riemann zeta function.

The **Hurwitz numbers** $\mathrm {H} _{n},$ named after Adolf Hurwitz, are the "lemniscate analogs" of the Bernoulli numbers. They can be defined by

$\mathrm {H} _{n}=-\lim _{z\to 0}{\frac {\mathrm {d} ^{n}}{\mathrm {d} z^{n}}}z\zeta (z;1/4,0),\quad n\geq 0$

where $\zeta (\cdot ;1/4,0)$ is the Weierstrass zeta function with lattice invariants $1/4$ and 0 . They appear in

$\sum _{z\in \mathbb {Z} [i]\setminus \{0\}}{\frac {1}{z^{4n}}}=\mathrm {H} _{4n}{\frac {(2\varpi )^{4n}}{(4n)!}}=G_{4n}(i),\quad n\geq 1$

where $\mathbb {Z} [i]$ are the Gaussian integers and $G_{4n}$ are the Eisenstein series of weight $4n$ , and in

$\displaystyle {\begin{array}{ll}\displaystyle \sum _{n=1}^{\infty }{\dfrac {n^{k}}{e^{2\pi n}-1}}={\begin{cases}{\dfrac {1}{24}}-{\dfrac {1}{8\pi }}&{\text{if}}\ k=1\\{\dfrac {\mathrm {B} _{k+1}}{2k+2}}&{\text{if}}\ k\equiv 1\,(\mathrm {mod} \,4)\ {\text{and}}\ k\geq 5\\{\dfrac {\mathrm {B} _{k+1}}{2k+2}}+{\dfrac {\mathrm {H} _{k+1}}{2k+2}}\left({\dfrac {\varpi }{\pi }}\right)^{k+1}&{\text{if}}\ k\equiv 3\,(\mathrm {mod} \,4)\ {\text{and}}\ k\geq 3.\\\end{cases}}\end{array}}$

The Hurwitz numbers can also be determined as follows: $\mathrm {H} _{4}=1/10$ ,

$\mathrm {H} _{4n}={\frac {3}{(2n-3)(16n^{2}-1)}}\sum _{k=1}^{n-1}{\binom {4n}{4k}}(4k-1)(4(n-k)-1)\mathrm {H} _{4k}\mathrm {H} _{4(n-k)},\quad n\geq 2$

and $\mathrm {H} _{n}=0$ if n is not a multiple of 4 . This yields

$\mathrm {H} _{8}={\frac {3}{10}},\,\mathrm {H} _{12}={\frac {567}{130}},\,\mathrm {H} _{16}={\frac {43\,659}{170}},\,\ldots$

Also

$\operatorname {denom} \mathrm {H} _{4n}=\prod _{(p-1)|4n}p$

where $p\in \mathbb {P}$ such that $p\not \equiv 3\,({\text{mod}}\,4),$ just as

$\operatorname {denom} \mathrm {B} _{2n}=\prod _{(p-1)|2n}p$

where $p\in \mathbb {P}$ (by the von Staudt–Clausen theorem).

In fact, the von Staudt–Clausen theorem determines the fractional part of the Bernoulli numbers:

$\mathrm {B} _{2n}+\sum _{(p-1)|2n}{\frac {1}{p}}\in \mathbb {Z} ,\quad n\geq 1$

(sequence A000146 in the OEIS) where p is any prime, and an analogous theorem holds for the Hurwitz numbers: suppose that $a\in \mathbb {Z}$ is odd, $b\in \mathbb {Z}$ is even, p is a prime such that $p\equiv 1\,(\mathrm {mod} \,4)$ , $p=a^{2}+b^{2}$ (see Fermat's theorem on sums of two squares) and $a\equiv b+1\,(\mathrm {mod} \,4)$ . Then for any given p , $2a=\nu (p)$ is uniquely determined; equivalently $\nu (p)=p-{\mathcal {N}}_{p}$ where ${\mathcal {N}}_{p}$ is the number of solutions of the congruence $X^{3}-X\equiv Y^{2}\,(\operatorname {mod} p)$ in variables $X,Y$ that are non-negative integers. The Hurwitz theorem then determines the fractional part of the Hurwitz numbers:

$\mathrm {H} _{4n}-{\frac {1}{2}}-\sum _{(p-1)|4n}{\frac {\nu (p)^{4n/(p-1)}}{p}}\mathrel {\overset {\text{def}}{=}} \mathrm {G} _{n}\in \mathbb {Z} ,\quad n\geq 1.$

The sequence of the integers $\mathrm {G} _{n}$ starts with $0,-1,5,253,\ldots .$

Let $n\geq 2$ . If $4n+1$ is a prime, then $\mathrm {G} _{n}\equiv 1\,(\mathrm {mod} \,4)$ . If $4n+1$ is not a prime, then $\mathrm {G} _{n}\equiv 3\,(\mathrm {mod} \,4)$ .

Some authors instead define the Hurwitz numbers as $\mathrm {H} _{n}'=\mathrm {H} _{4n}$ .

#### Appearances in Laurent series

The Hurwitz numbers appear in several Laurent series expansions related to the lemniscate functions:

${\begin{aligned}\operatorname {sl} ^{2}z&=\sum _{n=1}^{\infty }{\frac {2^{4n}(1-(-1)^{n}2^{2n})\mathrm {H} _{4n}}{4n}}{\frac {z^{4n-2}}{(4n-2)!}},\quad \left|z\right|<{\frac {\varpi }{\sqrt {2}}}\\{\frac {\operatorname {sl} 'z}{\operatorname {sl} {z}}}&={\frac {1}{z}}-\sum _{n=1}^{\infty }{\frac {2^{4n}(2-(-1)^{n}2^{2n})\mathrm {H} _{4n}}{4n}}{\frac {z^{4n-1}}{(4n-1)!}},\quad \left|z\right|<{\frac {\varpi }{\sqrt {2}}}\\{\frac {1}{\operatorname {sl} z}}&={\frac {1}{z}}-\sum _{n=1}^{\infty }{\frac {2^{2n}((-1)^{n}2-2^{2n})\mathrm {H} _{4n}}{4n}}{\frac {z^{4n-1}}{(4n-1)!}},\quad \left|z\right|<\varpi \\{\frac {1}{\operatorname {sl} ^{2}z}}&={\frac {1}{z^{2}}}+\sum _{n=1}^{\infty }{\frac {2^{4n}\mathrm {H} _{4n}}{4n}}{\frac {z^{4n-2}}{(4n-2)!}},\quad \left|z\right|<\varpi \end{aligned}}$

Analogously, in terms of the Bernoulli numbers:

${\frac {1}{\sinh ^{2}z}}={\frac {1}{z^{2}}}-\sum _{n=1}^{\infty }{\frac {2^{2n}\mathrm {B} _{2n}}{2n}}{\frac {z^{2n-2}}{(2n-2)!}},\quad \left|z\right|<\pi .$

### A quartic analog of the Legendre symbol

Let p be a prime such that $p\equiv 1\,({\text{mod}}\,4)$ . A **quartic residue** (mod p ) is any number congruent to the fourth power of an integer. Define $\left({\tfrac {a}{p}}\right)_{4}$ to be 1 if a is a quartic residue (mod p ) and define it to be $-1$ if a is not a quartic residue (mod p ).

If a and p are coprime, then there exist numbers $p'\in \mathbb {Z} [i]$ (see for these numbers) such that

$\left({\frac {a}{p}}\right)_{4}=\prod _{p'}{\frac {\operatorname {sl} (2\varpi ap'/p)}{\operatorname {sl} (2\varpi p'/p)}}.$

This theorem is analogous to

$\left({\frac {a}{p}}\right)=\prod _{n=1}^{\frac {p-1}{2}}{\frac {\sin(2\pi an/p)}{\sin(2\pi n/p)}}$

where $\left({\tfrac {\cdot }{\cdot }}\right)$ is the Legendre symbol.


## World map projections

The Peirce quincuncial projection, designed by Charles Sanders Peirce of the US Coast Survey in the 1870s, is a world map projection based on the inverse lemniscate sine of stereographically projected points (treated as complex numbers).

When lines of constant real or imaginary part are projected onto the complex plane via the hyperbolic lemniscate sine, and thence stereographically projected onto the sphere (see Riemann sphere), the resulting curves are spherical conics, the spherical analog of planar ellipses and hyperbolas. Thus the lemniscate functions (and more generally, the Jacobi elliptic functions) provide a parametrization for spherical conics.

A conformal map projection from the globe onto the 6 square faces of a cube can also be defined using the lemniscate functions. Because many partial differential equations can be effectively solved by conformal mapping, this map from sphere to cube is convenient for atmospheric modeling.
