---
title: "Pin group"
source: https://en.wikipedia.org/wiki/Pin_group
domain: clifford-algebra
license: CC-BY-SA-4.0
tags: clifford algebra, geometric algebra, spinor field, gamma matrices
fetched: 2026-07-02
---

# Pin group

In mathematics, the **pin group** is a certain subgroup of the Clifford algebra associated to a quadratic space. It maps 2-to-1 to the orthogonal group, just as the spin group maps 2-to-1 to the special orthogonal group.

In general the map from the Pin group to the orthogonal group is *not* surjective or a universal covering space, but if the quadratic form is definite (and dimension is greater than 2), it is both.

The non-trivial element of the kernel is denoted $-1,$ which should not be confused with the orthogonal transform of reflection through the origin, generally denoted $-I.$

## General definition

Let V be a vector space with a non-degenerate quadratic form Q . The pin group $\operatorname {Pin} (V,Q)$ is the subset of the Clifford algebra $\operatorname {Cl} (V,Q)$ consisting of elements of the form $v_{1}v_{2}\cdots v_{k}$ , where the $v_{i}$ are vectors such that $Q(v_{i})=\pm 1$ . The spin group $\operatorname {Spin} (V,Q)$ is defined similarly, but with k restricted to be even; it is a subgroup of the pin group.

In this article, V is always a real vector space. When V has basis vectors $e_{1},...,e_{p+q}$ satisfying $e_{1}^{2},...,e_{p}^{2}=1$ and $e_{p+1}^{2},...,e_{p+q}^{2}=-1,$ the pin group is denoted Pin(*p*, *q*).

Geometrically, for vectors v with $Q(v)\neq 0$ , $-vwv^{-1}$ is the reflection of a vector w across the hyperplane orthogonal to v . More generally, an element $v_{1}v_{2}\cdots v_{k}$ of the pin group acts on vectors by transforming w to $(-1)^{k}v_{1}v_{2}\cdots v_{k}w(v_{1}v_{2}\cdots v_{k})^{-1}$ , which is the composition of *k* reflections. Since every orthogonal transformation can be expressed as a composition of reflections (the Cartan–Dieudonné theorem), it follows that this representation of the pin group is a homomorphism from the pin group onto the orthogonal group. This is often called the twisted adjoint representation. The elements ±1 of the pin group are the elements which map to the identity $I\in O(p,q)$ , and every element of $O(p,q)$ corresponds to exactly two elements of $\operatorname {Pin} (p,q)$ .

## Definite form

The pin group of a definite form maps onto the orthogonal group, and each component is simply connected (in dimension 3 and higher): it double covers the orthogonal group. The pin groups for a positive definite quadratic form *Q* and for its negative −*Q* are not isomorphic, but the orthogonal groups are.

In terms of the standard forms, O(*n*, 0) = O(0, *n*), but Pin(*n*, 0) and Pin(0, *n*) are in general not isomorphic. Using the "+" sign convention for Clifford algebras (where $v^{2}=Q(v)\in \mathrm {Cl} (V,Q)$ ), one writes

${\mbox{Pin}}_{+}(n):={\mbox{Pin}}(n,0)\qquad {\mbox{Pin}}_{-}(n):={\mbox{Pin}}(0,n)$

and these both map onto O(*n*) = O(*n*, 0) = O(0, *n*).

By contrast, we have the natural isomorphism Spin(*n*, 0) ≅ Spin(0, *n*) and they are both the (unique) non-trivial double cover of the special orthogonal group SO(*n*), which is the (unique) universal cover for *n* ≥ 3.

## Indefinite form

Depending on how one counts, and the values of *q* and *p*, there may be as many as thirty-two different double covers of O(*p*, *q*), for *p*, *q* ≠ 0. Only two of them are the standard pin groups—those that are contained within the standard Clifford algebra constructions. They are called Pin(*p*, *q*) and Pin(*q*, *p*) respectively. Not all of these extensions are 'spinoral': one of these double covers, for example, is the trivial extension, which topologically is merely two copies of O(*q*, *p*).

It is worth pointing out for the indefinite case that while the group (in particular here, the component connected to the identity) Spin(*p*, *q*) is by definition a double cover of the special orthogonal group SO(*p*, *q*), this double covering is unique only in the compact and Lorentzian cases SO(*n*) and SO(*1*, *q*) with *q*>2. For SO(*p*, *q*) when both *p* and *q* are greater than two, the group has 3 unique connected double covers (only one of which is the spin group). Its universal cover is none of these, and is a non-trivial extension of the special orthogonal group by the Klein group, and so is a four fold covering of SO(*p*, *q*). The case of *p* or *q* being 2 is complicated (but well understood) by the infinite homotopy group of SO(2).

## As topological group

Every connected topological group has a unique universal cover as a topological space, which has a unique group structure as a central extension by the fundamental group. For a disconnected topological group, there is a unique universal cover of the identity component of the group, and one can take the same cover as topological spaces on the other components (which are principal homogeneous spaces for the identity component) but the group structure on other components is not uniquely determined in general.

The Pin and Spin groups are *particular* topological groups associated to the orthogonal and special orthogonal groups, coming from Clifford algebras: there are other similar groups, corresponding to other double covers or to other group structures on the other components, but they are not referred to as Pin or Spin groups, nor studied much.

In 2001, Andrzej Trautman found the set of all 32 inequivalent double covers of O(*p*) x O(*q*), the maximal compact subgroup of O(*p*, *q*) and an explicit construction of 8 double covers of the same group O(*p*, *q*).

## Construction

The two pin groups correspond to the two central extensions

