---
title: "Introduction"
source: https://docs.pinot.apache.org/
domain: apache-pinot
license: CC-BY-SA-4.0
tags: apache pinot, real-time olap datastore, low-latency analytics, columnar storage
fetched: 2026-07-02
---

# Introduction

For the complete documentation index, see

llms.txt

. This page is also available as

Markdown

.

# Introduction

Apache Pinot is a real-time distributed OLAP datastore purpose-built for low-latency, high-throughput analytics, and perfect for user-facing analytical workloads.

Apache Pinot™ is a real-time distributed online analytical processing (OLAP) datastore. Use Pinot to ingest and immediately query data from streaming or batch data sources (including, Apache Kafka, Amazon Kinesis, Hadoop HDFS, Amazon S3, Azure ADLS, and Google Cloud Storage).

We'd love to hear from you! to ask questions, troubleshoot, and share feedback.

Apache Pinot includes the following:

- **Ultra low-latency analytics** even at extremely high throughput.
- **Columnar data store** with several smart indexing and pre-aggregation techniques.
- **Scaling up and out** with no upper bound.
- **Consistent performance** based on the size of your cluster and an expected query per second (QPS) threshold.

It's perfect for user-facing real-time analytics and other analytical use cases, including internal dashboards, anomaly detection, and ad hoc data exploration.

### User-facing real-time analytics

User-facing analytics refers to the analytical tools exposed to the end users of your product. In a user-facing analytics application, all users receive personalized analytics on their devices, resulting in hundreds of thousands of queries per second. Queries triggered by apps may grow quickly in proportion to the number of active users on the app, as many as millions of events per second. Data generated in Pinot is immediately available for analytics in latencies under one second.

User-facing real-time analytics requires the following:

- **Fresh data.** The system needs to be able to ingest data in real time and make it available for querying, also in real time.
- **Support for high-velocity, highly dimensional event data** from a wide range of actions and from multiple sources.
- **Low latency.** Queries are triggered by end users interacting with apps, resulting in hundreds of thousands of queries per second with arbitrary patterns.
- **Reliability and high availability.**
- **Scalability.**
- **Low cost to serve.**

## Why Pinot?

Pinot is designed to execute OLAP queries with low latency. It works well where you need fast analytics, such as aggregations, on both mutable and immutable data.

**User-facing, real-time analytics**

Pinot was originally built at LinkedIn to power rich interactive real-time analytics applications, such as , , , and many more. is another example of a user-facing analytics app built with Pinot.

**Real-time dashboards for business metrics**

Pinot can perform typical analytical operations such as slice and dice, drill down, roll up, and pivot on large scale multi-dimensional data. For instance, at LinkedIn, Pinot powers dashboards for thousands of business metrics. Connect various business intelligence (BI) tools such as , , or to visualize data in Pinot.

**Enterprise business intelligence**

For analysts and data scientists, Pinot works well as a highly-scalable data platform for business intelligence. Pinot converges big data platforms with the traditional role of a data warehouse, making it a suitable replacement for analysis and reporting.

**Enterprise application development**

For application developers, Pinot works well as an aggregate store that sources events from streaming data sources, such as Kafka, and makes it available for a query using SQL. You can also use Pinot to aggregate data across a microservice architecture into one easily queryable view of the domain.

Pinot prevent any possibility of sharing ownership of database tables across microservice teams. Developers can create their own query models of data from multiple systems of record depending on their use case and needs. As with all aggregate stores, query models are eventually consistent.

## Get started

If you're new to Pinot, take a look at our Getting Started guide:

Start Here

To start importing data into Pinot, see how to import batch and stream data:

Ingestion

To start querying data in Pinot, check out our Query guide:

Querying & SQL

## Learn

For a conceptual overview that explains how Pinot works, check out the Concepts guide:

Concepts

To understand the distributed systems architecture that explains Pinot's operating model, take a look at our basic architecture section:

Architecture

Next

Start Here

Last updated 3 months ago

Was this helpful?
