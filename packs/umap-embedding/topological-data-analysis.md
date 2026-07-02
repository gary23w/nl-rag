---
title: "Topological data analysis"
source: https://en.wikipedia.org/wiki/Topological_data_analysis
domain: umap-embedding
license: CC-BY-SA-4.0
tags: umap projection, manifold approximation, topological embedding, neighbor graph
fetched: 2026-07-02
---

# Topological data analysis

In applied mathematics, **topological data analysis** (**TDA**) is an approach to the analysis of datasets using techniques from topology. Extraction of information from datasets that are high-dimensional, incomplete and noisy is generally challenging. TDA provides a general framework to analyze such data in a manner that is insensitive to the particular metric chosen and provides dimensionality reduction and robustness to noise. Beyond this, it inherits functoriality, a fundamental concept of modern mathematics, from its topological nature, which allows it to adapt to new mathematical tools.

The initial motivation is to study the shape of data. TDA has combined algebraic topology and other tools from pure mathematics to allow mathematically rigorous study of "shape". The main tool is persistent homology, an adaptation of homology to point cloud data. Persistent homology has been applied to many types of data across many fields. Moreover, its mathematical foundation is also of theoretical importance. The unique features of TDA make it a promising bridge between topology and geometry.

## Basic theory

### Intuition

TDA is premised on the idea that the shape of data sets contains relevant information. Real high-dimensional data is typically sparse, and tends to have relevant low dimensional features. One task of TDA is to provide a precise characterization of this fact. For example, the trajectory of a simple predator-prey system governed by the Lotka–Volterra equations forms a closed circle in state space. TDA provides tools to detect and quantify such recurrent motion.

Many algorithms for data analysis, including those used in TDA, require setting various parameters. Without prior domain knowledge, the correct collection of parameters for a data set is difficult to choose. The main insight of persistent homology is to use the information obtained from all parameter values by encoding this huge amount of information into an understandable and easy-to-represent form. With TDA, there is a mathematical interpretation when the information is a homology group. In general, the assumption is that features that persist for a wide range of parameters are "true" features. Features persisting for only a narrow range of parameters are presumed to be noise, although the theoretical justification for this is unclear.

### Early history

Precursors to the full concept of persistent homology appeared gradually over time. In 1990, Patrizio Frosini introduced a pseudo-distance between submanifolds, and later the size function, which on 1-dim curves is equivalent to the 0th persistent homology. Nearly a decade later, Vanessa Robins studied the images of homomorphisms induced by inclusion. Finally, shortly thereafter, Herbert Edelsbrunner et al. introduced the concept of persistent homology together with an efficient algorithm and its visualization as a persistence diagram. Gunnar Carlsson et al. reformulated the initial definition and gave an equivalent visualization method called persistence barcodes, interpreting persistence in the language of commutative algebra.

In algebraic topology the persistent homology has emerged through the work of Sergey Barannikov on Morse theory. The set of critical values of smooth Morse function was canonically partitioned into pairs "birth-death", filtered complexes were classified, their invariants, equivalent to persistence diagram and persistence barcodes, together with the efficient algorithm for their calculation, were described under the name of canonical forms in 1994 by Barannikov.

### Concepts

Some widely used concepts are introduced below. Note that some definitions may vary from author to author.

A **point cloud** is often defined as a finite set of points in some Euclidean space, but may be taken to be any finite metric space.

The **Čech complex** of a point cloud is the *nerve* of the *cover* of balls of a fixed radius around each point in the cloud.

A **persistence module** $\mathbb {U}$ indexed by $\mathbb {Z}$ is a vector space $U_{t}$ for each $t\in \mathbb {Z}$ , and a linear map $u_{t}^{s}\colon U_{s}\to U_{t}$ whenever $s\leq t$ , such that $u_{t}^{t}=1$ for all t and $u_{t}^{s}u_{s}^{r}=u_{t}^{r}$ whenever $r\leq s\leq t.$ An equivalent definition is a functor from $\mathbb {Z}$ considered as a partially ordered set to the category of vector spaces.

