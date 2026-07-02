---
title: "Recursion (computer science) (part 2/2)"
source: https://en.wikipedia.org/wiki/Recursion_(computer_science)
domain: algorithms
license: CC-BY-SA-4.0
tags: algorithm, sorting, complexity, big-o, dynamic programming
fetched: 2026-07-02
part: 2/2
---

## Time-efficiency of recursive algorithms

The time efficiency of recursive algorithms can be expressed in a recurrence relation of Big O notation. They can (usually) then be simplified into a single Big-O term.

### Shortcut rule (master theorem)

If the time-complexity of the function is in the form T ( n ) = a ⋅ T ( n / b ) + f ( n ) {\displaystyle T(n)=a\cdot T(n/b)+f(n)} ({\displaystyle T(n)=a\cdot T(n/b)+f(n)})

Then the Big O of the time-complexity is thus:

- If f ( n ) = O ( n log b ⁡ a − ε ) {\displaystyle f(n)=O(n^{\log _{b}a-\varepsilon })} ({\displaystyle f(n)=O(n^{\log _{b}a-\varepsilon })}) for some constant ε > 0 {\displaystyle \varepsilon >0} ({\displaystyle \varepsilon >0}), then T ( n ) = Θ ( n log b ⁡ a ) {\displaystyle T(n)=\Theta (n^{\log _{b}a})} ({\displaystyle T(n)=\Theta (n^{\log _{b}a})})
- If f ( n ) = Θ ( n log b ⁡ a ) {\displaystyle f(n)=\Theta (n^{\log _{b}a})} ({\displaystyle f(n)=\Theta (n^{\log _{b}a})}), then T ( n ) = Θ ( n log b ⁡ a log ⁡ n ) {\displaystyle T(n)=\Theta (n^{\log _{b}a}\log n)} ({\displaystyle T(n)=\Theta (n^{\log _{b}a}\log n)})
- If f ( n ) = Ω ( n log b ⁡ a + ε ) {\displaystyle f(n)=\Omega (n^{\log _{b}a+\varepsilon })} ({\displaystyle f(n)=\Omega (n^{\log _{b}a+\varepsilon })}) for some constant ε > 0 {\displaystyle \varepsilon >0} ({\displaystyle \varepsilon >0}), and if a ⋅ f ( n / b ) ≤ c ⋅ f ( n ) {\displaystyle a\cdot f(n/b)\leq c\cdot f(n)} ({\displaystyle a\cdot f(n/b)\leq c\cdot f(n)}) for some constant *c* < 1 and all sufficiently large n, then T ( n ) = Θ ( f ( n ) ) {\displaystyle T(n)=\Theta (f(n))} ({\displaystyle T(n)=\Theta (f(n))})

where a represents the number of recursive calls at each level of recursion, b represents by what factor smaller the input is for the next level of recursion (i.e. the number of pieces you divide the problem into), and *f*(*n*) represents the work that the function does independently of any recursion (e.g. partitioning, recombining) at each level of recursion.


## Recursion in Logic Programming

In the procedural interpretation of logic programs, clauses (or rules) of the form `A :- B` are treated as procedures, which reduce goals of the form `A` to subgoals of the form `B`. For example, the Prolog clauses:

```mw
path(X,Y) :- arc(X,Y).
path(X,Y) :- arc(X,Z), path(Z,Y).
```

define a procedure, which can be used to search for a path from *X* to *Y*, either by finding a direct arc from *X* to *Y*, or by finding an arc from *X* to *Z*, and then searching recursively for a path from *Z* to *Y*. Prolog executes the procedure by reasoning top-down (or backwards) and searching the space of possible paths depth-first, one branch at a time. If it tries the second clause, and finitely fails to find a path from *Z* to *Y*, it backtracks and tries to find an arc from *X* to another node, and then searches for a path from that other node to *Y*.

However, in the logical reading of logic programs, clauses are understood declaratively as universally quantified conditionals. For example, the recursive clause of the path-finding procedure is understood as representing the knowledge that, for every *X*, *Y* and *Z*, if there is an arc from *X* to *Z* and a path from *Z* to *Y* then there is a path from *X* to *Y*. In symbolic form:

∀

X

,

Y

,

Z

(

a

r

c

(

X

,

Z

)

∧

p

a

t

h

(

Z

,

Y

)

→

p

a

t

h

(

X

,

Y

)

)

.

{\displaystyle \forall X,Y,Z(arc(X,Z)\land path(Z,Y)\rightarrow path(X,Y)).}

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
