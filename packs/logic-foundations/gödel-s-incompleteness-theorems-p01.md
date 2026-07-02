---
title: "Gödel's incompleteness theorems (part 1/2)"
source: https://en.wikipedia.org/wiki/G%C3%B6del's_incompleteness_theorems
domain: logic-foundations
license: CC-BY-SA-4.0
tags: propositional logic, first-order logic, boolean algebra, truth table, mathematical proof
fetched: 2026-07-02
part: 1/2
---

# Gödel's incompleteness theorems

Checked


## Page version status

This is an accepted version of this page

This is the

latest accepted revision

,

reviewed

on

28 June 2026

.

**Gödel's incompleteness theorems** are two theorems of mathematical logic that are concerned with the limits of provability in formal axiomatic theories. These results, published by Kurt Gödel in 1931, are important both in mathematical logic and in philosophy of mathematics. The theorems are interpreted as showing that Hilbert's program to find a complete and consistent set of axioms for all mathematics is impossible.

The first incompleteness theorem states that no consistent system of axioms whose theorems can be listed by an effective procedure (i.e. an algorithm) is capable of proving all truths about the arithmetic of natural numbers. For any such consistent formal system, there will always be statements about natural numbers that are true, but that are unprovable within the system. Equivalently, there will always be statements about natural numbers that are false, but that cannot be proved false within the system.

The second incompleteness theorem, an extension of the first, shows that no such system can demonstrate its own consistency.

Employing a diagonal argument, Gödel's incompleteness theorems were among the first of several closely related theorems on the limitations of formal systems. They were followed by Tarski's undefinability theorem on the formal undefinability of truth, Church's proof that Hilbert's *Entscheidungsproblem* is unsolvable, and Turing's theorem that there is no algorithm to solve the halting problem.


## Formal systems

The incompleteness theorems apply to formal systems that are of sufficient complexity to express the basic arithmetic of the natural numbers and which are consistent and effectively axiomatized. Particularly in the context of first-order logic, formal systems are also called *formal theories*. In general, a formal system is a deductive apparatus that consists of a particular set of axioms along with rules of symbolic manipulation (or rules of inference) that allow for the derivation of new theorems from the axioms. One example of such a system is first-order Peano arithmetic, a system in which all variables are intended to denote natural numbers. In other systems, such as set theory, only some sentences of the formal system express statements about the natural numbers. The incompleteness theorems are about formal provability *within* these systems, rather than about "provability" in an informal sense.

There are several properties that a formal system may have, including completeness, consistency, and the existence of an effective axiomatization. The incompleteness theorems show that systems which contain a sufficient amount of arithmetic cannot possess all three of these properties.

### Effective axiomatization

A formal system is said to be *effectively axiomatized* (also called *effectively generated*) if its set of theorems is recursively enumerable. This means that there is a computer program that, in principle, could enumerate all the theorems of the system without listing any statements that are not theorems. Examples of effectively generated theories include Peano arithmetic and Zermelo–Fraenkel set theory (ZFC).

The theory known as true arithmetic consists of all true statements about the standard integers in the language of Peano arithmetic. This theory is consistent and complete, and contains a sufficient amount of arithmetic. However, it does not have a recursively enumerable set of axioms, and thus does not satisfy the hypotheses of the incompleteness theorems.

### Completeness

A set of axioms is (*syntactically*, or *negation*-) complete if, for any statement in the axioms' language, that statement or its negation is provable from the axioms. This is the notion relevant for Gödel's first Incompleteness theorem. It is not to be confused with *semantic* completeness, which means that the set of axioms proves all the semantic tautologies of the given language. In his completeness theorem (not to be confused with the incompleteness theorems described here), Gödel proved that first-order logic is *semantically* complete. But it is not syntactically complete, since there are sentences expressible in the language of first-order logic that can be neither proved nor disproved from the axioms of logic alone.

In a system of mathematics, thinkers such as Hilbert believed that it was just a matter of time to find such an axiomatization that would allow one to either prove or disprove (by proving its negation) every mathematical formula.

A formal system might be syntactically incomplete by design, as logics generally are. Or it may be incomplete simply because not all the necessary axioms have been discovered or included. For example, Euclidean geometry without the parallel postulate is incomplete, because some statements in the language (such as the parallel postulate itself) can not be proved from the remaining axioms. Similarly, the theory of dense linear orders is not complete, but becomes complete with an extra axiom stating that there are no endpoints in the order. The continuum hypothesis is a statement in the language of ZFC that is not provable within ZFC, so ZFC is not complete. In this case, there is no obvious candidate for a new axiom that resolves the issue.

