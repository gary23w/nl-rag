---
title: "Riemann integral"
source: https://en.wikipedia.org/wiki/Riemann_integral
domain: real-analysis
license: CC-BY-SA-4.0
tags: real analysis, uniform convergence, riemann integral, metric space
fetched: 2026-07-02
---

# Riemann integral

In real analysis, the **Riemann integral** is a rigorous definition of the integral of a function on an interval. It defines the integral by approximating the region under the graph of a function by finite sums of areas of vertical rectangles. For suitable functions, including every continuous function on a closed bounded interval, these Riemann sums approach a single limiting value as the partitions of the interval become finer. That limiting value defines the integral, and Riemann sums that are suitably close to the limit can be used as numerical approximations.

Bernhard Riemann introduced the integral in work presented to the faculty at the University of Göttingen in 1854 and published in 1868. It is the integral most commonly introduced in elementary calculus, although in advanced analysis it is often replaced by more general notions such as the Lebesgue integral.

## Overview

Consider a curve on a graph which stays above the *x*-axis, beginning at *x* = *a* and ending at *x* = *b*. The area under that curve, from *a* to *b*, is what we want to find. This area can be described as the set of all points (*x*, *y*) on the graph that follow these rules: *a* ≤ *x* ≤ *b* (the *x*-coordinate is between *a* and *b*) and 0 < *y* < *f*(*x*) (the *y*-coordinate is between 0 and the height of the curve *f*(*x*)). Mathematically, this region can be expressed in set-builder notation as $S=\left\{(x,y)\,:\,a\leq x\leq b\,,\,0<y<f(x)\right\}.$

To measure this area, we use a **Riemann integral**, which is written as: $\int _{a}^{b}f(x)\,dx.$

This notation means “the integral of *f*(*x*) from *a* to *b*,” and it represents the exact area under the curve *f*(*x*) and above the *x*-axis, between *x* = *a* and *x* = *b*.

The idea behind the Riemann integral is to break the area into small, simple shapes (like rectangles), add up their areas, and then make the rectangles smaller and smaller to get a better estimate. In the end, when the rectangles are infinitely small, the sum gives the exact area, which is what the integral represents.

If the curve dips below the *x*-axis, the integral gives a **signed area**. This means the integral adds the part above the *x*-axis as positive and subtracts the part below the *x*-axis as negative. So, the result of $\int _{a}^{b}f(x)\,dx$ can be positive, negative, or zero, depending on how much of the curve is above or below the *x*-axis.

## Definition

### Partitions of an interval

A **partition** of an interval [*a*, *b*] is a finite sequence of numbers of the form $a=x_{0}<x_{1}<x_{2}<\dots <x_{i}<\dots <x_{n}=b$

Each [*xi*, *x**i* + 1] is called a **sub-interval** of the partition. The **mesh** or **norm** of a partition is defined to be the length of the longest sub-interval, that is, $\max \left(x_{i+1}-x_{i}\right),\quad i\in [0,n-1].$

A **tagged partition** *P*(*x*, *t*) of an interval [*a*, *b*] is a partition together with a choice of a sample point within each sub-interval: that is, numbers *t*0, ..., *t**n* − 1 with *ti* ∈ [*xi*, *x**i* + 1] for each i. The mesh of a tagged partition is the same as that of an ordinary partition.

A partition Q is said to refine the a partition P if the intervals in the partition Q are all subintervals of the intervals in the partition P , so that the points marking the partition in Q include those of P and possibly others making it finer. A refinement of a tagged partition is defined so that each tag $t_{i}$ of P is a tag of some interval in Q .

We can turn the set of all tagged partitions into a directed set by saying that one tagged partition is greater than or equal to another if the former is a refinement of the latter.

### Riemann sum

A sequence of Riemann sums over a regular partition of an interval. The number on top is the total area of the rectangles, which converges to the integral of the function.

The partition does not need to be regular, as shown here. The approximation works as long as the width of each subdivision tends to zero.

Let f be a real-valued function defined on the interval [*a*, *b*]. The **Riemann sum** of f with respect to a tagged partition *P*(*x*, *t*) of [*a*, *b*] is $\sum _{i=0}^{n-1}f(t_{i})\left(x_{i+1}-x_{i}\right).$

