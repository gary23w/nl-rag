---
title: "First-order logic (part 1/2)"
source: https://en.wikipedia.org/wiki/First-order_logic
domain: descriptive-complexity
license: CC-BY-SA-4.0
tags: descriptive complexity, second order logic, fagin theorem, finite model theory
fetched: 2026-07-02
part: 1/2
---

# First-order logic

**First-order logic**, also called **predicate logic**, **predicate calculus**, or **quantificational logic**, is a type of formal system used in mathematics, philosophy, linguistics, and computer science. First-order logic uses quantified variables over non-logical objects, and allows the use of sentences that contain variables. Rather than propositions such as "all humans are mortal", in first-order logic one can have expressions in the form "for all *x*, if *x* is a human, then *x* is mortal", where "for all *x*" is a quantifier, *x* is a variable, and "... *is a human*" and "... *is mortal*" are predicates. This distinguishes it from propositional logic, which does not use quantifiers or relations; in this sense, first-order logic is an extension of propositional logic.

A theory about a topic, such as set theory, a theory for groups, or a formal theory of arithmetic, is usually a first-order logic together with a specified domain of discourse (over which the quantified variables range), finitely many functions from that domain to itself, finitely many predicates defined on that domain, and a set of axioms believed to hold about them. "Theory" is sometimes understood in a more formal sense as just a set of sentences in first-order logic.

The term "first-order" distinguishes first-order logic from higher-order logic, in which there are predicates having predicates or functions as arguments, or in which quantification over predicates, functions, or both, are permitted. In first-order theories, predicates are often associated with sets. In interpreted higher-order theories, predicates may be interpreted as sets of sets.

There are many deductive systems for first-order logic which are both sound, i.e. all provable statements are true in all models; and complete, i.e. all statements which are true in all models are provable. Although the logical consequence relation is only semidecidable, much progress has been made in automated theorem proving in first-order logic. First-order logic also satisfies several metalogical theorems that make it amenable to analysis in proof theory, such as the Löwenheim–Skolem theorem and the compactness theorem.

First-order logic is the standard for the formalization of mathematics into axioms, and is studied in the foundations of mathematics. Peano arithmetic and Zermelo–Fraenkel set theory are axiomatizations of number theory and set theory, respectively, into first-order logic. No first-order theory, however, has the strength to uniquely describe a structure with an infinite domain, such as the natural numbers or the real line. Axiom systems that do fully describe these two structures, i.e. categorical axiom systems, can be obtained in stronger logics such as second-order logic.

Historically speaking, the foundations of first-order logic were developed independently by Gottlob Frege and Charles Sanders Peirce in the 1880s. However, the distinction between first-order and higher-order logic was not well understood until metalogical ideas and results arrived, such as Gödel's completeness theorem in 1929. By the 1940s, first-order logic had become the dominant language of mathematical foundations.


## Introduction

While propositional logic deals with simple declarative propositions, first-order logic additionally covers predicates and quantification. A predicate evaluates to true or false for an entity or entities in the domain of discourse.

Consider the two sentences "Socrates is a philosopher" and "Plato is a philosopher". In propositional logic, these sentences themselves are viewed as the individuals of study, and might be denoted, for example, by variables such as *p* and *q*. They are not viewed as an application of a predicate, such as ${\text{isPhilosopher}}$ , to any particular objects in the domain of discourse, instead viewing them as purely an utterance which is either true or false. However, in first-order logic, these two sentences may be framed as statements that a certain individual or non-logical object has a property. In this example, both sentences happen to have the common form ${\text{isPhilosopher}}(x)$ for some individual x , in the first sentence the value of the variable *x* is "Socrates", and in the second sentence it is "Plato". Due to the ability to speak about non-logical individuals along with the original logical connectives, first-order logic includes propositional logic.

The truth of a formula such as "*x* is a philosopher" depends on which object is denoted by *x* and on the interpretation of the predicate "is a philosopher". Consequently, "*x* is a philosopher" alone does not have a definite truth value of true or false, and is akin to a sentence fragment. Relationships between predicates can be stated using logical connectives. For example, the first-order formula "if *x* is a philosopher, then *x* is a scholar", is a conditional statement with "*x* is a philosopher" as its hypothesis, and "*x* is a scholar" as its conclusion, which again needs specification of *x* in order to have a definite truth value.

Quantifiers can be applied to variables in a formula. The variable *x* in the previous formula can be universally quantified, for instance, with the first-order sentence "For every *x*, if *x* is a philosopher, then *x* is a scholar". The universal quantifier "for every" in this sentence expresses the idea that the claim "if *x* is a philosopher, then *x* is a scholar" holds for *all* choices of *x*.

The *negation* of the sentence "For every *x*, if *x* is a philosopher, then *x* is a scholar" is logically equivalent to the sentence "There exists *x* such that *x* is a philosopher and *x* is not a scholar". The existential quantifier "there exists" expresses the idea that the claim "*x* is a philosopher and *x* is not a scholar" holds for *some* choice of *x*.

The predicates "is a philosopher" and "is a scholar" each take a single variable. In general, predicates can take several variables. In the first-order sentence "Socrates is the teacher of Plato", the predicate "is the teacher of" takes two variables.

