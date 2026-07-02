---
title: "Quotient group"
source: https://en.wikipedia.org/wiki/Quotient_group
domain: abstract-algebra
license: CC-BY-SA-4.0
tags: abstract algebra, algebraic structure, group homomorphism, quotient structure
fetched: 2026-07-02
---

# Quotient group

In the branch of mathematics known as group theory, a **quotient group** or **factor group** is a group obtained by aggregating similar elements of a larger group using an equivalence relation that preserves some of the group structure (the rest of the structure is "factored out").

For example, the cyclic group of addition modulo *n* can be obtained from the group of integers under addition by identifying elements that differ by a multiple of n and defining a group structure that operates on each such class (known as a congruence class) as a single entity.

For a congruence relation on a group, the equivalence class of the identity element is always a normal subgroup of the original group, and the other equivalence classes are precisely the cosets of that normal subgroup. The resulting quotient is written ⁠ $G\,/\,N$ ⁠, where G is the original group and N is the normal subgroup. This is read as '⁠ $G{\bmod {N}}$ ⁠', where ${\text{mod}}$ is short for modulo. (The notation ⁠ $G\,/\,H$ ⁠ should be interpreted with caution, as some authors (e.g., Vinberg) use it to represent the left cosets of H in G for *any* subgroup H , even though these cosets do not form a group if H is not normal in ⁠ G ⁠. Others (e.g., Dummit and Foote) use this notation to refer only to the quotient group, with the appearance of this notation implying that H is normal in ⁠ G ⁠.)

Much of the importance of quotient groups is derived from their relation to homomorphisms. The first isomorphism theorem states that the image of any group G under a homomorphism is always isomorphic to a quotient of ⁠ G ⁠. Specifically, the image of G under a homomorphism $\varphi :G\rightarrow H$ is isomorphic to $G\,/\,\ker(\varphi )$ where $\ker(\varphi )$ denotes the kernel of ⁠ $\varphi$ ⁠.

The dual notion of a quotient group is a subgroup, these being the two primary ways of forming a smaller group from a larger one. Any normal subgroup has a corresponding quotient group, formed from the larger group by eliminating the distinction between elements of the subgroup. In category theory, quotient groups are examples of quotient objects, which are dual to subobjects.

## Definition and illustration

Given a group G and a subgroup ⁠ H ⁠, and a fixed element $a\in G$ , one can consider the corresponding left coset: ⁠ $aH:=\left\{ah:h\in H\right\}$ ⁠. Cosets are a natural class of subsets of a group; for example consider the abelian group G of integers, with operation defined by the usual addition, and the subgroup H of even integers. Then there are exactly two cosets: ⁠ $0+H$ ⁠, which are the even integers, and ⁠ $1+H$ ⁠, which are the odd integers (here we are using additive notation for the binary operation instead of multiplicative notation). The quotient group $G/H$ is thus $\{0+H,1+H\}$ , a two-element group isomorphic to $\mathbb {Z} /2\mathbb {Z}$ .

For a general subgroup ⁠ H ⁠, it is desirable to define a compatible group operation on the set of all possible cosets, ⁠ $\left\{aH:a\in G\right\}$ ⁠. This is possible exactly when H is a normal subgroup, see below. A subgroup N of a group G is normal if and only if the coset equality $aN=Na$ holds for all ⁠ $a\in G$ ⁠. A normal subgroup of G is denoted ⁠ N ⁠.

### Definition

Let N be a normal subgroup of a group ⁠ G ⁠. The quotient group $G\,/\,N$ is defined to be the set of all left cosets of N in ⁠ G ⁠, i.e. ⁠ $G\,/\,N=\left\{aN:a\in G\right\}$ ⁠, with the group operation defined as ⁠ $(aN)(bN)=(ab)N\ \forall \ a,b\in G$ ⁠. It can be shown that this operation satisfies all of the group axioms.

As N is a normal subgroup of G , the left and right cosets of N in G are the same, and so $G\,/\,N$ could equivalently have been defined to be the set of all right cosets of N in ⁠ G ⁠. Since the identity element ⁠ $e\in N$ ⁠, ⁠ $a\in aN$ ⁠.

To avoid contradiction, this definition requires that $(ab)N$ is the same when $aN$ or $bN$ are constructed using different elements of G , i.e. if ⁠ $aN=xN$ ⁠ and ⁠ $bN=yN$ ⁠, then ⁠ $(ab)N=(xy)N$ ⁠. This can be shown to always be true when N is a normal subgroup as follows: ${\textstyle (ab)N=a(bN)=a(yN)=a(Ny)=(aN)y=(xN)y=x(Ny)=x(yN)=(xy)N.}$ where ⁠ $a,b,x,y\in G$ ⁠. This proof is only valid for normal subgroups, as it uses the property ⁠ $yN=Ny$ ⁠.

