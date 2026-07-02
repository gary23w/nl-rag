---
title: "Apache Phoenix"
source: https://phoenix.apache.org/
domain: apache-phoenix
license: CC-BY-SA-4.0
tags: apache phoenix, sql over hbase, apache hbase, relational layer
fetched: 2026-07-02
---

# We Put SQL Back in NoSQL

Query HBase with standard SQL and JDBC. Low latency OLTP and operational analytics for Hadoop.

Download Phoenix

Read Documentation

## Why Phoenix

The trusted data platform for OLTP and operational analytics on Hadoop.

### Standard SQL & JDBC

Use familiar SQL queries and JDBC APIs with full ACID transaction capabilities.

### Millisecond Performance

Low latency performance for small queries or seconds for tens of millions of rows.

### Schema Flexibility

Schema-on-read flexibility from the NoSQL world leveraging HBase as backing store.

### Hadoop Ecosystem

Fully integrated with Spark, Hive, Pig, Flume, and Map Reduce.

## Use Cases

Proven patterns where Phoenix delivers value.

### Operational Analytics

Real-time SQL queries on operational data with ACID guarantees for business insights.

### Low Latency OLTP

Transactional workloads with millisecond response times and full ACID support.

### Multi-tenant Applications

Build SaaS applications with tenant isolation using views and dynamic columns.

### Secondary Indexing

Fast lookups on non-primary key columns with automatic index maintenance.

### Time-Series Data

SQL queries over time-series data with efficient storage and retrieval patterns.

### Data Integration

ETL pipelines with Spark, Hive, and Map Reduce for comprehensive data workflows.

What's New in 5.3.1

## Latest Phoenix Highlights

Recent capabilities now available in the 5.3.1 release.

### DynamoDB-Compatible REST API

Point your DynamoDB SDK clients at Phoenix using the phoenix-adapters REST service — no application rewrite required.

Learn more

### Document Data: BSON

Native binary JSON column type with server-side projection, filtering, and atomic per-field updates.

Learn more

### Change Data Capture

Stream row-level changes as ordered, partitioned events — read with standard SQL, with full split/merge lineage.

Learn more

### Eventually Consistent Indexes

Move global secondary index maintenance off the write path for write-heavy workloads — higher throughput, bounded staleness, no query-side changes.

Learn more

See all features in 5.3.1

## SQL Support

Phoenix takes your SQL query, compiles it into HBase scans, and orchestrates execution to produce JDBC result sets.

### Complete SQL Support

SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY, and more. Full DML and DDL support.

### Optimized Execution

Queries compiled into HBase scans with coprocessors and custom filters for millisecond performance.

### JDBC Connection

Connect using standard JDBC URL: jdbc:phoenix:server1,server2:port

## A Vibrant Community

Apache Phoenix is a top-level Apache project with an active community of users and contributors. Join discussions, explore the language reference, and help shape the future of SQL on HBase.

Mailing Lists

Contribute

Team

- News & EventsLatest releases and community tech talks.
- Who is Using PhoenixOrganizations running Phoenix in production.
- Language ReferenceComplete SQL grammar, functions, and datatypes.

## Getting Started

From download to production in a few simple steps.

### 1. Download

Grab the latest stable release and verify checksums.

Learn more →

### 2. Read the Guide

Walk through cluster setup, schema design, and operations.

Learn more →

### 3. Connect a Client

Configure the JDBC client classpath and connection URL.

Learn more →
