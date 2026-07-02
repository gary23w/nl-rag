---
title: "Thunk"
source: https://en.wikipedia.org/wiki/Thunk
domain: lazy-evaluation-theory
license: CC-BY-SA-4.0
tags: lazy evaluation, call by need, call by name, thunk (programming)
fetched: 2026-07-02
---

# Thunk

In computer programming, a **thunk** is a subroutine used to inject a calculation into another subroutine. Thunks are primarily used to delay a calculation until its result is needed, or to insert operations at the beginning or end of the other subroutine. They have many other applications in compiler code generation and modular programming.

The term originated as a whimsical irregular form of the verb *think*. It refers to the original use of thunks in ALGOL 60 compilers, which required special analysis (thought) to determine what type of routine to generate.

## Background

The early years of compiler research saw broad experimentation with different evaluation strategies. A key question was how to compile a subroutine call if the arguments can be arbitrary mathematical expressions rather than constants. One approach, known as "call by value", calculates all of the arguments before the call and then passes the resulting values to the subroutine. In the rival "call by name" approach, the subroutine receives the unevaluated argument expression and must evaluate it.

A simple implementation of "call by name" might substitute the code of an argument expression for each appearance of the corresponding parameter in the subroutine, but this can produce multiple versions of the subroutine and multiple copies of the expression code. As an improvement, the compiler can generate a helper subroutine, called a *thunk*, that calculates the value of the argument. The address and environment of this helper subroutine are then passed to the original subroutine in place of the original argument, where it can be called as many times as needed. Peter Ingerman first described thunks in reference to the ALGOL 60 programming language, which supports call-by-name evaluation.

## Applications

### Functional programming

Although the software industry largely standardized on call-by-value and call-by-reference evaluation, active study of call-by-name continued in the functional programming community. This research produced a series of lazy evaluation programming languages in which some variant of call-by-name is the standard evaluation strategy. Compilers for these languages, such as the Glasgow Haskell Compiler, have relied heavily on thunks, with the added feature that the thunks save their initial result so that they can avoid recalculating it; this is known as memoization or call-by-need.

Functional programming languages have also allowed programmers to explicitly generate thunks. This is done in source code by wrapping an argument expression in an anonymous function that has no parameters of its own. This prevents the expression from being evaluated until a receiving function calls the anonymous function, thereby achieving the same effect as call-by-name. The adoption of anonymous functions into other programming languages has made this capability widely available.

### Object-oriented programming

Thunks are useful in object-oriented programming platforms that allow a class to inherit multiple interfaces, leading to situations where the same method might be called via any of several interfaces. The following code illustrates such a situation in C++.

```mw
class A {
 public:
  virtual int Access() const { return value_; }

 private:
  int value_;
};

class B {
 public:
  virtual int Access() const { return value_; }

 private:
  int value_;
};

class C : public A, public B {
 public:
  int Access() const override { return better_value_; }

 private:
  int better_value_;
};

int use(B *b) { return b->Access(); }

int main() {
  // ...
  B some_b;
  use(&some_b);
  C some_c;
  use(&some_c);
}
```

In this example, the code generated for each of the classes A, B and C will include a dispatch table that can be used to call `Access` on an object of that type, via a reference that has the same type. Class C will have an additional dispatch table, used to call `Access` on an object of type C via a reference of type B. The expression `b->Access()` will use B's own dispatch table or the additional C table, depending on the type of object b refers to. If it refers to an object of type C, the compiler must ensure that C's `Access` implementation receives an instance address for the entire C object, rather than the inherited B part of that object.

As a direct approach to this pointer adjustment problem, the compiler can include an integer offset in each dispatch table entry. This offset is the difference between the reference's address and the address required by the method implementation. The code generated for each call through these dispatch tables must then retrieve the offset and use it to adjust the instance address before calling the method.

The solution just described has problems similar to the naïve implementation of call-by-name described earlier: the compiler generates several copies of code to calculate an argument (the instance address), while also increasing the dispatch table sizes to hold the offsets. As an alternative, the compiler can generate an *adjustor thunk* along with C's implementation of `Access` that adjusts the instance address by the required amount and then calls the method. The thunk can appear in C's dispatch table for B, thereby eliminating the need for callers to adjust the address themselves.

### Interoperability

Thunks have been widely used to provide interoperability between software modules whose routines cannot call each other directly. This may occur because the routines have different calling conventions, run in different CPU modes or address spaces, or at least one runs in a virtual machine. A compiler (or other tool) can solve this problem by generating a thunk that automates the additional steps needed to call the target routine, whether that is transforming arguments, copying them to another location, or switching the CPU mode. A successful thunk minimizes the extra work the caller must do compared to a normal call.

Much of the literature on interoperability thunks relates to various Wintel platforms, including MS-DOS, OS/2, Windows and .NET, and to the transition from 16-bit to 32-bit memory addressing. As customers have migrated from one platform to another, thunks have been essential to support legacy software written for the older platforms. UEFI CSM is another example to do thunk for legacy boot loaders.

The transition from 32-bit to 64-bit code on x86 also uses a form of thunking (WoW64). However, because the x86-64 address space is larger than the one available to 32-bit code, the old "generic thunk" mechanism could not be used to call 64-bit code from 32-bit code. The only case of 32-bit code calling 64-bit code is in the WoW64's thunking of Windows APIs to 32-bit.

### Overlays and dynamic linking

On systems that lack automatic virtual memory hardware, thunks can implement a limited form of virtual memory known as overlays. With overlays, a developer divides a program's code into segments that can be loaded and unloaded independently, and identifies the entry points into each segment. A segment that calls into another segment must do so indirectly via a branch table. When a segment is in memory, its branch table entries jump into the segment. When a segment is unloaded, its entries are replaced with "reload thunks" that can reload it on demand.

Similarly, systems that dynamically link modules of a program together at run-time can use thunks to connect the modules. Each module can call the others through a table of thunks that the linker fills in when it loads the module. This way the modules can interact without prior knowledge of where they are located in memory.
