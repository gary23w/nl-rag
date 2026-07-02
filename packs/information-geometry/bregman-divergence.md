---
title: "Bregman divergence"
source: https://en.wikipedia.org/wiki/Bregman_divergence
domain: information-geometry
license: CC-BY-SA-4.0
tags: information geometry, fisher information metric, statistical manifold, bregman divergence
fetched: 2026-07-02
---

# Bregman divergence

In mathematics, specifically statistics and information geometry, a **Bregman divergence** or **Bregman distance** is a measure of difference between two points, defined in terms of a strictly convex function; they form an important class of divergences. When the points are interpreted as probability distributions – notably as either values of the parameter of a parametric model or as a data set of observed values – the resulting distance is a statistical distance. The most basic Bregman divergence is the squared Euclidean distance.

Bregman divergences are similar to metrics, but satisfy neither the triangle inequality (ever) nor symmetry (in general). However, they satisfy a generalization of the Pythagorean theorem, and in information geometry the corresponding statistical manifold is interpreted as a (dually) flat manifold. This allows many techniques of optimization theory to be generalized to Bregman divergences, geometrically as generalizations of least squares.

Bregman divergences are named after Soviet and Israeli mathematician Lev M. Bregman, who introduced the concept in 1967.

## Definition

Let $F\colon \Omega \to \mathbb {R}$ be a continuously-differentiable, strictly convex function defined on a convex set $\Omega$ .

The Bregman distance associated with *F* for points $p,q\in \Omega$ is the difference between the value of *F* at point *p* and the value of the first-order Taylor expansion of *F* around point *q* evaluated at point *p*: $D_{F}(p,q)=F(p)-F(q)-\langle \nabla F(q),p-q\rangle .$

## Properties

- **Non-negativity**: $D_{F}(p,q)\geq 0$ for all p , q . This is a consequence of the convexity of F .
- **Positivity**: When F is strictly convex, $D_{F}(p,q)=0$ if and only if $p=q$ .
- **Uniqueness up to affine difference**: $D_{F}=D_{G}$ if and only if $F-G$ is an affine function.
- **Convexity**: $D_{F}(p,q)$ is convex in its first argument, but not necessarily in the second argument. If F is strictly convex, then $D_{F}(p,q)$ is strictly convex in its first argument.
  - For example, Take *f*(*x*) = |*x*|, smooth it at 0, then take $y=1,x_{1}=0.1,x_{2}=-0.9,x_{3}=0.9x_{1}+0.1x_{2}$ , then $D_{f}(y,x_{3})\approx 1>0.9D_{f}(y,x_{1})+0.1D_{f}(y,x_{2})\approx 0.2$ .
