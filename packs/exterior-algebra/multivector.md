---
title: "Multivector"
source: https://en.wikipedia.org/wiki/Multivector
domain: exterior-algebra
license: CC-BY-SA-4.0
tags: exterior algebra, differential form, wedge product, exterior derivative
fetched: 2026-07-02
---

# Multivector

In multilinear algebra, a **multivector**, sometimes called **Clifford number** or **multor**, is an element of the exterior algebra Λ(*V*) of a vector space V. This algebra is graded, associative and alternating, and consists of linear combinations of **simple** *k*-vectors (also known as **decomposable** *k*-vectors or *k*-blades) of the form

$v_{1}\wedge \cdots \wedge v_{k},$

where $v_{1},\ldots ,v_{k}$ are in V.

A ***k*-vector** is such a linear combination that is *homogeneous* of degree k (all terms are *k*-blades for the same k). Depending on the authors, a "multivector" may be either a *k*-vector or any element of the exterior algebra (any linear combination of *k*-blades with potentially differing values of *k*).

In differential geometry, a *k*-vector is usually a vector in the exterior algebra of the tangent vector space of a smooth manifold; that is, it is an antisymmetric tensor obtained by taking linear combinations of the exterior product of *k* tangent vectors, for some integer *k* ≥ 0. A differential *k*-form is a *k*-vector in the exterior algebra of the dual of the tangent space, which is also the dual of the exterior algebra of the tangent space.

For *k* = 0, 1, 2 and 3, *k*-vectors are often called respectively *scalars*, *vectors*, *bivectors* and *trivectors*; they are respectively dual to 0-forms, 1-forms, 2-forms and 3-forms.

## Exterior product

The exterior product (also called the wedge product) used to construct multivectors is multilinear (linear in each input), associative and alternating. This means for vectors **u**, **v** and **w** in a vector space *V* and for scalars *α*, *β*, the exterior product has the properties:

- Linear in an input: $\mathbf {u} \wedge (\alpha \mathbf {v} +\beta \mathbf {w} )=\alpha \mathbf {u} \wedge \mathbf {v} +\beta \mathbf {u} \wedge \mathbf {w} ;$
- Associative: $(\mathbf {u} \wedge \mathbf {v} )\wedge \mathbf {w} =\mathbf {u} \wedge (\mathbf {v} \wedge \mathbf {w} );$
- Alternating: $\mathbf {u} \wedge \mathbf {u} =0.$

The exterior product of *k* vectors or a sum of such products (for a single *k*) is called a grade *k* multivector, or a *k*-vector. The maximum grade of a multivector is the dimension of the vector space *V*.

Linearity in either input together with the alternating property implies linearity in the other input. The multilinearity of the exterior product allows a multivector to be expressed as a linear combination of exterior products of basis vectors of *V*. The exterior product of *k* basis vectors of *V* is the standard way of constructing each basis element for the space of *k*-vectors, which has dimension (*n* *k*) in the exterior algebra of an *n*-dimensional vector space.

## Area and volume

The *k*-vector obtained from the exterior product of *k* separate vectors in an *n*-dimensional space has components that define the projected (*k* − 1)-volumes of the *k*-parallelotope spanned by the vectors. The square root of the sum of the squares of these components defines the volume of the *k*-parallelotope.

The following examples show that a bivector in two dimensions measures the area of a parallelogram, and the magnitude of a bivector in three dimensions also measures the area of a parallelogram. Similarly, a three-vector in three dimensions measures the volume of a parallelepiped.

It is easy to check that the magnitude of a three-vector in four dimensions measures the volume of the parallelepiped spanned by these vectors.

### Multivectors in R2

Properties of multivectors can be seen by considering the two-dimensional vector space *V* = **R**2. Let the basis vectors be **e**1 and **e**2, so **u** and **v** are given by

$\mathbf {u} =u_{1}\mathbf {e} _{1}+u_{2}\mathbf {e} _{2},\quad \mathbf {v} =v_{1}\mathbf {e} _{1}+v_{2}\mathbf {e} _{2},$

and the multivector **u** ∧ **v**, also called a bivector, is computed to be

$\mathbf {u} \wedge \mathbf {v} \ =\ {\begin{vmatrix}u_{1}&v_{1}\\u_{2}&v_{2}\end{vmatrix}}\ (\mathbf {e} _{1}\wedge \mathbf {e} _{2}).$

