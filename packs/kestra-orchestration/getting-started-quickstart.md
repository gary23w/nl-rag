---
title: "Quickstart Guide: Run Your First Kestra Workflow"
source: https://kestra.io/docs/getting-started/quickstart
domain: kestra-orchestration
license: CC-BY-SA-4.0
tags: kestra orchestrator, workflow orchestration, data orchestration platform, declarative workflows
fetched: 2026-07-02
---

# Get Started with Kestra: Launch Locally with Docker and Run Your First Workflow

> For the complete documentation index, see
> 
> llms.txt
> 
> . For a full content snapshot, see
> 
> llms-full.txt
> 
> . Append
> 
> .md
> 
> to any
> 
> kestra.io/docs/*
> 
> URL for plain Markdown.

Launch Kestra locally, create a simple flow, and run your first execution in a few minutes.

## Watch the quickstart video

## Prerequisites

- Install Docker in your environment. We recommend Docker Desktop.
- If you use Windows, make sure WSL is enabled.

## Step 1: Start the Kestra container

Once Docker is running, start Kestra with a single command:

```
docker run --pull=always --rm -it -p 8080:8080 --user=root \
  --name kestra \
  -v kestra_data:/app/storage \
  -v kestra_db:/app/data \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /tmp:/tmp \
  kestra/kestra:latest server local
```

If you re-run the command and Docker reports `You have to remove (or rename) that container to be able to reuse that name.`, remove the old container with `docker rm -f kestra` or pick a different `--name`.

This command does the following:

- starts Kestra on port `8080`
- stores local files in the `kestra_data` Docker volume
- persists the H2 database in the `kestra_db` Docker volume
- mounts `/tmp` and the Docker socket so script and container tasks can run locally

The container is ready when the logs show `Main server is running at http://...:8080`.

## Step 2: Open the Kestra UI

Open `http://localhost:8080` in your browser. You will see the Kestra UI when the container is running. From here, create your user and take the product tour to begin building your first flow.

The above command starts Kestra with an embedded H2 database. Storage files are stored on the `kestra_data` Docker volume, and the H2 database is persisted on the `kestra_db` Docker volume. For production-ready persistence with a PostgreSQL database and more configurability, follow the Docker Compose installation.

## Next steps

You’ve taken the product tour, executed your first flow, and explored Kestra. Next, follow the documentation in this order to build on what you’ve learned:

- Continue with a Tutorial to add inputs, outputs, triggers, and more task types.
- Follow the full Installation guide for persistent local or distributed setups.
- Explore the available Plugins to integrate with external systems, and begin orchestrating your applications, microservices, and processes.
- Contribute to Kestra – whether a developer or not, we value outside contribution of all kinds: Plugins, Features, Documentation, Feature Requests, and Bug Reports. Get involved!

**Using an AI coding agent?** Add the Kestra MCP server to Claude Code, Cursor, or any MCP-compatible tool for live access to plugin docs, blueprints, and Kestra documentation while you build.

##### Send Feedback
