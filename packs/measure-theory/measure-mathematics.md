---
title: "Measure (mathematics)"
source: https://en.wikipedia.org/wiki/Measure_(mathematics)
domain: measure-theory
license: CC-BY-SA-4.0
tags: measure theory, lebesgue integration, lebesgue measure, borel set
fetched: 2026-07-02
---

# Measure (mathematics)

In mathematics, the concept of a **measure** is a generalization and formalization of geometrical measures (length, area, volume) and other common notions, such as magnitude, mass, and probability of events. These seemingly distinct concepts have many similarities and can often be treated together in a single mathematical context. Measures are foundational in probability theory, integration theory, and can be generalized to assume negative values, as with electrical charge. Far-reaching generalizations (such as spectral measures and positive operator-valued measures) of measure are widely used in quantum physics and physics in general.

The intuition behind this concept dates back to Ancient Greece, when Archimedes tried to calculate the area of a circle. But it was not until the late 19th and early 20th centuries that measure theory became a branch of mathematics. The foundations of modern measure theory were laid in the works of Émile Borel, Henri Lebesgue, Nikolai Luzin, Johann Radon, Constantin Carathéodory, and Maurice Fréchet, among others. According to Thomas W. Hawkins Jr., "It was primarily through the theory of multiple integrals and, in particular the work of Camille Jordan that the importance of the notion of measurability was first recognized."

## Definition

Let X be a set and $\Sigma$ a σ-algebra over X , defining subsets of X that are "measurable". A set function $\mu$ from $\Sigma$ to the extended real number line, that is, the real number line together with new (so-called infinite) values $+\infty$ and $-\infty$ , respectively greater and lower than all other (so-called finite) elements, is called a **measure** if the following conditions hold:

- $\mu (\varnothing )=0$
- **Non-negativity**: For all $E\in \Sigma ,\ \ \mu (E)\geq 0$
- **Countable additivity** (or σ-additivity): For all countable collections $\{E_{k}\}_{k=1}^{\infty }$ of pairwise disjoint sets in $\Sigma$ , $\mu {\left(\bigcup _{k=1}^{\infty }E_{k}\right)}=\sum _{k=1}^{\infty }\mu (E_{k})$

If at least one set E has finite measure, then the requirement $\mu (\varnothing )=0$ is met automatically due to countable additivity: $\mu (E)=\mu (E\cup \varnothing )=\mu (E)+\mu (\varnothing ),$ and therefore $\mu (\varnothing )=0.$

Note that any sum involving $+\infty$ will equal $+\infty$ , that is, $a+\infty =+\infty$ for all a in the extended reals.

If the condition of non-negativity is dropped, and $\mu (E)$ only ever equals one of $+\infty$ , $-\infty$ , i.e. no two distinct sets have measures $+\infty$ , $-\infty$ , respectively, then $\mu$ is called a *signed measure*.

The pair $(X,\Sigma )$ is called a *measurable space*, and the members of $\Sigma$ are called **measurable sets**.

A triple $(X,\Sigma ,\mu )$ is called a *measure space*. A probability measure is a measure with total measure one – that is, $\mu (X)=1.$ A probability space is a measure space with a probability measure.

For measure spaces that are also topological spaces various compatibility conditions can be placed for the measure and the topology. Most measures met in practice in analysis (and in many cases also in probability theory) are Radon measures (usually defined on Hausdorff spaces). When working with locally compact Hausdorff spaces, Radon measures have an alternative, equivalent definition in terms of linear functionals on the locally convex topological vector space of continuous functions with compact support. This approach is taken by Bourbaki (2004) and a number of other sources. For more details, see the article on Radon measures.

## Instances

Some important measures are listed here.

