---
title: "Rotation matrix (part 2/2)"
source: https://en.wikipedia.org/wiki/Rotation_matrix
domain: rotary-position-embedding
license: CC-BY-SA-4.0
tags: rotary position embedding, relative positional encoding, token position rotation, attention position bias
fetched: 2026-07-02
part: 2/2
---

## Group theory

Below follow some basic facts about the role of the collection of *all* rotation matrices of a fixed dimension (here mostly 3) in mathematics and particularly in physics where rotational symmetry is a *requirement* of every truly fundamental law (due to the assumption of **isotropy of space**), and where the same symmetry, when present, is a *simplifying property* of many problems of less fundamental nature. Examples abound in classical mechanics and quantum mechanics. Knowledge of the part of the solutions pertaining to this symmetry applies (with qualifications) to *all* such problems and it can be factored out of a specific problem at hand, thus reducing its complexity. A prime example – in mathematics and physics – would be the theory of spherical harmonics. Their role in the group theory of the rotation groups is that of being a representation space for the entire set of finite-dimensional irreducible representations of the rotation group SO(3). For this topic, see Rotation group SO(3) § Spherical harmonics.

The main articles listed in each subsection are referred to for more detail.

### Lie group

The *n* × *n* rotation matrices for each n form a group, the special orthogonal group, SO(*n*). This algebraic structure is coupled with a topological structure inherited from $\operatorname {GL} _{n}(\mathbb {R} )$ in such a way that the operations of multiplication and taking the inverse are analytic functions of the matrix entries. Thus SO(*n*) is for each n a Lie group. It is compact and connected, but not simply connected. It is also a semi-simple group, in fact a simple group with the exception SO(4). The relevance of this is that all theorems and all machinery from the theory of analytic manifolds (analytic manifolds are in particular smooth manifolds) apply and the well-developed representation theory of compact semi-simple groups is ready for use.

### Lie algebra

The Lie algebra **so**(*n*) of SO(*n*) is given by ${\mathfrak {so}}(n)={\mathfrak {o}}(n)=\left\{X\in M_{n}(\mathbb {R} )\mid X=-X^{\mathsf {T}}\right\},$ and is the space of skew-symmetric matrices of dimension *n*, see classical group, where **o**(*n*) is the Lie algebra of O(*n*), the orthogonal group. For reference, the most common basis for **so**(3) is $L_{\mathbf {x} }={\begin{bmatrix}0&0&0\\0&0&-1\\0&1&0\end{bmatrix}},\quad L_{\mathbf {y} }={\begin{bmatrix}0&0&1\\0&0&0\\-1&0&0\end{bmatrix}},\quad L_{\mathbf {z} }={\begin{bmatrix}0&-1&0\\1&0&0\\0&0&0\end{bmatrix}}.$

### Exponential map

Connecting the Lie algebra to the Lie group is the exponential map, which is defined using the standard matrix exponential series for eA For any skew-symmetric matrix A, exp(*A*) is always a rotation matrix.

An important practical example is the 3 × 3 case. In rotation group SO(3), it is shown that one can identify every *A* ∈ **so**(3) with an Euler vector **ω** = *θ***u**, where **u** = (*x*, *y*, *z*) is a unit magnitude vector.

By the properties of the identification $\mathbf {su} (2)\cong \mathbb {R} ^{3}$ , **u** is in the null space of A. Thus, **u** is left invariant by exp(*A*) and is hence a rotation axis.

According to Rodrigues' rotation formula on matrix form, one obtains,

${\begin{aligned}\exp(A)&=\exp {\bigl (}\theta (\mathbf {u} \cdot \mathbf {L} ){\bigr )}\\&=\exp \left({\begin{bmatrix}0&-z\theta &y\theta \\z\theta &0&-x\theta \\-y\theta &x\theta &0\end{bmatrix}}\right)\\&=I+\sin \theta \ \mathbf {u} \cdot \mathbf {L} +(1-\cos \theta )(\mathbf {u} \cdot \mathbf {L} )^{2},\end{aligned}}$

