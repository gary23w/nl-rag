---
title: "Fundamental theorem of Galois theory"
source: https://en.wikipedia.org/wiki/Fundamental_theorem_of_Galois_theory
domain: galois-theory
license: CC-BY-SA-4.0
tags: galois theory, galois group, field extension, solvable group
fetched: 2026-07-02
---

# Fundamental theorem of Galois theory

In mathematics, the **fundamental theorem of Galois theory** is a result that describes the structure of certain types of field extensions in relation to groups. It was proved by Évariste Galois in his development of Galois theory.

In its most basic form, the theorem asserts that given a field extension $E/F$ that is finite and Galois, there is a one-to-one correspondence between its intermediate fields and subgroups of its Galois group. (*Intermediate fields* are fields K satisfying $F\subseteq K\subseteq E$ ; they are also called *subextensions* of $E/F$ .)

## Explicit description of the correspondence

For finite extensions, the correspondence can be described explicitly as follows.

- For any subgroup H of ${\text{Gal}}(E/F)$ , the corresponding fixed field, denoted $E^{H}$ , is the set of those elements of E which are fixed by every automorphism in H .
- For any intermediate field K of $E/F$ , the corresponding subgroup is ${\text{Aut}}(E/K)$ , that is, the set of those automorphisms in ${\text{Gal}}(E/F)$ which fix every element of K .

The fundamental theorem says that this correspondence is a one-to-one correspondence if (and only if) $E/F$ is a Galois extension. For example, the topmost field E corresponds to the trivial subgroup of ${\text{Gal}}(E/F)$ , and the base field F corresponds to the whole group ${\text{Gal}}(E/F)$ .

The notation ${\text{Gal}}(E/F)$ is only used for Galois extensions. If $E/F$ is Galois, then ${\text{Gal}}(E/F)={\text{Aut}}(E/F)$ . If $E/F$ is not Galois, then the "correspondence" gives only an injective (but not surjective) map from $\{{\text{subgroups of Aut}}(E/F)\}$ to $\{{\text{subfields of }}E/F\}$ , and a surjective (but not injective) map in the reverse direction. In particular, if $E/F$ is not Galois, then F is not the fixed field of any subgroup of ${\text{Aut}}(E/F)$ .

## Properties of the correspondence

The correspondence has the following useful properties.

- It is *inclusion-reversing*. The inclusion of subgroups $H_{1}\subseteq H_{2}$ holds if and only if the inclusion of fields $E^{H_{1}}\supseteq E^{H_{2}}$ holds.
- Degrees of extensions are related to orders of groups, in a manner consistent with the inclusion-reversing property. Specifically, if H is a subgroup of ${\text{Gal}}(E/F)$ , then $|H|=\left[E:E^{H}\right]$ and $\left|{\text{Gal}}(E/F)\right|/|H|=\left[E^{H}:F\right]$ .
- The field $E^{H}$ is a normal extension of F (or, equivalently, Galois extension, since any subextension of a separable extension is separable) if and only if H is a normal subgroup of ${\text{Gal}}(E/F)$ . In this case, the restriction of the elements of ${\text{Gal}}(E/F)$ to $E^{H}$ induces an isomorphism between ${\text{Gal}}(E^{H}/F)$ and the quotient group ${\text{Gal}}(E/F)/H$ .

## Example 1

Consider the field

$K=\mathbb {Q} \left({\sqrt {2}},{\sqrt {3}}\right)=\left[\mathbb {Q} ({\sqrt {2}})\right]\!({\sqrt {3}}).$

Since *K* is constructed from the base field $\mathbb {Q}$ by adjoining √2, then √3, each element of *K* can be written as:

$(a+b{\sqrt {2}})+(c+d{\sqrt {2}}){\sqrt {3}},\qquad a,b,c,d\in \mathbb {Q} .$

Its Galois group $G={\text{Gal}}(K/\mathbb {Q} )$ comprises the automorphisms of *K* which fix *a*. Such automorphisms must send √2 to √2 or –√2, and send √3 to √3 or –√3, since they permute the roots of any irreducible polynomial. Suppose that *f* exchanges √2 and –√2, so

