---
title: "Christoffel symbols"
source: https://en.wikipedia.org/wiki/Christoffel_symbols
domain: general-relativity-numerics
license: CC-BY-SA-4.0
tags: numerical relativity, einstein field equations, adm formalism, gravitational wave modeling
fetched: 2026-07-02
---

# Christoffel symbols

In mathematics and physics, the **Christoffel symbols** are an array of numbers describing a metric connection. The metric connection is a specialization of the affine connection to surfaces or other manifolds endowed with a metric, allowing distances to be measured on that surface. In differential geometry, an affine connection can be defined without reference to a metric, and many additional concepts follow: parallel transport, covariant derivatives, geodesics, etc. also do not require the concept of a metric. However, when a metric is available, these concepts can be directly tied to the "shape" of the manifold itself; that shape is determined by how the tangent space is attached to the cotangent space by the metric tensor. Abstractly, one would say that the manifold has an associated (orthonormal) frame bundle, with each "frame" being a possible choice of a coordinate frame. An invariant metric implies that the structure group of the frame bundle is the orthogonal group O(*p*, *q*). As a result, such a manifold is necessarily a (pseudo-)Riemannian manifold. The Christoffel symbols provide a concrete representation of the connection of (pseudo-)Riemannian geometry in terms of coordinates on the manifold. Additional concepts, such as parallel transport, geodesics, etc. can then be expressed in terms of Christoffel symbols.

In general, there are an infinite number of metric connections for a given metric tensor; however, there is a unique connection that is free of torsion, the Levi-Civita connection. It is common in physics and general relativity to work almost exclusively with the Levi-Civita connection, by working in coordinate frames (called holonomic coordinates) where the torsion vanishes. For example, in Euclidean spaces, the Christoffel symbols describe how the local coordinate bases change from point to point.

At each point of the underlying *n*-dimensional manifold, for any local coordinate system around that point, the Christoffel symbols are denoted Γ*i**jk* for *i*, *j*, *k* = 1, 2, ..., *n*. Each entry of this *n* × *n* × *n* array is a real number. Under *linear* coordinate transformations on the manifold, the Christoffel symbols transform like the components of a tensor, but under general coordinate transformations (diffeomorphisms) they do not. Most of the algebraic properties of the Christoffel symbols follow from their relationship to the affine connection; only a few follow from the fact that the structure group is the orthogonal group O(*m*, *n*) (or the Lorentz group O(3, 1) for general relativity).

Christoffel symbols are used for performing practical calculations. For example, the Riemann curvature tensor can be expressed entirely in terms of the Christoffel symbols and their first partial derivatives. In general relativity, the connection plays the role of the gravitational force field with the corresponding gravitational potential being the metric tensor. When the coordinate system and the metric tensor share some symmetry, many of the Γ*i**jk* are zero.

The Christoffel symbols are named for Elwin Bruno Christoffel (1829–1900).

## Note

The definitions given below are valid for both Riemannian manifolds and pseudo-Riemannian manifolds, such as those of general relativity, with careful distinction being made between upper and lower indices (contra-variant and co-variant indices). The formulas hold for either sign convention, unless otherwise noted.

Einstein summation convention is used in this article, with vectors indicated by bold font. The **connection coefficients** of the Levi-Civita connection (or pseudo-Riemannian connection) expressed in a coordinate basis are called *Christoffel symbols*.

## Preliminary definitions

Given a manifold M , an atlas consists of a collection of charts $\varphi :U\to \mathbb {R} ^{n}$ for each open cover $U\subset M$ . Such charts allow the standard vector basis $({\vec {e}}_{1},\cdots ,{\vec {e}}_{n})$ on $\mathbb {R} ^{n}$ to be pulled back to a vector basis on the tangent space $TM$ of M . This is done as follows. Given some arbitrary real function $f:M\to \mathbb {R}$ , the chart allows a gradient to be defined:

$\partial _{i}f\equiv {\frac {\partial \left(f\circ \varphi ^{-1}\right)}{\partial x^{i}}}\quad {\mbox{for }}i=1,\,2,\,\dots ,\,n$

This gradient is commonly called a pullback because it "pulls back" the gradient on $\mathbb {R} ^{n}$ to a gradient on M . The pullback is independent of the chart $\varphi$ . In this way, the standard vector basis $({\vec {e}}_{1},\cdots ,{\vec {e}}_{n})$ on $\mathbb {R} ^{n}$ pulls back to a standard ("coordinate") vector basis $(\partial _{1},\cdots ,\partial _{n})$ on $TM$ . This is called the "coordinate basis", because it explicitly depends on the coordinates on $\mathbb {R} ^{n}$ . It is sometimes called the "local basis".

This definition allows a common abuse of notation. The $\partial _{i}$ were defined to be in one-to-one correspondence with the basis vectors ${\vec {e}}_{i}$ on $\mathbb {R} ^{n}$ . The notation $\partial _{i}$ serves as a reminder that the basis vectors on the tangent space $TM$ came from a gradient construction. Despite this, it is common to "forget" this construction, and just write (or rather, define) vectors $e_{i}$ on $TM$ such that $e_{i}\equiv \partial _{i}$ . The full range of commonly used notation includes the use of arrows and boldface to denote vectors:

$\partial _{i}\equiv {\frac {\partial }{\partial x^{i}}}\equiv e_{i}\equiv {\vec {e}}_{i}\equiv \mathbf {e} _{i}\equiv {\boldsymbol {\partial }}_{i}$

where $\equiv$ is used as a reminder that these are defined to be equivalent notation for the same concept. The choice of notation is according to style and taste, and varies from text to text.

The coordinate basis provides a vector basis for vector fields on M . Commonly used notation for vector fields on M include

$X={\vec {X}}=X^{i}\partial _{i}=X^{i}{\frac {\partial }{\partial x^{i}}}$

The upper-case X , without the vector-arrow, is particularly popular for index-free notation, because it both minimizes clutter and reminds that results are independent of the chosen basis, and, in this case, independent of the atlas.

The same abuse of notation is used to push forward one-forms from $\mathbb {R} ^{n}$ to M . This is done by writing $(\varphi ^{1},\ldots ,\varphi ^{n})=(x^{1},\ldots ,x^{n})$ or $x=\varphi$ or $x^{i}=\varphi ^{i}$ . The one-form is then $dx^{i}=d\varphi ^{i}$ . This is soldered to the basis vectors as $dx^{i}(\partial _{j})=\delta _{j}^{i}$ . Note the careful use of upper and lower indexes, to distinguish contravariant and covariant vectors.

The pullback induces (defines) a metric tensor on M . Several styles of notation are commonly used: $g_{ij}=\mathbf {e} _{i}\cdot \mathbf {e} _{j}=\langle {\vec {e}}_{i},{\vec {e}}_{j}\rangle =e_{i}^{a}e_{j}^{b}\,\eta _{ab}$ where both the centerdot and the angle-bracket $\langle ,\rangle$ denote the scalar product. The last form uses the tensor $\eta _{ab}$ , which is understood to be the "flat-space" metric tensor. For Riemannian manifolds, it is the Kronecker delta $\eta _{ab}=\delta _{ab}$ . For pseudo-Riemannian manifolds, it is the diagonal matrix having signature $(p,q)$ . The notation $e_{i}^{a}$ serves as a reminder that pullback really is a linear transform, given as the gradient, above. The index letters $a,b,c,\cdots$ live in $\mathbb {R} ^{n}$ while the index letters $i,j,k,\cdots$ live in the tangent manifold.

The matrix inverse $g^{ij}$ of the metric tensor $g_{ij}$ is given by $g^{ij}g_{jk}=\delta _{k}^{i}$ This is used to define the dual basis: $\mathbf {e} ^{i}=\mathbf {e} _{j}g^{ji},\quad i=1,\,2,\,\dots ,\,n$

Some texts write $\mathbf {g} _{i}$ for $\mathbf {e} _{i}$ , so that the metric tensor takes the particularly beguiling form $g_{ij}=\mathbf {g} _{i}\cdot \mathbf {g} _{j}$ . This is commonly done so that the symbol $e_{i}$ can be used unambiguously for the vierbein.

## Definition in Euclidean space

In Euclidean space, the general definition given below for the Christoffel symbols of the second kind can be proven to be equivalent to: ${\Gamma ^{k}}_{ij}={\frac {\partial \mathbf {e} _{j}}{\partial x^{i}}}\cdot \mathbf {e} ^{k}={\frac {\partial \mathbf {e} _{j}}{\partial x^{i}}}\cdot g^{km}\mathbf {e} _{m}$

Christoffel symbols of the first kind can then be found via index lowering: $\Gamma _{kij}={\Gamma ^{m}}_{ij}g_{mk}={\frac {\partial \mathbf {e} _{j}}{\partial x^{i}}}\cdot \mathbf {e} ^{m}g_{mk}={\frac {\partial \mathbf {e} _{j}}{\partial x^{i}}}\cdot \mathbf {e} _{k}$

Rearranging, we see that (assuming the partial derivative belongs to the tangent space, which cannot occur on a non-Euclidean curved space): ${\frac {\partial \mathbf {e} _{j}}{\partial x^{i}}}={\Gamma ^{k}}_{ij}\mathbf {e} _{k}=\Gamma _{kij}\mathbf {e} ^{k}$

In words, the arrays represented by the Christoffel symbols track how the basis changes from point to point. If the derivative does not lie on the tangent space, the right expression is the projection of the derivative over the tangent space (see covariant derivative below). Symbols of the second kind decompose the change with respect to the basis, while symbols of the first kind decompose it with respect to the dual basis. In this form, it is easy to see the symmetry of the lower or last two indices: ${\Gamma ^{k}}_{ij}={\Gamma ^{k}}_{ji}$ and $\Gamma _{kij}=\Gamma _{kji},$ from the definition of $\mathbf {e} _{i}$ and the fact that partial derivatives commute (as long as the manifold and coordinate system are well behaved).

The same numerical values for Christoffel symbols of the second kind also relate to derivatives of the dual basis, as seen in the expression: ${\frac {\partial \mathbf {e} ^{i}}{\partial x^{j}}}=-{\Gamma ^{i}}_{jk}\mathbf {e} ^{k},$ which we can rearrange as: ${\Gamma ^{i}}_{jk}=-{\frac {\partial \mathbf {e} ^{i}}{\partial x^{j}}}\cdot \mathbf {e} _{k}.$

## General definition

