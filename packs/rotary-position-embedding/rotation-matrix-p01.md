---
title: "Rotation matrix (part 1/2)"
source: https://en.wikipedia.org/wiki/Rotation_matrix
domain: rotary-position-embedding
license: CC-BY-SA-4.0
tags: rotary position embedding, relative positional encoding, token position rotation, attention position bias
fetched: 2026-07-02
part: 1/2
---

# Rotation matrix

In linear algebra, a **rotation matrix** is a transformation matrix that is used to perform a rotation in Euclidean space. For example, using the convention below, the matrix

$R={\begin{bmatrix}\cos \theta &-\sin \theta \\\sin \theta &\cos \theta \end{bmatrix}}\cdot$

rotates points in the xy plane counterclockwise through an angle θ about the origin of a two-dimensional Cartesian coordinate system. To perform the rotation on a plane point with standard coordinates **v** = (*x*, *y*), it should be written as a column vector, and multiplied by the matrix R:

$R\mathbf {v} ={\begin{bmatrix}\cos \theta &-\sin \theta \\\sin \theta &\cos \theta \end{bmatrix}}{\begin{bmatrix}x\\y\end{bmatrix}}=x{\begin{bmatrix}\cos \theta \\\sin \theta \end{bmatrix}}+y{\begin{bmatrix}-\sin \theta \\\cos \theta \end{bmatrix}}={\begin{bmatrix}x\cos \theta -y\sin \theta \\x\sin \theta +y\cos \theta \end{bmatrix}}.$

If x and y are the coordinates of the endpoint of a vector with the length *r* and the angle $\phi$ with respect to the x-axis, so that ${\textstyle x=r\cos \phi }$ and $y=r\sin \phi$ , then the above equations become the trigonometric summation angle formulae: $R\mathbf {v} =r{\begin{bmatrix}\cos \phi \cos \theta -\sin \phi \sin \theta \\\cos \phi \sin \theta +\sin \phi \cos \theta \end{bmatrix}}=r{\begin{bmatrix}\cos(\phi +\theta )\\\sin(\phi +\theta )\end{bmatrix}}.$ Indeed, these are the trigonometric summation angle formulae in matrix form. One way to understand this is to say we have a vector at an angle 30° from the x-axis, and we wish to rotate that angle by a further 45°. We simply need to compute the vector endpoint coordinates at 75°.

The examples in this article apply to *active rotations* of vectors *counterclockwise* in a *right-handed coordinate system* (y counterclockwise from x) by *pre-multiplication* (the rotation matrix R applied on the left of the column vector **v** to be rotated). If any one of these is changed (such as rotating axes instead of vectors, a *passive transformation*), then the inverse of the example matrix should be used, which coincides with its transpose.

Since matrix multiplication has no effect on the zero vector (the coordinates of the origin), rotation matrices describe rotations about the origin. Rotation matrices provide an algebraic description of such rotations, and are used extensively for computations in geometry, physics, and computer graphics. In some literature, the term *rotation* is generalized to include improper rotations, characterized by orthogonal matrices with a determinant of −1 (instead of +1). An improper rotation combines a *proper* rotation with *reflections* (which invert orientation). In other cases, where reflections are not being considered, the label *proper* may be dropped. The latter convention is followed in this article.

Rotation matrices are square matrices, with real entries. More specifically, they can be characterized as orthogonal matrices with determinant 1; that is, a square matrix *R* is a rotation matrix if and only if *R*T = *R*−1 and det *R* = 1. The set of all orthogonal matrices of size n with determinant +1 is a representation of a group known as the special orthogonal group SO(*n*), one example of which is the rotation group SO(3). The set of all orthogonal matrices of size n with determinant +1 or −1 is a representation of the (general) orthogonal group O(*n*).


## In two dimensions

In two dimensions, the standard rotation matrix has the following form: $R(\theta )={\begin{bmatrix}\cos \theta &-\sin \theta \\\sin \theta &\cos \theta \\\end{bmatrix}}.$

This rotates column vectors by means of the following matrix multiplication, ${\begin{bmatrix}x'\\y'\\\end{bmatrix}}={\begin{bmatrix}\cos \theta &-\sin \theta \\\sin \theta &\cos \theta \\\end{bmatrix}}{\begin{bmatrix}x\\y\\\end{bmatrix}}.$

Thus, the new coordinates (*x*′, *y*′) of a point (*x*, *y*) after rotation are ${\begin{aligned}x'&=x\cos \theta -y\sin \theta \,\\y'&=x\sin \theta +y\cos \theta \,\end{aligned}}.$

### Examples

For example, when the vector (initially aligned with the *x*-axis of the Cartesian coordinate system) $\mathbf {\hat {x}} ={\begin{bmatrix}1\\0\\\end{bmatrix}}$ is rotated by an angle θ, its new coordinates are ${\begin{bmatrix}\cos \theta \\\sin \theta \\\end{bmatrix}},$

and when the vector (initially aligned with the *y*-axis of the coordinate system) $\mathbf {\hat {y}} ={\begin{bmatrix}0\\1\\\end{bmatrix}}$ is rotated by an angle θ, its new coordinates are ${\begin{bmatrix}-\sin \theta \\\cos \theta \\\end{bmatrix}}.$

### Sense

The sense or "direction" of vector rotation (not to be confused with the vector direction) is counterclockwise if θ is positive (e.g. 90°), and clockwise if θ is negative (e.g. −90°) for $R(\theta )$ . Thus the clockwise rotation matrix is found as (by replacing θ with -θ and using the trigonometric symmetry of ${\textstyle \sin(-\theta )=-\sin(\theta )}$ and ${\textstyle \cos(-\theta )=\cos(\theta )}$ ) $R(-\theta )={\begin{bmatrix}\cos \theta &\sin \theta \\-\sin \theta &\cos \theta \\\end{bmatrix}}.$

An alternative convention uses rotating axes (instead of rotating a vector), and the above matrices also represent a rotation of the *axes clockwise* through an angle θ.

The two-dimensional case is the only non-trivial case where the rotation matrices group is commutative; it does not matter in which order rotations are multiply performed. For the 3-dimensional case, for example, a different order of multiple rotations gives a different result (e.g., rotating cell phones along the *z*-axis then the *y*-axis is not equal to rotating them along the *y*-axis then the *z*-axis.)

### Non-standard orientation of the coordinate system

If a standard right-handed Cartesian coordinate system is used, with the x-axis to the right and the y-axis up, the rotation *R*(*θ*) is counterclockwise. If a left-handed Cartesian coordinate system is used, with x directed to the right but y directed down, *R*(*θ*) is clockwise. Such non-standard orientations are rarely used in mathematics but are common in 2D computer graphics, which often have the origin in the top left corner and the y-axis down the screen or page.

