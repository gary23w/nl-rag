---
title: "Consul Documentation"
source: https://developer.hashicorp.com/consul/docs
domain: hashicorp-consul
license: CC-BY-SA-4.0
tags: hashicorp consul, service discovery, service mesh, distributed configuration
fetched: 2026-07-02
---

# Consul Documentation

Consul is a networking tool that provides comprehensive service discovery and service mesh solutions. It solves networking and security challenges when operating microservices and cloud infrastructure in multi-cloud and hybrid cloud environments at any scale. This documentation describes Consul, provides usage workflows for Consul operations and service networking scenarios, and includes specification and API references to help you build custom automated solutions for your network.

- API
- CLI

## Overview

### Popular use cases

Consul is a service networking platform with many features for securing your service communications and automating network service management.

- API Gateway solutionsConsul's API gateway enables external network clients to securely access applications and services.
- Configuration management solutionsConsul supports static and dynamic service configurations based on service and node state.
- Domain Name Service (DNS) solutionsConsul provides DNS functions including lookups, alternate domains, and access controls across runtimes and cloud providers.
- Service discovery solutionsConsul's service discovery capabilities help you discover, track, and monitor the health of services within a network.
- Service mesh solutionsConsul's service mesh features help you secure, manage, and observe service-to-service communication within a network.

### Supported runtimes and platforms

Consul supports many application runtimes and cloud platforms, and enables service networking in hybrid and multi-cloud environments.

- Consul on local and virtual machines
- Consul on Kubernetes
- Consul on Nomad
- Consul on RedHat OpenShift
- Consul on Docker
- Consul on AWS ECS
- Consul on AWS Lambda

## Usage

### Getting started

If you are new to Consul, these resources can help you learn about Consul and quickly get started with its service networking features.

- Consul fundamentalsThis documentation sequence summarizes the core knowledge, interactions, configurations, and operations for new Consul users.
- Get started with Consul on Virtual MachinesThese tutorials include a GitHub repo and a hosted terminal sessions to help you deploy Consul on VMs and explore its service discovery and service mesh features.
- Get started with Consul on KubernetesThese tutorials include a GitHub repo help you deploy Consul on a Kubernetes cluster and explore its service discovery and service mesh features.
- Migrate a monolith with Consul and NomadThese tutorials include a GitHub repo to demonstrate how you can migrate a monolithic application to microservices, integrate it with Consul, run the application on Nomad, and then scale the application automatically.

### Consul operations

The processes to install and manage Consul as a long-running daemon on multiple nodes in a network.

- Deploy ConsulHow to install and start Consul server agents, client agents, and dataplanes on nodes.
- Secure ConsulHow to set up and maintain secure communications with Consul agents, including ACLs, TLS, and gossip.
- Manage multi-tenancyHow to use one Consul datacenter for multiple tenants, with admin partitions, namespaces, network segments, and sameness groups.
- Manage ConsulHow to manage and customize Consul's behavior, including DNS forwarding on nodes, server disaster recovery, rate limiting, and best practices for scale.
- Monitor ConsulHow to export Consul logs and telemetry for insight into agent behavior.
- Upgrade ConsulHow to update the Consul version running in datacenters.

### Service networking

The processes to register services and use Consul's service discovery and service mesh features with your application workloads.

- Register servicesHow to define services and health checks and then register them with Consul.
- Discover servicesHow to use Consul's service discovery features, including Consul DNS, service lookups, load balancing.
- Connect service meshHow to set up and use sidecar proxies in a Consul service mesh.
- Secure north/south network accessHow to configure, deploy, and use the Consul API gateway to secure network ingress and egress.
- Expand east/west network trafficHow to connect Consul datacenters across regions, runtimes, and providers with WAN federation and cluster peering.
- Secure service mesh trafficHow to secure service-to-service communication with service intentions and TLS certificates.
- Manage service mesh trafficHow to route traffic between services in a service mesh, including service failover and progressive rollouts.
- Observe service mesh trafficHow to observe service mesh telemetry and application performance, including Grafana.
- Automate application configurationsHow to automate Consul and applications to update dynamically, including the KV store, Consul-Terraform-Sync (CTS), and Consul template.

## Reference documentation

### Configuration specifications

Manage your network by configuring Consul agents, service definitions, health checks, as well as service mesh behavior and application configuration.

- Agent configuration file
- Helm configuration
- Service definitions
- Health checks
- Consul template
- Consul-Terraform-Sync

## Developers

- Consul HTTP API documentation
- Consul CLI documentation
- Consul tools and integrations
- Example Consul configurations on GitHub
