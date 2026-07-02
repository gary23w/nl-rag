---
title: "Symbolic method (combinatorics)"
source: https://en.wikipedia.org/wiki/Symbolic_method_(combinatorics)
domain: generating-functions-deep
license: CC-BY-SA-4.0
tags: generating function, formal power series, umbral calculus, lagrange inversion theorem
fetched: 2026-07-02
---

# Symbolic method (combinatorics)

In combinatorics, the **symbolic method** is a technique for counting combinatorial objects. It uses the internal structure of the objects to derive formulas for their generating functions. The method is mostly associated with Philippe Flajolet and is detailed in Part A of his book with Robert Sedgewick, *Analytic Combinatorics*, while the rest of the book explains how to use complex analysis in order to get asymptotic and probabilistic results on the corresponding generating functions.

During two centuries, generating functions were popping up via the corresponding recurrences on their coefficients (as can be seen in the seminal works of Bernoulli, Euler, Arthur Cayley, Schröder, Ramanujan, Riordan, Knuth, Comtet, etc.). It was then slowly realized that the generating functions were capturing many other facets of the initial discrete combinatorial objects, and that this could be done in a more direct formal way: The recursive nature of some combinatorial structures translates, via some isomorphisms, into noteworthy identities on the corresponding generating functions. Following the works of Pólya, further advances were thus done in this spirit in the 1970s with generic uses of languages for specifying combinatorial classes and their generating functions, as found in works by Foata and Schützenberger on permutations, Bender and Goldman on prefabs, and Joyal on combinatorial species.

Note that this symbolic method in enumeration is unrelated to "Blissard's symbolic method", which is just another old name for umbral calculus.

The symbolic method in combinatorics constitutes the first step of many analyses of combinatorial structures, which can then lead to fast computation schemes, to asymptotic properties and limit laws, to random generation, all of them being suitable to automatization via computer algebra.

## Classes of combinatorial structures

Consider the problem of distributing objects given by a generating function into a set of *n* slots, where a permutation group *G* of degree *n* acts on the slots to create an equivalence relation of filled slot configurations, and asking about the generating function of the configurations by weight of the configurations with respect to this equivalence relation, where the weight of a configuration is the sum of the weights of the objects in the slots. We will first explain how to solve this problem in the labelled and the unlabelled case and use the solution to motivate the creation of classes of combinatorial structures.

The Pólya enumeration theorem solves this problem in the unlabelled case. Let *f*(*z*) be the ordinary generating function (OGF) of the objects, then the OGF of the configurations is given by the substituted cycle index

$Z(G)(f(z),f(z^{2}),\ldots ,f(z^{n})).$

In the labelled case we use an exponential generating function (EGF) *g*(*z*) of the objects and apply the Labelled enumeration theorem, which says that the EGF of the configurations is given by

${\frac {g(z)^{n}}{|G|}}.$

We are able to enumerate filled slot configurations using either Pólya enumeration theorem in the unlabelled case or the labelled enumeration theorem in the labelled case. We now ask about the generating function of configurations obtained when there is more than one set of slots, with a permutation group acting on each. Clearly the orbits do not intersect and we may add the respective generating functions. Suppose, for example, that we want to enumerate unlabelled sequences of length two or three of some objects contained in a set *X*. There are two sets of slots, the first one containing two slots, and the second one, three slots. The group acting on the first set is the full symmetric group $S_{2}$ , which in symbolic combinatorics is traditionally denoted $E_{2}$ . The group acting on the second set is, analogously, $S_{3}=E_{3}$ . We represent this by the following formal power series in *X*:

$X^{2}/E_{2}\;+\;X^{3}/E_{3}$

where the term $X^{n}/G$ is used to denote the set of orbits under *G* and $X^{n}=X\times \cdots \times X$ , which denotes in the obvious way the process of distributing the objects from *X* with repetition into the *n* slots. Similarly, consider the labelled problem of creating cycles of arbitrary length from a set of labelled objects *X*. This yields the following series of actions of cyclic groups:

$X/C_{1}\;+\;X^{2}/C_{2}\;+\;X^{3}/C_{3}\;+\;X^{4}/C_{4}\;+\cdots .$

Clearly we can assign meaning to any such power series of quotients (orbits) with respect to permutation groups, where we restrict the groups of degree *n* to the conjugacy classes $\operatorname {Cl} (S_{n})$ of the symmetric group $S_{n}$ , which form a unique factorization domain. (The orbits with respect to two groups from the same conjugacy class are isomorphic.) This motivates the following definition.

A class ${\mathcal {C}}\in \mathbb {N} [{\mathfrak {M}}]$ of combinatorial structures is a formal series

${\mathcal {C}}=\sum _{n\geq 1}\sum _{G\in \operatorname {Cl} (S_{n})}c_{G}(X^{n}/G)$

where ${\mathfrak {M}}$ (the "M" is for "molecules") is the set of primes of the UFD $\{\operatorname {Cl} (S_{n})\}_{n\geq 1}$ and $c_{G}\in \mathbb {N} .$

In the following we will simplify our notation a bit and write e.g.

$E_{2}+E_{3}{\text{ and }}C_{1}+C_{2}+C_{3}+\cdots .$

for the classes mentioned above.

## The Flajolet–Sedgewick fundamental theorem

A theorem in the Flajolet–Sedgewick theory of symbolic combinatorics treats the enumeration problem of labelled and unlabelled combinatorial classes by means of the creation of symbolic operators that make it possible to translate equations involving combinatorial structures directly (and automatically) into equations in the generating functions of these structures.

Let ${\mathcal {C}}\in \mathbb {N} [{\mathfrak {A}}]$ be a class of combinatorial structures. The OGF $F(z)$ of ${\mathcal {C}}(X)$ where *X* has OGF $f(z)$ and the EGF $G(z)$ of ${\mathcal {C}}(X)$ where *X* is labelled with EGF $g(z)$ are given by

$F(z)=\sum _{n\geq 1}\sum _{G\in \operatorname {Cl} (S_{n})}c_{G}Z(G)(f(z),f(z^{2}),\ldots ,f(z^{n}))$

and

$G(z)=\sum _{n\geq 1}\left(\sum _{G\in \operatorname {Cl} (S_{n})}{\frac {c_{G}}{|G|}}\right)g(z)^{n}.$

In the labelled case we have the additional requirement that *X* not contain elements of size zero. It will sometimes prove convenient to add one to $G(z)$ to indicate the presence of one copy of the empty set. It is possible to assign meaning to both ${\mathcal {C}}\in \mathbb {Z} [{\mathfrak {A}}]$ (the most common example is the case of unlabelled sets) and ${\mathcal {C}}\in \mathbb {Q} [{\mathfrak {A}}].$ To prove the theorem simply apply PET (Pólya enumeration theorem) and the labelled enumeration theorem.

The power of this theorem lies in the fact that it makes it possible to construct operators on generating functions that represent combinatorial classes. A structural equation between combinatorial classes thus translates directly into an equation in the corresponding generating functions. Moreover, in the labelled case it is evident from the formula that we may replace $g(z)$ by the atom *z* and compute the resulting operator, which may then be applied to EGFs. We now proceed to construct the most important operators. The reader may wish to compare with the data on the cycle index page.

### The sequence operator SEQ

This operator corresponds to the class

$L={\frac {1}{1-X}}=1+X+X^{2}+X^{3}+\cdots$

and represents sequences, i.e. the slots are not being permuted and there is exactly one empty sequence. We have

$F(z)=1+\sum _{n\geq 1}Z(1)(f(z),f(z^{2}),\ldots ,f(z^{n}))=1+\sum _{n\geq 1}f(z)^{n}={\frac {1}{1-f(z)}}$

and

$G(z)=1+\sum _{n\geq 1}g(z)^{n}={\frac {1}{1-g(z)}}.$

### The cycle operator CYC

This operator corresponds to the class

