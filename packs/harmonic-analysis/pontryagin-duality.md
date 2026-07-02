---
title: "Pontryagin duality"
source: https://en.wikipedia.org/wiki/Pontryagin_duality
domain: harmonic-analysis
license: CC-BY-SA-4.0
tags: harmonic analysis, fourier transform, fourier series, pontryagin duality
fetched: 2026-07-02
---

# Pontryagin duality

In mathematics, **Pontryagin duality** is a duality between locally compact abelian groups that allows generalizing Fourier transform to all such groups, which include the circle group (the multiplicative group of complex numbers of modulus one), the finite abelian groups (with the discrete topology), and the additive group of the integers (also with the discrete topology), the real numbers, and every finite-dimensional vector space over the reals or a p-adic field.

The **Pontryagin dual** of a locally compact abelian group is the locally compact abelian topological group, consisting of the continuous group homomorphisms from the group to the circle group, with the operation of pointwise multiplication and the topology of uniform convergence on compact sets. The **Pontryagin duality theorem** establishes Pontryagin duality by stating that any locally compact abelian group is naturally isomorphic with its bidual (the dual of its dual). The Fourier inversion theorem is a special case of this theorem.

The subject is named after Lev Pontryagin, who laid down the foundations for the theory of locally compact abelian groups and their duality during his early mathematical works in 1934. Pontryagin's treatment relied on the groups being second-countable and either compact or discrete. This was improved to cover the general locally compact abelian groups by Egbert van Kampen in 1935 and André Weil in 1940.

## Introduction

Pontryagin duality places in a unified context a number of observations about functions on the real line or on finite abelian groups:

- Suitably regular complex-valued periodic functions on the real line have Fourier series and these functions can be recovered from their Fourier series;
- Suitably regular complex-valued functions on the real line have Fourier transforms that are also functions on the real line and, just as for periodic functions, these functions can be recovered from their Fourier transforms; and
- Complex-valued functions on a finite abelian group have discrete Fourier transforms, which are functions on the dual group, which is a (non-canonically) isomorphic group. Moreover, any function on a finite abelian group can be recovered from its discrete Fourier transform.

The theory, introduced by Lev Pontryagin and combined with the Haar measure introduced by John von Neumann, André Weil and others depends on the theory of the dual group of a locally compact abelian group.

It is analogous to the dual vector space of a vector space: a finite-dimensional vector space V and its dual vector space $V^{*}$ are not naturally isomorphic, but the endomorphism algebra (matrix algebra) of one is isomorphic to the opposite of the endomorphism algebra of the other: ${\text{End}}(V)\cong {{\text{End}}(V^{*})}^{\text{op}},$ via the transpose. Similarly, a group G and its dual group ${\widehat {G}}$ are not in general isomorphic, but their endomorphism rings are opposite to each other: ${\text{End}}(G)\cong {\text{End}}({\widehat {G}})^{\text{op}}$ . More categorically, this is not just an isomorphism of endomorphism algebras, but a contravariant equivalence of categories – see *§ Categorical considerations*.

## Definition

A topological group is a locally compact group if the underlying topological space is locally compact and Hausdorff; a topological group is *abelian* if the underlying group is abelian. Examples of locally compact abelian groups include finite abelian groups, the integers (both for the discrete topology, which is also induced by the usual metric), the real numbers, the circle group *T* (both with their usual metric topology), and also the *p*-adic numbers (with their usual *p*-adic topology).

For a locally compact abelian group G , the **Pontryagin dual** is the group ${\widehat {G}}$ of continuous group homomorphisms from G to the circle group T . That is, ${\widehat {G}}:=\operatorname {Hom} (G,T).$ The Pontryagin dual ${\widehat {G}}$ is usually endowed with the topology given by uniform convergence on compact sets (that is, the topology induced by the compact-open topology on the space of all continuous functions from G to T ).

### Historical development

Before 1938, several developments contributed to what became known as **Pontryagin duality**.

