---
title: "Stateless protocol"
source: https://en.wikipedia.org/wiki/Stateless_protocol
domain: session-management
license: CC-BY-SA-4.0
tags: session management, http session, session identifier, session cookie
fetched: 2026-07-02
---

# Stateless protocol

A **stateless protocol** is a communication protocol in which the receiver does not retain session state from previous requests. The sender transfers relevant session state to the receiver in such a way that every request can be understood in isolation, without reference to session state from previous requests.

In contrast, a **stateful protocol** is a communication protocol in which the receiver may retain session state from previous requests.

In computer networks, examples of stateless protocols include the Internet Protocol (IP), which is the foundation for the Internet, and the Hypertext Transfer Protocol (HTTP), which is the foundation of the World Wide Web. Examples of stateful protocols include the Transmission Control Protocol (TCP) and the File Transfer Protocol (FTP).

Stateless protocols have superior visibility, reliability, and scalability properties. Visibility is improved because a monitoring system does not have to look beyond a single request in order to determine its full nature. Reliability is improved because it eases the task of recovering from failures such as packet loss. Scalability is improved because not having to store session state between requests allows the server to quickly free resources and further simplifies implementation. The disadvantage of stateless protocols is that they may decrease network performance by increasing the repetitive data sent in a series of requests, since that data is not retained or reused at the receiver.

## Examples

An HTTP server can understand each request in isolation.

Contrast this with a traditional FTP server that conducts an interactive session with the user. During the session, a user is provided a means to be authenticated and set various variables (working directory, transfer mode), all stored on the server as part of the session state.

## Stacking of stateless and stateful protocol layers

There can be complex interactions between stateful and stateless protocols among different protocol layers. For example, HTTP, a stateless protocol, is layered on top of TCP, a stateful protocol, which is layered on top of IP, another stateless protocol, which is routed on a network that employs BGP, another stateful protocol, to direct the IP packets riding on the network.

This stacking of layers continues even above HTTP. As a workaround for the lack of a retained session state, HTTP servers implement various session management methods, typically utilizing a session identifier in an HTTP cookie referencing a session state stored on the server, effectively creating a stateful protocol on top of HTTP.
