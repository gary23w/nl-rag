---
title: "Understand continuous aggregates"
source: https://docs.timescale.com/use-timescale/latest/continuous-aggregates/about-continuous-aggregates/
domain: timescaledb
license: CC-BY-SA-4.0
tags: timescaledb, hypertable, time series database, postgres extension
fetched: 2026-07-02
---

# Understand continuous aggregates

Learn how TimescaleDB continuous aggregates combine your data into analytic summaries and are refreshed in the background when new data is added

In modern applications, data usually grows very quickly. This means that aggregating it into useful summaries can become very slow. If you are collecting data very frequently, you might want to aggregate your data into minutes or hours instead. For example, if an IoT device takes temperature readings every second, you might want to find the average temperature for each hour. Every time you run this query, the database needs to scan the entire table and recalculate the average. TimescaleDB makes aggregating data lightning fast, accurate, and easy with continuous aggregates.

Continuous aggregates in TimescaleDB are a kind of hypertable that is refreshed automatically in the background as new data is added, or old data is modified. Changes to your dataset are tracked, and the hypertable behind the continuous aggregate is automatically updated in the background.

Continuous aggregates have a much lower maintenance burden than regular PostgreSQL materialized views, because the whole view is not created from scratch on each refresh. This means that you can get on with working your data instead of maintaining your database.

Because continuous aggregates are based on hypertables, you can query them in exactly the same way as your other tables. This includes continuous aggregates in the rowstore, compressed into the columnstore, or tiered to object storage. You can even create continuous aggregates on top of your continuous aggregates, for an even more fine-tuned aggregation.

Real-time aggregation enables you to combine pre-aggregated data from the materialized view with the most recent raw data. This gives you up-to-date results on every query.

In TimescaleDB v2.13 and later, real-time aggregates are **DISABLED** by default. In earlier versions, real-time aggregates are **ENABLED** by default; when you create a continuous aggregate, queries to that view include the results from the most recent raw data.

## Types of aggregation

Section titled “Types of aggregation”

There are three main ways to make aggregation easier: materialized views, continuous aggregates, and real-time aggregates.

Materialized views are a standard PostgreSQL function. They are used to cache the result of a complex query so that you can reuse it later on. Materialized views do not update regularly, although you can manually refresh them as required.

Continuous aggregates are a TimescaleDB-only feature. They work in a similar way to a materialized view, but they are updated automatically in the background, as new data is added to your database. Continuous aggregates are updated continuously and incrementally, which means they are less resource intensive to maintain than materialized views. Continuous aggregates are based on hypertables, and you can query them in the same way as you do your other tables.

Real-time aggregates are a TimescaleDB-only feature. They are the same as continuous aggregates, but they add the most recent raw data to the previously aggregated data to provide accurate and up-to-date results, without needing to aggregate data as it is being written.

## Continuous aggregates on continuous aggregates

Section titled “Continuous aggregates on continuous aggregates”

You can create a continuous aggregate on top of another continuous aggregate. This allows you to summarize data at different granularity. For example, you might have a raw hypertable that contains second-by-second data. Create a continuous aggregate on the hypertable to calculate hourly data. To calculate daily data, create a continuous aggregate on top of your hourly continuous aggregate.

For more information, see the documentation about continuous aggregates on continuous aggregates.

## Continuous aggregates with a `JOIN` clause

Section titled “Continuous aggregates with a JOIN clause”

Continuous aggregates support the following JOIN features:

| Feature | TimescaleDB < 2.10.x | TimescaleDB <= 2.15.x | TimescaleDB >= 2.16.x |
|---|---|---|---|
| INNER JOIN | ❌ | ✅ | ✅ |
| LEFT JOIN | ❌ | ❌ | ✅ |
| LATERAL JOIN | ❌ | ❌ | ✅ |
| Joins between **ONE** hypertable and **ONE** standard PostgreSQL table | ❌ | ✅ | ✅ |
| Joins between **ONE** hypertable and **MANY** standard PostgreSQL tables | ❌ | ❌ | ✅ |
| Join conditions must be equality conditions, and there can only be **ONE** `JOIN` condition | ❌ | ✅ | ✅ |
| Any join conditions | ❌ | ❌ | ✅ |