$C=C_{1}+C_{2}+C_{3}+\cdots$

i.e., cycles containing at least one object. We have

$F(z)=\sum _{n\geq 1}Z(C_{n})(f(z),f(z^{2}),\ldots ,f(z^{n}))=\sum _{n\geq 1}{\frac {1}{n}}\sum _{d\mid n}\varphi (d)f(z^{d})^{n/d}$

or

$F(z)=\sum _{k\geq 1}\varphi (k)\sum _{m\geq 1}{\frac {1}{km}}f(z^{k})^{m}=\sum _{k\geq 1}{\frac {\varphi (k)}{k}}\log {\frac {1}{1-f(z^{k})}}$

and

$G(z)=\sum _{n\geq 1}\left({\frac {1}{|C_{n}|}}\right)g(z)^{n}=\log {\frac {1}{1-g(z)}}.$

This operator, together with the set operator SET, and their restrictions to specific degrees are used to compute random permutation statistics. There are two useful restrictions of this operator, namely to even and odd cycles.

The labelled even cycle operator CYCeven is

$C_{2}+C_{4}+C_{6}+\cdots$

which yields

$G(z)=\sum _{n\geq 1}\left({\frac {1}{|C_{2n}|}}\right)g(z)^{2n}={\frac {1}{2}}\log {\frac {1}{1-g(z)^{2}}}.$

This implies that the labelled odd cycle operator CYCodd

$C_{1}+C_{3}+C_{5}+\cdots$

is given by

$G(z)=\log {\frac {1}{1-g(z)}}-{\frac {1}{2}}\log {\frac {1}{1-g(z)^{2}}}={\frac {1}{2}}\log {\frac {1+g(z)}{1-g(z)}}.$

### The multiset/set operator MSET/SET

The series is

$E=1+E_{1}+E_{2}+E_{3}+\cdots$

i.e., the symmetric group $S_{n}=E_{n}$ is applied to the *n*th slot. This creates multisets in the unlabelled case and sets in the labelled case (there are no multisets in the labelled case because the labels distinguish multiple instances of the same object from the set being put into different slots). We include the empty set in both the labelled and the unlabelled case.

The unlabelled case is done using the function

$M(f(z),y)=\sum _{n\geq 0}y^{n}Z(E_{n})(f(z),f(z^{2}),\ldots ,f(z^{n}))$

so that

${\mathfrak {M}}(f(z))=M(f(z),1).$

Evaluating $M(f(z),1)$ we obtain

$F(z)=\exp \left(\sum _{\ell \geq 1}{\frac {f(z^{\ell })}{\ell }}\right).$

For the labelled case we have

$G(z)=1+\sum _{n\geq 1}\left({\frac {1}{|S_{n}|}}\right)g(z)^{n}=\sum _{n\geq 0}{\frac {g(z)^{n}}{n!}}=\exp g(z).$

In the labelled case we denote the operator by SET, and in the unlabelled case, by MSET. This is because in the labeled case there are no multisets (the labels distinguish the constituents of a compound combinatorial class) whereas in the unlabeled case there are multisets and sets, with the latter being given by

$F(z)=\exp \left(\sum _{\ell \geq 1}(-1)^{\ell -1}{\frac {f(z^{\ell })}{\ell }}\right).$

## Procedure

Typically, one starts with the *neutral class* ${\mathcal {E}}$ , containing a single object of size 0 (the *neutral object*, often denoted by $\epsilon$ ), and one or more *atomic classes* ${\mathcal {Z}}$ , each containing a single object of size 1. Next, set-theoretic relations involving various simple operations, such as disjoint unions, products, sets, sequences, and multisets define more complex classes in terms of the already defined classes. These relations may be recursive. The elegance of symbolic combinatorics lies in that the set theoretic, or *symbolic*, relations translate directly into *algebraic* relations involving the generating functions.

In this article, we will follow the convention of using script uppercase letters to denote combinatorial classes and the corresponding plain letters for the generating functions (so the class ${\mathcal {A}}$ has generating function $A(z)$ ).