where

$\mathbf {u} \cdot \mathbf {L} ={\begin{bmatrix}0&-z&y\\z&0&-x\\-y&x&0\end{bmatrix}}.$

This is the matrix for a rotation around axis **u** by the angle θ. For full detail, see exponential map SO(3).

### Baker–Campbell–Hausdorff formula

The BCH formula provides an explicit expression for *Z* = log(*e**X**e**Y*) in terms of a series expansion of nested commutators of X and Y. This general expansion unfolds as $Z=C(X,Y)=X+Y+{\tfrac {1}{2}}[X,Y]+{\tfrac {1}{12}}{\bigl [}X,[X,Y]{\bigr ]}-{\tfrac {1}{12}}{\bigl [}Y,[X,Y]{\bigr ]}+\cdots .$

In the 3 × 3 case, the general infinite expansion has a compact form, $Z=\alpha X+\beta Y+\gamma [X,Y],$ for suitable trigonometric function coefficients, detailed in the Baker–Campbell–Hausdorff formula for SO(3).

As a group identity, the above holds for *all faithful representations*, including the doublet (spinor representation), which is simpler. The same explicit formula thus follows straightforwardly through Pauli matrices; see the 2 × 2 derivation for SU(2). For the general *n* × *n* case, one might use Ref.

### Spin group

The Lie group of *n* × *n* rotation matrices, SO(*n*), is not simply connected, so Lie theory tells us it is a homomorphic image of a universal covering group. Often the covering group, which in this case is called the spin group denoted by Spin(*n*), is simpler and more natural to work with.

In the case of planar rotations, SO(2) is topologically a circle, *S*1. Its universal covering group, Spin(2), is isomorphic to the real line, **R**, under addition. Whenever angles of arbitrary magnitude are used one is taking advantage of the convenience of the universal cover. Every 2 × 2 rotation matrix is produced by a countable infinity of angles, separated by integer multiples of 2π. Correspondingly, the fundamental group of SO(2) is isomorphic to the integers, **Z**.

In the case of spatial rotations, SO(3) is topologically equivalent to three-dimensional real projective space, **RP**3. Its universal covering group, Spin(3), is isomorphic to the 3-sphere, *S*3. Every 3 × 3 rotation matrix is produced by two opposite points on the sphere. Correspondingly, the fundamental group of SO(3) is isomorphic to the two-element group, **Z**2.

We can also describe Spin(3) as isomorphic to quaternions of unit norm under multiplication, or to certain 4 × 4 real matrices, or to 2 × 2 complex special unitary matrices, namely SU(2). The covering maps for the first and the last case are given by $\mathbb {H} \supset \{q\in \mathbb {H} :\|q\|=1\}\ni w+\mathbf {i} x+\mathbf {j} y+\mathbf {k} z\mapsto {\begin{bmatrix}1-2y^{2}-2z^{2}&2xy-2zw&2xz+2yw\\2xy+2zw&1-2x^{2}-2z^{2}&2yz-2xw\\2xz-2yw&2yz+2xw&1-2x^{2}-2y^{2}\end{bmatrix}}\in \mathrm {SO} (3),$ and $\mathrm {SU} (2)\ni {\begin{bmatrix}\alpha &\beta \\-{\overline {\beta }}&{\overline {\alpha }}\end{bmatrix}}\mapsto {\begin{bmatrix}{\frac {1}{2}}\left(\alpha ^{2}-\beta ^{2}+{\overline {\alpha ^{2}}}-{\overline {\beta ^{2}}}\right)&{\frac {i}{2}}\left(-\alpha ^{2}-\beta ^{2}+{\overline {\alpha ^{2}}}+{\overline {\beta ^{2}}}\right)&-\alpha \beta -{\overline {\alpha }}{\overline {\beta }}\\{\frac {i}{2}}\left(\alpha ^{2}-\beta ^{2}-{\overline {\alpha ^{2}}}+{\overline {\beta ^{2}}}\right)&{\frac {i}{2}}\left(\alpha ^{2}+\beta ^{2}+{\overline {\alpha ^{2}}}+{\overline {\beta ^{2}}}\right)&-i\left(+\alpha \beta -{\overline {\alpha }}{\overline {\beta }}\right)\\\alpha {\overline {\beta }}+{\overline {\alpha }}\beta &i\left(-\alpha {\overline {\beta }}+{\overline {\alpha }}\beta \right)&\alpha {\overline {\alpha }}-\beta {\overline {\beta }}\end{bmatrix}}\in \mathrm {SO} (3).$

