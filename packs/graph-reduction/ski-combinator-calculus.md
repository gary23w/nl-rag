---
title: "SKI combinator calculus"
source: https://en.wikipedia.org/wiki/SKI_combinator_calculus
domain: graph-reduction
license: CC-BY-SA-4.0
tags: graph reduction, combinator graph reduction, spineless tagless G-machine, supercombinator compilation
fetched: 2026-07-02
---

# SKI combinator calculus

The **SKI combinator calculus** is a combinatory logic system and a computational system. It can be thought of as a computer programming language, though it is not convenient for writing software. Instead, it is important in the mathematical theory of algorithms because it is an extremely simple Turing complete language. It can be likened to a reduced version of the untyped lambda calculus. It was introduced by Moses Schönfinkel and Haskell Curry.

All operations in lambda calculus can be encoded via abstraction elimination into the SKI calculus as binary trees whose leaves are one of the three symbols **S**, **K**, and **I** (called *combinators*).

**I** itself is redundant and can be expressed with **S** and **K** only, e.g. as **SKK**, but its use often makes the definitions shorter and easier to grasp.

## Notation

Although the most formal representation of the objects in this system requires binary trees, for simpler typesetting they are often represented as parenthesized expressions, as a shorthand for the tree they represent. Any subtrees may be parenthesized, but often only the right-side subtrees are parenthesized, with left associativity implied for any unparenthesized applications. For example, **ISK** means ((**IS**)**K**). Using this notation, a tree whose left subtree is the tree **KS** and whose right subtree is the tree **SK** can be written as **KS**(**SK**). If more explicitness is desired, the implied parentheses can be included as well: ((**KS**)(**SK**)).

## Informal description

Informally, and using programming language jargon, a tree (*xy*) can be thought of as an application of the function *x* to an argument *y*. When evaluated (*i.e.*, when the "function" is "applied" to the argument), the tree "returns a value", *i.e.*, transforms into another tree. The "function", "argument" and the "value" are either combinators or binary trees with application nodes. If they are binary trees, they may be thought of as functions too, if needed.

The **evaluation** operation is defined as follows:

(*x*, *y*, and *z* represent expressions made from the combinators **S**, **K**, and **I**, and possibly variables standing for some as yet unspecified **SKI** expressions):

**I** returns its argument:

I

x

=

x

**K**, when applied to any argument *x*, yields a one-argument constant function **K***x*, which, when applied to any argument *y*, returns *x*:

K

xy

=

x

**S** is a substitution operator. It takes three arguments and then returns the first argument applied to the third, which is then applied to the result of the second argument applied to the third. More clearly:

S

xyz

=

xz

(

yz

)

Example computation: **SKSK** evaluates to **KK**(**SK**) by the **S**-rule. Then if we evaluate **KK**(**SK**), we get **K** by the **K**-rule. As no further rule can be applied, the computation halts here.

For all trees *x* and all trees *y*, **SK***xy* will always evaluate to *y* in two steps, **K***y*(*xy*) = *y*, so the ultimate result of evaluating **SK***xy* will always be the same as the result of evaluating *y*. We say that **SK***x* and **I** are "functionally equivalent" for any *x*, because they always yield the same result when applied to any *y*.

From these definitions it can be shown that SKI calculus, while being a minimalistic system, can fully perform any computations of the lambda calculus. All occurrences of **I** in any expression can be replaced by (**SKK**) or (**SKS**) or (**SK** *x*) for any *x*, and the resulting expression will yield the same result. So the "**I**" is merely syntactic sugar. Since **I** is optional, the system is also referred to as **SK calculus** or **SK combinator calculus**.

It is possible to define a complete system using only one (improper) combinator. An example is Chris Barker's iota combinator, which can be expressed in terms of **S** and **K** as follows:

ι

x

=

x

SK

=

S

(λ

x

.

x

S

)(λ

x

.

K

)

x

=

S

(

S

(λ

x

.

x

)(λ

x

.

S

))(

KK

)

x

=

S

(

SI

(

KS

))(

KK

)

x

It is possible to reconstruct **S**, **K**, and **I** from the iota combinator. Applying ι to itself gives ιι = ι**SK** = **SSKK** = **SK**(**KK**) which is functionally equivalent to **I**. **K** can be constructed by applying ι twice to **I** (which is equivalent to application of ι to itself): ι(ι(ιι)) = ι(ιι**SK**) = ι(**ISK**) = ι(**SK**) = **SKSK** = **K**. Applying ι one more time gives ι(ι(ι(ιι))) = ι**K** = **KSK** = **S**.

The simplest possible term forming a basis is X = λ*f*.*f* (λ*xyz*.*x* *z* (*y* *z*)) (λ*xyz*.*x*), which satisfies X X = **K**, and X (X X) = **S**.