An interpretation (or model) of a first-order formula specifies what each predicate means, and the entities that can instantiate the variables. These entities form the domain of discourse or universe, which is usually required to be a nonempty set. For example, consider the sentence "There exists *x* such that *x* is a philosopher." This sentence is seen as being true in an interpretation under which the domain of discourse consists of all human beings, and the predicate "is a philosopher" is understood as "was the author of the *Republic*." It is thus true in the case of Plato.

There are two key parts of first-order logic. The syntax determines which finite sequences of symbols are well-formed expressions in first-order logic, while the semantics determines the meanings behind these expressions.


## Syntax

Unlike natural languages, such as English, the language of first-order logic is completely formal, so that it can be mechanically determined whether a given expression is well formed. There are two key types of well-formed expressions: *terms*, which intuitively represent objects, and *formulas*, which intuitively express statements that can be true or false. The terms and formulas of first-order logic are strings of *symbols*, where all the symbols together form the *alphabet* of the language.

### Alphabet

As with all formal languages, the nature of the symbols themselves is outside the scope of formal logic; they are often regarded simply as letters and punctuation symbols.

It is common to divide the symbols of the alphabet into *logical symbols*, which always have the same meaning, and *non-logical symbols*, whose meaning varies by interpretation. For example, the logical symbol $\land$ always represents "and"; it is never interpreted as "or", which is represented by the logical symbol $\lor$ . However, a non-logical predicate symbol such as Phil(*x*) could be interpreted to mean "*x* is a philosopher", "*x* is a man named Philip", or any other unary predicate depending on the interpretation at hand.

#### Logical symbols

Logical symbols are a set of characters that vary by author, but usually include the following:

- Quantifier symbols: ∀ for universal quantification, and ∃ for existential quantification
- Logical connectives: ∧ for conjunction, ∨ for disjunction, → for implication, ↔ for biconditional, ¬ for negation. Some authors use C*pq* instead of → and E*pq* instead of ↔, especially in contexts where → is used for other purposes. Moreover, the horseshoe ⊃ may replace →; the triple-bar ≡ may replace ↔; a tilde (~), N*p*, or F*p* may replace ¬; a double bar $\|$ , + , or A*pq* may replace ∨; and an ampersand &, K*pq*, or the middle dot ⋅ may replace ∧, especially if these symbols are not available for technical reasons.
- Parentheses, brackets, and other punctuation symbols. The choice of such symbols varies depending on context.
- An infinite set of *variables*, often denoted by lowercase letters at the end of the alphabet *x*, *y*, *z*, ... . Subscripts are often used to distinguish variables: *x*0, *x*1, *x*2, ... .
- An *equality symbol* (sometimes, *identity symbol*) = (see § Equality and its axioms below).

Not all of these symbols are required in first-order logic. Either one of the quantifiers along with negation, conjunction (or disjunction), variables, brackets, and equality suffices.

Other logical symbols include the following:

- Truth constants: T, or ⊤ for "true" and F, or ⊥ for "false". Without any such logical operators of valence 0, these two constants can only be expressed using quantifiers.
- Additional logical connectives such as the Sheffer stroke, D*pq* (NAND), and exclusive or, J*pq*.

#### Non-logical symbols

Non-logical symbols represent predicates (relations), functions and constants. It used to be standard practice to use a fixed, infinite set of non-logical symbols for all purposes:

- For every integer *n* ≥ 0, there is a collection of *n*-*ary*, or *n*-*place*, *predicate symbols*. Because they represent relations between *n* elements, they are also called *relation symbols*. For each arity *n*, there is an infinite supply of them: *P**n*0, *P**n*1, *P**n*2, *P**n*3, ...
- For every integer *n* ≥ 0, there are infinitely many *n*-ary *function symbols*: *f n*0, *f n*1, *f n*2, *f n*3, ...

When the arity of a predicate symbol or function symbol is clear from context, the superscript *n* is often omitted.

In this traditional approach, there is only one language of first-order logic. This approach is still common, especially in philosophically oriented books.

A more recent practice is to use different non-logical symbols according to the application one has in mind. Therefore, it has become necessary to name the set of all non-logical symbols used in a particular application. This choice is made via a *signature*.

Typical signatures in mathematics are {1, ×} or just {×} for groups, or {0, 1, +, ×, <} for ordered fields. There are no restrictions on the number of non-logical symbols. The signature can be empty, finite, or infinite, even uncountable. Uncountable signatures occur for example in modern proofs of the Löwenheim–Skolem theorem.

Though signatures might in some cases imply how non-logical symbols are to be interpreted, interpretation of the non-logical symbols in the signature is separate (and not necessarily fixed). Signatures concern syntax rather than semantics.

In this approach, every non-logical symbol is of one of the following types:

- A *predicate symbol* (or *relation symbol*) with some *valence* (or *arity*, number of arguments) greater than or equal to 0. These are often denoted by uppercase letters such as *P*, *Q* and *R*. Examples:
  - In *P*(*x*), *P* is a predicate symbol of valence 1. One possible interpretation is "*x* is a man".
  - In *Q*(*x*,*y*), *Q* is a predicate symbol of valence 2. Possible interpretations include "*x* is greater than *y*" and "*x* is the father of *y*".
  - Relations of valence 0 can be identified with propositional variables, which can stand for any statement. One possible interpretation of *R* is "Socrates is a man".
