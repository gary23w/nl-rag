---
title: "MediaStream - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/MediaStream
domain: webrtc
license: CC-BY-SA-2.5
tags: webrtc, rtcpeerconnection, peer-to-peer media, getusermedia, rtc data channel
fetched: 2026-07-02
---

# MediaStream

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2017.

- Learn more
- See full compatibility

The **`MediaStream`** interface of the Media Capture and Streams API represents a stream of media content. A stream consists of several **tracks**, such as video or audio tracks. Each track is specified as an instance of `MediaStreamTrack`.

You can obtain a `MediaStream` object either by using the constructor or by calling functions such as `MediaDevices.getUserMedia()`, `MediaDevices.getDisplayMedia()`, or `HTMLCanvasElement.captureStream()` and `HTMLMediaElement.captureStream()`.

## Constructor

**`MediaStream()`**

Creates and returns a new `MediaStream` object. You can create an empty stream, a stream which is based upon an existing stream, or a stream that contains a specified list of tracks (specified as an array of `MediaStreamTrack` objects).

## Instance properties

*This interface inherits properties from its parent, `EventTarget`.*

**`MediaStream.active` Read only**

A Boolean value that returns `true` if the `MediaStream` is active, or `false` otherwise.

**`MediaStream.id` Read only**

A string containing a 36-character universally unique identifier (UUID) for the object.

## Instance methods

*This interface inherits methods from its parent, `EventTarget`.*

**`MediaStream.addTrack()`**

Stores a copy of the `MediaStreamTrack` given as argument. If the track has already been added to the `MediaStream` object, nothing happens.

**`MediaStream.clone()`**

Returns a clone of the `MediaStream` object. The clone will, however, have a unique value for `id`.

**`MediaStream.getAudioTracks()`**

Returns a list of the `MediaStreamTrack` objects stored in the `MediaStream` object that have their `kind` attribute set to `audio`. The order is not defined, and may not only vary from one browser to another, but also from one call to another.

**`MediaStream.getTrackById()`**

Returns the track whose ID corresponds to the one given in parameters, `trackId`. If no parameter is given, or if no track with that ID does exist, it returns `null`. If several tracks have the same ID, it returns the first one.

**`MediaStream.getTracks()`**

Returns a list of all `MediaStreamTrack` objects stored in the `MediaStream` object, regardless of the value of the `kind` attribute. The order is not defined, and may not only vary from one browser to another, but also from one call to another.

**`MediaStream.getVideoTracks()`**

Returns a list of the `MediaStreamTrack` objects stored in the `MediaStream` object that have their `kind` attribute set to `"video"`. The order is not defined, and may not only vary from one browser to another, but also from one call to another.

**`MediaStream.removeTrack()`**

Removes the `MediaStreamTrack` given as argument. If the track is not part of the `MediaStream` object, nothing happens.

## Events

**`addtrack`**

Fired when a new `MediaStreamTrack` object is added.

**`removetrack`**

Fired when a `MediaStreamTrack` object has been removed.

**`active`**

Fired when the MediaStream is activated.

**`inactive`**

Fired when the MediaStream is inactivated.

## Specifications

| Specification |
|---|
| Media Capture and Streams # mediastream |

## Browser compatibility
