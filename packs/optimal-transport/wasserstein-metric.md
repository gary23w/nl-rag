---
title: "Wasserstein metric"
source: https://en.wikipedia.org/wiki/Wasserstein_metric
domain: optimal-transport
license: CC-BY-SA-4.0
tags: optimal transport, wasserstein metric, earth mover's distance, kantorovich metric
fetched: 2026-07-02
---

# Wasserstein metric

In mathematics, the **Wasserstein distance** or **Kantorovich–Rubinstein metric** is a distance function defined between probability distributions on a given metric space M . It is named after Leonid Vaseršteĭn.

Intuitively, if each distribution is viewed as a unit amount of earth (soil) piled on *M*, the metric is the minimum "cost" of turning one pile into the other, which is assumed to be the amount of earth that needs to be moved times the mean distance it has to be moved. This problem was first formalised by Gaspard Monge in 1781. Because of this analogy, the metric is known in computer science as the earth mover's distance.

## Definition

Let $(M,d)$ be a metric space that is a Polish space. For $p\in [1,+\infty ]$ , the Wasserstein p -distance between two probability measures $\mu$ and $\nu$ on M with finite p -moments is

$W_{p}(\mu ,\nu )=\inf _{\gamma \in \Gamma (\mu ,\nu )}\left(\mathbf {E} _{(x,y)\sim \gamma }d(x,y)^{p}\right)^{\frac {1}{p}},$

where $\Gamma (\mu ,\nu )$ is the set of all couplings of $\mu$ and $\nu$ ; $W_{\infty }(\mu ,\nu )$ is defined to be

$\lim _{p\rightarrow +\infty }W_{p}(\mu ,\nu )$

and corresponds to a supremum norm. Here, a coupling $\gamma$ is a joint probability measure on $M\times M$ whose marginals are $\mu$ and $\nu$ on the first and second factors, respectively. This means that for all measurable $A\subset M$ , it fulfills $\gamma (A\times M)=\mu (A)$ and $\gamma (M\times A)=\nu (A)$ .

The case of $p=\infty$ is special: $W_{\infty }(\mu ,\nu )=\lim _{p\rightarrow +\infty }W_{p}(\mu ,\nu )=\inf _{\gamma \in \Gamma (\mu ,\nu )}\gamma \operatorname {-essup} d(x,y),$ where $\gamma \operatorname {-essup} d(x,y)$ denotes the essential supremum of $d(x,y)$ with respect to measure $\gamma$ . The metric space (***P***∞(*M*), *W*∞) is complete if (*M*, *d*) is separable and complete. Here, ***P***∞ is the space of all probability measures with bounded support.

### Naming

The name "Wasserstein distance" was coined by R. L. Dobrushin in 1970, after learning of it in the work of Leonid Vaseršteĭn on Markov processes describing large systems of automata (Russian, 1969). However the metric was first defined by Leonid Kantorovich in *The Mathematical Method of Production Planning and Organization* (Russian original 1939) in the context of optimal transport planning of goods and materials. Some scholars thus encourage use of the terms "Kantorovich metric" and "Kantorovich distance". Most English-language publications use the German spelling "Wasserstein" (attributed to the name "Vaseršteĭn" (Russian: Васерштейн) being of Yiddish origin).

## Intuition and connection to optimal transport

One way to understand the above definition is to consider the optimal transport problem. That is, for a distribution of mass $\mu (x)$ on a space X , we wish to transport the mass in such a way that it is transformed into the distribution $\nu (x)$ on the same space; transforming the 'pile of earth' $\mu$ to the pile $\nu$ . This problem only makes sense if the pile to be created has the same mass as the pile to be moved; therefore without loss of generality assume that $\mu$ and $\nu$ are probability distributions containing a total mass of 1. Assume also that there is given some cost function

$c(x,y)\geq 0$

that gives the cost of transporting a unit mass from the point x to the point y . A transport plan to move $\mu$ into $\nu$ can be described by a function $\gamma (x,y)$ which gives the amount of mass to move from x to y . You can imagine the task as the need to move a pile of earth of shape $\mu$ to the hole in the ground of shape $\nu$ such that at the end, both the pile of earth and the hole in the ground completely vanish. In order for this plan to be meaningful, it must satisfy the following properties:

1. the amount of earth moved out of point x must equal the amount that was there to begin with; that is, $\int \gamma (x,y)\,\mathrm {d} y=\mu (x),$ and
2. the amount of earth moved into point y must equal the depth of the hole that was there at the beginning; that is, $\int \gamma (x,y)\,\mathrm {d} x=\nu (y).$

That is, that the total mass moved *out of* an infinitesimal region around x must be equal to $\mu (x)\mathrm {d} x$ and the total mass moved *into* a region around y must be $\nu (y)\mathrm {d} y$ . This is equivalent to the requirement that $\gamma$ be a joint probability distribution with marginals $\mu$ and $\nu$ . Thus, the infinitesimal mass transported from x to y is $\gamma (x,y)\,\mathrm {d} x\,\mathrm {d} y$ , and the cost of moving is $c(x,y)\gamma (x,y)\,\mathrm {d} x\,\mathrm {d} y$ , following the definition of the cost function. Therefore, the total cost of a transport plan $\gamma$ is $\iint c(x,y)\gamma (x,y)\,\mathrm {d} x\,\mathrm {d} y=\int c(x,y)\,\mathrm {d} \gamma (x,y).$

The plan $\gamma$ is not unique; the optimal transport plan is the plan with the minimal cost out of all possible transport plans. As mentioned, the requirement for a plan to be valid is that it is a joint distribution with marginals $\mu$ and $\nu$ ; letting $\Gamma$ denote the set of all such measures as in the first section, the cost of the optimal plan is $C=\inf _{\gamma \in \Gamma (\mu ,\nu )}\int c(x,y)\,\mathrm {d} \gamma (x,y).$ If the cost of a move is simply the distance between the two points, then the optimal cost is identical to the definition of the $W_{1}$ distance.

### Fortification

Gaspard Monge, who first considered the problem, considered it as an abstraction of a practical problem. Monge studied descriptive geometry in the context of military fortification. At the time, the outer walls were built with a large amount of earth which would be costly to transport. Furthermore, the ground near the outer walls would also be shaped with structures like ditches to remove favorable attacking positions. The military engineer, during design, should design it according to the terrain, so that for each sector of the fortress, the volume of the *déblai* (the earth excavated) would approximately equal the *remblai* (the material which built up the body of the rampart).

Monge abstracted the problem of minimizing transport cost between the *déblai* and *remblai* into a problem in pure geometry, and published it as *Mémoire sur la Théorie des Déblais et des Remblais*.

## Examples

### Point masses

Point masses naturally arise in statistics. If P and Q are empirical distributions, each based on n observations, then $W_{p}(P,Q)=\inf _{\pi }\left({\frac {1}{n}}\sum _{i=1}^{n}\|X_{i}-Y_{\pi (i)}\|^{p}\right)^{\frac {1}{p}},$ where the infimum is over all permutations $\pi$ of n elements. This is a linear assignment problem, and can be solved by the Hungarian algorithm in cubic time.

### Normal distributions

Let $\mu _{1}={\mathcal {N}}(m_{1},C_{1})$ and $\mu _{2}={\mathcal {N}}(m_{2},C_{2})$ be two non-degenerate Gaussian measures (i.e. normal distributions) on $\mathbb {R} ^{n}$ , with respective expected values $m_{1}$ and $m_{2}\in \mathbb {R} ^{n}$ and symmetric positive semi-definite covariance matrices $C_{1}$ and $C_{2}\in \mathbb {R} ^{n\times n}$ . Then, with respect to the usual Euclidean norm on $\mathbb {R} ^{n}$ , the 2-Wasserstein distance between $\mu _{1}$ and $\mu _{2}$ is $W_{2}(\mu _{1},\mu _{2})^{2}=\|m_{1}-m_{2}\|_{2}^{2}+\mathop {\mathrm {trace} } \left(C_{1}+C_{2}-2\left(C_{2}^{\frac {1}{2}}C_{1}C_{2}^{\frac {1}{2}}\right)^{\frac {1}{2}}\right).$ where $C^{\frac {1}{2}}$ denotes the principal square root of C . Note that the second term (involving the trace) is precisely the (unnormalised) Bures metric between $C_{1}$ and $C_{2}$ . This result generalises the earlier example of the Wasserstein distance between two point masses (at least in the case $p=2$ ), since a point mass can be regarded as a normal distribution with covariance matrix equal to zero, in which case the trace term disappears and only the term involving the Euclidean distance between the means remains.

