---
title: "Behavior tree"
source: https://en.wikipedia.org/wiki/Behavior_tree
domain: behavior-trees
license: CC-BY-SA-4.0
tags: behavior tree, behaviour tree ai, game ai behavior, behavior tree node
fetched: 2026-07-02
---

# Behavior tree

A **behavior tree** is a structured visual modeling technique used in systems engineering and software engineering to represent system behavior. It utilizes a hierarchical tree diagram composed of nodes and connectors to illustrate control flow and system actions. By replacing ambiguous natural language descriptions with standardized visual elements—such as boxes, arrows, and standard symbols—behavior trees improve clarity, reduce misinterpretation, and enhance understanding of complex systems.

## Overview

The extensive amount of detail involved in describing the numerous requirements of a large-scale system using natural language can lead to short-term memory overload, hindering a comprehensive understanding of the system's needs. Natural language often introduces ambiguities, aliases, inconsistencies, redundancies, and incomplete information to concepts. This creates uncertainty and over-complicates systems.

The behavior tree representation attempts to eliminate uncertainty by limiting vocabulary to the original requirements. Large requirement sets may require the help of a composition tree representation that resolves aliases and other vocabulary problems in a prior step. The aim is to produce a deep, accurate, and holistic representation of system needs that can be understood by all readers (often stakeholders). Since the behavior tree notation uses formal semantics, it can serve as input for further processing, such as making an executable for a given set of requirements.

### Behavior tree forms

Both single and integrated (composite) behavior tree forms are important in applying behavior trees in systems and software engineering.

- **Requirement behavior trees (RBT):** Initially, individual requirement behavior trees are constructed to capture all behavioral fragments from each natural language requirement, using a rigorous translation process that preserves both intent and vocabulary. The translation process can uncover a range of defects in original natural language requirements.
- **Integrated behavior trees (IBT):** Because a set of requirements imply the integrated behavior of a system, all the individual requirement behavior trees can be composed to construct an integrated behavior tree that provides a single holistic view of the emergent integrated behavior of the system. This enables the construction of the system's integrated behavior from its requirements. An analogy to help describe this process is the transition from a randomly arranged set of jigsaw puzzle pieces to putting each of the pieces in its appropriate place. When this happens, each piece of information is placed in its intended context and their collective emergent properties become clear.

Having all the requirements converted to behavior trees (RBT) is similar to having all the pieces for a jigsaw puzzle randomly spread out on a table – until all the pieces are connected, the emergent picture remains unclear, and it is uncertain whether any pieces are missing or don’t fit. Constructing an integrated behavior tree (IBT) reveals emergent behavior and missing pieces.

### Behavior engineering process

Critical aspects of behavior engineering representation and process are listed below.

**Representation:**

- The composition tree's role in the overall process is to provide a means to overcome the imperfect knowledge associated with the large set of requirements for a system.

**Process:**

- Behavior engineering uses behavior trees to control complexity while growing a shared understanding of a complex system.

- A shared holistic understanding of a complex system integrates requirements to show its implied emergent behavior.

## History

Behavior trees and the concepts for their application in systems and software engineering were originally developed by Geoff Dromey. The first publication of some of the key ideas were in 2001. Early publications on this work used the terms "genetic software engineering" and "genetic design" to describe the application of behavior trees. The reason for originally using the word "genetic" was because sets of genes, sets of jigsaw puzzle pieces, and sets of requirements, when represented as behavior trees, all appear to share several key properties:

- They contained enough information as a set to allow them to be composed – with behavior trees, this allows a system to be built out of its requirements.
- The order in which the pieces were put together was not important – with requirements, this aids in coping with complexity.
- When all the members of the set were put together, the resulting integrated entity exhibited a set of important emergent properties.

For behavior trees, important emergent properties include:

- The integrated behavior of the system is implied by the requirements.
- The coherent behavior of each component is referred to in the requirements.

These genetic parallels, in another context, were originally spelled out by Adrian Woolfson.

Despite these legitimate genetic parallels, it was felt that this emphasis led to confusion with the concept of genetic algorithms. As a result, the term behavior engineering was introduced to describe the processes that exploit behavior trees to construct systems.

Since the behavior tree notation was originally conceived, several people from the Dependable Complex Computer-based Systems Group (DCCS – a joint University of Queensland, Griffith University research group) have made important contributions to the evolution and refinement of the behavior tree notation and usage.

Probabilistic timed behavior trees have been developed by researchers such as Rob Colvin, Lars Grunske, and Kirsten Winter of the DCCS, so that reliability, performance, and other dependability properties could be expressed.

## Key concepts

### Behavior tree notation

