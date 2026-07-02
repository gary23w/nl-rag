---
title: "Jacobi polynomials"
source: https://en.wikipedia.org/wiki/Jacobi_polynomials
domain: orthogonal-polynomials
license: CC-BY-SA-4.0
tags: orthogonal polynomials, hermite polynomials, chebyshev polynomials, jacobi polynomials
fetched: 2026-07-02
---

# Jacobi polynomials

In mathematics, **Jacobi polynomials** (occasionally called **hypergeometric polynomials**) $P_{n}^{(\alpha ,\beta )}(x)$ are a class of classical orthogonal polynomials. They are orthogonal with respect to the weight $(1-x)^{\alpha }(1+x)^{\beta }$ on the interval $[-1,1]$ . The Gegenbauer polynomials, and thus also the Legendre, Zernike and Chebyshev polynomials, are special cases of the Jacobi polynomials.

The Jacobi polynomials were introduced by Carl Gustav Jacob Jacobi.

## Definitions

### Via the hypergeometric function

The Jacobi polynomials are defined via the hypergeometric function as follows:

$P_{n}^{(\alpha ,\beta )}(z)={\frac {(\alpha +1)_{n}}{n!}}\,{}_{2}F_{1}\left(-n,1+\alpha +\beta +n;\alpha +1;{\tfrac {1}{2}}(1-z)\right),$

where $(\alpha +1)_{n}$ is Pochhammer's symbol (for the rising factorial). In this case, the series for the hypergeometric function is finite, therefore one obtains the following equivalent expression:

$P_{n}^{(\alpha ,\beta )}(z)={\frac {\Gamma (\alpha +n+1)}{n!\,\Gamma (\alpha +\beta +n+1)}}\sum _{m=0}^{n}{n \choose m}{\frac {\Gamma (\alpha +\beta +n+m+1)}{\Gamma (\alpha +m+1)}}\left({\frac {z-1}{2}}\right)^{m}.$

### Rodrigues' formula

An equivalent definition is given by Rodrigues' formula:

$P_{n}^{(\alpha ,\beta )}(z)={\frac {(-1)^{n}}{2^{n}n!}}(1-z)^{-\alpha }(1+z)^{-\beta }{\frac {d^{n}}{dz^{n}}}\left\{(1-z)^{\alpha }(1+z)^{\beta }\left(1-z^{2}\right)^{n}\right\}.$

If $\alpha =\beta =0$ , then it reduces to the Legendre polynomials:

$P_{n}(z)={\frac {1}{2^{n}n!}}{\frac {d^{n}}{dz^{n}}}(z^{2}-1)^{n}\;.$

### Differential equation

The Jacobi polynomials $P_{n}^{(\alpha ,\beta )}$ is, up to scaling, the unique polynomial solution of the Sturm–Liouville problem

$\left(1-x^{2}\right)y''+(\beta -\alpha -(\alpha +\beta +2)x)y'=\lambda y$

where $\lambda =-n(n+\alpha +\beta +1)$ . The other solution involves the logarithm function. Bochner's theorem states that the Jacobi polynomials are uniquely characterized as polynomial solutions to Sturm–Liouville problems with polynomial coefficients.

### Alternate expression for real argument

For real x the Jacobi polynomial can alternatively be written as

$P_{n}^{(\alpha ,\beta )}(x)=\sum _{s=0}^{n}{n+\alpha \choose n-s}{n+\beta \choose s}\left({\frac {x-1}{2}}\right)^{s}\left({\frac {x+1}{2}}\right)^{n-s}$

and for integer n

${z \choose n}={\begin{cases}{\frac {\Gamma (z+1)}{\Gamma (n+1)\Gamma (z-n+1)}}&n\geq 0\\0&n<0\end{cases}}$

where $\Gamma (z)$ is the gamma function.

In the special case that the four quantities n , $n+\alpha$ , $n+\beta$ , $n+\alpha +\beta$ are nonnegative integers, the Jacobi polynomial can be written as

