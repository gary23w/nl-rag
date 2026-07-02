---
title: "Chern class"
source: https://en.wikipedia.org/wiki/Chern_class
domain: k-theory
license: CC-BY-SA-4.0
tags: topological k-theory, algebraic k-theory, grothendieck group, vector bundle
fetched: 2026-07-02
---

# Chern class

In mathematics, in particular in algebraic topology, differential geometry and algebraic geometry, the **Chern classes** are characteristic classes associated with complex vector bundles. They have since become fundamental concepts in many branches of mathematics and physics, such as string theory, Chern–Simons theory, knot theory, and Gromov–Witten invariants. Chern classes were introduced by Shiing-Shen Chern (1946).

## Geometric approach

### Basic idea and motivation

Chern classes are characteristic classes. They are topological invariants associated with vector bundles on a smooth manifold. The question of whether two ostensibly different vector bundles are the same can be quite hard to answer. The Chern classes provide a simple test: if the Chern classes of a pair of vector bundles do not agree, then the vector bundles are different. The converse, however, is not true.

In topology, differential geometry, and algebraic geometry, it is often important to count how many linearly independent sections a vector bundle has. The Chern classes offer some information about this through, for instance, the Riemann–Roch theorem and the Atiyah–Singer index theorem.

Chern classes are also feasible to calculate in practice. In differential geometry (and some types of algebraic geometry), the Chern classes can be expressed as polynomials in the coefficients of the curvature form.

### Construction

There are various ways of approaching the subject, each of which focuses on a slightly different flavor of Chern class.

The original approach to Chern classes was via algebraic topology: the Chern classes arise via homotopy theory which provides a mapping associated with a vector bundle to a classifying space (an infinite Grassmannian in this case). For any complex vector bundle *V* over a manifold *M*, there exists a map *f* from *M* to the classifying space such that the bundle *V* is equal to the pullback, by *f*, of a universal bundle over the classifying space, and the Chern classes of *V* can therefore be defined as the pullback of the Chern classes of the universal bundle. In turn, these universal Chern classes can be explicitly written down in terms of Schubert cycles.

It can be shown that for any two maps *f*, *g* from *M* to the classifying space whose pullbacks are the same bundle *V*, the maps must be homotopic. Therefore, the pullback by either *f* or *g* of any universal Chern class to a cohomology class of *M* must be the same class. This shows that the Chern classes of *V* are well-defined.

Chern's approach used differential geometry, via the curvature approach described predominantly in this article. He showed that the earlier definition was in fact equivalent to his. The resulting theory is known as the Chern–Weil theory.

There is also an approach of Alexander Grothendieck showing that axiomatically one need only define the line bundle case.

Chern classes arise naturally in algebraic geometry. The generalized Chern classes in algebraic geometry can be defined for vector bundles (or more precisely, locally free sheaves) over any nonsingular variety. Algebro-geometric Chern classes do not require the underlying field to have any special properties. In particular, the vector bundles need not necessarily be complex.

Regardless of the particular paradigm, the intuitive meaning of the Chern class concerns 'required zeroes' of a section of a vector bundle: for example the theorem saying one can't comb a hairy ball flat (hairy ball theorem). Although that is strictly speaking a question about a *real* vector bundle (the "hairs" on a ball are actually copies of the real line), there are generalizations in which the hairs are complex (see the example of the complex hairy ball theorem below), or for 1-dimensional projective spaces over many other fields.

See Chern–Simons theory for more discussion.

## The Chern class of line bundles

(Let *X* be a topological space having the homotopy type of a CW complex.)

An important special case occurs when *V* is a line bundle. Then the only nontrivial Chern class is the first Chern class, which is an element of the second cohomology group of *X*. As it is the top Chern class, it equals the Euler class of the bundle.

The first Chern class turns out to be a complete invariant with which to classify complex line bundles, topologically speaking. That is, there is a bijection between the isomorphism classes of line bundles over *X* and the elements of $H^{2}(X;\mathbb {Z} )$ , which associates to a line bundle its first Chern class. Moreover, this bijection is a group homomorphism (thus an isomorphism): $c_{1}(L\otimes L')=c_{1}(L)+c_{1}(L');$ the tensor product of complex line bundles corresponds to the addition in the second cohomology group.

In algebraic geometry, this classification of (isomorphism classes of) complex line bundles by the first Chern class is a crude approximation to the classification of (isomorphism classes of) holomorphic line bundles by linear equivalence classes of divisors.

