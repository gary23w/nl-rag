---
title: "Wire protocol"
source: https://en.wikipedia.org/wiki/Wire_protocol
domain: apache-thrift
license: CC-BY-SA-4.0
tags: apache thrift, thrift idl, cross-language rpc, interface definition language
fetched: 2026-07-02
---

# Wire protocol

In computer networking, a **wire protocol** refers to a way of getting data from point to point: A wire protocol is needed if more than one application has to interoperate. It generally refers to communication protocols higher than the physical layer. In contrast to transport protocols at the transport level (like TCP or UDP), the term *wire protocol* is used to describe a common way to exchange information at the application level. It refers to an application layer protocol and defines all the required attributes for the data exchange, like data types (units of data, message formats, etc.), communication endpoints and capabilities (such as delivery guarantees, direction of communication, etc.). Usually, the data is represented at the application level as a common infoset (e.g. XML, JSON, YAML) and requires a mechanism of data binding (using e.g. a common encoding scheme like XSD).

The wire protocol may be either text-based or a binary protocol. Although an important architectural decision, this is a separate matter from the distinction between wire protocols and programmatic APIs.

In electronics, a wire protocol is the mechanism used to transmit data from one point to another.

## Functionality

A wire protocol provides the means for the interoperation of one or more applications in a network. They often refer to distributed object protocols, or they use applications that were designed to work together. As the name suggests, these distributed object protocols run in different processes in one or several computers that are connected over a network.

## Types

Wire protocols provide the means for a program running under one operating system to communicate with a program running under some other operating system over a network such as an organization's intranet or the Internet. The protocol thus interconnects multiple platforms. Some wire protocols are language-independent, allowing the communication of programs written in different programming languages.

Examples of wire protocols include:

- IIOP for CORBA
- RTPS for DDS
- Java Debug Wire Protocol (JDWP) for Java debugging
- JRMP for RMI
- SOAP for Web services
- AMQP for message-oriented middleware
- PostgreSQL wire protocol
- XML-RPC is a remote procedure call (RPC) protocol which uses XML to encode its calls and HTTP as a transport mechanism.
- JSON-RPC is similar to XML-RPC.
