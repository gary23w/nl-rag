---
title: "Window: getSelection() method - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Window/getSelection
domain: selection-api
license: CC-BY-SA-4.0
tags: selection api, text selection range, user selected content, caret anchor focus
fetched: 2026-07-02
---

# Window: getSelection() method

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

- Learn more
- See full compatibility

The **`getSelection()`** method of the `Window` interface returns the `Selection` object associated with the window's `document`, representing the range of text selected by the user or the current position of the caret.

## Syntax

```js
getSelection()
```

### Parameters

None.

### Return value

A `Selection` object, or `null` if the associated document has no browsing context (for example, the window is an `<iframe>` that is not attached to a document).

When called on an `<iframe>` that is not displayed (e.g., where `display: none` is set) Firefox returns `null`, whereas other browsers returns a `Selection` object with `Selection.type` set to `None`.

## Examples

```js
function foo() {
  const selObj = window.getSelection();
  alert(selObj);
  const selRange = selObj.getRangeAt(0);
  // do stuff with the range
}
```
