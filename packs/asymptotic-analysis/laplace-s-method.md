---
title: "Laplace's method"
source: https://en.wikipedia.org/wiki/Laplace%27s_method
domain: asymptotic-analysis
license: CC-BY-SA-4.0
tags: asymptotic analysis, asymptotic expansion, steepest descent, borel summation
fetched: 2026-07-02
---

# Laplace's method

In mathematics, **Laplace's method**, named after Pierre-Simon Laplace, is a technique used to approximate integrals of the form

$\int _{a}^{b}e^{Mf(x)}\,dx,$

where f is a twice-differentiable function, M is a large number, and the endpoints a and b may be infinite. This technique was originally presented in the book by Laplace (1774).

In Bayesian statistics, Laplace's approximation can refer to either approximating the posterior normalizing constant with Laplace's method or approximating the posterior distribution with a Gaussian centered at the maximum a posteriori estimate. Laplace approximations are used in the integrated nested Laplace approximations method for fast approximations of Bayesian inference.

## Concept

Let the function $f(x)$ have a unique global maximum at $x_{0}$ . $M>0$ is a constant here. The following two functions are considered:

${\begin{aligned}g(x)&=Mf(x),\\h(x)&=e^{Mf(x)}.\end{aligned}}$

Then, $x_{0}$ is the global maximum of g and h as well. Hence:

${\begin{aligned}{\frac {g(x_{0})}{g(x)}}&={\frac {Mf(x_{0})}{Mf(x)}}={\frac {f(x_{0})}{f(x)}},\\[4pt]{\frac {h(x_{0})}{h(x)}}&={\frac {e^{Mf(x_{0})}}{e^{Mf(x)}}}=e^{M(f(x_{0})-f(x))}.\end{aligned}}$

As *M* increases, the ratio for h will grow exponentially, while the ratio for g does not change. Thus, significant contributions to the integral of this function will come only from points x in a neighborhood of $x_{0}$ , which can then be estimated.

## General theory

To state and motivate the method, one must make several assumptions. It is assumed that $x_{0}$ is not an endpoint of the interval of integration and that the values $f(x)$ cannot be very close to $f(x_{0})$ unless x is close to $x_{0}$ .

$f(x)$ can be expanded around $x_{0}$ by Taylor's theorem,

$f(x)=f(x_{0})+f'(x_{0})(x-x_{0})+{\frac {1}{2}}f''(x_{0})(x-x_{0})^{2}+R$

where $R=O\left((x-x_{0})^{3}\right)$ (see: big O notation).

Since f has a global maximum at $x_{0}$ , and $x_{0}$ is not an endpoint, it is a stationary point, i.e. $f'(x_{0})=0$ . Therefore, the second-order Taylor polynomial approximating $f(x)$ is

$f(x)\approx f(x_{0})+{\frac {1}{2}}f''(x_{0})(x-x_{0})^{2}.$

Then, just one more step is needed to get a Gaussian distribution. Since $x_{0}$ is a global maximum of the function f it can be stated, by definition of the second derivative, that $f''(x_{0})\leq 0$ , thus giving the relation

$f(x)\approx f(x_{0})-{\frac {1}{2}}|f''(x_{0})|(x-x_{0})^{2}$

for x close to $x_{0}$ . The integral can then be approximated with:

$\int _{a}^{b}e^{Mf(x)}\,dx\approx e^{Mf(x_{0})}\int _{a}^{b}e^{-{\frac {1}{2}}M|f''(x_{0})|(x-x_{0})^{2}}\,dx$

If $f''(x_{0})<0$ this latter integral becomes a Gaussian integral if we replace the limits of integration by $-\infty$ and $+\infty$ ; when M is large this creates only a small error because the exponential decays very fast away from $x_{0}$ . Computing this Gaussian integral we obtain:

$\int _{a}^{b}e^{Mf(x)}\,dx\approx {\sqrt {\frac {2\pi }{M|f''(x_{0})|}}}e^{Mf(x_{0})}{\text{ as }}M\to \infty .$

