---
title: "Flyweight pattern"
source: https://en.wikipedia.org/wiki/Flyweight_pattern
domain: software-design
license: CC-BY-SA-4.0
tags: design pattern, software architecture, software design, refactoring
fetched: 2026-07-02
---

# Flyweight pattern

In computer programming, the **flyweight** software design pattern refers to an object that minimizes memory usage by sharing some of its data with other similar objects. The flyweight pattern is one of twenty-three *GoF design patterns*.

In other contexts, the idea of sharing data structures is called hash consing.

The concept was coined and first extensively explored by Paul Calder and Mark Linton in 1990 to efficiently handle glyph information in a WYSIWYG document editor. Similar techniques were already used in other systems, however, as early as 1988.

## Overview

The flyweight pattern is useful when dealing with a large number of objects that share simple repeated elements which would use a large amount of memory if they were individually embedded. It is common to hold shared data in external data structures and pass it to the objects temporarily when they are used.

A classic example are the data structures used representing characters in a word processor. Naively, each character in a document might have a glyph object containing its font outline, font metrics, and other formatting data. However, this would use hundreds or thousands of bytes of memory for each character. Instead, each character can have a reference to a glyph object shared by every instance of the same character in the document. This way, only the position of each character needs to be stored internally.

As a result, flyweight objects can:

- store *intrinsic* state that is invariant, context-independent and shareable (for example, the code of character 'A' in a given character set)
- provide an interface for passing in *extrinsic* state that is variant, context-dependent and can't be shared (for example, the position of character 'A' in a text document)

Clients can reuse `Flyweight` objects and pass in extrinsic state as necessary, reducing the number of physically created objects.

### Structure

The above UML class diagram shows:

- the `Client` class, which uses the flyweight pattern
- the `FlyweightFactory` class, which creates and shares `Flyweight` objects
- the `Flyweight` interface, which takes in extrinsic state and performs an operation
- the `Flyweight1` class, which implements `Flyweight` and stores intrinsic state

The sequence diagram shows the following run-time interactions:

1. The `Client` object calls `getFlyweight(key)` on the `FlyweightFactory`, which returns a `Flyweight1` object.
2. After calling `operation(extrinsicState)` on the returned `Flyweight1` object, the `Client` again calls `getFlyweight(key)` on the `FlyweightFactory`.
3. The `FlyweightFactory` returns the already-existing `Flyweight1` object.

## Implementation details

There are multiple ways to implement the flyweight pattern. One example is mutability: whether the objects storing extrinsic flyweight state can change.

Immutable objects are easily shared, but require creating new extrinsic objects whenever a change in state occurs. In contrast, mutable objects can share state. Mutability allows better object reuse via the caching and re-initialization of old, unused objects. Sharing is usually nonviable when state is highly variable.

Other primary concerns include retrieval (how the end-client accesses the flyweight), caching and concurrency.

### Retrieval

The factory interface for creating or reusing flyweight objects is often a facade for a complex underlying system. For example, the factory interface is commonly implemented as a singleton to provide global access for creating flyweights.

Generally speaking, the retrieval algorithm begins with a request for a new object via the factory interface.

The request is typically forwarded to an appropriate cache based on what kind of object it is. If the request is fulfilled by an object in the cache, it may be reinitialized and returned. Otherwise, a new object is instantiated. If the object is partitioned into multiple extrinsic sub-components, they will be pieced together before the object is returned.

### Caching

There are two ways to cache flyweight objects: maintained and unmaintained caches.

Objects with highly variable state can be cached with a FIFO structure. This structure maintains unused objects in the cache, with no need to search the cache.

In contrast, unmaintained caches have less upfront overhead: objects for the caches are initialized in bulk at compile time or startup. Once objects populate the cache, the object retrieval algorithm might have more overhead associated than the push/pop operations of a maintained cache.

When retrieving extrinsic objects with immutable state one must simply search the cache for an object with the state one desires. If no such object is found, one with that state must be initialized. When retrieving extrinsic objects with mutable state, the cache must be searched for an unused object to reinitialize if no used object is found. If there is no unused object available, a new object must be instantiated and added to the cache.

Separate caches can be used for each unique subclass of extrinsic object. Multiple caches can be optimized separately, associating a unique search algorithm with each cache. This object caching system can be encapsulated with the chain of responsibility pattern, which promotes loose coupling between components.

### Concurrency

Special consideration must be taken into account where flyweight objects are created on multiple threads. If the list of values is finite and known in advance, the flyweights can be instantiated ahead of time and retrieved from a container on multiple threads with no contention. If flyweights are instantiated on multiple threads, there are two options:

1. Make flyweight instantiation single-threaded, thus introducing contention and ensuring one instance per value.
2. Allow concurrent threads to create multiple flyweight instances, thus eliminating contention and allowing multiple instances per value.

To enable safe sharing between clients and threads, flyweight objects can be made into immutable value objects, where two instances are considered equal if their values are equal.

## Examples

### C

In this example, every instance of the `MyObject` class uses a `Pointer` class to provide data.

```mw
// Defines Flyweight object that repeats itself.
public class Flyweight
{
    public string Name { get; set; }
    public string Location { get; set; }
    public string Website { get; set; }
    public byte[] Logo { get; set; }
}

public static class Pointer
{
    public static readonly Flyweight Company = new Flyweight { Name = "ABC", Location = "XYZ", Website = "www.example.com" };
}

public class MyObject
{
    public string Name { get; set; }
    public string Company => Pointer.Company.Name;
}
```

### C++

The C++ Standard Template Library provides several containers that allow unique objects to be mapped to a key. The use of containers helps further reduce memory usage by removing the need for temporary objects to be created.

```mw
import std;

template <typename K, typename V>
using TreeMap = std::map<K, V>;
using String = std::string;
using StringView = std::string_view;
template <typename K, typename V>
using HashMap = std::unordered_map<K, V>;

// Instances of Tenant will be the Flyweights
class Tenant {
private:
    const String name;
public:
    explicit Tenant(StringView name): 
        name{name} {}

    [[nodiscard]]
    String getName() const noexcept {
        return name;
    }
};

// Registry acts as a factory and cache for Tenant flyweight objects
class Registry {
private:
    HashMap<String, Tenant> tenants;
public:
    Registry() = default;

    [[nodiscard]]
    Tenant& findByName(StringView name) {
        if (!tenants.contains(name)) {
            tenants[name] = Tenant{name};
        }
        return tenants[name];
    }
};

// Apartment maps a unique tenant to their room number.
class Apartment {
private:
    TreeMap<int, Tenant*> occupants;
    Registry registry;
public:
    Apartment() = default;

    void addOccupant(StringView name, int room) {
        occupants[room] = &registry.findByName(name);
    }

    void printTenants() {
        // room: int, tenant: Tenant
        for (const auto& [room, tenant] : occupants) {
            std::println("{} occupies room {}", tenant.name(), room);
        }
    }
};

int main(int argc, char* argv[]) {
    Apartment apartment;
    apartment.addOccupant("David", 1);
    apartment.addOccupant("Sarah", 3);
    apartment.addOccupant("George", 2);
    apartment.addOccupant("Sarah", 12);
    apartment.addOccupant("Michael", 10);
    apartment.printTenants();

    return 0;
}
```

### PHP

```mw
<?php

class CoffeeFlavour {

    private static array $CACHE = [];

    private function __construct(private string $name) {}

    public static function intern(string $name): self {
        self::$CACHE[$name] ??= new self($name);
        return self::$CACHE[$name];
    }

    public static function flavoursInCache(): int {
        return count(self::$CACHE);
    }

    public function __toString(): string {
        return $this->name;
    }

}

class Order {

    private function __construct(
        private CoffeeFlavour $flavour,
        private int $tableNumber
    ) {}

    public static function create(string $flavourName, int $tableNumber): self {
        $flavour = CoffeeFlavour::intern($flavourName);
        return new self($flavour, $tableNumber);
    }

    public function __toString(): string {
        return "Serving {$this->flavour} to table {$this->tableNumber}";
    }
}

class CoffeeShop {

    private array $orders = [];

    public function takeOrder(string $flavour, int $tableNumber) {
        $this->orders[] = Order::create($flavour, $tableNumber);
    }

    public function service() {
        print(implode(PHP_EOL, $this->orders).PHP_EOL);
    }
}

$shop = new CoffeeShop();
$shop->takeOrder("Cappuccino", 2);
$shop->takeOrder("Frappe", 1);
$shop->takeOrder("Espresso", 1);
$shop->takeOrder("Frappe", 897);
$shop->takeOrder("Cappuccino", 97);
$shop->takeOrder("Frappe", 3);
$shop->takeOrder("Espresso", 3);
$shop->takeOrder("Cappuccino", 3);
$shop->takeOrder("Espresso", 96);
$shop->takeOrder("Frappe", 552);
$shop->takeOrder("Cappuccino", 121);
$shop->takeOrder("Espresso", 121);
$shop->service();
print("CoffeeFlavor objects in cache: ".CoffeeFlavour::flavoursInCache().PHP_EOL);
```
