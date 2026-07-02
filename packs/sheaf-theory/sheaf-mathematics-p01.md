---
title: "Sheaf (mathematics) (part 1/2)"
source: https://en.wikipedia.org/wiki/Sheaf_(mathematics)
domain: sheaf-theory
license: CC-BY-SA-4.0
tags: sheaf theory, sheaf cohomology, grothendieck topology, ringed space
fetched: 2026-07-02
part: 1/2
---

# Sheaf (mathematics)

In mathematics, a **sheaf** (pl.: **sheaves**) is a tool for systematically tracking data (such as sets, abelian groups, rings) attached to the open sets of a topological space and defined locally with regard to them. For example, for each open set, the data could be the ring of continuous functions defined on that open set. Such data are well-behaved in that they can be restricted to smaller open sets, and also the data assigned to an open set are equivalent to all collections of compatible data assigned to collections of smaller open sets covering the original open set (intuitively, every datum is the sum of its constituent data).

The field of mathematics that studies sheaves is called **sheaf theory**.

Sheaves are understood conceptually as general and abstract objects. Their precise definition is rather technical. They are specifically defined as **sheaves of sets** or as **sheaves of rings**, for example, depending on the type of data assigned to the open sets.

There are also maps (or morphisms) from one sheaf to another; sheaves (of a specific type, such as sheaves of abelian groups) with their morphisms on a fixed topological space form a category. On the other hand, to each continuous map there is associated both a direct image functor, taking sheaves and their morphisms on the domain to sheaves and morphisms on the codomain, and an inverse image functor operating in the opposite direction. These functors, and certain variants of them, are essential parts of sheaf theory.

Due to their general nature and versatility, sheaves have several applications in topology and especially in algebraic and differential geometry. First, geometric structures such as that of a differentiable manifold or a scheme can be expressed in terms of a sheaf of rings on the space. In such contexts, several geometric constructions such as vector bundles or divisors are naturally specified in terms of sheaves. Second, sheaves provide the framework for a very general cohomology theory, which encompasses also the "usual" topological cohomology theories such as singular cohomology. Especially in algebraic geometry and the theory of complex manifolds, sheaf cohomology provides a powerful link between topological and geometric properties of spaces. Sheaves also provide the basis for the theory of *D*-modules, which provide applications to the theory of differential equations. In addition, generalisations of sheaves to more general settings than topological spaces, such as the notion of a sheaf on a category with respect to some Grothendieck topology, have provided applications to mathematical logic and to number theory.


## Definitions and examples

In many mathematical branches, several structures defined on a topological space X (e.g., a differentiable manifold) can be naturally *localised* or *restricted* to open subsets $U\subseteq X$ : typical examples include continuous real-valued or complex-valued functions, n -times differentiable (real-valued or complex-valued) functions, bounded real-valued functions, vector fields, and sections of any vector bundle on the space. The ability to restrict data to smaller open subsets gives rise to the concept of presheaves. Roughly speaking, sheaves are then those presheaves, where local data can be glued to global data.

### Presheaves

Let X be a topological space. A *presheaf ${\mathcal {F}}$ of sets* on X consists of the following data:

- For each open set $U\subseteq X$ , there exists a set ${\mathcal {F}}(U)$ . This set is also denoted $\Gamma (U,{\mathcal {F}})$ . The elements in this set are called the *sections* of ${\mathcal {F}}$ over U . The sections of ${\mathcal {F}}$ over X are called the *global sections* of ${\mathcal {F}}$ .
- For each inclusion of open sets $V\subseteq U$ , a function $\operatorname {res} _{V}^{U}\colon {\mathcal {F}}(U)\rightarrow {\mathcal {F}}(V)$ . In view of many of the examples below, the morphisms ${\text{res}}_{V}^{U}$ are called *restriction morphisms*. If $s\in {\mathcal {F}}(U)$ , then its restriction ${\text{res}}_{V}^{U}(s)$ is often denoted $s|_{V}$ by analogy with restriction of functions.

The restriction morphisms are required to satisfy two additional (functorial) properties:

- For every open set U of X , the restriction morphism $\operatorname {res} _{U}^{U}\colon {\mathcal {F}}(U)\rightarrow {\mathcal {F}}(U)$ is the identity morphism on ${\mathcal {F}}(U)$ .
- If we have three open sets $W\subseteq V\subseteq U$ , then the composite ${\text{res}}_{W}^{V}\circ {\text{res}}_{V}^{U}={\text{res}}_{W}^{U}$ .

Informally, the second axiom says it does not matter whether we restrict to W in one step or restrict first to V , then to W . A concise functorial reformulation of this definition is given further below.

Many examples of presheaves come from different classes of functions: to any U , one can assign the set $C^{0}(U)$ of continuous real-valued functions on U . The restriction maps are then just given by restricting a continuous function on U to a smaller open subset $V\subseteq U$ , which again is a continuous function. The two presheaf axioms are immediately checked, thereby giving an example of a presheaf. This can be extended to a presheaf of holomorphic functions ${\mathcal {H}}(-)$ and a presheaf of smooth functions $C^{\infty }(-)$ .

Another common class of examples is assigning to U the set of constant real-valued functions on U . This presheaf is called the *constant presheaf* associated to $\mathbb {R}$ and is denoted ${\underline {\mathbb {R} }}^{\text{psh}}$ .

### Sheaves

Given a presheaf, a natural question to ask is to what extent its sections over an open set U are specified by their restrictions to open subsets of U . A *sheaf* is a presheaf whose sections are, in a technical sense, uniquely determined by their restrictions.

Axiomatically, a *sheaf* is a presheaf that satisfies both of the following axioms:

1. (*Locality*) Suppose U is an open set, $\{U_{i}\}_{i\in I}$ is an open cover of U with $U_{i}\subseteq U$ for all $i\in I$ , and $s,t\in {\mathcal {F}}(U)$ are sections. If $s|_{U_{i}}=t|_{U_{i}}$ for all $i\in I$ , then $s=t$ .
2. (*Gluing*) Suppose U is an open set, $\{U_{i}\}_{i\in I}$ is an open cover of U with $U_{i}\subseteq U$ for all $i\in I$ , and $\{s_{i}\in {\mathcal {F}}(U_{i})\}_{i\in I}$ is a family of sections. If all pairs of sections agree on the overlap of their domains, that is, if $s_{i}|_{U_{i}\cap U_{j}}=s_{j}|_{U_{i}\cap U_{j}}$ for all $i,j\in I$ , then there exists a section $s\in {\mathcal {F}}(U)$ such that $s|_{U_{i}}=s_{i}$ for all $i\in I$ .

- (Two lifted copies of the base opens intersecting the stalks to pick one germ over each point.) Sections over two opens of the two-point space.
- (Lifted copy of the union open restricting to the two chosen local sections on each open.) Gluing compatible local sections to a section over the union.

In both of these axioms, the hypothesis on the open cover is equivalent to the assumption that ${\textstyle \bigcup _{i\in I}U_{i}=U}$ .

The section s whose existence is guaranteed by axiom 2 is called the *gluing*, *concatenation*, or *collation* of the sections $s_{i}$ . By axiom 1 it is unique. Sections $s_{i}$ and $s_{j}$ satisfying the agreement precondition of axiom 2 are often called *compatible* ; thus axioms 1 and 2 together state that *any collection of pairwise compatible sections can be uniquely glued together*. A *separated presheaf*, or *monopresheaf*, is a presheaf satisfying axiom 1.

The presheaf consisting of continuous functions mentioned above is a sheaf. This assertion reduces to checking that, given continuous functions $f_{i}:U_{i}\to \mathbb {R}$ which agree on the intersections $U_{i}\cap U_{j}$ , there is a unique continuous function $f:U\to \mathbb {R}$ whose restriction equals the $f_{i}$ . By contrast, the constant presheaf is usually *not* a sheaf as it fails to satisfy the locality axiom on the empty set (this is explained in more detail at constant sheaf).

Presheaves and sheaves are typically denoted by capital letters, F being particularly common, presumably for the French word for sheaf, *faisceau*. Use of calligraphic letters such as ${\mathcal {F}}$ is also common.

It can be shown that to specify a sheaf, it is enough to specify its restriction to the open sets of a basis for the topology of the underlying space. Moreover, it can also be shown that it is enough to verify the sheaf axioms above relative to the open sets of a covering. This observation is used to construct another example which is crucial in algebraic geometry, namely quasi-coherent sheaves. Here the topological space in question is the spectrum of a commutative ring R , whose points are the prime ideals ${\mathfrak {p}}$ in R . The open sets $D_{f}:=\{{\mathfrak {p}}\subseteq R,f\notin {\mathfrak {p}}\}$ form a basis for the Zariski topology on this space. Given an R -module M , there is a sheaf, denoted by ${\tilde {M}}$ on the $\operatorname {Spec} R$ , that satisfies ${\tilde {M}}(D_{f}):=M[1/f],$ where $M[1/f]$ is the localization of M at f .

There is another characterization of sheaves that is equivalent to the previously discussed. A presheaf ${\mathcal {F}}$ is a sheaf if and only if for any open U and any open cover $\{U_{a}\}$ of U , ${\mathcal {F}}(U)$ is the fibre product ${\mathcal {F}}(U)\cong {\mathcal {F}}(U_{a})\times _{{\mathcal {F}}(U_{a}\cap U_{b})}{\mathcal {F}}(U_{b})$ . This characterization is useful in construction of sheaves, for example, if ${\mathcal {F}},{\mathcal {G}}$ are abelian sheaves, then the kernel of sheaves morphism ${\mathcal {F}}\to {\mathcal {G}}$ is a sheaf, since projective limits commute with projective limits. On the other hand, the cokernel is not always a sheaf because inductive limits do not necessarily commute with projective limits. One way to fix this is to consider Noetherian topological spaces; all open sets are compact so that the cokernel is a sheaf, since finite projective limits commute with inductive limits.

### Further examples

#### Sheaf of sections of a continuous map

Any continuous map $f:Y\to X$ of topological spaces determines a sheaf $\Gamma (Y/X)$ on X by setting

$\Gamma (Y/X)(U)=\{s:U\to Y,f\circ s=\operatorname {id} _{U}\}.$

Any such s is commonly called a section of f , and this example is the reason why the elements in ${\mathcal {F}}(U)$ are generally called sections. This construction is especially important when f is the projection of a fiber bundle onto its base space. For example, the sheaves of smooth functions are the sheaves of sections of the trivial bundle.

Another example: the sheaf of sections of

$\mathbb {C} {\stackrel {\exp }{\longrightarrow }}\mathbb {C} \setminus \{0\}$

is the sheaf which assigns to any $U\subseteq \mathbb {C} \setminus \{0\}$ the set of branches of the complex logarithm on U .

Given a point x and an abelian group S , the skyscraper sheaf $S_{x}$ is defined as follows: if U is an open set containing x , then $S_{x}(U)=S$ . If U does not contain x , then $S_{x}(U)=0$ , the trivial group. The restriction maps are either the identity on S , if both open sets contain x , or the zero map otherwise.

#### Sheaves on manifolds

On an n -dimensional $C^{k}$ -manifold M , there are a number of important sheaves, such as the sheaf of j -times continuously differentiable functions ${\mathcal {O}}_{M}^{j}$ (with $j\leq k$ ). Its sections on some open U are the $C^{j}$ -functions $U\to \mathbb {R}$ . For $j=k$ , this sheaf is called the *structure sheaf* and is denoted ${\mathcal {O}}_{M}$ . The nonzero $C^{k}$ functions also form a sheaf, denoted ${\mathcal {O}}_{X}^{\times }$ . Differential forms (of degree p ) also form a sheaf $\Omega _{M}^{p}$ . In all these examples, the restriction morphisms are given by restricting functions or forms.

The assignment sending U to the compactly supported functions on U is not a sheaf, since there is, in general, no way to preserve this property by passing to a smaller open subset. Instead, this forms a cosheaf, a dual concept where the restriction maps go in the opposite direction than with sheaves. However, taking the dual of these vector spaces does give a sheaf, the sheaf of distributions.