- **Linearity**: If we think of the Bregman distance as an operator on the function *F*, then it is linear with respect to non-negative coefficients. In other words, for $F_{1},F_{2}$ strictly convex and differentiable, and $\lambda \geq 0$ , $D_{F_{1}+\lambda F_{2}}(p,q)=D_{F_{1}}(p,q)+\lambda D_{F_{2}}(p,q)$
- **Duality**: If F is strictly convex, then the function F has a convex conjugate $F^{*}$ which is also strictly convex and continuously differentiable on some convex set $\Omega ^{*}$ . The Bregman distance defined with respect to $F^{*}$ is dual to $D_{F}(p,q)$ as $D_{F^{*}}(p^{*},q^{*})=D_{F}(q,p)$ Here, $p^{*}=\nabla F(p)$ and $q^{*}=\nabla F(q)$ are the dual points corresponding to *p* and *q*.Moreover, using the same notations: $D_{F}(p,q)=F(p)+F^{*}(q^{*})-\langle p,q^{*}\rangle$
- **Integral form:** by the integral remainder form of Taylor's Theorem, a Bregman divergence can be written as the integral of the Hessian of F along the line segment between the Bregman divergence's arguments.
- **Mean as minimizer**: A key result about Bregman divergences is that, given a random vector, the mean vector minimizes the expected Bregman divergence from the random vector. This result generalizes the textbook result that the mean of a set minimizes total squared error to elements in the set. This result was proved for the vector case by (Banerjee et al. 2005), and extended to the case of functions/distributions by (Frigyik et al. 2008). This result is important because it further justifies using a mean as a representative of a random set, particularly in Bayesian estimation.
- **Bregman balls are bounded, and compact if X is closed**: Define the Bregman ball centered at x with radius r by $B_{f}(x,r):=\left\{y\in X:D_{f}(y,x)\leq r\right\}$ . When $X\subset \mathbb {R} ^{n}$ is finite dimensional, $\forall x\in X$ , if x is in the relative interior of X , or if X is locally closed at x (that is, there exists a closed ball $B(x,r)$ centered at x , such that $B(x,r)\cap X$ is closed), then $B_{f}(x,r)$ is bounded for all r . If X is closed, then $B_{f}(x,r)$ is compact for all r .
- **Law of cosines**:For any $p,q,z$ $D_{F}(p,q)=D_{F}(p,z)+D_{F}(z,q)-(p-z)^{T}(\nabla F(q)-\nabla F(z))$
- Parallelogram law: for any $\theta ,\theta _{1},\theta _{2}$ , $B_{F}\left(\theta _{1}:\theta \right)+B_{F}\left(\theta _{2}:\theta \right)=B_{F}\left(\theta _{1}:{\frac {\theta _{1}+\theta _{2}}{2}}\right)+B_{F}\left(\theta _{2}:{\frac {\theta _{1}+\theta _{2}}{2}}\right)+2B_{F}\left({\frac {\theta _{1}+\theta _{2}}{2}}:\theta \right)$
- **Bregman projection**: For any $W\subset \Omega$ , define the "Bregman projection" of q onto W : $P_{W}(q)=\mathop {\operatorname {argmin} } _{\omega \in W}D_{F}(\omega ,q).$ Then
  - if W is convex, then the projection is unique if it exists;
  - if W is nonempty, closed, and convex and $\Omega \subset \mathbb {R} ^{n}$ is finite dimensional, then the projection exists and is unique.
- **Generalized Pythagorean Theorem**:For any $v\in \Omega ,a\in W$ , $D_{F}(a,v)\geq D_{F}(a,P_{W}(v))+D_{F}(P_{W}(v),v).$ This is an equality if $P_{W}(v)$ is in the relative interior of W .In particular, this always happens when W is an affine set.
- *Lack* of triangle inequality: Since the Bregman divergence is essentially a generalization of squared Euclidean distance, there is no triangle inequality. Indeed, $D_{F}(z,x)-D_{F}(z,y)-D_{F}(y,x)=\langle \nabla f(y)-\nabla f(x),z-y\rangle$ , which may be positive or negative.

### Proofs

- Non-negativity and positivity: use Jensen's inequality.
- Uniqueness up to affine difference: Fix some $x\in \Omega$ , then for any other $y\in \Omega$ , we have by definition $F(y)-G(y)=F(x)-G(x)+\langle \nabla F(x)-\nabla G(x),y-x\rangle$ .
- Convexity in the first argument: by definition, and use convexity of F. Same for strict convexity.
- Linearity in *F*, law of cosines, parallelogram law: by definition.
- Duality: See figure 1 of.
- Bregman balls are bounded, and compact if X is closed: Fix $x\in X$ . Take affine transform on f , so that $\nabla f(x)=0$ . Take some $\epsilon >0$ , such that $\partial B(x,\epsilon )\subset X$ . Then consider the "radial-directional" derivative of f on the Euclidean sphere $\partial B(x,\epsilon )$ . $\langle \nabla f(y),(y-x)\rangle$ for all $y\in \partial B(x,\epsilon )$ . Since $\partial B(x,\epsilon )\subset \mathbb {R} ^{n}$ is compact, it achieves minimal value $\delta$ at some $y_{0}\in \partial B(x,\epsilon )$ . Since f is strictly convex, $\delta >0$ . Then $B_{f}(x,r)\subset B(x,r/\delta )\cap X$ . Since $D_{f}(y,x)$ is $C^{1}$ in y , $D_{f}$ is continuous in y , thus $B_{f}(x,r)$ is closed if X is.
- Projection $P_{W}$ is well-defined when W is closed and convex. Fix $v\in X$ . Take some $w\in W$ , then let $r:=D_{f}(w,v)$ . Then draw the Bregman ball $B_{f}(v,r)\cap W$ . It is closed and bounded, thus compact. Since $D_{f}(\cdot ,v)$ is continuous and strictly convex on it, and bounded below by 0 , it achieves a unique minimum on it.
- Pythagorean inequality. By cosine law, $D_{f}(w,v)-D_{f}(w,P_{W}(v))-D_{f}(P_{W}(v),v)=\langle \nabla _{y}D_{f}(y,v)|_{y=P_{W}(v)},w-P_{W}(v)\rangle$ , which must be $\geq 0$ , since $P_{W}(v)$ minimizes $D_{f}(\cdot ,v)$ in W , and W is convex.
- Pythagorean equality when $P_{W}(v)$ is in the relative interior of X . If $\langle \nabla _{y}D_{f}(y,v)|_{y=P_{W}(v)},w-P_{W}(v)\rangle >0$ , then since w is in the relative interior, we can move from $P_{W}(v)$ in the direction opposite of w , to decrease $D_{f}(y,v)$ , contradiction. Thus $\langle \nabla _{y}D_{f}(y,v)|_{y=P_{W}(v)},w-P_{W}(v)\rangle =0$ .

