---
title: "Spanner (database)"
source: https://en.wikipedia.org/wiki/Google_Spanner
domain: fauna-db
license: CC-BY-SA-4.0
tags: fauna database, distributed document database, serializable transactions, serverless database
fetched: 2026-07-02
---

# Spanner (database)

(Redirected from

Google Spanner

)

**Spanner** is a distributed SQL database management and storage service developed by Google. It provides features such as global transactions, strongly consistent reads, and automatic multi-site replication and failover. Spanner is used in **Google F1**, the database for its advertising business Google Ads, as well as Gmail and Google Photos.

## Features

Spanner stores large amounts of mutable structured data. Spanner allows users to perform arbitrary queries using SQL with relational data while maintaining strong consistency and high availability for that data with synchronous replication.

Key features of Spanner:

- Transactions can be applied across rows, columns, tables, and databases within a Spanner universe.
- Clients can control the replication and placement of data using automatic multi-site replication and failover.
- Replication is synchronous and strongly consistent.
- Reads are strongly consistent and data is versioned to allow for stale reads: clients can read previous versions of data, subject to garbage collection windows.
- Supports a native SQL interface for reading and writing data.
- Support for Graph Query Language

## History

Spanner was first described in 2012 for internal Google data centers.

Spanner's SQL capability was added in 2017 and documented in a SIGMOD 2017 paper. It became available as part of Google Cloud Platform in 2017, under the name "Cloud Spanner".

## Architecture

Spanner uses the Paxos algorithm as part of its operation to shard (partition) data across up to hundreds of servers. It makes heavy use of hardware-assisted clock synchronization using GPS clocks and atomic clocks to ensure global consistency. TrueTime is the brand name for Google's distributed cloud infrastructure, which provides Spanner with the ability to generate monotonically increasing timestamps in data centers around the world.

Google's F1 SQL database management system (DBMS) is built on top of Spanner, replacing Google's custom MySQL variant.
