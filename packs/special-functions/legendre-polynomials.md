---
title: "Legendre polynomials"
source: https://en.wikipedia.org/wiki/Legendre_polynomials
domain: special-functions
license: CC-BY-SA-4.0
tags: special functions, bessel functions, gamma function, error function
fetched: 2026-07-02
---

# Legendre polynomials

In mathematics, **Legendre polynomials**, named after Adrien-Marie Legendre (1782), are a system of complete and orthogonal polynomials with a wide number of mathematical properties and numerous applications. They can be defined in many ways, and the various definitions highlight different aspects as well as suggest generalizations and connections to different mathematical structures and physical and numerical applications.

Closely related to the Legendre polynomials are associated Legendre polynomials, Legendre functions, Legendre functions of the second kind, big q-Legendre polynomials, and associated Legendre functions.

## Definition and representation

### Definition by construction as an orthogonal system

In this approach, the polynomials are defined as an orthogonal system with respect to the weight function $w(x)=1$ over the interval $[-1,1]$ . That is, $P_{n}(x)$ is a polynomial of degree n , such that $\int _{-1}^{1}P_{m}(x)P_{n}(x)\,dx=0\quad {\text{if }}n\neq m.$

With the additional standardization condition $P_{n}(1)=1$ , all the polynomials can be uniquely determined. We then start the construction process: $P_{0}(x)=1$ is the only correctly standardized polynomial of degree 0. $P_{1}(x)$ must be orthogonal to $P_{0}$ , leading to $P_{1}(x)=x$ , and $P_{2}(x)$ is determined by demanding orthogonality to $P_{0}$ and $P_{1}$ , and so on. $P_{n}$ is fixed by demanding orthogonality to all $P_{m}$ with $m<n$ . This gives n conditions, which, along with the standardization $P_{n}(1)=1$ fixes all $n+1$ coefficients in $P_{n}(x)$ . With work, all the coefficients of every polynomial can be systematically determined, leading to the explicit representation in powers of x given below.

This definition of the $P_{n}$ 's is the simplest one. It does not appeal to the theory of differential equations. Second, the completeness of the polynomials follows immediately from the completeness of the powers 1, $x,x^{2},x^{3},\ldots$ . Finally, by defining them via orthogonality with respect to the Lebesgue measure on $[-1,1]$ , it sets up the Legendre polynomials as one of the three classical orthogonal polynomial systems. The other two are the Laguerre polynomials, which are orthogonal over the half line $[0,\infty )$ with the weight $e^{-x}$ , and the Hermite polynomials, orthogonal over the full line $(-\infty ,\infty )$ with weight $e^{-x^{2}}$ .

### Definition via generating function

The Legendre polynomials can also be defined as the coefficients in a formal expansion in powers of t of the generating function

| ${\frac {1}{\sqrt {1-2xt+t^{2}}}}=\sum _{n=0}^{\infty }P_{n}(x)t^{n}\,.$ |   | 2 |
|---|---|---|

The coefficient of $t^{n}$ is a polynomial in x of degree n with $|x|\leq 1$ . Expanding up to $t^{1}$ gives $P_{0}(x)=1\,,\quad P_{1}(x)=x.$ Expansion to higher orders gets increasingly cumbersome, but is possible to do systematically, and again leads to one of the explicit forms given below.

It is possible to obtain the higher $P_{n}$ 's without resorting to direct expansion of the Taylor series, however. Equation **2** is differentiated with respect to t on both sides and rearranged to obtain ${\frac {x-t}{\sqrt {1-2xt+t^{2}}}}=\left(1-2xt+t^{2}\right)\sum _{n=1}^{\infty }nP_{n}(x)t^{n-1}\,.$ Replacing the quotient of the square root with its definition in Eq. **2**, and equating the coefficients of powers of *t* in the resulting expansion gives *Bonnet's recursion formula* $(n+1)P_{n+1}(x)=(2n+1)xP_{n}(x)-nP_{n-1}(x)\,.$ This relation, along with the first two polynomials *P*0 and *P*1, allows all the rest to be generated recursively.

The generating function approach is directly connected to the multipole expansion in electrostatics, as explained below, and is how the polynomials were first defined by Legendre in 1782.

### Definition via differential equation

