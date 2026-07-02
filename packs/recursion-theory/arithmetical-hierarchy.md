---
title: "Arithmetical hierarchy"
source: https://en.wikipedia.org/wiki/Arithmetical_hierarchy
domain: recursion-theory
license: CC-BY-SA-4.0
tags: computability theory, turing degree, halting problem, arithmetical hierarchy
fetched: 2026-07-02
---

# Arithmetical hierarchy

In mathematical logic, the **arithmetical hierarchy**, **arithmetic hierarchy** or **Kleene–Mostowski hierarchy** (after mathematicians Stephen Cole Kleene and Andrzej Mostowski) classifies certain sets based on the complexity of formulas that define them. Any set that receives a classification is called **arithmetical**. The arithmetical hierarchy was invented independently by Kleene (1943) and Mostowski (1946).

The arithmetical hierarchy is important in computability theory, effective descriptive set theory, and the study of formal theories such as Peano arithmetic.

The Tarski–Kuratowski algorithm provides an easy way to get an upper bound on the classifications assigned to a formula and the set it defines.

The hyperarithmetical hierarchy and the analytical hierarchy extend the arithmetical hierarchy to classify additional formulas and sets.

## The arithmetical hierarchy of formulas

The arithmetical hierarchy assigns classifications to the formulas in the language of first-order arithmetic. The classifications are denoted $\Sigma _{n}^{0}$ and $\Pi _{n}^{0}$ for natural numbers *n* (including 0). The Greek letters here are lightface symbols, which indicates that the formulas do not contain set parameters.

If a formula $\phi$ is logically equivalent to a formula having no unbounded quantifiers, i.e. in which all quantifiers are bounded quantifiers then $\phi$ is assigned the classifications $\Sigma _{0}^{0}$ and $\Pi _{0}^{0}$ .

The classifications $\Sigma _{n}^{0}$ and $\Pi _{n}^{0}$ are defined inductively for every natural number *n* using the following rules:

- If $\phi$ is logically equivalent to a formula of the form $\exists m_{1}\exists m_{2}\cdots \exists m_{k}\psi$ , where $\psi$ is $\Pi _{n}^{0}$ , then $\phi$ is assigned the classification $\Sigma _{n+1}^{0}$ .
- If $\phi$ is logically equivalent to a formula of the form $\forall m_{1}\forall m_{2}\cdots \forall m_{k}\psi$ , where $\psi$ is $\Sigma _{n}^{0}$ , then $\phi$ is assigned the classification $\Pi _{n+1}^{0}$ .

A $\Sigma _{n}^{0}$ formula is equivalent to a formula that begins with some existential quantifiers and alternates $n-1$ times between series of existential and universal quantifiers; while a $\Pi _{n}^{0}$ formula is equivalent to a formula that begins with some universal quantifiers and alternates analogously.

Because every first-order formula has a prenex normal form, every formula is assigned at least one classification. Because redundant quantifiers can be added to any formula, once a formula is assigned the classification $\Sigma _{n}^{0}$ or $\Pi _{n}^{0}$ it will be assigned the classifications $\Sigma _{m}^{0}$ and $\Pi _{m}^{0}$ for every *m* > *n*. The only relevant classification assigned to a formula is thus the one with the least *n*; all the other classifications can be determined from it.

## The arithmetical hierarchy of sets of natural numbers

A set *X* of natural numbers is defined by a formula *φ* in the language of Peano arithmetic (the first-order language with symbols "0" for zero, "S" for the successor function, "+" for addition, "×" for multiplication, and "=" for equality), if the elements of *X* are exactly the numbers that satisfy *φ*. That is, for all natural numbers *n*,

$n\in X\Leftrightarrow \mathbb {N} \models \varphi ({\underline {n}}),$

where ${\underline {n}}$ is the numeral in the language of arithmetic corresponding to n . A set is definable in first-order arithmetic if it is defined by some formula in the language of Peano arithmetic.