The **persistent homology group** $PH$ of a point cloud is the persistence module defined as $PH_{k}(X)=\prod H_{k}(X_{r})$ , where $X_{r}$ is the Čech complex of radius r of the point cloud X and $H_{k}$ is the homology group.

A **persistence barcode** is a multiset of intervals in $\mathbb {R}$ , and a **persistence diagram** is a multiset of points in $\Delta$ ( $:=\{(u,v)\in \mathbb {R} ^{2}\mid u,v\geq 0,u\leq v\}$ ).

The **Wasserstein distance** between two persistence diagrams X and Y is defined as $W_{p}[L_{q}](X,Y):=\inf _{\varphi :X\to Y}\left[\sum _{x\in X}(\Vert x-\varphi (x)\Vert _{q})^{p}\right]^{1/p}$ where $1\leq p,q\leq \infty$ and $\varphi$ ranges over bijections between X and Y . Please refer to figure 3.1 in Munch for illustration.

The **bottleneck distance** between X and Y is $W_{\infty }[L_{q}](X,Y):=\inf _{\varphi :X\to Y}\sup _{x\in X}\Vert x-\varphi (x)\Vert _{q}.$ This is a special case of Wasserstein distance, letting $p=\infty$ .

### Basic property

#### Structure theorem

The first classification theorem for persistent homology appeared in 1994 via Barannikov's canonical forms. The classification theorem interpreting persistence in the language of commutative algebra appeared in 2005: for a finitely generated persistence module C with field F coefficients, $H(C;F)\simeq \bigoplus _{i}x^{t_{i}}\cdot F[x]\oplus \left(\bigoplus _{j}x^{r_{j}}\cdot (F[x]/(x^{s_{j}}\cdot F[x]))\right).$ Intuitively, the free parts correspond to the homology generators that appear at filtration level $t_{i}$ and never disappear, while the torsion parts correspond to those that appear at filtration level $r_{j}$ and last for $s_{j}$ steps of the filtration (or equivalently, disappear at filtration level $s_{j}+r_{j}$ ).

Persistent homology is visualized through a barcode or persistence diagram. The barcode has its root in abstract mathematics. Namely, the category of finite filtered complexes over a field is semi-simple. Any filtered complex is isomorphic to its canonical form, a direct sum of one- and two-dimensional simple filtered complexes.

#### Stability

Stability is desirable because it provides robustness against noise. If X is any space which is homeomorphic to a simplicial complex, and $f,g:X\to \mathbb {R}$ are continuous tame functions, then the persistence vector spaces $\{H_{k}(f^{-1}([0,r]))\}$ and $\{H_{k}(g^{-1}([0,r]))\}$ are finitely presented, and $W_{\infty }(D(f),D(g))\leq \lVert f-g\rVert _{\infty }$ , where $W_{\infty }$ refers to the bottleneck distance and D is the map taking a continuous tame function to the persistence diagram of its k -th homology.

### Workflow

The basic workflow in TDA is:

| point cloud | $\to$ | nested complexes | $\to$ | persistence module | $\to$ | barcode or diagram |
|---|---|---|---|---|---|---|

1. If X is a point cloud, replace X with a nested family of simplicial complexes $X_{r}$ (such as the Čech or Vietoris-Rips complex). This process converts the point cloud into a filtration of simplicial complexes. Taking the homology of each complex in this filtration gives a persistence module $H_{i}(X_{r_{0}})\to H_{i}(X_{r_{1}})\to H_{i}(X_{r_{2}})\to \cdots$
2. Apply the structure theorem to obtain the persistent Betti numbers, **persistence diagram,** or equivalently, **barcode.**

Graphically speaking,

## Computation

The first algorithm over all fields for persistent homology in algebraic topology setting was described by Barannikov through reduction to the canonical form by upper-triangular matrices. The algorithm for persistent homology over $F_{2}$ was given by Edelsbrunner et al. Afra Zomorodian and Carlsson gave the practical algorithm to compute persistent homology over all fields. Edelsbrunner and Harer's book gives general guidance on computational topology.

