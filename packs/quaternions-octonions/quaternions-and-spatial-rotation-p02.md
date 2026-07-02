---
title: "Quaternions and spatial rotation (part 2/2)"
source: https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation
domain: quaternions-octonions
license: CC-BY-SA-4.0
tags: quaternion algebra, octonion algebra, cayley-dickson construction, spatial rotation
fetched: 2026-07-02
part: 2/2
---

## Comparison with other representations of rotations

### Advantages of quaternions

The representation of a rotation as a quaternion (4 numbers) is more compact than the representation as an orthogonal matrix (9 numbers). Furthermore, for a given axis and angle, one can easily construct the corresponding quaternion, and conversely, for a given quaternion one can easily read off the axis and the angle. Both of these are much harder with matrices or Euler angles.

In video games and other applications, one is often interested in "smooth rotations", meaning that the scene should slowly rotate and not in a single step. This can be accomplished by choosing a curve such as the spherical linear interpolation in the quaternions, with one endpoint being the identity transformation 1 (or some other initial rotation) and the other being the intended final rotation. This is more problematic with other representations of rotations.

When composing several rotations on a computer, rounding errors necessarily accumulate. A quaternion that is slightly off still represents a rotation after being normalized: a matrix that is slightly off may not be orthogonal any more and is harder to convert back to a proper orthogonal matrix.

Quaternions also avoid a phenomenon called gimbal lock which can result when, for example in pitch/yaw/roll rotational systems, the pitch is rotated 90° up or down, so that yaw and roll then correspond to the same motion, and a degree of freedom of rotation is lost. In a gimbal-based aerospace inertial navigation system, for instance, this could have disastrous results if the aircraft is in a steep dive or ascent.

### Conversion to and from the matrix representation

#### From a quaternion to an orthogonal matrix

The orthogonal matrix corresponding to a rotation by the unit quaternion **z** = *a* + *b* **i** + *c* **j** + *d* **k** (with | **z** | = 1) when post-multiplying with a column vector is given by

$R={\begin{pmatrix}a^{2}+b^{2}-c^{2}-d^{2}&2bc-2ad&2bd+2ac\\2bc+2ad&a^{2}-b^{2}+c^{2}-d^{2}&2cd-2ab\\2bd-2ac&2cd+2ab&a^{2}-b^{2}-c^{2}+d^{2}\\\end{pmatrix}}.$

This rotation matrix is used on vector w as $w_{\text{rotated}}=R\cdot w$ . The quaternion representation of this rotation is given by:

${\begin{bmatrix}0\\w_{\text{rotated}}\end{bmatrix}}=z{\begin{bmatrix}0\\w\end{bmatrix}}z^{*},$

where $z^{*}$ is the conjugate of the quaternion z , given by $\mathbf {z} ^{*}=a-b\mathbf {i} -c\mathbf {j} -d\mathbf {k}$

Also, quaternion multiplication is defined as (assuming a and b are quaternions, like z above):

$ab=\left(a_{0}b_{0}-{\vec {a}}\cdot {\vec {b}};a_{0}{\vec {b}}+b_{0}{\vec {a}}+{\vec {a}}\times {\vec {b}}\right)$

where the order a, b is important since the cross product of two vectors is not commutative.

A more efficient calculation in which the quaternion does not need to be unit normalized is given by

$R={\begin{pmatrix}1-cc-dd&bc-ad&bd+ac\\bc+ad&1-bb-dd&cd-ab\\bd-ac&cd+ab&1-bb-cc\\\end{pmatrix}},$

where the following intermediate quantities have been defined:

${\begin{alignedat}{2}&\ \ s=2/(a\cdot a+b\cdot b+c\cdot c+d\cdot d),\\&{\begin{array}{lll}bs=b\cdot s,&cs=c\cdot s,&ds=d\cdot s,\\ab=a\cdot bs,&ac=a\cdot cs,&ad=a\cdot ds,\\bb=b\cdot bs,&bc=b\cdot cs,&bd=b\cdot ds,\\cc=c\cdot cs,&cd=c\cdot ds,&dd=d\cdot ds.\\\end{array}}\end{alignedat}}$

#### From an orthogonal matrix to a quaternion

One must be careful when converting a rotation matrix to a quaternion, as several straightforward methods tend to be unstable when the trace (sum of the diagonal elements) of the rotation matrix is zero or very small. For a stable method of converting an orthogonal matrix to a quaternion, see the Rotation matrix#Quaternion.

#### Fitting quaternions

The above section described how to recover a quaternion **q** from a 3 × 3 rotation matrix Q. Suppose, however, that we have some matrix Q that is not a pure rotation—due to round-off errors, for example—and we wish to find the quaternion **q** that most accurately represents Q. In that case we construct a symmetric 4 × 4 matrix

