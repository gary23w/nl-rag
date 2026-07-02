---
title: "Kleisli category"
source: https://en.wikipedia.org/wiki/Kleisli_category
domain: monad-transformers
license: CC-BY-SA-4.0
tags: monad transformer, monad stack, kleisli category, free monad
fetched: 2026-07-02
---

# Kleisli category

In category theory, a **Kleisli category** is a category naturally associated to any monad *T*. It is equivalent to the category of free *T*-algebras. The Kleisli category is one of two extremal solutions to the question: "*Does every monad arise from an adjunction?*" The other extremal solution is the Eilenberg–Moore category. Kleisli categories are named for the mathematician Heinrich Kleisli.

## Formal definition

Let ⟨*T*, *η*, *μ*⟩ be a monad over a category *C*. The **Kleisli category** of *C* is the category *C**T* whose objects and morphisms are given by

${\begin{aligned}\mathrm {Obj} ({{\mathcal {C}}_{T}})&=\mathrm {Obj} ({\mathcal {C}}),\\\mathrm {Hom} _{{\mathcal {C}}_{T}}(X,Y)&=\mathrm {Hom} _{\mathcal {C}}(X,TY).\end{aligned}}$

That is, every morphism *f: X → T Y* in *C* (with codomain *TY*) can also be regarded as a morphism in *C**T* (but with codomain *Y*). Composition of morphisms in *C**T* is given by

$g\circ _{T}f=\mu _{Z}\circ Tg\circ f:X\to TY\to T^{2}Z\to TZ$

where *f: X → T Y* and *g: Y → T Z*. The identity morphism is given by the monad unit *η*:

$\mathrm {id} _{X}=\eta _{X}$

.

An alternative way of writing this, which clarifies the category in which each object lives, is used by MacLane. We use very slightly different notation for this presentation. Given the same monad and category C as above, we associate with each object X in  C a new object $X_{T}$ , and for each morphism $f\colon X\to TY$ in  C a morphism $f^{*}\colon X_{T}\to Y_{T}$ . Together, these objects and morphisms form our category $C_{T}$ , where we define composition, also called **Kleisli composition**, by

$g^{*}\circ _{T}f^{*}=(\mu _{Z}\circ Tg\circ f)^{*}.$

Then the identity morphism in $C_{T}$ , the **Kleisli identity**, is

$\mathrm {id} _{X_{T}}=(\eta _{X})^{*}.$

## Extension operators and Kleisli triples

Composition of Kleisli arrows can be expressed succinctly by means of the *extension operator* (–)# : Hom(*X*, *TY*) → Hom(*TX*, *TY*). Given a monad ⟨*T*, *η*, *μ*⟩ over a category *C* and a morphism *f* : *X* → *TY* let

$f^{\sharp }=\mu _{Y}\circ Tf.$

Composition in the Kleisli category *C**T* can then be written

$g\circ _{T}f=g^{\sharp }\circ f.$

The extension operator satisfies the identities:

${\begin{aligned}\eta _{X}^{\sharp }&=\mathrm {id} _{TX}\\f^{\sharp }\circ \eta _{X}&=f\\(g^{\sharp }\circ f)^{\sharp }&=g^{\sharp }\circ f^{\sharp }\end{aligned}}$

where *f* : *X* → *TY* and *g* : *Y* → *TZ*. It follows trivially from these properties that Kleisli composition is associative and that *η**X* is the identity.

In fact, to give a monad is to give a *Kleisli triple* ⟨*T*, *η*, (–)#⟩, i.e.

- A function $T\colon \mathrm {ob} (C)\to \mathrm {ob} (C)$ ;
- For each object A in C , a morphism $\eta _{A}\colon A\to T(A)$ ;
- For each morphism $f\colon A\to T(B)$ in C , a morphism $f^{\sharp }\colon T(A)\to T(B)$

such that the above three equations for extension operators are satisfied.

## Kleisli adjunction

Kleisli categories were originally defined in order to show that every monad arises from an adjunction. That construction is as follows.

Let ⟨*T*, *η*, *μ*⟩ be a monad over a category *C* and let *C**T* be the associated Kleisli category. Using Mac Lane's notation mentioned in the “Formal definition” section above, define a functor *F*: *C* → *C**T* by

$FX=X_{T}\;$

$F(f\colon X\to Y)=(\eta _{Y}\circ f)^{*}$

and a functor *G* : *C**T* → *C* by

$GY_{T}=TY\;$

$G(f^{*}\colon X_{T}\to Y_{T})=\mu _{Y}\circ Tf\;$

One can show that *F* and *G* are indeed functors and that *F* is left adjoint to *G*. The counit of the adjunction is given by

$\varepsilon _{Y_{T}}=(\mathrm {id} _{TY})^{*}:(TY)_{T}\to Y_{T}.$

Finally, one can show that *T* = *GF* and *μ* = *GεF* so that ⟨*T*, *η*, *μ*⟩ is the monad associated to the adjunction ⟨*F*, *G*, *η*, *ε*⟩.

### Showing that *GF* = *T*

For any object *X* in category *C*:

${\begin{aligned}(G\circ F)(X)&=G(F(X))\\&=G(X_{T})\\&=TX.\end{aligned}}$

For any $f:X\to Y$ in category *C*:

${\begin{aligned}(G\circ F)(f)&=G(F(f))\\&=G((\eta _{Y}\circ f)^{*})\\&=\mu _{Y}\circ T(\eta _{Y}\circ f)\\&=\mu _{Y}\circ T\eta _{Y}\circ Tf\\&={\text{id}}_{TY}\circ Tf\\&=Tf.\end{aligned}}$

Since $(G\circ F)(X)=TX$ is true for any object *X* in *C* and $(G\circ F)(f)=Tf$ is true for any morphism *f* in *C*, then $G\circ F=T$ . Q.E.D.
