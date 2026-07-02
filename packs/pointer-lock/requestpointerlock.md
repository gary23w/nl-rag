---
title: "Element: requestPointerLock() method - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Element/requestPointerLock
domain: pointer-lock
license: CC-BY-SA-4.0
tags: pointer lock api, mouse capture relative motion, raw mouse movement, pointer lock change event
fetched: 2026-07-02
---

# Element: requestPointerLock() method

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

The **`requestPointerLock()`** method of the `Element` interface lets you asynchronously ask for the pointer to be locked on the given element.

To track the success or failure of the request, it is necessary to listen for the `pointerlockchange` and `pointerlockerror` events at the `Document` level.

**Note:** In the current specification, `requestPointerLock()` only communicates the success or failure of the request by firing `pointerlockchange` or `pointerlockerror` events. A proposed update to the specification updates `requestPointerLock()` to return a `Promise` which communicates success or failure. This page documents the version that returns a `Promise`. However, note that this version is not yet a standard and is not implemented by all browsers. See Browser compatibility for more information.

## Syntax

```js
requestPointerLock()
requestPointerLock(options)
```

### Parameters

**`options` Optional**

An options object that can contain the following properties:

**`unadjustedMovement` Optional**

Disables OS-level adjustment for mouse acceleration, and accesses raw mouse input instead. The default value is `false`; setting it to `true` will disable mouse acceleration.

### Return value

A `Promise` that resolves with `undefined`.

## Security

Transient activation is required when calling `requestPointerLock()`. The user has to interact with the page or a UI element in order for this feature to work. Also, the target element's associated document must be in the active state.

If calling `requestPointerLock()` immediately after releasing the pointer lock via the default unlock gesture (instead of through an `exitPointerLock()` call), the call will fail, even if a transient activation is available.

If calling `requestPointerLock()` with `requestFullscreen()`, the `requestPointerLock()` must be called first, because the `requestFullscreen()` will consume the state of transient activation.

The `allow-pointer-lock` sandbox token must be added when calling `requestPointerLock()` in an `<iframe>` element. Also, no other elements in other `<iframe>` elements may be in pointer lock mode.

## Examples

Pointer lock is often used in online games, when you want your mouse movement to be focused on controlling the game, without the distraction of the mouse pointer moving around, going outside the game area, or reaching the edge of the window.

To enable pointer lock, you would get the user to interact with the UI in some way, perhaps by pressing a button, or the game canvas itself.

```js
canvas.addEventListener("click", async () => {
  await canvas.requestPointerLock();
});
```

Operating systems enable mouse acceleration by default, which is useful when you sometimes want slow precise movement (think about you might use a graphics package), but also want to move great distances with a faster mouse movement (think about scrolling, and selecting several files). For some first-person perspective games however, raw mouse input data is preferred for controlling camera rotation — where the same distance movement, fast or slow, results in the same rotation. This results in a better gaming experience and higher accuracy, according to professional gamers.

To disable OS-level mouse acceleration and access raw mouse input, you can set the `unadjustedMovement` to `true`:

```js
canvas.addEventListener("click", async () => {
  await canvas.requestPointerLock({
    unadjustedMovement: true,
  });
});
```

For more example code, see:

- pointer lock demo (see source code)
- Pointer Lock API
- Disable mouse acceleration to provide a better FPS gaming experience

## Specifications

| Specification |
|---|
| Pointer Lock 2.0 # dom-element-requestpointerlock |

## Browser compatibility
