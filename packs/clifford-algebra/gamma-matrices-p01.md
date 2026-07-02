---
title: "Gamma matrices (part 1/2)"
source: https://en.wikipedia.org/wiki/Gamma_matrices
domain: clifford-algebra
license: CC-BY-SA-4.0
tags: clifford algebra, geometric algebra, spinor field, gamma matrices
fetched: 2026-07-02
part: 1/2
---

# Gamma matrices

In mathematical physics, the **gamma matrices**, $\ \left\{\gamma ^{0},\gamma ^{1},\gamma ^{2},\gamma ^{3}\right\}\ ,$ also called the **Dirac matrices**, are a set of conventional matrices with specific anticommutation relations that ensure they generate a matrix representation of the Clifford algebra $\ \mathrm {Cl} _{1,3}(\mathbb {R} )~.$ It is also possible to define higher-dimensional gamma matrices. When interpreted as the matrices of the action of a set of orthogonal basis vectors for contravariant vectors in Minkowski space, the column vectors on which the matrices act become a space of spinors, on which the Clifford algebra of spacetime acts. This in turn makes it possible to represent infinitesimal spatial rotations and Lorentz boosts. Spinors facilitate spacetime computations in general, and in particular are fundamental to the Dirac equation for relativistic spin ${\tfrac {\ 1\ }{2}}$ particles. Gamma matrices were introduced by Paul Dirac in 1928.

In the Dirac representation, the four contravariant gamma matrices are

${\begin{aligned}\gamma ^{0}\ &=~~{\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&-1&0\\0&0&0&-1\end{pmatrix}},&\gamma ^{1}&={\begin{pmatrix}0&0&0&1\\0&0&1&0\\0&-1&0&0\\-1&0&0&0\end{pmatrix}},\\\\\gamma ^{2}&=i\ {\begin{pmatrix}0&0&0&-1\\0&0&1&0\\0&1&0&0\\-1&0&0&0\end{pmatrix}},&\gamma ^{3}&={\begin{pmatrix}0&0&1&0\\0&0&0&-1\\-1&0&0&0\\0&1&0&0\end{pmatrix}}~.\end{aligned}}$

$\gamma ^{0}$ is the time-like, Hermitian matrix. The other three are space-like, anti-Hermitian matrices. More compactly, $\ \gamma ^{0}=\sigma ^{3}\otimes I_{2}\ ,$ and $\ \gamma ^{j}=i\sigma ^{2}\otimes \sigma ^{j}\ ,$ where $\ \otimes \$ denotes the Kronecker product and the $\ \sigma ^{j}\$ (for j = 1, 2, 3) denote the Pauli matrices.

In addition, for discussions of group theory the identity matrix (I) is sometimes included with the four gamma matrices, and there is an auxiliary, "fifth" traceless matrix used in conjunction with the regular gamma matrices

${\begin{aligned}\ I_{4}={\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}}\ ,\qquad \gamma ^{5}\equiv i\gamma ^{0}\gamma ^{1}\gamma ^{2}\gamma ^{3}={\begin{pmatrix}0&0&1&0\\0&0&0&1\\1&0&0&0\\0&1&0&0\end{pmatrix}}~.\end{aligned}}$

The "fifth matrix" $\ \gamma ^{5}\$ is not a proper member of the main set of four; it is used for separating nominal left and right chiral representations.

The gamma matrices have a group structure, the gamma group, that is shared by all matrix representations of the group, in any dimension, for any signature of the metric. For example, the 2×2 Pauli matrices are a set of "gamma" matrices in three dimensional space with metric of Euclidean signature (3, 0). In five spacetime dimensions, the four gammas, above, together with the fifth gamma-matrix to be presented below generate the Clifford algebra.


## Mathematical structure

The defining property for the gamma matrices to generate a Clifford algebra is the anticommutation relation

$\left\{\gamma ^{\mu },\gamma ^{\nu }\right\}=\gamma ^{\mu }\gamma ^{\nu }+\gamma ^{\nu }\gamma ^{\mu }=2\eta ^{\mu \nu }I_{4}\ ,$

where the curly brackets $\ \{,\}\$ represent the anticommutator, $\ \eta _{\mu \nu }\$ is the Minkowski metric with signature (+ − − −), and $I_{4}$ is the 4 × 4 identity matrix.

This defining property is more fundamental than the numerical values used in the specific representation of the gamma matrices. Covariant gamma matrices are defined by

$\ \gamma _{\mu }=\eta _{\mu \nu }\gamma ^{\nu }=\left\{\gamma ^{0},-\gamma ^{1},-\gamma ^{2},-\gamma ^{3}\right\}\ ,$

and Einstein notation is assumed.

Note that the other sign convention for the metric, (− + + +) necessitates either a change in the defining equation:

$\ \left\{\gamma ^{\mu },\gamma ^{\nu }\right\}=-2\eta ^{\mu \nu }I_{4}\$

or a multiplication of all gamma matrices by i , which of course changes their hermiticity properties detailed below. Under the alternative sign convention for the metric the covariant gamma matrices are then defined by

$\ \gamma _{\mu }=\eta _{\mu \nu }\gamma ^{\nu }=\left\{-\gamma ^{0},\gamma ^{1},\gamma ^{2},\gamma ^{3}\right\}~.$


## Physical structure

The Clifford algebra $\ \mathrm {Cl} _{1,3}(\mathbb {R} )\$ over spacetime V can be regarded as the set of real linear operators from *V* to itself, End(*V*), or more generally, when complexified to $\ \mathrm {Cl} _{1,3}(\mathbb {R} )_{\mathbb {C} }\ ,$ as the set of linear operators from any four-dimensional complex vector space to itself. More simply, given a basis for *V*, $\ \mathrm {Cl} _{1,3}(\mathbb {R} )_{\mathbb {C} }\$ is just the set of all 4×4 complex matrices, but endowed with a Clifford algebra structure. Spacetime is assumed to be endowed with the Minkowski metric ημν. A space of Dirac spinors, Ux , is also assumed at every point in spacetime, endowed with the Dirac spinor representation of the Lorentz group. The Dirac spinor fields Ψ of the Dirac equations, evaluated at any point x in spacetime, are elements of Ux (see below). The Clifford algebra is assumed to act on Ux as well (by matrix multiplication with column vectors Ψ(*x*) in Ux for all x). This will be the primary view of elements of $\ \mathrm {Cl} _{1,3}(\mathbb {R} )_{\mathbb {C} }\$ in this section.

For each linear transformation S of Ux, there is a transformation of End(*Ux*) given by *S E S*−1 for *E* in $\ \mathrm {Cl} _{1,3}(\mathbb {R} )_{\mathbb {C} }\approx \operatorname {End} (U_{x})~.$ If S belongs to a representation of the Lorentz group, then the induced action *E* ↦ *S E S*−1 will also belong to a representation of the Lorentz group, see Representation theory of the Lorentz group.

If S(Λ) is the Dirac spinor representation acting on Ux of an arbitrary Lorentz transformation Λ in the standard (4 vector) representation acting on *V*, then there is a corresponding operator on $\ \operatorname {End} \left(U_{x}\right)=\mathrm {Cl} _{1,3}\left(\mathbb {R} \right)_{\mathbb {C} }\$ given by the equation:

$\ \gamma ^{\mu }\ \mapsto \ S(\Lambda )\ \gamma ^{\mu }\ {S(\Lambda )}^{-1}={\left(\Lambda ^{-1}\right)^{\mu }}_{\nu }\ \gamma ^{\nu }={\Lambda _{\nu }}^{\mu }\ \gamma ^{\nu }\ ,$