- The counting measure is defined by $\mu (S)$ = number of elements in $S.$
- The Lebesgue measure on $\mathbb {R}$ is a complete translation-invariant measure on a *σ*-algebra containing the intervals in $\mathbb {R}$ such that $\mu ([0,1])=1$ ; and every other measure with these properties extends the Lebesgue measure.
- The arc length of an interval on the unit circle in the Euclidean plane extends to a measure on the $\sigma$ -algebra they generate. It can be called angle measure since the arc length of an interval equals the angle it supports. This measure is invariant under rotations preserving the circle. Similarly, hyperbolic angle measure is invariant under squeeze mapping.
- The Haar measure for a locally compact topological group. For example, $\mathbb {R}$ is such a group and its Haar measure is the Lebesgue measure; for the unit circle (seen as a subgroup of the multiplicative group of $\mathbb {C}$ ) its Haar measure is the angle measure. For a discrete group the counting measure is a Haar measure.
- Every (pseudo) Riemannian manifold $(M,g)$ has a canonical measure $\mu _{g}$ that in local coordinates $x_{1},\ldots ,x_{n}$ looks like ${\sqrt {\left|\det g\right|}}d^{n}x$ where $d^{n}x$ is the usual Lebesgue measure.
- The Hausdorff measure is a generalization of the Lebesgue measure to sets with non-integer dimension, in particular, fractal sets.
- Every probability space gives rise to a measure which takes the value 1 on the whole space (and therefore takes all its values in the unit interval [0, 1]). Such a measure is called a *probability measure* or *distribution*. See the list of probability distributions for instances.
- The Dirac measure *δ**a* (cf. Dirac delta function) is given by *δ**a*(*S*) = *χ**S*(a), where *χ**S* is the indicator function of $S.$ The measure of a set is 1 if it contains the point a and 0 otherwise.

Other 'named' measures used in various theories include: Borel measure, Jordan measure, ergodic measure, Gaussian measure, Baire measure, Radon measure, Young measure, and Loeb measure.

In physics an example of a measure is spatial distribution of mass (see for example, gravity potential), or another non-negative extensive property, conserved (see conservation law for a list of these) or not. Negative values lead to signed measures, see "generalizations" below.

- Liouville measure, known also as the natural volume form on a symplectic manifold, is useful in classical statistical and Hamiltonian mechanics.
- Gibbs measure is widely used in statistical mechanics, often under the name canonical ensemble.

## Basic properties

Let $\mu$ be a measure.

### Monotonicity

If $E_{1}$ and $E_{2}$ are measurable sets with $E_{1}\subseteq E_{2}$ then $\mu (E_{1})\leq \mu (E_{2}).$

### Measure of countable unions and intersections

#### Countable subadditivity

For any countable sequence $E_{1},E_{2},E_{3},\ldots$ of (not necessarily disjoint) measurable sets $E_{n}$ in $\Sigma :$ $\mu \left(\bigcup _{i=1}^{\infty }E_{i}\right)\leq \sum _{i=1}^{\infty }\mu (E_{i}).$

#### Continuity from below

If $E_{1},E_{2},E_{3},\ldots$ are measurable sets that are increasing (meaning that $E_{1}\subseteq E_{2}\subseteq E_{3}\subseteq \ldots$ ) then the union of the sets $E_{n}$ is measurable and $\mu \left(\bigcup _{i=1}^{\infty }E_{i}\right)~=~\lim _{i\to \infty }\mu (E_{i})=\sup _{i\geq 1}\mu (E_{i}).$

#### Continuity from above

If $E_{1},E_{2},E_{3},\ldots$ are measurable sets that are decreasing (meaning that $E_{1}\supseteq E_{2}\supseteq E_{3}\supseteq \ldots$ ) then the intersection of the sets $E_{n}$ is measurable; furthermore, if at least one of the $E_{n}$ has finite measure then $\mu \left(\bigcap _{i=1}^{\infty }E_{i}\right)=\lim _{i\to \infty }\mu (E_{i})=\inf _{i\geq 1}\mu (E_{i}).$

This property is false without the assumption that at least one of the $E_{n}$ has finite measure. For instance, for each $n\in \mathbb {N} ,$ let $E_{n}=[n,\infty )\subseteq \mathbb {R} ,$ which all have infinite Lebesgue measure, but the intersection is empty.

