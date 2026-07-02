---
title: "Earth mover's distance"
source: https://en.wikipedia.org/wiki/Earth_mover%27s_distance
domain: optimal-transport
license: CC-BY-SA-4.0
tags: optimal transport, wasserstein metric, earth mover's distance, kantorovich metric
fetched: 2026-07-02
---

# Earth mover's distance

In computer science, the **earth mover's distance** (**EMD**) is a measure of dissimilarity between two frequency distributions, densities, or measures, over a metric space *D*. Informally, if the distributions are interpreted as two different ways of piling up earth (dirt) over *D*, the EMD captures the minimum cost of building the smaller pile using dirt taken from the larger, where cost is defined as the amount of dirt moved multiplied by the distance over which it is moved.

Over probability distributions, the earth mover's distance is also known as the Wasserstein metric $W_{1}$ , Kantorovich–Rubinstein metric, or Mallows's distance. It is the solution of the optimal transport problem, which in turn is also known as the Monge-Kantorovich problem, or sometimes the Hitchcock–Koopmans transportation problem; when the measures are uniform over a set of discrete elements, the same optimization problem is known as minimum weight bipartite matching.

## Formal definitions

The EMD between probability distributions ${\textstyle P}$ and ${\textstyle Q}$ can be defined as an infimum over joint probabilities:

${\text{EMD}}(P,Q)=\inf \limits _{\gamma \in \Pi (P,Q)}\mathbb {E} _{(x,y)\sim \gamma }\left[d(x,y)\right]\,$

where $\Pi (P,Q)$ is the set of all joint distributions whose marginals are P and Q .

By Kantorovich-Rubinstein duality, this can also be expressed as:

${\text{EMD}}(P,Q)=\sup \limits _{\|f\|_{L}\leq 1}\,\mathbb {E} _{x\sim P}[f(x)]-\mathbb {E} _{y\sim Q}[f(y)]\,$

where the supremum is taken over all 1-Lipschitz continuous functions, i.e. $\|\nabla f(x)\|\leq 1\quad \forall x$ .

### EMD between signatures

In some applications, it is convenient to represent a distribution ${\textstyle P}$ as a *signature*, or a collection of *clusters*, where the ${\textstyle i}$ -th cluster represents a feature of mass ${\textstyle w_{i}}$ centered at ${\textstyle p_{i}}$ . In this formulation, consider signatures ${\textstyle P=\{(p_{1},w_{p1}),(p_{2},w_{p2}),...,(p_{m},w_{pm})\}}$ and ${\textstyle Q=\{(q_{1},w_{q1}),(q_{2},w_{q2}),...,(q_{n},w_{qn})\}}$ . Let ${\textstyle D=[d_{i,j}]}$ be the ground distance between clusters ${\textstyle p_{i}}$ and ${\textstyle q_{j}}$ . Then the EMD between ${\textstyle P}$ and ${\textstyle Q}$ is given by the optimal flow ${\textstyle F=[f_{i,j}]}$ , with ${\textstyle f_{i,j}}$ the flow between ${\textstyle p_{i}}$ and ${\textstyle q_{j}}$ , that minimizes the overall cost.

$\min \limits _{F}{\sum _{i=1}^{m}\sum _{j=1}^{n}f_{i,j}d_{i,j}}$

subject to the constraints:

$f_{i,j}\geq 0,1\leq i\leq m,1\leq j\leq n$

$\sum _{j=1}^{n}{f_{i,j}}\leq w_{pi},1\leq i\leq m$

$\sum _{i=1}^{m}{f_{i,j}}\leq w_{qj},1\leq j\leq n$

$\sum _{i=1}^{m}\sum _{j=1}^{n}f_{i,j}=\min \left\{\ \sum _{i=1}^{m}w_{pi},\quad \sum _{j=1}^{n}w_{qj}\ \right\}$

The optimal flow ${\textstyle F}$ is found by solving this linear optimization problem. The earth mover's distance is defined as the work normalized by the total flow:

${\text{EMD}}(P,Q)={\frac {\sum _{i=1}^{m}\sum _{j=1}^{n}f_{i,j}d_{i,j}}{\sum _{i=1}^{m}\sum _{j=1}^{n}f_{i,j}}}$

## Variants and extensions

### Unequal probability mass

