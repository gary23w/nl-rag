---
title: "AudioEncoder - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/AudioEncoder
domain: webcodecs-api
license: CC-BY-SA-4.0
tags: webcodecs api, low-level frame encode, video frame decode, encoded audio chunk
fetched: 2026-07-02
---

# AudioEncoder

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

**Note:** This feature is available in Dedicated Web Workers.

The **`AudioEncoder`** interface of the WebCodecs API encodes `AudioData` objects.

## Constructor

**`AudioEncoder()`**

Creates a new `AudioEncoder` object.

## Instance properties

*Inherits properties from its parent, `EventTarget`.*

**`AudioEncoder.encodeQueueSize` Read only**

An integer representing the number of encode queue requests.

**`AudioEncoder.state` Read only**

Represents the state of the underlying codec and whether it is configured for encoding.

### Events

**`dequeue`**

Fires to signal a decrease in `AudioEncoder.encodeQueueSize`.

## Static methods

**`AudioEncoder.isConfigSupported()`**

Returns a promise indicating whether the provided `AudioEncoderConfig` is supported.

## Instance methods

*Inherits methods from its parent, `EventTarget`.*

**`AudioEncoder.configure()`**

Enqueues a control message to configure the audio encoder for encoding chunks.

**`AudioEncoder.encode()`**

Enqueues a control message to encode a given `AudioData` objects.

**`AudioEncoder.flush()`**

Returns a promise that resolves once all pending messages in the queue have been completed.

**`AudioEncoder.reset()`**

Resets all states including configuration, control messages in the control message queue, and all pending callbacks.

**`AudioEncoder.close()`**

Ends all pending work and releases system resources.

## Specifications

| Specification |
|---|
| WebCodecs # audioencoder-interface |

## Browser compatibility
