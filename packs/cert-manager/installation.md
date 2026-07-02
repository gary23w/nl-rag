---
title: "Installation"
source: https://cert-manager.io/docs/installation/
domain: cert-manager
license: CC-BY-SA-4.0
tags: cert manager, certificate automation, public key infrastructure, acme certificates
fetched: 2026-07-02
---

# Installation

Learn about the various ways you can install cert-manager and how to choose between them.

## Default static install

> You don't require any tweaking of the cert-manager install parameters.

The default static configuration can be installed as follows:

```bash
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.20.3/cert-manager.yaml
```

📖 Read more about installing cert-manager using kubectl apply and static manifests.

## Getting started

> You quickly want to learn how to use cert-manager and what it can be used for.

📖 **kubectl apply**: For new users we recommend installing cert-manager using kubectl apply and static manifests.

📖 **helm**: You can use helm to install cert-manager and this also allows you to customize the installation if necessary.

🚧 **cmctl**: Try the experimental `cmctl x install` command to quickly install cert-manager.

## Continuous deployment

> If you know how to configure your cert-manager setup and want to automate this, you can use the cert-manager Helm chart directly with tools like Flux, ArgoCD and Anthos. Or you can output YAML using `helm template` to generate customized cert-manager installation manifests, which can be piped into your preferred deployment tool.

📖 **Continuous Deployment**: Learn how to automate the installation of cert-manager using tools like Flux and Argo CD.
