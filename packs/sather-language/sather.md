---
title: "Sather"
source: https://en.wikipedia.org/wiki/Sather
domain: sather-language
license: CC-BY-SA-4.0
tags: sather language, iteration abstraction, category theory, object oriented programming, generic programming
fetched: 2026-07-02
---

# Sather

**Sather** is an object-oriented programming language. It originated circa 1990 at the International Computer Science Institute (ICSI) at the University of California, Berkeley, developed by an international team led by Steve Omohundro. It supports garbage collection and generics by subtypes.

Originally, it was based on Eiffel, but it has diverged, and now includes several functional programming features.

The name is inspired by Eiffel; the Sather Tower is a recognizable landmark at Berkeley, named after Jane Krom Sather, the widow of Peder Sather, who donated large sums to the foundation of the university.

Sather also takes inspiration from other programming languages and paradigms: iterators, design by contract, abstract classes, multiple inheritance, anonymous functions, operator overloading, contravariant type system.

The original Berkeley implementation (last stable version 1.1 was released in 1995, no longer maintained) has been adopted by the Free Software Foundation therefore becoming GNU Sather. Last stable GNU version (1.2.3) was released in July 2007 and the software is currently not maintained. There were several other variants: Sather-K from the University of Karlsruhe; Sather-W from the University of Waikato (implementation of Sather version 1.3); Peter Naulls' port of ICSI Sather 1.1 to RISC OS; and pSather, a parallel version of ICSI Sather addressing non-uniform memory access multiprocessor architectures but presenting a shared memory model to the programmer.

The former ICSI Sather compiler (now GNU Sather) is implemented as a compiler to C, i.e., the compiler does not output object or machine code, but takes Sather source code and generates C source code as an intermediate language. Optimizing is left to the C compiler.

The GNU Sather compiler, written in Sather itself, is dual licensed under the GNU GPL & LGPL.

## Hello World

```mw
 class HELLO_WORLD is
  main is 
   #OUT+"Hello World\n"; 
  end; 
 end;
```

A few remarks:

- Class names are ALL CAPS; this is not only a convention but it's enforced by the compiler.
- The method called `main` is the entry point for execution. It may belong to any class, but if this is different from `MAIN`, it must be specified as a compiler option.
- `#` is the constructor symbol: It calls the `create` method of the class whose name follows the operator. In this example, it's used for instantiating the `OUT` class, which is the class for the standard output.
- The `+` operator has been overloaded by the class to append the string passed as argument to the stream.
- Operators such as `+` are syntactic sugar for conventionally named method calls: `a + b` stands for `a.plus(b)`. The usual arithmetic precedence conventions are used to resolve the calling order of methods in complex formulae.

## Example of iterators

This program prints numbers from 1 to 10.

```mw
 class MAIN is
   main is
     loop
      i := 1.upto!(10);
      #OUT + i + "\n";
     end;
   end;
 end;
```

The `loop` ... `end` construct is the preferred means of defining loops, although `while` and `repeat`-`until` are also available. Within the construct, one or more iterators may be used. Iterator names always end with an exclamation mark. (This convention is enforced by the compiler.) `upto!` is a method of the `INT` class accepting one `once` argument, meaning its value won't change as the iterator yields. `upto!` could be implemented in the `INT` class with code similar to the following one.

```mw
  upto!(once m:INT):SAME is
    i: INT := self; -- initialise i to the value of self, 
                    -- that is the integer of which this method is called
    loop
      if i>m then 
        quit;  -- leave the loop when i goes beyond m
      end;
      yield i; -- else use i as return value and stay in the loop
      i := i + 1; -- and increment
    end;
  end;
```

Type information for variables is denoted by the postfix syntax `variable:CLASS`. The type can often be inferred and thus the typing information is optional, as in `anInteger::=1`. `SAME` is a pseudo-class referring to the current class.
