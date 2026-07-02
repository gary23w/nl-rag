---
title: "Propositional logic (part 1/2)"
source: https://en.wikipedia.org/wiki/Propositional_calculus
domain: logic-foundations
license: CC-BY-SA-4.0
tags: propositional logic, first-order logic, boolean algebra, truth table, mathematical proof
fetched: 2026-07-02
part: 1/2
---

# Propositional logic

(Redirected from

Propositional calculus

)

**Propositional logic** is a branch of classical logic. It is also called **statement logic**, **sentential calculus**, **propositional calculus**, **sentential logic**, or sometimes **zeroth-order logic**. Sometimes, it is called ***first-order* propositional logic** to contrast it with System F, but it should not be confused with first-order logic. It deals with propositions (which can be true or false) and relations between propositions, including the construction of arguments based on them. Compound propositions are formed by connecting propositions by logical connectives representing the truth functions of conjunction, disjunction, implication, biconditional, and negation. Some sources include other connectives, as in the table below.

Unlike first-order logic, propositional logic does not deal with non-logical objects, predicates about them, or quantifiers. However, all the machinery of propositional logic is included in first-order logic and higher-order logics. In this sense, propositional logic is the foundation of first-order logic and higher-order logic.

Propositional logic is typically studied with a formal language, in which propositions are represented by letters, which are called *propositional variables*. These are then used, together with symbols for connectives, to make *propositional formulas*. Because of this, the propositional variables are called *atomic formulas* of a formal propositional language. While the atomic propositions are typically represented by letters of the alphabet, there is a variety of notations to represent the logical connectives. For the benefit of readers who may only be used to a different variant notation for the logical connectives, the following table shows the main notational variants for each of the connectives in propositional logic. Other notations have been used historically, such as Polish notation. For the history of each of these symbols, see the respective articles as well as the article "Logical connective".

| Connective | Symbol |
|---|---|
| AND | $A\land B$ , $A\cdot B$ , $AB$ , $A\&B$ , $A\&\&B$ |
| equivalent | $A\equiv B$ , $A\Leftrightarrow B$ , $A\leftrightharpoons B$ |
| implies | $A\Rightarrow B$ , $A\supset B$ , $A\rightarrow B$ |
| NAND | $A{\overline {\land }}B$ , $A\mid B$ , ${\overline {A\cdot B}}$ |
| nonequivalent | $A\not \equiv B$ , $A\not \Leftrightarrow B$ , $A\nleftrightarrow B$ |
| NOR | $A{\overline {\lor }}B$ , $A\downarrow B$ , ${\overline {A+B}}$ |
| NOT | $\neg A$ , $-A$ , ${\overline {A}}$ , $\sim A$ |
| OR | $A\lor B$ , $A+B$ , $A\mid B$ , $A\parallel B$ |
| XNOR | $A\odot B$ |
| XOR | $A{\underline {\lor }}B$ , $A\oplus B$ |

The most thoroughly researched branch of propositional logic is **classical truth-functional propositional logic**, in which formulas are interpreted as having precisely one of two possible truth values, the truth value of *true* or the truth value of *false*. The principle of bivalence and the law of excluded middle are upheld. By comparison with first-order logic, truth-functional propositional logic is considered to be *zeroth-order logic*.


## History

Although propositional logic had been hinted by earlier philosophers, Chrysippus is often credited with development of a deductive system for propositional logic as his main achievement in the 3rd century BC which was expanded by his successor Stoics. The logic was focused on propositions. This was different from the traditional syllogistic logic, which focused on terms. However, most of the original writings were lost and, at some time between the 3rd and 6th century CE, Stoic logic faded into oblivion, to be resurrected only in the 20th century, in the wake of the (re)-discovery of propositional logic.

Symbolic logic, which would come to be important to refine propositional logic, was first developed by the 17th/18th-century mathematician Gottfried Leibniz, whose calculus ratiocinator was, however, unknown to the larger logical community. Consequently, many of the advances achieved by Leibniz were recreated by logicians like George Boole and Augustus De Morgan, completely independent of Leibniz.

Gottlob Frege's predicate logic builds upon propositional logic, and has been described as combining "the distinctive features of syllogistic logic and propositional logic." Consequently, predicate logic ushered in a new era in logic's history; however, advances in propositional logic were still made after Frege, including natural deduction, truth trees and truth tables. Natural deduction was invented by Gerhard Gentzen and Stanisław Jaśkowski. Truth trees were invented by Evert Willem Beth. The invention of truth tables, however, is of uncertain attribution.

Within works by Frege and Bertrand Russell, are ideas influential to the invention of truth tables. The actual tabular structure (being formatted as a table), itself, is generally credited to either Ludwig Wittgenstein or Emil Post (or both, independently). Besides Frege and Russell, others credited with having ideas preceding truth tables include Philo, Boole, Charles Sanders Peirce, and Ernst Schröder. Others credited with the tabular structure include Jan Łukasiewicz, Alfred North Whitehead, William Stanley Jevons, John Venn, and Clarence Irving Lewis. Ultimately, some have concluded, like John Shosky, that "It is far from clear that any one person should be given the title of 'inventor' of truth-tables".


## Sentences

Propositional logic, as currently studied in universities, is a specification of a standard of logical consequence in which only the meanings of propositional connectives are considered in evaluating the conditions for the truth of a sentence, or whether a sentence logically follows from some other sentence or group of sentences.

