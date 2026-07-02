---
title: "Channel Messaging API - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Channel_Messaging_API
domain: message-channel
license: CC-BY-SA-4.0
tags: message channel api, message port pair, channel messaging, transferable object handoff
fetched: 2026-07-02
---

# Channel Messaging API

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

- Learn more
- See full compatibility

**Note:** This feature is available in Web Workers.

The **Channel Messaging API** allows two separate scripts running in different browsing contexts attached to the same document (e.g., two IFrames, or the main document and an IFrame, two documents via a `SharedWorker`, or two workers) to communicate directly, passing messages between one another through two-way channels (or pipes) with a port at each end.

## Concepts and usage

A message channel is created using the `MessageChannel()` constructor. Once created, the two ports of the channel can be accessed through the `MessageChannel.port1` and `MessageChannel.port2` properties (which both return `MessagePort` objects.) The app that created the channel uses `port1`, and the app at the other end of the port uses `port2` — you send a message to `port2`, and transfer the port over to the other browsing context using `window.postMessage` along with two arguments (the message to send, and the object to transfer ownership of, in this case the port itself.)

When these transferable objects are transferred, they are no longer usable on the context they previously belonged to. A port, after it is sent, can no longer be used by the original context.

The other browsing context can listen for the message using `onmessage`, and grab the contents of the message using the event's `data` attribute. You could then respond by sending a message back to the original document using `MessagePort.postMessage`.

When you want to stop sending messages down the channel, you can invoke `MessagePort.close` to close the ports.

Find out more about how to use this API in Using channel messaging.

## Interfaces

**`MessageChannel`**

Creates a new message channel to send messages across.

**`MessagePort`**

Controls the ports on the message channel, allowing sending of messages from one port and listening out for them arriving at the other.

## Examples

- We have published a channel messaging basic demo on GitHub (run it live too), which shows a really simple single message transfer between a page and an embedded `<iframe>`.
- You can also see a multimessaging demo (run this live), which shows a slightly more complex setup that can send multiple messages between main page and IFrame.

## Specifications

| Specification |
|---|
| HTML # channel-messaging |

## Browser compatibility

### api.MessageChannel

### api.MessagePort