| $P_{n}^{(\alpha ,\beta )}(x)=(n+\alpha )!(n+\beta )!\sum _{s=0}^{n}{\frac {1}{s!(n+\alpha -s)!(\beta +s)!(n-s)!}}\left({\frac {x-1}{2}}\right)^{n-s}\left({\frac {x+1}{2}}\right)^{s}.$ |   | 1 |
|---|---|---|

The sum extends over all integer values of s for which the arguments of the factorials are nonnegative.

### Special cases

$P_{0}^{(\alpha ,\beta )}(z)=1,$

$P_{1}^{(\alpha ,\beta )}(z)=(\alpha +1)+(\alpha +\beta +2){\frac {z-1}{2}},$

$P_{2}^{(\alpha ,\beta )}(z)={\frac {(\alpha +1)(\alpha +2)}{2}}+(\alpha +2)(\alpha +\beta +3){\frac {z-1}{2}}+{\frac {(\alpha +\beta +3)(\alpha +\beta +4)}{2}}\left({\frac {z-1}{2}}\right)^{2}.$

$P_{n}^{(\alpha ,\beta )}(z)={\frac {\Gamma (1+2n+\alpha +\beta )}{\Gamma (1+n)\Gamma (1+n+\alpha +\beta )}}\left({\frac {z}{2}}\right)^{n}+{\text{ lower-degree terms }}$ Thus, the leading coefficient is ${\frac {\Gamma (1+2n+\alpha +\beta )}{2^{n}n!\Gamma (1+n+\alpha +\beta )}}$ .

## Basic properties

### Orthogonality

The Jacobi polynomials satisfy the orthogonality condition

$\int _{-1}^{1}(1-x)^{\alpha }(1+x)^{\beta }P_{m}^{(\alpha ,\beta )}(x)P_{n}^{(\alpha ,\beta )}(x)\,dx={\frac {2^{\alpha +\beta +1}}{2n+\alpha +\beta +1}}{\frac {\Gamma (n+\alpha +1)\Gamma (n+\beta +1)}{\Gamma (n+\alpha +\beta +1)n!}}\delta _{nm},\qquad \alpha ,\ \beta >-1.$

As defined, they do not have unit norm with respect to the weight. This can be corrected by dividing by the square root of the right hand side of the equation above, when $n=m$ .

Although it does not yield an orthonormal basis, an alternative normalization is sometimes preferred due to its simplicity:

$P_{n}^{(\alpha ,\beta )}(1)={n+\alpha \choose n}.$

### Symmetry relation

The polynomials have the symmetry relation

$P_{n}^{(\alpha ,\beta )}(-z)=(-1)^{n}P_{n}^{(\beta ,\alpha )}(z);$

thus the other terminal value is

$P_{n}^{(\alpha ,\beta )}(-1)=(-1)^{n}{n+\beta \choose n}.$

### Derivatives

The k th derivative of the explicit expression leads to

${\frac {d^{k}}{dz^{k}}}P_{n}^{(\alpha ,\beta )}(z)={\frac {\Gamma (\alpha +\beta +n+1+k)}{2^{k}\Gamma (\alpha +\beta +n+1)}}P_{n-k}^{(\alpha +k,\beta +k)}(z).$

### Recurrence relations

The 3-term recurrence relation for the Jacobi polynomials of fixed $\alpha$ , $\beta$ is:

${\begin{aligned}&2n(n+\alpha +\beta )(2n+\alpha +\beta -2)P_{n}^{(\alpha ,\beta )}(z)\\&\qquad =(2n+\alpha +\beta -1){\Big \{}(2n+\alpha +\beta )(2n+\alpha +\beta -2)z+\alpha ^{2}-\beta ^{2}{\Big \}}P_{n-1}^{(\alpha ,\beta )}(z)-2(n+\alpha -1)(n+\beta -1)(2n+\alpha +\beta )P_{n-2}^{(\alpha ,\beta )}(z),\end{aligned}}$

for $n=2,3,\ldots$ . Writing for brevity $a:=n+\alpha$ , $b:=n+\beta$ and $c:=a+b=2n+\alpha +\beta$ , this becomes in terms of $a,b,c$

