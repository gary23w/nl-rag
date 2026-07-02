---
title: "Transportation theory (mathematics)"
source: https://en.wikipedia.org/wiki/Monge_problem
domain: optimal-transport
license: CC-BY-SA-4.0
tags: optimal transport, wasserstein metric, earth mover's distance, kantorovich metric
fetched: 2026-07-02
---

# Transportation theory (mathematics)

(Redirected from

Monge problem

)

In mathematics and economics, **transportation theory** or **transport theory** is a name given to the study of optimal transportation and allocation of resources. The problem was formalized by the French mathematician Gaspard Monge in 1781.

In the 1920s A. N. Tolstoi was one of the first to study the transportation problem mathematically. In 1930, in the collection *Transportation Planning Volume I* for the National Commissariat of Transportation of the Soviet Union, he published a paper "Methods of Finding the Minimal Kilometrage in Cargo-transportation in space".

Major advances were made in the field during World War II by the Soviet mathematician and economist Leonid Kantorovich. Consequently, the problem as it is stated is sometimes known as the **Monge–Kantorovich transportation problem**. The linear programming formulation of the transportation problem is also known as the Hitchcock–Koopmans transportation problem.

## Motivation

### Mines and factories

Suppose that we have a collection of m mines mining iron ore, and a collection of n factories which use the iron ore that the mines produce. Suppose for the sake of argument that these mines and factories form two disjoint subsets M and F of the Euclidean plane $\mathbb {R} ^{2}$ . Suppose also that we have a *cost function* $c:\mathbb {R} ^{2}\times \mathbb {R} ^{2}\to [0,\infty )$ , so that $c(x,y)$ is the cost of transporting one shipment of iron from x to y . For simplicity, we ignore the time taken to do the transporting. We also assume that each mine can supply only one factory (no splitting of shipments) and that each factory requires precisely one shipment to be in operation (factories cannot work at half- or double-capacity). Having made the above assumptions, a *transport plan* is a bijection $T:M\to F$ . In other words, each mine $m\in M$ supplies precisely one target factory $T(m)\in F$ and each factory is supplied by precisely one mine. We wish to find the *optimal transport plan*, the plan T whose *total cost*

$c(T):=\sum _{m\in M}c(m,T(m))$

is the least of all possible transport plans from M to F . This motivating special case of the transportation problem is an instance of the assignment problem. More specifically, it is equivalent to finding a minimum weight matching in a bipartite graph.

This can be generalized to the continuous case, where there are infinitely many mines and factories distributed on the real line, or generally in any metric space. This case is usually pictured as "changing the shape of a pile of dirt", and thus called the earth mover's problem.

### Moving books: the importance of the cost function

The following simple example illustrates the importance of the cost function in determining the optimal transport plan. Suppose that we have n books of equal width on a shelf (the real line), arranged in a single contiguous block. We wish to rearrange them into another contiguous block, but shifted one book-width to the right. Two obvious candidates for the optimal transport plan present themselves:

1. move all n books one book-width to the right ("many small moves");
2. move the left-most book n book-widths to the right and leave all other books fixed ("one big move").

If the cost function is proportional to Euclidean distance ( $c(x,y)=\alpha \|x-y\|$ for some $\alpha >0$ ) then these two candidates are *both* optimal. If, on the other hand, we choose the strictly convex cost function proportional to the square of Euclidean distance ( $c(x,y)=\alpha \|x-y\|^{2}$ for some $\alpha >0$ ), then the "many small moves" option becomes the unique minimizer.

Note that the above cost functions consider only the horizontal distance traveled by the books, not the horizontal distance traveled by a device used to pick each book up and move the book into position. If the latter is considered instead, then, of the two transport plans, the second is always optimal for the Euclidean distance, while, provided there are at least 3 books, the first transport plan is optimal for the squared Euclidean distance.

### Hitchcock problem

The following transportation problem formulation is credited to F. L. Hitchcock:

Suppose there are

m

sources

$x_{1},\ldots ,x_{m}$

for a commodity, with

$a(x_{i})$

units of supply at

$x_{i}$

and

n

sinks

$y_{1},\ldots ,y_{n}$

for the commodity, with the demand

$b(y_{j})$

at

$y_{j}$

. If

