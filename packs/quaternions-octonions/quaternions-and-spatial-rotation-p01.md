---
title: "Quaternions and spatial rotation (part 1/2)"
source: https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation
domain: quaternions-octonions
license: CC-BY-SA-4.0
tags: quaternion algebra, octonion algebra, cayley-dickson construction, spatial rotation
fetched: 2026-07-02
part: 1/2
---

# Quaternions and spatial rotation

Unit quaternions, known as *versors*, provide a convenient mathematical notation for representing spatial orientations and rotations of elements in three dimensional space (*3D rotations*). This is a generalization of the use of unit complex numbers for 2D rotations. Specifically, quaternions encode information about an axis-angle rotation about an arbitrary axis. Rotation and orientation quaternions have applications in computer graphics, computer vision, robotics, navigation, molecular dynamics, flight dynamics, orbital mechanics of satellites, and crystallographic texture analysis.

When used to represent rotation, unit quaternions are also called **rotation quaternions** as they represent the 3D rotation group. When used to represent an orientation or attitude (body rotation relative to a reference coordinate system), they are called **orientation quaternions** or **attitude quaternions**. A spatial rotation in the amount of $\theta$ radians about a fixed unit axis $(X,Y,Z)$ that denotes the *Euler axis* is given by the quaternion $(C,X\,S,Y\,S,Z\,S)$ , where $C=\cos(\theta /2)$ and $S=\sin(\theta /2)$ .

Compared to rotation matrices, quaternions are more compact, efficient, and numerically stable. Compared to Euler angles, they are simpler to compose. However, they are not as intuitive and easy to understand and, due to the periodic nature of sine and cosine, rotation angles differing precisely by the natural period will be encoded into identical quaternions and recovered angles in radians will be limited to $[0,2\pi ]$ .


## Using quaternions as rotations

In 3-dimensional space, according to Euler's rotation theorem, any rotation or sequence of rotations of a rigid body or coordinate system about a fixed point is equivalent to a single rotation by a given angle $\theta$ about a fixed axis (called the *Euler axis*) that runs through the fixed point. The Euler axis is typically represented by a unit vector  ${\vec {u}}$ ( ${\hat {e}}$ in the picture). Therefore, any rotation in three dimensions can be represented as a vector  ${\vec {u}}$ and an angle $\theta$ .

Quaternions give a simple way to encode this axis–angle representation using four real numbers, and can be used to apply (calculate) the corresponding rotation to a position vector (x,y,z), representing a point relative to the origin in **R**3.

Euclidean vectors such as (2, 3, 4) or (*a**x*, *a**y*, *a**z*) can be rewritten as 2 **i** + 3 **j** + 4 **k** or *a**x* **i** + *a**y* **j** + *a**z* **k**, where **i**, **j**, **k** are unit vectors representing the three Cartesian axes (traditionally **x**, **y**, **z**), and also obey the multiplication rules of the fundamental quaternion units by interpreting the Euclidean vector (*a**x*, *a**y*, *a**z*) as the vector part of the pure quaternion (0, *a**x*, *a**y*, *a**z*).

A rotation of angle $\theta$ around the axis defined by the unit vector

$\mathbf {u} =(u_{x},u_{y},u_{z})=u_{x}\mathbf {i} +u_{y}\mathbf {j} +u_{z}\mathbf {k}$

can be represented by conjugation by a unit quaternion **q**. Since the quaternion product $\ (0+u_{x}\mathbf {i} +u_{y}\mathbf {j} +u_{z}\mathbf {k} )(0-u_{x}\mathbf {i} -u_{y}\mathbf {j} -u_{z}\mathbf {k} )$ gives 1, using the Taylor series of the exponential function, the extension of Euler's formula results:

$\mathbf {q} =e^{{\frac {\theta }{2}}{(u_{x}\mathbf {i} +u_{y}\mathbf {j} +u_{z}\mathbf {k} )}}=\cos {\frac {\theta }{2}}+(u_{x}\mathbf {i} +u_{y}\mathbf {j} +u_{z}\mathbf {k} )\sin {\frac {\theta }{2}}=\cos {\frac {\theta }{2}}+\mathbf {u} \sin {\frac {\theta }{2}}$