See below for other alternative conventions which may change the sense of the rotation produced by a rotation matrix.

### Common 2D rotations

Matrices ${\begin{bmatrix}1&0\\[3pt]0&1\\\end{bmatrix}},\quad {\begin{bmatrix}0&-1\\[3pt]1&0\\\end{bmatrix}},\quad {\begin{bmatrix}-1&0\\[3pt]0&-1\\\end{bmatrix}},\quad {\begin{bmatrix}0&1\\[3pt]-1&0\\\end{bmatrix}}$ are 2D rotation matrices corresponding to counter-clockwise rotations of respective angles of 0°, 90°, 180°, and 270°.

### Relationship with complex plane

The matrices of the shape ${\begin{bmatrix}x&-y\\y&x\end{bmatrix}}$ form a ring, since their set is closed under addition and multiplication. Since ${\begin{bmatrix}0&-1\\1&0\end{bmatrix}}^{2}\ =\ {\begin{bmatrix}-1&0\\0&-1\end{bmatrix}}\ =-I$ (where ${\textstyle I}$ is the identity matrix), the map ${\begin{bmatrix}x&-y\\y&x\end{bmatrix}}=x{\begin{bmatrix}1&0\\0&1\end{bmatrix}}+y{\begin{bmatrix}0&-1\\1&0\end{bmatrix}}\mapsto x+iy$ (where ${\begin{bmatrix}0&-1\\1&0\end{bmatrix}}$ corresponds to i ) is a ring isomorphism from this ring to the field of the complex numbers ⁠ $\mathbb {C}$ ⁠ (incidentally, this shows that this ring is a field). Under this isomorphism, the rotation matrices ${\begin{bmatrix}\cos t&-\sin t\\\sin t&\cos t\\\end{bmatrix}}=\cos t{\begin{bmatrix}1&0\\0&1\end{bmatrix}}+\sin t{\begin{bmatrix}0&-1\\1&0\end{bmatrix}}$ correspond to the circle of the unit complex numbers, the complex numbers of modulus 1, since $\cos t^{2}+\sin t^{2}=1$ . As a result, the following equality holds, $e^{it}=\cos t+i\sin t=\cos t{\begin{bmatrix}1&0\\0&1\end{bmatrix}}+\sin t{\begin{bmatrix}0&-1\\1&0\end{bmatrix}}={\begin{pmatrix}\cos t&-\sin t\\\sin t&\cos t\end{pmatrix}}$ where the first equality is Euler's formula, the matrix $I={\begin{bmatrix}1&0\\0&1\end{bmatrix}}$ corresponds to 1, and the matrix ${\begin{bmatrix}0&-1\\1&0\end{bmatrix}}$ corresponds to the imaginary unit ${\textstyle i}$ .

If one identifies $\mathbb {R} ^{2}$ with $\mathbb {C}$ through the linear isomorphism $(a,b)\mapsto a+ib$ , where $(a,b)\in \mathbb {R} ^{2}$ and $a+ib\in \mathbb {C}$ , the action of a matrix ${\begin{bmatrix}x&-y\\y&x\end{bmatrix}}$ on a vector $(a,b)$ corresponds to multiplication on the complex number $a+ib$ by *x* + *iy*. In other words, a vector rotation corresponds to multiplication on a complex number (corresponding to the vector being rotated) by a complex number of modulus 1 (corresponding to the rotation matrix).


## In three dimensions

### Basic 3D rotations

A basic 3D rotation (also called elemental rotation) is a rotation about one of the axes of a coordinate system. The following three basic rotation matrices rotate vectors by an angle θ about the x-, y-, or z-axis, in three dimensions, using the right-hand rule—which codifies their alternating signs. Notice that the right-hand rule only works when multiplying $R\cdot {\vec {x}}$ . The same matrices can also represent a clockwise rotation of the axes keeping the vectors unchanged.

${\begin{alignedat}{1}R_{x}(\theta )&={\begin{bmatrix}1&0&0\\0&\cos \theta &-\sin \theta \\[3pt]0&\sin \theta &\cos \theta \\[3pt]\end{bmatrix}}\\[6pt]R_{y}(\theta )&={\begin{bmatrix}\cos \theta &0&\sin \theta \\[3pt]0&1&0\\[3pt]-\sin \theta &0&\cos \theta \\\end{bmatrix}}\\[6pt]R_{z}(\theta )&={\begin{bmatrix}\cos \theta &-\sin \theta &0\\[3pt]\sin \theta &\cos \theta &0\\[3pt]0&0&1\\\end{bmatrix}}\end{alignedat}}$

For column vectors, each of these basic vector rotations appears counterclockwise when the axis about which they occur points toward the observer, the coordinate system is right-handed, and the angle θ is positive. *R**z*, for instance, would rotate toward the *y*-axis a vector aligned with the *x*-axis, as can easily be checked by operating with *R**z* on the vector (1,0,0): $R_{z}(90^{\circ }){\begin{bmatrix}1\\0\\0\\\end{bmatrix}}={\begin{bmatrix}\cos 90^{\circ }&-\sin 90^{\circ }&0\\\sin 90^{\circ }&\quad \cos 90^{\circ }&0\\0&0&1\\\end{bmatrix}}{\begin{bmatrix}1\\0\\0\\\end{bmatrix}}={\begin{bmatrix}0&-1&0\\1&0&0\\0&0&1\\\end{bmatrix}}{\begin{bmatrix}1\\0\\0\\\end{bmatrix}}={\begin{bmatrix}0\\1\\0\\\end{bmatrix}}$

This is similar to the rotation produced by the above-mentioned two-dimensional rotation matrix. See below for alternative conventions which may apparently or actually invert the sense of the rotation produced by these matrices.

### General 3D rotations

Other 3D rotation matrices can be obtained from these three using matrix multiplication. For example, the product ${\begin{aligned}R=R_{z}(\alpha )\,R_{y}(\beta )\,R_{x}(\gamma )&={\overset {\text{yaw}}{\begin{bmatrix}\cos \alpha &-\sin \alpha &0\\\sin \alpha &\cos \alpha &0\\0&0&1\\\end{bmatrix}}}{\overset {\text{pitch}}{\begin{bmatrix}\cos \beta &0&\sin \beta \\0&1&0\\-\sin \beta &0&\cos \beta \\\end{bmatrix}}}{\overset {\text{roll}}{\begin{bmatrix}1&0&0\\0&\cos \gamma &-\sin \gamma \\0&\sin \gamma &\cos \gamma \\\end{bmatrix}}}\\&={\begin{bmatrix}\cos \alpha \cos \beta &\cos \alpha \sin \beta \sin \gamma -\sin \alpha \cos \gamma &\cos \alpha \sin \beta \cos \gamma +\sin \alpha \sin \gamma \\\sin \alpha \cos \beta &\sin \alpha \sin \beta \sin \gamma +\cos \alpha \cos \gamma &\sin \alpha \sin \beta \cos \gamma -\cos \alpha \sin \gamma \\-\sin \beta &\cos \beta \sin \gamma &\cos \beta \cos \gamma \\\end{bmatrix}}\end{aligned}}$