A generalization of this method and extension to arbitrary precision is provided by the book Fog (2008).

### Formal statement and proof

Suppose $f(x)$ is a twice continuously differentiable function on $[a,b],$ and there exists a unique point $x_{0}\in (a,b)$ such that:

$f(x_{0})=\max _{x\in [a,b]}f(x)\quad {\text{and}}\quad f''(x_{0})<0.$

Then:

$\lim _{n\to \infty }{\frac {\int _{a}^{b}e^{nf(x)}\,dx}{e^{nf(x_{0})}{\sqrt {\frac {2\pi }{n\left(-f''(x_{0})\right)}}}}}=1.$

Proof

**Lower bound:** Let $\varepsilon >0$ . Since $f''$ is continuous there exists $\delta >0$ such that if $|x_{0}-c|<\delta$ then $f''(c)\geq f''(x_{0})-\varepsilon .$ By Taylor's Theorem, for any $x\in (x_{0}-\delta ,x_{0}+\delta ),$

$f(x)\geq f(x_{0})+{\frac {1}{2}}(f''(x_{0})-\varepsilon )(x-x_{0})^{2}.$

Then we have the following lower bound:

${\begin{aligned}\int _{a}^{b}e^{nf(x)}\,dx&\geq \int _{x_{0}-\delta }^{x_{0}+\delta }e^{nf(x)}\,dx\\&\geq e^{nf(x_{0})}\int _{x_{0}-\delta }^{x_{0}+\delta }e^{{\frac {n}{2}}(f''(x_{0})-\varepsilon )(x-x_{0})^{2}}\,dx\\&=e^{nf(x_{0})}{\sqrt {\frac {1}{n(-f''(x_{0})+\varepsilon )}}}\int _{-\delta {\sqrt {n(-f''(x_{0})+\varepsilon )}}}^{\delta {\sqrt {n(-f''(x_{0})+\varepsilon )}}}e^{-{\frac {1}{2}}y^{2}}\,dy\end{aligned}}$

where the last equality was obtained by a change of variables

$y={\sqrt {n(-f''(x_{0})+\varepsilon )}}(x-x_{0}).$

Remember $f''(x_{0})<0$ so we can take the square root of its negation.

If we divide both sides of the above inequality by

$e^{nf(x_{0})}{\sqrt {\frac {2\pi }{n(-f''(x_{0}))}}}$

and take the limit we get:

$\lim _{n\to \infty }{\frac {\int _{a}^{b}e^{nf(x)}\,dx}{e^{nf(x_{0})}{\sqrt {\frac {2\pi }{n(-f''(x_{0}))}}}}}\geq \lim _{n\to \infty }{\frac {1}{\sqrt {2\pi }}}\int _{-\delta {\sqrt {n(-f''(x_{0})+\varepsilon )}}}^{\delta {\sqrt {n(-f''(x_{0})+\varepsilon )}}}e^{-{\frac {1}{2}}y^{2}}\,dy\,\cdot {\sqrt {\frac {-f''(x_{0})}{-f''(x_{0})+\varepsilon }}}={\sqrt {\frac {-f''(x_{0})}{-f''(x_{0})+\varepsilon }}}$

since this is true for arbitrary $\varepsilon$ we get the lower bound:

$\lim _{n\to \infty }{\frac {\int _{a}^{b}e^{nf(x)}\,dx}{e^{nf(x_{0})}{\sqrt {\frac {2\pi }{n(-f''(x_{0}))}}}}}\geq 1$

Note that this proof works also when $a=-\infty$ or $b=\infty$ (or both).

**Upper bound:** The proof is similar to that of the lower bound but there are a few inconveniences. Again we start by picking an $\varepsilon >0$ but in order for the proof to work we need $\varepsilon$ small enough so that $f''(x_{0})+\varepsilon <0.$ Then, as above, by continuity of $f''$ and Taylor's Theorem we can find $\delta >0$ so that if $|x-x_{0}|<\delta$ , then

