---
title: "NewSQL"
source: https://en.wikipedia.org/wiki/NewSQL
domain: gcp-spanner
license: CC-BY-SA-4.0
tags: gcp cloud spanner, globally distributed database, newsql database gcp, horizontally scalable sql
fetched: 2026-07-02
---

# NewSQL

**NewSQL** is a class of relational database management systems that seek to provide the scalability of NoSQL systems for online transaction processing (OLTP) workloads while maintaining the ACID guarantees of a traditional database system.

Many enterprise systems that handle high-profile data (e.g., financial and order processing systems) are too large for conventional relational databases, but have transactional and consistency requirements that are not practical for NoSQL systems. The only options previously available for these organizations were to either purchase more powerful computers or to develop custom middleware that distributes requests over conventional DBMS. Both approaches feature high infrastructure costs and/or development costs. NewSQL systems attempt to reconcile the conflicts.

## History

The term was first used by 451 Group analyst Matthew Aslett in a 2011 research paper discussing the rise of a new generation of database management systems. One of the first NewSQL systems was the H-Store parallel database system.

## Applications

Typical applications are characterized by heavy OLTP transaction volumes. OLTP transactions;

- are short-lived (i.e., no user stalls)
- touch small amounts of data per transaction
- use indexed lookups (no table scans)
- have a small number of forms (a small number of queries with different arguments).

However, some support hybrid transactional/analytical processing (HTAP) applications. Such systems improve performance and scalability by omitting heavyweight recovery or concurrency control.

## List of NewSQL-databases

- Apache Trafodion
- Clustrix
- CockroachDB
- Couchbase
- CrateDB
- Google Spanner
- MySQL Cluster
- NuoDB
- OceanBase
- Pivotal GemFire XD
- SequoiaDB
- SingleStore was formerly known as MemSQL.
- TIBCO Active Spaces
- TiDB
- TokuDB
- TransLattice Elastic Database
- VoltDB
- YDB
- YugabyteDB

## Features

The two common distinguishing features of NewSQL database solutions are that they support online scalability of NoSQL databases and the relational data model (including ACID consistency) using SQL as their primary interface.

NewSQL systems can be loosely grouped into three categories:

### New architectures

NewSQL systems adopt various internal architectures. Some systems employ a cluster of shared-nothing nodes, in which each node manages a subset of the data. They include components such as distributed concurrency control, flow control, and distributed query processing.

### SQL engines

The second category are optimized storage engines for SQL. These systems provide the same programming interface as SQL, but scale better than built-in engines.

### Transparent sharding

These systems automatically split databases across multiple nodes using Raft or Paxos consensus algorithm.
