---
title: "Lebesgue integral"
source: https://en.wikipedia.org/wiki/Lebesgue_integration
domain: measure-theory
license: CC-BY-SA-4.0
tags: measure theory, lebesgue integration, lebesgue measure, borel set
fetched: 2026-07-02
---

# Lebesgue integral

(Redirected from

Lebesgue integration

)

In mathematics, the integral of a non-negative function of a single variable can be regarded, in the simplest case, as the area between the graph of that function and the x-axis. The **Lebesgue integral**, named after French mathematician Henri Lebesgue, is one way to make this concept rigorous and to extend it to more general functions.

The Lebesgue integral is more general than the Riemann integral, which it largely replaced in mathematical analysis since the first half of the 20th century. It can accommodate functions with discontinuities arising in many applications that are pathological from the perspective of the Riemann integral. The Lebesgue integral also has generally better analytical properties. For instance, under mild conditions, it is possible to exchange limits with Lebesgue integration, while the conditions for doing this with a Riemann integral are comparatively restrictive. Furthermore, the Lebesgue integral can be generalized in a straightforward way to more general spaces, measure spaces, such as those that arise in probability theory.

The term **Lebesgue integration** can mean either the general theory of integration of a function with respect to a general measure, as introduced by Lebesgue, or the specific case of integration of a function defined on a sub-domain of the real line with respect to the Lebesgue measure.

## Introduction

The integral of a positive real function f between boundaries a and b can be interpreted as the area under the graph of f, between a and b. This notion of area fits some functions, mainly piecewise continuous functions, including elementary functions, for example polynomials. However, the graphs of other functions, for example the Dirichlet function, do not fit well with the notion of area. Graphs like that of the latter raise the question, "For which class of functions does 'area under the curve' make sense?". The answer to this question has great theoretical importance.

As part of a general movement toward rigor in mathematics in the nineteenth century, mathematicians attempted to put integral calculus on a firm foundation. The Riemann integral—proposed by Bernhard Riemann (1826–1866)—is a broadly successful attempt to provide such a foundation. Riemann's definition starts with the construction of a sequence of easily calculated areas that converge to the integral of a given function. This definition is successful in the sense that it gives the expected answer for many already-solved problems, and gives useful results for many other problems.

However, Riemann integration does not interact well with taking limits of sequences of functions, making such limiting processes difficult to analyze. This is important, for instance, in the study of Fourier series, Fourier transforms, and other topics. The Lebesgue integral describes better how and when it is possible to take limits under the integral sign (via the monotone convergence theorem and dominated convergence theorem).

While the Riemann integral considers the area under a curve as made out of vertical rectangles, the Lebesgue definition considers horizontal slabs that are not necessarily just rectangles, and so it is more flexible. For this reason, the Lebesgue definition makes it possible to calculate integrals for a broader class of functions. For example, the Dirichlet function, which is 1 where its argument is rational and 0 otherwise, has a Lebesgue integral, but does not have a Riemann integral. Furthermore, the Lebesgue integral of this function is zero, which agrees with the intuition that when picking a real number uniformly at random from the unit interval, the probability of picking a rational number should be zero.

Lebesgue summarized his approach to integration in a letter to Paul Montel:

> I have to pay a certain sum, which I have collected in my pocket. I take the bills and coins out of my pocket and give them to the creditor in the order I find them until I have reached the total sum. This is the Riemann integral. But I can proceed differently. After I have taken all the money out of my pocket I order the bills and coins according to identical values and then I pay the several heaps one after the other to the creditor. This is my integral.

— *Source*: (Siegmund-Schultze 2008)

The insight is that one should be able to rearrange the values of a function freely, while preserving the value of the integral. This process of rearrangement can convert a very pathological function into one that is "nice" from the point of view of integration, and thus let such pathological functions be integrated.

### Intuitive interpretation

Folland (1999) summarizes the difference between the Riemann and Lebesgue approaches thus: "to compute the Riemann integral of f, one partitions the domain [*a*, *b*] into subintervals", while in the Lebesgue integral, "one is in effect partitioning the range of *f*".

