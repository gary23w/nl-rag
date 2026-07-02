---
title: "Object lifetime"
source: https://en.wikipedia.org/wiki/Object_lifetime
domain: affine-types
license: CC-BY-SA-4.0
tags: affine type system, affine logic, move semantics, borrow checker
fetched: 2026-07-02
---

# Object lifetime

In object-oriented programming (OOP), **object lifetime** is the period of time between an object's creation and its destruction. In some programming contexts, object lifetime coincides with the lifetime of a variable that represents the object. In other contexts – where the object is accessed by reference – object lifetime is not determined by the lifetime of a variable. For example, destruction of the variable may only destroy the reference, not the referenced object.

## Determinism

Creation of an object is generally *deterministic*, but destruction varies by programming context. Some contexts allow for deterministic destruction, but some do not. Notably, in a garbage-collection environment, objects are destroyed when the garbage collector chooses.

The syntax for creation and destruction varies by programming context. In many contexts, including C++, C# and Java, an object is created via special syntax like `new *typename()*`. In C++, that provides manual memory management, an object is destroyed via the `delete` keyword. In C# and Java, with no explicit destruction syntax, the garbage collector destroys unused objects automatically.

An alternative and deterministic approach to automatic destruction is where the object is destroyed when code decrements the object's reference count to zero.

With an object pool, where objects may be created ahead of time and reused, the apparent creation and destruction of an object may not correspond to actual. The pool provides reinitialization for creation and finalization for destruction. Both creation and destruction may be non-deterministic.

Objects with static memory allocation have a lifetime that coincides with the run of a program, but the *order* of creation and destruction of the various static objects is generally non-deterministic.

## Life cycle

Object **life cycle** refers to the events that an object experiences including and between creation and destruction.

Life cycle generally includes memory management and operations after allocation and before deallocation. Object creation generally consists of *memory allocation* and *initialization* where initialization includes assigning values to fields and running initialization code. Object destruction generally consists of *finalization* (a.k.a. cleanup) and *memory deallocation* (a.k.a. free). These steps generally proceed in order as: allocate, initialize, finalize, deallocate.

Based on programming context, these steps may be partially or fully automated, and some of the steps can be customized.

The frequency of customization tends to vary by step and programming context. Initialization is the most commonly customized step. Finalization is common in languages with deterministic destruction, notably C++, but rare in garbage-collected languages. Allocation is rarely customized, and deallocation generally cannot be customized.

### Creation

The way to create objects varies across programming contexts. In some class-based languages, a *constructor* handles initialization. Like other methods, a constructor can be overloaded in order to support creating with different initial state.

### Destruction

Generally, an object is removed from memory after it is no longer needed. However, if there is sufficient memory or a program has a short run time, object destruction may not occur, memory simply being deallocated at process termination.

In some cases, object destruction consists solely of deallocating memory, particularly with garbage-collection, or if the object is a plain old data structure. In other cases, cleanup is performed prior to deallocation, particularly destroying member objects (in manual memory management), or deleting references from the object to other objects to decrement reference counts (in reference counting). This may be automatic, or a special destruction method may be called on the object.

In class-based languages with deterministic object lifetime, notably C++, a *destructor* is called when an instance is deleted, before the memory is deallocated. In C++, destructors differ from constructors in various ways. They cannot be overloaded, must have no arguments, need not maintain class invariants, and can cause program termination if they throw exceptions.

With garbage collection, objects may be destroyed when they can no longer be accessed by the program. The garbage-collector calls a *finalizer* before memory deallocation.

Destroying an object will cause any references to the object to become invalid. With manual memory management, any existing reference becomes a dangling reference. With garbage collection, objects are only destroyed when there are no references to them.

## Consistency

Object lifetime begins when allocation completes and ends when deallocation starts. Thus, during initialization and finalization, an object is alive, but may not be in a consistent state. The period between when initialization completes to when finalization starts is when the object is both alive and in a consistent state.

If creation or destruction fail, error reporting (for example, raising an exception) can be complicated since the object or related objects may be in an inconsistent state.

For a static variable, with lifespan coinciding with the program run, a creation or destruction error is problematic since program execution is before or after normal execution.

## Class-based programming

In class-based programming, object creation is also known as *instantiation* (creating an *instance* of a *class*). Creation and destruction can be customized via a *constructor* and a *destructor* and sometimes with separate *initializer* and *finalizer* methods.

Notably, a constructor is a class method as there is no object (instance) available until the object is created, but destructors, initializers, and finalizers are instance methods.

Further, constructors and initializers often can accept arguments, while destructors and finalizers generally do not as they are often implicitly callable.

## Resource management

In languages with deterministic lifetime objects, lifetime may be used to piggyback resource management. This is called the Resource Acquisition Is Initialization (RAII) idiom. Resources are acquired during initialization, and released during finalization. In languages with non-deterministic lifetime objects (i.e. garbage collected), the management of memory is generally kept separate from management of other resources.

## Examples

### C++

A C++ class can be declared with defaults as:

```mw
class Foo {
    // ...
};
```

When declared in an automatic context, the object is destroyed at the close of the block it is declared.

```mw
int bar() {
    Foo foo;
    // foo is destroyed here
}
```

When created dynamically, it lives until it is explicitly destroyed.

```mw
int bar() {
    Foo* foo = new Foo();
    delete foo;
}
```

When using smart pointers, its destruction semantics are controlled based on scope or shared references.

### Java

A Java class can be declared with defaults as:

```mw
class Foo {
    // ...
}
```

After an instance is created (i.e. `new Foo()`) it lives until it has no references and the garbage collector deletes it.

### Rust

Rust uses lifetime annotations to declare the lifetime of arguments passed into a function. The lifetime is declared in the function signature within angle brackets. In this example a reference to the struct File is passed into the example function with the lifetime annotation 'a.

```mw
fn example<'a>(file: &'a File) {
    // ...
}
```
