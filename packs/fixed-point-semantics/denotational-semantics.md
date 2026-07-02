---
title: "Denotational semantics"
source: https://en.wikipedia.org/wiki/Denotational_semantics#Meanings_of_recursive_programs
domain: fixed-point-semantics
license: CC-BY-SA-4.0
tags: least fixed point, Kleene fixed-point theorem, Knaster-Tarski theorem, fixed-point combinator
fetched: 2026-07-02
---

# Denotational semantics

In computer science, **denotational semantics** (initially known as **mathematical semantics** or **Scott–Strachey semantics**) is an approach of formalizing the meanings of programming languages by constructing mathematical objects (called *denotations*) that describe the meanings of expressions from the languages. Other approaches providing formal semantics of programming languages include axiomatic semantics and operational semantics.

Broadly speaking, denotational semantics is concerned with finding mathematical objects called domains that represent what programs do. For example, programs (or program phrases) might be represented by partial functions or by games between the environment and the system.

An important tenet of denotational semantics is that *semantics should be compositional*: the denotation of a program phrase should be built out of the denotations of its subphrases.

## Historical development

Denotational semantics originated in the work of Christopher Strachey and Dana Scott published in the early 1970s. As originally developed by Strachey and Scott, denotational semantics provided the meaning of a computer program as a function that mapped input into output. To give meanings to recursively defined programs, Scott proposed working with continuous functions between domains, specifically complete partial orders. As described below, work has continued in investigating appropriate denotational semantics for aspects of programming languages such as sequentiality, concurrency, non-determinism and local state.

Denotational semantics has been developed for modern programming languages that use capabilities like concurrency and exceptions, e.g., Concurrent ML, CSP, and Haskell. The semantics of these languages is compositional in that the meaning of a phrase depends on the meanings of its subphrases. For example, the meaning of the applicative expression `f(E1,E2)` is defined in terms of semantics of its subphrases f, E1 and E2. In a modern programming language, E1 and E2 can be evaluated concurrently and the execution of one of them might affect the other by interacting through shared objects causing their meanings to be defined in terms of each other. Also, E1 or E2 might throw an exception which could terminate the execution of the other one. The sections below describe special cases of the semantics of these modern programming languages.

### Meanings of recursive programs

Denotational semantics is ascribed to a program phrase as a function from an environment (holding current values of its free variables) to its denotation. For example, the phrase `n*m` produces a denotation when provided with an environment that has binding for its two free variables: `n` and `m`. If in the environment `n` has the value 3 and `m` has the value 5, then the denotation is 15.

A function can be represented as a set of ordered pairs of argument and corresponding result values. For example, the set {(0,1), (4,3)} denotes a function with result 1 for argument 0, result 3 for the argument 4, and undefined otherwise.

Consider for example the factorial function, which might be defined recursively as:

```mw
int factorial(int n)
{
  if (n == 0)
    return 1;
  else
    return n * factorial(n - 1);
}
```

To provide a meaning for this recursive definition, the denotation is built up as the limit of approximations, where each approximation limits the number of calls to factorial. At the beginning, we start with no calls - hence nothing is defined. In the next approximation, we can add the ordered pair (0,1), because this doesn't require calling factorial again. Similarly we can add (1,1), (2,2), etc., adding one pair each successive approximation because computing *factorial(n)* requires *n+1* calls. In the limit we get a total function from $\mathbb {N}$ to $\mathbb {N}$ defined everywhere in its domain.

Formally we model each approximation as a partial function $\mathbb {N} \rightharpoonup \mathbb {N}$ . Our approximation is then repeatedly applying a function implementing "make a more defined partial factorial function", i.e. $F:(\mathbb {N} \rightharpoonup \mathbb {N} )\to (\mathbb {N} \rightharpoonup \mathbb {N} )$ , starting with the empty function (empty set). *F* could be defined in code as follows (using `Map<int,int>` for $\mathbb {N} \rightharpoonup \mathbb {N}$ ):

```mw
int factorial_nonrecursive(Map<int,int> factorial_less_defined, int n)
{
  if (n == 0) then return 1;
  else if (fprev = lookup(factorial_less_defined, n-1)) then
    return n * fprev;
  else
    return NOT_DEFINED;
}

Map<int,int> F(Map<int,int> factorial_less_defined)
{ 
  Map<int,int> new_factorial = Map.empty();
  for (int n in all<int>()) {
    if (f = factorial_nonrecursive(factorial_less_defined, n) != NOT_DEFINED)
      new_factorial.put(n, f);
  }
  return new_factorial;
}
```

Then we can introduce the notation *Fn* to indicate *F* applied *n* times.

- *F*0({}) is the totally undefined partial function, represented as the set {};
- *F*1({}) is the partial function represented as the set {(0,1)}: it is defined at 0, to be 1, and undefined elsewhere;
- *F*5({}) is the partial function represented as the set {(0,1), (1,1), (2,2), (3,6), (4,24)}: it is defined for arguments 0,1,2,3,4.

