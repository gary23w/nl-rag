---
title: "De Morgan's laws"
source: https://en.wikipedia.org/wiki/De_Morgan's_laws
domain: logic-foundations
license: CC-BY-SA-4.0
tags: propositional logic, first-order logic, boolean algebra, truth table, mathematical proof
fetched: 2026-07-02
---

# De Morgan's laws

In propositional logic and Boolean algebra, **De Morgan's laws**, also known as **De Morgan's theorem**, are a pair of transformation rules that are both valid rules of inference. They are named after Augustus De Morgan, a 19th-century British mathematician. The rules allow the expression of conjunctions and disjunctions purely in terms of each other via negation.

The rules can be expressed in English as:

- The negation of "A and B" is the same as "not A or not B".
- The negation of "A or B" is the same as "not A and not B".

or

- The complement of the union of two sets is the same as the intersection of their complements
- The complement of the intersection of two sets is the same as the union of their complements

or

- not (A or B) = (not A) and (not B)
- not (A and B) = (not A) or (not B)

where "A or B" is an "inclusive or" meaning *at least* one of A or B rather than an "exclusive or" that means *exactly* one of A or B.

Another form of De Morgan's law is the following as seen below.

$A-(B\cup C)=(A-B)\cap (A-C),$

$A-(B\cap C)=(A-B)\cup (A-C).$

Applications of the rules include simplification of logical expressions in computer programs and digital circuit designs. De Morgan's laws are an example of a more general concept of mathematical duality.

## Formal notation

The *negation of conjunction* rule may be written in sequent notation:

${\begin{aligned}\neg (P\land Q)&\vdash (\neg P\lor \neg Q),{\text{and}}\\(\neg P\lor \neg Q)&\vdash \neg (P\land Q).\end{aligned}}$

The *negation of disjunction* rule may be written as:

${\begin{aligned}\neg (P\lor Q)&\vdash (\neg P\land \neg Q),{\text{and}}\\(\neg P\land \neg Q)&\vdash \neg (P\lor Q).\end{aligned}}$

In rule form: *negation of conjunction*

${\frac {\neg (P\land Q)}{\therefore \neg P\lor \neg Q}}\qquad {\frac {\neg P\lor \neg Q}{\therefore \neg (P\land Q)}}$

and *negation of disjunction*

${\frac {\neg (P\lor Q)}{\therefore \neg P\land \neg Q}}\qquad {\frac {\neg P\land \neg Q}{\therefore \neg (P\lor Q)}}$

and expressed as truth-functional tautologies or theorems of propositional logic:

${\begin{aligned}\neg (P\land Q)&\leftrightarrow (\neg P\lor \neg Q),\\\neg (P\lor Q)&\leftrightarrow (\neg P\land \neg Q).\\\end{aligned}}$

where P and Q are propositions expressed in some formal system.

The **generalized De Morgan's laws** provide an equivalence for negating a conjunction or disjunction involving multiple terms. For a set of propositions $P_{1},P_{2},\dots ,P_{n}$ , the generalized De Morgan's Laws are as follows:

${\begin{aligned}\lnot (P_{1}\land P_{2}\land \dots \land P_{n})\leftrightarrow \lnot P_{1}\lor \lnot P_{2}\lor \ldots \lor \lnot P_{n}\\\lnot (P_{1}\lor P_{2}\lor \dots \lor P_{n})\leftrightarrow \lnot P_{1}\land \lnot P_{2}\land \ldots \land \lnot P_{n}\end{aligned}}$

These laws generalize De Morgan's original laws for negating conjunctions and disjunctions.

### Substitution form

De Morgan's laws are normally shown in the compact form above, with the negation of the output on the left and negation of the inputs on the right. A clearer form for substitution can be stated as:

${\begin{aligned}(P\land Q)&\Longleftrightarrow \neg (\neg P\lor \neg Q),\\(P\lor Q)&\Longleftrightarrow \neg (\neg P\land \neg Q).\end{aligned}}$

This emphasizes the need to invert both the inputs and the output, as well as change the operator when doing a substitution.

### Set theory

In set theory, it is often stated as "union and intersection interchange under complementation", which can be formally expressed as:

${\begin{aligned}{\overline {A\cup B}}&={\overline {A}}\cap {\overline {B}},\\{\overline {A\cap B}}&={\overline {A}}\cup {\overline {B}},\end{aligned}}$

where:

- ${\overline {A}}$ is the negation of A , the overline being written above the terms to be negated,
- $\cap$ is the intersection operator (AND),
- $\cup$ is the union operator (OR).

#### Unions and intersections of any number of sets

The generalized form is

${\begin{aligned}{\overline {\bigcap _{i\in I}A_{i}}}&\equiv \bigcup _{i\in I}{\overline {A_{i}}},\\{\overline {\bigcup _{i\in I}A_{i}}}&\equiv \bigcap _{i\in I}{\overline {A_{i}}},\end{aligned}}$

