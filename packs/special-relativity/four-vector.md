---
title: "Four-vector"
source: https://en.wikipedia.org/wiki/Four-vector
domain: special-relativity
license: CC-BY-SA-4.0
tags: special relativity, lorentz transformation, time dilation, mass-energy equivalence
fetched: 2026-07-02
---

# Four-vector

In special relativity, a **four-vector** (or **4-vector**, sometimes **Lorentz vector**) is an element of a four-dimensional vector space object with four components, which transform under Lorentz transformations with respect to a change of basis. Its magnitude is determined by an indefinite quadratic form, the preservation of which defines the Lorentz transformations, which include spatial rotations and boosts (a change by a constant velocity to another reference frame).

Four-vectors describe, for instance, position *x**μ* in spacetime modeled as Minkowski space, a particle's four-momentum *p**μ*, the amplitude of the electromagnetic four-potential *A**μ*(*x*) at a point x in spacetime, and the elements of the subspace spanned by the gamma matrices inside the Dirac algebra.

The Lorentz group may be represented by a set of 4 × 4 matrices Λ. The action of a Lorentz transformation on a general contravariant four-vector X (like the examples above), regarded as a column vector with Cartesian coordinates with respect to an inertial frame in the entries, is given by $X'=\Lambda X,$ (matrix multiplication) where the components of the primed object refer to the new frame. Related to the examples above that are given as contravariant vectors, there are also the corresponding covariant vectors *x**μ*, *p**μ* and *A**μ*(*x*). These transform according to the rule $X'=\left(\Lambda ^{-1}\right)^{\textrm {T}}X,$ where T denotes the matrix transpose. This rule is different from the above rule. It corresponds to the dual representation of the standard representation. However, for the Lorentz group the dual of any representation is equivalent to the original representation (see Representation theory of the Lorentz group). Thus the objects with covariant indices are four-vectors as well.

For an example of a well-behaved four-component object in special relativity that is *not* a four-vector, see Dirac spinor. It is similarly defined, the difference being that the transformation rule under Lorentz transformations is given by a representation other than the standard representation. In this case, the rule reads *X*′ = Π(Λ)*X*, where Π(Λ) is a 4×4 matrix other than Λ. Similar remarks apply to objects with fewer or more components that are well-behaved under Lorentz transformations. These include scalars, spinors, tensors and spinor-tensors.

The article considers four-vectors in the context of special relativity. Although the concept of four-vectors also extends to general relativity, some of the results stated in this article require modification in general relativity.

In the standard configuration, where the primed frame has speed *u* along the positive x-axis, the transformation of four-vectors is: $X'={\begin{bmatrix}{\gamma (u)}&{-\gamma (u){\frac {u}{c^{2}}}}&{0}&{0}\\{-\gamma (u)u}&{\gamma (u)}&{0}&{0}\\{0}&{0}&{1}&{0}\\{0}&{0}&{0}&{1}\end{bmatrix}}X,$ or $X'={\begin{bmatrix}{\gamma (u)}&{-\gamma (u){\frac {u}{c}}}&{0}&{0}\\{-\gamma (u){\frac {u}{c}}}&{\gamma (u)}&{0}&{0}\\{0}&{0}&{1}&{0}\\{0}&{0}&{0}&{1}\end{bmatrix}}X,$ depending on convention (viz. whether *events* are written (*t*, *x*, *y*, *z*) or (*ct*, *x*, *y*, *z*), respectively).

## Notation

The notations in this article are: lowercase bold for three-dimensional vectors, hats for three-dimensional unit vectors, capital bold for four dimensional vectors (except for the four-gradient operator), and tensor index notation.

## Four-vector algebra

### Four-vectors in a real-valued basis

A **four-vector** *A* is a vector with a "timelike" component and three "spacelike" components, and can be written in various equivalent notations: ${\begin{aligned}\mathbf {A} &=\left(A^{0},\,A^{1},\,A^{2},\,A^{3}\right)\\&=A^{0}\mathbf {E} _{0}+A^{1}\mathbf {E} _{1}+A^{2}\mathbf {E} _{2}+A^{3}\mathbf {E} _{3}\\&=A^{0}\mathbf {E} _{0}+A^{i}\mathbf {E} _{i}\\&=A^{\alpha }\mathbf {E} _{\alpha }\end{aligned}}$ where *Aα* is the component multiplier and **E***α* is the basis vector; note that both are necessary to make a vector, and that when *Aα* is seen alone, it refers strictly to the *components* of the vector.

The upper indices indicate contravariant components. Here the standard convention is that Latin indices take values for spatial components, so that *i* = 1, 2, 3, and Greek indices take values for time and space components, so *α* = 0, 1, 2, 3, used with the summation convention. The split between the time component and the spatial components is a useful one to make when determining contractions of one four vector with other tensor quantities, such as for calculating Lorentz invariants in scalar products (examples are given below), or raising and lowering indices.

