---
title: "Overview"
source: https://docs.drone.io/pipeline/overview/
domain: drone-ci
license: CC-BY-SA-4.0
tags: drone ci, container native ci, continuous integration, ci pipeline
fetched: 2026-07-02
---

# Overview

Pipelines help you automate steps in your software delivery process, such as initiating code builds, running automated tests, and deploying to a staging or production environment.

Pipeline execution is triggered by a source code repository. A change in code triggers a webhook to Drone which runs the corresponding pipeline. Other common triggers include automatically scheduled or user-initiated workflows.

Pipelines are configured by placing a `.drone.yml` file in the root of your git repository. The yaml syntax is designed to be easy to read and expressive so that anyone viewing the repository can understand the workflow.

Example pipeline configuration:

| `1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19` | `--- kind: pipeline type: docker name: default steps: - name: backend image: golang commands: - go build - go test - name: frontend image: node commands: - npm install - npm run test ...` |
|---|---|

Drone supports different types of pipelines, each optimized for different use cases and runtime environments:

Docker Pipelines Kubernetes Pipelines Exec Pipelines SSH Pipelines Digital Ocean Pipelines MacStadium Pipelines
