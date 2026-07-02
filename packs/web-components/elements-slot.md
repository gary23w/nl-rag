---
title: "<slot> HTML web component slot element - HTML"
source: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/slot
domain: web-components
license: CC-BY-SA-2.5
tags: web components, custom elements, html template element, customelementregistry
fetched: 2026-07-02
---

# `<slot>` HTML web component slot element

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

- Learn more
- See full compatibility

The **`<slot>`** HTML element is a placeholder inside a Web Component that you can fill with your own markup when the component is used. This lets you create separate DOM trees and present them together.

Slots can contain plain text, other HTML elements, or other web components. A slot can also contain default content, which is displayed if the slot is not assigned other content when the web component is used.

## Attributes

This element includes the global attributes.

**`name`**

The slot's name. A *named slot* is a `<slot>` element with a `name` attribute, while an *unnamed slot* has no `name` attribute, and the name defaults to the empty string.

When a shadow root uses named slot assignment, top-level child elements of its host are rendered in slots that have a matching name in their `slot` attribute. Slot names should be unique per shadow root: if you have two slots with the same name, all of the elements with a matching `slot` attribute are rendered in the *first* slot. All top-level child elements that don't have a `slot` attribute are rendered in the first unnamed `<slot>` element, which is referred to as the *default slot*. The `name` has no effect if the shadow root uses manual slot assignment.

For more information see `shadowrootslotassignment` on the `<template>` element and `Element.attachShadow()`.

## Examples

### Basic usage

This HTML shows how a number of named slots might be declared within a `<template>` element. Note that these slots are only used as slots when the template is used inside a shadow root.

```html
<template id="element-details-template">
  <style>
    details {
      font-family: "Open Sans Light", "Helvetica", "Arial", sans-serif;
    }
    .name {
      font-weight: bold;
      color: #217ac0;
      font-size: 120%;
    }
    h4 {
      margin: 10px 0 -8px 0;
      background: #217ac0;
      color: white;
      padding: 2px 6px;
      border: 1px solid #cee9f9;
      border-radius: 4px;
    }
    .attributes {
      margin-left: 22px;
      font-size: 90%;
    }
    .attributes p {
      margin-left: 16px;
      font-style: italic;
    }
  </style>
  <details>
    <summary>
      <code class="name">
        &lt;<slot name="element-name">NEED NAME</slot>&gt;
      </code>
      <span class="desc"><slot name="description">NEED DESCRIPTION</slot></span>
    </summary>
    <div class="attributes">
      <h4>Attributes</h4>
      <slot name="attributes"><p>None</p></slot>
    </div>
  </details>
  <hr />
</template>
```

**Note:** You can see this complete example in action at element-details (see it running live). In addition, you can find an explanation at Using templates and slots.

## Technical summary

| Content categories | Flow content, phrasing content |
|---|---|
| Permitted content | Transparent |
| Events | `slotchange` |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts phrasing content |
| Implicit ARIA role | No corresponding role |
| Permitted ARIA roles | No `role` permitted |
| DOM interface | `HTMLSlotElement` |

## Specifications

| Specification |
|---|
| HTML # the-slot-element |
| DOM # shadow-tree-slots |

## Browser compatibility
