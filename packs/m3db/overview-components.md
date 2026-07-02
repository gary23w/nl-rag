---
title: "Components"
source: https://m3db.io/docs/overview/components/
domain: m3db
license: CC-BY-SA-4.0
tags: m3db, distributed time series database, m3 metrics platform, prometheus monitoring
fetched: 2026-07-02
---

# Components

- Quickstart
- Create a Cluster
- Overview
- Kubernetes Operator
  - Getting Started
  - Configuration
- How To Guides
- Operational Guides
- Integrations
- FAQs
- Architecture
  - M3DB
  - M3 Aggregator
  - M3 Query
- Reference
  - M3DB
  - M3 Coordinator
  - M3 Query

# Components

## M3 Coordinator

M3 Coordinator is a service that coordinates reads and writes between upstream systems, such as Prometheus, and M3DB. It is a bridge that users can deploy to access the benefits of M3DB such as long term storage and multi-DC setup with other monitoring systems, such as Prometheus. See this presentation for more on long term storage in Prometheus.

## M3DB

M3DB is a distributed time series database that provides scalable storage and a reverse index of time series. It is optimized as a cost effective and reliable realtime and long term retention metrics store and index. For more details, see the M3DB documentation.

## M3 Query

M3 Query is a distributed query engine for querying realtime and historical data stored in M3DB nodes, supporting several query languages. It is designed to support both low latency realtime queries and queries that can take longer to execute, aggregating over larger datasets for analytical use cases.

For example, if you are using the Prometheus remote write endpoint with M3 Coordinator, you can use M3 Query instead of the Prometheus remote read endpoint. By doing so, you get all the benefits of M3 Query’s engine such as block processing. As M3 Query provides a Prometheus compatible API, you can use 3rd party graphing and alerting solutions like Grafana.

## M3 Aggregator

M3 Aggregator is a dedicated metrics aggregator that provides stateful stream-based downsampling before storing metrics in M3DB nodes. It uses dynamic rules stored in etcd .

It uses leader election and aggregation window tracking, leveraging etcd to manage this state, to reliably emit at-least-once aggregations for downsampled metrics to long term storage. This provides cost effective and reliable downsampling & roll up of metrics.

M3 Coordinator can also perform this role, but M3 Aggregator shards and replicates metrics, whereas M3 Coordinator is not and requires care to deploy and run in a highly available way.

Similar to M3DB, M3 Aggregator supports clustering and replication by default. This means that metrics are correctly routed to the instance(s) responsible for aggregating each metric and you can configure multiple M3 Aggregator replicas so that there are no single points of failure for aggregation.

M3 Aggregator is in heavy development to make it more usable without requiring you to write your own compatible producer and consumer.