There are two types of generating functions commonly used in symbolic combinatorics—ordinary generating functions, used for combinatorial classes of unlabelled objects, and exponential generating functions, used for classes of labelled objects.

It is trivial to show that the generating functions (either ordinary or exponential) for ${\mathcal {E}}$ and ${\mathcal {Z}}$ are $E(z)=1$ and $Z(z)=z$ , respectively. The disjoint union is also simple — for disjoint sets ${\mathcal {B}}$ and ${\mathcal {C}}$ , ${\mathcal {A}}={\mathcal {B}}\cup {\mathcal {C}}$ implies $A(z)=B(z)+C(z)$ . The relations corresponding to other operations depend on whether we are talking about labelled or unlabelled structures (and ordinary or exponential generating functions).

## Combinatorial sum

The restriction of unions to disjoint unions is an important one; however, in the formal specification of symbolic combinatorics, it is too much trouble to keep track of which sets are disjoint. Instead, we make use of a construction that guarantees there is no intersection (*be careful, however; this affects the semantics of the operation as well*). In defining the *combinatorial sum* of two sets ${\mathcal {A}}$ and ${\mathcal {B}}$ , we mark members of each set with a distinct marker, for example $\circ$ for members of ${\mathcal {A}}$ and $\bullet$ for members of ${\mathcal {B}}$ . The combinatorial sum is then:

${\mathcal {A}}+{\mathcal {B}}=({\mathcal {A}}\times \{\circ \})\cup ({\mathcal {B}}\times \{\bullet \})$

This is the operation that formally corresponds to addition.

## Unlabelled structures

With unlabelled structures, an ordinary generating function (OGF) is used. The OGF of a sequence $A_{n}$ is defined as

$A(x)=\sum _{n=0}^{\infty }A_{n}x^{n}$

### Product

The product of two combinatorial classes ${\mathcal {A}}$ and ${\mathcal {B}}$ is specified by defining the size of an ordered pair as the sum of the sizes of the elements in the pair. Thus we have for $a\in {\mathcal {A}}$ and $b\in {\mathcal {B}}$ , $|(a,b)|=|a|+|b|$ . This should be a fairly intuitive definition. We now note that the number of elements in ${\mathcal {A}}\times {\mathcal {B}}$ of size *n* is

$\sum _{k=0}^{n}A_{k}B_{n-k}.$

Using the definition of the OGF and some elementary algebra, we can show that

${\mathcal {A}}={\mathcal {B}}\times {\mathcal {C}}$

implies

$A(z)=B(z)\cdot C(z).$

### Sequence

The *sequence construction*, denoted by ${\mathcal {A}}={\mathfrak {G}}\{{\mathcal {B}}\}$ is defined as

${\mathfrak {G}}\{{\mathcal {B}}\}={\mathcal {E}}+{\mathcal {B}}+({\mathcal {B}}\times {\mathcal {B}})+({\mathcal {B}}\times {\mathcal {B}}\times {\mathcal {B}})+\cdots .$

In other words, a sequence is the neutral element, or an element of ${\mathcal {B}}$ , or an ordered pair, ordered triple, etc. This leads to the relation

$A(z)=1+B(z)+B(z)^{2}+B(z)^{3}+\cdots ={\frac {1}{1-B(z)}}.$

### Set

The *set* (or *powerset*) *construction*, denoted by ${\mathcal {A}}={\mathfrak {P}}\{{\mathcal {B}}\}$ is defined as

${\mathfrak {P}}\{{\mathcal {B}}\}=\prod _{\beta \in {\mathcal {B}}}({\mathcal {E}}+\{\beta \}),$

which leads to the relation

