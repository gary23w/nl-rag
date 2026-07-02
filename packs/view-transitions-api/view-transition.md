---
title: "::view-transition CSS pseudo-element - CSS"
source: https://developer.mozilla.org/en-US/docs/Web/CSS/::view-transition
domain: view-transitions-api
license: CC-BY-SA-4.0
tags: view transitions api, start view transition, view-transition-name property, animated dom state change
fetched: 2026-07-02
---

# `::view-transition` CSS pseudo-element

Baseline

2025

Newly available

Since October 2025, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

- Learn more
- See full compatibility

The **`::view-transition`** CSS pseudo-element represents the root of the view transitions overlay, which contains all view transition snapshot groups and sits over the top of all other page content.

During a view transition, `::view-transition` is included in the associated pseudo-element tree as explained in The view transition pseudo-element tree. It is the top-level node of this tree, and has one or more `::view-transition-group()`s as children.

`::view-transition` is given the following default styling in the UA stylesheet:

```css
:root::view-transition {
  position: fixed;
  inset: 0;
}
```

All `::view-transition-group()` pseudo-elements are positioned relative to the view transition root.

## Syntax

```css
::view-transition {
  /* ... */
}
```

## Examples

```css
::view-transition {
  background-color: rgb(0 0 0 / 25%);
}
```

## Specifications

| Specification |
|---|
| CSS View Transitions Module Level 1 # selectordef-view-transition |

## Browser compatibility