where *I* is some, possibly countably or uncountably infinite, indexing set.

In set notation, De Morgan's laws can be remembered using the mnemonic "break the line, change the sign".

### Boolean algebra

In Boolean algebra, similarly, this law which can be formally expressed as:

${\begin{aligned}{\overline {A\land B}}&={\overline {A}}\lor {\overline {B}},\\{\overline {A\lor B}}&={\overline {A}}\land {\overline {B}},\end{aligned}}$

where:

- ${\overline {A}}$ is the negation of A , the overline being written above the terms to be negated,
- $\land$ is the logical conjunction operator (AND),
- $\lor$ is the logical disjunction operator (OR).

which can be generalized to

${\begin{aligned}{\overline {A_{1}\land A_{2}\land \ldots \land A_{n}}}={\overline {A_{1}}}\lor {\overline {A_{2}}}\lor \ldots \lor {\overline {A_{n}}},\\{\overline {A_{1}\lor A_{2}\lor \ldots \lor A_{n}}}={\overline {A_{1}}}\land {\overline {A_{2}}}\land \ldots \land {\overline {A_{n}}}.\end{aligned}}$

### Engineering

In electrical and computer engineering, De Morgan's laws are commonly written as:

${\overline {(A\cdot B)}}\equiv ({\overline {A}}+{\overline {B}})$

and

${\overline {(A+B)}}\equiv ({\overline {A}}\cdot {\overline {B}}),$

where:

- $\cdot$ is the logical AND,
- + is the logical OR,
- the overbar is the logical NOT of what is underneath the overbar.

### Text searching

De Morgan's laws commonly apply to text searching using Boolean operators AND, OR, and NOT. Consider a set of documents containing the words "cats" and "dogs". De Morgan's laws hold that these two searches will return the same set of documents:

Search A: NOT (cats OR dogs)

Search B: (NOT cats) AND (NOT dogs)

The corpus of documents containing "cats" or "dogs" can be represented by four documents:

Document 1: Contains only the word "cats".

Document 2: Contains only "dogs".

Document 3: Contains both "cats" and "dogs".

Document 4: Contains neither "cats" nor "dogs".

To evaluate Search A, clearly the search "(cats OR dogs)" will hit on Documents 1, 2, and 3. So the negation of that search (which is Search A) will hit everything else, which is Document 4.

Evaluating Search B, the search "(NOT cats)" will hit on documents that do not contain "cats", which is Documents 2 and 4. Similarly the search "(NOT dogs)" will hit on Documents 1 and 4. Applying the AND operator to these two searches (which is Search B) will hit on the documents that are common to these two searches, which is Document 4.

A similar evaluation can be applied to show that the following two searches will both return Documents 1, 2, and 4:

Search C: NOT (cats AND dogs),

Search D: (NOT cats) OR (NOT dogs).

## Worked Example

Here is a more concrete example to illustrate how De Morgan's laws operate in practice.

Let's consider the statement: "It is not the case that a number is both even and positive". Using De Morgan's laws, this statement can be rewritten to read: "The number is either not even or it is not positive"

This transformation demonstrates how negation is distrubuted across a conjuction by negating each component and switching the logical operator. Step-by-step rewrites such as this are especially useful when simplifying logical expressions in proofs and problem solving.

## History

The laws are named after Augustus De Morgan (1806–1871), who introduced a formal version of the laws to classical propositional logic. The first explicit statement of De Morgan’s laws in his own work can be found in his 1847 book *Formal Logic*. De Morgan's formulation was influenced by the algebraization of logic undertaken by George Boole, which later cemented De Morgan's claim to the find. Nevertheless, a similar observation was made by Aristotle, and was known to Greek and Medieval logicians. For example, in the 14th century, William of Ockham wrote down the words that would result by reading the laws out. Jean Buridan, in his *Summulae de Dialectica*, also describes rules of conversion that follow the lines of De Morgan's laws. Still, De Morgan is given credit for stating the laws in the terms of modern formal logic, and incorporating them into the language of logic. De Morgan's laws can be proved easily, and may even seem trivial. Nonetheless, these laws are helpful in making valid inferences in proofs and deductive arguments.

## Proof for Boolean algebra

De Morgan's theorem may be applied to the negation of a disjunction or the negation of a conjunction in all or part of a formula.

### Negation of a disjunction

In the case of its application to a disjunction, consider the following claim: "it is false that either of A or B is true", which is written as:

$\neg (A\lor B).$

In that it has been established that *neither* A nor B is true, then it must follow that both A is not true and B is not true, which may be written directly as:

$(\neg A)\wedge (\neg B).$

