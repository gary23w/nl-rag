---
title: "Mellin transform"
source: https://en.wikipedia.org/wiki/Mellin_transform
domain: mellin-transform
license: CC-BY-SA-4.0
tags: mellin transform, mellin inversion theorem, dirichlet series, harmonic sum
fetched: 2026-07-02
---

# Mellin transform

In mathematics, the **Mellin transform** is an integral transform that may be regarded as the multiplicative version of the two-sided Laplace transform. This integral transform is closely connected to the theory of Dirichlet series, and is often used in number theory, mathematical statistics, and the theory of asymptotic expansions; it is essentially the same as the Laplace transform and closely related to the Fourier transform, and the theory of the gamma function and allied special functions.

The Mellin transform of a complex-valued function f defined on $\mathbf {R} _{+}^{\times }=(0,\infty )$ is the function ${\mathcal {M}}f$ of complex variable s given (where it exists, see § Fundamental strip below) by ${\mathcal {M}}\left\{f\right\}(s)=\varphi (s)=\int _{0}^{\infty }x^{s-1}f(x)\,dx=\int _{\mathbf {R} _{+}^{\times }}f(x)x^{s}{\frac {dx}{x}}.$ Notice that $dx/x$ is a Haar measure on the multiplicative group $\mathbf {R} _{+}^{\times }$ and $x\mapsto x^{s}$ is a (in general non-unitary) multiplicative character. The inverse transform is ${\mathcal {M}}^{-1}\left\{\varphi \right\}(x)=f(x)={\frac {1}{2\pi i}}\int _{c-i\infty }^{c+i\infty }x^{-s}\varphi (s)\,ds.$ The notation implies this is a line integral taken over a vertical line in the complex plane, whose real part *c* need only satisfy a mild lower bound. Conditions under which this inversion is valid are given in the Mellin inversion theorem.

The transform was introduced in 1859 by Bernhard Riemann. The transform is named after the Finnish mathematician Hjalmar Mellin, who developed the first rigorous account in paper published 1897 in *Acta Societatis Scientiarum Fennicae.*

## Relationship to other transforms

The two-sided Laplace transform may be defined in terms of the Mellin transform by ${\mathcal {B}}\left\{f\right\}(s)={\mathcal {M}}\left\{f(-\ln x)\right\}(s)$ and conversely we can get the Mellin transform from the two-sided Laplace transform by ${\mathcal {M}}\left\{f\right\}(s)={\mathcal {B}}\left\{f(e^{-x})\right\}(s).$

The Mellin transform may be thought of as integrating using a kernel xs with respect to the multiplicative Haar measure, ${\textstyle {\frac {dx}{x}}}$ , which is invariant under dilation $x\mapsto ax$ , so that ${\textstyle {\frac {d(ax)}{ax}}={\frac {dx}{x}};}$ the two-sided Laplace transform integrates with respect to the additive Haar measure ⁠ $dx$ ⁠, which is translation invariant, so that ⁠ $d(x+a)=dx$ ⁠.

We also may define the Fourier transform in terms of the Mellin transform and vice versa; in terms of the Mellin transform and of the two-sided Laplace transform defined above $\left\{{\mathcal {F}}f\right\}(-s)=\left\{{\mathcal {B}}f\right\}(-is)=\left\{{\mathcal {M}}f(-\ln x)\right\}(-is)\ .$ We may also reverse the process and obtain $\left\{{\mathcal {M}}f\right\}(s)=\left\{{\mathcal {B}}f(e^{-x})\right\}(s)=\left\{{\mathcal {F}}f(e^{-x})\right\}(-is)\ .$

The Mellin transform also connects the Newton series or binomial transform together with the Poisson generating function, by means of the Poisson–Mellin–Newton cycle.

The Mellin transform may also be viewed as the Gelfand transform for the convolution algebra of the locally compact abelian group of positive real numbers with multiplication.

## Examples

### Cahen–Mellin integral

