---
title: "Quaternion (part 1/2)"
source: https://en.wikipedia.org/wiki/Quaternion
domain: quaternions-octonions
license: CC-BY-SA-4.0
tags: quaternion algebra, octonion algebra, cayley-dickson construction, spatial rotation
fetched: 2026-07-02
part: 1/2
---

# Quaternion

| ↓ × → | 1 | **i** | **j** | **k** |
|---|---|---|---|---|
| 1 | 1 | **i** | **j** | **k** |
| **i** | **i** | −1 | **k** | −**j** |
| **j** | **j** | −**k** | −1 | **i** |
| **k** | **k** | **j** | −**i** | −1 |
| Left column shows the left factor, top row shows the right factor. Also, $a\mathbf {b} =\mathbf {b} a$ and $-\mathbf {b} =(-1)\mathbf {b}$ for $a\in \mathbb {R}$ , $\mathbf {b} =\mathbf {i} ,\mathbf {j} ,\mathbf {k}$ . |   |   |   |   |

In mathematics, the **quaternions** form a number system similar to the complex numbers, with the usual arithmetical operations of addition, subtraction, multiplication, and division, but with four real-number components instead of two. Unlike with the complex numbers, quaternion multiplication is not commutative, meaning that the result of multiplying two quaternions depends on their order. Quaternions can be used to represent vectors in three-dimensional space, which provides a definition of the quotient of two vectors.

Quaternions were first described by the Irish mathematician and physicist William Rowan Hamilton in 1843, and in his honor the set of all quaternions is conventionally denoted by $\mathbb {H}$ or **H**. A generic quaternion is usually represented in the form $a+b\,\mathbf {i} +c\,\mathbf {j} +d\,\mathbf {k} ,$ where the coefficients a, b, c, d are real numbers, and 1, **i**, **j**, **k** are the *basis vectors* or *basis elements*.

Quaternions are used in pure mathematics, but also have practical uses in applied mathematics, particularly for calculations involving three-dimensional rotations, such as in three-dimensional computer graphics, computer vision, robotics, magnetic resonance imaging and crystallographic texture analysis. They can be used alongside other methods of rotation, such as Euler angles and rotation matrices, or as an alternative to them, depending on the application.

As an abstract mathematical structure, quaternions form a four-dimensional associative normed division algebra over the real numbers, and therefore a ring, also a division ring and a domain. Because of their non-commutative multiplication, they do not form a field. The quaternions are also a special case of a Clifford algebra, classified as $\operatorname {Cl} _{0,2}(\mathbb {R} )\cong \operatorname {Cl} _{3,0}^{+}(\mathbb {R} ).$

According to the Frobenius theorem, the algebra $\mathbb {H}$ is one of only two finite-dimensional division rings containing a proper subring isomorphic to the real numbers; the other being the complex numbers. These rings are also Euclidean Hurwitz algebras, of which the quaternions are the largest associative algebra (and hence the largest ring). Further extending the quaternions yields the non-associative octonions, which is the last normed division algebra over the real numbers. The next extension gives the sedenions, which have zero divisors and so cannot be a normed division algebra.

The unit quaternions give a group structure on the 3-sphere S3 isomorphic to the groups Spin(3) and SU(2), i.e. the universal cover group of SO(3). The positive and negative basis vectors form the eight-element quaternion group.


## History

Quaternions were introduced by Hamilton in 1843. Important precursors to this work included Euler's four-square identity (1748) and Olinde Rodrigues' parameterization of general rotations by four parameters (1840), but neither of these writers treated the four-parameter rotations as an algebra. Gauss had discovered quaternions in 1819, but this work was not published until 1900.

Hamilton knew that the complex numbers could be interpreted as points in a plane, and he was looking for a way to do the same for points in three-dimensional space. Points in space can be represented by their coordinates, which are triples of numbers, and for many years he had known how to add and subtract triples of numbers. However, for a long time, he had been stuck on the problem of multiplication and division. He could not figure out how to calculate the quotient of the coordinates of two points in space. In fact, Ferdinand Georg Frobenius later proved in 1877 that for a division algebra over the real numbers to be finite-dimensional and associative, it cannot be three-dimensional, and there are only three such division algebras: $\mathbb {R,C}$ (complex numbers) and $\mathbb {H}$ (quaternions) which have dimension 1, 2, and 4 respectively.

The great breakthrough in quaternions finally came on Monday 16 October 1843 in Dublin, when Hamilton was on his way to the Royal Irish Academy to preside at a council meeting. As he walked along the towpath of the Royal Canal with his wife, the concepts behind quaternions were taking shape in his mind. When the answer dawned on him, Hamilton could not resist the urge to carve the defining formula for the quaternions into the stone of Brougham Bridge with his pocket knife:

$\mathbf {i} ^{2}=\mathbf {j} ^{2}=\mathbf {k} ^{2}=\mathbf {i\;j\;k} =-1$

Although the carving has since faded away, there has been an annual pilgrimage since 1989, called the *Hamilton Walk*, for scientists and mathematicians who process from the Dunsink Observatory to the Royal Canal bridge in remembrance of Hamilton's discovery.

On the following day, Hamilton wrote a letter to his friend and fellow mathematician, J.T. Graves, describing the train of thought that led to his discovery. The letter was later published in a letter to the *Philosophical Magazine*; Hamilton states:

> And here there dawned on me the notion that we must admit, in some sense, a fourth dimension of space for the purpose of calculating with triples ... An electric circuit seemed to close, and a spark flashed forth.

Hamilton called a quadruple with these rules of multiplication a *quaternion*, and he devoted most of the remainder of his life to studying and teaching them. Hamilton's treatment is more geometric than the modern approach, which emphasizes quaternions' algebraic properties. He founded a school of "quaternionists", and he tried to popularize quaternions in several books. The last and longest of his books, *Elements of Quaternions*, was 800 pages long; it was edited by his son and published shortly after his death.

After Hamilton's death, the Scottish mathematical physicist Peter Tait became the chief exponent of quaternions. At this time, quaternions were a mandatory examination topic in Dublin. Topics in physics and geometry that would now be described using vectors, such as kinematics in space and Maxwell's equations, were described entirely in terms of quaternions. There was even a professional research association, the Quaternion Association, devoted to the study of quaternions and other hypercomplex number systems.

