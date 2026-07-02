---
title: "Unification (computer science)"
source: https://en.wikipedia.org/wiki/Unification_(computer_science)
domain: prolog-lang
license: CC-BY-SA-4.0
tags: prolog language, prolog lang, swi-prolog, logic programming
fetched: 2026-07-02
---

# Unification (computer science)

In logic and computer science, specifically automated reasoning, **unification** is an algorithmic process of solving equations between symbolic expressions, each of the form *Left-hand side = Right-hand side*. For example, using *x*,*y*,*z* as variables, and taking *f* to be an uninterpreted function, the singleton equation set { *f*(1,*y*) = *f*(*x*,2) } is a syntactic first-order unification problem that has the substitution { *x* ↦ 1, *y* ↦ 2 } as its only solution.

Conventions differ on what values variables may assume and which expressions are considered equivalent. In first-order syntactic unification, variables range over first-order terms and equivalence is syntactic. This version of unification has a unique "best" answer and is used in logic programming and programming language type system implementation, especially in Hindley–Milner based type inference algorithms. In higher-order unification, possibly restricted to **higher-order pattern unification**, terms may include lambda expressions, and equivalence is up to beta-reduction. This version is used in proof assistants and higher-order logic programming, for example Isabelle, Twelf, and lambdaProlog. Finally, in semantic unification or E-unification, equality is subject to background knowledge and variables range over a variety of domains. This version is used in SMT solvers, term rewriting algorithms, and cryptographic protocol analysis.

## Formal definition

A *unification problem* is a finite set *E*={ *l*1 ≐ *r*1, ..., *l**n* ≐ *r**n* } of equations to solve, where *l**i*, *r**i* are in the set T of *terms* or *expressions*. Depending on which expressions or terms are allowed to occur in an equation set or unification problem, and which expressions are considered equal, several frameworks of unification are distinguished. If higher-order variables, that is, variables representing functions, are allowed in an expression, the process is called **higher-order unification**, otherwise *first-order unification*. If a solution is required to make both sides of each equation literally equal, the process is called **syntactic** or *free* **unification**, otherwise *semantic* or *equational unification*, or **E-unification**, or *unification modulo theory*.

If the right side of each equation is closed (no free variables), the problem is called (pattern) *matching*. The left side (with variables) of each equation is called the *pattern*.

### Prerequisites

Formally, a unification approach presupposes

- An infinite set V of *variables*. For higher-order unification, it is convenient to choose V disjoint from the set of lambda-term bound variables.
- A set T of *terms* such that $V\subseteq T$ . For first-order unification, T is usually the set of first-order terms (terms built from variable and function symbols). For higher-order unification T consists of first-order terms and lambda terms (terms containing some higher-order variables).
- A mapping ${\text{vars}}\colon T\rightarrow$ $\mathbb {P}$ $(V)$ , assigning to each term t the set ${\text{vars}}(t)\subsetneq V$ of *free variables* occurring in t .
- A theory or equivalence relation $\equiv$ on T , indicating which terms are considered equal. For first-order E-unification, $\equiv$ reflects the background knowledge about certain function symbols; for example, if $\oplus$ is considered commutative, $t\equiv u$ if u results from t by swapping the arguments of $\oplus$ at some (possibly all) occurrences. In the most typical case that there is no background knowledge at all, then only literally, or syntactically, identical terms are considered equal. In this case, ≡ is called the *free theory* (because it is a free object), the *empty theory* (because the set of equational sentences, or the background knowledge, is empty), the *theory of uninterpreted functions* (because unification is done on uninterpreted terms), or the *theory of constructors* (because all function symbols just build up data terms, rather than operating on them). For higher-order unification, usually $t\equiv u$ if t and u are alpha equivalent.

As an example of how the set of terms and theory affects the set of solutions, the syntactic first-order unification problem { *y* = *cons*(2,*y*) } has no solution over the set of finite terms. However, it has the single solution { *y* ↦ *cons*(2,*cons*(2,*cons*(2,...))) } over the set of infinite tree terms. Similarly, the semantic first-order unification problem { *a*⋅*x* = *x*⋅*a* } has each substitution of the form { *x* ↦ *a*⋅...⋅*a* } as a solution in a semigroup, i.e. if (⋅) is considered associative. But the same problem, viewed in an abelian group, where (⋅) is considered also commutative, has any substitution at all as a solution.

As an example of higher-order unification, the singleton set { *a* = *y*(*x*) } is a syntactic second-order unification problem, since *y* is a function variable. One solution is { *x* ↦ *a*, *y* ↦ (identity function) }; another one is { *y* ↦ (constant function mapping each value to *a*), *x* ↦ *(any value)* }.

### Substitution

A *substitution* is a mapping $\sigma :V\rightarrow T$ from variables to terms; the notation $\{x_{1}\mapsto t_{1},...,x_{k}\mapsto t_{k}\}$ refers to a substitution mapping each variable $x_{i}$ to the term $t_{i}$ , for $i=1,...,k$ , and every other variable to itself; the $x_{i}$ must be pairwise distinct. *Applying* that substitution to a term t is written in postfix notation as $t\{x_{1}\mapsto t_{1},...,x_{k}\mapsto t_{k}\}$ ; it means to (simultaneously) replace every occurrence of each variable $x_{i}$ in the term t by $t_{i}$ . The result $t\tau$ of applying a substitution $\tau$ to a term t is called an *instance* of that term t . As a first-order example, applying the substitution { *x* ↦ *h*(*a*,*y*), *z* ↦ *b* } to the term

