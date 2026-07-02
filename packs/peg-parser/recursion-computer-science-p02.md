---
title: "Recursion (computer science) (part 2/2)"
source: https://en.wikipedia.org/wiki/Recursion_(computer_science)
domain: peg-parser
license: CC-BY-SA-4.0
tags: parsing expression grammar, peg parser, packrat parsing, top-down parsing
fetched: 2026-07-02
part: 2/2
---

## Recursion in Logic Programming

In the procedural interpretation of logic programs, clauses (or rules) of the form `A :- B` are treated as procedures, which reduce goals of the form `A` to subgoals of the form `B`. For example, the Prolog clauses:

```mw
path(X,Y) :- arc(X,Y).
path(X,Y) :- arc(X,Z), path(Z,Y).
```

define a procedure, which can be used to search for a path from *X* to *Y*, either by finding a direct arc from *X* to *Y*, or by finding an arc from *X* to *Z*, and then searching recursively for a path from *Z* to *Y*. Prolog executes the procedure by reasoning top-down (or backwards) and searching the space of possible paths depth-first, one branch at a time. If it tries the second clause, and finitely fails to find a path from *Z* to *Y*, it backtracks and tries to find an arc from *X* to another node, and then searches for a path from that other node to *Y*.

However, in the logical reading of logic programs, clauses are understood declaratively as universally quantified conditionals. For example, the recursive clause of the path-finding procedure is understood as representing the knowledge that, for every *X*, *Y* and *Z*, if there is an arc from *X* to *Z* and a path from *Z* to *Y* then there is a path from *X* to *Y*. In symbolic form:

$\forall X,Y,Z(arc(X,Z)\land path(Z,Y)\rightarrow path(X,Y)).$

The logical reading frees the reader from needing to know how the clause is used to solve problems. The clause can be used top-down, as in Prolog, to reduce problems to subproblems. Or it can be used bottom-up (or forwards), as in Datalog, to derive conclusions from conditions. This separation of concerns is a form of abstraction, which separates declarative knowledge from problem solving methods (see Algorithm#Algorithm = Logic + Control).


## Infinite recursion

A common mistake among programmers is not providing a way to exit a recursive function, often by omitting or incorrectly checking the base case, letting it run (at least theoretically) infinitely by endlessly calling itself recursively. This is called *infinite recursion*, and the program will never terminate. In practice, this typically exhausts the available stack space. In most programming environments, a program with infinite recursion will not really run forever. Eventually, something will break and the program will report an error. However, if tail call optimization is used then the recursive calls may be optimized into an infinite loop that can run forever.

Below is a Java code that would use infinite recursion:

```mw
public class InfiniteRecursion {
    static void recursive() {
        // Recursive function with no way out
        recursive();
    }
    
    public static void main(String[] args) {
        recursive(); // Executes the recursive function upon runtime
    }
}
```

Running this code will result in a stack overflow error.