The Mellin transform of the function $f(x)=e^{-x}$ is $\Gamma (s)=\int _{0}^{\infty }x^{s-1}e^{-x}dx$ where $\Gamma (s)$ is the gamma function. $\Gamma (s)$ is a meromorphic function with simple poles at ⁠ $z=0,-1,-2,\dots$ ⁠. Therefore, $\Gamma (s)$ is analytic for ⁠ $\Re (s)>0$ ⁠. Thus, letting $c>0$ and $z^{-s}$ on the principal branch, the inverse transform gives $e^{-z}={\frac {1}{2\pi i}}\int _{c-i\infty }^{c+i\infty }\Gamma (s)z^{-s}\;ds.$

This integral is known as the Cahen–Mellin integral.

### Polynomial functions

Since ${\textstyle \int _{0}^{\infty }x^{a}dx}$ is not convergent for any value of ⁠ $a\in \mathbb {R}$ ⁠, the Mellin transform is not defined for polynomial functions defined on the whole positive real axis. However, by defining it to be zero on different sections of the real axis, it is possible to take the Mellin transform. For example, if $f(x)={\begin{cases}x^{a}&x<1,\\0&x>1,\end{cases}}$ then ${\mathcal {M}}f(s)=\int _{0}^{1}x^{s-1}x^{a}dx=\int _{0}^{1}x^{s+a-1}dx={\frac {1}{s+a}}.$

Thus ${\mathcal {M}}f(s)$ has a simple pole at $s=-a$ and is thus defined for ⁠ $\Re (s)>-a$ ⁠. Similarly, if $f(x)={\begin{cases}0&x<1,\\x^{b}&x>1,\end{cases}}$ then ${\mathcal {M}}f(s)=\int _{1}^{\infty }x^{s-1}x^{b}dx=\int _{1}^{\infty }x^{s+b-1}dx=-{\frac {1}{s+b}}.$ Thus ${\mathcal {M}}f(s)$ has a simple pole at $s=-b$ and is thus defined for ⁠ $\Re (s)<-b$ ⁠.

### Exponential functions

For ⁠ $p>0$ ⁠, let ⁠ $f(x)=e^{-px}$ ⁠. Then ${\mathcal {M}}f(s)=\int _{0}^{\infty }x^{s}e^{-px}{\frac {dx}{x}}=\int _{0}^{\infty }\left({\frac {u}{p}}\right)^{s}e^{-u}{\frac {du}{u}}={\frac {1}{p^{s}}}\int _{0}^{\infty }u^{s}e^{-u}{\frac {du}{u}}={\frac {1}{p^{s}}}\Gamma (s).$

### Zeta function

It is possible to use the Mellin transform to produce one of the fundamental formulas for the Riemann zeta function, ⁠ $\zeta (s)$ ⁠. Let ⁠ $f(x)={\tfrac {1}{e^{x}-1}}$ ⁠. Then ${\begin{alignedat}{3}{\mathcal {M}}f(s)&=\int _{0}^{\infty }x^{s-1}{\frac {1}{e^{x}-1}}dx&&=\int _{0}^{\infty }x^{s-1}{\frac {e^{-x}}{1-e^{-x}}}dx\\&=\int _{0}^{\infty }x^{s-1}\sum _{n=1}^{\infty }e^{-nx}dx&&=\sum _{n=1}^{\infty }\int _{0}^{\infty }x^{s}e^{-nx}{\frac {dx}{x}}\\&=\sum _{n=1}^{\infty }{\frac {1}{n^{s}}}\Gamma (s)=\Gamma (s)\zeta (s).\end{alignedat}}$ Thus, $\zeta (s)={\frac {1}{\Gamma (s)}}\int _{0}^{\infty }x^{s-1}{\frac {1}{e^{x}-1}}dx.$

### Generalized Gaussian

For ⁠ $p>0$ ⁠, let $f(x)=e^{-x^{p}}$ (i.e. f is a generalized Gaussian distribution without the scaling factor.) Then ${\begin{alignedat}{3}{\mathcal {M}}f(s)&=\int _{0}^{\infty }x^{s-1}e^{-x^{p}}dx&&=\int _{0}^{\infty }x^{p-1}x^{s-p}e^{-x^{p}}dx\\&=\int _{0}^{\infty }x^{p-1}(x^{p})^{(s/p)-1}e^{-x^{p}}dx&&={\frac {1}{p}}\int _{0}^{\infty }u^{(s/p)-1}e^{-u}du\\&={\frac {\Gamma (s/p)}{p}}.\end{alignedat}}$ In particular, setting $s=1$ recovers the following form of the gamma function $\Gamma \left(1+{\frac {1}{p}}\right)=\int _{0}^{\infty }e^{-x^{p}}dx.$

