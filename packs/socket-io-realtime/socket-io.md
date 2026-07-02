---
title: "Socket.IO"
source: https://en.wikipedia.org/wiki/Socket.IO
domain: socket-io-realtime
license: CC-BY-SA-4.0
tags: socket.io realtime, bidirectional event messaging, realtime websocket rooms, event emitter transport
fetched: 2026-07-02
---

# Socket.IO

**Socket.IO** is an event-driven library for real-time web applications. It enables real-time, bi-directional communication between web clients and servers. It consists of two components: a client, and a server. Both components have a nearly identical API.

Socket.IO is also a protocol, where different complying implementations of the protocol can communicate with each other. The main implementation consists of two parts: a client that runs in the browser and a server for Node.js. Apart from the main implementation, there are multiple implementations, for example, the official Deno (JavaScript), C++, Java, Python, and Swift servers.

Socket.IO primarily uses the WebSocket protocol with polling as a fallback option, while providing the same interface. Although it can be used simply as a wrapper for WebSockets, it provides many additional features such as heartbeats and timeouts.

It can be installed with the npm (Node Package Manager).
