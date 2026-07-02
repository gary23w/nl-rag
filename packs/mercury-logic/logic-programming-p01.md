---
title: "Logic programming (part 1/2)"
source: https://en.wikipedia.org/wiki/Logic_programming
domain: mercury-logic
license: CC-BY-SA-4.0
tags: mercury language, logic programming, prolog language, declarative programming, constraint logic programming
fetched: 2026-07-02
part: 1/2
---

# Logic programming

**Logic programming** is a programming, database, and knowledge representation paradigm based on formal logic. A logic program is a set of sentences in logical form, representing knowledge about some problem domain. Computation is performed by applying logical reasoning to that knowledge, to solve problems in the domain. Major logic programming language families include Prolog, Answer Set Programming (ASP), and Datalog. In all of these languages, rules are written in the form of *clauses*:

A :- B

1

, ..., B

n

.

and are read as declarative sentences in logical form:

A if B

1

and ... and B

n

.

`A` is called the *head* of the rule, `B1`, ..., `Bn` is called the *body*, and the `Bi` are called *literals* or conditions. When n = 0, the rule is called a *fact* and is written in the simplified form:

A.

Queries (or goals) have the same syntax as the bodies of rules and are commonly written in the form:

?- B

1

, ..., B

n

.

In the simplest case of Horn clauses (or "definite" clauses), all of the A, B1, ..., Bn are atomic formulae of the form p(t1 ,..., tm), where p is a predicate symbol naming a relation, like "motherhood", and the ti are terms naming objects (or individuals). Terms include both constant symbols, like "charles", and variables, such as X, which start with an upper case letter.

Consider, for example, the following Horn clause program:

```mw
mother_child(elizabeth, charles).
father_child(charles, william).
father_child(charles, harry).
parent_child(X, Y) :- 
     mother_child(X, Y).
parent_child(X, Y) :- 
     father_child(X, Y).
grandparent_child(X, Y) :- 
     parent_child(X, Z), 
     parent_child(Z, Y).
```

Given a query, the program produces answers. For instance for a query `?- parent_child(X, william)`, the single answer is

```mw
X = charles
```

Various queries can be asked. For instance the program can be queried both to generate grandparents and to generate grandchildren. It can even be used to generate all pairs of grandchildren and grandparents, or simply to check if a given pair is such a pair:

```mw
grandparent_child(X, william).
X = elizabeth

?- grandparent_child(elizabeth, Y).
Y = william;
Y = harry.

?- grandparent_child(X, Y).
X = elizabeth
Y = william;
X = elizabeth
Y = harry.

?- grandparent_child(william, harry).
no
?- grandparent_child(elizabeth, harry).
yes
```

Although Horn clause logic programs are Turing complete, for most practical applications, Horn clause programs need to be extended to "normal" logic programs with negative conditions. For example, the definition of sibling uses a negative condition, where the predicate = is defined by the clause `X = X`:

```mw
sibling(X, Y) :- 
     parent_child(Z, X), 
     parent_child(Z, Y), 
     not(X = Y).
```

Logic programming languages that include negative conditions have the knowledge representation capabilities of a non-monotonic logic.

In ASP and Datalog, logic programs have only a declarative reading, and their execution is performed by means of a proof procedure or model generator whose behaviour is not meant to be controlled by the programmer. However, in the Prolog family of languages, logic programs also have a procedural interpretation as goal-reduction procedures. From this point of view, clause A :- B1,...,Bn is understood as:

to solve

A

, solve

B

1

, and ... and solve

B

n

.

Negative conditions in the bodies of clauses also have a procedural interpretation, known as *negation as failure*: A negative literal `not B` is deemed to hold if and only if the positive literal `B` fails to hold.

Much of the research in the field of logic programming has been concerned with trying to develop a logical semantics for negation as failure and with developing other semantics and other implementations for negation. These developments have been important, in turn, for supporting the development of formal methods for logic-based program verification and program transformation.


## History

The use of mathematical logic to represent and execute computer programs is also a feature of the lambda calculus, developed by Alonzo Church in the 1930s. However, the first proposal to use the clausal form of logic for representing computer programs was made by Cordell Green. This used an axiomatization of a subset of LISP, together with a representation of an input-output relation, to compute the relation by simulating the execution of the program in LISP. Foster and Elcock's Absys, on the other hand, employed a combination of equations and lambda calculus in an assertional programming language that places no constraints on the order in which operations are performed.

