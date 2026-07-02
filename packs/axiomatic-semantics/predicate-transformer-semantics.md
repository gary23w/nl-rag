---
title: "Predicate transformer semantics"
source: https://en.wikipedia.org/wiki/Predicate_transformer_semantics
domain: axiomatic-semantics
license: CC-BY-SA-4.0
tags: axiomatic semantics, predicate transformer semantics, assertion language, program correctness
fetched: 2026-07-02
---

# Predicate transformer semantics

**Predicate transformer semantics** were introduced by Edsger Dijkstra in his seminal paper "Guarded commands, nondeterminacy and formal derivation of programs". They define the semantics of an imperative programming paradigm by assigning to each *statement* in this language a corresponding *predicate transformer*: a total function between two *predicates* on the state space of the statement. In this sense, predicate transformer semantics are a kind of denotational semantics. Actually, in guarded commands, Dijkstra uses only one kind of predicate transformer: the well-known **weakest preconditions** (see below).

Moreover, predicate transformer semantics are a reformulation of Floyd–Hoare logic. Whereas Hoare logic is presented as a deductive system, predicate transformer semantics (either by **weakest-preconditions** or by **strongest-postconditions** see below) are **complete strategies** to build valid deductions of Hoare logic. In other words, they provide an effective algorithm to reduce the problem of verifying a Hoare triple to the problem of proving a first-order formula. Technically, predicate transformer semantics perform a kind of symbolic execution of statements into predicates: execution runs *backward* in the case of weakest-preconditions, or runs *forward* in the case of strongest-postconditions.

## Weakest preconditions

### Definition

For a statement *S* and a postcondition *R*, a **weakest precondition** is a predicate *Q* such that for any precondition P, $\{P\}S\{R\}$ if and only if $P\Rightarrow Q$ . In other words, it is the "loosest" or least restrictive requirement needed to guarantee that *R* holds after *S*. Uniqueness follows easily from the definition: If both *Q* and *Q'* are weakest preconditions, then by the definition $\{Q'\}S\{R\}$ so $Q'\Rightarrow Q$ and $\{Q\}S\{R\}$ so $Q\Rightarrow Q'$ , and thus $Q=Q'$ . We often use $wp(S,R)$ to denote the weakest precondition for statement *S* with respect to a postcondition *R*.

### Conventions

We use *T* to denote the predicate that is everywhere true and *F* to denote the one that is everywhere false. We shouldn't at least conceptually confuse ourselves with a Boolean expression defined by some language syntax, which might also contain true and false as Boolean scalars. For such scalars we need to do a type coercion such that we have T = predicate(true) and F = predicate(false). Such a promotion is carried out often casually, so people tend to take T as true and F as false.

| $wp({\texttt {skip}},R)\ =\ R$ |
|---|

### Abort

| $wp({\texttt {abort}},R)\ =\ {\texttt {F}}$ |
|---|

### Assignment

We give below two equivalent weakest-preconditions for the assignment statement. In these formulas, $R[x\leftarrow E]$ is a copy of *R* where free occurrences of *x* are replaced by *E*. Hence, here, expression *E* is implicitly coerced into a *valid term* of the underlying logic: it is thus a *pure* expression, totally defined, terminating and without side effect.

- version 1:

| $wp(x:=E,R)\ =\ (\forall y.y=E\Rightarrow R[x\leftarrow y])$ where *y* is a fresh variable and not free in E and R (representing the final value of variable *x*) |
|---|

- version 2:

Provided that *E* is well defined, we apply the so-called *one-point* rule on version 1. Then

| $wp(x:=E,R)\ =\ R[x\leftarrow E]$ |
|---|

The first version avoids a potential duplication of *x* in *R*, whereas the second version is simpler when there is at most a single occurrence of *x* in *R*. The first version also reveals a deep duality between weakest-precondition and strongest-postcondition (see below).

An example of a valid calculation of *wp* (using version 2) for assignments with integer valued variable *x* is:

${\begin{array}{rcl}wp(x:=x-5,x>10)&=&x-5>10\\&\Leftrightarrow &x>15\end{array}}$