For a detailed account of the SU(2)-covering and the quaternionic covering, see spin group SO(3).

Many features of these cases are the same for higher dimensions. The coverings are all two-to-one, with SO(*n*), *n* > 2, having fundamental group **Z**2. The natural setting for these groups is within a Clifford algebra. One type of action of the rotations is produced by a kind of "sandwich", denoted by *qvq*∗. More importantly in applications to physics, the corresponding spin representation of the Lie algebra sits inside the Clifford algebra. It can be exponentiated in the usual way to give rise to a 2-valued representation, also known as projective representation of the rotation group. This is the case with SO(3) and SU(2), where the 2-valued representation can be viewed as an "inverse" of the covering map. By properties of covering maps, the inverse can be chosen ono-to-one as a local section, but not globally.

### Infinitesimal rotations

The matrices in the Lie algebra are not themselves rotations; the skew-symmetric matrices are derivatives, proportional differences of rotations. An actual "differential rotation", or *infinitesimal rotation matrix* has the form $I+A\,d\theta ,$ where *dθ* is vanishingly small and *A* ∈ **so**(n), for instance with *A* = *L**x*, $dL_{x}={\begin{bmatrix}1&0&0\\0&1&-d\theta \\0&d\theta &1\end{bmatrix}}.$

The computation rules are as usual except that infinitesimals of second order are routinely dropped. With these rules, these matrices do not satisfy all the same properties as ordinary finite rotation matrices under the usual treatment of infinitesimals. It turns out that *the order in which infinitesimal rotations are applied is irrelevant*. To see this exemplified, consult infinitesimal rotations SO(3).


## Conversions

We have seen the existence of several decompositions that apply in any dimension, namely independent planes, sequential angles, and nested dimensions. In all these cases we can either decompose a matrix or construct one. We have also given special attention to 3 × 3 rotation matrices, and these warrant further attention, in both directions (Stuelpnagel 1964).

### Quaternion

Given the unit quaternion **q** = *w* + *x***i** + *y***j** + *z***k**, the equivalent pre-multiplied (to be used with column vectors) 3 × 3 rotation matrix is $Q={\begin{bmatrix}1-2y^{2}-2z^{2}&2xy-2zw&2xz+2yw\\2xy+2zw&1-2x^{2}-2z^{2}&2yz-2xw\\2xz-2yw&2yz+2xw&1-2x^{2}-2y^{2}\end{bmatrix}}.$

Now every quaternion component appears multiplied by two in a term of degree two, and if all such terms are zero what is left is an identity matrix. This leads to an efficient, robust conversion from any quaternion – whether unit or non-unit – to a 3 × 3 rotation matrix. Given: ${\begin{aligned}n&=w\times w+x\times x+y\times y+z\times z\\s&={\begin{cases}0&{\text{if }}n=0\\{\frac {2}{n}}&{\text{otherwise}}\end{cases}}\\\end{aligned}}$ we can calculate $Q={\begin{bmatrix}1-s(yy+zz)&s(xy-wz)&s(xz+wy)\\s(xy+wz)&1-s(xx+zz)&s(yz-wx)\\s(xz-wy)&s(yz+wx)&1-s(xx+yy)\end{bmatrix}}$

Freed from the demand for a unit quaternion, we find that nonzero quaternions act as homogeneous coordinates for 3 × 3 rotation matrices. The Cayley transform, discussed earlier, is obtained by scaling the quaternion so that its w component is 1. For a 180° rotation around any axis, w will be zero, which explains the Cayley limitation.