$K={\frac {1}{3}}{\begin{bmatrix}Q_{xx}-Q_{yy}-Q_{zz}&Q_{yx}+Q_{xy}&Q_{zx}+Q_{xz}&Q_{zy}-Q_{yz}\\Q_{yx}+Q_{xy}&Q_{yy}-Q_{xx}-Q_{zz}&Q_{zy}+Q_{yz}&Q_{xz}-Q_{zx}\\Q_{zx}+Q_{xz}&Q_{zy}+Q_{yz}&Q_{zz}-Q_{xx}-Q_{yy}&Q_{yx}-Q_{xy}\\Q_{zy}-Q_{yz}&Q_{xz}-Q_{zx}&Q_{yx}-Q_{xy}&Q_{xx}+Q_{yy}+Q_{zz}\end{bmatrix}},$

and find the eigenvector (*x*, *y*, *z*, *w*) corresponding to the largest eigenvalue (that value will be 1 if and only if Q is a pure rotation). The quaternion so obtained will correspond to the rotation closest to the original matrix Q .

### Performance comparisons

This section discusses the performance implications of using quaternions versus other methods (axis/angle or rotation matrices) to perform rotations in 3D.

#### Results

| Method | Storage |
|---|---|
| Rotation matrix | 9 or 6 (see below) |
| Quaternion | 4 or 3 (see below) |
| Angle–axis | 4 or 3 (see below) |

Only three of the quaternion components are independent, as a rotation is represented by a unit quaternion. For further calculation one usually needs all four elements, so all calculations would suffer additional expense from recovering the fourth component. Likewise, angle–axis can be stored in a three-component vector by multiplying the unit direction by the angle (or a function thereof), but this comes at additional computational cost when using it for calculations. Similarly, a rotation matrix requires orthogonal basis vectors, so in 3D space the third vector can unambiguously be calculated from the first two vectors with a cross product (though there is ambiguity in the sign of the third vector if improper rotations are allowed).

| Method | # multiplies | # add/subtracts | total operations |
|---|---|---|---|
| Rotation matrices | 27 | 18 | 45 |
| Quaternions | 16 | 12 | 28 |

| Method | # multiplies | # add/subtracts | # sin/cos | total operations |   |
|---|---|---|---|---|---|
| Rotation matrix | 9 | 6 | 0 | 15 |   |
| Quaternions * | Without intermediate matrix | 15 | 15 | 0 | 30 |
| With intermediate matrix | 21 | 18 | 0 | 39 |   |
| Angle–axis | Without intermediate matrix | 18 | 13 | 2 | 31 + 2 |
| With intermediate matrix | 21 | 16 | 2 | 37 + 2 |   |

* Quaternions can be implicitly converted to a rotation-like matrix (12 multiplications and 12 additions/subtractions), which levels the following vectors rotating cost with the rotation matrix method.

#### Used methods

There are three basic approaches to rotating a vector *v*→:

1. Compute the matrix product of a 3 × 3 rotation matrix R and the original 3 × 1 column matrix representing *v*→. This requires 3 × (3 multiplications + 2 additions) = 9 multiplications and 6 additions, the most efficient method for rotating a vector.
2. A rotation can be represented by a unit-length quaternion **q** = (*w*, *r*→) with scalar (real) part w and vector (imaginary) part *r*→. The rotation can be applied to a 3D vector *v*→ via the formula ${\vec {v}}_{\text{new}}={\vec {v}}+2{\vec {r}}\times ({\vec {r}}\times {\vec {v}}+w{\vec {v}})$ . This requires only 15 multiplications and 15 additions to evaluate (or 18 multiplications and 12 additions if the factor of 2 is done via multiplication.) This formula, originally thought to be used with axis/angle notation (Rodrigues' formula), can also be applied to quaternion notation. This yields the same result as the less efficient but more compact formula of quaternion multiplication ${\vec {v}}_{\text{new}}=q{\vec {v}}q^{-1}$ .
3. Use the angle/axis formula to convert an angle/axis to a rotation matrix R then multiplying with a vector, or, similarly, use a formula to convert quaternion notation to a rotation matrix, then multiplying with a vector. Converting the angle/axis to R costs 12 multiplications, 2 function calls (sin, cos), and 10 additions/subtractions; from item 1, rotating using R adds an additional 9 multiplications and 6 additions for a total of 21 multiplications, 16 add/subtractions, and 2 function calls (sin, cos). Converting a quaternion to R costs 12 multiplications and 12 additions/subtractions; from item 1, rotating using R adds an additional 9 multiplications and 6 additions for a total of 21 multiplications and 18 additions/subtractions.

| Method | # multiplies | # add/subtracts | # sin/cos | total operations |   |
|---|---|---|---|---|---|
| Rotation matrix | 9n | 6n | 0 | 15n |   |
| Quaternions * | Without intermediate matrix | 15n | 15n | 0 | 30n |
| With intermediate matrix | 9n + 12 | 6n + 12 | 0 | 15n + 24 |   |
| Angle–axis | Without intermediate matrix | 18n | 12n + 1 | 2 | 30n + 3 |
| With intermediate matrix | 9n + 12 | 6n + 10 | 2 | 15n + 24 |   |


## Pairs of unit quaternions as rotations in 4D space

A pair of unit quaternions $\mathbf {z} _{\rm {L}}=a_{\rm {L}}+b_{\rm {L}}i+c_{\rm {L}}j+d_{\rm {L}}k$ and $\mathbf {z} _{\rm {R}}=a_{\rm {R}}+b_{\rm {R}}i+c_{\rm {R}}j+d_{\rm {R}}k$ can represent any rotation in 4D space. Given a four-dimensional vector ${\vec {v}}$ , expressed as a quaternion ${\vec {v}}=w+xi+yj+zk$ , we can rotate it as follows:

$f\left({\vec {v}}\right)=\mathbf {z} _{\rm {L}}{\vec {v}}\mathbf {z} _{\rm {R}}=M_{\rm {L}}M_{\rm {R}}{\vec {v}}={\begin{pmatrix}a_{\rm {L}}&-b_{\rm {L}}&-c_{\rm {L}}&-d_{\rm {L}}\\b_{\rm {L}}&a_{\rm {L}}&-d_{\rm {L}}&c_{\rm {L}}\\c_{\rm {L}}&d_{\rm {L}}&a_{\rm {L}}&-b_{\rm {L}}\\d_{\rm {L}}&-c_{\rm {L}}&b_{\rm {L}}&a_{\rm {L}}\end{pmatrix}}{\begin{pmatrix}a_{\rm {R}}&-b_{\rm {R}}&-c_{\rm {R}}&-d_{\rm {R}}\\b_{\rm {R}}&a_{\rm {R}}&d_{\rm {R}}&-c_{\rm {R}}\\c_{\rm {R}}&-d_{\rm {R}}&a_{\rm {R}}&b_{\rm {R}}\\d_{\rm {R}}&c_{\rm {R}}&-b_{\rm {R}}&a_{\rm {R}}\end{pmatrix}}{\begin{pmatrix}w\\x\\y\\z\end{pmatrix}},$

where the matrices $M_{\rm {L}}$ and $M_{\rm {R}}$ represent left and right quaternion multiplications, respectively. Together, these matrices form an isoclinic decomposition of a rotation in $\mathbb {R} ^{4}$ . Since quaternion multiplication is associative, we have:

$(\mathbf {z} _{\rm {L}}{\vec {v}})\mathbf {z} _{\rm {R}}=M_{\rm {R}}M_{\rm {L}}{\vec {v}}=M_{\rm {L}}M_{\rm {R}}{\vec {v}}=\mathbf {z} _{\rm {L}}({\vec {v}}\mathbf {z} _{\rm {R}})$

.

Thus, the two matrices $M_{\rm {L}}$ and $M_{\rm {R}}$ must commute. This implies the existence of two commuting subgroups within the group of four-dimensional rotations. An arbitrary four-dimensional rotation has six degrees of freedom, with each matrix contributing three of these six degrees of freedom.

Since the generators of the four-dimensional rotations can be represented by pairs of quaternions (as follows), all four-dimensional rotations can also be represented.

${\begin{aligned}\mathbf {z} _{\rm {L}}{\vec {v}}\mathbf {z} _{\rm {R}}&={\begin{pmatrix}1&-dt_{ab}&-dt_{ac}&-dt_{ad}\\dt_{ab}&1&-dt_{bc}&-dt_{bd}\\dt_{ac}&dt_{bc}&1&-dt_{cd}\\dt_{ad}&dt_{bd}&dt_{cd}&1\end{pmatrix}}{\begin{pmatrix}w\\x\\y\\z\end{pmatrix}}\\[3pt]\mathbf {z} _{\rm {L}}&=1+{dt_{ab}+dt_{cd} \over 2}i+{dt_{ac}-dt_{bd} \over 2}j+{dt_{ad}+dt_{bc} \over 2}k\\[3pt]\mathbf {z} _{\rm {R}}&=1+{dt_{ab}-dt_{cd} \over 2}i+{dt_{ac}+dt_{bd} \over 2}j+{dt_{ad}-dt_{bc} \over 2}k\end{aligned}}$