One issue that arises in computation is the choice of complex. The Čech complex and the Vietoris–Rips complex are most natural at first glance; however, their size grows rapidly with the number of data points. The Vietoris–Rips complex is preferred over the Čech complex because its definition is simpler and the Čech complex requires extra effort to define in a general finite metric space. Efficient ways to lower the computational cost of homology have been studied. For example, the α-complex and witness complex are used to reduce the dimension and size of complexes.

Recently, Discrete Morse theory has shown promise for computational homology because it can reduce a given simplicial complex to a much smaller cellular complex which is homotopic to the original one. This reduction can in fact be performed as the complex is constructed by using matroid theory, leading to further performance increases. Another recent algorithm saves time by ignoring the homology classes with low persistence.

Various software packages are available, such as javaPlex, Dionysus, Perseus, PHAT, DIPHA, GUDHI, Ripser, and TDAstats. A comparison between these tools is done by Otter et al. Giotto-tda is a Python package dedicated to integrating TDA in the machine learning workflow by means of a scikit-learn [1] API. An R package TDA is capable of calculating recently invented concepts like landscape and the kernel distance estimator. The Topology ToolKit is specialized for continuous data defined on manifolds of low dimension (1, 2 or 3), as typically found in scientific visualization. Cubicle is optimized for large (gigabyte-scale) grayscale image data in dimension 1, 2 or 3 using cubical complexes and discrete Morse theory. Another R package, TDAstats, uses the Ripser library to calculate persistent homology.

## Visualization

High-dimensional data is impossible to visualize directly. Many methods have been invented to extract a low-dimensional structure from the data set, such as principal component analysis and multidimensional scaling. However, it is important to note that the problem itself is ill-posed, since many different topological features can be found in the same data set. Thus, the study of visualization of high-dimensional spaces is of central importance to TDA, although it does not necessarily involve the use of persistent homology. However, recent attempts have been made to use persistent homology in data visualization.

Carlsson et al. have proposed a general method called **MAPPER**. It inherits the idea of Jean-Pierre Serre that a covering preserves homotopy. A generalized formulation of MAPPER is as follows:

Let X and Z be topological spaces and let $f\colon X\to Z$ be a continuous map. Let $\mathbb {U} =\{U_{\alpha }\}_{\alpha \in A}$ be a finite open covering of Z . The output of MAPPER is the nerve of the pullback cover ${\textstyle M(\mathbb {U} ,f):=N(f^{-1}(\mathbb {U} ))}$ , where each preimage is split into its connected components. This is a very general concept, of which the Reeb graph and merge trees are special cases.

This is not quite the original definition. Carlsson et al. choose Z to be $\mathbb {R}$ or $\mathbb {R} ^{2}$ , and cover it with open sets such that at most two intersect. This restriction means that the output is in the form of a complex network. Because the topology of a finite point cloud is trivial, clustering methods (such as single linkage) are used to produce the analogue of connected sets in the preimage $f^{-1}(U)$ when MAPPER is applied to actual data.

Mathematically speaking, MAPPER is a variation of the Reeb graph. If the ${\textstyle M(\mathbb {U} ,f)}$ is at most one dimensional, then for each $i\geq 0$ , $H_{i}(X)\simeq H_{0}(N(\mathbb {U} );{\hat {F}}_{i})\oplus H_{1}(N(\mathbb {U} );{\hat {F}}_{i-1}).$ The added flexibility also has disadvantages. One problem is instability, in that some change of the choice of the cover can lead to major change of the output of the algorithm. Work has been done to overcome this problem.

Three successful applications of MAPPER can be found in Carlsson et al. A comment on the applications in this paper by J. Curry is that "a common feature of interest in applications is the presence of flares or tendrils".

A free implementation of MAPPER written by Daniel Müllner and Aravindakshan Babu is available online. MAPPER also forms the basis of Ayasdi's AI platform.

## Multidimensional persistence