Logic programming, with its current syntax of facts and rules, can be traced back to debates in the late 1960s and early 1970s about declarative versus procedural representations of knowledge in artificial intelligence. Advocates of declarative representations were notably working at Stanford, associated with John McCarthy, Bertram Raphael, and Cordell Green, and in Edinburgh, with John Alan Robinson (an academic visitor from Syracuse University), Pat Hayes, and Robert Kowalski. Advocates of procedural representations were mainly centered at MIT, under the leadership of Marvin Minsky and Seymour Papert.

Although it was based on the proof methods of logic, Planner, developed by Carl Hewitt at MIT, was the first language to emerge within this proceduralist paradigm. Planner featured pattern-directed invocation of procedural plans from goals (i.e. goal-reduction or backward chaining) and from assertions (i.e. forward chaining). The most influential implementation of Planner was the subset of Planner, called Micro-Planner, implemented by Gerry Sussman, Eugene Charniak, and Terry Winograd. Winograd used Micro-Planner to implement the landmark, natural-language understanding program SHRDLU. For the sake of efficiency, Planner used a backtracking control structure so that only one possible computation path had to be stored at a time. Planner gave rise to the programming languages QA4, Popler, Conniver, QLISP, and the concurrent language Ether.

Hayes and Kowalski in Edinburgh tried to reconcile the logic-based declarative approach to knowledge representation with Planner's procedural approach. Hayes (1973) developed an equational language, Golux, in which different procedures could be obtained by altering the behavior of the theorem prover.

In the meanwhile, Alain Colmerauer in Marseille was working on natural-language understanding, using logic to represent semantics and using resolution for question-answering. During the summer of 1971, Colmerauer invited Kowalski to Marseille, and together they discovered that the clausal form of logic could be used to represent formal grammars and that resolution theorem provers could be used for parsing. They observed that some theorem provers, like hyper-resolution, behave as bottom-up parsers and others, like SL resolution (1971) behave as top-down parsers.

It was in the following summer of 1972, that Kowalski, again working with Colmerauer, developed the procedural interpretation of implications in clausal form. It also became clear that such clauses could be restricted to definite clauses or Horn clauses, and that SL-resolution could be restricted (and generalised) to SLD resolution. Kowalski's procedural interpretation and SLD were described in a 1973 memo, published in 1974.

Colmerauer, with Philippe Roussel, used the procedural interpretation as the basis of Prolog, which was implemented in the summer and autumn of 1972. The first Prolog program, also written in 1972 and implemented in Marseille, was a French question-answering system. The use of Prolog as a practical programming language was given great momentum by the development of a compiler by David H. D. Warren in Edinburgh in 1977. Experiments demonstrated that Edinburgh Prolog could compete with the processing speed of other symbolic programming languages such as Lisp. Edinburgh Prolog became the *de facto* standard and strongly influenced the definition of ISO standard Prolog.

Logic programming gained international attention during the 1980s, when it was chosen by the Japanese Ministry of International Trade and Industry to develop the software for the Fifth Generation Computer Systems (FGCS) project. The FGCS project aimed to use logic programming to develop advanced Artificial Intelligence applications on massively parallel computers. Although the project initially explored the use of Prolog, it later adopted the use of concurrent logic programming, because it was closer to the FGCS computer architecture.

However, the committed choice feature of concurrent logic programming interfered with the language's logical semantics and with its suitability for knowledge representation and problem solving applications. Moreover, the parallel computer systems developed in the project failed to compete with advances taking place in the development of more conventional, general-purpose computers. Together these two issues resulted in the FGCS project failing to meet its objectives. Interest in both logic programming and AI fell into world-wide decline.

In the meanwhile, more declarative logic programming approaches, including those based on the use of Prolog, continued to make progress independently of the FGCS project. In particular, although Prolog was developed to combine declarative and procedural representations of knowledge, the purely declarative interpretation of logic programs became the focus for applications in the field of deductive databases. Work in this field became prominent around 1977, when Hervé Gallaire and Jack Minker organized a workshop on logic and databases in Toulouse. The field was eventually renamed as *Datalog*.

This focus on the logical, declarative reading of logic programs was given further impetus by the development of constraint logic programming in the 1980s and Answer Set Programming in the 1990s. It is also receiving renewed emphasis in recent applications of Prolog