|   | $f($ | ${\textbf {x}}$ | $,a,g($ | ${\textbf {z}}$ | $),y)$ |
|---|---|---|---|---|---|
| yields |   |   |   |   |   |
|   | $f($ | ${\textbf {h}}({\textbf {a}},{\textbf {y}})$ | $,a,g($ | ${\textbf {b}}$ | $),y).$ |

### Generalization, specialization

If a term t has an instance equivalent to a term u , that is, if $t\sigma \equiv u$ for some substitution $\sigma$ , then t is called *more general* than u , and u is called *more special* than, or *subsumed* by, t . For example, $x\oplus a$ is more general than $a\oplus b$ if ⊕ is commutative, since then $(x\oplus a)\{x\mapsto b\}=b\oplus a\equiv a\oplus b$ .

If ≡ is literal (syntactic) identity of terms, a term may be both more general and more special than another one only if both terms differ just in their variable names, not in their syntactic structure; such terms are called *variants*, or *renamings* of each other. For example, $f(x_{1},a,g(z_{1}),y_{1})$ is a variant of $f(x_{2},a,g(z_{2}),y_{2})$ , since $f(x_{1},a,g(z_{1}),y_{1})\{x_{1}\mapsto x_{2},y_{1}\mapsto y_{2},z_{1}\mapsto z_{2}\}=f(x_{2},a,g(z_{2}),y_{2})$ and $f(x_{2},a,g(z_{2}),y_{2})\{x_{2}\mapsto x_{1},y_{2}\mapsto y_{1},z_{2}\mapsto z_{1}\}=f(x_{1},a,g(z_{1}),y_{1}).$ However, $f(x_{1},a,g(z_{1}),y_{1})$ is *not* a variant of $f(x_{2},a,g(x_{2}),x_{2})$ , since no substitution can transform the latter term into the former one. The latter term is therefore properly more special than the former one.

For arbitrary $\equiv$ , a term may be both more general and more special than a structurally different term. For example, if ⊕ is idempotent, that is, if always $x\oplus x\equiv x$ , then the term $x\oplus y$ is more general than z , and vice versa, although $x\oplus y$ and z are of different structure.

A substitution $\sigma$ is *more special* than, or *subsumed* by, a substitution $\tau$ if $t\sigma$ is subsumed by $t\tau$ for each term t . We also say that $\tau$ is more general than $\sigma$ . More formally, take a nonempty infinite set V of auxiliary variables such that no equation $l_{i}\doteq r_{i}$ in the unification problem contains variables from V . Then a substitution $\sigma$ is subsumed by another substitution $\tau$ if there is a substitution $\theta$ such that for all terms $X\notin V$ , $X\sigma \equiv X\tau \theta$ . For instance $\{x\mapsto a,y\mapsto a\}$ is subsumed by $\tau =\{x\mapsto y\}$ , using $\theta =\{y\mapsto a\}$ , but $\sigma =\{x\mapsto a\}$ is not subsumed by $\tau =\{x\mapsto y\}$ , as $f(x,y)\sigma =f(a,y)$ is not an instance of $f(x,y)\tau =f(y,y)$ .

### Solution set

A substitution σ is a *solution* of the unification problem *E* if *l**i*σ ≡ *r**i*σ for $i=1,...,n$ . Such a substitution is also called a *unifier* of *E*. For example, if ⊕ is associative, the unification problem { *x* ⊕ *a* ≐ *a* ⊕ *x* } has the solutions {*x* ↦ *a*}, {*x* ↦ *a* ⊕ *a*}, {*x* ↦ *a* ⊕ *a* ⊕ *a*}, etc., while the problem { *x* ⊕ *a* ≐ *a* } has no solution.

For a given unification problem *E*, a set *S* of unifiers is called *complete* if each solution substitution is subsumed by some substitution in *S*. A complete substitution set always exists (e.g. the set of all solutions), but in some frameworks (such as unrestricted higher-order unification) the problem of determining whether any solution exists (i.e., whether the complete substitution set is nonempty) is undecidable.

The set *S* is called *minimal* if none of its members subsumes another one. Depending on the framework, a complete and minimal substitution set may have zero, one, finitely many, or infinitely many members, or may not exist at all due to an infinite chain of redundant members. Thus, in general, unification algorithms compute a finite approximation of the complete set, which may or may not be minimal, although most algorithms avoid redundant unifiers when possible. For first-order syntactical unification, Martelli and Montanari gave an algorithm that reports unsolvability or computes a single unifier that by itself forms a complete and minimal substitution set, called the **most general unifier**.

## Syntactic unification of first-order terms

*Syntactic unification of first-order terms* is the most widely used unification framework. It is based on *T* being the set of *first-order terms* (over some given set *V* of variables, *C* of constants and *F**n* of *n*-ary function symbols) and on ≡ being *syntactic equality*. In this framework, each solvable unification problem {*l*1 ≐ *r*1, ..., *l**n* ≐ *r**n*} has a complete, and obviously minimal, singleton solution set {*σ*}. Its member σ is called the **most general unifier** (*mgu*) of the problem. The terms on the left and the right hand side of each potential equation become syntactically equal when the mgu is applied i.e. *l*1*σ* = *r*1*σ* ∧ ... ∧ *l**n**σ* = *r**n**σ*. Any unifier of the problem is subsumed by the mgu σ. The mgu is unique up to variants: if *S*1 and *S*2 are both complete and minimal solution sets of the same syntactical unification problem, then *S*1 = { *σ*1 } and *S*2 = { *σ*2 } for some substitutions *σ*1 and *σ*2, and *xσ*1 is a variant of *xσ*2 for each variable *x* occurring in the problem.

