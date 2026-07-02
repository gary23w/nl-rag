---
title: "ImageCapture: takePhoto() method - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/ImageCapture/takePhoto
domain: image-capture
license: CC-BY-SA-4.0
tags: image capture api, camera photo capture, grab video frame, camera track settings
fetched: 2026-07-02
---

# ImageCapture: takePhoto() method

The **`takePhoto()`** method of the `ImageCapture` interface takes a single exposure using the video capture device sourcing a `MediaStreamTrack` and returns a `Promise` that resolves with a `Blob` containing the data.

## Syntax

```js
takePhoto()
takePhoto(photoSettings)
```

### Parameters

**`photoSettings` Optional**

An object that sets options for the photo to be taken. The available options are:

**`fillLightMode`**

The flash setting of the capture device, one of `"auto"`, `"off"`, or `"flash"`.

**`imageHeight`**

The desired image height as an integer. The user agent selects the closest height value to this setting if it only supports discrete heights.

**`imageWidth`**

The desired image width as an integer. The user agent selects the closest width value to this setting if it only supports discrete widths.

**`redEyeReduction`**

A boolean indicating whether the red-eye reduction should be used if it is available.

### Return value

A `Promise` that resolves with a `Blob`.

### Exceptions

**`InvalidStateError` `DOMException`**

Thrown if `readyState` property of the `MediaStreamTrack` passing in the constructor is not `live`.

**`UnknownError` `DOMException`**

Thrown if the operation can't complete for any reason.

## Examples

This example is extracted from this Simple Image Capture demo. It shows how to use the `Promise` returned by `takePhoto()` to copy the returned `Blob` to an `<img>` element. For simplicity it does not show how to instantiate the `ImageCapture` object.

```js
let takePhotoButton = document.querySelector("button#takePhoto");
let canvas = document.querySelector("canvas");

takePhotoButton.onclick = takePhoto;

function takePhoto() {
  imageCapture
    .takePhoto()
    .then((blob) => {
      console.log("Took photo:", blob);
      img.classList.remove("hidden");
      img.src = URL.createObjectURL(blob);
    })
    .catch((error) => {
      console.error("takePhoto() error: ", error);
    });
}
```

## Specifications

| Specification |
|---|
| MediaStream Image Capture # dom-imagecapture-takephoto |

## Browser compatibility
