---
title: "Free variables and bound variables"
source: https://en.wikipedia.org/wiki/Free_variables_and_bound_variables
domain: closure-conversion
license: CC-BY-SA-4.0
tags: closure conversion, lambda lifting, free variable capture, environment representation
fetched: 2026-07-02
---

# Free variables and bound variables

In mathematics, and in other disciplines involving formal languages, including mathematical logic and computer science, a variable may be said to be either free or bound. Some older books use the terms **real variable** and **apparent variable** for **free variable** and **bound variable**, respectively. A *free variable* is a notation (symbol) that specifies places in an expression where substitution may take place and is not a parameter of this or any container expression. The idea is related to a *placeholder* (a symbol that will later be replaced by some value), or a wildcard character that stands for an unspecified symbol.

In computer programming, the term free variable refers to variables used in a function that are neither local variables nor parameters of that function. The term non-local variable is often a synonym in this context.

An instance of a variable symbol is *bound*, in contrast, if the value of that variable symbol has been bound to a specific value or range of values in the domain of discourse or universe. This may be achieved through the use of logical quantifiers, variable-binding operators, or an explicit statement of allowed values for the variable (such as, "...where n is a positive integer".)

Since the same variable symbol may appear in multiple places in an expression, some occurrences of the variable symbol may be free while others are bound, hence "free" and "bound" are at first defined for occurrences and then generalized over all occurrences of said variable symbol in the expression. A variable symbol overall is **free** if at least one occurrence of it is free.

While the domain of discourse in many contexts is understood, when an explicit range of values for the bound variable has not been given, it may be necessary to specify the domain in order to properly evaluate the expression. For example, consider the following expression in which both variables are bound by logical quantifiers:

$\forall y\,\exists x\,\left(x={\sqrt {y}}\right)$

This expression evaluates to *false* if the domain of x and y is the real numbers, but *true* if the domain is the complex numbers.

The term "dummy variable" is also sometimes used for a bound variable (more commonly in general mathematics than in computer science), but this should not be confused with the identically named but unrelated concept of dummy variable as used in statistics, most commonly in regression analysis.p.17

## Examples

Before stating a precise definition of free variable and bound variable, the following are some examples that perhaps make these two concepts clearer than the definition would:

- In the expression:

$\sum _{k=1}^{10}f(k,n),$

n

is a free variable and

k

is a bound variable; consequently the value of this expression depends on the value of

n

, but there is nothing called

k

on which it could depend.

- In the expression:

$\int _{0}^{\infty }x^{y-1}e^{-x}\,dx,$

y

is a free variable and

x

is a bound variable; consequently the value of this expression depends on the value of

y

, but there is nothing called

x

on which it could depend.

- In the expression:

$\lim _{h\rightarrow 0}{\frac {f(x+h)-f(x)}{h}},$

x

is a free variable and

h

is a bound variable; consequently the value of this expression depends on the value of

x

, but there is nothing called

h

on which it could depend.

- In the expression:

$\forall x\ \exists y\ {\Big [}\varphi (x,y,z){\Big ]},$

z

is a free variable and

x

and

y

are bound variables, associated with

logical quantifiers

; consequently the

logical value

of this expression depends on the value of

z

, but there is nothing called

x

or

y

on which it could depend.

### In proofs

In a broader context, bound variables are fundamental to the structure of mathematical proofs. For example, the following proof shows that the square of any positive even integer is divisible by 4:

> Let n be an arbitrary positive even integer. By definition, there exists an integer k such that $n=2k$ . Substituting this into the expression for the square gives $n^{2}=(2k)^{2}=4k^{2}$ . Since k is an integer, $k^{2}$ is also an integer. Therefore, $n^{2}$ is divisible by 4.

In this proof, both n and k function as bound variables, but they are bound in different ways.

The variable n is introduced as an *arbitrary but particular* element of a set. The statement "Let n be..." implicitly functions as a universal quantifier, binding n for the scope of the proof. The proof establishes a property for this single, arbitrary n , which licenses the general conclusion that the property holds for all positive even integers.

The variable k , on the other hand, is bound by an existential quantifier ("there exists an integer k "). It is introduced to represent a specific, though unnamed, integer whose existence is guaranteed by the definition of n being even. The scope of k is limited to the reasoning that follows its introduction.

