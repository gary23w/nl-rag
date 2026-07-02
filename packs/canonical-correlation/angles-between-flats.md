---
title: "Angles between flats"
source: https://en.wikipedia.org/wiki/Angles_between_flats
domain: canonical-correlation
license: CC-BY-SA-4.0
tags: canonical correlation, cross-covariance, angles between flats, multivariate statistics
fetched: 2026-07-02
---

# Angles between flats

The concept of angles between lines (in the plane or in space), between two planes (*dihedral angle*) or between a line and a plane can be generalized to arbitrary dimensions. This generalization was first discussed by Camille Jordan. For any pair of flats in a Euclidean space of arbitrary dimension one can define a set of mutual angles which are invariant under isometric transformation of the Euclidean space. If the flats do not intersect, their shortest distance is one more invariant. These angles are called **canonical** or **principal**. The concept of angles can be generalized to pairs of flats in a finite-dimensional inner product space over the complex numbers.

## Jordan's definition

Let F and G be flats of dimensions k and l in the n -dimensional Euclidean space $E^{n}$ . By definition, a translation of F or G does not alter their mutual angles. If F and G do not intersect, they will do so upon any translation of G which maps some point in G to some point in F . It can therefore be assumed without loss of generality that F and G intersect.

Jordan shows that Cartesian coordinates $x_{1},\dots ,x_{\rho },$ $y_{1},\dots ,y_{\sigma },$ $z_{1},\dots ,z_{\tau },$ $u_{1},\dots ,u_{\upsilon },$ $v_{1},\dots ,v_{\alpha },$ $w_{1},\dots ,w_{\alpha }$ in $E^{n}$ can then be defined such that F and G are described, respectively, by the sets of equations

$x_{1}=0,\dots ,x_{\rho }=0,$

$u_{1}=0,\dots ,u_{\upsilon }=0,$

$v_{1}=0,\dots ,v_{\alpha }=0$

and

$x_{1}=0,\dots ,x_{\rho }=0,$

$z_{1}=0,\dots ,z_{\tau }=0,$

$v_{1}\cos \theta _{1}+w_{1}\sin \theta _{1}=0,\dots ,v_{\alpha }\cos \theta _{\alpha }+w_{\alpha }\sin \theta _{\alpha }=0$

with $0<\theta _{i}<\pi /2,i=1,\dots ,\alpha$ . Jordan calls these coordinates **canonical**. By definition, the angles $\theta _{i}$ are the **angles** between F and G .

The non-negative integers $\rho ,\sigma ,\tau ,\upsilon ,\alpha$ are constrained by

$\rho +\sigma +\tau +\upsilon +2\alpha =n,$

$\sigma +\tau +\alpha =k,$

$\sigma +\upsilon +\alpha =\ell .$

For these equations to determine the five non-negative integers completely, besides the dimensions $n,k$ and $\ell$ and the number $\alpha$ of angles $\theta _{i}$ , the non-negative integer $\sigma$ must be given. This is the number of coordinates $y_{i}$ , whose corresponding axes are those lying entirely within both F and G . The integer $\sigma$ is thus the dimension of $F\cap G$ . The set of angles $\theta _{i}$ may be supplemented with $\sigma$ angles 0 to indicate that $F\cap G$ has that dimension.

Jordan's proof applies essentially unaltered when $E^{n}$ is replaced with the n -dimensional inner product space $\mathbb {C} ^{n}$ over the complex numbers. (For angles between subspaces, the generalization to $\mathbb {C} ^{n}$ is discussed by Galántai and Hegedũs in terms of the below variational characterization.)

## Angles between subspaces

Now let F and G be subspaces of the n -dimensional inner product space over the real or complex numbers. Geometrically, F and G are flats, so Jordan's definition of mutual angles applies. When for any canonical coordinate $\xi$ the symbol ${\hat {\xi }}$ denotes the unit vector of the $\xi$ axis, the vectors ${\hat {y}}_{1},\dots ,{\hat {y}}_{\sigma },$ ${\hat {w}}_{1},\dots ,{\hat {w}}_{\alpha },$ ${\hat {z}}_{1},\dots ,{\hat {z}}_{\tau }$ form an orthonormal basis for F and the vectors ${\hat {y}}_{1},\dots ,{\hat {y}}_{\sigma },$ ${\hat {w}}'_{1},\dots ,{\hat {w}}'_{\alpha },$ ${\hat {u}}_{1},\dots ,{\hat {u}}_{\upsilon }$ form an orthonormal basis for G , where

