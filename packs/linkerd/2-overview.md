---
title: "Overview"
source: https://linkerd.io/2/overview/
domain: linkerd
license: CC-BY-SA-4.0
tags: linkerd service mesh, service mesh, cloud native networking, mesh proxy
fetched: 2026-07-02
---

# Overview

Linkerd is a *service mesh* for Kubernetes. It makes running services easier and safer by giving you runtime debugging, observability, reliability, and security—all without requiring any changes to your code.

For a brief introduction to the service mesh model, we recommend reading The Service Mesh: What Every Software Engineer Needs to Know about the World’s Most Over-Hyped Technology.

Linkerd is fully open source, licensed under Apache v2, and is a Cloud Native Computing Foundation graduated project. Linkerd is developed in the open in the Linkerd GitHub organization.

Linkerd has two basic components: a *control plane* and a *data plane*. Once Linkerd’s control plane has been installed on your Kubernetes cluster, you add the data plane to your workloads (called “meshing” or “injecting” your workloads) and voila! Service mesh magic happens.

You can get started with Linkerd in minutes!

## How it works

Linkerd works by installing a set of ultralight, transparent “micro-proxies” next to each service instance. These proxies automatically handle all traffic to and from the service. Because they’re transparent, these proxies act as highly instrumented out-of-process network stacks, sending telemetry to, and receiving control signals from, the control plane. This design allows Linkerd to measure and manipulate traffic to and from your service without introducing excessive latency.

In order to be as small, lightweight, and safe as possible, Linkerd’s micro-proxies are written in Rust and specialized for Linkerd. You can learn more about these micro-proxies in our blog post, Under the hood of Linkerd’s state-of-the-art Rust proxy, Linkerd2-proxy, (If you want to know why Linkerd doesn’t use Envoy, you can learn why in our blog post, Why Linkerd doesn’t use Envoy.)

## Getting Linkerd

Linkerd is available in a variety of packages and channels. See the Linkerd Releases page for details.

## Next steps

Get started with Linkerd in minutes, or check out the architecture for more details on Linkerd’s components and how they all fit together.