Each set *X* of natural numbers that is definable in first-order arithmetic is assigned classifications of the form $\Sigma _{n}^{0}$ , $\Pi _{n}^{0}$ , and $\Delta _{n}^{0}$ , where n is a natural number, as follows. If *X* is definable by a $\Sigma _{n}^{0}$ formula then *X* is assigned the classification $\Sigma _{n}^{0}$ . If *X* is definable by a $\Pi _{n}^{0}$ formula then *X* is assigned the classification $\Pi _{n}^{0}$ . If *X* is both $\Sigma _{n}^{0}$ and $\Pi _{n}^{0}$ then X is assigned the additional classification $\Delta _{n}^{0}$ .

It rarely makes sense to speak of $\Delta _{n}^{0}$ *formulas*; the first quantifier of a formula is either existential or universal. So a $\Delta _{n}^{0}$ set is not necessarily defined by a $\Delta _{n}^{0}$ formula in the sense of a formula that is both $\Sigma _{n}^{0}$ and $\Pi _{n}^{0}$ ; rather, there are both $\Sigma _{n}^{0}$ and $\Pi _{n}^{0}$ formulas that define the set. For example, the set of odd natural numbers n is definable by either $\forall k(n\neq 2\times k)$ or $\exists k(n=2\times k+1)$ .

A parallel definition is used to define the arithmetical hierarchy on finite Cartesian powers of the set of natural numbers. Instead of formulas with one free variable, formulas with *k* free first-order variables are used to define the arithmetical hierarchy on sets of *k*-tuples of natural numbers. These are in fact related by the use of a pairing function.

## Meaning of the notation

The following meanings can be attached to the notation for the arithmetical hierarchy on formulas.

The subscript n in the symbols $\Sigma _{n}^{0}$ and $\Pi _{n}^{0}$ indicates the number of alternations of blocks of universal and existential first-order quantifiers that are used in a formula. Moreover, the outermost block is existential in $\Sigma _{n}^{0}$ formulas and universal in $\Pi _{n}^{0}$ formulas.

The superscript 0 in the symbols $\Sigma _{n}^{0}$ , $\Pi _{n}^{0}$ , and $\Delta _{n}^{0}$ indicates the type of the objects being quantified over. Type 0 objects are natural numbers, and objects of type $i+1$ are functions that map the set of objects of type i to the natural numbers. Quantification over higher type objects, such as functions from natural numbers to natural numbers, is described by a superscript greater than 0, as in the analytical hierarchy. The superscript 0 indicates quantifiers over numbers, the superscript 1 would indicate quantification over functions from numbers to numbers (type 1 objects), the superscript 2 would correspond to quantification over functions that take a type 1 object and return a number, and so on.

## Examples

- The $\Sigma _{1}^{0}$ sets of numbers are those definable by a formula of the form $\exists n_{1}\cdots \exists n_{k}\psi (n_{1},\ldots ,n_{k},m)$ where $\psi$ has only bounded quantifiers. These are exactly the recursively enumerable sets.
- The set of natural numbers that are indices for Turing machines that compute total functions is $\Pi _{2}^{0}$ . Intuitively, an index e falls into this set if and only if for every m "there is an s such that the Turing machine with index e halts on input m after s steps". A complete proof would show that the property displayed in quotes in the previous sentence is definable in the language of Peano arithmetic by a $\Sigma _{1}^{0}$ formula.
- Every $\Sigma _{1}^{0}$ subset of Baire space or Cantor space is an open set in the usual topology on the space. Moreover, for any such set there is a computable enumeration of Gödel numbers of basic open sets whose union is the original set. For this reason, $\Sigma _{1}^{0}$ sets are sometimes called *effectively open*. Similarly, every $\Pi _{1}^{0}$ set is closed and the $\Pi _{1}^{0}$ sets are sometimes called *effectively closed*.
- Every arithmetical subset of Cantor space or Baire space is a Borel set. The lightface Borel hierarchy extends the arithmetical hierarchy to include additional Borel sets. For example, every $\Pi _{2}^{0}$ subset of Cantor or Baire space is a $G_{\delta }$ set, that is, a set that equals the intersection of countably many open sets. Moreover, each of these open sets is $\Sigma _{1}^{0}$ and the list of Gödel numbers of these open sets has a computable enumeration. If $\phi (X,n,m)$ is a $\Sigma _{0}^{0}$ formula with a free set variable X and free number variables $n,m$ then the $\Pi _{2}^{0}$ set $\{X\mid \forall n\exists m\phi (X,n,m)\}$ is the intersection of the $\Sigma _{1}^{0}$ sets of the form $\{X\mid \exists m\phi (X,n,m)\}$ as n ranges over the set of natural numbers.
- The $\Sigma _{0}^{0}=\Pi _{0}^{0}=\Delta _{0}^{0}$ formulas can be checked by going over all cases one by one, which is possible because all their quantifiers are bounded. The time for this is polynomial in their arguments (e.g. polynomial in n for $\varphi (n)$ ); thus their corresponding decision problems are included in E (as n is exponential in its number of bits). This no longer holds under alternative definitions of $\Sigma _{0}^{0}=\Pi _{0}^{0}=\Delta _{0}^{0}$ that allow the use of primitive recursive functions, as now the quantifiers may be bounded by any primitive recursive function of the arguments.
- The $\Sigma _{0}^{0}=\Pi _{0}^{0}=\Delta _{0}^{0}$ formulas under an alternative definition, that allows the use of primitive recursive functions with bounded quantifiers, correspond to sets of natural numbers of the form $\{n:f(n)=0\}$ for a primitive recursive function f . This is because allowing bounded quantifier adds nothing to the definition: for a primitive recursive f , $\forall k<n:f(k)=0$ is the same as $f(0)+f(1)+...+f(n-1)=0$ , and $\exists k<n:f(k)=0$ is the same as $f(0)\cdot f(1)\cdot \ldots \cdot f(n-1)=0$ ; with course-of-values recursion each of these can be defined by a single primitive recursive function.

