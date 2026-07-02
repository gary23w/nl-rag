---
title: "Coroutine"
source: https://en.wikipedia.org/wiki/Coroutine
domain: asyncio-python
license: CC-BY-SA-4.0
tags: python asyncio, asyncio event loop, async await python
fetched: 2026-07-02
---

# Coroutine

**Coroutines** are computer program components that can be suspended and resumed — generalizing subroutines — for cooperative multitasking. Coroutines are well-suited for implementing familiar program components such as cooperative tasks, exceptions, event loops, iterators, infinite lists and pipes.

They have been described as "functions whose execution you can pause".

Melvin Conway coined the term *coroutine* in 1958 when he applied it to the construction of an assembly program. The first published explanation of the coroutine appeared later, in 1963.

## Definition and types

There is no single precise definition of coroutine. In 1980 Christopher D. Marlin summarized two widely-acknowledged fundamental characteristics of a coroutine:

1. the values of data local to a coroutine persist between successive calls;
2. the execution of a coroutine is suspended as control leaves it, only to carry on where it left off when control re-enters the coroutine at some later stage.

Besides that, a coroutine implementation has 3 features:

1. the control-transfer mechanism. *Asymmetric coroutines* usually provide keywords like `yield` and `resume`. Programmers cannot freely choose which frame to yield to. The runtime only yields to the nearest caller of the current coroutine. On the other hand, in *symmetric coroutines*, programmers must specify a yield destination.
2. whether coroutines are provided in the language as first-class objects, which can be freely manipulated by the programmer, or as constrained constructs;
3. whether a coroutine is able to suspend its execution from within nested function calls. Such a coroutine is a *stackful coroutine*. One to the contrary is called *stackless coroutines*, where unless marked as coroutine, a regular function can't use the keyword `yield`.

The paper "Revisiting Coroutines" published in 2009 proposed the term *full coroutine* to denote one that supports first-class coroutine and is stackful. Full Coroutines deserve their own name in that they have the same expressive power as one-shot continuations and delimited continuations. Full coroutines are either symmetric or asymmetric. Importantly, whether a coroutine is symmetric or asymmetric has no bearing on how expressive it can be, though full coroutines are more expressive than non-full coroutines. While their expressive power is the same, asymmetrical coroutines more closely resemble routine based control structures in the sense that control is always passed back to the invoker, which programmers may find more familiar.

## Comparisons

### Subroutines

Subroutines are special cases of coroutines. When subroutines are invoked, execution begins at the start, and once a subroutine exits, it is finished; an instance of a subroutine only returns once, and does not hold state between invocations. By contrast, coroutines can exit by calling other coroutines, which may later return to the point where they were invoked in the original coroutine; from the coroutine's point of view, it is not exiting but calling another coroutine. Thus, a coroutine instance holds state, and varies between invocations; there can be multiple instances of a given coroutine at once. The difference between calling another coroutine by means of "yielding" to it and simply calling another routine (which then, also, would return to the original point), is that the relationship between two coroutines which yield to each other is not that of caller-callee, but instead symmetric.

Any subroutine can be translated to a coroutine which does not call *yield*.

Here is a simple example of how coroutines can be useful. Suppose you have a consumer-producer relationship where one routine creates items and adds them to a queue and another removes items from the queue and uses them. For reasons of efficiency, you want to add and remove several items at once. The code might look like this:

```
q := new Queue<Item>

coroutine produce
    loop
        while q is not full
            create some new items
            add the items to q
        yield to consume

coroutine consume
    loop
        while q is not empty
            remove some items from q
            use the items
        yield to produce

call produce
```

The queue is then completely filled or emptied before yielding control to the other coroutine using the *yield* command. The further coroutines calls are starting right after the *yield*, in the outer coroutine loop.

Although this example is often used as an introduction to multithreading, two threads are not needed for this: the *yield* statement can be implemented by a jump directly from one routine into the other.

### Threads