## Formal definition

The terms and derivations in this system can also be more formally defined:

**Terms**: The set *T* of terms is defined recursively by the following rules.

1. **S**, **K**, and **I** are terms.
2. If *τ*1 and *τ*2 are terms, then (*τ*1*τ*2) is a term.
3. Nothing is a term if not required to be so by the first two rules.

**Derivations**: A derivation is a finite sequence of terms defined recursively by the following rules (where *α* and *ι* are words over the alphabet {**S**, **K**, **I**, (, )} while *β*, *γ* and *δ* are terms):

1. If Δ is a derivation ending in an expression of the form *α*(**I**β)*ι*, then Δ followed by the term *αβι* is a derivation.
2. If Δ is a derivation ending in an expression of the form *α*((**K**β)*γ*)*ι*, then Δ followed by the term *αβι* is a derivation.
3. If Δ is a derivation ending in an expression of the form *α*(((**S**β)*γ*)*δ*)*ι*, then Δ followed by the term *α*((*βδ*)(*γδ*))*ι* is a derivation.

Assuming a sequence is a valid derivation to begin with, it can be extended using these rules. All derivations of length 1 are valid derivations.

## Conversion of lambda terms to SKI combinators

An expression in the lambda calculus can be converted into an SKI combinator calculus expression in accordance with the following rules:

1. λ*x*. *x* = **I**
2. λ*x*. c = **K**c (provided that c does not depend on *x*)
3. λ*x*. c *x* = c (provided that c does not depend on *x*)
4. λ*x*. *y* *z* = **S**(λ*x*.*y*)(λ*x*.*z*)

## SKI expressions

### Self-application and recursion

**SII** is an expression that takes an argument and applies that argument to itself:

SII

α

=

I

α

(

I

α

) =

αα

This is also known as **U** combinator, **U***x* = *xx*. One interesting property of it is that its self-application is irreducible:

SII

(

SII

) =

I

(

SII

)(

I

(

SII

)) =

SII

(

I

(

SII

)) =

SII

(

SII

)

Or, using the equation **U***x* = *xx* as its definition directly, we immediately get **U** **U** = **U** **U**.

Another thing is that it allows one to write a function that applies one thing to the self application of another thing:

(

S

(

K

α

)(

SII

))

β

=

K

αβ

(

SII

β

) =

α

(

I

β(

I

β

)) =

α

(

ββ

)

or it can be seen as defining yet another combinator directly, **H***xy* = *x*(*yy*).

This function can be used to achieve recursion. If *β* is the function that applies *α* to the self application of something else,

β

=

H

α

=

S

(

K

α

)(

SII

)

then the self-application of this *β* is the fixed point of that *α*:

SII

β

=

ββ

=

α

(

ββ

) =

α

(

α

(

ββ

)) =

$\ldots$

Or, directly again from the derived definition, **H***α*(**H***α*) = *α*(**H***α*(**H***α*)).

If *α* expresses a "computational step" computed by *αρν* for some *ρ* and *ν*, that assumes *ρν′* expresses "the rest of the computation" (for some *ν′* that *α* will "compute" from *ν*), then its fixed point *ββ* expresses the whole recursive computation, since using *the same function* *ββ* for the "rest of computation" call (with *ββν* = *α*(*ββ*)*ν*) is the very definition of recursion: *ρν′ = ββν′ = α(ββ)ν′ = ...* . The term *α* will have to employ some kind of conditional to stop at some "base case" and not make the recursive call then, to avoid divergence.

This can be formalized, with

β

=

H

α

=

S

(

K

α

)(

SII

) =

S

(

KS

)

K

α

(

SII

) =

S

(

S

(

KS

)

K

)(

K

(

SII

))

α

as

Y

α

=

SII

β

=

SII

(

H

α

) =

S

(

K

(

SII

))

H

α

=

S

(

K

(

SII

))(

S

(

S

(

KS

)

K

)(

K

(

SII

)))

α

which gives us one possible encoding of the **Y** combinator. A shorter variation replaces its two leading subterms with just **SSI**, since **H**α(**H**α) = **SHH**α = **SSIH**α.

This becomes much shorter with the additional use of the **B,C,W** combinators, as the equivalent

Y

α =

S

(

KU

)(

SB

(

KU

))α =

U

(

B

α

U

) =

BU

(

CBU

)α =

SSI

(

CBU

)α

And with a pseudo-Haskell syntax it becomes the exceptionally short **Y** = **U** . (. **U**).

Following this approach, other fixpoint combinator definitions are possible. Thus,

- This **Y**, by Haskell Curry:

H

gx

=

g

(

xx

)

;

Y

g

=

H

g

(

H

g

)

;

Y = S(KU)(SB(KU)) = SS(S(S(KS)K))(K(SII))

