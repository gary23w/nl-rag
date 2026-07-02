---
title: "Apache Cassandra"
source: https://en.wikipedia.org/wiki/Apache_Cassandra
domain: aws-keyspaces
license: CC-BY-SA-4.0
tags: aws keyspaces, amazon keyspaces, managed cassandra, wide-column database service
fetched: 2026-07-02
---

# Apache Cassandra

**Apache Cassandra** is a free and open-source database management system designed to handle large volumes of data across multiple commodity servers. The system prioritizes availability and scalability over consistency, making it particularly suited for systems with high write throughput requirements due to its LSM tree indexing storage layer. As a wide-column database, Cassandra supports flexible schemas and efficiently handles data models with numerous sparse columns. The system is optimized for applications with well-defined data access patterns that can be incorporated into the schema design. Cassandra supports computer clusters which may span multiple data centers, featuring asynchronous and masterless replication. It enables low-latency operations for all clients and incorporates Amazon's Dynamo distributed storage and replication techniques, combined with Google's Bigtable data storage engine model.

## History

Avinash Lakshman, a co-author of Amazon's Dynamo, and Prashant Malik developed Cassandra at Facebook to support the inbox search functionality. Facebook released Cassandra as open-source software on Google Code in July 2008. In March 2009, it became an Apache Incubator project and on February 17, 2010, it graduated to a top-level project.

The developers at Facebook named their database after Cassandra, the mythological Trojan prophetess, referencing her curse of making prophecies that were never believed.

## Features and limitations

Cassandra uses a distributed architecture where all nodes perform identical functions, eliminating single points of failure. The system employs configurable replication strategies to distribute data across clusters, providing redundancy and disaster recovery capabilities. The system is capable of linear scaling, which increases read and write throughput with the addition of new nodes, while maintaining continuous service.

Cassandra is categorized as an AP (Availability and Partition Tolerance) system, emphasizing availability and partition tolerance over consistency. While it offers tunable consistency levels for both read and write operations, its architecture makes it less suitable for use cases requiring strict consistency guarantees. Additionally, Cassandra's compatibility with Hadoop and related tools allows for integration with existing big data processing workflows. Eventual consistency is maintained using tombstones to manage reads, upserts, and deletes.

The system's query capabilities have notable limitations. Cassandra does not support advanced query patterns such as multi-table JOINs, ad hoc aggregations, or complex queries. These limitations stem from its distributed architecture, which optimizes for scalability and availability rather than complex query operations.

## Data model

As a wide-column store, Cassandra combines features of both key-value and tabular database systems. It implements a partitioned row store model with adjustable consistency levels. The following table compares Cassandra and relational database management systems (RDBMS).

| Feature | Cassandra | RDBMS |
|---|---|---|
| Organization | Keyspace → Table → Row | Database → Table → Row |
| Row Structure | Dynamic columns | Fixed schema |
| Column Data | Name, type, value, timestamp | Name, type, value |
| Schema Changes | Runtime modifications | Usually requires downtime |
| Data Model | Denormalized | Normalized with JOINs |

The data model consists of several hierarchical components:

### Keyspace

A keyspace in Cassandra is analogous to a database in relational systems. It contains multiple tables and manages configuration information, including replication strategy and user-defined types (UDTs).

### Tables

Tables (formerly called column families prior to CQL 3) are containers for rows of data. Each table has a name and configuration information for its stored data. Tables may be created, dropped, or altered at run-time without blocking updates and queries.

### Rows and columns

Each row is identified by a primary key and contains columns. The first component of a table's primary key is the partition key; within a partition, rows are clustered by the remaining columns of the key.

Columns contain data belonging to a row and consist of:

- A name
- A type
- A value
- Timestamp metadata (used for write conflict resolution via "last write wins")

Unlike traditional RDBMS tables, rows within the same table can have varying columns, providing a flexible structure. This flexibility distinguishes Cassandra from relational databases, as not all columns need to be specified for each row. Other columns may be indexed separately from the primary key.

## Storage model

Cassandra uses a Log Structured Merge Tree (LSM tree) index to optimize write throughput, in contrast to the B-tree indexes used by most databases.

| Feature | Cassandra | RDBMS |
|---|---|---|
| Index Structure | LSM Tree | B-Tree |
| Write Process | Append-only with Memtable | In-place updates |
| Storage Components | Commit Log, Memtable, SSTable | Data files, Transaction Log |
| Update Strategy | New entry for each change | Modify existing data |
| Delete Handling | Tombstone markers | Direct removal |
| Read Optimization | Secondary | Primary |
| Write Optimization | Primary | Secondary |

The storage architecture consists of three main components:

### Core components

- **Commit Log**: A write-ahead log that ensures write durability
- **Memtable**: An in-memory data structure that stores writes, sorted by primary key
- **SSTable** (Sorted String Table): Immutable files containing data flushed from Memtables

### Write and read processes

Write operations follow a two-stage process:

1. The write is recorded in the commit log and added to the Memtable
2. When the Memtable reaches size or time thresholds, it flushes to an SSTable

Read operations:

1. Check Memtable for latest data
2. Search SSTables from newest to oldest using bloom filters for efficiency

### Data management

#### Tombstones