Pavel Alexandrov (late 1920s) developed the theory of inverse systems (projective limits) in topology, including so-called projection spectra. While not directly part of duality theory for topological groups, these methods introduced systematic use of limiting processes that later became important in the study of non-finitely generated groups and duality phenomena.

Alfréd Haar (1933) introduced Haar measure in *Der Maßbegriff in der Theorie der kontinuierlichen Gruppen*, providing a translation-invariant integration theory on locally compact groups. This became a fundamental tool for harmonic analysis and for the later formulation of Pontryagin duality in full generality.

Raymond Paley and Norbert Wiener (1933–1934), in work culminating in *Fourier Transforms in the Complex Domain* (1934), systematically studied Fourier transforms and characters of abelian groups (primarily discrete or Euclidean). They emphasized a duality between a group and its character group, though their framework did not yet extend to general locally compact abelian groups.

James Waddell Alexander II (1934–1935) clarified duality phenomena in algebraic topology and introduced early cohomological ideas, notably in *On the Chains of a Complex and Their Duals*. While not directly part of Pontryagin duality, this work contributed to the broader mathematical notion of duality.

John von Neumann (1934) studied almost periodic functions on groups and extended harmonic analysis beyond countable settings, removing certain separability assumptions and anticipating the need for a general locally compact framework.

Egbert van Kampen (1935), in *Locally Bicompact Abelian Groups and Their Character Groups*, refined the topology on character groups and removed countability restrictions, bringing the theory close to its modern formulation.

Claude Chevalley (1936) applied duality ideas in class field theory, demonstrating their arithmetic significance.

Finally, Lev Pontryagin (1931–1934) established the core results: the definition of the dual group as the group of continuous characters, the natural pairing between a locally compact abelian group and its dual, and the duality theorem identifying a group with its double dual in the compact and discrete cases. These results were soon extended to all locally compact abelian groups.

## Examples

- The Pontryagin dual of a finite cyclic group is isomorphic to itself.

${\widehat {\mathbb {Z} /n\mathbb {Z} }}\cong \mathbb {Z} /n\mathbb {Z}$

- The Pontryagin dual of the group of integers is the circle group, and the Pontryagin dual of the circle group is the group of integers.

${\widehat {\mathbb {Z} }}\cong T,~~{\widehat {T}}\cong \mathbb {Z}$

- The Pontryagin dual of the group of real numbers is itself.

${\widehat {\mathbb {R} }}\cong \mathbb {R}$

- The Pontryagin dual of the group of p-adic integers $\mathbb {Z} _{p}$ is the Prüfer p-group $\mathbb {Z} (p^{\infty })$ , and the Pontryagin dual of the Prüfer p-group is the group of p-adic integers.

${\widehat {\mathbb {Z} _{p}}}\cong \mathbb {Z} (p^{\infty }),~~{\widehat {\mathbb {Z} (p^{\infty })}}\cong \mathbb {Z} _{p}$

## Pontryagin duality theorem

**Theorem**—There is a canonical isomorphism $G\cong {\widehat {\widehat {G}}}$ between any locally compact abelian group G and its double dual.

Canonical means that there is a naturally defined map $\operatorname {ev} _{G}\colon G\to {\widehat {\widehat {G}}}$  ; more importantly, the map should be functorial in G . For the multiplicative character $\chi$ of the group G , the canonical isomorphism $\operatorname {ev} _{G}$ is defined on $x\in G$ as follows: $\operatorname {ev} _{G}(x)(\chi )=\chi (x)\in \mathbb {T} .$ That is, $\operatorname {ev} _{G}(x):(\chi \mapsto \chi (x)).$

In other words, each group element x is identified to the evaluation character on the dual. This is strongly analogous to the canonical isomorphism between a finite-dimensional vector space and its double dual, $V\cong V^{**}$ , and it is worth mentioning that any vector space V is an abelian group. If G is a finite abelian group, then $G\cong {\widehat {G}}$ but this isomorphism is not canonical. Making this statement precise (in general) requires thinking about dualizing not only on groups, but also on maps between the groups, in order to treat dualization as a functor and prove the identity functor and the dualization functor are not naturally equivalent. Also the duality theorem implies that for any group (not necessarily finite) the dualization functor is an exact functor.

