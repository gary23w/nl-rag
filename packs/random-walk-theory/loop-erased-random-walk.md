---
title: "Loop-erased random walk"
source: https://en.wikipedia.org/wiki/Loop-erased_random_walk
domain: random-walk-theory
license: CC-BY-SA-4.0
tags: random walk, self-avoiding walk, markov chain, gambler's ruin
fetched: 2026-07-02
---

# Loop-erased random walk

In mathematics, **loop-erased random walk** is a model for a random simple path with important applications in combinatorics, physics and quantum field theory. It is intimately connected to the **uniform spanning tree**, a model for a random tree. It is a case of the more general topic of *random walks*.

## Definition

Assume *G* is some graph and $\gamma$ is some path of length *n* on *G*. In other words, $\gamma (1),\dots ,\gamma (n)$ are vertices of *G* such that $\gamma (i)$ and $\gamma (i+1)$ are connected by an edge. Then the **loop erasure** of $\gamma$ is a new simple path created by erasing all the loops of $\gamma$ in chronological order. Formally, we define indices $i_{j}$ inductively using

$i_{1}=1\,$

$i_{j+1}=\max\{k:\gamma (k)=\gamma (i_{j})\}+1\,$

where "max" here means up to the length of the path $\gamma$ . The induction stops when for some $i_{j}$ we have $\gamma (i_{j})=\gamma (n)$ .

In words, to find $i_{j+1}$ , we hold $\gamma (i_{j})$ in one hand, and with the other hand, we trace back from the end: $\gamma (n),\gamma (n-1),...$ , until we either hit some $\gamma (k)=\gamma (i_{j})$ , in which case we set $i_{j+1}=k+1$ , or we end up at $\gamma (i_{j})$ , in which case we set $i_{j+1}=i_{j}+1$ .

Assume the induction stops at *J* i.e. $\gamma (i_{J})=\gamma (n)$ is the last $i_{J}$ . Then the loop erasure of $\gamma$ , denoted by $\mathrm {LE} (\gamma )$ is a simple path of length *J* defined by

$\mathrm {LE} (\gamma )(j)=\gamma (i_{j}).\,$

Now let *G* be some graph, let *v* be a vertex of *G*, and let *R* be a random walk on *G* starting from *v*. Let *T* be some stopping time for *R*. Then the **loop-erased random walk** until time *T* is LE(*R*([1,*T*])). In other words, take *R* from its beginning until *T* — that's a (random) path — erase all the loops in chronological order as above — you get a random simple path.

The stopping time *T* may be fixed, i.e. one may perform *n* steps and then loop-erase. However, it is usually more natural to take *T* to be the hitting time in some set. For example, let *G* be the graph **Z**2 and let *R* be a random walk starting from the point (0,0). Let *T* be the time when *R* first hits the circle of radius 100 (we mean here of course a *discretized* circle). LE(*R*) is called the loop-erased random walk starting at (0,0) and stopped at the circle.

## Uniform spanning tree

For any graph *G*, a spanning tree of *G* is a subgraph of *G* containing all vertices and some of the edges, which is a tree, i.e. connected and with no cycles. A spanning tree chosen randomly from among all possible spanning trees with equal probability is called a uniform spanning tree. There are typically exponentially many spanning trees (too many to generate them all and then choose one randomly); instead, uniform spanning trees can be generated more efficiently by an algorithm called Wilson's algorithm which uses loop-erased random walks.

The algorithm proceeds according to the following steps. First, construct a single-vertex tree *T* by choosing (arbitrarily) one vertex. Then, while the tree *T* constructed so far does not yet include all of the vertices of the graph, let *v* be an arbitrary vertex that is not in *T*, perform a loop-erased random walk from *v* until reaching a vertex in *T*, and add the resulting path to *T*. Repeating this process until all vertices are included produces a uniformly distributed tree, regardless of the arbitrary choices of vertices at each step.

A connection in the other direction is also true. If *v* and *w* are two vertices in *G* then, in any spanning tree, they are connected by a unique path. Taking this path in the *uniform* spanning tree gives a random simple path. It turns out that the distribution of this path is identical to the distribution of the loop-erased random walk starting at *v* and stopped at *w*. This fact can be used to justify the correctness of Wilson's algorithm. Another corollary is that loop-erased random walk is symmetric in its start and end points. More precisely, the distribution of the loop-erased random walk starting at *v* and stopped at *w* is identical to the distribution of the reversal of loop-erased random walk starting at *w* and stopped at *v*. Loop-erasing a random walk and the reverse walk do not, in general, give the same result, but according to this result the distributions of the two loop-erased walks are identical.

## The Laplacian random walk

Another representation of loop-erased random walk stems from solutions of the discrete Laplace equation. Let *G* again be a graph and let *v* and *w* be two vertices in *G*. Construct a random path from *v* to *w* inductively using the following procedure. Assume we have already defined $\gamma (1),...,\gamma (n)$ . Let *f* be a function from *G* to **R** satisfying

$f(\gamma (i))=0$

for all

$i\leq n$

and