## Relativized arithmetical hierarchies

Just as we can define what it means for a set *X* to be recursive relative to another set *Y* by allowing the computation defining *X* to consult *Y* as an oracle we can extend this notion to the whole arithmetic hierarchy and define what it means for *X* to be $\Sigma _{n}^{0}$ , $\Delta _{n}^{0}$ or $\Pi _{n}^{0}$ in *Y*, denoted respectively $\Sigma _{n}^{0,Y}$ , $\Delta _{n}^{0,Y}$ and $\Pi _{n}^{0,Y}$ . To do so, fix a set of natural numbers *Y* and add a predicate for membership of *Y* to the language of Peano arithmetic. We then say that *X* is in $\Sigma _{n}^{0,Y}$ if it is defined by a $\Sigma _{n}^{0}$ formula in this expanded language. In other words, *X* is $\Sigma _{n}^{0,Y}$ if it is defined by a $\Sigma _{n}^{0}$ formula allowed to ask questions about membership of *Y*. Alternatively one can view the $\Sigma _{n}^{0,Y}$ sets as those sets that can be built starting with sets recursive in *Y* and alternately taking unions and intersections of these sets up to *n* times.

For example, let *Y* be a set of natural numbers. Let *X* be the set of numbers divisible by an element of *Y*. Then *X* is defined by the formula $\phi (n)=\exists m\exists t(Y(m)\land m\times t=n)$ so *X* is in $\Sigma _{1}^{0,Y}$ (actually it is in $\Delta _{0}^{0,Y}$ as well, since we could bound both quantifiers by *n*).

## Arithmetic reducibility and degrees

Arithmetical reducibility is an intermediate notion between Turing reducibility and hyperarithmetic reducibility.

A set is **arithmetical** (also **arithmetic** and **arithmetically definable**) if it is defined by some formula in the language of Peano arithmetic. Equivalently *X* is arithmetical if *X* is $\Sigma _{n}^{0}$ or $\Pi _{n}^{0}$ for some natural number *n*. A set *X* **is arithmetical in** a set *Y*, denoted $X\leq _{A}Y$ , if *X* is definable as some formula in the language of Peano arithmetic extended by a predicate for membership of *Y*. Equivalently, *X* is arithmetical in *Y* if *X* is in $\Sigma _{n}^{0,Y}$ or $\Pi _{n}^{0,Y}$ for some natural number *n*. A synonym for $X\leq _{A}Y$ is: *X* is **arithmetically reducible** to *Y*.

The relation $X\leq _{A}Y$ is reflexive and transitive, and thus the relation $\equiv _{A}$ defined by the rule

$X\equiv _{A}Y\iff X\leq _{A}Y\land Y\leq _{A}X$

