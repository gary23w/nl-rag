---
title: "Exterior derivative"
source: https://en.wikipedia.org/wiki/Exterior_derivative
domain: exterior-algebra
license: CC-BY-SA-4.0
tags: exterior algebra, differential form, wedge product, exterior derivative
fetched: 2026-07-02
---

# Exterior derivative

On a differentiable manifold, the **exterior derivative** extends the concept of the differential of a function to differential forms of higher degree. The exterior derivative was first described in its current form by Élie Cartan in 1899. The resulting calculus, known as exterior calculus, allows for a natural, metric-independent generalization of Stokes' theorem, Gauss's theorem, and Green's theorem from vector calculus.

If a differential k -form is thought of as measuring the flux through an infinitesimal k -parallelotope at each point of the manifold, then its exterior derivative can be thought of as measuring the net flux through the boundary of a $(k+1)$ -parallelotope at each point.

## Definition

The exterior derivative of a differential form of degree k (also differential k -form, or just k -form for brevity here) is a differential form of degree $k+1$ .

If f is a smooth function (a 0 -form), then the exterior derivative of f is the differential of f . That is, $df$ is the unique 1-form such that for every smooth vector field X , $df(X)=d_{X}f$ , where $d_{X}f$ is the directional derivative of f in the direction of X .

The exterior product of differential forms (denoted with the same symbol $\wedge$ ) is defined as their pointwise exterior product.

There are a variety of equivalent definitions of the exterior derivative of a general k -form.

### In terms of axioms

The exterior derivative d is defined to be the unique $\mathbb {R}$ -linear mapping from k -forms to $(k+1)$ -forms that has the following properties:

- The operator d applied to the 0 -form f is the differential $df$ of f
- If $\alpha$ and $\beta$ are two k -forms, then $d(a\alpha +b\beta )=ad\alpha +bd\beta$ for any field elements $a,b$
- If $\alpha$ is a k -form and $\beta$ is an $\ell$ -form, then $d(\alpha \wedge \beta )=d\alpha \wedge \beta +(-1)^{k}\alpha \wedge d\beta$ (*graded product rule*)
- If $\alpha$ is a k -form, then $d(d\alpha )=0$

If f and g are two 0 -forms (functions), then from the third property for the quantity $d(f\wedge g)$ , which is simply $d(fg)$ , the familiar product rule $d(fg)=g\,df+f\,dg$ is recovered. The third property can be generalised, for instance, if $\alpha$ is a k -form, $\beta$ is an $\ell$ -form and $\gamma$ is an m -form, then

$d(\alpha \wedge \beta \wedge \gamma )=d\alpha \wedge \beta \wedge \gamma +(-1)^{k}\alpha \wedge d\beta \wedge \gamma +(-1)^{k+\ell }\alpha \wedge \beta \wedge d\gamma .$

### In terms of local coordinates

Alternatively, one can work entirely in a local coordinate system $(x^{1},\ldots ,x^{n})$ . The coordinate differentials ${\text{d}}x^{1},\ldots ,{\text{d}}x^{n}$ form a basis of the space of one-forms, each associated with a coordinate. Given a multi-index $I=(i_{1},\ldots ,i_{k})$ with $1\leq i_{p}\leq n$ for $1\leq p\leq k$ (and denoting ${\text{d}}x^{i_{1}}\wedge \cdots \wedge {\text{d}}x^{i_{k}}$ with ${\text{d}}x^{I}$ ), the exterior derivative of a (simple) k -form $\varphi =g\,dx^{I}=g\,dx^{i_{1}}\wedge dx^{i_{2}}\wedge \cdots \wedge dx^{i_{k}}$ over $\mathbb {R} ^{n}$ is defined as $d{\varphi }=dg\wedge dx^{i_{1}}\wedge dx^{i_{2}}\wedge \cdots \wedge dx^{i_{k}}={\frac {\partial g}{\partial x^{j}}}\,dx^{j}\wedge \,dx^{i_{1}}\wedge dx^{i_{2}}\wedge \cdots \wedge dx^{i_{k}}$ (using the Einstein summation convention). The definition of the exterior derivative is extended linearly to a general k -form (which is expressible as a linear combination of basic simple k -forms) $\omega =f_{I}\,dx^{I},$ where each of the components of the multi-index I run over all the values in $\{1,\ldots ,n\}$ . Note that whenever j equals one of the components of the multi-index I then ${\text{d}}x^{j}\wedge {\text{d}}x^{I}=0$ (see *Exterior product*).