Every operation (create/update/delete) generates a new entry, with deletes handled via "tombstones". While common in many databases, tombstones can cause performance degradation in delete-heavy workloads.

#### Compaction

Compaction consolidates multiple SSTables to:

- Reduce storage usage
- Remove deleted row tombstones
- Improve read performance

## Cassandra Query Language

Cassandra Query Language (CQL) is the interface for accessing Cassandra, as an alternative to the traditional Structured Query Language (SQL). CQL adds an abstraction layer that hides implementation details of this structure and provides native syntaxes for collections and other common encodings. Language drivers are available for Java (JDBC), Python (DBAPI2), Node.JS (DataStax), Go (gocql), and C++.

The key space in Cassandra is a namespace that defines data replication across nodes. Therefore, replication is defined at the key space level. Below is an example of key space creation, including a column family in CQL 3.0:

```mw
CREATE KEYSPACE MyKeySpace
  WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 3 };

USE MyKeySpace;

CREATE COLUMNFAMILY MyColumns (id text, lastName text, firstName text, PRIMARY KEY(id));

INSERT INTO MyColumns (id, lastName, firstName) VALUES ('1', 'Doe', 'John');

SELECT * FROM MyColumns;
```

Which gives:

```mw
 id | lastName | firstName
----+----------+----------
  1 | Doe      | John

(1 rows)
```

## Distributed architecture

### Gossip protocol

Cassandra uses a peer-to-peer gossip protocol for cluster communication. Nodes routinely exchange information about cluster state, including:

- Node availability status
- Schema versions
- Generation timestamps (node bootstrap time)
- Version numbers (logical clock values)

The system uses vector clocks to track information currency and ignore outdated state data.

### Seed nodes

The architecture designates certain nodes as "seed" nodes that:

- Bootstrap the cluster
- Serve as guaranteed gossip communication points
- Prevent cluster fragmentation
- Remain discoverable via service discovery methods

This design eliminates single points of failure while maintaining cluster-wide consistency of operational knowledge.

### Fault tolerance

Cassandra employs the Phi Accrual Failure Detector to manage node failures during cluster operation. Through this system, each node independently assesses the availability of other nodes during gossip communication. When a node fails to respond, it is "convicted" and removed from write operations, though it can rejoin the cluster upon resuming heartbeat signals.

To maintain data integrity during node outages, Cassandra uses a "hinted handoff" mechanism. When writing to an offline node, the coordinator node temporarily stores the write data as a "hint." Once the offline node returns to service, these hints are forwarded to restore data consistency. Notably, Cassandra only permanently removes nodes through explicit administrative decommissioning or rebuilding, preventing temporary communication failures or restarts from triggering unnecessary data rebalancing.

## Management and monitoring

Cassandra is a Java-based system that can be managed and monitored via Java Management Extensions (JMX). The JMX-compliant *Nodetool* utility, for instance, can be used to manage a Cassandra cluster. Nodetool also offers a number of commands to return Cassandra metrics pertaining to disk usage, latency, compaction, garbage collection, and more.

Since the release of Cassandra 2.0.2 in 2013, measures of several metrics are produced via the Dropwizard metrics framework, and may be queried via JMX using tools such as JConsole or passed to external monitoring systems via Dropwizard-compatible reporter plugins.

## Releases

Releases after graduation include:

| Version | Original release date | Latest version | Release date | Status |
|---|---|---|---|---|
| Unsupported: 0.6 | 2010-04-12 | 0.6.13 | 2011-04-18 | No longer maintained |
| Unsupported: 0.7 | 2011-01-10 | 0.7.10 | 2011-10-31 | No longer maintained |
| Unsupported: 0.8 | 2011-06-03 | 0.8.10 | 2012-02-13 | No longer maintained |
| Unsupported: 1.0 | 2011-10-18 | 1.0.12 | 2012-10-04 | No longer maintained |
| Unsupported: 1.1 | 2012-04-24 | 1.1.12 | 2013-05-27 | No longer maintained |
| Unsupported: 1.2 | 2013-01-02 | 1.2.19 | 2014-09-18 | No longer maintained |
| Unsupported: 2.0 | 2013-09-03 | 2.0.17 | 2015-09-21 | No longer maintained |
| Unsupported: 2.1 | 2014-09-16 | 2.1.22 | 2020-08-31 | No longer maintained |
| Unsupported: 2.2 | 2015-07-20 | 2.2.19 | 2020-11-04 | No longer maintained |
| Unsupported: 3.0 | 2015-11-09 | 3.0.29 | 2023-05-15 | No longer maintained |
| Unsupported: 3.11 | 2017-06-23 | 3.11.15 | 2023-05-05 | No longer maintained |
| Supported: 4.0 | 2021-07-26 | 4.0.18 | 2025-05-28 | Maintained until 5.1.0 release |
| Supported: 4.1 | 2022-06-17 | 4.1.9 | 2025-05-19 | Maintained until 5.2.0 release |
| Latest version: 5.0 | 2024-09-05 | 5.0.6 | 2025-10-29 | Latest release. Maintained until 5.3.0 release |
| **Legend:**UnsupportedSupported**Latest version**Preview versionFuture version |   |   |   |   |