A third definition is in terms of solutions to **Legendre's differential equation**:

| $(1-x^{2})P_{n}''(x)-2xP_{n}'(x)+n(n+1)P_{n}(x)=0.$ |   | 1 |
|---|---|---|

This differential equation has regular singular points at *x* = ±1 so if a solution is sought using the standard Frobenius or power series method, a series about the origin will only converge for |*x*| < 1 in general. When *n* is an integer, the solution *Pn*(*x*) that is regular at *x* = 1 is also regular at *x* = −1, and the series for this solution terminates (i.e. it is a polynomial). The orthogonality and completeness of these solutions is best seen from the viewpoint of Sturm–Liouville theory. We rewrite the differential equation as an eigenvalue problem, ${\frac {d}{dx}}\left(\left(1-x^{2}\right){\frac {d}{dx}}P(x)\right)=-\lambda P(x)\,,$ with the eigenvalue $\lambda$ in lieu of $n(n+1)$ . This is a Sturm–Liouville equation with $p=1-x^{2},q=0,w=1$ .

If we demand that the solution be regular at $x=\pm 1$ , the differential operator on the left is Hermitian. The eigenvalues are found to be of the form *n*(*n* + 1), with $n=0,1,2,\ldots$ and the eigenfunctions are the $P_{n}(x)$ . The orthogonality and completeness of this set of solutions follows at once from the larger framework of Sturm–Liouville theory.

The differential equation admits another, non-polynomial solution, the Legendre functions of the second kind $Q_{n}$ . A two-parameter generalization of (Eq. **1**) is called Legendre's *general* differential equation, solved by the Associated Legendre polynomials. Legendre functions are solutions of Legendre's differential equation (generalized or not) with *non-integer* parameters.

In physical settings, Legendre's differential equation arises naturally whenever one solves Laplace's equation (and related partial differential equations) by separation of variables in spherical coordinates. From this standpoint, the eigenfunctions of the angular part of the Laplacian operator are the spherical harmonics, of which the Legendre polynomials are (up to a multiplicative constant) the subset that is left invariant by rotations about the polar axis. The polynomials appear as $P_{n}(\cos \theta )$ where $\theta$ is the polar angle. This approach to the Legendre polynomials provides a deep connection to rotational symmetry. Many of their properties which are found laboriously through the methods of analysis — for example the addition theorem — are more easily found using the methods of symmetry and group theory, and acquire profound physical and geometrical meaning.

### Rodrigues' formula and other explicit formulas

An especially compact expression for the Legendre polynomials is given by Rodrigues' formula: $P_{n}(x)={\frac {1}{2^{n}n!}}{\frac {d^{n}}{dx^{n}}}(x^{2}-1)^{n}\,.$

This formula enables derivation of a large number of properties of the $P_{n}$ 's. Among these are explicit representations such as ${\begin{aligned}P_{n}(x)&={\frac {1}{2^{n}}}\sum _{k=0}^{n}{\binom {n}{k}}^{\!2}(x-1)^{n-k}(x+1)^{k},\\[1ex]P_{n}(x)&=\sum _{k=0}^{n}{\binom {n}{k}}{\binom {n+k}{k}}\left({\frac {x-1}{2}}\right)^{\!k},\\[1ex]P_{n}(x)&={\frac {1}{2^{n}}}\sum _{k=0}^{\left\lfloor n/2\right\rfloor }\left(-1\right)^{k}{\binom {n}{k}}{\binom {2n-2k}{n}}x^{n-2k},\\[1ex]P_{n}(x)&=2^{n}\sum _{k=0}^{n}x^{k}{\binom {n}{k}}{\binom {\frac {n+k-1}{2}}{n}},\\[1ex]P_{n}(x)&={\frac {1}{2^{n}}}\sum _{k=\lceil n/2\rceil }^{n}{\frac {(-1)^{k+n}(2k)!}{(2k-n)!(n-k)!k!}}x^{2k-n},\\[1ex]P_{n}(x)&={\begin{cases}\displaystyle {\frac {1}{\pi }}\int _{0}^{\pi }{\left(x+{\sqrt {x^{2}-1}}\cdot \cos(t)\right)}^{n}\,dt&{\text{if }}|x|>1,\\x^{n}&{\text{if }}|x|=1,\\\displaystyle {\frac {2}{\pi }}\cdot x^{n}\cdot |x|\cdot \int _{|x|}^{1}{\frac {t^{-n-1}}{\sqrt {t^{2}-x^{2}}}}\cdot {\frac {\cos \left(n\cdot \arccos(t)\right)}{\sin \left(\arccos(t)\right)}}\,dt&{\text{if }}0<|x|<1,\\\displaystyle (-1)^{n/2}\cdot 2^{-n}\cdot {\binom {n}{n/2}}&{\text{if }}x=0{\text{ and }}n{\text{ even}},\\0&{\text{if }}x=0{\text{ and }}n{\text{ odd}}.\end{cases}}\end{aligned}}$