Coroutines are very similar to threads. However, coroutines are cooperatively multitasked, whereas threads are typically preemptively multitasked. Coroutines provide concurrency, because they allow tasks to be performed out of order or in a changeable order, without changing the overall outcome, but they do not provide parallelism, because they do not execute multiple tasks simultaneously. The advantages of coroutines over threads are that they may be used in a hard real-time context (switching between coroutines does not involve any system calls or any blocking calls whatsoever), there is no need for synchronization primitives such as mutexes, semaphores, etc. in order to guard critical sections, and there is no need for support from the operating system.

It is possible to implement coroutines using preemptively-scheduled threads, in a way that will be transparent to the calling code, but some of the advantages (particularly the suitability for hard-realtime operation and relative cheapness of switching between them) will be lost.

### Generators

Generators, also known as semicoroutines, are a subset of coroutines. Specifically, while both can yield multiple times, suspending their execution and allowing re-entry at multiple entry points, they differ in coroutines' ability to control where execution continues immediately after they yield, while generators cannot, instead transferring control back to the generator's caller. That is, since generators are primarily used to simplify the writing of iterators, the `yield` statement in a generator does not specify a coroutine to jump to, but rather passes a value back to a parent routine.

However, it is still possible to implement coroutines on top of a generator facility, with the aid of a top-level dispatcher routine (a trampoline, essentially) that passes control explicitly to child generators identified by tokens passed back from the generators:

```
q := new Queue<Item>

generator produce
    loop
        while q is not full
            create some new items
            add the items to q
        yield

generator consume
    loop
        while q is not empty
            remove some items from q
            use the items
        yield

subroutine dispatcher
    d := new Map<Generator, Iterator>
    d[produce] := start consume
    d[consume] := start produce
    current := produce
    loop
        call current
        current := next d[current]

call dispatcher
```

A number of implementations of coroutines for languages with generator support but no native coroutines (e.g. Python before 2.5) use this or a similar model.

### Mutual recursion

Using coroutines for state machines or concurrency is similar to using mutual recursion with tail calls, as in both cases the control changes to a different one of a set of routines. However, coroutines are more flexible and generally more efficient. Since coroutines yield rather than return, and then resume execution rather than restarting from the beginning, they are able to hold state, both variables (as in a closure) and execution point, and yields are not limited to being in tail position; mutually recursive subroutines must either use shared variables or pass state as parameters. Further, each mutually recursive call of a subroutine requires a new stack frame (unless tail call elimination is implemented), while passing control between coroutines uses the existing contexts and can be implemented simply by a jump.

## Common uses

Coroutines are useful to implement the following:

- State machines within a single subroutine, where the state is determined by the current entry/exit point of the procedure; this can result in more readable code compared to use of goto, and may also be implemented via mutual recursion with tail calls.
- Actor model of concurrency, for instance in video games. Each actor has its own procedures (this again logically separates the code), but they voluntarily give up control to central scheduler, which executes them sequentially (this is a form of cooperative multitasking).
- Generators, and these are useful for streams – particularly input/output – and for generic traversal of data structures.
- Communicating sequential processes where each sub-process is a coroutine. Channel inputs/outputs and blocking operations yield coroutines and a scheduler unblocks them on completion events. Alternatively, each sub-process may be the parent of the one following it in the data pipeline (or preceding it, in which case the pattern can be expressed as nested generators).
- Reverse communication, commonly used in mathematical software, wherein a procedure such as a solver, integral evaluator, ... needs the using process to make a computation, such as evaluating an equation or integrand.

## Native support

Coroutines originated as an assembly language method, but are supported in some high-level programming languages.

