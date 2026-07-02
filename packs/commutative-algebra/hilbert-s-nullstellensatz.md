---
title: "Hilbert's Nullstellensatz"
source: https://en.wikipedia.org/wiki/Hilbert's_Nullstellensatz
domain: commutative-algebra
license: CC-BY-SA-4.0
tags: commutative algebra, noetherian ring, krull dimension, grobner basis
fetched: 2026-07-02
---

# Hilbert's Nullstellensatz

In mathematics, **Hilbert's Nullstellensatz** (German for "theorem of zeros" or, more literally, "zero-locus-theorem") is a theorem that establishes a fundamental relationship between geometry and algebra. It was proven by David Hilbert in his second major paper on invariant theory in 1893 (following his seminal 1890 paper in which he proved Hilbert's basis theorem) and became a foundational result of algebraic geometry.

There are several formulations of the Nullstellensatz, the most elementary of which deal with conditions for the existence of solutions to systems of multivariate polynomial equations over an algebraically closed field (such as the complex numbers $\mathbb {C}$ ). The **weak Nullstellensatz** is a corollary (or a lemma, depending which is proved first) of the Nullstellensatz which can be stated as follows. Consider a system of polynomial equations

${\begin{cases}f_{1}(x_{1},\dots ,x_{n})=0\\\vdots \\f_{m}(x_{1},\ldots ,x_{n})=0\end{cases}}$

in the variables $x_{1},\dots ,x_{n}$ , where $f_{1},\dots ,f_{m}\in K[x_{1},\dots ,x_{n}]$ are multivariate polynomials over an algebraically closed field K . If the system does *not* have a solution $(x_{1},\dots ,x_{n})\in K^{n}$ , then there is "algebraic reason" for this situation: namely, this occurs precisely when there exist polynomials $g_{1},\dots ,g_{m}\in K[x_{1},\dots ,x_{n}]$ such that

$g_{1}f_{1}+\cdots +g_{m}f_{m}=1.$

Since the expression on the left-hand side must evaluate to 0 at any $(x_{1},\dots ,x_{n})$ that solves the system of equations, it is obvious from the inconsistency that no solution can exist if this condition holds. Informally, the (weak) Nullstellensatz asserts that in the absence of such an inconsistency, a solution to the system of equations must exist.

The full Nullstellensatz is the following refinement: If $f\in K[x_{1},\dots ,x_{n}]$ is a polynomial such that every solution of the system of equations is also a solution of

$f(x_{1},\dots ,x_{n})=0,$

then there is a similar type of "algebraic reason" for this occurrence: this occurs precisely when there exist a natural number r and polynomials $g_{1},\dots ,g_{m}$ such that

$f^{r}=g_{1}f_{1}+\cdots +g_{m}f_{m}.$

## Formulations

Let *k* be a field (such as the rational numbers) and *K* be an algebraically closed field extension of *k* (such as the complex numbers). Consider the polynomial ring $k[X_{1},\ldots ,X_{n}]$ and let *J* be an ideal in this ring. The algebraic set $\mathrm {V} (J)$ defined by this ideal consists of all *n*-tuples $a=(a_{1},\dots ,a_{n})$ in $K^{n}$ such that $f(a)=0$ for all $f\in J$ . Hilbert's Nullstellensatz states that if *p* is a polynomial in $k[X_{1},\ldots ,X_{n}]$ that vanishes on the algebraic set $\mathrm {V} (J)$ , i.e., $p(a)=0$ for all $a\in \mathrm {V} (J)$ , then there exists a natural number r such that $p^{r}\in J$ .

With the notation common in algebraic geometry, the Nullstellensatz can be formulated as

${\hbox{I}}({\hbox{V}}(J))={\sqrt {J}}$

for every ideal *J* in $K[X_{1},...,X_{n}]$ with *K* algebraically closed. Here, ${\sqrt {J}}$ denotes the *radical* of *J* ( $p\in {\sqrt {J}}$ if and only if $\exists r\in \mathbb {N} ,\ p^{r}\in J$ ), $\mathrm {I} (U)$ is the *vanishing ideal* of *U* (the set of polynomials that vanish at the points in *U*), and $\mathrm {V} (J)$ is the *zero locus* of *J* (the set of points at which the polynomials in *J* vanish). The assertion that ${\hbox{I}}({\hbox{V}}(J))\subseteq {\sqrt {J}}$ is equivalent to the first formulation above with *k* = *K* algebraically closed, while the opposite inclusion is a straightforward consequence of the definitions.

