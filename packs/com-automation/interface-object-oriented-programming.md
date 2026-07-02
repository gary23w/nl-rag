---
title: "Interface (object-oriented programming)"
source: https://en.wikipedia.org/wiki/Interface_(object-oriented_programming)
domain: com-automation
license: CC-BY-SA-4.0
tags: component object model, ole automation, distributed com, activex control
fetched: 2026-07-02
---

# Interface (object-oriented programming)

In object-oriented programming, an **interface** or **protocol type** is a data type that acts as an abstraction of a class. It describes a set of method signatures, the implementations of which may be provided by multiple classes that are otherwise not necessarily related to each other. A class which provides the methods listed in an interface is said to *implement* the interface, or to *adopt* the protocol.

Interfaces are useful for encapsulation and reducing coupling. For example, in Java, the `java.lang.Comparable<T>` interface specifies the method `compareTo()`. Thus, a sorting method only needs to take objects of types which implement `java.lang.Comparable<T>` to sort them, without knowing about the inner nature of the class (except that two of these objects can be compared via `compareTo()`).

## Examples

Some programming languages provide explicit language support for interfaces: Ada, C#, D, Dart, Delphi, Go, Java, Logtalk, Object Pascal, Objective-C, OCaml, PHP, Racket, Swift, Python 3.8. In languages supporting multiple inheritance, such as C++, interfaces are abstract classes.

In Java, an implementation of interfaces may look like:

```mw
class Animal { ... }
class Theropod extends Animal { ... }

interface Flyable {
    void fly();
}

interface Vocal {
    void vocalize();
}

public class Bird extends Theropod implements Flyable, Vocal {
    // ...
    public void fly() { ... }
    public void vocalize() { ... }
}
```

In languages without explicit support, interfaces are often still present as conventions; this is known as duck typing. For example, in Python, any class can implement an `__iter__` method and be used as an iterable. Classes may also explicitly subclass an ABC, such as `collections.abc.Iterable`.

Type classes in languages like Haskell, or module signatures in ML and OCaml, are used for many of the same things as are interfaces.

In Rust, interfaces are called *traits*. In Rust, a `struct` does not contain methods, but may add methods through separate `impl` blocks:

```mw
trait Pet {
    fn speak(&self);
}

struct Dog {
    // Structs only contain their fields
    name: String
}

impl Dog {
    // Not from a trait
    fn new(name: String) -> Self {
        Dog { name }
    }
}

impl Pet for Dog {
    // From a trait
    fn speak(&self) {
        println!("{} says 'Woof!'", self.name);
    }
}

fn main() {
    let dog = Dog::new(String::from("Arlo"));
    dog.speak();
}
```

In C++, there are multiple ways to resemble interfaces. One such way is the Java-style interface, which is done using abstract classes. The other, which resembles Go interfaces, is using concepts. Unlike inheritance, with concepts any type may satisfy a concept (not just classes) so long as it satisfies all of its requirements.
