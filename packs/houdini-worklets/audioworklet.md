---
title: "AudioWorklet - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/AudioWorklet
domain: houdini-worklets
license: CC-BY-SA-4.0
tags: css houdini worklets, worklet global scope, add module worklet, extensible styling engine
fetched: 2026-07-02
---

# AudioWorklet

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2021.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The **`AudioWorklet`** interface of the Web Audio API is used to supply custom audio processing scripts that execute in a separate thread to provide very low latency audio processing.

The worklet's code is run in the `AudioWorkletGlobalScope` global execution context, using a separate Web Audio thread which is shared by the worklet and other audio nodes.

Access the audio context's instance of `AudioWorklet` through the `BaseAudioContext.audioWorklet` property.

## Instance properties

*This interface also inherits properties defined on its parent interface, `Worklet`.*

**`port` Read only**

Returns a `MessagePort` for custom, asynchronous communication between code in the main thread and the global scope of an audio worklet. This allows for custom messages, such as sending and receiving control data or global settings.

## Instance methods

*This interface inherits methods from `Worklet`. The `AudioWorklet` interface does not define any methods of its own.*

## Events

*`AudioWorklet` has no events to which it responds.*

## Examples

See `AudioWorkletNode` for complete examples of custom audio node creation.

## Specifications

| Specification |
|---|
| Web Audio API # AudioWorklet |

## Browser compatibility
