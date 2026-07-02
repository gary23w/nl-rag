---
title: "Mojo (programming language)"
source: https://en.wikipedia.org/wiki/Mojo_(programming_language)
domain: mojo-lang
license: CC-BY-SA-4.0
tags: mojo language, mojo lang, modular mojo
fetched: 2026-07-02
---

# Mojo (programming language)

**Mojo** is an in-development proprietary programming language based on Python available for Linux and macOS. Mojo aims to combine the usability of a high-level programming language, specifically Python, with the performance of a system programming language such as C++, Rust, and Zig.Modular, the company behind Mojo, has stated an intent to open source the Mojo language, committing to open-source Mojo in "fall 2026". In May 2026, Modular released the first beta of Mojo 1.0 and launched a website for the language. As of June 2026, the Mojo compiler is closed source with an open source standard library.

Mojo builds on the Multi-Level Intermediate Representation (MLIR) compiler software framework, instead of directly on the lower level LLVM compiler framework like many languages such as Julia, Swift, C++, and Rust. MLIR is a newer compiler framework that allows Mojo to exploit higher level compiler passes unavailable in LLVM alone, and allows Mojo to compile down and target more than only central processing units (CPUs), including producing code that can run on graphics processing units (GPUs), Tensor Processing Units (TPUs), application-specific integrated circuits (ASICs) and other accelerators. It can also often more effectively use certain types of CPU optimizations directly, like single instruction, multiple data (SIMD) with minor intervention by a developer, as occurs in many other languages. According to Jeremy Howard of fast.ai, Mojo can be seen as "syntax sugar for MLIR" and for that reason Mojo is well optimized for applications like artificial intelligence (AI).

## Origin and development history

The Mojo programming language was created by Modular Inc, which was founded by Chris Lattner, the original architect of the Swift programming language and LLVM, and Tim Davis, a former Google employee. The intention behind Mojo is to bridge the gap between Python’s ease of use and the fast performance required for cutting-edge AI applications.

According to public change logs, Mojo development goes back to 2022. In May 2023, the first publicly testable version was made available online via a hosted playground. By September 2023 Mojo was available for local download for Linux and by October 2023 it was also made available for download on Apple's macOS. The SDK included a command-line driver, a Visual Studio Code extension, and a Jupyter kernel.

In March 2024, Modular open sourced the Mojo standard library and started accepting community contributions under the Apache 2.0 license.

In December 2025, Modular published a roadmap toward a 1.0 release, stating that Mojo 1.0 would stabilize core language features and that additional features, such as a match statement and enums, would follow in 1.x releases. On May 7, 2026, Modular released Mojo 1.0.0 beta 1 and launched the language's website, mojolang.org.

## Features

Mojo was created for an easy transition from Python. The language has syntax similar to Python's, with inferred static typing, and allows users to import Python modules. It uses LLVM and MLIR as its compilation backend. Mojo programs can import and call Python modules via the CPython runtime, and Mojo functions can be called from Python through C-compatible bindings. The language is not source-compatible with Python 3. It does not support Python's class system; instead it provides struct types, memory-optimized alternatives to classes that support methods, fields, operator overloading, and decorators. Python-style list, set, and dictionary comprehensions are supported.

The language also provides a borrow checker, an influence from Rust. Function arguments are passed as immutable references by default (the read convention). Functions may instead declare arguments as mutable references (mut) or take ownership of them, and ownership can be transferred with the ^ operator.

While the Mojo standard library is open source under the Apache 2.0 license, the compiler is not; Modular has committed to open-sourcing it in fall 2026.

Mojo supports GPU programming through a gpu package in its standard library. A 2025 study by Oak Ridge National Laboratory researchers presented at the SC25 WACCPD workshop found Mojo's GPU kernels broadly competitive with CUDA and HIP for memory-bound workloads on Nvidia and AMD accelerators, while noting performance gaps for atomic operations and fast-math compute-bound workloads on AMD GPUs.

## Programming examples

Functions in Mojo are declared with def. Earlier versions also provided an fn keyword for stricter, statically typed functions; fn was deprecated in 2026 in favor of using def for all functions. Functions may declare typed parameters and return types:

```mw
def add(x: Int, y: Int) -> Int:
    """A typed addition."""
    return x + y
```

Variables may be declared explicitly with var, which gives block-level scope, or implicitly by assignment, which gives function-level scope matching Python's behavior:

```mw
def main():
    var total = add(1, 2)  # explicitly declared
    doubled = total * 2    # implicitly declared
    print(doubled)
```

Mojo originally included a let keyword for immutable bindings; it was removed from the language in 2024.

Structs are Mojo's compile-time-laid-out alternative to Python classes. The @fieldwise_init decorator synthesizes a constructor from the declared fields, and traits such as Copyable declare supported behaviors:

```mw
@fieldwise_init
struct Point(Copyable, Movable):
    var x: Int
    var y: Int

    def magnitude_squared(self) -> Int:
        return self.x * self.x + self.y * self.y

def main():
    p = Point(3, 4)
    print(p.magnitude_squared())  # 25
```

Mojo programs can import and use Python modules through the CPython runtime:

```mw
from std.python import Python

def main() raises:
    math = Python.import_module("math")
    print(math.sqrt(2.0))
```
