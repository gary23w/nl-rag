---
title: "Composite pattern"
source: https://en.wikipedia.org/wiki/Composite_pattern
domain: software-design
license: CC-BY-SA-4.0
tags: design pattern, software architecture, software design, refactoring
fetched: 2026-07-02
---

# Composite pattern

In software engineering, the **composite pattern** is a partitioning design pattern. The composite pattern describes a group of objects that are treated the same way as a single instance of the same type of object. The intent of a composite is to "compose" objects into tree structures to represent part-whole hierarchies. Implementing the composite pattern lets clients treat individual objects and compositions uniformly.

## Overview

The Composite design pattern is one of the twenty-three well-known *GoF design patterns* that describe how to solve recurring design problems to design flexible and reusable object-oriented software, that is, objects that are easier to implement, change, test, and reuse.

### Problems

The Composite pattern solves these problems:

- Represent a part-whole hierarchy so that clients can treat part and whole objects uniformly.
- Represent a part-whole hierarchy as tree structure.

When defining (1) `Part` objects and (2) `Whole` objects that act as containers for `Part` objects, clients must treat them separately, which complicates client code.

### Solution

- Define a unified `Component` interface for part (`Leaf`) objects and whole (`Composite`) objects.
- Individual `Leaf` objects implement the `Component` interface directly, and `Composite` objects forward requests to their child components.

This enables clients to work through the `Component` interface to treat `Leaf` and `Composite` objects uniformly: `Leaf` objects perform a request directly, and `Composite` objects forward the request to their child components recursively downwards the tree structure. This makes client classes easier to implement, change, test, and reuse.

See also the UML class and object diagram below.

## Motivation

When dealing with Tree-structured data, programmers often have to discriminate between a leaf-node and a branch. This makes code more complex, and therefore, more error prone. The solution is an interface that allows treating complex and primitive objects uniformly. In object-oriented programming, a composite is an object designed as a composition of one-or-more similar objects, all exhibiting similar functionality. This is known as a "has-a" relationship between objects. The key concept is that you can manipulate a single instance of the object just as you would manipulate a group of them. The operations you can perform on all the composite objects often have a least common denominator relationship. For example, if defining a system to portray grouped shapes on a screen, it would be useful to define resizing a group of shapes to have the same effect (in some sense) as resizing a single shape.

## When to use

Composite should be used when clients ignore the difference between compositions of objects and individual objects. If programmers find that they are using multiple objects in the same way, and often have nearly identical code to handle each of them, then composite is a good choice; it is less complex in this situation to treat primitives and composites as homogeneous.

## Structure

### UML class and object diagram

In the above UML class diagram, the `Client` class doesn't refer to the `Leaf` and `Composite` classes directly (separately). Instead, the `Client` refers to the common `Component` interface and can treat `Leaf` and `Composite` uniformly. The `Leaf` class has no children and implements the `Component` interface directly. The `Composite` class maintains a container of child `Component` objects (`children`) and forwards requests to these `children` (`for each child in children: child.operation()`).

The object collaboration diagram shows the run-time interactions: In this example, the `Client` object sends a request to the top-level `Composite` object (of type `Component`) in the tree structure. The request is forwarded to (performed on) all child `Component` objects (`Leaf` and `Composite` objects) downwards the tree structure.

**Defining Child-Related Operations**

There are two design variants for defining and implementing child-related operations like adding/removing a child component to/from the container (`add(child)/remove(child)`) and accessing a child component (`getChild()`):

- *Design for transparency:* Child-related operations are defined in the `Component` interface. This enables clients to treat `Leaf` and `Composite` objects uniformly. But type safety is lost because clients can perform child-related operations on `Leaf` objects.
- *Design for type safety:* Child-related operations are defined only in the `Composite` class. Clients must treat `Leaf` and `Composite` objects differently. But type safety is gained because clients *cannot* perform child-related operations on `Leaf` objects.

The GoF authors present a variant of the Composite design pattern that emphasizes *transparency* over *type safety* and discuss the tradeoffs of the two approaches.

The type-safe approach is particularly palatable if the composite structure is fixed post construction: the construction code does not require transparency because it needs to know the types involved in order to construct the composite. If downstream, the code does not need to modify the structure, then the child manipulation operations do not need to be present on the `Component` interface.

