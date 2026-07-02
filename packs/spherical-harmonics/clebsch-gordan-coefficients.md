---
title: "Clebsch–Gordan coefficients"
source: https://en.wikipedia.org/wiki/Clebsch%E2%80%93Gordan_coefficients
domain: spherical-harmonics
license: CC-BY-SA-4.0
tags: spherical harmonics, associated legendre polynomials, multipole expansion, wigner d-matrix
fetched: 2026-07-02
---

# Clebsch–Gordan coefficients

In physics, the **Clebsch–Gordan** (**CG**) **coefficients** are numbers that arise in angular momentum coupling in quantum mechanics. They appear as the expansion coefficients of total angular momentum eigenstates in an uncoupled tensor product basis. In more mathematical terms, the CG coefficients are used in representation theory, particularly of compact Lie groups, to perform the explicit direct sum decomposition of the tensor product of two irreducible representations (i.e., a reducible representation into irreducible representations, in cases where the numbers and types of irreducible components are already known abstractly). The name derives from the German mathematicians Alfred Clebsch and Paul Gordan, who encountered an equivalent problem in invariant theory.

From a vector calculus perspective, the CG coefficients associated with the SO(3) group can be defined simply in terms of integrals of products of spherical harmonics and their complex conjugates. The addition of spins in quantum-mechanical terms can be read directly from this approach as spherical harmonics are eigenfunctions of total angular momentum and projection thereof onto an axis, and the integrals correspond to the Hilbert space inner product. From the formal definition of angular momentum, recursion relations for the Clebsch–Gordan coefficients can be found. There also exist complicated explicit formulas for their direct calculation.

The formulas below use Dirac's bra–ket notation and the Condon–Shortley phase convention is adopted.

## Review of the angular momentum operators

Angular momentum operators are self-adjoint operators jx, jy, and jz that satisfy the commutation relations ${\begin{aligned}&[\mathrm {j} _{k},\mathrm {j} _{l}]\equiv \mathrm {j} _{k}\mathrm {j} _{l}-\mathrm {j} _{l}\mathrm {j} _{k}=i\hbar \varepsilon _{klm}\mathrm {j} _{m}&k,l,m&\in \{\mathrm {x,y,z} \},\end{aligned}}$ where *ε**klm* is the Levi-Civita symbol. Together the three operators define a *vector operator*, a rank one Cartesian tensor operator, $\mathbf {j} =(\mathrm {j_{x}} ,\mathrm {j_{y}} ,\mathrm {j_{z}} ).$ It is also known as a spherical vector, since it is also a spherical tensor operator. It is only for rank one that spherical tensor operators coincide with the Cartesian tensor operators.

By developing this concept further, one can define another operator **j**2 as the inner product of **j** with itself: $\mathbf {j} ^{2}=\mathrm {j_{x}^{2}} +\mathrm {j_{y}^{2}} +\mathrm {j_{z}^{2}} .$ This is an example of a Casimir operator. It is diagonal and its eigenvalue characterizes the particular irreducible representation of the angular momentum algebra ${\mathfrak {so}}(3,\mathbb {R} )\cong {\mathfrak {su}}(2)$ . This is physically interpreted as the square of the total angular momentum of the states on which the representation acts.

One can also define *raising* (j+) and *lowering* (j−) operators, the so-called ladder operators, $\mathrm {j_{\pm }} =\mathrm {j_{x}} \pm i\mathrm {j_{y}} .$

## Spherical basis for angular momentum eigenstates

It can be shown from the above definitions that **j**2 commutes with jx, jy, and jz: ${\begin{aligned}&[\mathbf {j} ^{2},\mathrm {j} _{k}]=0&k&\in \{\mathrm {x} ,\mathrm {y} ,\mathrm {z} \}.\end{aligned}}$

When two Hermitian operators commute, a common set of eigenstates exists. Conventionally, **j**2 and jz are chosen. From the commutation relations, the possible eigenvalues can be found. These eigenstates are denoted |*j* *m*⟩ where *j* is the *angular momentum quantum number* and *m* is the *angular momentum projection* onto the z-axis.

They comprise the spherical basis, are complete, and satisfy the following eigenvalue equations, ${\begin{aligned}\mathbf {j} ^{2}|j\,m\rangle &=\hbar ^{2}j(j+1)|j\,m\rangle ,&j&\in \{0,{\tfrac {1}{2}},1,{\tfrac {3}{2}},\ldots \}\\\mathrm {j_{z}} |j\,m\rangle &=\hbar m|j\,m\rangle ,&m&\in \{-j,-j+1,\ldots ,j\}.\end{aligned}}$

