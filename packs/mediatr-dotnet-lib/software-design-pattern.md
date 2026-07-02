---
title: "Software design pattern"
source: https://en.wikipedia.org/wiki/Software_design_pattern
domain: mediatr-dotnet-lib
license: CC-BY-SA-4.0
tags: mediatr library, dotnet mediator pattern, mediatr request handler, mediatr notification
fetched: 2026-07-02
---

# Software design pattern

A **software design pattern** describes a reusable solution to a commonly needed behavior in software. A design pattern is not a rigid structure to be copied directly into source code. Rather, it is a description of and a template for solving a particular type of problem that can be used in many different contexts, including different programming languages and computing platforms. Design patterns can be viewed as formalized best practices that the programmer may use to solve common problems when designing software.

Object-oriented design patterns typically show relationships and interactions between classes or objects, without specifying the final application classes or objects that are involved. Patterns that imply mutable state may be unsuited for functional programming languages. Some patterns can be rendered unnecessary in languages that have built-in support for solving the problem they are trying to solve, and object-oriented patterns are not necessarily suitable for non-object-oriented languages.

## History

Patterns originated as an architectural concept by Christopher Alexander as early as 1977 in A Pattern Language (cf. his article, "The Pattern of Streets," JOURNAL OF THE AIP, September, 1966, Vol. 32, No. 5, pp. 273–278). In 1987, Kent Beck and Ward Cunningham began experimenting with the idea of applying patterns to programming – specifically pattern languages – and presented their results at the OOPSLA conference that year. In the following years, Beck, Cunningham and others followed up on this work.

Design patterns gained popularity in computer science after the book *Design Patterns: Elements of Reusable Object-Oriented Software* was published in 1994 by the so-called "Gang of Four" (Erich Gamma, Richard Helm, Ralph Johnson and John Vlissides), which is frequently abbreviated as "GoF". That same year, the first Pattern Languages of Programming Conference was held, and the following year the Portland Pattern Repository was set up for documentation of design patterns.

Although design patterns have been applied practically for a long time, formalization of the concept of design patterns languished for several years.

## Practice

Design patterns can speed up the development process by providing proven development paradigms. Effective software design requires considering issues that may not become apparent until later in the implementation. Freshly written code can often have hidden, subtle issues that take time to be detected – issues that sometimes can cause major problems down the road. Reusing design patterns can help to prevent such issues, and enhance code readability for those familiar with the patterns.

Software design techniques are difficult to apply to a broader range of problems. Design patterns provide general solutions, documented in a format that does not require specifics tied to a particular problem.

In 1996, Christopher Alexander was invited to give a Keynote Speech to the 1996 OOPSLA Convention. Here he reflected on how his work on Patterns in Architecture had developed and his hopes for how the Software Design community could help Architecture extend Patterns to create living structures that use generative schemes that are more like computer code.

## Motif

A pattern describes a *design motif*, also known as a *prototypical micro-architecture*, as a set of program constituents (e.g., classes, methods...) and their relationships. A developer adapts the motif to their codebase to solve the problem described by the pattern. The resulting code has structure and organization similar to the chosen motif.

## Domain-specific patterns

Efforts have also been made to codify design patterns in particular domains, including the use of existing design patterns as well as domain-specific design patterns. Examples include user interface design patterns, information visualization, secure design, "secure usability", web design and business model design.

The annual Pattern Languages of Programming Conference proceedings include many examples of domain-specific patterns.

## Object-oriented programming

Object-oriented design patterns typically show relationships and interactions between classes or objects, without specifying the final application classes or objects that are involved. Patterns that imply mutable state may be unsuited for functional programming languages. Some patterns can be rendered unnecessary in languages that have built-in support for solving the problem they are trying to solve, and object-oriented patterns are not necessarily suitable for non-object-oriented languages.

## Examples

Design patterns can be organized into groups based on what kind of problem they solve.

### Creational

A creational pattern creates objects.

