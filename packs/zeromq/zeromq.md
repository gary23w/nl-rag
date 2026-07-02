---
title: "ZeroMQ"
source: https://en.wikipedia.org/wiki/ZeroMQ
domain: zeromq
license: CC-BY-SA-4.0
tags: zeromq library, message oriented middleware, asynchronous messaging, socket patterns, distributed messaging
fetched: 2026-07-02
---

# ZeroMQ

**ZeroMQ** (also spelled **ØMQ**, **0MQ** or **ZMQ**) is an asynchronous messaging library, aimed at use in distributed or concurrent applications. It provides a message queue, but unlike message-oriented middleware, a ZeroMQ system can run without a dedicated message broker; the zero in the name is for "zero broker". The library's API is designed to resemble Berkeley sockets.

ZeroMQ is developed by a large community of contributors, founded by iMatix, which holds the domain name and trademarks. There are third-party bindings for many popular programming languages.

## Technology

The ZeroMQ API provides *sockets* (a kind of generalization over the traditional IP and Unix domain sockets), each of which can represent a many-to-many connection between endpoints. Operating with a message-wise granularity, they require that a messaging pattern be used, and are particularly optimized for that kind of pattern.

The basic ZeroMQ patterns are:

**Request–reply**

Connects a set of clients to a set of services. This is a

remote procedure call

and task distribution pattern.

**Publish–subscribe**

Connects a set of publishers to a set of subscribers. This is a data distribution pattern.

**Push–pull (pipeline)**

Connects nodes in a fan-out / fan-in pattern that can have multiple steps, and loops. This is a

parallel

task distribution and collection pattern.

**Exclusive pair**

Connects two sockets in an exclusive pair. (This is an advanced low-level pattern for specific use cases.)

Each pattern defines a particular network topology. Request-reply defines a so-called "service bus", publish-subscribe defines a "data distribution tree", and push-pull defines "parallelised pipeline". All the patterns are deliberately designed in such a way as to be infinitely scalable and thus usable on Internet scale.

Any message through the socket is treated as an opaque blob of data. Delivery to a subscriber can be automatically filtered by the blob leading string. Available message transports include TCP, PGM (reliable multicast), inter-process communication (IPC) and inter-thread communication (ITC).

The ZeroMQ core library performs very well due to its internal threading model, and can outperform conventional TCP applications in terms of throughput by utilizing an automatic message batching technique.

ZeroMQ implements ZMTP, the ZeroMQ Message Transfer Protocol. ZMTP defines rules for backward interoperability, extensible security mechanisms, command and message framing, connection metadata, and other transport-level functionality. A growing number of projects implement ZMTP directly as an alternative to using the full ZeroMQ implementations.

## History

iMatix CEO Pieter Hintjens registered the zeromq.org domain in May 2007 and started the ZeroMQ project together with Martin Sustrik, who was its architect and lead developer until December 2011.

On March 30, 2010, Hintjens announced that iMatix (the original designer of Advanced Message Queuing Protocol) would leave the AMQP workgroup and did not plan to support AMQP/1.0 in favor of the significantly simpler and faster ZeroMQ.

In 2011, CERN was investigating ways to unify middleware solutions used to operate CERN accelerators. The CERN study compared two open source implementations of CORBA, Ice, Thrift, ZeroMQ, YAMI4, RTI, and Qpid (AMQP) and scored ZeroMQ highest, in part for its versatility, including its easy adaptability to the LynxOS.

At the start of 2012, two of the original developers forked ZeroMQ as Crossroads I/O. Martin Sustrik has started nanomsg, a rewrite of the ZeroMQ core library.

In August 2012, Dongmin Yu announced his pure Java conversion of ZeroMQ, JeroMQ. This has inspired further full-native ports of ZeroMQ, such as NetMQ for C# and zmq.rs for Rust.

In March 2013, Pieter Hintjens announced a new draft of the ZMTP wire-level protocol bringing extensible security mechanisms to ZeroMQ. Martin Hurton implemented the CurveZMQ authentication and encryption mechanism in the core library shortly afterwards.

In 2016, long-time ZeroMQ developer Garrett D'Amore forked Nanomsg to create project NNG (Nanomsg Next Generation).

## Development process

The ZeroMQ community mostly uses the Collective Code Construction Contract (C4) as a development contract. C4 is inspired by Wikipedia processes and GitHub's fork + pull request model. It focuses on making it simpler for new contributors to participate and reducing dependency on older contributors.
