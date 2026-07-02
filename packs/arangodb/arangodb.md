---
title: "ArangoDB"
source: https://en.wikipedia.org/wiki/ArangoDB
domain: arangodb
license: CC-BY-SA-4.0
tags: arangodb, multi-model database, aql query, graph database
fetched: 2026-07-02
---

# ArangoDB

**ArangoDB** is a graph database system developed by ArangoDB Inc. ArangoDB is a multi-model database system since it supports three data models (graphs, JSON documents, key/value) with one database core and a unified query language AQL (ArangoDB Query Language). AQL is mainly a declarative language and allows the combination of different data access patterns in a single query.

ArangoDB is a NoSQL database system but AQL is similar in many ways to SQL, it uses RocksDB as a storage engine.

## History

ArangoDB GmbH was founded in 2014 by Claudius Weinberger and Frank Celler. They originally called the database system “A Versatile Object Container", or AVOC for short, leading them to call the database AvocadoDB. Later, they changed the name to ArangoDB. The word "arango" refers to a little-known avocado variety grown in Cuba.

In January 2017 ArangoDB raised a seed round investment of 4.2 million Euros led by Target Partners. In March 2019 ArangoDB raised 10 million dollars in series A funding led by Bow Capital. In October 2021 ArangoDB raised 27.8 million dollars in series B funding led by Iris Capital.

## Release history

| Release | First Release | Latest Minor Version | Latest Release | Feature Notes | Reference |
|---|---|---|---|---|---|
| 3.11 | 2023-05-30 | 3.11.5 | 2023-11-09 | Faster query performance across search and graph. Data science and analytics operational enhancements. Improved user experience for database administration and management. | Release Notes |
| 3.10 | 2022-10-04 | 3.10.11 | 2023-10-19 | Native ARM support, including native support for Apple Silicon. Support for computed values (persistent document attributes that are generated when a document is created or updated). Parallelism for sharded graphs. A graph traversal algorithm to query for all paths with the shortest value, between two documents. | Release Notes |
| 3.9 | 2022-02-15 | 3.9.12 | 2023-08-23 | Collections replicated on all cluster nodes can be combined with graphs sharded by document attributes to enable more local execution of graph queries ("Hybrid SmartGraphs", "Hybrid Disjoint SmartGraphs"). Language-agnostic tokenization of text ("Segmentation Analyzer"). | Release Notes |
| 3.8 | 2021-07-29 | 3.8.9 | 2023-03-27 | Graph traversal algorithms to enumerate all paths between two vertices ("k Paths") and to emit paths in order of increasing edge weights ("Weighted Traversals"). Support for sliding window queries to aggregate adjacent documents, value ranges and time intervals. Geo-spatial queries can be combined with full-text search. Flexible data field pre-processing with custom queries ("AQL Analyzer") and the ability to chain built-in and custom analyzers ("Pipeline Analyzer"). Hardware-accelerated on-disk encryption. | Release Notes |
| 3.7 | 2020-09-16 | 3.7.17 | 2022-02-01 | Graphs replicated on all cluster nodes to execute graph traversals locally ("SatelliteGraphs"). Document validation using JSON Schema. Wildcard and fuzzy search support for full-text search. Key rotation for superuser JWT tokens, TLS certificates, and on-disk encryption keys. | Release Notes |
| 3.6 | 2020-01-08 | 3.6.16 | 2021-09-06 | Option to store all collections of a database on a single cluster node, to combine the performance of a single server and ACID semantics with a fault-tolerant cluster setup ("OneShard"). Parallel execution of queries on several cluster nodes. Late document materialization to only fetch the relevant documents from SORT/LIMIT queries and early pruning of non-matching documents in full collection scans. Inlining of certain subqueries to improve execution time. | Release Notes |
| 3.5 | 2019-08-21 | 3.5.7 | 2020-12-30 | Multi-document transactions with individual begin and commit / abort commands ("Stream Transactions"). Time-based removal of expired documents ("Time-to-live Index"). Stop condition support for graph traversals ("Pruning in Traversals"). Graph traversal algorithm to get multiple shortest paths ("k Shortest Paths"). Co-located joins in a cluster using identically sharded collections ("SmartJoins"). Consistent snapshot backup in cluster mode. Custom text pre-processors for full-text search ("Configurable Analyzers"). Data masking capabilities for attributes containing sensitive data / PII when creating backups. | Release Notes |
| 3.4 | 2018-12-06 | 3.4.11 | 2020-09-09 | Integrated full-text search and information retrieval engine ("ArangoSearch"). Improved geo-spatial index with GeoJSON support. Insert operations can be turned into a replace automatically, in case that the target document already exists ("Repsert"). Round-robin load-balancer support for cloud environments. Query profiling to show detailed runtime information. Cluster-distributed aggregation queries. Native implementations in C++ of all built-in query functions. Multi-threaded dump and restore operations. | Release Notes |
| 3.3 | 2017-12-22 | 3.3.25 | 2020-02-28 | Datacenter to Datacenter Replication for disaster recovery ("DC2DC"). Encrypted backups. Deployment mode for single servers with automatic failover. | Release Notes |
| 3.2 | 2017-07-20 | 3.2.18 | 2019-02-02 | Distributed iterative graph processing with Pregel in single server and cluster. Collections replicated on all cluster nodes to execute joins with sharded data locally ("SatelliteCollections"). Fault-tolerant microservices. Support for composable, distance-based geo-queries. Export utility for multiple formats. Encryption of on-disk data. LDAP authentication. | Release Notes |
| 3.1 | 2016-11-03 | 3.1.29 | 2018-06-23 | Value-based sharding of large graph datasets for better data locality when traversing graphs ("SmartGraphs"). Support for vertex-centric indexes for more efficient graph traversals with filter conditions. New viewer for large graphs, supporting WebGL. Binary wire format ("VelocyStream"). Low-latency request handling using a boost-ASIO server infrastructure. Improved query editor and query explain output. Audit logging. | Release Notes |
| 3.0 | 2016-07-23 | 3.0.12 | 2016-11-23 | Cluster support with synchronous replication and automatic failover. Binary storage format ("VelocyPack"). Persistent indexes that are stored on disk for faster restarts. | Release Notes |

