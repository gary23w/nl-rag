---
title: "Structured programming"
source: https://en.wikipedia.org/wiki/Structured_programming
domain: pl-i-language
license: CC-BY-SA-4.0
tags: pl i language, structured programming, mainframe computer, ibm system, punched card
fetched: 2026-07-02
---

# Structured programming

**Structured programming** is a programming paradigm characterized by source code that uses block-based source code structure to encode control flow such as sequence, selection (i.e. if-then-else and switch) and iteration (i.e. for and while).

Originally, the central goal of the structured programming movement was to eliminate the need for and use of the goto statement. As goto provides powerful and flexible flow control, it can be used to write any arbitrarily complex algorithm, but the resulting code often has significant quality issues, commonly described as spaghetti code. Structured programming replaces goto with constructs that tend to result in better code. The paradigm became popular and for the most part achieved the goal of supplanting goto. In fact, its ubiquity is so thorough that for much of software development, it is simply the way code is written, no longer a topic of discussion as it once was.

Structured programming is sometimes associated with modular programming even though they are different. In a general sense, *structured* implies a sense of modularity and of being written to be efficient and easy to understand and modify, but this is not what structured programming means in a narrow sense.

After structured programming became popular, the style of programming that preceded it was retroactively called non-structured programming. Although technically a programming paradigm, it differs from other paradigms in that it was not intentionally designed. It was simply the state-of-the-art before structured programming was envisioned.

## History

The paradigm emerged in the late 1950s with the appearance of the ALGOL 58 and ALGOL 60 programming languages, with the latter including support for block structures.

Contributing factors to its popularity and widespread acceptance, at first in academia and later among practitioners, include the publication of what is now known as the structured program theorem in 1966, and the publication of the influential "Go To Statement Considered Harmful" open letter in 1968 by Dutch computer scientist Edsger W. Dijkstra, who coined the term *structured programming*.

### Theoretical foundation

The structured program theorem provides the theoretical basis of structured programming. It states that three ways of combining programs—sequencing, selection, and iteration—are sufficient to express any computable function. This observation did not originate with the structured programming movement; these structures are sufficient to describe the instruction cycle of a central processing unit, as well as the operation of a Turing machine. Therefore, a processor is always executing a "structured program" in this sense, even if the instructions it reads from memory are not part of a structured program. However, authors usually credit the result to a 1966 paper by Böhm and Jacopini, possibly because Dijkstra cited this paper himself. The structured program theorem does not address how to write and analyze a usefully structured program. These issues were addressed during the late 1960s and early 1970s, with major contributions by Dijkstra, Robert W. Floyd, Tony Hoare, Ole-Johan Dahl, and David Gries.

### Debate

P. J. Plauger, an early adopter of structured programming, described his reaction to the structured program theorem:

> Us converts waved this interesting bit of news under the noses of the unreconstructed assembly-language programmers who kept trotting forth twisty bits of logic and saying, 'I betcha can't structure this.' Neither the proof by Böhm and Jacopini nor our repeated successes at writing structured code brought them around one day sooner than they were ready to convince themselves.

Donald Knuth accepted the principle that programs must be written with provability in mind, but he disagreed with abolishing the GOTO statement, and as of 2018 has continued to use it in his programs. In his 1974 paper, "Structured Programming with Goto Statements", he gave examples where he believed that a direct jump leads to clearer and more efficient code without sacrificing provability. Knuth proposed a looser structural constraint: It should be possible to draw a program's flow chart with all forward branches on the left, all backward branches on the right, and no branches crossing each other. Some of those knowledgeable in compilers and graph theory have advocated allowing only reducible flow graphs.

Structured programming theorists gained a major ally in the 1970s after IBM researcher Harlan Mills applied his interpretation of structured programming theory to the development of an indexing system for *The New York Times* research file. The project was a great engineering success, and managers at other companies cited it in support of adopting structured programming, although Dijkstra criticized the ways that Mills's interpretation differed from the published work.

As late as 1987, it was still possible to raise the question of structured programming in a computer science journal. Frank Rubin did so in that year with an open letter titled "'GOTO Considered Harmful' Considered Harmful". Multiple objections followed, including a response from Dijkstra that sharply criticized both Rubin and the concessions other writers made when responding to him.

### Outcome

By the end of the 20th century, nearly all computer scientists were convinced that it is useful to learn and apply the concepts of structured programming. High-level programming languages that originally lacked programming structures, such as FORTRAN, COBOL, and BASIC, now have them.

## Control structures

Following the structured program theorem, a program is composed of three control structures:

**Sequence**

