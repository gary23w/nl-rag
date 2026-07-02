---
title: "Stone–Weierstrass theorem"
source: https://en.wikipedia.org/wiki/Weierstrass_approximation_theorem
domain: approximation-theory
license: CC-BY-SA-4.0
tags: approximation theory, remez algorithm, pade approximant, minimax approximation
fetched: 2026-07-02
---

# Stone–Weierstrass theorem

(Redirected from

Weierstrass approximation theorem

)

In mathematical analysis, the **Weierstrass approximation theorem** states that every continuous function defined on a closed interval [*a*, *b*] can be uniformly approximated as closely as desired by a polynomial function. Because polynomials are among the simplest functions, and because computers can directly evaluate polynomials, this theorem has both practical and theoretical relevance, especially in polynomial interpolation. The original version of this result was established by Karl Weierstrass in 1885 using the Weierstrass transform.

Marshall H. Stone considerably generalized the theorem and simplified the proof. His result is known as the **Stone–Weierstrass theorem**. The Stone–Weierstrass theorem generalizes the Weierstrass approximation theorem in two directions: instead of the real interval [*a*, *b*], an arbitrary compact Hausdorff space X is considered, and instead of the algebra of polynomial functions, a variety of other families of continuous functions on X are shown to suffice, as is detailed below. The Stone–Weierstrass theorem is a vital result in the study of the algebra of continuous functions on a compact Hausdorff space.

Further, there is a generalization of the Stone–Weierstrass theorem to noncompact Tychonoff spaces, namely, any continuous function on a Tychonoff space is approximated uniformly on compact sets by algebras of the type appearing in the Stone–Weierstrass theorem and described below.

A different generalization of Weierstrass' original theorem is Mergelyan's theorem, which generalizes it to functions defined on certain subsets of the complex plane.

## Weierstrass approximation theorem

The statement of the approximation theorem as originally discovered by Weierstrass is as follows:

**Weierstrass approximation theorem**—Suppose *f* is a continuous real-valued function defined on the real interval [*a*, *b*]. For every *ε* > 0, there exists a polynomial *p* such that for all x in [*a*, *b*], we have |*f*(*x*) − *p*(*x*)| < *ε*, or equivalently, the supremum norm ‖*f* − *p*‖ < *ε*.

The page for Bernstein polynomials outlines a constructive proof of the above theorem.

### Degree of approximation

For differentiable functions, Jackson's inequality bounds the error of approximations by polynomials of a given degree: if f has a continuous k-th derivative, then for every $n\in \mathbb {N}$ there exists a polynomial $p_{n}$ of degree at most n such that $\lVert f-p_{n}\rVert \leq {\frac {\pi }{2}}{\frac {1}{(n+1)^{k}}}\lVert f^{(k)}\rVert$ .

However, if f is merely continuous, the convergence of the approximations can be arbitrarily slow in the following sense: for any sequence of positive real numbers $(a_{n})_{n\in \mathbb {N} }$ decreasing to 0 there exists a function f such that $\lVert f-p\rVert >a_{n}$ for every polynomial p of degree at most n .

### Applications

As a consequence of the Weierstrass approximation theorem, one can show that the space C[*a*, *b*] is separable: the polynomial functions are dense, and each polynomial function can be uniformly approximated by one with rational coefficients; there are only countably many polynomials with rational coefficients. Since C[*a*, *b*] is metrizable and separable it follows that C[*a*, *b*] has cardinality at most 2ℵ0. (Remark: This cardinality result also follows from the fact that a continuous function on the reals is uniquely determined by its restriction to the rationals.)

## Stone–Weierstrass theorem, real version

The set C[*a*, *b*] of continuous real-valued functions on [*a*, *b*], together with the supremum norm ‖*f*‖ = sup*a* ≤ *x* ≤ *b* |*f* (*x*)| is a Banach algebra, (that is, an associative algebra and a Banach space such that ‖*fg*‖ ≤ ‖*f*‖·‖*g*‖ for all  *f*, *g*). The set of all polynomial functions forms a subalgebra of C[*a*, *b*] (that is, a vector subspace of C[*a*, *b*] that is closed under multiplication of functions), and the content of the Weierstrass approximation theorem is that this subalgebra is dense in C[*a*, *b*].

Stone starts with an arbitrary compact Hausdorff space X and considers the algebra C(*X*, **R**) of real-valued continuous functions on X, with the topology induced by the supremum norm. He wants to find subalgebras of C(*X*, **R**) which are dense. It turns out that the crucial property that a subalgebra must satisfy is that it *separates points*: a set A of functions defined on X is said to separate points if, for every two different points x and y in X there exists a function p in A with *p*(*x*) ≠ *p*(*y*). Now we may state:

**Stone–Weierstrass theorem (real numbers)**—Suppose X is a compact Hausdorff space and A is a subalgebra of C(*X*, **R**) which contains a non-zero constant function. Then A is dense in C(*X*, **R**) if and only if it separates points.