$c(x_{i},\ y_{j})$

is the unit cost of shipment from

$x_{i}$

to

$y_{j}$

, find a flow that satisfies demand from supplies and minimizes the flow cost. This challenge in logistics was taken up by

D. R. Fulkerson

and in the book

Flows in Networks

(1962) written with

L. R. Ford Jr.

Tjalling Koopmans is also credited with formulations of transport economics and allocation of resources.

## Abstract formulation of the problem

### Monge and Kantorovich formulations

The transportation problem as it is stated in modern or more technical literature looks somewhat different because of the development of Riemannian geometry and measure theory. The mines-factories example, simple as it is, is a useful reference point when thinking of the abstract case. In this setting, we allow the possibility that we may not wish to keep all mines and factories open for business, and allow mines to supply more than one factory, and factories to accept iron from more than one mine.

Let X and Y be two separable metric spaces such that any probability measure on X (or Y ) is a Radon measure (i.e. they are Radon spaces). Let $c:X\times Y\to [0,\infty )$ be a Borel-measurable function. Given probability measures $\mu$ on X and $\nu$ on Y , Monge's formulation of the optimal transportation problem is to find a transport map $T:X\to Y$ that realizes the infimum

$\inf \left\{\left.\int _{X}c(x,T(x))\,\mathrm {d} \mu (x)\right|T_{*}(\mu )=\nu \right\},$

where $T_{*}(\mu )$ denotes the push forward of $\mu$ by T . A map T that attains this infimum (*i.e.* makes it a minimum instead of an infimum) is called an "optimal transport map".

Monge's formulation of the optimal transportation problem can be ill-posed, because sometimes there is no T satisfying $T_{*}(\mu )=\nu$ : this happens, for example, when $\mu$ is a Dirac measure but $\nu$ is not.

We can improve on this by adopting Kantorovich's formulation of the optimal transportation problem, which is to find a probability measure $\gamma$ on $X\times Y$ that attains the infimum

$\inf \left\{\left.\int _{X\times Y}c(x,y)\,\mathrm {d} \gamma (x,y)\right|\gamma \in \Gamma (\mu ,\nu )\right\},$

where $\Gamma (\mu ,\nu )$ denotes the collection of all probability measures on $X\times Y$ with marginals $\mu$ on X and $\nu$ on Y .

### Cost duality

Given a cost function $c(x,y)$ , it produces a duality transformation $\psi \mapsto \psi ^{c}$ defined by $\psi ^{c}(y):=\inf _{x}(c(x,y)-\psi (x))$ This generalizes Legendre transformation, which is the case where $c(x,y)=-xy$ with a sign flip.

$\leq 1$ .

We say that a function $\psi$ is ***c*-convex** if $\psi =\varphi ^{c}$ for some $\varphi$ . Note that because $\varphi ^{ccc}=\varphi ^{c}$ , we can always assume that $\varphi$ is *c*-convex. The ***c*-convexification** of a function $\psi$ is $\psi ^{cc}$ . Equivalently, it is the smallest *c*-convex function $\psi '$ such that $\psi '\geq \psi$ pointwise. Like in the case of convex transformation, $\psi$ is *c*-convex iff $\psi =\psi ^{cc}$ .

If $\psi =\varphi ^{c}:X\to \mathbb {R}$ is *c*-convex, then the set of ***c*-subdifferential** of $\psi$ at $x\in X$ is the set of $y\in Y$ such that $\psi (x)=c(x,y)-\varphi (y)$ . Similarly for Y .

When $X=Y$ , the graph $(y,\psi ^{c}(y))$ can be constructed as follows: Take the graph of $\psi$ , and flip it upside down. At each point $(x,-\psi (x))$ , construct a graph of $y\mapsto c(x,y)$ apexed at $(x,-\psi (x))$ . That is, it is the graph of $y\mapsto c(x,y)-\psi (x)$ . We obtain a whole set of such graphs. Their lower-edge envelope is the graph of $\psi ^{c}$ .