## Pontryagin duality and the Fourier transform

### Haar measure

One of the most remarkable facts about a locally compact group G is that it carries an essentially unique natural measure, the Haar measure, which allows one to consistently measure the "size" of sufficiently regular subsets of G . "Sufficiently regular subset" here means a Borel set; that is, an element of the σ-algebra generated by the compact sets. More precisely, a **right Haar measure** on a locally compact group G is a countably additive measure μ defined on the Borel sets of G which is *right invariant* in the sense that $\mu (Ax)=\mu (A)$ for x an element of G and A a Borel subset of G and also satisfies some regularity conditions (spelled out in detail in the article on Haar measure). Except for positive scaling factors, a Haar measure on G is unique.

The Haar measure on G allows us to define the notion of integral for (complex-valued) Borel functions defined on the group. In particular, one may consider various *Lp* spaces associated to the Haar measure $\mu$ . Specifically, ${\mathcal {L}}_{\mu }^{p}(G)=\left\{(f:G\to \mathbb {C} )\ {\Big |}\ \int _{G}|f(x)|^{p}\ d\mu (x)<\infty \right\}.$

Note that, since any two Haar measures on G are equal up to a scaling factor, this $L^{p}$ -space is independent of the choice of Haar measure and thus perhaps could be written as $L^{p}(G)$ . However, the $L^{p}$ -norm on this space depends on the choice of Haar measure, so if one wants to talk about isometries it is important to keep track of the Haar measure being used.

### Fourier transform and Fourier inversion formula for *L*1-functions

The dual group of a locally compact abelian group is used as the underlying space for an abstract version of the Fourier transform. If $f\in L^{1}(G)$ , then the Fourier transform is the function ${\widehat {f}}$ on ${\widehat {G}}$ defined by ${\widehat {f}}(\chi )=\int _{G}f(x){\overline {\chi (x)}}\ d\mu (x),$ where the integral is relative to Haar measure $\mu$ on G . This is also denoted $({\mathcal {F}}f)(\chi )$ . Note the Fourier transform depends on the choice of Haar measure. It is not too difficult to show that the Fourier transform of an $L^{1}$ function on G is a bounded continuous function on ${\widehat {G}}$ which vanishes at infinity.

**Fourier Inversion Formula for $L^{1}$ -Functions**—For each Haar measure $\mu$ on G there is a unique Haar measure $\nu$ on ${\widehat {G}}$ such that whenever $f\in L^{1}(G)$ and ${\widehat {f}}\in L^{1}\left({\widehat {G}}\right)$ , we have $f(x)=\int _{\widehat {G}}{\widehat {f}}(\chi )\chi (x)\ d\nu (\chi )\qquad \mu {\text{-almost everywhere}}$ If f is continuous then this identity holds for all x .

The *inverse Fourier transform* of an integrable function on ${\widehat {G}}$ is given by ${\check {g}}(x)=\int _{\widehat {G}}g(\chi )\chi (x)\ d\nu (\chi ),$ where the integral is relative to the Haar measure $\nu$ on the dual group ${\widehat {G}}$ . The measure $\nu$ on ${\widehat {G}}$ that appears in the Fourier inversion formula is called the dual measure to $\mu$ and may be denoted ${\widehat {\mu }}$ .

The various Fourier transforms can be classified in terms of their domain and transform domain (the group and dual group) as follows (note that $\mathbb {T}$ is Circle group):

| Transform | Original domain, G | Transform domain, ${\hat {G}}$ | Measure, $\mu$ |
|---|---|---|---|
| Fourier transform | $\mathbb {R}$ | $\mathbb {R}$ | ${\text{Constant}}\times {\text{Lebesgue measure}}$ |
| Fourier series | $\mathbb {T}$ | $\mathbb {Z}$ | ${\text{Constant}}\times {\text{Lebesgue measure}}$ |
| Discrete-time Fourier transform (DTFT) | $\mathbb {Z}$ | $\mathbb {T}$ | ${\text{Constant}}\times {\text{Counting measure}}$ |
| Discrete Fourier transform (DFT) | $\mathbb {Z} _{n}$ | $\mathbb {Z} _{n}$ | ${\text{Constant}}\times {\text{Counting measure}}$ |