In special relativity, the spacelike basis **E**1, **E**2, **E**3 and components *A*1, *A*2, *A*3 are often Cartesian basis and components: ${\begin{aligned}\mathbf {A} &=\left(A_{t},\,A_{x},\,A_{y},\,A_{z}\right)\\&=A_{t}\mathbf {E} _{t}+A_{x}\mathbf {E} _{x}+A_{y}\mathbf {E} _{y}+A_{z}\mathbf {E} _{z}\\\end{aligned}}$ although, of course, any other basis and components may be used, such as spherical polar coordinates ${\begin{aligned}\mathbf {A} &=\left(A_{t},\,A_{r},\,A_{\theta },\,A_{\phi }\right)\\&=A_{t}\mathbf {E} _{t}+A_{r}\mathbf {E} _{r}+A_{\theta }\mathbf {E} _{\theta }+A_{\phi }\mathbf {E} _{\phi }\\\end{aligned}}$ or cylindrical polar coordinates, ${\begin{aligned}\mathbf {A} &=(A_{t},\,A_{r},\,A_{\theta },\,A_{z})\\&=A_{t}\mathbf {E} _{t}+A_{r}\mathbf {E} _{r}+A_{\theta }\mathbf {E} _{\theta }+A_{z}\mathbf {E} _{z}\\\end{aligned}}$ or any other orthogonal coordinates, or even general curvilinear coordinates. Note the coordinate labels are always subscripted as labels and are not indices taking numerical values. In general relativity, local curvilinear coordinates in a local basis must be used. Geometrically, a four-vector can still be interpreted as an arrow, but in spacetime - not just space. In relativity, the arrows are drawn as part of Minkowski diagram (also called *spacetime diagram*). In this article, four-vectors will be referred to simply as vectors.

It is also customary to represent the bases by column vectors: $\mathbf {E} _{0}={\begin{pmatrix}1\\0\\0\\0\end{pmatrix}}\,,\quad \mathbf {E} _{1}={\begin{pmatrix}0\\1\\0\\0\end{pmatrix}}\,,\quad \mathbf {E} _{2}={\begin{pmatrix}0\\0\\1\\0\end{pmatrix}}\,,\quad \mathbf {E} _{3}={\begin{pmatrix}0\\0\\0\\1\end{pmatrix}}$ so that: $\mathbf {A} ={\begin{pmatrix}A^{0}\\A^{1}\\A^{2}\\A^{3}\end{pmatrix}}$

The relation between the covariant and contravariant coordinates is through the Minkowski metric tensor (referred to as the metric), *η* which raises and lowers indices as follows: $A_{\mu }=\eta _{\mu \nu }A^{\nu }\,,$ and in various equivalent notations the covariant components are: ${\begin{aligned}\mathbf {A} &=(A_{0},\,A_{1},\,A_{2},\,A_{3})\\&=A_{0}\mathbf {E} ^{0}+A_{1}\mathbf {E} ^{1}+A_{2}\mathbf {E} ^{2}+A_{3}\mathbf {E} ^{3}\\&=A_{0}\mathbf {E} ^{0}+A_{i}\mathbf {E} ^{i}\\&=A_{\alpha }\mathbf {E} ^{\alpha }\\\end{aligned}}$ where the lowered index indicates it to be covariant. Often the metric is diagonal, as is the case for orthogonal coordinates (see line element), but not in general curvilinear coordinates.

The bases can be represented by row vectors: ${\begin{aligned}\mathbf {E} ^{0}&={\begin{pmatrix}1&0&0&0\end{pmatrix}}\,,&\mathbf {E} ^{1}&={\begin{pmatrix}0&1&0&0\end{pmatrix}}\,,\\[1ex]\mathbf {E} ^{2}&={\begin{pmatrix}0&0&1&0\end{pmatrix}}\,,&\mathbf {E} ^{3}&={\begin{pmatrix}0&0&0&1\end{pmatrix}},\end{aligned}}$ so that: $\mathbf {A} ={\begin{pmatrix}A_{0}&A_{1}&A_{2}&A_{3}\end{pmatrix}}$

The motivation for the above conventions are that the scalar product is a scalar, see below for details.

### Lorentz transformation

Given two inertial or rotated frames of reference, a four-vector is defined as a quantity which transforms according to the Lorentz transformation matrix **Λ**: $\mathbf {A} '={\boldsymbol {\Lambda }}\mathbf {A}$

In index notation, the contravariant and covariant components transform according to, respectively: ${A'}^{\mu }=\Lambda ^{\mu }{}_{\nu }A^{\nu }\,,\quad {A'}_{\mu }=\Lambda _{\mu }{}^{\nu }A_{\nu }$ in which the matrix **Λ** has components Λ*μν* in row *μ* and column *ν*, and the matrix (**Λ**−1)T has components Λ*μν* in row *μ* and column *ν*.

For background on the nature of this transformation definition, see tensor. All four-vectors transform in the same way, and this can be generalized to four-dimensional relativistic tensors; see special relativity.

#### Pure rotations about an arbitrary axis

For two frames rotated by a fixed angle *θ* about an axis defined by the unit vector: ${\hat {\mathbf {n} }}=\left({\hat {n}}_{1},{\hat {n}}_{2},{\hat {n}}_{3}\right)\,,$ without any boosts, the matrix **Λ** has components given by: ${\begin{aligned}\Lambda _{00}&=1\\\Lambda _{0i}=\Lambda _{i0}&=0\\\Lambda _{ij}&=\left(\delta _{ij}-{\hat {n}}_{i}{\hat {n}}_{j}\right)\cos \theta -\varepsilon _{ijk}{\hat {n}}_{k}\sin \theta +{\hat {n}}_{i}{\hat {n}}_{j}\end{aligned}}$ where *δij* is the Kronecker delta, and *εijk* is the three-dimensional Levi-Civita symbol. The spacelike components of four-vectors are rotated, while the timelike components remain unchanged.

For the case of rotations about the *z*-axis only, the spacelike part of the Lorentz matrix reduces to the rotation matrix about the *z*-axis: ${\begin{pmatrix}{A'}^{0}\\{A'}^{1}\\{A'}^{2}\\{A'}^{3}\end{pmatrix}}={\begin{pmatrix}1&0&0&0\\0&\cos \theta &-\sin \theta &0\\0&\sin \theta &\cos \theta &0\\0&0&0&1\\\end{pmatrix}}{\begin{pmatrix}A^{0}\\A^{1}\\A^{2}\\A^{3}\end{pmatrix}}\ .$