An immediate corollary is the **weak Nullstellensatz**: If *J* is a proper ideal in $k[X_{1},\ldots ,X_{n}]$ , then $\mathrm {V} (J)$ is nonempty, i.e., for every algebraically closed extension $K\supseteq k$ , there exists a common zero in $K^{n}$ for all the polynomials in the ideal *J*. This is the reason for the name of the theorem, the full version of which can be proved easily from the 'weak' form using the Rabinowitsch trick. The assumption of considering common zeros in an algebraically closed field is essential here; for example, the elements of the proper ideal $(X^{2}+1)$ in $\mathbb {R} [X]$ do not have a common zero in $\mathbb {R} .$

Specializing to the case of a single polynomial when $K=\mathbb {C}$ and $n=1$ , one immediately recovers a restatement of the fundamental theorem of algebra: A polynomial *P* in $\mathbb {C} [X]$ has a root in $\mathbb {C}$ if and only if $\deg P\neq 0$ . For this reason, the (weak) Nullstellensatz applied to $K=\mathbb {C}$ can be thought of as a generalization of the fundamental theorem of algebra to systems of multivariable polynomial equations.

Taking *K* to be algebraically closed, the Nullstellensatz establishes an order-reversing bijective correspondence between the algebraic sets in $K^{n}$ and the radical ideals of $K[X_{1},\ldots ,X_{n}].$ In fact, more generally, one has a Galois connection between subsets of the space and subsets of the algebra, where "Zariski closure" and "radical of the ideal generated" are the closure operators.

As a particular example, consider an algebraic set consisting of a single point $a=(a_{1},\dots ,a_{n})\in K^{n}$ . Then $\mathrm {I} (\{a\})=(X_{1}-a_{1},\ldots ,X_{n}-a_{n})$ is a maximal ideal. Conversely, every maximal ideal of the polynomial ring $K[X_{1},\ldots ,X_{n}]$ (note that K is algebraically closed) is of the form $(X_{1}-a_{1},\ldots ,X_{n}-a_{n})$ for some $a_{1},\ldots ,a_{n}\in K$ . This characterization of maximal ideals of polynomial rings over algebraically closed fields is another common formulation of the weak Nullstellensatz. As another example of this correspondence and a consequence of the Nullstellensatz, one can show that an algebraic subset *W* in *$K^{n}$* is irreducible (in the Zariski topology) if and only if $\mathrm {I} (W)$ is a prime ideal.

More generally, for any ideal *J* in $K[X_{1},...,X_{n}]$ ,

${\sqrt {J}}=\bigcap _{{\mathfrak {m}}\supseteq J}{\mathfrak {m}}=\bigcap _{(a_{1},\dots ,a_{n})\in \mathrm {V} (J)}(X_{1}-a_{1},\dots ,X_{n}-a_{n}),$

where the first intersection is taken over maximal ideals ${\mathfrak {m}}\subsetneq K[X_{1},...,X_{n}]$ . This relationship is yet another common formulation of the Nullstellensatz. (The first equality actually holds for ideals in any Jacobson ring, including any finitely generated algebra over a field, while the second equality holds for algebraically closed *K*.)

## Proofs

There are many known proofs of the theorem. Some are non-constructive, such as the first one. Others are constructive, as based on algorithms for expressing 1 or *pr* as a linear combination of the generators of the ideal.

### Using Zariski's lemma

Zariski's lemma asserts that if a field is finitely generated as an associative algebra over a field *K*, then it is a finite field extension of *K* (that is, it is also finitely generated as a vector space). If *K* is an algebraically closed field and ${\mathfrak {m}}$ is a maximal ideal of the ring of polynomials $K[X_{1},\ldots ,X_{n}]$ , then Zariski's lemma implies that $K[X_{1},\ldots ,X_{n}]/{\mathfrak {m}}$ is a finite field extension of *K*, and thus, by algebraic closure, must be *K*. From this, it follows that there is an $a=(a_{1},\dots ,a_{n})\in K^{n}$ such that $X_{i}-a_{i}\in {\mathfrak {m}}$ for $i=1,\dots ,n$ . In other words,

