---
title: "Representation theory of finite groups (part 2/2)"
source: https://en.wikipedia.org/wiki/Representation_theory_of_finite_groups
domain: representation-theory
license: CC-BY-SA-4.0
tags: representation theory, group representation, character theory, irreducible representation
fetched: 2026-07-02
part: 2/2
---

## The induced representation

As was shown in the section on properties of linear representations, we can - by restriction - obtain a representation of a subgroup starting from a representation of a group. Naturally we are interested in the reverse process: Is it possible to obtain the representation of a group starting from a representation of a subgroup? We will see that the induced representation defined below provides us with the necessary concept. Admittedly, this construction is not inverse but rather adjoint to the restriction.

### Definitions

Let $\rho :G\to {\text{GL}}(V_{\rho })$ be a linear representation of $G.$ Let H be a subgroup and $\rho |_{H}$ the restriction. Let W be a subrepresentation of $\rho _{H}.$ We write $\theta :H\to {\text{GL}}(W)$ to denote this representation. Let $s\in G.$ The vector space $\rho (s)(W)$ depends only on the left coset $sH$ of $s.$ Let R be a representative system of $G/H,$ then

$\sum _{r\in R}\rho (r)(W)$

is a subrepresentation of $V_{\rho }.$

A representation $\rho$ of G in $V_{\rho }$ is called **induced** by the representation $\theta$ of H in $W,$ if

$V_{\rho }=\bigoplus _{r\in R}W_{r}.$

Here $W_{r}=\rho (s)(W)$ for all $s\in rH$ and for all $r\in R.$ In other words: the representation $(\rho ,V_{\rho })$ is induced by $(\theta ,W),$ if every $v\in V_{\rho }$ can be written uniquely as

$\sum _{r\in R}w_{r},$

where $w_{r}\in W_{r}$ for every $r\in R.$

We denote the representation $\rho$ of G which is induced by the representation $\theta$ of H as $\rho ={\text{Ind}}_{H}^{G}(\theta ),$ or in short $\rho ={\text{Ind}}(\theta ),$ if there is no danger of confusion. The representation space itself is frequently used instead of the representation map, i.e. $V={\text{Ind}}_{H}^{G}(W),$ or $V={\text{Ind}}(W),$ if the representation V is induced by $W.$

#### Alternative description of the induced representation

By using the group algebra we obtain an alternative description of the induced representation:

Let G be a group, V a $\mathbb {C} [G]$ –module and W a $\mathbb {C} [H]$ –submodule of V corresponding to the subgroup H of $G.$ We say that V is induced by W if $V=\mathbb {C} [G]\otimes _{\mathbb {C} [H]}W,$ in which G acts on the first factor: $s\cdot (e_{t}\otimes w)=e_{st}\otimes w$ for all $s,t\in G,w\in W.$

### Properties

The results introduced in this section will be presented without proof. These may be found in and .

Uniqueness and existence of the induced representation.

Let

$(\theta ,W_{\theta })$

be a linear representation of a subgroup

H

of

$G.$

Then there exists a linear representation

$(\rho ,V_{\rho })$

of

$G,$

which is induced by

$(\theta ,W_{\theta }).$

Note that this representation is unique up to isomorphism.

Transitivity of induction.

Let

W

be a representation of

H

and let

$H\leq G\leq K$

be an ascending series of groups. Then we have

${\text{Ind}}_{G}^{K}({\text{Ind}}_{H}^{G}(W))\cong {\text{Ind}}_{H}^{K}(W).$

Lemma.

Let

$(\rho ,V_{\rho })$

be induced by

$(\theta ,W_{\theta })$

and let

$\rho ':G\to {\text{GL}}(V')$

be a linear representation of

$G.$

Now let

$F:W_{\theta }\to V'$

be a linear map satisfying the property that

$F\circ \theta (t)=\rho '(t)\circ F$

for all

$t\in G.$

Then there exists a uniquely determined linear map

$F':V_{\rho }\to V',$

which extends

F

and for which

$F'\circ \rho (s)=\rho '(s)\circ F'$

is valid for all

$s\in G.$

This means that if we interpret $V'$ as a $\mathbb {C} [G]$ –module, we have ${\text{Hom}}^{H}(W_{\theta },V')\cong {\text{Hom}}^{G}(V_{\rho },V'),$ where ${\text{Hom}}^{G}(V_{\rho },V')$ is the vector space of all $\mathbb {C} [G]$ –homomorphisms of $V_{\rho }$ to $V'.$ The same is valid for ${\text{Hom}}^{H}(W_{\theta },V').$

**Induction on class functions.** In the same way as it was done with representations, we can - by *induction* - obtain a class function on the group from a class function on a subgroup. Let $\varphi$ be a class function on $H.$ We define a function $\varphi '$ on G by

$\varphi '(s)={\frac {1}{|H|}}\sum _{t\in G \atop t^{-1}st\in H}^{}\varphi (t^{-1}st).$

We say $\varphi '$ is *induced* by $\varphi$ and write ${\text{Ind}}_{H}^{G}(\varphi )=\varphi '$ or ${\text{Ind}}(\varphi )=\varphi '.$

Proposition.

The function

${\text{Ind}}(\varphi )$

is a class function on

$G.$

If

$\varphi$

is the

character

of a representation

W

of

$H,$

then

${\text{Ind}}(\varphi )$

is the character of the induced representation

${\text{Ind}}(W)$

of

$G.$

Lemma.

If

$\psi$

is a class function on

H

and

$\varphi$

is a class function on

$G,$

then we have:

${\text{Ind}}(\psi \cdot {\text{Res}}\varphi )=({\text{Ind}}\psi )\cdot \varphi .$