### Power series and Dirichlet series

Generally, assuming the necessary convergence, we can connect Dirichlet series and power series $F(s)=\sum \limits _{n=1}^{\infty }{\frac {a_{n}}{n^{s}}},\quad f(z)=\sum \limits _{n=1}^{\infty }a_{n}z^{n}$ by this formal identity involving the Mellin transform: $\Gamma (s)F(s)=\int _{0}^{\infty }x^{s-1}f(e^{-x})dx$

## Fundamental strip

For ⁠ $\alpha ,\beta \in \mathbb {R}$ ⁠, let the open strip $\langle \alpha ,\beta \rangle$ be defined to be all $s\in \mathbb {C}$ such that $s=\sigma +it$ with ⁠ $\alpha <\sigma <\beta$ ⁠. The **fundamental strip** of ${\mathcal {M}}f(s)$ is defined to be the largest open strip on which it is defined. For example, for $a>b$ the fundamental strip of $f(x)={\begin{cases}x^{a}&x<1,\\x^{b}&x>1,\end{cases}}$ is ⁠ $\langle -a,-b\rangle$ ⁠. As seen by this example, the asymptotics of the function as $x\to 0^{+}$ define the left endpoint of its fundamental strip, and the asymptotics of the function as $x\to +\infty$ define its right endpoint. To summarize using Big O notation, if f is $O(x^{a})$ as $x\to 0^{+}$ and $O(x^{b})$ as ⁠ $x\to +\infty$ ⁠, then ${\mathcal {M}}f(s)$ is defined in the strip ⁠ $\langle -a,-b\rangle$ ⁠.

An application of this can be seen in the gamma function, ⁠ $\Gamma (s)$ ⁠. Since $f(x)=e^{-x}$ is $O(x^{0})$ as $x\to 0^{+}$ and $O(x^{k})$ for all ⁠ k ⁠, then $\Gamma (s)={\mathcal {M}}f(s)$ should be defined in the strip ⁠ $\langle 0,+\infty \rangle$ ⁠, which confirms that $\Gamma (s)$ is analytic for ⁠ $\Re (s)>0$ ⁠.

## Properties

The properties in this table may be found in Bracewell (2000) and Erdélyi (1954).

