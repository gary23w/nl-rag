---
title: "Banach space (part 1/2)"
source: https://en.wikipedia.org/wiki/Banach_space
domain: functional-analysis
license: CC-BY-SA-4.0
tags: functional analysis, hilbert space, banach space, linear operator
fetched: 2026-07-02
part: 1/2
---

# Banach space

In mathematics, more specifically in functional analysis, a **Banach space** (/ˈbɑː.nʌx/, Polish pronunciation: [ˈba.nax]) is a complete normed vector space. Thus, a Banach space is a vector space with a metric that allows the computation of vector length and distance between vectors and is complete in the sense that a Cauchy sequence of vectors always converges to a well-defined limit that is within the space.

Banach spaces are named after the Polish mathematician Stefan Banach, who introduced this concept and studied it systematically in 1920–1922 along with Hans Hahn and Eduard Helly. Maurice René Fréchet was the first to use the term "Banach space" and Banach in turn then coined the term "Fréchet space". Banach spaces originally grew out of the study of function spaces by Hilbert, Fréchet, and Riesz earlier in the century. Banach spaces play a central role in functional analysis. In other areas of analysis, the spaces under study are often Banach spaces.


## Definition

A **Banach space** is a complete normed space $(X,\|{\cdot }\|).$ A normed space is a pair $(X,\|{\cdot }\|)$ consisting of a vector space X over a scalar field $\mathbb {K}$ (where $\mathbb {K}$ is commonly $\mathbb {R}$ or $\mathbb {C}$ ) together with a distinguished norm $\|{\cdot }\|:X\to \mathbb {R} .$ Like all norms, this norm induces a translation invariant distance function, called the *canonical* or *(norm) induced metric*, defined for all vectors $x,y\in X$ by $d(x,y):=\|y-x\|=\|x-y\|.$ This makes X into a metric space $(X,d).$ A sequence $x_{1},x_{2},\ldots$ is called *Cauchy in $(X,d)$* or *d -Cauchy* or *$\|{\cdot }\|$ -Cauchy* if for every real $r>0,$ there exists some index N such that, for m and n are greater than N $d(x_{n},x_{m})=\|x_{n}-x_{m}\|<r.$ The normed space $(X,\|{\cdot }\|)$ is called a **Banach space** and the canonical metric d is called a *complete metric* if $(X,d)$ is a complete metric space, which by definition means for every Cauchy sequence $x_{1},x_{2},\ldots$ in $(X,d),$ there exists some $x\in X$ such that $\lim _{n\to \infty }x_{n}=x\;{\text{ in }}(X,d),$ where because $\|x_{n}-x\|=d(x_{n},x),$ this sequence's convergence to x can equivalently be expressed as $\lim _{n\to \infty }\|x_{n}-x\|=0\;{\text{ in }}\mathbb {R} .$

The norm $\|{\cdot }\|$ of a normed space $(X,\|{\cdot }\|)$ is called a **complete norm** if $(X,\|{\cdot }\|)$ is a Banach space.

### L-semi-inner product

For any normed space $(X,\|{\cdot }\|),$ there exists an L-semi-inner product $\langle \cdot ,\cdot \rangle$ on X such that ${\textstyle \|x\|={\sqrt {\langle x,x\rangle }}}$ for all $x\in X.$ In general, there may be infinitely many L-semi-inner products that satisfy this condition and the proof of the existence of L-semi-inner products relies on the non-constructive Hahn–Banach theorem. L-semi-inner products are a generalization of inner products, which are what fundamentally distinguish Hilbert spaces from all other Banach spaces. This shows that all normed spaces (and hence all Banach spaces) can be considered as being generalizations of (pre-)Hilbert spaces.

### Characterization in terms of series

The vector space structure allows one to relate the behavior of Cauchy sequences to that of converging series of vectors. A normed space X is a Banach space if and only if each absolutely convergent series in X converges to a value that lies within $X,$ symbolically $\sum _{n=1}^{\infty }\|v_{n}\|<\infty \implies \sum _{n=1}^{\infty }v_{n}{\text{ converges in }}X.$

### Topology

The canonical metric d of a normed space $(X,\|{\cdot }\|)$ induces the usual metric topology $\tau _{d}$ on $X,$ which is referred to as the *canonical* or *norm induced topology*. Every normed space is automatically assumed to carry this Hausdorff topology, unless indicated otherwise. With this topology, every Banach space is a Baire space, although there exist normed spaces that are Baire but not Banach. The norm $\|{\cdot }\|:X\to \mathbb {R}$ is always a continuous function with respect to the topology that it induces.

The open and closed balls of radius $r>0$ centered at a point $x\in X$ are, respectively, the sets $B_{r}(x):=\{z\in X\mid \|z-x\|<r\}\qquad {\text{ and }}\qquad C_{r}(x):=\{z\in X\mid \|z-x\|\leq r\}.$ Any such ball is a convex and bounded subset of $X,$ but a compact ball/neighborhood exists if and only if X is finite-dimensional. In particular, no infinite–dimensional normed space can be locally compact or have the Heine–Borel property. If $x_{0}$ is a vector and $s\neq 0$ is a scalar, then $x_{0}+s\,B_{r}(x)=B_{|s|r}(x_{0}+sx)\qquad {\text{ and }}\qquad x_{0}+s\,C_{r}(x)=C_{|s|r}(x_{0}+sx).$ Using $s=1$ shows that the norm-induced topology is translation invariant, which means that for any $x\in X$ and $S\subseteq X,$ the subset S is open (respectively, closed) in X if and only if its translation $x+S:=\{x+s\mid s\in S\}$ is open (respectively, closed). Consequently, the norm induced topology is completely determined by any neighbourhood basis at the origin. Some common neighborhood bases at the origin include $\{B_{r}(0)\mid r>0\},\qquad \{C_{r}(0)\mid r>0\},\qquad \{B_{r_{n}}(0)\mid n\in \mathbb {N} \},\qquad {\text{ and }}\qquad \{C_{r_{n}}(0)\mid n\in \mathbb {N} \},$ where $r_{1},r_{2},\ldots$ can be any sequence of positive real numbers that converges to 0 in $\mathbb {R}$ (common choices are $r_{n}:={\tfrac {1}{n}}$ or $r_{n}:=1/2^{n}$ ). So, for example, any open subset U of X can be written as a union $U=\bigcup _{x\in I}B_{r_{x}}(x)=\bigcup _{x\in I}x+B_{r_{x}}(0)=\bigcup _{x\in I}x+r_{x}\,B_{1}(0)$ indexed by some subset $I\subseteq U,$ where each $r_{x}$ may be chosen from the aforementioned sequence $r_{1},r_{2},\ldots .$ (The open balls can also be replaced with closed balls, although the indexing set I and radii $r_{x}$ may then also need to be replaced). Additionally, I can always be chosen to be countable if X is a *separable space*, which by definition means that X contains some countable dense subset.