Thus, neither variable is free; their meaning is entirely determined by their role within the logical structure of the proof.

### Variable-binding operators

In mathematics and logic, a number of symbols function as **variable-binding operators**. These operators take a function or an open formula as an argument and bind a free variable within that expression to a specific domain or range of values, creating a new expression whose meaning does not depend on the bound variable.

Common variable-binding operators include:

- The summation ( $\Sigma$ ) and product ( $\Pi$ ) operators, which bind a variable over a set or range of values.

$\sum _{x\in S}f(x)\quad \quad \quad \prod _{x\in S}f(x)$

- The integral ( $\textstyle \int$ ) and limit ( $\lim$ ) operators, which bind a variable over a continuum or as it approaches a certain value.

$\int _{a}^{b}f(x)\,dx\quad \quad \lim _{x\to c}f(x)$

- The logical quantifiers, such as the universal quantifier ( $\forall$ ) and the existential quantifier ( $\exists$ ), which bind a variable over a domain of discourse.

$\forall x,P(x)\quad \quad \quad \exists x,P(x)$

In each case, the variable *x* is bound within the expression that follows the operator (e.g., $f(x)$ or $P(x)$ ). Many of these operators act on a function of the bound variable. While standard notation is often sufficient, complex expressions with nested operators can become ambiguous, particularly if the same variable name is reused. This can lead to a problem known as *variable capture*, where a variable intended to be free is incorrectly bound by an operator in a different scope.

To avoid such ambiguity, it can be useful to switch to a notation that makes the binding explicit, treating the operators as higher-order functions. This approach, rooted in the principles of lambda calculus, clearly separates the function being operated on from the operator itself.

For example:

- The summation $\sum _{k=1}^{10}f(k,n)$ can be written to make the functional argument explicit:

$\sum _{\{1,\ldots ,10\}}(k\mapsto f(k,n))$

Here, the operator $\sum _{S}f$ applies to the set *S* and the function *f*.

- The derivative operator can also be represented clearly as taking a function as its argument:

$D(x\mapsto x^{2}+2x+1)$

This notation clarifies that the operator D is applied to the entire function $x\mapsto x^{2}+2x+1$ , rather than just an expression in which x happens to be a variable.

## Formal explanation

Variable-binding mechanisms occur in different contexts in mathematics, logic and computer science. In all cases, however, they are purely syntactic properties of expressions and variables in them. For this section we can summarize syntax by identifying an expression with a tree whose leaf nodes are variables, constants, function constants or predicate constants and whose non-leaf nodes are logical operators. This expression can then be determined by doing an in-order traversal of the tree. Variable-binding operators are logical operators that occur in almost every formal language. A binding operator Q takes two arguments: a variable v and an expression P , and when applied to its arguments produces a new expression $Q(v,P)$ . The meaning of binding operators is supplied by the semantics of the language and does not concern us here.

Variable binding relates three things: a variable v , a location a for that variable in an expression and a non-leaf node n of the form $Q(v,P)$ . It worth noting that we define a location in an expression as a leaf node in the syntax tree. Variable binding occurs when that location is below the node n .

In the lambda calculus, `x` is a bound variable in the term `M = λx. T` and a free variable in the term `T`. We say `x` is bound in `M` and free in `T`. If `T` contains a subterm `λx. U` then `x` is rebound in this term. This nested, inner binding of `x` is said to "shadow" the outer binding. Occurrences of `x` in `U` are free occurrences of the new `x`.

Variables bound at the top level of a program are technically free variables within the terms to which they are bound but are often treated specially because they can be compiled as fixed addresses. Similarly, an identifier bound to a recursive function is also technically a free variable within its own body but is treated specially.

A *closed term* is one containing no free variables.

### Function definition and operators as binders

A clear example of a variable-binding operator from mathematics is function definition. An expression that defines a function, such as the right-hand side of:

$f=\left[(x_{1},\ldots ,x_{n})\mapsto t\right]\,,$

binds the variables $x_{1},\ldots ,x_{n}$ . The expression t , which forms the body of the function, may contain some, all, or none of the variables $x_{1},\ldots ,x_{n}$ , which are its formal parameters. Any occurrence of these variables within t is bound by the function definition. The body t may also contain other variables, which would be considered free variables whose values must be determined from a wider context.