| Function | Mellin transform | Fundamental strip | Comments |
|---|---|---|---|
| $f(x)$ | ${\tilde {f}}(s)=\{{\mathcal {M}}f\}(s)=\int _{0}^{\infty }f(x)x^{s}{\frac {dx}{x}}$ | $\alpha <\Re s<\beta$ | Definition |
| $x^{\nu }\,f(x)$ | ${\tilde {f}}(s+\nu )$ | $\alpha -\Re \nu <\Re s<\beta -\Re \nu$ |   |
| $f(x^{\nu })$ | ${\frac {1}{\|\nu \|}}\,{\tilde {f}}\left({\frac {s}{\nu }}\right)$ | $\alpha <\nu ^{-1}\,\Re s<\beta$ | $\nu \in \mathbb {R} ,\;\nu \neq 0$ |
| $f(x^{-1})$ | ${\tilde {f}}(-s)$ | $-\beta <\Re s<-\alpha$ |   |
| $x^{-1}\,f(x^{-1})$ | ${\tilde {f}}(1-s)$ | $1-\beta <\Re s<1-\alpha$ | Involution |
| ${\overline {f(x)}}$ | ${\overline {{\tilde {f}}({\overline {s}})}}$ | $\alpha <\Re s<\beta$ | Here ${\overline {z}}$ denotes the complex conjugate of ⁠ z ⁠. |
| $f(\nu x)$ | $\nu ^{-s}{\tilde {f}}(s)$ | $\alpha <\Re s<\beta$ | $\nu >0$ , Scaling |
| $f(x)\,\ln x$ | ${\tilde {f}}'(s)$ | $\alpha <\Re s<\beta$ |   |
| $f'(x)$ | $-(s-1)\,{\tilde {f}}(s-1)$ | $\alpha +1<\Re s<\beta +1$ | The domain shift is conditional and requires evaluation against specific convergence behavior. |
| $\left({\frac {d}{dx}}\right)^{n}\,f(x)$ | $(-1)^{n}\,{\frac {\Gamma (s)}{\Gamma (s-n)}}{\tilde {f}}(s-n)$ | $\alpha +n<\Re s<\beta +n$ |   |
| $x\,f'(x)$ | $-s\,{\tilde {f}}(s)$ | $\alpha <\Re s<\beta$ |   |
| $\left(x\,{\frac {d}{dx}}\right)^{n}\,f(x)$ | $(-s)^{n}{\tilde {f}}(s)$ | $\alpha <\Re s<\beta$ |   |
| $\left({\frac {d}{dx}}\,x\right)^{n}\,f(x)$ | $(1-s)^{n}{\tilde {f}}(s)$ | $\alpha <\Re s<\beta$ |   |
| $\int _{0}^{x}f(y)\,dy$ | $-s^{-1}\,{\tilde {f}}(s+1)$ | $\alpha -1<\Re s<\min(\beta -1,0)$ | Valid only if the integral exists. |
| $\int _{x}^{\infty }f(y)\,dy$ | $s^{-1}\,{\tilde {f}}(s+1)$ | $\max(\alpha -1,0)<\Re s<\beta -1$ | Valid only if the integral exists. |
| $\int _{0}^{\infty }f_{1}\left({\frac {x}{y}}\right)\,f_{2}(y)\,{\frac {dy}{y}}$ | ${\tilde {f}}_{1}(s)\,{\tilde {f}}_{2}(s)$ | $\max(\alpha _{1},\alpha _{2})<\Re s<\min(\beta _{1},\beta _{2})$ | Multiplicative convolution |
| $x^{\mu }\int _{0}^{\infty }y^{\nu }\,f_{1}\left({\frac {x}{y}}\right)\,f_{2}(y)\,dy$ | ${\tilde {f}}_{1}(s+\mu )\,{\tilde {f}}_{2}(s+\mu +\nu +1)$ |   | Multiplicative convolution (generalized) |
| $x^{\mu }\int _{0}^{\infty }y^{\nu }\,f_{1}(x\,y)\,f_{2}(y)\,dy$ | ${\tilde {f}}_{1}(s+\mu )\,{\tilde {f}}_{2}(1-s-\mu +\nu )$ |   | Multiplicative convolution (generalized) |
| $f_{1}(x)\,f_{2}(x)$ | ${\frac {1}{2\pi i}}\int _{c-i\infty }^{c+i\infty }{\tilde {f}}_{1}(r)\,{\tilde {f}}_{2}(s-r)\,dr$ | ${\begin{aligned}\alpha _{2}+c&<\Re s<\beta _{2}+c\\\alpha _{1}&<c<\beta _{1}\end{aligned}}$ | Multiplication. Only valid if integral exists. See Parseval's theorem below for conditions which ensure the existence of the integral. |

### Parseval's theorem and Plancherel's theorem

Let $f_{1}(x)$ and $f_{2}(x)$ be functions with well-defined Mellin transforms ${\tilde {f}}_{1,2}(s)={\mathcal {M}}\{f_{1,2}\}(s)$ in the fundamental strips ⁠ $\alpha _{1,2}<\Re s<\beta _{1,2}$ ⁠. Let $c\in \mathbb {R}$ with ⁠ $\max(\alpha _{1},1-\beta _{2})<c<\min(\beta _{1},1-\alpha _{2})$ ⁠. If the functions $x^{c-1/2}\,f_{1}(x)$ and $x^{1/2-c}\,f_{2}(x)$ are also square-integrable over the interval ⁠ $(0,\infty )$ ⁠, then Parseval's formula holds: $\int _{0}^{\infty }f_{1}(x)\,f_{2}(x)\,dx={\frac {1}{2\pi i}}\int _{c-i\infty }^{c+i\infty }{\tilde {f_{1}}}(s)\,{\tilde {f_{2}}}(1-s)\,ds$ The integration on the right hand side is done along the vertical line $\Re r=c$ that lies entirely within the overlap of the (suitable transformed) fundamental strips.

