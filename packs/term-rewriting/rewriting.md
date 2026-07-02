---
title: "Rewriting"
source: https://en.wikipedia.org/wiki/Rewriting
domain: term-rewriting
license: CC-BY-SA-4.0
tags: term rewriting system, rewrite rule, abstract rewriting system, critical pair
fetched: 2026-07-02
---

# Rewriting

In mathematics, linguistics, computer science, and logic, **rewriting** covers a wide range of methods of replacing subterms of a formula with other terms. Such methods may be achieved by **rewriting systems** (also known as **rewrite systems**, **rewrite engines**, or **reduction systems**). In their most basic form, they consist of a set of objects, plus relations on how to transform those objects.

Rewriting can be non-deterministic. One rule to rewrite a term could be applied in many different ways to that term, or more than one rule could be applicable. Rewriting systems then do not provide an algorithm for changing one term to another, but a set of possible rule applications. When combined with an appropriate algorithm, however, rewrite systems can be viewed as computer programs, and several theorem provers and declarative programming languages are based on term rewriting.

## Example cases

### Logic

In logic, the procedure for obtaining the conjunctive normal form (CNF) of a formula can be implemented as a rewriting system. For example, the rules of such a system would be:

$\neg \neg A\to A$

(

double negation elimination

)

$\neg (A\land B)\to \neg A\lor \neg B$

(

De Morgan's laws

)

$\neg (A\lor B)\to \neg A\land \neg B$

$(A\land B)\lor C\to (A\lor C)\land (B\lor C)$

(

distributivity

)

$A\lor (B\land C)\to (A\lor B)\land (A\lor C),$

For each rule, each variable denotes a subexpression, and the symbol ( $\to$ ) indicates that an expression matching the left hand side of it can be rewritten to one matching the right hand side of it. In such a system, each rule is a logical equivalence, so performing a rewrite on an expression by these rules does not change the truth value of it. Other useful rewriting systems in logic may not preserve truth values, see e.g. equisatisfiability.

### Arithmetic

Term rewriting systems can be employed to compute arithmetic operations on natural numbers. To this end, each such number has to be encoded as a term. The simplest encoding is the one used in the Peano axioms, based on the constant 0 (zero) and the successor function *S*. For example, the numbers 0, 1, 2, and 3 are represented by the terms 0, S(0), S(S(0)), and S(S(S(0))), respectively. The following term rewriting system can then be used to compute sum and product of given natural numbers.

${\begin{aligned}A+0&\to A&{\textrm {(1)}},\\A+S(B)&\to S(A+B)&{\textrm {(2)}},\\A\cdot 0&\to 0&{\textrm {(3)}},\\A\cdot S(B)&\to A+(A\cdot B)&{\textrm {(4)}}.\end{aligned}}$

For example, the computation of 2+2 to result in 4 can be duplicated by term rewriting as follows:

$S(S(0))+S(S(0))$

$\;\;{\stackrel {(2)}{\to }}\;\;$

$S(\;S(S(0))+S(0)\;)$

$\;\;{\stackrel {(2)}{\to }}\;\;$

$S(S(\;S(S(0))+0\;))$

$\;\;{\stackrel {(1)}{\to }}\;\;$

$S(S(S(S(0)))),$

where the notation above each arrow indicates the rule used for each rewrite.

As another example, the computation of 2⋅2 looks like:

$S(S(0))\cdot S(S(0))$

$\;\;{\stackrel {(4)}{\to }}\;\;$

$S(S(0))+S(S(0))\cdot S(0)$

$\;\;{\stackrel {(4)}{\to }}\;\;$

$S(S(0))+S(S(0))+S(S(0))\cdot 0$

$\;\;{\stackrel {(3)}{\to }}\;\;$

$S(S(0))+S(S(0))+0$

$\;\;{\stackrel {(1)}{\to }}\;\;$

$S(S(0))+S(S(0))$

$\;\;{\stackrel {\textrm {s.a.}}{\to }}\;\;$

$S(S(S(S(0)))),$

where the last step comprises the previous example computation.

### Linguistics

