---
title: "Smart pointer"
source: https://en.wikipedia.org/wiki/Smart_pointer
domain: boost-cpp-lib
license: CC-BY-SA-4.0
tags: boost libraries, cpp peer-reviewed library, boost header only, boost smart pointers
fetched: 2026-07-02
---

# Smart pointer

In computer science, a **smart pointer** is an abstract data type that simulates a pointer while providing added features, such as automatic memory management or bounds checking. Such features are intended to reduce bugs caused by the misuse of pointers, while retaining efficiency. Smart pointers typically keep track of the memory they point to, and may also be used to manage other resources, such as network connections and file handles. Smart pointers were first popularized in the programming language C++ during the first half of the 1990s as rebuttal to criticisms of C++'s lack of automatic garbage collection. Rust, which avoids raw pointers and uses ownership to dictate lifetimes, also has smart pointers.

Pointer misuse can be a major source of bugs. Smart pointers prevent most situations of memory leaks by making the memory deallocation automatic. More generally, they make object destruction automatic: an object controlled by a smart pointer is automatically destroyed (finalized and then deallocated) when the last (or only) owner of an object is destroyed, for example because the owner is a local variable, and execution leaves the variable's scope. Smart pointers also eliminate dangling pointers by postponing destruction until an object is no longer in use.