Expressing the polynomial as a power series, ${\textstyle P_{n}(x)=\sum a_{n,k}x^{k}}$ , the coefficients of powers of x can also be calculated using the recurrences

$a_{n,k}=-{\frac {(n-k+2)(n+k-1)}{k(k-1)}}a_{n,k-2}.$ or

$a_{n,k}=-{\frac {n+k-1}{n-k}}a_{n-2,k}.$

The Legendre polynomial is determined by the values used for the two constants ${\textstyle a_{n,0}}$ and ${\textstyle a_{n,1}}$ , where ${\textstyle a_{n,0}=0}$ if n is odd and ${\textstyle a_{n,1}=0}$ if n is even.

In the fourth representation, $\lfloor n/2\rfloor$ stands for the largest integer less than or equal to $n/2$ . The fifth representation, which is also immediate from the recursion formula, expresses the Legendre polynomials by simple monomials and involves the generalized form of the binomial coefficient.

The reversal of the representation as a power series is

$x^{m}=\sum _{s=0}^{\lfloor m/2\rfloor }(2m-4s+1){\frac {(2s+2)(2s+4)\cdots 2\lfloor m/2\rfloor }{(2m-2s+1)(2m-2s-1)(2m-2s-3)\cdots (1+2\lfloor (m+1)/2\rfloor )}}P_{m-2s}(x).$

for $m=0,1,2,\ldots$ , where an empty product in the numerator (last factor less than the first factor) evaluates to 1.

The first few Legendre polynomials are:

| n | $P_{n}(x)$ |
|---|---|
| 0 | ${\textstyle 1}$ |
| 1 | ${\textstyle x}$ |
| 2 | ${\textstyle {\tfrac {1}{2}}\left(3x^{2}-1\right)}$ |
| 3 | ${\textstyle {\tfrac {1}{2}}\left(5x^{3}-3x\right)}$ |
| 4 | ${\textstyle {\tfrac {1}{8}}\left(35x^{4}-30x^{2}+3\right)}$ |
| 5 | ${\textstyle {\tfrac {1}{8}}\left(63x^{5}-70x^{3}+15x\right)}$ |
| 6 | ${\textstyle {\tfrac {1}{16}}\left(231x^{6}-315x^{4}+105x^{2}-5\right)}$ |
| 7 | ${\textstyle {\tfrac {1}{16}}\left(429x^{7}-693x^{5}+315x^{3}-35x\right)}$ |
| 8 | ${\textstyle {\tfrac {1}{128}}\left(6435x^{8}-12012x^{6}+6930x^{4}-1260x^{2}+35\right)}$ |
| 9 | ${\textstyle {\tfrac {1}{128}}\left(12155x^{9}-25740x^{7}+18018x^{5}-4620x^{3}+315x\right)}$ |
| 10 | ${\textstyle {\tfrac {1}{256}}\left(46189x^{10}-109395x^{8}+90090x^{6}-30030x^{4}+3465x^{2}-63\right)}$ |

The graphs of these polynomials (up to *n* = 5) are shown below:

## Main properties

### Orthogonality and normalization

The standardization $P_{n}(1)=1$ fixes the normalization of the Legendre polynomials (with respect to the *L*2 norm on the interval −1 ≤ *x* ≤ 1). Rodrigues' formula may be employed to give the normalization integral $\int _{-1}^{1}P_{n}(x)^{2}\,dx={\frac {2}{2n+1}}.$ The statements of normalization and orthogonality can then be compactly written in a single equation: $\int _{-1}^{1}P_{m}(x)P_{n}(x)\,dx={\frac {2}{2n+1}}\delta _{mn},$ where *δmn* denotes the Kronecker delta.

