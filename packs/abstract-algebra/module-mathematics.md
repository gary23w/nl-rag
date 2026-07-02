---
title: "Module (mathematics)"
source: https://en.wikipedia.org/wiki/Module_(mathematics)
domain: abstract-algebra
license: CC-BY-SA-4.0
tags: abstract algebra, algebraic structure, group homomorphism, quotient structure
fetched: 2026-07-02
---

# Module (mathematics)

In mathematics, a **module** is a generalization of the notion of vector space in which the field of scalars is replaced by a (not necessarily commutative) ring. The concept of a *module* also generalizes the notion of an abelian group, since the abelian groups are exactly the modules over the ring of integers.

Like a vector space, a module is an additive abelian group, and scalar multiplication is distributive over the operations of addition between elements of the ring or module and is compatible with the ring multiplication.

Modules are very closely related to the representation theory of groups. They are also one of the central notions of commutative algebra and homological algebra, and are used widely in algebraic geometry and algebraic topology.

## Introduction and definition

### Motivation

In a vector space, the set of scalars is a field and acts on the vectors by scalar multiplication, subject to certain axioms such as the distributive law. In a module, the scalars need only be a ring, so the module concept represents a significant generalization. In commutative algebra, both ideals and quotient rings are modules, so that many arguments about ideals or quotient rings can be combined into a single argument about modules. In non-commutative algebra, the distinction between left ideals, ideals, and modules becomes more pronounced, though some ring-theoretic conditions can be expressed either about left ideals or left modules.

Much of the theory of modules consists of extending as many of the desirable properties of vector spaces as possible to the realm of modules over a "well-behaved" ring, such as a principal ideal domain. However, modules can be quite a bit more complicated than vector spaces; for instance, not all modules have a basis, and, even for those that do (free modules), the number of elements in a basis need not be the same for all bases (that is to say that they may not have a unique rank) if the underlying ring does not satisfy the invariant basis number condition, unlike vector spaces, which always have a (possibly infinite) basis whose cardinality is then unique. (These last two assertions require the axiom of choice in general, but not in the case of finite-dimensional vector spaces, or certain well-behaved infinite-dimensional vector spaces such as L*p* spaces.)

### Formal definition

Suppose that *R* is a ring, and 1 is its multiplicative identity. A **left *R*-module** *M* consists of an abelian group (*M*, +) and an operation **·** : *R* × *M* → *M* such that for all *r*, *s* in *R* and *x*, *y* in *M*, we have

$r\cdot (x+y)=r\cdot x+r\cdot y$

,

$(r+s)\cdot x=r\cdot x+s\cdot x$

,

$(rs)\cdot x=r\cdot (s\cdot x)$

,

$1\cdot x=x.$

The operation · is called *scalar multiplication*. Often the symbol · is omitted, but in this article we use it and reserve juxtaposition for multiplication in *R*. One may write *R**M* to emphasize that *M* is a left *R*-module. A **right *R*-module** *M**R* is defined similarly in terms of an operation · : *M* × *R* → *M*.

The qualificative of left- or right-module does not depend on whether the scalars are written on the left or on the right, but on the property 3: if, in the above definition, the property 3 is replaced by

$(rs)\cdot x=s\cdot (r\cdot x),$

one gets a right-module, even if the scalars are written on the left. However, writing the scalars on the left for left-modules and on the right for right modules makes the manipulation of property 3 much easier.

Authors who do not require rings to be unital omit condition 4 in the definition above; they would call the structures defined above "unital left *R*-modules". In this article, consistent with the glossary of ring theory, all rings and modules are assumed to be unital.

An (*R*,*S*)-bimodule is an abelian group together with both a left scalar multiplication · by elements of *R* and a right scalar multiplication ∗ by elements of *S*, making it simultaneously a left *R*-module and a right *S*-module, satisfying the additional condition (*r* · *x*) ∗ *s* = *r* ⋅ (*x* ∗ *s*) for all *r* in *R*, *x* in *M*, and *s* in *S*.