The vertical bars denote the determinant of the matrix, which is the area of the parallelogram spanned by the vectors **u** and **v**. The magnitude of **u** ∧ **v** is the area of this parallelogram. Notice that because *V* has dimension two the basis bivector **e**1 ∧ **e**2 is the only multivector in Λ*V*.

The relationship between the magnitude of a multivector and the area or volume spanned by the vectors is an important feature in all dimensions. Furthermore, the linear functional version of a multivector that computes this volume is known as a differential form.

### Multivectors in R3

More features of multivectors can be seen by considering the three-dimensional vector space *V* = **R**3. In this case, let the basis vectors be **e**1, **e**2, and **e**3, so **u**, **v** and **w** are given by

${\begin{aligned}\mathbf {u} &=u_{1}\mathbf {e} _{1}+u_{2}\mathbf {e} _{2}+u_{3}\mathbf {e} _{3},&\mathbf {v} &=v_{1}\mathbf {e} _{1}+v_{2}\mathbf {e} _{2}+v_{3}\mathbf {e} _{3},&\mathbf {w} &=w_{1}\mathbf {e} _{1}+w_{2}\mathbf {e} _{2}+w_{3}\mathbf {e} _{3},\end{aligned}}$

and the bivector **u** ∧ **v** is computed to be

$\mathbf {u} \wedge \mathbf {v} \ =\ {\begin{vmatrix}u_{2}&v_{2}\\u_{3}&v_{3}\end{vmatrix}}\left(\mathbf {e} _{2}\wedge \mathbf {e} _{3}\right)+{\begin{vmatrix}u_{1}&v_{1}\\u_{3}&v_{3}\end{vmatrix}}\left(\mathbf {e} _{1}\wedge \mathbf {e} _{3}\right)+{\begin{vmatrix}u_{1}&v_{1}\\u_{2}&v_{2}\end{vmatrix}}\left(\mathbf {e} _{1}\wedge \mathbf {e} _{2}\right).$

The components of this bivector are the same as the components of the cross product. The magnitude of this bivector is the square root of the sum of the squares of its components.

This shows that the magnitude of the bivector **u** ∧ **v** is the area of the parallelogram spanned by the vectors **u** and **v** as it lies in the three-dimensional space *V*. The components of the bivector are the projected areas of the parallelogram on each of the three coordinate planes.

Notice that because *V* has dimension three, there is one basis three-vector in Λ*V*. Compute the three-vector

$\mathbf {u} \wedge \mathbf {v} \wedge \mathbf {w} \ =\ {\begin{vmatrix}u_{1}&v_{1}&w_{1}\\u_{2}&v_{2}&w_{2}\\u_{3}&v_{3}&w_{3}\end{vmatrix}}\left(\mathbf {e} _{1}\wedge \mathbf {e} _{2}\wedge \mathbf {e} _{3}\right).$

