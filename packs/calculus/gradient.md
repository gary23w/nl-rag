---
title: "Gradient"
source: https://en.wikipedia.org/wiki/Gradient
domain: calculus
license: CC-BY-SA-4.0
tags: calculus, differential calculus, integral calculus, differentiation, antiderivative
fetched: 2026-07-02
---

# Gradient

In vector calculus, the **gradient** of a scalar-valued differentiable function f of several variables is the vector field (or vector-valued function) $\nabla f$ whose value at a point p gives the direction and the rate of fastest increase. The gradient transforms like a vector under change of basis of the space of variables of f . If the gradient of a function is non-zero at a point p , the direction of the gradient is the direction in which the function increases most quickly from p , and the magnitude of the gradient is the rate of increase in that direction, the greatest absolute directional derivative. Further, a point where the gradient is the zero vector is known as a stationary point. The gradient thus plays a fundamental role in optimization theory, machine learning, and artificial intelligence, where it is used to minimize a function by gradient descent. In coordinate-free terms, the gradient of a function $f(\mathbf {r} )$ may be defined by:

$df=\nabla f\cdot d\mathbf {r}$

where $df$ is the total infinitesimal change in f for an infinitesimal displacement $d\mathbf {r}$ , and is seen to be maximal when $d\mathbf {r}$ is in the direction of the gradient $\nabla f$ . The nabla symbol $\nabla$ , written as an upside-down triangle and pronounced "del", denotes the vector differential operator.

When a coordinate system is used in which the basis vectors are not functions of position, the gradient is given by the vector whose components are the partial derivatives of f at p . That is, for $f\colon \mathbb {R} ^{n}\to \mathbb {R}$ , its gradient $\nabla f\colon \mathbb {R} ^{n}\to \mathbb {R} ^{n}$ is defined at the point $p=(x_{1},\ldots ,x_{n})$ in *n*-dimensional space as the vector

$\nabla f(p)={\begin{bmatrix}{\frac {\partial f}{\partial x_{1}}}(p)\\\vdots \\{\frac {\partial f}{\partial x_{n}}}(p)\end{bmatrix}}$ .

Note that the above definition for gradient is defined for the function f only if f is differentiable at p . There can be functions for which partial derivatives exist in every direction but fail to be differentiable. Furthermore, this definition as the vector of partial derivatives is only valid when the basis of the coordinate system is orthonormal. For any other basis, the metric tensor at that point needs to be taken into account.

For example, the function $f(x,y)={\frac {x^{2}y}{x^{2}+y^{2}}}$ unless at origin where $f(0,0)=0$ , is not differentiable at the origin as it does not have a well defined tangent plane despite having well defined partial derivatives in every direction at the origin. In this particular example, under rotation of x-y coordinate system, the above formula for gradient fails to transform like a vector (gradient becomes dependent on choice of basis for coordinate system) and also fails to point towards the 'steepest ascent' in some orientations. For differentiable functions where the formula for gradient holds, it can be shown to always transform as a vector under transformation of the basis so as to always point towards the fastest increase.

The gradient is dual to the total derivative $df$ : the value of the gradient at a point is a tangent vector – a vector at each point; while the value of the derivative at a point is a *co*tangent vector – a linear functional on vectors. They are related in that the dot product of the gradient of f at a point p with another tangent vector $\mathbf {v}$ equals the directional derivative of f at p of the function along $\mathbf {v}$ ; that is, ${\textstyle \nabla f(p)\cdot \mathbf {v} ={\frac {\partial f}{\partial \mathbf {v} }}(p)=df_{p}(\mathbf {v} )}$ . The gradient admits multiple generalizations to more general functions on manifolds; see § Generalizations.

## Motivation

Consider a room where the temperature is given by a scalar field, *T*, so at each point (*x*, *y*, *z*) the temperature is *T*(*x*, *y*, *z*), independent of time. At each point in the room, the gradient of *T* at that point will show the direction in which the temperature rises most quickly, moving away from (*x*, *y*, *z*). The magnitude of the gradient will determine how fast the temperature rises in that direction.

Consider a surface whose height above sea level at point (*x*, *y*) is *H*(*x*, *y*). The gradient of *H* at a point is a plane vector pointing in the direction of the steepest slope or grade at that point. The steepness of the slope at that point is given by the magnitude of the gradient vector.

