---
title: "Grafana Loki OSS"
source: https://grafana.com/oss/loki/
domain: grafana-loki
license: CC-BY-SA-4.0
tags: grafana loki, log aggregation, log management, label based logs
fetched: 2026-07-02
---

# Grafana Loki OSS

Star us on GitHub

|

25,217

# Grafana Loki

Loki is a log aggregation system designed to store and query logs from all your applications and infrastructure.

The easiest way to get started is with Grafana Cloud, our fully composable observability stack.

Create a free account

### Quick links

Loki on GitHub

Docs

Demo: Getting started with logging and Loki

Demo: Scalable logging with Grafana Loki

## Grafana Loki

Loki is a horizontally scalable, highly available, multi-tenant log aggregation system inspired by Prometheus. It is designed to be very cost effective and easy to operate. It does not index the contents of the logs, but rather a set of labels for each log stream.

The Loki project was started at Grafana Labs in 2018, and announced at KubeCon Seattle. Loki is released under the AGPLv3 license.

Grafana Labs is proud to lead the development of the Loki project, building first-class support for Loki into Grafana, and ensuring Grafana Labs customers receive Loki support and features they need.

### Why use Grafana Loki?

It’s really easy to get started

because you can send logs in any format, from any source, using a wide array of clients

100% persistence to object storage

means you get petabyte scale, high throughput and cost-effective & durable storage

Build metrics and generate alerts

from your log lines

No ingestion log formatting requirements

gives you more flexibility and the option to format at query time

Tail your logs in realtime

to see the logs as they come into the system, update the logs after every certain time, view logs for a particular date, etc.

Natively integrates with Prometheus, Grafana and K8s

so you can seamlessly move between metrics, logs and traces within a single UI

(with loki)

Loki’s minimal indexing approach means that storing the same set of logs in Loki requires far less storage than with other solutions

- Log any and all formats
- Fast writes
- Tiny indexes

- Cheaper to run
- Simpler to operate
- Fast queries

- Cut and slice your logs in dynamic ways (Flexible)

## How does Grafana Loki work?

Pull in any logs with Promtail

Promtail is a logs collector built specifically for Loki. It uses the same service discovery as Prometheus and includes analogous features for labeling, transforming, and filtering logs before ingestion into Loki.

Store the logs in Loki

Loki does not index the text of logs. Instead, entries are grouped into streams and indexed with labels.Not only does this reduce costs, it also means log lines are available to query within milliseconds of being received by Loki.

Use LogQL to explore

Use Loki’s powerful query language, LogQL, to explore your logs. Run LogQL queries directly within Grafana to visualize your logs alongside other data sources, or with LogCLI, for those who prefer a command line experience.

Alert on your logs

Set up alerting rules for Loki to evaluate on your incoming log data. Configure Loki to send the resulting alerts to a Prometheus Alertmanager so they can then get routed to the right team.

## Built on open source, driven by the community

(active users)

66k+

Active users

(github)

12k+

GitHub stars

(github)

400+

Contributors

### Get started

Loki source

Getting started guide

Try on Grafana Cloud

### Get involved

Contribute

Community forum

Grafana Labs Slack

### Get help

Request a feature

Report a bug

Email us

### Learn more

Browse tutorials

See user success stories

Read the docs

## Meet the Grafana Loki contributors

Grafana Labs is proud to lead the development of the Loki project. And we’re hiring!

Work with great people like these

## Choose the version that works best for you

To use Grafana Logs, you have three options:

### Grafana Loki

Horizontally scalable, highly available, multi-tenant log aggregation system inspired by Prometheus.

For users who prefer to set up, administer, and maintain their own installation.

Download

Easiest way to get started

### Cloud Logs

Offered as a fully managed service, Grafana Cloud Logs is a lightweight and cost-effective log aggregation system based on Grafana Loki.

Managed and administered by Grafana Labs with free and paid options for individuals, teams, and large enterprises.

Get up to 50GB of logs at no cost in the free tier of Grafana Cloud.

Create FREE account

### Enterprise Logs

A self-managed logging solution that runs securely at scale with expert support from Grafana Labs.

A self-managed option for organizations that have special requirements around data localization and privacy.

Request a demo

## Featured Loki videos

60 min

### Getting started with logging and Grafana Loki

Watch

Webinar

### Getting started with managing your metrics, logs, and traces using Grafana

Register

Webinar

### Scaling and securing your logs with Grafana Loki

Watch

More videos

## Live, laugh, love, log

Create free account