For the Riemann integral, the *domain* is partitioned into intervals, and bars are constructed to meet the height of the graph. The areas of these bars are added together, and this approximates the integral, in effect by summing areas of the form *f*(*x*)*dx* where *f*(*x*) is the height of a rectangle and dx is its width.

For the Lebesgue integral, the *range* is partitioned into intervals, and so the region under the graph is partitioned into horizontal "slabs" (which may not be connected sets). The area of a small horizontal "slab" under the graph of f, of height dy, is equal to the measure of the slab's width times dy: $\mu \left(\{x\mid f(x)>y\}\right)\,dy.$ The Lebesgue integral may then be defined by adding up the areas of these horizontal slabs. From this perspective, a key difference with the Riemann integral is that the "slabs" are no longer rectangular (cartesian products of two intervals), but instead are cartesian products of a measurable set with an interval.

#### Simple functions

An equivalent way to introduce the Lebesgue integral is to use so-called simple functions, which generalize the step functions of Riemann integration. Consider, for example, determining the cumulative COVID-19 case count from a graph of smoothed cases each day (right).

**The Riemann–Darboux approach**

Partition the domain (time period) into intervals (eight, in the example) and construct bars with heights that meet the graph. The cumulative count is found by summing, over all bars, the product of interval width (time in days) and the bar height (cases per day).

**The Lebesgue approach**

Choose a finite number of target values (eight, in the example) in the range of the function. By constructing bars with heights equal to these values, but below the function, they imply a partitioning of the domain into the same number of subsets (subsets, indicated by color in the example, need not be connected). This is a "simple function", as described below. The cumulative count is found by summing, over all subsets of the domain, the product of the

measure

on that subset (total time in days) and the bar height (cases per day).

### Relation between the viewpoints

One can think of the Lebesgue integral either in terms of *slabs* or *simple functions*. Intuitively, the area under a simple function can be partitioned into slabs based on the (finite) collection of values in the range of a simple function (a real interval). Conversely, the (finite) collection of slabs in the undergraph of the function can be rearranged after a finite repartitioning to be the undergraph of a simple function.

The *slabs* viewpoint makes it easy to define the Lebesgue integral, in terms of basic calculus. Suppose that *f* is a (Lebesgue measurable) function, taking non-negative values (possibly including +∞). Define the distribution function of *f* as the "width of a slab", i.e., $F(y)=\mu \{x|f(x)>y\}.$ Then *F*(*y*) is monotone decreasing and non-negative, and therefore has an (improper) Riemann integral over (0, ∞), allowing that the integral can be +∞. The Lebesgue integral can then be *defined* by $\int f\,d\mu =\int _{0}^{\infty }F(y)\,dy$ where the integral on the right is an ordinary improper Riemann integral, of a non-negative function (interpreted appropriately as +∞ if *F*(*y*) = +∞ on a neighborhood of 0).

Most textbooks, however, emphasize the *simple functions* viewpoint, because it is then more straightforward to prove the basic theorems about the Lebesgue integral.

### Measure theory

Measure theory was initially created to provide a useful abstraction of the notion of length of subsets of the real line—and, more generally, area and volume of subsets of Euclidean spaces. In particular, it provided a systematic answer to the question of which subsets of **R** have a length. As later set theory developments showed (see non-measurable set), it is actually impossible to assign a length to all subsets of **R** in a way that preserves some natural additivity and translation invariance properties. This suggests that picking out a suitable class of *measurable* subsets is an essential prerequisite.

The Riemann integral uses the notion of length explicitly. Indeed, the element of calculation for the Riemann integral is the rectangle [*a*, *b*] × [*c*, *d*], whose area is calculated to be (*b* − *a*)(*d* − *c*). The quantity *b* − *a* is the length of the base of the rectangle and *d* − *c* is the height of the rectangle. Riemann could only use planar rectangles to approximate the area under the curve, because there was no adequate theory for measuring more general sets.

In the development of the theory in most modern textbooks (after 1950), the approach to measure and integration is *axiomatic*. This means that a measure is any function μ defined on a certain class X of subsets of a set E, which satisfies a certain list of properties. These properties can be shown to hold in many different cases.

### Measurable functions

We start with a measure space (*E*, *X*, *μ*) where E is a set, X is a σ-algebra of subsets of E, and μ is a (non-negative) measure on E defined on the sets of X.