Each term in the sum is the product of the value of the function at a given point and the length of an interval. Consequently, each term represents the (signed) area of a rectangle with height *f*(*ti*) and width *x**i* + 1 − *xi*. The Riemann sum is the (signed) area of all the rectangles.

Closely related concepts are the *lower and upper Darboux sums*. These are similar to Riemann sums, but the tags are replaced by the infimum and supremum (respectively) of f on each sub-interval: ${\begin{aligned}L(f,P)&=\sum _{i=0}^{n-1}\inf _{t\in [x_{i},x_{i+1}]}f(t)(x_{i+1}-x_{i}),\\U(f,P)&=\sum _{i=0}^{n-1}\sup _{t\in [x_{i},x_{i+1}]}f(t)(x_{i+1}-x_{i}).\end{aligned}}$

If f is continuous, then the lower and upper Darboux sums for an untagged partition are equal to the Riemann sum for that partition, where the tags are chosen to be the minimum or maximum (respectively) of f on each subinterval. (When f is discontinuous on a subinterval, there may not be a tag that achieves the infimum or supremum on that subinterval.) The Darboux integral, which is similar to the Riemann integral but based on Darboux sums, is equivalent to the Riemann integral.

### Riemann integral

Loosely speaking, the Riemann integral is the limit of the Riemann sums of a function as the partitions get finer. If the limit exists then the function is said to be **integrable** (or more specifically **Riemann-integrable**). The Riemann sum can be made as close as desired to the Riemann integral by making the partition fine enough.

One important requirement is that the mesh of the partitions must become smaller and smaller, so that it has the limit zero. If this were not so, then we would not be getting a good approximation to the function on certain subintervals. In fact, this is enough to define an integral. To be specific, we say that the Riemann integral of f exists and equals s if the following condition holds:

> For all *ε* > 0, there exists *δ* > 0 such that for any tagged partition *x*0, ..., *xn* and *t*0, ..., *t**n* − 1 whose mesh is less than δ, we have $\left|\left(\sum _{i=0}^{n-1}f(t_{i})(x_{i+1}-x_{i})\right)-s\right|<\varepsilon .$

Unfortunately, this definition is very difficult to use. It would help to develop an equivalent definition of the Riemann integral which is easier to work with. We develop this definition now, with a proof of equivalence following. Our new definition says that the Riemann integral of f exists and equals s if the following condition holds:

> For all *ε* > 0, there exists a tagged partition *y*0, ..., *ym* and *r*0, ..., *r**m* − 1 such that for any tagged partition *x*0, ..., *xn* and *t*0, ..., *t**n* − 1 which is a refinement of *y*0, ..., *ym* and *r*0, ..., *r**m* − 1, we have $\left|\left(\sum _{i=0}^{n-1}f(t_{i})(x_{i+1}-x_{i})\right)-s\right|<\varepsilon .$

Both of these mean that eventually, the Riemann sum of f with respect to any partition gets trapped close to s. Since this is true no matter how close we demand the sums be trapped, we say that the Riemann sums converge to s. These definitions are actually a special case of a more general concept, a net.

As we stated earlier, these two definitions are equivalent. In other words, s works in the first definition if and only if s works in the second definition. To show that the first definition implies the second, start with an ε, and choose a δ that satisfies the condition. Choose any tagged partition whose mesh is less than δ. Its Riemann sum is within ε of s, and any refinement of this partition will also have mesh less than δ, so the Riemann sum of the refinement will also be within ε of s.

To show that the second definition implies the first, it is easiest to use the Darboux integral. First, one shows that the second definition is equivalent to the definition of the Darboux integral; for this see the Darboux integral article. Now we will show that a Darboux integrable function satisfies the first definition. Fix ε, and choose a partition *y*0, ..., *ym* such that the lower and upper Darboux sums with respect to this partition are within *ε*/2 of the value s of the Darboux integral. Let $r=2\sup _{x\in [a,b]}|f(x)|.$

If *r* = 0, then f is the zero function, which is clearly both Darboux and Riemann integrable with integral zero. Therefore, we will assume that *r* > 0. If *m* > 1, then we choose δ such that $\delta <\min \left\{{\frac {\varepsilon }{2r(m-1)}},\left(y_{1}-y_{0}\right),\left(y_{2}-y_{1}\right),\cdots ,\left(y_{m}-y_{m-1}\right)\right\}$