The theory of first-order Peano arithmetic seems consistent. Assuming this is indeed the case, note that it has an infinite but recursively enumerable set of axioms, and can encode enough arithmetic for the hypotheses of the incompleteness theorem. Thus by the first incompleteness theorem, Peano Arithmetic is not complete. The theorem gives an explicit example of a statement of arithmetic that is neither provable nor disprovable in Peano's arithmetic. Moreover, this statement is true in the usual model. In addition, no effectively axiomatized, consistent extension of Peano arithmetic can be complete.

### Consistency

A set of axioms is (simply) consistent if there is no statement such that both the statement and its negation are provable from the axioms, and *inconsistent* otherwise. That is to say, a consistent axiomatic system is one that is free from contradiction.

Peano arithmetic is provably consistent from ZFC, but not from within itself. Similarly, ZFC is not provably consistent from within itself, but ZFC + "there exists an inaccessible cardinal" proves ZFC is consistent because if κ is the least such cardinal, then *V*κ sitting inside the von Neumann universe is a model of ZFC, and a theory is consistent if and only if it has a model.

If one takes all statements in the language of Peano arithmetic as axioms, then this theory is complete, has a recursively enumerable set of axioms, and can describe addition and multiplication. However, it is not consistent.

Additional examples of inconsistent theories arise from the paradoxes that result when the axiom schema of unrestricted comprehension is assumed in set theory.

### Systems which contain arithmetic

The incompleteness theorems apply only to formal systems which are able to prove a sufficient collection of facts about the natural numbers. One sufficient collection is the set of theorems of Robinson arithmetic Q. Some systems, such as Peano arithmetic, can directly express statements about natural numbers. Others, such as ZFC set theory, are able to interpret statements about natural numbers into their language. Either of these options is appropriate for the incompleteness theorems.

The theory of algebraically closed fields of a given characteristic is complete, consistent, and has an infinite but recursively enumerable set of axioms. However it is not possible to encode the integers into this theory, and the theory cannot describe arithmetic of integers. A similar example is the theory of real closed fields, which is essentially equivalent to Tarski's axioms for Euclidean geometry. So Euclidean geometry itself (in Tarski's formulation) is an example of a complete, consistent, effectively axiomatized theory.

The system of Presburger arithmetic consists of a set of axioms for the natural numbers with just the addition operation (multiplication is omitted). Presburger arithmetic is complete, consistent, and recursively enumerable and can encode addition but not multiplication of natural numbers, showing that for Gödel's theorems one needs the theory to encode not just addition but also multiplication.

Dan Willard (2001) has studied some weak families of arithmetic systems which allow enough arithmetic as relations to formalise Gödel numbering, but which are not strong enough to have multiplication as a function, and so fail to prove the second incompleteness theorem; that is to say, these systems are consistent and capable of proving their own consistency (see self-verifying theories).

### Conflicting goals

In choosing a set of axioms, one goal is to be able to prove as many correct results as possible, without proving any incorrect results. For example, we could imagine a set of true axioms which allow us to prove every true arithmetical claim about the natural numbers (Smith 2007, p. 2). In the standard system of first-order logic, an inconsistent set of axioms will prove every statement in its language (this is sometimes called the principle of explosion), and is thus automatically complete. A set of axioms that is both complete and consistent, however, proves a maximal set of non-contradictory theorems.

The pattern illustrated in the previous sections with Peano arithmetic, ZFC, and ZFC + "there exists an inaccessible cardinal" cannot generally be broken. Here ZFC + "there exists an inaccessible cardinal" cannot from itself, be proved consistent. It is also not complete, as illustrated by the continuum hypothesis, which is unresolvable in ZFC + "there exists an inaccessible cardinal".

The first incompleteness theorem shows that, in formal systems that can express basic arithmetic, a complete and consistent finite list of axioms can never be created: each time an additional, consistent statement is added as an axiom, there are other true statements that still cannot be proved, even with the new axiom. If an axiom is ever added that makes the system complete, it does so at the cost of making the system inconsistent. It is not even possible for an infinite list of axioms to be complete, consistent, and effectively axiomatized.


## First incompleteness theorem

**Gödel's first incompleteness theorem** first appeared as "Theorem VI" in Gödel's 1931 paper "On Formally Undecidable Propositions of Principia Mathematica and Related Systems I". The hypotheses of the theorem were improved shortly thereafter by J. Barkley Rosser (1936) using Rosser's trick. The resulting theorem (incorporating Rosser's improvement) may be paraphrased in English as follows, where "formal system" includes the assumption that the system is effectively generated.

> **First Incompleteness Theorem**: "Any consistent formal system F within which a certain amount of elementary arithmetic can be carried out is incomplete; i.e. there are statements of the language of F which can neither be proved nor disproved in F." (Raatikainen 2020)