The raising and lowering operators can be used to alter the value of *m*, $\mathrm {j} _{\pm }|j\,m\rangle =\hbar C_{\pm }(j,m)|j\,(m\pm 1)\rangle ,$ where the ladder coefficient is given by:

| $C_{\pm }(j,m)={\sqrt {j(j+1)-m(m\pm 1)}}={\sqrt {(j\mp m)(j\pm m+1)}}.$ |   | 1 |
|---|---|---|

In principle, one may also introduce a (possibly complex) phase factor in the definition of $C_{\pm }(j,m)$ . The choice made in this article is in agreement with the Condon–Shortley phase convention. The angular momentum states are orthogonal (because their eigenvalues with respect to a Hermitian operator are distinct) and are assumed to be normalized, $\langle j\,m|j'\,m'\rangle =\delta _{j,j'}\delta _{m,m'}.$

Here the italicized *j* and *m* denote integer or half-integer angular momentum quantum numbers of a particle or of a system. On the other hand, the roman jx, jy, jz, j+, j−, and **j**2 denote operators. The $\delta$ symbols are Kronecker deltas.

## Tensor product space

We now consider systems with two physically different angular momenta *j*1 and *j*2. Examples include the spin and the orbital angular momentum of a single electron, or the spins of two electrons, or the orbital angular momenta of two electrons. Mathematically, this means that the angular momentum operators act on a space $V_{1}$ of dimension $2j_{1}+1$ and also on a space $V_{2}$ of dimension $2j_{2}+1$ . We are then going to define a family of "total angular momentum" operators acting on the tensor product space $V_{1}\otimes V_{2}$ , which has dimension $(2j_{1}+1)(2j_{2}+1)$ . The action of the total angular momentum operator on this space constitutes a representation of the SU(2) Lie algebra, but a reducible one. The reduction of this reducible representation into irreducible pieces is the goal of Clebsch–Gordan theory.

Let *V*1 be the (2 *j*1 + 1)-dimensional vector space spanned by the states ${\begin{aligned}&|j_{1}\,m_{1}\rangle ,&m_{1}&\in \{-j_{1},-j_{1}+1,\ldots ,j_{1}\}\end{aligned}},$ and *V*2 the (2 *j*2 + 1)-dimensional vector space spanned by the states ${\begin{aligned}&|j_{2}\,m_{2}\rangle ,&m_{2}&\in \{-j_{2},-j_{2}+1,\ldots ,j_{2}\}\end{aligned}}.$

The tensor product of these spaces, *V*3 ≡ *V*1 ⊗ *V*2, has a (2 *j*1 + 1) (2 *j*2 + 1)-dimensional *uncoupled* basis $|j_{1}\,m_{1}\,j_{2}\,m_{2}\rangle \equiv |j_{1}\,m_{1}\rangle \otimes |j_{2}\,m_{2}\rangle ,\quad m_{1}\in \{-j_{1},-j_{1}+1,\ldots ,j_{1}\},\quad m_{2}\in \{-j_{2},-j_{2}+1,\ldots ,j_{2}\}.$ Angular momentum operators are defined to act on states in *V*3 in the following manner: $(\mathbf {j} _{1}\otimes 1)|j_{1}\,m_{1}\,j_{2}\,m_{2}\rangle \equiv \mathbf {j} _{1}|j_{1}\,m_{1}\rangle \otimes |j_{2}\,m_{2}\rangle$ and $(1\otimes \mathrm {\mathbf {j} } _{2})|j_{1}\,m_{1}\,j_{2}\,m_{2}\rangle \equiv |j_{1}\,m_{1}\rangle \otimes \mathbf {j} _{2}|j_{2}\,m_{2}\rangle ,$ where 1 denotes the identity operator.

The **total** **angular momentum** operators are defined by the coproduct (or tensor product) of the two representations acting on *V*1⊗*V*2,

$\mathbf {J} \equiv \mathbf {j} _{1}\otimes 1+1\otimes \mathbf {j} _{2}~.$

