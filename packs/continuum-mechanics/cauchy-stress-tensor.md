---
title: "Cauchy stress tensor"
source: https://en.wikipedia.org/wiki/Cauchy_stress_tensor
domain: continuum-mechanics
license: CC-BY-SA-4.0
tags: continuum mechanics, stress tensor, constitutive equation, deformation gradient
fetched: 2026-07-02
---

# Cauchy stress tensor

In continuum mechanics, the **Cauchy stress tensor** (symbol ⁠ ${\boldsymbol {\sigma }}$ ⁠, named after Augustin-Louis Cauchy), also called **true stress tensor** or simply **stress tensor**, completely defines the state of stress at a point inside a material in the deformed state, placement, or configuration. The second order tensor consists of nine components $\sigma _{ij}$ and relates a unit-length direction vector **e** to the *traction vector* **T**(**e**) across a surface perpendicular to **e**:

$\mathbf {T} ^{(\mathbf {e} )}=\mathbf {e} \cdot {\boldsymbol {\sigma }}\quad {\text{or}}\quad T_{j}^{(\mathbf {e} )}=\sum _{i}\sigma _{ij}e_{i}.$

The SI unit of both stress tensor and traction vector is the newton per square metre (N/m2) or pascal (Pa), corresponding to the stress scalar. The unit vector is dimensionless.

The Cauchy stress tensor obeys the tensor transformation law under a change in the system of coordinates. A graphical representation of two-dimensional coordinate transformations Mohr's circle for stress.

The Cauchy stress tensor is used for stress analysis of material bodies experiencing small deformations: it is a central concept in the linear theory of elasticity. For large deformations, also called finite deformations, other measures of stress are required, such as the Piola–Kirchhoff stress tensor, the Biot stress tensor, and the Kirchhoff stress tensor.

According to the principle of conservation of linear momentum, if the continuum body is in static equilibrium it can be demonstrated that the components of the Cauchy stress tensor in every material point in the body satisfy the equilibrium equations (Cauchy's equations of motion for zero acceleration). At the same time, according to the principle of conservation of angular momentum, equilibrium requires that the summation of moments with respect to an arbitrary point is zero, which leads to the conclusion that the stress tensor is symmetric, thus having only six independent stress components, instead of the original nine. However, in the presence of couple-stresses, i.e. moments per unit volume, the stress tensor is non-symmetric. This also is the case when the Knudsen number is close to one, ⁠ $K_{n}\rightarrow 1$ ⁠, or the continuum is a non-Newtonian fluid, which can lead to rotationally non-invariant fluids, such as polymers.

There are certain invariants associated with the stress tensor, whose values do not depend upon the coordinate system chosen, or the area element upon which the stress tensor operates. These are the three eigenvalues of the stress tensor, which are called the principal stresses.

## Euler–Cauchy stress principle – stress vector

The **Euler–Cauchy stress principle** states that *upon any surface that divides the body, the action of one part of the body on the other is equivalent (equipollent) to the system of distributed forces and couples on the surface dividing the body*, and it is represented by a field ⁠ $\mathbf {T} ^{(\mathbf {n} )}$ ⁠, called the **traction vector**, defined on the surface S and assumed to depend continuously on the surface's normal unit vector ⁠ $\mathbf {n}$ ⁠.

To formulate the Euler–Cauchy stress principle, consider a surface S passing through an internal material point P dividing the continuous body into two segments, as seen in Figure 2.1a or 2.1b (one may use either the cutting plane diagram or the diagram with the arbitrary volume inside the continuum enclosed by the surface ⁠ S ⁠).

Following the classical dynamics of Newton and Euler, the motion of a material body is produced by the action of externally applied forces which are assumed to be of two kinds: surface forces $\mathbf {F}$ and body forces ⁠ $\mathbf {b}$ ⁠. Thus, the total force ${\mathcal {F}}$ applied to a body or to a portion of the body can be expressed as:

${\mathcal {F}}=\mathbf {b} +\mathbf {F}$

Only surface forces will be discussed in this article as they are relevant to the Cauchy stress tensor.

When the body is subjected to external surface forces or *contact forces* ⁠ $\mathbf {F}$ ⁠, following Euler's equations of motion, internal contact forces and moments are transmitted from point to point in the body, and from one segment to the other through the dividing surface ⁠ S ⁠, due to the mechanical contact of one portion of the continuum onto the other (Figure 2.1a and 2.1b). On an element of area $\Delta S$ containing P , with normal vector ⁠ $\mathbf {n}$ ⁠, the force distribution is equipollent to a contact force $\Delta \mathbf {F}$ exerted at point P and surface moment $\Delta \mathbf {M}$ . In particular, the contact force is given by

$\Delta \mathbf {F} =\mathbf {T} ^{(\mathbf {n} )}\,\Delta S,$

where $\mathbf {T} ^{(\mathbf {n} )}$ is the *mean surface traction*.

Cauchy's stress principle asserts that as $\Delta S$ tends to zero the ratio $\Delta \mathbf {F} /\Delta S$ becomes $d\mathbf {F} /dS$ and the couple stress vector $\Delta \mathbf {M}$ vanishes. In specific fields of continuum mechanics the couple stress is assumed not to vanish; however, classical branches of continuum mechanics address non-polar materials which do not consider couple stresses and body moments.

The resultant vector $d\mathbf {F} /dS$ is defined as the *surface traction*, also called *stress vector*, *traction*, or *traction vector*. given by $\mathbf {T} ^{(\mathbf {n} )}=T_{i}^{(\mathbf {n} )}\mathbf {e} _{i}$ at the point P associated with a plane with a normal vector ⁠ $\mathbf {n}$ ⁠:

$T_{i}^{(\mathbf {n} )}=\lim _{\Delta S\to 0}{\frac {\Delta F_{i}}{\Delta S}}={dF_{i} \over dS}.$

This equation means that the stress vector depends on its location in the body and the orientation of the plane on which it is acting.

This implies that the balancing action of internal contact forces generates a *contact force density* or *Cauchy traction field* $\mathbf {T} (\mathbf {n} ,\mathbf {x} ,t)$ that represents a distribution of internal contact forces throughout the volume of the body in a particular configuration of the body at a given time ⁠ t ⁠. It is not a vector field because it depends not only on the position $\mathbf {x}$ of a particular material point, but also on the local orientation of the surface element as defined by its normal vector ⁠ $\mathbf {n}$ ⁠.

Depending on the orientation of the plane under consideration, the stress vector may not necessarily be perpendicular to that plane, *i.e.* parallel to ⁠ $\mathbf {n}$ ⁠, and can be resolved into two components (Figure 2.1c):

- one normal to the plane, called *normal stress* $\mathbf {\sigma _{\mathrm {n} }} =\lim _{\Delta S\to 0}{\frac {\Delta F_{\mathrm {n} }}{\Delta S}}={\frac {dF_{\mathrm {n} }}{dS}},$

where

$dF_{\mathrm {n} }$

is the normal component of the force

$d\mathbf {F}$

to the differential area

$dS$

- and the other parallel to this plane, called the *shear stress* $\mathbf {\tau } =\lim _{\Delta S\to 0}{\frac {\Delta F_{\mathrm {s} }}{\Delta S}}={\frac {dF_{\mathrm {s} }}{dS}},$

where

$dF_{\mathrm {s} }$

is the tangential component of the force

$d\mathbf {F}$

to the differential surface area

⁠

$dS$

⁠

. The shear stress can be further decomposed into two mutually perpendicular vectors.

### Cauchy's postulate

According to the *Cauchy Postulate*, the stress vector $\mathbf {T} ^{(\mathbf {n} )}$ remains unchanged for all surfaces passing through the point P and having the same normal vector $\mathbf {n}$ at ⁠ P ⁠, i.e., having a common tangent at ⁠ P ⁠. This means that the stress vector is a function of the normal vector $\mathbf {n}$ only, and is not influenced by the curvature of the internal surfaces.

### Cauchy's fundamental lemma

A consequence of Cauchy's postulate is *Cauchy's Fundamental Lemma*, also called the *Cauchy reciprocal theorem*, which states that the stress vectors acting on opposite sides of the same surface are equal in magnitude and opposite in direction. Cauchy's fundamental lemma is equivalent to Newton's third law of motion of action and reaction, and is expressed as

$-\mathbf {T} ^{(\mathbf {n} )}=\mathbf {T} ^{(-\mathbf {n} )}.$

## Cauchy's stress theorem—stress tensor

*The state of stress at a point* in the body is then defined by all the stress vectors **T**(**n**) associated with all planes (infinite in number) that pass through that point. However, according to *Cauchy's fundamental theorem*, also called *Cauchy's stress theorem*, merely by knowing the stress vectors on three mutually perpendicular planes, the stress vector on any other plane passing through that point can be found through coordinate transformation equations.

Cauchy's stress theorem states that there exists a second-order tensor field **σ**(**x**, t), called the Cauchy stress tensor, independent of **n**, such that **T** is a linear function of **n**:

$\mathbf {T} ^{(\mathbf {n} )}=\mathbf {n} \cdot {\boldsymbol {\sigma }}\quad {\text{or}}\quad T_{j}^{(\mathbf {n} )}=\sigma _{ij}n_{i}.$

This equation implies that the stress vector **T**(**n**) at any point *P* in a continuum associated with a plane with normal unit vector **n** can be expressed as a function of the stress vectors on the planes perpendicular to the coordinate axes, *i.e.* in terms of the components *σij* of the stress tensor **σ**.

To prove this expression, consider a tetrahedron with three faces oriented in the coordinate planes, and with an infinitesimal area d*A* oriented in an arbitrary direction specified by a normal unit vector **n** (Figure 2.2). The tetrahedron is formed by slicing the infinitesimal element along an arbitrary plane with unit normal **n**. The stress vector on this plane is denoted by **T**(**n**). The stress vectors acting on the faces of the tetrahedron are denoted as **T**(**e**1), **T**(**e**2), and **T**(**e**3), and are by definition the components *σij* of the stress tensor **σ**. This tetrahedron is sometimes called the *Cauchy tetrahedron*. The equilibrium of forces, *i.e.* Euler's first law of motion (Newton's second law of motion), gives:

$\mathbf {T} ^{(\mathbf {n} )}\,dA-\mathbf {T} ^{(\mathbf {e} _{1})}\,dA_{1}-\mathbf {T} ^{(\mathbf {e} _{2})}\,dA_{2}-\mathbf {T} ^{(\mathbf {e} _{3})}\,dA_{3}=\rho \left({\frac {h}{3}}dA\right)\mathbf {a} ,$

where the right-hand-side represents the product of the mass enclosed by the tetrahedron and its acceleration: *ρ* is the density, **a** is the acceleration, and *h* is the height of the tetrahedron, considering the plane **n** as the base. The area of the faces of the tetrahedron perpendicular to the axes can be found by projecting d*A* into each face (using the dot product):

$dA_{1}=\left(\mathbf {n} \cdot \mathbf {e} _{1}\right)dA=n_{1}\;dA,$

$dA_{2}=\left(\mathbf {n} \cdot \mathbf {e} _{2}\right)dA=n_{2}\;dA,$

$dA_{3}=\left(\mathbf {n} \cdot \mathbf {e} _{3}\right)dA=n_{3}\;dA,$

and then substituting into the equation to cancel out d*A*:

$\mathbf {T} ^{(\mathbf {n} )}-\mathbf {T} ^{(\mathbf {e} _{1})}n_{1}-\mathbf {T} ^{(\mathbf {e} _{2})}n_{2}-\mathbf {T} ^{(\mathbf {e} _{3})}n_{3}=\rho \left({\frac {h}{3}}\right)\mathbf {a} .$

To consider the limiting case as the tetrahedron shrinks to a point, *h* must go to 0 (intuitively, the plane **n** is translated along **n** toward *O*). As a result, the right-hand-side of the equation approaches 0, so

$\mathbf {T} ^{(\mathbf {n} )}=\mathbf {T} ^{(\mathbf {e} _{1})}n_{1}+\mathbf {T} ^{(\mathbf {e} _{2})}n_{2}+\mathbf {T} ^{(\mathbf {e} _{3})}n_{3}.$

Assuming a material element (see figure at the top of the page) with planes perpendicular to the coordinate axes of a Cartesian coordinate system, the stress vectors associated with each of the element planes, *i.e.* **T**(**e**1), **T**(**e**2), and **T**(**e**3) can be decomposed into a normal component and two shear components, *i.e.* components in the direction of the three coordinate axes. For the particular case of a surface with normal unit vector oriented in the direction of the *x*1-axis, denote the normal stress by *σ*11, and the two shear stresses as *σ*12 and *σ*13:

$\mathbf {T} ^{(\mathbf {e} _{1})}=T_{1}^{(\mathbf {e} _{1})}\mathbf {e} _{1}+T_{2}^{(\mathbf {e} _{1})}\mathbf {e} _{2}+T_{3}^{(\mathbf {e} _{1})}\mathbf {e} _{3}=\sigma _{11}\mathbf {e} _{1}+\sigma _{12}\mathbf {e} _{2}+\sigma _{13}\mathbf {e} _{3},$

$\mathbf {T} ^{(\mathbf {e} _{2})}=T_{1}^{(\mathbf {e} _{2})}\mathbf {e} _{1}+T_{2}^{(\mathbf {e} _{2})}\mathbf {e} _{2}+T_{3}^{(\mathbf {e} _{2})}\mathbf {e} _{3}=\sigma _{21}\mathbf {e} _{1}+\sigma _{22}\mathbf {e} _{2}+\sigma _{23}\mathbf {e} _{3},$

$\mathbf {T} ^{(\mathbf {e} _{3})}=T_{1}^{(\mathbf {e} _{3})}\mathbf {e} _{1}+T_{2}^{(\mathbf {e} _{3})}\mathbf {e} _{2}+T_{3}^{(\mathbf {e} _{3})}\mathbf {e} _{3}=\sigma _{31}\mathbf {e} _{1}+\sigma _{32}\mathbf {e} _{2}+\sigma _{33}\mathbf {e} _{3},$

In index notation this is

$\mathbf {T} ^{(\mathbf {e} _{i})}=T_{j}^{(\mathbf {e} _{i})}\mathbf {e} _{j}=\sigma _{ij}\mathbf {e} _{j}.$

The nine components *σij* of the stress vectors are the components of a second-order Cartesian tensor called the *Cauchy stress tensor*, which can be used to completely define the state of stress at a point and is given by

${\boldsymbol {\sigma }}=\sigma _{ij}=\left[{\begin{matrix}\mathbf {T} ^{(\mathbf {e} _{1})}\\\mathbf {T} ^{(\mathbf {e} _{2})}\\\mathbf {T} ^{(\mathbf {e} _{3})}\\\end{matrix}}\right]=\left[{\begin{matrix}\sigma _{11}&\sigma _{12}&\sigma _{13}\\\sigma _{21}&\sigma _{22}&\sigma _{23}\\\sigma _{31}&\sigma _{32}&\sigma _{33}\\\end{matrix}}\right]\equiv \left[{\begin{matrix}\sigma _{xx}&\sigma _{xy}&\sigma _{xz}\\\sigma _{yx}&\sigma _{yy}&\sigma _{yz}\\\sigma _{zx}&\sigma _{zy}&\sigma _{zz}\\\end{matrix}}\right]\equiv \left[{\begin{matrix}\sigma _{x}&\tau _{xy}&\tau _{xz}\\\tau _{yx}&\sigma _{y}&\tau _{yz}\\\tau _{zx}&\tau _{zy}&\sigma _{z}\\\end{matrix}}\right],$