#### Pure boosts in any direction

For two frames moving at constant relative three-velocity **v** (not four-velocity, see below), it is convenient to denote and define the relative velocity in units of *c* by: ${\boldsymbol {\beta }}=(\beta _{1},\,\beta _{2},\,\beta _{3})={\frac {1}{c}}(v_{1},\,v_{2},\,v_{3})={\frac {1}{c}}\mathbf {v} \,.$

Then without rotations, the matrix **Λ** has components given by: ${\begin{aligned}\Lambda _{00}&=\gamma ,\\\Lambda _{0i}=\Lambda _{i0}&=-\gamma \beta _{i},\\\Lambda _{ij}=\Lambda _{ji}&=(\gamma -1){\frac {\beta _{i}\beta _{j}}{\beta ^{2}}}+\delta _{ij}=(\gamma -1){\frac {v_{i}v_{j}}{v^{2}}}+\delta _{ij},\\\end{aligned}}$ where the Lorentz factor is defined by: $\gamma ={\frac {1}{\sqrt {1-{\boldsymbol {\beta }}\cdot {\boldsymbol {\beta }}}}}\,,$ and *δij* is the Kronecker delta. Contrary to the case for pure rotations, the spacelike and timelike components are mixed together under boosts.

For the case of a boost in the *x*-direction only, the matrix reduces to; ${\begin{pmatrix}A'^{0}\\A'^{1}\\A'^{2}\\A'^{3}\end{pmatrix}}={\begin{pmatrix}\cosh \phi &-\sinh \phi &0&0\\-\sinh \phi &\cosh \phi &0&0\\0&0&1&0\\0&0&0&1\\\end{pmatrix}}{\begin{pmatrix}A^{0}\\A^{1}\\A^{2}\\A^{3}\end{pmatrix}}$

Where the rapidity *ϕ* expression has been used, written in terms of the hyperbolic functions: $\gamma =\cosh \phi .$

This Lorentz matrix illustrates the boost to be a *hyperbolic rotation* in four dimensional spacetime, analogous to the circular rotation above in three-dimensional space.

### Properties

#### Linearity

Four-vectors have the same linearity properties as Euclidean vectors in three dimensions. They can be added in the usual entrywise way: ${\begin{aligned}\mathbf {A} +\mathbf {B} &=\left(A^{0},A^{1},A^{2},A^{3}\right)+\left(B^{0},B^{1},B^{2},B^{3}\right)\\&=\left(A^{0}+B^{0},A^{1}+B^{1},A^{2}+B^{2},A^{3}+B^{3}\right)\end{aligned}}$ and similarly scalar multiplication by a scalar *λ* is defined entrywise by: $\lambda \mathbf {A} =\lambda \left(A^{0},A^{1},A^{2},A^{3}\right)=\left(\lambda A^{0},\lambda A^{1},\lambda A^{2},\lambda A^{3}\right)$

Then subtraction is the inverse operation of addition, defined entrywise by: ${\begin{aligned}\mathbf {A} +(-1)\mathbf {B} &=\left(A^{0},A^{1},A^{2},A^{3}\right)+(-1)\left(B^{0},B^{1},B^{2},B^{3}\right)\\&=\left(A^{0}-B^{0},A^{1}-B^{1},A^{2}-B^{2},A^{3}-B^{3}\right)\end{aligned}}$

#### Minkowski tensor

Applying the Minkowski tensor *ημν* to two four-vectors **A** and **B**, writing the result in dot product notation, we have, using Einstein notation: $\mathbf {A} \cdot \mathbf {B} =A^{\mu }B^{\nu }\mathbf {E} _{\mu }\cdot \mathbf {E} _{\nu }=A^{\mu }\eta _{\mu \nu }B^{\nu }$

in special relativity. The dot product of the basis vectors is the Minkowski metric, as opposed to the Kronecker delta as in Euclidean space. It is convenient to rewrite the definition in matrix form: $\mathbf {A\cdot B} ={\begin{pmatrix}A^{0}&A^{1}&A^{2}&A^{3}\end{pmatrix}}{\begin{pmatrix}\eta _{00}&\eta _{01}&\eta _{02}&\eta _{03}\\\eta _{10}&\eta _{11}&\eta _{12}&\eta _{13}\\\eta _{20}&\eta _{21}&\eta _{22}&\eta _{23}\\\eta _{30}&\eta _{31}&\eta _{32}&\eta _{33}\end{pmatrix}}{\begin{pmatrix}B^{0}\\B^{1}\\B^{2}\\B^{3}\end{pmatrix}}$ in which case *ημν* above is the entry in row *μ* and column *ν* of the Minkowski metric as a square matrix. The Minkowski metric is not a Euclidean metric, because it is indefinite (see metric signature). A number of other expressions can be used because the metric tensor can raise and lower the components of **A** or **B**. For contra/co-variant components of **A** and co/contra-variant components of **B**, we have: $\mathbf {A} \cdot \mathbf {B} =A^{\mu }\eta _{\mu \nu }B^{\nu }=A_{\nu }B^{\nu }=A^{\mu }B_{\mu }$ so in the matrix notation: ${\begin{aligned}\mathbf {A} \cdot \mathbf {B} &={\begin{pmatrix}A_{0}&A_{1}&A_{2}&A_{3}\end{pmatrix}}{\begin{pmatrix}B^{0}\\B^{1}\\B^{2}\\B^{3}\end{pmatrix}}\\[1ex]&={\begin{pmatrix}B_{0}&B_{1}&B_{2}&B_{3}\end{pmatrix}}{\begin{pmatrix}A^{0}\\A^{1}\\A^{2}\\A^{3}\end{pmatrix}}\end{aligned}}$ while for **A** and **B** each in covariant components: $\mathbf {A} \cdot \mathbf {B} =A_{\mu }\eta ^{\mu \nu }B_{\nu }$ with a similar matrix expression to the above.

