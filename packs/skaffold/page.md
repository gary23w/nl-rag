---
title: "Skaffold 2.0 Documentation"
source: https://skaffold.dev/docs/
domain: skaffold
license: CC-BY-SA-4.0
tags: skaffold workflow, kubernetes development workflow, continuous development, build deploy loop
fetched: 2026-07-02
---

# Skaffold 2.0 Documentation

You are viewing the Skaffold v2 documentation. View the archived v1 documentation here.

Skaffold is a command line tool that facilitates continuous development for container based & Kubernetes applications. Skaffold handles the workflow for building, pushing, and deploying your application, and provides building blocks for creating CI/CD pipelines. This enables you to focus on iterating on your application locally while Skaffold continuously deploys to your local or remote Kubernetes cluster, local Docker environment or Cloud Run project.

## Features

- Fast local Kubernetes Development
  - **optimized “Source to Kubernetes”** - Skaffold detects changes in your source code and handles the pipeline to **build**, **push**, **test** and **deploy** your application automatically with **policy-based image tagging** and **highly optimized, fast local workflows**
  - **continuous feedback** - Skaffold automatically manages deployment logging and resource port-forwarding
- Skaffold projects work everywhere
  - **share with other developers** - Skaffold is the easiest way to **share your project** with the world: `git clone` and `skaffold run`
  - **context aware** - use Skaffold profiles, local user config, environment variables, and flags to easily incorporate differences across environments
  - **platform aware** - use cross-platform and multi-platform **build** support, with automatic platform detection, to easily handle operating system and architecture differences between the development machine and Kubernetes cluster nodes.
  - **CI/CD building blocks** - use `skaffold build`, `skaffold test` and `skaffold deploy` as part of your CI/CD pipeline, or simply `skaffold run` end-to-end
  - **GitOps integration** - use `skaffold render` to build your images and render templated Kubernetes manifests for use in GitOps workflows
- skaffold.yaml - a single pluggable, declarative configuration for your project
  - **skaffold init** - Skaffold can discover your build and deployment configuration and generate a Skaffold config
  - **multi-component apps** - Skaffold supports applications with many components, making it great for microservice-based applications
  - **bring your own tools** - Skaffold has a pluggable architecture, allowing for different implementations of the build and deploy stages
- Lightweight
  - **client-side only** - Skaffold has no cluster-side component, so there’s no overhead or maintenance burden to your cluster
  - **minimal pipeline** - Skaffold provides an opinionated, minimal pipeline to keep things simple

## Demo

(architecture)

## Skaffold Workflow and Architecture

Skaffold simplifies your development workflow by organizing common development stages into one simple command. Every time you run `skaffold dev`, the system

1. Collects and watches your source code for changes
2. Syncs files directly to pods if user marks them as syncable
3. Builds artifacts from the source code
4. Tests the built artifacts using container-structure-tests or custom scripts
5. Tags the artifacts
6. Pushes the artifacts
7. Deploys the artifacts
8. Monitors the deployed artifacts
9. Cleans up deployed artifacts on exit (Ctrl+C)

#### Note

Any of these stages can be skipped.

The pluggable architecture is central to Skaffold’s design, allowing you to use your preferred tool or technology in each stage. Also, Skaffold’s `profiles` feature grants you the freedom to switch tools on the fly with a simple flag.

For example, if you are coding on a local machine, you can configure Skaffold to build artifacts with your local Docker daemon and deploy them to minikube using `kubectl`. When you finalize your design, you can switch to your production profile and start building with Google Cloud Build and deploy with Helm.

Skaffold supports the following tools:

- Dockerfile
  - locally with Docker
  - in-cluster with Kaniko
  - on cloud with Google Cloud Build
- Jib Maven and Gradle
  - locally
  - on cloud with Google Cloud Build
- Bazel locally
- Cloud Native Buildpacks
  - locally with Docker
  - on cloud with Google Cloud Build
- Custom script
  - locally
  - in-cluster

- container-structure-test
- custom script

- Kubernetes Command-Line Interface (`kubectl`)
- Helm
- kustomize

- tag by git commit
- tag by current date & time
- tag by environment variables based template
- tag by digest of the Docker image

- don’t push - keep the image on the local daemon
- push to registry

(architecture)

Besides the above steps, Skaffold also automatically manages the following utilities for you:

- port-forwarding of deployed resources to your local machine using `kubectl port-forward`
- log aggregation from the deployed pods

Last modified November 13, 2025:

chore: Skaffold 2.17 release (#9912) (561ce51e)
