---
title: "Embedded database"
source: https://en.wikipedia.org/wiki/Embedded_database
domain: apache-derby
license: CC-BY-SA-4.0
tags: apache derby, java embedded database, javadb, relational database
fetched: 2026-07-02
---

# Embedded database

An **embedded database** system is a database management system (DBMS) that is tightly integrated with application software, and is embedded within the application rather than provided as a standalone system. It is a broad technology category that includes:

- database systems with differing application programming interfaces (SQL as well as proprietary, native APIs)
- database architectures (client-server and in-process)
- storage modes (on-disk, in-memory, and combined)
- database models (relational, object-oriented, entity–attribute–value model, network/CODASYL)
- target markets

The term “embedded” is sometimes used to refer to use on embedded devices (as opposed to the definition given above). However, only a small subset of embedded database systems are used in real-time embedded systems such as telecommunications switches and consumer electronics. (See mobile database for small-footprint databases that can be used on embedded devices.)

## Implementations

Major embedded database products include, in alphabetical order:

- Actian Zen (Actian)
- Advantage Database Server (SAP)
- ArcticDB (Man Group)
- Badger
- Berkeley DB (Oracle)
- DuckDB (DuckDB Labs)
- CSQL
- Extensible Storage Engine (Microsoft)
- eXtremeDB (McObject)
- Firebird Embedded (Fairbird Foundation)
- H2
- HSQLDB
- Informix Dynamic Server (IDS) (IBM)
- InfinityDB (Boiler Bay)
- InnoDB (Oracle)
- InterBase (Embarcadero Technologies)
- Kùzu
- LanceDB
- Lightning Memory-Mapped Database (LMDB) (Symas)
- Mimer SQL
- MonetDB (Embedded version)
- ObjectBox
- ObjectDB
- RocksDB
- solidDB
- SQLite
- SQL Server Express LocalDB (Microsoft)
- TursoDB
- Sophia – an embeddable key-value storage engine

## Storage engine comparison

### Advantage Database Server

Advantage Database Server (ADS) is an embedded database management system developed by Sybase. It provides both Indexed Sequential Access Method (ISAM) and relational data access and is compatible with multiple platforms, including Windows, Linux, and Netware. It is available as a royalty-free local file-server database or as a full client-server system. ADS is highly scalable, with no administration, and supports a variety of integrated development environments (IDEs), such as .NET Framework (.NET), Object Pascal (Delphi), Visual FoxPro (FoxPro), as well as supported programming languages, like PHP, Visual Basic (VB), Visual Objects (VO), Vulcan, Clipper, Perl, Java, and xHarbour.

### Apache Derby

Apache Derby is an embeddable SQL database engine written entirely in Java. It is fully transactional and supports multi-user access, and is available under the Apache license. Derby is actively maintained. It is also distributed as part of Oracle's Java SE Development Kit (JDK) under the name of Java DB.

### Empress Embedded Database

Empress Embedded Database was developed by Empress Software, Inc., a privately held company founded in 1979. It is a relational database management system that has been embedded in a range of applications, including medical systems, network routers, nuclear power plant monitors, and satellite management systems. Empress is an ACID-compliant, SQL database engine with APIs for C, C++, Java, JDBC, ODBC, SQL, ADO.NET, and kernel-level APIs. Applications developed using these APIs can be run in standalone or client-server modes. Empress Embedded Database runs on Linux, Unix, Microsoft Windows, and real-time operating systems.

### Extensible Storage Engine

Extensible Storage Engine (ESE) is an ISAM data storage technology developed by Microsoft. It serves as a core component of Microsoft Exchange Server and Active Directory, allowing applications to store and retrieve data using indexed and sequential access. ESE is also used by Windows Mail and Desktop Search in Windows Vista to store indexes and property information, respectively.

### eXtremeDB

eXtremeDB, launched by McObject LLC as an in-memory embedded database, was designed specifically for real-time embedded systems. The initial product was later joined by eXtremeDB High Availability (HA) for fault-tolerant applications. The eXtremeDB family now includes 64-bit and transaction logging editions, as well as the hybrid eXtremeDB Fusion, which combines in-memory and on-disk data storage. In 2008, McObject introduced eXtremeDB Kernel Mode, an embedded DBMS designed to run in an operating system kernel.

eXtremeDB is used in real-time and embedded systems worldwide. McObject also offers Perst, an open source, object-oriented embedded database for Java, Java ME, .NET, .NET Compact Framework, and Silverlight.

