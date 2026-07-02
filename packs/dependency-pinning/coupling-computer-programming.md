---
title: "Coupling (computer programming)"
source: https://en.wikipedia.org/wiki/Coupling_(computer_programming)
domain: dependency-pinning
license: CC-BY-SA-4.0
tags: dependency version pinning, lock file reproducibility, hash pinned dependency, deterministic dependency resolution
fetched: 2026-07-02
---

# Coupling (computer programming)

In software engineering, **coupling** is the degree of interdependence between software modules, a measure of how closely connected two routines or modules are, and the strength of the relationships between modules. Coupling is not binary but multi-dimensional.

Coupling is usually contrasted with cohesion. Low coupling often correlates with high cohesion, and vice versa. Low coupling is often thought to be a sign of a well-structured computer system and a good design, and when combined with high cohesion, supports the general goals of high readability and maintainability.

## History

The software quality metrics of coupling and cohesion were invented by Larry Constantine in the late 1960s as part of a structured design, based on characteristics of “good” programming practices that reduced maintenance and modification costs. Structured design, including cohesion and coupling, were published in the article *Stevens, Myers & Constantine* (1974) and the book *Yourdon & Constantine* (1979), and the latter subsequently became standard terms.

## Coupling versus cohesion

Coupling and cohesion are terms which occur together very frequently. Coupling refers to the interdependencies between modules, while cohesion describes how related the functions within a single module are. Low cohesion implies that a given module performs tasks which are not very related to each other and hence can create problems as the module becomes large.

## Degree

Coupling can be "low" (also "loose" and "weak") or "high" (also "tight" and "strong"). Some types of coupling, in order of highest to lowest coupling, are as follows:

### Procedural programming

A module here refers to a subroutine of any kind, i.e. a set of one or more statements having a name and preferably its own set of variable names.

**Content coupling (high)**

Content coupling is said to occur when one module uses the code of another module, for instance a branch. This violates

information hiding

– a basic software design concept.

**Common coupling**

Common coupling is said to occur when several modules have access to the same global data. But it can lead to uncontrolled error propagation and unforeseen side-effects when changes are made.

**External coupling**

External coupling occurs when two modules share an externally imposed data format,

communication protocol

, or device interface. This is basically related to the communication to external tools and devices.

**Control coupling**

Control coupling is one module controlling the flow of another, by passing it information on what to do (e.g., passing a what-to-do flag).

**Stamp coupling (data-structured coupling)**

Stamp coupling occurs when modules share a composite

data structure

and use only parts of it, possibly different parts (e.g., passing a whole record to a function that needs only one field of it).

In this situation, a modification in a field that a module does not need may lead to changing the way the module reads the record. To illustrate the concept of stamp coupling, consider a scenario involving a

UserProfile

component

. This component is designed to return the entire user profile information in response to

requests

, even when

consumers

only require a specific

attribute

. This practice exemplifies stamp coupling, which can lead to significant

bandwidth

issues, especially at scale. When any attribute within the

UserProfile

component changes, all consumers that interact with it may need to undergo

testing

, even if they do not utilize the modified attribute.

**Data coupling**

Data coupling occurs when modules share data through, for example, parameters. Each datum is an elementary piece, and these are the only data shared (e.g., passing an integer to a function that computes a square root).

### Object-oriented programming

**Subclass coupling**

Describes the relationship between a child and its parent. The child is connected to its parent, but the parent is not connected to the child.

**Temporal coupling**

It is when two actions are bundled together into one module just because they happen to occur at the same time.

In recent work various other coupling concepts have been investigated and used as indicators for different modularization principles used in practice.

#### Dynamic coupling

The goal of defining and measuring this type of coupling is to provide a run-time evaluation of a software system. It has been argued that static coupling metrics lose precision when dealing with an intensive use of dynamic binding or inheritance. In the attempt to solve this issue, dynamic coupling measures have been taken into account.

#### Semantic coupling

This kind of a coupling metric considers the conceptual similarities between software entities using, for example, comments and identifiers and relying on techniques such as latent semantic indexing (LSI).

#### Logical coupling

Logical coupling (or evolutionary coupling or change coupling) analysis exploits the release history of a software system to find change patterns among modules or classes: e.g., entities that are likely to be changed together or sequences of changes (a change in a class A is always followed by a change in a class B).

## Dimensions of coupling

According to Gregor Hohpe, coupling is multi-dimensional:

- Technology Dependency
- Location Dependency
- Topology Dependency
- Data Format & Type Dependency
- Semantic Dependency
- Conversation Dependency
- Order Dependency
- Temporal Dependency

## Disadvantages of tight coupling

Tightly coupled systems tend to exhibit the following developmental characteristics, which are often seen as disadvantages:

1. A change in one module usually forces a ripple effect of changes in other modules.
2. Assembly of modules might require more effort and/or time due to the increased inter-module dependency.
3. A particular module might be harder to reuse and/or test because dependent modules must be included.

## Performance issues

Whether loosely or tightly coupled, a system's performance is often reduced by message and parameter creation, transmission, translation (e.g. marshaling) and message interpretation (which might be a reference to a string, array or data structure), which require less overhead than creating a complicated message such as a SOAP message. Longer messages require more CPU and memory to produce. To optimize runtime performance, message length must be minimized and message meaning must be maximized.

**Message Transmission Overhead and Performance**

