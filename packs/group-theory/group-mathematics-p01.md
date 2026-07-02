---
title: "Group (mathematics) (part 1/2)"
source: https://en.wikipedia.org/wiki/Group_(mathematics)
domain: group-theory
license: CC-BY-SA-4.0
tags: group theory, abstract algebra, symmetry group, abelian group
fetched: 2026-07-02
part: 1/2
---

# Group (mathematics)

In mathematics, a **group** is a set with an operation that combines any two elements of the set to produce a third element within the same set and the following conditions must hold: the operation is associative, it has an identity element, and every element of the set has an inverse element. For example, the integers with the addition operation form a group.

The concept of a group was elaborated for handling, in a unified way, many mathematical structures such as numbers, geometric shapes and polynomial roots. Because the concept of groups is ubiquitous in numerous areas both within and outside mathematics, some authors consider it as a central organizing principle of contemporary mathematics.

In geometry, groups arise naturally in the study of symmetries and geometric transformations: the symmetries of an object form a group, called the symmetry group of the object, and the transformations of a given type form a general group. Lie groups appear in symmetry groups in geometry, and also in the Standard Model of particle physics. The Poincaré group is a Lie group consisting of the symmetries of spacetime in special relativity. Point groups describe symmetry in molecular chemistry.

The concept of a group arose in the study of polynomial equations. Évariste Galois, in the 1830s, introduced the term *group* (French: *groupe*) for the symmetry group of the roots of an equation, now called a Galois group. After contributions from other fields such as number theory and geometry, the group notion was generalized and firmly established around 1870. Modern group theory—an active mathematical discipline—studies groups in their own right. To explore groups, mathematicians have devised various notions to break groups into smaller, better-understandable pieces, such as subgroups, quotient groups and simple groups. In addition to their abstract properties, group theorists also study the different ways in which a group can be expressed concretely, both from a point of view of representation theory (that is, through the representations of the group) and of computational group theory. A theory has been developed for finite groups, which culminated with the classification of finite simple groups, completed in 2004. Since the mid-1980s, geometric group theory, which studies finitely generated groups as geometric objects, has become an active area in group theory.


## Definition and illustration

### First example: the integers

One of the more familiar groups is the set of integers $\mathbb {Z} =\{\ldots ,-4,-3,-2,-1,0,1,2,3,4,\ldots \}$ together with addition. For any two integers a and ⁠ b ⁠, the sum $a+b$ is also an integer; this *closure* property says that + is a binary operation on ⁠ $\mathbb {Z}$ ⁠. The following properties of integer addition serve as a model for the group axioms in the definition below.

- For all integers ⁠ a ⁠, b and ⁠ c ⁠, one has ⁠ $(a+b)+c=a+(b+c)$ ⁠. Expressed in words, adding a to b first, and then adding the result to c gives the same final result as adding a to the sum of b and ⁠ c ⁠. This property is known as *associativity*.
- If a is any integer, then $0+a=a$ and ⁠ $a+0=a$ ⁠. Zero is called the *identity element* of addition because adding it to any integer returns the same integer.
- For every integer ⁠ a ⁠, there is an integer b such that $a+b=0$ and ⁠ $b+a=0$ ⁠. The integer b is called the *inverse element* of the integer a and is denoted ⁠ $-a$ ⁠.

The integers, together with the operation ⁠ + ⁠, form a mathematical object belonging to a broad class sharing similar structural aspects. To appropriately understand these structures as a collective, the following definition is developed.

### Definition

A group is a set G together with a binary operation on ⁠ G ⁠, here denoted "⁠ $\cdot$ ⁠", that combines any two elements a and b of G to form an element of ⁠ G ⁠, denoted ⁠ $a\cdot b$ ⁠, such that the following three requirements, known as **group axioms**, are satisfied:

**Associativity**

For all

⁠

a

⁠

,

⁠

b

⁠

,

⁠

c

⁠

in

⁠

G

⁠

, one has

⁠

$(a\cdot b)\cdot c=a\cdot (b\cdot c)$

⁠

.

**Identity element**

There exists an element

e

in

G

such that, for every

a

in

⁠

G

⁠

, one has

⁠

$e\cdot a=a$

⁠

and

⁠

$a\cdot e=a$

⁠

.

Such an element

e

is unique. It is called the

identity element

(or sometimes

neutral element

) of the group.

**Inverse element**

For each

a

in

⁠

G

⁠

, there exists an element

b

in

G

such that

$a\cdot b=e$

and

⁠

$b\cdot a=e$

⁠

, where

e

is the identity element.

For each

⁠

a

⁠

, the element

b

is unique; it is called

the inverse

of

a

and is commonly denoted

⁠

$a^{-1}$

⁠

.

Note: Uniqueness of the identity and uniqueness of inverse elements are not part of the axioms; they are *consequences* of the three axioms.

### Notation and terminology

Formally, a group is an ordered pair of a set and a binary operation on this set that satisfies the group axioms. The set is called the *underlying set* of the group, and the operation is called the *group operation* or the *group law*.

A group and its underlying set are thus two different mathematical objects. To avoid cumbersome notation, it is common to abuse notation by using the same symbol to denote both. This reflects also an informal way of thinking: that the group is the same as the set except that it has been enriched by additional structure provided by the operation.

For example, consider the set of real numbers ⁠ $\mathbb {R}$ ⁠, which has the operations of addition $a+b$ and multiplication ⁠ $ab$ ⁠. Formally, $\mathbb {R}$ is a set, $(\mathbb {R} ,+)$ is a group, and $(\mathbb {R} ,+,\cdot )$ is a field. But it is common to write $\mathbb {R}$ to denote any of these three objects.

The *additive group* of the field $\mathbb {R}$ is the group whose underlying set is $\mathbb {R}$ and whose operation is addition. The *multiplicative group* of the field $\mathbb {R}$ is the group $\mathbb {R} ^{\times }$ whose underlying set is the set of nonzero real numbers $\mathbb {R} \smallsetminus \{0\}$ and whose operation is multiplication.

