---
title: "CSSUnitValue - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/CSSUnitValue
domain: css-typed-om
license: CC-BY-SA-4.0
tags: css typed object model, typed cssom value, css unit value, attribute style map
fetched: 2026-07-02
---

# CSSUnitValue

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

The **`CSSUnitValue`** interface of the CSS Typed Object Model API represents values that contain a single unit type.

For example, the value `42px` (a `<dimension>`) would be represented by a `CSSNumericValue`.

## Constructor

**`CSSUnitValue()`**

Creates a new `CSSUnitValue` object.

## Instance properties

**`CSSUnitValue.value`**

Returns a double indicating the number of units. For a `CSSNumericValue` representing `42px`, this would be `42`.

**`CSSUnitValue.unit`**

Returns a string indicating the type of unit. For a `CSSNumericValue` representing `42px`, this would be `"px"`.

## Static methods

*The interface may also inherit methods from its parent interface, `CSSNumericValue`.*

## Instance methods

*The interface may also inherit methods from its parent interface, `CSSNumericValue`.*

## Examples

The following shows a method of creating a `CSSPositionValue` from individual `CSSUnitValue` constructors.

```js
let pos = new CSSPositionValue(
  new CSSUnitValue(5, "px"),
  new CSSUnitValue(10, "px"),
);
```

## Specifications

| Specification |
|---|
| CSS Typed OM Level 1 # simple-numeric |

## Browser compatibility