The gradient can also be used to measure how a scalar field changes in other directions, rather than just the direction of greatest change, by taking a dot product. Suppose that the steepest slope on a hill is 40%. A road going directly uphill has slope 40%, but a road going around the hill at an angle will have a shallower slope. For example, if the road is at a 60° angle from the uphill direction (when both directions are projected onto the horizontal plane), then the slope along the road will be the dot product between the gradient vector and a unit vector along the road, as the dot product measures how much the unit vector along the road aligns with the steepest slope, which is 40% times the cosine of 60°, or 20%.

More generally, if the hill height function *H* is differentiable, then the gradient of *H* dotted with a unit vector gives the slope of the hill in the direction of the vector, the directional derivative of *H* along the unit vector.

## Notation

The gradient of a function f at point a is usually written as $\nabla f(a)$ . It may also be denoted by any of the following:

- ${\vec {\nabla }}f(a)$  : to emphasize the vector nature of the result.
- $\operatorname {grad} f$
- $\partial _{i}f$ and $f_{i}$  : Written with Einstein notation, where repeated indices (i) are summed over.

## Definition

The gradient (or gradient vector field) of a scalar function *f*(*x*1, *x*2, *x*3, …, *xn*) is denoted ∇*f* or ∇→*f* where ∇ (nabla) denotes the vector differential operator, del. The notation grad *f* is also commonly used to represent the gradient. The gradient of *f* is defined as the unique vector field whose dot product with any vector **v** at each point *x* is the directional derivative of *f* along **v**. That is,

${\big (}\nabla f(x){\big )}\cdot {\hat {\mathbf {v} }}=D_{\mathbf {v} }f(x)$

where the right-hand side is the directional derivative and there are many ways to represent it. Formally, the derivative is *dual* to the gradient; see relationship with derivative.

When a function also depends on a parameter such as time, the gradient often refers simply to the vector of its spatial derivatives only (see Spatial gradient).

The magnitude and direction of the gradient vector are independent of the particular coordinate representation.

### Cartesian coordinates

In the three-dimensional Cartesian coordinate system with a Euclidean metric, the gradient, if it exists, is given by

$\nabla f={\frac {\partial f}{\partial x}}\mathbf {i} +{\frac {\partial f}{\partial y}}\mathbf {j} +{\frac {\partial f}{\partial z}}\mathbf {k} ,$

where **i**, **j**, **k** are the standard unit vectors in the directions of the *x*, *y* and *z* coordinates, respectively.

For example, the gradient of the function $f(x,y,z)=2x+3y^{2}-\sin(z)$ is $\nabla f(x,y,z)=2\mathbf {i} +6y\mathbf {j} -\cos(z)\mathbf {k} .$ or $\nabla f(x,y,z)={\begin{bmatrix}2\\6y\\-\cos z\end{bmatrix}}.$

In some applications it is customary to represent the gradient as a row vector or column vector of its components in a rectangular coordinate system; this article follows the convention of the gradient being a column vector, while the derivative is a row vector.

### Cylindrical and spherical coordinates

In cylindrical coordinates, the gradient is given by:

$\nabla f(\rho ,\varphi ,z)={\frac {\partial f}{\partial \rho }}\mathbf {e} _{\rho }+{\frac {1}{\rho }}{\frac {\partial f}{\partial \varphi }}\mathbf {e} _{\varphi }+{\frac {\partial f}{\partial z}}\mathbf {e} _{z},$

where *ρ* is the axial distance, *φ* is the azimuthal or azimuth angle, *z* is the axial coordinate, and **e***ρ*, **e***φ* and **e***z* are unit vectors pointing along the coordinate directions.

In spherical coordinates with a Euclidean metric, the gradient is given by:

$\nabla f(r,\theta ,\varphi )={\frac {\partial f}{\partial r}}\mathbf {e} _{r}+{\frac {1}{r}}{\frac {\partial f}{\partial \theta }}\mathbf {e} _{\theta }+{\frac {1}{r\sin \theta }}{\frac {\partial f}{\partial \varphi }}\mathbf {e} _{\varphi },$

where *r* is the radial distance, *φ* is the azimuthal angle and *θ* is the polar angle, and **e***r*, **e***θ* and **e***φ* are again local unit vectors pointing in the coordinate directions (that is, the normalized covariant basis).

For the gradient in other orthogonal coordinate systems, see Orthogonal coordinates (Differential operators in three dimensions).

