---
title: "Loop (statement)"
source: https://en.wikipedia.org/wiki/Loop_(computing)
domain: tqdm-progress
license: CC-BY-SA-4.0
tags: python tqdm, tqdm progress bar, progress meter python
fetched: 2026-07-02
---

# Loop (statement)

(Redirected from

Loop (computing)

)

In computer programming, a **loop** is a control flow construct that allows code to be executed repeatedly, usually with minor alterations between repetitions. Loops can be used to perform a repeated action on all items in a collection, or to implement a long lived program.

## Overview

Loops are a feature of high-level programming languages. In low-level programming languages the same functionality is achieved using jumps. When a program is compiled to machine code, looping may be achieved using jumps; but some loops can be optimized to run without jumping.

Usually, loops are expected to run for a finite number of iteration. Without proper care, loops may accidentally be created that have no possibility of terminating. Such loops are called infinite loops. The problem of determining whether a program contains an infinite loop is known as the halting problem.

## Conditional loop

A **conditional loop** (also known as an **indeterminate loop**) is a loop that determines whether to terminate based on a logical condition. These loops are flexible, but their exact behavior can be difficult to reason about.

A conditional loop is usually composed of two parts: a *condition* and a *body*. The *condition* is a logical statement depending on the state of the program and the *body* is a block of code that runs as long as the *condition* holds.

A common misconception is that the execution of the *body* terminates as soon as the *condition* does not hold anymore; but this is usually not the case. In most programming languages, the *condition* is checked once for every execution of the *body*. When the *condition* is checked is not standardized and some programming languages contain multiple conditional looping structures with different rules about when the *condition* is assessed.

### Pre-test loop

A **pre-test loop** is a conditional loop where the *condition* is checked before the *body* is executed. More precisely, the *condition* is checked and if it holds the *body* is execute. Afterwards, the *condition* is checked again, and if it holds the *body* is executed again. This process repeats until the *condition* does not hold. Many programming languages call this loop a *while loop* and refer to it with the keyword *while*. They are commonly formatted in manner similar to

```
while condition do
    body
repeat
```

Instead of the keywords *do* and *repeat*, other methods are sometimes used to indicate where the *body* begins and ends, such as curly braces or whitespace.

For example, the following code fragment first checks whether *x* is less than five, which it is, so the *body* is entered. There, *x* is displayed and then incremented by one. After executing the statements in the *body*, the *condition* is checked again, and the loop is executed again. This process repeats until *x* has the value five.

```
x ← 0
while x < 5 do
    display(x)
    x ← x + 1
repeat
```

### Post-test loop

A **post-test loop** is a conditional loop where the *condition* is checked after the *body* is executed. More precisely, the *body* is executed and afterwards the *condition* is checked. If it holds the *body* is run again and then the *condition* is checked. This is repeated until the *condition* does not hold. This is sometimes called a *do-while loop* due to the syntax used in various programming languages, although this can be confusing since Fortran and PL/I use the syntax "DO WHILE" for pre-test loops. Post-test loops are commonly formatted in manner similar to

```
do
    body
repeat while condition 
```

Instead of the keywords *do* and *repeat* others methods are sometime use to indicate where the *body* begins and ends, such as curly braces.

Some languages may use a different naming convention for this type of loop. For example, the Pascal and Lua languages have a "*repeat until*" loop, which continues to run *until* the control expression is true and then terminates.

### Three-part for loop

A **three-part for loop**, popularized by C, has two additional parts: *initialization* (loop variant), and *increment*, both of which are blocks of code. The *initialization* is intended as code that prepares the loop and is run once in the beginning and *increment* is used to update the state of the program after each iteration of the loop. Otherwise, the three-part for loop is a pre-test loop. They are commonly formatted in manner similar to

```
for initialization, condition, increment do
    body
repeat
```

This syntax came from B and was originally invented by Stephen C. Johnson. The following C code is an example of a three part loop that prints the numbers from 0 to 4.

```mw
for (int i = 0; i < 5; i++) {
    printf("%d\n", i);
}
```

### Equivalent constructs

Assuming there is a properly declared function or method called `do_work()`, the following are equivalent in programming languages which support post-test loops.

| **do** do_work() **repeat while** *condition* | do_work() **while** *condition* **do** do_work() **repeat** |
|---|---|

Furthermore, given that a `continue` statement is not used, the above is technically equivalent to the following, though these examples are not typical or modern style used in everyday computers.

