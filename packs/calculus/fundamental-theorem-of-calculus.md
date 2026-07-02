---
title: "Fundamental theorem of calculus"
source: https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus
domain: calculus
license: CC-BY-SA-4.0
tags: calculus, differential calculus, integral calculus, differentiation, antiderivative
fetched: 2026-07-02
---

# Fundamental theorem of calculus

The **fundamental theorem of calculus** is a theorem that links the concept of differentiating a function (calculating its slopes, or rate of change at every point on its domain) with the concept of integrating a function (calculating the area under its graph, or the cumulative effect of small contributions). Roughly speaking, the two operations can be thought of as inverses of each other.

The first part of the theorem, the **first fundamental theorem of calculus**, states that for a continuous function f , an antiderivative or indefinite integral F can be obtained as the integral of f over an interval with a variable upper bound.

Conversely, the second part of the theorem, the **second fundamental theorem of calculus**, states that the integral of a function f over a fixed interval is equal to the change of any antiderivative F between the ends of the interval. This greatly simplifies the calculation of a definite integral provided an antiderivative can be found by symbolic integration, thus avoiding numerical integration.

## History

The fundamental theorem of calculus relates differentiation and integration, showing that these two operations are essentially inverses of one another. Before the discovery of this theorem, it was not recognized that these two operations were related. Ancient Greek mathematicians knew how to compute area via infinitesimals, an operation that we would now call integration. The origins of differentiation likewise predate the fundamental theorem of calculus by hundreds of years; for example, in the fourteenth century the notions of *continuity* of functions and *motion* were studied by the Oxford Calculators and other scholars. The historical relevance of the fundamental theorem of calculus is not the ability to calculate these operations, but the realization that the two seemingly distinct operations (calculation of geometric areas, and calculation of gradients) are actually closely related.

Calculus as a unified theory of integration and differentiation started from the conjecture and the proof of the fundamental theorem of calculus. The first published statement and proof of a rudimentary form of the fundamental theorem, strongly geometric in character, was by James Gregory (1638–1675). Isaac Barrow (1630–1677) proved a more generalized version of the theorem, while his student Isaac Newton (1642–1727) completed the development of the surrounding mathematical theory. Gottfried Leibniz (1646–1716) systematized the knowledge into a calculus for infinitesimal quantities and introduced the notation used today.

## Sketch of geometric proof

The first fundamental theorem may be interpreted as follows. Given a continuous function $y=f(x)$ whose graph is plotted as a curve, one defines a corresponding "area function" $x\mapsto A(x)$ such that *A*(*x*) is the area beneath the curve between 0 and x. The area *A*(*x*) may not be easily computable, but it is assumed to be well defined.

The area under the curve between x and *x* + *h* could be computed by finding the area between 0 and *x* + *h*, then subtracting the area between 0 and x. In other words, the area of this "strip" would be *A*(*x* + *h*) − *A*(*x*).

There is another way to *estimate* the area of this same strip. As shown in the accompanying figure, h is multiplied by *f*(*x*) to find the area of a rectangle that is approximately the same size as this strip. So: $A(x+h)-A(x)\approx f(x)\cdot h$

Dividing by h on both sides, we get: ${\frac {A(x+h)-A(x)}{h}}\approx f(x)$

This estimate becomes a perfect equality when h approaches 0: $f(x)=\lim _{h\to 0}{\frac {A(x+h)-A(x)}{h}}\ {\stackrel {\text{def}}{=}}\ A'(x).$ That is, the derivative of the area function *A*(*x*) exists and is equal to the original function *f*(*x*), so the area function is an antiderivative of the original function.

Thus, the derivative of the integral of a function (the area) is the original function, so that derivative and integral are inverse operations which reverse each other. This is the essence of the Fundamental Theorem.

## Intuitive understanding

Intuitively, the fundamental theorem states that *integration* and *differentiation* are inverse operations which reverse each other.