- A *function symbol*, with some valence greater than or equal to 0. These are often denoted by lowercase roman letters such as *f*, *g* and *h*. Examples:
  - *f*(*x*) may be interpreted as "the father of *x*". In arithmetic, it may stand for "-x". In set theory, it may stand for "the power set of x".
  - In arithmetic, *g*(*x*,*y*) may stand for "*x*+*y*". In set theory, it may stand for "the union of *x* and *y*".
  - Function symbols of valence 0 are called *constant symbols*, and are often denoted by lowercase letters at the beginning of the alphabet such as *a*, *b* and *c*. The symbol *a* may stand for Socrates. In arithmetic, it may stand for 0. In set theory, it may stand for the empty set.

The traditional approach can be recovered in the modern approach, by simply specifying the "custom" signature to consist of the traditional sequences of non-logical symbols.

### Formation rules

| BNF grammar |
|---|
| <index> ::= "" \| <index> "'" <variable> ::= "x" <index> <constant> ::= "c" <index> <unary function> ::= "f1" <index> <binary function> ::= "f2" <index> <ternary function> ::= "f3" <index> <unary predicate> ::= "p1" <index> <binary predicate> ::= "p2" <index> <ternary predicate> ::= "p3" <index> <term> ::= <variable> \| <constant> \| <unary function> "(" <term> ")" \| <binary function> "(" <term> "," <term> ")" \| <ternary function> "(" <term> "," <term> "," <term> ")" <atomic formula> ::= "TRUE" \| "FALSE" \| <term> "=" <term> \| <unary predicate> "(" <term> ")" \| <binary predicate> "(" <term> "," <term> ")" \| <ternary predicate> "(" <term> "," <term> "," <term> ")" <formula> ::= <atomic formula> \| "¬" <formula> \| <formula> "∧" <formula> \| <formula> "∨" <formula> \| <formula> "⇒" <formula> \| <formula> "⇔" <formula> \| "(" <formula> ")" \| "∀" <variable> <formula> \| "∃" <variable> <formula> |
| The above context-free grammar in Backus-Naur form defines the language of syntactically valid first-order formulas with function symbols and predicate symbols up to arity 3. For higher arities, it needs to be adapted accordingly. |
| The example formula `∀x ∃x' (¬x=c) ⇒ f2(x,x')=c'` describes multiplicative inverses when `f2'`, `c`, and `c'` are interpreted as multiplication, zero, and one, respectively. |

The formation rules define the terms and formulas of first-order logic. When terms and formulas are represented as strings of symbols, these rules can be used to write a formal grammar for terms and formulas. These rules are generally context-free (each production has a single symbol on the left side), except that the set of symbols may be allowed to be infinite and there may be many start symbols, for example the variables in the case of terms.

#### Terms

The set of *terms* is inductively defined by the following rules:

1. *Variables*. Any variable symbol is a term.
2. *Functions*. If *f* is an *n*-ary function symbol, and *t*1, ..., *t**n* are terms, then *f*(*t*1,...,*t**n*) is a term. In particular, symbols denoting individual constants are nullary function symbols, and thus are terms.

Only expressions which can be obtained by finitely many applications of rules 1 and 2 are terms. For example, no expression involving a predicate symbol is a term.

#### Formulas

The set of *formulas* (also called *well-formed formulas* or *WFFs*) is inductively defined by the following rules:

1. *Predicate symbols*. If *P* is an *n*-ary predicate symbol and *t*1, ..., *t**n* are terms then *P*(*t*1,...,*t**n*) is a formula.
  - *Equality*. If the equality symbol is considered part of logic, and *t*1 and *t*2 are terms, then *t*1 = *t*2 is a formula.
2. *Negation*. If $\varphi$ is a formula, then $\lnot \varphi$ is a formula.
3. *Binary connectives*. If ⁠ $\varphi$ ⁠ and ⁠ $\psi$ ⁠ are formulas, then ( $\varphi \rightarrow \psi$ ) is a formula. Similar rules apply to other binary logical connectives.
4. *Quantifiers*. If $\varphi$ is a formula and *x* is a variable, then $\forall x\varphi$ (for all x, $\varphi$ holds) and $\exists x\varphi$ (there exists x such that $\varphi$ ) are formulas.

Only expressions which can be obtained by finitely many applications of rules 1–4 are formulas. The formulas obtained from the first rule are said to be *atomic formulas*.

For example:

$\forall x\forall y(P(f(x))\rightarrow \neg (P(x)\rightarrow Q(f(y),x,z)))$

is a formula, if *f* is a unary function symbol, *P* a unary predicate symbol, and Q a ternary predicate symbol. However, $\forall x\,x\rightarrow$ is not a formula, although it is a string of symbols from the alphabet.

The role of the parentheses in the definition is to ensure that any formula can only be obtained in one way—by following the inductive definition (i.e., there is a unique parse tree for each formula). This property is known as *unique readability* of formulas. There are many conventions for where parentheses are used in formulas. For example, some authors use colons or full stops instead of parentheses, or change the places in which parentheses are inserted. Each author's particular definition must be accompanied by a proof of unique readability.

#### Notational conventions

For convenience, conventions have been developed about the precedence of the logical operators, to avoid the need to write parentheses in some cases. These rules are similar to the order of operations in arithmetic. A common convention is:

- $\lnot$ is evaluated first
- $\land$ and $\lor$ are evaluated next
- Quantifiers are evaluated next
- $\to$ and $\leftrightarrow$ are evaluated last.

Moreover, extra punctuation not required by the definition may be inserted—to make formulas easier to read. Thus the formula:

$\lnot \forall xP(x)\to \exists x\lnot P(x)$

might be written as:

$(\lnot [\forall xP(x)])\to \exists x[\lnot P(x)].$

### Free and bound variables

In a formula, a variable may occur *free* or *bound* (or both). One formalization of this notion is due to Quine, first the concept of a variable occurrence is defined, then whether a variable occurrence is free or bound, then whether a variable symbol overall is free or bound. In order to distinguish different occurrences of the identical symbol *x*, each occurrence of a variable symbol *x* in a formula φ is identified with the initial substring of φ up to the point at which said instance of the symbol *x* appears.p. 297 Then, an occurrence of *x* is said to be bound if that occurrence of *x* lies within the scope of at least one of either $\exists x$ or $\forall x$ . Finally, *x* is bound in φ if all occurrences of *x* in φ are bound.pp. 142–143

Intuitively, a variable symbol is free in a formula if at no point is it quantified:pp. 142–143 in ∀*y* *P*(*x*, *y*), the sole occurrence of variable *x* is free while that of *y* is bound. The free and bound variable occurrences in a formula are defined inductively as follows.

**Atomic formulas**

If

φ

is an atomic formula, then

x

occurs free in

φ

if and only if

x

occurs in

φ

. Moreover, there are no bound variables in any atomic formula.

**Negation**

x

occurs free in ¬

φ

if and only if

x

occurs free in

φ

.

x

occurs bound in ¬

φ

if and only if

x

occurs bound in

φ

**Binary connectives**

x

occurs free in (

φ

→

ψ

) if and only if

x

occurs free in either

φ

or

ψ

.

x

occurs bound in (

φ

→

ψ

) if and only if

x

occurs bound in either

φ

or

ψ

. The same rule applies to any other binary connective in place of →.

**Quantifiers**

x

occurs free in

∀

y

φ

, if and only if x occurs free in

φ

and

x

is a different symbol from

y

. Also,

x

occurs bound in

∀

y

φ

, if and only if

x

is

y

or

x

occurs bound in

φ

. The same rule holds with

∃

in place of

∀

.

For example, in ∀*x* ∀*y* (*P*(*x*) → *Q*(*x*,*f*(*x*),*z*)), *x* and *y* occur only bound, *z* occurs only free, and *w* is neither because it does not occur in the formula.

Free and bound variables of a formula need not be disjoint sets: in the formula *P*(*x*) → ∀*x* *Q*(*x*), the first occurrence of *x*, as argument of *P*, is free while the second one, as argument of *Q*, is bound.

A formula in first-order logic with no free variable occurrences is called a *first-order sentence*. These are the formulas that will have well-defined truth values under an interpretation. For example, whether a formula such as Phil(*x*) is true must depend on what *x* represents. But the sentence ∃*x* Phil(*x*) will be either true or false in a given interpretation.

### Example: ordered abelian groups

In mathematics, the language of ordered abelian groups has one constant symbol 0, one unary function symbol −, one binary function symbol +, and one binary relation symbol ≤. Then:

- The expressions +(*x*, *y*) and +(*x*, +(*y*, −(*z*))) are *terms*. These are usually written as *x* + *y* and *x* + *y* − *z*.
- The expressions +(*x*, *y*) = 0 and ≤(+(*x*, +(*y*, −(*z*))), +(*x*, *y*)) are *atomic formulas*. These are usually written as *x* + *y* = 0 and *x* + *y* − *z*  ≤  *x* + *y*.
- The expression $(\forall x\forall y\,[\mathop {\leq } (\mathop {+} (x,y),z)\to \forall x\,\forall y\,\mathop {+} (x,y)=0)]$ is a *formula*, which is usually written as $\forall x\forall y(x+y\leq z)\to \forall x\forall y(x+y=0).$ This formula has one free variable, *z*.

The axioms for ordered abelian groups can be expressed as a set of sentences in the language. For example, the axiom stating that the group is commutative is usually written $(\forall x)(\forall y)[x+y=y+x].$


## Semantics

An interpretation of a first-order language assigns a denotation to each non-logical symbol (predicate symbol, function symbol, or constant symbol) in that language. It also determines a domain of discourse that specifies the range of the quantifiers. The result is that each term is assigned an object that it represents, each predicate is assigned a property of objects, and each sentence is assigned a truth value. In this way, an interpretation provides semantic meaning to the terms, predicates, and formulas of the language. The study of the interpretations of formal languages is called formal semantics. What follows is a description of the standard or Tarskian semantics for first-order logic. (It is also possible to define game semantics for first-order logic, but aside from requiring the axiom of choice, game semantics agree with Tarskian semantics for first-order logic, so game semantics will not be elaborated herein.)

### First-order structures

The most common way of specifying an interpretation (especially in mathematics) is to specify a *structure* (also called a *model*; see below). The structure consists of a domain of discourse *D* and an interpretation function I mapping non-logical symbols to predicates, functions, and constants.