As an example, suppose $G=\mathbb {R} ^{n}$ , so we can think about ${\widehat {G}}$ as $\mathbb {R} ^{n}$ by the pairing $(\mathbf {v} ,\mathbf {w} )\mapsto e^{i\mathbf {v} \cdot \mathbf {w} }.$ If $\mu$ is the Lebesgue measure on Euclidean space, we obtain the ordinary Fourier transform on $\mathbb {R} ^{n}$ and the dual measure needed for the Fourier inversion formula is ${\widehat {\mu }}=(2\pi )^{-n}\mu$ . If we want to get a Fourier inversion formula with the same measure on both sides (that is, since we can think about $\mathbb {R} ^{n}$ as its own dual space we can ask for ${\widehat {\mu }}$ to equal $\mu$ ) then we need to use ${\begin{aligned}\mu &=(2\pi )^{-{\frac {n}{2}}}\times {\text{Lebesgue measure}}\\{\widehat {\mu }}&=(2\pi )^{-{\frac {n}{2}}}\times {\text{Lebesgue measure}}\end{aligned}}$

However, if we change the way we identify $\mathbb {R} ^{n}$ with its dual group, by using the pairing $(\mathbf {v} ,\mathbf {w} )\mapsto e^{2\pi i\mathbf {v} \cdot \mathbf {w} },$ then Lebesgue measure on $\mathbb {R} ^{n}$ is equal to its own dual measure. This convention minimizes the number of factors of $2\pi$ that show up in various places when computing Fourier transforms or inverse Fourier transforms on Euclidean space. (In effect it limits the $2\pi$ only to the exponent rather than as a pre-factor outside the integral sign.) Note that the choice of how to identify $\mathbb {R} ^{n}$ with its dual group affects the meaning of the term "self-dual function", which is a function on $\mathbb {R} ^{n}$ equal to its own Fourier transform: using the classical pairing $(\mathbf {v} ,\mathbf {w} )\mapsto e^{i\mathbf {v} \cdot \mathbf {w} }$ the function $e^{-{\frac {1}{2}}x^{2}}$ is self-dual. But using the pairing, which keeps the pre-factor as unity, $(\mathbf {v} ,\mathbf {w} )\mapsto e^{2\pi i\mathbf {v} \cdot \mathbf {w} }$ makes $e^{-\pi x^{2}}$ self-dual instead. This second definition for the Fourier transform has the advantage that it maps the multiplicative identity to the convolution identity, which is useful as $L^{1}$ is a convolution algebra. See the next section on the group algebra. In addition, this form is also necessarily isometric on $L^{2}$ spaces. See below at Plancherel and *L*2 Fourier inversion theorems.

### Group algebra

The space of integrable functions on a locally compact abelian group G is an algebra, where multiplication is convolution: the convolution of two integrable functions f and g is defined as $(f*g)(x)=\int _{G}f(x-y)g(y)\ d\mu (y).$

**Theorem**—The Banach space $L^{1}(G)$ is an associative and commutative algebra under convolution.

This algebra is referred to as the *Group Algebra* of G . By the Fubini–Tonelli theorem, the convolution is submultiplicative with respect to the $L^{1}$ norm, making $L^{1}(G)$ a Banach algebra. The Banach algebra $L^{1}(G)$ has a multiplicative identity element if and only if G is a discrete group, namely the function that is 1 at the identity and zero elsewhere. In general, however, it has an approximate identity which is a net (or generalized sequence) $\{e_{i}\}_{i\in I}$ indexed on a directed set I such that $f*e_{i}\to f.$

The Fourier transform takes convolution to multiplication, i.e. it is a homomorphism of abelian Banach algebras $L^{1}(G)\to C_{0}\left({\widehat {G}}\right)$ (of norm ≤ 1): ${\mathcal {F}}(f*g)(\chi )={\mathcal {F}}(f)(\chi )\cdot {\mathcal {F}}(g)(\chi ).$

