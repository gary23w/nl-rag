---
title: "Akka (toolkit)"
source: https://en.wikipedia.org/wiki/Akka_(toolkit)
domain: akka-http-scala
license: CC-BY-SA-4.0
tags: akka http scala, akka actor streams, scala reactive http, akka routing directives
fetched: 2026-07-02
---

# Akka (toolkit)

**Akka** is a source-available platform, SDK, toolkit, and runtime simplifying building concurrent and distributed applications on the JVM, for example, agentic AI, microservices, edge/IoT, and streaming applications. Akka supports multiple programming models for concurrency and distribution, but it emphasizes actor-based concurrency, with inspiration drawn from Erlang.

Language bindings exist for both Java and Scala. Akka is mainly written in Scala.

## History

An actor implementation, written by Philipp Haller, was released in July 2006 as part of Scala 2.1.7. By 2008 Scala was attracting attention for use in complex server applications, but concurrency was still typically achieved by creating threads that shared memory and synchronized when necessary using locks. Aware of the difficulties with that approach and inspired by the Erlang programming language's library support for writing highly concurrent, distributed, and event-driven applications, the Swedish programmer Jonas Bonér created Akka to bring similar capabilities to the JVM. Bonér began working on Akka in early 2009 and wrote up his vision for it in June of that year. The first public release was Akka 0.5, announced in January 2010. Akka is now part of the Lightbend Platform together with the Play framework and the Scala programming language.

In September 2022, Lightbend announced that Akka would change its license from the free software license Apache License 2.0 to a proprietary source-available license, known as the Business Source License (BSL). Any new code under the BSL would become available under the Apache License after three years.

Apache Pekko is an Apache licensed fork of Akka.

## Distinguishing features

The key points distinguishing applications based on Akka are:

- Asynchronous and non-blocking communication, distribution, and concurrency: Akka applications are event-based, asynchronous, and non-blocking: no mutable data are shared, and no synchronization primitives are used; Akka implements the actor model with support for streaming, Publish-Subscribe, HTTP, gRPC, and multiple other protocols (through the Alpakka module).
- Location transparency: The way Akka-based services/agents interact is the same whether they are on the same host or separate hosts (cores, nodes, data centers, or clouds), communicating directly or through routing facilities. This means that the topology of the application is not fixed but dynamic and may be altered at deployment time through a configuration mechanism, allowing a program to be scaled up (to make use of more powerful servers), out (to make use of more servers), and clustered, without code modifications.
- Self-healing through declarative failure management: Actors are arranged hierarchically in so-called ‘supervisor hierarchies’. Failures are treated as immutable facts, reified events, and sent asynchronously to the component’s supervisor, who can manage the failure in a safe and healthy context outside of the failed component (which, thanks to location transparency, can be on another node or even data center). In contrast to Erlang, Akka enforces parental supervision, which means that each actor is created and supervised by its parent actor.
- Durable replicated in-memory persistence: Akka services/agents are durable with their in-memory state acting as the source of truth and each state-changing event (immutable fact) is logged to disk in the order they arrive leveraging so-called event-sourcing. Replaying the event log allows them to gracefully recover from failure, sourcing replicas, and provides a built-in audit log (full history) of everything that has happened in the system.
- Multi-region/multi-cloud clustering: Akka services/agents are clustered automatically “from within”. Each service is its own fully replicated and sharded cluster of nodes that can span multiple data centers, regions, clouds, or span from the cloud to the edge.

The programming model for Akka consists of Akka SDK and Akka Libraries:

- Akka Libraries is an open-ended toolkit for building distributed systems. It has a modular structure, with a core module providing actors. Other modules are available to add features such as network distribution of actors, cluster support, Command and Event Sourcing, data distribution and management (through CRDTs and event logging), integration with various third-party systems through the Alpakka streaming integration module, and even support for other concurrency models such as asynchronous stream-processing and Futures.
- Akka SDK is a high-level and opinionated framework built on top of the Akka Libraries. It encodes the most common and useful patterns and best practices learned from the use of Akka Libraries through a set of discrete composable components (Entity, View, Endpoint, Workflow, Consumer, and Timer), allowing developers to build highly responsive, scalable, resilient, distributed agentic and services-based applications.

## Relation to other libraries

Other frameworks and toolkits have emerged to form an ecosystem around Akka:

- The Play framework for developing web applications offers integration with Akka
- Up until version 1.6, Apache Spark used Akka for communication between nodes
- The Socko Web Server library supports the implementation of REST APIs for Akka applications
- The *eventsourced* library provides event-driven architecture (see also domain-driven design) support for Akka actors
- The Gatling stress test tool for load-testing web servers is built upon Akka
- The Scalatra web framework offers integration with Akka.
- The Vaadin web app development framework can integrate with Akka
- The Apache Flink (platform for distributed stream and batch data processing) RPC system is built using Akka but isolated since v1.14.
- The Lagom framework for building reactive microservices is implemented on top of Akka.

There are more than 250 public projects registered on GitHub which use Akka.

## Publications about Akka

There are several books about Akka:

- Akka Essentials
- Akka Code Examples
- Akka Concurrency
- Akka in Action, Second Edition
- Akka in Action
- Effective Akka
- Composable Futures with Akka 2.0, Featuring Java, Scala and Akka Code Examples

Akka also features in:

- P. Haller's "Actors in Scala"
- N. Raychaudhuri's "Scala in Action"
- D. Wampler's "Functional Programming for Java Developers"
- A. Alexander's "Scala Cookbook"
- V. Subramaniam's "Programming Concurrency on the JVM"
- M. Bernhardt's "Reactive Web Applications"

Besides many web articles that describe the commercial use of Akka, there are also overview articles about it.
