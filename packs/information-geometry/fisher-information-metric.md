---
title: "Fisher information metric"
source: https://en.wikipedia.org/wiki/Fisher_information_metric
domain: information-geometry
license: CC-BY-SA-4.0
tags: information geometry, fisher information metric, statistical manifold, bregman divergence
fetched: 2026-07-02
---

# Fisher information metric

In information geometry, the **Fisher information metric** is a particular Riemannian metric which can be defined on a smooth statistical manifold, *i.e.*, a smooth manifold whose points are probability distributions. It can be used to calculate the distance between probability distributions.

The metric is interesting in several aspects. By Chentsov's theorem, the Fisher information metric on statistical models is the only Riemannian metric (up to rescaling) that is invariant under sufficient statistics.

It can also be understood to be the infinitesimal form of the relative entropy (*i.e.*, the Kullback–Leibler divergence); specifically, it is the Hessian of the divergence. Alternately, it can be understood as the metric induced by the flat space Euclidean metric, after appropriate changes of variable. When pulled back to a complex projective Hilbert space, it becomes the Fubini–Study metric; when written in terms of mixed states, it is the quantum Bures metric.

Considered purely as a matrix, it is known as the Fisher information matrix. Considered as a measurement technique, where it is used to estimate hidden parameters in terms of observed random variables, it is known as the observed information.

## Definition

Given a statistical manifold with coordinates $\theta =(\theta _{1},\theta _{2},\ldots ,\theta _{n})$ , one writes $p(x\mid \theta )$ for the likelihood, that is the probability density of x as a function of $\theta$ . Here x is drawn from the value space *R* for a (discrete or continuous) random variable *X*. The likelihood is normalized over x but not $\theta$ : $\int _{R}p(x\mid \theta )\,dx=1.$

The Fisher information metric then takes the form:

$g_{jk}(\theta )=-\int _{R}{\frac {\partial ^{2}\log p(x\mid \theta )}{\partial \theta _{j}\,\partial \theta _{k}}}p(x\mid \theta )\,dx=\mathbb {E} _{x\sim p(x|\theta )}\left[-{\frac {\partial ^{2}\log p(x\mid \theta )}{\partial \theta _{j}\,\partial \theta _{k}}}\right].$

The integral is performed over all values *x* in *R*. The variable $\theta$ is now a coordinate on a Riemann manifold. The labels *j* and *k* index the local coordinate axes on the manifold.

When the probability is derived from the Gibbs measure, as it would be for any Markovian process, then $\theta$ can also be understood to be a Lagrange multiplier; Lagrange multipliers are used to enforce constraints, such as holding the expectation value of some quantity constant. If there are *n* constraints holding *n* different expectation values constant, then the dimension of the manifold is *n* dimensions smaller than the original space. In this case, the metric can be explicitly derived from the partition function; a derivation and discussion is presented there.

Equivalent forms are given by

$g_{jk}(\theta )=\int _{R}{\frac {\partial p(x\mid \theta )}{\partial \theta _{j}}}{\frac {\partial \log p(x\mid \theta )}{\partial \theta _{k}}}dx=\int _{R}{\frac {1}{p(x\mid \theta )}}{\frac {\partial p(x\mid \theta )}{\partial \theta _{j}}}{\frac {\partial p(x\mid \theta )}{\partial \theta _{k}}}dx.$

To show that the equivalent form equals the above definition, note that, because $p\cdot \partial \log p=\partial p$ ,

$\mathbb {E} _{x\sim p(x|\theta )}\left[{\frac {\partial \log {}p(x\mid \theta )}{\partial \theta _{j}}}\right]=0,$

and apply ${\frac {\partial }{\partial \theta _{k}}}$ on both sides.

Multiplying and dividing by p in the integrand, this can also be expressed as

$\mathbb {E} _{x\sim p(x|\theta )}\left[{\frac {\partial \log p(x\mid \theta )}{\partial \theta _{j}}}{\frac {\partial \log p(x\mid \theta )}{\partial \theta _{j}}}\right].$

Substituting $i(x\mid \theta )=-\log {}p(x\mid \theta )$ from information theory, an equivalent form of the above definition is:

