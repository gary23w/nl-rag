---
title: "CloseEvent - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/CloseEvent
domain: ws-websocket
license: CC-BY-SA-4.0
tags: ws websocket, node websocket server, websocket protocol library, duplex socket connection
fetched: 2026-07-02
---

# CloseEvent

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

- Learn more
- See full compatibility

**Note:** This feature is available in Web Workers.

A `CloseEvent` is sent to clients using WebSockets when the connection is closed. This is delivered to the listener indicated by the `WebSocket` object's `onclose` attribute.

## Constructor

**`CloseEvent()`**

Creates a new `CloseEvent`.

## Instance properties

*This interface also inherits properties from its parent, `Event`.*

**`CloseEvent.code` Read only**

Returns an `unsigned short` containing the close code.

**`CloseEvent.reason` Read only**

Returns a string indicating the reason the server closed the connection. This is specific to the particular server and sub-protocol.

**`CloseEvent.wasClean` Read only**

Returns a boolean value that Indicates whether or not the connection was cleanly closed.

## Instance methods

*This interface also inherits methods from its parent, `Event`.*

## Specifications

| Specification |
|---|
| WebSockets # the-closeevent-interface |

## Browser compatibility
