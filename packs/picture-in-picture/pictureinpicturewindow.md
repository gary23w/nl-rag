---
title: "PictureInPictureWindow - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/PictureInPictureWindow
domain: picture-in-picture
license: CC-BY-SA-4.0
tags: picture in picture api, floating video window, detached video overlay, enter pip mode
fetched: 2026-07-02
---

# PictureInPictureWindow

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

The **`PictureInPictureWindow`** interface represents an object able to programmatically obtain the **`width`** and **`height`** and **`resize event`** of the floating video window.

An object with this interface is obtained using the `HTMLVideoElement.requestPictureInPicture()` promise return value.

## Instance properties

*The `PictureInPictureWindow` interface doesn't inherit any properties.*

**`PictureInPictureWindow.width` Read only**

Determines the width of the floating video window.

**`PictureInPictureWindow.height` Read only**

Determines the height of the floating video window.

## Instance methods

*The `PictureInPictureWindow` interface doesn't inherit any methods.*

## Events

*The `PictureInPictureWindow` interface doesn't inherit any events.*

**`resize`**

Sent to a `PictureInPictureWindow` when the floating video window is resized.

## Examples

Given a `<button>` and a `<video>`, clicking the button will make the video enter the picture-in-picture mode; we then attach an event to print the floating video window dimensions to the console.

```js
const button = document.querySelector("button");
const video = document.querySelector("video");

function printPipWindowDimensions(evt) {
  const pipWindow = evt.target;
  console.log(
    `The floating window dimensions are: ${pipWindow.width}x${pipWindow.height}px`,
  );
  // will print:
  // The floating window dimensions are: 640x360px
}

button.onclick = () => {
  video.requestPictureInPicture().then((pictureInPictureWindow) => {
    pictureInPictureWindow.onresize = printPipWindowDimensions;
  });
};
```

## Specifications

| Specification |
|---|
| Picture-in-Picture # interface-picture-in-picture-window |

## Browser compatibility
