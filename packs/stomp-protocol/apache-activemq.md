---
title: "Apache ActiveMQ"
source: https://en.wikipedia.org/wiki/Apache_ActiveMQ
domain: stomp-protocol
license: CC-BY-SA-4.0
tags: stomp protocol, streaming text oriented messaging protocol, text messaging protocol, simple broker protocol
fetched: 2026-07-02
---

# Apache ActiveMQ

**Apache ActiveMQ** is an open source message broker written in Java together with a full Java Message Service (JMS) client. It provides "Enterprise Features" which in this case means fostering the communication from more than one client or server. Supported clients include Java via JMS 1.1 as well as several other "cross language" clients. The communication is managed with features such as computer clustering and ability to use any database as a JMS persistence provider besides virtual memory, cache, and journal persistency.

There's another broker under the ActiveMQ umbrella code-named *Artemis*.

## History

The ActiveMQ project was originally created by its founders from LogicBlaze in 2004, as an open source message broker, hosted by CodeHaus. The code and ActiveMQ trademark were donated to the Apache Software Foundation in 2007, where the founders continued to develop the codebase with the extended Apache community.

## Artemis

Artemis is another broker under the ActiveMQ umbrella based on the HornetQ code-base which was donated from the JBoss community to the Apache ActiveMQ community in 2015. Artemis is the "next generation" broker from ActiveMQ. Artemis is a multi-protocol, embeddable, high performance, clustered, asynchronous messaging system.

## Technical features

ActiveMQ Classic uses several modes for high availability, including both file-system and database row-level locking mechanisms, sharing of the persistence store via a shared filesystem, or true replication using Apache ZooKeeper. ActiveMQ supports a horizontal scaling mechanism called a Network of Brokers out of the box. ActiveMQ supports a number of transport protocols, including OpenWire, STOMP, MQTT, AMQP, REST, and WebSockets.

## Usage

ActiveMQ is used in enterprise service bus implementations such as Apache ServiceMix and Mule. Other projects using ActiveMQ include Apache Camel and Apache CXF in SOA infrastructure projects.

## Benchmark

Coinciding with the release of Apache ActiveMQ 5.3, the world's first results for the SPECjms2007 industry standard benchmark were announced. Four results were submitted to the SPEC and accepted for publication. The results cover different topologies to analyze the scalability of Apache ActiveMQ in two dimensions.

## Commercial support

Apache is used in enterprise software and offers limited ActiveMQ support on a voluntary basis. Users that need more extensive support may need to consult commercial companies specializing in ActiveMQ.