The Christoffel symbols come in two forms: the first kind, and the second kind. The definition of the second kind is more basic, and thus is presented first.

### Christoffel symbols of the second kind (symmetric definition)

The Christoffel symbols of the second kind are the connection coefficients—in a coordinate basis—of the Levi-Civita connection. In other words, the Christoffel symbols of the second kind Γ*k**ij* (sometimes Γ*k* *ij* or {*k* *ij*}) are defined as the unique coefficients such that $\nabla _{i}\mathrm {e} _{j}={\Gamma ^{k}}_{ij}\mathrm {e} _{k},$ where $\nabla _{i}$ is the Levi-Civita connection on *M* taken in the coordinate direction e*i* (i.e., ∇*i* ≡ ∇e*i*) and where $e_{i}=\partial _{i}$ is a local coordinate (holonomic) basis. Since this connection has zero torsion, and holonomic vector fields commute (i.e. $[e_{i},e_{j}]=[\partial _{i},\partial _{j}]=0$ ) we have $\nabla _{i}\mathrm {e} _{j}=\nabla _{j}\mathrm {e} _{i}.$ Hence in this basis the connection coefficients are symmetric: ${\Gamma ^{k}}_{ij}={\Gamma ^{k}}_{ji}.$ For this reason, a torsion-free connection is often called *symmetric*.

The Christoffel symbols can be derived from the vanishing of the covariant derivative of the metric tensor $g_{ik}$ : $0=\nabla _{l}g_{ik}={\frac {\partial g_{ik}}{\partial x^{l}}}-g_{mk}{\Gamma ^{m}}_{il}-g_{im}{\Gamma ^{m}}_{kl}={\frac {\partial g_{ik}}{\partial x^{l}}}-2g_{m(k}{\Gamma ^{m}}_{i)l}.$

As a shorthand notation, the nabla symbol and the partial derivative symbols are frequently dropped, and instead a semicolon and a comma are used to set off the index that is being used for the derivative. Thus, the above is sometimes written as $0=\,g_{ik;l}=g_{ik,l}-g_{mk}{\Gamma ^{m}}_{il}-g_{im}{\Gamma ^{m}}_{kl}.$

Using that the symbols are symmetric in the lower two indices, one can solve explicitly for the Christoffel symbols as a function of the metric tensor by permuting the indices and resumming: ${\Gamma ^{i}}_{kl}={\frac {1}{2}}g^{im}\left({\frac {\partial g_{mk}}{\partial x^{l}}}+{\frac {\partial g_{ml}}{\partial x^{k}}}-{\frac {\partial g_{kl}}{\partial x^{m}}}\right)={\frac {1}{2}}g^{im}\left(g_{mk,l}+g_{ml,k}-g_{kl,m}\right),$

where (*gjk*) is the inverse of the matrix (*gjk*), defined as (using the Kronecker delta, and Einstein notation for summation) $g^{ji}g_{ik}=\delta ^{j}{}_{k}$ . Although the Christoffel symbols are written in the same notation as tensors with index notation, they do not transform like tensors under a change of coordinates.

#### Contraction of indices

Contracting the upper index with either of the lower indices (those being symmetric) leads to ${\Gamma ^{i}}_{ki}={\frac {\partial }{\partial x^{k}}}\ln {\sqrt {|g|}}$ where $g=\det g_{ik}$ is the determinant of the metric tensor. This identity can be used to evaluate the divergence of vectors and the covariant derivatives of tensor densities. Also

${\Gamma ^{i}}_{ki}={\Gamma ^{i}}_{ik}={\tfrac {1}{2}}\left(g^{mi}g_{mk,i}+g^{mi}g_{mi,k}-g^{im}g_{ki,m}\right)={\tfrac {1}{2}}g^{mi}g_{mi,k}$

.

### Christoffel symbols of the first kind

The Christoffel symbols of the first kind can be derived either from the Christoffel symbols of the second kind and the metric, $\Gamma _{cab}=g_{cd}{\Gamma ^{d}}_{ab}\,,$

or from the metric alone, ${\begin{aligned}\Gamma _{cab}&={\frac {1}{2}}\left({\frac {\partial g_{ca}}{\partial x^{b}}}+{\frac {\partial g_{cb}}{\partial x^{a}}}-{\frac {\partial g_{ab}}{\partial x^{c}}}\right)\\&={\frac {1}{2}}\,\left(g_{ca,b}+g_{cb,a}-g_{ab,c}\right)\\&={\frac {1}{2}}\,\left(\partial _{b}g_{ca}+\partial _{a}g_{cb}-\partial _{c}g_{ab}\right)\,.\\\end{aligned}}$

As an alternative notation one also finds

$\Gamma _{cab}=[ab,c].$ It is worth noting that [*ab*, *c*] = [*ba*, *c*].

### Connection coefficients in a nonholonomic basis

The Christoffel symbols are most typically defined in a coordinate basis, which is the convention followed here. In other words, the name **Christoffel symbols** is reserved only for coordinate (i.e., holonomic) frames. However, the connection coefficients can also be defined in an arbitrary (i.e., nonholonomic) basis of tangent vectors **u***i* by $\nabla _{\mathbf {u} _{i}}\mathbf {u} _{j}={\omega ^{k}}_{ij}\mathbf {u} _{k}.$