This iterative process builds a sequence of partial functions from $\mathbb {N}$ to $\mathbb {N}$ . Partial functions form a chain-complete partial order using ⊆ as the ordering. Furthermore, this iterative process of better approximations of the factorial function forms an expansive (also called progressive) mapping because each $F^{i}\leq F^{i+1}$ using ⊆ as the ordering. So by a fixed-point theorem (specifically Bourbaki–Witt theorem), there exists a fixed point for this iterative process.

In this case, the fixed point is the least upper bound of this chain, which is the full `factorial` function, which can be expressed as the union

$\bigcup _{i\in \mathbb {N} }F^{i}(\{\}).$

The fixed point we found is the least fixed point of *F*, because our iteration started with the smallest element in the domain (the empty set). To prove this we need a more complex fixed point theorem such as the Knaster–Tarski theorem.

### Denotational semantics of non-deterministic programs

The concept of power domains has been developed to give a denotational semantics to non-deterministic sequential programs. Writing *P* for a power-domain constructor, the domain *P*(*D*) is the domain of non-deterministic computations of type denoted by *D*.

There are difficulties with fairness and unboundedness in domain-theoretic models of non-determinism.

### Denotational semantics of concurrency

Many researchers have argued that the domain-theoretic models given above do not suffice for the more general case of concurrent computation. For this reason various new models have been introduced. In the early 1980s, people began using the style of denotational semantics to give semantics for concurrent languages. Examples include Will Clinger's work with the actor model; Glynn Winskel's work with event structures and Petri nets; and the work by Francez, Hoare, Lehmann, and de Roever (1979) on trace semantics for CSP. All these lines of inquiry remain under investigation (see e.g. the various denotational models for CSP).

Recently, Winskel and others have proposed the category of profunctors as a domain theory for concurrency.

### Denotational semantics of state

State (such as a heap) and simple imperative features can be straightforwardly modeled in the denotational semantics described above. The key idea is to consider a command as a partial function on some domain of states. The meaning of "`x:=3`" is then the function that takes a state to the state with `3` assigned to `x`. The sequencing operator "`;`" is denoted by composition of functions. Fixed-point constructions are then used to give a semantics to looping constructs, such as "`while`".

Things become more difficult in modelling programs with local variables. One approach is to no longer work with domains, but instead to interpret types as functors from some category of worlds to a category of domains. Programs are then denoted by natural continuous functions between these functors.

### Denotations of data types

Many programming languages allow users to define recursive data types. For example, the type of lists of numbers can be specified by

```mw
datatype list = Cons of nat * list | Empty
```

This section deals only with functional data structures that cannot change. Conventional imperative programming languages would typically allow the elements of such a recursive list to be changed.

For another example: the type of denotations of the untyped lambda calculus is

```mw
datatype D = D of (D → D)
```

The problem of *solving domain equations* is concerned with finding domains that model these kinds of datatypes. One approach, roughly speaking, is to consider the collection of all domains as a domain itself, and then solve the recursive definition there.

Polymorphic data types are data types that are defined with a parameter. For example, the type of α `list`s is defined by

```mw
datatype α list = Cons of α * α list | Empty
```

Lists of natural numbers, then, are of type `nat list`, while lists of strings are of `string list`.

Some researchers have developed domain theoretic models of polymorphism. Other researchers have also modeled parametric polymorphism within constructive set theories.

A recent research area has involved denotational semantics for object and class based programming languages.

### Denotational semantics for programs of restricted complexity

Following the development of programming languages based on linear logic, denotational semantics have been given to languages for linear usage (see e.g. proof nets, coherence spaces) and also polynomial time complexity.

### Denotational semantics of sequentiality

The problem of full abstraction for the sequential programming language PCF was, for a long time, a big open question in denotational semantics. The difficulty with PCF is that it is a very sequential language. For example, there is no way to define the parallel-or function in PCF. It is for this reason that the approach using domains, as introduced above, yields a denotational semantics that is not fully abstract.

This open question was mostly resolved in the 1990s with the development of game semantics and also with techniques involving logical relations. For more details, see the page on PCF.

### Denotational semantics as source-to-source translation

It is often useful to translate one programming language into another. For example, a concurrent programming language might be translated into a process calculus; a high-level programming language might be translated into byte-code. (Indeed, conventional denotational semantics can be seen as the interpretation of programming languages into the internal language of the category of domains.)

In this context, notions from denotational semantics, such as full abstraction, help to satisfy security concerns.

## Abstraction

It is often considered important to connect denotational semantics with operational semantics. This is especially important when the denotational semantics is rather mathematical and abstract, and the operational semantics is more concrete or closer to the computational intuitions. The following properties of a denotational semantics are often of interest.

