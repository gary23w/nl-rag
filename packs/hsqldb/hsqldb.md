---
title: "HSQLDB"
source: https://en.wikipedia.org/wiki/HSQLDB
domain: hsqldb
license: CC-BY-SA-4.0
tags: hsqldb database, hypersql database, java database, embedded database
fetched: 2026-07-02
---

# HSQLDB

**HSQLDB** (***H**yper **SQL** **D**ata**b**ase*) is a relational database management system written in Java. It has a JDBC driver and supports a large subset of SQL-92, SQL:2008, SQL:2011, and SQL:2016 standards. It offers a fast, small (around 1300 kilobytes in version 2.2) database engine which offers both in-memory and disk-based tables. Both embedded and server modes are available.

Additionally, it includes tools such as a minimal Web server, command line and GUI management tools (can be run as applets), and a number of demonstration examples. It can run on Java runtimes from version 1.1 upwards, including free Java implementations such as Kaffe.

HSQLDB is available under a BSD license. It is used as a database and persistence engine in many open source software projects, such as descendants of OpenOffice.org Base (i.e., Apache OpenOffice Base, LibreOffice Base, etc.), and the Jitsi VoIP and video-conference client since version 2.6. It is also used in commercial products, such as Mathematica and InstallAnywhere (starting with version 8.0).

## Transaction support

HSQLDB version 2.0 has three transaction control modes. It supports read committed and serializable transaction isolation levels with table level locks or with multiversion concurrency control (MVCC), or a combination of locks and MVCC. Version 1.8.1 supports transaction isolation level 0 (read uncommitted) only.

## Data storage

HSQLDB has two main table types used for durable read-write data storage, i.e., if a transaction has been successfully committed, it is guaranteed that the data will survive system failure and will keep their integrity.

The default MEMORY type stores all data changes to the disk in the form of a SQL script. During engine start-up, these commands are executed and data are reconstructed into the memory.

Another table type is CACHED, which allows one to store more data, at the cost of the slower performance. The HSQLDB engine loads them only partially and synchronizes the data to the disk on transaction commits. However, the engine always loads all rows affected during an update into the memory. This renders very large updates impossible without splitting the work into smaller parts.

Other table types allow access to comma-separated values (CSV) files. These tables can participate, for example, in queries with JOINs and simplify spreadsheet processing and read-write non-durable in-memory data storage.

## SQL features

HSQLDB 2.0 supports all the core features and many optional features of SQL:2008. Advanced features include user-defined SQL procedures and functions, schemas, datetime intervals, updatable views, arrays, lobs, full and lateral joins and set operations. Many non-standard functions such as TO_CHAR and DECODE are also supported. Extensions to standard SQL include user-defined aggregate functions.

## Releases

Several versions of HSQLDB have been released since 2001. Early versions were based on the discontinued HypersonicSQL database engine. Version 2.0, released in 2010, is mostly new code, written to conform to Standard SQL and JDBC 4 Specification.

Version 2.3.2 (released in 2014) is fully multi-threaded and supports high performance two-phase locking and MVCC (multiversion concurrency control) transaction control models.