$2n(c-n)(c-2)P_{n}^{(\alpha ,\beta )}(z)=(c-1){\Big \{}c(c-2)z+(a-b)(c-2n){\Big \}}P_{n-1}^{(\alpha ,\beta )}(z)-2(a-1)(b-1)c\;P_{n-2}^{(\alpha ,\beta )}(z).$

Since the Jacobi polynomials can be described in terms of the hypergeometric function, recurrences of the hypergeometric function give equivalent recurrences of the Jacobi polynomials. In particular, Gauss' contiguous relations correspond to the identities

${\begin{aligned}(z-1){\frac {d}{dz}}P_{n}^{(\alpha ,\beta )}(z)&={\frac {1}{2}}(z-1)(1+\alpha +\beta +n)P_{n-1}^{(\alpha +1,\beta +1)}\\&=nP_{n}^{(\alpha ,\beta )}-(\alpha +n)P_{n-1}^{(\alpha ,\beta +1)}\\&=(1+\alpha +\beta +n)\left(P_{n}^{(\alpha ,\beta +1)}-P_{n}^{(\alpha ,\beta )}\right)\\&=(\alpha +n)P_{n}^{(\alpha -1,\beta +1)}-\alpha P_{n}^{(\alpha ,\beta )}\\&={\frac {2(n+1)P_{n+1}^{(\alpha ,\beta -1)}-\left(z(1+\alpha +\beta +n)+\alpha +1+n-\beta \right)P_{n}^{(\alpha ,\beta )}}{1+z}}\\&={\frac {(2\beta +n+nz)P_{n}^{(\alpha ,\beta )}-2(\beta +n)P_{n}^{(\alpha ,\beta -1)}}{1+z}}\\&={\frac {1-z}{1+z}}\left(\beta P_{n}^{(\alpha ,\beta )}-(\beta +n)P_{n}^{(\alpha +1,\beta -1)}\right)\,.\end{aligned}}$

### Generating function

The generating function of the Jacobi polynomials is given by

$\sum _{n=0}^{\infty }P_{n}^{(\alpha ,\beta )}(z)t^{n}=2^{\alpha +\beta }R^{-1}(1-t+R)^{-\alpha }(1+t+R)^{-\beta },$

where

$R=R(z,t)=\left(1-2zt+t^{2}\right)^{\frac {1}{2}}~,$

and the branch of square root is chosen so that $R(z,0)=1$ .

### Other polynomials

The Jacobi polynomials reduce to other classical polynomials.

Ultraspherical: ${\begin{aligned}C_{n}^{(\lambda )}(x)&={\frac {(2\lambda )_{n}}{\left(\lambda +{\frac {1}{2}}\right)_{n}}}P_{n}^{\left(\lambda -{\frac {1}{2}},\lambda -{\frac {1}{2}}\right)}(x),\\P_{n}^{(\alpha ,\alpha )}(x)&={\frac {(\alpha +1)_{n}}{(2\alpha +1)_{n}}}C_{n}^{\left(\alpha +{\frac {1}{2}}\right)}(x).\end{aligned}}$ Legendre: $P_{n}(x)=C_{n}^{\left({\frac {1}{2}}\right)}(x)=P_{n}^{(0,0)}(x)$ Chebyshev: ${\begin{aligned}T_{n}(x)&=P_{n}^{\left(-{\frac {1}{2}},-{\frac {1}{2}}\right)}(x)/P_{n}^{\left(-{\frac {1}{2}},-{\frac {1}{2}}\right)}(1),\\U_{n}(x)&=C_{n}^{(1)}(x)=(n+1)P_{n}^{\left({\frac {1}{2}},{\frac {1}{2}}\right)}(x)/P_{n}^{\left({\frac {1}{2}},{\frac {1}{2}}\right)}(1),\\V_{n}(x)&=P_{n}^{\left(-{\frac {1}{2}},{\frac {1}{2}}\right)}(x)/P_{n}^{\left(-{\frac {1}{2}},{\frac {1}{2}}\right)}(1),\\W_{n}(x)&=(2n+1)P_{n}^{\left({\frac {1}{2}},-{\frac {1}{2}}\right)}(x)/P_{n}^{\left({\frac {1}{2}},-{\frac {1}{2}}\right)}(1).\\T_{n}^{*}(x)&=T_{n}(2x-1),\\U_{n}^{*}(x)&=U_{n}(2x-1).\end{aligned}}$ Laguerre: ${\begin{aligned}\lim _{\beta \rightarrow \infty }P_{n}^{(\alpha ,\beta )}(1-(2x/\beta ))&=L_{n}^{(\alpha )}(x).\\\lim _{\alpha \rightarrow \infty }P_{n}^{(\alpha ,\beta )}((2x/\alpha )-1)&=(-1)^{n}L_{n}^{(\beta )}(x).\end{aligned}}$ Hermite: $\lim _{\alpha \rightarrow \infty }\alpha ^{-{\frac {1}{2}}n}P_{n}^{(\alpha ,\alpha )}\left(\alpha ^{-{\frac {1}{2}}}x\right)={\frac {H_{n}(x)}{2^{n}n!}}$