In linguistics, phrase structure rules, also called **rewrite rules**, are used in some systems of generative grammar, as a means of generating the grammatically correct sentences of a language. Such a rule typically takes the form ${\rm {A\rightarrow X}}$ , where A is a syntactic category label, such as noun phrase or sentence, and X is a sequence of such labels or morphemes, expressing the fact that A can be replaced by X in generating the constituent structure of a sentence. For example, the rule ${\rm {S\rightarrow NP\ VP}}$ means that a sentence can consist of a noun phrase (NP) followed by a verb phrase (VP); further rules will specify what sub-constituents a noun phrase and a verb phrase can consist of, and so on.

## Abstract rewriting systems

From the above examples, it is clear that we can think of rewriting systems in an abstract manner. We need to specify a set of objects and the rules that can be applied to transform them. The most general (unidimensional) setting of this notion is called an *abstract reduction system* or *abstract rewriting system* (abbreviated *ARS*). An ARS is simply a set *A* of objects, together with a binary relation → on *A* called the *reduction relation*, *rewrite relation* or just *reduction*.

Many notions and notations can be defined in the general setting of an ARS. ${\overset {*}{\rightarrow }}$ is the reflexive transitive closure of $\rightarrow$ . $\leftrightarrow$ is the symmetric closure of $\rightarrow$ . ${\overset {*}{\leftrightarrow }}$ is the reflexive transitive symmetric closure of $\rightarrow$ . The word problem for an ARS is determining, given *x* and *y*, whether $x{\overset {*}{\leftrightarrow }}y$ . An object *x* in *A* is called *reducible* if there exists some other *y* in *A* such that $x\rightarrow y$ ; otherwise it is called *irreducible* or a normal form. An object *y* is called a "normal form of *x*" if $x{\stackrel {*}{\rightarrow }}y$ , and *y* is irreducible. If the normal form of *x* is unique, then this is usually denoted with $x{\downarrow }$ . If every object has at least one normal form, the ARS is called *normalizing*. $x\downarrow y$ or *x* and *y* are said to be *joinable* if there exists some *z* with the property that $x{\overset {*}{\rightarrow }}z{\overset {*}{\leftarrow }}y$ . An ARS is said to possess the Church–Rosser property if $x{\overset {*}{\leftrightarrow }}y$ implies $x\downarrow y$ . An ARS is confluent if for all *w*, *x*, and *y* in *A*, $x{\overset {*}{\leftarrow }}w{\overset {*}{\rightarrow }}y$ implies $x\downarrow y$ . An ARS is *locally confluent* if and only if for all *w*, *x*, and *y* in *A*, $x\leftarrow w\rightarrow y$ implies $x{\mathbin {\downarrow }}y$ . An ARS is said to be *terminating* or *noetherian* if there is no infinite chain $x_{0}\rightarrow x_{1}\rightarrow x_{2}\rightarrow \cdots$ . A confluent and terminating ARS is called *convergent* or *canonical*.

Important theorems for abstract rewriting systems are that an ARS is confluent iff it has the Church–Rosser property, Newman's lemma (a terminating ARS is confluent if and only if it is locally confluent), and that the word problem for an ARS is undecidable in general.

## String rewriting systems

A *string rewriting system* (SRS), also known as *semi-Thue system*, exploits the free monoid structure of the strings (words) over an alphabet to extend a rewriting relation, R , to *all* strings in the alphabet that contain left- and respectively right-hand sides of some rules as substrings. Formally a semi-Thue system is a tuple $(\Sigma ,R)$ where $\Sigma$ is a (usually finite) alphabet, and R is a binary relation between some (fixed) strings in the alphabet, called the set of *rewrite rules*. The *one-step rewriting relation* ${\underset {R}{\rightarrow }}$ induced by R on $\Sigma ^{*}$ is defined as: if $s,t\in \Sigma ^{*}$ are any strings, then $s{\underset {R}{\rightarrow }}t$ if there exist $x,y,u,v\in \Sigma ^{*}$ such that $s=xuy$ , $t=xvy$ , and $uRv$ . Since ${\underset {R}{\rightarrow }}$ is a relation on $\Sigma ^{*}$ , the pair $(\Sigma ^{*},{\underset {R}{\rightarrow }})$ fits the definition of an abstract rewriting system. Since the empty string is in $\Sigma ^{*}$ , R is a subset of ${\underset {R}{\rightarrow }}$ . If the relation R is symmetric, then the system is called a *Thue system*.

