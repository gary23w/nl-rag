---
title: "Separation of concerns"
source: https://en.wikipedia.org/wiki/Separation_of_concerns
domain: druid-rust
license: CC-BY-SA-4.0
tags: druid toolkit, data-oriented ui, rust widget tree, reactive data binding
fetched: 2026-07-02
---

# Separation of concerns

**Separation of concerns (SoC)** is a design principle in computer science and software engineering, it holds that a complex problem should be divided into distinct concerns — aspects or issues — that can be analyzed, addressed or managed individually, even when they belong to the same system. This allows focusing on one issue at a time, reducing cognitive load and complexity.

Separation of Concerns can be achieved in several ways: **temporally** (e.g., sequencing activities in a software lifecycle), by **quality** (e.g., treating correctness separately from efficiency ), by **view** (e.g., analyzing data flow separately from control flow) or by **size** (modularity)

Modularity is a specific application of concerns to system components (separation by size). In modular systems, each module encapsulates a single concern, and modules are designed, implemented, and understood in isolation before being composed into a larger system. While modularity is the most common and recognizable embodiment of SoC in code structure, the principle of Separation of concerns is broader. For example, separating requirements analysis from implementation in a project timeline, or separating functional from non-functional requirements in a specification, are valid forms of separation of concerns that do not necessarily require a modular design.

Edsger W. Dijkstra in his 1974 paper *"On the Role of Scientific Thought"*, coined the term *separation of concerns* in relation to software qualities such as *correctness* and *efficiency*.

Carlo Ghezzi in his book "Fundamentals of software engineering" promotes Separation Of Concerns as the primary way to tackle the inherited complexity in software production.

Philippe Kruchten in his article "Architectural Blueprints—The “4+1” View Model of Software Architecture" used a model composed of five main views to address large architectures, essentially this is a view-based separation of concerns, where each view focus on a different aspect of the architecture.

According to Carlo Ghezzi, the main benefit of software modularity is that it allows the application of the separation of concerns principle to system components, or "modules." Module details can be addressed in isolation; furthermore, module integration is treated as a separate concern that deals with the overall characteristics of software modules and their relationships.

Laplante, Phillip also mentioned that separation of concerns can be applied in software design, coding, time, and software qualities.

## Origin

The term *separation of concerns* was probably coined by Edsger W. Dijkstra in his 1974 paper "On the role of scientific thought".

> Let me try to explain to you, what to my taste is characteristic for all intelligent thinking. It is, that one is willing to study in depth an aspect of one's subject matter in isolation for the sake of its own consistency, all the time knowing that one is occupying oneself only with one of the aspects. We know that a program must be correct and we can study it from that viewpoint only; we also know that it should be efficient and we can study its efficiency on another day, so to speak. In another mood we may ask ourselves whether, and if so: why, the program is desirable. But nothing is gained—on the contrary!—by tackling these various aspects simultaneously. It is what I sometimes have called "the separation of concerns", which, even if not perfectly possible, is yet the only available technique for effective ordering of one's thoughts, that I know of. This is what I mean by "focusing one's attention upon some aspect": it does not mean ignoring the other aspects, it is just doing justice to the fact that from this aspect's point of view, the other is irrelevant. It is being one- and multiple-track minded simultaneously.

Fifteen years later, it was evident the term *separation of concerns* was becoming an accepted idea. In 1989, Chris Reade wrote a book titled *Elements of Functional Programming* that describes SoC:

> The programmer is having to do several things at the same time, namely,
> 
> 1. describe what is to be computed;
> 2. organise the computation sequencing into small steps;
> 3. organise memory management during the computation.

Reade continues to say,

> Ideally, the programmer should be able to concentrate on the first of the three tasks (describing what is to be computed) without being distracted by the other two, more administrative, tasks. Clearly, administration is important, but by separating it from the main task we are likely to get more reliable results and we can ease the programming problem by automating much of the administration.
> 
> SoC has other advantages. For example, program proving becomes much more feasible when details of sequencing and memory management are absent from the program. Furthermore, descriptions of what is to be computed should be free of such detailed step-by-step descriptions of how to do it, if they are to be evaluated with different machine architectures. Sequences of small changes to a data object held in a store may be an inappropriate description of how to compute something when a highly parallel machine is being used with thousands of processors distributed throughout the machine and local rather than global storage facilities.
> 
> Automating the administrative aspects means that the language implementor has to deal with them, but he/she has far more opportunity to make use of very different computation mechanisms with different machine architectures.

## Examples

### Internet protocol stack

SoC is crucial to the design of the Internet. In the Internet protocol suite, great efforts have been made to separate concerns into well-defined layers. This allows protocol designers to focus on the concerns in one layer, and ignore the other layers. The Application Layer protocol SMTP, for example, is concerned about all the details of conducting an email session over a reliable transport service (usually TCP), but not in the least concerned about how the transport service makes that service reliable. Similarly, TCP is not concerned about the routing of data packets, which is handled at the Internet layer.

### HTML, CSS, JavaScript

HTML, CSS, and JavaScript are complementary languages used in the development of web pages and websites. HTML is mainly used for organization of webpage content, CSS is used for definition of content presentation style, and JavaScript defines how the content interacts and behaves with the user. Historically, this was not the case: prior to the introduction of CSS, HTML performed both duties of defining semantics and style.

### Subject-oriented programming

Subject-oriented programming allows separate concerns to be addressed as separate software constructs, each on an equal footing with the others. Each concern provides its own class-structure into which the objects in common are organized, and contributes state and methods to the composite result where they cut across one another. Correspondence rules describe how the classes and methods in the various concerns are related to each other at points where they interact, allowing composite behavior for a method to be derived from several concerns. Multi-dimensional SoC allows the analysis and composition of concerns to be manipulated as a multi-dimensional "matrix" in which each concern provides a dimension in which different points of choice are enumerated, with the cells of the matrix occupied by the appropriate software artifacts.

### Aspect-oriented programming

Aspect-oriented programming allows cross-cutting concerns to be addressed as primary concerns. For example, most programs require some form of security and logging. Security and logging are often secondary concerns, whereas the primary concern is often on accomplishing business goals. However, when designing a program, its security must be built into the design from the beginning instead of being treated as a secondary concern. Applying security afterwards often results in an insufficient security model that leaves too many gaps for future attacks. This may be solved with aspect-oriented programming. For example, an aspect may be written to enforce that calls to a certain API are always logged, or that errors are always logged when an exception is thrown, regardless of whether the program's procedural code handles the exception or propagates it.

### Levels of analysis in artificial intelligence

In cognitive science and artificial intelligence, it is common to refer to David Marr's levels of analysis. At any given time, a researcher may be focusing on what some aspect of intelligence needs to compute, what algorithm it employs, or how that algorithm is implemented in hardware. This separation of concerns is similar to the interface/implementation distinction in software and hardware engineering.
