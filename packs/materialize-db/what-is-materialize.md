---
title: "What is Materialize?"
source: https://materialize.com/docs/overview/what-is-materialize/
domain: materialize-db
license: CC-BY-SA-4.0
tags: materialize database, streaming sql database, incremental view maintenance, timely dataflow
fetched: 2026-07-02
---

# What is Materialize?

View as Markdown

Materialize is the live data layer for apps and AI agents. To keep results up-to-date as new data arrives, Materialize incrementally updates results as it ingests data rather than recalculating results from scratch.

## Materialize offerings

Materialize is available as:

| Offering | Description | Get Started 🚀 |
|---|---|---|
| **Materialize Cloud** | Materialize Cloud is a fully-managed service for Materialize. | Sign up for a free trial account on Materialize Cloud and try out the Quickstart. |
| **Materialize Self-Managed** | Deploy and operate Materialize in your Kubernetes environment. Whereas Materialize Cloud gives you a fully managed service, Materialize Self-Managed allows you to deploy Materialize in your own infrastructure. Self-managed Materialize is available as a paid Enterprise Edition and a free Community Edition: Feature Enterprise Edition Community Edition **Maximum Usage Limits (Memory)** None 24 GiB **Maximum Usage Limits (Disk)** None 48 GiB **Support** Per terms of your license Community slack or messenger app **License** Enterprise License - Contact Us BSL/Privacy Policy | Install self-managed and try out the Quickstart. |
| **Materialize Emulator** | Materialize Emulator is an all-in-one Docker image that provides the fastest way to get hands-on experience with Materialize for local development. | Download and run Materialize Emulator and try out the Quickstart. |
|   |   |   |

## Key features

Materialize combines the accessibility of SQL databases with a streaming engine that is horizontally scalable, highly available, and strongly consistent.

### Incremental updates

In traditional databases, materialized views help you avoid re-running heavy queries, typically by caching queries to serve results faster. But you have to make a compromise between the freshness of the results, the cost of refreshing the view, and the complexity of the SQL statements you can use.

In Materialize, you don’t have to make such compromises. Materialize supports incrementally updated view results that are **always fresh** (even when using complex SQL statements, like multi-way joins with aggregations) for *both*:

- Indexed views and
- Materialized views.

How? Its engine is built on Timely and Differential Dataflow — data processing frameworks backed by many years of research and optimized for this exact purpose.

### Standard SQL support

Like most databases, you interact with Materialize using **SQL**. You can build complex analytical workloads using **any type of join** (including non-windowed joins and joins on arbitrary conditions) as well as leverage new SQL patterns enabled by streaming like **Change Data Capture (CDC)**, **temporal filters**, and **subscriptions**.

Materialize follows the SQL standard (SQL-92) implementation and aims for compatibility with the PostgreSQL dialect. It **does not** aim for compatibility with a specific version of PostgreSQL. This means that Materialize might support syntax from any released PostgreSQL version, but does not provide full coverage of the PostgreSQL dialect. The implementation and performance of specific features (like window functions) might also differ, because Materialize uses an entirely different database engine based on Timely and Differential Dataflow.

If you need specific syntax or features that are not currently supported in Materialize, please submit a feature request.

### Real-time data ingestion

Materialize provides **native connectors** that allow ingesting data from various external systems:

Databases (CDC)

- PostgreSQL
- MySQL
- SQL Server
- CockroachDB
- MongoDB

Message Brokers

- Kafka
- Redpanda

Webhooks

- Amazon EventBridge
- Segment
- Other webhooks

For more information, see Ingest Data and Integrations.

### PostgreSQL wire-compatibility

Every database needs a protocol to standardize communication with the outside world. Materialize uses the PostgreSQL wire protocol, which allows it to integrate out-of-the-box with many SQL clients and other tools in the data ecosystem that support PostgreSQL — like dbt.

Don’t see the a tool that you’d like to use with Materialize listed under Tools and integrations? Let us know by submitting a feature request!

### Strong consistency guarantees

By default, Materialize provides the highest level of transaction isolation: **strict serializability**. This means that it presents as if it were a single process, despite spanning a large number of threads, processes, and machines. Strict serializability avoids common pitfalls like eventual consistency and dual writes, which affect the correctness of your results. You can adjust the transaction isolation level depending on your consistency and performance requirements.

## Learn more

- Key concepts
- Get started with Materialize

Back to top ↑
