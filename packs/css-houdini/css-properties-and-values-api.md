---
title: "CSS Properties and Values API - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/CSS_Properties_and_Values_API
domain: css-houdini
license: CC-BY-SA-4.0
tags: css houdini apis, css painting worklet, css properties and values api, registered custom property
fetched: 2026-07-02
---

# CSS Properties and Values API

Baseline

2024

Newly available

Since July 2024, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

- Learn more
- See full compatibility

The **CSS Properties and Values API** — part of the CSS Houdini umbrella of APIs — allows developers to explicitly define their CSS custom properties, allowing for property type checking, default values, and properties that do or do not inherit their value.

## Interfaces

**`CSS.registerProperty`**

Defines how a browser should parse CSS custom properties. Access this interface through `CSS.registerProperty` in JavaScript.

**`@property`**

Defines how a browser should parse CSS custom properties. Access this interface through `@property` at-rule in CSS.

## Examples

The following will register a custom property named `--my-color` using `CSS.registerProperty` in JavaScript. `--my-color` will use the CSS color syntax, it will have a default value of `#c0ffee`, and it will not inherit its value:

```js
window.CSS.registerProperty({
  name: "--my-color",
  syntax: "<color>",
  inherits: false,
  initialValue: "#c0ffee",
});
```

The same registration can take place in CSS using the `@property` at-rule:

```css
@property --my-color {
  syntax: "<color>";
  inherits: false;
  initial-value: #c0ffee;
}
```

## Specifications

| Specification |
|---|
| CSS Properties and Values API Level 1 # the-css-property-rule-interface |
| CSS Properties and Values API Level 1 # the-registerproperty-function |

## Browser compatibility

### api.CSSPropertyRule

### api.CSS.registerProperty_static
