---
title: "VictoriaMetrics/README.md at master · VictoriaMetrics/VictoriaMetrics · GitHub"
source: https://github.com/VictoriaMetrics/VictoriaMetrics/blob/master/README.md
domain: victoriametrics
license: CC-BY-SA-4.0
tags: victoriametrics, time series database, prometheus monitoring, metrics database
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

VictoriaMetrics

/

VictoriaMetrics

Public

- Notifications You must be signed in to change notification settings
- Fork 1.7k
- Star

## Expand file tree

More file actions

More file actions

## Latest commit

## History

History

History

## File metadata and controls

131 lines (99 loc) · 13.4 KB

Outline

# VictoriaMetrics

(Latest Release) (Docker Pulls) (Go Report) (Build Status) (License) (Join Slack) (X) (Reddit)

VictoriaMetrics is a fast, cost-effective, and scalable solution for monitoring and managing time series data. It delivers high performance and reliability, making it an ideal choice for businesses of all sizes.

Here are some resources and information about VictoriaMetrics:

- **Case studies**: Grammarly, Roblox, Wix, Spotify,....
- **Available**: Binary releases, Docker images on Docker Hub and Quay, Source code.
- **Deployment types**: Single-node version and Cluster version under Apache License 2.0.
- **Getting started:** Read key concepts and follow the quick start guide.
- **Community**: Slack (join via Slack Inviter), X (Twitter), YouTube. See full list here.
- **Changelog**: Project evolves fast - check the CHANGELOG, and How to upgrade.
- **Enterprise support:** Contact us for commercial support with additional enterprise features.
- **Enterprise releases:** Enterprise and long-term support releases (LTS) are publicly available and can be evaluated for free using a free trial license.
- **Security:** we achieved security certifications for Database Software Development and Software-Based Monitoring Services.

Yes, we open-source both the single-node VictoriaMetrics and the cluster version.

## Prominent features

VictoriaMetrics is optimized for timeseries data, even when old time series are constantly replaced by new ones at a high rate, it offers a lot of features:

- **Long-term storage for Prometheus** or as a drop-in replacement for Prometheus and Graphite in Grafana.
- **Powerful stream aggregation**: Can be used as a StatsD alternative.
- **Ideal for big data**: Works well with large amounts of time series data from APM, Kubernetes, IoT sensors, connected cars, industrial telemetry, financial data and various Enterprise workloads.
- **Query language**: Supports both PromQL and the more performant MetricsQL.
- **Easy to setup**: No dependencies, single small binary, configuration through command-line flags, but the default is also fine-tuned; backup and restore with instant snapshots.
- **Global query view**: Multiple Prometheus instances or any other data sources may ingest data into VictoriaMetrics and queried via a single query.
- **Various Protocols**: Support metric scraping, ingestion and backfilling in various protocol.
  - Prometheus exporters, Prometheus remote write API, Prometheus exposition format.
  - InfluxDB line protocol over HTTP, TCP and UDP.
  - Graphite plaintext protocol with tags.
  - OpenTSDB put message.
  - HTTP OpenTSDB /api/put requests.
  - JSON line format.
  - Arbitrary CSV data.
  - Native binary format.
  - DataDog agent or DogStatsD.
  - NewRelic infrastructure agent.
  - OpenTelemetry metrics format.
- **NFS-based storages**: Supports storing data on NFS-based storages such as Amazon EFS, Google Filestore.
- And many other features such as metrics relabeling, cardinality limiter, etc.

## Enterprise version

In addition, the Enterprise version includes extra features:

- **Anomaly detection**: Automation and simplification of your alerting rules, covering complex anomalies found in metrics data.
- **Backup automation**: Automates regular backup procedures.
- **Multiple retentions**: Reducing storage costs by specifying different retentions for different datasets.
- **Downsampling**: Reducing storage costs and increasing performance for queries over historical data.
- **Stable releases** with long-term support lines (LTS).
- **Comprehensive support**: First-class consulting, feature requests and technical support provided by the core VictoriaMetrics dev team.
- Many other features, which you can read about on the Enterprise page.

Contact us if you need enterprise support for VictoriaMetrics. Or you can request a free trial license here, downloaded Enterprise binaries are available at Github Releases.

We strictly apply security measures in everything we do. VictoriaMetrics has achieved security certifications for Database Software Development and Software-Based Monitoring Services. See Security page for more details.

## Benchmarks

Some good benchmarks VictoriaMetrics achieved:

- **Minimal memory footprint**: handling millions of unique timeseries with 10x less RAM than InfluxDB, up to 7x less RAM than Prometheus, Thanos or Cortex.
- **Highly scalable and performance** for data ingestion and querying, 20x outperforms InfluxDB and TimescaleDB.
- **High data compression**: 70x more data points may be stored into limited storage than TimescaleDB, 7x less storage space is required than Prometheus, Thanos or Cortex.
- **Reducing storage costs**: 10x more effective than Graphite according to the Grammarly case study.
- **A single-node VictoriaMetrics** can replace medium-sized clusters built with competing solutions such as Thanos, M3DB, Cortex, InfluxDB or TimescaleDB. See VictoriaMetrics vs Thanos, Measuring vertical scalability, Remote write storage wars - PromCon 2019.
- **Optimized for storage**: Works well with high-latency IO and low IOPS (HDD and network storage in AWS, Google Cloud, Microsoft Azure, etc.).

## Community and contributions

Feel free asking any questions regarding VictoriaMetrics:

- Slack Inviter and Slack channel
- X (Twitter)
- Linkedin
- Reddit
- Telegram-en
- Telegram-ru
- Mastodon

If you like VictoriaMetrics and want to contribute, then please read these docs.

## VictoriaMetrics Logo

The provided ZIP file contains three folders with different logo orientations. Each folder includes the following file types:

- JPEG: Preview files
- PNG: Preview files with transparent background
- AI: Adobe Illustrator files

### VictoriaMetrics Logo Usage Guidelines

#### Font

- Font Used: Lato Black
- Download here: Lato Font

#### Color Palette

- Black #000000
- Purple #4d0e82
- Orange #ff2e00
- White #ffffff

### Logo Usage Rules

- Only use the Lato Black font as specified.
- Maintain sufficient clear space around the logo for visibility.
- Do not modify the spacing, alignment, or positioning of design elements.
- You may resize the logo as needed, but ensure all proportions remain intact.

Thank you for your cooperation!
