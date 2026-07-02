---
title: "Document: pointerlockchange event - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Document/pointerlockchange_event
domain: pointer-lock
license: CC-BY-SA-4.0
tags: pointer lock api, mouse capture relative motion, raw mouse movement, pointer lock change event
fetched: 2026-07-02
---

# Document: pointerlockchange event

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

The **`pointerlockchange`** event is fired when the pointer is locked/unlocked.

The event handler can use `Document.pointerLockElement` to determine whether the pointer is locked, and if so, to which element it is locked.

This event is not cancelable and does not bubble.

## Syntax

Use the event name in methods like `addEventListener()`, or set an event handler property.

```js
addEventListener("pointerlockchange", (event) => { })

onpointerlockchange = (event) => { }
```

## Event type

A generic `Event`.

## Examples

Using `addEventListener()`:

```js
addEventListener("pointerlockchange", (event) => {
  if (document.pointerLockElement)
    console.log("The pointer is locked to: ", document.pointerLockElement);
  else {
    console.log("The pointer is not locked");
  }
});
```

Using the `onpointerlockchange` event handler property:

```js
document.onpointerlockchange = (event) => {
  if (document.pointerLockElement)
    console.log("The pointer is locked to: ", document.pointerLockElement);
  else {
    console.log("The pointer is not locked");
  }
};
```

## Specifications

| Specification |
|---|
| Pointer Lock 2.0 # pointerlockchange-and-pointerlockerror-events |
| Pointer Lock 2.0 # dom-document-onpointerlockchange |

## Browser compatibility
