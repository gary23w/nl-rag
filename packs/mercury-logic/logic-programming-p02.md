---
title: "Logic programming (part 2/2)"
source: https://en.wikipedia.org/wiki/Logic_programming
domain: mercury-logic
license: CC-BY-SA-4.0
tags: mercury language, logic programming, prolog language, declarative programming, constraint logic programming
fetched: 2026-07-02
part: 2/2
---

## Variants and extensions

### Prolog

The SLD resolution rule of inference is neutral about the order in which subgoals in the bodies of clauses can be *selected* for solution. For the sake of efficiency, Prolog restricts this order to the order in which the subgoals are written. SLD is also neutral about the strategy for searching the space of SLD proofs. Prolog searches this space, top-down, depth-first, trying different clauses for solving the same (sub)goal in the order in which the clauses are written.

This search strategy has the advantage that the current branch of the tree can be represented efficiently by a stack. When a goal clause at the top of the stack is reduced to a new goal clause, the new goal clause is pushed onto the top of the stack. When the selected subgoal in the goal clause at the top of the stack cannot be solved, the search strategy *backtracks*, removing the goal clause from the top of the stack, and retrying the attempted solution of the selected subgoal in the previous goal clause using the next clause that matches the selected subgoal.

Backtracking can be restricted by using a subgoal, called *cut*, written as !, which always succeeds but cannot be backtracked. Cut can be used to improve efficiency, but can also interfere with the logical meaning of clauses. In many cases, the use of cut can be replaced by negation as failure. In fact, negation as failure can be defined in Prolog, by using cut, together with any literal, say *fail*, that unifies with the head of no clause:

```mw
not(P) :- P, !, fail.
not(P).
```

Prolog provides other features, in addition to cut, that do not have a logical interpretation. These include the built-in predicates *assert* and *retract* for destructively updating the state of the program during program execution.

For example, the toy blocks world example above can be implemented without frame axioms using destructive change of state:

```mw
on(green_block, table).
on(red_block, green_block).

move(Object, Place2) :- 
	retract(on(Object, Place1)), 
	assert(on(Object, Place2).
```

The sequence of move events and the resulting locations of the blocks can be computed by executing the query:

```mw
?- move(red_block, table), move(green_block, red_block), on(Object, Place).

Object = red_block,
Place = table.
Object = green_block,
Place = red_block.
```

Various extensions of logic programming have been developed to provide a logical framework for such destructive change of state.

The broad range of Prolog applications, both in isolation and in combination with other languages is highlighted in the Year of Prolog Book, celebrating the 50 year anniversary of Prolog in 2022.

Prolog has also contributed to the development of other programming languages, including ALF, Fril, Gödel, Mercury, Oz, Ciao, Visual Prolog, XSB, and λProlog.

### Constraint logic programming

Constraint logic programming (CLP) combines Horn clause logic programming with constraint solving. It extends Horn clauses by allowing some predicates, declared as constraint predicates, to occur as literals in the body of a clause. Constraint predicates are not defined by the facts and rules in the program, but are predefined by some domain-specific model-theoretic structure or theory.

Procedurally, subgoals whose predicates are defined by the program are solved by goal-reduction, as in ordinary logic programming, but constraints are simplified and checked for satisfiability by a domain-specific constraint-solver, which implements the semantics of the constraint predicates. An initial problem is solved by reducing it to a satisfiable conjunction of constraints.

Interestingly, the first version of Prolog already included a constraint predicate dif(term1, term2), from Philippe Roussel's 1972 PhD thesis, which succeeds if both of its arguments are different terms, but which is delayed if either of the terms contains a variable.

The following constraint logic program represents a toy temporal database of `john's` history as a teacher:

```mw
teaches(john, hardware, T) :- 1990 ≤ T, T < 1999.
teaches(john, software, T) :- 1999 ≤ T, T < 2005.
teaches(john, logic, T) :- 2005 ≤ T, T ≤ 2012.
rank(john, instructor, T) :- 1990 ≤ T, T < 2010.
rank(john, professor, T) :- 2010 ≤ T, T < 2014.
```