${\hat {w}}'_{i}={\hat {w}}_{i}\cos \theta _{i}+{\hat {v}}_{i}\sin \theta _{i},\quad i=1,\dots ,\alpha .$

Being related to canonical coordinates, these basic vectors may be called **canonical**.

When $a_{i},i=1,\dots ,k$ denote the canonical basic vectors for F and $b_{i},i=1,\dots ,l$ the canonical basic vectors for G then the inner product $\langle a_{i},b_{j}\rangle$ vanishes for any pair of i and j except the following ones.

${\begin{aligned}&\langle {\hat {y}}_{i},{\hat {y}}_{i}\rangle =1,&&i=1,\dots ,\sigma ,\\&\langle {\hat {w}}_{i},{\hat {w}}'_{i}\rangle =\cos \theta _{i},&&i=1,\dots ,\alpha .\end{aligned}}$

With the above ordering of the basic vectors, the matrix of the inner products $\langle a_{i},b_{j}\rangle$ is thus diagonal. In other words, if $(a'_{i},i=1,\dots ,k)$ and $(b'_{i},i=1,\dots ,\ell )$ are arbitrary orthonormal bases in F and G then the real, orthogonal or unitary transformations from the basis $(a'_{i})$ to the basis $(a_{i})$ and from the basis $(b'_{i})$ to the basis $(b_{i})$ realize a singular value decomposition of the matrix of inner products $\langle a'_{i},b'_{j}\rangle$ . The diagonal matrix elements $\langle a_{i},b_{i}\rangle$ are the singular values of the latter matrix. By the uniqueness of the singular value decomposition, the vectors ${\hat {y}}_{i}$ are then unique up to a real, orthogonal or unitary transformation among them, and the vectors ${\hat {w}}_{i}$ and ${\hat {w}}'_{i}$ (and hence ${\hat {v}}_{i}$ ) are unique up to equal real, orthogonal or unitary transformations applied simultaneously to the sets of the vectors ${\hat {w}}_{i}$ associated with a common value of $\theta _{i}$ and to the corresponding sets of vectors ${\hat {w}}'_{i}$ (and hence to the corresponding sets of ${\hat {v}}_{i}$ ).

A singular value 1 can be interpreted as $\cos \,0$ corresponding to the angles 0 introduced above and associated with $F\cap G$ and a singular value 0 can be interpreted as $\cos \pi /2$ corresponding to right angles between the orthogonal spaces $F\cap G^{\bot }$ and $F^{\bot }\cap G$ , where superscript $\bot$ denotes the orthogonal complement.

## Variational characterization

The variational characterization of singular values and vectors implies as a special case a variational characterization of the angles between subspaces and their associated canonical vectors. This characterization includes the angles 0 and $\pi /2$ introduced above and orders the angles by increasing value. It can be given the form of the below alternative definition. In this context, it is customary to talk of **principal** angles and vectors.

### Definition

Let V be an inner product space. Given two subspaces ${\mathcal {U}},{\mathcal {W}}$ with $\dim({\mathcal {U}})=k\leq \dim({\mathcal {W}}):=\ell$ , there exists then a sequence of k angles $0\leq \theta _{1}\leq \theta _{2}\leq \cdots \leq \theta _{k}\leq \pi /2$ called the principal angles, the first one defined as

$\theta _{1}:=\min \left\{\arccos \left(\left.{\frac {|\langle u,w\rangle |}{\|u\|\|w\|}}\right)\,\right|\,u\in {\mathcal {U}},w\in {\mathcal {W}}\right\}=\angle (u_{1},w_{1}),$

where $\langle \cdot ,\cdot \rangle$ is the inner product and $\|\cdot \|$ the induced norm. The vectors $u_{1}$ and $w_{1}$ are the corresponding *principal vectors.*

The other principal angles and vectors are then defined recursively via

$\theta _{i}:=\min \left\{\left.\arccos \left({\frac {|\langle u,w\rangle |}{\|u\|\|w\|}}\right)\,\right|\,u\in {\mathcal {U}},~w\in {\mathcal {W}},~u\perp u_{j},~w\perp w_{j}\quad \forall j\in \{1,\ldots ,i-1\}\right\}.$

This means that the principal angles $(\theta _{1},\ldots ,\theta _{k})$ form a set of minimized angles between the two subspaces, and the principal vectors in each subspace are orthogonal to each other.

### Examples

#### Geometric example

Geometrically, subspaces are flats (points, lines, planes etc.) that include the origin, thus any two subspaces intersect at least in the origin. Two two-dimensional subspaces ${\mathcal {U}}$ and ${\mathcal {W}}$ generate a set of two angles. In a three-dimensional Euclidean space, the subspaces ${\mathcal {U}}$ and ${\mathcal {W}}$ are either identical, or their intersection forms a line. In the former case, both $\theta _{1}=\theta _{2}=0$ . In the latter case, only $\theta _{1}=0$ , where vectors $u_{1}$ and $w_{1}$ are on the line of the intersection ${\mathcal {U}}\cap {\mathcal {W}}$ and have the same direction. The angle $\theta _{2}>0$ will be the angle between the subspaces ${\mathcal {U}}$ and ${\mathcal {W}}$ in the orthogonal complement to ${\mathcal {U}}\cap {\mathcal {W}}$ . Imagining the angle between two planes in 3D, one intuitively thinks of the largest angle, $\theta _{2}>0$ .

#### Algebraic example

In 4-dimensional real coordinate space **R**4, let the two-dimensional subspace ${\mathcal {U}}$ be spanned by $u_{1}=(1,0,0,0)$ and $u_{2}=(0,1,0,0)$ , and let the two-dimensional subspace ${\mathcal {W}}$ be spanned by $w_{1}=(1,0,0,a)/{\sqrt {1+a^{2}}}$ and $w_{2}=(0,1,b,0)/{\sqrt {1+b^{2}}}$ with some real a and b such that $|a|<|b|$ . Then $u_{1}$ and $w_{1}$ are, in fact, the pair of principal vectors corresponding to the angle $\theta _{1}$ with $\cos(\theta _{1})=1/{\sqrt {1+a^{2}}}$ , and $u_{2}$ and $w_{2}$ are the principal vectors corresponding to the angle $\theta _{2}$ with $\cos(\theta _{2})=1/{\sqrt {1+b^{2}}}.$

To construct a pair of subspaces with any given set of k angles $\theta _{1},\ldots ,\theta _{k}$ in a $2k$ (or larger) dimensional Euclidean space, take a subspace ${\mathcal {U}}$ with an orthonormal basis $(e_{1},\ldots ,e_{k})$ and complete it to an orthonormal basis $(e_{1},\ldots ,e_{n})$ of the Euclidean space, where $n\geq 2k$ . Then, an orthonormal basis of the other subspace ${\mathcal {W}}$ is, e.g.,

$(\cos(\theta _{1})e_{1}+\sin(\theta _{1})e_{k+1},\ldots ,\cos(\theta _{k})e_{k}+\sin(\theta _{k})e_{2k}).$

## Basic properties

- If the largest angle is zero, one subspace is a subset of the other.
- If the largest angle is $\pi /2$ , there is at least one vector in one subspace perpendicular to the other subspace.
- If the smallest angle is zero, the subspaces intersect at least in a line.
- If the smallest angle is $\pi /2$ , the subspaces are orthogonal.
- The number of angles equal to zero is the dimension of the space where the two subspaces intersect.

## Advanced properties

- Non-trivial (different from 0 and $\pi /2$ ) angles between two subspaces are the same as the non-trivial angles between their orthogonal complements.
- Non-trivial angles between the subspaces ${\mathcal {U}}$ and ${\mathcal {W}}$ and the corresponding non-trivial angles between the subspaces ${\mathcal {U}}$ and ${\mathcal {W}}^{\perp }$ sum up to $\pi /2$ .
- The angles between subspaces satisfy the triangle inequality in terms of majorization and thus can be used to define a distance on the set of all subspaces turning the set into a metric space.
- The sine of the angles between subspaces satisfy the triangle inequality in terms of majorization and thus can be used to define a distance on the set of all subspaces turning the set into a metric space. For example, the sine of the largest angle is known as a gap between subspaces.

## Extensions

The notion of the angles and some of the variational properties can be naturally extended to arbitrary inner products and subspaces with infinite dimensions.

## Computation

Historically, the principal angles and vectors first appear in the context of canonical correlation and were originally computed using SVD of corresponding covariance matrices. However, as first noticed in, the canonical correlation is related to the cosine of the principal angles, which is ill-conditioned for small angles, leading to very inaccurate computation of highly correlated principal vectors in finite precision computer arithmetic. The sine-based algorithm fixes this issue, but creates a new problem of very inaccurate computation of highly uncorrelated principal vectors, since the sine function is ill-conditioned for angles close to **π/2.** To produce accurate principal vectors in computer arithmetic for the full range of the principal angles, the combined technique first compute all principal angles and vectors using the classical cosine-based approach, and then recomputes the principal angles smaller than **π/4** and the corresponding principal vectors using the sine-based approach. The combined technique is implemented in open-source libraries Octave and SciPy and contributed and to MATLAB.
