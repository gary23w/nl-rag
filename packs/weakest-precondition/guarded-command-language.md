---
title: "Guarded Command Language"
source: https://en.wikipedia.org/wiki/Guarded_Command_Language
domain: weakest-precondition
license: CC-BY-SA-4.0
tags: weakest precondition, predicate transformer semantics, guarded command language, verification condition
fetched: 2026-07-02
---

# Guarded Command Language

The **Guarded Command Language** (**GCL**) is a programming language defined by Edsger Dijkstra for predicate transformer semantics in EWD472. It combines programming concepts in a compact way. It makes it easier to develop a program and its proof hand-in-hand, with the proof ideas leading the way; moreover, parts of a program can actually be *calculated*.

An important property of **GCL** is nondeterminism. For example, in the if-statement, several alternatives may be true, and the choice is made at runtime, when the if-statement is executed. This frees the programmer from having to make unnecessary choices and is an aid in the formal development of programs.

**GCL** includes the multiple assignment statement. For example, execution of the statement `x, y:= y, x` is done by first evaluating the righthand side values and then storing them in the lefthand variables. Thus, this statement swaps the values of x and y.

The following books discuss the development of programs using **GCL**:

- *Dijkstra, Edsger W. (1976). *A Discipline of Programming*. Prentice Hall. ISBN 978-0132158718.*
- *Gries, D. (1981). *The Science of Programming*. Monographs in Computer Science (in English, Spanish, Japanese, Chinese, Italian, and Russian). New York: Springer Verlag. doi:10.1007/978-1-4612-5983-1. ISBN 978-0-387-96480-5. S2CID 37034126.*
- *Dijkstra, Edsger W.; Feijen, Wim H.J. (1988). *A Method of Programming*. Boston, MA: Addison-Wesley Longman Publishing Co., Inc. p. 200. ISBN 978-0-201-17536-3.*
- *Kaldewaij, Anne (1990). *Programming: the derivation of algorithms*. Prentice-Hall, Inc. ISBN 0132041081.*
- *Cohen, Edward (1990). David Gries (ed.). *Programming in the 1990s: An introduction to the calculation of programs*. Texts and Monographs in Computer Science. Springer Verlag. doi:10.1007/978-1-4613-9706-9. ISBN 978-1-4613-9706-9. S2CID 1509875.*

## Guarded command

A guarded command consists of a boolean condition or guard, and a statement "guarded" by it. The statement is only executed if the guard is true, so when reasoning about the statement, the condition can be assumed true. This makes it easier to prove the program meets a specification.

### Syntax

A guarded command is a statement of the form G → S, where

- G is a proposition, called the guard
- S is a statement

### Semantics

- If G evaluates to true, S is eligible to be executed. In most GCL constructs, multiple guarded commands may have guards that are true, and exactly one of them is chosen *arbitrarily* to be executed.
- If G is false, S will not be executed.

**skip** and **abort** are important statements in the guarded command language. **abort** is the undefined instruction: do anything. It does not even need to terminate. It is used to describe the program when formulating a proof, in which case the proof usually fails. **skip** is the empty instruction: do nothing. It is often used when the syntax requires a statement but the state should not change.

### Syntax

```
skip
```

```
abort
```

### Semantics

- **skip**: do nothing
- **abort**: do anything

## Assignment

Assigns values to variables.

### Syntax

```
v := E
```

or

```
v0, v1, ..., vn := E0, E1, ..., En
```

where

- v are program variables
- E are expressions of the same data type as their corresponding variables

## Catenation

Statements are separated by one semicolon (;)

## Selection: if

The selection (often called the "conditional statement" or "if statement") is a list of guarded commands, of which one is chosen to execute. If more than one guard is true, one statement whose guard is true is arbitrarily chosen to be executed. If no guard is true, the result is undefined, that is, equivalent to **abort**. Because at least one of the guards must be true, the empty statement **skip** is often needed. The statement **if fi** has no guarded commands, so there is never a true guard. Hence, **if fi** is equivalent to **abort**.

### Syntax

```
if G0 → S0
 □ G1 → S1
...
 □ Gn → Sn
fi
```

### Semantics

Upon execution of a selection, the guards are evaluated. If none of the guards is *true*, then the selection aborts, otherwise one of the clauses with a *true* guard is chosen arbitrarily and its statement is executed.

### Implementation

