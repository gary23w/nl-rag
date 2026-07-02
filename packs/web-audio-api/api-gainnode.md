---
title: "GainNode - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/GainNode
domain: web-audio-api
license: CC-BY-SA-4.0
tags: web audio api, audio node graph, audio context processing, gain oscillator node
fetched: 2026-07-02
---

# GainNode

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

- Learn more
- See full compatibility

The `GainNode` interface represents a change in volume. It is an `AudioNode` audio-processing module that causes a given gain to be applied to the input data before its propagation to the output. A `GainNode` always has exactly one input and one output, both with the same number of channels.

The gain is a unitless value, changing with time, that is multiplied to each corresponding sample of all input channels. If modified, the new gain is instantly applied, causing unaesthetic 'clicks' in the resulting audio. To prevent this from happening, never change the value directly but use the exponential interpolation methods on the `AudioParam` interface.

(The GainNode is increasing the gain of the output.)

| Number of inputs | `1` |
|---|---|
| Number of outputs | `1` |
| Channel count mode | `"max"` |
| Channel count | `2` (not used in the default count mode) |
| Channel interpretation | `"speakers"` |

## Constructor

**`GainNode()`**

Creates and returns a new `GainNode` object. As an alternative, you can use the `BaseAudioContext.createGain()` factory method; see Creating an AudioNode.

## Instance properties

*Inherits properties from its parent, `AudioNode`*.

**`GainNode.gain` Read only**

An a-rate `AudioParam` representing the amount of gain to apply. You have to set `AudioParam.value` or use the methods of `AudioParam` to change the effect of gain.

## Instance methods

*No specific method; inherits methods from its parent, `AudioNode`*.

## Example

See `BaseAudioContext.createGain()` for example code showing how to use an `AudioContext` to create a `GainNode`.

## Specifications

| Specification |
|---|
| Web Audio API # GainNode |

## Browser compatibility
