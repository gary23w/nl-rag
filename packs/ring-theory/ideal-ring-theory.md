---
title: "Ideal (ring theory)"
source: https://en.wikipedia.org/wiki/Ideal_(ring_theory)
domain: ring-theory
license: CC-BY-SA-4.0
tags: ring theory, commutative ring, ring ideal, polynomial ring
fetched: 2026-07-02
---

# Ideal (ring theory)

In mathematics, and more specifically in ring theory, an **ideal** of a ring is a special subset of its elements. Ideals generalize certain subsets of the integers, such as the even numbers or the multiples of 3. Addition and subtraction of even numbers preserves evenness, and multiplying an even number by any integer (even or odd) results in an even number; these closure and absorption properties are the defining properties of an ideal. An ideal can be used to construct a quotient ring in a way similar to how, in group theory, a normal subgroup can be used to construct a quotient group.

Among the integers, the ideals correspond one-for-one with the non-negative integers: in this ring, every ideal is a principal ideal consisting of the multiples of a single non-negative number. However, in other rings, the ideals may not correspond directly to the ring elements, and certain properties of integers, when generalized to rings, attach more naturally to the ideals than to the elements of the ring. For instance, the prime ideals of a ring are analogous to prime numbers, and the Chinese remainder theorem can be generalized to ideals. There is a version of unique prime factorization for the ideals of a Dedekind domain (a type of ring important in number theory).

The related, but distinct, concept of an ideal in order theory is derived from the notion of an ideal in ring theory. A fractional ideal is a generalization of an ideal, and the usual ideals are sometimes called **integral ideals** for clarity.

## History

Ernst Kummer invented the concept of ideal numbers to serve as the "missing" factors in number rings in which unique factorization fails; here the word "ideal" is in the sense of existing in imagination only, in analogy with "ideal" objects in geometry such as points at infinity. In 1876, Richard Dedekind replaced Kummer's undefined concept by concrete sets of numbers, sets that he called ideals, in the third edition of Dirichlet's book *Vorlesungen über Zahlentheorie*, to which Dedekind had added many supplements. Later the notion was extended beyond number rings to the setting of polynomial rings and other commutative rings by David Hilbert and especially Emmy Noether.

## Definitions

Given a ring R , a **left ideal** is a subset I of R that is a subgroup of the additive group of R that is closed under left multiplication by elements of ⁠ R ⁠; that is, $0\in I$ and for every $r\in R$ and every ⁠ $x,y\in I$ ⁠, one has

- ⁠ $x+y\in I$ ⁠
- ⁠ $-x\in I$ ⁠
- ⁠ $rx\in I$ ⁠.

In other words, a left ideal is a left submodule of R , considered as a left module over itself.

A **right ideal** is defined similarly, with the condition $rx\in I$ replaced by ⁠ $xr\in I$ ⁠. A **two-sided ideal** is a left ideal that is also a right ideal.

If the ring is commutative, the definitions of left, right, and two-sided ideal coincide, and one talks simply of an **ideal**. In the non-commutative case, "ideal" is often used instead of "two-sided ideal".

Since an ideal I is an abelian subgroup, the relation between ⁠ x ⁠ and ⁠ y ⁠ defined by

$x-y\in I$

is an equivalence relation on R , and the set of equivalence classes is an abelian group denoted ⁠ $R/I$ ⁠ and called the *quotient* of R by I . If I is a left or a right ideal, the quotient ⁠ $R/I$ ⁠ is a left or right ⁠ R ⁠-module, respectively.

If the ideal I is two-sided, the quotient $R/I$ is a ring, and the function

$R\to R/I$

that associates to each element of R its equivalence class is a surjective ring homomorphism that has the ideal as its kernel. Conversely, the kernel of a ring homomorphism is a two-sided ideal. Therefore, *the two-sided ideals are exactly the kernels of ring homomorphisms.*

### Notes on convention