In the same image, we can see what it means for a function $\varphi (y)$ to be *c*-convex. It is *c*-convex iff its entire graph can be "touched" by a "tipped tool" that is moving and shape-shifting. When the tipped tool is at x , it has a shape of $y\mapsto c(x,y)$ and is raised to a height of $-\psi (x)$ . The graph of the *c*-convexification $\varphi ^{cc}(y)$ is constructed by running the tipped tool so that it is lowered as much as possible, while still touching graph of $\varphi (y)$ on the upper side. The lower envelope swept out by the tipped tool is the graph of $\varphi ^{cc}(y)$ .

For example, if $X=Y=\mathbb {R} ^{n}$ is a metric space and $c(x,y)=\|x-y\|$ , then $\varphi :X\to \mathbb {R}$ is *c*-convex iff it is 1-Lipschitz. This is used in the definition of 1-Wasserstein distance. If $c(x,y)=\|x-y\|^{2}$ , then $\varphi$ is *c*-convex iff its graph could be touched from above by a tipped tool with the shape of a paraboloid.

### Existence and uniqueness

Under fairly permissive assumptions, optimal transport plan exists.

> If
> 
> - $(X,\mu _{X}),(Y,\mu _{Y})$ are Polish probability spaces,
> - $c:X\times Y\to \mathbb {R} \cup \{\infty \}$ is lower semicontinuous,
> - and there exists some upper semicontinuous functions $a\in L^{1}(\mu _{X}),b\in L^{1}(\mu _{Y})$ of type $a:X\to \mathbb {R} \cup \{-\infty \},\;b:Y\to \mathbb {R} \cup \{-\infty \}$ such that $c(x,y)\geq a(x)+b(y)$ ,
> 
> then an optimal transport *plan* exists. That is, exists $\gamma ^{*}\in \Gamma (\mu _{X},\mu _{Y})$ such that it reaches the infimum.

Note that the infimum could be infinite if all transport plans turn out to be infinite. For example, if $X=Y=\mathbb {R} ,c(x,y)=|x-y|,\;\mu _{X}$ is the Cauchy distribution, and $\mu _{Y}=\delta _{0}$ .

> If
> 
> - $(X,\mu _{X}),(Y,\mu _{Y})$ are Polish probability spaces,
> - $c:X\times Y\to \mathbb {R}$ is lower semicontinuous,
> - there exists some upper semicontinuous functions $a\in L^{1}(\mu _{X}),b\in L^{1}(\mu _{Y})$ of type $a:X\to \mathbb {R} ,\;b:Y\to \mathbb {R}$ such that $c(x,y)\geq a(x)+b(y)$ ,
> - there exists a finite-cost transport plan,
> - and for any *c*-convex function $\psi :X\to \mathbb {R} \cup \{\infty \}$ , for $\mu _{X}$ -almost all $x\in X$ , $\psi$ has a unique *c*-subdifferential at x
> 
> then an optimal transport *map* exists.

A restriction of an optimal transport plan is still optimal. That is, suppose $\gamma \in \Gamma (\mu ,\nu )$ is optimal, and $0<\gamma '<\gamma$ , and define the normalized transport plan ${\bar {\gamma }}':=\gamma '/\gamma '(X\times Y)$ , then ${\bar {\gamma }}'$ is an optimal transport plan between its own marginals. If ${\bar {\gamma }}'$ isn't optimal, then there exists an improvement of it, which then translates back to an improvement of the original $\gamma$ .

### Kantorovich duality

The **Kantorovich duality** states that:

> If $(X,\mu _{X}),(Y,\mu _{Y})$ are Polish probability spaces, $c:X\times Y\to \mathbb {R} \cup \{\infty \}$ is lower semicontinuous, and there exists some upper semicontinuous functions $a\in L^{1}(\mu _{X}),b\in L^{1}(\mu _{Y})$ of type $a:X\to \mathbb {R} ,\;b:Y\to \mathbb {R}$ such that $c(x,y)\geq a(x)+b(y)$ , then $\inf _{\gamma \in \Gamma (\mu ,\nu )}\left(\int _{X\times Y}c(x,y)\,\mathrm {d} \gamma (x,y)\right)=\sup _{\varphi {\text{ is }}c{\text{-convex}}}\left(\int _{X}\varphi (x)\,\mathrm {d} \mu (x)+\int _{Y}\varphi ^{c}(y)\,\mathrm {d} \nu (y)\right)$ If furthermore, c only takes real values, there exists a transport plan with finite cost, and there exists some functions $a'\in L^{1}(\mu _{X}),b'\in L^{1}(\mu _{Y})$ such that $c(x,y)\leq a'(x)+b'(y)$ , then $\min _{\gamma \in \Gamma (\mu ,\nu )}\left(\int _{X\times Y}c(x,y)\,\mathrm {d} \gamma (x,y)\right)=\max _{\varphi {\text{ is }}c{\text{-convex}}}\left(\int _{X}\varphi (x)\,\mathrm {d} \mu (x)+\int _{Y}\varphi ^{c}(y)\,\mathrm {d} \nu (y)\right)$

