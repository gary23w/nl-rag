---
title: "Window: gamepadconnected event - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Window/gamepadconnected_event
domain: gamepad-api
license: CC-BY-SA-4.0
tags: gamepad api, game controller input, gamepad button axes, gamepad connected event
fetched: 2026-07-02
---

# Window: gamepadconnected event

Baseline

2025

Newly available

Since December 2025, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

- Learn more
- See full compatibility

The `gamepadconnected` event is fired when the browser detects that a gamepad has been connected or the first time a button/axis of the gamepad is used.

The event will not fire if disallowed by the document's `gamepad` Permissions Policy.

This event is not cancelable and does not bubble.

## Syntax

Use the event name in methods like `addEventListener()`, or set an event handler property.

```js
addEventListener("gamepadconnected", (event) => { })

ongamepadconnected = (event) => { }
```

## Examples

To be informed when a gamepad is connected, you can add a handler to the window using `addEventListener()`, like this:

```js
window.addEventListener("gamepadconnected", (event) => {
  // All buttons and axes values can be accessed through
  const gamepad = event.gamepad;
});
```

Alternatively, you can use the `window.ongamepadconnected` event handler property to establish a handler for the `gamepadconnected` event:

```js
window.ongamepadconnected = (event) => {
  // All buttons and axes values can be accessed through
  const gamepad = event.gamepad;
};
```

## Specifications

| Specification |
|---|
| Gamepad # event-gamepadconnected |

## Browser compatibility