$f(x)\leq f(x_{0})+{\frac {1}{2}}(f''(x_{0})+\varepsilon )(x-x_{0})^{2}.$

Lastly, by our assumptions (assuming $a,b$ are finite) there exists an $\eta >0$ such that if $|x-x_{0}|\geq \delta$ , then $f(x)\leq f(x_{0})-\eta$ .

Then we can calculate the following upper bound:

${\begin{aligned}\int _{a}^{b}e^{nf(x)}\,dx&\leq \int _{a}^{x_{0}-\delta }e^{nf(x)}\,dx+\int _{x_{0}-\delta }^{x_{0}+\delta }e^{nf(x)}\,dx+\int _{x_{0}+\delta }^{b}e^{nf(x)}\,dx\\&\leq (b-a)e^{n(f(x_{0})-\eta )}+\int _{x_{0}-\delta }^{x_{0}+\delta }e^{nf(x)}\,dx\\&\leq (b-a)e^{n(f(x_{0})-\eta )}+e^{nf(x_{0})}\int _{x_{0}-\delta }^{x_{0}+\delta }e^{{\frac {n}{2}}(f''(x_{0})+\varepsilon )(x-x_{0})^{2}}\,dx\\&\leq (b-a)e^{n(f(x_{0})-\eta )}+e^{nf(x_{0})}\int _{-\infty }^{+\infty }e^{{\frac {n}{2}}(f''(x_{0})+\varepsilon )(x-x_{0})^{2}}\,dx\\&\leq (b-a)e^{n(f(x_{0})-\eta )}+e^{nf(x_{0})}{\sqrt {\frac {2\pi }{n(-f''(x_{0})-\varepsilon )}}}\end{aligned}}$

If we divide both sides of the above inequality by

$e^{nf(x_{0})}{\sqrt {\frac {2\pi }{n(-f''(x_{0}))}}}$

and take the limit we get:

$\lim _{n\to \infty }{\frac {\int _{a}^{b}e^{nf(x)}\,dx}{e^{nf(x_{0})}{\sqrt {\frac {2\pi }{n(-f''(x_{0}))}}}}}\leq \lim _{n\to \infty }(b-a)e^{-\eta n}{\sqrt {\frac {n(-f''(x_{0}))}{2\pi }}}+{\sqrt {\frac {-f''(x_{0})}{-f''(x_{0})-\varepsilon }}}={\sqrt {\frac {-f''(x_{0})}{-f''(x_{0})-\varepsilon }}}$

Since $\varepsilon$ is arbitrary we get the upper bound:

$\lim _{n\to \infty }{\frac {\int _{a}^{b}e^{nf(x)}\,dx}{e^{nf(x_{0})}{\sqrt {\frac {2\pi }{n(-f''(x_{0}))}}}}}\leq 1$

And combining this with the lower bound gives the result.

Note that the above proof obviously fails when $a=-\infty$ or $b=\infty$ (or both). To deal with these cases, we need some extra assumptions. A sufficient (not necessary) assumption is that for $n=1,$

$\int _{a}^{b}e^{nf(x)}\,dx<\infty ,$

and that the number $\eta$ as above exists (note that this must be an assumption in the case when the interval $[a,b]$ is infinite). The proof proceeds otherwise as above, but with a slightly different approximation of integrals:

$\int _{a}^{x_{0}-\delta }e^{nf(x)}\,dx+\int _{x_{0}+\delta }^{b}e^{nf(x)}\,dx\leq \int _{a}^{b}e^{f(x)}e^{(n-1)(f(x_{0})-\eta )}\,dx=e^{(n-1)(f(x_{0})-\eta )}\int _{a}^{b}e^{f(x)}\,dx.$

When we divide by

$e^{nf(x_{0})}{\sqrt {\frac {2\pi }{n(-f''(x_{0}))}}},$

we get for this term