More generally, one speaks of an *additive group* whenever the group operation is notated as addition; in this case, the identity is typically denoted ⁠ 0 ⁠, and the inverse of an element x is denoted ⁠ $-x$ ⁠. Similarly, one speaks of a *multiplicative group* whenever the group operation is notated as multiplication; in this case, the identity is typically denoted ⁠ 1 ⁠, and the inverse of an element x is denoted ⁠ $x^{-1}$ ⁠. In a multiplicative group, the operation symbol is usually omitted entirely, so that the operation is denoted by juxtaposition, $ab$ instead of ⁠ $a\cdot b$ ⁠.

The definition of a group does not require that $a\cdot b=b\cdot a$ for all elements a and b in ⁠ G ⁠. If this additional condition holds, then the operation is said to be commutative, and the group is called an abelian group. It is a common convention that for an abelian group either additive or multiplicative notation may be used, but for a nonabelian group only multiplicative notation is used.

Several other notations are commonly used for groups whose elements are not numbers. For a group whose elements are functions, the operation is often function composition ⁠ $f\circ g$ ⁠; then the identity may be denoted id. In the more specific cases of geometric transformation groups, symmetry groups, permutation groups, and automorphism groups, the symbol $\circ$ is often omitted, as for multiplicative groups. Many other variants of notation may be encountered.

### Second example: a symmetry group

The elements of the symmetry group of the square,

⁠

$\mathrm {D} _{4}$

⁠

. Vertices are identified by color or number.

$\mathrm {id}$

(keeping it as it is)

$r_{1}$

(rotation by 90° clockwise)

$r_{2}$

(rotation by 180°)

$r_{3}$

(rotation by 270° clockwise)

$f_{\mathrm {v} }$

(vertical reflection)

$f_{\mathrm {h} }$

(horizontal reflection)

$f_{\mathrm {d} }$

(diagonal reflection)

$f_{\mathrm {c} }$

(counter-diagonal reflection)

Two figures in the plane are congruent if one can be changed into the other using a combination of rotations, reflections, and translations. Any figure is congruent to itself. However, some figures are congruent to themselves in more than one way, and these extra congruences are called symmetries. A square has eight symmetries. These are:

- the identity operation leaving everything unchanged, denoted $\operatorname {id}$ ;
- rotations of the square around its center by 90°, 180°, and 270° clockwise, denoted by ⁠ $r_{1}$ ⁠, $r_{2}$ and ⁠ $r_{3}$ ⁠, respectively;
- reflections about the horizontal and vertical middle line (⁠ $f_{\mathrm {v} }$ ⁠ and ⁠ $f_{\mathrm {h} }$ ⁠), or through the two diagonals (⁠ $f_{\mathrm {d} }$ ⁠ and ⁠ $f_{\mathrm {c} }$ ⁠).

These symmetries are functions. Each sends a point in the square to the corresponding point under the symmetry. For example, $r_{1}$ sends a point to its rotation 90° clockwise around the square's center, and $f_{\mathrm {h} }$ sends a point to its reflection across the square's vertical middle line. Composing two of these symmetries gives another symmetry. These symmetries determine a group called the dihedral group of degree four, denoted ⁠ $\mathrm {D} _{4}$ ⁠. The underlying set of the group is the above set of symmetries, and the group operation is function composition. Two symmetries are combined by composing them as functions, that is, applying the first one to the square, and the second one to the result of the first application. The result of performing first a and then b is written symbolically *from right to left* as $b\circ a$ ("apply the symmetry b after performing the symmetry ⁠ a ⁠"). This is the usual notation for the composition of functions.

A Cayley table lists the results of all such compositions possible. For example, rotating by 270° clockwise (⁠ $r_{3}$ ⁠) and then reflecting horizontally (⁠ $f_{\mathrm {h} }$ ⁠) is the same as performing a reflection along the diagonal (⁠ $f_{\mathrm {d} }$ ⁠). Using the above symbols, highlighted in blue in the Cayley table: $f_{\mathrm {h} }\circ r_{3}=f_{\mathrm {d} }.$

Cayley table

of

$\mathrm {D} _{4}$

$\circ$

$\mathrm {id}$

$r_{1}$

$r_{2}$

$r_{3}$

$f_{\mathrm {v} }$

$f_{\mathrm {h} }$

$f_{\mathrm {d} }$

$f_{\mathrm {c} }$

$\mathrm {id}$

$\mathrm {id}$

$r_{1}$

$r_{2}$

$r_{3}$

$f_{\mathrm {v} }$

$f_{\mathrm {h} }$

$f_{\mathrm {d} }$

$f_{\mathrm {c} }$

$r_{1}$

$r_{1}$

$r_{2}$

$r_{3}$

$\mathrm {id}$

$f_{\mathrm {c} }$

$f_{\mathrm {d} }$

$f_{\mathrm {v} }$

$f_{\mathrm {h} }$

$r_{2}$

$r_{2}$

$r_{3}$

$\mathrm {id}$

$r_{1}$

$f_{\mathrm {h} }$

$f_{\mathrm {v} }$

$f_{\mathrm {c} }$

$f_{\mathrm {d} }$

$r_{3}$

$r_{3}$

$\mathrm {id}$

$r_{1}$

$r_{2}$

$f_{\mathrm {d} }$

$f_{\mathrm {c} }$

$f_{\mathrm {h} }$

$f_{\mathrm {v} }$

$f_{\mathrm {v} }$

$f_{\mathrm {v} }$

$f_{\mathrm {d} }$

$f_{\mathrm {h} }$

$f_{\mathrm {c} }$

$\mathrm {id}$

$r_{2}$

$r_{1}$

$r_{3}$

$f_{\mathrm {h} }$

$f_{\mathrm {h} }$

$f_{\mathrm {c} }$

$f_{\mathrm {v} }$

$f_{\mathrm {d} }$

$r_{2}$

$\mathrm {id}$

$r_{3}$

$r_{1}$

$f_{\mathrm {d} }$

$f_{\mathrm {d} }$

$f_{\mathrm {h} }$

$f_{\mathrm {c} }$

