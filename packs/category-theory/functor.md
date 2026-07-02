---
title: "Functor"
source: https://en.wikipedia.org/wiki/Functor
domain: category-theory
license: CC-BY-SA-4.0
tags: category theory, functor, monad, morphism, natural transformation
fetched: 2026-07-02
---

# Functor

In mathematics, specifically category theory, a **functor** is a mapping between categories. Functors were first considered in algebraic topology, where algebraic objects (such as the fundamental group) are associated to topological spaces, and maps between these algebraic objects are associated to continuous maps between spaces. Nowadays, functors are used throughout modern mathematics to relate various categories. Thus, functors are important in every area of mathematics where category theory is applied.

The words *category* and *functor* were borrowed by mathematicians from the philosophers Aristotle and Rudolf Carnap, respectively. The latter used *functor* in a linguistic context; see function word.

## Definition

Let *C* and *D* be categories. A **functor** *F* from *C* to *D* is a mapping that:

- associates each object X in *C* to an object $F(X)$ in *D*,
- associates each morphism $f\colon X\to Y$ in *C* to a morphism $F(f)\colon F(X)\to F(Y)$ in *D* such that the following two conditions hold:
  - $F(\mathrm {id} _{X})=\mathrm {id} _{F(X)}\,\!$ for every object X in *C*,
  - $F(g\circ f)=F(g)\circ F(f)$ for all morphisms $f\colon X\to Y\,\!$ and $g\colon Y\to Z$ in *C*.

That is, functors must preserve identity morphisms and composition of morphisms.

### Covariance and contravariance

There are many constructions in mathematics that would be functors but for the fact that they "turn morphisms around" and "reverse composition". We then define a **contravariant functor** *F* from *C* to *D* as a mapping that

- associates each object X in *C* with an object $F(X)$ in *D*,
- associates each morphism $f\colon X\to Y$ in *C* with a morphism $F(f)\colon F(Y)\to F(X)$ in *D* such that the following two conditions hold:
  - $F(\mathrm {id} _{X})=\mathrm {id} _{F(X)}\,\!$ for every object X in *C*,
  - $F(g\circ f)=F(f)\circ F(g)$ for all morphisms $f\colon X\to Y$ and $g\colon Y\to Z$ in *C*.

Variance of functor (composite)

- The composite of two functors of the same variance:
  - $\mathrm {Covariant} \circ \mathrm {Covariant} \to \mathrm {Covariant}$
  - $\mathrm {Contravariant} \circ \mathrm {Contravariant} \to \mathrm {Covariant}$
- The composite of two functors of opposite variance:
  - $\mathrm {Covariant} \circ \mathrm {Contravariant} \to \mathrm {Contravariant}$
  - $\mathrm {Contravariant} \circ \mathrm {Covariant} \to \mathrm {Contravariant}$

Note that contravariant functors reverse the direction of composition.

Ordinary functors are also called **covariant functors** in order to distinguish them from contravariant ones. Note that one can also define a contravariant functor as a *covariant* functor on the opposite category $C^{\mathrm {op} }$ . Some authors prefer to write all expressions covariantly. That is, instead of saying $F\colon C\to D$ is a contravariant functor, they simply write $F\colon C^{\mathrm {op} }\to D$ (or sometimes $F\colon C\to D^{\mathrm {op} }$ ) and call it a functor.

Contravariant functors are also occasionally called *cofunctors*.

