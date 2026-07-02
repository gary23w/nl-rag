---
title: "Facade pattern"
source: https://en.wikipedia.org/wiki/Facade_pattern
domain: slf4j-logging-java
license: CC-BY-SA-4.0
tags: slf4j facade, java logging abstraction, slf4j binding, slf4j logger factory
fetched: 2026-07-02
---

# Facade pattern

The **facade pattern** (also spelled *façade*) is a software design pattern commonly used in object-oriented programming. Analogous to a façade in architecture, it is an object that serves as a front-facing interface masking more complex underlying or structural code. A facade can:

- improve the readability and usability of a software library by masking interaction with more complex components behind a single (and often simplified) application programming interface (API)
- provide a context-specific interface to more generic functionality (complete with context-specific input validation)
- serve as a launching point for a broader refactor of monolithic or tightly-coupled systems in favor of more loosely-coupled code

Developers often use the facade design pattern when a system is very complex or difficult to understand because the system has many interdependent classes or because its source code is unavailable. This pattern hides the complexities of the larger system and provides a simpler interface to the client. It typically involves a single wrapper class that contains a set of members required by the client. These members access the system on behalf of the facade client and hide the implementation details.

## Overview

The Facade design pattern is one of the twenty-three well-known *GoF design patterns* that describe how to solve recurring design problems to design flexible and reusable object-oriented software, that is, objects that are easier to implement, change, test, and reuse.

What problems can the Facade design pattern solve?

- To make a complex subsystem easier to use, a simple interface should be provided for a set of interfaces in the subsystem.
- The dependencies on a subsystem should be minimized.

Clients that access a complex subsystem directly refer to (depend on) many different objects having different interfaces (tight coupling), which makes the clients hard to implement, change, test, and reuse.

What solution does the Facade design pattern describe?

Define a `Facade` object that

- implements a simple interface in terms of (by delegating to) the interfaces in the subsystem and
- may perform additional functionality before/after forwarding a request.

This enables to work through a `Facade` object to minimize the dependencies on a subsystem. See also the UML class and sequence diagram below.

## Usage

A Facade is used when an easier or simpler interface to an underlying object is desired. Alternatively, an adapter can be used when the wrapper must respect a particular interface and must support polymorphic behavior. A decorator makes it possible to add or alter behavior of an interface at run-time.

| Pattern | Intent |
|---|---|
| Adapter | Converts one interface to another so that it matches what the client is expecting |
| Decorator | Dynamically adds responsibility to the interface by wrapping the original code |
| Facade | Provides a simplified interface |

The facade pattern is typically used when

- a simple interface is required to access a complex system,
- a system is very complex or difficult to understand,
- an entry point is needed to each level of layered software, or
- the abstractions and implementations of a subsystem are tightly coupled.

A good example of where a facade is used is in register indexed values like Modbus, I2C or Special function register.

## Structure

### UML class and sequence diagram

A sample UML class and sequence diagram for the facade design pattern

In this UML class diagram, the `Client` class doesn't access the subsystem classes directly. Instead, the `Client` works through a `Facade` class that implements a simple interface in terms of (by delegating to) the subsystem classes (`Class1`, `Class2`, and `Class3`). The `Client` depends only on the simple `Facade` interface and is independent of the complex subsystem.

The sequence diagram shows the run-time interactions: The `Client` object works through a `Facade` object that delegates the request to the `Class1`, `Class2`, and `Class3` instances that perform the request.

### UML class diagram

**Facade**

The facade class abstracts Packages 1, 2, and 3 from the rest of the application.

**Clients**

The objects are using the facade pattern to access resources from the packages.