1. **Syntax independence**: The denotations of programs should not involve the syntax of the source language.
2. **Adequacy (or soundness)**: All observably distinct programs have distinct denotations;
3. **Full abstraction**: All observationally equivalent programs have equal denotations.

For semantics in the traditional style, adequacy and full abstraction may be understood roughly as the requirement that "operational equivalence coincides with denotational equality". For denotational semantics in more intensional models, such as the actor model and process calculi, there are different notions of equivalence within each model, and so the concepts of adequacy and of full abstraction are a matter of debate, and harder to pin down. Also the mathematical structure of operational semantics and denotational semantics can become very close.

Additional desirable properties we may wish to hold between operational and denotational semantics are:

1. **Constructivism**: Constructivism is concerned with whether domain elements can be shown to exist by constructive methods.
2. **Independence of denotational and operational semantics**: The denotational semantics should be formalized using mathematical structures that are independent of the operational semantics of a programming language; However, the underlying concepts can be closely related. See the section on Compositionality below.
3. **Full completeness** or **definability**: Every morphism of the semantic model should be the denotation of a program.

## Compositionality

An important aspect of denotational semantics of programming languages is compositionality, by which the denotation of a program is constructed from denotations of its parts. For example, consider the expression "7 + 4". Compositionality in this case is to provide a meaning for "7 + 4" in terms of the meanings of "7", "4" and "+".

A basic denotational semantics in domain theory is compositional because it is given as follows. We start by considering program fragments, i.e. programs with free variables. A *typing context* assigns a type to each free variable. For instance, in the expression (*x* + *y*) might be considered in a typing context (*x*:`nat`,*y*:`nat`). We now give a denotational semantics to program fragments, using the following scheme.

1. We begin by describing the meaning of the types of our language: the meaning of each type must be a domain. We write 〚τ〛 for the domain denoting the type τ. For instance, the meaning of type `nat` should be the domain of natural numbers: 〚`nat`〛= $\mathbb {N}$ ⊥.
2. From the meaning of types we derive a meaning for typing contexts. We set 〚 *x*1:τ1,..., *x*n:τn〛 = 〚 τ1〛× ... ×〚τn〛. For instance, 〚*x*:`nat`,*y*:`nat`〛= $\mathbb {N}$ ⊥× $\mathbb {N}$ ⊥. As a special case, the meaning of the empty typing context, with no variables, is the domain with one element, denoted 1.
3. Finally, we must give a meaning to each program-fragment-in-typing-context. Suppose that *P* is a program fragment of type σ, in typing context Γ, often written Γ⊢*P*:σ. Then the meaning of this program-in-typing-context must be a continuous function 〚Γ⊢*P*:σ〛:〚Γ〛→〚σ〛. For instance, 〚⊢7:`nat`〛:1→ $\mathbb {N}$ ⊥ is the constantly "7" function, while 〚*x*:`nat`,*y*:`nat`⊢*x*+*y*:`nat`〛: $\mathbb {N}$ ⊥× $\mathbb {N}$ ⊥→ $\mathbb {N}$ ⊥ is the function that adds two numbers.

Now, the meaning of the compound expression (7+4) is determined by composing the three functions 〚⊢7:`nat`〛:1→ $\mathbb {N}$ ⊥, 〚⊢4:`nat`〛:1→ $\mathbb {N}$ ⊥, and 〚*x*:`nat`,*y*:`nat`⊢*x*+*y*:`nat`〛: $\mathbb {N}$ ⊥× $\mathbb {N}$ ⊥→ $\mathbb {N}$ ⊥.

In fact, this is a general scheme for compositional denotational semantics. There is nothing specific about domains and continuous functions here. One can work with a different category instead. For example, in game semantics, the category of games has games as objects and strategies as morphisms: we can interpret types as games, and programs as strategies. For a simple language without general recursion, we can make do with the category of sets and functions. For a language with side-effects, we can work in the Kleisli category for a monad. For a language with state, we can work in a functor category. Milner has advocated modelling location and interaction by working in a category with interfaces as objects and *bigraphs* as morphisms.

## Semantics versus implementation

According to Dana Scott (1980):

It is not necessary for the semantics to determine an implementation, but it should provide criteria for showing that an implementation is correct.

According to Clinger (1981):

Usually, however, the formal semantics of a conventional sequential programming language may itself be interpreted to provide an (inefficient) implementation of the language. A formal semantics need not always provide such an implementation, though, and to believe that semantics must provide an implementation leads to confusion about the formal semantics of concurrent languages. Such confusion is painfully evident when the presence of unbounded nondeterminism in a programming language's semantics is said to imply that the programming language cannot be implemented.

## Connections to other areas of computer science

Some work in denotational semantics has interpreted types as domains in the sense of domain theory, which can be seen as a branch of model theory, leading to connections with type theory and category theory. Within computer science, there are connections with abstract interpretation, program verification, and model checking.