Multidimensional persistence is important to TDA. The concept arises in both theory and practice. The first investigation of multidimensional persistence was early in the development of TDA. Carlsson-Zomorodian introduced the theory of multidimensional persistence in and in collaboration with Singh introduced the use of tools from symbolic algebra (Gröbner basis methods) to compute MPH modules. Their definition presents multidimensional persistence with n parameters as a $\mathbb {Z} ^{n}$ graded module over a polynomial ring in n variables. Tools from commutative and homological algebra are applied to the study of multidimensional persistence in work of Harrington-Otter-Schenck-Tillman. The first application to appear in the literature is a method for shape comparison, similar to the invention of TDA.

The definition of an ***n*-dimensional persistence module** in $\mathbb {R} ^{n}$ is

- vector space $V_{s}$ is assigned to each point in $s=(s_{1},\ldots ,s_{n})$
- map $\rho _{s}^{t}\colon V_{s}\to V_{t}$ is assigned if $s\leq t$ ( $s_{i}\leq t_{i},i=1,\ldots ,n)$
- maps satisfy $\rho _{r}^{t}=\rho _{s}^{t}\circ \rho _{r}^{s}$ for all $r\leq s\leq t$

It might be worth noting that there are controversies on the definition of multidimensional persistence.

One of the advantages of one-dimensional persistence is its representability by a diagram or barcode. However, discrete complete invariants of multidimensional persistence modules do not exist. The main reason for this is that the structure of the collection of indecomposables is extremely complicated by Gabriel's theorem in the theory of quiver representations, although a finitely generated n-dim persistence module can be uniquely decomposed into a direct sum of indecomposables due to the Krull-Schmidt theorem.