GCL does not specify an implementation. Since guards cannot have side effects and the choice of clause is arbitrary, an implementation may evaluate the guards in any sequence and choose the first *true* clause, for example.

### Examples

#### Simple

In pseudocode:

```
if a < b then set c to True
else set c to False
```

In guarded command language:

```
if a < b → c := true
 □ a ≥ b → c := false
fi
```

In pseudocode:

```
if error is True then set x to 0
```

In guarded command language:

```
if error → x := 0
 □ 
  
    
      
        ¬
      
    
    {\displaystyle \neg }
  
error → skip
fi
```

If the second guard is omitted and error is False, the result is abort.

#### More guards true

```
if a ≥ b → max := a
 □ b ≥ a → max := b
fi
```

If a = b, either a or b is chosen as the new value for the maximum, with equal results. However, the implementation may find that one is easier or faster than the other. Since there is no difference to the programmer, any implementation will do.

## Repetition: *do*

Execution of this repetition, or loop, is shown below.

### Syntax

```
do G0 → S0
 □ G1 → S1
...
 □ Gn → Sn
od
```

### Semantics

Execution of the repetition consists of executing 0 or more *iterations*, where an iteration consists of arbitrarily choosing a guarded command Gi → Si whose guard Gi is true and executing the command Si. Thus, if all guards are initially false, the repetition terminates immediately, without executing an iteration. Execution of the repetition **do od**, which has no guarded commands, executes 0 iterations, so **do od** is equivalent to **skip**.

### Examples

#### Original Euclidean algorithm

```
a, b := A, B;
do a < b → b := b - a
 □ b < a → a := a - b
od
```

This repetition ends when a = b, in which case a and b hold the greatest common divisor of A and B.

Dijkstra sees in this algorithm a way of synchronizing two infinite cycles `a := a - b` and `b := b - a` in such a way that `a≥0` and `b≥0` remains true.

#### Extended Euclidean algorithm

```
a, b, x, y, u, v := A, B, 1, 0, 0, 1;
do b ≠ 0 →
   q, r := a div b, a mod b;
   a, b, x, y, u, v := b, r, u, v, x - q*u, y - q*v
od
```

This repetition ends when b = 0, in which case the variables hold the solution to Bézout's identity: xA + yB = gcd(A,B) .

#### Non-deterministic sort

```
do a>b → a, b := b, a
 □ b>c → b, c := c, b
 □ c>d → c, d := d, c
od
```

The program keeps on permuting elements while one of them is greater than its successor. This non-deterministic bubble sort is not more efficient than its deterministic version, but easier to prove: it will not stop while the elements are not sorted and that each step it sorts at least 2 elements.

#### Arg max

```
x, y = 1, 1;
do x≠n →
   if f(x) ≤ f(y) → x := x+1
    □ f(x) ≥ f(y) → y := x; x := x+1
   fi
od
```

This algorithm finds the value 1 ≤ *y* ≤ *n* for which a given integer function *f* is maximal. Not only the computation but also the final state is not necessarily uniquely determined.

## Applications

### Programs correct by construction

Generalizing the observational congruence of Guarded Commands into a lattice has led to Refinement Calculus. This has been mechanized in Formal Methods like B-Method that allow one to formally derive programs from their specifications.

### Asynchronous circuits

Guarded commands are suitable for quasi-delay-insensitive circuit design because the repetition allows arbitrary relative delays for the selection of different commands. In this application, a logic gate driving a node *y* in the circuit consists of two guarded commands, as follows:

```
PullDownGuard → y := 0
PullUpGuard → y := 1
```

*PullDownGuard* and *PullUpGuard* here are functions of the logic gate's inputs, which describe when the gate pulls the output down or up, respectively. Unlike classical circuit evaluation models, the repetition for a set of guarded commands (corresponding to an asynchronous circuit) can accurately describe all possible dynamic behaviors of that circuit. Depending on the model one is willing to live with for the electrical circuit elements, additional restrictions on the guarded commands may be necessary for a guarded-command description to be entirely satisfactory. Common restrictions include stability, non-interference, and absence of self-invalidating commands.

### Model checking

Guarded commands are used within the Promela programming language, which is used by the SPIN model checker. SPIN verifies correct operation of concurrent software applications.

### Other

The Perl module Commands::Guarded implements a deterministic, rectifying variant on Dijkstra's guarded commands.
