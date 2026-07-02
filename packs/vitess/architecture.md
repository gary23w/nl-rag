---
title: "The Vitess Docs"
source: https://vitess.io/docs/22.0/overview/architecture/
domain: vitess
license: CC-BY-SA-4.0
tags: vitess, mysql sharding, database clustering, horizontal scaling
fetched: 2026-07-02
---

# The Vitess Docs

Architecture

<<

What Is Vitess

Supported Databases

>>

The Vitess platform consists of a number of server processes, command-line utilities, and web-based utilities, backed by a consistent metadata store.

Depending on the current state of your application, you could arrive at a full Vitess implementation through a number of different process flows. For example, if you're building a service from scratch, your first step with Vitess would be to define your database topology. However, if you need to scale your existing database, you'd likely start by deploying Vitess in Unmanaged mode.

Vitess tools and servers are designed to help you whether you start with a complete fleet of databases or start small and scale over time. For smaller implementations, vttablet features like connection pooling and query rewriting help you get more from your existing hardware. Vitess' automation tools then provide additional benefits for larger implementations.

The diagram below illustrates Vitess' components:

For additional details on each of the components, see Concepts.

<<

What Is Vitess

Supported Databases

>>