represents a rotation whose yaw, pitch, and roll angles are α, β and γ, respectively. More formally, it is an intrinsic rotation whose Tait–Bryan angles are α, β, γ, about axes z, y, x, respectively. Similarly, the product ${\begin{aligned}\\R=R_{x}(\alpha )\,R_{y}(\beta )\,R_{z}(\gamma )&={\overset {\text{roll}}{\begin{bmatrix}1&0&0\\0&\cos \alpha &-\sin \alpha \\0&\sin \alpha &\cos \alpha \\\end{bmatrix}}}{\overset {\text{pitch}}{\begin{bmatrix}\cos \beta &0&\sin \beta \\0&1&0\\-\sin \beta &0&\cos \beta \\\end{bmatrix}}}{\overset {\text{yaw}}{\begin{bmatrix}\cos \gamma &-\sin \gamma &0\\\sin \gamma &\cos \gamma &0\\0&0&1\\\end{bmatrix}}}\\&={\begin{bmatrix}\cos \beta \cos \gamma &-\cos \beta \sin \gamma &\sin \beta \\\cos \alpha \sin \gamma +\sin \alpha \sin \beta \cos \gamma &\cos \alpha \cos \gamma -\sin \alpha \sin \beta \sin \gamma &-\sin \alpha \cos \beta \\\sin \alpha \sin \gamma -\cos \alpha \sin \beta \cos \gamma &\sin \alpha \cos \gamma +\cos \alpha \sin \beta \sin \gamma &\cos \alpha \cos \beta \\\end{bmatrix}}\end{aligned}}$ represents an extrinsic rotation whose (improper) Euler angles are α, β, γ, about axes x, y, z.

These matrices produce the desired effect only if they are used to premultiply column vectors, and (since in general matrix multiplication is not commutative) only if they are applied in the specified order (see Ambiguities for more details). The order of rotation operations is from right to left; the matrix adjacent to the column vector is the first to be applied, and then the one to the left.

### Conversion from rotation matrix to axis–angle

Every rotation in three dimensions is defined by its **axis** (a vector along this axis is unchanged by the rotation), and its **angle** — the amount of rotation about that axis (Euler rotation theorem).

There are several methods to compute the axis and angle from a rotation matrix (see also axis–angle representation). Here, we only describe the method based on the computation of the eigenvectors and eigenvalues of the rotation matrix. It is also possible to use the trace of the rotation matrix.

#### Determining the axis

Given a 3 × 3 rotation matrix R, a vector **u** parallel to the rotation axis must satisfy $R\mathbf {u} =\mathbf {u} ,$ since the rotation of **u** around the rotation axis must result in **u**. The equation above may be solved for **u** which is unique up to a scalar factor unless R is the identity matrix I.

Further, the equation may be rewritten $R\mathbf {u} =I\mathbf {u} \implies \left(R-I\right)\mathbf {u} =0,$ which shows that **u** lies in the null space of *R* − *I*.

This means precisely that that **u** is an eigenvector of R corresponding to the eigenvalue *λ* = 1. Every rotation matrix must have this eigenvalue, the other two eigenvalues being complex conjugates of each other. It follows that a general rotation matrix in three dimensions has, up to a multiplicative constant, only one real eigenvector.

One way to determine the rotation axis is by showing that:

${\begin{aligned}0&=R^{\mathsf {T}}0+0\\&=R^{\mathsf {T}}\left(R-I\right)\mathbf {u} +\left(R-I\right)\mathbf {u} \\&=\left(R^{\mathsf {T}}R-R^{\mathsf {T}}+R-I\right)\mathbf {u} \\&=\left(I-R^{\mathsf {T}}+R-I\right)\mathbf {u} \\&=\left(R-R^{\mathsf {T}}\right)\mathbf {u} \end{aligned}}$

Since (*R* − *R*T) is a skew-symmetric matrix, we can choose **u** such that $[\mathbf {u} ]_{\times }=\left(R-R^{\mathsf {T}}\right).$ The matrix–vector product becomes a cross product of a vector with itself, ensuring that the result is zero:

$\left(R-R^{\mathsf {T}}\right)\mathbf {u} =[\mathbf {u} ]_{\times }\mathbf {u} =\mathbf {u} \times \mathbf {u} =0\,$

Therefore, if $R={\begin{bmatrix}a&b&c\\d&e&f\\g&h&i\\\end{bmatrix}},$ then $\mathbf {u} ={\begin{bmatrix}h-f\\c-g\\d-b\\\end{bmatrix}}.$ The magnitude of **u** computed this way is ‖**u**‖ = 2 sin *θ*, where θ is the angle of rotation.

This **does not work** if R is symmetric. Above, if *R* − *R*T is zero, then all subsequent steps are invalid. In this case, the angle of rotation is 0° or 180° and any nonzero column of *I* + *R* is an eigenvector of R with eigenvalue 1 because *R*(*I* + *R*) = *R* + *R*2 = *R* + *RR*T = *I* + *R*.

#### Determining the angle

To find the angle of a rotation, once the axis of the rotation is known, select a vector **v** perpendicular to the axis. Then the angle of the rotation is the angle between **v** and *R***v**.

A more direct method, however, is to simply calculate the **trace**: the sum of the diagonal elements of the rotation matrix. Care should be taken to select the right sign for the angle θ to match the chosen axis: $\operatorname {tr} (R)=1+2\cos \theta ,$

from which follows that the angle's absolute value is $|\theta |=\arccos \left({\frac {\operatorname {tr} (R)-1}{2}}\right).$

For the rotation axis $\mathbf {n} =(n_{1},n_{2},n_{3})$ , you can get the correct angle from