Applying the Minkowski tensor to a four-vector **A** with itself we get: $\mathbf {A\cdot A} =A^{\mu }\eta _{\mu \nu }A^{\nu }$ which, depending on the case, may be considered the square, or its negative, of the length of the vector.

Following are two common choices for the metric tensor in the standard basis (essentially Cartesian coordinates). If orthogonal coordinates are used, there would be scale factors along the diagonal part of the spacelike part of the metric, while for general curvilinear coordinates the entire spacelike part of the metric would have components dependent on the curvilinear basis used.

##### Standard basis, (+−−−) signature

The (+−−−) metric signature is sometimes called the "mostly minus" convention, or the "west coast" convention.

In the (+−−−) metric signature, evaluating the summation over indices gives: $\mathbf {A} \cdot \mathbf {B} =A^{0}B^{0}-A^{1}B^{1}-A^{2}B^{2}-A^{3}B^{3}$ while in matrix form: $\mathbf {A\cdot B} ={\begin{pmatrix}A^{0}&A^{1}&A^{2}&A^{3}\end{pmatrix}}{\begin{pmatrix}1&0&0&0\\0&-1&0&0\\0&0&-1&0\\0&0&0&-1\end{pmatrix}}{\begin{pmatrix}B^{0}\\B^{1}\\B^{2}\\B^{3}\end{pmatrix}}$

