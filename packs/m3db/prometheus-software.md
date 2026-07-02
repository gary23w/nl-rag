---
title: "Prometheus (software)"
source: https://en.wikipedia.org/wiki/Prometheus_(software)
domain: m3db
license: CC-BY-SA-4.0
tags: m3db, distributed time series database, m3 metrics platform, prometheus monitoring
fetched: 2026-07-02
---

# Prometheus (software)

**Prometheus** is a free software application for event monitoring and alerting. It records metrics in a time series database built using an HTTP pull model, supporting high dimensionality through key-value label pairs, flexible queries, and real-time alerting. The project is written in Go and licensed under the Apache 2.0 License, with source code available on GitHub.

Prometheus originated at SoundCloud in 2012 and was accepted by the Cloud Native Computing Foundation (CNCF) in 2016, graduating from incubation in 2018. It is commonly paired with Grafana for dashboard visualization and supports a wide range of exporters and integrations.

## History

Prometheus was developed at SoundCloud starting in 2012, after the company found that its existing metrics tools, based on StatsD and Graphite, could not meet the demands of its containerized infrastructure. The design goals included a multi-dimensional data model, operational simplicity, scalable data collection, and a powerful query language in a single tool. The project was open source from the start and was adopted by Boxever and Docker users before any official announcement.

The design was influenced by Borgmon, Google's internal time-series monitoring system, which treated time-series data as a source for alert generation.

By 2013, Prometheus was in production use at SoundCloud. The project was publicly announced in January 2015.

In May 2016, the Cloud Native Computing Foundation accepted Prometheus as its second incubated project, after Kubernetes. In August 2018, the CNCF announced that Prometheus had graduated from incubation.

### Versions

Prometheus 1.0 was released in July 2016. Subsequent releases through 2016 and 2017 led to Prometheus 2.0 in November 2017, which introduced a new storage engine with significantly improved performance and reduced disk usage.

## Architecture

A typical Prometheus monitoring deployment consists of several components working together. Exporters run on monitored hosts to collect and expose local metrics. The Prometheus server scrapes those exporters at a configured interval, aggregates the data, and stores it locally. Alertmanager receives alerts from Prometheus and handles routing, grouping, and silencing before forwarding notifications. Grafana is commonly used to build dashboards from Prometheus data. Queries against all of these are written in PromQL, Prometheus's native query language.

### Data model

Prometheus data is organized as named metrics, each optionally qualified by an arbitrary number of key-value label pairs. Labels can identify the data source (server name, datacenter) or carry application-specific context such as HTTP status code, request method, or endpoint. Querying in real time against any combination of labels is what makes the data model multi-dimensional.

Prometheus stores data locally on disk for fast writes and queries. Metrics can also be forwarded to remote storage backends, including Grafana Mimir and other Prometheus-compatible systems.

### Data collection

Prometheus collects data through a pull model: the server periodically queries a configured list of targets (exporters) and aggregates the returned time-series values. Prometheus includes several service discovery mechanisms to automatically locate targets in dynamic environments.

### PromQL

Prometheus provides its own query language, PromQL (Prometheus Query Language), which allows users to select and aggregate time-series data. The language includes time-oriented constructs such as the rate() function, instant vectors, and range vectors that return multiple samples per series over a specified time window.

Prometheus defines four metric types that PromQL operates on: Counter (a monotonically increasing value), Gauge (an arbitrary value that can go up or down), Histogram (samples observations and counts them in configurable buckets), and Summary (similar to Histogram but calculates quantiles on the client side).

#### Example

```mw
# A metric with label filtering
go_gc_duration_seconds{instance="localhost:9090", job="alertmanager"}

# Aggregation operators
sum by (app, proc) (
  instance_memory_limit_bytes - instance_memory_usage_bytes
) / 1024 / 1024
```

### Alerting

Alert rules in Prometheus specify a condition and a duration; if the condition holds for that duration, Prometheus fires an alert to Alertmanager. Alertmanager handles silencing, inhibition, and routing to notification destinations including email, Slack, and PagerDuty. Additional targets such as Microsoft Teams can be reached through the Alertmanager webhook receiver interface.

### Time series database

Prometheus includes its own time series database. Recent data (by default, one to three hours) is held in a combination of memory and mmap-backed files. Older data is written to persistent blocks indexed with an inverted index, which suits Prometheus's label-based query patterns. A background compaction process merges smaller blocks into larger ones to reduce read overhead. Durability against crashes is provided by a write-ahead log (WAL).

### Dashboards

Prometheus includes a basic expression browser but is not a full dashboard system. Grafana is the standard pairing, querying Prometheus via PromQL to produce dashboards; the need to deploy and maintain Grafana separately is sometimes cited as an operational drawback.

### Interoperability

Prometheus favors white-box monitoring, where applications publish internal metrics for collection. Exporters and agents are available for many applications and systems. For transition from existing monitoring stacks, Prometheus supports several protocols: Graphite, StatsD, SNMP, JMX, and CollectD.

Metrics are typically retained for a few weeks. For longer retention, Prometheus can stream data to remote storage backends.

### OpenMetrics

An effort to standardize the Prometheus exposition format as OpenMetrics has gained adoption from several vendors, including InfluxData's TICK suite, InfluxDB, Google Cloud Platform, Datadog, and New Relic. The OpenMetrics specification is maintained separately from the Prometheus project.

## Library support

Prometheus client libraries are available for most major programming languages. The POCO C++ Libraries expose Prometheus metrics through the `Poco::Prometheus` namespace.