The expression $\left[(x_{1},\ldots ,x_{n})\mapsto t\right]$ is directly analogous to lambda expressions in lambda calculus, where the $\lambda$ symbol is the fundamental variable-binding operator. For instance, the function definition $(x\mapsto x^{2})$ is equivalent to the lambda abstraction $\lambda x.x^{2}$ .

The same definition, binding the function being defined to the name f , is more commonly written in mathematical texts in the form

$f(x_{1},\ldots ,x_{n})=t\,.$

Other mathematical operators can be understood as higher-order functions that bind variables. For example, the summation operator, $\Sigma$ , can be analyzed as an operator that takes a function and a set to evaluate that function over. The expression:

$\sum _{x\in S}{x^{2}}$

binds the variable *x* within the term $x^{2}$ . The scope of the binding is the term that follows the summation symbol. This expression can be treated as a more compact notation for:

$\sum _{S}{(x\mapsto x^{2})}$

Here, $\sum _{S}{f}$ is an operator with two parameters: a one-parameter function f (in this case, $x\mapsto x^{2}$ ) and a set S to evaluate that function over.

Other operators can be expressed in a similar manner. The universal quantifier $\forall x\in S,P(x)$ can be understood as an operator that evaluates to the logical conjunction of the Boolean-valued function P applied to each element in the (possibly infinite) set S . Likewise, the product operator ( ${\textstyle \prod }$ ), the limit operator ( $\lim _{n\to \infty }$ ), and the integral operator ( $\int _{a}^{b}f(x)\,dx$ ) all function as variable binders, binding the variables n and x respectively over a specified domain.

## Natural language

When analyzed through the lens of formal semantics, natural languages exhibit a system of variable binding that is analogous to what is found in formal logic and computer science. This system governs how referring expressions, particularly pronouns, are interpreted within a sentence or discourse.

### Pronouns as free variables

In English, personal pronouns such as *he*, *she*, *they*, and their variants (e.g., *her*, *him*) can function as **free variables**. A free variable is a term whose referent is not determined within the immediate syntactic structure of the sentence and must be identified by the broader context, which can be either linguistic or situational (pragmatic).

Consider the following sentence:

> Lisa found her book.

The possessive pronoun *her* is a free variable. Its interpretation is flexible; it can refer to *Lisa*, an entity within the sentence, or to some other female individual salient in the context of the utterance. This ambiguity leads to two primary interpretations, which can be formally represented using co-indexing subscripts. An identical subscript indicates coreference, while different subscripts signal that the expressions refer to different entities.

1. **Lisa**i found **her**i book.
  - *(This interpretation signifies coreference, where "her" refers to Lisa. This is often called an anaphoric reading, where "her" is an anaphor and "Lisa" is its antecedent.)*
2. **Lisa**i found **her**j book.
  - *(In this interpretation, "her" refers to a female individual who is not Lisa, for instance, a person named Jane who was mentioned earlier in the conversation.)*

This distinction is not merely a theoretical exercise. Some languages have distinct pronominal forms to differentiate between these two readings. For example, Norwegian and Swedish use the reflexive possessive *sin* for the coreferential reading (*her*i) and a non-reflexive form like *hennes* (in Swedish) for the non-coreferential reading (*her*j).

While English does not have this explicit distinction in its standard pronouns, it can force a coreferential reading by using the emphatic possessive *own*.

- **Lisa**i found **her**i own book. (Coreference is required)
- ***Lisa**i found **her**j own book. (This interpretation is ungrammatical)

### Anaphors as bound variables

In contrast to personal pronouns, reflexive pronouns (e.g., *himself*, *herself*, *themselves*) and reciprocal pronouns (e.g., *each other*) act as **bound variables**, also known in linguistics as **anaphors**. A bound variable is an expression that must be co-indexed with, and c-commanded by, an antecedent within a specific syntactic domain.

Consider the sentence:

> Jane hurt herself.

The reflexive pronoun *herself* must refer to the subject of the clause, *Jane*. It cannot refer to any other individual. This obligatory coreference is a hallmark of a bound variable.

- **Jane**i hurt **herself**i. (Grammatical interpretation: *herself* = *Jane*)
- ***Jane**i hurt **herself**j. (Ungrammatical interpretation: *herself* ≠ *Jane*)