The Association for Logic Programming (ALP) was founded in 1986 to promote Logic Programming. Its official journal until 2000, was *The Journal of Logic Programming*. Its founding editor-in-chief was J. Alan Robinson. In 2001, the journal was renamed *The Journal of Logic and Algebraic Programming*, and the official journal of ALP became *Theory and Practice of Logic Programming*, published by Cambridge University Press.


## Concepts

Logic programs enjoy a rich variety of semantics and problem solving methods, as well as a wide range of applications in programming, databases, knowledge representation, and problem solving.

### Algorithm = Logic + Control

The procedural interpretation of logic programs, which uses backward reasoning to reduce goals to subgoals, is a special case of the use of a problem-solving strategy to **control** the use of a declarative, **logical** representation of knowledge to obtain the behaviour of an **algorithm**. More generally, different problem-solving strategies can be applied to the same logical representation to obtain different algorithms. Alternatively, different algorithms can be obtained with a given problem-solving strategy by using different logical representations.

The two main problem-solving strategies are backward reasoning (goal reduction) and forward reasoning, also known as top-down and bottom-up reasoning, respectively.

In the simple case of a propositional Horn clause program and a top-level atomic goal, backward reasoning determines an and-or tree, which constitutes the search space for solving the goal. The top-level goal is the root of the tree. Given any node in the tree and any clause whose head matches the node, there exists a set of child nodes corresponding to the sub-goals in the body of the clause. These child nodes are grouped together by an "and". The alternative sets of children corresponding to alternative ways of solving the node are grouped together by an "or".

Any search strategy can be used to search this space. Prolog uses a sequential, last-in-first-out, backtracking strategy, in which only one alternative and one sub-goal are considered at a time. For example, subgoals can be solved in parallel, and clauses can also be tried in parallel. The first strategy is called **and-parallel** and the second strategy is called **or-parallel**. Other search strategies, such as intelligent backtracking, or best-first search to find an optimal solution, are also possible.

In the more general, non-propositional case, where sub-goals can share variables, other strategies can be used, such as choosing the subgoal that is most highly instantiated or that is sufficiently instantiated so that only one procedure applies. Such strategies are used, for example, in concurrent logic programming.

In most cases, backward reasoning from a query or goal is more efficient than forward reasoning. But sometimes with Datalog and Answer Set Programming, there may be no query that is separate from the set of clauses as a whole, and then generating all the facts that can be derived from the clauses is a sensible problem-solving strategy. Here is another example, where forward reasoning beats backward reasoning in a more conventional computation task, where the goal `?- fibonacci(n, Result)` is to find the nth fibonacci number:

```mw
fibonacci(0, 0).
fibonacci(1, 1).

fibonacci(N, Result) :-
    N > 1,
    N1 is N - 1,
    N2 is N - 2,
    fibonacci(N1, F1),
    fibonacci(N2, F2),
    Result is F1 + F2.
```

Here the relation `fibonacci(N, M)` stands for the function `fibonacci(N) = M`, and the predicate `N is Expression` is Prolog notation for the predicate that instantiates the variable `N` to the value of `Expression`.

Given the goal of computing the fibonacci number of `n`, backward reasoning reduces the goal to the two subgoals of computing the fibonacci numbers of n-1 and n-2. It reduces the subgoal of computing the fibonacci number of n-1 to the two subgoals of computing the fibonacci numbers of n-2 and n-3, redundantly computing the fibonacci number of n-2. This process of reducing one fibonacci subgoal to two fibonacci subgoals continues until it reaches the numbers 0 and 1. Its complexity is of the order 2n. In contrast, forward reasoning generates the sequence of fibonacci numbers, starting from 0 and 1 without any recomputation, and its complexity is linear with respect to n.

Prolog cannot perform forward reasoning directly. But it can achieve the effect of forward reasoning within the context of backward reasoning by means of tabling: Subgoals are maintained in a table, along with their solutions. If a subgoal is re-encountered, it is solved directly by using the solutions already in the table, instead of re-solving the subgoals redundantly.

### Relationship with functional programming

Logic programming can be viewed as a generalisation of functional programming, in which functions are a special case of relations. For example, the function, mother(X) = Y, (every X has only one mother Y) can be represented by the relation mother(X, Y). In this respect, logic programs are similar to relational databases, which also represent functions as relations.