$f_{\mathrm {v} }$

$r_{3}$

$r_{1}$

$\mathrm {id}$

$r_{2}$

$f_{\mathrm {c} }$

$f_{\mathrm {c} }$

$f_{\mathrm {v} }$

$f_{\mathrm {d} }$

$f_{\mathrm {h} }$

$r_{1}$

$r_{3}$

$r_{2}$

$\mathrm {id}$

The elements

⁠

$\mathrm {id}$

⁠

,

⁠

$r_{1}$

⁠

,

⁠

$r_{2}$

⁠

, and

⁠

$r_{3}$

⁠

form a

subgroup

whose Cayley table is highlighted in

red (upper left region). A left and right

coset

of this subgroup are highlighted in

green (in the last row) and

yellow (last column), respectively. The result of the composition

⁠

$f_{\mathrm {h} }\circ r_{3}$

⁠

, the symmetry

⁠

$f_{\mathrm {d} }$

⁠

, is highlighted in

blue (below table center).

Given this set of symmetries and the described operation, the group axioms can be understood as follows:

- *Binary operation*: Composition is a binary operation. That is, $a\circ b$ is a symmetry for any two symmetries a and ⁠ b ⁠. For example, $r_{3}\circ f_{\mathrm {h} }=f_{\mathrm {c} }.$ That is, rotating 270° clockwise after reflecting horizontally equals reflecting along the counter-diagonal (⁠ $f_{\mathrm {c} }$ ⁠). Indeed, every other combination of two symmetries still gives a symmetry, as can be checked using the Cayley table.
- *Associativity*: The associativity axiom deals with composing more than two symmetries: Starting with three elements ⁠ a ⁠, ⁠ b ⁠ and ⁠ c ⁠ of ⁠ $\mathrm {D} _{4}$ ⁠, there are two possible ways of using these three symmetries in this order to determine a symmetry of the square. One of these ways is to first compose a and b into a single symmetry, then to compose that symmetry with ⁠ c ⁠. The other way is to first compose b and ⁠ c ⁠, then to compose the resulting symmetry with ⁠ a ⁠. These two ways must always give the same result, that is, $(a\circ b)\circ c=a\circ (b\circ c).$ For example, $(f_{\mathrm {d} }\circ f_{\mathrm {v} })\circ r_{2}=f_{\mathrm {d} }\circ (f_{\mathrm {v} }\circ r_{2})$ can be checked using the Cayley table: ${\begin{aligned}(f_{\mathrm {d} }\circ f_{\mathrm {v} })\circ r_{2}&=r_{3}\circ r_{2}=r_{1}\\f_{\mathrm {d} }\circ (f_{\mathrm {v} }\circ r_{2})&=f_{\mathrm {d} }\circ f_{\mathrm {h} }=r_{1}.\end{aligned}}$
- *Identity element*: The identity element is ⁠ $\mathrm {id}$ ⁠, as it does not change any symmetry a when composed with it either on the left or on the right.
- *Inverse element*: Each symmetry has an inverse: ⁠ $\mathrm {id}$ ⁠, the reflections ⁠ $f_{\mathrm {h} }$ ⁠, ⁠ $f_{\mathrm {v} }$ ⁠, ⁠ $f_{\mathrm {d} }$ ⁠, ⁠ $f_{\mathrm {c} }$ ⁠ and the 180° rotation $r_{2}$ are their own inverse, because performing them twice brings the square back to its original orientation. The rotations $r_{3}$ and $r_{1}$ are each other's inverses, because rotating 90° and then rotating 270° (or vice versa) yields a rotation over 360° which leaves the square unchanged. This is easily verified in the table.

In contrast to the group of integers above, where the order of the operation is immaterial, it does matter in ⁠ $\mathrm {D} _{4}$ ⁠, as, for example, $f_{\mathrm {h} }\circ r_{1}=f_{\mathrm {c} }$ but ⁠ $r_{1}\circ f_{\mathrm {h} }=f_{\mathrm {d} }$ ⁠. In other words, $\mathrm {D} _{4}$ is not abelian.


## History

The modern concept of an abstract group developed out of several fields of mathematics. The original motivation for group theory was the quest for solutions of polynomial equations of degree higher than 4. The 19th-century French mathematician Évariste Galois, extending prior work of Paolo Ruffini and Joseph-Louis Lagrange, gave a criterion for the solvability of a particular polynomial equation in terms of the symmetry group of its roots (solutions). The elements of such a Galois group correspond to certain permutations of the roots. At first, Galois's ideas were rejected by his contemporaries, and published only posthumously. More general permutation groups were investigated in particular by Augustin Louis Cauchy. Arthur Cayley's *On the theory of groups, as depending on the symbolic equation $\theta ^{n}=1$* (1854) gives the first abstract definition of a finite group.

Geometry was a second field in which groups were used systematically, especially symmetry groups as part of Felix Klein's 1872 Erlangen program. After novel geometries such as hyperbolic and projective geometry had emerged, Klein used group theory to organize them in a more coherent way. Further advancing these ideas, Sophus Lie founded the study of Lie groups in 1884.

The third field contributing to group theory was number theory. Certain abelian group structures had been used implicitly in Carl Friedrich Gauss's number-theoretical work *Disquisitiones Arithmeticae* (1798), and more explicitly by Leopold Kronecker. In 1847, Ernst Kummer made early attempts to prove Fermat's Last Theorem by developing groups describing factorization into prime numbers.

The convergence of these various sources into a uniform theory of groups started with Jordan (1870)'s *Traité des substitutions et des équations algébriques*. von Dyck (1882) introduced the idea of specifying a group by means of generators and relations, and was also the first to give an axiomatic definition of an "abstract group", in the terminology of the time. As of the 20th century, groups gained wide recognition by the pioneering work of Ferdinand Georg Frobenius and William Burnside, who worked on representation theory of finite groups and wrote the first book about group theory in the English language: *Theory of Groups of Finite Order*, Richard Brauer's modular representation theory and Issai Schur's papers. The theory of Lie groups, and more generally locally compact groups was studied by Hermann Weyl, Élie Cartan and many others. Its algebraic counterpart, the theory of algebraic groups, was first shaped by Claude Chevalley (from the late 1930s) and later by the work of Armand Borel and Jacques Tits.