This shows that the operation is well-defined when N is a normal subgroup. The definition however *required* that N be a normal subgroup. This is because the group operation is *only* well-defined for normal subgroups.

To show this, first assume that the group operation is well defined, i.e. that if $xN=aN$ and $yN=bN$ for any ⁠ $x,y,a,b\in G$ ⁠, then ⁠ $(ab)N=(xy)N$ ⁠.

Now take any $n\in N$ and ⁠ $g\in G$ ⁠. Using the property of cosets that ⁠ $nN=N=eN$ ⁠, we have: ⁠ $gN=(eg)N=(eN)(gN)=(nN)(gN)=(ng)N$ ⁠.

Using $gN=(ng)N$ , we have ⁠ $N=(g^{-1}ng)N$ ⁠, and so ⁠ $g^{-1}ng\in N,\;\forall \,n\in N,g\in G$ ⁠, meaning that N must be a normal subgroup of G . As such, the group operation is only well-defined if N is a normal subgroup.

### Example: Addition modulo 6

For example, consider the group with addition modulo 6: ⁠ $G=\left\{0,1,2,3,4,5\right\}$ ⁠. Consider the subgroup ⁠ $N=\left\{0,3\right\}$ ⁠, which is normal because G is abelian. Then the set of (left) cosets is of size three:

$G\,/\,N=\left\{a+N:a\in G\right\}=\left\{\left\{0,3\right\},\left\{1,4\right\},\left\{2,5\right\}\right\}=\left\{0+N,1+N,2+N\right\}.$

The binary operation defined above makes this set into a group, known as the quotient group, which in this case is isomorphic to the cyclic group of order 3.

## Motivation for the name "quotient"

The quotient group $G\,/\,N$ can be compared to division of integers. When dividing 12 by 3 one obtains the result 4 because one can regroup 12 objects into 4 subcollections of 3 objects. The quotient group is the same idea, although one ends up with a group for a final answer instead of a number. In general groups have more structure than an arbitrary collection of objects: in the quotient ⁠ $G\,/\,N$ ⁠, therefore the group structure is used to form a natural "regrouping". These are the cosets of N in ⁠ G ⁠. Because we started with a group and normal subgroup, the final quotient contains more information than just the number of cosets (which is what regular division yields), but instead has a group structure itself.

## Examples

### Even and odd integers

Consider the group of integers $\mathbb {Z}$ (under addition) and the subgroup $2\mathbb {Z}$ consisting of all even integers. This is a normal subgroup, because $\mathbb {Z}$ is abelian. There are only two cosets: the set of even integers and the set of odd integers, and therefore the quotient group $\mathbb {Z} \,/\,2\mathbb {Z}$ is the cyclic group with two elements. This quotient group is isomorphic with the set $\left\{0,1\right\}$ with addition modulo 2; informally, it is sometimes said that $\mathbb {Z} \,/\,2\mathbb {Z}$ *equals* the set $\left\{0,1\right\}$ with addition modulo 2.

**Example further explained...**

Let

$\gamma (m)$

be the remainders of

$m\in \mathbb {Z}$

when dividing by

⁠

2

⁠

. Then,

$\gamma (m)=0$

when

m

is even and

$\gamma (m)=1$

when

m

is odd.

By definition of

⁠

$\gamma$

⁠

, the kernel of

⁠

$\gamma$

⁠

,

⁠

$\ker(\gamma )=\{m\in \mathbb {Z} :\gamma (m)=0\}$

⁠

, is the set of all even integers.

Let

⁠

$H=\ker(\gamma )$

⁠

. Then,

H

is a subgroup, because the identity in

⁠

$\mathbb {Z}$

⁠

, which is

⁠

0

⁠

, is in

⁠

H

⁠

, the sum of two even integers is even and hence if

m

and

n

are in

⁠

H

⁠

,

$m+n$

is in

H

(closure) and if

m

is even,

$-m$

is also even and so

H

contains its inverses.

Define

$\mu :\mathbb {Z} /H\to \mathrm {Z} _{2}$

as

$\mu (aH)=\gamma (a)$

for

$a\in \mathbb {Z}$

and

$\mathbb {Z} /H$

is the quotient group of left cosets;

⁠

$\mathbb {Z} /H=\{H,1+H\}$

⁠

.

Note that we have defined

⁠

$\mu$

⁠

,

$\mu (aH)$

is

1

if

a

is odd and

0

if

