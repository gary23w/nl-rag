---
title: "Database abstraction layer"
source: https://en.wikipedia.org/wiki/Database_abstraction_layer
domain: web2py-framework
license: CC-BY-SA-4.0
tags: web2py python framework, full stack python framework, python web framework, web2py database abstraction
fetched: 2026-07-02
---

# Database abstraction layer

A **database abstraction layer** (**DBAL** or **DAL**) is an application programming interface which unifies the communication between a computer application and databases such as SQL Server, IBM Db2, MySQL, PostgreSQL, Oracle or SQLite. Traditionally, all database vendors provide their own interface that is tailored to their products. It is up to the application programmer to implement code for the database interfaces that will be supported by the application. Database abstraction layers reduce the amount of work by providing a consistent API to the developer and hide the database specifics behind this interface as much as possible. There exist many abstraction layers with different interfaces in numerous programming languages. If an application has such a layer built in, it is called **database-agnostic**.

## Database levels of abstraction

### Physical level (lowest level)

The lowest level connects to the database and performs the actual operations required by the users. At this level the conceptual instruction has been translated into multiple instructions that the database understands. Executing the instructions in the correct order allows the DAL to perform the conceptual instruction.

Implementation of the physical layer may use database-specific APIs or use the underlying language standard database access technology and the database's version SQL.

Implementation of data types and operations are the most database-specific at this level.

### Conceptual or logical level (middle or next highest level)

The conceptual level consolidates external concepts and instructions into an intermediate data structure that can be devolved into physical instructions. This layer is the most complex as it spans the external and physical levels. Additionally it needs to span all the supported databases and their quirks, APIs, and problems.

This level is aware of the differences between the databases and able to construct an execution path of operations in all cases. However the conceptual layer defers to the physical layer for the actual implementation of each individual operation.

### External or view level

The external level is exposed to users and developers and supplies a consistent pattern for performing database operations. Database operations are represented only loosely as SQL or even database access at this level.

Every database should be treated equally at this level with no apparent difference despite varying physical data types and operations.

## Database abstraction in the API

Libraries unify access to databases by providing a single low-level programming interface to the application developer. Their advantages are most often speed and flexibility because they are not tied to a specific query language (subset) and only have to implement a thin layer to reach their goal. As all SQL dialects are similar to one another, application developers can use all the language features, possibly providing configurable elements for database-specific cases, such as typically user-IDs and credentials. A thin-layer allows the same queries and statements to run on a variety of database products with negligible overhead.

Popular use for database abstraction layers are among object-oriented programming languages, which are similar to API-level abstraction layers. In an object-oriented language like C++ or Java, a database can be represented through an object, whose methods and members (or the equivalent thereof in other programming languages) represent various functionalities of the database. They also share advantages and disadvantages with API-level interfaces.

## Language-level abstraction

An example of a database abstraction layer on the language level would be ODBC that is a platform-independent implementation of a database abstraction layer. The user installs specific driver software, through which ODBC can communicate with a database or set of databases. The user then has the ability to have programs communicate with ODBC, which then relays the results back and forth between the user programs and the database. The downside of this abstraction level is the increased overhead to transform statements into constructs understood by the target database.

Alternatively, there are thin wrappers, often described as *lightweight* abstraction layers, such as OpenDBX and libzdb. Finally, large projects may develop their own libraries, such as, for example, libgda for GNOME.

## Arguments

### In favor

- Development period: software developers only have to know the database abstraction layer's API instead of all APIs of the databases their application should support. The more databases should be supported the bigger is the time saving.
- Wider potential install-base: using a database abstraction layer means that there is no requirement for new installations to utilise a specific database, i.e. new users who are unwilling or unable to switch databases can deploy on their existing infrastructure.
- Future-proofing: as new database technologies emerge, software developers won't have to adapt to new interfaces.
- Developer testing: a production database may be replaced with a desktop-level implementation of the data for developer-level unit tests.
- Added Database Features: depending on the database and the DAL, it may be possible for the DAL to add features to the database. A DAL may use database programming facilities or other methods to create standard but unsupported functionality or completely new functionality. For instance, the DBvolution DAL implements the standard deviation function for several databases that do not support it.

### Against it

- Speed: any abstraction layer will reduce the overall speed more or less depending on the amount of additional code that has to be executed. The more a database layer abstracts from the native database interface and tries to emulate features not present on all database backends, the slower the overall performance. This is especially true for database abstraction layers that try to unify the query language as well like ODBC.
- Dependency: a database abstraction layer provides yet another functional dependency for a software system, i.e. a given database abstraction layer, like anything else, may eventually become obsolete, outmoded or unsupported.
- Masked operations: database abstraction layers may limit the number of available database operations to a subset of those supported by the supported database backends. In particular, database abstraction layers may not fully support database backend-specific optimizations or debugging features. These problems magnify significantly with database size, scale, and complexity.