### Declarative sentences

Propositional logic deals with **statements**, which are defined as declarative sentences having truth value. Examples of statements might include:

- *Wikipedia is a free online encyclopedia that anyone can edit.*
- *London is the capital of England.*
- *All Wikipedia editors speak at least three languages.*

Declarative sentences are contrasted with questions, such as "What is Wikipedia?", and imperative statements, such as "Please add citations to support the claims in this article.". Such non-declarative sentences have no truth value, and are only dealt with in nonclassical logics, called erotetic and imperative logics.

### Compounding sentences with connectives

In propositional logic, a statement can contain one or more other statements as parts. *Compound sentences* are formed from simpler sentences and express relationships among the constituent sentences. This is done by combining them with logical connectives: the main types of compound sentences are negations, conjunctions, disjunctions, implications, and biconditionals, which are formed by using the corresponding connectives to connect propositions. In English, these connectives are expressed by the words "and" (conjunction), "or" (disjunction), "not" (negation), "if" (material conditional), and "if and only if" (biconditional). Examples of such compound sentences might include:

- *Wikipedia is a free online encyclopedia that anyone can edit, **and** millions already have.* (conjunction)
- ***It is not true that** all Wikipedia editors speak at least three languages.* (negation)
- ***Either** London is the capital of England, **or** London is the capital of the United Kingdom, **or both.*** (disjunction)

If sentences lack any logical connectives, they are called *simple sentences*, or *atomic sentences*; if they contain one or more logical connectives, they are called *compound sentences*, or *molecular sentences*.

*Sentential connectives* are a broader category that includes logical connectives. Sentential connectives are any linguistic particles that bind sentences to create a new compound sentence, or that inflect a single sentence to create a new sentence. A *logical connective*, or *propositional connective*, is a kind of sentential connective with the characteristic feature that, when the original sentences it operates on are (or express) propositions, the new sentence that results from its application also is (or expresses) a proposition. Philosophers disagree about what exactly a proposition is, as well as about which sentential connectives in natural languages should be counted as logical connectives. Sentential connectives are also called *sentence-functors*, and logical connectives are also called *truth-functors*.


## Arguments

An argument is defined as a pair of things, namely a set of sentences, called the **premises**, and a sentence, called the **conclusion**. The conclusion is claimed to *follow from* the premises, and the premises are claimed to *support* the conclusion.

### Example argument

The following is an example of an argument within the scope of propositional logic:

Premise 1:

If

it's raining,

then

it's cloudy.

Premise 2:

It's raining.

Conclusion:

It's cloudy.

The logical form of this argument is known as modus ponens, which is a classically valid form. So, in classical logic, the argument is *valid*, although it may or may not be *sound*, depending on the meteorological facts in a given context. This **example argument** will be reused when explaining § Formalization.

### Validity and soundness

An argument is **valid** if, and only if, it is *necessary* that, if all its premises are true, its conclusion is true. Alternatively, an argument is valid if, and only if, it is *impossible* for all the premises to be true while the conclusion is false.

Validity is contrasted with *soundness*. An argument is **sound** if, and only if, it is valid and all its premises are true. Otherwise, it is *unsound*.

Logic, in general, aims to precisely specify valid arguments. This is done by defining a valid argument as one in which its conclusion is a logical consequence of its premises, which, when this is understood as *semantic consequence*, means that there is no *case* in which the premises are true but the conclusion is not true – see § Semantics below.


## Formalization

Propositional logic is typically studied through a formal system in which formulas of a formal language are interpreted to represent propositions. This formal language is the basis for proof systems, which allow a conclusion to be derived from premises if, and only if, it is a logical consequence of them. This section will show how this works by formalizing the § Example argument. The formal language for a propositional calculus will be fully specified in § Language, and an overview of proof systems will be given in § Proof systems.

### Propositional variables

Since propositional logic is not concerned with the structure of propositions beyond the point where they cannot be decomposed any more by logical connectives, it is typically studied by replacing such *atomic* (indivisible) statements with letters of the alphabet, which are interpreted as variables representing statements (*propositional variables*). With propositional variables, the § Example argument would then be symbolized as follows:

Premise 1:

$P\to Q$

Premise 2:

P

Conclusion:

Q

When P is interpreted as "It's raining" and Q as "it's cloudy" these symbolic expressions correspond exactly with the original expression in natural language. Not only that, but they will also correspond with any other inference with the same logical form.

When a formal system is used to represent formal logic, only statement letters (usually capital roman letters such as P , Q and R ) are represented directly. The natural language propositions that arise when they're interpreted are outside the scope of the system, and the relation between the formal system and its interpretation is likewise outside the formal system itself.

### Gentzen notation

If we assume that the validity of modus ponens has been accepted as an axiom, then the same § Example argument can also be depicted like this:

${\frac {P\to Q,P}{Q}}$

This method of displaying it is Gentzen's notation for natural deduction and sequent calculus. The premises are shown above a line, called the **inference line**, separated by a **comma**, which indicates *combination* of premises. The conclusion is written below the inference line. The inference line represents *syntactic consequence*, sometimes called *deductive consequence*, which is also symbolized with ⊢. So the above can also be written in one line as $P\to Q,P\vdash Q$ .