is an equivalence relation. The equivalence classes of this relation are called the **arithmetic degrees**; they are partially ordered under $\leq _{A}$ .

## The arithmetical hierarchy of subsets of Cantor and Baire space

The Cantor space, denoted $2^{\omega }$ , is the set of all infinite sequences of 0s and 1s; the Baire space, denoted $\omega ^{\omega }$ or ${\mathcal {N}}$ , is the set of all infinite sequences of natural numbers. Note that elements of the Cantor space can be identified with sets of natural numbers and elements of the Baire space with functions from natural numbers to natural numbers.

The ordinary axiomatization of second-order arithmetic uses a set-based language in which the set quantifiers can naturally be viewed as quantifying over Cantor space. A subset of Cantor space is assigned the classification $\Sigma _{n}^{0}$ if it is definable by a $\Sigma _{n}^{0}$ formula. The set is assigned the classification $\Pi _{n}^{0}$ if it is definable by a $\Pi _{n}^{0}$ formula. If the set is both $\Sigma _{n}^{0}$ and $\Pi _{n}^{0}$ then it is given the additional classification $\Delta _{n}^{0}$ . For example, let $O\subseteq 2^{\omega }$ be the set of all infinite binary strings that aren't all 0 (or equivalently the set of all non-empty sets of natural numbers). As $O=\{X\in 2^{\omega }|\exists n(X(n)=1)\}$ we see that O is defined by a $\Sigma _{1}^{0}$ formula and hence is a $\Sigma _{1}^{0}$ set.

Note that while both the elements of the Cantor space (regarded as sets of natural numbers) and subsets of the Cantor space are classified in arithmetic hierarchies, these are not the same hierarchy. In fact the relationship between the two hierarchies is interesting and non-trivial. For instance the $\Pi _{n}^{0}$ elements of the Cantor space are not (in general) the same as the elements X of the Cantor space so that $\{X\}$ is a $\Pi _{n}^{0}$ subset of the Cantor space. However, many interesting results relate the two hierarchies.

There are two ways that a subset of Baire space can be classified in the arithmetical hierarchy.

- A subset of Baire space has a corresponding subset of Cantor space under the map that takes each function from $\omega$ to $\omega$ to the characteristic function of its graph. A subset of Baire space is given the classification $\Sigma _{n}^{0}$ , $\Pi _{n}^{0}$ , or $\Delta _{n}^{0}$ if and only if the corresponding subset of Cantor space has the same classification.
- An equivalent definition of the arithmetical hierarchy on Baire space is given by defining the arithmetical hierarchy of formulas using a functional version of second-order arithmetic; then the arithmetical hierarchy on subsets of Cantor space can be defined from the hierarchy on Baire space. This alternate definition gives exactly the same classifications as the first definition.

A parallel definition is used to define the arithmetical hierarchy on finite Cartesian powers of Baire space or Cantor space, using formulas with several free variables. The arithmetical hierarchy can be defined on any effective Polish space; the definition is particularly simple for Cantor space and Baire space because they fit with the language of ordinary second-order arithmetic.

Note that we can also define the arithmetic hierarchy of subsets of the Cantor and Baire spaces relative to some set of natural numbers. In fact boldface $\mathbf {\Sigma } _{n}^{0}$ is just the union of $\Sigma _{n}^{0,Y}$ for all sets of natural numbers *Y*. Note that the boldface hierarchy is just the standard hierarchy of Borel sets.

## Extensions and variations

It is possible to define the arithmetical hierarchy of formulas using a language extended with a function symbol for each primitive recursive function. This variation slightly changes the classification of $\Sigma _{0}^{0}=\Pi _{0}^{0}=\Delta _{0}^{0}$ , since using primitive recursive functions in first-order Peano arithmetic requires, in general, an unbounded existential quantifier, and thus some sets that are in $\Sigma _{0}^{0}$ by this definition are strictly in $\Sigma _{1}^{0}$ by the definition given in the beginning of this article. The class $\Sigma _{1}^{0}$ and thus all higher classes in the hierarchy remain unaffected.