showing that the quantity of γμ can be viewed as a *basis* of a representation space of the 4 vector representation of the Lorentz group sitting inside the Clifford algebra. The last identity can be recognized as the defining relationship for matrices belonging to an indefinite orthogonal group, which is $\ \eta \Lambda ^{\textsf {T}}\eta =\Lambda ^{-1}\ ,$ written in indexed notation. This means that quantities of the form

$a\!\!\!/\equiv a_{\mu }\gamma ^{\mu }$

should be treated as 4 vectors in manipulations. It also means that indices can be raised and lowered on the γ using the metric ημν as with any 4 vector. The notation is called the Feynman slash notation. The slash operation maps the basis eμ of V, or any 4 dimensional vector space, to basis vectors γμ. The transformation rule for slashed quantities is simply

${a\!\!\!/}^{\mu }\mapsto {\Lambda ^{\mu }}_{\nu }{a\!\!\!/}^{\nu }~.$

This is different from the transformation rule for the γμ, which are now treated as (fixed) basis vectors. The designation of the 4 tuple $\left(\gamma ^{\mu }\right)_{\mu =0}^{3}=\left(\gamma ^{0},\gamma ^{1},\gamma ^{2},\gamma ^{3}\right)$ as a 4 vector sometimes found in the literature is thus a slight misnomer. The latter transformation corresponds to an active transformation of the components of a slashed quantity in terms of the basis γμ, and the former to a passive transformation of the basis γμ itself.

The elements $\ \sigma ^{\mu \nu }=\gamma ^{\mu }\gamma ^{\nu }-\gamma ^{\nu }\gamma ^{\mu }\$ form a representation of the Lie algebra of the Lorentz group. This is a spin representation. When these matrices, and linear combinations of them, are exponentiated, they are Dirac spinor representations of the Lorentz group, e.g., the S(Λ) of above are of this form. The 6 dimensional space the *σμν* span is the representation space of a tensor representation of the Lorentz group. For the higher order elements of the Clifford algebra in general and their transformation rules, see the article Dirac algebra. The spin representation of the Lorentz group is encoded in the spin group Spin(1, 3) (for real, uncharged spinors) and in the complexified spin group Spin(1, 3) for charged (Dirac) spinors.


## Expressing the Dirac equation

In natural units, the Dirac equation may be written as

$\ \left(i\gamma ^{\mu }\partial _{\mu }-m\right)\psi =0\$

where $\ \psi \$ is a Dirac spinor.

Switching to Feynman notation, the Dirac equation is

$\ (i{\partial \!\!\!/}-m)\psi =0~.$


## The fifth "gamma" matrix, *γ*5

It is useful to define a product of the four gamma matrices as $\gamma ^{5}=\sigma _{1}\otimes I$ , so that

$\ \gamma ^{5}\equiv i\gamma ^{0}\gamma ^{1}\gamma ^{2}\gamma ^{3}={\begin{pmatrix}0&0&1&0\\0&0&0&1\\1&0&0&0\\0&1&0&0\end{pmatrix}}\qquad$

(in the Dirac basis).

Although $\ \gamma ^{5}\$ uses the letter gamma, it is not one of ***the*** gamma matrices of $\ \mathrm {Cl} _{1,3}(\mathbb {R} )~.$ The index number 5 is a relic of old notation: $\ \gamma ^{0}\$ used to be called " $\gamma ^{4}$ ".

$\ \gamma ^{5}\$ has also an alternative form:

$\ \gamma ^{5}={\tfrac {i}{4!}}\varepsilon ^{\mu \nu \alpha \beta }\gamma _{\mu }\gamma _{\nu }\gamma _{\alpha }\gamma _{\beta }\$

using the convention $\varepsilon _{0123}=1\ ,$ or

$\ \gamma ^{5}=-{\tfrac {i}{4!}}\varepsilon ^{\mu \nu \alpha \beta }\gamma _{\mu }\gamma _{\nu }\gamma _{\alpha }\gamma _{\beta }\$

using the convention $\varepsilon ^{0123}=1~.$ Proof:

This can be seen by exploiting the fact that all the four gamma matrices anticommute, so

$\gamma ^{0}\gamma ^{1}\gamma ^{2}\gamma ^{3}=\gamma ^{[0}\gamma ^{1}\gamma ^{2}\gamma ^{3]}={\tfrac {1}{4!}}\delta _{\mu \nu \varrho \sigma }^{0123}\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\varrho }\gamma ^{\sigma }\ ,$

where $\delta _{\mu \nu \varrho \sigma }^{\alpha \beta \gamma \delta }$ is the type (4,4) generalized Kronecker delta in 4 dimensions, in full antisymmetrization. If $\ \varepsilon _{\alpha \dots \beta }\$ denotes the Levi-Civita symbol in n dimensions, we can use the identity $\delta _{\mu \nu \varrho \sigma }^{\alpha \beta \gamma \delta }=-\varepsilon ^{\alpha \beta \gamma \delta }\varepsilon _{\mu \nu \varrho \sigma }$ . Then we get, using the convention $\ \varepsilon ^{0123}=1\ ,$

$\ \gamma ^{5}=i\gamma ^{0}\gamma ^{1}\gamma ^{2}\gamma ^{3}=-{\frac {i}{4!}}\varepsilon ^{0123}\varepsilon _{\mu \nu \varrho \sigma }\,\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\varrho }\gamma ^{\sigma }=-{\tfrac {i}{4!}}\varepsilon _{\mu \nu \varrho \sigma }\,\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\varrho }\gamma ^{\sigma }=-{\tfrac {i}{4!}}\varepsilon ^{\mu \nu \varrho \sigma }\,\gamma _{\mu }\gamma _{\nu }\gamma _{\varrho }\gamma _{\sigma }$

This matrix is useful in discussions of quantum mechanical chirality. For example, a Dirac field can be projected onto its left-handed and right-handed components by:

$\ \psi _{\mathrm {L} }={\frac {\ I-\gamma ^{5}\ }{2}}\ \psi ,\qquad \psi _{\mathrm {R} }={\frac {\ I+\gamma ^{5}\ }{2}}\ \psi ~.$

Some properties are:

- It is Hermitian: $\left(\gamma ^{5}\right)^{\dagger }=\gamma ^{5}~.$
- Its eigenvalues are ±1, because: $\left(\gamma ^{5}\right)^{2}=I_{4}~.$
- It anticommutes with the four gamma matrices: $\left\{\gamma ^{5},\gamma ^{\mu }\right\}=\gamma ^{5}\gamma ^{\mu }+\gamma ^{\mu }\gamma ^{5}=0~.$

In fact, $\ \psi _{\mathrm {L} }\$ and $\ \psi _{\mathrm {R} }\$ are eigenvectors of $\ \gamma ^{5}\$ since

$\gamma ^{5}\psi _{\mathrm {L} }={\frac {\ \gamma ^{5}-\left(\gamma ^{5}\right)^{2}\ }{2}}\psi =-\psi _{\mathrm {L} }\ ,$

and

$\gamma ^{5}\psi _{\mathrm {R} }={\frac {\ \gamma ^{5}+\left(\gamma ^{5}\right)^{2}\ }{2}}\psi =\psi _{\mathrm {R} }~.$

### Five dimensions