Since a message must be transmitted in full to retain its complete meaning, message transmission must be optimized. Longer messages require more CPU and memory to transmit and receive. Also, when necessary, receivers must reassemble a message into its original state to completely receive it. Hence, to optimize runtime performance, message length must be minimized and message meaning must be maximized.

**Message Translation Overhead and Performance**

Message protocols and messages themselves often contain extra information (i.e., packet, structure, definition and language information). Hence, the receiver often needs to translate a message into a more refined form by removing extra characters and structure information and/or by converting values from one type to another. Any sort of translation increases CPU and/or memory overhead. To optimize runtime performance, message form and content must be reduced and refined to maximize its meaning and reduce translation.

**Message Interpretation Overhead and Performance**

All messages must be interpreted by the receiver. Simple messages such as integers might not require additional processing to be interpreted. However, complex messages such as

SOAP

messages require a parser and a string transformer for them to exhibit intended meanings. To optimize runtime performance, messages must be refined and reduced to minimize interpretation overhead.

## Solutions

One approach to decreasing coupling is functional design, which seeks to limit the responsibilities of modules along functionality. Coupling increases between two classes `A` and `B` if:

- `A` has an attribute that refers to (is of type) `B`.
- `A` calls on services of an object `B`.
- `A` has a method that references `B` (via return type or parameter).
- `A` is a subclass of (or implements) class `B`.

Low coupling refers to a relationship in which one module interacts with another module through a simple and stable interface and does not need to be concerned with the other module's internal implementation (see Information Hiding).

Systems such as CORBA or COM allow objects to communicate with each other without having to know anything about the other object's implementation. Both of these systems even allow for objects to communicate with objects written in other languages.

## Coupling vs Connascence

Coupling describes the degree and nature of dependency between software components, focusing on what they share (e.g., data, control flow, technology) and how tightly they are bound. It evaluates two key dimensions: strength, which measures how difficult it is to change the dependency, and scope (or visibility), which indicates how widely the dependency is exposed across modules or boundaries. Traditional coupling types typically include content coupling, common coupling, control coupling, stamp coupling, external coupling, and data coupling.

Connascence, introduced by Meilir Page-Jones, provides a systematic framework for analyzing and measuring coupling dependencies. It evaluates dependencies based on three dimensions: strength, which measures the effort required to refactor or modify the dependency; locality, which considers how physically or logically close dependent components are in the codebase; and degree, which measures how many components are affected by the dependency. Connascence can be categorized into static (detectable at compile-time) and dynamic (detectable at runtime) forms. Static connascence refers to compile-time dependencies, such as method signatures, while dynamic connascence refers to runtime dependencies, which can manifest in forms like connascence of timing, values, or algorithm.

Each coupling flavor can exhibit multiple types of connascence, a specific type, or, in rare cases, none at all, depending on how the dependency is implemented. Common types of connascence include connascence of name, type, position, and meaning. Certain coupling types naturally align with specific connascence types; for example, data coupling often involves connascence of name or type. However, not every combination of coupling and connascence is practically meaningful. Dependencies relying on parameter order in a method signature demonstrate connascence of position, which is fragile and difficult to refactor because reordering parameters breaks the interface. In contrast, connascence of name, which relies on field or parameter names, is generally more resilient to change. Connascence types themselves exhibit a natural hierarchy of strength, with connascence of name typically considered weaker than connascence of meaning.

Dependencies spanning module boundaries or distributed systems typically have higher coordination costs, increasing the difficulty of refactoring and propagating changes across distant boundaries. Modern practices, such as dependency injection and interface-based programming, are often employed to reduce coupling strength and improve the maintainability of dependencies.

While coupling identifies what is shared between components, connascence evaluates how those dependencies behave, how changes propagate, and how difficult they are to refactor. Strength, locality, and degree are interrelated; dependencies with high strength, wide scope, and spanning distant boundaries are significantly harder to refactor and maintain. Together, coupling provides a high-level overview of dependency relationships, while connascence offers a granular framework for analyzing dependency strength, locality, degree, and resilience to change, supporting the design of maintainable and robust systems.

## Module coupling

Coupling in Software Engineering describes a version of metrics associated with this concept.

For data and control flow coupling:

- $d_{i}$ : number of input data parameters
- $c_{i}$ : number of input control parameters
- $d_{o}$ : number of output data parameters
- $c_{o}$ : number of output control parameters

For global coupling:

- $g_{d}$ : number of global variables used as data
- $g_{c}$ : number of global variables used as control

For environmental coupling:

- w : number of modules called (fan-out)
- r : number of modules calling the module under consideration (fan-in)

$\mathrm {Coupling} (C)=1-{\frac {1}{d_{i}+2\times c_{i}+d_{o}+2\times c_{o}+g_{d}+2\times g_{c}+w+r}}$

`Coupling(C)` makes the value larger the more coupled the module is. This number ranges from approximately 0.67 (low coupling) to 1.0 (highly coupled)

For example, if a module has only a single input and output data parameter

$C=1-{\frac {1}{1+0+1+0+0+0+1+0}}=1-{\frac {1}{3}}=0.67$

If a module has 5 input and output data parameters, an equal number of control parameters, and accesses 10 items of global data, with a fan-in of 3 and a fan-out of 4,

$C=1-{\frac {1}{5+2\times 5+5+2\times 5+10+0+3+4}}=0.98$