$f\left((a+b{\sqrt {2}})+(c+d{\sqrt {2}}){\sqrt {3}}\right)=(a-b{\sqrt {2}})+(c-d{\sqrt {2}}){\sqrt {3}}=a-b{\sqrt {2}}+c{\sqrt {3}}-d{\sqrt {6}},$

and *g* exchanges √3 and –√3, so

$g\left((a+b{\sqrt {2}})+(c+d{\sqrt {2}}){\sqrt {3}}\right)=(a+b{\sqrt {2}})-(c+d{\sqrt {2}}){\sqrt {3}}=a+b{\sqrt {2}}-c{\sqrt {3}}-d{\sqrt {6}}.$

These are clearly automorphisms of *K*, respecting its addition and multiplication. There is also the identity automorphism *e* which fixes each element, and the composition of *f* and *g* which changes the signs on *both* radicals:

$(fg)\left((a+b{\sqrt {2}})+(c+d{\sqrt {2}}){\sqrt {3}}\right)=(a-b{\sqrt {2}})-(c-d{\sqrt {2}}){\sqrt {3}}=a-b{\sqrt {2}}-c{\sqrt {3}}+d{\sqrt {6}}.$

Since the order of the Galois group is equal to the degree of the field extension, $|G|=[K:\mathbb {Q} ]=4$ , there can be no further automorphisms:

$G=\left\{1,f,g,fg\right\},$

which is isomorphic to the Klein four-group. Its five subgroups correspond to the fields intermediate between the base $\mathbb {Q}$ and the extension *K*.

- The trivial subgroup {1} corresponds to the entire extension field *K*.
- The entire group *G* corresponds to the base field $\mathbb {Q} .$
- The subgroup {1, *f*} corresponds to the subfield $\mathbb {Q} ({\sqrt {3}}),$ since *f* fixes √3.
- The subgroup {1, *g*} corresponds to the subfield $\mathbb {Q} ({\sqrt {2}}),$ since *g* fixes √2.
- The subgroup {1, *fg*} corresponds to the subfield $\mathbb {Q} ({\sqrt {6}}),$ since *fg* fixes √6.

## Example 2

The following is the simplest case where the Galois group is not abelian.

Consider the splitting field *K* of the irreducible polynomial $x^{3}-2$ over $\mathbb {Q}$ ; that is, $K=\mathbb {Q} (\theta ,\omega )$ where *θ* is a cube root of 2, and *ω* is a cube root of 1 (but not 1 itself). If we consider *K* inside the complex numbers, we may take $\theta ={\sqrt[{3}]{2}}$ , the real cube root of 2, and $\omega =-{\tfrac {1}{2}}+i{\tfrac {\sqrt {3}}{2}}.$ Since *ω* has minimal polynomial $x^{2}+x+1$ *,* the extension $\mathbb {Q} \subset K$ has degree: $[\,K:\mathbb {Q} \,]=[\,K:\mathbb {Q} (\,\theta \,)\,]\cdot [\,\mathbb {Q} (\,\theta \,):\mathbb {Q} \,]=2\cdot 3=6,$ with $\mathbb {Q}$ -basis $\{1,\theta ,\theta ^{2},\omega ,\omega \theta ,\omega \theta ^{2}\}$ as in the previous example. Therefore, the Galois group $G=\mathrm {Gal} (K/\mathbb {Q} )$ has six elements, determined by all permutations of the three roots of $x^{3}-2$ :

> $\alpha _{1}=\theta ,\ \alpha _{2}=\omega \theta ,\ \alpha _{3}=\omega ^{2}\theta .$

Since there are only 3! = 6 such permutations, *G* must be isomorphic to the symmetric group of all permutations of three objects. The group can be generated by two automorphisms *f* and *g* defined by:

$f(\theta )=\omega \theta ,\quad f(\omega )=\omega ,$

$g(\theta )=\theta ,\quad g(\omega )=\omega ^{2},$