The Clifford algebra in odd dimensions behaves like *two* copies of the Clifford algebra of one less dimension, a left copy and a right copy. Thus, one can employ a bit of a trick to repurpose i *γ* 5 as one of the generators of the Clifford algebra in five dimensions. In this case, the set {*γ* 0, *γ* 1, *γ* 2, *γ* 3, *i γ* 5} therefore, by the last two properties (keeping in mind that *i* 2 ≡ −1) and those of the ‘old’ gammas, forms the basis of the Clifford algebra in 5 spacetime dimensions for the metric signature (1,4). . In metric signature (4,1), the set {*γ* 0, *γ* 1, *γ* 2, *γ* 3, *γ* 5} is used, where the *γ* *μ* are the appropriate ones for the (3,1) signature. This pattern is repeated for spacetime dimension 2*n* even and the next odd dimension 2*n* + 1 for all *n* ≥ 1. For more detail, see higher-dimensional gamma matrices.


## Identities

The following identities follow from the fundamental anticommutation relation, so they hold in any basis (although the last one depends on the sign choice for $\gamma ^{5}$ ).

### Miscellaneous identities

1. $\gamma ^{\mu }\gamma _{\mu }=4I_{4}$

| Proof |
|---|
| Take the standard anticommutation relation: $\left\{\gamma ^{\mu },\gamma ^{\nu }\right\}=\gamma ^{\mu }\gamma ^{\nu }+\gamma ^{\nu }\gamma ^{\mu }=2\eta ^{\mu \nu }I_{4}.$ One can make this situation look similar by using the metric $\eta$ : $\gamma ^{\mu }\gamma _{\mu }$ $=\gamma ^{\mu }\eta _{\mu \nu }\gamma ^{\nu }=\eta _{\mu \nu }\gamma ^{\mu }\gamma ^{\nu }$ $={\tfrac {1}{2}}\left(\eta _{\mu \nu }+\eta _{\nu \mu }\right)\gamma ^{\mu }\gamma ^{\nu }$ ( $\eta$ symmetric) $={\tfrac {1}{2}}\left(\eta _{\mu \nu }\gamma ^{\mu }\gamma ^{\nu }+\eta _{\nu \mu }\gamma ^{\mu }\gamma ^{\nu }\right)$ (expanding) $={\tfrac {1}{2}}\left(\eta _{\mu \nu }\gamma ^{\mu }\gamma ^{\nu }+\eta _{\mu \nu }\gamma ^{\nu }\gamma ^{\mu }\right)$ (relabeling term on right) $={\tfrac {1}{2}}\eta _{\mu \nu }\left\{\gamma ^{\mu },\gamma ^{\nu }\right\}$ $={\tfrac {1}{2}}\eta _{\mu \nu }\left(2\eta ^{\mu \nu }I_{4}\right)=\eta _{\mu \nu }\eta ^{\mu \nu }I_{4}=4I_{4}.$ |

2. $\gamma ^{\mu }\gamma ^{\nu }\gamma _{\mu }=-2\gamma ^{\nu }$

| Proof |
|---|
| Similarly to the proof of 1, again beginning with the standard anticommutation relation: ${\begin{aligned}\gamma ^{\mu }\gamma ^{\nu }\gamma _{\mu }&=\gamma ^{\mu }\left(2\eta _{\mu }^{\nu }I_{4}-\gamma _{\mu }\gamma ^{\nu }\right)\\&=2\gamma ^{\mu }\eta _{\mu }^{\nu }-\gamma ^{\mu }\gamma _{\mu }\gamma ^{\nu }\\&=2\gamma ^{\nu }-4\gamma ^{\nu }=-2\gamma ^{\nu }.\end{aligned}}$ |

3. $\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\rho }\gamma _{\mu }=4\eta ^{\nu \rho }I_{4}$

| Proof |
|---|
| To show $\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\rho }\gamma _{\mu }=4\eta ^{\nu \rho }I_{4}.$ Use the anticommutator to shift $\gamma ^{\mu }$ to the right $\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\rho }\gamma _{\mu }$ $=\left\{\gamma ^{\mu },\gamma ^{\nu }\right\}\gamma ^{\rho }\gamma _{\mu }-\gamma ^{\nu }\gamma ^{\mu }\gamma ^{\rho }\gamma _{\mu }$ $=2\ \eta ^{\mu \nu }\gamma ^{\rho }\gamma _{\mu }-\gamma ^{\nu }\left\{\gamma ^{\mu },\gamma ^{\rho }\right\}\gamma _{\mu }+\gamma ^{\nu }\gamma ^{\rho }\gamma ^{\mu }\gamma _{\mu }.$ Using the relation $\gamma ^{\mu }\gamma _{\mu }=4I$ we can contract the last two gammas, and get $\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\rho }\gamma _{\mu }$ $=2\gamma ^{\rho }\gamma ^{\nu }-\gamma ^{\nu }2\eta ^{\mu \rho }\gamma _{\mu }+4\gamma ^{\nu }\gamma ^{\rho }$ $=2\gamma ^{\rho }\gamma ^{\nu }-2\gamma ^{\nu }\gamma ^{\rho }+4\gamma ^{\nu }\gamma ^{\rho }$ $=2\left(\gamma ^{\rho }\gamma ^{\nu }+\gamma ^{\nu }\gamma ^{\rho }\right)$ $=2\left\{\gamma ^{\nu },\gamma ^{\rho }\right\}.$ Finally using the anticommutator identity, we get $\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\rho }\gamma _{\mu }=4\eta ^{\nu \rho }I_{4}.$ |

4. $\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\rho }\gamma ^{\sigma }\gamma _{\mu }=-2\gamma ^{\sigma }\gamma ^{\rho }\gamma ^{\nu }$

| Proof |
|---|
| $\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\rho }\gamma ^{\sigma }\gamma _{\mu }$ $=(2\eta ^{\mu \nu }-\gamma ^{\nu }\gamma ^{\mu })\gamma ^{\rho }\gamma ^{\sigma }\gamma _{\mu }\,$ (anticommutator identity) $=2\eta ^{\mu \nu }\gamma ^{\rho }\gamma ^{\sigma }\gamma _{\mu }-4\gamma ^{\nu }\eta ^{\rho \sigma }\,$ (using identity 3) $=2\gamma ^{\rho }\gamma ^{\sigma }\gamma ^{\nu }-4\gamma ^{\nu }\eta ^{\rho \sigma }$ (raising an index) $=2\left(2\eta ^{\rho \sigma }-\gamma ^{\sigma }\gamma ^{\rho }\right)\gamma ^{\nu }-4\gamma ^{\nu }\eta ^{\rho \sigma }$ (anticommutator identity) $=-2\gamma ^{\sigma }\gamma ^{\rho }\gamma ^{\nu }$ (2 terms cancel) |

5. $\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\rho }=\eta ^{\mu \nu }\gamma ^{\rho }+\eta ^{\nu \rho }\gamma ^{\mu }-\eta ^{\mu \rho }\gamma ^{\nu }-i\epsilon ^{\sigma \mu \nu \rho }\gamma _{\sigma }\gamma ^{5}$

