---
title: "Picture-in-Picture API - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Picture-in-Picture_API
domain: picture-in-picture
license: CC-BY-SA-4.0
tags: picture in picture api, floating video window, detached video overlay, enter pip mode
fetched: 2026-07-02
---

# Picture-in-Picture API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

The **Picture-in-Picture API** allow websites to create a floating, always-on-top video window. This allows users to continue consuming media while they interact with other sites or applications on their device.

**Note:** The Document Picture-in-Picture API extends the Picture-in-Picture API to allow the always-on-top window to be populated with *any* arbitrary HTML content, not just a video.

**Note:** You can run code when the always-on-top window is programmatically opened, using the `enterpictureinpicture` event. However, this event isn't fired when the browser itself (rather than your code) triggers moving content into the always-on-top window. This can occur, for example, due to the content being occluded, by the displayed tab being switched, or by the user selecting a "picture-in-picture" option from a video's context menu or the browser chrome.

To run code in response to such actions, set up a media session action handler using `MediaSession.setActionHandler()` with a `type` of `enterpictureinpicture`.

## Interfaces

**`PictureInPictureWindow`**

Represents the floating video window; contains `width` and `height` properties, and an `onresize` event handler property.

**`PictureInPictureEvent`**

Represents picture-in-picture-related events, including `enterpictureinpicture`, `leavepictureinpicture` and `resize`.

## Instance methods

The Picture-in-Picture API adds methods to the `HTMLVideoElement` and `Document` interfaces to allow toggling of the floating video window.

### Instance methods on the HTMLVideoElement interface

**`HTMLVideoElement.requestPictureInPicture()`**

Requests that the user agent enters the video into picture-in-picture mode

### Instance methods on the Document interface

**`Document.exitPictureInPicture()`**

Requests that the user agent returns the element in picture-in-picture mode back into its original box.

## Instance properties

The Picture-in-Picture API augments the `HTMLVideoElement`, `Document`, and `ShadowRoot` interfaces with properties that can be used to determine if the floating video window mode is supported and available, if picture-in-picture mode is currently active, and which video is floating.

### Instance properties on the HTMLVideoElement interface

**`HTMLVideoElement.disablePictureInPicture`**

The `disablePictureInPicture` property will provide a hint to the user agent to not suggest the picture-in-picture to users or to request it automatically.

### Instance properties on the Document interface

**`Document.pictureInPictureEnabled`**

The `pictureInPictureEnabled` property tells you whether or not it is possible to engage picture-in-picture mode. This is `false` if picture-in-picture mode is not available for any reason (e.g., the `"picture-in-picture"` feature has been disallowed, or picture-in-picture mode is not supported).

### Instance properties on the Document or ShadowRoot interfaces

**`Document.pictureInPictureElement` / `ShadowRoot.pictureInPictureElement`**

The `pictureInPictureElement` property tells you which `Element` is currently being displayed in the floating window (or in the shadow DOM). If this is `null`, the document (or shadow DOM) has no node currently in picture-in-picture mode.

## Events

*The Picture-in-Picture API defines three events, which can be used to detect when picture-in-picture mode is toggled and when the floating video window is resized.*

**`enterpictureinpicture`**

Sent to a `HTMLVideoElement` when it enters picture-in-picture mode.

**`leavepictureinpicture`**

Sent to a `HTMLVideoElement` when it leaves picture-in-picture mode.

**`resize`**

Sent to a `PictureInPictureWindow` when it changes size.

## Adding Controls

If media action handlers have been set via the Media Session API, then appropriate controls for those actions will be added by the browser to the picture-in-picture overlay. For example, if a `"nexttrack"` action has been set, then a skip button might be displayed in the picture-in-picture view. There is no support for adding custom HTML buttons or controls.

## Controlling styling

The `:picture-in-picture` CSS pseudo-class matches the video element currently in picture-in-picture mode, allowing you to configure your stylesheets to automatically adjust the size, style, or layout of content when a video switches back and forth between picture-in-picture and traditional presentation modes.

## Controlling access

The availability of picture-in-picture mode can be controlled using Permissions Policy. The picture-in-picture mode feature is identified by the string `"picture-in-picture"`, with a default allowlist value of `*`, meaning that picture-in-picture mode is permitted in top-level document contexts, as well as to nested browsing contexts loaded from the same origin as the top-most document.

## Examples

### Toggling picture-in-picture mode

In this example, we have a `<video>` element in a web page, a `<button>` to toggle picture-in-picture, and an element to log information relevant for the example. The `<button>` element is `disabled` initially until we've determined browser support.

```html
<video
  src="/shared-assets/videos/friday.mp4"
  id="video"
  muted
  controls
  loop
  width="300"></video>

<button id="pip-button" disabled>Toggle PiP</button>
<pre id="log"></pre>
```

```css
body {
  font:
    14px "Open Sans",
    sans-serif;
  padding: 0.5em;
}

button {
  display: block;
  margin-block: 1rem;
}
```

We first check if the browser supports PiP with `document.pictureInPictureEnabled`, and if it's not supported, we log that information to the `<pre>` element. If it is available in the browser, we can enable the toggle to enter and exit PiP.

For the controls, an event listener on the `<button>` element calls a `togglePictureInPicture()` function that we've defined. In `togglePictureInPicture()`, an `if` statement checks the value of the `document`'s `pictureInPictureElement` attribute.

- If the value is `null`, no video is in a floating window, so we can request the video to enter picture-in-picture mode. We do that by calling `HTMLVideoElement.requestPictureInPicture()` on the `<video>` element.
- If the value is not `null`, an element is currently in picture-in-picture mode. We can then call `document.exitPictureInPicture()` to bring the video back into its initial box, exiting picture-in-picture mode.

```js
const video = document.getElementById("video");
const pipButton = document.getElementById("pip-button");
const log = document.getElementById("log");

if (document.pictureInPictureEnabled) {
  pipButton.removeAttribute("disabled");
} else {
  log.innerText = "PiP not supported. Check browser compatibility for details.";
}

function togglePictureInPicture() {
  if (document.pictureInPictureElement) {
    document.exitPictureInPicture();
  } else {
    video.requestPictureInPicture();
  }
}

pipButton.addEventListener("click", togglePictureInPicture);
```

```css
:picture-in-picture {
  outline: 5px dashed green;
}
```

Clicking the "Toggle PiP" button lets the user toggle between playing the video in the page and in a floating window:

## Specifications

| Specification |
|---|
| Picture-in-Picture # interface-picture-in-picture-window |

## Browser compatibility