This binding relationship can be formally captured using a lambda expression, a tool from lambda calculus used in formal semantics to model function abstraction and application. The sentence can be represented as:

(λx.x hurt x)(Jane)

In this notation:

- `λx` is the lambda operator that binds the variable `x`.
- `x hurt x` is the predicate, a function that takes an argument and states that this argument hurt itself.
- `(Jane)` is the argument applied to the function.

The expression evaluates to "Jane hurt Jane," correctly capturing the fact that the subject and object of the verb are the same entity.

### Binding theory

The distinct behavior of pronouns and anaphors is systematically explained by the **binding theory**, a central component of Noam Chomsky's Government and Binding Theory. This theory proposes three principles that govern the interpretation of different types of noun phrases:

- **Principle A:** An anaphor (reflexive, reciprocal) must be bound in its governing category (roughly, the local clause). This explains why *herself* in "Jane hurt herself" must be bound by *Jane*.

- **Principle B:** A pronoun must be free in its governing category. This explains why a personal pronoun often cannot be bound by a local antecedent. For example, in "Ashley hit her," the pronoun *her* cannot refer to *Ashley*.
  - ***Ashley**i hit **her**i. (Ungrammatical due to Principle B)
  - **Ashley**i hit **her**j. (Grammatical; *her* refers to someone other than Ashley)

- **Principle C:** An R-expression (a referring expression like a proper name, e.g., *Jane*, or a definite description, e.g., *the woman*) must be free everywhere. This prevents an R-expression from being co-indexed with a c-commanding pronoun, as in ***He**i said that **John**i was tired*.

### Quantificational noun phrases

The concept of variable binding is essential for understanding quantificational noun phrases (QNPs), such as *every student*, *some politician*, or *no one*. Unlike proper names, these phrases do not refer to a specific entity. Instead, they express a quantity over a set of individuals. A QNP can bind a pronoun that falls within its scope, making the pronoun a bound variable.

> Every studenti thinks hei is smart.

In this sentence, the pronoun *he* is most naturally interpreted as a bound variable. Its reference co-varies with the individuals in the set denoted by "every student". The sentence does not mean that every student thinks a specific person (e.g., Peter) is smart; rather, it means that for each individual student x , x thinks that x is smart. In syntactic theories, this is often analyzed via a process of quantifier raising (QR), where the QNP moves at the abstract syntactic level of logical form to a position where it c-commands and binds the pronoun.

### Wh-questions and relative clauses

Variable binding is also central to the analysis of wh-movement, which occurs in the formation of questions and relative clauses. *Wh*-words like *who*, *what*, and *which* function as operators that bind a variable in the main clause.

- **Question:** Whoi does John like *t*i?
- **Relative Clause:** The man [whoi Mary saw *t*i] is my brother.

In these structures, the *wh*-word is said to move from an underlying position, leaving behind a "trace" $(t)$ , which is treated as a bound variable. The meaning of the question can be paraphrased as "For which person x , does John like x ?". Similarly, the relative clause denotes a set of individuals x such that "Mary saw x ".

### Sloppy versus strict identity in ellipsis

The distinction between free and bound variables provides a powerful explanation for certain ambiguities that arise under VP-ellipsis. Consider the following sentence:

> John loves his mother, and Bill does too.

This sentence has two distinct interpretations:

1. **Strict identity:** Bill loves *John's* mother.
2. **Sloppy identity:** Bill loves *Bill's* mother.

This ambiguity can be explained by the status of the pronoun *his* in the first clause.

- If *his* is treated as a **free variable** referring to John, the elided (or "missing") verb phrase is interpreted as "loves John's mother". When this is applied to Bill, the result is the **strict** reading.
- If *his* is treated as a **bound variable** bound by the subject of its clause (i.e., *John*), the verb phrase is interpreted as a lambda-abstracted property: `λx.x loves x's mother`. When this property is applied to Bill, the result is the **sloppy** reading.

The existence of the sloppy identity reading is considered strong evidence for the psychological reality of bound variable interpretations in the grammar of natural languages.

Thus, the distribution and interpretation of pronouns and other referring expressions in natural languages are not random but are governed by a sophisticated syntactic and semantic system.

The distinction between free and bound variables is a cornerstone of modern linguistic theory, providing the analytical tools necessary to account for coreference, quantification, question formation, and ellipsis.
