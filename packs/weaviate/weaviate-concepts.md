---
title: "Concepts"
source: https://weaviate.io/developers/weaviate/concepts
domain: weaviate
license: CC-BY-SA-4.0
tags: weaviate, vector database, vector search engine, hierarchical navigable small world
fetched: 2026-07-02
---

# Concepts

The **Concepts** section explains various aspects related to Weaviate and its architecture to help you get the most out of it. You can read these sections in any order.

Quickstart

If you are after a practical guide with code examples, check out the quickstart tutorial.

#### Course: A Quick Tour of Weaviate

Become familiar with Weaviate's architecture, core concepts, and key capabilities. Understand how its features and integrations map to AI builders' needs.

Open Academy Course

## Core concepts

**Data structure**

- How Weaviate deals with data objects, including how they are stored, represented, and linked to each other.

**Modules**

- An overview of Weaviate's module system, including what can be done with modules, existing module types, and custom modules.

**Indexing**

- Read how data is indexed within Weaviate using inverted and ANN indexes, and about configurable settings.

**Vector indexing**

- Read more about Weaviate's vector indexing architecture, such as the HNSW algorithm, distance metrics, and configurable settings.

**Vector quantization**

- Read more about Weaviate's vector quantization options.

## Weaviate Architecture

The figure below gives a 30,000 feet view of Weaviate's architecture.

(Weaviate module APIs overview)

You can learn more about the individual components in this figure by following these guides:

**Learn about storage inside a shard**

- How Weaviate stores data
- How Weaviate makes writes durable
- How an inverted index, a vector index and an object store interact with each other

**Ways to scale Weaviate horizontally**

- Different motivations to scale
- Sharding vs. Replication
- Configuring a cluster
- Consistency

**How to plan resources**

- The roles of CPU, Memory and GPUs
- How to size a cluster correctly
- Speeding up specific processes
- Preventing bottlenecks

**Filtered vector search**

- Combine vector search with filters
- Learn how combining an HNSW with an inverted index leads to high-recall, high-speed filtered queries

**User-facing interfaces**

- Design philosophy behind user-facing APIs
- Role of the REST and GraphQL APIs

**Replication architecture**

- About replication
- Weaviate's implementation
- Use cases

Have a question or feedback? Here's how to reach us.

Community Forum

Ask questions and connect with other developers on our Community forum.

Support

Weaviate Cloud user or customer? Find the right channel on the Support page.