## Other properties

### Completeness

A measurable set X is called a *null set* if $\mu (X)=0.$ A subset of a null set is called a *negligible set*. A negligible set need not be measurable, but every measurable negligible set is automatically a null set. A measure is called *complete* if every negligible set is measurable.

A measure can be extended to a complete one by considering the σ-algebra of subsets Y which differ by a negligible set from a measurable set $X,$ that is, such that the symmetric difference of X and Y is contained in a null set. One defines $\mu (Y)$ to equal $\mu (X).$

### "Dropping the edge"

If $f:X\to [0,+\infty ]$ is $(\Sigma ,{\cal {B}}([0,+\infty ]))$ -measurable, then $\mu \{x\in X:f(x)\geq t\}=\mu \{x\in X:f(x)>t\}$ for almost all $t\in [-\infty ,\infty ].$ This property is used in connection with Lebesgue integral.

Proof

Both $F(t):=\mu \{x\in X:f(x)>t\}$ and $G(t):=\mu \{x\in X:f(x)\geq t\}$ are monotonically non-increasing functions of $t,$ so both of them have at most countably many discontinuities and thus they are continuous almost everywhere, relative to the Lebesgue measure. If $t<0$ then $\{x\in X:f(x)\geq t\}=X=\{x\in X:f(x)>t\},$ so that $F(t)=G(t),$ as desired.

If t is such that $\mu \{x\in X:f(x)>t\}=+\infty$ then monotonicity implies $\mu \{x\in X:f(x)\geq t\}=+\infty ,$ so that $F(t)=G(t),$ as required. If $\mu \{x\in X:f(x)>t\}=+\infty$ for all t then we are done, so assume otherwise. Then there is a unique $t_{0}\in \{-\infty \}\cup [0,+\infty )$ such that F is infinite to the left of t (which can only happen when $t_{0}\geq 0$ ) and finite to the right. Arguing as above, $\mu \{x\in X:f(x)\geq t\}=+\infty$ when $t<t_{0}.$ Similarly, if $t_{0}\geq 0$ and $F\left(t_{0}\right)=+\infty$ then $F\left(t_{0}\right)=G\left(t_{0}\right).$

For $t>t_{0},$ let $t_{n}$ be a monotonically non-decreasing sequence converging to $t.$ The monotonically non-increasing sequences $\{x\in X:f(x)>t_{n}\}$ of members of $\Sigma$ has at least one finitely $\mu$ -measurable component, and $\{x\in X:f(x)\geq t\}=\bigcap _{n}\{x\in X:f(x)>t_{n}\}.$ Continuity from above guarantees that $\mu \{x\in X:f(x)\geq t\}=\lim _{t_{n}\uparrow t}\mu \{x\in X:f(x)>t_{n}\}.$ The right-hand side $\lim _{t_{n}\uparrow t}F\left(t_{n}\right)$ then equals $F(t)=\mu \{x\in X:f(x)>t\}$ if t is a point of continuity of $F.$ Since F is continuous almost everywhere, this completes the proof.

### Additivity

Measures are required to be countably additive. However, the condition can be strengthened as follows. For any set I and any set of nonnegative $r_{i}$ where $i\in I$ define: $\sum _{i\in I}r_{i}=\sup \left\lbrace \sum _{i\in J}r_{i}:|J|<\infty ,J\subseteq I\right\rbrace .$ That is, we define the sum of the $r_{i}$ to be the supremum of all the sums of finitely many of them.

A measure $\mu$ on $\Sigma$ is $\kappa$ -additive if for any $\lambda <\kappa$ and any family of disjoint sets $X_{\alpha },\alpha <\lambda$ the following hold: $\bigcup _{\alpha \in \lambda }X_{\alpha }\in \Sigma$ $\mu \left(\bigcup _{\alpha \in \lambda }X_{\alpha }\right)=\sum _{\alpha \in \lambda }\mu \left(X_{\alpha }\right).$ The second condition is equivalent to the statement that the ideal of null sets is $\kappa$ -complete.