${\begin{aligned}A(z)&{}=\prod _{\beta \in {\mathcal {B}}}(1+z^{|\beta |})\\&{}=\prod _{n=1}^{\infty }(1+z^{n})^{B_{n}}\\&{}=\exp \left(\ln \prod _{n=1}^{\infty }(1+z^{n})^{B_{n}}\right)\\&{}=\exp \left(\sum _{n=1}^{\infty }B_{n}\ln(1+z^{n})\right)\\&{}=\exp \left(\sum _{n=1}^{\infty }B_{n}\cdot \sum _{k=1}^{\infty }{\frac {(-1)^{k-1}z^{nk}}{k}}\right)\\&{}=\exp \left(\sum _{k=1}^{\infty }{\frac {(-1)^{k-1}}{k}}\cdot \sum _{n=1}^{\infty }B_{n}z^{nk}\right)\\&{}=\exp \left(\sum _{k=1}^{\infty }{\frac {(-1)^{k-1}B(z^{k})}{k}}\right),\end{aligned}}$

where the expansion

$\ln(1+u)=\sum _{k=1}^{\infty }{\frac {(-1)^{k-1}u^{k}}{k}}$

was used to go from line 4 to line 5.

### Multiset

The *multiset construction*, denoted ${\mathcal {A}}={\mathfrak {M}}\{{\mathcal {B}}\}$ is a generalization of the set construction. In the set construction, each element can occur zero or one times. In a multiset, each element can appear an arbitrary number of times. Therefore,

${\mathfrak {M}}\{{\mathcal {B}}\}=\prod _{\beta \in {\mathcal {B}}}{\mathfrak {G}}\{\beta \}.$

This leads to the relation

${\begin{aligned}A(z)&{}=\prod _{\beta \in {\mathcal {B}}}(1-z^{|\beta |})^{-1}\\&{}=\prod _{n=1}^{\infty }(1-z^{n})^{-B_{n}}\\&{}=\exp \left(\ln \prod _{n=1}^{\infty }(1-z^{n})^{-B_{n}}\right)\\&{}=\exp \left(\sum _{n=1}^{\infty }-B_{n}\ln(1-z^{n})\right)\\&{}=\exp \left(\sum _{k=1}^{\infty }{\frac {B(z^{k})}{k}}\right),\end{aligned}}$

where, similar to the above set construction, we expand $\ln(1-z^{n})$ , swap the sums, and substitute for the OGF of ${\mathcal {B}}$ .

### Other elementary constructions

Other important elementary constructions are:

- the *cycle construction* ( ${\mathfrak {C}}\{{\mathcal {B}}\}$ ), like sequences except that cyclic rotations are not considered distinct
- *pointing* ( $\Theta {\mathcal {B}}$ ), in which each member of B is augmented by a neutral (zero size) pointer to one of its atoms
- *substitution* ( ${\mathcal {B}}\circ {\mathcal {C}}$ ), in which each atom in a member of B is replaced by a member of C.

The derivations for these constructions are too complicated to show here. Here are the results:

| Construction | Generating function |
|---|---|
| ${\mathcal {A}}={\mathfrak {C}}\{{\mathcal {B}}\}$ | $A(z)=\sum _{k=1}^{\infty }{\frac {\phi (k)}{k}}\ln {\frac {1}{1-B(z^{k})}}$ (where $\phi (k)$ is the Euler totient function) |
| ${\mathcal {A}}=\Theta {\mathcal {B}}$ | $A(z)=z{\frac {d}{dz}}B(z)$ |
| ${\mathcal {A}}={\mathcal {B}}\circ {\mathcal {C}}$ | $A(z)=B(C(z))$ |

### Examples

Many combinatorial classes can be built using these elementary constructions. For example, the class of plane trees (that is, trees embedded in the plane, so that the order of the subtrees matters) is specified by the recursive relation

${\mathcal {G}}={\mathcal {Z}}\times \operatorname {SEQ} \{{\mathcal {G}}\}.$

In other words, a tree is a root node of size 1 and a sequence of subtrees. This gives

$G(z)={\frac {z}{1-G(z)}}$

we solve for *G*(*z*) by multiplying $1-G(z)$ to get

$G(z)-G(z)^{2}=z$

subtracting z and solving for G(z) using the quadratic formula gives

$G(z)={\frac {1-{\sqrt {1-4z}}}{2}}.$

