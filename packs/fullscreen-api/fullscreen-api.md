---
title: "Fullscreen API - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Fullscreen_API
domain: fullscreen-api
license: CC-BY-SA-4.0
tags: fullscreen api, request fullscreen element, fullscreen change event, exit fullscreen mode
fetched: 2026-07-02
---

# Fullscreen API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

The **Fullscreen API** adds methods to present a specific `Element` (and its descendants) in fullscreen mode, and to exit fullscreen mode once it is no longer needed. This makes it possible to present desired content—such as an online game—using the user's entire screen, removing all browser user interface elements and other applications from the screen until fullscreen mode is shut off.

See the article Guide to the Fullscreen API for details on how to use the API.

## Interfaces

*The Fullscreen API has no interfaces of its own. Instead, it augments several other interfaces to add the methods, properties, and event handlers needed to provide fullscreen functionality. These are listed in the following sections.*

## Instance methods

The Fullscreen API adds methods to the `Document` and `Element` interfaces to allow turning off and on fullscreen mode.

### Instance methods on the Document interface

**`Document.exitFullscreen()`**

Requests that the user agent switch from fullscreen mode back to windowed mode. Returns a `Promise` which is resolved once fullscreen mode has been completely shut off.

### Instance methods on the Element interface

**`Element.requestFullscreen()`**

Asks the user agent to place the specified element (and, by extension, its descendants) into fullscreen mode, removing all of the browser's UI elements as well as all other applications from the screen. Returns a `Promise` which is resolved once fullscreen mode has been activated.

## Instance properties

**`Document.fullscreenElement` / `ShadowRoot.fullscreenElement`**

The `fullscreenElement` property tells you the `Element` that's currently being displayed in fullscreen mode on the DOM (or shadow DOM). If this is `null`, the document (or shadow DOM) is not in fullscreen mode.

**`Document.fullscreenEnabled`**

The `fullscreenEnabled` property tells you whether or not it is possible to engage fullscreen mode. This is `false` if fullscreen mode is not available for any reason (such as the `"fullscreen"` feature not being allowed, or fullscreen mode not being supported).

### Obsolete properties

**`Document.fullscreen`**

A Boolean value which is `true` if the document has an element currently being displayed in fullscreen mode; otherwise, this returns `false`.

**Note:** Use the `fullscreenElement` property on the `Document` or `ShadowRoot` instead; if it's not `null`, then it's an `Element` currently being displayed in fullscreen mode.

## Events

**`fullscreenchange`**

Sent to an `Element` when it transitions into or out of fullscreen mode.

**`fullscreenerror`**

Sent to an `Element` if an error occurs while attempting to switch it into or out of fullscreen mode.

## Controlling access

The availability of fullscreen mode can be controlled using a Permissions Policy. The fullscreen mode feature is identified by the string `"fullscreen"`, with a default allowlist value of `"self"`, meaning that fullscreen mode is permitted in top-level document contexts, as well as to nested browsing contexts loaded from the same origin as the top-most document.

## Usage notes

Users can choose to exit fullscreen mode by pressing the ESC (or F11) key, rather than waiting for the site or app to programmatically do so. Make sure you provide, somewhere in your user interface, appropriate user interface elements that inform the user that this option is available to them.

**Note:** Navigating to another page, changing tabs, or switching to another application using any application switcher (or Alt-Tab) will likewise exit fullscreen mode.

## Examples

### Simple fullscreen usage

In this example, a video is presented in a web page. Pressing the Enter key lets the user toggle between windowed and fullscreen presentation of the video.

View Live Example

#### Watching for the Enter key

When the page is loaded, this code is run to set up an event listener to watch for the Enter key.

```js
const video = document.getElementById("video");

// On pressing ENTER call toggleFullScreen method
document.addEventListener("keydown", (e) => {
  if (e.key === "Enter") {
    toggleFullScreen(video);
  }
});
```

#### Toggling fullscreen mode

This code is called by the event handler above when the user hits the Enter key.

```js
function toggleFullScreen(video) {
  if (!document.fullscreenElement) {
    // If the document is not in full screen mode
    // make the video full screen
    video.requestFullscreen();
  } else {
    // Otherwise exit the full screen
    document.exitFullscreen?.();
  }
}
```

This starts by looking at the value of the `document`'s `fullscreenElement` attribute. If the value is `null`, the document is currently in windowed mode, so we need to switch to fullscreen mode; otherwise, it's the element that's currently in fullscreen mode. Switching to fullscreen mode is done by calling `Element.requestFullscreen()` on the `<video>` element.

If fullscreen mode is already active (`fullscreenElement` is not `null`), we call `exitFullscreen()` on the `document` to shut off fullscreen mode.

## Specifications

| Specification |
|---|
| Fullscreen API # ref-for-dom-document-fullscreenelement① |
| Fullscreen API # ref-for-dom-document-fullscreenenabled① |
| Fullscreen API # ref-for-dom-document-exitfullscreen① |
| Fullscreen API # ref-for-dom-element-requestfullscreen① |

## Browser compatibility

### api.Document.fullscreenElement

### api.Document.fullscreenEnabled

### api.Document.exitFullscreen

### api.Element.requestFullscreen
