---
title: "Finite model theory"
source: https://en.wikipedia.org/wiki/Finite_model_theory
domain: descriptive-complexity
license: CC-BY-SA-4.0
tags: descriptive complexity, second order logic, fagin theorem, finite model theory
fetched: 2026-07-02
---

# Finite model theory

**Finite model theory** is a subarea of model theory. Model theory is the branch of logic which deals with the relation between a formal language (syntax) and its interpretations (semantics). Finite model theory is a restriction of model theory to interpretations on finite structures, which have a finite universe.

Since many central theorems of model theory do not hold when restricted to finite structures, finite model theory is quite different from model theory in its methods of proof. Central results of classical model theory that fail for finite structures under finite model theory include the compactness theorem, Gödel's completeness theorem, and the method of ultraproducts for first-order logic (FO). These invalidities all follow from Trakhtenbrot's theorem.

While model theory has many applications to mathematical algebra, finite model theory became an "unusually effective" instrument in computer science. In other words: "In the history of mathematical logic most interest has concentrated on infinite structures. [...] Yet, the objects computers have and hold are always finite. To study computation we need a theory of finite structures." Thus the main application areas of finite model theory are: descriptive complexity theory, database theory and formal language theory.

## Axiomatisability

A common motivating question in finite model theory is whether a given class of structures can be described in a given language. For instance, one might ask whether the class of cyclic graphs can be distinguished among graphs by a FO sentence, which can also be phrased as asking whether cyclicity is FO-expressible.

A single finite structure can always be axiomatized in first-order logic, where axiomatized in a language *L* means described uniquely up to isomorphism by a single *L*-sentence. Similarly, any finite collection of finite structures can always be axiomatized in first-order logic. Some, but not all, infinite collections of finite structures can also be axiomatized by a single first-order sentence.

### Characterisation of a single structure

Is a language *L* expressive enough to axiomatize a single finite structure *S*?

#### Problem

A structure like (1) in the figure can be described by FO sentences in the logic of graphs like

1. Every node has an edge to another node: $\forall _{x}\exists _{y}G(x,y).$
2. No node has an edge to itself: $\forall _{x,y}(G(x,y)\Rightarrow x\neq y).$
3. There is at least one node that is connected to all others: $\exists _{x}\forall _{y}(x\neq y\Rightarrow G(x,y)).$

However, these properties do not axiomatize the structure, since for structure (1') the above properties hold as well, yet structures (1) and (1') are not isomorphic.

Informally the question is whether by adding enough properties, these properties together describe exactly (1) and are valid (all together) for no other structure (up to isomorphism).

#### Approach

For a single finite structure it is always possible to precisely describe the structure by a single FO sentence. The principle is illustrated here for a structure with one binary relation R and without constants. To this aim, we introduce first-order variables $x_{1},\dots ,x_{n}$ that are interpreted as the n elements of the structure. We then introduce the four following formulas:

1. $\varphi _{1}=\bigwedge _{i\neq j}\neg (x_{i}=x_{j})$ says that there are at least n elements;
2. $\varphi _{2}=\forall _{y}\bigvee _{i}(x_{i}=y)$ says that there are at most n elements;
3. $\varphi _{3}=\bigwedge _{(a_{i},a_{j})\in R}R(x_{i},x_{j})$ states every edge of the relation R ;
4. $\varphi _{4}=\bigwedge _{(a_{i},a_{j})\notin R}\neg R(x_{i},x_{j})$ states every non-edge of the relation R .

Finally, the structure is described by the FO sentence $\exists _{x_{1}}\dots \exists _{x_{n}}(\varphi _{1}\land \varphi _{2}\land \varphi _{3}\land \varphi _{4})$ .

#### Extension to a fixed number of structures

The method of describing a single finite structure by means of a first-order sentence can easily be extended for any fixed number of structures. A unique description can be obtained by the disjunction of the descriptions for each structure. For instance, for two finite structures A and B with defining sentences $\varphi _{A}$ and $\varphi _{B}$ this would be

$\varphi _{A}\lor \varphi _{B}.$

#### Extension to an infinite structure

By definition, a set containing an infinite structure falls outside the area that FMT deals with. Note that infinite structures can never be discriminated in FO, because of the Löwenheim–Skolem theorem, which implies that no first-order theory with an infinite model can have a unique model up to isomorphism.

The most famous example is probably Skolem's theorem, that there is a countable non-standard model of arithmetic.

### Characterisation of a class of structures

Is a language *L* expressive enough to describe exactly (up to isomorphism) those finite structures that have certain property *P*?

#### Problem

