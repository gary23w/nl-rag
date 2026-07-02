---
title: "CSS Object Model (CSSOM) - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/CSS_Object_Model
domain: critical-rendering-path
license: CC-BY-SA-4.0
tags: critical rendering path, browser rendering engine, document object model, css object model
fetched: 2026-07-02
---

# CSS Object Model (CSSOM)

The **CSS Object Model** is a set of APIs allowing the manipulation of CSS from JavaScript. It is much like the DOM, but for the CSS rather than the HTML. It allows users to read and modify CSS style dynamically.

The values of CSS are represented untyped, that is using `String` objects.

## Reference

- `AnimationEvent`
- `CaretPosition`
- `CSS`
- `CSSConditionRule`
- `CSSCounterStyleRule`
- `CSSFontFaceDescriptors`
- `CSSFontFaceRule`
- `CSSFontFeatureValuesMap`
- `CSSFontFeatureValuesRule`
- `CSSFunctionDeclarations`
- `CSSFunctionDescriptors`
- `CSSFunctionRule`
- `CSSGroupingRule`
- `CSSImportRule`
- `CSSKeyframeRule`
- `CSSKeyframesRule`
- `CSSMarginRule`
- `CSSMediaRule`
- `CSSNamespaceRule`
- `CSSPageRule`
- `CSSPositionTryRule`
- `CSSPositionTryDescriptors`
- `CSSRule`
- `CSSRuleList`
- `CSSStartingStyleRule`
- `CSSStyleDeclaration`
- `CSSStyleSheet`
- `CSSStyleRule`
- `CSSSupportsRule`
- `CSSNestedDeclarations`
- `FontFace`
- `FontFaceSet`
- `FontFaceSetLoadEvent`
- `MediaList`
- `MediaQueryList`
- `MediaQueryListEvent`
- `Screen`
- `StyleSheet`
- `StyleSheetList`
- `TransitionEvent`
- `VisualViewport`

Several other interfaces are also extended by the CSSOM-related specifications: `Document`, `Window`, `Element`, `HTMLElement`, `HTMLImageElement`, `Range`, `MouseEvent`, and `SVGElement`.

### CSS Typed Object Model

- `CSSImageValue`
- `CSSKeywordValue`
- `CSSMathClamp`
- `CSSMathInvert`
- `CSSMathMax`
- `CSSMathMin`
- `CSSMathNegate`
- `CSSMathProduct`
- `CSSMathSum`
- `CSSMathValue`
- `CSSMatrixComponent`
- `CSSNumericArray`
- `CSSNumericValue`
- `CSSPerspective`
- `CSSPositionValue`
- `CSSRotate`
- `CSSScale`
- `CSSSkew`
- `CSSSkewX`
- `CSSSkewY`
- `CSSStyleValue`
- `CSSTransformComponent`
- `CSSTransformValue`
- `CSSTranslate`
- `CSSUnitValue`
- `CSSUnparsedValue`
- `CSSVariableReferenceValue`
- `StylePropertyMap`
- `StylePropertyMapReadOnly`

### Obsolete CSSOM interfaces

**Deprecated:** This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the compatibility table at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

- `CSSPrimitiveValue`
- `CSSValue`
- `CSSValueList`

## Tutorials

- Determining the dimensions of elements
- Managing screen orientation

## Specifications

| Specification |
|---|
| CSS Object Model (CSSOM) |
| CSSOM View Module |
| CSS Typed OM Level 1 |

## Browser compatibility

All these features have been added little by little over the years to the different browsers: it was a quite complex process that can't be summarized in a simple table. Please refer to the specific interfaces for its availability.