For complex vector bundles of dimension greater than one, the Chern classes are not a complete invariant.

## Constructions

### Via the Chern–Weil theory

Given a complex vector bundle *V* of complex rank *n* over a smooth manifold *M,* fix a vector bundle connection $\nabla$ . Then representatives of each Chern class (also called a **Chern form**) $c_{k}(V)$ of *V* are given as the coefficients of the characteristic polynomial of the curvature form $\Omega$ of $\nabla$ .

$\det \left({\frac {it\Omega }{2\pi }}+I\right)=\sum _{k}c_{k}(V)t^{k}$

The determinant is over the ring of $n\times n$ matrices whose entries are polynomials in *t* with coefficients in the commutative algebra of even-degree complex differential forms on *M*. The curvature form $\Omega$ of *V* is defined as $\Omega =d\omega +{\frac {1}{2}}[\omega ,\omega ]$ with ω the connection form and *d* the exterior derivative, or via the same expression in which ω is a gauge field for the gauge group of *V*. The scalar *t* is used here only as an indeterminate to generate the sum from the determinant, and *I* denotes the *n* × *n* identity matrix.

To say that the expression given is a *representative* of the Chern class indicates that 'class' here means up to addition of an exact differential form. That is, Chern classes are cohomology classes in the sense of de Rham cohomology. It can be shown that the cohomology classes of the Chern forms do not depend on the choice of connection $\nabla$ .

It follows from the matrix identity $\mathrm {tr} (\ln(X))=\ln(\det(X))$ that $\det(X)=\exp(\mathrm {tr} (\ln(X)))$ . Now applying the Maclaurin series for $\ln(X+I)$ , we get the following expression for the Chern forms:

$\sum _{k}c_{k}(V)t^{k}=\left[1+i{\frac {\mathrm {tr} (\Omega )}{2\pi }}t+{\frac {\mathrm {tr} (\Omega ^{2})-\mathrm {tr} (\Omega )^{2}}{8\pi ^{2}}}t^{2}+i{\frac {-2\mathrm {tr} (\Omega ^{3})+3\mathrm {tr} (\Omega ^{2})\mathrm {tr} (\Omega )-\mathrm {tr} (\Omega )^{3}}{48\pi ^{3}}}t^{3}+\cdots \right].$

### Via an Euler class

One can define a Chern class in terms of an Euler class. This is the approach in the book by Milnor and Stasheff, and emphasizes the role of an orientation of a vector bundle.

The basic observation is that a complex vector bundle comes with a canonical orientation, ultimately because $\operatorname {GL} _{n}(\mathbb {C} )$ is connected. Hence, one simply defines the top Chern class of the bundle to be its Euler class (the Euler class of the underlying real vector bundle) and handles lower Chern classes in an inductive fashion.