Some applications may require the comparison of distributions with different total masses. One approach is to allow for *partial matching*, where dirt from the more massive distribution is rearranged to make the less massive, and any leftover "dirt" is discarded at no cost. Formally, let ${\textstyle w_{P}}$ be the total weight of ${\textstyle P}$ , and ${\textstyle w_{Q}}$ be the total weight of ${\textstyle Q}$ . We have:

${\text{EMD}}(P,Q)={\tfrac {1}{\min(w_{P},w_{Q})}}\inf \limits _{\gamma \in \Pi _{\geq }(P,Q)}\int d(x,y)\,\mathrm {d} \gamma (x,y)$

where $\Pi _{\geq }(P,Q)$ is the set of all measures whose projections are $\geq P$ and $\geq Q$ . Note that this generalization of EMD is not a true distance between distributions, as it does not satisfy the triangle inequality.

An alternative approach is to allow for mass to be created or destroyed, on a global or local level, as an alternative to transportation, but with a cost penalty. In that case one must specify a real parameter $\alpha$ , the ratio between the cost of creating or destroying one unit of "dirt", and the cost of transporting it by a unit distance. This is equivalent to minimizing the sum of the earth moving cost plus $\alpha$ times the *L*1 distance between the rearranged pile and the second distribution. The resulting measure ${\widehat {EMD}}_{\alpha }$ is a true distance function.

### More than two distributions

The EMD can be extended naturally to the case where more than two distributions are compared. In this case, the "distance" between the many distributions is defined as the optimal value of a linear program. This generalized EMD may be computed exactly using a greedy algorithm, and the resulting functional has been shown to be Minkowski additive and convex monotone.

## Computing the EMD

The EMD can be computed by solving an instance of transportation problem, using any algorithm for minimum-cost flow problem, e.g. the network simplex algorithm.

The Hungarian algorithm can be used to get the solution if the domain *D* is the set {0, 1}. If the domain is integral, it can be translated for the same algorithm by representing integral bins as multiple binary bins.

As a special case, if *D* is a one-dimensional array of "bins" of length *n*, the EMD can be efficiently computed by scanning the array and keeping track of how much dirt needs to be transported between consecutive bins. Here the bins are zero-indexed:

${\begin{aligned}{\text{EMD}}_{0}&=0\\{\text{EMD}}_{i+1}&=P_{i}+{\text{EMD}}_{i}-Q_{i}\\{\text{Total Distance}}&=\sum _{i=0}^{n}|{\text{EMD}}_{i}|\end{aligned}}$

## EMD-based similarity analysis

EMD-based similarity analysis (EMDSA) is an important and effective tool in many multimedia information retrieval and pattern recognition applications. However, the computational cost of EMD is super-cubic to the number of the "bins" given an arbitrary "D". Efficient and scalable EMD computation techniques for large scale data have been investigated using MapReduce, as well as bulk synchronous parallel and resilient distributed dataset.

## Applications

An early application of the EMD in computer science was to compare two grayscale images that may differ due to dithering, blurring, or local deformations. In this case, the region is the image's domain, and the total amount of light (or ink) is the "dirt" to be rearranged.

The EMD is widely used in content-based image retrieval to compute distances between the color histograms of two digital images. In this case, the region is the RGB color cube, and each image pixel is a parcel of "dirt". The same technique can be used for any other quantitative pixel attribute, such as luminance, gradient, apparent motion in a video frame, etc..

More generally, the EMD is used in pattern recognition to compare generic summaries or surrogates of data records called signatures. A typical signature consists of list of pairs ((*x*1,*m*1), ... (*x**n*,*m**n*)), where each *x**i* is a certain "feature" (e.g., color in an image, letter in a text, etc.), and *m**i* is "mass" (how many times that feature occurs in the record). Alternatively, *x**i* may be the centroid of a data cluster, and *m**i* the number of entities in that cluster. To compare two such signatures with the EMD, one must define a distance between features, which is interpreted as the cost of turning a unit mass of one feature into a unit mass of the other. The EMD between two signatures is then the minimum cost of turning one of them into the other.

EMD analysis has been used for quantitating multivariate changes in biomarkers measured by flow cytometry, with potential applications to other technologies that report distributions of measurements.

## History

The concept was first introduced by Gaspard Monge in 1781, in the context of transportation theory. The use of the EMD as a distance measure for monochromatic images was described in 1989 by S. Peleg, M. Werman and H. Rom. The name "earth mover's distance" was proposed by J. Stolfi in 1994, and was used in print in 1998 by Y. Rubner, C. Tomasi and L. G. Guibas.
