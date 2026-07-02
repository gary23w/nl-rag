---
title: "Pony (programming language)"
source: https://en.wikipedia.org/wiki/Pony_(programming_language)
domain: pony-language
license: CC-BY-SA-4.0
tags: pony language, actor model, capability based security, reference capability, object capability model
fetched: 2026-07-02
---

# Pony (programming language)

**Pony** (also known as **ponylang**) is a object-oriented, actor model, capabilities-secure, high performance programming language. Pony's reference capabilities allow even mutable data to be safely passed by reference between actors. Garbage collection is performed concurrently, per-actor, which eliminates the need to pause program execution or "stop the world". Sylvan Clebsch is the original creator of the language. It is now being maintained and developed by members of the Pony team. It is free and open-source software with a BSD 2-clause license.

## History

The language was created by Sylvan Clebsch, while a PhD student at Imperial College London. His professor at that time was Sophia Drossopoulou, who is also well known for her contributions to computer programming, and as a lecturer. According to developers who have talked to Sylvan, he was frustrated with not having a high performance language that could run concurrent code securely, safely, and more simply.

## Language design

At its core, Pony is a systems language designed around safety and performance.

### Safety

- Type safety – Pony is a type safe language.
- Memory safety – There are no dangling pointers and no buffer overruns. There is no null but optional types can be safely represented using unions with the None type.
- Exception safety – There are no runtime exceptions. All exceptions have defined semantics and are always caught.
- Concurrency safety – The type system employs reference capabilities to ensure (at compile time) that there are no data races nor deadlocks.

### Performance

- Lock-free – By design, Pony avoids the need for traditional locking mechanisms, which eliminates the overhead and contention associated with locks.
- Native code – Pony is an ahead-of-time compiled language. There is no interpreter or virtual machine
- Concurrent garbage collection – Each actor's heap is collected separately and concurrently, avoiding the need to "stop the world" for global collection.

## Examples

### Hello, World

In Pony, instead of a main function, there is a main *actor*. The creation of this actor serves as the entry point into a Pony program, as in this "Hello, World!" program.

```mw
actor Main
  new create(env: Env) =>
    env.out.print("Hello, world!")
```

There are no global variables in Pony, meaning everything must be contained within an instance of a class or an actor. As such, even the environment that allows for printing to standard output is passed as a parameter.
