---
title: "Jacobian matrix and determinant"
source: https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant
domain: inverse-kinematics-games
license: CC-BY-SA-4.0
tags: inverse kinematics, ik solver, forward kinematics, jacobian ik
fetched: 2026-07-02
---

# Jacobian matrix and determinant

In vector calculus, the **Jacobian matrix** (/dʒəˈkoʊbiən/, /dʒɪ-, jɪ-/) of a vector-valued function of several variables is the matrix of all its first-order partial derivatives. If this matrix is square, that is, if the number of variables equals the number of components of function values, then its determinant is called the **Jacobian determinant**. Both the matrix and (if applicable) the determinant are often referred to simply as the **Jacobian**. They are named after Carl Gustav Jacob Jacobi (1804-1851).

The Jacobian matrix is the natural generalization of the derivative and the differential of a usual function to vector valued functions of several variables. This generalization includes generalizations of the inverse function theorem and the implicit function theorem, where the non-nullity of the derivative is replaced by the non-nullity of the Jacobian determinant, and the multiplicative inverse of the derivative is replaced by the inverse of the Jacobian matrix.

The Jacobian determinant is fundamentally used for changes of variables in multiple integrals.

## Definition

Let ${\textstyle \mathbf {f}$ be a function such that each of its first-order partial derivatives exists on ${\textstyle \mathbb {R} ^{n}}$ . This function takes a vector ⁠ $\mathbf {x} =(x_{1},\ldots ,x_{n})\in \mathbb {R} ^{n}$ ⁠ as input and produces the vector ⁠ $\mathbf {f} (\mathbf {x} )=(f_{1}(\mathbf {x} ),\ldots ,f_{m}(\mathbf {x} ))\in \mathbb {R} ^{m}$ ⁠ as output. Then the Jacobian matrix of **f**, denoted **Jf**, is the ⁠ $m\times n$ ⁠ matrix whose (*i*, *j*) entry is ${\textstyle {\frac {\partial f_{i}}{\partial x_{j}}};}$ explicitly $\mathbf {J_{f}} ={\begin{bmatrix}{\dfrac {\partial \mathbf {f} }{\partial x_{1}}}&\cdots &{\dfrac {\partial \mathbf {f} }{\partial x_{n}}}\end{bmatrix}}={\begin{bmatrix}\nabla ^{\mathsf {T}}f_{1}\\\vdots \\\nabla ^{\mathsf {T}}f_{m}\end{bmatrix}}={\begin{bmatrix}{\dfrac {\partial f_{1}}{\partial x_{1}}}&\cdots &{\dfrac {\partial f_{1}}{\partial x_{n}}}\\\vdots &\ddots &\vdots \\{\dfrac {\partial f_{m}}{\partial x_{1}}}&\cdots &{\dfrac {\partial f_{m}}{\partial x_{n}}}\end{bmatrix}}$ where $\nabla ^{\mathsf {T}}f_{i}$ is the transpose (row vector) of the gradient of the i -th component.

The Jacobian matrix, whose entries are functions of **x**, is denoted in various ways; other common notations include *D***f**, $\nabla \mathbf {f}$ , and ${\textstyle {\frac {\partial (f_{1},\ldots ,f_{m})}{\partial (x_{1},\ldots ,x_{n})}}}$ . Some authors define the Jacobian as the transpose of the form given above.

The Jacobian matrix represents the total derivative of **f** at every point where **f** is differentiable. In detail, if **h** is a displacement vector represented by a column matrix, the matrix product **Jf**(**x**) ⋅ **h** is another displacement vector, that is the best linear approximation of the change of **f** along **h** in a neighborhood of **x**, if **f**(**x**) is differentiable at **x**. This means that the function that maps **y** to **f**(**x**) + **Jf**(**x**) ⋅ (**y** – **x**) is the best linear approximation of **f**(**y**) for all points **y** close to **x**. The linear map **h** → **Jf**(**x**) ⋅ **h** is known as the *derivative* or the *differential* of **f** at **x**.

When ${\textstyle m=n}$ , the Jacobian matrix is square, so its determinant is a well-defined function of **x**, known as the **Jacobian determinant** of **f**. It carries important information about the local behavior of **f**. In particular, the function **f** has a differentiable inverse function in a neighborhood of a point **x** if and only if the Jacobian determinant is nonzero at **x** (see inverse function theorem for an explanation of this and Jacobian conjecture for a related problem of *global* invertibility). The Jacobian determinant also appears when changing the variables in multiple integrals (see substitution rule for multiple variables).

When ${\textstyle m=1}$ , that is when ${\textstyle f:\mathbb {R} ^{n}\to \mathbb {R} }$ is a scalar-valued function, the Jacobian matrix reduces to the row vector $\nabla ^{\mathsf {T}}f$ ; this row vector of all first-order partial derivatives of ⁠ f ⁠ is the transpose of the gradient of ⁠ f ⁠, i.e. $\mathbf {J} _{f}=\nabla ^{\mathsf {T}}f$ . Specializing further, when ${\textstyle m=n=1}$ , that is when ${\textstyle f:\mathbb {R} \to \mathbb {R} }$ is a scalar-valued function of a single variable, the Jacobian matrix has a single entry; this entry is the derivative of the function ⁠ f ⁠.

## Jacobian matrix

The Jacobian of a vector-valued function in several variables generalizes the gradient of a scalar-valued function in several variables, which in turn generalizes the derivative of a scalar-valued function of a single variable. In other words, the Jacobian matrix of a scalar-valued function of several variables is (the transpose of) its gradient and the gradient of a scalar-valued function of a single variable is its derivative.

At each point where a function is differentiable, its Jacobian matrix can also be thought of as describing the amount of "stretching", "rotating" or "transforming" that the function imposes locally near that point. For example, if (*x*′, *y*′) = **f**(*x*, *y*) is used to smoothly transform an image, the Jacobian matrix **J****f**(*x*, *y*), describes how the image in the neighborhood of (*x*, *y*) is transformed.

If a function is differentiable at a point, its differential is given in coordinates by the Jacobian matrix. However, a function does not need to be differentiable for its Jacobian matrix to be defined, since only its first-order partial derivatives are required to exist.

If **f** is differentiable at a point **p** in **R***n*, then its differential is represented by **J****f**(**p**). In this case, the linear transformation represented by **J****f**(**p**) is the best linear approximation of **f** near the point **p**, in the sense that

$\mathbf {f} (\mathbf {x} )-\mathbf {f} (\mathbf {p} )=\mathbf {J} _{\mathbf {f} }(\mathbf {p} )(\mathbf {x} -\mathbf {p} )+o(\|\mathbf {x} -\mathbf {p} \|)\quad ({\text{as }}\mathbf {x} \to \mathbf {p} ),$

where *o*(‖**x** − **p**‖) is a quantity that approaches zero much faster than the distance between **x** and **p** does as **x** approaches **p**. This approximation specializes to the approximation of a scalar function of a single variable by its Taylor polynomial of degree one, namely

$f(x)-f(p)=f'(p)(x-p)+o(x-p)\quad ({\text{as }}x\to p).$

In this sense, the Jacobian may be regarded as a kind of "first-order derivative" of a vector-valued function of several variables. In particular, this means that the gradient of a scalar-valued function of several variables may too be regarded as its "first-order derivative".

Composable differentiable functions **f** : **R***n* → **R***m* and **g** : **R***m* → **R***k* satisfy the chain rule, namely $\mathbf {J} _{\mathbf {g} \circ \mathbf {f} }(\mathbf {x} )=\mathbf {J} _{\mathbf {g} }(\mathbf {f} (\mathbf {x} ))\mathbf {J} _{\mathbf {f} }(\mathbf {x} )$ for **x** in **R***n*.

The Jacobian of the gradient of a scalar function of several variables has a special name: the Hessian matrix, which in a sense is the "second derivative" of the function in question.

## Jacobian determinant

If *m* = *n*, then **f** is a function from **R***n* to itself and the Jacobian matrix is a square matrix. We can then form its determinant, known as the **Jacobian determinant**. The Jacobian determinant is sometimes simply referred to as "the Jacobian".

The Jacobian determinant at a given point gives important information about the behavior of **f** near that point. For instance, the continuously differentiable function **f** is invertible near a point **p** ∈ **R***n* if the Jacobian determinant at **p** is non-zero. This is the inverse function theorem. Furthermore, if the Jacobian determinant at **p** is positive, then **f** preserves orientation near **p**; if it is negative, **f** reverses orientation. The absolute value of the Jacobian determinant at **p** gives us the factor by which the function **f** expands or shrinks volumes near **p**; this is why it occurs in the general substitution rule.

The Jacobian determinant is used when making a change of variables when evaluating a multiple integral of a function over a region within its domain. To accommodate for the change of coordinates the magnitude of the Jacobian determinant arises as a multiplicative factor within the integral. This is because the *n*-dimensional *dV* element is in general a parallelepiped in the new coordinate system, and the *n*-volume of a parallelepiped is the determinant of its edge vectors.

The Jacobian can also be used to determine the stability of equilibria for systems of differential equations by approximating behavior near an equilibrium point.

## Inverse

According to the inverse function theorem, the matrix inverse of the Jacobian matrix of an invertible function **f** : **R***n* → **R***n* is the Jacobian matrix of the *inverse* function. That is, the Jacobian matrix of the inverse function at a point **p** is

$\mathbf {J} _{\mathbf {f} ^{-1}}(\mathbf {p} )={\mathbf {J} _{\mathbf {f} }^{-1}(\mathbf {f} ^{-1}(\mathbf {p} ))},$

and the Jacobian determinant is

$\det(\mathbf {J} _{\mathbf {f} ^{-1}}(\mathbf {p} ))={\frac {1}{\det(\mathbf {J} _{\mathbf {f} }(\mathbf {f} ^{-1}(\mathbf {p} )))}}.$

If the Jacobian is continuous and nonsingular at the point **p** in **R***n*, then **f** is invertible when restricted to some neighbourhood of **p**. In other words, if the Jacobian determinant is not zero at a point, then the function is *locally invertible* near this point.

The (unproved) Jacobian conjecture is related to global invertibility in the case of a polynomial function, that is a function defined by *n* polynomials in *n* variables. It asserts that, if the Jacobian determinant is a non-zero constant (or, equivalently, that it does not have any complex zero), then the function is invertible and its inverse is a polynomial function.

## Critical points

If **f** : **R***n* → **R***m* is a differentiable function, a *critical point* of **f** is a point where the rank of the Jacobian matrix is not maximal. This means that the rank at the critical point is lower than the rank at some neighbour point. In other words, let *k* be the maximal dimension of the open balls contained in the image of **f**; then a point is critical if all minors of rank *k* of **f** are zero.

In the case where *m* = *n* = *k*, a point is critical if the Jacobian determinant is zero.

## Examples

### Example 1

Consider a function **f** : **R**2 → **R**3, with (*x*, *y*) ↦ (*f*1(*x*, *y*), *f*2(*x*, *y*), *f*3(*x*, *y*)), given by

$\mathbf {f} \left({\begin{bmatrix}x\\y\end{bmatrix}}\right)={\begin{bmatrix}f_{1}(x,y)\\f_{2}(x,y)\\f_{3}(x,y)\end{bmatrix}}={\begin{bmatrix}x^{2}y\\5x+\sin y\\4y\end{bmatrix}}.$

The Jacobian matrix of **f** is

$\mathbf {J} _{\mathbf {f} }(x,y)={\begin{bmatrix}{\dfrac {\partial f_{1}}{\partial x}}&{\dfrac {\partial f_{1}}{\partial y}}\\[1em]{\dfrac {\partial f_{2}}{\partial x}}&{\dfrac {\partial f_{2}}{\partial y}}\\[1em]{\dfrac {\partial f_{3}}{\partial x}}&{\dfrac {\partial f_{3}}{\partial y}}\end{bmatrix}}={\begin{bmatrix}2xy&x^{2}\\5&\cos y\\0&4\end{bmatrix}}$

### Example 2: polar-Cartesian transformation

The transformation from polar coordinates (*r*, *φ*) to Cartesian coordinates (*x*, *y*), is given by the function **F**: **R**+ × [0, 2π) → **R**2 with components

${\displaystyle {\begin{aligned}x&=r\cos \varphi$

$\mathbf {J} _{\mathbf {F} }(r,\varphi )={\begin{bmatrix}{\frac {\partial x}{\partial r}}&{\frac {\partial x}{\partial \varphi }}\\[0.5ex]{\frac {\partial y}{\partial r}}&{\frac {\partial y}{\partial \varphi }}\end{bmatrix}}={\begin{bmatrix}\cos \varphi &-r\sin \varphi \\\sin \varphi &r\cos \varphi \end{bmatrix}}$

The Jacobian determinant is equal to *r*. This can be used to transform integrals between the two coordinate systems:

$\iint _{\mathbf {F} (A)}f(x,y)\,dx\,dy=\iint _{A}f(r\cos \varphi ,r\sin \varphi )\,r\,dr\,d\varphi .$

### Example 3: spherical-Cartesian transformation

The transformation from spherical coordinates (*ρ*, *φ*, *θ*) to Cartesian coordinates (*x*, *y*, *z*), is given by the function **F**: **R**+ × [0, *π*) × [0, 2*π*) → **R**3 with components

${\displaystyle {\begin{aligned}x&=\rho \sin \varphi \cos \theta$

The Jacobian matrix for this coordinate change is

$\mathbf {J} _{\mathbf {F} }(\rho ,\varphi ,\theta )={\begin{bmatrix}{\dfrac {\partial x}{\partial \rho }}&{\dfrac {\partial x}{\partial \varphi }}&{\dfrac {\partial x}{\partial \theta }}\\[1em]{\dfrac {\partial y}{\partial \rho }}&{\dfrac {\partial y}{\partial \varphi }}&{\dfrac {\partial y}{\partial \theta }}\\[1em]{\dfrac {\partial z}{\partial \rho }}&{\dfrac {\partial z}{\partial \varphi }}&{\dfrac {\partial z}{\partial \theta }}\end{bmatrix}}={\begin{bmatrix}\sin \varphi \cos \theta &\rho \cos \varphi \cos \theta &-\rho \sin \varphi \sin \theta \\\sin \varphi \sin \theta &\rho \cos \varphi \sin \theta &\rho \sin \varphi \cos \theta \\\cos \varphi &-\rho \sin \varphi &0\end{bmatrix}}.$

The determinant is *ρ*2 sin *φ*. Since *dV* = *dx* *dy* *dz* is the volume for a rectangular differential volume element (because the volume of a rectangular prism is the product of its sides), we can interpret *dV* = *ρ*2 sin *φ* *dρ* *dφ* *dθ* as the volume of the spherical differential volume element. Unlike rectangular differential volume element's volume, this differential volume element's volume is not a constant, and varies with coordinates (*ρ* and *φ*). It can be used to transform integrals between the two coordinate systems:

$\iiint _{\mathbf {F} (U)}f(x,y,z)\,dx\,dy\,dz=\iiint _{U}f(\rho \sin \varphi \cos \theta ,\rho \sin \varphi \sin \theta ,\rho \cos \varphi )\,\rho ^{2}\sin \varphi \,d\rho \,d\varphi \,d\theta .$

### Example 4

The Jacobian matrix of the function **F** : **R**3 → **R**4 with components

${\begin{aligned}y_{1}&=x_{1}\\y_{2}&=5x_{3}\\y_{3}&=4x_{2}^{2}-2x_{3}\\y_{4}&=x_{3}\sin x_{1}\end{aligned}}$

is

$\mathbf {J} _{\mathbf {F} }(x_{1},x_{2},x_{3})={\begin{bmatrix}{\dfrac {\partial y_{1}}{\partial x_{1}}}&{\dfrac {\partial y_{1}}{\partial x_{2}}}&{\dfrac {\partial y_{1}}{\partial x_{3}}}\\[1em]{\dfrac {\partial y_{2}}{\partial x_{1}}}&{\dfrac {\partial y_{2}}{\partial x_{2}}}&{\dfrac {\partial y_{2}}{\partial x_{3}}}\\[1em]{\dfrac {\partial y_{3}}{\partial x_{1}}}&{\dfrac {\partial y_{3}}{\partial x_{2}}}&{\dfrac {\partial y_{3}}{\partial x_{3}}}\\[1em]{\dfrac {\partial y_{4}}{\partial x_{1}}}&{\dfrac {\partial y_{4}}{\partial x_{2}}}&{\dfrac {\partial y_{4}}{\partial x_{3}}}\end{bmatrix}}={\begin{bmatrix}1&0&0\\0&0&5\\0&8x_{2}&-2\\x_{3}\cos x_{1}&0&\sin x_{1}\end{bmatrix}}.$

This example shows that the Jacobian matrix need not be a square matrix.

### Example 5

The Jacobian determinant of the function **F** : **R**3 → **R**3 with components

${\begin{aligned}y_{1}&=5x_{2}\\y_{2}&=4x_{1}^{2}-2\sin(x_{2}x_{3})\\y_{3}&=x_{2}x_{3}\end{aligned}}$

is

${\begin{vmatrix}0&5&0\\8x_{1}&-2x_{3}\cos(x_{2}x_{3})&-2x_{2}\cos(x_{2}x_{3})\\0&x_{3}&x_{2}\end{vmatrix}}=-8x_{1}{\begin{vmatrix}5&0\\x_{3}&x_{2}\end{vmatrix}}=-40x_{1}x_{2}.$

From this we see that **F** reverses orientation near those points where *x*1 and *x*2 have the same sign; the function is locally invertible everywhere except near points where *x*1 = 0 or *x*2 = 0. Intuitively, if one starts with a tiny object around the point (1, 2, 3) and apply **F** to that object, one will get a resulting object with approximately 40 × 1 × 2 = 80 times the volume of the original one, with orientation reversed.

## Other uses

### Dynamical systems

Consider a dynamical system of the form ${\dot {\mathbf {x} }}=F(\mathbf {x} )$ , where ${\dot {\mathbf {x} }}$ is the (component-wise) derivative of $\mathbf {x}$ with respect to the evolution parameter t (time), and $F\colon \mathbb {R} ^{n}\to \mathbb {R} ^{n}$ is differentiable. If $F(\mathbf {x} _{0})=0$ , then $\mathbf {x} _{0}$ is a stationary point (also called a steady state). By the Hartman–Grobman theorem, the behavior of the system near a stationary point is related to the eigenvalues of $\mathbf {J} _{F}\left(\mathbf {x} _{0}\right)$ , the Jacobian of F at the stationary point. Specifically, if the eigenvalues all have real parts that are negative, then the system is stable near the stationary point. If any eigenvalue has a real part that is positive, then the point is unstable. If the largest real part of the eigenvalues is zero, the Jacobian matrix does not allow for an evaluation of the stability.

### Newton's method

A square system of coupled nonlinear equations can be solved iteratively by Newton's method. This method uses the Jacobian matrix of the system of equations.

### Regression and least squares fitting

The Jacobian serves as a linearized design matrix in statistical regression and curve fitting; see non-linear least squares. The Jacobian is also used in random matrices, moments, local sensitivity and statistical diagnostics.
