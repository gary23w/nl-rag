---
title: "Abstract interpretation"
source: https://en.wikipedia.org/wiki/Abstract_interpretation
domain: refinement-types
license: CC-BY-SA-4.0
tags: refinement type, liquid types, predicate subtyping, dependent refinement
fetched: 2026-07-02
---

# Abstract interpretation

In computer science, **abstract interpretation** is a theory of sound approximation of the semantics of computer programs, based on monotonic functions over ordered sets, especially lattices. It can be viewed as a partial execution of a computer program which gains information about its semantics (e.g., control-flow, data-flow) without performing all the calculations.

Its main concrete application is formal static analysis, the automatic extraction of information about the possible executions of computer programs; such analyses have two main usages:

- inside compilers, to analyse programs to decide whether certain optimizations or transformations are applicable;
- for debugging or even the certification of programs against classes of bugs.

Abstract interpretation was formalized by the French computer scientist working couple Patrick Cousot and Radhia Cousot in the late 1970s.

## Intuition

This section illustrates abstract interpretation by means of real-world, non-computing examples.

Consider the people in a conference room. Assume a unique identifier for each person in the room, like a social security number in the United States. To prove that someone is not present, all one needs to do is see if their social security number is not on the list. Since two different people cannot have the same number, it is possible to prove or disprove the presence of a participant simply by looking up their number.

However it is possible that only the names of attendees were registered. If the name of a person is not found in the list, we may safely conclude that that person was not present; but if it is, we cannot conclude definitely without further inquiries, due to the possibility of homonyms (for example, two people named John Smith). Note that this imprecise information will still be adequate for most purposes, because homonyms are rare in practice. However, in all rigor, we cannot say for sure that somebody was present in the room; all we can say is that they were *possibly* here. If the person we are looking up is a criminal, we will issue an *alarm*; but there is of course the possibility of issuing a *false alarm*. Similar phenomena will occur in the analysis of programs.

If we are only interested in some specific information, say, "was there a person of age n in the room?", keeping a list of all names and dates of births is unnecessary. We may safely and without loss of precision restrict ourselves to keeping a list of the participants' ages. If this is already too much to handle, we might keep only the age of the youngest, m and oldest person, M . If the question is about an age strictly lower than m or strictly higher than M , then we may safely respond that no such participant was present. Otherwise, we may only be able to say that we do not know.

In the case of computing, concrete, precise information is in general not computable within finite time and memory (see Rice's theorem and the halting problem). Abstraction is used to allow for generalized answers to questions (for example, answering "maybe" to a yes/no question, meaning "yes or no", when we (an algorithm of abstract interpretation) cannot compute the precise answer with certainty); this simplifies the problems, making them amenable to automatic solutions. One crucial requirement is to add enough vagueness so as to make problems manageable while still retaining enough precision for answering the important questions (such as "might the program crash?").

## Abstract interpretation of computer programs

Given a programming or specification language, abstract interpretation consists of giving several semantics linked by relations of abstraction. A semantics is a mathematical characterization of a possible behavior of the program. The most precise semantics, describing very closely the actual execution of the program, are called the *concrete semantics*. For instance, the concrete semantics of an imperative programming language may associate to each program the set of execution traces it may produce – an execution trace being a sequence of possible consecutive states of the execution of the program; a state typically consists of the value of the program counter and the memory locations (globals, stack and heap). More abstract semantics are then derived; for instance, one may consider only the set of reachable states in the executions (which amounts to considering the last states in finite traces).

The goal of static analysis is to derive a computable semantic interpretation at some point. For instance, one may choose to represent the state of a program manipulating integer variables by forgetting the actual values of the variables and only keeping their signs (+, − or 0). For some elementary operations, such as multiplication, such an abstraction does not lose any precision: to get the sign of a product, it is sufficient to know the sign of the operands. For some other operations, the abstraction may lose precision: for instance, it is impossible to know the sign of a sum whose operands are respectively positive and negative.

Sometimes a loss of precision is necessary to make the semantics decidable (see Rice's theorem and the halting problem). In general, there is a compromise to be made between the precision of the analysis and its decidability (computability), or tractability (computational cost).

In practice the abstractions that are defined are tailored to both the program properties one desires to analyze, and to the set of target programs. The first large scale automated analysis of computer programs with abstract interpretation was motivated by the accident that resulted in the destruction of the first flight of the Ariane 5 rocket in 1996.

## Formalization

Let L be an ordered set, called *concrete set*, and let $L'$ be another ordered set, called *abstract set*. These two sets are related to each other by defining total functions that map elements from one to the other.

A function $\alpha$ is called an *abstraction function* if it maps an element x in the concrete set L to an element $\alpha (x)$ in the abstract set $L'$ . That is, element $\alpha (x)$ in $L'$ is the *abstraction* of x in L .

A function $\gamma$ is called a *concretization function* if it maps an element $x'$ in the abstract set $L'$ to an element $\gamma (x')$ in the concrete set L . That is, element $\gamma (x')$ in L is a *concretization* of $x'$ in $L'$ .

Let $L_{1}$ , $L_{2}$ , $L'_{1}$ , and $L'_{2}$ be ordered sets. The concrete semantics f is a monotonic function from $L_{1}$ to $L_{2}$ . A function $f'$ from $L'_{1}$ to $L'_{2}$ is said to be a *valid abstraction* of f if, for all $x'$ in $L'_{1}$ , we have $(f\circ \gamma )(x')\leq (\gamma \circ f')(x')$ .

Program semantics are generally described using fixed points in the presence of loops or recursive procedures. Suppose that L is a complete lattice and let f be a monotonic function from L into L . Then, any $x'$ such that $f(x')\leq x'$ is an abstraction of the least fixed-point of f , which exists, according to the Knaster–Tarski theorem.