$g_{jk}(\theta )=\int _{R}{\frac {\partial ^{2}i(x\mid \theta )}{\partial \theta _{j}\,\partial \theta _{k}}}p(x\mid \theta )\,dx=\mathbb {E} _{x\sim p(x|\theta )}\left[{\frac {\partial ^{2}i(x\mid \theta )}{\partial \theta _{j}\,\partial \theta _{k}}}\right]=\mathbb {E} _{x\sim p(x|\theta )}\left[{\frac {\partial i(x\mid \theta )}{\partial \theta _{j}}}{\frac {\partial i(x\mid \theta )}{\partial \theta _{k}}}\right].$

This last identity may look like a logical error at first, since it seems as though the second partial derivative has erroneously been factorized as a product of two first derivatives; however, this identity is true, and follows from the above algebraic manipulations of the log-likelihood derivatives within the expectation integral. Furthermore, because the expectations of each of these last two first partial derivative factors is zero, we can see that the Fisher information metric tensor is a covariance matrix, namely, the covariance matrix of the score functions (the partial derivatives of the negative log-likelihood) with respect to each parameter.

Finally, and perhaps most geometrically relevant, we can view the Fisher-Rao information metric as the inner product between two tangent vectors on the square-root embedding of probability distributions, namely,

$\int _{R}{\frac {\partial {\sqrt {p(x|\theta )}}}{\partial \theta _{j}}}{\frac {\partial {\sqrt {p(x|\theta )}}}{\partial \theta _{k}}}dx.$

## Examples

The Fisher information metric is particularly simple for the exponential family, which has $p(x\mid \theta )=\exp \!{\bigl [}\ \eta (\theta )\cdot T(x)-A(\theta )+B(x)\ {\bigr ]}$ The metric is $g_{jk}(\theta )={\frac {\partial ^{2}A(\theta )}{\partial \theta _{j}\,\partial \theta _{k}}}-{\frac {\partial ^{2}\eta (\theta )}{\partial \theta _{j}\,\partial \theta _{k}}}\cdot \mathrm {E} [T(x)]$ The metric has a particularly simple form if we are using the natural parameters. In this case, $\eta (\theta )=\theta$ , so the metric is just $\nabla _{\theta }^{2}A$ .

### Normal distribution

Multivariate normal distribution ${\mathcal {N}}(\mu ,\Sigma )$ $-\ln p(x|\mu ,\Sigma )={\frac {1}{2}}(x-\mu )^{T}\Sigma ^{-1}(x-\mu )+{\frac {1}{2}}\ln \det(\Sigma )+C$ Let $T=\Sigma ^{-1}$ be the precision matrix.

The metric diagonalizes to a mean part and a precision/variance part, that is, $g_{\mu ,\Sigma }=0$ . This is because $\partial _{\Sigma }(\partial _{\mu }\ln p(x|\mu ,\Sigma ))$ is the product of $(x-\mu )$ with a term that depends only on $\Sigma$ . Thus, its expectation is zero.

The mean part is the precision matrix: $g_{\mu _{i},\mu _{j}}=T_{ij}$ . The precision part is $g_{T,T}=-{\frac {1}{2}}\nabla _{T}^{2}\ln \det T$ .

An approximate expression can be derived for a Gaussian mixture model.

#### Single-variable normal distribution

In particular, for single variable normal distribution, $g={\begin{bmatrix}t&0\\0&(2t^{2})^{-1}\end{bmatrix}}$ where $t=\sigma ^{-2}$ . Let $x=\mu /{\sqrt {2}},y=\sigma$ , then $ds^{2}=td\mu ^{2}+{\frac {1}{2t^{2}}}dt^{2}=\sigma ^{-2}(d\mu ^{2}+2d\sigma ^{2})=2{\frac {dx^{2}+dy^{2}}{y^{2}}}$ This is the Poincaré half-plane model.

The shortest paths (geodesics) between two univariate normal distributions are either parallel to the $\sigma$ axis, or half circular arcs centered on the $\mu /{\sqrt {2}}$ -axis.

