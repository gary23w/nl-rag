---
title: "Streaming Text Oriented Messaging Protocol"
source: https://en.wikipedia.org/wiki/Streaming_Text_Oriented_Messaging_Protocol
domain: stomp-protocol
license: CC-BY-SA-4.0
tags: stomp protocol, streaming text oriented messaging protocol, text messaging protocol, simple broker protocol
fetched: 2026-07-02
---

# Streaming Text Oriented Messaging Protocol

**Simple (or Streaming) Text Oriented Message Protocol** (**STOMP**), formerly known as TTMP, is a simple text-based protocol, designed for working with message-oriented middleware (MOM). It provides an interoperable wire format that allows STOMP clients to talk with any message broker supporting the protocol.

## Overview

The protocol is broadly similar to HTTP, and works over TCP using the following commands:

- CONNECT
- SEND
- SUBSCRIBE
- UNSUBSCRIBE
- BEGIN
- COMMIT
- ABORT
- ACK
- NACK
- DISCONNECT

Communication between client and server is through a "frame" consisting of a number of lines. The first line contains the command, followed by headers in the form <key>: <value> (one per line), followed by a blank line and then the body content, ending in a null character. Communication between server and client is through a MESSAGE, RECEIPT or ERROR frame with a similar format of headers and body content.

## Example

```
SEND
destination:/queue/a
content-type:text/plain

hello queue a
^@
```

Here ^@ is the caret notation for the null character. Lines are terminated with LF (\n, ^J, 0x10).

## Implementations

Some message-oriented middleware products support STOMP, such as:

- Apache ActiveMQ
- Fuse Message Broker
- HornetQ
- Open Message Queue (OpenMQ)
- RabbitMQ
- syslog-ng
- Spring Framework