If *m* = 1, then we choose δ to be less than one. Choose a tagged partition *x*0, ..., *xn* and *t*0, ..., *t**n* − 1 with mesh smaller than δ. We must show that the Riemann sum is within ε of s.

To see this, choose an interval [*xi*, *x**i* + 1]. If this interval is contained within some [*yj*, *y**j* + 1], then $m_{j}\leq f(t_{i})\leq M_{j}$ where mj and Mj are respectively, the infimum and the supremum of *f* on [*yj*, *y**j* + 1]. If all intervals had this property, then this would conclude the proof, because each term in the Riemann sum would be bounded by a corresponding term in the Darboux sums, and we chose the Darboux sums to be near s. This is the case when *m* = 1, so the proof is finished in that case.

Therefore, we may assume that *m* > 1. In this case, it is possible that one of the [*xi*, *x**i* + 1] is not contained in any [*yj*, *y**j* + 1]. Instead, it may stretch across two of the intervals determined by *y*0, ..., *ym*. (It cannot meet three intervals because δ is assumed to be smaller than the length of any one interval.) In symbols, it may happen that $y_{j}<x_{i}<y_{j+1}<x_{i+1}<y_{j+2}.$

(We may assume that all the inequalities are strict because otherwise we are in the previous case by our assumption on the length of δ.) This can happen at most *m* − 1 times.

To handle this case, we will estimate the difference between the Riemann sum and the Darboux sum by subdividing the partition *x*0, ..., *xn* at *y**j* + 1. The term *f*(*ti*)(*x**i* + 1 − *xi*) in the Riemann sum splits into two terms: $f\left(t_{i}\right)\left(x_{i+1}-x_{i}\right)=f\left(t_{i}\right)\left(x_{i+1}-y_{j+1}\right)+f\left(t_{i}\right)\left(y_{j+1}-x_{i}\right).$

Suppose, without loss of generality, that *ti* ∈ [*yj*, *y**j* + 1]. Then $m_{j}\leq f(t_{i})\leq M_{j},$ so this term is bounded by the corresponding term in the Darboux sum for yj. To bound the other term, notice that $x_{i+1}-y_{j+1}<\delta <{\frac {\varepsilon }{2r(m-1)}},$

It follows that, for some (indeed any) *t** *i* ∈ [*y**j* + 1, *x**i* + 1], $\left|f\left(t_{i}\right)-f\left(t_{i}^{*}\right)\right|\left(x_{i+1}-y_{j+1}\right)<{\frac {\varepsilon }{2(m-1)}}.$

Since this happens at most *m* − 1 times, the distance between the Riemann sum and a Darboux sum is at most *ε*/2. Therefore, the distance between the Riemann sum and s is at most ε.

## Examples

Let $f:[0,1]\to \mathbb {R}$ be the function which takes the value 1 at every point. Any Riemann sum of f on [0, 1] will have the value 1, therefore the Riemann integral of f on [0, 1] is 1.

Let $I_{\mathbb {Q} }:[0,1]\to \mathbb {R}$ be the indicator function of the rational numbers in [0, 1]; that is, $I_{\mathbb {Q} }$ takes the value 1 on rational numbers and 0 on irrational numbers. This function does not have a Riemann integral. To prove this, we will show how to construct tagged partitions whose Riemann sums get arbitrarily close to both zero and one.

To start, let *x*0, ..., *xn* and *t*0, ..., *t**n* − 1 be a tagged partition (each ti is between xi and *x**i* + 1). Choose *ε* > 0. The ti have already been chosen, and we can't change the value of f at those points. But if we cut the partition into tiny pieces around each ti, we can minimize the effect of the ti. Then, by carefully choosing the new tags, we can make the value of the Riemann sum turn out to be within ε of either zero or one.

Our first step is to cut up the partition. There are n of the ti, and we want their total effect to be less than ε. If we confine each of them to an interval of length less than *ε*/*n*, then the contribution of each ti to the Riemann sum will be at least 0 · *ε*/*n* and at most 1 · *ε*/*n*. This makes the total sum at least zero and at most ε. So let δ be a positive number less than *ε*/*n*. If it happens that two of the ti are within δ of each other, choose δ smaller. If it happens that some ti is within δ of some xj, and ti is not equal to xj, choose δ smaller. Since there are only finitely many ti and xj, we can always choose δ sufficiently small.

