---
title: "tarantool/README.md at master · tarantool/tarantool · GitHub"
source: https://github.com/tarantool/tarantool/blob/master/README.md
domain: tarantool
license: CC-BY-SA-4.0
tags: tarantool database, in-memory database, lua application server, key-value store
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

tarantool

/

tarantool

Public

- Notifications You must be signed in to change notification settings
- Fork 409
- Star

## Expand file tree

More file actions

More file actions

## Latest commit

## History

History

History

## File metadata and controls

91 lines (75 loc) · 4.1 KB

# Tarantool

(Actions Status) (Code Coverage) (OSS Fuzz) (Telegram) (GitHub Discussions) (Stack Overflow)

Tarantool is an in-memory computing platform consisting of a database and an application server.

It is distributed under BSD 2-Clause terms.

Key features of the application server:

- Heavily optimized Lua interpreter with incredibly fast tracing JIT compiler, based on LuaJIT 2.1.
- Cooperative multitasking, non-blocking IO.
- Persistent queues.
- Sharding.
- Cluster and application management framework.
- Access to external databases such as MySQL and PostgreSQL.
- A rich set of built-in and standalone modules.

Key features of the database:

- MessagePack data format and MessagePack based client-server protocol.
- Two data engines: 100% in-memory with complete WAL-based persistence and an own implementation of LSM-tree, to use with large data sets.
- Multiple index types: HASH, TREE, RTREE, BITSET.
- Document oriented JSON path indexes.
- Asynchronous master-master replication.
- Synchronous quorum-based replication.
- RAFT-based automatic leader election for the single-leader configuration.
- Authentication and access control.
- ANSI SQL, including views, joins, referential and check constraints.
- Connectors for many programming languages.
- The database is a C extension of the application server and can be turned off.

Supported platforms are Linux (x86_64, aarch64), Mac OS X (x86_64, M1), FreeBSD (x86_64).

Tarantool is ideal for data-enriched components of scalable Web architecture: queue servers, caches, stateful Web applications.

To download and install Tarantool as a binary package for your OS or using Docker, please see the download instructions.

To build Tarantool from source, see detailed instructions in the Tarantool documentation.

To find modules, connectors and tools for Tarantool, check out our Awesome Tarantool list.

Please report bugs to our issue tracker. We also warmly welcome your feedback on the discussions page and questions on Stack Overflow.

We accept contributions via pull requests. Check out our contributing guide.

Thank you for your interest in Tarantool!