The unprovable statement *G**F* referred to by the theorem is often referred to as "the Gödel sentence" for the system F. The proof constructs a particular Gödel sentence for the system F, but there are infinitely many statements in the language of the system that share the same properties, such as the conjunction of the Gödel sentence and any logically valid sentence.

Each effectively generated system has its own Gödel sentence. It is possible to define a larger system F' that contains the whole of F plus *G**F* as an additional axiom. This will not result in a complete system, because Gödel's theorem will also apply to F', and thus F' also cannot be complete. In this case, *G**F* is indeed a theorem in F', because it is an axiom. Because *G**F* states only that it is not provable in F, no contradiction is presented by its provability within F'. However, because the incompleteness theorem applies to F', there will be a new Gödel statement *G**F* ' for F', showing that F' is also incomplete. *G**F* ' will differ from *G**F* in that *G**F* ' will refer to F', rather than F.

### Syntactic form of the Gödel sentence

The Gödel sentence is designed to refer, indirectly, to itself. The sentence states that, when a particular sequence of steps is used to construct another sentence, that constructed sentence will not be provable in F. However, the sequence of steps is such that the constructed sentence turns out to be *G**F* itself. In this way, the Gödel sentence *G**F* indirectly states its own unprovability within F.

To prove the first incompleteness theorem, Gödel demonstrated that the notion of provability within a system could be expressed purely in terms of arithmetical functions that operate on Gödel numbers of sentences of the system. Therefore, the system, which can prove certain facts about numbers, can also indirectly prove facts about its own statements, provided that it is effectively generated. Questions about the provability of statements within the system are represented as questions about the arithmetical properties of numbers themselves, which would be decidable by the system if it were complete.

Thus, although the Gödel sentence refers indirectly to sentences of the system F, when read as an arithmetical statement the Gödel sentence directly refers only to natural numbers. It asserts that no natural number has a particular property, where that property is given by a primitive recursive relation (Smith 2007, p. 141). As such, the Gödel sentence can be written in the language of arithmetic with a simple syntactic form. In particular, it can be expressed as a formula in the language of arithmetic consisting of a number of leading universal quantifiers followed by a quantifier-free body (these formulas are at level $\Pi _{1}^{0}$ of the arithmetical hierarchy). Via the MRDP theorem, the Gödel sentence can be re-written as a statement that a particular polynomial in many variables with integer coefficients never takes the value zero when integers are substituted for its variables (Franzén 2005, p. 71).

### Truth of the Gödel sentence

The first incompleteness theorem shows that the Gödel sentence *G**F* of an appropriate formal theory F is unprovable in F. Because, when interpreted as a statement about arithmetic, this unprovability is exactly what the sentence (indirectly) asserts, the Gödel sentence is, in fact, true (Smoryński 1977, p. 825; also see Franzén 2005, pp. 28–33). For this reason, the sentence *G**F* is often said to be "true but unprovable." (Raatikainen 2020). However, since the Gödel sentence cannot itself formally specify its intended interpretation, the truth of the sentence *G**F* may only be arrived at via a meta-analysis from outside the system. In general, this meta-analysis can be carried out within the weak formal system known as primitive recursive arithmetic, which proves the implication *Con*(*F*)→*G*F, where *Con*(*F*) is a canonical sentence asserting the consistency of F (Smoryński 1977, p. 840, Kikuchi & Tanaka 1994, p. 403).

Although the Gödel sentence of a consistent theory is true as a statement about the intended interpretation of arithmetic, the Gödel sentence will be false in some nonstandard models of arithmetic, as a consequence of Gödel's completeness theorem (Franzén 2005, p. 135). That theorem shows that, when a sentence is independent of a theory, the theory will have models in which the sentence is true and models in which the sentence is false. As described earlier, the Gödel sentence of a system F is an arithmetical statement which claims that no number exists with a particular property. The incompleteness theorem shows that this claim will be independent of the system F, and the truth of the Gödel sentence follows from the fact that no standard natural number has the property in question. Any model in which the Gödel sentence is false must contain some element which satisfies the property within that model. Such a model must be "nonstandard" – it must contain elements that do not correspond to any standard natural number (Raatikainen 2020, Franzén 2005, p. 135).

### Relationship with the liar paradox

Gödel specifically cites Richard's paradox and the liar paradox as semantical analogues to his syntactical incompleteness result in the introductory section of "On Formally Undecidable Propositions in Principia Mathematica and Related Systems I". The liar paradox is the sentence "This sentence is false." An analysis of the liar sentence shows that it cannot be true (for then, as it asserts, it is false), nor can it be false (for then, it is true). A Gödel sentence G for a system F makes a similar assertion to the liar sentence, but with truth replaced by provability: G says "G is not provable in the system F." The analysis of the truth and provability of G is a formalized version of the analysis of the truth of the liar sentence.

