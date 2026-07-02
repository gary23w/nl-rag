---
title: "Selection: getRangeAt() method - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Selection/getRangeAt
domain: selection-api
license: CC-BY-SA-4.0
tags: selection api, text selection range, user selected content, caret anchor focus
fetched: 2026-07-02
---

# Selection: getRangeAt() method

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

- Learn more
- See full compatibility

The **`getRangeAt()`** method of the `Selection` interface returns a range object representing a currently selected range.

If the endpoints of the selected range are within a shadow tree then JavaScript does not have visibility of the shadow nodes, and the method should re-scope the range to include the host element that contains the end point. In practice most browsers do not yet implement this behavior, and the returned range is unpredictable.

**Note:** When selecting within nodes that might contain a shadow root, you can use `Selection.getComposedRanges()` (if supported) to get a selection range inside a shadow tree, or to reliably re-scope the selection to the host node.

## Syntax

```js
getRangeAt(index)
```

### Parameters

**`index`**

The zero-based index of the range to return. A negative number or a number greater than or equal to `Selection.rangeCount` will result in an error.

### Return value

The specified `Range` object.

## Examples

```js
let ranges = [];

const sel = window.getSelection();

for (let i = 0; i < sel.rangeCount; i++) {
  ranges[i] = sel.getRangeAt(i);
}
/* Each item in the ranges array is now
 * a range object representing one of the
 * ranges in the current selection */
```

## Specifications

| Specification |
|---|
| Selection API # dom-selection-getrangeat |

## Browser compatibility