If a language supports automatic garbage collection (for example, Java or C#), then smart pointers are unneeded for reclaiming and safety aspects of memory management, yet are useful for other purposes, such as cache data structure residence management and resource management of objects such as file handles or network sockets. Java, although not having a pointer API, has similar concepts for dealing with references.

Several types of smart pointers exist. Some work with reference counting, others by assigning ownership of an object to one pointer.

## History

Even though C++ popularized the concept of smart pointers, especially the reference-counted variety, the immediate predecessor of one of the languages that inspired C++'s design had reference-counted references built into the language. C++ was inspired in part by Simula67. Simula67's ancestor was Simula I. Insofar as Simula I's *element* is analogous to C++'s pointer without *null*, and insofar as Simula I's process with a dummy-statement as its activity body is analogous to C++'s *struct* (which itself is analogous to C. A. R. Hoare's *record* in then-contemporary 1960s work), Simula I had reference counted elements (i.e., pointer-expressions that house indirection) to processes (i.e., records) no later than September 1965, as shown in the quoted paragraphs below.

> Processes can be referenced individually. Physically, a process reference is a pointer to an area of memory containing the data local to the process and some additional information defining its current state of execution. However, for reasons stated in the Section 2.2 process references are always indirect, through items called *elements.* Formally a reference to a process is the value of an expression of type *element*. … *element* values can be stored and retrieved by assignments and references to *element* variables and by other means. The language contains a mechanism for making the attributes of a process accessible from the outside, i.e., from within other processes. This is called remote accessing. A process is thus a referenceable data structure.
> 
> It is worth noticing the similarity between a process whose activity body is a dummy statement, and the record concept recently proposed by C. A. R. Hoare and N. Wirth

Because C++ borrowed Simula's approach to memory allocation—the *new* keyword when allocating a process/record to obtain a fresh *element* to that process/record—it is not surprising that C++ eventually resurrected Simula's reference-counted smart-pointer mechanism within *element* as well.

## Features

In C++, a smart pointer is implemented as a template class that mimics, by means of operator overloading, the behaviors of a traditional (raw) pointer, (e.g. dereferencing, assignment) while providing additional memory management features.

Smart pointers can facilitate intentional programming by expressing, in the type, how the memory of the referent of the pointer will be managed. For example, if a C++ function returns a pointer, there is no way to know whether the caller should delete the memory of the referent when the caller is finished with the information.

```mw
SomeType* ambiguousFunction();  // What should be done with the result?
```

Traditionally, naming conventions have been used to resolve the ambiguity, which is an error-prone, labor-intensive approach. C++11 introduced a way to ensure correct memory management in this case by declaring the function to return a `std::unique_ptr`,

```mw
unique_ptr<SomeType> obviousFunction();
```

The declaration of the function return type as a `unique_ptr` makes explicit the fact that the caller takes ownership of the result, and the C++ runtime ensures that the memory will be reclaimed automatically. Before C++11, `unique_ptr` can be replaced with auto_ptr, which is now deprecated.

## Creating new objects

To ease the allocation of a `std::shared_ptr<SomeType>`, C++11 introduced:

```mw
shared_ptr<SomeType> s = std::make_shared<SomeType>(constructor, parameters, here);
```

and similarly `std::unique_ptr<SomeType>`, since C++14 one can use:

```mw
unique_ptr<SomeType> u = std::make_unique<SomeType>(constructor, parameters, here);
```

It is preferred, in almost all circumstances, to use these facilities over the `new` keyword.

## Unique pointers

C++11 introduces `std::unique_ptr`, defined in the header `<memory>`.

A `unique_ptr` is a container for a raw pointer, which the `unique_ptr` is said to own. A `unique_ptr` explicitly prevents copying of its contained pointer (as would happen with normal assignment), but the `std::move` function can be used to transfer ownership of the contained pointer to another `unique_ptr`. A `unique_ptr` cannot be copied because its copy constructor and assignment operators are explicitly deleted.

```mw
import std;

using std::unique_ptr;

unique_ptr<int> p1(new int(5));
unique_ptr<int> p2 = p1;  // Compile error.
unique_ptr<int> p3 = std::move(p1);  // Transfers ownership. p3 now owns the memory and p1 is set to nullptr.

p3.reset();  // Deletes the memory.
p1.reset();  // Does nothing.
```

`std::auto_ptr` is deprecated under C++11 and completely removed from C++17. The copy constructor and assignment operators of `auto_ptr` do not actually copy the stored pointer. Instead, they transfer it, leaving the prior `auto_ptr` object empty. This was one way to implement strict ownership, so that only one `auto_ptr` object can own the pointer at any given time. This means that `auto_ptr` should not be used where copy semantics are needed. Since `auto_ptr` already existed with its copy semantics, it could not be upgraded to be a move-only pointer without breaking backward compatibility with existing code.

The Rust equivalent of unique pointers is `std::boxed::Box`, which has unique ownership of a heap allocated object. In previous versions of Rust, there was also a `std::ptr::Unique` that wrapped around raw non-null `*mut T`.

It is possible to use "smart void pointers" using `std::unique_ptr`, using its second template parameter `Deleter`, which stores a type of a deallocator.

```mw
using std::unique_ptr;

struct MyDeleter {
    void operator()(void* p) const {
        delete static_cast<int*>(p);
    }
};

int main() {
    unique_ptr<void, MyDeleter> myPointer(new int(42), MyDeleter());
}
```

## Shared pointers and weak pointers

C++11 introduces `std::shared_ptr` and `std::weak_ptr`, defined in the header `<memory>`. C++11 also introduces `std::make_shared` (`std::make_unique` was introduced in C++14) to safely allocate dynamic memory in the RAII paradigm.

A `shared_ptr` is a container for a raw pointer. It maintains reference counting ownership of its contained pointer in cooperation with all copies of the `shared_ptr`. An object referenced by the contained raw pointer will be destroyed when and only when all copies of the `shared_ptr` have been destroyed.

```mw
import std;

using std::shared_ptr;

shared_ptr<int> p0(new int(5)); // Valid, allocates 1 integer and initialize it with value 5.
shared_ptr<int[]> p1(new int[5]); // Valid, allocates 5 integers.
shared_ptr<int[]> p2 = p1; // Both now own the memory.

p1.reset(); // Memory still exists, due to p2.
p2.reset(); // Frees the memory, since no one else owns the memory.
```

A `weak_ptr` is a container for a raw pointer. It is created as a copy of a `shared_ptr`. The existence or destruction of `weak_ptr` copies of a `shared_ptr` have no effect on the `shared_ptr` or its other copies. After all copies of a `shared_ptr` have been destroyed, all `weak_ptr` copies become empty.

```mw
import std;

using std::shared_ptr;
using std::weak_ptr;

shared_ptr<int> p1 = std::make_shared<int>(5);
weak_ptr<int> wp1{p1};  // p1 owns the memory.

{
    shared_ptr<int> p2 = wp1.lock();  // Now p1 and p2 own the memory.
    // p2 is initialized from a weak pointer, so you have to check if the
    // memory still exists!
    if (p2) {
        useSomePointer(p2);
    }
}
// p2 is destroyed. Memory is owned by p1.

p1.reset();  // Free the memory.

shared_ptr<int> p3 = wp1.lock(); 
// Memory is gone, so we get an empty shared_ptr.
if (p3) {  // code will not execute
    useLivePointer(p3);
}
```

Because the implementation of `shared_ptr` uses reference counting, circular references are potentially a problem. A circular `shared_ptr` chain can be broken by changing the code so that one of the references is a `weak_ptr`.

Multiple threads can safely simultaneously access different `shared_ptr` and `weak_ptr` objects that point to the same object.

The referenced object must be protected separately to ensure thread safety.

`shared_ptr` and `weak_ptr` are based on versions used by the Boost libraries. C++ Technical Report 1 (TR1) first introduced them to the standard, as general utilities, but C++11 adds more functions, in line with the Boost version.

In Java, every object is effectively a shared reference, and the Java Virtual Machine (JVM) tracks object reachability. Rust has two kinds of shared pointers, `std::rc::Rc` (reference-counted, single-threaded) and `std::sync::Arc` (atomically reference-counted, thread-safe).

Java has an equivalent concept to weak pointers, `java.lang.ref.WeakReference` (implementing a weak reference), which does not increase the reference count of an object, and can check that an object still lives using `WeakReference::get`. Java similarly has the `java.lang.ref.PhantomReference` (implementing a phantom reference), used with a `java.lang.ref.ReferenceQueue`, for performing cleanup actions after an object is garbage collected, but prior to finalisation. Unlike `WeakReference`), `PhantomReference` cannot actually access the object. `java.lang.ref.SoftReference`, on the other hand, are cleared according to the discretion of the garbage collector. Rust has a `std::rc::Weak` for a weak, non-owning reference which is created from an `Rc` or `Arc` by using `downgrade()`.

## Hazard pointers

Starting in C++26, there is a new pointer defined in `<hazard_pointer>`, the hazard pointer (`std::hazard_pointer`). It is a single-writer multi-reader pointer that can be owned by at most one thread at any point in time.

The hazard pointer had existed already previously in some third-party libraries.

## Other types of smart pointers

There are other types of smart pointers (which are not in the C++ standard) implemented on popular C++ libraries or custom STL, some examples include the intrusive pointer.
