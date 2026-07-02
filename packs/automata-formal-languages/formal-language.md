---
title: "Formal language"
source: https://en.wikipedia.org/wiki/Formal_language
domain: automata-formal-languages
license: CC-BY-SA-4.0
tags: automata, automaton, finite state machine, formal language, context-free grammar, turing machine
fetched: 2026-07-02
---

# Formal language

In logic, mathematics, computer science, and linguistics, a **formal language** is a set of strings whose symbols are taken from a set called "alphabet".

The alphabet of a formal language consists of symbols that concatenate into strings (also called "words"). Words that belong to a particular formal language are sometimes called *well-formed words*. A formal language is often defined by means of a formal grammar such as a regular grammar or context-free grammar.

In computer science, formal languages are used, among others, as the basis for defining the grammars of programming languages and controlled natural languages (i.e., formalized versions of subsets of natural languages). In computational complexity theory, decision problems are typically defined as formal languages, and complexity classes are defined as the sets of the formal languages that can be parsed by machines with limited computational power. In logic and the foundations of mathematics, formal languages are used to represent the syntax of axiomatic systems, and mathematical formalism is the philosophy that all of mathematics can be reduced to the syntactic manipulation of formal languages in this way.

The field of **formal language theory** studies primarily the purely syntactic aspects of such languages—that is, their internal structural patterns. Formal language theory sprang out of linguistics, as a way of understanding the syntactic regularities of natural languages.

## History

In the 17th century, Gottfried Leibniz imagined and described the characteristica universalis, a universal and formal language which utilised pictographs. Later, Carl Friedrich Gauss investigated the problem of Gauss codes.

In the mid-19th century, George Boole established the field of boolean algebra, which is a formal way of describing logical operations using truth values and set operators. In his work *An Investigation of The Laws of Thought*, he demonstrated that logical reasoning can be expressed and manipulated through symbolic equations.

Gottlob Frege attempted to realize Leibniz's ideas, through a notational system, first outlined in *Begriffsschrift* (1879) and more fully developed in his 2-volume *Grundgesetze der Arithmetik* (1893/1903). This described a "formal language of pure language."

In the first half of the 20th century, several developments were made with relevance to formal languages. Axel Thue published four papers relating to words and language between 1906 and 1914. The last of these introduced what Emil Post later termed 'Thue Systems', and gave an early example of an undecidable problem. Post would later use this paper as the basis for a 1947 proof "that the word problem for semigroups was recursively insoluble", and later devised the canonical system for the creation of formal languages.

In 1907, Leonardo Torres Quevedo introduced a formal language for the description of mechanical drawings (mechanical devices), in Vienna. He published "Sobre un sistema de notaciones y símbolos destinados a facilitar la descripción de las máquinas" ("On a system of notations and symbols intended to facilitate the description of machines"). Heinz Zemanek rated it as an equivalent to a programming language for the numerical control of machine tools.

Noam Chomsky devised an abstract representation of formal and natural languages, known as the Chomsky hierarchy. In 1959 John Backus developed the Backus-Naur form to describe the syntax of a high level programming language, following his work in the creation of FORTRAN. Peter Naur was the secretary/editor for the ALGOL60 Report in which he used Backus–Naur form to describe the Formal part of ALGOL60.

## Words over an alphabet

An *alphabet*, in the context of formal languages, can be any set; its elements are called *letters*. An alphabet may contain an infinite number of elements; however, most definitions in formal language theory specify alphabets with a finite number of elements, and many results apply only to them. It often makes sense to use an alphabet in the usual sense of the word, or more generally any finite character encoding such as ASCII or Unicode.

A **word** over an alphabet can be any finite sequence (i.e., string) of letters. The set of all words over an alphabet Σ is usually denoted by Σ* (using the Kleene star). The length of a word is the number of letters it is composed of. For any alphabet, there is only one word of length 0, the *empty word*, which is often denoted by e, ε, λ or even Λ. By concatenation one can combine two words to form a new word, whose length is the sum of the lengths of the original words. The result of concatenating a word with the empty word is the original word.

In some applications, especially in logic, the alphabet is also known as the *vocabulary* and words are known as *formulas* or *sentences*; this breaks the letter/word metaphor and replaces it by a word/sentence metaphor.

## Definition

Given a non-empty set $\Sigma$ , a **formal language L over $\Sigma$** is a subset of $\Sigma ^{*}$ , where $\Sigma ^{*}$ is the set of all possible finite-length words over $\Sigma$ . We call the set $\Sigma$ **the alphabet of L**. On the other hand, given a formal language L over $\Sigma$ , a word $w\in \Sigma ^{*}$ is *well-formed* if $w\in L$ . Similarly, an expression $E\subseteq \Sigma ^{*}$ is *well-formed* if $E\subseteq L$ . Sometimes, a formal language L over $\Sigma$ has a set of clear rules and constraints for the creation of all possible well-formed words from $\Sigma ^{*}$ .

In computer science and mathematics, which do not usually deal with natural languages, the adjective "formal" is often omitted as redundant. On the other hand, we can just say "a formal language L " when its alphabet $\Sigma$ is clear in the context.