${\mathfrak {m}}\supseteq {\mathfrak {m}}_{a}=(X_{1}-a_{1},\ldots ,X_{n}-a_{n})$

for some $a=(a_{1},\dots ,a_{n})\in K^{n}$ . But ${\mathfrak {m}}_{a}$ is clearly maximal, so ${\mathfrak {m}}={\mathfrak {m}}_{a}$ . This is the weak Nullstellensatz: every maximal ideal of $K[X_{1},\ldots ,X_{n}]$ for algebraically closed *K* is of the form ${\mathfrak {m}}_{a}=(X_{1}-a_{1},\ldots ,X_{n}-a_{n})$ for some $a=(a_{1},\dots ,a_{n})\in K^{n}$ . Because of this close relationship, some texts refer to Zariski's lemma as the weak Nullstellensatz or as the 'algebraic version' of the weak Nullstellensatz.

The full Nullstellensatz can also be proved directly from Zariski's lemma without employing the Rabinowitsch trick. Here is a sketch of a proof using this lemma.

Let $A=K[X_{1},\ldots ,X_{n}]$ for algebraically closed field *K*, and let *J* be an ideal of *A* and $V=\mathrm {V} (J)$ be the common zeros of *J* in $K^{n}$ . Recall that $\mathrm {I} (V)$ is radical, and therefore ${\sqrt {J}}\subseteq \mathrm {I} (V)$ , where $\mathrm {I} (V)$ is the ideal of polynomials in *A* vanishing on *V*. To show the opposite inclusion, let $f\not \in {\sqrt {J}}$ . Then $f\not \in {\mathfrak {p}}$ for some prime ideal ${\mathfrak {p}}\supseteq J$ in *A*. Let $R=(A/{\mathfrak {p}})[1/{\bar {f}}]$ , where ${\bar {f}}$ is the image of *f* under the natural map $A\to A/{\mathfrak {p}}$ , and ${\mathfrak {m}}$ be a maximal ideal in *R*. By Zariski's lemma, $R/{\mathfrak {m}}$ is a finite extension of *K*, and thus, is *K* since *K* is algebraically closed. Let $x_{i}$ be the images of $X_{i}$ under the natural map $A\to A/{\mathfrak {p}}\to R\to R/{\mathfrak {m}}\cong K$ . It follows that, by construction, $x=(x_{1},\ldots ,x_{n})\in V$ but $f(x)\neq 0$ , so $f\notin \mathrm {I} (V)$ .

### Using resultants

The following constructive proof of the weak form is one of the oldest proofs (the strong form results from the Rabinowitsch trick, which is also constructive).

The resultant of two polynomials depending on a variable x and other variables is a polynomial in the other variables that is in the ideal generated by the two polynomials, and has the following properties: if one of the polynomials is monic in x, every zero (in the other variables) of the resultant may be extended into a common zero of the two polynomials.

The proof is as follows.

If the ideal is principal, generated by a non-constant polynomial p that depends on x, one chooses arbitrary values for the other variables. The fundamental theorem of algebra asserts that this choice can be extended to a zero of p.

In the case of several polynomials $p_{1},\ldots ,p_{n},$ a linear change of variables allows to suppose that $p_{1}$ is monic in the first variable x. Then, one introduces $n-1$ new variables $u_{2},\ldots ,u_{n},$ and one considers the resultant

$R=\operatorname {Res} _{x}(p_{1},u_{2}p_{2}+\cdots +u_{n}p_{n}).$

As R is in the ideal generated by $p_{1},\ldots ,p_{n},$ the same is true for the coefficients in R of the monomials in $u_{2},\ldots ,u_{n}.$ So, if 1 is in the ideal generated by these coefficients, it is also in the ideal generated by $p_{1},\ldots ,p_{n}.$ On the other hand, if these coefficients have a common zero, this zero can be extended to a common zero of $p_{1},\ldots ,p_{n},$ by the above property of the resultant.

This proves the weak Nullstellensatz by induction on the number of variables.

### Using Gröbner bases

A Gröbner basis is an algorithmic concept that was introduced in 1973 by Bruno Buchberger. It is presently fundamental in computational geometry. A Gröbner basis is a special generating set of an ideal from which most properties of the ideal can easily be extracted. Those that are related to the Nullstellensatz are the following:

- An ideal contains 1 if and only if its reduced Gröbner basis (for any monomial ordering) is 1.
- The number of the common zeros of the polynomials in a Gröbner basis is strongly related to the number of monomials that are irreducibles by the basis. Namely, the number of common zeros is infinite if and only if the same is true for the irreducible monomials; if the two numbers are finite, the number of irreducible monomials equals the numbers of zeros (in an algebraically closed field), counted with multiplicities.
- With a lexicographic monomial order, the common zeros can be computed by solving iteratively univariate polynomials (this is not used in practice since one knows better algorithms).
- Strong Nullstellensatz: a power of p belongs to an ideal I if and only the saturation of I by p produces the Gröbner basis 1. Thus, the strong Nullstellensatz results almost immediately from the definition of the saturation.

## Generalizations

The Nullstellensatz is subsumed by a systematic development of the theory of Jacobson rings, which are those rings in which every radical ideal is an intersection of maximal ideals. Given Zariski's lemma, proving the Nullstellensatz amounts to showing that if *k* is a field, then every finitely generated *k*-algebra *R* (necessarily of the form ${\textstyle R=k[t_{1},\cdots ,t_{n}]/I}$ ) is Jacobson. More generally, one has the following theorem:

Let

R

be a Jacobson ring. If

S

is a finitely generated

R

-algebra

, then

S

is a Jacobson ring. Furthermore, if

${\mathfrak {n}}\subseteq S$

is a maximal ideal, then

${\mathfrak {m}}:={\mathfrak {n}}\cap R$

is a maximal ideal of

${\textstyle R}$

, and

$S/{\mathfrak {n}}$

is a finite extension of

$R/{\mathfrak {m}}$

.

Other generalizations proceed from viewing the Nullstellensatz in scheme-theoretic terms as saying that for any field *k* and nonzero finitely generated *k*-algebra *R*, the morphism ${\textstyle \mathrm {Spec} \,R\to \mathrm {Spec} \,k}$ admits a section étale-locally (equivalently, after base change along ${\textstyle \mathrm {Spec} \,L\to \mathrm {Spec} \,k}$ for some finite field extension ${\textstyle L/k}$ ). In this vein, one has the following theorem:

Any

faithfully flat

morphism of schemes

${\textstyle f:Y\to X}$

locally of finite presentation

admits a

quasi-section

, in the sense that there exists a faithfully flat and locally

quasi-finite

morphism