The definition of the exterior derivative in local coordinates follows from the preceding definition in terms of axioms. Indeed, with the k -form $\varphi$ as defined above, ${\begin{aligned}d{\varphi }&=d\left(g\,dx^{i_{1}}\wedge \cdots \wedge dx^{i_{k}}\right)\\&=dg\wedge \left(dx^{i_{1}}\wedge \cdots \wedge dx^{i_{k}}\right)+g\,d\left(dx^{i_{1}}\wedge \cdots \wedge dx^{i_{k}}\right)\\&=dg\wedge dx^{i_{1}}\wedge \cdots \wedge dx^{i_{k}}+g\sum _{p=1}^{k}(-1)^{p-1}\,dx^{i_{1}}\wedge \cdots \wedge dx^{i_{p-1}}\wedge d^{2}x^{i_{p}}\wedge dx^{i_{p+1}}\wedge \cdots \wedge dx^{i_{k}}\\&=dg\wedge dx^{i_{1}}\wedge \cdots \wedge dx^{i_{k}}\\&={\frac {\partial g}{\partial x^{i}}}\,dx^{i}\wedge dx^{i_{1}}\wedge \cdots \wedge dx^{i_{k}}\end{aligned}}$

Here, we have interpreted g as a 0 -form, and then applied the properties of the exterior derivative.

This result extends directly to the general k -form $\omega$ as $d\omega ={\frac {\partial f_{I}}{\partial x^{i}}}\,dx^{i}\wedge dx^{I}.$

In particular, for a 1 -form $\omega$ , the components of $d\omega$ in local coordinates are $(d\omega )_{ij}=\partial _{i}\omega _{j}-\partial _{j}\omega _{i}.$

*Caution*: There are two conventions regarding the meaning of $dx^{i_{1}}\wedge \cdots \wedge dx^{i_{k}}$ . Most current authors have the convention that $\left(dx^{i_{1}}\wedge \cdots \wedge dx^{i_{k}}\right)\left({\frac {\partial }{\partial x^{i_{1}}}},\ldots ,{\frac {\partial }{\partial x^{i_{k}}}}\right)=1.$ while in older texts like Kobayashi and Nomizu or Helgason $\left(dx^{i_{1}}\wedge \cdots \wedge dx^{i_{k}}\right)\left({\frac {\partial }{\partial x^{i_{1}}}},\ldots ,{\frac {\partial }{\partial x^{i_{k}}}}\right)={\frac {1}{k!}}.$

### In terms of invariant formula

Alternatively, an explicit formula can be given for the exterior derivative of a k -form $\omega$ , when paired with $k+1$ arbitrary smooth vector fields $V_{0},V_{1},\ldots ,V_{k}$ : $d\omega (V_{0},\ldots ,V_{k})=\sum _{i}(-1)^{i}V_{i}(\omega (V_{0},\ldots ,{\widehat {V}}_{i},\ldots ,V_{k}))+\sum _{i<j}(-1)^{i+j}\omega ([V_{i},V_{j}],V_{0},\ldots ,{\widehat {V}}_{i},\ldots ,{\widehat {V}}_{j},\ldots ,V_{k})$

where $[V_{i},V_{j}]$ denotes the Lie bracket and a hat denotes the omission of that element: $\omega (V_{0},\ldots ,{\widehat {V}}_{i},\ldots ,V_{k})=\omega (V_{0},\ldots ,V_{i-1},V_{i+1},\ldots ,V_{k}).$

In particular, when $\omega$ is a 1 -form, we have that $(d\omega )(X,Y)={\mathcal {L}}_{X}(\omega (Y))-{\mathcal {L}}_{Y}(\omega (X))-\omega ([X,Y])$ .

**Note:** With the conventions of e.g., Kobayashi–Nomizu and Helgason the formula differs by a factor of ${\textstyle {\frac {1}{k+1}}}$ : $d\omega (V_{0},\ldots ,V_{k})={\frac {1}{k+1}}\left(\sum _{i}(-1)^{i}V_{i}(\omega (V_{0},\ldots ,{\widehat {V}}_{i},\ldots ,V_{k}))+\sum _{i<j}(-1)^{i+j}\omega ([V_{i},V_{j}],V_{0},\ldots ,{\widehat {V}}_{i},\ldots ,{\widehat {V}}_{j},\ldots ,V_{k})\right).$

## Examples

### Example 1

