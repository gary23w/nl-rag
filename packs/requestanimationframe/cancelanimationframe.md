---
title: "Window: cancelAnimationFrame() method - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Window/cancelAnimationFrame
domain: requestanimationframe
license: CC-BY-SA-4.0
tags: request animation frame, frame-synced callback, smooth animation loop, repaint scheduling browser
fetched: 2026-07-02
---

# Window: cancelAnimationFrame() method

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

- Learn more
- See full compatibility

The **`window.cancelAnimationFrame()`** method cancels an animation frame request previously scheduled through a call to `window.requestAnimationFrame()`.

## Syntax

```js
cancelAnimationFrame(requestID)
```

### Parameters

**`requestID`**

The ID value returned by the call to `window.requestAnimationFrame()` that requested the callback.

### Return value

None (`undefined`).

## Examples

```js
const start = document.timeline.currentTime;

let myReq;

function step(timestamp) {
  const progress = timestamp - start;
  d.style.left = `${Math.min(progress / 10, 200)}px`;
  if (progress < 2000) {
    // it's important to update the requestId each time you're calling requestAnimationFrame
    myReq = requestAnimationFrame(step);
  }
}
myReq = requestAnimationFrame(step);
// the cancellation uses the last requestId
cancelAnimationFrame(myReq);
```

## Specifications

| Specification |
|---|
| HTML # animationframeprovider-cancelanimationframe |

## Browser compatibility
