---
title: "Maschke's theorem"
source: https://en.wikipedia.org/wiki/Maschke's_theorem
domain: representation-theory
license: CC-BY-SA-4.0
tags: representation theory, group representation, character theory, irreducible representation
fetched: 2026-07-02
---

# Maschke's theorem

In mathematics, **Maschke's theorem**, named after Heinrich Maschke, is a theorem in group representation theory that concerns the decomposition of representations of a finite group into irreducible pieces. Maschke's theorem allows one to make general conclusions about representations of a finite group *G* without actually computing them. It reduces the task of classifying all representations to a more manageable task of classifying irreducible representations, since when the theorem applies, any representation is a direct sum of irreducible pieces (constituents). Moreover, it follows from the Jordan–Hölder theorem that, while the decomposition into a direct sum of irreducible subrepresentations may not be unique, the irreducible pieces have well-defined multiplicities. In particular, a representation of a finite group over a field of characteristic zero is determined up to isomorphism by its character.

## Formulations

Maschke's theorem addresses the question: when is a general (finite-dimensional) representation built from irreducible subrepresentations using the direct sum operation? This question (and its answer) are formulated differently for different perspectives on group representation theory.

### Group-theoretic

Maschke's theorem is commonly formulated as a corollary to the following result:

**Theorem**—Let V be a representation of a finite group G over a field $\mathbb {F}$ with characteristic not dividing the order of G . If V has a subrepresentation W , then it has another subrepresentation U such that $V=W\oplus U$ .

Then the corollary is

