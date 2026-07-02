---
title: "Window: customElements property - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Window/customElements
domain: custom-elements
license: CC-BY-SA-4.0
tags: custom elements, custom element registry, autonomous html element, define web component
fetched: 2026-07-02
---

# Window: customElements property

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

- Learn more
- See full compatibility

The **`customElements`** read-only property of the `Window` interface returns a reference to the global `CustomElementRegistry` object, which can be used to register new custom elements and get information about previously registered custom elements.

The global registry is used for registering custom elements by default, but a shadow root can choose to use a scoped custom element registry in order to avoid potential clashes in defined element names.

## Value

A `CustomElementRegistry`.

## Examples

### Basic usage

The most common example you'll see of this property being used is to get access to the `CustomElementRegistry.define()` method to define and register a new custom element.

For example:

```js
let customElementRegistry = window.customElements;
customElementRegistry.define("my-custom-element", MyCustomElement);
```

Note that the custom element class is commonly defined directly inside the `define()` call, as shown:

```js
customElements.define(
  "element-details",
  class extends HTMLElement {
    constructor() {
      super();
      const template = document.getElementById("element-details-template");
      const shadowRoot = this.attachShadow({ mode: "open" }).appendChild(
        document.importNode(template.content, true),
      );
    }
  },
);
```

See our web-components-examples repo for more usage examples.

## Specifications

| Specification |
|---|
| HTML # dom-window-customelements |

## Browser compatibility
