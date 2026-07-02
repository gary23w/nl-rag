---
title: "Ricci calculus"
source: https://en.wikipedia.org/wiki/Tensor_calculus
domain: tensor-analysis
license: CC-BY-SA-4.0
tags: tensor calculus, covariant derivative, metric tensor, christoffel symbols
fetched: 2026-07-02
---

# Ricci calculus

(Redirected from

Tensor calculus

)

In mathematics, **Ricci calculus** constitutes the rules of index notation and manipulation for tensors and tensor fields on a differentiable manifold, with or without a metric tensor or connection. It is also the modern name for what used to be called the **absolute differential calculus** (the foundation of tensor calculus), **tensor calculus** or **tensor analysis** developed by Gregorio Ricci-Curbastro in 1887–1896, and subsequently popularized in a paper written with his pupil Tullio Levi-Civita in 1900. Jan Arnoldus Schouten developed the modern notation and formalism for this mathematical framework, and made contributions to the theory during its applications to general relativity and differential geometry in the early twentieth century. The basis of modern tensor analysis was developed by Bernhard Riemann in a paper from 1861.

A component of a tensor is a real number that is used as a coefficient of a basis element for the tensor space. The tensor is the sum of its components multiplied by their corresponding basis elements. Tensors and tensor fields can be expressed in terms of their components, and operations on tensors and tensor fields can be expressed in terms of operations on their components. The description of tensor fields and operations on them in terms of their components is the focus of the Ricci calculus. This notation allows an efficient expression of such tensor fields and operations. While much of the notation may be applied with any tensors, operations relating to a differential structure are only applicable to tensor fields. Where needed, the notation extends to components of non-tensors, particularly multidimensional arrays.

A tensor may be expressed as a linear sum of the tensor product of vector and covector basis elements. The resulting tensor components are labelled by indices of the basis. Each index has one possible value per dimension of the underlying vector space. The number of indices equals the degree (or order) of the tensor.

For compactness and convenience, the Ricci calculus incorporates Einstein notation, which implies summation over indices repeated within a term and universal quantification over free indices. Expressions in the notation of the Ricci calculus may generally be interpreted as a set of simultaneous equations relating the components as functions over a manifold, usually more specifically as functions of the coordinates on the manifold. This allows intuitive manipulation of expressions with familiarity of only a limited set of rules.

## Applications

Tensor calculus has many applications in physics, engineering and computer science including elasticity, continuum mechanics, electromagnetism (see mathematical descriptions of the electromagnetic field), general relativity (see mathematics of general relativity), quantum field theory, and machine learning.

Working with a main proponent of the exterior calculus Élie Cartan, the influential geometer Shiing-Shen Chern summarizes the role of tensor calculus:

> In our subject of differential geometry, where you talk about manifolds, one difficulty is that the geometry is described by coordinates, but the coordinates do not have meaning. They are allowed to undergo transformation. And in order to handle this kind of situation, an important tool is the so-called tensor analysis, or Ricci calculus, which was new to mathematicians. In mathematics you have a function, you write down the function, you calculate, or you add, or you multiply, or you can differentiate. You have something very concrete. In geometry the geometric situation is described by numbers, but you can change your numbers arbitrarily. So to handle this, you need the Ricci calculus.

## Notation for indices

#### Space and time coordinates

Where a distinction is to be made between the space-like basis elements and a time-like element in the four-dimensional spacetime of classical physics, this is conventionally done through indices as follows:

- The lowercase Latin alphabet *a*, *b*, *c*, ... is used to indicate restriction to 3-dimensional Euclidean space, which take values 1, 2, 3 for the spatial components; and the time-like element, indicated by 0, is shown separately.
- The lowercase Greek alphabet *α*, *β*, *γ*, ... is used for 4-dimensional spacetime, which typically take values 0 for time components and 1, 2, 3 for the spatial components.

Some sources use 4 instead of 0 as the index value corresponding to time; in this article, 0 is used. Otherwise, in general mathematical contexts, any symbols can be used for the indices, generally running over all dimensions of the vector space.

#### Coordinate and index notation

The author(s) will usually make it clear whether a subscript is intended as an index or as a label.

For example, in 3-D Euclidean space and using Cartesian coordinates; the coordinate vector **A** = (*A*1, *A*2, *A*3) = (*A*x, *A*y, *A*z) shows a direct correspondence between the subscripts 1, 2, 3 and the labels x, y, z. In the expression *Ai*, *i* is interpreted as an index ranging over the values 1, 2, 3, while the x, y, z subscripts are only labels, not variables. In the context of spacetime, the index value 0 conventionally corresponds to the label t.

#### Reference to basis

Indices themselves may be *labelled* using diacritic-like symbols, such as a hat (ˆ), bar (¯), tilde (˜), or prime (′) as in:

$X_{\hat {\phi }}\,,Y_{\bar {\lambda }}\,,Z_{\tilde {\eta }}\,,T_{\mu '}$

to denote a possibly different basis for that index. An example is in Lorentz transformations from one frame of reference to another, where one frame could be unprimed and the other primed, as in:

$v^{\mu '}=v^{\nu }L_{\nu }{}^{\mu '}.$

This is not to be confused with van der Waerden notation for spinors, which uses hats and overdots on indices to reflect the chirality of a spinor.

### Upper and lower indices

Ricci calculus, and index notation more generally, distinguishes between lower indices (subscripts) and upper indices (superscripts); the latter are *not* exponents, even though they may look as such to the reader only familiar with other parts of mathematics.

In the special case that the metric tensor is everywhere equal to the identity matrix, it is possible to drop the distinction between upper and lower indices, and then all indices could be written in the lower position. Coordinate formulae in linear algebra such as $a_{ij}b_{jk}$ for the product of matrices may be examples of this. But in general, the distinction between upper and lower indices should be maintained.

#### Covariant tensor components

A *lower index* (subscript) indicates covariance of the components with respect to that index:

$A_{\alpha \beta \gamma \cdots }$

#### Contravariant tensor components

An *upper index* (superscript) indicates contravariance of the components with respect to that index:

$A^{\alpha \beta \gamma \cdots }$

#### Mixed-variance tensor components

A tensor may have both upper and lower indices:

$A_{\alpha }{}^{\beta }{}_{\gamma }{}^{\delta \cdots }.$

Ordering of indices is significant, even when of differing variance. However, when it is understood that no indices will be raised or lowered while retaining the base symbol, covariant indices are sometimes placed below contravariant indices for notational convenience (e.g. with the generalized Kronecker delta).

#### Tensor type and degree

The number of each upper and lower indices of a tensor gives its *type*: a tensor with *p* upper and *q* lower indices is said to be of type (*p*, *q*), or to be a type-(*p*, *q*) tensor.

The number of indices of a tensor, regardless of variance, is called the *degree* of the tensor (alternatively, its *valence*, *order* or *rank*, although *rank* is ambiguous). Thus, a tensor of type (*p*, *q*) has degree *p* + *q*.

#### Summation convention

The same symbol occurring twice (one upper and one lower) within a term indicates a pair of indices that are summed over:

$A_{\alpha }B^{\alpha }\equiv \sum _{\alpha }A_{\alpha }B^{\alpha }\quad {\text{or}}\quad A^{\alpha }B_{\alpha }\equiv \sum _{\alpha }A^{\alpha }B_{\alpha }\,.$

The operation implied by such a summation is called tensor contraction:

$A_{\alpha }B^{\beta }\rightarrow A_{\alpha }B^{\alpha }\equiv \sum _{\alpha }A_{\alpha }B^{\alpha }\,.$

This summation may occur more than once within a term with a distinct symbol per pair of indices, for example:

$A_{\alpha }{}^{\gamma }B^{\alpha }C_{\gamma }{}^{\beta }\equiv \sum _{\alpha }\sum _{\gamma }A_{\alpha }{}^{\gamma }B^{\alpha }C_{\gamma }{}^{\beta }\,.$

Other combinations of repeated indices within a term are considered to be ill-formed, such as

| $A_{\alpha \alpha }{}^{\gamma }\qquad$ | (both occurrences of $\alpha$ are lower; $A_{\alpha }{}^{\alpha \gamma }$ would be fine) |
|---|---|
| $A_{\alpha \gamma }{}^{\gamma }B^{\alpha }C_{\gamma }{}^{\beta }$ | ( $\gamma$ occurs twice as a lower index; $A_{\alpha \gamma }{}^{\gamma }B^{\alpha }$ or $A_{\alpha \delta }{}^{\gamma }B^{\alpha }C_{\gamma }{}^{\beta }$ would be fine). |

The reason for excluding such formulae is that although these quantities could be computed as arrays of numbers, they would not in general transform as tensors under a change of basis.

#### Multi-index notation

If a tensor has a list of all upper or lower indices, one shorthand is to use a capital letter for the list:

$A_{i_{1}\cdots i_{n}}B^{i_{1}\cdots i_{n}j_{1}\cdots j_{m}}C_{j_{1}\cdots j_{m}}\equiv A_{I}B^{IJ}C_{J},$

where *I* = *i*1 *i*2 ⋅⋅⋅ *in* and *J* = *j*1 *j*2 ⋅⋅⋅ *jm*.

#### Sequential summation

A pair of vertical bars | ⋅ | around a set of all-upper indices or all-lower indices (but not both), associated with contraction with another set of indices when the expression is completely antisymmetric in each of the two sets of indices:

$A_{|\alpha \beta \gamma |\cdots }B^{\alpha \beta \gamma \cdots }=A_{\alpha \beta \gamma \cdots }B^{|\alpha \beta \gamma |\cdots }=\sum _{\alpha <\beta <\gamma }A_{\alpha \beta \gamma \cdots }B^{\alpha \beta \gamma \cdots }$

means a restricted sum over index values, where each index is constrained to being strictly less than the next. More than one group can be summed in this way, for example:

${\begin{aligned}&A_{|\alpha \beta \gamma |}{}^{|\delta \epsilon \cdots \lambda |}B^{\alpha \beta \gamma }{}_{\delta \epsilon \cdots \lambda |\mu \nu \cdots \zeta |}C^{\mu \nu \cdots \zeta }\\[3pt]={}&\sum _{\alpha <\beta <\gamma }~\sum _{\delta <\epsilon <\cdots <\lambda }~\sum _{\mu <\nu <\cdots <\zeta }A_{\alpha \beta \gamma }{}^{\delta \epsilon \cdots \lambda }B^{\alpha \beta \gamma }{}_{\delta \epsilon \cdots \lambda \mu \nu \cdots \zeta }C^{\mu \nu \cdots \zeta }\end{aligned}}$

When using multi-index notation, an underarrow is placed underneath the block of indices:

$A_{\underset {\rightharpoondown }{P}}{}^{\underset {\rightharpoondown }{Q}}B^{P}{}_{Q{\underset {\rightharpoondown }{R}}}C^{R}=\sum _{\underset {\rightharpoondown }{P}}\sum _{\underset {\rightharpoondown }{Q}}\sum _{\underset {\rightharpoondown }{R}}A_{P}{}^{Q}B^{P}{}_{QR}C^{R}$

where

${\underset {\rightharpoondown }{P}}=|\alpha \beta \gamma |\,,\quad {\underset {\rightharpoondown }{Q}}=|\delta \epsilon \cdots \lambda |\,,\quad {\underset {\rightharpoondown }{R}}=|\mu \nu \cdots \zeta |$

#### Raising and lowering indices

By contracting an index with a non-singular metric tensor, the type of a tensor can be changed, converting a lower index to an upper index or vice versa:

$B^{\gamma }{}_{\beta \cdots }=g^{\gamma \alpha }A_{\alpha \beta \cdots }\quad {\text{and}}\quad A_{\alpha \beta \cdots }=g_{\alpha \gamma }B^{\gamma }{}_{\beta \cdots }$

The base symbol in many cases is retained (e.g. using *A* where *B* appears here), and when there is no ambiguity, repositioning an index may be taken to imply this operation.

### Correlations between index positions and invariance

This table summarizes how the manipulation of covariant and contravariant indices fit in with invariance under a passive transformation between bases, with the components of each basis set in terms of the other reflected in the first column. The barred indices refer to the final coordinate system after the transformation.

The Kronecker delta is used, see also below.

|   | Basis transformation | Component transformation | Invariance |
|---|---|---|---|
| Covector, covariant vector, 1-form | $\omega ^{\bar {\alpha }}=L_{\beta }{}^{\bar {\alpha }}\omega ^{\beta }$ | $a_{\bar {\alpha }}=a_{\gamma }L^{\gamma }{}_{\bar {\alpha }}$ | $a_{\bar {\alpha }}\omega ^{\bar {\alpha }}=a_{\gamma }L^{\gamma }{}_{\bar {\alpha }}L_{\beta }{}^{\bar {\alpha }}\omega ^{\beta }=a_{\gamma }\delta ^{\gamma }{}_{\beta }\omega ^{\beta }=a_{\beta }\omega ^{\beta }$ |
| Vector, contravariant vector | $e_{\bar {\alpha }}=e_{\gamma }L_{\bar {\alpha }}{}^{\gamma }$ | $u^{\bar {\alpha }}=L^{\bar {\alpha }}{}_{\beta }u^{\beta }$ | $e_{\bar {\alpha }}u^{\bar {\alpha }}=e_{\gamma }L_{\bar {\alpha }}{}^{\gamma }L^{\bar {\alpha }}{}_{\beta }u^{\beta }=e_{\gamma }\delta ^{\gamma }{}_{\beta }u^{\beta }=e_{\gamma }u^{\gamma }$ |

## General outlines for index notation and operations

Tensors are equal if and only if every corresponding component is equal; e.g., tensor *A* equals tensor *B* if and only if

$A^{\alpha }{}_{\beta \gamma }=B^{\alpha }{}_{\beta \gamma }$

for all *α*, *β*, *γ*. Consequently, there are facets of the notation that are useful in checking that an equation makes sense (an analogous procedure to dimensional analysis).

### Free and dummy indices

Indices not involved in contractions are called *free indices*. Indices used in contractions are termed *dummy indices*, or *summation indices*.

### A tensor equation represents many ordinary (real-valued) equations

The components of tensors (like *Aα*, *Bβγ* etc.) are just real numbers. Since the indices take various integer values to select specific components of the tensors, a single tensor equation represents many ordinary equations. If a tensor equality has *n* free indices, and if the dimensionality of the underlying vector space is *m*, the equality represents *mn* equations: each index takes on every value of a specific set of values.

For instance, if

$A^{\alpha }B_{\beta }{}^{\gamma }C_{\gamma \delta }+D^{\alpha }{}_{\beta }{}E_{\delta }=T^{\alpha }{}_{\beta }{}_{\delta }$

is in four dimensions (that is, each index runs from 0 to 3 or from 1 to 4), then because there are three free indices (*α*, *β*, *δ*), there are 43 = 64 equations. Three of these are:

${\begin{aligned}A^{0}B_{1}{}^{0}C_{00}+A^{0}B_{1}{}^{1}C_{10}+A^{0}B_{1}{}^{2}C_{20}+A^{0}B_{1}{}^{3}C_{30}+D^{0}{}_{1}{}E_{0}&=T^{0}{}_{1}{}_{0}\\A^{1}B_{0}{}^{0}C_{00}+A^{1}B_{0}{}^{1}C_{10}+A^{1}B_{0}{}^{2}C_{20}+A^{1}B_{0}{}^{3}C_{30}+D^{1}{}_{0}{}E_{0}&=T^{1}{}_{0}{}_{0}\\A^{1}B_{2}{}^{0}C_{02}+A^{1}B_{2}{}^{1}C_{12}+A^{1}B_{2}{}^{2}C_{22}+A^{1}B_{2}{}^{3}C_{32}+D^{1}{}_{2}{}E_{2}&=T^{1}{}_{2}{}_{2}.\end{aligned}}$

This illustrates the compactness and efficiency of using index notation: many equations which all share a similar structure can be collected into one simple tensor equation.

### Indices are replaceable labels

Replacing any index symbol throughout by another leaves the tensor equation unchanged (provided there is no conflict with other symbols already used). This can be useful when manipulating indices, such as using index notation to verify vector calculus identities or identities of the Kronecker delta and Levi-Civita symbol (see also below). An example of a correct change is:

$A^{\alpha }B_{\beta }{}^{\gamma }C_{\gamma \delta }+D^{\alpha }{}_{\beta }{}E_{\delta }\rightarrow A^{\lambda }B_{\beta }{}^{\mu }C_{\mu \delta }+D^{\lambda }{}_{\beta }{}E_{\delta }\,,$

whereas an erroneous change is:

$A^{\alpha }B_{\beta }{}^{\gamma }C_{\gamma \delta }+D^{\alpha }{}_{\beta }{}E_{\delta }\nrightarrow A^{\lambda }B_{\beta }{}^{\gamma }C_{\mu \delta }+D^{\alpha }{}_{\beta }{}E_{\delta }\,.$

In the first replacement, *λ* replaced *α* and *μ* replaced *γ* *everywhere*, so the expression still has the same meaning. In the second, *λ* did not fully replace *α*, and *μ* did not fully replace *γ* (incidentally, the contraction on the *γ* index became a tensor product), which is entirely inconsistent for reasons shown next.

### Indices are the same in every term

The free indices in a tensor expression always appear in the same (upper or lower) position throughout every term, and in a tensor equation the free indices are the same on each side. Dummy indices (which implies a summation over that index) need not be the same, for example:

$A^{\alpha }B_{\beta }{}^{\gamma }C_{\gamma \delta }+D^{\alpha }{}_{\delta }E_{\beta }=T^{\alpha }{}_{\beta }{}_{\delta }$

as for an erroneous expression:

$A^{\alpha }B_{\beta }{}^{\gamma }C_{\gamma \delta }+D_{\alpha }{}_{\beta }{}^{\gamma }E^{\delta }.$

In other words, non-repeated indices must be of the same type in every term of the equation. In the above identity, *α*, *β*, *δ* line up throughout and *γ* occurs twice in one term due to a contraction (once as an upper index and once as a lower index), and thus it is a valid expression. In the invalid expression, while *β* lines up, *α* and *δ* do not, and *γ* appears twice in one term (contraction) *and* once in another term, which is inconsistent.

### Brackets and punctuation used once where implied

When applying a rule to a number of indices (differentiation, symmetrization etc., shown next), the bracket or punctuation symbols denoting the rules are only shown on one group of the indices to which they apply.

If the brackets enclose *covariant indices* – the rule applies only to *all covariant indices enclosed in the brackets*, not to any contravariant indices which happen to be placed intermediately between the brackets.

Similarly if brackets enclose *contravariant indices* – the rule applies only to *all enclosed contravariant indices*, not to intermediately placed covariant indices.

## Symmetric and antisymmetric parts

### Symmetric part of tensor

Parentheses, ( ), around multiple indices denotes the symmetrized part of the tensor. When symmetrizing *p* indices using *σ* to range over permutations of the numbers 1 to *p*, one takes a sum over the permutations of those indices *α**σ*(*i*) for *i* = 1, 2, 3, ..., *p*, and then divides by the number of permutations:

$A_{(\alpha _{1}\alpha _{2}\cdots \alpha _{p})\alpha _{p+1}\cdots \alpha _{q}}={\dfrac {1}{p!}}\sum _{\sigma }A_{\alpha _{\sigma (1)}\cdots \alpha _{\sigma (p)}\alpha _{p+1}\cdots \alpha _{q}}\,.$

For example, two symmetrizing indices mean there are two indices to permute and sum over:

$A_{(\alpha \beta )\gamma \cdots }={\dfrac {1}{2!}}\left(A_{\alpha \beta \gamma \cdots }+A_{\beta \alpha \gamma \cdots }\right)$

while for three symmetrizing indices, there are three indices to sum over and permute:

$A_{(\alpha \beta \gamma )\delta \cdots }={\dfrac {1}{3!}}\left(A_{\alpha \beta \gamma \delta \cdots }+A_{\gamma \alpha \beta \delta \cdots }+A_{\beta \gamma \alpha \delta \cdots }+A_{\alpha \gamma \beta \delta \cdots }+A_{\gamma \beta \alpha \delta \cdots }+A_{\beta \alpha \gamma \delta \cdots }\right)$

The symmetrization is distributive over addition;

$A_{(\alpha }\left(B_{\beta )\gamma \cdots }+C_{\beta )\gamma \cdots }\right)=A_{(\alpha }B_{\beta )\gamma \cdots }+A_{(\alpha }C_{\beta )\gamma \cdots }$