$\left\{{\begin{matrix}\cos \theta &=&{\dfrac {\operatorname {tr} (R)-1}{2}}\\\sin \theta &=&-{\dfrac {\operatorname {tr} (K_{n}R)}{2}}\end{matrix}}\right.$

where

$K_{n}={\begin{bmatrix}0&-n_{3}&n_{2}\\n_{3}&0&-n_{1}\\-n_{2}&n_{1}&0\\\end{bmatrix}}$

#### Rotation matrix from axis and angle

The matrix of a proper rotation R by angle θ around the axis **u** = (*ux*, *uy*, *uz*), a unit vector with *u*2 *x* + *u*2 *y* + *u*2 *z* = 1, is given by: $R={\begin{bmatrix}u_{x}^{2}\left(1-\cos \theta \right)+\cos \theta &u_{x}u_{y}\left(1-\cos \theta \right)-u_{z}\sin \theta &u_{x}u_{z}\left(1-\cos \theta \right)+u_{y}\sin \theta \\u_{x}u_{y}\left(1-\cos \theta \right)+u_{z}\sin \theta &u_{y}^{2}\left(1-\cos \theta \right)+\cos \theta &u_{y}u_{z}\left(1-\cos \theta \right)-u_{x}\sin \theta \\u_{x}u_{z}\left(1-\cos \theta \right)-u_{y}\sin \theta &u_{y}u_{z}\left(1-\cos \theta \right)+u_{x}\sin \theta &u_{z}^{2}\left(1-\cos \theta \right)+\cos \theta \end{bmatrix}}.$

A derivation of this matrix from first principles can be found in section 9.2 here. The basic idea to derive this matrix is dividing the problem into few known simple steps.

1. First rotate the given axis and the point such that the axis lies in one of the coordinate planes (xy, yz or zx)
2. Then rotate the given axis and the point such that the axis is aligned with one of the two coordinate axes for that particular coordinate plane (x, y or z)
3. Use one of the fundamental rotation matrices to rotate the point depending on the coordinate axis with which the rotation axis is aligned.
4. Reverse rotate the axis-point pair such that it attains the final configuration as that was in step 2 (Undoing step 2)
5. Reverse rotate the axis-point pair which was done in step 1 (undoing step 1)

This can be written more concisely as $R=(\cos \theta )\,I+(\sin \theta )\,[\mathbf {u} ]_{\times }+(1-\cos \theta )\,(\mathbf {u} \otimes \mathbf {u} ),$ where [**u**]× is the cross product matrix of **u**; the expression **u** ⊗ **u** is the outer product, and I is the identity matrix. Alternatively, the matrix entries are: $R_{jk}={\begin{cases}\cos ^{2}{\frac {\theta }{2}}+\sin ^{2}{\frac {\theta }{2}}\left(2u_{j}^{2}-1\right),\quad &{\text{if }}j=k\\2u_{j}u_{k}\sin ^{2}{\frac {\theta }{2}}-\varepsilon _{jkl}u_{l}\sin \theta ,\quad &{\text{if }}j\neq k\end{cases}}$

where εjkl is the Levi-Civita symbol with *ε*123 = 1. This is a matrix form of Rodrigues' rotation formula, (or the equivalent, differently parametrized Euler–Rodrigues formula) with

$\mathbf {u} \otimes \mathbf {u} =\mathbf {u} \mathbf {u} ^{\mathsf {T}}={\begin{bmatrix}u_{x}^{2}&u_{x}u_{y}&u_{x}u_{z}\\[3pt]u_{x}u_{y}&u_{y}^{2}&u_{y}u_{z}\\[3pt]u_{x}u_{z}&u_{y}u_{z}&u_{z}^{2}\end{bmatrix}},\qquad [\mathbf {u} ]_{\times }={\begin{bmatrix}0&-u_{z}&u_{y}\\[3pt]u_{z}&0&-u_{x}\\[3pt]-u_{y}&u_{x}&0\end{bmatrix}}.$

In $\mathbb {R} ^{3}$ the rotation of a vector **x** around the axis **u** by an angle θ can be written as: $R_{\mathbf {u} }(\theta )\mathbf {x} =\mathbf {u} (\mathbf {u} \cdot \mathbf {x} )+\cos \left(\theta \right)(\mathbf {u} \times \mathbf {x} )\times \mathbf {u} +\sin \left(\theta \right)(\mathbf {u} \times \mathbf {x} )$

or equivalently: $R_{\mathbf {u} }(\theta )\mathbf {x} =\mathbf {x} \cos(\theta )+\mathbf {u} (\mathbf {x} \cdot \mathbf {u} )(1-\cos(\theta ))-\mathbf {x} \times \mathbf {u} \sin {\theta }$

This can also be written in tensor notation as: $(R_{\mathbf {u} }(\theta )\mathbf {x} )_{i}=(R_{\mathbf {u} }(\theta ))_{ij}{\mathbf {x} }_{j}\quad {\text{with}}\quad (R_{\mathbf {u} }(\theta ))_{ij}=\delta _{ij}\cos(\theta )+\mathbf {u} _{i}\mathbf {u} _{j}(1-\cos(\theta ))-\sin {\theta }\varepsilon _{ijk}\mathbf {u} _{k}$

If the 3D space is right-handed and *θ* > 0, this rotation will be counterclockwise when **u** points towards the observer (Right-hand rule). Explicitly, with $({\boldsymbol {\alpha }},{\boldsymbol {\beta }},\mathbf {u} )$ a right-handed orthonormal basis, $R_{\mathbf {u} }(\theta ){\boldsymbol {\alpha }}=\cos \left(\theta \right){\boldsymbol {\alpha }}+\sin \left(\theta \right){\boldsymbol {\beta }},\quad R_{\mathbf {u} }(\theta ){\boldsymbol {\beta }}=-\sin \left(\theta \right){\boldsymbol {\alpha }}+\cos \left(\theta \right){\boldsymbol {\beta }},\quad R_{\mathbf {u} }(\theta )\mathbf {u} =\mathbf {u} .$

Note the striking *merely apparent differences* to the *equivalent* Lie-algebraic formulation below.


## Properties

For any n-dimensional rotation matrix R acting on $\mathbb {R} ^{n},$

$R^{\mathsf {T}}=R^{-1}$

(The rotation is an

orthogonal matrix

)

$\det R=\pm 1$

A rotation is termed proper if det *R* = 1, and improper (or a roto-reflection) if det *R* = –1. For even dimensions *n* = 2*k*, the n eigenvalues λ of a proper rotation occur as pairs of complex conjugates which are roots of unity: *λ* = *e*±*iθj* for *j* = 1, ..., *k*, which is real only for *λ* = ±1. Therefore, there may be no vectors fixed by the rotation (*λ* = 1), and thus no axis of rotation. Any fixed eigenvectors occur in pairs, and the axis of rotation is an even-dimensional subspace.

For odd dimensions *n* = 2*k* + 1, a proper rotation R will have an odd number of eigenvalues, with at least one *λ* = 1 and the axis of rotation will be an odd dimensional subspace. Proof:

${\begin{aligned}\det \left(R-I\right)&=\det \left(R^{\mathsf {T}}\right)\det \left(R-I\right)=\det \left(R^{\mathsf {T}}R-R^{\mathsf {T}}\right)=\det \left(I-R^{\mathsf {T}}\right)\\&=\det(I-R)=\left(-1\right)^{n}\det \left(R-I\right)=-\det \left(R-I\right).\end{aligned}}$

Here I is the identity matrix, and we use det(*R*T) = det(*R*) = 1, as well as (−1)*n* = −1 since n is odd. Therefore, det(*R* – *I*) = 0, meaning there is a nonzero vector **v** with (*R – I*)**v** = 0, that is *R***v** = **v**, a fixed eigenvector. There may also be pairs of fixed eigenvectors in the even-dimensional subspace orthogonal to **v**, so the total dimension of fixed eigenvectors is odd.

For example, in 2-space *n* = 2, a rotation by angle θ has eigenvalues *λ* = *eiθ* and *λ* = *e*−*iθ*, so there is no axis of rotation except when *θ* = 0, the case of the null rotation. In 3-space *n* = 3, the axis of a non-null proper rotation is always a unique line, and a rotation around this axis by angle θ has eigenvalues *λ* = 1, *eiθ*, *e*−*iθ*. In 4-space *n* = 4, the four eigenvalues are of the form *e*±*iθ*, *e*±*iφ*. The null rotation has *θ* = *φ* = 0. The case of *θ* = 0, *φ* ≠ 0 is called a *simple rotation*, with two unit eigenvalues forming an *axis plane*, and a two-dimensional rotation orthogonal to the axis plane. Otherwise, there is no axis plane. The case of *θ* = *φ* is called an *isoclinic rotation*, having eigenvalues *e*±*iθ* repeated twice, so every vector is rotated through an angle θ.

The trace of a rotation matrix is equal to the sum of its eigenvalues. For *n* = 2, a rotation by angle θ has trace 2 cos *θ*. For *n* = 3, a rotation around any axis by angle θ has trace 1 + 2 cos *θ*. For *n* = 4, and the trace is 2(cos *θ* + cos *φ*), which becomes 4 cos *θ* for an isoclinic rotation.


## Examples

| The 2 × 2 rotation matrix $Q={\begin{bmatrix}0&1\\-1&0\end{bmatrix}}$ corresponds to a 90° planar rotation clockwise about the origin. The transpose of the 2 × 2 matrix $M={\begin{bmatrix}0.936&0.352\\0.352&-0.936\end{bmatrix}}$ is its inverse, but since its determinant is −1, this is not a proper rotation matrix; it is a reflection across the line 11*y* = 2*x*. The 3 × 3 rotation matrix $Q={\begin{bmatrix}1&0&0\\0&{\frac {\sqrt {3}}{2}}&{\frac {1}{2}}\\0&-{\frac {1}{2}}&{\frac {\sqrt {3}}{2}}\end{bmatrix}}={\begin{bmatrix}1&0&0\\0&\cos 30^{\circ }&\sin 30^{\circ }\\0&-\sin 30^{\circ }&\cos 30^{\circ }\\\end{bmatrix}}$ corresponds to a −30° rotation around the x-axis in three-dimensional space. The 3 × 3 rotation matrix $Q={\begin{bmatrix}0.36&0.48&-0.80\\-0.80&0.60&0.00\\0.48&0.64&0.60\end{bmatrix}}$ corresponds to a rotation of approximately −74° around the axis (−⁠1/2⁠,1,1) in three-dimensional space. The 3 × 3 permutation matrix $P={\begin{bmatrix}0&0&1\\1&0&0\\0&1&0\end{bmatrix}}$ is a rotation matrix, as is the matrix of any even permutation, and rotates through 120° about the axis *x* = *y* = *z*. | The 3 × 3 matrix $M={\begin{bmatrix}3&-4&1\\5&3&-7\\-9&2&6\end{bmatrix}}$ has determinant +1, but is not orthogonal (its transpose is not its inverse), so it is not a rotation matrix. The 4 × 3 matrix $M={\begin{bmatrix}0.5&-0.1&0.7\\0.1&0.5&-0.5\\-0.7&0.5&0.5\\-0.5&-0.7&-0.1\end{bmatrix}}$ is not square, and so cannot be a rotation matrix; yet *M*T*M* yields a 3 × 3 identity matrix (the columns are orthonormal). The 4 × 4 matrix $Q=-I={\begin{bmatrix}-1&0&0&0\\0&-1&0&0\\0&0&-1&0\\0&0&0&-1\end{bmatrix}}$ describes an isoclinic rotation in four dimensions, a rotation through equal angles (180°) through two orthogonal planes. The 5 × 5 rotation matrix $Q={\begin{bmatrix}0&-1&0&0&0\\1&0&0&0&0\\0&0&-1&0&0\\0&0&0&-1&0\\0&0&0&0&1\end{bmatrix}}$ rotates vectors in the plane of the first two coordinate axes 90°, rotates vectors in the plane of the next two axes 180°, and leaves the last coordinate axis unmoved. |
|---|---|


## Geometry

In Euclidean geometry, a rotation is an example of an isometry, a transformation that moves points without changing the distances between them. Rotations are distinguished from other isometries by two additional properties: they leave (at least) one point fixed, and they leave "handedness" unchanged. In contrast, a translation moves every point, a reflection exchanges left- and right-handed ordering, a glide reflection does both, and an improper rotation combines a change in handedness with a normal rotation.

If a fixed point is taken as the origin of a Cartesian coordinate system, then every point can be given coordinates as a displacement from the origin. Thus one may work with the vector space of displacements instead of the points themselves. Now suppose (*p*1, ..., *pn*) are the coordinates of the vector **p** from the origin O to point P. Choose an orthonormal basis for our coordinates; then the squared distance to P, by Pythagoras, is $d^{2}(O,P)=\|\mathbf {p} \|^{2}=\sum _{r=1}^{n}p_{r}^{2}$ which can be computed using the matrix multiplication $\|\mathbf {p} \|^{2}={\begin{bmatrix}p_{1}\cdots p_{n}\end{bmatrix}}{\begin{bmatrix}p_{1}\\\vdots \\p_{n}\end{bmatrix}}=\mathbf {p} ^{\mathsf {T}}\mathbf {p} .$

A geometric rotation transforms lines to lines, and preserves ratios of distances between points. From these properties it can be shown that a rotation is a linear transformation of the vectors, and thus can be written in matrix form, *Q***p**. The fact that a rotation preserves, not just ratios, but distances themselves, is stated as $\mathbf {p} ^{\mathsf {T}}\mathbf {p} =(Q\mathbf {p} )^{\mathsf {T}}(Q\mathbf {p} ),$ or ${\begin{aligned}\mathbf {p} ^{\mathsf {T}}I\mathbf {p} &{}=\left(\mathbf {p} ^{\mathsf {T}}Q^{\mathsf {T}}\right)(Q\mathbf {p} )\\&{}=\mathbf {p} ^{\mathsf {T}}\left(Q^{\mathsf {T}}Q\right)\mathbf {p} .\end{aligned}}$ Because this equation holds for all vectors, **p**, one concludes that every rotation matrix, *Q*, satisfies the **orthogonality condition**, $Q^{\mathsf {T}}Q=I.$ Rotations preserve handedness because they cannot change the ordering of the axes, which implies the **special matrix** condition, $\det Q=+1.$ Equally important, it can be shown that any matrix satisfying these two conditions acts as a rotation.


## Multiplication

The inverse of a rotation matrix is its transpose, which is also a rotation matrix: ${\begin{aligned}\left(Q^{\mathsf {T}}\right)^{\mathsf {T}}\left(Q^{\mathsf {T}}\right)&=QQ^{\mathsf {T}}=I\\\det Q^{\mathsf {T}}&=\det Q=+1.\end{aligned}}$ The product of two rotation matrices is a rotation matrix: ${\begin{aligned}\left(Q_{1}Q_{2}\right)^{\mathsf {T}}\left(Q_{1}Q_{2}\right)&=Q_{2}^{\mathsf {T}}\left(Q_{1}^{\mathsf {T}}Q_{1}\right)Q_{2}=I\\\det \left(Q_{1}Q_{2}\right)&=\left(\det Q_{1}\right)\left(\det Q_{2}\right)=+1.\end{aligned}}$ For *n* > 2, multiplication of *n* × *n* rotation matrices is generally not commutative. ${\begin{aligned}Q_{1}&={\begin{bmatrix}0&-1&0\\1&0&0\\0&0&1\end{bmatrix}}&Q_{2}&={\begin{bmatrix}0&0&1\\0&1&0\\-1&0&0\end{bmatrix}}\\Q_{1}Q_{2}&={\begin{bmatrix}0&-1&0\\0&0&1\\-1&0&0\end{bmatrix}}&Q_{2}Q_{1}&={\begin{bmatrix}0&0&1\\1&0&0\\0&1&0\end{bmatrix}}.\end{aligned}}$ Noting that any identity matrix is a rotation matrix, and that matrix multiplication is associative, we may summarize all these properties by saying that the *n* × *n* rotation matrices form a group, which for *n* > 2 is non-abelian, called a special orthogonal group, and denoted by SO(*n*), SO(*n*,**R**), SO*n*, or SO*n*(**R**), the group of *n* × *n* rotation matrices is isomorphic to the group of rotations in an *n*-dimensional space. This means that multiplication of rotation matrices corresponds to composition of rotations, applied in left-to-right order of their corresponding matrices.


## Ambiguities

The interpretation of a rotation matrix can be subject to many ambiguities.

In most cases the effect of the ambiguity is equivalent to the effect of a rotation matrix inversion (for these orthogonal matrices equivalently matrix transpose).

**Alias or alibi (passive or active) transformation**

The coordinates of a point

P

may change due to either a rotation of the coordinate system

CS

(

alias

), or a rotation of the point

P

(

alibi

). In the latter case, the rotation of

P

also produces a rotation of the vector

v

representing

P

. In other words, either

P

and

v

are fixed while

CS

rotates (alias), or

CS

is fixed while

P

and

v

rotate (alibi). Any given rotation can be legitimately described both ways, as vectors and coordinate systems actually rotate with respect to each other, about the same axis but in opposite directions. Throughout this article, we chose the alibi approach to describe rotations. For instance,

$R(\theta )={\begin{bmatrix}\cos \theta &-\sin \theta \\\sin \theta &\cos \theta \\\end{bmatrix}}$

represents a counterclockwise rotation of a vector

v

by an angle

θ

, or a rotation of

CS

by the same angle but in the opposite direction (i.e. clockwise). Alibi and alias transformations are also known as

active and passive transformations

, respectively.

**Pre-multiplication or post-multiplication**

The same point

P

can be represented either by a

column vector

v

or a

row vector

w

. Rotation matrices can either pre-multiply column vectors (

R

v

), or post-multiply row vectors (

w

R

). However,

R

v

produces a rotation in the opposite direction with respect to

w

R

. Throughout this article, rotations produced on column vectors are described by means of a pre-multiplication. To obtain exactly the same rotation (i.e. the same final coordinates of point

P

), the equivalent row vector must be post-multiplied by the

transpose

of

R

(i.e.

w

R

T

).

**Right- or left-handed coordinates**

The matrix and the vector can be represented with respect to a

right-handed

or left-handed coordinate system. Throughout the article, we assumed a right-handed orientation, unless otherwise specified.

**Vectors or forms**

The vector space has a

dual space

of

linear forms

, and the matrix can act on either vectors or forms.


## Decompositions

### Independent planes

Consider the 3 × 3 rotation matrix $Q={\begin{bmatrix}0.36&0.48&-0.80\\-0.80&0.60&0.00\\0.48&0.64&0.60\end{bmatrix}}.$ If *Q* acts in a certain direction, **v**, purely as a scaling by a factor λ, then we have $Q\mathbf {v} =\lambda \mathbf {v} ,$ so that $\mathbf {0} =(\lambda I-Q)\mathbf {v} .$ Thus λ is a root of the characteristic polynomial for Q, ${\begin{aligned}0&{}=\det(\lambda I-Q)\\&{}=\lambda ^{3}-{\tfrac {39}{25}}\lambda ^{2}+{\tfrac {39}{25}}\lambda -1\\&{}=(\lambda -1)\left(\lambda ^{2}-{\tfrac {14}{25}}\lambda +1\right).\end{aligned}}$ Two features are noteworthy. First, one of the roots (or eigenvalues) is 1, which tells us that some direction is unaffected by the matrix. For rotations in three dimensions, this is the *axis* of the rotation (a concept that has no meaning in any other dimension). Second, the other two roots are a pair of complex conjugates, whose product is 1 (the constant term of the quadratic), and whose sum is 2 cos *θ* (the negated linear term). This factorization is of interest for 3 × 3 rotation matrices because the same thing occurs for all of them. (As special cases, for a null rotation the "complex conjugates" are both 1, and for a 180° rotation they are both −1.) Furthermore, a similar factorization holds for any *n* × *n* rotation matrix. If the dimension, n, is odd, there will be a "dangling" eigenvalue of 1; and for any dimension the rest of the polynomial factors into quadratic terms like the one here (with the two special cases noted). We are guaranteed that the characteristic polynomial will have degree n and thus n eigenvalues. And since a rotation matrix commutes with its transpose, it is a normal matrix, so can be diagonalized. We conclude that every rotation matrix, when expressed in a suitable coordinate system, partitions into independent rotations of two-dimensional subspaces, at most ⁠*n*/2⁠ of them.

The sum of the entries on the main diagonal of a matrix is called the trace; it does not change if we reorient the coordinate system, and always equals the sum of the eigenvalues. This has the convenient implication for 2 × 2 and 3 × 3 rotation matrices that the trace reveals the angle of rotation, θ, in the two-dimensional space (or subspace). For a 2 × 2 matrix the trace is 2 cos *θ*, and for a 3 × 3 matrix it is 1 + 2 cos *θ*. In the three-dimensional case, the subspace consists of all vectors perpendicular to the rotation axis (the invariant direction, with eigenvalue 1). Thus we can extract from any 3 × 3 rotation matrix a rotation axis and an angle, and these completely determine the rotation.

### Sequential angles

The constraints on a 2 × 2 rotation matrix imply that it must have the form $Q={\begin{bmatrix}a&-b\\b&a\end{bmatrix}}$ with *a*2 + *b*2 = 1. Therefore, we may set *a* = cos *θ* and *b* = sin *θ*, for some angle θ. To solve for θ it is not enough to look at a alone or b alone; we must consider both together to place the angle in the correct quadrant, using a two-argument arctangent function.

Now consider the first column of a 3 × 3 rotation matrix, ${\begin{bmatrix}a\\b\\c\end{bmatrix}}.$ Although *a*2 + *b*2 will probably not equal 1, but some value *r*2 < 1, we can use a slight variation of the previous computation to find a so-called Givens rotation that transforms the column to ${\begin{bmatrix}r\\0\\c\end{bmatrix}},$ zeroing b. This acts on the subspace spanned by the x- and y-axes. We can then repeat the process for the xz-subspace to zero c. Acting on the full matrix, these two rotations produce the schematic form $Q_{xz}Q_{xy}Q={\begin{bmatrix}1&0&0\\0&\ast &\ast \\0&\ast &\ast \end{bmatrix}}.$ Shifting attention to the second column, a Givens rotation of the yz-subspace can now zero the z value. This brings the full matrix to the form $Q_{yz}Q_{xz}Q_{xy}Q={\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix}},$ which is an identity matrix. Thus we have decomposed Q as $Q=Q_{xy}^{-1}Q_{xz}^{-1}Q_{yz}^{-1}.$