| Proof |
|---|
| If $\mu =\nu =\rho$ then $\epsilon ^{\sigma \mu \nu \rho }=0$ and it is easy to verify the identity. That is the case also when $\mu =\nu \neq \rho$ , $\mu =\rho \neq \nu$ or $\nu =\rho \neq \mu$ . On the other hand, if all three indices are different, $\eta ^{\mu \nu }=0$ , $\eta ^{\mu \rho }=0$ and $\eta ^{\nu \rho }=0$ and both sides are completely antisymmetric; the left hand side because of the anticommutativity of the $\gamma$ matrices, and on the right hand side because of the antisymmetry of $\epsilon _{\sigma \mu \nu \rho }$ . It thus suffices to verify the identities for the cases of $\gamma ^{0}\gamma ^{1}\gamma ^{2}$ , $\gamma ^{0}\gamma ^{1}\gamma ^{3}$ , $\gamma ^{0}\gamma ^{2}\gamma ^{3}$ and $\gamma ^{1}\gamma ^{2}\gamma ^{3}$ . ${\begin{aligned}-i\epsilon ^{\sigma 012}\gamma _{\sigma }\gamma ^{5}&=-i\epsilon ^{3012}\left(-\gamma ^{3}\right)\left(i\gamma ^{0}\gamma ^{1}\gamma ^{2}\gamma ^{3}\right)=-\epsilon ^{3012}\gamma ^{0}\gamma ^{1}\gamma ^{2}=\epsilon ^{0123}\gamma ^{0}\gamma ^{1}\gamma ^{2}\\-i\epsilon ^{\sigma 013}\gamma _{\sigma }\gamma ^{5}&=-i\epsilon ^{2013}\left(-\gamma ^{2}\right)\left(i\gamma ^{0}\gamma ^{1}\gamma ^{2}\gamma ^{3}\right)=\epsilon ^{2013}\gamma ^{0}\gamma ^{1}\gamma ^{3}=\epsilon ^{0123}\gamma ^{0}\gamma ^{1}\gamma ^{3}\\-i\epsilon ^{\sigma 023}\gamma _{\sigma }\gamma ^{5}&=-i\epsilon ^{1023}\left(-\gamma ^{1}\right)\left(i\gamma ^{0}\gamma ^{1}\gamma ^{2}\gamma ^{3}\right)=-\epsilon ^{1023}\gamma ^{0}\gamma ^{2}\gamma ^{3}=\epsilon ^{0123}\gamma ^{0}\gamma ^{2}\gamma ^{3}\\-i\epsilon ^{\sigma 123}\gamma _{\sigma }\gamma ^{5}&=-i\epsilon ^{0123}\left(\gamma ^{0}\right)\left(i\gamma ^{0}\gamma ^{1}\gamma ^{2}\gamma ^{3}\right)=\epsilon ^{0123}\gamma ^{1}\gamma ^{2}\gamma ^{3}\end{aligned}}$ |

6. $\gamma ^{5}\sigma ^{\nu \rho }={\tfrac {i}{2}}\epsilon ^{\sigma \mu \nu \rho }\sigma _{\sigma \mu }\ ,$ where $\ \sigma _{\mu \nu }={\tfrac {i}{2}}[\gamma _{\mu },\gamma _{\nu }]={\tfrac {i}{2}}(\gamma _{\mu }\gamma _{\nu }-\gamma _{\nu }\gamma _{\mu })\$

| Proof |
|---|
| For $\ \nu =\rho \ ,$ $\ \epsilon ^{\sigma \mu \nu \rho }=0\$ and both sides vanish. Otherwise, multiplying identity 5 by $\ \gamma _{\mu }\$ from the right gives that $\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\rho }\gamma _{\mu }$ $=\eta ^{\mu \nu }\gamma ^{\rho }\gamma _{\mu }+\eta ^{\nu \rho }\gamma ^{\mu }\gamma _{\mu }-\eta ^{\mu \rho }\gamma ^{\nu }\gamma _{\mu }-i\epsilon ^{\sigma \mu \nu \rho }\gamma _{\sigma }\gamma ^{5}\gamma _{\mu }\,$ $=\gamma ^{\rho }\gamma ^{\nu }+4\eta ^{\nu \rho }I_{4}-\gamma ^{\nu }\gamma ^{\rho }-i\epsilon ^{\sigma \mu \nu \rho }\gamma _{\sigma }\gamma ^{5}\gamma _{\mu }\,$ (raising indices and using identity 1) where $4\eta ^{\nu \rho }I_{4}=0$ since $\nu \neq \rho$ . The left hand side of this equation also vanishes since $\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\rho }\gamma _{\mu }=4\eta ^{\nu \rho }I_{4}$ by property 3. Rearranging gives that $\gamma ^{\rho }\gamma ^{\nu }-\gamma ^{\nu }\gamma ^{\rho }$ $=i\epsilon ^{\sigma \mu \nu \rho }\gamma _{\sigma }\gamma ^{5}\gamma _{\mu }\,$ $=-i\epsilon ^{\sigma \mu \nu \rho }\gamma ^{5}\gamma _{\sigma }\gamma _{\mu }\,$ (since $\gamma ^{5}$ anticommutes with the gamma matrices) Note that $2\gamma _{\sigma }\gamma _{\mu }=\gamma _{\sigma }\gamma _{\mu }-\gamma _{\mu }\gamma _{\sigma }=[\gamma _{\sigma },\gamma _{\mu }]$ for $\sigma \neq \mu$ (for $\sigma =\mu$ , $\epsilon ^{\sigma \mu \nu \rho }$ vanishes) by the standard anticommutation relation. It follows that $-[\gamma ^{\nu },\gamma ^{\rho }]$ $=-{\tfrac {i}{2}}\epsilon ^{\sigma \mu \nu \rho }\gamma ^{5}[\gamma _{\sigma },\gamma _{\mu }]\,$ Multiplying from the left times $\ -{\tfrac {i}{2}}\gamma ^{5}\$ and using that $\ (\gamma ^{5})^{2}=I_{4}\$ yields the desired result. |

### Trace identities

The gamma matrices obey the following trace identities:

1. $\operatorname {tr} \left(\gamma ^{\mu }\right)=0$
2. Trace of any product of an odd number of $\gamma ^{\mu }$ is zero
3. Trace of $\gamma ^{5}$ times a product of an odd number of $\gamma ^{\mu }$ is still zero
4. $\operatorname {tr} \left(\gamma ^{\mu }\gamma ^{\nu }\right)=4\eta ^{\mu \nu }$
5. $\operatorname {tr} \left(\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\rho }\gamma ^{\sigma }\right)=4\left(\eta ^{\mu \nu }\eta ^{\rho \sigma }-\eta ^{\mu \rho }\eta ^{\nu \sigma }+\eta ^{\mu \sigma }\eta ^{\nu \rho }\right)$
6. $\operatorname {tr} \left(\gamma ^{5}\right)=\operatorname {tr} \left(\gamma ^{\mu }\gamma ^{\nu }\gamma ^{5}\right)=0$
7. $\operatorname {tr} \left(\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\rho }\gamma ^{\sigma }\gamma ^{5}\right)=-4i\epsilon ^{\mu \nu \rho \sigma }$
8. $\operatorname {tr} \left(\gamma ^{\mu _{1}}\dots \gamma ^{\mu _{n}}\right)=\operatorname {tr} \left(\gamma ^{\mu _{n}}\dots \gamma ^{\mu _{1}}\right)$

Proving the above involves the use of three main properties of the trace operator:

- $\operatorname {tr} (A+B)=\operatorname {tr} (A)+\operatorname {tr} (B)$
- $\operatorname {tr} (rA)=r\cdot \operatorname {tr} (A)$
- $\operatorname {tr} (ABC)=\operatorname {tr} (BCA)=\operatorname {tr} (CAB)$

