---
title: "Entity component system"
source: https://en.wikipedia.org/wiki/Entity_component_system
domain: game-dev
license: CC-BY-SA-4.0
tags: game development, game engine, entity component system, collision detection, pathfinding, game physics
fetched: 2026-07-02
---

# Entity component system

**Entity component system** (**ECS**) is a software architectural pattern. An ECS consists of entities composed of data components, along with systems that operate on those components. It is most associated with video game development for the representation of game world objects.

ECS prioritizes composition over inheritance. Every entity is defined not by a type hierarchy, but by the components associated with it. Systems act globally over all entities that have the required components. For example, a food system might iterate through every entity with a relevant component tracking hunger, and act on them to push them a little away from satiation at time intervals. Entities lacking the component like terrain or items would be naturally ignored by the food system.

Due to an ambiguity in the English language, an interpretation of the name is that an ECS is a system comprising entities and components. In the 2002 talk at GDC, Scott Bilas compared a C++ object system and his new custom component system. This is consistent with a traditional use of *system* terms in general systems engineering with Common Lisp Object System and type system as examples.

Although mostly found in video game development, the ECS can be useful in other domains, such as in robotics simulators like Gazebo.

## Characteristics

ECS combines orthogonal, well-established ideas in general computer science and programming language theory. For example, components can be seen as a mixin idiom in various programming languages. Components are a specialized case under the general delegation approach and meta-object protocol. That is, any complete component object system can be expressed with the *templates* and *empathy* model within The Orlando Treaty vision of object-oriented programming.

**Entity**

An entity represents a general-purpose object. In a game engine context, for example, every coarse game object is represented as an entity. Usually, it only consists of a unique ID. Implementations typically use a plain

integer

for this.

**Component**

A component characterizes an

entity

as possessing a particular aspect, and (the component) holds the data needed to model that aspect. For example, every game object that can take damage might have a Health component associated with its entity. Implementations typically use

structs

,

classes

, or

associative arrays

.

**System**

A system is a process that acts on all entities with the desired components. For example, a physics system may query for entities having mass, velocity and position components, iterate over the results, and do physics calculations for each entity using the set of components.

The behavior of an entity can be changed at runtime by systems that add, remove or modify components. This eliminates the ambiguity problems of deep and wide inheritance hierarchies often found in object-oriented programming techniques that are difficult to understand, maintain, and extend. Common ECS approaches are highly compatible with, and are often combined with, data-oriented design techniques. Data for all instances of a component are contiguously stored together in physical memory, enabling efficient memory access for systems that operate over many entities.

## History

In 1963, Ivan Sutherland's Sketchpad stored the visual elements of a drawing using an early form of an ECS. Instead of encapsulating points in different objects (e.g. lines, circles, rectangles) points were stored in a ring buffer, and visual elements were only referencing them. When moving a point, this allowed updating all the shapes and constraints using it.

In 1998, *Thief: The Dark Project* pioneered an ECS. The engine was later used for its sequel, as well as *System Shock 2*.

In 2002, Scott Bilas of Gas Powered Games (Dungeon Siege) gave a seminal talk on ECS. This inspired numerous later well-known implementations.

In early January 2007, Mick West who worked on the Tony Hawk series, shared his experiences on the process of ECS adoption at Neversoft.

Also in 2007, the team working on *Operation Flashpoint: Dragon Rising* experimented with ECS designs, including those inspired by Bilas/*Dungeon Siege*, and Adam Martin later wrote a detailed account of ECS design, including definitions of core terminology and concepts. In particular, Martin's work popularized the ideas of systems as a first-class element, entities as identifiers, components as raw data, and code stored in systems, not in components or entities.

In 2015, Apple Inc. introduced GameplayKit, an API framework for iOS, macOS and tvOS game development that includes an implementation of ECS.

In October 2018 the company Unity released its megacity demo that utilized a tech stack built on an ECS. Unity's ECS runs on a powerful optimized architecture known as DOTS, which "empowers creators to scale processing in a highly performant manner".

## Variations

The data layout of different ECS's can differ as well as the definition of components, how they relate to entities, and how systems access entities' components.

### Martin's ECS

Adam Martin defines in his blog series what he considers an Entity–Component–System.

An entity only consists of an ID for accessing components. It is a common practice to use a unique ID for each entity. This is not a requirement, but it has several advantages:

- The entity can be referred using the ID instead of a pointer. This is more robust, as it would allow for the entity to be destroyed without leaving dangling pointers.
- It also helps for saving the state externally, when the state is loaded again, there is no need for pointers to be reconstructed.
- Data can be shuffled around in memory as needed, as long as the pointers are adjusted accordingly.
- Entity IDs can be used when communicating over a network to uniquely identify the entity.

Some of these advantages can also be achieved using smart pointers.

Components have no game code (behavior) inside of them. The components don't have to be located physically together with the entity, but should be easy to find and access using the entity.

"Each System runs continuously (as though each System had its own private thread) and performs global actions on every Entity that possesses a Component or Components that match that System's query."

### The Unity game engine

Unity's layout has tables, each with columns of components. In this system an entity *type* is based on the components it holds. For every entity *type* there is a table (called an *archetype*) holding columns of components that match the components used in the entity. To access a particular entity one must find the correct archetype (table) and index into each column to get each corresponding component for that entity.

## Common patterns in ECS use

The normal way to transmit data between systems is to store the data in components, and then have each system access the component sequentially. For example, the position of an object can be updated regularly. This position is then used by other systems. If there are a lot of different infrequent events, a lot of flags will be needed in one or more components. Systems will then have to monitor these flags every iteration, which can become inefficient. A solution could be to use the observer pattern. All systems that depend on an event subscribe to it. The action from the event will thus only be executed once, when it happens, and no polling is needed.

The ECS has no trouble with dependency problems commonly found in object-oriented programming since components are simple data buckets and have no dependencies. Each system will typically query the set of components an entity must have for the system to operate on it. For example, a render system might register the model, transformations, and drawable components. When it runs, the system will perform its logic on any entity that has all of those components. Other entities are simply skipped, with no need for complex dependency trees. However, this can be a place for bugs to hide, since propagating values from one system to another through components may be hard to debug. ECS may be used where uncoupled data needs to be bound to a given lifetime.

The ECS uses composition, rather than inheritance trees. An entity will be typically made up of an ID and a list of components that are attached to it. Any game object can be created by adding the correct components to an entity. This allows the developer to easily add features to an entity, without any dependency issues. For example, a player entity could have a *bullet* component added to it, which would then meet the requirements to be manipulated by some *bulletHandler* system, which then could result in that bullet doing damage to other objects by running into them.

The merits of using ECS for storing the game state have been proclaimed by many game developers like Adam Martin. One good example is the blog posts by Richard Lord, where he discusses the merits and why ECS-designed game data storage systems are so useful.