Some authors do not require a ring to have the multiplicative identity; for these authors, the term "ring" refers to what others call a "rng". For a rng R , a **left ideal** I is a subrng with the additional property that $rx$ is in I for every $r\in R$ and every $x\in I$ . (Right and two-sided ideals are defined similarly.) For a ring, an ideal I (say a left ideal) is rarely a subring; since a subring shares the same multiplicative identity with the ambient ring R , if I were a subring, for every $r\in R$ , we have $r=r1\in I;$ i.e., $I=R$ .

The notion of an ideal does not involve associativity; thus, an ideal is also defined for non-associative rings.

For algebras, we additionally assume that an ideal is a linear subspace. If a k -algebra A is unital, then any ring-ideal $I\subseteq A$ is an algebra-ideal, since $ax+by=(a1)x+(b1)y\in I$ when $x,y\in I$ and $a,b\in k$ . For non-unital algebras, there can exist ring-ideals that are not algebra-ideals, for example if $xy=0$ for all $x,y\in A$ , then ring-ideals of A are subrings of A , while algebra-ideals of A are linear subspaces of A .

Traditionally, ideals are denoted using Fraktur lower-case letters, generally the first few letters ( ${\mathfrak {a}},{\mathfrak {b}},{\mathfrak {c}}$ , etc.) for generic ideals, ${\mathfrak {m}}$ for maximal ideals, and ${\mathfrak {p}}$ for prime ideals. In modern texts, capital letters, like I or J (or M and P for maximal and prime ideals, respectively) are also commonly used.

## Examples and properties

(For the sake of brevity, some results are stated only for left ideals but are usually also true for right ideals with appropriate notation changes.)

