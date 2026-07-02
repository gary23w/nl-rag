---
title: "Navigator: getGamepads() method - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Navigator/getGamepads
domain: gamepad-api
license: CC-BY-SA-4.0
tags: gamepad api, game controller input, gamepad button axes, gamepad connected event
fetched: 2026-07-02
---

# Navigator: getGamepads() method

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2017.

- Learn more
- See full compatibility

The **`Navigator.getGamepads()`** method returns an array of `Gamepad` objects, one for each gamepad connected to the device.

Elements in the array may be `null` if a gamepad disconnects during a session, so that the remaining gamepads retain the same index.

## Syntax

```js
getGamepads()
```

### Parameters

None.

### Return value

An `Array` of `Gamepad` objects, eventually empty.

### Exceptions

**`SecurityError` `DOMException`**

Use of this feature was blocked by a Permissions Policy.

## Examples

```js
window.addEventListener("gamepadconnected", (e) => {
  const gp = navigator.getGamepads()[e.gamepad.index];
  console.log(
    `Gamepad connected at index ${gp.index}: ${gp.id} with ${gp.buttons.length} buttons, ${gp.axes.length} axes.`,
  );
});
```

## Specifications

| Specification |
|---|
| Gamepad # dom-navigator-getgamepads |

## Browser compatibility
