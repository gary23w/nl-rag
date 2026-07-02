---
title: "Cartan subalgebra"
source: https://en.wikipedia.org/wiki/Cartan_subalgebra
domain: lie-algebras
license: CC-BY-SA-4.0
tags: lie algebra, semisimple lie algebra, cartan subalgebra, killing form
fetched: 2026-07-02
---

# Cartan subalgebra

In mathematics, a **Cartan subalgebra**, often abbreviated as **CSA**, is a nilpotent subalgebra ${\mathfrak {h}}$ of a Lie algebra ${\mathfrak {g}}$ that is self-normalising (if $[X,Y]\in {\mathfrak {h}}$ for all $X\in {\mathfrak {h}}$ , then $Y\in {\mathfrak {h}}$ ). They were introduced by Élie Cartan in his doctoral thesis, and control the representation theory of a semi-simple Lie algebra ${\mathfrak {g}}$ over a field of characteristic 0 .

In a finite-dimensional semisimple Lie algebra over an algebraically closed field of characteristic zero (e.g., $\mathbb {C}$ ), a Cartan subalgebra is the same thing as a maximal abelian subalgebra consisting of elements *x* such that the adjoint endomorphism $\operatorname {ad} (x):{\mathfrak {g}}\to {\mathfrak {g}}$ is semisimple (i.e., diagonalizable). Sometimes this characterization is simply taken as the definition of a Cartan subalgebra.pg 231

In general, a subalgebra is called toral if it consists of semisimple elements. Over an algebraically closed field, a toral subalgebra is automatically abelian. Thus, over an algebraically closed field of characteristic zero, a Cartan subalgebra can also be defined as a maximal toral subalgebra.

Kac–Moody algebras and generalized Kac–Moody algebras also have subalgebras that play the same role as the Cartan subalgebras of semisimple Lie algebras (over a field of characteristic zero).

## Existence and uniqueness

Cartan subalgebras exist for finite-dimensional Lie algebras whenever the base field is infinite. One way to construct a Cartan subalgebra is by means of a regular element. Over a finite field, the question of the existence is still open.

For a finite-dimensional semisimple Lie algebra ${\mathfrak {g}}$ over an algebraically closed field of characteristic zero, there is a simpler approach: by definition, a toral subalgebra is a subalgebra of ${\mathfrak {g}}$ that consists of semisimple elements (an element is semisimple if the adjoint endomorphism induced by it is diagonalizable). A Cartan subalgebra of ${\mathfrak {g}}$ is then the same thing as a maximal toral subalgebra and the existence of a maximal toral subalgebra is easy to see.

In a finite-dimensional Lie algebra over an algebraically closed field of characteristic zero, all Cartan subalgebras are conjugate under automorphisms of the algebra, and in particular are all isomorphic. The common dimension of a Cartan subalgebra is then called the rank of the algebra.

For a finite-dimensional complex semisimple Lie algebra, the existence of a Cartan subalgebra is much simpler to establish, assuming the existence of a compact real form. In that case, ${\mathfrak {h}}$ may be taken as the complexification of the Lie algebra of a maximal torus of the compact group.

If ${\mathfrak {g}}$ is a linear Lie algebra (a Lie subalgebra of the Lie algebra of endomorphisms of a finite-dimensional vector space *V*) over an algebraically closed field, then any Cartan subalgebra of ${\mathfrak {g}}$ is the centralizer of a maximal toral subalgebra of ${\mathfrak {g}}$ . If ${\mathfrak {g}}$ is semisimple and the field has characteristic zero, then a maximal toral subalgebra is self-normalizing, and so is equal to the associated Cartan subalgebra. If in addition ${\mathfrak {g}}$ is semisimple, then the adjoint representation presents ${\mathfrak {g}}$ as a linear Lie algebra, so that a subalgebra of ${\mathfrak {g}}$ is Cartan if and only if it is a maximal toral subalgebra.

## Examples

