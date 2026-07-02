---
title: "Singleton pattern"
source: https://en.wikipedia.org/wiki/Singleton_pattern
domain: software-design
license: CC-BY-SA-4.0
tags: design pattern, software architecture, software design, refactoring
fetched: 2026-07-02
---

# Singleton pattern

In object-oriented programming, the **singleton pattern** is a software design pattern that restricts the instantiation of a class to a singular instance. It is one of the well-known "Gang of Four" design patterns, which describe how to solve recurring problems in object-oriented software. The pattern is useful when exactly one object is needed to coordinate actions across a system.

More specifically, the singleton pattern allows classes to:

- Ensure they only have one instance
- Provide easy access to that instance
- Control their instantiation (for example, hiding the constructors of a class)

The term comes from the mathematical concept of a singleton.

## Common uses

Singletons are often preferred to global variables because they do not pollute the global namespace (or their containing namespace). Additionally, they permit lazy allocation and initialization, whereas global variables in many languages will always consume resources.

The singleton pattern can also be used as a basis for other design patterns, such as the abstract factory, factory method, builder and prototype patterns. Facade objects are also often singletons because only one facade object is required.

Logging is a common real-world use case for singletons, because all objects that wish to log messages require a uniform point of access and conceptually write to a single source.

## Implementations

Implementations of the singleton pattern ensure that only one instance of the singleton class ever exists and typically provide global access to that instance.

Typically, this is accomplished by:

- Declaring all constructors of the class to be private, which prevents it from being instantiated by other objects
- Providing a static method that returns a reference to the instance

The instance is usually stored as a private static variable; the instance is created when the variable is initialized, at some point before when the static method is first called.

This C++23 implementation is based on the pre-C++98 implementation in the book .

```mw
import std;

class Singleton {
private:
    Singleton() = default; // no public constructor
    ~Singleton() = default; // no public destructor
    inline static Singleton* instance = nullptr; // declaration class variable
    int value;
public:
    // defines a class operation that lets clients access its unique instance.
    static Singleton& getInstance() {
        if (!instance) {
            instance = new Singleton();
        }
        return *instance;
    }
  
    Singleton(const Singleton&) = delete("Copy construction disabled");
    Singleton& operator=(const Singleton&) = delete("Copy assignment disabled");

    static void destroy() {
        delete instance;
        instance = nullptr;
    }

    // existing interface goes here
    [[nodiscard]]
    int getValue() const noexcept {
        return value;
    }

    void setValue(int newValue) noexcept {
        value = newValue;
    }
};

int main() {
    Singleton::getInstance().setValue(42);
    std::println("value = {}", Singleton::getInstance().getValue());
    Singleton::destroy();
}
```

The program output is

```mw
value=42
```

This is an implementation of the Meyers singleton in C++11. The Meyers singleton has no destruct method. The program output is the same as above.

```mw
import std;

class Singleton {
private:
    Singleton() = default;
    ~Singleton() = default;
    int value;
public:
    static Singleton& getInstance() {
        static Singleton instance;
        return instance;
    }
  
    [[nodiscard]]
    int getValue() const noexcept {
        return value;
    }
  
    void setValue(int newValue) noexcept {
        value = newValue;
    }
};

int main() {
    Singleton::getInstance().setValue(42);
    std::println("value = {}", Singleton::getInstance().getValue());
}
```

### Lazy initialization

A singleton implementation may use lazy initialization in which the instance is created when the static method is first invoked. In multithreaded programs, this can cause race conditions that result in the creation of multiple instances. The following Java 5+ example is a thread-safe implementation, using lazy initialization with double-checked locking.

```mw
public class Singleton {
    private static volatile Singleton instance = null;

    private Singleton() {}

    public static Singleton getInstance() {
        if (instance == null) {
            synchronized (Singleton.class) {
                if (instance == null) {
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }
}
```

## Criticism

Some consider the singleton to be an anti-pattern that introduces global state into an application, often unnecessarily. This introduces a potential dependency on the singleton by other objects, requiring analysis of implementation details to determine whether a dependency actually exists. This increased coupling can introduce difficulties with unit testing. In turn, this places restrictions on any abstraction that uses the singleton, such as preventing concurrent use of multiple instances.

Singletons also violate the single-responsibility principle because they are responsible for enforcing their own uniqueness along with performing their normal functions.