### General coordinates

We consider general coordinates, which we write as *x*1, …, *x**i*, …, *x**n*, where n is the number of dimensions of the domain. Here, the upper index refers to the position in the list of the coordinate or component, so *x*2 refers to the second component—not the quantity *x* squared. The index variable *i* refers to an arbitrary element *x**i*. Using Einstein notation, the gradient can then be written as:

$\nabla f={\frac {\partial f}{\partial x^{i}}}g^{ij}\mathbf {e} _{j}$ (Note that its dual is ${\textstyle \mathrm {d} f={\frac {\partial f}{\partial x^{i}}}\mathbf {e} ^{i}}$ ),

where $\mathbf {e} ^{i}=\mathrm {d} x^{i}$ and $\mathbf {e} _{i}=\partial \mathbf {x} /\partial x^{i}$ refer to the unnormalized local covariant and contravariant bases respectively, $g^{ij}$ is the inverse metric tensor, and the Einstein summation convention implies summation over *i* and *j*.

If the coordinates are orthogonal we can easily express the gradient (and the differential) in terms of the normalized bases, which we refer to as ${\hat {\mathbf {e} }}_{i}$ and ${\hat {\mathbf {e} }}^{i}$ , using the scale factors (also known as Lamé coefficients) $h_{i}=\lVert \mathbf {e} _{i}\rVert ={\sqrt {g_{ii}}}=1\,/\lVert \mathbf {e} ^{i}\rVert$  :

$\nabla f={\frac {\partial f}{\partial x^{i}}}g^{ij}{\hat {\mathbf {e} }}_{j}{\sqrt {g_{jj}}}=\sum _{i=1}^{n}\,{\frac {\partial f}{\partial x^{i}}}{\frac {1}{h_{i}}}\mathbf {\hat {e}} _{i}$ (and ${\textstyle \mathrm {d} f=\sum _{i=1}^{n}\,{\frac {\partial f}{\partial x^{i}}}{\frac {1}{h_{i}}}\mathbf {\hat {e}} ^{i}}$ ),

where we cannot use Einstein notation, since it is impossible to avoid the repetition of more than two indices. Despite the use of upper and lower indices, $\mathbf {\hat {e}} _{i}$ , $\mathbf {\hat {e}} ^{i}$ , and $h_{i}$ are neither contravariant nor covariant.

The latter expression evaluates to the expressions given above for cylindrical and spherical coordinates.

## Relationship with derivative

### Relationship with total derivative

The gradient is closely related to the total derivative (total differential) $df$ : they are transpose (dual) to each other. Using the convention that vectors in $\mathbb {R} ^{n}$ are represented by column vectors, and that covectors (linear maps $\mathbb {R} ^{n}\to \mathbb {R}$ ) are represented by row vectors, the gradient $\nabla f$ and the derivative $df$ are expressed as a column and row vector, respectively, with the same components, but transpose of each other:

$\nabla f(p)={\begin{bmatrix}{\frac {\partial f}{\partial x_{1}}}(p)\\\vdots \\{\frac {\partial f}{\partial x_{n}}}(p)\end{bmatrix}};$ $df_{p}={\begin{bmatrix}{\frac {\partial f}{\partial x_{1}}}(p)&\cdots &{\frac {\partial f}{\partial x_{n}}}(p)\end{bmatrix}}.$

While these both have the same components, they differ in what kind of mathematical object they represent: at each point, the derivative is a cotangent vector, a linear form (or covector) which expresses how much the (scalar) output changes for a given infinitesimal change in (vector) input, while at each point, the gradient is a tangent vector, which represents an infinitesimal change in (vector) input. In symbols, the gradient is an element of the tangent space at a point, $\nabla f(p)\in T_{p}\mathbb {R} ^{n}$ , while the derivative is a map from the tangent space to the real numbers, $df_{p}\colon T_{p}\mathbb {R} ^{n}\to \mathbb {R}$ . The tangent spaces at each point of $\mathbb {R} ^{n}$ can be "naturally" identified with the vector space $\mathbb {R} ^{n}$ itself, and similarly the cotangent space at each point can be naturally identified with the dual vector space $(\mathbb {R} ^{n})^{*}$ of covectors; thus the value of the gradient at a point can be thought of a vector in the original $\mathbb {R} ^{n}$ , not just as a tangent vector.

