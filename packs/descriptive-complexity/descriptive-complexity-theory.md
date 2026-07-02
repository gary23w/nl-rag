---
title: "Descriptive complexity theory"
source: https://en.wikipedia.org/wiki/Descriptive_complexity_theory
domain: descriptive-complexity
license: CC-BY-SA-4.0
tags: descriptive complexity, second order logic, fagin theorem, finite model theory
fetched: 2026-07-02
---

# Descriptive complexity theory

**Descriptive complexity** is a branch of computational complexity theory and of finite model theory that characterizes complexity classes by the type of logic needed to express the languages in them. For example, PH, the union of all complexity classes in the polynomial hierarchy, is precisely the class of languages expressible by statements of second-order logic. This connection between complexity and the logic of finite structures allows results to be transferred easily from one area to the other, facilitating new proof methods and providing additional evidence that the main complexity classes are somehow "natural" and not tied to the specific abstract machines used to define them.

Specifically, each logical system produces a set of queries expressible in it. The queries – when restricted to finite structures – correspond to the computational problems of traditional complexity theory.

The first main result of descriptive complexity was Fagin's theorem, shown by Ronald Fagin in 1974. It established that NP is precisely the set of languages expressible by sentences of existential second-order logic; that is, second-order logic excluding universal quantification over relations, functions, and subsets. Many other classes were later characterized in such a manner.

## The setting

When we use the logic formalism to describe a computational problem, the input is a finite structure, and the elements of that structure are the domain of discourse. Usually the input is either a string (of bits or over an alphabet) and the elements of the logical structure represent positions of the string, or the input is a graph and the elements of the logical structure represent its vertices. The length of the input will be measured by the size of the respective structure. Whatever the structure is, we can assume that there are relations that can be tested, for example " $E(x,y)$ is true if and only if there is an edge from x to y" (in case of the structure being a graph), or " $P(n)$ is true if and only if the nth letter of the string is 1." These relations are the predicates for the first-order logic system. We also have constants, which are special elements of the respective structure, for example if we want to check reachability in a graph, we will have to choose two constants *s* (start) and *t* (terminal).

In descriptive complexity theory we often assume that there is a total order over the elements and that we can check equality between elements. This lets us consider elements as numbers: the element x represents the number n if and only if there are $(n-1)$ elements y with $y<x$ . Thanks to this we also may have the primitive predicate "bit", where $bit(x,k)$ is true if only the kth bit of the binary expansion of x is 1. (We can replace addition and multiplication by ternary relations such that $plus(x,y,z)$ is true if and only if $x+y=z$ and $times(x,y,z)$ is true if and only if $x*y=z$ ).

## Overview of characterisations of complexity classes

If we restrict ourselves to ordered structures with a successor relation and basic arithmetical predicates, then we get the following characterisations:

- First-order logic defines the class AC0, the languages recognized by polynomial-size circuits of bounded depth, which equals the languages recognized by a concurrent random access machine in constant time.
- First-order logic augmented with symmetric or deterministic transitive closure operators yield L, problems solvable in logarithmic space.
- First-order logic with a transitive closure operator yields NL, the problems solvable in nondeterministic logarithmic space.
- First-order logic with a least fixed point operator gives P, the problems solvable in deterministic polynomial time, **but uniquely on ordered structures**.
- Existential second-order logic yields NP.
- Universal second-order logic (excluding existential second-order quantification) yields co-NP.
- Second-order logic corresponds to the polynomial hierarchy PH.
- Second-order logic with a transitive closure operator (commutative or not) yields PSPACE, the problems solvable in polynomial space.
- Second-order logic with a least fixed point operator gives EXPTIME, the problems solvable in exponential time.
- HO, the complexity class defined by higher-order logic, is equal to ELEMENTARY

## Sub-polynomial time

### FO without any operators

In circuit complexity, first-order logic with arbitrary predicates can be shown to be equal to AC0, the first class in the AC hierarchy. Indeed, there is a natural translation from FO's symbols to nodes of circuits, with $\forall ,\exists$ being $\land$ and $\lor$ of size n. First-order logic in a signature with arithmetical predicates characterises the restriction of the AC0 family of circuits to those constructible in alternating logarithmic time. First-order logic in a signature with only the order relation corresponds to the set of star-free languages.

### Transitive closure logic

First-order logic gains substantially in expressive power when it is augmented with an operator that computes the transitive closure of a binary relation. The resulting transitive closure logic is known to characterise non-deterministic logarithmic space (NL) on ordered structures. This was used by Immerman to show that NL is closed under complement (i. e. that NL = co-NL).

When restricting the transitive closure operator to deterministic transitive closure, the resulting logic exactly characterises logarithmic space on ordered structures.

### Second-order Krom formulae

On structures that have a successor function, NL can also be characterised by second-order Krom formulae.

SO-Krom is the set of Boolean queries definable with second-order formulae in conjunctive normal form such that the first-order quantifiers are universal and the quantifier-free part of the formula is in Krom form, which means that the first-order formula is a conjunction of disjunctions, and in each "disjunction" there are at most two variables. Every second-order Krom formula is equivalent to an existential second-order Krom formula.

SO-Krom characterises NL on structures with a successor function.

## Polynomial time

On ordered structures, first-order least fixed-point logic captures PTIME:

### First-order least fixed-point logic

