---
title: "Iterator pattern"
source: https://en.wikipedia.org/wiki/Iterator_pattern
domain: software-design
license: CC-BY-SA-4.0
tags: design pattern, software architecture, software design, refactoring
fetched: 2026-07-02
---

# Iterator pattern

In object-oriented programming, the **iterator pattern** is a design pattern in which an iterator is used to traverse a container and access the container's elements. The iterator pattern decouples algorithms from containers; in some cases, algorithms are necessarily container-specific and thus cannot be decoupled.

For example, the hypothetical algorithm `searchForElement()` can be implemented generally using a specified type of iterator rather than implementing it as a container-specific algorithm. This allows `searchForElement()` to be used on any container that supports the required type of iterator.

## Overview

The Iterator design pattern is one of the 23 well-known *"Gang of Four" design patterns* that describe how to solve recurring design problems to design flexible and reusable object-oriented software, that is, objects that are easier to implement, change, test, and reuse.

### What problems can the Iterator design pattern solve?

- The elements of an aggregate object should be accessed and traversed without exposing its representation (data structures).
- New traversal operations should be defined for an aggregate object without changing its interface.

Defining access and traversal operations in the aggregate interface is inflexible because it commits the aggregate to particular access and traversal operations and makes it impossible to add new operations later without having to change the aggregate interface.

### What solution does the Iterator design pattern describe?

- Define a separate (iterator) object that encapsulates accessing and traversing an aggregate object.
- Clients use an iterator to access and traverse an aggregate without knowing its representation (data structures).

Different iterators can be used to access and traverse an aggregate in different ways. New access and traversal operations can be defined independently by defining new iterators.

See also the UML class and sequence diagram below.

## Definition

The essence of the Iterator Pattern is to "Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation.".

## Structure

### UML class and sequence diagram

In the above UML class diagram, the `Client` class refers (1) to the `Aggregate` interface for creating an `Iterator` object (`createIterator()`) and (2) to the `Iterator` interface for traversing an `Aggregate` object (`next()`, `hasNext()`). The `Iterator1` class implements the `Iterator` interface by accessing the `Aggregate1` class.

The UML sequence diagram shows the run-time interactions: The `Client` object calls `createIterator()` on an `Aggregate1` object, which creates an `Iterator1` object and returns it to the `Client`. The `Client` uses then `Iterator1` to traverse the elements of the `Aggregate1` object.

### UML class diagram

## Example

Some languages standardize syntax. C++ and Python are notable examples.

### C++

C++ implements iterators with the semantics of pointers in that language. In C++, a class can overload all of the pointer operations, so an iterator can be implemented that acts more or less like a pointer, complete with dereference, increment, and decrement. This has the advantage that C++ algorithms such as `std::sort` can immediately be applied to plain old memory buffers, and that there is no new syntax to learn. However, it requires an "end" iterator to test for equality, rather than allowing an iterator to know that it has reached the end. In C++ language, we say that an iterator models the iterator concept.

This C++23 implementation is based on chapter "Generalizing vector yet again".

```mw
import std;

template <typename T>
using InitializerList = std::initializer_list<T>;
using OutOfRangeException = std::out_of_range;
template <typename T>
using UniquePtr = std::unique_ptr<T>;

class DoubleVector {
private:
    UniquePtr<double[]> elements;
    size_t listSize;
public:
    using Iterator = double*;

    [[nodiscard]]
    Iterator begin() const noexcept { 
        return elements; 
    }

    [[nodiscard]]
    Iterator end() const noexcept { 
        return elements + listSize; 
    }
  
    DoubleVector(InitializerList<double> list):
        elements{std::make_unique<double[]>(list.size())}, listSize{list.size()} {
        double* p = elements;
        for (auto i = list.begin(); i != list.end(); ++i, ++p) {
            *p = *i;
        }
        // alternatively implemented with
        // std::ranges::copy(list, elements.get())
    }  

    ~DoubleVector() = default;

    [[nodiscard]]
    size_t size() const noexcept { 
        return listSize; 
    }

    [[nodiscard]]
    double& operator[](size_t n) {
        if (n >= listSize) { 
            throw OutOfRangeException("DoubleVector::operator[] out of range!");
        }
        return elements[n];
    }

    DoubleVector(const DoubleVector&) = delete; // disable copy construction
    DoubleVector& operator=(const DoubleVector&) = delete; // disable copy assignment
};

int main(int argc, char* argv[]) {
    DoubleVector v = {1.1 * 1.1, 2.2 * 2.2};
  
    for (const double& x : v) {
        std::println("{}", x);
    }
    for (size_t i = v.begin(); i != v.end(); ++i) {
        std::println("{}", *i);
    }
    for (size_t i = 0; i <= v.size(); ++i) {
        std::println("{}", v[i]);
    } 
}
```

The program output is

```mw
1.21
4.84
1.21
4.84
1.21
4.84
terminate called after throwing an instance of 'OutOfRangeException'
  what():  DoubleVector::operator[] out of range!
```
