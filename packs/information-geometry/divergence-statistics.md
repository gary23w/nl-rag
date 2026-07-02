---
title: "Divergence (statistics)"
source: https://en.wikipedia.org/wiki/Divergence_(statistics)
domain: information-geometry
license: CC-BY-SA-4.0
tags: information geometry, fisher information metric, statistical manifold, bregman divergence
fetched: 2026-07-02
---

# Divergence (statistics)

In information geometry, a **divergence** is a kind of statistical distance: a binary function which establishes the separation from one probability distribution to another on a statistical manifold.

The simplest divergence is squared Euclidean distance (SED), and divergences can be viewed as generalizations of SED. The other most important divergence is relative entropy (also called Kullback–Leibler divergence), which is central to information theory. There are numerous other specific divergences and classes of divergences, notably *f*-divergences and Bregman divergences (see § Examples).

## Definition

Given a differentiable manifold M of dimension n , a **divergence** on M is a $C^{2}$ -function $D:M\times M\to [0,\infty )$ satisfying:

1. $D(p,q)\geq 0$ for all $p,q\in M$ (non-negativity),
2. $D(p,q)=0$ if and only if $p=q$ (positivity),
3. At every point $p\in M$ , $D(p,p+dp)$ is a positive-definite quadratic form for infinitesimal displacements $dp$ from p .

In applications to statistics, the manifold M is typically the space of parameters of a parametric family of probability distributions.

Condition 3 means that D defines an inner product on the tangent space $T_{p}M$ for every $p\in M$ . Since D is $C^{2}$ on M , this defines a Riemannian metric g on M .

Locally at $p\in M$ , we may construct a local coordinate chart with coordinates x , then the divergence is $D(x(p),x(p)+dx)=\textstyle {\frac {1}{2}}dx^{T}g_{p}(x)dx+O(|dx|^{3})$ where $g_{p}(x)$ is a matrix of size $n\times n$ . It is the Riemannian metric at point p expressed in coordinates x .

Dimensional analysis of condition 3 shows that divergence has the dimension of squared distance.

The **dual divergence** $D^{*}$ is defined as

$D^{*}(p,q)=D(q,p).$

When we wish to contrast D against $D^{*}$ , we refer to D as **primal divergence**.

Given any divergence D , its symmetrized version is obtained by averaging it with its dual divergence:

$D_{S}(p,q)=\textstyle {\frac {1}{2}}{\big (}D(p,q)+D(q,p){\big )}.$

### Difference from other similar concepts

Unlike metrics, divergences are not required to be symmetric, and the asymmetry is important in applications. Accordingly, one often refers asymmetrically to the divergence "of *q* from *p*" or "from *p* to *q*", rather than "between *p* and *q*". Secondly, divergences generalize *squared* distance, not linear distance, and thus do not satisfy the triangle inequality, but some divergences (such as the Bregman divergence) do satisfy generalizations of the Pythagorean theorem.

In general statistics and probability, "divergence" generally refers to any kind of function $D(p,q)$ , where $p,q$ are probability distributions or other objects under consideration, such that conditions 1, 2 are satisfied. Condition 3 is required for "divergence" as used in information geometry.

As an example, the total variation distance, a commonly used statistical divergence, does not satisfy condition 3.

## Notation

Notation for divergences varies significantly between fields, though there are some conventions.

Divergences are generally notated with an uppercase 'D', as in $D(x,y)$ , to distinguish them from metric distances, which are notated with a lowercase 'd'. When multiple divergences are in use, they are commonly distinguished with subscripts, as in $D_{\text{KL}}$ for Kullback–Leibler divergence (KL divergence).

Often a different separator between parameters is used, particularly to emphasize the asymmetry. In information theory, a double bar is commonly used: $D(p\parallel q)$ ; this is similar to, but distinct from, the notation for conditional probability, $P(A|B)$ , and emphasizes interpreting the divergence as a relative measurement, as in relative entropy; this notation is common for the KL divergence. A colon may be used instead, as $D(p:q)$ ; this emphasizes the relative information supporting the two distributions.

The notation for parameters varies as well. Uppercase $P,Q$ interprets the parameters as probability distributions, while lowercase $p,q$ or $x,y$ interprets them geometrically as points in a space, and $\mu _{1},\mu _{2}$ or $m_{1},m_{2}$ interprets them as measures.

## Geometrical properties