| Name | Description | In *Design Patterns* | In *Code Complete* | Other |
|---|---|---|---|---|
| Abstract factory | Provide an interface for creating *families* of related or dependent objects without specifying their concrete classes. | Yes | Yes | —N/a |
| Builder | Separate the construction of a complex object from its representation, allowing the same construction process to create various representations. | Yes | Yes | —N/a |
| Dependency Injection | A class accepts the objects it requires from an injector instead of creating the objects directly. | —N/a | Yes | —N/a |
| Factory method | Define an interface for creating a *single* object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses. | Yes | Yes | —N/a |
| Lazy initialization | Tactic of delaying the creation of an object, the calculation of a value, or some other expensive process until the first time it is needed. This pattern appears in the GoF catalog as "virtual proxy", an implementation strategy for the Proxy pattern. | Yes | Yes | PoEAA |
| Multiton | Ensure a class has only named instances, and provide a global point of access to them. | Yes | Yes | Yes |
| Object pool | Avoid expensive acquisition and release of resources by recycling objects that are no longer in use. Can be considered a generalisation of connection pool and thread pool patterns. | Yes | Yes | Yes |
| Prototype | Specify the kinds of objects to create using a prototypical instance, and create new objects from the 'skeleton' of an existing object, thus boosting performance and keeping memory footprints to a minimum. | Yes | Yes | Yes |
| Resource acquisition is initialization (RAII) | Ensure that resources are properly released by tying them to the lifespan of suitable objects. | Yes | Yes | Yes |
| Singleton | Ensure a class has only one instance, and provide a global point of access to it. | Yes | Yes | Yes |

### Structural

A structural pattern organizes classes and objects to form larger structures that provide new functionality.

| Name | Description | In *Design Patterns* | In *Code Complete* | Other |
|---|---|---|---|---|
| Adapter, Wrapper, or Translator | Convert the interface of a class into another interface clients expect. An adapter lets classes work together that could not otherwise because of incompatible interfaces. The enterprise integration pattern equivalent is the translator. | Yes | Yes | Yes |
| Bridge | Decouple an abstraction from its implementation allowing the two to vary independently. | Yes | Yes | Yes |
| Composite | Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly. | Yes | Yes | Yes |
| Decorator | Attach additional responsibilities to an object dynamically keeping the same interface. Decorators provide a flexible alternative to subclassing for extending functionality. | Yes | Yes | Yes |
| Delegation | Extend a class by composition instead of subclassing. The object handles a request by delegating to a second object (the delegate) | Yes | Yes | Yes |
| Extension object | Adding functionality to a hierarchy without changing the hierarchy. | Yes | Yes | Yes |
| Facade | Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use. | Yes | Yes | Yes |
| Flyweight | Use sharing to support large numbers of similar objects efficiently. | Yes | Yes | Yes |
| Front controller | The pattern relates to the design of Web applications. It provides a centralized entry point for handling requests. | Yes | Yes | J2EE Patterns PoEAA |
| Marker | Empty interface to associate metadata with a class. | Yes | Yes | Effective Java |
| Module | Group several related elements, such as classes, singletons, methods, globally used, into a single conceptual entity. | Yes | Yes | Yes |
| Proxy | Provide a surrogate or placeholder for another object to control access to it. | Yes | Yes | Yes |
| Twin | Twin allows modeling of multiple inheritance in programming languages that do not support this feature. | Yes | Yes | Yes |

### Behavioral

A behavioral pattern describes collaboration between objects.