This means that, for the postcondition *x > 10* to be true after the assignment, the precondition *x > 15* must be true before the assignment. This is also the "weakest precondition", in that it is the "weakest" restriction on the value of *x* which makes *x > 10* true after the assignment.

### Sequence

| $wp(S_{1};S_{2},R)\ =\ wp(S_{1},wp(S_{2},R))$ |
|---|

For example,

${\begin{array}{rcl}wp(x:=x-5;x:=x*2\ ,\ x>20)&=&wp(x:=x-5,wp(x:=x*2,x>20))\\&=&wp(x:=x-5,x*2>20)\\&=&(x-5)*2>20\\&=&x>15\end{array}}$

### Conditional

| $wp({\texttt {if}}\ E\ {\texttt {then}}\ S_{1}\ {\texttt {else}}\ S_{2}\ {\texttt {end}},R)\ =\ (E\Rightarrow wp(S_{1},R))\wedge (\neg E\Rightarrow wp(S_{2},R))$ |
|---|

As example:

${\begin{array}{rcl}wp({\texttt {if}}\ x<y\ {\texttt {then}}\ x:=y\ {\texttt {else}}\;\;{\texttt {skip}}\;\;{\texttt {end}},\ x\geq y)&=&(x<y\Rightarrow wp(x:=y,x\geq y))\ \wedge \ (\neg (x<y)\Rightarrow wp({\texttt {skip}},x\geq y))\\&=&(x<y\Rightarrow y\geq y)\ \wedge \ (\neg (x<y)\Rightarrow x\geq y)\\&\Leftrightarrow &{\texttt {true}}\end{array}}$

### While loop

#### Partial correctness

Ignoring termination for a moment, we can define the rule for the *weakest liberal precondition*, denoted *wlp*, using a predicate *INV*, called the Loop *INV*ariant, typically supplied by a programmer:

| $wlp({\texttt {while}}\ E\ {\texttt {do}}\ S\ {\texttt {done}},R)\Leftarrow \ {\textit {INV}}\ \ {\text{if}}\ \ {\begin{array}{l}\\(E\wedge {\textit {INV}}\Rightarrow wlp(S,{\textit {INV}}))\\\wedge \ (\neg E\wedge {\textit {INV}}\Rightarrow R)\end{array}}$ |
|---|

#### Total correctness

To show total correctness, we also have to show that the loop terminates. For this we define a well-founded relation on the state space denoted as (wfs, <) and define a variant function vf , such that we have:

| $wp({\texttt {while}}\ E\ {\texttt {do}}\ S\ {\texttt {done}},R)\ \Leftarrow \ {\textit {INV}}\ \ {\text{if}}\ \ \ \ {\begin{array}{l}\\(E\wedge {\textit {INV}}\Rightarrow {\textit {vf}}\in {\textit {wfs}})\\\wedge \ (E\wedge {\textit {INV}}\wedge v={\textit {vf}}\Rightarrow wp(S,{\textit {INV}}\wedge v<{\textit {vf}}))\\\wedge \ (\neg E\wedge {\textit {INV}}\Rightarrow R)\end{array}}$ where v is a fresh tuple of variables |
|---|

Informally, in the above conjunction of three formulas:

- the first one means that the variant must be part of the well-founded relation before entering the loop;
- the second one means that the body of the loop (i.e. statement S) must preserve the invariant and reduce the variant;
- the last one means that the loop postcondition R must be established when the loop finishes.

However, the conjunction of those three is not a necessary condition. Exactly, we have

| $wp({\texttt {while}}\ E\ {\texttt {do}}\ S\ {\texttt {done}},R)\ \ =\ \ {\text{the strongest solution of the recursive equation}}\ {\begin{array}{l}Z:[Z\equiv (E\wedge wp(S,Z))\vee (\neg E\wedge R)]\end{array}}$ |
|---|

### Non-deterministic guarded commands

Actually, Dijkstra's Guarded Command Language (GCL) is an extension of the simple imperative language given until here with non-deterministic statements. Indeed, GCL aims to be a formal notation to define algorithms. Non-deterministic statements represent choices left to the actual implementation (in an effective programming language): properties proved on non-deterministic statements are ensured for all possible choices of implementation. In other words, weakest-preconditions of non-deterministic statements ensure

