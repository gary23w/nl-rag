---
title: "AudioContext - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/AudioContext
domain: web-audio-api
license: CC-BY-SA-4.0
tags: web audio api, audio node graph, audio context processing, gain oscillator node
fetched: 2026-07-02
---

# AudioContext

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2021.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

The `AudioContext` interface represents an audio-processing graph built from audio modules linked together, each represented by an `AudioNode`.

An audio context controls both the creation of the nodes it contains and the execution of the audio processing, or decoding. You need to create an `AudioContext` before you do anything else, as everything happens inside a context. It's recommended to create one AudioContext and reuse it instead of initializing a new one each time, and it's OK to use a single `AudioContext` for several different audio sources and pipeline concurrently.

## Constructor

**`AudioContext()`**

Creates and returns a new `AudioContext` object.

## Instance properties

*Also inherits properties from its parent interface, `BaseAudioContext`.*

**`AudioContext.baseLatency` Read only**

Returns the number of seconds of processing latency incurred by the `AudioContext` passing the audio from the `AudioDestinationNode` to the audio subsystem.

**`AudioContext.outputLatency` Read only**

Returns an estimation of the output latency of the current audio context.

**`AudioContext.playbackStats` Read only**

Returns an `AudioPlaybackStats` object providing access to duration, underrun, and latency statistics for the `AudioContext`.

**`AudioContext.sinkId` Read only Secure context**

Returns the sink ID of the current output audio device.

## Instance methods

*Also inherits methods from its parent interface, `BaseAudioContext`.*

**`AudioContext.close()`**

Closes the audio context, releasing any system audio resources that it uses.

**`AudioContext.createMediaElementSource()`**

Creates a `MediaElementAudioSourceNode` associated with an `HTMLMediaElement`. This can be used to play and manipulate audio from `<video>` or `<audio>` elements.

**`AudioContext.createMediaStreamSource()`**

Creates a `MediaStreamAudioSourceNode` associated with a `MediaStream` representing an audio stream which may come from the local computer microphone or other sources.

**`AudioContext.createMediaStreamDestination()`**

Creates a `MediaStreamAudioDestinationNode` associated with a `MediaStream` representing an audio stream which may be stored in a local file or sent to another computer.

**`AudioContext.createMediaStreamTrackSource()`**

Creates a `MediaStreamTrackAudioSourceNode` associated with a `MediaStream` representing a media stream track.

**`AudioContext.getOutputTimestamp()`**

Returns a new `AudioTimestamp` object containing two audio timestamp values relating to the current audio context.

**`AudioContext.resume()`**

Resumes the progression of time in an audio context that has previously been suspended/paused.

**`AudioContext.setSinkId()` Secure context**

Sets the output audio device for the `AudioContext`.

**`AudioContext.suspend()`**

Suspends the progression of time in the audio context, temporarily halting audio hardware access and reducing CPU/battery usage in the process.

## Events

**`sinkchange`**

Fired when the output audio device (and therefore, the `AudioContext.sinkId`) has changed.

## Examples

Basic audio context declaration:

```js
const audioCtx = new AudioContext();

const oscillatorNode = audioCtx.createOscillator();
const gainNode = audioCtx.createGain();
const finish = audioCtx.destination;
// etc.
```

## Specifications

| Specification |
|---|
| Web Audio API # AudioContext |

## Browser compatibility