In particular, to every group character on G corresponds a unique *multiplicative linear functional* on the group algebra defined by $f\mapsto {\widehat {f}}(\chi ).$

It is an important property of the group algebra that these exhaust the set of non-trivial (that is, not identically zero) multiplicative linear functionals on the group algebra; see section 34 of Loomis (1953). This means the Fourier transform is a special case of the Gelfand transform.

### Plancherel and *L*2 Fourier inversion theorems

As we have stated, the dual group of a locally compact abelian group is a locally compact abelian group in its own right and thus has a Haar measure, or more precisely a whole family of scale-related Haar measures.

**Theorem**—Choose a Haar measure $\mu$ on G and let $\nu$ be the dual measure on ${\widehat {G}}$ as defined above. If $f:G\to \mathbb {C}$ is continuous with compact support then ${\widehat {f}}\in L^{2}\left({\widehat {G}}\right)$ and $\int _{G}|f(x)|^{2}\ d\mu (x)=\int _{\widehat {G}}\left|{\widehat {f}}(\chi )\right|^{2}\ d\nu (\chi ).$ In particular, the Fourier transform is an $L^{2}$ isometry from the complex-valued continuous functions of compact support on G to the $L^{2}$ -functions on ${\widehat {G}}$ (using the $L^{2}$ -norm with respect to $\mu$ for functions on G and the $L^{2}$ -norm with respect to $\nu$ for functions on ${\widehat {G}}$ ).

Since the complex-valued continuous functions of compact support on G are $L^{2}$ -dense, there is a unique extension of the Fourier transform from that space to a unitary operator ${\mathcal {F}}:L_{\mu }^{2}(G)\to L_{\nu }^{2}\left({\widehat {G}}\right).$ and we have the formula $\forall f\in L^{2}(G):\quad \int _{G}|f(x)|^{2}\ d\mu (x)=\int _{\widehat {G}}\left|{\widehat {f}}(\chi )\right|^{2}\ d\nu (\chi ).$

Note that for non-compact locally compact groups G the space $L^{1}(G)$ does not contain $L^{2}(G)$ , so the Fourier transform of general $L^{2}$ -functions on G is "not" given by any kind of integration formula (or really any explicit formula). To define the $L^{2}$ Fourier transform one has to resort to some technical trick such as starting on a dense subspace like the continuous functions with compact support and then extending the isometry by continuity to the whole space. This unitary extension of the Fourier transform is what we mean by the Fourier transform on the space of square integrable functions.

The dual group also has an inverse Fourier transform in its own right; it can be characterized as the inverse (or adjoint, since it is unitary) of the $L^{2}$ Fourier transform. This is the content of the $L^{2}$ Fourier inversion formula which follows.

**Theorem**—The adjoint of the Fourier transform restricted to continuous functions of compact support is the inverse Fourier transform $L_{\nu }^{2}\left({\widehat {G}}\right)\to L_{\mu }^{2}(G)$ where $\nu$ is the dual measure to $\mu$ .

In the case $G=\mathbb {T}$ the dual group ${\widehat {G}}$ is naturally isomorphic to the group of integers $\mathbb {Z}$ and the Fourier transform specializes to the computation of coefficients of Fourier series of periodic functions.

If G is a finite group, we recover the discrete Fourier transform. Note that this case is very easy to prove directly.

## Bohr compactification and almost-periodicity

One important application of Pontryagin duality is the following characterization of compact abelian topological groups:

**Theorem**—A locally compact *abelian* group G is compact if and only if the dual group ${\widehat {G}}$ is discrete. Conversely, G is discrete if and only if ${\widehat {G}}$ is compact.

That G being compact implies ${\widehat {G}}$ is discrete or that G being discrete implies that ${\widehat {G}}$ is compact is an elementary consequence of the definition of the compact-open topology on ${\widehat {G}}$ and does not need Pontryagin duality. One uses Pontryagin duality to prove the converses.