This implies Weierstrass' original statement since the polynomials on [*a*, *b*] form a subalgebra of C[*a*, *b*] which contains the constants and separates points.

### Locally compact version

A version of the Stone–Weierstrass theorem is also true when X is only locally compact. Let C0(*X*, **R**) be the space of real-valued continuous functions on X that vanish at infinity; that is, a continuous function  *f*  is in C0(*X*, **R**) if, for every *ε* > 0, there exists a compact set *K* ⊂ *X* such that  |*f*|  < *ε* on *X* \ *K*. Again, C0(*X*, **R**) is a Banach algebra with the supremum norm. A subalgebra A of C0(*X*, **R**) is said to **vanish nowhere** if not all of the elements of A simultaneously vanish at a point; that is, for every x in X, there is some  *f*  in A such that  *f* (*x*) ≠ 0. The theorem generalizes as follows:

**Stone–Weierstrass theorem (locally compact spaces)**—Suppose X is a *locally compact* Hausdorff space and A is a subalgebra of C0(*X*, **R**). Then A is dense in C0(*X*, **R**) (given the topology of uniform convergence) if and only if it separates points and vanishes nowhere.

This version clearly implies the previous version in the case when X is compact, since in that case C0(*X*, **R**) = C(*X*, **R**). There are also more general versions of the Stone–Weierstrass theorem that weaken the assumption of local compactness.

### Applications

The Stone–Weierstrass theorem can be used to prove the following two statements, which go beyond Weierstrass's result.

- If  *f*  is a continuous real-valued function defined on the set [*a*, *b*] × [*c*, *d*] and *ε* > 0, then there exists a polynomial function p in two variables such that | *f* (*x*, *y*) − *p*(*x*, *y*) | < *ε* for all x in [*a*, *b*] and y in [*c*, *d*].
- If X and Y are two compact Hausdorff spaces and *f* : *X* × *Y* → **R** is a continuous function, then for every *ε* > 0 there exist *n* > 0 and continuous functions  *f*1, ...,  *fn*  on X and continuous functions *g*1, ..., *gn* on Y such that ‖*f* − Σ *fi gi*‖ < *ε*.

## Stone–Weierstrass theorem, complex version

Slightly more general is the following theorem, where we consider the algebra $C(X,\mathbb {C} )$ of complex-valued continuous functions on the compact space X , again with the topology of uniform convergence. This is a C*-algebra with the *-operation given by pointwise complex conjugation.

**Stone–Weierstrass theorem (complex numbers)**—Let X be a compact Hausdorff space and let S be a separating subset of $C(X,\mathbb {C} )$ . Then the complex unital *-algebra generated by S is dense in $C(X,\mathbb {C} )$ .

The complex unital *-algebra generated by S consists of all those functions that can be obtained from the elements of S by throwing in the constant function 1 and adding them, multiplying them, conjugating them, or multiplying them with complex scalars, and repeating finitely many times.

This theorem implies the real version, because if a net of complex-valued functions uniformly approximates a given function, $f_{n}\to f$ , then the real parts of those functions uniformly approximate the real part of that function, $\operatorname {Re} f_{n}\to \operatorname {Re} f$ , and because for real subsets, $S\subset C(X,\mathbb {R} )\subset C(X,\mathbb {C} ),$ taking the real parts of the generated complex unital (selfadjoint) algebra agrees with the generated real unital algebra generated.

As in the real case, an analog of this theorem is true for locally compact Hausdorff spaces.

The following is an application of this complex version.

- Fourier series: The set of linear combinations of functions *en*(*x*) = *e*2*πinx*, *n* ∈ **Z** is dense in C([0, 1]/{0, 1}), where we identify the endpoints of the interval [0, 1] to obtain a circle. An important consequence of this is that the *en* are an orthonormal basis of the space L2([0, 1]) of square-integrable functions on [0, 1].

## Stone–Weierstrass theorem, quaternion version

Following Holladay (1957), consider the algebra C(*X*, **H**) of quaternion-valued continuous functions on the compact space X, again with the topology of uniform convergence.

If a quaternion *q* is written in the form ${\textstyle q=a+ib+jc+kd}$

- its scalar part *a* is the real number ${\frac {q-iqi-jqj-kqk}{4}}$ .

Likewise

- the scalar part of −*qi* is *b* which is the real number ${\frac {-qi-iq+jqk-kqj}{4}}$ .
- the scalar part of −*qj* is *c* which is the real number ${\frac {-qj-iqk-jq+kqi}{4}}$ .
- the scalar part of −*qk* is *d* which is the real number ${\frac {-qk+iqj-jqk-kq}{4}}$ .

Then we may state:

**Stone–Weierstrass theorem (quaternion numbers)**—Suppose X is a compact Hausdorff space and A is a subalgebra of C(*X*, **H**) which contains a non-zero constant function. Then A is dense in C(*X*, **H**) if and only if it separates points.

