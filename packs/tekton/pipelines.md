---
title: "Tasks and Pipelines"
source: https://tekton.dev/docs/pipelines/
domain: tekton
license: CC-BY-SA-4.0
tags: tekton pipelines, cloud native ci, kubernetes native pipeline, continuous delivery
fetched: 2026-07-02
---

# Tasks and Pipelines

Building Blocks of Tekton CI/CD Workflow

# Tekton Pipelines

Tekton Pipelines is a Kubernetes extension that installs and runs on your Kubernetes cluster. It defines a set of Kubernetes Custom Resources that act as building blocks from which you can assemble CI/CD pipelines. Once installed, Tekton Pipelines becomes available via the Kubernetes CLI (kubectl) and via API calls, just like pods and other resources. Tekton is open-source and part of the CD Foundation, a Linux Foundation project.

## Tekton Pipelines entities

Tekton Pipelines defines the following entities:

| Entity | Description |
|---|---|
| `Task` | Defines a series of steps which launch specific build or delivery tools that ingest specific inputs and produce specific outputs. |
| `TaskRun` | Instantiates a `Task` for execution with specific inputs, outputs, and execution parameters. Can be invoked on its own or as part of a `Pipeline`. |
| `Pipeline` | Defines a series of `Tasks` that accomplish a specific build or delivery goal. Can be triggered by an event or invoked from a `PipelineRun`. |
| `PipelineRun` | Instantiates a `Pipeline` for execution with specific inputs, outputs, and execution parameters. |
| `PipelineResource (Deprecated)` | Defines locations for inputs ingested and outputs produced by the steps in `Tasks`. |
| `Run` (alpha) | Instantiates a Custom Task for execution when specific inputs. |

## Getting started

To get started, complete the Tekton Pipelines Tutorial and go through our examples.

## Understanding Tekton Pipelines

See the following topics to learn how to use Tekton Pipelines in your project:

- Creating a Task
- Running a standalone Task
- Creating a Pipeline
- Running a Pipeline
- Defining Workspaces
- Configuring authentication
- Using labels
- Viewing logs
- Pipelines metrics
- Variable Substitutions
- Running a Custom Task
- Remote resolution of Pipelines and Tasks
- Trusted Resources

## Contributing to Tekton Pipelines

If you’d like to contribute to the Tekton Pipelines project, see the Tekton Pipeline Contributor’s Guide.

Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License.

##### Install Tekton Pipelines

Install Tekton Pipelines on your cluster

##### Additional Configuration Options

Additional configurations when installing Tekton Pipelines

##### Pipeline API

Last modified October 28, 2020:

Add the past 4 versions for pipeline, triggers and CLI (4f7f217)
