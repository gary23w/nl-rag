---
title: "Apache Impala"
source: https://en.wikipedia.org/wiki/Apache_Impala
domain: apache-kudu
license: CC-BY-SA-4.0
tags: apache kudu, columnar storage engine, apache hadoop, analytical storage
fetched: 2026-07-02
---

# Apache Impala

**Apache Impala** is an open source massively parallel processing (MPP) SQL query engine for data stored in a computer cluster running Apache Hadoop. Impala has been described as the open-source equivalent of Google F1, which inspired its development in 2012.

## Description

Apache Impala is a query engine that runs on Apache Hadoop. The project was announced in October 2012 with a public beta test distribution and became generally available in May 2013.

Impala brings scalable parallel database technology to Hadoop, enabling users to issue low-latency SQL queries to data stored in HDFS and Apache HBase without requiring data movement or transformation. Impala is integrated with Hadoop to use the same file and data formats, metadata, security and resource management frameworks used by MapReduce, Apache Hive, Apache Pig and other Hadoop software.

Impala is promoted for analysts and data scientists to perform analytics on data stored in Hadoop via SQL or business intelligence tools. The result is that large-scale data processing (via MapReduce) and interactive queries can be done on the same system using the same data and metadata – removing the need to migrate data sets into specialized systems and/or proprietary formats simply to perform analysis.

Features include:

- Supports HDFS, S3, Microsoft Azure Blob Storage, Apache HBase and Apache Kudu storage,
- Reads Hadoop file formats, including text, LZO, SequenceFile, Avro, RCFile, Parquet and ORC
- Supports Hadoop security (Kerberos authentication, Ldap),
- Fine-grained, role-based authorization with Apache Ranger
- Uses metadata, ODBC driver, and SQL syntax from Apache Hive.

In early 2013, a column-oriented file format called Parquet was announced for architectures including Impala. In December 2013, Amazon Web Services announced support for Impala. In early 2014, MapR added support for Impala. In 2015, another format called Kudu was announced, which Cloudera proposed to donate to the Apache Software Foundation along with Impala. Impala graduated to an Apache Top-Level Project (TLP) on 28 November 2017.
