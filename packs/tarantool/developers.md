---
title: "Tarantool Community Edition"
source: https://www.tarantool.io/en/developers/
domain: tarantool
license: CC-BY-SA-4.0
tags: tarantool database, in-memory database, lua application server, key-value store
fetched: 2026-07-02
---

## Why use Tarantool?

Combined DBMS and application server

Set the logic of data processing using the programming languages Lua (inside Tarantool) and Rust and C (for additional modules).

In Tarantool, the code and the database are in the same address space. Processing data at the place where it is stored allows you to reduce delays in the execution of operations.

Synchronous and asynchronous replication

Tarantool allows you to select synchronous or asynchronous replication mode depending on the task and the nature of the data.

Asynchronous replication guarantees maximum cluster speed and minimal delays. And synchronous replication, linearizable reads and the MVCC (multi-version concurrency control) engine together provide the highest possible level of consistency — strict serializable.

Secondary indexes

You can create indexes for any data in Tarantool. Searching indexed fields is faster and more predictable.

If you need to select similar data based on several criteria, you can create multiple indexes for a single table. Tarantool supports both regular and JSON indexes.

Hybrid data storage model

In Tarantool, you can choose a data storage model. Use a tabular format, and when the number and names of fields are not known in advance — JSON.

For a table, you can set a format that fixes the data types in the columns: for the entire table or only for a part of it.