From the mid-1880s, quaternions began to be displaced by vector analysis, which had been developed by Josiah Willard Gibbs, Oliver Heaviside, and Hermann von Helmholtz. Vector analysis described the same phenomena as quaternions, so it borrowed some ideas and terminology liberally from the literature on quaternions. However, vector analysis was conceptually simpler and notationally cleaner, and eventually quaternions were relegated to a minor role in mathematics and physics. A side-effect of this transition is that Hamilton's work is difficult to comprehend for many modern readers. Hamilton's original definitions are unfamiliar and his writing style was wordy and difficult to follow.

However, quaternions have had a revival since the late 20th century, primarily due to their utility in describing spatial rotations. The representations of rotations by quaternions are more compact and quicker to compute than the representations by matrices. In addition, unlike Euler angles, they are not susceptible to "gimbal lock". For this reason, quaternions are used in computer graphics, computer vision, robotics, nuclear magnetic resonance image sampling, control theory, signal processing, attitude control, physics, bioinformatics, molecular dynamics, computer simulations, and orbital mechanics. For example, it is common for the attitude control systems of spacecraft to be commanded in terms of quaternions. Quaternions also have contributed to number theory, because of their relationships with the quadratic forms.

### Quaternions in physics

Hamilton had introduced biquaternions in his *Lectures on Quaternions*, and these were used by Ludwik Silberstein in 1914 to exhibit the Lorentz transformations of special relativity. This representation of Lorentz transformations was also used by Cornelius Lanczos in 1949.

The finding of 1924 that in quantum mechanics the spin of an electron and other matter particles (known as spinors) can be described using quaternions (in the form of the famous Pauli spin matrices) furthered their interest; quaternions helped to understand how rotations of electrons by 360° can be discerned from those by 720° (the "Plate trick"). As of 2018, their use has not yet overtaken rotation groups.

W. K. Clifford (1845 − 1879) introduced his algebras as a tensor product (”compound of algebras”) of quaternion algebras (and its even sub-algebra), a concept introduced by B. Peirce (1809 − 1880). R. Lipschitz (1832 − 1903) rediscovered independently the even subalgebra. In 1922, C. L. E. Moore (1876 − 1931) was to call Lipschitz’ algebras ”hyperquaternions”. The term ”hyperquaternion” designates nowadays both the tensor product of n quaternion algebras $\mathbb {H} ^{\otimes n}$ and its even subalgebra $\mathbb {H} ^{\otimes n-1}\otimes \mathbb {C}$ .

Examples of hyperquaternions are: $\mathbb {H} ,\mathbb {H} ^{\otimes 2}=\mathbb {H} \otimes _{\mathbb {R} }\mathbb {H}$ (isomorphic to the Clifford algebra $Cl_{3,1}\mathbb {(R)}$ and to $4\times 4$ real matrices $M(4,\mathbb {R} )$ ) leading to applications in special relativity. Its even subalgebra is $\mathbb {H} \otimes \mathbb {C}$ (biquaternions).

Another example is $\mathbb {H} ^{\otimes 3}=M(4,\mathbb {H} )$ yielding a quaternionic matrix and its even subalgebra $\mathbb {H} ^{\otimes 2}\otimes _{\mathbb {R} }\mathbb {C}$ (Dirac algebra).


## Definition

A *quaternion* is an expression of the form

$a+b\,\mathbf {i} +c\,\mathbf {j} +d\,\mathbf {k} ,$

where a, b, c, d, are real numbers, and **i**, **j**, **k**, are symbols that can be interpreted as unit-vectors pointing along the three spatial axes. In practice, if one of a, b, c, d is 0, the corresponding term is omitted; if a, b, c, d are all zero, the quaternion is the *zero quaternion*, denoted 0; if one of b, c, d equals 1, the corresponding term is written simply **i**, **j**, or **k**.

A quaternion $q=a+b\,\mathbf {i} +c\,\mathbf {j} +d\,\mathbf {k}$ , can be decomposed into its *scalar part* ⁠ a ⁠ (sometimes *real part*) and its *vector part* $q-a=b\,\mathbf {i} +c\,\mathbf {j} +d\,\mathbf {k}$ (sometimes *imaginary part*). A quaternion that equals its real part (that is, its vector part is zero) is called a **scalar quaternion** (sometimes *real quaternion* or simply *scalar*), and is identified with the corresponding real number. That is, the real numbers are *embedded* in the quaternions. A quaternion that equals its vector part is called a **vector quaternion** (sometimes *right quaternion*).

Quaternions form a 4-dimensional vector space over the real numbers, with $\left\{1,\mathbf {i} ,\mathbf {j} ,\mathbf {k} \right\}$ as a basis, by the component-wise addition

${\begin{aligned}&(a_{1}+b_{1}\mathbf {i} +c_{1}\mathbf {j} +d_{1}\mathbf {k} )+(a_{2}+b_{2}\mathbf {i} +c_{2}\mathbf {j} +d_{2}\mathbf {k} )\\[3mu]&\qquad =(a_{1}+a_{2})+(b_{1}+b_{2})\mathbf {i} +(c_{1}+c_{2})\mathbf {j} +(d_{1}+d_{2})\mathbf {k} ,\end{aligned}}$

and the component-wise scalar multiplication

$\lambda (a+b\,\mathbf {i} +c\,\mathbf {j} +d\,\mathbf {k} )=\lambda a+(\lambda b)\mathbf {i} +(\lambda c)\mathbf {j} +(\lambda d)\mathbf {k} .$

A multiplicative group structure, called the *Hamilton product*, denoted by juxtaposition, can be defined on the quaternions in the following way:

- The scalar quaternion 1 is the identity element.
- The scalar quaternions commute with all other quaternions, that is *aq* = *qa* for every quaternion q and every scalar quaternion a. In algebraic terminology this is to say that the field of the scalar quaternions is the *center* of the quaternion algebra.
- The product is first given for the basis elements, and then extended to all quaternions by using the distributive property and the center property of the scalar quaternions (see below for details). The Hamilton product is not commutative, but is associative, thus the quaternions form an associative algebra over the real numbers.
- Additionally, every nonzero quaternion has an inverse with respect to the Hamilton product: $(a+b\,\mathbf {i} +c\,\mathbf {j} +d\,\mathbf {k} )^{-1}={\frac {1}{a^{2}+b^{2}+c^{2}+d^{2}}}\,(a-b\,\mathbf {i} -c\,\mathbf {j} -d\,\mathbf {k} ).$