The descriptions given so far all specify the number of elements of the universe. Unfortunately most interesting sets of structures are not restricted to a certain size, like all graphs that are trees, are connected or are acyclic. Thus to discriminate a finite number of structures is of special importance.

#### Approach

Instead of a general statement, the following is a sketch of a methodology to differentiate between structures that can and cannot be discriminated.

1. The core idea is that whenever one wants to see if a property *P* can be expressed in FO, one chooses structures *A* and *B*, where *A* does have *P* and *B* doesn't. If for *A* and *B* the same FO sentences hold, then *P* cannot be expressed in FO. In short: $A\in P,B\not \in P$ and $A\equiv B,$ where $A\equiv B$ is shorthand for $A\models \alpha \Leftrightarrow B\models \alpha$ for all FO-sentences α, and *P* represents the class of structures with property *P*.
2. The methodology considers countably many subsets of the language, the union of which forms the language itself. For instance, for FO consider classes FO[*m*] for each *m*. For each *m* the above core idea then has to be shown. That is: $A\in P,B\not \in P$ and $A\equiv _{m}B$ with a pair $A,B$ for each m and α (in ≡) from FO[*m*]. It may be appropriate to choose the classes FO[*m*] to form a partition of the language.
3. One common way to define FO[*m*] is by means of the quantifier rank qr(α) of a FO formula α, which expresses the depth of quantifier nesting. For example, for a formula in prenex normal form, qr is simply the total number of its quantifiers. Then FO[*m*] can be defined as all FO formulas α with qr(α) ≤ *m* (or, if a partition is desired, as those FO formulas with quantifier rank equal to *m*).
4. Thus it all comes down to showing $A\models \alpha \Leftrightarrow B\models \alpha$ on the subsets FO[*m*]. The main approach here is to use the algebraic characterization provided by Ehrenfeucht–Fraïssé games. Informally, these take a single partial isomorphism on *A* and *B* and extend it *m* times, in order to either prove or disprove $A\equiv _{m}B$ , dependent on who wins the game.

#### Example

We want to show that the property that the size of an ordered structure **A** = (A, ≤) is even, can not be expressed in FO.

1. The idea is to pick **A** ∈ EVEN and **B** ∉ EVEN, where EVEN is the class of all structures of even size.
2. We start with two ordered structures **A2** and **B2** with universes A2 = {1, 2, 3, 4} and B2 = {1, 2, 3}. Obviously **A2** ∈ EVEN and **B2** ∉ EVEN.
3. For *m* = 2, in a 2-move Ehrenfeucht–Fraïssé game on **A2** and **B2** the duplicator always wins, and thus **A2** and **B2** cannot be discriminated in FO[2], i.e. $\mathbf {A} _{2}\models \alpha \iff \mathbf {B} _{2}\models \alpha$ for every *α* ∈ FO[2].
4. Next we have to scale the structures up by increasing *m*. For example, for *m* = 3 we must find an **A3** and **B3** such that the duplicator always wins the 3-move game. This can be achieved by A3 = {1, ..., 8} and B3 = {1, ..., 7}. More generally, we can choose A*m* = {1, ..., 2*m*} and B*m* = {1, ..., 2*m*−1}; for any *m* the duplicator always wins the *m*-move game for this pair of structures*.
5. Thus EVEN on finite ordered structures cannot be expressed in FO.

## Zero-one laws

Glebskiĭ et al. (1969) and, independently, Fagin (1976) proved a zero–one law for first-order sentences in finite models; Fagin's proof used the compactness theorem. According to this result, every first-order sentence in a relational signature $\sigma$ is either almost always true or almost always false in finite $\sigma$ -structures. That is, let S be a fixed first-order sentence, and choose a random $\sigma$ -structure $G_{n}$ with domain $\{1,\dots ,n\}$ , uniformly among all $\sigma$ -structures with domain $\{1,\dots ,n\}$ . Then in the limit as n tends to infinity, the probability that Gn models S will tend either to zero or to one:

$\lim _{n\to \infty }\operatorname {Pr} [G_{n}\models S]\in \{0,1\}.$

The problem of determining whether a given sentence has probability tending to zero or to one is PSPACE-complete.

A similar analysis has been performed for more expressive logics than first-order logic. The 0-1 law has been shown to hold for sentences in FO(LFP), first-order logic augmented with a least fixed point operator, and more generally for sentences in the infinitary logic $L_{\infty \omega }^{\omega }$ , which allows for potentially arbitrarily long conjunctions and disjunctions. Another important variant is the unlabelled 0-1 law, where instead of considering the fraction of structures with domain $\{1,\dots ,n\}$ , one considers the fraction of isomorphism classes of structures with n elements. This fraction is well-defined, since any two isomorphic structures satisfy the same sentences. The unlabelled 0-1 law also holds for $L_{\infty \omega }^{\omega }$ and therefore in particular for FO(LFP) and first-order logic.

