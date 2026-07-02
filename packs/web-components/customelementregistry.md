---
title: "CustomElementRegistry - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/CustomElementRegistry
domain: web-components
license: CC-BY-SA-2.5
tags: web components, custom elements, html template element, customelementregistry
fetched: 2026-07-02
---

# CustomElementRegistry

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

The **`CustomElementRegistry`** interface provides methods for registering custom elements and querying registered elements. To get an instance of it, use the `window.customElements` property. To create a scoped registry, use the `CustomElementRegistry()` constructor.

## Constructor

**`CustomElementRegistry()`**

Creates a new `CustomElementRegistry` object, for scoped usage.

## Instance methods

**`CustomElementRegistry.define()`**

Defines a new custom element.

**`CustomElementRegistry.get()`**

Returns the constructor for the named custom element, or `undefined` if the custom element is not defined.

**`CustomElementRegistry.getName()`**

Returns the name for the already-defined custom element, or `null` if the custom element is not defined.

**`CustomElementRegistry.upgrade()`**

Upgrades a custom element directly, even before it is connected to its shadow root.

**`CustomElementRegistry.initialize()`**

Associates a scoped registry with a DOM subtree, setting the custom element registry on each inclusive descendant and upgrading any custom elements.

**`CustomElementRegistry.whenDefined()`**

Returns an empty `Promise` that resolves when a custom element becomes defined with the given name. If such a custom element is already defined, the returned promise is immediately fulfilled.

## Examples

See the Examples section in our guide to using custom elements.

## Specifications

| Specification |
|---|
| HTML # custom-elements-api |

## Browser compatibility