We can replace $f_{2}(x)$ by ⁠ $f_{2}(x)\,x^{s_{0}-1}$ ⁠. This gives following alternative form of the theorem: Let $f_{1}(x)$ and $f_{2}(x)$ be functions with well-defined Mellin transforms ${\tilde {f}}_{1,2}(s)={\mathcal {M}}\{f_{1,2}\}(s)$ in the fundamental strips ⁠ $\alpha _{1,2}<\Re s<\beta _{1,2}$ ⁠. Let $c\in \mathbb {R}$ with $\alpha _{1}<c<\beta _{1}$ and choose $s_{0}\in \mathbb {C}$ with ⁠ $\alpha _{2}<\Re s_{0}-c<\beta _{2}$ ⁠. If the functions $x^{c-1/2}\,f_{1}(x)$ and $x^{s_{0}-c-1/2}\,f_{2}(x)$ are also square-integrable over the interval $(0,\infty )$ , then we have $\int _{0}^{\infty }f_{1}(x)\,f_{2}(x)\,x^{s_{0}-1}\,dx={\frac {1}{2\pi i}}\int _{c-i\infty }^{c+i\infty }{\tilde {f_{1}}}(s)\,{\tilde {f_{2}}}(s_{0}-s)\,ds$ We can replace $f_{2}(x)$ by ⁠ ${\overline {f_{1}(x)}}$ ⁠. This gives following theorem: Let $f(x)$ be a function with well-defined Mellin transform ${\tilde {f}}(s)={\mathcal {M}}\{f\}(s)$ in the fundamental strip ⁠ $\alpha <\Re s<\beta$ ⁠. Let $c\in \mathbb {R}$ with ⁠ $\alpha <c<\beta$ ⁠. If the function $x^{c-1/2}\,f(x)$ is also square-integrable over the interval ⁠ $(0,\infty )$ ⁠, then Plancherel's theorem holds: $\int _{0}^{\infty }|f(x)|^{2}\,x^{2c-1}dx={\frac {1}{2\pi }}\int _{-\infty }^{\infty }|{\tilde {f}}(c+it)|^{2}\,dt$

## As an isometry on *L*2 spaces

In the study of Hilbert spaces, the Mellin transform is often posed in a slightly different way. For functions in $L^{2}(0,\infty )$ (see *L**p* space) the fundamental strip always includes ⁠ ${\tfrac {1}{2}}+i\mathbb {R}$ ⁠, so we may define a linear operator ${\tilde {\mathcal {M}}}$ as ${\tilde {\mathcal {M}}}\colon L^{2}(0,\infty )\to L^{2}(-\infty ,\infty ),$ $\{{\tilde {\mathcal {M}}}f\}(s):={\frac {1}{\sqrt {2\pi }}}\int _{0}^{\infty }x^{-{\frac {1}{2}}+is}f(x)\,dx.$ In other words, we have set $\{{\tilde {\mathcal {M}}}f\}(s):={\tfrac {1}{\sqrt {2\pi }}}\{{\mathcal {M}}f\}({\tfrac {1}{2}}+is).$ This operator is usually denoted by just plain ${\mathcal {M}}$ and called the "Mellin transform", but ${\tilde {\mathcal {M}}}$ is used here to distinguish from the definition used elsewhere in this article. The Mellin inversion theorem then shows that ${\tilde {\mathcal {M}}}$ is invertible with inverse ${\tilde {\mathcal {M}}}^{-1}\colon L^{2}(-\infty ,\infty )\to L^{2}(0,\infty ),$ $\{{\tilde {\mathcal {M}}}^{-1}\varphi \}(x)={\frac {1}{\sqrt {2\pi }}}\int _{-\infty }^{\infty }x^{-{\frac {1}{2}}-is}\varphi (s)\,ds.$ Furthermore, this operator is an isometry, that is to say $\|{\tilde {\mathcal {M}}}f\|_{L^{2}(-\infty ,\infty )}=\|f\|_{L^{2}(0,\infty )}$ for all $f\in L^{2}(0,\infty )$ (this explains why the factor of $1/{\sqrt {2\pi }}$ was used).

## In probability theory