It can be shown that the desired rotation can be applied to an ordinary vector $\mathbf {p} =(p_{x},p_{y},p_{z})=p_{x}\mathbf {i} +p_{y}\mathbf {j} +p_{z}\mathbf {k}$ in 3-dimensional space, considered as the vector part of the pure quaternion $\mathbf {p'}$ , by evaluating the conjugation of **p**′ by **q**, given by:

$L(\mathbf {p'} ):=\mathbf {q} \mathbf {p'} \mathbf {q} ^{-1}=(0,\mathbf {r} ),$

$\mathbf {r} =(\cos ^{2}{\frac {\theta }{2}}-\sin ^{2}{\frac {\theta }{2}}||\mathbf {u} ||^{2})\mathbf {p} +2\sin ^{2}{\frac {\theta }{2}}(\mathbf {u} \cdot \mathbf {p} )\mathbf {u} +2\cos {\frac {\theta }{2}}\sin {\frac {\theta }{2}}(\mathbf {u} \times \mathbf {p} ),$

using the Hamilton product, where the vector part of the pure quaternion L(**p**′) = (0, *r**x*, *r**y*, *r**z*) is the new position vector of the point after the rotation. In a programmatic implementation, the conjugation is achieved by constructing a pure quaternion whose vector part is **p**, and then performing the quaternion conjugation. The vector part of the resulting pure quaternion is the desired vector **r**. Clearly, L provides a linear transformation of the quaternion space to itself; also, since $\mathbf {q}$ is unitary, the transformation is an isometry. Also, $L(\mathbf {q} )=\mathbf {q}$ and so L leaves vectors parallel to $\mathbf {q}$ invariant. So, by decomposing $\mathbf {p}$ as a vector parallel to the vector part $(u_{x},u_{y},u_{z})\sin {\frac {\theta }{2}}$ of $\mathbf {q}$ and a vector normal to the vector part of $\mathbf {q}$ and showing that the application of L to the normal component of $\mathbf {p}$ rotates it, the claim is shown. So let $\mathbf {n}$ be the component of $\mathbf {p}$ orthogonal to the vector part of $\mathbf {q}$ and let $\mathbf {n} _{T}=\mathbf {u} \times \mathbf {n}$ . It turns out that the vector part of $L(0,\mathbf {n} )$ is given by

$\left(\cos ^{2}{\frac {\theta }{2}}-\sin ^{2}{\frac {\theta }{2}}\right)\mathbf {n} +2\left(\cos {\frac {\theta }{2}}\sin {\frac {\theta }{2}}\right)\mathbf {n} _{T}=\cos \theta \mathbf {n} +\sin \theta \mathbf {n} _{T}$

.

The conjugation of **p**′ by **q** can be expressed with fewer arithmetic operations as:

$\mathbf {r} =\mathbf {p} +2\cos {\frac {\theta }{2}}\sin {\frac {\theta }{2}}(\mathbf {u} \times \mathbf {p} )+2\sin ^{2}{\frac {\theta }{2}}\mathbf {u} \times (\mathbf {u} \times \mathbf {p} ).$

A geometric fact independent of quaternions is the existence of a two-to-one mapping from physical rotations to rotational transformation matrices. If 0 ⩽ $\theta$ ⩽ $2\pi$ , a physical rotation about ${\vec {u}}$ by $\theta$ and a physical rotation about $-{\vec {u}}$ by $2\pi -\theta$ both achieve the same final orientation by disjoint paths through intermediate orientations. By inserting those vectors and angles into the formula for **q** above, one finds that if **q** represents the first rotation, −**q** represents the second rotation. This is a geometric proof that conjugation by **q** and by −**q** must produce the same rotational transformation matrix. That fact is confirmed algebraically by noting that the conjugation is quadratic in **q**, so the sign of **q** cancels, and does not affect the result. (See 2:1 mapping of SU(2) to SO(3)) If both rotations are a half-turn $(\theta =\pi )$ , both **q** and −**q** will have a real coordinate equal to zero. Otherwise, one will have a positive real part, representing a rotation by an angle less than $\pi$ , and the other will have a negative real part, representing a rotation by an angle greater than $\pi$ .

Mathematically, this operation carries the *set* of all "pure" quaternions **p** (those with real part equal to zero)—which constitute a 3-dimensional space among the quaternions—into itself, by the desired rotation about the axis ***u***, by the angle θ. (Each real quaternion is carried into itself by this operation. But for the purpose of rotations in 3-dimensional space, we ignore the real quaternions.)

The rotation is clockwise if our line of sight points in the same direction as ${\vec {u}}$ .

In this instance, **q** is a unit quaternion and

$\mathbf {q} ^{-1}=e^{-{\frac {\theta }{2}}{(u_{x}\mathbf {i} +u_{y}\mathbf {j} +u_{z}\mathbf {k} )}}=\cos {\frac {\theta }{2}}-(u_{x}\mathbf {i} +u_{y}\mathbf {j} +u_{z}\mathbf {k} )\sin {\frac {\theta }{2}}.$

It follows that conjugation by the product of two quaternions is the composition of conjugations by these quaternions: If **p** and **q** are unit quaternions, then rotation (conjugation) by **pq** is

$\mathbf {pq} {\vec {v}}(\mathbf {pq} )^{-1}=\mathbf {pq} {\vec {v}}\mathbf {q} ^{-1}\mathbf {p} ^{-1}=\mathbf {p} (\mathbf {q} {\vec {v}}\mathbf {q} ^{-1})\mathbf {p} ^{-1}$

,

which is the same as rotating (conjugating) by **q** and then by **p**. The scalar component of the result is necessarily zero.

The quaternion inverse of a rotation is the opposite rotation, since $\mathbf {q} ^{-1}(\mathbf {q} {\vec {v}}\mathbf {q} ^{-1})\mathbf {q} ={\vec {v}}$ . The square of a quaternion rotation is a rotation by twice the angle around the same axis. More generally **q***n* is a rotation by n times the angle around the same axis as **q**. This can be extended to arbitrary real n, allowing for smooth interpolation between spatial orientations; see Slerp.

Two rotation quaternions can be combined into one equivalent quaternion by the relation:

$\mathbf {q} '=\mathbf {q} _{2}\mathbf {q} _{1}$

in which **q**′ corresponds to the rotation **q**1 followed by the rotation **q**2. Thus, an arbitrary number of rotations can be composed together and then applied as a single rotation. (Note that quaternion multiplication is not commutative.)

### Example conjugation operation

*Conjugating* **p** *by* **q** refers to the operation **p** ↦ **qpq**−1.

Consider the rotation f around the axis ${\vec {v}}=\mathbf {i} +\mathbf {j} +\mathbf {k}$ , with a rotation angle of 120°, or ⁠2π/3⁠ radians.

$\alpha ={\frac {2\pi }{3}}$

The length of ${\vec {v}}$ is √3, the half angle is ⁠π/3⁠ (60°) with cosine ⁠1/2⁠, (cos  60° = 0.5) and sine ⁠√3/2⁠, (sin  60° ≈ 0.866). We are therefore dealing with a conjugation by the unit quaternion

${\begin{aligned}u&=\cos {\frac {\alpha }{2}}+\sin {\frac {\alpha }{2}}\cdot {\frac {1}{\|{\vec {v}}\|}}{\vec {v}}\\&=\cos {\frac {\pi }{3}}+\sin {\frac {\pi }{3}}\cdot {\frac {1}{\sqrt {3}}}{\vec {v}}\\&={\frac {1}{2}}+{\frac {\sqrt {3}}{2}}\cdot {\frac {1}{\sqrt {3}}}{\vec {v}}\\&={\frac {1}{2}}+{\frac {\sqrt {3}}{2}}\cdot {\frac {\mathbf {i} +\mathbf {j} +\mathbf {k} }{\sqrt {3}}}\\&={\frac {1+\mathbf {i} +\mathbf {j} +\mathbf {k} }{2}}\end{aligned}}$

If f is the rotation function,

$f(a\mathbf {i} +b\mathbf {j} +c\mathbf {k} )=u(a\mathbf {i} +b\mathbf {j} +c\mathbf {k} )u^{-1}$

It can be proven that the inverse of a unit quaternion is obtained simply by changing the sign of its imaginary components. As a consequence,

$u^{-1}={\dfrac {1-\mathbf {i} -\mathbf {j} -\mathbf {k} }{2}}$

and

$f(a\mathbf {i} +b\mathbf {j} +c\mathbf {k} )={\dfrac {1+\mathbf {i} +\mathbf {j} +\mathbf {k} }{2}}(a\mathbf {i} +b\mathbf {j} +c\mathbf {k} ){\dfrac {1-\mathbf {i} -\mathbf {j} -\mathbf {k} }{2}}$

This can be simplified, using the ordinary rules for quaternion arithmetic, to

$f(a\mathbf {i} +b\mathbf {j} +c\mathbf {k} )=c\mathbf {i} +a\mathbf {j} +b\mathbf {k}$

As expected, the rotation corresponds to keeping a cube held fixed at one point, and rotating it 120° about the long diagonal through the fixed point (observe how the three axes are permuted cyclically).

### Quaternion-derived rotation matrix

A quaternion rotation $\mathbf {p'} =\mathbf {q} \mathbf {p} \mathbf {q} ^{-1}$ (with $\mathbf {q} =q_{r}+q_{i}\mathbf {i} +q_{j}\mathbf {j} +q_{k}\mathbf {k}$ ) can be algebraically manipulated into a matrix rotation $\mathbf {p'} =\mathbf {Rp}$ , where $\mathbf {R}$ is the rotation matrix given by:

$\mathbf {R} ={\begin{bmatrix}1-2s(q_{j}^{2}+q_{k}^{2})&2s(q_{i}q_{j}-q_{k}q_{r})&2s(q_{i}q_{k}+q_{j}q_{r})\\2s(q_{i}q_{j}+q_{k}q_{r})&1-2s(q_{i}^{2}+q_{k}^{2})&2s(q_{j}q_{k}-q_{i}q_{r})\\2s(q_{i}q_{k}-q_{j}q_{r})&2s(q_{j}q_{k}+q_{i}q_{r})&1-2s(q_{i}^{2}+q_{j}^{2})\end{bmatrix}}$

Here $s=\|q\|^{-2}$ and if q is a unit quaternion, $s=1^{-2}=1$ .

This can be obtained by using vector calculus and linear algebra if we express $\mathbf {p}$ and $\mathbf {q}$ as scalar and vector parts and use the formula for the multiplication operation in the equation $\mathbf {p'} =\mathbf {q} \mathbf {p} \mathbf {q} ^{-1}$ . If we write $\mathbf {p}$ as $\left(0,\ \mathbf {p} \right)$ , $\mathbf {p} '$ as $\left(0,\ \mathbf {p} '\right)$ and $\mathbf {q}$ as $\left(q_{r},\ \mathbf {v} \right)$ , where $\mathbf {v} =\left(q_{i},q_{j},q_{k}\right)$ , our equation turns into $\left(0,\ \mathbf {p} '\right)=\left(q_{r},\ \mathbf {v} \right)\left(0,\ \mathbf {p} \right)s\left(q_{r},\ -\mathbf {v} \right)$ . By using the formula for multiplication of two quaternions that are expressed as scalar and vector parts,

$\left(r_{1},\ {\vec {v}}_{1}\right)\left(r_{2},\ {\vec {v}}_{2}\right)=\left(r_{1}r_{2}-{\vec {v}}_{1}\cdot {\vec {v}}_{2},\ r_{1}{\vec {v}}_{2}+r_{2}{\vec {v}}_{1}+{\vec {v}}_{1}\times {\vec {v}}_{2}\right),$

this equation can be rewritten as

${\begin{aligned}(0,\ \mathbf {p} ')=&((q_{r},\ \mathbf {v} )(0,\ \mathbf {p} ))s(q_{r},\ -\mathbf {v} )\\=&(q_{r}0-\mathbf {v} \cdot \mathbf {p} ,\ q_{r}\mathbf {p} +0\mathbf {v} +\mathbf {v} \times \mathbf {p} )s(q_{r},\ -\mathbf {v} )\\=&s(-\mathbf {v} \cdot \mathbf {p} ,\ q_{r}\mathbf {p} +\mathbf {v} \times \mathbf {p} )(q_{r},\ -\mathbf {v} )\\=&s(-\mathbf {v} \cdot \mathbf {p} q_{r}-(q_{r}\mathbf {p} +\mathbf {v} \times \mathbf {p} )\cdot (-\mathbf {v} ),\ (-\mathbf {v} \cdot \mathbf {p} )(-\mathbf {v} )+q_{r}(q_{r}\mathbf {p} +\mathbf {v} \times \mathbf {p} )+(q_{r}\mathbf {p} +\mathbf {v} \times \mathbf {p} )\times (-\mathbf {v} ))\\=&s\left(-\mathbf {v} \cdot \mathbf {p} q_{r}+q_{r}\mathbf {v} \cdot \mathbf {p} ,\ \mathbf {v} \left(\mathbf {v} \cdot \mathbf {p} \right)+q_{r}^{2}\mathbf {p} +q_{r}\mathbf {v} \times \mathbf {p} +\mathbf {v} \times \left(q_{r}\mathbf {p} +\mathbf {v} \times \mathbf {p} \right)\right)\\=&\left(0,\ s\left(\mathbf {v} \otimes \mathbf {v} +q_{r}^{2}\mathbf {I} +2q_{r}[\mathbf {v} ]_{\times }+[\mathbf {v} ]_{\times }^{2}\right)\mathbf {p} \right),\end{aligned}}$

where $\otimes$ denotes the outer product, $\mathbf {I}$ is the identity matrix and $[\mathbf {v} ]_{\times }$ is the transformation matrix that when multiplied from the right with a vector $\mathbf {u}$ gives the cross product $\mathbf {v} \times \mathbf {u}$ .

Since $\mathbf {p} '=\mathbf {R} \mathbf {p}$ , we can identify $\mathbf {R}$ as $s\left(\mathbf {v} \otimes \mathbf {v} +q_{r}^{2}\mathbf {I} +2q_{r}[\mathbf {v} ]_{\times }+[\mathbf {v} ]_{\times }^{2}\right)$ , which upon expansion should result in the expression written in matrix form above.

### Recovering the axis-angle representation

The expression $\mathbf {q} \mathbf {p} \mathbf {q} ^{-1}$ rotates any vector quaternion $\mathbf {p}$ around an axis given by the vector $\mathbf {a}$ by the angle $\theta$ , where $\mathbf {a}$ and $\theta$ depends on the quaternion $\mathbf {q} =q_{r}+q_{i}\mathbf {i} +q_{j}\mathbf {j} +q_{k}\mathbf {k}$ .

$\mathbf {a}$ and $\theta$ can be found from the following equations:

${\begin{aligned}(a_{x},a_{y},a_{z})={}&{\frac {(q_{i},q_{j},q_{k})}{\sqrt {q_{i}^{2}+q_{j}^{2}+q_{k}^{2}}}}\\[2pt]\theta =2\operatorname {atan2} &\left({\sqrt {q_{i}^{2}+q_{j}^{2}+q_{k}^{2}}},\,q_{r}\right),\end{aligned}}$

where $\operatorname {atan2}$ is the two-argument arctangent. While $\theta =2\operatorname {acos} (q_{r})$ works, it is numerically unstable (inaccurate) near $q_{r}=\pm 1$ for numbers with finite precision.

Care should be taken when the quaternion approaches a scalar, since due to degeneracy the axis of an identity rotation is not well-defined.

### The composition of spatial rotations

A benefit of the quaternion formulation of the composition of two rotations *R**B* and *R**A* is that it yields directly the rotation axis and angle of the composite rotation *R**C* = *R**B**R**A*.

Let the quaternion associated with a spatial rotation R be constructed from its rotation axis **S** with the rotation angle $\varphi$ around this axis. The associated quaternion is given by $S=\cos {\frac {\varphi }{2}}+\mathbf {S} \sin {\frac {\varphi }{2}}.$ Then the composition of the rotation *R**B* with *R**A* is the rotation *R**C* = *R**B**R**A* with rotation axis and angle defined by the product of the quaternions $A=\cos {\frac {\alpha }{2}}+\mathbf {A} \sin {\frac {\alpha }{2}}\quad {\text{and}}\quad B=\cos {\frac {\beta }{2}}+\mathbf {B} \sin {\frac {\beta }{2}},$ that is $C=\cos {\frac {\gamma }{2}}+\mathbf {C} \sin {\frac {\gamma }{2}}=\left(\cos {\frac {\beta }{2}}+\mathbf {B} \sin {\frac {\beta }{2}}\right)\left(\cos {\frac {\alpha }{2}}+\mathbf {A} \sin {\frac {\alpha }{2}}\right).$

Expand this product to obtain $\cos {\frac {\gamma }{2}}+\mathbf {C} \sin {\frac {\gamma }{2}}=\left(\cos {\frac {\beta }{2}}\cos {\frac {\alpha }{2}}-\mathbf {B} \cdot \mathbf {A} \sin {\frac {\beta }{2}}\sin {\frac {\alpha }{2}}\right)+\left(\mathbf {B} \sin {\frac {\beta }{2}}\cos {\frac {\alpha }{2}}+\mathbf {A} \sin {\frac {\alpha }{2}}\cos {\frac {\beta }{2}}+\mathbf {B} \times \mathbf {A} \sin {\frac {\beta }{2}}\sin {\frac {\alpha }{2}}\right).$

Divide both sides of this equation by the identity, which is the law of cosines on a sphere, $\cos {\frac {\gamma }{2}}=\cos {\frac {\beta }{2}}\cos {\frac {\alpha }{2}}-\mathbf {B} \cdot \mathbf {A} \sin {\frac {\beta }{2}}\sin {\frac {\alpha }{2}},$ and compute $\mathbf {C} \tan {\frac {\gamma }{2}}={\frac {\mathbf {B} \tan {\frac {\beta }{2}}+\mathbf {A} \tan {\frac {\alpha }{2}}+\mathbf {B} \times \mathbf {A} \tan {\frac {\beta }{2}}\tan {\frac {\alpha }{2}}}{1-\mathbf {B} \cdot \mathbf {A} \tan {\frac {\beta }{2}}\tan {\frac {\alpha }{2}}}}.$

This is Rodrigues' formula for the axis of a composite rotation defined in terms of the axes of the two rotations. He derived this formula in 1840 (see page 408).

The three rotation axes **A**, **B**, and **C** form a spherical triangle and the dihedral angles between the planes formed by the sides of this triangle are defined by the rotation angles. Hamilton presented the component form of these equations showing that the quaternion product computes the third vertex of a spherical triangle from two given vertices and their associated arc-lengths, which is also defines an algebra for points in Elliptic geometry.

#### Axis–angle composition

The normalized rotation axis, removing the ${\textstyle \cos {\frac {\gamma }{2}}}$ from the expanded product, leaves the vector which is the rotation axis, times some constant. Care should be taken normalizing the axis vector when $\gamma$ is 0 or $k2\pi$ where the vector is near 0 ; which is identity, or 0 rotation around any axis.

${\begin{aligned}\gamma &=2\cos ^{-1}\left(\cos {\frac {\beta }{2}}\cos {\frac {\alpha }{2}}-\mathbf {B} \cdot \mathbf {A} \sin {\frac {\beta }{2}}\sin {\frac {\alpha }{2}}\right)\\\mathbf {D} &=\mathbf {B} \sin {\frac {\beta }{2}}\cos {\frac {\alpha }{2}}+\mathbf {A} \sin {\frac {\alpha }{2}}\cos {\frac {\beta }{2}}+\mathbf {B} \times \mathbf {A} \sin {\frac {\beta }{2}}\sin {\frac {\alpha }{2}}\end{aligned}}$

Or with angle addition trigonometric substitutions... ${\begin{aligned}\gamma &=2\cos ^{-1}\left(\left(1-\mathbf {A} \cdot \mathbf {B} \right)\cos {\frac {\beta -\alpha }{2}}+\left(1+\mathbf {A} \cdot \mathbf {B} \right)\cos {\frac {\beta +\alpha }{2}}\right)\\\mathbf {D} &=\left(\sin {\frac {\beta +\alpha }{2}}+\sin {\frac {\beta -\alpha }{2}}\right)\mathbf {A} +\left(\sin {\frac {\beta +\alpha }{2}}-\sin {\frac {\beta -\alpha }{2}}\right)\mathbf {B} +\left(\cos {\frac {\beta -\alpha }{2}}-\cos {\frac {\beta +\alpha }{2}}\right)\mathbf {B} \times \mathbf {A} \end{aligned}}$

finally normalizing the rotation axis: ${\textstyle {\frac {\mathbf {D} }{2\sin {\frac {1}{2}}\gamma }}}$ or ${\textstyle {\frac {\mathbf {D} }{\|\mathbf {D} \|}}}$ .

### Differentiation with respect to the rotation quaternion

The rotated quaternion **p' = q p q**−1 needs to be differentiated with respect to the rotating quaternion **q**, when the rotation is estimated from numerical optimization. The estimation of rotation angle is an essential procedure in 3D object registration or camera calibration. For unitary **q** and pure imaginary **p**, that is for a rotation in 3D space, the derivatives of the rotated quaternion can be represented using matrix calculus notation as

${\begin{aligned}{\frac {\partial \mathbf {p'} }{\partial \mathbf {q} }}\equiv \left[{\frac {\partial \mathbf {p'} }{\partial q_{0}}},{\frac {\partial \mathbf {p'} }{\partial q_{x}}},{\frac {\partial \mathbf {p'} }{\partial q_{y}}},{\frac {\partial \mathbf {p'} }{\partial q_{z}}}\right]=\left[\mathbf {qp} -(\mathbf {qp} )^{*},(\mathbf {qpi} )^{*}-\mathbf {qpi} ,(\mathbf {qpj} )^{*}-\mathbf {qpj} ,(\mathbf {qpk} )^{*}-\mathbf {qpk} \right].\end{aligned}}$

A derivation can be found in.


## Background

### Quaternions

The complex numbers can be defined by introducing an abstract symbol **i** which satisfies the usual rules of algebra and additionally the rule **i**2 = −1. This is sufficient to reproduce all of the rules of complex number arithmetic: for example:

$(a+b\mathbf {i} )(c+d\mathbf {i} )=ac+ad\mathbf {i} +b\mathbf {i} c+b\mathbf {i} d\mathbf {i} =ac+ad\mathbf {i} +bc\mathbf {i} +bd\mathbf {i} ^{2}=(ac-bd)+(bc+ad)\mathbf {i} .$

In the same way the quaternions can be defined by introducing abstract symbols **i**, **j**, **k** which satisfy the rules **i**2 = **j**2 = **k**2 = **i j k** = −1 and the usual algebraic rules *except* the commutative law of multiplication (a familiar example of such a noncommutative multiplication is matrix multiplication). From this all of the rules of quaternion arithmetic follow, such as the rules on multiplication of quaternion basis elements. Using these rules, one can show that:

${\begin{aligned}&(a+b\mathbf {i} +c\mathbf {j} +d\mathbf {k} )(e+f\mathbf {i} +g\mathbf {j} +h\mathbf {k} )=\\&(ae-bf-cg-dh)+(af+be+ch-dg)\mathbf {i} +(ag-bh+ce+df)\mathbf {j} +(ah+bg-cf+de)\mathbf {k} .\end{aligned}}$

The imaginary part $b\mathbf {i} +c\mathbf {j} +d\mathbf {k}$ of a quaternion behaves like a vector ${\vec {v}}=(b,c,d)$ in three-dimensional vector space, and the real part a behaves like a scalar in **R**. When quaternions are used in geometry, it is more convenient to define them as a scalar plus a vector:

$a+b\mathbf {i} +c\mathbf {j} +d\mathbf {k} =a+{\vec {v}}.$

Some might find it strange to add a *number* to a *vector*, as they are objects of very different natures, or to *multiply* two vectors together, as this operation is usually undefined. However, if one remembers that it is a mere notation for the real and imaginary parts of a quaternion, it becomes more legitimate. In other words, the correct reasoning is the addition of two quaternions, one with zero vector/imaginary part, and another one with zero scalar/real part:

$q_{1}=s+{\vec {v}}=\left(s,{\vec {0}}\right)+\left(0,{\vec {v}}\right).$

We can express quaternion multiplication in the modern language of vector cross and dot products (which were actually inspired by the quaternions in the first place). When multiplying the vector/imaginary parts, in place of the rules **i**2 = **j**2 = **k**2 = **ijk** = −1 we have the quaternion multiplication rule:

${\vec {v}}{\vec {w}}=-{\vec {v}}\cdot {\vec {w}}+{\vec {v}}\times {\vec {w}},$

where:

- ${\vec {v}}{\vec {w}}$ is the resulting quaternion,
- ${\vec {v}}\times {\vec {w}}$ is vector cross product (a vector),
- ${\vec {v}}\cdot {\vec {w}}$ is vector scalar product (a scalar).

Quaternion multiplication is noncommutative (because of the cross product, which anti-commutes), while scalar–scalar and scalar–vector multiplications commute. From these rules it follows immediately that (see Quaternions § Quaternions and three-dimensional geometry):

$q_{1}q_{2}=\left(s+{\vec {v}}\right)\left(t+{\vec {w}}\right)=\left(st-{\vec {v}}\cdot {\vec {w}}\right)+\left(s{\vec {w}}+t{\vec {v}}+{\vec {v}}\times {\vec {w}}\right).$

The (left and right) multiplicative inverse or reciprocal of a nonzero quaternion is given by the conjugate-to-norm ratio (see details):

$q_{1}^{-1}=\left(s+{\vec {v}}\right)^{-1}={\frac {\left(s+{\vec {v}}\right)^{*}}{\lVert s+{\vec {v}}\rVert ^{2}}}={\frac {s-{\vec {v}}}{s^{2}+\lVert {\vec {v}}\rVert ^{2}}},$

as can be verified by direct calculation (note the similarity to the multiplicative inverse of complex numbers).

### Rotation identity

Let ${\vec {u}}$ be a unit vector (the rotation axis) and let $q=\cos {\frac {\alpha }{2}}+{\vec {u}}\sin {\frac {\alpha }{2}}$ . Our goal is to show that

${\vec {v}}'=q{\vec {v}}q^{-1}=\left(\cos {\frac {\alpha }{2}}+{\vec {u}}\sin {\frac {\alpha }{2}}\right)\,{\vec {v}}\,\left(\cos {\frac {\alpha }{2}}-{\vec {u}}\sin {\frac {\alpha }{2}}\right)$

yields the vector ${\vec {v}}$ rotated by an angle $\alpha$ around the axis ${\vec {u}}$ . Expanding out (and bearing in mind that ${\vec {u}}{\vec {v}}={\vec {u}}\times {\vec {v}}-{\vec {u}}\cdot {\vec {v}}$ ), we have

${\begin{aligned}{\vec {v}}'&={\vec {v}}\cos ^{2}{\frac {\alpha }{2}}+\left({\vec {u}}{\vec {v}}-{\vec {v}}{\vec {u}}\right)\sin {\frac {\alpha }{2}}\cos {\frac {\alpha }{2}}-{\vec {u}}{\vec {v}}{\vec {u}}\sin ^{2}{\frac {\alpha }{2}}\\[6pt]&={\vec {v}}\cos ^{2}{\frac {\alpha }{2}}+2\left({\vec {u}}\times {\vec {v}}\right)\sin {\frac {\alpha }{2}}\cos {\frac {\alpha }{2}}-\left(\left({\vec {u}}\times {\vec {v}}\right)-\left({\vec {u}}\cdot {\vec {v}}\right)\right){\vec {u}}\sin ^{2}{\frac {\alpha }{2}}\\[6pt]&={\vec {v}}\cos ^{2}{\frac {\alpha }{2}}+2\left({\vec {u}}\times {\vec {v}}\right)\sin {\frac {\alpha }{2}}\cos {\frac {\alpha }{2}}-\left(\left({\vec {u}}\times {\vec {v}}\right){\vec {u}}-\left({\vec {u}}\cdot {\vec {v}}\right){\vec {u}}\right)\sin ^{2}{\frac {\alpha }{2}}\\[6pt]&={\vec {v}}\cos ^{2}{\frac {\alpha }{2}}+2\left({\vec {u}}\times {\vec {v}}\right)\sin {\frac {\alpha }{2}}\cos {\frac {\alpha }{2}}-\left(\left(\left({\vec {u}}\times {\vec {v}}\right)\times {\vec {u}}-\left({\vec {u}}\times {\vec {v}}\right)\cdot {\vec {u}}\right)-\left({\vec {u}}\cdot {\vec {v}}\right){\vec {u}}\right)\sin ^{2}{\frac {\alpha }{2}}\\[6pt]&={\vec {v}}\cos ^{2}{\frac {\alpha }{2}}+2\left({\vec {u}}\times {\vec {v}}\right)\sin {\frac {\alpha }{2}}\cos {\frac {\alpha }{2}}-\left(\left({\vec {v}}-\left({\vec {u}}\cdot {\vec {v}}\right){\vec {u}}\right)-0-\left({\vec {u}}\cdot {\vec {v}}\right){\vec {u}}\right)\sin ^{2}{\frac {\alpha }{2}}\\[6pt]&={\vec {v}}\cos ^{2}{\frac {\alpha }{2}}+2\left({\vec {u}}\times {\vec {v}}\right)\sin {\frac {\alpha }{2}}\cos {\frac {\alpha }{2}}-\left({\vec {v}}-2{\vec {u}}\left({\vec {u}}\cdot {\vec {v}}\right)\right)\sin ^{2}{\frac {\alpha }{2}}\\[6pt]&={\vec {v}}\cos ^{2}{\frac {\alpha }{2}}+2\left({\vec {u}}\times {\vec {v}}\right)\sin {\frac {\alpha }{2}}\cos {\frac {\alpha }{2}}+\left(2{\vec {u}}\left({\vec {u}}\cdot {\vec {v}}\right)-{\vec {v}}\right)\sin ^{2}{\frac {\alpha }{2}}\\[6pt]\end{aligned}}$

If we let ${\vec {v}}_{\bot }$ and ${\vec {v}}_{\|}$ equal the components of ${\vec {v}}$ perpendicular and parallel to ${\vec {u}}$ respectively, then ${\vec {v}}={\vec {v}}_{\bot }+{\vec {v}}_{\|}$ and ${\vec {u}}\left({\vec {u}}\cdot {\vec {v}}\right)={\vec {v}}_{\|}$ , leading to

${\begin{aligned}{\vec {v}}'&={\vec {v}}\cos ^{2}{\frac {\alpha }{2}}+2\left({\vec {u}}\times {\vec {v}}\right)\sin {\frac {\alpha }{2}}\cos {\frac {\alpha }{2}}+\left(2{\vec {u}}\left({\vec {u}}\cdot {\vec {v}}\right)-{\vec {v}}\right)\sin ^{2}{\frac {\alpha }{2}}\\[6pt]&=\left({\vec {v}}_{\|}+{\vec {v}}_{\bot }\right)\cos ^{2}{\frac {\alpha }{2}}+2\left({\vec {u}}\times {\vec {v}}\right)\sin {\frac {\alpha }{2}}\cos {\frac {\alpha }{2}}+\left({\vec {v}}_{\|}-{\vec {v}}_{\bot }\right)\sin ^{2}{\frac {\alpha }{2}}\\[6pt]&={\vec {v}}_{\|}\left(\cos ^{2}{\frac {\alpha }{2}}+\sin ^{2}{\frac {\alpha }{2}}\right)+\left({\vec {u}}\times {\vec {v}}\right)\left(2\sin {\frac {\alpha }{2}}\cos {\frac {\alpha }{2}}\right)+{\vec {v}}_{\bot }\left(\cos ^{2}{\frac {\alpha }{2}}-\sin ^{2}{\frac {\alpha }{2}}\right)\\[6pt]\end{aligned}}$

Using the trigonometric pythagorean and double-angle identities, we then have

${\begin{aligned}{\vec {v}}'&={\vec {v}}_{\|}\left(\cos ^{2}{\frac {\alpha }{2}}+\sin ^{2}{\frac {\alpha }{2}}\right)+\left({\vec {u}}\times {\vec {v}}\right)\left(2\sin {\frac {\alpha }{2}}\cos {\frac {\alpha }{2}}\right)+{\vec {v}}_{\bot }\left(\cos ^{2}{\frac {\alpha }{2}}-\sin ^{2}{\frac {\alpha }{2}}\right)\\[6pt]&={\vec {v}}_{\|}+\left({\vec {u}}\times {\vec {v}}\right)\sin \alpha +{\vec {v}}_{\bot }\cos \alpha \end{aligned}}$

This is the formula of a rotation by $\alpha$ around the *u*→ axis.


## Quaternion rotation operations

A very formal explanation of the properties used in this section is given by Altman.

### The hypersphere of rotations

#### Visualizing the space of rotations

Unit quaternions represent the group of Euclidean rotations in three dimensions in a very straightforward way. The correspondence between rotations and quaternions can be understood by first visualizing the space of rotations itself.

In order to visualize the space of rotations, it helps to consider a simpler case. Any rotation in three dimensions can be described by a rotation by some angle about some axis; for our purposes, we will use an axis *vector* to establish handedness for our angle. Consider the special case in which the axis of rotation lies in the *xy* plane. We can then specify the axis of one of these rotations by a point on a circle through which the vector crosses, and we can select the radius of the circle to denote the angle of rotation.

Similarly, a rotation whose axis of rotation lies in the *xy* plane can be described as a point on a sphere of *fixed* radius in *three* dimensions. Beginning at the north pole of a sphere in three-dimensional space, we specify the point at the north pole to be the identity rotation (a zero angle rotation). Just as in the case of the identity rotation, no axis of rotation is defined, and the angle of rotation (zero) is irrelevant. A rotation having a very small rotation angle can be specified by a slice through the sphere parallel to the *xy* plane and very near the north pole. The circle defined by this slice will be very small, corresponding to the small angle of the rotation. As the rotation angles become larger, the slice moves in the negative z direction, and the circles become larger until the equator of the sphere is reached, which will correspond to a rotation angle of 180 degrees. Continuing southward, the radii of the circles now become smaller (corresponding to the absolute value of the angle of the rotation considered as a negative number). Finally, as the south pole is reached, the circles shrink once more to the identity rotation, which is also specified as the point at the south pole.

Notice that a number of characteristics of such rotations and their representations can be seen by this visualization. The space of rotations is continuous, each rotation has a neighborhood of rotations which are nearly the same, and this neighborhood becomes flat as the neighborhood shrinks. Also, each rotation is actually represented by two antipodal points on the sphere, which are at opposite ends of a line through the center of the sphere. This reflects the fact that each rotation can be represented as a rotation about some axis, or, equivalently, as a negative rotation about an axis pointing in the opposite direction (a so-called double cover). The "latitude" of a circle representing a particular rotation angle will be half of the angle represented by that rotation, since as the point is moved from the north to south pole, the latitude ranges from zero to 180 degrees, while the angle of rotation ranges from 0 to 360 degrees. (the "longitude" of a point then represents a particular axis of rotation.) Note however that this set of rotations is not closed under composition. Two successive rotations with axes in the *xy* plane will not necessarily give a rotation whose axis lies in the *xy* plane, and thus cannot be represented as a point on the sphere. This will not be the case with a general rotation in 3-space, in which rotations do form a closed set under composition.

This visualization can be extended to a general rotation in 3-dimensional space. The identity rotation is a point, and a small angle of rotation about some axis can be represented as a point on a sphere with a small radius. As the angle of rotation grows, the sphere grows, until the angle of rotation reaches 180 degrees, at which point the sphere begins to shrink, becoming a point as the angle approaches 360 degrees (or zero degrees from the negative direction). This set of expanding and contracting spheres represents a hypersphere in four dimensional space (a 3-sphere). Just as in the simpler example above, each rotation represented as a point on the hypersphere is matched by its antipodal point on that hypersphere. The "latitude" on the hypersphere will be half of the corresponding angle of rotation, and the neighborhood of any point will become "flatter" (i.e. be represented by a 3-D Euclidean space of points) as the neighborhood shrinks. This behavior is matched by the set of unit quaternions: A general quaternion represents a point in a four dimensional space, but constraining it to have unit magnitude yields a three-dimensional space equivalent to the surface of a hypersphere. The magnitude of the unit quaternion will be unity, corresponding to a hypersphere of unit radius. The vector part of a unit quaternion represents the radius of the 2-sphere corresponding to the axis of rotation, and its magnitude is the sine of half the angle of rotation. Each rotation is represented by two unit quaternions of opposite sign, and, as in the space of rotations in three dimensions, the quaternion product of two unit quaternions will yield a unit quaternion. Also, the space of unit quaternions is "flat" in any infinitesimal neighborhood of a given unit quaternion.

#### Parameterizing the space of rotations

We can parameterize the surface of a sphere with two coordinates, such as latitude and longitude. But latitude and longitude are ill-behaved (degenerate as described by the hairy ball theorem) at the north and south poles, though the poles are not intrinsically different from any other points on the sphere. At the poles (latitudes +90° and −90°), the longitude becomes meaningless.

It can be shown that no two-parameter coordinate system can avoid such degeneracy. We can avoid such problems by embedding the sphere in three-dimensional space and parameterizing it with three Cartesian coordinates (*w*, *x*, *y*), placing the north pole at (*w*, *x*, *y*) = (1, 0, 0), the south pole at (*w*, *x*, *y*) = (−1, 0, 0), and the equator at *w* = 0, *x*2 + *y*2 = 1. Points on the sphere satisfy the constraint *w*2 + *x*2 + *y*2 = 1, so we still have just two degrees of freedom though there are three coordinates. A point (*w*, *x*, *y*) on the sphere represents a rotation in the ordinary space around the horizontal axis directed by the vector (*x*, *y*, 0) by an angle $\alpha =2\cos ^{-1}w=2\sin ^{-1}{\sqrt {x^{2}+y^{2}}}$ .

In the same way the hyperspherical space of 3D rotations can be parameterized by three angles (Euler angles), but any such parameterization is degenerate at some points on the hypersphere, leading to the problem of gimbal lock. We can avoid this by using four Euclidean coordinates *w*, *x*, *y*, *z*, with *w*2 + *x*2 + *y*2 + *z*2 = 1. The point (*w*, *x*, *y*, *z*) represents a rotation around the axis directed by the vector (*x*, *y*, *z*) by an angle $\alpha =2\cos ^{-1}w=2\sin ^{-1}{\sqrt {x^{2}+y^{2}+z^{2}}}.$


## Explaining quaternions' properties with rotations

### Non-commutativity

The multiplication of quaternions is non-commutative. This fact explains how the **p** ↦ **q p q**−1 formula can work at all, having **q q**−1 = 1 by definition. Since the multiplication of unit quaternions corresponds to the composition of three-dimensional rotations, this property can be made intuitive by showing that three-dimensional rotations are not commutative in general.

The figure to the right illustrates this with dice. Use the right hand to create a pair of 90 degree rotations. Both dice are initially configured as shown in the upper left-hand corner (with 1 dot on the top face.) Path A begins with a rotation about the –*y* axis (using the right-hand rule.), followed by a rotation about the +*z* axis, resulting in the configuration shown in the lower left corner (5 dots on the top face.) Path B reverses the sequence of rotations, resulting with 3 dots on top.

Alternatively, set two books next to each other. Rotate one of them 90 degrees clockwise around the z axis, then flip it 180 degrees around the x axis. Take the other book, flip it 180° around x axis first, and 90° clockwise around z later. The two books do not end up parallel. This shows that, in general, the composition of two different rotations around two distinct spatial axes will not commute.

### Orientation

The vector cross product, used to define the axis–angle representation, does confer an orientation ("handedness") to space: in a three-dimensional vector space, the three vectors in the equation **a** × **b** = **c** will always form a right-handed set (or a left-handed set, depending on how the cross product is defined), thus fixing an orientation in the vector space. Alternatively, the dependence on orientation is expressed in referring to such ${\vec {u}}$ that specifies a rotation as to *axial vectors*. In quaternionic formalism the choice of an orientation of the space corresponds to order of multiplication: **ij** = **k** but **ji** = −**k**. If one reverses the orientation, then the formula above becomes **p** ↦ **q**−1 **p q**, i.e., a unit **q** is replaced with the conjugate quaternion – the same behaviour as of axial vectors.


## Alternative conventions

It is reported that the existence and continued usage of an alternative quaternion convention in the aerospace and, to a lesser extent, robotics community is incurring a *significant and ongoing cost* [*sic*]. This alternative convention is proposed by Shuster M.D. in and departs from tradition by reversing the definition for multiplying quaternion basis elements such that under Shuster's convention, $\mathbf {i} \mathbf {j} =-\mathbf {k}$ whereas Hamilton's definition is $\mathbf {i} \mathbf {j} =\mathbf {k}$ . This convention is also referred to as "JPL convention" for its use in some parts of NASA's Jet Propulsion Laboratory.

Under Shuster's convention, the formula for multiplying two quaternions is altered such that

$\left(r_{1},\ {\vec {v}}_{1}\right)\left(r_{2},\ {\vec {v}}_{2}\right)=\left(r_{1}r_{2}-{\vec {v}}_{1}\cdot {\vec {v}}_{2},\ r_{1}{\vec {v}}_{2}+r_{2}{\vec {v}}_{1}\mathbin {\color {red}\mathbf {-} } {\vec {v}}_{1}\times {\vec {v}}_{2}\right),\qquad {\text{(Alternative convention, usage discouraged!)}}$

The formula for rotating a vector by a quaternion is altered to be

${\begin{aligned}\mathbf {p} '_{\text{alt}}={}&(\mathbf {v} \otimes \mathbf {v} +q_{r}^{2}\mathbf {I} \mathbin {\color {red}\mathbf {-} } 2q_{r}[\mathbf {v} ]_{\times }+[\mathbf {v} ]_{\times }^{2})\mathbf {p} &{\text{(Alternative convention, usage discouraged!)}}\\=&\ (\mathbf {I} \mathbin {\color {red}\mathbf {-} } 2q_{r}[\mathbf {v} ]_{\times }+2[\mathbf {v} ]_{\times }^{2})\mathbf {p} &\end{aligned}}$

To identify the changes under Shuster's convention, see that the sign before the cross product is flipped from plus to minus.

Finally, the formula for converting a quaternion to a rotation matrix is altered to be

${\begin{aligned}\mathbf {R} _{alt}&=\mathbf {I} \mathbin {\color {red}\mathbf {-} } 2q_{r}[\mathbf {v} ]_{\times }+2[\mathbf {v} ]_{\times }^{2}\qquad {\text{(Alternative convention, usage discouraged!)}}\\&={\begin{bmatrix}1-2s(q_{j}^{2}+q_{k}^{2})&2(q_{i}q_{j}\mathbin {\color {red}\mathbf {+} } q_{k}q_{r})&2(q_{i}q_{k}\mathbin {\color {red}\mathbf {-} } q_{j}q_{r})\\2(q_{i}q_{j}\mathbin {\color {red}\mathbf {-} } q_{k}q_{r})&1-2s(q_{i}^{2}+q_{k}^{2})&2(q_{j}q_{k}\mathbin {\color {red}\mathbf {+} } q_{i}q_{r})\\2(q_{i}q_{k}\mathbin {\color {red}\mathbf {+} } q_{j}q_{r})&2(q_{j}q_{k}\mathbin {\color {red}\mathbf {-} } q_{i}q_{r})&1-2s(q_{i}^{2}+q_{j}^{2})\end{bmatrix}}\end{aligned}}$

which is exactly the transpose of the rotation matrix converted under the traditional convention.

### Software applications by convention used

The table below groups applications by their adherence to either quaternion convention:

| Hamilton multiplication convention | Shuster multiplication convention |
|---|---|
| Wolfram MathematicaMATLAB Robotics System ToolboxMATLAB Aerospace ToolboxROSEigenBoost quaternionsQuaternion.jsCeres SolverSciPy spatial.transform.Rotation librarySymPy symbolic mathematics librarynumpy-quaternion libraryUniversal Scene Description | Microsoft DirectX Math Library |

While use of either convention does not impact the capability or correctness of applications thus created, the authors of argued that the Shuster convention should be abandoned because it departs from the much older quaternion multiplication convention by Hamilton and may never be adopted by the mathematical or theoretical physics areas.