The Bohr compactification is defined for any topological group G , regardless of whether G is locally compact or abelian. One use made of Pontryagin duality between compact abelian groups and discrete abelian groups is to characterize the Bohr compactification of an arbitrary abelian *locally compact* topological group. The *Bohr compactification* $B(G)$ of G is ${\widehat {H}}$ , where *H* has the group structure ${\widehat {G}}$ , but given the discrete topology. Since the inclusion map $\iota :H\to {\widehat {G}}$ is continuous and a homomorphism, the dual morphism $G\sim {\widehat {\widehat {G}}}\to {\widehat {H}}$ is a morphism into a compact group which is easily shown to satisfy the requisite universal property.

## Categorical considerations

Pontryagin duality can also profitably be considered functorially. In what follows, **LCA** is the category of locally compact abelian groups and continuous group homomorphisms. The dual group construction of ${\widehat {G}}$ is a contravariant functor **LCA** → **LCA**, represented (in the sense of representable functors) by the circle group $\mathbb {T}$ as ${\widehat {G}}={\text{Hom}}(G,\mathbb {T} ).$ In particular, the double dual functor $G\to {\widehat {\widehat {G}}}$ is *covariant*. A categorical formulation of Pontryagin duality then states that the natural transformation between the identity functor on **LCA** and the double dual functor is an isomorphism. Unwinding the notion of a natural transformation, this means that the maps $G\to \operatorname {Hom} (\operatorname {Hom} (G,T),T)$ are isomorphisms for any locally compact abelian group G , and these isomorphisms are functorial in G . This isomorphism is analogous to the double dual of finite-dimensional vector spaces (a special case, for real and complex vector spaces).

An immediate consequence of this formulation is another common categorical formulation of Pontryagin duality: the dual group functor is an equivalence of categories from **LCA** to **LCA**op.

The duality interchanges the subcategories of discrete groups and compact groups. If R is a ring and G is a left R –module, the dual group ${\widehat {G}}$ will become a right R –module; in this way we can also see that discrete left R –modules will be Pontryagin dual to compact right R –modules. The ring ${\text{End}}(G)$ of endomorphisms in **LCA** is changed by duality into its opposite ring (change the multiplication to the other order). For example, if G is an infinite cyclic discrete group, ${\widehat {G}}$ is a circle group: the former has ${\text{End}}(G)=\mathbb {Z}$ so this is true also of the latter.

## Generalizations

Generalizations of Pontryagin duality are constructed in two main directions: for commutative topological groups that are not locally compact, and for noncommutative topological groups. The theories in these two cases are very different.

### Dualities for commutative topological groups

When G is a Hausdorff abelian topological group, the group ${\widehat {G}}$ with the compact-open topology is a Hausdorff abelian topological group and the natural mapping from G to its double-dual ${\widehat {\widehat {G}}}$ makes sense. If this mapping is an isomorphism, it is said that G satisfies Pontryagin duality (or that G is a *reflexive group*, or a *reflective group*). This has been extended in a number of directions beyond the case that G is locally compact.

In particular, Samuel Kaplan showed in 1948 and 1950 that arbitrary products and countable inverse limits of locally compact (Hausdorff) abelian groups satisfy Pontryagin duality. Note that an infinite product of locally compact non-compact spaces is not locally compact.

Later, in 1975, Rangachari Venkataraman showed, among other facts, that every open subgroup of an abelian topological group which satisfies Pontryagin duality itself satisfies Pontryagin duality.

More recently, Sergio Ardanza-Trevijano and María Jesús Chasco have extended the results of Kaplan mentioned above. They showed that direct and inverse limits of sequences of abelian groups satisfying Pontryagin duality also satisfy Pontryagin duality if the groups are metrizable or $k_{\omega }$ -spaces but not necessarily locally compact, provided some extra conditions are satisfied by the sequences.

