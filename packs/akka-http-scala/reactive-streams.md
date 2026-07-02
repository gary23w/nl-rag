---
title: "Reactive Streams"
source: https://en.wikipedia.org/wiki/Reactive_Streams
domain: akka-http-scala
license: CC-BY-SA-4.0
tags: akka http scala, akka actor streams, scala reactive http, akka routing directives
fetched: 2026-07-02
---

# Reactive Streams

**Reactive Streams** is an initiative to provide a standard for asynchronous stream processing with non-blocking back pressure.

## Origin

Reactive Streams started as an initiative in late 2013 between engineers at Netflix, Pivotal and Lightbend. Some of the earliest discussions began in 2013 between the Play and Akka teams at Lightbend. Lightbend is one of the main contributors of Reactive Streams. Other contributors include Red Hat, Oracle, Twitter and spray.io.

## Goals

The main goal of Reactive Streams is to govern the exchange of stream data across an asynchronous boundary – like passing elements on to another thread or thread-pool – while ensuring that the receiving side is not forced to buffer arbitrary amounts of data. In other words, back pressure is an integral part of this model in order to allow the queues which mediate between threads to be bounded.

The intention of the specification is to allow the creation of many conforming implementations, which by virtue of abiding by the rules will be able to interoperate smoothly, preserving the mentioned benefits and characteristics across the whole processing graph of a stream application. A freely-available Technology Compatibility Kit was developed alongside the specification that allows implementors of the specification to verify if they covered all rules and requirements, including checks for potential race conditions.

The scope of Reactive Streams is a minimal set of interfaces, methods and protocols that describe the necessary operations and entities to achieve the asynchronous streams of data with non-blocking back pressure. End-user DSLs or protocol binding APIs have purposefully been left out of the scope to encourage and enable different implementations that potentially use different programming languages to stay as true as possible to the idioms of their platform.

## Inclusion in Java standard

The specification developed with the intent of future inclusion in the official Java standard library, if proven successful and adopted by enough libraries and vendors.

Reactive Streams were proposed to become part of Java 9 by Doug Lea, leader of JSR 166 as a new Flow class that would include the interfaces currently provided by Reactive Streams. After a successful 1.0 release of Reactive Streams and growing adoption, the proposal was accepted and Reactive Streams was included in JDK9 via the JEP-266.

## Adoption

On April 30, 2015 version 1.0.0 of Reactive Streams for the JVM was released, including Java API, a textual specification, a TCK and implementation examples. It comes with a multitude of compliant implementations verified by the TCK for 1.0.0, listed in alphabetical order:

- Akka Streams
- MongoDB
- Ratpack
- Reactive Rabbit – driver for RabbitMQ/AMQP
- Spring and Pivotal Project Reactor
- Netflix RxJava
- Slick 3.0
- Vert.x 3.0
- Mutiny
- Helidon

Other implementations include Cassandra, Elasticsearch, Apache Kafka, Parallel Universe Quasar, Play Framework, Armeria.

Spring 5 is announced to be built upon Reactive Streams compatible Reactor Core.

Amazon announced that its Amazon Web Services SDK would support Reactive Streams to provide streaming capabilities in its client libraries in version 2.0.

Reactive Streams 1.0.1 is released on August 9, 2017, including various improvements in specification preciseness, TCK improvements and other clarifications. The specification as well as interfaces remained fully backwards compatible with the 1.0.0 version, however aimed to streamline the adoption for future implementors as well as align with some additional requirements set by the OpenJDK.

## Ports and influences

- A direct port of the specification, interfaces and TCK was made available under the same working group for the .NET platform.
- When the Elixir language introduced its streaming API called GenStage, the authors extended a thanks "[to] akka-streams and reactive-streams projects which provided us guidance in implementing the demand-driven exchange between stages".