### One-dimensional distributions

Let $\mu _{1},\mu _{2}\in P_{p}(\mathbb {R} )$ be probability measures on $\mathbb {R}$ , and denote their cumulative distribution functions by $F_{1}(x)$ and $F_{2}(x)$ . Then the transport problem has an analytic solution: Optimal transport preserves the order of probability mass elements, so the mass at quantile q of $\mu _{1}$ moves to quantile q of $\mu _{2}$ . Thus, the p -Wasserstein distance between $\mu _{1}$ and $\mu _{2}$ is $W_{p}(\mu _{1},\mu _{2})=\left(\int _{0}^{1}\left|F_{1}^{-1}(q)-F_{2}^{-1}(q)\right|^{p}\,\mathrm {d} q\right)^{\frac {1}{p}},$ where $F_{1}^{-1}$ and $F_{2}^{-1}$ are the quantile functions (inverse CDFs). In the case of $p=1$ , a change of variables leads to the formula $W_{1}(\mu _{1},\mu _{2})=\int _{\mathbb {R} }\left|F_{1}(x)-F_{2}(x)\right|\,\mathrm {d} x.$

## Properties

### Metric structure

*W**p* satisfies all the axioms of a metric on the Wasserstein space ***P****p*(*M*) consisting of all Borel probability measures on *M* having finite *p*th moment.

Convergence with respect to *W**p* is equivalent to the usual weak convergence of measures plus convergence of the first *p*th moments.

For any *p* ≥ 1, the metric space (***P****p*(*M*), *W**p*) is separable, and is complete if (*M*, *d*) is separable and complete.

### Existence

By a theorem of Gangbo and McCann, if $X,Y$ are subsets of $\mathbb {R} ^{n}$ , and the cost function $c(x,y)=h(x-y)$ for some strictly convex function $h:\mathbb {R} ^{n}\to \mathbb {R}$ , then the optimal transport problem has a unique optimal transport map. In particular, for all $p>1$ , optimal transport map exists and is unique.

### Duality

Kantorovich and Rubinstein proved a duality representation theorem for general cost functions $c(x,y)$ , of which the Wasserstein metric is a special case.

Given a cost function $c(x,y)$ , it produces a duality transformation $\psi \mapsto \psi ^{c}$ defined by $\psi ^{c}(y):=\inf _{x}(c(x,y)-\psi (x))$ This generalizes Legendre transformation, which is the case where $c(x,y)=xy$ with a sign flip.

We say that a function $\psi$ is ***c*-convex** iff $\psi =\varphi ^{c}$ for some $\varphi$ . Like in the case of convex transformation, a function is *c*-convex iff its double dual is itself. In this language, the **Kantorovich duality** states theorem:

> If $(X,\mu _{X}),(Y,\mu _{Y})$ are Polish probability spaces, $c:X\times Y\to \mathbb {R} \cup \{\infty \}$ is lower semicontinuous, and there exists some upper semicontinuous functions $a\in L^{1}(\mu _{X}),b\in L^{1}(\mu _{Y})$ such that $c(x,y)\geq a(x)+b(y)$ , then $\inf _{\gamma \in \Gamma (\mu ,\nu )}\left(\int _{X\times Y}c(x,y)\,\mathrm {d} \gamma (x,y)\right)=\sup _{\varphi {\text{ is }}c{\text{-convex}}}\left(\int _{X}\varphi (x)\,\mathrm {d} \mu (x)+\int _{Y}\varphi ^{c}(y)\,\mathrm {d} \nu (y)\right)$ If furthermore, c only takes real values, there exists a transport plan with finite cost, and there exists some functions $a'\in L^{1}(\mu _{X}),b'\in L^{1}(\mu _{Y})$ such that $c(x,y)\leq a'(x)+b'(y)$ , then $\min _{\gamma \in \Gamma (\mu ,\nu )}\left(\int _{X\times Y}c(x,y)\,\mathrm {d} \gamma (x,y)\right)=\max _{\varphi {\text{ is }}c{\text{-convex}}}\left(\int _{X}\varphi (x)\,\mathrm {d} \mu (x)+\int _{Y}\varphi ^{c}(y)\,\mathrm {d} \nu (y)\right)$

#### Proof

The following is an intuitive proof which skips over technical points. A fully rigorous proof is found in.