Indices are not part of the symmetrization when they are:

- not on the same level, for example; $A_{(\alpha }B^{\beta }{}_{\gamma )}={\dfrac {1}{2!}}\left(A_{\alpha }B^{\beta }{}_{\gamma }+A_{\gamma }B^{\beta }{}_{\alpha }\right)$
- within the parentheses and between vertical bars (i.e. |⋅⋅⋅|), modifying the previous example; $A_{(\alpha }B_{|\beta |}{}_{\gamma )}={\dfrac {1}{2!}}\left(A_{\alpha }B_{\beta \gamma }+A_{\gamma }B_{\beta \alpha }\right)$

Here the *α* and *γ* indices are symmetrized, *β* is not.

### Antisymmetric or alternating part of tensor

Square brackets, [ ], around multiple indices denotes the *anti*symmetrized part of the tensor. For *p* antisymmetrizing indices – the sum over the permutations of those indices *α**σ*(*i*) multiplied by the signature of the permutation sgn(*σ*) is taken, then divided by the number of permutations:

${\begin{aligned}&A_{[\alpha _{1}\cdots \alpha _{p}]\alpha _{p+1}\cdots \alpha _{q}}\\[3pt]={}&{\dfrac {1}{p!}}\sum _{\sigma }\operatorname {sgn}(\sigma )A_{\alpha _{\sigma (1)}\cdots \alpha _{\sigma (p)}\alpha _{p+1}\cdots \alpha _{q}}\\={}&\delta _{\alpha _{1}\cdots \alpha _{p}}^{\beta _{1}\dots \beta _{p}}A_{\beta _{1}\cdots \beta _{p}\alpha _{p+1}\cdots \alpha _{q}}\\\end{aligned}}$