### UML class diagram

**Component**

- is the abstraction for all components, including composite ones
- declares the interface for objects in the composition
- (optional) defines an interface for accessing a component's parent in the recursive structure, and implements it if that's appropriate

**Leaf**

- represents leaf objects in the composition
- implements all Component methods

**Composite**

- represents a composite Component (component having children)
- implements methods to manipulate children
- implements all Component methods, generally by delegating them to its children

## Variation

As it is described in Design Patterns, the pattern also involves including the child-manipulation methods in the main Component interface, not just the Composite subclass. More recent descriptions sometimes omit these methods.

## Example

This C++23 implementation is based on the pre C++98 implementation in the book.

```mw
import std;

using std::runtime_error;
using std::shared_ptr;
using std::string;
using std::unique_ptr;
using std::vector;

// Component object
// declares the interface for objects in the composition.
class Equipment {
private:
    string name;
    double netPrice;
protected:
    Equipment() = default;

    explicit Equipment(const string& name): 
        name{name}, netPrice{0} {}
public:
    // implements default behavior for the interface common to all classes, as appropriate.
    [[nodiscard]]
    virtual const string& getName() const noexcept {
        return name;
    }

    virtual void setName(const string& name) noexcept {
        this->name = name;
    }

    [[nodiscard]]
    virtual double getNetPrice() const noexcept {
        return netPrice;
    }

    virtual void setNetPrice(double netPrice) noexcept {
        this->netPrice = netPrice;
    }

    // declares an interface for accessing and managing its child components.
    virtual void add(shared_ptr<Equipment>) = 0;
    virtual void remove(shared_ptr<Equipment>) = 0;
    virtual ~Equipment() = default;
};

// Composite object
// defines behavior for components having children.
class CompositeEquipment: public Equipment {
private:
    // stores child components.
    using EquipmentList = vector<shared_ptr<Equipment>>;
    EquipmentList equipments;
protected:
    CompositeEquipment() = default;

    explicit CompositeEquipment(const string& name):
        Equipment(name), equipments{EquipmentList()} {}
public:
    // implements child-related operations in the Component interface.
    [[nodiscard]]
    virtual double getNetPrice() const noexcept override {
        double total = Equipment::getNetPrice();
        for (const Equipment& i: equipments) {
            total += i->getNetPrice();
        }
        return total;
    }

    virtual void add(shared_ptr<Equipment> equipment) override {
        equipments.push_back(equipment.get());
    }

    virtual void remove(shared_ptr<Equipment> equipment) override {
        equipments.remove(equipment.get());
    }
};

// Leaf object
// represents leaf objects in the composition.
class FloppyDisk: public Equipment {
public:
    explicit FloppyDisk(const String& name):
        Equipment(name) {}

    // A leaf has no children.
    void add(shared_ptr<Equipment>) override {
        throw runtime_error("FloppyDisk::add() cannot be called!");
    }

    void remove(shared_ptr<Equipment>) override {
        throw runtime_error("FloppyDisk::remove() cannot be called!");
    }
};

class Chassis: public CompositeEquipment {
public:
    explicit Chassis(const string& name): 
        CompositeEquipment(name) {}
};

int main() {
    shared_ptr<FloppyDisk> fd1 = std::make_shared<FloppyDisk>("3.5in Floppy");
    fd1->setNetPrice(19.99);
    std::println("{}: netPrice = {}", fd1->getName(), fd1->getNetPrice);

    shared_ptr<FloppyDisk> fd2 = std::make_shared<FloppyDisk>("5.25in Floppy");
    fd2->setNetPrice(29.99);
    std::println("{}: netPrice = {}", fd2->getName(), fd2->getNetPrice);

    unique_ptr<Chassis> ch = std::make_unique<Chassis>("PC Chassis");
    ch->setNetPrice(39.99);
    ch->add(fd1);
    ch->add(fd2);
    std::println("{}: netPrice = {}", ch->getName(), ch->getNetPrice);

    fd2->add(fd1);
}
```

The program output is

```mw
3.5in Floppy: netPrice=19.99
5.25in Floppy: netPrice=29.99
PC Chassis: netPrice=89.97
terminate called after throwing an instance of 'std::runtime_error'
  what():  FloppyDisk::add
```