$f(w)=1$

f

is discretely

harmonic

everywhere else

Where a function *f* on a graph is discretely harmonic at a point *x* if *f*(*x*) equals the average of *f* on the neighbors of *x*.

With *f* defined choose $\gamma (n+1)$ using *f* at the neighbors of $\gamma (n)$ as weights. In other words, if $x_{1},...,x_{d}$ are these neighbors, choose $x_{i}$ with probability

${\frac {f(x_{i})}{\sum _{j=1}^{d}f(x_{j})}}.$

Continuing this process, recalculating *f* at each step, will result in a random simple path from *v* to *w*; the distribution of this path is identical to that of a loop-erased random walk from *v* to *w*.

An alternative view is that the distribution of a loop-erased random walk conditioned to start in some path β is identical to the loop-erasure of a random walk conditioned not to hit β. This property is often referred to as the **Markov property** of loop-erased random walk (though the relation to the usual Markov property is somewhat vague).

It is important to notice that while the proof of the equivalence is quite easy, models which involve dynamically changing harmonic functions or measures are typically extremely difficult to analyze. Practically nothing is known about the p-Laplacian walk or diffusion-limited aggregation. Another somewhat related model is the harmonic explorer.

Finally there is another link that should be mentioned: Kirchhoff's theorem relates the number of spanning trees of a graph *G* to the eigenvalues of the discrete Laplacian. See spanning tree for details.

## Grids

Let *d* be the dimension, which we will assume to be at least 2. Examine **Z***d* i.e. all the points $(a_{1},...,a_{d})$ with integer $a_{i}$ . This is an infinite graph with degree 2*d* when you connect each point to its nearest neighbors. From now on we will consider loop-erased random walk on this graph or its subgraphs.

### High dimensions

The easiest case to analyze is dimension 5 and above. In this case it turns out that there the intersections are only local. A calculation shows that if one takes a random walk of length *n*, its loop-erasure has length of the same order of magnitude, i.e. *n*. Scaling accordingly, it turns out that loop-erased random walk converges (in an appropriate sense) to Brownian motion as *n* goes to infinity. Dimension 4 is more complicated, but the general picture is still true. It turns out that the loop-erasure of a random walk of length *n* has approximately $n/\log ^{1/3}n$ vertices, but again, after scaling (that takes into account the logarithmic factor) the loop-erased walk converges to Brownian motion.

### Two dimensions

In two dimensions, arguments from conformal field theory and simulation results led to a number of exciting conjectures. Assume *D* is some simply connected domain in the plane and *x* is a point in *D*. Take the graph *G* to be

$G:=D\cap \varepsilon \mathbb {Z} ^{2},$

that is, a grid of side length ε restricted to *D*. Let *v* be the vertex of *G* closest to *x*. Examine now a loop-erased random walk starting from *v* and stopped when hitting the "boundary" of *G*, i.e. the vertices of *G* which correspond to the boundary of *D*. Then the conjectures are

- As ε goes to zero the distribution of the path converges to some distribution on simple paths from *x* to the boundary of *D* (different from Brownian motion, of course — in 2 dimensions paths of Brownian motion are not simple). This distribution (denote it by $S_{D,x}$ ) is called the **scaling limit** of loop-erased random walk.
- These distributions are conformally invariant. Namely, if φ is a Riemann map between *D* and a second domain *E* then

$\phi (S_{D,x})=S_{E,\phi (x)}.\,$

- The Hausdorff dimension of these paths is 5/4 almost surely.

The first attack at these conjectures came from the direction of **domino tilings**. Taking a spanning tree of *G* and adding to it its planar dual one gets a domino tiling of a special derived graph (call it *H*). Each vertex of *H* corresponds to a vertex, edge or face of *G*, and the edges of *H* show which vertex lies on which edge and which edge on which face. It turns out that taking a uniform spanning tree of *G* leads to a uniformly distributed random domino tiling of *H*. The number of domino tilings of a graph can be calculated using the determinant of special matrices, which allow to connect it to the discrete Green function which is approximately conformally invariant. These arguments allowed to show that certain measurables of loop-erased random walk are (in the limit) conformally invariant, and that the expected number of vertices in a loop-erased random walk stopped at a circle of radius *r* is of the order of $r^{5/4}$ .

In 2002 these conjectures were resolved (positively) using stochastic Löwner evolution. Very roughly, it is a stochastic conformally invariant ordinary differential equation which allows to catch the Markov property of loop-erased random walk (and many other probabilistic processes).

### Three dimensions

The scaling limit exists and is invariant under rotations and dilations. If $L(r)$ denotes the expected number of vertices in the loop-erased random walk until it gets to a distance of *r*, then

$cr^{1+\varepsilon }\leq L(r)\leq Cr^{5/3}\,$

where ε, *c* and *C* are some positive numbers (the numbers can, in principle, be calculated from the proofs, but the author did not do it). This suggests that the scaling limit should have Hausdorff dimension between $1+\varepsilon$ and 5/3 almost surely. Numerical experiments show that it should be $1.62400\pm 0.00005$ .