Syntactic consequence is contrasted with *semantic consequence*, which is symbolized with ⊧. In this case, the conclusion follows *syntactically* because the natural deduction inference rule of modus ponens has been assumed. For more on inference rules, see the sections on proof systems below.


## Language

The language (commonly called ${\mathcal {L}}$ ) of a propositional calculus is defined in terms of:

1. a set of primitive symbols, called *atomic formulas*, *atomic sentences*, *atoms,* *placeholders*, *prime formulas*, *proposition letters*, *sentence letters*, or *variables*, and
2. a set of operator symbols, called *connectives*, *logical connectives*, *logical operators*, *truth-functional connectives,* *truth-functors*, or *propositional connectives*.

A *well-formed formula* is any atomic formula, or any formula that can be built up from atomic formulas by means of operator symbols according to the rules of the grammar. The language ${\mathcal {L}}$ , then, is defined either as being *identical to* its set of well-formed formulas, or as *containing* that set (together with, for instance, its set of connectives and variables).

Usually the syntax of ${\mathcal {L}}$ is defined recursively by just a few definitions, as seen next; some authors explicitly include *parentheses* as punctuation marks when defining their language's syntax, while others use them without comment.

### Syntax

Given a set of atomic propositional variables $p_{1}$ , $p_{2}$ , $p_{3}$ , ..., and a set of propositional connectives $c_{1}^{1}$ , $c_{2}^{1}$ , $c_{3}^{1}$ , ..., $c_{1}^{2}$ , $c_{2}^{2}$ , $c_{3}^{2}$ , ..., $c_{1}^{3}$ , $c_{2}^{3}$ , $c_{3}^{3}$ , ..., a formula of propositional logic is defined recursively by these definitions:

Definition 1

: Atomic propositional variables are formulas.

Definition 2

: If

$c_{n}^{m}$

is a propositional connective, and

$\langle$

A, B, C, …

$\rangle$

is a sequence of m, possibly but not necessarily atomic, possibly but not necessarily distinct, formulas, then the result of applying

$c_{n}^{m}$

to

$\langle$

A, B, C, …

$\rangle$

is a formula.

Definition 3:

Nothing else is a formula.

Writing the result of applying $c_{n}^{m}$ to $\langle$ A, B, C, ... $\rangle$ in functional notation, as $c_{n}^{m}$ (A, B, C, ...), we have the following as examples of well-formed formulas:

- $p_{5}$
- $c_{3}^{2}(p_{2},p_{9})$
- $c_{3}^{2}(p_{1},c_{2}^{1}(p_{3}))$
- $c_{1}^{3}(p_{4},p_{6},c_{2}^{2}(p_{1},p_{2}))$
- $c_{4}^{2}(c_{1}^{1}(p_{7}),c_{3}^{1}(p_{8}))$
- $c_{2}^{3}(c_{1}^{2}(p_{3},p_{4}),c_{2}^{1}(p_{5}),c_{3}^{2}(p_{6},p_{7}))$
- $c_{3}^{1}(c_{1}^{3}(p_{2},p_{3},c_{2}^{2}(p_{4},p_{5})))$

What was given as *Definition 2* above, which is responsible for the composition of formulas, is referred to by Colin Howson as the *principle of composition*. It is this recursion in the definition of a language's syntax which justifies the use of the word "atomic" to refer to propositional variables, since all formulas in the language ${\mathcal {L}}$ are built up from the atoms as ultimate building blocks. Composite formulas (all formulas besides atoms) are called *molecules*, or *molecular sentences*. (This is an imperfect analogy with chemistry, since a chemical molecule may sometimes have only one atom, as in monatomic gases.)

The definition that "nothing else is a formula", given above as *Definition 3*, excludes any formula from the language which is not specifically required by the other definitions in the syntax. In particular, it excludes *infinitely long* formulas from being well-formed. It is sometimes called the *Closure Clause*.

#### CF grammar in BNF

An alternative to the syntax definitions given above is to write a context-free (CF) grammar for the language ${\mathcal {L}}$ in Backus-Naur form (BNF). This is more common in computer science than in philosophy. It can be done in many ways, of which a particularly brief one, for the common set of five connectives, is this single clause:

$\phi ::=a_{1},a_{2},\ldots ~|~\neg \phi ~|~\phi ~\&~\psi ~|~\phi \vee \psi ~|~\phi \rightarrow \psi ~|~\phi \leftrightarrow \psi$

This clause, due to its self-referential nature (since $\phi$ is in some branches of the definition of $\phi$ ), also acts as a recursive definition, and therefore specifies the entire language. To expand it to add modal operators, one need only add ...  $|~\Box \phi ~|~\Diamond \phi$ to the end of the clause.

### Constants and schemata

Mathematicians sometimes distinguish between propositional constants, propositional variables, and schemata. *Propositional constants* represent some particular proposition, while *propositional variables* range over the set of all atomic propositions. Schemata, or *schematic letters*, however, range over all formulas. (Schematic letters are also called *metavariables*.) It is common to represent propositional constants by A, B, and C, propositional variables by P, Q, and R, and schematic letters are often Greek letters, most often φ, ψ, and χ.

However, some authors recognize only two "propositional constants" in their formal system: the special symbol $\top$ , called "truth", which always evaluates to *True*, and the special symbol $\bot$ , called "falsity", which always evaluates to *False*. Other authors also include these symbols, with the same meaning, but consider them to be "zero-place truth-functors", or equivalently, "nullary connectives".