**Discrete case**: When M is discrete, solving for the 1-Wasserstein distance is a problem in linear programming: ${\begin{cases}\min _{\gamma }\displaystyle \sum _{x,y}c(x,y)\gamma (x,y)\\[6pt]\displaystyle \sum _{y}\gamma (x,y)=\mu (x)\\[6pt]\displaystyle \sum _{x}\gamma (x,y)=\nu (y)\\[6pt]\gamma \geq 0\end{cases}}$ where $c:M\times M\to [0,\infty )$ is a general "cost function".

By carefully writing the above equations as matrix equations, we obtain its dual problem: ${\begin{cases}\max _{f,g}\displaystyle \sum _{x}\mu (x)f(x)+\sum _{y}\nu (y)g(y)\\[6pt]f(x)+g(y)\leq c(x,y)\end{cases}}$ and by the duality theorem of linear programming, since the primal problem is feasible and bounded, so is the dual problem, and the minimum in the first problem equals the maximum in the second problem. That is, the problem pair exhibits *strong duality*.

For the general case, the dual problem is found by converting sums to integrals: ${\begin{cases}\sup _{f,g}\mathbb {E} _{x\sim \mu }[f(x)]+\mathbb {E} _{y\sim \nu }[g(y)]\\[6pt]f(x)+g(y)\leq c(x,y)\end{cases}}$ and the *strong duality* still holds. This is the **Kantorovich duality theorem**. Cédric Villani recounts the following interpretation from Luis Caffarelli:

> Suppose you want to ship some coal from mines, distributed as $\mu$ , to factories, distributed as $\nu$ . The cost function of transport is c . Now a shipper comes and offers to do the transport for you. You would pay him $f(x)$ per coal for loading the coal at x , and pay him $g(y)$ per coal for unloading the coal at y .
> 
> For you to accept the deal, the price schedule must satisfy $f(x)+g(y)\leq c(x,y)$ . The Kantorovich duality states that the shipper can make a price schedule that makes you pay almost as much as you would ship yourself.

This result can be pressed further to yield:

**Theorem** (Kantorovich-Rubenstein duality)—When the probability space $\Omega$ is a metric space, then $W_{1}(\mu ,\nu )=\sup _{\|f\|_{L}\leq 1}\mathbb {E} _{x\sim \mu }[f(x)]-\mathbb {E} _{y\sim \nu }[f(y)]$ where $\|\cdot \|_{L}$ is the Lipschitz norm.

Proof

Start with $W_{1}(\mu ,\nu )=\sup _{f(x)+g(y)\leq d(x,y)}\mathbb {E} _{x\sim \mu }[f(x)]+\mathbb {E} _{y\sim \nu }[g(y)].$ Then, for any choice of g , one can push the term higher by setting $f(x)=\inf _{y}d(x,y)-g(y)$ , making it an infimal convolution of $-g$ with a cone. This implies $f(x)-f(y)\leq d(x,y)$ for any $x,y$ , that is, $\|f\|_{L}\leq 1$ .

Thus, ${\begin{aligned}W_{1}(\mu ,\nu )&=\sup _{g}\sup _{f(x)+g(y)\leq d(x,y)}\mathbb {E} _{x\sim \mu }[f(x)]+\mathbb {E} _{y\sim \nu }[g(y)]\\[6pt]&=\sup _{g}\sup _{\|f\|_{L}\leq 1,f(x)+g(y)\leq d(x,y)}\mathbb {E} _{x\sim \mu }[f(x)]+\mathbb {E} _{y\sim \nu }[g(y)]\\[6pt]&=\sup _{\|f\|_{L}\leq 1}\sup _{g,f(x)+g(y)\leq d(x,y)}\mathbb {E} _{x\sim \mu }[f(x)]+\mathbb {E} _{y\sim \nu }[g(y)].\end{aligned}}$ Next, for any choice of $\|f\|_{L}\leq 1$ , g can be optimized by setting $g(y)=\inf _{x}d(x,y)-f(x)$ . Since $\|f\|_{L}\leq 1$ , this implies $g(y)=-f(y)$ .

The two infimal convolution steps are visually clear when the probability space is $\mathbb {R}$ .

For notational convenience, let $\square$ denote the infimal convolution operation.