Consider the second case, where we can actually arrive at an exactly optimal plan, instead of merely getting closer and closer. In this case, an optimal transport plan $\gamma \in \Gamma (\mu ,\nu )$ , constrains the form of an optimal pricing pair $(\varphi ,\psi )$ , and vice versa.

Given such an optimal pricing pair $(\varphi ,\psi )$ ,

- given an arbitrary transport plan $\gamma \in \Gamma (\mu ,\nu )$ , if all $(x,y)\in \operatorname {supp} (\gamma )$ satisfies the exact equality $c(x,y)=\varphi (x)+\psi (y)$ , then $\gamma$ is an optimal plan;
- given an optimal transport plan $\gamma \in \Gamma (\mu ,\nu )$ , any $(x,y)\in \operatorname {supp} (\gamma )$ must satisfy the exact equality $c(x,y)=\varphi (x)+\psi (y)$ .

More succinctly, a transport plan is optimal iff it is supported on the set of *c*-subdifferential pairs of $(\varphi ,\psi )$ .

### Stability

The optimal transportation is *stable* in the following sense:

> Assume that $(X,\mu ),(Y,\nu )$ are Polish probability spaces, $c:X\times Y\to \mathbb {R}$ is continuous, and $\inf c$ is finite. Given a sequence of continuous functions $c:X\times Y\to \mathbb {R}$ converging uniformly to c over $X\times Y$ , a sequence $\mu _{k}\to \mu$ weakly, a sequence $\nu _{k}\to \nu$ weakly, and a sequence of optimal transport plans $\gamma _{k}\in \Gamma (\mu _{k},\nu _{k})$ . If the transport costs $\int c_{k}d\pi _{k}$ satisfy $\int c_{k}d\pi _{k}<+\infty ,\;\forall k$ and $\liminf _{k}\int c_{k}d\pi _{k}<+\infty$ , then $\gamma _{k}$ converges weakly to some $\gamma$ , and $\gamma$ is an optimal transport plan from $\mu$ to $\nu$ .

Similarly, the optimal transport map is also stable.

> Assume that $(X,\mu ),(Y,\nu )$ are Polish probability spaces, X is locally compact, $c:X\times Y\to \mathbb {R}$ is lower semicontinuous, and $\inf c$ is finite. Given a sequence of lower semicontinuous functions $c:X\times Y\to \mathbb {R}$ converging uniformly to c over $X\times Y$ , a sequence $\nu _{k}\to \nu$ weakly,

### Economic interpretation

The optimal transport problem has an economic interpretation. Cédric Villani recounts the following interpretation from Luis Caffarelli:

> Suppose you want to ship some coal from mines, distributed as $\mu$ , to factories, distributed as $\nu$ . The cost function of transport is c . Now a shipper comes and offers to do the transport for you. You would pay him $f(x)$ per coal for loading the coal at x , and pay him $g(y)$ per coal for unloading the coal at y . For you to accept the deal, the price schedule must satisfy $f(x)+g(y)\leq c(x,y)$ . The Kantorovich duality states that the shipper can make a price schedule that makes you pay almost as much as you would ship yourself.

