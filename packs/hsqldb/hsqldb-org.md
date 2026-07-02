---
title: "HSQLDB"
source: https://hsqldb.org/
domain: hsqldb
license: CC-BY-SA-4.0
tags: hsqldb database, hypersql database, java database, embedded database
fetched: 2026-07-02
---

### (hsqldb.org Home Page)

### HSQLDB - 100% Java Database

Version 2.7.4

23rd Anniversary Release

October 2024. Version 2.7.4 of HyperSQL Database adds features from the latest SQL:2023 standard, including ANY_VALUE and LISTAGG aggregate functions and CAST with templates. Zip package at the download link above contains Java 11 module jars and Java 8 jars for HSQLDB and SQL Tool. Jars are also available at

Maven repositories

.

HSQLDB (HyperSQL DataBase) is the leading SQL relational database system written in Java. It offers a small, fast multithreaded and transactional database engine with in-memory and disk-based tables and supports embedded and server modes. It includes a powerful command line

SQL tool

and simple GUI query tools.

HSQLDB supports the widest range of SQL Standard features seen in any open source database engine: SQL:2023 core language features and an extensive list of SQL:2023 optional features. It supports full Advanced ANSI-92 SQL with only two exceptions. Many extensions to the Standard, including syntax compatibility modes and features of other popular database engines, are also supported.

HyperSQL is fully multithreaded and supports high performance 2PL and MVCC (multiversion concurrency control) transaction control models. See the list of features in the latest version.

Recent releases added support for JSON constructor functions as well as direct CSV data load and unload. Temporal system-versioned tables keep all the data changes over time, allowing queries to view historic snapshots and, with PERIOD predicates, data changes over any period of time. Fine-grained row-level access control governs visibility and permissions on rows of data. Log-based synchronization keeps replicas in sync. Support for Java 8 java.time classes in JDBC, table spaces for disk-based tables, UUID type for columns, SYNONYM for tables and functions, and auto-updated TIMESTAMP columns on row updates, are some of the recent features. Other features include: The ability to cancel long-running statements from JDBC as well as from admin sessions. UTF-16 file support for text table sources. MySQL compatibility for REPLACE, INSERT IGNORE and ON DUPLICATE KEY UPDATE statements.

HSQLDB has been constantly developed for over 20 years and is used as a database and persistence engine in over 1700 Open Source Software projects and many commercial products. The latest versions are extremely stable and reliable. It is known for its small size, ability to execute completely or partly in memory, its flexibility and speed.

HSQLDB is completely free to use and distribute under our licenses, based on the standard BSD license and fully compatible with all major open source licenses.

(pole position graph)

The database performance test package PolePosition compares the performance of relational and object databases for storing objects. We ran the PolePosition 0.4 tests with HSQLDB 2.2.6 embedded and server (both with disk tables with sync-on-commit), Apache Derby embedded and MySQL+InnoDB server. See the results, which show the query processing improvements since HSQLDB 2.0

### Background

HyperSQL is developed and published by the The HSQL Development Group. The group was formed in 2001 and has released several major versions of the database over the years. Version 2.0 was released in 2010 with a brand new transactional core engine and JDBC implementation. The engine has been developed much further in version 2.7.

Direct downloads from SourceForge exceed 2,000,000 copies, with hundreds of millions of copies distributed as part of other software packages.

HyperSQL was selected as the SourceForge Project of the Month for January 2012. An interview with core developers is published here.

(SourceForge Logo)     (Our ISP...The BEST on the planet!!!)

###### *Contents of this page are ©2001-2024 The HSQL Development Group. All rights reserved.*
