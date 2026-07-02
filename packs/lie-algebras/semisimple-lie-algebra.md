---
title: "Semisimple Lie algebra"
source: https://en.wikipedia.org/wiki/Semisimple_Lie_algebra
domain: lie-algebras
license: CC-BY-SA-4.0
tags: lie algebra, semisimple lie algebra, cartan subalgebra, killing form
fetched: 2026-07-02
---

# Semisimple Lie algebra

In mathematics, a Lie algebra is **semisimple** if it is a direct sum of simple Lie algebras. (A simple Lie algebra is a non-abelian Lie algebra without any non-zero proper ideals.)

Throughout the article, unless otherwise stated, a Lie algebra is a finite-dimensional Lie algebra over a field of characteristic 0. For such a Lie algebra ${\mathfrak {g}}$ , if nonzero, the following conditions are equivalent:

- ${\mathfrak {g}}$ is semisimple;
- the Killing form $\kappa (x,y)=\operatorname {tr} (\operatorname {ad} (x)\operatorname {ad} (y))$ is non-degenerate;
- ${\mathfrak {g}}$ has no non-zero abelian ideals;
- ${\mathfrak {g}}$ has no non-zero solvable ideals;
- the radical (maximal solvable ideal) of ${\mathfrak {g}}$ is zero.

## Significance

The significance of semisimplicity comes firstly from the Levi decomposition, which states that every finite dimensional Lie algebra is the semidirect product of a solvable ideal (its radical) and a semisimple algebra. In particular, there is no nonzero Lie algebra that is both solvable and semisimple.

Semisimple Lie algebras have a very elegant classification, in stark contrast to solvable Lie algebras. Semisimple Lie algebras over an algebraically closed field of characteristic zero are completely classified by their root system, which are in turn classified by Dynkin diagrams. Semisimple algebras over non-algebraically closed fields can be understood in terms of those over the algebraic closure, though the classification is somewhat more intricate; see real form for the case of real semisimple Lie algebras, which were classified by Élie Cartan.

Further, the representation theory of semisimple Lie algebras is much cleaner than that for general Lie algebras. For example, the Jordan decomposition in a semisimple Lie algebra coincides with the Jordan decomposition in its representation; this is not the case for Lie algebras in general.

If ${\mathfrak {g}}$ is semisimple, then ${\mathfrak {g}}=[{\mathfrak {g}},{\mathfrak {g}}]$ . In particular, every linear semisimple Lie algebra is a subalgebra of ${\mathfrak {sl}}$ , the special linear Lie algebra. The study of the structure of ${\mathfrak {sl}}$ constitutes an important part of the representation theory for semisimple Lie algebras.

## History

The semisimple Lie algebras over the complex numbers were first classified by Wilhelm Killing (1888–90), though his proof lacked rigor. His proof was made rigorous by Élie Cartan (1894) in his Ph.D. thesis, who also classified semisimple real Lie algebras. This was subsequently refined, and the present classification by Dynkin diagrams was given by then 22-year-old Eugene Dynkin in 1947. Some minor modifications have been made (notably by J. P. Serre), but the proof is unchanged in its essentials and can be found in any standard reference, such as (Humphreys 1972).

## Basic properties