The difficulty is now to obtain such an $x'$ . If $L'$ is of finite height, or at least verifies the ascending chain condition (all ascending sequences are ultimately stationary), then such an $x'$ may be obtained as the stationary limit of the ascending sequence $x'_{n}$ defined by induction as follows: $x'_{0}=\bot$ (the least element of $L'$ ) and $x'_{n+1}=f'(x'_{n})$ .

In other cases, it is still possible to obtain such an $x'$ through a (pair-)widening operator, defined as a binary operator $\nabla \colon L\times L\to L$ which satisfies the following conditions:

1. For all x and y , we have $x\leq x\mathbin {\nabla } y$ and $y\leq x\mathbin {\nabla } y$ , and
2. For any ascending sequence $(y'_{n})_{n\geq 0}$ , the sequence defined by $x'_{0}:=\bot$ and $x'_{n+1}:=x'_{n}\mathbin {\nabla } y'_{n}$ is ultimately stationary. We can then take $y'_{n}=f'(x'_{n})$ .

In some cases, it is possible to define abstractions using Galois connections $(\alpha ,\gamma )$ where $\alpha$ is from L to $L'$ and $\gamma$ is from $L'$ to L . This supposes the existence of best abstractions, which is not necessarily the case. For instance, if we abstract sets of couples $(x,y)$ of real numbers by enclosing convex polyhedra, there is no optimal abstraction to the disc defined by $x^{2}+y^{2}\leq 1$ .

## Examples of abstract domains

### Numerical abstract domains

One can assign to each variable x available at a given program point an interval $[L_{x},H_{x}]$ . A state assigning the value $v(x)$ to variable x will be a concretization of these intervals if, for all x , we have $v(x)\in [L_{x},H_{x}]$ . From the intervals $[L_{x},H_{x}]$ and $[L_{y},H_{y}]$ for variables x and y , respectively, one can easily obtain intervals for $x+y$ (namely, $[L_{x}+L_{y},H_{x}+H_{y}]$ ) and for $x-y$ (namely, $[L_{x}-H_{y},H_{x}-L_{y}]$ ); note that these are *exact* abstractions, since the set of possible outcomes for, say, $x+y$ , is precisely the interval $[L_{x}+L_{y},H_{x}+H_{y}]$ . More complex formulas can be derived for multiplication, division, etc., yielding so-called interval arithmetics.

Let us now consider the following very simple program:

```
y = x;
z = x - y;
```

|   |
|---|

|   |
|---|

With reasonable arithmetic types, the result for z should be zero. But if we do interval arithmetic starting from x in [0, 1], one gets z in [−1, +1]. While each of the operations taken individually was exactly abstracted, their composition isn't.

The problem is evident: we did not keep track of the equality relationship between x and y; actually, this domain of intervals does not take into account any relationships between variables, and is thus a *non-relational domain*. Non-relational domains tend to be fast and simple to implement, but imprecise.

Some examples of *relational* numerical abstract domains are:

- congruence relations on integers
- convex polyhedra (cf. left picture) – with some high computational costs
- difference-bound matrices
- "octagons"
- linear equalities

and combinations thereof (such as the reduced product, cf. right picture).

When one chooses an abstract domain, one typically has to strike a balance between keeping fine-grained relationships, and high computational costs.

### Machine word abstract domains

While high-level languages such as Python or Haskell use unbounded integers by default, lower-level programming languages such as C or assembly language typically operate on finitely-sized machine words, which are more suitably modeled using the integers modulo ${\textstyle 2^{n}}$ (where *n* is the bit width of a machine word). There are several abstract domains suitable for various analyses of such variables.

The *bitfield domain* treats each bit in a machine word separately, i.e., a word of width *n* is treated as an array of *n* abstract values. The abstract values are taken from the set ${\textstyle \{0,1,\bot \}}$ , and the abstraction and concretization functions are given by: $\gamma (0)=\{0\}$ , $\gamma (1)=\{1\}$ , $\gamma (\bot )=\{0,1\}$ , $\alpha (\{0\})=0$ , $\alpha (\{1\})=1$ , $\alpha (\{0,1\})=\bot$ , $\alpha (\{\})=\bot$ . Bitwise operations on these abstract values are identical with the corresponding logical operations in some three-valued logics:

|   |   |   |
|---|---|---|
| NOT(A) A ¬A 0 1 ⊥ ⊥ 1 0 | AND(A, B) A ∧ B B 0 ⊥ 1 A 0 0 0 0 ⊥ 0 ⊥ ⊥ 1 0 ⊥ 1 | OR(A, B) A ∨ B B 0 ⊥ 1 A 0 0 ⊥ 1 ⊥ ⊥ ⊥ 1 1 1 1 1 |

Further domains include the *signed interval domain* and the *unsigned interval domain*. All three of these domains support forwards and backwards abstract operators for common operations such as addition, shifts, xor, and multiplication. These domains can be combined using the reduced product.