The sum of the entries along the main diagonal (the trace), plus one, equals 4 − 4(*x*2 + *y*2 + *z*2), which is 4*w*2. Thus we can write the trace itself as 2*w*2 + 2*w*2 − 1; and from the previous version of the matrix we see that the diagonal entries themselves have the same form: 2*x*2 + 2*w*2 − 1, 2*y*2 + 2*w*2 − 1, and 2*z*2 + 2*w*2 − 1. So we can easily compare the magnitudes of all four quaternion components using the matrix diagonal. We can, in fact, obtain all four magnitudes using sums and square roots, and choose consistent signs using the skew-symmetric part of the off-diagonal entries: ${\begin{aligned}t&=\operatorname {tr} Q=Q_{xx}+Q_{yy}+Q_{zz}\quad ({\text{the trace of }}Q)\\r&={\sqrt {1+t}}\\w&={\tfrac {1}{2}}r\\x&=\operatorname {sgn} \left(Q_{zy}-Q_{yz}\right)\left|{\tfrac {1}{2}}{\sqrt {1+Q_{xx}-Q_{yy}-Q_{zz}}}\right|\\y&=\operatorname {sgn} \left(Q_{xz}-Q_{zx}\right)\left|{\tfrac {1}{2}}{\sqrt {1-Q_{xx}+Q_{yy}-Q_{zz}}}\right|\\z&=\operatorname {sgn} \left(Q_{yx}-Q_{xy}\right)\left|{\tfrac {1}{2}}{\sqrt {1-Q_{xx}-Q_{yy}+Q_{zz}}}\right|\end{aligned}}$

Alternatively, use a single square root and division ${\begin{aligned}t&=\operatorname {tr} Q=Q_{xx}+Q_{yy}+Q_{zz}\\r&={\sqrt {1+t}}\\s&={\tfrac {1}{2r}}\\w&={\tfrac {1}{2}}r\\x&=\left(Q_{zy}-Q_{yz}\right)s\\y&=\left(Q_{xz}-Q_{zx}\right)s\\z&=\left(Q_{yx}-Q_{xy}\right)s\end{aligned}}$

This is numerically stable so long as the trace, t, is not negative; otherwise, we risk dividing by (nearly) zero. In that case, suppose Qxx is the largest diagonal entry, so x will have the largest magnitude (the other cases are derived by cyclic permutation); then the following is safe. ${\begin{aligned}r&={\sqrt {1+Q_{xx}-Q_{yy}-Q_{zz}}}\\s&={\tfrac {1}{2r}}\\w&=\left(Q_{zy}-Q_{yz}\right)s\\x&={\tfrac {1}{2}}r\\y&=\left(Q_{xy}+Q_{yx}\right)s\\z&=\left(Q_{zx}+Q_{xz}\right)s\end{aligned}}$

If the matrix contains significant error, such as accumulated numerical error, we may construct a symmetric 4 × 4 matrix, $K={\frac {1}{3}}{\begin{bmatrix}Q_{xx}-Q_{yy}-Q_{zz}&Q_{yx}+Q_{xy}&Q_{zx}+Q_{xz}&Q_{zy}-Q_{yz}\\Q_{yx}+Q_{xy}&Q_{yy}-Q_{xx}-Q_{zz}&Q_{zy}+Q_{yz}&Q_{xz}-Q_{zx}\\Q_{zx}+Q_{xz}&Q_{zy}+Q_{yz}&Q_{zz}-Q_{xx}-Q_{yy}&Q_{yx}-Q_{xy}\\Q_{zy}-Q_{yz}&Q_{xz}-Q_{zx}&Q_{yx}-Q_{xy}&Q_{xx}+Q_{yy}+Q_{zz}\end{bmatrix}},$ and find the eigenvector, (*x*, *y*, *z*, *w*), of its largest magnitude eigenvalue. (If Q is truly a rotation matrix, that value will be 1.) The quaternion so obtained will correspond to the rotation matrix closest to the given matrix (Bar-Itzhack 2000) (Note: formulation of the cited article is post-multiplied, works with row vectors).