In the interpretation, the duality transformation transforms a loading cost function $\varphi (x)$ into the optimal (for the shipper) unloading cost function $\psi (y)=\varphi ^{c}(y)$ . If the unloading cost function $\psi (y)$ were any higher at any point, then there would be some route $x\to y$ on which $c(x,y)<\varphi (x)+\psi (y)$ , meaning that there is some route on which you would rather ship yourself. But if the unloading cost function were any lower at any point, then the shipper could have earned more money by raising the price there. Therefore, the shipper should always choose $\psi =\varphi ^{c}$ . The same argument applied again then states that the shipper should always choose $\varphi =\psi ^{c}$ , and therefore we obtain the lower bound half of the duality formula: $\inf _{\gamma \in \Gamma (\mu ,\nu )}\left(\int _{X\times Y}c(x,y)\,\mathrm {d} \gamma (x,y)\right)\geq \sup _{\varphi {\text{ is }}c{\text{-convex}}}\left(\int _{X}\varphi (x)\,\mathrm {d} \mu (x)+\int _{Y}\varphi ^{c}(y)\,\mathrm {d} \nu (y)\right),$ The Kantorovich duality states that it is in fact an equality, i.e. the shipper can make you pay as much as you would pay yourself, though the shipper might never exactly reach the bound (thus the use of infimum and supremum, instead of minimum and maximum).

Assume that the shipper in fact must pay the same cost function and us, and can exactly reach the maximum revenue using $(\varphi ,\psi )$ as their pricing chart. Then the shipper must use an optimal plan, at which point the shipper just breaks even with no profit. Conversely, any shipping plan that allows the shipper to exactly break even must be optimal.

## Solution of the problem

### Optimal transportation on the real line

Optimal transportation matrix

Continuous optimal transport

For $1\leq p<\infty$ , let ${\mathcal {P}}_{p}(\mathbb {R} )$ denote the collection of probability measures on $\mathbb {R}$ that have finite p -th moment. Let $\mu ,\nu \in {\mathcal {P}}_{p}(\mathbb {R} )$ and let $c(x,y)=h(x-y)$ , where $h:\mathbb {R} \to [0,\infty )$ is a convex function.

1. If $\mu$ has no atom, i.e., if the cumulative distribution function $F_{\mu }:\mathbb {R} \to [0,1]$ of $\mu$ is a continuous function, then $F_{\nu }^{-1}\circ F_{\mu }:\mathbb {R} \to \mathbb {R}$ is an optimal transport map. It is the unique optimal transport map if h is strictly convex.
2. We have

$\min _{\gamma \in \Gamma (\mu ,\nu )}\int _{\mathbb {R} ^{2}}c(x,y)\,\mathrm {d} \gamma (x,y)=\int _{0}^{1}c\left(F_{\mu }^{-1}(s),F_{\nu }^{-1}(s)\right)\,\mathrm {d} s.$

The proof of this solution appears in Rachev & Rüschendorf (1998).

### Discrete version and linear programming formulation

In the case where the margins $\mu$ and $\nu$ are discrete, let $\mu _{x}$ and $\nu _{y}$ be the probability masses respectively assigned to $x\in \mathbf {X}$ and $y\in \mathbf {Y}$ , and let $\gamma _{xy}$ be the probability of an $xy$ assignment. The objective function in the primal Kantorovich problem is then

$\sum _{x\in \mathbf {X} ,y\in \mathbf {Y} }\gamma _{xy}c_{xy}$

and the constraint $\gamma \in \Gamma (\mu ,\nu )$ expresses as

$\sum _{y\in \mathbf {Y} }\gamma _{xy}=\mu _{x},\forall x\in \mathbf {X}$

and

$\sum _{x\in \mathbf {X} }\gamma _{xy}=\nu _{y},\forall y\in \mathbf {Y} .$

In order to input this in a linear programming problem, we need to vectorize the matrix $\gamma _{xy}$ by either stacking its columns or its rows, we call $\operatorname {vec}$ this operation. In the column-major order, the constraints above rewrite as

$\left(1_{1\times |\mathbf {Y} |}\otimes I_{|\mathbf {X} |}\right)\operatorname {vec} (\gamma )=\mu$

and

$\left(I_{|\mathbf {Y} \|}\otimes 1_{1\times |\mathbf {X} |}\right)\operatorname {vec} (\gamma )=\nu$

where $\otimes$ is the Kronecker product, $1_{n\times m}$ is a matrix of size $n\times m$ with all entries of ones, and $I_{n}$ is the identity matrix of size n . As a result, setting $z=\operatorname {vec} (\gamma )$ , the linear programming formulation of the problem is