If *R* is commutative, then left *R*-modules are the same as right *R*-modules and are simply called *R*-modules. Most often the scalars are written on the left in this case.

## Examples

- If *K* is a field, then *K*-modules are called *K*-vector spaces (vector spaces over *K*).
- If *K* is a field, and *K*[*x*] a univariate polynomial ring, then a *K*[*x*]-module *M* is a *K*-module with an additional action of *x* on *M* by a group homomorphism that commutes with the action of *K* on *M*. In other words, a *K*[*x*]-module is a *K*-vector space *M* combined with a linear map from *M* to *M*. Applying the structure theorem for finitely generated modules over a principal ideal domain to this example shows the existence of the rational and Jordan canonical forms.
- The concept of a **Z**-module agrees with the notion of an abelian group. That is, every abelian group is a module over the ring of integers **Z** in a unique way. For *n* > 0, let *n* ⋅ *x* = *x* + *x* + ... + *x* (*n* summands), 0 ⋅ *x* = 0, and (−*n*) ⋅ *x* = −(*n* ⋅ *x*). Such a module need not have a basis—groups containing torsion elements do not. (For example, in the group of integers modulo 3, one cannot find even one element that satisfies the definition of a linearly independent set, since when an integer such as 3 or 6 multiplies an element, the result is 0. However, if a finite field is considered as a module over the same finite field taken as a ring, it is a vector space and does have a basis.)
- The decimal fractions (including negative ones) form a module over the integers. Only singletons are linearly independent sets, but there is no singleton that can serve as a basis, so the module has no basis and no rank, in the usual sense of linear algebra. However this module has a torsion-free rank equal to 1.
- If *R* is any ring and *n* a natural number, then the cartesian product *R**n* is both a left and right *R*-module over *R* if we use the component-wise operations. Hence when *n* = 1, *R* is an *R*-module, where the scalar multiplication is just ring multiplication. The case *n* = 0 yields the trivial *R*-module {0} consisting only of its identity element. Modules of this type are called free and if *R* has invariant basis number (e.g. any commutative ring or field) the number *n* is then the rank of the free module.
- If M*n*(*R*) is the ring of *n* × *n* matrices over a ring *R*, *M* is an M*n*(*R*)-module, and *e**i* is the *n* × *n* matrix with 1 in the (*i*, *i*)-entry (and zeros elsewhere), then *e**i**M* is an *R*-module, since *re**i**m* = *e**i**rm* ∈ *e**i**M*. So *M* breaks up as the direct sum of *R*-modules, *M* = *e*1*M* ⊕ ... ⊕ *e**n**M*. Conversely, given an *R*-module *M*0, then *M*0⊕*n* is an M*n*(*R*)-module. In fact, the category of *R*-modules and the category of M*n*(*R*)-modules are equivalent. The special case is that the module *M* is just *R* as a module over itself, then *R**n* is an M*n*(*R*)-module.
- If *S* is a nonempty set, *M* is a left *R*-module, and *M**S* is the collection of all functions *f* : *S* → *M*, then with addition and scalar multiplication in *M**S* defined pointwise by (*f* + *g*)(*s*) = *f*(*s*) + *g*(*s*) and (*rf*)(*s*) = *rf*(*s*), *M**S* is a left *R*-module. The right *R*-module case is analogous. In particular, if *R* is commutative then the collection of *R-module homomorphisms* *h* : *M* → *N* (see below) is an *R*-module (and in fact a *submodule* of *N**M*).
- If *X* is a smooth manifold, then the smooth functions from *X* to the real numbers form a ring *C*∞(*X*). The set of all smooth vector fields defined on *X* forms a module over *C*∞(*X*), and so do the tensor fields and the differential forms on *X*. More generally, the sections of any vector bundle form a projective module over *C*∞(*X*), and by Swan's theorem, every projective module is isomorphic to the module of sections of some vector bundle; the category of *C*∞(*X*)-modules and the category of vector bundles over *X* are equivalent.
- If *R* is any ring and *I* is any left ideal in *R*, then *I* is a left *R*-module, and analogously right ideals in *R* are right *R*-modules.
- If *R* is a ring, we can define the opposite ring *R*op, which has the same underlying set and the same addition operation, but the opposite multiplication: if *ab* = *c* in *R*, then *ba* = *c* in *R*op. Any *left* *R*-module *M* can then be seen to be a *right* module over *R*op, and any right module over *R* can be considered a left module over *R*op.
- Modules over a Lie algebra are (associative algebra) modules over its universal enveloping algebra.
- If *R* and *S* are rings with a ring homomorphism *φ* : *R* → *S*, then every *S*-module *M* is an *R*-module by defining *rm* = *φ*(*r*)*m*. In particular, *S* itself is such an *R*-module.