#### Homeomorphism classes of separable Banach spaces

All finite–dimensional normed spaces are separable Banach spaces and any two Banach spaces of the same finite dimension are linearly homeomorphic. Every separable infinite–dimensional Hilbert space is linearly isometrically isomorphic to the separable Hilbert sequence space $\ell ^{2}(\mathbb {N} )$ with its usual norm $\|{\cdot }\|_{2}.$

The Anderson–Kadec theorem states that every infinite–dimensional separable Fréchet space is homeomorphic to the product space ${\textstyle \prod _{i\in \mathbb {N} }\mathbb {R} }$ of countably many copies of $\mathbb {R}$ (this homeomorphism need not be a linear map). Thus all infinite–dimensional separable Fréchet spaces are homeomorphic to each other (or said differently, their topology is unique up to a homeomorphism). Since every Banach space is a Fréchet space, this is also true of all infinite–dimensional separable Banach spaces, including $\ell ^{2}(\mathbb {N} ).$ In fact, $\ell ^{2}(\mathbb {N} )$ is even homeomorphic to its own unit *sphere* $\{x\in \ell ^{2}(\mathbb {N} )\mid \|x\|_{2}=1\},$ which stands in sharp contrast to finite–dimensional spaces (the Euclidean plane $\mathbb {R} ^{2}$ is not homeomorphic to the unit circle, for instance).

This pattern in homeomorphism classes extends to generalizations of metrizable (locally Euclidean) topological manifolds known as *metric Banach manifolds*, which are metric spaces that are around every point, locally homeomorphic to some open subset of a given Banach space (metric Hilbert manifolds and metric Fréchet manifolds are defined similarly). For example, every open subset U of a Banach space X is canonically a metric Banach manifold modeled on X since the inclusion map $U\to X$ is an open local homeomorphism. Using Hilbert space microbundles, David Henderson showed in 1969 that every metric manifold modeled on a separable infinite–dimensional Banach (or Fréchet) space can be topologically embedded as an *open* subset of $\ell ^{2}(\mathbb {N} )$ and, consequently, also admits a unique smooth structure making it into a $C^{\infty }$ Hilbert manifold.

#### Compact and convex subsets

There is a compact subset S of $\ell ^{2}(\mathbb {N} )$ whose convex hull $\operatorname {co} (S)$ is *not* closed and thus also *not* compact. However, like in all Banach spaces, the *closed* convex hull ${\overline {\operatorname {co} }}S$ of this (and every other) compact subset will be compact. In a normed space that is not complete then it is in general *not* guaranteed that ${\overline {\operatorname {co} }}S$ will be compact whenever S is; an example can even be found in a (non-complete) pre-Hilbert vector subspace of $\ell ^{2}(\mathbb {N} ).$

#### As a topological vector space

This norm-induced topology also makes $(X,\tau _{d})$ into what is known as a topological vector space (TVS), which by definition is a vector space endowed with a topology making the operations of addition and scalar multiplication continuous. It is emphasized that the TVS $(X,\tau _{d})$ is *only* a vector space together with a certain type of topology; that is to say, when considered as a TVS, it is *not* associated with *any* particular norm or metric (both of which are "forgotten"). This Hausdorff TVS $(X,\tau _{d})$ is even locally convex because the set of all open balls centered at the origin forms a neighbourhood basis at the origin consisting of convex balanced open sets. This TVS is also *normable*, which by definition refers to any TVS whose topology is induced by some (possibly unknown) norm. Normable TVSs are characterized by being Hausdorff and having a bounded convex neighborhood of the origin. All Banach spaces are barrelled spaces, which means that every barrel is neighborhood of the origin (all closed balls centered at the origin are barrels, for example) and guarantees that the Banach–Steinhaus theorem holds.

#### Comparison of complete metrizable vector topologies

The open mapping theorem implies that when $\tau _{1}$ and $\tau _{2}$ are topologies on X that make both $(X,\tau _{1})$ and $(X,\tau _{2})$ into complete metrizable TVSes (for example, Banach or Fréchet spaces), if one topology is finer or coarser than the other, then they must be equal (that is, if $\tau _{1}\subseteq \tau _{2}$ or $\tau _{2}\subseteq \tau _{1}$ then $\tau _{1}=\tau _{2}$ ). So, for example, if $(X,p)$ and $(X,q)$ are Banach spaces with topologies $\tau _{p}$ and $\tau _{q},$ and if one of these spaces has some open ball that is also an open subset of the other space (or, equivalently, if one of $p:(X,\tau _{q})\to \mathbb {R}$ or $q:(X,\tau _{p})\to \mathbb {R}$ is continuous), then their topologies are identical and the norms p and q are equivalent.

### Completeness

#### Complete norms and equivalent norms