In a SRS, the reduction relation ${\overset {*}{\underset {R}{\rightarrow }}}$ is compatible with the monoid operation, meaning that $x{\overset {*}{\underset {R}{\rightarrow }}}y$ implies $uxv{\overset {*}{\underset {R}{\rightarrow }}}uyv$ for all strings $x,y,u,v\in \Sigma ^{*}$ . Similarly, the reflexive transitive symmetric closure of ${\underset {R}{\rightarrow }}$ , denoted ${\overset {*}{\underset {R}{\leftrightarrow }}}$ , is a congruence, meaning it is an equivalence relation (by definition) and it is also compatible with string concatenation. The relation ${\overset {*}{\underset {R}{\leftrightarrow }}}$ is called the *Thue congruence* generated by R . In a Thue system, i.e. if R is symmetric, the rewrite relation ${\overset {*}{\underset {R}{\rightarrow }}}$ coincides with the Thue congruence ${\overset {*}{\underset {R}{\leftrightarrow }}}$ .

The notion of a semi-Thue system essentially coincides with the presentation of a monoid. Since ${\overset {*}{\underset {R}{\leftrightarrow }}}$ is a congruence, we can define the factor monoid ${\mathcal {M}}_{R}=\Sigma ^{*}/{\overset {*}{\underset {R}{\leftrightarrow }}}$ of the free monoid $\Sigma ^{*}$ by the Thue congruence. If a monoid ${\mathcal {M}}$ is isomorphic with ${\mathcal {M}}_{R}$ , then the semi-Thue system $(\Sigma ,R)$ is called a monoid presentation of ${\mathcal {M}}$ .

We immediately get some very useful connections with other areas of algebra. For example, the alphabet $\{a,b\}$ with the rules $\{ab\rightarrow \varepsilon ,ba\rightarrow \varepsilon \}$ , where $\varepsilon$ is the empty string, is a presentation of the free group on one generator. If instead the rules are just $\{ab\rightarrow \varepsilon \}$ , then we obtain a presentation of the bicyclic monoid. Thus semi-Thue systems constitute a natural framework for solving the word problem for monoids and groups. In fact, every monoid has a presentation of the form $(\Sigma ,R)$ , i.e. it may always be presented by a semi-Thue system, possibly over an infinite alphabet.

The word problem for a semi-Thue system is undecidable in general; this result is sometimes known as the *Post–Markov theorem*.

## Term rewriting systems

A **term rewriting system** (**TRS**) is a rewriting system whose objects are *terms*, which are expressions with nested sub-expressions. For example, the system shown under *§ Logic* above is a term rewriting system. The terms in this system are composed of binary operators $(\vee )$ and $(\wedge )$ and the unary operator $(\neg )$ . Also present in the rules are variables, which represent any possible term (though a single variable always represents the same term throughout a single rule).

In contrast to string rewriting systems, whose objects are sequences of symbols, the objects of a term rewriting system form a term algebra. A term can be visualized as a tree of symbols, the set of admitted symbols being fixed by a given signature. As a formalism, term rewriting systems have the full power of Turing machines, that is, every computable function can be defined by a term rewriting system.

Some programming languages are based on term rewriting. One such example is Pure, a functional programming language for mathematical applications.

### Formal definition

A *rewrite rule* is a pair of terms, commonly written as $l\rightarrow r$ , to indicate that the left-hand side *l* can be replaced by the right-hand side *r*. A *term rewriting system* is a set *R* of such rules. A rule $l\rightarrow r$ can be *applied* to a term *s* if the left term l matches some subterm of *s*, that is, if there is some substitution $\sigma$ such that the subterm of s rooted at some position *p* is the result of applying the substitution $\sigma$ to the term l. The subterm matching the left hand side of the rule is called a **redex** or **reducible expression**. The result term *t* of this rule application is then the result of replacing the subterm at position *p* in *s* by the term r with the substitution $\sigma$ applied, see picture 1. In this case, s is said to be *rewritten in one step*, or *rewritten directly*, to t by the system R , formally denoted as $s\rightarrow _{R}t$ , $s{\underset {R}{\rightarrow }}t$ , or as $s{\overset {R}{\rightarrow }}t$ by some authors.

