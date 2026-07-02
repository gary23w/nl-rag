---
title: "CSSStyleDeclaration - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleDeclaration
domain: css-object-model
license: CC-BY-SA-4.0
tags: css object model, cssom style sheet, computed style access, cssstyledeclaration interface
fetched: 2026-07-02
---

# CSSStyleDeclaration

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

- Learn more
- See full compatibility

The **`CSSStyleDeclaration`** interface is the base class for objects that represent CSS declaration blocks with different supported sets of CSS style information:

- `CSSStyleProperties` — CSS styles declared in stylesheet (`CSSStyleRule.style`), inline styles for an element such as `HTMLElement`, `SVGElement`, and `MathMLElement`, or the computed style for an element returned by `Window.getComputedStyle()`.
- `CSSPageDescriptors` — Styles for CSS at-rules.

The interface exposes style information and various style-related methods and properties. For example, it provides `getPropertyValue()` for getting the value of a dash-named CSS property, such as `border-top`, which can't be directly accessed using dot notation because of the hyphens in its name.

**Note:** Earlier versions of the specification used `CSSStyleDeclaration` to represent all CSS declaration blocks, and some browsers and browser versions may still do so (check the browser compatibility tables for the above APIs). Generally the same website code will be functional in both old and new versions, but some properties returned in a `CSSStyleDeclaration` may not be relevant in a particular context.

## Attributes

**`CSSStyleDeclaration.cssText`**

Textual representation of the declaration block, if and only if it is exposed via `HTMLElement.style`. Setting this attribute changes the inline style. If you want a text representation of a computed declaration block, you can get it with `JSON.stringify()`.

**`CSSStyleDeclaration.length` Read only**

The number of properties. See the `item()` method below.

**`CSSStyleDeclaration.parentRule` Read only**

The containing `CSSRule`.

### CSS Properties

**`CSSStyleDeclaration.cssFloat`**

Special alias for the `float` CSS property.

**`CSSStyleDeclaration` named properties**

Dashed and camel-cased attributes for all supported CSS properties.

## Instance methods

**`CSSStyleDeclaration.getPropertyPriority()`**

Returns the optional priority, "important".

**`CSSStyleDeclaration.getPropertyValue()`**

Returns the property value given a property name.

**`CSSStyleDeclaration.item()`**

Returns a CSS property name by its index, or the empty string if the index is out-of-bounds.

**`CSSStyleDeclaration.removeProperty()`**

Removes a property from the CSS declaration block.

**`CSSStyleDeclaration.setProperty()`**

Modifies an existing CSS property or creates a new CSS property in the declaration block.

**`CSSStyleDeclaration.getPropertyCSSValue()`**

**Only supported via getComputedStyle in Firefox.** Returns the property value as a `CSSPrimitiveValue` or `null` for shorthand properties.

## Example

```js
const styleObj = document.styleSheets[0].cssRules[0].style;
console.log(styleObj.cssText);

for (let i = styleObj.length; i--; ) {
  const nameString = styleObj[i];
  styleObj.removeProperty(nameString);
}

console.log(styleObj.cssText);
```

## Specifications

| Specification |
|---|
| CSS Object Model (CSSOM) # the-cssstyledeclaration-interface |

## Browser compatibility