### Classification theorems

- The only symmetric Bregman divergences on $X\subset \mathbb {R} ^{n}$ are squared generalized Euclidean distances (Mahalanobis distance), that is, $D_{f}(y,x)=(y-x)^{T}A(y-x)$ for some positive definite A .

Proof

For any $x\neq y\in X$ , define $r=\|y-x\|,v=(y-x)/r,g(t)=f(x+tv)$ for $t\in [0,r]$ . Let $z(t)=x+tv$ .

Then $g'(t)=\langle \nabla f(z(t)),v\rangle$ for $t\in (0,r)$ , and since $\nabla f$ is continuous, also for $t=0,r$ .

Then, from the diagram, we see that for $D_{f}(x;z(t))=D_{f}(z(t);x)$ for all $t\in [0,r]$ , we must have $g'(t)$ linear on $t\in [0,r]$ .

Thus we find that $\nabla f$ varies linearly along any direction. By the next lemma, f is quadratic. Since f is also strictly convex, it is of form $f(x)+x^{T}Ax+B^{T}x+C$ , where $A\succ 0$ .

**Lemma**: If S is an open subset of $\mathbb {R} ^{n}$ , $f:S\to \mathbb {R}$ has continuous derivative, and given any line segment $[x,x+v]\subset S$ , the function $h(t):=\langle \nabla f(x+tv),v\rangle$ is linear in t , then f is a quadratic function.

Proof idea: For any quadratic function $q:S\to \mathbb {R}$ , we have $f-q$ still has such derivative-linearity, so we will subtract away a few quadratic functions and show that f becomes zero.

The proof idea can be illustrated fully for the case of $S=\mathbb {R} ^{2}$ , so we prove it in this case.

By the derivative-linearity, f is a quadratic function on any line segment in $\mathbb {R} ^{2}$ . We subtract away four quadratic functions, such that $g:=f-q_{0}-q_{1}-q_{2}-q_{3}$ becomes identically zero on the x-axis, y-axis, and the $\{x=y\}$ line.

Let $q_{0}(x,y)=f(0,0)+\nabla f(0,0)\cdot (x,y),q_{1}(x,y)=A_{1}x^{2},q_{2}(x,y)=A_{2}y^{2},q_{3}(x,y)=A_{3}xy$ , for well-chosen $A_{1},A_{2},A_{3}$ . Now use $q_{0}$ to remove the linear term, and use $q_{1},q_{2},q_{3}$ respectively to remove the quadratic terms along the three lines.

$\forall (x,y)\in \mathbb {R} ^{2}$ not on the origin, there exists a line l across $(x,y)$ that intersects the x-axis, y-axis, and the $\{x=y\}$ line at three different points. Since g is quadratic on l , and is zero on three different points, g is identically zero on l , thus $g(x,y)=0$ . Thus $f=q_{0}+q_{1}+q_{2}+q_{3}$ is quadratic.

The following two characterizations are for divergences on $\Gamma _{n}$ , the set of all probability measures on $\{1,2,...,n\}$ , with $n\geq 2$ .

Define a divergence on $\Gamma _{n}$ as any function of type $D:\Gamma _{n}\times \Gamma _{n}\to [0,\infty ]$ , such that $D(x,x)=0$ for all $x\in \Gamma _{n}$ , then:

- The only divergence on $\Gamma _{n}$ that is both a Bregman divergence and an f-divergence is the Kullback–Leibler divergence.
- If $n\geq 3$ , then any Bregman divergence on $\Gamma _{n}$ that satisfies the data processing inequality must be the Kullback–Leibler divergence. (In fact, a weaker assumption of "sufficiency" is enough.) Counterexamples exist when $n=2$ .