**Corollary (Maschke's theorem)**—Every representation of a finite group G over a field $\mathbb {F}$ with characteristic not dividing the order of G is a direct sum of irreducible representations.

The vector space of complex-valued class functions of a group G has a natural G -invariant inner product structure, described in the article Schur orthogonality relations. Maschke's theorem was originally proved for the case of representations over $\mathbb {C}$ by constructing U as the orthogonal complement of W under this inner product.

### Module-theoretic

One of the approaches to representations of finite groups is through module theory. *Representations* of a group G are replaced by *modules* over its group algebra  $K[G]$ (to be precise, there is an isomorphism of categories between $K[G]{\text{-Mod}}$ and $\operatorname {Rep} _{G}$ , the category of representations of G ). Irreducible representations correspond to simple modules. In the module-theoretic language, Maschke's theorem asks: is an arbitrary module semisimple? In this context, the theorem can be reformulated as follows:

**Maschke's Theorem**—Let G be a finite group and K a field whose characteristic does not divide the order of G . Then $K[G]$ , the group algebra of G , is semisimple.

The importance of this result stems from the well developed theory of semisimple rings, in particular, their classification as given by the Wedderburn–Artin theorem. When K is the field of complex numbers, this shows that the algebra $K[G]$ is a product of several copies of complex matrix algebras, one for each irreducible representation. If the field K has characteristic zero, but is not algebraically closed, for example if K is the field of real or rational numbers, then a somewhat more complicated statement holds: the group algebra $K[G]$ is a product of matrix algebras over division rings over K . The summands correspond to irreducible representations of G over K .

### Category-theoretic

Reformulated in the language of semi-simple categories, Maschke's theorem states

**Maschke's theorem**—If *G* is a group and *F* is a field with characteristic not dividing the order of *G*, then the category of representations of *G* over *F* is semi-simple.

## Proofs

### Group-theoretic

Let *U* be a subspace of *V* complement of *W*. Let $p_{0}:V\to W$ be the projection function, i.e., $p_{0}(w+u)=w$ for any $u\in U,w\in W$ .

Define ${\textstyle p(x)={\frac {1}{\#G}}\sum _{g\in G}g\cdot p_{0}\cdot g^{-1}(x)}$ , where $g\cdot p_{0}\cdot g^{-1}$ is an abbreviation of $\rho _{W}{g}\cdot p_{0}\cdot \rho _{V}{g^{-1}}$ , with $\rho _{W}{g},\rho _{V}{g^{-1}}$ being the representation of *G* on *W and* *V*. Then, $\ker p$ is preserved by *G* under representation $\rho _{V}$ : for any $w'\in \ker p,h\in G$ , ${\begin{aligned}p(hw')&=h\cdot h^{-1}{\frac {1}{\#G}}\sum _{g\in G}g\cdot p_{0}\cdot g^{-1}(hw')\\&=h\cdot {\frac {1}{\#G}}\sum _{g\in G}(h^{-1}\cdot g)\cdot p_{0}\cdot (g^{-1}h)w'\\&=h\cdot {\frac {1}{\#G}}\sum _{g\in G}g\cdot p_{0}\cdot g^{-1}w'\\&=h\cdot p(w')\\&=0\end{aligned}}$

so $w'\in \ker p$ implies that $hw'\in \ker p$ . So the restriction of $\rho _{V}$ on $\ker p$ is also a representation.

By the definition of p , for any $w\in W$ , $p(w)=w$ , so $W\cap \ker \ p=\{0\}$ , and for any $v\in V$ , $p(p(v))=p(v)$ . Thus, $p(v-p(v))=0$ , and $v-p(v)\in \ker p$ . Therefore, $V=W\oplus \ker p$ .

### Module-theoretic

Let *V* be a *K*[*G*]-submodule. We will prove that *V* is a direct summand. Let *π* be any *K*-linear projection of *K*[*G*] onto *V*. Consider the map ${\begin{cases}\varphi :K[G]\to V\\\varphi :x\mapsto {\frac {1}{\#G}}\sum _{s\in G}s\cdot \pi (s^{-1}\cdot x)\end{cases}}$

Then *φ* is again a projection: it is clearly *K*-linear, maps *K*[*G*] to *V*, and induces the identity on *V* (therefore, maps *K*[*G*] onto *V*). Moreover we have

${\begin{aligned}\varphi (t\cdot x)&={\frac {1}{\#G}}\sum _{s\in G}s\cdot \pi (s^{-1}\cdot t\cdot x)\\&={\frac {1}{\#G}}\sum _{u\in G}t\cdot u\cdot \pi (u^{-1}\cdot x)\\&=t\cdot \varphi (x),\end{aligned}}$

so *φ* is in fact *K*[*G*]-linear. By the splitting lemma, $K[G]=V\oplus \ker \varphi$ . This proves that every submodule is a direct summand, that is, *K*[*G*] is semisimple.

## Converse statement

The above proof depends on the fact that #*G* is invertible in *K*. This might lead one to ask if the converse of Maschke's theorem also holds: if the characteristic of *K* divides the order of *G*, does it follow that *K*[*G*] is not semisimple? The answer is *yes*.

**Proof.** For ${\textstyle x=\sum \lambda _{g}g\in K[G]}$ define ${\textstyle \epsilon (x)=\sum \lambda _{g}}$ . Let $I=\ker \epsilon$ . Then *I* is a *K*[*G*]-submodule. We will prove that for every nontrivial submodule *V* of *K*[*G*], $I\cap V\neq 0$ . Let *V* be given, and let ${\textstyle v=\sum \mu _{g}g}$ be any nonzero element of *V*. If $\epsilon (v)=0$ , the claim is immediate. Otherwise, let ${\textstyle s=\sum 1g}$ . Then $\epsilon (s)=\#G\cdot 1=0$ so $s\in I$ and $sv=\left(\sum 1g\right)\!\left(\sum \mu _{g}g\right)=\sum \epsilon (v)g=\epsilon (v)s$

so that $sv$ is a nonzero element of both *I* and *V*. This proves *V* is not a direct complement of *I* for all *V*, so *K*[*G*] is not semisimple.

## Non-examples

The theorem can not apply to the case where *G* is infinite, or when the field *K* has characteristics dividing #*G*. For example,

- Consider the infinite group $\mathbb {Z}$ and the representation $\rho :\mathbb {Z} \to \mathrm {GL} _{2}(\mathbb {C} )$ defined by $\rho (n)={\begin{bmatrix}1&1\\0&1\end{bmatrix}}^{n}={\begin{bmatrix}1&n\\0&1\end{bmatrix}}$ . Let $W=\mathbb {C} \cdot {\begin{bmatrix}1\\0\end{bmatrix}}$ , a 1-dimensional subspace of $\mathbb {C} ^{2}$ spanned by ${\begin{bmatrix}1\\0\end{bmatrix}}$ . Then the restriction of $\rho$ on *W* is a trivial subrepresentation of $\mathbb {Z}$ . However, there's no *U* such that both *W, U* are subrepresentations of $\mathbb {Z}$ and $\mathbb {C} ^{2}=W\oplus U$ : any such *U* needs to be 1-dimensional, but any 1-dimensional subspace preserved by $\rho$ has to be spanned by an eigenvector for ${\begin{bmatrix}1&1\\0&1\end{bmatrix}}$ , and the only eigenvector for that is ${\begin{bmatrix}1\\0\end{bmatrix}}$ .
- Consider a prime *p*, and the group $\mathbb {Z} /p\mathbb {Z}$ , field $K=\mathbb {F} _{p}$ , and the representation $\rho :\mathbb {Z} /p\mathbb {Z} \to \mathrm {GL} _{2}(\mathbb {F} _{p})$ defined by $\rho (n)={\begin{bmatrix}1&n\\0&1\end{bmatrix}}$ . Simple calculations show that there is only one eigenvector for ${\begin{bmatrix}1&1\\0&1\end{bmatrix}}$ here, so by the same argument, the 1-dimensional subrepresentation of $\mathbb {Z} /p\mathbb {Z}$ is unique, and $\mathbb {Z} /p\mathbb {Z}$ cannot be decomposed into the direct sum of two 1-dimensional subrepresentations.
