---
title: "etcd"
source: https://en.wikipedia.org/wiki/Etcd
domain: etcd-store
license: CC-BY-SA-4.0
tags: etcd, distributed key-value store, raft consensus, apache zookeeper
fetched: 2026-07-02
---

# etcd

**etcd** is a key-value database commonly deployed with distributed systems. The software is used by Kubernetes. It is written in the Go programming language and published under the Apache License 2.0.

## History

etcd was originally developed as part of the CoreOS project, it was first announced in June of 2013. It was later donated to the Cloud Native Computing Foundation (CNCF). It became a CNCF incubating project in December 2018, and graduated in November of 2020. At the time, the maintainer team consisted of 10 members, including: Amazon, Google Cloud, IBM, Alibaba, and Red Hat. As of 2018, all 32 of the CFNFs Kubernetes compliant distributions and platforms used etcd as their datastore.

According to a 2024 report by the CNCF, the project had over 3300 contributors and at least 450 contributing companies.

The first stable version of etcd, v2.0.0, was released on January 28, 2015. v3.0.0 was released on June 30, 2016.

## Name

The name "etcd" is derived from the Unix convention of storing system configuration files in the `/etc` directory, which applies to a single system, etcd stores configurations for a distributed system, hence the appended "d" standing for "distributed".

## Architecture

The software consists of three executables:

- `etcd`
- `etcdctl`
- `etcdutl`

On particular database entries, locks can be set to prevent writing by other entities while it is being used. It uses the raft consensus algorithm.

Etcd was initially inspired by Chubby, a distributed lock manager developed Google in 2006, as well as Apache ZooKeeper.

## Features

It supports TLS/SSL encryption, exposes a client-facing gRPC API, and supports multiversion concurrency control, and runtime cluster membership reconfiguration.

The official IANA assigned ports for etcd are TCP 2379/2380.

## Users

Etcd is used to store cluster data by default for most Kubernetes implementations, like AWS EKS. One notable exception being Google Kubernetes Engine, whose control-plane datastore was migrated from etcd to a Spanner-based store in 2024, while preserving etcd compatibility.

Kubernetes also depends on the etcd API to communicate with its datastore, meaning that all storage backends used by it are required to support the etcd API.
