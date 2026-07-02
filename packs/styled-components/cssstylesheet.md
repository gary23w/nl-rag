---
title: "CSSStyleSheet - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleSheet
domain: styled-components
license: CC-BY-SA-4.0
tags: styled components, css-in-js, component-scoped styling, tagged template css
fetched: 2026-07-02
---

# CSSStyleSheet

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

The **`CSSStyleSheet`** interface represents a single CSS stylesheet, and lets you inspect and modify the list of rules contained in the stylesheet. It inherits properties and methods from its parent, `StyleSheet`.

A stylesheet consists of a collection of `CSSRule` objects representing each of the rules in the stylesheet. The rules are contained in a `CSSRuleList`, which can be obtained from the stylesheet's `cssRules` property.

For example, one rule might be a `CSSStyleRule` object containing a style such as:

```css
h1,
h2 {
  font-size: 16pt;
}
```

Another rule might be an *at-rule* such as `@import` or `@media`, and so forth.

See the Obtaining a StyleSheet section for the various ways a `CSSStyleSheet` object can be obtained. A `CSSStyleSheet` object can also be directly constructed. The constructor, and the `CSSStyleSheet.replace()`, and `CSSStyleSheet.replaceSync()` methods are newer additions to the specification, enabling *Constructable Stylesheets*.

To apply a `CSSStyleSheet` to a document or shadow root, assign it to the `Document.adoptedStyleSheets` or `ShadowRoot.adoptedStyleSheets` property, respectively.

## Constructor

**`CSSStyleSheet()`**

Creates a new `CSSStyleSheet` object.

## Instance properties

*Inherits properties from its parent, `StyleSheet`.*

**`CSSStyleSheet.cssRules` Read only**

Returns a live `CSSRuleList` which maintains an up-to-date list of the `CSSRule` objects that comprise the stylesheet.

**Note:** In some browsers, if a stylesheet is loaded from a different domain, accessing `cssRules` results in a `SecurityError`.

**`CSSStyleSheet.ownerRule` Read only**

If this stylesheet is imported into the document using an `@import` rule, the `ownerRule` property returns the corresponding `CSSImportRule`; otherwise, this property's value is `null`.

## Instance methods

*Inherits methods from its parent, `StyleSheet`.*

**`CSSStyleSheet.deleteRule()`**

Deletes the rule at the specified index into the stylesheet's rule list.

**`CSSStyleSheet.insertRule()`**

Inserts a new rule at the specified position in the stylesheet, given the textual representation of the rule.

**`CSSStyleSheet.replace()`**

Asynchronously replaces the content of the stylesheet and returns a `Promise` that resolves with the updated `CSSStyleSheet`.

**`CSSStyleSheet.replaceSync()`**

Synchronously replaces the content of the stylesheet.

## Legacy properties

*These properties are legacy properties as introduced by Microsoft; these are maintained for compatibility with existing sites.*

**`rules` Read only**

The `rules` property is functionally identical to the standard `cssRules` property; it returns a live `CSSRuleList` which maintains an up-to-date list of all of the rules in the style sheet.

## Legacy methods

*These methods are legacy methods as introduced by Microsoft; these are maintained for compatibility with existing sites.*

**`addRule()`**

Adds a new rule to the stylesheet given the selector to which the style applies and the style block to apply to the matching elements.

This differs from `insertRule()`, which takes the textual representation of the entire rule as a single string.

**`removeRule()`**

Functionally identical to `deleteRule()`; removes the rule at the specified index from the stylesheet's rule list.

## Obtaining a StyleSheet

A stylesheet is associated with at most one `Document`, which it applies to (unless disabled). A list of `CSSStyleSheet` objects for a given document can be obtained using the `Document.styleSheets` property. A specific style sheet can also be accessed from its *owner* object (`Node` or `CSSImportRule`), if any.

A `CSSStyleSheet` object is created and inserted into the document's `Document.styleSheets` list automatically by the browser, when a stylesheet is loaded for a document.

A (possibly incomplete) list of ways a stylesheet can be associated with a document follows:

| Reason for the style sheet to be associated with the document | Appears in `document. styleSheets` list | Getting the owner element/rule given the style sheet object | The interface for the owner object | Getting the CSSStyleSheet object from the owner |
|---|---|---|---|---|
| `<style>` and `<link>` elements in the document | Yes | `.ownerNode` | `HTMLLinkElement`, `HTMLStyleElement`, or `SVGStyleElement` | `HTMLLinkElement.sheet`, `HTMLStyleElement.sheet`, or `SVGStyleElement.sheet` |
| CSS `@import` rule in other style sheets applied to the document | Yes | `.ownerRule` | `CSSImportRule` | `.styleSheet` |
| `<?xml-stylesheet ?>` processing instruction in the (non-HTML) document | Yes | `.ownerNode` | `ProcessingInstruction` | `.sheet` |
| JavaScript `import ... with { type: "css" }` | No | N/A | N/A | N/A |
| HTTP Link Header | Yes | *N/A* | N/A | N/A |
| User agent (default) style sheets | No | N/A | N/A | N/A |

## Specifications

| Specification |
|---|
| CSS Object Model (CSSOM) # the-cssstylesheet-interface |

## Browser compatibility
