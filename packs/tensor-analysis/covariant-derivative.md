---
title: "Covariant derivative"
source: https://en.wikipedia.org/wiki/Covariant_derivative
domain: tensor-analysis
license: CC-BY-SA-4.0
tags: tensor calculus, covariant derivative, metric tensor, christoffel symbols
fetched: 2026-07-02
---

# Covariant derivative

In mathematics, the **covariant derivative** is a way of specifying a derivative along tangent vectors of a manifold. Alternatively, the covariant derivative is a way of introducing and working with a connection on a manifold by means of a differential operator, to be contrasted with the approach given by a principal connection on the frame bundle – see affine connection. In the special case of a manifold isometrically embedded into a higher-dimensional Euclidean space, the covariant derivative can be viewed as the orthogonal projection of the Euclidean directional derivative onto the manifold's tangent space. In this case the Euclidean derivative is broken into two parts, the extrinsic normal component (dependent on the embedding) and the intrinsic covariant derivative component.

The name is motivated by the importance of changes of coordinate in physics: the covariant derivative transforms covariantly under a general coordinate transformation, that is, linearly via the Jacobian matrix of the transformation.

This article presents an introduction to the covariant derivative of a vector field with respect to a vector field, both in a coordinate-free language and using a local coordinate system and the traditional index notation. The covariant derivative of a tensor field is presented as an extension of the same concept. The covariant derivative generalizes straightforwardly to a notion of differentiation associated to a connection on a vector bundle, also known as a **Koszul connection**.

## History

Historically, at the turn of the 20th century, the covariant derivative was introduced by Gregorio Ricci-Curbastro and Tullio Levi-Civita in the theory of Riemannian and pseudo-Riemannian geometry. Ricci and Levi-Civita (following ideas of Elwin Bruno Christoffel) observed that the Christoffel symbols used to define the curvature could also provide a notion of differentiation which generalized the classical directional derivative of vector fields on a manifold. This new derivative – the Levi-Civita connection – was *covariant* in the sense that it satisfied Riemann's requirement that objects in geometry should be independent of their description in a particular coordinate system.

It was soon noted by other mathematicians, prominent among these being Hermann Weyl, Jan Arnoldus Schouten, and Élie Cartan, that a covariant derivative could be defined abstractly without the presence of a metric. The crucial feature was not a particular dependence on the metric, but that the Christoffel symbols satisfied a certain precise second-order transformation law. This transformation law could serve as a starting point for defining the derivative in a covariant manner. Thus the theory of covariant differentiation forked off from the strictly Riemannian context to include a wider range of possible geometries.

In the 1940s, practitioners of differential geometry began introducing other notions of covariant differentiation in general vector bundles which were, in contrast to the classical bundles of interest to geometers, not part of the tensor analysis of the manifold. By and large, these generalized covariant derivatives had to be specified *ad hoc* by some version of the connection concept. In 1950, Jean-Louis Koszul unified these new ideas of covariant differentiation in a vector bundle by means of what is known today as a Koszul connection or a connection on a vector bundle. Using ideas from Lie algebra cohomology, Koszul successfully converted many of the analytic features of covariant differentiation into algebraic ones. In particular, Koszul connections eliminated the need for awkward manipulations of Christoffel symbols (and other analogous non-tensorial objects) in differential geometry. Thus they quickly supplanted the classical notion of covariant derivative in many post-1950 treatments of the subject.

## Motivation

The **covariant derivative** is a generalization of the directional derivative from vector calculus. As with the directional derivative, the covariant derivative is a rule, $\nabla _{\mathbf {u} }{\mathbf {v} }$ , which takes as its inputs: (1) a vector, **u**, defined at a point P, and (2) a vector field **v** defined in a neighborhood of P. The output is the vector $\nabla _{\mathbf {u} }{\mathbf {v} }(P)$ , also at the point P. The primary difference from the usual directional derivative is that $\nabla _{\mathbf {u} }{\mathbf {v} }$ must, in a certain precise sense, be *independent* of the manner in which it is expressed in a coordinate system.

A vector may be *described* as a list of numbers in terms of a basis, but as a geometrical object the vector retains its identity regardless of how it is described. For a geometric vector written in components with respect to one basis, when the basis is changed the components transform according to a change of basis formula, with the coordinates undergoing a covariant transformation. The covariant derivative is required to transform, under a change in coordinates, by a covariant transformation in the same way as a basis does (hence the name).