For the first step, where we used $f={\text{cone}}\mathbin {\square } (-g)$ , plot out the curve of $-g$ , then at each point, draw a cone of slope 1, and take the lower envelope of the cones as f , as shown in the diagram, then f cannot increase with slope larger than 1. Thus all its secants have slope ${\bigg |}{\frac {f(x)-f(y)}{x-y}}{\bigg |}\leq 1$ .

For the second step, picture the infimal convolution ${\text{cone}}\mathbin {\square } (-f)$ , then if all secants of f have slope at most 1, then the lower envelope of ${\text{cone}}\mathbin {\square } (-f)$ are just the cone-apices themselves, thus ${\text{cone}}\mathbin {\square } (-f)=-f$ .

**1D Example**. When both $\mu ,\nu$ are distributions on $\mathbb {R}$ , then integration by parts give $\mathbb {E} _{x\sim \mu }[f(x)]-\mathbb {E} _{y\sim \nu }[f(y)]=\int f'(x)(F_{\nu }(x)-F_{\mu }(x))\,\mathrm {d} x,$ thus $f(x)=K\cdot \operatorname {sign} (F_{\nu }(x)-F_{\mu }(x)).$

## *W*1

In the case of *W*1, we have $c(x,y)=d(x,y)$ , and there is a particularly simple way to state that a function is c-convex in this case: a function f is *c*-convex iff it is Lipschitz, with Lipschitz constant $\leq 1$ . In this case, $f^{c}=-f$ , so the Kantorovich duality states that $W_{1}(\mu ,\nu )=\sup \left\{\left.\int _{M}f(x)\,\mathrm {d} (\mu -\nu )(x)\,\right|{\text{ continuous }}f:M\to \mathbb {R} ,\operatorname {Lip} (f)\leq 1\right\},$ This form shows that *W*1 is an integral probability metric. If there exists a f that reaches the supremum exactly, then such a function is called a **Kantorovich potential** for this optimal transport problem.

For example, for any $k>2$ , the optimal transport plan of moving an upside-down unit hemisphere centered at $(0,0,k)$ to a rightside-up unit hemisphere centered at $(0,0,0)$ is simply moving it along the *z*-direction. This is proven by using the Kantorovich potential $f(x,y,z)=z$ .

### Connection to Radon measure

Compare this with the definition of the Radon metric: $\rho (\mu ,\nu ):=\sup \left\{\left.\int _{M}f(x)\,\mathrm {d} (\mu -\nu )(x)\,\right|{\text{ continuous }}f:M\to [-1,1]\right\}.$ If the metric *d* of the metric space (*M*,*d*) is bounded by some constant *C*, then $2W_{1}(\mu ,\nu )\leq C\rho (\mu ,\nu ),$ and so convergence in the Radon metric (identical to **total variation convergence** when *M* is a Polish space) implies convergence in the Wasserstein metric, but not vice versa.

### Geometric interpretation

Monge's original insight was that, in the case where X is a Riemannian manifold with the geodesic distance metric, the duality of optimal transport is geometrically meaningful.

Let $\gamma$ be an optimal transport plan from $\mu$ to $\nu$ . To avoid complications and make the imagery clear, suppose that $\gamma$ is a *deterministic* plan. That is, it is equivalent to a transport *map* $T:\operatorname {supp} (\mu )\to \operatorname {supp} (\nu )$ , so that any infinitesimal lump of coal at x is transported to $T(x)$ . The entire transport map can then be drawn as a family of geodesic curve segments in X connecting each x to its corresponding $T(x)$ . These are **transport rays**.

