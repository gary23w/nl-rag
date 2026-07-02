---
title: "Dynamo (storage system)"
source: https://en.wikipedia.org/wiki/Dynamo_(storage_system)
domain: dynamodb
license: CC-BY-SA-4.0
tags: dynamodb, amazon dynamodb, dynamo storage system, vector clock
fetched: 2026-07-02
---

# Dynamo (storage system)

**Dynamo** is a set of techniques that together can form a highly available key-value structured storage system or a distributed data store. It has properties of both databases and distributed hash tables (DHTs). It was created to help address some scalability issues that Amazon experienced during the holiday season of 2004. By 2007, it was used in Amazon Web Services, such as its Simple Storage Service (S3).

## Relationship to DynamoDB

Amazon DynamoDB is "built on the principles of Dynamo" and is a hosted service within the AWS infrastructure. However, while Dynamo is based on leaderless replication, DynamoDB uses single-leader replication.

## Principles

- Incremental scalability: Dynamo should be able to scale out one storage host (or “node”) at a time, with minimal impact on both operators of the system and the system itself.
- Symmetry: Every node in Dynamo should have the same set of responsibilities as its peers; there should be no distinguished node or nodes that take special roles or extra set of responsibilities.
- Decentralization: An extension of symmetry, the design should favor decentralized peer-to-peer techniques over centralized control.
- Heterogeneity: The system should be able to exploit heterogeneity in the infrastructure it runs on. For example, the work distribution must be proportional to the capabilities of the individual servers. This is essential in adding new nodes with higher capacity without having to upgrade all hosts at once.

## Techniques

| Problem | Technique | Advantage |
|---|---|---|
| Dataset partitioning | Consistent Hashing | Incremental, possibly linear scalability in proportion to the number of collaborating nodes. |
| Highly available writes | Vector Clock or Dotted-Version-Vector Sets, reconciliation during reads | Version size is decoupled from update rates. |
| Handling temporary failures | Sloppy Quorum and Hinted Handoff | Provides high availability and durability guarantee when some of the replicas are not available. |
| Recovering from permanent failures | Anti-entropy using Merkle tree | Can be used to identify differences between replica owners and synchronize divergent replicas pro-actively. |
| Membership and failure detection | Gossip-based membership protocol and failure detection | Avoids having a centralized registry for storing membership and node liveness information, preserving symmetry. |

## Implementations

Amazon published the paper on Dynamo, but never released its implementation. The index layer of Amazon S3 implements and extends many core features of Dynamo. Since then, several implementations have been created based on the paper. The paper also inspired many other NoSQL database implementations, such as Apache Cassandra, Project Voldemort and Riak.