JOINS in TimescaleDB must meet the following conditions:

- Only the changes to the hypertable are tracked, and they are updated in the continuous aggregate when it is refreshed. Changes to standard PostgreSQL table are not tracked.
- You can use an `INNER`, `LEFT`, and `LATERAL` joins; no other join type is supported.
- Joins on the materialized hypertable of a continuous aggregate are not supported.
- Hierarchical continuous aggregates can be created on top of a continuous aggregate with a `JOIN` clause, but cannot themselves have a `JOIN` clause.

### JOIN examples

Section titled “JOIN examples”

Given the following schema:

```
CREATE TABLE locations (
  id TEXT PRIMARY KEY,
  name TEXT
);

CREATE TABLE devices (
  id SERIAL PRIMARY KEY,
  location_id TEXT,
  name TEXT
);

CREATE TABLE conditions (
  "time" TIMESTAMPTZ,
  device_id INTEGER,
  temperature FLOAT8
) WITH (
  tsdb.hypertable
);
```

When you create a hypertable using CREATE TABLE ... WITH ..., the default partitioning column is automatically the first column with a timestamp data type. Also, TimescaleDB creates a columnstore policy that automatically converts your data to the columnstore, after an interval equal to the value of the chunk_interval, defined through `after` in the policy. This columnar format enables fast scanning and aggregation, optimizing performance for analytical workloads while also saving significant storage space. In the columnstore conversion, hypertable chunks are compressed by up to 98%, and organized for efficient, large-scale queries.

You can customize this policy later using alter_job. However, to change `after` or `created_before`, the compression settings, or the hypertable the policy is acting on, you must remove the columnstore policy and add a new one.

You can also manually convert chunks in a hypertable to the columnstore.

See the following `JOIN` examples on continuous aggregates:

- `INNER JOIN` on a single equality condition, using the `ON` clause: `CREATE MATERIALIZED VIEW conditions_by_day WITH (timescaledb.continuous) ASSELECT time_bucket('1 day', time) AS bucket, devices.name, MIN(temperature), MAX(temperature)FROM conditionsJOIN devices ON devices.id = conditions.device_idGROUP BY bucket, devices.nameWITH NO DATA;`
- `INNER JOIN` on a single equality condition, using the `ON` clause, with a further condition added in the `WHERE` clause: `CREATE MATERIALIZED VIEW conditions_by_day WITH (timescaledb.continuous) ASSELECT time_bucket('1 day', time) AS bucket, devices.name, MIN(temperature), MAX(temperature)FROM conditionsJOIN devices ON devices.id = conditions.device_idWHERE devices.location_id = 'location123'GROUP BY bucket, devices.nameWITH NO DATA;`
- `INNER JOIN` on a single equality condition specified in `WHERE` clause: `CREATE MATERIALIZED VIEW conditions_by_day WITH (timescaledb.continuous) ASSELECT time_bucket('1 day', time) AS bucket, devices.name, MIN(temperature), MAX(temperature)FROM conditions, devicesWHERE devices.id = conditions.device_idGROUP BY bucket, devices.nameWITH NO DATA;`
- `INNER JOIN` on multiple equality conditions: `CREATE MATERIALIZED VIEW conditions_by_day WITH (timescaledb.continuous) ASSELECT time_bucket('1 day', time) AS bucket, devices.name, MIN(temperature), MAX(temperature)FROM conditionsJOIN devices ON devices.id = conditions.device_id AND devices.location_id = 'location123'GROUP BY bucket, devices.nameWITH NO DATA;` TimescaleDB v2.16.x and higher.
- `INNER JOIN` with a single equality condition specified in `WHERE` clause can be combined with further conditions in the `WHERE` clause: `CREATE MATERIALIZED VIEW conditions_by_day WITH (timescaledb.continuous) ASSELECT time_bucket('1 day', time) AS bucket, devices.name, MIN(temperature), MAX(temperature)FROM conditions, devicesWHERE devices.id = conditions.device_idAND devices.location_id = 'location123'GROUP BY bucket, devices.nameWITH NO DATA;` TimescaleDB v2.16.x and higher.
- `INNER JOIN` between a hypertable and multiple PostgreSQL tables: `CREATE MATERIALIZED VIEW conditions_by_day WITH (timescaledb.continuous) ASSELECT time_bucket('1 day', time) AS bucket, devices.name AS device, locations.name AS location, MIN(temperature), MAX(temperature)FROM conditionsJOIN devices ON devices.id = conditions.device_idJOIN locations ON locations.id = devices.location_idGROUP BY bucket, devices.name, locations.nameWITH NO DATA;` TimescaleDB v2.16.x and higher.
- `LEFT JOIN` between a hypertable and a PostgreSQL table: `CREATE MATERIALIZED VIEW conditions_by_day WITH (timescaledb.continuous) ASSELECT time_bucket('1 day', time) AS bucket, devices.name, MIN(temperature), MAX(temperature)FROM conditionsLEFT JOIN devices ON devices.id = conditions.device_idGROUP BY bucket, devices.nameWITH NO DATA;` TimescaleDB v2.16.x and higher.
- `LATERAL JOIN` between a hypertable and a subquery: `CREATE MATERIALIZED VIEW conditions_by_day WITH (timescaledb.continuous) ASSELECT time_bucket('1 day', time) AS bucket, devices.name, MIN(temperature), MAX(temperature)FROM conditions,LATERAL (SELECT * FROM devices WHERE devices.id = conditions.device_id) AS devicesGROUP BY bucket, devices.nameWITH NO DATA;` TimescaleDB v2.16.x and higher.