## Stone–Weierstrass theorem, C*-algebra version

The space of complex-valued continuous functions on a compact Hausdorff space X i.e. $C(X,\mathbb {C} )$ is the canonical example of a unital commutative C*-algebra ${\mathfrak {A}}$ . The space *X* may be viewed as the space of pure states on ${\mathfrak {A}}$ , with the weak-* topology. Following the above cue, a non-commutative extension of the Stone–Weierstrass theorem, which remains unsolved, is as follows:

**Conjecture**—If a unital C*-algebra ${\mathfrak {A}}$ has a C*-subalgebra ${\mathfrak {B}}$ which separates the pure states of ${\mathfrak {A}}$ , then ${\mathfrak {A}}={\mathfrak {B}}$ .

In 1960, Jim Glimm proved a weaker version of the above conjecture.

**Stone–Weierstrass theorem (C*-algebras)**—If a unital C*-algebra ${\mathfrak {A}}$ has a C*-subalgebra ${\mathfrak {B}}$ which separates the pure state space (i.e. the weak-* closure of the pure states) of ${\mathfrak {A}}$ , then ${\mathfrak {A}}={\mathfrak {B}}$ .

## Lattice versions

Let X be a compact Hausdorff space. Stone's original proof of the theorem used the idea of lattices in C(*X*, **R**). A subset L of C(*X*, **R**) is called a lattice if for any two elements  *f*, *g* ∈ *L*, the functions max{ *f*, *g*}, min{ *f*, *g*} also belong to L. The lattice version of the Stone–Weierstrass theorem states:

**Stone–Weierstrass theorem (lattices)**—Suppose X is a compact Hausdorff space with at least two points and L is a lattice in C(*X*, **R**) with the property that for any two distinct elements x and y of X and any two real numbers a and b there exists an element  *f*  ∈ *L* with  *f* (*x*) = *a* and  *f* (*y*) = *b*. Then L is dense in C(*X*, **R**).

The above versions of Stone–Weierstrass can be proven from this version once one realizes that the lattice property can also be formulated using the absolute value | *f* | which in turn can be approximated by polynomials in  *f* . A variant of the theorem applies to linear subspaces of C(*X*, **R**) closed under max:

**Stone–Weierstrass theorem (max-closed)**—Suppose X is a compact Hausdorff space and B is a family of functions in C(*X*, **R**) such that

1. B separates points.
2. B contains the constant function 1.
3. If  *f*  ∈ *B* then *af*  ∈ *B* for all constants *a* ∈ **R**.
4. If  *f*,  *g* ∈ *B*, then  *f*  + *g*, max{ *f*, *g*} ∈ *B*.

Then B is dense in C(*X*, **R**).

More precise information is available:

Suppose

X

is a compact Hausdorff space with at least two points and

L

is a lattice in

C(

X

,

R

)

. The function

φ

∈ C(

X

,

R

)

belongs to the

closure

of

L

if and only if for each pair of distinct points

x

and

y

in

X

and for each

ε

> 0

there exists some

f

∈

L

for which

|

f

(

x

) −

φ

(

x

)| <

ε

and

|

f

(

y

) −

φ

(

y

)| <

ε

.

## Bishop's theorem

Another generalization of the Stone–Weierstrass theorem is due to Errett Bishop. Bishop's theorem is as follows:

**Bishop's theorem**—Let A be a closed subalgebra of the complex Banach algebra C(*X*, **C**) of continuous complex-valued functions on a compact Hausdorff space X, using the supremum norm. For *S* ⊂ *X* we write *AS* = {*g|S* : g ∈ *A*}. Suppose that *f*  ∈ C(*X*, **C**) has the following property:

f

|

S

∈

A

S

for every maximal set

S

⊂

X

such that all real functions of

A

S

are constant.

Then  *f*  ∈ *A*.

Glicksberg (1962) gives a short proof of Bishop's theorem using the Krein–Milman theorem in an essential way, as well as the Hahn–Banach theorem: the process of Louis de Branges (1959). See also Rudin (1973, §5.7).

## Nachbin's theorem

Nachbin's theorem gives an analog for Stone–Weierstrass theorem for algebras of complex valued smooth functions on a smooth manifold. Nachbin's theorem is as follows:

**Nachbin's theorem**—Let A be a subalgebra of the algebra C∞(*M*) of smooth functions on a finite dimensional smooth manifold M. Suppose that A separates the points of M and also separates the tangent vectors of M: for each point *m* ∈ *M* and tangent vector *v* at the tangent space at *m*, there is a *f* ∈ A such that d*f*(*x*)(*v*) ≠ 0. Then A is dense in C∞(*M*).

## Editorial history

In 1885 it was also published in an English version of the paper whose title was *On the possibility of giving an analytic representation to an arbitrary function of real variable*. According to the mathematician Yamilet Quintana, Weierstrass "suspected that any analytic functions could be represented by power series".
