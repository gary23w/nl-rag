---
title: "ResizeObserver: observe() method - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver/observe
domain: resize-observer
license: CC-BY-SA-4.0
tags: resize observer api, element size change callback, content box resize, observe box dimensions
fetched: 2026-07-02
---

# ResizeObserver: observe() method

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2020.

- Learn more
- See full compatibility

The **`observe()`** method of the `ResizeObserver` interface starts observing the specified `Element` or `SVGElement`.

## Syntax

```js
observe(target)
observe(target, options)
```

### Parameters

**`target`**

A reference to an `Element` or `SVGElement` to be observed.

**`options` Optional**

An options object allowing you to set options for the observation. Currently this only has one possible option that can be set:

**`box`**

Sets which box model the observer will observe changes to. Possible values are:

**`content-box` (the default)**

Size of the content area as defined in CSS.

**`border-box`**

Size of the box border area as defined in CSS.

**`device-pixel-content-box`**

The size of the content area as defined in CSS, in device pixels, before applying any CSS transforms on the element or its ancestors.

### Return value

None (`undefined`).

### Exceptions

None.

## Examples

The following snippet is taken from the resize-observer-text.html (see source) example:

```js
const resizeObserver = new ResizeObserver((entries) => {
  for (const entry of entries) {
    if (entry.contentBoxSize) {
      // Checking for chrome as using a non-standard array
      if (entry.contentBoxSize[0]) {
        h1Elem.style.fontSize = `${Math.max(
          1.5,
          entry.contentBoxSize[0].inlineSize / 200,
        )}rem`;
        pElem.style.fontSize = `${Math.max(
          1,
          entry.contentBoxSize[0].inlineSize / 600,
        )}rem`;
      } else {
        h1Elem.style.fontSize = `${Math.max(
          1.5,
          entry.contentBoxSize.inlineSize / 200,
        )}rem`;
        pElem.style.fontSize = `${Math.max(
          1,
          entry.contentBoxSize.inlineSize / 600,
        )}rem`;
      }
    } else {
      h1Elem.style.fontSize = `${Math.max(
        1.5,
        entry.contentRect.width / 200,
      )}rem`;
      pElem.style.fontSize = `${Math.max(1, entry.contentRect.width / 600)}rem`;
    }
  }
  console.log("Size changed");
});

resizeObserver.observe(divElem);
```

An `observe()` call with an options object would look like so:

```js
resizeObserver.observe(divElem, { box: "border-box" });
```

## Specifications

| Specification |
|---|
| Resize Observer # dom-resizeobserver-observe |

## Browser compatibility