Theorem.

Let

$(\rho ,V_{\rho })$

be the representation of

G

induced by the representation

$(\theta ,W_{\theta })$

of the subgroup

$H.$

Let

$\chi _{\rho }$

and

$\chi _{\theta }$

be the corresponding characters. Let

R

be a representative system of

$G/H.$

The induced character is given by

$\forall t\in G:\qquad \chi _{\rho }(t)=\sum _{r\in R, \atop r^{-1}tr\in H}^{}\chi _{\theta }(r^{-1}tr)={\frac {1}{|H|}}\sum _{s\in G, \atop s^{-1}ts\in H}^{}\chi _{\theta }(s^{-1}ts).$

### Frobenius reciprocity

As a preemptive summary, the lesson to take from Frobenius reciprocity is that the maps ${\text{Res}}$ and ${\text{Ind}}$ are adjoint to each other.

Let W be an irreducible representation of H and let V be an irreducible representation of $G,$ then the Frobenius reciprocity tells us that W is contained in ${\text{Res}}(V)$ as often as ${\text{Ind}}(W)$ is contained in $V.$

Frobenius reciprocity.

If

$\psi \in \mathbb {C} _{\text{class}}(H)$

and

$\varphi \in \mathbb {C} _{\text{class}}(G)$

we have

$\langle \psi ,{\text{Res}}(\varphi )\rangle _{H}=\langle {\text{Ind}}(\psi ),\varphi \rangle _{G}.$

This statement is also valid for the inner product.

### Mackey's irreducibility criterion

George Mackey established a criterion to verify the irreducibility of induced representations. For this we will first need some definitions and some specifications with respect to the notation.

Two representations $V_{1}$ and $V_{2}$ of a group G are called **disjoint**, if they have no irreducible component in common, i.e. if $\langle V_{1},V_{2}\rangle _{G}=0.$

Let G be a group and let H be a subgroup. We define $H_{s}=sHs^{-1}\cap H$ for $s\in G.$ Let $(\rho ,W)$ be a representation of the subgroup $H.$ This defines by restriction a representation ${\text{Res}}_{H_{s}}(\rho )$ of $H_{s}.$ We write ${\text{Res}}_{s}(\rho )$ for ${\text{Res}}_{H_{s}}(\rho ).$ We also define another representation $\rho ^{s}$ of $H_{s}$ by $\rho ^{s}(t)=\rho (s^{-1}ts).$ These two representations are not to be confused.

Mackey's irreducibility criterion.

The induced representation

$V={\text{Ind}}_{H}^{G}(W)$

is irreducible if and only if the following conditions are satisfied:

- W is irreducible
- For each $s\in G\setminus H$ the two representations $\rho ^{s}$ and ${\text{Res}}_{s}(\rho )$ of $H_{s}$ are disjoint. A proof of this theorem may be found in .

For the case of H normal, we have $H_{s}=H$ and ${\text{Res}}_{s}(\rho )=\rho$ . Thus we obtain the following:

Corollary.

Let

H

be a normal subgroup of

$G.$

Then

${\text{Ind}}_{H}^{G}(\rho )$

is irreducible if and only if

$\rho$

is irreducible and not isomorphic to the conjugates

$\rho ^{s}$

for

$s\notin H.$

### Applications to special groups

In this section we present some applications of the so far presented theory to normal subgroups and to a special group, the semidirect product of a subgroup with an abelian normal subgroup.

Proposition.

Let

A

be a

normal subgroup

of the group

G

and let

$\rho :G\to {\text{GL}}(V)$

be an irreducible representation of

$G.$

Then one of the following statements has to be valid:

- either there exists a proper subgroup H of G containing A , and an irreducible representation $\eta$ of H which induces $\rho$ ,
- or V is an isotypic $\mathbb {C} A$ -module.

Proof.

Consider

V

as a

$\mathbb {C} A$

-module, and decompose it into isotypes as

$V=\bigoplus _{j}{V_{j}}$

. If this decomposition is trivial, we are in the second case. Otherwise, the larger

G

-action permutes these isotypic modules; because

V

is irreducible as a

$\mathbb {C} G$

-module, the permutation action is

transitive

(in fact

primitive

). Fix any

j

; the

stabilizer

in

G

of

$V_{j}$

is elementarily seen to exhibit the claimed properties.

$\Box$

Note that if A is abelian, then the isotypic modules of A are irreducible, of degree one, and all homotheties.

We obtain also the following

Corollary.

Let

A

be an abelian normal subgroup of

G

and let

$\tau$

be any irreducible representation of

$G.$

We denote with

$(G:A)$

the

index

of

A

in

$G.$

Then

$\deg(\tau )|(G:A).$

If A is an abelian subgroup of G (not necessarily normal), generally $\deg(\tau )|(G:A)$ is not satisfied, but nevertheless $\deg(\tau )\leq (G:A)$ is still valid.

#### Classification of representations of a semidirect product

In the following, let $G=A\rtimes H$ be a semidirect product such that the normal semidirect factor, A , is abelian. The irreducible representations of such a group $G,$ can be classified by showing that all irreducible representations of G can be constructed from certain subgroups of H . This is the so-called method of “little groups” of Wigner and Mackey.

Since A is abelian, the irreducible characters of A have degree one and form the group $\mathrm {X} ={\text{Hom}}(A,\mathbb {C} ^{\times }).$ The group G acts on $\mathrm {X}$ by $(s\chi )(a)=\chi (s^{-1}as)$ for $s\in G,\chi \in \mathrm {X} ,a\in A.$