Here `≤` and `<` are constraint predicates, with their usual intended semantics. The following goal clause queries the database to find out when `john` both taught `logic` and was a `professor`:

```mw
?- teaches(john, logic, T), rank(john, professor, T).
```

The solution `2010 ≤ T, T ≤ 2012` results from simplifying the constraints `2005 ≤ T, T ≤ 2012, 2010 ≤ T, T < 2014.`

Constraint logic programming has been used to solve problems in such fields as civil engineering, mechanical engineering, digital circuit verification, automated timetabling, air traffic control, and finance. It is closely related to abductive logic programming.

### Datalog

Datalog is a database definition language, which combines a relational view of data, as in relational databases, with a logical view, as in logic programming.

Relational databases use a relational calculus or relational algebra, with relational operations, such as *union*, *intersection*, *set difference* and *cartesian product* to specify queries, which access a database. Datalog uses logical connectives, such as *or*, *and* and *not* in the bodies of rules to define relations as part of the database itself.

It was recognized early in the development of relational databases that recursive queries cannot be expressed in either relational algebra or relational calculus, and that this deficiency can be remedied by introducing a least-fixed-point operator. In contrast, recursive relations can be defined naturally by rules in logic programs, without the need for any new logical connectives or operators.

Datalog differs from more general logic programming by having only constants and variables as terms. Moreover, all facts are variable-free, and rules are restricted, so that if they are executed bottom-up, then the derived facts are also variable-free.

For example, consider the family database:

```mw
mother_child(elizabeth, charles).
father_child(charles, william).
father_child(charles, harry).
parent_child(X, Y) :- 
     mother_child(X, Y).
parent_child(X, Y) :- 
     father_child(X, Y).
ancestor_descendant(X, Y) :- 
     parent_child(X, X).
ancestor_descendant(X, Y) :- 
     ancestor_descendant(X, Z), 
     ancestor_descendant(Z, Y).
```

Bottom-up execution derives the following set of additional facts and terminates:

```mw
parent_child(elizabeth, charles).
parent_child(charles, william).
parent_child(charles, harry).

ancestor_descendant(elizabeth, charles).
ancestor_descendant(charles, william).
ancestor_descendant(charles, harry).

ancestor_descendant(elizabeth, william).
ancestor_descendant(elizabeth, harry).
```

Top-down execution derives the same answers to the query:

```mw
?- ancestor_descendant(X, Y).
```

But then it goes into an infinite loop. However, top-down execution with tabling gives the same answers and terminates without looping.

### Answer set programming

Like Datalog, Answer Set programming (ASP) is not Turing-complete. Moreover, instead of separating goals (or queries) from the program to be used in solving the goals, ASP treats the whole program as a goal, and solves the goal by generating a stable model that makes the goal true. For this purpose, it uses the stable model semantics, according to which a logic program can have zero, one or more intended models. For example, the following program represents a degenerate variant of the map colouring problem of colouring two countries red or green:

```mw
country(oz).
country(iz).
adjacent(oz, iz).
colour(C, red) :- country(C), not(colour(C, green)).
colour(C, green) :- country(C), not(colour(C, red)).
```

The problem has four solutions represented by four stable models:

```mw
country(oz). country(iz). adjacent(oz, iz). colour(oz, red).   colour(iz, red).

country(oz). country(iz). adjacent(oz, iz). colour(oz, green). colour(iz, green).

country(oz). country(iz). adjacent(oz, iz). colour(oz, red).   colour(iz, green).

country(oz). country(iz). adjacent(oz, iz). colour(oz, green). colour(iz, red).
```

To represent the standard version of the map colouring problem, we need to add a constraint that two adjacent countries cannot be coloured the same colour. In ASP, this constraint can be written as a clause of the form:

```mw
:- country(C1), country(C2), adjacent(C1, C2), colour(C1, X), colour(C2, X).
```

With the addition of this constraint, the problem now has only two solutions:

```mw
country(oz). country(iz). adjacent(oz, iz). colour(oz, red).   colour(iz, green).

country(oz). country(iz). adjacent(oz, iz). colour(oz, green). colour(iz, red).
```