a

is even.

Thus,

$\mu$

is an isomorphism from

$\mathbb {Z} /H$

to

⁠

$\mathrm {Z} _{2}$

⁠

.

### Remainders of integer division

A slight generalization of the last example. Once again consider the group of integers $\mathbb {Z}$ under addition. Let ⁠ n ⁠ be any positive integer. We will consider the subgroup $n\mathbb {Z}$ of $\mathbb {Z}$ consisting of all multiples of ⁠ n ⁠. Once again $n\mathbb {Z}$ is normal in $\mathbb {Z}$ because $\mathbb {Z}$ is abelian. The cosets are the collection ⁠ $\left\{n\mathbb {Z} ,1+n\mathbb {Z} ,\;\ldots ,(n-2)+n\mathbb {Z} ,(n-1)+n\mathbb {Z} \right\}$ ⁠. An integer k belongs to the coset ⁠ $r+n\mathbb {Z}$ ⁠, where r is the remainder when dividing k by ⁠ n ⁠. The quotient $\mathbb {Z} \,/\,n\mathbb {Z}$ can be thought of as the group of "remainders" modulo ⁠ n ⁠. This is a cyclic group of order ⁠ n ⁠.

### Complex integer roots of 1

The twelfth roots of unity, which are points on the complex unit circle, form a multiplicative abelian group ⁠ G ⁠, shown on the picture on the right as colored balls with the number at each point giving its complex argument. Consider its subgroup N made of the fourth roots of unity, shown as red balls. This normal subgroup splits the group into three cosets, shown in red, green and blue. One can check that the cosets form a group of three elements (the product of a red element with a blue element is blue, the inverse of a blue element is green, etc.). Thus, the quotient group $G\,/\,N$ is the group of three colors, which turns out to be the cyclic group with three elements.

### Real numbers modulo the integers