The University of Chicago's 1960–61 Group Theory Year brought together group theorists such as Daniel Gorenstein, John G. Thompson and Walter Feit, laying the foundation of a collaboration that, with input from numerous other mathematicians, led to the classification of finite simple groups, with the final step taken by Aschbacher and Smith in 2004. This project exceeded previous mathematical endeavours by its sheer size, in both length of proof and number of researchers. Research concerning this classification proof is ongoing. Group theory remains a highly active mathematical branch, impacting many other fields, as the examples below illustrate.


## Elementary consequences of the group axioms

Basic facts about all groups that can be obtained directly from the group axioms are commonly subsumed under *elementary group theory*. For example, repeated applications of the associativity axiom show that the unambiguity of $a\cdot b\cdot c=(a\cdot b)\cdot c=a\cdot (b\cdot c)$ generalizes to more than three factors (for example, $a\cdot b\cdot c\cdot d$ is also unambiguous). Because this implies that parentheses can be inserted anywhere within such a series of terms, parentheses are usually omitted.

### Uniqueness of identity element

The group axioms imply that the identity element is unique; that is, there exists only one identity element: any two identity elements e and f of a group are equal, because the group axioms imply ⁠ $e=e\cdot f=f$ ⁠. It is thus customary to speak of *the* identity element of the group.

### Uniqueness of inverses

The group axioms also imply that the inverse of each element is unique. Let a group element a have both b and c as inverses. Then

${\begin{aligned}b&=b\cdot e&&{\text{(}}e{\text{ is the identity element)}}\\&=b\cdot (a\cdot c)&&{\text{(}}c{\text{ and }}a{\text{ are inverses of each other)}}\\&=(b\cdot a)\cdot c&&{\text{(associativity)}}\\&=e\cdot c&&{\text{(}}b{\text{ is an inverse of }}a{\text{)}}\\&=c&&{\text{(}}e{\text{ is the identity element and }}b=c{\text{)}}\end{aligned}}$

Therefore, it is customary to speak of *the* inverse of an element.

### Division

Given elements a and b of a group G , there is a unique solution x in G to the equation $a\cdot x=b$ , namely $a^{-1}\cdot b$ . It follows that for each a in G , the function $G\to G$ that maps each x to $a\cdot x$ is a bijection; it is called *left multiplication* by a or *left translation* by a .

Similarly, given a and b in G , the unique solution x to $x\cdot a=b$ is $b\cdot a^{-1}$ . For each a , the function $G\to G$ that maps each x to $x\cdot a$ is a bijection called *right multiplication* by a or *right translation* by a .

### Equivalent definition with relaxed axioms

The group axioms for identity and inverses may be "weakened" to assert only the existence of a left identity and left inverses. From these *one-sided axioms*, one can prove that the left identity is also a right identity and a left inverse is also a right inverse for the same element. Since they define exactly the same structures as groups, collectively the axioms are not weaker.

In particular, assuming associativity and the existence of a left identity e (that is, ⁠ $e\cdot f=f$ ⁠) and a left inverse $f^{-1}$ for each element f (that is, ⁠ $f^{-1}\cdot f=e$ ⁠), it follows that every left inverse is also a right inverse of the same element as follows. Indeed, one has

${\begin{aligned}f\cdot f^{-1}&=e\cdot (f\cdot f^{-1})&&{\text{(left identity)}}\\&=((f^{-1})^{-1}\cdot f^{-1})\cdot (f\cdot f^{-1})&&{\text{(left inverse)}}\\&=(f^{-1})^{-1}\cdot ((f^{-1}\cdot f)\cdot f^{-1})&&{\text{(associativity)}}\\&=(f^{-1})^{-1}\cdot (e\cdot f^{-1})&&{\text{(left inverse)}}\\&=(f^{-1})^{-1}\cdot f^{-1}&&{\text{(left identity)}}\\&=e&&{\text{(left inverse)}}\end{aligned}}$

Similarly, the left identity is also a right identity:

${\begin{aligned}f\cdot e&=f\cdot (f^{-1}\cdot f)&&{\text{(left inverse)}}\\&=(f\cdot f^{-1})\cdot f&&{\text{(associativity)}}\\&=e\cdot f&&{\text{(right inverse)}}\\&=f&&{\text{(left identity)}}\end{aligned}}$

These results do not hold if any of these axioms (associativity, existence of left identity and existence of left inverse) is removed. For a structure with a looser definition (like a semigroup) one may have, for example, that a left identity is not necessarily a right identity.

The same result can be obtained by only assuming the existence of a right identity and a right inverse.

However, only assuming the existence of a *left* identity and a *right* inverse (or vice versa) is not sufficient to define a group. For example, consider the set $G=\{e,f\}$ with the operator $\,\!\cdot$ satisfying $e\cdot e=f\cdot e=e$ and ⁠ $e\cdot f=f\cdot f=f$ ⁠. This structure does have a left identity (namely, ⁠ e ⁠), and each element has a right inverse (which is e for both elements). Furthermore, this operation is associative (since the product of any number of elements is always equal to the rightmost element in that product, regardless of the order in which these operations are applied). However, $(G,\cdot )$ is not a group, since it lacks a right identity.


## Basic concepts

When studying sets, one uses concepts such as subset, function, and quotient by an equivalence relation. When studying groups, one uses instead subgroups, homomorphisms, and quotient groups. These are the analogues that take the group structure into account.

### Group homomorphisms

Group homomorphisms are functions that respect group structure; they may be used to relate two groups. A *homomorphism* from a group $(G,\cdot )$ to a group $(H,*)$ is a function $\varphi :G\to H$ such that

$\varphi (a\cdot b)=\varphi (a)*\varphi (b)$

for all elements

a

and

b

in

⁠

G

⁠

.

