---
title: "Architecture Overview"
source: https://questdb.com/docs/concept/storage-model/
domain: questdb
license: CC-BY-SA-4.0
tags: questdb database, time series database, sql time series, column-oriented dbms
fetched: 2026-07-02
---

# Architecture Overview

QuestDB offers high-speed ingestion and low-latency analytics on time-series data. It stores data in a three-tier architecture (streaming WAL files, local binary storage, and local or remote storage in Parquet format) to improve interoperability and avoid vendor lock-in.

WHERE symbol in ('AAPL', 'NVDA')

LATEST ON timestamp PARTITION BY symbol

CREATE MATERIALIZED VIEW 'trades_OHLC'

min(price) AS low

timestamp IN today()

SELECT spread_bps(bids[1][1], asks[1][1])

FROM read_parquet('trades.parquet')

SAMPLE BY 15m

**Tier One:** Hot ingest (WAL), durable by default

Incoming data is appended to the write-ahead log (WAL) with ultra-low latency. Writes are made durable before any processing, preserving order and surviving failures without data loss. The WAL is asynchronously shipped to object storage, so new replicas can bootstrap quickly and read the same history.

**Tier Two:** Real-time SQL on live data

Data is time-ordered and de-duplicated into QuestDB's native, time-partitioned columnar format and becomes immediately queryable. Power real-time analysis with vectorized, multi-core execution, streaming materialized views, and time-series SQL (e.g., ASOF JOIN, SAMPLE BY). The query planner spans tiers seamlessly.

**Tier Three:** Cold storage, open and queryable

Older data is automatically tiered to object storage in Apache Parquet. Query it in-place through QuestDB or use any tool that reads Parquet. This delivers predictable costs, interoperability with AI/ML tooling, and zero lock-in.

This document explains QuestDB's internal architecture.

## Key components

QuestDB is comprised of several key components:

- **Storage engine:** Uses a column-oriented design to ensure high I/O performance and low latency.
- **Memory management and native integration:** The system leverages both memory mapping and explicit memory management techniques, integrating native code for performance-critical tasks.
- **Query engine:** A custom SQL parser, a just-in-time (JIT) compiler, and a vectorized execution engine process data in table page frames for better CPU use.
- **Time-series optimizations:** QuestDB is specifically designed for time-series, and it provides several optimizations, such as a designated timestamp, sequential reads, materialized views, and in-memory processing.
- **Replication:** QuestDB Enterprise supports high availability with read replicas and multi-primary configurations. See High Availability for details.
- **Observability:** QuestDB exposes real-time metrics, health checks, and structured logs to monitor performance and streamline diagnostics.
- **Web console:** The engine includes a web console for running SQL statements, bulk loading CSV files, and displaying monitoring dashboards. QuestDB Enterprise supports single sign-on (SSO) in the web console.

## Design patterns & best practices throughout the codebase

- **Immutable data structures:** The system favors immutability to avoid concurrency issues and simplify state management.
- **Modular architecture:** Each component (eg., storage, query processing, ingestion, etc.) has well-defined interfaces that enhance maintainability and decouple functionality.
- **Factory & builder patterns:** These patterns are used to centralize construction logic for complex objects such as SQL execution plans and storage buffers.
- **Lazy initialization:** Resource-intensive components initialize only when needed to reduce startup overhead.
- **Rigorous testing & benchmarks:** Unit tests, integration tests, and performance benchmarks ensure that new enhancements do not compromise reliability or performance.

## Next up

Continue to Storage Engine to learn how QuestDB stores and manages data on disk.