Given a Bregman divergence $D_{F}$ , its "opposite", defined by $D_{F}^{*}(v,w)=D_{F}(w,v)$ , is generally not a Bregman divergence. For example, the Kullback-Leiber divergence is both a Bregman divergence and an f-divergence. Its reverse is also an f-divergence, but by the above characterization, the reverse KL divergence cannot be a Bregman divergence.

## Examples

- The canonical example of a Bregman distance is the squared Euclidean distance $D_{F}(x,y)=\|x-y\|^{2}$ .
- The squared Mahalanobis distance $D_{F}(x,y)={\tfrac {1}{2}}(x-y)^{T}Q(x-y)$ is generated by the convex quadratic form $F(x)={\tfrac {1}{2}}x^{T}Qx$ . The squared Euclidean distance is the special case where Q is the identity, i.e. for $F(x)=\|x\|^{2}$ . As noted, affine differences, i.e. the lower orders added in F , are irrelevant to $D_{F}$ .
- The generalized Kullback–Leibler divergence $D_{F}(p,q)=\sum _{i}p(i)\log {\frac {p(i)}{q(i)}}-\sum _{i}p(i)+\sum _{i}q(i)$ is generated by the negative entropy function $F(p)=\sum _{i}p(i)\log p(i)$ When restricted to the simplex, the last two terms cancel, giving the usual Kullback–Leibler divergence for distributions.
- The Itakura–Saito distance, $D_{F}(p,q)=\sum _{i}\left({\frac {p(i)}{q(i)}}-\log {\frac {p(i)}{q(i)}}-1\right)$ is generated by the convex function $F(p)=-\sum _{i}\log p(i)$

## Generalizing projective duality

A key tool in computational geometry is the idea of projective duality, which maps points to hyperplanes and vice versa, while preserving incidence and above-below relationships. There are numerous analytical forms of the projective dual: one common form maps the point $p=(p_{1},\ldots p_{d})$ to the hyperplane ${\textstyle x_{d+1}=\sum _{i=1}^{d}2p_{i}x_{i}}$ . This mapping can be interpreted (identifying the hyperplane with its normal) as the convex conjugate mapping that takes the point p to its dual point $p^{*}=\nabla F(p)$ , where *F* defines the *d*-dimensional paraboloid ${\textstyle x_{d+1}=\sum _{i}x_{i}^{2}}$ .

If we now replace the paraboloid by an arbitrary convex function, we obtain a different dual mapping that retains the incidence and above-below properties of the standard projective dual. This implies that natural dual concepts in computational geometry like Voronoi diagrams and Delaunay triangulations retain their meaning in distance spaces defined by an arbitrary Bregman divergence. Thus, algorithms from "normal" geometry extend directly to these spaces (Boissonnat, Nielsen and Nock, 2010)

## Generalization of Bregman divergences

Bregman divergences can be interpreted as limit cases of skewed Jensen divergences (see Nielsen and Boltz, 2011). Jensen divergences can be generalized using comparative convexity, and limit cases of these skewed Jensen divergences generalizations yields generalized Bregman divergence (see Nielsen and Nock, 2017). The Bregman chord divergence is obtained by taking a chord instead of a tangent line.

## Bregman divergence on other objects

Bregman divergences can also be defined between matrices, between functions, and between measures (distributions). Bregman divergences between matrices include the Stein's loss and von Neumann entropy. Bregman divergences between functions include total squared error, relative entropy, and squared bias; see the references by Frigyik et al. below for definitions and properties. Similarly Bregman divergences have also been defined over sets, through a submodular set function which is known as the discrete analog of a convex function. The submodular Bregman divergences subsume a number of discrete distance measures, like the Hamming distance, precision and recall, mutual information and some other set based distance measures (see Iyer & Bilmes, 2012 for more details and properties of the submodular Bregman.)

For a list of common matrix Bregman divergences, see Table 15.1 in.

## Applications

In machine learning, Bregman divergences are used to calculate the bi-tempered logistic loss, performing better than the softmax function with noisy datasets.

Bregman divergence is used in the formulation of mirror descent, which includes optimization algorithms used in machine learning such as gradient descent and the hedge algorithm.