- In a ring *R*, the set *R* itself forms a two-sided ideal of *R* called the **unit ideal**. It is often also denoted by $(1)$ since it is precisely the two-sided ideal generated (see below) by the unity ⁠ $1_{R}$ ⁠. Also, the set $\{0_{R}\}$ consisting of only the additive identity 0*R* forms a two-sided ideal called the **zero ideal** and is denoted by ⁠ $(0)$ ⁠. Every (left, right or two-sided) ideal contains the zero ideal and is contained in the unit ideal.
- An (left, right or two-sided) ideal that is not the unit ideal is called a **proper ideal** (as it is a proper subset). Note: a left ideal ${\mathfrak {a}}$ is proper if and only if it does not contain a unit element, since if $u\in {\mathfrak {a}}$ is a unit element, then $r=(ru^{-1})u\in {\mathfrak {a}}$ for every ⁠ $r\in R$ ⁠. Typically there are plenty of proper ideals. In fact, if *R* is a skew-field, then $(0),(1)$ are its only ideals and conversely: that is, a nonzero ring *R* is a skew-field if $(0),(1)$ are the only left (or right) ideals. (Proof: if x is a nonzero element, then the principal left ideal $Rx$ (see below) is nonzero and thus $Rx=(1)$ ; i.e., $yx=1$ for some nonzero ⁠ y ⁠. Likewise, $zy=1$ for some nonzero z . Then $z=z(yx)=(zy)x=x$ .)
- The even integers form an ideal in the ring $\mathbb {Z}$ of all integers, since the sum of any two even integers is even, and the product of any integer with an even integer is also even; this ideal is usually denoted by ⁠ $2\mathbb {Z}$ ⁠. More generally, the set of all integers divisible by a fixed integer n is an ideal denoted ⁠ $n\mathbb {Z}$ ⁠. In fact, every non-zero ideal of the ring $\mathbb {Z}$ is generated by its smallest positive element, as a consequence of Euclidean division, so $\mathbb {Z}$ is a principal ideal domain.
- The set of all polynomials with real coefficients that are divisible by the polynomial $x^{2}+1$ is an ideal in the ring of all real-coefficient polynomials ⁠ $\mathbb {R} [x]$ ⁠.
- Take a ring R and positive integer ⁠ n ⁠. For each ⁠ $1\leq i\leq n$ ⁠, the set of all $n\times n$ matrices with entries in R whose i -th row is zero is a right ideal in the ring $M_{n}(R)$ of all $n\times n$ matrices with entries in ⁠ R ⁠. It is not a left ideal. Similarly, for each ⁠ $1\leq j\leq n$ ⁠, the set of all $n\times n$ matrices whose j -th *column* is zero is a left ideal but not a right ideal.
- The ring $C(\mathbb {R} )$ of all continuous functions f from $\mathbb {R}$ to $\mathbb {R}$ under pointwise multiplication contains the ideal of all continuous functions f such that ⁠ $f(1)=0$ ⁠. Another ideal in $C(\mathbb {R} )$ is given by those functions that vanish for large enough arguments, i.e. those continuous functions f for which there exists a number $L>0$ such that $f(x)=0$ whenever ⁠ $\vert x\vert >L$ ⁠.
- A ring is called a simple ring if it is nonzero and has no two-sided ideals other than ⁠ $(0),(1)$ ⁠. Thus, a skew-field is simple and a simple commutative ring is a field. The matrix ring over a skew-field is a simple ring.
- If $f:R\to S$ is a ring homomorphism, then the kernel $\ker(f)=f^{-1}(0_{S})$ is a two-sided ideal of ⁠ R ⁠. By definition, ⁠ $f(1_{R})=1_{S}$ ⁠, and thus if S is not the zero ring (so ⁠ $1_{S}\neq 0_{S}$ ⁠), then $\ker(f)$ is a proper ideal. More generally, for each left ideal *I* of *S*, the pre-image $f^{-1}(I)$ is a left ideal. If *I* is a left ideal of *R*, then $f(I)$ is a left ideal of the subring $f(R)$ of *S*: unless *f* is surjective, $f(I)$ need not be an ideal of *S*; see also § Extension and contraction of an ideal.
- **Ideal correspondence**: Given a surjective ring homomorphism ⁠ $f:R\to S$ ⁠, there is a bijective order-preserving correspondence between the left (resp. right, two-sided) ideals of R containing the kernel of f and the left (resp. right, two-sided) ideals of S : the correspondence is given by $I\mapsto f(I)$ and the pre-image ⁠ $J\mapsto f^{-1}(J)$ ⁠. Moreover, for commutative rings, this bijective correspondence restricts to prime ideals, maximal ideals, and radical ideals (see the Types of ideals section for the definitions of these ideals).
- If *M* is a left *R*-module and $S\subset M$ a subset, then the annihilator $\operatorname {Ann} _{R}(S)=\{r\in R\mid rs=0,s\in S\}$ of *S* is a left ideal. Given ideals ${\mathfrak {a}},{\mathfrak {b}}$ of a commutative ring *R*, the *R*-annihilator of $({\mathfrak {b}}+{\mathfrak {a}})/{\mathfrak {a}}$ is an ideal of *R* called the ideal quotient of ${\mathfrak {a}}$ by ${\mathfrak {b}}$ and is denoted by ⁠ $({\mathfrak {a}}:{\mathfrak {b}})$ ⁠; it is an instance of idealizer in commutative algebra.
- Let ${\mathfrak {a}}_{i},i\in S$ be an **ascending chain of left ideals** in a ring *R*; i.e., S is a totally ordered set and ${\mathfrak {a}}_{i}\subset {\mathfrak {a}}_{j}$ for each ⁠ $i<j$ ⁠. Then the union $\textstyle \bigcup _{i\in S}{\mathfrak {a}}_{i}$ is a left ideal of *R*. (Note: this fact remains true even if *R* is without the unity 1.)
- The above fact together with Zorn's lemma proves the following: if $E\subset R$ is a possibly empty subset and ${\mathfrak {a}}_{0}\subset R$ is a left ideal that is disjoint from *E*, then there is an ideal that is maximal among the ideals containing ${\mathfrak {a}}_{0}$ and disjoint from *E*. (Again this is still valid if the ring *R* lacks the unity 1.) When $R\neq 0$ , taking ${\mathfrak {a}}_{0}=(0)$ and ⁠ $E=\{1\}$ ⁠, in particular, there exists a left ideal that is maximal among proper left ideals (often simply called a maximal left ideal); see Krull's theorem for more.
- A left (resp. right, two-sided) ideal generated by a single element *x* is called the principal left (resp. right, two-sided) ideal generated by *x* and is denoted by $Rx$ (resp. ⁠ $xR,RxR$ ⁠). The principal two-sided ideal $RxR$ is often also denoted by ⁠ $(x)$ ⁠ or $\langle x\rangle$ .
- An arbitrary union of ideals need not be an ideal, but the following is still true: given a possibly empty subset *X* of *R*, there is the smallest left ideal containing *X*, called the left ideal generated by *X* and is denoted by ⁠ $RX$ ⁠. Such an ideal exists since it is the intersection of all left ideals containing *X*. Equivalently, $RX$ is the set of all the (finite) left *R*-linear combinations of elements of *X* over *R*: $RX=\{r_{1}x_{1}+\dots +r_{n}x_{n}\mid n\in \mathbb {N} ,r_{i}\in R,x_{i}\in X\}$ (since such a span is the smallest left ideal containing *X*.) A right (resp. two-sided) ideal generated by *X* is defined in the similar way. For "two-sided", one has to use linear combinations from both sides; i.e., $RXR=\{r_{1}x_{1}s_{1}+\dots +r_{n}x_{n}s_{n}\mid n\in \mathbb {N} ,r_{i}\in R,s_{i}\in R,x_{i}\in X\}.$ If $X=\{x_{1},\dots ,x_{n}\}$ is a finite set, then $RXR$ is also written as ⁠ $(x_{1},\dots ,x_{n})$ ⁠ or $\langle x_{1},...,x_{n}\rangle$ . More generally, the two-sided ideal generated by a (finite or infinite) set of indexed ring elements $X=\{x_{i}\}_{i\in I}$ is denoted $(X)=(x_{i})_{i\in I}$ or $\langle X\rangle =\langle x_{i}\rangle _{i\in I}$ .
- There is a bijective correspondence between ideals and congruence relations (equivalence relations that respect the ring structure) on the ring: Given an ideal I of a ring ⁠ R ⁠, let $x\sim y$ if ⁠ $x-y\in I$ ⁠. Then $\sim$ is a congruence relation on ⁠ R ⁠. Conversely, given a congruence relation $\sim$ on ⁠ R ⁠, let ⁠ $I=\{x\in R:x\sim 0\}$ ⁠. Then I is an ideal of ⁠ R ⁠.