Compared with relational syntax, functional syntax is more compact for nested functions. For example, in functional syntax the definition of maternal grandmother can be written in the nested form:

```mw
maternal_grandmother(X) = mother(mother(X)).
```

The same definition in relational notation needs to be written in the unnested, flattened form:

```mw
maternal_grandmother(X, Y) :- mother(X, Z), mother(Z, Y).
```

However, nested syntax can be regarded as syntactic sugar for unnested syntax. Ciao Prolog, for example, transforms functional syntax into relational form and executes the resulting logic program using the standard Prolog execution strategy. Moreover, the same transformation can be used to execute nested relations that are not functional. For example:

```mw
grandparent(X) := parent(parent(X)).
parent(X) := mother(X).
parent(X) := father(X).

mother(charles) := elizabeth.
father(charles) := phillip.
mother(harry) := diana.
father(harry) := charles.

?- grandparent(X,Y).
X = harry,
Y = elizabeth.
X = harry,
Y = phillip.
```

### Relationship with relational programming

The term *relational programming* has been used to cover a variety of programming languages that treat functions as a special case of relations. Some of these languages, such as miniKanren and relational linear programming are logic programming languages in the sense of this article.

However, the relational language RML is an imperative programming language whose core construct is a relational expression, which is similar to an expression in first-order predicate logic.

Other relational programming languages are based on the relational calculus or relational algebra.

### Semantics of Horn clause programs

Viewed in purely logical terms, there are two approaches to the declarative semantics of Horn clause logic programs: One approach is the original *logical consequence semantics*, which understands solving a goal as showing that the goal is a theorem that is true in all models of the program.

In this approach, computation is theorem-proving in first-order logic; and both backward reasoning, as in SLD resolution, and forward reasoning, as in hyper-resolution, are correct and complete theorem-proving methods. Sometimes such theorem-proving methods are also regarded as providing a separate proof-theoretic (or operational) semantics for logic programs. But from a logical point of view, they are proof methods, rather than semantics.

The other approach to the declarative semantics of Horn clause programs is the *satisfiability semantics*, which understands solving a goal as showing that the goal is true (or satisfied) in some intended (or standard) model of the program. For Horn clause programs, there always exists such a standard model: It is the unique *minimal model* of the program.

Informally speaking, a minimal model is a model that, when it is viewed as the set of all (variable-free) facts that are true in the model, contains no smaller set of facts that is also a model of the program.

For example, the following facts represent the minimal model of the family relationships example in the introduction of this article. All other variable-free facts are false in the model:

```mw
mother_child(elizabeth, charles).
father_child(charles, william).
father_child(charles, harry).
parent_child(elizabeth, charles).
parent_child(charles, william).
parent_child(charles, harry).
grandparent_child(elizabeth, william).
grandparent_child(elizabeth, harry).
```

The satisfiability semantics also has an alternative, more mathematical characterisation as the least fixed point of the function that uses the rules in the program to derive new facts from existing facts in one step of inference.

Remarkably, the same problem-solving methods of forward and backward reasoning, which were originally developed for the logical consequence semantics, are equally applicable to the satisfiability semantics: Forward reasoning generates the minimal model of a Horn clause program, by deriving new facts from existing facts, until no new additional facts can be generated. Backward reasoning, which succeeds by reducing a goal to subgoals, until all subgoals are solved by facts, ensures that the goal is true in the minimal model, without generating the model explicitly.

The difference between the two declarative semantics can be seen with the definitions of addition and multiplication in successor arithmetic, which represents the natural numbers `0, 1, 2, ...` as a sequence of terms of the form `0, s(0), s(s(0)), ...`. In general, the term `s(X)` represents the successor of `X,` namely `X + 1.` Here are the standard definitions of addition and multiplication in functional notation:

```
     X + 0 = X.
     X + s(Y)    = s(X + Y). 
i.e. X + (Y + 1) = (X + Y) + 1

     X × 0 = 0.
     X × s(Y)    = X + (X × Y). 
i.e. X × (Y + 1) = X + (X × Y).
```

Here are the same definitions as a logic program, using `add(X, Y, Z)` to represent `X + Y = Z,` and `multiply(X, Y, Z)` to represent `X × Y = Z`:

```mw
add(X, 0, X).
add(X, s(Y), s(Z)) :- add(X, Y, Z).

multiply(X, 0, 0).
multiply(X, s(Y), W) :- multiply(X, Y, Z), add(X, Z, W).
```