The geodesic connecting $\delta _{\mu _{0}},\delta _{\mu _{1}}$ has formula $\phi \mapsto {\mathcal {N}}\left({\frac {\mu _{0}+\mu _{1}}{2}}+{\frac {\mu _{1}-\mu _{0}}{2}}\cos \phi ,\sigma ^{2}\sin ^{2}\phi \right)$ where $\sigma ={\frac {\mu _{1}-\mu _{0}}{2{\sqrt {2}}}}$ , and the arc-length parametrization is $s={\sqrt {2}}\ln \tan(\phi /2)$ .

## Relation to the Kullback–Leibler divergence

Alternatively, the metric can be obtained as the second derivative of the *relative entropy* or Kullback–Leibler divergence. To obtain this, one considers two probability distributions $P(\theta )$ and $P(\theta _{0})$ , which are infinitesimally close to one another, so that

$P(\theta )=P(\theta _{0})+\sum _{j}\Delta \theta ^{j}\left.{\frac {\partial P}{\partial \theta ^{j}}}\right|_{\theta _{0}}$

with $\Delta \theta ^{j}$ an infinitesimally small change of $\theta$ in the *j* direction. Then, since the Kullback–Leibler divergence $D_{\mathrm {KL} }[P(\theta _{0})\|P(\theta )]$ has an absolute minimum of 0 when $P(\theta )=P(\theta _{0})$ , one has an expansion up to second order in $\theta =\theta _{0}$ of the form

$f_{\theta _{0}}(\theta ):=D_{\mathrm {KL} }[P(\theta _{0})\|P(\theta )]={\frac {1}{2}}\sum _{jk}\Delta \theta ^{j}\Delta \theta ^{k}g_{jk}(\theta _{0})+\mathrm {O} (\Delta \theta ^{3})$

.

The symmetric matrix $g_{jk}$ is positive (semi) definite and is the Hessian matrix of the function $f_{\theta _{0}}(\theta )$ at the extremum point $\theta _{0}$ . Intuitively, this states that the distance between two infinitesimally close points on a statistical differential manifold is the informational difference between them.

## Relation to Ruppeiner geometry

The Ruppeiner metric and Weinhold metric are the Fisher information metric calculated for Gibbs distributions as the ones found in equilibrium statistical mechanics.

## Change in free entropy

The action of a curve on a Riemannian manifold is given by

$A={\frac {1}{2}}\int _{a}^{b}{\frac {\partial \theta ^{j}}{\partial t}}g_{jk}(\theta ){\frac {\partial \theta ^{k}}{\partial t}}dt$

The path parameter here is time *t*; this action can be understood to give the change in free entropy of a system as it is moved from time *a* to time *b*. Specifically, one has

$\Delta S=(b-a)A\,$

as the change in free entropy. This observation has resulted in practical applications in chemical and processing industry: in order to minimize the change in free entropy of a system, one should follow the minimum geodesic path between the desired endpoints of the process. The geodesic minimizes the entropy, due to the Cauchy–Schwarz inequality, which states that the action is bounded below by the length of the curve, squared.

## Relation to the Jensen–Shannon divergence

The Fisher metric also allows the action and the curve length to be related to the Jensen–Shannon divergence. Specifically, one has

$(b-a)\int _{a}^{b}{\frac {\partial \theta ^{j}}{\partial t}}g_{jk}{\frac {\partial \theta ^{k}}{\partial t}}\,dt=8\int _{a}^{b}dJSD$

where the integrand *dJSD* is understood to be the infinitesimal change in the Jensen–Shannon divergence along the path taken. Similarly, for the curve length, one has

$\int _{a}^{b}{\sqrt {{\frac {\partial \theta ^{j}}{\partial t}}g_{jk}{\frac {\partial \theta ^{k}}{\partial t}}}}\,dt={\sqrt {8}}\int _{a}^{b}{\sqrt {dJSD}}$

That is, the square root of the Jensen–Shannon divergence is just the Fisher metric (divided by the square root of 8).

## As Euclidean metric

For a discrete probability space, that is, a probability space on a finite set of objects, the Fisher metric can be understood to simply be the Euclidean metric restricted to a positive orthant (e.g. "quadrant" in $\mathbb {R} ^{2}$ ) of a unit sphere, after appropriate changes of variable.

Consider a flat, Euclidean space, of dimension *N*+1, parametrized by points $y=(y_{0},\cdots ,y_{n})$ . The metric for Euclidean space is given by