### Sigma-finite measures

A measure space $(X,\Sigma ,\mu )$ is called finite if $\mu (X)$ is a finite real number (rather than $\infty$ ). A measure $\mu$ is called *σ-finite* if X can be decomposed into a countable union of measurable sets of finite measure.

For example, the real numbers with the standard Lebesgue measure are σ-finite but not finite. The natural numbers are also σ-finite with respect to counting measure. However, the real numbers are not σ-finite with respect to counting measure.

### Strictly localizable measures

### Semifinite measures

Let X be a set, let ${\cal {A}}$ be a sigma-algebra on $X,$ and let $\mu$ be a measure on ${\cal {A}}.$ We say $\mu$ is **semifinite** to mean that for all $A\in \mu ^{\text{pre}}\{+\infty \},$ ${\cal {P}}(A)\cap \mu ^{\text{pre}}(\mathbb {R} _{>0})\neq \emptyset .$

Semifinite measures generalize sigma-finite measures, in such a way that some big theorems of measure theory that hold for sigma-finite but not arbitrary measures can be extended with little modification to hold for semifinite measures. (To-do: add examples of such theorems; cf. the talk page.)

#### Basic examples

- Every sigma-finite measure is semifinite.
- Assume ${\cal {A}}={\cal {P}}(X),$ let $f:X\to [0,+\infty ],$ and assume $\mu (A)=\sum _{a\in A}f(a)$ for all $A\subseteq X.$
  - We have that $\mu$ is sigma-finite if and only if $f(x)<+\infty$ for all $x\in X$ and $f^{\text{pre}}(\mathbb {R} _{>0})$ is countable. We have that $\mu$ is semifinite if and only if $f(x)<+\infty$ for all $x\in X.$
  - Taking $f=X\times \{1\}$ above (so that $\mu$ is counting measure on ${\cal {P}}(X)$ ), we see that counting measure on ${\cal {P}}(X)$ is
    - sigma-finite if and only if X is countable; and
    - semifinite (without regard to whether X is countable). (Thus, counting measure, on the power set ${\cal {P}}(X)$ of an arbitrary uncountable set $X,$ gives an example of a semifinite measure that is not sigma-finite.)
- Let d be a complete, separable metric on $X,$ let ${\cal {B}}$ be the Borel sigma-algebra induced by $d,$ and let $s\in \mathbb {R} _{>0}.$ Then the Hausdorff measure ${\cal {H}}^{s}|{\cal {B}}$ is semifinite.
- Let d be a complete, separable metric on $X,$ let ${\cal {B}}$ be the Borel sigma-algebra induced by $d,$ and let $s\in \mathbb {R} _{>0}.$ Then the packing measure ${\cal {H}}^{s}|{\cal {B}}$ is semifinite.

#### Involved example

The zero measure is sigma-finite and thus semifinite. In addition, the zero measure is clearly less than or equal to $\mu .$ It can be shown there is a greatest measure with these two properties:

**Theorem (semifinite part)**—For any measure $\mu$ on ${\cal {A}},$ there exists, among semifinite measures on ${\cal {A}}$ that are less than or equal to $\mu ,$ a greatest element $\mu _{\text{sf}}.$

We say the **semifinite part** of $\mu$ to mean the semifinite measure $\mu _{\text{sf}}$ defined in the above theorem. We give some nice, explicit formulas, which some authors may take as definition, for the semifinite part:

- $\mu _{\text{sf}}=(\sup\{\mu (B):B\in {\cal {P}}(A)\cap \mu ^{\text{pre}}(\mathbb {R} _{\geq 0})\})_{A\in {\cal {A}}}.$
- $\mu _{\text{sf}}=(\sup\{\mu (A\cap B):B\in \mu ^{\text{pre}}(\mathbb {R} _{\geq 0})\})_{A\in {\cal {A}}}\}.$
- $\mu _{\text{sf}}=\mu |_{\mu ^{\text{pre}}(\mathbb {R} _{>0})}\cup \{A\in {\cal {A}}:\sup\{\mu (B):B\in {\cal {P}}(A)\}=+\infty \}\times \{+\infty \}\cup \{A\in {\cal {A}}:\sup\{\mu (B):B\in {\cal {P}}(A)\}<+\infty \}\times \{0\}.$

Since $\mu _{\text{sf}}$ is semifinite, it follows that if $\mu =\mu _{\text{sf}}$ then $\mu$ is semifinite. It is also evident that if $\mu$ is semifinite then $\mu =\mu _{\text{sf}}.$

#### Non-examples

Every *$0-\infty$ measure* that is not the zero measure is not semifinite. (Here, we say *$0-\infty$ measure* to mean a measure whose range lies in $\{0,+\infty \}$ : $(\forall A\in {\cal {A}})(\mu (A)\in \{0,+\infty \}).$ ) Below we give examples of $0-\infty$ measures that are not zero measures.

- Let X be nonempty, let ${\cal {A}}$ be a $\sigma$ -algebra on $X,$ let $f:X\to \{0,+\infty \}$ be not the zero function, and let $\mu =(\sum _{x\in A}f(x))_{A\in {\cal {A}}}.$ It can be shown that $\mu$ is a measure.
  - $\mu =\{(\emptyset ,0)\}\cup ({\cal {A}}\setminus \{\emptyset \})\times \{+\infty \}.$
    - $X=\{0\},$ ${\cal {A}}=\{\emptyset ,X\},$ $\mu =\{(\emptyset ,0),(X,+\infty )\}.$
- Let X be uncountable, let ${\cal {A}}$ be a $\sigma$ -algebra on $X,$ let ${\cal {C}}=\{A\in {\cal {A}}:A{\text{ is countable}}\}$ be the countable elements of ${\cal {A}},$ and let $\mu ={\cal {C}}\times \{0\}\cup ({\cal {A}}\setminus {\cal {C}})\times \{+\infty \}.$ It can be shown that $\mu$ is a measure.

#### Involved non-example

> Measures that are not semifinite are very wild when restricted to certain sets. Every measure is, in a sense, semifinite once its $0-\infty$ part (the wild part) is taken away.

— A. Mukherjea and K. Pothoven, *Real and Functional Analysis, Part A: Real Analysis* (1985)

**Theorem (Luther decomposition)**—For any measure $\mu$ on ${\cal {A}},$ there exists a $0-\infty$ measure $\xi$ on ${\cal {A}}$ such that $\mu =\nu +\xi$ for some semifinite measure $\nu$ on ${\cal {A}}.$ In fact, among such measures $\xi ,$ there exists a least measure $\mu _{0-\infty }.$ Also, we have $\mu =\mu _{\text{sf}}+\mu _{0-\infty }.$

We say the **$\mathbf {0-\infty }$ part** of $\mu$ to mean the measure $\mu _{0-\infty }$ defined in the above theorem. Here is an explicit formula for $\mu _{0-\infty }$ : $\mu _{0-\infty }=(\sup\{\mu (B)-\mu _{\text{sf}}(B):B\in {\cal {P}}(A)\cap \mu _{\text{sf}}^{\text{pre}}(\mathbb {R} _{\geq 0})\})_{A\in {\cal {A}}}.$

#### Results regarding semifinite measures

