---
title: "HTMLElement: attachInternals() method - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/attachInternals
domain: custom-elements-deep
license: CC-BY-SA-4.0
tags: custom elements lifecycle, connected callback reaction, attribute changed callback, element upgrade reaction
fetched: 2026-07-02
---

# HTMLElement: attachInternals() method

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2023.

- Learn more
- See full compatibility

The **`HTMLElement.attachInternals()`** method returns an `ElementInternals` object. This method allows a custom element to participate in HTML forms. The `ElementInternals` interface provides utilities for working with these elements in the same way you would work with any standard HTML form element, and also exposes the Accessibility Object Model to the element.

## Syntax

```js
attachInternals()
```

### Parameters

None.

### Return value

An `ElementInternals` object.

### Exceptions

**`NotSupportedError` `DOMException`**

Thrown if the element is not a custom element.

**`NotSupportedError` `DOMException`**

Thrown if the "internals" feature was disabled as part of the element definition.

**`NotSupportedError` `DOMException`**

Thrown if this method is called twice on the same element.

## Examples

The following example demonstrates how to create a custom form-associated element with `HTMLElement.attachInternals`. The `ElementInternals.form` property is then printed to the console to demonstrate that we have an `ElementInternals` object.

```js
class CustomCheckbox extends HTMLElement {
  static formAssociated = true;

  constructor() {
    super();
    this.internals_ = this.attachInternals();
  }
  // …
}

window.customElements.define("custom-checkbox", CustomCheckbox);

let element = document.getElementById("custom-checkbox");
console.log(element.internals_.form);
```

## Specifications

| Specification |
|---|
| HTML # dom-attachinternals |

## Browser compatibility
