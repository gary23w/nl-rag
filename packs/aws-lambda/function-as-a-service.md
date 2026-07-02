---
title: "Function as a service"
source: https://en.wikipedia.org/wiki/Function_as_a_service
domain: aws-lambda
license: CC-BY-SA-4.0
tags: aws lambda, serverless function, lambda function, function as a service
fetched: 2026-07-02
---

# Function as a service

**Function as a service** is a "platform-level cloud capability" that enables its users "to build and manage microservices applications with low initial investment for scalability," according to ISO/IEC 22123-2.

Function as a Service is a subset of the serverless computing ecosystem.

## Anti-patterns

The "Grain of Sand Anti-pattern" refers to the creation of excessively small components (e.g., functions) within a system, often resulting in increased complexity, operational overhead, and performance inefficiencies. "Lambda Pinball" is a related anti-pattern that can occur in serverless architectures when functions (e.g., AWS Lambda, Azure Functions) excessively invoke each other in fragmented chains, leading to latency, debugging and testing challenges, and reduced observability. These anti-patterns are associated with the formation of a distributed monolith.

These anti-patterns are often addressed through the application of clear domain boundaries, which distinguish between public and published interfaces. Public interfaces are technically accessible interfaces, such as methods, classes, API endpoints, or triggers, but they do not come with formal stability guarantees. In contrast, published interfaces involve an explicit stability contract, including formal versioning, thorough documentation, a defined deprecation policy, and often support for backward compatibility. Published interfaces may also require maintaining multiple versions simultaneously and adhering to formal deprecation processes when breaking changes are introduced.

Fragmented chains of function calls are often observed in systems where serverless components (functions) interact with other resources in complex patterns, sometimes described as spaghetti architecture or a distributed monolith. In contrast, systems exhibiting clearer boundaries typically organize serverless components into cohesive groups, where internal public interfaces manage inter-component communication, and published interfaces define communication across group boundaries. This distinction highlights differences in stability guarantees and maintenance commitments, contributing to reduced dependency complexity.

Additionally, patterns associated with excessive serverless function chaining are sometimes addressed through architectural strategies that emphasize native service integrations instead of individual functions, a concept referred to as the functionless mindset. However, this approach is noted to involve a steeper learning curve, and integration limitations may vary even within the same cloud vendor ecosystem.

## Portability issues

Function as a service workloads may encounter migration obstacles due to service lock-in from tight vendor integrations. Hexagonal architecture can facilitate workload portability.