An *n* × *n* rotation matrix will have (*n* − 1) + (*n* − 2) + ⋯ + 2 + 1, or $\sum _{k=1}^{n-1}k={\frac {1}{2}}n(n-1)$ entries below the diagonal to zero. We can zero them by extending the same idea of stepping through the columns with a series of rotations in a fixed sequence of planes. We conclude that the set of *n* × *n* rotation matrices, each of which has *n*2 entries, can be parameterized by ⁠1/2⁠*n*(*n* − 1) angles.

| *xzx*w | *xzy*w | *xyx*w | *xyz*w |
|---|---|---|---|
| *yxy*w | *yxz*w | *yzy*w | *yzx*w |
| *zyz*w | *zyx*w | *zxz*w | *zxy*w |
| *xzx*b | *yzx*b | *xyx*b | *zyx*b |
| *yxy*b | *zxy*b | *yzy*b | *xzy*b |
| *zyz*b | *xyz*b | *zxz*b | *yxz*b |

In three dimensions this restates in matrix form an observation made by Euler, so mathematicians call the ordered sequence of three angles Euler angles. However, the situation is somewhat more complicated than we have so far indicated. Despite the small dimension, we actually have considerable freedom in the sequence of axis pairs we use; and we also have some freedom in the choice of angles. Thus we find many different conventions employed when three-dimensional rotations are parameterized for physics, or medicine, or chemistry, or other disciplines. When we include the option of world axes or body axes, 24 different sequences are possible. And while some disciplines call any sequence Euler angles, others give different names (Cardano, Tait–Bryan, roll-pitch-yaw) to different sequences.