$1\to \{\pm 1\}\to {\mbox{Pin}}_{\pm }(V)\to \mathrm {O} (V)\to 1.$

The group structure on Spin(*V*) (the connected component of determinant 1) is already determined; the group structure on the other component is determined up to the center, and thus has a ±1 ambiguity.

The two extensions are distinguished by whether the preimage of a reflection squares to ±1 ∈ Ker (Spin(*V*) → SO(*V*)), and the two pin groups are named accordingly. Explicitly, a reflection has order 2 in O(*V*), *r*2 = 1, so the square of the preimage of a reflection (which has determinant one) must be in the kernel of Spin±(*V*) → SO(*V*), so ${\tilde {r}}^{2}=\pm 1$ , and either choice determines a pin group (since all reflections are conjugate by an element of SO(*V*), which is connected, all reflections must square to the same value).

Concretely, in Pin+, ${\tilde {r}}$ has order 2, and the preimage of a subgroup {1, *r*} is C2 × C2: if one repeats the same reflection twice, one gets the identity.

In Pin−, ${\tilde {r}}$ has order 4, and the preimage of a subgroup {1, *r*} is C4: if one repeats the same reflection twice, one gets "a rotation by 2π"—the non-trivial element of Spin(*V*) → SO(*V*) can be interpreted as "rotation by 2π" (every axis yields the same element).

### Low dimensions

In 1 dimension, the pin groups are congruent to the first dihedral and dicyclic groups:

${\begin{aligned}{\mbox{Pin}}_{+}(1)&\cong \mathrm {C} _{2}\times \mathrm {C} _{2}={\mbox{Dih}}_{1}\\{\mbox{Pin}}_{-}(1)&\cong \mathrm {C} _{4}={\mbox{Dic}}_{1}.\end{aligned}}$

In 2 dimensions, the distinction between Pin+ and Pin− mirrors the distinction between the dihedral group of a 2*n*-gon and the dicyclic group of the cyclic group C2*n*.

In Pin+, the preimage of the dihedral group of an *n*-gon, considered as a subgroup Dih*n* < O(2), is the dihedral group of a 2*n*-gon, Dih2*n* < Pin+(2), while in Pin−, the preimage of the dihedral group is the dicyclic group Dic*n* < Pin−(2).

The resulting commutative square of subgroups for Spin(2), Pin+(2), SO(2), O(2) – namely C2*n*, Dih2*n*, C*n*, Dih*n* – is also obtained using the projective orthogonal group (going down from O by a 2-fold quotient, instead of up by a 2-fold cover) in the square SO(2), O(2), PSO(2), PO(2), though in this case it is also realized geometrically, as "the projectivization of a 2*n*-gon in the circle is an *n*-gon in the projective line".

In 3 dimensions the situation is as follows. The Clifford algebra generated by 3 anticommuting square roots of +1 is the algebra of 2×2 complex matrices, and Pin+(3) is isomorphic to $\{A\in U(2):\det A=\pm 1\}$ . The Clifford algebra generated by 3 anticommuting square roots of -1 is the algebra $\mathbb {H} \oplus \mathbb {H}$ , and Pin−(3) is isomorphic to SU(2) × C2. These groups are nonisomorphic because the center of Pin+(3) is C4 while the center of Pin−(3) is C2 × C2.

## Center

For real (as opposed to complex) compact Pin groups, the center depends upon the dimension n of the relevant vector space, modulo four. If $n=2k$ is even, the Clifford algebra is central simple, and as such the center of either $\mathrm {Pin}$ group can only be $\mathrm {C} _{2}$ . When $n=4k+1$ , the center of $\mathrm {Pin} _{+}(4k+1)$ is $\mathrm {C} _{2}\times \mathrm {C} _{2}$ , and the center of $\mathrm {Pin} _{-}(4k+1)$ is $\mathrm {C} _{4}$ . When $n=4k+3$ , the center of $\mathrm {Pin} _{+}(4k+3)$ is $\mathrm {C} _{4}$ , and the center of $\mathrm {Pin} _{-}(4k+3)$ is $\mathrm {C} _{2}\times \mathrm {C} _{2}$ .

In the indefinite case for $\mathrm {Pin} (p,q)$ where $n=p+q$ , one has the same situation but determined instead by $(p-q)\operatorname {mod} 8$ . The even dimensional case is as before: when $(p-q)\operatorname {mod} 2=0$ the algebra is central simple, and so the Pin group has a center of $\mathrm {C} _{2}$ . When $p-q\operatorname {mod} 8=4k+1$ , the center is $\mathrm {C} _{2}\times \mathrm {C} _{2}$ . When $p-q\operatorname {mod} 8=4k+3$ , the center is $\mathrm {C} _{4}$ . The case of opposite signature is simply swapping *p* and *q*, and repeating the above. In the odd dimensional case, if one signature has center $\mathrm {C} _{4}$ , the other signature has center $\mathrm {C} _{2}\times \mathrm {C} _{2}$ , and vice versa.

Though it may seem the center should always be order four, as the orthogonal group always has center of order two, those Pin group elements which are mapped to the center of the orthogonal group need only commute with everything up to a sign, as the Pin group serves as a projective representation of the orthogonal group. That is to say, pre-images of the center of the orthogonal group, need only commute or anti-commute with every element of the Pin group.

## Name

The name was introduced in (Atiyah, Bott & Shapiro 1964, page 3, line 17), where they state "This joke is due to J-P. Serre". It is a back-formation from Spin: "Pin is to O(*n*) as Spin is to SO(*n*)", hence dropping the "S" from "Spin" yields "Pin".
