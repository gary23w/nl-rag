---
title: "YugabyteDB"
source: https://en.wikipedia.org/wiki/YugabyteDB
domain: yugabytedb
license: CC-BY-SA-4.0
tags: yugabytedb, distributed sql, postgres compatible, distributed database
fetched: 2026-07-02
---

# YugabyteDB

**YugabyteDB** is a high-performance transactional distributed SQL database for cloud-native applications, developed by Yugabyte.

## History

Yugabyte was founded by ex-Facebook engineers Kannan Muthukkaruppan, Karthik Ranganathan, and Mikhail Bautin. At Facebook, they were part of the team that built and operated Cassandra and HBase for workloads such as Facebook Messenger and Facebook's Operational Data Store.

The founders came together in February 2016 to build YugabyteDB.

YugabyteDB was initially available in two editions: community and enterprise. In July 2019, Yugabyte open-sourced previously commercial features and launched YugabyteDB as open-source under the Apache 2.0 license.

### Funding

In October 2021, five years after the company's inception, Yugabyte closed a $188 Million Series C funding round to become a Unicorn start-up with a valuation of $1.3Bn

| Series | Date Announced | Amount | Investors |
|---|---|---|---|
| A | 10 Feb 2016 | $8M | Lightspeed Venture Partners, Jeff Rothschild |
| A | 12 Jun 2018 | $16M | Lightspeed Venture Partners, Dell Technology Capital |
| B | 09 Jun 2020 | $30M | Wipro Ventures, Lightspeed Venture Partners. Dell Technology Capital. 8VC |
| B | 03 Mar 2021 | $48M | Wipro Ventures. Lightspeed Venture Partners. Greenspring Associates, Dell Technology Capital, 8VC |
| C | 28 Oct 2021 | $188M | Wells Fargo Strategic Capital, Sapphire Ventures, Meritech Capital Partners, Lightspeed Venture Partners, Dell Technology Capital, 8VC |

## Architecture

YugabyteDB is a distributed SQL database that aims to be strongly transactionally consistent across failure zones (i.e. ACID compliance). In CAP Theorem terms YugabyteDB is a Consistent/Partition Tolerant (CP) database. YugabyteDB has two layers, a storage engine known as DocDB and the Yugabyte Query Layer.

### DocDB

The storage engine consists of a customized RocksDB combined with sharding and load balancing algorithms for the data. In addition, the Raft consensus algorithm controls the replication of data between the nodes. There is also a Distributed transaction manager and Multiversion concurrency control (MVCC) to support distributed transactions.

The engine also exploits a Hybrid Logical Clock that combines coarsely-synchronized physical clocks with Lamport clocks to track causal relationships.

The DocDB layer is not directly accessible by users.

### YugabyteDB Query Layer

Yugabyte has a pluggable query layer that abstracts the query layer from the storage layer below. There are currently two APIs that can access the database:

**YSQL** is a PostgreSQL code-compatible API based around v11.2. YSQL is accessed via standard PostgreSQL drivers using native protocols. It exploits the native PostgreSQL code for the query layer and replaces the storage engine with calls to the pluggable query layer. This re-use means that Yugabyte supports many features, including:

- Triggers & Stored Procedures
- PostgreSQL extensions that operate in the query layer
- Native JSONB support

**YCQL** is a Cassandra-like API based around v3.10 and re-written in C++. YCQL is accessed via standard Cassandra drivers using the native protocol port of 9042. In addition to the 'vanilla' Cassandra components, YCQL is augmented with the following features:

- Transactional consistency - unlike Cassandra, Yugabyte YCQL is transactional.
- JSON data types supported natively
- Tables can have secondary indexes

Currently, data written to either API is not accessible via the other API, however YSQL can access YCQL using the PostgreSQL foreign data wrapper feature.

The security model for accessing the system is inherited from the API, so access controls for YSQL look like PostgreSQL, and YCQL looks like Cassandra access controls.

## Cluster-to-cluster replication

In addition to its core functionality of distributing a single database, YugabyteDB has the ability to replicate between database instances. The replication can be one-way or bi-directional and is asynchronous. One-way replication is used either to create a read-only copy for workload off-loading or in a read-write mode to create an active-passive standby. Bi-directional replication is generally used in read-write configurations and is used for active-active configurations, geo-distributed applications, etc.

## Migration tooling

Yugabyte also provides YugabyteDB Voyager, tooling to facilitate the migration of Oracle and other similar databases to YugabyteDB. This tool supports the migration of schemas, procedural code and data from the source platform to YugabyteDB.