Ordered statements executed in sequence.

Although not part of the structured program theorem, languages generally include a block concept that groups a sequence of code so that it acts much like a single statement. A language includes a way to mark a sequence of statements as a block that, unless it contains flow control, will be executed sequentially, top-to-bottom. For example, a block is enclosed in curly braces

{...}

in

C

and other

curly-brace languages

, enclosed in

BEGIN...END

in

PL/I

and

Pascal

, and indicated via indentation in

Python

. Some blocks use different syntax for each structure. For example, an if-statement is enclosed in

if...fi

in

ALGOL 68

.

**Selection**

A block (which can be a single statement) is executed depending on the state of the program. This construct is often expressed with

keywords

such as

if

,

then

, and

else

. The conditional statement should have at least one true-condition path, and each condition path should have just one exit point.

**Iteration**

(a.k.a. repetition) A block (which can be a single statement) is executed repeatedly until the program reaches a certain state. This construct is often expressed with keywords such as

while

,

repeat

,

for

, or

do-until

. Although structured programming limits the flow to have exactly one entry point and exactly one exit point, most languages allow for multiple, early exit.

## Language support

Generally, a language is intended to support one or more programming paradigms. At the same time, even though a language is not intended to support a paradigm, it often can be used in that way regardless. In theory, any language can be used for structured programming. Some of the languages initially used for structured programming include ALGOL, Pascal, PL/I, Ada, and RPL, but most new procedural programming languages since that time have included features to encourage structured programming, and sometimes deliberately left out features – notably GOTO – to avoid its pitfalls.

## Common deviations

While the use of goto has largely been replaced by structured constructs, most languages provide features that are not strictly consistent with the structured programming theorem.

### Early return

Most languages provide a return statement that allows for multiple, early return exit points from a function. As a function is a block, this feature is counter to the single exit point described in the theorem.

### Early exit

Many languages provide for early exit from a block (other than via return). For example, a loop construct may support a break statement that exits the loop block before its end. As the theorem describes, such early-exit logic can be eliminated by adding branches or tests, but this can add significant complexity. C is an early and prominent example of these constructs. Some newer languages also have "labeled breaks", which allow breaking out of more than just the innermost loop.

The need for multiple exits can arise for a variety of reasons, most often either that the function has no more work to do (if returning a value, it has completed the calculation), or has encountered "exceptional" circumstances that prevent it from continuing, hence needing exception handling.

A problem with early exit is that cleanup statements might not be executed. For example, allocated memory is not deallocated, or open files are not closed, causing memory leak and resource leak. Cleanup must be done at each return site, which is brittle and can easily result in bugs. For instance, in later development, a return statement could be overlooked by a developer, and an action that should be performed at the end of a function (e.g., a trace statement) might not be performed in all cases. Languages without a return statement, such as Pascal, Lisp, and OCaml, do not have this problem.

Most modern languages provide language-level support to prevent such leaks (see resource management). As a structured alternative to using goto and a cleanup block, unwind protection ensures that certain code is runs when execution exits a block; it is often implemented in connection with exception handling as a try-finally. An alternative approach, in C++, is resource acquisition is initialization, which uses normal stack unwinding (variable deallocation) at function exit to call destructors on local variables to deallocate resources.

Kent Beck, Martin Fowler, and co-authors have argued in their refactoring books that nested conditionals may be harder to understand than a certain type of flatter structure using multiple exits predicated by guard clauses. Their 2009 book flatly states that "one exit point is really not a useful rule. Clarity is the key principle: If the method is clearer with one exit point, use one exit point; otherwise don’t". They offer a cookbook solution for transforming a function consisting only of nested conditionals into a sequence of guarded return (or throw) statements, followed by a single unguarded block, which is intended to contain the code for the common case, while the guarded statements are supposed to deal with the less common ones (or with errors). Herb Sutter and Andrei Alexandrescu also argue in their 2004 C++ tips book that the single exit point is an obsolete requirement.

In his 2004 textbook, David Watt writes that "single-entry multi-exit control flows are often desirable". Using Tennent's framework notion of sequencer, Watt uniformly describes the control flow constructs found in contemporary programming languages and attempts to explain why certain types of sequencers are preferable to others in the context of multi-exit control flows. Watt writes that unrestricted gotos (jump sequencers) are bad because the destination of the jump is not self-explanatory to the reader of a program until the reader finds and examines the actual label or address that is the target of the jump. In contrast, Watt argues that the conceptual intent of a return sequencer is clear from its own context, without having to examine its destination. Watt writes that a class of sequencers known as *escape sequencers*, defined as a "sequencer that terminates execution of a textually enclosing command or procedure", encompasses both breaks from loops (including multi-level breaks) and return statements. Watt also notes that while jump sequencers (gotos) have been somewhat restricted in languages like C, where the target must be inside the local block or an encompassing outer block, that restriction alone is not sufficient to make the intent of gotos in C self-describing and so they can still produce "spaghetti code". Watt also examines how exception sequencers differ from escape and jump sequencers; this is explained in the next section of this article.

