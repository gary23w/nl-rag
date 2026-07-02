---
title: "Grafana Tempo"
source: https://grafana.com/docs/tempo/latest/
domain: thanos-metrics
license: CC-BY-SA-4.0
tags: thanos metrics, prometheus long term storage, highly available metrics, global query view
fetched: 2026-07-02
---

# Grafana Tempo

Open source

# Grafana Tempo

Grafana Tempo is an open-source, easy-to-use, and high-scale distributed tracing backend. Tempo lets you search for traces, generate metrics from spans, and link your tracing data with logs and metrics.

## Overview

Distributed tracing visualizes the lifecycle of a request as it passes through a set of applications.

Tempo is cost-efficient and only requires an object storage to operate. Tempo is deeply integrated with Grafana, Mimir, Prometheus, and Loki. You can use Tempo with open source tracing protocols, including Jaeger, Zipkin, or OpenTelemetry.

Tempo integrates well with a number of open source tools:

- **Grafana** ships with native support using the built-in Tempo data source.
- **Grafana Loki**, with its powerful query language LogQL v2 lets you filter requests that you care about, and jump to traces using the Derived fields support in Grafana.
- **Prometheus exemplars** let you jump from Prometheus metrics to Tempo traces by clicking on recorded exemplars.

## Explore

Learn about tracing

What is distributed tracing? Learn about traces and how you can use them, how you can instrument your app for tracing, and how you can visualize tracing data in Grafana.

Solutions and use cases

Learn how tracing data can help you understand application insights and performance as well as help triage issues in your services and applications.

Set up for tracing

Plan your deployment to meet your needs, deploy Tempo, test your installation, and instrument your app or services for traces.

Manage Tempo

Learn about Tempo architecture, best practices, Parquet backend, dedicated attribute columns, and more.

Metrics and tracing

Learn about metrics created from traces, including the metrics-generator processor and TraceQL metrics.

Query with TraceQL

Inspired by PromQL and LogQL, TraceQL is a query language designed for selecting traces in Tempo. This query language lets you precisely and easily select spans and jump directly to the spans fulfilling the specified conditions.
