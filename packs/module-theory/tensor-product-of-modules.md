---
title: "Tensor product of modules"
source: https://en.wikipedia.org/wiki/Tensor_product_of_modules
domain: module-theory
license: CC-BY-SA-4.0
tags: module theory, projective module, injective module, flat module
fetched: 2026-07-02
---

# Tensor product of modules

In mathematics, the **tensor product of modules** is a construction that allows arguments about bilinear maps (e.g. multiplication) to be carried out in terms of linear maps. The module construction is analogous to the construction of the tensor product of vector spaces, but can be carried out for a pair of modules over a commutative ring resulting in a third module, and also for a pair of a right-module and a left-module over any ring, with result an abelian group. Tensor products are important in areas of abstract algebra, homological algebra, algebraic topology, algebraic geometry, operator algebras and noncommutative geometry. The universal property of the tensor product of vector spaces extends to more general situations in abstract algebra. The tensor product of an algebra and a module can be used for extension of scalars. For a commutative ring, the tensor product of modules can be iterated to form the tensor algebra of a module, allowing one to define multiplication in the module in a universal way.

## Balanced product

For a ring *R*, a right *R*-module *M*, a left *R*-module *N*, and an abelian group *G*, a map *φ*: *M* × *N* → *G* is said to be ***R*-balanced**, ***R*-middle-linear** or an ***R*-balanced product** if for all *m*, *m*′ in *M*, *n*, *n*′ in *N*, and *r* in *R* the following hold: ${\begin{aligned}\varphi (m,n+n')&=\varphi (m,n)+\varphi (m,n')&&{\text{Dl}}_{\varphi }\\\varphi (m+m',n)&=\varphi (m,n)+\varphi (m',n)&&{\text{Dr}}_{\varphi }\\\varphi (m\cdot r,n)&=\varphi (m,r\cdot n)&&{\text{A}}_{\varphi }\\\end{aligned}}$

The set of all such balanced products over *R* from *M* × *N* to *G* is denoted by L*R*(*M*, *N*; *G*).

If *φ*, *ψ* are balanced products, then each of the operations *φ* + *ψ* and −*φ* defined pointwise is a balanced product. This turns the set L*R*(*M*, *N*; *G*) into an abelian group.

For *M* and *N* fixed, the map *G* ↦ L*R*(*M*, *N*; *G*) is a functor from the category of abelian groups to itself. The morphism part is given by mapping a group homomorphism *g* : *G* → *G*′ to the function *φ* ↦ *g* ∘ *φ*, which goes from L*R*(*M*, *N*; *G*) to L*R*(*M*, *N*; *G*′).

**Remarks**

1. Properties (Dl) and (Dr) express biadditivity of *φ*, which may be regarded as distributivity of *φ* over addition.
2. Property (A) resembles some associative property of *φ*.
3. Every ring *R* is an *R*-bimodule. So the ring multiplication (*r*, *r*′) ↦ *r* ⋅ *r*′ in *R* is an *R*-balanced product *R* × *R* → *R*.

## Definition

For a ring *R*, a right *R*-module *M*, a left *R*-module *N*, the **tensor product** over *R* $M\otimes _{R}N$ is an abelian group together with a balanced product (as defined above) $\otimes :M\times N\to M\otimes _{R}N$ which is universal in the following sense:

For every abelian group

G

and every balanced product

$f:M\times N\to G$

there is a

unique

group homomorphism

${\tilde {f}}:M\otimes _{R}N\to G$

such that

${\tilde {f}}\circ \otimes =f.$

As with all universal properties, the above property defines the tensor product uniquely up to a unique isomorphism: any other abelian group and balanced product with the same properties will be isomorphic to *M* ⊗*R* *N* and ⊗. Indeed, the mapping ⊗ is called *canonical*, or more explicitly: the canonical mapping (or balanced product) of the tensor product.

The definition does not prove the existence of *M* ⊗*R* *N*; see below for a construction.

The tensor product can also be defined as a representing object for the functor *G* → L*R*(*M*,*N*;*G*); explicitly, this means there is a natural isomorphism: ${\begin{cases}\operatorname {Hom} _{\mathbb {Z} }(M\otimes _{R}N,G)\simeq \operatorname {L} _{R}(M,N;G)\\g\mapsto g\circ \otimes \end{cases}}$

This is a succinct way of stating the universal mapping property given above. (If a priori one is given this natural isomorphism, then $\otimes$ can be recovered by taking $G=M\otimes _{R}N$ and then mapping the identity map.)

Similarly, given the natural identification ⁠ $\operatorname {L} _{R}(M,N;G)=\operatorname {Hom} _{R}(M,\operatorname {Hom} _{\mathbb {Z} }(N,G))$ ⁠, one can also define *M* ⊗*R* *N* by the formula $\operatorname {Hom} _{\mathbb {Z} }(M\otimes _{R}N,G)\simeq \operatorname {Hom} _{R}(M,\operatorname {Hom} _{\mathbb {Z} }(N,G)).$

This is known as the tensor-hom adjunction; see also § Properties.

For each *x* in *M*, *y* in *N*, one writes

x

⊗

y

for the image of (*x*, *y*) under the canonical map ⁠ $\otimes :M\times N\to M\otimes _{R}N$ ⁠. It is often called a pure tensor. Strictly speaking, the correct notation would be *x* ⊗*R* *y* but it is conventional to drop *R* here. Then, immediately from the definition, there are relations:

| *x* ⊗ (*y* + *y*′) = *x* ⊗ *y* + *x* ⊗ *y*′ | (Dl⊗) |
|---|---|
| (*x* + *x*′) ⊗ *y* = *x* ⊗ *y* + *x*′ ⊗ *y* | (Dr⊗) |
| (*x* ⋅ *r*) ⊗ *y* = *x* ⊗ (*r* ⋅ *y*) | (A⊗) |

The universal property of a tensor product has the following important consequence:

**Proposition**—Every element of $M\otimes _{R}N$ can be written, non-uniquely, as $\sum _{i}x_{i}\otimes y_{i},\,x_{i}\in M,y_{i}\in N.$ In other words, the image of $\otimes$ generates $M\otimes _{R}N$ . Furthermore, if *f* is a function defined on elements $x\otimes y$ with values in an abelian group *G*, then *f* extends uniquely to a homomorphism defined on the whole of $M\otimes _{R}N$ if and only if $f(x\otimes y)$ is $\mathbb {Z}$ -bilinear in *x* and *y*.

Proof: For the first statement, let *L* be the subgroup of $M\otimes _{R}N$ generated by elements of the form in question, $Q=(M\otimes _{R}N)/L$ and *q* the quotient map to *Q*. We have: $0=q\circ \otimes$ as well as ⁠ $0=0\circ \otimes$ ⁠. Hence, by the uniqueness part of the universal property, *q* = 0. The second statement is because to define a module homomorphism, it is enough to define it on the generating set of the module. $\square$

## Application of the universal property of tensor products

### Determining whether a tensor product of modules is zero

In practice, it is sometimes more difficult to show that a tensor product of *R*-modules $M\otimes _{R}N$ is nonzero than it is to show that it is 0. The universal property gives a convenient way for checking this.

To check that a tensor product $M\otimes _{R}N$ is nonzero, one can construct an *R*-bilinear map $f:M\times N\rightarrow G$ to an abelian group G such that ⁠ $f(m,n)\neq 0$ ⁠. This works because if ⁠ $m\otimes n=0$ ⁠, then ⁠ $f(m,n)={\bar {f}}(m\otimes n)={\bar {(f)}}(0)=0$ ⁠.

For example, to see that ⁠ $\mathbb {Z} /p\mathbb {Z} \otimes _{\mathbb {Z} }\mathbb {Z} /p\mathbb {Z}$ ⁠, is nonzero, take G to be $\mathbb {Z} /p\mathbb {Z}$ and ⁠ $(m,n)\mapsto mn$ ⁠. This says that the pure tensors $m\otimes n\neq 0$ as long as $mn$ is nonzero in ⁠ $\mathbb {Z} /p\mathbb {Z}$ ⁠.

### For equivalent modules

The proposition says that one can work with explicit elements of the tensor products instead of invoking the universal property directly each time. This is very convenient in practice. For example, if *R* is commutative and the left and right actions by *R* on modules are considered to be equivalent, then $M\otimes _{R}N$ can naturally be furnished with the *R*-scalar multiplication by extending $r\cdot (x\otimes y):=(r\cdot x)\otimes y=x\otimes (r\cdot y)$ to the whole $M\otimes _{R}N$ by the previous proposition (strictly speaking, what is needed is a bimodule structure not commutativity; see a paragraph below). Equipped with this *R*-module structure, $M\otimes _{R}N$ satisfies a universal property similar to the above: for any *R*-module *G*, there is a natural isomorphism: ${\begin{cases}\operatorname {Hom} _{R}(M\otimes _{R}N,G)\simeq \{R{\text{-bilinear maps }}M\times N\to G\},\\g\mapsto g\circ \otimes \end{cases}}$

If *R* is not necessarily commutative but if *M* has a left action by a ring *S* (for example, *R*), then $M\otimes _{R}N$ can be given the left *S*-module structure, like above, by the formula $s\cdot (x\otimes y):=(s\cdot x)\otimes y.$

Analogously, if *N* has a right action by a ring *S*, then $M\otimes _{R}N$ becomes a right *S*-module.

### Tensor product of linear maps and a change of base ring

Given linear maps $f:M\to M'$ of right modules over a ring *R* and $g:N\to N'$ of left modules, there is a unique group homomorphism ${\begin{cases}f\otimes g:M\otimes _{R}N\to M'\otimes _{R}N'\\x\otimes y\mapsto f(x)\otimes g(y)\end{cases}}$

The construction has a consequence that tensoring is a functor: each right *R*-module *M* determines the functor $M\otimes _{R}-:R{\text{-Mod}}\longrightarrow {\text{Ab}}$ from the category of left modules to the category of abelian groups that sends *N* to *M* ⊗ *N* and a module homomorphism *f* to the group homomorphism 1 ⊗ *f*.

If $f:R\to S$ is a ring homomorphism and if *M* is a right *S*-module and *N* a left *S*-module, then there is the canonical *surjective* homomorphism: $M\otimes _{R}N\to M\otimes _{S}N$ induced by $M\times N{\overset {\otimes _{S}}{\longrightarrow }}M\otimes _{S}N.$

The resulting map is surjective since pure tensors *x* ⊗ *y* generate the whole module. In particular, taking *R* to be $\mathbb {Z}$ this shows every tensor product of modules is a quotient of a tensor product of abelian groups.

### Several modules

(This section need to be updated. For now, see § Properties for the more general discussion.)

It is possible to extend the definition to a tensor product of any number of modules over the same commutative ring. For example, the universal property of

M

1

⊗

M

2

⊗

M

3

is that each trilinear map on

M

1

×

M

2

×

M

3

→

Z

corresponds to a unique linear map

