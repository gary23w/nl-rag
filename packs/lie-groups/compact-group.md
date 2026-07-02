---
title: "Compact group"
source: https://en.wikipedia.org/wiki/Compact_group
domain: lie-groups
license: CC-BY-SA-4.0
tags: lie group, lie theory, compact group, maximal torus
fetched: 2026-07-02
---

# Compact group

In mathematics, a **compact** (**topological**) **group** is a topological group whose topology realizes it as a compact topological space. Compact groups are a natural generalization of finite groups with the discrete topology and have properties that carry over in significant fashion. Compact groups have a well-understood theory, in relation to group actions and representation theory.

In the following we will assume all groups are Hausdorff spaces.

## Compact Lie groups

Lie groups form a class of topological groups, and the compact Lie groups have a particularly well-developed theory. Basic examples of compact Lie groups include

- the circle group **T** and the torus groups **T***n*,
- the orthogonal group O(*n*), the special orthogonal group SO(*n*) and its covering spin group Spin(*n*),
- the compact symplectic group USp(*n*),
- the unitary group U(*n*) and the special unitary group SU(*n*),
- the compact forms of the exceptional Lie groups: G2, F4, E6, E7, and E8.

The classification theorem of compact Lie groups states that up to finite extensions and finite covers this exhausts the list of examples (which already includes some redundancies). This classification is described in more detail in the next subsection.

### Classification