Explicitly, in terms of the metric tensor, this is ${\omega ^{i}}_{kl}={\frac {1}{2}}g^{im}\left(g_{mk,l}+g_{ml,k}-g_{kl,m}+c_{mkl}+c_{mlk}-c_{klm}\right),$

where *cklm* = *gmpcklp* are the commutation coefficients of the basis; that is, $[\mathbf {u} _{k},\,\mathbf {u} _{l}]={c_{kl}}^{m}\mathbf {u} _{m}$

where **u***k* are the basis vectors and [ , ] is the Lie bracket. The standard unit vectors in spherical and cylindrical coordinates furnish an example of a basis with non-vanishing commutation coefficients. The difference between the connection in such a frame, and the Levi-Civita connection is known as the contorsion tensor.

### Ricci rotation coefficients (asymmetric definition)

When we choose the basis **X***i* ≡ **u***i* orthonormal: *gab* ≡ *ηab* = ⟨*Xa*, *Xb*⟩ then *gmk,l* ≡ *ηmk,l* = 0. This implies that ${\omega ^{i}}_{kl}={\frac {1}{2}}\eta ^{im}\left(c_{mkl}+c_{mlk}-c_{klm}\right)$ and the connection coefficients become antisymmetric in the first two indices: $\omega _{abc}=-\omega _{bac}\,,$ where $\omega _{abc}=\eta _{ad}{\omega ^{d}}_{bc}\,.$

In this case, the connection coefficients *ωabc* are called the **Ricci rotation coefficients**.

Equivalently, one can define Ricci rotation coefficients as follows: ${\omega ^{k}}_{ij}:=\mathbf {u} ^{k}\cdot \left(\nabla _{j}\mathbf {u} _{i}\right)\,,$ where **u***i* is an orthonormal nonholonomic basis and **u***k* = *ηkl***u***l* its *co-basis*.

## Transformation law under change of variable

Under a change of variable from $\left(x^{1},\,\ldots ,\,x^{n}\right)$ to $\left({\bar {x}}^{1},\,\ldots ,\,{\bar {x}}^{n}\right)$ , Christoffel symbols transform as

${{\bar {\Gamma }}^{i}}_{kl}={\frac {\partial {\bar {x}}^{i}}{\partial x^{m}}}\,{\frac {\partial x^{n}}{\partial {\bar {x}}^{k}}}\,{\frac {\partial x^{p}}{\partial {\bar {x}}^{l}}}\,{\Gamma ^{m}}_{np}+{\frac {\partial ^{2}x^{m}}{\partial {\bar {x}}^{k}\partial {\bar {x}}^{l}}}\,{\frac {\partial {\bar {x}}^{i}}{\partial x^{m}}}$

where the overline denotes the Christoffel symbols in the ${\bar {x}}^{i}$ coordinate system. The Christoffel symbol does **not** transform as a tensor, but rather as an object in the jet bundle. More precisely, the Christoffel symbols can be considered as functions on the jet bundle of the frame bundle of *M*, independent of any local coordinate system. Choosing a local coordinate system determines a local section of this bundle, which can then be used to pull back the Christoffel symbols to functions on *M*, though of course these functions then depend on the choice of local coordinate system.

For each point, there exist coordinate systems in which the Christoffel symbols vanish at the point. These are called (geodesic) normal coordinates, and are often used in Riemannian geometry.

There are some interesting properties which can be derived directly from the transformation law.

- For linear transformation, the inhomogeneous part of the transformation (second term on the right-hand side) vanishes identically and then ${\Gamma ^{i}}_{jk}$ behaves like a tensor.
- If we have two fields of connections, say ${\Gamma ^{i}}_{jk}$ and ${{\tilde {\Gamma }}^{i}}_{jk}$ , then their difference ${\Gamma ^{i}}_{jk}-{{\tilde {\Gamma }}^{i}}_{jk}$ is a tensor since the inhomogeneous terms cancel each other. The inhomogeneous terms depend only on how the coordinates are changed, but are independent of Christoffel symbol itself.
- If the Christoffel symbol is unsymmetric about its lower indices in one coordinate system i.e., ${\Gamma ^{i}}_{jk}\neq {\Gamma ^{i}}_{kj}$ , then they remain unsymmetric under any change of coordinates. A corollary to this property is that it is impossible to find a coordinate system in which all elements of Christoffel symbol are zero at a point, unless lower indices are symmetric. This property was pointed out by Albert Einstein and Erwin Schrödinger independently.

## Relationship to parallel transport and derivation of Christoffel symbols in Riemannian space

If a vector $\xi ^{i}$ is transported parallel on a curve parametrized by some parameter s on a Riemannian manifold, the rate of change of the components of the vector is given by ${\frac {d\xi ^{i}}{ds}}=-{\Gamma ^{i}}_{mj}{\frac {dx^{m}}{ds}}\xi ^{j}.$

Now just by using the condition that the scalar product $g_{ik}\xi ^{i}\eta ^{k}$ formed by two arbitrary vectors $\xi ^{i}$ and $\eta ^{k}$ is unchanged is enough to derive the Christoffel symbols. The condition is ${\frac {d}{ds}}\left(g_{ik}\xi ^{i}\eta ^{k}\right)=0$ which by the product rule expands to ${\frac {\partial g_{ik}}{\partial x^{l}}}{\frac {dx^{l}}{ds}}\xi ^{i}\eta ^{k}+g_{ik}{\frac {d\xi ^{i}}{ds}}\eta ^{k}+g_{ik}\xi ^{i}{\frac {d\eta ^{k}}{ds}}=0.$

