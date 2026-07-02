---
title: "Constructible universe"
source: https://en.wikipedia.org/wiki/Constructible_universe
domain: forcing-set-theory
license: CC-BY-SA-4.0
tags: forcing method, continuum hypothesis, constructible universe, large cardinal
fetched: 2026-07-02
---

# Constructible universe

In mathematics, in set theory, the **constructible universe** (or **Gödel's constructible universe**), denoted by $L,$ is a particular class of sets that can be described entirely in terms of simpler sets. L is the union of the **constructible hierarchy** $L_{\alpha }$ . It was introduced by Kurt Gödel in his 1938 paper "The Consistency of the Axiom of Choice and of the Generalized Continuum-Hypothesis". In this paper, he proved that the constructible universe is an inner model of ZF set theory (that is, of Zermelo–Fraenkel set theory with the axiom of choice excluded), and also that the axiom of choice and the generalized continuum hypothesis are true in the constructible universe. This shows that both propositions are consistent with the basic axioms of set theory, if ZF itself is consistent. Since many other theorems only hold in systems in which one or both of the propositions is true, their consistency is an important result.

## What *L* is

L can be thought of as being built in "stages" resembling the construction of the von Neumann universe, V . The stages are indexed by ordinals. In von Neumann's universe, at a successor stage, one takes $V_{\alpha +1}$ to be the set of *all* subsets of the previous stage, $V_{\alpha }$ . By contrast, in Gödel's constructible universe L , one uses *only* those subsets of the previous stage that are:

- definable by a formula in the formal language of set theory,
- with parameters from the previous stage and,
- with the quantifiers interpreted to range over the previous stage.

By limiting oneself to sets defined only in terms of what has already been constructed, one ensures that the resulting sets will be constructed in a way that is independent of the peculiarities of the surrounding model of set theory and contained in any such model.

Define the Def operator:

$\operatorname {Def} (X):={\Bigl \{}\{y\in X\mid (X,\in )\models \Phi (y,z_{1},\ldots ,z_{n})\}~{\Big |}~\Phi {\text{ is a first-order formula and }}z_{1},\ldots ,z_{n}\in X{\Bigr \}}.$

L is defined by transfinite recursion as follows:

- ${\textstyle L_{0}:=\varnothing .}$
- ${\textstyle L_{\alpha +1}:=\operatorname {Def} (L_{\alpha }).}$
- If ${\textstyle \lambda }$ is a limit ordinal, then ${\textstyle L_{\lambda }:=\bigcup _{\alpha <\lambda }L_{\alpha }.}$ Here ${\textstyle \alpha <\lambda }$ means ${\textstyle \alpha }$ precedes ${\textstyle \lambda }$ .
- ${\textstyle L:=\bigcup _{\alpha \in \mathbf {Ord} }L_{\alpha }.}$ Here **Ord** denotes the class of all ordinals.

If z is an element of $L_{\alpha }$ , then $z=\{y\in L_{\alpha }\mid y\in z\}\in {\textrm {Def}}(L_{\alpha })=L_{\alpha +1}$ . So $L_{\alpha }$ is a subset of $L_{\alpha +1}$ , which is a subset of the power set of $L_{\alpha }$ . Consequently, this is a tower of nested transitive sets. But L itself is a proper class.

The elements of L are called "constructible" sets; and L itself is the "constructible universe". The "axiom of constructibility", sometimes denoted " $V=L$ ", says that every set (of V ) is constructible, i.e. in L .

## Additional facts about the sets *L**α*

An equivalent definition for $L_{\alpha }$ is:

For any ordinal

$\alpha$

,

$L_{\alpha }=\bigcup _{\beta <\alpha }\operatorname {Def} (L_{\beta })\!$

.

For any finite ordinal n , the sets $L_{n}$ and $V_{n}$ are the same (whether V equals L or not), and thus $L_{\omega }$ = $V_{\omega }$ : their elements are exactly the hereditarily finite sets. Equality beyond this point does not hold. Even in models of ZFC in which V equals L , $L_{\omega +1}$ is a proper subset of $V_{\omega +1}$ , and thereafter $L_{\alpha +1}$ is a proper subset of the power set of $L_{\alpha }$ for all $\alpha >\omega$ . On the other hand, $V=L$ does imply that $V_{\alpha }$ equals $L_{\alpha }$ if $\alpha =\omega _{\alpha }$ , for example if $\alpha$ is inaccessible. More generally, $V=L$ implies $H_{\alpha }$ = $L_{\alpha }$ for all infinite cardinals $\alpha$ , where $H_{\alpha }$ is the set of sets which are hereditarily of cardinality less than $\alpha$ (see hereditarily countable set#Generalizations).

If $\alpha$ is an infinite ordinal then there is a bijection between $L_{\alpha }$ and $\alpha$ , and the bijection is constructible. So these sets are equinumerous in any transitive model of set theory that includes them.

As defined above, ${\textrm {Def}}(X)$ is the set of subsets of X defined by $\Delta _{0}$ formulas (with respect to the Lévy hierarchy, i.e., formulas of set theory containing only bounded quantifiers) that use as parameters only X and its elements.

Another definition, due to Gödel, characterizes each $L_{\alpha +1}$ as the intersection of the power set of $L_{\alpha }$ with the closure of $L_{\alpha }\cup \{L_{\alpha }\}$ under a collection of nine explicit functions, similar to Gödel operations. This definition makes no reference to definability.

All arithmetical subsets of $\omega$ and relations on $\omega$ belong to $L_{\omega +1}$ (because the arithmetic definition gives one in $L_{\omega +1}$ ). Conversely, any subset of $\omega$ belonging to $L_{\omega +1}$ is arithmetical (because elements of $L_{\omega }$ can be coded by natural numbers in such a way that $\in$ is definable, i.e., arithmetic). On the other hand, $L_{\omega +2}$ already contains certain non-arithmetical subsets of $\omega$ , such as the set of (natural numbers coding) true arithmetical statements (this can be defined from $L_{\omega +1}$ {\displaystyle } ({\displaystyle }) so it is in $L_{\omega +2}$ ).

All hyperarithmetical subsets of $\omega$ and relations on $\omega$ belong to $L_{\omega _{1}^{\mathrm {CK} }}$ (where $\omega _{1}^{\mathrm {CK} }$ stands for the Church–Kleene ordinal), and conversely any subset of $\omega$ that belongs to $L_{\omega _{1}^{\mathrm {CK} }}$ is hyperarithmetical.

## *L* is a standard inner model of ZFC

$(L,\in )$ is a standard model, i.e. L is a transitive class and the interpretation uses the real element relationship, so it is well-founded. L is an inner model, i.e. it contains all the ordinal numbers of V and it has no "extra" sets beyond those in V . However L might be strictly a subclass of V . L is a model of ZFC, which means that it satisfies the following axioms:

- Axiom of regularity: Every non-empty set x contains some element y such that x and y are disjoint sets.

$(L,\in )$

is a substructure of

$(V,\in )$

, which is well founded, so

L

is well founded. In particular, if

$y\in x\in L$

, then by the transitivity of

L

,

$y\in L$

. If we use this same

y

as in

V

, then it is still disjoint from

x

because we are using the same element relation and no new sets were added.

- Axiom of extensionality: Two sets are the same if they have the same elements.

If

x

and

y

are in

L

and they have the same elements in

L

, then by

L

's transitivity, they have the same elements (in

V

). So they are equal (in

V

and thus in

L

).

- Axiom of empty set: {} is a set.

$\{\}=L_{0}=\{y\mid y\in L_{0}\land y=y\}$

, which is in

$L_{1}$

. So

$\{\}\in L$

. Since the element relation is the same and no new elements were added, this is the empty set of

L

.

- Axiom of pairing: If x , y are sets, then $\{x,y\}$ is a set.

If

$x\in L$

and

$y\in L$

, then there is some ordinal

$\alpha$

such that

$x\in L_{\alpha }$

and

$y\in L_{\alpha }$

. Then

$\{x,y\}=\{s\mid s\in L_{\alpha }\;\mathrm {and} \;(s=x\;\mathrm {or} \;s=y)\}\in L_{\alpha +1}$

. Thus

$\{x,y\}\in L$

and it has the same meaning for

L

as for

V

.

- Axiom of union: For any set x there is a set y whose elements are precisely the elements of the elements of x .

If

$x\in L_{\alpha }$

, then its elements are in

$L_{\alpha }$

and their elements are also in

$L_{\alpha }$

. So

y

is a subset of

$L_{\alpha }$

. Then

$y=\{s\mid s\in L_{\alpha }\;\mathrm {and} \;\mathrm {there} \;\mathrm {exists} \;z\in x\;\mathrm {such} \;\mathrm {that} \;s\in z\}\in L_{\alpha +1}$

. Thus

$y\in L$

.

- Axiom of infinity: There exists a set x such that $\varnothing$ is in x and whenever y is in x , so is the union $y\cup \{y\}$ .

Transfinite induction

can be used to show each ordinal

$\alpha$

is in

$L_{\alpha +1}$

. In particular,

$\omega \in L_{\omega +1}$

and thus

$\omega \in L$

.

- Axiom of separation: Given any set S and any proposition $P(x,z_{1},\ldots ,z_{n})$ , $\{x\mid x\in S\;\mathrm {and} \;P(x,z_{1},\ldots ,z_{n})\}$ is a set.

By induction on subformulas of

P

, one can show that there is an

$\alpha$

such that

$L_{\alpha }$

contains

S

and

$z_{1},\ldots ,z_{n}$

and (

P

is true in

$L_{\alpha }$

if and only if

P

is true in

L

), the latter is called the "

reflection principle

"). So

$\{x\mid x\in S\;\mathrm {and} \;P(x,z_{1},\ldots ,z_{n})\;\mathrm {holds} \;\mathrm {in} \;L\}$

=

$\{x\mid x\in L_{\alpha }\;\mathrm {and} \;x\in S\;\mathrm {and} \;P(x,z_{1},\ldots ,z_{n})\;\mathrm {holds} \;\mathrm {in} \;L_{\alpha }\}\in L_{\alpha +1}$

. Thus the subset is in

L

.

- Axiom of replacement: Given any set S and any mapping (formally defined as a proposition $P(x,y)$ where $P(x,y)$ and $P(x,z)$ implies $y=z$ ), $\{y\mid \;\mathrm {there} \;\mathrm {exists} \;x\in S\;\mathrm {such} \;\mathrm {that} \;P(x,y)\}$ is a set.

Let

$Q(x,y)$

be the formula that relativizes

P

to

L

, i.e. all quantifiers in

P

are restricted to

L

.

Q

is a much more complex formula than

Q

, but it is still a finite formula, and since

P

was a mapping over

L

,

Q

must be a mapping over

V

; thus we can apply replacement in

V

to

Q

. So

$\{y\mid y\in L\;\mathrm {and} \;\mathrm {there} \;\mathrm {exists} \;x\in S\;\mathrm {such} \;\mathrm {that} \;P(x,y)\;\mathrm {holds} \;\mathrm {in} \;L\}$

=

$\{y\mid \mathrm {there} \;\mathrm {exists} \;\mathrm {x} \in S\;\mathrm {such} \;\mathrm {that} \;Q(x,y)\}$

is a set in

V

and a subclass of

L

. Again using the axiom of replacement in

V

, we can show that there must be an

$\alpha$

such that this set is a subset of

$L_{\alpha }\in L_{\alpha +1}$

. Then one can use the axiom of separation in

L

to finish showing that it is an element of

L

- Axiom of power set: For any set x there exists a set y , such that the elements of y are precisely the subsets of x .

In general, some subsets of a set in

L

will not be in

L

So the whole power set of a set in

L

will usually not be in

L

. What we need here is to show that the intersection of the power set with

L

is

in

L

. Use replacement in

V

to show that there is an α such that the intersection is a subset of

$L_{\alpha }$

. Then the intersection is

$\{z\mid z\in L_{\alpha }\;\mathrm {and} \;z\;\mathrm {is} \;\mathrm {a} \;\mathrm {subset} \;\mathrm {of} \;x\}\in L_{\alpha +1}$

. Thus the required set is in

L

.

- Axiom of choice: Given a set x of mutually disjoint nonempty sets, there is a set y (a choice set for x ) containing exactly one element from each member of x .

One can show that there is a definable well-ordering of

L

, in particular based on ordering all sets in

L

by their definitions and by the rank they appear at. So one chooses the least element of each member of

x

to form

y

using the axioms of union and separation in

L

Notice that the proof that L is a model of ZFC only requires that V be a model of ZF, i.e. we do *not* assume that the axiom of choice holds in V .

## *L* is absolute and minimal

If W is any standard model of ZF sharing the same ordinals as V , then the L defined in W is the same as the L defined in V . In particular, $L_{\alpha }$ is the same in W and V , for any ordinal $\alpha$ . And the same formulas and parameters in $\mathrm {Def} (L_{\alpha })$ produce the same constructible sets in $L_{\alpha +1}$ .

Furthermore, since L is a subclass of V and, similarly, L is a subclass of W , L is the smallest class containing all the ordinals that is an inner model of ZF. Indeed, L is the intersection of all such classes.

If there is a *set* W in V that is an inner model of ZF, and the ordinal $\kappa$ is the set of ordinals that occur in W , then $L_{\kappa }$ is the L of W . If there is a set that is a standard model of ZF, then the smallest such set is such a $L_{\kappa }$ . This set is called the **minimal model** of ZFC. Using the downward Löwenheim–Skolem theorem, one can show that the minimal model (if it exists) is a countable set.

Of course, any consistent theory must have a model, so even within the minimal model of set theory there are sets that are models of ZF (assuming ZF is consistent). However, those set models are non-standard. In particular, they do not use the normal element relation and they are not well founded.

Because both " L constructed within L " and " V constructed within L " result in the real L , and both the L of $L_{\kappa }$ and the V of $L_{\kappa }$ are the real $L_{\kappa }$ , we get that $V=L$ is true in L and in any $L_{\kappa }$ that is a model of ZF. However, $V=L$ does not hold in any other standard model of ZF.

### *L* and large cardinals

Since $\mathrm {Ord} \subset L\subseteq V$ , properties of ordinals that depend on the absence of a function or other structure (i.e. $\Pi _{1}^{\mathrm {ZF} }$ formulas) are preserved when going down from V to L . Hence initial ordinals of cardinals remain initial in L . Regular ordinals remain regular in L . Weak limit cardinals become strong limit cardinals in L because the generalized continuum hypothesis holds in L . Weakly inaccessible cardinals become strongly inaccessible. Weakly Mahlo cardinals become strongly Mahlo. And more generally, any large cardinal property weaker than 0# (see the list of large cardinal properties) will be retained in L .

However, $0^{\sharp }$ is false in L even if true in V . So all the large cardinals whose existence implies $0^{\sharp }$ cease to have those large cardinal properties, but retain the properties weaker than $0^{\sharp }$ which they also possess. For example, measurable cardinals cease to be measurable but remain Mahlo in L .

If $0^{\sharp }$ holds in V , then there is a closed unbounded class of ordinals that are order-indiscernible in L . While some of these are not even initial ordinals in V , they have all the large cardinal properties weaker than $0^{\sharp }$ in L . Furthermore, any strictly increasing class function from this class of order-indiscernibles to itself can be extended in a unique way to an elementary embedding of L into L . This gives L a nice structure of repeating segments.

## *L* can be well-ordered

There are various ways of well-ordering L . Some of these involve the "fine structure" of L , which was first described by Ronald Bjorn Jensen in his 1972 paper entitled "The fine structure of the constructible hierarchy". Instead of explaining the fine structure, we will give an outline of how L could be well-ordered using only the definition given above.

Suppose x and y are two different sets in L and we wish to determine whether $x<y$ or $x>y$ . If x first appears in $L_{\alpha +1}$ and y first appears in $L_{\beta +1}$ and $\beta$ is different from $\alpha$ , then let $x<y$ if and only if $\alpha <\beta$ . Henceforth, we suppose that $\beta =\alpha$ .

The stage $L_{\alpha +1}=\mathrm {Def} (L_{\alpha })$ uses formulas with parameters from $L_{\alpha }$ to define the sets x and y . If one discounts (for the moment) the parameters, the formulas can be given a standard Gödel numbering by the natural numbers. If $\Phi$ is the formula with the smallest Gödel number that can be used to define x , and $\Psi$ is the formula with the smallest Gödel number that can be used to define y , and $\Psi$ is different from $\Phi$ , then let $x<y$ if and only if $\Phi <\Psi$ in the Gödel numbering. Henceforth, we suppose that $\Psi =\Phi$ .

Suppose that $\Phi$ uses n parameters from $L_{\alpha }$ . Suppose $z_{1},\ldots ,z_{n}$ is the sequence of parameters that can be used with $\Phi$ to define x , and $w_{1},\ldots ,w_{n}$ does the same for y . Then let $x<y$ if and only if either $z_{n}<w_{n}$ or ( $z_{n}=w_{n}$ and $z_{n-1}<w_{n-1}$ ) or ( $z_{n}=w_{n}$ and $z_{n-1}=w_{n-1}$ and $z_{n-2}<w_{n-2}$ ), etc. This is called the reverse lexicographic ordering; if there are multiple sequences of parameters that define one of the sets, we choose the least one under this ordering. It being understood that each parameter's possible values are ordered according to the restriction of the ordering of L to $L_{\alpha }$ , so this definition involves transfinite recursion on $\alpha$ .

The well-ordering of the values of single parameters is provided by the inductive hypothesis of the transfinite induction. The values of n -tuples of parameters are well-ordered by the product ordering. The formulas with parameters are well-ordered by the ordered sum (by Gödel numbers) of well-orderings. And L is well-ordered by the ordered sum (indexed by $\alpha$ ) of the orderings on $L_{\alpha +1}$ .

Notice that this well-ordering can be defined within L itself by a formula of set theory with no parameters, only the free-variables x and y . And this formula gives the same truth value regardless of whether it is evaluated in L , V , or W (some other standard model of ZF with the same ordinals) and we will suppose that the formula is false if either x or y is not in L .

It is well known that the axiom of choice is equivalent to the ability to well-order every set. Being able to well-order the proper class V (as we have done here with L ) is equivalent to the axiom of global choice, which is more powerful than the ordinary axiom of choice because it also covers proper classes of non-empty sets.

## *L* has a reflection principle

Proving that the axiom of separation, axiom of replacement, and axiom of choice hold in L requires (at least as shown above) the use of a reflection principle for L . Here we describe such a principle.

By induction on $n<\omega$ , we can use ZF in V to prove that for any ordinal $\alpha$ , there is an ordinal $\beta >\alpha$ such that for any sentence $P(z_{1},\ldots ,z_{k})$ with $z_{1},\ldots ,z_{k}$ in $L_{\beta }$ and containing fewer than n symbols (counting a constant symbol for an element of $L_{\beta }$ as one symbol) we get that $P(z_{1},\ldots ,z_{k})$ holds in $L_{\beta }$ if and only if it holds in L .

## The generalized continuum hypothesis holds in *L*

Let $S\in L_{\alpha }$ , and let T be any constructible subset of S . Then there is some $\beta$ with $T\in L_{\beta +1}$ , so $T=\{x\in L_{\beta }:x\in S\wedge \Phi (x,z_{i})\}=\{x\in S:\Phi (x,z_{i})\}$ , for some formula $\Phi$ and some $z_{i}$ drawn from $L_{\beta }$ . By the downward Löwenheim–Skolem theorem and Mostowski collapse, there must be some transitive set K containing $L_{\alpha }$ and some $w_{i}$ , and having the same first-order theory as $L_{\beta }$ with the $w_{i}$ substituted for the $z_{i}$ ; and this K will have the same cardinal as $L_{\alpha }$ . Since $V=L$ is true in $L_{\beta }$ , it is also true in *K*, so $K=L_{\gamma }$ for some $\gamma$ having the same cardinal as $\alpha$ . And $T=\{x\in L_{\beta }:x\in S\wedge \Phi (x,z_{i})\}=\{x\in L_{\gamma }:x\in S\wedge \Phi (x,w_{i})\}$ because $L_{\beta }$ and $L_{\gamma }$ have the same theory. So T is in fact in $L_{\gamma +1}$ .

So all the constructible subsets of an infinite set S have ranks with (at most) the same cardinal $\kappa$ as the rank of S ; it follows that if $\delta$ is the initial ordinal for $\kappa ^{+}$ , then $L\cap {\mathcal {P}}(S)\subseteq L_{\delta }$ serves as the "power set" of S within L Thus this "power set" $L\cap {\mathcal {P}}(S)\in L_{\delta +1}$ . And this in turn means that the "power set" of S has cardinal at most $\vert \delta \vert$ . Assuming S itself has cardinal $\kappa$ , the "power set" must then have cardinal exactly $\kappa ^{+}$ . But this is precisely the generalized continuum hypothesis relativized to L .

## Constructible sets are definable from the ordinals

There is a formula of set theory that expresses the idea that $X=L_{\alpha }$ . It has only free variables for X and $\alpha$ . Using this we can expand the definition of each constructible set. If $S\in L_{\alpha +1}$ , then $S=\{y\mid y\in L_{\alpha }\;\mathrm {and} \;\Phi (y,z_{1},\ldots ,z_{n})\;\mathrm {holds} \;\mathrm {in} \;(L_{\alpha },\in )\}$ for some formula $\Phi$ and some $z_{1},\ldots ,z_{n}$ in $L_{\alpha }$ . This is equivalent to saying that: for all y , $y\in S$ if and only if [there exists X such that $X=L_{\alpha }$ and $y\in X$ and $\Psi (X,y,z_{1},\ldots ,z_{n})$ ] where $\Psi (X,\ldots )$ is the result of restricting each quantifier in $\Phi (\ldots )$ to X . Notice that each $z_{k}\in L_{\beta +1}$ for some $\beta <\alpha$ . Combine formulas for the z 's with the formula for S and apply existential quantifiers over the z 's outside and one gets a formula that defines the constructible set S using only the ordinals $\alpha$ that appear in expressions like $x=L_{\alpha }$ as parameters.

Example: The set $\{5,\omega \}$ is constructible. It is the unique set s that satisfies the formula:

$\forall y(y\in s\iff (y\in L_{\omega +1}\land (\forall a(a\in y\iff a\in L_{5}\land Ord(a))\lor \forall b(b\in y\iff b\in L_{\omega }\land Ord(b)))))$

where $Ord(a)$ is short for:

$\forall c\in a(\forall d\in c(d\in a\land \forall e\in d(e\in c))).$

Actually, even this complex formula has been simplified from what the instructions given in the first paragraph would yield. But the point remains, there is a formula of set theory that is true only for the desired constructible set S and that contains parameters only for ordinals.

## Relative constructibility

Sometimes it is desirable to find a model of set theory that is narrow like L , but that includes or is influenced by a set that is not constructible. This gives rise to the concept of relative constructibility, of which there are two flavors, denoted by $L(A)$ and $L[A]$ .

The class $L(A)$ for a non-constructible set A is the intersection of all classes that are standard models of set theory and contain A and all the ordinals.

$L(A)$ can be defined by transfinite recursion as follows:

- $L_{0}(A)$ = the smallest transitive set containing A as an element, i.e. the transitive closure of $\{A\}$ .
- $L_{\alpha +1}(A)$ = $\mathrm {Def} (L_{\alpha }(A))$
- If $\lambda$ is a limit ordinal, then $L_{\lambda }(A)=\bigcup _{\alpha <\lambda }L_{\alpha }(A)$ .
- $L(A)=\bigcup _{\alpha }L_{\alpha }(A)$ .

If $L(A)$ contains a well-ordering of the transitive closure of $\{A\}$ , then this can be extended to a well-ordering of $L(A)$ . Otherwise, the axiom of choice will fail in $L(A)$ .

A common example is $L(\mathbb {R} )$ , the smallest model that contains all the real numbers, which is used extensively in modern descriptive set theory.

The class $L[A]$ is the class of sets whose construction is influenced by A , where A may be a (presumably non-constructible) set or a proper class. The definition of this class uses $\mathrm {Def} _{A}(X)$ , which is the same as $\mathrm {Def} (X)$ except instead of evaluating the truth of formulas $\Phi$ in the model $(X,\in )$ , one uses the model $(X,\in ,A)$ where A is a unary predicate. The intended interpretation of $A(y)$ is $y\in A$ . Then the definition of $L[A]$ is exactly that of L only with $\mathrm {Def}$ replaced by $\mathrm {Def} _{A}$ .

$L[A]$ is always a model of the axiom of choice. Even if A is a set, A is not necessarily itself a member of $L[A]$ , although it always is if A is a set of ordinals.

The sets in $L(A)$ or $L[A]$ are usually not actually constructible, and the properties of these models may be quite different from the properties of L itself.