Let $(\chi _{j})_{j\in \mathrm {X} /H}$ be a representative system of the orbit of H in $\mathrm {X} .$ For every $j\in \mathrm {X} /H$ let $H_{j}=\{t\in H:t\chi _{j}=\chi _{j}\}.$ This is a subgroup of $H.$ Let $G_{j}=A\cdot H_{j}$ be the corresponding subgroup of $G.$ We now extend the function $\chi _{j}$ onto $G_{j}$ by $\chi _{j}(at)=\chi _{j}(a)$ for $a\in A,t\in H_{j}.$ Thus, $\chi _{j}$ is a class function on $G_{j}.$ Moreover, since $t\chi _{j}=\chi _{j}$ for all $t\in H_{j},$ it can be shown that $\chi _{j}$ is a group homomorphism from $G_{j}$ to $\mathbb {C} ^{\times }.$ Therefore, we have a representation of $G_{j}$ of degree one which is equal to its own character.

Let now $\rho$ be an irreducible representation of $H_{j}.$ Then we obtain an irreducible representation ${\tilde {\rho }}$ of $G_{j},$ by combining $\rho$ with the canonical projection $G_{j}\to H_{j}.$ Finally, we construct the tensor product of $\chi _{j}$ and ${\tilde {\rho }}.$ Thus, we obtain an irreducible representation $\chi _{j}\otimes {\tilde {\rho }}$ of $G_{j}.$

To finally obtain the classification of the irreducible representations of G we use the representation $\theta _{j,\rho }$ of $G,$ which is induced by the tensor product $\chi _{j}\otimes {\tilde {\rho }}.$ Thus, we achieve the following result:

Proposition.

- $\theta _{j,\rho }$ is irreducible.
- If $\theta _{j,\rho }$ and $\theta _{j',\rho '}$ are isomorphic, then $j=j'$ and additionally $\rho$ is isomorphic to $\rho '.$
- Every irreducible representation of G is isomorphic to one of the $\theta _{j,\rho }.$

Amongst others, the criterion of Mackey and a conclusion based on the Frobenius reciprocity are needed for the proof of the proposition. Further details may be found in .

In other words, we classified all irreducible representations of $G=A\rtimes H.$


## Representation ring

The representation ring of G is defined as the abelian group

$R(G)=\left\{\left.\sum _{j=1}^{m}a_{j}\tau _{j}\right|\tau _{1},\ldots ,\tau _{m}{\text{ all irreducible representations of }}G{\text{ up to isomorphism}},a_{j}\in \mathbb {Z} \right\}.$

With the multiplication provided by the tensor product, $R(G)$ becomes a ring. The elements of $R(G)$ are called **virtual representations**.

The character defines a ring homomorphism in the set of all class functions on G with complex values

${\begin{cases}\chi :R(G)\to \mathbb {C} _{\text{class}}(G)\\\sum a_{j}\tau _{j}\mapsto \sum a_{j}\chi _{j}\end{cases}}$

in which the $\chi _{j}$ are the irreducible characters corresponding to the $\tau _{j}.$

Because a representation is determined by its character, $\chi$ is injective. The images of $\chi$ are called **virtual characters**.

As the irreducible characters form an orthonormal basis of $\mathbb {C} _{\text{class}},\chi$ induces an isomorphism

$\chi _{\mathbb {C} }:R(G)\otimes \mathbb {C} \to \mathbb {C} _{\text{class}}(G).$

This isomorphism is defined on a basis out of elementary tensors $(\tau _{j}\otimes 1)_{j=1,\ldots ,m}$ by $\chi _{\mathbb {C} }(\tau _{j}\otimes 1)=\chi _{j}$ respectively $\chi _{\mathbb {C} }(\tau _{j}\otimes z)=z\chi _{j},$ and extended bilinearly.

We write ${\mathcal {R}}^{+}(G)$ for the set of all characters of G and ${\mathcal {R}}(G)$ to denote the group generated by ${\mathcal {R}}^{+}(G),$ i.e. the set of all differences of two characters. It then holds that ${\mathcal {R}}(G)=\mathbb {Z} \chi _{1}\oplus \cdots \oplus \mathbb {Z} \chi _{m}$ and ${\mathcal {R}}(G)={\text{Im}}(\chi )=\chi (R(G)).$ Thus, we have $R(G)\cong {\mathcal {R}}(G)$ and the virtual characters correspond to the virtual representations in an optimal manner.

Since ${\mathcal {R}}(G)={\text{Im}}(\chi )$ holds, ${\mathcal {R}}(G)$ is the set of all virtual characters. As the product of two characters provides another character, ${\mathcal {R}}(G)$ is a subring of the ring $\mathbb {C} _{\text{class}}(G)$ of all class functions on $G.$ Because the $\chi _{i}$ form a basis of $\mathbb {C} _{\text{class}}(G)$ we obtain, just as in the case of $R(G),$ an isomorphism $\mathbb {C} \otimes {\mathcal {R}}(G)\cong \mathbb {C} _{\text{class}}(G).$

Let H be a subgroup of $G.$ The restriction thus defines a ring homomorphism ${\mathcal {R}}(G)\to {\mathcal {R}}(H),\phi \mapsto \phi |_{H},$ which will be denoted by ${\text{Res}}_{H}^{G}$ or ${\text{Res}}.$ Likewise, the induction on class functions defines a homomorphism of abelian groups ${\mathcal {R}}(H)\to {\mathcal {R}}(G),$ which will be written as ${\text{Ind}}_{H}^{G}$ or in short ${\text{Ind}}.$