For example, E can be Euclidean *n*-space **R***n* or some Lebesgue measurable subset of it, X is the σ-algebra of all Lebesgue measurable subsets of E, and *μ* is the Lebesgue measure. In the mathematical theory of probability, we confine our study to a probability measure *μ*, which satisfies *μ*(*E*) = 1.

Lebesgue's theory defines integrals for a class of functions called measurable functions. A real-valued function f on E is measurable if the pre-image of every interval of the form (*t*, ∞) is in X: $\{x\,\mid \,f(x)>t\}\in X\quad \forall t\in \mathbb {R} .$

We can show that this is equivalent to requiring that the pre-image of any Borel subset of **R** be in X. The set of measurable functions is closed under algebraic operations, but more importantly it is closed under various kinds of point-wise sequential limits: $\sup _{k\in \mathbb {N} }f_{k},\quad \liminf _{k\in \mathbb {N} }f_{k},\quad \limsup _{k\in \mathbb {N} }f_{k}$ are measurable if the original sequence (*f**k*), where *k* ∈ **N**, consists of measurable functions.

There are several approaches for defining an integral for measurable real-valued functions f defined on E, and several notations are used to denote such an integral. $\int _{E}f\,d\mu =\int _{E}f(x)\,d\mu (x)=\int _{E}f(x)\,\mu (dx).$

Following the identification in Distribution theory of measures with distributions of order 0, or with Radon measures, one can also use a dual pair notation and write the integral with respect to *μ* in the form $\langle \mu ,f\rangle .$

## Definition

The theory of the Lebesgue integral requires a theory of measurable sets and measures on these sets, as well as a theory of measurable functions and integrals on these functions.

### Via simple functions

One approach to constructing the Lebesgue integral is to make use of so-called *simple functions*: finite, real linear combinations of *indicator functions*. Simple functions that lie directly underneath a given function f can be constructed by partitioning the range of f into a finite number of layers. The intersection of the graph of f with a layer identifies a set of intervals in the domain of f, which, taken together, is defined to be the preimage of the lower bound of that layer, under the simple function. In this way, the partitioning of the range of f implies a partitioning of its domain. The integral of a simple function is found by summing, over these (not necessarily connected) subsets of the domain, the product of the measure of the subset and its image under the simple function (the lower bound of the corresponding layer); intuitively, this product is the sum of the areas of all bars of the same height. The integral of a non-negative general measurable function is then defined as an appropriate supremum of approximations by simple functions, and the integral of a (not necessarily positive) measurable function is the difference of two integrals of non-negative measurable functions.

#### Indicator functions

To assign a value to the integral of the indicator function 1*S* of a measurable set S consistent with the given measure μ, the only reasonable choice is to set: $\int 1_{S}\,d\mu =\mu (S).$

Notice that the result may be equal to +∞, unless *μ* is a *finite* measure.

#### Simple functions

A finite linear combination of indicator functions $\sum _{k}a_{k}1_{S_{k}}$ where the coefficients ak are real numbers and *S**k* are disjoint measurable sets, is called a measurable simple function. We extend the integral by linearity to *non-negative* measurable simple functions. When the coefficients *a**k* are positive, we set $\int \left(\sum _{k}a_{k}1_{S_{k}}\right)\,d\mu =\sum _{k}a_{k}\int 1_{S_{k}}\,d\mu =\sum _{k}a_{k}\,\mu (S_{k})$ whether this sum is finite or +∞. A simple function can be written in different ways as a linear combination of indicator functions, but the integral will be the same by the additivity of measures.

Some care is needed when defining the integral of a *real-valued* simple function, to avoid the undefined expression ∞ − ∞: one assumes that the representation $f=\sum _{k}a_{k}1_{S_{k}}$ is such that *μ*(*S**k*) < ∞ whenever *a**k* ≠ 0. Then the above formula for the integral of f makes sense, and the result does not depend upon the particular representation of f satisfying the assumptions. (It is important that the representation be a *finite* linear combination, i.e. that *k* only take on a finite number of values.)