Computationally, given a tangent vector, the vector can be *multiplied* by the derivative (as matrices), which is equal to taking the dot product with the gradient: $(df_{p})(v)={\begin{bmatrix}{\frac {\partial f}{\partial x_{1}}}(p)&\cdots &{\frac {\partial f}{\partial x_{n}}}(p)\end{bmatrix}}{\begin{bmatrix}v_{1}\\\vdots \\v_{n}\end{bmatrix}}=\sum _{i=1}^{n}{\frac {\partial f}{\partial x_{i}}}(p)v_{i}={\begin{bmatrix}{\frac {\partial f}{\partial x_{1}}}(p)\\\vdots \\{\frac {\partial f}{\partial x_{n}}}(p)\end{bmatrix}}\cdot {\begin{bmatrix}v_{1}\\\vdots \\v_{n}\end{bmatrix}}=\nabla f(p)\cdot v$

#### Differential or (exterior) derivative

The best linear approximation to a differentiable function $f:\mathbb {R} ^{n}\to \mathbb {R}$ at a point x in $\mathbb {R} ^{n}$ is a linear map from $\mathbb {R} ^{n}$ to $\mathbb {R}$ which is often denoted by $df_{x}$ or $Df(x)$ and called the differential or total derivative of f at x . The function $df$ , which maps x to $df_{x}$ , is called the total differential or exterior derivative of f and is an example of a differential 1-form.

Much as the derivative of a function of a single variable represents the slope of the tangent to the graph of the function, the directional derivative of a function in several variables represents the slope of the tangent hyperplane in the direction of the vector.

The gradient is related to the differential by the formula $(\nabla f)_{x}\cdot v=df_{x}(v)$ for any $v\in \mathbb {R} ^{n}$ , where $\cdot$ is the dot product: taking the dot product of a vector with the gradient is the same as taking the directional derivative along the vector.

If $\mathbb {R} ^{n}$ is viewed as the space of (dimension n ) column vectors (of real numbers), then one can regard $df$ as the row vector with components $\left({\frac {\partial f}{\partial x_{1}}},\dots ,{\frac {\partial f}{\partial x_{n}}}\right),$ so that $df_{x}(v)$ is given by matrix multiplication. Assuming the standard Euclidean metric on $\mathbb {R} ^{n}$ , the gradient is then the corresponding column vector, that is, $(\nabla f)_{i}=df_{i}^{\mathsf {T}}.$

#### Linear approximation to a function

The best linear approximation to a function can be expressed in terms of the gradient, rather than the derivative. The gradient of a function f from the Euclidean space $\mathbb {R} ^{n}$ to $\mathbb {R}$ at any particular point $x_{0}$ in $\mathbb {R} ^{n}$ characterizes the best linear approximation to f at $x_{0}$ . The approximation is as follows:

$f(x)\approx f(x_{0})+(\nabla f)_{x_{0}}\cdot (x-x_{0})$

for x close to $x_{0}$ , where $(\nabla f)_{x_{0}}$ is the gradient of f computed at $x_{0}$ , and the dot denotes the dot product on $\mathbb {R} ^{n}$ . This equation is equivalent to the first two terms in the multivariable Taylor series expansion of f at $x_{0}$ .

### Relationship with Fréchet derivative

Let *U* be an open set in **R***n*. If the function *f* : *U* → **R** is differentiable, then the differential of *f* is the Fréchet derivative of *f*. Thus ∇*f* is a function from *U* to the space **R***n* such that $\lim _{h\to 0}{\frac {|f(x+h)-f(x)-\nabla f(x)\cdot h|}{\|h\|}}=0,$ where · is the dot product.

As a consequence, the usual properties of the derivative hold for the gradient, though the gradient is not a derivative itself, but rather dual to the derivative:

**Linearity**

The gradient is linear in the sense that if

f

and

g

are two real-valued functions differentiable at the point

a

∈

R

n

, and

α

and

β

are two constants, then

αf

+

βg

is differentiable at

a

, and moreover

$\nabla \left(\alpha f+\beta g\right)(a)=\alpha \nabla f(a)+\beta \nabla g(a).$

**Product rule**

If

f

and

g

are real-valued functions differentiable at a point

a

∈

R

n

, then the product rule asserts that the product

fg

is differentiable at

a

, and

