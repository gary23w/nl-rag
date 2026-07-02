---
title: "Twelve-Factor App methodology"
source: https://en.wikipedia.org/wiki/Twelve-Factor_App_methodology
domain: swe-practice
license: CC-BY-SA-4.0
tags: semantic versioning, software license, technical documentation, twelve-factor, code convention
fetched: 2026-07-02
---

# Twelve-Factor App methodology

The **Twelve-Factor App methodology** is a methodology for building software-as-a-service applications. These best practices are designed to enable applications to be built with portability and resilience when deployed to the web.

## History

The methodology was drafted by developers at Heroku, a platform-as-a-service company, and was first presented by Adam Wiggins circa 2011.

## The Twelve Factors

| # | Factor | Description |
|---|---|---|
| I | Codebase | There should be exactly one codebase for a deployed service with the codebase being used for many deployments. |
| II | Dependencies | All dependencies should be declared, with no implicit reliance on system tools or libraries. |
| III | Config | Configuration that varies between deployments should be stored in the environment. |
| IV | Backing services | All backing services are treated as attached resources and attached and detached by the execution environment. |
| V | Build, release, run | The delivery pipeline should strictly consist of build, release, run. |
| VI | Processes | Applications should be deployed as one or more stateless processes with persisted data stored on a backing service. |
| VII | Port binding | Self-contained services should make themselves available to other services by specified ports. |
| VIII | Concurrency | Concurrency is advocated by scaling individual processes. |
| IX | Disposability | Fast startup and shutdown are advocated for a more robust and resilient system. |
| X | Dev/Prod parity | All environments should be as similar as possible. |
| XI | Logs | Applications should produce logs as event streams and leave the execution environment to aggregate. |
| XII | Admin Processes | Any needed admin tasks should be kept in source control and packaged with the application. |

## Criticism and adaptation

An Nginx architect argued that the relevance of the Twelve-Factor app concept is somewhat specific to Heroku, while introducing their own (Nginx's) proposed architecture for microservices. The twelve factors are however cited as a baseline from which to adapt or extend.