FO[LFP] is the extension of first-order logic by a least fixed-point operator, which expresses the fixed-point of a monotone expression. This augments first-order logic with the ability to express recursion. The Immerman–Vardi theorem, shown independently by Immerman and Vardi, shows that FO[LFP] characterises PTIME on ordered structures.

As of 2025, it is still open whether there is a natural logic characterising PTIME on unordered structures.

The Abiteboul–Vianu theorem states that FO[LFP]=FO[PFP] on all structures if and only if FO[LFP]=FO[PFP]; hence if and only if P=PSPACE. This result has been extended to other fixpoints.

### Second-order Horn formulae

In the presence of a successor function, PTIME can also be characterised by second-order Horn formulae.

SO-Horn is the set of Boolean queries definable with SO formulae in disjunctive normal form such that the first-order quantifiers are all universal and the quantifier-free part of the formula is in Horn form, which means that it is a big AND of OR, and in each "OR" every variable except possibly one are negated.

This class is equal to P on structures with a successor function.

Those formulae can be transformed to prenex formulas in existential second-order Horn logic.

## Non-deterministic polynomial time

### Fagin's theorem

Ronald Fagin's 1974 proof that the complexity class NP was characterised exactly by those classes of structures axiomatizable in existential second-order logic was the starting point of descriptive complexity theory.

Since the complement of an existential formula is a universal formula, it follows immediately that co-NP is characterized by universal second-order logic.

SO, unrestricted second-order logic, is equal to the Polynomial hierarchy PH. More precisely, we have the following generalisation of Fagin's theorem: The set of formulae in prenex normal form where existential and universal quantifiers of second order alternate *k* times characterise the *k*th level of the polynomial hierarchy.

Unlike most other characterisations of complexity classes, Fagin's theorem and its generalisation do not presuppose a total ordering on the structures. This is because existential second-order logic is itself sufficiently expressive to refer to the possible total orders on a structure using second-order variables.

## Beyond NP

### Partial fixed point is PSPACE

The class of all problems computable in polynomial space, PSPACE, can be characterised by augmenting first-order logic with a more expressive partial fixed-point operator.

Partial fixed-point logic, FO[PFP], is the extension of first-order logic with a partial fixed-point operator, which expresses the fixed-point of a formula if there is one and returns 'false' otherwise.

Partial fixed-point logic characterises PSPACE on ordered structures.

### Transitive closure is PSPACE

Second-order logic can be extended by a transitive closure operator in the same way as first-order logic, resulting in SO[TC]. The TC operator can now also take second-order variables as argument. SO[TC] characterises PSPACE. Since ordering can be referenced in second-order logic, this characterisation does not presuppose ordered structures.

## Elementary functions

The time complexity class ELEMENTARY of elementary functions can be characterised by **HO**, the complexity class of structures that can be recognized by formulas of higher-order logic. Higher-order logic is an extension of first-order logic and second-order logic with higher-order quantifiers. There is a relation between the i th order and non-deterministic algorithms the time of which is bounded by $i-1$ levels of exponentials.

### Definition

We define higher-order variables. A variable of order $i>1$ has an arity k and represents any set of k -tuples of elements of order $i-1$ . They are usually written in upper-case and with a natural number as exponent to indicate the order. Higher-order logic is the set of first-order formulae where we add quantification over higher-order variables; hence we will use the terms defined in the FO article without defining them again.

HO $^{i}$ is the set of formulae with variables of order at most i . HO $_{j}^{i}$ is the subset of formulae of the form $\phi =\exists {\overline {X_{1}^{i}}}\forall {\overline {X_{2}^{i}}}\dots Q{\overline {X_{j}^{i}}}\psi$ , where Q is a quantifier and $Q{\overline {X^{i}}}$ means that ${\overline {X^{i}}}$ is a tuple of variable of order i with the same quantification. So HO $_{j}^{i}$ is the set of formulae with j alternations of quantifiers of order i , beginning with $\exists$ , followed by a formula of order $i-1$ .

Using the standard notation of the tetration, $\exp _{2}^{0}(x)=x$ and $\exp _{2}^{i+1}(x)=2^{\exp _{2}^{i}(x)}$ . $\exp _{2}^{i+1}(x)=2^{2^{2^{2^{\dots ^{2^{x}}}}}}$ with i times 2

### Normal form

Every formula of order i th is equivalent to a formula in prenex normal form, where we first write quantification over variable of i th order and then a formula of order $i-1$ in normal form.

### Relation to complexity classes

HO is equal to the class ELEMENTARY of elementary functions. To be more precise, ${\mathsf {HO}}_{0}^{i}={\mathsf {NTIME}}(\exp _{2}^{i-2}(n^{O(1)}))$ , meaning a tower of $(i-2)$ 2s, ending with $n^{c}$ , where c is a constant. A special case of this is that $\exists {\mathsf {SO}}={\mathsf {HO}}_{0}^{2}={\mathsf {NTIME}}(n^{O(1)})={\color {Blue}{\mathsf {NP}}}$ , which is exactly Fagin's theorem. Using oracle machines in the polynomial hierarchy, ${\mathsf {HO}}_{j}^{i}={\color {Blue}{\mathsf {NTIME}}}(\exp _{2}^{i-2}(n^{O(1)})^{\Sigma _{j}^{\mathsf {P}}})$