Thus the quaternions form a division algebra.

### Multiplication of basis elements

| ↓ × → | 1 | **i** | **j** | **k** |
|---|---|---|---|---|
| 1 | 1 | **i** | **j** | **k** |
| **i** | **i** | −1 | **k** | −**j** |
| **j** | **j** | −**k** | −1 | **i** |
| **k** | **k** | **j** | −**i** | −1 |
| Non-commutativity is emphasized by colored squares |   |   |   |   |

The multiplication with 1 of the basis elements **i**, **j**, and **k** is defined by the fact that 1 is a multiplicative identity, that is, $\mathbf {i} \,1=1\,\mathbf {i} =\mathbf {i} ,\qquad \mathbf {j} \,1=1\,\mathbf {j} =\mathbf {j} ,\qquad \mathbf {k} \,1=1\,\mathbf {k} =\mathbf {k} .$

The products of other basis elements are ${\begin{aligned}\mathbf {i} ^{2}&=\mathbf {j} ^{2}=\mathbf {k} ^{2}=-1,\\\mathbf {i\,j} &=-\mathbf {j\,i} =\mathbf {k} ,\qquad \mathbf {j\,k} =-\mathbf {k\,j} =\mathbf {i} ,\qquad \mathbf {k\,i} =-\mathbf {i\,k} =\mathbf {j} .\end{aligned}}$

Combining these rules, ${\begin{aligned}\mathbf {i\,j\,k} &=-1.\end{aligned}}$

### Center

The *center* of a noncommutative ring is the subring of elements c such that *cx* = *xc* for every x. The center of the quaternion algebra is the subfield of scalar quaternions. In fact, it is a part of the definition that the scalar quaternions belong to the center. Conversely, if *q* = *a* + *b* **i** + *c* **j** + *d* **k** belongs to the center, then $0=\mathbf {i} \,q-q\,\mathbf {i} =2c\,\mathbf {i} \mathbf {j} +2d\,\mathbf {i} \mathbf {k} =2c\,\mathbf {k} -2d\,\mathbf {j} ,$

and *c* = *d* = 0. A similar computation with **j** instead of **i** shows that one has also *b* = 0. Thus *q* = *a* is a scalar quaternion.

The quaternions form a division algebra. This means that the non-commutativity of multiplication is the only property that makes quaternions different from a field. This non-commutativity has some unexpected consequences, among them that a polynomial equation over the quaternions can have more distinct solutions than the degree of the polynomial. For example, the equation *z*2 + 1 = 0, has infinitely many quaternion solutions, which are the quaternions *z* = *b* **i** + *c* **j** + *d* **k** such that *b*2 + *c*2 + *d*2 = 1. Thus these imaginary units form a unit sphere in the three-dimensional space of quaternion vectors.

### Hamilton product

For two elements *a*1 + *b*1**i** + *c*1**j** + *d*1**k** and *a*2 + *b*2**i** + *c*2**j** + *d*2**k**, their product, called the **Hamilton product** (*a*1 + *b*1**i** + *c*1**j** + *d*1**k**) (*a*2 + *b*2**i** + *c*2**j** + *d*2**k**), is determined by the products of the basis elements and the distributive law. The distributive law makes it possible to expand the product so that it is a sum of products of basis elements. This gives the following expression:

${\begin{alignedat}{4}&a_{1}a_{2}&&+a_{1}b_{2}\mathbf {i} &&+a_{1}c_{2}\mathbf {j} &&+a_{1}d_{2}\mathbf {k} \\{}+{}&b_{1}a_{2}\mathbf {i} &&+b_{1}b_{2}\mathbf {i} ^{2}&&+b_{1}c_{2}\mathbf {ij} &&+b_{1}d_{2}\mathbf {ik} \\{}+{}&c_{1}a_{2}\mathbf {j} &&+c_{1}b_{2}\mathbf {ji} &&+c_{1}c_{2}\mathbf {j} ^{2}&&+c_{1}d_{2}\mathbf {jk} \\{}+{}&d_{1}a_{2}\mathbf {k} &&+d_{1}b_{2}\mathbf {ki} &&+d_{1}c_{2}\mathbf {kj} &&+d_{1}d_{2}\mathbf {k} ^{2}\end{alignedat}}$

Now the basis elements can be multiplied using the rules given above to get:

${\begin{alignedat}{4}&a_{1}a_{2}&&-b_{1}b_{2}&&-c_{1}c_{2}&&-d_{1}d_{2}\\{}+{}(&a_{1}b_{2}&&+b_{1}a_{2}&&+c_{1}d_{2}&&-d_{1}c_{2})\mathbf {i} \\{}+{}(&a_{1}c_{2}&&-b_{1}d_{2}&&+c_{1}a_{2}&&+d_{1}b_{2})\mathbf {j} \\{}+{}(&a_{1}d_{2}&&+b_{1}c_{2}&&-c_{1}b_{2}&&+d_{1}a_{2})\mathbf {k} \end{alignedat}}$

### Scalar and vector parts

A quaternion of the form *a* + 0 **i** + 0 **j** + 0 **k**, where a is a real number, is called a *scalar quaternion* (sometimes *real quaternion*), and a quaternion of the form 0 + *b* **i** + *c* **j** + *d* **k**, where b, c, and d are real numbers, and at least one of b, c, or d is nonzero, is called a *vector quaternion* (sometimes *right quaternion*). For any quaternion *a* + *b* **i** + *c* **j** + *d* **k**, a is called its *scalar part* and *b* **i** + *c* **j** + *d* **k** is called its *vector part*. Even though every quaternion can be viewed as a vector in a four-dimensional vector space, it is common to refer to the vector part as vectors in three-dimensional space. With this convention, a vector is the same as an element of the vector space $\mathbb {R} ^{3}.$

Hamilton also called vector quaternions *right quaternions* and real numbers (considered as quaternions with zero vector part) *scalar quaternions*.

