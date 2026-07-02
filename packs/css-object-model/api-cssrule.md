---
title: "CSSRule - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/CSSRule
domain: css-object-model
license: CC-BY-SA-4.0
tags: css object model, cssom style sheet, computed style access, cssstyledeclaration interface
fetched: 2026-07-02
---

# CSSRule

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

- Learn more
- See full compatibility

The **`CSSRule`** interface represents a single CSS rule. There are several types of rules which inherit properties from `CSSRule`.

- `CSSGroupingRule`
- `CSSStyleRule`
- `CSSImportRule`
- `CSSMediaRule`
- `CSSFontFaceRule`
- `CSSFunctionDeclarations`
- `CSSPageRule`
- `CSSNamespaceRule`
- `CSSKeyframesRule`
- `CSSKeyframeRule`
- `CSSCounterStyleRule`
- `CSSSupportsRule`
- `CSSFontFeatureValuesRule`
- `CSSFontPaletteValuesRule`
- `CSSLayerBlockRule`
- `CSSLayerStatementRule`
- `CSSPropertyRule`
- `CSSNestedDeclarations`
- `CSSViewTransitionRule`

## Instance properties

The `CSSRule` interface specifies the properties common to all rules, while properties unique to specific rule types are specified in the more specialized interfaces for those rules' respective types.

**`CSSRule.cssText`**

Represents the textual representation of the rule, e.g., `"h1,h2 { font-size: 16pt }"` or `"@import 'url'"`. To access or modify parts of the rule (e.g., the value of "font-size" in the example) use the properties on the specialized interface for the rule's type (see above).

**`CSSRule.parentRule` Read only**

Returns the containing rule, otherwise `null`. E.g. if this rule is a style rule inside an `@media` block, the parent rule would be that `CSSMediaRule`.

**`CSSRule.parentStyleSheet` Read only**

Returns the `CSSStyleSheet` object for the style sheet that contains this rule

**`CSSRule.type` Read only**

Returns one of the Type constants to determine which type of rule is represented.

## Examples

References to a `CSSRule` may be obtained by looking at a `CSSStyleSheet`'s `cssRules` list.

```js
let myRules = document.styleSheets[0].cssRules; // Returns a CSSRuleList
console.log(myRules);
```

## Specifications

| Specification |
|---|
| CSS Object Model (CSSOM) # the-cssrule-interface |

## Browser compatibility