The total angular momentum operators can be shown to *satisfy the very same commutation relations*, $[\mathrm {J} _{k},\mathrm {J} _{l}]=i\hbar \varepsilon _{klm}\mathrm {J} _{m}~,$ where *k*, *l*, *m* ∈ {*x*, *y*, *z*}. Indeed, the preceding construction is the standard method for constructing an action of a Lie algebra on a tensor product representation.

Hence, a set of *coupled* eigenstates exist for the total angular momentum operator as well, ${\begin{aligned}\mathbf {J} ^{2}|[j_{1}\,j_{2}]\,J\,M\rangle &=\hbar ^{2}J(J+1)|[j_{1}\,j_{2}]\,J\,M\rangle \\\mathrm {J_{z}} |[j_{1}\,j_{2}]\,J\,M\rangle &=\hbar M|[j_{1}\,j_{2}]\,J\,M\rangle \end{aligned}}$ for *M* ∈ {−*J*, −*J* + 1, ..., *J*}. Note that it is common to omit the [*j*1 *j*2] part.

The total angular momentum quantum number *J* must satisfy the triangular condition that $|j_{1}-j_{2}|\leq J\leq j_{1}+j_{2},$ such that the three nonnegative integer or half-integer values could correspond to the three sides of a triangle.

The total number of total angular momentum eigenstates is necessarily equal to the dimension of *V*3: $\sum _{J=|j_{1}-j_{2}|}^{j_{1}+j_{2}}(2J+1)=(2j_{1}+1)(2j_{2}+1)~.$ As this computation suggests, the tensor product representation decomposes as the direct sum of one copy of each of the irreducible representations of dimension $2J+1$ , where J ranges from $|j_{1}-j_{2}|$ to $j_{1}+j_{2}$ in increments of 1. As an example, consider the tensor product of the three-dimensional representation corresponding to $j_{1}=1$ with the two-dimensional representation with $j_{2}=1/2$ . The possible values of J are then $J=1/2$ and $J=3/2$ . Thus, the six-dimensional tensor product representation decomposes as the direct sum of a two-dimensional representation and a four-dimensional representation.

The goal is now to describe the preceding decomposition explicitly, that is, to explicitly describe basis elements in the tensor product space for each of the component representations that arise.

The total angular momentum states form an orthonormal basis of *V*3: $\left\langle J\,M|J'\,M'\right\rangle =\delta _{J,J'}\delta _{M,M'}~.$