and $G=\left\{1,f,f^{2},g,gf,gf^{2}\right\}$ , obeying the relations $f^{3}=g^{2}=(gf)^{2}=1$ . Their effect as permutations of $\alpha _{1},\alpha _{2},\alpha _{3}$ is (in cycle notation): $f=(123),g=(23)$ . Also, *g* can be considered as the complex conjugation mapping.

The subgroups of *G* and corresponding subfields are as follows:

- As always, the trivial group {1} corresponds to the whole field *K*, while the entire group *G* to the base field $\mathbb {Q}$ .
- The unique subgroup of order 3, $H=\{1,f,f^{2}\}$ , corresponds to the subfield $\mathbb {Q} (\omega )$ of degree two, since the subgroup has index two in *G*: i.e. $[\mathbb {Q} (\omega ):\mathbb {Q} ]={\tfrac {|G|}{|H|}}=2$ . Also, this subgroup is normal, so the subfield is normal over $\mathbb {Q}$ , being the splitting field of $x^{2}+x+1$ . Its Galois group over the base field is the quotient group $G/H=\{[1],[g]\}$ , where [*g*] denotes the coset of *g* modulo *H*; that is, its only non-trivial automorphism is the complex conjugation *g*.
- There are three subgroups of order 2, $\{1,g\},\{1,gf\}$ and $\{1,gf^{2}\},$ corresponding respectively to the subfields $\mathbb {Q} (\theta ),\mathbb {Q} (\omega \theta ),\mathbb {Q} (\omega ^{2}\theta ).$ These subfields have degree 3 over $\mathbb {Q}$ since the subgroups have index 3 in *G*. The subgroups are *not* normal in *G*, so the subfields are *not* Galois or normal over $\mathbb {Q}$ . In fact, each subfield contains only a single one of the roots $\alpha _{1},\alpha _{2},\alpha _{3}$ , so none has any non-trivial automorphisms.

## Example 3

Let $E=\mathbb {Q} (\lambda )$ be the field of rational functions in the indeterminate *λ,* and consider the group of automorphisms:

$G=\left\{\lambda ,{\frac {1}{1-\lambda }},{\frac {\lambda -1}{\lambda }},{\frac {1}{\lambda }},{\frac {\lambda }{\lambda -1}},1-\lambda \right\}\subset \mathrm {Aut} (E);$

here we denote an automorphism $\phi :E\to E$ by its value $\phi (\lambda )$ , so that $f(\lambda )\mapsto f(\phi (\lambda ))$ . This group is isomorphic to $S_{3}$ (see: six cross-ratios). Let F be the fixed field of G , so that ${\rm {Gal}}(E/F)=G$ .

If H is a subgroup of G , then the coefficients of the polynomial

$P(T):=\prod _{h\in H}(T-h)\in E[T]$

generate the fixed field of H . The Galois correspondence implies that every subfield of $E/F$ can be constructed this way. For example, for $H=\{\lambda ,1-\lambda \}$ , the fixed field is $\mathbb {Q} (\lambda (1-\lambda ))$ and if $H=\{\lambda ,{\tfrac {1}{\lambda }}\}$ then the fixed field is $\mathbb {Q} (\lambda +{\tfrac {1}{\lambda }})$ . The fixed field of G is the base field $F=\mathbb {Q} (j),$ where j is the j-invariant written in terms of the modular lambda function:

> $j={\frac {256(1-\lambda (1-\lambda ))^{3}}{(\lambda (1-\lambda ))^{2}}}={\frac {256(1-\lambda +\lambda ^{2})^{3}}{\lambda ^{2}(1-\lambda )^{2}}}\ .$

Similar examples can be constructed for each of the symmetry groups of the platonic solids as these also have faithful actions on the projective line $\mathbb {P} ^{1}(\mathbb {C} )$ and hence on $\mathbb {C} (x)$ .

## Example 4

Here we give an example of a finite extension $E/F$ which is not Galois, and with this we show that (the fundamental theorem of) Galois theory no longer works when $E/F$ is not Galois.

