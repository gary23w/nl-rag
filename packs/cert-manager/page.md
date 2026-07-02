---
title: "cert-manager"
source: https://cert-manager.io/docs/
domain: cert-manager
license: CC-BY-SA-4.0
tags: cert manager, certificate automation, public key infrastructure, acme certificates
fetched: 2026-07-02
---

# cert-manager

cert-manager creates TLS certificates for workloads in your Kubernetes or OpenShift cluster and renews the certificates before they expire.

cert-manager can obtain certificates from a variety of certificate authorities, including: Let's Encrypt, HashiCorp Vault, CyberArk Certificate Manager and private PKI.

With cert-manager's Certificate resource, the private key and certificate are stored in a Kubernetes Secret which is mounted by an application Pod or used by an Ingress controller. With csi-driver, csi-driver-spiffe, or istio-csr , the private key is generated on-demand, before the application starts up; the private key never leaves the node and it is not stored in a Kubernetes Secret.

(High level overview diagram explaining cert-manager architecture)

This website provides the full technical documentation for the project, and can be used as a reference; if you feel that there's anything missing, please let us know or raise a PR to add it.