## Semantics

To serve as a model of the logic of a given natural language, a formal language must be semantically interpreted. In classical logic, all propositions evaluate to exactly one of two truth-values: *True* or *False*. For example, "Wikipedia is a free online encyclopedia that anyone can edit" evaluates to *True*, while "Wikipedia is a paper encyclopedia" evaluates to *False*.

In other respects, the following formal semantics can apply to the language of any propositional logic, but the assumptions that there are only two semantic values (*bivalence*), that only one of the two is assigned to each formula in the language (*noncontradiction*), and that every formula gets assigned a value (*excluded middle*), are distinctive features of classical logic. To learn about nonclassical logics with more than two truth-values, and their unique semantics, one may consult the articles on "Many-valued logic", "Three-valued logic", "Finite-valued logic", and "Infinite-valued logic".

### Interpretation (case) and argument

For a given language ${\mathcal {L}}$ , an **interpretation**, **valuation**, **Boolean valuation**, or **case**, is an assignment of *semantic values* to each formula of ${\mathcal {L}}$ . For a formal language of classical logic, a case is defined as an *assignment*, to each formula of ${\mathcal {L}}$ , of one or the other, but not both, of the truth values, namely truth (**T**, or 1) and falsity (**F**, or 0). An interpretation that follows the rules of classical logic is sometimes called a **Boolean valuation**. An interpretation of a formal language for classical logic is often expressed in terms of truth tables. Since each formula is only assigned a single truth-value, an interpretation may be viewed as a function, whose domain is ${\mathcal {L}}$ , and whose range is its set of semantic values ${\mathcal {V}}=\{{\mathsf {T}},{\mathsf {F}}\}$ , or ${\mathcal {V}}=\{1,0\}$ .

For n distinct propositional symbols there are $2^{n}$ distinct possible interpretations. For any particular symbol a , for example, there are $2^{1}=2$ possible interpretations: either a is assigned **T**, or a is assigned **F**. And for the pair a , b there are $2^{2}=4$ possible interpretations: either both are assigned **T**, or both are assigned **F**, or a is assigned **T** and b is assigned **F**, or a is assigned **F** and b is assigned **T**. Since ${\mathcal {L}}$ has $\aleph _{0}$ , that is, denumerably many propositional symbols, there are $2^{\aleph _{0}}={\mathfrak {c}}$ , and therefore uncountably many distinct possible interpretations of ${\mathcal {L}}$ as a whole.

Where ${\mathcal {I}}$ is an interpretation and $\varphi$ and $\psi$ represent formulas, the definition of an *argument*, given in § Arguments, may then be stated as a pair $\langle \{\varphi _{1},\varphi _{2},\varphi _{3},...,\varphi _{n}\},\psi \rangle$ , where $\{\varphi _{1},\varphi _{2},\varphi _{3},...,\varphi _{n}\}$ is the set of premises and $\psi$ is the conclusion. The definition of an argument's *validity*, i.e. its property that $\{\varphi _{1},\varphi _{2},\varphi _{3},...,\varphi _{n}\}\models \psi$ , can then be stated as its *absence of a counterexample*, where a **counterexample** is defined as a case ${\mathcal {I}}$ in which the argument's premises $\{\varphi _{1},\varphi _{2},\varphi _{3},...,\varphi _{n}\}$ are all true but the conclusion $\psi$ is not true. As will be seen in § Semantic truth, validity, consequence, this is the same as to say that the conclusion is a *semantic consequence* of the premises.

### Propositional connective semantics

An interpretation assigns semantic values to atomic formulas directly. Molecular formulas are assigned a *function* of the value of their constituent atoms, according to the connective used; the connectives are defined in such a way that the truth-value of a sentence formed from atoms with connectives depends on the truth-values of the atoms that they're applied to, and *only* on those. This assumption is referred to by Colin Howson as the assumption of the *truth-functionality of the connectives*.

#### Semantics via truth tables

Since logical connectives are defined semantically only in terms of the truth values that they take when the propositional variables that they're applied to take either of the two possible truth values, the semantic definition of the connectives is usually represented as a truth table for each of the connectives, as seen below:

| p | q | $p\land q$ | $p\lor q$ | $p\rightarrow q$ | $p\Leftrightarrow q$ | $\neg p$ | $\neg q$ |
|---|---|---|---|---|---|---|---|
| T | T | T | T | T | T | F | F |
| T | F | F | T | F | F | F | T |
| F | T | F | T | T | F | T | F |
| F | F | F | F | T | T | T | T |

This table covers each of the main five logical connectives: conjunction (here notated $p\land q$ ), disjunction (*p* ∨ *q*), implication (*p* → *q*), biconditional (*p* ↔ *q*) and negation, (¬*p*, or ¬*q*, as the case may be). It is sufficient for determining the semantics of each of these operators. For more truth tables for more different kinds of connectives, see the article "Truth table".

#### Semantics via assignment expressions

Some authors write out the connective semantics using a list of statements instead of a table. In this format, where ${\mathcal {I}}(\varphi )$ is the interpretation of $\varphi$ , the five connectives are defined as:

- ${\mathcal {I}}(\neg P)={\mathsf {T}}$ if, and only if, ${\mathcal {I}}(P)={\mathsf {F}}$
- ${\mathcal {I}}(P\land Q)={\mathsf {T}}$ if, and only if, ${\mathcal {I}}(P)={\mathsf {T}}$ and ${\mathcal {I}}(Q)={\mathsf {T}}$
- ${\mathcal {I}}(P\lor Q)={\mathsf {T}}$ if, and only if, ${\mathcal {I}}(P)={\mathsf {T}}$ or ${\mathcal {I}}(Q)={\mathsf {T}}$
- ${\mathcal {I}}(P\to Q)={\mathsf {T}}$ if, and only if, it is true that, if ${\mathcal {I}}(P)={\mathsf {T}}$ , then ${\mathcal {I}}(Q)={\mathsf {T}}$
- ${\mathcal {I}}(P\leftrightarrow Q)={\mathsf {T}}$ if, and only if, it is true that ${\mathcal {I}}(P)={\mathsf {T}}$ if, and only if, ${\mathcal {I}}(Q)={\mathsf {T}}$

Instead of ${\mathcal {I}}(\varphi )$ , the interpretation of $\varphi$ may be written out as $|\varphi |$ , or, for definitions such as the above, ${\mathcal {I}}(\varphi )={\mathsf {T}}$ may be written simply as the English sentence " $\varphi$ is given the value ${\mathsf {T}}$ ". Yet other authors may prefer to speak of a Tarskian model ${\mathfrak {M}}$ for the language, so that instead they'll use the notation ${\mathfrak {M}}\models \varphi$ , which is equivalent to saying ${\mathcal {I}}(\varphi )={\mathsf {T}}$ , where ${\mathcal {I}}$ is the interpretation function for ${\mathfrak {M}}$ .

#### Connective definition methods

Some of these connectives may be defined in terms of others: for instance, implication, $p\rightarrow q$ , may be defined in terms of disjunction and negation, as $\neg p\lor q$ ; and disjunction may be defined in terms of negation and conjunction, as $\neg (\neg p\land \neg q$ ). In fact, a *truth-functionally complete* system, in the sense that all and only the classical propositional tautologies are theorems, may be derived using only disjunction and negation (as Russell, Whitehead, and Hilbert did), or using only implication and negation (as Frege did), or using only conjunction and negation, or even using only a single connective for "not and" (the Sheffer stroke), as Jean Nicod did. A *joint denial* connective (logical NOR) will also suffice, by itself, to define all other connectives. Besides NOR and NAND, no other connectives have this property.

Some authors, namely Howson and Cunningham, distinguish equivalence from the biconditional. (As to equivalence, Howson calls it "truth-functional equivalence", while Cunningham calls it "logical equivalence".) Equivalence is symbolized with ⇔ and is a metalanguage symbol, while a biconditional is symbolized with ↔ and is a logical connective in the object language ${\mathcal {L}}$ . Regardless, an equivalence or biconditional is true if, and only if, the formulas connected by it are assigned the same semantic value under every interpretation. Other authors often do not make this distinction, and may use the word "equivalence", and/or the symbol ⇔, to denote their object language's biconditional connective.

### Semantic truth, validity, consequence

Given $\varphi$ and $\psi$ as formulas (or sentences) of a language ${\mathcal {L}}$ , and ${\mathcal {I}}$ as an interpretation (or case) of ${\mathcal {L}}$ , then the following definitions apply:

- **Truth-in-a-case:** A sentence $\varphi$ of ${\mathcal {L}}$ is *true under an interpretation* ${\mathcal {I}}$ if ${\mathcal {I}}$ assigns the truth value **T** to $\varphi$ . If $\varphi$ is true under ${\mathcal {I}}$ , then ${\mathcal {I}}$ is called a *model* of $\varphi$ .
- **Falsity-in-a-case:** $\varphi$ is *false under an interpretation* ${\mathcal {I}}$ if, and only if, $\neg \varphi$ is true under ${\mathcal {I}}$ . This is the "truth of negation" definition of falsity-in-a-case. Falsity-in-a-case may also be defined by the "complement" definition: $\varphi$ is *false under an interpretation* ${\mathcal {I}}$ if, and only if, $\varphi$ is not true under ${\mathcal {I}}$ . In classical logic, these definitions are equivalent, but in nonclassical logics, they are not.
- **Semantic consequence:** A sentence $\psi$ of ${\mathcal {L}}$ is a *semantic consequence* ( $\varphi \models \psi$ ) of a sentence $\varphi$ if there is no interpretation under which $\varphi$ is true and $\psi$ is not true.
- **Valid formula (tautology):** A sentence $\varphi$ of ${\mathcal {L}}$ is *logically valid* ( $\models \varphi$ ), or a *tautology*, if it is true under every interpretation, or *true in every case.*
- **Consistent sentence:** A sentence of ${\mathcal {L}}$ is *consistent* if it is true under at least one interpretation. It is *inconsistent* if it is not consistent. An inconsistent formula is also called *self-contradictory*, and said to be a *self-contradiction*, or simply a *contradiction*, although this latter name is sometimes reserved specifically for statements of the form $(p\land \neg p)$ .

For interpretations (cases) ${\mathcal {I}}$ of ${\mathcal {L}}$ , these definitions are sometimes given:

- **Complete case:** A case ${\mathcal {I}}$ is *complete* if, and only if, either $\varphi$ is true-in- ${\mathcal {I}}$ or $\neg \varphi$ is true-in- ${\mathcal {I}}$ , for any $\varphi$ in ${\mathcal {L}}$ .
- **Consistent case:** A case ${\mathcal {I}}$ is *consistent* if, and only if, there is no $\varphi$ in ${\mathcal {L}}$ such that both $\varphi$ and $\neg \varphi$ are true-in- ${\mathcal {I}}$ .

For classical logic, which assumes that all cases are complete and consistent, the following theorems apply:

- For any given interpretation, a given formula is either true or false under it.
- No formula is both true and false under the same interpretation.
- $\varphi$ is true under ${\mathcal {I}}$ if, and only if, $\neg \varphi$ is false under ${\mathcal {I}}$ ; $\neg \varphi$ is true under ${\mathcal {I}}$ if, and only if, $\varphi$ is not true under ${\mathcal {I}}$ .
- If $\varphi$ and $(\varphi \to \psi )$ are both true under ${\mathcal {I}}$ , then $\psi$ is true under ${\mathcal {I}}$ .
- If $\models \varphi$ and $\models (\varphi \to \psi )$ , then $\models \psi$ .
- $(\varphi \to \psi )$ is true under ${\mathcal {I}}$ if, and only if, either $\varphi$ is not true under ${\mathcal {I}}$ , or $\psi$ is true under ${\mathcal {I}}$ .
- $\varphi \models \psi$ if, and only if, $(\varphi \to \psi )$ is logically valid, that is, $\varphi \models \psi$ if, and only if, $\models (\varphi \to \psi )$ .


## Proof systems

Proof systems in propositional logic can be broadly classified into *semantic proof systems* and *syntactic proof systems*, according to the kind of logical consequence that they rely on: semantic proof systems rely on semantic consequence ( $\varphi \models \psi$ ), whereas syntactic proof systems rely on syntactic consequence ( $\varphi \vdash \psi$ ). Semantic consequence deals with the truth values of propositions in all possible interpretations, whereas syntactic consequence concerns the derivation of conclusions from premises based on rules and axioms within a formal system. This section gives a very brief overview of the kinds of proof systems, with anchors to the relevant sections of this article on each one, as well as to the separate Wikipedia articles on each one.

### Semantic proof systems

${\begin{array}{|c|c|c|c|}x_{0}&x_{1}&{\bar {x_{1}}}&x_{0}\&{\bar {x_{1}}}\\\hline 0&0&1&0\\0&1&0&0\\1&0&1&1\\1&1&0&0\end{array}}$

Example of a

truth table

Semantic proof systems rely on the concept of semantic consequence, symbolized as $\varphi \models \psi$ , which indicates that if $\varphi$ is true, then $\psi$ must also be true in every possible interpretation.

#### Truth tables

A truth table is a semantic proof method used to determine the truth value of a propositional logic expression in every possible scenario. By exhaustively listing the truth values of its constituent atoms, a truth table can show whether a proposition is true, false, tautological, or contradictory. See § Semantic proof via truth tables.

#### Semantic tableaux

A semantic tableau is another semantic proof technique that systematically explores the truth of a proposition. It constructs a tree where each branch represents a possible interpretation of the propositions involved. If every branch leads to a contradiction, the original proposition is considered to be a contradiction, and its negation is considered a tautology. See § Semantic proof via tableaux.

### Syntactic proof systems

Syntactic proof systems, in contrast, focus on the formal manipulation of symbols according to specific rules. The notion of syntactic consequence, $\varphi \vdash \psi$ , signifies that $\psi$ can be derived from $\varphi$ using the rules of the formal system.

#### Axiomatic systems

A Hilbert-style axiomatic system, or Hilbert system, is a set of axioms or assumptions from which other statements (theorems) are logically derived. In propositional logic, axiomatic systems define a base set of propositions considered to be self-evidently true, and theorems are proved by applying deduction rules to these axioms. See § Syntactic proof via axioms.

#### Natural deduction

Natural deduction is a syntactic method of proof that emphasizes the derivation of conclusions from premises through the use of intuitive rules reflecting ordinary reasoning. Each rule reflects a particular logical connective and shows how it can be introduced or eliminated. See § Syntactic proof via natural deduction.

#### Sequent calculus

The sequent calculus is a formal system that represents logical deductions as sequences or "sequents" of formulas. Developed by Gerhard Gentzen, this approach focuses on the structural properties of logical deductions and provides a powerful framework for proving statements within propositional logic.


## Semantic proof via truth tables

Taking advantage of the semantic concept of validity (truth in every interpretation), it is possible to prove a formula's validity by using a truth table, which gives every possible interpretation (assignment of truth values to variables) of a formula. If, and only if, all the lines of a truth table come out true, the formula is semantically valid (true in every interpretation). Further, if (and only if) $\neg \varphi$ is valid, then $\varphi$ is inconsistent.

For instance, this table shows that "*p* → (*q* ∨ *r* → (*r* → ¬*p*))" is not valid:

| *p* | *q* | *r* | *q* ∨ *r* | *r* → ¬*p* | *q* ∨ *r* → (*r* → ¬*p*) | *p* → (*q* ∨ *r* → (*r* → ¬*p*)) |
|---|---|---|---|---|---|---|
| T | T | T | T | F | F | F |
| T | T | F | T | T | T | T |
| T | F | T | T | F | F | F |
| T | F | F | F | T | T | T |
| F | T | T | T | T | T | T |
| F | T | F | T | T | T | T |
| F | F | T | T | T | T | T |
| F | F | F | F | T | T | T |

