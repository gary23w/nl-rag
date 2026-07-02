---
title: "Hecke operator"
source: https://en.wikipedia.org/wiki/Hecke_operator
domain: modular-forms
license: CC-BY-SA-4.0
tags: modular form, modular group, eisenstein series, hecke operator
fetched: 2026-07-02
---

# Hecke operator

In mathematics, in particular in the theory of modular forms, a **Hecke operator**, studied by Erich Hecke (1937a,1937b), is a certain kind of "averaging" operator that plays a significant role in the structure of vector spaces of modular forms and more general automorphic representations.

## Mathematical description

Hecke operators can be realized in a number of contexts. The simplest meaning is combinatorial, namely as taking for a given integer n some function ${\textstyle f(\Lambda )}$ defined on the lattices of fixed rank to

$\sum f(\Lambda ')$

with the sum taken over all the ${\textstyle \Lambda '}$ that are subgroups of ${\textstyle \Lambda }$ of index n . For example, with ${\textstyle n=2}$ and two dimensions, there are three such ${\textstyle \Lambda '}$ . Modular forms are particular kinds of functions of a lattice, subject to conditions making them analytic functions and homogeneous with respect to homotheties, as well as moderate growth at infinity; these conditions are preserved by the summation, and so Hecke operators preserve the space of modular forms of a given weight.

Another way to express Hecke operators is by means of double cosets in the modular group. In the contemporary adelic approach, this translates to double cosets with respect to some compact subgroups.

### Explicit formula

Let ${\textstyle M_{m}}$ be the set of ${\textstyle 2\times 2}$ integral matrices with determinant m and ${\textstyle \Gamma =M_{1}}$ be the full modular group ${\textstyle {\text{SL}}_{2}(\mathbb {Z} )}$ . Given a modular form ${\textstyle f(z)}$ of weight k , the m th Hecke operator acts by the formula

$T_{m}f(z)=m^{k-1}\sum _{\left({\begin{smallmatrix}a&b\\c&d\end{smallmatrix}}\right)\in \Gamma \backslash M_{m}}(cz+d)^{-k}f\left({\frac {az+b}{cz+d}}\right),$

where ${\textstyle z}$ is in the upper half-plane and the normalization constant ${\textstyle m^{k-1}}$ assures that the image of a form with integer Fourier coefficients has integer Fourier coefficients. This can be rewritten in the form

$T_{m}f(z)=m^{k-1}\sum _{\begin{smallmatrix}ad=m\\a,d>0\end{smallmatrix}}{\frac {1}{d^{k}}}\sum _{b{\pmod {d}}}f\left({\frac {az+b}{d}}\right),$

which leads to the formula for the Fourier coefficients of ${\textstyle T_{m}(f(z))=\sum b(n)q^{n}}$ in terms of the Fourier coefficients of ${\textstyle f(z)=\sum a(n)q^{n}}$ :

$b(n)=\sum _{d|(m,n)}d^{k-1}a\left({\frac {mn}{d^{2}}}\right).$

One can see from this explicit formula that Hecke operators with different indices commute and that if ${\textstyle a(0)=0}$ then ${\textstyle b(0)=0}$ , so the subspace ${\textstyle S_{k}}$ of cusp forms of weight k is preserved by the Hecke operators. If a (non-zero) cusp form f is a simultaneous eigenform of all Hecke operators ${\textstyle T_{m}}$ with eigenvalues ${\textstyle \lambda _{m}}$ then ${\textstyle a(m)=\lambda _{m}a(1)}$ and ${\textstyle a(1)\neq 1}$ . Hecke eigenforms are **normalized** so that ${\textstyle a(1)=0}$ , then

$T_{m}f=a(m)f,\quad a(m)a(n)=\sum _{d|(m,n)}d^{k-1}a\left({\frac {mn}{d^{2}}}\right),\quad m,n\geq 1.$

Thus for normalized cuspidal Hecke eigenforms of integer weight, their Fourier coefficients coincide with their Hecke eigenvalues.

## History

Mordell (1917) used Hecke operators on modular forms in a paper on the special cusp form of Ramanujan, ahead of the general theory given by Hecke (1937a,1937b). Mordell proved the Hecke relations for the Ramanujan tau function, which implies that it is a multiplicative function, a property conjectured by Ramanujan. The idea goes back to earlier work of Adolf Hurwitz, who treated algebraic correspondences between modular curves which realise some individual Hecke operators.

## Hecke algebras

Algebras of Hecke operators are called "Hecke algebras", and are commutative rings. In the classical elliptic modular form theory, the Hecke operators ${\textstyle T_{n}}$ with ${\textstyle n}$ coprime to the level acting on the space of cusp forms of a given weight are self-adjoint with respect to the Petersson inner product. Therefore, the spectral theorem implies that there is a basis of modular forms that are eigenfunctions for these Hecke operators. Each of these basic forms possesses an Euler product. More precisely, its Mellin transform is the Dirichlet series that has Euler products with the local factor for each prime ${\textstyle p}$ is the inverse of the **Hecke polynomial**, a quadratic polynomial in ${\textstyle p^{-s}}$ . In the case treated by Mordell, the space of cusp forms of weight 12 with respect to the full modular group is one-dimensional. It follows that the Ramanujan form has an Euler product and establishes the multiplicativity of Ramanujan's tau function ${\textstyle \tau (n)}$ .

Other related mathematical rings are also called "Hecke algebras", although sometimes the link to Hecke operators is not entirely obvious. These algebras include certain quotients of the group algebras of braid groups. The presence of this commutative operator algebra plays a significant role in the harmonic analysis of modular forms and generalisations.
