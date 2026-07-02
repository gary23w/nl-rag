---
title: "CSSStyleValue - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleValue
domain: css-typed-om
license: CC-BY-SA-4.0
tags: css typed object model, typed cssom value, css unit value, attribute style map
fetched: 2026-07-02
---

# CSSStyleValue

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

The **`CSSStyleValue`** interface of the CSS Typed Object Model API is the base class of all CSS values accessible through the Typed OM API. An instance of this class may be used anywhere a string is expected.

## Interfaces based on CSSStyleValue

Below is a list of interfaces based on the `CSSStyleValue` interface.

- `CSSImageValue`
- `CSSKeywordValue`
- `CSSNumericValue`
- `CSSPositionValue`
- `CSSTransformValue`
- `CSSUnparsedValue`

## Static methods

**`CSSStyleValue.parse()`**

Sets a specific CSS property to the specified values and returns the first value as a `CSSStyleValue` object.

**`CSSStyleValue.parseAll()`**

Sets all occurrences of a specific CSS property to the specified value and returns an array of `CSSStyleValue` objects, each containing one of the supplied values.

## Specifications

| Specification |
|---|
| CSS Typed OM Level 1 # stylevalue-objects |

## Browser compatibility