The computation of the last column of the third line may be displayed as follows:

p

→

(q

∨

r

→

(r

→

¬

p))

T

→

(F

∨

T

→

(T

→

¬

T))

T

→

(

T

→

(T

→

F

))

T

→

(

T

→

F

)

T

→

F

F

T

F

F

T

T

F

T

F

F

T

Further, using the theorem that $\varphi \models \psi$ if, and only if, $(\varphi \to \psi )$ is valid, we can use a truth table to prove that a formula is a semantic consequence of a set of formulas: $\{\varphi _{1},\varphi _{2},\varphi _{3},...,\varphi _{n}\}\models \psi$ if, and only if, we can produce a truth table that comes out all true for the formula $\left(\left(\bigwedge _{i=1}^{n}\varphi _{i}\right)\rightarrow \psi \right)$ (that is, if $\models \left(\left(\bigwedge _{i=1}^{n}\varphi _{i}\right)\rightarrow \psi \right)$ ).


## Semantic proof via tableaux

Since truth tables have 2n lines for n variables, they can be tiresomely long for large values of n. Analytic tableaux are a more efficient, but nevertheless mechanical, semantic proof method; they take advantage of the fact that "we learn nothing about the validity of the inference from examining the truth-value distributions which make either the premises false or the conclusion true: the only relevant distributions when considering deductive validity are clearly just those which make the premises true or the conclusion false."

Analytic tableaux for propositional logic are fully specified by the rules that are stated in schematic form below. These rules use "signed formulas", where a signed formula is an expression $TX$ or $FX$ , where X is a (unsigned) formula of the language ${\mathcal {L}}$ . (Informally, $TX$ is read " X is true", and $FX$ is read " X is false".) Their formal semantic definition is that "under any interpretation, a signed formula $TX$ is called true if X is true, and false if X is false, whereas a signed formula $FX$ is called false if X is true, and true if X is false."

${\begin{aligned}&1)\quad {\frac {T\sim X}{FX}}\quad &&{\frac {F\sim X}{TX}}\\{\phantom {spacer}}\\&2)\quad {\frac {T(X\land Y)}{\begin{matrix}TX\\TY\end{matrix}}}\quad &&{\frac {F(X\land Y)}{FX|FY}}\\{\phantom {spacer}}\\&3)\quad {\frac {T(X\lor Y)}{TX|TY}}\quad &&{\frac {F(X\lor Y)}{\begin{matrix}FX\\FY\end{matrix}}}\\{\phantom {spacer}}\\&4)\quad {\frac {T(X\supset Y)}{FX|TY}}\quad &&{\frac {F(X\supset Y)}{\begin{matrix}TX\\FY\end{matrix}}}\end{aligned}}$

In this notation, rule 2 means that $T(X\land Y)$ yields both $TX,TY$ , whereas $F(X\land Y)$ *branches* into $FX,FY$ . The notation is to be understood analogously for rules 3 and 4. Often, in tableaux for classical logic, the *signed formula* notation is simplified so that $T\varphi$ is written simply as $\varphi$ , and $F\varphi$ as $\neg \varphi$ , which accounts for naming rule 1 the "*Rule of Double Negation*".

One constructs a tableau for a set of formulas by applying the rules to produce more lines and tree branches until every line has been used, producing a *complete* tableau. In some cases, a branch can come to contain both $TX$ and $FX$ for some X , which is to say, a contradiction. In that case, the branch is said to **close**. If every branch in a tree closes, the tree itself is said to close. In virtue of the rules for construction of tableaux, a closed tree is a proof that the original formula, or set of formulas, used to construct it was itself self-contradictory, and therefore false. Conversely, a tableau can also prove that a logical formula is tautologous: if a formula is tautologous, its negation is a contradiction, so a tableau built from its negation will close.

To construct a tableau for an argument $\langle \{\varphi _{1},\varphi _{2},\varphi _{3},...,\varphi _{n}\},\psi \rangle$ , one first writes out the set of premise formulas, $\{\varphi _{1},\varphi _{2},\varphi _{3},...,\varphi _{n}\}$ , with one formula on each line, signed with T (that is, $T\varphi$ for each $T\varphi$ in the set); and together with those formulas (the order is unimportant), one also writes out the conclusion, $\psi$ , signed with F (that is, $F\psi$ ). One then produces a truth tree (analytic tableau) by using all those lines according to the rules. A closed tree will be proof that the argument was valid, in virtue of the fact that $\varphi \models \psi$ if, and only if, $\{\varphi ,\sim \psi \}$ is inconsistent (also written as $\varphi ,\sim \psi \models$ ).


## List of classically valid argument forms

Using semantic checking methods, such as truth tables or semantic tableaux, to check for tautologies and semantic consequences, it can be shown that, in classical logic, the following classical argument forms are semantically valid, i.e., these tautologies and semantic consequences hold. We use $\varphi$ ⟚ $\psi$ to denote equivalence of $\varphi$ and $\psi$ , that is, as an abbreviation for both $\varphi \models \psi$ and $\psi \models \varphi$ ; as an aid to reading the symbols, a description of each formula is given. The description reads the symbol ⊧ (called the "double turnstile") as "therefore", which is a common reading of it, although many authors prefer to read it as "entails", or as "models".