- that there exists a terminating execution (e.g. there exists an implementation),
- and, that the final state of all terminating execution satisfies the postcondition.

The definitions of weakest-precondition given above (in particular for **while-loop**) preserve this property.

#### Selection

Selection is a generalization of **if** statement:

| $wp({\texttt {if}}\ E_{1}\rightarrow S_{1}\ [\!]\ \ldots \ [\!]\ E_{n}\rightarrow S_{n}\ {\texttt {fi}},R)\ ={\begin{array}{l}(E_{1}\vee \ldots \vee E_{n})\\\wedge \ (E_{1}\Rightarrow wp(S_{1},R))\\\ldots \\\wedge \ (E_{n}\Rightarrow wp(S_{n},R))\\\end{array}}$ |
|---|

Here, when two guards $E_{i}$ and $E_{j}$ are simultaneously true, then execution of this statement can run any of the associated statement $S_{i}$ or $S_{j}$ .

#### Repetition

Repetition is a generalization of **while** statement in a similar way.

### Specification statement

Refinement calculus extends GCL with the notion of *specification statement*. Syntactically, we prefer to write a specification statement as

```
     
  
    
      
        x
        :
        l
        [
        p
        r
        e
        ,
        p
        o
        s
        t
        ]
      
    
    {\displaystyle x:l[pre,post]}
  
```

which specifies a computation that starts in a state satisfying *pre* and is guaranteed to end in a state satisfying *post* by changing only *x*. We call l a logical constant employed to aid in a specification. For example, we can specify a computation that increment x by 1 as

```
     
  
    
      
        x
        :
        l
        [
        x
        =
        l
        ,
        x
        =
        l
        +
        1
        ]
      
    
    {\displaystyle x:l[x=l,x=l+1]}
  
```

Another example is a computation of a square root of an integer.

```
     
  
    
      
        x
        :
        l
        [
        x
        =
        
          l
          
            2
          
        
        ,
        x
        =
        l
        ]
      
    
    {\displaystyle x:l[x=l^{2},x=l]}
  
```

The specification statement appears like a primitive in the sense that it does not contain other statements. However, it is very expressive, as *pre* and *post* are arbitrary predicates. Its weakest precondition is as follows.

| $wp(x:l[pre,post],R)=(\exists l::pre)\wedge (\forall s:(\forall l:pre:post(x\leftarrow s)):R(x\leftarrow s))$ where *s* is fresh. |
|---|

It combines Morgan's syntactic idea with the sharpness idea by Bijlsma, Matthews and Wiltink. The very advantage of this is its capability of defining wp of goto L and other jump statements.

### Goto statement

Formalization of jump statements like *goto L* takes a very long bumpy process. A common belief seems to indicate the goto statement could only be argued operationally. This is probably due to a failure to recognize that *goto L* is actually miraculous (i.e. non-strict) and does not follow Dijkstra's coined Law of Miracle Excluded, as stood in itself. But it enjoys an extremely simple operational view from the weakest precondition perspective, which was unexpected. We define

| $wp({\texttt {goto}}\ L,R)=wpL$ where *wpL* is the weakest precondition at label *L*. |
|---|

For *goto L* execution transfers control to label *L* at which the weakest precondition must hold. The way that *wpL* is referred to in the rule should not be taken as a big surprise. It is only ⁠ $wp(L:S,Q)$ ⁠ for some *Q* computed to that point. This is like any wp rules, using constituent statements to give wp definitions, even though *goto L* appears a primitive. The rule does not require the uniqueness for locations where *wpL* holds within a program, so theoretically it allows the same label to appear in multiple locations as long as the weakest precondition at each location is the same wpL. The goto statement can jump to any of such locations. This actually justifies that we could place the same labels at the same location multiple times, as ⁠ $S(L:L:S1)$ ⁠, which is the same as ⁠ $S(L:S1)$ ⁠. Also, it does not imply any scoping rule, thus allowing a jump into a loop body, for example. Let us calculate wp of the following program S, which has a jump into the loop body.

