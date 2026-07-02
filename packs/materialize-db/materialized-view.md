---
title: "Materialized view"
source: https://en.wikipedia.org/wiki/Materialized_view
domain: materialize-db
license: CC-BY-SA-4.0
tags: materialize database, streaming sql database, incremental view maintenance, timely dataflow
fetched: 2026-07-02
---

# Materialized view

In computing, a **materialized view** is a database object that contains the results of a query. For example, it may be a local copy of data located remotely, or may be a subset of the rows and/or columns of a table or join result, or may be a summary using an aggregate function.

The process of setting up a materialized view is sometimes called **materialization**. This is a form of caching the results of a query, similar to memoization of the value of a function in functional languages, and it is sometimes described as a form of precomputation. As with other forms of precomputation, database users typically use materialized views for performance reasons, i.e. as a form of optimization.

Materialized views that store data based on remote tables were also known as snapshots (deprecated Oracle terminology).

In any database management system following the relational model, a view is a virtual table representing the result of a database query. Whenever a query or an update addresses an ordinary view's virtual table, the DBMS converts these into queries or updates against the underlying base tables. A materialized view takes a different approach: the query result is cached as a concrete ("materialized") table (rather than a view as such) that may be updated from the original base tables from time to time. This enables much more efficient access, at the cost of extra storage and of some data being potentially out-of-date. Materialized views find use especially in data warehousing scenarios, where frequent queries of the actual base tables can be expensive.

In a materialized view, indexes can be built on any column. In contrast, in a normal view, it's typically only possible to exploit indexes on columns that come directly from (or have a mapping to) indexed columns in the base tables; often this functionality is not offered at all.

## Implementations

### Oracle

Materialized views were implemented first by the Oracle Database: the Query rewrite feature was added from version 8i.

Example syntax to create a materialized view in Oracle:

```mw
 CREATE MATERIALIZED VIEW MV_MY_VIEW
REFRESH FAST START WITH SYSDATE
   NEXT SYSDATE + 1
     AS SELECT * FROM <table_name>;
```

### PostgreSQL

In PostgreSQL, version 9.3 and newer natively support materialized views. In version 9.3, a materialized view is not auto-refreshed, and is populated only at time of creation (unless `WITH NO DATA` is used). It may be refreshed later manually using `REFRESH MATERIALIZED VIEW`. In version 9.4, the refresh may be concurrent with selects on the materialized view if `CONCURRENTLY` is used.

Example syntax to create a materialized view in PostgreSQL:

```mw
 CREATE MATERIALIZED VIEW MV_MY_VIEW
 [ WITH (storage_parameter [= value] [, ... ]) ]
    [ TABLESPACE tablespace_name ]
     AS SELECT * FROM <table_name>;
```

### SQL Server

Microsoft SQL Server differs from other RDBMS by the way of implementing materialized view via a concept known as "Indexed Views". The main difference is that such views do not require a refresh because they are in fact always synchronized to the original data of the tables that compound the view. To achieve this, it is necessary that the lines of origin and destination are "deterministic" in their mapping, which limits the types of possible queries to do this. This mechanism has been realised since the 2000 version of SQL Server.

Example syntax to create a materialized view in SQL Server:

```mw
CREATE VIEW MV_MY_VIEW
WITH SCHEMABINDING
AS 
SELECT COL1, SUM(COL2) AS TOTAL
FROM <table_name>
GROUP BY COL1;
GO
CREATE UNIQUE CLUSTERED INDEX XV 
   ON MV_MY_VIEW (COL1);
```

### Stream processing frameworks

Apache Kafka (since v0.10.2), Apache Spark (since v2.0), Apache Flink, Kinetica DB, Materialize, RisingWave, and Epsio all support materialized views on streams of data.

### Others

Materialized views are also supported in Sybase SQL Anywhere. In IBM Db2, they are called "materialized query tables". ClickHouse supports materialized views that automatically refresh on merges. MySQL doesn't support materialized views natively, but workarounds can be implemented by using triggers or stored procedures or by using the open-source application Flexviews. Materialized views can be implemented in Amazon DynamoDB using data modification events captured by DynamoDB Streams. Google announced in 8 April 2020 the availability of materialized views for BigQuery as a beta release.
