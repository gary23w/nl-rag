---
title: "Features"
source: https://linkerd.io/2/features/
domain: linkerd
license: CC-BY-SA-4.0
tags: linkerd service mesh, service mesh, cloud native networking, mesh proxy
fetched: 2026-07-02
---

# Features

Linkerd offers many features, outlined below. For our walkthroughs and guides, please see the Linkerd task docs. For a reference, see the Linkerd reference docs.

## Linkerd’s features

- HTTP, HTTP/2, and gRPC Proxying Linkerd will automatically enable advanced features (including metrics, load balancing, retries, and more) for HTTP, HTTP/2, and gRPC connections.
- TCP Proxying and Protocol Detection Linkerd is capable of proxying all TCP traffic, including TLS'd connections, WebSockets, and HTTP tunneling.
- Retries and Timeouts Linkerd can retry and timeout HTTP and gRPC requests.
- Automatic mTLS Linkerd automatically enables mutual Transport Layer Security (TLS) for all communication between meshed applications.
- Ingress Linkerd can work alongside your ingress controller of choice.
- Telemetry and Monitoring Linkerd automatically collects metrics from all services that send traffic through it.
- Load Balancing Linkerd automatically load balances requests across all destination endpoints on HTTP, HTTP/2, and gRPC connections.
- Authorization Policy Linkerd can restrict which types of traffic are allowed between meshed services.
- Automatic Proxy Injection Linkerd will automatically inject the data plane proxy into your pods based annotations.
- CNI Plugin Linkerd can optionally use a CNI plugin instead of an init-container to avoid NET_ADMIN capabilities.
- Dashboard and on-cluster metrics stack Linkerd provides a full on-cluster metrics stack, including CLI tools and dashboards.
- Distributed Tracing You can enable distributed tracing support in Linkerd.
- Dynamic Request Routing Linkerd can route individual HTTP requests based on their properties.
- Egress Linkerd features capabilities to monitor and apply policies to egress traffic.
- Fault Injection Linkerd provides mechanisms to programmatically inject failures into services.
- Gateway API support Linkerd uses Gateway API resource types to configure certain features.
- High Availability The Linkerd control plane can run in high availability (HA) mode.
- HTTP Access Logging Linkerd proxies can be configured to emit HTTP access logs.
- Iptables-nft Support Linkerd's init container can use iptables-nft on systems that require it.
- IPv6 Support Linkerd is compatible with both IPv6-only and dual-stack clusters.
- Multi-cluster communication Linkerd can transparently and securely connect services that are running in different clusters.
- Native sidecars Linkerd supports Kubernetes native sidecars, which fix some of the long-standing annoyances of using sidecar containers in Kubernetes, especially around support for Jobs and race conditions around container startup.
- Non-Kubernetes workloads (mesh expansion)
- Rate Limiting Linkerd offers a simple and performant HTTP local rate limiting solution to protect services from misbehaved clients
- Service Profiles Linkerd's service profiles enable per-route metrics as well as retries and timeouts.
- Topology Aware Routing Linkerd's implementation of Kubernetes topology aware routing enables endpoint consumption based on a node's zone label.
- Traffic Split (canaries, blue/green deploys) Linkerd can dynamically send a portion of traffic to different services.