Consider $\sigma =u\ {\text{d}}x^{1}\wedge {\text{d}}x^{2}$ over a 1 -form basis ${\text{d}}x^{1},\ldots ,{\text{d}}x^{n}$ for a scalar field u . The exterior derivative is: ${\begin{aligned}d\sigma &=du\wedge dx^{1}\wedge dx^{2}\\&=\left(\sum _{i=1}^{n}{\frac {\partial u}{\partial x^{i}}}\,dx^{i}\right)\wedge dx^{1}\wedge dx^{2}\\&=\sum _{i=3}^{n}\left({\frac {\partial u}{\partial x^{i}}}\,dx^{i}\wedge dx^{1}\wedge dx^{2}\right)\end{aligned}}$

The last formula, where summation starts at $i=3$ , follows easily from the properties of the exterior product. Namely, ${\text{d}}x^{i}\wedge {\text{d}}x^{i}=0$ .

### Example 2

Let $\sigma =u\ {\text{d}}x+v\ {\text{d}}y$ be a 1 -form defined over $\mathbb {R} ^{2}$ . By applying the above formula to each term (consider $x^{1}=x$ and $x^{2}=y$ ) we have the sum ${\begin{aligned}d\sigma &=\left(\sum _{i=1}^{2}{\frac {\partial u}{\partial x^{i}}}dx^{i}\wedge dx\right)+\left(\sum _{i=1}^{2}{\frac {\partial v}{\partial x^{i}}}\,dx^{i}\wedge dy\right)\\&=\left({\frac {\partial {u}}{\partial {x}}}\,dx\wedge dx+{\frac {\partial {u}}{\partial {y}}}\,dy\wedge dx\right)+\left({\frac {\partial {v}}{\partial {x}}}\,dx\wedge dy+{\frac {\partial {v}}{\partial {y}}}\,dy\wedge dy\right)\\&=0-{\frac {\partial {u}}{\partial {y}}}\,dx\wedge dy+{\frac {\partial {v}}{\partial {x}}}\,dx\wedge dy+0\\&=\left({\frac {\partial {v}}{\partial {x}}}-{\frac {\partial {u}}{\partial {y}}}\right)\,dx\wedge dy\end{aligned}}$

## Stokes' theorem on manifolds

If M is a compact smooth orientable n -dimensional manifold with boundary, and $\omega$ is an $(n-1)$ -form on M , then the generalized form of Stokes' theorem states that $\int _{M}d\omega =\int _{\partial {M}}\omega$

Intuitively, if one thinks of M as being divided into infinitesimal regions, and one adds the flux through the boundaries of all the regions, the interior boundaries all cancel out, leaving the total flux through the boundary of M .

## Further properties

### Closed and exact forms

A k -form $\omega$ is called *closed* if $d\omega =0$ ; closed forms are the kernel of d . $\omega$ is called *exact* if $\omega =d\alpha$ for some $(k-1)$ -form $\alpha$ ; exact forms are the image of d . Because $d^{2}=0$ , every exact form is closed. The Poincaré lemma states that in a contractible region, the converse is true.

### de Rham cohomology

Because the exterior derivative d has the property that $d^{2}=0$ , it can be used as the differential (coboundary) to define de Rham cohomology on a manifold. The k -th de Rham cohomology (group) is the vector space of closed k -forms modulo the exact k -forms; as noted in the previous section, the Poincaré lemma states that these vector spaces are trivial for a contractible region, for $k>0$ . For smooth manifolds, integration of forms gives a natural homomorphism from the de Rham cohomology to the singular cohomology over $\mathbb {R}$ . The theorem of de Rham shows that this map is actually an isomorphism, a far-reaching generalization of the Poincaré lemma. As suggested by the generalized Stokes' theorem, the exterior derivative is the "dual" of the boundary map on singular simplices.

### Naturality

The exterior derivative is natural in the technical sense: if $f:M\rightarrow N$ is a smooth map and $\Omega ^{k}$ is the contravariant smooth functor that assigns to each manifold the space of k -forms on the manifold, then the following diagram commutes

so $d(f^{*}\omega )=f^{*}d\omega$ , where $f^{*}$ denotes the pullback of f . This follows from that $f^{*}\omega (\cdot )$ , by definition, is $\omega (f_{*}(\cdot ))$ , $f_{*}$ being the pushforward of f . Thus d is a natural transformation from $\Omega ^{k}$ to $\Omega ^{k+1}$ .

## Exterior derivative in vector calculus

