---
title: "Loop invariant"
source: https://en.wikipedia.org/wiki/Loop_invariant
domain: axiomatic-semantics
license: CC-BY-SA-4.0
tags: axiomatic semantics, predicate transformer semantics, assertion language, program correctness
fetched: 2026-07-02
---

# Loop invariant

In computer science, a **loop invariant** is a property of a program loop that is true before (and after) each iteration. It is a logical assertion, sometimes checked with a code assertion. Knowing its invariant(s) is essential in understanding the effect of a loop.

In formal program verification, particularly the Floyd-Hoare approach, loop invariants are expressed by formal predicate logic and used to prove properties of loops and by extension algorithms that employ loops (usually correctness properties). The loop invariants will be true on entry into a loop and following each iteration, so that on exit from the loop, both the loop invariants and the loop termination condition can be guaranteed.

From a programming methodology viewpoint, the loop invariant can be viewed as a more abstract specification of the loop, which characterizes the deeper purpose of the loop beyond the details of this implementation. A survey article covers fundamental algorithms from many areas of computer science (searching, sorting, optimization, arithmetic etc.), characterizing each of them from the viewpoint of its invariant.

Because of the similarity of loops and recursive programs, proving partial correctness of loops with invariants is very similar to proving the correctness of recursive programs via induction. In fact, the loop invariant is often the same as the inductive hypothesis to be proved for a recursive program equivalent to a given loop.

## Informal example

The following C subroutine `max()` returns the maximum value in its argument array `a[]`, provided its length `n` is at least 1. Comments are provided at lines 3, 6, 9, 11, and 13. Each comment makes an assertion about the values of one or more variables at that stage of the function. The highlighted assertions within the loop body, at the beginning and end of the loop (lines 6 and 11), are exactly the same. They thus describe an invariant property of the loop. When line 13 is reached, this invariant still holds, and it is known that the loop condition `i!=n` from line 5 has become false. Both properties together imply that `m` equals the maximum value in `a[0...n-1]`, that is, that the correct value is returned from line 14.

```mw
int max(int n, const int a[]) {
    int m = a[0];
    // m equals the maximum value in a[0...0]
    int i = 1;
    while (i != n) {
        // m equals the maximum value in a[0...i-1]
        if (m < a[i])
            m = a[i];
        // m equals the maximum value in a[0...i]
        ++i;
        // m equals the maximum value in a[0...i-1]
    }
    // m equals the maximum value in a[0...i-1], and i==n
    return m;
}
```

Following a defensive programming paradigm, the loop condition `i!=n` in line 5 should better be modified to `i<n`, in order to avoid endless looping for illegitimate negative values of `n`. While this change in code intuitively shouldn't make a difference, the reasoning leading to its correctness becomes somewhat more complicated, since then only `i>=n` is known in line 13. In order to obtain that also `i<=n` holds, that condition has to be included in the loop invariant. It is easy to see that `i<=n`, too, is an invariant of the loop, since `i<n` in line 6 can be obtained from the (modified) loop condition in line 5, and hence `i<=n` holds in line 11 after `i` has been incremented in line 10. However, when loop invariants have to be manually provided for formal program verification, such intuitively too obvious properties like `i<=n` are often overlooked.

## Floyd–Hoare logic

In Floyd–Hoare logic, the partial correctness of a while loop is governed by the following rule of inference:

${\frac {\{C\land I\}\;\mathrm {body} \;\{I\}}{\{I\}\;{\mathtt {while}}\ (C)\ \mathrm {body} \;\{\lnot C\land I\}}}$

This means:

- If some property I is preserved by the code $\mathrm {body}$ —more precisely, if I holds after the execution of $\mathrm {body}$ whenever both C and I held beforehand— *(upper line)* then
- C and I are guaranteed to be false and true, respectively, after the execution of the whole loop ${\mathtt {while}}\ (C)\ \mathrm {body}$ , provided I was true before the loop *(lower line)*.

In other words: The rule above is a deductive step that has as its premise the Hoare triple $\{C\land I\}\;\mathrm {body} \;\{I\}$ . This triple is actually a relation on machine states. It holds whenever starting from a state in which the boolean expression $C\land I$ is true and successfully executing some code called $\mathrm {body}$ , the machine ends up in a state in which I is true. If this relation can be proven, the rule then allows us to conclude that successful execution of the program ${\mathtt {while}}\ (C)\ \mathrm {body}$ will lead from a state in which I is true to a state in which $\lnot C\land I$ holds. The Boolean formula I in this rule is called a loop invariant.

With some variations in the notation used, and with the premise that the loop halts, this rule is also known as the **Invariant Relation Theorem**. As one 1970s textbook presents it in a way meant to be accessible to student programmers:

Let the notation `P { seq } Q` mean that if `P` is true before the sequence of statements `seq` runs, then `Q` is true after it. Then the invariant relation theorem holds that

P & c { seq } P

implies

P { DO WHILE (c); seq END; } P & ¬c

### Example

The following example illustrates how this rule works. Consider the program:

```
while (x < 10)
    x := x+1;
```

One can then prove the following Hoare triple:

$\{x\leq 10\}\;{\mathtt {while}}\ (x<10)\ x:=x+1\;\{x=10\}$

