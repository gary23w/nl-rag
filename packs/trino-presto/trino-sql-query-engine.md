---
title: "Trino (SQL query engine)"
source: https://en.wikipedia.org/wiki/Trino_(SQL_query_engine)
domain: trino-presto
license: CC-BY-SA-4.0
tags: trino query engine, presto sql, distributed query engine, query optimization
fetched: 2026-07-02
---

# Trino (SQL query engine)

**Trino** is an open-source distributed SQL query engine designed to query large data sets distributed over one or more heterogeneous data sources. Trino can query data lakes that contain a variety of file formats such as simple row-oriented CSV and JSON data files to more performant open column-oriented data file formats like ORC or Parquet residing on different storage systems like HDFS, AWS S3, Google Cloud Storage, or Azure Blob Storage using the Hive and Iceberg table formats. Trino also has the ability to run federated queries that query tables in different data sources such as MySQL, PostgreSQL, Cassandra, Kafka, MongoDB and Elasticsearch. Trino is released under the Apache License.

## History

In January 2019, the original creators of Presto, Martin Traverso, Dain Sundstrom, and David Phillips, created a fork of the Presto project. They initially kept the name Presto and used the PrestoSQL web handle to distinguish it from the original PrestoDB project. Simultaneously, they announced the Presto Software Foundation. The foundation is a not-for-profit organization dedicated to the advancement of the Presto open source distributed SQL query engine.

In December 2020, PrestoSQL was rebranded as Trino. The Trino Software Foundation, code base, and all other PrestoSQL assets were renamed as part of the rebrand.

Presto and Trino were originally designed and developed by Martin, Dain, David, and Eric Hwang at Facebook to allow data analysts to run interactive queries on its large data warehouse in Apache Hadoop. Trino shares the first six years of development with the Presto project. To learn more about the earlier history of Trino, you can reference the Presto history section.

Trino is used in many data platforms and products from cloud providers and other vendors. Customization of these products varies from pure Trino usage to heavily customized systems to run a data platform or integration in specialized data platforms for usage with specific data. Examples include Amazon Athena, Starburst Galaxy, Dune, and many others.

## Architecture

Trino is written in Java. It runs on a cluster of servers that contains two types of nodes, a **coordinator** and a **worker**.

- The coordinator is responsible for parsing, analyzing, optimizing, planning, and scheduling a query submitted by a client. The coordinator interacts with the service provider interface (SPI) to obtain the available tables, table statistics, and other information needed to carry out its tasks.
- The workers are responsible for executing the tasks and operators fed to them by the scheduler. These tasks process rows from the data sources which produce results that are returned to the coordinator and ultimately back to the client.

Trino adheres to the ANSI SQL standard and includes various parts of the following ANSI specifications: SQL-92, SQL:1999, SQL:2003, SQL:2008, SQL:2011, SQL:2016, SQL:2023.

Trino supports the separation of compute and storage and may be deployed both on-premises and in the cloud.

Trino has a Distributed computing MPP architecture. Trino first distributes work over multiple workers by running ad-hoc partitioning operations or relying on existing partitions in the data of the underlying data store. Once this data has reached the worker, the data is processed over pipelined operators carried out on multiple threads.