Another example (and a classic combinatorics problem) is integer partitions. First, define the class of positive integers ${\mathcal {I}}$ , where the size of each integer is its value:

${\mathcal {I}}={\mathcal {Z}}\times \operatorname {SEQ} \{{\mathcal {Z}}\}$

The OGF of ${\mathcal {I}}$ is then

$I(z)={\frac {z}{1-z}}.$

Now, define the set of partitions ${\mathcal {P}}$ as

${\mathcal {P}}=\operatorname {MSET} \{{\mathcal {I}}\}.$

The OGF of ${\mathcal {P}}$ is

$P(z)=\exp \left(I(z)+{\frac {1}{2}}I(z^{2})+{\frac {1}{3}}I(z^{3})+\cdots \right).$

Unfortunately, there is no closed form for $P(z)$ ; however, the OGF can be used to derive a recurrence relation, or using more advanced methods of analytic combinatorics, calculate the asymptotic behavior of the counting sequence.

### Specification and specifiable classes

The elementary constructions mentioned above allow us to define the notion of *specification*. This specification allows us to use a set of recursive equations, with multiple combinatorial classes.

Formally, a specification for a set of combinatorial classes $({\mathcal {A}}_{1},\dots ,{\mathcal {A}}_{r})$ is a set of r equations ${\mathcal {A}}_{i}=\Phi _{i}({\mathcal {A}}_{1},\dots ,{\mathcal {A}}_{r})$ , where $\Phi _{i}$ is an expression, whose atoms are ${\mathcal {E}},{\mathcal {Z}}$ and the ${\mathcal {A}}_{i}$ 's, and whose operators are the elementary constructions listed above.

A class of combinatorial structures is said to be *constructible* or *specifiable* when it admits a specification.

For example, the set of trees whose leaves' depth is even (respectively, odd) can be defined using the specification with two classes ${\mathcal {A}}_{\text{even}}$ and ${\mathcal {A}}_{\text{odd}}$ . Those classes should satisfy the equation ${\mathcal {A}}_{\text{odd}}={\mathcal {Z}}\times \operatorname {Seq} _{\geq 1}{\mathcal {A}}_{\text{even}}$ and ${\mathcal {A}}_{\text{even}}={\mathcal {Z}}\times \operatorname {Seq} {\mathcal {A}}_{\text{odd}}$ .

## Labelled structures

An object is *weakly labelled* if each of its atoms has a nonnegative integer label, and each of these labels is distinct. An object is (*strongly* or *well*) *labelled*, if furthermore, these labels comprise the consecutive integers $[1\ldots n]$ . *Note: some combinatorial classes are best specified as labelled structures or unlabelled structures, but some readily admit both specifications.* A good example of labelled structures is the class of labelled graphs.

With labelled structures, an exponential generating function (EGF) is used. The EGF of a sequence $A_{n}$ is defined as

$A(x)=\sum _{n=0}^{\infty }A_{n}{\frac {x^{n}}{n!}}.$

### Product

For labelled structures, we must use a different definition for product than for unlabelled structures. In fact, if we simply used the cartesian product, the resulting structures would not even be well labelled. Instead, we use the so-called *labelled product*, denoted ${\mathcal {A}}\star {\mathcal {B}}.$

For a pair $\beta \in {\mathcal {B}}$ and $\gamma \in {\mathcal {C}}$ , we wish to combine the two structures into a single structure. In order for the result to be well labelled, this requires some relabelling of the atoms in $\beta$ and $\gamma$ . We will restrict our attention to relabellings that are consistent with the order of the original labels. Note that there are still multiple ways to do the relabelling; thus, each pair of members determines not a single member in the product, but a set of new members. The details of this construction are found on the page of the Labelled enumeration theorem.

To aid this development, let us define a function, $\rho$ , that takes as its argument a (possibly weakly) labelled object $\alpha$ and relabels its atoms in an order-consistent way so that $\rho (\alpha )$ is well labelled. We then define the labelled product for two objects $\alpha$ and $\beta$ as