The addition of constraints of the form `:- Body.` eliminates models in which `Body` is true.

Confusingly, *constraints in ASP* are different from *constraints in CLP*. Constraints in CLP are predicates that qualify answers to queries (and solutions of goals). Constraints in ASP are clauses that eliminate models that would otherwise satisfy goals. Constraints in ASP are like integrity constraints in databases.

This combination of ordinary logic programming clauses and constraint clauses illustrates the generate-and-test methodology of problem solving in ASP: The ordinary clauses define a search space of possible solutions, and the constraints filter out unwanted solutions.

Most implementations of ASP proceed in two steps: First they instantiate the program in all possible ways, reducing it to a propositional logic program (known as *grounding*). Then they apply a propositional logic problem solver, such as the DPLL algorithm or a Boolean SAT solver. However, some implementations, such as s(CASP) use a goal-directed, top-down, SLD resolution-like procedure without grounding.

### Abductive logic programming

Abductive logic programming (ALP), like CLP, extends normal logic programming by allowing the bodies of clauses to contain literals whose predicates are not defined by clauses. In ALP, these predicates are declared as *abducible* (or *assumable*), and are used as in abductive reasoning to explain observations, or more generally to add new facts to the program (as assumptions) to solve goals.

For example, suppose we are given an initial state in which a red block is on a green block on a table at time 0:

```mw
holds(on(green_block, table), 0).
holds(on(red_block, green_block), 0).
```

Suppose we are also given the goal:

```mw
?- holds(on(green_block,red_block), 3), holds(on(red_block,table), 3).
```

The goal can represent an observation, in which case a solution is an explanation of the observation. Or the goal can represent a desired future state of affairs, in which case a solution is a plan for achieving the goal.

We can use the rules for cause and effect presented earlier to solve the goal, by treating the `happens` predicate as abducible:

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

initiates(move(Object, Place), on(Object, Place)).
terminates(move(Object, Place2), on(Object, Place1)).
```

ALP solves the goal by reasoning backwards and adding assumptions to the program, to solve abducible subgoals. In this case there are many alternative solutions, including:

```mw
happens(move(red_block, table), 0).
happens(tick, 1).
happens(move(green_block, red_block), 2).
```

```mw
happens(tick,0).
happens(move(red_block, table), 1).
happens(move(green_block, red_block), 2).
```

```mw
happens(move(red_block, table), 0).
happens(move(green_block, red_block), 1).
happens(tick, 2).
```

Here `tick` is an event that marks the passage of time without initiating or terminating any fluents.

There are also solutions in which the two `move` events happen at the same time. For example:

```mw
happens(move(red_block, table), 0).
happens(move(green_block, red_block), 0).
happens(tick, 1).
happens(tick, 2).
```

Such solutions, if not desired, can be removed by adding an integrity constraint, which is like a constraint clause in ASP:

```mw
:- happens(move(Block1, Place), Time), happens(move(Block2, Block1), Time).
```

Abductive logic programming has been used for fault diagnosis, planning, natural language processing and machine learning. It has also been used to interpret negation as failure as a form of abductive reasoning.

### Inductive logic programming

Inductive logic programming (ILP) is an approach to machine learning that induces logic programs as hypothetical generalisations of positive and negative examples. Given a logic program representing background knowledge and positive examples together with constraints representing negative examples, an ILP system induces a logic program that generalises the positive examples while excluding the negative examples.

ILP is similar to ALP, in that both can be viewed as generating hypotheses to explain observations, and as employing constraints to exclude undesirable hypotheses. But in ALP the hypotheses are variable-free facts, and in ILP the hypotheses are general rules.

For example, given only background knowledge of the mother_child and father_child relations, and suitable examples of the grandparent_child relation, current ILP systems can generate the definition of grandparent_child, inventing an auxiliary predicate, which can be interpreted as the parent_child relation:

```mw
grandparent_child(X, Y):- auxiliary(X, Z), auxiliary(Z, Y).
auxiliary(X, Y):- mother_child(X, Y).
auxiliary(X, Y):- father_child(X, Y).
```

Stuart Russell has referred to such invention of new concepts as the most important step needed for reaching human-level AI.

Recent work in ILP, combining logic programming, learning and probability, has given rise to the fields of statistical relational learning and probabilistic inductive logic programming.

### Concurrent logic programming

Concurrent logic programming integrates concepts of logic programming with concurrent programming. Its development was given a big impetus in the 1980s by its choice for the systems programming language of the Japanese Fifth Generation Project (FGCS).

A concurrent logic program is a set of guarded Horn clauses of the form:

H :- G

1

, ..., G

n

| B

1

, ..., B

n

.

The conjunction `G1, ... , Gn` is called the guard of the clause, and | is the commitment operator. Declaratively, guarded Horn clauses are read as ordinary logical implications:

H if G

1

and ... and G

n

and B

1

and ... and B

n

.

However, procedurally, when there are several clauses whose heads `H` match a given goal, then all of the clauses are executed in parallel, checking whether their guards `G1, ... , Gn` hold. If the guards of more than one clause hold, then a committed choice is made to one of the clauses, and execution proceeds with the subgoals `B1, ..., Bn` of the chosen clause. These subgoals can also be executed in parallel. Thus concurrent logic programming implements a form of "don't care nondeterminism", rather than "don't know nondeterminism".

For example, the following concurrent logic program defines a predicate `shuffle(Left, Right, Merge)`, which can be used to shuffle two lists `Left` and `Right`, combining them into a single list `Merge` that preserves the ordering of the two lists `Left` and `Right`:

```mw
shuffle([], [], []).
shuffle(Left, Right, Merge) :-
    Left = [First | Rest] |
    Merge = [First | ShortMerge],
    shuffle(Rest, Right, ShortMerge).