Two norms, p and $q,$ on a vector space X are said to be *equivalent* if they induce the same topology; this happens if and only if there exist real numbers $c,C>0$ such that ${\textstyle c\,q(x)\leq p(x)\leq C\,q(x)}$ for all $x\in X.$ If p and q are two equivalent norms on a vector space X then $(X,p)$ is a Banach space if and only if $(X,q)$ is a Banach space. See this footnote for an example of a continuous norm on a Banach space that is *not* equivalent to that Banach space's given norm. All norms on a finite-dimensional vector space are equivalent and every finite-dimensional normed space is a Banach space.

#### Complete norms vs complete metrics

A metric D on a vector space X is induced by a norm on X if and only if D is translation invariant and *absolutely homogeneous*, which means that $D(sx,sy)=|s|D(x,y)$ for all scalars s and all $x,y\in X,$ in which case the function $\|x\|:=D(x,0)$ defines a norm on X and the canonical metric induced by $\|{\cdot }\|$ is equal to $D.$

Suppose that $(X,\|{\cdot }\|)$ is a normed space and that $\tau$ is the norm topology induced on $X.$ Suppose that D is *any* metric on X such that the topology that D induces on X is equal to $\tau .$ If D is translation invariant then $(X,\|{\cdot }\|)$ is a Banach space if and only if $(X,D)$ is a complete metric space. If D is *not* translation invariant, then it may be possible for $(X,\|{\cdot }\|)$ to be a Banach space but for $(X,D)$ to *not* be a complete metric space (see this footnote for an example). In contrast, a theorem of Klee, which also applies to all metrizable topological vector spaces, implies that if there exists *any* complete metric D on X that induces the norm topology $\tau$ on $X,$ then $(X,\|{\cdot }\|)$ is a Banach space.

A Fréchet space is a locally convex topological vector space whose topology is induced by some translation-invariant complete metric. Every Banach space is a Fréchet space but not conversely; indeed, there even exist Fréchet spaces on which no norm is a continuous function (such as the space of real sequences ${\textstyle \mathbb {R} ^{\mathbb {N} }=\prod _{i\in \mathbb {N} }\mathbb {R} }$ with the product topology). However, the topology of every Fréchet space is induced by some countable family of real-valued (necessarily continuous) maps called seminorms, which are generalizations of norms. It is even possible for a Fréchet space to have a topology that is induced by a countable family of *norms* (such norms would necessarily be continuous) but to not be a Banach/normable space because its topology can not be defined by any *single* norm. An example of such a space is the Fréchet space $C^{\infty }(K),$ whose definition can be found in the article on spaces of test functions and distributions.

#### Complete norms vs complete topological vector spaces

There is another notion of completeness besides metric completeness and that is the notion of a complete topological vector space (TVS) or TVS-completeness, which uses the theory of uniform spaces. Specifically, the notion of TVS-completeness uses a unique translation-invariant uniformity, called the canonical uniformity, that depends *only* on vector subtraction and the topology $\tau$ that the vector space is endowed with, and so in particular, this notion of TVS completeness is independent of whatever norm induced the topology $\tau$ (and even applies to TVSs that are *not* even metrizable). Every Banach space is a complete TVS. Moreover, a normed space is a Banach space (that is, its norm-induced metric is complete) if and only if it is complete as a topological vector space. If $(X,\tau )$ is a metrizable topological vector space (such as any norm induced topology, for example), then $(X,\tau )$ is a complete TVS if and only if it is a *sequentially* complete TVS, meaning that it is enough to check that every Cauchy *sequence* in $(X,\tau )$ converges in $(X,\tau )$ to some point of X (that is, there is no need to consider the more general notion of arbitrary Cauchy nets).

If $(X,\tau )$ is a topological vector space whose topology is induced by *some* (possibly unknown) norm (such spaces are called *normable*), then $(X,\tau )$ is a complete topological vector space if and only if X may be assigned a norm $\|{\cdot }\|$ that induces on X the topology $\tau$ and also makes $(X,\|{\cdot }\|)$ into a Banach space. A Hausdorff locally convex topological vector space X is normable if and only if its strong dual space $X'_{b}$ is normable, in which case $X'_{b}$ is a Banach space ( $X'_{b}$ denotes the strong dual space of $X,$ whose topology is a generalization of the dual norm-induced topology on the continuous dual space $X'$ ; see this footnote for more details). If X is a metrizable locally convex TVS, then X is normable if and only if $X'_{b}$ is a Fréchet–Urysohn space. This shows that in the category of locally convex TVSs, Banach spaces are exactly those complete spaces that are both metrizable and have metrizable strong dual spaces.

#### Completions

Every normed space can be isometrically embedded onto a dense vector subspace of a Banach space, where this Banach space is called a *completion* of the normed space. This Hausdorff completion is unique up to isometric isomorphism.

More precisely, for every normed space $X,$ there exists a Banach space Y and a mapping $T:X\to Y$ such that T is an isometric mapping and $T(X)$ is dense in $Y.$ If Z is another Banach space such that there is an isometric isomorphism from X onto a dense subset of $Z,$ then Z is isometrically isomorphic to $Y.$ The Banach space Y is the Hausdorff *completion* of the normed space $X.$ The underlying metric space for Y is the same as the metric completion of $X,$ with the vector space operations extended from X to $Y.$ The completion of X is sometimes denoted by ${\widehat {X}}.$


## General theory

### Linear operators, isomorphisms

If X and Y are normed spaces over the same ground field $\mathbb {K} ,$ the set of all continuous $\mathbb {K}$ -linear maps $T:X\to Y$ is denoted by $B(X,Y).$ In infinite-dimensional spaces, not all linear maps are continuous. A linear mapping from a normed space X to another normed space is continuous if and only if it is bounded on the closed unit ball of $X.$ Thus, the vector space $B(X,Y)$ can be given the operator norm $\|T\|=\sup\{\|Tx\|_{Y}\mid x\in X,\ \|x\|_{X}\leq 1\}.$