## Types of ideals

*To simplify the description all rings are assumed to be commutative. The non-commutative case is discussed in detail in the respective articles.*

Ideals are important because they appear as kernels of ring homomorphisms and allow one to define factor rings. Different types of ideals are studied because they can be used to construct different types of factor rings.

- **Maximal ideal**: A proper ideal I is called a **maximal ideal** if there exists no other proper ideal *J* with I a proper subset of *J*. The factor ring of a maximal ideal is a simple ring in general and is a field for commutative rings.
- **Minimal ideal**: A nonzero ideal is called minimal if it contains no other nonzero ideal.
- **Zero ideal**: the ideal $\{0\}$ .
- **Unit ideal**: the whole ring (being the ideal generated by 1 ).
- **Prime ideal**: A proper ideal I is called a **prime ideal** if for any a and b in ⁠ R ⁠, if $ab$ is in ⁠ I ⁠, then at least one of a and b is in ⁠ I ⁠. The factor ring of a prime ideal is a prime ring in general and is an integral domain for commutative rings.
- **Radical ideal** or semiprime ideal: A proper ideal I is called **radical** or **semiprime** if for any *a* in R , if *a**n* is in I for some *n*, then *a* is in I. The factor ring of a radical ideal is a semiprime ring for general rings, and is a reduced ring for commutative rings.
- **Primary ideal**: An ideal I is called a **primary ideal** if for all *a* and *b* in *R*, if *ab* is in I, then at least one of *a* and *b**n* is in I for some natural number *n*. Every prime ideal is primary, but not conversely. A semiprime primary ideal is prime.
- **Principal ideal**: An ideal generated by *one* element.
- **Finitely generated ideal**: This type of ideal is finitely generated as a module.
- **Primitive ideal**: A left primitive ideal is the annihilator of a simple left module.
- **Irreducible ideal**: An ideal is said to be irreducible if it cannot be written as an intersection of ideals that properly contain it.
- **Comaximal ideals**: Two ideals I, J are said to be **comaximal** if $x+y=1$ for some $x\in I$ and ⁠ $y\in J$ ⁠.
- **Regular ideal**: This term has multiple uses. See the article for a list.
- **Nil ideal**: An ideal is a nil ideal if each of its elements is nilpotent.
- **Nilpotent ideal**: Some power of it is zero.
- **Parameter ideal**: an ideal generated by a system of parameters.
- **Perfect ideal**: A proper ideal I in a Noetherian ring R is called a **perfect ideal** if its grade equals the projective dimension of the associated quotient ring, ⁠ ${\textrm {grade}}(I)={\textrm {proj}}\dim(R/I)$ ⁠. A perfect ideal is unmixed.
- **Unmixed ideal**: A proper ideal I in a Noetherian ring R is called an **unmixed ideal** (in height) if the height of I is equal to the height of every associated prime *P* of $R/I$ . (This is stronger than saying that $R/I$ is equidimensional. See also equidimensional ring.

Two other important terms using "ideal" are not always ideals of their ring. See their respective articles for details:

- **Fractional ideal**: This is usually defined when R is a commutative domain with quotient field K . Despite their names, fractional ideals are not necessarily ideals. A fractional ideal of R is an R -submodule ⁠ I ⁠ of K for which there exists a non-zero $r\in R$ such that $rI\subseteq R$ . If the fractional ideal is contained entirely in R , then it is truly an ideal of R .
- **Invertible ideal**: Usually an invertible ideal *A* is defined as a fractional ideal for which there is another fractional ideal *B* such that *AB* = *BA* = *R*. Some authors may also apply "invertible ideal" to ordinary ring ideals *A* and *B* with *AB* = *BA* = *R* in rings other than domains.

## Ideal operations

The sum and product of ideals are defined as follows. For ${\mathfrak {a}}$ and ⁠ ${\mathfrak {b}}$ ⁠, left (resp. right) ideals of a ring *R*, their sum is

${\mathfrak {a}}+{\mathfrak {b}}:=\{a+b\mid a\in {\mathfrak {a}}{\mbox{ and }}b\in {\mathfrak {b}}\},$

which is a left (resp. right) ideal, and, if ${\mathfrak {a}},{\mathfrak {b}}$ are two-sided,

${\mathfrak {a}}{\mathfrak {b}}:=\{a_{1}b_{1}+\dots +a_{n}b_{n}\mid a_{i}\in {\mathfrak {a}}{\mbox{ and }}b_{i}\in {\mathfrak {b}},i=1,2,\dots ,n;{\mbox{ for }}n=1,2,\dots \},$

i.e. the product is the ideal generated by all products of the form *ab* with *a* in ${\mathfrak {a}}$ and *b* in ⁠ ${\mathfrak {b}}$ ⁠.

Note ${\mathfrak {a}}+{\mathfrak {b}}$ is the smallest left (resp. right) ideal containing both ${\mathfrak {a}}$ and ${\mathfrak {b}}$ (or the union ⁠ ${\mathfrak {a}}\cup {\mathfrak {b}}$ ⁠), while the product ${\mathfrak {a}}{\mathfrak {b}}$ is contained in the intersection of ${\mathfrak {a}}$ and ⁠ ${\mathfrak {b}}$ ⁠.

The distributive law holds for two-sided ideals ⁠ ${\mathfrak {a}},{\mathfrak {b}},{\mathfrak {c}}$ ⁠,

- ⁠ ${\mathfrak {a}}({\mathfrak {b}}+{\mathfrak {c}})={\mathfrak {a}}{\mathfrak {b}}+{\mathfrak {a}}{\mathfrak {c}}$ ⁠,
- ⁠ $({\mathfrak {a}}+{\mathfrak {b}}){\mathfrak {c}}={\mathfrak {a}}{\mathfrak {c}}+{\mathfrak {b}}{\mathfrak {c}}$ ⁠.

If a product is replaced by an intersection, a partial distributive law holds:

${\mathfrak {a}}\cap ({\mathfrak {b}}+{\mathfrak {c}})\supset {\mathfrak {a}}\cap {\mathfrak {b}}+{\mathfrak {a}}\cap {\mathfrak {c}}$

where the equality holds if ${\mathfrak {a}}$ contains ${\mathfrak {b}}$ or ${\mathfrak {c}}$ .

**Remark**: The sum and the intersection of ideals is again an ideal; with these two operations as join and meet, the set of all ideals of a given ring forms a complete modular lattice. The lattice is not, in general, a distributive lattice. The three operations of intersection, sum (or join), and product make the set of ideals of a commutative ring into a quantale.

If ${\mathfrak {a}},{\mathfrak {b}}$ are ideals of a commutative ring *R*, then ${\mathfrak {a}}\cap {\mathfrak {b}}={\mathfrak {a}}{\mathfrak {b}}$ in the following two cases (at least)

- ${\mathfrak {a}}+{\mathfrak {b}}=(1)$
- ${\mathfrak {a}}$ is generated by elements that form a regular sequence modulo ⁠ ${\mathfrak {b}}$ ⁠.

(More generally, the difference between a product and an intersection of ideals is measured by the Tor functor: ⁠ $\operatorname {Tor} _{1}^{R}(R/{\mathfrak {a}},R/{\mathfrak {b}})=({\mathfrak {a}}\cap {\mathfrak {b}})/{\mathfrak {a}}{\mathfrak {b}}$ ⁠.)

An integral domain is called a Dedekind domain if for each pair of ideals ${\mathfrak {a}}\subset {\mathfrak {b}}$ , there is an ideal ${\mathfrak {c}}$ such that ⁠ ${\mathfrak {\mathfrak {a}}}={\mathfrak {b}}{\mathfrak {c}}$ ⁠. It can then be shown that every nonzero ideal of a Dedekind domain can be uniquely written as a product of maximal ideals, a generalization of the fundamental theorem of arithmetic.

## Examples of ideal operations

In $\mathbb {Z}$ we have

$(n)\cap (m)=\operatorname {lcm} (n,m)\mathbb {Z}$

since $(n)\cap (m)$ is the set of integers that are divisible by both n and ⁠ m ⁠.

Let $R=\mathbb {C} [x,y,z,w]$ and let ⁠ ${\mathfrak {a}}=(z,w),{\mathfrak {b}}=(x+z,y+w),{\mathfrak {c}}=(x+z,w)$ ⁠. Then,

- ${\mathfrak {a}}+{\mathfrak {b}}=(z,w,x+z,y+w)=(x,y,z,w)$ and ${\mathfrak {a}}+{\mathfrak {c}}=(z,w,x)$
- ${\mathfrak {a}}{\mathfrak {b}}=(z(x+z),z(y+w),w(x+z),w(y+w))=(z^{2}+xz,zy+wz,wx+wz,wy+w^{2})$
- ${\mathfrak {a}}{\mathfrak {c}}=(xz+z^{2},zw,xw+zw,w^{2})$
- ${\mathfrak {a}}\cap {\mathfrak {b}}={\mathfrak {a}}{\mathfrak {b}}$ while ${\mathfrak {a}}\cap {\mathfrak {c}}=(w,xz+z^{2})\neq {\mathfrak {a}}{\mathfrak {c}}$

In the first computation, we see the general pattern for taking the sum of two finitely generated ideals, it is the ideal generated by the union of their generators. In the last three we observe that products and intersections agree whenever the two ideals intersect in the zero ideal. These computations can be checked using Macaulay2.

## Radical of a ring

Ideals appear naturally in the study of modules, especially in the form of a radical.

For simplicity, we work with commutative rings but, with some changes, the results are also true for non-commutative rings.

Let *R* be a commutative ring. By definition, a primitive ideal of *R* is the annihilator of a (nonzero) simple *R*-module. The Jacobson radical $J=\operatorname {Jac} (R)$ of *R* is the intersection of all primitive ideals. Equivalently,

$J=\bigcap _{{\mathfrak {m}}{\text{ maximal ideals}}}{\mathfrak {m}}.$

Indeed, if M is a simple module and *x* is a nonzero element in *M*, then $Rx=M$ and $R/\operatorname {Ann} (M)=R/\operatorname {Ann} (x)\simeq M$ , meaning $\operatorname {Ann} (M)$ is a maximal ideal. Conversely, if ${\mathfrak {m}}$ is a maximal ideal, then ${\mathfrak {m}}$ is the annihilator of the simple *R*-module ⁠ $R/{\mathfrak {m}}$ ⁠. There is also another characterization (the proof is not hard):

$J=\{x\in R\mid 1-yx\,{\text{ is a unit element for every }}y\in R\}.$

For a not-necessarily-commutative ring, it is a general fact that $1-yx$ is a unit element if and only if $1-xy$ is (see the link) and so this last characterization shows that the radical can be defined both in terms of left and right primitive ideals.

The following simple but important fact (Nakayama's lemma) is built-in to the definition of a Jacobson radical: if *M* is a module such that ⁠ $JM=M$ ⁠, then *M* does not admit a maximal submodule, since if there is a maximal submodule ⁠ $L\subsetneq M$ ⁠, $J\cdot (M/L)=0$ and so ⁠ $M=JM\subset L\subsetneq M$ ⁠, a contradiction. Since a nonzero finitely generated module admits a maximal submodule, in particular, one has:

If

$JM=M$

and

M

is finitely generated, then

⁠

$M=0$

⁠

.

A maximal ideal is a prime ideal and so one has

$\operatorname {nil} (R)=\bigcap _{{\mathfrak {p}}{\text{ prime ideals }}}{\mathfrak {p}}\subset \operatorname {Jac} (R)$

where the intersection on the left is called the nilradical of *R*. As it turns out, $\operatorname {nil} (R)$ is also the set of nilpotent elements of *R*.

If *R* is an Artinian ring, then $\operatorname {Jac} (R)$ is nilpotent and ⁠ $\operatorname {nil} (R)=\operatorname {Jac} (R)$ ⁠. (Proof: first note the DCC implies $J^{n}=J^{n+1}$ for some *n*. If (DCC) ${\mathfrak {a}}\supsetneq \operatorname {Ann} (J^{n})$ is an ideal properly minimal over the latter, then $J\cdot ({\mathfrak {a}}/\operatorname {Ann} (J^{n}))=0$ . That is, ⁠ $J^{n}{\mathfrak {a}}=J^{n+1}{\mathfrak {a}}=0$ ⁠, a contradiction.)

## Extension and contraction of an ideal

Let A and B be two commutative rings, and let $f:A\to B$ be a ring homomorphism. If ${\mathfrak {a}}$ is an ideal in A , then $f({\mathfrak {a}})$ need not be an ideal in B (e.g. take f to be the inclusion of the ring of integers $\mathbb {Z}$ into the field of rationals $\mathbb {Q}$ ). The **extension** ${\mathfrak {a}}^{e}$ of ${\mathfrak {a}}$ in B is defined to be the ideal in B generated by ⁠ $f({\mathfrak {a}})$ ⁠. Explicitly,

${\mathfrak {a}}^{e}=f({\mathfrak {a}})B={\Big \{}\sum y_{i}f(x_{i}):x_{i}\in {\mathfrak {a}},y_{i}\in B{\Big \}}.$

By abuse of notation, ${\mathfrak {a}}B$ is another common notation for this ideal extension.

If ${\mathfrak {b}}$ is an ideal of B , then $f^{-1}({\mathfrak {b}})$ is always an ideal of A , called the **contraction** ${\mathfrak {b}}^{c}$ of ${\mathfrak {b}}$ to A .

Assuming $f:A\to B$ is a ring homomorphism, ${\mathfrak {a}}$ is an ideal in A , ${\mathfrak {b}}$ is an ideal in B , then:

- ${\mathfrak {b}}$ is prime in B $\Rightarrow$ ${\mathfrak {b}}^{c}$ is prime in A ,
- ${\mathfrak {a}}^{ec}\supseteq {\mathfrak {a}},$
- ${\mathfrak {b}}^{ce}\subseteq {\mathfrak {b}}.$

It is false, in general, that ${\mathfrak {a}}$ being prime (or maximal) in A implies that ${\mathfrak {a}}^{e}$ is prime (or maximal) in B . Many classic examples of this stem from algebraic number theory. For example, consider the embedding $\mathbb {Z} \to \mathbb {Z} \left\lbrack i\right\rbrack .$ In $B=\mathbb {Z} \left\lbrack i\right\rbrack$ , the element 2 factors as $2=(1+i)(1-i)$ where (one can show) neither of $1+i,1-i$ are units in B . So $(2)^{e}$ is not prime in B (and therefore not maximal, as well). Indeed, $(1\pm i)^{2}=\pm 2i$ shows that ⁠ $(1+i)=((1-i)-(1-i)^{2})$ ⁠, ⁠ $(1-i)=((1+i)-(1+i)^{2})$ ⁠, and therefore ⁠ $(2)^{e}=(1+i)^{2}$ ⁠.

On the other hand, if f is surjective and ${\mathfrak {a}}\supseteq \ker f$ then:

- ${\mathfrak {a}}^{ec}={\mathfrak {a}}$ and ${\mathfrak {b}}^{ce}={\mathfrak {b}},$
- ${\mathfrak {a}}$ is a prime ideal in A $\Leftrightarrow$ ${\mathfrak {a}}^{e}$ is a prime ideal in B ,
- ${\mathfrak {a}}$ is a maximal ideal in A $\Leftrightarrow$ ${\mathfrak {a}}^{e}$ is a maximal ideal in B .

**Remark**: Let K be a field extension of L , and let B and A be the rings of integers of K and L , respectively. Then B is an integral extension of A , and we let f be the inclusion map from A to B . The behaviour of a prime ideal ${\mathfrak {a}}={\mathfrak {p}}$ of A under extension is one of the central problems of algebraic number theory.

The following is sometimes useful: a prime ideal ${\mathfrak {p}}$ is a contraction of a prime ideal if and only if ${\mathfrak {p}}={\mathfrak {p}}^{ec}$ . (Proof: Assuming the latter, note ${\mathfrak {p}}^{e}B_{\mathfrak {p}}=B_{\mathfrak {p}}\Rightarrow {\mathfrak {p}}^{e}$ intersects $A-{\mathfrak {p}}$ , a contradiction. Now, the prime ideals of $B_{\mathfrak {p}}$ correspond to those in B that are disjoint from $A-{\mathfrak {p}}$ . Hence, there is a prime ideal ${\mathfrak {q}}$ of B , disjoint from $A-{\mathfrak {p}}$ , such that ${\mathfrak {q}}B_{\mathfrak {p}}$ is a maximal ideal containing ${\mathfrak {p}}^{e}B_{\mathfrak {p}}$ . One then checks that ${\mathfrak {q}}$ lies over ${\mathfrak {p}}$ . The converse is obvious.)

## Generalizations

Ideals can be generalized to any monoid object ⁠ $(R,\otimes )$ ⁠, where R is the object where the monoid structure has been forgotten. A **left ideal** of R is a subobject I that "absorbs multiplication from the left by elements of ⁠ R ⁠"; that is, I is a **left ideal** if it satisfies the following two conditions:

1. I is a subobject of R
2. For every $r\in (R,\otimes )$ and every ⁠ $x\in (I,\otimes )$ ⁠, the product $r\otimes x$ is in ⁠ $(I,\otimes )$ ⁠.

A **right ideal** is defined with the condition "⁠ $r\otimes x\in (I,\otimes )$ ⁠" replaced by "'⁠ $x\otimes r\in (I,\otimes )$ ⁠". A **two-sided ideal** is a left ideal that is also a right ideal, and is sometimes simply called an ideal. When R is a commutative monoid object respectively, the definitions of left, right, and two-sided ideal coincide, and the term **ideal** is used alone.
