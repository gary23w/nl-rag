---
title: "Profinite integer"
source: https://en.wikipedia.org/wiki/Profinite_integer
domain: p-adic-analysis
license: CC-BY-SA-4.0
tags: p-adic analysis, p-adic number, hensel's lemma, local field
fetched: 2026-07-02
---

# Profinite integer

In mathematics, a **profinite integer** is an element of the ring (sometimes pronounced as zee-hat or zed-hat)

${\widehat {\mathbb {Z} }}=\varprojlim \mathbb {Z} /n\mathbb {Z} ,$

where the inverse limit of the quotient rings $\mathbb {Z} /n\mathbb {Z}$ runs through all natural numbers n , partially ordered by divisibility. By definition, this ring is the profinite completion of the integers $\mathbb {Z}$ . By the Chinese remainder theorem, ${\widehat {\mathbb {Z} }}$ can also be understood as the direct product of rings

${\widehat {\mathbb {Z} }}=\prod _{p}\mathbb {Z} _{p},$

where the index p runs over all prime numbers, and $\mathbb {Z} _{p}$ is the ring of *p*-adic integers. This group is important because of its relation to Galois theory, étale homotopy theory, and the ring of adeles. In addition, it provides a basic tractable example of a profinite group.

## Construction

The profinite integers ${\widehat {\mathbb {Z} }}$ can be constructed as the set of sequences $\upsilon$ of residues represented as $\upsilon =(\upsilon _{1}{\bmod {1}},~\upsilon _{2}{\bmod {2}},~\upsilon _{3}{\bmod {3}},~\ldots )$ such that $m\ |\ n\implies \upsilon _{m}\equiv \upsilon _{n}\!\!\!\!\!{\pmod {m}}$ . Pointwise addition and multiplication make it a commutative ring.

The ring of integers embeds into the ring of profinite integers by the canonical injection $\eta :\mathbb {Z} \hookrightarrow {\widehat {\mathbb {Z} }},$ where $n\mapsto (n{\bmod {1}},n{\bmod {2}},\dots ).$ It is canonical since it satisfies the universal property of profinite groups that, given any profinite group H and any group homomorphism $f:\mathbb {Z} \rightarrow H$ , there exists a unique continuous group homomorphism $g:{\widehat {\mathbb {Z} }}\rightarrow H$ with $f=g\eta$ .

### Using the factorial number system

Every integer $n\geq 0$ has a unique representation in the factorial number system as $n=\sum _{i=1}^{\infty }c_{i}i!\quad {\text{with }}c_{i}\in \mathbb {Z} ,$ where $0\leq c_{i}\leq i$ for every i , and only finitely many of $c_{1},c_{2},c_{3},\ldots$ are nonzero. This can be written as $(\cdots c_{3}c_{2}c_{1})_{!}$ .

In the same way, a profinite integer can be uniquely represented in the factorial number system as an infinite string $(\cdots c_{3}c_{2}c_{1})_{!}$ , where each $c_{i}$ is an integer satisfying $0\leq c_{i}\leq i$ . The digits $c_{1},c_{2},c_{3},\ldots ,c_{k-1}$ determine the value of the profinite integer modulo $k!$ . More specifically, there is a ring homomorphism ${\widehat {\mathbb {Z} }}\to \mathbb {Z} /k!\,\mathbb {Z}$ sending $(\cdots c_{3}c_{2}c_{1})_{!}\mapsto \sum _{i=1}^{k-1}c_{i}i!{\bmod {k}}!$ The difference of a profinite integer from an integer is that the "finitely many nonzero digits" condition is dropped, allowing for its factorial number representation to have infinitely many nonzero digits.

### Using the Chinese remainder theorem

Another way to understand the construction of the profinite integers is by using the Chinese remainder theorem. Recall that for an integer n with prime factorization $n=p_{1}^{a_{1}}\cdots p_{k}^{a_{k}}$ of non-repeating primes, there is a ring isomorphism $\mathbb {Z} /n\cong \mathbb {Z} /p_{1}^{a_{1}}\times \cdots \times \mathbb {Z} /p_{k}^{a_{k}}$ from the theorem. Moreover, any surjection $\mathbb {Z} /n\to \mathbb {Z} /m$ will just be a map on the underlying decompositions where there are induced surjections $\mathbb {Z} /p_{i}^{a_{i}}\to \mathbb {Z} /p_{i}^{b_{i}}$ since we must have $a_{i}\geq b_{i}$ . Under the inverse limit definition of the profinite integers, we have the isomorphism ${\widehat {\mathbb {Z} }}\cong \prod _{p}\mathbb {Z} _{p}$ with the direct product of *p*-adic integers. Explicitly, the isomorphism is $\phi :\prod _{p}\mathbb {Z} _{p}\to {\widehat {\mathbb {Z} }}$ by $\phi ((n_{2},n_{3},n_{5},\cdots ))(k)=\prod _{q}n_{q}{\bmod {k}},$ where q ranges over all prime-power factors $p_{i}^{d_{i}}$ of k ; that is, $k=\prod _{i=1}^{l}p_{i}^{d_{i}}$ for some different prime numbers $p_{1},...,p_{l}$ .

## Relations

### Topological properties

The set of profinite integers has an induced topology in which it is a compact Hausdorff space (in fact, a Stone space) arising from the fact that it can be seen as a closed subset of the infinite direct product ${\widehat {\mathbb {Z} }}\subset \prod _{n=1}^{\infty }\mathbb {Z} /n\mathbb {Z} ,$ which is compact with its product topology by Tychonoff's theorem. The topology on each finite group $\mathbb {Z} /n\mathbb {Z}$ is given as the discrete topology.