### Polar decomposition

If the *n* × *n* matrix M is nonsingular, its columns are linearly independent vectors; thus the Gram–Schmidt process can adjust them to be an orthonormal basis. Stated in terms of numerical linear algebra, we convert M to an orthogonal matrix, Q, using QR decomposition. However, we often prefer a Q closest to M, which this method does not accomplish. For that, the tool we want is the polar decomposition (Fan & Hoffman 1955; Higham 1989).

To measure closeness, we may use any matrix norm invariant under orthogonal transformations. A convenient choice is the Frobenius norm, ‖*Q* − *M*‖F, squared, which is the sum of the squares of the element differences. Writing this in terms of the trace, Tr, our goal is,

Find

Q

minimizing

Tr( (

Q

−

M

)

T

(

Q

−

M

) )

, subject to

Q

T

Q

=

I

.

Though written in matrix terms, the objective function is just a quadratic polynomial. We can minimize it in the usual way, by finding where its derivative is zero. For a 3 × 3 matrix, the orthogonality constraint implies six scalar equalities that the entries of Q must satisfy. To incorporate the constraint(s), we may employ a standard technique, Lagrange multipliers, assembled as a symmetric matrix, Y. Thus our method is:

Differentiate

Tr( (

Q

−

M

)

T

(

Q

−

M

) + (

Q

T

Q

−

I

)

Y

)

with respect to (the entries of)

Q

, and equate to zero.

Consider a 2 × 2 example. Including constraints, we seek to minimize ${\begin{aligned}&\left(Q_{xx}-M_{xx}\right)^{2}+\left(Q_{xy}-M_{xy}\right)^{2}+\left(Q_{yx}-M_{yx}\right)^{2}+\left(Q_{yy}-M_{yy}\right)^{2}\\&\quad {}+\left(Q_{xx}^{2}+Q_{yx}^{2}-1\right)Y_{xx}+\left(Q_{xy}^{2}+Q_{yy}^{2}-1\right)Y_{yy}+2\left(Q_{xx}Q_{xy}+Q_{yx}Q_{yy}\right)Y_{xy}.\end{aligned}}$

Taking the derivative with respect to Qxx, Qxy, Qyx, Qyy in turn, we assemble a matrix. $2{\begin{bmatrix}Q_{xx}-M_{xx}+Q_{xx}Y_{xx}+Q_{xy}Y_{xy}&Q_{xy}-M_{xy}+Q_{xx}Y_{xy}+Q_{xy}Y_{yy}\\Q_{yx}-M_{yx}+Q_{yx}Y_{xx}+Q_{yy}Y_{xy}&Q_{yy}-M_{yy}+Q_{yx}Y_{xy}+Q_{yy}Y_{yy}\end{bmatrix}}$

In general, we obtain the equation $0=2(Q-M)+2QY,$ so that $M=Q(I+Y)=QS,$ where Q is orthogonal and S is symmetric. To ensure a minimum, the Y matrix (and hence S) must be positive definite. Linear algebra calls QS the polar decomposition of M, with S the positive square root of *S*2 = *M*T*M*. $S^{2}=\left(Q^{\mathsf {T}}M\right)^{\mathsf {T}}\left(Q^{\mathsf {T}}M\right)=M^{\mathsf {T}}QQ^{\mathsf {T}}M=M^{\mathsf {T}}M$

When M is non-singular, the Q and S factors of the polar decomposition are uniquely determined. However, the determinant of S is positive because S is positive definite, so Q inherits the sign of the determinant of M. That is, Q is only guaranteed to be orthogonal, not a rotation matrix. This is unavoidable; an M with negative determinant has no uniquely defined closest rotation matrix.

### Axis and angle

To efficiently construct a rotation matrix Q from an angle θ and a unit axis **u**, we can take advantage of symmetry and skew-symmetry within the entries. If x, y, and z are the components of the unit vector representing the axis, and

