---
title: "Monolithic application"
source: https://en.wikipedia.org/wiki/Monolithic_application
domain: architecture-patterns
license: CC-BY-SA-4.0
tags: event-driven architecture, cqrs, message broker, publish-subscribe, service-oriented, hexagonal architecture
fetched: 2026-07-02
---

# Monolithic application

In software engineering, a **monolithic application** is a single unified software application that is self-contained and independent from other applications, but typically lacks flexibility. There are advantages and disadvantages of building applications in a monolithic style of software architecture, depending on requirements. Monolith applications are relatively simple and have a low cost but their shortcomings are lack of elasticity, fault tolerance and scalability. Alternative styles to monolithic applications include multitier architectures, distributed computing and microservices. Despite their popularity in recent years, monolithic applications are still a good choice for applications with small team and little complexity. However, once it becomes too complex, you can consider refactoring it into microservices or a distributed application. Note that a monolithic application deployed on a single machine, may be performant enough for your current workload but it's less available, less durable, less changeable, less fine-tuned and less scalable than a well designed distributed system.

The design philosophy is that the application is responsible not just for a particular task, but can perform every step needed to complete a particular function. Some personal finance applications are monolithic in the sense that they help the user carry out a complete task, end to end, and are private data silos rather than parts of a larger system of applications that work together. Some word processors are monolithic applications. These applications are sometimes associated with mainframe computers.

In software engineering, a monolithic application describes a software application that is designed as a single service. Multiple services can be desirable in certain scenarios as it can facilitate maintenance by allowing repair or replacement of parts of the application without requiring wholesale replacement.

Modularity is achieved to various extents by different modular programming approaches. Code-based modularity allows developers to reuse and repair parts of the application, but development tools are required to perform these maintenance functions (e.g. the application may need to be recompiled). Object-based modularity provides the application as a collection of separate executable files that may be independently maintained and replaced without redeploying the entire application (e.g. Microsoft's Dynamic-link library (DLL); Sun/UNIX shared object files). Some object messaging capabilities allow object-based applications to be distributed across multiple computers (e.g. Microsoft's Component Object Model (COM)). Service-oriented architectures use specific communication standards/protocols to communicate between modules.

In its original use, the term "monolithic" described enormous mainframe applications with no usable modularity. This, in combination with the rapid increase in computational power and therefore rapid increase in the complexity of the problems which could be tackled by software, resulted in unmaintainable systems and the "software crisis".

## Patterns

The following are common architectural patterns used for monolithic applications, with each having their own trade-offs:

- Layered architecture
- Modular monolith
- Microkernel architecture
