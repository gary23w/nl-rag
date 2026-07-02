---
title: "MessagePort - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/MessagePort
domain: message-channel
license: CC-BY-SA-4.0
tags: message channel api, message port pair, channel messaging, transferable object handoff
fetched: 2026-07-02
---

# MessagePort

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

- Learn more
- See full compatibility

**Note:** This feature is available in Web Workers.

The **`MessagePort`** interface of the Channel Messaging API represents one of the two ports of a `MessageChannel`, allowing messages to be sent from one port and listening out for them arriving at the other.

`MessagePort` is a transferable object.

## Instance methods

*Inherits methods from its parent, `EventTarget`*.

**`postMessage()`**

Sends a message from the port, and optionally, transfers ownership of objects to other browsing contexts.

**`start()`**

Starts the sending of messages queued on the port (only needed when using `EventTarget.addEventListener`; it is implied when using `onmessage`).

**`close()`**

Disconnects the port, so it is no longer active.

## Events

*Inherits events from its parent, `EventTarget`*.

**`message`**

Fired when a `MessagePort` object receives a message.

**`messageerror`**

Fired when a `MessagePort` object receives a message that can't be deserialized.

## Example

In the following example, you can see a new channel being created using the `MessageChannel()` constructor.

When the IFrame has loaded, we register an `onmessage` handler for `MessageChannel.port1` and transfer `MessageChannel.port2` to the IFrame using the `window.postMessage` method along with a message.

When a message is received back from the IFrame, the `onMessage` function outputs the message to a paragraph.

```js
const channel = new MessageChannel();
const output = document.querySelector(".output");
const iframe = document.querySelector("iframe");

// Wait for the iframe to load
iframe.addEventListener("load", onLoad);

function onLoad() {
  // Listen for messages on port1
  channel.port1.onmessage = onMessage;

  // Transfer port2 to the iframe
  iframe.contentWindow.postMessage("Hello from the main page!", "*", [
    channel.port2,
  ]);
}

// Handle messages received on port1
function onMessage(e) {
  output.innerHTML = e.data;
}
```

For a full working example, see our channel messaging basic demo on GitHub (run it live too).

## Specifications

| Specification |
|---|
| HTML # message-ports |

## Browser compatibility