According to the Frobenius reciprocity, these two homomorphisms are adjoint with respect to the bilinear forms $\langle \cdot ,\cdot \rangle _{H}$ and $\langle \cdot ,\cdot \rangle _{G}.$ Furthermore, the formula ${\text{Ind}}(\varphi \cdot {\text{Res}}(\psi ))={\text{Ind}}(\varphi )\cdot \psi$ shows that the image of ${\text{Ind}}:{\mathcal {R}}(H)\to {\mathcal {R}}(G)$ is an ideal of the ring ${\mathcal {R}}(G).$

By the restriction of representations, the map ${\text{Res}}$ can be defined analogously for $R(G),$ and by the induction we obtain the map ${\text{Ind}}$ for $R(G).$ Due to the Frobenius reciprocity, we get the result that these maps are adjoint to each other and that the image ${\text{Im}}({\text{Ind}})={\text{Ind}}(R(H))$ is an ideal of the ring $R(G).$

If A is a commutative ring, the homomorphisms ${\text{Res}}$ and ${\text{Ind}}$ may be extended to A –linear maps:

${\begin{cases}A\otimes {\text{Res}}:A\otimes R(G)\to A\otimes R(H)\\\left(a\otimes \sum a_{j}\tau _{j}\right)\mapsto \left(a\otimes \sum a_{j}{\text{Res}}(\tau _{j})\right)\end{cases}},\qquad {\begin{cases}A\otimes {\text{Ind}}:A\otimes R(H)\to A\otimes R(G)\\\left(a\otimes \sum a_{j}\eta _{j}\right)\mapsto \left(a\otimes \sum a_{j}{\text{Ind}}(\eta _{j})\right)\end{cases}}$

in which $\eta _{j}$ are all the irreducible representations of H up to isomorphism.

With $A=\mathbb {C}$ we obtain in particular that ${\text{Ind}}$ and ${\text{Res}}$ supply homomorphisms between $\mathbb {C} _{\text{class}}(G)$ and $\mathbb {C} _{\text{class}}(H).$

Let $G_{1}$ and $G_{2}$ be two groups with respective representations $(\rho _{1},V_{1})$ and $(\rho _{2},V_{2}).$ Then, $\rho _{1}\otimes \rho _{2}$ is the representation of the direct product $G_{1}\times G_{2}$ as was shown in a previous section. Another result of that section was that all irreducible representations of $G_{1}\times G_{2}$ are exactly the representations $\eta _{1}\otimes \eta _{2},$ where $\eta _{1}$ and $\eta _{2}$ are irreducible representations of $G_{1}$ and $G_{2},$ respectively. This passes over to the representation ring as the identity $R(G_{1}\times G_{2})=R(G_{1})\otimes _{\mathbb {Z} }R(G_{2}),$ in which $R(G_{1})\otimes _{\mathbb {Z} }R(G_{2})$ is the tensor product of the representation rings as $\mathbb {Z}$ –modules.


## Induction theorems

Induction theorems relate the representation ring of a given finite group *G* to representation rings of a family *X* consisting of some subsets *H* of *G*. More precisely, for such a collection of subgroups, the induction functor yields a map

$\varphi :{\text{Ind}}:\bigoplus _{H\in X}{\mathcal {R}}(H)\to {\mathcal {R}}(G)$

; induction theorems give criteria for the surjectivity of this map or closely related ones.

*Artin's induction theorem* is the most elementary theorem in this group of results. It asserts that the following are equivalent:

- The cokernel of $\varphi$ is finite.
- G is the union of the conjugates of the subgroups belonging to $X,$ i.e. $G=\bigcup _{H\in X \atop s\in G}sHs^{-1}.$

Since ${\mathcal {R}}(G)$ is finitely generated as a group, the first point can be rephrased as follows:

- For each character $\chi$ of $G,$ there exist virtual characters $\chi _{H}\in {\mathcal {R}}(H),\,H\in X$ and an integer $d\geq 1,$ such that $d\cdot \chi =\sum _{H\in X}{\text{Ind}}_{H}^{G}(\chi _{H}).$

Serre (1977) gives two proofs of this theorem. For example, since *G* is the union of its cyclic subgroups, every character of G is a linear combination with rational coefficients of characters induced by characters of cyclic subgroups of $G.$ Since the representations of cyclic groups are well-understood, in particular the irreducible representations are one-dimensional, this gives a certain control over representations of *G*.

Under the above circumstances, it is not in general true that $\varphi$ is surjective. *Brauer's induction theorem* asserts that $\varphi$ is surjective, provided that *X* is the family of all *elementary subgroups*. Here a group *H* is elementary if there is some prime *p* such that *H* is the direct product of a cyclic group of order prime to p and a p –group. In other words, every character of G is a linear combination with integer coefficients of characters induced by characters of elementary subgroups. The elementary subgroups *H* arising in Brauer's theorem have a richer representation theory than cyclic groups, they at least have the property that any irreducible representation for such *H* is induced by a one-dimensional representation of a (necessarily also elementary) subgroup $K\subset H$ . (This latter property can be shown to hold for any supersolvable group, which includes nilpotent groups and, in particular, elementary groups.) This ability to induce representations from degree 1 representations has some further consequences in the representation theory of finite groups.


## Real representations

For proofs and more information about representations over general subfields of $\mathbb {C}$ please refer to .

If a group G acts on a real vector space $V_{0},$ the corresponding representation on the complex vector space $V=V_{0}\otimes _{\mathbb {R} }\mathbb {C}$ is called **real** ( V is called the complexification of $V_{0}$ ). The corresponding representation mentioned above is given by $s\cdot (v_{0}\otimes z)=(s\cdot v_{0})\otimes z$ for all $s\in G,v_{0}\in V_{0},z\in \mathbb {C} .$