```
     wp(do x > 0 → L: x := x-1 od;  if x < 0 → x := -x; goto L ⫿ x ≥ 0 → skip fi,  post)
   =   { sequential composition and alternation rules }
     wp(do x > 0 → L: x := x-1 od, (x<0 ∧ wp(x := -x; goto L, post)) ∨ (x ≥  0 ∧ post)
   =   { sequential composition, goto, assignment rules }
     wp(do x > 0 → L: x := x-1 od, x<0 ∧ wpL(x ← -x) ∨ x≥0 ∧ post)
   =   { repetition rule }
     the strongest solution of 
              Z: [ Z ≡ x > 0 ∧ wp(L: x := x-1, Z) ∨ x < 0 ∧ wpL(x ← -x) ∨ x=0 ∧ post ]    
   =  { assignment rule, found wpL = Z(x ← x-1) }
     the strongest solution of 
              Z: [ Z ≡ x > 0 ∧ Z(x ← x-1) ∨ x < 0 ∧ Z(x ← x-1) (x ← -x) ∨ x=0 ∧ post]
   =  { substitution }
     the strongest solution of 
              Z:[ Z ≡ x > 0 ∧ Z(x ← x-1) ∨ x < 0 ∧ Z(x ← -x-1) ∨ x=0 ∧ post ]
   =  { solve the equation by approximation }
     post(x ← 0)
```

Therefore,

```
wp(S, post) = post(x ← 0).
```

## Other predicate transformers

### Weakest liberal precondition

An important variant of the weakest precondition is the **weakest liberal precondition** $wlp(S,R)$ , which yields the weakest condition under which *S* either does not terminate or establishes *R*. It therefore differs from *wp* in not guaranteeing termination. Hence it corresponds to Hoare logic in partial correctness: for the statement language given above, *wlp* differs with *wp* only on **while-loop**, in not requiring a variant (see above).

### Strongest postcondition

Given *S* a statement and *R* a precondition (a predicate on the initial state), then $sp(S,R)$ is their **strongest-postcondition**: it implies any postcondition satisfied by the final state of any execution of S, for any initial state satisfying R. In other words, a Hoare triple $\{P\}S\{Q\}$ is provable in Hoare logic if and only if the predicate below hold:

$\forall x,sp(S,P)\Rightarrow Q$

Usually, **strongest-postconditions** are used in partial correctness. Hence, we have the following relation between weakest-liberal-preconditions and strongest-postconditions:

$(\forall x,P\Rightarrow wlp(S,Q))\ \Leftrightarrow \ (\forall x,sp(S,P)\Rightarrow Q)$

For example, on assignment we have:

| $sp(x:=E,R)\ =\ \exists y,x=E[x\leftarrow y]\wedge R[x\leftarrow y]$ where *y* is fresh |
|---|

Above, the logical variable *y* represents the initial value of variable *x*. Hence,

$sp(x:=x-5,x>15)\ =\ \exists y,x=y-5\wedge y>15\ \Leftrightarrow \ x>10$

On sequence, it appears that *sp* runs forward (whereas *wp* runs backward):

| $sp(S_{1};S_{2}\ ,\ R)\ =\ sp(S_{2},sp(S_{1},R))$ |
|---|

### Win and sin predicate transformers

Leslie Lamport has suggested *win* and *sin* as *predicate transformers* for concurrent programming.

## Predicate transformers properties

This section presents some characteristic properties of predicate transformers. Below, *S* denotes a predicate transformer (a function between two predicates on the state space) and *P* a predicate. For instance, *S(P)* may denote *wp(S,P)* or *sp(S,P)*. We keep *x* as the variable of the state space.

### Monotonic

Predicate transformers of interest (*wp*, *wlp*, and *sp*) are monotonic. A predicate transformer *S* is **monotonic** if and only if:

$(\forall x:P:Q)\Rightarrow (\forall x:S(P):S(Q))$

This property is related to the consequence rule of Hoare logic.

### Strict

A predicate transformer *S* is **strict** iff:

$S({\texttt {F}})\ \Leftrightarrow \ {\texttt {F}}$

For instance, *wp* is artificially made strict, whereas *wlp* is generally not. In particular, if statement *S* may not terminate then $wlp(S,{\texttt {F}})$ is satisfiable. We have

