---
title: "Document: exitFullscreen() method - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Document/exitFullscreen
domain: fullscreen-api
license: CC-BY-SA-4.0
tags: fullscreen api, request fullscreen element, fullscreen change event, exit fullscreen mode
fetched: 2026-07-02
---

# Document: exitFullscreen() method

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

The `Document` method **`exitFullscreen()`** requests that the element on this document which is currently being presented in fullscreen mode be taken out of fullscreen mode, restoring the previous state of the screen. This usually reverses the effects of a previous call to `Element.requestFullscreen()`.

## Syntax

```js
exitFullscreen()
```

### Parameters

None.

### Return value

A `Promise` which is resolved once the user agent has finished exiting fullscreen mode. If an error occurs while attempting to exit fullscreen mode, the `catch()` handler for the promise is called.

## Examples

This example causes the current document to toggle in and out of a fullscreen presentation whenever the mouse button is clicked within it.

```js
document.onclick = (event) => {
  if (document.fullscreenElement) {
    document
      .exitFullscreen()
      .then(() => console.log("Document Exited from Full screen mode"))
      .catch((err) => console.error(err));
  } else {
    document.documentElement.requestFullscreen();
  }
};
```

**Note:** For a more complete example, see the `Element.requestFullscreen()` examples.

## Specifications

| Specification |
|---|
| Fullscreen API # ref-for-dom-document-exitfullscreen① |

## Browser compatibility
