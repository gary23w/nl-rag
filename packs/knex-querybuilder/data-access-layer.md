---
title: "Data access layer"
source: https://en.wikipedia.org/wiki/Data_access_layer
domain: knex-querybuilder
license: CC-BY-SA-4.0
tags: knex query builder, sql query builder, database migration tool, fluent sql interface
fetched: 2026-07-02
---

# Data access layer

A **data access layer** (**DAL**) is a software architectural layer that provides access to data from one or more sources, such as a relational database, NoSQL database, SQL query engine, file system, or other persistent storage. It separates client code from the details of storage systems, query execution, connection handling, and data retrieval.

Data access layers are commonly used to centralize data access logic, reduce coupling between applications and data sources, and provide a consistent interface for retrieving, writing, or querying data. Depending on the system, a data access layer may be implemented as application code, a shared library, an intermediary service, or part of a broader database abstraction layer.

## In application architecture

In application software, a data access layer provides a boundary between business logic or application code and the systems used to store or retrieve data. For example, a data access layer may expose methods or interfaces for retrieving, writing, or querying data while hiding details such as connection management, SQL statements, storage APIs, error handling, and result conversion. Depending on the application, the layer may return objects, records, tabular results, documents, streams, or other representations of data.

A common implementation is a set of classes, functions, or methods that directly reference database queries, stored procedures, storage APIs, or other data sources. For example, instead of using commands such as *insert*, *delete*, and *update* throughout an application to access a specific table, methods such as *registerUser* or *loginUser* may be implemented inside the data access layer. Business logic methods from an application can also be mapped to the data access layer. Instead of making several database queries directly, an application can call a single DAL method that abstracts those database calls.

Applications using a data access layer may be either dependent on or independent from a particular database server. If the data access layer supports multiple database systems, the application can use any database system that the DAL can access. In either case, the data access layer provides a centralized location for calls into the underlying data store, which can make it easier to maintain, test, or port the application to other storage systems.

## Implementation patterns

A data access layer can be implemented using several patterns and technologies, including data access objects, repositories, stored procedures, query builders, database drivers, or object–relational mapping tools. These mechanisms may implement part or all of a data access layer, but are not always equivalent to the layer itself.

Object–relational mapping tools are commonly used in data access layers for object-oriented applications that map records in a relational database to objects in a programming language. Other data access layers may expose lower-level database interfaces, tabular results, document-oriented data, files, streams, or protocol-level interfaces.

## Use with multiple underlying data systems

A data access layer may be used to abstract differences between multiple underlying data systems, allowing applications to access them through a more consistent interface. In such designs, applications call the DAL rather than interacting directly with each database or storage system. The layer may then handle connection management, query generation, result mapping, error handling, and other implementation details.

A data access layer may be implemented as a shared library or as an intermediary service, such as a proxy or gateway. In this configuration, client applications or services connect to the data access layer, which then communicates with one or more underlying databases or query engines. This can provide a common location for authentication, authorization, logging, routing, and translation between different database interfaces.

## Interfaces and protocols

Data access layers may expose or use standardized interfaces and protocols for database access. Examples include Open Database Connectivity (ODBC), Java Database Connectivity (JDBC), database-native wire protocols, and newer interfaces such as Apache Arrow Database Connectivity (ADBC) and Arrow Flight SQL.

In systems that support multiple data stores, a data access layer may provide a consistent interface while using different drivers, protocols, or query mechanisms internally.

A data access layer is related to, but broader than, a data access object, which is usually an object-oriented design pattern for encapsulating access to a persistence mechanism. It is also related to a database abstraction layer, which focuses on hiding differences between database systems. In practice, the terms may overlap.