### Firebird Embedded

Firebird Embedded is a relational database engine and an open-source fork of InterBase. It is ACID-compliant, supports triggers and stored procedures, and is available on Linux, macOS, and Windows. It has the same features as the Classic and SuperServer versions of Firebird. Starting with Firebird 2.5, two or more threads or applications can access the same database simultaneously. Firebird Embedded acts as a local server for one-threaded client accessing its databases. For example, this allows ASP.NET web applications to work properly, because each user runs in a separate thread, so two users can access the same database at the same time without a conflict. Firebird Embedded exports the standard Firebird API entry points. Unlike SQLite or Access databases, Firebird Embedded databases can be moved to a full Firebird server without modification and are multi-platform, running on Linux and macOS with full ASP.NET Mono support.

Although it can operate within an application process, Firebird is not truly embedded because it cannot be statically linked.

### H2

H2 is an open-source database engine written in Java. It supports both embedded and server modes, as well as clustering, and can run within the Google App Engine environment. It supports encrypted database files using AES or XTEA.

Development of H2 began in May 2004, and it was first published on December 14, 2005. H2 is dual-licensed and is available under a modified version of the Mozilla Public License (MPL) or the unmodified Eclipse Public License (EPL) 1.0.

### HailDB, formerly Embedded InnoDB

HailDB is a standalone, embeddable form of the InnoDB Storage Engine. Because it is based on the same codebase as InnoDB, it includes many of the same features, such as high performance and scalability, multiversion concurrency control (MVCC), row-level locking, deadlock detection, fault tolerance, and automatic crash recovery.

As an embedded engine independent of MySQL, HailDB does not include server components such as networking or object-level permissions. By eliminating MySQL server overhead, it has a relatively small footprint and is well suited for embedding in applications that require high performance and concurrency.

As with many embedded database systems, HailDB is designed to be accessed primarily through an ISAM-like C API rather than SQL, although a limited SQL variant is supported.

The project is no longer maintained as of 2015.

### HSQLDB

HSQLDB is an open-source relational database management system with a BSD-like license that runs within the same Java Virtual Machine as the embedded application. It supports a variety of in-memory and disk-based table modes, Unicode, and SQL:2016.

### InfinityDB

InfinityDB is a sorted, hierarchical key-value store. It is available in encrypted and client-server editions. The database provides transactional support, data compression, and operates within a single file, enabling simplified deployment and minimal administration.

APIs include the ItemSpace interface, a ConcurrentNavigableMap view, and support for JSON. The RemoteItemSpace component can redirect embedded API calls to other database instances. The client-server edition includes a lightweight servlet server, web-based administration and database browsing tools, and REST support for Python.

### Informix Dynamic Server

Informix Dynamic Server (IDS) is an enterprise-class, embeddable database server that combines features such as low footprint, programmability, and autonomic capabilities with enterprise database features including high availability and flexible replication. IDS is used in embedded scenarios such as IP telephony call-processing systems, point-of-sale applications, and financial transaction processing systems.

### InterBase

InterBase is a cross-platform, Unicode-enabled SQL database that can be embedded within turn-key applications. It supports symmetric multiprocessing (SMP), on-disk AES-256 encryption, SQL-92 compliance, and ACID properties, and is available on Windows, macOS, Linux, Solaris, iOS, and Android platforms.

InterBase is used in both small- to medium-sized and large enterprise environments, supporting multi-user and mobile application development. *InterBase Light* is a free version designed for mobile devices and is suitable for mobile applications. Organizations can upgrade to a paid version as requirements for features such as change management and security increase. InterBase has been adopted in industries including defense, airspace, oil and gas, and manufacturing.

### Kùzu

Kùzu is an embeddable graph database management system that supports the Cypher query language. It implements a range of existing and novel state-of-art storage, indexing, and query processing techniques to support the management and querying of large graphs.

Kùzu achieves its performance through a combination of join algorithms, including binary and worst-case optimal joins, as well as factorization and vectorized query execution on a columnar storage layer, along with compression and parallelization techniques common in modern database systems. Kùzu is developed and maintained by Kùzu Inc., a startup based in Waterloo, Ontario, Canada, and is available as open-source software under the MIT license.

### LevelDB

LevelDB is an ordered key-value store created by Google as a compact implementation of the Bigtable storage design. It is provided as a library, with a native API in C++. It also includes official C wrappers for most functionality, and third-party wrappers are available for languages such as Python, PHP, Go, Node.js, and Objective C.