| Name | Sequent | Description |
|---|---|---|
| Modus Ponens | $((p\to q)\land p)\models q$ | If p then q; p; therefore q |
| Modus Tollens | $((p\to q)\land \neg q)\models \neg p$ | If p then q; not q; therefore not p |
| Hypothetical Syllogism | $((p\to q)\land (q\to r))\models (p\to r)$ | If p then q; if q then r; therefore, if p then r |
| Disjunctive Syllogism | $((p\lor q)\land \neg p)\models q$ | Either p or q, or both; not p; therefore, q |
| Constructive Dilemma | $((p\to q)\land (r\to s)\land (p\lor r))\models (q\lor s)$ | If p then q; and if r then s; but p or r; therefore q or s |
| Destructive Dilemma | $((p\to q)\land (r\to s)\land (\neg q\lor \neg s))\models (\neg p\lor \neg r)$ | If p then q; and if r then s; but not q or not s; therefore not p or not r |
| Bidirectional Dilemma | $((p\to q)\land (r\to s)\land (p\lor \neg s))\models (q\lor \neg r)$ | If p then q; and if r then s; but p or not s; therefore q or not r |
| Simplification | $(p\land q)\models p$ | p and q are true; therefore p is true |
| Conjunction | $p,q\models (p\land q)$ | p and q are true separately; therefore they are true conjointly |
| Addition | $p\models (p\lor q)$ | p is true; therefore the disjunction (p or q) is true |
| Composition of conjunction | $((p\to q)\land (p\to r))$ ⟚ $(p\to (q\land r))$ | If p then q; and if p then r; therefore if p is true then q and r are true |
| Composition of disjunction | $((p\to q)\lor (p\to r))$ ⟚ $(p\to (q\lor r))$ | If p then q; or if p then r; therefore if p is true then q or r is true |
| De Morgan's Theorem (1) | $\neg (p\land q)$ ⟚ $(\neg p\lor \neg q)$ | The negation of (p and q) is equiv. to (not p or not q) |
| De Morgan's Theorem (2) | $\neg (p\lor q)$ ⟚ $(\neg p\land \neg q)$ | The negation of (p or q) is equiv. to (not p and not q) |
| Commutation (1) | $(p\lor q)$ ⟚ $(q\lor p)$ | (p or q) is equiv. to (q or p) |
| Commutation (2) | $(p\land q)$ ⟚ $(q\land p)$ | (p and q) is equiv. to (q and p) |
| Commutation (3) | $(p\leftrightarrow q)$ ⟚ $(q\leftrightarrow p)$ | (p iff q) is equiv. to (q iff p) |
| Association (1) | $(p\lor (q\lor r))$ ⟚ $((p\lor q)\lor r)$ | p or (q or r) is equiv. to (p or q) or r |
| Association (2) | $(p\land (q\land r))$ ⟚ $((p\land q)\land r)$ | p and (q and r) is equiv. to (p and q) and r |
| Distribution (1) | $(p\land (q\lor r))$ ⟚ $((p\land q)\lor (p\land r))$ | p and (q or r) is equiv. to (p and q) or (p and r) |
| Distribution (2) | $(p\lor (q\land r))$ ⟚ $((p\lor q)\land (p\lor r))$ | p or (q and r) is equiv. to (p or q) and (p or r) |
| Double Negation | p ⟚ $\neg \neg p$ | p is equivalent to the negation of not p |
| Transposition | $(p\to q)$ ⟚ $(\neg q\to \neg p)$ | If p then q is equiv. to if not q then not p |
| Material Implication | $(p\to q)$ ⟚ $(\neg p\lor q)$ | If p then q is equiv. to not p or q |
| Material Equivalence (1) | $(p\leftrightarrow q)$ ⟚ $((p\to q)\land (q\to p))$ | (p iff q) is equiv. to (if p is true then q is true) and (if q is true then p is true) |
| Material Equivalence (2) | $(p\leftrightarrow q)$ ⟚ $((p\land q)\lor (\neg p\land \neg q))$ | (p iff q) is equiv. to either (p and q are true) or (both p and q are false) |
| Material Equivalence (3) | $(p\leftrightarrow q)$ ⟚ $((p\lor \neg q)\land (\neg p\lor q))$ | (p iff q) is equiv to., both (p or not q is true) and (not p or q is true) |
| Exportation | $((p\land q)\to r)\models (p\to (q\to r))$ | from (if p and q are true then r is true) we can prove (if q is true then r is true, if p is true) |
| Importation | $(p\to (q\to r))\models ((p\land q)\to r)$ | If p then (if q then r) is equivalent to if p and q then r |
| Idempotence of disjunction | p ⟚ $(p\lor p)$ | p is true is equiv. to p is true or p is true |
| Idempotence of conjunction | p ⟚ $(p\land p)$ | p is true is equiv. to p is true and p is true |
| Tertium non datur (Law of Excluded Middle) | $\models (p\lor \neg p)$ | p or not p is true |
| Law of Non-Contradiction | $\models \neg (p\land \neg p)$ | p and not p is false, is a true statement |
| Explosion | $(p\land \neg p)\models q$ | p and not p; therefore q |
