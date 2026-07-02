---
title: "BroadcastChannel: postMessage() method - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/BroadcastChannel/postMessage
domain: broadcast-channel
license: CC-BY-SA-4.0
tags: broadcast channel api, same-origin messaging bus, cross-tab communication, message event dispatch
fetched: 2026-07-02
---

# BroadcastChannel: postMessage() method

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2022.

- Learn more
- See full compatibility

**Note:** This feature is available in Web Workers.

The **`postMessage()`** method of the `BroadcastChannel` interface sends a message, which can be of any kind of `Object`, to each listener in any browsing context with the same origin. The message is transmitted as a `message` event targeted at each `BroadcastChannel` bound to the channel.

## Syntax

```js
postMessage(message)
```

### Parameters

**`message`**

Data to be sent to the other window. The data is serialized using the structured clone algorithm. This means you can pass a broad variety of data objects safely to the destination window without having to serialize them yourself.

**Note:** Execution contexts that can message each other may not be in the same agent cluster, and therefore cannot share memory. `SharedArrayBuffer` objects, or buffer views backed by one, cannot be posted across agent clusters. Trying to do so will generate a `messageerror` event containing a `DataCloneError` `DOMException` on the receiving end.

### Return value

None.

### Exceptions

**`InvalidStateError` `DOMException`**

Thrown if the `BroadcastChannel` has already been closed.

**`DataCloneError` `DOMException`**

Thrown if any part of the input data is not serializable.

## Specifications

| Specification |
|---|
| HTML # dom-broadcastchannel-postmessage-dev |

## Browser compatibility