While formal language theory usually concerns itself with formal languages that are described by some syntactic rules, the actual definition of the concept "formal language" is only as above: a (possibly infinite) set of finite-length strings composed from a given alphabet, no more and no less. In practice, there are many languages that can be described by rules, such as regular languages or context-free languages. The notion of a formal grammar may be closer to the intuitive concept of a "language", one described by syntactic rules. By an abuse of the definition, a particular formal language is often thought of as being accompanied with a formal grammar that describes it.

## Examples

The following rules describe a formal language L over the alphabet Σ = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, +, =}:

- Every nonempty string that does not contain "+" or "=" and does not start with "0" is in L.
- The string "0" is in L.
- A string containing "=" is in L if and only if there is exactly one "=", and it separates two valid strings of L.
- A string containing "+" but not "=" is in L if and only if every "+" in the string separates two valid strings of L.
- No string is in L other than those implied by the previous rules.

Under these rules, the string "23+4=555" is in L, but the string "=234=+" is not. This formal language expresses natural numbers, well-formed additions, and well-formed addition equalities, but it expresses only what they look like (their syntax), not what they mean (semantics). For instance, nowhere in these rules is there any indication that "0" means the number zero, "+" means addition, "23+4=555" is false, etc.

### Constructions

For finite languages, one can explicitly enumerate all well-formed words. For example, we can describe a language L as just L = {a, b, ab, cba}. The degenerate case of this construction is the **empty language**, which contains no words at all (L = ∅).

However, even over a finite (non-empty) alphabet such as Σ = {a, b} there are an infinite number of finite-length words that can potentially be expressed: "a", "abb", "ababba", "aaababbbbaab", .... Therefore, formal languages are typically infinite, and describing an infinite formal language is not as simple as writing *L* = {a, b, ab, cba}. Here are some examples of formal languages:

- L = Σ*, the set of *all* words over Σ;
- L = {a}* = {a*n*}, where *n* ranges over the natural numbers and "a*n*" means "a" repeated *n* times (this is the set of words consisting only of the symbol "a");
- the set of syntactically correct programs in a given programming language (the syntax of which is usually defined by a context-free grammar);
- the set of inputs upon which a certain Turing machine halts; or
- the set of maximal strings of alphanumeric ASCII characters on this line, i.e., the set {the, set, of, maximal, strings, alphanumeric, ASCII, characters, on, this, line, i, e}.

## Language-specification formalisms

Formal languages are used as tools in multiple disciplines. However, formal language theory rarely concerns itself with particular languages (except as examples), but is mainly concerned with the study of various types of formalisms to describe languages. For instance, a language can be given as

- those strings generated by some formal grammar;
- those strings described or matched by a particular regular expression;
- those strings accepted by some automaton, such as a Turing machine or finite-state automaton;
- those strings for which some decision procedure (an algorithm that asks a sequence of related YES/NO questions) produces the answer YES.

Typical questions asked about such formalisms include:

- What is their expressive power? (Can formalism *X* describe every language that formalism *Y* can describe? Can it describe other languages?)
- What is their recognizability? (How difficult is it to decide whether a given word belongs to a language described by formalism *X*?)
- What is their comparability? (How difficult is it to decide whether two languages, one described in formalism *X* and one in formalism *Y*, or in *X* again, are actually the same language?).

Surprisingly often, the answer to these decision problems is "it cannot be done at all", or "it is extremely expensive" (with a characterization of how expensive). Therefore, formal language theory is a major application area of computability theory and complexity theory. Formal languages may be classified in the Chomsky hierarchy based on the expressive power of their generative grammar as well as the complexity of their recognizing automaton. Context-free grammars and regular grammars provide a good compromise between expressivity and ease of parsing, and are widely used in practical applications.

## Operations on languages

Certain operations on languages are common. This includes the standard set operations, such as union, intersection, and complement. Another class of operation is the element-wise application of string operations.

Examples: suppose $L_{1}$ and $L_{2}$ are languages over some common alphabet $\Sigma$ .

- The *concatenation* $L_{1}\cdot L_{2}$ consists of all strings of the form $vw$ where v is a string from $L_{1}$ and w is a string from $L_{2}$ .
- The *intersection* $L_{1}\cap L_{2}$ of $L_{1}$ and $L_{2}$ consists of all strings that are contained in both languages
- The *complement* $\neg L_{1}$ of $L_{1}$ with respect to $\Sigma$ consists of all strings over $\Sigma$ that are not in $L_{1}$ .
- The Kleene star: the language consisting of all words that are concatenations of zero or more words in the original language;
- *Reversal*:
  - Let *ε* be the empty word, then $\varepsilon ^{R}=\varepsilon$ , and
  - for each non-empty word $w=\sigma _{1}\cdots \sigma _{n}$ (where $\sigma _{1},\ldots ,\sigma _{n}$ are elements of some alphabet), let $w^{R}=\sigma _{n}\cdots \sigma _{1}$ ,
  - then for a formal language L , $L^{R}=\{w^{R}\mid w\in L\}$ .
- String homomorphism

