---
title: "Apache HBase"
source: https://en.wikipedia.org/wiki/Apache_HBase
domain: apache-phoenix
license: CC-BY-SA-4.0
tags: apache phoenix, sql over hbase, apache hbase, relational layer
fetched: 2026-07-02
---

# Apache HBase

**HBase** is an open-source non-relational distributed database modeled after Google's Bigtable and written in Java. It is developed as part of Apache Software Foundation's Apache Hadoop project and runs on top of HDFS (Hadoop Distributed File System) or Alluxio, providing Bigtable-like capabilities for Hadoop. That is, it provides a fault-tolerant way of storing large quantities of sparse data (small amounts of information caught within a large collection of empty or unimportant data, such as finding the 50 largest items in a group of 2 billion records, or finding the non-zero items representing less than 0.1% of a huge collection).

HBase features compression, in-memory operation, and Bloom filters on a per-column basis as outlined in the original Bigtable paper. Tables in HBase can serve as the input and output for MapReduce jobs run in Hadoop, and may be accessed through the Java API but also through REST, Avro or Thrift gateway APIs. HBase is a wide-column store and has been widely adopted because of its lineage with Hadoop and HDFS. HBase runs on top of HDFS and is well-suited for fast read and write operations on large datasets with high throughput and low input/output latency.

HBase is not a direct replacement for a classic SQL database, however Apache Phoenix project provides a SQL layer for HBase as well as JDBC driver that can be integrated with various analytics and business intelligence applications. The Apache Trafodion project provides a SQL query engine with ODBC and JDBC drivers and distributed ACID transaction protection across multiple statements, tables and rows that use HBase as a storage engine.

HBase is now serving several data-driven websites but Facebook's Messaging Platform migrated from HBase to MyRocks in 2018. Unlike relational and traditional databases, HBase does not support SQL scripting; instead the equivalent is written in Java, employing similarity with a MapReduce application.

In the parlance of Eric Brewer's CAP Theorem, HBase is a CP type system.

## History

Apache HBase began as a project by the company Powerset out of a need to process massive amounts of data for the purposes of natural-language search. Since 2010 it is a top-level Apache project.

Facebook elected to implement its new messaging platform using HBase in November 2010, but migrated away from HBase in 2018.

The 2.5.x series is the current stable release line, it supersedes earlier release lines.

## Use cases & production deployments

### Enterprises that use HBase

The following is a list of notable enterprises that have used or are using HBase:

- 23andMe
- Adobe
- Airbnb uses HBase as part of its AirStream realtime stream computation framework
- Alibaba Group
- Amadeus IT Group, as its main long-term storage DB.
- Bloomberg, for time series data storage
- Facebook used HBase for its messaging platform between 2010 and 2018
- Flipkart uses HBase for its search index and user insights.
- Flurry
- HubSpot
- Imgur uses HBase to power its notifications system
- Kakao, operator of KakaoTalk
- LY, operator of Line
- Netflix
- Pinterest
- Quicken Loans
- Rocket Fuel
- Salesforce.com
- Sears
- Sophos, for some of their back-end systems.
- Spotify uses HBase as base for Hadoop and machine learning jobs.
- Twitter
- Tuenti uses HBase for its messaging platform.
- Xiaomi
- Yahoo!
