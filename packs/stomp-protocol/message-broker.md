---
title: "Message broker"
source: https://en.wikipedia.org/wiki/Message_broker
domain: stomp-protocol
license: CC-BY-SA-4.0
tags: stomp protocol, streaming text oriented messaging protocol, text messaging protocol, simple broker protocol
fetched: 2026-07-02
---

# Message broker

A **message broker** (also known as an **integration broker** or **interface engine**) is an intermediary computer program module that translates a message from the formal messaging protocol of the sender to the formal messaging protocol of the receiver. Message brokers are elements in telecommunication or computer networks where software applications communicate by exchanging formally defined messages. Message brokers are a building block of message-oriented middleware (MOM) but are typically not a replacement for traditional middleware like MOM and remote procedure call (RPC).

## Overview

A message broker is an architectural pattern for message validation, transformation, and routing. It mediates communication among applications, minimizing the mutual awareness that applications should have of each other in order to be able to exchange messages, effectively implementing decoupling.

### Purpose

The primary purpose of a broker is to take incoming messages from applications and perform some action on them. Message brokers can decouple end-points, meet specific non-functional requirements, and facilitate reuse of intermediary functions. For example, a message broker may be used to manage a workload queue or message queue for multiple receivers, providing reliable storage, guaranteed message delivery and perhaps transaction management.

### Life cycle

The following represent other examples of actions that might be handled by the broker:

- Route messages to one or more destinations
- Transform messages to an alternative representation
- Perform message aggregation, decomposing messages into multiple messages and sending them to their destination, then recomposing the responses into one message to return to the user
- Interact with an external repository to augment a message or store it
- Invoke web services to retrieve data
- Respond to events or errors
- Provide content and topic-based message routing using the publish–subscribe pattern

Message brokers are generally based on one of two fundamental architectures: hub-and-spoke and message bus. In the first, a central server acts as the mechanism that provides integration services, whereas with the latter, the message broker is a communication backbone or distributed service that acts on the bus. Additionally, a more scalable multi-hub approach can be used to integrate multiple brokers.

## Real-time semantics

Message brokers that are purpose built to achieve time-bounded communications with end-to-end predictability allow for the development of real-time systems that require execution predictability. Frequently systems with real-time requirements involve interaction with the real world (robotics, vehicle automation, software-defined radio, et al.)

The Object Management Group Real-time CORBA specification provides a theoretical foundation for predictable communications technologies by levying the following requirements:

> For the purposes of this specification, "end-to-end predictability" of timeliness in a fixed priority CORBA system is defined to mean:
> 
> - respecting thread priorities between client and server for resolving resource contention during the processing of CORBA invocations;
> - bounding the duration of thread priority inversions during end-to-end processing;
> - bounding the latencies of operation invocations.

## List of message broker software

- Amazon Web Services (AWS) Amazon MQ
- Amazon Web Services (AWS) Kinesis
- **Apache**
  - Apache ActiveMQ
  - Apache Artemis
  - Apache Camel
  - Apache Kafka
  - Apache Qpid
  - Apache Thrift
  - Apache Pulsar
- Cloverleaf (Enovation Lifeline - NL)
- Comverse Message Broker (Comverse Technology)
- Coreflux Coreflux MQTT Broker
- Eclipse Mosquitto MQTT Broker (Eclipse Foundation)
- EMQX EMQX MQTT Broker
- Enduro/X Transactional Message Queue (TMQ)
- Financial Fusion Message Broker (Sybase)
- Fuse Message Broker (enterprise ActiveMQ)
- Gearman
- Google Cloud Pub/Sub (Google)
- HiveMQ HiveMQ MQTT Broker
- HornetQ (Red Hat) (Now part of Apache Artemis)
- IBM App Connect
- IBM MQ
- JBoss Messaging (JBoss)
- JORAM
- LavinMQ written in Crystal
- Microsoft Azure Service Bus (Microsoft)
- Microsoft BizTalk Server (Microsoft)
- MigratoryData (a publish/subscribe WebSockets message broker written to address the C10M problem )
- NATS (MIT License, written in Go)
- NanoMQ MQTT Broker for IoT Edge
- Open Message Queue
- Oracle Message Broker (Oracle Corporation)
- ORBexpress (OIS)
  - ORBexpress written in Ada
  - ORBexpress written in C#
  - ORBexpress written in C++
  - ORBexpress written in Java
- RabbitMQ (Mozilla Public License, written in Erlang)
- Redpanda (implement Apache Kafka API, written in C++)
- Redis An open source, in-memory data structure store, used as a database, cache and message broker
- SAP PI (SAP AG)
- SMC SMC Platform
- Solace PubSub+
- Spread Toolkit
- Tarantool, a NoSQL database, with a set of stored procedures for message queues
- TIBCO Enterprise Message Service
- WSO2 Message Broker
- ZeroMQ