$h=\sum _{i=0}^{N}dy_{i}\;dy_{i}$

where the $\textstyle dy_{i}$ are 1-forms; they are the basis vectors for the cotangent space. Writing $\textstyle {\frac {\partial }{\partial y_{j}}}$ as the basis vectors for the tangent space, so that

$dy_{j}\left({\frac {\partial }{\partial y_{k}}}\right)=\delta _{jk}$

,

the Euclidean metric may be written as

$h_{jk}^{\mathrm {flat} }=h\left({\frac {\partial }{\partial y_{j}}},{\frac {\partial }{\partial y_{k}}}\right)=\delta _{jk}$

The superscript 'flat' is there to remind that, when written in coordinate form, this metric is with respect to the flat-space coordinate y .

An *N*-dimensional unit sphere embedded in (*N* + 1)-dimensional Euclidean space may be defined as

$\sum _{i=0}^{N}y_{i}^{2}=1$

This embedding induces a metric on the sphere, it is inherited directly from the Euclidean metric on the ambient space. It takes exactly the same form as the above, taking care to ensure that the coordinates are constrained to lie on the surface of the sphere. This can be done, e.g. with the technique of Lagrange multipliers.

Consider now the change of variable $p_{i}=y_{i}^{2}$ . The sphere condition now becomes the probability normalization condition

$\sum _{i}p_{i}=1$

while the metric becomes

${\begin{aligned}h&=\sum _{i}dy_{i}\;dy_{i}=\sum _{i}d{\sqrt {p_{i}}}\;d{\sqrt {p_{i}}}\\&={\frac {1}{4}}\sum _{i}{\frac {dp_{i}\;dp_{i}}{p_{i}}}={\frac {1}{4}}\sum _{i}p_{i}\;d(\log p_{i})\;d(\log p_{i})\end{aligned}}$

The last can be recognized as one-fourth of the Fisher information metric. To complete the process, recall that the probabilities are parametric functions of the manifold variables $\theta$ , that is, one has $p_{i}=p_{i}(\theta )$ . Thus, the above induces a metric on the parameter manifold:

${\begin{aligned}h&={\frac {1}{4}}\sum _{i}p_{i}(\theta )\;d(\log p_{i}(\theta ))\;d(\log p_{i}(\theta ))\\&={\frac {1}{4}}\sum _{jk}\sum _{i}p_{i}(\theta )\;{\frac {\partial \log p_{i}(\theta )}{\partial \theta _{j}}}{\frac {\partial \log p_{i}(\theta )}{\partial \theta _{k}}}d\theta _{j}d\theta _{k}\end{aligned}}$

or, in coordinate form, the Fisher information metric is:

${\begin{aligned}g_{jk}(\theta )=4h_{jk}^{\mathrm {fisher} }&=4h\left({\frac {\partial }{\partial \theta _{j}}},{\frac {\partial }{\partial \theta _{k}}}\right)\\&=\sum _{i}p_{i}(\theta )\;{\frac {\partial \log p_{i}(\theta )}{\partial \theta _{j}}}\;{\frac {\partial \log p_{i}(\theta )}{\partial \theta _{k}}}\\&=\mathrm {E} \left[{\frac {\partial \log p_{i}(\theta )}{\partial \theta _{j}}}\;{\frac {\partial \log p_{i}(\theta )}{\partial \theta _{k}}}\right]\end{aligned}}$

where, as before,

$d\theta _{j}\left({\frac {\partial }{\partial \theta _{k}}}\right)=\delta _{jk}.$

The superscript 'fisher' is present to remind that this expression is applicable for the coordinates $\theta$ ; whereas the non-coordinate form is the same as the Euclidean (flat-space) metric. That is, the Fisher information metric on a statistical manifold is simply (four times) the Euclidean metric restricted to the positive orthant of the sphere, after appropriate changes of variable.

When the random variable p is not discrete, but continuous, the argument still holds. This can be seen in one of two different ways. One way is to carefully recast all of the above steps in an infinite-dimensional space, being careful to define limits appropriately, etc., in order to make sure that all manipulations are well-defined, convergent, etc. The other way, as noted by Gromov, is to use a category-theoretic approach; that is, to note that the above manipulations remain valid in the category of probabilities. Here such a category would have the Radon–Nikodym property, that is, the Radon–Nikodym theorem holds in this category. This includes the Hilbert spaces; these are square-integrable, and in the manipulations above, this is sufficient to safely replace the sum over squares by an integral over squares.

