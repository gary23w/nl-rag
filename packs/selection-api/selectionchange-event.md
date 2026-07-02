---
title: "Document: selectionchange event - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Document/selectionchange_event
domain: selection-api
license: CC-BY-SA-4.0
tags: selection api, text selection range, user selected content, caret anchor focus
fetched: 2026-07-02
---

# Document: selectionchange event

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2017.

- Learn more
- See full compatibility

The **`selectionchange`** event of the Selection API is fired when the current `Selection` of a `Document` is changed.

This event is not cancelable and does not bubble.

The event can be handled by adding an event listener for `selectionchange` or using the `onselectionchange` event handler.

**Note:** This event is not quite the same as the `selectionchange` events fired when the text selection in an `<input>` or `<textarea>` element is changed. See the `selectionchange` event of `HTMLInputElement` for more details.

## Syntax

Use the event name in methods like `addEventListener()`, or set an event handler property.

```js
addEventListener("selectionchange", (event) => { })

onselectionchange = (event) => { }
```

## Event type

A generic `Event`.

## Examples

```js
// addEventListener version
document.addEventListener("selectionchange", () => {
  console.log(document.getSelection());
});

// onselectionchange version
document.onselectionchange = () => {
  console.log(document.getSelection());
};
```

## Specifications

| Specification |
|---|
| Selection API # selectionchange-event |
| Selection API # dom-globaleventhandlers-onselectionchange |

## Browser compatibility