- Every ideal, quotient and product of semisimple Lie algebras is again semisimple.
- The center of a semisimple Lie algebra ${\mathfrak {g}}$ is trivial (since the center is an abelian ideal). In other words, the adjoint representation $\operatorname {ad}$ is injective. Moreover, the image turns out to be $\operatorname {Der} ({\mathfrak {g}})$ of derivations on ${\mathfrak {g}}$ . Hence, $\operatorname {ad$ is an isomorphism. (This is a special case of Whitehead's lemma.)
- As the adjoint representation is injective, a semisimple Lie algebra is a linear Lie algebra under the adjoint representation. This may lead to some ambiguity, as every Lie algebra is already linear with respect to some other vector space (Ado's theorem), although not necessarily via the adjoint representation. But in practice, such ambiguity rarely occurs.
- If ${\mathfrak {g}}$ is a semisimple Lie algebra, then ${\mathfrak {g}}=[{\mathfrak {g}},{\mathfrak {g}}]$ (because ${\mathfrak {g}}/[{\mathfrak {g}},{\mathfrak {g}}]$ is semisimple and abelian).
- A finite-dimensional Lie algebra ${\mathfrak {g}}$ over a field *k* of characteristic zero is semisimple if and only if the base extension ${\mathfrak {g}}\otimes _{k}F$ is semisimple for each field extension $F\supset k$ . Thus, for example, a finite-dimensional real Lie algebra is semisimple if and only if its complexification is semisimple.

## Jordan decomposition

Each endomorphism *x* of a finite-dimensional vector space over a field of characteristic zero can be decomposed uniquely into a semisimple (i.e., diagonalizable over the algebraic closure) and nilpotent part

$x=s+n\$

such that *s* and *n* commute with each other. Moreover, each of *s* and *n* is a polynomial in *x*. This is the Jordan decomposition of *x*.

The above applies to the adjoint representation $\operatorname {ad}$ of a semisimple Lie algebra ${\mathfrak {g}}$ . An element *x* of ${\mathfrak {g}}$ is said to be semisimple (resp. nilpotent) if $\operatorname {ad} (x)$ is a semisimple (resp. nilpotent) operator. If $x\in {\mathfrak {g}}$ , then the **abstract Jordan decomposition** states that *x* can be written uniquely as:

$x=s+n$

where s is semisimple, n is nilpotent and $[s,n]=0$ . Moreover, if $y\in {\mathfrak {g}}$ commutes with *x*, then it commutes with both $s,n$ as well.

The abstract Jordan decomposition factors through any representation of ${\mathfrak {g}}$ in the sense that given any representation ρ,

$\rho (x)=\rho (s)+\rho (n)\,$

is the Jordan decomposition of ρ(*x*) in the endomorphism algebra of the representation space. (This is proved as a consequence of Weyl's complete reducibility theorem; see Weyl's theorem on complete reducibility#Application: preservation of Jordan decomposition.)

## Structure

Let ${\mathfrak {g}}$ be a (finite-dimensional) semisimple Lie algebra over an algebraically closed field of characteristic zero. The structure of ${\mathfrak {g}}$ can be described by an adjoint action of a certain distinguished subalgebra on it, a Cartan subalgebra. By definition, a Cartan subalgebra (also called a maximal toral subalgebra) ${\mathfrak {h}}$ of ${\mathfrak {g}}$ is a maximal subalgebra such that, for each $h\in {\mathfrak {h}}$ , $\operatorname {ad} (h)$ is diagonalizable. As it turns out, ${\mathfrak {h}}$ is abelian and so all the operators in $\operatorname {ad} ({\mathfrak {h}})$ are simultaneously diagonalizable. For each linear functional $\alpha$ of ${\mathfrak {h}}$ , let

${\mathfrak {g}}_{\alpha }=\{x\in {\mathfrak {g}}|\operatorname {ad} (h)x:=[h,x]=\alpha (h)x\,{\text{ for all }}h\in {\mathfrak {h}}\}$

.

(Note that ${\mathfrak {g}}_{0}$ is the centralizer of ${\mathfrak {h}}$ .) Then

**Root space decomposition**— Given a Cartan subalgebra ${\mathfrak {h}}$ , it holds that ${\mathfrak {g}}_{0}={\mathfrak {h}}$ and there is a decomposition (as an ${\mathfrak {h}}$ -module):

${\mathfrak {g}}={\mathfrak {h}}\oplus \bigoplus _{\alpha \in \Phi }{\mathfrak {g}}_{\alpha }$

where $\Phi$ is the set of all nonzero linear functionals $\alpha$ of ${\mathfrak {h}}$ such that ${\mathfrak {g}}_{\alpha }\neq \{0\}$ . Moreover, for each $\alpha ,\beta \in \Phi$ ,

- $[{\mathfrak {g}}_{\alpha },{\mathfrak {g}}_{\beta }]\subseteq {\mathfrak {g}}_{\alpha +\beta }$ , which is the equality if $\alpha +\beta \neq 0$ .
- $[{\mathfrak {g}}_{\alpha },{\mathfrak {g}}_{-\alpha }]\oplus {\mathfrak {g}}_{-\alpha }\oplus {\mathfrak {g}}_{\alpha }\simeq {\mathfrak {sl}}_{2}$ as a Lie algebra.
- $\dim {\mathfrak {g}}_{\alpha }=1$ ; in particular, $\dim {\mathfrak {g}}=\dim {\mathfrak {h}}+\#\Phi$ .
- ${\mathfrak {g}}_{2\alpha }=\{0\}$ ; in other words, $2\alpha \not \in \Phi$ .
- With respect to the Killing form *B*, ${\mathfrak {g}}_{\alpha },{\mathfrak {g}}_{\beta }$ are orthogonal to each other if $\alpha +\beta \neq 0$ ; the restriction of *B* to ${\mathfrak {h}}$ is nondegenerate.

(The most difficult item to show is $\dim {\mathfrak {g}}_{\alpha }=1$ . The standard proofs all use some facts in the representation theory of ${\mathfrak {sl}}_{2}$ ; e.g., Serre uses the fact that an ${\mathfrak {sl}}_{2}$ -module with a primitive element of negative weight is infinite-dimensional, contradicting $\dim {\mathfrak {g}}<\infty$ .)

Let $h_{\alpha }\in {\mathfrak {h}},e_{\alpha }\in {\mathfrak {g}}_{\alpha },f_{\alpha }\in {\mathfrak {g}}_{-\alpha }$ with the commutation relations $[e_{\alpha },f_{\alpha }]=h_{\alpha },[h_{\alpha },e_{\alpha }]=2e_{\alpha },[h_{\alpha },f_{\alpha }]=-2f_{\alpha }$ ; i.e., the $h_{\alpha },e_{\alpha },f_{\alpha }$ correspond to the standard basis of ${\mathfrak {sl}}_{2}$ .

The linear functionals in $\Phi$ are called the **roots** of ${\mathfrak {g}}$ relative to ${\mathfrak {h}}$ . The roots span ${\mathfrak {h}}^{*}$ (since if $\alpha (h)=0,\alpha \in \Phi$ , then $\operatorname {ad} (h)$ is the zero operator; i.e., h is in the center, which is zero.) Moreover, from the representation theory of ${\mathfrak {sl}}_{2}$ , one deduces the following symmetry and integral properties of $\Phi$ : for each $\alpha ,\beta \in \Phi$ ,

- The endomorphism $s_{\alpha }:{\mathfrak {h}}^{*}\to {\mathfrak {h}}^{*},\,\gamma \mapsto \gamma -\gamma (h_{\alpha })\alpha$ leaves $\Phi$ invariant (i.e., $s_{\alpha }(\Phi )\subset \Phi$ ).
- $\beta (h_{\alpha })$ is an integer.

Note that $s_{\alpha }$ has the properties (1) $s_{\alpha }(\alpha )=-\alpha$ and (2) the fixed-point set is $\{\gamma \in {\mathfrak {h}}^{*}|\gamma (h_{\alpha })=0\}$ , which means that $s_{\alpha }$ is the reflection with respect to the hyperplane corresponding to $\alpha$ . The above then says that $\Phi$ is a root system.

It follows from the general theory of a root system that $\Phi$ contains a basis $\alpha _{1},\dots ,\alpha _{l}$ of ${\mathfrak {h}}^{*}$ such that each root is a linear combination of $\alpha _{1},\dots ,\alpha _{l}$ with integer coefficients of the same sign; the roots $\alpha _{i}$ are called simple roots. Let $e_{i}=e_{\alpha _{i}}$ , etc. Then the $3l$ elements $e_{i},f_{i},h_{i}$ (called **Chevalley generators**) generate ${\mathfrak {g}}$ as a Lie algebra. Moreover, they satisfy the relations (called **Serre relations**): with $a_{ij}=\alpha _{j}(h_{i})$ ,

$[h_{i},h_{j}]=0,$

$[e_{i},f_{i}]=h_{i},[e_{i},f_{j}]=0,i\neq j,$

$[h_{i},e_{j}]=a_{ij}e_{j},[h_{i},f_{j}]=-a_{ij}f_{j},$

$\operatorname {ad} (e_{i})^{-a_{ij}+1}(e_{j})=\operatorname {ad} (f_{i})^{-a_{ij}+1}(f_{j})=0,i\neq j$

.

The converse of this is also true: i.e., the Lie algebra generated by the generators and the relations like the above is a (finite-dimensional) semisimple Lie algebra that has the root space decomposition as above (provided the $[a_{ij}]_{1\leq i,j\leq l}$ is a Cartan matrix). This is a theorem of Serre. In particular, two semisimple Lie algebras are isomorphic if they have the same root system.

The implication of the axiomatic nature of a root system and Serre's theorem is that one can enumerate all possible root systems; hence, "all possible" semisimple Lie algebras (finite-dimensional over an algebraically closed field of characteristic zero).

The **Weyl group** is the group of linear transformations of ${\mathfrak {h}}^{*}\simeq {\mathfrak {h}}$ generated by the $s_{\alpha }$ 's. The Weyl group is an important symmetry of the problem; for example, the weights of any finite-dimensional representation of ${\mathfrak {g}}$ are invariant under the Weyl group.

## Example root space decomposition in sln(C)

For ${\mathfrak {g}}={\mathfrak {sl}}_{n}(\mathbb {C} )$ and the Cartan subalgebra ${\mathfrak {h}}$ of diagonal matrices, define $\lambda _{i}\in {\mathfrak {h}}^{*}$ by

$\lambda _{i}(d(a_{1},\ldots ,a_{n}))=a_{i}$

,

where $d(a_{1},\ldots ,a_{n})$ denotes the diagonal matrix with $a_{1},\ldots ,a_{n}$ on the diagonal. Then the decomposition is given by

${\mathfrak {g}}={\mathfrak {h}}\oplus \left(\bigoplus _{i\neq j}{\mathfrak {g}}_{\lambda _{i}-\lambda _{j}}\right)$

where

${\mathfrak {g}}_{\lambda _{i}-\lambda _{j}}={\text{Span}}_{\mathbb {C} }(e_{ij})$

for the vector $e_{ij}$ in ${\mathfrak {sl}}_{n}(\mathbb {C} )$ with the standard (matrix) basis, meaning $e_{ij}$ represents the basis vector in the i -th row and j -th column. This decomposition of ${\mathfrak {g}}$ has an associated root system:

$\Phi =\{\lambda _{i}-\lambda _{j}:i\neq j\}$

### sl2(C)

For example, in ${\mathfrak {sl}}_{2}(\mathbb {C} )$ the decomposition is

${\mathfrak {sl}}_{2}={\mathfrak {h}}\oplus {\mathfrak {g}}_{\lambda _{1}-\lambda _{2}}\oplus {\mathfrak {g}}_{\lambda _{2}-\lambda _{1}}$

and the associated root system is

$\Phi =\{\lambda _{1}-\lambda _{2},\lambda _{2}-\lambda _{1}\}$

### sl3(C)

In ${\mathfrak {sl}}_{3}(\mathbb {C} )$ the decomposition is

${\mathfrak {sl}}_{3}={\mathfrak {h}}\oplus {\mathfrak {g}}_{\lambda _{1}-\lambda _{2}}\oplus {\mathfrak {g}}_{\lambda _{1}-\lambda _{3}}\oplus {\mathfrak {g}}_{\lambda _{2}-\lambda _{3}}\oplus {\mathfrak {g}}_{\lambda _{2}-\lambda _{1}}\oplus {\mathfrak {g}}_{\lambda _{3}-\lambda _{1}}\oplus {\mathfrak {g}}_{\lambda _{3}-\lambda _{2}}$

and the associated root system is given by

$\Phi =\{\pm (\lambda _{1}-\lambda _{2}),\pm (\lambda _{1}-\lambda _{3}),\pm (\lambda _{2}-\lambda _{3})\}$

## Examples

As noted in #Structure, semisimple Lie algebras over $\mathbb {C}$ (or more generally an algebraically closed field of characteristic zero) are classified by the root system associated to their Cartan subalgebras, and the root systems, in turn, are classified by their Dynkin diagrams. Examples of semisimple Lie algebras, the classical Lie algebras, with notation coming from their Dynkin diagrams, are:

- $A_{n}:$ ${\mathfrak {sl}}_{n+1}$ , the special linear Lie algebra.
- $B_{n}:$ ${\mathfrak {so}}_{2n+1}$ , the odd-dimensional special orthogonal Lie algebra.
- $C_{n}:$ ${\mathfrak {sp}}_{2n}$ , the symplectic Lie algebra.
- $D_{n}:$ ${\mathfrak {so}}_{2n}$ , the even-dimensional special orthogonal Lie algebra ( $n>1$ ).

The restriction $n>1$ in the $D_{n}$ family is needed because ${\mathfrak {so}}_{2}$ is one-dimensional and commutative and therefore not semisimple.

These Lie algebras are numbered so that *n* is the rank. Almost all of these semisimple Lie algebras are actually simple and the members of these families are almost all distinct, except for some collisions in small rank. For example ${\mathfrak {so}}_{4}\cong {\mathfrak {so}}_{3}\oplus {\mathfrak {so}}_{3}$ and ${\mathfrak {sp}}_{2}\cong {\mathfrak {so}}_{5}$ . These four families, together with five exceptions (E6, E7, E8, F4, and G2), are in fact the *only* simple Lie algebras over the complex numbers.

## Classification

Every semisimple Lie algebra over an algebraically closed field of characteristic 0 is a direct sum of simple Lie algebras (by definition), and the finite-dimensional simple Lie algebras fall in four families – An, Bn, Cn, and Dn – with five exceptions E6, E7, E8, F4, and G2. Simple Lie algebras are classified by the connected Dynkin diagrams, shown on the right, while semisimple Lie algebras correspond to not necessarily connected Dynkin diagrams, where each component of the diagram corresponds to a summand of the decomposition of the semisimple Lie algebra into simple Lie algebras.

The classification proceeds by considering a Cartan subalgebra (see below) and its adjoint action on the Lie algebra. The root system of the action then both determines the original Lie algebra and must have a very constrained form, which can be classified by the Dynkin diagrams. See the section below describing Cartan subalgebras and root systems for more details.

The classification is widely considered one of the most elegant results in mathematics – a brief list of axioms yields, via a relatively short proof, a complete but non-trivial classification with surprising structure. This should be compared to the classification of finite simple groups, which is significantly more complicated.

The enumeration of the four families is non-redundant and consists only of simple algebras if $n\geq 1$ for An, $n\geq 2$ for Bn, $n\geq 3$ for Cn, and $n\geq 4$ for Dn. If one starts numbering lower, the enumeration is redundant, and one has exceptional isomorphisms between simple Lie algebras, which are reflected in isomorphisms of Dynkin diagrams; the En can also be extended down, but below E6 are isomorphic to other, non-exceptional algebras.

Over a non-algebraically closed field, the classification is more complicated – one classifies simple Lie algebras over the algebraic closure, then for each of these, one classifies simple Lie algebras over the original field which have this form (over the closure). For example, to classify simple real Lie algebras, one classifies real Lie algebras with a given complexification, which are known as real forms of the complex Lie algebra; this can be done by Satake diagrams, which are Dynkin diagrams with additional data ("decorations").

## Representation theory of semisimple Lie algebras

Let ${\mathfrak {g}}$ be a (finite-dimensional) semisimple Lie algebra over an algebraically closed field of characteristic zero. Then, as in #Structure, ${\textstyle {\mathfrak {g}}={\mathfrak {h}}\oplus \bigoplus _{\alpha \in \Phi }{\mathfrak {g}}_{\alpha }}$ where $\Phi$ is the root system. Choose the simple roots in $\Phi$ ; a root $\alpha$ of $\Phi$ is then called positive and is denoted by $\alpha >0$ if it is a linear combination of the simple roots with non-negative integer coefficients. Let ${\textstyle {\mathfrak {b}}={\mathfrak {h}}\oplus \bigoplus _{\alpha >0}{\mathfrak {g}}_{\alpha }}$ , which is a maximal solvable subalgebra of ${\mathfrak {g}}$ , the Borel subalgebra.

Let *V* be a (possibly-infinite-dimensional) simple ${\mathfrak {g}}$ -module. If *V* happens to admit a ${\mathfrak {b}}$ -weight vector $v_{0}$ , then it is unique up to scaling and is called the highest weight vector of *V*. It is also an ${\mathfrak {h}}$ -weight vector and the ${\mathfrak {h}}$ -weight of $v_{0}$ , a linear functional of ${\mathfrak {h}}$ , is called the highest weight of *V*. The basic yet nontrivial facts then are (1) to each linear functional $\mu \in {\mathfrak {h}}^{*}$ , there exists a simple ${\mathfrak {g}}$ -module $V^{\mu }$ having $\mu$ as its highest weight and (2) two simple modules having the same highest weight are equivalent. In short, there exists a bijection between ${\mathfrak {h}}^{*}$ and the set of the equivalence classes of simple ${\mathfrak {g}}$ -modules admitting a Borel-weight vector.

For applications, one is often interested in a finite-dimensional simple ${\mathfrak {g}}$ -module (a finite-dimensional irreducible representation). This is especially the case when ${\mathfrak {g}}$ is the Lie algebra of a Lie group (or complexification of such), since, via the Lie correspondence, a Lie algebra representation can be integrated to a Lie group representation when the obstructions are overcome. The next criterion then addresses this need: by the positive Weyl chamber $C\subset {\mathfrak {h}}^{*}$ , we mean the convex cone $C=\{\mu \in {\mathfrak {h}}^{*}|\mu (h_{\alpha })\geq 0,\alpha \in \Phi >0\}$ where $h_{\alpha }\in [{\mathfrak {g}}_{\alpha },{\mathfrak {g}}_{-\alpha }]$ is a unique vector such that $\alpha (h_{\alpha })=2$ . The criterion then reads:

- $\dim V^{\mu }<\infty$ if and only if, for each positive root $\alpha >0$ , (1) $\mu (h_{\alpha })$ is an integer and (2) $\mu$ lies in C .

A linear functional $\mu$ satisfying the above equivalent condition is called a dominant integral weight. Hence, in summary, there exists a bijection between the dominant integral weights and the equivalence classes of finite-dimensional simple ${\mathfrak {g}}$ -modules, the result known as the theorem of the highest weight. The character of a finite-dimensional simple module in turns is computed by the Weyl character formula.

The theorem due to Weyl says that, over a field of characteristic zero, every finite-dimensional module of a semisimple Lie algebra ${\mathfrak {g}}$ is completely reducible; i.e., it is a direct sum of simple ${\mathfrak {g}}$ -modules. Hence, the above results then apply to finite-dimensional representations of a semisimple Lie algebra.

## Real semisimple Lie algebra

For a semisimple Lie algebra over a field that has characteristic zero but is not algebraically closed, there is no general structure theory like the one for those over an algebraically closed field of characteristic zero. But over the field of real numbers, there are still the structure results.

Let ${\mathfrak {g}}$ be a finite-dimensional real semisimple Lie algebra and ${\mathfrak {g}}^{\mathbb {C} }={\mathfrak {g}}\otimes _{\mathbb {R} }\mathbb {C}$ the complexification of it (which is again semisimple). The real Lie algebra ${\mathfrak {g}}$ is called a real form of ${\mathfrak {g}}^{\mathbb {C} }$ . A real form is called a compact form if the Killing form on it is negative-definite; it is necessarily the Lie algebra of a compact Lie group (hence, the name).

### Compact case

Suppose ${\mathfrak {g}}$ is a compact form and ${\mathfrak {h}}\subset {\mathfrak {g}}$ a maximal abelian subspace. One can show (for example, from the fact ${\mathfrak {g}}$ is the Lie algebra of a compact Lie group) that $\operatorname {ad} ({\mathfrak {h}})$ consists of skew-Hermitian matrices, diagonalizable over $\mathbb {C}$ with imaginary eigenvalues. Hence, ${\mathfrak {h}}^{\mathbb {C} }$ is a Cartan subalgebra of ${\mathfrak {g}}^{\mathbb {C} }$ and there results in the root space decomposition (cf. #Structure)

${\mathfrak {g}}^{\mathbb {C} }={\mathfrak {h}}^{\mathbb {C} }\oplus \bigoplus _{\alpha \in \Phi }{\mathfrak {g}}_{\alpha }$

where each $\alpha \in \Phi$ is real-valued on $i{\mathfrak {h}}$ ; thus, can be identified with a real-linear functional on the real vector space $i{\mathfrak {h}}$ .

For example, let ${\mathfrak {g}}={\mathfrak {su}}(n)$ and take ${\mathfrak {h}}\subset {\mathfrak {g}}$ the subspace of all diagonal matrices. Note ${\mathfrak {g}}^{\mathbb {C} }={\mathfrak {sl}}_{n}\mathbb {C}$ . Let $e_{i}$ be the linear functional on ${\mathfrak {h}}^{\mathbb {C} }$ given by $e_{i}(H)=h_{i}$ for $H=\operatorname {diag} (h_{1},\dots ,h_{n})$ . Then for each $H\in {\mathfrak {h}}^{\mathbb {C} }$ ,

$[H,E_{ij}]=(e_{i}(H)-e_{j}(H))E_{ij}$

where $E_{ij}$ is the matrix that has 1 on the $(i,j)$ -th spot and zero elsewhere. Hence, each root $\alpha$ is of the form $\alpha =e_{i}-e_{j},i\neq j$ and the root space decomposition is the decomposition of matrices:

${\mathfrak {g}}^{\mathbb {C} }={\mathfrak {h}}^{\mathbb {C} }\oplus \bigoplus _{i\neq j}\mathbb {C} E_{ij}.$

### Noncompact case

Suppose ${\mathfrak {g}}$ is not necessarily a compact form (i.e., the signature of the Killing form is not all negative). Suppose, moreover, it has a Cartan involution $\theta$ and let ${\mathfrak {g}}={\mathfrak {k}}\oplus {\mathfrak {p}}$ be the eigenspace decomposition of $\theta$ , where ${\mathfrak {k}},{\mathfrak {p}}$ are the eigenspaces for 1 and -1, respectively. For example, if ${\mathfrak {g}}={\mathfrak {sl}}_{n}\mathbb {R}$ and $\theta$ the negative transpose, then ${\mathfrak {k}}={\mathfrak {so}}(n)$ .

Let ${\mathfrak {a}}\subset {\mathfrak {p}}$ be a maximal abelian subspace. Now, $\operatorname {ad} ({\mathfrak {p}})$ consists of symmetric matrices (with respect to a suitable inner product) and thus the operators in $\operatorname {ad} ({\mathfrak {a}})$ are simultaneously diagonalizable, with real eigenvalues. By repeating the arguments for the algebraically closed base field, one obtains the decomposition (called the **restricted root space decomposition**):

${\mathfrak {g}}={\mathfrak {g}}_{0}\oplus \bigoplus _{\alpha \in \Phi }{\mathfrak {g}}_{\alpha }$

where

- the elements in $\Phi$ are called the restricted roots,
- $\theta ({\mathfrak {g}}_{\alpha })={\mathfrak {g}}_{-\alpha }$ for any linear functional $\alpha$ ; in particular, $-\Phi \subset \Phi$ ,
- ${\mathfrak {g}}_{0}={\mathfrak {a}}\oplus Z_{\mathfrak {k}}({\mathfrak {a}})$ .

Moreover, $\Phi$ is a root system but not necessarily reduced one (i.e., it can happen $\alpha ,2\alpha$ are both roots).

## The case of sl(n,C)

If ${\mathfrak {g}}=\mathrm {sl} (n,\mathbb {C} )$ , then ${\mathfrak {h}}$ may be taken to be the diagonal subalgebra of ${\mathfrak {g}}$ , consisting of diagonal matrices whose diagonal entries sum to zero. Since ${\mathfrak {h}}$ has dimension $n-1$ , we see that $\mathrm {sl} (n;\mathbb {C} )$ has rank $n-1$ .

The root vectors X in this case may be taken to be the matrices $E_{i,j}$ with $i\neq j$ , where $E_{i,j}$ is the matrix with a 1 in the $(i,j)$ spot and zeros elsewhere. If H is a diagonal matrix with diagonal entries $\lambda _{1},\ldots ,\lambda _{n}$ , then we have

$[H,E_{i,j}]=(\lambda _{i}-\lambda _{j})E_{i,j}$

.

Thus, the roots for $\mathrm {sl} (n,\mathbb {C} )$ are the linear functionals $\alpha _{i,j}$ given by

$\alpha _{i,j}(H)=\lambda _{i}-\lambda _{j}$

.

After identifying ${\mathfrak {h}}$ with its dual, the roots become the vectors $\alpha _{i,j}:=e_{i}-e_{j}$ in the space of n -tuples that sum to zero. This is the root system known as $A_{n-1}$ in the conventional labeling.

The reflection associated to the root $\alpha _{i,j}$ acts on ${\mathfrak {h}}$ by transposing the i and j diagonal entries. The Weyl group is then just the permutation group on n elements, acting by permuting the diagonal entries of matrices in ${\mathfrak {h}}$ .

## Generalizations

Semisimple Lie algebras admit certain generalizations. Firstly, many statements that are true for semisimple Lie algebras are true more generally for reductive Lie algebras. Abstractly, a reductive Lie algebra is one whose adjoint representation is completely reducible, while concretely, a reductive Lie algebra is a direct sum of a semisimple Lie algebra and an abelian Lie algebra; for example, ${\mathfrak {sl}}_{n}$ is semisimple, and ${\mathfrak {gl}}_{n}$ is reductive. Many properties of semisimple Lie algebras depend only on reducibility.

Many properties of complex semisimple/reductive Lie algebras are true not only for semisimple/reductive Lie algebras over algebraically closed fields, but more generally for split semisimple/reductive Lie algebras over other fields: semisimple/reductive Lie algebras over algebraically closed fields are always split, but over other fields this is not always the case. Split Lie algebras have essentially the same representation theory as semisimple Lie algebras over algebraically closed fields, for instance, the splitting Cartan subalgebra playing the same role as the Cartan subalgebra plays over algebraically closed fields. This is the approach followed in (Bourbaki 2005), for instance, which classifies representations of split semisimple/reductive Lie algebras.

## Semisimple and reductive groups

A connected Lie group is called semisimple if its Lie algebra is a semisimple Lie algebra, i.e. a direct sum of simple Lie algebras. It is called reductive if its Lie algebra is a direct sum of simple and trivial (one-dimensional) Lie algebras. Reductive groups occur naturally as symmetries of a number of mathematical objects in algebra, geometry, and physics. For example, the group $GL_{n}(\mathbb {R} )$ of symmetries of an *n*-dimensional real vector space (equivalently, the group of invertible matrices) is reductive.
