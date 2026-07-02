---
title: "Replication Overview"
source: https://mariadb.com/kb/en/replication-overview/
domain: mariadb
license: CC-BY-SA-4.0
tags: mariadb, aria storage engine, galera cluster, innodb engine
fetched: 2026-07-02
---

# Replication Overview

For the complete documentation index, see

llms.txt

. This page is also available as

Markdown

.

ChatGPT

# Replication Overview

Explore the core concepts of MariaDB standard replication. Learn about the primary-replica architecture, data redundancy strategies, and how to scale read operations effectively.

In MariaDB 11.8, the default character set and collation have changed. This has implications on replicating to older replicas, particularly replicas running MariaDB 10.6 or older.

See for details, and how to configure MariaDB 11.8+ primaries to replicate to older replicas.

## Overview

Replication is a feature allowing the contents of one or more servers (called primaries) to be mirrored on one or more servers (called replicas).

You can exert control over which data to replicate. All databases, one or more databases, or tables within a database can each be selectively replicated.

The main mechanism used in replication is the . If binary logging is enabled, all updates to the database (data manipulation and data definition) are written into the binary log as binlog events. Replicas read the binary log from each primary in order to access the data to replicate. A is created on the replica, using the same format as the binary log, and this is used to perform the replication. Old relay log files are removed when no longer needed.

A replica server keeps track of the position in the primary's binlog of the last event applied on the replica. This allows the replica server to re-connect and resume from where it left off after replication has been temporarily stopped. It also allows a replica to disconnect, be cloned and then have the new replica resume replication from the same primary.

Primaries and replicas do not need to be in constant communication with each other. It's quite possible to take servers offline or disconnect from the network, and when they come back, replication will continue where it left off.

## Replication Formats

There are three kinds of replication format – essentially, they're binary log formats, and therefore documented on this page: :

- Statement-based replication (SBR)
- Row-based replication (RBR)
- Mixed replication

## Replication Uses

Replication is used in a number of common scenarios. Uses include:

- Scalability. By having one or more replicas, reads can be spread over multiple servers, reducing the load on the primary. The most common scenario for a high-read, low-write environment is to have one primary, where all the writes occur, replicating to multiple replicas, which handle most of the reads.
- Data analysis. Analyzing data may have too much of an impact on a primary server, and this can similarly be handled on a replica, while the primary continues unaffected by the extra load.
- Backup assistance. can more easily be run if a server is not actively changing the data. A common scenario is to replicate the data to a replica, which is then disconnected from the primary with the data in a stable state. Backup is then performed from this server. See .
- Distribution of data. Instead of being connected to a remote primary, it's possible to replicate the data locally and work from this data instead.

## Common Replication Setups

### Standard Replication

- Provides infinite read scale out.
- Provides high-availability by upgrading replica to primary.

### Ring Replication

- Provides read and write scaling.
- Doesn’t handle conflicts.
- If one primary fails, replication stops.

### Ring Replication with slaves

- Provides read and write scaling.
- Doesn’t handle conflicts.
- If one primary fails, replication stops.

### Ring Replication with replication through slaves

- Provides read and write scaling.
- Doesn’t handle conflicts.
- If one primary fails, replication stops.

### Star Replication

- Provides read and write scaling.
- Doesn’t handle conflicts.
- Have to use replication filters to avoid duplication of data.
- , which is a multi-primary (multi-master) cluster for MariaDB, has a similar configuration and can handle conflicts.

### Multi-Source Replication

- Allows you to combine data from different sources.
- Different domains executed independently in parallel on all replicas.

## Cross-Version Replication Compatibility

The following table describes replication compatibility between different MariaDB Server versions. In general, the replica should be of the same or a later version. The constraint also applies to minor/patch releases:

Primary→

Replica ↓

✅

⛔

⛔

⛔

⛔

⛔

✅

✅

⛔

⛔

⛔

⛔

✅

✅

✅

⛔

⛔

⛔

✅

✅

✅

✅

⛔

⛔

✅

✅

✅

✅

✅

⛔

✅

✅

✅

✅

✅

✅

- ✅: This combination is supported.
- ⛔: This combination is not supported.

Note: where it is not officially supported to replicate to a server with a lesser minor version, replication can still be safe for:

- DMLs logged in ROW binlog_format, and
- DMLS logged in STATEMENT format and DDLs where neither use features that do not yet exist on the replica

provided the configurations for each server allow for consistent behavior in the execution of the events (i.e. the execution of the event should not be reliant on newer configuration variables, character sets/collations, etc, that don't exist on the replica). Additionally note, if binlog_format=MIXED, it may be possible that the higher-versioned server (primary) may consider it safe to log a transaction using STATEMENT binlog format, while the older-versioned replica categorizes it as unsafe, which will result in an error while the replica tries to execute the transaction. See for more details on unsafe statements.

For replication compatibility details between MariaDB and MySQL, see .