If B is a measurable subset of E and s is a measurable simple function one defines $\int _{B}s\,\mathrm {d} \mu =\int 1_{B}\,s\,\mathrm {d} \mu =\sum _{k}a_{k}\,\mu (S_{k}\cap B).$

#### Non-negative functions

Let f be a non-negative measurable function on E, which we allow to attain the value +∞, in other words, f takes non-negative values in the extended real number line. We define $\int _{E}f\,d\mu =\sup \left\{\,\int _{E}s\,d\mu :0\leq s\leq f,\ s\ {\text{simple}}\,\right\}.$

We need to show this integral coincides with the preceding one, defined on the set of simple functions, when E is a segment [*a*, *b*]. There is also the question of whether this corresponds in any way to a Riemann notion of integration. It is possible to prove that the answer to both questions is yes.

We have defined the integral of f for any non-negative extended real-valued measurable function on E. For some functions, this integral ${\textstyle \int _{E}f\,d\mu }$ is infinite.

It is often useful to have a particular sequence of simple functions that approximates the Lebesgue integral well (analogously to a Riemann sum). For a non-negative measurable function f, let *s**n*(*x*) be the simple function whose value is *k*/2*n* whenever *k*/2*n* ≤ *f*(*x*) < (*k* + 1)/2*n*, for k a non-negative integer less than, say, 4*n*. Then it can be proven directly that $\int f\,d\mu =\lim _{n\to \infty }\int s_{n}\,d\mu$ and that the limit on the right hand side exists as an extended real number. This bridges the connection between the approach to the Lebesgue integral using simple functions, and the motivation for the Lebesgue integral using a partition of the range.

#### Signed functions

To handle signed functions, we need a few more definitions. If f is a measurable function of the set E to the reals (including ±∞), then we can write $f=f^{+}-f^{-},$ where ${\begin{aligned}f^{+}(x)&={\begin{cases}f(x){\hphantom {-}}&{\text{if }}f(x)>0,\\0&{\text{otherwise}},\end{cases}}\\f^{-}(x)&={\begin{cases}-f(x)&{\text{if }}f(x)<0,\\0&{\text{otherwise}}.\end{cases}}\end{aligned}}$

Note that both *f*+ and *f*− are non-negative measurable functions. Also note that $|f|=f^{+}+f^{-}.$

We say that the Lebesgue integral of the measurable function f *exists*, or *is defined* if at least one of ${\textstyle \int f^{+}\,d\mu }$ and ${\textstyle \int f^{-}\,d\mu }$ is finite: $\min \left(\int f^{+}\,d\mu ,\int f^{-}\,d\mu \right)<\infty .$

In this case we *define* $\int f\,d\mu =\int f^{+}\,d\mu -\int f^{-}\,d\mu .$

If $\int |f|\,\mathrm {d} \mu <\infty ,$ we say that f is *Lebesgue integrable*. That is, f belongs to the space *L*1.

It turns out that this definition gives the desirable properties of the integral.

### Via improper Riemann integral

Assuming that f is measurable and non-negative, the function $f^{*}(t)\ {\stackrel {\text{def}}{=}}\ \mu \left(\{x\in E\mid f(x)>t\}\right).$ is monotonically non-increasing. The Lebesgue integral may then be defined as the improper Riemann integral of *f*∗: $\int _{E}f\,d\mu \ {\stackrel {\text{def}}{=}}\ \int _{0}^{\infty }f^{*}(t)\,dt.$ This integral is improper at the upper limit of ∞, and possibly also at zero. It exists, with the allowance that it may be infinite.

As above, the integral of a Lebesgue integrable (not necessarily non-negative) function is defined by subtracting the integral of its positive and negative parts.

### Complex-valued functions

Complex-valued functions can be similarly integrated, by considering the real part and the imaginary part separately.

If *h* = *f* + *ig* for real-valued integrable functions f, g, then the integral of h is defined by $\int h\,d\mu =\int f\,d\mu +i\int g\,d\mu .$

The function is Lebesgue integrable if and only if its absolute value is Lebesgue integrable (see Absolutely integrable function).

## Example

Consider the indicator function of the rational numbers, 1**Q**, also known as the Dirichlet function. This function is nowhere continuous.