For Y a Banach space, the space $B(X,Y)$ is a Banach space with respect to this norm. In categorical contexts, it is sometimes convenient to restrict the function space between two Banach spaces to only the short maps; in that case the space $B(X,Y)$ reappears as a natural bifunctor.

If X is a Banach space, the space $B(X)=B(X,X)$ forms a unital Banach algebra; the multiplication operation is given by the composition of linear maps.

If X and Y are normed spaces, they are **isomorphic normed spaces** if there exists a linear bijection $T:X\to Y$ such that T and its inverse $T^{-1}$ are continuous. If one of the two spaces X or Y is complete (or reflexive, separable, etc.) then so is the other space. Two normed spaces X and Y are *isometrically isomorphic* if in addition, T is an isometry, that is, $\|T(x)\|=\|x\|$ for every x in $X.$ The Banach–Mazur distance $d(X,Y)$ between two isomorphic but not isometric spaces X and Y gives a measure of how much the two spaces X and Y differ.

#### Continuous and bounded linear functions and seminorms

Every continuous linear operator is a bounded linear operator and if dealing only with normed spaces then the converse is also true. That is, a linear operator between two normed spaces is bounded if and only if it is a continuous function. So in particular, because the scalar field (which is $\mathbb {R}$ or $\mathbb {C}$ ) is a normed space, a linear functional on a normed space is a bounded linear functional if and only if it is a continuous linear functional. This allows for continuity-related results (like those below) to be applied to Banach spaces. Although boundedness is the same as continuity for linear maps between normed spaces, the term "bounded" is more commonly used when dealing primarily with Banach spaces.

If $f:X\to \mathbb {R}$ is a subadditive function (such as a norm, a sublinear function, or real linear functional), then f is continuous at the origin if and only if f is uniformly continuous on all of X ; and if in addition $f(0)=0$ then f is continuous if and only if its absolute value $|f|:X\to [0,\infty )$ is continuous, which happens if and only if $\{x\in X\mid |f(x)|<1\}$ is an open subset of $X.$ And very importantly for applying the Hahn–Banach theorem, a linear functional f is continuous if and only if this is true of its real part $\operatorname {Re} f$ and moreover, $\|\operatorname {Re} f\|=\|f\|$ and the real part $\operatorname {Re} f$ completely determines $f,$ which is why the Hahn–Banach theorem is often stated only for real linear functionals. Also, a linear functional f on X is continuous if and only if the seminorm $|f|$ is continuous, which happens if and only if there exists a continuous seminorm $p:X\to \mathbb {R}$ such that $|f|\leq p$ ; this last statement involving the linear functional f and seminorm p is encountered in many versions of the Hahn–Banach theorem.

### Basic notions

The Cartesian product $X\times Y$ of two normed spaces is not canonically equipped with a norm. However, several equivalent norms are commonly used, such as $\|(x,y)\|_{1}=\|x\|+\|y\|,\qquad \|(x,y)\|_{\infty }=\max(\|x\|,\|y\|)$ which correspond (respectively) to the coproduct and product in the category of Banach spaces and short maps (discussed above). For finite (co)products, these norms give rise to isomorphic normed spaces, and the product $X\times Y$ (or the direct sum $X\oplus Y$ ) is complete if and only if the two factors are complete.

If M is a closed linear subspace of a normed space $X,$ there is a natural norm on the quotient space $X/M,$ $\|x+M\|=\inf \limits _{m\in M}\|x+m\|.$

The quotient $X/M$ is a Banach space when X is complete. The quotient map from X onto $X/M,$ sending $x\in X$ to its class $x+M,$ is linear, onto, and of norm $1,$ except when $M=X,$ in which case the quotient is the null space.

The closed linear subspace M of X is said to be a *complemented subspace* of X if M is the range of a surjective bounded linear projection $P:X\to M.$ In this case, the space X is isomorphic to the direct sum of M and $\ker P,$ the kernel of the projection $P.$

Suppose that X and Y are Banach spaces and that $T\in B(X,Y).$ There exists a canonical factorization of T as $T=T_{1}\circ \pi ,\quad T:X{\overset {\pi }{{}\longrightarrow {}}}X/\ker T{\overset {T_{1}}{{}\longrightarrow {}}}Y$ where the first map $\pi$ is the quotient map, and the second map $T_{1}$ sends every class $x+\ker T$ in the quotient to the image $T(x)$ in $Y.$ This is well defined because all elements in the same class have the same image. The mapping $T_{1}$ is a linear bijection from $X/\ker T$ onto the range $T(X),$ whose inverse need not be bounded.

### Classical spaces

Basic examples of Banach spaces include: the Lp spaces $L^{p}$ and their special cases, the sequence spaces $\ell ^{p}$ that consist of scalar sequences indexed by natural numbers $\mathbb {N}$ ; among them, the space $\ell ^{1}$ of absolutely summable sequences and the space $\ell ^{2}$ of square summable sequences; the space $c_{0}$ of sequences tending to zero and the space $\ell ^{\infty }$ of bounded sequences; the space $C(K)$ of continuous scalar functions on a compact Hausdorff space $K,$ equipped with the max norm, $\|f\|_{C(K)}=\max\{|f(x)|\mid x\in K\},\quad f\in C(K).$

According to the Banach–Mazur theorem, every Banach space is isometrically isomorphic to a subspace of some $C(K).$ For every separable Banach space $X,$ there is a closed subspace M of $\ell ^{1}$ such that $X:=\ell ^{1}/M.$

Any Hilbert space serves as an example of a Banach space. A Hilbert space H on $\mathbb {K} =\mathbb {R} ,\mathbb {C}$ is complete for a norm of the form $\|x\|_{H}={\sqrt {\langle x,x\rangle }},$ where $\langle \cdot ,\cdot \rangle :H\times H\to \mathbb {K}$ is the inner product, linear in its first argument that satisfies the following: ${\begin{aligned}\langle y,x\rangle &={\overline {\langle x,y\rangle }},\quad {\text{ for all }}x,y\in H\\\langle x,x\rangle &\geq 0,\quad {\text{ for all }}x\in H\\\langle x,x\rangle =0{\text{ if and only if }}x&=0.\end{aligned}}$