## Features

- JSON: ArangoDB uses JSON as a default storage format, but internally it uses ArangoDB VelocyPack – a fast and compact binary format for serialization and storage. ArangoDB can natively store a nested JSON object as a data entry inside a collection. Therefore, there is no need to disassemble the resulting JSON objects. Thus, the stored data would simply inherit the tree structure of the JSON data.
- Predictable performance: ArangoDB is written mainly in C++ and manages its own memory to avoid unpredictable performance arising from garbage collection.
- Scaling: ArangoDB provides scaling through clustering.
- Reliability: ArangoDB provides datacenter-to-datacenter replication.
- Kubernetes: ArangoDB runs on Kubernetes, including cloud-based Kubernetes services Amazon Elastic Kubernetes Service (EKS), Google Kubernetes Engine (GKE), and Microsoft Azure Kubernetes Service (AKS).
- Microservices: ArangoDB provides integration with native JavaScript microservices directly on top of the DBMS using the Foxx framework.
- Multiple query languages: The database has its own query language, AQL (ArangoDB Query Language), and also provides GraphQL to write flexible native web services directly on top of the DBMS.
- Search: ArangoDB's search engine combines Boolean retrieval capabilities with generalized ranking components allowing for data retrieval based on a precise vector space model.
- Pregel algorithm: Pregel is a system for large scale graph processing. Pregel is implemented in ArangoDB and can be used with predefined algorithms, e.g. PageRank, Single-Source Shortest Path and Connected components.
- Transactions: ArangoDB supports user-definable transactions. Transactions in ArangoDB are atomic, consistent, isolated, and durable (ACID), but only if data is not sharded.

AQL (ArangoDB Query Language) is the SQL-like query language used in ArangoDB. It supports CRUD operations for both documents (nodes) and edges, but it is not a data definition language (DDL). AQL does support geospatial queries.

AQL is JSON-oriented:

```mw
// Return every document in a collection
FOR doc IN collection 
  RETURN doc
  
// Count the number of documents in a collection
FOR doc IN collection
    COLLECT WITH COUNT INTO length
    RETURN length

// Add a new document into our collection
INSERT { _key: "john", name: "John", age: 45 } INTO collection

// Update document with key of “john” to have age 46.
UPDATE { _key: "john", age: 46 } IN collection

// Add an attribute numberOfLogins for all users with status active:
FOR u IN users
  FILTER u.active == true
  UPDATE u WITH { numberOfLogins: 0 } IN users
```

## Editions

- Community Edition: ArangoDB Community Edition is a graph database with native multi-model database capabilities written mainly in C++ and was available under an open-source license (Apache 2). In October 2023, the source code license was changed from Apache 2.0 to Business Source License, while the license for the pre-compiled binaries was changed from Apache 2.0 to a "ArangoDB Community License", which "limits its use for commercial purposes and imposes a 100GB limit on dataset size within a single cluster"
- Commercial self-managed: ArangoDB Enterprise is a paid subscription that includes graph-aware sharding (called “SmartGraphs”) and collection replication (called “Satellite Collections”) to reduce query times, and increased security.
- Cloud: ArangoDB is offered as a cloud service called Oasis, providing ArangoDB databases as a Service (DBaaS). ArangoDB Oasis provides the functionality of an ArangoDB cluster deployment while minimizing the amount of administrative effort required. ArangoDB Oasis run on multiple cloud service providers, include AWS, Azure, and Google Cloud.