Let $\rho$ be a real representation. The linear map $\rho (s)$ is $\mathbb {R}$ -valued for all $s\in G.$ Thus, we can conclude that the character of a real representation is always real-valued. But not every representation with a real-valued character is real. To make this clear, let G be a finite, non-abelian subgroup of the group

${\text{SU}}(2)=\left\{{\begin{pmatrix}a&b\\-{\overline {b}}&{\overline {a}}\end{pmatrix}}\ :\ |a|^{2}+|b|^{2}=1\right\}.$

Then $G\subset {\text{SU}}(2)$ acts on $V=\mathbb {C} ^{2}.$ Since the trace of any matrix in ${\text{SU}}(2)$ is real, the character of the representation is real-valued. Suppose $\rho$ is a real representation, then $\rho (G)$ would consist only of real-valued matrices. Thus, $G\subset {\text{SU}}(2)\cap {\text{GL}}_{2}(\mathbb {R} )={\text{SO}}(2)=S^{1}.$ However the circle group is abelian but G was chosen to be a non-abelian group. Now we only need to prove the existence of a non-abelian, finite subgroup of ${\text{SU}}(2).$ To find such a group, observe that ${\text{SU}}(2)$ can be identified with the units of the quaternions. Now let $G=\{\pm 1,\pm i,\pm j,\pm ij\}.$ The following two-dimensional representation of G is not real-valued, but has a real-valued character:

${\begin{cases}\rho :G\to {\text{GL}}_{2}(\mathbb {C} )\\[4pt]\rho (\pm 1)={\begin{pmatrix}\pm 1&0\\0&\pm 1\end{pmatrix}},\quad \rho (\pm i)={\begin{pmatrix}\pm i&0\\0&\mp i\end{pmatrix}},\quad \rho (\pm j)={\begin{pmatrix}0&\pm i\\\pm i&0\end{pmatrix}}\end{cases}}$

Then the image of $\rho$ is not real-valued, but nevertheless it is a subset of ${\text{SU}}(2).$ Thus, the character of the representation is real.

Lemma.

An irreducible representation

V

of

G

is real if and only if there exists a

nondegenerate

symmetric bilinear form

B

on

V

preserved by

$G.$

An irreducible representation of G on a real vector space can become reducible when extending the field to $\mathbb {C} .$ For example, the following real representation of the cyclic group is reducible when considered over $\mathbb {C}$

${\begin{cases}\rho :\mathbb {Z} /m\mathbb {Z} \to {\text{GL}}_{2}(\mathbb {R} )\\[4pt]\rho (k)={\begin{pmatrix}\cos \left({\frac {2\pi ik}{m}}\right)&\sin \left({\frac {2\pi ik}{m}}\right)\\-\sin \left({\frac {2\pi ik}{m}}\right)&\cos \left({\frac {2\pi ik}{m}}\right)\end{pmatrix}}\end{cases}}$

Therefore, by classifying all the irreducible representations that are real over $\mathbb {C} ,$ we still haven't classified all the irreducible real representations. But we achieve the following:

Let $V_{0}$ be a real vector space. Let G act irreducibly on $V_{0}$ and let $V=V_{0}\otimes \mathbb {C} .$ If V is not irreducible, there are exactly two irreducible factors which are complex conjugate representations of $G.$

**Definition.** A **quaternionic** representation is a (complex) representation $V,$ which possesses a G –invariant anti-linear homomorphism $J:V\to V$ satisfying $J^{2}=-{\text{Id}}.$ Thus, a skew-symmetric, nondegenerate G –invariant bilinear form defines a quaternionic structure on $V.$

Theorem.

An irreducible representation

V

is one and only one of the following:

(i) complex:

$\chi _{V}$

is not real-valued and there exists no

G

–invariant

nondegenerate

bilinear form on

$V.$

(ii) real:

$V=V_{0}\otimes \mathbb {C} ,$

a real representation;

V

has a

G

–invariant nondegenerate

symmetric bilinear form

.

(iii) quaternionic:

$\chi _{V}$

is real, but

V

is not real;

V

has a

G

–invariant skew-symmetric nondegenerate bilinear form.


## Representations of particular groups

### Symmetric groups

Representation of the symmetric groups $S_{n}$ have been intensely studied. Conjugacy classes in $S_{n}$ (and therefore, by the above, irreducible representations) correspond to partitions of *n*. For example, $S_{3}$ has three irreducible representations, corresponding to the partitions

3; 2+1; 1+1+1

of 3. For such a partition, a Young tableau is a graphical device depicting a partition. The irreducible representation corresponding to such a partition (or Young tableau) is called a Specht module.

Representations of different symmetric groups are related: any representation of $S_{n}\times S_{m}$ yields a representation of $S_{n+m}$ by induction, and vice versa by restriction. The direct sum of all these representation rings

$\bigoplus _{n\geq 0}R(S_{n})$

inherits from these constructions the structure of a Hopf algebra which, it turns out, is closely related to symmetric functions.

### Finite groups of Lie type

To a certain extent, the representations of the $GL_{n}(\mathbf {F} _{q})$ , as *n* varies, have a similar flavor as for the $S_{n}$ ; the above-mentioned induction process gets replaced by so-called parabolic induction. However, unlike for $S_{n}$ , where all representations can be obtained by induction of trivial representations, this is not true for $GL_{n}(\mathbf {F} _{q})$ . Instead, new building blocks, known as cuspidal representations, are needed.