Many properties of divergences can be derived if we restrict *S* to be a statistical manifold, meaning that it can be parametrized with a finite-dimensional coordinate system *θ*, so that for a distribution *p* ∈ *S* we can write *p* = *p*(*θ*).

For a pair of points *p*, *q* ∈ *S* with coordinates *θ**p* and *θ**q*, denote the partial derivatives of *D*(*p*, *q*) as

${\begin{aligned}D((\partial _{i})_{p},q)\ \ &{\stackrel {\mathrm {def} }{=}}\ \ {\tfrac {\partial }{\partial \theta _{p}^{i}}}D(p,q),\\D((\partial _{i}\partial _{j})_{p},(\partial _{k})_{q})\ \ &{\stackrel {\mathrm {def} }{=}}\ \ {\tfrac {\partial }{\partial \theta _{p}^{i}}}{\tfrac {\partial }{\partial \theta _{p}^{j}}}{\tfrac {\partial }{\partial \theta _{q}^{k}}}D(p,q),\ \ \mathrm {etc.} \end{aligned}}$

Now we restrict these functions to a diagonal *p* = *q*, and denote

${\begin{aligned}D[\partial _{i},\cdot ]\ &:\ p\mapsto D((\partial _{i})_{p},p),\\D[\partial _{i},\partial _{j}]\ &:\ p\mapsto D((\partial _{i})_{p},(\partial _{j})_{p}),\ \ \mathrm {etc.} \end{aligned}}$

By definition, the function *D*(*p*, *q*) is minimized at *p* = *q*, and therefore

${\begin{aligned}&D[\partial _{i},\cdot ]=D[\cdot ,\partial _{i}]=0,\\&D[\partial _{i}\partial _{j},\cdot ]=D[\cdot ,\partial _{i}\partial _{j}]=-D[\partial _{i},\partial _{j}]\ \equiv \ g_{ij}^{(D)},\end{aligned}}$

where matrix *g*(*D*) is positive semi-definite and defines a unique Riemannian metric on the manifold *S*.

Divergence *D*(·, ·) also defines a unique torsion-free affine connection ∇(*D*) with coefficients

$\Gamma _{ij,k}^{(D)}=-D[\partial _{i}\partial _{j},\partial _{k}],$

and the dual to this connection ∇* is generated by the dual divergence *D**.

Thus, a divergence *D*(·, ·) generates on a statistical manifold a unique dualistic structure (*g*(*D*), ∇(*D*), ∇(*D**)). The converse is also true: every torsion-free dualistic structure on a statistical manifold is induced from some globally defined divergence function (which however need not be unique).

For example, when *D* is an f-divergence for some function ƒ(·), then it generates the metric *g*(*D**f*) = *c·g* and the connection ∇(*D**f*) = ∇(*α*), where *g* is the canonical Fisher information metric, ∇(*α*) is the α-connection, *c* = ƒ′′(1), and *α* = 3 + 2ƒ′′′(1)/ƒ′′(1).

## Examples

The two most important divergences are the relative entropy (Kullback–Leibler divergence, KL divergence), which is central to information theory and statistics, and the squared Euclidean distance (SED). Minimizing these two divergences is the main way that linear inverse problems are solved, via the principle of maximum entropy and least squares, notably in logistic regression and linear regression.

The two most important classes of divergences are the *f*-divergences and Bregman divergences; however, other types of divergence functions are also encountered in the literature. The only divergence for probabilities over a finite alphabet that is both an *f*-divergence and a Bregman divergence is the Kullback–Leibler divergence. The squared Euclidean divergence is a Bregman divergence (corresponding to the function ⁠ $x^{2}$ ⁠) but not an *f*-divergence.

### f-divergences

Given a convex function $f:[0,+\infty )\to (-\infty ,+\infty ]$ such that $f(0)=\lim _{t\to 0^{+}}f(t),f(1)=0$ , the *f*-divergence generated by f is defined as

$D_{f}(p,q)=\int p(x)f{\bigg (}{\frac {q(x)}{p(x)}}{\bigg )}dx$

.