$\nabla (fg)(a)=f(a)\nabla g(a)+g(a)\nabla f(a).$

**Chain rule**

Suppose that

f

:

A

→

R

is a real-valued function defined on a subset

A

of

R

n

, and that

f

is differentiable at a point

a

. There are two forms of the chain rule applying to the gradient. First, suppose that the function

g

is a

parametric curve

; that is, a function

g

:

I

→

R

n

maps a subset

I

⊂

R

into

R

n

. If

g

is differentiable at a point

c

∈

I

such that

g

(

c

) =

a

, then

$(f\circ g)'(c)=\nabla f(a)\cdot g'(c),$

where ∘ is the

composition operator

:

(

f

∘

g

)(

x

) =

f

(

g

(

x

))

.

More generally, if instead *I* ⊂ **R***k*, then the following holds: $\nabla (f\circ g)(c)={\big (}Dg(c){\big )}^{\mathsf {T}}{\big (}\nabla f(a){\big )},$ where (*Dg*)T denotes the transpose Jacobian matrix.

For the second form of the chain rule, suppose that *h* : *I* → **R** is a real valued function on a subset *I* of **R**, and that *h* is differentiable at the point *f*(*a*) ∈ *I*. Then $\nabla (h\circ f)(a)=h'{\big (}f(a){\big )}\nabla f(a).$

## Further properties and applications

### Level sets

A level surface, or isosurface, is the set of all points where some function has a given value.

If *f* is differentiable, then the dot product (∇*f* )*x* ⋅ *v* of the gradient at a point *x* with a vector *v* gives the directional derivative of *f* at *x* in the direction *v*. It follows that in this case the gradient of *f* is orthogonal to the level sets of *f*. For example, a level surface in three-dimensional space is defined by an equation of the form *F*(*x*, *y*, *z*) = *c*. The gradient of *F* is then normal to the surface.

More generally, any embedded hypersurface in a Riemannian manifold can be cut out by an equation of the form *F*(*P*) = 0 such that *dF* is nowhere zero. The gradient of *F* is then normal to the hypersurface.

Similarly, an affine algebraic hypersurface may be defined by an equation *F*(*x*1, ..., *x**n*) = 0, where *F* is a polynomial. The gradient of *F* is zero at a singular point of the hypersurface (this is the definition of a singular point). At a non-singular point, it is a nonzero normal vector.

### Conservative vector fields and the gradient theorem

The gradient of a function is called a gradient field. A (continuous) gradient field is always a conservative vector field: its line integral along any path depends only on the endpoints of the path, and can be evaluated by the gradient theorem (the fundamental theorem of calculus for line integrals). Conversely, a (continuous) conservative vector field is always the gradient of a function.

### Gradient is direction of steepest ascent

The gradient of a function $f\colon \mathbb {R} ^{n}\to \mathbb {R}$ at point *x* is also the direction of its steepest ascent, i.e. it maximizes its directional derivative:

Let $v\in \mathbb {R} ^{n}$ be an arbitrary unit vector. With the directional derivative defined as

$\nabla _{v}f(x)=\lim _{h\rightarrow 0}{\frac {f(x+vh)-f(x)}{h}},$

we get, by substituting the function $f(x+vh)$ with its Taylor series,

$\nabla _{v}f(x)=\lim _{h\rightarrow 0}{\frac {(f(x)+\nabla f\cdot vh+R)-f(x)}{h}},$

where R denotes higher order terms in $vh$ .

Dividing by h , and taking the limit yields a term which is bounded from above by the Cauchy–Schwarz inequality

$|\nabla _{v}f(x)|=|\nabla f\cdot v|\leq ||\nabla f||||v||=||\nabla f||.$

Choosing $v^{*}=\nabla f/||\nabla f||$ maximizes the directional derivative, and equals the upper bound

$|\nabla _{v^{*}}f(x)|=||\nabla f||^{2}/||\nabla f||=||\nabla f||.$

## Generalizations

### Jacobian

The Jacobian matrix is the generalization of the gradient for vector-valued functions of several variables and differentiable maps between Euclidean spaces or, more generally, manifolds. A further generalization for a function between Banach spaces is the Fréchet derivative.