If a term $t_{1}$ can be rewritten in several steps into a term $t_{n}$ , that is, if $t_{1}{\underset {R}{\rightarrow }}t_{2}{\underset {R}{\rightarrow }}\cdots {\underset {R}{\rightarrow }}t_{n}$ , the term $t_{1}$ is said to be *rewritten* to $t_{n}$ , formally denoted as $t_{1}{\overset {+}{\underset {R}{\rightarrow }}}t_{n}$ . In other words, the relation ${\overset {+}{\underset {R}{\rightarrow }}}$ is the transitive closure of the relation ${\underset {R}{\rightarrow }}$ ; often, also the notation ${\overset {*}{\underset {R}{\rightarrow }}}$ is used to denote the reflexive-transitive closure of ${\underset {R}{\rightarrow }}$ , that is, $s{\overset {*}{\underset {R}{\rightarrow }}}t$ if $s=t$ or $s{\overset {+}{\underset {R}{\rightarrow }}}t$ . A term rewriting given by a set R of rules can be viewed as an abstract rewriting system as defined above, with terms as its objects and ${\underset {R}{\rightarrow }}$ as its rewrite relation.

For example, $x*(y*z)\rightarrow (x*y)*z$ is a rewrite rule, commonly used to establish a normal form with respect to the associativity of * . That rule can be applied at the numerator in the term ${\frac {a*((a+1)*(a+2))}{1*(2*3)}}$ with the matching substitution $\{x\mapsto a,\;y\mapsto a+1,\;z\mapsto a+2\}$ , see picture 2. Applying that substitution to the rule's right-hand side yields the term $(a*(a+1))*(a+2)$ , and replacing the numerator by that term yields ${\frac {(a*(a+1))*(a+2)}{1*(2*3)}}$ , which is the result term of applying the rewrite rule. Altogether, applying the rewrite rule has achieved what is called "applying the associativity law for * to ${\frac {a*((a+1)*(a+2))}{1*(2*3)}}$ " in elementary algebra. Alternately, the rule could have been applied to the denominator of the original term, yielding ${\frac {a*((a+1)*(a+2))}{(1*2)*3}}$ .

### Termination

Termination issues of rewrite systems in general are handled in *Abstract rewriting system#Termination and convergence*. For term rewriting systems in particular, the following additional subtleties are to be considered.

Termination even of a system consisting of one rule with a linear left-hand side is undecidable. Termination is also undecidable for systems using only unary function symbols; however, it is decidable for finite ground systems.

The following term rewrite system is normalizing, but not terminating, and not confluent: ${\begin{aligned}f(x,x)&\rightarrow g(x),\\f(x,g(x))&\rightarrow b,\\h(c,x)&\rightarrow f(h(x,c),h(x,x)).\\\end{aligned}}$

The following two examples of terminating term rewrite systems are due to Toyama:

$f(0,1,x)\rightarrow f(x,x,x)$

and

$g(x,y)\rightarrow x,$

$g(x,y)\rightarrow y.$

Their union is a non-terminating system, since

${\begin{aligned}&f(g(0,1),g(0,1),g(0,1))\\\rightarrow &f(0,g(0,1),g(0,1))\\\rightarrow &f(0,1,g(0,1))\\\rightarrow &f(g(0,1),g(0,1),g(0,1))\\\rightarrow &\cdots \end{aligned}}$ This result disproves a conjecture of Dershowitz, who claimed that the union of two terminating term rewrite systems $R_{1}$ and $R_{2}$ is again terminating if all left-hand sides of $R_{1}$ and right-hand sides of $R_{2}$ are linear, and there are no "*overlaps*" between left-hand sides of $R_{1}$ and right-hand sides of $R_{2}$ . All these properties are satisfied by Toyama's examples.

See Rewrite order and Path ordering (term rewriting) for ordering relations used in termination proofs for term rewriting systems.

### Higher-order rewriting systems

Higher-order rewriting systems are a generalization of first-order term rewriting systems to lambda terms, allowing higher order functions and bound variables. Various results about first-order TRSs can be reformulated for HRSs as well.

### Graph rewriting systems

Graph rewrite systems are another generalization of term rewrite systems, operating on graphs instead of (ground-) terms / their corresponding tree representation.

## Trace rewriting systems

Trace theory provides a means for discussing multiprocessing in more formal terms, such as via the trace monoid and the history monoid. Rewriting can be performed in trace systems as well.
