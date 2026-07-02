---
title: "Amazon DocumentDB"
source: https://en.wikipedia.org/wiki/Amazon_DocumentDB
domain: aws-documentdb
license: CC-BY-SA-4.0
tags: aws documentdb, amazon documentdb, managed document database, mongodb-compatible database
fetched: 2026-07-02
---

# Amazon DocumentDB

**Amazon DocumentDB** is a managed proprietary NoSQL database service that supports document data structures, with some compatibility with MongoDB version 3.6 (released by MongoDB in 2017) and version 4.0 (released by MongoDB in 2018). As a document database, Amazon DocumentDB can store, query, and index JSON data. It is available on Amazon Web Services. As of March 2023, AWS introduced some compliance with MongoDB 5.0 but lacks time series collection support.

## Main features

A document database natively stores JSON data. DocumentDB provides single document lookups, index scans, regular expression queries, and aggregations. It can create single-field, compound, and multi-key indexes to improve the performance of query patterns. Reads from the indexes on the primary instance are read-after-write consistent and users can delete or create new indexes at any time.

DocumentDB was an enhancement to the Amazon Aurora relational database system, specifically the PostgreSQL-compatible edition. Its architecture separates storage and computing so that each layer can scale independently, though the system is limited to a single writable primary. Amazon DocumentDB, through Aurora PostgreSQL, uses the Aurora Storage Engine, originally built for the MySQL relational database. This storage engine is distributed, fault-tolerant, self-healing, and durable, which it maintains by replicating data six ways across three AWS Availability Zones (AZs). Amazon DocumentDB databases cannot span AWS Regions or span cloud providers, nor can Amazon DocumentDB run on-premises. The system can support up to 15 low-latency readable replicas and continuously backs up all changes to Amazon S3.