One reason for the large number of options is that, as noted previously, rotations in three dimensions (and higher) do not commute. If we reverse a given sequence of rotations, we get a different outcome. This also implies that we cannot compose two rotations by adding their corresponding angles. Thus Euler angles are not vectors, despite a similarity in appearance as a triplet of numbers.

### Nested dimensions

A 3 × 3 rotation matrix such as $Q_{3\times 3}={\begin{bmatrix}\cos \theta &-\sin \theta &{\color {CadetBlue}0}\\\sin \theta &\cos \theta &{\color {CadetBlue}0}\\{\color {CadetBlue}0}&{\color {CadetBlue}0}&{\color {CadetBlue}1}\end{bmatrix}}$

suggests a 2 × 2 rotation matrix, $Q_{2\times 2}={\begin{bmatrix}\cos \theta &-\sin \theta \\\sin \theta &\cos \theta \end{bmatrix}},$

is embedded in the upper left corner: $Q_{3\times 3}=\left[{\begin{matrix}Q_{2\times 2}&\mathbf {0} \\\mathbf {0} ^{\mathsf {T}}&1\end{matrix}}\right].$

This is no illusion; not just one, but many, copies of n-dimensional rotations are found within (*n* + 1)-dimensional rotations, as subgroups. Each embedding leaves one direction fixed, which in the case of 3 × 3 matrices is the rotation axis. For example, we have ${\begin{aligned}Q_{\mathbf {x} }(\theta )&={\begin{bmatrix}{\color {CadetBlue}1}&{\color {CadetBlue}0}&{\color {CadetBlue}0}\\{\color {CadetBlue}0}&\cos \theta &-\sin \theta \\{\color {CadetBlue}0}&\sin \theta &\cos \theta \end{bmatrix}},\\[8px]Q_{\mathbf {y} }(\theta )&={\begin{bmatrix}\cos \theta &{\color {CadetBlue}0}&\sin \theta \\{\color {CadetBlue}0}&{\color {CadetBlue}1}&{\color {CadetBlue}0}\\-\sin \theta &{\color {CadetBlue}0}&\cos \theta \end{bmatrix}},\\[8px]Q_{\mathbf {z} }(\theta )&={\begin{bmatrix}\cos \theta &-\sin \theta &{\color {CadetBlue}0}\\\sin \theta &\cos \theta &{\color {CadetBlue}0}\\{\color {CadetBlue}0}&{\color {CadetBlue}0}&{\color {CadetBlue}1}\end{bmatrix}},\end{aligned}}$