If a quaternion is divided up into its scalar part and its vector part, that is,

$\mathbf {q} =(r,\,{\vec {v}}),\ \mathbf {q} \in \mathbb {H} ,\ r\in \mathbb {R} ,\ {\vec {v}}\in \mathbb {R} ^{3},$

then the formulas for addition, multiplication, and multiplicative inverse are

${\begin{aligned}(r_{1},\,{\vec {v}}_{1})+(r_{2},\,{\vec {v}}_{2})&=(r_{1}+r_{2},\,{\vec {v}}_{1}+{\vec {v}}_{2}),\\[5mu](r_{1},\,{\vec {v}}_{1})(r_{2},\,{\vec {v}}_{2})&=(r_{1}r_{2}-{\vec {v}}_{1}\cdot {\vec {v}}_{2},\,r_{1}{\vec {v}}_{2}+r_{2}{\vec {v}}_{1}+{\vec {v}}_{1}\times {\vec {v}}_{2}),\\[5mu](r,\,{\vec {v}})^{-1}&=\left({\frac {r}{r^{2}+{\vec {v}}\cdot {\vec {v}}}},\ {\frac {-{\vec {v}}}{r^{2}+{\vec {v}}\cdot {\vec {v}}}}\right)\end{aligned}}$

where " ${}\cdot {}$ " and " $\times$ " denote respectively the dot product and the cross product.


## Conjugation, the norm, and reciprocal

Conjugation of quaternions is analogous to conjugation of complex numbers and to transposition (also known as reversal) of elements of Clifford algebras. To define it, let $q=a+b\,\mathbf {i} +c\,\mathbf {j} +d\,\mathbf {k}$ be a quaternion. The **conjugate** of q is the quaternion $q^{*}=a-b\,\mathbf {i} -c\,\mathbf {j} -d\,\mathbf {k}$ . It is denoted by *q*∗, *qt*, ${\tilde {q}}$ , or *q*. Conjugation is an involution, meaning that it is its own inverse, so conjugating an element twice returns the original element. The conjugate of a product of two quaternions is the product of the conjugates *in the reverse order*. That is, if p and q are quaternions, then (*pq*)∗ = *q*∗*p*∗, not *p*∗*q*∗.

The conjugation of a quaternion, in contrast to the complex setting, can be expressed with multiplication and addition of quaternions:

$q^{*}=-{\tfrac {1}{2}}(q+\mathbf {i} \,q\,\mathbf {i} +\mathbf {j} \,q\,\mathbf {j} +\mathbf {k} \,q\,\mathbf {k} ).$

Conjugation can be used to extract the scalar and vector parts of a quaternion. The scalar part of p is ⁠1/2⁠(*p* + *p*∗), and the vector part of p is ⁠1/2⁠(*p* − *p*∗).

The square root of the product of a quaternion with its conjugate is called its *norm* and is denoted ‖*q*‖ (Hamilton called this quantity the *tensor* of *q*, but this conflicts with the modern meaning of "tensor"). In formulas, this is expressed as follows:

$\lVert q\rVert ={\sqrt {qq^{*}}}={\sqrt {q^{*}q}}={\sqrt {a^{2}+b^{2}+c^{2}+d^{2}}}$

This is always a non-negative real number, and it is the same as the Euclidean norm on $\mathbb {H}$ considered as the vector space $\mathbb {R} ^{4}$ . Multiplying a quaternion by a real number scales its norm by the absolute value of the number. That is, if α is real, then

$\lVert \alpha q\rVert =\left|\alpha \right|\,\lVert q\rVert .$

This is a special case of the fact that the norm is *multiplicative*, meaning that

$\lVert pq\rVert =\lVert p\rVert \,\lVert q\rVert$

for any two quaternions p and q. Multiplicativity is a consequence of the formula for the conjugate of a product. Alternatively it follows from the identity

$\det {\begin{pmatrix}a+ib&id+c\\id-c&a-ib\end{pmatrix}}=a^{2}+b^{2}+c^{2}+d^{2},$

(where i denotes the usual imaginary unit) and hence from the multiplicative property of determinants of square matrices.

This norm makes it possible to define the **distance** *d*(*p*, *q*) between p and q as the norm of their difference:

$d(p,q)=\lVert p-q\rVert .$

This makes $\mathbb {H}$ a metric space. Addition and multiplication are continuous in regard to the associated metric topology. This follows with exactly the same proof as for the real numbers $\mathbb {R}$ from the fact that $\mathbb {H}$ is a normed algebra.

### Unit quaternion

A **unit quaternion** is a quaternion of norm one. Dividing a nonzero quaternion q by its norm produces a unit quaternion **U***q* called the *versor* of q:

$\mathbf {U} q={\frac {q}{\lVert q\rVert }}.$

Every nonzero quaternion has a unique polar decomposition $q=\lVert q\rVert \cdot \mathbf {U} q,$ while the zero quaternion can be formed from any unit quaternion.

Using conjugation and the norm makes it possible to define the reciprocal of a nonzero quaternion. The product of a quaternion with its reciprocal should equal 1, and the considerations above imply that the product of q and $q^{*}/\left\Vert q\right\|^{2}$ is 1 (for either order of multiplication). So the *reciprocal* of q is defined to be

$q^{-1}={\frac {q^{*}}{\lVert q\rVert ^{2}}}.$

