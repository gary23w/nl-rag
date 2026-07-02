---
title: "Element: setPointerCapture() method - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Element/setPointerCapture
domain: pointer-events
license: CC-BY-SA-4.0
tags: pointer events model, unified input pointer, pointer capture target, primary pointer detection
fetched: 2026-07-02
---

# Element: setPointerCapture() method

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2020.

- Learn more
- See full compatibility

The **`setPointerCapture()`** method of the `Element` interface is used to designate a specific element as the *capture target* of future pointer events. Subsequent events for the pointer will be targeted at the capture element until capture is released (via `Element.releasePointerCapture()` or the `pointerup` event is fired).

See pointer events for an overview and examples of how pointer capture works.

## Syntax

```js
setPointerCapture(pointerId)
```

### Parameters

**`pointerId`**

The `pointerId` of a `PointerEvent` object.

### Return value

None (`undefined`).

### Exceptions

**`NotFoundError` `DOMException`**

Thrown if `pointerId` does not match any active pointer.

## Examples

This example sets pointer capture on a `<div>` when you press down on it. This lets you slide the element horizontally, even when your pointer moves outside of its boundaries.

### HTML

```html
<div id="slider">SLIDE ME</div>
```

### CSS

```css
div {
  width: 140px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #ffbbee;
  touch-action: none;
}
```

### JavaScript

```js
const slider = document.getElementById("slider");

function beginSliding(e) {
  slider.onpointermove = slide;
  slider.setPointerCapture(e.pointerId);
}

function stopSliding(e) {
  slider.onpointermove = null;
  slider.releasePointerCapture(e.pointerId);
}

function slide(e) {
  slider.style.transform = `translate(${e.clientX - 70}px)`;
}

slider.onpointerdown = beginSliding;
slider.onpointerup = stopSliding;
```

### Result

## Specifications

| Specification |
|---|
| Pointer Events # dom-element-setpointercapture |

## Browser compatibility