### Stochastic process

The Jacobi polynomials appear as the eigenfunctions of the Markov process on $[-1,+1]$ ${\mathcal {L}}=\left(1-x^{2}\right){\frac {\partial ^{2}}{\partial x^{2}}}+(px+q){\frac {\partial }{\partial x}}$ defined up to the time it hits the boundary. For $p=-(\beta +\alpha +2),q=\beta -\alpha$ , we have ${\mathcal {L}}P_{n}^{(\alpha ,\beta )}=-n(n+\alpha +\beta +1)P_{n}^{(\alpha ,\beta )}$ Thus this process is named the **Jacobi process**.

### Heat kernel

Let

- $J^{(\alpha ,\beta )}:=-\left(1-x^{2}\right){\frac {d^{2}}{dx^{2}}}-[\beta -\alpha -(\alpha +\beta +2)x]{\frac {d}{dx}}$
- $T_{t}^{(\alpha ,\beta )}:=e^{-tJ^{(\alpha ,\beta )}}$
- $h_{n}^{(\alpha ,\beta )}=\int _{-1}^{1}\left[P_{n}^{(\alpha ,\beta )}(x)\right]^{2}(1-x)^{\alpha }(1+x)^{\beta }dx={\frac {2^{\alpha +\beta +1}\Gamma (n+\alpha +1)\Gamma (n+\beta +1)}{(2n+\alpha +\beta +1)\Gamma (n+\alpha +\beta +1)\Gamma (n+1)}}$
- $G_{t}^{(\alpha ,\beta )}(x,y)=\sum _{n=0}^{\infty }\exp(-tn(n+\alpha +\beta +1)){\frac {P_{n}^{(\alpha ,\beta )}(x)P_{n}^{(\alpha ,\beta )}(y)}{h_{n}^{(\alpha ,\beta )}}},\quad x,y\in [-1,1],\quad t>0,$
- $d\rho _{(\alpha ,\beta )}(x)=(1-x)^{\alpha }(1+x)^{\beta }dx$

Then, for any $f\in L^{1}\left(d\rho _{(\alpha ,\beta )}\right)$ , $T_{t}^{(\alpha ,\beta )}f(x)=\int _{-1}^{1}G_{t}^{(\alpha ,\beta )}(x,y)f(y)d\varrho _{(\alpha ,\beta )}(y)$ Thus, $G_{t}^{(\alpha ,\beta )}$ is called the **Jacobi heat kernel**.

### Other properties

