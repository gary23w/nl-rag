---
title: "Skaffold Pipeline Stages"
source: https://skaffold.dev/docs/pipeline-stages/
domain: skaffold
license: CC-BY-SA-4.0
tags: skaffold workflow, kubernetes development workflow, continuous development, build deploy loop
fetched: 2026-07-02
---

# Skaffold Pipeline Stages

Skaffold features a multi-stage workflow:

(workflow)

When you start Skaffold, it collects source code in your project and builds artifacts with the tool of your choice; the artifacts, once successfully built, are tagged as you see fit and pushed to the repository you specify. In the end of the workflow, Skaffold also helps you deploy the artifacts to your Kubernetes cluster, once again using the tools you prefer.

Skaffold allows you to skip stages. If, for example, you run Kubernetes locally with Minikube, Skaffold will not push artifacts to a remote repository.

| Skaffold Pipeline stages | Description |   |
|---|---|---|
| Init | generate a starting point for Skaffold configuration |   |
| Build | build images with different builders |   |
| Render | render manifests with different renderers |   |
| Tag | tag images based on different policies |   |
| Test | run tests with testers |   |
| Deploy | deploy with kubectl, kustomize or helm |   |
| Verify | verify deployments with specified test containers |   |
| File Sync | sync changed files directly to containers |   |
| Log Tailing | tail logs from workloads |   |
| Port Forwarding | forward ports from services and arbitrary resources to localhost |   |
| Deploy Status Checking | wait for deployed resources to stabilize |   |
| Lifecycle Hooks | run code triggered by different events during the skaffold process lifecycle |   |
| Cleanup | cleanup manifests and images |   |

Last modified November 13, 2025:

chore: Skaffold 2.17 release (#9912) (561ce51e)
