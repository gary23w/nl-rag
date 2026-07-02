---
title: "Document: pictureInPictureElement property - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Document/pictureInPictureElement
domain: picture-in-picture
license: CC-BY-SA-4.0
tags: picture in picture api, floating video window, detached video overlay, enter pip mode
fetched: 2026-07-02
---

# Document: pictureInPictureElement property

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

The read-only **`pictureInPictureElement`** property of the `Document` interface returns the `Element` that is currently being presented in picture-in-picture mode in this document, or `null` if picture-in-picture mode is not currently in use.

Although this property is read-only, it will not throw if it is modified (even in strict mode); the setter is a no-operation and will be ignored.

## Value

A reference to the `Element` object that's currently in picture-in-picture mode.

Returns `null` if the document has no associated element in picture-in-picture mode. For example, there's no picture-in-picture element, or the element is from an iframe.

## Examples

This example presents a function, `exitPictureInPicture()`, which tests the value returned by `pictureInPictureElement`. If the document is in picture-in-picture mode (`pictureInPictureElement` isn't `null`), `Document.exitPictureInPicture()` is run to exit picture-in-picture mode.

```js
function exitPictureInPicture() {
  if (document.pictureInPictureElement) {
    document.exitPictureInPicture();
  }
}
```

## Specifications

| Specification |
|---|
| Picture-in-Picture # dom-documentorshadowroot-pictureinpictureelement |

## Browser compatibility
