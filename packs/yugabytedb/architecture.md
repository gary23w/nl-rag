---
title: "Architecture"
source: https://docs.yugabyte.com/preview/architecture/
domain: yugabytedb
license: CC-BY-SA-4.0
tags: yugabytedb, distributed sql, postgres compatible, distributed database
fetched: 2026-07-02
---

# Architecture

Internals of query, transactions, sharding, replication, and storage layers

YugabyteDB is a distributed database that seamlessly combines the principles of distributed systems, where multiple machines collaborate, with the familiar concepts of traditional databases, where data is organized in tables with standard interfaces for reading and writing data.

Unlike traditional centralized databases, YugabyteDB is designed to manage and process data across multiple nodes or servers, ensuring resiliency, consistency, high availability, scalability, fault tolerance, and other design goals.

Check out YugabyteDB

key concepts

for your quick reference.

## Layered architecture

In general, operations in YugabyteDB are split logically into 2 layers, the query layer and the storage layer. The query layer is responsible for handling user requests and sending the requests to the right data. The storage layer is responsible for optimally storing the data on disk and managing replication and consistency.

(YugabyteDB Layered Architecture)

## Query layer

For operating (CRUD) on the data that is split and stored across multiple machines, YugabyteDB provides two APIs, YSQL and YCQL. The query layer takes the user query submitted via the API and sends or fetches data to and from the right set of tablets.

To understand how the query layer is designed, see

Query layer

.

## Storage layer

The tablet data is optimally stored and managed by DocDB, a document store that has been built on top of RocksDB for higher performance and persistence.

To understand how data storage works in YugabyteDB, see

DocDB

.

## Sharding

YugabyteDB splits table data into smaller pieces called tablets so that the data can be stored in parts across multiple machines. The mapping of a row to a tablet is deterministic and this process is known as sharding.

To learn more about the various sharding schemes, see

Sharding

.

## Replication

Tablets are replicated for resiliency, high availability, and fault tolerance. Each tablet has a leader that is responsible for consistent reads and writes to the data of the tablet and a few followers. The replication is done using the Raft protocol to ensure consistency of data across the leader and followers.

To understand how replication works, see

Replication

.

## Transactions

Transactions are a set of operations (CRUD) that are executed atomically with the option to roll back all actions if any operation fails.

To understand how transactions work in YugabyteDB, see

Transactions

.

## Master server

The master service acts a catalog manager and cluster orchestrator, and manages many background tasks.

For more details, see

YB-Master

.

## TServer

YugabyteDB splits table data into tablets. These tablets are maintained and managed on each node by the TServer.

For more details, see

YB-TServer

.
