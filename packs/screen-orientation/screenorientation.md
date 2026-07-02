---
title: "ScreenOrientation - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/ScreenOrientation
domain: screen-orientation
license: CC-BY-SA-4.0
tags: screen orientation api, orientation lock landscape, portrait orientation type, orientation change event
fetched: 2026-07-02
---

# ScreenOrientation

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2023.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

The **`ScreenOrientation`** interface of the Screen Orientation API provides information about the current orientation of the document.

A **`ScreenOrientation`** instance object can be retrieved using the `screen.orientation` property.

## Instance properties

**`ScreenOrientation.type` Read only**

Returns the document's current orientation type, one of `portrait-primary`, `portrait-secondary`, `landscape-primary`, or `landscape-secondary`.

**`ScreenOrientation.angle` Read only**

Returns the document's current orientation angle.

## Instance methods

**`ScreenOrientation.lock()`**

Locks the orientation of the containing document to its default orientation and returns a `Promise`.

**`ScreenOrientation.unlock()`**

Unlocks the orientation of the containing document from its default orientation.

## Events

Listen to these events using `addEventListener()` or by assigning an event listener to the `oneventname` property of this interface.

**`change`**

Fired whenever the screen changes orientation.

## Example

In the following example, we listen for an orientation `change` event and log the new screen orientation type and angle.

```js
screen.orientation.addEventListener("change", (event) => {
  const type = event.target.type;
  const angle = event.target.angle;
  console.log(`ScreenOrientation change: ${type}, ${angle} degrees.`);
});
```

## Specifications

| Specification |
|---|
| Screen Orientation # screenorientation-interface |

## Browser compatibility