A behavior tree is used to formally represent the *fragment of behavior* in each requirement. In general, behavior for a large-scale system, where concurrency is admitted, appears abstractly as a set of communicating sequential processes. The behavior tree notation captures these composed component-states and represents them as a tree-like form.

Traceability tags (see Section 1.2 of behavior tree notation) in behavior tree nodes link the formal representation to the corresponding natural language requirement.

A behavior tree with leaf nodes may revert (symbolized by adding the caret operator "^") to an ancestor node to repeat behavior or start a new thread (symbolized by two carets "^^").

For a complete reference to behavior tree notation, see *Behavior Tree Notation v1.0* (2007).

### Semantics

The formal semantics of behavior trees is given via a process algebra and its operational semantics. The semantics have been used as the basis for developing simulation, model checking, and failure modes and effects analysis.

### Requirements translation

### Requirement integration

### Operations on integrated behavior trees

Once an integrated behavior tree has been composed, there are a number of important operations that can be performed upon it.

#### Inspection: defect detection and correction

In general, many defects become much more visible when there is an integrated view of the requirements and each requirement has been placed in the behavior context where it needs to execute. For example, it is much easier to tell whether a set of conditions or events emanating from a node is complete and consistent. The traceability tags also make it easy to refer back to the original natural-language requirements. There is also the potential to automate a number of defect and consistency checks on an integrated behavior tree.

When all defects have been corrected and the IBT is logically consistent and complete, it becomes a model behavior tree (MBT), which serves as a formal specification for the system's behavior that has been constructed out of the original requirements. This is the clearly defined stopping point for the analysis phase. With other modeling notations and methods (i.e. UML), it is less clear-cut when modelling can stop. In some cases, parts of a model behavior tree may need to be transformed to make the specification executable. Once an MBT has been made executable, it is possible to carry out a number of other dependability checks.

#### Simulation

A model behavior tree can be readily simulated to explore the dynamic properties of the system. Both a symbolic tool and a graphics tool have been constructed to support these activities.

#### Model checking

A translator has been written to convert a model behavior tree into the "actions systems" language. This input can then be fed into the SAL Model checker to allow checks to be made as to whether certain safety and security properties are satisfied.

#### Failure mode and effects analysis (FMEA)

Model checking has often been applied to system models to check that hazardous states can’t be reached during normal operation of the system. It is possible to combine model-checking with behavior trees to provide automated support for failure mode and effects analysis (FMEA). The advantage of using behavior trees for this purpose is that they allow the formal method aspects of the approach to be hidden from non-expert users.

#### Requirement changes

The ideal sought when responding to a change in the functional requirements for a system is that it can be quickly determined:

- where to make the change,
- how the change affects the architecture of the existing system,
- which components of the system are affected by the change, and,
- what behavioral changes will need to be made to the components (and their interfaces) that are affected by the change of requirements.

Because a system is likely to undergo many changes over its service life, it is necessary to record, manage, and optimize its evolution driven by these changes.

A traceability model, which uses behavior trees as a formal notation to represent functional requirements, reveals change impacts on different types of design constructs (documents) caused by the changes of the requirements. The model introduces the concept of evolutionary design documents that record the change history of the designs. From these documents, any version of a design document, as well as the difference between any two versions, can be retrieved. An important advantage of this model is that automated tools can support a major part of the procedure to generate these evolutionary design documents.

#### Code generation and execution

The behavior tree representation of the integrated behavior of the system offers several important advantages as an executable model. It clearly separates the tasks of *component integration* from the task of individual *component implementation*. The integrated system behavior resulting from requirement integration can serve as a foundation for design decisions. The result is a design behavior tree (DBT): an executable multi-thread component integration specification that has been built out of the original requirements.

Behavior tree models are executed in a virtual machine called the behavior run-time environment (BRE). The BRE links together components using middleware, allowing components to be independent programs written in one of several languages that can be executed in a distributed environment. The BRE also contains an expression parser that automatically performs simple operations to minimize the amount of code required to be manually implemented in the component.

Executable behavior trees have been developed for case studies including automated train protection, mobile robots with a dynamic object following, an ambulatory infusion pump, and traffic light management systems. A version of the BRE suited for embedded systems (eBRE) is also available, with reduced functionality tailored for small-footprint microcontrollers.

## Applications

Behavior tree modeling can and has been applied to a diverse range of applications over a number of years. Some of the main application areas are described below.

### Large-scale systems