### Completeness

That the polynomials are complete means the following. Given any piecewise continuous function $f(x)$ with finitely many discontinuities in the interval [−1, 1], the sequence of sums $f_{n}(x)=\sum _{\ell =0}^{n}a_{\ell }P_{\ell }(x)$ converges in the mean to $f(x)$ as $n\to \infty$ , provided we take $a_{\ell }={\frac {2\ell +1}{2}}\int _{-1}^{1}f(x)P_{\ell }(x)\,dx.$

This completeness property underlies all the expansions discussed in this article, and is often stated in the form $\sum _{\ell =0}^{\infty }{\frac {2\ell +1}{2}}P_{\ell }(x)P_{\ell }(y)=\delta (x-y),$ with −1 ≤ *x* ≤ 1 and −1 ≤ *y* ≤ 1.

## Applications

### Expanding an inverse distance potential

The Legendre polynomials were first introduced in 1782 by Adrien-Marie Legendre as the coefficients in the expansion of the Newtonian potential ${\frac {1}{\left|\mathbf {x} -\mathbf {x} '\right|}}={\frac {1}{\sqrt {r^{2}+{r'}^{2}-2r{r'}\cos \gamma }}}=\sum _{\ell =0}^{\infty }{\frac {{r'}^{\ell }}{r^{\ell +1}}}P_{\ell }(\cos \gamma ),$ where *r* and *r*′ are the lengths of the vectors **x** and **x**′ respectively and *γ* is the angle between those two vectors. The series converges when *r* > *r*′. The expression gives the gravitational potential associated to a point mass or the Coulomb potential associated to a point charge. The expansion using Legendre polynomials might be useful, for instance, when integrating this expression over a continuous mass or charge distribution.

Legendre polynomials occur in the solution of Laplace's equation of the static potential, ∇2 Φ(**x**) = 0, in a charge-free region of space, using the method of separation of variables, where the boundary conditions have axial symmetry (no dependence on an azimuthal angle). Where **ẑ** is the axis of symmetry and *θ* is the angle between the position of the observer and the **ẑ** axis (the zenith angle), the solution for the potential will be $\Phi (r,\theta )=\sum _{\ell =0}^{\infty }\left(A_{\ell }r^{\ell }+B_{\ell }r^{-(\ell +1)}\right)P_{\ell }(\cos \theta )\,.$

*Al* and *Bl* are to be determined according to the boundary condition of each problem.

They also appear when solving the Schrödinger equation in three dimensions for a central force.

### In multipole expansions

Legendre polynomials are also useful in expanding functions of the form (this is the same as before, written a little differently): ${\frac {1}{\sqrt {1+\eta ^{2}-2\eta x}}}=\sum _{k=0}^{\infty }\eta ^{k}P_{k}(x),$ which arise naturally in multipole expansions. The left-hand side of the equation is the generating function for the Legendre polynomials.

As an example, the electric potential Φ(*r*,*θ*) (in spherical coordinates) due to a point charge located on the *z*-axis at *z* = *a* (see diagram right) varies as $\Phi (r,\theta )\propto {\frac {1}{R}}={\frac {1}{\sqrt {r^{2}+a^{2}-2ar\cos \theta }}}.$

