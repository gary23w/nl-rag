---
title: "ShadowRoot: mode property - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot/mode
domain: declarative-shadow-dom
license: CC-BY-SA-4.0
tags: declarative shadow dom, shadowrootmode attribute, server rendered shadow tree, template shadowroot parsing
fetched: 2026-07-02
---

# ShadowRoot: mode property

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

- Learn more
- See full compatibility

The **`mode`** read-only property of the `ShadowRoot` specifies its mode — either `open` or `closed`. This defines whether or not the shadow root's internal features are accessible from JavaScript.

When the `mode` of a shadow root is `"closed"`, the shadow root's implementation internals are inaccessible and unchangeable from JavaScript—in the same way the implementation internals of, for example, the `<video>` element are inaccessible and unchangeable from JavaScript.

The property value is set using the `mode` property of the object passed to `Element.attachShadow()`, or using the `shadowrootmode` attribute of the `<template>` element when a shadow root is created declaratively.

## Value

A string value that can have either of the values:

**`open`**

Elements of the shadow root are accessible from JavaScript outside the root.

**`closed`**

Nodes inside the closed shadow tree cannot be accessed by JavaScript outside of the root.

## Examples

```js
// We create a closed shadow root, that is not accessible
let element = document.createElement("div");
element.attachShadow({ mode: "closed" });
console.log(element.shadowRoot); // logs null as the shadow root is closed

// We create an open shadow root, that is accessible
let element2 = document.createElement("div");
element2.attachShadow({ mode: "open" });
console.log(`The shadow is ${element2.shadowRoot.mode}`); // logs "The shadow is open"
element2.shadowRoot.textContent = "Opened shadow"; // The shadow is open, we can access it from outside
```

## Specifications

| Specification |
|---|
| DOM # dom-shadowroot-mode |

## Browser compatibility