Representations of $GL_{n}(\mathbf {F} _{q})$ and more generally, representations of finite groups of Lie type have been thoroughly studied. Bonnafé (2010) describes the representations of $SL_{2}(\mathbf {F} _{q})$ . A geometric description of irreducible representations of such groups, including the above-mentioned cuspidal representations, is obtained by Deligne-Lusztig theory, which constructs such representation in the l-adic cohomology of Deligne-Lusztig varieties.

The similarity of the representation theory of $S_{n}$ and $GL_{n}(\mathbf {F} _{q})$ goes beyond finite groups. The philosophy of cusp forms highlights the kinship of representation theoretic aspects of these types of groups with general linear groups of local fields such as **Q***p* and of the ring of adeles, see Bump (2004).


## Outlook—Representations of compact groups

The theory of representations of compact groups may be, to some degree, extended to locally compact groups. The representation theory unfolds in this context great importance for harmonic analysis and the study of automorphic forms. For proofs, further information and for a more detailed insight which is beyond the scope of this chapter please consult and .

### Definition and properties

A **topological group** is a group together with a topology with respect to which the group composition and the inversion are continuous. Such a group is called **compact**, if any cover of $G,$ which is open in the topology, has a finite subcover. Closed subgroups of a compact group are compact again.

Let G be a compact group and let V be a finite-dimensional $\mathbb {C}$ –vector space. A linear representation of G to V is a **continuous group homomorphism** $\rho :G\to {\text{GL}}(V),$ i.e. $\rho (s)v$ is a continuous function in the two variables $s\in G$ and $v\in V.$

A linear representation of G into a Banach space V is defined to be a continuous group homomorphism of G into the set of all bijective bounded linear operators on V with a continuous inverse. Since $\pi (g)^{-1}=\pi (g^{-1}),$ we can do without the last requirement. In the following, we will consider in particular representations of compact groups in Hilbert spaces.

Just as with finite groups, we can define the group algebra and the convolution algebra. However, the group algebra provides no helpful information in the case of infinite groups, because the continuity condition gets lost during the construction. Instead the convolution algebra $L^{1}(G)$ takes its place.

Most properties of representations of finite groups can be transferred with appropriate changes to compact groups. For this we need a counterpart to the summation over a finite group:

### Existence and uniqueness of the Haar measure

On a compact group G there exists exactly one measure $dt,$ such that:

- It is a left-translation-invariant measure

$\forall s\in G:\quad \int _{G}f(t)dt=\int _{G}f(st)dt.$

- The whole group has unit measure:

$\int _{G}dt=1,$

Such a left-translation-invariant, normed measure is called **Haar measure** of the group $G.$

Since G is compact, it is possible to show that this measure is also right-translation-invariant, i.e. it also applies

$\forall s\in G:\quad \int _{G}f(t)dt=\int _{G}f(ts)dt.$

By the scaling above the Haar measure on a finite group is given by $dt(s)={\tfrac {1}{|G|}}$ for all $s\in G.$

All the definitions to representations of finite groups that are mentioned in the section ”Properties”, also apply to representations of compact groups. But there are some modifications needed:

To define a subrepresentation we now need a closed subspace. This was not necessary for finite-dimensional representation spaces, because in this case every subspace is already closed. Furthermore, two representations $\rho ,\pi$ of a compact group G are called equivalent, if there exists a bijective, continuous, linear operator T between the representation spaces whose inverse is also continuous and which satisfies $T\circ \rho (s)=\pi (s)\circ T$ for all $s\in G.$

If T is unitary, the two representations are called **unitary equivalent**.

To obtain a G –invariant inner product from a not G –invariant, we now have to use the integral over G instead of the sum. If $(\cdot |\cdot )$ is an inner product on a Hilbert space $V,$ which is not invariant with respect to the representation $\rho$ of $G,$ then

$(v|u)_{\rho }=\int _{G}(\rho (t)v|\rho (t)u)dt$

is a G –invariant inner product on V due to the properties of the Haar measure $dt.$ Thus, we can assume every representation on a Hilbert space to be unitary.

Let G be a compact group and let $s\in G.$ Let $L^{2}(G)$ be the Hilbert space of the square integrable functions on $G.$ We define the operator $L_{s}$ on this space by $L_{s}\Phi (t)=\Phi (s^{-1}t),$ where $\Phi \in L^{2}(G),t\in G.$

The map $s\mapsto L_{s}$ is a unitary representation of $G.$ It is called **left-regular representation**. The **right-regular representation** is defined similarly. As the Haar measure of G is also right-translation-invariant, the operator $R_{s}$ on $L^{2}(G)$ is given by $R_{s}\Phi (t)=\Phi (ts).$ The right-regular representation is then the unitary representation given by $s\mapsto R_{s}.$ The two representations $s\mapsto L_{s}$ and $s\mapsto R_{s}$ are dual to each other.

If G is infinite, these representations have no finite degree. The left- and right-regular representation as defined at the beginning are isomorphic to the left- and right-regular representation as defined above, if the group G is finite. This is due to the fact that in this case $L^{2}(G)\cong L^{1}(G)\cong \mathbb {C} [G].$

### Constructions and decompositions

The different ways of constructing new representations from given ones can be used for compact groups as well, except for the dual representation with which we will deal later. The direct sum and the tensor product with a finite number of summands/factors are defined in exactly the same way as for finite groups. This is also the case for the symmetric and alternating square. However, we need a Haar measure on the direct product of compact groups in order to extend the theorem saying that the irreducible representations of the product of two groups are (up to isomorphism) exactly the tensor product of the irreducible representations of the factor groups. First, we note that the direct product $G_{1}\times G_{2}$ of two compact groups is again a compact group when provided with the product topology. The Haar measure on the direct product is then given by the product of the Haar measures on the factor groups.