Now we add two cuts to the partition for each ti. One of the cuts will be at *ti* − *δ*/2, and the other will be at *ti* + *δ*/2. If one of these leaves the interval [0, 1], then we leave it out. ti will be the tag corresponding to the subinterval $\left[t_{i}-{\frac {\delta }{2}},t_{i}+{\frac {\delta }{2}}\right].$

If ti is directly on top of one of the xj, then we let ti be the tag for both intervals: $\left[t_{i}-{\frac {\delta }{2}},x_{j}\right],\quad {\text{and}}\quad \left[x_{j},t_{i}+{\frac {\delta }{2}}\right].$

We still have to choose tags for the other subintervals. We will choose them in two different ways. The first way is to always choose a rational point, so that the Riemann sum is as large as possible. This will make the value of the Riemann sum at least 1 − *ε*. The second way is to always choose an irrational point, so that the Riemann sum is as small as possible. This will make the value of the Riemann sum at most ε.

Since we started from an arbitrary partition and ended up as close as we wanted to either zero or one, it is false to say that we are eventually trapped near some number s, so this function is not Riemann integrable. However, it is Lebesgue integrable. In the Lebesgue sense its integral is zero, since the function is zero almost everywhere. But this is a fact that is beyond the reach of the Riemann integral.

There are even worse examples. $I_{\mathbb {Q} }$ is equivalent (that is, equal almost everywhere) to a Riemann integrable function, but there are non-Riemann integrable bounded functions which are not equivalent to any Riemann integrable function. For example, let C be the Smith–Volterra–Cantor set, and let *IC* be its indicator function. Because C is not Jordan measurable, *IC* is not Riemann integrable. Moreover, no function g equivalent to *IC* is Riemann integrable: g, like *IC*, must be zero on a dense set, so as in the previous example, any Riemann sum of g has a refinement which is within ε of 0 for any positive number ε. But if the Riemann integral of g exists, then it must equal the Lebesgue integral of *IC*, which is 1/2. Therefore, g is not Riemann integrable.

## Similar concepts

It is popular to define the Riemann integral as the Darboux integral. This is because the Darboux integral is technically simpler and because a function is Riemann-integrable if and only if it is Darboux-integrable.

Some calculus books do not use general tagged partitions, but limit themselves to specific types of tagged partitions. If the type of partition is limited too much, some non-integrable functions may appear to be integrable.

One popular restriction is the use of "left-hand" and "right-hand" Riemann sums. In a left-hand Riemann sum, *ti* = *xi* for all i, and in a right-hand Riemann sum, *ti* = *x**i* + 1 for all i. Alone this restriction does not impose a problem: we can refine any partition in a way that makes it a left-hand or right-hand sum by subdividing it at each ti. In more formal language, the set of all left-hand Riemann sums and the set of all right-hand Riemann sums is cofinal in the set of all tagged partitions.

Another popular restriction is the use of regular subdivisions of an interval. For example, the nth regular subdivision of [0, 1] consists of the intervals $\left[0,{\frac {1}{n}}\right],\left[{\frac {1}{n}},{\frac {2}{n}}\right],\ldots ,\left[{\frac {n-1}{n}},1\right].$

Again, alone this restriction does not impose a problem, but the reasoning required to see this fact is more difficult than in the case of left-hand and right-hand Riemann sums.

However, combining these restrictions, so that one uses only left-hand or right-hand Riemann sums on regularly divided intervals, is dangerous. If a function is known in advance to be Riemann integrable, then this technique will give the correct value of the integral. But under these conditions the indicator function $I_{\mathbb {Q} }$ will appear to be integrable on [0, 1] with integral equal to one: Every endpoint of every subinterval will be a rational number, so the function will always be evaluated at rational numbers, and hence it will appear to always equal one. The problem with this definition becomes apparent when we try to split the integral into two pieces. The following equation ought to hold: $\int _{0}^{{\sqrt {2}}-1}I_{\mathbb {Q} }(x)\,dx+\int _{{\sqrt {2}}-1}^{1}I_{\mathbb {Q} }(x)\,dx=\int _{0}^{1}I_{\mathbb {Q} }(x)\,dx.$