| Kullback–Leibler divergence: | $D_{\mathrm {KL} }(p,q)=\int p(x)\ln \left({\frac {p(x)}{q(x)}}\right)dx$ |
|---|---|
| squared Hellinger distance: | $H^{2}(p,\,q)=2\int {\Big (}{\sqrt {p(x)}}-{\sqrt {q(x)}}\,{\Big )}^{2}dx$ |
| Jensen–Shannon divergence: | $D_{JS}(p,q)={\frac {1}{2}}\int p(x)\ln \left(p(x)\right)+q(x)\ln \left(q(x)\right)-(p(x)+q(x))\ln \left({\frac {p(x)+q(x)}{2}}\right)dx$ |
| α-divergence | $D^{(\alpha )}(p,q)={\frac {4}{1-\alpha ^{2}}}{\bigg (}1-\int p(x)^{\frac {1-\alpha }{2}}q(x)^{\frac {1+\alpha }{2}}dx{\bigg )}$ |
| chi-squared divergence: | $D_{\chi ^{2}}(p,q)=\int {\frac {(p(x)-q(x))^{2}}{p(x)}}dx$ |
| (*α*,*β*)-product divergence: | $D_{\alpha ,\beta }(p,q)={\frac {2}{(1-\alpha )(1-\beta )}}\int {\Big (}1-{\Big (}{\tfrac {q(x)}{p(x)}}{\Big )}^{\!\!{\frac {1-\alpha }{2}}}{\Big )}{\Big (}1-{\Big (}{\tfrac {q(x)}{p(x)}}{\Big )}^{\!\!{\frac {1-\beta }{2}}}{\Big )}p(x)dx$ |

### Bregman divergences

Bregman divergences correspond to convex functions on convex sets. Given a strictly convex, continuously differentiable function *F* on a convex set, known as the *Bregman generator*, the Bregman divergence measures the convexity of: the error of the linear approximation of *F* from *q* as an approximation of the value at *p*:

$D_{F}(p,q)=F(p)-F(q)-\langle \nabla F(q),p-q\rangle .$

The dual divergence to a Bregman divergence is the divergence generated by the convex conjugate *F** of the Bregman generator of the original divergence. For example, for the squared Euclidean distance, the generator is ⁠ $x^{2}$ ⁠, while for the relative entropy the generator is the negative entropy ⁠ $x\log x$ ⁠.

## History

The use of the term "divergence" – both what functions it refers to, and what various statistical distances are called – has varied significantly over time, but by c. 2000 had settled on the current usage within information geometry, notably in the textbook Amari & Nagaoka (2000).

The term "divergence" for a statistical distance was used informally in various contexts from c. 1910 to c. 1940. Its formal use dates at least to Bhattacharyya (1943), entitled "On a measure of divergence between two statistical populations defined by their probability distributions", which defined the Bhattacharyya distance, and Bhattacharyya (1946), entitled "On a Measure of Divergence between Two Multinomial Populations", which defined the Bhattacharyya angle. The term was popularized by its use for the Kullback–Leibler divergence in Kullback & Leibler (1951) and its use in the textbook Kullback (1959). The term "divergence" was used generally by Ali & Silvey (1966) for statistically distances. Numerous references to earlier uses of statistical distances are given in Adhikari & Joshi (1956) and Kullback (1959, pp. 6–7, §1.3 Divergence).

Kullback & Leibler (1951) actually used "divergence" to refer to the *symmetrized* divergence (this function had already been defined and used by Harold Jeffreys in 1948), referring to the asymmetric function as "the mean information for discrimination ... per observation", while Kullback (1959) referred to the asymmetric function as the "directed divergence". Ali & Silvey (1966) referred generally to such a function as a "coefficient of divergence", and showed that many existing functions could be expressed as *f*-divergences, referring to Jeffreys' function as "Jeffreys' measure of divergence" (today "Jeffreys divergence"), and Kullback–Leibler's asymmetric function (in each direction) as "Kullback's and Leibler's measures of discriminatory information" (today "Kullback–Leibler divergence").

The information geometry definition of divergence (the subject of this article) was initially referred to by alternative terms, including "quasi-distance" Amari (1982, p. 369) and "contrast function" Eguchi (1985), though "divergence" was used in Amari (1985) for the *α*-divergence, and has become standard for the general class.

The term "divergence" is in contrast to a distance (metric), since the symmetrized divergence does not satisfy the triangle inequality. For example, the term "Bregman distance" is still found, but "Bregman divergence" is now preferred.

Notationally, Kullback & Leibler (1951) denoted their asymmetric function as $I(1:2)$ , while Ali & Silvey (1966) denote their functions with a lowercase 'd' as $d\left(P_{1},P_{2}\right)$ .