The two declarative semantics both give the same answers for the same existentially quantified conjunctions of addition and multiplication goals. For example `2 × 2 = X` has the solution `X = 4`; and `X × X = X + X` has two solutions `X = 0` and `X = 2`:

```mw
?- multiply(s(s(0)), s(s(0)), X).
X = s(s(s(s(0)))).

?- multiply(X, X, Y), add(X, X, Y).
X = 0, Y = 0.
X = s(s(0)), Y = s(s(s(s(0)))).
```

However, with the logical-consequence semantics, there are non-standard models of the program, in which, for example, `add(s(s(0)), s(s(0)), s(s(s(s(s(0)))))),` i.e. `2 + 2 = 5` is true. But with the satisfiability semantics, there is only one model, namely the standard model of arithmetic, in which `2 + 2 = 5` is false.

In both semantics, the goal `?- add(s(s(0)), s(s(0)), s(s(s(s(s(0))))))` fails. In the satisfiability semantics, the failure of the goal means that the truth value of the goal is false. But in the logical consequence semantics, the failure means that the truth value of the goal is unknown.

### Negation as failure

Negation as failure (NAF), as a way of concluding that a negative condition `not p` holds by showing that the positive condition `p` fails to hold, was already a feature of early Prolog systems. The resulting extension of SLD resolution is called SLDNF. A similar construct, called "thnot", also existed in Micro-Planner.

The logical semantics of NAF was unresolved until Keith Clark showed that, under certain natural conditions, NAF is an efficient, correct (and sometimes complete) way of reasoning with the logical consequence semantics using the *completion* of a logic program in first-order logic.

Completion amounts roughly to regarding the set of all the program clauses with the same predicate in the head, say:

A :- Body

1

.

...

A :- Body

k

.

as a definition of the predicate:

A iff (Body

1

or ... or Body

k

)

where `iff` means "if and only if". The completion also includes axioms of equality, which correspond to unification. Clark showed that proofs generated by SLDNF are structurally similar to proofs generated by a natural deduction style of reasoning with the completion of the program.

Consider, for example, the following program:

```mw
should_receive_sanction(X, punishment) :- 
    is_a_thief(X),
    not should_receive_sanction(X, rehabilitation).
    
should_receive_sanction(X, rehabilitation) :-
    is_a_thief(X),
    is_a_minor(X),
    not is_violent(X).
    
is_a_thief(tom).
```

Given the goal of determining whether tom should receive a sanction, the first rule succeeds in showing that tom should be punished:

```mw
?- should_receive_sanction(tom, Sanction).
Sanction = punishment.
```

This is because tom is a thief, and it cannot be shown that tom should be rehabilitated. It cannot be shown that tom should be rehabilitated, because it cannot be shown that tom is a minor.

If, however, we receive new information that tom is indeed a minor, the previous conclusion that tom should be punished is replaced by the new conclusion that tom should be rehabilitated:

```mw
is_a_minor(tom).

?- should_receive_sanction(tom, Sanction).
Sanction = rehabilitation.
```

This property of withdrawing a conclusion when new information is added, is called non-monotonicity, and it makes logic programming a non-monotonic logic.

But, if we are now told that tom is violent, the conclusion that tom should be punished will be reinstated:

```mw
is_violent(tom).

?- should_receive_sanction(tom, Sanction).
Sanction = punishment.
```

The completion of this program is:

```mw
should_receive_sanction(X, Sanction) iff 
    Sanction = punishment, is_a_thief(X), 
    not should_receive_sanction(X, rehabilitation)
 or Sanction = rehabilitation, is_a_thief(X), is_a_minor(X),
    not is_violent(X).
    
is_a_thief(X) iff X = tom.
is_a_minor(X) iff X = tom.
is_violent(X) iff X = tom.
```

The notion of completion is closely related to John McCarthy's circumscription semantics for default reasoning, and to Ray Reiter's closed world assumption.

The completion semantics for negation is a logical consequence semantics, for which SLDNF provides a proof-theoretic implementation. However, in the 1980s, the satisfiability semantics became more popular for logic programs with negation. In the satisfiability semantics, negation is interpreted according to the classical definition of truth in an intended or standard model of the logic program.