The discriminant is $\operatorname {Disc} \left(P_{n}^{(\alpha ,\beta )}\right)=2^{-n(n-1)}\prod _{j=1}^{n}j^{j-2n+2}(j+\alpha )^{j-1}(j+\beta )^{j-1}(n+j+\alpha +\beta )^{n-j}$ **Bailey’s formula**: ${\begin{aligned}&\sum _{n=0}^{\infty }{\frac {P_{n}^{(\alpha ,\beta )}(\cos \theta )P_{n}^{(\alpha ,\beta )}(\cos \varphi )}{h_{n}^{(\alpha ,\beta )}}}r^{n}={\frac {\Gamma (\alpha +\beta +2)}{2^{\alpha +\beta +1}\Gamma (\alpha +1)\Gamma (\beta +1)}}{\frac {1-r}{(1+r)^{\alpha +\beta +2}}}\\&\quad \times F_{4}\left({\frac {\alpha +\beta +2}{2}},{\frac {\alpha +\beta +3}{2}};\alpha +1,\beta +1;\left({\frac {2\sin {\frac {\theta }{2}}\sin {\frac {\varphi }{2}}}{r^{1/2}+r^{-1/2}}}\right)^{2},\left({\frac {2\cos {\frac {\theta }{2}}\cos {\frac {\varphi }{2}}}{r^{1/2}+r^{-1/2}}}\right)^{2}\right)\end{aligned}}$ where $|r|<1,\alpha ,\beta >-1$ , and $F_{4}$ is Appel's hypergeometric function of two variables. This is an analog of the Mehler kernel for Hermite polynomials, and the Hardy–Hille formula for Laguerre polynomials.

**Laplace-type integral representation**: ${\begin{aligned}P_{n}^{\left(\alpha ,\beta \right)}\left(1-2t^{2}\right)=&{\frac {(-1)^{n}2^{2n}}{\pi (2n)!}}{\frac {\Gamma (n+\alpha +1)\Gamma (n+\beta +1)}{\Gamma \left(\alpha +{\frac {1}{2}}\right)\Gamma \left(\beta +{\frac {1}{2}}\right)}}.\\&\int _{-1}^{1}\int _{-1}^{1}\left(tu\pm i{\sqrt {1-t^{2}}}v\right)^{2n}\left(1-u^{2}\right)^{\alpha -{\frac {1}{2}}}\left(1-v^{2}\right)^{\beta -{\frac {1}{2}}}dudv.\end{aligned}}$

## Zeroes

If $\alpha ,\beta >-1$ , then $P_{n}^{(\alpha ,\beta )}$ has n real roots. Thus in this section we assume $\alpha ,\beta >-1$ by default. This section is based on.

Define:

- $j_{\alpha ,m}$ are the positive zero of the Bessel function of the first kind $J_{\alpha }$ , ordered such that $0<j_{\alpha ,1}<j_{\alpha ,2}<\cdots$ .
- $\theta _{n,m}=\theta _{n,m}^{(\alpha ,\beta )}$ are the zeroes of $P_{n}^{(\alpha ,\beta )}\left(\cos \theta \right)$ , ordered such that $0<\theta _{n,1}<\theta _{n,2}<\cdots <\theta _{n,n}<\pi$ .
- $\rho =n+{\frac {1}{2}}(\alpha +\beta +1)$
- $\phi _{m}=j_{\alpha ,m}/\rho$

### Inequalities

$\theta _{n,m}$ is strictly monotonically increasing with $\alpha$ and strictly monotonically decreasing with $\beta$ .

If $\alpha =\beta$ , and $m<n/2$ , then $\theta _{n,m}$ is strictly monotonically increasing with $\alpha$ .

When $\alpha ,\beta \in [-1/2,+1/2]$ ,