#### Presheaves that are not sheaves

In addition to the constant presheaf mentioned above, which is usually not a sheaf, there are further examples of presheaves that are not sheaves:

- Let X be the two-point topological space $\{x,y\}$ with the discrete topology. Define a presheaf F as follows: $F(\varnothing )=\{\varnothing \},\ F(\{x\})=\mathbb {R} ,\ F(\{y\})=\mathbb {R} ,\ F(\{x,y\})=\mathbb {R} \times \mathbb {R} \times \mathbb {R}$ The restriction map $F(\{x,y\})\to F(\{x\})$ is the projection of $\mathbb {R} \times \mathbb {R} \times \mathbb {R}$ onto its first coordinate, and the restriction map $F(\{x,y\})\to F(\{y\})$ is the projection of $\mathbb {R} \times \mathbb {R} \times \mathbb {R}$ onto its second coordinate. F is a presheaf that is not separated: a global section is determined by three numbers, but the values of that section over $\{x\}$ and $\{y\}$ determine only two of those numbers. So while we can glue any two sections over $\{x\}$ and $\{y\}$ , we cannot glue them uniquely.
- Let $X=\mathbb {R}$ be the real line, and let $F(U)$ be the set of bounded continuous functions on U . This is not a sheaf because it is not always possible to glue. For example, let $U_{i}$ be the set of all x such that $|x|<i$ . The identity function $f(x)=x$ is bounded on each $U_{i}$ . Consequently, we get a section $s_{i}$ on $U_{i}$ . However, these sections do not glue, because the function f is not bounded on the real line. Consequently F is a presheaf, but not a sheaf. In fact, F is separated because it is a sub-presheaf of the sheaf of continuous functions.

### Motivating sheaves from complex analytic spaces and algebraic geometry

One of the historical motivations for sheaves have come from studying complex manifolds, complex analytic geometry, and scheme theory from algebraic geometry. This is because in all of the previous cases, we consider a topological space X together with a structure sheaf ${\mathcal {O}}$ giving it the structure of a complex manifold, complex analytic space, or scheme. This perspective of equipping a topological space with a sheaf is essential to the theory of locally ringed spaces (see below).

#### Technical challenges with complex manifolds

One of the main historical motivations for introducing sheaves was constructing a device which keeps track of holomorphic functions on complex manifolds. For example, on a compact complex manifold X (like complex projective space or the vanishing locus in projective space of a homogeneous polynomial), the *only* holomorphic functions

$f:X\to \mathbb {C}$

are the constant functions. This means there exist two compact complex manifolds $X,X'$ which are not isomorphic, but nevertheless their rings of global holomorphic functions, denoted ${\mathcal {H}}(X),{\mathcal {H}}(X')$ , are isomorphic. Contrast this with smooth manifolds where every manifold M can be embedded inside some $\mathbb {R} ^{n}$ , hence its ring of smooth functions $C^{\infty }(M)$ comes from restricting the smooth functions from $C^{\infty }(\mathbb {R} ^{n})$ , of which there exist plenty.

Another complexity when considering the ring of holomorphic functions on a complex manifold X is given a small enough open set $U\subseteq X$ , the holomorphic functions will be isomorphic to ${\mathcal {H}}(U)\cong {\mathcal {H}}(\mathbb {C} ^{n})$ . Sheaves are a direct tool for dealing with this complexity since they make it possible to keep track of the holomorphic structure on the underlying topological space of X on arbitrary open subsets $U\subseteq X$ . This means as U becomes more complex topologically, the ring ${\mathcal {H}}(U)$ can be expressed from gluing the ${\mathcal {H}}(U_{i})$ . Note that sometimes this sheaf is denoted ${\mathcal {O}}(-)$ or just ${\mathcal {O}}$ , or even ${\mathcal {O}}_{X}$ when we want to emphasize the space the structure sheaf is associated to.

#### Tracking submanifolds with sheaves

Another common example of sheaves can be constructed by considering a complex submanifold $Y\hookrightarrow X$ . There is an associated sheaf ${\mathcal {O}}_{Y}$ which takes an open subset $U\subseteq X$ and gives the ring of holomorphic functions on $U\cap Y$ . This kind of formalism was found to be extremely powerful and motivates a lot of homological algebra such as sheaf cohomology since an intersection theory can be built using these kinds of sheaves from the Serre intersection formula.


## Operations with sheaves

### Morphisms

Morphisms of sheaves are, roughly speaking, analogous to functions between them. In contrast to a function between sets, which is simply an assignment of outputs to inputs, morphisms of sheaves are also required to be compatible with the local–global structures of the underlying sheaves. This idea is made precise in the following definition.

Let ${\mathcal {F}}$ and ${\mathcal {G}}$ be two sheaves of sets (respectively abelian groups, rings, etc.) on X . A *morphism* $\varphi :{\mathcal {F}}\to {\mathcal {G}}$ consists of a morphism $\varphi _{U}:{\mathcal {F}}(U)\to {\mathcal {G}}(U)$ of sets (respectively abelian groups, rings, etc.) for each open set U of X , subject to the condition that this morphism is compatible with restrictions. In other words, for every open subset V of an open set U , the following diagram is commutative.