shuffle(Left, Right, Merge) :-
    Right = [First | Rest] |
    Merge = [First | ShortMerge],
    shuffle(Left, Rest, ShortMerge).
```

Here, `[]` represents the empty list, and `[Head | Tail]` represents a list with first element `Head` followed by list `Tail`, as in Prolog. (Notice that the first occurrence of | in the second and third clauses is the list constructor, whereas the second occurrence of | is the commitment operator.) The program can be used, for example, to shuffle the lists `[ace, queen, king]` and `[1, 4, 2]` by invoking the goal clause:

```mw
shuffle([ace, queen, king], [1, 4, 2], Merge).
```

The program will non-deterministically generate a single solution, for example `Merge = [ace, queen, 1, king, 4, 2]`.

Carl Hewitt has argued that, because of the indeterminacy of concurrent computation, concurrent logic programming cannot implement general concurrency. However, according to the logical semantics, any result of a computation of a concurrent logic program is a logical consequence of the program, even though not all logical consequences can be derived.

### Concurrent constraint logic programming

Concurrent constraint logic programming combines concurrent logic programming and constraint logic programming, using constraints to control concurrency. A clause can contain a guard, which is a set of constraints that may block the applicability of the clause. When the guards of several clauses are satisfied, concurrent constraint logic programming makes a committed choice to use only one.

### Higher-order logic programming

Several researchers have extended logic programming with higher-order programming features derived from higher-order logic, such as predicate variables. Such languages include the Prolog extensions HiLog and λProlog.

### Linear logic programming

Basing logic programming within linear logic has resulted in the design of logic programming languages that are considerably more expressive than those based on classical logic. Horn clause programs can only represent state change by the change in arguments to predicates. In linear logic programming, one can use the ambient linear logic to support state change. Some early designs of logic programming languages based on linear logic include LO, Lolli, ACL, and Forum. Forum provides a goal-directed interpretation of all linear logic.

### Object-oriented logic programming

F-logic extends logic programming with objects and the frame syntax.

Logtalk extends the Prolog programming language with support for objects, protocols, and other OOP concepts. It supports most standard-compliant Prolog systems as backend compilers.

### Transaction logic programming

Transaction logic is an extension of logic programming with a logical theory of state-modifying updates. It has both a model-theoretic semantics and a procedural one. An implementation of a subset of Transaction logic is available in the Flora-2 system. Other prototypes are also available.