The domain of discourse *D* is a nonempty set of "objects" of some kind. Intuitively, given an interpretation, a first-order formula becomes a statement about these objects; for example, $\exists xP(x)$ states the existence of some object in *D* for which the predicate *P* is true (or, more precisely, for which the predicate assigned to the predicate symbol *P* by the interpretation is true). For example, one can take *D* to be the set of integers.

Non-logical symbols are interpreted as follows:

- The interpretation of an *n*-ary function symbol is a function from *D**n* to *D*. For example, if the domain of discourse is the set of integers, a function symbol *f* of arity 2 can be interpreted as the function that gives the sum of its arguments. In other words, the symbol *f* is associated with the function ⁠ $I(f)$ ⁠ which, in this interpretation, is addition.
- The interpretation of a constant symbol (a function symbol of arity 0) is a function from *D*0 (a set whose only member is the empty tuple) to *D*, which can be simply identified with an object in *D*. For example, an interpretation may assign the value $I(c)=10$ to the constant symbol c .
- The interpretation of an *n*-ary predicate symbol is a set of *n*-tuples of elements of *D*, giving the arguments for which the predicate is true. For example, an interpretation $I(P)$ of a binary predicate symbol *P* may be the set of pairs of integers such that the first one is less than the second. According to this interpretation, the predicate *P* would be true if its first argument is less than its second argument. Equivalently, predicate symbols may be assigned Boolean-valued functions from *D**n* to $\{\mathrm {true,false} \}$ .

### Evaluation of truth values

A formula evaluates to true or false given an interpretation and a **variable assignment** μ that associates an element of the domain of discourse with each variable. The reason that a variable assignment is required is to give meanings to formulas with free variables, such as $y=x$ . The truth value of this formula changes depending on the values that *x* and *y* denote.

First, the variable assignment μ can be extended to all terms of the language, with the result that each term maps to a single element of the domain of discourse. The following rules are used to make this assignment:

- *Variables*. Each variable *x* evaluates to *μ*(*x*)
- *Functions*. Given terms $t_{1},\ldots ,t_{n}$ that have been evaluated to elements $d_{1},\ldots ,d_{n}$ of the domain of discourse, and a *n*-ary function symbol *f*, the term $f(t_{1},\ldots ,t_{n})$ evaluates to $(I(f))(d_{1},\ldots ,d_{n})$ .

Next, each formula is assigned a truth value. The inductive definition used to make this assignment is called the T-schema.

- *Atomic formulas (1)*. A formula $P(t_{1},\ldots ,t_{n})$ is associated the value true or false depending on whether $\langle v_{1},\ldots ,v_{n}\rangle \in I(P)$ , where $v_{1},\ldots ,v_{n}$ are the evaluation of the terms $t_{1},\ldots ,t_{n}$ and $I(P)$ is the interpretation of P , which by assumption is a subset of $D^{n}$ .
- *Atomic formulas (2)*. A formula $t_{1}=t_{2}$ is assigned true if $t_{1}$ and $t_{2}$ evaluate to the same object of the domain of discourse (see the section on equality below).
- *Logical connectives*. A formula in the form $\neg \varphi$ , $\varphi \rightarrow \psi$ , etc. is evaluated according to the truth table for the connective in question, as in propositional logic.
- *Existential quantifiers*. A formula $\exists x\varphi (x)$ is true according to *M* and $\mu$ if there exists an evaluation $\mu '$ of the variables that differs from $\mu$ at most regarding the evaluation of *x* and such that φ is true according to the interpretation *M* and the variable assignment $\mu '$ . This formal definition captures the idea that $\exists x\varphi (x)$ is true if and only if there is a way to choose a value for *x* such that φ(*x*) is satisfied.
- *Universal quantifiers*. A formula $\forall x\varphi (x)$ is true according to *M* and $\mu$ if φ(*x*) is true for every pair composed by the interpretation *M* and some variable assignment $\mu '$ that differs from $\mu$ at most on the value of *x*. This captures the idea that $\forall x\varphi (x)$ is true if every possible choice of a value for *x* causes φ(*x*) to be true.

If a formula does not contain free variables, and thus is a sentence, then the initial variable assignment does not affect its truth value. In other words, a sentence is true according to *M* and $\mu$ if and only if it is true according to *M* and every other variable assignment $\mu '$ .

There is a second common approach to defining truth values that does not rely on variable assignment functions. Instead, given an interpretation *M*, one first adds to the signature a collection of constant symbols, one for each element of the domain of discourse in *M*; say that for each *d* in the domain the constant symbol *c**d* is fixed. The interpretation is extended so that each new constant symbol is assigned to its corresponding element of the domain. One now defines truth for quantified formulas syntactically, as follows:

- *Existential quantifiers (alternate)*. A formula $\exists x\varphi (x)$ is true according to *M* if there is some *d* in the domain of discourse such that $\varphi (c_{d})$ holds. Here $\varphi (c_{d})$ is the result of substituting *c**d* for every free occurrence of *x* in φ.
- *Universal quantifiers (alternate)*. A formula $\forall x\varphi (x)$ is true according to *M* if, for every *d* in the domain of discourse, $\varphi (c_{d})$ is true according to *M*.

This alternate approach gives exactly the same truth values to all sentences as the approach via variable assignments.

### Validity, satisfiability, and logical consequence

