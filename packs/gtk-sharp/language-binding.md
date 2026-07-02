---
title: "Language binding"
source: https://en.wikipedia.org/wiki/Language_binding
domain: gtk-sharp
license: CC-BY-SA-4.0
tags: gtk sharp binding, mono gtk wrapper, dotnet gnome binding, managed widget wrapper
fetched: 2026-07-02
---

# Language binding

In programming and software design, a **binding** is an application programming interface (API) that provides glue code specifically made to allow a programming language to use a foreign library or operating system service (one that is not native to that language).

## Characteristics

Binding generally refers to a mapping of one thing to another. In the context of software libraries, bindings are wrapper libraries that bridge two programming languages, so that a library written for one language can be used in another language. Many software libraries are written in system programming languages such as C or C++. To use such libraries from another language, usually of higher-level, such as Java, Common Lisp, Scheme, Python, or Lua, a binding to the library must be created in that language, possibly requiring recompiling the language's code, depending on the amount of modification needed. However, most languages offer a foreign function interface, such as Python's and OCaml's `ctypes`, and Embeddable Common Lisp's `cffi` and `uffi`.

For example, Python bindings are used when an extant C library, written for some purpose, is to be used from Python. Another example is `libsvn` which is written in C to provide an API to access the Subversion software repository. To access Subversion from within Java code, `libsvnjavahl` can be used, which depends on `libsvn` being installed and acts as a bridge between the language Java and `libsvn`, thus providing an API that invokes functions from `libsvn` to do the work.

Major motives to create library bindings include software reuse, to reduce reimplementing a library in several languages, and the difficulty of implementing some algorithms efficiently in some high-level languages.

## Runtime environment

### Object models

- Common Object Request Broker Architecture (CORBA) – cross-platform-language model
- Component Object Model (COM) – Microsoft Windows only cross-language model
  - Distributed Component Object Model (DCOM) – extension enabling COM to work over networks
  - Cross Platform Component Object Model (XPCOM) – Mozilla applications cross-platform model
- Common Language Infrastructure – .NET Framework cross-platform-language model
- Freedesktop.org D-Bus – open cross-platform-language model

### Virtual machines

- Comparison of application virtual machines

## Porting

- Portable object – cross-platform-language object model definition