The condition *C* of the `while` loop is $x<10$ . A useful loop invariant I has to be guessed; it will turn out that $x\leq 10$ is appropriate. Under these assumptions, it is possible to prove the following Hoare triple:

$\{x<10\land x\leq 10\}\;x:=x+1\;\{x\leq 10\}$

While this triple can be derived formally from the rules of Floyd-Hoare logic governing assignment, it is also intuitively justified: Computation starts in a state where $x<10\land x\leq 10$ is true, which means simply that $x<10$ is true. The computation adds 1 to x, which means that $x\leq 10$ is still true (for integer x).

Under this premise, the rule for `while` loops permits the following conclusion:

$\{x\leq 10\}\;{\mathtt {while}}\ (x<10)\ x:=x+1\;\{\lnot (x<10)\land x\leq 10\}$

However, the post-condition $\lnot (x<10)\land x\leq 10$ (x is less than or equal to 10, but it is not less than 10) is logically equivalent to $x=10$ , which is what we wanted to show.

The property $0\leq x$ is another invariant of the example loop, and the trivial property $\mathrm {true}$ is another one. Applying the above inference rule to the former invariant yields $\{0\leq x\}\;{\mathtt {while}}\ (x<10)\ x:=x+1\;\{10\leq x\}$ . Applying it to invariant $\mathrm {true}$ yields $\{\mathrm {true} \}\;{\mathtt {while}}\ (x<10)\ x:=x+1\;\{10\leq x\}$ , which is slightly more expressive.

## Programming language support

### Eiffel

The Eiffel programming language provides native support for loop invariants. A loop invariant is expressed with the same syntax used for a class invariant. In the sample below, the loop invariant expression `x <= 10` must be true following the loop initialization, and after each execution of the loop body; this is checked at runtime.

```mw
    from
        x := 0
    invariant
        x <= 10
    until
        x > 10
    loop
        x := x + 1
    end
```

### Whiley

The Whiley programming language also provides first-class support for loop invariants. Loop invariants are expressed using one or more `where` clauses, as the following illustrates:

```mw
function max(int[] items) -> (int r)
// Requires at least one element to compute max
requires |items| > 0
// (1) Result is not smaller than any element
ensures all { i in 0..|items| | items[i] <= r }
// (2) Result matches at least one element
ensures some { i in 0..|items| | items[i] == r }:
    //
    nat i = 1
    int m = items[0]
    //
    while i < |items|
    // (1) No item seen so far is larger than m
    where all { k in 0..i | items[k] <= m }
    // (2) One or more items seen so far matches m
    where some { k in 0..i | items[k] == m }:
        if items[i] > m:
            m = items[i]
        i = i + 1
    //
    return m
```

The `max()` function determines the largest element in an integer array. For this to be defined, the array must contain at least one element. The postconditions of `max()` require that the returned value is: (1) not smaller than any element; and, (2) that it matches at least one element. The loop invariant is defined inductively through two `where` clauses, each of which corresponds to a clause in the postcondition. The fundamental difference is that each clause of the loop invariant identifies the result as being correct up to the current element `i`, whilst the postconditions identify the result as being correct for all elements.

## Use of loop invariants

A loop invariant can serve one of the following purposes:

1. purely documentary
2. to be checked within the code, e.g., by an assertion call
3. to be verified based on the Floyd–Hoare approach

For 1., a natural language comment (like `// m equals the maximum value in a[0...i-1]` in the above example) is sufficient.

For 2., programming language support is required, such as the C library assert.h, or the above-shown `invariant` clause in Eiffel. Often, run-time checking can be switched on (for debugging runs) and off (for production runs) by a compiler or a runtime option.

For 3., some tools exist to support mathematical proofs, usually based on the above-shown Floyd–Hoare rule, that a given loop code in fact satisfies a given (set of) loop invariant(s).

The technique of abstract interpretation can be used to detect loop invariants of given code automatically. However, this approach is limited to very simple invariants (such as `0<=i && i<=n && i%2==0`).

## Distinction from loop-invariant code

**Loop-invariant code** consists of statements or expressions that can be moved outside a loop body without affecting the program semantics. Such transformations, called loop-invariant code motion, are performed by some compilers to optimize programs. A loop-invariant code example (in the C programming language) is

```mw
for (int i=0; i<n; ++i) {
    x = y+z;
    a[i] = 6*i + x*x;
}
```

where the calculations `x = y+z` and `x*x` can be moved before the loop, resulting in an equivalent, but faster, program:

```mw
x = y+z;
t1 = x*x;
for (int i=0; i<n; ++i) {
    a[i] = 6*i + t1;
}
```

In contrast, e.g., the property `0<=i && i<=n` is a loop invariant for both the original and the optimized program, but is not part of the code, hence it doesn't make sense to speak of "moving it out of the loop".

Loop-invariant code may induce a corresponding loop-invariant property. For the above example, the easiest way to see it is to consider a program where the loop invariant code is computed both before and within the loop:

```mw
x1 = y+z;
t1 = x1*x1;
for (int i=0; i<n; ++i) {
    x2 = y+z;
    a[i] = 6*i + t1;
}
```

A loop-invariant property of this code is `(x1==x2 && t1==x2*x2) || i==0`, indicating that the values computed before the loop agree with those computed within (except before the first iteration).
