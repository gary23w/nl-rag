---
title: "Sobolev space"
source: https://en.wikipedia.org/wiki/Sobolev_space
domain: partial-differential-equations-theory
license: CC-BY-SA-4.0
tags: partial differential equation, heat equation, wave equation, sobolev space
fetched: 2026-07-02
---

# Sobolev space

In mathematics, a **Sobolev space** is a vector space of functions equipped with a norm that is a combination of *Lp*-norms of the function together with its derivatives up to a given order. The derivatives are understood in a suitable weak sense to make the space complete, i.e. a Banach space. Intuitively, a Sobolev space is a space of functions possessing sufficiently many derivatives for some application domain, such as partial differential equations, and equipped with a norm that measures both the size and regularity of a function.

Sobolev spaces are named after the Russian mathematician Sergei Sobolev. Their importance comes from the fact that weak solutions of some important partial differential equations exist in appropriate Sobolev spaces, even when there are no strong solutions in spaces of continuous functions with the derivatives understood in the classical sense.

## Motivation

Throughout the article, $\Omega$ is an open subset of $\mathbb {R} ^{n}.$

There are many criteria for smoothness of mathematical functions. The most basic criterion may be that of continuity. A stronger notion of smoothness is that of differentiability (because functions that are differentiable are also continuous) and a yet stronger notion of smoothness is that the derivative also be continuous (these functions are said to be of class $C^{1}$ — see Differentiability classes). Differentiable functions are important in many areas, and in particular for differential equations. In the twentieth century, however, it was observed that the space $C^{1}$ (or $C^{2}$ , etc.) was not exactly the right space to study solutions of differential equations. The Sobolev spaces are the modern replacement for these spaces in which to look for solutions of partial differential equations.

Quantities or properties of the underlying model of the differential equation are usually expressed in terms of integral norms. A typical example is measuring the energy of a temperature or velocity distribution by an $L^{2}$ -norm. It is therefore important to develop a tool for differentiating Lebesgue space functions.

The integration by parts formula yields that for every $u\in C^{k}(\Omega )$ , where k is a natural number, and for all infinitely differentiable functions with compact support $\varphi \in C_{c}^{\infty }(\Omega ),$

$\int _{\Omega }u\,D^{\alpha \!}\varphi \,dx=(-1)^{|\alpha |}\int _{\Omega }\varphi \,D^{\alpha \!}u\,dx,$

where $\alpha =(\alpha _{1},...,\alpha _{n})$ is a multi-index of order $|\alpha |=k$ and we are using the notation:

$D^{\alpha \!}f={\frac {\partial ^{|\alpha |}\!f}{\partial x_{1}^{\alpha _{1}}\dots \partial x_{n}^{\alpha _{n}}}}.$

The left-hand side of this equation still makes sense if we assume u to be only locally integrable. If there exists a locally integrable function v , such that

$\int _{\Omega }u\,D^{\alpha \!}\varphi \;dx=(-1)^{|\alpha |}\int _{\Omega }\varphi \,v\;dx\qquad {\text{for all }}\varphi \in C_{c}^{\infty }(\Omega ),$

then we call v the weak $\alpha$ -th partial derivative of u . If there exists a weak $\alpha$ -th partial derivative of u , then it is uniquely defined almost everywhere, and thus it is uniquely determined as an element of a Lebesgue space. On the other hand, if $u\in C^{k}(\Omega )$ , then the classical and the weak derivative coincide. Thus, if v is a weak $\alpha$ -th partial derivative of u , we may denote it by $D^{\alpha }u:=v$ .

For example, the function

$u(x)={\begin{cases}1+x&-1<x<0\\10&x=0\\1-x&0<x<1\\0&{\text{else}}\end{cases}}$

is not continuous at zero, and not differentiable at −1, 0, or 1. Yet the function

$v(x)={\begin{cases}1&-1<x<0\\-1&0<x<1\\0&{\text{else}}\end{cases}}$

satisfies the definition for being the weak derivative of $u(x),$ which then qualifies as being in the Sobolev space $W^{1,p}$ (for any allowed p , see definition below).

The Sobolev spaces $W^{k,p}(\Omega )$ combine the concepts of weak differentiability and Lebesgue norms.

## Sobolev spaces with integer *k*

### One-dimensional case

