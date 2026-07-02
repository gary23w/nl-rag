---
title: "Spherical harmonics (part 2/2)"
source: https://en.wikipedia.org/wiki/Spherical_harmonics
domain: light-probes
license: CC-BY-SA-4.0
tags: light probe capture, spherical harmonic lighting, irradiance probe, precomputed radiance transfer
fetched: 2026-07-02
part: 2/2
---

## Algebraic properties

### Addition theorem

A mathematical result of considerable interest and use is called the *addition theorem* for spherical harmonics. Given two vectors **r** and **r′**, with spherical coordinates $(r,\theta ,\varphi )$ and $(r,\theta ',\varphi ')$ , respectively, the angle $\gamma$ between them is given by the relation $\cos \gamma =\cos \theta '\cos \theta +\sin \theta \sin \theta '\cos(\varphi -\varphi ')$ in which the role of the trigonometric functions appearing on the right-hand side is played by the spherical harmonics and that of the left-hand side is played by the Legendre polynomials.

The *addition theorem* states

| $P_{\ell }(\mathbf {x} \cdot \mathbf {y} )={\frac {4\pi }{2\ell +1}}\sum _{m=-\ell }^{\ell }Y_{\ell }^{m}(\mathbf {y} )\,Y_{\ell }^{m}{}^{*}(\mathbf {x} )\quad \forall \,\ell \in \mathbb {N} _{0}\;\forall \,\mathbf {x} ,\mathbf {y} \in \mathbb {R} ^{3}\colon \;\\|\mathbf {x} \\|_{2}=\\|\mathbf {y} \\|_{2}=1\,,$ |   | 1 |
|---|---|---|

where *P**ℓ* is the Legendre polynomial of degree ℓ. This expression is valid for both real and complex harmonics. The result can be proven analytically, using the properties of the Poisson kernel in the unit ball, or geometrically by applying a rotation to the vector **y** so that it points along the *z*-axis, and then directly calculating the right-hand side.

In particular, when **x** = **y**, this gives Unsöld's theorem $\sum _{m=-\ell }^{\ell }Y_{\ell }^{m}{}^{*}(\mathbf {x} )\,Y_{\ell }^{m}(\mathbf {x} )={\frac {2\ell +1}{4\pi }}$ which generalizes the identity cos2*θ* + sin2*θ* = 1 to two dimensions.

In the expansion (**1**), the left-hand side $P_{\ell }(\mathbf {x} \cdot \mathbf {y} )$ is a constant multiple of the degree ℓ zonal spherical harmonic. From this perspective, one has the following generalization to higher dimensions. Let *Y**j* be an arbitrary orthonormal basis of the space **H***ℓ* of degree ℓ spherical harmonics on the n-sphere. Then $Z_{\mathbf {x} }^{(\ell )}$ , the degree ℓ zonal harmonic corresponding to the unit vector x, decomposes as

| $Z_{\mathbf {x} }^{(\ell )}({\mathbf {y} })=\sum _{j=1}^{\dim(\mathbf {H} _{\ell })}{\overline {Y_{j}({\mathbf {x} })}}\,Y_{j}({\mathbf {y} })$ |   | 2 |
|---|---|---|

Furthermore, the zonal harmonic $Z_{\mathbf {x} }^{(\ell )}({\mathbf {y} })$ is given as a constant multiple of the appropriate Gegenbauer polynomial:

| $Z_{\mathbf {x} }^{(\ell )}({\mathbf {y} })=C_{\ell }^{((n-2)/2)}({\mathbf {x} }\cdot {\mathbf {y} })$ |   | 3 |
|---|---|---|

Combining (**2**) and (**3**) gives (**1**) in dimension *n* = 2 when **x** and **y** are represented in spherical coordinates. Finally, evaluating at **x** = **y** gives the functional identity ${\frac {\dim \mathbf {H} _{\ell }}{\omega _{n-1}}}=\sum _{j=1}^{\dim(\mathbf {H} _{\ell })}|Y_{j}({\mathbf {x} })|^{2}$ where *ω**n*−1 is the volume of the (*n*−1)-sphere.

### Contraction rule

Another useful identity expresses the product of two spherical harmonics as a sum over spherical harmonics ${\begin{aligned}Y_{a}^{\alpha }\left(\theta ,\varphi \right)Y_{b}^{\beta }\left(\theta ,\varphi \right)&={\sqrt {\frac {\left(2a+1\right)\left(2b+1\right)}{4\pi }}}\sum _{c=0}^{\infty }\sum _{\gamma =-c}^{c}\left(-1\right)^{\gamma }{\sqrt {2c+1}}{\begin{pmatrix}a&b&c\\\alpha &\beta &-\gamma \end{pmatrix}}{\begin{pmatrix}a&b&c\\0&0&0\end{pmatrix}}Y_{c}^{\gamma }\left(\theta ,\varphi \right)\\&={\sqrt {\frac {\left(2a+1\right)\left(2b+1\right)}{4\pi }}}\sum _{c=|a-b|}^{a+b}{\frac {1}{\sqrt {2c+1}}}\left\langle a\,\alpha \,b\,\beta |c\,\alpha +\beta \right\rangle \left\langle a\,0\,b\,0|c\,0\right\rangle Y_{c}^{\gamma }\left(\theta ,\varphi \right)\end{aligned}}$ Many of the terms in this sum are trivially zero. The values of c and $\gamma$ that result in non-zero terms in this sum are determined by the selection rules for the 3j-symbols.

### Clebsch–Gordan coefficients

The Clebsch–Gordan coefficients are the coefficients appearing in the expansion of the product of two spherical harmonics in terms of spherical harmonics themselves. A variety of techniques are available for doing essentially the same calculation, including the Wigner 3-jm symbol, the Racah coefficients, and the Slater integrals. Abstractly, the Clebsch–Gordan coefficients express the tensor product of two irreducible representations of the rotation group as a sum of irreducible representations: suitably normalized, the coefficients are then the multiplicities.


## Visualization of the spherical harmonics

The Laplace spherical harmonics $Y_{\ell }^{m}$ can be visualized by considering their "nodal lines", that is, the set of points on the sphere where $\Re [Y_{\ell }^{m}]=0$ , or alternatively where $\Im [Y_{\ell }^{m}]=0$ . Nodal lines of $Y_{\ell }^{m}$ are composed of *ℓ* circles: there are |*m*| circles along longitudes and *ℓ*−|*m*| circles along latitudes. One can determine the number of nodal lines of each type by counting the number of zeros of $Y_{\ell }^{m}$ in the $\theta$ and $\varphi$ directions respectively. Considering $Y_{\ell }^{m}$ as a function of $\theta$ , the real and imaginary components of the associated Legendre polynomials each possess *ℓ*−|*m*| zeros, each giving rise to a nodal 'line of latitude'. On the other hand, considering $Y_{\ell }^{m}$ as a function of $\varphi$ , the trigonometric sin and cos functions possess 2|*m*| zeros, each of which gives rise to a nodal 'line of longitude'.

When the spherical harmonic order *m* is zero (upper-left in the figure), the spherical harmonic functions do not depend upon longitude, and are referred to as ***zonal***. Such spherical harmonics are a special case of zonal spherical functions. When *ℓ* = |*m*| (bottom-right in the figure), there are no zero crossings in latitude, and the functions are referred to as ***sectoral***. For the other cases, the functions checker the sphere, and they are referred to as ***tesseral***.

More general spherical harmonics of degree ℓ are not necessarily those of the Laplace basis $Y_{\ell }^{m}$ , and their nodal sets can be of a fairly general kind.


## List of spherical harmonics

Analytic expressions for the first few orthonormalized Laplace spherical harmonics $Y_{\ell }^{m}:S^{2}\to \mathbb {C}$ that use the Condon–Shortley phase convention: $Y_{0}^{0}(\theta ,\varphi )={\frac {1}{2}}{\sqrt {\frac {1}{\pi }}}$

${\begin{aligned}Y_{1}^{-1}(\theta ,\varphi )&={\frac {1}{2}}{\sqrt {\frac {3}{2\pi }}}\,\sin \theta \,e^{-i\varphi }\\Y_{1}^{0}(\theta ,\varphi )&={\frac {1}{2}}{\sqrt {\frac {3}{\pi }}}\,\cos \theta \\Y_{1}^{1}(\theta ,\varphi )&={\frac {-1}{2}}{\sqrt {\frac {3}{2\pi }}}\,\sin \theta \,e^{i\varphi }\end{aligned}}$

${\begin{aligned}Y_{2}^{-2}(\theta ,\varphi )&={\frac {1}{4}}{\sqrt {\frac {15}{2\pi }}}\,\sin ^{2}\theta \,e^{-2i\varphi }\\Y_{2}^{-1}(\theta ,\varphi )&={\frac {1}{2}}{\sqrt {\frac {15}{2\pi }}}\,\sin \theta \,\cos \theta \,e^{-i\varphi }\\Y_{2}^{0}(\theta ,\varphi )&={\frac {1}{4}}{\sqrt {\frac {5}{\pi }}}\,(3\cos ^{2}\theta -1)\\Y_{2}^{1}(\theta ,\varphi )&={\frac {-1}{2}}{\sqrt {\frac {15}{2\pi }}}\,\sin \theta \,\cos \theta \,e^{i\varphi }\\Y_{2}^{2}(\theta ,\varphi )&={\frac {1}{4}}{\sqrt {\frac {15}{2\pi }}}\,\sin ^{2}\theta \,e^{2i\varphi }\end{aligned}}$


## Higher dimensions

The classical spherical harmonics are defined as complex-valued functions on the unit sphere $S^{2}$ inside three-dimensional Euclidean space $\mathbb {R} ^{3}$ . Spherical harmonics can be generalized to higher-dimensional Euclidean space $\mathbb {R} ^{n}$ as follows, leading to functions $S^{n-1}\to \mathbb {C}$ . Let **P***ℓ* denote the space of complex-valued homogeneous polynomials of degree ℓ in n real variables, here considered as functions $\mathbb {R} ^{n}\to \mathbb {C}$ . That is, a polynomial *p* is in **P***ℓ* provided that for any real $\lambda \in \mathbb {R}$ , one has

$p(\lambda \mathbf {x} )=\lambda ^{\ell }p(\mathbf {x} ).$

Let **A***ℓ* denote the subspace of **P***ℓ* consisting of all harmonic polynomials: $\mathbf {A} _{\ell }:=\{p\in \mathbf {P} _{\ell }\,\mid \,\Delta p=0\}\,.$ These are the (regular) solid spherical harmonics. Let **H***ℓ* denote the space of functions on the unit sphere $S^{n-1}:=\{\mathbf {x} \in \mathbb {R} ^{n}\,\mid \,\left|x\right|=1\}$ obtained by restriction from **A***ℓ* $\mathbf {H} _{\ell }:=\left\{f:S^{n-1}\to \mathbb {C} \,\mid \,{\text{ for some }}p\in \mathbf {A} _{\ell },\,f(\mathbf {x} )=p(\mathbf {x} ){\text{ for all }}\mathbf {x} \in S^{n-1}\right\}.$

The following properties hold:

- The sum of the spaces **H***ℓ* is dense in the set $C(S^{n-1})$ of continuous functions on $S^{n-1}$ with respect to the uniform topology, by the Stone–Weierstrass theorem. As a result, the sum of these spaces is also dense in the space *L*2(*S**n*−1) of square-integrable functions on the sphere. Thus every square-integrable function on the sphere decomposes uniquely into a series of spherical harmonics, where the series converges in the *L*2 sense.
- For all *f* ∈ **H***ℓ*, one has $\Delta _{S^{n-1}}f=-\ell (\ell +n-2)f.$ where Δ*S**n*−1 is the Laplace–Beltrami operator on *S**n*−1. This operator is the analog of the angular part of the Laplacian in three dimensions; to wit, the Laplacian in n dimensions decomposes as $\nabla ^{2}=r^{1-n}{\frac {\partial }{\partial r}}r^{n-1}{\frac {\partial }{\partial r}}+r^{-2}\Delta _{S^{n-1}}={\frac {\partial ^{2}}{\partial r^{2}}}+{\frac {n-1}{r}}{\frac {\partial }{\partial r}}+r^{-2}\Delta _{S^{n-1}}$
- It follows from the Stokes theorem and the preceding property that the spaces **H***ℓ* are orthogonal with respect to the inner product from *L*2(*S**n*−1). That is to say, $\int _{S^{n-1}}f{\bar {g}}\,\mathrm {d} \Omega =0$ for *f* ∈ **H***ℓ* and *g* ∈ **H***k* for *k* ≠ *ℓ*.
- Conversely, the spaces **H***ℓ* are precisely the eigenspaces of Δ*S**n*−1. In particular, an application of the spectral theorem to the Riesz potential $\Delta _{S^{n-1}}^{-1}$ gives another proof that the spaces **H***ℓ* are pairwise orthogonal and complete in *L*2(*S**n*−1).
- Every homogeneous polynomial *p* ∈ **P***ℓ* can be uniquely written in the form $p(x)=p_{\ell }(x)+|x|^{2}p_{\ell -2}+\cdots +{\begin{cases}|x|^{\ell }p_{0}&\ell {\rm {\ even}}\\|x|^{\ell -1}p_{1}(x)&\ell {\rm {\ odd}}\end{cases}}$ where *p**j* ∈ **A***j*. In particular, $\dim \mathbf {H} _{\ell }={\binom {n+\ell -1}{n-1}}-{\binom {n+\ell -3}{n-1}}={\binom {n+\ell -2}{n-2}}+{\binom {n+\ell -3}{n-2}}.$

An orthogonal basis of spherical harmonics in higher dimensions can be constructed inductively by the method of separation of variables, by solving the Sturm-Liouville problem for the spherical Laplacian $\Delta _{S^{n-1}}=\sin ^{2-n}\varphi {\frac {\partial }{\partial \varphi }}\sin ^{n-2}\varphi {\frac {\partial }{\partial \varphi }}+\sin ^{-2}\varphi \Delta _{S^{n-2}}$ where *φ* is the axial coordinate in a spherical coordinate system on *S**n*−1. The end result of such a procedure is $Y_{\ell _{1},\dots \ell _{n-1}}(\theta _{1},\dots \theta _{n-1})={\frac {1}{\sqrt {2\pi }}}e^{i\ell _{1}\theta _{1}}\prod _{j=2}^{n-1}{}_{j}{\bar {P}}_{\ell _{j}}^{\ell _{j-1}}(\theta _{j})$ where the indices satisfy |*ℓ*1| ≤ *ℓ*2 ≤ ⋯ ≤ *ℓ**n*−1 and the eigenvalue is −*ℓ**n*−1(*ℓ**n*−1 + *n*−2). The functions in the product are defined in terms of the Legendre function ${}_{j}{\bar {P}}_{L}^{\ell }(\theta )={\sqrt {{\frac {2L+j-1}{2}}{\frac {(L+\ell +j-2)!}{(L-\ell )!}}}}\sin ^{\frac {2-j}{2}}(\theta )P_{L+{\frac {j-2}{2}}}^{-\left(\ell +{\frac {j-2}{2}}\right)}(\cos \theta )\,.$


## Connection with representation theory

The space **H***ℓ* of spherical harmonics of degree ℓ is a representation of the symmetry group of rotations around a point (SO(3)) and its double-cover SU(2). Indeed, rotations act on the two-dimensional sphere, and thus also on **H***ℓ* by function composition $\psi \mapsto \psi \circ \rho ^{-1}$ for ψ a spherical harmonic and ρ a rotation. The representation **H***ℓ* is an irreducible representation of SO(3).

The elements of **H***ℓ* arise as the restrictions to the sphere of elements of **A***ℓ*: harmonic polynomials homogeneous of degree ℓ on three-dimensional Euclidean space **R**3. By polarization of *ψ* ∈ **A***ℓ*, there are coefficients $\psi _{i_{1}\dots i_{\ell }}$ symmetric on the indices, uniquely determined by the requirement $\psi (x_{1},\dots ,x_{n})=\sum _{i_{1}\dots i_{\ell }}\psi _{i_{1}\dots i_{\ell }}x_{i_{1}}\cdots x_{i_{\ell }}.$ The condition that ψ be harmonic is equivalent to the assertion that the tensor $\psi _{i_{1}\dots i_{\ell }}$ must be trace free on every pair of indices. Thus as an irreducible representation of SO(3), **H***ℓ* is isomorphic to the space of traceless symmetric tensors of degree ℓ.

More generally, the analogous statements hold in higher dimensions: the space **H***ℓ* of spherical harmonics on the n-sphere is the irreducible representation of SO(*n*+1) corresponding to the traceless symmetric ℓ-tensors. However, whereas every irreducible tensor representation of SO(2) and SO(3) is of this kind, the special orthogonal groups in higher dimensions have additional irreducible representations that do not arise in this manner.

The special orthogonal groups have additional spin representations that are not tensor representations, and are *typically* not spherical harmonics. An exception are the spin representation of SO(3): strictly speaking these are representations of the double cover SU(2) of SO(3). In turn, SU(2) is identified with the group of unit quaternions, and so coincides with the 3-sphere. The spaces of spherical harmonics on the 3-sphere are certain spin representations of SO(3), with respect to the action by quaternionic multiplication.


## Connection with hemispherical harmonics

Spherical harmonics can be separated into two sets of functions. One is hemispherical harmonics (HSH), orthogonal and complete on hemisphere. Another is complementary hemispherical harmonics (CHSH).

### Generalizations

The angle-preserving symmetries of the two-sphere are described by the group of Möbius transformations PSL(2,**C**). With respect to this group, the sphere is equivalent to the usual Riemann sphere. The group PSL(2,**C**) is isomorphic to the (proper) Lorentz group, and its action on the two-sphere agrees with the action of the Lorentz group on the celestial sphere in Minkowski space. The analog of the spherical harmonics for the Lorentz group is given by the hypergeometric series; furthermore, the spherical harmonics can be re-expressed in terms of the hypergeometric series, as SO(3) = PSU(2) is a subgroup of PSL(2,**C**).

More generally, hypergeometric series can be generalized to describe the symmetries of any symmetric space; in particular, hypergeometric series can be developed for any Lie group.
