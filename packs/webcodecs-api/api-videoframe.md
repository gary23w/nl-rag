---
title: "VideoFrame - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/VideoFrame
domain: webcodecs-api
license: CC-BY-SA-4.0
tags: webcodecs api, low-level frame encode, video frame decode, encoded audio chunk
fetched: 2026-07-02
---

# VideoFrame

Baseline

2024

*

Newly available

Since September 2024, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

Want more support for this feature? Tell us why.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

**Note:** This feature is available in Dedicated Web Workers.

The **`VideoFrame`** interface of the Web Codecs API represents a frame of a video.

`VideoFrame` is a transferable object.

## Description

A `VideoFrame` object can be created or accessed in a number of ways. The `MediaStreamTrackProcessor` breaks a media track into individual `VideoFrame` objects.

A `VideoFrame` is an image source and has a constructor that accepts any other canvas source ( an `SVGImageElement`, an `HTMLVideoElement`, an `HTMLCanvasElement`, an `ImageBitmap`, an `OffscreenCanvas`, or another `VideoFrame`). This means that a frame can be created from an image or video element.

A second constructor enables the creation of a `VideoFrame` from its binary pixel representation in an `ArrayBuffer`, a `TypedArray`, or a `DataView`.

Created frames may then turned into a media track, for example with the `MediaStreamTrackGenerator` interface that creates a media track from a stream of frames.

## Constructor

**`VideoFrame()`**

Creates a new `VideoFrame` object.

## Instance properties

**`VideoFrame.format` Read only**

Returns the pixel format of the `VideoFrame`.

**`VideoFrame.codedWidth` Read only**

Returns the width of the `VideoFrame` in pixels, potentially including non-visible padding, and prior to considering potential ratio adjustments.

**`VideoFrame.codedHeight` Read only**

Returns the height of the `VideoFrame` in pixels, potentially including non-visible padding, and prior to considering potential ratio adjustments.

**`VideoFrame.codedRect` Read only**

Returns a `DOMRectReadOnly` with the width and height matching `codedWidth` and `codedHeight`.

**`VideoFrame.visibleRect` Read only**

Returns a `DOMRectReadOnly` describing the visible rectangle of pixels for this `VideoFrame`.

**`VideoFrame.displayWidth` Read only**

Returns the width of the `VideoFrame` when displayed after applying aspect ratio adjustments.

**`VideoFrame.displayHeight` Read only**

Returns the height of the `VideoFrame` when displayed after applying aspect ratio adjustments.

**`VideoFrame.duration` Read only**

Returns an integer indicating the duration of the video in microseconds.

**`VideoFrame.timestamp` Read only**

Returns an integer indicating the timestamp of the video in microseconds.

**`VideoFrame.colorSpace` Read only**

Returns a `VideoColorSpace` object.

**`VideoFrame.flip` Read only**

Returns whether the `VideoFrame` is horizontally mirrored.

**`VideoFrame.rotation` Read only**

Returns the rotation (0, 90, 180, or 270) in degrees clockwise applied to the `VideoFrame`. Arbitrary numbers (including negatives) are rounded to the next quarter turn.

## Instance methods

**`VideoFrame.allocationSize()`**

Returns the number of bytes required to hold the `VideoFrame` as filtered by options passed into the method.

**`VideoFrame.copyTo()`**

Copies the contents of the `VideoFrame` to an `ArrayBuffer`.

**`VideoFrame.clone()`**

Creates a new `VideoFrame` object with reference to the same media resource as the original.

**`VideoFrame.close()`**

Clears all states and releases the reference to the media resource.

**`VideoFrame.metadata()`**

Returns the metadata associated with the `VideoFrame`.

## Examples

In the following example frames are returned from a `MediaStreamTrackProcessor`, then encoded. See the full example and read more about it in the article Video processing with WebCodecs.

```js
let frameCounter = 0;

const track = stream.getVideoTracks()[0];
const mediaProcessor = new MediaStreamTrackProcessor(track);

const reader = mediaProcessor.readable.getReader();
while (true) {
  const result = await reader.read();
  if (result.done) break;

  let frame = result.value;
  if (encoder.encodeQueueSize > 2) {
    // Too many frames in flight, encoder is overwhelmed
    // let's drop this frame.
    frame.close();
  } else {
    frameCounter++;
    const insertKeyframe = frameCounter % 150 === 0;
    encoder.encode(frame, { keyFrame: insertKeyframe });
    frame.close();
  }
}
```

## Specifications

| Specification |
|---|
| WebCodecs # videoframe-interface |

## Browser compatibility
