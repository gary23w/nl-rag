---
title: "Element: slot property - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Element/slot
domain: shadow-dom
license: CC-BY-SA-2.5
tags: shadow dom, shadow root, attachshadow, encapsulated dom, template and slots
fetched: 2026-07-02
---

# Element: slot property

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

- Learn more
- See full compatibility

The **`slot`** property of the `Element` interface returns the name of the shadow DOM slot the element is inserted in.

A slot is a placeholder inside a web component that users can fill with their own markup (see Using templates and slots for more information).

## Value

A string.

## Examples

In our simple-template example (see it live), we create a trivial custom element example called `<my-paragraph>` in which a shadow root is attached and then populated using the contents of a template that contains a slot named `my-text`.

When `<my-paragraph>` is used in the document, the slot is populated by a slottable element by including it inside the element with a `slot` attribute with the value `my-text`. Here is one such example:

```html
<my-paragraph>
  <span slot="my-text">Let's have some different text!</span>
</my-paragraph>
```

In our JavaScript file we get a reference to the `<span>` shown above, then log a reference to the name of the corresponding `<slot>` element.

```js
let slottedSpan = document.querySelector("my-paragraph span");
console.log(slottedSpan.slot); // logs 'my-text'
```

## Specifications

| Specification |
|---|
| DOM # ref-for-dom-element-slot① |

## Browser compatibility