Applying the parallel transport rule for the two arbitrary vectors and relabelling dummy indices and collecting the coefficients of $\xi ^{i}\eta ^{k}dx^{l}$ (arbitrary), we obtain

${\frac {\partial g_{ik}}{\partial x^{l}}}=g_{rk}{\Gamma ^{r}}_{il}+g_{ir}{\Gamma ^{r}}_{lk}.$

This is same as the equation obtained by requiring the covariant derivative of the metric tensor to vanish in the General definition section. The derivation from here is simple. By cyclically permuting the indices $ikl$ in above equation, we can obtain two more equations and then linearly combining these three equations, we can express ${\Gamma ^{i}}_{jk}$ in terms of the metric tensor.

## Relationship to index-free notation

Let *X* and *Y* be vector fields with components *Xi* and *Yk*. Then the *k*th component of the covariant derivative of *Y* with respect to *X* is given by $\left(\nabla _{X}Y\right)^{k}=X^{i}(\nabla _{i}Y)^{k}=X^{i}\left({\frac {\partial Y^{k}}{\partial x^{i}}}+{\Gamma ^{k}}_{im}Y^{m}\right).$

Here, the Einstein notation is used, so repeated indices indicate summation over indices and contraction with the metric tensor serves to raise and lower indices: $g(X,Y)=X^{i}Y_{i}=g_{ik}X^{i}Y^{k}=g^{ik}X_{i}Y_{k}.$

Keep in mind that *gik* ≠ *gik* and that *gik* = *δ ik*, the Kronecker delta. The convention is that the metric tensor is the one with the lower indices; the correct way to obtain *gik* from *gik* is to solve the linear equations *gijgjk* = *δ ik*.

The statement that the connection is torsion-free, namely that $\nabla _{X}Y-\nabla _{Y}X=[X,\,Y]$

is equivalent to the statement that—in a coordinate basis—the Christoffel symbol is symmetric in the lower two indices: ${\Gamma ^{i}}_{jk}={\Gamma ^{i}}_{kj}.$

The index-less transformation properties of a tensor are given by pullbacks for covariant indices, and pushforwards for contravariant indices. The article on covariant derivatives provides additional discussion of the correspondence between index-free notation and indexed notation.

## Covariant derivatives of tensors

The covariant derivative of a vector field with components *Vm* is $\nabla _{l}V^{m}={\frac {\partial V^{m}}{\partial x^{l}}}+{\Gamma ^{m}}_{kl}V^{k}.$

By corollary, divergence of a vector can be obtained as $\nabla _{i}V^{i}={\frac {1}{\sqrt {-g}}}{\frac {\partial \left({\sqrt {-g}}\,V^{i}\right)}{\partial x^{i}}}.$

The covariant derivative of a covector field *ωm* is $\nabla _{l}\omega _{m}={\frac {\partial \omega _{m}}{\partial x^{l}}}-{\Gamma ^{k}}_{ml}\omega _{k}.$

The symmetry of the Christoffel symbol now implies $\nabla _{i}\nabla _{j}\varphi =\nabla _{j}\nabla _{i}\varphi$ for any scalar field, but in general the covariant derivatives of higher order tensor fields do not commute (see curvature tensor).

The covariant derivative of a type (2, 0) tensor field *Aik* is $\nabla _{l}A^{ik}={\frac {\partial A^{ik}}{\partial x^{l}}}+{\Gamma ^{i}}_{ml}A^{mk}+{\Gamma ^{k}}_{ml}A^{im},$ that is, ${A^{ik}}_{;l}={A^{ik}}_{,l}+A^{mk}{\Gamma ^{i}}_{ml}+A^{im}{\Gamma ^{k}}_{ml}.$

If the tensor field is mixed then its covariant derivative is ${A^{i}}_{k;l}={A^{i}}_{k,l}+{A^{m}}_{k}{\Gamma ^{i}}_{ml}-{A^{i}}_{m}{\Gamma ^{m}}_{kl},$ and if the tensor field is of type (0, 2) then its covariant derivative is $A_{ik;l}=A_{ik,l}-A_{mk}{\Gamma ^{m}}_{il}-A_{im}{\Gamma ^{m}}_{kl}.$

### Contravariant derivatives of tensors

To find the contravariant derivative of a vector field, we must first transform it into a covariant derivative using the metric tensor $\nabla ^{l}V^{m}=g^{il}\nabla _{i}V^{m}=g^{il}\partial _{i}V^{m}+g^{il}\Gamma _{ki}^{m}V^{k}=\partial ^{l}V^{m}+g^{il}\Gamma _{ki}^{m}V^{k}$

## Applications

### In general relativity

The Christoffel symbols find frequent use in Einstein's theory of general relativity, where spacetime is represented by a curved 4-dimensional Lorentz manifold with a Levi-Civita connection. The Einstein field equations—which determine the geometry of spacetime in the presence of matter—contain the Ricci tensor, and so calculating the Christoffel symbols is essential. Once the geometry is determined, the paths of particles and light beams are calculated by solving the geodesic equations in which the Christoffel symbols explicitly appear.

### In classical (non-relativistic) mechanics