In contrast to the above, Bertrand Meyer wrote in his 2009 textbook that instructions like break and continue "are just the old goto in sheep's clothing" and strongly advised against their use.

### Exception handling

Peter Ritchie notes that, in principle, even a single throw right before the return constitutes a violation of the single-exit principle, but argues that Dijkstra's rules were written in a time before exception handling became a paradigm in programming languages, so he proposes to allow any number of throw points in addition to a single return point. He notes that solutions that wrap exceptions for the sake of creating a single exit have higher nesting depth and thus are more difficult to comprehend, and even accuses those who propose to apply such solutions to programming languages that support exceptions of engaging in cargo-cult thinking.

David Watt also analyzes exception handling in the framework of sequencers (introduced in this article in the previous section on early exits.) Watt notes that an abnormal situation (generally exemplified with arithmetic overflows or input/output failures like file not found) is a kind of error that "is detected in some low-level program unit, but [for which] a handler is more naturally located in a high-level program unit". For example, a program might contain several calls to read files, but the action to perform when a file is not found depends on the meaning (purpose) of the file in question to the program and thus a handling routine for this abnormal situation cannot be located in low-level system code. Watts further notes that introducing status flags testing in the caller, as single-exit structured programming or even (multi-exit) return sequencers would entail, results in a situation where "the application code tends to get cluttered by tests of status flags" and that "the programmer might forgetfully or lazily omit to test a status flag. In fact, abnormal situations represented by status flags are by default ignored!" He notes that in contrast to status-flags testing, exceptions have the opposite default behavior, causing the program to terminate unless the programmer explicitly deals with the exception in some way, possibly by adding code to willfully ignore it. Based on these arguments, Watt concludes that jump sequencers or escape sequencers (discussed in the previous section) are not as suitable as a dedicated exception sequencer with the semantics discussed above.

The textbook by Louden and Lambert emphasizes that exception handling differs from structured programming constructs like while loops because the transfer of control "is set up at a different point in the program than that where the actual transfer takes place. At the point where the transfer actually occurs, there may be no syntactic indication that control will in fact be transferred." Computer science professor Arvind Kumar Bansal also notes that in languages which implement exception handling, even control structures like for, which have the single-exit property in absence of exceptions, no longer have it in presence of exceptions, because an exception can prematurely cause an early exit in any part of the control structure; for instance if `init()` throws an exception in `for (init(); check(); increm())`, then the usual exit point after check() is not reached. Citing multiple prior studies by others (1999–2004) and their own results, Westley Weimer and George Necula wrote that a significant problem with exceptions is that they "create hidden control-flow paths that are difficult for programmers to reason about".

The necessity to limit code to single-exit points appears in some contemporary programming environments focused on parallel computing, such as OpenMP. The various parallel constructs from OpenMP, like `parallel do`, do not allow early exit from inside to the outside of the parallel construct; this restriction includes all manner of exits, including break and exceptions, but all of these are permitted inside the parallel construct if the jump target is also inside.

### Multiple entry

Relatively rarely, functions allow multiple *entry.* This is most commonly only *re*-entry into a coroutine (or generator/semicoroutine), where a function yields control (and possibly a value), but can then be resumed where it left off. There are a number of common uses of such programming, notably for streams (particularly input/output), state machines, and concurrency. From a code-execution point of view, yielding from a coroutine is closer to structured programming than returning from a function, as the function has not actually terminated, and will continue when called again – it is not an early exit. However, coroutines mean that multiple functions have execution state – rather than a single call stack of functions – and thus introduce a different form of complexity.

It is rare for functions to allow entry to an arbitrary position in the function, as in this case the program state (such as variable values) is uninitialized or ambiguous, and this is similar to a goto.

### State machines

Some programs, particularly parsers and communications protocols, have a number of states that follow each other in a way that is not easily reduced to the basic structures, and some programmers implement the state-changes with a jump to the new state. This type of state-switching is often used in the Linux kernel.

However, it is possible to structure these systems by making each state-change a separate function and using a variable to indicate the active state (see trampoline). Alternatively, these can be implemented via coroutines, which dispense with the trampoline.