In the case of Euclidean space, one usually defines the directional derivative of a vector field in terms of the difference between two vectors at two nearby points. In such a system one translates one of the vectors to the origin of the other, keeping it parallel, then takes their difference within the same vector space. With a Cartesian (fixed orthonormal) coordinate system "keeping it parallel" amounts to keeping the components constant. This ordinary directional derivative on Euclidean space is the first example of a covariant derivative.

Next, one must take into account changes of the coordinate system. For example, if the Euclidean plane is described by polar coordinates, "keeping it parallel" does *not* amount to keeping the polar components constant under translation, since the coordinate grid itself "rotates". Thus, the same covariant derivative written in polar coordinates contains extra terms that describe how the coordinate grid itself rotates, or how in more general coordinates the grid expands, contracts, twists, interweaves, etc.

Consider the example of a particle moving along a curve *γ*(*t*) in the Euclidean plane. In polar coordinates, γ may be written in terms of its radial and angular coordinates by *γ*(*t*) = (*r*(*t*), *θ*(*t*)). A vector at a particular time t (for instance, a constant acceleration of the particle) is expressed in terms of $(\mathbf {e} _{r},\mathbf {e} _{\theta })$ , where $\mathbf {e} _{r}$ and $\mathbf {e} _{\theta }$ are unit tangent vectors for the polar coordinates, serving as a basis to decompose a vector in terms of radial and tangential components. At a slightly later time, the new basis in polar coordinates appears slightly rotated with respect to the first set. The covariant derivative of the basis vectors (the Christoffel symbols) serve to express this change.

In a curved space, such as the surface of the Earth (regarded as a sphere), the translation of tangent vectors between different points is not well defined, and its analog, parallel transport, depends on the path along which the vector is translated. A vector on a globe on the equator at point Q is directed to the north. Suppose we transport the vector (keeping it parallel) first along the equator to the point P, then drag it along a meridian to the N pole, and finally transport it along another meridian back to Q. Then we notice that the parallel-transported vector along a closed circuit does not return as the same vector; instead, it has another orientation. This would not happen in Euclidean space and is caused by the *curvature* of the surface of the globe. The same effect occurs if we drag the vector along an infinitesimally small closed surface subsequently along two directions and then back. This infinitesimal change of the vector is a measure of the curvature, and can be defined in terms of the covariant derivative.

### Remarks

- The definition of the covariant derivative does not use the metric in space. However, for each metric there is a unique torsion-free covariant derivative called the Levi-Civita connection such that the covariant derivative of the metric is zero.
- The properties of a derivative imply that $\nabla _{\mathbf {v} }\mathbf {u}$ depends on the values of u in a neighborhood of a point p in the same way as e.g. the derivative of a scalar function f along a curve at a given point p depends on the values of f in a neighborhood of p.
- The information in a neighborhood of a point p in the covariant derivative can be used to define parallel transport of a vector. Also the curvature, torsion, and geodesics may be defined only in terms of the covariant derivative or other related variation on the idea of a linear connection.
- Some equations involving covariant derivative can be locally solved using Chen's iterated integrals of using approach based on linear homotopy operator.

## Informal definition using an embedding into Euclidean space

Suppose an open subset U of a d-dimensional Riemannian manifold M is embedded into Euclidean space $(\mathbb {R} ^{n},\langle \cdot ,\cdot \rangle )$ via a twice continuously-differentiable (C2) mapping ${\vec {\Psi }}:\mathbb {R} ^{d}\supset U\to \mathbb {R} ^{n}$ such that the tangent space at ${\vec {\Psi }}(p)$ is spanned by the vectors $\left\{\left.{\frac {\partial {\vec {\Psi }}}{\partial x^{i}}}\right|_{p}:i\in \{1,\dots ,d\}\right\}$ and the scalar product $\left\langle \cdot ,\cdot \right\rangle$ on $\mathbb {R} ^{n}$ is compatible with the metric on M: $g_{ij}=\left\langle {\frac {\partial {\vec {\Psi }}}{\partial x^{i}}},{\frac {\partial {\vec {\Psi }}}{\partial x^{j}}}\right\rangle .$

(Since the manifold metric is always assumed to be regular, the compatibility condition implies linear independence of the partial derivative tangent vectors.)

