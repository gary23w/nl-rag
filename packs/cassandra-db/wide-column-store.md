---
title: "Wide-column store"
source: https://en.wikipedia.org/wiki/Wide-column_store
domain: cassandra-db
license: CC-BY-SA-4.0
tags: cassandra, wide-column store, apache cassandra, gossip protocol
fetched: 2026-07-02
---

# Wide-column store

A **wide-column store** (or **extensible record store**) is a type of NoSQL database. It uses tables, rows, and columns, but unlike a relational database, the names and format of the columns can vary from row to row in the same table. A wide-column store can be interpreted as a two-dimensional key–value store. Google's Bigtable is one of the prototypical examples of a wide-column store.

## Wide-column stores versus columnar databases

Wide-column stores such as Bigtable and Apache Cassandra are not column stores in the original sense of the term, since their two-level structures do not use a columnar data layout. In genuine column stores, a columnar data layout is adopted such that each column is stored separately on disk. Wide-column stores do often support the notion of column families that are stored separately. However, each such column family typically contains multiple columns that are used together, similar to traditional relational database tables. Within a given column family, all data is stored in a row-by-row fashion, such that the columns for a given row are stored together, rather than each column being stored separately.

Wide-column stores that support column families are also known as *column family databases*.

## Notable examples

Notable wide-column stores include:

- Apache Accumulo
- Apache Cassandra
- Apache HBase
- Bigtable
- DataStax Enterprise (uses Apache Cassandra)
- DataStax Astra DB (uses Apache Cassandra)
- Hypertable
- Azure Tables
- ScyllaDB
