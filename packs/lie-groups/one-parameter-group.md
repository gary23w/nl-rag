---
title: "One-parameter group"
source: https://en.wikipedia.org/wiki/One-parameter_group
domain: lie-groups
license: CC-BY-SA-4.0
tags: lie group, lie theory, compact group, maximal torus
fetched: 2026-07-02
---

# One-parameter group

In mathematics, a **one-parameter group** or **one-parameter subgroup** usually means a continuous group homomorphism

$\varphi :\mathbb {R} \rightarrow G$

from the real line $\mathbb {R}$ (as an additive group) to some other topological group G . If $\varphi$ is injective then $\varphi (\mathbb {R} )$ , the image, will be a subgroup of G that is isomorphic to $\mathbb {R}$ as an additive group. Despite its name, "a one-parameter group" is not actually a group, but a homomorphism *between* groups.

One-parameter groups were introduced by Sophus Lie in 1893 to define infinitesimal transformations. According to Lie, an *infinitesimal transformation* is an infinitely small transformation of the one-parameter group that it generates. It is these infinitesimal transformations that generate a Lie algebra that is used to describe a Lie group of any dimension.

The action of a one-parameter group on a set is known as a flow. A smooth vector field on a manifold, at a point, induces a *local flow* - a one parameter group of local diffeomorphisms, sending points along integral curves of the vector field. The local flow of a vector field is used to define the Lie derivative of tensor fields along the vector field.

## Definition

A curve $\phi :\mathbb {R} \rightarrow G$ is called one-parameter subgroup of G if it satisfies the condition

$\phi (t)\phi (s)=\phi (s+t)$

.

## Examples

In Lie theory, one-parameter groups correspond to one-dimensional subspaces of the associated Lie algebra. The Lie group–Lie algebra correspondence is the basis of a science begun by Sophus Lie in the 1890s.

Another important case is seen in functional analysis, with G being the group of unitary operators on a Hilbert space. See Stone's theorem on one-parameter unitary groups.

In his monograph *Lie Groups*, P. M. Cohn gave the following theorem:

Any connected 1-dimensional Lie group is analytically isomorphic either to the additive group of real numbers

${\mathfrak {R}}$

, or to

${\mathfrak {T}}$

, the additive group of real numbers

$\mod 1$

. In particular, every 1-dimensional Lie group is locally isomorphic to

$\mathbb {R}$

.

## Physics

In physics, one-parameter groups describe dynamical systems. Furthermore, whenever a system of physical laws admits a one-parameter group of differentiable symmetries, then there is a conserved quantity, by Noether's theorem.

In the study of spacetime the use of the unit hyperbola to calibrate spatio-temporal measurements has become common since Hermann Minkowski discussed it in 1908. The principle of relativity was reduced to arbitrariness of which diameter of the unit hyperbola was used to determine a world-line. Using the parametrization of the hyperbola with hyperbolic angle, the theory of special relativity provided a calculus of relative motion with the one-parameter group indexed by rapidity. The *rapidity* replaces the *velocity* in kinematics and dynamics of relativity theory. Since rapidity is unbounded, the one-parameter group it stands upon is non-compact. The rapidity concept was introduced by E.T. Whittaker in 1910, and named by Alfred Robb the next year. The rapidity parameter amounts to the length of a hyperbolic versor, a concept of the nineteenth century. Mathematical physicists James Cockle, William Kingdon Clifford, and Alexander Macfarlane had all employed in their writings an equivalent mapping of the Cartesian plane by operator $(\cosh {a}+r\sinh {a})$ , where a is the hyperbolic angle and $r^{2}=+1$ .

## In GL(n,C)

An important example in the theory of Lie groups arises when G is taken to be $\mathrm {GL} (n;\mathbb {C} )$ , the group of invertible $n\times n$ matrices with complex entries. In that case, a basic result is the following:

Theorem

: Suppose

$\varphi :\mathbb {R} \rightarrow \mathrm {GL} (n;\mathbb {C} )$

is a one-parameter group. Then there exists a unique

$n\times n$

matrix

X

such that

$\varphi (t)=e^{tX}$

for all

$t\in \mathbb {R}$

.

It follows from this result that $\varphi$ is differentiable, even though this was not an assumption of the theorem. The matrix X can then be recovered from $\varphi$ as

$\left.{\frac {d\varphi (t)}{dt}}\right|_{t=0}=\left.{\frac {d}{dt}}\right|_{t=0}e^{tX}=\left.(Xe^{tX})\right|_{t=0}=Xe^{0}=X$

.

This result can be used, for example, to show that any continuous homomorphism between matrix Lie groups is smooth.

## Topology

A technical complication is that $\varphi (\mathbb {R} )$ as a subspace of G may carry a topology that is coarser than that on $\mathbb {R}$ ; this may happen in cases where $\varphi$ is injective. Think for example of the case where G is a torus T , and $\varphi$ is constructed by winding a straight line round T at an irrational slope.

In that case the induced topology may not be the standard one of the real line.