${\begin{aligned}c&=\cos \theta \\s&=\sin \theta \\C&=1-c\end{aligned}}$

then

$Q(\theta )={\begin{bmatrix}xxC+c&xyC-zs&xzC+ys\\yxC+zs&yyC+c&yzC-xs\\zxC-ys&zyC+xs&zzC+c\end{bmatrix}}$

Determining an axis and angle, like determining a quaternion, is only possible up to the sign; that is, (**u**, *θ*) and (−**u**, −*θ*) correspond to the same rotation matrix, just like *q* and −*q*. Additionally, axis–angle extraction presents additional difficulties. The angle can be restricted to be from 0° to 180°, but angles are formally ambiguous by multiples of 360°. When the angle is zero, the axis is undefined. When the angle is 180°, the matrix becomes symmetric, which has implications in extracting the axis. Near multiples of 180°, care is needed to avoid numerical problems: in extracting the angle, a two-argument arctangent with atan2(sin *θ*, cos *θ*) equal to θ avoids the insensitivity of arccos; and in computing the axis magnitude in order to force unit magnitude, a brute-force approach can lose accuracy through underflow (Moler & Morrison 1983).

A partial approach is as follows:

${\begin{aligned}x&=Q_{zy}-Q_{yz}\\y&=Q_{xz}-Q_{zx}\\z&=Q_{yx}-Q_{xy}\\r&={\sqrt {x^{2}+y^{2}+z^{2}}}\\t&=Q_{xx}+Q_{yy}+Q_{zz}\\\theta &=\operatorname {atan2} (r,t-1)\end{aligned}}$

The x-, y-, and z-components of the axis would then be divided by r. A fully robust approach will use a different algorithm when t, the trace of the matrix Q, is negative, as with quaternion extraction. When r is zero because the angle is zero, an axis must be provided from some source other than the matrix.

### Euler angles

Complexity of conversion escalates with Euler angles (used here in the broad sense). The first difficulty is to establish which of the twenty-four variations of Cartesian axis order we will use. Suppose the three angles are *θ*1, *θ*2, *θ*3; physics and chemistry may interpret these as $Q(\theta _{1},\theta _{2},\theta _{3})=Q_{\mathbf {z} }(\theta _{1})Q_{\mathbf {y} }(\theta _{2})Q_{\mathbf {z} }(\theta _{3}),$ while aircraft dynamics may use $Q(\theta _{1},\theta _{2},\theta _{3})=Q_{\mathbf {z} }(\theta _{3})Q_{\mathbf {y} }(\theta _{2})Q_{\mathbf {x} }(\theta _{1}).$ One systematic approach begins with choosing the rightmost axis. Among all permutations of (*x*,*y*,*z*), only two place that axis first; one is an even permutation and the other odd. Choosing parity thus establishes the middle axis. That leaves two choices for the left-most axis, either duplicating the first or not. These three choices gives us 3 × 2 × 2 = 12 variations; we double that to 24 by choosing static or rotating axes.

This is enough to construct a matrix from angles, but triples differing in many ways can give the same rotation matrix. For example, suppose we use the **zyz** convention above; then we have the following equivalent pairs:

| (90°, | 45°, | −105°) | ≡ | (−270°, | −315°, | 255°) | *multiples of 360°* |
|---|---|---|---|---|---|---|---|
| (72°, | 0°, | 0°) | ≡ | (40°, | 0°, | 32°) | *singular alignment* |
| (45°, | 60°, | −30°) | ≡ | (−135°, | −60°, | 150°) | *bistable flip* |

Angles for any order can be found using a concise common routine (Herter & Lott 1993; Shoemake 1994).

The problem of singular alignment, the mathematical analog of physical gimbal lock, occurs when the middle rotation aligns the axes of the first and last rotations. It afflicts every axis order at either even or odd multiples of 90°. These singularities are not characteristic of the rotation matrix as such, and only occur with the usage of Euler angles.