$\alpha \star \beta =\{(\alpha ',\beta '):(\alpha ',\beta '){\text{ is well-labelled, }}\rho (\alpha ')=\alpha ,\rho (\beta ')=\beta \}.$

Finally, the labelled product of two classes ${\mathcal {A}}$ and ${\mathcal {B}}$ is

${\mathcal {A}}\star {\mathcal {B}}=\bigcup _{\alpha \in {\mathcal {A}},\beta \in {\mathcal {B}}}(\alpha \star \beta ).$

The EGF can be derived by noting that for objects of size k and $n-k$ , there are ${n \choose k}$ ways to do the relabelling. Therefore, the total number of objects of size n is

$\sum _{k=0}^{n}{n \choose k}A_{k}B_{n-k}.$

This *binomial convolution* relation for the terms is equivalent to multiplying the EGFs,

$A(z)\cdot B(z).$

### Sequence

The *sequence construction* ${\mathcal {A}}={\mathfrak {G}}\{{\mathcal {B}}\}$ is defined similarly to the unlabelled case:

${\mathfrak {G}}\{{\mathcal {B}}\}={\mathcal {E}}+{\mathcal {B}}+({\mathcal {B}}\star {\mathcal {B}})+({\mathcal {B}}\star {\mathcal {B}}\star {\mathcal {B}})+\cdots$

and again, as above,

$A(z)={\frac {1}{1-B(z)}}$

### Set

In labelled structures, a set of k elements corresponds to exactly $k!$ sequences. This is different from the unlabelled case, where some of the permutations may coincide. Thus for ${\mathcal {A}}={\mathfrak {P}}\{{\mathcal {B}}\}$ , we have

$A(z)=\sum _{k=0}^{\infty }{\frac {B(z)^{k}}{k!}}=\exp(B(z))$

### Cycle

Cycles are also easier than in the unlabelled case. A cycle of length k corresponds to k distinct sequences. Thus for ${\mathcal {A}}={\mathfrak {C}}\{{\mathcal {B}}\}$ , we have

$A(z)=\sum _{k=0}^{\infty }{\frac {B(z)^{k}}{k}}=\ln \left({\frac {1}{1-B(z)}}\right).$

### Boxed product

In labelled structures, the min-boxed product ${\mathcal {A}}_{\min }={\mathcal {B}}^{\square }\star {\mathcal {C}}$ is a variation of the original product which requires the element of ${\mathcal {B}}$ in the product with the minimal label. Similarly, we can also define a max-boxed product, denoted by ${\mathcal {A}}_{\max }={\mathcal {B}}^{\blacksquare }\star {\mathcal {C}}$ , by the same manner. Then we have,

$A_{\min }(z)=A_{\max }(z)=\int _{0}^{z}B'(t)C(t)\,dt.$

or equivalently,

$A_{\min }'(t)=A_{\max }'(t)=B'(t)C(t).$

### Example

An increasing Cayley tree is a labelled non-plane and rooted tree whose labels along any branch stemming from the root form an increasing sequence. Then, let ${\mathcal {L}}$ be the class of such trees. The recursive specification is now ${\mathcal {L}}={\mathcal {Z}}^{\square }\star \operatorname {SET} ({\mathcal {L}}).$

### Other elementary constructions

The operators CYCeven, CYCodd, SETeven, and SETodd represent cycles of even and odd length, and sets of even and odd cardinality.

### Example

Stirling numbers of the second kind may be derived and analyzed using the structural decomposition

$\operatorname {SET} (\operatorname {SET} _{\geq 1}({\mathcal {Z}})).$

The decomposition

$\operatorname {SET} (\operatorname {CYC} ({\mathcal {Z}}))$

is used to study unsigned Stirling numbers of the first kind, and in the derivation of the statistics of random permutations. A detailed examination of the exponential generating functions associated to Stirling numbers within symbolic combinatorics may be found on the page on Stirling numbers and exponential generating functions in symbolic combinatorics.