The topology on ${\widehat {\mathbb {Z} }}$ can be defined by the metric $d(x,y)={\frac {1}{\min\{k\in \mathbb {Z} _{>0}:x\not \equiv y{\bmod {(k+1)!}}\}}}.$ Since addition of profinite integers is continuous, ${\widehat {\mathbb {Z} }}$ is a compact Hausdorff abelian group, and thus its Pontryagin dual must be a discrete abelian group. In fact, the Pontryagin dual of ${\widehat {\mathbb {Z} }}$ is the abelian group $\mathbb {Q} /\mathbb {Z}$ equipped with the discrete topology (note that it is not the subset topology inherited from $\mathbb {R} /\mathbb {Z}$ , which is not discrete). The Pontryagin dual is explicitly constructed by the function $\mathbb {Q} /\mathbb {Z} \times {\widehat {\mathbb {Z} }}\to U(1),\,(q,a)\mapsto \chi (qa),$ where $\chi$ is the character of the adele (introduced below) $\mathbf {A} _{\mathbb {Q} ,f}$ induced by $\mathbb {Q} /\mathbb {Z} \to U(1),\,\alpha \mapsto e^{2\pi i\alpha }$ .

### Relation with adeles

The tensor product ${\widehat {\mathbb {Z} }}\otimes _{\mathbb {Z} }\mathbb {Q}$ is the ring of finite adeles $\mathbf {A} _{\mathbb {Q} ,f}={\prod _{p}}'\mathbb {Q} _{p}$ of $\mathbb {Q}$ , where the symbol ' indicates a restricted product. That is, an element is a sequence that is integral except at a finite number of places. There is an isomorphism $\mathbf {A} _{\mathbb {Q} }\cong \mathbb {R} \times ({\widehat {\mathbb {Z} }}\otimes _{\mathbb {Z} }\mathbb {Q} ).$

### Applications in Galois theory and étale homotopy theory

For the algebraic closure ${\overline {\mathbf {F} }}_{q}$ of a finite field $\mathbf {F} _{q}$ of order *q,* the Galois group can be computed explicitly. From the fact ${\text{Gal}}(\mathbf {F} _{q^{n}}/\mathbf {F} _{q})\cong \mathbb {Z} /n\mathbb {Z}$ where the automorphisms are given by the Frobenius endomorphism, the Galois group of the algebraic closure of $\mathbf {F} _{q}$ is given by the inverse limit of the groups $\mathbb {Z} /n\mathbb {Z}$ , so its Galois group is isomorphic to the group of profinite integers $\operatorname {Gal} ({\overline {\mathbf {F} }}_{q}/\mathbf {F} _{q})\cong {\widehat {\mathbb {Z} }},$ which gives a computation of the absolute Galois group of a finite field.

#### Relation with étale fundamental groups of algebraic tori

This construction can be reinterpreted in many ways. One of them is from étale homotopy type, which defines the étale fundamental group $\pi _{1}^{et}(X)$ as the profinite completion of automorphisms $\pi _{1}^{et}(X)=\lim _{i\in I}{\text{Aut}}(X_{i}/X),$ where $X_{i}\to X$ is an étale cover. Then, the profinite integers are isomorphic to the group $\pi _{1}^{et}({\text{Spec}}(\mathbf {F} _{q}))\cong {\widehat {\mathbb {Z} }}$ from the earlier computation of the profinite Galois group. In addition, there is an embedding of the profinite integers inside the étale fundamental group of the algebraic torus ${\widehat {\mathbb {Z} }}\hookrightarrow \pi _{1}^{et}(\mathbb {G} _{m}),$ since the covering maps come from the polynomial maps $(\cdot )^{n}:\mathbb {G} _{m}\to \mathbb {G} _{m}$ from the map of commutative rings $f:\mathbb {Z} [x,x^{-1}]\to \mathbb {Z} [x,x^{-1}]$ sending $x\mapsto x^{n}$ since $\mathbb {G} _{m}={\text{Spec}}(\mathbb {Z} [x,x^{-1}])$ . If the algebraic torus is considered over a field k , then the étale fundamental group $\pi _{1}^{et}(\mathbb {G} _{m}/{\text{Spec(k)}})$ contains an action of ${\text{Gal}}({\overline {k}}/k)$ as well from the fundamental exact sequence in étale homotopy theory.

### Class field theory and the profinite integers

Class field theory is a branch of algebraic number theory studying the abelian field extensions of a field. Given the global field $\mathbb {Q}$ , the abelianization of its absolute Galois group ${\text{Gal}}({\overline {\mathbb {Q} }}/\mathbb {Q} )^{ab}$ is intimately related to the associated ring of adeles $\mathbb {A} _{\mathbb {Q} }$ and the group of profinite integers. In particular, there is a map, called the Artin map $\Psi _{\mathbb {Q} }:\mathbb {A} _{\mathbb {Q} }^{\times }/\mathbb {Q} ^{\times }\to {\text{Gal}}({\overline {\mathbb {Q} }}/\mathbb {Q} )^{ab},$ which is an isomorphism. This quotient can be determined explicitly as ${\begin{aligned}\mathbb {A} _{\mathbb {Q} }^{\times }/\mathbb {Q} ^{\times }&\cong (\mathbb {R} \times {\widehat {\mathbb {Z} }})/\mathbb {Z} \\&={\underset {\leftarrow }{\lim }}\mathbb {(} {\mathbb {R} }/m\mathbb {Z} )\\&={\underset {x\mapsto x^{m}}{\lim }}S^{1}\\&={\widehat {\mathbb {Z} }},\end{aligned}}$ giving the desired relation. There is an analogous statement for local class field theory since every finite abelian extension of $K/\mathbb {Q} _{p}$ is induced from a finite field extension $\mathbb {F} _{p^{n}}/\mathbb {F} _{p}$ .