If a sentence φ evaluates to *true* under a given interpretation *M*, one says that *M* *satisfies* φ; this is denoted $M\vDash \varphi$ . A sentence is *satisfiable* if there is some interpretation under which it is true. This is a bit different from the symbol $\vDash$ from model theory, where $M\vDash \phi$ denotes satisfiability in a model, i.e. "there is a suitable assignment of values in M 's domain to variable symbols of $\phi$ ".

Satisfiability of formulas with free variables is more complicated, because an interpretation on its own does not determine the truth value of such a formula. The most common convention is that a formula φ with free variables $x_{1}$ , ..., $x_{n}$ is said to be satisfied by an interpretation if the formula φ remains true regardless which individuals from the domain of discourse are assigned to its free variables $x_{1}$ , ..., $x_{n}$ . This has the same effect as saying that a formula φ is satisfied if and only if its universal closure $\forall x_{1}\dots \forall x_{n}\phi (x_{1},\dots ,x_{n})$ is satisfied.

A formula is *logically valid* (or simply *valid*) if it is true in every interpretation. These formulas play a role similar to tautologies in propositional logic.

A formula φ is a *logical consequence* of a formula ψ if every interpretation that makes ψ true also makes φ true. In this case one says that φ is logically implied by ψ.

### Algebraizations

An alternate approach to the semantics of first-order logic proceeds via abstract algebra. This approach generalizes the Lindenbaum–Tarski algebras of propositional logic. There are three ways of eliminating quantified variables from first-order logic that do not involve replacing quantifiers with other variable binding term operators:

- Cylindric algebra, by Alfred Tarski, et al.;
- Polyadic algebra, by Paul Halmos;
- Predicate functor logic, primarily by Willard Quine.

These algebras are all lattices that properly extend the two-element Boolean algebra.

Tarski and Givant (1987) showed that the fragment of first-order logic that has no atomic sentence lying in the scope of more than three quantifiers has the same expressive power as relation algebra. This fragment is of great interest because it suffices for Peano arithmetic and most axiomatic set theory, including the canonical Zermelo–Fraenkel set theory (ZFC). They also prove that first-order logic with a primitive ordered pair is equivalent to a relation algebra with two ordered pair projection functions.

### First-order theories, models, and elementary classes

A *first-order theory* of a particular signature is a set of axioms, which are sentences consisting of symbols from that signature. The set of axioms is often finite or recursively enumerable, in which case the theory is called *effective*. Some authors require theories to also include all logical consequences of the axioms. The axioms are considered to hold within the theory and from them other sentences that hold within the theory can be derived.

A first-order structure that satisfies all sentences in a given theory is said to be a *model* of the theory. An *elementary class* is the set of all structures satisfying a particular theory. These classes are a main subject of study in model theory.

Many theories have an *intended interpretation*, a certain model that is kept in mind when studying the theory. For example, the intended interpretation of Peano arithmetic consists of the usual natural numbers with their usual operations. However, the Löwenheim–Skolem theorem shows that most first-order theories will also have other, nonstandard models.

A theory is *consistent* (within a deductive system) if it is not possible to prove a contradiction from the axioms of the theory. A theory is *complete* if, for every formula in its signature, either that formula or its negation is a logical consequence of the axioms of the theory. Gödel's incompleteness theorem shows that effective first-order theories that include a sufficient portion of the arithmetic of the natural numbers can never be both consistent and complete.

### Empty domains

The definition above requires that the domain of discourse of any interpretation must be nonempty. There are settings, such as inclusive logic, where empty domains are permitted. Moreover, if a class of algebraic structures includes an empty structure (for example, there is an empty poset), that class can only be an elementary class in first-order logic if empty domains are permitted or the empty structure is removed from the class.

There are several difficulties with empty domains, however:

- Many common rules of inference are valid only when the domain of discourse is required to be nonempty. One example is the rule stating that $\varphi \lor \exists x\psi$ implies $\exists x(\varphi \lor \psi )$ when *x* is not a free variable in $\varphi$ . This rule, which is used to put formulas into prenex normal form, is sound in nonempty domains, but unsound if the empty domain is permitted.
- The definition of truth in an interpretation that uses a variable assignment function cannot work with empty domains, because there are no variable assignment functions whose range is empty. (Similarly, one cannot assign interpretations to constant symbols.) This truth definition requires that one must select a variable assignment function (μ above) before truth values for even atomic formulas can be defined. Then the truth value of a sentence is defined to be its truth value under any variable assignment, and it is proved that this truth value does not depend on which assignment is chosen. This technique does not work if there are no assignment functions at all; it must be changed to accommodate empty domains.

Thus, when the empty domain is permitted, it must often be treated as a special case. Most authors, however, simply exclude the empty domain by definition.


## Deductive systems

A *deductive system* is used to demonstrate, on a purely syntactic basis, that one formula is a logical consequence of another formula. There are many such systems for first-order logic, including Hilbert-style deductive systems, natural deduction, the sequent calculus, the tableaux method, and resolution. These share the common property that a deduction is a finite syntactic object; the format of this object, and the way it is constructed, vary widely. These finite deductions themselves are often called *derivations* in proof theory. They are also often called *proofs* but are completely formalized unlike natural-language mathematical proofs.