## Function support

Section titled “Function support”

In TimescaleDB v2.7 and later, continuous aggregates support all PostgreSQL aggregate functions. This includes both parallelizable aggregates, such as `SUM` and `AVG`, and non-parallelizable aggregates, such as `RANK`.

In TimescaleDB v2.10.0 and later, the `FROM` clause supports `JOINS`, with some restrictions. For more information, see the `JOIN` support section.

In older versions of TimescaleDB, continuous aggregates only support aggregate functions that can be parallelized by PostgreSQL. You can work around this by aggregating the other parts of your query in the continuous aggregate, then using the window function to query the aggregate.

The following table summarizes the aggregate functions supported in continuous aggregates:

| Function, clause, or feature | TimescaleDB 2.6 and earlier | TimescaleDB 2.7, 2.8, and 2.9 | TimescaleDB 2.10 and later |
|---|---|---|---|
| Parallelizable aggregate functions | ✅ | ✅ | ✅ |
| Non-parallelizable SQL aggregates | ❌ | ✅ | ✅ |
| `ORDER BY` | ❌ | ✅ | ✅ |
| Ordered-set aggregates | ❌ | ✅ | ✅ |
| Hypothetical-set aggregates | ❌ | ✅ | ✅ |
| `DISTINCT` in aggregate functions | ❌ | ✅ | ✅ |
| `FILTER` in aggregate functions | ❌ | ✅ | ✅ |
| `FROM` clause supports `JOINS` | ❌ | ❌ | ✅ |

DISTINCT works in aggregate functions, not in the query definition. For example, for the table:

```
CREATE TABLE public.candle(
symbol_id uuid                     NOT NULL,
symbol    text                     NOT NULL,
"time"    timestamp with time zone NOT NULL,
open      double precision         NOT NULL,
high      double precision         NOT NULL,
low       double precision         NOT NULL,
close     double precision         NOT NULL,
volume    double precision         NOT NULL
);
```

