---
title: "Gamma function (part 1/2)"
source: https://en.wikipedia.org/wiki/Gamma_function
domain: gamma-beta-functions
license: CC-BY-SA-4.0
tags: gamma function, beta function, digamma function, incomplete gamma function
fetched: 2026-07-02
part: 1/2
---

# Gamma function

In mathematics, the **gamma function** (represented by ⁠ $\Gamma$ ⁠, capital Greek letter gamma) is the most common extension of the factorial function to complex numbers. First studied by Daniel Bernoulli, the gamma function $\Gamma (z)$ is defined for all complex numbers z except non-positive integers, and $\Gamma (n)=(n-1)!$ for every positive integer ⁠ n ⁠. The gamma function can be defined via a convergent improper integral for complex numbers with positive real part: $\Gamma (z)=\int _{0}^{\infty }t^{z-1}e^{-t}\,dt,\ \qquad \Re (z)>0.$ The gamma function then is defined in the complex plane as the analytic continuation of this integral function: it is a meromorphic function which is holomorphic except at zero and the negative integers, where it has simple poles.

Since the gamma function has no zeros, its reciprocal ${\frac {1}{\Gamma }}$ is an entire function. In fact, the gamma function corresponds to the Mellin transform of the exponential decay: $\Gamma (z)={\mathcal {M}}\{e^{-x}\}(z)\,.$

Other extensions of the factorial function do exist, but the gamma function is the most popular and useful. It appears as a factor in various probability-distribution functions and other formulas in the fields of probability, statistics, analytic number theory, and combinatorics.


## Motivation

The gamma function can be seen as a solution to the interpolation problem of finding a smooth curve $y=f(x)$ that connects the points of the factorial sequence: $(x,y)=(n,n!)$ for all positive integer values of ⁠ n ⁠. The simple formula for the factorial, $x!=1\cdot 2\cdot 3\cdots x$ is only valid when x is a positive integer, and no elementary function has this property, but a good solution is the gamma function ⁠ $f(x)=\Gamma (x+1)$ ⁠.

The gamma function is not only smooth but analytic (except at the non-positive integers), and it can be defined in several explicit ways. However, it is not the only analytic function that extends the factorial, as one may add any analytic function that is zero on the positive integers, such as $k\sin(m\pi x)$ for an integer ⁠ m ⁠. Such a function is known as a pseudogamma function, the most famous being the Hadamard function.

A more restrictive requirement is the functional equation that interpolates the shifted factorial ⁠ $f(n)=(n-1)!$ ⁠: $f(x+1)=xf(x)\ {\text{ for all }}x>0,\qquad f(1)=1.$

But this still does not give a unique solution, since it allows for multiplication by any periodic function $g(x)$ with $g(x)=g(x+1)$ and ⁠ $g(0)=1$ ⁠, such as ⁠ $g(x)=e^{k\sin(m\pi x)}$ ⁠.

One way to resolve the ambiguity is the Bohr–Mollerup theorem, which shows that $f(x)=\Gamma (x)$ is the unique interpolating function for the factorial, defined over the positive reals, which is logarithmically convex, meaning that $y=\log f(x)$ is convex.


## Definition

### Main definition