| Derivation of triple exterior product |
|---|
| ${\begin{aligned}&\mathbf {u} \wedge \mathbf {v} \wedge \mathbf {w} =(\mathbf {u} \wedge \mathbf {v} )\wedge \mathbf {w} \\{}={}&\left({\begin{vmatrix}u_{2}&v_{2}\\u_{3}&v_{3}\end{vmatrix}}\left(\mathbf {e} _{2}\wedge \mathbf {e} _{3}\right)+{\begin{vmatrix}u_{1}&v_{1}\\u_{3}&v_{3}\end{vmatrix}}\left(\mathbf {e} _{1}\wedge \mathbf {e} _{3}\right)+{\begin{vmatrix}u_{1}&v_{1}\\u_{2}&v_{2}\end{vmatrix}}\left(\mathbf {e} _{1}\wedge \mathbf {e} _{2}\right)\right)\wedge \left(w_{1}\mathbf {e} _{1}+w_{2}\mathbf {e} _{2}+w_{3}\mathbf {e} _{3}\right)\\{}={}&{\begin{vmatrix}u_{2}&v_{2}\\u_{3}&v_{3}\end{vmatrix}}\left(\mathbf {e} _{2}\wedge \mathbf {e} _{3}\right)\wedge \left(w_{1}\mathbf {e} _{1}+w_{2}\mathbf {e} _{2}+w_{3}\mathbf {e} _{3}\right)\\&{}+{\begin{vmatrix}u_{1}&v_{1}\\u_{3}&v_{3}\end{vmatrix}}\left(\mathbf {e} _{1}\wedge \mathbf {e} _{3}\right)\wedge \left(w_{1}\mathbf {e} _{1}+w_{2}\mathbf {e} _{2}+w_{3}\mathbf {e} _{3}\right)\\&{}+{\begin{vmatrix}u_{1}&v_{1}\\u_{2}&v_{2}\end{vmatrix}}\left(\mathbf {e} _{1}\wedge \mathbf {e} _{2}\right)\wedge \left(w_{1}\mathbf {e} _{1}+w_{2}\mathbf {e} _{2}+w_{3}\mathbf {e} _{3}\right)\\{}={}&{\begin{vmatrix}u_{2}&v_{2}\\u_{3}&v_{3}\end{vmatrix}}\left(\mathbf {e} _{2}\wedge \mathbf {e} _{3}\right)\wedge w_{1}\mathbf {e} _{1}+{\cancel {{\begin{vmatrix}u_{2}&v_{2}\\u_{3}&v_{3}\end{vmatrix}}\left(\mathbf {e} _{2}\wedge \mathbf {e} _{3}\right)\wedge w_{2}\mathbf {e} _{2}}}+{\cancel {{\begin{vmatrix}u_{2}&v_{2}\\u_{3}&v_{3}\end{vmatrix}}\left(\mathbf {e} _{2}\wedge \mathbf {e} _{3}\right)\wedge w_{3}\mathbf {e} _{3}}}&&\mathbf {e} _{2}\wedge \mathbf {e} _{2}=0;\mathbf {e} _{3}\wedge \mathbf {e} _{3}=0\\&{}+{\cancel {{\begin{vmatrix}u_{1}&v_{1}\\u_{3}&v_{3}\end{vmatrix}}\left(\mathbf {e} _{1}\wedge \mathbf {e} _{3}\right)\wedge w_{1}\mathbf {e} _{1}}}+{\begin{vmatrix}u_{1}&v_{1}\\u_{3}&v_{3}\end{vmatrix}}\left(\mathbf {e} _{1}\wedge \mathbf {e} _{3}\right)\wedge w_{2}\mathbf {e} _{2}+{\cancel {{\begin{vmatrix}u_{1}&v_{1}\\u_{3}&v_{3}\end{vmatrix}}\left(\mathbf {e} _{1}\wedge \mathbf {e} _{3}\right)\wedge w_{3}\mathbf {e} _{3}}}&&\mathbf {e} _{1}\wedge \mathbf {e} _{1}=0;\mathbf {e} _{3}\wedge \mathbf {e} _{3}=0\\&{}+{\cancel {{\begin{vmatrix}u_{1}&v_{1}\\u_{2}&v_{2}\end{vmatrix}}\left(\mathbf {e} _{1}\wedge \mathbf {e} _{2}\right)\wedge w_{1}\mathbf {e} _{1}}}+{\cancel {{\begin{vmatrix}u_{1}&v_{1}\\u_{2}&v_{2}\end{vmatrix}}\left(\mathbf {e} _{1}\wedge \mathbf {e} _{2}\right)\wedge w_{2}\mathbf {e} _{2}}}+{\begin{vmatrix}u_{1}&v_{1}\\u_{2}&v_{2}\end{vmatrix}}\left(\mathbf {e} _{1}\wedge \mathbf {e} _{2}\right)\wedge w_{3}\mathbf {e} _{3}&&\mathbf {e} _{1}\wedge \mathbf {e} _{1}=0;\mathbf {e} _{2}\wedge \mathbf {e} _{2}=0\\{}={}&{\begin{vmatrix}u_{2}&v_{2}\\u_{3}&v_{3}\end{vmatrix}}\left(\mathbf {e} _{2}\wedge \mathbf {e} _{3}\right)\wedge w_{1}\mathbf {e} _{1}+{\begin{vmatrix}u_{1}&v_{1}\\u_{3}&v_{3}\end{vmatrix}}\left(\mathbf {e} _{1}\wedge \mathbf {e} _{3}\right)\wedge w_{2}\mathbf {e} _{2}+{\begin{vmatrix}u_{1}&v_{1}\\u_{2}&v_{2}\end{vmatrix}}\left(\mathbf {e} _{1}\wedge \mathbf {e} _{2}\right)\wedge w_{3}\mathbf {e} _{3}\\{}={}&-w_{1}{\begin{vmatrix}u_{2}&v_{2}\\u_{3}&v_{3}\end{vmatrix}}\left(\mathbf {e} _{2}\wedge \mathbf {e} _{1}\wedge \mathbf {e} _{3}\right)-w_{2}{\begin{vmatrix}u_{1}&v_{1}\\u_{3}&v_{3}\end{vmatrix}}\left(\mathbf {e} _{1}\wedge \mathbf {e} _{2}\wedge \mathbf {e} _{3}\right)+w_{3}{\begin{vmatrix}u_{1}&v_{1}\\u_{2}&v_{2}\end{vmatrix}}\left(\mathbf {e} _{1}\wedge \mathbf {e} _{2}\wedge \mathbf {e} _{3}\right)\\{}={}&w_{1}{\begin{vmatrix}u_{2}&v_{2}\\u_{3}&v_{3}\end{vmatrix}}\left(\mathbf {e} _{1}\wedge \mathbf {e} _{2}\wedge \mathbf {e} _{3}\right)-w_{2}{\begin{vmatrix}u_{1}&v_{1}\\u_{3}&v_{3}\end{vmatrix}}\left(\mathbf {e} _{1}\wedge \mathbf {e} _{2}\wedge \mathbf {e} _{3}\right)+w_{3}{\begin{vmatrix}u_{1}&v_{1}\\u_{2}&v_{2}\end{vmatrix}}\left(\mathbf {e} _{1}\wedge \mathbf {e} _{2}\wedge \mathbf {e} _{3}\right)\\{}={}&\left(w_{1}{\begin{vmatrix}u_{2}&v_{2}\\u_{3}&v_{3}\end{vmatrix}}-w_{2}{\begin{vmatrix}u_{1}&v_{1}\\u_{3}&v_{3}\end{vmatrix}}+w_{3}{\begin{vmatrix}u_{1}&v_{1}\\u_{2}&v_{2}\end{vmatrix}}\right)\left(\mathbf {e} _{1}\wedge \mathbf {e} _{2}\wedge \mathbf {e} _{3}\right)\\{}={}&{\begin{vmatrix}u_{1}&v_{1}&w_{1}\\u_{2}&v_{2}&w_{2}\\u_{3}&v_{3}&w_{3}\end{vmatrix}}\left(\mathbf {e} _{1}\wedge \mathbf {e} _{2}\wedge \mathbf {e} _{3}\right)\\\end{aligned}}$ |