- $1_{\mathbf {Q} }$ **is not Riemann-integrable on** [0, 1]: No matter how the set [0, 1] is partitioned into subintervals, each partition contains at least one rational and at least one irrational number, because rationals and irrationals are both dense in the reals. Thus the upper Darboux sums are all one, and the lower Darboux sums are all zero.
- $1_{\mathbf {Q} }$ **is Lebesgue-integrable on** [0, 1] using the Lebesgue measure: Indeed, it is the indicator function of the rationals so by definition $\int _{[0,1]}1_{\mathbf {Q} }\,d\mu =\mu (\mathbf {Q} \cap [0,1])=0,$ because **Q** is countable.

## Domain of integration

A technical issue in Lebesgue integration is that the domain of integration is defined as a *set* (a subset of a measure space), with no notion of orientation. In elementary calculus, one defines integration with respect to an orientation: $\int _{b}^{a}f=-\int _{a}^{b}f.$ Generalizing this to higher dimensions yields integration of differential forms on manifolds, and to Stokes' theorem as the generalization of the fundamental theorem of calculus. By contrast, Lebesgue integration provides an alternative generalization, integrating over subsets with respect to a measure; this can be notated as $\int _{A}f\,d\mu =\int _{[a,b]}f\,d\mu$ to indicate integration over a subset A. For details on the relation between these generalizations, see Differential form § Relation with measures. The main theory linking these ideas is that of homological integration (sometimes called geometric integration theory), pioneered by Georges de Rham and Hassler Whitney.

## Limitations of the Riemann integral

With the advent of Fourier series, many analytical problems involving integrals arose whose satisfactory solution required interchanging limit processes and integral signs. However, the conditions under which the integrals $\sum _{k}\int f_{k}(x)\,dx\quad {\text{and}}\quad \int \left[\sum _{k}f_{k}(x)\right]dx$ are equal proved quite elusive in the Riemann framework. There are some other technical difficulties with the Riemann integral. These are linked with the limit-taking difficulty discussed above.

### Failure of monotone convergence

As shown above, the indicator function 1**Q** on the rationals is not Riemann integrable. In particular, the Monotone convergence theorem fails. To see why, let {*a**k*} be an enumeration of all the rational numbers in [0, 1] (they are countable so this can be done). Then let $g_{k}(x)={\begin{cases}1&{\text{if }}x=a_{j},j\leq k\\0&{\text{otherwise}}\end{cases}}$

The function gk is zero everywhere, except on a finite set of points. Hence its Riemann integral is zero. Each gk is non-negative, and this sequence of functions is monotonically increasing, but its limit as *k* → ∞ is 1**Q**, which is not Riemann integrable.

### Unsuitability for most domains and functions

The Riemann integral in its original form is defined over a closed bounded interval of the real line for real functions that are defined on the interval's entirety and continuous almost everywhere within it. It can, however, be extended to the complex plane, Euclidean space or unions of integrable regions with similar limitations. An improper Riemann integral, meanwhile, can integrate a function by taking limits on unbounded intervals or at points at which the function is not defined so long as the proper integral approaches a limit as the region of proper integration approaches the desired region of improper integration. While improper integration is an advantage of the Riemann integral, many Lebesgue-integrable functions are not well behaved enough or are defined on domains that are too irregular to be suitable for proper Riemann integration.

### Integrating on structures other than Euclidean space

The Riemann integral is inextricably linked to the order structure of the real line.

## Basic theorems of the Lebesgue integral

Two functions are said to be equal almost everywhere ( $f\ {\stackrel {\text{a.e.}}{=}}\ g$ for short) if $\{x\mid f(x)\neq g(x)\}$ is a subset of a null set. Measurability of the set $\{x\mid f(x)\neq g(x)\}$ is *not* required.

The following theorems are proved in most textbooks on measure theory and Lebesgue integration.