| Proof of 1 |
|---|
| From the definition of the gamma matrices, $\gamma ^{\mu }\gamma ^{\nu }+\gamma ^{\nu }\gamma ^{\mu }=2\eta ^{\mu \nu }I$ We get $\gamma ^{\mu }\gamma ^{\mu }=\eta ^{\mu \mu }I$ or equivalently, ${\frac {\ \gamma ^{\mu }\gamma ^{\mu }\ }{\ \eta ^{\mu \mu }\ }}=I\$ where $\ \eta ^{\mu \mu }\$ is a number, and $\ \gamma ^{\mu }\gamma ^{\mu }\$ is a matrix. $\operatorname {tr} (\gamma ^{\nu })={\frac {1}{\eta ^{\mu \mu }}}\operatorname {tr} (\gamma ^{\nu }\gamma ^{\mu }\gamma ^{\mu })$ (inserting the identity and using tr(*r*A) = *r* tr(A) .) $=-{\frac {1}{\eta ^{\mu \mu }}}\operatorname {tr} (\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\mu })$ (from anti-commutation relation, and given that we are free to select $\mu \neq \nu$ ) $=-{\frac {1}{\eta ^{\mu \mu }}}\operatorname {tr} (\gamma ^{\nu }\gamma ^{\mu }\gamma ^{\mu })$ (using tr(ABC) = tr(BCA)) $=-\operatorname {tr} (\gamma ^{\nu })$ (removing the identity) This implies $\operatorname {tr} (\gamma ^{\nu })=0$ |

| Proof of 2 |
|---|
| To show $\operatorname {tr} ({\text{odd num of }}\gamma )=0$ First note that $\operatorname {tr} \left(\gamma ^{\mu }\right)=0.$ We'll also use two facts about the fifth gamma matrix $\gamma ^{5}$ that say: $\left(\gamma ^{5}\right)^{2}=I_{4},\quad \mathrm {and} \quad \gamma ^{\mu }\gamma ^{5}=-\gamma ^{5}\gamma ^{\mu }$ So let's use these two facts to prove this identity for the first non-trivial case: the trace of three gamma matrices. Step one is to put in one pair of $\gamma ^{5}$ 's in front of the three original $\gamma$ 's, and step two is to swap the $\gamma ^{5}$ matrix back to the original position, after making use of the cyclicity of the trace. $\operatorname {tr} \left(\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\rho }\right)$ $=\operatorname {tr} \left(\gamma ^{5}\gamma ^{5}\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\rho }\right)$ $=\operatorname {tr} \left(\gamma ^{5}\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\rho }\gamma ^{5}\right)$ (using tr(ABC) = tr(BCA)) $=-\operatorname {tr} \left(\gamma ^{5}\gamma ^{5}\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\rho }\right)$ (anticommuting $\gamma ^{5}$ three times) $=-\operatorname {tr} \left(\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\rho }\right)$ This can only be fulfilled if $\operatorname {tr} \left(\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\rho }\right)=0$ The extension to 2n + 1 (n integer) gamma matrices is found by placing two gamma-5s after (say) the 2n-th gamma-matrix in the trace, commuting one out to the right (giving a minus sign) and commuting the other gamma-5 2n steps out to the left [with sign change (-1)^2n = 1]. Then we use cyclic identity to get the two gamma-5s together, and hence they square to identity, leaving us with the trace equalling minus itself, i.e., 0. |

| Proof of 3 |
|---|
| If an odd number of gamma matrices appear in a trace followed by $\gamma ^{5}$ , our goal is to move $\gamma ^{5}$ from the right side to the left. This will leave the trace invariant by the cyclic property. In order to do this move, we must anticommute it with all of the other gamma matrices. This means that we anticommute it an odd number of times and pick up a minus sign. A trace equal to the negative of itself must be zero. |

| Proof of 4 |
|---|
| To show $\operatorname {tr} \left(\gamma ^{\mu }\gamma ^{\nu }\right)=4\eta ^{\mu \nu }$ Begin with, $\operatorname {tr} (\gamma ^{\mu }\gamma ^{\nu })$ $={\tfrac {1}{2}}\left(\operatorname {tr} \left(\gamma ^{\mu }\gamma ^{\nu }\right)+\operatorname {tr} \left(\gamma ^{\nu }\gamma ^{\mu }\right)\right)$ $={\tfrac {1}{2}}\operatorname {tr} \left(\gamma ^{\mu }\gamma ^{\nu }+\gamma ^{\nu }\gamma ^{\mu }\right)={\frac {1}{2}}\operatorname {tr} \left(\left\{\gamma ^{\mu },\gamma ^{\nu }\right\}\right)$ $={\tfrac {1}{2}}2\eta ^{\mu \nu }\operatorname {tr} (I_{4})=4\eta ^{\mu \nu }$ |

| Proof of 5 |
|---|
| $\operatorname {tr} \left(\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\rho }\gamma ^{\sigma }\right)$ $=\operatorname {tr} \left(\gamma ^{\mu }\gamma ^{\nu }\left(2\eta ^{\rho \sigma }-\gamma ^{\sigma }\gamma ^{\rho }\right)\right)$ $=2\eta ^{\rho \sigma }\operatorname {tr} \left(\gamma ^{\mu }\gamma ^{\nu }\right)-\operatorname {tr} \left(\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\sigma }\gamma ^{\rho }\right)\quad \quad (1)$ For the term on the right, we'll continue the pattern of swapping $\gamma ^{\sigma }$ with its neighbor to the left, $\operatorname {tr} \left(\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\sigma }\gamma ^{\rho }\right)$ $=\operatorname {tr} \left(\gamma ^{\mu }\left(2\eta ^{\nu \sigma }-\gamma ^{\sigma }\gamma ^{\nu }\right)\gamma ^{\rho }\right)$ $=2\eta ^{\nu \sigma }\operatorname {tr} \left(\gamma ^{\mu }\gamma ^{\rho }\right)-\operatorname {tr} \left(\gamma ^{\mu }\gamma ^{\sigma }\gamma ^{\nu }\gamma ^{\rho }\right)\quad \quad (2)$ Again, for the term on the right swap $\gamma ^{\sigma }$ with its neighbor to the left, $\operatorname {tr} \left(\gamma ^{\mu }\gamma ^{\sigma }\gamma ^{\nu }\gamma ^{\rho }\right)$ $=\operatorname {tr} \left(\left(2\eta ^{\mu \sigma }-\gamma ^{\sigma }\gamma ^{\mu }\right)\gamma ^{\nu }\gamma ^{\rho }\right)$ $=2\eta ^{\mu \sigma }\operatorname {tr} \left(\gamma ^{\nu }\gamma ^{\rho }\right)-\operatorname {tr} \left(\gamma ^{\sigma }\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\rho }\right)\quad \quad (3)$ Eq (3) is the term on the right of eq (2), and eq (2) is the term on the right of eq (1). We'll also use identity number 3 to simplify terms like so: $2\eta ^{\rho \sigma }\operatorname {tr} \left(\gamma ^{\mu }\gamma ^{\nu }\right)=2\eta ^{\rho \sigma }\left(4\eta ^{\mu \nu }\right)=8\eta ^{\rho \sigma }\eta ^{\mu \nu }.$ So finally Eq (1), when you plug all this information in gives $\operatorname {tr} \left(\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\rho }\gamma ^{\sigma }\right)=8\eta ^{\rho \sigma }\eta ^{\mu \nu }-8\eta ^{\nu \sigma }\eta ^{\mu \rho }+8\eta ^{\mu \sigma }\eta ^{\nu \rho }$ $-\ \operatorname {tr} \left(\gamma ^{\sigma }\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\rho }\right)\quad \quad \quad \quad \quad \quad (4)$ The terms inside the trace can be cycled, so $\operatorname {tr} \left(\gamma ^{\sigma }\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\rho }\right)=\operatorname {tr} \left(\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\rho }\gamma ^{\sigma }\right).$ So really (4) is $2\ \operatorname {tr} \left(\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\rho }\gamma ^{\sigma }\right)=8\eta ^{\rho \sigma }\eta ^{\mu \nu }-8\eta ^{\nu \sigma }\eta ^{\mu \rho }+8\eta ^{\mu \sigma }\eta ^{\nu \rho }$ or $\operatorname {tr} \left(\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\rho }\gamma ^{\sigma }\right)=4\left(\eta ^{\rho \sigma }\eta ^{\mu \nu }-\eta ^{\nu \sigma }\eta ^{\mu \rho }+\eta ^{\mu \sigma }\eta ^{\nu \rho }\right)$ |