This shows that the magnitude of the three-vector **u** ∧ **v** ∧ **w** is the volume of the parallelepiped spanned by the three vectors **u**, **v** and **w**.

In higher-dimensional spaces, the component three-vectors are projections of the volume of a parallelepiped onto the coordinate three-spaces, and the magnitude of the three-vector is the volume of the parallelepiped as it sits in the higher-dimensional space.

## Grassmann coordinates

In this section, we consider multivectors on a projective space *P**n*, which provide a convenient set of coordinates for lines, planes and hyperplanes that have properties similar to the homogeneous coordinates of points, called Grassmann coordinates.

Points in a real projective space *P**n* are defined to be lines through the origin of the vector space **R***n*+1. For example, the projective plane *P*2 is the set of lines through the origin of **R**3. Thus, multivectors defined on **R***n*+1 can be viewed as multivectors on *P**n*.

A convenient way to view a multivector on *P**n* is to examine it in an affine component of *P**n*, which is the intersection of the lines through the origin of **R***n*+1 with a selected hyperplane, such as H: *x**n*+1 = 1. Lines through the origin of **R**3 intersect the plane E: *z* = 1 to define an affine version of the projective plane that only lacks the points for which *z* = 0, called the points at infinity.

### Multivectors on the projective plane *P*2

Points in the affine component E: *z* = 1 of the projective plane **P**2 have coordinates **x** = (*x*, *y*, 1). A linear combination of two points **p** = (*p*1, *p*2, 1) and **q** = (*q*1, *q*2, 1) defines a plane in **R**3 that intersects E in the line joining **p** and **q**. The multivector **p** ∧ **q** defines a parallelogram in **R**3 given by