- Aikido
- AngelScript
- Ballerina
- BCPL
- Pascal (Borland Turbo Pascal 7.0 with uThreads module)
- BETA
- BLISS
- C++ (since C++20)
- C# (since 2.0)
- Chapel
- ChucK
- CLU
- D
- Dynamic C
- Erlang
- F#
- Factor
- GameMonkey Script
- GDScript (Godot's scripting language)
- Haskell
- High Level Assembly
- Icon
- Io
- JavaScript (since 1.7, standardized in ECMAScript 6) ECMAScript 2017 also includes await support.
- Julia
- Kotlin (since 1.1)
- Limbo
- Lua
- Lucid
- μC++
- Modula-2
- Nemerle
- Perl 5 (using the Coro module)
- PHP (since version 5.5)
- Picolisp
- Prolog
- Python (since 2.5, with improved support since 3.3 and with explicit syntax since 3.5)
- Racket
- Raku
- Ruby
- Sather
- Scheme
- Self
- Simula 67
- Smalltalk
- Squirrel
- Stackless Python
- SuperCollider
- Tcl (since 8.6)
- urbiscript

Java does not have native or library support for coroutines, but it can call Kotlin coroutines `kotlinx.coroutines` (though this is not ideal and would require a Java wrapper over Kotlin).

Since continuations can be used to implement coroutines, programming languages that support them can also quite easily support coroutines.

## Implementations

As of 2003, many of the most popular programming languages, including C and its derivatives, do not have built-in support for coroutines within the language or their standard libraries. This is, in large part, due to the limitations of stack-based subroutine implementation. An exception is the C++ library Boost.Context, part of Boost, which supports context swapping on ARM, MIPS, PowerPC, SPARC and x86 on POSIX, Mac OS X and Windows. Coroutines can be built upon Boost.Context.

In situations where a coroutine would be the natural implementation of a mechanism, but is not available, the typical response is to use a closure – a subroutine with state variables (static variables, often boolean flags) to maintain an internal state between calls, and to transfer control to the correct point. Conditionals within the code result in the execution of different code paths on successive calls, based on the values of the state variables. Another typical response is to implement an explicit state machine in the form of a large and complex switch statement or via a goto statement, particularly a computed goto. Such implementations are considered difficult to understand and maintain, and a motivation for coroutine support.

Threads, and to a lesser extent fibers, are an alternative to coroutines in mainstream programming environments today. Threads provide facilities for managing the real-time cooperative interaction of *simultaneously* executing pieces of code. Threads are widely available in environments that support C (and are supported natively in many other modern languages), are familiar to many programmers, and are usually well-implemented, well-documented and well-supported. However, as they solve a large and difficult problem they include many powerful and complex facilities and have a correspondingly difficult learning curve. As such, when a coroutine is all that is needed, using a thread can be overkill.

One important difference between threads and coroutines is that threads are typically preemptively scheduled while coroutines are not. Because threads can be rescheduled at any instant and can execute concurrently, programs using threads must be careful about locking. In contrast, because coroutines can only be rescheduled at specific points in the program and do not execute concurrently, programs using coroutines can often avoid locking entirely. This property is also cited as a benefit of event-driven or asynchronous programming.

Since fibers are cooperatively scheduled, they provide an ideal base for implementing coroutines above. However, system support for fibers is often lacking compared to that for threads.

### C

In order to implement general-purpose coroutines, a second call stack must be obtained, which is a feature not directly supported by the C language. A reliable (albeit platform-specific) way to achieve this is to use a small amount of inline assembly to explicitly manipulate the stack pointer during initial creation of the coroutine. This is the approach recommended by Tom Duff in a discussion on its relative merits vs. the method used by Protothreads. On platforms which provide the POSIX sigaltstack system call, a second call stack can be obtained by calling a springboard function from within a signal handler to achieve the same goal in portable C, at the cost of some extra complexity. C libraries complying to POSIX or the Single Unix Specification (SUSv3) provided such routines as getcontext, setcontext, makecontext and swapcontext, but these functions were declared obsolete in POSIX 1.2008.

Once a second call stack has been obtained with one of the methods listed above, the setjmp and longjmp functions in the standard C library can then be used to implement the switches between coroutines. These functions save and restore, respectively, the stack pointer, program counter, callee-saved registers, and any other internal state as required by the ABI, such that returning to a coroutine after having yielded restores all the state that would be restored upon returning from a function call. Minimalist implementations, which do not piggyback off the setjmp and longjmp functions, may achieve the same result via a small block of inline assembly which swaps merely the stack pointer and program counter, and clobbers all other registers. This can be significantly faster, as setjmp and longjmp must conservatively store all registers which may be in use according to the ABI, whereas the clobber method allows the compiler to store (by spilling to the stack) only what it knows is actually in use.

Due to the lack of direct language support, many authors have written their own libraries for coroutines which hide the above details. Russ Cox's libtask library is a good example of this genre. It uses the context functions if they are provided by the native C library; otherwise it provides its own implementations for ARM, PowerPC, Sparc, and x86. Other notable implementations include libpcl, coro, lthread, libCoroutine, libconcurrency, libcoro, ribs2, libdill., libaco, and libco.

In addition to the general approach above, several attempts have been made to approximate coroutines in C with combinations of subroutines and macros. Simon Tatham's contribution, based on Duff's device, is a notable example of the genre, and is the basis for Protothreads and similar implementations. In addition to Duff's objections, Tatham's own comments provide a frank evaluation of the limitations of this approach: "As far as I know, this is the worst piece of C hackery ever seen in serious production code." The main shortcomings of this approximation are that, in not maintaining a separate stack frame for each coroutine, local variables are not preserved across yields from the function, it is not possible to have multiple entries to the function, and control can only be yielded from the top-level routine.

### C++

C++20 introduced standardized coroutines as stackless functions that can be suspended in the middle of execution and resumed at a later point. The suspended state of a coroutine is stored on the heap. Implementation of this standard is ongoing, with the G++ and MSVC compilers currently fully supporting standard coroutines in recent versions. A generator class for synchronous and lazy-evaluated ranges, `std::generator`, was added in C++23. A proper task class, `std::execution::task`, was introduced in C++26. It is invoked using `std::execution::sync_wait()`, which returns `std::optional<std::tuple<Ts...>>`.

This is an example of C++20 coroutines with the C++26 `std::execution::task` class.

```mw
import std;

using std::optional;
using std::tuple;
using std::execution::task;

task<int> add(int a, int b) noexcept {
    co_return a + b;
}

task<int> test() {
    int ret = co_await add(1, 2);
    std::println("Return {}", ret);
    co_return ret;
}

int main(int argc, char* argv[]) {
    optional<tuple<int>> result = std::execution::sync_wait(test());
    std::println("Result: {}", std::get<0>(result).value_or(std::make_tuple(-1)));

    return 0;
}
```

### C

C# 2.0 added semi-coroutine (generator) functionality through the iterator pattern and `yield` keyword. C# 5.0 includes await syntax support.

### Clojure

Cloroutine is a third-party library providing support for stackless coroutines in Clojure. It's implemented as a macro, statically splitting an arbitrary code block on arbitrary var calls and emitting the coroutine as a stateful function.

### D

D implements coroutines as its standard library class `core.thread.Fiber` for a fiber. A generator (`std.concurrency.Generator`) makes it trivial to expose a fiber function as an input range (`std.range.interfaces.InputRange`), making any fiber compatible with existing range algorithms.

### Go

Go has a built-in concept of "goroutines", a type of green thread which are lightweight, independent processes managed by the Go runtime. A new goroutine can be started using the "go" keyword. Each goroutine has a variable-size stack which can be expanded as needed. Goroutines generally communicate using Go's built-in channels. However, goroutines are not coroutines (for instance, local data does not persist between successive calls).

### Java

There are several implementations for coroutines in Java. Despite the constraints imposed by Java's abstractions, the JVM does not preclude the possibility. There are four general methods used, but two break bytecode portability among standards-compliant JVMs.

- Modified JVMs. It is possible to build a patched JVM to support coroutines more natively. The Da Vinci JVM has had patches created.
- Modified bytecode. Coroutine functionality is possible by rewriting regular Java bytecode, either on the fly or at compile time. Toolkits include Javaflow, Java Coroutines, and Coroutines.
- Platform-specific JNI mechanisms. These use JNI methods implemented in the OS or C libraries to provide the functionality to the JVM.
- Thread abstractions. Coroutine libraries which are implemented using threads may be heavyweight, though performance will vary based on the JVM's thread implementation.
- One can call Kotlin coroutines from Java, but as Java cannot "`suspend`", one must instead block using `kotlinx.coroutines.runBlocking`, expose a `kotlinx.coroutines.CoroutineScope` or `kotlinx.coroutines.Job` API, or (most idiomatically) return a `java.util.concurrent.CompletableFuture`.

### JavaScript

Since ECMAScript 2015, JavaScript has support for generators, which are a special case of coroutines.

### Kotlin

Kotlin implements coroutines as part of a first-party library.

```mw
import kotlinx.coroutines.*

fun main() = runBlocking {
    launch {
        delay(1000L)
        print("Hello from within coroutine!")
    }

    print("Hello world!")
}
```

### Lua

Lua has supported first-class stackful asymmetric coroutines since version 5.0 (2003), in the standard library *coroutine*.

### Modula-2

Modula-2 as defined by Wirth implements coroutines as part of the standard SYSTEM library.

The procedure NEWPROCESS() fills in a context given a code block and space for a stack as parameters, and the procedure TRANSFER() transfers control to a coroutine given the coroutine's context as its parameter.

### Mono

The Mono Common Language Runtime has support for continuations, from which coroutines can be built.

### .NET Framework

During the development of the .NET Framework 2.0, Microsoft extended the design of the Common Language Runtime (CLR) hosting APIs to handle fiber-based scheduling with an eye towards its use in fiber-mode for SQL server. Before release, support for the task switching hook `ICLRTask::SwitchOut` was removed due to time constraints. Consequently, the use of the fiber API to switch tasks is currently not a viable option in the .NET Framework.

### OCaml

OCaml supports coroutines through its `Thread` module. These coroutines provide concurrency without parallelism, and are scheduled preemptively on a single operating system thread. Since OCaml 5.0, green threads are also available; provided by different modules.

### Perl

- Coro

Coroutines are natively implemented in all Raku backends.

### PHP

- Fibers native since PHP 8.1
- Amphp
- Open Swoole
- Coroutine implemented in a way that resembles Python functions, and some Go, many examples showing there code converted with same number of lines and behavior.

### Python

Python has support for coroutines using the `asyncio.create_task()` function.

- Python 2.5 implements better support for coroutine-like functionality, based on extended generators (PEP 342)
- Python 3.3 improves this ability, by supporting delegating to a subgenerator (PEP 380)
- Python 3.4 introduces a comprehensive asynchronous I/O framework as standardized in PEP 3156, which includes coroutines that leverage subgenerator delegation
- Python 3.5 introduces explicit support for coroutines with async/await syntax (PEP 0492).
- Since Python 3.7, async/await have become reserved keywords.
- Eventlet
- Greenlet
- gevent
- Stackless Python

```mw
import asyncio
import time
from asyncio import Task

async def main() -> None:
    task1: Task[str] = asyncio.create_task(say_after(1, "hello"))
    task2: Task[str] = asyncio.create_task(say_after(2, "world"))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take around 2 seconds)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")
```

### Racket

Racket provides native continuations, with a trivial implementation of coroutines provided in the official package catalog. Implementation by S. De Gabrielle

### Ruby

- Ruby 1.9 supports coroutines natively which are implemented as fibers, which are semi-coroutines.
- An implementation by Marc De Scheemaecker
- Ruby 2.5 and higher supports coroutines natively which are implemented as fibers
- An implementation by Thomas W Branson

### Scheme

Since Scheme provides full support for continuations, implementing coroutines is nearly trivial, requiring only that a queue of continuations be maintained.

### Smalltalk

Since, in most Smalltalk environments, the execution stack is a first-class citizen, coroutines can be implemented without additional library or VM support.

### Tcl

Since version 8.6, Tcl supports coroutines in the core language.

### Vala

Vala implements native support for coroutines. They are designed to be used with a GTK Main Loop, but can be used alone if care is taken to ensure that the end callback will never have to be called before doing, at least, one yield.

### Assembly languages

Machine-dependent assembly languages often provide direct methods for coroutine execution. For example, in MACRO-11, the assembly language of the PDP-11 family of minicomputers, the "classic" coroutine switch is effected by the instruction "JSR PC,@(SP)+", which jumps to the address popped from the stack and pushes the current (*i.e* that of the **next**) instruction address onto the stack. On VAXen (in VAX MACRO) the comparable instruction is "JSB @(SP)+". Even on a Motorola 6809 there is the instruction "JSR [,S++]"; note the "++", as 2 bytes (of address) are popped from the stack. This instruction is much used in the (standard) 'monitor' Assist 09.