The notation $\Gamma (z)$ is due to Legendre. If the real part of the complex number z is strictly positive (⁠ $\Re (z)>0$ ⁠), then the integral $\Gamma (z)=\int _{0}^{\infty }t^{z-1}e^{-t}\,dt$ converges absolutely, and is known as the **Euler integral of the second kind**. (Euler's integral of the first kind is the beta function.)

The value $\Gamma (1)$ can be calculated as ${\begin{aligned}\Gamma (1)&=\int _{0}^{\infty }t^{1-1}e^{-t}\,dt\\[6pt]&=\int _{0}^{\infty }e^{-t}\,dt=1.\end{aligned}}$

Integrating by parts, one sees that ${\begin{aligned}\Gamma (z+1)&=\int _{0}^{\infty }t^{z}e^{-t}\,dt\\[6pt]&={\Bigl [}-t^{z}e^{-t}{\Bigr ]}_{0}^{\infty }+\int _{0}^{\infty }z\,t^{z-1}e^{-t}\,dt.\end{aligned}}$ Recognizing that $-t^{z}e^{-t}\to 0$ as ⁠ $t\to 0$ ⁠ (so long as ⁠ $\Re (z)>0$ ⁠) and as ⁠ $t\to \infty$ ⁠, ${\begin{aligned}\Gamma (z+1)&=z\int _{0}^{\infty }t^{z-1}e^{-t}\,dt\\[6pt]&=z\,\Gamma (z).\end{aligned}}$

Thus we have shown that $\Gamma (n)=(n-1)!$ for any positive integer n by induction.

The identity ${\textstyle z\Gamma (z)=\Gamma (z+1)}$ can be used (or, yielding the same result, analytic continuation can be used) to uniquely extend the integral formulation for $\Gamma (z)$ to a meromorphic function defined for all complex numbers ⁠ z ⁠, except integers less than or equal to zero. It is this extended version that is commonly referred to as the gamma function.

### Alternative definitions

There are many equivalent definitions.

#### Euler's definition as an infinite product

For a fixed integer ⁠ m ⁠, as the integer n increases, we have that $\lim _{n\to \infty }{\frac {n!\,\left(n+1\right)^{m}}{(n+m)!}}=1\,.$

If m is not an integer then this equation is meaningless since, in this section, the factorial of a non-integer has not been defined yet. However, in order to define the Gamma function for non-integers, let us assume that this equation continues to hold when m is replaced by an arbitrary complex number ⁠ z ⁠:

$\lim _{n\to \infty }{\frac {n!\,\left(n+1\right)^{z}}{(n+z)!}}=1\,.$ Multiplying both sides by $(z-1)!$ gives ${\begin{aligned}(z-1)!&={\frac {1}{z}}\lim _{n\to \infty }n!{\frac {z!}{(n+z)!}}(n+1)^{z}\\[6pt]&={\frac {1}{z}}\lim _{n\to \infty }(1\cdot 2\cdots n){\frac {1}{(1+z)\cdots (n+z)}}\left({\frac {2}{1}}\cdot {\frac {3}{2}}\cdots {\frac {n+1}{n}}\right)^{z}\\[6pt]&={\frac {1}{z}}\prod _{n=1}^{\infty }\left[{\frac {1}{1+{\frac {z}{n}}}}\left(1+{\frac {1}{n}}\right)^{z}\right].\end{aligned}}$ This infinite product, which is due to Euler, converges for all complex numbers z except the non-positive integers, which fail because of a division by zero. In fact, the above assumption produces a unique definition of $\Gamma (z)$ as ⁠ $(z-1)!$ ⁠.

Intuitively, this formula indicates that $\Gamma (z)$ is approximately the result of computing $\Gamma (n+1)=n!$ for some large integer ⁠ n ⁠, multiplying by $(n+1)^{z}$ to approximate ⁠ $\Gamma (n+z+1)$ ⁠, and then using the relationship $\Gamma (x+1)=x\Gamma (x)$ backwards $n+1$ times to get an approximation for ⁠ $\Gamma (z)$ ⁠, and furthermore that this approximation becomes exact as n increases to infinity.

The infinite product for the reciprocal ${\frac {1}{\Gamma (z)}}=z\prod _{n=1}^{\infty }\left[\left(1+{\frac {z}{n}}\right)/{\left(1+{\frac {1}{n}}\right)^{z}}\right]$ is an entire function, converging for every complex number ⁠ z ⁠.

#### Weierstrass's definition

The definition for the gamma function due to Weierstrass is also valid for all complex numbers  z except non-positive integers: $\Gamma (z)={\frac {e^{-\gamma z}}{z}}\prod _{n=1}^{\infty }\left(1+{\frac {z}{n}}\right)^{-1}e^{z/n},$ where $\gamma \approx 0.577216$ is the Euler–Mascheroni constant. This is the Hadamard product of $\textstyle {\frac {1}{\Gamma (z)}}$ in a rewritten form.

| Proof of equivalence of the three definitions |
|---|
| **Equivalence of the integral definition and Weierstrass definition** By the integral definition, the relation $\Gamma (z+1)=z\Gamma (z)$ and Hadamard factorization theorem, ${\frac {1}{\Gamma (z)}}=ze^{c_{1}z+c_{2}}\prod _{n=1}^{\infty }e^{-{\frac {z}{n}}}\left(1+{\frac {z}{n}}\right)$ for some constants ⁠ $c_{1}$ ⁠, ⁠ $c_{2}$ ⁠ since $1/\Gamma$ is an entire function of order ⁠ 1 ⁠. Since $z\Gamma (z)\to 1$ as ⁠ $z\to 0$ ⁠, $c_{2}=0$ (or an integer multiple of ⁠ $2\pi i$ ⁠) and since ⁠ $\Gamma (1)=1$ ⁠, ${\begin{aligned}e^{-c_{1}}&=\prod _{n=1}^{\infty }e^{-{\frac {1}{n}}}\left(1+{\frac {1}{n}}\right)\\&=\exp \left(\lim _{N\to \infty }\sum _{n=1}^{N}\left(\log \left(1+{\frac {1}{n}}\right)-{\frac {1}{n}}\right)\right)\\&=\exp \left(\lim _{N\to \infty }\left(\log(N+1)-\sum _{n=1}^{N}{\frac {1}{n}}\right)\right).\end{aligned}}$ where $c_{1}=\gamma +2\pi ik$ for some integer ⁠ k ⁠. Since $\Gamma (z)\in \mathbb {R}$ for ⁠ $z\in \mathbb {R} \setminus \mathbb {Z} _{0}^{-}$ ⁠, we have $k=0$ and ${\frac {1}{\Gamma (z)}}=ze^{\gamma z}\prod _{n=1}^{\infty }e^{-{\frac {z}{n}}}\left(1+{\frac {z}{n}}\right)$ **Equivalence of the Weierstrass definition and Euler definition** ${\begin{aligned}\Gamma (z)&={\frac {e^{-\gamma z}}{z}}\prod _{n=1}^{\infty }\left(1+{\frac {z}{n}}\right)^{-1}e^{z/n}\\&={\frac {1}{z}}\lim _{n\to \infty }e^{z\left(\log(n+1)-1-{\frac {1}{2}}-{\frac {1}{3}}-\cdots -{\frac {1}{n}}\right)}{\frac {e^{z\left(1+{\frac {1}{2}}+{\frac {1}{3}}+\cdots +{\frac {1}{n}}\right)}}{\left(1+z\right)\left(1+{\frac {z}{2}}\right)\cdots \left(1+{\frac {z}{n}}\right)}}\\&={\frac {1}{z}}\lim _{n\to \infty }{\frac {1}{\left(1+z\right)\left(1+{\frac {z}{2}}\right)\cdots \left(1+{\frac {z}{n}}\right)}}e^{z\log \left(n+1\right)}\\&=\lim _{n\to \infty }{\frac {n!(n+1)^{z}}{z(z+1)\cdots (z+n)}},\quad z\in \mathbb {C} \setminus \mathbb {Z} _{0}^{-}\end{aligned}}$ |


## Properties

### General

Besides the fundamental property discussed above, $\Gamma (z+1)=z\ \Gamma (z).$ Other important functional equations for the gamma function are Euler's reflection formula, $\Gamma (1-z)\Gamma (z)={\frac {\pi }{\sin \pi z}},\qquad z\not \in \mathbb {Z} ,$ which implies $\Gamma (z-n)=(-1)^{n-1}\;{\frac {\Gamma (-z)\Gamma (1+z)}{\Gamma (n+1-z)}},\qquad n\in \mathbb {Z}$ and the Legendre duplication formula $\Gamma (z)\Gamma \left(z+{\frac {1}{2}}\right)=2^{1-2z}\,{\sqrt {\pi }}\,\Gamma (2z).$

| Derivation of Euler's reflection formula |
|---|
| **Proof 1** With Euler's infinite product $\Gamma (z)={\frac {1}{z}}\prod _{n=1}^{\infty }{\frac {(1+1/n)^{z}}{1+z/n}}$ compute ${\frac {1}{\Gamma (1-z)\Gamma (z)}}={\frac {1}{(-z)\Gamma (-z)\Gamma (z)}}=z\prod _{n=1}^{\infty }{\frac {(1-z/n)(1+z/n)}{(1+1/n)^{-z}(1+1/n)^{z}}}=z\prod _{n=1}^{\infty }\left(1-{\frac {z^{2}}{n^{2}}}\right)={\frac {\sin \pi z}{\pi }}\,,$ where the last equality is a known result. A similar derivation begins with Weierstrass's definition. **Proof 2** First prove that $I=\int _{-\infty }^{\infty }{\frac {e^{ax}}{1+e^{x}}}\,dx=\int _{0}^{\infty }{\frac {v^{a-1}}{1+v}}\,dv={\frac {\pi }{\sin \pi a}},\quad a\in (0,1).$ Consider the positively oriented rectangular contour $C_{R}$ with vertices at ⁠ R ⁠, ⁠ $-R$ ⁠, $R+2\pi i$ and $-R+2\pi i$ where ⁠ $R\in \mathbb {R} ^{+}$ ⁠. Then by the residue theorem, $\int _{C_{R}}{\frac {e^{az}}{1+e^{z}}}\,dz=-2\pi ie^{a\pi i}.$ Let $I_{R}=\int _{-R}^{R}{\frac {e^{ax}}{1+e^{x}}}\,dx$ and let $I_{R}'$ be the analogous integral over the top side of the rectangle. Then $I_{R}\to I$ as $R\to \infty$ and ⁠ $I_{R}'=-e^{2\pi ia}I_{R}$ ⁠. If $A_{R}$ denotes the right vertical side of the rectangle, then $\left\|\int _{A_{R}}{\frac {e^{az}}{1+e^{z}}}\,dz\right\|\leq \int _{0}^{2\pi }\left\|{\frac {e^{a(R+it)}}{1+e^{R+it}}}\right\|\,dt\leq Ce^{(a-1)R}$ for some constant C and since ⁠ $a<1$ ⁠, the integral tends to 0 as ⁠ $R\to \infty$ ⁠. Analogously, the integral over the left vertical side of the rectangle tends to 0 as ⁠ $R\to \infty$ ⁠. Therefore $I-e^{2\pi ia}I=-2\pi ie^{a\pi i},$ from which $I={\frac {\pi }{\sin \pi a}},\quad a\in (0,1).$ Then $\Gamma (1-z)=\int _{0}^{\infty }e^{-u}u^{-z}\,du=t\int _{0}^{\infty }e^{-vt}(vt)^{-z}\,dv,\quad t>0$ and ${\begin{aligned}\Gamma (z)\Gamma (1-z)&=\int _{0}^{\infty }\int _{0}^{\infty }e^{-t(1+v)}v^{-z}\,dv\,dt\\&=\int _{0}^{\infty }{\frac {v^{-z}}{1+v}}\,dv\\&={\frac {\pi }{\sin \pi (1-z)}}\\&={\frac {\pi }{\sin \pi z}},\quad z\in (0,1).\end{aligned}}$ Proving the reflection formula for all $z\in (0,1)$ proves it for all $z\in \mathbb {C} \setminus \mathbb {Z}$ by analytic continuation. |

| Derivation of the Legendre duplication formula |
|---|
| The beta function can be represented as $\mathrm {B} (z_{1},z_{2})={\frac {\Gamma (z_{1})\Gamma (z_{2})}{\Gamma (z_{1}+z_{2})}}=\int _{0}^{1}t^{z_{1}-1}(1-t)^{z_{2}-1}\,dt.$ Setting $z_{1}=z_{2}=z$ yields ${\frac {\Gamma ^{2}(z)}{\Gamma (2z)}}=\int _{0}^{1}t^{z-1}(1-t)^{z-1}\,dt.$ After the substitution ⁠ $t={\frac {1+u}{2}}$ ⁠: ${\frac {\Gamma ^{2}(z)}{\Gamma (2z)}}={\frac {1}{2^{2z-1}}}\int _{-1}^{1}\left(1-u^{2}\right)^{z-1}\,du.$ The function $(1-u^{2})^{z-1}$ is even, hence $2^{2z-1}\Gamma ^{2}(z)=2\Gamma (2z)\int _{0}^{1}(1-u^{2})^{z-1}\,du.$ Now $\mathrm {B} \left({\frac {1}{2}},z\right)=\int _{0}^{1}t^{{\frac {1}{2}}-1}(1-t)^{z-1}\,dt,\quad t=s^{2}.$ Then $\mathrm {B} \left({\frac {1}{2}},z\right)=2\int _{0}^{1}(1-s^{2})^{z-1}\,ds=2\int _{0}^{1}(1-u^{2})^{z-1}\,du.$ This implies $2^{2z-1}\Gamma ^{2}(z)=\Gamma (2z)\mathrm {B} \left({\frac {1}{2}},z\right).$ Since $\mathrm {B} \left({\frac {1}{2}},z\right)={\frac {\Gamma \left({\frac {1}{2}}\right)\Gamma (z)}{\Gamma \left(z+{\frac {1}{2}}\right)}},\quad \Gamma \left({\frac {1}{2}}\right)={\sqrt {\pi }},$ the Legendre duplication formula follows: $\Gamma (z)\Gamma \left(z+{\frac {1}{2}}\right)=2^{1-2z}{\sqrt {\pi }}\;\Gamma (2z).$ |

The duplication formula is a special case of the multiplication theorem (see  Eq. 5.5.6): $\prod _{k=0}^{m-1}\Gamma \left(z+{\frac {k}{m}}\right)=(2\pi )^{\frac {m-1}{2}}\;m^{{\frac {1}{2}}-mz}\;\Gamma (mz).$

A simple but useful property, which can be seen from the limit definition, is: ${\overline {\Gamma (z)}}=\Gamma ({\overline {z}})\;\Rightarrow \;\Gamma (z)\Gamma ({\overline {z}})\in \mathbb {R} .$

In particular, with ⁠ $z=a+bi$ ⁠, this product is $|\Gamma (a+bi)|^{2}=|\Gamma (a)|^{2}\prod _{k=0}^{\infty }{\frac {1}{1+{\frac {b^{2}}{(a+k)^{2}}}}}$

If the real part is an integer or a half-integer, this can be finitely expressed in closed form: ${\begin{aligned}|\Gamma (bi)|^{2}&={\frac {\pi }{b\sinh \pi b}}\\[6pt]\left|\Gamma \left({\tfrac {1}{2}}+bi\right)\right|^{2}&={\frac {\pi }{\cosh \pi b}}\\[6pt]\left|\Gamma \left(1+bi\right)\right|^{2}&={\frac {\pi b}{\sinh \pi b}}\\[6pt]\left|\Gamma \left(1+n+bi\right)\right|^{2}&={\frac {\pi b}{\sinh \pi b}}\prod _{k=1}^{n}\left(k^{2}+b^{2}\right),\quad n\in \mathbb {N} \\[6pt]\left|\Gamma \left(-n+bi\right)\right|^{2}&={\frac {\pi }{b\sinh \pi b}}\prod _{k=1}^{n}\left(k^{2}+b^{2}\right)^{-1},\quad n\in \mathbb {N} \\[6pt]\left|\Gamma \left({\tfrac {1}{2}}\pm n+bi\right)\right|^{2}&={\frac {\pi }{\cosh \pi b}}\prod _{k=1}^{n}\left(\left(k-{\tfrac {1}{2}}\right)^{2}+b^{2}\right)^{\pm 1},\quad n\in \mathbb {N} \\[-1ex]&\end{aligned}}$

| Proof of absolute value formulas for arguments of integer or half-integer real part |
|---|
| First, consider the reflection formula applied to ⁠ $z=bi$ ⁠. $\Gamma (bi)\Gamma (1-bi)={\frac {\pi }{\sin \pi bi}}$ Applying the recurrence relation to the second term: $-bi\cdot \Gamma (bi)\Gamma (-bi)={\frac {\pi }{\sin \pi bi}}$ which with simple rearrangement gives $\Gamma (bi)\Gamma (-bi)={\frac {\pi }{-bi\sin \pi bi}}={\frac {\pi }{b\sinh \pi b}}$ Second, consider the reflection formula applied to ⁠ $z={\tfrac {1}{2}}+bi$ ⁠. $\Gamma ({\tfrac {1}{2}}+bi)\Gamma \left(1-({\tfrac {1}{2}}+bi)\right)=\Gamma ({\tfrac {1}{2}}+bi)\Gamma ({\tfrac {1}{2}}-bi)={\frac {\pi }{\sin \pi ({\tfrac {1}{2}}+bi)}}={\frac {\pi }{\cos \pi bi}}={\frac {\pi }{\cosh \pi b}}$ Formulas for other values of z for which the real part is integer or half-integer quickly follow by induction using the recurrence relation in the positive and negative directions. |

Perhaps the best-known value of the gamma function at a non-integer argument is $\Gamma \left({\tfrac {1}{2}}\right)={\sqrt {\pi }},$ which can be found by setting ${\textstyle z={\frac {1}{2}}}$ in the reflection formula, by using the relation to the beta function given below with ⁠ $z_{1}=z_{2}={\frac {1}{2}}$ ⁠, or simply by making the substitution $t=u^{2}$ in the integral definition of the gamma function, resulting in a Gaussian integral. In general, for non-negative integer values of n we have: ${\begin{aligned}\Gamma \left({\frac {1}{2}}+n\right)&={(2n)! \over 4^{n}n!}{\sqrt {\pi }}={\frac {(2n-1)!!}{2^{n}}}{\sqrt {\pi }}={\binom {n-{\frac {1}{2}}}{n}}\,n!\,{\sqrt {\pi }}\\[6pt]\Gamma \left({\frac {1}{2}}-n\right)&={(-4)^{n}n! \over (2n)!}{\sqrt {\pi }}={\frac {(-2)^{n}}{(2n-1)!!}}{\sqrt {\pi }}={\frac {\sqrt {\pi }}{{\binom {-1/2}{n}}\,n!}}\end{aligned}}$ where the double factorial ⁠ $(2n-1)!!=(2n-1)(2n-3)\cdots (3)(1)$ ⁠. See Particular values of the gamma function for calculated values.

It might be tempting to generalize the result that ${\textstyle \Gamma \left({\frac {1}{2}}\right)={\sqrt {\pi }}}$ by looking for a formula for other individual values $\Gamma (r)$ where r is rational, especially because according to Gauss's digamma theorem, it is possible to do so for the closely related digamma function at every rational value. However, these numbers $\Gamma (r)$ are not known to be expressible by themselves in terms of elementary functions. It has been proved that $\Gamma (n+r)$ is a transcendental number and algebraically independent of $\pi$ for any integer n and each of the fractions ⁠ $\textstyle r={\frac {1}{6}},{\frac {1}{4}},{\frac {1}{3}},{\frac {2}{3}},{\frac {3}{4}},{\frac {5}{6}}$ ⁠. In general, when computing values of the gamma function, we must settle for numerical approximations.

The derivatives of the gamma function are described in terms of the polygamma function, ⁠ $\psi ^{(m)}(z)$ ⁠: $\Gamma '(z)=\Gamma (z)\psi ^{(0)}(z).$ For a positive integer m the derivative of the gamma function can be calculated as follows:

$\Gamma '(m+1)=m!\left(-\gamma +\sum _{k=1}^{m}{\frac {1}{k}}\right)=m!\left(-\gamma +H(m)\right)\,,$ where $H(m)$ is the m th harmonic number and $\gamma$ is the Euler–Mascheroni constant.

For $\Re (z)>0$ the n th derivative of the gamma function is: ${\frac {d^{n}}{dz^{n}}}\Gamma (z)=\int _{0}^{\infty }t^{z-1}e^{-t}(\log t)^{n}\,dt.$ (This can be derived by differentiating the integral form of the gamma function with respect to ⁠ z ⁠.)

Using the identity $\Gamma ^{(n)}(1)=(-1)^{n}B_{n}(\gamma ,1!\zeta (2),\ldots ,(n-1)!\,\zeta (n)),$ where $\zeta (z)$ is the Riemann zeta function, and $B_{n}$ is the n th Bell polynomial, we have in particular the Laurent series expansion of the gamma function $\Gamma (z)={\frac {1}{z}}-\gamma +{\frac {1}{2}}\left(\gamma ^{2}+{\frac {\pi ^{2}}{6}}\right)z-{\frac {1}{6}}\left(\gamma ^{3}+{\frac {\gamma \pi ^{2}}{2}}+2\zeta (3)\right)z^{2}+O(z^{3}).$

### Inequalities

When restricted to the positive real numbers, the gamma function is a strictly logarithmically convex function. This property may be stated in any of the following three equivalent ways:

- For any two positive real numbers $x_{1}$ and ⁠ $x_{2}$ ⁠, and for any ⁠ $t\in [0,1]$ ⁠, $\Gamma (tx_{1}+(1-t)x_{2})\leq \Gamma (x_{1})^{t}\Gamma (x_{2})^{1-t}.$
- For any two positive real numbers $x_{1}$ and ⁠ $x_{2}$ ⁠, and $x_{2}$ > $x_{1}$ $\left({\frac {\Gamma (x_{2})}{\Gamma (x_{1})}}\right)^{\frac {1}{x_{2}-x_{1}}}>\exp \left({\frac {\Gamma '(x_{1})}{\Gamma (x_{1})}}\right).$
- For any positive real number ⁠ x ⁠, $\Gamma ''(x)\Gamma (x)>\Gamma '(x)^{2}.$

The last of these statements is, essentially by definition, the same as the statement that ⁠ $\psi ^{(1)}(x)>0$ ⁠, where $\psi ^{(1)}$ is the polygamma function of order 1. To prove the logarithmic convexity of the gamma function, it therefore suffices to observe that $\psi ^{(1)}$ has a series representation which, for positive real x, consists of only positive terms.

Logarithmic convexity and Jensen's inequality together imply, for any positive real numbers ⁠ $x_{1},\ldots ,x_{n}$ ⁠ and ⁠ $a_{1},\ldots ,a_{n}$ ⁠, $\Gamma \left({\frac {a_{1}x_{1}+\cdots +a_{n}x_{n}}{a_{1}+\cdots +a_{n}}}\right)\leq {\bigl (}\Gamma (x_{1})^{a_{1}}\cdots \Gamma (x_{n})^{a_{n}}{\bigr )}^{\frac {1}{a_{1}+\cdots +a_{n}}}.$

There are also bounds on ratios of gamma functions. The best-known is Gautschi's inequality, which says that for any positive real number x and any *s* ∈ (0, 1), $x^{1-s}<{\frac {\Gamma (x+1)}{\Gamma (x+s)}}<\left(x+1\right)^{1-s}.$

### Stirling's formula

The behavior of $\Gamma (x)$ for an increasing positive real variable is given by Stirling's formula $\Gamma (x+1)\sim {\sqrt {2\pi x}}\left({\frac {x}{e}}\right)^{x},$ where the symbol $\sim$ means asymptotic convergence: the ratio of the two sides converges to ⁠ 1 ⁠ in the limit ⁠ $\textstyle x\to +\infty$ ⁠. This growth is faster than exponential, ⁠ $\exp(\beta x)$ ⁠, for any fixed value of ⁠ $\beta$ ⁠.

Another useful limit for asymptotic approximations for $x\to +\infty$ is: ${\Gamma (x+\alpha )}\sim {\Gamma (x)x^{\alpha }},\qquad \alpha \in \mathbb {C} .$

When writing the error term as an infinite product, Stirling's formula can be used to define the gamma function: $\Gamma (x)={\sqrt {\frac {2\pi }{x}}}\left({\frac {x}{e}}\right)^{x}\prod _{n=0}^{\infty }\left[{\frac {1}{e}}\left(1+{\frac {1}{x+n}}\right)^{x+n+{\frac {1}{2}}}\right].$

### Extension to negative, non-integer values

Although the main definition of the gamma function—the Euler integral of the second kind—is only valid (on the real axis) for positive arguments, its domain can be extended with analytic continuation to negative arguments by shifting the negative argument to positive values by using either the Euler's reflection formula, $\Gamma (-x)={\frac {1}{\Gamma (x+1)}}{\frac {\pi }{\sin {\big (}\pi (x+1){\big )}}},$ or the fundamental property, $\Gamma (-x):={\frac {\,1}{-x}}\,\Gamma (-x+1),$ when ⁠ $x\not \in \mathbb {Z}$ ⁠. For example, $\Gamma \!\left(\!-{\frac {1}{2}}\right)=-2\,\Gamma \!\left({\frac {1}{2}}\right).$

### Residues

The behavior for non-positive z is more intricate. Euler's integral does not converge for ⁠ $\Re (z)\leq 0$ ⁠, but the function it defines in the positive complex half-plane has a unique analytic continuation to the negative half-plane. One way to find that analytic continuation is to use Euler's integral for positive arguments and extend the domain to negative numbers by repeated application of the recurrence formula, $\Gamma (z)={\frac {\Gamma (z+n+1)}{z(z+1)\cdots (z+n)}},$ choosing n such that $z+n$ is positive. The product in the denominator is zero when z equals any of the integers ⁠ $0,-1,-2,\ldots$ ⁠. Thus, the gamma function must be undefined at those points to avoid division by zero; it is a meromorphic function with simple poles at the non-positive integers.

For a function f of a complex variable ⁠ z ⁠, at a simple pole ⁠ c ⁠, the residue of f is given by: $\operatorname {Res} (f,c)=\lim _{z\to c}(z-c)f(z).$

For the simple pole ⁠ $z=-n$ ⁠, the recurrence formula can be rewritten as: $(z+n)\Gamma (z)={\frac {\Gamma (z+n+1)}{z(z+1)\cdots (z+n-1)}}.$ The numerator at ⁠ $z=-n$ ⁠, is $\Gamma (z+n+1)=\Gamma (1)=1$ and the denominator $z(z+1)\cdots (z+n-1)=-n(1-n)\cdots (n-1-n)=(-1)^{n}n!.$ So the residues of the gamma function at those points are: $\operatorname {Res} (\Gamma ,-n)={\frac {(-1)^{n}}{n!}}.$ The gamma function is non-zero everywhere along the real line, although it comes arbitrarily close to zero as ⁠ $z\rightarrow -\infty$ ⁠. There is in fact no complex number z for which ⁠ $\Gamma (z)=0$ ⁠, and hence the reciprocal gamma function ${\textstyle {\dfrac {1}{\Gamma (z)}}}$ is an entire function, with zeros at ⁠ $z=0,-1,-2,\ldots$ ⁠.

### Minima and maxima

On the real line, the gamma function has a local minimum at *z*min = +1.46163214496836234126... where it attains the value Γ(*z*min) = +0.88560319441088870027.... The gamma function rises to either side of this minimum. The solution to Γ(*z* − 0.5) = Γ(*z* + 0.5) is *z* = +1.5 and the common value is Γ(1) = Γ(2) = +1. The positive solution to Γ(*z* − 1) = Γ(*z* + 1) is *z* = *φ* ≈ +1.618, the golden ratio, and the common value is Γ(*φ* − 1) = Γ(*φ* + 1) = *φ*! = +1.44922960226989660037....

The gamma function must alternate sign between its poles at the non-positive integers because the product in the forward recurrence contains an odd number of negative factors if the number of poles between z and $z+n$ is odd, and an even number if the number of poles is even. The values at the local extrema of the gamma function along the real axis between the non-positive integers are:

Γ(

−0.50408

30082

64455

40925...

) =

−3.54464

36111

55005

08912...

,

Γ(

−1.57349

84731

62390

45877...

) =

2.30240

72583

39680

13582...

,

Γ(

−2.61072

08684

44144

65000...

) =

−0.88813

63584

01241

92009...

,

Γ(

−3.63529

33664

36901

09783...

) =

0.24512

75398

34366

25043...

,

Γ(

−4.65323

77617

43142

44171...

) =

−0.05277

96395

87319

40076...

, etc.

### Integral representations

There are many formulas, besides the Euler integral of the second kind, that express the gamma function as an integral. For instance, when the real part of z is positive, $\Gamma (z)=\int _{-\infty }^{\infty }e^{zt-e^{t}}\,dt$ and $\Gamma (z)=\int _{0}^{1}\left(\log {\frac {1}{t}}\right)^{z-1}\,dt,$ $\Gamma (z)=2c^{z}\int _{0}^{\infty }t^{2z-1}e^{-ct^{2}}\,dt\,,\;c>0$ where the three integrals respectively follow from the substitutions ⁠ $t=e^{-x}$ ⁠, $t=-\log x$ and $t=cx^{2}$ in Euler's second integral. The last integral in particular makes clear the connection between the gamma function at half integer arguments and the Gaussian integral: if $z=1/2,\;c=1$ we get $\Gamma (1/2)=2\int _{0}^{\infty }e^{-t^{2}}\,dt={\sqrt {\pi }}\;.$

Binet's first integral formula for the gamma function states that, when the real part of z is positive, then: $\operatorname {log\Gamma } (z)=\left(z-{\frac {1}{2}}\right)\log z-z+{\frac {1}{2}}\log(2\pi )+\int _{0}^{\infty }\left({\frac {1}{2}}-{\frac {1}{t}}+{\frac {1}{e^{t}-1}}\right){\frac {e^{-tz}}{t}}\,dt.$ The integral on the right-hand side may be interpreted as a Laplace transform. That is, $\log \left(\Gamma (z)\left({\frac {e}{z}}\right)^{z}{\sqrt {\frac {z}{2\pi }}}\right)={\mathcal {L}}\left({\frac {1}{2t}}-{\frac {1}{t^{2}}}+{\frac {1}{t(e^{t}-1)}}\right)(z).$

Binet's second integral formula states that, again when the real part of z is positive, then: $\operatorname {log\Gamma } (z)=\left(z-{\frac {1}{2}}\right)\log z-z+{\frac {1}{2}}\log(2\pi )+2\int _{0}^{\infty }{\frac {\arctan(t/z)}{e^{2\pi t}-1}}\,dt.$

Let C be a Hankel contour, meaning a path that begins and ends at the point ∞ on the Riemann sphere, whose unit tangent vector converges to −1 at the start of the path and to 1 at the end, which has winding number 1 around 0, and which does not cross ⁠ $[0,\infty )$ ⁠. Fix a branch of $\log(-t)$ by taking a branch cut along $[0,\infty )$ and by taking $\log(-t)$ to be real when t is on the negative real axis. If z is not an integer, then Hankel's formula for the gamma function is: $\Gamma (z)=-{\frac {1}{2i\sin \pi z}}\int _{C}(-t)^{z-1}e^{-t}\,dt,$ where $(-t)^{z-1}$ is interpreted as ⁠ $\exp((z-1)\log(-t))$ ⁠. The reflection formula leads to the closely related expression ${\frac {1}{\Gamma (z)}}={\frac {i}{2\pi }}\int _{C}(-t)^{-z}e^{-t}\,dt,$ which is valid whenever ⁠ $z\not \in \mathbb {Z}$ ⁠.

### Continued fraction representation

The gamma function can also be represented by a sum of two continued fractions: ${\begin{aligned}\Gamma (z)&={\cfrac {e^{-1}}{2+0-z+1{\cfrac {z-1}{2+2-z+2{\cfrac {z-2}{2+4-z+3{\cfrac {z-3}{2+6-z+4{\cfrac {z-4}{2+8-z+5{\cfrac {z-5}{2+10-z+\ddots }}}}}}}}}}}}\\&+\ {\cfrac {e^{-1}}{z+0-{\cfrac {z+0}{z+1+{\cfrac {1}{z+2-{\cfrac {z+1}{z+3+{\cfrac {2}{z+4-{\cfrac {z+2}{z+5+{\cfrac {3}{z+6-\ddots }}}}}}}}}}}}}}\end{aligned}}$ where ⁠ $z\in \mathbb {C}$ ⁠.

### Fourier series expansion

The logarithm of the gamma function has the following Fourier series expansion for $0<z<1:$ $\operatorname {log\Gamma } (z)=\left({\frac {1}{2}}-z\right)(\gamma +\log 2)+(1-z)\log \pi -{\frac {1}{2}}\log \sin(\pi z)+{\frac {1}{\pi }}\sum _{n=1}^{\infty }{\frac {\log n}{n}}\sin(2\pi nz),$ which was for a long time attributed to Ernst Kummer, who derived it in 1847. However, Iaroslav Blagouchine discovered that Carl Johan Malmsten first derived this series in 1842.

### Raabe's formula

In 1840 Joseph Ludwig Raabe proved that $\int _{a}^{a+1}\log \Gamma (z)\,dz={\tfrac {1}{2}}\log 2\pi +a\log a-a,\quad a>0.$ In particular, if $a=0$ then $\int _{0}^{1}\log \Gamma (z)\,dz={\frac {1}{2}}\log(2\pi ).$

The latter can be derived taking the logarithm in the above multiplication formula, which gives an expression for the Riemann sum of the integrand. Taking the limit for $a\to \infty$ gives the formula.

### Pi function

An alternative notation introduced by Gauss is the $\Pi$ -function, a shifted version of the gamma function: $\Pi (z)=\Gamma (z+1)=z\Gamma (z)=\int _{0}^{\infty }e^{-t}t^{z}\,dt,$ so that $\Pi (n)=n!$ for every non-negative integer ⁠ n ⁠.

Using the pi function, the reflection formula is: $\Pi (z)\Pi (-z)={\frac {\pi z}{\sin(\pi z)}}={\frac {1}{\operatorname {sinc} (z)}}$ using the normalized sinc function; while the multiplication theorem becomes: $\Pi \left({\frac {z}{m}}\right)\,\Pi \left({\frac {z-1}{m}}\right)\cdots \Pi \left({\frac {z-m+1}{m}}\right)=(2\pi )^{\frac {m-1}{2}}m^{-z-{\frac {1}{2}}}\Pi (z)\ .$

The shifted reciprocal gamma function is sometimes denoted ⁠ $\pi (z)={\frac {1}{\Pi (z)}}$ ⁠, an entire function.

The volume of an n-ellipsoid with radii *r*1, ..., *r**n* can be expressed as $V_{n}(r_{1},\dotsc ,r_{n})={\frac {\pi ^{\frac {n}{2}}}{\Pi \left({\frac {n}{2}}\right)}}\prod _{k=1}^{n}r_{k}.$

### Relation to other functions

- In the first integral defining the gamma function, the limits of integration are fixed. The upper incomplete gamma function is obtained by allowing the lower limit of integration to vary: $\Gamma (z,x)=\int _{x}^{\infty }t^{z-1}e^{-t}dt.$ There is a similar lower incomplete gamma function.
- The gamma function is related to Euler's beta function by the formula $\mathrm {B} (z_{1},z_{2})=\int _{0}^{1}t^{z_{1}-1}(1-t)^{z_{2}-1}\,dt={\frac {\Gamma (z_{1})\,\Gamma (z_{2})}{\Gamma (z_{1}+z_{2})}}.$
- The logarithmic derivative of the gamma function is called the digamma function; higher derivatives are the polygamma functions.
- The analog of the gamma function over a finite field or a finite ring is the Gaussian sums, a type of exponential sum.
- The reciprocal gamma function is an entire function and has been studied as a specific topic.
- The gamma function also shows up in an important relation with the Riemann zeta function, ⁠ $\zeta (z)$ ⁠. $\pi ^{-{\frac {z}{2}}}\;\Gamma \left({\frac {z}{2}}\right)\zeta (z)=\pi ^{-{\frac {1-z}{2}}}\;\Gamma \left({\frac {1-z}{2}}\right)\;\zeta (1-z).$ It also appears in the following formula: $\zeta (z)\Gamma (z)=\int _{0}^{\infty }{\frac {u^{z}}{e^{u}-1}}\,{\frac {du}{u}},$ which is valid only for ⁠ $\Re (z)>1$ ⁠. The logarithm of the gamma function satisfies the following formula due to Lerch: $\operatorname {log\Gamma } (z)=\zeta _{H}'(0,z)-\zeta '(0),$ where $\zeta _{H}$ is the Hurwitz zeta function, $\zeta$ is the Riemann zeta function and the prime (′) denotes differentiation in the first variable.
- The gamma function is related to the stretched exponential function. For instance, the moments of that function are $\langle \tau ^{n}\rangle \equiv \int _{0}^{\infty }t^{n-1}\,e^{-\left({\frac {t}{\tau }}\right)^{\beta }}\,\mathrm {d} t={\frac {\tau ^{n}}{\beta }}\Gamma \left({n \over \beta }\right).$

### Particular values

Including up to the first 20 digits after the decimal point, some particular values of the gamma function are: ${\begin{array}{rcccl}\Gamma \left(-{\frac {3}{2}}\right)&=&{\frac {4{\sqrt {\pi }}}{3}}&\approx &+2.36327\,18012\,07354\,70306\\[6pt]\Gamma \left(-{\frac {1}{2}}\right)&=&-2{\sqrt {\pi }}&\approx &-3.54490\,77018\,11032\,05459\\[6pt]\Gamma \left({\frac {1}{2}}\right)&=&{\sqrt {\pi }}&\approx &+1.77245\,38509\,05516\,02729\\[6pt]\Gamma (1)&=&0!&=&+1\\[6pt]\Gamma \left({\frac {3}{2}}\right)&=&{\frac {\sqrt {\pi }}{2}}&\approx &+0.88622\,69254\,52758\,01364\\[6pt]\Gamma (2)&=&1!&=&+1\\[6pt]\Gamma \left({\frac {5}{2}}\right)&=&{\frac {3{\sqrt {\pi }}}{4}}&\approx &+1.32934\,03881\,79137\,02047\\[6pt]\Gamma (3)&=&2!&=&+2\\[6pt]\Gamma \left({\frac {7}{2}}\right)&=&{\tfrac {15{\sqrt {\pi }}}{8}}&\approx &+3.32335\,09704\,47842\,55118\\[6pt]\Gamma (4)&=&3!&=&+6\end{array}}$ (These numbers can be found in the OEIS. The values presented here are truncated rather than rounded.) The complex-valued gamma function is undefined for non-positive integers, but in these cases the value can be defined in the Riemann sphere as ⁠ $\infty$ ⁠. The reciprocal gamma function is well defined and analytic at these values (and in the entire complex plane): ${\frac {1}{\Gamma (-3)}}={\frac {1}{\Gamma (-2)}}={\frac {1}{\Gamma (-1)}}={\frac {1}{\Gamma (0)}}=0.$


## Log-gamma function

Because the gamma and factorial functions grow so rapidly for moderately large arguments, many computing environments include a function that returns the natural logarithm of the gamma function, often given the name `lgamma` or `lngamma` in programming environments or `gammaln` in spreadsheets. This grows much more slowly, and for combinatorial calculations allows adding and subtracting logarithmic values instead of multiplying and dividing very large values. It is often defined as $\operatorname {log\Gamma } (z)=-\gamma z-\log z+\sum _{k=1}^{\infty }\left[{\frac {z}{k}}-\log \left(1+{\frac {z}{k}}\right)\right].$

The digamma function, which is the derivative of this function, is also commonly seen. In the context of technical and physical applications, e.g. with wave propagation, the functional equation $\operatorname {log\Gamma } (z)=\operatorname {log\Gamma } (z+1)-\log z$

is often used since it allows one to determine function values in one strip of width 1 in z from the neighbouring strip. In particular, starting with a good approximation for a z with large real part one may go step by step down to the desired ⁠ z ⁠. Following an indication of Carl Friedrich Gauss, Rocktaeschel (1922) proposed for $\log \Gamma (z)$ an approximation for large ⁠ $\Re (z)$ ⁠: $\operatorname {log\Gamma } (z)\approx (z-{\tfrac {1}{2}})\log z-z+{\tfrac {1}{2}}\log(2\pi ).$

This can be used to accurately approximate $\log \Gamma (z)$ for z with a smaller $\Re (z)$ via (P.E.Böhmer, 1939) $\operatorname {log\Gamma } (z-m)=\operatorname {log\Gamma } (z)-\sum _{k=1}^{m}\log(z-k).$

A more accurate approximation can be obtained by using more terms from the asymptotic expansions of $\log \Gamma (z)$ and ⁠ $\Gamma (z)$ ⁠, which are based on Stirling's approximation. $\Gamma (z)\sim z^{z-{\frac {1}{2}}}e^{-z}{\sqrt {2\pi }}\left(1+{\frac {1}{12z}}+{\frac {1}{288z^{2}}}-{\frac {139}{51\,840z^{3}}}-{\frac {571}{2\,488\,320z^{4}}}\right)$

as

$|z|\rightarrow \infty$

at constant

⁠

$\vert \arg(z)\vert <\pi$

⁠

. (See sequences

A001163

and

A001164

in the

OEIS

.)

In a more "natural" presentation, $\log \Gamma (z)=z\log z-z-{\frac {1}{2}}\log z+{\frac {1}{2}}\log 2\pi +{\frac {1}{12z}}-{\frac {1}{360z^{3}}}+{\frac {1}{1260z^{5}}}+O\left({\frac {1}{z^{5}}}\right)$

as

$|z|\rightarrow \infty$

at constant

⁠

$\vert \arg(z)\vert <\pi$

⁠

. (See sequences

A046968

and

A046969

in the

OEIS

.)

The coefficients of the terms with $k>1$ of $z^{1-k}$ in the last expansion are simply ${\frac {B_{k}}{k(k-1)}},$ where the $B_{k}$ are the Bernoulli numbers.

The gamma function also has Stirling Series (derived by Charles Hermite in 1900) equal to $\operatorname {log\Gamma } (1+x)={\frac {x(x-1)}{2!}}\log(2)+{\frac {x(x-1)(x-2)}{3!}}(\log(3)-2\log(2))+\cdots ,\quad \Re (x)>0.$

### Properties

The Bohr–Mollerup theorem states that among all functions extending the factorial functions to the positive real numbers, only the gamma function is log-convex, that is, its natural logarithm is convex on the positive real axis. Another characterisation is given by the Wielandt theorem.

The gamma function is the unique function that simultaneously satisfies

1. ⁠ $\Gamma (1)=1$ ⁠,
2. $\Gamma (z+1)=z\Gamma (z)$ for all complex numbers z except the non-positive integers, and,
3. for integer n, ${\textstyle \lim _{n\to \infty }{\frac {\Gamma (n+z)}{\Gamma (n)\;n^{z}}}=1}$ for all complex numbers ⁠ z ⁠.

In a certain sense, the log-gamma function is the more natural form; it makes some intrinsic attributes of the function clearer. A striking example is the Taylor series of logΓ around 1: $\operatorname {log\Gamma } (z+1)=-\gamma z+\sum _{k=2}^{\infty }{\frac {\zeta (k)}{k}}\,(-z)^{k}\qquad \forall \;|z|<1$ with ⁠ $\zeta (k)$ ⁠ denoting the Riemann zeta function at ⁠ k ⁠.

So, using the following property: $\zeta (s)\Gamma (s)=\int _{0}^{\infty }{\frac {t^{s}}{e^{t}-1}}\,{\frac {dt}{t}}$ an integral representation for the log-gamma function is: $\operatorname {log\Gamma } (z+1)=-\gamma z+\int _{0}^{\infty }{\frac {e^{-zt}-1+zt}{t\left(e^{t}-1\right)}}\,dt$ or, setting ⁠ $z=1$ ⁠ to obtain an integral for ⁠ $\gamma$ ⁠, we can replace the ⁠ $\gamma$ ⁠ term with its integral and incorporate that into the above formula, to get: $\operatorname {log\Gamma } (z+1)=\int _{0}^{\infty }{\frac {e^{-zt}-ze^{-t}-1+z}{t\left(e^{t}-1\right)}}\,dt\,.$

There also exist special formulas for the logarithm of the gamma function for rational ⁠ z ⁠. For instance, if k and n are integers with $k<n$ and ⁠ $k\neq n/2$ ⁠, then ${\begin{aligned}\operatorname {log\Gamma } \left({\frac {k}{n}}\right)={}&{\frac {\,(n-2k)\log 2\pi \,}{2n}}+{\frac {1}{2}}\left\{\,\log \pi -\log \sin {\frac {\pi k}{n}}\,\right\}+{\frac {1}{\pi }}\!\sum _{r=1}^{n-1}{\frac {\,\gamma +\log r\,}{r}}\cdot \sin {\frac {\,2\pi rk\,}{n}}\\&{}-{\frac {1}{2\pi }}\sin {\frac {2\pi k}{n}}\cdot \!\int _{0}^{\infty }\!\!{\frac {\,e^{-nx}\!\cdot \log x\,}{\,\cosh x-\cos(2\pi k/n)\,}}\,{\mathrm {d} }x.\end{aligned}}$ This formula is sometimes used for numerical computation, since the integrand decreases very quickly.

### Integration over log-gamma

The integral $\int _{0}^{z}\operatorname {log\Gamma } (x)\,dx$ can be expressed in terms of the Barnes G-function (see Barnes G-function for a proof): $\int _{0}^{z}\operatorname {log\Gamma } (x)\,dx={\frac {z}{2}}\log(2\pi )+{\frac {z(1-z)}{2}}+z\operatorname {log\Gamma } (z)-\log G(z+1)$ where ⁠ $\Re (z)>-1$ ⁠.

It can also be written in terms of the Hurwitz zeta function: $\int _{0}^{z}\operatorname {log\Gamma } (x)\,dx={\frac {z}{2}}\log(2\pi )+{\frac {z(1-z)}{2}}-\zeta '(-1)+\zeta '(-1,z).$

When $z=1$ it follows that $\int _{0}^{1}\operatorname {log\Gamma } (x)\,dx={\frac {1}{2}}\log(2\pi ),$ and this is a consequence of Raabe's formula as well. Espinosa and Moll derived a similar formula for the integral of the square of ⁠ $\operatorname {log\Gamma }$ ⁠: $\int _{0}^{1}\log ^{2}\Gamma (x)dx={\frac {\gamma ^{2}}{12}}+{\frac {\pi ^{2}}{48}}+{\frac {1}{3}}\gamma L_{1}+{\frac {4}{3}}L_{1}^{2}-\left(\gamma +2L_{1}\right){\frac {\zeta ^{\prime }(2)}{\pi ^{2}}}+{\frac {\zeta ^{\prime \prime }(2)}{2\pi ^{2}}},$ where $L_{1}$ is ⁠ ${\frac {1}{2}}\log(2\pi )$ ⁠.

D. H. Bailey and his co-authors gave an evaluation for $L_{n}:=\int _{0}^{1}\log ^{n}\Gamma (x)\,dx$ when $n=1,2$ in terms of the Tornheim–Witten zeta function and its derivatives.

In addition, it is also known that $\lim _{n\to \infty }{\frac {L_{n}}{n!}}=1.$


## Approximations

Complex values of the gamma function can be approximated using Stirling's approximation or the Lanczos approximation, $\Gamma (z)\sim {\sqrt {2\pi }}z^{z-1/2}e^{-z}\quad {\hbox{as }}z\to \infty {\hbox{ in }}\left|\arg(z)\right|<\pi .$ This is precise in the sense that the ratio of the approximation to the true value approaches ⁠ 1 ⁠ in the limit as ⁠ $\vert z\vert \rightarrow \infty$ ⁠.

The gamma function can be computed to fixed precision for $\Re (z)\in [1,2]$ by applying integration by parts to Euler's integral. For any positive number ⁠ x ⁠ the gamma function can be written ${\begin{aligned}\Gamma (z)&=\int _{0}^{x}e^{-t}t^{z}\,{\frac {dt}{t}}+\int _{x}^{\infty }e^{-t}t^{z}\,{\frac {dt}{t}}\\&=x^{z}e^{-x}\sum _{n=0}^{\infty }{\frac {x^{n}}{z(z+1)\cdots (z+n)}}+\int _{x}^{\infty }e^{-t}t^{z}\,{\frac {dt}{t}}.\end{aligned}}$

When ⁠ $\Re (z)\in [1,2]$ ⁠ and ⁠ $x\geq 1$ ⁠, the absolute value of the last integral is smaller than ⁠ $(x+1)e^{-x}$ ⁠. By choosing a large enough ⁠ x ⁠, this last expression can be made smaller than $2^{-N}$ for any desired value ⁠ N ⁠. Thus, the gamma function can be evaluated to N bits of precision with the above series.

A fast algorithm for calculation of the Euler gamma function for any algebraic argument (including rational) was constructed by E.A. Karatsuba.

For arguments that are integer multiples of ⁠ ${\tfrac {1}{24}}$ ⁠, the gamma function can also be evaluated quickly using arithmetic–geometric mean iterations (see particular values of the gamma function).


## Practical implementations

Unlike many other functions, such as a normal distribution, no obvious fast, accurate implementation that is easy to implement for the gamma function $\Gamma (z)$ is easily found. Therefore, it is worth investigating potential solutions. For the case that speed is more important than accuracy, published tables for $\Gamma (z)$ are easily found in an Internet search, such as the Online Wiley Library. Such tables may be used with linear interpolation. Greater accuracy is obtainable with the use of cubic interpolation at the cost of more computational overhead. Since $\Gamma (z)$ tables are usually published for argument values between 1 and 2, the property $\Gamma (z+1)=z\ \Gamma (z)$ may be used to quickly and easily translate all real values $z<1$ and $z>2$ into the range ⁠ $1\leq z\leq 2$ ⁠, such that only tabulated values of z between 1 and 2 need be used.

If interpolation tables are not desirable, then the Lanczos approximation mentioned above works well for 1 to 2 digits of accuracy for small, commonly used values of ⁠ z ⁠. If the Lanczos approximation is not sufficiently accurate, the Stirling's formula for the Gamma Function may be used.