fixing the x-axis, the y-axis, and the z-axis, respectively. The rotation axis need not be a coordinate axis; if **u** = (*x*,*y*,*z*) is a unit vector in the desired direction, then ${\begin{aligned}Q_{\mathbf {u} }(\theta )&={\begin{bmatrix}0&-z&y\\z&0&-x\\-y&x&0\end{bmatrix}}\sin \theta +\left(I-\mathbf {u} \mathbf {u} ^{\mathsf {T}}\right)\cos \theta +\mathbf {u} \mathbf {u} ^{\mathsf {T}}\\[8px]&={\begin{bmatrix}\left(1-x^{2}\right)c_{\theta }+x^{2}&-zs_{\theta }-xyc_{\theta }+xy&ys_{\theta }-xzc_{\theta }+xz\\zs_{\theta }-xyc_{\theta }+xy&\left(1-y^{2}\right)c_{\theta }+y^{2}&-xs_{\theta }-yzc_{\theta }+yz\\-ys_{\theta }-xzc_{\theta }+xz&xs_{\theta }-yzc_{\theta }+yz&\left(1-z^{2}\right)c_{\theta }+z^{2}\end{bmatrix}}\\[8px]&={\begin{bmatrix}x^{2}(1-c_{\theta })+c_{\theta }&xy(1-c_{\theta })-zs_{\theta }&xz(1-c_{\theta })+ys_{\theta }\\xy(1-c_{\theta })+zs_{\theta }&y^{2}(1-c_{\theta })+c_{\theta }&yz(1-c_{\theta })-xs_{\theta }\\xz(1-c_{\theta })-ys_{\theta }&yz(1-c_{\theta })+xs_{\theta }&z^{2}(1-c_{\theta })+c_{\theta }\end{bmatrix}},\end{aligned}}$

