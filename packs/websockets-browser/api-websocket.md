---
title: "WebSocket - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/WebSocket
domain: websockets-browser
license: CC-BY-SA-2.5
tags: websocket, websocket client, full-duplex browser, realtime messaging, server-sent events
fetched: 2026-07-02
---

# WebSocket

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

**Note:** This feature is available in Web Workers.

The `WebSocket` object provides the API for creating and managing a WebSocket connection to a server, as well as for sending and receiving data on the connection.

To construct a `WebSocket`, use the `WebSocket()` constructor.

**Note:** The `WebSocket` API has no way to apply backpressure, therefore when messages arrive faster than the application can process them, the application will either fill up the device's memory by buffering those messages, become unresponsive due to 100% CPU usage, or both. For an alternative that provides backpressure automatically, see `WebSocketStream`.

## Constructor

**`WebSocket()`**

Returns a newly created `WebSocket` object.

## Instance properties

**`WebSocket.binaryType`**

The binary data type used by the connection.

**`WebSocket.bufferedAmount` Read only**

The number of bytes of queued data.

**`WebSocket.extensions` Read only**

The extensions selected by the server.

**`WebSocket.protocol` Read only**

The sub-protocol selected by the server.

**`WebSocket.readyState` Read only**

The current state of the connection.

**`WebSocket.url` Read only**

The absolute URL of the WebSocket.

## Instance methods

**`WebSocket.close()`**

Closes the connection.

**`WebSocket.send()`**

Enqueues data to be transmitted.

## Events

Listen to these events using `addEventListener()` or by assigning an event listener to the `oneventname` property of this interface.

**`close`**

Fired when a connection with a `WebSocket` is closed. Also available via the `onclose` property

**`error`**

Fired when a connection with a `WebSocket` has been closed because of an error, such as when some data couldn't be sent. Also available via the `onerror` property.

**`message`**

Fired when data is received through a `WebSocket`. Also available via the `onmessage` property.

**`open`**

Fired when a connection with a `WebSocket` is opened. Also available via the `onopen` property.

## Examples

```js
// Create WebSocket connection.
const socket = new WebSocket("ws://localhost:8080");

// Connection opened
socket.addEventListener("open", (event) => {
  socket.send("Hello Server!");
});

// Listen for messages
socket.addEventListener("message", (event) => {
  console.log("Message from server ", event.data);
});
```

## Specifications

| Specification |
|---|
| WebSockets # the-websocket-interface |

## Browser compatibility