Let $x^{i}$ be the generalized coordinates and ${\dot {x}}^{i}$ be the generalized velocities, then the kinetic energy for a unit mass is given by $T={\tfrac {1}{2}}g_{ik}{\dot {x}}^{i}{\dot {x}}^{k}$ , where $g_{ik}$ is the metric tensor. If $V\left(x^{i}\right)$ , the potential function, exists then the contravariant components of the generalized force per unit mass are $F_{i}=\partial V/\partial x^{i}$ . The metric (here in a purely spatial domain) can be obtained from the line element $ds^{2}=2Tdt^{2}$ . Substituting the Lagrangian $L=T-V$ into the Euler-Lagrange equation, we get

$g_{ik}{\ddot {x}}^{k}+{\frac {1}{2}}\left({\frac {\partial g_{ik}}{\partial x^{l}}}+{\frac {\partial g_{il}}{\partial x^{k}}}-{\frac {\partial g_{lk}}{\partial x^{i}}}\right){\dot {x}}^{l}{\dot {x}}^{k}=F_{i}.$

Now multiplying by $g^{ij}$ , we get ${\ddot {x}}^{j}+{\Gamma ^{j}}_{lk}{\dot {x}}^{l}{\dot {x}}^{k}=F^{j}.$

When Cartesian coordinates can be adopted (as in inertial frames of reference), we have an Euclidean metrics, the Christoffel symbol vanishes, and the equation reduces to Newton's second law of motion. In curvilinear coordinates (forcedly in non-inertial frames, where the metrics is non-Euclidean and not flat), fictitious forces like the Centrifugal force and Coriolis force originate from the Christoffel symbols, so from the purely spatial curvilinear coordinates.

### In Earth surface coordinates

Given a spherical coordinate system, which describes points on the Earth surface (approximated as an ideal sphere).

${\begin{aligned}x(R,\theta ,\varphi )&={\begin{pmatrix}R\cos \theta \cos \varphi &R\cos \theta \sin \varphi &R\sin \theta \end{pmatrix}}\\\end{aligned}}$

For a point x, R is the distance to the Earth core (usually approximately the Earth radius). θ and φ are the latitude and longitude. Positive θ is the northern hemisphere. To simplify the derivatives, the angles are given in radians (where d sin(x)/dx = cos(x), the degree values introduce an additional factor of 360 / 2 pi).

At any location, the tangent directions are $e_{R}$ (up), $e_{\theta }$ (north) and $e_{\varphi }$ (east) - you can also use indices 1,2,3.

${\begin{aligned}e_{R}&={\begin{pmatrix}\cos \theta \cos \varphi &\cos \theta \sin \varphi &\sin \theta \end{pmatrix}}\\e_{\theta }&=R\cdot {\begin{pmatrix}-\sin \theta \cos \varphi &-\sin \theta \sin \varphi &\cos \theta \end{pmatrix}}\\e_{\varphi }&=R\cos \theta \cdot {\begin{pmatrix}-\sin \varphi &\cos \varphi &0\end{pmatrix}}\\\end{aligned}}$

The related metric tensor has only diagonal elements (the squared vector lengths). This is an advantage of the coordinate system and not generally true.

${\begin{aligned}g_{RR}=1\qquad &g_{\theta \theta }=R^{2}\qquad &g_{\varphi \varphi }=R^{2}\cos ^{2}\theta \qquad &g_{ij}=0\quad \mathrm {else} \\g^{RR}=1\qquad &g^{\theta \theta }=1/R^{2}\qquad &g^{\varphi \varphi }=1/(R^{2}\cos ^{2}\theta )\qquad &g^{ij}=0\quad \mathrm {else} \\\end{aligned}}$

Now the necessary quantities can be calculated. Examples:

${\begin{aligned}e^{R}=e_{R}g^{RR}=1\cdot e_{R}&={\begin{pmatrix}\cos \theta \cos \varphi &\cos \theta \sin \varphi &\sin \theta \end{pmatrix}}\\{\Gamma ^{R}}_{\varphi \varphi }=e^{R}\cdot {\frac {\partial }{\partial \varphi }}e_{\varphi }&=e^{R}\cdot {\begin{pmatrix}-R\cos \theta \cos \varphi &-R\cos \theta \sin \varphi &0\end{pmatrix}}=-R\cos ^{2}\theta \\\end{aligned}}$

The resulting Christoffel symbols of the second kind ${\Gamma ^{k}}_{ji}=e^{k}\cdot {\frac {\partial e_{j}}{\partial x^{i}}}$ then are (organized by the "derivative" index i in a matrix):