In the one-dimensional case the Sobolev space $W^{k,p}(\mathbb {R} )$ for $1\leq p\leq \infty$ is defined as the subset of functions f in $L^{p}(\mathbb {R} )$ such that f and its weak derivatives up to order k have a finite *Lp* norm. As mentioned above, some care must be taken to define derivatives in the proper sense. In the one-dimensional problem it is enough to assume that the $(k{-}1)$ -th derivative $f^{(k-1)}$ is differentiable almost everywhere and is equal almost everywhere to the Lebesgue integral of its derivative (this excludes irrelevant examples such as Cantor's function).

With this definition, the Sobolev spaces admit a natural norm,

$\|f\|_{k,p}=\left(\sum _{i=0}^{k}\left\|f^{(i)}\right\|_{p}^{p}\right)^{\frac {1}{p}}=\left(\sum _{i=0}^{k}\int \left|f^{(i)}(t)\right|^{p}\,dt\right)^{\frac {1}{p}}.$

One can extend this to the case $p=\infty$ , with the norm then defined using the essential supremum by

$\|f\|_{k,\infty }=\max _{i=0,\ldots ,k}\left\|f^{(i)}\right\|_{\infty }=\max _{i=0,\ldots ,k}\left({\text{ess}}\,\sup _{t}\left|f^{(i)}(t)\right|\right).$

Equipped with the norm $\|\cdot \|_{k,p},W^{k,p}$ becomes a Banach space. It turns out that it is enough to take only the first and last in the sequence, i.e., the norm defined by

$\left\|f^{(k)}\right\|_{p}+\|f\|_{p}$

is equivalent to the norm above (i.e., the induced topologies of the norms are the same).

#### The case *p* = 2

Sobolev spaces with *p* = 2 are especially important because of their connection with Fourier series and because they form a Hilbert space. A special notation has arisen to cover this case, since the space is a Hilbert space:

$H^{k}=W^{k,2}.$

The space $H^{k}$ can be defined naturally in terms of Fourier series whose coefficients decay sufficiently rapidly, namely,

$H^{k}(\mathbb {T} )={\Big \{}f\in L^{2}(\mathbb {T} ):\sum _{n=-\infty }^{\infty }\left(1+n^{2}+n^{4}+\dots +n^{2k}\right)\left|{\widehat {f}}(n)\right|^{2}<\infty {\Big \}},$

where ${\widehat {f}}$ is the Fourier series of $f,$ and $\mathbb {T}$ denotes the 1-torus. As above, one can use the equivalent norm

$\|f\|_{k,2}^{2}=\sum _{n=-\infty }^{\infty }\left(1+|n|^{2}\right)^{k}\left|{\widehat {f}}(n)\right|^{2}.$

Both representations follow easily from Parseval's theorem and the fact that differentiation is equivalent to multiplying the Fourier coefficient by $in$ .

Furthermore, the space $H^{k}$ admits an inner product, like the space $H^{0}=L^{2}.$ In fact, the $H^{k}$ inner product is defined in terms of the $L^{2}$ inner product:

$\langle u,v\rangle _{H^{k}}=\sum _{i=0}^{k}\left\langle D^{i}u,D^{i}v\right\rangle _{L^{2}}.$

The space $H^{k}$ becomes a Hilbert space with this inner product.

#### Other examples

In one dimension, some other Sobolev spaces permit a simpler description. For example, $W^{1,1}(0,1)$ is the space of absolutely continuous functions on (0, 1) (or rather, equivalence classes of functions that are equal almost everywhere to such), while $W^{1,\infty }(I)$ is the space of bounded Lipschitz functions on I, for every interval I. However, these properties are lost or not as simple for functions of more than one variable.

All spaces $W^{k,\infty }$ are (normed) algebras, i.e. the product of two elements is once again a function of this Sobolev space, which is not the case for $p<\infty .$ (E.g., functions behaving like |*x*|−1/3 at the origin are in $L^{2},$ but the product of two such functions is not in $L^{2}$ ).

### Multidimensional case

The transition to multiple dimensions brings more difficulties, starting from the very definition. The requirement that $f^{(k-1)}$ be the integral of $f^{(k)}$ does not generalize, and the simplest solution is to consider derivatives in the sense of distribution theory.

A formal definition now follows. Let $k\in \mathbb {N} ,1\leqslant p\leqslant \infty .$ The Sobolev space $W^{k,p}(\Omega )$ is defined to be the set of all functions f on $\Omega$ such that for every multi-index $\alpha$ with $|\alpha |\leqslant k,$ the mixed partial derivative

$f^{(\alpha )}={\frac {\partial ^{|\alpha |\!}f}{\partial x_{1}^{\alpha _{1}}\dots \partial x_{n}^{\alpha _{n}}}}$

exists in the weak sense and is in $L^{p}(\Omega ),$ i.e.

$\left\|f^{(\alpha )}\right\|_{L^{p}}<\infty .$

That is, the Sobolev space $W^{k,p}(\Omega )$ is defined as

$W^{k,p}(\Omega )=\left\{u\in L^{p}(\Omega ):D^{\alpha }u\in L^{p}(\Omega )\,\,\forall |\alpha |\leqslant k\right\}.$

The natural number k is called the order of the Sobolev space $W^{k,p}(\Omega ).$

There are several choices for a norm for $W^{k,p}(\Omega ).$ The following two are common and are equivalent in the sense of equivalence of norms:

${\displaystyle \|u\|_{W^{k,p}(\Omega )}:={\begin{cases}\left(\sum _{|\alpha |\leqslant k}\left\|D^{\alpha }u\right\|_{L^{p}(\Omega )}^{p}\right)^{\frac {1}{p}}&1\leqslant p<\infty$

and

${\displaystyle \|u\|'_{W^{k,p}(\Omega )}:={\begin{cases}\sum _{|\alpha |\leqslant k}\left\|D^{\alpha }u\right\|_{L^{p}(\Omega )}&1\leqslant p<\infty$

With respect to either of these norms, $W^{k,p}(\Omega )$ is a Banach space. For $p<\infty ,W^{k,p}(\Omega )$ is also a separable space. It is conventional to denote $W^{k,2}(\Omega )$ by $H^{k}(\Omega )$ for it is a Hilbert space with the norm $\|\cdot \|_{W^{k,2}(\Omega )}$ .

#### Approximation by smooth functions

It is rather hard to work with Sobolev spaces relying only on their definition. It is therefore interesting to know that by the Meyers–Serrin theorem a function $u\in W^{k,p}(\Omega )$ can be approximated by smooth functions. This fact often allows us to translate properties of smooth functions to Sobolev functions. If p is finite and $\Omega$ is open, then there exists for any $u\in W^{k,p}(\Omega )$ an approximating sequence of functions $u_{m}\in C^{\infty }(\Omega )$ such that:

$\left\|u_{m}-u\right\|_{W^{k,p}(\Omega )}\to 0.$

If $\Omega$ has Lipschitz boundary, we may even assume that the $u_{m}$ are the restriction of smooth functions with compact support on all of $\mathbb {R} ^{n}.$

#### Examples

In higher dimensions, it is no longer true that, for example, $W^{1,1}$ contains only continuous functions. For example, $|x|^{-1}\in W^{1,1}(\mathbb {B} ^{3})$ where $\mathbb {B} ^{3}$ is the unit ball in three dimensions. For $k>n/p$ , the space $W^{k,p}(\Omega )$ will contain only continuous functions, but for which k this is already true depends both on p and on the dimension. For example, as can be easily checked using spherical polar coordinates for the function $f:\mathbb {B} ^{n}\to \mathbb {R} \cup \{\infty \}$ defined on the *n*-dimensional unit ball we have:

$f(x)=|x|^{-\alpha }\in W^{k,p}(\mathbb {B} ^{n})\Longleftrightarrow \alpha <{\tfrac {n}{p}}-k.$

Intuitively, the blow-up of *f* at 0 "counts for less" when *n* is large since the unit ball has "more outside and less inside" in higher dimensions.

#### Absolutely continuous on lines (ACL) characterization of Sobolev functions

Let $1\leqslant p\leqslant \infty .$ If a function is in $W^{1,p}(\Omega ),$ then, possibly after modifying the function on a set of measure zero, the restriction to almost every line parallel to the coordinate directions in $\mathbb {R} ^{n}$ is absolutely continuous; what's more, the classical derivative along the lines that are parallel to the coordinate directions are in $L^{p}(\Omega ).$ Conversely, if the restriction of f to almost every line parallel to the coordinate directions is absolutely continuous, then the pointwise gradient $\nabla f$ exists almost everywhere, and f is in $W^{1,p}(\Omega )$ provided $f,|\nabla f|\in L^{p}(\Omega ).$ In particular, in this case the weak partial derivatives of f and pointwise partial derivatives of f agree almost everywhere. The ACL characterization of the Sobolev spaces was established by Otto M. Nikodym (1933); see (Maz'ya 2011, §1.1.3).

A stronger result holds when $p>n.$ A function in $W^{1,p}(\Omega )$ is, after modifying on a set of measure zero, Hölder continuous of exponent $\gamma =1-{\tfrac {n}{p}},$ by Morrey's inequality. In particular, if $p=\infty$ and $\Omega$ has Lipschitz boundary, then the function is Lipschitz continuous.

#### Functions vanishing at the boundary

The Sobolev space $W^{1,2}(\Omega )$ is also denoted by $H^{1}\!(\Omega ).$ It is a Hilbert space, with an important subspace $H_{0}^{1}\!(\Omega )$ defined to be the closure of the infinitely differentiable functions compactly supported in $\Omega$ in $H^{1}\!(\Omega ).$ The Sobolev norm defined above reduces here to

$\|f\|_{H^{1}}=\left(\int _{\Omega }\!|f|^{2}\!+\!|\nabla \!f|^{2}\right)^{\!{\frac {1}{2}}}.$

When $\Omega$ has a regular boundary, $H_{0}^{1}\!(\Omega )$ can be described as the space of functions in $H^{1}\!(\Omega )$ that vanish at the boundary, in the sense of traces (see below). When $n=1,$ if $\Omega =(a,b)$ is a bounded interval, then $H_{0}^{1}(a,b)$ consists of continuous functions on $[a,b]$ of the form

$f(x)=\int _{a}^{x}f'(t)\,\mathrm {d} t,\qquad x\in [a,b]$

where the generalized derivative $f'$ is in $L^{2}(a,b)$ and has 0 integral, so that $f(b)=f(a)=0.$

When $\Omega$ is bounded, the Poincaré inequality states that there is a constant $C=C(\Omega )$ such that:

$\int _{\Omega }|f|^{2}\leqslant C^{2}\int _{\Omega }|\nabla f|^{2},\qquad f\in H_{0}^{1}(\Omega ).$

When $\Omega$ is bounded, the injection from $H_{0}^{1}\!(\Omega )$ to $L^{2}\!(\Omega ),$ is compact. This fact plays a role in the study of the Dirichlet problem, and in the fact that there exists an orthonormal basis of $L^{2}(\Omega )$ consisting of eigenvectors of the Laplace operator (with Dirichlet boundary condition).

## Traces

Sobolev spaces are often considered when investigating partial differential equations. It is essential to consider boundary values of Sobolev functions. If $u\in C(\Omega )$ , those boundary values are described by the restriction $u|_{\partial \Omega }.$ However, it is not clear how to describe values at the boundary for $u\in W^{k,p}(\Omega ),$ as the *n*-dimensional measure of the boundary is zero. The following theorem resolves the problem:

**Trace theorem**—Assume Ω is bounded with Lipschitz boundary. Then there exists a bounded linear operator $T:W^{1,p}(\Omega )\to L^{p}(\partial \Omega )$ such that ${\begin{aligned}Tu&=u|_{\partial \Omega }&&u\in W^{1,p}(\Omega )\cap C({\overline {\Omega }})\\\|Tu\|_{L^{p}(\partial \Omega )}&\leqslant c(p,\Omega )\|u\|_{W^{1,p}(\Omega )}&&u\in W^{1,p}(\Omega ).\end{aligned}}$

*Tu* is called the trace of *u*. Roughly speaking, this theorem extends the restriction operator to the Sobolev space $W^{1,p}(\Omega )$ for well-behaved Ω. Note that the trace operator *T* is in general not surjective, but for 1 < *p* < ∞ it maps continuously onto the Sobolev–Slobodeckij space $W^{1-{\frac {1}{p}},p}(\partial \Omega ).$

Intuitively, taking the trace costs 1/*p* of a derivative. The functions *u* in *W*1,p(Ω) with zero trace, i.e. *Tu* = 0, can be characterized by the equality

$W_{0}^{1,p}(\Omega )=\left\{u\in W^{1,p}(\Omega ):Tu=0\right\},$

where

$W_{0}^{1,p}(\Omega ):=\left\{u\in W^{1,p}(\Omega ):\exists \{u_{m}\}_{m=1}^{\infty }\subset C_{c}^{\infty }(\Omega ),\ {\text{such that}}\ u_{m}\to u\ {\textrm {in}}\ W^{1,p}(\Omega )\right\}.$

In other words, for Ω bounded with Lipschitz boundary, trace-zero functions in $W^{1,p}(\Omega )$ can be approximated by smooth functions with compact support.

## Sobolev spaces with non-integer *k*

### Bessel potential spaces

For a natural number *k* and 1 < *p* < ∞ one can show (by using Fourier multipliers) that the space $W^{k,p}(\mathbb {R} ^{n})$ can equivalently be defined as

$W^{k,p}(\mathbb {R} ^{n})=H^{k,p}(\mathbb {R} ^{n}):={\Big \{}f\in L^{p}(\mathbb {R} ^{n}):{\mathcal {F}}^{-1}{\Big [}{\big (}1+|\xi |^{2}{\big )}^{\frac {k}{2}}{\mathcal {F}}f{\Big ]}\in L^{p}(\mathbb {R} ^{n}){\Big \}},$

with the norm

$\|f\|_{H^{k,p}(\mathbb {R} ^{n})}:=\left\|{\mathcal {F}}^{-1}{\Big [}{\big (}1+|\xi |^{2}{\big )}^{\frac {k}{2}}{\mathcal {F}}f{\Big ]}\right\|_{L^{p}(\mathbb {R} ^{n})}.$

This motivates Sobolev spaces with non-integer order since in the above definition we can replace *k* by any real number *s*. The resulting spaces

$H^{s,p}(\mathbb {R} ^{n}):=\left\{f\in {\mathcal {S}}'(\mathbb {R} ^{n}):{\mathcal {F}}^{-1}\left[{\big (}1+|\xi |^{2}{\big )}^{\frac {s}{2}}{\mathcal {F}}f\right]\in L^{p}(\mathbb {R} ^{n})\right\}$

are called Bessel potential spaces (named after Friedrich Bessel). They are Banach spaces in general and Hilbert spaces in the special case *p* = 2.

For $s\geq 0,H^{s,p}(\Omega )$ is the set of restrictions of functions from $H^{s,p}(\mathbb {R} ^{n})$ to Ω equipped with the norm

$\|f\|_{H^{s,p}(\Omega )}:=\inf \left\{\|g\|_{H^{s,p}(\mathbb {R} ^{n})}:g\in H^{s,p}(\mathbb {R} ^{n}),g|_{\Omega }=f\right\}.$

Again, *Hs,p*(Ω) is a Banach space and in the case *p* = 2 a Hilbert space.

Using extension theorems for Sobolev spaces, it can be shown that also *Wk,p*(Ω) = *Hk,p*(Ω) holds in the sense of equivalent norms, if Ω is domain with uniform *Ck*-boundary, *k* a natural number and 1 < *p* < ∞. By the embeddings

$H^{k+1,p}(\mathbb {R} ^{n})\hookrightarrow H^{s',p}(\mathbb {R} ^{n})\hookrightarrow H^{s,p}(\mathbb {R} ^{n})\hookrightarrow H^{k,p}(\mathbb {R} ^{n}),\quad k\leqslant s\leqslant s'\leqslant k+1$

the Bessel potential spaces $H^{s,p}(\mathbb {R} ^{n})$ form a continuous scale between the Sobolev spaces $W^{k,p}(\mathbb {R} ^{n}).$ From an abstract point of view, the Bessel potential spaces occur as complex interpolation spaces of Sobolev spaces, i.e. in the sense of equivalent norms it holds that

$\left[W^{k,p}(\mathbb {R} ^{n}),W^{k+1,p}(\mathbb {R} ^{n})\right]_{\theta }=H^{s,p}(\mathbb {R} ^{n}),$

where:

$1\leqslant p\leqslant \infty ,\ 0<\theta <1,\ s=(1-\theta )k+\theta (k+1)=k+\theta .$

### Sobolev–Slobodeckij spaces

Another approach to define fractional order Sobolev spaces arises from the idea to generalize the Hölder condition to the *Lp*-setting. For $1\leqslant p<\infty ,\theta \in (0,1)$ and $f\in L^{p}(\Omega ),$ the **Slobodeckij seminorm** (roughly analogous to the Hölder seminorm) is defined by

$[f]_{\theta ,p,\Omega }:=\left(\int _{\Omega }\int _{\Omega }{\frac {|f(x)-f(y)|^{p}}{|x-y|^{\theta p+n}}}\;dx\;dy\right)^{\frac {1}{p}}.$

Let *s* > 0 be not an integer and set $\theta =s-\lfloor s\rfloor \in (0,1)$ . Using the same idea as for the Hölder spaces, the **Sobolev–Slobodeckij space** $W^{s,p}(\Omega )$ is defined as

$W^{s,p}(\Omega ):=\left\{f\in W^{\lfloor s\rfloor ,p}(\Omega ):\sup _{|\alpha |=\lfloor s\rfloor }[D^{\alpha }f]_{\theta ,p,\Omega }<\infty \right\}.$

It is a Banach space for the norm

$\|f\|_{W^{s,p}(\Omega )}:=\|f\|_{W^{\lfloor s\rfloor ,p}(\Omega )}+\sup _{|\alpha |=\lfloor s\rfloor }[D^{\alpha }f]_{\theta ,p,\Omega }.$

If $\Omega$ is suitably regular in the sense that there exist certain extension operators, then also the Sobolev–Slobodeckij spaces form a scale of Banach spaces, i.e. one has the continuous injections or embeddings

$W^{k+1,p}(\Omega )\hookrightarrow W^{s',p}(\Omega )\hookrightarrow W^{s,p}(\Omega )\hookrightarrow W^{k,p}(\Omega ),\quad k\leqslant s\leqslant s'\leqslant k+1.$

There are examples of irregular Ω such that $W^{1,p}(\Omega )$ is not even a vector subspace of $W^{s,p}(\Omega )$ for 0 < *s* < 1 (see Example 9.1 of )

From an abstract point of view, the spaces $W^{s,p}(\Omega )$ coincide with the real interpolation spaces of Sobolev spaces, i.e. in the sense of equivalent norms the following holds:

$W^{s,p}(\Omega )=\left(W^{k,p}(\Omega ),W^{k+1,p}(\Omega )\right)_{\theta ,p},\quad k\in \mathbb {N} ,s\in (k,k+1),\theta =s-\lfloor s\rfloor .$

Sobolev–Slobodeckij spaces play an important role in the study of traces of Sobolev functions. They are special cases of Besov spaces.

The constant arising in the characterization of the fractional Sobolev space $W^{s,p}(\Omega )$ can be characterized through the Bourgain-Brezis-Mironescu formula:

$\lim _{s\nearrow 1}\;(1-s)\int _{\Omega }\int _{\Omega }{\frac {|f(x)-f(y)|^{p}}{|x-y|^{sp+n}}}\;dx\;dy={\frac {2\pi ^{\frac {n-1}{2}}\Gamma ({\frac {p+1}{2}})}{p\Gamma ({\frac {p+n}{2}})}}\int _{\Omega }\vert \nabla f\vert ^{p};$

and the condition

$\limsup _{s\nearrow 1}\;(1-s)\int _{\Omega }\int _{\Omega }{\frac {|f(x)-f(y)|^{p}}{|x-y|^{sp+n}}}\;dx\;dy<\infty$

characterizes those functions of $L^{p}(\Omega )$ that are in the first-order Sobolev space $W^{1,p}(\Omega )$ .

## Extension operators

If $\Omega$ is a domain whose boundary is not too poorly behaved (e.g., if its boundary is a manifold, or satisfies the more permissive "cone condition") then there is an operator *A* mapping functions of $\Omega$ to functions of $\mathbb {R} ^{n}$ such that:

1. *Au*(*x*) = *u*(*x*) for almost every *x* in $\Omega$ and
2. $A:W^{k,p}(\Omega )\to W^{k,p}(\mathbb {R} ^{n})$ is continuous for any 1 ≤ *p* ≤ ∞ and integer *k*.

We will call such an operator *A* an extension operator for $\Omega .$

### Case of *p* = 2

Extension operators are the most natural way to define $H^{s}(\Omega )$ for non-integer *s* (we cannot work directly on $\Omega$ since taking Fourier transform is a global operation). We define $H^{s}(\Omega )$ by saying that $u\in H^{s}(\Omega )$ if and only if $Au\in H^{s}(\mathbb {R} ^{n}).$ Equivalently, complex interpolation yields the same $H^{s}(\Omega )$ spaces so long as $\Omega$ has an extension operator. If $\Omega$ does not have an extension operator, complex interpolation is the only way to obtain the $H^{s}(\Omega )$ spaces.

As a result, the interpolation inequality still holds.

### Extension by zero

Like above, we define $H_{0}^{s}(\Omega )$ to be the closure in $H^{s}(\Omega )$ of the space $C_{c}^{\infty }(\Omega )$ of infinitely differentiable compactly supported functions. Given the definition of a trace, above, we may state the following

**Theorem**—Let $\Omega$ be uniformly *Cm* regular, *m* ≥ *s* and let *P* be the linear map sending *u* in $H^{s}(\Omega )$ to $\left.\left(u,{\frac {du}{dn}},\dots ,{\frac {d^{k}u}{dn^{k}}}\right)\right|_{G}$ where *d/dn* is the derivative normal to *G*, and *k* is the largest integer less than *s*. Then $H_{0}^{s}$ is precisely the kernel of *P*.

If $u\in H_{0}^{s}(\Omega )$ we may define its **extension by zero** ${\tilde {u}}\in L^{2}(\mathbb {R} ^{n})$ in the natural way, namely

${\tilde {u}}(x)={\begin{cases}u(x)&x\in \Omega \\0&{\text{else}}\end{cases}}$

**Theorem**—Let $s>{\tfrac {1}{2}}.$ The map $u\mapsto {\tilde {u}}$ is continuous into $H^{s}(\mathbb {R} ^{n})$ if and only if *s* is not of the form $n+{\tfrac {1}{2}}$ for *n* an integer.

For *f* ∈ *Lp*(Ω) its extension by zero,

$Ef:={\begin{cases}f&{\textrm {on}}\ \Omega ,\\0&{\textrm {otherwise}}\end{cases}}$

is an element of $L^{p}(\mathbb {R} ^{n}).$ Furthermore,

$\|Ef\|_{L^{p}(\mathbb {R} ^{n})}=\|f\|_{L^{p}(\Omega )}.$

In the case of the Sobolev space *W*1,p(Ω) for 1 ≤ p ≤ ∞, extending a function *u* by zero will not necessarily yield an element of $W^{1,p}(\mathbb {R} ^{n}).$ But if Ω is bounded with Lipschitz boundary (e.g. ∂Ω is *C*1), then for any bounded open set O such that Ω⊂⊂O (i.e. Ω is compactly contained in O), there exists a bounded linear operator

$E:W^{1,p}(\Omega )\to W^{1,p}(\mathbb {R} ^{n}),$

such that for each $u\in W^{1,p}(\Omega ):Eu=u$ a.e. on Ω, *Eu* has compact support within O, and there exists a constant *C* depending only on *p*, Ω, O and the dimension *n*, such that

$\|Eu\|_{W^{1,p}(\mathbb {R} ^{n})}\leqslant C\|u\|_{W^{1,p}(\Omega )}.$

We call $Eu$ an extension of u to $\mathbb {R} ^{n}.$

## Sobolev embeddings

It is a natural question to ask if a Sobolev function is continuous or even continuously differentiable. Roughly speaking, sufficiently many weak derivatives (i.e. large *k*) result in a classical derivative. This idea is generalized and made precise in the Sobolev embedding theorem.

Write $W^{k,p}$ for the Sobolev space of some compact Riemannian manifold of dimension *n*. Here *k* can be any real number, and 1 ≤ *p* ≤ ∞. (For *p* = ∞ the Sobolev space $W^{k,\infty }$ is defined to be the Hölder space *C**n*,α where *k* = *n* + α and 0 < α ≤ 1.) The Sobolev embedding theorem states that if $k\geqslant m$ and $k-{\tfrac {n}{p}}\geqslant m-{\tfrac {n}{q}}$ then

$W^{k,p}\subseteq W^{m,q}$

and the embedding is continuous. Moreover, if $k>m$ and $k-{\tfrac {n}{p}}>m-{\tfrac {n}{q}}$ then the embedding is completely continuous (this is sometimes called Kondrachov's theorem or the Rellich–Kondrachov theorem). Functions in $W^{m,\infty }$ have all derivatives of order less than *m* continuous, so in particular this gives conditions on Sobolev spaces for various derivatives to be continuous. Informally these embeddings say that to convert an *Lp* estimate to a boundedness estimate costs 1/*p* derivatives per dimension.

There are similar variations of the embedding theorem for non-compact manifolds such as $\mathbb {R} ^{n}$ (Stein 1970). Sobolev embeddings on $\mathbb {R} ^{n}$ that are not compact often have a related, but weaker, property of cocompactness.