- Let $\mathbb {F}$ be $\mathbb {R}$ or $\mathbb {C} ,$ and let $T:L_{\mathbb {F} }^{\infty }(\mu )\to \left(L_{\mathbb {F} }^{1}(\mu )\right)^{*}:g\mapsto T_{g}=\left(\int fgd\mu \right)_{f\in L_{\mathbb {F} }^{1}(\mu )}.$ Then $\mu$ is semifinite if and only if T is injective. (This result has import in the study of the dual space of $L^{1}=L_{\mathbb {F} }^{1}(\mu )$ .)
- Let $\mathbb {F}$ be $\mathbb {R}$ or $\mathbb {C} ,$ and let ${\cal {T}}$ be the topology of convergence in measure on $L_{\mathbb {F} }^{0}(\mu ).$ Then $\mu$ is semifinite if and only if ${\cal {T}}$ is Hausdorff.
- (Johnson) Let X be a set, let ${\cal {A}}$ be a sigma-algebra on $X,$ let $\mu$ be a measure on ${\cal {A}},$ let Y be a set, let ${\cal {B}}$ be a sigma-algebra on $Y,$ and let $\nu$ be a measure on ${\cal {B}}.$ If $\mu ,\nu$ are both not a $0-\infty$ measure, then both $\mu$ and $\nu$ are semifinite if and only if $(\mu \times _{\text{cld}}\nu )$ $(A\times B)=\mu (A)\nu (B)$ for all $A\in {\cal {A}}$ and $B\in {\cal {B}}.$ (Here, $\mu \times _{\text{cld}}\nu$ is the measure defined in Theorem 39.1 in Berberian '65.)

### Localizable measures

Localizable measures are a special case of semifinite measures and a generalization of sigma-finite measures.

Let X be a set, let ${\cal {A}}$ be a sigma-algebra on $X,$ and let $\mu$ be a measure on ${\cal {A}}.$

- Let $\mathbb {F}$ be $\mathbb {R}$ or $\mathbb {C} ,$ and let $T:L_{\mathbb {F} }^{\infty }(\mu )\to \left(L_{\mathbb {F} }^{1}(\mu )\right)^{*}:g\mapsto T_{g}=\left(\int fgd\mu \right)_{f\in L_{\mathbb {F} }^{1}(\mu )}.$ Then $\mu$ is localizable if and only if T is bijective (if and only if $L_{\mathbb {F} }^{\infty }(\mu )$ "is" $L_{\mathbb {F} }^{1}(\mu )^{*}$ ).

### s-finite measures

A measure is said to be s-finite if it is a countable sum of finite measures. S-finite measures are more general than sigma-finite ones and have applications in the theory of stochastic processes.

## Non-measurable sets

If the axiom of choice is assumed to be true, it can be proved that not all subsets of Euclidean space are Lebesgue measurable; examples of such sets include the Vitali set, and the non-measurable sets postulated by the Hausdorff paradox and the Banach–Tarski paradox.

## Generalizations

For certain purposes, it is useful to have a "measure" whose values are not restricted to the non-negative reals or infinity. For instance, a countably additive set function with values in the (signed) real numbers is called a *signed measure*, while such a function with values in the complex numbers is called a *complex measure*. Observe, however, that complex measure is necessarily of finite variation, hence complex measures include finite signed measures but not, for example, the Lebesgue measure.

Measures that take values in Banach spaces have been studied extensively. A measure that takes values in the set of self-adjoint projections on a Hilbert space is called a *projection-valued measure*; these are used in functional analysis for the spectral theorem. When it is necessary to distinguish the usual measures which take non-negative values from generalizations, the term **positive measure** is used. Positive measures are closed under conical combination but not general linear combination, while signed measures are the linear closure of positive measures. More generally see measure theory in topological vector spaces.

Another generalization is the *finitely additive measure*, also known as a content. This is the same as a measure except that instead of requiring *countable* additivity we require only *finite* additivity. Historically, this definition was used first. It turns out that in general, finitely additive measures are connected with notions such as Banach limits, the dual of $L^{\infty }$ and the Stone–Čech compactification. All these are linked in one way or another to the axiom of choice. Contents remain useful in certain technical problems in geometric measure theory; this is the theory of Banach measures.

A *charge* is a generalization in both directions: it is a finitely additive, signed measure. (Cf. ba space for information about *bounded* charges, where we say a charge is *bounded* to mean its range is a bounded subset of *R*.)
