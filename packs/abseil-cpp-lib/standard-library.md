---
title: "Standard library"
source: https://en.wikipedia.org/wiki/Standard_library
domain: abseil-cpp-lib
license: CC-BY-SA-4.0
tags: abseil library, cpp common libraries, abseil augmented standard library, abseil flat hash map
fetched: 2026-07-02
---

# Standard library

In computer programming, a **standard library** is the library made available across implementations of a programming language. Often, a standard library is specified by its associated programming language specification, however, some are set in part or whole by more informal practices of a language community.

Some languages define a core part of the standard library that must be made available in all implementations while allowing other parts to be implemented optionally.

In many languages, the standard library often has its own namespace. For example, C++, D, and Rust use `std::*` as the standard library namespace. C# uses `System.*`, while Java uses `java.*`, `javax.*` and `jdk.*`. However, in some like Python and Go, there is no "standard library namespace" or common prefix for modules belonging to the standard library.

As defined with the core language aspects, the line between the core language and its standard library is relatively subtle. A programmer may confuse the two aspects even though the language designers intentionally separate the two.

The line between the core language and its standard library is further blurred in some languages by defining core language constructs in terms of its standard library. For example, Java defines a string literal as an instance of the `java.lang.String` class. Smalltalk defines an anonymous function expression (a "block") as an instance of its library's `BlockContext` class. Scheme does not specify which portions must be implemented as core language vs. standard library.

Depending on the constructs available in the core language, a standard library may include:

- Subroutines
- Macro definitions
- Global variables
- Class definitions
- Templates

Commonly provided functionality includes:

- Algorithms, such as sorting algorithms
- Data structures, such as the list, tree, and hash table
- Interaction with external systems (input/output)
- Interaction with the host operating system

## Philosophies

Philosophies of standard library design vary widely. For example, Bjarne Stroustrup, designer of C++, writes:

> What ought to be in the standard C++ library? One ideal is for a programmer to be able to find every interesting, significant, and reasonably general class, function, template, etc., in a library. However, the question here is not, "What ought to be in *some* library?" but "What ought to be in the *standard* library?" The answer "Everything!" is a reasonable first approximation to an answer to the former question but not the latter. A standard library is something every implementer must supply so that every programmer can rely on it.

This suggests a relatively small standard library, containing only the constructs that "every programmer" might reasonably require when building a large collection of software. This is the philosophy that is used in the C and C++ standard libraries. As a result, the C standard library and C++ Standard Library are significantly smaller in size and scope compared to, for instance, the Java standard library and C# standard library, which feature more extensive abilities.

By contrast, Guido van Rossum, designer of Python, has embraced a much more inclusive vision of the standard library. Python attempts to offer an easy-to-code, object-oriented, high-level language. In the Python tutorial, he writes:

> Python has a "batteries included" philosophy. This is best seen through the sophisticated and robust capabilities of its larger packages.

Van Rossum goes on to list libraries for processing XML, XML-RPC, email messages, and localization, facilities that the C++ Standard Library omits. This other philosophy is often found in scripting languages (as in Python or Ruby) or languages that use a virtual machine, such as Java or the .NET Framework languages. In C++, such facilities are not part of the standard library, but instead are included in other libraries, such as Boost or POCO. In Java, the formerly standard libraries Java Platform, Enterprise Edition (now Jakarta EE) and JavaFX were moved to separate independent libraries.

## Examples

- C standard library
- C++ Standard Library
- .NET Framework Class Library (FCL)
- Java Class Library (JCL)
- Rust standard library
- Factor standard library
- Ruby standard library
- Python standard library
- Common Language Infrastructure (CLI) standard libraries