Consider the group of real numbers $\mathbb {R}$ under addition, and the subgroup $\mathbb {Z}$ of integers. Each coset of $\mathbb {Z}$ in $\mathbb {R}$ is a set of the form ⁠ $a+\mathbb {Z}$ ⁠, where a is a real number. Since $a_{1}+\mathbb {Z}$ and $a_{2}+\mathbb {Z}$ are identical sets when the non-integer parts of $a_{1}$ and $a_{2}$ are equal, one may impose the restriction $0\leq a<1$ without change of meaning. Adding such cosets is done by adding the corresponding real numbers, and subtracting 1 if the result is greater than or equal to 1. The quotient group $\mathbb {R} \,/\,\mathbb {Z}$ is isomorphic to the circle group, the group of complex numbers of absolute value 1 under multiplication, or correspondingly, the group of rotations in 2D about the origin, that is, the special orthogonal group ⁠ $\mathrm {SO} (2)$ ⁠. An isomorphism is given by $f(a+\mathbb {Z} )=\exp(2\pi ia)$ (see Euler's identity).

### Matrices of real numbers

If G is the group of invertible $3\times 3$ real matrices, and N is the subgroup of $3\times 3$ real matrices with determinant 1, then N is normal in G (since it is the kernel of the determinant homomorphism). The cosets of N are the sets of matrices with a given determinant, and hence $G\,/\,N$ is isomorphic to the multiplicative group of non-zero real numbers. The group N is known as the special linear group ⁠ $\mathrm {SL} (3)$ ⁠.

### Integer modular arithmetic

Consider the abelian group $\mathrm {Z} _{4}=\mathbb {Z} \,/\,4\mathbb {Z}$ (that is, the set $\left\{0,1,2,3\right\}$ with addition modulo 4), and its subgroup ⁠ $\left\{0,2\right\}$ ⁠. The quotient group $\mathrm {Z} _{4}\,/\,\left\{0,2\right\}$ is ⁠ $\left\{\left\{0,2\right\},\left\{1,3\right\}\right\}$ ⁠. This is a group with identity element ⁠ $\left\{0,2\right\}$ ⁠, and group operations such as ⁠ $\left\{0,2\right\}+\left\{1,3\right\}=\left\{1,3\right\}$ ⁠. Both the subgroup $\left\{0,2\right\}$ and the quotient group $\left\{\left\{0,2\right\},\left\{1,3\right\}\right\}$ are isomorphic with ⁠ $\mathrm {Z} _{2}$ ⁠.

### Integer multiplication

Consider the multiplicative group ⁠ $G=(\mathbb {Z} _{n^{2}})^{\times }$ ⁠. The set N of ⁠ n ⁠th residues is a multiplicative subgroup isomorphic to ⁠ $(\mathbb {Z} _{n})^{\times }$ ⁠. Then N is normal in G and the factor group $G\,/\,N$ has the cosets ⁠ $N,(1+n)N,(1+n)2N,\;\ldots ,(1+n)n-1N$ ⁠. The Paillier cryptosystem is based on the conjecture that it is difficult to determine the coset of a random element of G without knowing the factorization of ⁠ n ⁠.

## Properties

The quotient group $G\,/\,G$ is isomorphic to the trivial group (the group with one element), and $G\,/\,\left\{e\right\}$ is isomorphic to ⁠ G ⁠.

The order of ⁠ $G\,/\,N$ ⁠, by definition the number of elements, is equal to ⁠ $\vert G:N\vert$ ⁠, the index of N in ⁠ G ⁠. If G is finite, the index is also equal to the order of G divided by the order of ⁠ N ⁠. The set $G\,/\,N$ may be finite, although both G and N are infinite (for example, ⁠ $\mathbb {Z} \,/\,2\mathbb {Z}$ ⁠).

There is a "natural" surjective group homomorphism ⁠ $\pi :G\rightarrow G\,/\,N$ ⁠, sending each element g of G to the coset of N to which g belongs, that is: ⁠ $\pi (g)=gN$ ⁠. The mapping $\pi$ is sometimes called the *canonical projection of G onto ⁠ $G\,/\,N$ ⁠*. Its kernel is ⁠ N ⁠.

There is a bijective correspondence between the subgroups of G that contain N and the subgroups of ⁠ $G\,/\,N$ ⁠; if H is a subgroup of G containing ⁠ N ⁠, then the corresponding subgroup of $G\,/\,N$ is ⁠ $\pi (H)$ ⁠. This correspondence holds for normal subgroups of G and $G\,/\,N$ as well, and is formalized in the lattice theorem.

Several important properties of quotient groups are recorded in the fundamental theorem on homomorphisms and the isomorphism theorems.

If G is abelian, nilpotent, solvable, cyclic or finitely generated, then so is ⁠ $G\,/\,N$ ⁠.

If H is a subgroup in a finite group ⁠ G ⁠, and the order of H is one half of the order of ⁠ G ⁠, then H is guaranteed to be a normal subgroup, so $G\,/\,H$ exists and is isomorphic to ⁠ $\mathrm {C} _{2}$ ⁠. This result can also be stated as "any subgroup of index 2 is normal", and in this form it applies also to infinite groups. Furthermore, if p is the smallest prime number dividing the order of a finite group, ⁠ G ⁠, then if $G\,/\,H$ has order ⁠ p ⁠, H must be a normal subgroup of ⁠ G ⁠.

Given G and a normal subgroup ⁠ N ⁠, then G is a group extension of $G\,/\,N$ by ⁠ N ⁠. One could ask whether this extension is trivial or split; in other words, one could ask whether G is a direct product or semidirect product of N and ⁠ $G\,/\,N$ ⁠. This is a special case of the extension problem. An example where the extension is not split is as follows: Let ⁠ $G=\mathrm {Z} _{4}=\left\{0,1,2,3\right\}$ ⁠, and ⁠ $N=\left\{0,2\right\}$ ⁠, which is isomorphic to ⁠ $\mathrm {Z} _{2}$ ⁠. Then $G\,/\,N$ is also isomorphic to ⁠ $\mathrm {Z} _{2}$ ⁠. But $\mathrm {Z} _{2}$ has only the trivial automorphism, so the only semi-direct product of N and $G\,/\,N$ is the direct product. Since $\mathrm {Z} _{4}$ is different from ⁠ $\mathrm {Z} _{2}\times \mathrm {Z} _{2}$ ⁠, we conclude that G is not a semi-direct product of N and ⁠ $G\,/\,N$ ⁠.

## Quotients of Lie groups

If G is a Lie group and N is a normal and (topologically) closed Lie subgroup of ⁠ G ⁠, the quotient $G\,/\,N$ is also a Lie group. In this case, the original group *G* has the structure of a fiber bundle (specifically, a principal ⁠ N ⁠-bundle), with base space $G\,/\,N$ and fiber ⁠ N ⁠. The dimension of $G\,/\,N$ equals ⁠ $\dim G-\dim N$ ⁠.

Note that the condition that N is closed is necessary. Indeed, if N is not closed then the quotient space is not a T1-space (since there is a coset in the quotient which cannot be separated from the identity by an open set), and thus not a Hausdorff space.

For a non-normal Lie subgroup ⁠ N ⁠, the space $G\,/\,N$ of left cosets is not a group, but simply a differentiable manifold on which G acts. The result is known as a homogeneous space.