It would be natural to require also that $\varphi$ respect identities, ⁠ $\varphi (1_{G})=1_{H}$ ⁠, and inverses, $\varphi (a^{-1})=\varphi (a)^{-1}$ for all a in ⁠ G ⁠. However, these additional requirements need not be included in the definition of homomorphisms, because they are already implied by the requirement of respecting the group operation.

The *identity homomorphism* of a group G is the homomorphism $\iota _{G}:G\to G$ that maps each element of G to itself. An *inverse homomorphism* of a homomorphism $\varphi :G\to H$ is a homomorphism $\psi :H\to G$ such that $\psi \circ \varphi =\iota _{G}$ and ⁠ $\varphi \circ \psi =\iota _{H}$ ⁠, that is, such that $\psi {\bigl (}\varphi (g){\bigr )}=g$ for all g in G and such that $\varphi {\bigl (}\psi (h){\bigr )}=h$ for all h in ⁠ H ⁠. An *isomorphism* is a homomorphism that has an inverse homomorphism; equivalently, it is a bijective homomorphism. Groups G and H are called *isomorphic* if there exists an isomorphism ⁠ $\varphi :G\to H$ ⁠. In this case, H can be obtained from G simply by renaming its elements according to the function ⁠ $\varphi$ ⁠; then any statement true for G is true for ⁠ H ⁠, provided that any specific elements mentioned in the statement are also renamed.

The collection of all groups, together with the homomorphisms between them, form a category, the category of groups.

An injective homomorphism $\phi :G'\to G$ factors canonically as an isomorphism followed by an inclusion, $G'\;{\stackrel {\sim }{\to }}\;H\hookrightarrow G$ for some subgroup ⁠ H ⁠ of ⁠ G ⁠. Injective homomorphisms are the monomorphisms in the category of groups.

### Subgroups

Informally, a *subgroup* is a group H contained within a bigger one, ⁠ G ⁠: it has a subset of the elements of ⁠ G ⁠, with the same operation. Concretely, this means that the identity element of G must be contained in ⁠ H ⁠, and whenever $h_{1}$ and $h_{2}$ are both in ⁠ H ⁠, then so are $h_{1}\cdot h_{2}$ and ⁠ $h_{1}^{-1}$ ⁠, so the elements of ⁠ H ⁠, equipped with the group operation on G restricted to ⁠ H ⁠, indeed form a group. In this case, the inclusion map $H\to G$ is a homomorphism.

In the example of symmetries of a square, the identity and the rotations constitute a subgroup ⁠ $R=\{\mathrm {id} ,r_{1},r_{2},r_{3}\}$ ⁠, highlighted in red in the Cayley table of the example: any two rotations composed are still a rotation, and a rotation can be undone by (i.e., is inverse to) the complementary rotations 270° for 90°, 180° for 180°, and 90° for 270°. The subgroup test provides a necessary and sufficient condition for a nonempty subset ⁠ H ⁠ of a group ⁠ G ⁠ to be a subgroup: it is sufficient to check that $g^{-1}\cdot h\in H$ for all elements g and h in ⁠ H ⁠. Knowing a group's subgroups is important in understanding the group as a whole.

Given any subset S of a group ⁠ G ⁠, the subgroup generated by S consists of all products of elements of S and their inverses. It is the smallest subgroup of G containing ⁠ S ⁠. In the example of symmetries of a square, the subgroup generated by $r_{2}$ and $f_{\mathrm {v} }$ consists of these two elements, the identity element ⁠ $\mathrm {id}$ ⁠, and the element ⁠ $f_{\mathrm {h} }=f_{\mathrm {v} }\cdot r_{2}$ ⁠. Again, this is a subgroup, because combining any two of these four elements or their inverses (which are, in this particular case, these same elements) yields an element of this subgroup.

### Cosets

In many situations it is desirable to consider two group elements the same if they differ by an element of a given subgroup. For example, in the symmetry group of a square, once any reflection is performed, rotations alone cannot return the square to its original position, so one can think of the reflected positions of the square as all being equivalent to each other, and as inequivalent to the unreflected positions; the rotation operations are irrelevant to the question whether a reflection has been performed. Cosets are used to formalize this insight: a subgroup H determines left and right cosets, which can be thought of as translations of H by an arbitrary group element ⁠ g ⁠. In symbolic terms, the *left* and *right* cosets of ⁠ H ⁠, containing an element ⁠ g ⁠, are

$gH=\{g\cdot h\mid h\in H\}$

and

⁠

$Hg=\{h\cdot g\mid h\in H\}$

⁠

, respectively.

The left cosets of any subgroup H form a partition of ⁠ G ⁠; that is, the union of all left cosets is equal to G and two left cosets are either equal or have an empty intersection. The first case $g_{1}H=g_{2}H$ happens precisely when ⁠ $g_{1}^{-1}\cdot g_{2}\in H$ ⁠, i.e., when the two elements differ by an element of ⁠ H ⁠. Similar considerations apply to the right cosets of ⁠ H ⁠. The left cosets of H may or may not be the same as its right cosets. If they are (that is, if all g in G satisfy ⁠ $gH=Hg$ ⁠), then H is said to be a *normal subgroup*.

In ⁠ $\mathrm {D} _{4}$ ⁠, the group of symmetries of a square, with its subgroup R of rotations, the left cosets $gR$ are either equal to ⁠ R ⁠, if g is an element of R itself, or otherwise equal to $U=f_{\mathrm {c} }R=\{f_{\mathrm {c} },f_{\mathrm {d} },f_{\mathrm {v} },f_{\mathrm {h} }\}$ (highlighted in green in the Cayley table of ⁠ $\mathrm {D} _{4}$ ⁠). The subgroup R is normal, because $f_{\mathrm {c} }R=U=Rf_{\mathrm {c} }$ and similarly for the other elements of the group. (In fact, in the case of ⁠ $\mathrm {D} _{4}$ ⁠, the cosets generated by reflections are all equal: ⁠ $f_{\mathrm {h} }R=f_{\mathrm {v} }R=f_{\mathrm {d} }R=f_{\mathrm {c} }R$ ⁠.)

### Quotient groups