These rules may be iterated to, e.g., combine n doublets (s=1/2) to obtain the Clebsch-Gordan decomposition series, (Catalan's triangle), $\mathbf {2} ^{\otimes n}=\bigoplus _{k=0}^{\lfloor n/2\rfloor }~\left({\frac {n+1-2k}{n+1}}{n+1 \choose k}\right)~(\mathbf {n} +\mathbf {1} -\mathbf {2} \mathbf {k} )~,$ where $\lfloor n/2\rfloor$ is the integer floor function; and the number preceding the boldface irreducible representation dimensionality (2*j*+1) label indicates multiplicity of that representation in the representation reduction. For instance, from this formula, addition of three spin 1/2s yields a spin 3/2 and two spin 1/2s, ${\mathbf {2} }\otimes {\mathbf {2} }\otimes {\mathbf {2} }={\mathbf {4} }\oplus {\mathbf {2} }\oplus {\mathbf {2} }$ .

## Formal definition of Clebsch–Gordan coefficients

The coupled states can be expanded via the completeness relation (resolution of identity) in the uncoupled basis

| $\|J\,M\rangle =\sum _{m_{1}=-j_{1}}^{j_{1}}\sum _{m_{2}=-j_{2}}^{j_{2}}\|j_{1}\,m_{1}\,j_{2}\,m_{2}\rangle \langle j_{1}\,m_{1}\,j_{2}\,m_{2}\|J\,M\rangle$ |   | 2 |
|---|---|---|

The expansion coefficients

$\langle j_{1}\,m_{1}\,j_{2}\,m_{2}|J\,M\rangle$

are the *Clebsch–Gordan coefficients*. Note that some authors write them in a different order such as ⟨*j*1 *j*2; *m*1 *m*2 | *J* *M*⟩. Another common notation is ⟨*j*1 *m*1 *j*2 *m*2 | *J* *M*⟩ = *C**JM* *j*1*m*1*j*2*m*2.

Applying the operators

${\begin{aligned}\mathrm {J} &=\mathrm {j} \otimes 1+1\otimes \mathrm {j} \\\mathrm {J} _{\mathrm {z} }&=\mathrm {j} _{\mathrm {z} }\otimes 1+1\otimes \mathrm {j} _{\mathrm {z} }\end{aligned}}$

to both sides of the defining equation shows that the Clebsch–Gordan coefficients can only be nonzero when

${\begin{aligned}|j_{1}-j_{2}|\leq J&\leq j_{1}+j_{2}\\M&=m_{1}+m_{2}.\end{aligned}}$

## Recursion relations

The recursion relations were discovered by physicist Giulio Racah from the Hebrew University of Jerusalem in 1941.

Applying the total angular momentum raising and lowering operators $\mathrm {J} _{\pm }=\mathrm {j} _{\pm }\otimes 1+1\otimes \mathrm {j} _{\pm }$ to the left hand side of the defining equation gives ${\begin{aligned}\mathrm {J} _{\pm }|[j_{1}\,j_{2}]\,J\,M\rangle &=\hbar C_{\pm }(J,M)|[j_{1}\,j_{2}]\,J\,(M\pm 1)\rangle \\&=\hbar C_{\pm }(J,M)\sum _{m_{1},m_{2}}|j_{1}\,m_{1}\,j_{2}\,m_{2}\rangle \langle j_{1}\,m_{1}\,j_{2}\,m_{2}|J\,(M\pm 1)\rangle \end{aligned}}$ Applying the same operators to the right hand side gives ${\begin{aligned}\mathrm {J} _{\pm }&\sum _{m_{1},m_{2}}|j_{1}\,m_{1}\,j_{2}\,m_{2}\rangle \langle j_{1}\,m_{1}\,j_{2}\,m_{2}|J\,M\rangle \\=\hbar &\sum _{m_{1},m_{2}}{\Bigl (}C_{\pm }(j_{1},m_{1})|j_{1}\,(m_{1}\pm 1)\,j_{2}\,m_{2}\rangle +C_{\pm }(j_{2},m_{2})|j_{1}\,m_{1}\,j_{2}\,(m_{2}\pm 1)\rangle {\Bigr )}\langle j_{1}\,m_{1}\,j_{2}\,m_{2}|J\,M\rangle \\=\hbar &\sum _{m_{1},m_{2}}|j_{1}\,m_{1}\,j_{2}\,m_{2}\rangle {\Bigl (}C_{\pm }(j_{1},m_{1}\mp 1)\langle j_{1}\,(m_{1}\mp 1)\,j_{2}\,m_{2}|J\,M\rangle +C_{\pm }(j_{2},m_{2}\mp 1)\langle j_{1}\,m_{1}\,j_{2}\,(m_{2}\mp 1)|J\,M\rangle {\Bigr )}.\end{aligned}}$

Combining these results gives recursion relations for the Clebsch–Gordan coefficients, where *C*± was defined in **1**: $C_{\pm }(J,M)\langle j_{1}\,m_{1}\,j_{2}\,m_{2}|J\,(M\pm 1)\rangle =C_{\pm }(j_{1},m_{1}\mp 1)\langle j_{1}\,(m_{1}\mp 1)\,j_{2}\,m_{2}|J\,M\rangle +C_{\pm }(j_{2},m_{2}\mp 1)\langle j_{1}\,m_{1}\,j_{2}\,(m_{2}\mp 1)|J\,M\rangle .$

Taking the upper sign with the condition that *M* = *J* gives initial recursion relation: $0=C_{+}(j_{1},m_{1}-1)\langle j_{1}\,(m_{1}-1)\,j_{2}\,m_{2}|J\,J\rangle +C_{+}(j_{2},m_{2}-1)\langle j_{1}\,m_{1}\,j_{2}\,(m_{2}-1)|J\,J\rangle .$ In the Condon–Shortley phase convention, one adds the constraint that

$\langle j_{1}\,j_{1}\,j_{2}\,(J-j_{1})|J\,J\rangle >0$

(and is therefore also real). The Clebsch–Gordan coefficients ⟨*j*1 *m*1 *j*2 *m*2 | *J* *M*⟩ can then be found from these recursion relations. The normalization is fixed by the requirement that the sum of the squares, which equivalent to the requirement that the norm of the state |[*j*1 *j*2] *J* *J*⟩ must be one.

The lower sign in the recursion relation can be used to find all the Clebsch–Gordan coefficients with *M* = *J* − 1. Repeated use of that equation gives all coefficients.

This procedure to find the Clebsch–Gordan coefficients shows that they are all real in the Condon–Shortley phase convention.

## Explicit expression

## Orthogonality relations

These are most clearly written down by introducing the alternative notation $\langle J\,M|j_{1}\,m_{1}\,j_{2}\,m_{2}\rangle \equiv \langle j_{1}\,m_{1}\,j_{2}\,m_{2}|J\,M\rangle$

The first orthogonality relation is $\sum _{J=|j_{1}-j_{2}|}^{j_{1}+j_{2}}\sum _{M=-J}^{J}\langle j_{1}\,m_{1}\,j_{2}\,m_{2}|J\,M\rangle \langle J\,M|j_{1}\,m_{1}'\,j_{2}\,m_{2}'\rangle =\langle j_{1}\,m_{1}\,j_{2}\,m_{2}|j_{1}\,m_{1}'\,j_{2}\,m_{2}'\rangle =\delta _{m_{1},m_{1}'}\delta _{m_{2},m_{2}'}$ (derived from the fact that ${\textstyle \mathbf {1} =\sum _{x}|x\rangle \langle x|}$ ) and the second one is $\sum _{m_{1},m_{2}}\langle J\,M|j_{1}\,m_{1}\,j_{2}\,m_{2}\rangle \langle j_{1}\,m_{1}\,j_{2}\,m_{2}|J'\,M'\rangle =\langle J\,M|J'\,M'\rangle =\delta _{J,J'}\delta _{M,M'}.$

## Special cases

For *J* = 0 the Clebsch–Gordan coefficients are given by $\langle j_{1}\,m_{1}\,j_{2}\,m_{2}|0\,0\rangle =\delta _{j_{1},j_{2}}\delta _{m_{1},-m_{2}}{\frac {(-1)^{j_{1}-m_{1}}}{\sqrt {2j_{1}+1}}}.$

For *J* = *j*1 + *j*2 and *M* = *J* we have $\langle j_{1}\,j_{1}\,j_{2}\,j_{2}|(j_{1}+j_{2})\,(j_{1}+j_{2})\rangle =1.$

For *j*1 = *j*2 = *J* / 2 and *m*1 = −*m*2 we have $\langle j_{1}\,m_{1}\,j_{1}\,(-m_{1})|(2j_{1})\,0\rangle ={\frac {(2j_{1})!^{2}}{(j_{1}-m_{1})!(j_{1}+m_{1})!{\sqrt {(4j_{1})!}}}}.$

For *j*1 = *j*2 = *m*1 = −*m*2 we have $\langle j_{1}\,j_{1}\,j_{1}\,(-j_{1})|J\,0\rangle =(2j_{1})!{\sqrt {\frac {2J+1}{(J+2j_{1}+1)!(2j_{1}-J)!}}}.$

For *j*2 = 1, *m*2 = 0 we have ${\begin{aligned}\langle j_{1}\,m\,1\,0|(j_{1}+1)\,m\rangle &={\sqrt {\frac {(j_{1}-m+1)(j_{1}+m+1)}{(2j_{1}+1)(j_{1}+1)}}}\\\langle j_{1}\,m\,1\,0|j_{1}\,m\rangle &={\frac {m}{\sqrt {j_{1}(j_{1}+1)}}}\\\langle j_{1}\,m\,1\,0|(j_{1}-1)\,m\rangle &=-{\sqrt {\frac {(j_{1}-m)(j_{1}+m)}{j_{1}(2j_{1}+1)}}}\end{aligned}}$

For *j*2 = 1/2 we have ${\begin{aligned}\left\langle j_{1}\,\left(M-{\frac {1}{2}}\right)\,{\frac {1}{2}}\,{\frac {1}{2}}{\Bigg |}\left(j_{1}\pm {\frac {1}{2}}\right)\,M\right\rangle &=\pm {\sqrt {{\frac {1}{2}}\left(1\pm {\frac {M}{j_{1}+{\frac {1}{2}}}}\right)}}\\\left\langle j_{1}\,\left(M+{\frac {1}{2}}\right)\,{\frac {1}{2}}\,\left(-{\frac {1}{2}}\right){\Bigg |}\left(j_{1}\pm {\frac {1}{2}}\right)\,M\right\rangle &={\sqrt {{\frac {1}{2}}\left(1\mp {\frac {M}{j_{1}+{\frac {1}{2}}}}\right)}}\end{aligned}}$

## Symmetry properties

${\begin{aligned}\langle j_{1}\,m_{1}\,j_{2}\,m_{2}|J\,M\rangle &=(-1)^{j_{1}+j_{2}-J}\langle j_{1}\,(-m_{1})\,j_{2}\,(-m_{2})|J\,(-M)\rangle \\&=(-1)^{j_{1}+j_{2}-J}\langle j_{2}\,m_{2}\,j_{1}\,m_{1}|J\,M\rangle \\&=(-1)^{j_{1}-m_{1}}{\sqrt {\frac {2J+1}{2j_{2}+1}}}\langle j_{1}\,m_{1}\,J\,(-M)|j_{2}\,(-m_{2})\rangle \\&=(-1)^{j_{2}+m_{2}}{\sqrt {\frac {2J+1}{2j_{1}+1}}}\langle J\,(-M)\,j_{2}\,m_{2}|j_{1}\,(-m_{1})\rangle \\&=(-1)^{j_{1}-m_{1}}{\sqrt {\frac {2J+1}{2j_{2}+1}}}\langle J\,M\,j_{1}\,(-m_{1})|j_{2}\,m_{2}\rangle \\&=(-1)^{j_{2}+m_{2}}{\sqrt {\frac {2J+1}{2j_{1}+1}}}\langle j_{2}\,(-m_{2})\,J\,M|j_{1}\,m_{1}\rangle \end{aligned}}$

A convenient way to derive these relations is by converting the Clebsch–Gordan coefficients to Wigner 3-j symbols using **3**. The symmetry properties of Wigner 3-j symbols are much simpler.

### Rules for phase factors

Care is needed when simplifying phase factors: a quantum number may be a half-integer rather than an integer, therefore (−1)2*k* is not necessarily 1 for a given quantum number *k* unless it can be proven to be an integer. Instead, it is replaced by the following weaker rule: $(-1)^{4k}=1$ for any angular-momentum-like quantum number *k*.

Nonetheless, a combination of *ji* and *mi* is always an integer, so the stronger rule applies for these combinations: $(-1)^{2(j_{i}-m_{i})}=1$ This identity also holds if the sign of either *ji* or *mi* or both is reversed.

It is useful to observe that any phase factor for a given (*ji*, *mi*) pair can be reduced to the canonical form: $(-1)^{aj_{i}+b(j_{i}-m_{i})}$ where *a* ∈ {0, 1, 2, 3} and *b* ∈ {0, 1} (other conventions are possible too). Converting phase factors into this form makes it easy to tell whether two phase factors are equivalent. (Note that this form is only *locally* canonical: it fails to take into account the rules that govern combinations of (*ji*, *mi*) pairs such as the one described in the next paragraph.)

An additional rule holds for combinations of *j*1, *j*2, and *j*3 that are related by a Clebsch-Gordan coefficient or Wigner 3-j symbol: $(-1)^{2(j_{1}+j_{2}+j_{3})}=1$ This identity also holds if the sign of any *ji* is reversed, or if any of them are substituted with an *mi* instead.

## Relation to Wigner 3-j symbols

Clebsch–Gordan coefficients are related to Wigner 3-j symbols which have more convenient symmetry relations.

| ${\begin{aligned}\langle j_{1}\,m_{1}\,j_{2}\,m_{2}\|J\,M\rangle &=(-1)^{-j_{1}+j_{2}-M}{\sqrt {2J+1}}{\begin{pmatrix}j_{1}&j_{2}&J\\m_{1}&m_{2}&-M\end{pmatrix}}\\&=(-1)^{2j_{2}}(-1)^{J-M}{\sqrt {2J+1}}{\begin{pmatrix}j_{1}&J&j_{2}\\m_{1}&-M&m_{2}\end{pmatrix}}\end{aligned}}$ |   | 3 |
|---|---|---|

The factor (−1)2 *j*2 is due to the Condon–Shortley constraint that ⟨*j*1 *j*1 *j*2 (*J* − *j*1)|*J J*⟩ > 0, while (−1)*J* − *M* is due to the time-reversed nature of |*J M*⟩.

This allows to reach the general expression:

${\begin{aligned}\langle j_{1}\,m_{1}\,j_{2}\,m_{2}|J\,M\rangle &\equiv \delta (m_{1}+m_{2},M){\sqrt {\frac {(2J+1)(j_{1}+j_{2}-J)!(j_{1}-j_{2}+J)!(-j_{1}+j_{2}+J)!}{(j_{1}+j_{2}+J+1)!}}}\ \times {}\\[6pt]&\times {\sqrt {(j_{1}-m_{1})!(j_{1}+m_{1})!(j_{2}-m_{2})!(j_{2}+m_{2})!(J-M)!(J+M)!}}\ \times {}\\[6pt]&\times \sum _{k=K}^{N}{\frac {(-1)^{k}}{k!(j_{1}+j_{2}-J-k)!(j_{1}-m_{1}-k)!(j_{2}+m_{2}-k)!(J-j_{2}+m_{1}+k)!(J-j_{1}-m_{2}+k)!}},\end{aligned}}.$

The summation is performed over those integer values k for which the argument of each factorial in the denominator is non-negative, i.e. summation limits K and N are taken equal: the lower one $K=\max(0,j_{2}-J-m_{1},j_{1}-J+m_{2}),$ the upper one $N=\min(j_{1}+j_{2}-J,j_{1}-m_{1},j_{2}+m_{2}).$ Factorials of negative numbers are conventionally taken equal to zero, so that the values of the 3*j* symbol at, for example, $j_{3}>j_{1}+j_{2}$ or $j_{1}<m_{1}$ are automatically set to zero.

## Relation to Wigner D-matrices

${\begin{aligned}&\int _{0}^{2\pi }d\alpha \int _{0}^{\pi }\sin \beta \,d\beta \int _{0}^{2\pi }d\gamma \,D_{M,K}^{J}(\alpha ,\beta ,\gamma )^{*}D_{m_{1},k_{1}}^{j_{1}}(\alpha ,\beta ,\gamma )D_{m_{2},k_{2}}^{j_{2}}(\alpha ,\beta ,\gamma )\\{}={}&{\frac {8\pi ^{2}}{2J+1}}\langle j_{1}\,m_{1}\,j_{2}\,m_{2}|J\,M\rangle \langle j_{1}\,k_{1}\,j_{2}\,k_{2}|J\,K\rangle \end{aligned}}$

## Relation to spherical harmonics

In the case where integers are involved, the coefficients can be related to integrals of spherical harmonics: $\int _{4\pi }Y_{\ell _{1}}^{m_{1}}{}^{*}(\Omega )Y_{\ell _{2}}^{m_{2}}{}^{*}(\Omega )Y_{L}^{M}(\Omega )\,d\Omega ={\sqrt {\frac {(2\ell _{1}+1)(2\ell _{2}+1)}{4\pi (2L+1)}}}\langle \ell _{1}\,0\,\ell _{2}\,0|L\,0\rangle \langle \ell _{1}\,m_{1}\,\ell _{2}\,m_{2}|L\,M\rangle$

It follows from this and orthonormality of the spherical harmonics that CG coefficients are in fact the expansion coefficients of a product of two spherical harmonics in terms of a single spherical harmonic: $Y_{\ell _{1}}^{m_{1}}(\Omega )Y_{\ell _{2}}^{m_{2}}(\Omega )=\sum _{L,M}{\sqrt {\frac {(2\ell _{1}+1)(2\ell _{2}+1)}{4\pi (2L+1)}}}\langle \ell _{1}\,0\,\ell _{2}\,0|L\,0\rangle \langle \ell _{1}\,m_{1}\,\ell _{2}\,m_{2}|L\,M\rangle Y_{L}^{M}(\Omega )$

## Other properties

$\sum _{m}(-1)^{j-m}\langle j\,m\,j\,(-m)|J\,0\rangle =\delta _{J,0}{\sqrt {2j+1}}$

## Clebsch–Gordan coefficients for specific groups

For arbitrary groups and their representations, Clebsch–Gordan coefficients are not known in general. However, algorithms to produce Clebsch–Gordan coefficients for the special unitary group SU(*n*) are known. In particular, SU(3) Clebsch-Gordan coefficients have been computed and tabulated because of their utility in characterizing hadronic decays, where a flavor-SU(3) symmetry exists that relates the up, down, and strange quarks. A web interface for tabulating SU(N) Clebsch–Gordan coefficients is readily available.