The second fundamental theorem says that the sum of infinitesimal changes in a quantity (the integral of the derivative of the quantity) adds up to the net change in the quantity. To visualize this, imagine traveling in a car and wanting to know the distance traveled (the net change in position along the highway). You can see the velocity on the speedometer but cannot look out to see your location. Each second, you can find how far the car has traveled using distance = speed × time, that is, multiplying the current speed (in kilometers or miles per hour) by the time interval (1 second = ${\tfrac {1}{3600}}$ hour). By summing up all these small steps, you can approximate the total distance traveled, in spite of not looking outside the car: ${\text{distance traveled}}=\sum \left({\begin{array}{c}{\text{velocity at}}\\{\text{each time}}\end{array}}\right)\times \left({\begin{array}{c}{\text{time}}\\{\text{interval}}\end{array}}\right)=\sum v_{t}\times \Delta t.$ As $\Delta t$ becomes infinitesimally small, the summing up corresponds to integration. Thus, the integral of the velocity function (the derivative of position) computes how far the car has traveled (the net change in position).

The first fundamental theorem says that the value of any function is the rate of change (the derivative) of its integral from a fixed starting point up to any chosen end point. Continuing the above example using a velocity as the function, you can integrate it from the starting time up to any given time to obtain a distance function whose derivative is that velocity. (To obtain your highway-marker position, you would need to add your starting position to this integral and to take into account whether your travel was in the direction of increasing or decreasing mile markers.)

## Formal statements

There are two parts to the theorem. The first part deals with the derivative of an antiderivative, while the second part deals with the relationship between antiderivatives and definite integrals. The terminology on this topic has not been completely standardized. For convenience, this article uses one of the common conventions. The conventions adopted in other sources are discussed later.

### First part

This part is sometimes referred to as the *first fundamental theorem of calculus*.

Let f be a continuous real-valued function defined on a closed interval [*a*, *b*]. Let F be the function defined, for all x in [*a*, *b*], by $F(x)=\int _{a}^{x}f(t)\,dt.$

Then F is uniformly continuous on [*a*, *b*] and differentiable on the open interval (*a*, *b*), and $F'(x)=f(x)$ for all x in (*a*, *b*) so F is an antiderivative of f.

### Corollary

The fundamental theorem is often employed to compute the definite integral of a function f for which an antiderivative F is known. Specifically, if f is a real-valued continuous function on $[a,b]$ and F is an antiderivative of f in $[a,b]$ , then $\int _{a}^{b}f(t)\,dt=F(b)-F(a).$

The corollary assumes continuity on the whole interval. This result is strengthened slightly in the following part of the theorem.

### Second part

This part is sometimes referred to as the *second fundamental theorem of calculus* or the **Newton–Leibniz theorem**.

Let f be a real-valued function on a closed interval $[a,b]$ and F a continuous function on $[a,b]$ which is an antiderivative of f in $(a,b)$ : $F'(x)=f(x).$

If f is Riemann integrable on $[a,b]$ then $\int _{a}^{b}f(x)\,dx=F(b)-F(a).$

The second part is somewhat stronger than the corollary because it does not assume that f is continuous.

When an antiderivative F of f exists, then there are infinitely many antiderivatives for f , obtained by adding an arbitrary constant to F . Also, by the first part of the theorem, antiderivatives of f always exist when f is continuous.

## Proof of the first part

For a given function *f*, define the function *F*(*x*) as $F(x)=\int _{a}^{x}f(t)\,dt.$

For any two numbers *x*1 and *x*1 + Δ*x* in [*a*, *b*], we have

${\begin{aligned}F(x_{1}+\Delta x)-F(x_{1})&=\int _{a}^{x_{1}+\Delta x}f(t)\,dt-\int _{a}^{x_{1}}f(t)\,dt\\&=\int _{x_{1}}^{x_{1}+\Delta x}f(t)\,dt,\end{aligned}}$ the latter equality resulting from the basic properties of integrals and the additivity of areas.