For example, the space $L^{2}$ is a Hilbert space.

The Hardy spaces, the Sobolev spaces are examples of Banach spaces that are related to $L^{p}$ spaces and have additional structure. They are important in different branches of analysis, Harmonic analysis and Partial differential equations among others.

### Banach algebras

A *Banach algebra* is a Banach space A over $\mathbb {K} =\mathbb {R}$ or $\mathbb {C} ,$ together with a structure of algebra over $\mathbb {K}$ , such that the product map $A\times A\ni (a,b)\mapsto ab\in A$ is continuous. An equivalent norm on A can be found so that $\|ab\|\leq \|a\|\|b\|$ for all $a,b\in A.$

#### Examples

- The Banach space $C(K)$ with the pointwise product, is a Banach algebra.
- The disk algebra $A(\mathbf {D} )$ consists of functions holomorphic in the open unit disk $D\subseteq \mathbb {C}$ and continuous on its closure: ${\overline {\mathbf {D} }}.$ Equipped with the max norm on ${\overline {\mathbf {D} }},$ the disk algebra $A(\mathbf {D} )$ is a closed subalgebra of $C\left({\overline {\mathbf {D} }}\right).$
- The Wiener algebra $A(\mathbf {T} )$ is the algebra of functions on the unit circle $\mathbf {T}$ with absolutely convergent Fourier series. Via the map associating a function on $\mathbf {T}$ to the sequence of its Fourier coefficients, this algebra is isomorphic to the Banach algebra $\ell ^{1}(Z),$ where the product is the convolution of sequences.
- For every Banach space $X,$ the space $B(X)$ of bounded linear operators on $X,$ with the composition of maps as product, is a Banach algebra.
- A C*-algebra is a complex Banach algebra A with an antilinear involution $a\mapsto a^{*}$ such that $\|a^{*}a\|=\|a\|^{2}.$ The space $B(H)$ of bounded linear operators on a Hilbert space H is a fundamental example of C*-algebra. The Gelfand–Naimark theorem states that every C*-algebra is isometrically isomorphic to a C*-subalgebra of some $B(H).$ The space $C(K)$ of complex continuous functions on a compact Hausdorff space K is an example of commutative C*-algebra, where the involution associates to every function f its complex conjugate ${\overline {f}}.$

### Dual space

If X is a normed space and $\mathbb {K}$ the underlying field (either the reals or the complex numbers), the *continuous dual space* is the space of continuous linear maps from X into $\mathbb {K} ,$ or *continuous linear functionals*. The notation for the continuous dual is $X'=B(X,\mathbb {K} )$ in this article. Since $\mathbb {K}$ is a Banach space (using the absolute value as norm), the dual $X'$ is a Banach space, for every normed space $X.$ The Dixmier–Ng theorem characterizes the dual spaces of Banach spaces.

The main tool for proving the existence of continuous linear functionals is the Hahn–Banach theorem.

**Hahn–Banach theorem**—Let X be a vector space over the field $\mathbb {K} =\mathbb {R} ,\mathbb {C} .$ Let further

- $Y\subseteq X$ be a linear subspace,
- $p:X\to \mathbb {R}$ be a sublinear function and
- $f:Y\to \mathbb {K}$ be a linear functional so that $\operatorname {Re} (f(y))\leq p(y)$ for all $y\in Y.$

Then, there exists a linear functional $F:X\to \mathbb {K}$ so that $F{\big \vert }_{Y}=f,\quad {\text{ and }}\quad {\text{ for all }}x\in X,\ \ \operatorname {Re} (F(x))\leq p(x).$