Any compact Lie group *G* has an identity component *G*0, defined as the connected component of the group in which the identity element lies. The quotient group *G*/*G*0 is the group of components π0(*G*) which must be finite since *G* is compact. We therefore have a finite extension

$1\to G_{0}\to G\to \pi _{0}(G)\to 1.$

Meanwhile, for connected compact Lie groups, we have the following result:

Theorem

: Every connected compact Lie group is the quotient by a finite central subgroup of a product of a simply connected compact Lie group and a torus.

Thus, the classification of connected compact Lie groups can in principle be reduced to knowledge of the simply connected compact Lie groups together with information about their centers. (For information about the center, see the section below on fundamental group and center.)

Finally, every compact, connected, simply-connected Lie group *K* is a product of finitely many compact, connected, simply-connected simple Lie groups *K**i* each of which is isomorphic to exactly one of the following:

- The compact symplectic group $\operatorname {Sp} (n),\,n\geq 1$
- The special unitary group $\operatorname {SU} (n),\,n\geq 3$
- The spin group $\operatorname {Spin} (n),\,n\geq 7$

or one of the five exceptional groups G2, F4, E6, E7, and E8. The restrictions on *n* are to avoid special isomorphisms among the various families for small values of *n*. For each of these groups, the center is known explicitly. The classification is through the associated root system (for a fixed maximal torus), which in turn are classified by their Dynkin diagrams.

The classification of compact, simply connected Lie groups is the same as the classification of complex semisimple Lie algebras. Indeed, if *K* is a simply connected compact Lie group, then the complexification of the Lie algebra of *K* is semisimple. Conversely, every complex semisimple Lie algebra has a compact real form isomorphic to the Lie algebra of a compact, simply connected Lie group.

### Maximal tori and root systems

A key idea in the study of a connected compact Lie group *K* is the concept of a *maximal torus*, that is a subgroup *T* of *K* that is isomorphic to a product of several copies of $S^{1}$ and that is not contained in any larger subgroup of this type. A basic example is the case $K=\operatorname {SU} (n)$ , in which case we may take T to be the group of diagonal elements in K . A basic result is the *torus theorem* which states that every element of K belongs to a maximal torus and that all maximal tori are conjugate.

The maximal torus in a compact group plays a role analogous to that of the Cartan subalgebra in a complex semisimple Lie algebra. In particular, once a maximal torus $T\subset K$ has been chosen, one can define a root system and a Weyl group similar to what one has for semisimple Lie algebras. These structures then play an essential role both in the classification of connected compact groups (described above) and in the representation theory of a fixed such group (described below).

The root systems associated to the simple compact groups appearing in the classification of simply connected compact groups are as follows:

- The special unitary groups $\operatorname {SU} (n)$ correspond to the root system $A_{n-1}$
- The odd spin groups $\operatorname {Spin} (2n+1)$ correspond to the root system $B_{n}$
- The compact symplectic groups $\operatorname {Sp} (n)$ correspond to the root system $C_{n}$
- The even spin groups $\operatorname {Spin} (2n)$ correspond to the root system $D_{n}$
- The exceptional compact Lie groups correspond to the five exceptional root systems G2, F4, E6, E7, or E8

### Fundamental group and center

It is important to know whether a connected compact Lie group is simply connected, and if not, to determine its fundamental group. For compact Lie groups, there are two basic approaches to computing the fundamental group. The first approach applies to the classical compact groups $\operatorname {SU} (n)$ , $\operatorname {U} (n)$ , $\operatorname {SO} (n)$ , and $\operatorname {Sp} (n)$ and proceeds by induction on n . The second approach uses the root system and applies to all connected compact Lie groups.

It is also important to know the center of a connected compact Lie group. The center of a classical group G can easily be computed "by hand," and in most cases consists simply of whatever roots of the identity are in G . (The group SO(2) is an exception—the center is the whole group, even though most elements are not roots of the identity.) Thus, for example, the center of $\operatorname {SU} (n)$ consists of *n*th roots of unity times the identity, a cyclic group of order n .

In general, the center can be expressed in terms of the root lattice and the kernel of the exponential map for the maximal torus. The general method shows, for example, that the simply connected compact group corresponding to the exceptional root system $G_{2}$ has trivial center. Thus, the compact $G_{2}$ group is one of very few simple compact groups that are simultaneously simply connected and center free. (The others are $F_{4}$ and $E_{8}$ .)

## Further examples

Amongst groups that are not Lie groups, and so do not carry the structure of a manifold, examples are the additive group *Z**p* of p-adic integers, and constructions from it. In fact any profinite group is a compact group. This means that Galois groups are compact groups, a basic fact for the theory of algebraic extensions in the case of infinite degree.

Pontryagin duality provides a large supply of examples of compact commutative groups. These are in duality with abelian discrete groups.

## Haar measure

Compact groups all carry a Haar measure, which will be invariant by both left and right translation (the modulus function must be a continuous homomorphism to positive reals (**R**+, ×), and so 1). In other words, these groups are unimodular. Haar measure is easily normalized to be a probability measure, analogous to dθ/2π on the circle.

Such a Haar measure is in many cases easy to compute; for example for orthogonal groups it was known to Adolf Hurwitz, and in the Lie group cases can always be given by an invariant differential form. In the profinite case there are many subgroups of finite index, and Haar measure of a coset will be the reciprocal of the index. Therefore, integrals are often computable quite directly, a fact applied constantly in number theory.

If K is a compact group and m is the associated Haar measure, the Peter–Weyl theorem provides a decomposition of $L^{2}(K,dm)$ as an orthogonal direct sum of finite-dimensional subspaces of matrix entries for the irreducible representations of K .

## Representation theory

The representation theory of compact groups (not necessarily Lie groups and not necessarily connected) was founded by the Peter–Weyl theorem. Hermann Weyl went on to give the detailed character theory of the compact connected Lie groups, based on maximal torus theory. The resulting Weyl character formula was one of the influential results of twentieth century mathematics. The combination of the Peter–Weyl theorem and the Weyl character formula led Weyl to a complete classification of the representations of a connected compact Lie group; this theory is described in the next section.

A combination of Weyl's work and Cartan's theorem gives a survey of the whole representation theory of compact groups *G*. That is, by the Peter–Weyl theorem the irreducible unitary representations ρ of *G* are into a unitary group (of finite dimension) and the image will be a closed subgroup of the unitary group by compactness. Cartan's theorem states that Im(ρ) must itself be a Lie subgroup in the unitary group. If *G* is not itself a Lie group, there must be a kernel to ρ. Further one can form an inverse system, for the kernel of ρ smaller and smaller, of finite-dimensional unitary representations, which identifies *G* as an inverse limit of compact Lie groups. Here the fact that in the limit a faithful representation of *G* is found is another consequence of the Peter–Weyl theorem.

The unknown part of the representation theory of compact groups is thereby, roughly speaking, thrown back onto the complex representations of finite groups. This theory is rather rich in detail, but is qualitatively well understood.

## Representation theory of a connected compact Lie group

Certain simple examples of the representation theory of compact Lie groups can be worked out by hand, such as the representations of the rotation group SO(3), the special unitary group SU(2), and the special unitary group SU(3). We focus here on the general theory. See also the parallel theory of representations of a semisimple Lie algebra.

Throughout this section, we fix a connected compact Lie group *K* and a maximal torus *T* in *K*.

### Representation theory of *T*

Since *T* is commutative, Schur's lemma tells us that each irreducible representation $\rho$ of *T* is one-dimensional:

$\rho :T\rightarrow GL(1;\mathbb {C} )=\mathbb {C} ^{*}.$

Since, also, *T* is compact, $\rho$ must actually map into $S^{1}\subset \mathbb {C}$ .

To describe these representations concretely, we let ${\mathfrak {t}}$ be the Lie algebra of *T* and we write points $h\in T$ as

$h=e^{H},\quad H\in {\mathfrak {t}}.$

In such coordinates, $\rho$ will have the form

$\rho (e^{H})=e^{i\lambda (H)}$

for some linear functional $\lambda$ on ${\mathfrak {t}}$ .

Now, since the exponential map $H\mapsto e^{H}$ is not injective, not every such linear functional $\lambda$ gives rise to a well-defined map of *T* into $S^{1}$ . Rather, let $\Gamma$ denote the kernel of the exponential map:

$\Gamma =\left\{H\in {\mathfrak {t}}\mid e^{2\pi H}=\operatorname {Id} \right\},$

where $\operatorname {Id}$ is the identity element of *T*. (We scale the exponential map here by a factor of $2\pi$ in order to avoid such factors elsewhere.) Then for $\lambda$ to give a well-defined map $\rho$ , $\lambda$ must satisfy

$\lambda (H)\in \mathbb {Z} ,\quad H\in \Gamma ,$

where $\mathbb {Z}$ is the set of integers. A linear functional $\lambda$ satisfying this condition is called an **analytically integral element**. This integrality condition is related to, but not identical to, the notion of integral element in the setting of semisimple Lie algebras.

Suppose, for example, *T* is just the group $S^{1}$ of complex numbers $e^{i\theta }$ of absolute value 1. The Lie algebra is the set of purely imaginary numbers, $H=i\theta ,\,\theta \in \mathbb {R} ,$ and the kernel of the (scaled) exponential map is the set of numbers of the form $in$ where n is an integer. A linear functional $\lambda$ takes integer values on all such numbers if and only if it is of the form $\lambda (i\theta )=k\theta$ for some integer k . The irreducible representations of *T* in this case are one-dimensional and of the form

$\rho (e^{i\theta })=e^{ik\theta },\quad k\in \mathbb {Z} .$

### Representation theory of *K*

We now let $\Sigma$ denote a finite-dimensional irreducible representation of *K* (over $\mathbb {C}$ ). We then consider the restriction of $\Sigma$ to *T*. This restriction is not irreducible unless $\Sigma$ is one-dimensional. Nevertheless, the restriction decomposes as a direct sum of irreducible representations of *T*. (Note that a given irreducible representation of *T* may occur more than once.) Now, each irreducible representation of *T* is described by a linear functional $\lambda$ as in the preceding subsection. If a given $\lambda$ occurs at least once in the decomposition of the restriction of $\Sigma$ to *T*, we call $\lambda$ a **weight** of $\Sigma$ . The strategy of the representation theory of *K* is to classify the irreducible representations in terms of their weights.

We now briefly describe the structures needed to formulate the theorem; more details can be found in the article on weights in representation theory. We need the notion of a **root system** for *K* (relative to a given maximal torus *T*). The construction of this root system $R\subset {\mathfrak {t}}$ is very similar to the construction for complex semisimple Lie algebras. Specifically, the weights are the nonzero weights for the adjoint action of *T* on the complexified Lie algebra of *K*. The root system *R* has all the usual properties of a root system, except that the elements of *R* may not span ${\mathfrak {t}}$ . We then choose a base $\Delta$ for *R* and we say that an integral element $\lambda$ is **dominant** if $\lambda (\alpha )\geq 0$ for all $\alpha \in \Delta$ . Finally, we say that one weight is **higher** than another if their difference can be expressed as a linear combination of elements of $\Delta$ with non-negative coefficients.

The irreducible finite-dimensional representations of *K* are then classified by a **theorem of the highest weight**, which is closely related to the analogous theorem classifying representations of a semisimple Lie algebra. The result says that:

1. every irreducible representation has highest weight,
2. the highest weight is always a dominant, analytically integral element,
3. two irreducible representations with the same highest weight are isomorphic, and
4. every dominant, analytically integral element arises as the highest weight of an irreducible representation.

The theorem of the highest weight for representations of *K* is then almost the same as for semisimple Lie algebras, with one notable exception: The concept of an integral element is different. The weights $\lambda$ of a representation $\Sigma$ are analytically integral in the sense described in the previous subsection. Every analytically integral element is integral in the Lie algebra sense, but not the other way around. (This phenomenon reflects that, in general, not every representation of the Lie algebra ${\mathfrak {k}}$ comes from a representation of the group *K*.) On the other hand, if *K* is simply connected, the set of possible highest weights in the group sense is the same as the set of possible highest weights in the Lie algebra sense.

### The Weyl character formula

If $\Pi :K\to \operatorname {GL} (V)$ is representation of *K*, we define the **character** of $\Pi$ to be the function $\mathrm {X} :K\to \mathbb {C}$ given by

$\mathrm {X} (x)=\operatorname {trace} (\Pi (x)),\quad x\in K$

.

This function is easily seen to be a class function, i.e., $\mathrm {X} (xyx^{-1})=\mathrm {X} (y)$ for all x and y in *K*. Thus, $\mathrm {X}$ is determined by its restriction to *T*.

The study of characters is an important part of the representation theory of compact groups. One crucial result, which is a corollary of the Peter–Weyl theorem, is that the characters form an orthonormal basis for the set of square-integrable class functions in *K*. A second key result is the Weyl character formula, which gives an explicit formula for the character—or, rather, the restriction of the character to *T*—in terms of the highest weight of the representation.

In the closely related representation theory of semisimple Lie algebras, the Weyl character formula is an additional result established *after* the representations have been classified. In Weyl's analysis of the compact group case, however, the Weyl character formula is actually a crucial part of the classification itself. Specifically, in Weyl's analysis of the representations of *K*, the hardest part of the theorem—showing that every dominant, analytically integral element is actually the highest weight of some representation—is proved in a totally different way from the usual Lie algebra construction using Verma modules. In Weyl's approach, the construction is based on the Peter–Weyl theorem and an analytic proof of the Weyl character formula. Ultimately, the irreducible representations of *K* are realized inside the space of continuous functions on *K*.

### The SU(2) case

We now consider the case of the compact group SU(2). The representations are often considered from the Lie algebra point of view, but we here look at them from the group point of view. We take the maximal torus to be the set of matrices of the form

${\begin{pmatrix}e^{i\theta }&0\\0&e^{-i\theta }\end{pmatrix}}.$

According to the example discussed above in the section on representations of *T*, the analytically integral elements are labeled by integers, so that the dominant, analytically integral elements are non-negative integers m . The general theory then tells us that for each m , there is a unique irreducible representation of SU(2) with highest weight m .

Much information about the representation corresponding to a given m is encoded in its character. Now, the Weyl character formula says, in this case, that the character is given by

$\mathrm {X} \left({\begin{pmatrix}e^{i\theta }&0\\0&e^{-i\theta }\end{pmatrix}}\right)={\frac {\sin((m+1)\theta )}{\sin(\theta )}}.$

We can also write the character as sum of exponentials as follows:

$\mathrm {X} \left({\begin{pmatrix}e^{i\theta }&0\\0&e^{-i\theta }\end{pmatrix}}\right)=e^{im\theta }+e^{i(m-2)\theta }+\cdots e^{-i(m-2)\theta }+e^{-im\theta }.$

(If we use the formula for the sum of a finite geometric series on the above expression and simplify, we obtain the earlier expression.)

From this last expression and the standard formula for the character in terms of the weights of the representation, we can read off that the weights of the representation are

$m,m-2,\ldots ,-(m-2),-m,$

each with multiplicity one. (The weights are the integers appearing in the exponents of the exponentials and the multiplicities are the coefficients of the exponentials.) Since there are $m+1$ weights, each with multiplicity 1, the dimension of the representation is $m+1$ . Thus, we recover much of the information about the representations that is usually obtained from the Lie algebra computation.

### An outline of the proof

We now outline the proof of the theorem of the highest weight, following the original argument of Hermann Weyl. We continue to let K be a connected compact Lie group and T a fixed maximal torus in K . We focus on the most difficult part of the theorem, showing that every dominant, analytically integral element is the highest weight of some (finite-dimensional) irreducible representation.

The tools for the proof are the following:

- The torus theorem.
- The Weyl integral formula.
- The Peter–Weyl theorem for class functions, which states that the characters of the irreducible representations form an orthonormal basis for the space of square integrable class functions on K .

With these tools in hand, we proceed with the proof. The first major step in the argument is to prove the Weyl character formula. The formula states that if $\Pi$ is an irreducible representation with highest weight $\lambda$ , then the character $\mathrm {X}$ of $\Pi$ satisfies:

$\mathrm {X} (e^{H})={\frac {\sum _{w\in W}\det(w)e^{i\langle w\cdot (\lambda +\rho ),H\rangle }}{\sum _{w\in W}\det(w)e^{i\langle w\cdot \rho ,H\rangle }}}$

for all H in the Lie algebra of T . Here $\rho$ is half the sum of the positive roots. (The notation uses the convention of "real weights"; this convention requires an explicit factor of i in the exponent.) Weyl's proof of the character formula is analytic in nature and hinges on the fact that the $L^{2}$ norm of the character is 1. Specifically, if there were any additional terms in the numerator, the Weyl integral formula would force the norm of the character to be greater than 1.

Next, we let $\Phi _{\lambda }$ denote the function on the right-hand side of the character formula. We show that *even if $\lambda$ is not known to be the highest weight of a representation*, $\Phi _{\lambda }$ is a well-defined, Weyl-invariant function on T , which therefore extends to a class function on K . Then using the Weyl integral formula, one can show that as $\lambda$ ranges over the set of dominant, analytically integral elements, the functions $\Phi _{\lambda }$ form an orthonormal family of class functions. We emphasize that we do not currently know that every such $\lambda$ is the highest weight of a representation; nevertheless, the expressions on the right-hand side of the character formula gives a well-defined set of functions $\Phi _{\lambda }$ , and these functions are orthonormal.

Now comes the conclusion. The set of all $\Phi _{\lambda }$ —with $\lambda$ ranging over the dominant, analytically integral elements—forms an orthonormal set in the space of square integrable class functions. But by the Weyl character formula, the characters of the irreducible representations form a subset of the $\Phi _{\lambda }$ 's. And by the Peter–Weyl theorem, the characters of the irreducible representations form an orthonormal basis for the space of square integrable class functions. If there were some $\lambda$ that is not the highest weight of a representation, then the corresponding $\Phi _{\lambda }$ would not be the character of a representation. Thus, the characters would be a *proper* subset of the set of $\Phi _{\lambda }$ 's. But then we have an impossible situation: an orthonormal *basis* (the set of characters of the irreducible representations) would be contained in a strictly larger orthonormal set (the set of $\Phi _{\lambda }$ 's). Thus, every $\lambda$ must actually be the highest weight of a representation.

## Duality

The topic of recovering a compact group from its representation theory is the subject of the Tannaka–Krein duality, now often recast in terms of Tannakian category theory.

## From compact to non-compact groups

The influence of the compact group theory on non-compact groups was formulated by Weyl in his unitarian trick. Inside a general semisimple Lie group there is a maximal compact subgroup, and the representation theory of such groups, developed largely by Harish-Chandra, uses intensively the restriction of a representation to such a subgroup, and also the model of Weyl's character theory.
