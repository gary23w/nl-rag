---
title: "BroadcastChannel - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/BroadcastChannel
domain: broadcast-channel
license: CC-BY-SA-4.0
tags: broadcast channel api, same-origin messaging bus, cross-tab communication, message event dispatch
fetched: 2026-07-02
---

# BroadcastChannel

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2022.

- Learn more
- See full compatibility

**Note:** This feature is available in Web Workers.

The **`BroadcastChannel`** interface represents a named channel that any browsing context of a given origin can subscribe to. It allows communication between different documents (in different windows, tabs, frames or iframes) of the same origin. Messages are broadcasted via a `message` event fired at all `BroadcastChannel` objects listening to the channel, except the object that sent the message.

## Constructor

**`BroadcastChannel()`**

Creates an object linking to the named channel.

## Instance properties

*This interface also inherits properties from its parent, `EventTarget`.*

**`BroadcastChannel.name` Read only**

Returns a string, the name of the channel.

## Instance methods

*This interface also inherits methods from its parent, `EventTarget`.*

**`BroadcastChannel.postMessage()`**

Sends the message, of any type of object, to each `BroadcastChannel` object listening to the same channel.

**`BroadcastChannel.close()`**

Closes the channel object, indicating it won't get any new messages, and allowing it to be, eventually, garbage collected.

## Events

*This interface also inherits events from its parent, `EventTarget`.*

**`message`**

Fired when a message arrives on the channel. Also available via the `onmessage` property.

**`messageerror`**

Fired when a message arrives that can't be deserialized. Also available via the `onmessageerror` property.

## Specifications

| Specification |
|---|
| HTML # broadcasting-to-other-browsing-contexts |

## Browser compatibility
