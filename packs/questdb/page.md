---
title: "QuestDB Documentation: SQL time-series guides"
source: https://questdb.com/docs/
domain: questdb
license: CC-BY-SA-4.0
tags: questdb database, time series database, sql time series, column-oriented dbms
fetched: 2026-07-02
---

# Introduction

QuestDB is an open source time-series database engineered for low latency. It uses a column-oriented, time-partitioned storage engine with memory-mapped files and vectorized (SIMD) execution to support high-throughput ingestion and millisecond-level analytical queries. The system is built from scratch with a zero-GC Java core and focused C++/Rust components, in a compact codebase optimized for cache locality and predictable tail latency. SQL is extended with time-series operators such as `SAMPLE BY`, `LATEST ON`, `ASOF JOIN`, and `WINDOW JOIN`. See Architecture for details.

Quick start

Live demo

Test your skills

## About this documentation

This documentation covers both **QuestDB Open Source** and **QuestDB Enterprise**.

QuestDB Enterprise builds on top of QuestDB Open Source, using it as its core library. Everything in open source works in Enterprise, but not the other way around. Enterprise adds features like high availability, advanced security, RBAC, automated backups, and multi-tier storage with seamless object storage integration.

## Get started

1. **Quick start** - Install and run QuestDB
2. **Schema design** - Design your tables
3. **Ingest data** - Bring your data using QuestDB clients
4. **Query data** - Analyze with SQL

## Guides

### Create database

Set up your first QuestDB database and start storing time-series data.

Read more

### Capacity planning

Select a storage medium, plan, size and compress your QuestDB deployment.

Read more

### Working with time

It's about time. Learn how to work with timestamps and timezones in QuestDB.

Read more

### Backup and restore

See the methods to backup and restore your QuestDB deployment.

Read more

## Resources

### Query overview

Learn about our powerful extended SQL and how to use it to query QuestDB.

### Language clients

Explore our language clients and how to use them to ingest data into QuestDB.

### Configuration

See all of our available configuration options and fine-tune to match your use case.

### Third-Party Tools

Our recommended third-party tools can aid you in analyzing and visualizing your data.
