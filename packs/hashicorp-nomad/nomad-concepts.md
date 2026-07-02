---
title: "Documentation"
source: https://developer.hashicorp.com/nomad/docs/concepts
domain: hashicorp-nomad
license: CC-BY-SA-4.0
tags: hashicorp nomad, workload orchestration, cluster scheduler, container orchestration
fetched: 2026-07-02
---

# Nomad Documentation

Nomad is a highly available, distributed, data-center aware cluster and application scheduler designed to support the modern datacenter with support for long-running services, batch jobs, and much more.

- API
- CLI
- Tools
- Plugins

## Getting Started

Learn how to use Nomad to schedule and orchestrate workloads.

CLI Quick Start

## Use Cases

### Fundamentals

Become familiar with the core concepts of Nomad.

- Installing NomadNomad is available as a pre-compiled binary, a package for several OSs, or as source code for you to build from.
- Writing Job SpecsThe Nomad job specification or 'jobspec' is written in HCL and defines the schema for Nomad jobs.
- Agent ConfigurationThe Nomad agent specification is written in HCL and defines configs like networking, plugins, and integrations.
- Manage Nomad JobsLearn how to deploy and manage jobs.

### Nomad Pack

Use Nomad Pack to deploy popular applications to Nomad.

- Introduction to Nomad PackLearn about Nomad Pack and how to use it to easily create, share, deploy, and re-use Nomad job specs.
- Write a custom Nomad PackLearn how to create your own custom Nomad Pack.
- Community RepositoryThe registry of community-maintained packs for Nomad Pack.

### Autoscaling

Automatically maintain your cluster and workload instance count to respond to demand while minimizing over-provisioning cost.

- Introduction to AutoscalingThe Nomad Autoscaler is a horizontal application and cluster autoscaler for Nomad.
- Horizontal Cluster AutoscalingLearn how to use the autoscaler to dynamically scale infrastructure up and down and handle application load spikes.
- Create On-demand Batch JobsLearn how to use the autoscaler to automatically provision and decommission clients for running batch jobs.
- Manage Job Placement and AffinitiesLearn how to use the affinity stanza to express job placement preferences.

### Cluster Management

Learn the features operators will need to build and maintain Nomad clusters.

- Upgrade a ClusterLearn about the process of upgrading a cluster including upgrading in place.
- Enable Multi-Region FederationLearn how to use federation to allow users to submit jobs or interact with the API from any region attached to the cluster.
- Connect Nodes into a ClusterLearn how to connect nodes to a cluster manually, with Cloud Auto-Join, or with Consul.
- Enable AutopilotLearn about the Autopilot features and how to use them to cleanup servers, monitor Raft state, and introduce servers stably.

## Developers

- Provision Nomad with Terraform
- API Reference
- Nomad Ecosystem Tools
- Community Task Drivers
