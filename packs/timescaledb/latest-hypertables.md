---
title: "Understand hypertables"
source: https://docs.timescale.com/use-timescale/latest/hypertables/
domain: timescaledb
license: CC-BY-SA-4.0
tags: timescaledb, hypertable, time series database, postgres extension
fetched: 2026-07-02
---

# Understand hypertables

Hypertables are PostgreSQL tables with special features that power real-time analytics on time-series and event data

Tiger Cloud supercharges your real-time analytics by letting you run complex queries continuously, with near-zero latency. Under the hood, this is achieved by using hypertables, PostgreSQL tables that automatically partition your time-series data by time and optionally by other dimensions. When you run a query, Tiger Cloud identifies the correct partition, called chunk, and runs the query on it, instead of going through the entire table.

Hypertables offer the following benefits:

- **Efficient data management with automated partitioning by time**: Tiger Cloud splits your data into chunks that hold data from a specific time range. For example, one day or one week. You can configure this range to better suit your needs.
- **Better performance with strategic indexing**: an index on time in the descending order is automatically created when you create a hypertable. More indexes are created on the chunk level, to optimize performance. You can create additional indexes, including unique indexes, on the columns you need.
- **Faster queries with chunk skipping**: Tiger Cloud skips the chunks that are irrelevant in the context of your query, dramatically reducing the time and resources needed to fetch results. Even more, you can enable chunk skipping on non-partitioning columns.
- **Advanced data analysis with hyperfunctions**: Tiger Cloud enables you to efficiently process, aggregate, and analyze significant volumes of data while maintaining high performance.

To top it all, there is no added complexity, you interact with hypertables in the same way as you would with regular PostgreSQL tables. All the optimization magic happens behind the scenes.

## Get hands on

Section titled “Get hands on”

## Learn more

Section titled “Learn more”

- Partition a hypertable: Time, integer, and space partitioning.
- Hypertable indexes: Default indexes, supported types, and unique constraints.
- Hypertable operations: Alter, drop, delete data, and vacuum.
- CREATE TABLE reference: Full API reference.
- Informational views: Query hypertable metadata from SQL.
