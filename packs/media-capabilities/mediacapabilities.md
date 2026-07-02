---
title: "MediaCapabilities - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/MediaCapabilities
domain: media-capabilities
license: CC-BY-SA-4.0
tags: media capabilities api, decoding playback ability, media codec support query, smooth power-efficient playback
fetched: 2026-07-02
---

# MediaCapabilities

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

**Note:** This feature is available in Web Workers.

The **`MediaCapabilities`** interface of the Media Capabilities API provides information about the decoding abilities of the device, system and browser. The API can be used to query the browser about the decoding abilities of the device based on codecs, profile, resolution, and bitrates. The information can be used to serve optimal media streams to the user and determine if playback should be smooth and power efficient.

The information is accessed through the **`mediaCapabilities`** property of the `Navigator` and `WorkerNavigator` interface.

## Instance methods

**`MediaCapabilities.encodingInfo()`**

When passed a valid media configuration, it returns a promise with information as to whether the media type is supported, and whether encoding such media would be smooth and power efficient.

**`MediaCapabilities.decodingInfo()`**

When passed a valid media configuration, it returns a promise with information as to whether the media type is supported, and whether decoding such media would be smooth and power efficient.

## Specifications

| Specification |
|---|
| Media Capabilities # media-capabilities-interface |

## Browser compatibility
