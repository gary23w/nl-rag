---
title: "Stack trace"
source: https://en.wikipedia.org/wiki/Stack_trace
domain: debug-adapter-protocol
license: CC-BY-SA-4.0
tags: debug adapter protocol, dap debugging, editor debugger integration, breakpoint protocol
fetched: 2026-07-02
---

# Stack trace

In computing, a **stack trace** (also called **stack backtrace** or **stack traceback**) is a report of the active stack frames at a certain point in time during the execution of a program. When a program is run, memory is often dynamically allocated in two places: the stack and the heap. Memory is continuously allocated on a stack but not on a heap. Stack also refers to a programming construct, thus to differentiate it, this stack is referred to as the program's **function call stack**. Technically, once a block of memory has been allocated on the stack, it cannot be easily removed as there can be other blocks of memory that were allocated after it. Each time a function is called in a program, a block of memory called an **activation record** is allocated on top of the call stack. Generally, the activation record stores the function's arguments and local variables. What exactly it contains and how it's laid out is determined by the calling convention.

Programmers commonly use stack tracing during interactive and post-mortem debugging. End-users may see a stack trace displayed as part of an error message, which the user can then report to a programmer.

A stack trace allows tracking the sequence of nested functions called - up to the point where the stack trace is generated. In a post-mortem scenario this extends up to the function where the failure occurred (but was not necessarily caused). Sibling calls do not appear in a stack trace.

## Language support

Many programming languages, including Java and C#, have built-in support for retrieving the current stack trace via system calls. Before `std::stacktrace` was added in standard library as a container for `std::stacktrace_entry`, pre-C++23 has no built-in support for doing this, but C++ users can retrieve stack traces with (for example) the stacktrace library. In JavaScript, exceptions hold a `stack` property that contain the stack from the place where it was thrown.

### Python

As an example, the following Python program contains an error.

```mw
def a() -> int:
    i: int = 0
    j: int = b(i)
    return j

def b(z: int) -> int:
    k: int = 5
    if z == 0:
        c()
    return k + z

def c() -> None:
    error()

if __name__ == "__main__":
    a()
```

Running the program under the standard Python interpreter produces the following error message.

```mw
Traceback (most recent call last):
  File "file.py", line 16, in <module>
    a()
  File "file.py", line 3, in a
    j = b(i)
  File "file.py", line 9, in b
    c()
  File "file.py", line 13, in c
    error()
NameError: name 'error' is not defined
```

The stack trace shows where the error occurs, namely in the `c` function. It also shows that the `c` function was called by `b`, which was called by `a`, which was in turn called by the code on line 16 (the last line) of the program. The activation records for each of these three functions would be arranged in a stack such that the `a` function would occupy the bottom of the stack and the `c` function would occupy the top of the stack.

### Java

In Java, stack traces can be dumped manually with `java.lang.Thread::dumpStack()` Take the following input:

```mw
public class Main {
    static void demo() {
        demo1();
    }

    static void demo1() {
        demo2();
    }

    static void demo2() {
        demo3();
    }

    static void demo3() {
        Thread.dumpStack();
    }

    public static void main(String args[]) {
        demo();
    }
}
```

The exception lists functions in descending order, so the most-inner call is first.

```mw
java.lang.Exception: Stack trace
        at java.lang.Thread.dumpStack(Thread.java:1336)
        at Main.demo3(Main.java:15)
        at Main.demo2(Main.java:11)
        at Main.demo1(Main.java:7)
        at Main.demo(Main.java:3)
        at Main.main(Main.java:19)
```

Java also allows retrieving the current stack trace using `java.lang.Thread::getStackTrace()`, or displaying the stack trace at an error using `java.lang.Throwable::printStackTrace()`. A stack trace in Java is represented as `java.lang.StackTraceElement[]`, an array.

### C and C++

C does not have native support for obtaining stack traces, but libraries such as glibc provide this functionality.

In C and C++, some compiler optimizations may interfere with the call stack information that can be recovered at runtime. For instance, inlining can cause missing stack frames, tail call optimizations can replace one stack frame with another, and frame pointer elimination can prevent call stack analysis tools from correctly interpreting the contents of the call stack.

For example, glibc's `backtrace()` function returns an output with the program function and memory address.

```mw
./a.out() [0x40067f]
./a.out() [0x4006fe]
./a.out() [0x40070a]
/lib/x86_64-linux-gnu/libc.so.6(__libc_start_main+0xf5) [0x7f7e60738f45]
./a.out() [0x400599]
```

Prior to C++23, no mechanisms in C++ existed to obtain stack traces, but third-party libraries like *Boost.Stacktrace* offered stack traces. C++23 added stack traces with `std::stacktrace` and `std::stacktrace_entry` Stack traces can be dumped manually by printing the value returned by static member function `std::stacktrace::current()`:

```mw
import std;

using std::stacktrace;

void bar() {
    std::println("Stacktrace from bar():\n{}", stacktrace::current());
}

void foo() {
    bar();
}

int main() {
    foo();
}
```

### C

C# offers a `System.Diagnostics.StackTrace` class.

### Rust

Rust has two types of errors. Functions that use the panic macro are "unrecoverable" and the current thread will become poisoned experiencing stack unwinding. Functions that return a `std::result::Result` are "recoverable" and can be handled gracefully. However, recoverable errors cannot generate a stack trace as they are manually added and not a result of a runtime error.

As of June 2021, Rust has experimental support for stack traces on unrecoverable errors. Rust supports printing to stderr when a thread panics, but it must be enabled by setting the `RUST_BACKTRACE` environment variable.

When enabled, such backtraces look similar to below, with the most recent call first.

```mw
thread 'main' panicked at 'execute_to_panic', main.rs:3
stack backtrace:
   0: std::sys::imp::backtrace::tracing::imp::unwind_backtrace
   1: std::panicking::default_hook::{{closure}}
   2: std::panicking::default_hook
   3: std::panicking::rust_panic_with_hook
   4: std::panicking::begin_panic
   5: futures::task_impl::with
   6: futures::task_impl::park
...
```