A more semantic variation of the hierarchy can be defined on all finitary relations on the natural numbers; the following definition is used. Every computable relation is defined to be $\Sigma _{0}^{0}=\Pi _{0}^{0}=\Delta _{0}^{0}$ . The classifications $\Sigma _{n}^{0}$ and $\Pi _{n}^{0}$ are defined inductively with the following rules.

- If the relation $R(n_{1},\ldots ,n_{l},m_{1},\ldots ,m_{k})\,$ is $\Sigma _{n}^{0}$ then the relation $S(n_{1},\ldots ,n_{l})=\forall m_{1}\cdots \forall m_{k}R(n_{1},\ldots ,n_{l},m_{1},\ldots ,m_{k})$ is defined to be $\Pi _{n+1}^{0}$
- If the relation $R(n_{1},\ldots ,n_{l},m_{1},\ldots ,m_{k})\,$ is $\Pi _{n}^{0}$ then the relation $S(n_{1},\ldots ,n_{l})=\exists m_{1}\cdots \exists m_{k}R(n_{1},\ldots ,n_{l},m_{1},\ldots ,m_{k})$ is defined to be $\Sigma _{n+1}^{0}$

This variation slightly changes the classification of some sets. In particular, $\Sigma _{0}^{0}=\Pi _{0}^{0}=\Delta _{0}^{0}$ , as a class of sets (definable by the relations in the class), is identical to $\Delta _{1}^{0}$ as the latter was formerly defined. It can be extended to cover finitary relations on the natural numbers, Baire space, and Cantor space.

## Properties

The following properties hold for the arithmetical hierarchy of sets of natural numbers and the arithmetical hierarchy of subsets of Cantor or Baire space.

- The collections $\Pi _{n}^{0}$ and $\Sigma _{n}^{0}$ are closed under finite unions and finite intersections of their respective elements.
- A set is $\Sigma _{n}^{0}$ if and only if its complement is $\Pi _{n}^{0}$ . A set is $\Delta _{n}^{0}$ if and only if the set is both $\Sigma _{n}^{0}$ and $\Pi _{n}^{0}$ , in which case its complement will also be $\Delta _{n}^{0}$ .
- The inclusions $\Pi _{n}^{0}\subsetneq \Pi _{n+1}^{0}$ and $\Sigma _{n}^{0}\subsetneq \Sigma _{n+1}^{0}$ hold for all n . Thus the hierarchy does not collapse. This is a direct consequence of Post's theorem.
- The inclusions $\Delta _{n}^{0}\subsetneq \Pi _{n}^{0}$ , $\Delta _{n}^{0}\subsetneq \Sigma _{n}^{0}$ and $\Sigma _{n}^{0}\cup \Pi _{n}^{0}\subsetneq \Delta _{n+1}^{0}$ hold for $n\geq 1$ .

- For example, for a universal Turing machine *T*, the set of pairs (*n*,*m*) such that *T* halts on *n* but not on *m*, is in $\Delta _{2}^{0}$ (being computable with an oracle to the halting problem) but not in $\Sigma _{1}^{0}\cup \Pi _{1}^{0}$ .
- $\Sigma _{0}^{0}=\Pi _{0}^{0}=\Delta _{0}^{0}=\Sigma _{0}^{0}\cup \Pi _{0}^{0}\subseteq \Delta _{1}^{0}$ . The inclusion is strict by the definition given in this article, but an identity with $\Delta _{1}^{0}$ holds under one of the variations of the definition given above.

## Relation to Turing machines

### Computable sets

If *S* is a Turing computable set, then both *S* and its complement are recursively enumerable (if *T* is a Turing machine giving 1 for inputs in *S* and 0 otherwise, we may build a Turing machine halting only on the former, and another halting only on the latter).

By Post's theorem, both *S* and its complement are in $\Sigma _{1}^{0}$ . This means that *S* is both in $\Sigma _{1}^{0}$ and in $\Pi _{1}^{0}$ , and hence it is in $\Delta _{1}^{0}$ .