For example, the unification problem { *x* ≐ *z*, *y* ≐ *f*(*x*) } has a unifier { *x* ↦ *z*, *y* ↦ *f*(*z*) }, because

| *x* | { *x* ↦ *z*, *y* ↦ *f*(*z*) } | = | *z* | = | *z* | { *x* ↦ *z*, *y* ↦ *f*(*z*) } | , and |
|---|---|---|---|---|---|---|---|
| *y* | { *x* ↦ *z*, *y* ↦ *f*(*z*) } | = | *f*(*z*) | = | *f*(*x*) | { *x* ↦ *z*, *y* ↦ *f*(*z*) } | . |

This is also the most general unifier. Other unifiers for the same problem are e.g. { *x* ↦ *f*(*x*1), *y* ↦ *f*(*f*(*x*1)), *z* ↦ *f*(*x*1) }, { *x* ↦ *f*(*f*(*x*1)), *y* ↦ *f*(*f*(*f*(*x*1))), *z* ↦ *f*(*f*(*x*1)) }, and so on; there are infinitely many similar unifiers.

As another example, the problem *g*(*x*,*x*) ≐ *f*(*y*) has no solution with respect to ≡ being literal identity, since any substitution applied to the left and right hand side will keep the outermost *g* and *f*, respectively, and terms with different outermost function symbols are syntactically different.

### Unification algorithms

Robinson's 1965 unification algorithm

> Symbols are ordered such that variables precede function symbols. Terms are ordered by increasing written length; equally long terms are ordered lexicographically. For a set *T* of terms, its disagreement path *p* is the lexicographically least path where two member terms of *T* differ. Its disagreement set is the set of subterms starting at *p*, formally: { *t*|*p* : *t* ∈ *T* }.
> 
> *Algorithm:*
> 
> ```
> Given a set T of terms to be unified
> Let σ initially be the identity substitution
> do forever
>     if Tσ is a singleton set then
>         return σ
>     fi
>     let D be the disagreement set of Tσ
>     let s, t be the two lexicographically least terms in D
>     if s is not a variable or s occurs in t then
>         return "NONUNIFIABLE"
>     fi
>      
>   
>     
>       
>         σ
>         :=
>         σ
>         {
>         s
>         ↦
>         t
>         }
>       
>     
>     {\displaystyle \sigma :=\sigma \{s\mapsto t\}}
>   
> 
> done
> ```

Jacques Herbrand discussed the basic concepts of unification and sketched an algorithm in 1930. But most authors attribute the first unification algorithm to John Alan Robinson (cf. box). Robinson's algorithm had worst-case exponential behavior in both time and space. Numerous authors have proposed more efficient unification algorithms. Algorithms with worst-case linear-time behavior were discovered independently by Martelli & Montanari (1976) and Paterson & Wegman (1976) Baader & Snyder (2001) uses a similar technique as Paterson-Wegman, hence is linear, but like most linear-time unification algorithms is slower than the Robinson version on small sized inputs due to the overhead of preprocessing the inputs and postprocessing of the output, such as construction of a DAG representation. de Champeaux (2022) is also of linear complexity in the input size but is competitive with the Robinson algorithm on small size inputs. The speedup is obtained by using an object-oriented representation of the predicate calculus that avoids the need for pre- and post-processing, instead making variable objects responsible for creating a substitution and for dealing with aliasing. de Champeaux claims that the ability to add functionality to predicate calculus represented as programmatic objects provides opportunities for optimizing other logic operations as well.

The following algorithm is commonly presented and originates from Martelli & Montanari (1982). Given a finite set $G=\{s_{1}\doteq t_{1},...,s_{n}\doteq t_{n}\}$ of potential equations, the algorithm applies rules to transform it to an equivalent set of equations of the form { *x*1 ≐ *u*1, ..., *x**m* ≐ *u**m* } where *x*1, ..., *x**m* are distinct variables and *u*1, ..., *u**m* are terms containing none of the *x**i*. A set of this form can be read as a substitution. If there is no solution the algorithm terminates with ⊥; other authors use "Ω", or "*fail*" in that case. The operation of substituting all occurrences of variable *x* in problem *G* with term *t* is denoted *G* {*x* ↦ *t*}. For simplicity, constant symbols are regarded as function symbols having zero arguments.

| $G\cup \{t\doteq t\}$ | $\Rightarrow$ | G |   |   | *delete* |
|---|---|---|---|---|---|
| $G\cup \{f(s_{0},...,s_{k})\doteq f(t_{0},...,t_{k})\}$ | $\Rightarrow$ | $G\cup \{s_{0}\doteq t_{0},...,s_{k}\doteq t_{k}\}$ |   |   | *decompose* |
| $G\cup \{f(s_{0},\ldots ,s_{k})\doteq g(t_{0},...,t_{m})\}$ | $\Rightarrow$ | $\bot$ | if $f\neq g$ or $k\neq m$ |   | *conflict* |
| $G\cup \{f(s_{0},...,s_{k})\doteq x\}$ | $\Rightarrow$ | $G\cup \{x\doteq f(s_{0},...,s_{k})\}$ |   |   | *swap* |
| $G\cup \{x\doteq t\}$ | $\Rightarrow$ | $G\{x\mapsto t\}\cup \{x\doteq t\}$ | if $x\not \in {\text{vars}}(t)$ and $x\in {\text{vars}}(G)$ |   | *eliminate* |
| $G\cup \{x\doteq f(s_{0},...,s_{k})\}$ | $\Rightarrow$ | $\bot$ | if $x\in {\text{vars}}(f(s_{0},...,s_{k}))$ |   | *check* |

