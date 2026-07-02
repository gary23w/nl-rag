---
title: "Document: fullscreenElement property - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Document/fullscreenElement
domain: fullscreen-api
license: CC-BY-SA-4.0
tags: fullscreen api, request fullscreen element, fullscreen change event, exit fullscreen mode
fetched: 2026-07-02
---

# Document: fullscreenElement property

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

The **`Document.fullscreenElement`** read-only property returns the `Element` that is currently being presented in fullscreen mode in this document, or `null` if fullscreen mode is not currently in use.

Although this property is read-only, it will not throw if it is modified (even in strict mode); the setter is a no-operation and it will be ignored.

## Value

The `Element` object that's currently in fullscreen mode; if fullscreen mode isn't currently in use by the `document`, the returned value is `null`. If there are multiple elements in fullscreen mode, the topmost (most recently requested) element is returned.

## Examples

This example presents a function, `isVideoInFullscreen()`, which looks at the value returned by `fullscreenElement`; if the document is in fullscreen mode (`fullscreenElement` isn't `null`) and the fullscreen element's `nodeName` is `VIDEO`, indicating a `<video>` element, the function returns `true`, indicating that the video is in fullscreen mode.

```js
function isVideoInFullscreen() {
  if (document.fullscreenElement?.nodeName === "VIDEO") {
    return true;
  }
  return false;
}
```

## Specifications

| Specification |
|---|
| Fullscreen API # ref-for-dom-document-fullscreenelement① |

## Browser compatibility
