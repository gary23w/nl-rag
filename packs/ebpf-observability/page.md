---
title: "Welcome to Cilium’s documentation!"
source: https://docs.cilium.io/en/stable/
domain: ebpf-observability
license: CC-BY-SA-4.0
tags: ebpf tracing, kernel probe instrumentation, in kernel observability, bpf program
fetched: 2026-07-02
---

# Welcome to Cilium’s documentation!

The documentation is divided into the following sections:

- Cilium Quick Installation: Provides a simple tutorial for running a small Cilium setup on your laptop. Intended as an easy way to get your hands dirty applying Cilium security policies between containers.
- Getting Started : Details instructions for installing, configuring, and troubleshooting Cilium in different deployment modes.
- Overview of Network Policy : Detailed walkthrough of the policy language structure and the supported formats.
- Observability : Provides instructions on setting up and configuring Network Observability with Hubble and configuring metrics collection from Cilium and Hubble.
- Troubleshooting : Describes how to troubleshoot Cilium in different deployment modes.
- BPF and XDP Reference Guide : Provides a technical deep dive of eBPF and XDP technology, primarily focused at developers.
- API Reference : Details the Cilium agent API for interacting with a local Cilium instance.
- Development : Gives background to those looking to develop and contribute modifications to the Cilium code or documentation.
- Securing Networks with Cilium : Provides a one-page resource of best practices for securing Cilium.

A hands-on tutorial in a live environment is also available for users looking for a way to quickly get started and experiment with Cilium.

Overview

- Introduction to Cilium & Hubble
  - What is Cilium?
  - What is Hubble?
  - Why Cilium & Hubble?
  - Functionality Overview
- Component Overview
  - Cilium
  - Hubble
  - eBPF
  - Data Store

Getting Started

- Cilium Quick Installation
  - Create the Cluster
  - Install the Cilium CLI
  - Install Cilium
  - Validate the Installation
  - Next Steps
- Getting Started with the Star Wars Demo
  - Deploy the Demo Application
  - Check Current Access
  - Apply an L3/L4 Policy
  - Inspecting the Policy
  - Apply and Test HTTP-aware L7 Policy
  - Clean-up
  - Next Steps
- Terminology
  - Labels
  - Endpoint
  - Identity
  - Node
- Getting Help
  - FAQ
  - Slack
  - GitHub
  - Training
  - Enterprise support
  - Security Bugs

Advanced Installation

- Considerations on Node Pool Taints and Unmanaged Pods
- Installation using Helm
  - Helm Installation Methods
  - Install Cilium
  - Upgrading
  - OCI vs Traditional Repository
  - Troubleshooting
  - Restart unmanaged Pods
  - Validate the Installation
  - Next Steps
- Migrating a cluster to Cilium
  - Background
  - Requirements
  - Limitations
  - Overview
  - Migration procedure
- Installation with K8s distributions
  - Installation with external etcd
  - Installation on OpenShift OKD
  - Installation on Broadcom VMware ESXi / NSX
  - Installation Using K3s
  - Installation k0s Using k0sctl
  - Installation Using Kind
  - CNI Chaining
- External Installers
  - Installation using Azure CNI Powered by Cilium in AKS
  - Installation using Kops
  - Installation using Kubespray
  - Installation using kubeadm
  - Installation using Rancher
  - Installation using Rancher Kubernetes Engine
  - Installation Using Rancher Desktop

Networking

- Networking Concepts
  - Routing
  - IP Address Management (IPAM)
  - Masquerading
  - Fragment Handling
- Kubernetes Networking
  - Introduction
  - Concepts
  - Requirements
  - Configuration
  - Network Policy
  - Kubernetes Without kube-proxy
  - CiliumCIDRGroup
  - Endpoint CRD
  - CiliumEndpointSlice
  - Kubernetes Compatibility
  - Troubleshooting
  - Bandwidth Manager
  - Kata Containers with Cilium
  - Configuring IPAM Modes
  - Local Redirect Policy
  - Identity Management Mode
- BGP
  - Cilium BGP Control Plane
  - LoadBalancer IP Address Management (LB IPAM)
  - Using Kube-Router to Run BGP (deprecated)
  - Using BIRD to run BGP (deprecated)
- eBPF Datapath
  - Introduction
  - Life of a Packet
  - eBPF Maps
  - Service LB Map Sizing
  - Iptables Usage
- Multi-cluster Networking
  - Multi-Cluster (Cluster Mesh)
  - Setting up Cluster Mesh
  - Load-balancing & Service Discovery
  - Multi-Cluster Services API (Beta)
  - Network Policy
  - Service Affinity
  - AKS-to-AKS Clustermesh Preparation
  - EKS-to-EKS Clustermesh Preparation
  - GKE-to-GKE Clustermesh Preparation
- Egress Gateway
  - Egress Gateway
  - Egress Gateway Advanced Troubleshooting
- Service Mesh
  - What is Service Mesh?
  - Why Cilium Service Mesh?
- VXLAN Tunnel Endpoint (VTEP) Integration (beta)
  - Enable VXLAN Tunnel Endpoint (VTEP) integration
  - How to test VXLAN Tunnel Endpoint (VTEP) Integration
  - Limitations
- L2 Announcements / L2 Aware LB (Beta)
  - Configuration
  - Prerequisites
  - Limitations
  - Policies
  - Leader Election
  - Troubleshooting
  - L2 Pod Announcements
- Node IPAM LB
  - Enable and use Node IPAM
- Use a Specific MAC Address for a Pod
  - Configuring the address
