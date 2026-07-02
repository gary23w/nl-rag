---
title: "Presto (SQL query engine)"
source: https://en.wikipedia.org/wiki/Presto_(SQL_query_engine)
domain: trino-presto
license: CC-BY-SA-4.0
tags: trino query engine, presto sql, distributed query engine, query optimization
fetched: 2026-07-02
---

# Presto (SQL query engine)

**Presto** (including PrestoDB, and PrestoSQL which was re-branded to **Trino**) is a distributed query engine for big data using the SQL query language. Its architecture allows users to query data sources such as Hadoop, Cassandra, Kafka, AWS S3, Alluxio, MySQL, MongoDB and Teradata, and allows use of multiple data sources within a query. Presto is community-driven open-source software released under the Apache License.

## History

Presto was originally designed and developed at Facebook, Inc. (later renamed Meta) for their data analysts to run interactive queries on its large data warehouse in Apache Hadoop. The first four developers were Martin Traverso, Dain Sundstrom, David Phillips, and Eric Hwang. Before Presto, the data analysts at Facebook relied on Apache Hive for running SQL analytics on their multi-petabyte data warehouse. Hive was deemed too slow for Facebook's scale and Presto was invented to fill the gap to run fast queries. Original development started in 2012 and deployed at Facebook later that year. In November 2013, Facebook announced its open source release.

In 2014, Netflix disclosed they used Presto on 10 petabytes of data stored in the Amazon Simple Storage Service (S3). In November, 2016, Amazon announced a service called Athena that was based on Presto. In 2017, Teradata spun out a company called Starburst Data to commercially support Presto, which included staff acquired from Hadapt in 2014. Teradata's QueryGrid software allowed Presto to access a Teradata relational database.

In January 2019, the Presto Software Foundation was announced. The foundation is a not-for-profit organization for the advancement of the Presto open source distributed SQL query engine. At the same time, Presto development forked: PrestoDB maintained by Facebook, and PrestoSQL maintained by the Presto Software Foundation, with some cross pollination of code.

In September 2019, Facebook donated PrestoDB to the Linux Foundation, establishing the Presto Foundation. Neither the creators of Presto, nor the top contributors and committers, were invited to join this foundation.

By 2020, all four of the original Presto developers had joined Starburst. In December 2020, PrestoSQL was rebranded as Trino, since Facebook had obtained a trademark on the name "Presto" (also donated to the Linux Foundation).

Another company called Ahana was announced in 2020 to commercialize the PrestoDB fork as a cloud service and was acquired by IBM in 2023.

## Architecture

Presto's architecture is very similar to other database management systems using cluster computing, sometimes called massively parallel processing (MPP). One coordinator works in sync with multiple workers. Clients submit SQL statements that are parsed and planned, following which parallel tasks are scheduled to workers. Workers jointly process rows from the data sources and produce results that are returned to the client. Compared to the original Apache Hive execution model which used the Hadoop MapReduce mechanism on each query, Presto does not write intermediate results to disk, resulting in a significant speed improvement. Presto is written in Java.

A Presto query can combine data from multiple sources. Presto offers connectors to data sources including files in Alluxio, Hadoop Distributed File System (often called a data lake), Amazon S3, MySQL, PostgreSQL, Microsoft SQL Server, Amazon Redshift, Apache Kudu, Apache Phoenix, Apache Kafka, Apache Cassandra, Apache Accumulo, MongoDB and Redis. Unlike other Hadoop distribution-specific tools, such as Apache Impala, Presto can work with any variant of Hadoop or without it. Presto supports separation of compute and storage and may be deployed on-premises or using cloud computing.