## Descriptive complexity theory

An important goal of finite model theory is the characterisation of complexity classes by the type of logic needed to express the languages in them. For example, PH, the union of all complexity classes in the polynomial hierarchy, is precisely the class of languages expressible by statements of second-order logic. This connection between complexity and the logic of finite structures allows results to be transferred easily from one area to the other, facilitating new proof methods and providing additional evidence that the main complexity classes are somehow "natural" and not tied to the specific abstract machines used to define them.

Specifically, each logical system produces a set of queries expressible in it. The queries – when restricted to finite structures – correspond to the computational problems of traditional complexity theory.

Some well-known complexity classes are captured by logical languages as follows:

- In the presence of a linear order, first-order logic with a commutative, transitive closure operator added yields L, problems solvable in logarithmic space.
- In the presence of a linear order, first-order logic with a transitive closure operator yields NL, the problems solvable in nondeterministic logarithmic space.
- In the presence of a linear order, first-order logic with a least fixed point operator gives P, the problems solvable in deterministic polynomial time.
- On all finite structures (regardless of whether they are ordered), Existential second-order logic gives NP (Fagin's theorem).

## Applications

### Database theory

A substantial fragment of SQL (namely that which is effectively relational algebra) is based on first-order logic (more precisely can be translated in domain relational calculus by means of Codd's theorem), as the following example illustrates: Think of a database table "GIRLS" with the columns "FIRST_NAME" and "LAST_NAME". This corresponds to a binary relation, say G(f, l) on FIRST_NAME × LAST_NAME. The FO query ${l:G({\text{'Judy'}},l)}$ , which returns all the last names where the first name is 'Judy', would look in SQL like this:

```mw
select LAST_NAME 
from GIRLS
where FIRST_NAME = 'Judy'
```

Notice, we assume here, that all last names appear only once (or we should use SELECT DISTINCT since we assume that relations and answers are sets, not bags).

Next we want to make a more complex statement. Therefore, in addition to the "GIRLS" table we have a table "BOYS" also with the columns "FIRST_NAME" and "LAST_NAME". Now we want to query the names of all the girls that have the same last name as at least one of the boys. The FO query is ${(f,l):\exists h(G(f,l)\land B(h,l))}$ , and the corresponding SQL statement is:

```mw
select FIRST_NAME, LAST_NAME 
from GIRLS
where LAST_NAME IN ( select LAST_NAME from BOYS );
```

Notice that in order to express the "∧" we introduced the new language element "IN" with a subsequent select statement. This makes the language more expressive for the price of higher difficulty to learn and implement. This is a common trade-off in formal language design. The way shown above ("IN") is by far not the only one to extend the language. An alternative way is e.g. to introduce a "JOIN" operator, that is:

```mw
select distinct g.FIRST_NAME, g.LAST_NAME 
from GIRLS g, BOYS b
where g.LAST_NAME=b.LAST_NAME;
```

First-order logic is too restrictive for some database applications, for instance because of its inability to express transitive closure. This has led to more powerful constructs being added to database query languages, such as recursive WITH in SQL:1999. More expressive logics, like fixpoint logics, have therefore been studied in finite model theory because of their relevance to database theory and applications.

Narrative data contains no defined relations. Thus the logical structure of text search queries can be expressed in propositional logic, like in:

```
("Java" AND NOT "island") OR ("C#" AND NOT "music")
```

Note that the challenges in full text search are different from database querying, like ranking of results.

## History

- Trakhtenbrot 1950: failure of completeness theorem in first-order logic
- Scholz 1952: characterisation of spectra in first-order logic
- Fagin 1974: the set of all properties expressible in existential second-order logic is precisely the complexity class NP
- Chandra, Harel 1979/80: fixed-point first-order logic extension for database query languages capable of expressing transitive closure -> queries as central objects of FMT
- Immerman, Vardi 1982: fixed-point logic over ordered structures captures PTIME -> descriptive complexity (Immerman–Szelepcsényi theorem)
- Ebbinghaus, Flum 1995: first comprehensive book "Finite Model Theory"
- Abiteboul, Hull, Vianu 1995: book "Foundations of Databases"
- Immerman 1999: book "Descriptive Complexity"
- Kuper, Libkin, Paredaens 2000: book "Constraint Databases"
- Darmstadt 2005/ Aachen 2006: first international workshops on "Algorithmic Model Theory"
