---
title: "JanusGraph"
source: https://docs.janusgraph.org/
domain: janusgraph
license: CC-BY-SA-4.0
tags: janusgraph, distributed graph database, apache tinkerpop, gremlin query language
fetched: 2026-07-02
---

# Introduction

## The Benefits of JanusGraph

JanusGraph is designed to support the processing of graphs so large that they require storage and computational capacities beyond what a single machine can provide. Scaling graph data processing for real time traversals and analytical queries is JanusGraph’s foundational benefit. This section will discuss the various specific benefits of JanusGraph and its underlying, supported persistence solutions.

### General JanusGraph Benefits

- Support for very large graphs. JanusGraph graphs scale with the number of machines in the cluster.
- Support for very many concurrent transactions and operational graph processing. JanusGraph’s transactional capacity scales with the number of machines in the cluster and answers complex traversal queries on huge graphs in milliseconds.
- Support for global graph analytics and batch graph processing through the Hadoop framework.
- Support for geo, numeric range, and full text search for vertices and edges on very large graphs.
- Native support for the popular property graph data model exposed by Apache TinkerPop.
- Native support for the graph traversal language Gremlin.
- Numerous graph-level configurations provide knobs for tuning performance.
- Vertex-centric indices provide vertex-level querying to alleviate issues with the infamous super node problem.
- Provides an optimized disk representation to allow for efficient use of storage and speed of access.
- Open source under the liberal Apache 2 license.

### Benefits of JanusGraph with Apache Cassandra

- Continuously available with no single point of failure.
- No read/write bottlenecks to the graph as there is no master/slave architecture.
- Elastic scalability allows for the introduction and removal of machines.
- Caching layer ensures that continuously accessed data is available in memory.
- Increase the size of the cache by adding more machines to the cluster.
- Integration with Apache Hadoop.
- Open source under the liberal Apache 2 license.

### Benefits of JanusGraph with HBase

- Tight integration with the Apache Hadoop ecosystem.
- Native support for strong consistency.
- Linear scalability with the addition of more machines.
- Strictly consistent reads and writes.
- Convenient base classes for backing Hadoop MapReduce jobs with HBase tables.
- Support for exporting metrics via JMX.
- Open source under the liberal Apache 2 license.

### JanusGraph and the CAP Theorem

> Despite your best efforts, your system will experience enough faults that it will have to make a choice between reducing yield (i.e., stop answering requests) and reducing harvest (i.e., giving answers based on incomplete data). This decision should be based on business requirements.
> 
> — Coda Hale

When using a database, the CAP theorem should be thoroughly considered (C=Consistency, A=Availability, P=Partition tolerance). JanusGraph is distributed with 3 supporting backends: Apache Cassandra, Apache HBase, and Oracle Berkeley DB Java Edition. Note that BerkeleyDB JE is a non-distributed database and is typically only used with JanusGraph for testing and exploration purposes.

HBase gives preference to consistency at the expense of yield, i.e. the probability of completing a request. Cassandra gives preference to availability at the expense of harvest, i.e. the completeness of the answer to the query (data available/complete data).