If we use regular subdivisions and left-hand or right-hand Riemann sums, then the two terms on the left are equal to zero, since every endpoint except 0 and 1 will be irrational, but as we have seen the term on the right will equal 1.

As defined above, the Riemann integral avoids this problem by refusing to integrate $I_{\mathbb {Q} }.$ The Lebesgue integral is defined in such a way that all these integrals are 0.

## Properties

### Linearity

The Riemann integral is a linear transformation; that is, if f and g are Riemann-integrable on [*a*, *b*] and α and β are constants, then $\int _{a}^{b}(\alpha f(x)+\beta g(x))\,dx=\alpha \int _{a}^{b}f(x)\,dx+\beta \int _{a}^{b}g(x)\,dx.$

Because the Riemann integral of a function is a number, this makes the Riemann integral a linear functional on the vector space of Riemann-integrable functions.

## Integrability

A bounded function on a compact interval [*a*, *b*] is Riemann integrable if and only if it is continuous almost everywhere (the set of its points of discontinuity has measure zero, in the sense of Lebesgue measure). This is the **Lebesgue-Vitali theorem** (of characterization of the Riemann integrable functions). It has been proven independently by Giuseppe Vitali and by Henri Lebesgue in 1907, and uses the notion of measure zero, but makes use of neither Lebesgue's general measure or integral.

The integrability condition can be proven in various ways, one of which is sketched below.