It is not possible to replace "not provable" with "false" in a Gödel sentence because the predicate "Q is the Gödel number of a false formula" cannot be represented as a formula of arithmetic. This result, known as Tarski's undefinability theorem, was discovered independently both by Gödel, when he was working on the proof of the incompleteness theorem, and by the theorem's namesake, Alfred Tarski.

### Extensions of Gödel's original result

Compared to the theorems stated in Gödel's 1931 paper, many contemporary statements of the incompleteness theorems are more general in two ways. These generalized statements are phrased to apply to a broader class of systems, and they are phrased to incorporate weaker consistency assumptions.

Gödel demonstrated the incompleteness of the system of *Principia Mathematica*, a particular system of arithmetic, but a parallel demonstration could be given for any effective system of a certain expressiveness. Gödel commented on this fact in the introduction to his paper, but restricted the proof to one system for concreteness. In modern statements of the theorem, it is common to state the effectiveness and expressiveness conditions as hypotheses for the incompleteness theorem, so that it is not limited to any particular formal system. The terminology used to state these conditions was not yet developed in 1931 when Gödel published his results.

Gödel's original statement and proof of the incompleteness theorem requires the assumption that the system is not just consistent but *ω-consistent*. A system is **ω-consistent** if it is not ω-inconsistent, and is ω-inconsistent if there is a predicate P such that for every specific natural number m the system proves ~*P*(*m*), and yet the system also proves that there exists a natural number n such that P(n). That is, the system says that a number with property P exists while denying that it has any specific value. The ω-consistency of a system implies its consistency, but consistency does not imply ω-consistency. J. Barkley Rosser (1936) strengthened the incompleteness theorem by finding a variation of the proof (Rosser's trick) that only requires the system to be consistent, rather than ω-consistent. This is mostly of technical interest, because all true formal theories of arithmetic (theories whose axioms are all true statements about natural numbers) are ω-consistent, and thus Gödel's theorem as originally stated applies to them. The stronger version of the incompleteness theorem that only assumes consistency, rather than ω-consistency, has become commonly known as Gödel's incompleteness theorem and as the Gödel–Rosser theorem.


## Second incompleteness theorem

For each formal system F containing basic arithmetic, it is possible to canonically define a formula Cons(F) expressing the consistency of F. This formula expresses the property that "there does not exist a natural number coding a formal derivation within the system F whose conclusion is a syntactic contradiction." The syntactic contradiction is often taken to be "0=1", in which case Cons(F) states "there is no natural number that codes a derivation of '0=1' from the axioms of F."

**Gödel's second incompleteness theorem** shows that, under general assumptions, this canonical consistency statement Cons(F) will not be provable in F. The theorem first appeared as "Theorem XI" in Gödel's 1931 paper "On Formally Undecidable Propositions in Principia Mathematica and Related Systems I". In the following statement, the term "formalized system" also includes an assumption that F is effectively axiomatized. This theorem states that for any consistent system *F* within which a certain amount of elementary arithmetic can be carried out, the consistency of *F* cannot be proved in *F* itself. This theorem is stronger than the first incompleteness theorem because the statement constructed in the first incompleteness theorem does not directly express the consistency of the system. The proof of the second incompleteness theorem is obtained by formalizing the proof of the first incompleteness theorem within the system F itself.

### Expressing consistency

There is a technical subtlety in the second incompleteness theorem regarding the method of expressing the consistency of F as a formula in the language of F. There are many ways to express the consistency of a system, and not all of them lead to the same result. The formula Cons(F) from the second incompleteness theorem is a particular expression of consistency.

Other formalizations of the claim that F is consistent may be inequivalent in F, and some may even be provable. For example, first-order Peano arithmetic (PA) can prove that "the largest consistent subset of PA" is consistent. But, because PA is consistent, the largest consistent subset of PA is just PA, so in this sense PA "proves that it is consistent". What PA does not prove is that the largest consistent subset of PA is, in fact, the whole of PA. (The term "largest consistent subset of PA" is meant here to be the largest consistent initial segment of the axioms of PA under some particular effective enumeration.)

### The Hilbert–Bernays conditions

The standard proof of the second incompleteness theorem assumes that the provability predicate *Prov*A(*P*) satisfies the Hilbert–Bernays provability conditions. Letting #(*P*) represent the Gödel number of a formula P, the provability conditions say:

1. If F proves P, then F proves *Prov*A(#(*P*)).
2. F proves 1.; that is, F proves *Prov*A(#(*P*)) → *Prov*A(#(*Prov*A(#(*P*)))).
3. F proves *Prov*A(#(*P* → *Q*)) ∧ *Prov*A(#(*P*)) → *Prov*A(#(*Q*))   (analogue of modus ponens).

There are systems, such as Robinson arithmetic, which are strong enough to meet the assumptions of the first incompleteness theorem, but which do not prove the Hilbert–Bernays conditions. Peano arithmetic, however, is strong enough to verify these conditions, as are all theories stronger than Peano arithmetic.

### Implications for consistency proofs

Gödel's second incompleteness theorem also implies that a system *F*1 satisfying the technical conditions outlined above cannot prove the consistency of any system *F*2 that proves the consistency of *F*1. This is because such a system *F*1 can prove that if *F*2 proves the consistency of *F*1, then *F*1 is in fact consistent. For the claim that *F*1 is consistent has form "for all numbers n, n has the decidable property of not being a code for a proof of contradiction in *F*1". If *F*1 were in fact inconsistent, then *F*2 would prove for some n that n is the code of a contradiction in *F*1. But if *F*2 also proved that *F*1 is consistent (that is, that there is no such n), then it would itself be inconsistent. This reasoning can be formalized in *F*1 to show that if *F*2 is consistent, then *F*1 is consistent. Since, by second incompleteness theorem, *F*1 does not prove its consistency, it cannot prove the consistency of *F*2 either.

This corollary of the second incompleteness theorem shows that there is no hope of proving, for example, the consistency of Peano arithmetic using any finitistic means that can be formalized in a system the consistency of which is provable in Peano arithmetic (PA). For example, the system of primitive recursive arithmetic (PRA), which is widely accepted as an accurate formalization of finitistic mathematics, is provably consistent in PA. Thus PRA cannot prove the consistency of PA. This fact is generally seen to imply that Hilbert's program, which aimed to justify the use of "ideal" (infinitistic) mathematical principles in the proofs of "real" (finitistic) mathematical statements by giving a finitistic proof that the ideal principles are consistent, cannot be carried out.

The corollary also indicates the epistemological relevance of the second incompleteness theorem. It would provide no interesting information if a system F proved its consistency. This is because inconsistent theories prove everything, including their consistency. Thus a consistency proof of F in F would give us no clue as to whether F is consistent; no doubts about the consistency of F would be resolved by such a consistency proof. The interest in consistency proofs lies in the possibility of proving the consistency of a system F in some system F' that is in some sense less doubtful than F itself, for example, weaker than F. For many naturally occurring theories F and F', such as F = Zermelo–Fraenkel set theory and F' = primitive recursive arithmetic, the consistency of F' is provable in F, and thus F' cannot prove the consistency of F by the above corollary of the second incompleteness theorem.

The second incompleteness theorem does not rule out altogether the possibility of proving the consistency of a different system with different axioms. For example, Gerhard Gentzen proved the consistency of Peano arithmetic in a different system that includes an axiom asserting that the ordinal called *ε*0 is wellfounded; see Gentzen's consistency proof. Gentzen's theorem spurred the development of ordinal analysis in proof theory.


## Examples of undecidable statements

There are two distinct senses of the word "undecidable" in mathematics and computer science. The first of these is the proof-theoretic sense used in relation to Gödel's theorems, that of a statement being neither provable nor refutable in a specified deductive system. The second sense, which will not be discussed here, is used in relation to computability theory and applies not to statements but to decision problems, which are countably infinite sets of questions each requiring a yes or no answer. Such a problem is said to be undecidable if there is no computable function that correctly answers every question in the problem set (see undecidable problem).

Because of the two meanings of the word undecidable, the term independent is sometimes used instead of undecidable for the "neither provable nor refutable" sense.

Undecidability of a statement in a particular deductive system does not, in and of itself, address the question of whether the truth value of the statement is well-defined, or whether it can be determined by other means. Undecidability only implies that the particular deductive system being considered does not prove the truth or falsity of the statement. Whether there exist so-called "absolutely undecidable" statements, whose truth value can never be known or is ill-specified, is a controversial point in the philosophy of mathematics.

The combined work of Gödel and Paul Cohen has given two concrete examples of undecidable statements (in the first sense of the term): The continuum hypothesis can neither be proved nor refuted in ZFC (the standard axiomatization of set theory), and the axiom of choice can neither be proved nor refuted in ZF (which is all the ZFC axioms *except* the axiom of choice). These results do not require the incompleteness theorem. Gödel proved in 1940 that neither of these statements could be disproved in ZF or ZFC set theory. In the 1960s, Cohen proved that neither is provable from ZF, and the continuum hypothesis cannot be proved from ZFC.

Shelah (1974) showed that the Whitehead problem in group theory is undecidable, in the first sense of the term, in standard set theory.

Gregory Chaitin produced undecidable statements in algorithmic information theory and proved another incompleteness theorem in that setting. Chaitin's incompleteness theorem states that for any system that can represent enough arithmetic, there is an upper bound c such that no specific number can be proved in that system to have Kolmogorov complexity greater than c. While Gödel's theorem is related to the liar paradox, Chaitin's result is related to Berry's paradox.

### Undecidable statements provable in larger systems

These are natural mathematical equivalents of the Gödel "true but undecidable" sentence. They can be proved in a larger system which is generally accepted as a valid form of reasoning, but are undecidable in a more limited system such as Peano Arithmetic.

In 1977, Paris and Harrington proved that the Paris–Harrington principle, a version of the infinite Ramsey theorem, is undecidable in (first-order) Peano arithmetic, but can be proved in the stronger system of second-order arithmetic. Kirby and Paris later showed that Goodstein's theorem, a statement about sequences of natural numbers somewhat simpler than the Paris–Harrington principle, is also undecidable in Peano arithmetic.

Kruskal's tree theorem, which has applications in computer science, is also undecidable from Peano arithmetic but provable in set theory. In fact Kruskal's tree theorem (or its finite form) is undecidable in a much stronger system ATR0 codifying the principles acceptable based on a philosophy of mathematics called predicativism. The related but more general graph minor theorem (2003) has consequences for computational complexity theory.


## Relationship with computability

The incompleteness theorem is closely related to several results about undecidable sets in recursion theory.

Kleene (1943) presented a proof of Gödel's incompleteness theorem using basic results of computability theory. One such result shows that the halting problem is undecidable: no computer program can correctly determine, given any program P as input, whether P eventually halts when run with a particular given input. Kleene showed that the existence of a complete effective system of arithmetic with certain consistency properties would force the halting problem to be decidable, a contradiction. This method of proof has also been presented by Shoenfield (1967); Charlesworth (1981); and Hopcroft & Ullman (1979).

Franzén (2005) explains how Matiyasevich's solution to Hilbert's 10th problem can be used to obtain a proof to Gödel's first incompleteness theorem. Matiyasevich proved that there is no algorithm that, given a multivariate polynomial *p*(*x*1, *x*2,...,*x*k) with integer coefficients, determines whether there is an integer solution to the equation p = 0. Because polynomials with integer coefficients, and integers themselves, are directly expressible in the language of arithmetic, if a multivariate integer polynomial equation p = 0 does have a solution in the integers then any sufficiently strong system of arithmetic T will prove this. Moreover, suppose the system T is ω-consistent. In that case, it will never prove that a particular polynomial equation has a solution when there is no solution in the integers. Thus, if T were complete and ω-consistent, it would be possible to determine algorithmically whether a polynomial equation has a solution by merely enumerating proofs of T until either "p has a solution" or "p has no solution" is found, in contradiction to Matiyasevich's theorem. Hence it follows that T cannot be ω-consistent and complete. Moreover, for each consistent effectively generated system T, it is possible to effectively generate a multivariate polynomial p over the integers such that the equation p = 0 has no solutions over the integers, but the lack of solutions cannot be proved in T.

Smoryński (1977) shows how the existence of recursively inseparable sets can be used to prove the first incompleteness theorem. This proof is often extended to show that systems such as Peano arithmetic are essentially undecidable.

Chaitin's incompleteness theorem gives a different method of producing independent sentences, based on Kolmogorov complexity. Like the proof presented by Kleene that was mentioned above, Chaitin's theorem only applies to theories with the additional property that all their axioms are true in the standard model of the natural numbers. Gödel's incompleteness theorem is distinguished by its applicability to consistent theories that nonetheless include false statements in the standard model; these theories are known as ω-inconsistent.


## Proof sketch for the first theorem

The proof by contradiction has three essential parts. To begin, choose a formal system that meets the proposed criteria:

1. Statements in the system can be represented by natural numbers (known as Gödel numbers). The significance of this is that properties of statements—such as their truth and falsehood—will be equivalent to determining whether their Gödel numbers have certain properties, and that properties of the statements can therefore be demonstrated by examining their Gödel numbers. This part culminates in the construction of a formula expressing the idea that *"statement S is provable in the system"* (which can be applied to any statement "S" in the system).
2. In the formal system it is possible to construct a number whose matching statement, when interpreted, is self-referential and essentially says that it (i.e. the statement itself) is unprovable. This is done using a technique called "diagonalization" (so-called because of its origins as Cantor's diagonal argument).
3. Within the formal system this statement permits a demonstration that it is neither provable nor disprovable in the system, and therefore the system cannot in fact be ω-consistent. Hence the original assumption that the proposed system met the criteria is false.

### Arithmetization of syntax

The main problem in fleshing out the proof just described is that it seems at first that to construct a statement p that is equivalent to "p cannot be proved", p would somehow have to contain a reference to p, which could easily give rise to an infinite regress. Gödel's technique is to show that statements can be matched with numbers (often called the arithmetization of syntax) in such a way that *"proving a statement"* can be replaced with *"testing whether a number has a given property"*. This allows a self-referential formula to be constructed in a way that avoids any infinite regress of definitions. The same technique was later used by Alan Turing in his work on the *Entscheidungsproblem*.

In simple terms, a method can be devised so that every formula or statement that can be formulated in the system gets a unique number, called its Gödel number, in such a way that it is possible to mechanically convert back and forth between formulas and Gödel numbers. The numbers involved might be very long indeed (in terms of number of digits), but this is not a barrier; all that matters is that such numbers can be constructed. A simple example is how English can be stored as a sequence of numbers for each letter and then combined into a single larger number:

- The word **`hello`** is encoded as 104-101-108-108-111 in ASCII, which can be converted into the number 104101108108111.
- The logical statement **`x=y => y=x`** is encoded as 120-061-121-032-061-062-032-121-061-120 in ASCII, which can be converted into the number 120061121032061062032121061120.

In principle, proving a statement true or false can be shown to be equivalent to proving that the number matching the statement does or does not have a given property. Because the formal system is strong enough to support reasoning about *numbers in general*, it can support reasoning about *numbers that represent formulae and statements* as well. Crucially, because the system can support reasoning about *properties of numbers*, the results are equivalent to reasoning about *provability of their equivalent statements*.

### Construction of a statement about "provability"

Having shown that in principle the system can indirectly make statements about provability, by analyzing properties of those numbers representing statements it is possible to show how to create a statement that actually does this.

A formula *F*(*x*) that contains exactly one free variable x is called a *statement form* or *class-sign*. As soon as x is replaced by a specific number, the statement form turns into a *bona fide* statement, and it is then either provable in the system, or not. For certain formulas one can show that for every natural number n, ⁠ $F(n)$ ⁠ is true if and only if it can be proved (the precise requirement in the original proof is weaker, but for the proof sketch this will suffice). In particular, this is true for every specific arithmetic operation between a finite number of natural numbers, such as "2 × 3 = 6".

Statement forms themselves are not statements and therefore cannot be proved or disproved. But every statement form *F*(*x*) can be assigned a Gödel number denoted by **G**(*F*). The choice of the free variable used in the form F(x) is not relevant to the assignment of the Gödel number **G**(*F*).

The notion of provability itself can also be encoded by Gödel numbers, in the following way: since a proof is a list of statements which obey certain rules, the Gödel number of a proof can be defined. Then, for every statement p, one may ask whether a number x is the Gödel number of its proof. The relation between the Gödel number of p and x, the potential Gödel number of its proof, is an arithmetical relation between two numbers. Therefore, there is a statement form *Bew*(*y*) that uses this arithmetical relation to state that a Gödel number of a proof of y exists:

Bew

(

y

) = ∃

x

(

y

is the Gödel number of a formula and

x

is the Gödel number of a proof of the formula encoded by

y

).

The name **Bew** is short for *beweisbar*, the German word for "provable"; this name was originally used by Gödel to denote the provability formula just described. Note that "*Bew*(*y*)" is merely an abbreviation that represents a particular, very long, formula in the original language of T; the string "Bew" itself is not claimed to be part of this language.

An important feature of the formula *Bew*(*y*) is that if a statement p is provable in the system then *Bew*(**G**(*p*)) is also provable. This is because any proof of p would have a corresponding Gödel number, the existence of which causes Bew(**G**(*p*)) to be satisfied.

### Diagonalization

The next step in the proof is to obtain a statement which, indirectly, asserts its own unprovability. Although Gödel constructed this statement directly, the existence of at least one such statement follows from the diagonal lemma, which says that for any sufficiently strong formal system and any statement form F there is a statement p such that the system proves

p

↔

F

(

G

(

p

))

.

By letting F be the negation of *Bew*(*x*), we obtain the theorem

p

↔ ~

Bew

(

G

(

p

))

and the p defined by this roughly states that its own Gödel number is the Gödel number of an unprovable formula.

The statement p is not literally equal to ~*Bew*(**G**(*p*)); rather, p states that if a certain calculation is performed, the resulting Gödel number will be that of an unprovable statement. But when this calculation is performed, the resulting Gödel number turns out to be the Gödel number of p itself. This is similar to the following sentence in English:

", when preceded by itself in quotes, is unprovable.", when preceded by itself in quotes, is unprovable.

This sentence does not directly refer to itself, but when the stated transformation is made the original sentence is obtained as a result, and thus this sentence indirectly asserts its own unprovability. The proof of the diagonal lemma employs a similar method.

Next, assume that the axiomatic system is ω-consistent, and let p be the statement obtained in the previous section.

If p were provable, then *Bew*(**G**(*p*)) would be provable, as argued above. But p asserts the negation of *Bew*(**G**(*p*)). Thus the system would be inconsistent, proving both a statement and its negation. This contradiction shows that p cannot be provable.

If the negation of p were provable, then *Bew*(**G**(*p*)) would be provable (because p was constructed to be equivalent to the negation of *Bew*(**G**(*p*))). However, for each specific number x, x cannot be the Gödel number of the proof of p, because p is not provable (from the previous paragraph). Thus on one hand the system proves there is a number with a certain property (that it is the Gödel number of the proof of p), but on the other hand, for every specific number x, we can prove that it does not have this property. This is impossible in an ω-consistent system. Thus the negation of p is not provable.

Thus the statement p is undecidable in our axiomatic system: it can neither be proved nor disproved within the system.

In fact, to show that p is not provable only requires the assumption that the system is consistent. The stronger assumption of ω-consistency is required to show that the negation of p is not provable. Thus, if p is constructed for a particular system:

- If the system is ω-consistent, it can prove neither p nor its negation, and so p is undecidable.
- If the system is consistent, it may have the same situation, or it may prove the negation of p. In the later case, we have a statement ("not p") which is false but provable, and the system is not ω-consistent.

If one tries to "add the missing axioms" to avoid the incompleteness of the system, then one has to add either p or "not p" as axioms. But then the definition of "being a Gödel number of a proof" of a statement changes. which means that the formula *Bew*(*x*) is now different. Thus when we apply the diagonal lemma to this new Bew, we obtain a new statement p, different from the previous one, which will be undecidable in the new system if it is ω-consistent.

### Proof via Berry's paradox

Boolos (1989) sketches an alternative proof of the first incompleteness theorem that uses Berry's paradox rather than the liar paradox to construct a true but unprovable formula. A similar proof method was independently discovered by Saul Kripke. Boolos's proof proceeds by constructing, for any computably enumerable set S of true sentences of arithmetic, another sentence which is true but not contained in S. This gives the first incompleteness theorem as a corollary. According to Boolos, this proof is interesting because it provides a "different sort of reason" for the incompleteness of effective, consistent theories of arithmetic.

### Computer verified proofs

The incompleteness theorems are among a relatively small number of nontrivial theorems that have been transformed into formalized theorems that can be completely verified by proof assistant software. Gödel's original proofs of the incompleteness theorems, like most mathematical proofs, were written in natural language intended for human readers.

Computer-verified proofs of versions of the first incompleteness theorem were announced by Natarajan Shankar in 1986 using Nqthm (Shankar 1994), by Russell O'Connor in 2003 using Rocq (previously known as *Coq*) (O'Connor 2005) and by John Harrison in 2009 using HOL Light (Harrison 2009). A computer-verified proof of both incompleteness theorems was announced by Lawrence Paulson in 2013 using Isabelle (Paulson 2014).


## Proof sketch for the second theorem

The main difficulty in proving the second incompleteness theorem is to show that various facts about provability used in the proof of the first incompleteness theorem can be formalized within a system S using a formal predicate *P* for provability. Once this is done, the second incompleteness theorem follows by formalizing the entire proof of the first incompleteness theorem within the system S itself.

Let p stand for the undecidable sentence constructed above, and assume for purposes of obtaining a contradiction that the consistency of the system S can be proved from within the system S itself. This is equivalent to proving the statement "System S is consistent". Next consider the statement c, where c = "If the system S is consistent, then p is not provable". The proof of sentence c can be formalized within the system S, and therefore the statement c, "p is not provable", (or identically, "not *P*(*p*)") can be proved in the system S.

Observe then, that if we can prove that the system S is consistent (i.e. the statement in the hypothesis of c), then we have proved that p is not provable. But this is a contradiction since by the 1st Incompleteness Theorem, this sentence (i.e. what is implied in the sentence c, ""p" is not provable") is what we construct to be unprovable. Notice that this is why we require formalizing the first Incompleteness Theorem in S: to prove the 2nd Incompleteness Theorem, we obtain a contradiction with the 1st Incompleteness Theorem which can do only by showing that the theorem holds in S. So we cannot prove that the system S is consistent. And the 2nd Incompleteness Theorem statement follows.