For a tangent vector field, ${\vec {V}}=v^{j}{\frac {\partial {\vec {\Psi }}}{\partial x^{j}}}$ , one has ${\frac {\partial {\vec {V}}}{\partial x^{i}}}={\frac {\partial }{\partial x^{i}}}\left(v^{j}{\frac {\partial {\vec {\Psi }}}{\partial x^{j}}}\right)={\frac {\partial v^{j}}{\partial x^{i}}}{\frac {\partial {\vec {\Psi }}}{\partial x^{j}}}+v^{j}{\frac {\partial ^{2}{\vec {\Psi }}}{\partial x^{i}\,\partial x^{j}}}.$

The last term is not tangential to M, but can be expressed as a linear combination of the tangent space base vectors using the Christoffel symbols as linear factors plus a vector orthogonal to the tangent space: $v^{j}{\frac {\partial ^{2}{\vec {\Psi }}}{\partial x^{i}\,\partial x^{j}}}=v^{j}{\Gamma ^{k}}_{ij}{\frac {\partial {\vec {\Psi }}}{\partial x^{k}}}+{\vec {n}}.$

In the case of the Levi-Civita connection, the covariant derivative $\nabla _{\mathbf {e} _{i}}{\vec {V}}$ , also written $\nabla _{i}{\vec {V}}$ , is defined as the orthogonal projection of the usual derivative onto tangent space: $\nabla _{\mathbf {e} _{i}}{\vec {V}}:={\frac {\partial {\vec {V}}}{\partial x^{i}}}-{\vec {n}}=\left({\frac {\partial v^{k}}{\partial x^{i}}}+v^{j}{\Gamma ^{k}}_{ij}\right){\frac {\partial {\vec {\Psi }}}{\partial x^{k}}}.$

From here it may be computationally convenient to obtain a relation between the Christoffel symbols for the Levi-Civita connection and the metric. To do this we first note that, since the vector ${\vec {n}}$ in the previous equation is orthogonal to the tangent space, $\left\langle {\frac {\partial ^{2}{\vec {\Psi }}}{\partial x^{i}\,\partial x^{j}}},{\frac {\partial {\vec {\Psi }}}{\partial x^{l}}}\right\rangle =\left\langle {\Gamma ^{k}}_{ij}{\frac {\partial {\vec {\Psi }}}{\partial x^{k}}}+{\vec {n}},{\frac {\partial {\vec {\Psi }}}{\partial x^{l}}}\right\rangle =\left\langle {\frac {\partial {\vec {\Psi }}}{\partial x^{k}}},{\frac {\partial {\vec {\Psi }}}{\partial x^{l}}}\right\rangle {\Gamma ^{k}}_{ij}=g_{kl}\,{\Gamma ^{k}}_{ij}.$