## As Fubini–Study metric

The above manipulations deriving the Fisher metric from the Euclidean metric can be extended to complex projective Hilbert spaces. In this case, one obtains the Fubini–Study metric. This should perhaps be no surprise, as the Fubini–Study metric provides the means of measuring information in quantum mechanics. The Bures metric, also known as the Helstrom metric, is identical to the Fubini–Study metric, although the latter is usually written in terms of pure states, as below, whereas the Bures metric is written for mixed states. By setting the phase of the complex coordinate to zero, one obtains exactly one-fourth of the Fisher information metric, exactly as above.

One begins with the same trick, of constructing a probability amplitude, written in polar coordinates, so:

$\psi (x;\theta )={\sqrt {p(x;\theta )}}\;e^{i\alpha (x;\theta )}$

Here, $\psi (x;\theta )$ is a complex-valued probability amplitude; $p(x;\theta )$ and $\alpha (x;\theta )$ are strictly real. The previous calculations are obtained by setting $\alpha (x;\theta )=0$ . The usual condition that probabilities lie within a simplex, namely that

$\int _{X}p(x;\theta )\,dx=1$

is equivalently expressed by the idea the square amplitude be normalized:

$\int _{X}\vert \psi (x;\theta )\vert ^{2}\,dx=1$

When $\psi (x;\theta )$ is real, this is the surface of a sphere.

The Fubini–Study metric, written in infinitesimal form, using quantum-mechanical bra–ket notation, is

$ds^{2}={\frac {\langle \delta \psi \mid \delta \psi \rangle }{\langle \psi \mid \psi \rangle }}-{\frac {\langle \delta \psi \mid \psi \rangle \;\langle \psi \mid \delta \psi \rangle }{{\langle \psi \mid \psi \rangle }^{2}}}.$

In this notation, one has that $\langle x\mid \psi \rangle =\psi (x;\theta )$ and integration over the entire measure space *X* is written as

$\langle \phi \mid \psi \rangle =\int _{X}\phi ^{*}(x;\theta )\psi (x;\theta )\,dx.$

The expression $\vert \delta \psi \rangle$ can be understood to be an infinitesimal variation; equivalently, it can be understood to be a 1-form in the cotangent space. Using the infinitesimal notation, the polar form of the probability above is simply

$\delta \psi =\left({\frac {\delta p}{2p}}+i\delta \alpha \right)\psi$

Inserting the above into the Fubini–Study metric gives:

${\begin{aligned}ds^{2}={}&{\frac {1}{4}}\int _{X}(\delta \log p)^{2}\;p\,dx\\[8pt]{}&+\int _{X}(\delta \alpha )^{2}\;p\,dx-\left(\int _{X}\delta \alpha \;p\,dx\right)^{2}\\[8pt]&{}+{\frac {i}{2}}\int _{X}(\delta \log p\delta \alpha -\delta \alpha \delta \log p)\;p\,dx\end{aligned}}$

Setting $\delta \alpha =0$ in the above makes it clear that the first term is (one-fourth of) the Fisher information metric. The full form of the above can be made slightly clearer by changing notation to that of standard Riemannian geometry, so that the metric becomes a symmetric 2-form acting on the tangent space. The change of notation is done simply replacing $\delta \to d$ and $ds^{2}\to h$ and noting that the integrals are just expectation values; so:

${\begin{aligned}h={}&{\frac {1}{4}}\mathrm {E} \left[(d\log p)^{2}\right]+\mathrm {E} \left[(d\alpha )^{2}\right]-\left(\mathrm {E} \left[d\alpha \right]\right)^{2}\\[8pt]{}&+{\frac {i}{2}}\mathrm {E} \left[d\log p\wedge d\alpha \right]\end{aligned}}$

The imaginary term is a symplectic form, it is the Berry phase or geometric phase. In index notation, the metric is:

${\begin{aligned}h_{jk}={}&h\left({\frac {\partial }{\partial \theta _{j}}},{\frac {\partial }{\partial \theta _{k}}}\right)\\[8pt]={}&{\frac {1}{4}}\mathrm {E} \left[{\frac {\partial \log p}{\partial \theta _{j}}}{\frac {\partial \log p}{\partial \theta _{k}}}\right]\\[8pt]{}&+\mathrm {E} \left[{\frac {\partial \alpha }{\partial \theta _{j}}}{\frac {\partial \alpha }{\partial \theta _{k}}}\right]-\mathrm {E} \left[{\frac {\partial \alpha }{\partial \theta _{j}}}\right]\mathrm {E} \left[{\frac {\partial \alpha }{\partial \theta _{k}}}\right]\\[8pt]&{}+{\frac {i}{2}}\mathrm {E} \left[{\frac {\partial \log p}{\partial \theta _{j}}}{\frac {\partial \alpha }{\partial \theta _{k}}}-{\frac {\partial \alpha }{\partial \theta _{j}}}{\frac {\partial \log p}{\partial \theta _{k}}}\right]\end{aligned}}$

Again, the first term can be clearly seen to be (one fourth of) the Fisher information metric, by setting $\alpha =0$ . Equivalently, the Fubini–Study metric can be understood as the metric on complex projective Hilbert space that is induced by the complex extension of the flat Euclidean metric. The difference between this, and the Bures metric, is that the Bures metric is written in terms of mixed states.

## Continuously-valued probabilities

A slightly more formal, abstract definition can be given, as follows.

Let *X* be an orientable manifold, and let $(X,\Sigma ,\mu )$ be a measure on *X*. Equivalently, let $(\Omega ,{\mathcal {F}},P)$ be a probability space on $\Omega =X$ , with sigma algebra ${\mathcal {F}}=\Sigma$ and probability $P=\mu$ .

The statistical manifold *S*(*X*) of *X* is defined as the space of all measures $\mu$ on *X* (with the sigma-algebra $\Sigma$ held fixed). Note that this space is infinite-dimensional, and is commonly taken to be a Fréchet space. The points of *S*(*X*) are measures.

Pick a point $\mu \in S(X)$ and consider the tangent space $T_{\mu }S$ . The Fisher information metric is then an inner product on the tangent space. With some abuse of notation, one may write this as

$g(\sigma _{1},\sigma _{2})=\int _{X}{\frac {d\sigma _{1}}{d\mu }}{\frac {d\sigma _{2}}{d\mu }}d\mu$

Here, $\sigma _{1}$ and $\sigma _{2}$ are vectors in the tangent space; that is, $\sigma _{1},\sigma _{2}\in T_{\mu }S$ . The abuse of notation is to write the tangent vectors as if they are derivatives, and to insert the extraneous *d* in writing the integral: the integration is meant to be carried out using the measure $\mu$ over the whole space *X*. This abuse of notation is, in fact, taken to be perfectly normal in measure theory; it is the standard notation for the Radon–Nikodym derivative.

In order for the integral to be well-defined, the space *S*(*X*) must have the Radon–Nikodym property, and more specifically, the tangent space is restricted to those vectors that are square-integrable. Square integrability is equivalent to saying that a Cauchy sequence converges to a finite value under the weak topology: the space contains its limit points. Note that Hilbert spaces possess this property.

This definition of the metric can be seen to be equivalent to the previous, in several steps. First, one selects a submanifold of *S*(*X*) by considering only those measures $\mu$ that are parameterized by some smoothly varying parameter $\theta$ . Then, if $\theta$ is finite-dimensional, then so is the submanifold; likewise, the tangent space has the same dimension as $\theta$ .

With some additional abuse of language, one notes that the exponential map provides a map from vectors in a tangent space to points in an underlying manifold. Thus, if $\sigma \in T_{\mu }S$ is a vector in the tangent space, then $p=\exp(\sigma )$ is the corresponding probability associated with point $p\in S(X)$ (after the parallel transport of the exponential map to $\mu$ .) Conversely, given a point $p\in S(X)$ , the logarithm gives a point in the tangent space (roughly speaking, as again, one must transport from the origin to point $\mu$ ; for details, refer to original sources). Thus, one has the appearance of logarithms in the simpler definition, previously given.