Since the multiplication is non-commutative, the quotient quantities *p q*−1 or *q*−1*p* are different (except if p and q have parallel vector parts): the notation ⁠*p*/*q*⁠ is ambiguous and should not be used.


## Algebraic properties

The set $\mathbb {H}$ of all quaternions is a vector space over the real numbers with dimension 4. Multiplication of quaternions is associative and distributive over vector addition, but it is not commutative. Therefore, the quaternions, $\mathbb {H} ,$ are a non-commutative, associative algebra over the real numbers. Even though $\mathbb {H}$ embeds multiple *copies* of the complex numbers, it is not itself an *associative algebra* over the complex numbers.

Because it is possible to divide quaternions, they form a division algebra. This is a structure similar to a field except that it admits non-commutative multiplication. *Finite-dimensional associative division algebras* over the real numbers are very rare: The Frobenius theorem states that there are exactly three. Those are $\mathbb {R} ,$ $\mathbb {C} ,$ and $\mathbb {H} .$ The norm makes the quaternions into a *normed algebra*, and normed division algebras over the real numbers are also very rare: Hurwitz's theorem says that there are only four: $\mathbb {R} ,$ $\mathbb {C} ,$ $\mathbb {H} ,$ and $\mathbb {O}$ (the octonions). The quaternions are also an example of a composition algebra and of a unital Banach algebra.

Because the product of any two basis vectors is plus or minus another basis vector, the set {±1, ±**i**, ±**j**, ±**k**} forms a group under multiplication. This non-abelian group is called the quaternion group and is denoted Q8. The real group ring of Q8 is a ring $\mathbb {R} [\mathrm {Q} _{8}]$ which is also an eight-dimensional vector space over $\mathbb {R} .$ It has one basis vector for each element of $\mathrm {Q} _{8}.$ The quaternions are isomorphic to the quotient ring of $\mathbb {R} [\mathrm {Q} _{8}]$ by the ideal generated by the elements 1 + (−1), **i** + (−**i**), **j** + (−**j**), and **k** + (−**k**). Here the first term in each of the sums is one of the basis elements 1, **i**, **j**, and **k**, and the second term is one of basis elements −1, −**i**, −**j**, and −**k**, not the additive inverses of 1, **i**, **j**, and **k**.


## Quaternions and three-dimensional geometry

The vector part of a quaternion can be interpreted as a coordinate vector in $\mathbb {R} ^{3};$ therefore, the algebraic operations of the quaternions reflect the geometry of $\mathbb {R} ^{3}.$ Operations such as the vector dot and cross products can be defined in terms of quaternions, and this makes it possible to apply quaternion techniques wherever spatial vectors arise. A useful application of quaternions has been to interpolate the orientations of key-frames in computer graphics.

For the remainder of this section, **i**, **j**, and **k** will denote both the three imaginary basis vectors of $\mathbb {H}$ and a basis for $\mathbb {R} ^{3}.$ Replacing **i** by −**i**, **j** by −**j**, and **k** by −**k** sends a vector to its additive inverse, so the additive inverse of a vector is the same as its conjugate as a quaternion. For this reason, conjugation is sometimes called the *spatial inverse*.

For two vector quaternions *p* = *b*1**i** + *c*1**j** + *d*1**k** and *q* = *b*2**i** + *c*2**j** + *d*2**k** their dot product, by analogy to vectors in $\mathbb {R} ^{3},$ is

$p\cdot q=b_{1}b_{2}+c_{1}c_{2}+d_{1}d_{2}.$

It can also be expressed in a component-free manner as

$p\cdot q=\textstyle {\frac {1}{2}}(p^{*}q+q^{*}p)=\textstyle {\frac {1}{2}}(pq^{*}+qp^{*}).$

This is equal to the scalar parts of the products *pq*∗, *qp*∗, *p*∗*q*, and *q*∗*p*. Note that their vector parts are different.

The cross product of p and q relative to the orientation determined by the ordered basis **i**, **j**, and **k** is

$p\times q=(c_{1}d_{2}-d_{1}c_{2})\mathbf {i} +(d_{1}b_{2}-b_{1}d_{2})\mathbf {j} +(b_{1}c_{2}-c_{1}b_{2})\mathbf {k} .$

(Recall that the orientation is necessary to determine the sign.) This is equal to the vector part of the product *pq* (as quaternions), as well as the vector part of −*q*∗*p*∗. It also has the formula

$p\times q=\textstyle {\tfrac {1}{2}}(pq-qp).$

For the commutator, [*p*, *q*] = *pq* − *qp*, of two vector quaternions one obtains

$[p,q]=2p\times q,$

which gives the commutation relationship

$qp=pq-2p\times q.$

In general, let p and q be quaternions and write

${\begin{aligned}p&=p_{\text{s}}+p_{\text{v}},\\[5mu]q&=q_{\text{s}}+q_{\text{v}},\end{aligned}}$

where *p*s and *q*s are the scalar parts, and *p*v and *q*v are the vector parts of p and q. Then we have the formula

$pq=(pq)_{\text{s}}+(pq)_{\text{v}}=(p_{\text{s}}q_{\text{s}}-p_{\text{v}}\cdot q_{\text{v}})+(p_{\text{s}}q_{\text{v}}+q_{\text{s}}p_{\text{v}}+p_{\text{v}}\times q_{\text{v}}).$

This shows that the noncommutativity of quaternion multiplication comes from the multiplication of vector quaternions. It also shows that two quaternions commute if and only if their vector parts are collinear. Hamilton showed that this product computes the third vertex of a spherical triangle from two given vertices and their associated arc-lengths, which is also an algebra of points in Elliptic geometry.

Unit quaternions can be identified with rotations in $\mathbb {R} ^{3}$ and were called versors by Hamilton. Also see Quaternions and spatial rotation for more information about modeling three-dimensional rotations using quaternions.

See Hanson (2005) for visualization of quaternions.


## Matrix representations

Just as complex numbers can be represented as matrices, so can quaternions. There are at least two ways of representing quaternions as matrices in such a way that quaternion addition and multiplication correspond to matrix addition and matrix multiplication. One is to use 2 × 2 complex matrices, and the other is to use 4 × 4 real matrices. In each case, the representation given is one of a family of linearly related representations. These are injective homomorphisms from $\mathbb {H}$ to the matrix rings M(2,**C**) and M(4,**R**), respectively.

### Representation as complex 2 × 2 matrices

The quaternion *a* + *b* **i** + *c* **j** + *d* **k** can be represented using a complex 2 × 2 matrix as

${\begin{bmatrix}{\phantom {-}}a+bi&c+di\\-c+di&a-bi\end{bmatrix}}.$

This representation has the following properties:

- Constraining any two of b, c, and d to zero produces a representation of complex numbers. For example, setting *c* = *d* = 0 produces a diagonal complex matrix representation of complex numbers, and setting *b* = *d* = 0 produces a real matrix representation.
- The norm of a quaternion (the square root of the product with its conjugate, as with complex numbers) is the square root of the determinant of the corresponding matrix.
- The scalar part of a quaternion is one half of the matrix trace.
- The conjugate of a quaternion corresponds to the conjugate transpose of the matrix.
- By restriction this representation yields a group isomorphism between the subgroup of unit quaternions and their image SU(2). Topologically, the unit quaternions are the 3-sphere, so the underlying space of SU(2) is also a 3-sphere. The group SU(2) is important for describing spin in quantum mechanics; see Pauli matrices.
- There is a strong relation between quaternions and Pauli matrices. The 2 × 2 complex matrix above can be written as $a\,I+b\,i\,\sigma _{3}+c\,i\,\sigma _{2}+d\,i\,\sigma _{1},$ so in this representation the quaternion units {1, **i**, **j**, **k**} correspond to $\left\{I,i\,\sigma _{3},i\,\sigma _{2},i\,\sigma _{1}\right\}$ = $\left\{I,\sigma _{1}\,\sigma _{2},\sigma _{3}\,\sigma _{1},\sigma _{2}\,\sigma _{3}\right\}$ . Multiplying any two Pauli matrices always yields a quaternion unit matrix, all of them except for −1 . One obtains −1 via **i**2 = **j**2 = **k**2 = **i j k** = −1 ; e.g. the last equality is $\mathbf {i\;j\;k} =\sigma _{1}\,\sigma _{2}\,\sigma _{3}\,\sigma _{1}\,\sigma _{2}\,\sigma _{3}=-1.$

The representation in M(2,ℂ) is not unique: A different convention, that preserves the direction of cyclic ordering between the quaternions and the Pauli matrices, is to choose $1\mapsto \mathbf {I} ,\quad \mathbf {i} \mapsto -i\,\sigma _{1}=-\sigma _{2}\,\sigma _{3},\quad \mathbf {j} \mapsto -i\,\sigma _{2}=-\sigma _{3}\,\sigma _{1},\quad \mathbf {k} \mapsto -i\,\sigma _{3}=-\sigma _{1}\,\sigma _{2},$

This gives an alternative representation,

$a+b\,\mathbf {i} +c\,\mathbf {j} +d\,\mathbf {k} \mapsto {\begin{bmatrix}a-d\,i&-c-b\,i\\c-b\,i&{\phantom {-}}a+d\,i\end{bmatrix}}.$

### Representation as real 4 × 4 matrices

Using 4 × 4 real matrices, that same quaternion can be written as

${\begin{aligned}\left[{\begin{array}{rrrr}a&-b&-c&-d\\b&a&-d&c\\c&d&a&-b\\d&-c&b&a\end{array}}\right]&=a\left[{\begin{array}{rrrr}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{array}}\right]+b\left[{\begin{array}{rrrr}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{array}}\right]\\[10mu]&\qquad +c\left[{\begin{array}{rrrr}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{array}}\right]+d\left[{\begin{array}{rrrr}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{array}}\right].\end{aligned}}$

However, the representation of quaternions in M(4,ℝ) is not unique. For example, the same quaternion can also be represented as

${\begin{aligned}\left[{\begin{array}{rrrr}a&d&-b&-c\\-d&a&c&-b\\b&-c&a&-d\\c&b&d&a\end{array}}\right]&=a\left[{\begin{array}{rrrr}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{array}}\right]+b\left[{\begin{array}{rrrr}0&0&-1&0\\0&0&0&-1\\1&0&0&0\\0&1&0&0\end{array}}\right]\\[10mu]&\qquad +c\left[{\begin{array}{rrrr}0&0&0&-1\\0&0&1&0\\0&-1&0&0\\1&0&0&0\end{array}}\right]+d\left[{\begin{array}{rrrr}0&1&0&0\\-1&0&0&0\\0&0&0&-1\\0&0&1&0\end{array}}\right].\end{aligned}}$

There are 48 distinct matrix representations of this form, in which one of the matrices represents the scalar part and the other three are all skew-symmetric. More precisely, there are 48 sets of quadruples of matrices with these symmetry constraints, such that a function sending 1, **i**, **j**, and **k** to the matrices in the quadruple is a homomorphism, that is, it sends sums and products of quaternions to sums and products of matrices. In this representation, the conjugate of a quaternion corresponds to the transpose of the matrix. The fourth power of the norm of a quaternion is the determinant of the corresponding matrix. The scalar part of a quaternion is one quarter of the matrix trace. As with the 2 × 2 complex representation above, complex numbers can again be produced by constraining the coefficients suitably; for example, as block diagonal matrices with two 2 × 2 blocks by setting   *c* = *d* = 0 .

Each 4 × 4 matrix representation of quaternions corresponds to a multiplication table of unit quaternions. For example, the last matrix representation given above corresponds to the multiplication table

| ↓ × → | a | d | −b | −c |
|---|---|---|---|---|
| a | a | d | −b | −c |
| −d | −d | a | c | −b |
| b | b | −c | a | −d |
| c | c | b | d | a |

which is isomorphic, through $\{a\mapsto 1,\ b\mapsto i,\ c\mapsto j,\ d\mapsto k\},$ to

| ↓ × → | 1 | **k** | −**i** | −**j** |
|---|---|---|---|---|
| 1 | 1 | **k** | −**i** | −**j** |
| −**k** | −**k** | 1 | **j** | −**i** |
| **i** | **i** | −**j** | 1 | −**k** |
| **j** | **j** | **i** | **k** | 1 |

Constraining any such multiplication table to have the identity in the first row and column and for the signs of the row headers to be opposite to those of the column headers, then there are 3 possible choices for the second column (ignoring sign), 2 possible choices for the third column (ignoring sign), and 1 possible choice for the fourth column (ignoring sign); that makes 6 possibilities. Then, the second column can be chosen to be either positive or negative, the third column can be chosen to be positive or negative, and the fourth column can be chosen to be positive or negative, giving 8 possibilities for the sign. Multiplying the possibilities for the letter positions and for their signs yields 48. Then replacing 1 with a, **i** with b, **j** with c, and **k** with d and removing the row and column headers yields a matrix representation of *a* + *b* **i** + *c* **j** + *d* **k** .


## Lagrange's four-square theorem

Quaternions are also used in one of the proofs of Lagrange's four-square theorem in number theory, which states that every nonnegative integer is the sum of four integer squares. As well as being an elegant theorem in its own right, Lagrange's four square theorem has useful applications in areas of mathematics outside number theory, such as combinatorial design theory. The quaternion-based proof uses Hurwitz quaternions, a subring of the ring of all quaternions for which there is an analog of the Euclidean algorithm.


## Quaternions as pairs of complex numbers

Quaternions can be represented as pairs of complex numbers. From this perspective, quaternions are the result of applying the Cayley–Dickson construction to the complex numbers. This is a generalization of the construction of the complex numbers as pairs of real numbers.

Let $\mathbb {C} ^{2}$ be a two-dimensional vector space over the complex numbers. Choose a basis consisting of two elements 1 and **j**. A vector in $\mathbb {C} ^{2}$ can be written in terms of the basis elements 1 and **j** as

$(a+b\,i)1+(c+d\,i)\mathbf {j} .$

If we define **j**2 = −1 and *i* **j** = −**j** *i*, then we can multiply two vectors using the distributive law. Using **k** as an abbreviated notation for the product *i* **j** leads to the same rules for multiplication as the usual quaternions. Therefore, the above vector of complex numbers corresponds to the quaternion *a* + *b i* + *c* **j** + *d* **k**. If we write the elements of $\mathbb {C} ^{2}$ as ordered pairs and quaternions as quadruples, then the correspondence is

$(a+bi,\,c+di)\leftrightarrow (a,\,b,\,c,\,d).$


## Square roots

### Square roots of −1

In the complex numbers, $\mathbb {C} ,$ there are exactly two numbers, i and −*i*, that give −1 when squared. In $\mathbb {H}$ there are infinitely many square roots of minus one: the quaternion solution for the square root of −1 is the unit sphere in $\mathbb {R} ^{3}.$ To see this, let *q* = *a* + *b* **i** + *c* **j** + *d* **k** be a quaternion, and assume that its square is −1. In terms of a, b, c, and d, this means

${\begin{aligned}a^{2}-b^{2}-c^{2}-d^{2}&=-1,{\vphantom {x^{|}}}\\[3mu]2ab&=0,\\[3mu]2ac&=0,\\[3mu]2ad&=0.\end{aligned}}$

To satisfy the last three equations, either *a* = 0 or b, c, and d are all 0 . The latter is impossible because *a* is a real number and the first equation would imply that *a*2 = −1. Therefore, *a* = 0 and *b*2 + *c*2 + *d*2 = 1. In other words: A quaternion squares to −1 if and only if it is a vector quaternion with norm 1 . By definition, the set of all such vectors forms the unit sphere.

Only negative real quaternions have infinitely many square roots. All others have just two (or one in the case of 0).

#### As a union of complex planes

Each antipodal pair of square roots of −1 creates a distinct copy of the complex numbers inside the quaternions. If *q*2 = −1 , then the copy is the image of the function

$a+bi\mapsto a+bq.$

This is an injective ring homomorphism from $\mathbb {C}$ to $\mathbb {H} ,$ which defines a field isomorphism from $\mathbb {C}$ onto its image. The images of the embeddings corresponding to +q and −q are identical.

Every non-real quaternion generates a subalgebra of the quaternions that is isomorphic to $\mathbb {C}$ , and is thus a planar subspace of $\mathbb {H}$ : write q as the sum of its scalar part and its vector part: $q=q_{s}+{\vec {q}}_{v}.$

Decompose the vector part further as the product of its norm and its versor: $q=q_{s}+\lVert {\vec {q}}_{v}\rVert \cdot \mathbf {U} \,{\vec {q}}_{v}=q_{s}+\|{\vec {q}}_{v}\|\,{\frac {{\vec {q}}_{v}}{\|{\vec {q}}_{v}\|}}.$

(This is not the same as $q_{s}+\lVert q\rVert \cdot \mathbf {U} q.$ ) The versor of the vector part of q, $\mathbf {U} {\vec {q}}_{v},$ is a right versor with –1 as its square. A straightforward verification shows that $a+bi\mapsto a+b\mathbf {U} {\vec {q}}_{v}$ defines an injective homomorphism of normed algebras from $\mathbb {C}$ into the quaternions. Under this homomorphism, q is the image of the complex number $q_{s}+\lVert {\vec {q}}_{v}\rVert i.$

As $\mathbb {H}$ is the union of the images of all these homomorphisms, one can view the quaternions as a pencil of planes intersecting on the real line. Each of these complex planes contains exactly one pair of antipodal points of the sphere of square roots of minus one.

#### Commutative subrings

The relationship of quaternions to each other within the complex subplanes of $\mathbb {H}$ can also be identified and expressed in terms of commutative subrings. Specifically, since two quaternions p and q commute (i.e., *p q* = *q p*) only if they lie in the same complex subplane of $\mathbb {H} ,$ the profile of $\mathbb {H}$ as a union of complex planes arises when one seeks to find all commutative subrings of the quaternion ring.

### Square roots of arbitrary quaternions

Any quaternion $\mathbf {q} =(r,\,{\vec {v}})$ (represented here in scalar–vector representation) has at least one square root ${\sqrt {\mathbf {q} }}=(x,\,{\vec {y}})$ which solves the equation $({\sqrt {\mathbf {q} }})^{2}=(x,\,{\vec {y}})^{2}=\mathbf {q} .$ Looking at the scalar and vector parts in this equation separately yields two equations, which when solved gives the solutions

${\sqrt {\mathbf {q} }}={\sqrt {(r,\,{\vec {v}})}}=\pm \left({\sqrt {{\tfrac {1}{2}}{\bigl (}\|\mathbf {q} \|+r{\bigr )}}},\ {\frac {\vec {v}}{\|{\vec {v}}\|}}{\sqrt {{\tfrac {1}{2}}{\bigl (}\|\mathbf {q} \|-r{\bigr )}}}\right),$

where ${\textstyle \|{\vec {v}}\|={\sqrt {{\vec {v}}\cdot {\vec {v}}}}}$ is the norm of ${\vec {v}}$ and ${\textstyle \|\mathbf {q} \|={\sqrt {\mathbf {q} ^{*}\mathbf {q} }}={\sqrt {r^{2}+\|{\vec {v}}\|^{2}}}}$ is the norm of $\mathbf {q} .$ For any scalar quaternion $\mathbf {q}$ , this equation provides the correct square roots if ${\textstyle {\vec {v}}/\|{\vec {v}}\|}$ is interpreted as an arbitrary unit vector.

Therefore, nonzero, non-scalar quaternions, or positive scalar quaternions, have exactly two roots, while 0 has exactly one root (0), and negative scalar quaternions have infinitely many roots, which are the vector quaternions located on $\{0\}\times S^{2}{\bigl (}{\sqrt {-r}}{\bigr )}$ , i.e., where the scalar part is zero and the vector part is located on the 2-sphere with radius ${\sqrt {-r}}.$


## Functions of a quaternion variable

Like functions of a complex variable, functions of a quaternion variable suggest useful physical models. For example, the original electric and magnetic fields described by Maxwell were functions of a quaternion variable. Examples of other functions include the extension of the Mandelbrot set and Julia sets into 4-dimensional space.

### Exponential, logarithm, and power functions

A function of a quaternion can be defined from a power series with real coefficients. For example, given a quaternion,

$q=a+b\,\mathbf {i} +c\,\mathbf {j} +d\,\mathbf {k} =a+\mathbf {v} ,$

the exponential is computed as

$\exp(q)=\sum _{n=0}^{\infty }{\frac {q^{n}}{n!}}=e^{a}{\biggl (}{\cos \|\mathbf {v} \|}+{\frac {\mathbf {v} }{\|\mathbf {v} \|}}\sin \|\mathbf {v} \|{\biggr )},$

and the logarithm is

$\ln(q)=\ln \|q\|+{\frac {\mathbf {v} }{\|\mathbf {v} \|}}\arccos {\frac {a}{\|q\|}}.$

It follows that the polar decomposition of a quaternion may be written

$q=\|q\|e^{\varphi {\hat {n}}}=\|q\|{\bigl (}{\cos(\varphi )+{\hat {n}}\,\sin(\varphi )}{\bigr )},$

where the angle $\varphi$

$a=\|q\|\,\cos(\varphi )$

and the unit vector ${\hat {n}}$ is defined by:

$\mathbf {v} ={\hat {n}}\|\mathbf {v} \|={\hat {n}}\|q\|\,\sin(\varphi ).$

Any unit quaternion may be expressed in polar form as:

$q=\exp {({\hat {n}}\varphi )}.$

The power of a quaternion raised to an arbitrary (real) exponent x is given by:

$q^{x}=\|q\|^{x}e^{{\hat {n}}x\varphi }=\|q\|^{x}{\bigl (}\cos(x\varphi )+{\hat {n}}\sin(x\varphi ){\bigr )}.$

### Geodesic norm

The geodesic distance *d*g(*p*, *q*) between unit quaternions p and q is defined as:

$d_{\text{g}}(p,q)=\lVert \ln(p^{-1}q)\rVert .$

and amounts to the absolute value of half the angle subtended by p and q along a great arc of the S3 sphere. This angle can also be computed from the quaternion dot product without the logarithm as:

$d_{\text{g}}(p,q)={\arccos }{\bigl (}2(p\cdot q)^{2}-1{\bigr )}.$


## Three-dimensional and four-dimensional rotation groups

The word "conjugation", besides the meaning given above, can also mean taking an element a to *r a r*−1 where r is some nonzero quaternion. All elements that are conjugate to a given element (in this sense of the word conjugate) have the same real part and the same norm of the vector part. (Thus the conjugate in the other sense is one of the conjugates in this sense.)

Thus the multiplicative group of nonzero quaternions acts by conjugation on the copy of $\mathbb {R} ^{3}$ consisting of quaternions with real part equal to zero. Conjugation by a unit quaternion (a quaternion of absolute value 1) with real part cos(*φ*) is a rotation by an angle 2*φ*, the axis of the rotation being the direction of the vector part. The advantages of quaternions are:

- Avoiding gimbal lock, a problem with systems such as Euler angles.
- Faster and more compact than matrices.
- Nonsingular representation (compared with Euler angles for example).
- Pairs of unit quaternions represent a rotation in 4D space (see *Rotations in 4-dimensional Euclidean space: Algebra of 4D rotations*).

The set of all unit quaternions (versors) forms a 3-sphere *S*3 and a group (a Lie group) under multiplication, double covering the group ${\text{SO}}(3,\mathbb {R} )$ of real orthogonal 3×3 matrices of determinant 1 since *two* unit quaternions correspond to every rotation under the above correspondence. See plate trick.

The image of a subgroup of versors is a point group, and conversely, the preimage of a point group is a subgroup of versors. The preimage of a finite point group is called by the same name, with the prefix **binary**. For instance, the preimage of the icosahedral group is the binary icosahedral group.

The versors' group is isomorphic to SU(2), the group of complex unitary 2 × 2 matrices of determinant 1.

Let A be the set of quaternions of the form *a* + *b* **i** + *c* **j** + *d* **k** where a, b, c, and d are either all integers or all half-integers. The set A is a ring (in fact a domain) and a lattice and is called the ring of Hurwitz quaternions. There are 24 unit quaternions in this ring, and they are the vertices of a regular 24 cell with Schläfli symbol  {3,4,3} . They correspond to the double cover of the rotational symmetry group of the regular tetrahedron. Similarly, the vertices of a regular 600 cell with Schläfli symbol  {3,3,5}  can be taken as the unit icosians, corresponding to the double cover of the rotational symmetry group of the regular icosahedron. The double cover of the rotational symmetry group of the regular octahedron corresponds to the quaternions that represent the vertices of the disphenoidal 288-cell.


## Quaternion algebras

The Quaternions can be generalized into further algebras called *quaternion algebras*. Take F to be any field with characteristic different from 2, and a and b to be elements of F; a four-dimensional unitary associative algebra can be defined over F with basis 1, **i**, **j**, and **i j**, where **i**2 = *a*, **j**2 = *b* and **i j** = −**j i** (so **(i j)**2 = −*a b*).

Quaternion algebras are isomorphic to the algebra of 2×2 matrices over F or form division algebras over F, depending on the choice of a and b.
