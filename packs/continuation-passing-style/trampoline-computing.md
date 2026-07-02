---
title: "Trampoline (computing)"
source: https://en.wikipedia.org/wiki/Trampoline_(computing)
domain: continuation-passing-style
license: CC-BY-SA-4.0
tags: continuation passing style, call-with-current-continuation, tail call, administrative normal form
fetched: 2026-07-02
---

# Trampoline (computing)

In computer programming, the word **trampoline** has a number of meanings, and is generally associated with jump instructions (i.e. moving to different code paths).

## Low-level programming

Trampolines (sometimes referred to as indirect jump vectors) are memory locations holding addresses pointing to interrupt service routines, I/O routines, etc. Execution jumps into the trampoline and then immediately jumps out, or bounces, hence the term *trampoline*. They have many uses:

- Trampoline can be used to overcome the limitations imposed by a central processing unit (CPU) architecture that expects to always find vectors in fixed locations.
- When an operating system is booted on a symmetric multiprocessing (SMP) machine, only one processor, the bootstrap processor, will be active. After the operating system has configured itself, it will instruct the other processors to jump to a piece of trampoline code that will initialize the processors and wait for the operating system to start scheduling threads on them.

## High-level programming

- As used in some Lisp implementations, a trampoline is a loop that iteratively invokes thunk-returning functions (continuation-passing style). A single trampoline suffices to express all control transfers of a program; a program so expressed is trampolined, or in *trampolined style*; converting a program to trampolined style is trampolining. Programmers can use trampolined functions to implement tail-recursive function calls in stack-oriented programming languages.
- In Java, *trampoline* refers to using reflection to avoid using inner classes, for example in event listeners. The time overhead of a reflection call is traded for the space overhead of an inner class. Trampolines in Java usually involve the creation of a *GenericListener* to pass events to an outer class.
- In Mono Runtime, trampolines are small, hand-written pieces of assembly code used to perform various tasks.
- When interfacing pieces of code with incompatible calling conventions, a trampoline is used to convert the caller's convention into the callee's convention.
  - In embedded systems, trampolines are short snippets of code that start up other snippets of code. For example, rather than write interrupt handlers entirely in assembly language, another option is to write interrupt handlers mostly in C, and use a short trampoline to convert the assembly-language interrupt calling convention into the C calling convention.
  - When passing a callback to a system that expects to call a C function, but one wants it to execute the method of a particular instance of a class written in C++, one uses a short *trampoline* to convert the C function-calling convention to the C++ method-calling convention. One way of writing such a trampoline is to use a thunk. Another method is to use a *generic listener*.
- In Objective-C, a trampoline is an object returned by a method that captures and reifies all messages sent to it and then "bounces" those messages on to another object, for example in higher order messaging.
- In the GCC compiler, trampoline refers to a technique for implementing pointers to nested functions when `-ftrampolines` option is enabled. The trampoline is a small piece of code which is constructed on the fly on the stack when the address of a nested function is taken. The trampoline sets up the static link pointer, which allows the nested function to access local variables of the enclosing function. The function pointer is then simply the address of the trampoline. This avoids having to use "fat" function pointers for nested functions which carry both the code address and the static link. This, however, conflicts with the desire to make the stack non-executable for security reasons.
- In the esoteric programming language Befunge, a trampoline is an instruction to skip the next cell in the control flow.

## No-execute stacks

Some implementations of trampolines cause a loss of no-execute stacks (NX stack). In the GNU Compiler Collection (GCC) in particular, a nested function builds a trampoline on the stack at runtime, and then calls the nested function through the data on stack. The trampoline requires the stack to be executable.

No-execute stacks and nested functions are mutually exclusive under GCC. If a nested function is used in the development of a program, then the NX stack is silently lost. GCC offers the `-Wtrampolines` warning to alert of the condition.

Software engineered using secure development lifecycle often do not allow the use of nested functions due to the loss of NX stacks.
