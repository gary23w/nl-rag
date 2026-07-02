---
title: "Object graph"
source: https://en.wikipedia.org/wiki/Object_graph
domain: core-data
license: CC-BY-SA-4.0
tags: core data, object graph, object-relational mapping, persistence layer
fetched: 2026-07-02
---

# Object graph

In computer science, in an object-oriented program, groups of objects form a network through their relationships with each other, either through a direct reference to another object or through a chain of intermediate references. These groups of objects are referred to as **object graphs**, after the mathematical objects called graphs studied in graph theory.

An object graph is a view of an object system at a particular point in time. Unlike a normal data model such as a Unified Modeling Language (UML) class diagram, which details the relationships between classes, the object graph relates their instances. Object diagrams are subsets of the overall object graph.

Object-oriented applications contain complex webs of interrelated objects. Objects are linked to each other by one object either owning or containing another object or holding a reference to another object. This web of objects is called an object graph and it is the more abstract structure that can be used in discussing an application's state.

## Physical representation

An object graph is a directed graph, which might be cyclic. When stored in RAM, objects occupy different segments of the memory with their attributes and function table, while relationships are represented by pointers or a different type of global handler in higher-level languages.

## Examples

For instance, a Car class can compose a Wheel one. In the object graph a Car instance will have up to four links to its wheels, which can be named frontLeft, frontRight, back Left and back Right. An example of an adjacency list representation might be something as follows:

```
 c:Car → {front Left:Wheel, front Right:Wheel, back Left:Wheel, back Right:Wheel}.
```