Modeling large-scale systems with extensive sets of natural-language requirements has always been a major focus for testing behavior trees and the overall behavior engineering process. Conducting these evaluations and trials of the method has involved work with a number of industry partners and government departments in Australia. The systems studied have included a significant number of defense systems, enterprise systems, transportation systems, information systems, health systems, and sophisticated control systems with stringent safety requirements. The results of these studies have all been classified as commercial-in-confidence. However, the results of the extensive industry trials with Raytheon Australia are presented below in the Industry Section. This work has shown that translating requirements into integrated static and dynamic behavior-tree views revealed substantially more major defects than the company’s standard review processes detected.

### Embedded systems

Failure of a design to meet a system's requirements can result in schedule and cost overruns. If there are also critical dependability issues, not satisfying system requirements can have life-threatening consequences. However, in current approaches, ensuring that requirements are met is often delayed until late in the development process, during a cycle of testing and debugging.. This work describes how the system development approach, behavior engineering, can be used to develop software for embedded systems.

### Hardware – software systems

Many large-scale systems consist of a mixture of co-dependent software and hardware. The different nature of software and hardware means they’re often modeled separately using different approaches. This can subsequently lead to integration problems due to incompatible assumptions about hardware/software interactions. These problems can be overcome by integrating behavior trees with the Modelica mathematical modeling approach. The environment and hardware components are modeled using Modelica and integrated with an executable software model that uses behavior trees.

### Role-based access control

To ensure correct implementation of complex access control requirements, it is important that the validated and verified requirements are effectively integrated with the rest of the system. It is also important that the system can be validated and verified early in the development process. An integrated, role-based access control model has been developed. The model is based on the graphical behavior tree notation and can be validated by simulation, as well as verified using a model checker. Using this model, access control requirements can be integrated with the rest of the system from the outset, because: a single notation is used to express both access control and functional requirements; a systematic and incremental approach to constructing a formal behavior tree specification can be adopted; and the specification can be simulated and model checked. The effectiveness of the model has been evaluated using a case study with distributed access control requirements.

### Biological systems

Because behavior trees describe complex behavior, they can be used for describing a range of systems not limited to those that are computer-based.

### Game AI modeling

While behavior trees have become popular for modeling the artificial intelligence in computer games such as Halo and Spore, these types of trees are very different from the ones described on this page and are closer to a combination of hierarchical finite-state machines or decision trees. Soccer-player modeling has also been a successful application of behavior trees.

### Model-Based Testing

Model-based testing is an approach to software testing that requires testers to create test models from requirements of Software Under Test (SUT). Traditionally, modeling languages such as UML statecharts, finite-state machines (FSMs), extended finite-state machines (EFSMs), and flowcharts have been used. Recently, an interesting approach in which Event-Driven Swim Lane Petri Net (EDSLPN) is used as the modeling language also appeared. Behavior tree notation should be considered as a good modeling notation to MBT also, and it has a few advantages among other notations:

1. It has the same expressiveness level as UML state charts and EDSLPN.
2. It is intuitive to use as a modeling notation due to its graphical nature.
3. Each behavior tree node has a requirement tag; these greatly facilitate the creation of a traceability matrix from requirement to test artifact.

## Scalability and industry applications

The first industry trials to test the feasibility of the method and refine its capability were conducted in 2002. Over the last three years, a number of systematic industry trials on large-scale defense, transportation, and enterprise systems have been conducted. This work has established that the method scales to systems with large numbers of requirements but also that it is important to use tool support in order to efficiently navigate and edit the resultant large integrated views of graphical data. On average, over a number of projects, 130 confirmed major defects per 1000 requirements have consistently been found after normal reviews and corrections have been made. With less mature requirements sets, much higher defect rates have been observed.

## Advantages

As a behavior modeling representation, behavior trees have a number of significant benefits and advantages:

- They employ a well-defined and effective strategy for dealing with requirement complexity, particularly where the initial needs of a system are expressed using hundreds or thousands of requirements written in natural language. This significantly reduces the risk on large-scale projects.
- By rigorously translating then integrating requirements at the earliest possible time, they provide a more effective means for uncovering requirement defects than competing methods.
- They employ a single, simple notation for analysis, specification, and to represent the behavior design of a system.
- They represent the system behavior as an executable integrated whole.
- They build the behavior of a system out of its functional requirements in a directly traceable way, which aids verification and validation.
- They can be understood by stakeholders without the need for formal methods training. By strictly retaining the vocabulary of the original requirements, this eases the burden of understanding.
- They have a formal semantics, they support concurrency, they are executable, and they can be simulated, model checked, and used to undertake failure mode and effects analysis.
- They can be used equally well to model human processes, to analyze contracts, to represent forensic information, to represent biological systems, and many other applications. In each case, they deliver the same benefits in terms of managing complexity and seeing things as a whole. They can also be used for safety critical systems, embedded systems, and real-time systems.