- The following works: `CREATE MATERIALIZED VIEW candles_start_endWITH (timescaledb.continuous) ASSELECT time_bucket('1 hour', "time"), COUNT(DISTINCT symbol), first(time, time) as first_candle, last(time, time) as last_candleFROM candleGROUP BY 1;`
- This does not: `CREATE MATERIALIZED VIEW candles_start_endWITH (timescaledb.continuous) ASSELECT DISTINCT ON (symbol)symbol,symbol_id, first(time, time) as first_candle, last(time, time) as last_candleFROM candleGROUP BY symbol_id;`

If you want the old behavior in later versions of TimescaleDB, set the `timescaledb.finalized` parameter to `false` when you create your continuous aggregate.

## Components of a continuous aggregate

Section titled “Components of a continuous aggregate”

Continuous aggregates consist of:

- Materialization hypertable to store the aggregated data in
- Materialization engine to aggregate data from the raw, underlying, table to the materialization hypertable
- Invalidation engine to determine when data needs to be re-materialized, due to changes in the data
- Query engine to access the aggregated data

### Materialization hypertable

Section titled “Materialization hypertable”

Continuous aggregates take raw data from the original hypertable, aggregate it, and store the aggregated data in a materialization hypertable. When you query the continuous aggregate view, the aggregated data is returned to you as needed.

Using the same temperature example, the materialization table looks like this:

| day | location | chunk | avg temperature |
|---|---|---|---|
| 2021/01/01 | New York | 1 | 73 |
| 2021/01/01 | Stockholm | 1 | 70 |
| 2021/01/02 | New York | 2 |   |
| 2021/01/02 | Stockholm | 2 | 69 |

The materialization table is stored as a TimescaleDB hypertable, to take advantage of the scaling and query optimizations that hypertables offer. Materialization tables contain a column for each group-by clause in the query, and an `aggregate` column for each aggregate in the query.

For more information, see materialized hypertables.

### Materialization engine

Section titled “Materialization engine”

The materialization engine performs two transactions. The first transaction blocks all INSERTs, UPDATEs, and DELETEs, determines the time range to materialize, and updates the invalidation threshold. The second transaction unblocks other transactions, and materializes the aggregates. The first transaction is very quick, and most of the work happens during the second transaction, to ensure that the work does not interfere with other operations.

### Invalidation engine

Section titled “Invalidation engine”

Any change to the data in a hypertable could potentially invalidate some materialized rows. The invalidation engine checks to ensure that the system does not become swamped with invalidations.

Fortunately, time-series data means that nearly all INSERTs and UPDATEs have a recent timestamp, so the invalidation engine does not materialize all the data, but to a set point in time called the materialization threshold. This threshold is set so that the vast majority of INSERTs contain more recent timestamps. These data points have never been materialized by the continuous aggregate, so there is no additional work needed to notify the continuous aggregate that they have been added. When the materializer next runs, it is responsible for determining how much new data can be materialized without invalidating the continuous aggregate. It then materializes the more recent data and moves the materialization threshold forward in time. This ensures that the threshold lags behind the point-in-time where data changes are common, and that most INSERTs do not require any extra writes.

When data older than the invalidation threshold is changed, each transaction logs the minimum and maximum timestamps of the rows it modified. The continuous aggregate then identifies which complete time buckets are affected based on this per-transaction tracking. The range of buckets that are recalculated depends on transaction boundaries:

- If you modify rows in the 10:00 bucket and rows in the 15:00 bucket within a **single transaction**, all buckets from 10:00 to 15:00 (including intermediate buckets 11:00, 12:00, 13:00, and 14:00) are recalculated during refresh.
- If you modify rows in the 10:00 bucket in one transaction and rows in the 15:00 bucket in a **separate transaction**, only the 10:00 and 15:00 buckets are recalculated. The intermediate buckets (11:00, 12:00, 13:00, 14:00) are not affected.

This logging does cause some write load. However, the threshold lags behind the area of data that is currently changing, so the writes are small and rare.

## Get hands on

Section titled “Get hands on”

## Learn more

Section titled “Learn more”

- `CREATE MATERIALIZED VIEW` reference: Full API reference.
- Continuous aggregates API overview: All continuous aggregate functions and policies.
