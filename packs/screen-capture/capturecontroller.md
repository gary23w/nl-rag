---
title: "CaptureController - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/CaptureController
domain: screen-capture
license: CC-BY-SA-4.0
tags: screen capture api, display media stream, get display media, screen sharing surface
fetched: 2026-07-02
---

# CaptureController

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

**Experimental:** **This is an experimental technology** Check the Browser compatibility table carefully before using this in production.

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The **`CaptureController`** interface provides methods that can be used to further manipulate a captured display surface (captured via `MediaDevices.getDisplayMedia()`)

A `CaptureController` object is associated with a captured display surface by passing it into a `getDisplayMedia()` call as the value of the options object's `controller` property.

## Constructor

**`CaptureController()`**

Creates a new `CaptureController` object instance.

## Instance properties

**`zoomLevel`**

The captured display surface's current zoom level.

## Instance methods

**`decreaseZoomLevel()`**

Decreases the captured display surface's zoom level by one increment.

**`forwardWheel()`**

Starts forwarding `wheel` events fired on the referenced element to the viewport of an associated captured display surface.

**`getSupportedZoomLevels()`**

Returns the different zoom levels supported by the captured display surface.

**`increaseZoomLevel()`**

Increases the captured display surface's zoom level by one increment.

**`resetZoomLevel()`**

Resets the captured display surface's zoom to its initial level, which is `100`.

**`setFocusBehavior()`**

Controls whether the captured tab or window will be focused or whether the focus will remain with the tab containing the capturing app.

## Events

**`zoomlevelchange`**

Fires when the captured display surface's zoom level changes.

## Examples

```js
// Create a new CaptureController instance
const controller = new CaptureController();

// Prompt the user to share a tab, window, or screen.
const stream = await navigator.mediaDevices.getDisplayMedia({ controller });

// Query the displaySurface value of the captured video track
const [track] = stream.getVideoTracks();
const displaySurface = track.getSettings().displaySurface;

if (displaySurface === "browser") {
  // Focus the captured tab.
  controller.setFocusBehavior("focus-captured-surface");
} else if (displaySurface === "window") {
  // Do not move focus to the captured window.
  // Keep the capturing page focused.
  controller.setFocusBehavior("no-focus-change");
}
```

## Specifications

| Specification |
|---|
| Screen Capture # dom-capturecontroller |

## Browser compatibility
