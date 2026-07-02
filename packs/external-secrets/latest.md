---
title: "Introduction"
source: https://external-secrets.io/latest/
domain: external-secrets
license: CC-BY-SA-4.0
tags: external secrets operator, secret store sync, provider backed secret, secret synchronization
fetched: 2026-07-02
---

# Sponsored by

(cs-logo) (External Secrets inc.) (Form3) (Pento)

# Introduction

(high-level)

**External Secrets Operator** is a Kubernetes operator that integrates external secret management systems like AWS Secrets Manager, HashiCorp Vault, Google Secrets Manager, Azure Key Vault, IBM Cloud Secrets Manager, CyberArk Secrets Manager, Pulumi ESC and many more. The operator reads information from external APIs and automatically injects the values into a Kubernetes Secret.

### What is the goal of External Secrets Operator?

The goal of External Secrets Operator is to synchronize secrets from external APIs into Kubernetes. ESO is a collection of custom API resources - `ExternalSecret`, `SecretStore` and `ClusterSecretStore` that provide a user-friendly abstraction for the external API that stores and manages the lifecycle of the secrets for you.

### Where to get started

To get started, please read through API overview this should give you a high-level overview to understand the API and use-cases. After that please follow one of our guides to get a jump start using the operator. See our getting started guide for installation instructions.

For a complete reference of the API types please refer to our API Reference.

### How to get involved

This project is driven by its users and contributors, and we welcome everybody to get involved. Join our meetings, open issues or ask questions in Slack. The success of this project depends on your input: No contribution is too small - even opinions matter!

How to get involved:

- Bi-weekly Development Meeting every odd week at 8:00 PM Berlin Time on Wednesday (agenda, jitsi call)
- Kubernetes Slack #external-secrets
- Contributing Process
- Twitter

### Kicked off by

(godaddy-logo)