There is a convention which refers to "vectors"—i.e., vector fields, elements of the space of sections $\Gamma (TM)$ of a tangent bundle $TM$ —as "contravariant" and to "covectors"—i.e., 1-forms, elements of the space of sections $\Gamma {\mathord {\left(T^{*}M\right)}}$ of a cotangent bundle $T^{*}M$ —as "covariant". This terminology originates in physics, and its rationale has to do with the position of the indices ("upstairs" and "downstairs") in expressions such as ${x'}^{\,i}=\Lambda _{j}^{i}x^{j}$ for $\mathbf {x} '={\boldsymbol {\Lambda }}\mathbf {x}$ or $\omega '_{i}=\Lambda _{i}^{j}\omega _{j}$ for ${\boldsymbol {\omega }}'={\boldsymbol {\omega }}{\boldsymbol {\Lambda }}^{\textsf {T}}.$ In this formalism it is observed that the coordinate transformation symbol $\Lambda _{i}^{j}$ (representing the matrix ${\boldsymbol {\Lambda }}^{\textsf {T}}$ ) acts on the "covector coordinates" "in the same way" as on the basis vectors: $\mathbf {e} _{i}=\Lambda _{i}^{j}\mathbf {e} _{j}$ —whereas it acts "in the opposite way" on the "vector coordinates" (but "in the same way" as on the basis covectors: $\mathbf {e} ^{i}=\Lambda _{j}^{i}\mathbf {e} ^{j}$ ). This terminology is contrary to the one used in category theory because it is the covectors that have *pullbacks* in general and are thus *contravariant*, whereas vectors in general are *covariant* since they can be *pushed forward*. See also Covariance and contravariance of vectors.

### Opposite functor

Every functor $F\colon C\to D$ induces the **opposite functor** $F^{\mathrm {op} }\colon C^{\mathrm {op} }\to D^{\mathrm {op} }$ , where $C^{\mathrm {op} }$ and $D^{\mathrm {op} }$ are the opposite categories to C and D . By definition, $F^{\mathrm {op} }$ maps objects and morphisms in the identical way as does F . Since $C^{\mathrm {op} }$ does not coincide with C as a category, and similarly for D , $F^{\mathrm {op} }$ is distinguished from F . For example, when composing $F\colon C_{0}\to C_{1}$ with $G\colon C_{1}^{\mathrm {op} }\to C_{2}$ , one should use either $G\circ F^{\mathrm {op} }$ or $G^{\mathrm {op} }\circ F$ . Note that, following the property of opposite category, $\left(F^{\mathrm {op} }\right)^{\mathrm {op} }=F$ .

### Bifunctors and multifunctors

A **bifunctor** (also known as a **binary functor**) is a functor whose domain is a product category. For example, the Hom functor is of the type *Cop* × *C* → **Set**. It can be seen as a functor in *two* arguments; it is contravariant in one argument, covariant in the other.

A **multifunctor** is a generalization of the functor concept to *n* variables. So, for example, a bifunctor is a multifunctor with *n* = 2.

## Properties

Two important consequences of the functor axioms are:

- *F* transforms each commutative diagram in *C* into a commutative diagram in *D*;
- if *f* is an isomorphism in *C*, then *F*(*f*) is an isomorphism in *D*.

One can compose functors, i.e. if *F* is a functor from *A* to *B* and *G* is a functor from *B* to *C* then one can form the composite functor *G* ∘ *F* from *A* to *C*. Composition of functors is associative where defined. Identity of composition of functors is the identity functor. This shows that functors can be considered as morphisms in categories of categories, for example in the category of small categories.

A small category with a single object is the same thing as a monoid: the morphisms of a one-object category can be thought of as elements of the monoid, and composition in the category is thought of as the monoid operation. Functors between one-object categories correspond to monoid homomorphisms. So in a sense, functors between arbitrary categories are a kind of generalization of monoid homomorphisms to categories with more than one object.

## Examples

**Diagram**

For categories

C

and

J

, a diagram of type

J

in

C

is a covariant functor

$D\colon J\to C$

.

**(Category theoretical) presheaf**

For categories

C

and

J

, a

J

-presheaf on

C

is a contravariant functor

$D\colon C\to J$

.

In the special case when

J

is

Set

, the category of sets and functions,

D

is called a

presheaf

on

C

.

**Presheaves (over a topological space)**

If

X

is a

topological space

, then the

open sets

in

X

form a

partially ordered set

Open(

X

) under inclusion. Like every partially ordered set, Open(

X

) forms a small category by adding a single arrow

U

→

V

if and only if

$U\subseteq V$

. Contravariant functors on Open(

X

) are called

presheaves

on

X

. For instance, by assigning to every open set

U

the

associative algebra

of real-valued continuous functions on

U

, one obtains a presheaf of algebras on

X

.

**Constant functor**

The functor

C

→

D

which maps every object of

C

to a fixed object

X

in

D

and every morphism in

C

to the identity morphism on

X

. Such a functor is called a

constant

or

selection

functor.

***Endofunctor***

A functor that maps a category to that same category; e.g.,

polynomial functor

.

***Identity functor***

In category

C

, written 1

C

or id

C

, maps an object to itself and a morphism to itself. The identity functor is an endofunctor.

**Diagonal functor**

The

diagonal functor

is defined as the functor from

D

to the functor category

D

C

which sends each object in

D

to the constant functor at that object.

**Limit functor**

For a fixed

index category

J

, if every functor

J

→

C

has a

limit

(for instance if

C

is complete), then the limit functor

C

J

→

C

assigns to each functor its limit. The existence of this functor can be proved by realizing that it is the

right-adjoint

to the

diagonal functor

and invoking the

Freyd adjoint functor theorem

. This requires a suitable version of the

axiom of choice

. Similar remarks apply to the colimit functor (which assigns to every functor its colimit, and is covariant).

**Power sets functor**

The power set functor

P

:

Set

→

Set

maps each set to its

power set

and each function

$f\colon X\to Y$

to the map which sends

$U\in {\mathcal {P}}(X)$

to its image

$f(U)\in {\mathcal {P}}(Y)$

. One can also consider the

contravariant power set functor

which sends

$f\colon X\to Y$

to the map which sends

$V\subseteq Y$

to its

inverse image

$f^{-1}(V)\subseteq X.$

For example, if

$X=\{0,1\}$

then

$F(X)={\mathcal {P}}(X)=\{\{\},\{0\},\{1\},X\}$

. Suppose

$f(0)=\{\}$

and

$f(1)=X$

. Then

$F(f)$

is the function which sends any subset

U

of

X

to its image

$f(U)$

, which in this case means

$\{\}\mapsto f(\{\})=\{\}$

, where

$\mapsto$

denotes the mapping under

$F(f)$

, so this could also be written as

$(F(f))(\{\})=\{\}$

. For the other values,

$\{0\}\mapsto f(\{0\})=\{f(0)\}=\{\{\}\},\$

$\{1\}\mapsto f(\{1\})=\{f(1)\}=\{X\},\$

$\{0,1\}\mapsto f(\{0,1\})=\{f(0),f(1)\}=\{\{\},X\}.$

Note that

$f(\{0,1\})$

consequently generates the

trivial topology

on

X

. Also note that although the function

f

in this example mapped to the power set of

X

, that need not be the case in general.

**Dual vector space**

The map which assigns to every

vector space

its

dual space

and to every

linear map

its dual or transpose is a contravariant functor from the category of all vector spaces over a fixed

field

to itself.

**Fundamental group**

Consider the category of

pointed topological spaces

, i.e. topological spaces with distinguished points. The objects are pairs

(

X

,

x

0

)

, where

X

is a topological space and

x

0

is a point in

X

. A morphism from

(

X

,

x

0

)

to

(

Y

,

y

0

)

is given by a

continuous

map

f

:

X

→

Y

with

f

(

x

0

) =

y

0

.

To every topological space

X

with distinguished point

x

0

, one can define the

fundamental group

based at

x

0

, denoted

π

1

(

X

,

x

0

)

. This is the

group

of

homotopy

classes of loops based at

x

0

, with the group operation of concatenation. If

f

:

X

→

Y

is a morphism of

pointed spaces

, then every loop in

X

with base point

x

0

can be composed with

f

to yield a loop in

Y

with base point

y

0

. This operation is compatible with the homotopy

equivalence relation

and the composition of loops, and we get a

group homomorphism

from

π(

X

,

x

0

)

to

π(

Y

,

y

0

)

. We thus obtain a functor from the category of pointed topological spaces to the

category of groups

.

In the category of topological spaces (without distinguished point), one considers homotopy classes of generic curves, but they cannot be composed unless they share an endpoint. Thus one has the

fundamental

groupoid

instead of the fundamental group, and this construction is functorial.

**Algebra of continuous functions**

A contravariant functor from the category of

topological spaces

(with continuous maps as morphisms) to the category of real

associative algebras

is given by assigning to every topological space

X

the algebra C(

X

) of all real-valued continuous functions on that space. Every continuous map

f

:

X

→

Y

induces an

algebra homomorphism

C(

f

) : C(

Y

) → C(

X

)

by the rule

C(

f

)(

φ

) =

φ

∘

f

for every

φ

in C(

Y

).

**Tangent and cotangent bundles**

The map which sends every

differentiable manifold

to its

tangent bundle

and every

smooth map

to its

derivative

is a covariant functor from the category of differentiable manifolds to the category of

vector bundles

.

Doing this constructions pointwise gives the

tangent space

, a covariant functor from the category of pointed differentiable manifolds to the category of real vector spaces. Likewise,

cotangent space

is a contravariant functor, essentially the composition of the tangent space with the

dual space

above.

**Group actions/representations**

Every

group

G

can be considered as a category with a single object whose morphisms are the elements of

G

. A functor from

G

to

Set

is then nothing but a

group action

of

G

on a particular set, i.e. a

G

-set. Likewise, a functor from

G

to the

category of vector spaces

,

Vect

K

, is a

linear representation

of

G

. In general, a functor

G

→

C

can be considered as an "action" of

G

on an object in the category

C

. If

C

is a group, then this action is a group homomorphism.

**Lie algebras**

Assigning to every real (complex)

Lie group

its real (complex)

Lie algebra

defines a functor.

**Tensor products**

If

C

denotes the category of vector spaces over a fixed field, with

linear maps

as morphisms, then the

tensor product

$V\otimes W$

defines a functor

C

×

C

→

C

which is covariant in both arguments.

**Forgetful functors**

The functor

U

:

Grp

→

Set

which maps a

group

to its underlying set and a

group homomorphism

to its underlying function of sets is a functor.

Functors like these, which "forget" some structure, are termed

forgetful functors

. Another example is the functor

Rng

→

Ab

which maps a

ring

to its underlying additive

abelian group

. Morphisms in

Rng

(

ring homomorphisms

) become morphisms in

Ab

(abelian group homomorphisms).

**Free functors**

Going in the opposite direction of forgetful functors are free functors. The free functor

F

:

Set

→

Grp

sends every set

X

to the

free group

generated by

X

. Functions get mapped to group homomorphisms between free groups. Free constructions exist for many categories based on structured sets. See

free object

.

**Homomorphism groups**

To every pair

A

,

B

of

abelian groups

one can assign the abelian group Hom(

A

,

B

) consisting of all

group homomorphisms

from

A

to

B

. This is a functor which is contravariant in the first and covariant in the second argument, i.e. it is a functor

Ab

op

×

Ab

→

Ab

(where

Ab

denotes the

category of abelian groups

with group homomorphisms). If

f

:

A

1

→

A

2

and

g

:

B

1

→

B

2

are morphisms in

Ab

, then the group homomorphism

Hom(

f

,

g

)

:

Hom(

A

2

,

B

1

) → Hom(

A

1

,

B

2

)

is given by

φ

↦

g

∘

φ

∘

f

. See

Hom functor

.

**Representable functors**

We can generalize the previous example to any category

C

. To every pair

X

,

Y

of objects in

C

one can assign the set

Hom(

X

,

Y

)

of morphisms from

X

to

Y

. This defines a functor to

Set

which is contravariant in the first argument and covariant in the second, i.e. it is a functor

C

op

×

C

→

Set

. If

f

:

X

1

→

X

2

and

g

:

Y

1

→

Y

2

are morphisms in

C

, then the map

Hom(

f

,

g

) : Hom(

X

2

,

Y

1

) → Hom(

X

1

,

Y

2

)

is given by

φ

↦

g

∘

φ

∘

f

.

Functors like these are called

representable functors

. An important goal in many settings is to determine whether a given functor is representable.

## Relation to other categorical concepts

Let *C* and *D* be categories. The collection of all functors from *C* to *D* forms the objects of a category: the functor category. Morphisms in this category are natural transformations between functors.

Functors are often defined by universal properties; examples are the tensor product, the direct sum and direct product of groups or vector spaces, construction of free groups and modules, direct and inverse limits. The concepts of limit and colimit generalize several of the above.

Universal constructions often give rise to pairs of adjoint functors.

## Computer implementations

Functors sometimes appear in functional programming. For instance, the programming language Haskell has a class `Functor` where `fmap` is a polytypic function used to map functions (*morphisms* on *Hask*, the category of Haskell types) between existing types to functions between some new types.
