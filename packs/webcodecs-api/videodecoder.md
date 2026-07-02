---
title: "VideoDecoder - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/VideoDecoder
domain: webcodecs-api
license: CC-BY-SA-4.0
tags: webcodecs api, low-level frame encode, video frame decode, encoded audio chunk
fetched: 2026-07-02
---

# VideoDecoder

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

**Note:** This feature is available in Dedicated Web Workers.

The **`VideoDecoder`** interface of the WebCodecs API decodes chunks of video.

## Constructor

**`VideoDecoder()`**

Creates a new `VideoDecoder` object.

## Instance properties

*Inherits properties from its parent, `EventTarget`.*

**`VideoDecoder.decodeQueueSize` Read only**

An integer representing the number of queued decode requests.

**`VideoDecoder.state` Read only**

Indicates the current state of decoder. Possible values are:

- `"unconfigured"`
- `"configured"`
- `"closed"`

### Events

**`dequeue`**

Fires to signal a decrease in `VideoDecoder.decodeQueueSize`.

## Static methods

**`VideoDecoder.isConfigSupported()`**

Returns a promise indicating whether the provided `VideoDecoderConfig` is supported.

## Instance methods

*Inherits methods from its parent, `EventTarget`.*

**`VideoDecoder.configure()`**

Enqueues a control message to configure the video decoder for decoding chunks.

**`VideoDecoder.decode()`**

Enqueues a control message to decode a given chunk of video.

**`VideoDecoder.flush()`**

Returns a promise that resolves once all pending messages in the queue have been completed.

**`VideoDecoder.reset()`**

Resets all states including configuration, control messages in the control message queue, and all pending callbacks.

**`VideoDecoder.close()`**

Ends all pending work and releases system resources.

## Specifications

| Specification |
|---|
| WebCodecs # videodecoder-interface |

## Browser compatibility