- $\theta _{n,m}^{(-{\frac {1}{2}},{\frac {1}{2}})}={\frac {(m-{\tfrac {1}{2}})\pi }{n+{\tfrac {1}{2}}}}\leq \theta _{n,m}^{(\alpha ,\beta )}\leq {\frac {m\pi }{n+{\tfrac {1}{2}}}}=\theta _{n,m}^{({\frac {1}{2}},-{\frac {1}{2}})}$
- $\theta _{n,m}^{(-{\frac {1}{2}},-{\frac {1}{2}})}={\frac {(m-{\tfrac {1}{2}})\pi }{n}}\leq \theta _{n,m}^{(\alpha ,\alpha )}\leq {\frac {m\pi }{n+1}}=\theta _{n,m}^{({\frac {1}{2}},{\frac {1}{2}})}$ for $m\leq n/2$
- ${{\frac {\left(m+{\tfrac {1}{2}}(\alpha +\beta -1)\right)\pi }{\rho }}<\theta _{n,m}<{\frac {m\pi }{\rho }}}$ except when $\alpha ^{2}=\beta ^{2}={\tfrac {1}{4}}$
- $\theta _{n,m}^{(\alpha ,\alpha )}>{\frac {\left(m+{\tfrac {1}{2}}\alpha -{\tfrac {1}{4}}\right){\pi }}{n+\alpha +{\tfrac {1}{2}}}}$ for $m\leq n/2$ , except when $\alpha ^{2}={\tfrac {1}{4}}$
- $\displaystyle \theta _{n,m}\displaystyle \leq {\frac {j_{\alpha ,m}}{\left(\rho ^{2}+{\tfrac {1}{12}}\left(1-\alpha ^{2}-3\beta ^{2}\right)\right)^{\frac {1}{2}}}}$
- $\displaystyle \theta _{n,m}\displaystyle \geq {\frac {j_{\alpha ,m}}{\left(\rho ^{2}+{\tfrac {1}{4}}-{\tfrac {1}{2}}(\alpha ^{2}+\beta ^{2})-{\pi }^{-2}(1-4\alpha ^{2})\right)^{\frac {1}{2}}}}$ for $m\leq n/2$

### Asymptotics

Fix $\alpha >-1/2,\beta \geq -1-\alpha$ . Fix $c\in (0,1)$ .

$\theta _{n,m}=\phi _{m}+\left(\left(\alpha ^{2}-{\tfrac {1}{4}}\right){\frac {1-\phi _{m}\cot \phi _{m}}{2\phi _{m}}}-{\tfrac {1}{4}}(\alpha ^{2}-\beta ^{2})\tan \left({\tfrac {1}{2}}\phi _{m}\right)\right){\frac {1}{\rho ^{2}}}+\phi _{m}^{2}O\left({\frac {1}{\rho ^{3}}}\right)$

uniformly for $m=1,2,\dots ,\left\lfloor cn\right\rfloor$ .

### Electrostatics

The zeroes satisfy the **Stieltjes relations**: ${\begin{aligned}\sum _{1\leq j\leq n,i\neq j}{\frac {1}{x_{i}-x_{j}}}&={\frac {1}{2}}\left({\frac {\alpha +1}{1-x_{i}}}-{\frac {\beta +1}{1+x_{i}}}\right)\\\sum _{1\leq j\leq n}{\frac {1}{1-x_{j}}}&={\frac {n(n+\alpha +\beta +1)}{2(\alpha +1)}}\\\sum _{1\leq j\leq n}{\frac {1}{1+x_{j}}}&={\frac {n(n+\alpha +\beta +1)}{2(\beta +1)}}\\\sum _{1\leq j\leq n}x_{j}&={\frac {n(\beta -\alpha )}{2n+\alpha +\beta }}\end{aligned}}$ The first relation can be interpreted physically. Fix an electric particle at +1 with charge ${\frac {1+\alpha }{2}}$ , and another particle at -1 with charge ${\frac {1+\beta }{2}}$ . Then, place n electric particles with charge $+1$ . The first relation states that the zeroes of $P_{n}^{(\alpha ,\beta )}$ are the equilibrium positions of the particles. This equilibrium is stable and unique.

Other relations, such as $\sum _{1\leq j\leq n,i\neq j}{\frac {1}{(x_{i}-x_{j})^{2}}},\sum _{1\leq j\leq n,i\neq j}{\frac {1}{(x_{i}-x_{j})^{3}}}$ , are known in closed form.

As the zeroes specify the polynomial up to scaling, this provides an alternative way to uniquely characterize the Jacobi polynomials.