```
while true do
    do_work()
    if condition is not true then
        break
    end if
repeat
```

or alternatively,

```
LOOPSTART:
do_work()
if condition then
    goto LOOPSTART
end if
```

## Enumeration

An **enumeration** (also known as an **determinate loop**) is a loop intended to iterate over all the items of a collection. It is not as flexible as a conditional loop; but it is more predictable. For example, it is easier to guarantee that enumerations terminate and they avoid potential off-by-one errors. Enumerations can be implemented using an iterator, whether implicitly or explicitly.

Depending on the programming language, various keywords are used to invoke enumerations. For example, descendants of ALGOL use `for`, while descendants of Fortran use `do` and COBOL uses `PERFORM VARYING`.

Enumerations are sometimes called "for loops," for example in Zig and Rust. This can be confusing since many of the most popular programming languages, such as C, C++, and Java, use that term for the three-part for loop, which is not an enumeration. Other programming languages, such as Perl and C#, avoid this confusion by using the term "foreach loop."

The order in which the items in the collection are iterated through depends on the programming language. Fortran 95 has a loop, invoked using the keyword `FORALL`, that is independent of this order. It has the effect of executing each iteration of the loop at the same time. This feature was made obsolescent in Fortran 2018.

## Loops in functional programming

In most functional programming languages, recursion is used instead of traditional loops. This is due to the fact that variables are immutable, and therefore the *increment* step of a loop cannot occur.

To avoid running into stack overflow errors for long loops, functional programming languages implement tail call optimisation, which allows the same stack frame to be used for each iteration of the loop, compiling to effectively the same code as a *while* or *for* loop.

Some languages, such as Haskell, have a syntax known as a list comprehension, which is similar to enumeration, iterating over the contents of a list and transforming it into a new list.

## Loop counter

A **loop counter** is a control variable that controls the iterations of a loop. Loop counters change with each iteration of a loop, providing a unique value for each iteration. The loop counter is used to decide when the loop should terminate. It is so named because most uses of this construct result in the variable taking on a range of integer values.

A common identifier naming convention is for the loop counter to use the variable names *i*, *j*, and *k* (and so on if needed), where *i* would be the most outer loop, *j* the next inner loop, etc. This style is generally agreed to have originated from the early programming of Fortran, where these variable names beginning with these letters were implicitly declared as having an integer type, and so were obvious choices for loop counters that were only temporarily required. The practice dates back further to mathematical notation where indices for sums and multiplications are often *i*, *j*, and *k*.

Using terse names for loop counters, like *i* and *j*, is discouraged by some since the purpose of the variables is not as clear as if they were given a longer more descriptive name.

Different languages specify different rules for what value the loop counter will hold on termination of its loop, and indeed some hold that it becomes undefined. This permits a compiler to generate code that leaves any value in the loop counter, or perhaps even leaves it unchanged because the loop value was held in a register and never stored in memory. Actual behavior may even vary according to the compiler's optimization settings.

Modifying the loop counter within the body of the loop can lead to unexpected consequences. To prevent such problems, some languages make the loop counter immutable. However, only overt changes are likely to be detected by the compiler. Situations where the address of the loop counter is passed as an argument to a subroutine, make it very difficult to check because the routine's behavior is in general unknowable to the compiler unless the language supports procedure signatures and argument intents.

## Early exit and continuation

Some languages may also provide supporting statements for altering how a loop's iteration proceeds. Common among these are the *break* statement, which terminates the current loop the program is in, and the *continue* statement, which skips to the next iteration of the current loop. These statements may have other names; For example in Fortran 90, they are called *exit* and *cycle*.

A loop can also be terminated by returning from the function within which it is being executed.

In the case of nested loops, the *break* and *continue* statements apply to the inner most loop. Some languages allow loops to be labelled. These statements can then be applied to any of the loops in which the program is nested.

```
outer_loop: (This is a label for the outermost loop)
for 1 ≤ i ≤ 2 do
    for 1 ≤ j ≤ 2 do
        display(i, j)
        if i = 2
            continue outer_loop
        end if
    repeat
repeat
(This nested loop displays the pairs (1, 1), (1, 2), and (2, 1))
```

## Infinite loop

An infinite loop is a loop which never terminates. This can be intentional, or the result of a logic error.

Systematically detecting infinite loops is known as the halting problem.

Infinite loops are useful in applications which need to perform a repeated calculation until a program terminates, such as web servers.