M

1

⊗

M

2

⊗

M

3

→

Z

.

The binary tensor product is associative: (*M*1 ⊗ *M*2) ⊗ *M*3 is naturally isomorphic to *M*1 ⊗ (*M*2 ⊗ *M*3). The tensor product of three modules defined by the universal property of trilinear maps is isomorphic to both of these iterated tensor products.

## Properties

### Modules over general rings

Let *R*1, *R*2, *R*3, *R* be rings, not necessarily commutative.

- For an *R*1-*R*2-bimodule *M*12 and a left *R*2-module *M*20, $M_{12}\otimes _{R_{2}}M_{20}$ is a left *R*1-module.
- For a right *R*2-module *M*02 and an *R*2-*R*3-bimodule *M*23, $M_{02}\otimes _{R_{2}}M_{23}$ is a right *R*3-module.
- (associativity) For a right *R*1-module *M*01, an *R*1-*R*2-bimodule *M*12, and a left *R*2-module *M*20 we have: $\left(M_{01}\otimes _{R_{1}}M_{12}\right)\otimes _{R_{2}}M_{20}=M_{01}\otimes _{R_{1}}\left(M_{12}\otimes _{R_{2}}M_{20}\right).$
- Since *R* is an *R*-*R*-bimodule, we have $R\otimes _{R}R=R$ with the ring multiplication $mn=:m\otimes _{R}n$ as its canonical balanced product.

### Modules over commutative rings

Let *R* be a commutative ring, and *M*, *N* and *P* be *R*-modules. Then (in the below, "=" denotes canonical isomorphisms; this attitude is permissible since a tensor product is defined only up to unique isomorphisms)

**Identity**

$R\otimes _{R}M=M.$

**Associativity**

$(M\otimes _{R}N)\otimes _{R}P=M\otimes _{R}(N\otimes _{R}P).$

**Symmetry**

$M\otimes _{R}N=N\otimes _{R}M.$

In fact, for any permutation

σ

of the set {1, ...,

n

}, there is a unique isomorphism:

${\begin{cases}M_{1}\otimes _{R}\cdots \otimes _{R}M_{n}\longrightarrow M_{\sigma (1)}\otimes _{R}\cdots \otimes _{R}M_{\sigma (n)}\\x_{1}\otimes \cdots \otimes x_{n}\longmapsto x_{\sigma (1)}\otimes \cdots \otimes x_{\sigma (n)}\end{cases}}$

The first three properties (plus identities on morphisms) say that the category of

R

-modules, with

R

commutative, forms a

symmetric monoidal category

.

**Distribution over direct sums**

$M\otimes _{R}(N\oplus P)=(M\otimes _{R}N)\oplus (M\otimes _{R}P).$

In fact,

$M\otimes _{R}\left(\bigoplus \nolimits _{i\in I}N_{i}\right)=\bigoplus \nolimits _{i\in I}\left(M\otimes _{R}N_{i}\right),$

for an

index set

I

of arbitrary

cardinality

. Since finite products coincide with finite direct sums, this implies:

- Distribution over finite products For any finitely many $N_{i}$ , $M\otimes _{R}\prod _{i=1}^{n}N_{i}=\prod _{i=1}^{n}M\otimes _{R}N_{i}.$

**Base extension**

If

S

is an

R

-algebra, writing

$-_{S}=S\otimes _{R}-$

,

$(M\otimes _{R}N)_{S}=M_{S}\otimes _{S}N_{S};$

cf.

§ Extension of scalars

. A corollary is:

- Distribution over localization For any multiplicatively closed subset *S* of *R*, $S^{-1}(M\otimes _{R}N)=S^{-1}M\otimes _{S^{-1}R}S^{-1}N$ as an $S^{-1}R$ -module, since $S^{-1}R$ is an *R*-algebra and $S^{-1}-=S^{-1}R\otimes _{R}-$ .

**Commutativity with direct limits**

For any direct system of

R

-modules

M

i

,

$(\varinjlim M_{i})\otimes _{R}N=\varinjlim (M_{i}\otimes _{R}N).$

**Adjunction**

$\operatorname {Hom} _{R}(M\otimes _{R}N,P)=\operatorname {Hom} _{R}(M,\operatorname {Hom} _{R}(N,P)){\text{.}}$

A corollary is:

- Right-exactness If $0\to N'{\overset {f}{\to }}N{\overset {g}{\to }}N''\to 0$ is an exact sequence of *R*-modules, then $M\otimes _{R}N'{\overset {1\otimes f}{\to }}M\otimes _{R}N{\overset {1\otimes g}{\to }}M\otimes _{R}N''\to 0$ is an exact sequence of *R*-modules, where $(1\otimes f)(x\otimes y)=x\otimes f(y).$

**Tensor-hom relation**

There is a canonical

R

-linear map:

$\operatorname {Hom} _{R}(M,N)\otimes P\to \operatorname {Hom} _{R}(M,N\otimes P),$

which is an isomorphism if either

M

or

P

is a

finitely generated projective module

(see

§ As linearity-preserving maps

for the non-commutative case);

more generally, there is a canonical

R

-linear map:

$\operatorname {Hom} _{R}(M,N)\otimes \operatorname {Hom} _{R}(M',N')\to \operatorname {Hom} _{R}(M\otimes M',N\otimes N')$

which is an isomorphism if either

$(M,N)$

or