- If f and g are non-negative measurable functions (possibly assuming the value +∞) such that *f* = *g* almost everywhere, then $\int f\,d\mu =\int g\,d\mu .$ To wit, the integral respects the equivalence relation of almost-everywhere equality.
- If f and g are functions such that *f* = *g* almost everywhere, then f is Lebesgue integrable if and only if g is Lebesgue integrable, and the integrals of f and g are the same if they exist.
- Linearity: If f and g are Lebesgue integrable functions and a and b are real numbers, then *af* + *bg* is Lebesgue integrable and $\int (af+bg)\,d\mu =a\int f\,d\mu +b\int g\,d\mu .$
- Monotonicity: If *f* ≤ *g*, then $\int f\,d\mu \leq \int g\,d\mu .$
- Monotone convergence theorem: Suppose {*f**k*}*k*∈**N** is a sequence of non-negative measurable functions such that $f_{k}(x)\leq f_{k+1}(x)\quad \forall k\in \mathbb {N} ,\,\forall x\in E.$ Then, the pointwise limit f of fk is Lebesgue measurable and $\lim _{k}\int f_{k}\,d\mu =\int f\,d\mu .$ The value of any of the integrals is allowed to be infinite.
- Fatou's lemma: If {*f**k*}*k*∈**N** is a sequence of non-negative measurable functions, then $\int \liminf _{k}f_{k}\,d\mu \leq \liminf _{k}\int f_{k}\,d\mu .$ Again, the value of any of the integrals may be infinite.
- Dominated convergence theorem: Suppose {*f**k*}*k*∈**N** is a sequence of complex measurable functions with pointwise limit f, and there is a Lebesgue integrable function g (i.e., g belongs to the space *L*1) such that |*f**k*| ≤ *g* for all k. Then f is Lebesgue integrable and $\lim _{k}\int f_{k}\,d\mu =\int f\,d\mu .$

Necessary and sufficient conditions for the interchange of limits and integrals were proved by Cafiero, generalizing earlier work of Renato Caccioppoli, Vladimir Dubrovskii, and Gaetano Fichera.

## Alternative formulations

It is possible to develop the integral with respect to the Lebesgue measure without relying on the full machinery of measure theory. One such approach is provided by the Daniell integral.

There is also an alternative approach to developing the theory of integration via methods of functional analysis. The Riemann integral exists for any continuous function f of compact support defined on **R***n* (or a fixed open subset). Integrals of more general functions can be built starting from these integrals.

Let *C*c be the space of all real-valued compactly supported continuous functions of **R**. Define a norm on *C*c by $\left\|f\right\|=\int |f(x)|\,dx.$

Then *C*c is a normed vector space (and in particular, it is a metric space.) All metric spaces have Hausdorff completions, so let *L*1 be its completion. This space is isomorphic to the space of Lebesgue integrable functions modulo the subspace of functions with integral zero. Furthermore, the Riemann integral ∫ is a uniformly continuous functional with respect to the norm on *C*c, which is dense in *L*1. Hence ∫ has a unique extension to all of *L*1. This integral is precisely the Lebesgue integral.

More generally, when the measure space on which the functions are defined is also a locally compact topological space (as is the case with the real numbers **R**), measures compatible with the topology in a suitable sense (Radon measures, of which the Lebesgue measure is an example) an integral with respect to them can be defined in the same manner, starting from the integrals of continuous functions with compact support. More precisely, the compactly supported functions form a vector space that carries a natural topology, and a (Radon) measure is defined as a continuous linear functional on this space. The value of a measure at a compactly supported function is then also by definition the integral of the function. One then proceeds to expand the measure (the integral) to more general functions by continuity, and defines the measure of a set as the integral of its indicator function. This is the approach taken by Nicolas Bourbaki and a certain number of other authors. For details see Radon measures.

## Limitations of Lebesgue integral

The main purpose of the Lebesgue integral is to provide an integral notion where limits of integrals hold under mild assumptions. There is no guarantee that every function is Lebesgue integrable. But it may happen that improper integrals exist for functions that are not Lebesgue integrable. One example would be the sinc function: $\operatorname {sinc} (x)={\frac {\sin(x)}{x}}$ over the entire real line. This function is not Lebesgue integrable, as $\int _{-\infty }^{\infty }\left|{\frac {\sin(x)}{x}}\right|dx=\infty .$ On the other hand, ${\textstyle \int _{-\infty }^{\infty }{\frac {\sin(x)}{x}}\,dx}$ exists as an improper integral and can be computed to be finite; it is twice the Dirichlet integral and equal to *π*.