A deductive system is *sound* if any formula that can be derived in the system is logically valid. Conversely, a deductive system is *complete* if every logically valid formula is derivable. All of the systems discussed in this article are both sound and complete. They also share the property that it is possible to effectively verify that a purportedly valid deduction is actually a deduction; such deduction systems are called *effective*.

A key property of deductive systems is that they are purely syntactic, so that derivations can be verified without considering any interpretation. Thus, a sound argument is correct in every possible interpretation of the language, regardless of whether that interpretation is about mathematics, economics, or some other area.

In general, logical consequence in first-order logic is only semidecidable: if a sentence A logically implies a sentence B then this can be discovered (for example, by searching for a proof until one is found, using some effective, sound, complete proof system). However, if A does not logically imply B, this does not mean that A logically implies the negation of B. There is no effective procedure that, given formulas A and B, always correctly decides whether A logically implies B.

### Rules of inference

A *rule of inference* states that, given a particular formula (or set of formulas) with a certain property as a hypothesis, another specific formula (or set of formulas) can be derived as a conclusion. The rule is sound (or truth-preserving) if it preserves validity in the sense that whenever any interpretation satisfies the hypothesis, that interpretation also satisfies the conclusion.

For example, one common rule of inference is the *rule of substitution*. If *t* is a term and φ is a formula possibly containing the variable *x*, then φ[*t*/*x*] is the result of replacing all free instances of *x* by *t* in φ. The substitution rule states that for any φ and any term *t*, one can conclude φ[*t*/*x*] from φ provided that no free variable of *t* becomes bound during the substitution process. (If some free variable of *t* becomes bound, then to substitute *t* for *x* it is first necessary to change the bound variables of φ to differ from the free variables of *t*.)