$\mathbf {p} \wedge \mathbf {q} \ =\ (p_{2}-q_{2})(\mathbf {e} _{2}\wedge \mathbf {e} _{3})+(p_{1}-q_{1})(\mathbf {e} _{1}\wedge \mathbf {e} _{3})+(p_{1}q_{2}-q_{1}p_{2})(\mathbf {e} _{1}\wedge \mathbf {e} _{2}).$

Notice that substitution of *α***p** + *β***q** for **p** multiplies this multivector by a constant. Therefore, the components of **p** ∧ **q** are homogeneous coordinates for the plane through the origin of **R**3.

The set of points **x** = (*x*, *y*, 1) on the line through **p** and **q** is the intersection of the plane defined by **p** ∧ **q** with the plane E: *z* = 1. These points satisfy **x** ∧ **p** ∧ **q** = 0, that is,

$\mathbf {x} \wedge \mathbf {p} \wedge \mathbf {q} \ =\ (x\mathbf {e} _{1}+y\mathbf {e} _{2}+\mathbf {e} _{3})\wedge {\big (}(p_{2}-q_{2})(\mathbf {e} _{2}\wedge \mathbf {e} _{3})+(p_{1}-q_{1})(\mathbf {e} _{1}\wedge \mathbf {e} _{3})+(p_{1}q_{2}-q_{1}p_{2})(\mathbf {e} _{1}\wedge \mathbf {e} _{2}){\big )}=0,$

which simplifies to the equation of a line

$\lambda :x(p_{2}-q_{2})+y(p_{1}-q_{1})+(p_{1}q_{2}-q_{1}p_{2})=0.$

This equation is satisfied by points **x** = *α***p** + *β***q** for real values of α and β.

The three components of **p** ∧ **q** that define the line *λ* are called the Grassmann coordinates of the line. Because three homogeneous coordinates define both a point and a line, the geometry of points is said to be dual to the geometry of lines in the projective plane. This is called the principle of duality.

### Multivectors on projective 3-space *P*3

Three-dimensional projective space *P*3 consists of all lines through the origin of **R**4. Let the three-dimensional hyperplane, H: *w* = 1, be the affine component of projective space defined by the points **x** = (*x*, *y*, *z*, 1). The multivector **p** ∧ **q** ∧ **r** defines a parallelepiped in **R**4 given by

$\mathbf {p} \wedge \mathbf {q} \wedge \mathbf {r} ={\begin{vmatrix}p_{2}&q_{2}&r_{2}\\p_{3}&q_{3}&r_{3}\\1&1&1\end{vmatrix}}\mathbf {e} _{2}\wedge \mathbf {e} _{3}\wedge \mathbf {e} _{4}+{\begin{vmatrix}p_{1}&q_{1}&r_{1}\\p_{3}&q_{3}&r_{3}\\1&1&1\end{vmatrix}}\mathbf {e} _{1}\wedge \mathbf {e} _{3}\wedge \mathbf {e} _{4}+{\begin{vmatrix}p_{1}&q_{1}&r_{1}\\p_{2}&q_{2}&r_{2}\\1&1&1\end{vmatrix}}\mathbf {e} _{1}\wedge \mathbf {e} _{2}\wedge \mathbf {e} _{4}+{\begin{vmatrix}p_{1}&q_{1}&r_{1}\\p_{2}&q_{2}&r_{2}\\p_{3}&q_{3}&r_{3}\end{vmatrix}}\mathbf {e} _{1}\wedge \mathbf {e} _{2}\wedge \mathbf {e} _{3}.$

Notice that substitution of α**p** + β**q** + γ**r** for **p** multiplies this multivector by a constant. Therefore, the components of **p** ∧ **q** ∧ **r** are homogeneous coordinates for the 3-space through the origin of **R**4.

A plane in the affine component H: *w* = 1 is the set of points **x** = (*x*, *y*, *z*, 1) in the intersection of H with the 3-space defined by **p** ∧ **q** ∧ **r**. These points satisfy **x** ∧ **p** ∧ **q** ∧ **r** = 0, that is,

