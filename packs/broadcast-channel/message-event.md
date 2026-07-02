---
title: "BroadcastChannel: message event - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/BroadcastChannel/message_event
domain: broadcast-channel
license: CC-BY-SA-4.0
tags: broadcast channel api, same-origin messaging bus, cross-tab communication, message event dispatch
fetched: 2026-07-02
---

# BroadcastChannel: message event

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2022.

- Learn more
- See full compatibility

**Note:** This feature is available in Web Workers.

The **`message`** event of the `BroadcastChannel` interface fires when a message arrives on that channel.

## Syntax

Use the event name in methods like `addEventListener()`, or set an event handler property.

```js
addEventListener("message", (event) => { })

onmessage = (event) => { }
```

## Event type

A `MessageEvent`. Inherits from `Event`.

## Event properties

*In addition to the properties listed below, properties from the parent interface, `Event`, are available.*

**`data` Read only**

The data sent by the message emitter.

**`origin` Read only**

A string representing the origin of the message emitter.

**`lastEventId` Read only**

A string representing a unique ID for the event.

**`source` Read only**

A *message event source*, which is either a WindowProxy, a `MessagePort`, or a `ServiceWorker` object representing the message emitter.

**`ports` Read only**

An array of `MessagePort` objects representing the ports associated with the channel the message is being sent through (where appropriate, e.g., in channel messaging or when sending a message to a shared worker).

## Examples

In this example there's a "sender" `<iframe>` that broadcasts the contents of a `<textarea>` when the user clicks a button. There are two "receiver" iframes that listen to the broadcast message and write the result into a `<div>` element.

### Sender

```html
<h1>Sender</h1>
<label for="message">Type a message to broadcast:</label><br />
<textarea id="message" name="message" rows="1" cols="40">Hello</textarea>
<button id="broadcast-message" type="button">Broadcast message</button>
```

```css
body {
  border: 1px solid black;
  padding: 0.5rem;
  height: 150px;
  font-family: "Fira Sans", sans-serif;
}

h1 {
  font:
    1.6em "Fira Sans",
    sans-serif;
  margin-bottom: 1rem;
}

textarea {
  padding: 0.2rem;
}

label,
br {
  margin: 0.5rem 0;
}

button {
  vertical-align: top;
  height: 1.5rem;
}
```

```js
const channel = new BroadcastChannel("example-channel");
const messageControl = document.querySelector("#message");
const broadcastMessageButton = document.querySelector("#broadcast-message");

broadcastMessageButton.addEventListener("click", () => {
  channel.postMessage(messageControl.value);
});
```

### Receiver 1

```html
<h1>Receiver 1</h1>
<div id="received"></div>
```

```css
body {
  border: 1px solid black;
  padding: 0.5rem;
  height: 100px;
  font-family: "Fira Sans", sans-serif;
}

h1 {
  font:
    1.6em "Fira Sans",
    sans-serif;
  margin-bottom: 1rem;
}
```

```js
const channel = new BroadcastChannel("example-channel");
channel.addEventListener("message", (event) => {
  received.textContent = event.data;
});
```

### Receiver 2

```html
<h1>Receiver 2</h1>
<div id="received"></div>
```

```css
body {
  border: 1px solid black;
  padding: 0.5rem;
  height: 100px;
  font-family: "Fira Sans", sans-serif;
}

h1 {
  font:
    1.6em "Fira Sans",
    sans-serif;
  margin-bottom: 1rem;
}
```

```js
const channel = new BroadcastChannel("example-channel");
channel.addEventListener("message", (event) => {
  received.textContent = event.data;
});
```

### Result

## Specifications

| Specification |
|---|
| HTML # event-message |
| HTML # handler-broadcastchannel-onmessage |

## Browser compatibility