${\textstyle g:X'\to X}$

locally of finite presentation such that the base change

${\textstyle f':Y\times _{X}X'\to X'}$

of

${\textstyle f}$

along

${\textstyle g}$

admits a section.

Moreover, if

${\textstyle X}$

is

quasi-compact

(resp. quasi-compact and

quasi-separated

), then one may take

${\textstyle X'}$

to be affine (resp.

${\textstyle X'}$

affine and

${\textstyle g}$

quasi-finite), and if

${\textstyle f}$

is

smooth

surjective, then one may take

${\textstyle g}$

to be

étale

.

Serge Lang gave an extension of the Nullstellensatz to the case of infinitely many generators:

Let

${\textstyle \kappa }$

be an

infinite cardinal

and let

${\textstyle K}$

be an algebraically closed field whose

transcendence degree

over its

prime subfield

is strictly greater than

$\kappa$

. Then for any set

${\textstyle S}$

of cardinality

${\textstyle \kappa }$

, the polynomial ring

${\textstyle A=K[x_{i}]_{i\in S}}$

satisfies the Nullstellensatz, i.e., for any ideal

${\textstyle J\subset A}$

we have that

${\sqrt {J}}={\hbox{I}}({\hbox{V}}(J))$

.

## Effective Nullstellensatz

In all of its variants, Hilbert's Nullstellensatz asserts that some polynomial g belongs or not to an ideal generated, say, by *f*1, ..., *fk*; we have *g* = *f r* in the strong version, *g* = 1 in the weak form. This means the existence or the non-existence of polynomials *g*1, ..., *gk* such that *g* = *f*1*g*1 + ... + *fkgk*. The usual proofs of the Nullstellensatz are not constructive, non-effective, in the sense that they do not give any way to compute the *gi*.

It is thus a rather natural question to ask if there is an effective way to compute the *gi* (and the exponent r in the strong form) or to prove that they do not exist. To solve this problem, it suffices to provide an upper bound on the total degree of the *gi*: such a bound reduces the problem to a finite system of linear equations that may be solved by usual linear algebra techniques. Any such upper bound is called an **effective Nullstellensatz**.

A related problem is the **ideal membership problem**, which consists in testing if a polynomial belongs to an ideal. For this problem also, a solution is provided by an upper bound on the degree of the *gi*. A general solution of the ideal membership problem provides an effective Nullstellensatz, at least for the weak form.

In 1925, Grete Hermann gave an upper bound for ideal membership problem that is doubly exponential in the number of variables. In 1982 Mayr and Meyer gave an example where the *gi* have a degree that is at least double exponential, showing that every general upper bound for the ideal membership problem is doubly exponential in the number of variables.

Since most mathematicians at the time assumed the effective Nullstellensatz was at least as hard as ideal membership, few mathematicians sought a bound better than double-exponential. In 1987, however, W. Dale Brownawell gave an upper bound for the effective Nullstellensatz that is simply exponential in the number of variables. Brownawell's proof relied on analytic techniques valid only in characteristic 0, but, one year later, János Kollár gave a purely algebraic proof, valid in any characteristic, of a slightly better bound.

In the case of the weak Nullstellensatz, Kollár's bound is the following:

Let

f

1

, ...,

f

s

be polynomials in

n

≥ 2

variables, of total degree

d

1

≥ ... ≥

d

s

. If there exist polynomials

g

i

such that

f

1

g

1

+ ... +

f

s

g

s

= 1

, then they can be chosen such that

$\deg(f_{i}g_{i})\leq \max(d_{s},3)\prod _{j=1}^{\min(n,s)-1}\max(d_{j},3).$

This bound is optimal if all the degrees are greater than 2.

If d is the maximum of the degrees of the *fi*, this bound may be simplified to

$\max(3,d)^{\min(n,s)}.$

An improvement due to M. Sombra is

$\deg(f_{i}g_{i})\leq 2d_{s}\prod _{j=1}^{\min(n,s)-1}d_{j}.$

His bound improves Kollár's as soon as at least two of the degrees that are involved are lower than 3.

## Projective Nullstellensatz

We can formulate a certain correspondence between homogeneous ideals of polynomials and algebraic subsets of a projective space, called the **projective Nullstellensatz**, that is analogous to the affine one. To do that, we introduce some notations. Let $R=k[t_{0},\ldots ,t_{n}].$ The homogeneous ideal,

$R_{+}=\bigoplus _{d\geqslant 1}R_{d}$

is called the *maximal homogeneous ideal* (see also irrelevant ideal). As in the affine case, we let: for a subset $S\subseteq \mathbb {P} ^{n}$ and a homogeneous ideal *I* of *R*,

${\begin{aligned}\operatorname {I} _{\mathbb {P} ^{n}}(S)&=\{f\in R_{+}\mid f=0{\text{ on }}S\},\\\operatorname {V} _{\mathbb {P} ^{n}}(I)&=\{x\in \mathbb {P} ^{n}\mid f(x)=0{\text{ for all }}f\in I\}.\end{aligned}}$

By $f=0{\text{ on }}S$ we mean: for every homogeneous coordinates $(a_{0}:\cdots :a_{n})$ of a point of *S* we have $f(a_{0},\ldots ,a_{n})=0$ . This implies that the homogeneous components of *f* are also zero on *S* and thus that $\operatorname {I} _{\mathbb {P} ^{n}}(S)$ is a homogeneous ideal. Equivalently, $\operatorname {I} _{\mathbb {P} ^{n}}(S)$ is the homogeneous ideal generated by homogeneous polynomials *f* that vanish on *S*. Now, for any homogeneous ideal $I\subseteq R_{+}$ , by the usual Nullstellensatz, we have:

${\sqrt {I}}=\operatorname {I} _{\mathbb {P} ^{n}}(\operatorname {V} _{\mathbb {P} ^{n}}(I)),$

and so, like in the affine case, we have:

There exists an order-reversing one-to-one correspondence between proper homogeneous radical ideals of

R

and subsets of

$\mathbb {P} ^{n}$

of the form

$\operatorname {V} _{\mathbb {P} ^{n}}(I).$

The correspondence is given by

$\operatorname {I} _{\mathbb {P} ^{n}}$

and

$\operatorname {V} _{\mathbb {P} ^{n}}.$

## Analytic Nullstellensatz (Rückert’s Nullstellensatz)

The Nullstellensatz also holds for the germs of holomorphic functions at a point of complex *n*-space $\mathbb {C} ^{n}.$ Precisely, for each open subset $U\subseteq \mathbb {C} ^{n},$ let ${\mathcal {O}}_{\mathbb {C} ^{n}}(U)$ denote the ring of holomorphic functions on *U*; then ${\mathcal {O}}_{\mathbb {C} ^{n}}$ is a *sheaf* on $\mathbb {C} ^{n}.$ The stalk ${\mathcal {O}}_{\mathbb {C} ^{n},0}$ at, say, the origin can be shown to be a Noetherian local ring that is a unique factorization domain.

If $f\in {\mathcal {O}}_{\mathbb {C} ^{n},0}$ is a germ represented by a holomorphic function ${\widetilde {f}}:U\to \mathbb {C}$ , then let $V_{0}(f)$ be the equivalence class of the set

$\left\{z\in U\mid {\widetilde {f}}(z)=0\right\},$

where two subsets $X,Y\subseteq \mathbb {C} ^{n}$ are considered equivalent if $X\cap U=Y\cap U$ for some neighborhood *U* of 0. Note $V_{0}(f)$ is independent of a choice of the representative ${\widetilde {f}}.$ For each ideal $I\subseteq {\mathcal {O}}_{\mathbb {C} ^{n},0},$ let $V_{0}(I)$ denote $V_{0}(f_{1})\cap \dots \cap V_{0}(f_{r})$ for some generators $f_{1},\ldots ,f_{r}$ of *I*. It is well-defined; i.e., is independent of a choice of the generators.

For each subset $X\subseteq \mathbb {C} ^{n}$ , let

$I_{0}(X)=\left\{f\in {\mathcal {O}}_{\mathbb {C} ^{n},0}\mid V_{0}(f)\supset X\right\}.$

It is easy to see that $I_{0}(X)$ is an ideal of ${\mathcal {O}}_{\mathbb {C} ^{n},0}$ and that $I_{0}(X)=I_{0}(Y)$ if $X\sim Y$ in the sense discussed above.

The **analytic Nullstellensatz** then states: for each ideal $I\subseteq {\mathcal {O}}_{\mathbb {C} ^{n},0}$ ,

${\sqrt {I}}=I_{0}(V_{0}(I))$

where the left-hand side is the radical of *I*.

## Formal Nullstellensatz

In classical algebraic geometry, the zero locus ('variety') operation (V) is applied to subsets of the ring of polynomials over an algebraically closed field, while the vanishing ideal operation (I) is applied to subsets of affine *n-*space, whose points are in one-to-one correspondence with the maximal ideals of the polynomial ring by the weak Nullstellensatz (see above). In scheme theory, V and I are generalized and redefined so that they could be applied to subsets of arbitrary commutative (unital) rings and their *prime* spectra, respectively. In particular, for any commutative ring *A*, its set of prime ideals (prime spectrum) $\mathrm {Spec} \ A$ , and subsets $S\subset A$ and $X\subset \mathrm {Spec} \ A$ , we set

$\mathbb {V} (S)=\{{\mathfrak {p}}\in \mathrm {Spec} \ A\mid {\mathfrak {p}}\supset S\}$

and

$\mathbb {I} (X)=\bigcap _{{\mathfrak {p}}\in X}{\mathfrak {p}}.$

Then for any ideal $J\triangleleft A$ , a formal analogue of Hilbert's Nullstellensatz holds:

$\mathbb {I} (\mathbb {V} (J))=\bigcap _{{\mathfrak {p}}\in \mathbb {V} (J)}{\mathfrak {p}}=\bigcap _{{\mathfrak {p}}\in \mathrm {Spec} \ A,\ {\mathfrak {p}}\supset J}{\mathfrak {p}}={\sqrt {J}},$

where the last equality follows from a standard property of prime ideals from commutative algebra. In analogy to zero loci in the classical theory, the $\mathbb {V} (S)$ are used to define the closed sets in the Zariski topology of $\mathrm {Spec} \ A$ .