In the case of logic programs with negative conditions, there are two main variants of the satisfiability semantics: In the well-founded semantics, the intended model of a logic program is a unique, three-valued, minimal model, which always exists. The well-founded semantics generalises the notion of inductive definition in mathematical logic. XSB Prolog implements the well-founded semantics using SLG resolution.

In the alternative stable model semantics, there may be no intended models or several intended models, all of which are minimal and two-valued. The stable model semantics underpins answer set programming (ASP).

Both the well-founded and stable model semantics apply to arbitrary logic programs with negation. However, both semantics coincide for stratified logic programs. For example, the program for sanctioning thieves is (locally) stratified, and all three semantics for the program determine the same intended model:

```mw
should_receive_sanction(tom, punishment).
is_a_thief(tom).
is_a_minor(tom).
is_violent(tom).
```

Attempts to understand negation in logic programming have also contributed to the development of abstract argumentation frameworks. In an argumentation interpretation of negation, the initial argument that tom should be punished because he is a thief, is attacked by the argument that he should be rehabilitated because he is a minor. But the fact that tom is violent undermines the argument that tom should be rehabilitated and reinstates the argument that tom should be punished.

### Metalogic programming

Metaprogramming, in which programs are treated as data, was already a feature of early Prolog implementations. For example, the Edinburgh DEC10 implementation of Prolog included "an interpreter and a compiler, both written in Prolog itself". The simplest metaprogram is the so-called "vanilla" meta-interpreter:

```mw
    solve(true).
    solve((B,C)):- solve(B),solve(C).
    solve(A):- clause(A,B),solve(B).
```

where true represents an empty conjunction, and (B,C) is a composite term representing the conjunction of B and C. The predicate clause(A,B) means that there is a clause of the form A :- B.

Metaprogramming is an application of the more general use of a *metalogic* or *metalanguage* to describe and reason about another language, called the *object language*.

Metalogic programming allows object-level and metalevel representations to be combined, as in natural language. For example, in the following program, the atomic formula `attends(Person, Meeting)` occurs both as an object-level formula, and as an argument of the metapredicates `prohibited` and `approved.`

```mw
prohibited(attends(Person, Meeting)) :- 
    not(approved(attends(Person, Meeting))).

should_receive_sanction(Person, scolding) :- attends(Person, Meeting), 
    lofty(Person), prohibited(attends(Person, Meeting)).
should_receive_sanction(Person, banishment) :- attends(Person, Meeting), 
    lowly(Person), prohibited(attends(Person, Meeting)).

approved(attends(alice, tea_party)).
attends(mad_hatter, tea_party).
attends(dormouse, tea_party).

lofty(mad_hatter).
lowly(dormouse).

?- should_receive_sanction(X,Y).
Person = mad_hatter,
Sanction = scolding.
Person = dormouse,
Sanction = banishment.
```

### Relationship with the Computational-representational understanding of mind

In his popular Introduction to Cognitive Science, Paul Thagard includes logic and rules as alternative approaches to modelling human thinking. He argues that rules, which have the form *IF condition THEN action*, are "very similar" to logical conditionals, but they are simpler and have greater psychological plausibility (page 51). Among other differences between logic and rules, he argues that logic uses deduction, but rules use search (page 45) and can be used to reason either forward or backward (page 47). Sentences in logic "have to be interpreted as *universally true*", but rules can be *defaults*, which admit exceptions (page 44).

He states that "unlike logic, rule-based systems can also easily represent strategic information about what to do" (page 45). For example, "IF you want to go home for the weekend, and you have bus fare, THEN you can catch a bus". He does not observe that the same strategy of reducing a goal to subgoals can be interpreted, in the manner of logic programming, as applying backward reasoning to a logical conditional:

```mw
can_go(you, home) :- have(you, bus_fare), catch(you, bus).
```

All of these characteristics of rule-based systems - search, forward and backward reasoning, default reasoning, and goal-reduction - are also defining characteristics of logic programming. This suggests that Thagard's conclusion (page 56) that:

> Much of human knowledge is naturally described in terms of rules, and many kinds of thinking such as planning can be modeled by rule-based systems.

also applies to logic programming.

Other arguments showing how logic programming can be used to model aspects of human thinking are presented by Keith Stenning and Michiel van Lambalgen in their book, Human Reasoning and Cognitive Science. They show how the non-monotonic character of logic programs can be used to explain human performance on a variety of psychological tasks. They also show (page 237) that "closed–world reasoning in its guise as logic programming has an appealing neural implementation, unlike classical logic."