Let $E=\mathbb {Q} ({\sqrt[{3}]{2}})$ and $F=\mathbb {Q}$ . Then $E/F$ is a finite extension, but not a splitting field over F (since the minimal polynomials of ${\sqrt[{3}]{2}}$ has two complex roots that do not lie in E ). Any $f\in G=\mathrm {Gal} (E/F)$ is completely determined by $f({\sqrt[{3}]{2}})$ and that $2=f({\sqrt[{3}]{2}})^{3}\implies f=1$ Thus, $G=\{1\}$ , is the trivial group. In particular, $|G|=1<3=[E:F]$ . This shows that $E/F$ is not Galois.

Now, G has only one subgroup, i.e., itself. The only intermediate field that contains $F=\mathbb {Q}$ is $E=\mathbb {Q} ({\sqrt[{3}]{2}})$ . It follows that the Galois correspondence fails.

## Applications

The theorem classifies the intermediate fields of *E*/*F* in terms of group theory. This translation between intermediate fields and subgroups is key to showing that the general quintic equation is not solvable by radicals (see Abel–Ruffini theorem). One first determines the Galois groups of radical extensions (extensions of the form *F*(α) where α is an *n*-th root of some element of *F*), and then uses the fundamental theorem to show that solvable extensions correspond to solvable groups.

Theories such as Kummer theory and class field theory are predicated on the fundamental theorem.

## Infinite case

Given an infinite algebraic extension we can still define it to be Galois if it is normal and separable. The problem that one encounters in the infinite case is that the bijection in the fundamental theorem does not hold as we get too many subgroups generally. More precisely if we just take every subgroup we can in general find two different subgroups that fix the same intermediate field. Therefore, we amend this by introducing a topology on the Galois group.

Let $E/F$ be a Galois extension (possibly infinite) and let $G={\text{Gal}}(E/F)$ be the Galois group of the extension. Let ${\text{Int}}_{\text{F}}(E/F)=\{G_{i}={\text{Gal}}(L_{i}/F)~|~L_{i}/F{\text{ is a finite Galois extension and }}L_{i}\subseteq E\}$ be the set of the Galois groups of all finite intermediate Galois extensions. Note that for all $i\in I$ we can define the maps $\varphi _{i}:G\rightarrow G_{i}$ by $\sigma \mapsto \sigma _{|L_{i}}$ . We then define the *Krull topology* on G to be weakest topology such that for all $i\in I$ the maps $\varphi _{i}:G\rightarrow G_{i}$ are continuous, where we endow each $G_{i}$ with the discrete topology. Stated differently $G\cong \varprojlim G_{i}$ as an inverse limit of topological groups (where again each $G_{i}$ is endowed with the discrete topology). This makes G a profinite group (in fact every profinite group can be realised as the Galois group of a Galois extension, see for example ). Note that when $E/F$ is finite, the Krull topology is the discrete topology.

Now that we have defined a topology on the Galois group we can restate the fundamental theorem for infinite Galois extensions.

Let ${\mathcal {F}}(E/F)$ denote the set of all intermediate field extensions of $E/F$ and let ${\mathcal {C}}(G)$ denote the set of all closed subgroups of $G={\text{Gal}}(E/F)$ endowed with the Krull topology. Then there exists a bijection between ${\mathcal {F}}(E/F)$ and ${\mathcal {C}}(G)$ given by the map

$\Phi :{\mathcal {F}}(E/F)\rightarrow {\mathcal {C}}(G)$

defined by $L\mapsto {\text{Gal}}(E/L)$ and the map

$\Gamma :{\mathcal {C}}(G)\rightarrow {\mathcal {F}}(E/F)$

defined by $N\mapsto {\text{Fix}}_{E}(N):=\{a\in E~|~\sigma (a)=a{\text{ for all }}\sigma \in N\}$ . One important thing one needs to check is that $\Phi$ is a well-defined map, that is that $\Phi (L)$ is a closed subgroup of G for all intermediate fields L . This is proved in Ribes–Zalesskii, Theorem 2.11.3.
