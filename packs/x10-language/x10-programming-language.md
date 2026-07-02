---
title: "X10 (programming language)"
source: https://en.wikipedia.org/wiki/X10_(programming_language)
domain: x10-language
license: CC-BY-SA-4.0
tags: x10 language, high performance computing, concurrent computing, partitioned global address space, parallel computing
fetched: 2026-07-02
---

# X10 (programming language)

**X10** is a programming language being developed by IBM at the Thomas J. Watson Research Center as part of the Productive, Easy-to-use, Reliable Computing System (PERCS) project funded by DARPA's High Productivity Computing Systems (HPCS) program.

## History

Its primary authors are Kemal Ebcioğlu, Saravanan Arumugam (Aswath), Vijay Saraswat, and Vivek Sarkar.

X10 is designed specifically for parallel computing using the partitioned global address space (PGAS) model. A computation is divided among a set of *places*, each of which holds some data and hosts one or more *activities* that operate on those data. It has a constrained type system for object-oriented programming, a form of dependent types. Other features include user-defined primitive *struct* types; globally distributed *arrays*, and structured and unstructured parallelism.

X10 uses the concept of parent and child relationships for activities to prevent the lock stalemate that can occur when two or more processes wait for each other to finish before they can complete. An activity may spawn one or more child activities, which may themselves have children. Children cannot wait for a parent to finish, but a parent can wait for a child using the *finish* command.

## Example code

### Hello, World!

An X10 "Hello, World!" program:

```mw
/** Example file for the X10 programming language (http://x10-lang.org).
 */
class Example {
    public static def main(Rail[String]) {
        Console.OUT.println("Hello, World!"); // say hello.
    }
}
```
