---
title: "InfluxDB OSS v2 Documentation"
source: https://docs.influxdata.com/influxdb/v2/
domain: time-series-databases-obs
license: CC-BY-SA-4.0
tags: time series storage, metrics retention downsampling, data point compaction, monitoring backend
fetched: 2026-07-02
---

# InfluxDB OSS v2 Documentation

Doc

umentation

InfluxDB OSS v2

InfluxDB 3

- InfluxDB 3 Core New
- InfluxDB 3 Enterprise New
- InfluxDB Clustered

- InfluxDB Cloud Serverless
- InfluxDB Cloud Dedicated

- InfluxDB 3 Explorer New

InfluxDB 2

- InfluxDB OSS v2
- InfluxDB Cloud (TSM)
- Flux

InfluxDB 1

- InfluxDB OSS v1
- InfluxDB Enterprise
- InfluxDB Cloud 1

Telegraf

- Telegraf
- Telegraf Controller New
- Telegraf Enterprise New

Other products

- Chronograf
- Kapacitor

# Get started with InfluxDB v2

Get started

### Write Data

Write data to InfluxDB using a number of different options.

### Query Data

Use Flux to query and transform your data.

### Process Data

Use InfluxDB tasks to process and downsample data.

### Visualize Data

Build powerful dashboards to visualize your data.

### Monitor & Alert

Monitor metrics and send alerts with InfluxDB.

© 2026 InfluxData, Inc.

### What is your InfluxDB OSS URL?

Customize your **InfluxDB OSS URL** and we’ll update code examples for you.

##### Default

##### Custom

For more information, see InfluxDB OSS URLs.

### InfluxDB OSS 2.9.0: API tokens are hashed by default

Stronger token security in **InfluxDB OSS 2.9.0** — tokens are hashed on disk by default. Existing tokens are hashed on first startup and can’t be recovered afterward. **Capture any plaintext tokens you still need before you upgrade.**

View InfluxDB OSS 2.9.0 release notes

Hashed tokens authenticate exactly like unhashed tokens — clients and integrations keep working.

**Also new in 2.9.0:**

- Configurable backup compression
- Restore support for backups containing hashed tokens
- Tighter Edge Data Replication queue validation
- Flux upgrade
- Compaction reliability improvements

### Key enhancements in Explorer 1.9

Explorer 1.9 is now available with InfluxQL support, an AI-assisted Flux to SQL converter (beta), and new live sample data simulators.

View Explorer 1.9 release notes

Explorer 1.9 includes new features and improvements that make it easier to query, visualize, and manage data.

**Highlights:**

- **Flux to SQL converter (beta)**: Convert Flux queries to SQL with an AI-assisted converter.
- **InfluxQL support**: Query data with InfluxQL in the Data Explorer and dashboards, and save and load InfluxQL queries.
- **InfluxQL visualizations**: Render line and bar charts from InfluxQL results with per-tag series grouping.
- **Query error history**: Review a history of query errors in the query tool.
- **Live sample data simulators**: Generate continuous live sample data with new bird data and signal generator simulators.

For more details, see Explorer 1.9 release notes

### InfluxDB 3.10 is now available

InfluxDB 3 Core 3.10 adds an automatic catalog format upgrade, a configurable query-concurrency limit, and processing engine improvements.

**Key updates in InfluxDB 3 Core 3.10:**

- **Catalog format upgrade**: the on-disk catalog automatically upgrades from format v2 to v3 on first 3.10 startup. Migration is one-way—back up your catalog before upgrading.
- **`--max-concurrent-queries`**: limit concurrent queries (adjustable at runtime).
- **`GET /ready` endpoint** for readiness probes.
- **Processing engine**: cross-database queries and trigger lockdown flags.

For more information, see the InfluxDB 3 Core release notes.

### InfluxDB 3.10 is now available

InfluxDB 3 Enterprise 3.10 adds automated backup and restore, row-level deletions, and user management, with an automatic catalog format upgrade and performance preview improvements.

**Key updates in InfluxDB 3 Enterprise 3.10:**

- **Catalog format upgrade**: the on-disk catalog automatically upgrades from format v2 to v3 on first 3.10 startup. Migration is one-way—back up your catalog before upgrading.
- **Automated backup and restore** (beta)
- **Row-level deletions**
- **User management** (authentication and RBAC) — preview
- **Performance preview improvements**

Backup and restore, row-level deletions, and the performance preview require the Enterprise storage engine upgrade (opt-in beta). *Beta and preview features are subject to breaking changes and aren’t recommended for production use.*

For more information, see the InfluxDB 3 Enterprise release notes

### Telegraf Enterprise is now generally available

Telegraf Enterprise

is now generally available, along with

Telegraf Controller v1.0

.

Telegraf Enterprise combines Telegraf Controller, a centralized management console for Telegraf, with official support from InfluxData. Manage configurations, monitor fleet health, and operate tens of thousands of Telegraf agents from a single system.

- Read the announcement
- Documentation
- Download and install Telegraf Controller

### InfluxDB Docker latest tag changing to InfluxDB 3 Core

On

September 15, 2026

, the

latest

tag for InfluxDB Docker images will point to InfluxDB 3 Core. To avoid unexpected upgrades, use specific version tags in your Docker deployments.

If using Docker to install and run InfluxDB, the `latest` tag will point to InfluxDB 3 Core. To avoid unexpected upgrades, use specific version tags in your Docker deployments. For example, if using Docker to run InfluxDB v2, replace the `latest` version tag with a specific version tag in your Docker pull command–for example:

```sh
docker pull influxdb:2
```
