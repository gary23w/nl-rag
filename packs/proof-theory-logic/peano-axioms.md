---
title: "Peano axioms"
source: https://en.wikipedia.org/wiki/Peano_axioms
domain: proof-theory-logic
license: CC-BY-SA-4.0
tags: proof theory, sequent calculus, natural deduction, cut-elimination theorem
fetched: 2026-07-02
---

# Peano axioms

In mathematical logic, the **Peano axioms** (/piˈɑːnoʊ/; [peˈaːno]), also known as the **Dedekind–Peano axioms** or the **Peano postulates**, are axioms for the natural numbers presented by the 19th-century Italian mathematician Giuseppe Peano. These axioms have been used nearly unchanged in a number of metamathematical investigations, including research into fundamental questions of whether number theory is consistent and complete.

The axiomatization of arithmetic provided by Peano axioms is commonly called **Peano arithmetic**.

The importance of formalizing arithmetic was not well appreciated until the work of Hermann Grassmann, who showed in the 1860s that many facts in arithmetic could be derived from more basic facts about the successor operation and induction. In 1881, Charles Sanders Peirce provided an axiomatization of natural-number arithmetic. In 1888, Richard Dedekind proposed another axiomatization of natural-number arithmetic, and in 1889, Peano published a simplified version of them as a collection of axioms in his book *The principles of arithmetic presented by a new method* (Latin: *Arithmetices principia, nova methodo exposita*).

Peano’s axioms can be divided into groups according to their subject matter. The first axiom asserts the existence of at least one member of the set of natural numbers. The next four are general statements about equality; in modern treatments these are often not taken as part of the Peano axioms, but rather as axioms of the "underlying logic". The next three axioms are first-order statements about natural numbers expressing the fundamental properties of the successor operation. The ninth, final, axiom is a second-order statement of the principle of mathematical induction over the natural numbers, which makes this formulation close to second-order arithmetic. A weaker first-order system is obtained by explicitly adding the addition and multiplication operation symbols and replacing the second-order induction axiom with a first-order axiom schema. The term *Peano arithmetic* is sometimes used for specifically naming this restricted system.

## Historical second-order formulation