Suppose that N is a normal subgroup of a group ⁠ G ⁠, and $G/N=\{gN\mid g\in G\}$ denotes its set of cosets. Then there is a unique group law on $G/N$ for which the map $G\to G/N$ sending each element g to $gN$ is a homomorphism. Explicitly, the product of two cosets $gN$ and $hN$ is ⁠ $(gh)N$ ⁠, the coset $eN=N$ serves as the identity of ⁠ $G/N$ ⁠, and the inverse of $gN$ in the quotient group is ⁠ $(gN)^{-1}=\left(g^{-1}\right)N$ ⁠. The group ⁠ $G/N$ ⁠, read as "⁠ G ⁠ modulo ⁠ N ⁠", is called a *quotient group* or *factor group*. The quotient group can alternatively be characterized by a universal property.

| $\cdot$ | R | U |
|---|---|---|
| R | R | U |
| U | U | R |

The elements of the quotient group $\mathrm {D} _{4}/R$ are R and ⁠ $U=f_{\mathrm {v} }R$ ⁠. The group operation on the quotient is shown in the table. For example, ⁠ $U\cdot U=f_{\mathrm {v} }R\cdot f_{\mathrm {v} }R=(f_{\mathrm {v} }\cdot f_{\mathrm {v} })R=R$ ⁠. Both the subgroup $R=\{\mathrm {id} ,r_{1},r_{2},r_{3}\}$ and the quotient $\mathrm {D} _{4}/R$ are abelian, but $\mathrm {D} _{4}$ is not. Sometimes a group can be reconstructed from a subgroup and quotient (plus some additional data), by the semidirect product construction; $\mathrm {D} _{4}$ is an example.

The first isomorphism theorem implies that any surjective homomorphism $\phi :G\to H$ factors canonically as a quotient homomorphism followed by an isomorphism: ⁠ $G\to G/\ker \phi \;{\stackrel {\sim }{\to }}\;H$ ⁠. Surjective homomorphisms are the epimorphisms in the category of groups.

### Presentations

Every group is isomorphic to a quotient of a free group, in many ways.

For example, the dihedral group $\mathrm {D} _{4}$ is generated by the right rotation $r_{1}$ and the reflection $f_{\mathrm {v} }$ in a vertical line (every element of $\mathrm {D} _{4}$ is a finite product of copies of these and their inverses). Hence there is a surjective homomorphism ⁠ $\phi$ ⁠ from the free group $\langle r,f\rangle$ on two generators to $\mathrm {D} _{4}$ sending r to $r_{1}$ and f to ⁠ $f_{1}$ ⁠. Elements in $\ker \phi$ are called *relations*; examples include ⁠ $r^{4},f^{2},(r\cdot f)^{2}$ ⁠. In fact, it turns out that $\ker \phi$ is the smallest normal subgroup of $\langle r,f\rangle$ containing these three elements; in other words, all relations are consequences of these three. The quotient of the free group by this normal subgroup is denoted ⁠ $\langle r,f\mid r^{4}=f^{2}=(r\cdot f)^{2}=1\rangle$ ⁠. This is called a *presentation* of $\mathrm {D} _{4}$ by generators and relations, because the first isomorphism theorem for ⁠ $\phi$ ⁠ yields an isomorphism ⁠ $\langle r,f\mid r^{4}=f^{2}=(r\cdot f)^{2}=1\rangle \to \mathrm {D} _{4}$ ⁠.

A presentation of a group can be used to construct the Cayley graph, a graphical depiction of a discrete group.


## Examples and applications

Examples and applications of groups abound. A starting point is the group $\mathbb {Z}$ of integers with addition as group operation, introduced above. If, instead of addition, multiplication is considered, one obtains multiplicative groups. These groups are predecessors of important constructions in abstract algebra.

Groups are also applied in many other mathematical areas. Mathematical objects are often examined by associating groups to them and studying the properties of the corresponding groups. For example, Henri Poincaré founded what is now called algebraic topology by introducing the fundamental group. By means of this connection, topological properties such as proximity and continuity translate into properties of groups.

Elements of the fundamental group of a topological space are equivalence classes of loops, where loops are considered equivalent if one can be smoothly deformed into another, and the group operation is "concatenation" (tracing one loop then the other). For example, as shown in the figure, if the topological space is the plane with one point removed, then loops which do not wrap around the missing point (blue) can be smoothly contracted to a single point and are the identity element of the fundamental group. A loop which wraps around the missing point k times cannot be deformed into a loop which wraps m times (with ⁠ $m\neq k$ ⁠), because the loop cannot be smoothly deformed across the hole, so each class of loops is characterized by its winding number around the missing point. The resulting group is isomorphic to the integers under addition.

In more recent applications, the influence has also been reversed to motivate geometric constructions by a group-theoretical background. In a similar vein, geometric group theory employs geometric concepts, for example in the study of hyperbolic groups. Further branches crucially applying groups include algebraic geometry and number theory.

In addition to the above theoretical applications, many practical applications of groups exist. Cryptography relies on the combination of the abstract group theory approach together with algorithmical knowledge obtained in computational group theory, in particular when implemented for finite groups. Applications of group theory are not restricted to mathematics; sciences such as physics, chemistry and computer science benefit from the concept.

### Numbers

Many number systems, such as the integers and the rationals, enjoy a naturally given group structure. In some cases, such as with the rationals, both addition and multiplication operations give rise to group structures. Such number systems are predecessors to more general algebraic structures known as rings and fields. Further abstract algebraic concepts such as modules, vector spaces and algebras also form groups.

#### Integers

The group of integers $\mathbb {Z}$ under addition, denoted ⁠ $\left(\mathbb {Z} ,+\right)$ ⁠, has been described above. The integers, with the operation of multiplication instead of addition, $\left(\mathbb {Z} ,\cdot \right)$ do *not* form a group. The associativity and identity axioms are satisfied, but inverses do not exist: for example, $a=2$ is an integer, but the only solution to the equation $a\cdot b=1$ in this case is ⁠ $b={\tfrac {1}{2}}$ ⁠, which is a rational number, but not an integer. Hence not every element of $\mathbb {Z}$ has a (multiplicative) inverse.