| Name | Description | In *Design Patterns* | In *Code Complete* | Other |
|---|---|---|---|---|
| Blackboard | Artificial intelligence pattern for combining disparate sources of data (see blackboard system) | Yes | Yes | Yes |
| Chain of responsibility | Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. Chain the receiving objects and pass the request along the chain until an object handles it. | Yes | Yes | Yes |
| Command | Encapsulate a request as an object, thereby allowing for the parameterization of clients with different requests, and the queuing or logging of requests. It also allows for the support of undoable operations. | Yes | Yes | Yes |
| Fluent interface | Design an API to be method chained so that it reads like a DSL. Each method call returns a context through which the next logical method call(s) are made available. | Yes | Yes | Yes |
| Interpreter | Given a language, define a representation for its grammar along with an interpreter that uses the representation to interpret sentences in the language. | Yes | Yes | Yes |
| Iterator | Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation. | Yes | Yes | Yes |
| Mediator | Define an object that encapsulates how a set of objects interact. Mediator promotes loose coupling by keeping objects from referring to each other explicitly, and it allows their interaction to vary independently. | Yes | Yes | Yes |
| Memento | Without violating encapsulation, capture and externalize an object's internal state allowing the object to be restored to this state later. | Yes | Yes | Yes |
| Null object | Avoid null references by providing a default object. | Yes | Yes | Yes |
| Observer or Publish/subscribe | Define a one-to-many dependency between objects where a state change in one object results in all its dependents being notified and updated automatically. | Yes | Yes | Yes |
| Servant | Define common functionality for a group of classes. The servant pattern is also frequently called helper class or utility class implementation for a given set of classes. The helper classes generally have no objects hence they have all static methods that act upon different kinds of class objects. | Yes | Yes | Yes |
| Specification | Recombinable business logic in a Boolean fashion. | Yes | Yes | Yes |
| State | Allow an object to alter its behavior when its internal state changes. The object will appear to change its class. | Yes | Yes | Yes |
| Strategy | Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it. | Yes | Yes | Yes |
| Template method | Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure. | Yes | Yes | Yes |
| Visitor | Represent an operation to be performed on instances of a set of classes. Visitor lets a new operation be defined without changing the classes of the elements on which it operates. | Yes | Yes | Yes |

### Concurrency

A concurrency pattern supports concurrent processing.

| Name | Description | In *POSA2* | Other |
|---|---|---|---|
| Active Object | Decouples method execution from method invocation that reside in their own thread of control. The goal is to introduce concurrency, by using asynchronous method invocation and a scheduler for handling requests. | Yes | —N/a |
| Balking | Only execute an action on an object when the object is in a particular state. | No | —N/a |
| Binding properties | Combining multiple observers to force properties in different objects to be synchronized or coordinated in some way. | No | —N/a |
| Compute kernel | The same calculation many times in parallel, differing by integer parameters used with non-branching pointer math into shared arrays, such as GPU-optimized Matrix multiplication or Convolutional neural network. | No | —N/a |
| Double-checked locking | Reduce the overhead of acquiring a lock by first testing the locking criterion (the 'lock hint') in an unsafe manner; only if that succeeds does the actual locking logic proceed. Can be unsafe when implemented in some language/hardware combinations. It can therefore sometimes be considered an anti-pattern. | Yes | —N/a |
| Event-based asynchronous | Addresses problems with the asynchronous pattern that occur in multithreaded programs. | No | —N/a |
| Guarded suspension | Manages operations that require both a lock to be acquired and a precondition to be satisfied before the operation can be executed. | No | —N/a |
| Join | Join-pattern provides a way to write concurrent, parallel and distributed programs by message passing. Compared to the use of threads and locks, this is a high-level programming model. | No | —N/a |
| Lock | One thread puts a "lock" on a resource, preventing other threads from accessing or modifying it. | No | PoEAA |
| Messaging design pattern (MDP) | Allows the interchange of information (i.e. messages) between components and applications. | No | —N/a |
| Monitor object | An object whose methods are subject to mutual exclusion, thus preventing multiple objects from erroneously trying to use it at the same time. | Yes | —N/a |
| Reactor | A reactor object provides an asynchronous interface to resources that must be handled synchronously. | Yes | —N/a |
| Read-write lock | Allows concurrent read access to an object, but requires exclusive access for write operations. An underlying semaphore might be used for writing, and a Copy-on-write mechanism may or may not be used. | No | —N/a |
| Scheduler | Explicitly control when threads may execute single-threaded code. | No | —N/a |
| Service handler pattern | For each request, a server spawns a dedicated client handler to handle a request. Also referred to as *thread-per-session*. | No | —N/a |
| Thread pool | A number of threads are created to perform a number of tasks, which are usually organized in a queue. Typically, there are many more tasks than threads. Can be considered a special case of the object pool pattern. | No | —N/a |
| Thread-specific storage | Static or "global" memory local to a thread. | Yes | —N/a |
| Safe Concurrency with Exclusive Ownership | Avoiding the need for runtime concurrent mechanisms, because exclusive ownership can be proven. This is a notable capability of the Rust language, but compile-time checking isn't the only means, a programmer will often manually design such patterns into code - omitting the use of locking mechanism because the programmer assesses that a given variable is never going to be concurrently accessed. | No | —N/a |
| CPU atomic operation | x86 and other CPU architectures support a range of atomic instructions that guarantee memory safety for modifying and accessing primitive values (integers). For example, two threads may both increment a counter safely. These capabilities can also be used to implement the mechanisms for other concurrency patterns as above. The C# language uses the Interlocked class for these capabilities. | No | —N/a |

