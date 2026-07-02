---
title: "Storage Engines"
source: https://mariadb.com/kb/en/storage-engines/
domain: mariadb
license: CC-BY-SA-4.0
tags: mariadb, aria storage engine, galera cluster, innodb engine
fetched: 2026-07-02
---

# Storage Engines

For the complete documentation index, see

llms.txt

. This page is also available as

Markdown

.

ChatGPT

# Storage Engines

Understand MariaDB Server's storage engines. Explore the features and use cases of InnoDB, Aria, MyISAM, and other engines to choose the best option for your specific data needs.

Storage Engines Overview

An introduction to MariaDB's pluggable storage engine architecture, highlighting key engines like InnoDB, MyISAM, and Aria for different workloads.

Choosing the Right Storage Engine

A guide to selecting the appropriate storage engine based on data needs, comparing features of general-purpose, columnar, and specialized engines.

ARCHIVE

The Archive storage engine is optimized for high-speed insertion and compression of large amounts of data, suitable for logging and auditing.

ARIA

Learn about the Aria storage engine in MariaDB Server. Understand its features, advantages, and use cases, particularly for crash-safe operations and transactional workloads.

BLACKHOLE

The BLACKHOLE storage engine discards all data written to it but records operations in the binary log, useful for replication filtering and testing.

CONNECT

The main characteristic of CONNECT is to enable accessing data scattered on a machine as if it was a centralized database.

CSV

The CSV storage engine stores data in text files using comma-separated values format, allowing easy data exchange with other applications.

FederatedX

FederatedX is a storage engine that allows access to tables on remote MariaDB or MySQL servers as if they were local tables.

InnoDB

Discover InnoDB, the default storage engine for MariaDB Server. Learn about its transaction-safe capabilities, foreign key support, and high performance for demanding workloads.

MEMORY

The MEMORY storage engine stores tables in RAM for fast access, but data is lost upon server restart.

MERGE

The MERGE storage engine allows a collection of identical MyISAM tables to be treated as a single logical table, useful for managing large datasets.

Mroonga

Mroonga (formerly named Groonga Storage Engine) is a storage engine that provides fast CJK-ready full text searching using column store.

MyISAM

Explore the MyISAM storage engine in MariaDB Server. Understand its characteristics, including suitability for read-heavy workloads, and its role in specific use cases.

MyRocks

Learn about the MyRocks storage engine in MariaDB Server. Discover its advantages for flash storage, high write throughput, and compression efficiency in modern database deployments.

OQGRAPH

Explore the OQGRAPH storage engine in MariaDB Server. Learn how to efficiently manage hierarchical and complex graph data structures, perfect for social networks and bill of materials.

PERFORMANCE_SCHEMA

While technically a storage engine, PERFORMANCE_SCHEMA provides a way to inspect internal server execution details at a low level.

SEQUENCE Storage Engine

The Sequence engine generates virtual tables of number sequences on the fly, useful for generating series of integers without storing data.

S3 Storage Engine

Integrate MariaDB Server with Amazon S3 using the S3 Storage Engine. Learn how to store and retrieve data directly from cloud object storage for scalability and cost efficiency.

SphinxSE

Integrate MariaDB Server with Sphinx for advanced full-text search. The Sphinx storage engine allows you to query external Sphinx indexes directly from your database.

Spider

Explore the Spider storage engine in MariaDB Server. Learn how to shard data across multiple MariaDB and MySQL servers, enabling horizontal scaling and distributed database solutions.

VIDEX Storage Engine

The VIDEX storage engine is an aggregated, extensible engine suitable for what-if analyses in MariaDB. The name is derived from [VI]rtual in[DEX].

Converting Tables from MyISAM to InnoDB

This guide outlines the benefits and process of migrating tables from MyISAM to InnoDB, highlighting key differences like transaction support and foreign keys.

Machine Learning with MindsDB

Learn how to integrate MindsDB with MariaDB to train and query machine learning models directly using standard SQL commands.

Legacy Storage Engines

Explore legacy storage engines in MariaDB Server. This section provides information on older engines, their historical context, and considerations for migration or compatibility.

Previous

DBMS_OUTPUT

Next

Storage Engines Overview

Last updated 28 days ago

Was this helpful?