#### Occurs check

An attempt to unify a variable *x* with a term containing *x* as a strict subterm *x* ≐ *f*(..., *x*, ...) would lead to an infinite term as solution for *x*, since *x* would occur as a subterm of itself. In the set of (finite) first-order terms as defined above, the equation *x* ≐ *f*(..., *x*, ...) has no solution; hence the *eliminate* rule may only be applied if *x* ∉ *vars*(*t*). Since that additional check, called *occurs check*, slows down the algorithm, it is omitted e.g. in most Prolog systems. From a theoretical point of view, omitting the check amounts to solving equations over infinite trees, see #Unification of infinite terms below.

#### Proof of termination

For the proof of termination of the algorithm consider a triple $\langle n_{var},n_{lhs},n_{eqn}\rangle$ where *n**var* is the number of variables that occur more than once in the equation set, *n**lhs* is the number of function symbols and constants on the left hand sides of potential equations, and *n**eqn* is the number of equations. When rule *eliminate* is applied, *n**var* decreases, since *x* is eliminated from *G* and kept only in { *x* ≐ *t* }. Applying any other rule can never increase *n**var* again. When rule *decompose*, *conflict*, or *swap* is applied, *n**lhs* decreases, since at least the left hand side's outermost *f* disappears. Applying any of the remaining rules *delete* or *check* can't increase *n**lhs*, but decreases *n**eqn*. Hence, any rule application decreases the triple $\langle n_{var},n_{lhs},n_{eqn}\rangle$ with respect to the lexicographical order, which is possible only a finite number of times.

Conor McBride observes that "by expressing the structure which unification exploits" in a dependently typed language such as Epigram, Robinson's unification algorithm can be made recursive on the number of variables, in which case a separate termination proof becomes unnecessary.

### Examples of syntactic unification of first-order terms

In the Prolog syntactical convention a symbol starting with an upper case letter is a variable name; a symbol that starts with a lowercase letter is a function symbol; the comma is used as the logical *and* operator. For mathematical notation, *x,y,z* are used as variables, *f,g* as function symbols, and *a,b* as constants.