In probability theory, the Mellin transform is an essential tool in studying the distributions of products of random variables. If ⁠ X ⁠ is a random variable, and ⁠ $X^{+}=\max\{X,0\}$ ⁠ denotes its positive part, while ⁠ $X^{-}=\max\{-X,0\}$ ⁠ is its negative part, then the *Mellin transform* of ⁠ X ⁠ is defined as ${\mathcal {M}}_{X}(s)=\int _{0}^{\infty }x^{s}dF_{X^{+}}(x)+\gamma \int _{0}^{\infty }x^{s}dF_{X^{-}}(x),$ where ⁠ $\gamma$ ⁠ is a formal indeterminate with ⁠ $\gamma ^{2}=1$ ⁠. This transform exists for all ⁠ s ⁠ in some complex strip ⁠ $D=\{s:a\leq \Re (s)\leq b\}$ ⁠, where ⁠ $a\leq 0\leq b$ ⁠.

The Mellin transform ${\mathcal {M}}_{X}(it)$ of a random variable ⁠ X ⁠ uniquely determines its distribution function ⁠ $F_{X}$ ⁠. The importance of the Mellin transform in probability theory lies in the fact that if ⁠ X ⁠ and ⁠ Y ⁠ are two independent random variables, then the Mellin transform of their product is equal to the product of the Mellin transforms of ⁠ X ⁠ and ⁠ Y ⁠: ${\mathcal {M}}_{XY}(s)={\mathcal {M}}_{X}(s){\mathcal {M}}_{Y}(s)$

## Problems with Laplacian in cylindrical coordinate system

In the Laplacian in cylindrical coordinates in a generic dimension (orthogonal coordinates with one angle and one radius, and the remaining lengths) there is always a term: ${\frac {1}{r}}{\frac {\partial }{\partial r}}\left(r{\frac {\partial f}{\partial r}}\right)=f_{rr}+{\frac {f_{r}}{r}}$

For example, in 2-D polar coordinates the Laplacian is: $\nabla ^{2}f={\frac {1}{r}}{\frac {\partial }{\partial r}}\left(r{\frac {\partial f}{\partial r}}\right)+{\frac {1}{r^{2}}}{\frac {\partial ^{2}f}{\partial \theta ^{2}}}$ and in 3-D cylindrical coordinates the Laplacian is, $\nabla ^{2}f={\frac {1}{r}}{\frac {\partial }{\partial r}}\left(r{\frac {\partial f}{\partial r}}\right)+{\frac {1}{r^{2}}}{\frac {\partial ^{2}f}{\partial \varphi ^{2}}}+{\frac {\partial ^{2}f}{\partial z^{2}}}.$

This term can be treated with the Mellin transform, since: ${\mathcal {M}}\left(r^{2}f_{rr}+rf_{r},r\to s\right)=s^{2}{\mathcal {M}}\left(f,r\to s\right)=s^{2}F$

For example, the 2-D Laplace equation in polar coordinates is the PDE in two variables: $r^{2}f_{rr}+rf_{r}+f_{\theta \theta }=0$ and by multiplication: ${\frac {1}{r}}{\frac {\partial }{\partial r}}\left(r{\frac {\partial f}{\partial r}}\right)+{\frac {1}{r^{2}}}{\frac {\partial ^{2}f}{\partial \theta ^{2}}}=0$ with a Mellin transform on radius becomes the simple harmonic oscillator: $F_{\theta \theta }+s^{2}F=0$ with general solution: $F(s,\theta )=C_{1}(s)\cos(s\theta )+C_{2}(s)\sin(s\theta )$

Now let's impose for example some simple wedge boundary conditions to the original Laplace equation: $f(r,-\theta _{0})=a(r),\quad f(r,\theta _{0})=b(r)$ these are particularly simple for Mellin transform, becoming: $F(s,-\theta _{0})=A(s),\quad F(s,\theta _{0})=B(s)$

These conditions imposed to the solution particularize it to: $F(s,\theta )=A(s){\frac {\sin(s(\theta _{0}-\theta ))}{\sin(2\theta _{0}s)}}+B(s){\frac {\sin(s(\theta _{0}+\theta ))}{\sin(2\theta _{0}s)}}$