## Submodules and homomorphisms

Suppose *M* is a left *R*-module and *N* is a subgroup of *M*. Then *N* is a **submodule** (or more explicitly an *R*-submodule) if for any *n* in *N* and any *r* in *R*, the product *r* ⋅ *n* (or *n* ⋅ *r* for a right *R*-module) is in *N*.

If *X* is any subset of an *R*-module *M*, then the submodule spanned by *X* is defined to be ${\textstyle \langle X\rangle =\,\bigcap _{N\supseteq X}N}$ where *N* runs over the submodules of *M* that contain *X*, or explicitly ${\textstyle {\bigl \{}\!\sum _{i=1}^{k}r_{i}x_{i}\mathrel {\big |} r_{i}\in R,\,x_{i}\in X{\bigr \}}}$ , which is important in the definition of tensor products of modules.

The set of submodules of a given module *M*, together with the two binary operations + (the module spanned by the union of the arguments) and ∩, forms a lattice that satisfies the **modular law**: Given submodules *U*, *N*1, *N*2 of *M* such that *N*1 ⊆ *N*2, then the following two submodules are equal: (*N*1 + *U*) ∩ *N*2 = *N*1 + (*U* ∩ *N*2).

If *M* and *N* are left *R*-modules, then a map *f* : *M* → *N* is a **homomorphism of *R*-modules** if for any *m*, *n* in *M* and *r*, *s* in *R*,

$f(r\cdot m+s\cdot n)=r\cdot f(m)+s\cdot f(n)$

.

This, like any homomorphism of mathematical objects, is just a mapping that preserves the structure of the objects. Another name for a homomorphism of *R*-modules is an *R*-linear map.

A bijective module homomorphism *f* : *M* → *N* is called a module isomorphism, and the two modules *M* and *N* are called **isomorphic**. Two isomorphic modules are identical for all practical purposes, differing solely in the notation for their elements.

The kernel of a module homomorphism *f* : *M* → *N* is the submodule of *M* consisting of all elements that are sent to zero by *f*, and the image of *f* is the submodule of *N* consisting of values *f*(*m*) for all elements *m* of *M*. The isomorphism theorems familiar from groups and vector spaces are also valid for *R*-modules.

Given a ring *R*, the set of all left *R*-modules together with their module homomorphisms forms an abelian category, denoted by *R*-**Mod** (see category of modules).

## Types of modules

**Finitely generated**

An

R

-module

M

is

finitely generated

if there exist finitely many elements

x

1

, ...,

x

n

in

M

such that every element of

M

is a

linear combination

of those elements with coefficients from the ring

R

.

**Cyclic**

A module is called a

cyclic module

if it is generated by one element.

**Free**

A

free

R

-module

is a module that has a basis, or equivalently, one that is isomorphic to a

direct sum

of copies of the ring

R

. These are the modules that behave very much like vector spaces.

**Projective**

Projective modules

are

direct summands

of free modules and share many of their desirable properties.

**Injective**

Injective modules

are defined dually to projective modules.

**Flat**

A module is called

flat

if taking the

tensor product

of it with any

exact sequence

of

R

-modules preserves exactness.

**Torsionless**

A module is called

torsionless

if it embeds into its

algebraic dual

.

**Simple**

A

simple module

S

is a module that is not {0} and whose only submodules are {0} and

S

. Simple modules are sometimes called

irreducible

.

**Semisimple**

A

semisimple module