Such string operations are used to investigate closure properties of classes of languages. A class of languages is closed under a particular operation when the operation, applied to languages in the class, always produces a language in the same class again. For instance, the context-free languages are known to be closed under union, concatenation, and intersection with regular languages, but not closed under intersection or complement. The theory of trios and abstract families of languages studies the most common closure properties of language families in their own right.

Closure properties of language families (

$L_{1}$

Op

$L_{2}$

where both

$L_{1}$

and

$L_{2}$

are in the language family given by the column). After Hopcroft and Ullman.

Operation

Regular

DCFL

CFL

IND

CSL

Recursive

RE

Union

$L_{1}\cup L_{2}=\{w\mid w\in L_{1}\lor w\in L_{2}\}$

Yes

No

Yes

Yes

Yes

Yes

Yes

Intersection

$L_{1}\cap L_{2}=\{w\mid w\in L_{1}\land w\in L_{2}\}$

Yes

No

No

No

Yes

Yes

Yes

Complement

$\neg L_{1}=\{w\mid w\not \in L_{1}\}$

Yes

Yes

No

No

Yes

Yes

No

Concatenation

$L_{1}\cdot L_{2}=\{wz\mid w\in L_{1}\land z\in L_{2}\}$

Yes

No

Yes

Yes

Yes

Yes

Yes

Kleene star

$L_{1}^{*}=\{\varepsilon \}\cup \{wz\mid w\in L_{1}\land z\in L_{1}^{*}\}$

Yes

No

Yes

Yes

Yes

Yes

Yes

(String) homomorphism

h

$h(L_{1})=\{h(w)\mid w\in L_{1}\}$

Yes

No

Yes

Yes

No

No

Yes

ε-free (string) homomorphism

h

$h(L_{1})=\{h(w)\mid w\in L_{1}\}$

Yes

No

Yes

Yes

Yes

Yes

Yes

Substitution

$\varphi$

$\varphi (L_{1})=\bigcup _{\sigma _{1}\cdots \sigma _{n}\in L_{1}}\varphi (\sigma _{1})\cdot \ldots \cdot \varphi (\sigma _{n})$

Yes

No

Yes

Yes

Yes

No

Yes

Inverse homomorphism

$h^{-1}$

$h^{-1}(L_{1})=\bigcup _{w\in L_{1}}h^{-1}(w)$

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Reverse

$L^{R}=\{w^{R}\mid w\in L\}$

Yes

No

Yes

Yes

Yes

Yes

Yes

Intersection with a

regular language

R

$L\cap R=\{w\mid w\in L\land w\in R\}$

Yes

Yes

Yes

Yes

Yes

Yes

Yes

## Applications

### Programming languages

A compiler usually has two distinct components. A lexical analyzer, sometimes generated by a tool like `lex`, identifies the tokens of the programming language grammar, e.g. identifiers or keywords, numeric and string literals, punctuation and operator symbols, which are themselves specified by a simpler formal language, usually by means of regular expressions. At the most basic conceptual level, a parser, sometimes generated by a parser generator like `yacc`, attempts to decide if the source program is syntactically valid, that is if it is well formed with respect to the programming language grammar for which the compiler was built.

Of course, compilers do more than just parse the source code – they usually translate it into some executable format. Because of this, a parser usually outputs more than a yes/no answer, typically an abstract syntax tree. This is used by subsequent stages of the compiler to eventually generate an executable containing machine code that runs directly on the hardware, or some intermediate code that requires a virtual machine to execute.

### Formal theories, systems, and proofs

In mathematical logic, a *formal theory* is a set of sentences expressed in a formal language.

A *formal system* (also called a *logical calculus*, or a *logical system*) consists of a formal language together with a deductive apparatus (also called a *deductive system*). The deductive apparatus may consist of a set of transformation rules, which may be interpreted as valid rules of inference, or a set of axioms, or have both. A formal system is used to derive one expression from one or more other expressions. Although a formal language can be identified with its formulas, a formal system cannot be likewise identified by its theorems. Two formal systems ${\mathcal {FS}}$ and ${\mathcal {FS'}}$ may have all the same theorems and yet differ in some significant proof-theoretic way (a formula A may be a syntactic consequence of a formula B in one but not another for instance).

A *formal proof* or *derivation* is a finite sequence of well-formed formulas (which may be interpreted as sentences, or propositions) each of which is an axiom or follows from the preceding formulas in the sequence by a rule of inference. The last sentence in the sequence is a theorem of a formal system. Formal proofs are useful because their theorems can be interpreted as true propositions.

#### Interpretations and models

Formal languages are entirely syntactic in nature, but may be given semantics that give meaning to the elements of the language. For instance, in mathematical logic, the set of possible formulas of a particular logic is a formal language, and an interpretation assigns a meaning to each of the formulas—usually, a truth value.

The study of interpretations of formal languages is called formal semantics. In mathematical logic, this is often done in terms of model theory. In model theory, the terms that occur in a formula are interpreted as objects within mathematical structures, and fixed compositional interpretation rules determine how the truth value of the formula can be derived from the interpretation of its terms; a *model* for a formula is an interpretation of terms such that the formula becomes true.