$\mathbf {x} \wedge \mathbf {p} \wedge \mathbf {q} \wedge \mathbf {r} =(x\mathbf {e} _{1}+y\mathbf {e} _{2}+z\mathbf {e} _{3}+\mathbf {e} _{4})\wedge \mathbf {p} \wedge \mathbf {q} \wedge \mathbf {r} =0,$

which simplifies to the equation of a plane

$\lambda :x{\begin{vmatrix}p_{2}&q_{2}&r_{2}\\p_{3}&q_{3}&r_{3}\\1&1&1\end{vmatrix}}+y{\begin{vmatrix}p_{1}&q_{1}&r_{1}\\p_{3}&q_{3}&r_{3}\\1&1&1\end{vmatrix}}+z{\begin{vmatrix}p_{1}&q_{1}&r_{1}\\p_{2}&q_{2}&r_{2}\\1&1&1\end{vmatrix}}+{\begin{vmatrix}p_{1}&q_{1}&r_{1}\\p_{2}&q_{2}&r_{2}\\p_{3}&q_{3}&r_{3}\end{vmatrix}}=0.$

This equation is satisfied by points **x** = *α***p** + *β***q** + *γ***r** for real values of *α*, *β* and *γ*.

The four components of **p** ∧ **q** ∧ **r** that define the plane *λ* are called the Grassmann coordinates of the plane. Because four homogeneous coordinates define both a point and a plane in projective space, the geometry of points is dual to the geometry of planes.

**A line as the join of two points:** In projective space the line *λ* through two points **p** and **q** can be viewed as the intersection of the affine space H: *w* = 1 with the plane **x** = *α***p** + *β***q** in **R**4. The multivector **p** ∧ **q** provides homogeneous coordinates for the line

${\begin{aligned}\lambda :\mathbf {p} \wedge \mathbf {q} &=(p_{1}\mathbf {e} _{1}+p_{2}\mathbf {e} _{2}+p_{3}\mathbf {e} _{3}+\mathbf {e} _{4})\wedge (q_{1}\mathbf {e} _{1}+q_{2}\mathbf {e} _{2}+q_{3}\mathbf {e} _{3}+\mathbf {e} _{4}),\\&={\begin{vmatrix}p_{1}&q_{1}\\1&1\end{vmatrix}}\mathbf {e} _{1}\wedge \mathbf {e} _{4}+{\begin{vmatrix}p_{2}&q_{2}\\1&1\end{vmatrix}}\mathbf {e} _{2}\wedge \mathbf {e} _{4}+{\begin{vmatrix}p_{3}&q_{3}\\1&1\end{vmatrix}}\mathbf {e} _{3}\wedge \mathbf {e} _{4}\\&+{\begin{vmatrix}p_{2}&q_{2}\\p_{3}&q_{3}\end{vmatrix}}\mathbf {e} _{2}\wedge \mathbf {e} _{3}+{\begin{vmatrix}p_{3}&q_{3}\\p_{1}&q_{1}\end{vmatrix}}\mathbf {e} _{3}\wedge \mathbf {e} _{1}+{\begin{vmatrix}p_{1}&q_{1}\\p_{2}&q_{2}\end{vmatrix}}\mathbf {e} _{1}\wedge \mathbf {e} _{2}.\end{aligned}}$

These are known as the Plücker coordinates of the line, though they are also an example of Grassmann coordinates.

**A line as the intersection of two planes:** A line *μ* in projective space can also be defined as the set of points **x** that form the intersection of two planes *π* and *ρ* defined by grade three multivectors, so the points **x** are the solutions to the linear equations

$\mu :\mathbf {x} \wedge \pi =0,\mathbf {x} \wedge \rho =0.$

In order to obtain the Plucker coordinates of the line *μ*, map the multivectors *π* and *ρ* to their dual point coordinates using the right complement, denoted by an overline, as in

$\mathbf {e} _{1}={\overline {\mathbf {e} _{2}\wedge \mathbf {e} _{3}\wedge \mathbf {e} _{4}}},\quad \mathbf {e} _{2}={\overline {\mathbf {e} _{3}\wedge \mathbf {e} _{1}\wedge \mathbf {e} _{4}}},\quad \mathbf {e} _{3}={\overline {\mathbf {e} _{1}\wedge \mathbf {e} _{2}\wedge \mathbf {e} _{4}}},\quad \mathbf {e} _{4}={\overline {\mathbf {e} _{1}\wedge \mathbf {e} _{2}\wedge \mathbf {e} _{3}}},$