Nonetheless, many results have been established. Carlsson and Zomorodian introduced the **rank invariant** $\rho _{M}(u,v)$ , defined as the $\rho _{M}(u,v)=\mathrm {rank} (x^{u-v}\colon M_{u}\to M_{v})$ , in which M is a finitely generated n-graded module. In one dimension, it is equivalent to the barcode. In the literature, the rank invariant is often referred as the persistent Betti numbers (PBNs). In many theoretical works, authors have used a more restricted definition, an analogue from sublevel set persistence. Specifically, the persistence Betti numbers of a function $f:X\to \mathbb {R} ^{k}$ are given by the function $\beta _{f}\colon \Delta ^{+}\to \mathrm {N}$ , taking each $(u,v)\in \Delta ^{+}$ to $\beta _{f}(u,v):=\mathrm {rank} (H(X(f\leq u)\to H(X(f\leq v)))$ , where $\Delta ^{+}:=\{(u,v)\in \mathbb {R} ^{k}\times \mathbb {R} ^{k}:u\leq v\}$ and $X(f\leq u):=\{x\in X:f(x)\leq u\}$ .

Some basic properties include monotonicity and diagonal jump. Persistent Betti numbers will be finite if X is a compact and locally contractible subspace of $\mathbb {R} ^{n}$ .

Using a foliation method, the k-dim PBNs can be decomposed into a family of 1-dim PBNs by dimensionality deduction. This method has also led to a proof that multi-dim PBNs are stable. The discontinuities of PBNs only occur at points $(u,v)(u\leq v)$ where either u is a discontinuous point of $\rho _{M}(\star ,v)$ or v is a discontinuous point of $\rho (u,\star )$ under the assumption that $f\in C^{0}(X,\mathbb {R} ^{k})$ and X is a compact, triangulable topological space.

Persistent space, a generalization of persistent diagram, is defined as the multiset of all points with multiplicity larger than 0 and the diagonal. It provides a stable and complete representation of PBNs. An ongoing work by Carlsson et al. is trying to give geometric interpretation of persistent homology, which might provide insights on how to combine machine learning theory with topological data analysis.

The first practical algorithm to compute multidimensional persistence was invented very early. After then, many other algorithms have been proposed, based on such concepts as discrete morse theory and finite sample estimating.

## Other persistences

The standard paradigm in TDA is often referred as **sublevel persistence**. Apart from multidimensional persistence, many works have been done to extend this special case.

### Zigzag persistence

The nonzero maps in persistence module are restricted by the preorder relationship in the category. However, mathematicians have found that the unanimity of direction is not essential to many results. "The philosophical point is that the decomposition theory of graph representations is somewhat independent of the orientation of the graph edges". Zigzag persistence is important to the theoretical side. The examples given in Carlsson's review paper to illustrate the importance of functorality all share some of its features.

### Extended persistence and levelset persistence

There are some attempts to loosen the stricter restriction of the function. Please refer to the Categorification and cosheaves and Impact on mathematics sections for more information.

It's natural to extend persistence homology to other basic concepts in algebraic topology, such as cohomology and relative homology/cohomology. An interesting application is the computation of circular coordinates for a data set via the first persistent cohomology group.

### Circular persistence

Normal persistence homology studies real-valued functions. The circle-valued map might be useful, "persistence theory for circle-valued maps promises to play the role for some vector fields as does the standard persistence theory for scalar fields", as commented in Dan Burghelea et al. The main difference is that Jordan cells (very similar in format to the Jordan blocks in linear algebra) are nontrivial in circle-valued functions, which would be zero in real-valued case, and combining with barcodes give the invariants of a tame map, under moderate conditions.

Two techniques they use are Morse-Novikov theory and graph representation theory. More recent results can be found in D. Burghelea et al. For example, the tameness requirement can be replaced by the much weaker condition, continuous.

### Persistence with torsion

The proof of the structure theorem relies on the base domain being field, so not many attempts have been made on persistence homology with torsion. Frosini defined a pseudometric on this specific module and proved its stability. One of its novelty is that it doesn't depend on some classification theory to define the metric.

## Categorification and cosheaves

One advantage of category theory is its ability to lift concrete results to a higher level, showing relationships between seemingly unconnected objects. Peter Bubenik et al. offers a short introduction of category theory fitted for TDA.

Category theory is the language of modern algebra, and has been widely used in the study of algebraic geometry and topology. It has been noted that "the key observation of is that the persistence diagram produced by depends only on the algebraic structure carried by this diagram." The use of category theory in TDA has proved to be fruitful.

Following the notations made in Bubenik et al., the **indexing category** ${\textstyle P}$ is any preordered set (not necessarily $\mathbb {N}$ or $\mathbb {R}$ ), the target category D is any category (instead of the commonly used ${\textstyle \mathrm {Vect} _{\mathbb {F} }}$ ), and functors ${\textstyle P\to D}$ are called **generalized persistence modules** in D , over ${\textstyle P}$ .

One advantage of using category theory in TDA is a clearer understanding of concepts and the discovery of new relationships between proofs. Take two examples for illustration. The understanding of the correspondence between interleaving and matching is of huge importance, since matching has been the method used in the beginning (modified from Morse theory). A summary of works can be found in Vin de Silva et al. Many theorems can be proved much more easily in a more intuitive setting. Another example is the relationship between the construction of different complexes from point clouds. It has long been noticed that Čech and Vietoris-Rips complexes are related. Specifically, $V_{r}(X)\subset C_{{\sqrt {2}}r}(X)\subset V_{2r}(X)$ . The essential relationship between Cech and Rips complexes can be seen much more clearly in categorical language.

The language of category theory also helps cast results in terms recognizable to the broader mathematical community. Bottleneck distance is widely used in TDA because of the results on stability with respect to the bottleneck distance. In fact, the interleaving distance is the terminal object in a poset category of stable metrics on multidimensional persistence modules in a prime field.

Sheaves, a central concept in modern algebraic geometry, are intrinsically related to category theory. Roughly speaking, sheaves are the mathematical tool for understanding how local information determines global information. Justin Curry regards level set persistence as the study of fibers of continuous functions. The objects that he studies are very similar to those by MAPPER, but with sheaf theory as the theoretical foundation. Although no breakthrough in the theory of TDA has yet used sheaf theory, it is promising since there are many beautiful theorems in algebraic geometry relating to sheaf theory. For example, a natural theoretical question is whether different filtration methods result in the same output.

## Stability

Stability is of central importance to data analysis, since real data carry noises. By usage of category theory, Bubenik et al. have distinguished between soft and hard stability theorems, and proved that soft cases are formal. Specifically, general workflow of TDA is

| data | ${\stackrel {F}{\longrightarrow }}$ | topological persistence module | ${\stackrel {H}{\longrightarrow }}$ | algebraic persistence module | ${\stackrel {J}{\longrightarrow }}$ | discrete invariant |
|---|---|---|---|---|---|---|

The soft stability theorem asserts that $HF$ is Lipschitz continuous, and the hard stability theorem asserts that J is Lipschitz continuous.

Bottleneck distance is widely used in TDA. The isometry theorem asserts that the **interleaving distance** $d_{I}$ is equal to the bottleneck distance. Bubenik et al. have abstracted the definition to that between functors $F,G\colon P\to D$ when ${\textstyle P}$ is equipped with a sublinear projection or superlinear family, in which still remains a pseudometric. Considering the magnificent characters of interleaving distance, here we introduce the general definition of interleaving distance(instead of the first introduced one): Let $\Gamma ,K\in \mathrm {Trans_{P}}$ (a function from ${\textstyle P}$ to ${\textstyle P}$ which is monotone and satisfies $x\leq \Gamma (x)$ for all ${\textstyle x\in P}$ ). A $(\Gamma ,K)$ -interleaving between F and G consists of natural transformations $\varphi \colon F\Rightarrow G\Gamma$ and $\psi \colon G\Rightarrow FK$ , such that $(\psi \Gamma )=\varphi F\eta _{K\Gamma }$ and $(\varphi \Gamma )=\psi G\eta _{\Gamma K}$ .

The two main results are

- Let ${\textstyle P}$ be a preordered set with a sublinear projection or superlinear family. Let ${\textstyle H:D\to E}$ be a functor between arbitrary categories ${\textstyle D,E}$ . Then for any two functors ${\textstyle F,G\colon P\to D}$ , we have ${\textstyle d_{I}(HF,HG)\leq d_{I}(F,G)}$ .
- Let ${\textstyle P}$ be a poset of a metric space ${\textstyle Y}$ , ${\textstyle X}$ be a topological space. And let ${\textstyle f,g\colon X\to Y}$ (not necessarily continuous) be functions, and ${\textstyle F,G}$ to be the corresponding persistence diagram. Then $d_{I}(F,G)\leq d_{\infty }(f,g):=\sup _{x\in X}d_{Y}(f(x),g(x))$ .

These two results summarize many results on stability of different models of persistence.

For the stability theorem of multidimensional persistence, please refer to the subsection of persistence.

## Structure theorem

The structure theorem is of central importance to TDA; as commented by G. Carlsson, "what makes homology useful as a discriminator between topological spaces is the fact that there is a classification theorem for finitely generated abelian groups". (see the fundamental theorem of finitely generated abelian groups).

The main argument used in the proof of the original structure theorem is the standard structure theorem for finitely generated modules over a principal ideal domain. However, this argument fails if the indexing set is $(\mathbb {R} ,\leq )$ .

In general, not every persistence module can be decomposed into intervals. Many attempts have been made at relaxing the restrictions of the original structure theorem. The case for pointwise finite-dimensional persistence modules indexed by a locally finite subset of $\mathbb {R}$ is solved based on the work of Webb. The most notable result is done by Crawley-Boevey, which solved the case of $\mathbb {R}$ . Crawley-Boevey's theorem states that any pointwise finite-dimensional persistence module is a direct sum of interval modules.

To understand the definition of his theorem, some concepts need introducing. An **interval** in $(\mathbb {R} ,\leq )$ is defined as a subset $I\subset \mathbb {R}$ having the property that if $r,t\in I$ and if there is an $s\in \mathbb {R}$ such that $r\leq s\leq t$ , then $s\in I$ as well. An **interval module** $k_{I}$ assigns to each element $s\in I$ the vector space k and assigns the zero vector space to elements in $\mathbb {R} \setminus I$ . All maps $\rho _{s}^{t}$ are the zero map, unless $s,t\in I$ and $s\leq t$ , in which case $\rho _{s}^{t}$ is the identity map. Interval modules are indecomposable.

Although the result of Crawley-Boevey is a very powerful theorem, it still doesn't extend to the q-tame case. A persistence module is **q-tame** if the rank of $\rho _{s}^{t}$ is finite for all $s<t$ . There are examples of q-tame persistence modules that fail to be pointwise finite. However, it turns out that a similar structure theorem still holds if the features that exist only at one index value are removed. This holds because the infinite dimensional parts at each index value do not persist, due to the finite-rank condition. Formally, the observable category $\mathrm {Ob}$ is defined as $\mathrm {Pers} /\mathrm {Eph}$ , in which $\mathrm {Eph}$ denotes the full subcategory of $\mathrm {Pers}$ whose objects are the ephemeral modules ( $\rho _{s}^{t}=0$ whenever $s<t$ ).

Note that the extended results listed here do not apply to zigzag persistence, since the analogue of a zigzag persistence module over $\mathbb {R}$ is not immediately obvious.

## Statistics

Real data is always finite, and so its study requires us to take stochasticity into account. Statistical analysis gives us the ability to separate true features of the data from artifacts introduced by random noise. Persistent homology has no inherent mechanism to distinguish between low-probability features and high-probability features.

One way to apply statistics to topological data analysis is to study the statistical properties of topological features of point clouds. The study of random simplicial complexes offers some insight into statistical topology. Katharine Turner et al. offers a summary of work in this vein.

A second way is to study probability distributions on the persistence space. The persistence space $B_{\infty }$ is $\coprod _{n}B_{n}/{\backsim }$ , where $B_{n}$ is the space of all barcodes containing exactly n intervals and the equivalences are $\{[x_{1},y_{1}],[x_{2},y_{2}],\ldots ,[x_{n},y_{n}]\}\backsim \{[x_{1},y_{1}],[x_{2},y_{2}],\ldots ,[x_{n-1},y_{n-1}]\}$ if $x_{n}=y_{n}$ . This space is fairly complicated; for example, it is not complete under the bottleneck metric. The first attempt made to study it is by Yuriy Mileyko et al. The space of persistence diagrams $D_{p}$ in their paper is defined as $D_{p}:=\left\{d\mid \sum _{x\in d}\left(2\inf _{y\in \Delta }\lVert x-y\rVert \right)^{p}<\infty \right\}$ where $\Delta$ is the diagonal line in $\mathbb {R} ^{2}$ . A nice property is that $D_{p}$ is complete and separable in the Wasserstein metric $W_{p}(u,v)=\left(\inf _{\gamma \in \Gamma (u,v)}\int _{\mathbb {X} \times \mathbb {X} }\rho ^{p}(x,y)\,\mathrm {d} \gamma (x,y)\right)^{1/p}$ . Expectation, variance, and conditional probability can be defined in the Fréchet sense. This allows many statistical tools to be ported to TDA. Works on null hypothesis significance test, confidence intervals, and robust estimates are notable steps.

A third way is to consider the cohomology of probabilistic space or statistical systems directly, called information structures and basically consisting in the triple ( $\Omega ,\Pi ,P$ ), sample space, random variables and probability laws. Random variables are considered as partitions of the n atomic probabilities (seen as a probability (n-1)-simplex, $|\Omega |=n$ ) on the lattice of partitions ( $\Pi _{n}$ ). The random variables or modules of measurable functions provide the cochain complexes while the coboundary is considered as the general homological algebra first discovered by Gerhard Hochschild with a left action implementing the action of conditioning. The first cocycle condition corresponds to the chain rule of entropy, allowing to derive uniquely up to the multiplicative constant, Shannon entropy as the first cohomology class. The consideration of a deformed left-action generalises the framework to Tsallis entropies. The information cohomology is an example of ringed topos. Multivariate k-Mutual information appear in coboundaries expressions, and their vanishing, related to cocycle condition, gives equivalent conditions for statistical independence. Minima of mutual-informations, also called synergy, give rise to interesting independence configurations analog to homotopical links. Because of its combinatorial complexity, only the simplicial subcase of the cohomology and of information structure has been investigated on data. Applied to data, those cohomological tools quantifies statistical dependences and independences, including Markov chains and conditional independence, in the multivariate case. Notably, mutual-informations generalize correlation coefficient and covariance to non-linear statistical dependences. These approaches were developed independently and only indirectly related to persistence methods, but may be roughly understood in the simplicial case using Hu Kuo Tin Theorem that establishes one-to-one correspondence between mutual-informations functions and finite measurable function of a set with intersection operator, to construct the Čech complex skeleton. Information cohomology offers some direct interpretation and application in terms of neuroscience (neural assembly theory and qualitative cognition), statistical physic, and deep neural network for which the structure and learning algorithm are imposed by the complex of random variables and the information chain rule.

Persistence landscapes, introduced by Peter Bubenik, are a different way to represent barcodes, more amenable to statistical analysis. The **persistence landscape** of a persistent module M is defined as a function $\lambda :\mathbb {N} \times \mathbb {R} \to {\bar {\mathbb {R} }}$ , $\lambda (k,t):=\sup(m\geq 0\mid \beta ^{t-m,t-m}\geq k)$ , where ${\bar {\mathbb {R} }}$ denotes the extended real line and $\beta ^{a,b}=\mathrm {dim} (\mathrm {im} (M(a\leq b)))$ . The space of persistence landscapes is very nice: it inherits all good properties of barcode representation (stability, easy representation, etc.), but statistical quantities can be readily defined, and some problems in Y. Mileyko et al.'s work, such as the non-uniqueness of expectations, can be overcome. Effective algorithms for computation with persistence landscapes are available. Another approach is to use revised persistence, which is image, kernel and cokernel persistence.

## Applications

### Classification of applications

More than one way exists to classify the applications of TDA. Perhaps the most natural way is by field. A very incomplete list of successful applications includes data skeletonization, shape study, graph reconstruction, image analysis, material, progression analysis of disease, sensor network, signal analysis, cosmic web, complex network, fractal geometry, viral evolution, propagation of contagions on networks, bacteria classification using molecular spectroscopy, super-resolution microscopy, hyperspectral imaging in physical-chemistry, remote sensing, feature selection, and early warning signs of financial crashes.

Another way is by distinguishing the techniques by G. Carlsson,

> one being the study of homological invariants of data on individual data sets, and the other is the use of homological invariants in the study of databases where the data points themselves have geometric structure.

### Impact on mathematics

Topological data analysis and persistent homology have had impacts on Morse theory. Morse theory has played a very important role in the theory of TDA, including on computation. Some work in persistent homology has extended results about Morse functions to tame functions or, even to continuous functions. A forgotten result of R. Deheuvels long before the invention of persistent homology extends Morse theory to all continuous functions.

One recent result is that the category of Reeb graphs is equivalent to a particular class of cosheaf. This is motivated by theoretical work in TDA, since the Reeb graph is related to Morse theory and MAPPER is derived from it. The proof of this theorem relies on the interleaving distance.

Persistent homology is closely related to spectral sequences. In particular the algorithm bringing a filtered complex to its canonical form permits much faster calculation of spectral sequences than the standard procedure of calculating $E_{p,q}^{r}$ groups page by page. Zigzag persistence may turn out to be of theoretical importance to spectral sequences.

### DONUT: A Database of TDA Applications

The Database of Original & Non-Theoretical Uses of Topology (DONUT) is a database of scholarly articles featuring practical applications of topological data analysis to various areas of science. DONUT was started in 2017 by Barbara Giunti, Janis Lazovskis, and Bastian Rieck, and as of October 2023 currently contains 447 articles. DONUT was featured in the November 2023 issue of the *Notices of the American Mathematical Society*.

### Applications to Adversarial ML

The stability property of topological features to small perturbations has been applied to make Graph Neural Networks robust against adversaries. Arafat et. al. proposed a robustness framework which systematically integrates both local and global topological graph feature representations, the impact of which is controlled by the robust regularized topological loss. Given the attacker's budget, they derived stability guarantees on the node representations, establishing an important connection between Topological stability and Adversarial ML.