However, there is a fundamental aspect that changes if we want to consider Pontryagin duality beyond the locally compact case. Elena Martín-Peinador proved in 1995 that if G is a Hausdorff abelian topological group that satisfies Pontryagin duality, and the natural evaluation pairing ${\begin{cases}G\times {\widehat {G}}\to \mathbb {T} \\(x,\chi )\mapsto \chi (x)\end{cases}}$ is (jointly) continuous, then G is locally compact. As a corollary, all non-locally compact examples of Pontryagin duality are groups where the pairing $G\times {\widehat {G}}\to \mathbb {T}$ is not (jointly) continuous.

Another way to generalize Pontryagin duality to wider classes of commutative topological groups is to endow the dual group ${\widehat {G}}$ with a bit different topology, namely the *topology of uniform convergence on totally bounded sets*. The groups satisfying the identity $G\cong {\widehat {\widehat {G}}}$ under this assumption are called *stereotype groups*. This class is also very wide (and it contains locally compact abelian groups), but it is narrower than the class of reflective groups.

### Pontryagin duality for topological vector spaces

In 1952 Marianne F. Smith noticed that Banach spaces and reflexive spaces, being considered as topological groups (with the additive group operation), satisfy Pontryagin duality. Later B. S. Brudovskiĭ, William C. Waterhouse and K. Brauner showed that this result can be extended to the class of all quasi-complete barreled spaces (in particular, to all Fréchet spaces). In the 1990s Sergei Akbarov gave a description of the class of the topological vector spaces that satisfy a stronger property than the classical Pontryagin reflexivity, namely, the identity $(X^{\star })^{\star }\cong X$ where $X^{\star }$ means the space of all linear continuous functionals $f\colon X\to \mathbb {C}$ endowed with the *topology of uniform convergence on totally bounded sets* in X (and $(X^{\star })^{\star }$ means the dual to $X^{\star }$ in the same sense). The spaces of this class are called stereotype spaces, and the corresponding theory found a series of applications in Functional analysis and Geometry, including the generalization of Pontryagin duality for non-commutative topological groups.

### Dualities for non-commutative topological groups

For non-commutative locally compact groups G the classical Pontryagin construction stops working for various reasons, in particular, because the characters don't always separate the points of G , and the irreducible representations of G are not always one-dimensional. At the same time it is not clear how to introduce multiplication on the set of irreducible unitary representations of G , and it is even not clear whether this set is a good choice for the role of the dual object for G . So the problem of constructing duality in this situation requires complete rethinking.

Theories built to date are divided into two main groups: the theories where the dual object has the same nature as the source one (like in the Pontryagin duality itself), and the theories where the source object and its dual differ from each other so radically that it is impossible to count them as objects of one class.

The second type theories were historically the first: soon after Pontryagin's work Tadao Tannaka (1938) and Mark Krein (1949) constructed a duality theory for arbitrary compact groups known now as the Tannaka–Krein duality. In this theory the dual object for a group G is not a group but a category of its representations $\Pi (G)$ .

The theories of first type appeared later and the key example for them was the duality theory for finite groups. In this theory the category of finite groups is embedded by the operation $G\mapsto \mathbb {C} _{G}$ of taking group algebra $\mathbb {C} _{G}$ (over $\mathbb {C}$ ) into the category of finite dimensional Hopf algebras, so that the Pontryagin duality functor $G\mapsto {\widehat {G}}$ turns into the operation $H\mapsto H^{*}$ of taking the dual vector space (which is a duality functor in the category of finite dimensional Hopf algebras).

In 1973 Leonid I. Vainerman, George I. Kac, Michel Enock, and Jean-Marie Schwartz built a general theory of this type for all locally compact groups. From the 1980s the research in this area was resumed after the discovery of quantum groups, to which the constructed theories began to be actively transferred. These theories are formulated in the language of C*-algebras, or Von Neumann algebras, and one of its variants is the recent theory of locally compact quantum groups.

One of the drawbacks of these general theories, however, is that in them the objects generalizing the concept of a group are not Hopf algebras in the usual algebraic sense. This deficiency can be corrected (for some classes of groups) within the framework of duality theories constructed on the basis of the notion of envelope of topological algebra.
