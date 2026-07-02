---
title: "Get started with Grafana Loki"
source: https://grafana.com/docs/loki/latest/get-started/
domain: grafana-loki
license: CC-BY-SA-4.0
tags: grafana loki, log aggregation, log management, label based logs
fetched: 2026-07-02
---

# Get started with Grafana Loki

Open source

# Get started with Grafana Loki

Loki is a horizontally scalable, highly available, multi-tenant log aggregation system inspired by Prometheus. It’s designed to be very cost-effective and easy to operate. It doesn’t index the contents of the logs, but rather a set of labels for each log stream. Note that the entire content of the log line is searchable, using labels just makes searching more efficient by narrowing the number of logs retrieved during querying.

Because all Loki implementations are unique, the installation process is different for every customer. But there are some steps in the process that are common to every installation.

To collect logs and view your log data generally involves the following steps:

(Loki implementation steps)

1. Install Loki on Kubernetes in monolithic (single-binary) mode, using the recommended Helm chart. Supply the Helm chart with your object storage authentication details.
  - Storage options
  - Configuration reference
  - There are examples for specific object storage providers that you can modify.
2. Deploy Grafana Alloy to collect logs from your applications.
  1. On Kubernetes, deploy Grafana Alloy using the Helm chart. Configure Grafana Alloy to scrape logs from your Kubernetes cluster, and add your Loki endpoint details. Refer to the following section for an example Grafana Alloy configuration file.
  2. Add labels to your logs following our best practices. Most Loki users start by adding labels that describe where the logs are coming from such as region, cluster, or environment.
3. Deploy Grafana or Grafana Cloud and configure a Loki data source.
4. Select the Explore feature in the Grafana main menu. To view logs in Explore:
  1. Pick a time range.
  2. Choose the Loki data source.
  3. Use LogQL in the query editor, use the Builder view to explore your labels, or select from sample pre-configured queries using the **Kick start your query** button.

**Next steps:** Learn more about the Loki query language, LogQL.

## Example Grafana Alloy configuration file to ship Kubernetes Pod logs to Loki

To deploy Grafana Alloy to collect Pod logs from your Kubernetes cluster and ship them to Loki, you can use a Helm chart, and a `values.yaml` file.

This sample `values.yaml` file is configured to:

- Install Grafana Alloy to discover Pod logs.
- Add `container` and `pod` labels to the logs.
- Push the logs to your Loki cluster using the tenant ID `local`.

1. Install Loki with the Helm chart.
2. Deploy Grafana Alloy using the Helm chart. Refer to Install Grafana Alloy on Kubernetes for more information.
3. Create a `values.yaml` file, based on the following example, making sure to update the value for `forward_to = [loki.write.endpoint.receiver]`:`alloy: mounts: varlog: true configMap: content: | logging { level = "info" format = "logfmt" } discovery.kubernetes "pods" { role = "pod" } loki.source.kubernetes "pods" { targets = discovery.kubernetes.pods.targets forward_to = [loki.write.endpoint.receiver] } loki.write "endpoint" { endpoint { url = "http://loki-gateway.default.svc.cluster.local:80/loki/api/v1/push" tenant_id = "local" } }`
4. Then install Alloy in your Kubernetes cluster using:`helm install alloy grafana/alloy -f ./values.yaml`
