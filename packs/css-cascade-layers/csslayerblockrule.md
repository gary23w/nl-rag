---
title: "CSSLayerBlockRule - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/CSSLayerBlockRule
domain: css-cascade-layers
license: CC-BY-SA-4.0
tags: css cascade layers, at-layer rule, cascade specificity ordering, layered style precedence
fetched: 2026-07-02
---

# CSSLayerBlockRule

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2022.

- Learn more
- See full compatibility

The **`CSSLayerBlockRule`** represents a `@layer` block rule.

## Instance properties

*Inherits properties from its ancestors `CSSGroupingRule` and `CSSRule`.*

**`CSSLayerBlockRule.name` Read only**

A string containing the name of the associated cascade layer.

## Instance methods

*Inherits methods from its ancestors `CSSGroupingRule` and `CSSRule`.*

## Examples

### HTML

```html
<p>I am displayed in <code>color: rebeccapurple</code>.</p>
```

### CSS

```css
@layer special {
  p {
    color: rebeccapurple;
  }
}
```

### JavaScript

```js
const item = document.getElementsByTagName("p")[0];
const rules = document.getElementById("css-output").sheet.cssRules;

const layer = rules[0]; // A CSSLayerBlockRule

item.textContent = `The CSSLayerBlockRule is for the "${layer.name}" layer`;
```

### Result

## Specifications

| Specification |
|---|
| CSS Cascading and Inheritance Level 5 # csslayerblockrule |

## Browser compatibility