Suppose **f** : **R***n* → **R***m* is a function such that each of its first-order partial derivatives exist on ℝ*n*. Then the Jacobian matrix of **f** is defined to be an *m*×*n* matrix, denoted by $\mathbf {J} _{\mathbb {f} }(\mathbb {x} )$ or simply $\mathbf {J}$ . The (*i*,*j*)th entry is ${\textstyle \mathbf {J} _{ij}={\partial f_{i}}/{\partial x_{j}}}$ . Explicitly $\mathbf {J} ={\begin{bmatrix}{\dfrac {\partial \mathbf {f} }{\partial x_{1}}}&\cdots &{\dfrac {\partial \mathbf {f} }{\partial x_{n}}}\end{bmatrix}}={\begin{bmatrix}\nabla ^{\mathsf {T}}f_{1}\\\vdots \\\nabla ^{\mathsf {T}}f_{m}\end{bmatrix}}={\begin{bmatrix}{\dfrac {\partial f_{1}}{\partial x_{1}}}&\cdots &{\dfrac {\partial f_{1}}{\partial x_{n}}}\\\vdots &\ddots &\vdots \\{\dfrac {\partial f_{m}}{\partial x_{1}}}&\cdots &{\dfrac {\partial f_{m}}{\partial x_{n}}}\end{bmatrix}}.$

### Gradient of a vector field

Since the total derivative of a vector field is a linear mapping from vectors to vectors, it is a tensor quantity.

In rectangular coordinates, the gradient of a vector field **f** = ( *f*1, *f*2, *f*3) is defined by:

$\nabla \mathbf {f} =g^{jk}{\frac {\partial f^{i}}{\partial x^{j}}}\mathbf {e} _{i}\otimes \mathbf {e} _{k},$

(where the Einstein summation notation is used and the tensor product of the vectors **e***i* and **e***k* is a dyadic tensor of type (2,0)). Overall, this expression equals the transpose of the Jacobian matrix:

${\frac {\partial f^{i}}{\partial x^{j}}}={\frac {\partial (f^{1},f^{2},f^{3})}{\partial (x^{1},x^{2},x^{3})}}.$

In curvilinear coordinates, or more generally on a curved manifold, the gradient involves Christoffel symbols:

$\nabla \mathbf {f} =g^{jk}\left({\frac {\partial f^{i}}{\partial x^{j}}}+{\Gamma ^{i}}_{jl}f^{l}\right)\mathbf {e} _{i}\otimes \mathbf {e} _{k},$

where *g**jk* are the components of the inverse metric tensor and the **e***i* are the coordinate basis vectors.

Expressed more invariantly, the gradient of a vector field **f** can be defined by the Levi-Civita connection and metric tensor:

$\nabla ^{a}f^{b}=g^{ac}\nabla _{c}f^{b},$

where ∇*c* is the connection.

### Riemannian manifolds

For any smooth function f on a Riemannian manifold (*M*, *g*), the gradient of *f* is the vector field ∇*f* such that for any vector field *X*, $g(\nabla f,X)=\partial _{X}f,$ that is, $g_{x}{\big (}(\nabla f)_{x},X_{x}{\big )}=(\partial _{X}f)(x),$ where *g**x*( , ) denotes the inner product of tangent vectors at *x* defined by the metric *g* and ∂*X* *f* is the function that takes any point *x* ∈ *M* to the directional derivative of *f* in the direction *X*, evaluated at *x*. In other words, in a coordinate chart *φ* from an open subset of *M* to an open subset of **R***n*, (∂*X* *f* )(*x*) is given by: $\sum _{j=1}^{n}X^{j}{\big (}\varphi (x){\big )}{\frac {\partial }{\partial x_{j}}}(f\circ \varphi ^{-1}){\Bigg |}_{\varphi (x)},$ where *X**j* denotes the *j*th component of *X* in this coordinate chart.

So, the local form of the gradient takes the form:

$\nabla f=g^{ik}{\frac {\partial f}{\partial x^{k}}}{\textbf {e}}_{i}.$

Generalizing the case *M* = **R***n*, the gradient of a function is related to its exterior derivative, since $(\partial _{X}f)(x)=(df)_{x}(X_{x}).$ More precisely, the gradient ∇*f* is the vector field associated to the differential 1-form *df* using the musical isomorphism $\sharp =\sharp ^{g}\colon T^{*}M\to TM$ (called "sharp") defined by the metric *g*. The relation between the exterior derivative and the gradient of a function on **R***n* is a special case of this in which the metric is the flat metric given by the dot product.
