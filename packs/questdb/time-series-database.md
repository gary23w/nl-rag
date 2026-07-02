---
title: "Time series database"
source: https://en.wikipedia.org/wiki/Time_series_database
domain: questdb
license: CC-BY-SA-4.0
tags: questdb database, time series database, sql time series, column-oriented dbms
fetched: 2026-07-02
---

# Time series database

A **time series database** is a software system that is optimized for storing and serving time series through associated pairs of time(s) and value(s). In some fields, *time series* may be called profiles, curves, traces or trends. Several early time series databases are associated with industrial applications which could efficiently store measured values from sensory equipment (also referred to as data historians), but now are used in support of a much wider range of applications. In many cases, the repositories of time-series data will utilize compression algorithms to manage the data efficiently. Although it is possible to store time-series data in many different database types, the design of these systems with time as a key index is distinctly different from relational databases which reduce discrete relationships through referential models.

## Overview

Time series datasets are relatively large and uniform compared to other datasets―usually being composed of a timestamp and associated data. Time series datasets can also have fewer relationships between data entries in different tables and don't require indefinite storage of entries. The unique properties of time series datasets mean that time series databases can provide significant improvements in storage space and performance over general purpose databases. For instance, due to the uniformity of time series data, specialized compression algorithms can provide improvements over regular compression algorithms designed to work on less uniform data. Time series databases can also be configured to regularly delete (or downsample) old data, unlike regular databases which are designed to store data indefinitely. Special database indices can also provide boosts in query performance.

## Common characteristics

Time series databases are commonly designed for append-heavy workloads, where large numbers of measurements or events are continuously written together with timestamps. Specialized time series management systems have been developed for data from monitoring, automation, the Internet of Things, and cyber-physical systems, where data may be produced at high velocity and in large volumes.

Common design goals include high-throughput data ingestion, low-latency queries over time ranges, efficient compression, and support for aggregation or downsampling over time windows. Many systems also organize data by tags, devices, sensors, or other metadata, so that users can retrieve measurements by both time range and source.

## Applications and workloads

Time series databases are used in application areas where data is collected continuously over time. Examples include industrial monitoring, operational historians, infrastructure and application monitoring, Internet of Things sensor data, energy systems, financial market data, and scientific measurements.

In monitoring applications, time series database systems may need to process large amounts of sensor or metric data in real time, execute continuous queries, and support analytical tasks such as data exploration, anomaly detection, predictive modeling, trend analysis, and missing-value recovery.

## Analysis and machine learning

Time series databases are often used as storage and query systems for downstream analytical tasks, including forecasting, anomaly detection, imputation, and pattern matching. Some systems also integrate analytical or machine-learning functions closer to the database layer, allowing users to invoke forecasting or anomaly detection through database query interfaces such as SQL.

Recent research in time series analysis has also explored large pre-trained models for tasks such as forecasting, imputation, and anomaly detection. These models are usually discussed as analytical methods for time series data rather than as defining features of time series databases.

## List of time series databases

The following database systems have functionality optimized for handling time series data.

| Name | License | Language | References |
|---|---|---|---|
| Apache IoTDB | Apache License 2.0 | Java |   |
| Apache Kudu | Apache License 2.0 | C++ |   |
| Apache Pinot | Apache License 2.0 | Java |   |
| ClickHouse | Apache License 2.0 | C++ |   |
| CrateDB | Apache License 2.0 | Java |   |
| eXtremeDB | Commercial | SQL, Python, C / C++, Java, and C# |   |
| FAME (database) | Commercial | C |   |
| InfluxDB | MIT. Chronograf AGPLv3, Clustering Commercial | Go (version 2), Rust (version 3) |   |
| Informix TimeSeries | Commercial | C / C++ |   |
| Kx kdb+ | Commercial | Q |   |
| MongoDB | Server Side Public License (SSPL) v1.0 | C++ |   |
| Prometheus | Apache License 2.0 | Go |   |
| Riak-TS | Apache License 2.0 | Erlang |   |
| RRDtool | GPLv2 | C |   |
| TimescaleDB | Apache License 2.0 | C |   |
| Whisper (Graphite) | Apache License 2.0 | Python |   |