- Turing's **Θ**:

H

hg

=

g

(

hhg

)

;

Θ

g

=

HH

g

;

Θ = U(B(SI)U) = SII(S(K(SI))(SII))

- **Y′** (with SK-encoding by John Tromp):

H

gh

=

g

(

hgh

)

;

Y′

g

=

H

g

H

;

Y′ = WC(SB(C(WC))) = SSK(S(K(SS(S(SSK))))K)

- **Θ4** by R. Statman:

H

gyz

=

g

(

yyz

)

;

Θ

4

g

=

H

g

(

H

g

)(

H

g

)

;

Θ

4

= B(WW)(BW(BBB))

- or in general,

H

something

=

g

(

hsomething

)

;

Y

H

g

=

H

_____

H

__

g

(where anything goes instead of "_") or any other intermediary

H

combinator's definition, with its corresponding

Y

H

definition to jump-start it correctly. In particular, one construction, due to Jan Klop,

is

L

abcdefghijklmnopqstuvwxyzr

=

r

(

thisisafixedpointcombinator

)

;

Y

K

=

LLLLLLLLLLLLLLLLLLLLLLLLLL

In a strict programming language the Y combinator will expand until stack overflow, or never halt in case of tail call optimization. The **Z** combinator will work in strict languages (also called eager languages), where the applicative evaluation order is in effect.

Its difference from the **Y** combinator is that it is using $Qx=B(Ux)I=S(K(Ux))I=S(BS(BKU))(KI)x$ as the $\eta$ -expanded form of **Y'**s plain $Ux$ . Whereas **Y** = **BU**(**CBU**), we have **Z** = **BU**(**CBQ**) = **S**(**KU**)(**SB**(**KQ**)):

${\begin{aligned}\\Z&=\lambda f.(\lambda x.f(\lambda v.xxv))(\lambda x.f(\lambda v.xxv))\\&=\lambda f.U(\lambda x.f(\lambda v.Uxv))\\&=S(\lambda f.U)(\lambda f.\lambda x.f(\lambda v.Uxv))\\&=S(KU)(\lambda f.S(\lambda x.f)(\lambda x.\lambda v.Uxv))\\&=S(KU)(\lambda f.S(Kf)(\lambda x.\lambda v.Uxv))\\&=S(KU)(S(\lambda f.S(Kf))(\lambda f.\lambda x.\lambda v.Uxv))\\&=S(KU)(S(S(\lambda f.S)(\lambda f.Kf))(K(\lambda x.\lambda v.Uxv)))\\&=S(KU)(S(S(KS)K)(K(\lambda x.\lambda v.Uxv)))\\&=S(KU)(S(S(KS)K)(K(\lambda x.S({\color {Red}\lambda v.Ux})(\lambda v.v))))\\&=S(KU)(S(S(KS)K)(K(\lambda x.S(K(Ux))I)))\\&=S(KU)(S(S(KS)K)(K(S(\lambda x.S(K(Ux)))(\lambda x.I))))\\&=S(KU)(S(S(KS)K)(K(S(\lambda x.S(K(Ux)))(KI))))\\&=S(KU)(S(S(KS)K)(K(S(S(\lambda x.S)(\lambda x.K(Ux)))(KI))))\\&=S(KU)(S(S(KS)K)(K(S(S(KS)(S(\lambda x.K)(\lambda x.Ux)))(KI))))\\&=S(KU)(S(S(KS)K)(K(S(S(KS)(S(KK)U))(KI))))\\\end{aligned}}$

### The reversal expression

**S**(**K**(**SI**))**K** reverses the two terms following it:

S

(

K

(

SI

))

K

αβ →

K

(

SI

)α(

K

α)β →

SI

(

K

α)β →

I

β(

K

αβ) →

I

βα →

βα

It is thus equivalent to **CI**. And in general, **S**(**K**(**S***f*))**K** is equivalent to **C***f*, for any *f*.

### Boolean logic

SKI combinator calculus can also implement Boolean logic in the form of an *if-then-else* structure. An *if-then-else* structure consists of a Boolean expression that is either true (**T**) or false (**F**) and two arguments, such that:

T

xy

=

x

and

F

xy

=

y

The key is in defining the two Boolean expressions. The first works just like one of our basic combinators:

T

=

K

K

xy

=

x

The second is also fairly simple:

F

=

SK

SK

xy

=

K

y

(

xy

) =

y

Once true and false are defined, all Boolean logic can be implemented in terms of Booleans acting as *if-then-else* structures.

Boolean **NOT** (which returns the opposite of a given Boolean) works the same as the *if-then-else* structure, with **F** and **T** as the second and third values:

NOT

b

=

b

FT

=

S

(

SI

(

KF

))(

KT

)

