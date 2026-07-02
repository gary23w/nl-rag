---
title: "NATS Messaging"
source: https://en.wikipedia.org/wiki/NATS_Messaging
domain: nats-messaging
license: CC-BY-SA-4.0
tags: nats messaging, publish subscribe pattern, message oriented middleware, lightweight broker, event driven architecture
fetched: 2026-07-02
---

# NATS Messaging

**NATS** ("Neural Autonomic Transport System") is an open-source messaging system developed under the stewardship of the Cloud Native Computing Foundation. The NATS server is written in the Go programming language. Client libraries to interface with the server are available for dozens of major programming languages. The core design principles of NATS are performance, scalability, and ease of use.

NATS was originally developed by Derek Collison as the messaging control plane for Cloud Foundry and was written in Ruby. NATS was later ported to Go.

The source code is released under the Apache 2.0 License. NATS consists of:

- The NATS Server - The core Publish-Subscribe Server for NATS.
- Client libraries for a variety of programming languages.
- A connector framework - a pluggable Java based framework to connect NATS and other services.

The NATS server is often referred to as either 'Core NATS' or NATS with 'JetStream'. 'Core NATS' is the set of core NATS functionalities and qualities of service. 'JetStream' is the (optionally enabled) built-in persistence layer that adds streaming, queues, at-least-once and exactly-once delivery guarantees, historical data replay, decoupled flow-control and key/value store functionalities to Core NATS. JetStream replaced the old STAN (NATS Streaming) approach.

## Example

Below is a sample connection string from a telnet connection to the demo.nats.io site:

```mw
Trying 107.170.221.32...
Connected to demo.nats.io.
Escape character is '^]'.
INFO {"server_id":"NDH3TUKI4Q5S72ESTECUI6AN7GWZT7VGLMQ6NJTIZTIPFK65OTRERVLZ","server_name":"nats-demo-us-tx","version":"2.12.8","proto":1,"git_commit":"e9559e9","go":"go1.25.9","host":"0.0.0.0","port":4222,"headers":true,"tls_available":true,"max_payload":1048576,"jetstream":true,"client_id":37220096,"client_ip":"2605:a601:a0f6:c100:84d:60c8:7e1f:37b7","nonce":"oiCSqsFWATMKZkc","api_lvl":3,"xkey":"XCCVI7W3IKXVZEI7JXNPM6OX76H2HXI4GGCOIBGCDQUAO6XEDGRERHHV"}
```