#### Rationals

The desire for the existence of multiplicative inverses suggests considering fractions ${\frac {a}{b}}.$

Fractions of integers (with b nonzero) are known as rational numbers. The set of all such irreducible fractions is commonly denoted ⁠ $\mathbb {Q}$ ⁠. There is still a minor obstacle for ⁠ $\left(\mathbb {Q} ,\cdot \right)$ ⁠, the rationals with multiplication, being a group: because zero does not have a multiplicative inverse (i.e., there is no x such that ⁠ $x\cdot 0=1$ ⁠), $\left(\mathbb {Q} ,\cdot \right)$ is still not a group.

However, the set of all *nonzero* rational numbers $\mathbb {Q} \smallsetminus \left\{0\right\}=\left\{q\in \mathbb {Q} \mid q\neq 0\right\}$ does form an abelian group under multiplication, also denoted ⁠ $\mathbb {Q} ^{\times }$ ⁠. Associativity and identity element axioms follow from the properties of integers. The closure requirement still holds true after removing zero, because the product of two nonzero rationals is never zero. Finally, the inverse of $a/b$ is ⁠ $b/a$ ⁠, therefore the axiom of the inverse element is satisfied.

The rational numbers (including zero) also form a group under addition. Intertwining addition and multiplication operations yields more complicated structures called rings and – if division by other than zero is possible, such as in $\mathbb {Q}$ – fields, which occupy a central position in abstract algebra. Group theoretic arguments therefore underlie parts of the theory of those entities.

### Modular arithmetic

Modular arithmetic for a *modulus* n defines any two elements a and b that differ by a multiple of n to be equivalent, denoted by ⁠ $a\equiv b{\pmod {n}}$ ⁠. Every integer is equivalent to one of the integers from 0 to ⁠ $n-1$ ⁠, and the operations of modular arithmetic modify normal arithmetic by replacing the result of any operation by its equivalent representative. Modular addition, defined in this way for the integers from 0 to ⁠ $n-1$ ⁠, forms a group, denoted as $\mathrm {Z} _{n}$ or ⁠ $(\mathbb {Z} /n\mathbb {Z} ,+)$ ⁠, with 0 as the identity element and $n-a$ as the inverse element of ⁠ a ⁠.

A familiar example is addition of hours on the face of a clock, where 12 rather than 0 is chosen as the representative of the identity. If the hour hand is on 9 and is advanced 4 hours, it ends up on ⁠ 1 ⁠, as shown in the illustration. This is expressed by saying that $9+4$ is congruent to 1 "modulo ⁠ $12$ ⁠" or, in symbols, $9+4\equiv 1{\pmod {12}}.$

For any prime number ⁠ p ⁠, there is also the multiplicative group of integers modulo ⁠ p ⁠. Its elements can be represented by 1 to ⁠ $p-1$ ⁠. The group operation, multiplication modulo ⁠ p ⁠, replaces the usual product by its representative, the remainder of division by ⁠ p ⁠. For example, for ⁠ $p=5$ ⁠, the four group elements can be represented by ⁠ $1,2,3,4$ ⁠. In this group, ⁠ $4\cdot 4\equiv 1{\pmod {5}}$ ⁠, because the usual product $16$ is equivalent to ⁠ 1 ⁠: when divided by 5 it yields a remainder of ⁠ 1 ⁠. The primality of p ensures that the usual product of two representatives is not divisible by ⁠ p ⁠, and therefore that the modular product is nonzero. The identity element is represented by ⁠ 1 ⁠, and associativity follows from the corresponding property of the integers. Finally, the inverse element axiom requires that given an integer a not divisible by ⁠ p ⁠, there exists an integer b such that $a\cdot b\equiv 1{\pmod {p}},$ that is, such that p evenly divides ⁠ $a\cdot b-1$ ⁠. The inverse b can be found by using Bézout's identity and the fact that the greatest common divisor $\gcd(a,p)$ equals ⁠ 1 ⁠. In the case $p=5$ above, the inverse of the element represented by 4 is that represented by ⁠ 4 ⁠, and the inverse of the element represented by 3 is represented by ⁠ 2 ⁠, as ⁠ $3\cdot 2=6\equiv 1{\pmod {5}}$ ⁠. Hence all group axioms are fulfilled. This example is similar to $\left(\mathbb {Q} \smallsetminus \left\{0\right\},\cdot \right)$ above: it consists of exactly those elements in the ring $\mathbb {Z} /p\mathbb {Z}$ that have a multiplicative inverse. These groups, denoted ⁠ $\mathbb {F} _{p}^{\times }$ ⁠, are crucial to public-key cryptography.

### Cyclic groups

A *cyclic group* is a group all of whose elements are powers of a particular element ⁠ a ⁠. In multiplicative notation, the elements of the group are $\dots ,a^{-3},a^{-2},a^{-1},a^{0},a,a^{2},a^{3},\dots ,$ where $a^{2}$ means ⁠ $a\cdot a$ ⁠, $a^{-3}$ stands for ⁠ $a^{-1}\cdot a^{-1}\cdot a^{-1}=(a\cdot a\cdot a)^{-1}$ ⁠, etc. Such an element a is called a generator or a primitive element of the group. In additive notation, the requirement for an element to be primitive is that each element of the group can be written as $\dots ,(-a)+(-a),-a,0,a,a+a,\dots .$

In the groups $(\mathbb {Z} /n\mathbb {Z} ,+)$ introduced above, the element 1 is primitive, so these groups are cyclic. Indeed, each element is expressible as a sum all of whose terms are ⁠ 1 ⁠. Any cyclic group with n elements is isomorphic to this group. A second example for cyclic groups is the group of ⁠ n ⁠th complex roots of unity, given by complex numbers z satisfying ⁠ $z^{n}=1$ ⁠. These numbers can be visualized as the vertices on a regular n -gon, as shown in blue in the image for ⁠ $n=6$ ⁠. The group operation is multiplication of complex numbers. In the picture, multiplying with z corresponds to a counter-clockwise rotation by 60°. From field theory, the group $\mathbb {F} _{p}^{\times }$ is cyclic for prime p : for example, if ⁠ $p=5$ ⁠, 3 is a generator since ⁠ $3^{1}=3$ ⁠, ⁠ $3^{2}=9\equiv 4$ ⁠, ⁠ $3^{3}\equiv 2$ ⁠, and ⁠ $3^{4}\equiv 1$ ⁠.