where *σ*11, *σ*22, and *σ*33 are normal stresses, and *σ*12, *σ*13, *σ*21, *σ*23, *σ*31, and *σ*32 are shear stresses. The first index *i* indicates that the stress acts on a plane normal to the *Xi* -axis, and the second index *j* denotes the direction in which the stress acts (for example, *σ*12 implies that the stress is acting on the plane that is normal to the 1st axis i.e., *X*1, and acts along the 2nd axis i.e., *X*2). A stress component is positive if it acts in the positive direction of the coordinate axes, and if the plane where it acts has an outward normal vector pointing in the positive coordinate direction.

Thus, using the components of the stress tensor

${\begin{aligned}\mathbf {T} ^{(\mathbf {n} )}&=\mathbf {T} ^{(\mathbf {e} _{1})}n_{1}+\mathbf {T} ^{(\mathbf {e} _{2})}n_{2}+\mathbf {T} ^{(\mathbf {e} _{3})}n_{3}\\&=\sum _{i=1}^{3}\mathbf {T} ^{(\mathbf {e} _{i})}n_{i}\\&=\left(\sigma _{ij}\mathbf {e} _{j}\right)n_{i}\\&=\sigma _{ij}n_{i}\mathbf {e} _{j}\end{aligned}}$

or, equivalently,

$T_{j}^{(\mathbf {n} )}=\sigma _{ij}n_{i}.$

Alternatively, in matrix form we have

$\left[{\begin{matrix}T_{1}^{(\mathbf {n} )}&T_{2}^{(\mathbf {n} )}&T_{3}^{(\mathbf {n} )}\end{matrix}}\right]=\left[{\begin{matrix}n_{1}&n_{2}&n_{3}\end{matrix}}\right]\cdot \left[{\begin{matrix}\sigma _{11}&\sigma _{12}&\sigma _{13}\\\sigma _{21}&\sigma _{22}&\sigma _{23}\\\sigma _{31}&\sigma _{32}&\sigma _{33}\\\end{matrix}}\right].$

The Voigt notation representation of the Cauchy stress tensor takes advantage of the symmetry of the stress tensor to express the stress as a six-dimensional vector of the form:

${\boldsymbol {\sigma }}={\begin{bmatrix}\sigma _{1}&\sigma _{2}&\sigma _{3}&\sigma _{4}&\sigma _{5}&\sigma _{6}\end{bmatrix}}^{\textsf {T}}\equiv {\begin{bmatrix}\sigma _{11}&\sigma _{22}&\sigma _{33}&\sigma _{23}&\sigma _{13}&\sigma _{12}\end{bmatrix}}^{\textsf {T}}.$

The Voigt notation is used extensively in representing stress–strain relations in solid mechanics and for computational efficiency in numerical structural mechanics software.

### Transformation rule of the stress tensor

It can be shown that the stress tensor is a contravariant second order tensor, which is a statement of how it transforms under a change of the coordinate system. From an *xi*-system to an *xi'*-system, the components *σij* in the initial system are transformed into the components *σij*′ in the new system according to the tensor transformation rule (Figure 2.4):

$\sigma '_{ij}=a_{im}a_{jn}\sigma _{mn}\quad {\text{or}}\quad {\boldsymbol {\sigma }}'=\mathbf {A} {\boldsymbol {\sigma }}\mathbf {A} ^{\textsf {T}},$

where **A** is a rotation matrix with components *aij*. In matrix form this is