Now by the convolution theorem for Mellin transform, the solution in the Mellin domain can be inverted: $f(r,\theta )={\frac {r^{m}\cos(m\theta )}{2\theta _{0}}}\int _{0}^{\infty }\left({\frac {a(x)}{x^{2m}+2r^{m}x^{m}\sin(m\theta )+r^{2m}}}+{\frac {b(x)}{x^{2m}-2r^{m}x^{m}\sin(m\theta )+r^{2m}}}\right)x^{m-1}\,dx$ where the following inverse transform relation was employed: ${\mathcal {M}}^{-1}\left({\frac {\sin(s\varphi )}{\sin(2\theta _{0}s)}};s\to r\right)={\frac {1}{2\theta _{0}}}{\frac {r^{m}\sin(m\varphi )}{1+2r^{m}\cos(m\varphi )+r^{2m}}}$ where $m={\frac {\pi }{2\theta _{0}}}$ .

## Applications

The Mellin transform is widely used in computer science for the analysis of algorithms because of its scale invariance property. The magnitude of the Mellin Transform of a scaled function is identical to the magnitude of the original function for purely imaginary inputs. This scale invariance property is analogous to the Fourier Transform's shift invariance property. The magnitude of a Fourier transform of a time-shifted function is identical to the magnitude of the Fourier transform of the original function.

This property is useful in image recognition. An image of an object is easily scaled when the object is moved towards or away from the camera.

In quantum mechanics and especially quantum field theory, Fourier space is enormously useful and used extensively because momentum and position are Fourier transforms of each other (for instance, Feynman diagrams are much more easily computed in momentum space). In 2011, A. Liam Fitzpatrick, Jared Kaplan, João Penedones, Suvrat Raju, and Balt C. van Rees showed that Mellin space serves an analogous role in the context of the AdS/CFT correspondence.

## Examples

- Perron's formula describes the inverse Mellin transform applied to a Dirichlet series.
- The Mellin transform is used in analysis of the prime-counting function and occurs in discussions of the Riemann zeta function.
- Inverse Mellin transforms commonly occur in Riesz means.
- The Mellin transform can be used in audio timescale-pitch modification .

## Table of selected Mellin transforms

Below is a list of interesting examples for the Mellin transform:

| Function $f(x)$ | Mellin transform ${\tilde {f}}(s)={\mathcal {M}}\{f\}(s)$ | Region of convergence | Comment |
|---|---|---|---|
| $e^{-x}$ | $\Gamma (s)$ | $0<\Re s<\infty$ |   |
| $e^{-x}-1$ | $\Gamma (s)$ | $-1<\Re s<0$ |   |
| $e^{-x}-1+x$ | $\Gamma (s)$ | $-2<\Re s<-1$ | Generally $\Gamma (s)$ is the Mellin transform of ⁠ $\textstyle e^{-x}-\sum _{n=0}^{N-1}{\frac {(-1)^{n}}{n!}}x^{n}$ ⁠, for $-N<\Re s<-N+1$ |
| $e^{-x^{2}}$ | ${\tfrac {1}{2}}\Gamma ({\tfrac {1}{2}}s)$ | $0<\Re s<\infty$ |   |
| $\mathrm {erfc} (x)$ | ${\frac {\Gamma ({\tfrac {1}{2}}(1+s))}{{\sqrt {\pi }}\;s}}$ | $0<\Re s<\infty$ |   |
| $e^{-(\ln x)^{2}}$ | ${\sqrt {\pi }}\,e^{{\tfrac {1}{4}}s^{2}}$ | $-\infty <\Re s<\infty$ |   |
| $\delta (x-a)$ | $a^{s-1}$ | $-\infty <\Re s<\infty$ | $a>0,\;\delta (x)$ is the Dirac delta function |
| $u(1-x)=\left\{{\begin{aligned}&1&&\;{\text{if}}\;0<x<1&\\&0&&\;{\text{if}}\;1<x<\infty &\end{aligned}}\right.$ | ${\frac {1}{s}}$ | $0<\Re s<\infty$ | $u(x)$ is the Heaviside step function |
| $-u(x-1)=\left\{{\begin{aligned}&0&&\;{\text{if}}\;0<x<1&\\&-1&&\;{\text{if}}\;1<x<\infty &\end{aligned}}\right.$ | ${\frac {1}{s}}$ | $-\infty <\Re s<0$ |   |
| $u(1-x)\,x^{a}=\left\{{\begin{aligned}&x^{a}&&\;{\text{if}}\;0<x<1&\\&0&&\;{\text{if}}\;1<x<\infty &\end{aligned}}\right.$ | ${\frac {1}{s+a}}$ | $-\Re a<\Re s<\infty$ |   |
| $-u(x-1)\,x^{a}=\left\{{\begin{aligned}&0&&\;{\text{if}}\;0<x<1&\\&-x^{a}&&\;{\text{if}}\;1<x<\infty &\end{aligned}}\right.$ | ${\frac {1}{s+a}}$ | $-\infty <\Re s<-\Re a$ |   |
| $u(1-x)\,x^{a}\ln x=\left\{{\begin{aligned}&x^{a}\ln x&&\;{\text{if}}\;0<x<1&\\&0&&\;{\text{if}}\;1<x<\infty &\end{aligned}}\right.$ | ${\frac {1}{(s+a)^{2}}}$ | $-\Re a<\Re s<\infty$ |   |
| $-u(x-1)\,x^{a}\ln x=\left\{{\begin{aligned}&0&&\;{\text{if}}\;0<x<1&\\&-x^{a}\ln x&&\;{\text{if}}\;1<x<\infty &\end{aligned}}\right.$ | ${\frac {1}{(s+a)^{2}}}$ | $-\infty <\Re s<-\Re a$ |   |
| ${\frac {1}{1+x}}$ | ${\frac {\pi }{\sin(\pi s)}}$ | $0<\Re s<1$ |   |
| ${\frac {1}{1-x}}$ | ${\frac {\pi }{\tan(\pi s)}}$ | $0<\Re s<1$ | The integral uses the Cauchy principal value. |
| ${\frac {1}{1+x^{2}}}$ | ${\frac {\pi }{2\sin({\tfrac {1}{2}}\pi s)}}$ | $0<\Re s<2$ |   |
| ${\frac {1}{(1+x)^{a}}}$ | ${\frac {\Gamma (s)\,\Gamma (a-s)}{\Gamma (a)}}$ | $0<\Re s<\Re a$ | Binomial series |
| $u(1-x)\;(1-x)^{a-1}$ | ${\frac {\Gamma (s)\,\Gamma (a)}{\Gamma (s+a)}}$ | $0<\Re s<\infty$ | $\Re a>0$ |
| $u(x-1)\;(1-x)^{-a}$ | ${\frac {\Gamma (a-s)\,\Gamma (1-a)}{\Gamma (1-s)}}$ | $-\infty <\Re s<\Re a$ | $\Re a<1$ |
| $\ln(1+x)$ | ${\frac {\pi }{s\,\sin(\pi s)}}$ | $-1<\Re s<0$ |   |
| $\ln \vert 1-x\vert$ | ${\frac {\pi }{s}}\,\cot(\pi s)$ | $-1<\Re s<0$ |   |
| $\operatorname {acot} x={\frac {\pi }{2}}-\operatorname {atan} x$ | ${\frac {\pi }{2s\,\cos(\pi s/2)}}$ | $0<\Re s<1$ |   |
| $\sin(x)$ | $\sin({\tfrac {1}{2}}\pi s)\,\Gamma (s)$ | $-1<\Re s<1$ |   |
| $\cos(x)$ | $\cos({\tfrac {1}{2}}\pi s)\,\Gamma (s)$ | $0<\Re s<1$ |   |
| $e^{ix}$ | $e^{i\pi s/2}\,\Gamma (s)$ | $0<\Re s<1$ |   |
| $J_{0}(x)$ | ${\frac {2^{s-1}}{\pi }}\,\sin(\pi s/2)\,\left[\Gamma (s/2)\right]^{2}$ | $0<\Re s<{\tfrac {3}{2}}$ | $J_{0}(x)$ is the Bessel function of the first kind. |
| $Y_{0}(x)$ | $-{\frac {2^{s-1}}{\pi }}\,\cos(\pi s/2)\,\left[\Gamma (s/2)\right]^{2}$ | $0<\Re s<{\tfrac {3}{2}}$ | $Y_{0}(x)$ is the Bessel function of the second kind |
| $K_{0}(x)$ | $2^{s-2}\,\left[\Gamma (s/2)\right]^{2}$ | $0<\Re s<\infty$ | $K_{0}(x)$ is the modified Bessel function of the second kind |