$(M,M')$

is a pair of finitely generated projective modules.

To give a practical example, suppose *M*, *N* are free modules with bases $e_{i},i\in I$ and $f_{j},j\in J$ . Then *M* is the direct sum $M=\bigoplus _{i\in I}Re_{i}$ and the same for *N*. By the distributive property, one has: $M\otimes _{R}N=\bigoplus _{i,j}R(e_{i}\otimes f_{j});$ i.e., $e_{i}\otimes f_{j},\,i\in I,j\in J$ are the *R*-basis of $M\otimes _{R}N$ . Even if *M* is not free, a free presentation of *M* can be used to compute tensor products.

The tensor product, in general, does not commute with inverse limit: on the one hand, $\mathbb {Q} \otimes _{\mathbb {Z} }\mathbb {Z} /p^{n}=0$ (cf. "examples"). On the other hand, $\left(\varprojlim \mathbb {Z} /p^{n}\right)\otimes _{\mathbb {Z} }\mathbb {Q} =\mathbb {Z} _{p}\otimes _{\mathbb {Z} }\mathbb {Q} =\mathbb {Z} _{p}\left[p^{-1}\right]=\mathbb {Q} _{p}$ where $\mathbb {Z} _{p},\mathbb {Q} _{p}$ are the ring of p-adic integers and the field of p-adic numbers. See also "profinite integer" for an example in the similar spirit.

If *R* is not commutative, the order of tensor products could matter in the following way: we "use up" the right action of *M* and the left action of *N* to form the tensor product ⁠ $M\otimes _{R}N$ ⁠; in particular, $N\otimes _{R}M$ would not even be defined. If *M*, *N* are bi-modules, then $M\otimes _{R}N$ has the left action coming from the left action of *M* and the right action coming from the right action of *N*; those actions need not be the same as the left and right actions of ⁠ $N\otimes _{R}M$ ⁠.

The associativity holds more generally for non-commutative rings: if *M* is a right *R*-module, *N* a (*R*, *S*)-module and *P* a left *S*-module, then $(M\otimes _{R}N)\otimes _{S}P=M\otimes _{R}(N\otimes _{S}P)$ as abelian group.

The general form of adjoint relation of tensor products says: if *R* is not necessarily commutative, *M* is a right *R*-module, *N* is a (*R*, *S*)-module, *P* is a right *S*-module, then as abelian group $\operatorname {Hom} _{S}(M\otimes _{R}N,P)=\operatorname {Hom} _{R}(M,\operatorname {Hom} _{S}(N,P)),\,f\mapsto f'$ where $f'$ is given by ⁠ $f'(x)(y)=f(x\otimes y)$ ⁠.

### Tensor product of an *R*-module with the fraction field

Let *R* be an integral domain with fraction field *K*.

- For any *R*-module *M*, $K\otimes _{R}M\cong K\otimes _{R}(M/M_{\operatorname {tor} })$ as *R*-modules, where $M_{\operatorname {tor} }$ is the torsion submodule of *M*.
- If *M* is a torsion *R*-module then $K\otimes _{R}M=0$ and if *M* is not a torsion module then ⁠ $K\otimes _{R}M\neq 0$ ⁠.
- If *N* is a submodule of *M* such that $M/N$ is a torsion module then $K\otimes _{R}N\cong K\otimes _{R}M$ as *R*-modules by ⁠ $x\otimes n\mapsto x\otimes n$ ⁠.
- In ⁠ $K\otimes _{R}M$ ⁠, $x\otimes m=0$ if and only if $x=0$ or ⁠ $m\in M_{\operatorname {tor} }$ ⁠. In particular, $M_{\operatorname {tor} }=\operatorname {ker} (M\to K\otimes _{R}M)$ where ⁠ $m\mapsto 1\otimes m$ ⁠.
- $K\otimes _{R}M\cong M_{(0)}$ where $M_{(0)}$ is the localization of the module M at the prime ideal $(0)$ (i.e., the localization with respect to the nonzero elements).

### Extension of scalars

The adjoint relation in the general form has an important special case: for any *R*-algebra *S*, *M* a right *R*-module, *P* a right *S*-module, using ⁠ $\operatorname {Hom} _{S}(S,-)=-$ ⁠, we have the natural isomorphism: $\operatorname {Hom} _{S}(M\otimes _{R}S,P)=\operatorname {Hom} _{R}(M,\operatorname {Res} _{R}(P)).$

This says that the functor $-\otimes _{R}S$ is a left adjoint to the forgetful functor ⁠ $\operatorname {Res} _{R}$ ⁠, which restricts an *S*-action to an *R*-action. Because of this, $-\otimes _{R}S$ is often called the extension of scalars from *R* to *S*. In representation theory, when *R*, *S* are group algebras, the above relation becomes Frobenius reciprocity.

#### Examples

- ⁠ $R^{n}\otimes _{R}S=S^{n}$ ⁠, for any *R*-algebra *S* (i.e., a free module remains free after extending scalars.)
- For a commutative ring R and a commutative *R*-algebra *S*, we have: $S\otimes _{R}R[x_{1},\dots ,x_{n}]=S[x_{1},\dots ,x_{n}];$ in fact, more generally, $S\otimes _{R}(R[x_{1},\dots ,x_{n}]/I)=S[x_{1},\dots ,x_{n}]/IS[x_{1},\dots ,x_{n}],$ where I is an ideal.
- Using ⁠ $\mathbb {C} =\mathbb {R} [x]/(x^{2}+1)$ ⁠, the previous example and the Chinese remainder theorem, we have as rings $\mathbb {C} \otimes _{\mathbb {R} }\mathbb {C} =\mathbb {C} [x]/(x^{2}+1)=\mathbb {C} [x]/(x+i)\times \mathbb {C} [x]/(x-i)=\mathbb {C} ^{2}.$ This gives an example when a tensor product is a direct product.
- ⁠ $\mathbb {R} \otimes _{\mathbb {Z} }\mathbb {Z} [i]=\mathbb {R} [i]=\mathbb {C}$ ⁠.

## Examples

The structure of a tensor product of quite ordinary modules may be unpredictable.

Let *G* be an abelian group in which every element has finite order (that is *G* is a torsion abelian group; for example *G* can be a finite abelian group or ⁠ $\mathbb {Q} /\mathbb {Z}$ ⁠). Then: $\mathbb {Q} \otimes _{\mathbb {Z} }G=0.$

Indeed, any $x\in \mathbb {Q} \otimes _{\mathbb {Z} }G$ is of the form $x=\sum _{i}r_{i}\otimes g_{i},\qquad r_{i}\in \mathbb {Q} ,g_{i}\in G.$

If $n_{i}$ is the order of ⁠ $g_{i}$ ⁠, then we compute: $x=\sum (r_{i}/n_{i})n_{i}\otimes g_{i}=\sum r_{i}/n_{i}\otimes n_{i}g_{i}=0.$

Similarly, one sees $\mathbb {Q} /\mathbb {Z} \otimes _{\mathbb {Z} }\mathbb {Q} /\mathbb {Z} =0.$

Here are some identities useful for calculation: Let *R* be a commutative ring, *I*, *J* ideals, *M*, *N* *R*-modules. Then

1. ⁠ $R/I\otimes _{R}M=M/IM$ ⁠. If *M* is flat, ⁠ $IM=I\otimes _{R}M$ ⁠.
2. $M/IM\otimes _{R/I}N/IN=M\otimes _{R}N\otimes _{R}R/I$ (because tensoring commutes with base extensions)
3. ⁠ $R/I\otimes _{R}R/J=R/(I+J)$ ⁠.

**Example:** If *G* is an abelian group, ⁠ $G\otimes _{\mathbb {Z} }\mathbb {Z} /n=G/nG$ ⁠; this follows from 1.

**Example:** ⁠ $\mathbb {Z} /n\otimes _{\mathbb {Z} }\mathbb {Z} /m=\mathbb {Z} /{\gcd(n,m)}$ ⁠; this follows from 3. In particular, for distinct prime numbers *p*, *q*, $\mathbb {Z} /p\mathbb {Z} \otimes \mathbb {Z} /q\mathbb {Z} =0.$

Tensor products can be applied to control the order of elements of groups. Let G be an abelian group. Then the multiples of 2 in $G\otimes \mathbb {Z} /2\mathbb {Z}$ are zero.

**Example:** Let $\mu _{n}$ be the group of *n*-th roots of unity. It is a cyclic group and cyclic groups are classified by orders. Thus, non-canonically, $\mu _{n}\approx \mathbb {Z} /n$ and thus, when *g* is the gcd of *n* and *m*, $\mu _{n}\otimes _{\mathbb {Z} }\mu _{m}\approx \mu _{g}.$

**Example:** Consider ⁠ $\mathbb {Q} \otimes _{\mathbb {Z} }\mathbb {Q}$ ⁠. Since $\mathbb {Q} \otimes _{\mathbb {Q} }\mathbb {Q}$ is obtained from $\mathbb {Q} \otimes _{\mathbb {Z} }\mathbb {Q}$ by imposing $\mathbb {Q}$ -linearity on the middle, we have the surjection $\mathbb {Q} \otimes _{\mathbb {Z} }\mathbb {Q} \to \mathbb {Q} \otimes _{\mathbb {Q} }\mathbb {Q}$ whose kernel is generated by elements of the form ${r \over s}x\otimes y-x\otimes {r \over s}y$ where *r*, *s*, *x*, *u* are integers and *s* is nonzero. Since ${r \over s}x\otimes y={r \over s}x\otimes {s \over s}y=x\otimes {r \over s}y,$ the kernel actually vanishes; hence, ⁠ $\mathbb {Q} \otimes _{\mathbb {Z} }\mathbb {Q} =\mathbb {Q} \otimes _{\mathbb {Q} }\mathbb {Q} =\mathbb {Q}$ ⁠.

However, consider $\mathbb {C} \otimes _{\mathbb {R} }\mathbb {C}$ and ⁠ $\mathbb {C} \otimes _{\mathbb {C} }\mathbb {C}$ ⁠. As $\mathbb {R}$ -vector space, $\mathbb {C} \otimes _{\mathbb {R} }\mathbb {C}$ has dimension 4, but $\mathbb {C} \otimes _{\mathbb {C} }\mathbb {C}$ has dimension 2.

Thus, $\mathbb {C} \otimes _{\mathbb {R} }\mathbb {C}$ and $\mathbb {C} \otimes _{\mathbb {C} }\mathbb {C}$ are not isomorphic.

**Example:** We propose to compare $\mathbb {R} \otimes _{\mathbb {Z} }\mathbb {R}$ and ⁠ $\mathbb {R} \otimes _{\mathbb {R} }\mathbb {R}$ ⁠. Like in the previous example, we have: $\mathbb {R} \otimes _{\mathbb {Z} }\mathbb {R} =\mathbb {R} \otimes _{\mathbb {Q} }\mathbb {R}$ as abelian group and thus as ⁠ $\mathbb {Q}$ ⁠-vector space (any $\mathbb {Z}$ -linear map between $\mathbb {Q}$ -vector spaces is $\mathbb {Q}$ -linear). As $\mathbb {Q}$ -vector space, $\mathbb {R}$ has dimension (cardinality of a basis) of continuum. Hence, $\mathbb {R} \otimes _{\mathbb {Q} }\mathbb {R}$ has a $\mathbb {Q}$ -basis indexed by a product of continuums; thus its $\mathbb {Q}$ -dimension is continuum. Hence, for dimension reason, there is a non-canonical isomorphism of $\mathbb {Q}$ -vector spaces: $\mathbb {R} \otimes _{\mathbb {Z} }\mathbb {R} \approx \mathbb {R} \otimes _{\mathbb {R} }\mathbb {R} .$

Consider the modules $M=\mathbb {C} [x,y,z]/(f),N=\mathbb {C} [x,y,z]/(g)$ for $f,g\in \mathbb {C} [x,y,z]$ irreducible polynomials such that ⁠ $\gcd(f,g)=1$ ⁠. Then, ${\frac {\mathbb {C} [x,y,z]}{(f)}}\otimes _{\mathbb {C} [x,y,z]}{\frac {\mathbb {C} [x,y,z]}{(g)}}\cong {\frac {\mathbb {C} [x,y,z]}{(f,g)}}$

Another useful family of examples comes from changing the scalars. Notice that ${\frac {\mathbb {Z} [x_{1},\ldots ,x_{n}]}{(f_{1},\ldots ,f_{k})}}\otimes _{\mathbb {Z} }R\cong {\frac {R[x_{1},\ldots ,x_{n}]}{(f_{1},\ldots ,f_{k})}}$

Good examples of this phenomenon to look at are when ⁠ $R=\mathbb {Q} ,\mathbb {C} ,\mathbb {Z} /(p^{k}),\mathbb {Z} _{p},\mathbb {Q} _{p}$ ⁠.

## Construction

The construction of *M* ⊗ *N* takes a quotient of a free abelian group with basis the symbols *m* ∗ *n*, used here to denote the ordered pair (*m*, *n*), for *m* in *M* and *n* in *N* by the subgroup generated by all elements of the form

1. −*m* ∗ (*n* + *n*′) + *m* ∗ *n* + *m* ∗ *n*′
2. −(*m* + *m*′) ∗ *n* + *m* ∗ *n* + *m*′ ∗ *n*
3. (*m* · *r*) ∗ *n* − *m* ∗ (*r* · *n*)

where *m*, *m*′ in *M*, *n*, *n*′ in *N*, and *r* in *R*. The quotient map which takes *m* ∗ *n* = (*m*, *n*) to the coset containing *m* ∗ *n*; that is, $\otimes :M\times N\to M\otimes _{R}N,\,(m,n)\mapsto [m*n]$ is balanced, and the subgroup has been chosen minimally so that this map is balanced. The universal property of ⊗ follows from the universal properties of a free abelian group and a quotient.

If *S* is a subring of a ring *R*, then $M\otimes _{R}N$ is the quotient group of $M\otimes _{S}N$ by the subgroup generated by $xr\otimes _{S}y-x\otimes _{S}ry,\,r\in R,x\in M,y\in N$ , where $x\otimes _{S}y$ is the image of $(x,y)$ under ⁠ $\otimes :M\times N\to M\otimes _{S}N$ ⁠. In particular, any tensor product of *R*-modules can be constructed, if so desired, as a quotient of a tensor product of abelian groups by imposing the *R*-balanced product property.

More category-theoretically, let σ be the given right action of *R* on *M*; i.e., σ(*m*, *r*) = *m* · *r* and τ the left action of *R* of *N*. Then, provided the tensor product of abelian groups is already defined, the tensor product of *M* and *N* over *R* can be defined as the coequalizer: $M\otimes R\otimes N{{{} \atop {\overset {\sigma \times 1}{\to }}} \atop {{\underset {1\times \tau }{\to }} \atop {}}}M\otimes N\to M\otimes _{R}N$ where $\otimes$ without a subscript refers to the tensor product of abelian groups.

In the construction of the tensor product over a commutative ring *R*, the *R*-module structure can be built in from the start by forming the quotient of a free *R*-module by the submodule generated by the elements given above for the general construction, augmented by the elements *r* ⋅ (*m* ∗ *n*) − *m* ∗ (*r* ⋅ *n*). Alternately, the general construction can be given a Z(*R*)-module structure by defining the scalar action by *r* ⋅ (*m* ⊗ *n*) = *m* ⊗ (*r* ⋅ *n*) when this is well-defined, which is precisely when *r* ∈ Z(*R*), the centre of *R*.

The direct product of *M* and *N* is rarely isomorphic to the tensor product of *M* and *N*. When *R* is not commutative, then the tensor product requires that *M* and *N* be modules on opposite sides, while the direct product requires they be modules on the same side. In all cases the only function from *M* × *N* to *G* that is both linear and bilinear is the zero map.

## As linear maps

In the general case, not all the properties of a tensor product of vector spaces extend to modules. Yet, some useful properties of the tensor product, considered as module homomorphisms, remain.

### Dual module

The **dual module** of a right *R*-module *E*, is defined as Hom*R*(*E*, *R*) with the canonical left *R*-module structure, and is denoted *E*∗. The canonical structure is the pointwise operations of addition and scalar multiplication. Thus, *E*∗ is the set of all *R*-linear maps *E* → *R* (also called *linear forms*), with operations $(\phi +\psi )(u)=\phi (u)+\psi (u),\quad \phi ,\psi \in E^{*},u\in E$ $(r\cdot \phi )(u)=r\cdot \phi (u),\quad \phi \in E^{*},u\in E,r\in R,$ The dual of a left *R*-module is defined analogously, with the same notation.

There is always a canonical homomorphism *E* → *E*∗∗ from *E* to its second dual. It is an isomorphism if *E* is a free module of finite rank. In general, *E* is called a reflexive module if the canonical homomorphism is an isomorphism.

### Duality pairing

We denote the natural pairing of its dual *E*∗ and a right *R*-module *E*, or of a left *R*-module *F* and its dual *F*∗ as $\langle \cdot ,\cdot \rangle :E^{*}\times E\to R:(e',e)\mapsto \langle e',e\rangle =e'(e)$ $\langle \cdot ,\cdot \rangle :F\times F^{*}\to R:(f,f')\mapsto \langle f,f'\rangle =f'(f).$ The pairing is left *R*-linear in its left argument, and right *R*-linear in its right argument: $\langle r\cdot g,h\cdot s\rangle =r\cdot \langle g,h\rangle \cdot s,\quad r,s\in R.$

### An element as a (bi)linear map

In the general case, each element of the tensor product of modules gives rise to a left *R*-linear map, to a right *R*-linear map, and to an *R*-bilinear form. Unlike in the commutative case, in the general case the tensor product is not an *R*-module, and thus does not support scalar multiplication.

- Given a right *R*-module *E* and a right *R*-module *F*, there is a canonical homomorphism *θ* : *F* ⊗*R* *E*∗ → Hom*R*(*E*, *F*) such that *θ*(*f* ⊗ *e*′) is the map *e* ↦ *f* ⋅ ⟨*e*′, *e*⟩.
- Given a left *R*-module *E* and a right *R*-module *F*, there is a canonical homomorphism *θ* : *F* ⊗*R* *E* → Hom*R*(*E*∗, *F*) such that *θ*(*f* ⊗ *e*) is the map *e*′ ↦ *f* ⋅ ⟨*e*, *e*′⟩.

Both cases hold for general modules, and the homomorphisms are isomorphisms if the modules *E* and *F* are finitely generated projective modules (in particular, free modules of finite ranks). Thus, an element of the tensor product of modules over a ring *R* maps canonically onto an *R*-linear map, though as with vector spaces, constraints apply to the modules for this to be equivalent to the full space of such linear maps.

- Given a right *R*-module *E* and left *R*-module *F*, there is a canonical homomorphism *θ* : *F*∗ ⊗*R* *E*∗ → L*R*(*F* × *E*, *R*) such that *θ*(*f*′ ⊗ *e*′) is the map (*f*, *e*) ↦ ⟨*f*, *f*′⟩ ⋅ ⟨*e*′, *e*⟩. Thus, an element *ξ* of the tensor product *F*∗ ⊗*R* *E*∗ of *R*-modules may be thought of as giving rise to an *R*-bilinear map *F* × *E* → *R*.

### Trace

Let *R* be a commutative ring and *E* an *R*-module. Then there is a canonical *R*-linear map: $E^{*}\otimes _{R}E\to R$ induced through linearity by ⁠ $\phi \otimes x\mapsto \phi (x)$ ⁠; it is the unique *R*-linear map corresponding to the natural pairing.

If *E* is a finitely generated projective *R*-module, then one can identify $E^{*}\otimes _{R}E=\operatorname {End} _{R}(E)$ through the canonical homomorphism mentioned above and then the above is the **trace map**: $\operatorname {tr} :\operatorname {End} _{R}(E)\to R.$

When *R* is a field, this is the usual trace of a linear transformation.

## Example from differential geometry: tensor field

The most prominent example of a tensor product of modules in differential geometry is the tensor product of the spaces of vector fields and differential forms. More precisely, if *R* is the (commutative) ring of smooth functions on a smooth manifold *M*, then one puts ${\mathfrak {T}}_{q}^{p}=\Gamma (M,TM)^{\otimes p}\otimes _{R}\Gamma (M,T^{*}M)^{\otimes q}$ where Γ means the space of sections and the superscript $\otimes p$ means tensoring *p* times over *R*. By definition, an element of ${\mathfrak {T}}_{q}^{p}$ is a tensor field of type (*p*, *q*).

As *R*-modules, ${\mathfrak {T}}_{p}^{q}$ is the dual module of ⁠ ${\mathfrak {T}}_{q}^{p}$ ⁠.

To lighten the notation, put $E=\Gamma (M,TM)$ and so ⁠ $E^{*}=\Gamma (M,T^{*}M)$ ⁠. When *p*, *q* ≥ 1, for each (*k*, *l*) with 1 ≤ *k* ≤ *p*, 1 ≤ *l* ≤ *q*, there is an *R*-multilinear map: $E^{p}\times {E^{*}}^{q}\to {\mathfrak {T}}_{q-1}^{p-1},\,(X_{1},\dots ,X_{p},\omega _{1},\dots ,\omega _{q})\mapsto \langle X_{k},\omega _{l}\rangle X_{1}\otimes \cdots \otimes {\widehat {X_{l}}}\otimes \cdots \otimes X_{p}\otimes \omega _{1}\otimes \cdots {\widehat {\omega _{l}}}\otimes \cdots \otimes \omega _{q}$ where $E^{p}$ means $\prod _{1}^{p}E$ and the hat means a term is omitted. By the universal property, it corresponds to a unique *R*-linear map: $C_{l}^{k}:{\mathfrak {T}}_{q}^{p}\to {\mathfrak {T}}_{q-1}^{p-1}.$

It is called the contraction of tensors in the index (*k*, *l*). Unwinding what the universal property says one sees: $C_{l}^{k}(X_{1}\otimes \cdots \otimes X_{p}\otimes \omega _{1}\otimes \cdots \otimes \omega _{q})=\langle X_{k},\omega _{l}\rangle X_{1}\otimes \cdots {\widehat {X_{l}}}\cdots \otimes X_{p}\otimes \omega _{1}\otimes \cdots {\widehat {\omega _{l}}}\cdots \otimes \omega _{q}.$

**Remark**: The preceding discussion is standard in textbooks on differential geometry (e.g., Helgason). In a way, the sheaf-theoretic construction (i.e., the language of sheaf of modules) is more natural and increasingly more common; for that, see the section § Tensor product of sheaves of modules.

## Relationship to flat modules

In general, $-\otimes _{R}-:{\text{Mod-}}R\times R{\text{-Mod}}\longrightarrow \mathrm {Ab}$ is a bifunctor which accepts a right and a left *R* module pair as input, and assigns them to the tensor product in the category of abelian groups.

By fixing a right *R* module *M*, a functor $M\otimes _{R}-:R{\text{-Mod}}\longrightarrow \mathrm {Ab}$ arises, and symmetrically a left *R* module *N* could be fixed to create a functor $-\otimes _{R}N:{\text{Mod-}}R\longrightarrow \mathrm {Ab} .$

Unlike the Hom bifunctor $\mathrm {Hom} _{R}(-,-),$ the tensor functor is covariant in both inputs.

It can be shown that $M\otimes _{R}-$ and $-\otimes _{R}N$ are always right exact functors, but not necessarily left exact (⁠ $0\to \mathbb {Z} \to \mathbb {Z} \to \mathbb {Z} _{n}\to 0$ ⁠, where the first map is multiplication by ⁠ n ⁠, is exact but not after taking the tensor with $\mathbb {Z} _{n}$ ). By definition, a module *T* is a flat module if $T\otimes _{R}-$ is an exact functor.

If $\{m_{i}\mid i\in I\}$ and $\{n_{j}\mid j\in J\}$ are generating sets for *M* and *N*, respectively, then $\{m_{i}\otimes n_{j}\mid i\in I,j\in J\}$ will be a generating set for $M\otimes _{R}N.$ Because the tensor functor $M\otimes _{R}-$ sometimes fails to be left exact, this may not be a minimal generating set, even if the original generating sets are minimal. If *M* is a flat module, the functor $M\otimes _{R}-$ is exact by the very definition of a flat module. If the tensor products are taken over a field *F*, we are in the case of vector spaces as above. Since all *F* modules are flat, the bifunctor $-\otimes _{R}-$ is exact in both positions, and the two given generating sets are bases, then $\{m_{i}\otimes n_{j}\mid i\in I,j\in J\}$ indeed forms a basis for ⁠ $M\otimes _{F}N$ ⁠.

## Additional structure

If *S* and *T* are commutative *R*-algebras, then, similar to #For equivalent modules, *S* ⊗*R* *T* will be a commutative *R*-algebra as well, with the multiplication map defined by (*m*1 ⊗ *m*2) (*n*1 ⊗ *n*2) = (*m*1*n*1 ⊗ *m*2*n*2) and extended by linearity. In this setting, the tensor product become a fibered coproduct in the category of commutative *R*-algebras. (But it is not a coproduct in the category of *R*-algebras.)

If *M* and *N* are both *R*-modules over a commutative ring, then their tensor product is again an *R*-module. If *R* is a ring, *R**M* is a left *R*-module, and the commutator

rs

−

sr

of any two elements *r* and *s* of *R* is in the annihilator of *M*, then we can make *M* into a right *R* module by setting

mr

=

rm

.

The action of *R* on *M* factors through an action of a quotient commutative ring. In this case the tensor product of *M* with itself over *R* is again an *R*-module. This is a very common technique in commutative algebra.

## Generalization

### Tensor product of complexes of modules

If *X*, *Y* are complexes of *R*-modules (*R* a commutative ring), then their tensor product is the complex given by $(X\otimes _{R}Y)_{n}=\sum _{i+j=n}X_{i}\otimes _{R}Y_{j},$ with the differential given by: for *x* in *X**i* and *y* in *Y**j*, $d_{X\otimes Y}(x\otimes y)=d_{X}(x)\otimes y+(-1)^{i}x\otimes d_{Y}(y).$

For example, if *C* is a chain complex of flat abelian groups and if *G* is an abelian group, then the homology group of $C\otimes _{\mathbb {Z} }G$ is the homology group of *C* with coefficients in *G* (see also: universal coefficient theorem).

### Tensor product of sheaves of modules

The tensor product of sheaves of modules is the sheaf associated to the pre-sheaf of the tensor products of the modules of sections over open subsets.

In this setup, for example, one can define a tensor field on a smooth manifold *M* as a (global or local) section of the tensor product (called **tensor bundle**) $(TM)^{\otimes p}\otimes _{O}(T^{*}M)^{\otimes q}$ where *O* is the sheaf of rings of smooth functions on *M* and the bundles $TM,T^{*}M$ are viewed as locally free sheaves on *M*.

The **exterior bundle** on *M* is the subbundle of the tensor bundle consisting of all antisymmetric covariant tensors. Sections of the exterior bundle are differential forms on *M*.

One important case when one forms a tensor product over a sheaf of non-commutative rings appears in theory of *D*-modules; that is, tensor products over the sheaf of differential operators.
