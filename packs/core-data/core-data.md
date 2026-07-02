---
title: "Core Data"
source: https://en.wikipedia.org/wiki/Core_Data
domain: core-data
license: CC-BY-SA-4.0
tags: core data, object graph, object-relational mapping, persistence layer
fetched: 2026-07-02
---

# Core Data

**Core Data** is an object graph and persistence framework provided by Apple in the macOS and iOS operating systems. It was introduced in Mac OS X 10.4 Tiger and iOS with iPhone SDK 3.0. It allows data organized by the relational entity–attribute model to be serialized into XML, binary, or SQLite stores. The data can be manipulated using higher level objects representing entities and their relationships. Core Data manages the serialized version, providing object lifecycle and object graph management, including persistence. Core Data interfaces directly with SQLite, insulating the developer from the underlying SQL.

Just as Cocoa Bindings handle many of the duties of the controller in a model–view–controller design, Core Data handles many of the duties of the data model. Among other tasks, it handles change management, serializing to disk, memory footprint minimization and queries against the data.

## Usage

Core Data describes data with a high level data model expressed in terms of entities and their relationships plus fetch requests that retrieve entities meeting specific criteria. Code can retrieve and manipulate this data on a purely object level without having to worry about the details of storage and retrieval. The controller objects available in Interface Builder can retrieve and manipulate these entities directly. When combined with Cocoa bindings the UI can display many components of the data model without needing background code.

For example: a developer might be writing a program to handle vCards. In order to manage these, the author intends to read the vCards into objects, and then store them in a single larger XML file. Using Core Data the developer would drag their schema from the data designer in Xcode into an interface builder window to create a GUI for their schema. They could then write standard Objective-C or Swift code to read vCard files and put the data into Core Data managed entities. From that point on the author's code manipulates these Core Data objects, rather than the underlying vCards. Connecting the `Save` menu item to the appropriate method in the controller object will direct the controller to examine the object stack, determine which objects are dirty, and then re-write a Core Data document file with these changes.

Core Data is organized into a large hierarchy of classes, though interaction is only prevalent with a small set of them.

| Name | Use | Key methods |
|---|---|---|
| NSManagedObject | Access attributes A "row" of data | -entity -valueForKey: -setValue:forKey: |
| NSManagedObjectContext | Actions Changes | -executeFetchRequest:error: -save |
| NSManagedObjectModel | Structure Storage | -entities -fetchRequestTemplateForName: -setFetchRequestTemplate:  forName: |
| NSFetchRequest | Request data | -setEntity: -setPredicate: -setFetchBatchSize: |
| NSPersistentStoreCoordinator | Mediator Persisting the data | -addPersistentStoreWithType:  configuration:URL:  options:error: -persistentStoreForURL: |
| NSPredicate | Specify query | +predicateWithFormat: -evaluateWithObject: |

Sources:

## Storage formats

Core Data can serialize objects into XML, binary, or SQLite for storage. With the release of Mac OS X 10.5 Leopard, developers can also create their own custom atomic store types. Each method carries advantages and disadvantages, such as being human readable (XML) or more memory efficient (SQLite).

This portion of Core Data is similar to the original Enterprise Objects Framework (EOF) system, in that one can write fairly sophisticated queries. Unlike EOF, it is not possible to write your own SQL, as the underlying store may not be SQL-based. Recently, Core Data store for ODBC has been made available in ODBC framework.

Core Data schemas are standardized. If you have the Xcode Data Model file, you can read and write files in that format freely. Unlike EOF, though, Core Data is not currently designed for multiuser or simultaneous access unless you use ODBC framework.

Schema migration is also non-trivial, almost always requiring code. If other developers have access to and depend upon your data model, you may need to provide version translation code in addition to a new data model if your schema changes.

## History and genesis

Core Data owes much of its design to an earlier NeXT product, Enterprise Objects Framework (EOF).

EOF was an object-relational mapping for high-end SQL database engines such as Microsoft SQL Server and Oracle. EOF's purpose was twofold: first, to connect to the database engine and hide the implementation details; second, to read the data out of the relational format and translate that into a set of objects. Developers typically interacted only with the objects, which simplified development of complex programs, at the cost of some setup to map the data to the objects. The EOF object model was deliberately designed to make the resulting programs work in a document-like fashion; the user could edit the data locally in memory, and then write out all changes with a single Save command.

Throughout its history, EOF contained a number of bits of useful code that were not otherwise available under NeXTSTEP/OpenStep. For instance, EOF required the ability to track which objects were dirty so the system could later write them out. This was presented to the developer not only as a document-like system, but also in the form of an unlimited Undo command stack, with each command applied to the data represented as an undoable action. Many developers complained that this state management code was far too useful to be isolated in EOF, and it was later moved into the Cocoa API during the transition to Mac OS X.

Initially, what was not translated was EOF itself. EOF was used primarily along with another OpenStep-era product, WebObjects, which was an application server originally based on Objective-C. At the time, Apple was in the process of porting WebObjects to the Java programming language, and as part of this conversion, EOF became much more difficult to use from Cocoa. Once again, there was considerable complaining among 3rd party developers.

One critical realization is that the object state management system in EOF did not really have anything to do with relational databases. The same code could be, and was, used by developers to manage graphs of other objects as well. In this role, the really useful parts of EOF were those that automatically built the object sets from the raw data, and then tracked them. It is this concept that forms the basis of Core Data.
