---
title: "Architectural Overview"
source: https://docs.janusgraph.org/getting-started/architecture/
domain: janusgraph
license: CC-BY-SA-4.0
tags: janusgraph, distributed graph database, apache tinkerpop, gremlin query language
fetched: 2026-07-02
---

# Architectural Overview

JanusGraph is a graph database engine. JanusGraph itself is focused on compact graph serialization, rich graph data modeling, and efficient query execution. In addition, JanusGraph utilizes Hadoop for graph analytics and batch graph processing. JanusGraph implements robust, modular interfaces for data persistence, data indexing, and client access. JanusGraph’s modular architecture allows it to interoperate with a wide range of storage, index, and client technologies; it also eases the process of extending JanusGraph to support new ones.

Between JanusGraph and the disks sits one or more storage and indexing adapters. JanusGraph comes standard with the following adapters, but JanusGraph’s modular architecture supports third-party adapters.

- Data storage:
  - Apache Cassandra
  - Apache HBase
  - Oracle Berkeley DB Java Edition
- Indices, which speed up and enable more complex queries:
  - Elasticsearch
  - Apache Solr
  - Apache Lucene

Broadly speaking, applications can interact with JanusGraph in two ways:

- Embed JanusGraph inside the application executing Gremlin queries directly against the graph within the same JVM. Query execution, JanusGraph’s caches, and transaction handling all happen in the same JVM as the application while data retrieval from the storage backend may be local or remote.
- Interact with a local or remote JanusGraph instance by submitting Gremlin queries to the server. JanusGraph natively supports the Gremlin Server component of the Apache TinkerPop stack.

(High-level JanusGraph Architecture and Context)