To see why the restriction on bound variables is necessary, consider the logically valid formula φ given by $\exists x(x=y)$ , in the signature of (0,1,+,×,=) of arithmetic. If *t* is the term "x + 1", the formula φ[*t*/*y*] is $\exists x(x=x+1)$ , which will be false in many interpretations. The problem is that the free variable *x* of *t* became bound during the substitution. The intended replacement can be obtained by renaming the bound variable *x* of φ to something else, say *z*, so that the formula after substitution is $\exists z(z=x+1)$ , which is again logically valid.

The substitution rule demonstrates several common aspects of rules of inference. It is entirely syntactical; one can tell whether it was correctly applied without appeal to any interpretation. It has (syntactically defined) limitations on when it can be applied, which must be respected to preserve the correctness of derivations. Moreover, as is often the case, these limitations are necessary because of interactions between free and bound variables that occur during syntactic manipulations of the formulas involved in the inference rule.

### Hilbert-style systems and natural deduction

A deduction in a Hilbert-style deductive system is a list of formulas, each of which is a *logical axiom*, a hypothesis that has been assumed for the derivation at hand or follows from previous formulas via a rule of inference. The logical axioms consist of several axiom schemas of logically valid formulas; these encompass a significant amount of propositional logic. The rules of inference enable the manipulation of quantifiers. Typical Hilbert-style systems have a small number of rules of inference, along with several infinite schemas of logical axioms. It is common to have only modus ponens and universal generalization as rules of inference.

Natural deduction systems resemble Hilbert-style systems in that a deduction is a finite list of formulas. However, natural deduction systems have no logical axioms; they compensate by adding additional rules of inference that can be used to manipulate the logical connectives in formulas in the proof.

### Sequent calculus

The sequent calculus was developed to study the properties of natural deduction systems. Instead of working with one formula at a time, it uses *sequents*, which are expressions of the form:

$A_{1},\ldots ,A_{n}\vdash B_{1},\ldots ,B_{k},$

where A1, ..., A*n*, B1, ..., B*k* are formulas and the turnstile symbol $\vdash$ is used as punctuation to separate the two halves. Intuitively, a sequent expresses the idea that $(A_{1}\land \cdots \land A_{n})$ implies $(B_{1}\lor \cdots \lor B_{k})$ .

### Tableaux method

Unlike the methods just described the derivations in the tableaux method are not lists of formulas. Instead, a derivation is a tree of formulas. To show that a formula A is provable, the tableaux method attempts to demonstrate that the negation of A is unsatisfiable. The tree of the derivation has $\lnot A$ at its root; the tree branches in a way that reflects the structure of the formula. For example, to show that $C\lor D$ is unsatisfiable requires showing that C and D are each unsatisfiable; this corresponds to a branching point in the tree with parent $C\lor D$ and children C and D.

### Resolution

The resolution rule is a single rule of inference that, together with unification, is sound and complete for first-order logic. As with the tableaux method, a formula is proved by showing that the negation of the formula is unsatisfiable. Resolution is commonly used in automated theorem proving.

The resolution method works only with formulas that are disjunctions of atomic formulas; arbitrary formulas must first be converted to this form through Skolemization. The resolution rule states that from the hypotheses $A_{1}\lor \cdots \lor A_{k}\lor C$ and $B_{1}\lor \cdots \lor B_{l}\lor \lnot C$ , the conclusion $A_{1}\lor \cdots \lor A_{k}\lor B_{1}\lor \cdots \lor B_{l}$ can be obtained.

### Provable identities

Many identities can be proved, which establish equivalences between particular formulas. These identities allow for rearranging formulas by moving quantifiers across other connectives and are useful for putting formulas in prenex normal form. Some provable identities include:

$\lnot \forall x\,P(x)\Leftrightarrow \exists x\,\lnot P(x)$

$\lnot \exists x\,P(x)\Leftrightarrow \forall x\,\lnot P(x)$

$\forall x\,\forall y\,P(x,y)\Leftrightarrow \forall y\,\forall x\,P(x,y)$

$\exists x\,\exists y\,P(x,y)\Leftrightarrow \exists y\,\exists x\,P(x,y)$

$\forall x\,P(x)\land \forall x\,Q(x)\Leftrightarrow \forall x\,(P(x)\land Q(x))$

$\exists x\,P(x)\lor \exists x\,Q(x)\Leftrightarrow \exists x\,(P(x)\lor Q(x))$

$P\land \exists x\,Q(x)\Leftrightarrow \exists x\,(P\land Q(x))$

(where

x

must not occur free in

P

)

$P\lor \forall x\,Q(x)\Leftrightarrow \forall x\,(P\lor Q(x))$

(where

x

must not occur free in

P

)


## Equality and its axioms

There are several different conventions for using equality (or identity) in first-order logic. The most common convention, known as **first-order logic with equality**, includes the equality symbol as a primitive logical symbol which is always interpreted as the real equality relation between members of the domain of discourse, such that the "two" given members are the same member. This approach also adds certain axioms about equality to the deductive system employed. These equality axioms are:

- *Reflexivity*. For each variable *x*, *x* = *x*.
- *Substitution for functions*. For all variables *x* and *y*, and any function symbol *f*, *x* = *y* → *f*(..., *x*, ...) = *f*(..., *y*, ...).
- *Substitution for formulas*. For any variables *x* and *y* and any formula φ(*z*) with a free variable z, then: *x* = *y* → (φ(x) → φ(y)).

These are axiom schemas, each of which specifies an infinite set of axioms. The third schema is known as *Leibniz's law*, "the principle of substitutivity", "the indiscernibility of identicals", or "the replacement property". The second schema, involving the function symbol *f*, is (equivalent to) a special case of the third schema, using the formula:

φ(z):

f

(...,

x

, ...) =

f

(...,

z

, ...)

Then

x

=

y

→ (

f

(...,

x

, ...) =

f

(...,

x

, ...) →

f

(...,

x

, ...) =

f

(...,

y

, ...)).

Since *x* = *y* is given, and *f*(..., *x*, ...) = *f*(..., *x*, ...) true by reflexivity, we have *f*(..., *x*, ...) = *f*(..., *y*, ...)

Many other properties of equality are consequences of the axioms above, for example:

- *Symmetry*. If *x* = *y* then *y* = *x*.
- *Transitivity*. If *x* = *y* and *y* = *z* then *x* = *z*.

### First-order logic without equality

An alternate approach considers the equality relation to be a non-logical symbol. This convention is known as *first-order logic without equality*. If an equality relation is included in the signature, the axioms of equality must now be added to the theories under consideration, if desired, instead of being considered rules of logic. The main difference between this method and first-order logic with equality is that an interpretation may now interpret two distinct individuals as "equal" (although, by Leibniz's law, these will satisfy exactly the same formulas under any interpretation). That is, the equality relation may now be interpreted by an arbitrary equivalence relation on the domain of discourse that is congruent with respect to the functions and relations of the interpretation.

When this second convention is followed, the term *normal model* is used to refer to an interpretation where no distinct individuals *a* and *b* satisfy *a* = *b*. In first-order logic with equality, only normal models are considered, and so there is no term for a model other than a normal model. When first-order logic without equality is studied, it is necessary to amend the statements of results such as the Löwenheim–Skolem theorem so that only normal models are considered.

First-order logic without equality is often employed in the context of second-order arithmetic and other higher-order theories of arithmetic, where the equality relation between sets of natural numbers is usually omitted.

### Defining equality within a theory

If a theory has a binary formula *A*(*x*,*y*) which satisfies reflexivity and Leibniz's law, the theory is said to have equality, or to be a theory with equality. The theory may not have all instances of the above schemas as axioms, but rather as derivable theorems. For example, in theories with no function symbols and a finite number of relations, it is possible to define equality in terms of the relations, by defining the two terms *s* and *t* to be equal if any relation is unchanged by changing *s* to *t* in any argument.

Some theories allow other *ad hoc* definitions of equality:

- In the theory of partial orders with one relation symbol ≤, one could define *s* = *t* to be an abbreviation for *s* ≤ *t* $\wedge$ *t* ≤ *s*.
- In set theory with one relation ∈, one may define *s* = *t* to be an abbreviation for ∀*x* (*s* ∈ *x* ↔ *t* ∈ *x*) $\wedge$ ∀*x* (*x* ∈ *s* ↔ *x* ∈ *t*). This definition of equality then automatically satisfies the axioms for equality. In this case, one should replace the usual axiom of extensionality, which can be stated as $\forall x\forall y[\forall z(z\in x\Leftrightarrow z\in y)\Rightarrow x=y]$ , with an alternative formulation $\forall x\forall y[\forall z(z\in x\Leftrightarrow z\in y)\Rightarrow \forall z(x\in z\Leftrightarrow y\in z)]$ , which says that if sets *x* and *y* have the same elements, then they also belong to the same sets.