Most vector calculus operators are special cases of, or have close relationships to, the notion of exterior differentiation.

### Gradient

A smooth function $f:M\rightarrow \mathbb {R}$ on a real differentiable manifold M is a 0 -form. The exterior derivative of this 0 -form is the 1 -form $df$ .

When an inner product $\langle \cdot ,\cdot \rangle$ is defined, the gradient $\nabla f$ of a function f is defined as the unique vector in V such that its inner product with any element of V is the directional derivative of f along the vector, that is such that $\langle \nabla f,\cdot \rangle =df=\sum _{i=1}^{n}{\frac {\partial f}{\partial x^{i}}}\,dx^{i}.$

That is, $\nabla f=(df)^{\sharp }=\sum _{i=1}^{n}{\frac {\partial f}{\partial x^{i}}}\,\left(dx^{i}\right)^{\sharp },$ where $\sharp$ denotes the musical isomorphism $\sharp :V^{*}\rightarrow V$ mentioned earlier that is induced by the inner product.

The 1 -form $df$ is a section of the cotangent bundle, that gives a local linear approximation to f in the cotangent space at each point.

### Divergence

A vector field $V=(v_{1},v_{2},\ldots ,v_{n})$ on $\mathbb {R} ^{n}$ has a corresponding $(n-1)$ -form ${\begin{aligned}\omega _{V}&=v_{1}\left(dx^{2}\wedge \cdots \wedge dx^{n}\right)-v_{2}\left(dx^{1}\wedge dx^{3}\wedge \cdots \wedge dx^{n}\right)+\cdots +(-1)^{n-1}v_{n}\left(dx^{1}\wedge \cdots \wedge dx^{n-1}\right)\\&=\sum _{i=1}^{n}(-1)^{(i-1)}v_{i}\left(dx^{1}\wedge \cdots \wedge dx^{i-1}\wedge {\widehat {dx^{i}}}\wedge dx^{i+1}\wedge \cdots \wedge dx^{n}\right)\end{aligned}}$ where ${\widehat {dx^{i}}}$ denotes the omission of that element.

(For instance, when $n=3$ , i.e. in three-dimensional space, the 2 -form $\omega _{V}$ is locally the scalar triple product with V .) The integral of $\omega _{V}$ over a hypersurface is the flux of V over that hypersurface.

The exterior derivative of this $(n-1)$ -form is the n -form $d\omega _{V}=\operatorname {div} V\left(dx^{1}\wedge dx^{2}\wedge \cdots \wedge dx^{n}\right).$

### Curl

A vector field V on $\mathbb {R} ^{n}$ also has a corresponding 1 -form $\eta _{V}=v_{1}\,dx^{1}+v_{2}\,dx^{2}+\cdots +v_{n}\,dx^{n}.$

Locally, $\eta _{V}$ is the dot product with V . The integral of $\eta _{V}$ along a path is the work done against $-V$ along that path.

When $n=3$ , in three-dimensional space, the exterior derivative of the 1 -form $\eta _{V}$ is the 2 -form $d\eta _{V}=\omega _{\operatorname {curl} V}.$

### Invariant formulations of operators in vector calculus

The standard vector calculus operators can be generalized for any pseudo-Riemannian manifold, and written in coordinate-free notation as follows: ${\begin{array}{rcccl}\operatorname {grad} f&\equiv &\nabla f&=&\left(df\right)^{\sharp }\\\operatorname {div} F&\equiv &\nabla \cdot F&=&{\star d{\star }{\mathord {\left(F^{\flat }\right)}}}\\\operatorname {curl} F&\equiv &\nabla \times F&=&\left({\star }d{\mathord {\left(F^{\flat }\right)}}\right)^{\sharp }\\\Delta f&\equiv &\nabla ^{2}f&=&{\star }d{\star }df\\&&\nabla ^{2}F&=&\left(d{\star }d{\star }{\mathord {\left(F^{\flat }\right)}}-{\star }d{\star }d{\mathord {\left(F^{\flat }\right)}}\right)^{\sharp },\\\end{array}}$ where $\star$ is the Hodge star operator, $\flat$ and $\sharp$ are the musical isomorphisms, f is a scalar field and F is a vector field.

Note that the expression for $\operatorname {curl}$ requires $\sharp$ to act on $\star d(F^{\flat })$ , which is a form of degree $n-2$ . A natural generalization of $\sharp$ to k -forms of arbitrary degree allows this expression to make sense for any n .