${\begin{aligned}&{\text{Minimize }}&&\operatorname {vec} (c)^{\top }z\\[4pt]&{\text{subject to:}}&&z\geq 0,\\[4pt]&&&{\begin{pmatrix}1_{1\times |\mathbf {Y} |}\otimes I_{|\mathbf {X} |}\\I_{|\mathbf {Y} |}\otimes 1_{1\times |\mathbf {X} |}\end{pmatrix}}z={\binom {\mu }{\nu }}\end{aligned}}$

which can be readily inputted in a large-scale linear programming solver (see chapter 3.4 of Galichon (2016)).

### Semi-discrete case

In the semi-discrete case, $X=Y=\mathbb {R} ^{d}$ and $\mu$ is a continuous distribution over $\mathbb {R} ^{d}$ , while $\nu =\sum _{j=1}^{J}\nu _{j}\delta _{y_{i}}$ is a discrete distribution which assigns probability mass $\nu _{j}$ to site $y_{j}\in \mathbb {R} ^{d}$ . In this case, we can see that the primal and dual Kantorovich problems respectively boil down to:

$\inf \left\{\int _{X}\sum _{j=1}^{J}c(x,y_{j})\,d\gamma _{j}(x),\gamma \in \Gamma (\mu ,\nu )\right\}$

for the primal, where $\gamma \in \Gamma (\mu ,\nu )$ means that $\int _{X}d\gamma _{j}(x)=\nu _{j}$ and $\sum _{j}d\gamma _{j}(x)=d\mu (x)$ , and:

$\sup \left\{\int _{X}\varphi (x)d\mu (x)+\sum _{j=1}^{J}\psi _{j}\nu _{j}:\psi _{j}+\varphi (x)\leq c(x,y_{j})\right\}$

for the dual, which can be rewritten as:

$\sup _{\psi \in \mathbb {R} ^{J}}\left\{\int _{X}\inf _{j}\left\{c(x,y_{j})-\psi _{j}\right\}d\mu (x)+\sum _{j=1}^{J}\psi _{j}\nu _{j}\right\}$

which is a finite-dimensional convex optimization problem that can be solved by standard techniques, such as gradient descent.

In the case when $c(x,y)=|x-y|^{2}/2$ , one can show that the set of $x\in \mathbf {X}$ assigned to a particular site j is a convex polyhedron. The resulting configuration is called a power diagram.

### Quadratic normal case

Assume the particular case $\mu ={\mathcal {N}}(0,\Sigma _{X})$ , $\nu ={\mathcal {N}}(0,\Sigma _{Y})$ , and $c(x,y)=|y-Ax|^{2}/2$ where A is invertible. One then has

$\varphi (x)=-x^{\top }\Sigma _{X}^{-1/2}\left(\Sigma _{X}^{1/2}A^{\top }\Sigma _{Y}A\Sigma _{X}^{1/2}\right)^{1/2}\Sigma _{X}^{-1/2}x/2$

$\psi (y)=-y^{\top }A\Sigma _{X}^{1/2}\left(\Sigma _{X}^{1/2}A^{\top }\Sigma _{Y}A\Sigma _{X}^{1/2}\right)^{-1/2}\Sigma _{X}^{1/2}Ay/2$

$T(x)=(A^{\top })^{-1}\Sigma _{X}^{-1/2}\left(\Sigma _{X}^{1/2}A^{\top }\Sigma _{Y}A\Sigma _{X}^{1/2}\right)^{1/2}\Sigma _{X}^{-1/2}x$

The proof of this solution appears in Galichon (2016).

### Separable Hilbert spaces

Let X be a separable Hilbert space. Let ${\mathcal {P}}_{p}(X)$ denote the collection of probability measures on X that have finite p -th moment; let ${\mathcal {P}}_{p}^{r}(X)$ denote those elements $\mu \in {\mathcal {P}}_{p}(X)$ that are **Gaussian regular**: if g is any strictly positive Gaussian measure on X and $g(N)=0$ , then $\mu (N)=0$ also.

Let $\mu \in {\mathcal {P}}_{p}^{r}(X)$ , $\nu \in {\mathcal {P}}_{p}(X)$ , $c(x,y)=|x-y|^{p}/p$ for $p\in (1,\infty ),p^{-1}+q^{-1}=1$ . Then the Kantorovich problem has a unique solution $\kappa$ , and this solution is induced by an optimal transport map: i.e., there exists a Borel map $r\in L^{p}(X,\mu ;X)$ such that