If the radius *r* of the observation point P is greater than *a*, the potential may be expanded in the Legendre polynomials $\Phi (r,\theta )\propto {\frac {1}{r}}\sum _{k=0}^{\infty }\left({\frac {a}{r}}\right)^{k}P_{k}(\cos \theta ),$ where we have defined *η* = ⁠*a*/*r*⁠ < 1 and *x* = cos *θ*. This expansion is used to develop the normal multipole expansion.

Conversely, if the radius *r* of the observation point P is smaller than *a*, the potential may still be expanded in the Legendre polynomials as above, but with *a* and *r* exchanged. This expansion is the basis of interior multipole expansion.

### In trigonometry

The trigonometric functions cos *nθ*, also denoted as the Chebyshev polynomials *Tn*(cos *θ*) ≡ cos *nθ*, can also be multipole expanded by the Legendre polynomials *Pn*(cos *θ*). The first several orders are as follows: ${\begin{alignedat}{2}T_{0}(\cos \theta )&=1&&=P_{0}(\cos \theta ),\\[4pt]T_{1}(\cos \theta )&=\cos \theta &&=P_{1}(\cos \theta ),\\[4pt]T_{2}(\cos \theta )&=\cos 2\theta &&={\tfrac {1}{3}}{\bigl (}4P_{2}(\cos \theta )-P_{0}(\cos \theta ){\bigr )},\\[4pt]T_{3}(\cos \theta )&=\cos 3\theta &&={\tfrac {1}{5}}{\bigl (}8P_{3}(\cos \theta )-3P_{1}(\cos \theta ){\bigr )},\\[4pt]T_{4}(\cos \theta )&=\cos 4\theta &&={\tfrac {1}{105}}{\bigl (}192P_{4}(\cos \theta )-80P_{2}(\cos \theta )-7P_{0}(\cos \theta ){\bigr )},\\[4pt]T_{5}(\cos \theta )&=\cos 5\theta &&={\tfrac {1}{63}}{\bigl (}128P_{5}(\cos \theta )-56P_{3}(\cos \theta )-9P_{1}(\cos \theta ){\bigr )},\\[4pt]T_{6}(\cos \theta )&=\cos 6\theta &&={\tfrac {1}{1155}}{\bigl (}2560P_{6}(\cos \theta )-1152P_{4}(\cos \theta )-220P_{2}(\cos \theta )-33P_{0}(\cos \theta ){\bigr )}.\end{alignedat}}$

This can be summarized for $n>0$ as

$T_{n}(x)=2^{2n-n'}{\hat {n}}!\sum _{t=0}^{\hat {n}}(n-2t+1/2){\frac {(n-t-1)!}{2^{2t}t!(n-1)!}}\times {\frac {(-1)\cdot 1\cdot 3\cdots (2t-3)}{(1+2n')(3+2n')\cdots (2n-2t+1)}}P_{n-2t}(x).$

where ${\hat {n}}\equiv \lfloor n/2\rfloor$ , $n'\equiv \lfloor (n+1)/2\rfloor$ , and where the products with the steps of two in the numerator and denominator are to be interpreted as 1 if they are empty, i.e., if the last factor is smaller than the first factor.

Another property is the expression for sin (*n* + 1)*θ*, which is ${\frac {\sin(n+1)\theta }{\sin \theta }}=\sum _{\ell =0}^{n}P_{\ell }(\cos \theta )P_{n-\ell }(\cos \theta ).$

### In recurrent neural networks

A recurrent neural network that contains a *d*-dimensional memory vector, $\mathbf {m} \in \mathbb {R} ^{d}$ , can be optimized such that its neural activities obey the linear time-invariant system given by the following state-space representation: $\theta {\dot {\mathbf {m} }}(t)=A\mathbf {m} (t)+Bu(t),$ ${\begin{aligned}A&=\left[a\right]_{ij}\in \mathbb {R} ^{d\times d}{\text{,}}\quad &&a_{ij}=\left(2i+1\right){\begin{cases}-1&i<j\\(-1)^{i-j+1}&i\geq j\end{cases}},\\B&=\left[b\right]_{i}\in \mathbb {R} ^{d\times 1}{\text{,}}\quad &&b_{i}=(2i+1)(-1)^{i}.\end{aligned}}$

In this case, the sliding window of u across the past $\theta$ units of time is best approximated by a linear combination of the first d shifted Legendre polynomials, weighted together by the elements of $\mathbf {m}$ at time t : $u(t-\theta ')\approx \sum _{\ell =0}^{d-1}{\widetilde {P}}_{\ell }\left({\frac {\theta '}{\theta }}\right)\,m_{\ell }(t),\quad 0\leq \theta '\leq \theta .$

When combined with deep learning methods, these networks can be trained to outperform long short-term memory units and related architectures, while using fewer computational resources.

## Additional properties

Legendre polynomials have definite parity. That is, they are even or odd, according to $P_{n}(-x)=(-1)^{n}P_{n}(x)\,.$

Another useful property is $\int _{-1}^{1}P_{n}(x)\,dx=0,\quad n\geq 1,$ which follows from considering the orthogonality relation with $P_{0}(x)=1$ . It is convenient when a Legendre series ${\textstyle \sum _{i}a_{i}P_{i}}$ is used to approximate a function or experimental data: the *average* of the series over the interval [−1, 1] is simply given by the leading expansion coefficient $a_{0}$ .

The antiderivative is

$\int P_{n}(x)\,dx={\frac {1}{2n+1}}[P_{n+1}(x)-P_{n-1}(x)],\quad n\geq 1.$

Since the differential equation and the orthogonality property are independent of scaling, the Legendre polynomials' definitions are "standardized" (sometimes called "normalization", but the actual norm is not 1) by being scaled so that $P_{n}(1)=1\,.$

The derivative at the end point is given by $P_{n}'(1)={\frac {n(n+1)}{2}}\,.$

The product expansion is

$P_{m}(x)P_{n}(x)=\sum _{r=0}^{\min(m,n)}{\frac {A_{r}A_{m-r}A_{n-r}}{A_{m+n-r}}}{\frac {2m+2n-4r+1}{2m+2n-2r+1}}P_{m+n-2r}(x)$

where $A_{r}\equiv (2r-1)!!/r!$ .

The Askey–Gasper inequality for Legendre polynomials reads $\sum _{j=0}^{n}P_{j}(x)\geq 0\quad {\text{for }}\quad x\geq -1\,.$

The Legendre polynomials of a scalar product of unit vectors can be expanded with spherical harmonics using $P_{\ell }\left(r\cdot r'\right)={\frac {4\pi }{2\ell +1}}\sum _{m=-\ell }^{\ell }Y_{\ell m}(\theta ,\varphi )Y_{\ell m}^{*}(\theta ',\varphi ')\,,$ where the unit vectors *r* and *r*′ have spherical coordinates (*θ*, *φ*) and (*θ*′, *φ*′), respectively.

The product of two Legendre polynomials $\sum _{p=0}^{\infty }t^{p}P_{p}(\cos \theta _{1})P_{p}(\cos \theta _{2})={\frac {2}{\pi }}{\frac {\mathbf {K} \left(2{\sqrt {\frac {t\sin \theta _{1}\sin \theta _{2}}{t^{2}-2t\cos \left(\theta _{1}+\theta _{2}\right)+1}}}\right)}{\sqrt {t^{2}-2t\cos \left(\theta _{1}+\theta _{2}\right)+1}}}\,,$ where $K(\cdot )$ is the complete elliptic integral of the first kind.

The formulas of Dirichlet-Mehler: $P_{n}(\cos \theta )={\frac {2}{\pi }}\int _{0}^{\theta }{\frac {\cos \left(n+{\frac {1}{2}}\right)\phi }{(2\cos \phi -2\cos \theta )^{\frac {1}{2}}}}d\phi ={\frac {2}{\pi }}\int _{\theta }^{\pi }{\frac {\sin \left(n+{\frac {1}{2}}\right)\phi }{(2\cos \theta -2\cos \phi )^{\frac {1}{2}}}}d\phi$ which has generalizations for associated Legendre polynomials.

The Fourier-Legendre series: $e^{itx}=\sum _{n=0}^{\infty }(2n+1)i^{n}{\sqrt {\frac {\pi }{2t}}}J_{n+{\frac {1}{2}}}(t)P_{n}(x)$ where J is the Bessel function of the first kind.

### Recurrence relations

As discussed above, the Legendre polynomials obey the three-term recurrence relation known as Bonnet's recursion formula given by $(n+1)P_{n+1}(x)=(2n+1)xP_{n}(x)-nP_{n-1}(x)$ and ${\frac {x^{2}-1}{n}}{\frac {d}{dx}}P_{n}(x)=xP_{n}(x)-P_{n-1}(x)$ or, with the alternative expression, which also holds at the endpoints ${\frac {d}{dx}}P_{n+1}(x)=(n+1)P_{n}(x)+x{\frac {d}{dx}}P_{n}(x)\,.$

Useful for the integration of Legendre polynomials is $(2n+1)P_{n}(x)={\frac {d}{dx}}{\bigl (}P_{n+1}(x)-P_{n-1}(x){\bigr )}\,.$

From the above one can see also that ${\frac {d}{dx}}P_{n+1}(x)=(2n+1)P_{n}(x)+{\bigl (}2(n-2)+1{\bigr )}P_{n-2}(x)+{\bigl (}2(n-4)+1{\bigr )}P_{n-4}(x)+\cdots$ or equivalently ${\frac {d}{dx}}P_{n+1}(x)={\frac {2P_{n}(x)}{\left\|P_{n}\right\|^{2}}}+{\frac {2P_{n-2}(x)}{\left\|P_{n-2}\right\|^{2}}}+\cdots$ where ‖*Pn*‖ is the norm over the interval −1 ≤ *x* ≤ 1 $\|P_{n}\|={\sqrt {\int _{-1}^{1}{\bigl (}P_{n}(x){\bigr )}^{2}\,dx}}={\sqrt {\frac {2}{2n+1}}}\,.$ More generally, all orders of derivatives are expressible as a sum of Legendre polynomials: ${\begin{aligned}&{\begin{aligned}&{\frac {d^{q}}{dx^{q}}}P_{q+2j}(x)={\frac {2^{q-1}}{(q-1)!}}\sum _{i=0}^{j}(4i+1){\frac {(q+j-i-1)!\Gamma \left(q+j+i+{\frac {1}{2}}\right)}{(j-i)!\Gamma (j+i+3/2)}}P_{2i}(x)\\&\quad ={\frac {1}{2^{q-2}(q-1)!}}\sum _{i=0}^{j}(4i+1){\frac {(q+j-i-1)!(2q+2j+2i-1)!}{(j-i)!(2j+2i+2)!}}{\frac {(j+i+1)!}{(q+j+i-1)!}}P_{2i}(x)\end{aligned}}\\&{\begin{aligned}&{\frac {d^{q}}{dx^{q}}}P_{q+2j+1}(x)={\frac {2^{q-1}}{(q-1)!}}\sum _{i=0}^{j}(4i+3){\frac {(q+j-i-1)!\Gamma (q+j+i+3/2)}{(j-i)!\Gamma (j+i+5/2)}}P_{2i+1}(x)\\&\quad ={\frac {1}{2^{q-2}(q-1)!}}\sum _{i=0}^{j}(4i+3){\frac {(q+j-i-1)!(2q+2j+2i+1)!}{(j-i)!(2j+2i+4)!}}{\frac {(j+i+2)!}{(q+j+i)!}}P_{2i+1}(x)\end{aligned}}\end{aligned}}$

### Asymptotics

Asymptotically, for $\ell \to \infty$ , the Legendre polynomials can be written as the **Hilb's formula**: ${\begin{aligned}P_{\ell }(\cos \theta )&={\sqrt {\frac {\theta }{\sin \left(\theta \right)}}}\left\{J_{0}{\left[\left(\ell +{\tfrac {1}{2}}\right)\theta \right]}-{\frac {\left({\frac {1}{\theta }}-\cot \theta \right)}{8(\ell +{\frac {1}{2}})}}J_{1}{\left[\left(\ell +{\tfrac {1}{2}}\right)\theta \right]}\right\}+{\mathcal {O}}\left(\ell ^{-2}\right)\\[1ex]&={\sqrt {\frac {2}{\pi \ell \sin \left(\theta \right)}}}\cos \left[\left(\ell +{\tfrac {1}{2}}\right)\theta -{\tfrac {\pi }{4}}\right]+{\mathcal {O}}\left(\ell ^{-3/2}\right),\quad \theta \in (0,\pi ),\end{aligned}}$ and for arguments of magnitude greater than 1 ${\begin{aligned}P_{\ell }\left(\cosh \xi \right)&={\sqrt {\frac {\xi }{\sinh \xi }}}I_{0}\left(\left(\ell +{\frac {1}{2}}\right)\xi \right)\left(1+{\mathcal {O}}\left(\ell ^{-1}\right)\right)\,,\\P_{\ell }\left({\frac {1}{\sqrt {1-e^{2}}}}\right)&={\frac {1}{\sqrt {2\pi \ell e}}}{\frac {(1+e)^{\frac {\ell +1}{2}}}{(1-e)^{\frac {\ell }{2}}}}+{\mathcal {O}}\left(\ell ^{-1}\right)\end{aligned}}$ where *J*0, *J*1, and *I*0 are Bessel functions.

### Zeros

All n zeros of $P_{n}(x)$ are real, distinct from each other, and lie in the interval $(-1,1)$ . Furthermore, if we regard them as dividing the interval $[-1,1]$ into $n+1$ subintervals, each subinterval will contain exactly one zero of $P_{n+1}$ . This is known as the interlacing property. Because of the parity property it is evident that if $x_{k}$ is a zero of $P_{n}(x)$ , so is $-x_{k}$ . These zeros play an important role in numerical integration based on Gaussian quadrature. The specific quadrature based on the $P_{n}$ 's is known as Gauss-Legendre quadrature.

The zeros of $P_{n}(\cos \theta )$ are distributed nearly uniformly over the range of $\theta \in (0,\pi )$ , in the sense that there is one zero $\theta \in \left({\frac {\pi (k+1/2)}{n+1/2}},{\frac {\pi (k+1)}{n+1/2}}\right)$ per $k=0,1,\dots ,n-1$ . This can be proved by looking at the first formula of Dirichlet-Mehler.

From this property and the facts that $P_{n}(\pm 1)\neq 0$ , it follows that $P_{n}(x)$ has $n-1$ local minima and maxima in $(-1,1)$ . Equivalently, $dP_{n}(x)/dx$ has $n-1$ zeros in $(-1,1)$ .

### Pointwise evaluations

The parity and normalization implicate the values at the boundaries $x=\pm 1$ to be $P_{n}(1)=1\,,\quad P_{n}(-1)=(-1)^{n}$ At the origin $x=0$ one can show that the values are given by $P_{2n}(0)={\frac {(-1)^{n}}{4^{n}}}{\binom {2n}{n}}={\frac {(-1)^{n}}{2^{2n}}}{\frac {(2n)!}{\left(n!\right)^{2}}}=(-1)^{n}{\frac {(2n-1)!!}{(2n)!!}}$ $P_{2n+1}(0)=0$

## Variants with transformed argument

### Shifted Legendre polynomials

The **shifted Legendre polynomials** are defined as ${\widetilde {P}}_{n}(x)=P_{n}(2x-1)\,.$ Here the "shifting" function *x* ↦ 2*x* − 1 is an affine transformation that bijectively maps the interval [0, 1] to the interval [−1, 1], implying that the polynomials *P̃n*(*x*) are orthogonal on [0, 1]: $\int _{0}^{1}{\widetilde {P}}_{m}(x){\widetilde {P}}_{n}(x)\,dx={\frac {1}{2n+1}}\delta _{mn}\,.$

An explicit expression for the shifted Legendre polynomials is given by ${\widetilde {P}}_{n}(x)=(-1)^{n}\sum _{k=0}^{n}{\binom {n}{k}}{\binom {n+k}{k}}(-x)^{k}\,.$

The analogue of Rodrigues' formula for the shifted Legendre polynomials is ${\widetilde {P}}_{n}(x)={\frac {1}{n!}}{\frac {d^{n}}{dx^{n}}}\left(x^{2}-x\right)^{n}\,.$

The first few shifted Legendre polynomials are:

| n | ${\widetilde {P}}_{n}(x)$ |
|---|---|
| 0 | 1 |
| 1 | $2x-1$ |
| 2 | $6x^{2}-6x+1$ |
| 3 | $20x^{3}-30x^{2}+12x-1$ |
| 4 | $70x^{4}-140x^{3}+90x^{2}-20x+1$ |
| 5 | $252x^{5}-630x^{4}+560x^{3}-210x^{2}+30x-1$ |

### Legendre rational functions

The Legendre rational functions are a sequence of orthogonal functions on [0, ∞). They are obtained by composing the Cayley transform with Legendre polynomials.

A rational Legendre function of degree *n* is defined as: $R_{n}(x)={\frac {\sqrt {2}}{x+1}}\,P_{n}\left({\frac {x-1}{x+1}}\right)\,.$

They are eigenfunctions of the singular Sturm–Liouville problem: $\left(x+1\right){\frac {d}{dx}}\left(x{\frac {d}{dx}}\left[\left(x+1\right)v(x)\right]\right)+\lambda v(x)=0$ with eigenvalues $\lambda _{n}=n(n+1)\,.$
