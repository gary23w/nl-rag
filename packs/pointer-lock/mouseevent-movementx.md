---
title: "MouseEvent: movementX property - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/movementX
domain: pointer-lock
license: CC-BY-SA-4.0
tags: pointer lock api, mouse capture relative motion, raw mouse movement, pointer lock change event
fetched: 2026-07-02
---

# MouseEvent: movementX property

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- Learn more
- See full compatibility

The **`movementX`** read-only property of the `MouseEvent` interface provides the difference in the X coordinate of the mouse (or pointer) between the given move event and the previous move event of the same type.

In other words, the value of the property is computed like this: `currentEvent.movementX = currentEvent.screenX - previousEvent.screenX`. The value is zero for all events other than `mousemove`, `pointermove`, and `pointerrawupdate`.

**Warning:** Browsers use different units for `movementX` and `screenX` than what the specification defines. Depending on the browser and operating system, the `movementX` units may be a physical pixel, a logical pixel, or a CSS pixel. You may want to avoid the movement properties, and instead calculate the delta between the current client values (`screenX`, `screenY`) and the previous client values.

## Value

A number. Always zero on any `MouseEvent` other than `mousemove`, and any `PointerEvent` other than `pointermove` or `pointerrawupdate`.

## Examples

### Log mouse movement for `mousemove` events

This example logs the amount of mouse movement using `movementX` and `movementY`.

#### HTML

```html
<p id="log">Move your mouse around.</p>
```

#### JavaScript

```js
const log = document.getElementById("log");

function logMovement(event) {
  log.insertAdjacentHTML(
    "afterbegin",
    `movement: ${event.movementX}, ${event.movementY}<br>`,
  );
  while (log.childNodes.length > 128) log.lastChild.remove();
}

document.addEventListener("mousemove", logMovement);
```

#### Result

## Specifications

| Specification |
|---|
| Pointer Lock 2.0 # dom-mouseevent-movementx |

## Browser compatibility