is a direct sum (finite or not) of simple modules. Historically these modules are also called

completely reducible

.

**Indecomposable**

An

indecomposable module

is a non-zero module that cannot be written as a

direct sum

of two non-zero submodules. Every simple module is indecomposable, but there are indecomposable modules that are not simple (e.g.

uniform modules

).

**Faithful**

A

faithful module

M

is one where the action of each

r

≠ 0

in

R

on

M

is nontrivial (i.e.

r

⋅

x

≠ 0

for some

x

in

M

). Equivalently, the

annihilator

of

M

is the

zero ideal

.

**Torsion-free**

A

torsion-free module

is a module over a ring such that 0 is the only element annihilated by a regular element (non

zero-divisor

) of the ring, equivalently

rm

= 0

implies

r

= 0

or

m

= 0

.

**Noetherian**

A

Noetherian module

is a module that satisfies the

ascending chain condition

on submodules, that is, every increasing chain of submodules becomes stationary after finitely many steps. Equivalently, every submodule is finitely generated.

**Artinian**

An

Artinian module

is a module that satisfies the

descending chain condition

on submodules, that is, every decreasing chain of submodules becomes stationary after finitely many steps.

**Graded**

A

graded module

is a module over a

graded ring

R

=

⨁

x

R

x

together with a

direct sum

decomposition

M

=

⨁

x

M

x

such that

R

x

M

y

⊆

M

x

+

y

for all

x

and

y

.

**Uniform**

A

uniform module

is a module in which all pairs of nonzero submodules have nonzero intersection.

## Further notions

### Relation to representation theory

A representation of a group *G* over a field *k* is a module over the group ring *k*[*G*].

If *M* is a left *R*-module, then the *action* of an element *r* in *R* is defined to be the map *M* → *M* that sends each *x* to *rx* (or *xr* in the case of a right module), and is necessarily a group endomorphism of the abelian group (*M*, +). The set of all group endomorphisms of *M* is denoted End**Z**(*M*) and forms a ring under addition and composition, and sending a ring element *r* of *R* to its action actually defines a ring homomorphism from *R* to End**Z**(*M*).

Such a ring homomorphism *R* → End**Z**(*M*) is called a *representation* of the abelian group *M* over the ring *R*; an alternative and equivalent way of defining left *R*-modules is to say that a left *R*-module is an abelian group *M* together with a representation of *M* over *R*. Such a representation *R* → End**Z**(*M*) may also be called a *ring action* of *R* on *M*.

A representation is called *faithful* if the map *R* → End**Z**(*M*) is injective. In terms of modules, this means that if *r* is an element of *R* such that *rx* = 0 for all *x* in *M*, then *r* = 0. Every abelian group is a faithful module over the integers or over the ring of integers modulo *n*, **Z**/*n***Z**, for some *n*.

### Generalizations

A ring *R* corresponds to a preadditive category **R** with a single object. With this understanding, a left *R*-module is just a covariant additive functor from **R** to the category of abelian groups **Ab**, and right *R*-modules are contravariant additive functors. This suggests that, if **C** is any preadditive category, a covariant additive functor from **C** to **Ab** should be considered a generalized left module over **C**. These functors form a functor category **C**-**Mod**, which is the natural generalization of the module category *R*-**Mod**.

Modules over *commutative* rings can be generalized in a different direction: take a ringed space (*X*, O*X*) and consider the sheaves of O*X*-modules (see sheaf of modules). These form a category O*X*-**Mod**, and play an important role in modern algebraic geometry. If *X* has only a single point, then this is a module category in the old sense over the commutative ring O*X*(*X*).

One can also consider modules over a semiring, called a semimodule. Modules over rings are abelian groups, but modules over semirings are only commutative monoids. Most applications of modules are still possible. In particular, for any semiring *S*, the matrices over *S* form a semiring over which the tuples of elements from *S* are a module (in this generalized sense only). This allows a further generalization of the concept of vector space incorporating the semirings from theoretical computer science.

Over near-rings, one can consider near-ring modules, a nonabelian generalization of modules.