For the dual representation on compact groups we require the topological dual $V'$ of the vector space $V.$ This is the vector space of all continuous linear functionals from the vector space V into the base field. Let $\pi$ be a representation of a compact group G in $V.$

The dual representation $\pi ':G\to {\text{GL}}(V')$ is defined by the property

$\forall v\in V,\forall v'\in V',\forall s\in G:\qquad \left\langle \pi '(s)v',\pi (s)v\right\rangle =\langle v',v\rangle :=v'(v).$

Thus, we can conclude that the dual representation is given by $\pi '(s)v'=v'\circ \pi (s^{-1})$ for all $v'\in V',s\in G.$ The map $\pi '$ is again a continuous group homomorphism and thus a representation.

On Hilbert spaces: $\pi$ is irreducible if and only if $\pi '$ is irreducible.

By transferring the results of the section decompositions to compact groups, we obtain the following theorems:

Theorem.

Every irreducible representation

$(\tau ,V_{\tau })$

of a compact group into a

Hilbert space

is finite-dimensional and there exists an

inner product

on

$V_{\tau }$

such that

$\tau$

is unitary. Since the Haar measure is normalized, this inner product is unique.

Every representation of a compact group is isomorphic to a direct Hilbert sum of irreducible representations.

Let $(\rho ,V_{\rho })$ be a unitary representation of the compact group $G.$ Just as for finite groups we define for an irreducible representation $(\tau ,V_{\tau })$ the isotype or isotypic component in $\rho$ to be the subspace

$V_{\rho }(\tau )=\sum _{V_{\tau }\cong U\subset V_{\rho }}U.$

This is the sum of all invariant closed subspaces $U,$ which are G –isomorphic to $V_{\tau }.$

Note that the isotypes of not equivalent irreducible representations are pairwise orthogonal.

Theorem.

(i)

$V_{\rho }(\tau )$

is a closed invariant subspace of

$V_{\rho }.$

(ii)

$V_{\rho }(\tau )$

is

G

–isomorphic to the direct sum of copies of

$V_{\tau }.$

(iii) Canonical decomposition:

$V_{\rho }$

is the direct Hilbert sum of the isotypes

$V_{\rho }(\tau ),$

in which

$\tau$

passes through all the isomorphism classes of the irreducible representations.

The corresponding projection to the canonical decomposition $p_{\tau }:V\to V(\tau ),$ in which $V(\tau )$ is an isotype of $V,$ is for compact groups given by

$p_{\tau }(v)=n_{\tau }\int _{G}{\overline {\chi _{\tau }(t)}}\rho (t)(v)dt,$

where $n_{\tau }=\dim(V(\tau ))$ and $\chi _{\tau }$ is the character corresponding to the irreducible representation $\tau .$

#### Projection formula

For every representation $(\rho ,V)$ of a compact group G we define

$V^{G}=\{v\in V:\rho (s)v=v\,\,\,\forall s\in G\}.$

In general $\rho (s):V\to V$ is not G –linear. Let

$Pv:=\int _{G}\rho (s)vds.$

The map P is defined as endomorphism on V by having the property

$\left.\left(\int _{G}\rho (s)vds\right|w\right)=\int _{G}(\rho (s)v|w)ds,$

which is valid for the inner product of the Hilbert space $V.$

Then P is G –linear, because of

${\begin{aligned}\left.\left(\int _{G}\rho (s)(\rho (t)v)ds\right|w\right)&=\int _{G}\left.\left(\rho \left(tst^{-1}\right)(\rho (t)v)\right|w\right)ds\\&=\int _{G}(\rho (ts)v|w)ds\\&=\int (\rho (t)\rho (s)v|w)ds\\&=\left.\left(\rho (t)\int _{G}\rho (s)vds\right|w\right),\end{aligned}}$

where we used the invariance of the Haar measure.

Proposition.

The map

P

is a projection from

V

to

$V^{G}.$

If the representation is finite-dimensional, it is possible to determine the direct sum of the trivial subrepresentation just as in the case of finite groups.

### Characters, Schur's lemma and the inner product

Generally, representations of compact groups are investigated on Hilbert- and Banach spaces. In most cases they are not finite-dimensional. Therefore, it is not useful to refer to characters when speaking about representations of compact groups. Nevertheless, in most cases it is possible to restrict the study to the case of finite dimensions:

Since irreducible representations of compact groups are finite-dimensional and unitary (see results from the first subsection), we can define irreducible characters in the same way as it was done for finite groups.

As long as the constructed representations stay finite-dimensional, the characters of the newly constructed representations may be obtained in the same way as for finite groups.

**Schur's lemma** is also valid for compact groups:

Let $(\pi ,V)$ be an irreducible unitary representation of a compact group $G.$ Then every bounded operator $T:V\to V$ satisfying the property $T\circ \pi (s)=\pi (s)\circ T$ for all $s\in G,$ is a scalar multiple of the identity, i.e. there exists $\lambda \in \mathbb {C}$ such that $T=\lambda {\text{Id}}.$

**Definition.** The formula

$(\Phi |\Psi )=\int _{G}\Phi (t){\overline {\Psi (t)}}dt.$

defines an inner product on the set of all square integrable functions $L^{2}(G)$ of a compact group $G.$ Likewise

$\langle \Phi ,\Psi \rangle =\int _{G}\Phi (t)\Psi (t^{-1})dt.$

defines a bilinear form on $L^{2}(G)$ of a compact group $G.$

The bilinear form on the representation spaces is defined exactly as it was for finite groups and analogous to finite groups the following results are therefore valid:

Theorem.

Let

$\chi$

and

$\chi '$