According to the mean value theorem for integration, there exists a real number $c\in [x_{1},x_{1}+\Delta x]$ such that $\int _{x_{1}}^{x_{1}+\Delta x}f(t)\,dt=f(c)\cdot \Delta x.$

It follows that $F(x_{1}+\Delta x)-F(x_{1})=f(c)\cdot \Delta x,$ and thus that ${\frac {F(x_{1}+\Delta x)-F(x_{1})}{\Delta x}}=f(c).$

Taking the limit as $\Delta x\to 0,$ and keeping in mind that $c\in [x_{1},x_{1}+\Delta x],$ one gets $\lim _{\Delta x\to 0}{\frac {F(x_{1}+\Delta x)-F(x_{1})}{\Delta x}}=\lim _{\Delta x\to 0}f(c),$ that is, $F'(x_{1})=f(x_{1}),$ according to the definition of the derivative, the continuity of f, and the squeeze theorem.

## Proof of the corollary

Suppose F is an antiderivative of f, with f continuous on [*a*, *b*]. Let $G(x)=\int _{a}^{x}f(t)\,dt.$

By the *first part* of the theorem, we know G is also an antiderivative of f. Since *F*′ − *G*′ = 0 the mean value theorem implies that *F* − *G* is a constant function, that is, there is a number c such that *G*(*x*) = *F*(*x*) + *c* for all x in [*a*, *b*]. Letting *x* = *a*, we have $F(a)+c=G(a)=\int _{a}^{a}f(t)\,dt=0,$ which means *c* = −*F*(*a*). In other words, *G*(*x*) = *F*(*x*) − *F*(*a*), and so $\int _{a}^{b}f(x)\,dx=G(b)=F(b)-F(a).$

## Proof of the second part

This is a limit proof by Riemann sums.

To begin, we recall the mean value theorem. Stated briefly, if F is continuous on the closed interval [*a*, *b*] and differentiable on the open interval (*a*, *b*), then there exists some c in (*a*, *b*) such that $F'(c)(b-a)=F(b)-F(a).$

Let f be (Riemann) integrable on the interval [*a*, *b*], and let f admit an antiderivative F on (*a*, *b*) such that F is continuous on [*a*, *b*]. Begin with the quantity *F*(*b*) − *F*(*a*). Let there be numbers *x*0, ..., *x**n* such that $a=x_{0}<x_{1}<x_{2}<\cdots <x_{n-1}<x_{n}=b.$

It follows that $F(b)-F(a)=F(x_{n})-F(x_{0}).$

Now, we add each *F*(*x**i*) along with its additive inverse, so that the resulting quantity is equal: ${\begin{aligned}F(b)-F(a)&=F(x_{n})+[-F(x_{n-1})+F(x_{n-1})]+\cdots +[-F(x_{1})+F(x_{1})]-F(x_{0})\\&=[F(x_{n})-F(x_{n-1})]+[F(x_{n-1})-F(x_{n-2})]+\cdots +[F(x_{2})-F(x_{1})]+[F(x_{1})-F(x_{0})].\end{aligned}}$

The above quantity can be written as the following sum:

| $F(b)-F(a)=\sum _{i=1}^{n}[F(x_{i})-F(x_{i-1})].$ |   | 1' |
|---|---|---|

The function F is differentiable on the interval (*a*, *b*) and continuous on the closed interval [*a*, *b*]; therefore, it is also differentiable on each interval (*x**i*−1, *x**i*) and continuous on each interval [*x**i*−1, *x**i*]. According to the mean value theorem (above), for each i there exists a $c_{i}$ in (*x**i*−1, *x**i*) such that $F(x_{i})-F(x_{i-1})=F'(c_{i})(x_{i}-x_{i-1}).$

Substituting the above into (**1'**), we get $F(b)-F(a)=\sum _{i=1}^{n}[F'(c_{i})(x_{i}-x_{i-1})].$