where *δ**β*1⋅⋅⋅*βp* *α*1⋅⋅⋅*αp* is the generalized Kronecker delta of degree 2*p*, with scaling as defined below.

For example, two antisymmetrizing indices imply:

$A_{[\alpha \beta ]\gamma \cdots }={\dfrac {1}{2!}}\left(A_{\alpha \beta \gamma \cdots }-A_{\beta \alpha \gamma \cdots }\right)$

while three antisymmetrizing indices imply:

$A_{[\alpha \beta \gamma ]\delta \cdots }={\dfrac {1}{3!}}\left(A_{\alpha \beta \gamma \delta \cdots }+A_{\gamma \alpha \beta \delta \cdots }+A_{\beta \gamma \alpha \delta \cdots }-A_{\alpha \gamma \beta \delta \cdots }-A_{\gamma \beta \alpha \delta \cdots }-A_{\beta \alpha \gamma \delta \cdots }\right)$

as for a more specific example, if *F* represents the electromagnetic tensor, then the equation

$0=F_{[\alpha \beta ,\gamma ]}={\dfrac {1}{3!}}\left(F_{\alpha \beta ,\gamma }+F_{\gamma \alpha ,\beta }+F_{\beta \gamma ,\alpha }-F_{\beta \alpha ,\gamma }-F_{\alpha \gamma ,\beta }-F_{\gamma \beta ,\alpha }\right)\,$