In The Proper Treatment of Events, Michiel van Lambalgen and Fritz Hamm investigate the use of constraint logic programming to code "temporal notions in natural language by looking at the way human beings construct time".

### Knowledge representation

The use of logic to represent procedural knowledge and strategic information was one of the main goals contributing to the early development of logic programming. Moreover, it continues to be an important feature of the Prolog family of logic programming languages today. However, many applications of logic programming, including Prolog applications, increasingly focus on the use of logic to represent purely declarative knowledge. These applications include both the representation of general commonsense knowledge and the representation of domain specific expertise.

Commonsense includes knowledge about cause and effect, as formalised, for example, in the situation calculus, event calculus and action languages. Here is a simplified example, which illustrates the main features of such formalisms. The first clause states that a fact holds immediately after an event initiates (or causes) the fact. The second clause is a *frame axiom*, which states that a fact that holds at a time continues to hold at the next time unless it is terminated by an event that happens at the time. This formulation allows more than one event to occur at the same time:

```mw
holds(Fact, Time2) :- 
    happens(Event, Time1),
    Time2 is Time1 + 1,
    initiates(Event, Fact).
     
holds(Fact, Time2) :- 
	happens(Event, Time1),
    Time2 is Time1 + 1,
    holds(Fact, Time1),
    not(terminated(Fact, Time1)).

terminated(Fact, Time) :-
   happens(Event, Time),
   terminates(Event, Fact).
```

Here `holds` is a meta-predicate, similar to `solve` above. However, whereas `solve` has only one argument, which applies to general clauses, the first argument of `holds` is a fact and the second argument is a time (or state). The atomic formula `holds(Fact, Time)` expresses that the `Fact` holds at the `Time`. Such time-varying facts are also called fluents. The atomic formula `happens(Event, Time)` expresses that the Event happens at the `Time`.

The following example illustrates how these clauses can be used to reason about causality in a toy blocks world. Here, in the initial state at time 0, a green block is on a table and a red block is stacked on the green block (like a traffic light). At time 0, the red block is moved to the table. At time 1, the green block is moved onto the red block. Moving an object onto a place terminates the fact that the object is on any place, and initiates the fact that the object is on the place to which it is moved:

```mw
holds(on(green_block, table), 0).
holds(on(red_block, green_block), 0).

happens(move(red_block, table), 0).
happens(move(green_block, red_block), 1).

initiates(move(Object, Place), on(Object, Place)).
terminates(move(Object, Place2), on(Object, Place1)).

?- holds(Fact, Time).

Fact = on(green_block,table),
Time = 0.
Fact = on(red_block,green_block),
Time = 0.
Fact = on(green_block,table),
Time = 1.
Fact = on(red_block,table),
Time = 1.
Fact = on(green_block,red_block),
Time = 2.
Fact = on(red_block,table),
Time = 2.
```

Forward reasoning and backward reasoning generate the same answers to the goal `holds(Fact, Time)`. But forward reasoning generates fluents *progressively* in temporal order, and backward reasoning generates fluents *regressively*, as in the domain-specific use of regression in the situation calculus.

Logic programming has also proved to be useful for representing domain-specific expertise in expert systems. But human expertise, like general-purpose commonsense, is mostly implicit and tacit, and it is often difficult to represent such implicit knowledge in explicit rules. This difficulty does not arise, however, when logic programs are used to represent the existing, explicit rules of a business organisation or legal authority.

For example, here is a representation of a simplified version of the first sentence of the British Nationality Act, which states that a person who is born in the UK becomes a British citizen at the time of birth if a parent of the person is a British citizen at the time of birth:

```mw
initiates(birth(Person), citizen(Person, uk)):-
    time_of(birth(Person), Time),
    place_of(birth(Person), uk),
    parent_child(Another_Person, Person),
    holds(citizen(Another_Person, uk), Time).
```

Historically, the representation of a large portion of the British Nationality Act as a logic program in the 1980s was "hugely influential for the development of computational representations of legislation, showing how logic programming enables intuitively appealing representations that can be directly deployed to generate automatic inferences".

More recently, the PROLEG system, initiated in 2009 and consisting of approximately 2500 rules and exceptions of civil code and supreme court case rules in Japan, has become possibly the largest legal rule base in the world.
