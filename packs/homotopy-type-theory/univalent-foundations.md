---
title: "Univalent foundations"
source: https://en.wikipedia.org/wiki/Univalent_foundations
domain: homotopy-type-theory
license: CC-BY-SA-4.0
tags: homotopy type theory, intuitionistic type theory, univalent foundations, identity type
fetched: 2026-07-02
---

# Univalent foundations

**Univalent foundations** are an approach to the foundations of mathematics in which mathematical structures are built out of objects called *types*. Types in univalent foundations do not correspond exactly to anything in set-theoretic foundations, but they may be thought of as spaces, with equal types corresponding to homotopy equivalent spaces and with equal elements of a type corresponding to points of a space connected by a path. Univalent foundations are inspired both by the old Platonic ideas of Hermann Grassmann and Georg Cantor and by "categorical" mathematics in the style of Alexander Grothendieck. Univalent foundations depart from (although are also compatible with) the use of classical predicate logic as the underlying formal deduction system, replacing it, at the moment, with a version of Martin-Löf type theory. The development of univalent foundations is closely related to the development of homotopy type theory.

Univalent foundations are compatible with structuralism, if an appropriate (i.e., categorical) notion of mathematical structure is adopted.

## History

The main ideas of univalent foundations were formulated by Vladimir Voevodsky during the years 2006 to 2009. The sole reference for the philosophical connections between univalent foundations and earlier ideas are Voevodsky's 2014 Bernays lectures. The name "univalence" is due to Voevodsky. A more detailed discussion of the history of some of the ideas that contribute to the current state of univalent foundations can be found at the page on homotopy type theory (HoTT).

A fundamental characteristic of univalent foundations is that they—when combined with the Martin-Löf type theory (MLTT)—provide a practical system for formalization of modern mathematics. A considerable amount of mathematics has been formalized using this system and modern proof assistants such as Rocq (previously known as *Coq*) and Agda. The first such library called "Foundations" was created by Vladimir Voevodsky in 2010. Now Foundations is a part of a larger development with several authors called UniMath. Foundations also inspired other libraries of formalized mathematics, such as the HoTT Coq library and HoTT Agda library, that developed univalent ideas in new directions.

An important milestone for univalent foundations was the Bourbaki Seminar talk by Thierry Coquand in June 2014.

## Main concepts

Univalent foundations originated from certain attempts to create foundations of mathematics based on higher category theory. The closest earlier ideas to univalent foundations were the ideas that Michael Makkai denotes 'first-order logic with dependent sorts' (FOLDS). The main distinction between univalent foundations and the foundations envisioned by Makkai is the recognition that "higher dimensional analogs of sets" correspond to infinity groupoids and that categories should be considered as higher-dimensional analogs of partially ordered sets.

Originally, univalent foundations were devised by Vladimir Voevodsky with the goal of enabling those who work in classical pure mathematics to use computers to verify their theorems and constructions. The fact that univalent foundations are inherently constructive was discovered in the process of writing the Foundations library (now part of UniMath). At present, in univalent foundations, classical mathematics is considered to be a "retract" of constructive mathematics, i.e., classical mathematics is both a subset of constructive mathematics consisting of those theorems and constructions that use the law of the excluded middle as their assumption and a "quotient" of constructive mathematics by the relation of being equivalent modulo the axiom of the excluded middle.

In the formalization system for univalent foundations that is based on Martin-Löf type theory and its descendants such as Calculus of Inductive Constructions, the higher dimensional analogs of sets are represented by types. The collection of types is stratified by the concept of *h-level* (or *homotopy level*).

Types of h-level 0 are those equal to the one point type. They are also called contractible types.

Types of h-level 1 are those in which any two elements are equal. Such types are called "propositions" in univalent foundations. The definition of propositions in terms of the h-level agrees with the definition suggested earlier by Awodey and Bauer. So, while all propositions are types, not all types are propositions. Being a proposition is a property of a type that requires proof. For example, the first fundamental construction in univalent foundations is called **iscontr**. It is a function from types to types. If **X** is a type then **iscontr X** is a type that has an object if and only if **X** is contractible. It is a theorem (which is called, in the UniMath library, **isapropiscontr**) that for any **X** the type **iscontr X** has h-level 1 and therefore being a contractible type is a property. This distinction between properties that are witnessed by objects of types of h-level 1 and structures that are witnessed by objects of types of higher h-levels is very important in the univalent foundations.

Types of h-level 2 are called sets. It is a theorem that the type of natural numbers has h-level 2 (**isasetnat** in UniMath). It is claimed by the creators of univalent foundations that the univalent formalization of sets in Martin-Löf type theory is the best currently-available environment for formal reasoning about all aspects of set-theoretical mathematics, both constructive and classical.

Categories are defined (see the RezkCompletion library in UniMath) as types of h-level 3 with an additional structure that is very similar to the structure on types of h-level 2 that defines partially ordered sets. The theory of categories in univalent foundations is somewhat different and richer than the theory of categories in the set-theoretic world with the key new distinction being that between pre-categories and categories.

An account of the main ideas of univalent foundations and their connection to constructive mathematics can be found in a tutorial by Thierry Coquand. A presentation of the main ideas from the perspective of classical mathematics can be found in the 2014 review by Alvaro Pelayo and Michael Warren, as well as in the introduction by Daniel Grayson. See also: Vladimir Voevodsky (2014).

## Current developments

An account of Voevodsky's construction of a univalent model of the Martin-Löf type theory with values in Kan simplicial sets can be found in a paper by Chris Kapulkin, Peter LeFanu Lumsdaine and Vladimir Voevodsky. Univalent models with values in the categories of inverse diagrams of simplicial sets were constructed by Michael Shulman. These models have shown that the univalence axiom is independent from the excluded middle axiom for propositions.

Voevodsky's model is considered to be non-constructive since it uses the axiom of choice in an ineliminable way.

The problem of finding a constructive interpretation of the rules of the Martin-Löf type theory that in addition satisfies the univalence axiom and canonicity for natural numbers remains open. A partial solution is outlined in a paper by Marc Bezem, Thierry Coquand and Simon Huber with the key remaining issue being the computational property of the eliminator for the identity types. The ideas of this paper are now being developed in several directions including the development of the cubical type theory.

## New directions

Most of the work on formalization of mathematics in the framework of univalent foundations is being done using various sub-systems and extensions of the Calculus of Inductive Constructions (CIC).

There are three standard problems whose solution, despite many attempts, could not be constructed using CIC:

1. To define the types of semi-simplicial types, H-types or (infty,1)-category structures on types.
2. To extend CIC with a universe management system that would allow implementation of the resizing rules.
3. To develop a constructive variant of the Univalence Axiom

These unsolved problems indicate that while CIC is a good system for the initial phase of the development of the univalent foundations, moving towards the use of computer proof assistants in the work on its more sophisticated aspects will require the development of a new generation of formal deduction and computation systems.
