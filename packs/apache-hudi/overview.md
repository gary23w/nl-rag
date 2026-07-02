---
title: "Overview"
source: https://hudi.apache.org/docs/overview/
domain: apache-hudi
license: CC-BY-SA-4.0
tags: apache hudi, incremental data lake, upsert table format, copy on write, multiversion concurrency control
fetched: 2026-07-02
---

# Overview

Version: 1.2.0

# Overview

Hello there! This overview will provide a high level summary of what Apache Hudi is and will orient you on how to learn more to get started.

## What is Apache Hudi

Apache Hudi (pronounced "hoodie") pioneered the concept of "transactional data lakes", which is more popularly known today as the data lakehouse architecture. Today, Hudi has grown into an open data lakehouse platform, with a open table format purpose-built for high performance writes on incremental data pipelines and fast query performance due to comprehensive table optimizations.

Hudi brings core database functionality directly to a data lake - tables, transactions, efficient upserts/deletes, advanced indexes, ingestion services, data clustering/compaction optimizations, and concurrency control all while keeping your data in open file formats. Not only is Apache Hudi great for streaming workloads, but it also allows you to create efficient incremental batch pipelines. Apache Hudi can easily be used on any cloud storage platform. Hudi’s advanced performance optimizations, make analytical queries/pipelines faster with any of the popular query engines including, Apache Spark, Flink, Presto, Trino, Hive, etc.

Read the docs for more use case descriptions and check out who's using Hudi, to see how some of the largest data lakes in the world including Uber, Amazon, ByteDance, Robinhood and more are transforming their production data lakes with Hudi.

Hudi-rs is the native Rust implementation for Apache Hudi, which also provides bindings to Python. It expands the use of Apache Hudi for a diverse range of use cases in the non-JVM ecosystems.

## Core Concepts to Learn

If you are relatively new to Apache Hudi, it is important to be familiar with a few core concepts:

- Hudi Timeline – How Hudi manages transactions and other table services
- Hudi File Layout - How the files are laid out on storage
- Hudi Table Types – `COPY_ON_WRITE` and `MERGE_ON_READ`
- Hudi Query Types – Snapshot Queries, Incremental Queries, Read-Optimized Queries

See more in the "Design & Concepts" section of the docs.

Take a look at recent blog posts that go in depth on certain topics or use cases.

## Getting Started

Sometimes the fastest way to learn is by doing. Try out these Quick Start resources to get up and running in minutes:

- Spark Quick Start Guide – if you primarily use Apache Spark
- Flink Quick Start Guide – if you primarily use Apache Flink
- Python/Rust Quick Start Guide (Hudi-rs) - if you primarily use Python or Rust
- Unstructured Data Quick Start Guide – store embeddings (`VECTOR`) and raw bytes (`BLOB`) and run similarity search with `hudi_vector_search`

If you want to experience Apache Hudi integrated into an end to end demo with Kafka, Spark, Hive, Presto, etc, try out the Docker Demo

## Connect With The Community

Apache Hudi is community-focused and community-led and welcomes new-comers with open arms. Leverage the following resources to learn more, engage, and get help as you get started.

### Join in on discussions

See all the ways to engage with the community here. Two most popular methods include:

- Hudi Slack Channel
- Hudi mailing list - (send any msg to subscribe)

### Come to Office Hours for help

Weekly office hours are posted here

### Community Calls

Attend monthly community calls to learn best practices and see what others are building.

## Contribute

Apache Hudi welcomes you to join in on the fun and make a lasting impact on the industry as a whole. See our contributor guide to learn more, and don’t hesitate to directly reach out to any of the current committers to learn more.

Have an idea, an ask, or feedback about a pain-point, but don’t have time to contribute? Join the Hudi Slack Channel and share!