The singularities are avoided when considering and manipulating the rotation matrix as orthonormal row vectors (in 3D applications often named the right-vector, up-vector and out-vector) instead of as angles. The singularities are also avoided when working with quaternions.

### Vector to vector formulation

In some instances it is interesting to describe a rotation by specifying how a vector is mapped into another through the shortest path (smallest angle). In $\mathbb {R} ^{3}$ this completely describes the associated rotation matrix. In general, given $x,y\in \mathbb {S} ^{n}$ , the matrix $R:=I+yx^{\mathsf {T}}-xy^{\mathsf {T}}+{\frac {1}{1+\langle x,y\rangle }}\left(yx^{\mathsf {T}}-xy^{\mathsf {T}}\right)^{2}$ belongs to SO(*n* + 1) and maps x to y.

### Voigt notation

In materials science, the four-dimensional stiffness and compliance tensors are often simplified to a two-dimensional matrix using Voigt notation. When applying a rotational transform through angle $\theta$ in this notation, the rotation matrix is given by

$T={\begin{bmatrix}\cos ^{2}\theta &\sin ^{2}\theta &2\sin \theta \cos \theta \\\sin ^{2}\theta &\cos ^{2}\theta &2\sin \theta \cos \theta \\-\sin \theta \cos \theta &\sin \theta \cos \theta &\cos ^{2}\theta -\sin ^{2}\theta \end{bmatrix}}.$

This is particularly useful in composite laminate design, where plies are often rotated by a certain angle to bring the properties of the laminate closer to isotropic.


## Uniform random rotation matrices

We sometimes need to generate a uniformly distributed random rotation matrix. It seems intuitively clear in two dimensions that this means the rotation angle is uniformly distributed between 0 and 2π. That intuition is correct, but does not carry over to higher dimensions. For example, if we decompose 3 × 3 rotation matrices in axis–angle form, the angle should *not* be uniformly distributed; the probability that (the magnitude of) the angle is at most θ should be ⁠1/π⁠(*θ* − sin *θ*), for 0 ≤ *θ* ≤ π.

Since SO(*n*) is a connected and locally compact Lie group, we have a simple standard criterion for uniformity, namely that the distribution be unchanged when composed with any arbitrary rotation (a Lie group "translation"). This definition corresponds to what is called *Haar measure*. León, Massé & Rivest (2006) show how to use the Cayley transform to generate and test matrices according to this criterion.

We can also generate a uniform distribution in any dimension using the *subgroup algorithm* of Diaconis & Shahshahani (1987). This recursively exploits the nested dimensions group structure of SO(*n*), as follows. Generate a uniform angle and construct a 2 × 2 rotation matrix. To step from *n* to *n* + 1, generate a vector **v** uniformly distributed on the n-sphere *S**n*, embed the *n* × *n* matrix in the next larger size with last column (0, ..., 0, 1), and rotate the larger matrix so the last column becomes **v**.

As usual, we have special alternatives for the 3 × 3 case. Each of these methods begins with three independent random scalars uniformly distributed on the unit interval. Arvo (1992) takes advantage of the odd dimension to change a Householder reflection to a rotation by negation, and uses that to aim the axis of a uniform planar rotation.

Another method uses unit quaternions. Multiplication of rotation matrices is homomorphic to multiplication of quaternions, and multiplication by a unit quaternion rotates the unit sphere. Since the homomorphism is a local isometry, we immediately conclude that to produce a uniform distribution on SO(3) we may use a uniform distribution on *S*3. In practice: create a four-element vector where each element is a sampling of a normal distribution. Normalize its length and you have a uniformly sampled random unit quaternion which represents a uniformly sampled random rotation. Note that the aforementioned only applies to rotations in dimension 3. For a generalised idea of quaternions, one should look into Rotors.

Euler angles can also be used, though not with each angle uniformly distributed (Murnaghan 1962; Miles 1965).

For the axis–angle form, the axis is uniformly distributed over the unit sphere of directions, *S*2, while the angle has the nonuniform distribution over [0,π] noted previously (Miles 1965).