| Proof |
|---|
| The proof is easiest using the Darboux integral definition of integrability (formally, the Riemann condition for integrability) – a function is Riemann integrable if and only if the upper and lower sums can be made arbitrarily close by choosing an appropriate partition. One direction can be proven using the oscillation definition of continuity: For every positive ε, Let *X**ε* be the set of points in [*a*, *b*] with oscillation of at least ε. Since every point where f is discontinuous has a positive oscillation and vice versa, the set of points in [*a*, *b*], where f is discontinuous is equal to the union over {*X*1/*n*} for all natural numbers n. If this set does not have zero Lebesgue measure, then by countable additivity of the measure there is at least one such n so that *X*1/*n* does not have a zero measure. Thus there is some positive number c such that every countable collection of open intervals covering *X*1/*n* has a total length of at least c. In particular this is also true for every such finite collection of intervals. This remains true also for *X*1/*n* less a finite number of points (as a finite number of points can always be covered by a finite collection of intervals with arbitrarily small total length). For every partition of [*a*, *b*], consider the set of intervals whose interiors include points from *X*1/*n*. These interiors consist of a finite open cover of *X*1/*n*, possibly up to a finite number of points (which may fall on interval edges). Thus these intervals have a total length of at least c. Since in these points f has oscillation of at least 1/*n*, the infimum and supremum of f in each of these intervals differ by at least 1/*n*. Thus the upper and lower sums of f differ by at least *c*/*n*. Since this is true for every partition, f is not Riemann integrable. We now prove the converse direction using the sets *X**ε* defined above. For every ε, *X**ε* is compact, as it is bounded (by a and b) and closed: For every series of points in *X**ε* that is converging in [*a*, *b*], its limit is in *X**ε* as well. This is because every neighborhood of the limit point is also a neighborhood of some point in *X**ε*, and thus f has an oscillation of at least ε on it. Hence the limit point is in *X**ε*. Now, suppose that f is continuous almost everywhere. Then for every ε, *X**ε* has zero Lebesgue measure. Therefore, there is a countable collections of open intervals in [*a*, *b*] which is an open cover of *X**ε*, such that the sum over all their lengths is arbitrarily small. Since *X**ε* is compact, there is a finite subcover – a finite collections of open intervals in [*a*, *b*] with arbitrarily small total length that together contain all points in *X**ε*. We denote these intervals {*I*(*ε*)*i*}, for 1 ≤ *i* ≤ *k*, for some natural k. The complement of the union of these intervals is itself a union of a finite number of intervals, which we denote {*J*(*ε*)*i*} (for 1 ≤ *i* ≤ *k* − 1 and possibly for *i* = *k*, *k* + 1 as well). We now show that for every *ε* > 0, there are upper and lower sums whose difference is less than ε, from which Riemann integrability follows. To this end, we construct a partition of [*a*, *b*] as follows: Denote *ε*1 = *ε* / 2(*b* − *a*) and *ε*2 = *ε* / 2(*M* − *m*), where m and M are the infimum and supremum of f on [*a*, *b*]. Since we may choose intervals {*I*(*ε*1)*i*} with arbitrarily small total length, we choose them to have total length smaller than *ε*2. Each of the intervals {*J*(*ε*1)*i*} has an empty intersection with *X**ε*1, so each point in it has a neighborhood with oscillation smaller than *ε*1. These neighborhoods consist of an open cover of the interval, and since the interval is compact there is a finite subcover of them. This subcover is a finite collection of open intervals, which are subintervals of *J*(*ε*1)*i* (except for those that include an edge point, for which we only take their intersection with *J*(*ε*1)*i*). We take the edge points of the subintervals for all *J*(*ε*1)*i* − *s*, including the edge points of the intervals themselves, as our partition. Thus the partition divides [*a*, *b*] to two kinds of intervals: Intervals of the latter kind (themselves subintervals of some *J*(*ε*1)*i*). In each of these, f oscillates by less than *ε*1. Since the total length of these is not larger than *b* − *a*, they together contribute at most *ε* 1(*b* − *a*) = *ε*/2 to the difference between the upper and lower sums of the partition. The intervals {*I*(*ε*)*i*}. These have total length smaller than *ε*2, and f oscillates on them by no more than *M* − *m*. Thus together they contribute less than *ε* 2(*M* − *m*) = *ε*/2 to the difference between the upper and lower sums of the partition. In total, the difference between the upper and lower sums of the partition is smaller than ε, as required. |

In particular, any set that is at most countable has Lebesgue measure zero, and thus a bounded function (on a compact interval) with only finitely or countably many discontinuities is Riemann integrable. Another sufficient criterion to Riemann integrability over [*a*, *b*], but which does not involve the concept of measure, is the existence of a right-hand (or left-hand) limit at *every* point in [*a*, *b*) (or (*a*, *b*]).

An indicator function of a bounded set is Riemann-integrable if and only if the set is Jordan measurable. The Riemann integral can be interpreted measure-theoretically as the integral with respect to the Jordan measure.

If a real-valued function is monotone on the interval [*a*, *b*] it is Riemann integrable, since its set of discontinuities is at most countable, and therefore of Lebesgue measure zero. If a real-valued function on [*a*, *b*] is Riemann integrable, it is Lebesgue integrable. That is, Riemann-integrability is a *stronger* (meaning more difficult to satisfy) condition than Lebesgue-integrability. The converse does not hold; not all Lebesgue-integrable functions are Riemann integrable.

The Lebesgue–Vitali theorem does not imply that all type of discontinuities have the same weight on the obstruction that a real-valued bounded function be Riemann integrable on [*a*, *b*]. In fact, certain discontinuities have absolutely no role on the Riemann integrability of the function—a consequence of the classification of the discontinuities of a function.

If *f**n* is a uniformly convergent sequence on [*a*, *b*] with limit f, then Riemann integrability of all *f**n* implies Riemann integrability of f, and $\int _{a}^{b}f\,dx=\int _{a}^{b}{\lim _{n\to \infty }{f_{n}}\,dx}=\lim _{n\to \infty }\int _{a}^{b}f_{n}\,dx.$

However, the Lebesgue monotone convergence theorem (on a monotone pointwise limit) does not hold for Riemann integrals. Thus, in Riemann integration, taking limits under the integral sign is far more difficult to logically justify than in Lebesgue integration.

## Generalizations

It is easy to extend the Riemann integral to functions with values in the Euclidean vector space $\mathbb {R} ^{n}$ for any n. The integral is defined component-wise; in other words, if **f** = (*f*1, ..., *f**n*) then $\int \mathbf {f} =\left(\int f_{1},\,\dots ,\int f_{n}\right).$

In particular, since the complex numbers are a real vector space, this allows the integration of complex valued functions.

The Riemann integral is only defined on bounded intervals, and it does not extend well to unbounded intervals. The simplest possible extension is to define such an integral as a limit, in other words, as an improper integral: $\int _{-\infty }^{\infty }f(x)\,dx=\lim _{a\to -\infty \atop b\to \infty }\int _{a}^{b}f(x)\,dx.$

This definition carries with it some subtleties, such as the fact that it is not always equivalent to compute the Cauchy principal value $\lim _{a\to \infty }\int _{-a}^{a}f(x)\,dx.$

For example, consider the sign function *f*(*x*) = sgn(*x*) which is 0 at *x* = 0, 1 for *x* > 0, and −1 for *x* < 0. By symmetry, $\int _{-a}^{a}f(x)\,dx=0$ always, regardless of a. But there are many ways for the interval of integration to expand to fill the real line, and other ways can produce different results; in other words, the multivariate limit does not always exist. We can compute ${\begin{aligned}\int _{-a}^{2a}f(x)\,dx&=a,\\\int _{-2a}^{a}f(x)\,dx&=-a.\end{aligned}}$

In general, this improper Riemann integral is undefined. Even standardizing a way for the interval to approach the real line does not work because it leads to disturbingly counterintuitive results. If we agree (for instance) that the improper integral should always be $\lim _{a\to \infty }\int _{-a}^{a}f(x)\,dx,$ then the integral of the translation *f*(*x* − 1) is −2, so this definition is not invariant under shifts, a highly undesirable property. In fact, not only does this function not have an improper Riemann integral, its Lebesgue integral is also undefined (it equals ∞ − ∞).

Unfortunately, the improper Riemann integral is not powerful enough. The most severe problem is that there are no widely applicable theorems for commuting improper Riemann integrals with limits of functions. In applications such as Fourier series it is important to be able to approximate the integral of a function using integrals of approximations to the function. For proper Riemann integrals, a standard theorem states that if *fn* is a sequence of functions that converge uniformly to f on a compact set [*a*, *b*], then $\lim _{n\to \infty }\int _{a}^{b}f_{n}(x)\,dx=\int _{a}^{b}f(x)\,dx.$

On non-compact intervals such as the real line, this is false. For example, take *fn*(*x*) to be *n*−1 on [0, *n*] and zero elsewhere. For all n we have: $\int _{-\infty }^{\infty }f_{n}\,dx=1.$

The sequence (*fn*) converges uniformly to the zero function, and clearly the integral of the zero function is zero. Consequently, $\int _{-\infty }^{\infty }f\,dx\neq \lim _{n\to \infty }\int _{-\infty }^{\infty }f_{n}\,dx.$

This demonstrates that for integrals on unbounded intervals, uniform convergence of a function is not strong enough to allow passing a limit through an integral sign. This makes the Riemann integral unworkable in applications (even though the Riemann integral assigns both sides the correct value), because there is no other general criterion for exchanging a limit and a Riemann integral, and without such a criterion it is difficult to approximate integrals by approximating their integrands.

A better route is to abandon the Riemann integral for the Lebesgue integral. The definition of the Lebesgue integral is not obviously a generalization of the Riemann integral, but it is not hard to prove that every Riemann-integrable function is Lebesgue-integrable and that the values of the two integrals agree whenever they are both defined. Moreover, a function f defined on a bounded interval is Riemann-integrable if and only if it is bounded and the set of points where f is discontinuous has Lebesgue measure zero.

An integral which is in fact a direct generalization of the Riemann integral is the Henstock–Kurzweil integral.

Another way of generalizing the Riemann integral is to replace the factors *x**k* + 1 − *x**k* in the definition of a Riemann sum by something else; roughly speaking, this gives the interval of integration a different notion of length. This is the approach taken by the Riemann–Stieltjes integral.

In multivariable calculus, the Riemann integrals for functions from $\mathbb {R} ^{n}\to \mathbb {R}$ are multiple integrals.

## Comparison with other theories of integration

The Riemann integral is unsuitable for many theoretical purposes. Some of the technical deficiencies in Riemann integration can be remedied with the Riemann–Stieltjes integral, and most disappear with the Lebesgue integral, though the latter does not have a satisfactory treatment of improper integrals. The gauge integral is a generalisation of the Lebesgue integral that is at the same time closer to the Riemann integral. These more general theories allow for the integration of more "jagged" or "highly oscillating" functions whose Riemann integral does not exist; but the theories give the same value as the Riemann integral when it does exist.

In educational settings, the Darboux integral offers a simpler definition that is easier to work with; it can be used to introduce the Riemann integral. The Darboux integral is defined whenever the Riemann integral is, and always gives the same result. Conversely, the gauge integral is a simple but more powerful generalization of the Riemann integral and has led some educators to advocate that it should replace the Riemann integral in introductory calculus courses.