Then, since the partial derivative of a component $g_{ab}$ of the metric with respect to a coordinate $x^{c}$ is ${\frac {\partial g_{ab}}{\partial x^{c}}}={\frac {\partial }{\partial x^{c}}}\left\langle {\frac {\partial {\vec {\Psi }}}{\partial x^{a}}},{\frac {\partial {\vec {\Psi }}}{\partial x^{b}}}\right\rangle =\left\langle {\frac {\partial ^{2}{\vec {\Psi }}}{\partial x^{c}\,\partial x^{a}}},{\frac {\partial {\vec {\Psi }}}{\partial x^{b}}}\right\rangle +\left\langle {\frac {\partial {\vec {\Psi }}}{\partial x^{a}}},{\frac {\partial ^{2}{\vec {\Psi }}}{\partial x^{c}\,\partial x^{b}}}\right\rangle ,$ any triplet *i*, *j*, *k* of indices yields a system of equations $\left\{{\begin{alignedat}{2}{\frac {\partial g_{jk}}{\partial x^{i}}}=&&\left\langle {\frac {\partial {\vec {\Psi }}}{\partial x^{j}}},{\frac {\partial ^{2}{\vec {\Psi }}}{\partial x^{k}\partial x^{i}}}\right\rangle &+\left\langle {\frac {\partial {\vec {\Psi }}}{\partial x^{k}}},{\frac {\partial ^{2}{\vec {\Psi }}}{\partial x^{i}\partial x^{j}}}\right\rangle \\{\frac {\partial g_{ki}}{\partial x^{j}}}=&\left\langle {\frac {\partial {\vec {\Psi }}}{\partial x^{i}}},{\frac {\partial ^{2}{\vec {\Psi }}}{\partial x^{j}\partial x^{k}}}\right\rangle &&+\left\langle {\frac {\partial {\vec {\Psi }}}{\partial x^{k}}},{\frac {\partial ^{2}{\vec {\Psi }}}{\partial x^{i}\partial x^{j}}}\right\rangle \\{\frac {\partial g_{ij}}{\partial x^{k}}}=&\left\langle {\frac {\partial {\vec {\Psi }}}{\partial x^{i}}},{\frac {\partial ^{2}{\vec {\Psi }}}{\partial x^{j}\partial x^{k}}}\right\rangle &+\left\langle {\frac {\partial {\vec {\Psi }}}{\partial x^{j}}},{\frac {\partial ^{2}{\vec {\Psi }}}{\partial x^{k}\partial x^{i}}}\right\rangle &&.\end{alignedat}}\right.$ (Here the symmetry of the scalar product has been used and the order of partial differentiations has been swapped.)

Adding the first two equations and subtracting the third, we obtain ${\frac {\partial g_{jk}}{\partial x^{i}}}+{\frac {\partial g_{ki}}{\partial x^{j}}}-{\frac {\partial g_{ij}}{\partial x^{k}}}=2\left\langle {\frac {\partial {\vec {\Psi }}}{\partial x^{k}}},{\frac {\partial ^{2}{\vec {\Psi }}}{\partial x^{i}\,\partial x^{j}}}\right\rangle .$

Thus the Christoffel symbols for the Levi-Civita connection are related to the metric by $g_{kl}{\Gamma ^{k}}_{ij}={\frac {1}{2}}\left({\frac {\partial g_{jl}}{\partial x^{i}}}+{\frac {\partial g_{li}}{\partial x^{j}}}-{\frac {\partial g_{ij}}{\partial x^{l}}}\right).$

If g is nondegenerate then ${\Gamma ^{k}}_{ij}$ can be solved for directly as ${\Gamma ^{k}}_{ij}={\frac {1}{2}}g^{kl}\left({\frac {\partial g_{jl}}{\partial x^{i}}}+{\frac {\partial g_{li}}{\partial x^{j}}}-{\frac {\partial g_{ij}}{\partial x^{l}}}\right).$

For a very simple example that captures the essence of the description above, draw a circle on a flat sheet of paper. Travel around the circle at a constant speed. The derivative of your velocity, your acceleration vector, always points radially inward. Roll this sheet of paper into a cylinder. Now the (Euclidean) derivative of your velocity has a component that sometimes points inward toward the axis of the cylinder depending on whether you're near a solstice or an equinox. (At the point of the circle when you are moving parallel to the axis, there is no inward acceleration. Conversely, at a point (1/4 of a circle later) when the velocity is along the cylinder's bend, the inward acceleration is maximum.) This is the (Euclidean) normal component. The covariant derivative component is the component parallel to the cylinder's surface, and is the same as that before you rolled the sheet into a cylinder.

## Formal definition

A covariant derivative is a (Koszul) connection on the tangent bundle and other tensor bundles: it differentiates vector fields in a way analogous to the usual differential on functions. The definition extends to a differentiation on the dual of vector fields (i.e. covector fields) and to arbitrary tensor fields, in a unique way that ensures compatibility with the tensor product and trace operations (tensor contraction).

### Functions