- Multicast Support in Cilium (Beta)
  - Prerequisites
  - Enable Multicast Feature
  - Configure Multicast and Subscriber IPs
  - Limitations

Security

- Securing Networks with Cilium
  - Identity-Aware and HTTP-Aware Policy Enforcement
  - Locking Down External Access with DNS-Based Policies
  - Standalone DNS Proxy (alpha)
  - Inspecting TLS Encrypted Connections with Cilium
  - Securing a Kafka Cluster
  - Securing gRPC
  - Securing Elasticsearch
  - Locking Down External Access Using AWS Metadata
  - Creating Policies from Verdicts
  - Host Firewall
  - Restricting privileged Cilium pod access
- Overview of Network Security
  - Introduction
  - Identity-Based
  - Policy Enforcement
  - Proxy Injection
  - Transparent Encryption
- Overview of Network Policy
  - Policy Enforcement Modes
  - Policy Deny Response Handling
  - Rule Basics
  - Layer 3 Policies
  - Layer 4 Policies
  - Layer 7 Policies
  - Deny Policies
  - Disk based Cilium Network Policies
  - Host Policies
  - Using Kubernetes Constructs In Policy
  - Endpoint Lifecycle
  - Troubleshooting
  - Caveats
- Restricting privileged Cilium pod access
  - Setup Cilium
- Threat Model
  - Scope and Prerequisites
  - Methodology
  - Reference Architecture
  - The Threat Model
  - Overall Recommendations

Observability

- Network Observability with Hubble
  - Setting up Hubble Observability
  - Inspecting Network Flows with the CLI
  - Service Map & Hubble UI
  - Tutorial: Monitoring Generic IP Options with Cilium
  - Configuring Hubble exporter
  - Configure TLS with Hubble
- Running Prometheus & Grafana
  - Install Prometheus & Grafana
  - Deploy Cilium and Hubble with metrics enabled
  - How to access Grafana
  - How to access Prometheus
  - Examples
- Monitoring & Metrics
  - Cilium Metrics
  - Hubble Metrics
  - Cluster Mesh API Server Metrics
  - Example Prometheus & Grafana Deployment
  - Metrics Reference
- Layer 7 Protocol Visibility
  - Security Implications
  - Limitations

Operations

- System Requirements
  - Summary
  - Architecture Support
  - Linux Distribution Compatibility & Considerations
  - Linux Kernel
  - Required Kernel Versions for Advanced Features
  - Key-Value store
  - clang+LLVM
  - Firewall Rules
  - Mounted eBPF filesystem
  - Routing Tables
  - Privileges
- Upgrade Guide
  - Running pre-flight check (Required)
  - Upgrading Cilium
  - Version Specific Notes
  - Advanced
- Configuration
  - `cilium-config` ConfigMap
  - Making Changes
  - Detecting unapplied ConfigMap changes
  - Core Agent
  - Security
- Performance & Scalability
  - Tuning Guide
  - CNI Performance Benchmark
  - Scalability
- Troubleshooting
  - Component & Cluster Health
  - Observing Flows with Hubble
  - Observing flows with Hubble Relay
  - Connectivity Problems
  - Policy Troubleshooting
  - etcd (kvstore)
  - Cluster Mesh Troubleshooting
  - Service Mesh Troubleshooting
  - Symptom Library
  - Useful Scripts
  - Reporting a problem

Community

- Governance
- Community Meetings
  - Weekly Community Meeting
  - Monthly APAC Community Meeting
- Slack
  - Slack channels
  - How to create a Slack channel
- Special Interest Groups
- Roadmap
  - Release Cadence
  - Welcoming New Contributors

Contributor Guide

- Development
  - How To Contribute
  - Contributing as a Reviewer or Committer
  - Development Setup
  - Building Container Images
  - Code Overview
  - Configuring the Datapath
  - Run eBPF Tests with Little VM Helper
  - Guide to the Hive
  - StateDB in Cilium
  - Debugging
  - Hubble
  - Introducing New CRDs
  - BGP Control Plane
  - Updating dependencies with Renovate
- Release Management
  - Organization
  - Backporting process
- Testing
  - CI / GitHub Actions
  - End-To-End Connectivity Testing
  - End-To-End Testing Framework (Legacy)
  - Scalability and Performance Testing
  - Integration Testing
  - BPF Unit and Integration Testing
- Documentation
  - Recommendations on documentation structure
  - Documentation style
  - Documentation testing
  - Documentation framework
- API Reference
  - Introduction
  - How to access the API
  - Compatibility Guarantees
  - API Reference
- gRPC API Reference
  - Flow
  - Observer
  - Peer
  - Relay
- SDP gRPC API Reference
  - Standalone DNS Proxy
- Internals
  - Code Overview
  - Hubble internals
  - Cilium Operator
  - eBPF Program Types
  - Security Identities

Reference

- Command Cheatsheet
  - Command utilities:
  - Command examples:
  - Kubernetes examples:
- Command Reference
  - cilium-agent
  - cilium-bugtool
  - cilium-dbg
  - cilium-health
  - cilium-operator
  - clustermesh-apiserver
  - Key-Value Store
- Helm Reference
- Key-Value Store
  - Layout
  - Leases
  - Caveats and Limitations
  - Debugging
- Further Reading
- Glossary

Reference Guides

- BPF and XDP Reference Guide
  - BPF Architecture
  - Development Tools
  - Debugging and Testing
  - Program Types
  - Further Reading
- XFRM Reference Guide
  - Overview
  - XFRM Packet Flows
  - Output Description of `ip xfrm`
  - XFRM Errors
  - Performance Considerations