Similarly, for every set *S* in $\Delta _{1}^{0}$ , both *S* and its complement are in $\Sigma _{1}^{0}$ and are therefore (by Post's theorem) recursively enumerable by some Turing machines *T*1 and *T*2, respectively. For every number *n*, exactly one of these halts. We may therefore construct a Turing machine *T* that alternates between *T*1 and *T*2, halting and returning 1 when the former halts or halting and returning 0 when the latter halts. Thus *T* halts on every *n* and returns whether it is in *S*; so *S* is computable.

### Summary of main results

The Turing computable sets of natural numbers are exactly the sets at level $\Delta _{1}^{0}$ of the arithmetical hierarchy. The recursively enumerable sets are exactly the sets at level $\Sigma _{1}^{0}$ .

No oracle machine is capable of solving its own halting problem (a variation of Turing's proof applies). The halting problem for a $\Delta _{n}^{0,Y}$ oracle in fact sits in $\Sigma _{n+1}^{0,Y}$ .

Post's theorem establishes a close connection between the arithmetical hierarchy of sets of natural numbers and the Turing degrees. In particular, it establishes the following facts for all *n* ≥ 1:

- The set $\emptyset ^{(n)}$ (the *n*th Turing jump of the empty set) is many-one complete in $\Sigma _{n}^{0}$ .
- The set $\mathbb {N} \setminus \emptyset ^{(n)}$ is many-one complete in $\Pi _{n}^{0}$ .
- The set $\emptyset ^{(n-1)}$ is Turing complete in $\Delta _{n}^{0}$ .

The polynomial hierarchy is a "feasible resource-bounded" version of the arithmetical hierarchy in which polynomial length bounds are placed on the numbers involved (or, equivalently, polynomial time bounds are placed on the Turing machines involved). It gives a finer classification of some sets of natural numbers that are at level $\Delta _{1}^{0}$ of the arithmetical hierarchy.

## Relation to other hierarchies

|   |   |   |   |
|---|---|---|---|
| Lightface | Boldface |   |   |
| Σ0 0 = Π0 0 = Δ0 0 (sometimes the same as Δ0 1) | **Σ0 0** = **Π0 0** = **Δ0 0** (if defined) |   |   |
| Δ0 1 = recursive | **Δ0 1** = clopen |   |   |
| Σ0 1 = recursively enumerable | Π0 1 = co-recursively enumerable | **Σ0 1** = *G* = open | **Π0 1** = *F* = closed |
| Δ0 2 | **Δ0 2** |   |   |
| Σ0 2 | Π0 2 | **Σ0 2** = *F*σ | **Π0 2** = *G*δ |
| Δ0 3 | **Δ0 3** |   |   |
| Σ0 3 | Π0 3 | **Σ0 3** = *G*δσ | **Π0 3** = *F*σδ |
| ⋮ | ⋮ |   |   |
| Σ0 <ω = Π0 <ω = Δ0 <ω = Σ1 0 = Π1 0 = Δ1 0 = arithmetical | **Σ0 <ω** = **Π0 <ω** = **Δ0 <ω** = **Σ1 0** = **Π1 0** = **Δ1 0** = boldface arithmetical |   |   |
| ⋮ | ⋮ |   |   |
| Δ0 α (α recursive) | **Δ0 α** (α countable) |   |   |
| Σ0 α | Π0 α | **Σ0 α** | **Π0 α** |
| ⋮ | ⋮ |   |   |
| Σ0 ωCK 1 = Π0 ωCK 1 = Δ0 ωCK 1 = Δ1 1 = hyperarithmetical | **Σ0 ω1** = **Π0 ω1** = **Δ0 ω1** = **Δ1 1** = **B** = Borel |   |   |
| Σ1 1 = lightface analytic | Π1 1 = lightface coanalytic | **Σ1 1** = A = analytic | **Π1 1** = CA = coanalytic |
| Δ1 2 | **Δ1 2** |   |   |
| Σ1 2 | Π1 2 | **Σ1 2** = PCA | **Π1 2** = CPCA |
| Δ1 3 | **Δ1 3** |   |   |
| Σ1 3 | Π1 3 | **Σ1 3** = PCPCA | **Π1 3** = CPCPCA |
| ⋮ | ⋮ |   |   |
| Σ1 <ω = Π1 <ω = Δ1 <ω = Σ2 0 = Π2 0 = Δ2 0 = analytical | **Σ1 <ω** = **Π1 <ω** = **Δ1 <ω** = **Σ2 0** = **Π2 0** = **Δ2 0** = **P** = projective |   |   |
| ⋮ | ⋮ |   |   |
