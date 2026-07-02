---
title: "Distributed SQL"
source: https://en.wikipedia.org/wiki/Distributed_SQL
domain: cockroachdb
license: CC-BY-SA-4.0
tags: cockroachdb, distributed sql, cockroach labs, distributed database
fetched: 2026-07-02
---

# Distributed SQL

A **distributed SQL** database is a single relational database which replicates data across multiple servers. Distributed SQL databases are strongly consistent and most support consistency across racks, data centers, and wide area networks including cloud availability zones and cloud geographic zones. Distributed SQL databases typically use the Paxos or Raft algorithms to achieve consensus across multiple nodes.

Sometimes distributed SQL databases are referred to as NewSQL but NewSQL is a more inclusive term that includes databases that are not distributed databases.

## History

Google's Spanner popularized the modern distributed SQL database concept. Google described the database and its architecture in a 2012 whitepaper called "Spanner: Google's Globally-Distributed Database." The paper described Spanner as having evolved from a Big Table-like key value store into a temporal multi-version database where data is stored in "schematized semi-relational tables."

Spanner uses atomic clocks with the Paxos algorithm to accomplish consensus with regards to state distributed between servers. In 2010, and earlier implementation, ClustrixDB (now MariaDB Xpand) moved from a hardware appliance to a Paxos-based software database and was later acquired by MariaDB and added to a SaaS cloud offering called SkySQL. In 2015, two Google engineers left the company to create Cockroach DB which achieves similar results using the Raft algorithm without atomic clocks or custom hardware.

Spanner is primarily used for transactional and time-series use cases. However, Google furthered this research with a follow on paper about Google F1 which it describes as a Hybrid transactional/analytical processing database built on Spanner.

## Architecture

Distributed SQL databases have the following general characteristics:

- synchronous replication
- strong transactional consistency across at least availability zones (i.e. ACID compliance)
- relational database front end structure – meaning data represented as tables with rows and columns similar to any other RDBMS
- automatically sharded data storage
- underlying key–value storage
- native SQL implementation

Following the CAP Theorem, distributed SQL databases are "CP" or consistent and partition-tolerant. Algorithmically they sacrifice availability in that a failure of a primary node can make the database unavailable for writes.

All distributed SQL implementations require some kind of temporal synchronization to guarantee consistency. With the exception of Spanner, most do not use custom hardware to provide atomic clocks. Spanner is able to synchronize writes with temporal guarantees. Implementations without custom hardware require servers to compare clock offsets and potentially retry reads.

## Distributed SQL implementations

| Vendor | API | License model |
|---|---|---|
| Amazon Aurora | PostgreSQL & MySQL | Proprietary |
| CockroachDB | PostgreSQL-like | Proprietary |
| Google Spanner | Proprietary SQL-like | Proprietary |
| MySQL Cluster | MySQL | Open Source (GPLv2) |
| NuoDB | Proprietary SQL | Proprietary |
| YugabyteDB | PostgreSQL & Cassandra CQL-like | Open Source (Apache 2.0) |
| TiDB | MySQL-like | Open Source (Apache 2.0) |
| MariaDB XPand | MariaDB | Proprietary |
| Teradata | Proprietary SQL-like | Proprietary |
| YDB | Proprietary SQL-like, PostgreSQL-like | Open Source (Apache 2.0) |

## Compared to NewSQL

CockroachDB, YugabyteDB and others have at times referred to themselves as NewSQL databases. Some of the NewSQL databases have fundamentally different architectures, but were cited as examples of NewSQL by Matthew Aslett who coined the term. In essence, distributed SQL databases are built from the ground-up and NewSQL databases include replication and sharding technologies added to existing client-server relational databases like PostgreSQL. Some experts define DistributedSQL databases as a more specific subset of NewSQL databases.