$\kappa =(\mathrm {id} _{X}\times r)_{*}(\mu )\in \Gamma (\mu ,\nu ).$

Moreover, if $\nu$ has bounded support, then

$r(x)=x-|\nabla \varphi (x)|^{q-2}\,\nabla \varphi (x)$

for $\mu$ -almost all $x\in X$ for some locally Lipschitz, c -concave and maximal Kantorovich potential $\varphi$ . (Here $\nabla \varphi$ denotes the Gateaux derivative of $\varphi$ .)

### By minimizing flows

A gradient descent formulation for the solution of the Monge–Kantorovich problem was given by Sigurd Angenent, Steven Haker, and Allen Tannenbaum.

## Entropic regularization

Consider a variant of the discrete problem above, where we have added an entropic regularization term to the objective function of the primal problem

${\begin{aligned}&{\text{Minimize }}\sum _{x\in \mathbf {X} ,y\in \mathbf {Y} }\gamma _{xy}c_{xy}+\varepsilon \gamma _{xy}\ln \gamma _{xy}\\[4pt]&{\text{subject to: }}\\[4pt]&\gamma \geq 0\\[4pt]&\sum _{y\in \mathbf {Y} }\gamma _{xy}=\mu _{x},\forall x\in \mathbf {X} \\[4pt]&\sum _{x\in \mathbf {X} }\gamma _{xy}=\nu _{y},\forall y\in \mathbf {Y} \end{aligned}}$

One can show that the dual regularized problem is

$\max _{\varphi ,\psi }\sum _{x\in \mathbf {X} }\varphi _{x}\mu _{x}+\sum _{y\in \mathbf {Y} }\psi _{y}v_{y}-\varepsilon \sum _{x\in \mathbf {X} ,y\in \mathbf {Y} }\exp \left({\frac {\varphi _{x}+\psi _{y}-c_{xy}}{\varepsilon }}\right)$

where, compared with the unregularized version, the "hard" constraint in the former dual ( $\varphi _{x}+\psi _{y}-c_{xy}\geq 0$ ) has been replaced by a "soft" penalization of that constraint (the sum of the $\varepsilon \exp \left((\varphi _{x}+\psi _{y}-c_{xy})/\varepsilon \right)$ terms). The optimality conditions in the dual problem can be expressed as

Eq. 5.1:

$\mu _{x}=\sum _{y\in \mathbf {Y} }\exp \left({\frac {\varphi _{x}+\psi _{y}-c_{xy}}{\varepsilon }}\right)~\forall x\in \mathbf {X}$

Eq. 5.2:

$\nu _{y}=\sum _{x\in \mathbf {X} }\exp \left({\frac {\varphi _{x}+\psi _{y}-c_{xy}}{\varepsilon }}\right)~\forall y\in \mathbf {Y}$

Denoting A as the $|\mathbf {X} |\times |\mathbf {Y} |$ matrix of term $A_{xy}=\exp \left(-c_{xy}/\varepsilon \right)$ , solving the dual is therefore equivalent to looking for two diagonal positive matrices $D_{1}$ and $D_{2}$ of respective sizes $|\mathbf {X} |$ and $|\mathbf {Y} |$ , such that $D_{1}AD_{2}1_{|\mathbf {Y} |}=\mu$ and $(D_{1}AD_{2})^{\top }1_{|\mathbf {X} |}=\nu$ . The existence of such matrices generalizes Sinkhorn's theorem and the matrices can be computed using the Sinkhorn–Knopp algorithm, which simply consists of iteratively looking for $\varphi _{x}$ to solve **Equation 5.1**, and $\psi _{y}$ to solve **Equation 5.2**. Sinkhorn–Knopp's algorithm is therefore a coordinate descent algorithm on the dual regularized problem.

## Applications

The Monge–Kantorovich optimal transport has found applications in wide range in different fields. Among them are:

- Image registration and warping
- Reflector design
- Retrieving information from shadowgraphy and proton radiography
- Seismic tomography and reflection seismology
- The broad class of economic modelling that involves gross substitutes property (among others, models of matching and discrete choice).