## Documentation

The documentation for a design pattern describes the context in which the pattern is used, the forces within the context that the pattern seeks to resolve, and the suggested solution. There is no single, standard format for documenting design patterns. Rather, a variety of different formats have been used by different pattern authors. However, according to Martin Fowler, certain pattern forms have become more well-known than others, and consequently become common starting points for new pattern-writing efforts. One example of a commonly used documentation format is the one used by Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides in their book *Design Patterns*. It contains the following sections:

**Name**

A descriptive and unique name that helps in identifying and referring to the pattern.

**Intent**

A description of the goal behind the pattern and the reason for using it.

**Also Known As**

Other names for the pattern.

**Motivation**

A scenario consisting of a problem and a context in which this pattern can be used.

**Applicability**

Situations in which this pattern is usable; the context for the pattern.

**Structure**

A graphical representation of the pattern.

Class diagrams

and

Interaction diagrams

may be used for this purpose.

**Participants**

A listing of the classes and objects used in the pattern and their roles in the design.

**Collaboration**

A description of how classes and objects used in the pattern interact with each other.

**Consequences**

A description of the results, side effects, and trade offs caused by using the pattern.

**Implementation**

A description of an implementation of the pattern; the solution part of the pattern.

**Sample Code**

An illustration of how the pattern can be used in a programming language.

**Known Uses**

Examples of real usages of the pattern.

**Related Patterns**

Other patterns that have some relationship with the pattern; discussion of the differences between the pattern and similar patterns.

## Criticism

Some suggest that the need for a design pattern may be a sign that a feature is missing from a programming language. Peter Norvig demonstrates that 16 out of the 23 patterns in the *Design Patterns* book (which is primarily focused on C++) are simplified or eliminated (via direct language support) in Lisp or Dylan. Related observations were made by Hannemann & Kiczales (2002) who implemented several of the 23 design patterns using an aspect-oriented programming language (AspectJ) and showed that code-level dependencies were removed from the implementations of 17 of the 23 design patterns and that aspect-oriented programming could simplify the implementations of design patterns. See also Paul Graham's essay "Revenge of the Nerds".

Inappropriate use of patterns may unnecessarily increase complexity.

By definition, a pattern must be programmed anew into each application that uses it. Since some authors see this as a step backward from software reuse as provided by components, researchers have worked to use generic programming facilities to turn patterns into components, in a process called *componentization*. Meyer & Arnout (2006) were able to provide full or partial componentization of two-thirds of the patterns they attempted.

In order to achieve flexibility, design patterns may introduce additional levels of indirection, which may complicate the resulting design and decrease runtime performance.

The following concepts are similar in general nature yet differ from software design pattern:

**Software architecture pattern**

A reusable, proven solution to a recurring problem at the system level, addressing concerns related to the overall structure, component interactions, and quality attributes of the system.

Software architecture patterns operate at a higher level of abstraction than design patterns, solving broader system-level challenges. While these patterns typically affect system-level concerns, the distinction between architectural patterns and architectural styles can sometimes be blurry. Examples include

Circuit Breaker

.

**Software architecture style**

A high-level, structural organization that defines the overall system organization, specifying how components are organized, how they interact, and the constraints on those interactions.

Architecture styles typically include a vocabulary of component and connector types, as well as semantic models for interpreting the system's properties. These styles represent the most coarse-grained level of system organization. Examples include

Layered Architecture

,

Microservices

, and

Event-Driven Architecture

.

**Implementation pattern**

Beck draws a distinction between design patterns, which generally describe the relationships between classes, and

implementation patterns

, which are often limited to a single class.

Building on this,

Iglberger (2022)

defines an implementation pattern as a

programming idiom

which does not introduce an abstraction, and so which resides at the level of implementation details.

For this reason, they are commonly specific to the language of implementation, with

copy-and-swap

and

RAII

as examples in C++,

although in other languages, such idioms may constitute true design patterns.