represents Gauss's law for magnetism and Faraday's law of induction.

As before, the antisymmetrization is distributive over addition;

$A_{[\alpha }\left(B_{\beta ]\gamma \cdots }+C_{\beta ]\gamma \cdots }\right)=A_{[\alpha }B_{\beta ]\gamma \cdots }+A_{[\alpha }C_{\beta ]\gamma \cdots }$

As with symmetrization, indices are not antisymmetrized when they are:

- not on the same level, for example; $A_{[\alpha }B^{\beta }{}_{\gamma ]}={\dfrac {1}{2!}}\left(A_{\alpha }B^{\beta }{}_{\gamma }-A_{\gamma }B^{\beta }{}_{\alpha }\right)$
- within the square brackets and between vertical bars (i.e. |⋅⋅⋅|), modifying the previous example; $A_{[\alpha }B_{|\beta |}{}_{\gamma ]}={\dfrac {1}{2!}}\left(A_{\alpha }B_{\beta \gamma }-A_{\gamma }B_{\beta \alpha }\right)$

Here the *α* and *γ* indices are antisymmetrized, *β* is not.

### Sum of symmetric and antisymmetric parts

Any tensor can be written as the sum of its symmetric and antisymmetric parts on two indices:

$A_{\alpha \beta \gamma \cdots }=A_{(\alpha \beta )\gamma \cdots }+A_{[\alpha \beta ]\gamma \cdots }$