The precise construction is as follows. The idea is to do base change to get a bundle of one-less rank. Let $\pi \colon E\to B$ be a complex vector bundle over a paracompact space *B*. Thinking of *B* as being embedded in *E* as the zero section, let $B'=E\setminus B$ and define the new vector bundle: $E'\to B'$ such that each fiber is the quotient of a fiber *F* of *E* by the line spanned by a nonzero vector *v* in *F* (a point of *B′* is specified by a fiber *F* of *E* and a nonzero vector on *F*.) Then $E'$ has rank one less than that of *E*. From the Gysin sequence for the fiber bundle $\pi |_{B'}\colon B'\to B$ : $\cdots \to \operatorname {H} ^{k}(B;\mathbb {Z} ){\overset {\pi |_{B'}^{*}}{\to }}\operatorname {H} ^{k}(B';\mathbb {Z} )\to \cdots ,$ we see that $\pi |_{B'}^{*}$ is an isomorphism for $k<2n-1$ . Let $c_{k}(E)={\begin{cases}{\pi |_{B'}^{*}}^{-1}c_{k}(E')&k<n\\e(E_{\mathbb {R} })&k=n\\0&k>n\end{cases}}$

It then takes some work to check the axioms of Chern classes are satisfied for this definition.

See also: The Thom isomorphism.

## Examples

### The complex tangent bundle of the Riemann sphere

Let $\mathbb {CP} ^{1}$ be the Riemann sphere: 1-dimensional complex projective space. Suppose that *z* is a holomorphic local coordinate for the Riemann sphere. Let $V=T\mathbb {CP} ^{1}$ be the bundle of complex tangent vectors having the form $a\partial /\partial z$ at each point, where *a* is a complex number. We prove the complex version of the *hairy ball theorem*: *V* has no section which is everywhere nonzero.

For this, we need the following fact: the first Chern class of a trivial bundle is zero, i.e., $c_{1}(\mathbb {CP} ^{1}\times \mathbb {C} )=0.$

This is evinced by the fact that a trivial bundle always admits a flat connection. So, we shall show that $c_{1}(V)\not =0.$

Consider the Kähler metric $h={\frac {dzd{\bar {z}}}{(1+|z|^{2})^{2}}}.$

One readily shows that the curvature 2-form is given by $\Omega ={\frac {2dz\wedge d{\bar {z}}}{(1+|z|^{2})^{2}}}.$

Furthermore, by the definition of the first Chern class $c_{1}=\left[{\frac {i}{2\pi }}\operatorname {tr} \Omega \right].$

We must show that this cohomology class is non-zero. It suffices to compute its integral over the Riemann sphere: $\int c_{1}={\frac {i}{\pi }}\int {\frac {dz\wedge d{\bar {z}}}{(1+|z|^{2})^{2}}}=2$ after switching to polar coordinates. By Stokes' theorem, an exact form would integrate to 0, so the cohomology class is nonzero.

This proves that $T\mathbb {CP} ^{1}$ is not a trivial vector bundle.

### Complex projective space

There is an exact sequence of sheaves/bundles: $0\to {\mathcal {O}}_{\mathbb {CP} ^{n}}\to {\mathcal {O}}_{\mathbb {CP} ^{n}}(1)^{\oplus (n+1)}\to T\mathbb {CP} ^{n}\to 0$ where ${\mathcal {O}}_{\mathbb {CP} ^{n}}$ is the structure sheaf (i.e., the trivial line bundle), ${\mathcal {O}}_{\mathbb {CP} ^{n}}(1)$ is Serre's twisting sheaf (i.e., the hyperplane bundle) and the last nonzero term is the tangent sheaf/bundle.

There are two ways to get the above sequence:

1. Let $z_{0},\ldots ,z_{n}$ be the coordinates of $\mathbb {C} ^{n+1},$ let $\pi \colon \mathbb {C} ^{n+1}\setminus \{0\}\to \mathbb {C} \mathbb {P} ^{n}$ be the canonical projection, and let $U=\mathbb {CP} ^{n}\setminus \{z_{0}=0\}$ . Then we have: $\pi ^{*}d(z_{i}/z_{0})={z_{0}dz_{i}-z_{i}dz_{0} \over z_{0}^{2}},\,i\geq 1.$ In other words, the cotangent sheaf $\Omega _{\mathbb {C} \mathbb {P} ^{n}}|_{U}$ , which is a free ${\mathcal {O}}_{U}$ -module with basis $d(z_{i}/z_{0})$ , fits into the exact sequence $0\to \Omega _{\mathbb {C} \mathbb {P} ^{n}}|_{U}{\overset {dz_{i}\mapsto e_{i}}{\to }}\oplus _{1}^{n+1}{\mathcal {O}}(-1)|_{U}{\overset {e_{i}\mapsto z_{i}}{\to }}{\mathcal {O}}_{U}\to 0,\,i\geq 0,$ where $e_{i}$ are the basis of the middle term. The same sequence is clearly then exact on the whole projective space and the dual of it is the aforementioned sequence.
2. Let *L* be a line in $\mathbb {C} ^{n+1}$ that passes through the origin. It is an exercise in elementary geometry to see that the complex tangent space to $\mathbb {C} \mathbb {P} ^{n}$ at the point *L* is naturally the set of linear maps from *L* to its complement. Thus, the tangent bundle $T\mathbb {C} \mathbb {P} ^{n}$ can be identified with the hom bundle $\operatorname {Hom} ({\mathcal {O}}(-1),\eta )$ where η is the vector bundle such that ${\mathcal {O}}(-1)\oplus \eta ={\mathcal {O}}^{\oplus (n+1)}$ . It follows: $T\mathbb {C} \mathbb {P} ^{n}\oplus {\mathcal {O}}=\operatorname {Hom} ({\mathcal {O}}(-1),\eta )\oplus \operatorname {Hom} ({\mathcal {O}}(-1),{\mathcal {O}}(-1))={\mathcal {O}}(1)^{\oplus (n+1)}.$

By the additivity of total Chern class $c=1+c_{1}+c_{2}+\cdots$ (i.e., the Whitney sum formula), $c(\mathbb {C} \mathbb {P} ^{n}){\overset {\mathrm {def} }{=}}c(T\mathbb {CP} ^{n})=c({\mathcal {O}}_{\mathbb {C} \mathbb {P} ^{n}}(1))^{n+1}=(1+a)^{n+1},$ where *a* is the canonical generator of the cohomology group $H^{2}(\mathbb {C} \mathbb {P} ^{n},\mathbb {Z} )$ ; i.e., the negative of the first Chern class of the tautological line bundle ${\mathcal {O}}_{\mathbb {C} \mathbb {P} ^{n}}(-1)$ (note: $c_{1}(E^{*})=-c_{1}(E)$ when $E^{*}$ is the dual of *E*.)

In particular, for any $k\geq 0$ , $c_{k}(\mathbb {C} \mathbb {P} ^{n})={\binom {n+1}{k}}a^{k}.$

## Chern polynomial

A Chern polynomial is a convenient way to handle Chern classes and related notions systematically. By definition, for a complex vector bundle *E*, the **Chern polynomial** *c**t* of *E* is given by: $c_{t}(E)=1+c_{1}(E)t+\cdots +c_{n}(E)t^{n}.$

This is not a new invariant: the formal variable *t* simply keeps track of the degree of *c**k*(*E*). In particular, $c_{t}(E)$ is completely determined by the **total Chern class** of *E*: $c(E)=1+c_{1}(E)+\cdots +c_{n}(E)$ and conversely.

The Whitney sum formula, one of the axioms of Chern classes (see below), says that *c**t* is additive in the sense: $c_{t}(E\oplus E')=c_{t}(E)c_{t}(E').$ Now, if $E=L_{1}\oplus \cdots \oplus L_{n}$ is a direct sum of (complex) line bundles, then it follows from the sum formula that: $c_{t}(E)=(1+a_{1}(E)t)\cdots (1+a_{n}(E)t)$ where $a_{i}(E)=c_{1}(L_{i})$ are the first Chern classes. The roots $a_{i}(E)$ , called the **Chern roots** of *E*, determine the coefficients of the polynomial: i.e., $c_{k}(E)=\sigma _{k}(a_{1}(E),\ldots ,a_{n}(E))$ where σ*k* are elementary symmetric polynomials. In other words, thinking of *a**i* as formal variables, *c**k* "are" σ*k*. A basic fact on symmetric polynomials is that any symmetric polynomial in, say, *t**i*'s is a polynomial in elementary symmetric polynomials in *t**i*'s. Either by splitting principle or by ring theory, any Chern polynomial $c_{t}(E)$ factorizes into linear factors after enlarging the cohomology ring; *E* need not be a direct sum of line bundles in the preceding discussion. The conclusion is

"One can evaluate any symmetric polynomial

f

at a complex vector bundle

E

by writing

f

as a polynomial in σ

k

and then replacing σ

k

by

c

k

(

E

)."

**Example**: We have polynomials *s**k* $t_{1}^{k}+\cdots +t_{n}^{k}=s_{k}(\sigma _{1}(t_{1},\ldots ,t_{n}),\ldots ,\sigma _{k}(t_{1},\ldots ,t_{n}))$ with $s_{1}=\sigma _{1},s_{2}=\sigma _{1}^{2}-2\sigma _{2}$ and so on (cf. Newton's identities). The sum $\operatorname {ch} (E)=e^{a_{1}(E)}+\cdots +e^{a_{n}(E)}=\sum s_{k}(c_{1}(E),\ldots ,c_{n}(E))/k!$ is called the Chern character of *E*, whose first few terms are: (we drop *E* from writing.) $\operatorname {ch} (E)=\operatorname {rk} +c_{1}+{\frac {1}{2}}(c_{1}^{2}-2c_{2})+{\frac {1}{6}}(c_{1}^{3}-3c_{1}c_{2}+3c_{3})+\cdots .$

**Example**: The Todd class of *E* is given by: $\operatorname {td} (E)=\prod _{1}^{n}{a_{i} \over 1-e^{-a_{i}}}=1+{1 \over 2}c_{1}+{1 \over 12}(c_{1}^{2}+c_{2})+{\frac {1}{24}}c_{1}c_{2}\cdots .$

**Remark**: The observation that a Chern class is essentially an elementary symmetric polynomial can be used to "define" Chern classes. Let *G**n* be the infinite Grassmannian of *n*-dimensional complex vector spaces. This space is equipped with a tautologous vector bundle of rank n , say $E_{n}\to G_{n}$ . $G_{n}$ is called the classifying space for rank- n vector bundles because given any complex vector bundle *E* of rank *n* over *X*, there is a continuous map $f_{E}:X\to G_{n}$ such that the pullback of $E_{n}$ to X along $f_{E}$ is isomorphic to E , and this map $f_{E}$ is unique up to homotopy. Borel's theorem says the cohomology ring of *G**n* is exactly the ring of symmetric polynomials, which are polynomials in elementary symmetric polynomials σ*k*; so, the pullback of *f**E* reads: $f_{E}^{*}:\mathbb {Z} [\sigma _{1},\ldots ,\sigma _{n}]\to H^{*}(X,\mathbb {Z} ).$ One then puts: $c_{k}(E)=f_{E}^{*}(\sigma _{k}).$

**Remark**: Any characteristic class is a polynomial in Chern classes, for the reason as follows. Let $\operatorname {Vect} _{n}^{\mathbb {C} }$ be the contravariant functor that, to a CW complex *X*, assigns the set of isomorphism classes of complex vector bundles of rank *n* over *X* and, to a map, its pullback. By definition, a characteristic class is a natural transformation from $\operatorname {Vect} _{n}^{\mathbb {C} }=[-,G_{n}]$ to the cohomology functor $H^{*}(-,\mathbb {Z} ).$ Characteristic classes form a ring because of the ring structure of cohomology ring. Yoneda's lemma says this ring of characteristic classes is exactly the cohomology ring of *G**n*: $\operatorname {Nat} ([-,G_{n}],H^{*}(-,\mathbb {Z} ))=H^{*}(G_{n},\mathbb {Z} )=\mathbb {Z} [\sigma _{1},\ldots ,\sigma _{n}].$

## Computation formulae

Let *E* be a vector bundle of rank *r* and $c_{t}(E)=\sum _{i=0}^{r}c_{i}(E)t^{i}$ the Chern polynomial of it.

- For the dual bundle $E^{*}$ of E , $c_{i}(E^{*})=(-1)^{i}c_{i}(E)$ .
- If *L* is a line bundle, then $c_{t}(E\otimes L)=\sum _{i=0}^{r}c_{i}(E)c_{t}(L)^{r-i}t^{i}$ and so $c_{i}(E\otimes L),i=1,2,\dots ,r$ are $c_{1}(E)+rc_{1}(L),\dots ,\sum _{j=0}^{i}{\binom {r-i+j}{j}}c_{i-j}(E)c_{1}(L)^{j},\dots ,\sum _{j=0}^{r}c_{r-j}(E)c_{1}(L)^{j}.$
- For the Chern roots $\alpha _{1},\dots ,\alpha _{r}$ of E , ${\begin{aligned}c_{t}(\operatorname {Sym} ^{p}E)&=\prod _{i_{1}\leq \cdots \leq i_{p}}(1+(\alpha _{i_{1}}+\cdots +\alpha _{i_{p}})t),\\c_{t}(\wedge ^{p}E)&=\prod _{i_{1}<\cdots <i_{p}}(1+(\alpha _{i_{1}}+\cdots +\alpha _{i_{p}})t).\end{aligned}}$ In particular, $c_{1}(\wedge ^{r}E)=c_{1}(E).$
- For example, for $c_{i}=c_{i}(E)$ , when $r=2$ , $c(\operatorname {Sym} ^{2}E)=1+3c_{1}+2c_{1}^{2}+4c_{2}+4c_{1}c_{2},$ when $r=3$ , $c(\operatorname {Sym} ^{2}E)=1+4c_{1}+5c_{1}^{2}+5c_{2}+2c_{1}^{3}+11c_{1}c_{2}+7c_{3}.$

(cf.

Segre class#Example 2

.)

### Applications of formulae

We can use these abstract properties to compute the rest of the chern classes of line bundles on $\mathbb {CP} ^{1}$ . Recall that ${\mathcal {O}}(-1)^{*}\cong {\mathcal {O}}(1)$ showing $c_{1}({\mathcal {O}}(1))=1\in H^{2}(\mathbb {CP} ^{1};\mathbb {Z} )$ . Then using tensor powers, we can relate them to the chern classes of $c_{1}({\mathcal {O}}(n))=n$ for any integer.

## Properties

Given a complex vector bundle *E* over a topological space *X*, the Chern classes of *E* are a sequence of elements of the cohomology of *X*. The ***k*-th Chern class** of *E*, which is usually denoted *ck*(*E*), is an element of $H^{2k}(X;\mathbb {Z} ),$ the cohomology of *X* with integer coefficients. One can also define the **total Chern class** $c(E)=c_{0}(E)+c_{1}(E)+c_{2}(E)+\cdots .$

Since the values are in integral cohomology groups, rather than cohomology with real coefficients, these Chern classes are slightly more refined than those in the Riemannian example.

### Classical axiomatic definition

The Chern classes satisfy the following four axioms:

1. $c_{0}(E)=1$ for all *E*.
2. Naturality: If $f:Y\to X$ is continuous and *f*E* is the vector bundle pullback of *E*, then $c_{k}(f^{*}E)=f^{*}c_{k}(E)$ .
3. Whitney sum formula: If $F\to X$ is another complex vector bundle, then the Chern classes of the direct sum $E\oplus F$ are given by $c(E\oplus F)=c(E)\smile c(F);$ that is, $c_{k}(E\oplus F)=\sum _{i=0}^{k}c_{i}(E)\smile c_{k-i}(F).$
4. Normalization: The total Chern class of the tautological line bundle over $\mathbb {CP} ^{k}$ is 1−*H*, where *H* is Poincaré dual to the hyperplane $\mathbb {CP} ^{k-1}\subseteq \mathbb {CP} ^{k}$ .

### Grothendieck axiomatic approach

Alternatively, Alexander Grothendieck (1958) replaced these with a slightly smaller set of axioms:

- Naturality: (Same as above)
- Additivity: If $0\to E'\to E\to E''\to 0$ is an exact sequence of vector bundles, then $c(E)=c(E')\smile c(E'')$ .
- Normalization: If *E* is a line bundle, then $c(E)=1+e(E_{\mathbb {R} })$ where $e(E_{\mathbb {R} })$ is the Euler class of the underlying real vector bundle.

He shows using the Leray–Hirsch theorem that the total Chern class of an arbitrary finite rank complex vector bundle can be defined in terms of the first Chern class of a tautologically defined line bundle.

Namely, introducing the projectivization $\mathbb {P} (E)$ of the rank *n* complex vector bundle *E* → *B* as the fiber bundle on *B* whose fiber at any point $b\in B$ is the projective space of the fiber *Eb*. The total space of this bundle $\mathbb {P} (E)$ is equipped with its tautological complex line bundle, that we denote $\tau$ , and the first Chern class $c_{1}(\tau )=:-a$ restricts on each fiber $\mathbb {P} (E_{b})$ to minus the (Poincaré-dual) class of the hyperplane, that spans the cohomology of the fiber, in view of the cohomology of complex projective spaces.

The classes $1,a,a^{2},\ldots ,a^{n-1}\in H^{*}(\mathbb {P} (E))$ therefore form a family of ambient cohomology classes restricting to a basis of the cohomology of the fiber. The Leray–Hirsch theorem then states that any class in $H^{*}(\mathbb {P} (E))$ can be written uniquely as a linear combination of the 1, *a*, *a*2, ..., *a**n*−1 with classes on the base as coefficients.

In particular, one may define the Chern classes of *E* in the sense of Grothendieck, denoted $c_{1}(E),\ldots c_{n}(E)$ by expanding this way the class $-a^{n}$ , with the relation: $-a^{n}=c_{1}(E)\cdot a^{n-1}+\cdots +c_{n-1}(E)\cdot a+c_{n}(E).$

One then may check that this alternative definition coincides with whatever other definition one may favor, or use the previous axiomatic characterization.

### The top Chern class

In fact, these properties uniquely characterize the Chern classes. They imply, among other things:

- If *n* is the complex rank of *V*, then $c_{k}(V)=0$ for all *k* > *n*. Thus the total Chern class terminates.
- The top Chern class of *V* (meaning $c_{n}(V)$ , where *n* is the rank of *V*) is always equal to the Euler class of the underlying real vector bundle.

## In algebraic geometry

### Axiomatic description

There is another construction of Chern classes which take values in the algebrogeometric analogue of the cohomology ring, the Chow ring.

Let X be a nonsingular quasi-projective variety of dimension n . It can be shown that there is a unique theory of Chern classes which assigns an algebraic vector bundle $E\to X$ to elements $c_{i}(E)\in A^{i}(X)$ called Chern classes, with Chern polynomial $c_{t}(E)=c_{0}(E)+c_{1}(E)t+\cdots +c_{n}(E)t^{n}$ , satisfying the following (similar to Grothendieck's axiomatic approach).

1. If for a Cartier divisor D , we have $E\cong {\mathcal {O}}_{X}(D)$ , then $c_{t}(E)=1+Dt$ .
2. If $f:X'\to X$ is a morphism, then $c_{i}(f^{*}E)=f^{*}c_{i}(E)$ .
3. If $0\to E'\to E\to E''\to 0$ is an exact sequence of vector bundles on X , the Whitney sum formula holds: $c_{t}(E)=c_{t}(E')c_{t}(E'')$ .

### Normal sequence

Computing the characteristic classes for projective space forms the basis for many characteristic class computations since for any smooth projective subvariety $X\subset \mathbb {P} ^{n}$ there is the short exact sequence $0\to {\mathcal {T}}_{X}\to {\mathcal {T}}_{\mathbb {P} ^{n}}|_{X}\to {\mathcal {N}}_{X/\mathbb {P} ^{n}}\to 0$

#### Quintic threefold

For example, consider a nonsingular quintic threefold in $\mathbb {P} ^{4}$ . Its normal bundle is given by ${\mathcal {O}}_{X}(5)$ and we have the short exact sequence $0\to {\mathcal {T}}_{X}\to {\mathcal {T}}_{\mathbb {P} ^{4}}|_{X}\to {\mathcal {O}}_{X}(5)\to 0$

Let h denote the hyperplane class in $A^{\bullet }(X)$ . Then the Whitney sum formula gives us that $c({\mathcal {T}}_{X})c({\mathcal {O}}_{X}(5))=(1+h)^{5}=1+5h+10h^{2}+10h^{3}$

Since the Chow ring of a hypersurface is difficult to compute, we will consider this sequence as a sequence of coherent sheaves in $\mathbb {P} ^{4}$ . This gives us that ${\begin{aligned}c({\mathcal {T}}_{X})&={\frac {1+5h+10h^{2}+10h^{3}}{1+5h}}\\&=\left(1+5h+10h^{2}+10h^{3}\right)\left(1-5h+25h^{2}-125h^{3}\right)\\&=1+10h^{2}-40h^{3}\end{aligned}}$

Using the Gauss-Bonnet theorem we can integrate the class $c_{3}({\mathcal {T}}_{X})$ to compute the Euler characteristic. Traditionally this is called the Euler class. This is $\int _{[X]}c_{3}({\mathcal {T}}_{X})=\int _{[X]}-40h^{3}=-200$ since the class of $h^{3}$ can be represented by five points (by Bézout's theorem). The Euler characteristic can then be used to compute the Betti numbers for the cohomology of X by using the definition of the Euler characteristic and using the Lefschetz hyperplane theorem.

#### Degree d hypersurfaces

If $X\subset \mathbb {P} ^{3}$ is a degree d smooth hypersurface, we have the short exact sequence $0\to {\mathcal {T}}_{X}\to {\mathcal {T}}_{\mathbb {P} ^{3}}|_{X}\to {\mathcal {O}}_{X}(d)\to 0$ giving the relation $c({\mathcal {T}}_{X})={\frac {c({\mathcal {T}}_{\mathbb {P} ^{3}|_{X}})}{c({\mathcal {O}}_{X}(d))}}$ we can then calculate this as ${\begin{aligned}c({\mathcal {T}}_{X})&={\frac {(1+[H])^{4}}{(1+d[H])}}\\&=(1+4[H]+6[H]^{2})(1-d[H]+d^{2}[H]^{2})\\&=1+(4-d)[H]+(6-4d+d^{2})[H]^{2}\end{aligned}}$ Giving the total chern class. In particular, we can find X is a spin 4-manifold if $4-d$ is even, so every smooth hypersurface of degree $2k$ is a spin manifold.

## Proximate notions

### The Chern character

Chern classes can be used to construct a homomorphism of rings from the topological K-theory of a space to (the completion of) its rational cohomology. For a line bundle *L*, the Chern character ch is defined by

$\operatorname {ch} (L)=\exp(c_{1}(L)):=\sum _{m=0}^{\infty }{\frac {c_{1}(L)^{m}}{m!}}.$

More generally, if $V=L_{1}\oplus \cdots \oplus L_{n}$ is a direct sum of line bundles, with first Chern classes $x_{i}=c_{1}(L_{i}),$ the Chern character is defined additively $\operatorname {ch} (V)=e^{x_{1}}+\cdots +e^{x_{n}}:=\sum _{m=0}^{\infty }{\frac {1}{m!}}(x_{1}^{m}+\cdots +x_{n}^{m}).$

This can be rewritten as:

$\operatorname {ch} (V)=\operatorname {rk} (V)+c_{1}(V)+{\frac {1}{2}}(c_{1}(V)^{2}-2c_{2}(V))+{\frac {1}{6}}(c_{1}(V)^{3}-3c_{1}(V)c_{2}(V)+3c_{3}(V))+\cdots .$

This last expression, justified by invoking the splitting principle, is taken as the definition *ch(V)* for arbitrary vector bundles *V*.

If a connection is used to define the Chern classes when the base is a manifold (i.e., the Chern–Weil theory), then the explicit form of the Chern character is $\operatorname {ch} (V)=\left[\operatorname {tr} \left(\exp \left({\frac {i\Omega }{2\pi }}\right)\right)\right]$ where Ω is the curvature of the connection.

The Chern character is useful in part because it facilitates the computation of the Chern class of a tensor product. Specifically, it obeys the following identities:

$\operatorname {ch} (V\oplus W)=\operatorname {ch} (V)+\operatorname {ch} (W)$ $\operatorname {ch} (V\otimes W)=\operatorname {ch} (V)\operatorname {ch} (W).$

As stated above, using the Grothendieck additivity axiom for Chern classes, the first of these identities can be generalized to state that *ch* is a homomorphism of abelian groups from the K-theory *K*(*X*) into the rational cohomology of *X*. The second identity establishes the fact that this homomorphism also respects products in *K*(*X*), and so *ch* is a homomorphism of rings.

The Chern character is used in the Hirzebruch–Riemann–Roch theorem.

### Chern numbers

If we work on an oriented manifold of dimension $2n$ , then any product of Chern classes of total degree $2n$ (i.e., the sum of indices of the Chern classes in the product should be n ) can be paired with the orientation homology class (or "integrated over the manifold") to give an integer, a **Chern number** of the vector bundle. For example, if the manifold has dimension 6, there are three linearly independent Chern numbers, given by $c_{1}^{3}$ , $c_{1}c_{2}$ , and $c_{3}$ . In general, if the manifold has dimension $2n$ , the number of possible independent Chern numbers is the number of partitions of n .

The Chern numbers of the tangent bundle of a complex (or almost complex) manifold are called the Chern numbers of the manifold, and are important invariants.

### Generalized cohomology theories

There is a generalization of the theory of Chern classes, where ordinary cohomology is replaced with a generalized cohomology theory. The theories for which such generalization is possible are called *complex orientable*. The formal properties of the Chern classes remain the same, with one crucial difference: the rule which computes the first Chern class of a tensor product of line bundles in terms of first Chern classes of the factors is not (ordinary) addition, but rather a formal group law.

### Algebraic geometry

In algebraic geometry there is a similar theory of Chern classes of vector bundles. There are several variations depending on what groups the Chern classes lie in:

- For complex varieties the Chern classes can take values in ordinary cohomology, as above.
- For varieties over general fields, the Chern classes can take values in cohomology theories such as etale cohomology or l-adic cohomology.
- For varieties *V* over general fields the Chern classes can also take values in homomorphisms of Chow groups CH(V): for example, the first Chern class of a line bundle over a variety *V* is a homomorphism from CH(*V*) to CH(*V*) reducing degrees by 1. This corresponds to the fact that the Chow groups are a sort of analog of homology groups, and elements of cohomology groups can be thought of as homomorphisms of homology groups using the cap product.

### Manifolds with structure

The theory of Chern classes gives rise to cobordism invariants for almost complex manifolds.

If *M* is an almost complex manifold, then its tangent bundle is a complex vector bundle. The **Chern classes** of *M* are thus defined to be the Chern classes of its tangent bundle. If *M* is also compact and of dimension 2*d*, then each monomial of total degree 2*d* in the Chern classes can be paired with the fundamental class of *M*, giving an integer, a **Chern number** of *M*. If *M*′ is another almost complex manifold of the same dimension, then it is cobordant to *M* if and only if the Chern numbers of *M*′ coincide with those of *M*.

The theory also extends to real symplectic vector bundles, by the intermediation of compatible almost complex structures. In particular, symplectic manifolds have a well-defined Chern class.

### Arithmetic schemes and Diophantine equations

(See Arakelov geometry)