If either A or B *were* true, then the disjunction of A and B would be true, making its negation false. Presented in English, this follows the logic that "since two things are both false, it is also false that either of them is true".

Working in the opposite direction, the second expression asserts that A is false and B is false (or equivalently that "not A" and "not B" are true). Knowing this, a disjunction of A and B must be false also. The negation of said disjunction must thus be true, and the result is identical to the first claim.

### Negation of a conjunction

The application of De Morgan's theorem to conjunction is very similar to its application to a disjunction both in form and rationale. Consider the following claim: "it is false that A and B are both true", which is written as:

$\neg (A\land B).$

In order for this claim to be true, either or both of A or B must be false, for if they both were true, then the conjunction of A and B would be true, making its negation false. Thus, one (at least) or more of A and B must be false (or equivalently, one or more of "not A" and "not B" must be true). This may be written directly as,

$(\neg A)\lor (\neg B).$

Presented in a natural language like English, it is expressed as "since it is false that two things are both true, at least one of them must be false".

Working in the opposite direction again, the second expression asserts that at least one of "not A" and "not B" must be true, or equivalently that at least one of A and B must be false. Since at least one of them must be false, then their conjunction would likewise be false. Negating said conjunction thus results in a true expression, and this expression is identical to the first claim.

## Proof for set theory

Here we use ${\overline {A}}$ to denote the complement of A, as above in § Set theory and Boolean algebra. The proof that ${\overline {A\cap B}}={\overline {A}}\cup {\overline {B}}$ is completed in 2 steps by proving both ${\overline {A\cap B}}\subseteq {\overline {A}}\cup {\overline {B}}$ and ${\overline {A}}\cup {\overline {B}}\subseteq {\overline {A\cap B}}$ .

### Part 1

Let $x\in {\overline {A\cap B}}$ . Then, $x\not \in A\cap B$ .

Because $A\cap B=\{\,y\ |\ y\in A\wedge y\in B\,\}$ , it must be the case that $x\not \in A$ or $x\not \in B$ .

If $x\not \in A$ , then $x\in {\overline {A}}$ , so $x\in {\overline {A}}\cup {\overline {B}}$ .

Similarly, if $x\not \in B$ , then $x\in {\overline {B}}$ , so $x\in {\overline {A}}\cup {\overline {B}}$ .

Thus, $\forall x{\Big (}x\in {\overline {A\cap B}}\implies x\in {\overline {A}}\cup {\overline {B}}{\Big )}$ ;

that is, ${\overline {A\cap B}}\subseteq {\overline {A}}\cup {\overline {B}}$ .

### Part 2

To prove the reverse direction, let $x\in {\overline {A}}\cup {\overline {B}}$ , and for contradiction assume $x\not \in {\overline {A\cap B}}$ .

Under that assumption, it must be the case that $x\in A\cap B$ ,

so it follows that $x\in A$ and $x\in B$ , and thus $x\not \in {\overline {A}}$ and $x\not \in {\overline {B}}$ .

However, that means $x\not \in {\overline {A}}\cup {\overline {B}}$ , in contradiction to the hypothesis that $x\in {\overline {A}}\cup {\overline {B}}$ ,

therefore, the assumption $x\not \in {\overline {A\cap B}}$ must not be the case, meaning that $x\in {\overline {A\cap B}}$ .

Hence, $\forall x{\Big (}x\in {\overline {A}}\cup {\overline {B}}\implies x\in {\overline {A\cap B}}{\Big )}$ ,

that is, ${\overline {A}}\cup {\overline {B}}\subseteq {\overline {A\cap B}}$ .

### Conclusion

If ${\overline {A}}\cup {\overline {B}}\subseteq {\overline {A\cap B}}$ *and* ${\overline {A\cap B}}\subseteq {\overline {A}}\cup {\overline {B}}$ , then ${\overline {A\cap B}}={\overline {A}}\cup {\overline {B}}$ ; this concludes the proof of De Morgan's law.

The other De Morgan's law, ${\overline {A\cup B}}={\overline {A}}\cap {\overline {B}}$ , is proven similarly.

## Generalising De Morgan duality

In extensions of classical propositional logic, the duality still holds (that is, to any logical operator one can always find its dual), since in the presence of the identities governing negation, one may always introduce an operator that is the De Morgan dual of another. This leads to an important property of logics based on classical logic, namely the existence of negation normal forms: any formula is equivalent to another formula where negations only occur applied to the non-logical atoms of the formula. The existence of negation normal forms drives many applications, for example in digital circuit design, where it is used to manipulate the types of logic gates, and in formal logic, where it is needed to find the conjunctive normal form and disjunctive normal form of a formula. Computer programmers use them to simplify or properly negate complicated logical conditions. They are also often useful in computations in elementary probability theory.

