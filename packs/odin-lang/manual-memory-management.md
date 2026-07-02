---
title: "Manual memory management"
source: https://en.wikipedia.org/wiki/Manual_memory_management
domain: odin-lang
license: docs: BSD-3-Clause (odin-lang.org)
tags: odin language, odin lang, odin programming
fetched: 2026-07-02
---

# Manual memory management

In computer science, **manual memory management** refers to the usage of manual instructions by the programmer to identify and deallocate unused objects, or garbage. Up until the mid-1990s, the majority of programming languages used in industry supported manual memory management, though garbage collection has existed since 1959, when it was introduced with Lisp. Today, however, languages with garbage collection such as Java are increasingly popular and the languages Objective-C and Swift provide similar functionality through Automatic Reference Counting. The main manually managed languages still in widespread use today are C and C++ – see C dynamic memory allocation.

## Description

Many programming languages use manual techniques to determine when to *allocate* a new object from the free store. C uses the `malloc` function; C++ and Java use the `new` operator; and many other languages (such as Python) allocate all objects from the free store. Determining when an object ought to be created (object creation) is generally trivial and unproblematic, though techniques such as object pools mean an object may be created before immediate use. The real challenge is object destruction – determination of when an object is no longer needed (i.e. is garbage), and arranging for its underlying storage to be returned to the free store for re-use. In manual memory allocation, this is also specified manually by the programmer; via functions such as `free()` in C, or the `delete` operator in C++ – this contrasts with automatic destruction of objects held in automatic variables, notably (non-static) local variables of functions, which are destroyed at the end of their scope in C and C++.

## Manual memory management techniques

For example:

- malloc() and free() or new and delete
- Memory arena
- Scratch buffer
- Resource acquisition is initialization, the pattern of tying an object's ownership of resources to its lifetime
- Defer, the act of deferring or postponing cleanup until the end of a function call

## Manual management and correctness

Manual memory management is known to enable several major classes of bugs into a program when used incorrectly, notably violations of memory safety or memory leaks. These are a significant source of security bugs.

- When an unused object is never released back to the free store, this is known as a memory leak. In some cases, memory leaks may be tolerable, such as a program which "leaks" a bounded amount of memory over its lifetime, or a short-running program which relies on an operating system to deallocate its resources when it terminates. However, in many cases memory leaks occur in long-running programs, and in such cases an *unbounded* amount of memory is leaked. When this occurs, the size of the available free store continues to decrease over time; when it is finally exhausted, the program then crashes.
- Catastrophic failure of the dynamic memory management system may result when an object's backing memory is deleted out from under it more than once; an object is explicitly destroyed more than once; when, while using a pointer to manipulate an object *not* allocated on the free store, a programmer attempts to release said pointer's target object's backing memory; or when, while manipulating an object via a pointer to another, arbitrary area of memory managed by an unknown external task, thread, or process, a programmer corrupts that object's state, possibly in such a way as to write outside of its bounds and corrupt its memory management data. The result of such actions can include heap corruption, premature destruction of a *different* (and newly created) object which happens to occupy the same location in memory as the multiply deleted object, program crashes due to a segmentation fault (violation of memory protection) and other forms of undefined behavior.
- Pointers to deleted objects become wild pointers if used post-deletion; attempting to use such pointers can result in difficult-to-diagnose bugs.

Languages which exclusively use garbage collection are known to avoid the last two classes of defects. Memory leaks can still occur (and bounded leaks frequently occur with generational or conservative garbage collection), but are generally less severe than memory leaks in manual systems.

## Resource acquisition is initialization

Manual memory management has one correctness advantage, which is that it allows automatic resource management via the resource acquisition is initialization (RAII) paradigm.

This arises when objects own scarce system resources (like graphics resources, file handles, or database connections) which must be relinquished when an object is destroyed – when the lifetime of the resource ownership should be tied to the lifetime of the object. Languages with manual management can arrange this by acquiring the resource during object initialization (in the constructor), and releasing during object destruction (in the destructor), which occurs at a precise time. This is known as Resource Acquisition Is Initialization (RAII).

This can also be used with deterministic reference counting. In C++, this ability is put to further use to automate memory deallocation within an otherwise-manual framework, use of smart pointers in the language's standard library to perform memory management is a common paradigm. In languages like Rust which enforce strict ownership, RAII becomes the default behavior for managing resources.

