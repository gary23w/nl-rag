---
title: "H2 Database Engine"
source: https://en.wikipedia.org/wiki/H2_(database)
domain: h2-database
license: CC-BY-SA-4.0
tags: h2 database, h2 java database, embedded database, in-memory database
fetched: 2026-07-02
---

# H2 Database Engine

(Redirected from

H2 (database)

)

**H2** is a relational database management system written in Java. It can be used as an embedded database in Java applications or run in client–server mode.

The software is available as open source software Mozilla Public License 2.0 or the original Eclipse Public License.

## History

The development of the H2 database engine started in May 2004, and first published in December 2005. The database engine was written by Thomas Mueller. He also developed the Java database engine Hypersonic SQL. In 2001, the Hypersonic SQL project was stopped, and the HSQLDB Group was formed to continue work on the Hypersonic SQL code. The name H2 stands for Hypersonic 2, however H2 does not share code with Hypersonic SQL or HSQLDB. H2 is built from scratch.

Version 2.0.x was released in January 2022.

## Features

A subset of the SQL (Structured Query Language) standard is supported. The main programming APIs are SQL and JDBC, however the database also supports using the PostgreSQL ODBC driver by acting like a PostgreSQL server.

It is possible to create both in-memory tables, as well as disk-based tables. Tables can be persistent or temporary. Index types are hash table and tree for in-memory tables, and b-tree for disk-based tables. All data manipulation operations are transactional. Table level locking and multiversion concurrency control are implemented. The two-phase commit protocol is supported as well, but no standard API for distributed transactions is implemented.

The security features of the database are: role based access rights, encryption of the password using SHA-256 and data using the AES or the Tiny Encryption Algorithm, XTEA. The cryptographic features are available as functions inside the database as well. SSL / TLS connections are supported in the client–server mode, as well as when using the console application.

The database supports protection against SQL injection by enforcing the use of parameterized statements. In H2, this feature is called 'disabling literals'.

Two full text search implementations are included, a native implementation and one using Lucene.

A simple form of high availability is implemented: when used in the client–server mode, the database engine supports hot failover (this is commonly known as clustering). However, the clustering mode must be enabled manually after a failure.

Since version 1.1.111, H2 in-memory database can run inside the Google App Engine.
