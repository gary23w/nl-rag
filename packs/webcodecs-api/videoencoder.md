---
title: "VideoEncoder - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/VideoEncoder
domain: webcodecs-api
license: CC-BY-SA-4.0
tags: webcodecs api, low-level frame encode, video frame decode, encoded audio chunk
fetched: 2026-07-02
---

# VideoEncoder

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

**Note:** This feature is available in Dedicated Web Workers.

The **`VideoEncoder`** interface of the WebCodecs API encodes `VideoFrame` objects into `EncodedVideoChunk`s.

## Constructor

**`VideoEncoder()`**

Creates a new `VideoEncoder` object.

## Instance properties

*Inherits properties from its parent, `EventTarget`.*

**`VideoEncoder.encodeQueueSize` Read only**

An integer representing the number of encode queue requests.

**`VideoEncoder.state` Read only**

Represents the state of the underlying codec and whether it is configured for encoding.

### Events

**`dequeue`**

Fires to signal a decrease in `VideoEncoder.encodeQueueSize`.

## Static methods

**`VideoEncoder.isConfigSupported()`**

Returns a promise indicating whether the provided `VideoEncoderConfig` is supported.

## Instance methods

*Inherits methods from its parent, `EventTarget`.*

**`VideoEncoder.configure()`**

Asynchronously prepares the encoder to accept video frames for encoding with the specified parameters.

**`VideoEncoder.encode()`**

Asynchronously encodes a `VideoFrame`.

**`VideoEncoder.flush()`**

Returns a promise that resolves once all pending encodes have been completed.

**`VideoEncoder.reset()`**

Cancels all pending encodes and callbacks.

**`VideoEncoder.close()`**

Ends all pending work and releases system resources.

## Specifications

| Specification |
|---|
| WebCodecs # videoencoder-interface |

## Browser compatibility