In particular, every continuous linear functional on a subspace of a normed space can be continuously extended to the whole space, without increasing the norm of the functional. An important special case is the following: for every vector x in a normed space $X,$ there exists a continuous linear functional f on X such that $f(x)=\|x\|_{X},\quad \|f\|_{X'}\leq 1.$

When x is not equal to the $\mathbf {0}$ vector, the functional f must have norm one, and is called a *norming functional* for $x.$

The Hahn–Banach separation theorem states that two disjoint non-empty convex sets in a real Banach space, one of them open, can be separated by a closed affine hyperplane. The open convex set lies strictly on one side of the hyperplane, the second convex set lies on the other side but may touch the hyperplane.

A subset S in a Banach space X is *total* if the linear span of S is dense in $X.$ The subset S is total in X if and only if the only continuous linear functional that vanishes on S is the $\mathbf {0}$ functional: this equivalence follows from the Hahn–Banach theorem.

If X is the direct sum of two closed linear subspaces M and $N,$ then the dual $X'$ of X is isomorphic to the direct sum of the duals of M and $N.$ If M is a closed linear subspace in $X,$ one can associate the *orthogonal of* M in the dual, $M^{\bot }=\{x'\in X\mid x'(m)=0{\text{ for all }}m\in M\}.$

The orthogonal $M^{\bot }$ is a closed linear subspace of the dual. The dual of M is isometrically isomorphic to $X'/M^{\bot }.$ The dual of $X/M$ is isometrically isomorphic to $M^{\bot }.$

The dual of a separable Banach space need not be separable, but:

**Theorem**—Let X be a normed space. If $X'$ is separable, then X is separable.

When $X'$ is separable, the above criterion for totality can be used for proving the existence of a countable total subset in $X.$

#### Weak topologies

The *weak topology* on a Banach space X is the coarsest topology on X for which all elements $x'$ in the continuous dual space $X'$ are continuous. The norm topology is therefore finer than the weak topology. It follows from the Hahn–Banach separation theorem that the weak topology is Hausdorff, and that a norm-closed convex subset of a Banach space is also weakly closed. A norm-continuous linear map between two Banach spaces X and Y is also *weakly continuous*, that is, continuous from the weak topology of X to that of $Y.$

If X is infinite-dimensional, there exist linear maps which are not continuous. The space $X^{*}$ of all linear maps from X to the underlying field $\mathbb {K}$ (this space $X^{*}$ is called the algebraic dual space, to distinguish it from $X'$ also induces a topology on X which is finer than the weak topology, and much less used in functional analysis.

On a dual space $X',$ there is a topology weaker than the weak topology of $X',$ called the *weak* topology*. It is the coarsest topology on $X'$ for which all evaluation maps $x'\in X'\mapsto x'(x),$ where x ranges over $X,$ are continuous. Its importance comes from the Banach–Alaoglu theorem.

**Banach–Alaoglu theorem**—Let X be a normed vector space. Then the closed unit ball $B=\{x\in X\mid \|x\|\leq 1\}$ of the dual space is compact in the weak* topology.

The Banach–Alaoglu theorem can be proved using Tychonoff's theorem about infinite products of compact Hausdorff spaces. When X is separable, the unit ball $B'$ of the dual is a metrizable compact in the weak* topology.

#### Examples of dual spaces

The dual of $c_{0}$ is isometrically isomorphic to $\ell ^{1}$ : for every bounded linear functional f on $c_{0},$ there is a unique element $y=\{y_{n}\}\in \ell ^{1}$ such that $f(x)=\sum _{n\in \mathbb {N} }x_{n}y_{n},\qquad x=\{x_{n}\}\in c_{0},\ \ {\text{and}}\ \ \|f\|_{(c_{0})'}=\|y\|_{\ell _{1}}.$

The dual of $\ell ^{1}$ is isometrically isomorphic to $\ell ^{\infty }$ . The dual of Lebesgue space $L^{p}([0,1])$ is isometrically isomorphic to $L^{q}([0,1])$ when $1\leq p<\infty$ and ${\frac {1}{p}}+{\frac {1}{q}}=1.$

For every vector y in a Hilbert space $H,$ the mapping $x\in H\to f_{y}(x)=\langle x,y\rangle$

defines a continuous linear functional $f_{y}$ on $H.$ The Riesz representation theorem states that every continuous linear functional on H is of the form $f_{y}$ for a uniquely defined vector y in $H.$ The mapping $y\in H\to f_{y}$ is an antilinear isometric bijection from H onto its dual $H'.$ When the scalars are real, this map is an isometric isomorphism.

When K is a compact Hausdorff topological space, the dual $M(K)$ of $C(K)$ is the space of Radon measures in the sense of Bourbaki. The subset $P(K)$ of $M(K)$ consisting of non-negative measures of mass 1 (probability measures) is a convex w*-closed subset of the unit ball of $M(K).$ The extreme points of $P(K)$ are the Dirac measures on $K.$ The set of Dirac measures on $K,$ equipped with the w*-topology, is homeomorphic to $K.$

**Banach–Stone Theorem**—If K and L are compact Hausdorff spaces and if $C(K)$ and $C(L)$ are isometrically isomorphic, then the topological spaces K and L are homeomorphic.

The result has been extended by Amir and Cambern to the case when the multiplicative Banach–Mazur distance between $C(K)$ and $C(L)$ is $<2.$ The theorem is no longer true when the distance is $=2.$

In the commutative Banach algebra $C(K),$ the maximal ideals are precisely kernels of Dirac measures on $K,$ $I_{x}=\ker \delta _{x}=\{f\in C(K)\mid f(x)=0\},\quad x\in K.$

More generally, by the Gelfand–Mazur theorem, the maximal ideals of a unital commutative Banach algebra can be identified with its characters—not merely as sets but as topological spaces: the former with the hull-kernel topology and the latter with the w*-topology. In this identification, the maximal ideal space can be viewed as a w*-compact subset of the unit ball in the dual $A'.$

**Theorem**—If K is a compact Hausdorff space, then the maximal ideal space $\Xi$ of the Banach algebra $C(K)$ is homeomorphic to $K.$

Not every unital commutative Banach algebra is of the form $C(K)$ for some compact Hausdorff space $K.$ However, this statement holds if one places $C(K)$ in the smaller category of commutative C*-algebras. Gelfand's representation theorem for commutative C*-algebras states that every commutative unital *C**-algebra A is isometrically isomorphic to a $C(K)$ space. The Hausdorff compact space K here is again the maximal ideal space, also called the spectrum of A in the C*-algebra context.

#### Bidual

If X is a normed space, the (continuous) dual $X''$ of the dual $X'$ is called the **bidual** or **second dual** of $X.$ For every normed space $X,$ there is a natural map, ${\begin{cases}F_{X}\colon X\to X''\\F_{X}(x)(f)=f(x)&{\text{ for all }}x\in X,{\text{ and for all }}f\in X'\end{cases}}$

This defines $F_{X}(x)$ as a continuous linear functional on $X',$ that is, an element of $X''.$ The map $F_{X}\colon x\to F_{X}(x)$ is a linear map from X to $X''.$ As a consequence of the existence of a norming functional f for every $x\in X,$ this map $F_{X}$ is isometric, thus injective.

For example, the dual of $X=c_{0}$ is identified with $\ell ^{1},$ and the dual of $\ell ^{1}$ is identified with $\ell ^{\infty },$ the space of bounded scalar sequences. Under these identifications, $F_{X}$ is the inclusion map from $c_{0}$ to $\ell ^{\infty }.$ It is indeed isometric, but not onto.

If $F_{X}$ is surjective, then the normed space X is called *reflexive* (see below). Being the dual of a normed space, the bidual $X''$ is complete, therefore, every reflexive normed space is a Banach space.

Using the isometric embedding $F_{X},$ it is customary to consider a normed space X as a subset of its bidual. When X is a Banach space, it is viewed as a closed linear subspace of $X''.$ If X is not reflexive, the unit ball of X is a proper subset of the unit ball of $X''.$ The Goldstine theorem states that the unit ball of a normed space is weakly*-dense in the unit ball of the bidual. In other words, for every $x''$ in the bidual, there exists a net $(x_{i})_{i\in I}$ in X so that $\sup _{i\in I}\|x_{i}\|\leq \|x''\|,\ \ x''(f)=\lim _{i}f(x_{i}),\quad f\in X'.$

The net may be replaced by a weakly*-convergent sequence when the dual $X'$ is separable. On the other hand, elements of the bidual of $\ell ^{1}$ that are not in $\ell ^{1}$ cannot be weak*-limit of *sequences* in $\ell ^{1},$ since $\ell ^{1}$ is weakly sequentially complete.

### Banach's theorems

Here are the main general results about Banach spaces that go back to the time of Banach's book (Banach (1932)) and are related to the Baire category theorem. According to this theorem, a complete metric space (such as a Banach space, a Fréchet space or an F-space) cannot be equal to a union of countably many closed subsets with empty interiors. Therefore, a Banach space cannot be the union of countably many closed subspaces, unless it is already equal to one of them; a Banach space with a countable Hamel basis is finite-dimensional.

**Banach–Steinhaus Theorem**—Let X be a Banach space and Y be a normed vector space. Suppose that F is a collection of continuous linear operators from X to $Y.$ The uniform boundedness principle states that if for all x in X we have $\sup _{T\in F}\|T(x)\|_{Y}<\infty ,$ then $\sup _{T\in F}\|T\|_{Y}<\infty .$

The Banach–Steinhaus theorem is not limited to Banach spaces. It can be extended for example to the case where X is a Fréchet space, provided the conclusion is modified as follows: under the same hypothesis, there exists a neighborhood U of $\mathbf {0}$ in X such that all T in F are uniformly bounded on $U,$ $\sup _{T\in F}\sup _{x\in U}\;\|T(x)\|_{Y}<\infty .$

**The Open Mapping Theorem**—Let X and Y be Banach spaces and $T:X\to Y$ be a surjective continuous linear operator, then T is an open map.

**Corollary**—Every one-to-one bounded linear operator from a Banach space onto a Banach space is an isomorphism.

**The First Isomorphism Theorem for Banach spaces**—Suppose that X and Y are Banach spaces and that $T\in B(X,Y).$ Suppose further that the range of T is closed in $Y.$ Then $X/\ker T$ is isomorphic to $T(X).$

This result is a direct consequence of the preceding *Banach isomorphism theorem* and of the canonical factorization of bounded linear maps.

**Corollary**—If a Banach space X is the internal direct sum of closed subspaces $M_{1},\ldots ,M_{n},$ then X is isomorphic to $M_{1}\oplus \cdots \oplus M_{n}.$

This is another consequence of Banach's isomorphism theorem, applied to the continuous bijection from $M_{1}\oplus \cdots \oplus M_{n}$ onto X sending $m_{1},\cdots ,m_{n}$ to the sum $m_{1}+\cdots +m_{n}.$

**The Closed Graph Theorem**—Let $T:X\to Y$ be a linear mapping between Banach spaces. The graph of T is closed in $X\times Y$ if and only if T is continuous.

### Reflexivity

The normed space X is called *reflexive* when the natural map ${\begin{cases}F_{X}:X\to X''\\F_{X}(x)(f)=f(x)&{\text{ for all }}x\in X,{\text{ and for all }}f\in X'\end{cases}}$ is surjective. Reflexive normed spaces are Banach spaces.

**Theorem**—If X is a reflexive Banach space, every closed subspace of X and every quotient space of X are reflexive.

This is a consequence of the Hahn–Banach theorem. Further, by the open mapping theorem, if there is a bounded linear operator from the Banach space X onto the Banach space $Y,$ then Y is reflexive.

**Theorem**—If X is a Banach space, then X is reflexive if and only if $X'$ is reflexive.

**Corollary**—Let X be a reflexive Banach space. Then X is separable if and only if $X'$ is separable.

Indeed, if the dual $Y'$ of a Banach space Y is separable, then Y is separable. If X is reflexive and separable, then the dual of $X'$ is separable, so $X'$ is separable.

**Theorem**—Suppose that $X_{1},\ldots ,X_{n}$ are normed spaces and that $X=X_{1}\oplus \cdots \oplus X_{n}.$ Then X is reflexive if and only if each $X_{j}$ is reflexive.

Hilbert spaces are reflexive. The $L^{p}$ spaces are reflexive when $1<p<\infty .$ More generally, uniformly convex spaces are reflexive, by the Milman–Pettis theorem. The spaces $c_{0},\ell ^{1},L^{1}([0,1]),C([0,1])$ are not reflexive. In these examples of non-reflexive spaces $X,$ the bidual $X''$ is "much larger" than $X.$ Namely, under the natural isometric embedding of X into $X''$ given by the Hahn–Banach theorem, the quotient $X''/X$ is infinite-dimensional, and even nonseparable. However, Robert C. James has constructed an example of a non-reflexive space, usually called "*the James space*" and denoted by $J,$ such that the quotient $J''/J$ is one-dimensional. Furthermore, this space J is isometrically isomorphic to its bidual.

**Theorem**—A Banach space X is reflexive if and only if its unit ball is compact in the weak topology.

When X is reflexive, it follows that all closed and bounded convex subsets of X are weakly compact. In a Hilbert space $H,$ the weak compactness of the unit ball is very often used in the following way: every bounded sequence in H has weakly convergent subsequences.

Weak compactness of the unit ball provides a tool for finding solutions in reflexive spaces to certain optimization problems. For example, every convex continuous function on the unit ball B of a reflexive space attains its minimum at some point in $B.$

As a special case of the preceding result, when X is a reflexive space over $\mathbb {R} ,$ every continuous linear functional f in $X'$ attains its maximum $\|f\|$ on the unit ball of $X.$ The following theorem of Robert C. James provides a converse statement.

**James' Theorem**—For a Banach space the following two properties are equivalent:

- X is reflexive.
- for all f in $X'$ there exists $x\in X$ with $\|x\|\leq 1,$ so that $f(x)=\|f\|.$

The theorem can be extended to give a characterization of weakly compact convex sets.

On every non-reflexive Banach space $X,$ there exist continuous linear functionals that are not *norm-attaining*. However, the Bishop–Phelps theorem states that norm-attaining functionals are norm dense in the dual $X'$ of $X.$

### Weak convergences of sequences

A sequence $\{x_{n}\}$ in a Banach space X is *weakly convergent* to a vector $x\in X$ if $\{f(x_{n})\}$ converges to $f(x)$ for every continuous linear functional f in the dual $X'.$ The sequence $\{x_{n}\}$ is a *weakly Cauchy sequence* if $\{f(x_{n})\}$ converges to a scalar limit $L(f)$ for every f in $X'.$ A sequence $\{f_{n}\}$ in the dual $X'$ is *weakly* convergent* to a functional $f\in X'$ if $f_{n}(x)$ converges to $f(x)$ for every x in $X.$ Weakly Cauchy sequences, weakly convergent and weakly* convergent sequences are norm bounded, as a consequence of the Banach–Steinhaus theorem.

When the sequence $\{x_{n}\}$ in X is a weakly Cauchy sequence, the limit L above defines a bounded linear functional on the dual $X',$ that is, an element L of the bidual of $X,$ and L is the limit of $\{x_{n}\}$ in the weak*-topology of the bidual. The Banach space X is *weakly sequentially complete* if every weakly Cauchy sequence is weakly convergent in $X.$ It follows from the preceding discussion that reflexive spaces are weakly sequentially complete.

**Theorem**—For every measure $\mu ,$ the space $L^{1}(\mu )$ is weakly sequentially complete.

An orthonormal sequence in a Hilbert space is a simple example of a weakly convergent sequence, with limit equal to the $\mathbf {0}$ vector. The unit vector basis of $\ell ^{p}$ for $1<p<\infty ,$ or of $c_{0},$ is another example of a *weakly null sequence*, that is, a sequence that converges weakly to $\mathbf {0} .$ For every weakly null sequence in a Banach space, there exists a sequence of convex combinations of vectors from the given sequence that is norm-converging to $\mathbf {0} .$

The unit vector basis of $\ell ^{1}$ is not weakly Cauchy. Weakly Cauchy sequences in $\ell ^{1}$ are weakly convergent, since $L^{1}$ -spaces are weakly sequentially complete. Actually, weakly convergent sequences in $\ell ^{1}$ are norm convergent. This means that $\ell ^{1}$ satisfies Schur's property.

#### Results involving the 𝓁1 basis

Weakly Cauchy sequences and the $\ell ^{1}$ basis are the opposite cases of the dichotomy established in the following deep result of Haskell P. Rosenthal.

**Theorem**—Let $\{x_{n}\}_{n\in \mathbb {N} }$ be a bounded sequence in a Banach space. Either $\{x_{n}\}_{n\in \mathbb {N} }$ has a weakly Cauchy subsequence, or it admits a subsequence equivalent to the standard unit vector basis of $\ell ^{1}.$

A complement to this result is due to Odell and Rosenthal (1975).

**Theorem**—Let X be a separable Banach space. The following are equivalent:

- The space X does not contain a closed subspace isomorphic to $\ell ^{1}.$
- Every element of the bidual $X''$ is the weak*-limit of a sequence $\{x_{n}\}$ in $X.$

By the Goldstine theorem, every element of the unit ball $B''$ of $X''$ is weak*-limit of a net in the unit ball of $X.$ When X does not contain $\ell ^{1},$ every element of $B''$ is weak*-limit of a *sequence* in the unit ball of $X.$

When the Banach space X is separable, the unit ball of the dual $X',$ equipped with the weak*-topology, is a metrizable compact space $K,$ and every element $x''$ in the bidual $X''$ defines a bounded function on K : $x'\in K\mapsto x''(x'),\quad |x''(x')|\leq \|x''\|.$

This function is continuous for the compact topology of K if and only if $x''$ is actually in $X,$ considered as subset of $X''.$ Assume in addition for the rest of the paragraph that X does not contain $\ell ^{1}.$ By the preceding result of Odell and Rosenthal, the function $x''$ is the pointwise limit on K of a sequence $\{x_{n}\}\subseteq X$ of continuous functions on $K,$ it is therefore a first Baire class function on $K.$ The unit ball of the bidual is a pointwise compact subset of the first Baire class on $K.$

#### Sequences, weak and weak* compactness

When X is separable, the unit ball of the dual is weak*-compact by the Banach–Alaoglu theorem and metrizable for the weak* topology, hence every bounded sequence in the dual has weakly* convergent subsequences. This applies to separable reflexive spaces, but more is true in this case, as stated below.

The weak topology of a Banach space X is metrizable if and only if X is finite-dimensional. If the dual $X'$ is separable, the weak topology of the unit ball of X is metrizable. This applies in particular to separable reflexive Banach spaces. Although the weak topology of the unit ball is not metrizable in general, one can characterize weak compactness using sequences.

**Eberlein–Šmulian theorem**—A set A in a Banach space is relatively weakly compact if and only if every sequence $\{a_{n}\}$ in A has a weakly convergent subsequence.

A Banach space X is reflexive if and only if each bounded sequence in X has a weakly convergent subsequence.

A weakly compact subset A in $\ell ^{1}$ is norm-compact. Indeed, every sequence in A has weakly convergent subsequences by Eberlein–Šmulian, that are norm convergent by the Schur property of $\ell ^{1}.$

### Type and cotype

A way to classify Banach spaces is through the probabilistic notion of type and cotype, these two measure how far a Banach space is from a Hilbert space.