The electrostatic interpretation allows many relations to be intuitively seen. For example:

- the symmetry relation between $P_{n}^{(\alpha ,\beta )}$ and $P_{n}^{(\beta ,\alpha )}$ ;
- the roots monotonically decrease when $\alpha$ increases;

Since the Stieltjes relation also exists for the Hermite polynomials and the Laguerre polynomials, by taking an appropriate limit of $\alpha ,\beta$ , the limit relations are derived. For example, for the Hermite polynomials, the zeros satisfy $-x_{i}+\sum _{1\leq j\leq n,i\neq j}{\frac {1}{x_{i}-x_{j}}}=0$ Thus, by taking $\alpha =\beta \to \infty$ limit, all the electric particles are forced into an infinitesimal neighborhood of the origin, where the field strength is linear. Then after scaling up the line, we obtain the same electrostatic configuration for the zeroes of Hermite polynomials.

## Asymptotics

### Darboux formula

For x in the interior of $[-1,1]$ , the asymptotics of $P_{n}^{(\alpha ,\beta )}$ for large n is given by the Darboux formula

$P_{n}^{(\alpha ,\beta )}(\cos \theta )=n^{-{\frac {1}{2}}}k(\theta )\cos(N\theta +\gamma )+O\left(n^{-{\frac {3}{2}}}\right),$

where

${\begin{aligned}k(\theta )&=\pi ^{-{\frac {1}{2}}}\sin ^{-\alpha -{\frac {1}{2}}}{\tfrac {\theta }{2}}\cos ^{-\beta -{\frac {1}{2}}}{\tfrac {\theta }{2}},\\N&=n+{\tfrac {1}{2}}(\alpha +\beta +1),\\\gamma &=-{\tfrac {\pi }{2}}\left(\alpha +{\tfrac {1}{2}}\right),\\0<\theta &<\pi \end{aligned}}$

and the " O " term is uniform on the interval $[\varepsilon ,\pi -\varepsilon ]$ for every $\varepsilon >0$ .

For higher orders, define:

- $\mathrm {B}$ is the Euler beta function
- $(\cdot )_{m}$ is the falling factorial.
- ${\displaystyle f_{m}(\theta )=\sum _{\ell =0}^{m}{\frac {C_{m,\ell }(\alpha ,\beta )}{\ell$
- $C_{m,\ell }(\alpha ,\beta )={\left({\tfrac {1}{2}}+\alpha \right)_{\ell }}{\left({\tfrac {1}{2}}-\alpha \right)_{\ell }}{\left({\tfrac {1}{2}}+\beta \right)_{m-\ell }}{\left({\tfrac {1}{2}}-\beta \right)_{m-\ell }}$
- $\theta _{n,m,\ell }={\tfrac {1}{2}}(2n+\alpha +\beta +m+1)\theta -{\tfrac {1}{2}}(\alpha +\ell +{\tfrac {1}{2}})\pi$

Fix real $\alpha ,\beta$ , fix $M=1,2,\dots$ , fix $\delta \in (0,\pi /2)$ . As $n\to \infty$ , $\left(\sin {\tfrac {1}{2}}\theta \right)^{\alpha +{\frac {1}{2}}}\left(\cos {\tfrac {1}{2}}\theta \right)^{\beta +{\frac {1}{2}}}P_{n}^{(\alpha ,\beta )}\left(\cos \theta \right)={\pi }^{-1}2^{2n+\alpha +\beta +1}\mathrm {B} \left(n+\alpha +1,n+\beta +1\right)\left(\sum _{m=0}^{M-1}{\frac {f_{m}(\theta )}{2^{m}{\left(2n+\alpha +\beta +2\right)_{m}}}}+O\left(n^{-M}\right)\right)$ uniformly for all $\theta \in [\delta ,\pi -\delta ]$ .

The $M=1$ case is the above Darboux formula.

### Hilb's type formula

Define:

- $J_{\nu }$ is the Bessel function
- $\rho =n+{\tfrac {1}{2}}(\alpha +\beta +1)$
- $g(\theta )=\left({\tfrac {1}{4}}-\alpha ^{2}\right)\left(\cot \left({\tfrac {1}{2}}\theta \right)-\left({\tfrac {1}{2}}\theta \right)^{-1}\right)-\left({\tfrac {1}{4}}-\beta ^{2}\right)\tan \left({\tfrac {1}{2}}\theta \right)$

Fix real $\alpha ,\beta$ , fix $M=0,1,2,\dots$ . As $n\to \infty$ , we have the **Hilb's type formula**: $(\sin {\tfrac {1}{2}}\theta )^{\alpha +{\frac {1}{2}}}(\cos {\tfrac {1}{2}}\theta )^{\beta +{\frac {1}{2}}}P_{n}^{(\alpha ,\beta )}\left(\cos \theta \right)={\frac {\Gamma \left(n+\alpha +1\right)}{2^{\frac {1}{2}}\rho ^{\alpha }n!}}\left(\theta ^{\frac {1}{2}}J_{\alpha }\left(\rho \theta \right)\sum _{m=0}^{M}{\dfrac {A_{m}(\theta )}{\rho ^{2m}}}+\theta ^{\frac {3}{2}}J_{\alpha +1}\left(\rho \theta \right)\sum _{m=0}^{M-1}{\dfrac {B_{m}(\theta )}{\rho ^{2m+1}}}+\varepsilon _{M}(\rho ,\theta )\right)$ where $A_{m},B_{m}$ are functions of $\theta$ . The first few entries are: ${\begin{aligned}A_{0}(\theta )&=1\\\theta B_{0}(\theta )&={\frac {1}{4}}g(\theta )\\A_{1}(\theta )&={\frac {1}{8}}g^{\prime }(\theta )-{\frac {1+2\alpha }{8}}{\frac {g(\theta )}{\theta }}-{\frac {1}{32}}(g(\theta ))^{2}\end{aligned}}$

For any fixed arbitrary constant $c>0$ , the error term satisfies $\varepsilon _{M}(\rho ,\theta )={\begin{cases}\theta O\left(\rho ^{-2M-(3/2)}\right),&c\rho ^{-1}\leq \theta \leq \pi -\delta ,\\\theta ^{\alpha +(5/2)}O\left(\rho ^{-2M+\alpha }\right),&0\leq \theta \leq c\rho ^{-1},\end{cases}}$

### Mehler–Heine formula

The asymptotics of the Jacobi polynomials near the points $\pm 1$ is given by the Mehler–Heine formula

${\begin{aligned}\lim _{n\to \infty }n^{-\alpha }P_{n}^{(\alpha ,\beta )}\left(\cos \left({\tfrac {z}{n}}\right)\right)&=\left({\tfrac {z}{2}}\right)^{-\alpha }J_{\alpha }(z)\\\lim _{n\to \infty }n^{-\beta }P_{n}^{(\alpha ,\beta )}\left(\cos \left(\pi -{\tfrac {z}{n}}\right)\right)&=\left({\tfrac {z}{2}}\right)^{-\beta }J_{\beta }(z)\end{aligned}}$

where the limits are uniform for z in a bounded domain.

The asymptotics outside $[-1,1]$ is less explicit.

## Applications

### Wigner d-matrix

The expression (**1**) allows the expression of the Wigner d-matrix $d_{m',m}^{j}(\phi )$ (for $0\leq \phi \leq 4\pi$ ) in terms of Jacobi polynomials:

$d_{m'm}^{j}(\phi )=(-1)^{\frac {m-m'-|m-m'|}{2}}\left[{\frac {(j+M)!(j-M)!}{(j+N)!(j-N)!}}\right]^{\frac {1}{2}}\left(\sin {\tfrac {\phi }{2}}\right)^{|m-m'|}\left(\cos {\tfrac {\phi }{2}}\right)^{|m+m'|}P_{j-M}^{(|m-m'|,|m+m'|)}(\cos \phi ),$

where $M=\max(|m|,|m'|),N=\min(|m|,|m'|)$ .