be the characters of two non-isomorphic irreducible representations

V

and

$V',$

respectively. Then the following is valid

- $(\chi |\chi ')=0.$
- $(\chi |\chi )=1,$ i.e. $\chi$ has "norm" $1.$

Theorem.

Let

V

be a representation of

G

with character

$\chi _{V}.$

Suppose

W

is an irreducible representation of

G

with character

$\chi _{W}.$

The number of subrepresentations of

V

equivalent to

W

is independent of any given decomposition for

V

and is equal to the inner product

$(\chi _{V}|\chi _{W}).$

Irreducibility Criterion.

Let

$\chi$

be the character of the representation

$V,$

then

$(\chi |\chi )$

is a positive integer. Moreover

$(\chi |\chi )=1$

if and only if

V

is irreducible.

Therefore, using the first theorem, the characters of irreducible representations of G form an orthonormal set on $L^{2}(G)$ with respect to this inner product.

Corollary.

Every irreducible representation

V

of

G

is contained

$\dim(V)$

–times in the left-regular representation.

Lemma.

Let

G

be a compact group. Then the following statements are equivalent:

- G is abelian.
- All the irreducible representations of G have degree $1.$

Orthonormal Property.

Let

G

be a group. The non-isomorphic irreducible representations of

G

form an

orthonormal basis

in

$L^{2}(G)$

with respect to this inner product.

As we already know that the non-isomorphic irreducible representations are orthonormal, we only need to verify that they generate $L^{2}(G).$ This may be done, by proving that there exists no non-zero square integrable function on G orthogonal to all the irreducible characters.

Just as in the case of finite groups, the number of the irreducible representations up to isomorphism of a group G equals the number of conjugacy classes of $G.$ However, because a compact group has in general infinitely many conjugacy classes, this does not provide any useful information.

### The induced representation

If H is a closed subgroup of finite index in a compact group $G,$ the definition of the induced representation for finite groups may be adopted.

However, the induced representation can be defined more generally, so that the definition is valid independent of the index of the subgroup $H.$

For this purpose let $(\eta ,V_{\eta })$ be a unitary representation of the closed subgroup $H.$ The continuous induced representation ${\text{Ind}}_{H}^{G}(\eta )=(I,V_{I})$ is defined as follows:

Let $V_{I}$ denote the Hilbert space of all measurable, square integrable functions $\Phi :G\to V_{\eta }$ with the property $\Phi (ls)=\eta (l)\Phi (s)$ for all $l\in H,s\in G.$ The norm is given by

$\|\Phi \|_{G}={\text{sup}}_{s\in G}\|\Phi (s)\|$

and the representation I is given as the right-translation: $I(s)\Phi (k)=\Phi (ks).$

The induced representation is then again a unitary representation.

Since G is compact, the induced representation can be decomposed into the direct sum of irreducible representations of $G.$ Note that all irreducible representations belonging to the same isotype appear with a multiplicity equal to $\dim({\text{Hom}}_{G}(V_{\eta },V_{I}))=\langle V_{\eta },V_{I}\rangle _{G}.$

Let $(\rho ,V_{\rho })$ be a representation of $G,$ then there exists a canonical isomorphism

$T:{\text{Hom}}_{G}(V_{\rho },I_{H}^{G}(\eta ))\to {\text{Hom}}_{H}(V_{\rho }|_{H},V_{\eta }).$

The Frobenius reciprocity transfers, together with the modified definitions of the inner product and of the bilinear form, to compact groups. The theorem now holds for square integrable functions on G instead of class functions, but the subgroup H must be closed.

### The Peter-Weyl Theorem

Another important result in the representation theory of compact groups is the Peter-Weyl Theorem. It is usually presented and proven in harmonic analysis, as it represents one of its central and fundamental statements.

The Peter-Weyl Theorem.

Let

G

be a compact group. For every irreducible representation

$(\tau ,V_{\tau })$

of

G

let

$\{e_{1},\ldots ,e_{\dim(\tau )}\}$

be an

orthonormal basis

of

$V_{\tau }.$

We define the

matrix coefficients

$\tau _{k,l}(s)=\langle \tau (s)e_{k},e_{l}\rangle$

for

$k,l\in \{1,\ldots ,\dim(\tau )\},s\in G.$

Then we have the following

orthonormal basis

of

$L^{2}(G)$

:

$\left({\sqrt {\dim(\tau )}}\tau _{k,l}\right)_{k,l}$

We can reformulate this theorem to obtain a generalization of the Fourier series for functions on compact groups:

The Peter-Weyl Theorem (Second version).

A proof of this theorem and more information regarding the representation theory of compact groups may be found in

. There exists a natural

$G\times G$

–isomorphism

$L^{2}(G)\cong _{G\times G}{\widehat {\bigoplus }}_{\tau \in {\widehat {G}}}{\text{End}}(V_{\tau })\cong _{G\times G}{\widehat {\bigoplus }}_{\tau \in {\widehat {G}}}\tau \otimes \tau ^{*}$

in which

${\widehat {G}}$

is the set of all irreducible representations of

G

up to isomorphism and

$V_{\tau }$

is the representation space corresponding to

$\tau .$

More concretely:

${\begin{cases}\Phi \mapsto \sum _{\tau \in {\widehat {G}}}\tau (\Phi )\\[5pt]\tau (\Phi )=\int _{G}\Phi (t)\tau (t)dt\in {\text{End}}(V_{\tau })\end{cases}}$


## History

The general features of the representation theory of a finite group *G*, over the complex numbers, were discovered by Ferdinand Georg Frobenius in the years before 1900. Later the modular representation theory of Richard Brauer was developed.