b

If this is put in an *if-then-else* structure, it has the expected result:

NOT

(

T

) = (

T

)

FT

=

F

NOT

(

F

) = (

F

)

FT

=

T

Boolean **OR** (which returns **T** if either of its two Boolean argument values is **T**) works the same as an *if-then-else* structure with **T** as the second value:

OR

ab

=

a

T

b

=

SI

(

KT

)

ab

If this is put in an *if-then-else* structure, it has the expected result:

OR

(

T

)(

T

) = (

T

)

T

(

T

) =

T

OR

(

T

)(

F

) = (

T

)

T

(

F

) =

T

OR

(

F

)(

T

) = (

F

)

T

(

T

) =

T

OR

(

F

)(

F

) = (

F

)

T

(

F

) =

F

Boolean **AND** (which returns **T** if both its Boolean argument values are **T**) works the same as an *if-then-else* structure with **F** as the third value:

AND

ab

=

ab

F

=

S

a

(

KF

)

b

=

SS

(

K

(

KF

))

ab

If this is put in an *if-then-else* structure, it has the expected result:

AND

(

T

)(

T

) = (

T

)(

T

)

F

=

T

AND

(

T

)(

F

) = (

T

)(

F

)

F

=

F

AND

(

F

)(

T

) = (

F

)(

T

)

F

=

F

AND

(

F

)(

F

) = (

F

)(

F

)

F

=

F

This proves that the SKI system can fully express Boolean logic.

SKI calculus is complete, so any other logical combinator can be expressed in it as well, like, e.g.,

XOR

ab

=

OR

(

AND

a

(

NOT

b

)) (

AND

(

NOT

a

)

b

)

so that

XOR

abxy

= (

a

(

b

FT

)

F

)

T

((

a

FT

)

b

F

)

xy

=

a

(

byx

)(

bxy

)

as well as

NOT

bxy

=

b

FT

xy

=

b

(

F

xy

)(

T

xy

) =

byx

OR

abxy

=

a

T

bxy

=

a

(

T

xy

)(

bxy

) =

ax(bxy)

AND

abxy

=

ab

F

xy

=

a

(

bxy

)(

F

xy

) =

a(bxy)y

## Connection to intuitionistic logic

The combinators **K** and **S** correspond to two well-known axioms of propositional logic:

AK

:

A

→ (

B

→

A

)

,

AS

: (

A

→ (

B

→

C

)) → ((

A

→

B

) → (

A

→

C

))

.

Function application corresponds to the rule modus ponens:

MP

: from

A

and

A

→

B

, infer

B

.

The axioms **AK** and **AS**, and the rule **MP** are complete for the implicational fragment of intuitionistic logic. In order for combinatory logic to have as a model:

- the *implicational fragment of classical logic*, would require the combinatory analog to the law of excluded middle, *i.e.*, Peirce's law;
- *full classical logic*, would require the combinatory analog to the propositional axiom **F** → *A*.

This connection between the types of combinators and the corresponding logical axioms is an instance of the Curry–Howard isomorphism.

## Examples of reduction

There usually are multiple ways to do a reduction. If the term has a normal form, it is unique, hence the same result will be reached in such a case whatever the order of operations.

- ${\mathsf {SKI(KIS)}}$
  - ${\mathsf {SKI(KIS)}}\Rightarrow {\mathsf {K(KIS)(I(KIS))}}\Rightarrow {\mathsf {KI(I(KIS))}}\Rightarrow {\mathsf {I}}$
  - ${\mathsf {SKI(KIS)}}\Rightarrow {\mathsf {K(KIS)(I(KIS))}}\Rightarrow {\mathsf {KIS}}\Rightarrow {\mathsf {I}}$
  - ${\mathsf {SKI(KIS)}}\Rightarrow {\mathsf {SKII}}\Rightarrow {\mathsf {KI(II)}}\Rightarrow {\mathsf {I}}$
- ${\mathsf {KS(I(SKSI))}}$
  - ${\mathsf {KS(I(SKSI))}}\Rightarrow {\mathsf {KS(I(KI(SI)))}}\Rightarrow {\mathsf {KS(I(I))}}\Rightarrow {\mathsf {KS(II)}}\Rightarrow {\mathsf {KSI}}\Rightarrow {\mathsf {S}}$
  - ${\mathsf {KS(I(SKSI))}}\Rightarrow {\mathsf {S}}$
- ${\mathsf {SKIK}}$
  - ${\mathsf {SKIK}}\Rightarrow {\mathsf {KK(IK)}}\Rightarrow {\mathsf {KKK}}\Rightarrow {\mathsf {K}}$
  - ${\mathsf {SKIK}}\Rightarrow {\mathsf {KK(IK)}}\Rightarrow {\mathsf {K}}$