as can be seen by adding the above expressions for *A*(*αβ*)*γ*⋅⋅⋅ and *A*[*αβ*]*γ*⋅⋅⋅. This does not hold for other than two indices.

## Differentiation

For compactness, derivatives may be indicated by adding indices after a comma or semicolon.

### Partial derivative

While most of the expressions of the Ricci calculus are valid for arbitrary bases, the expressions involving partial derivatives of tensor components with respect to coordinates apply only with a coordinate basis: a basis that is defined through differentiation with respect to the coordinates. Coordinates are typically denoted by *x**μ*, but do not in general form the components of a vector. In flat spacetime with linear coordinatization, a tuple of *differences* in coordinates, Δ*x**μ*, can be treated as a contravariant vector. With the same constraints on the space and on the choice of coordinate system, the partial derivatives with respect to the coordinates yield a result that is effectively covariant. Aside from use in this special case, the partial derivatives of components of tensors do not in general transform covariantly, but are useful in building expressions that are covariant, albeit still with a coordinate basis if the partial derivatives are explicitly used, as with the covariant, exterior and Lie derivatives below.

To indicate partial differentiation of the components of a tensor field with respect to a coordinate variable *x**γ*, a *comma* is placed before an appended lower index of the coordinate variable.

$A_{\alpha \beta \cdots ,\gamma }={\dfrac {\partial }{\partial x^{\gamma }}}A_{\alpha \beta \cdots }$

This may be repeated (without adding further commas):

$A_{\alpha _{1}\alpha _{2}\cdots \alpha _{p}\,,\,\alpha _{p+1}\cdots \alpha _{q}}={\dfrac {\partial }{\partial x^{\alpha _{q}}}}\cdots {\dfrac {\partial }{\partial x^{\alpha _{p+2}}}}{\dfrac {\partial }{\partial x^{\alpha _{p+1}}}}A_{\alpha _{1}\alpha _{2}\cdots \alpha _{p}}.$

These components do *not* transform covariantly, unless the expression being differentiated is a scalar. This derivative is characterized by the product rule and the derivatives of the coordinates

$x^{\alpha }{}_{,\gamma }=\delta _{\gamma }^{\alpha },$

where *δ* is the Kronecker delta.

### Covariant derivative

The covariant derivative is only defined if a connection is defined. For any tensor field, a *semicolon* ( ; ) placed before an appended lower (covariant) index indicates covariant differentiation. Less common alternatives to the semicolon include a *forward slash* ( / ) or in three-dimensional curved space a single vertical bar ( | ).

The covariant derivative of a scalar function, a contravariant vector and a covariant vector are:

$f_{;\beta }=f_{,\beta }$

$A^{\alpha }{}_{;\beta }=A^{\alpha }{}_{,\beta }+\Gamma ^{\alpha }{}_{\gamma \beta }A^{\gamma }$