then

${\overline {\pi }}=\pi _{1}\mathbf {e} _{1}+\pi _{2}\mathbf {e} _{2}+\pi _{3}\mathbf {e} _{3}+\pi _{4}\mathbf {e} _{4},\quad {\overline {\rho }}=\rho _{1}\mathbf {e} _{1}+\rho _{2}\mathbf {e} _{2}+\rho _{3}\mathbf {e} _{3}+\rho _{4}\mathbf {e} _{4}.$

So, the Plücker coordinates of the line *μ* are given by

${\begin{aligned}\mu :{\underline {{\overline {\pi }}\wedge {\overline {\rho }}}}&={\begin{vmatrix}\pi _{1}&\rho _{1}\\\pi _{4}&\rho _{4}\end{vmatrix}}\mathbf {e} _{2}\wedge \mathbf {e} _{3}+{\begin{vmatrix}\pi _{2}&\rho _{2}\\\pi _{4}&\rho _{4}\end{vmatrix}}\mathbf {e} _{3}\wedge \mathbf {e} _{1}+{\begin{vmatrix}\pi _{3}&\rho _{3}\\\pi _{4}&\rho _{4}\end{vmatrix}}\mathbf {e} _{1}\wedge \mathbf {e} _{2}\\&+{\begin{vmatrix}\pi _{2}&\rho _{2}\\\pi _{3}&\rho _{3}\end{vmatrix}}\mathbf {e} _{1}\wedge \mathbf {e} _{4}+{\begin{vmatrix}\pi _{3}&\rho _{3}\\\pi _{1}&\rho _{1}\end{vmatrix}}\mathbf {e} _{2}\wedge \mathbf {e} _{4}+{\begin{vmatrix}\pi _{1}&\rho _{1}\\\pi _{2}&\rho _{2}\end{vmatrix}}\mathbf {e} _{3}\wedge \mathbf {e} _{4},\end{aligned}}$

where the underline denotes the left complement. The left complement of the wedge product of right complements is called the antiwedge product, denoted by a downward pointing wedge, allowing us to write $\mu =\pi \vee \rho .$

## Clifford product

W. K. Clifford combined multivectors with the inner product defined on the vector space, in order to obtain a general construction for hypercomplex numbers that includes the usual complex numbers and Hamilton's quaternions.

The Clifford product between two vectors **u** and **v** is bilinear and associative like the exterior product, and has the additional property that the multivector **uv** is coupled to the inner product **u** ⋅ **v** by Clifford's relation,

$\mathbf {u} \mathbf {v} +\mathbf {v} \mathbf {u} =2\mathbf {u} \cdot \mathbf {v} .$

Clifford's relation retains the anticommuting property for vectors that are perpendicular. This can be seen from the mutually orthogonal unit vectors **e***i*, *i* = 1, ..., *n* in **R***n*: Clifford's relation yields

$\mathbf {e} _{i}\mathbf {e} _{j}+\mathbf {e} _{j}\mathbf {e} _{i}=2\mathbf {e} _{i}\cdot \mathbf {e} _{j}=\delta _{i,j},$

which shows that the basis vectors mutually anticommute,

$\mathbf {e} _{i}\mathbf {e} _{j}=-\mathbf {e} _{j}\mathbf {e} _{i},\quad i\neq j=1,\ldots ,n.$

In contrast to the exterior product, the Clifford product of a vector with itself is not zero. To see this, compute the product

$\mathbf {e} _{i}\mathbf {e} _{i}+\mathbf {e} _{i}\mathbf {e} _{i}=2\mathbf {e} _{i}\cdot \mathbf {e} _{i}=2,$

which yields

$\mathbf {e} _{i}\mathbf {e} _{i}=1,\quad i=1,\ldots ,n.$

The set of multivectors constructed using Clifford's product yields an associative algebra known as a Clifford algebra. Inner products with different properties can be used to construct different Clifford algebras.

## Geometric algebra

The term *k-blade* was used in *Clifford Algebra to Geometric Calculus* (1984)