${\frac {e^{(n-1)(f(x_{0})-\eta )}\int _{a}^{b}e^{f(x)}\,dx}{e^{nf(x_{0})}{\sqrt {\frac {2\pi }{n(-f''(x_{0}))}}}}}=e^{-(n-1)\eta }{\sqrt {n}}e^{-f(x_{0})}\int _{a}^{b}e^{f(x)}\,dx{\sqrt {\frac {-f''(x_{0})}{2\pi }}}$

whose limit as $n\to \infty$ is 0 . The rest of the proof (the analysis of the interesting term) proceeds as above.

The given condition in the infinite interval case is, as said above, sufficient but not necessary. However, the condition is fulfilled in many, if not in most, applications: the condition simply says that the integral we are studying must be well-defined (not infinite) and that the maximum of the function at $x_{0}$ must be a "true" maximum (the number $\eta >0$ must exist). There is no need to demand that the integral is finite for $n=1$ but it is enough to demand that the integral is finite for some $n=N.$

This method relies on 4 basic concepts such as

Concepts

1. Relative error

The "approximation" in this method is related to the relative error and not the absolute error. Therefore, if we set

$s={\sqrt {\frac {2\pi }{M\left|f''(x_{0})\right|}}},$

the integral can be written as

${\begin{aligned}\int _{a}^{b}e^{Mf(x)}\,dx&=se^{Mf(x_{0})}{\frac {1}{s}}\int _{a}^{b}e^{M(f(x)-f(x_{0}))}\,dx\\&=se^{Mf(x_{0})}\int _{\frac {a-x_{0}}{s}}^{\frac {b-x_{0}}{s}}e^{M(f(sy+x_{0})-f(x_{0}))}\,dy\end{aligned}}$

where s is a small number when M is a large number obviously and the relative error will be

$\left|\int _{\frac {a-x_{0}}{s}}^{\frac {b-x_{0}}{s}}e^{M(f(sy+x_{0})-f(x_{0}))}dy-1\right|.$

Now, let us separate this integral into two parts: $y\in [-D_{y},D_{y}]$ region and the rest.

2.

$e^{M(f(sy+x_{0})-f(x_{0}))}\to e^{-\pi y^{2}}$

around the

stationary point

when

M

is large enough

Considering the Taylor expansion of $M(f(x)-f(x_{0}))$ around $x_{0}$ and translate x to y , as the comparison is done in y-space:

$M(f(x)-f(x_{0}))={\frac {Mf''(x_{0})}{2}}s^{2}y^{2}+{\frac {Mf'''(x_{0})}{6}}s^{3}y^{3}+\cdots =-\pi y^{2}+O\left({\frac {1}{\sqrt {M}}}\right).$

Note that $f'(x_{0})=0$ because $x_{0}$ is a stationary point. From this equation you will find that the terms higher than second derivative in this Taylor expansion is suppressed as the order of ${\tfrac {1}{\sqrt {M}}}$ so that $\exp(M(f(x)-f(x_{0})))$ will get closer to the Gaussian function as shown in figure. Besides,

$\int _{-\infty }^{\infty }e^{-\pi y^{2}}dy=1.$

3. The larger

M

is, the smaller range of

x

is related

Because we do the comparison in y-space, y is fixed in $y\in [-D_{y},D_{y}]$ which will cause $x\in [-sD_{y},sD_{y}]$ ; however, s is inversely proportional to ${\sqrt {M}}$ , the chosen region of x will be smaller when M is increased.

4. If the integral in Laplace's method converges, the contribution of the region which is not around the stationary point of the integration of its relative error will tend to zero as

M

grows.

Relying on the 3rd concept, even if we choose a very large *Dy*, *sDy* will finally be a very small number when M is increased to a huge number. Then, how can we guarantee the integral of the rest will tend to 0 when M is large enough?

The basic idea is to find a function $m(x)$ such that $m(x)\geq f(x)$ and the integral of $e^{Mm(x)}$ will tend to zero when M grows. Because the exponential function of $Mm(x)$ will be always larger than zero as long as $m(x)$ is a real number, and this exponential function is proportional to $m(x),$ the integral of $e^{Mf(x)}$ will tend to zero. For simplicity, choose $m(x)$ as a tangent through the point $x=sD_{y}$ as shown in the figure:

If the interval of the integration of this method is finite, we will find that no matter $f(x)$ is continue in the rest region, it will be always smaller than $m(x)$ shown above when M is large enough. By the way, it will be proved later that the integral of $e^{Mm(x)}$ will tend to zero when M is large enough.

If the interval of the integration of this method is infinite, $m(x)$ and $f(x)$ might always cross to each other. If so, we cannot guarantee that the integral of $e^{Mf(x)}$ will tend to zero finally. For example, in the case of $f(x)={\tfrac {\sin(x)}{x}},$ $\int _{0}^{\infty }e^{Mf(x)}dx$ will always diverge. Therefore, we need to require that $\int _{d}^{\infty }e^{Mf(x)}dx$ can converge for the infinite interval case. If so, this integral will tend to zero when d is large enough and we can choose this d as the cross of $m(x)$ and $f(x).$

You might ask why not choose $\int _{d}^{\infty }e^{f(x)}dx$ as a convergent integral? Let me use an example to show you the reason. Suppose the rest part of $f(x)$ is $-\ln x,$ then $e^{f(x)}={\tfrac {1}{x}}$ and its integral will diverge; however, when $M=2,$ the integral of $e^{Mf(x)}={\tfrac {1}{x^{2}}}$ converges. So, the integral of some functions will diverge when M is not a large number, but they will converge when M is large enough.

Based on these four concepts, we can derive the relative error of this method.

## Other formulations

Laplace's approximation is sometimes written as

$\int _{a}^{b}h(x)e^{Mg(x)}\,dx\approx {\sqrt {\frac {2\pi }{M|g''(x_{0})|}}}h(x_{0})e^{Mg(x_{0})}\ {\text{ as }}M\to \infty$

where h is positive.

Importantly, the accuracy of the approximation depends on the variable of integration, that is, on what stays in $g(x)$ and what goes into $h(x).$

The derivation of its relative error

First, use $x_{0}=0$ to denote the global maximum, which will simplify this derivation. We are interested in the relative error, written as $|R|$ ,

$\int _{a}^{b}h(x)e^{Mg(x)}\,dx=h(0)e^{Mg(0)}s\underbrace {\int _{a/s}^{b/s}{\frac {h(sy)}{h(0)}}e^{M\left[g(sy)-g(0)\right]}dy} _{1+R},$

where

$s\equiv {\sqrt {\frac {2\pi }{M\left|g''(0)\right|}}}.$

So, if we let

$A\equiv {\frac {h(sy)}{h(0)}}e^{M\left[g(sy)-g(0)\right]}$

and $A_{0}\equiv e^{-\pi y^{2}}$ , we can get

$\left|R\right|=\left|\int _{a/s}^{b/s}A\,dy-\int _{-\infty }^{\infty }A_{0}\,dy\right|$

since $\int _{-\infty }^{\infty }A_{0}\,dy=1$ .

For the upper bound, note that $|A+B|\leq |A|+|B|,$ thus we can separate this integration into 5 parts with 3 different types (a), (b) and (c), respectively. Therefore,

$|R|<\underbrace {\left|\int _{D_{y}}^{\infty }A_{0}dy\right|} _{(a_{1})}+\underbrace {\left|\int _{D_{y}}^{b/s}Ady\right|} _{(b_{1})}+\underbrace {\left|\int _{-D_{y}}^{D_{y}}\left(A-A_{0}\right)dy\right|} _{(c)}+\underbrace {\left|\int _{a/s}^{-D_{y}}Ady\right|} _{(b_{2})}+\underbrace {\left|\int _{-\infty }^{-D_{y}}A_{0}dy\right|} _{(a_{2})}$

where $(a_{1})$ and $(a_{2})$ are similar, and likewise so are $(b_{1})$ and $(b_{2})$ are similar, so we can just calculate $(a_{1})$ and $(b_{1})$ .

For $(a_{1})$ , after the translation of $z\equiv \pi y^{2}$ , we can get

$(a_{1})=\left|{\frac {1}{2{\sqrt {\pi }}}}\int _{\pi D_{y}^{2}}^{\infty }e^{-z}z^{-1/2}dz\right|<{\frac {e^{-\pi D_{y}^{2}}}{2\pi D_{y}}}.$

This means that as long as $D_{y}$ is large enough, it will tend to zero.

For $(b_{1})$ , we can get

$(b_{1})\leq \left|\int _{D_{y}}^{b/s}\left[{\frac {h(sy)}{h(0)}}\right]_{\text{max}}e^{Mm(sy)}dy\right|$

where

$m(x)\geq g(x)-g(0){\text{as}}x\in [sD_{y},b]$

and $h(x)$ should have the same sign of $h(0)$ during this region. Let us choose $m(x)$ as the tangent across the point at $x=sD_{y}$ , i.e. $m(sy)=g(sD_{y})-g(0)+g'(sD_{y})\left(sy-sD_{y}\right)$ which is shown in the figure

From this figure you can find that when s or $D_{y}$ gets smaller, the region satisfies the above inequality will get larger. Therefore, if we want to find a suitable $m(x)$ to cover the whole $f(x)$ during the interval of $(b_{1})$ , $D_{y}$ will have an upper limit. Besides, because the integration of $e^{-\alpha x}$ is simple, let me use it to estimate the relative error contributed by this $(b_{1})$ .

Based on Taylor expansion, we can get

${\begin{aligned}M\left[g(sD_{y})-g(0)\right]&=M\left[{\frac {g''(0)}{2}}s^{2}D_{y}^{2}+{\frac {g'''(\xi )}{6}}s^{3}D_{y}^{3}\right]&&{\text{as }}\xi \in [0,sD_{y}]\\&=-\pi D_{y}^{2}+{\frac {(2\pi )^{3/2}g'''(\xi )D_{y}^{3}}{6{\sqrt {M}}|g''(0)|^{\frac {3}{2}}}},\end{aligned}}$

and

${\begin{aligned}Msg'(sD_{y})&=Ms\left(g''(0)sD_{y}+{\frac {g'''(\zeta )}{2}}s^{2}D_{y}^{2}\right)&&{\text{as }}\zeta \in [0,sD_{y}]\\&=-2\pi D_{y}+{\sqrt {\frac {2}{M}}}\left({\frac {\pi }{|g''(0)|}}\right)^{\frac {3}{2}}g'''(\zeta )D_{y}^{2},\end{aligned}}$

and then substitute them back into the calculation of $(b_{1})$ ; however, you can find that the remainders of these two expansions are both inversely proportional to the square root of M , let me drop them out to beautify the calculation. Keeping them is better, but it will make the formula uglier.

${\begin{aligned}(b_{1})&\leq \left|\left[{\frac {h(sy)}{h(0)}}\right]_{\max }e^{-\pi D_{y}^{2}}\int _{0}^{b/s-D_{y}}e^{-2\pi D_{y}y}dy\right|\\&\leq \left|\left[{\frac {h(sy)}{h(0)}}\right]_{\max }e^{-\pi D_{y}^{2}}{\frac {1}{2\pi D_{y}}}\right|.\end{aligned}}$

Therefore, it will tend to zero when $D_{y}$ gets larger, but don't forget that the upper bound of $D_{y}$ should be considered during this calculation.

About the integration near $x=0$ , we can also use Taylor's Theorem to calculate it. When $h'(0)\neq 0$

${\begin{aligned}(c)&\leq \int _{-D_{y}}^{D_{y}}e^{-\pi y^{2}}\left|{\frac {sh'(\xi )}{h(0)}}y\right|\,dy\\&<{\sqrt {\frac {2}{\pi M|g''(0)|}}}\left|{\frac {h'(\xi )}{h(0)}}\right|_{\max }\left(1-e^{-\pi D_{y}^{2}}\right)\end{aligned}}$

and you can find that it is inversely proportional to the square root of M . In fact, $(c)$ will have the same behave when $h(x)$ is a constant.

Conclusively, the integral near the stationary point will get smaller as ${\sqrt {M}}$ gets larger, and the rest parts will tend to zero as long as $D_{y}$ is large enough; however, we need to remember that $D_{y}$ has an upper limit which is decided by whether the function $m(x)$ is always larger than $g(x)-g(0)$ in the rest region. However, as long as we can find one $m(x)$ satisfying this condition, the upper bound of $D_{y}$ can be chosen as directly proportional to ${\sqrt {M}}$ since $m(x)$ is a tangent across the point of $g(x)-g(0)$ at $x=sD_{y}$ . So, the bigger M is, the bigger $D_{y}$ can be.

In the multivariate case, where $\mathbf {x}$ is a d -dimensional vector and $f(\mathbf {x} )$ is a scalar function of $\mathbf {x}$ , Laplace's approximation is usually written as:

$\int h(\mathbf {x} )e^{Mf(\mathbf {x} )}\,d^{d}x\approx \left({\frac {2\pi }{M}}\right)^{d/2}{\frac {h(\mathbf {x} _{0})e^{Mf(\mathbf {x} _{0})}}{\left|-H(f)(\mathbf {x} _{0})\right|^{1/2}}}{\text{ as }}M\to \infty$

where $H(f)(\mathbf {x} _{0})$ is the Hessian matrix of f evaluated at $\mathbf {x} _{0}$ and where $|\cdot |$ denotes its matrix determinant. Analogously to the univariate case, the Hessian is required to be negative-definite.

## Steepest descent extension

In extensions of Laplace's method, complex analysis, and in particular Cauchy's integral formula, is used to find a contour *of steepest descent* for an (asymptotically with large *M*) equivalent integral, expressed as a line integral. In particular, if no point *x*0 where the derivative of f vanishes exists on the real line, it may be necessary to deform the integration contour to an optimal one, where the above analysis will be possible. Again, the main idea is to reduce, at least asymptotically, the calculation of the given integral to that of a simpler integral that can be explicitly evaluated. See the book of Erdelyi (1956) for a simple discussion (where the method is termed *steepest descents*).

The appropriate formulation for the complex *z*-plane is

$\int _{a}^{b}e^{Mf(z)}\,dz\approx {\sqrt {\frac {2\pi }{-Mf''(z_{0})}}}e^{Mf(z_{0})}{\text{ as }}M\to \infty .$

for a path passing through the saddle point at *z*0. Note the explicit appearance of a minus sign to indicate the direction of the second derivative: one must *not* take the modulus. Also note that if the integrand is meromorphic, one may have to add residues corresponding to poles traversed while deforming the contour (see for example section 3 of Okounkov's paper *Symmetric functions and random partitions*).

In statistics and statistical physics, this approximation is called the saddle-point approximation.

## Further generalizations

An extension of the *steepest descent method* is the so-called *nonlinear stationary phase/steepest descent method*. Here, instead of integrals, one needs to evaluate asymptotically solutions of Riemann–Hilbert factorization problems.

Given a contour *C* in the complex sphere, a function f defined on that contour and a special point, such as infinity, a holomorphic function *M* is sought away from *C*, with prescribed jump across *C*, and with a given normalization at infinity. If f and hence *M* are matrices rather than scalars this is a problem that in general does not admit an explicit solution.

An asymptotic evaluation is then possible along the lines of the linear stationary phase/steepest descent method. The idea is to reduce asymptotically the solution of the given Riemann–Hilbert problem to that of a simpler, explicitly solvable, Riemann–Hilbert problem. Cauchy's theorem is used to justify deformations of the jump contour.

The nonlinear stationary phase was introduced by Deift and Zhou in 1993, based on earlier work of Its. A (properly speaking) nonlinear steepest descent method was introduced by Kamvissis, K. McLaughlin and P. Miller in 2003, based on previous work of Lax, Levermore, Deift, Venakides and Zhou. As in the linear case, "steepest descent contours" solve a min-max problem. In the nonlinear case they turn out to be "S-curves" (defined in a different context back in the 80s by Stahl, Gonchar and Rakhmanov).

The nonlinear stationary phase/steepest descent method has applications to the theory of soliton equations and integrable models, random matrices and combinatorics.

## Median-point approximation generalization

In the generalization, evaluation of the integral is considered equivalent to finding the norm of the distribution with density

$e^{Mf(x)}.$

Denoting the cumulative distribution $F(x)$ , if there is a diffeomorphic Gaussian distribution with density

$e^{-g-{\frac {\gamma }{2}}y^{2}}$

the norm is given by

${\sqrt {2\pi \gamma ^{-1}}}e^{-g}$

and the corresponding diffeomorphism is

$y(x)={\frac {1}{\sqrt {\gamma }}}\Phi ^{-1}{\left({\frac {F(x)}{F(\infty )}}\right)},$

where $\Phi$ denotes cumulative standard normal distribution function.

In general, any distribution diffeomorphic to the Gaussian distribution has density

$e^{-g-{\frac {\gamma }{2}}y^{2}(x)}y'(x)$

and the median-point is mapped to the median of the Gaussian distribution. Matching the logarithm of the density functions and their derivatives at the median point up to a given order yields a system of equations that determine the approximate values of $\gamma$ and g .

The approximation was introduced in 2019 by D. Makogon and C. Morais Smith primarily in the context of partition function evaluation for a system of interacting fermions.

## Complex integrals

For complex integrals in the form:

${\frac {1}{2\pi i}}\int _{c-i\infty }^{c+i\infty }g(s)e^{st}\,ds$

with $t\gg 1,$ we make the substitution *t* = *iu* and the change of variable $s=c+ix$ to get the bilateral Laplace transform:

${\frac {1}{2\pi }}\int _{-\infty }^{\infty }g(c+ix)e^{-ux}e^{icu}\,dx.$

We then split *g*(*c* + *ix*) in its real and complex part, after which we recover *u* = *t*/*i*. This is useful for inverse Laplace transforms, the Perron formula and complex integration.

## Example: Stirling's approximation

Laplace's method can be used to derive Stirling's approximation

$N!\approx {\sqrt {2\pi N}}\left({\frac {N}{e}}\right)^{N}\,$

for a large integer *N*. From the definition of the Gamma function, we have

$N!=\Gamma (N+1)=\int _{0}^{\infty }e^{-x}x^{N}\,dx.$

Now we change variables, letting $x=Nz$ so that $dx=Ndz.$ Plug these values back in to obtain

${\begin{aligned}N!&=\int _{0}^{\infty }e^{-Nz}(Nz)^{N}N\,dz\\&=N^{N+1}\int _{0}^{\infty }e^{-Nz}z^{N}\,dz\\&=N^{N+1}\int _{0}^{\infty }e^{-Nz}e^{N\ln z}\,dz\\&=N^{N+1}\int _{0}^{\infty }e^{N(\ln z-z)}\,dz.\end{aligned}}$

This integral has the form necessary for Laplace's method with

$f(z)=\ln {z}-z$

which is twice-differentiable:

$f'(z)={\frac {1}{z}}-1,$

$f''(z)=-{\frac {1}{z^{2}}}.$

The maximum of $f(z)$ lies at *z*0 = 1, and the second derivative of $f(z)$ has the value −1 at this point. Therefore, we obtain

$N!\approx N^{N+1}{\sqrt {\frac {2\pi }{N}}}e^{-N}={\sqrt {2\pi N}}N^{N}e^{-N}.$