${\begin{aligned}{\begin{pmatrix}{\Gamma ^{R}}_{RR}&{\Gamma ^{R}}_{\theta R}&{\Gamma ^{R}}_{\varphi R}\\{\Gamma ^{\theta }}_{RR}&{\Gamma ^{\theta }}_{\theta R}&{\Gamma ^{\theta }}_{\varphi R}\\{\Gamma ^{\varphi }}_{RR}&{\Gamma ^{\varphi }}_{\theta R}&{\Gamma ^{\varphi }}_{\varphi R}\\\end{pmatrix}}&=\quad {\begin{pmatrix}0&0&0\\0&1/R&0\\0&0&1/R\end{pmatrix}}\\{\begin{pmatrix}{\Gamma ^{R}}_{R\theta }&{\Gamma ^{R}}_{\theta \theta }&{\Gamma ^{R}}_{\varphi \theta }\\{\Gamma ^{\theta }}_{R\theta }&{\Gamma ^{\theta }}_{\theta \theta }&{\Gamma ^{\theta }}_{\varphi \theta }\\{\Gamma ^{\varphi }}_{R\theta }&{\Gamma ^{\varphi }}_{\theta \theta }&{\Gamma ^{\varphi }}_{\varphi \theta }\\\end{pmatrix}}\quad &={\begin{pmatrix}0&-R&0\\1/R&0&0\\0&0&-\tan \theta \end{pmatrix}}\\{\begin{pmatrix}{\Gamma ^{R}}_{R\varphi }&{\Gamma ^{R}}_{\theta \varphi }&{\Gamma ^{R}}_{\varphi \varphi }\\{\Gamma ^{\theta }}_{R\varphi }&{\Gamma ^{\theta }}_{\theta \varphi }&{\Gamma ^{\theta }}_{\varphi \varphi }\\{\Gamma ^{\varphi }}_{R\varphi }&{\Gamma ^{\varphi }}_{\theta \varphi }&{\Gamma ^{\varphi }}_{\varphi \varphi }\\\end{pmatrix}}&=\quad {\begin{pmatrix}0&0&-R\cos ^{2}\theta \\0&0&\cos \theta \sin \theta \\1/R&-\tan \theta &0\end{pmatrix}}\\\end{aligned}}$

These values show how the tangent directions (columns: $e_{R}$ , $e_{\theta }$ , $e_{\varphi }$ ) change, seen from an outside perspective (e.g. from space), but given in the tangent directions of the actual location (rows: R, θ, φ).

As an example, take the nonzero derivatives by θ in ${\Gamma ^{k}}_{j\ \theta }$ , which corresponds to a movement towards north (positive dθ):

- The new north direction $e_{\theta }$ changes by -R dθ in the up (R) direction. So the north direction will rotate downwards towards the center of the Earth.
- Similarly, the up direction $e_{R}$ will be adjusted towards the north. The different lengths of $e_{R}$ and $e_{\theta }$ lead to a factor of 1/R .
- Moving north, the east tangent vector $e_{\varphi }$ changes its length (-tan(θ) on the diagonal), it will shrink (-tan(θ) dθ < 0) on the northern hemisphere, and increase (-tan(θ) dθ > 0) on the southern hemisphere.

These effects are maybe not apparent during the movement, because they are the adjustments that keep the measurements in the coordinates R, θ, φ. Nevertheless, it can affect distances, physics equations, etc. So if e.g. you need the exact change of a magnetic field pointing approximately "south", it can be necessary to also correct your measurement by the change of the north direction using the Christoffel symbols to get the "true" (tensor) value.

The Christoffel symbols of the first kind ${\Gamma _{l}}_{ji}=g_{lk}{\Gamma ^{k}}_{ji}$ show the same change using metric-corrected coordinates, e.g. for derivative by φ:

${\begin{aligned}{\begin{pmatrix}{\Gamma _{R}}_{R\varphi }&{\Gamma _{R}}_{\theta \varphi }&{\Gamma _{R}}_{\varphi \varphi }\\{\Gamma _{\theta }}_{R\varphi }&{\Gamma _{\theta }}_{\theta \varphi }&{\Gamma _{\theta }}_{\varphi \varphi }\\{\Gamma _{\varphi }}_{R\varphi }&{\Gamma _{\varphi }}_{\theta \varphi }&{\Gamma _{\varphi }}_{\varphi \varphi }\\\end{pmatrix}}&=R\cos \theta {\begin{pmatrix}0&0&-\cos \theta \\0&0&R\sin \theta \\\cos \theta &-R\sin \theta &0\end{pmatrix}}\\\end{aligned}}$

**Lagrangian approach at finding a solution**

In cylindrical coordinates, Cartesian and cylindrical polar coordinates exist as:

${\textstyle {\begin{cases}x=r\cos \varphi \\y=r\sin \varphi \\z=h\end{cases}}}$ and ${\begin{cases}r={\sqrt {x^{2}+y^{2}}}\\\varphi =\arctan \left({\frac {y}{x}}\right)\\h=z\end{cases}}$

Cartesian points exist and Christoffel Symbols vanish as time passes, therefore, in cylindrical coordinates:

$\Gamma _{rr}^{r}=\Gamma _{\varphi r}^{r}={\frac {\partial ^{2}x}{\partial r^{2}}}{\frac {\partial r}{\partial x}}+{\frac {\partial ^{2}y}{\partial r^{2}}}{\frac {\partial r}{\partial y}}+{\frac {\partial ^{2}z}{\partial r^{2}}}{\frac {\partial r}{\partial z}}=0$

$\Gamma _{r\varphi }^{r}=\Gamma _{\varphi r}^{r}={\frac {\partial ^{2}x}{\partial r\partial \varphi }}{\frac {\partial r}{\partial x}}+{\frac {\partial ^{2}y}{\partial r\partial \varphi }}{\frac {\partial r}{\partial y}}+{\frac {\partial ^{2}z}{\partial r\partial \varphi }}{\frac {\partial r}{\partial z}}=-\sin \varphi \cos \varphi +\sin \varphi \cos \varphi =0$