Monge noted that the transport rays do not intersect at an angle, because otherwise the plan is not optimal. Concretely, suppose that there exist $x,x'$ such that $x\to T(x)$ and $x'\to T(x')$ intersect at an X-shape at some point y , then we can redirect x to $T(x')$ and vice versa, and "pull apart" the X-shape into a )(-shape, and thus cost less in transport. Therefore, the transport rays make up a non-intersecting family of geodesic arcs.

#### Planar case

Monge studied first the case where $X=\mathbb {R} ^{2}$ , in which case transport rays are line segments. He studied in particular the case where the transport rays cover a solid region of the plane. That is, we have a 1-parameter family of lines, a **line congruence**. He showed that these are orthogonal to a 1-parameter family of curves. That is, there exists some partially defined $f:\mathbb {R} ^{2}\to \mathbb {R}$ , such that each contour curve $f^{-1}(k)$ is orthogonal to the transport rays, and furthermore, the curves are separated by their distance. That is, starting on some point z on the curve $f^{-1}(k)$ , and move along the transport ray that the point z is on for a distance $\delta k$ , we would arrive at a point on the curve $f^{-1}(k+\delta k)$ . This is the Kantorovich potential.

Any point in the thin slice can be moved to any other point in the other thin slice without changing the cost. All such plans are optimal. Furthermore, any other plan is suboptimal. In this way, the Kantorovich potential field entirely solves the problem.

Each line in the line congruence divides the plane into two halves, such that the mass of $\mu ,\nu$ in the two halves are the same. The line congruence produces a caustic curve, and the involutes of the caustic curve are the contours of the Kantorovich potential field.

#### Spatial case

Next, Monge noted that when $X=\mathbb {R} ^{3}$ , transport rays are line segments. He studied in particular the case where the transport rays cover a solid region of space. That is, we have a 2-parameter line congruence. He showed that these are orthogonal to a 1-parameter family of surfaces. That is, there exists some partially defined $f:\mathbb {R} ^{3}\to \mathbb {R}$ , such that each contour surface $f^{-1}(k)$ is orthogonal to the transport rays, and furthermore, the surfaces are separated by their distance. That is, starting on some point z on the surface $f^{-1}(k)$ , and move along the transport ray that the point z is on for a distance $\delta k$ , we would arrive at a point on the surface $f^{-1}(k+\delta k)$ . This is the Kantorovich potential.

Any infinitesimal circle in the transport rays sweeps out a thin tube in space, and it encloses one thin filament in $\mu$ and another in $\nu$ . Any point in one thin filament can slide along the tube to any other point in the other thin filament without changing the cost. All such plans are optimal. Furthermore, any other plan is suboptimal. In this way, the Kantorovich potential field entirely solves the problem.

Unlike the planar case, a non-intersecting family of line congruences cannot in general be normal to any surface. For example, consider the standard contact structure on $\mathbb {R} ^{3}$ , which can be understood as a field of infinitesimal planes. Now, perpendicular to every infinitesimal plane, draw a directed ray. This gives us a "twisted" line congruence. There is no surface perpendicular to the congruence, because there is no surface that can be tangent to every infinitesimal plane.

However, Monge showed that in this particular case, this 2-parameter line congruence can be split into a 1-parameter family of 1-parameter line congruences, in such a way that each such 1-parameter line congruence is a developable surface. In fact, there are two ways to split. Thus, the 2-parameter line congruence is generated as the grid of intersections between two 1-parameter families of developable surfaces. He showed that a line congruence satisfying such a condition *is* normal to a 1-parameter family of surfaces, and thus he constructed the surfaces. In modern language, he showed that this is an *integrable* foliation of space by lines.

Each contour surface $f^{-1}(k)$ intersects these two families of developable surfaces at two families of curves, and Monge named them "lines of curvature". He would later study those of the ellipsoid in 1795. Let the surfaces be contours of the equation $f(x,y,z)=const$ . The lines of curvature can be computed from the equation, and 4 lines of curvature produce an infinitesimal square tube. The volumes of $\mu$ and $\nu$ cut by the square tube are equal. This is the partial differential equation satisfied by the surface.

#### General case

In general, at each point z on a transport ray $x\to T(x)$ , define the unit velocity vector $v_{z}$ . This produces a vector field. The vector field cannot have curl in it, since if there is a curl, then effectively, some lump of coal is being transported in a cycle, which is suboptimal. Therefore, the vector field is irrotational, thus locally integrable as the gradient field $\nabla f$ of some function $X\to \mathbb {R}$ . This corresponds to the general fact that an optimal transport plan is *c*-cyclically monotonic. In this way, an optimal transport map produces the Kantorovich potential.

Note that in general, the Kantorovich potential is not everywhere differentiable, and there may be singular points on its surface. For example, consider the transport from the unit circle in $\mathbb {R} ^{2}$ to the origin. Its optimal transport rays are radii of the circle, and its Kantorovich potential has a sharp point at origin. However, it is still differentiable generically, i.e. almost everywhere (like in Sard's theorem).

Conversely, given a continuous $f:X\to \mathbb {R}$ such that almost everywhere it is differentiable with gradient $\nabla f$ of unit length, it is a Kantorovich potential, and its gradient flow generates an optimal transport map.

This duality between the transport *rays* and the potential *field* can be regarded as a Huygens–Fresnel principle.

### Economic interpretation

Economically, this can be interpreted as follows. Consider a market of coals. The price of coal vary over space, so define the price function $f:X\to \mathbb {R}$ , where $f(x)$ is the price of coal at location x .

The market may have opportunity for spatial arbitrage, means that $\exists x,x'\in X$ such that $f(x)-f(x')>d(x,x')$ . An enterprising merchant can then buy coal at $x'$ and sell coal at x , earning a net profit of $f(x)-f(x')-d(x,x')$ .

The price function is *c*-convex iff it is free of spatial arbitrage. For example, a market of constant pricing $f=c_{0}$ has no spatial arbitrage, since the coal is the same price everywhere, so any movement of coal would waste transportation without earning any profit.

Given such a market, a configuration of coal $\mu$ has a total market-value of $\int _{X}fd\mu$ , and two configurations $\mu ,\nu$ may have differing market-values $\int _{X}fd(\mu -\nu )$ . The two parts of duality then state:

- $W_{1}(\mu ,\nu )\geq \int _{X}fd(\mu -\nu )$ for any arbitrage-free market pricing, because otherwise, one can purchase $\nu$ , transport to $\mu$ using an optimal transport plan at a cost of $W_{1}(\mu ,\nu )$ , then sell it, creating profit, so f is not arbitrage-free after all.
- In the case of exact equality $W_{1}(\mu ,\nu )=\int _{X}fd(\mu -\nu )$ , the price f can be interpreted as the shadow price of any optimal transport plan, and any transport plan that exactly breaks even is an optimal plan.

The shadow price interpretation is Kantorovich's original understanding of the duality between optimal planning and market pricing.

## *W*2

### Monge–Ampère equation

Suppose $\mu ,\nu$ are distributions on $\mathbb {R} ^{n}$ with probability density functions $\rho _{\mu },\rho _{\nu }$ . In this case, a map $T:\operatorname {supp} (\mu )\to \operatorname {supp} (\nu )$ is a transport map iff it satisfies $\int h(T(x))\rho _{\mu }(x)dx=\int h(y)\rho _{\nu }(y)dy$ for any integrable test function $h\in L^{1}(\operatorname {supp} (\nu ))$ .

By a theorem of Brenier, the optimal transport map is the (almost everywhere) unique gradient of a convex function $u:\operatorname {supp} (\mu )\to \mathbb {R} ^{n}$ , with $T=\nabla \psi$ . The convex function satisfies a Monge–Ampère equation: ${\begin{cases}\det(\nabla ^{2}\psi )={\frac {\rho _{\mu }}{\rho _{\nu }\circ \nabla \psi }}\\\nabla \psi (\partial \operatorname {supp} (\mu ))=\partial \operatorname {supp} (\nu )\end{cases}}$ The boundary condition simply states that the optimal transport maps the boundary of the source to the boundary of the target.

Conversely, some Monge–Ampère equations can be interpreted optimal transport. Weak-solutions of a Monge–Ampère equations obtained by optimal transport are often called **Brenier solutions** in the literature. Brenier solutions satisfy their corresponding Monge–Ampère equations almost everywhere.

This connection to the Monge–Ampère equation allows one to apply regularity theory to optimal transport with quadratic cost.

#### Applications to geometry

At this point, a very short proof of the **isoperimetric inequality** appears. The inequality states that among all open sets of $\mathbb {R} ^{n}$ with smooth boundaries, the sphere has the smallest surface area (after scaling). That is, $|\partial X|\geq n|B_{1}|^{1/n}|X|^{1-1/n}$ for any open subset $X\subset \mathbb {R} ^{n}$ with smooth boundary.

Consider the quadratic cost transport problem from the uniform distribution on X to the uniform distribution on $B_{1}$ . By the regularity theory of optimal transport, there exists some convex u , smooth on all of X , such that $T:X\to B_{1}$ defined by $T=\nabla u$ is a transport map. (Note that we don't need the optimality of T , just its existence.)

Then we have the following properties: ${\begin{cases}|T|\leq 1\\\det(DT)={\frac {|B_{1}|}{X}}\\\operatorname {div} (T)\geq n\det(DT)^{1/n}\end{cases}}$ The first two properties are because T is a transport map. The third property is by first noting that the convexity of u implies all eigenvalues of $DT$ are nonnegative, then applying the AM–GM inequality. This then gives ${\begin{aligned}|\partial X|&=\int _{\partial X}dS\geq \int _{\partial X}|T|dS\\&\geq \int _{\partial X}(T\cdot {\hat {n}})dS=\int _{X}\operatorname {div} (T)dV\\&\geq \int _{X}n\det(DT)^{1/n}dV=n|B_{1}|^{1/n}|X|^{1-1/n}\end{aligned}}$ Here we use the notation commonly used in vector calculus in 3 dimensions, though it works in any dimension.

### Minimizing flow

Angenent, Haker, and Tannenbaum proposed a way to obtain the optimal transport map by minimizing flow.

### Fluid mechanics interpretation

Benamou & Brenier found a dual representation of $W_{2}$ by fluid mechanics, which allows efficient solution by convex optimization.

Given two probability densities $p,q$ on $\mathbb {R} ^{n}$ , $W_{2}^{2}(p,q)=\min _{\mathbf {v}}\int _{0}^{1}\int _{\mathbb {R} ^{n}}\|{\mathbf {v}}({\mathbf {x}},t)\|^{2}\rho ({\mathbf {x}},t)\,d{\mathbf {x}}\,dt$ where ${\mathbf {v}}$ ranges over velocity fields driving the continuity equation with boundary conditions on the fluid density field: ${\dot {\rho }}+\nabla \cdot (\rho {\mathbf {v}})=0\quad \rho (\cdot ,0)=p,\;\rho (\cdot ,1)=q$ That is, the mass should be conserved, and the velocity field should transport the probability distribution p to q during the time interval $[0,1]$ .

### Negative-order Sobolev norm

Under suitable assumptions, $W_{2}$ is Lipschitz-equivalent to a negative-order homogeneous Sobolev norm. More precisely, if we take M to be a connected Riemannian manifold equipped with a positive measure $\pi$ , then we may define for $f\colon M\to \mathbb {R}$ the seminorm $\|f\|_{{\dot {H}}^{1}(\pi )}^{2}=\int _{M}\|\nabla f(x)\|^{2}\,\pi (\mathrm {d} x)$ and for a signed measure $\mu$ on M the dual norm $\|\mu \|_{{\dot {H}}^{-1}(\pi )}=\sup {\bigg \{}|\langle f,\mu \rangle |\,{\bigg |}\,\|f\|_{{\dot {H}}^{1}(\pi )}\leq 1{\bigg \}}.$ Then any two probability measures $\mu$ and $\nu$ on M satisfy the upper bound $W_{2}(\mu ,\nu )\leq 2\,\|\mu -\nu \|_{{\dot {H}}^{-1}(\pi )}.$ In the other direction, if $\mu$ and $\nu$ each have densities with respect to the standard volume measure on M that are both bounded above by some $0<C<\infty$ , and M has non-negative Ricci curvature, then $\|\mu -\nu \|_{{\dot {H}}^{-1}(\pi )}\leq {\sqrt {C}}\,W_{2}(\mu ,\nu ).$

### Gradient flow

## Applications

The Wasserstein metric is a natural way to compare the probability distributions of two variables *X* and *Y*, where one variable is derived from the other by small, non-uniform perturbations (random or deterministic).

In computer science, for example, the metric *W*1 is widely used to compare discrete distributions, *e.g.* the color histograms of two digital images; see earth mover's distance for more details.

In their paper 'Wasserstein GAN', Arjovsky et al. use the Wasserstein-1 metric as a way to improve the original framework of generative adversarial networks (GAN), to alleviate the vanishing gradient and the mode collapse issues. The special case of normal distributions is used in a Frechet inception distance.

The Wasserstein metric has a formal link with Procrustes analysis, with application to chirality measures, and to shape analysis.

In applied and computational topology, the Wasserstein metric can be used to compare persistence diagrams, for example cytometry datasets in computational biology.

The Wasserstein metric also has been used in inverse problems in geophysics.

The Wasserstein metric is used in integrated information theory to compute the difference between concepts and conceptual structures.

The Wasserstein metric and related formulations have also been used to provide a unified theory for shape observable analysis in high energy and collider physics datasets.