$wlp({\texttt {while}}\ {\texttt {true}}\ {\texttt {do}}\ {\texttt {skip}}\ {\texttt {done}},{\texttt {F}})\ \Leftrightarrow {\texttt {T}}$

Indeed, **T** is a valid invariant of that loop.

The non-strict but monotonic or conjunctive predicate transformers are called miraculous and can also be used to define a class of programming constructs, in particular, jump statements, which Dijkstra cared less about. Those jump statements include straight goto L, break and continue in a loop and return statements in a procedure body, exception handling, etc. It turns out that all jump statements are executable miracles, i.e. they can be implemented but not strict.

### Terminating

A predicate transformer *S* is **terminating** if:

$S({\texttt {T}})\ \Leftrightarrow \ {\texttt {T}}$

Actually, this terminology makes sense only for strict predicate transformers: indeed, $wp(S,{\texttt {T}})$ is the weakest-precondition ensuring termination of *S*.

It seems that naming this property **non-aborting** would be more appropriate: in total correctness, non-termination is abortion, whereas in partial correctness, it is not.

### Conjunctive

A predicate transformer *S* is **conjunctive** iff:

$S(P\wedge Q)\ \Leftrightarrow \ S(P)\wedge S(Q)$

This is the case for $wp(S,.)$ , even if statement *S* is non-deterministic as a selection statement or a specification statement.

### Disjunctive

A predicate transformer *S* is **disjunctive** iff:

$S(P\vee Q)\ \Leftrightarrow \ S(P)\vee S(Q)$

This is generally not the case of $wp(S,.)$ when *S* is non-deterministic. Indeed, consider a non-deterministic statement *S* choosing an arbitrary Boolean. This statement is given here as the following *selection statement*:

$S\ =\ {\texttt {if}}\ {\texttt {true}}\rightarrow x:=0\ [\!]\ {\texttt {true}}\rightarrow x:=1\ {\texttt {fi}}$

Then, $wp(S,R)$ reduces to the formula $R[x\leftarrow 0]\wedge R[x\leftarrow 1]$ .

Hence, $wp(S,\ x=0\vee x=1)$ reduces to the *tautology* $(0=0\vee 0=1)\wedge (1=0\vee 1=1)$

Whereas, the formula $wp(S,x=0)\vee wp(S,x=1)$ reduces to the *wrong proposition* $(0=0\wedge 1=0)\vee (1=0\wedge 1=1)$ .

## Applications

- Computations of weakest-preconditions are largely used to statically check assertions in programs using a theorem-prover (like a satisfiability modulo theories (SMT) solver or interactive theorem proving assistant): see Frama-C or ESC/Java2.
- Unlike many other semantic formalisms, predicate transformer semantics was not designed as an investigation into foundations of computation. Rather, it was intended to provide programmers with a methodology to develop their programs as "correct by construction" in a "calculation style". This "top-down" style was advocated by Dijkstra and N. Wirth. It has been formalized further by R.-J. Back and others in the refinement calculus. Some tools like B-Method now provide automated reasoning to promote this methodology.
- In the meta-theory of Hoare logic, weakest-preconditions appear as a key notion in the proof of relative completeness.

## Beyond predicate transformers

### Weakest-preconditions and strongest-postconditions of imperative expressions

In predicate transformers semantics, expressions are restricted to terms of the logic (see above). However, this restriction seems too strong for most existing programming languages, where expressions may have side effects (call to a function having a side effect), may not terminate or abort (like *division by zero*). There are many proposals to extend weakest-preconditions or strongest-postconditions for imperative expression languages and in particular for monads.

Among them, *Hoare Type Theory* combines Hoare logic for a Haskell-like language, separation logic and type theory. This system is implemented as a Rocq library named *Ynot*. In this language, evaluation of expressions corresponds to computations of *strongest-postconditions*.

### Probabilistic predicate transformers

*Probabilistic predicate transformers* are an extension of predicate transformers for probabilistic programs. Such programs have many uses in cryptography (hiding information using some randomized noise), distributed computing (symmetry breaking).