| Proof of 6 |
|---|
| To show $\operatorname {tr} \left(\gamma ^{5}\right)=0$ , begin with $\operatorname {tr} \left(\gamma ^{5}\right)$ $=\operatorname {tr} \left(\gamma ^{0}\gamma ^{0}\gamma ^{5}\right)$ (because $\gamma ^{0}\gamma ^{0}=I_{4}$ ) $=-\operatorname {tr} \left(\gamma ^{0}\gamma ^{5}\gamma ^{0}\right)$ (anti-commute the $\gamma ^{5}$ with $\gamma ^{0}$ ) $=-\operatorname {tr} \left(\gamma ^{0}\gamma ^{0}\gamma ^{5}\right)$ (rotate terms within trace) $=-\operatorname {tr} \left(\gamma ^{5}\right)$ (remove $\gamma ^{0}$ 's) Add $\operatorname {tr} \left(\gamma ^{5}\right)$ to both sides of the above to see $2\operatorname {tr} \left(\gamma ^{5}\right)=0$ . Now, this pattern can also be used to show $\operatorname {tr} \left(\gamma ^{\mu }\gamma ^{\nu }\gamma ^{5}\right)=0$ . Simply add two factors of $\gamma ^{\alpha }$ , with $\alpha$ different from $\mu$ and $\nu$ . Anticommute three times instead of once, picking up three minus signs, and cycle using the cyclic property of the trace. So, $\operatorname {tr} \left(\gamma ^{\mu }\gamma ^{\nu }\gamma ^{5}\right)=0$ . |

| Proof of 7 |
|---|
| For a proof of identity 7, the same trick still works unless $\left(\mu \nu \rho \sigma \right)$ is some permutation of (0123), so that all 4 gammas appear. The anticommutation rules imply that interchanging two of the indices changes the sign of the trace, so $\operatorname {tr} \left(\gamma ^{\mu }\gamma ^{\nu }\gamma ^{\rho }\gamma ^{\sigma }\gamma ^{5}\right)$ must be proportional to $\epsilon ^{\mu \nu \rho \sigma }$ $\left(\epsilon ^{0123}=\eta ^{0\mu }\eta ^{1\nu }\eta ^{2\rho }\eta ^{3\sigma }\epsilon _{\mu \nu \rho \sigma }=\eta ^{00}\eta ^{11}\eta ^{22}\eta ^{33}\epsilon _{0123}=-1\right)$ . The proportionality constant is $4i$ , as can be checked by plugging in $(\mu \nu \rho \sigma )=(0123)$ , writing out $\gamma ^{5}$ , and remembering that the trace of the identity is 4. |

| Proof of 8 |
|---|
| Denote the product of n gamma matrices by $\Gamma =\gamma ^{\mu 1}\gamma ^{\mu 2}\dots \gamma ^{\mu n}.$ Consider the Hermitian conjugate of $\Gamma$ : $\Gamma ^{\dagger }$ $=\gamma ^{\mu n\dagger }\dots \gamma ^{\mu 2\dagger }\gamma ^{\mu 1\dagger }$ $=\gamma ^{0}\gamma ^{\mu n}\gamma ^{0}\dots \gamma ^{0}\gamma ^{\mu 2}\gamma ^{0}\gamma ^{0}\gamma ^{\mu 1}\gamma ^{0}$ (since conjugating a gamma matrix with $\gamma ^{0}$ produces its Hermitian conjugate as described below) $=\gamma ^{0}\gamma ^{\mu n}\dots \gamma ^{\mu 2}\gamma ^{\mu 1}\gamma ^{0}$ (all $\gamma ^{0}$ s except the first and the last drop out) Conjugating with $\gamma ^{0}$ one more time to get rid of the two $\gamma ^{0}$ s that are there, we see that $\gamma ^{0}\Gamma ^{\dagger }\gamma ^{0}$ is the reverse of $\Gamma$ . Now, $\operatorname {tr} \left(\gamma ^{0}\Gamma ^{\dagger }\gamma ^{0}\right)$ $=\operatorname {tr} \left(\Gamma ^{\dagger }\right)$ (since trace is invariant under similarity transformations) $=\operatorname {tr} \left(\Gamma ^{*}\right)$ (since trace is invariant under transposition) $=\operatorname {tr} \left(\Gamma \right)$ (since the trace of a product of gamma matrices is real) |

### Normalization

The gamma matrices can be chosen with extra hermiticity conditions which are restricted by the above anticommutation relations however. We can impose

$\left(\gamma ^{0}\right)^{\dagger }=\gamma ^{0}$

, compatible with

$\left(\gamma ^{0}\right)^{2}=I_{4}$

and for the other gamma matrices (for *k* = 1, 2, 3)

$\left(\gamma ^{k}\right)^{\dagger }=-\gamma ^{k}$

, compatible with

$\left(\gamma ^{k}\right)^{2}=-I_{4}.$

One checks immediately that these hermiticity relations hold for the Dirac representation.

The above conditions can be combined in the relation

$\left(\gamma ^{\mu }\right)^{\dagger }=\gamma ^{0}\gamma ^{\mu }\gamma ^{0}.$

The hermiticity conditions are not invariant under the action $\gamma ^{\mu }\to S(\Lambda )\gamma ^{\mu }{S(\Lambda )}^{-1}$ of a Lorentz transformation $\Lambda$ because $S(\Lambda )$ is not necessarily a unitary transformation due to the non-compactness of the Lorentz group.

### Charge conjugation

The charge conjugation operator, in any basis, may be defined as

$C\gamma _{\mu }C^{-1}=-(\gamma _{\mu })^{\textsf {T}}$

where $(\cdot )^{\textsf {T}}$ denotes the matrix transpose. The explicit form that C takes is dependent on the specific representation chosen for the gamma matrices, up to an arbitrary phase factor. This is because although charge conjugation is an automorphism of the gamma group, it is *not* an inner automorphism (of the group). Conjugating matrices can be found, but they are representation-dependent.

Representation-independent identities include:

${\begin{aligned}C\gamma _{5}C^{-1}&=+(\gamma _{5})^{\textsf {T}}\\C\sigma _{\mu \nu }C^{-1}&=-(\sigma _{\mu \nu })^{\textsf {T}}\\C\gamma _{5}\gamma _{\mu }C^{-1}&=+(\gamma _{5}\gamma _{\mu })^{\textsf {T}}\\\end{aligned}}$

The charge conjugation operator is also unitary $C^{-1}=C^{\dagger }$ , while for $\mathrm {Cl} _{1,3}(\mathbb {R} )$ it also holds that $C^{\textsf {T}}=-C$ for any representation. Given a representation of gamma matrices, the arbitrary phase factor for the charge conjugation operator can not always be chosen such that $C^{\dagger }=C^{\textsf {T}}$ , as is the case for the common four representations given below, known as Dirac, chiral and Majorana representation.

### Feynman slash notation

The Feynman slash notation is defined by

${a\!\!\!/}:=\gamma ^{\mu }a_{\mu }$

for any 4-vector a .

Here are some similar identities to the ones above, but involving slash notation:

- ${a\!\!\!/}{b\!\!\!/}=\left[a\cdot b\right]I_{4}-ia_{\mu }\sigma ^{\mu \nu }b_{\nu }$
- ${a\!\!\!/}{a\!\!\!/}=a^{\mu }a^{\nu }\gamma _{\mu }\gamma _{\nu }={\tfrac {1}{2}}a^{\mu }a^{\nu }\left(\gamma _{\mu }\gamma _{\nu }+\gamma _{\nu }\gamma _{\mu }\right)=\left[\eta _{\mu \nu }a^{\mu }a^{\nu }\right]I_{4}=a^{2}I_{4}$
- $\operatorname {tr} \left({a\!\!\!/}{b\!\!\!/}\right)=4(a\cdot b)$
- $\operatorname {tr} \left({a\!\!\!/}{b\!\!\!/}{c\!\!\!/}{d\!\!\!/}\right)=4\left[(a\cdot b)(c\cdot d)-(a\cdot c)(b\cdot d)+(a\cdot d)(b\cdot c)\right]$
- $\operatorname {tr} \left(\gamma _{5}{a\!\!\!/}{b\!\!\!/}\right)=0$
- $\operatorname {tr} \left(\gamma _{5}{a\!\!\!/}{b\!\!\!/}{c\!\!\!/}{d\!\!\!/}\right)=-4i\epsilon _{\mu \nu \rho \sigma }a^{\mu }b^{\nu }c^{\rho }d^{\sigma }$
- $\gamma _{\mu }{a\!\!\!/}\gamma ^{\mu }=-2{a\!\!\!/}$
- $\gamma _{\mu }{a\!\!\!/}{b\!\!\!/}\gamma ^{\mu }=4(a\cdot b)I_{4}$
- $\gamma _{\mu }{a\!\!\!/}{b\!\!\!/}{c\!\!\!/}\gamma ^{\mu }=-2{c\!\!\!/}{b\!\!\!/}{a\!\!\!/}$ where $\epsilon _{\mu \nu \rho \sigma }$ is the Levi-Civita symbol and $\sigma ^{\mu \nu }={\tfrac {i}{2}}\left[\gamma ^{\mu },\gamma ^{\nu }\right]~.$ Actually traces of products of odd number of $\ \gamma \$ is zero and thus
- $\operatorname {tr} (a_{1}\!\!\!\!\!\!/\,\,\,a_{2}\!\!\!\!\!\!/\,\,\,\cdots a_{n}\!\!\!\!\!\!/\,\,\,)=0\$ for n odd.

Many follow directly from expanding out the slash notation and contracting expressions of the form $\ a_{\mu }b_{\nu }c_{\rho }\ \ldots \$ with the appropriate identity in terms of gamma matrices.


## Other representations

The matrices are also sometimes written using the 2×2 identity matrix, $I_{2}$ , and

$\gamma ^{k}={\begin{pmatrix}0&\sigma ^{k}\\-\sigma ^{k}&0\end{pmatrix}}$

where *k* runs from 1 to 3 and the σk are Pauli matrices.

### Dirac basis

The gamma matrices we have written so far are appropriate for acting on Dirac spinors written in the *Dirac basis*; in fact, the Dirac basis is defined by these matrices. To summarize, in the Dirac basis:

$\gamma ^{0}={\begin{pmatrix}I_{2}&0\\0&-I_{2}\end{pmatrix}},\quad \gamma ^{k}={\begin{pmatrix}0&\sigma ^{k}\\-\sigma ^{k}&0\end{pmatrix}},\quad \gamma ^{5}={\begin{pmatrix}0&I_{2}\\I_{2}&0\end{pmatrix}}~.$

or using the Kronecker product:

$\gamma ^{0}=(\sigma ^{3}\otimes I_{2}),\quad \gamma ^{k}=(i\sigma ^{2}\otimes \sigma ^{k}),\quad \gamma ^{5}=(\sigma ^{1}\otimes I_{2})~.$

In the Dirac basis, the charge conjugation operator is real antisymmetric,

$C_{D}=i\gamma ^{2}\gamma ^{0}={\begin{pmatrix}0&-i\sigma ^{2}\\-i\sigma ^{2}&0\end{pmatrix}}={\begin{pmatrix}0&~~0&~~0&-1\\0&~~0&~~1&~~0\\0&-1&~~0&~~0\\1&~~0&~~0&~~0\end{pmatrix}}~.$

### Weyl (chiral) basis

Another common choice is the *Weyl* or *chiral basis*, in which $\gamma ^{k}$ remains the same but $\gamma ^{0}$ is different, and so $\gamma ^{5}$ is also different, and diagonal,

$\gamma ^{0}={\begin{pmatrix}0&I_{2}\\I_{2}&0\end{pmatrix}},\quad \gamma ^{k}={\begin{pmatrix}0&\sigma ^{k}\\-\sigma ^{k}&0\end{pmatrix}},\quad \gamma ^{5}={\begin{pmatrix}-I_{2}&0\\0&I_{2}\end{pmatrix}},$

or in more compact notation:

$\gamma ^{\mu }={\begin{pmatrix}0&\sigma ^{\mu }\\{\overline {\sigma }}^{\mu }&0\end{pmatrix}},\quad \sigma ^{\mu }\equiv (1,\sigma ^{i}),\quad {\overline {\sigma }}^{\mu }\equiv \left(1,-\sigma ^{i}\right).$

The Weyl basis has the advantage that its chiral projections take a simple form,

$\psi _{\mathrm {L} }={\tfrac {1}{2}}\left(1-\gamma ^{5}\right)\psi ={\begin{pmatrix}I_{2}&0\\0&0\end{pmatrix}}\psi ,\quad \psi _{\mathrm {R} }={\tfrac {1}{2}}\left(1+\gamma ^{5}\right)\psi ={\begin{pmatrix}0&0\\0&I_{2}\end{pmatrix}}\psi ~.$

The idempotence of the chiral projections is manifest.

By slightly abusing the notation and reusing the symbols $\psi _{\mathrm {L} /R}$ we can then identify

$\psi ={\begin{pmatrix}\psi _{\mathrm {L} }\\\psi _{\mathrm {R} }\end{pmatrix}},$

where now $\psi _{\mathrm {L} }$ and $\psi _{\mathrm {R} }$ are left-handed and right-handed two-component Weyl spinors.

The charge conjugation operator in this basis is real antisymmetric,

$C_{W}=UC_{D}U^{\text{T}}=i\gamma ^{2}\gamma ^{0}={\begin{pmatrix}i\sigma ^{2}&0\\0&-i\sigma ^{2}\end{pmatrix}}$

The Weyl basis can be obtained from the Dirac basis as

$\gamma _{\mathrm {W} }^{\mu }=U\gamma _{\mathrm {D} }^{\mu }U^{\dagger },\quad \psi _{\mathrm {W} }=U\psi _{\mathrm {D} }$

via the unitary transform

$U={\tfrac {1}{{\sqrt {2\ }}\ }}\left(1+\gamma ^{5}\gamma ^{0}\right)={\tfrac {1}{{\sqrt {2\ }}\ }}{\begin{pmatrix}I_{2}&-I_{2}\\I_{2}&I_{2}\end{pmatrix}}.$

### Weyl (chiral) basis (alternate form)

Another possible choice of the Weyl basis has

$\gamma ^{0}={\begin{pmatrix}0&-I_{2}\\-I_{2}&0\end{pmatrix}},\quad \gamma ^{k}={\begin{pmatrix}0&\sigma ^{k}\\-\sigma ^{k}&0\end{pmatrix}},\quad \gamma ^{5}={\begin{pmatrix}I_{2}&0\\0&-I_{2}\end{pmatrix}}.$

The chiral projections take a slightly different form from the other Weyl choice,

$\psi _{\mathrm {R} }={\begin{pmatrix}I_{2}&0\\0&0\end{pmatrix}}\psi ,\quad \psi _{\mathrm {L} }={\begin{pmatrix}0&0\\0&I_{2}\end{pmatrix}}\psi .$

In other words,

$\psi ={\begin{pmatrix}\psi _{\mathrm {R} }\\\psi _{\mathrm {L} }\end{pmatrix}},$

where $\psi _{\mathrm {L} }$ and $\psi _{\mathrm {R} }$ are the left-handed and right-handed two-component Weyl spinors, as before.

The charge conjugation operator in this basis is

$C=i\gamma ^{2}\gamma ^{0}={\begin{pmatrix}-i\sigma ^{2}&0\\0&i\sigma ^{2}\end{pmatrix}}={\begin{pmatrix}0&-1&~~0&~~0\\1&~~0&~~0&~~0\\0&~~0&~~0&~~1\\0&~~0&-1&~~0\\\end{pmatrix}}~=-i\sigma ^{3}\otimes \sigma ^{2}.$

This basis can be obtained from the Dirac basis above as $\gamma _{\mathrm {W} }^{\mu }=U\gamma _{\mathrm {D} }^{\mu }U^{\dagger },~~\psi _{\mathrm {W} }=U\psi _{\mathrm {D} }$ via the unitary transform

$U={\tfrac {1}{{\sqrt {2\ }}\ }}\left(1-\gamma ^{5}\gamma ^{0}\right)={\tfrac {1}{{\sqrt {2\ }}\ }}{\begin{pmatrix}~~I_{2}&I_{2}\\-I_{2}&I_{2}\end{pmatrix}}~.$

### Majorana basis

There is also the Majorana basis, in which all of the Dirac matrices are imaginary, and the spinors and Dirac equation are real. Using the Pauli matrices, the basis can be written as

${\begin{aligned}\gamma ^{0}&={\begin{pmatrix}0&\sigma ^{2}\\\sigma ^{2}&0\end{pmatrix}}\ ,~&\gamma ^{1}&={\begin{pmatrix}i\sigma ^{3}&0\\0&i\sigma ^{3}\end{pmatrix}}\ ,~&\gamma ^{2}&={\begin{pmatrix}0&-\sigma ^{2}\\\sigma ^{2}&0\end{pmatrix}},\\\gamma ^{3}&={\begin{pmatrix}-i\sigma ^{1}&0\\0&-i\sigma ^{1}\end{pmatrix}}\ ,~&\gamma ^{5}&={\begin{pmatrix}\sigma ^{2}&0\\0&-\sigma ^{2}\end{pmatrix}}\ ,~&C&={\begin{pmatrix}0&-i\sigma ^{2}\\-i\sigma ^{2}&0\end{pmatrix}}\ ,\end{aligned}}$

where C is the charge conjugation matrix, which matches the Dirac version defined above.

The reason for making all gamma matrices imaginary is solely to obtain the particle physics metric (+, −, −, −), in which squared masses are positive. The Majorana representation, however, is real. One can factor out the $\ i\$ to obtain a different representation with four component real spinors and real gamma matrices. The consequence of removing the $\ i\$ is that the only possible metric with real gamma matrices is (−, +, +, +).

The Majorana basis can be obtained from the Dirac basis above as $\gamma _{\mathrm {M} }^{\mu }=U\gamma _{\mathrm {D} }^{\mu }U^{\dagger },~~\psi _{\mathrm {M} }=U\psi _{\mathrm {D} }$ via the unitary transform

$U=U^{\dagger }={\tfrac {1}{{\sqrt {2\ }}\ }}{\begin{pmatrix}I_{2}&\sigma ^{2}\\\sigma ^{2}&-I_{2}\end{pmatrix}}~.$

### Cl1,3(C) and Cl1,3(R)

The Dirac algebra can be regarded as a complexification of the real algebra Cl1,3( $\mathbb {R}$ ), called the space time algebra:

$\mathrm {Cl} _{1,3}(\mathbb {C} )=\mathrm {Cl} _{1,3}(\mathbb {R} )\otimes \mathbb {C}$

Cl1,3( $\mathbb {R}$ ) differs from Cl1,3( $\mathbb {C}$ ): in Cl1,3( $\mathbb {R}$ ) only *real* linear combinations of the gamma matrices and their products are allowed.

Two things deserve to be pointed out. As *Clifford algebras*, Cl1,3( $\mathbb {C}$ ) and Cl4( $\mathbb {C}$ ) are isomorphic, see classification of Clifford algebras. The reason is that the underlying signature of the spacetime metric loses its signature (1,3) upon passing to the complexification. However, the transformation required to bring the bilinear form to the complex canonical form is not a Lorentz transformation and hence not "permissible" (at the very least impractical) since all physics is tightly knit to the Lorentz symmetry and it is preferable to keep it manifest.

Proponents of geometric algebra strive to work with real algebras wherever that is possible. They argue that it is generally possible (and usually enlightening) to identify the presence of an imaginary unit in a physical equation. Such units arise from one of the many quantities in a real Clifford algebra that square to −1, and these have geometric significance because of the properties of the algebra and the interaction of its various subspaces. Some of these proponents also question whether it is necessary or even useful to introduce an additional imaginary unit in the context of the Dirac equation.

In the mathematics of Riemannian geometry, it is conventional to define the Clifford algebra Clp,q( $\mathbb {R}$ ) for arbitrary dimensions p,q. The Weyl spinors transform under the action of the spin group $\mathrm {Spin} (n)$ . The complexification of the spin group, called the spinc group $\mathrm {Spin} ^{\mathbb {C} }(n)$ , is a product $\mathrm {Spin} (n)\times _{\mathbb {Z} _{2}}S^{1}$ of the spin group with the circle $S^{1}\cong U(1).$ The product $\times _{\mathbb {Z} _{2}}$ just a notational device to identify $(a,u)\in \mathrm {Spin} (n)\times S^{1}$ with $(-a,-u).$ The geometric point of this is that it disentangles the real spinor, which is covariant under Lorentz transformations, from the $U(1)$ component, which can be identified with the $\mathrm {U} (1)$ fiber of the electromagnetic interaction. The $\times _{\mathbb {Z} _{2}}$ is entangling parity and charge conjugation in a manner suitable for relating the Dirac particle/anti-particle states (equivalently, the chiral states in the Weyl basis). The Dirac spinor, insofar as it has linearly independent left and right components, can interact with the electromagnetic field. This is in contrast to the Majorana spinor and the ELKO spinor (Eigenspinoren des Ladungskonjugationsoperators), which cannot (*i.e.* they are electrically neutral), as they explicitly constrain the spinor so as to not interact with the $S^{1}$ part coming from the complexification. The ELKO spinor is a Lounesto class 5 spinor.

However, in contemporary practice in physics, the Dirac algebra rather than the space-time algebra continues to be the standard environment the spinors of the Dirac equation "live" in.
