---
title: "Apache Kudu"
source: https://en.wikipedia.org/wiki/Apache_Kudu
domain: apache-kudu
license: CC-BY-SA-4.0
tags: apache kudu, columnar storage engine, apache hadoop, analytical storage
fetched: 2026-07-02
---

# Apache Kudu

**Apache Kudu** is a free and open source column-oriented data store of the Apache Hadoop ecosystem. It is compatible with most of the data processing frameworks in the Hadoop environment. It provides completeness to Hadoop's storage layer to enable fast analytics on fast data.

The open source project to build Apache Kudu began as internal project at Cloudera. The first version Apache Kudu 1.0 was released 19 September 2016.

## Comparison with other storage engines

Kudu was designed and optimized for OLAP workloads. Like HBase, it is a real-time store that supports key-indexed record lookup and mutation. Kudu differs from HBase since Kudu's datamodel is a more traditional relational model, while HBase is schemaless. Kudu's "on-disk representation is truly columnar and follows an entirely different storage design than HBase/Bigtable".