Some cyclic groups have an infinite number of elements. In these groups, for every non-zero element ⁠ a ⁠, all the powers of a are distinct; despite the name "cyclic group", the powers of the elements do not cycle. An infinite cyclic group is isomorphic to ⁠ $(\mathbb {Z} ,+)$ ⁠, the group of integers under addition introduced above. As these two prototypes are both abelian, so are all cyclic groups.

The study of finitely generated abelian groups is quite mature, including the fundamental theorem of finitely generated abelian groups; and reflecting this state of affairs, many group-related notions, such as center and commutator, describe the extent to which a given group is not abelian.

### Symmetry groups

*Symmetry groups* are groups consisting of symmetries of given mathematical objects, principally geometric entities, such as the symmetry group of the square given as an introductory example above, although they also arise in algebra such as the symmetries among the roots of polynomial equations dealt with in Galois theory (see below). Conceptually, group theory can be thought of as the study of symmetry. Symmetries in mathematics greatly simplify the study of geometrical or analytical objects. A group is said to act on another mathematical object ⁠ X ⁠ if every group element can be associated to some operation on ⁠ X ⁠ and the composition of these operations follows the group law. For example, an element of the (2,3,7) triangle group acts on a triangular tiling of the hyperbolic plane by permuting the triangles. By a group action, the group pattern is connected to the structure of the object being acted on.

In chemistry, point groups describe molecular symmetries, while space groups describe crystal symmetries in crystallography. These symmetries underlie the chemical and physical behavior of these systems, and group theory enables simplification of quantum mechanical analysis of these properties. For example, group theory is used to show that optical transitions between certain quantum levels cannot occur simply because of the symmetry of the states involved.

Group theory helps predict the changes in physical properties that occur when a material undergoes a phase transition, for example, from a cubic to a tetrahedral crystalline form. An example is ferroelectric materials, where the change from a paraelectric to a ferroelectric state occurs at the Curie temperature and is related to a change from the high-symmetry paraelectric state to the lower symmetry ferroelectric state, accompanied by a so-called soft phonon mode, a vibrational lattice mode that goes to zero frequency at the transition.

Such spontaneous symmetry breaking has found further application in elementary particle physics, where its occurrence is related to the appearance of Goldstone bosons.

| (A schematic depiction of a Buckminsterfullerene molecule) | (A schematic depiction of an Ammonia molecule) | (A schematic depiction of a cubane molecule) |   |
|---|---|---|---|
| Buckminsterfullerene displays icosahedral symmetry | Ammonia, NH3. Its symmetry group is of order 6, generated by a 120° rotation and a reflection. | Cubane C8H8 features octahedral symmetry. | The tetrachloroplatinate(II) ion, [PtCl4]2− exhibits square-planar geometry |

Finite symmetry groups such as the Mathieu groups are used in coding theory, which is in turn applied in error correction of transmitted data, and in CD players. Another application is differential Galois theory, which characterizes functions having antiderivatives of a prescribed form, giving group-theoretic criteria for when solutions of certain differential equations are well-behaved. Geometric properties that remain stable under group actions are investigated in (geometric) invariant theory.

### General linear group and representation theory

Matrix groups consist of matrices together with matrix multiplication. The *general linear group* $\mathrm {GL} (n,\mathbb {R} )$ consists of all invertible ⁠ n ⁠-by-⁠ n ⁠ matrices with real entries. Its subgroups are referred to as *matrix groups* or *linear groups*. The dihedral group example mentioned above can be viewed as a (very small) matrix group. Another important matrix group is the special orthogonal group ⁠ $\mathrm {SO} (n)$ ⁠. It describes all possible rotations in n dimensions. Rotation matrices in this group are used in computer graphics.

*Representation theory* is both an application of the group concept and important for a deeper understanding of groups. It studies the group by its group actions on other spaces. A broad class of group representations are linear representations in which the group acts on a vector space, such as the three-dimensional Euclidean space ⁠ $\mathbb {R} ^{3}$ ⁠. A representation of a group G on an n -dimensional real vector space is simply a group homomorphism $\rho :G\to \mathrm {GL} (n,\mathbb {R} )$ from the group to the general linear group. This way, the group operation, which may be abstractly given, translates to the multiplication of matrices making it accessible to explicit computations.

A group action gives further means to study the object being acted on. On the other hand, it also yields information about the group. Group representations are an organizing principle in the theory of finite groups, Lie groups, algebraic groups and topological groups, especially (locally) compact groups.

### Galois groups

*Galois groups* were developed to help solve polynomial equations by capturing their symmetry features. For example, the solutions of the quadratic equation $ax^{2}+bx+c=0$ are given by $x={\frac {-b\pm {\sqrt {b^{2}-4ac}}}{2a}}.$ Each solution can be obtained by replacing the $\pm$ sign by + or ⁠ - ⁠; analogous formulae are known for cubic and quartic equations, but do *not* exist in general for degree 5 and higher. In the quadratic formula, changing the sign (permuting the resulting two solutions) can be viewed as a (very simple) group operation. Analogous Galois groups act on the solutions of higher-degree polynomial equations and are closely related to the existence of formulas for their solution. Abstract properties of these groups (in particular their solvability) give a criterion for the ability to express the solutions of these polynomials using solely addition, multiplication, and roots similar to the formula above.

Modern Galois theory generalizes the above type of Galois groups by shifting to field theory and considering field extensions formed as the splitting field of a polynomial. This theory establishes—via the fundamental theorem of Galois theory—a precise relationship between fields and groups, underlining once again the ubiquity of groups in mathematics.