Given a point $p\in M$ of the manifold M, a real function $f:M\to \mathbb {R}$ on the manifold and a tangent vector $\mathbf {v} \in T_{p}M$ , the covariant derivative of f at p along **v** is the scalar at p, denoted $\left(\nabla _{\mathbf {v} }f\right)_{p}$ , that represents the principal part of the change in the value of f when the argument of f is changed by the infinitesimal displacement vector **v**. (This is the differential of f evaluated against the vector **v**.) Formally, there is a differentiable curve ${\displaystyle \phi$ such that $\phi (0)=p$ and $\phi '(0)=\mathbf {v}$ , and the covariant derivative of f at p is defined by $\left(\nabla _{\mathbf {v} }f\right)_{p}=\left(f\circ \phi \right)^{\prime }\left(0\right)=\lim _{t\to 0}{\frac {f(\phi \left(t\right))-f(p)}{t}}.$

When $\mathbf {v} :M\to T_{p}M$ is a vector field on M, the covariant derivative $\nabla _{\mathbf {v} }f:M\to \mathbb {R}$ is the function that associates with each point p in the common domain of f and **v** the scalar $\left(\nabla _{\mathbf {v} }f\right)_{p}$ .

For a scalar function f and vector field **v**, the covariant derivative $\nabla _{\mathbf {v} }f$ coincides with the Lie derivative $L_{\mathbf {v} }(f)$ , and with the exterior derivative $df(\mathbf {v} )$ .

### Vector fields

Given a point p of the manifold M, a vector field $\mathbf {u} :M\to T_{p}M$ defined in a neighborhood of p and a tangent vector $\mathbf {v} \in T_{p}M$ , the covariant derivative of **u** at p along **v** is the tangent vector at p, denoted $(\nabla _{\mathbf {v} }\mathbf {u} )_{p}$ , such that the following properties hold (for any tangent vectors **v**, **x** and **y** at p, vector fields **u** and **w** defined in a neighborhood of p, scalar values g and h at p, and scalar function f defined in a neighborhood of p):

1. $\left(\nabla _{\mathbf {v} }\mathbf {u} \right)_{p}$ is linear in $\mathbf {v}$ so $\left(\nabla _{g\mathbf {x} +h\mathbf {y} }\mathbf {u} \right)_{p}=g(p)\left(\nabla _{\mathbf {x} }\mathbf {u} \right)_{p}+h(p)\left(\nabla _{\mathbf {y} }\mathbf {u} \right)_{p}$
2. $\left(\nabla _{\mathbf {v} }\mathbf {u} \right)_{p}$ is additive in $\mathbf {u}$ so: $\left(\nabla _{\mathbf {v} }\left[\mathbf {u} +\mathbf {w} \right]\right)_{p}=\left(\nabla _{\mathbf {v} }\mathbf {u} \right)_{p}+\left(\nabla _{\mathbf {v} }\mathbf {w} \right)_{p}$
3. $(\nabla _{\mathbf {v} }\mathbf {u} )_{p}$ obeys the product rule; i.e., where $\nabla _{\mathbf {v} }f$ is defined above, $\left(\nabla _{\mathbf {v} }\left[f\mathbf {u} \right]\right)_{p}=f(p)\left(\nabla _{\mathbf {v} }\mathbf {u} )_{p}+(\nabla _{\mathbf {v} }f\right)_{p}\mathbf {u} _{p}.$

Note that $\left(\nabla _{\mathbf {v} }\mathbf {u} \right)_{p}$ depends not only on the value of **u** at p but also on values of **u** in a neighborhood of p, because the last property, the product rule, involves the directional derivative of f (by the vector **v**).

If **u** and **v** are both vector fields defined over a common domain, then $\nabla _{\mathbf {v} }\mathbf {u}$ denotes the vector field whose value at each point p of the domain is the tangent vector $\left(\nabla _{\mathbf {v} }\mathbf {u} \right)_{p}$ .

### Covector fields

Given a field of covectors (or one-form) $\alpha$ defined in a neighborhood of p, its covariant derivative $(\nabla _{\mathbf {v} }\alpha )_{p}$ is defined in a way to make the resulting operation compatible with tensor contraction and the product rule. That is, $(\nabla _{\mathbf {v} }\alpha )_{p}$ is defined as the unique one-form at p such that the following identity is satisfied for all vector fields **u** in a neighborhood of p $\left(\nabla _{\mathbf {v} }\alpha \right)_{p}\left(\mathbf {u} _{p}\right)=\nabla _{\mathbf {v} }\left[\alpha \left(\mathbf {u} \right)\right]_{p}-\alpha _{p}\left[\left(\nabla _{\mathbf {v} }\mathbf {u} \right)_{p}\right].$

The covariant derivative of a covector field along a vector field **v** is again a covector field.

### Tensor fields

Once the covariant derivative is defined for fields of vectors and covectors it can be defined for arbitrary tensor fields by imposing the following identities for every pair of tensor fields $\varphi$ and $\psi$ in a neighborhood of the point p: $\nabla _{\mathbf {v} }\left(\varphi \otimes \psi \right)_{p}=\left(\nabla _{\mathbf {v} }\varphi \right)_{p}\otimes \psi (p)+\varphi (p)\otimes \left(\nabla _{\mathbf {v} }\psi \right)_{p},$ and for $\varphi$ and $\psi$ of the same valence $\nabla _{\mathbf {v} }(\varphi +\psi )_{p}=(\nabla _{\mathbf {v} }\varphi )_{p}+(\nabla _{\mathbf {v} }\psi )_{p}.$ The covariant derivative of a tensor field along a vector field **v** is again a tensor field of the same type.

Explicitly, let T be a tensor field of type (*p*, *q*). Consider T to be a differentiable multilinear map of smooth sections *α*1, *α*2, ..., *α**q* of the cotangent bundle *T*∗*M* and of sections *X*1, *X*2, ..., *X**p* of the tangent bundle *TM*, written *T*(*α*1, *α*2, ..., *X*1, *X*2, ...) into **R**. The covariant derivative of T along Y is given by the formula ${\begin{aligned}(\nabla _{Y}T)\left(\alpha _{1},\alpha _{2},\ldots ,X_{1},X_{2},\ldots \right)=&{}\nabla _{Y}\left(T\left(\alpha _{1},\alpha _{2},\ldots ,X_{1},X_{2},\ldots \right)\right)\\&{}-T\left(\nabla _{Y}\alpha _{1},\alpha _{2},\ldots ,X_{1},X_{2},\ldots \right)-T\left(\alpha _{1},\nabla _{Y}\alpha _{2},\ldots ,X_{1},X_{2},\ldots \right)-\cdots \\&{}-T\left(\alpha _{1},\alpha _{2},\ldots ,\nabla _{Y}X_{1},X_{2},\ldots \right)-T\left(\alpha _{1},\alpha _{2},\ldots ,X_{1},\nabla _{Y}X_{2},\ldots \right)-\cdots \end{aligned}}$

## Coordinate description

Given coordinate functions $x^{i},\ i=0,1,2,\dots ,$ any tangent vector can be described by its components in the basis $\mathbf {e} _{i}={\frac {\partial }{\partial x^{i}}}.$

The covariant derivative of a basis vector along a basis vector is again a vector and so can be expressed as a linear combination $\Gamma ^{k}\mathbf {e} _{k}$ . To specify the covariant derivative it is enough to specify the covariant derivative of each basis vector field $\mathbf {e} _{i}$ along $\mathbf {e} _{j}$ . $\nabla _{\mathbf {e} _{j}}\mathbf {e} _{i}={\Gamma ^{k}}_{ij}\mathbf {e} _{k},$

the coefficients $\Gamma ^{k}{}_{ij}$ are the components of the connection with respect to a system of local coordinates. In the theory of Riemannian and pseudo-Riemannian manifolds, the components of the Levi-Civita connection with respect to a system of local coordinates are called Christoffel symbols.

Then using the rules in the definition, we find that for general vector fields $\mathbf {v} =v^{j}\mathbf {e} _{j}$ and $\mathbf {u} =u^{i}\mathbf {e} _{i}$ we get ${\begin{aligned}\nabla _{\mathbf {v} }\mathbf {u} &=\nabla _{v^{j}\mathbf {e} _{j}}u^{i}\mathbf {e} _{i}\\&=v^{j}\nabla _{\mathbf {e} _{j}}u^{i}\mathbf {e} _{i}\\&=v^{j}u^{i}\nabla _{\mathbf {e} _{j}}\mathbf {e} _{i}+v^{j}\mathbf {e} _{i}\nabla _{\mathbf {e} _{j}}u^{i}\\&=v^{j}u^{i}{\Gamma ^{k}}_{ij}\mathbf {e} _{k}+v^{j}{\partial u^{i} \over \partial x^{j}}\mathbf {e} _{i}\end{aligned}}$ so $\nabla _{\mathbf {v} }\mathbf {u} =\left(v^{j}u^{i}{\Gamma ^{k}}_{ij}+v^{j}{\partial u^{k} \over \partial x^{j}}\right)\mathbf {e} _{k}.$

The first term in this formula is responsible for "twisting" the coordinate system with respect to the covariant derivative and the second for changes of components of the vector field $\mathbf {u}$ . In particular $\nabla _{\mathbf {e} _{j}}\mathbf {u} =\nabla _{j}\mathbf {u} =\left({\frac {\partial u^{i}}{\partial x^{j}}}+u^{k}{\Gamma ^{i}}_{kj}\right)\mathbf {e} _{i}$

In words: the covariant derivative is the usual derivative along the coordinates with correction terms which tell how the coordinates change.

For covectors similarly we have $\nabla _{\mathbf {e} _{j}}{\mathbf {\theta } }=\left({\frac {\partial \theta _{i}}{\partial x^{j}}}-\theta _{k}{\Gamma ^{k}}_{ij}\right){\mathbf {e} ^{*}}^{i},$ where ${\mathbf {e} ^{*}}^{i}(\mathbf {e} _{j})={\delta ^{i}}_{j}$ .

The covariant derivative of a type (*r*, *s*) tensor field along $e_{c}$ is given by the expression:

${\begin{aligned}{(\nabla _{e_{c}}T)^{a_{1}\ldots a_{r}}}_{b_{1}\ldots b_{s}}={}&{\frac {\partial }{\partial x^{c}}}{T^{a_{1}\ldots a_{r}}}_{b_{1}\ldots b_{s}}\\&+\,{\Gamma ^{a_{1}}}_{dc}{T^{da_{2}\ldots a_{r}}}_{b_{1}\ldots b_{s}}+\cdots +{\Gamma ^{a_{r}}}_{dc}{T^{a_{1}\ldots a_{r-1}d}}_{b_{1}\ldots b_{s}}\\&-\,{\Gamma ^{d}}_{b_{1}c}{T^{a_{1}\ldots a_{r}}}_{db_{2}\ldots b_{s}}-\cdots -{\Gamma ^{d}}_{b_{s}c}{T^{a_{1}\ldots a_{r}}}_{b_{1}\ldots b_{s-1}d}.\end{aligned}}$ Or, in words: take the partial derivative of the tensor and add: $+{\Gamma ^{a_{i}}}_{dc}$ for every upper index $a_{i}$ , and $-{\Gamma ^{d}}_{b_{i}c}$ for every lower index $b_{i}$ .

If instead of a tensor, one is trying to differentiate a *tensor density* (of weight +1), then one also adds a term $-{\Gamma ^{d}}_{dc}{T^{a_{1}\ldots a_{r}}}_{b_{1}\ldots b_{s}}.$ If it is a tensor density of weight W, then multiply that term by W. For example, ${\textstyle {\sqrt {-g}}}$ is a scalar density (of weight +1), so we get: $\left({\sqrt {-g}}\right)_{;c}=\left({\sqrt {-g}}\right)_{,c}-{\sqrt {-g}}\,{\Gamma ^{d}}_{dc}$ where the semicolon ";" indicates covariant differentiation and the comma "," indicates partial differentiation. Incidentally, this particular expression is equal to zero, because the covariant derivative of a function solely of the metric is always zero.

## Notation

In textbooks on physics, the covariant derivative is sometimes stated in terms of its components in this equation.

Often a notation is used in which the covariant derivative is given with a semicolon, while a normal partial derivative is indicated by a comma. In this notation we write the same as: $\nabla _{e_{j}}\mathbf {v} \ {\stackrel {\mathrm {def} }{=}}\ {v^{s}}_{;j}\mathbf {e} _{s}\;\;\;\;\;\;{v^{i}}_{;j}={v^{i}}_{,j}+v^{k}{\Gamma ^{i}}_{kj}$ In case two or more indexes appear after the semicolon, all of them must be understood as covariant derivatives: $\nabla _{e_{k}}\left(\nabla _{e_{j}}\mathbf {v} \right)\ {\stackrel {\mathrm {def} }{=}}\ {v^{s}}_{;jk}\mathbf {e} _{s}$

In some older texts (notably Adler, Bazin & Schiffer, *Introduction to General Relativity*), the covariant derivative is denoted by a double pipe and the partial derivative by single pipe: $\nabla _{e_{j}}\mathbf {v} \ {\stackrel {\mathrm {def} }{=}}\ {v^{i}}_{||j}={v^{i}}_{|j}+v^{k}{\Gamma ^{i}}_{kj}$

## Covariant derivative by field type

For a scalar field $\phi \,$ , covariant differentiation is simply partial differentiation: $\phi _{;a}\equiv \partial _{a}\phi$

For a contravariant vector field $\lambda ^{a}$ , we have: ${\lambda ^{a}}_{;b}\equiv \partial _{b}\lambda ^{a}+{\Gamma ^{a}}_{bc}\lambda ^{c}$

For a covariant vector field $\lambda _{a}$ , we have: $\lambda _{a;c}\equiv \partial _{c}\lambda _{a}-{\Gamma ^{b}}_{ca}\lambda _{b}$

For a type (2,0) tensor field $\tau ^{ab}$ , we have: ${\tau ^{ab}}_{;c}\equiv \partial _{c}\tau ^{ab}+{\Gamma ^{a}}_{cd}\tau ^{db}+{\Gamma ^{b}}_{cd}\tau ^{ad}$

For a type (0,2) tensor field $\tau _{ab}$ , we have: $\tau _{ab;c}\equiv \partial _{c}\tau _{ab}-{\Gamma ^{d}}_{ca}\tau _{db}-{\Gamma ^{d}}_{cb}\tau _{ad}$

For a type (1,1) tensor field ${\tau ^{a}}_{b}$ , we have: ${\tau ^{a}}_{b;c}\equiv \partial _{c}{\tau ^{a}}_{b}+{\Gamma ^{a}}_{cd}{\tau ^{d}}_{b}-{\Gamma ^{d}}_{cb}{\tau ^{a}}_{d}$

The notation above is meant in the sense ${\tau ^{ab}}_{;c}\equiv \left(\nabla _{\mathbf {e} _{c}}\tau \right)^{ab}$

## Properties

In general, covariant derivatives do not commute. By example, the covariant derivatives of vector field $\lambda _{a;bc}\neq \lambda _{a;cb}$ . The Riemann tensor ${R^{d}}_{abc}$ is defined such that: $\lambda _{a;bc}-\lambda _{a;cb}={R^{d}}_{abc}\lambda _{d}$ or, equivalently, ${\lambda ^{a}}_{;bc}-{\lambda ^{a}}_{;cb}=-{R^{a}}_{dbc}\lambda ^{d}$

The covariant derivative of a (2,0)-tensor field fulfills: ${\tau ^{ab}}_{;cd}-{\tau ^{ab}}_{;dc}=-{R^{a}}_{ecd}\tau ^{eb}-{R^{b}}_{ecd}\tau ^{ae}$

The latter can be shown by taking (without loss of generality) that $\tau ^{ab}=\lambda ^{a}\mu ^{b}$ .

## Derivative along a curve

Since the covariant derivative $\nabla _{X}T$ of a tensor field T at a point p depends only on the value of the vector field X at p one can define the covariant derivative along a smooth curve $\gamma (t)$ in a manifold: $D_{t}T=\nabla _{{\dot {\gamma }}(t)}T.$ Note that the tensor field T only needs to be defined on the curve $\gamma (t)$ for this definition to make sense.

In particular, ${\dot {\gamma }}(t)$ is a vector field along the curve $\gamma$ itself. If $\nabla _{{\dot {\gamma }}(t)}{\dot {\gamma }}(t)$ vanishes then the curve is called a geodesic of the covariant derivative. If the covariant derivative is the Levi-Civita connection of a positive-definite metric then the geodesics for the connection are precisely the geodesics of the metric that are parametrized by arc length.

The derivative along a curve is also used to define the parallel transport along the curve.

Sometimes the covariant derivative along a curve is called **absolute** or **intrinsic derivative**.

## Relation to Lie derivative

A covariant derivative introduces an extra geometric structure on a manifold that allows vectors in neighboring tangent spaces to be compared: there is no canonical way to compare vectors from different tangent spaces because there is no canonical coordinate system.

There is however another generalization of directional derivatives which *is* canonical: the Lie derivative, which evaluates the change of one vector field along the flow of another vector field. Thus, one must know both vector fields in a neighborhood, not merely at a single point. The covariant derivative on the other hand introduces its own change for vectors in a given direction, and it only depends on the vector direction at a single point, rather than a vector field in a neighborhood of a point. In other words, the covariant derivative is linear (over *C*∞(*M*)) in the direction argument, while the Lie derivative is linear in neither argument.

Note that the antisymmetrized covariant derivative ∇*u**v* − ∇*v**u*, and the Lie derivative *L**u**v* differ by the torsion of the connection, so that if a connection is torsion free, then its antisymmetrization *is* the Lie derivative.