where *cθ* = cos *θ*, *sθ* = sin *θ*, is a rotation by angle θ leaving axis **u** fixed.

A direction in (*n* + 1)-dimensional space will be a unit magnitude vector, which we may consider a point on a generalized sphere, *S**n*. Thus it is natural to describe the rotation group SO(*n* + 1) as combining SO(*n*) and *S**n*. A suitable formalism is the fiber bundle, $SO(n)\hookrightarrow SO(n+1)\to S^{n},$

where for every direction in the base space, *S**n*, the fiber over it in the total space, SO(*n* + 1), is a copy of the fiber space, SO(*n*), namely the rotations that keep that direction fixed.

Thus we can build an *n* × *n* rotation matrix by starting with a 2 × 2 matrix, aiming its fixed axis on *S*2 (the ordinary sphere in three-dimensional space), aiming the resulting rotation on *S*3, and so on up through *S**n*−1. A point on *S**n* can be selected using n numbers, so we again have ⁠1/2⁠*n*(*n* − 1) numbers to describe any *n* × *n* rotation matrix.

In fact, we can view the sequential angle decomposition, discussed previously, as reversing this process. The composition of *n* − 1 Givens rotations brings the first column (and row) to (1, 0, ..., 0), so that the remainder of the matrix is a rotation matrix of dimension one less, embedded so as to leave (1, 0, ..., 0) fixed.

### Skew parameters via Cayley's formula

When an *n* × *n* rotation matrix Q, does not include a −1 eigenvalue, thus none of the planar rotations which it comprises are 180° rotations, then *Q* + *I* is an invertible matrix. Most rotation matrices fit this description, and for them it can be shown that (*Q* − *I*)(*Q* + *I*)−1 is a skew-symmetric matrix, A. Thus *A*T = −*A*; and since the diagonal is necessarily zero, and since the upper triangle determines the lower one, A contains ⁠1/2⁠*n*(*n* − 1) independent numbers.

Conveniently, *I* − *A* is invertible whenever A is skew-symmetric; thus we can recover the original matrix using the *Cayley transform*, $A\mapsto (I+A)(I-A)^{-1},$ which maps any skew-symmetric matrix A to a rotation matrix. In fact, aside from the noted exceptions, we can produce any rotation matrix in this way. Although in practical applications we can hardly afford to ignore 180° rotations, the Cayley transform is still a potentially useful tool, giving a parameterization of most rotation matrices without trigonometric functions.

In three dimensions, for example, we have (Cayley 1846) ${\begin{aligned}&{\begin{bmatrix}0&-z&y\\z&0&-x\\-y&x&0\end{bmatrix}}\mapsto \\[3pt]\quad {\frac {1}{1+x^{2}+y^{2}+z^{2}}}&{\begin{bmatrix}1+x^{2}-y^{2}-z^{2}&2xy-2z&2y+2xz\\2xy+2z&1-x^{2}+y^{2}-z^{2}&2yz-2x\\2xz-2y&2x+2yz&1-x^{2}-y^{2}+z^{2}\end{bmatrix}}.\end{aligned}}$

If we condense the skew entries into a vector, (*x*,*y*,*z*), then we produce a 90° rotation around the x-axis for (1, 0, 0), around the y-axis for (0, 1, 0), and around the z-axis for (0, 0, 1). The 180° rotations are just out of reach; for, in the limit as *x* → ∞, (*x*, 0, 0) does approach a 180° rotation around the x axis, and similarly for other directions.

### Decomposition into shears

For the 2D case, a rotation matrix can be decomposed into three shear matrices (Paeth 1986):

${\begin{aligned}R(\theta )&{}={\begin{bmatrix}1&-\tan {\frac {\theta }{2}}\\0&1\end{bmatrix}}{\begin{bmatrix}1&0\\\sin \theta &1\end{bmatrix}}{\begin{bmatrix}1&-\tan {\frac {\theta }{2}}\\0&1\end{bmatrix}}\end{aligned}}$

This is useful, for instance, in computer graphics, since shears can be implemented with fewer multiplication instructions than rotating a bitmap directly. On modern computers, this may not matter, but it can be relevant for very old or low-end microprocessors.

A rotation can also be written as two shears and a squeeze mapping (an area preserving scaling) (Daubechies & Sweldens 1998):

${\begin{aligned}R(\theta )&{}={\begin{bmatrix}1&0\\\tan \theta &1\end{bmatrix}}{\begin{bmatrix}1&-\sin \theta \cos \theta \\0&1\end{bmatrix}}{\begin{bmatrix}\cos \theta &0\\0&{\frac {1}{\cos \theta }}\end{bmatrix}}\end{aligned}}$