- Any nilpotent Lie algebra is its own Cartan subalgebra.
- The algebra of all diagonal matrices is a Cartan subalgebra of ${\mathfrak {gl}}_{n}$ , the Lie algebra of $n\times n$ matrices over a field.
- For the special Lie algebra of traceless $n\times n$ matrices ${\mathfrak {sl}}_{n}(\mathbb {C} )$ , it has the Cartan subalgebra: ${\mathfrak {h}}=\left\{d(a_{1},\ldots ,a_{n})\mid a_{i}\in \mathbb {C} {\text{ and }}\sum _{i=1}^{n}a_{i}=0\right\}$ where $d(a_{1},\ldots ,a_{n})={\begin{pmatrix}a_{1}&0&\cdots &0\\0&\ddots &&0\\\vdots &&\ddots &\vdots \\0&\cdots &\cdots &a_{n}\end{pmatrix}}$ For example, in ${\mathfrak {sl}}_{2}(\mathbb {C} )$ the Cartan subalgebra is the subalgebra of matrices: ${\mathfrak {h}}=\left\{{\begin{pmatrix}a&0\\0&-a\end{pmatrix}}:a\in \mathbb {C} \right\}$ with Lie bracket given by the matrix commutator.
- The Lie algebra ${\mathfrak {sl}}_{2}(\mathbb {R} )$ of 2 by 2 matrices of trace 0 has two non-conjugate Cartan subalgebras.
- The dimension of a Cartan subalgebra is not in general the maximal dimension of an abelian subalgebra, even for complex simple Lie algebras. For example, the Lie algebra ${\mathfrak {sl}}_{2n}(\mathbb {C} )$ of $2n$ by $2n$ matrices of trace 0 has a Cartan subalgebra of rank $2n-1$ but has a maximal abelian subalgebra of dimension $n^{2}$ consisting of all matrices of the form ${\begin{pmatrix}0&A\\0&0\end{pmatrix}}$ with A any n by n matrix. One can directly see this abelian subalgebra is not a Cartan subalgebra, since it is contained in the nilpotent algebra of strictly upper triangular matrices (or, since it is normalized by diagonal matrices).

## Cartan subalgebras of semisimple Lie algebras

For finite-dimensional semisimple Lie algebra ${\mathfrak {g}}$ over an algebraically closed field of characteristic 0, a Cartan subalgebra ${\mathfrak {h}}$ has the following properties:

- ${\mathfrak {h}}$ is abelian,
- For the adjoint representation $\operatorname {ad$ , the image $\operatorname {ad} ({\mathfrak {h}})$ consists of semisimple operators (i.e., diagonalizable matrices).

(As noted earlier, a Cartan subalgebra can in fact be characterized as a subalgebra that is maximal among those having the above two properties.)

These two properties say that the operators in $\operatorname {ad} ({\mathfrak {h}})$ are simultaneously diagonalizable and that there is a direct sum decomposition of ${\mathfrak {g}}$ as:

${\mathfrak {g}}=\bigoplus _{\lambda \in {\mathfrak {h}}^{*}}{\mathfrak {g}}_{\lambda }$

where

${\mathfrak {g}}_{\lambda }=\{x\in {\mathfrak {g}}:{\text{ad}}(h)x=\lambda (h)x,{\text{ for }}h\in {\mathfrak {h}}\}$

.

Let $\Phi =\{\lambda \in {\mathfrak {h}}^{*}\setminus \{0\}|{\mathfrak {g}}_{\lambda }\neq \{0\}\}$ . Then $\Phi$ is a root system and, moreover, ${\mathfrak {g}}_{0}={\mathfrak {h}}$ ; i.e., the centralizer of ${\mathfrak {h}}$ coincides with ${\mathfrak {h}}$ . The above decomposition can then be written as:

${\mathfrak {g}}={\mathfrak {h}}\oplus \left(\bigoplus _{\lambda \in \Phi }{\mathfrak {g}}_{\lambda }\right)$

As it turns out, for each $\lambda \in \Phi$ , ${\mathfrak {g}}_{\lambda }$ has dimension one and so:

$\dim {\mathfrak {g}}=\dim {\mathfrak {h}}+\#\Phi$

.

See also Semisimple Lie algebra#Structure for further information.

### Decomposing representations with dual Cartan subalgebra

Given a Lie algebra ${\mathfrak {g}}$ over a field of characteristic 0 , and a Lie algebra representation ${\displaystyle \sigma$ there is a decomposition related to the decomposition of the Lie algebra from its Cartan subalgebra. If we set $V_{\lambda }=\{v\in V:(\sigma (h))(v)=\lambda (h)v{\text{ for }}h\in {\mathfrak {h}}\}$ with $\lambda \in {\mathfrak {h}}^{*}$ , called the **weight space for weight** $\lambda$ , there is a decomposition of the representation in terms of these weight spaces $V=\bigoplus _{\lambda \in {\mathfrak {h}}^{*}}V_{\lambda }$ In addition, whenever $V_{\lambda }\neq \{0\}$ we call $\lambda$ a **weight** of the ${\mathfrak {g}}$ -representation V .

#### Classification of irreducible representations using weights

But, it turns out these weights can be used to classify the irreducible representations of the Lie algebra ${\mathfrak {g}}$ . For a finite dimensional irreducible ${\mathfrak {g}}$ -representation V , there exists a unique weight $\lambda \in \Phi$ with respect to a partial ordering on ${\mathfrak {h}}^{*}$ . Moreover, given a $\lambda \in \Phi$ such that $\langle \alpha ,\lambda \rangle \in \mathbb {N}$ for every positive root $\alpha \in \Phi ^{+}$ , there exists a unique irreducible representation $L^{+}(\lambda )$ . This means the root system $\Phi$ contains all information about the representation theory of ${\mathfrak {g}}$ .pg 240

## Splitting Cartan subalgebra

Over non-algebraically closed fields, not all Cartan subalgebras are conjugate. An important class are splitting Cartan subalgebras: if a Lie algebra admits a splitting Cartan subalgebra ${\mathfrak {h}}$ then it is called *splittable,* and the pair $({\mathfrak {g}},{\mathfrak {h}})$ is called a split Lie algebra; over an algebraically closed field every semisimple Lie algebra is splittable. Any two splitting Cartan algebras are conjugate, and they fulfill a similar function to Cartan algebras in semisimple Lie algebras over algebraically closed fields, so split semisimple Lie algebras (indeed, split reductive Lie algebras) share many properties with semisimple Lie algebras over algebraically closed fields.

Over a non-algebraically closed field not every semisimple Lie algebra is splittable, however.

## Cartan subgroup

A Cartan subgroup of a Lie group is a special type of subgroup. Specifically, its Lie algebra (which captures the group’s algebraic structure) is itself a Cartan subalgebra. When we consider the identity component of a subgroup, it shares the same Lie algebra. However, there isn’t a universally agreed-upon definition for which subgroup with this property should be called the ‘Cartan subgroup,’ especially when dealing with disconnected groups.

For compact connected Lie groups, a Cartan subgroup is essentially a maximal connected Abelian subgroup—often referred to as a ‘maximal torus.’ The Lie algebra associated with this subgroup is also a Cartan subalgebra.

Now, when we explore disconnected compact Lie groups, things get interesting. There are multiple definitions for a Cartan subgroup. One common approach, proposed by David Vogan, defines it as the group of elements that normalize a fixed maximal torus while preserving the fundamental Weyl chamber. This version is sometimes called the ‘large Cartan subgroup.’ Additionally, there exists a ‘small Cartan subgroup,’ defined as the centralizer of a maximal torus. It’s important to note that these Cartan subgroups may not always be abelian in general.

### Examples of Cartan Subgroups

- The subgroup in GL2(**R**) consisting of diagonal matrices.