When Peano formulated his axioms, the language of mathematical logic was in its infancy. The system of logical notation he created to present the axioms did not prove to be popular, although it was the genesis of the modern notation for set membership (∈, which comes from Peano's ε). Peano maintained a clear distinction between mathematical and logical symbols, which was not yet common in mathematics; such a separation had first been introduced in the *Begriffsschrift* by Gottlob Frege, published in 1879. Peano was unaware of Frege's work and independently recreated his logical apparatus based on the work of Boole and Schröder.

The Peano axioms define the arithmetical properties of *natural numbers*, usually represented as a set **N** or $\mathbb {N} .$ The non-logical symbols for the axioms consist of a constant symbol 0 and a unary function symbol *S*.

The first axiom states that the constant 0 is a natural number:

1. 0 is a natural number.

Peano's original formulation of the axioms used 1 instead of 0 as the "first" natural number, while the axioms in *Formulario mathematico* include zero.

The next four axioms describe the equality relation. Since they are logically valid in first-order logic with equality, they are not considered to be part of "the Peano axioms" in modern treatments.

1. For every natural number *x*, *x* = *x*. That is, equality is reflexive.
2. For all natural numbers *x* and *y*, if *x* = *y*, then *y* = *x*. That is, equality is symmetric.
3. For all natural numbers *x*, *y* and *z*, if *x* = *y* and *y* = *z*, then *x* = *z*. That is, equality is transitive.
4. For all *a* and *b*, if *b* is a natural number and *a* = *b*, then *a* is also a natural number. That is, the natural numbers are closed under equality.

The remaining axioms define the arithmetical properties of the natural numbers. The naturals are assumed to be closed under a single-valued "successor" function *S*.

1. For every natural number *n*, *S*(*n*) is a natural number. That is, the natural numbers are closed under *S*.
2. For all natural numbers *m* and *n*, if *S*(*m*) = *S*(*n*), then *m* = *n*. That is, *S* is an injection.
3. For every natural number *n*, *S*(*n*) = 0 is false. That is, there is no natural number whose successor is 0.

Axioms 1, 6, 7, 8 define a unary representation of the intuitive notion of natural numbers: the number 1 can be defined as *S*(0), 2 as *S*(*S*(0)), etc. However, considering the notion of natural numbers as being defined by these axioms, axioms 1, 6, 7, 8 do not imply that the successor function generates all the natural numbers different from 0.

The intuitive notion that each natural number can be obtained by applying *successor* sufficiently many times to zero requires an additional axiom, which is sometimes called the *axiom of induction*.

1. If *K* is a set such that: then *K* contains every natural number.
  - 0 is in *K*, and
  - for every natural number *n*, *n* being in *K* implies that *S*(*n*) is in *K*,

The induction axiom is sometimes stated in the following form:

1. If *φ* is a unary predicate such that: then *φ*(*n*) is true for every natural number *n*.
  - *φ*(0) is true, and
  - for every natural number *n*, *φ*(*n*) being true implies that *φ*(*S*(*n*)) is true,

In Peano's original formulation, the induction axiom is a second-order axiom. It is now common to replace this second-order principle with a weaker first-order induction scheme. There are important differences between the second-order and first-order formulations, as discussed in the section § Peano arithmetic as first-order theory below.

### Defining arithmetic operations and relations

If the second-order induction axiom is used, it is possible to define addition, multiplication, and total (linear) ordering on **N** directly using the axioms. However, with first-order induction, this is not possible and addition and multiplication are often added as axioms. The respective functions and relations are constructed in set theory or second-order logic, and can be shown to be unique using the Peano axioms.

#### Addition

Addition is a function that maps two natural numbers (two elements of **N**) to another one. It is defined recursively as:

${\begin{aligned}a+0&=a,&{\textrm {(1)}}\\a+S(b)&=S(a+b).&{\textrm {(2)}}\end{aligned}}$

For example:

${\begin{aligned}a+1&=a+S(0)&{\mbox{by definition}}\\&=S(a+0)&{\mbox{using (2)}}\\&=S(a),&{\mbox{using (1)}}\\\\a+2&=a+S(1)&{\mbox{by definition}}\\&=S(a+1)&{\mbox{using (2)}}\\&=S(S(a))&{\mbox{using }}a+1=S(a)\\\\a+3&=a+S(2)&{\mbox{by definition}}\\&=S(a+2)&{\mbox{using (2)}}\\&=S(S(S(a)))&{\mbox{using }}a+2=S(S(a))\\{\text{etc.}}&\\\end{aligned}}$

To prove commutativity of addition, first prove $0+b=b$ and $S(a)+b=S(a+b)$ , each by induction on b . Using both results, then prove $a+b=b+a$ by induction on b . The structure (**N**, +) is a commutative monoid with identity element 0. (**N**, +) is also a cancellative magma, and thus embeddable in a group. The smallest group embedding **N** is the integers.

#### Multiplication

Similarly, multiplication is a function mapping two natural numbers to another one. Given addition, it is defined recursively as:

${\begin{aligned}a\cdot 0&=0,\\a\cdot S(b)&=a+(a\cdot b).\end{aligned}}$

It is easy to see that $S(0)$ is the multiplicative right identity:

$a\cdot S(0)=a+(a\cdot 0)=a+0=a$

To show that $S(0)$ is also the multiplicative left identity requires the induction axiom due to the way multiplication is defined:

- $S(0)$ is the left identity of 0: $S(0)\cdot 0=0$ .
- If $S(0)$ is the left identity of a (that is $S(0)\cdot a=a$ ), then $S(0)$ is also the left identity of $S(a)$ : $S(0)\cdot S(a)=S(0)+S(0)\cdot a=S(0)+a=a+S(0)=S(a+0)=S(a)$ , using commutativity of addition.

Therefore, by the induction axiom $S(0)$ is the multiplicative left identity of all natural numbers. Moreover, it can be shown that multiplication is commutative and distributes over addition:

$a\cdot (b+c)=(a\cdot b)+(a\cdot c)$

.

Thus, $(\mathbb {N} ,+,0,\cdot ,S(0))$ is a commutative semiring.

#### Inequalities

The usual total order relation ≤ on natural numbers can be defined as follows, assuming 0 is a natural number:

For all

a

,

b

∈

N

,

a

≤

b

if and only if there exists some

c

∈

N

such that

a

+

c

=

b

.

This relation is stable under addition and multiplication: for $a,b,c\in \mathbb {N}$ , if *a* ≤ *b*, then:

- *a* + *c* ≤ *b* + *c*, and
- *a* · *c* ≤ *b* · *c*.

Thus, the structure (**N**, +, ·, 1, 0, ≤) is an ordered semiring; because there is no natural number between 0 and 1, it is a discrete ordered semiring.

The axiom of induction is sometimes stated in the following form that uses a stronger hypothesis, making use of the order relation "≤":

For any

predicate

φ

, if

- *φ*(0) is true, and
- for every *n* ∈ **N**, if *φ*(*k*) is true for every *k* ∈ **N** such that *k* ≤ *n*, then *φ*(*S*(*n*)) is true,
- then for every *n* ∈ **N**, *φ*(*n*) is true.

This form of the induction axiom, called *strong induction*, is a consequence of the standard formulation, but is often better suited for reasoning about the ≤ order. For example, to show that the naturals are well-ordered—every nonempty subset of **N** has a least element—one can reason as follows. Let a nonempty *X* ⊆ **N** be given and assume *X* has no least element.

- Because 0 is the least element of **N**, it must be that 0 ∉ *X*.
- For any *n* ∈ **N**, suppose for every *k* ≤ *n*, *k* ∉ *X*. Then *S*(*n*) ∉ *X*, for otherwise it would be the least element of *X*.

Thus, by the strong induction principle, for every *n* ∈ **N**, *n* ∉ *X*. Thus, *X* ∩ **N** = ∅, which contradicts *X* being a nonempty subset of **N**. Thus *X* has a least element.

### Models

A model of the Peano axioms is a triple (**N**, 0, *S*), where **N** is a (necessarily infinite) set, 0 ∈ **N** and *S*: **N** → **N** satisfies the axioms above. Dedekind proved in his 1888 book, *The Nature and Meaning of Numbers* (German: *Was sind und was sollen die Zahlen?*, i.e., "What are the numbers and what are they good for?") that any two models of the Peano axioms (including the second-order induction axiom) are isomorphic. In particular, given two models (**N***A*, 0*A*, *S**A*) and (**N***B*, 0*B*, *S**B*) of the Peano axioms, there is a unique homomorphism *f* : **N***A* → **N***B* satisfying

${\begin{aligned}f(0_{A})&=0_{B}\\f(S_{A}(n))&=S_{B}(f(n))\end{aligned}}$

and it is a bijection. This means that the second-order Peano axioms are categorical. (This is not the case with any first-order reformulation of the Peano axioms, below.)

#### Set-theoretic models

The Peano axioms can be derived from set theoretic constructions of the natural numbers and axioms of set theory such as ZF. The standard construction of the naturals, due to John von Neumann, starts from a definition of 0 as the empty set, ∅, and an operator *s* on sets defined as:

$s(a)=a\cup \{a\}$

The set of natural numbers **N** is defined as the intersection of all sets closed under *s* that contain the empty set. Each natural number is equal (as a set) to the set of natural numbers less than it:

${\begin{aligned}0&=\emptyset \\1&=s(0)=s(\emptyset )=\emptyset \cup \{\emptyset \}=\{\emptyset \}=\{0\}\\2&=s(1)=s(\{0\})=\{0\}\cup \{\{0\}\}=\{0,\{0\}\}=\{0,1\}\\3&=s(2)=s(\{0,1\})=\{0,1\}\cup \{\{0,1\}\}=\{0,1,\{0,1\}\}=\{0,1,2\}\end{aligned}}$

and so on. The set **N** together with 0 and the successor function *s* : **N** → **N** satisfies the Peano axioms.

Peano arithmetic is equiconsistent with several weak systems of set theory. One such system is ZFC with the axiom of infinity replaced by its negation. Another such system consists of general set theory (extensionality, existence of the empty set, and the axiom of adjunction), augmented by an axiom schema stating that a property that holds for the empty set and holds of an adjunction whenever it holds of the adjunct must hold for all sets.

#### Interpretation in category theory

The Peano axioms can also be understood using category theory. Let *C* be a category with terminal object 1*C*, and define the category of pointed unary systems, US1(*C*) as follows:

- The objects of US1(*C*) are triples (*X*, 0*X*, *S**X*) where *X* is an object of *C*, and 0*X* : 1*C* → *X* and *S**X* : *X* → *X* are *C*-morphisms.
- A morphism *φ* : (*X*, 0*X*, *S**X*) → (*Y*, 0*Y*, *S**Y*) is a *C*-morphism *φ* : *X* → *Y* with *φ* 0*X* = 0*Y* and *φ* *S**X* = *S**Y* *φ*.

Then *C* is said to satisfy the Dedekind–Peano axioms if US1(*C*) has an initial object; this initial object is known as a natural number object in *C*. If (**N**, 0, *S*) is this initial object, and (*X*, 0*X*, *S**X*) is any other object, then the unique map *u* : (**N**, 0, *S*) → (*X*, 0*X*, *S**X*) is such that

${\begin{aligned}u(0)&=0_{X},\\u(S)&=S_{X}(u).\end{aligned}}$

This is precisely the recursive definition of 0*X* and *S**X*.

### Consistency

When the Peano axioms were first proposed, Bertrand Russell and others agreed that these axioms implicitly defined what we mean by a "natural number". Henri Poincaré was more cautious, saying they only defined natural numbers if they were *consistent*; if there is a proof that starts from just these axioms and derives a contradiction such as 0 = 1, then the axioms are inconsistent, and do not define anything. In 1900, David Hilbert posed the problem of proving their consistency using only finitistic methods as the second of his twenty-three problems. In 1931, Kurt Gödel proved his second incompleteness theorem, which shows that such a consistency proof cannot be formalized within Peano arithmetic itself, if Peano arithmetic is consistent.

Although it is widely claimed that Gödel's theorem rules out the possibility of a finitistic consistency proof for Peano arithmetic, this depends on exactly what one means by a finitistic proof. Gödel himself pointed out the possibility of giving a finitistic consistency proof of Peano arithmetic or stronger systems by using finitistic methods that are not formalizable in Peano arithmetic, and in 1958, Gödel published a method for proving the consistency of arithmetic using type theory. In 1936, Gerhard Gentzen gave a proof of the consistency of Peano's axioms, using transfinite induction up to an ordinal called ε0. Gentzen explained: "The aim of the present paper is to prove the consistency of elementary number theory or, rather, to reduce the question of consistency to certain fundamental principles". Gentzen's proof is arguably finitistic, since the transfinite ordinal ε0 can be encoded in terms of finite objects (for example, as a Turing machine describing a suitable order on the integers, or more abstractly as consisting of the finite trees, suitably linearly ordered). Whether or not Gentzen's proof meets the requirements Hilbert envisioned is unclear: there is no generally accepted definition of exactly what is meant by a finitistic proof, and Hilbert himself never gave a precise definition.

The vast majority of contemporary mathematicians believe that Peano's axioms are consistent, relying either on intuition or the acceptance of a consistency proof such as Gentzen's proof. A small number of philosophers and mathematicians, some of whom also advocate ultrafinitism, reject Peano's axioms because accepting the axioms amounts to accepting the infinite collection of natural numbers. In particular, addition (including the successor function) and multiplication are assumed to be total. Curiously, there are self-verifying theories that are similar to PA but have subtraction and division instead of addition and multiplication, which are axiomatized in such a way to avoid proving sentences that correspond to the totality of addition and multiplication, but which are still able to prove all true $\Pi _{1}$ theorems of PA, and yet can be extended to a consistent theory that proves its own consistency (stated as the non-existence of a Hilbert-style proof of "0=1").

## Peano arithmetic as first-order theory

All of the Peano axioms except the ninth axiom (the induction axiom) are statements in first-order logic. The arithmetical operations of addition and multiplication and the order relation can also be defined using first-order axioms. The axiom of induction above is second-order, since it quantifies over predicates (equivalently, sets of natural numbers rather than natural numbers). As an alternative one can consider a first-order *axiom schema* of induction. Such a schema includes one axiom per predicate definable in the first-order language of Peano arithmetic, making it weaker than the second-order axiom. The reason that it is weaker is that the number of predicates in first-order language is countable, whereas the number of sets of natural numbers is uncountable. Thus, there exist sets that cannot be described in first-order language (in fact, most sets have this property).

First-order axiomatizations of Peano arithmetic have another technical limitation. In second-order logic, it is possible to define the addition and multiplication operations from the successor operation, but this cannot be done in the more restrictive setting of first-order logic. Therefore, the addition and multiplication operations are directly included in the signature of Peano arithmetic, and axioms are included that relate the three operations to each other.

The following list of axioms (along with the usual axioms of equality), which contains six of the seven axioms of Robinson arithmetic, is sufficient for this purpose:

- $\forall x\ (0\neq S(x))$
- $\forall x,y\ (S(x)=S(y)\Rightarrow x=y)$
- $\forall x\ (x+0=x)$
- $\forall x,y\ (x+S(y)=S(x+y))$
- $\forall x\ (x\cdot 0=0)$
- $\forall x,y\ (x\cdot S(y)=x\cdot y+x)$

In addition to this list of numerical axioms, Peano arithmetic contains the induction schema, which consists of a recursively enumerable and even decidable set of axioms. For each formula *φ*(*x*, *y*1, ..., *y**k*) in the language of Peano arithmetic, the **first-order induction axiom** for *φ* is the sentence

$\forall {\bar {y}}{\Bigg (}{\bigg (}\varphi (0,{\bar {y}})\land \forall x{\Big (}\varphi (x,{\bar {y}})\Rightarrow \varphi (S(x),{\bar {y}}){\Big )}{\bigg )}\Rightarrow \forall x\varphi (x,{\bar {y}}){\Bigg )}$

where ${\bar {y}}$ is an abbreviation for *y*1,...,*y**k*. The first-order induction schema includes every instance of the first-order induction axiom; that is, it includes the induction axiom for every formula *φ*.

### Equivalent axiomatizations

The above axiomatization of Peano arithmetic uses a signature that only has symbols for zero as well as the successor, addition, and multiplications operations. There are many other different, but equivalent, axiomatizations. One such alternative uses an order relation symbol instead of the successor operation and the language of discretely ordered semirings (axioms 1-7 for semirings, 8-10 on order, 11-13 regarding compatibility, and 14-15 for discreteness):

1. $\forall x,y,z\ ((x+y)+z=x+(y+z))$ , i.e., addition is associative.
2. $\forall x,y\ (x+y=y+x)$ , i.e., addition is commutative.
3. $\forall x,y,z\ ((x\cdot y)\cdot z=x\cdot (y\cdot z))$ , i.e., multiplication is associative.
4. $\forall x,y\ (x\cdot y=y\cdot x)$ , i.e., multiplication is commutative.
5. $\forall x,y,z\ (x\cdot (y+z)=(x\cdot y)+(x\cdot z))$ , i.e., multiplication distributes over addition.
6. $\forall x\ (x+0=x\land x\cdot 0=0)$ , i.e., zero is an identity for addition, and an absorbing element for multiplication (actually superfluous).
7. $\forall x\ (x\cdot 1=x)$ , i.e., one is an identity for multiplication.
8. $\forall x,y,z\ (x<y\land y<z\Rightarrow x<z)$ , i.e., the '<' operator is transitive.
9. $\forall x\ (\neg (x<x))$ , i.e., the '<' operator is irreflexive.
10. $\forall x,y\ (x<y\lor x=y\lor y<x)$ , i.e., the ordering satisfies trichotomy.
11. $\forall x,y,z\ (x<y\Rightarrow x+z<y+z)$ , i.e. the ordering is preserved under addition of the same element.
12. $\forall x,y,z\ (0<z\land x<y\Rightarrow x\cdot z<y\cdot z)$ , i.e. the ordering is preserved under multiplication by the same positive element.
13. $\forall x,y\ (x<y\Rightarrow \exists z\ (x+z=y))$ , i.e. given any two distinct elements, the larger is the smaller plus another element.
14. $0<1\land \forall x\ (x>0\Rightarrow x\geq 1)$ , i.e. zero and one are distinct and there is no element between them. In other words, 0 is covered by 1, which suggests that these numbers are discrete.
15. $\forall x\ (x\geq 0)$ , i.e. zero is the minimum element.

The theory defined by these axioms is known as **PA−**. It is also incomplete and one of its important properties is that any structure M satisfying this theory has an initial segment (ordered by $\leq$ ) isomorphic to $\mathbb {N}$ . Elements in that segment are called **standard** elements, while other elements are called **nonstandard** elements.

Finally, Peano arithmetic **PA** is obtained by adding the first-order induction schema.

### Undecidability and incompleteness

According to Gödel's incompleteness theorems, the theory of **PA** (if consistent) is incomplete. Consequently, there are sentences of first-order logic (FOL) that are true in the standard model of **PA** but are not a consequence of the FOL axiomatization. Essential incompleteness already arises for theories with weaker axioms, such as Robinson arithmetic.

Closely related to the above incompleteness result (via Gödel's completeness theorem for FOL) it follows that there is no algorithm for deciding whether a given FOL sentence is a consequence of a first-order axiomatization of Peano arithmetic or not. Hence, **PA** is an example of an undecidable theory. Undecidability arises already for the existential sentences of **PA**, due to the negative answer to Hilbert's tenth problem, whose proof implies that all computably enumerable sets are diophantine sets, and thus definable by existentially quantified formulas (with free variables) of **PA**. Formulas of **PA** with higher quantifier rank (more quantifier alternations) than existential formulas are more expressive, and define sets in the higher levels of the arithmetical hierarchy.

### Nonstandard models

Although the usual natural numbers satisfy the axioms of PA, there are other models as well (called "non-standard models"); the compactness theorem implies that the existence of nonstandard elements cannot be excluded in first-order logic. The upward Löwenheim–Skolem theorem shows that there are nonstandard models of PA of all infinite cardinalities. This is not the case for the original (second-order) Peano axioms, which have only one model, up to isomorphism. This illustrates one way the first-order system PA is weaker than the second-order Peano axioms.

When interpreted as a proof within a first-order set theory, such as ZFC, Dedekind's categoricity proof for PA shows that each model of set theory has a unique model of the Peano axioms, up to isomorphism, that embeds as an initial segment of all other models of PA contained within that model of set theory. In the standard model of set theory, this smallest model of PA is the standard model of PA; however, in a nonstandard model of set theory, it may be a nonstandard model of PA. This situation cannot be avoided with any first-order formalization of set theory.

It is natural to ask whether a countable nonstandard model can be explicitly constructed. The answer is affirmative as Skolem in 1933 provided an explicit construction of such a nonstandard model. On the other hand, Tennenbaum's theorem, proved in 1959, shows that there is no countable nonstandard model of PA in which either the addition or multiplication operation is computable. This result shows it is difficult to be completely explicit in describing the addition and multiplication operations of a countable nonstandard model of PA. There is only one possible order type of a countable nonstandard model. Letting *ω* be the order type of the natural numbers, *ζ* be the order type of the integers, and *η* be the order type of the rationals, the order type of any countable nonstandard model of PA is *ω* + *ζ*·*η*, which can be visualized as a copy of the natural numbers followed by a dense linear ordering of copies of the integers.

#### Overspill

A **cut** in a nonstandard model *M* is a nonempty subset *C* of *M* so that *C* is downward closed (*x* < *y* and *y* ∈ *C* ⇒ *x* ∈ *C*) and *C* is closed under successor. A **proper cut** is a cut that is a proper subset of *M*. Each nonstandard model has many proper cuts, including one that corresponds to the standard natural numbers. However, the induction scheme in Peano arithmetic prevents any proper cut from being definable. The overspill lemma, first proved by Abraham Robinson, formalizes this fact.

**Overspill lemma**—Let *M* be a nonstandard model of PA and let *C* be a proper cut of *M*. Suppose that ${\bar {a}}$ is a tuple of elements of *M* and $\varphi (x,{\bar {a}})$ is a formula in the language of arithmetic so that

$M\vDash \varphi (b,{\bar {a}})$

for all

b

∈

C

.

Then there is a *c* in *M* that is greater than every element of *C* such that

$M\vDash \varphi (c,{\bar {a}}).$
