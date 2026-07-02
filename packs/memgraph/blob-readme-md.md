---
title: "memgraph/README.md at master · memgraph/memgraph · GitHub"
source: https://github.com/memgraph/memgraph/blob/master/README.md
domain: memgraph
license: CC-BY-SA-4.0
tags: memgraph database, in-memory graph database, cypher query language, graph analytics
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

memgraph

/

memgraph

Public

- Notifications You must be signed in to change notification settings
- Fork 243
- Star

## Expand file tree

More file actions

More file actions

## Latest commit

## History

History

History

## File metadata and controls

265 lines (213 loc) · 12.4 KB

Outline

(memgraph-repo-banner)

(license) (license) (license)

(Discord)

## 📋 Description

Memgraph is a high-performance, in-memory graph database that powers real-time AI context and graph analytics. Built in C/C++, it serves as the graph engine for GraphRAG pipelines, AI memory systems, and agentic workflows — delivering sub-millisecond multi-hop traversals for any system that needs structured, connected context alongside semantic vector or text search.

Memgraph provides both in a single query layer: built-in text and vector indexes for similarity search combined with full graph traversal, so retrieval pipelines can run as a single atomic database operation instead of being scattered across multiple systems.

The same architecture drives real-time graph analytics for fraud detection, network analysis, infrastructure monitoring, and other operational workloads where performance matters. Memgraph is fully compatible with Neo4j’s Cypher query language, ACID-compliant, and highly available.

## ⚡ Features

#### AI & Graph Intelligence

- **Indexes** - Built-in vector indexes power hybrid graph retrieval with similarity search in a single query, alongside text and geospatial indexes for keyword and location-aware queries.
- **MAGE algorithm library** - 40+ graph algorithms in C++, Python, and CUDA including PageRank, community detection, GNN-based link prediction, temporal graph networks, embeddings, and native ML.
- **Atomic GraphRAG** - Pivot search, graph expansion, ranking, and prompt assembly expressed as a single Cypher query.
- **LLM utility module** - Graph-aware context formatting for large language models.
- **AI Toolkit** - Integrations with popular agentic frameworks, MCP server, and ready-made components for building GraphRAG, AI memory, and agent workflows on top of Memgraph.
- **Real-time schema introspection** - `SHOW SCHEMA INFO` returns the full graph ontology for Text2Cypher and AI agent integration.

#### Performance & Query Power

- **In-memory C/C++ engine** - Sub-millisecond traversals with benchmarked performance.
- **Deep-path traversals** - Accumulators and path filtering without additional application logic.
- **Custom query modules** - Extend with Python, Rust, and C/C++ code natively.
- **Parallel query execution** - Concurrent query processing for high-throughput workloads.
- **Native Parquet & JSONL loading** - Load data directly from Parquet and JSONL files on local disk, S3, or HTTP endpoints.
- **Streaming support** - Ingest from Kafka, Pulsar, and RedPanda with dynamic graph algorithms that react to changes in real time.

#### Enterprise

- **High availability** - Raft-based coordination with automatic failover.
- **Multi-tenancy** - Isolated databases with per-tenant role assignments.
- **Fine-grained access control** - Role-based and label-based permissions at the node and edge level.
- **Authentication & authorization** - SSO integration, user impersonation, and 30+ granular permissions.
- **Encryption in transit, monitoring, backup & restore.**

## 🎮 Memgraph Playground

You don't need to install anything to try out Memgraph. Check out our **Memgraph Playground** sandboxes in your browser.

(Memgraph Playground)

## 💾 Download & Install

### Windows

(Windows) (Windows)

### macOS

(macOS) (macOS)

### Linux

(Linux) (Debian) (Ubuntu) (Cent OS) (Fedora) (RedHat)

### Kubernetes

(Helm)

Deploy Memgraph on Kubernetes using the official Helm charts, including charts for standalone and high-availability deployments:

```highlight
helm repo add memgraph https://memgraph.github.io/helm-charts
helm install my-memgraph memgraph/memgraph
```

You can find the binaries and Docker images on the Download Hub and the installation instructions in the official documentation.

## 🚀 Daily Builds

Stay on the cutting edge with the latest features and improvements by using Memgraph Daily Builds. Daily builds are updated frequently and allow you to test new capabilities before they reach stable releases.

(Daily Builds)

## ☁️ Memgraph Cloud

Check out Memgraph Cloud - a cloud service fully managed on AWS and available in 6 geographic regions around the world. Memgraph Cloud allows you to create projects with Enterprise instances of MemgraphDB from your browser.

(Memgraph Cloud)

## 🔗 Connect to Memgraph

Connect to the database using Memgraph Lab, mgconsole, various drivers (Python, C/C++ and others) and WebSocket.

### 🔬 Memgraph Lab

Visualize graphs and play with queries to understand your data. Memgraph Lab is a user interface that helps you explore and manipulate the data stored in Memgraph. Visualize graphs, execute ad hoc queries, and optimize their performance.

(Memgraph Cloud)

## 📁 Import data

Import data into Memgraph using Kafka, RedPanda or Pulsar streams, CSV, JSON, Parquet, and JSONL files (from local disk, S3, or HTTP), or Cypher commands.

## 💡 Best Practices

The memgraph/best-practices repository contains ready-to-use examples covering graph modeling, data import, query optimization, GraphRAG, high-availability deployment, and more.

## 🗺️ Roadmap

See what's coming next on the memgraph/roadmap.

## 📑 Documentation

The Memgraph documentation is available at memgraph.com/docs.

## ❓ Configuration

Command line options that Memgraph accepts are available in the reference guide.

## 🏆 Contributing

Welcome to the heart of Memgraph development! We're on a mission to supercharge Memgraph, making it faster, more user-friendly, and even more powerful. We owe a big thanks to our fantastic community of contributors who help us fix bugs and bring incredible improvements to life. If you're passionate about databases and open source, here's your chance to make a difference!

### Compile from Source

Learn how to download, compile and run Memgraph from source with the Quick Start guide.

### Explore Memgraph Internals

Interested in the nuts and bolts of Memgraph? Our internals documentation is where you can uncover the inner workings of Memgraph's architecture, learn how to build the project from scratch, and discover the secrets of effective contributions. Dive deep into the database!

### Dive into the Contributing Guide

Ready to jump into the action? Explore our contributing guide to get the inside scoop on how we develop Memgraph. It's your roadmap for suggesting bug fixes and enhancements. Contribute your skills and ideas!

### Code of Conduct

Our commitment to a respectful and professional community is unwavering. Every participant in Memgraph is expected to adhere to a stringent Code of Conduct. Please carefully review the complete text to gain a comprehensive understanding of the behaviors that are both expected and explicitly prohibited.

We maintain a zero-tolerance policy towards any violations. Our shared commitment to this Code of Conduct ensures that Memgraph remains a place where integrity and excellence are paramount.

### 📜 License

Memgraph Community is available under the BSL license. Memgraph Enterprise is available under the MEL license.

## ⭐ Special Thanks

We're grateful to all contributors, especially external ones, who have helped improve Memgraph through bug fixes, features, and documentation. Thank you for making Memgraph better!

## 👥 Community

- 💜 **Discord**
- 🌊 **Stack Overflow**
- 🐦 **Twitter**
- 🎥 **YouTube**

(Back to top)
