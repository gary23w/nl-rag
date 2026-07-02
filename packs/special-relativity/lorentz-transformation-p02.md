---
title: "Lorentz transformation (part 2/2)"
source: https://en.wikipedia.org/wiki/Lorentz_transformation
domain: special-relativity
license: CC-BY-SA-4.0
tags: special relativity, lorentz transformation, time dilation, mass-energy equivalence
fetched: 2026-07-02
part: 2/2
---

## Mathematical formulation

Throughout, italic non-bold capital letters are 4 × 4 matrices, while non-italic bold letters are 3 × 3 matrices.

### Homogeneous Lorentz group

Writing the coordinates in column vectors and the Minkowski metric η as a square matrix $X'={\begin{bmatrix}c\,t'\\x'\\y'\\z'\end{bmatrix}}\,,\quad \eta ={\begin{bmatrix}-1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{bmatrix}}\,,\quad X={\begin{bmatrix}c\,t\\x\\y\\z\end{bmatrix}}$ the spacetime interval takes the form (superscript T denotes transpose) $X\cdot X=X^{\mathrm {T} }\eta X={X'}^{\mathrm {T} }\eta {X'}$ and is invariant under a Lorentz transformation $X'=\Lambda X$ where Λ is a square matrix which can depend on parameters.

The set of all Lorentz transformations $\Lambda$ in this article is denoted ${\mathcal {L}}$ . This set together with matrix multiplication forms a group, in this context known as the *Lorentz group*. Also, the above expression *X*·*X* is a quadratic form of signature (3,1) on spacetime, and the group of transformations which leaves this quadratic form invariant is the indefinite orthogonal group O(3,1), a Lie group. In other words, the Lorentz group is O(3,1). As presented in this article, any Lie groups mentioned are matrix Lie groups. In this context the operation of composition amounts to matrix multiplication.

From the invariance of the spacetime interval it follows $\eta =\Lambda ^{\mathrm {T} }\eta \Lambda$ and this matrix equation contains the general conditions on the Lorentz transformation to ensure invariance of the spacetime interval. Taking the determinant of the equation using the product rule gives immediately $\left[\det(\Lambda )\right]^{2}=1\quad \Rightarrow \quad \det(\Lambda )=\pm 1$

Writing the Minkowski metric as a block matrix, and the Lorentz transformation in the most general form, $\eta ={\begin{bmatrix}-1&0\\0&\mathbf {I} \end{bmatrix}}\,,\quad \Lambda ={\begin{bmatrix}\Gamma &-\mathbf {a} ^{\mathrm {T} }\\-\mathbf {b} &\mathbf {M} \end{bmatrix}}\,,$ carrying out the block matrix multiplications obtains general conditions on Γ, **a**, **b**, **M** to ensure relativistic invariance. Not much information can be directly extracted from all the conditions, however one of the results $\Gamma ^{2}=1+\mathbf {b} ^{\mathrm {T} }\mathbf {b}$ is useful; **b**T**b** ≥ 0 always so it follows that $\Gamma ^{2}\geq 1\quad \Rightarrow \quad \Gamma \leq -1\,,\quad \Gamma \geq 1$

The negative inequality may be unexpected, because Γ multiplies the time coordinate and this has an effect on time symmetry. If the positive equality holds, then Γ is the Lorentz factor.

The determinant and inequality provide four ways to classify **L**orentz **T**ransformations (*herein **LT**s for brevity*). Any particular LT has only one determinant sign *and* only one inequality. There are four sets which include every possible pair given by the intersections ("n"-shaped symbol meaning "and") of these classifying sets.

| Intersection, ∩ | **Antichronous** (or non-orthochronous) LTs ${\mathcal {L}}^{\downarrow }=\{\Lambda :\Gamma \leq -1\}$ | **Orthochronous** LTs ${\mathcal {L}}^{\uparrow }=\{\Lambda :\Gamma \geq 1\}$ |
|---|---|---|
| **Proper** LTs ${\mathcal {L}}_{+}=\{\Lambda :\det(\Lambda )=+1\}$ | **Proper antichronous** LTs ${\mathcal {L}}_{+}^{\downarrow }={\mathcal {L}}_{+}\cap {\mathcal {L}}^{\downarrow }$ | **Proper orthochronous** LTs ${\mathcal {L}}_{+}^{\uparrow }={\mathcal {L}}_{+}\cap {\mathcal {L}}^{\uparrow }$ |
| **Improper** LTs ${\mathcal {L}}_{-}=\{\Lambda :\det(\Lambda )=-1\}$ | **Improper antichronous** LTs ${\mathcal {L}}_{-}^{\downarrow }={\mathcal {L}}_{-}\cap {\mathcal {L}}^{\downarrow }$ | **Improper orthochronous** LTs ${\mathcal {L}}_{-}^{\uparrow }={\mathcal {L}}_{-}\cap {\mathcal {L}}^{\uparrow }$ |

where "+" and "−" indicate the determinant sign, while "↑" for ≥ and "↓" for ≤ denote the inequalities.

The full Lorentz group splits into the union ("u"-shaped symbol meaning "or") of four disjoint sets ${\mathcal {L}}={\mathcal {L}}_{+}^{\uparrow }\cup {\mathcal {L}}_{-}^{\uparrow }\cup {\mathcal {L}}_{+}^{\downarrow }\cup {\mathcal {L}}_{-}^{\downarrow }$

A subgroup of a group must be closed under the same operation of the group (here matrix multiplication). In other words, for two Lorentz transformations Λ and L from a particular subgroup, the composite Lorentz transformations Λ*L* and *L*Λ must be in the same subgroup as Λ and L. This is not always the case: the composition of two antichronous Lorentz transformations is orthochronous, and the composition of two improper Lorentz transformations is proper. In other words, while the sets ${\mathcal {L}}_{+}^{\uparrow }$ , ${\mathcal {L}}_{+}$ , ${\mathcal {L}}^{\uparrow }$ , and ${\mathcal {L}}_{0}={\mathcal {L}}_{+}^{\uparrow }\cup {\mathcal {L}}_{-}^{\downarrow }$ all form subgroups, the sets containing improper and/or antichronous transformations without enough proper orthochronous transformations (e.g. ${\mathcal {L}}_{+}^{\downarrow }$ , ${\mathcal {L}}_{-}^{\downarrow }$ , ${\mathcal {L}}_{-}^{\uparrow }$ ) do not form subgroups.

### Proper transformations

If a Lorentz covariant 4-vector is measured in one inertial frame with result X , and the same measurement made in another inertial frame (with the same orientation and origin) gives result $X'$ , the two results will be related by $X'=B(\mathbf {v} )X$ where the boost matrix $B(\mathbf {v} )$ represents the rotation-free Lorentz transformation between the unprimed and primed frames and $\mathbf {v}$ is the velocity of the primed frame as seen from the unprimed frame. The matrix is given by $B(\mathbf {v} )={\begin{bmatrix}\gamma &-\gamma v_{\text{x}}/c&-\gamma v_{\text{y}}/c&-\gamma v_{\text{z}}/c\\-\gamma v_{\text{x}}/c&1+(\gamma -1){\dfrac {v_{\text{x}}^{2}}{v^{2}}}&(\gamma -1){\dfrac {v_{\text{x}}v_{\text{y}}}{v^{2}}}&(\gamma -1){\dfrac {v_{\text{x}}v_{\text{z}}}{v^{2}}}\\-\gamma v_{\text{y}}/c&(\gamma -1){\dfrac {v_{\text{y}}v_{\text{x}}}{v^{2}}}&1+(\gamma -1){\dfrac {v_{\text{y}}^{2}}{v^{2}}}&(\gamma -1){\dfrac {v_{\text{y}}v_{\text{z}}}{v^{2}}}\\-\gamma v_{\text{z}}/c&(\gamma -1){\dfrac {v_{\text{z}}v_{\text{x}}}{v^{2}}}&(\gamma -1){\dfrac {v_{\text{z}}v_{\text{y}}}{v^{2}}}&1+(\gamma -1){\dfrac {v_{\text{z}}^{2}}{v^{2}}}\end{bmatrix}}={\begin{bmatrix}\gamma &-\gamma {\vec {\beta }}^{\text{T}}\\-\gamma {\vec {\beta }}&I+(\gamma -1){\dfrac {{\vec {\beta }}{\vec {\beta }}^{\text{T}}}{\beta ^{2}}}\end{bmatrix}},$

where ${\textstyle v={\sqrt {v_{\text{x}}^{2}+v_{\text{y}}^{2}+v_{\text{z}}^{2}}}}$ is the magnitude of the velocity and ${\textstyle \gamma ={\frac {1}{\sqrt {1-{v^{2}}/{c^{2}}}}}}$ is the Lorentz factor. This formula represents a passive transformation, as it describes how the coordinates of the measured quantity changes from the unprimed frame to the primed frame. The active transformation is given by $B(-\mathbf {v} )$ .

If a frame *F*′ is boosted with velocity **u** relative to frame F, and another frame F′′ is boosted with velocity **v** relative to *F*′, the separate boosts are $X''=B(\mathbf {v} )X'\,,\quad X'=B(\mathbf {u} )X$ and the composition of the two boosts connects the coordinates in *F*′′ and F, $X''=B(\mathbf {v} )B(\mathbf {u} )X\,.$ Successive transformations act on the left. If **u** and **v** are collinear (parallel or antiparallel along the same line of relative motion), the boost matrices commute: *B*(**v**)*B*(**u**) = *B*(**u**)*B*(**v**). This composite transformation happens to be another boost, *B*(**w**), where **w** is collinear with **u** and **v**.

If **u** and **v** are not collinear but in different directions, the situation is considerably more complicated. Lorentz boosts along different directions do not commute: *B*(**v**)*B*(**u**) and *B*(**u**)*B*(**v**) are not equal. Although each of these compositions is *not* a single boost, each composition is still a Lorentz transformation as it preserves the spacetime interval. It turns out the composition of any two Lorentz boosts is equivalent to a boost followed or preceded by a rotation on the spatial coordinates, in the form of *R*(**ρ**)*B*(**w**) or *B*(**w**)*R*(**ρ**). The **w** and **w** are composite velocities, while **ρ** and **ρ** are rotation parameters (e.g. axis-angle variables, Euler angles, etc.). The rotation in block matrix form is simply $\quad R({\boldsymbol {\rho }})={\begin{bmatrix}1&0\\0&\mathbf {R} ({\boldsymbol {\rho }})\end{bmatrix}}\,,$ where **R**(**ρ**) is a 3 × 3 rotation matrix, which rotates any 3-dimensional vector in one sense (active transformation), or equivalently the coordinate frame in the opposite sense (passive transformation). It is *not* simple to connect **w** and **ρ** (or **w** and **ρ**) to the original boost parameters **u** and **v**. In a composition of boosts, the R matrix is named the Wigner rotation, and gives rise to the Thomas precession. These articles give the explicit formulae for the composite transformation matrices, including expressions for **w**, **ρ**, **w**, **ρ**.

In this article the axis-angle representation is used for **ρ**. The rotation is about an axis in the direction of a unit vector **e**, through angle θ (positive anticlockwise, negative clockwise, according to the right-hand rule). The "axis-angle vector" ${\boldsymbol {\theta }}=\theta \mathbf {e}$ will serve as a useful abbreviation.

Spatial rotations alone are also Lorentz transformations since they leave the spacetime interval invariant. Like boosts, successive rotations about different axes do not commute. Unlike boosts, the composition of any two rotations is equivalent to a single rotation. Some other similarities and differences between the boost and rotation matrices include:

- inverses: *B*(**v**)−1 = *B*(−**v**) (relative motion in the opposite direction), and *R*(**θ**)−1 = *R*(−**θ**) (rotation in the opposite sense about the same axis)
- identity transformation for no relative motion/rotation: *B*(**0**) = *R*(**0**) = *I*
- unit determinant: det(*B*) = det(*R*) = +1. This property makes them proper transformations.
- matrix symmetry: B is symmetric (equals transpose), while R is nonsymmetric but orthogonal (transpose equals inverse, *R*T = *R*−1).

The most general proper Lorentz transformation Λ(**v**, **θ**) includes a boost and rotation together, and is a nonsymmetric matrix. As special cases, Λ(**0**, **θ**) = *R*(**θ**) and Λ(**v**, **0**) = *B*(**v**). An explicit form of the general Lorentz transformation is cumbersome to write down and will not be given here. Nevertheless, closed form expressions for the transformation matrices will be given below using group theoretical arguments. It will be easier to use the rapidity parametrization for boosts, in which case one writes Λ(**ζ**, **θ**) and *B*(**ζ**).

#### Lie group SO+(3,1)

The set of transformations $\{B({\boldsymbol {\zeta }}),R({\boldsymbol {\theta }}),\Lambda ({\boldsymbol {\zeta }},{\boldsymbol {\theta }})\}$ with matrix multiplication as the operation of composition forms a group, called the "restricted Lorentz group", and is the special indefinite orthogonal group SO+(3,1). (The plus sign indicates that it preserves the orientation of the temporal dimension).

For simplicity, look at the infinitesimal Lorentz boost in the x direction (examining a boost in any other direction, or rotation about any axis, follows an identical procedure). The infinitesimal boost is a small boost away from the identity, obtained by the Taylor expansion of the boost matrix to first order about *ζ* = 0, $B_{\text{x}}=I+\zeta \left.{\frac {\partial B_{\text{x}}}{\partial \zeta }}\right|_{\zeta =0}+\cdots$ where the higher order terms not shown are negligible because ζ is small, and *B**x* is simply the boost matrix in the *x* direction. The derivative of the matrix is the matrix of derivatives (of the entries, with respect to the same variable), and it is understood the derivatives are found first then evaluated at *ζ* = 0, $\left.{\frac {\partial B_{\text{x}}}{\partial \zeta }}\right|_{\zeta =0}=-K_{\text{x}}\,.$

For now, *K**x* is defined by this result (its significance will be explained shortly). In the limit of an infinite number of infinitely small steps, the finite boost transformation in the form of a matrix exponential is obtained $B_{\text{x}}=\lim _{N\to \infty }\left(I-{\frac {\zeta }{N}}K_{\text{x}}\right)^{\!N}=e^{-\zeta K_{\text{x}}}$ where the limit definition of the exponential has been used (see also *Characterizations of the exponential function*). More generally $B({\boldsymbol {\zeta }})=e^{-{\boldsymbol {\zeta }}\cdot \mathbf {K} }\,,\quad R({\boldsymbol {\theta }})=e^{{\boldsymbol {\theta }}\cdot \mathbf {J} }\,.$

The axis-angle vector **θ** and rapidity vector **ζ** are altogether six continuous variables which make up the group parameters (in this particular representation), and the generators of the group are **K** = (*K**x*, *K**y*, *K**z*) and **J** = (*J**x*, *J**y*, *J**z*), each vectors of matrices with the explicit forms ${\begin{alignedat}{3}K_{\text{x}}&={\begin{bmatrix}0&1&0&0\\1&0&0&0\\0&0&0&0\\0&0&0&0\\\end{bmatrix}}\,,\quad &K_{\text{y}}&={\begin{bmatrix}0&0&1&0\\0&0&0&0\\1&0&0&0\\0&0&0&0\end{bmatrix}}\,,\quad &K_{\text{z}}&={\begin{bmatrix}0&0&0&1\\0&0&0&0\\0&0&0&0\\1&0&0&0\end{bmatrix}}\\[10mu]J_{\text{x}}&={\begin{bmatrix}0&0&0&0\\0&0&0&0\\0&0&0&-1\\0&0&1&0\\\end{bmatrix}}\,,\quad &J_{\text{y}}&={\begin{bmatrix}0&0&0&0\\0&0&0&1\\0&0&0&0\\0&-1&0&0\end{bmatrix}}\,,\quad &J_{\text{z}}&={\begin{bmatrix}0&0&0&0\\0&0&-1&0\\0&1&0&0\\0&0&0&0\end{bmatrix}}\end{alignedat}}$

These are all defined in an analogous way to *K**x* above, although the minus signs in the boost generators are conventional. Physically, the generators of the Lorentz group correspond to important symmetries in spacetime: **J** are the *rotation generators* which correspond to angular momentum, and **K** are the *boost generators* which correspond to the motion of the system in spacetime. The derivative of any smooth curve *C*(*t*) with *C*(0) = *I* in the group depending on some group parameter t with respect to that group parameter, evaluated at *t* = 0, serves as a definition of a corresponding group generator G, and this reflects an infinitesimal transformation away from the identity. The smooth curve can always be taken as an exponential as the exponential will always map G smoothly back into the group via *t* → exp(*tG*) for all t; this curve will yield G again when differentiated at *t* = 0.

Expanding the exponentials in their Taylor series obtains $B({\boldsymbol {\zeta }})=I-\sinh \zeta (\mathbf {n} \cdot \mathbf {K} )+(\cosh \zeta -1)(\mathbf {n} \cdot \mathbf {K} )^{2}$ $R({\boldsymbol {\theta }})=I+\sin \theta (\mathbf {e} \cdot \mathbf {J} )+(1-\cos \theta )(\mathbf {e} \cdot \mathbf {J} )^{2}\,.$ which compactly reproduce the boost and rotation matrices as given in the previous section.

It has been stated that the general proper Lorentz transformation is a product of a boost and rotation. At the *infinitesimal* level the product ${\begin{aligned}\Lambda &=(I-{\boldsymbol {\zeta }}\cdot \mathbf {K} +\cdots )(I+{\boldsymbol {\theta }}\cdot \mathbf {J} +\cdots )\\&=(I+{\boldsymbol {\theta }}\cdot \mathbf {J} +\cdots )(I-{\boldsymbol {\zeta }}\cdot \mathbf {K} +\cdots )\\&=I-{\boldsymbol {\zeta }}\cdot \mathbf {K} +{\boldsymbol {\theta }}\cdot \mathbf {J} +\cdots \end{aligned}}$ is commutative because only linear terms are required (products like (**θ**·**J**)(**ζ**·**K**) and (**ζ**·**K**)(**θ**·**J**) count as higher order terms and are negligible). Taking the limit as before leads to the finite transformation in the form of an exponential $\Lambda ({\boldsymbol {\zeta }},{\boldsymbol {\theta }})=e^{-{\boldsymbol {\zeta }}\cdot \mathbf {K} +{\boldsymbol {\theta }}\cdot \mathbf {J} }.$

The converse is also true, but the decomposition of a finite general Lorentz transformation into such factors is nontrivial. In particular, $e^{-{\boldsymbol {\zeta }}\cdot \mathbf {K} +{\boldsymbol {\theta }}\cdot \mathbf {J} }\neq e^{-{\boldsymbol {\zeta }}\cdot \mathbf {K} }e^{{\boldsymbol {\theta }}\cdot \mathbf {J} },$ because the generators do not commute. For a description of how to find the factors of a general Lorentz transformation in terms of a boost and a rotation *in principle* (this usually does not yield an intelligible expression in terms of generators **J** and **K**), see *Wigner rotation*. If, on the other hand, *the decomposition is given* in terms of the generators, and one wants to find the product in terms of the generators, then the Baker–Campbell–Hausdorff formula applies.

#### Lie algebra so(3,1)

Lorentz generators can be added together, or multiplied by real numbers, to obtain more Lorentz generators. In other words, the set of all Lorentz generators $V=\{{\boldsymbol {\zeta }}\cdot \mathbf {K} +{\boldsymbol {\theta }}\cdot \mathbf {J} \}$ together with the operations of ordinary matrix addition and multiplication of a matrix by a number, forms a vector space over the real numbers. The generators *J**x*, *J**y*, *J**z*, *K**x*, *K**y*, *K**z* form a basis set of *V*, and the components of the axis-angle and rapidity vectors, *θ**x*, *θ**y*, *θ**z*, *ζ**x*, *ζ**y*, *ζ**z*, are the coordinates of a Lorentz generator with respect to this basis.

Three of the commutation relations of the Lorentz generators are $[J_{\text{x}},J_{\text{y}}]=J_{\text{z}}\,,\quad [K_{\text{x}},K_{\text{y}}]=-J_{\text{z}}\,,\quad [J_{\text{x}},K_{\text{y}}]=K_{\text{z}}\,,$ where the bracket [*A*, *B*] = *AB* − *BA* is known as the *commutator*, and the other relations can be found by taking cyclic permutations of x, y, z components (i.e. change x to y, y to z, and z to x, repeat).

These commutation relations, and the vector space of generators, fulfill the definition of the Lie algebra ${\mathfrak {so}}(3,1)$ . In summary, a Lie algebra is defined as a vector space *V* over a field of numbers, and with a binary operation [ , ] (called a Lie bracket in this context) on the elements of the vector space, satisfying the axioms of bilinearity, alternatization, and the Jacobi identity. Here the operation [ , ] is the commutator which satisfies all of these axioms, the vector space is the set of Lorentz generators *V* as given previously, and the field is the set of real numbers.

Linking terminology used in mathematics and physics: A group generator is any element of the Lie algebra. A group parameter is a component of a coordinate vector representing an arbitrary element of the Lie algebra with respect to some basis. A basis, then, is a set of generators being a basis of the Lie algebra in the usual vector space sense.

The exponential map from the Lie algebra to the Lie group, $\exp :{\mathfrak {so}}(3,1)\to \mathrm {SO} (3,1),$ provides a one-to-one correspondence between small enough neighborhoods of the origin of the Lie algebra and neighborhoods of the identity element of the Lie group. In the case of the Lorentz group, the exponential map is just the matrix exponential. Globally, the exponential map is not one-to-one, but in the case of the Lorentz group, it is surjective (onto). Hence any group element in the connected component of the identity can be expressed as an exponential of an element of the Lie algebra.

### Improper transformations

Lorentz transformations also include parity inversion $P={\begin{bmatrix}1&0\\0&-\mathbf {I} \end{bmatrix}}$ which negates all the spatial coordinates only, and time reversal $T={\begin{bmatrix}-1&0\\0&\mathbf {I} \end{bmatrix}}$ which negates the time coordinate only, because these transformations leave the spacetime interval invariant. Here **I** is the 3 × 3 identity matrix. These are both symmetric, they are their own inverses (see *Involution (mathematics)*), and each have determinant −1. This latter property makes them improper transformations.

If Λ is a proper orthochronous Lorentz transformation, then *T*Λ is improper antichronous, *P*Λ is improper orthochronous, and *TP*Λ = *PT*Λ is proper antichronous.

### Inhomogeneous Lorentz group

Two other spacetime symmetries have not been accounted for. In order for the spacetime interval to be invariant, it can be shown that it is necessary and sufficient for the coordinate transformation to be of the form $X'=\Lambda X+C$ where *C* is a constant column containing translations in time and space. If *C* ≠ 0, this is an **inhomogeneous Lorentz transformation** or **Poincaré transformation**. If *C* = 0, this is a **homogeneous Lorentz transformation**. Poincaré transformations are not dealt further in this article.


## Tensor formulation

### Contravariant vectors

Writing the general matrix transformation of coordinates as the matrix equation ${\begin{bmatrix}{x'}^{0}\\{x'}^{1}\\{x'}^{2}\\{x'}^{3}\end{bmatrix}}={\begin{bmatrix}{\Lambda ^{0}}_{0}&{\Lambda ^{0}}_{1}&{\Lambda ^{0}}_{2}&{\Lambda ^{0}}_{3}{\vphantom {{x'}^{0}}}\\{\Lambda ^{1}}_{0}&{\Lambda ^{1}}_{1}&{\Lambda ^{1}}_{2}&{\Lambda ^{1}}_{3}{\vphantom {{x'}^{0}}}\\{\Lambda ^{2}}_{0}&{\Lambda ^{2}}_{1}&{\Lambda ^{2}}_{2}&{\Lambda ^{2}}_{3}{\vphantom {{x'}^{0}}}\\{\Lambda ^{3}}_{0}&{\Lambda ^{3}}_{1}&{\Lambda ^{3}}_{2}&{\Lambda ^{3}}_{3}{\vphantom {{x'}^{0}}}\\\end{bmatrix}}{\begin{bmatrix}x^{0}{\vphantom {{x'}^{0}}}\\x^{1}{\vphantom {{x'}^{0}}}\\x^{2}{\vphantom {{x'}^{0}}}\\x^{3}{\vphantom {{x'}^{0}}}\end{bmatrix}}$ allows the transformation of other physical quantities that cannot be expressed as four-vectors; e.g., tensors or spinors of any order in 4-dimensional spacetime, to be defined. In the corresponding tensor index notation, the above matrix expression is ${x'}^{\nu }={\Lambda ^{\nu }}_{\mu }x^{\mu },$

where lower and upper indices label covariant and contravariant components respectively, and the summation convention is applied. It is a standard convention to use Greek indices that take the value 0 for time components, and 1, 2, 3 for space components, while Latin indices simply take the values 1, 2, 3, for spatial components (the opposite for Landau and Lifshitz). Note that the first index (reading left to right) corresponds in the matrix notation to a *row index*. The second index corresponds to the column index.

The transformation matrix is universal for all four-vectors, not just 4-dimensional spacetime coordinates. If A is any four-vector, then in tensor index notation ${A'}^{\nu }={\Lambda ^{\nu }}_{\mu }A^{\mu }\,.$

Alternatively, one writes $A^{\nu '}={\Lambda ^{\nu '}}_{\mu }A^{\mu }\,.$ in which the primed indices denote the indices of *A* in the primed frame. For a general n-component object one may write ${X'}^{\alpha }={\Pi (\Lambda )^{\alpha }}_{\beta }X^{\beta }\,,$ where Π is the appropriate representation of the Lorentz group, an *n* × *n* matrix for every Λ. In this case, the indices should *not* be thought of as spacetime indices (sometimes called Lorentz indices), and they run from 1 to n. E.g., if X is a Dirac spinor, then the indices are called *Dirac indices*.

### Covariant vectors

There are also vector quantities with covariant indices. They are generally obtained from their corresponding objects with contravariant indices by the operation of *lowering an index*; e.g., $x_{\nu }=\eta _{\mu \nu }x^{\mu },$ where η is the metric tensor. (The linked article also provides more information about what the operation of raising and lowering indices really is mathematically.) The inverse of this transformation is given by $x^{\mu }=\eta ^{\mu \nu }x_{\nu },$ where, when viewed as matrices, *η**μν* is the inverse of *η**μν*. As it happens, *η**μν* = *η**μν*. This is referred to as *raising an index*. To transform a covariant vector *A**μ*, first raise its index, then transform it according to the same rule as for contravariant 4-vectors, then finally lower the index; ${A'}_{\nu }=\eta _{\rho \nu }{\Lambda ^{\rho }}_{\sigma }\eta ^{\mu \sigma }A_{\mu }.$

But $\eta _{\rho \nu }{\Lambda ^{\rho }}_{\sigma }\eta ^{\mu \sigma }={\left(\Lambda ^{-1}\right)^{\mu }}_{\nu },$

That is, it is the (*μ*, *ν*)-component of the *inverse* Lorentz transformation. One defines (as a matter of notation), ${\Lambda _{\nu }}^{\mu }\equiv {\left(\Lambda ^{-1}\right)^{\mu }}_{\nu },$ and may in this notation write ${A'}_{\nu }={\Lambda _{\nu }}^{\mu }A_{\mu }.$

Now for a subtlety. The implied summation on the right hand side of ${A'}_{\nu }={\Lambda _{\nu }}^{\mu }A_{\mu }={\left(\Lambda ^{-1}\right)^{\mu }}_{\nu }A_{\mu }$ is running over *a row index* of the matrix representing Λ−1. Thus, in terms of matrices, this transformation should be thought of as the *inverse transpose* of Λ acting on the column vector *A**μ*. That is, in pure matrix notation, $A'=\left(\Lambda ^{-1}\right)^{\mathrm {T} }A.$

This means exactly that covariant vectors (thought of as column matrices) transform according to the dual representation of the standard representation of the Lorentz group. This notion generalizes to general representations, simply replace Λ with Π(Λ).

### Tensors

If A and B are linear operators on vector spaces U and V, then a linear operator *A* ⊗ *B* may be defined on the tensor product of U and V, denoted *U* ⊗ *V* according to

$(A\otimes B)(u\otimes v)=Au\otimes Bv,\qquad u\in U,v\in V,u\otimes v\in U\otimes V.$               (T1)

From this it is immediately clear that if u and v are a four-vectors in V, then *u* ⊗ *v* ∈ *T*2*V* ≡ *V* ⊗ *V* transforms as

$u\otimes v\rightarrow \Lambda u\otimes \Lambda v={\Lambda ^{\mu }}_{\nu }u^{\nu }\otimes {\Lambda ^{\rho }}_{\sigma }v^{\sigma }={\Lambda ^{\mu }}_{\nu }{\Lambda ^{\rho }}_{\sigma }u^{\nu }\otimes v^{\sigma }\equiv {\Lambda ^{\mu }}_{\nu }{\Lambda ^{\rho }}_{\sigma }w^{\nu \sigma }.$               (T2)

The second step uses the bilinearity of the tensor product and the last step defines a 2-tensor on component form, or rather, it just renames the tensor *u* ⊗ *v*.

These observations generalize in an obvious way to more factors, and using the fact that a general tensor on a vector space V can be written as a sum of a coefficient (component!) times tensor products of basis vectors and basis covectors, one arrives at the transformation law for any tensor quantity T. It is given by

$T_{\theta '\iota '\cdots \kappa '}^{\alpha '\beta '\cdots \zeta '}={\Lambda ^{\alpha '}}_{\mu }{\Lambda ^{\beta '}}_{\nu }\cdots {\Lambda ^{\zeta '}}_{\rho }{\Lambda _{\theta '}}^{\sigma }{\Lambda _{\iota '}}^{\upsilon }\cdots {\Lambda _{\kappa '}}^{\zeta }T_{\sigma \upsilon \cdots \zeta }^{\mu \nu \cdots \rho },$               (T3)

where *Λ**χ*′*ψ* is defined above. This form can generally be reduced to the form for general n-component objects given above with a single matrix (Π(Λ)) operating on column vectors. This latter form is sometimes preferred; e.g., for the electromagnetic field tensor.

#### Transformation of the electromagnetic field

Lorentz transformations can also be used to illustrate that the magnetic field **B** and electric field **E** are simply different aspects of the same force—the electromagnetic force, as a consequence of relative motion between electric charges and observers. The fact that the electromagnetic field shows relativistic effects becomes clear by carrying out a simple thought experiment.

- An observer measures a charge at rest in frame F. The observer will detect a static electric field. As the charge is stationary in this frame, there is no electric current, so the observer does not observe any magnetic field.
- The other observer in frame F′ moves at velocity **v** relative to F and the charge. *This* observer sees a different electric field because the charge moves at velocity −**v** in their rest frame. The motion of the charge corresponds to an electric current, and thus the observer in frame F′ also sees a magnetic field.

The electric and magnetic fields transform differently from space and time, but exactly the same way as relativistic angular momentum and the boost vector.

The electromagnetic field strength tensor is given by $F^{\mu \nu }={\begin{bmatrix}0&-{\frac {1}{c}}E_{\text{x}}&-{\frac {1}{c}}E_{\text{y}}&-{\frac {1}{c}}E_{\text{z}}\\{\frac {1}{c}}E_{\text{x}}&0&-B_{\text{z}}&B_{\text{y}}\\{\frac {1}{c}}E_{\text{y}}&B_{\text{z}}&0&-B_{\text{x}}\\{\frac {1}{c}}E_{\text{z}}&-B_{\text{y}}&B_{\text{x}}&0\end{bmatrix}}$ in with signature (+, −, −, −). In relativity, the factor *c* may be absorbed into the tensor components to eliminate its explicit appearance in expressions. Consider a Lorentz boost in the x-direction. It is given by ${\Lambda ^{\mu }}_{\nu }={\begin{bmatrix}\gamma &-\gamma \beta &0&0\\-\gamma \beta &\gamma &0&0\\0&0&1&0\\0&0&0&1\\\end{bmatrix}},\qquad F^{\mu \nu }={\begin{bmatrix}0&E_{\text{x}}&E_{\text{y}}&E_{\text{z}}\\-E_{\text{x}}&0&B_{\text{z}}&-B_{\text{y}}\\-E_{\text{y}}&-B_{\text{z}}&0&B_{\text{x}}\\-E_{\text{z}}&B_{\text{y}}&-B_{\text{x}}&0\end{bmatrix}},$ where the signature is (−, +, +, +) and the field tensor is displayed side by side for easiest possible reference in the manipulations below.

The general transformation law **(T3)** becomes $F^{\mu '\nu '}={\Lambda ^{\mu '}}_{\mu }{\Lambda ^{\nu '}}_{\nu }F^{\mu \nu }.$

For the magnetic field one obtains ${\begin{aligned}B_{x'}&=F^{2'3'}={\Lambda ^{2}}_{\mu }{\Lambda ^{3}}_{\nu }F^{\mu \nu }={\Lambda ^{2}}_{2}{\Lambda ^{3}}_{3}F^{23}=1\times 1\times B_{\text{x}}\\&=B_{\text{x}},\\B_{y'}&=F^{3'1'}={\Lambda ^{3}}_{\mu }{\Lambda ^{1}}_{\nu }F^{\mu \nu }={\Lambda ^{3}}_{3}{\Lambda ^{1}}_{\nu }F^{3\nu }={\Lambda ^{3}}_{3}{\Lambda ^{1}}_{0}F^{30}+{\Lambda ^{3}}_{3}{\Lambda ^{1}}_{1}F^{31}\\&=1\times (-\beta \gamma )(-E_{\text{z}})+1\times \gamma B_{\text{y}}=\gamma B_{\text{y}}+\beta \gamma E_{\text{z}}\\&=\gamma \left(\mathbf {B} -{\boldsymbol {\beta }}\times \mathbf {E} \right)_{\text{y}}\\B_{z'}&=F^{1'2'}={\Lambda ^{1}}_{\mu }{\Lambda ^{2}}_{\nu }F^{\mu \nu }={\Lambda ^{1}}_{\mu }{\Lambda ^{2}}_{2}F^{\mu 2}={\Lambda ^{1}}_{0}{\Lambda ^{2}}_{2}F^{02}+{\Lambda ^{1}}_{1}{\Lambda ^{2}}_{2}F^{12}\\&=(-\gamma \beta )\times 1\times E_{\text{y}}+\gamma \times 1\times B_{\text{z}}=\gamma B_{\text{z}}-\beta \gamma E_{\text{y}}\\&=\gamma \left(\mathbf {B} -{\boldsymbol {\beta }}\times \mathbf {E} \right)_{\text{z}}\end{aligned}}$

For the electric field results ${\begin{aligned}E_{x'}&=F^{0'1'}={\Lambda ^{0}}_{\mu }{\Lambda ^{1}}_{\nu }F^{\mu \nu }={\Lambda ^{0}}_{1}{\Lambda ^{1}}_{0}F^{10}+{\Lambda ^{0}}_{0}{\Lambda ^{1}}_{1}F^{01}\\&=(-\gamma \beta )(-\gamma \beta )(-E_{\text{x}})+\gamma \gamma E_{\text{x}}=-\gamma ^{2}\beta ^{2}(E_{\text{x}})+\gamma ^{2}E_{\text{x}}=E_{\text{x}}(1-\beta ^{2})\gamma ^{2}\\&=E_{\text{x}},\\E_{y'}&=F^{0'2'}={\Lambda ^{0}}_{\mu }{\Lambda ^{2}}_{\nu }F^{\mu \nu }={\Lambda ^{0}}_{\mu }{\Lambda ^{2}}_{2}F^{\mu 2}={\Lambda ^{0}}_{0}{\Lambda ^{2}}_{2}F^{02}+{\Lambda ^{0}}_{1}{\Lambda ^{2}}_{2}F^{12}\\&=\gamma \times 1\times E_{\text{y}}+(-\beta \gamma )\times 1\times B_{\text{z}}=\gamma E_{\text{y}}-\beta \gamma B_{\text{z}}\\&=\gamma \left(\mathbf {E} +{\boldsymbol {\beta }}\times \mathbf {B} \right)_{\text{y}}\\E_{z'}&=F^{0'3'}={\Lambda ^{0}}_{\mu }{\Lambda ^{3}}_{\nu }F^{\mu \nu }={\Lambda ^{0}}_{\mu }{\Lambda ^{3}}_{3}F^{\mu 3}={\Lambda ^{0}}_{0}{\Lambda ^{3}}_{3}F^{03}+{\Lambda ^{0}}_{1}{\Lambda ^{3}}_{3}F^{13}\\&=\gamma \times 1\times E_{\text{z}}-\beta \gamma \times 1\times (-B_{\text{y}})=\gamma E_{\text{z}}+\beta \gamma B_{\text{y}}\\&=\gamma \left(\mathbf {E} +{\boldsymbol {\beta }}\times \mathbf {B} \right)_{\text{z}}.\end{aligned}}$

Here, ***β*** = (*β*, 0, 0) is used. These results can be summarized by ${\begin{aligned}\mathbf {E} _{\parallel '}&=\mathbf {E} _{\parallel }\\\mathbf {B} _{\parallel '}&=\mathbf {B} _{\parallel }\\\mathbf {E} _{\bot '}&=\gamma \left(\mathbf {E} _{\bot }+{\boldsymbol {\beta }}\times \mathbf {B} _{\bot }\right)=\gamma \left(\mathbf {E} +{\boldsymbol {\beta }}\times \mathbf {B} \right)_{\bot },\\\mathbf {B} _{\bot '}&=\gamma \left(\mathbf {B} _{\bot }-{\boldsymbol {\beta }}\times \mathbf {E} _{\bot }\right)=\gamma \left(\mathbf {B} -{\boldsymbol {\beta }}\times \mathbf {E} \right)_{\bot },\end{aligned}}$ and are independent of the metric signature. For SI units, substitute *E* → *E*/*c*. Misner, Thorne & Wheeler (1973) refer to this last form as the 3 + 1 view as opposed to the *geometric view* represented by the tensor expression $F^{\mu '\nu '}={\Lambda ^{\mu '}}_{\mu }{\Lambda ^{\nu '}}_{\nu }F^{\mu \nu },$ and make a strong point of the ease with which results that are difficult to achieve using the 3 + 1 view can be obtained and understood. Only objects that have well defined Lorentz transformation properties (in fact under *any* smooth coordinate transformation) are geometric objects. In the geometric view, the electromagnetic field is a six-dimensional geometric object in *spacetime* as opposed to two interdependent, but separate, 3-vector fields in *space* and *time*. The fields **E** (alone) and **B** (alone) do not have well defined Lorentz transformation properties. The mathematical underpinnings are equations **(T1)** and **(T2)** that immediately yield **(T3)**. The primed and unprimed tensors refer to the *same event in spacetime*. Thus the complete equation with spacetime dependence is $F^{\mu '\nu '}\left(x'\right)={\Lambda ^{\mu '}}_{\mu }{\Lambda ^{\nu '}}_{\nu }F^{\mu \nu }\left(\Lambda ^{-1}x'\right)={\Lambda ^{\mu '}}_{\mu }{\Lambda ^{\nu '}}_{\nu }F^{\mu \nu }(x).$

Length contraction has an effect on charge density ρ and current density **J**, and time dilation has an effect on the rate of flow of charge (current), so charge and current distributions must transform in a related way under a boost. It turns out they transform exactly like the space-time and energy-momentum four-vectors, ${\begin{aligned}\mathbf {j} '&=\mathbf {j} -\gamma \rho v\mathbf {n} +\left(\gamma -1\right)(\mathbf {j} \cdot \mathbf {n} )\mathbf {n} \\\rho '&=\gamma \left(\rho -\mathbf {j} \cdot {\frac {v\mathbf {n} }{c^{2}}}\right),\end{aligned}}$ or, in the simpler geometric view, $j^{\mu '}={\Lambda ^{\mu '}}_{\mu }j^{\mu }.$

Charge density transforms as the time component of a four-vector. It is a rotational scalar. The current density is a 3-vector.

The Maxwell equations are invariant under Lorentz transformations.

### Spinors

Equation **(T1)** hold unmodified for any representation of the Lorentz group, including the Dirac spinor representation. In **(T2)** one simply replaces all occurrences of Λ by the Dirac spinor representation Π(Λ),

${\begin{aligned}u\otimes v\rightarrow \Pi (\Lambda )u\otimes \Pi (\Lambda )v&={\Pi (\Lambda )^{\alpha }}_{\beta }u^{\beta }\otimes {\Pi (\Lambda )^{\rho }}_{\sigma }v^{\sigma }\\&={\Pi (\Lambda )^{\alpha }}_{\beta }{\Pi (\Lambda )^{\rho }}_{\sigma }u^{\beta }\otimes v^{\sigma }\\&\equiv {\Pi (\Lambda )^{\alpha }}_{\beta }{\Pi (\Lambda )^{\rho }}_{\sigma }w^{\beta \sigma }\end{aligned}}$               (T4)

The above equation could, for instance, be the transformation of a state in Fock space describing two free electrons.

#### Transformation of general fields

A general *noninteracting* multi-particle state (Fock space state) in quantum field theory transforms according to the rule

| ${\begin{aligned}&U(\Lambda ,a)\Psi _{p_{1}\sigma _{1}n_{1};p_{2}\sigma _{2}n_{2};\cdots }\\={}&e^{-ia_{\mu }\left[(\Lambda p_{1})^{\mu }+(\Lambda p_{2})^{\mu }+\cdots \right]}{\sqrt {\frac {(\Lambda p_{1})^{0}(\Lambda p_{2})^{0}\cdots }{p_{1}^{0}p_{2}^{0}\cdots }}}\left(\sum _{\sigma _{1}'\sigma _{2}'\cdots }D_{\sigma _{1}'\sigma _{1}}^{(j_{1})}\left[W(\Lambda ,p_{1})\right]D_{\sigma _{2}'\sigma _{2}}^{(j_{2})}\left[W(\Lambda ,p_{2})\right]\cdots \right)\Psi _{\Lambda p_{1}\sigma _{1}'n_{1};\Lambda p_{2}\sigma _{2}'n_{2};\cdots },\end{aligned}}$ |   | 1 |
|---|---|---|

where *W*(Λ, *p*) is the Wigner's little group and *D*(*j*) is the (2*j* + 1)-dimensional representation of SO(3).