Let one define the dual of any propositional operator P(*p*, *q*, ...) depending on elementary propositions *p*, *q*, ... to be the operator ${\mbox{P}}^{d}$ defined by

${\mbox{P}}^{d}(p,q,...)=\neg P(\neg p,\neg q,\dots ).$

## Extension to predicate and modal logic

This duality can be generalised to quantifiers, so for example the universal quantifier and existential quantifier are duals:

$\forall x\,P(x)\equiv \neg [\exists x\,\neg P(x)]$

$\exists x\,P(x)\equiv \neg [\forall x\,\neg P(x)]$

To relate these quantifier dualities to the De Morgan laws, consider a domain of discourse *D* (with some small number of entities) to which properties are ascribed universally and existentially, such as

D

= {

a

,

b

,

c

}.

Then express universal quantifier equivalently by conjunction of individual statements

$\forall x\,P(x)\equiv P(a)\land P(b)\land P(c)$

and existential quantifier by disjunction of individual statements

$\exists x\,P(x)\equiv P(a)\lor P(b)\lor P(c).$

But, using De Morgan's laws,

$P(a)\land P(b)\land P(c)\equiv \neg (\neg P(a)\lor \neg P(b)\lor \neg P(c))$

and

$P(a)\lor P(b)\lor P(c)\equiv \neg (\neg P(a)\land \neg P(b)\land \neg P(c)),$

verifying the quantifier dualities in the model.

Then, the quantifier dualities can be extended further to modal logic, relating the box ("necessarily") and diamond ("possibly") operators:

$\Box p\equiv \neg \Diamond \neg p,$

$\Diamond p\equiv \neg \Box \neg p.$

In its application to the alethic modalities of possibility and necessity, Aristotle observed this case, and in the case of normal modal logic, the relationship of these modal operators to the quantification can be understood by setting up models using Kripke semantics.

## In intuitionistic logic

Three out of the four implications of de Morgan's laws hold in intuitionistic logic. Specifically, we have

$\neg (P\lor Q)\,\leftrightarrow \,{\big (}(\neg P)\land (\neg Q){\big )},$

and

${\big (}(\neg P)\lor (\neg Q){\big )}\,\to \,\neg (P\land Q).$

The converse of the last implication does not hold in pure intuitionistic logic. That is, the failure of the joint proposition $P\land Q$ cannot necessarily be resolved to the failure of either of the two conjuncts. For example, from knowing it not to be the case that both Alice and Bob showed up to their date, it does not follow who did not show up. The latter principle is equivalent to the principle of the weak excluded middle ${\mathrm {WPEM} }$ ,

$(\neg P)\lor \neg (\neg P).$

This weak form can be used as a foundation for an intermediate logic. For a refined version of the failing law concerning existential statements, see the lesser limited principle of omniscience ${\mathrm {LLPO} }$ , which however is different from ${\mathrm {WLPO} }$ .

The validity of the other three De Morgan's laws remains true if negation $\neg P$ is replaced by implication $P\to C$ for some arbitrary constant predicate C, meaning that the above laws are still true in minimal logic.

Similarly to the above, the quantifier laws:

$\forall x\,\neg P(x)\,\leftrightarrow \,\neg \exists x\,P(x)$

and

$\exists x\,\neg P(x)\,\to \,\neg \forall x\,P(x).$

are tautologies even in minimal logic with negation replaced with implying a fixed Q , while the converse of the last law does not have to be true in general.

Further, one still has

$(P\lor Q)\,\to \,\neg {\big (}(\neg P)\land (\neg Q){\big )},$

$(P\land Q)\,\to \,\neg {\big (}(\neg P)\lor (\neg Q){\big )},$

$\forall x\,P(x)\,\to \,\neg \exists x\,\neg P(x),$

$\exists x\,P(x)\,\to \,\neg \forall x\,\neg P(x),$

but their inversion implies excluded middle, ${\mathrm {PEM} }$ .

## In computer engineering

- De Morgan's laws are widely used in computer engineering and digital logic for the purpose of simplifying circuit designs.
- In modern programming languages, compilers and interpreters use De Morgan's laws to optimize Boolean expressions. Therefore performance differences between logically equivalent expressions are usually negligible or completely absent.

## Expanded Applications

De Morgan's laws are commonly cited in digital circuit design and Boolean algebra, however, they also play an important role in reasoning and computation. De Morgan's laws are utilized in probability theory, allowing one to simplify complements of compound events. Expressions involving "not both" or "not either" can be rewritten in more manageable forms.

In computer science, these laws are frequestly applied when rewriting conditional statements. Negating a compound condition in code often requires transforming an AND condition into an OR condition with negated components, illustrating how these laws improve both readabillity and correctness when designing algorithms.

De Morgan's laws are also useful in formal proofs. where transforming logical statements into equivalent forms can make arguments earier to construct and verify.