It is a recurring theme in special relativity to take the expression $\mathbf {A} \cdot \mathbf {B} =A^{0}B^{0}-A^{1}B^{1}-A^{2}B^{2}-A^{3}B^{3}=C$ in one reference frame, where *C* is the value of the scalar product in this frame, and: $\mathbf {A} '\cdot \mathbf {B} '={A'}^{0}{B'}^{0}-{A'}^{1}{B'}^{1}-{A'}^{2}{B'}^{2}-{A'}^{3}{B'}^{3}=C'$ in another frame, in which *C*′ is the value of the scalar product in this frame. Then since the scalar product is an invariant, these must be equal: $\mathbf {A} \cdot \mathbf {B} =\mathbf {A} '\cdot \mathbf {B} '$ that is: ${\begin{aligned}C&=A^{0}B^{0}-A^{1}B^{1}-A^{2}B^{2}-A^{3}B^{3}\\[2pt]&={A'}^{0}{B'}^{0}-{A'}^{1}{B'}^{1}-{A'}^{2}{B'}^{2}-{A'}^{3}{B'}^{3}\end{aligned}}$

Considering that physical quantities in relativity are four-vectors, this equation has the appearance of a "conservation law", but there is no "conservation" involved. The primary significance of the Minkowski scalar product is that for any two four-vectors, its value is invariant for all observers; a change of coordinates does not result in a change in value of the scalar product. The components of the four-vectors change from one frame to another; **A** and **A**′ are connected by a Lorentz transformation, and similarly for **B** and **B**′, although the scalar products are the same in all frames. Nevertheless, this type of expression is exploited in relativistic calculations on a par with conservation laws, since the magnitudes of components can be determined without explicitly performing any Lorentz transformations. A particular example is with energy and momentum in the energy-momentum relation derived from the four-momentum vector (see also below).

In this signature we have: $\mathbf {A\cdot A} =\left(A^{0}\right)^{2}-\left(A^{1}\right)^{2}-\left(A^{2}\right)^{2}-\left(A^{3}\right)^{2}$

With the signature (+−−−), four-vectors may be classified as either spacelike if **A** ⋅ **A** < 0, timelike if **A** ⋅ **A** > 0, and null vectors if **A** ⋅ **A** = 0.

##### Standard basis, (−+++) signature

The (−+++) metric signature is sometimes called the "east coast" convention.

Some authors define *η* with the opposite sign, in which case we have the (−+++) metric signature. Evaluating the summation with this signature: $\mathbf {A\cdot B} =-A^{0}B^{0}+A^{1}B^{1}+A^{2}B^{2}+A^{3}B^{3}$ while the matrix form is: $\mathbf {A\cdot B} =\left({\begin{matrix}A^{0}&A^{1}&A^{2}&A^{3}\end{matrix}}\right)\left({\begin{matrix}-1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{matrix}}\right)\left({\begin{matrix}B^{0}\\B^{1}\\B^{2}\\B^{3}\end{matrix}}\right)$

Note that in this case, in one frame: $\mathbf {A} \cdot \mathbf {B} =-A^{0}B^{0}+A^{1}B^{1}+A^{2}B^{2}+A^{3}B^{3}=-C$ while in another: $\mathbf {A} '\cdot \mathbf {B} '=-{A'}^{0}{B'}^{0}+{A'}^{1}{B'}^{1}+{A'}^{2}{B'}^{2}+{A'}^{3}{B'}^{3}=-C'$ so that ${\begin{aligned}-C&=-A^{0}B^{0}+A^{1}B^{1}+A^{2}B^{2}+A^{3}B^{3}\\[2pt]&=-{A'}^{0}{B'}^{0}+{A'}^{1}{B'}^{1}+{A'}^{2}{B'}^{2}+{A'}^{3}{B'}^{3}\end{aligned}}$ which is equivalent to the above expression for *C* in terms of **A** and **B**. Either convention will work. With the Minkowski metric defined in the two ways above, the only difference between covariant and contravariant four-vector components are signs, therefore the signs depend on which sign convention is used.

We have: $\mathbf {A\cdot A} =-\left(A^{0}\right)^{2}+\left(A^{1}\right)^{2}+\left(A^{2}\right)^{2}+\left(A^{3}\right)^{2}$

With the signature (−+++), four-vectors may be classified as either spacelike if **A** ⋅ **A** > 0, timelike if **A** ⋅ **A** < 0, and null if **A** ⋅ **A** = 0.

##### Dual vectors

Applying the Minkowski tensor is often expressed as the effect of the dual vector of one vector on the other: $\mathbf {A\cdot B} =A^{*}(\mathbf {B} )=A{_{\nu }}B^{\nu }.$

Here the *Aν* are the components of the dual **A*** of vector **A** in the dual basis and called the covariant coordinates of **A**, while the original *Aν* components are called the contravariant coordinates.

## Four-vector calculus

### Derivatives and differentials

In special relativity (but not general relativity), the derivative of a four-vector with respect to a scalar *λ* (invariant) is itself a four-vector. It is also useful to take the differential of the four-vector, *d***A** and divide it by the differential of the scalar, *dλ*: ${\underset {\text{differential}}{d\mathbf {A} }}={\underset {\text{derivative}}{\frac {d\mathbf {A} }{d\lambda }}}{\underset {\text{differential}}{d\lambda }}$ where the contravariant components are: $d\mathbf {A} =\left(dA^{0},dA^{1},dA^{2},dA^{3}\right)$ while the covariant components are: $d\mathbf {A} =\left(dA_{0},dA_{1},dA_{2},dA_{3}\right)$

In relativistic mechanics, one often takes the differential of a four-vector and divides by the differential in proper time (see below).

## Fundamental four-vectors

### Four-position

A point in Minkowski space is a time and spatial position, called an "event", or sometimes the **position four-vector** or **four-position** or **4-position**, described in some reference frame by a set of four coordinates: $\mathbf {R} =\left(ct,\mathbf {r} \right)$ where **r** is the three-dimensional space position vector. If **r** is a function of coordinate time *t* in the same frame, i.e. **r** = **r**(*t*), this corresponds to a sequence of events as *t* varies. The definition *R*0 = *ct* ensures that all the coordinates have the same dimension (of length) and units. These coordinates are the components of the *position four-vector* for the event.

The **displacement four-vector** is defined to be an "arrow" linking two events: $\Delta \mathbf {R} =\left(c\Delta t,\Delta \mathbf {r} \right)$

For the differential four-position on a world line we have, using a norm notation: $\|d\mathbf {R} \|^{2}=\mathbf {dR\cdot dR} =dR^{\mu }dR_{\mu }=c^{2}d\tau ^{2}=ds^{2}\,,$ defining the differential line element d*s* and differential proper time increment d*τ*, but this "norm" is also: $\|d\mathbf {R} \|^{2}=(cdt)^{2}-d\mathbf {r} \cdot d\mathbf {r} \,,$ so that: $(cd\tau )^{2}=(cdt)^{2}-d\mathbf {r} \cdot d\mathbf {r} \,.$

When considering physical phenomena, differential equations arise naturally; however, when considering space and time derivatives of functions, it is unclear which reference frame these derivatives are taken with respect to. It is agreed that time derivatives are taken with respect to the proper time $\tau$ . As proper time is an invariant, this guarantees that the proper-time-derivative of any four-vector is itself a four-vector. It is then important to find a relation between this proper-time-derivative and another time derivative (using the coordinate time *t* of an inertial reference frame). This relation is provided by taking the above differential invariant spacetime interval, then dividing by (*cdt*)2 to obtain $\left({\frac {cd\tau }{cdt}}\right)^{2}=1-\left({\frac {d\mathbf {r} }{cdt}}\cdot {\frac {d\mathbf {r} }{cdt}}\right)=1-{\frac {\mathbf {u} \cdot \mathbf {u} }{c^{2}}}={\frac {1}{\gamma (\mathbf {u} )^{2}}}\,,$ where **u** = *d***r**/*dt* is the coordinate 3-velocity of an object measured in the same frame as the coordinates *x*, *y*, *z*, and coordinate time *t*, and $\gamma (\mathbf {u} )={\frac {1}{\sqrt {1-{\frac {\mathbf {u} \cdot \mathbf {u} }{c^{2}}}}}}$ is the Lorentz factor. This provides a useful relation between the differentials in coordinate time and proper time: $dt=\gamma (\mathbf {u} )d\tau \,.$

This relation can also be found from the time transformation in the Lorentz transformations.

Important four-vectors in relativity theory can be defined by applying this differential ⁠*d*/*dτ*⁠.

### Four-gradient

Considering that partial derivatives are linear operators, one can form a four-gradient from the partial time derivative ∂/∂*t* and the spatial gradient operator ∇. Using the standard basis, in index and abbreviated notations, the contravariant components are: ${\begin{aligned}{\boldsymbol {\partial }}&=\left({\frac {\partial }{\partial x_{0}}},\,-{\frac {\partial }{\partial x_{1}}},\,-{\frac {\partial }{\partial x_{2}}},\,-{\frac {\partial }{\partial x_{3}}}\right)\\&=(\partial ^{0},\,-\partial ^{1},\,-\partial ^{2},\,-\partial ^{3})\\&=\mathbf {E} _{0}\partial ^{0}-\mathbf {E} _{1}\partial ^{1}-\mathbf {E} _{2}\partial ^{2}-\mathbf {E} _{3}\partial ^{3}\\&=\mathbf {E} _{0}\partial ^{0}-\mathbf {E} _{i}\partial ^{i}\\&=\mathbf {E} _{\alpha }\partial ^{\alpha }\\&=\left({\frac {1}{c}}{\frac {\partial }{\partial t}},\,-\nabla \right)\\&=\left({\frac {\partial _{t}}{c}},-\nabla \right)\\&=\mathbf {E} _{0}{\frac {1}{c}}{\frac {\partial }{\partial t}}-\nabla \\\end{aligned}}$

Note the basis vectors are placed in front of the components, to prevent confusion between taking the derivative of the basis vector, or simply indicating the partial derivative is a component of this four-vector. The covariant components are: ${\begin{aligned}{\boldsymbol {\partial }}&=\left({\frac {\partial }{\partial x^{0}}},\,{\frac {\partial }{\partial x^{1}}},\,{\frac {\partial }{\partial x^{2}}},\,{\frac {\partial }{\partial x^{3}}}\right)\\&=(\partial _{0},\,\partial _{1},\,\partial _{2},\,\partial _{3})\\&=\mathbf {E} ^{0}\partial _{0}+\mathbf {E} ^{1}\partial _{1}+\mathbf {E} ^{2}\partial _{2}+\mathbf {E} ^{3}\partial _{3}\\&=\mathbf {E} ^{0}\partial _{0}+\mathbf {E} ^{i}\partial _{i}\\&=\mathbf {E} ^{\alpha }\partial _{\alpha }\\&=\left({\frac {1}{c}}{\frac {\partial }{\partial t}},\,\nabla \right)\\&=\left({\frac {\partial _{t}}{c}},\nabla \right)\\&=\mathbf {E} ^{0}{\frac {1}{c}}{\frac {\partial }{\partial t}}+\nabla \\\end{aligned}}$

Since this is an operator, it does not have a "length", but evaluating the scalar product of the operator with itself gives another operator: $\partial ^{\mu }\partial _{\mu }={\frac {1}{c^{2}}}{\frac {\partial ^{2}}{\partial t^{2}}}-\nabla ^{2}={\frac {{\partial _{t}}^{2}}{c^{2}}}-\nabla ^{2}$ called the D'Alembert operator.

## Kinematics

### Four-velocity

The four-velocity of a particle is defined by: $\mathbf {U} ={\frac {d\mathbf {X} }{d\tau }}={\frac {d\mathbf {X} }{dt}}{\frac {dt}{d\tau }}=\gamma (\mathbf {u} )\left(c,\mathbf {u} \right),$

Geometrically, **U** is a normalized vector tangent to the world line of the particle. Using the differential of the four-position, the magnitude of the four-velocity can be obtained: $\|\mathbf {U} \|^{2}=U^{\mu }U_{\mu }={\frac {dX^{\mu }}{d\tau }}{\frac {dX_{\mu }}{d\tau }}={\frac {dX^{\mu }dX_{\mu }}{d\tau ^{2}}}=c^{2}\,,$

In short, the magnitude of the four-velocity for any object is always a fixed constant: $\|\mathbf {U} \|^{2}=c^{2}$

The norm is also: $\|\mathbf {U} \|^{2}={\gamma (\mathbf {u} )}^{2}\left(c^{2}-\mathbf {u} \cdot \mathbf {u} \right)\,,$ so that: $c^{2}={\gamma (\mathbf {u} )}^{2}\left(c^{2}-\mathbf {u} \cdot \mathbf {u} \right)\,,$ which reduces to the definition of the Lorentz factor.

Units of four-velocity are m/s in SI and 1 in the geometrized unit system. Four-velocity is a contravariant vector.

### Four-acceleration

The four-acceleration is given by: $\mathbf {A} ={\frac {d\mathbf {U} }{d\tau }}=\gamma (\mathbf {u} )\left({\frac {d{\gamma }(\mathbf {u} )}{dt}}c,{\frac {d{\gamma }(\mathbf {u} )}{dt}}\mathbf {u} +\gamma (\mathbf {u} )\mathbf {a} \right).$ where **a** = *d***u**/*dt* is the coordinate 3-acceleration. Since the magnitude of **U** is a constant, the four acceleration is orthogonal to the four velocity, i.e. the Minkowski scalar product of the four-acceleration and the four-velocity is zero: $\mathbf {A} \cdot \mathbf {U} =A^{\mu }U_{\mu }={\frac {dU^{\mu }}{d\tau }}U_{\mu }={\frac {1}{2}}\,{\frac {d}{d\tau }}\left(U^{\mu }U_{\mu }\right)=0\,$ which is true for all world lines. The geometric meaning of four-acceleration is the curvature vector of the world line in Minkowski space.

## Dynamics

### Four-momentum

For a massive particle of rest mass (or invariant mass) *m*0, the four-momentum is given by: $\mathbf {P} =m_{0}\mathbf {U} =m_{0}\gamma (\mathbf {u} )(c,\mathbf {u} )=\left({\frac {E}{c}},\mathbf {p} \right)$ where the total energy of the moving particle is: $E=\gamma (\mathbf {u} )m_{0}c^{2}$ and the total relativistic momentum is: $\mathbf {p} =\gamma (\mathbf {u} )m_{0}\mathbf {u}$

Taking the scalar product of the four-momentum with itself: $\|\mathbf {P} \|^{2}=P^{\mu }P_{\mu }=m_{0}^{2}U^{\mu }U_{\mu }=m_{0}^{2}c^{2}$ and also: $\|\mathbf {P} \|^{2}={\frac {E^{2}}{c^{2}}}-\mathbf {p} \cdot \mathbf {p}$ which leads to the energy–momentum relation: $E^{2}=c^{2}\mathbf {p} \cdot \mathbf {p} +\left(m_{0}c^{2}\right)^{2}\,.$

This last relation is useful in relativistic mechanics, essential in relativistic quantum mechanics and relativistic quantum field theory, all with applications to particle physics.

### Four-force

The four-force acting on a particle is defined analogously to the 3-force as the time derivative of 3-momentum in Newton's second law: $\mathbf {F} ={\frac {d\mathbf {P} }{d\tau }}=\gamma (\mathbf {u} )\left({\frac {1}{c}}{\frac {dE}{dt}},{\frac {d\mathbf {p} }{dt}}\right)=\gamma (\mathbf {u} )\left({\frac {P}{c}},\mathbf {f} \right)$ where *P* is the power transferred to move the particle, and **f** is the 3-force acting on the particle. For a particle of constant invariant mass *m*0, this is equivalent to $\mathbf {F} =m_{0}\mathbf {A} =m_{0}\gamma (\mathbf {u} )\left({\frac {d{\gamma }(\mathbf {u} )}{dt}}c,\left({\frac {d{\gamma }(\mathbf {u} )}{dt}}\mathbf {u} +\gamma (\mathbf {u} )\mathbf {a} \right)\right)$

An invariant derived from the four-force is: $\mathbf {F} \cdot \mathbf {U} =F^{\mu }U_{\mu }=m_{0}A^{\mu }U_{\mu }=0$ from the above result.

## Thermodynamics

### Four-heat flux

The four-heat flux vector field, is essentially similar to the 3-d heat flux vector field **q**, in the local frame of the fluid: $\mathbf {Q} =-k{\boldsymbol {\partial }}T=-k\left({\frac {1}{c}}{\frac {\partial T}{\partial t}},\nabla T\right)$ where *T* is absolute temperature and *k* is thermal conductivity.

### Four-baryon number flux

The flux of baryons is: $\mathbf {S} =n\mathbf {U}$ where *n* is the number density of baryons in the local rest frame of the baryon fluid (positive values for baryons, negative for antibaryons), and **U** the four-velocity field (of the fluid) as above.

### Four-entropy

The four-entropy vector is defined by: $\mathbf {s} =s\mathbf {S} +{\frac {\mathbf {Q} }{T}}$ where *s* is the entropy per baryon, and T the absolute temperature, in the local rest frame of the fluid.

## Electromagnetism

Examples of four-vectors in electromagnetism include the following.

### Four-current

The electromagnetic four-current (or more correctly a four-current density) is defined by $\mathbf {J} =\left(\rho c,\mathbf {j} \right)$ formed from the current density **j** and charge density *ρ*.

### Four-potential

The electromagnetic four-potential (or more correctly a four-EM vector potential) defined by $\mathbf {A} =\left({\frac {\phi }{c}},\mathbf {a} \right)$ formed from the vector potential **a** and the scalar potential *ϕ*.

The four-potential is not uniquely determined, because it depends on a choice of gauge.

In the wave equation for the electromagnetic field:

- In vacuum, $({\boldsymbol {\partial }}\cdot {\boldsymbol {\partial }})\mathbf {A} =0$
- With a four-current source and using the Lorenz gauge condition $({\boldsymbol {\partial }}\cdot \mathbf {A} )=0$ , $({\boldsymbol {\partial }}\cdot {\boldsymbol {\partial }})\mathbf {A} =\mu _{0}\mathbf {J}$

## Waves

### Four-frequency

A photonic plane wave can be described by the *four-frequency*, defined as $\mathbf {N} =\nu \left(1,{\hat {\mathbf {n} }}\right)$ where ν is the frequency of the wave and ${\hat {\mathbf {n} }}$ is a unit vector in the travel direction of the wave. Now, $\|\mathbf {N} \|=N^{\mu }N_{\mu }=\nu ^{2}\left(1-{\hat {\mathbf {n} }}\cdot {\hat {\mathbf {n} }}\right)=0$ so the four-frequency of a photon is always a null vector.

### Four-wavevector

The quantities reciprocal to time t and space **r** are the angular frequency ω and angular wave vector **k**, respectively. They form the components of the **four-wavevector** or **wave four-vector**: $\mathbf {K} =\left({\frac {\omega }{c}},{\vec {\mathbf {k} }}\right)=\left({\frac {\omega }{c}},{\frac {\omega }{v_{p}}}{\hat {\mathbf {n} }}\right)\,.$

The wave four-vector has coherent derived unit of reciprocal meters in the SI.

A wave packet of nearly monochromatic light can be described by: $\mathbf {K} ={\frac {2\pi }{c}}\mathbf {N} ={\frac {2\pi }{c}}\nu \left(1,{\hat {\mathbf {n} }}\right)={\frac {\omega }{c}}\left(1,{\hat {\mathbf {n} }}\right)~.$

The de Broglie relations then showed that four-wavevector applied to matter waves as well as to light waves: $\mathbf {P} =\hbar \mathbf {K} =\left({\frac {E}{c}},{\vec {p}}\right)=\hbar \left({\frac {\omega }{c}},{\vec {k}}\right),$ yielding $E=\hbar \omega$ and ${\vec {p}}=\hbar {\vec {k}}$ , where ħ is the Planck constant divided by 2*π*.

The square of the norm is: $\|\mathbf {K} \|^{2}=K^{\mu }K_{\mu }=\left({\frac {\omega }{c}}\right)^{2}-\mathbf {k} \cdot \mathbf {k} \,,$ and by the de Broglie relation: $\|\mathbf {K} \|^{2}={\frac {1}{\hbar ^{2}}}\|\mathbf {P} \|^{2}=\left({\frac {m_{0}c}{\hbar }}\right)^{2}\,,$ we have the matter wave analogue of the energy–momentum relation: $\left({\frac {\omega }{c}}\right)^{2}-\mathbf {k} \cdot \mathbf {k} =\left({\frac {m_{0}c}{\hbar }}\right)^{2}~.$

Note that for massless particles, in which case *m*0 = 0, we have: $\left({\frac {\omega }{c}}\right)^{2}=\mathbf {k} \cdot \mathbf {k} \,,$ or ‖**k**‖ = *ω*/*c*. Note this is consistent with the above case; for photons with a 3-wavevector of modulus *ω / c* , in the direction of wave propagation defined by the unit vector ${\hat {\mathbf {n} }}~.$

## Quantum theory

### Four-probability current

In quantum mechanics, the four-probability current or probability four-current is analogous to the electromagnetic four-current: $\mathbf {J} =(\rho c,\mathbf {j} )$ where *ρ* is the probability density function corresponding to the time component, and **j** is the probability current vector. In non-relativistic quantum mechanics, this current is always well defined because the expressions for density and current are positive definite and can admit a probability interpretation. In relativistic quantum mechanics and quantum field theory, it is not always possible to find a current, particularly when interactions are involved.

Replacing the energy by the energy operator and the momentum by the momentum operator in the four-momentum, one obtains the four-momentum operator, used in relativistic wave equations.

### Four-spin

The four-spin of a particle is defined in the rest frame of a particle to be $\mathbf {S} =(0,\mathbf {s} )$ where **s** is the spin pseudovector. In quantum mechanics, not all three components of this vector are simultaneously measurable, only one component is. The timelike component is zero in the particle's rest frame, but not in any other frame. This component can be found from an appropriate Lorentz transformation.

The norm squared is the (negative of the) magnitude squared of the spin, and according to quantum mechanics we have $\|\mathbf {S} \|^{2}=-|\mathbf {s} |^{2}=-\hbar ^{2}s(s+1)$

This value is observable and quantized, with *s* the spin quantum number (not the magnitude of the spin vector).

## Other formulations

### Four-vectors in the algebra of physical space

A four-vector *A* can also be defined in using the Pauli matrices as a basis, again in various equivalent notations: ${\begin{aligned}\mathbf {A} &=\left(A^{0},\,A^{1},\,A^{2},\,A^{3}\right)\\&=A^{0}{\boldsymbol {\sigma }}_{0}+A^{1}{\boldsymbol {\sigma }}_{1}+A^{2}{\boldsymbol {\sigma }}_{2}+A^{3}{\boldsymbol {\sigma }}_{3}\\&=A^{0}{\boldsymbol {\sigma }}_{0}+A^{i}{\boldsymbol {\sigma }}_{i}\\&=A^{\alpha }{\boldsymbol {\sigma }}_{\alpha }\\\end{aligned}}$ or explicitly: ${\begin{aligned}\mathbf {A} &=A^{0}{\begin{pmatrix}1&0\\0&1\end{pmatrix}}+A^{1}{\begin{pmatrix}0&1\\1&0\end{pmatrix}}+A^{2}{\begin{pmatrix}0&-i\\i&0\end{pmatrix}}+A^{3}{\begin{pmatrix}1&0\\0&-1\end{pmatrix}}\\&={\begin{pmatrix}A^{0}+A^{3}&A^{1}-iA^{2}\\A^{1}+iA^{2}&A^{0}-A^{3}\end{pmatrix}}\end{aligned}}$ and in this formulation, the four-vector is represented as a Hermitian matrix (the matrix transpose and complex conjugate of the matrix leaves it unchanged), rather than a real-valued column or row vector. The determinant of the matrix is the modulus of the four-vector, so the determinant is an invariant: ${\begin{aligned}|\mathbf {A} |&={\begin{vmatrix}A^{0}+A^{3}&A^{1}-iA^{2}\\A^{1}+iA^{2}&A^{0}-A^{3}\end{vmatrix}}\\[1ex]&=\left(A^{0}+A^{3}\right)\left(A^{0}-A^{3}\right)-\left(A^{1}-iA^{2}\right)\left(A^{1}+iA^{2}\right)\\[1ex]&=\left(A^{0}\right)^{2}-\left(A^{1}\right)^{2}-\left(A^{2}\right)^{2}-\left(A^{3}\right)^{2}\end{aligned}}$

This idea of using the Pauli matrices as basis vectors is employed in the algebra of physical space, an example of a Clifford algebra.

### Four-vectors in spacetime algebra

In spacetime algebra, another example of Clifford algebra, the gamma matrices can also form a basis. (They are also called the Dirac matrices, owing to their appearance in the Dirac equation). There is more than one way to express the gamma matrices, detailed in that main article.

The Feynman slash notation is a shorthand for a four-vector **A** contracted with the gamma matrices: $\mathbf {A} \!\!\!\!/=A_{\alpha }\gamma ^{\alpha }=A_{0}\gamma ^{0}+A_{1}\gamma ^{1}+A_{2}\gamma ^{2}+A_{3}\gamma ^{3}$

The four-momentum contracted with the gamma matrices is an important case in relativistic quantum mechanics and relativistic quantum field theory. In the Dirac equation and other relativistic wave equations, terms of the form: ${\begin{aligned}\mathbf {P} \!\!\!\!/=P_{\alpha }\gamma ^{\alpha }&=P_{0}\gamma ^{0}+P_{1}\gamma ^{1}+P_{2}\gamma ^{2}+P_{3}\gamma ^{3}\\[4pt]&={\dfrac {E}{c}}\gamma ^{0}-p_{x}\gamma ^{1}-p_{y}\gamma ^{2}-p_{z}\gamma ^{3}\\\end{aligned}}$ appear, in which the energy E and momentum components (*px*, *py*, *pz*) are replaced by their respective operators.
