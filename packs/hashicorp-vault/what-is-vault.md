---
title: "What is Vault?"
source: https://developer.hashicorp.com/vault/docs/what-is-vault
domain: hashicorp-vault
license: CC-BY-SA-4.0
tags: hashicorp vault, secrets management, secret sharing, key management
fetched: 2026-07-02
---

# What is Vault?

Vault provides centralized, well-audited privileged access and secret management for mission-critical data whether you deploy systems on-premises, in the cloud, or in a hybrid environment.

With a modular design based around a growing plugin ecosystem, Vault lets you integrate with your existing systems and customize your application workflow.

## Why should I use Vault?

Modern software works because of **secrets**. Secrets are sensitive, discrete pieces of information like credentials, encryption keys, authentication certificates, and other critical pieces of information your applications need to run consistently and securely.

Vault helps harden applications by centralizing secret management. With Vault you can:

- Manage static secrets
- Manage certificates
- Manage identities and authentication
- Manage 3rd-party secrets
- Manage sensitive data
- Support regulatory compliance

Try HCP Vault Dedicated

HCP Vault Dedicated runs Vault in the cloud using the same binary as self-managed Vault Enterprise. It offers a consistent user experience without the hassle of managing deployment clusters or servers.

Sign up for HCP Vault Dedicated or review the HCP Vault Dedicated tutorials to learn more.

## What is a plugin?

Plugins act as building blocks in Vault that let you control how data moves through your environment and how clients access that data.

The plugin ecosystem includes:

- authentication plugins that handle authentication flows and control client access to Vault.
- general secret plugins that generate, store, manage, or transform sensitive information.
- database secret plugins that manage dynamic credentials that clients use to access database data.

Use plugins from the curated plugin registry or build custom plugins to integrate Vault in the way that makes the most sense for you workflows.

## Who can access data in Vault?

Vault encrypts data at rest and gates access to that data with configurable, robust authentication and authorization methods.

(How Vault works)

1. Clients authenticate with manually generated tokens, protocols like LDAP, or third-party providers like Azure and AWS.
2. Vault generates an access token that links the client request to an internal entity and applicable security policies.
3. Clients interact with secrets and encryption operations based on resource paths mounted in Vault.
4. Vault authorizes the client request against policies set on the resource path and grants or denies access accordingly.

Throughout the process, Vault audits all activity, regardless of whether authentication or authorization succeeds so you can track interactions with mission critical systems.

## Where does Vault store data?

Vault supports a variety of options for durable information storage.

| Storage type | HA support | Description |
|---|---|---|
| Integrated | YES | The "built-in" storage option that encrypts and replicates data across an operating Vault cluster. |
| File system | NO | Persists data to the local file system on the machine running Vault. |
| External | MAYBE | A durable third-party storage system like Azure, AWS, Google Cloud, or MySQL. |
| In-memory | NO | Persists data entirely in-memory on the machine running Vault for development and experimentation. |

We recommend integrated storage for most deployments. Integrated storage supports backup/restore workflows, high availability, and Enterprise replication features without relying on third-party systems where Vault cannot verify the security and traceability of data access.

## When should I not use Vault?

Vault is robust, powerful, and flexible. But it can also be overwhelming if you have limited or simple secret management needs.

If your organization is just getting started with secrets management or looking to simplify an existing secrets management processes, consider starting with HCP Vault Dedicated instead of Vault.

HCP Vault Dedicated is a managed offering of Vault that runs on the HashiCorp cloud platform. HCP Vault Dedicated provides a Vault Enterprise cluster without the operational overhead of planning, deploying, and managing a self-hosted Vault cluster.

## How do I get Vault?

You can download Vault as a precompiled binary, install an official Community or Enterprise package with supported package managers, or clone the Vault Community repo in GitHub and build Vault from source code.

To use Vault Enterprise features, you must have a valid license configured.

|   |   |   |   |   |
|---|---|---|---|---|