This approach is not usable in most garbage collected languages – notably tracing garbage collectors or more advanced reference counting – due to finalization being non-deterministic, and sometimes not occurring at all. That is, it is difficult to define (or determine) when or if a finalizer method might be called; this is commonly known as the finalizer problem. Java and other languages implementing a garbage collector frequently use manual management for scarce system resources *besides* memory via the dispose pattern: any object which manages resources is expected to implement the `dispose()` method, which releases any such resources and marks the object as inactive. Programmers are expected to invoke `dispose()` manually as appropriate to prevent "leaking" of scarce graphics resources. For stack resources (resources acquired and released within a single block of code), this can be automated by various language constructs, such as Python's `with`, C#'s `using`-with-resources (which call an object's `Dispose()` method) or Java's `try`-with-resources (usable on any object which implements `java.lang.AutoCloseable` and calls its `close()` method).

## Defer

A defer mechanism is a feature that allows the postponing of execution of a piece of code until later, usually either the end of scope or end of a function. This can be seen as similar to a finally block in other languages.

### C

C (beginning in C29) introduces a `defer` mechanism. Each `defer` block which is encountered in execution is run at scope exit (not when encountered), in the reverse order they were encountered.

```mw
#include <stddefer.h>
#include <stdio.h>
#include <stdlib.h>

int processFile(const char path[]) {
    FILE* f = fopen(path, "r");
    if (!f) {
        return -1;
    }

    defer {
        printf("Closing file.\n");
        fclose(f);
    };

    char* buffer = malloc(1024);
    if (!buffer) {
        return -2;
    }

    defer {
        printf("Freeing buffer.\n");
        free(buffer);
    };

    // Simulate multiple early exits
    if (fgets(buffer, 1024, f)) {
        return -3; // both defers still run
    }

    if (buffer[0] == '#') {
        return -4; // both defers still run
    }

    printf("Processing: %s\n", buffer);
    return 0;
}
```

C++ has not yet commented on whether or not it will integrate C `defer`, as RAII covers this use case.

### Go

In Go, `defer` is used to schedule a function call to run when the surrounding function returns. Multiple `defer`s run in last-in-first-out (LIFO) order.

```mw
package main

import "fmt"

func main() {
    fmt.Println("start")

    defer fmt.Println("first defer")
    defer fmt.Println("second defer")

    fmt.Println("end")
}
```

### Zig

In Zig, `defer` is block-level and runs when the current scope ends, not just the function. Unlike Go, Zig `defer` incurs no overhead.

```mw
const std = @import("std");

pub fn main() void {
    std.debug.print("start\n", .{});

    {
        defer std.debug.print("inner defer\n", .{});
        std.debug.print("inside block\n", .{});
    }

    std.debug.print("end\n", .{});
}
```

Zig also includes `errdefer`, which runs only if the function exits with an error.

## Performance

Many advocates of manual memory management argue that it affords superior performance when compared to automatic techniques such as garbage collection. Traditionally latency was the biggest advantage, but this is no longer the case. Manual allocation frequently has superior locality of reference.

Manual allocation is also known to be more appropriate for systems where memory is a scarce resource, due to faster reclamation. Memory systems can and do frequently "thrash" as the size of a program's working set approaches the size of available memory; unused objects in a garbage-collected system remain in an unreclaimed state for longer than in manually managed systems, because they are not immediately reclaimed, increasing the effective working set size.

Manual management has a number of documented performance *disadvantages*:

- Calls to `delete` and such incur an overhead each time they are made, this overhead can be amortized in garbage collection cycles. This is especially true of multithreaded applications, where delete calls must be synchronized.
- The allocation routine may be more complicated, and slower. Some garbage collection schemes, such as those with heap compaction, can maintain the free store as a simple array of memory (as opposed to the complicated implementations required by manual management schemes).

Latency is a debated point that has changed over time, with early garbage collectors and simple implementations performing very poorly compared to manual memory management, but sophisticated modern garbage collectors often performing as well or better than manual memory management.

Manual allocation does not suffer from the long "pause" times that occur in simple stop-the-world garbage collection, although modern garbage collectors have collection cycles which are often not noticeable.

Manual memory management and garbage collection both suffer from potentially unbounded deallocation times – manual memory management because deallocating a single object may require deallocating its members, and recursively its members' members, etc., while garbage collection may have long collection cycles. This is especially an issue in real time systems, where unbounded collection cycles are generally unacceptable; real-time garbage collection is possible by pausing the garbage collector, while real-time manual memory management requires avoiding large deallocations, or manually pausing deallocation.