${\displaystyle A_{\alpha$

where Γ*αγβ* are the connection coefficients.

For an arbitrary tensor:

${\begin{aligned}T^{\alpha _{1}\cdots \alpha _{r}}{}_{\beta _{1}\cdots \beta _{s};\gamma }&\\=T^{\alpha _{1}\cdots \alpha _{r}}{}_{\beta _{1}\cdots \beta _{s},\gamma }&+\,\Gamma ^{\alpha _{1}}{}_{\delta \gamma }T^{\delta \alpha _{2}\cdots \alpha _{r}}{}_{\beta _{1}\cdots \beta _{s}}+\cdots +\Gamma ^{\alpha _{r}}{}_{\delta \gamma }T^{\alpha _{1}\cdots \alpha _{r-1}\delta }{}_{\beta _{1}\cdots \beta _{s}}\\&-\,\Gamma ^{\delta }{}_{\beta _{1}\gamma }T^{\alpha _{1}\cdots \alpha _{r}}{}_{\delta \beta _{2}\cdots \beta _{s}}-\cdots -\Gamma ^{\delta }{}_{\beta _{s}\gamma }T^{\alpha _{1}\cdots \alpha _{r}}{}_{\beta _{1}\cdots \beta _{s-1}\delta }\,.\end{aligned}}$

An alternative notation for the covariant derivative of any tensor is the subscripted nabla symbol ∇*β*. For the case of a vector field *Aα*:

$\nabla _{\beta }A^{\alpha }=A^{\alpha }{}_{;\beta }\,.$

The covariant formulation of the directional derivative of any tensor field along a vector *vγ* may be expressed as its contraction with the covariant derivative, e.g.:

${\displaystyle v^{\gamma }A_{\alpha$

The components of this derivative of a tensor field transform covariantly, and hence form another tensor field, despite subexpressions (the partial derivative and the connection coefficients) separately not transforming covariantly.

This derivative is characterized by the product rule:

${\displaystyle (A^{\alpha }{}_{\beta \cdots }B^{\gamma }{}_{\delta \cdots })_{;\epsilon }=A^{\alpha }{}_{\beta \cdots$

#### Connection types

A Koszul connection on the tangent bundle of a differentiable manifold is called an affine connection.

A connection is a metric connection when the covariant derivative of the metric tensor vanishes:

${\displaystyle g_{\mu \nu$

An affine connection that is also a metric connection is called a Riemannian connection. A Riemannian connection that is torsion-free (i.e., for which the torsion tensor vanishes: *T**α**βγ* = 0) is a Levi-Civita connection.

The Γ*α**βγ* for a Levi-Civita connection in a coordinate basis are called Christoffel symbols of the second kind.

### Exterior derivative

The exterior derivative of a totally antisymmetric type (0, *s*) tensor field with components *A**α*1⋅⋅⋅*α**s* (also called a differential form) is a derivative that is covariant under basis transformations. It does not depend on either a metric tensor or a connection: it requires only the structure of a differentiable manifold. In a coordinate basis, it may be expressed as the antisymmetrization of the partial derivatives of the tensor components:

$(\mathrm {d} A)_{\gamma \alpha _{1}\cdots \alpha _{s}}={\frac {\partial }{\partial x^{[\gamma }}}A_{\alpha _{1}\cdots \alpha _{s}]}=A_{[\alpha _{1}\cdots \alpha _{s},\gamma ]}.$

This derivative is not defined on any tensor field with contravariant indices or that is not totally antisymmetric. It is characterized by a graded product rule.

### Lie derivative

The Lie derivative is another derivative that is covariant under basis transformations. Like the exterior derivative, it does not depend on either a metric tensor or a connection. The Lie derivative of a type (*r*, *s*) tensor field *T* along (the flow of) a contravariant vector field *X**ρ* may be expressed using a coordinate basis as

${\begin{aligned}({\mathcal {L}}_{X}T)^{\alpha _{1}\cdots \alpha _{r}}{}_{\beta _{1}\cdots \beta _{s}}&\\=X^{\gamma }T^{\alpha _{1}\cdots \alpha _{r}}{}_{\beta _{1}\cdots \beta _{s},\gamma }&-\,X^{\alpha _{1}}{}_{,\gamma }T^{\gamma \alpha _{2}\cdots \alpha _{r}}{}_{\beta _{1}\cdots \beta _{s}}-\cdots -X^{\alpha _{r}}{}_{,\gamma }T^{\alpha _{1}\cdots \alpha _{r-1}\gamma }{}_{\beta _{1}\cdots \beta _{s}}\\&+\,X^{\gamma }{}_{,\beta _{1}}T^{\alpha _{1}\cdots \alpha _{r}}{}_{\gamma \beta _{2}\cdots \beta _{s}}+\cdots +X^{\gamma }{}_{,\beta _{s}}T^{\alpha _{1}\cdots \alpha _{r}}{}_{\beta _{1}\cdots \beta _{s-1}\gamma }\,.\end{aligned}}$

This derivative is characterized by the product rule and the fact that the Lie derivative of a contravariant vector field along itself is zero:

$({\mathcal {L}}_{X}X)^{\alpha }=X^{\gamma }X^{\alpha }{}_{,\gamma }-X^{\alpha }{}_{,\gamma }X^{\gamma }=0\,.$

## Notable tensors

### Kronecker delta

The Kronecker delta is like the identity matrix when multiplied and contracted:

${\begin{aligned}\delta _{\beta }^{\alpha }\,A^{\beta }&=A^{\alpha }\\\delta _{\nu }^{\mu }\,B_{\mu }&=B_{\nu }.\end{aligned}}$

The components *δ**α* *β* are the same in any basis and form an invariant tensor of type (1, 1), i.e. the identity of the tangent bundle over the identity mapping of the base manifold, and so its trace is an invariant. Its trace is the dimensionality of the space; for example, in four-dimensional spacetime,

$\delta _{\rho }^{\rho }=\delta _{0}^{0}+\delta _{1}^{1}+\delta _{2}^{2}+\delta _{3}^{3}=4.$

The Kronecker delta is one of the family of generalized Kronecker deltas. The generalized Kronecker delta of degree 2*p* may be defined in terms of the Kronecker delta by (a common definition includes an additional multiplier of *p*! on the right):

$\delta _{\beta _{1}\cdots \beta _{p}}^{\alpha _{1}\cdots \alpha _{p}}=\delta _{\beta _{1}}^{[\alpha _{1}}\cdots \delta _{\beta _{p}}^{\alpha _{p}]},$

and acts as an antisymmetrizer on *p* indices:

$\delta _{\beta _{1}\cdots \beta _{p}}^{\alpha _{1}\cdots \alpha _{p}}\,A^{\beta _{1}\cdots \beta _{p}}=A^{[\alpha _{1}\cdots \alpha _{p}]}.$

### Torsion tensor

An affine connection has a torsion tensor *T**α**βγ*:

$T^{\alpha }{}_{\beta \gamma }=\Gamma ^{\alpha }{}_{\beta \gamma }-\Gamma ^{\alpha }{}_{\gamma \beta }-\gamma ^{\alpha }{}_{\beta \gamma },$

where *γ**α**βγ* are given by the components of the Lie bracket of the local basis, which vanish when it is a coordinate basis.

For a Levi-Civita connection this tensor is defined to be zero, which for a coordinate basis gives the equations

$\Gamma ^{\alpha }{}_{\beta \gamma }=\Gamma ^{\alpha }{}_{\gamma \beta }.$

### Riemann curvature tensor

If this tensor is defined as

$R^{\rho }{}_{\sigma \mu \nu }=\Gamma ^{\rho }{}_{\nu \sigma ,\mu }-\Gamma ^{\rho }{}_{\mu \sigma ,\nu }+\Gamma ^{\rho }{}_{\mu \lambda }\Gamma ^{\lambda }{}_{\nu \sigma }-\Gamma ^{\rho }{}_{\nu \lambda }\Gamma ^{\lambda }{}_{\mu \sigma }\,,$

then it is the commutator of the covariant derivative with itself:

${\displaystyle A_{\nu$

since the connection is torsionless, which means that the torsion tensor vanishes.

This can be generalized to get the commutator for two covariant derivatives of an arbitrary tensor as follows:

${\begin{aligned}T^{\alpha _{1}\cdots \alpha _{r}}{}_{\beta _{1}\cdots \beta _{s};\gamma \delta }&-T^{\alpha _{1}\cdots \alpha _{r}}{}_{\beta _{1}\cdots \beta _{s};\delta \gamma }\\&\!\!\!\!\!\!\!\!\!\!=-R^{\alpha _{1}}{}_{\rho \gamma \delta }T^{\rho \alpha _{2}\cdots \alpha _{r}}{}_{\beta _{1}\cdots \beta _{s}}-\cdots -R^{\alpha _{r}}{}_{\rho \gamma \delta }T^{\alpha _{1}\cdots \alpha _{r-1}\rho }{}_{\beta _{1}\cdots \beta _{s}}\\&+R^{\sigma }{}_{\beta _{1}\gamma \delta }T^{\alpha _{1}\cdots \alpha _{r}}{}_{\sigma \beta _{2}\cdots \beta _{s}}+\cdots +R^{\sigma }{}_{\beta _{s}\gamma \delta }T^{\alpha _{1}\cdots \alpha _{r}}{}_{\beta _{1}\cdots \beta _{s-1}\sigma }\,\end{aligned}}$

which are often referred to as the *Ricci identities*.

### Metric tensor

The metric tensor *g**αβ* is used for lowering indices and gives the length of any space-like curve

${\text{length}}=\int _{y_{1}}^{y_{2}}{\sqrt {g_{\alpha \beta }{\frac {dx^{\alpha }}{d\gamma }}{\frac {dx^{\beta }}{d\gamma }}}}\,d\gamma \,,$

where *γ* is any smooth strictly monotone parameterization of the path. It also gives the duration of any time-like curve

${\text{duration}}=\int _{t_{1}}^{t_{2}}{\sqrt {{\frac {-1}{c^{2}}}g_{\alpha \beta }{\frac {dx^{\alpha }}{d\gamma }}{\frac {dx^{\beta }}{d\gamma }}}}\,d\gamma \,,$

where *γ* is any smooth strictly monotone parameterization of the trajectory. See also *Line element*.

The inverse matrix *g**αβ* of the metric tensor is another important tensor, used for raising indices:

$g^{\alpha \beta }g_{\beta \gamma }=\delta _{\gamma }^{\alpha }\,.$