$\Gamma _{\varphi \varphi }^{r}={\frac {\partial ^{2}x}{\partial \varphi ^{2}}}{\frac {\partial r}{\partial x}}+{\frac {\partial ^{2}y}{\partial \varphi ^{2}}}{\frac {\partial r}{\partial y}}+{\frac {\partial ^{2}z}{\partial \varphi ^{2}}}{\frac {\partial r}{\partial z}}=-{\frac {x}{r}}-{\frac {y}{r}}=-r$

$\Gamma _{rr}^{\varphi }=\Gamma _{\varphi r}^{\varphi }={\frac {\partial ^{2}x}{\partial r^{2}}}{\frac {\partial \varphi }{\partial x}}+{\frac {\partial ^{2}y}{\partial r^{2}}}{\frac {\partial \varphi }{\partial y}}+{\frac {\partial ^{2}z}{\partial r^{2}}}{\frac {\partial \varphi }{\partial z}}=0$

$\Gamma _{r\varphi }^{\varphi }=\Gamma _{\varphi r}^{\varphi }={\frac {\partial ^{2}x}{\partial r\partial \varphi }}{\frac {\partial \varphi }{\partial x}}+{\frac {\partial ^{2}y}{\partial r\partial \varphi }}{\frac {\partial \varphi }{\partial y}}+{\frac {\partial ^{2}z}{\partial r\partial \varphi }}{\frac {\partial \varphi }{\partial z}}=-{\frac {y}{r^{2}}}+\cos \varphi {\frac {x}{r^{2}}}={\frac {1}{r}}$

$\Gamma _{\varphi \varphi }^{\varphi }={\frac {\partial ^{2}x}{\partial \varphi ^{2}}}{\frac {\partial \varphi }{\partial x}}+{\frac {\partial ^{2}y}{\partial \varphi ^{2}}}{\frac {\partial \varphi }{\partial y}}+{\frac {\partial ^{2}z}{\partial \varphi ^{2}}}{\frac {\partial \varphi }{\partial z}}=-{\frac {x}{r^{2}}}-{\frac {y}{r^{2}}}=0$

**Spherical coordinates (using Lagrangian 2x2x2)**

$ds^{2}=d\theta ^{2}+\sin ^{2}\theta d\phi ^{2}$

The Lagrangian can be evaluated as:

$L={\dot {\theta }}^{2}+\sin ^{2}\theta {\dot {\phi }}^{2}$

Hence,

${\begin{cases}{\ddot {\phi }}+2{\frac {\cos \theta }{\sin \theta }}{\dot {\theta }}{\dot {\phi }}=0\\{\ddot {\theta }}-\sin \theta \cos \theta {\dot {\phi }}^{2}=0\\{\frac {d^{2}x^{k}}{d\lambda ^{2}}}+\Gamma _{ij}^{k}{\frac {dx^{i}}{d\lambda }}{\frac {dx^{j}}{d\lambda }}=0\\{\frac {\partial L}{\partial {\ddot {\theta }}}}=0\end{cases}}$ can be rearranged to ${\begin{cases}{\ddot {\phi }}+2{\frac {\cos \theta }{\sin \theta }}{\dot {\theta }}{\dot {\phi }}=0\\{\ddot {\theta }}-\sin \theta \cos \theta {\dot {\phi }}^{2}=0\end{cases}}$

By using the following geodesic equation:

${\frac {d^{2}x^{k}}{d\lambda ^{2}}}+\Gamma _{ij}^{k}{\frac {dx^{i}}{d\lambda }}{\frac {dx^{j}}{d\lambda }}=0$

The following can be obtained:

$\Gamma _{22}^{1}=-\sin \theta \cos \theta (\Gamma _{12}^{2})=\Gamma _{21}^{2}{\frac {\cos \theta }{\sin \theta }}$

## Lagrangian mechanics in geodesics (principles of least action in Christoffel symbols)

Incorporating Lagrangian mechanics and using the Euler–Lagrange equation, Christoffel symbols can be substituted into the Lagrangian to account for the geometry of the manifold. Christoffel symbols being calculated from the metric tensor, the equations can be derived and expressed from the principle of least action. When applying the Euler-Lagrange equation to a system of equations, the Lagrangian will include terms involving the Christoffel symbols, allowing the equation to act for the curvature which can determine the correct equations of motion for objects moving along geodesics.

### Using the principle of least action from the Euler-Lagrange equation

The Euler-Lagrange equation is applied to a functional related to the path of an object in a spherical coordinate system,

Given $L\in C^{2}(\mathbb {R} ^{3})$ and $y\in C^{1}[a,b]$ such that $y(a)=C$ and $ey(b)=d$

if

${\begin{cases}\int _{a}^{b}L(y(x))dx\\\int _{a}^{b}L(y'(x))dx\\\int _{a}^{b}L(x)dx\end{cases}}$

Reaches its minimum $min\equiv y_{0}\in C$ , where $y_{0}$  is a solution that can be found by solving the differential equation:

${\frac {d}{dx}}\left({\frac {\partial L}{\partial y'}}(y(x),y'(x))\right)-{\frac {\partial L}{\partial y}}(y(x),y'(x))=0$

The differential equation provides the mathematical conditions that must be satisfied for this optimal path.