The assumption implies $F'(c_{i})=f(c_{i}).$ Also, $x_{i}-x_{i-1}$ can be expressed as $\Delta x$ of partition i .

| $F(b)-F(a)=\sum _{i=1}^{n}[f(c_{i})(\Delta x_{i})].$ |   | 2' |
|---|---|---|

We are describing the area of a rectangle, with the width times the height, and we are adding the areas together. Each rectangle, by virtue of the mean value theorem, describes an approximation of the curve section it is drawn over. Also $\Delta x_{i}$ need not be the same for all values of i, or in other words that the width of the rectangles can differ. What we have to do is approximate the curve with n rectangles. Now, as the size of the partitions get smaller and n increases, resulting in more partitions to cover the space, we get closer and closer to the actual area of the curve.

By taking the limit of the expression as the norm of the partitions approaches zero, we arrive at the Riemann integral. We know that this limit exists because f was assumed to be integrable. That is, we take the limit as the largest of the partitions approaches zero in size, so that all other partitions are smaller and the number of partitions approaches infinity.

So, we take the limit on both sides of (**2'**). This gives us $\lim _{\|\Delta x_{i}\|\to 0}F(b)-F(a)=\lim _{\|\Delta x_{i}\|\to 0}\sum _{i=1}^{n}[f(c_{i})(\Delta x_{i})].$

Neither *F*(*b*) nor *F*(*a*) is dependent on $\|\Delta x_{i}\|$ , so the limit on the left side remains *F*(*b*) − *F*(*a*). $F(b)-F(a)=\lim _{\|\Delta x_{i}\|\to 0}\sum _{i=1}^{n}[f(c_{i})(\Delta x_{i})].$

The expression on the right side of the equation defines the integral over f from a to b. Therefore, we obtain $F(b)-F(a)=\int _{a}^{b}f(x)\,dx,$ which completes the proof.

## Relationship between the parts

As discussed above, a slightly weaker version of the second part follows from the first part.

Similarly, it almost looks like the first part of the theorem follows directly from the second. That is, suppose G is an antiderivative of f. Then by the second theorem, ${\textstyle G(x)-G(a)=\int _{a}^{x}f(t)\,dt}$ . Now, suppose ${\textstyle F(x)=\int _{a}^{x}f(t)\,dt=G(x)-G(a)}$ . Then F has the same derivative as G, and therefore *F*′ = *f*. This argument only works, however, if we already know that f has an antiderivative, and the only way we know that all continuous functions have antiderivatives is by the first part of the Fundamental Theorem. For example, if *f*(*x*) = *e*−*x*2, then f has an antiderivative, namely $G(x)=\int _{0}^{x}f(t)\,dt$ and there is no simpler expression for this function. It is therefore important not to interpret the second part of the theorem as the definition of the integral. Indeed, there are many functions that are integrable but lack elementary antiderivatives, and discontinuous functions can be integrable but lack any antiderivatives at all. Conversely, many functions that have antiderivatives are not Riemann integrable (see Volterra's function).

## Examples

### Computing a particular integral

Suppose the following is to be calculated: $\int _{2}^{5}x^{2}\,dx.$

Here, $f(x)=x^{2}$ and we can use ${\textstyle F(x)={\frac {1}{3}}x^{3}}$ as the antiderivative. Therefore: $\int _{2}^{5}x^{2}\,dx=F(5)-F(2)={\frac {5^{3}}{3}}-{\frac {2^{3}}{3}}={\frac {125}{3}}-{\frac {8}{3}}={\frac {117}{3}}=39.$

### Using the first part

Suppose ${\frac {d}{dx}}\int _{0}^{x}t^{3}\,dt$ is to be calculated. Using the first part of the theorem with $f(t)=t^{3}$ gives ${\frac {d}{dx}}\int _{0}^{x}t^{3}\,dt=f(x)=x^{3}.$

This can also be checked using the second part of the theorem. Specifically, ${\textstyle F(t)={\frac {1}{4}}t^{4}}$ is an antiderivative of $f(t)$ , so ${\frac {d}{dx}}\int _{0}^{x}t^{3}\,dt={\frac {d}{dx}}F(x)-{\frac {d}{dx}}F(0)={\frac {d}{dx}}{\frac {x^{4}}{4}}=x^{3}.$

### An integral where the corollary is insufficient

Suppose $f(x)={\begin{cases}\sin \left({\frac {1}{x}}\right)-{\frac {1}{x}}\cos \left({\frac {1}{x}}\right)&x\neq 0\\0&x=0\\\end{cases}}$ Then $f(x)$ is not continuous at zero. Moreover, this is not just a matter of how f is defined at zero, since the limit as $x\to 0$ of $f(x)$ does not exist. Therefore, the corollary cannot be used to compute $\int _{0}^{1}f(x)\,dx.$ But consider the function $F(x)={\begin{cases}x\sin \left({\frac {1}{x}}\right)&x\neq 0\\0&x=0.\\\end{cases}}$ Notice that $F(x)$ is continuous on $[0,1]$ (including at zero by the squeeze theorem), and $F(x)$ is differentiable on $(0,1)$ with $F'(x)=f(x).$ Therefore, part two of the theorem applies, and $\int _{0}^{1}f(x)\,dx=F(1)-F(0)=\sin(1).$

### Theoretical example

The theorem can be used to prove that $\int _{a}^{b}f(x)dx=\int _{a}^{c}f(x)dx+\int _{c}^{b}f(x)dx.$

Since, ${\begin{aligned}\int _{a}^{b}f(x)dx&=F(b)-F(a),\\\int _{a}^{c}f(x)dx&=F(c)-F(a),{\text{ and }}\\\int _{c}^{b}f(x)dx&=F(b)-F(c),\end{aligned}}$ the result follows from, $F(b)-F(a)=F(c)-F(a)+F(b)-F(c).$

## Variations in terminology

The mathematics literature is not completely consistent as to which result should be called the *first* fundamental theorem of calculus and which should be called the *second.* In this article, the first fundamental theorem is that, if one is given a continuous function f and defines a new function by $F(x)=\int _{a}^{x}f(t)\,dt$ , then $F'(x)=f(x)$ . Apostol's calculus series uses this terminology, and similarly, Strang et al. call this "part 1" of the fundamental theorem of calculus. Multiple other texts also call this result the first fundamental theorem or the fundamental theorem's first part.

On the other hand, Larson and Edwards adopt a different convention, in which "the fundamental theorem" is that the definite integral is the change of the antiderivative, $F(x)-F(c)=\int _{c}^{x}f(t)\,dt\,$ for a continuous function f . That is, this article's "corollary" is designated "the fundamental theorem", while the "second fundamental theorem" is what Apostol calls the first. Other textbooks also call this article's "second fundamental theorem", or a weaker form of it that assumes continuity, the first.

Salas and Hille's *Calculus: One and Several Variables* (1971) says that the latter expression in the special case of continuous f (this article's "corollary") is "the fundamental theorem of integral calculus", while this article's "first part" is just the un-named Theorem 4.3.2. Similarly, some other works call this article's "second part" *the* fundamental theorem while leaving the other part un-named.

Boyer's *History of the Calculus* first explains "what is commonly known as the fundamental theorem of the calculus": that if $F(x)=\int _{a}^{x}f(t)\,dt$ , then $F'(x)=f(x)$ . For Boyer, our "first part" is "the fundamental theorem". Then, Boyer writes that the difference of the antiderivatives $F(b)-F(a)$ "is occasionally taken as the definition" of the integral $\int _{a}^{b}f(x)\,dx$ . And in *that* case, $\int _{a}^{b}f(x)\,dx=\lim _{n\to \infty }\sum _{i=1}^{n}f(x_{i})\Delta x_{i}$ is "the fundamental theorem".

## Generalizations

The function f does not have to be continuous over the whole interval. Part I of the theorem then says: if f is any Lebesgue integrable function on [*a*, *b*] and *x*0 is a number in [*a*, *b*] such that f is continuous at *x*0, then $F(x)=\int _{a}^{x}f(t)\,dt$

is differentiable for *x* = *x*0 with *F*′(*x*0) = *f*(*x*0). We can relax the conditions on f still further and suppose that it is merely locally integrable. In that case, we can conclude that the function F is differentiable almost everywhere and *F*′(*x*) = *f*(*x*) almost everywhere. On the real line this statement is equivalent to Lebesgue's differentiation theorem. These results remain true for the Henstock–Kurzweil integral, which allows a larger class of integrable functions.

In higher dimensions Lebesgue's differentiation theorem generalizes the Fundamental theorem of calculus by stating that for almost every x, the average value of a function f over a ball of radius r centered at x tends to *f*(*x*) as r tends to 0.

Part II of the theorem is true for any Lebesgue integrable function f, which has an antiderivative F (not all integrable functions do, though). In other words, if a real function F on [*a*, *b*] admits a derivative *f*(*x*) at *every* point x of [*a*, *b*] and if this derivative f is Lebesgue integrable on [*a*, *b*], then $F(b)-F(a)=\int _{a}^{b}f(t)\,dt.$

This result may fail for continuous functions F that admit a derivative *f*(*x*) at almost every point x, as the example of the Cantor function shows. However, if F is absolutely continuous, it admits a derivative *F′*(*x*) at almost every point x, and moreover F′ is integrable, with *F*(*b*) − *F*(*a*) equal to the integral of F′ on [*a*, *b*]. Conversely, if f is any integrable function, then F as given in the first formula will be absolutely continuous with *F′* = *f* almost everywhere.

The conditions of this theorem may again be relaxed by considering the integrals involved as Henstock–Kurzweil integrals. Specifically, if a continuous function *F*(*x*) admits a derivative *f*(*x*) at all but countably many points, then *f*(*x*) is Henstock–Kurzweil integrable and *F*(*b*) − *F*(*a*) is equal to the integral of f on [*a*, *b*]. The difference here is that the integrability of f does not need to be assumed.

The version of Taylor's theorem that expresses the error term as an integral can be seen as a generalization of the fundamental theorem.

There is a version of the theorem for complex functions: suppose U is an open set in **C** and *f* : *U* → **C** is a function that has a holomorphic antiderivative F on U. Then for every curve γ : [*a*, *b*] → *U*, the curve integral can be computed as $\int _{\gamma }f(z)\,dz=F(\gamma (b))-F(\gamma (a)).$

The fundamental theorem can be generalized to curve and surface integrals in higher dimensions and on manifolds. One such generalization offered by the calculus of moving surfaces is the time evolution of integrals. The most familiar extensions of the fundamental theorem of calculus in higher dimensions are the divergence theorem and the gradient theorem.

One of the most powerful generalizations in this direction is the generalized Stokes theorem (sometimes known as the fundamental theorem of multivariable calculus): Let M be an oriented piecewise smooth manifold of dimension n and let $\omega$ be a smooth compactly supported (*n* − 1)-form on M. If ∂*M* denotes the boundary of M given its induced orientation, then $\int _{M}d\omega =\int _{\partial M}\omega .$

Here *d* is the exterior derivative, which is defined using the manifold structure only.

The theorem is often used in situations where M is an embedded oriented submanifold of some bigger manifold (e.g. **R***k*) on which the form $\omega$ is defined.

The fundamental theorem of calculus allows us to pose a definite integral as a first-order ordinary differential equation. $\int _{a}^{b}f(x)\,dx$ can be posed as ${\frac {dy}{dx}}=f(x),\;\;y(a)=0$ with $y(b)$ as the value of the integral.
