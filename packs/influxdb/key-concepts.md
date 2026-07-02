---
title: "InfluxDB key concepts"
source: https://docs.influxdata.com/influxdb/v2/reference/key-concepts/
domain: influxdb
license: CC-BY-SA-4.0
tags: influxdb, time series database, influxdata, database engine
fetched: 2026-07-02
---

# InfluxDB key concepts

This page documents an earlier version of InfluxDB OSS. InfluxDB 3 Core is the latest stable version.

#### API token hashing is enabled by default in InfluxDB OSS 2.9.0

Stronger token security: tokens are stored as hashes on disk, so a copy of the database file doesn’t expose usable tokens. Existing tokens are hashed on first startup and the original strings can’t be recovered afterward — **capture any plaintext tokens you still need before you upgrade**.

For more information, see Token hashing.

Before working with InfluxDB 2.9, it’s helpful to learn a few key concepts. Browse the topics and videos below to learn more.

### InfluxDB data elements

InfluxDB structures data using elements such as timestamps, field keys, field values, tags, etc.

### InfluxDB data schema

InfluxDB uses a tabular data schema for displaying raw data in Data Explorer and for returning query results in annotated CSV syntax.

### InfluxDB design principles

Principles and tradeoffs related to InfluxDB design.

key concepts

Thank you for your feedback!