${\begin{array}{rcl}{\mathcal {F}}(U)&\xrightarrow {\quad \varphi _{U}\quad } &{\mathcal {G}}(U)\\r_{V}^{U}{\Biggl \downarrow }&&{\Biggl \downarrow }{r'}_{V}^{U}\\{\mathcal {F}}(V)&{\xrightarrow[{\quad \varphi _{V}\quad }]{}}&{\mathcal {G}}(V)\end{array}}$

For example, taking the derivative gives a morphism of sheaves on $\mathbb {R}$ ,

${\frac {\mathrm {d} }{\mathrm {d} x}}\colon {\mathcal {O}}_{\mathbb {R} }^{n}\to {\mathcal {O}}_{\mathbb {R} }^{n-1}.$

Indeed, given an ( n -times continuously differentiable) function $f:U\to \mathbb {R}$ (with U in $\mathbb {R}$ open), the restriction (to a smaller open subset V ) of its derivative equals the derivative of $f|_{V}$ .

With this notion of morphism, sheaves of sets (respectively abelian groups, rings, etc.) on a fixed topological space X form a category. The general categorical notions of mono-, epi- and isomorphisms can therefore be applied to sheaves.

In fact, from the point of view of category theory, the category of sheaves over a (small) category C with values in another category D is a full subcategory of the category of presheaves over C with values in D , which is simply the category $D^{C^{\text{op}}}$ of contravariant functors from C to D with natural transformations between them as morphisms: the notion of morphism defined above can simply be stated as $\varphi$ being a natural transformation between the two sheaves seen as functors.

A morphism $\varphi \colon {\mathcal {F}}\rightarrow {\mathcal {G}}$ of sheaves on X is an isomorphism (respectively monomorphism) if and only if for every open set $U\subseteq X$ , we have an isomorphism ${\mathcal {F}}(U)\approx {\mathcal {G}}(U)$ which is natural with respect to the restriction maps. These statements give examples of how to work with sheaves using local information, but it's important to note that we cannot check if a morphism of sheaves is an epimorphism in the same manner. Indeed the statement that maps on the level of open sets $\varphi _{U}\colon {\mathcal {F}}(U)\rightarrow {\mathcal {G}}(U)$ are not always surjective for epimorphisms of sheaves is equivalent to non-exactness of the global sections functor—or equivalently, to non-triviality of sheaf cohomology.

### Stalks of a sheaf

The *stalk* ${\mathcal {F}}_{x}$ of a sheaf ${\mathcal {F}}$ captures the properties of a sheaf "around" a point $x\in X$ , generalizing the germs of functions. Here, "around" means that, conceptually speaking, one looks at smaller and smaller neighborhoods of the point. Of course, no single neighborhood will be small enough, which requires considering a limit of some sort. More precisely, the stalk is defined by

${\mathcal {F}}_{x}=\varinjlim _{U\ni x}{\mathcal {F}}(U),$

the direct limit being over all open subsets of X containing the given point x . In other words, an element of the stalk is given by a section over some open neighborhood of x , and two such sections are considered equivalent if their restrictions agree on a smaller neighborhood.

The natural morphism ${\mathcal {F}}(U)\to {\mathcal {F}}_{x}$ takes a section s in ${\mathcal {F}}(U)$ to its *germ* $s_{x}$ at x . This generalises the usual definition of a germ.

In many situations, knowing the stalks of a sheaf is enough to control the sheaf itself. For example, whether or not a morphism of sheaves is a monomorphism, epimorphism, or isomorphism can be tested on the stalks. In this sense, a sheaf is determined by its stalks, which are a local data. By contrast, the *global* information present in a sheaf, i.e., the *global sections*, i.e., the sections ${\mathcal {F}}(X)$ on the whole space X , typically carry less information. For example, for a compact complex manifold X , the global sections of the sheaf of holomorphic functions are just $\mathbb {C}$ , since any holomorphic function $X\to \mathbb {C}$ is constant by Liouville's theorem.

### Turning a presheaf into a sheaf

It is frequently useful to take the data contained in a presheaf and to express it as a sheaf. It turns out that there is a best possible way to do this. It takes a presheaf ${\mathcal {F}}$ and produces a new sheaf $a{\mathcal {F}}$ called the *sheafification* or *sheaf associated to the presheaf* ${\mathcal {F}}$ . For example, the sheafification of the constant presheaf (see above) is called the *constant sheaf*. Despite its name, its sections are *locally* constant functions.

The sheaf $a{\mathcal {F}}$ can be constructed using the étalé space E of ${\mathcal {F}}$ , namely as the sheaf of sections of the map

$E\to X.$

Another construction of the sheaf $a{\mathcal {F}}$ proceeds by means of a functor L from presheaves to presheaves that gradually improves the properties of a presheaf: for any presheaf ${\mathcal {F}}$ , $L{\mathcal {F}}$ is a separated presheaf, and for any separated presheaf ${\mathcal {F}}$ , $L{\mathcal {F}}$ is a sheaf. The associated sheaf $a{\mathcal {F}}$ is given by $LL{\mathcal {F}}$ .

The idea that the sheaf $a{\mathcal {F}}$ is the best possible approximation to ${\mathcal {F}}$ by a sheaf is made precise using the following universal property: there is a natural morphism of presheaves $i\colon {\mathcal {F}}\to a{\mathcal {F}}$ so that for any sheaf ${\mathcal {G}}$ and any morphism of presheaves $f\colon {\mathcal {F}}\to {\mathcal {G}}$ , there is a unique morphism of sheaves ${\tilde {f}}\colon a{\mathcal {F}}\rightarrow {\mathcal {G}}$ such that $f={\tilde {f}}i$ . In fact, a is the left adjoint functor to the inclusion functor (or forgetful functor) from the category of sheaves to the category of presheaves, and i is the unit of the adjunction. In this way, the category of sheaves turns into a Giraud subcategory of presheaves. This categorical situation is the reason why the sheafification functor appears in constructing cokernels of sheaf morphisms or tensor products of sheaves, but not for kernels, say.

### Subsheaves, quotient sheaves

If K is a subsheaf of a sheaf F of abelian groups, then the **quotient sheaf** Q is the sheaf associated to the presheaf $U\mapsto F(U)/K(U)$ ; in other words, the quotient sheaf fits into an exact sequence of sheaves of abelian groups;

$0\to K\to F\to Q\to 0.$

(this is also called a sheaf extension.)

Let $F,G$ be sheaves of abelian groups. The set $\operatorname {Hom} (F,G)$ of morphisms of sheaves from F to G forms an abelian group (by the abelian group structure of G ). The **sheaf hom** of F and G , denoted by,

${\mathcal {Hom}}(F,G)$

is the sheaf of abelian groups $U\mapsto \operatorname {Hom} (F|_{U},G|_{U})$ where $F|_{U}$ is the sheaf on U given by $(F|_{U})(V)=F(V)$ (note sheafification is not needed here). The direct sum of F and G is the sheaf given by $U\mapsto F(U)\oplus G(U)$ , and the tensor product of F and G is the sheaf associated to the presheaf $U\mapsto F(U)\otimes G(U)$ .

All of these operations extend to sheaves of modules over a sheaf of rings A ; the above is the special case when A is the constant sheaf ${\underline {\mathbf {Z} }}$ .

### Basic functoriality

Since the data of a (pre-)sheaf depends on the open subsets of the base space, sheaves on different topological spaces are unrelated to each other in the sense that there are no morphisms between them. However, given a continuous map $f:X\to Y$ between two topological spaces, pushforward and pullback relate sheaves on X to those on Y and vice versa.

#### Direct image

The pushforward (also known as direct image) of a sheaf ${\mathcal {F}}$ on X is the sheaf defined by

$(f_{*}{\mathcal {F}})(V)={\mathcal {F}}(f^{-1}(V)).$

Here V is an open subset of Y , so that its preimage is open in X by the continuity of f . This construction recovers the skyscraper sheaf $S_{x}$ mentioned above:

$S_{x}=i_{*}(S)$

where $i:\{x\}\to X$ is the inclusion, and S is regarded as a sheaf on the singleton by $S(\{*\})=S,S(\emptyset )=\emptyset$ .

For a map between locally compact spaces, the direct image with compact support is a subsheaf of the direct image. By definition, $(f_{!}{\mathcal {F}})(V)$ consists of those $s\in {\mathcal {F}}(f^{-1}(V))$ whose support is mapped properly. If f is proper itself, then $f_{!}{\mathcal {F}}=f_{*}{\mathcal {F}}$ , but in general they disagree.

#### Inverse image

The pullback or inverse image goes the other way: it produces a sheaf on X , denoted $f^{-1}{\mathcal {G}}$ out of a sheaf ${\mathcal {G}}$ on Y . If f is the inclusion of an open subset, then the inverse image is just a restriction, i.e., it is given by $(f^{-1}{\mathcal {G}})(U)={\mathcal {G}}(U)$ for an open U in X . A sheaf ${\mathcal {F}}$ (on some space X ) is called locally constant if $X=\bigcup _{i\in I}U_{i}$ by some open subsets $U_{i}$ such that the restriction of ${\mathcal {F}}$ to all these open subsets is constant. On a wide range of topological spaces X , such sheaves are equivalent to representations of the fundamental group $\pi _{1}(X)$ .

For general maps f , the definition of $f^{-1}{\mathcal {G}}$ is more involved; it is detailed at inverse image functor. The stalk is an essential special case of the pullback in view of a natural identification, where i is as above:

${\mathcal {G}}_{x}=i^{-1}{\mathcal {G}}(\{x\}).$

More generally, stalks satisfy $(f^{-1}{\mathcal {G}})_{x}={\mathcal {G}}_{f(x)}$ .

#### Extension by zero

For the inclusion $j:U\to X$ of an open subset, the *extension by zero* $j_{!}{\mathcal {F}}$ (pronounced "j lower shriek of F") of a sheaf ${\mathcal {F}}$ of abelian groups on U is the sheafification of the presheaf defined by

$V\mapsto {\begin{cases}{\mathcal {F}}(V)&{\textrm {if}}\ V\subseteq U\\0&{\textrm {otherwise.}}\end{cases}}$

For a sheaf ${\mathcal {G}}$ on X , this construction is in a sense complementary to $i_{*}$ , where $i:X\setminus U\to X$ is the inclusion of the complement of U :

$(j_{!}j^{*}{\mathcal {G}})_{x}={\mathcal {G}}_{x}$

for

x

in

U

, and the stalk is zero otherwise, while

$(i_{*}i^{*}{\mathcal {G}})_{x}=0$

for

x

in

U

, and equals

${\mathcal {G}}_{x}$

otherwise.

More generally, if $A\subset X$ is a locally closed subset, then there exists an open U of X containing A such that A is closed in U . Let $f:A\to U$ and $j:U\to X$ be the natural inclusions. Then the *extension by zero* of a sheaf ${\mathcal {F}}$ on A is defined by $j_{!}f_{*}F$ .

Due to its nice behavior on stalks, the extension by zero functor is useful for reducing sheaf-theoretic questions on X to ones on the strata of a stratification, i.e., a decomposition of X into smaller, locally closed subsets.


## Complements

### Sheaves in more general categories

In addition to (pre-)sheaves as introduced above, where ${\mathcal {F}}(U)$ is merely a set, it is in many cases important to keep track of additional structure on these sections. For example, the sections of the sheaf of continuous functions naturally form a real vector space, and restriction is a linear map between these vector spaces.

Presheaves with values in an arbitrary category C are defined by first considering the category of open sets on X to be the posetal category $O(X)$ whose objects are the open sets of X and whose morphisms are inclusions. Then a C -valued presheaf on X is the same as a contravariant functor from $O(X)$ to C . Morphisms in this category of functors, also known as natural transformations, are the same as the morphisms defined above, as can be seen by unraveling the definitions.

If the target category C admits all limits, a C -valued presheaf is a sheaf if the following diagram is an equalizer for every open cover ${\mathcal {U}}=\{U_{i}\}_{i\in I}$ of any open set U :

$F(U)\rightarrow \prod _{i}F(U_{i}){{{} \atop \longrightarrow } \atop {\longrightarrow \atop {}}}\prod _{i,j}F(U_{i}\cap U_{j}).$

Here the first map is the product of the restriction maps

$\operatorname {res} _{U_{i},U}\colon F(U)\rightarrow F(U_{i})$

and the pair of arrows the products of the two sets of restrictions

$\operatorname {res} _{U_{i}\cap U_{j},U_{i}}\colon F(U_{i})\rightarrow F(U_{i}\cap U_{j})$

and

$\operatorname {res} _{U_{i}\cap U_{j},U_{j}}\colon F(U_{j})\rightarrow F(U_{i}\cap U_{j}).$

If C is an abelian category, this condition can also be rephrased by requiring that there is an exact sequence

$0\to F(U)\to \prod _{i}F(U_{i})\xrightarrow {\operatorname {res} _{U_{i}\cap U_{j},U_{i}}-\operatorname {res} _{U_{i}\cap U_{j},U_{j}}} \prod _{i,j}F(U_{i}\cap U_{j}).$

A particular case of this sheaf condition occurs for U being the empty set, and the index set I also being empty. In this case, the sheaf condition requires ${\mathcal {F}}(\emptyset )$ to be the terminal object in C .

### Ringed spaces and sheaves of modules

In several geometrical disciplines, including algebraic geometry and differential geometry, the spaces come along with a natural sheaf of rings, often called the structure sheaf and denoted by ${\mathcal {O}}_{X}$ . Such a pair $(X,{\mathcal {O}}_{X})$ is called a *ringed space*. Many types of spaces can be defined as certain types of ringed spaces. Commonly, all the stalks ${\mathcal {O}}_{X,x}$ of the structure sheaf are local rings, in which case the pair is called a *locally ringed space*.

For example, an n -dimensional $C^{k}$ manifold M is a locally ringed space whose structure sheaf consists of $C^{k}$ -functions on the open subsets of M . The property of being a *locally* ringed space translates into the fact that such a function, which is nonzero at a point x , is also non-zero on a sufficiently small open neighborhood of x . Some authors actually *define* real (or complex) manifolds to be locally ringed spaces that are locally isomorphic to the pair consisting of an open subset of $\mathbb {R} ^{n}$ (respectively $\mathbb {C} ^{n}$ ) together with the sheaf of $C^{k}$ (respectively holomorphic) functions. Similarly, schemes, the foundational notion of spaces in algebraic geometry, are locally ringed spaces that are locally isomorphic to the spectrum of a ring.

Given a ringed space, a *sheaf of modules* is a sheaf ${\mathcal {M}}$ such that on every open set U of X , ${\mathcal {M}}(U)$ is an ${\mathcal {O}}_{X}(U)$ -module and for every inclusion of open sets $V\subseteq U$ , the restriction map ${\mathcal {M}}(U)\to {\mathcal {M}}(V)$ is compatible with the restriction map ${\mathcal {O}}(U)\to {\mathcal {O}}(V)$ : the restriction of $fs$ is the restriction of f times that of s for any f in ${\mathcal {O}}(U)$ and s in ${\mathcal {M}}(U)$ .

Most important geometric objects are sheaves of modules. For example, there is a one-to-one correspondence between vector bundles and locally free sheaves of ${\mathcal {O}}_{X}$ -modules. This paradigm applies to real vector bundles, complex vector bundles, or vector bundles in algebraic geometry (where ${\mathcal {O}}$ consists of smooth functions, holomorphic functions, or regular functions, respectively). Sheaves of solutions to differential equations are D -modules, that is, modules over the sheaf of differential operators. On any topological space, modules over the constant sheaf ${\underline {\mathbf {Z} }}$ are the same as sheaves of abelian groups in the sense above.

There is a different inverse image functor for sheaves of modules over sheaves of rings. This functor is usually denoted $f^{*}$ and it is distinct from $f^{-1}$ . See inverse image functor.

#### Finiteness conditions for sheaves of modules

Finiteness conditions for module over commutative rings give rise to similar finiteness conditions for sheaves of modules: ${\mathcal {M}}$ is called *finitely generated* (respectively *finitely presented*) if, for every point x of X , there exists an open neighborhood U of x , a natural number n (possibly depending on U ), and a surjective morphism of sheaves ${\mathcal {O}}_{X}^{n}|_{U}\to {\mathcal {M}}|_{U}$ (respectively, in addition a natural number m , and an exact sequence ${\mathcal {O}}_{X}^{m}|_{U}\to {\mathcal {O}}_{X}^{n}|_{U}\to {\mathcal {M}}|_{U}\to 0$ .) Paralleling the notion of a coherent module, ${\mathcal {M}}$ is called a *coherent sheaf* if it is of finite type and if, for every open set U and every morphism of sheaves $\phi :{\mathcal {O}}_{X}^{n}\to {\mathcal {M}}$ (not necessarily surjective), the kernel of $\phi$ is of finite type. ${\mathcal {O}}_{X}$ is *coherent* if it is coherent as a module over itself. Like for modules, coherence is in general a strictly stronger condition than finite presentation. The Oka coherence theorem states that the sheaf of holomorphic functions on a complex manifold is coherent.

### The étalé space of a sheaf

In the examples above it was noted that some sheaves occur naturally as sheaves of sections. In fact, all sheaves of sets can be represented as sheaves of sections of a topological space called the *étalé space*, from the French word French pronunciation: [étalé], meaning roughly "spread out". If $F\in {\text{Sh}}(X)$ is a sheaf over X , then the **étalé space** (sometimes called the **étale space**) of F is a topological space E together with a local homeomorphism $\pi :E\to X$ such that the sheaf of sections $\Gamma (\pi ,-)$ of $\pi$ is F . The space E is usually very strange, and even if the sheaf F arises from a natural topological situation, E may not have any clear topological interpretation. For example, if F is the sheaf of sections of a continuous function $f:Y\to X$ , then $E=Y$ if and only if f is a local homeomorphism.

The étalé space E is constructed from the stalks of F over X . As a set, it is their disjoint union and $\pi$ is the obvious map that takes the value x on the stalk of F over $x\in X$ . The topology of E is defined as follows. For each element $s\in F(U)$ and each $x\in U$ , we get a germ of s at x , denoted $[s]_{x}$ or $s_{x}$ . These germs determine points of E . For any U and $s\in F(U)$ , the union of these points (for all $x\in U$ ) is declared to be open in E . Notice that each stalk has the discrete topology as subspace topology. A morphism between two sheaves determine a continuous map of the corresponding étalé spaces that is compatible with the projection maps (in the sense that every germ is mapped to a germ over the same point). This makes the construction into a functor.

The construction above determines an equivalence of categories between the category of sheaves of sets on X and the category of étalé spaces over X . The construction of an étalé space can also be applied to a presheaf, in which case the sheaf of sections of the étalé space recovers the sheaf associated to the given presheaf.

This construction makes all sheaves into representable functors on certain categories of topological spaces. As above, let F be a sheaf on X , let E be its étalé space, and let $\pi :E\to X$ be the natural projection. Consider the overcategory ${\text{Top}}/X$ of topological spaces over X , that is, the category of topological spaces together with fixed continuous maps to X . Every object of this category is a continuous map $f:Y\to X$ , and a morphism from $Y\to X$ to $Z\to X$ is a continuous map $Y\to Z$ that commutes with the two maps to X . There is a functor

> $\Gamma :{\text{Top}}/X\to {\text{Sets}}$

sending an object $f:Y\to X$ to $f^{-1}F(Y)$ . For example, if $i:U\hookrightarrow X$ is the inclusion of an open subset, then

> $\Gamma (i)=f^{-1}F(U)=F(U)=\Gamma (F,U)$

and for the inclusion of a point $i:\{x\}\hookrightarrow X$ , then

> $\Gamma (i)=f^{-1}F(\{x\})=F|_{x}$

is the stalk of F at x . There is a natural isomorphism

> $(f^{-1}F)(Y)\cong \operatorname {Hom} _{\mathbf {Top} /X}(f,\pi )$ ,

which shows that $\pi :E\to X$ (for the étalé space) represents the functor $\Gamma$ .

E is constructed so that the projection map $\pi$ is a covering map. In algebraic geometry, the natural analog of a covering map is called an étale morphism. Despite its similarity to "étalé", the word étale [etal] has a different meaning in French. It is possible to turn E into a scheme and $\pi$ into a morphism of schemes in such a way that $\pi$ retains the same universal property, but $\pi$ is *not* in general an étale morphism because it is not quasi-finite. It is, however, formally étale.

The definition of sheaves by étalé spaces is older than the definition given earlier in the article. It is still common in some areas of mathematics such as mathematical analysis.


## Sheaf cohomology

In contexts where the open set U is fixed, and the sheaf is regarded as a variable, the set $F(U)$ is also often denoted $\Gamma (U,F).$

As was noted above, this functor does not preserve epimorphisms. Instead, an epimorphism of sheaves ${\mathcal {F}}\to {\mathcal {G}}$ is a map with the following property: for any section $g\in {\mathcal {G}}(U)$ there is a covering ${\mathcal {U}}=\{U_{i}\}_{i\in I}$ where

> $U=\bigcup _{i\in I}U_{i}$

of open subsets, such that the restriction $g|_{U_{i}}$ are in the image of ${\mathcal {F}}(U_{i})$ . However, g itself need not be in the image of ${\mathcal {F}}(U)$ . A concrete example of this phenomenon is the exponential map

${\mathcal {O}}{\stackrel {\exp }{\to }}{\mathcal {O}}^{\times }$ between the sheaf of holomorphic functions and non-zero holomorphic functions. This map is an epimorphism, which amounts to saying that any non-zero holomorphic function g (on some open subset in $\mathbb {C}$ , say), admits a complex logarithm *locally*, i.e., after restricting g to appropriate open subsets. However, g need not have a logarithm globally.

Sheaf cohomology captures this phenomenon. More precisely, for an exact sequence of sheaves of abelian groups $0\to {\mathcal {F}}_{1}\to {\mathcal {F}}_{2}\to {\mathcal {F}}_{3}\to 0,$ (i.e., an epimorphism ${\mathcal {F}}_{2}\to {\mathcal {F}}_{3}$ whose kernel is ${\mathcal {F}}_{1}$ ), there is a long exact sequence $0\to \Gamma (U,{\mathcal {F}}_{1})\to \Gamma (U,{\mathcal {F}}_{2})\to \Gamma (U,{\mathcal {F}}_{3})\to H^{1}(U,{\mathcal {F}}_{1})\to H^{1}(U,{\mathcal {F}}_{2})\to H^{1}(U,{\mathcal {F}}_{3})\to H^{2}(U,{\mathcal {F}}_{1})\to \dots$ By means of this sequence, the first cohomology group $H^{1}(U,{\mathcal {F}}_{1})$ is a measure for the non-surjectivity of the map between sections of ${\mathcal {F}}_{2}$ and ${\mathcal {F}}_{3}$ .

There are several different ways of constructing sheaf cohomology. Grothendieck (1957) introduced them by defining sheaf cohomology as the derived functor of $\Gamma$ . This method is theoretically satisfactory, but, being based on injective resolutions, of little use in concrete computations. Godement resolutions are another general, but practically inaccessible approach.

### Computing sheaf cohomology

Especially in the context of sheaves on manifolds, sheaf cohomology can often be computed using resolutions by soft sheaves, fine sheaves, and flabby sheaves (also known as ***flasque sheaves*** from the French *flasque* meaning flabby). For example, a partition of unity argument shows that the sheaf of smooth functions on a manifold is soft. The higher cohomology groups $H^{i}(U,{\mathcal {F}})$ for $i>0$ vanish for soft sheaves, which gives a way of computing cohomology of other sheaves. For example, the de Rham complex is a resolution of the constant sheaf ${\underline {\mathbf {R} }}$ on any smooth manifold, so the sheaf cohomology of ${\underline {\mathbf {R} }}$ is equal to its de Rham cohomology.

A different approach is by Čech cohomology. Čech cohomology was the first cohomology theory developed for sheaves and it is well-suited to concrete calculations, such as computing the coherent sheaf cohomology of complex projective space $\mathbb {P} ^{n}$ . It relates sections on open subsets of the space to cohomology classes on the space. In most cases, Čech cohomology computes the same cohomology groups as the derived functor cohomology. However, for some pathological spaces, Čech cohomology will give the correct $H^{1}$ but incorrect higher cohomology groups. To get around this, Jean-Louis Verdier developed hypercoverings. Hypercoverings not only give the correct higher cohomology groups but also allow the open subsets mentioned above to be replaced by certain morphisms from another space. This flexibility is necessary in some applications, such as the construction of Pierre Deligne's mixed Hodge structures.

Many other coherent sheaf cohomology groups are found using an embedding $i:X\hookrightarrow Y$ of a space X into a space with known cohomology, such as $\mathbb {P} ^{n}$ , or some weighted projective space. In this way, the known sheaf cohomology groups on these ambient spaces can be related to the sheaves $i_{*}{\mathcal {F}}$ , giving $H^{i}(Y,i_{*}{\mathcal {F}})\cong H^{i}(X,{\mathcal {F}})$ . For example, computing the coherent sheaf cohomology of projective plane curves is easily found. One big theorem in this space is the Hodge decomposition found using a spectral sequence associated to sheaf cohomology groups, proved by Deligne. Essentially, the $E_{1}$ -page with terms

> $E_{1}^{p,q}=H^{p}(X,\Omega _{X}^{q})$

the sheaf cohomology of a smooth projective variety X , degenerates, meaning $E_{1}=E_{\infty }$ . This gives the canonical Hodge structure on the cohomology groups $H^{k}(X,\mathbb {C} )$ . It was later found these cohomology groups can be easily explicitly computed using Griffiths residues. See Jacobian ideal. These kinds of theorems lead to one of the deepest theorems about the cohomology of algebraic varieties, the decomposition theorem, paving the path for Mixed Hodge modules.

Another clean approach to the computation of some cohomology groups is the Borel–Bott–Weil theorem, which identifies the cohomology groups of some line bundles on flag manifolds with irreducible representations of Lie groups. This theorem can be used, for example, to easily compute the cohomology groups of all line bundles on projective space and grassmann manifolds.

In many cases there is a duality theory for sheaves that generalizes Poincaré duality. See Grothendieck duality and Verdier duality.

### Derived categories of sheaves

The derived category of the category of sheaves of, say, abelian groups on some space *X*, denoted here as $D(X)$ , is the conceptual haven for sheaf cohomology, by virtue of the following relation: $H^{n}(X,{\mathcal {F}})=\operatorname {Hom} _{D(X)}(\mathbf {Z} ,{\mathcal {F}}[n]).$ The adjunction between $f^{-1}$ , which is the left adjoint of $f_{*}$ (already on the level of sheaves of abelian groups) gives rise to an adjunction $f^{-1}:D(Y)\rightleftarrows D(X):Rf_{*}$ (for $f:X\to Y$ ), where $Rf_{*}$ is the derived functor. This latter functor encompasses the notion of sheaf cohomology since $H^{n}(X,{\mathcal {F}})=R^{n}f_{*}{\mathcal {F}}$ for $f:X\to \{*\}$ .

Like $f_{*}$ , the direct image with compact support $f_{!}$ can also be derived. By virtue of the following isomorphism $Rf_{!}{\mathcal {F}}$ parametrizes the cohomology with compact support of the fibers of f : $(R^{i}f_{!}{\mathcal {F}})_{y}=H_{c}^{i}(f^{-1}(y),{\mathcal {F}}).$ This isomorphism is an example of a base change theorem. There is another adjunction $Rf_{!}:D(X)\rightleftarrows D(Y):f^{!}.$ Unlike all the functors considered above, the twisted (or exceptional) inverse image functor $f^{!}$ is in general only defined on the level of derived categories, i.e., the functor is not obtained as the derived functor of some functor between abelian categories. If $f:X\to \{*\}$ and *X* is a smooth orientable manifold of dimension *n*, then $f^{!}{\underline {\mathbf {R} }}\cong {\underline {\mathbf {R} }}[n].$ This computation, and the compatibility of the functors with duality (see Verdier duality) can be used to obtain a high-brow explanation of Poincaré duality. In the context of quasi-coherent sheaves on schemes, there is a similar duality known as coherent duality.

Perverse sheaves are certain objects in $D(X)$ , i.e., complexes of sheaves (but not in general sheaves proper). They are an important tool to study the geometry of singularities.

#### Derived categories of coherent sheaves and the Grothendieck group

Another important application of derived categories of sheaves is with the derived category of coherent sheaves on a scheme X denoted $D_{Coh}(X)$ . This was used by Grothendieck in his development of intersection theory using derived categories and K-theory, that the intersection product of subschemes $Y_{1},Y_{2}$ is represented in K-theory as

$[Y_{1}]\cdot [Y_{2}]=[{\mathcal {O}}_{Y_{1}}\otimes _{{\mathcal {O}}_{X}}^{\mathbf {L} }{\mathcal {O}}_{Y_{2}}]\in K({\text{Coh(X)}})$

where ${\mathcal {O}}_{Y_{i}}$ are coherent sheaves defined by the ${\mathcal {O}}_{X}$ -modules given by their structure sheaves.


## Sites and topoi

André Weil's Weil conjectures stated that there was a cohomology theory for algebraic varieties over finite fields that would give an analogue of the Riemann hypothesis. The cohomology of a complex manifold can be defined as the sheaf cohomology of the locally constant sheaf ${\underline {\mathbf {C} }}$ in the Euclidean topology, which suggests defining a Weil cohomology theory in positive characteristic as the sheaf cohomology of a constant sheaf. But the only classical topology on such a variety is the Zariski topology, and the Zariski topology has very few open sets, so few that the cohomology of any Zariski-constant sheaf on an irreducible variety vanishes (except in degree zero). Alexandre Grothendieck solved this problem by introducing Grothendieck topologies, which axiomatize the notion of *covering*. Grothendieck's insight was that the definition of a sheaf depends only on the open sets of a topological space, not on the individual points. Once he had axiomatized the notion of covering, open sets could be replaced by other objects. A presheaf takes each one of these objects to data, just as before, and a sheaf is a presheaf that satisfies the gluing axiom with respect to our new notion of covering. This allowed Grothendieck to define étale cohomology and ℓ-adic cohomology, which eventually were used to prove the Weil conjectures.

A category with a Grothendieck topology is called a *site*. A category of sheaves on a site is called a *topos* or a *Grothendieck topos*. The notion of a topos was later abstracted by William Lawvere and Miles Tierney to define an elementary topos, which has connections to mathematical logic.