Multivectors play a central role in the mathematical formulation of physics known as geometric algebra. According to David Hestenes,

[Non-scalar]

k

-vectors are sometimes called

k-blades

or, merely

blades

, to emphasize the fact that, in contrast to 0-vectors (scalars), they have "directional properties".

In 2003 the term *blade* for a multivector that can be written as the exterior product of [a scalar and] a set of vectors was used by C. Doran and A. Lasenby. Here, by the statement "Any multivector can be expressed as the sum of blades", scalars are implicitly defined as 0-blades.

In geometric algebra, a multivector is defined to be the sum of different-grade *k*-blades, such as the summation of a scalar, a vector, and a 2-vector. A sum of only *k*-grade components is called a *k*-vector, or a *homogeneous* multivector.

The highest grade element in a space is called a *pseudoscalar*.

If a given element is homogeneous of a grade *k*, then it is a *k*-vector, but not necessarily a *k*-blade. Such an element is a *k*-blade when it can be expressed as the exterior product of *k* vectors. A geometric algebra generated by a four-dimensional vector space illustrates the point with an example: The sum of any two blades with one taken from the XY-plane and the other taken from the ZW-plane will form a 2-vector that is not a 2-blade. In a geometric algebra generated by a vector space of dimension 2 or 3, all sums of 2-blades may be written as a single 2-blade.

### Examples

Orientation defined by an ordered set of vectors.

Reversed orientation corresponds to negating the exterior product.

Geometric interpretation of grade

n

elements in a real exterior algebra for

n

= 0

(signed point), 1 (directed line segment, or vector), 2 (oriented plane element), 3 (oriented volume). The exterior product of

n

vectors can be visualized as any

n

-dimensional shape (e.g.

n

-

parallelotope

,

n

-

ellipsoid

); with magnitude (

hypervolume

), and

orientation

defined by that on its

(

n

− 1)

-dimensional boundary and on which side the interior is.

- 0-vectors are scalars;
- 1-vectors are vectors;
- 2-vectors are bivectors;
- (*n* − 1)-vectors are pseudovectors;
- *n*-vectors are pseudoscalars.

In the presence of a volume form (such as given an inner product and an orientation), pseudovectors and pseudoscalars can be identified with vectors and scalars, which is routine in vector calculus, but without a volume form this cannot be done without making an arbitrary choice.

In the algebra of physical space (the geometric algebra of Euclidean 3-space, used as a model of (3+1)-spacetime), a sum of a scalar and a vector is called a paravector, and represents a point in spacetime (the vector the space, the scalar the time).

### Bivectors

A **bivector** is an element of the antisymmetric tensor product of a tangent space with itself.

In geometric algebra, also, a **bivector** is a grade 2 element (a 2-vector) resulting from the wedge product of two vectors, and so it is geometrically an *oriented area*, in the same way a *vector* is an oriented line segment. If **a** and **b** are two vectors, the bivector **a** ∧ **b** has

- a norm which is its area, given by $\left\|\mathbf {a} \wedge \mathbf {b} \right\|=\left\|\mathbf {a} \right\|\,\left\|\mathbf {b} \right\|\,\sin(\phi _{a,b})$
- a direction: the plane where that area lies on, i.e., the plane determined by **a** and **b**, as long as they are linearly independent;
- an orientation (out of two), determined by the order in which the originating vectors are multiplied.

Bivectors are connected to pseudovectors, and are used to represent rotations in geometric algebra.

As bivectors are elements of a vector space Λ2*V* (where *V* is a finite-dimensional vector space with dim *V* = *n*), it makes sense to define an inner product on this vector space as follows. First, write any element *F* ∈ Λ2*V* in terms of a basis (**e***i* ∧ **e***j*)1 ≤ *i* < *j* ≤ *n* of Λ2*V* as

$F=F^{ab}\mathbf {e} _{a}\wedge \mathbf {e} _{b}\quad (1\leq a<b\leq n),$

where the Einstein summation convention is being used.

Now define a map G : Λ2*V* × Λ2*V* → **R** by insisting that

$G(F,H):=G_{abcd}F^{ab}H^{cd},$

where $G_{abcd}$ are a set of numbers.

## Applications

Bivectors play many important roles in physics, for example, in the classification of electromagnetic fields.