Google distributes LevelDB under the New BSD License.

### LMDB

Lightning Memory-Mapped Database (LMDB) is a memory-mapped key-value database developed for the OpenLDAP Project. It is written in C, and its API is modeled after the Berkeley DB API, but simplified. The library is compact, typically compiling to under 40 KB of x86 object code.

LMDB implements B+ trees with multiversion concurrency control (MVCC), a single-level store, copy-on-write, and provides full ACID transactions without deadlocks. It is optimized for high read concurrency: readers require no locks, readers do not block writers, and writers do not block readers, allowing read performance to scale linearly across multiple threads and CPUs. Third-party wrappers are available for C++, Erlang and Python. LMDB is distributed under the OpenLDAP Public License. As of 2013, the OpenLDAP Project has deprecated the use of Berkeley DB in favor of LMDB.

### Mimer SQL

Mimer SQL is a proprietary relational database server. An embedded, zero-maintenance version is available, featuring a small footprint due to its modular design, full support for the SQL standard, and ports to Windows, Linux, Automotive Grade Linux, Android, QNX, INTEGRITY, and other platforms.

### MonetDB/e

MonetDB/e is the embedded version of the open-source MonetDB SQL column store engine. It is available for C, C++, Java (JDBC), and Python, and is distributed under the MonetDB License, based on MPL 2.0. Its predecessor, MonetDBLite (for R, Python, and Java), is no longer maintained and has been replaced by MonetDB/e.

### MySQL Embedded Server Library

The Embedded MySQL Server Library provides most of the features of the standard MySQL server as a linkable library that runs within the context of a client process. After initialization, clients can use the same C API calls as when communicating with a separate MySQL server, but with lower communication overhead and without the need for a separate database process.

### NexusDB

NexusDB is the commercial successor to the FlashFiler database, which is now open source. Both databases can be embedded in Delphi applications to create stand-alone executables with full database functionality.

### ObjectDB

ObjectDB is an object database for Java that can be used in either client-server mode or embedded (in process) mode.

### Oracle Berkeley DB

Oracle's embedded database is Berkeley DB, which Oracle acquired from Sleepycat Software. Berkeley DB was originally developed at the University of California. It is a fast, open-source embedded database and is used in several well-known open-source products, including the Linux and BSD Unix operating systems, the Apache Web server, and the OpenOffice productivity suite. In recent years, some projects have switched to using Lightning Memory-Mapped Database (LMDB), citing better performance in key scenarios and a simpler "less is more" design, as well as changes to Berkeley DB's licensing.

### RocksDB

RocksDB was created by Facebook as a fork of LevelDB. It focuses on performance, particularly on solid-state drives (SSDs), and adds a range of features, including transactions, backups, snapshots, bloom filters, column families, expiry, custom merge operators, more tunable compaction, statistics collection, and geospatial indexing. It is used as a storage engine inside of several other databases, including ArangoDB, Ceph, CockroachDB, MyRocks, Rocksandra, TiKV, and YugabyteDB.

### solidDB

solid DB is a hybrid on-disk/in-memory, relational database often used as an embedded system database in telecommunications equipment, network software, and similar applications. Its in-memory technology enables throughput of tens of thousands of transactions per second with response times measured in microseconds. A high-availability option maintains two synchronized copies of the data. In the event of a system failure, applications can recover access to solidDB in less than a second without data loss.

### SQLite

SQLite is a software library that provides a self-contained, serverless, zero-configuration, transactional SQL database engine. It is the most widely deployed SQL database engine in the world. The source code, written primarily in C, is in the public domain. SQLite includes both a native C library and a simple command-line client for managing its database. It is included in several operating systems, including Android, FreeBSD, iOS, macOS, and Windows 10, and is also used by the Chromium web browser and its derivatives.

### SQL Server Compact

SQL Server Compact is an embedded database by Microsoft with features including multi-process connections, T-SQL, ADO.NET Sync Services for synchronizing with back-end databases, Merge Replication with SQL Server, and programming APIs such as LINQ to SQL, LINQ to Entities, and ADO.NET. The product runs on both desktop and mobile Windows platforms. It has been in production software over a long period. SQL Server Compact has undergone multiple rebrandings and has been known by various names, including SQL CE, SQL Server CE, SQL Server Mobile, and SQL Mobile.