| Prolog notation | Mathematical notation | Unifying substitution | Explanation |
|---|---|---|---|
| `a = a` | { *a* = *a* } | {} | Succeeds. (tautology) |
| `a = b` | { *a* = *b* } | ⊥ | *a* and *b* do not match |
| `X = X` | { *x* = *x* } | {} | Succeeds. (tautology) |
| `a = X` | { *a* = *x* } | { *x* ↦ *a* } | *x* is unified with the constant *a* |
| `X = Y` | { *x* = *y* } | { *x* ↦ *y* } | *x* and *y* are aliased |
| `f(a,X) = f(a,b)` | { *f*(*a*,*x*) = *f*(*a*,*b*) } | { *x* ↦ *b* } | function and constant symbols match, *x* is unified with the constant *b* |
| `f(a) = g(a)` | { *f*(*a*) = *g*(*a*) } | ⊥ | *f* and *g* do not match |
| `f(X) = f(Y)` | { *f*(*x*) = *f*(*y*) } | { *x* ↦ *y* } | *x* and *y* are aliased |
| `f(X) = g(Y)` | { *f*(*x*) = *g*(*y*) } | ⊥ | *f* and *g* do not match |
| `f(X) = f(Y,Z)` | { *f*(*x*) = *f*(*y*,*z*) } | ⊥ | Fails. The *f* function symbols have different arity |
| `f(g(X)) = f(Y)` | { *f*(*g*(*x*)) = *f*(*y*) } | { *y* ↦ *g*(*x*) } | Unifies *y* with the term ⁠ $g(x)$ ⁠ |
| `f(g(X),X) = f(Y,a)` | { *f*(*g*(*x*),*x*) = *f*(*y*,*a*) } | { *x* ↦ *a*, *y* ↦ *g*(*a*) } | Unifies *x* with constant *a*, and *y* with the term ⁠ $g(a)$ ⁠ |
| `X = f(X)` | { *x* = *f*(*x*) } | should be ⊥ | Returns ⊥ in first-order logic and many modern Prolog dialects (enforced by the *occurs check*). Succeeds in traditional Prolog and in Prolog II, unifying *x* with infinite term `x=f(f(f(f(...))))`. |
| `X = Y, Y = a` | { *x* = *y*, *y* = *a* } | { *x* ↦ *a*, *y* ↦ *a* } | Both *x* and *y* are unified with the constant *a* |
| `a = Y, X = Y` | { *a* = *y*, *x* = *y* } | { *x* ↦ *a*, *y* ↦ *a* } | As above (order of equations in set doesn't matter) |
| `X = a, b = X` | { *x* = *a*, *b* = *x* } | ⊥ | Fails. *a* and *b* do not match, so *x* can't be unified with both |

The most general unifier of a syntactic first-order unification problem of size n may have a size of 2*n*. For example, the problem ⁠ $(((a*z)*y)*x)*w\doteq w*(x*(y*(z*a)))$ ⁠ has the most general unifier ⁠ $\{z\mapsto a,y\mapsto a*a,x\mapsto (a*a)*(a*a),w\mapsto ((a*a)*(a*a))*((a*a)*(a*a))\}$ ⁠, cf. picture. In order to avoid exponential time complexity caused by such blow-up, advanced unification algorithms work on directed acyclic graphs (dags) rather than trees.

### Application: unification in logic programming

The concept of unification is one of the main ideas behind logic programming. Specifically, unification is a basic building block of resolution, a rule of inference for determining formula satisfiability. In Prolog, the equality symbol `=` implies first-order syntactic unification. It represents the mechanism of binding the contents of variables and can be viewed as a kind of one-time assignment.

In Prolog:

1. A variable can be unified with a constant, a term, or another variable, thus effectively becoming its alias. In many modern Prolog dialects and in first-order logic, a variable cannot be unified with a term that contains it; this is the so-called *occurs check*.
2. Two constants can be unified only if they are identical.
3. Similarly, a term can be unified with another term if the top function symbols and arities of the terms are identical and if the parameters can be unified simultaneously. Note that this is a recursive behavior.
4. Most operations, including `+`, `-`, `*`, `/`, are not evaluated by `=`. So for example `1+2 = 3` is not satisfiable because they are syntactically different. The use of integer arithmetic constraints `#=` introduces a form of E-unification for which these operations are interpreted and evaluated.

### Application: type inference

Type inference algorithms are typically based on unification, particularly Hindley-Milner type inference which is used by the functional languages Haskell and ML. For example, when attempting to infer the type of the Haskell expression `True : ['x']`, the compiler will use the type `a -> [a] -> [a]` of the list construction function `(:)`, the type `Bool` of the first argument `True`, and the type `[Char]` of the second argument `['x']`. The polymorphic type variable `a` will be unified with `Bool` and the second argument `[a]` will be unified with `[Char]`. `a` cannot be both `Bool` and `Char` at the same time, therefore this expression is not correctly typed.

Like for Prolog, an algorithm for type inference can be given:

1. Any type variable unifies with any type expression, and is instantiated to that expression. A specific theory might restrict this rule with an occurs check.
2. Two type constants unify only if they are the same type.
3. Two type constructions unify only if they are applications of the same type constructor and all of their component types recursively unify.

### Application: Feature Structure Unification

Unification has been used in different research areas of computational linguistics.

## Order-sorted unification

*Order-sorted logic* allows one to assign a *sort*, or *type*, to each term, and to declare a sort *s*1 a *subsort* of another sort *s*2, commonly written as *s*1 ⊆ *s*2. For example, when reаsoning about biological creatures, it is useful to declare a sort *dog* to be a subsort of a sort *animal*. Wherever a term of some sort *s* is required, a term of any subsort of *s* may be supplied instead. For example, assuming a function declaration *mother*: *animal* → *animal*, and a constant declaration *lassie*: *dog*, the term *mother*(*lassie*) is perfectly valid and has the sort *animal*. In order to supply the information that the mother of a dog is a dog in turn, another declaration *mother*: *dog* → *dog* may be issued; this is called *function overloading*, similar to overloading in programming languages.

Walther gave a unification algorithm for terms in order-sorted logic, requiring for any two declared sorts *s*1, *s*2 their intersection *s*1 ∩ *s*2 to be declared, too: if *x*1 and *x*2 is a variable of sort *s*1 and *s*2, respectively, the equation *x*1 ≐ *x*2 has the solution { *x*1 = *x*, *x*2 = *x* }, where *x*: *s*1 ∩ *s*2. After incorporating this algorithm into a clause-based automated theorem prover, he could solve a benchmark problem by translating it into order-sorted logic, thereby boiling it down an order of magnitude, as many unary predicates turned into sorts.

Smolka generalized order-sorted logic to allow for parametric polymorphism. In his framework, subsort declarations are propagated to complex type expressions. As a programming example, a parametric sort *list*(*X*) may be declared (with *X* being a type parameter as in a C++ template), and from a subsort declaration *int* ⊆ *float* the relation *list*(*int*) ⊆ *list*(*float*) is automatically inferred, meaning that each list of integers is also a list of floats.

Schmidt-Schauß generalized order-sorted logic to allow for term declarations. As an example, assuming subsort declarations *even* ⊆ *int* and *odd* ⊆ *int*, a term declaration like ∀ *i* : *int*. (*i* + *i*) : *even* allows to declare a property of integer addition that could not be expressed by ordinary overloading.

## Unification of infinite terms

Background on infinite trees:

- *B. Courcelle (1983). "Fundamental Properties of Infinite Trees". *Theoret. Comput. Sci*. **25** (2): 95–169. doi:10.1016/0304-3975(83)90059-2.*
- *Michael J. Maher (Jul 1988). "Complete Axiomatizations of the Algebras of Finite, Rational and Infinite Trees". *Proc. IEEE 3rd Annual Symp. on Logic in Computer Science, Edinburgh*. pp. 348–357.*
- *Joxan Jaffar; Peter J. Stuckey (1986). "Semantics of Infinite Tree Logic Programming". *Theoretical Computer Science*. **46**: 141–158. doi:10.1016/0304-3975(86)90027-7.*

Unification algorithm, Prolog II:

- *A. Colmerauer (1982). K.L. Clark; S.-A. Tarnlund (eds.). *Prolog and Infinite Trees*. Academic Press.*
- *Alain Colmerauer (1984). "Equations and Inequations on Finite and Infinite Trees". In ICOT (ed.). *Proc. Int. Conf. on Fifth Generation Computer Systems*. pp. 85–99.*

Applications:

- *Francis Giannesini; Jacques Cohen (1984). "Parser Generation and Grammar Manipulation using Prolog's Infinite Trees". *Journal of Logic Programming*. **1** (3): 253–265. doi:10.1016/0743-1066(84)90013-X.*

## E-unification

**E-unification** is the problem of finding solutions to a given set of equations, taking into account some equational background knowledge *E*. The latter is given as a set of universal equalities. For some particular sets *E*, equation solving algorithms (a.k.a. *E-unification algorithms*) have been devised; for others it has been proven that no such algorithms can exist.

For example, if a and b are distinct constants, the equation ⁠ $x*a\doteq y*b$ ⁠ has no solution with respect to purely syntactic unification, where nothing is known about the operator ⁠ * ⁠. However, if the ⁠ * ⁠ is known to be commutative, then the substitution {*x* ↦ *b*, *y* ↦ *a*} solves the above equation, since

|   | ⁠ $x*a$ ⁠ | {*x* ↦ *b*, *y* ↦ *a*} |   |
|---|---|---|---|
| = | ⁠ $b*a$ ⁠ |   | by substitution application |
| = | ⁠ $a*b$ ⁠ |   | by commutativity of ⁠ * ⁠ |
| = | ⁠ $y*b$ ⁠ | {*x* ↦ *b*, *y* ↦ *a*} | by (converse) substitution application |

The background knowledge *E* could state the commutativity of ⁠ * ⁠ by the universal equality "⁠ $u*v=v*u$ ⁠ for all *u*, *v*".

### Particular background knowledge sets E

| ∀ *u*,*v*,*w*: | ⁠ $u*(v*w)$ ⁠ | = | ⁠ $(u*v)*w$ ⁠ | **A** | Associativity of ⁠ * ⁠ |
|---|---|---|---|---|---|
| ∀ *u*,*v*: | ⁠ $u*v$ ⁠ | = | ⁠ $v*u$ ⁠ | **C** | Commutativity of ⁠ * ⁠ |
| ∀ *u*,*v*,*w*: | ⁠ $u*(v+w)$ ⁠ | = | ⁠ $u*v+u*w$ ⁠ | **Dl** | Left distributivity of ⁠ * ⁠ over ⁠ + ⁠ |
| ∀ *u*,*v*,*w*: | ⁠ $(v+w)*u$ ⁠ | = | ⁠ $v*u+w*u$ ⁠ | **Dr** | Right distributivity of ⁠ * ⁠ over ⁠ + ⁠ |
| ∀ *u*: | ⁠ $u*u$ ⁠ | = | u | **I** | Idempotence of ⁠ * ⁠ |
| ∀ *u*: | ⁠ $n*u$ ⁠ | = | u | **Nl** | Left neutral element n with respect to ⁠ * ⁠ |
| ∀ *u*: | ⁠ $u*n$ ⁠ | = | u | **Nr** | Right neutral element n with respect to ⁠ * ⁠ |

It is said that *unification is decidable* for a theory, if a unification algorithm has been devised for it that terminates for *any* input problem. It is said that *unification is semi-decidable* for a theory, if a unification algorithm has been devised for it that terminates for any *solvable* input problem, but may keep searching forever for solutions of an unsolvable input problem.

*Unification is decidable* for the following theories:

- **A**
- **A**,**C**
- **A**,**C**,**I**
- **A**,**C**,**Nl**
- **A**,**I**
- **A**,**Nl**,**Nr** (monoid)
- **C**
- Boolean rings
- Abelian groups, even if the signature is expanded by arbitrary additional symbols (but not axioms)
- K4 modal algebras

*Unification is semi-decidable* for the following theories:

- **A**,**Dl**,**Dr**
- **A**,**C**,**Dl**
- Commutative rings

### One-sided paramodulation

If there is a convergent term rewriting system *R* available for *E*, the *one-sided paramodulation* algorithm can be used to enumerate all solutions of given equations.

| *G* ∪ { *f*(*s*1,...,*s**n*) ≐ *f*(*t*1,...,*t**n*) } | ; *S* | ⇒ | *G* ∪ { *s*1 ≐ *t*1, ..., *s**n* ≐ *t**n* } | ; *S* |   | *decompose* |
|---|---|---|---|---|---|---|
| *G* ∪ { *x* ≐ *t* } | ; *S* | ⇒ | *G* { *x* ↦ *t* } | ; *S*{*x*↦*t*} ∪ {*x*↦*t*} | if the variable *x* doesn't occur in *t* | *eliminate* |
| *G* ∪ { *f*(*s*1,...,*s**n*) ≐ *t* } | ; *S* | ⇒ | *G* ∪ { *s*1 ≐ u1, ..., *s**n* ≐ u*n*, *r* ≐ *t* } | ; *S* | if *f*(*u*1,...,*u**n*) → *r* is a rule from *R* | *mutate* |
| *G* ∪ { *f*(*s*1,...,*s**n*) ≐ *y* } | ; *S* | ⇒ | *G* ∪ { *s*1 ≐ *y*1, ..., *s**n* ≐ *y**n*, *y* ≐ *f*(*y*1,...,*y**n*) } | ; *S* | if *y*1,...,*y**n* are new variables | *imitate* |

Starting with *G* being the unification problem to be solved and *S* being the identity substitution, rules are applied nondeterministically until the empty set appears as the actual *G*, in which case the actual *S* is a unifying substitution. Depending on the order the paramodulation rules are applied, on the choice of the actual equation from *G*, and on the choice of *R*'s rules in *mutate*, different computations paths are possible. Only some lead to a solution, while others end at a *G* ≠ {} where no further rule is applicable (e.g. *G* = { *f*(...) ≐ *g*(...) }).

| **1** | *app*(*nil*,*z*) | → *z* |
|---|---|---|
| **2** | *app*(*x*.*y*,*z*) | → *x*.*app*(*y*,*z*) |

For an example, a term rewrite system *R* is used defining the *append* operator of lists built from *cons* and *nil*; where *cons*(*x*,*y*) is written in infix notation as *x*.*y* for brevity; e.g. *app*(*a*.*b*.*nil*,*c*.*d*.*nil*) → *a*.*app*(*b*.*nil*,*c*.*d*.*nil*) → *a*.*b*.*app*(*nil*,*c*.*d*.*nil*) → *a*.*b*.*c*.*d*.*nil* demonstrates the concatenation of the lists *a*.*b*.*nil* and *c*.*d*.*nil*, employing the rewrite rule 2,2, and 1. The equational theory *E* corresponding to *R* is the congruence closure of *R*, both viewed as binary relations on terms. For example, *app*(*a*.*b*.*nil*,*c*.*d*.*nil*) ≡ *a*.*b*.*c*.*d*.*nil* ≡ *app*(*a*.*b*.*c*.*d*.*nil*,*nil*). The paramodulation algorithm enumerates solutions to equations with respect to that *E* when fed with the example *R*.

A successful example computation path for the unification problem { *app*(*x*,*app*(*y*,*x*)) ≐ *a*.*a*.*nil* } is shown below. To avoid variable name clashes, rewrite rules are consistently renamed each time before their use by rule *mutate*; *v*2, *v*3, ... are computer-generated variable names for this purpose. In each line, the chosen equation from *G* is highlighted in red. Each time the *mutate* rule is applied, the chosen rewrite rule (*1* or *2*) is indicated in parentheses. From the last line, the unifying substitution *S* = { *y* ↦ *nil*, *x* ↦ *a*.*nil* } can be obtained. In fact, *app*(*x*,*app*(*y*,*x*)) {*y*↦*nil*, *x*↦ *a*.*nil* } = *app*(*a*.*nil*,*app*(*nil*,*a*.*nil*)) ≡ *app*(*a*.*nil*,*a*.*nil*) ≡ *a*.*app*(*nil*,*a*.*nil*) ≡ *a*.*a*.*nil* solves the given problem. A second successful computation path, obtainable by choosing "mutate(1), mutate(2), mutate(2), mutate(1)" leads to the substitution *S* = { *y* ↦ *a*.*a*.*nil*, *x* ↦ *nil* }; it is not shown here. No other path leads to a success.

| Used rule |   | *G* | *S* |
|---|---|---|---|
|   |   | { *app*(*x*,*app*(*y*,*x*)) ≐ *a*.*a*.*nil* } | {} |
| mutate(2) | ⇒ | { *x* ≐ *v*2.*v*3, *app*(*y*,*x*) ≐ *v*4, *v*2.*app*(*v*3,*v*4) ≐ *a*.*a*.*nil* } | {} |
| decompose | ⇒ | { *x* ≐ *v*2.*v*3, *app*(*y*,*x*) ≐ *v*4, *v*2 ≐ *a*, *app*(*v*3,*v*4) ≐ *a*.*nil* } | {} |
| eliminate | ⇒ | { *app*(*y*,*v*2.*v*3) ≐ *v*4, *v*2 ≐ *a*, *app*(*v*3,*v*4) ≐ *a*.*nil* } | { *x* ↦ *v*2.*v*3 } |
| eliminate | ⇒ | { *app*(*y*,*a*.*v*3) ≐ *v*4, *app*(*v*3,*v*4) ≐ *a*.*nil* } | { *x* ↦ *a*.*v*3 } |
| mutate(1) | ⇒ | { *y* ≐ *nil*, *a*.*v*3 ≐ *v*5, *v*5 ≐ *v*4, *app*(*v*3,*v*4) ≐ *a*.*nil* } | { *x* ↦ *a*.*v*3 } |
| eliminate | ⇒ | { *y* ≐ *nil*, *a*.*v*3 ≐ *v*4, *app*(*v*3,*v*4) ≐ *a*.*nil* } | { *x* ↦ *a*.*v*3 } |
| eliminate | ⇒ | { *a*.*v*3 ≐ *v*4, *app*(*v*3,*v*4) ≐ *a*.*nil* } | { *y* ↦ *nil*, *x* ↦ *a*.*v*3 } |
| mutate(1) | ⇒ | { *a*.*v*3 ≐ *v*4, *v*3 ≐ *nil*, *v*4 ≐ *v*6, *v*6 ≐ *a*.*nil* } | { *y* ↦ *nil*, *x* ↦ *a*.*v*3 } |
| eliminate | ⇒ | { *a*.*v*3 ≐ *v*4, *v*3 ≐ *nil*, *v*4 ≐ *a*.*nil* } | { *y* ↦ *nil*, *x* ↦ *a*.*v*3 } |
| eliminate | ⇒ | { *a*.*nil* ≐ *v*4, *v*4 ≐ *a*.*nil* } | { *y* ↦ *nil*, *x* ↦ *a*.*nil* } |
| eliminate | ⇒ | { *a*.*nil* ≐ *a*.*nil* } | { *y* ↦ *nil*, *x* ↦ *a*.*nil* } |
| decompose | ⇒ | { *a* ≐ *a*, *nil* ≐ *nil* } | { *y* ↦ *nil*, *x* ↦ *a*.*nil* } |
| decompose | ⇒ | { *nil* ≐ *nil* } | { *y* ↦ *nil*, *x* ↦ *a*.*nil* } |
| decompose | ⇒ | {} | { *y* ↦ *nil*, *x* ↦ *a*.*nil* } |

### Narrowing

If *R* is a convergent term rewriting system for *E*, an approach alternative to the previous section consists in successive application of "**narrowing** steps"; this will eventually enumerate all solutions of a given equation. A narrowing step (cf. picture) consists in

- choosing a nonvariable subterm of the current term,
- syntactically unifying it with the left hand side of a rule from *R*, and
- replacing the instantiated rule's right hand side into the instantiated term.

Formally, if *l* → *r* is a renamed copy of a rewrite rule from *R*, having no variables in common with a term *s*, and the subterm *s*|*p* is not a variable and is unifiable with l via the mgu σ, then s can be *narrowed* to the term *t* = *sσ*[*rσ*]*p*, i.e. to the term sσ, with the subterm at *p* replaced by rσ. The situation that *s* can be narrowed to *t* is commonly denoted as *s* ↝ *t*. Intuitively, a sequence of narrowing steps *t*1 ↝ *t*2 ↝ ... ↝ *t**n* can be thought of as a sequence of rewrite steps *t*1 → *t*2 → ... → *t**n*, but with the initial term *t*1 being further and further instantiated, as necessary to make each of the used rules applicable.

The above example paramodulation computation corresponds to the following narrowing sequence ("↓" indicating instantiation here):

app

(

x

,

app

(

y

,

x

))

↓

↓

x

↦

v

2

.

v

3

app

(

v

2

.

v

3

,

app

(

y

,

v

2

.

v

3

))

→

v

2

.

app

(

v

3

,

app

(

y

,

v

2

.

v

3

))

↓

y

↦

nil

v

2

.

app

(

v

3

,

app

(

nil

,

v

2

.

v

3

))

→

v

2

.

app

(

v

3

,

v

2

.

v

3

)

↓

↓

v

3

↦

nil

v

2

.

app

(

nil

,

v

2

.

nil

)

→

v

2

.

v

2

.

nil

The last term, *v*2.*v*2.*nil* can be syntactically unified with the original right hand side term *a*.*a*.*nil*.

The *narrowing lemma* ensures that whenever an instance of a term *s* can be rewritten to a term *t* by a convergent term rewriting system, then *s* and *t* can be narrowed and rewritten to a term *s*′ and *t*′, respectively, such that *t*′ is an instance of *s*′.

Formally: whenever *sσ* →∗ *t* holds for some substitution σ, then there exist terms *s*′, *t*′ such that *s* ↝∗ *s*′ and *t* →∗ *t*′ and *s*′ *τ* = *t*′ for some substitution τ.

## Higher-order unification

Many applications require one to consider the unification of typed lambda-terms instead of first-order terms. Such unification is often called *higher-order unification*. Higher-order unification is undecidable, and such unification problems do not have most general unifiers. For example, the unification problem { *f*(*a*,*b*,*a*) ≐ *d*(*b*,*a*,*c*) }, where the only variable is *f*, has the solutions {*f* ↦ λ*x*.λ*y*.λ*z*. *d*(*y*,*x*,*c*) }, {*f* ↦ λ*x*.λ*y*.λ*z*. *d*(*y*,*z*,*c*) }, {*f* ↦ λ*x*.λ*y*.λ*z*. *d*(*y*,*a*,*c*) }, {*f* ↦ λ*x*.λ*y*.λ*z*. *d*(*b*,*x*,*c*) }, {*f* ↦ λ*x*.λ*y*.λ*z*. *d*(*b*,*z*,*c*) } and {*f* ↦ λ*x*.λ*y*.λ*z*. *d*(*b*,*a*,*c*) }. A well studied branch of higher-order unification is the problem of unifying simply typed lambda terms modulo the equality determined by αβη conversions. Gérard Huet gave a semi-decidable (pre-)unification algorithm that allows a systematic search of the space of unifiers (generalizing the unification algorithm of Martelli-Montanari with rules for terms containing higher-order variables) that seems to work sufficiently well in practice. Huet and Gilles Dowek have written articles surveying this topic.

Several subsets of higher-order unification are well-behaved, in that they are decidable and have a most-general unifier for solvable problems. One such subset is the previously described first-order terms. **Higher-order pattern unification**, due to Dale Miller, is another such subset. The higher-order logic programming languages λProlog and Twelf have switched from full higher-order unification to implementing only the pattern fragment; surprisingly pattern unification is sufficient for almost all programs, if each non-pattern unification problem is suspended until a subsequent substitution puts the unification into the pattern fragment. A superset of pattern unification called functions-as-constructors unification is also well-behaved. The Zipperposition theorem prover has an algorithm integrating these well-behaved subsets into a full higher-order unification algorithm.

In computational linguistics, one of the most influential theories of elliptical construction is that ellipses are represented by free variables whose values are then determined using Higher-Order Unification. For instance, the semantic representation of "Jon likes Mary and Peter does too" is like(*j*, *m*) ∧ R(*p*) and the value of R (the semantic representation of the ellipsis) is determined by the equation like(*j*, *m*) = R(*j*) . The process of solving such equations is called Higher-Order Unification.

Wayne Snyder gave a generalization of both higher-order unification and E-unification, i.e. an algorithm to unify lambda-terms modulo an equational theory.
