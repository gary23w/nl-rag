---
title: "Use-define chain"
source: https://en.wikipedia.org/wiki/Def-use_chain
domain: data-flow-analysis
license: CC-BY-SA-4.0
tags: data-flow analysis, reaching definition, live variable analysis, available expression
fetched: 2026-07-02
---

# Use-define chain

(Redirected from

Def-use chain

)

Within computer science, a **use-definition chain** (or **UD chain**) is a data structure that consists of a use *U*, of a variable, and all the definitions *D* of that variable that can reach that use without any other intervening definitions. A UD Chain generally means the assignment of some value to a variable.

A counterpart of a *UD Chain* is a **definition-use chain** (or **DU chain**), which consists of a definition *D* of a variable and all the uses *U* reachable from that definition without any other intervening definitions.

Both UD and DU chains are created by using a form of static code analysis known as data flow analysis. Knowing the use-def and def-use chains for a program or subprogram is a prerequisite for many compiler optimizations, including constant propagation and common subexpression elimination.

## Purpose

Making the use-define or define-use chains is a step in liveness analysis, so that logical representations of all the variables can be identified and tracked through the code.

Consider the following snippet of code:

```mw
 int x = 0;    /* A */
 x = x + y;    /* B */
 /* 1, some uses of x */
 x = 35;       /* C */
 /* 2, some more uses of x */
```

Notice that `x` is assigned a value at three points (marked A, B, and C). However, at the point marked "1", the use-def chain for `x` should indicate that its current value must have come from line B (and its value at line B must have come from line A). Contrariwise, at the point marked "2", the use-def chain for `x` indicates that its current value must have come from line C. Since the value of the `x` in block 2 does not depend on any definitions in block 1 or earlier, `x` might as well be a different variable there; practically speaking, it *is* a different variable — call it `x2`.

```mw
 int x = 0;    /* A */
 x = x + y;    /* B */
 /* 1, some uses of x */
 int x2 = 35;  /* C */
 /* 2, some uses of x2 */
```

The process of splitting `x` into two separate variables is called live range splitting. See also static single assignment form.

## Setup

The list of statements determines a strong order among statements.

- Statements are labeled using the following conventions: ⁠ $s(i)$ ⁠, where *i* is an integer in ⁠ $[1,n]$ ⁠; and *n* is the number of statements in the basic block
- Variables are identified in italic (e.g., *v*,*u* and *t*)
- Every variable is assumed to have a definition in the context or scope. (In static single assignment form, use-define chains are explicit because each chain contains a single element.)

For a variable, such as *v*, its declaration is identified as *V* (italic capital letter), and for short, its declaration is identified as ⁠ $s(0)$ ⁠. In general, a declaration of a variable can be in an outer scope (e.g., a global variable).

### Definition of a variable

When a variable, *v*, is on the LHS of an assignment statement, such as ⁠ $s(j)$ ⁠, then ⁠ $s(j)$ ⁠ is a definition of *v*. Every variable (*v*) has at least one definition by its declaration (*V*) (or initialization).

### Use of a variable

If variable, *v*, is on the RHS of statement ⁠ $s(j)$ ⁠, there is a statement, ⁠ $s(i)$ ⁠ with *i* < *j* and ⁠ $\min(j-i)$ ⁠, that it is a definition of *v* and it has a use at ⁠ $s(j)$ ⁠ (or, in short, when a variable, *v*, is on the RHS of a statement ⁠ $s(j)$ ⁠, then *v* has a use at statement ⁠ $s(j)$ ⁠).

## Execution

Consider the sequential execution of the list of statements, ⁠ $s(i)$ ⁠, and what can now be observed as the computation at statement, *j*:

- A definition at statement ⁠ $s(i)$ ⁠ with *i* < *j* is **alive** at *j*, if it has a use at a statement ⁠ $s(k)$ ⁠ with *k* ≥ *j*. The set of alive definitions at statement *i* is denoted as ⁠ $A(i)$ ⁠ and the number of alive definitions as $|A(i)|$ . (⁠ $A(i)$ ⁠ is a simple but powerful concept: theoretical and practical results in space complexity theory, access complexity(I/O complexity), register allocation and cache locality exploitation are based on ⁠ $A(i)$ ⁠.)
- A definition at statement ⁠ $s(i)$ ⁠ **kills** all previous definitions (⁠ $s(k)$ ⁠ with *k* < *i*) for the same variables.

## Execution example for def-use-chain

This example is based on a Java algorithm for finding the gcd. (It is not important to understand what this function does.)

```mw
/**
 * @param(a, b) The values used to calculate the divisor.
 * @return The greatest common divisor of a and b.
 */
int gcd(int a, int b) { 
    int c = a;
    int d = b; 
    if (c == 0)
        return d;
    while (d != 0) { 
        if (c > d)
            c = c - d;
        else
            d = d - c;
    } 
    return c; 
}
```

To find out all def-use-chains for variable d, do the following steps:

1. Search for the first time the variable is defined (write access). In this case it is "`d=b`" (l.7)
2. Search for the first time the variable is read. In this case it is "`return d`"
3. Write down this information in the following style: [name of the variable you are creating a def-use-chain for, the concrete write access, the concrete read access] In this case it is: `[d, d=b, return d]`

Repeat these steps in the following style: combine each write access with each read access (but NOT the other way round).

The result should be:

```mw
 [d, d=b, return d] 
 [d, d=b, while(d!=0)] 
 [d, d=b, if(c>d)] 
 [d, d=b, c=c-d] 
 [d, d=b, d=d-c]
 [d, d=d-c, while(d!=0)] 
 [d, d=d-c, if(c>d)] 
 [d, d=d-c, c=c-d] 
 [d, d=d-c, d=d-c]
```

You have to take care, if the variable is changed by the time.

For example: From line 7 down to line 13 in the source code, d is not redefined / changed. At line 14, d could be redefined. This is why you have to recombine this write access on d with all possible read accesses which could be reached. In this case, only the code beyond line 10 is relevant. Line 7, for example, cannot be reached again. For your understanding, you can imagine 2 different variables d:

```mw
 [d1, d1=b, return d1] 
 [d1, d1=b, while(d1!=0)] 
 [d1, d1=b, if(c>d1)] 
 [d1, d1=b, c=c-d1] 
 [d1, d1=b, d1=d1-c]
 [d2, d2=d2-c, while(d2!=0)] 
 [d2, d2=d2-c, if(c>d2)] 
 [d2, d2=d2-c, c=c-d2] 
 [d2, d2=d2-c, d2=d2-c]
```

As a result, you could get something like this. The variable d1 would be replaced by b

```mw
/**
 * @param(a, b) The values used to calculate the divisor.
 * @return The greatest common divisor of a and b.
 **/
int gcd(int a, int b) {
    int c = a;
    int d; 
    if (c == 0)
        return b;
    if (b != 0) {
        if (c > b) {
            c = c - b;
            d = b;
        }
        else
            d = b - c;
        while (d != 0) { 
            if (c > d)
                c = c - d;
            else
                d = d - c;
        }
    } 
    return c; 
}
```

## Method of building a *use-def* (or *ud*) chain

1. Set definitions in statement ⁠ $s(0)$ ⁠
2. For each i in ⁠ $[1,n]$ ⁠, find live definitions that have use in statement ⁠ $s(i)$ ⁠
3. Make a link among definitions and uses
4. Set the statement ⁠ $s(i)$ ⁠, as definition statement
5. Kill previous definitions

With this algorithm, two things are accomplished:

1. A directed acyclic graph (DAG) is created on the variable uses and definitions. The DAG specifies a data dependency among assignment statements, as well as a partial order (therefore parallelism among statements).
2. When statement ⁠ $s(i)$ ⁠ is reached, there is a list of *live* variable assignments. If only one assignment is live, for example, constant propagation might be used.