$\left[{\begin{matrix}\sigma '_{11}&\sigma '_{12}&\sigma '_{13}\\\sigma '_{21}&\sigma '_{22}&\sigma '_{23}\\\sigma '_{31}&\sigma '_{32}&\sigma '_{33}\\\end{matrix}}\right]=\left[{\begin{matrix}a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33}\\\end{matrix}}\right]\left[{\begin{matrix}\sigma _{11}&\sigma _{12}&\sigma _{13}\\\sigma _{21}&\sigma _{22}&\sigma _{23}\\\sigma _{31}&\sigma _{32}&\sigma _{33}\\\end{matrix}}\right]\left[{\begin{matrix}a_{11}&a_{21}&a_{31}\\a_{12}&a_{22}&a_{32}\\a_{13}&a_{23}&a_{33}\\\end{matrix}}\right].$

Expanding the matrix operation, and simplifying terms using the symmetry of the stress tensor, gives

${\begin{aligned}\sigma _{11}'={}&a_{11}^{2}\sigma _{11}+a_{12}^{2}\sigma _{22}+a_{13}^{2}\sigma _{33}+2a_{11}a_{12}\sigma _{12}+2a_{11}a_{13}\sigma _{13}+2a_{12}a_{13}\sigma _{23},\\\sigma _{22}'={}&a_{21}^{2}\sigma _{11}+a_{22}^{2}\sigma _{22}+a_{23}^{2}\sigma _{33}+2a_{21}a_{22}\sigma _{12}+2a_{21}a_{23}\sigma _{13}+2a_{22}a_{23}\sigma _{23},\\\sigma _{33}'={}&a_{31}^{2}\sigma _{11}+a_{32}^{2}\sigma _{22}+a_{33}^{2}\sigma _{33}+2a_{31}a_{32}\sigma _{12}+2a_{31}a_{33}\sigma _{13}+2a_{32}a_{33}\sigma _{23},\\\sigma _{12}'={}&a_{11}a_{21}\sigma _{11}+a_{12}a_{22}\sigma _{22}+a_{13}a_{23}\sigma _{33}\\&+(a_{11}a_{22}+a_{12}a_{21})\sigma _{12}+(a_{12}a_{23}+a_{13}a_{22})\sigma _{23}+(a_{11}a_{23}+a_{13}a_{21})\sigma _{13},\\\sigma _{23}'={}&a_{21}a_{31}\sigma _{11}+a_{22}a_{32}\sigma _{22}+a_{23}a_{33}\sigma _{33}\\&+(a_{21}a_{32}+a_{22}a_{31})\sigma _{12}+(a_{22}a_{33}+a_{23}a_{32})\sigma _{23}+(a_{21}a_{33}+a_{23}a_{31})\sigma _{13},\\\sigma _{13}'={}&a_{11}a_{31}\sigma _{11}+a_{12}a_{32}\sigma _{22}+a_{13}a_{33}\sigma _{33}\\&+(a_{11}a_{32}+a_{12}a_{31})\sigma _{12}+(a_{12}a_{33}+a_{13}a_{32})\sigma _{23}+(a_{11}a_{33}+a_{13}a_{31})\sigma _{13}.\end{aligned}}$

The Mohr circle for stress is a graphical representation of this transformation of stresses.

### Normal and shear stresses

The magnitude of the normal stress component *σ*n of any stress vector **T**(**n**) acting on an arbitrary plane with normal unit vector **n** at a given point, in terms of the components *σij* of the stress tensor **σ**, is the dot product of the stress vector and the normal unit vector:

${\begin{aligned}\sigma _{\mathrm {n} }&=\mathbf {T} ^{(\mathbf {n} )}\cdot \mathbf {n} \\&=T_{i}^{(\mathbf {n} )}n_{i}\\&=\sigma _{ij}n_{i}n_{j}.\end{aligned}}$

The magnitude of the shear stress component *τ*n, acting orthogonal to the vector **n**, can then be found using the Pythagorean theorem:

${\begin{aligned}\tau _{\mathrm {n} }&={\sqrt {\left(T^{(\mathbf {n} )}\right)^{2}-\sigma _{\mathrm {n} }^{2}}}\\&={\sqrt {T_{i}^{(\mathbf {n} )}T_{i}^{(\mathbf {n} )}-\sigma _{\mathrm {n} }^{2}}},\end{aligned}}$

where

$\left(T^{(\mathbf {n} )}\right)^{2}=T_{i}^{(\mathbf {n} )}T_{i}^{(\mathbf {n} )}=\left(\sigma _{ij}n_{j}\right)\left(\sigma _{ik}n_{k}\right)=\sigma _{ij}\sigma _{ik}n_{j}n_{k}.$

## Balance laws – Cauchy's equations of motion

### Cauchy's first law of motion

According to the principle of conservation of linear momentum, if the continuum body is in static equilibrium it can be demonstrated that the components of the Cauchy stress tensor in every material point in the body satisfy the equilibrium equations:

$\sigma _{ji,j}+F_{i}=0,$

where $\sigma _{ji,j}=\sum _{j}\partial _{j}\sigma _{ji}$

For example, for a hydrostatic fluid in equilibrium conditions, the stress tensor takes on the form:

${\sigma _{ij}}=-p{\delta _{ij}},$

where p is the hydrostatic pressure, and ${\delta _{ij}}\$ is the Kronecker delta.

| Derivation of equilibrium equations |
|---|
| Consider a continuum body (see Figure 4) occupying a volume V , having a surface area ⁠ S ⁠, with defined traction or surface forces $T_{i}^{(n)}$ per unit area acting on every point of the body surface, and body forces $F_{i}$ per unit of volume on every point within the volume V . Thus, if the body is in equilibrium the resultant force acting on the volume is zero, thus: $\int _{S}T_{i}^{(n)}dS+\int _{V}F_{i}dV=0$ By definition the stress vector is $T_{i}^{(n)}=\sigma _{ji}n_{j}$ , then $\int _{S}\sigma _{ji}n_{j}\,dS+\int _{V}F_{i}\,dV=0$ Using the Gauss's divergence theorem to convert a surface integral to a volume integral gives $\int _{V}\sigma _{ji,j}\,dV+\int _{V}F_{i}\,dV=0$ $\int _{V}(\sigma _{ji,j}+F_{i}\,)dV=0$ For an arbitrary volume the integral vanishes, and we have the *equilibrium equations* $\sigma _{ji,j}+F_{i}=0$ |

### Cauchy's second law of motion

According to the principle of conservation of angular momentum, equilibrium requires that the summation of moments with respect to an arbitrary point is zero, which leads to the conclusion that the stress tensor is symmetric, thus having only six independent stress components, instead of the original nine:

$\sigma _{ij}=\sigma _{ji}$

| Derivation of symmetry of the stress tensor |
|---|
| Summing moments about point *O* (Figure 4) the resultant moment is zero as the body is in equilibrium. Thus, ${\begin{aligned}M_{O}&=\int _{S}(\mathbf {r} \times \mathbf {T} )dS+\int _{V}(\mathbf {r} \times \mathbf {F} )dV=0\\0&=\int _{S}\varepsilon _{ijk}x_{j}T_{k}^{(n)}dS+\int _{V}\varepsilon _{ijk}x_{j}F_{k}dV\\\end{aligned}}$ where $\mathbf {r}$ is the position vector and is expressed as $\mathbf {r} =x_{j}\mathbf {e} _{j}$ and $\varepsilon _{ijk}$ is the Levi-Civita symbol. Knowing that $T_{k}^{(n)}=\sigma _{mk}n_{m}$ and using Gauss's divergence theorem to change from a surface integral to a volume integral, we have ${\begin{aligned}0&=\int _{S}\varepsilon _{ijk}x_{j}\sigma _{mk}n_{m}\,dS+\int _{V}\varepsilon _{ijk}x_{j}F_{k}\,dV\\&=\int _{V}(\varepsilon _{ijk}x_{j}\sigma _{mk})_{,m}dV+\int _{V}\varepsilon _{ijk}x_{j}F_{k}\,dV\\&=\int _{V}(\varepsilon _{ijk}x_{j,m}\sigma _{mk}+\varepsilon _{ijk}x_{j}\sigma _{mk,m})dV+\int _{V}\varepsilon _{ijk}x_{j}F_{k}\,dV\\&=\int _{V}(\varepsilon _{ijk}x_{j,m}\sigma _{mk})dV+\int _{V}\varepsilon _{ijk}x_{j}(\sigma _{mk,m}+F_{k})dV\\\end{aligned}}$ The second integral is zero as it contains the equilibrium equations. This leaves the first integral, where $x_{j,m}=\delta _{jm}$ , therefore $\int _{V}(\varepsilon _{ijk}\sigma _{jk})dV=0$ For an arbitrary volume V, we then have $\varepsilon _{ijk}\sigma _{jk}=0,$ which is satisfied at every point within the body. Expanding this equation we have $\sigma _{12}=\sigma _{21}$ , $\sigma _{23}=\sigma _{32}$ , and $\sigma _{13}=\sigma _{31}$ or in general $\sigma _{ij}=\sigma _{ji}$ This proves that the stress tensor is symmetric |

However, in the presence of couple-stresses, i.e. moments per unit volume, the stress tensor is non-symmetric. This also is the case when the Knudsen number is close to one, ⁠ $K_{n}\rightarrow 1$ ⁠, or the continuum is a non-Newtonian fluid, which can lead to rotationally non-invariant fluids, such as polymers.

## Principal stresses and stress invariants

At every point in a stressed body there are at least three planes, called *principal planes*, with normal vectors ⁠ $\mathbf {n}$ ⁠, called *principal directions*, where the corresponding stress vector is perpendicular to the plane, i.e., parallel or in the same direction as the normal vector ⁠ $\mathbf {n}$ ⁠, and where there are no normal shear stresses ⁠ $\tau _{\mathrm {n} }$ ⁠. The three stresses normal to these principal planes are called *principal stresses*.

The components $\sigma _{ij}$ of the stress tensor depend on the orientation of the coordinate system at the point under consideration. However, the stress tensor itself is a physical quantity and as such, it is independent of the coordinate system chosen to represent it. There are certain invariants associated with every tensor which are also independent of the coordinate system. For example, a vector is a simple tensor of rank one. In three dimensions, it has three components. The value of these components will depend on the coordinate system chosen to represent the vector, but the magnitude of the vector is a physical quantity (a scalar) and is independent of the Cartesian coordinate system chosen to represent the vector (so long as it is normal). Similarly, every second rank tensor (such as the stress and the strain tensors) has three independent invariant quantities associated with it. One set of such invariants are the principal stresses of the stress tensor, which are just the eigenvalues of the stress tensor. Their direction vectors are the principal directions or eigenvectors.

A stress vector parallel to the normal unit vector $\mathbf {n}$ is given by:

$\mathbf {T} ^{(\mathbf {n} )}=\lambda \mathbf {n} =\mathbf {\sigma } _{\mathrm {n} }\mathbf {n} ,$

where $\lambda$ is a constant of proportionality, and in this particular case corresponds to the magnitudes $\sigma _{\mathrm {n} }$ of the normal stress vectors or principal stresses.

Knowing that $T_{i}^{(n)}=\sigma _{ij}n_{j}$ and ⁠ ${1}$ ⁠, we have

${\begin{aligned}T_{i}^{(n)}&=\lambda n_{i}\\\sigma _{ij}n_{j}&=\lambda n_{i}\\\sigma _{ij}n_{j}-\lambda n_{i}&=0\\\left(\sigma _{ij}-\lambda \delta _{ij}\right)n_{j}&=0\\\end{aligned}}$

This is a homogeneous system, i.e. equal to zero, of three linear equations where $n_{j}$ are the unknowns. To obtain a nontrivial (non-zero) solution for ⁠ $n_{j}$ ⁠, the matrix determinant of the coefficients must be equal to zero, i.e. the system is singular. Thus,

$\left|\sigma _{ij}-\lambda \delta _{ij}\right|={\begin{vmatrix}\sigma _{11}-\lambda &\sigma _{12}&\sigma _{13}\\\sigma _{21}&\sigma _{22}-\lambda &\sigma _{23}\\\sigma _{31}&\sigma _{32}&\sigma _{33}-\lambda \\\end{vmatrix}}=0$

Expanding the determinant leads to the *characteristic equation*

$\left|\sigma _{ij}-\lambda \delta _{ij}\right|=-\lambda ^{3}+I_{1}\lambda ^{2}-I_{2}\lambda +I_{3}=0$

where

${\begin{aligned}I_{1}&=\sigma _{11}+\sigma _{22}+\sigma _{33}\\&=\sigma _{kk}={\text{tr}}({\boldsymbol {\sigma }})\\[4pt]I_{2}&={\begin{vmatrix}\sigma _{22}&\sigma _{23}\\\sigma _{32}&\sigma _{33}\\\end{vmatrix}}+{\begin{vmatrix}\sigma _{11}&\sigma _{13}\\\sigma _{31}&\sigma _{33}\\\end{vmatrix}}+{\begin{vmatrix}\sigma _{11}&\sigma _{12}\\\sigma _{21}&\sigma _{22}\\\end{vmatrix}}\\&=\sigma _{11}\sigma _{22}+\sigma _{22}\sigma _{33}+\sigma _{11}\sigma _{33}-\sigma _{12}^{2}-\sigma _{23}^{2}-\sigma _{31}^{2}\\&={\frac {1}{2}}\left(\sigma _{ii}\sigma _{jj}-\sigma _{ij}\sigma _{ji}\right)={\frac {1}{2}}\left[\left({\text{tr}}({\boldsymbol {\sigma }})\right)^{2}-{\text{tr}}\left({\boldsymbol {\sigma }}^{2}\right)\right]\\[4pt]I_{3}&=\det(\sigma _{ij})=\det({\boldsymbol {\sigma }})\\&=\sigma _{11}\sigma _{22}\sigma _{33}+2\sigma _{12}\sigma _{23}\sigma _{31}-\sigma _{12}^{2}\sigma _{33}-\sigma _{23}^{2}\sigma _{11}-\sigma _{31}^{2}\sigma _{22}\\\end{aligned}}$

The characteristic equation has three real roots $\lambda _{i}$ (i.e. with a zero imaginary component) due to the stress tensor being symmetric. The $\sigma _{1}=\max \left(\lambda _{1},\lambda _{2},\lambda _{3}\right)$ , $\sigma _{3}=\min \left(\lambda _{1},\lambda _{2},\lambda _{3}\right)$ and ⁠ $\sigma _{2}=I_{1}-\sigma _{1}-\sigma _{3}$ ⁠, are the principal stresses, functions of the eigenvalues ⁠ $\lambda _{i}$ ⁠. The eigenvalues are the roots of the characteristic polynomial. The principal stresses are unique for a given stress tensor. Therefore, from the characteristic equation, the coefficients $I_{1}$ , $I_{2}$ and $I_{3}$ , called the first, second, and third *stress invariants*, respectively, always have the same value regardless of the coordinate system's orientation.

For each eigenvalue, there is a non-trivial solution for $n_{j}$ in the equation ⁠ $\left(\sigma _{ij}-\lambda \delta _{ij}\right)n_{j}=0$ ⁠. These solutions are the principal directions or eigenvectors defining the plane where the principal stresses act. The principal stresses and principal directions characterize the stress at a point and are independent of the orientation.

A coordinate system with axes oriented to the principal directions implies that the normal stresses are the principal stresses and the stress tensor is represented by a diagonal matrix:

$\sigma _{ij}={\begin{bmatrix}\sigma _{1}&0&0\\0&\sigma _{2}&0\\0&0&\sigma _{3}\end{bmatrix}}$

The principal stresses can be combined to form the stress invariants, ⁠ $I_{1}$ ⁠, ⁠ $I_{2}$ ⁠, and ⁠ $I_{3}$ ⁠. The first and third invariant are the trace and determinant respectively, of the stress tensor. Thus,

${\begin{aligned}I_{1}&=\sigma _{1}+\sigma _{2}+\sigma _{3}\\I_{2}&=\sigma _{1}\sigma _{2}+\sigma _{2}\sigma _{3}+\sigma _{3}\sigma _{1}\\I_{3}&=\sigma _{1}\sigma _{2}\sigma _{3}\\\end{aligned}}$

Because of its simplicity, the principal coordinate system is often useful when considering the state of the elastic medium at a particular point. Principal stresses are often expressed in the following equation for evaluating stresses in the x and y directions or axial and bending stresses on a part. The principal normal stresses can then be used to calculate the von Mises stress and ultimately the safety factor and margin of safety.

$\sigma _{1},\sigma _{2}={\frac {\sigma _{x}+\sigma _{y}}{2}}\pm {\sqrt {\left({\frac {\sigma _{x}-\sigma _{y}}{2}}\right)^{2}+\tau _{xy}^{2}}}.$

Using just the part of the equation under the square root is equal to the maximum and minimum shear stress for plus and minus. This is shown as:

$\tau _{\max },\tau _{\min }=\pm {\sqrt {\left({\frac {\sigma _{x}-\sigma _{y}}{2}}\right)^{2}+\tau _{xy}^{2}}}.$

## Maximum and minimum shear stresses

The maximum shear stress or maximum principal shear stress is equal to one-half the difference between the largest and smallest principal stresses, and acts on the plane that bisects the angle between the directions of the largest and smallest principal stresses, i.e. the plane of the maximum shear stress is oriented $45^{\circ }$ from the principal stress planes. The maximum shear stress is expressed as

$\tau _{\max }={\frac {1}{2}}\left|\sigma _{\max }-\sigma _{\min }\right|.$

Assuming $\sigma _{1}\geq \sigma _{2}\geq \sigma _{3}$ then

$\tau _{\max }={\frac {1}{2}}\left|\sigma _{1}-\sigma _{3}\right|$

When the stress tensor is non-zero the normal stress component acting on the plane for the maximum shear stress is non-zero and it is equal to

$\sigma _{\text{n}}={\frac {1}{2}}\left(\sigma _{1}+\sigma _{3}\right).$

| Derivation of the maximum and minimum shear stresses |
|---|
| The normal stress can be written in terms of principal stresses $(\sigma _{1}\geq \sigma _{2}\geq \sigma _{3})$ as ${\begin{aligned}\sigma _{\mathrm {n} }&=\sigma _{ij}n_{i}n_{j}\\&=\sigma _{1}n_{1}^{2}+\sigma _{2}n_{2}^{2}+\sigma _{3}n_{3}^{2}\\\end{aligned}}$ Knowing that ⁠ $\left(T^{(n)}\right)^{2}=\sigma _{ij}\sigma _{ik}n_{j}n_{k}$ ⁠, the shear stress in terms of principal stresses components is expressed as ${\begin{aligned}\tau _{\text{n}}^{2}&=\left(T^{(n)}\right)^{2}-\sigma _{\text{n}}^{2}\\&=\sigma _{1}^{2}n_{1}^{2}+\sigma _{2}^{2}n_{2}^{2}+\sigma _{3}^{2}n_{3}^{2}-\left(\sigma _{1}n_{1}^{2}+\sigma _{2}n_{2}^{2}+\sigma _{3}n_{3}^{2}\right)^{2}\\&=\left(\sigma _{1}^{2}-\sigma _{2}^{2}\right)n_{1}^{2}+\left(\sigma _{2}^{2}-\sigma _{3}^{2}\right)n_{2}^{2}+\sigma _{3}^{2}-\left[\left(\sigma _{1}-\sigma _{3}\right)n_{1}^{2}+\left(\sigma _{2}-\sigma _{3}\right)n_{2}^{2}+\sigma _{3}\right]^{2}\\&=(\sigma _{1}-\sigma _{2})^{2}n_{1}^{2}n_{2}^{2}+(\sigma _{2}-\sigma _{3})^{2}n_{2}^{2}n_{3}^{2}+(\sigma _{1}-\sigma _{3})^{2}n_{1}^{2}n_{3}^{2}\\\end{aligned}}$ The maximum shear stress at a point in a continuum body is determined by maximizing $\tau _{\mathrm {n} }^{2}$ subject to the condition that $n_{i}n_{i}=n_{1}^{2}+n_{2}^{2}+n_{3}^{2}=1.$ This is a constrained maximization problem, which can be solved using the Lagrangian multiplier technique to convert the problem into an unconstrained optimization problem. Thus, the stationary values (maximum and minimum values)of $\tau _{\text{n}}^{2}$ occur where the gradient of $\tau _{\text{n}}^{2}$ is parallel to the gradient of ⁠ F ⁠. The Lagrangian function for this problem can be written as ${\begin{aligned}F\left(n_{1},n_{2},n_{3},\lambda \right)&=\tau ^{2}+\lambda \left(g\left(n_{1},n_{2},n_{3}\right)-1\right)\\&=\sigma _{1}^{2}n_{1}^{2}+\sigma _{2}^{2}n_{2}^{2}+\sigma _{3}^{2}n_{3}^{2}-\left(\sigma _{1}n_{1}^{2}+\sigma _{2}n_{2}^{2}+\sigma _{3}n_{3}^{2}\right)^{2}+\lambda \left(n_{1}^{2}+n_{2}^{2}+n_{3}^{2}-1\right)\\\end{aligned}}$ where $\lambda$ is the Lagrangian multiplier (which is different from the $\lambda$ use to denote eigenvalues). The extreme values of these functions are ${\frac {\partial F}{\partial n_{1}}}=0\qquad {\frac {\partial F}{\partial n_{2}}}=0\qquad {\frac {\partial F}{\partial n_{3}}}=0$ thence ${\frac {\partial F}{\partial n_{1}}}=n_{1}\sigma _{1}^{2}-2n_{1}\sigma _{1}\left(\sigma _{1}n_{1}^{2}+\sigma _{2}n_{2}^{2}+\sigma _{3}n_{3}^{2}\right)+\lambda n_{1}=0$ ${\frac {\partial F}{\partial n_{2}}}=n_{2}\sigma _{2}^{2}-2n_{2}\sigma _{2}\left(\sigma _{1}n_{1}^{2}+\sigma _{2}n_{2}^{2}+\sigma _{3}n_{3}^{2}\right)+\lambda n_{2}=0$ ${\frac {\partial F}{\partial n_{3}}}=n_{3}\sigma _{3}^{2}-2n_{3}\sigma _{3}\left(\sigma _{1}n_{1}^{2}+\sigma _{2}n_{2}^{2}+\sigma _{3}n_{3}^{2}\right)+\lambda n_{3}=0$ These three equations together with the condition $n_{i}n_{i}=1$ may be solved for ⁠ $\lambda$ ⁠, ⁠ $n_{1}$ ⁠, ⁠ $n_{2}$ ⁠, and ⁠ $n_{3}$ ⁠. By multiplying the first three equations by ⁠ $n_{1}$ ⁠, ⁠ $n_{2}$ ⁠, and ⁠ $n_{3}$ ⁠, respectively, and knowing that $\sigma _{\text{n}}=\sigma _{ij}n_{i}n_{j}=\sigma _{1}n_{1}^{2}+\sigma _{2}n_{2}^{2}+\sigma _{3}n_{3}^{2}$ we obtain $n_{1}^{2}\sigma _{1}^{2}-2\sigma _{1}n_{1}^{2}\sigma _{\text{n}}+n_{1}^{2}\lambda =0$ $n_{2}^{2}\sigma _{2}^{2}-2\sigma _{2}n_{2}^{2}\sigma _{\text{n}}+n_{2}^{2}\lambda =0$ $n_{3}^{2}\sigma _{3}^{2}-2\sigma _{1}n_{3}^{2}\sigma _{\text{n}}+n_{3}^{2}\lambda =0$ Adding these three equations we get ${\begin{aligned}\left[n_{1}^{2}\sigma _{1}^{2}+n_{2}^{2}\sigma _{2}^{2}+n_{3}^{2}\sigma _{3}^{2}\right]-2\left(\sigma _{1}n_{1}^{2}+\sigma _{2}n_{2}^{2}+\sigma _{3}n_{3}^{2}\right)\sigma _{\mathrm {n} }+\lambda \left(n_{1}^{2}+n_{2}^{2}+n_{3}^{2}\right)&=0\\\left[\tau _{\mathrm {n} }^{2}+\left(\sigma _{1}n_{1}^{2}+\sigma _{2}n_{2}^{2}+\sigma _{3}n_{3}^{2}\right)^{2}\right]-2\sigma _{\mathrm {n} }^{2}+\lambda &=0\\\left[\tau _{\mathrm {n} }^{2}+\sigma _{\mathrm {n} }^{2}\right]-2\sigma _{\mathrm {n} }^{2}+\lambda &=0\\\lambda &=\sigma _{\mathrm {n} }^{2}-\tau _{\mathrm {n} }^{2}\end{aligned}}$ This result can be substituted into each of the first three equations to obtain ${\begin{aligned}{\frac {\partial F}{\partial n_{1}}}=n_{1}\sigma _{1}^{2}-2n_{1}\sigma _{1}\left(\sigma _{1}n_{1}^{2}+\sigma _{2}n_{2}^{2}+\sigma _{3}n_{3}^{2}\right)+\left(\sigma _{\text{n}}^{2}-\tau _{\text{n}}^{2}\right)n_{1}&=0\\n_{1}\sigma _{1}^{2}-2n_{1}\sigma _{1}\sigma _{\text{n}}+\left(\sigma _{\text{n}}^{2}-\tau _{\text{n}}^{2}\right)n_{1}&=0\\\left(\sigma _{1}^{2}-2\sigma _{1}\sigma _{\text{n}}+\sigma _{\text{n}}^{2}-\tau _{\text{n}}^{2}\right)n_{1}&=0\\\end{aligned}}$ Doing the same for the other two equations we have ${\frac {\partial F}{\partial n_{2}}}=\left(\sigma _{2}^{2}-2\sigma _{2}\sigma _{\text{n}}+\sigma _{\text{n}}^{2}-\tau _{\text{n}}^{2}\right)n_{2}=0$ ${\frac {\partial F}{\partial n_{3}}}=\left(\sigma _{3}^{2}-2\sigma _{3}\sigma _{\text{n}}+\sigma _{\text{n}}^{2}-\tau _{\text{n}}^{2}\right)n_{3}=0$ A first approach to solve these last three equations is to consider the trivial solution ⁠ $n_{i}=0$ ⁠. However, this option does not fulfill the constraint ⁠ $n_{i}n_{i}=1$ ⁠. Considering the solution where $n_{1}=n_{2}=0$ and ⁠ $n_{3}\neq 0$ ⁠, it is determine from the condition $n_{i}n_{i}=1$ that ⁠ $n_{3}=\pm 1$ ⁠, then from the original equation for $\tau _{\text{n}}^{2}$ it is seen that ⁠ $\tau _{\text{n}}=0$ ⁠. The other two possible values for $\tau _{\text{n}}$ can be obtained similarly by assuming $n_{1}=n_{3}=0$ and $n_{2}\neq 0$ $n_{2}=n_{3}=0$ and $n_{1}\neq 0$ Thus, one set of solutions for these four equations is: ${\begin{aligned}n_{1}&=0,&n_{2}&=0,&n_{3}&=\pm 1,&\tau _{\text{n}}&=0\\n_{1}&=0,&n_{2}&=\pm 1,&n_{3}&=0,&\tau _{\text{n}}&=0\\n_{1}&=\pm 1,&n_{2}&=0,&n_{3}&=0,&\tau _{\text{n}}&=0\end{aligned}}$ These correspond to minimum values for $\tau _{\mathrm {n} }$ and verifies that there are no shear stresses on planes normal to the principal directions of stress, as shown previously. A second set of solutions is obtained by assuming ⁠ $n_{1}=0$ ⁠, ⁠ $n_{2}\neq 0$ ⁠ and ⁠ $n_{3}\neq 0$ ⁠. Thus we have ${\frac {\partial F}{\partial n_{2}}}=\sigma _{2}^{2}-2\sigma _{2}\sigma _{\text{n}}+\sigma _{\text{n}}^{2}-\tau _{\text{n}}^{2}=0$ ${\frac {\partial F}{\partial n_{3}}}=\sigma _{3}^{2}-2\sigma _{3}\sigma _{\text{n}}+\sigma _{\text{n}}^{2}-\tau _{\text{n}}^{2}=0$ To find the values for $n_{2}$ and $n_{3}$ we first add these two equations ${\begin{aligned}\sigma _{2}^{2}-\sigma _{3}^{2}-2\sigma _{2}\sigma _{\text{n}}+2\sigma _{3}\sigma _{\text{n}}&=0\\\sigma _{2}^{2}-\sigma _{3}^{2}-2\sigma _{\text{n}}\left(\sigma _{2}-\sigma _{3}\right)&=0\\\sigma _{2}+\sigma _{3}&=2\sigma _{\text{n}}\end{aligned}}$ Knowing that for $n_{1}=0$ $\sigma _{\text{n}}=\sigma _{1}n_{1}^{2}+\sigma _{2}n_{2}^{2}+\sigma _{3}n_{3}^{2}=\sigma _{2}n_{2}^{2}+\sigma _{3}n_{3}^{2}$ and $n_{1}^{2}+n_{2}^{2}+n_{3}^{2}=n_{2}^{2}+n_{3}^{2}=1$ we have ${\begin{aligned}\sigma _{2}+\sigma _{3}&=2\sigma _{\text{n}}\\\sigma _{2}+\sigma _{3}&=2\left(\sigma _{2}n_{2}^{2}+\sigma _{3}n_{3}^{2}\right)\\\sigma _{2}+\sigma _{3}&=2\left(\sigma _{2}n_{2}^{2}+\sigma _{3}\left(1-n_{2}^{2}\right)\right)=0\end{aligned}}$ and solving for $n_{2}$ we have $n_{2}=\pm {\frac {1}{\sqrt {2}}}$ Then solving for $n_{3}$ we have $n_{3}={\sqrt {1-n_{2}^{2}}}=\pm {\frac {1}{\sqrt {2}}}$ and ${\begin{aligned}\tau _{\text{n}}^{2}&=(\sigma _{2}-\sigma _{3})^{2}n_{2}^{2}n_{3}^{2}\\\tau _{\text{n}}&={\frac {\sigma _{2}-\sigma _{3}}{2}}\end{aligned}}$ The other two possible values for $\tau _{\text{n}}$ can be obtained similarly by assuming ⁠ $n_{2}=0$ ⁠, ⁠ $n_{1}\neq 0$ ⁠ and $n_{3}\neq 0$ ⁠ $n_{3}=0$ ⁠, ⁠ $n_{1}\neq 0$ ⁠ and $n_{2}\neq 0$ Therefore, the second set of solutions for ⁠ $\textstyle {\frac {\partial F}{\partial n_{1}}}=0$ ⁠, representing a maximum for $\tau _{\text{n}}$ is $n_{1}=0,\,\,n_{2}=\pm {\frac {1}{\sqrt {2}}},\,\,n_{3}=\pm {\frac {1}{\sqrt {2}}},\,\,\tau _{\text{n}}=\pm {\frac {\sigma _{2}-\sigma _{3}}{2}}$ $n_{1}=\pm {\frac {1}{\sqrt {2}}},\,\,n_{2}=0,\,\,n_{3}=\pm {\frac {1}{\sqrt {2}}},\,\,\tau _{\text{n}}=\pm {\frac {\sigma _{1}-\sigma _{3}}{2}}$ $n_{1}=\pm {\frac {1}{\sqrt {2}}},\,\,n_{2}=\pm {\frac {1}{\sqrt {2}}},\,\,n_{3}=0,\,\,\tau _{\text{n}}=\pm {\frac {\sigma _{1}-\sigma _{2}}{2}}$ Therefore, assuming ⁠ $\sigma _{1}\geq \sigma _{2}\geq \sigma _{3}$ ⁠, the maximum shear stress is expressed by $\tau _{\max }={\frac {1}{2}}\left\|\sigma _{1}-\sigma _{3}\right\|={\frac {1}{2}}\left\|\sigma _{\max }-\sigma _{\min }\right\|$ and it can be stated as being equal to one-half the difference between the largest and smallest principal stresses, acting on the plane that bisects the angle between the directions of the largest and smallest principal stresses. |

## Stress deviator tensor

The stress tensor $\sigma _{ij}$ can be expressed as the sum of two other stress tensors:

1. a *mean hydrostatic stress tensor* or *volumetric stress tensor* or *mean normal stress tensor*, ⁠ $\pi \delta _{ij}$ ⁠, which tends to change the volume of the stressed body; and
2. a deviatoric component called the *stress deviator tensor*, ⁠ $s_{ij}$ ⁠, which tends to distort it.

So

$\sigma _{ij}=s_{ij}+\pi \delta _{ij},$

where $\pi$ is the mean stress given by

$\pi ={\frac {\sigma _{kk}}{3}}={\frac {\sigma _{11}+\sigma _{22}+\sigma _{33}}{3}}={\frac {1}{3}}I_{1}.$

Pressure (⁠ p ⁠) is generally defined as negative one-third the trace of the stress tensor minus any stress the divergence of the velocity contributes with, i.e.

$p=\zeta \,\nabla \cdot {\vec {u}}-\pi =\zeta \,{\frac {\partial u_{k}}{\partial x_{k}}}-\pi =\sum _{k}\zeta \,{\frac {\partial u_{k}}{\partial x_{k}}}-\pi ,$

where $\zeta$ is a proportionality constant (viz. the Volume viscosity), $\nabla \cdot$ is the divergence operator, $x_{k}$ is the *k*th Cartesian coordinate, ${\vec {u}}$ is the flow velocity and $u_{k}$ is the *k*th Cartesian component of ⁠ ${\vec {u}}$ ⁠.

The deviatoric stress tensor can be obtained by subtracting the hydrostatic stress tensor from the Cauchy stress tensor:

${\begin{aligned}s_{ij}&=\sigma _{ij}-{\frac {\sigma _{kk}}{3}}\delta _{ij},\,\\\left[{\begin{matrix}s_{11}&s_{12}&s_{13}\\s_{21}&s_{22}&s_{23}\\s_{31}&s_{32}&s_{33}\end{matrix}}\right]&=\left[{\begin{matrix}\sigma _{11}&\sigma _{12}&\sigma _{13}\\\sigma _{21}&\sigma _{22}&\sigma _{23}\\\sigma _{31}&\sigma _{32}&\sigma _{33}\end{matrix}}\right]-\left[{\begin{matrix}\pi &0&0\\0&\pi &0\\0&0&\pi \end{matrix}}\right]\\&=\left[{\begin{matrix}\sigma _{11}-\pi &\sigma _{12}&\sigma _{13}\\\sigma _{21}&\sigma _{22}-\pi &\sigma _{23}\\\sigma _{31}&\sigma _{32}&\sigma _{33}-\pi \end{matrix}}\right].\end{aligned}}$

### Invariants of the stress deviator tensor

As it is a second order tensor, the stress deviator tensor also has a set of invariants, which can be obtained using the same procedure used to calculate the invariants of the stress tensor. It can be shown that the principal directions of the stress deviator tensor $s_{ij}$ are the same as the principal directions of the stress tensor ⁠ $\sigma _{ij}$ ⁠. Thus, the characteristic equation is

$\left|s_{ij}-\lambda \delta _{ij}\right|=\lambda ^{3}-J_{1}\lambda ^{2}-J_{2}\lambda -J_{3}=0,$

where ⁠ $J_{1}$ ⁠, $J_{2}$ and $J_{3}$ are the first, second, and third *deviatoric stress invariants*, respectively. Their values are the same (invariant) regardless of the orientation of the coordinate system chosen. These deviatoric stress invariants can be expressed as a function of the components of $s_{ij}$ or its principal values $s_{1}$ , $s_{2}$ , and $s_{3}$ , or alternatively, as a function of $\sigma _{ij}$ or its principal values ⁠ $\sigma _{1}$ ⁠, ⁠ $\sigma _{2}$ ⁠, and ⁠ $\sigma _{3}$ ⁠. Thus,

${\begin{aligned}J_{1}&=s_{kk}=0,\\[3pt]J_{2}&={\frac {1}{2}}s_{ij}s_{ji}={\frac {1}{2}}\operatorname {tr} \left({\boldsymbol {s}}^{2}\right)\\&={\frac {1}{2}}\left(s_{1}^{2}+s_{2}^{2}+s_{3}^{2}\right)\\&={\frac {1}{6}}\left[(\sigma _{11}-\sigma _{22})^{2}+(\sigma _{22}-\sigma _{33})^{2}+(\sigma _{33}-\sigma _{11})^{2}\right]+\sigma _{12}^{2}+\sigma _{23}^{2}+\sigma _{31}^{2}\\&={\frac {1}{6}}\left[(\sigma _{1}-\sigma _{2})^{2}+(\sigma _{2}-\sigma _{3})^{2}+(\sigma _{3}-\sigma _{1})^{2}\right]\\&={\frac {1}{3}}I_{1}^{2}-I_{2}={\frac {1}{2}}\left[\operatorname {tr} \left({\boldsymbol {\sigma }}^{2}\right)-{\frac {1}{3}}\operatorname {tr} ({\boldsymbol {\sigma }})^{2}\right],\\[3pt]J_{3}&=\det(s_{ij})\\&={\frac {1}{3}}s_{ij}s_{jk}s_{ki}={\frac {1}{3}}{\text{tr}}\left({\boldsymbol {s}}^{3}\right)\\&={\frac {1}{3}}\left(s_{1}^{3}+s_{2}^{3}+s_{3}^{3}\right)\\&=s_{1}s_{2}s_{3}\\&={\frac {2}{27}}I_{1}^{3}-{\frac {1}{3}}I_{1}I_{2}+I_{3}={\frac {1}{3}}\left[{\text{tr}}({\boldsymbol {\sigma }}^{3})-\operatorname {tr} \left({\boldsymbol {\sigma }}^{2}\right)\operatorname {tr} ({\boldsymbol {\sigma }})+{\frac {2}{9}}\operatorname {tr} ({\boldsymbol {\sigma }})^{3}\right].\,\end{aligned}}$

Because ⁠ $s_{kk}=0$ ⁠, the stress deviator tensor is in a state of pure shear.

A quantity called the equivalent stress or von Mises stress is commonly used in solid mechanics. The equivalent stress is defined as

$\sigma _{\text{vM}}={\sqrt {3\,J_{2}}}={\sqrt {{\frac {1}{2}}~\left[(\sigma _{1}-\sigma _{2})^{2}+(\sigma _{2}-\sigma _{3})^{2}+(\sigma _{3}-\sigma _{1})^{2}\right]}}\,.$

## Octahedral stresses

Considering the principal directions as the coordinate axes, a plane whose normal vector makes equal angles with each of the principal axes (i.e. having direction cosines equal to ⁠ $\vert 1/{\sqrt {3}}\vert$ ⁠) is called an *octahedral plane*. There are a total of eight octahedral planes (Figure 6). The normal and shear components of the stress tensor on these planes are called *octahedral normal stress* $\sigma _{\text{oct}}$ and *octahedral shear stress* ⁠ $\tau _{\text{oct}}$ ⁠, respectively. Octahedral plane passing through the origin is known as the *π-plane* (*π* not to be confused with *mean stress* denoted by *π* in above section) *.* On the *π-plane*, ⁠ $\textstyle s_{ij}={\frac {1}{3}}I$ ⁠.

Knowing that the stress tensor of point O (Figure 6) in the principal axes is

$\sigma _{ij}={\begin{bmatrix}\sigma _{1}&0&0\\0&\sigma _{2}&0\\0&0&\sigma _{3}\end{bmatrix}}$

the stress vector on an octahedral plane is then given by:

${\begin{aligned}\mathbf {T} _{\text{oct}}^{(\mathbf {n} )}&=\sigma _{ij}n_{i}\mathbf {e} _{j}\\&=\sigma _{1}n_{1}\mathbf {e} _{1}+\sigma _{2}n_{2}\mathbf {e} _{2}+\sigma _{3}n_{3}\mathbf {e} _{3}\\&={\frac {1}{\sqrt {3}}}(\sigma _{1}\mathbf {e} _{1}+\sigma _{2}\mathbf {e} _{2}+\sigma _{3}\mathbf {e} _{3})\end{aligned}}$

The normal component of the stress vector at point O associated with the octahedral plane is

${\begin{aligned}\sigma _{\text{oct}}&=T_{i}^{(n)}n_{i}\\&=\sigma _{ij}n_{i}n_{j}\\&=\sigma _{1}n_{1}n_{1}+\sigma _{2}n_{2}n_{2}+\sigma _{3}n_{3}n_{3}\\&={\frac {1}{3}}(\sigma _{1}+\sigma _{2}+\sigma _{3})={\frac {1}{3}}I_{1}\end{aligned}}$

which is the mean normal stress or hydrostatic stress. This value is the same in all eight octahedral planes. The shear stress on the octahedral plane is then

${\begin{aligned}\tau _{\text{oct}}&={\sqrt {T_{i}^{(n)}T_{i}^{(n)}-\sigma _{\text{oct}}^{2}}}\\&=\left[{\frac {1}{3}}\left(\sigma _{1}^{2}+\sigma _{2}^{2}+\sigma _{3}^{2}\right)-{\frac {1}{9}}(\sigma _{1}+\sigma _{2}+\sigma _{3})^{2}\right]^{\frac {1}{2}}\\&={\frac {1}{3}}\left[(\sigma _{1}-\sigma _{2})^{2}+(\sigma _{2}-\sigma _{3})^{2}+(\sigma _{3}-\sigma _{1})^{2}\right]^{\frac {1}{2}}={\frac {1}{3}}{\sqrt {2I_{1}^{2}-6I_{2}}}={\sqrt {{\frac {2}{3}}J_{2}}}\end{aligned}}$
