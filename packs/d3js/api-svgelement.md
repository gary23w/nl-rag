---
title: "SVGElement - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/SVGElement
domain: d3js
license: CC-BY-SA-4.0
tags: d3.js, d3js, data-driven documents, svg data binding
fetched: 2026-07-02
---

# SVGElement

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

All of the SVG DOM interfaces that correspond directly to elements in the SVG language derive from the `SVGElement` interface.

## Instance properties

*Also inherits properties from the `Element` interface.*

**`SVGElement.attributeStyleMap` Read only**

A `StylePropertyMap` representing the declarations of the element's `style` attribute.

**`SVGElement.autofocus`**

Whether the control should be focused when the page loads, or when a `<dialog>` or popover become shown.

**`SVGElement.className` Read only**

An `SVGAnimatedString` that reflects the value of the `class` attribute on the given element, or the empty string if `class` is not present. This attribute is deprecated and may be removed in a future version of this specification. Authors are advised to use `Element.classList` instead.

**`SVGElement.dataset` Read only**

A `DOMStringMap` object which provides a list of key/value pairs of named data attributes which correspond to custom data attributes attached to the element. These can also be defined in SVG using attributes of the form `data-*`, where `*` is the key name for the pair. This works just like HTML's `HTMLElement.dataset` property and HTML's `data-*` global attribute.

**`SVGElement.nonce`**

Returns the cryptographic number used once that is used by Content Security Policy to determine whether a given fetch will be allowed to proceed.

**`SVGElement.ownerSVGElement` Read only**

An `SVGSVGElement` referring to the nearest ancestor `<svg>` element. `null` if the given element is the outermost `<svg>` element.

**`SVGElement.style`**

A `CSSStyleDeclaration` representing the declarations of the element's `style` attribute.

**`SVGElement.tabIndex`**

The position of the element in the tabbing order.

**`SVGElement.viewportElement` Read only**

The `SVGElement` which established the current viewport. Often the nearest ancestor `<svg>` element. `null` if the given element is the outermost `<svg>` element.

## Instance methods

*This interface also inherits methods from `Element`.*

**`SVGElement.blur()`**

Removes keyboard focus from the currently focused element.

**`SVGElement.focus()`**

Makes the element the current keyboard focus.

## Events

Listen to these events using `addEventListener()` or by assigning an event listener to the equivalent `on...` handler property.

**`abort`**

Fired when page loading is stopped before an SVG element has been allowed to load completely.

**`error`**

Fired when an SVG element does not load properly or when an error occurs during script execution.

**`load`**

Fires on an `SVGElement` when it is loaded in the browser.

**`resize`**

Fired when an SVG document is being resized.

**`scroll`**

Fired when an SVG document view is being shifted along the X and/or Y axes.

**`unload`**

Fired when the DOM implementation removes an SVG document from a window or frame.

## Specifications

| Specification |
|---|
| Scalable Vector Graphics (SVG) 2 # InterfaceSVGElement |

## Browser compatibility
